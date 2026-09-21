# -*- coding: utf-8 -*-
"""把语料 `## Functional changes` 里的版本事实抽出来，生成 `wiki/versions/` 的版本页。

**纯脚本，零 LLM。** 依据是 `schema.md` §4 的铁律：
「脚本能产出的，不许调 LLM。参考手册的条目不需要模型重写，它需要的是被索引。」

（§4 的表格里 version 页那行原本写的是「LLM（批量，按簇）」——**它和同节的铁律
自相矛盾**。语料写的是 `- SmarTest 7.2.0: <一句话>`，分组、排序、出处都机械，
没有一处需要模型判断。**2026-09-18 已把那一行改成脚本。**）

---

**这个脚本要绕开的三个坑**（都是先量了数据才看见的，不是猜的）：

**坑一：`Introduced before SmarTest 6.3.2` 不是「6.3.2 的变更」。**
2,677 条可用性行全部写的是 6.3.2，措辞是 `before`——
它的意思是「**在文档覆盖范围开始之前就有了**」，是个哨兵值。
若照字面把它当成「6.3.2 引入了 2,677 个功能」，**这一页就是纯编的**，
而且看上去还挺像回事（数字大、格式齐）。**处置：这一页单列为「基线」，
并在页首把话说明白。**

**坑二：`## Functional changes` 段落会吞掉文件末尾的脚注块。**
语料生成器把脚注定义（`[1)](<>) …`）挂在文件最后，而 `Functional changes`
按模板顺序正好是最后一个 `## ` 段——于是 171 篇的脚注连同脚注里的
`- CFIM: Force current…` 清单**全被算进了本段**。
抽出来的 10,303 条里有 1,095 条是这么来的。**处置：遇到脚注定义行即截断。**
（这是语料结构如此，不是脚本 bug——raw 一个字节不动，此处记下。）

**坑三：版本号会撞车，页名不能只用版本号。**
`schema.md` §2.7 举的例是 `7.10.3.md`。但 `Functional changes` 里不止
SmarTest 一条产品线——**SmarTest 7.5.0 和 SmartRDI 7.5.0 都存在**，
同名不同物。**处置：页名一律带产品前缀 `<product>-<version>.md`。**

---
用：`python versions.py`（抽 + 出页）
    `python versions.py --facts`（只抽成 csv，不出页）
"""
import collections
import csv
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
BASE = Path(r'F:\master-dev\understand-anything-wiki')
OUT = BASE / 'extract'
WIKI = BASE / 'wiki'
VDIR = WIKI / 'versions'

# 本目录的目录页叫什么。**不能叫 `index.md`**（第一版就叫这个，2026-09-18 改掉）。
#
# 两条理由，第二条是硬的：
#
# 1. **§5 要求 slug 合 `^[a-z0-9]+([-.][a-z0-9]+)*$`，而链接里必须写得下它。**
#    `[[versions/index]]` 不合规（`/` 不在字符集里），第九类当场报 ❌。
# 2. **页面身份就是文件名（stem），`index` 这个 stem 已经被 `wiki/index.md` 占了。**
#    全库的检查一律按 stem 建集合（第八/九类的 `have`、第六类的跳过、第十一类的 lookup），
#    两个文件同一个 stem，**集合把它们当同一个东西**——谁被谁遮住取决于遍历顺序。
#    §13 那条「老建重复页」的反面就是这样：**看不见的重复比看得见的更坏。**
#
# 名字取 §7 给的子索引命名法 `index-<类型>`。
IDX_NAME = 'index-versions.md'

# 产品线 → 页名用的 slug。**顺序即页内小节顺序：SmarTest 是主角，排第一。**
PROD = [('SmarTest', 'smartest'), ('MTP', 'mtp'), ('SmartRDI', 'smartrdi'),
        ('TP360', 'tp360'), ('SmartProd', 'smartprod')]
PROD_ALT = '|'.join(p for p, _ in PROD)
SLUG_OF = dict(PROD)

# 脚注定义：`[1)](<>) …` / `[2)](<#fnsrc_2>) …`。**行首匹配即截断本段。**
FN_DEF = re.compile(r'^\[\d+\)\]\(<')

# 语料编码损坏：UTF-8 的三字节标点被按 GBK 读成了两字。
# `鈥` 是 U+2011（非断行连字符）等字符的头两个字节（E2 80），
# **第三个字节和后面那个 ASCII 字符合起来成了第二个坏字**——
# 所以 `鈥慴` = `‑b`、`鈥慶` = `‑c`（**那个字母没丢，是并进坏字里了**）。
# 已建页面里的对照表：[[pogo-block-compatibility]]。
MOJIBAKE = re.compile(r'鈥.')

# 版本号可出现多次，分隔符有 `/` 也有 `and`：
#   `Introduced in SmarTest 7.4.0 / 8.1.0`、`Introduced in SmarTest 7.10.0 and 7.6.1`
#
# **这里踩了两个坑，都是「一个字没写」造成的，一并记着：**
#
# ① 第一版的可用性正则写的是 `(before\s+)?`，**没写 `in`**。
#    结果凡是 `Introduced in SmarTest X` 的行**一条都没匹配上**——
#    3,996 条被判成「没归类」。而 `Introduced before …` 那 2,677 条照样匹配，
#    **所以「base 有数、intro 是 0」这件事看起来只像「数据就这样」。**
#    这正是本仓库反复记的那个病：**判据比它该覆盖的范围窄，窄掉的那块一直是绿的。**
#
# ② 版本列表原来只按 `/` 切，`and` 连接的版本整串成了一个版本号，
#    于是 `7.10.0 and 7.6.1` 会生成一个**根本不存在的版本**。
VER = r'[\d.,]+[A-Za-z]?(?:-\d+)?'
VER_SPLIT = re.compile(r'\s*(?:/|and)\s*')
VER_LIST = rf'{VER}(?:\s*(?:/|and)\s*{VER})*'
# `- Introduced in SmarTest 7.2.0` / `- Introduced before SmarTest 6.3.2`
# / `- Available in MTP 3.4.0`。`before` 与非 before 要分开——见坑一。
RE_AVAIL = re.compile(
    rf'^(Introduced|Available|Supported|Added)\s+(before\s+|in\s+|since\s+|with\s+)?'
    rf'({PROD_ALT})\s+({VER_LIST})\s*$', re.I)
# `- SmarTest 7.2.3.9 / 7.3.4.4 / 7.4.1.1: New parameter: xxx`（多版本，斜杠分隔）
RE_CHANGE = re.compile(rf'^({PROD_ALT})\s+({VER_LIST})\s*[:：]\s*(.+)$')
# 版本号里混进逗号的：语料有 `SmarTest 7.6,0: …`。**只在做 key 时归一，
# 正文照原样印**，并在页上记一笔——不许悄悄替语料改字。
RE_COMMA = re.compile(r'^([\d.]+),(\d+)$')


def norm_ver(v):
    """版本号 → 排序/分组用的 key。**只归一 `7.6,0` 这种逗号笔误。**

    返回 `(key, 是否归一过)`——调用方要把归一过的那几处**印出来**，
    否则「脚本替我改了语料」这件事就没人知道。
    """
    v = v.strip()
    m = RE_COMMA.match(v)
    if m:
        return f'{m.group(1)}.{m.group(2)}', True
    return v, False


def vkey(v):
    """版本 → 可排序的元组。`7.10.3` 要排在 `7.4.0` 后面，字符串排不出来。"""
    return tuple(int(x) if x.isdigit() else -1 for x in re.findall(r'\d+', v))


def load_facts():
    """读过 `sections.jsonl`，返回 `(facts, 未归类, 归一记录)`。

    `facts` 每项：`{prod, slug, ver, kind, text, doc, line}`。
    `kind` 三种：
      - `change`  —— 该版本**改了**什么（`SmarTest X: …`）
      - `intro`   —— 该版本**新引入**了什么（`Introduced in SmarTest X`）
      - `base`    —— **文档范围之前就有**（`Introduced before SmarTest 6.3.2`）
    """
    facts, odd, renorm = [], [], []
    with (OUT / 'sections.jsonl').open(encoding='utf-8') as f:
        for ln in f:
            r = json.loads(ln)
            if r.get('group') != 'version':
                continue
            for raw in r['body'].splitlines():
                s = raw.strip()
                if FN_DEF.match(s):     # 坑二：脚注块开始，本节内容到此为止
                    break
                if not (s.startswith('- ') or s.startswith('* ')):
                    continue
                b = s[2:].strip()

                m = RE_AVAIL.match(b)
                if m:
                    _, kw, prod, vers = m.groups()
                    is_base = bool(kw) and kw.strip().lower() == 'before'
                    # 可用性行也可能是多版本（`Introduced in SmarTest 7.4.0 / 8.1.0`），
                    # **每个版本都要落到自己页上**，不然 8.1.0 那页就少了这一条。
                    for one in VER_SPLIT.split(vers):
                        key, changed = norm_ver(one)
                        if changed:
                            renorm.append((prod, one, key, r['doc']))
                        facts.append({
                            'prod': prod, 'slug': SLUG_OF[prod], 'ver': key,
                            'kind': 'base' if is_base else 'intro',
                            'text': b, 'doc': r['doc'], 'line': r['line']})
                    continue

                m = RE_CHANGE.match(b)
                if m:
                    prod, vers, text = m.groups()
                    for one in VER_SPLIT.split(vers):
                        key, changed = norm_ver(one)
                        if changed:
                            renorm.append((prod, one, key, r['doc']))
                        facts.append({
                            'prod': prod, 'slug': SLUG_OF[prod], 'ver': key,
                            'kind': 'change', 'text': b, 'doc': r['doc'],
                            'line': r['line']})
                    continue

                odd.append({'text': b, 'doc': r['doc'], 'line': r['line']})
    return facts, odd, renorm


def titles():
    """`rel → H1 标题`。出处的链接文字用它——**没有标题就退回文件名**，
    但要在页面上看得出来是文件名（加反引号），不能冒充标题。"""
    out = {}
    with (OUT / 'docs.jsonl').open(encoding='utf-8') as f:
        for ln in f:
            d = json.loads(ln)
            out[d['rel']] = d.get('title') or None
    return out


def src_link(rel, ttl):
    """出处链接。**`rel` 原样进 URL，显示文字优先用 H1。**"""
    name = rel.rsplit('/', 1)[-1]
    if not ttl:
        ttl = f'`{name}`'
    return f'[{ttl}](<{rel}>)'


def write_facts(facts, odd):
    p = OUT / 'version-facts.csv'
    with p.open('w', encoding='utf-8', newline='') as f:
        f.write('# 语料 `## Functional changes` 的版本事实。**由 extract/versions.py 写，不许手改。**\n')
        f.write('# kind: change=该版改了什么 / intro=该版新引入 / base=文档范围之前就有\n')
        w = csv.writer(f)
        w.writerow(['product', 'version', 'kind', 'text', 'doc', 'line'])
        for r in sorted(facts, key=lambda r: (r['prod'], vkey(r['ver']), r['kind'],
                                              r['doc'], r['line'])):
            w.writerow([r['prod'], r['ver'], r['kind'], r['text'], r['doc'], r['line']])
    print(f'✅ {p.name}：{len(facts):,} 条')
    if odd:
        q = OUT / 'version-unclassified.csv'
        with q.open('w', encoding='utf-8', newline='') as f:
            f.write('# 抽不出版本号的条目。**不许静默丢**，列出来人看。\n')
            w = csv.writer(f)
            w.writerow(['text', 'doc', 'line'])
            for r in odd:
                w.writerow([r['text'], r['doc'], r['line']])
        print(f'⚠️  {q.name}：{len(odd)} 条没归入任何版本——**没有静默丢掉**')

    print(f'   共 {len(facts):,} 条，按产品线：')
    for prod, slug in PROD:
        n = sum(1 for r in facts if r['prod'] == prod)
        vs = {r['ver'] for r in facts if r['prod'] == prod}
        if n:
            print(f'     {prod:10s} {n:5,d} 条 / {len(vs):3d} 个版本')
    return len(facts)


# ---------------------------------------------------------------------------
# 出页
# ---------------------------------------------------------------------------
TODAY = '2026-09-18'          # 与 schema.md / 各页用的日期口径一致
BASE_SENTINEL = '6.3.2'       # 见坑一：`Introduced before SmarTest 6.3.2`
# frontmatter `sources:` 的条数上限。
#
# **为什么不列全**：7.2.0 那页涉及 144 篇，逐篇列进 frontmatter 要 144 行，
# **正文被推到 200 行之后**——agent 读一页先啃两百行清单。
# 而本页**每一条后面都已经挂着自己的出处链接**，逐条可追，
# 所以 frontmatter 这份是**冗余的**，它的作用只剩「满足 schema §6 的必填」。
# 处置：列前 30 篇，并在页里明说「完整出处看正文每条的链接」——
# **是一处有意的偏离，不是漏列。**
SRC_CAP = 30

HEAD_NOTE = (
    '> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**'
    '——分组、排序、出处都是脚本算的，**没有一句是模型写的**。\n'
    '> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。\n'
    '>\n'
    '> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。\n'
    '> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。')


def read_created(p):
    """取已有页面的 `created:`——**重跑时不许把建页日期改成今天**。"""
    if not p.exists():
        return TODAY
    for ln in p.read_text(encoding='utf-8').splitlines()[:12]:
        if ln.startswith('created:'):
            return ln.split(':', 1)[1].strip()
    return TODAY


def render(prod, ver, items, base_items, ttl):
    """一页 → 文本。`items` 是本版真条目，`base_items` 只有 6.3.2 那个哨兵有。

    ---

    **这个函数的第一版吞掉过 2,677 条，记在这里。**

    第一版的分支写的是「**只有** base 条目、没有真变更」才走基线页，
    而 6.3.2 那组**同时有 13 条真变更 + 20 条 `Introduced in`**——
    于是基线分支不成立，`base_items` 就**只被用来数出处文档数**（算出 2,698 篇），
    **2,677 条本身一个字都没印出来**。

    页面看上去完全正常：小节齐、出处齐、数字还挺大。
    **唯一不对劲的地方是「出处说 2,698 篇，正文里只有 33 条」**——
    两个数摆在同一页上对不上。**是这两个数互相打架才露的馅，不是哪条检查发现的。**

    修法：base 条目**不再走单独分支**，改成**永远单独成节**——
    有真条目时它排在这些条目后面，没真条目时它就是全页唯一内容。
    **吞掉和「不列」长得一样，所以「不列」必须有一节明说。**
    """
    slug = SLUG_OF[prod]
    p = VDIR / f'{slug}-{ver}.md'
    # **出处文档数只数本页真列出来的条目**——基线那 2,677 条不在正文里，
    # 就不许进这个数，否则又是「印出来的数不是数出来的数」。
    docs = sorted({r['doc'] for r in items})
    base_docs = sorted({r['doc'] for r in base_items})

    out = ['---', 'type: version', f'title: {prod} {ver} — 版本页',
           f'tags: [version, {slug}]', 'related: []', 'sources:']
    for d in docs[:SRC_CAP]:
        out.append(f'  - {d}')
    if len(docs) > SRC_CAP:
        out.append(f'  # 本页共涉及 {len(docs)} 篇文档。上面只列了前 {SRC_CAP} 篇——'
                   '**完整出处是正文每条后面的链接**，')
        out.append('  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。'
                   '**这是有意的截断，不是漏列。**')
    out += [f'created: {read_created(p)}', f'updated: {TODAY}',
            'verified: doc-only', '---', '', f'# {prod} {ver}', '', HEAD_NOTE]
    # 两种条目同页时，**得先把「别读混」说在头里**——
    # 一批是「这一版改的」，另一批是「这一版之前就有的」，**方向正好相反**。
    if base_items and items:
        out += ['', f'> ⚠️ **本页末尾另有一批 `Introduced before SmarTest {ver}` 的条目'
                f'（{len(base_items):,} 条），那批不是本版的变更。**'
                '读之前先看那一节的开头。']

    chg = [r for r in items if r['kind'] == 'change']
    intro = [r for r in items if r['kind'] == 'intro']

    def show(rs):
        # 同一篇文档的改动排在一起，读起来才知道「这篇一共变了哪几处」
        for r in sorted(rs, key=lambda r: (r['doc'], r['line'])):
            t = ttl.get(r['doc'])
            name = t if t else f'`{r["doc"].rsplit("/", 1)[-1]}`'
            out.append(f'- [{name}](<{r["doc"]}>) —— {r["text"]}')
        out.append('')

    if chg:
        out += ['', f'## 这一版改了什么（{len(chg)} 条）', '',
                f'格式：**出处文档 —— 语料原条目**。条目本身带 `{prod} {ver}:` 前缀，'
                '**那是原文的一部分，没有去掉**。', '']
        show(chg)
    if intro:
        out += ['', f'## 这一版新引入（{len(intro)} 条）', '',
                '语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。'
                '条目短，所以**文档放前面、原句放后面**：', '']
        show(intro)
    if not chg and not intro:
        out += ['', '## 这一版没有条目', '',
                '语料里没有任何一条 `Functional changes` 指到这个版本号。', '']

    # 基线节：**永远单独成节，永不吞**。见 `render()` 的 docstring。
    if base_items:
        out += ['', f'## ⚠️ 另一批：`Introduced before SmarTest {ver}`'
                f'（{len(base_items):,} 条，**不是本版变更**）', '',
                f'语料里有 **{len(base_items):,} 条**可用性行写的是同一个版本号，'
                f'措辞都是 `Introduced before SmarTest {ver}`——**是 `before`，不是 `in`**。', '',
                '它的意思是「**在本文档集覆盖范围开始之前就已经有了**」，'
                '**不是「这个版本引入了它」**。这个版本号在这里是个**哨兵值**。', '',
                f'**所以本节不逐条列出这 {len(base_items):,} 条。** 两个理由：', '',
                f'1. 照字面列出来，就等于宣称「{ver} 新增了 {len(base_items):,} 个功能」'
                '——**那是一条彻头彻尾的假信息，而且格式看着还挺齐整**，'
                '正是本 wiki 最该防的那种错（schema §11）。',
                f'2. 这 {len(base_items):,} 条合起来约等于**整个产品的清点**'
                f'（{len(base_docs):,} 篇文档），逐条铺开就是把目录树镜像一遍，'
                'schema §3 明确不许。', '',
                '**要查某篇文档「是不是在这个版本之前就有」**，用机器索引：'
                '`extract/version-facts.csv` 里 `kind=base` 的行，`doc` 列即文档路径。', '',
                '**要查某个功能哪版才有**，看**它自己那页的 `## 版本` 段**，'
                '或在本目录里找对应版本页。', '']

    out += ['', '## 出处', '',
            f'- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 '
            f'{len(items)} 条**，涉及 **{len(docs)} 篇**文档。']
    if base_items:
        out.append(f'- 另有 `kind=base` 的 **{len(base_items):,} 条 / '
                   f'{len(base_docs):,} 篇**（`Introduced before {ver}`），'
                   '**见上一节，正文里没有逐条列出**。')
    out += ['- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：'
            '`extract/version-facts.csv`。',
            '- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。'
            '若要据此下结论，请点开对应出处链接核对。']
    # **语料编码损坏要逐页点名，但只在真出现时报。**
    # 全语料 528 篇有此问题（见 schema §11.2），**不在这里写死总数**——
    # 写死了就又是一条会过期的绿。**只报本页实际出现的形态。**
    bad = collections.Counter()
    for r in items:
        for m in re.finditer(MOJIBAKE, r['text']):
            bad[m.group(0)] += 1
    if bad:
        forms = '、'.join(f'`{k}`（{v} 处）' for k, v in bad.most_common(8))
        out += ['', '## ⚠️ 本页出现的语料编码损坏', '',
                f'本页条目里有 **{sum(bad.values())} 处**「`鈥`」字样：{forms}。', '',
                '**这是 raw 自带的编码损坏，不是本页打错、也不是转录出错。**'
                '损坏的成因与对照表见 [[pogo-block-compatibility]]，'
                '同族实例见 [[dps128-dps64-cards]] 与 [[xps256-programming-dps-operating-mode]]。', '',
                '**本页照原样转录**（raw 一个字节不动，schema §1.1）。'
                '**代价是：拿修好的字去 raw 里搜是搜不到的**，要搜坏掉的那个形态。']
    return p, '\n'.join(out).rstrip() + '\n'


def write_page(p, text):
    """**内容没变就不写**——不然每次重跑都刷新 `updated:`，diff 全是噪声。"""
    if p.exists() and p.read_text(encoding='utf-8') == text:
        return False
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')
    return True


def index_rows(facts):
    """目录页那张表的原料：`rows[产品线] = [(版本, 条目数, 涉及文档数, 页名)]`。

    **为什么单独抽出来**：它原来是 `build()` 里的一个局部变量，
    于是「目录页有没有跟上那 142 个版本页」**只能靠人看**。
    抽出来之后，`check_version_fresh` 能用**同一个函数**重算一遍目录页正文，
    和磁盘上的逐字节比——**这就是目录页的对账方式**（它没有 `sources`，见下）。
    """
    grp = collections.defaultdict(list)
    for r in facts:
        grp[(r['prod'], r['ver'])].append(r)
    rows = collections.defaultdict(list)
    for (prod, ver), items in sorted(grp.items(),
                                     key=lambda kv: (kv[0][0], vkey(kv[0][1]))):
        rows[prod].append((ver, len(items), len({r['doc'] for r in items}),
                           f'{SLUG_OF[prod]}-{ver}.md'))
    return rows


def render_index(facts):
    """`index-versions.md` 的全文。**`build()` 与对账脚本调的是同一个它。**

    两份实现就是两份规格——这一条在本仓库已经栽过多次（§13.1 第十一、十二次）。
    """
    rows = index_rows(facts)
    idx = ['---', 'type: version', 'title: 版本页 — Index', 'tags: [version, index]',
           'related: []', 'sources:',
           '  # 本页是 `wiki/versions/` 的目录页，条目来自机器清单而不是 raw 文档，',
           '  # 所以这里不列 sources——每一页自己的 `sources:` 才是出处。',
           f'created: {read_created(VDIR / IDX_NAME)}', f'updated: {TODAY}',
           'verified: doc-only', '---', '',
           '# 版本页 — Index', '',
           '**这个目录回答「这个功能哪一版才有 / 哪一版变了」。**', '',
           '- 全部条目**原样转录自语料的 `## Functional changes` 段落**，'
           '由 `extract/versions.py` 机械分组，**零 LLM**。',
           '- **每页只说明「文档这么写」**，不说明「机台这样」（schema §11）。',
           '- 机器可读全量：`extract/version-facts.csv`'
           '（`product, version, kind, text, doc, line`）。', '',
           '**`kind` 三态**：`change` = 该版改了什么；`intro` = 该版新引入；'
           '`base` = 文档范围之前就有（**只有 6.3.2 一个哨兵值**，见该页说明）。', '']
    for prod, _ in PROD:
        if prod not in rows:
            continue
        rs = rows[prod]
        idx += [f'## {prod}（{len(rs)} 个版本）', '',
                '| 版本 | 条目 | 涉及文档 | 页 |', '|---|---:|---:|---|']
        for ver, n, nd, name in rs:
            idx.append(f'| {ver} | {n} | {nd} | [[{name[:-3]}]] |')
        idx.append('')
    return '\n'.join(idx).rstrip() + '\n'


def build(facts, ttl):
    """出页 + 出本目录的 index。返回 `(页数, 新建, 改写)`。"""
    grp = collections.defaultdict(list)
    for r in facts:
        grp[(r['prod'], r['ver'])].append(r)
    new = chg = 0
    for (prod, ver), items in sorted(grp.items(),
                                     key=lambda kv: (kv[0][0], vkey(kv[0][1]))):
        base = [r for r in items if r['kind'] == 'base']
        rest = [r for r in items if r['kind'] != 'base']
        p, text = render(prod, ver, rest, base, ttl)
        if not p.exists():
            new += 1
        if write_page(p, text):
            chg += 1

    write_page(VDIR / IDX_NAME, render_index(facts))
    return len(grp), new, chg


def main():
    facts, odd, renorm = load_facts()
    write_facts(facts, odd)
    if '--facts' in sys.argv:
        return
    pages, new, chg = build(facts, titles())
    print(f'✅ wiki/versions/：{pages} 个版本页 + {IDX_NAME}（新建 {new}，改写 {chg}）')
    if renorm:
        print(f'⚠️  **替语料归一了 {len(renorm)} 处版本号**（正文照原样印，'
              '只在做分组 key 时归一）——列出来，不许悄悄改：')
        for prod, raw, key, doc in renorm[:10]:
            print(f'     {prod} `{raw}` → `{key}`   {doc}')


if __name__ == '__main__':
    main()
