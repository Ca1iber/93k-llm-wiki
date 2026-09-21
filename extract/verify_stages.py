#!/usr/bin/env python3
# verify_stages.py — 9 个 stage 页的对账
#
# 为什么必须有这一份：
#   stage 页是**唯一由 LLM 写的**东西（object / constraint / mapping 都能从边数据脚本长出来）。
#   凡是 LLM 写的，就必须有机器验的东西，否则「看着挺像」就是唯一的验收标准。
#
# 检验的立足点，先说清楚**能抓什么、抓不到什么**：
#
#   抓得到（格式 + 可追溯性 + 覆盖性）：
#     - 九页齐不齐、十个小节齐不齐（schema §2.1 明令不许省节）
#     - frontmatter 必填字段在不在，`verified` 是不是 doc-only
#     - `sources:` 里每条路径**是否真的存在于语料**（typo 与幻觉一抓一个准）
#     - 正文里引用的分类号（`01.07.01.02` 这种）是否真的存在
#     - 「下一步」链是否成环、是否断头、results 是否正确收尾
#     - `in_src >= 20` 的 object 候选（去重后 125 个），**每一个**是否落进了某页的「涉及对象」。
#       漏一个就是硬错误（第六类）
#     - **同一对象在两页里被标成不同的层**（第十一类）。这条是纯内部一致性：
#       不需要知道哪层对，只需要知道两页不一致
#
#   **覆盖范围（2026-09-18 扩过一次，扩的原因值得记住）**：
#     第二 / 三 / 十一类原先**只走 `wiki/stages/` 九页**。这一批开始建 `objects/`
#     和 `concepts/` 之后，新页的 frontmatter、`sources:`、`layer:` **落在所有检查之外**——
#     而它们比九页更容易错（路径是手抄的，`layer`/`stage` 是这批新引入的字段）。
#     **绿的部分恰好是没查的那部分**，这是本项目里第三次同类错
#     （前两次：第八类漏行内代码跨度、第六类只 glob `objects/`）。
#     所以三处都补了「续」，`_other_pages()` 是唯一的页面来源。
#     **凡再扩一类检查，先问一句：它扫的目录，是不是「所有页面」。**
#
#   **第二次扩范围（2026-09-18，第十五类）扩的不是目录，是「查什么」**：
#     前十四类查的全是「该有的结构在不在」，**没有一类查「结构里有没有东西」**。
#     于是一页 `## 是什么` 写着 `（待补）` 的骨架，**十四条全绿**。
#     **每加一类检查，除了问「扫哪个目录」，还要问一句：
#     它查的是「东西在不在」，还是「东西对不对」——这两件事不是一回事。**
#
#   抓不到（**必须由人读**）：
#     - 内容对不对。机器能证明「你引的文档真的存在」，不能证明「你引对了」。
#       也不能证明「文档事实 / 推断 / 建议」分得对——那条只能读。
#       所以本脚本只把可疑处**摊开**，不假装判过。
#     - **「对象属于哪层」不能靠查文档章节判。** 试过，4 条全是误报：
#       `run()` 是 L2 API 而讲它的教学文档在 `01.06`；`FW_TASK` 是 L1 通道
#       而它的参考页在 `02.07`（L2 章）。**对象属于哪层**和**讲它的文档在哪章**
#       是两件事，章节结构里没有这个信息。别再试第三遍。
#
# 输出  extract/stage-report.md
#       extract/stage-map.csv      （object -> stage，从页面反推，供 object 页建页时用）

import csv
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

WIKI = Path(r'F:\master-dev\understand-anything-wiki\wiki')
OUTDIR = Path(r'F:\master-dev\understand-anything-wiki\extract')
CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')

STAGES = ['project', 'pin', 'level', 'timing', 'pattern',
          'testmethod', 'testflow', 'run', 'results']
SECTIONS = ['目的', '前置条件', '涉及对象', 'L1 — Firmware / Setup Command',
            'L2 — Test Method API', 'L3 — 外部控制', '产物', '验证', '常见错误', '下一步']
NEXT = dict(zip(STAGES, STAGES[1:] + [None]))
NOT_COVERED = '文档未覆盖'
# 分类号必须**整体**匹配，不许从中间截。
# 第一版用 \b(...)\b，结果从 `02.08.04.34.04.02.01` 里截出了 `04.02.01`，
# 报了个「引用了不存在的分类号」——**误报**，`timing` 页没编，是我的正则编了。
# 前后都排除数字和小数点，才能保证抓的是完整分类号。
RE_CATNO = re.compile(r'(?<![\d.])(\d{2}\.\d{2}(?:\.\d+)*)(?![\d.])')
RE_WIKILINK = re.compile(r'\[\[([^\]|#]+)')
R = []
STATS = {}          # 跨类传计数用（如第六类的未归属数），别用全局猜


def w(s=''):
    R.append(s)
    print(s)


def parse_page(p):
    """极简 frontmatter 解析——只吃本 schema 用到的那几种形式，不引 yaml 依赖。"""
    txt = p.read_text(encoding='utf-8')
    fm, body = {}, txt
    if txt.startswith('---'):
        i = txt.find('\n---', 3)
        if i > 0:
            raw, body = txt[4:i], txt[i + 4:]
            key = None
            for line in raw.split('\n'):
                if not line.strip():
                    continue
                if line.lstrip().startswith('- ') and key:
                    fm.setdefault(key, [])
                    if isinstance(fm[key], list):
                        fm[key].append(line.strip()[2:].strip().strip('"\'[]'))
                    continue
                if ':' in line:
                    key, _, val = line.partition(':')
                    key, val = key.strip(), val.strip()
                    fm[key] = [] if val in ('[]', '') else val.strip('"\'')
    return fm, body


def cat1_files():
    w('## 第一类 · 九页齐不齐、十节齐不齐')
    w()
    ok = True
    rows = []
    pages = {}
    for s in STAGES:
        p = WIKI / 'stages' / f'{s}.md'
        if not p.is_file():
            w(f'- ❌ 缺 `stages/{s}.md`')
            ok = False
            continue
        fm, body = parse_page(p)
        pages[s] = (fm, body)
        heads = [h.strip() for h in re.findall(r'^##\s+(.+?)\s*$', body, re.M)]
        miss = [x for x in SECTIONS if x not in heads]
        extra = [h for h in heads if h not in SECTIONS]
        n_blank = sum(1 for x in SECTIONS
                      if x in heads and NOT_COVERED in _section_body(body, x))
        if miss:
            w(f'- ❌ `{s}.md` 缺小节：{miss}')
            ok = False
        if extra:
            w(f'- ⚠️ `{s}.md` 有多余小节（schema 未定义）：{extra}')
        rows.append((s, len(body), len(heads), len(miss), n_blank))
    w()
    w('| stage | 字节 | 小节数 | 缺 | 声明「文档未覆盖」的小节 |')
    w('|---|---|---|---|---|')
    for s, b, h, m, nb in rows:
        w(f'| `{s}` | {b:,} | {h} | {m} | {nb} |')
    w()
    return ok, pages


def _section_body(body, name):
    """取某个 `## name` 到下一个 `## ` 之间的正文。"""
    m = re.search(r'^##\s+' + re.escape(name) + r'\s*$', body, re.M)
    if not m:
        return ''
    nxt = re.search(r'^##\s+', body[m.end():], re.M)
    return body[m.end():m.end() + nxt.start()] if nxt else body[m.end():]


TYPES = {'stage': 'stages', 'object': 'objects', 'concept': 'concepts',
         'constraint': 'constraints', 'mapping': 'mappings',
         'error': 'errors', 'version': 'versions'}
LAYERS = ('L1', 'L2', 'L3', 'file', 'gui', 'n/a')
# §6 只给 `object` / `constraint` / `mapping` 写了 `layer` + `stage`。
# `concept` 页带 `stage` 是**有用的**（读者要知道这段概念在哪段流程里用得上），
# 所以「带了就合法」和「必须带」是两条规矩：这一条只查前者。
# 不查前者的话，`layer: L4` 这种拼法会一路绿到底——§11 那句「层要写清」就落空了。
HAS_LAYER_STAGE = ('object', 'constraint', 'mapping')

# **机械汇编页**：`sources:` 的含义比别的类型弱一层。
#
# 别的页写 `sources: [X]` 的意思是「**本页讲的就是 X**」；
# 而 `wiki/versions/7.2.0.md` 写 `sources: [X]` 的意思是
# 「**X 这篇文档里有一条 7.2.0 的变更记录**」——它**不是一页「讲 X」的页**。
#
# 第六类拿 `sources:` 当「这个候选有归宿」的判据。142 个版本页一进来，
# 它们各自列着几十篇文档，**几乎把候选全认领了**——
# 于是第六类变成一条**永远不会红**的检查，而报告上仍是绿的。
# **这正是本仓库记了六次的那个病的第七次：判据在动，绿不变。**
#
# 处置：**第六类只用「讲这个对象」的页**，机械汇编页排除在外。
# 排除之后第六类仍然全绿（真归属是够的）——**绿是查出来的，不是让出来的。**
MECH_TYPES = ('version',)


def _fm_good(fm, k, typ):
    """一页的一个字段合不合 §6。**判据集中在这里**，免得两处表格各判各的。"""
    v = fm.get(k)
    if k == 'type':
        return v == typ
    if k == 'verified':
        return v == 'doc-only'
    if k == 'title':
        return bool(v)
    if k in ('created', 'updated'):
        return isinstance(v, str) and bool(re.match(r'\d{4}-\d{2}-\d{2}', v or ''))
    if k == 'sources':
        return bool(v)                      # §6：**必填且至少一条**
    if k == 'layer':
        return v in LAYERS
    if k == 'stage':
        return v in STAGES
    return v is not None


def _fm_row(fm, typ, need):
    """一行 `| ✅ | … |`，**顺带返回这一行有没有错**。"""
    cells, ok = [], True
    for k in need:
        good = _fm_good(fm, k, typ)
        ok &= good
        cells.append('✅' if good else f'❌`{fm.get(k)}`')
    return cells, ok


def cat2_frontmatter(pages):
    w('## 第二类 · frontmatter 必填字段')
    w()
    need = ['type', 'title', 'tags', 'related', 'sources', 'created', 'updated', 'verified']
    ok = True
    w('| stage | type | title | tags | related | sources | created | updated | verified |')
    w('|---|---|---|---|---|---|---|---|---|')
    for s in STAGES:
        if s not in pages:
            continue
        fm, _ = pages[s]
        cells, this = _fm_row(fm, 'stage', need)
        ok &= this
        w(f'| `{s}` | ' + ' | '.join(cells) + ' |')
    w()
    w('`type` 必须 `stage`、`verified` 必须 `doc-only`（是否上机验证过只有人能改，'
      '见 `schema.md` §6）。')
    w()
    return ok and cat2b_other()


# §7 的子索引页（`index-<类型>.md`）**没有 `sources`**——它们是机器汇编的清单，
# 没有对应的 raw 文档，所以 §6 那条「`sources` 至少一条」对它们是**空的**。
#
# **豁免必须配一条替换判据，否则豁免就等于「没人管」。** 所以这里是一个
# **具名的登记表**：每一条都要写清「谁生成它」和「哪条检查接替 §6 管它」。
# 名字（而不是「文件名以 index- 开头」）是有意的：**按名字模式豁免，
# 就等于让「新加一个子索引」自动获得豁免**——那正是 §13 记过的那类洞
# （`_skip_prose` 的注释里写过：改个文件名就改变检查范围，本身就是缺陷）。
#
# **没登记的 `index-*.md` 会让第二类变红并报出它**：于是「加一个子索引」
# 这个动作**被迫同时接上它的对账**，接不上就红着。**防的是静默生长。**
IDX_PAGES = {
    'versions/index-versions.md':
        '由 `extract/versions.py` 的 `render_index()` 生成；'
        '替换判据 = **与它的产出逐字节一致**（第十三类甲之二）',
}


def _idx_exempt(rel, k):
    """这一页的这个字段是不是被登记的豁免。返回豁免说明，或 `None`。"""
    if k in ('sources', 'related') and rel in IDX_PAGES:
        return IDX_PAGES[rel]
    return None


def cat2b_other():
    """**`wiki/stages/` 以外的每一页**，同一套 §6 判据。

    补这个口子是因为：第二类原先只扫九页，所以「✅ 通过」只覆盖九页的 frontmatter。
    这一批开始建 `objects/` / `concepts/` 之后，**新页的 frontmatter 没有任何检查**——
    而它们恰恰更容易错（`layer` / `stage` 是这一批新引入的字段，
    外加 `type` 和目录必须对得上，不然 §2 那七类就白分了）。
    **报了绿就得说清绿的是哪一块**；说不清的那一块等于没查。
    """
    w('### 第二类续 · `stages/` 以外各页（`objects/` `concepts/` …）')
    w()
    others = _other_pages()
    if not others:
        w('*（还没有这类页）*')
        w()
        return True
    need = ['type', 'title', 'tags', 'related', 'sources', 'created', 'updated', 'verified']
    ok = True
    w('| 页 | type | title | tags | related | sources | created | updated | verified |')
    w('|---|---|---|---|---|---|---|---|---|')
    # **`ok &= this` 这一句原先没有。**
    #
    # 原来是 `cells, _ = _fm_row(...)`——**表格照打 ❌，那个 ❌ 谁也不管**：
    # 这一节返回的 `ok` 只由下面那张表（`type` / 目录 / `layer` / `stage`）决定，
    # 于是 `title` / `tags` / `related` / `sources` / `created` / `updated` / `verified`
    # 七列上的红**一个都没进汇总**。`versions/index-versions.md` 的 `sources` 空着、
    # 表格里印着 `❌[]`，而第二类照样报「✅ 通过」——**自相矛盾的报告比没有报告更坏**
    # （同一句本文件里已经写过一次，见第九类那段）。
    # **这是「判据在动、绿不变」的第十三次**：这次动的不是判据，是**判据的出口被丢掉了**。
    for p in others:
        fm, _ = parse_page(p)
        rel = f'{p.parent.name}/{p.name}'
        cells, this = [], True
        for k in need:
            ex = _idx_exempt(rel, k)
            if ex:
                # **印出来，不静默。** 一格空着的 ❌ 和一句「已豁免、由谁接替」
                # 在报告里长得完全不同——后者下一轮读报告的人能直接去核。
                cells.append('— 豁免')
                continue
            good = _fm_good(fm, k, _type_of(p))
            this &= good
            cells.append('✅' if good else f'❌`{fm.get(k)}`')
        ok &= this
        w(f'| `{rel}` | ' + ' | '.join(cells) + ' |')
    for rel, why in sorted(IDX_PAGES.items()):
        if rel in {f'{p.parent.name}/{p.name}' for p in others}:
            w(f'    - ℹ️ `{rel}`：`sources` / `related` **豁免**（§7 子索引）。{why}')
    # **没登记的 `index-*.md` 一律红**，见 `IDX_PAGES` 上面那段。
    for p in others:
        if p.name.startswith('index-') and f'{p.parent.name}/{p.name}' not in IDX_PAGES:
            ok = False
            w(f'    - ❌ `{p.parent.name}/{p.name}` 是子索引，但**没登记替换判据**——'
              f'加进 `IDX_PAGES` 并接上生成脚本的对账，或者给它一个真的 `sources`。')
    w()
    w('| 页 | `type` | 目录对不对 | `layer` | `stage` |')
    w('|---|---|---|---|---|')
    for p in others:
        fm, _ = parse_page(p)
        typ = _type_of(p)
        good_type = _fm_good(fm, 'type', typ)
        want_dir = TYPES.get(fm.get('type'), '（未知类型）')
        dir_ok = (want_dir == p.parent.name)
        cells = []
        for k in ('layer', 'stage'):
            if k not in fm:
                # 缺不缺**分类型判**：`object`/`constraint`/`mapping` 缺了就是错，
                # 其余类型这里只记「没带」——**别把「没要求」写成 ❌**。
                cells.append('— 未带' if typ not in HAS_LAYER_STAGE else '❌缺')
                ok &= typ not in HAS_LAYER_STAGE
            else:
                good = _fm_good(fm, k, typ)
                ok &= good
                cells.append('✅' if good else f'❌`{fm.get(k)}`')
        ok &= good_type and dir_ok
        w(f'| `{p.parent.name}/{p.name}` | ' +
          ('✅' if good_type else f'❌`{fm.get("type")}`') + ' | ' +
          ('✅' if dir_ok else f'❌应为 `{want_dir}/`') + ' | ' + ' | '.join(cells) + ' |')
    w()
    w('`layer` 合法值：' + ' / '.join(f'`{x}`' for x in LAYERS) + '（§2 那六层）。')
    w('`stage` 合法值：九段之一。**`layer`/`stage` 对 `object`/`constraint`/`mapping` '
      '是必填**，其余类型带了就得合法。')
    w()
    w('> **`stage` 该填什么，建了这一批才有个真问题**：§12 允许为**不属于任何一段流程**'
      '的对象建页（判据是入度），可 §6 又要求 `stage` 必填。')
    w('> 处置：**填「最近的一段」，并在页内写明这是「最近」不是「归属」**。')
    w('> 理由：这个字段的用处是「读者该去哪一段里找它的用法」，填最近的一段对这个用处是对的；')
    w('> 而把「归属」写成字段会把**没人要它**的东西伪装成某一环的正式成员。')
    w()
    return ok


def _type_of(p):
    """目录 → 应有的 `type`。**目录是判据**，不是页里自称的 `type`——
    否则「`type` 和目录对不上」这条检查会自证成立。"""
    for t, d in TYPES.items():
        if d == p.parent.name:
            return t
    raise SystemExit(f'❌ {p} 不在 §2 定义的任何一个目录里')


def cat3_sources(pages, docs_by_rel):
    """**最值钱的一类**：`sources:` 里的路径是不是真的存在。

    编路径是 LLM 最典型的幻觉——引用看起来完全合理，但那篇文档不存在。
    这一条能把「我读过 X」和「我记得有 X」分开。
    """
    w('## 第三类 · `sources:` 可追溯（**抓幻觉**）')
    w()
    w('每条来源路径逐个查语料。**不存在的路径 = 编的**，一个都不许放过。')
    w()
    ok = True
    total = 0
    for s in STAGES:
        if s not in pages:
            continue
        n, good = _src_check(pages[s][0], f'`{s}`', docs_by_rel)
        total += n
        ok &= good
    w()
    w(f'阶段页合计 {total} 条来源路径。')
    w()
    # **`stages/` 以外的页也要查。** 这一条自称「最值钱」，而第一版只走九页——
    # 于是新一批 `objects/` / `concepts/` 页的 `sources:` **完全没查过**。
    # 偏偏新页最容易编路径：九页的路径是从 `stage-map.csv` 抄的，
    # 新页的路径是我从 pack 里手抄的。**手抄是幻觉的高发区，而它正好在检查之外。**
    others = _other_pages()
    if others:
        w(f'### 第三类续 · `stages/` 以外 {len(others)} 页')
        w()
        n = 0
        for p in others:
            fm, _ = parse_page(p)
            k, good = _src_check(fm, f'`{p.parent.name}/{p.name}`', docs_by_rel)
            n += k
            ok &= good
        w()
        w(f'其余页合计 {n} 条来源路径（阶段页合计 {total} 条）。')
        w()
    return ok


def _src_check(fm, label, docs_by_rel):
    """查一页的 `sources:`。返回 `(条数, 是否全存在)`。"""
    src = fm.get('sources') or []
    if isinstance(src, str):
        src = [src]
    bad = [x for x in src if x not in docs_by_rel]
    mark = '✅' if not bad else '❌'
    w(f'- {mark} {label} — {len(src)} 条来源' +
      (f'，**{len(bad)} 条不存在**：' if bad else ''))
    for b in bad:
        w(f'    - ❌ `{b}`')
    return len(src), not bad


def _other_pages():
    """`wiki/stages/` 以外的全部内容页（按路径排序）。**机械汇编页也算**——
    第三类要查它们的 `sources:` 存在不存在（存在性判据对所有页一视同仁）。"""
    return sorted(p for t, d in TYPES.items() if t != 'stage'
                  for p in (WIKI / d).glob('*.md'))


def page_of_type(real=True):
    """要不要 `MECH_TYPES` 那几类。

    **存在的理由是「哪些页算数」对不同检查不是同一个答案**：
    第三类要最宽的网（连机械页的路径也查），第六类只要「讲对象的页」
    （机械页会把候选全认领，见 `MECH_TYPES`）。**把它们写成一个共用的
    `_other_pages()` 正是这次出错的地方**——共用了，口径就只能有一个。
    """
    return sorted(p for t, d in TYPES.items()
                  if t != 'stage' and (t not in MECH_TYPES) == real
                  for p in (WIKI / d).glob('*.md'))


def cat4_catno(pages, catnos):
    """正文里引用的分类号是否真的存在（比 sources 更宽的一层网）。"""
    w('## 第四类 · 正文引用的分类号是否存在于语料')
    w()
    ok = True
    for s in STAGES:
        if s not in pages:
            continue
        _, body = pages[s]
        refs = set(RE_CATNO.findall(body))
        bad = sorted(r for r in refs if r not in catnos)
        if bad:
            ok = False
            w(f'- ❌ `{s}` 引用了不存在的分类号：{bad}')
        else:
            w(f'- ✅ `{s}` — 引用 {len(refs)} 个分类号，全部存在')
    w()
    w('> 分类号只取前两级/三级也能命中（如 `01.07`），所以这一类比第三类松；')
    w('> 它是补第三类的漏网，不是替代。')
    w()
    return ok


def cat5_chain(pages):
    w('## 第五类 · 「下一步」链')
    w()
    ok = True
    for s in STAGES:
        if s not in pages:
            continue
        _, body = pages[s]
        seg = _section_body(body, '下一步')
        links = RE_WIKILINK.findall(seg)
        exp = NEXT[s]
        if exp is None:
            if links:
                w(f'- ℹ️ `{s}`（末段）指向 {links} — 末段允许指向收尾页，只要不是硬造第十段')
            else:
                w(f'- ✅ `{s}`（末段）正确收尾，未硬造下一段')
        elif exp not in links:
            ok = False
            w(f'- ❌ `{s}` 的「下一步」应指向 `[[{exp}]]`，实际是 {links or "（空）"}')
        else:
            w(f'- ✅ `{s}` → `[[{exp}]]`')
    w()
    return ok


# **第六类里已查明的误报**：候选那篇文档讲的对象，**已经由另一篇文档建的页认领了**。
# 这是工作单第二条限界「同一对象在两章各有文档」（2026-09-20 核实）。
#
# **为什么要写下来而不是留着 ❌**：一个**常亮的假红**会训练人忽略红——
# 下次真漏了页，那一片红里看不出区别。**但例外必须能被证伪**：
# 每条都指名「是哪一页认领的」，**那一页一没，例外当场失效、❌ 回来**
# （同 `FORMAT_EXAMPLES` 那套：允许列例外，但不许例外没人管）。
NO_PAGE_EXC = {
    '02_System_reference/02.03_DUT_board_design_reference/'
    '02.03.08.01.06_DC_Scale_UHC4___UHC4T_card.md': (
        'DC Scale UHC4 / UHC4T card',
        'wiki/objects/dc-scale-uhc4t-card.md',
        '同一对象在 `02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.md` '
        '另有一篇，页以那一篇为 `sources:`'),
}


def apply_no_page_exceptions(no_page):
    """→ `(还该报的, 例外生效的, **例外失效的**)`。

    **失效的那种必须浮上来**：指名的页被删了/改了名，例外就没有依据了，
    这时**藏着它比不设例外更坏**——它会把一个真漏报压成绿。
    """
    hit, dead, keep = [], [], []
    for c in no_page:
        e = NO_PAGE_EXC.get(c['rel'])
        if not e:
            keep.append(c)
            continue
        nm, pg, why = e
        # **页的路径按 `WIKI` 的父目录解析**，不写死盘符——
        # 反向测试会把 `WIKI` 指到临时目录，写死就变成「查的是真的那份」。
        (hit if (WIKI.parent / pg).exists() else dead).append((c, nm, pg, why))
    return keep, hit, dead


def cat6_coverage(pages, hubs, docs_by_rel):
    """**建页映射表**：`in_src >= 20` 的 object 候选（去重后 125 个），每个落到某个 stage。

    这是本脚本的第二个主要产出。映射从页面反推（页面是判断落地的地方），
    然后**反查覆盖**——没被任何页提到的候选，就是漏了。
    """
    w('## 第六类 · object 候选的 stage 归属覆盖')
    w()
    def norm(x):
        return re.sub(r'[^a-z0-9]', '', x.lower())

    # ── 已建的 `object` / `concept` 页也算「有归属」──
    #
    # §12（2026-09-18 那条）定了 stage 之外照建 object 页。**建了就必须被这里认出来**，
    # 否则 ❌ 永远不灭——报告说的和事实不一致，就是报告在骗人，
    # 而下一轮读报告的人（或下一个我）会照着假数字去重复建页。
    #
    # 判据用 frontmatter 的 `sources:`，**不用文件名相似度**：
    # 文件名相似是猜，`sources` 是**页面自己声明的「我定义的是哪篇」**。
    # 猜错会把两个不同对象算成一个，那种错看不出来。
    #
    # **扫全部类型目录，不只 `objects/`。** 上面那句注释第一版就写着「object / concept
    # 页也算」，而代码只 glob 了 `objects/`——**说的和做的不一致，代码赢**，
    # 于是 `pogo-pad-and-via-design`（建成了 `concepts/` 页）继续留在「未归属」里，
    # ❌ 数报 29 而真相是 28。**这类错的形态要记住：检查比它自称的范围窄，
    # 而窄的那部分恰好是绿的那部分。**「有没有页」和「页放在哪个目录」是两个问题，
    # 前者决定归属，后者是 §2 的类型判断。
    built = {}
    for t, d in TYPES.items():
        if t == 'stage' or t in MECH_TYPES:
            # 机械汇编页的 `sources:` 不是「我讲的是它」——见 `MECH_TYPES` 的注释。
            continue
        for p in sorted((WIKI / d).glob('*.md')):
            fm, _ = parse_page(p)
            srcs = fm.get('sources') or []
            if isinstance(srcs, str):
                srcs = [srcs]
            for s in srcs:
                built[s] = f'{p.parent.name}/{p.stem}'

    mentions = defaultdict(set)          # norm(link) -> {stage}
    body_mentions = defaultdict(set)
    linktext = {}                        # stage -> 全部 wikilink 拼成的串（供短名兜底匹配）
    for s in STAGES:
        if s not in pages:
            continue
        _, body = pages[s]
        linktext[s] = ' '.join(RE_WIKILINK.findall(body)).lower().replace('-', '')
        for m in RE_WIKILINK.findall(body):
            mentions[norm(m)].add(s)
        # 正文里直接写的对象名（如 `DFPN`、`PSFC`）也算提及
        for tok in re.findall(r'`([A-Za-z][A-Za-z0-9_\.\(\)]{2,40})`', body):
            body_mentions[norm(tok)].add(s)

    # 整页拍平（只留字母数字），用于「散文提及」的兜底匹配。
    # 为什么需要兜底：对象名在页里常常就是普通散文（「SmartCalc framework 把耗时计算…」），
    # 第一版只认 wikilink 和反引号，于是把明明讲过的对象报成「未覆盖」——
    # **那是我的检查太窄，不是页的漏**。同 timing 那次正则误报是一类错。
    flat = {s: re.sub(r'[^a-z0-9]', '', pages[s][1].lower()) for s in linktext}

    cands = []
    for h in hubs:
        # `is_index` 只存在于未去重表；去重表本来就不含 index 行，取值兜底即可。
        if h.get('is_index') == '1' or int(h['in_src']) < 20:
            continue
        rel = h.get('rel') or h['path']
        stem = rel.split('/')[-1][:-3]
        title = (docs_by_rel[rel].get('title') or '').strip()
        cands.append({'rel': rel, 'in_src': int(h['in_src']), 'title': title,
                      'stem': stem})

    linked, prose_only, unassigned, built_hit = [], [], [], []
    for c in cands:
        if c['rel'] in built:
            built_hit.append((c, built[c['rel']]))
            continue
        keys = {norm(c['title']), norm(c['stem'].split('_', 1)[-1]),
                norm(c['stem'].split('_', 1)[-1].split('__')[0])}
        keys = {k for k in keys if len(k) >= 3}
        strong = set()
        for k in keys:
            strong |= mentions.get(k, set()) | body_mentions.get(k, set())
        # 对象名也可能被 wikilink 成短名（dfpn / psfc）
        for k in list(keys):
            strong |= {s for s in linktext if k in linktext[s]}
        if strong:
            linked.append((c, sorted(strong)))
            continue
        # 兜底：标题里每个有实义的词都出现在该页散文里，算「提过但没成链」
        toks = [norm(t) for t in re.split(r'[^A-Za-z0-9]+', c['title'])]
        toks = [t for t in toks if len(t) >= 3]
        weak = {s for s in flat if toks and all(t in flat[s] for t in toks)}
        if weak:
            prose_only.append((c, sorted(weak)))
        else:
            unassigned.append(c)

    w(f'`in_src >= 20` 的 object 候选（排除 index）：**{len(cands)}** 个。')
    w()
    w(f'- ✅ **已建页**（`wiki/` 下任意类型目录，由 frontmatter `sources` 认领）：**{len(built_hit)}**')
    w(f'- ✅ **成链**（wikilink 或反引号点名，九页里）：**{len(linked)}**')
    w(f'- ⚠️ **只在散文里提过，没成链**：**{len(prose_only)}**')
    # **这一档是「坏桶」，计数为 0 才是好事——符号必须跟着数走，不能跟着档位走。**
    # 原本无论几行都印 `❌`，于是 `❌ … 0` 和 `❌ … 47` 长得一样：
    # **grep `❌` 的人会看见它，却分不出「红」和「这一档是空的」。**
    # 与先前修过的 `sorted(c_buckets)` 吞掉 0 号桶同源（§13.1 ④：
    # 「红的是不是我要它抓的东西？」——反过来也成立：**绿的是不是我以为在红的东西？**）
    n_un = len(unassigned)
    w(f'- {"✅" if not n_un else "❌"} **一个字都没提的：{n_un}**'
      + ('（**这一档空着才是对的**）' if not n_un else ''))
    # ── ⚠️ 2026-09-20：**这一条查的是「提没提到」，而欠账是「有没有页」** ──
    # 踩法：候选按「已建页 → 成链 → 只在散文 → 一个字没提」**顺序**分桶，
    # 所以一个「被 stage 页提过、但没有页」的候选会落进**成链**桶，而那一桶印 ✅。
    # `WSUS`（**语料入度 93**）就这样绿了很久：`timing.md` 甚至把它写进了 `sources:`
    # 并在正文里点出「被 93 篇引用」——**提了，但没有它的页**。
    # `unowned.py` 的工作单用的是同一套判据（`object_rel` 在不在 `stage-map.csv` 里），
    # 于是那 23 篇从**两张单上同时消失**。
    # **这正是本工程反复踩的那个形状：检查（和工作单）比它自称的范围窄，
    # 而窄掉的那块一直是绿的。**
    no_page = [c for c in cands if c['rel'] not in {x[0]['rel'] for x in built_hit}]
    no_page, exc_hit, exc_dead = apply_no_page_exceptions(no_page)
    for c, nm, pg, why in exc_hit:
        w(f'- ⚪ **已查明误报**（不计入 ❌）：`{nm}` 这一篇由 `{pg}` 认领——{why}。')
    for c, nm, pg, why in exc_dead:
        w(f'- ❌ **例外失效**：`{nm}` 的例外指名的 `{pg}` **已经不在**，'
          '所以这个例外没有依据了，**如实计回 ❌**。')
    w(f'- {"✅" if not no_page else "❌"} **`in_src >= 20` 还没有页的：{len(no_page)}**'
      + ('（**这一档空着才是对的**）' if not no_page else
         '（**提没提到都不算数，要的是「有没有页」**——明细见 `extract/unowned.csv`）'))
    if no_page:
        w()
        w('| in_src | 对象 | 没页 |')
        w('|---|---|---|')
        for c in sorted(no_page, key=lambda x: -x['in_src'])[:30]:
            w(f'| {c["in_src"]} | {c["title"][:44]} | `{c["rel"]}` |')
        if len(no_page) > 30:
            w(f'| … | 其余 {len(no_page) - 30} 条见 `extract/unowned.csv` | |')
        w()
    w()
    if built_hit:
        w('已建页（这些从「未归属」里出列了）：')
        w()
        w('| in_src | 对象 | 页 |')
        w('|---|---|---|')
        for c, slug in sorted(built_hit, key=lambda x: -x[0]['in_src']):
            w(f'| {c["in_src"]} | {c["title"][:44]} | `wiki/{slug}.md` |')
        w()
    if prose_only:
        w('「只在散文里提过」不算漏，但**对象页建起来之后没有入链**——'
          '这页读起来会像没有这个对象。值得补成 `[[...]]`。')
        w()
        w('| in_src | 对象 | 出现在 |')
        w('|---|---|---|')
        for c, ss in sorted(prose_only, key=lambda x: -x[0]['in_src'])[:40]:
            w(f'| {c["in_src"]} | {c["title"][:40]} | {", ".join(ss)} |')
        if len(prose_only) > 40:
            w(f'| … | 其余 {len(prose_only) - 40} 条见 `stage-map.csv` | |')
        w()
    if unassigned:
        # **按顶层子树归并**。散着看会以为「漏了 36 个零星对象」；
        # 归并后才知道是**整棵子树没有归属**——这是两种完全不同的结论，
        # 处置也完全不同（零星要补，整块要决定收不收）。
        roll = defaultdict(list)
        for c in unassigned:
            seg = c['rel'].split('/')
            roll['/'.join(seg[:2]) if seg[0].startswith('0') else seg[0]].append(c)
        w('下面这些**没有被任何 stage 页提到**，**按顶层子树归并**：')
        w()
        w('| 子树 | 未归属对象数 | 其中 in_src 最高 |')
        w('|---|---|---|')
        for k in sorted(roll, key=lambda k: -len(roll[k])):
            top = max(roll[k], key=lambda x: x['in_src'])
            w(f'| `{k}` | {len(roll[k])} | {top["in_src"]} — {top["title"][:36]} |')
        w()
        w('**处置已定（2026-09-18）：建 stage 之外的 `object` 页。**')
        w('理由：这些是「硬件规格 / 存储专用测试 / 程序管理」，不是流程步骤，')
        w('所以不该硬塞进九页；但它们的入度比很多已归属对象还高，')
        w('**wiki 的第一价值就是告诉人「这是什么」**——不建，读者就永远不知道。')
        w('清单：`extract/unowned.csv`（按子树归并，含 in_src 与路径）。')
        w()
        w('| in_src | 对象 | 路径 |')
        w('|---|---|---|')
        for c in sorted(unassigned, key=lambda x: -x['in_src']):
            w(f'| {c["in_src"]} | {c["title"][:40]} | `{c["rel"]}` |')
        w()

    STATS['unassigned'] = len(unassigned)
    # **❌ 的判据是 `no_page`，不是 `unassigned`**——所以汇总里那句结论要的数字
    # 必须从 `no_page` 自己这儿出。**借旁边的统计 = 迟早借到一个意思不一样的数**
    # （2026-09-20 就是这么在报表上印出「0 个」配一个 ❌ 的）。
    STATS['no_page'] = len(no_page)
    STATS['no_page_names'] = [(c['title'][:44], c['rel']) for c in no_page]
    # 第八类的散文里要引用「候选面有多少个」。**写死过一次 153，那是没去重时的旧数**——
    # 报告里印一个自己算不出来的数字，就是报告在骗人（本文件已经栽过几次）。
    # 数在这里产出，就在这里是唯一出处。
    STATS['cand'] = len(cands)
    with open(OUTDIR / 'stage-map.csv', 'w', encoding='utf-8', newline='\n') as f:
        f.write('stage,object_title,object_rel,in_src,strength\n')
        for c, ss in sorted(linked + prose_only,
                            key=lambda x: (x[1][0], -x[0]['in_src'])):
            st = 'linked' if (c, ss) in linked else 'prose'
            for s in ss:
                f.write(f'{s},"{c["title"]}",{c["rel"]},{c["in_src"]},{st}\n')
        # 已建页也写进来，属主写成 `page:<类型目录>/<slug>`——**一张表里必须能查到全部归属**。
        # 不写的话 `unowned.py` 会拿这份表反算「未归属」，于是清单永远比报告多
        # 那几个已经建好的页（那个 assert 会红，红得对，但原因是我漏了这一步）。
        for c, slug in sorted(built_hit, key=lambda x: -x[0]['in_src']):
            f.write(f'object:{slug},"{c["title"]}",{c["rel"]},{c["in_src"]},page\n')
    w(f'映射表写入 `extract/stage-map.csv`（{len(linked) + len(prose_only)} 条候选 + '
      f'{len(built_hit)} 条已建页；多归属的会多行；已建页的属主写成 `page:<类型目录>/<slug>`）。')
    w()
    return len(unassigned) == 0 and len(no_page) == 0


def cat7_quotes(pages):
    """第七类 · **引文是否逐字**。抓「编引文」。

    前三类抓的是「路径编了」「分类号编了」。但页里大量「逐字」引的英文原句，
    格式检查一个字都抓不到：**编一句看起来极合理的英文，和真引一句，长得一样**。

    但逐字引文是**可以回原文对的**——它本该在语料里一字不差地存在。

    做法：把页面里的引用块（`>` 行）与代码块抠出来，中文化/规范化后，
    去 9,398 篇里找**完全子串**。找不到的有三种归宿（同本项目既有规矩）：
      （a）引错了 / 编的 → 改页
      （b）原文有但被改写过（换行、省略号、加粗）→ 属于「转述」，**不该写「逐字」**
      （c）语料本身如此（比如引的是 PDF 里的东西）→ 记录

    **不做自动修改**，只摊开。规范化只做两件不影响语义的事：折叠空白、去 markdown 强调符。
    凡是为「让它匹配上」而多做的规范化，都是在替被检对象打掩护。
    """
    w('## 第七类 · 引文是否逐字（**抓编引文**）')
    w()
    n_skip = sum(1 for p in WIKI.rglob('*.md') if _skip_prose(p))
    w(f'> **范围：`wiki/` 下**除 `log.md` / `index.md` 和 §7 的子索引（`index-*.md`）**外的'
      f'全部页面**——本次跳过 **{n_skip} 个元文件**，逐个列在下面（本类曾只走九页，见下）。'
      f'判据是「引用块能在 9,398 篇里找到完全子串」，不是「读起来像」。')
    w()
    w('> 跳过的：' + '、'.join(f'`{p.relative_to(WIKI).as_posix()}`'
                              for p in sorted(WIKI.rglob('*.md')) if _skip_prose(p))
      + '。**这是全部**——排除必须报出来，不许静默缩小范围。')
    w()
    normed = {}
    for rel in docs_by_rel_cache:
        try:
            t = (CORPUS / rel).read_text(encoding='utf-8', errors='replace')
        except OSError:
            continue
        if t.startswith('---'):
            i = t.find('\n---', 3)
            if i > 0:
                t = t[i + 4:]
        normed[rel] = _norm(t)

    # 拼成一块再查，比「每个窗口 × 9,398 篇」快一个数量级。
    # 用 `\x00` 当分隔符：窗口里不可能含它，**所以匹配绝不会跨过文档边界**——
    # 图快而放松判据，就等于把这条检查变成安慰剂。
    blob = '\x00'.join(normed.values())
    # 第二级判据用的「去掉所有空白」版。空语料在这里**必须报错**——
    # 诊断脚本第一版就是因为语料没加载上，把每一块都报成 0%（见 `_why.py`）。
    wsfree = re.sub(r'\s+', '', blob)
    assert len(wsfree) > 1_000_000, f'语料没加载上（{len(wsfree)} 字符）——查了等于没查'

    ok = True
    n_struct_tot = 0   # 疑似自加结构的处数（跨页合计，**0 也要印出来**，见下）
    # 被切掉的「语法节」：页数与字符数。**0 也要印出来**（同上）。
    n_syn, n_syn_chars = 0, 0
    # **所有页都要查，不只九页。**
    #
    # 第一版这里是 `for s in STAGES`——本类的名字叫「抓编引文」，
    # 但**它只走了九个 stage 页**：`objects/` `concepts/` 底下十几页
    # 里的 `*"…"*` 逐字引文**一条都没进检查**。
    # **同类错第五次**（前四次：第八类漏行内代码跨度、第六类只 glob 一个目录、
    # 第二/三/十一类只走九页、抽取器只收「H2 底下第一个 H3 之前」）。
    # 这次是**在自己正要再写 26 页之前发现的**——先修镜子，再照。
    for p in sorted(WIKI.rglob('*.md')):
        if _skip_prose(p):
            continue              # 流水账 / 目录页，不是内容页
        s = str(p.relative_to(WIKI)).replace('\\', '/')
        _, body = parse_page(p)
        # **`<!-- 语法节 begin -->` 到 `end` 之间那一段不归本类管。**
        #
        # 那一段是 `objscaffold.py` 写的（§4），**它按设计就不是逐字的**：
        # 段内的语料内部链接被机械改写成 ``文本``（raw: `路径`）——
        # 那是脚本为了「文本和路径都留着」故意做的，**改写本身就是它的职责**。
        #
        # 不切掉它，第七类就会报一条**它自己造成的**「对不上」。
        # 建 `objects/pogocabling-section.md` 时实测撞上：该页 16 处引用块里
        # **唯一**一处对不上就是这块 —— 而它的出处正是 objscaffold。
        #
        # **第十二类已经用更硬的口径管着这一段**（页面与脚本当前产出**逐字节一致**）。
        # 两个检查管同一段、一个用「逐字」一个用「逐字节」，**弱的那条只会产生噪声**；
        # 而噪声会淹掉真缺陷——§13.1 第五次那句在这里是反向适用：
        # **报得太多，等于没报。**
        #
        # **切了多少必须印出来**（下面 `n_syn` / `n_syn_chars`），不许静默缩小范围——
        # 这是本类开头那条「排除必须报出来」的同一规矩。
        body, cut = _cut_syntax_region(body)
        if cut:
            n_syn += 1
            n_syn_chars += cut
        blocks = _extract_quotes(body)
        hard, soft = [], []
        n_fmt = 0
        # **`all_struct` 在 `cov >= 0.8` 那道闸之前收集**，这是有意的：
        # 那道闸是给「整块还行」的块放行的（它顺手滤掉了滑窗接缝的误报），
        # 但**一个 10 行的引文块里混 1 行编的 `- ` 列表符，覆盖率是 0.9**——
        # 整块被放行，那一行就**永远看不见**。
        # 形状判据问的是「这一行有没有原文没有的结构」，**和整块的平均覆盖率无关**，
        # 所以它不能待在那个闸后面。
        all_struct = []
        for b in blocks:
            def check(units):
                """→ `(对不上的, 仅忽略空白才对上的, 疑似自加结构的)`。

                **「疑似自加结构」是筛查项，不是判据。** 形状判据三条：
                引文单元**以 `- ` 开头**、**中间含 ` - `**、或**含 `…` / `...`**，
                **且对不上原文**。（省略号两个写法都查——只查 U+2026 的那一版
                **漏掉了 `stages/run.md` 里那条真缺陷**，见下面那句的判断处。）
                页面自加的列表符、和页面自加的 `—`，规范化后**都是 `- `**
                （`_norm` 把 `—` 折成 `-`），所以这三条同时覆盖两种。

                **它会有误报，而且误报有名字**：滑窗跨过两个**真**列表项时也命中
                （`run.md` / `timing.md` 那两条就是「……flags. - Execute……」这种接缝）。
                **所以这一档只报给人看，不判错**——它的价值在于**把这一类从「排版差异」里拎出来**。

                **为什么要单列**：2026-09-18 同一天里这个形状出现了两次
                （`objects/…Debug_View` 表格两列被 `—` 连成句；`cross-card-ganging-requires-ddic`
                里 `DDIC` 参数表两格被合成 `- CONN — …`）。两次都**被机器报了**，
                两次都**因为「未称逐字、覆盖率还行」被读成排版差异**。
                **报出来而不单列，等于没报**——§11.1 的闭合清单管的就是这一类。

                **曾经写过一版「反证」，它是坏的，留在这儿当教训**：那版说
                「把 `- ` 剥掉之后还能对上，就**证明**原文那里没有 `- `」。
                它**在自己要抓的那个形状上恰好全瞎**——因为查的是「剥掉后能否整块对上」，
                而**表格类引文的原文里，两格之间还夹着抽取留下的 ` | `**
                （raw 是 `CLR` / ` | ` / `Clears all previously defined circuitry.` 三行），
                所以「`CLR` + 说明」这两个真格的拼接**永远不可能是原文的子串**，
                反证因此**永远不成立**。
                **负测试当场抓住它**：把一个真缺陷写回页面，它报「0 处」，退出码 0。
                **教训**：「证明」这个词要慎用——这一版证明的是**我的探针**，不是页面。
                """
                bad, fmt, struct = [], 0, []
                for u in units:
                    r = _hit(u, blob, wsfree)
                    if r == 0:
                        bad.append(u)
                        # **`…`（U+2026）和 `...`（三个 ASCII 点）都要查。**
                        # 只查前者是**我自己给自己留的洞**：`stages/run.md` 里
                        # 那句真缺陷写的就是 `displayed... They require`——三个点，
                        # 于是它**从筛查项里漏了出去**，是后来拿 grep 手工回原文才认出来的。
                        # 「省略号」这一件事在语料里有两个写法，判据只认一个，就不是判据。
                        if u.startswith('- ') or ' - ' in u \
                                or '…' in u or '...' in u:
                            struct.append(u)
                    elif r == 1:
                        fmt += 1
                return bad, fmt, struct

            if b['kind'] == 'fence' and b['lines']:
                # **代码块逐行验**。拼接块的「逐字取自 A 与 B 与 C」说的是
                # **每一行**取自其中某篇，不是整块连续。整块比对必然冤枉它——
                # pin 页那个 DFPN 块就是这么被误判的。
                miss, fmt, struct = check(b['lines'])
                all_struct.extend(struct)
                cov = 1 - len(miss) / len(b['lines'])
                n_fmt += fmt
                rec = (cov, b['text'], miss)
            else:
                wins = _windows(b['text'])
                miss, fmt, struct = check(wins)
                all_struct.extend(struct)
                cov = 1 - len(miss) / len(wins)
                n_fmt += fmt
                rec = (cov, b['text'], miss)
            if cov >= 0.8:
                continue
            (hard if '逐字' in b['tail'] else soft).append(rec)
        mark = '✅' if not hard else '❌'
        extra = f'；另有 {n_fmt} 处**忽略空白后才对上**（排版差异，不判错）' if n_fmt else ''
        w(f'- {mark} `{s}` — 引用块/代码块 {len(blocks)} 处；'
          f'对不上的 {len(hard) + len(soft)} 处，其中'
          f'**页面自称「逐字」的 {len(hard)} 处**{extra}')
        for cov, q, miss in hard:
            w(f'    - ❌ **自称逐字、覆盖率 {cov:.0%}**｜`{q[:100]}{"…" if len(q) > 100 else ""}`')
            for m in miss[:3]:
                w(f'        - 缺失：`{m}`')
        for cov, q, miss in soft[:5]:
            w(f'    - ⚠️ 未称逐字，覆盖率 {cov:.0%}｜`{q[:80]}{"…" if len(q) > 80 else ""}`')
        if len(soft) > 5:
            w(f'    - …其余 {len(soft) - 5} 处同类')
        # **单列这一类**，理由见 `check()` 的 docstring：报出来而不单列，等于没报。
        if all_struct:
            n_struct_tot += len(all_struct)
            w(f'    - 🟠 **疑似自加结构 {len(all_struct)} 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / '
              f'含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——'
              f'滑窗跨过两个真列表项的接缝时也会命中，要人看。')
            for u in all_struct[:5]:
                w(f'        - `{u[:90]}{"…" if len(u) > 90 else ""}`')
        if hard:
            ok = False
    w()
    w('> **判据分两档，因为这两件事严重程度差一个数量级：**')
    w('>')
    w('> - **自称「逐字」却没对上 = 硬错误。** 要么改回原文，要么把「逐字」二字删掉。')
    w('> - **没自称逐字 = 转述，对不上是正常的。** 只提示，不判错。')
    w('>')
    # **0 也要印出来。** 一个只在自己非零时才出现的数字，等于没有这个数字——
    # 「本类报 0」和「本类没跑/没印」在报告里长得一模一样。
    w(f'> **另一档，与上面两档都不同：疑似自加结构 —— 本次共 {n_struct_tot} 处。**')
    # **本类主动切掉了一段，切多少必须印出来。** 理由见 `cat7_quotes` 里那段注释：
    # 那一段是 `objscaffold.py` 写的、**按设计就不逐字**，归第十二类（逐字节）管。
    # 但「另一个检查管着它」**不构成不说的理由**——静默缩小范围，
    # 下一个读这份报告的人就不知道本类到底查过哪些字。
    w(f'> **本类主动排除：`<!-- 语法节 begin -->`…`<!-- 语法节 end -->` 之间那一段，'
      f'本次涉及 {n_syn} 页、共 {n_syn_chars} 字符。**')
    w('> 那一段由 `objscaffold.py` 写（§4），段内语料链接被机械改写成 ``文本``（raw: `路径`），'
      '**按设计就不是逐字的**——不排除它，本类会稳定地报一条自己造成的「对不上」。')
    w('> **它没有被放过，是被更硬的口径接管了**：第十二类查的是'
      '「页面与脚本当前产出**逐字节一致**」。两个检查管同一段时，弱的那条只产生噪声。')
    w('> 形状判据三条：引文单元**以 `- ` 开头**、**中间含 ` - `**、或**含 `…` / `...`**，'
      '**且对不上原文**。')
    w('> 页面自加的列表符和页面自加的 `—` 在规范化后都是 `- `，三条同时覆盖两种。')
    w('> **这一档不看「有没有自称逐字」**——§11.1 的闭合清单是**引文本身**的规矩：'
      '在引文块里，`…`、列表符 `- `、单元格分隔都算原文的一部分。'
      '**排版差异可以放过，加进结构不行。**')
    w('> **它会误报，误报有名字**：滑窗跨过两个**真**列表项的接缝时也命中。'
      '**所以它是筛查项、不判错**——价值在于**把这一类从「排版差异」里拎出来**。')
    w('> 单列这一档的原因写在 `check()` 的 docstring 里：'
      '**同一个形状 2026-09-18 一天内出现两次，两次都被读成「排版差异」。**')
    w()
    w('> **判法分两种，因为块有两种：**')
    w('>')
    w('> - **代码块逐行验。** 页面会把多篇文档的行**拼成一个示例块**'
      '（`pin` 页那个 DFPN 会话块自注「逐字取自 A 与 B 与 C」）——')
    w('>   那句话的意思是**每一行**取自其中某篇，不是整块连续。整块比对必然冤枉它。')
    w('> - **散文引用用滑窗验**（8 词窗、步长 4）。散文会被换行、省略号、并句打断，')
    w('>   滑窗能把「接缝丢一两窗」和「成片丢窗」分开。')
    w()
    w('> ⚠️ **这条容忍 2026-09-18 收紧了。** 原文这里写的是「表格被改写成一行、多行被并成一句，'
      '只丢窗不丢片——**它们不是编，是格式改写**」。**那句话是错的**：')
    w('> 它并没有骗过机器（这几处一样被报成失配），**它是骗过了我**——'
      '被报出来之后，我**照着这句话把它们归类成「排版差异」而不是缺陷**，于是留在待办里。')
    w('>')
    w('> 复核那几处「格式改写」时发现，其中三处**真的少了字符**，不是只换了排版：')
    w('> `02.07.04.01.69_FLUSH` 的两个列表被拍平成行内代码（少抄了每行的 `- `）；')
    w('> `02.06.05_Level_Setup_Commands` 的六项列表被拍平，并加上**原文没有的粗体**；')
    w('> `01.01.08.06_Debug_View` 表格的两列被用**页面自加的 `—`** 连成句（原文里没有这个破折号）。')
    w('>')
    w('> **判据现在写死：`…`、列表符 `- `、单元格分隔，都算原文的一部分。**')
    w('> 引文里出现 `…`，等于承认中间有字没抄——**那就不是引文，是转述：要么补全，要么把引号去掉。**')
    w('> 分界是：**跨段合并不算错**（字还是连续的），**丢字符才算错**。')
    w('>')
    w('> **这条也是「检查比它自称的范围窄」那类错的第六次**——前五次见 §13。'
      '这次窄在**判据自己写的容忍度**上：本类叫「引文逐字」，却预先声明「格式改写放行」。')
    w()
    return ok


def _norm(s):
    """折叠空白 + 去 markdown 强调符 + 去中日韩引号。

    去 `「」『』` 是必须的：页面引英文原句时爱写 `「...」`，
    这两个字符语料里没有，不剥掉会**每一条都判失败**——那是我的格式问题，不是引文问题。
    """
    # 语料里的散文是**带链接标记**的：`The [TEST()](<02.07.04.01.241_TEST.md>) and ...`。
    # 页面引这句时会（正确地）把链接渲染成纯文本，于是对不上。
    # 不剥掉链接标记，等于**因为页面把引用做对了而扣它分**。
    s = re.sub(r'\[([^\]]*)\]\(\s*<?[^)>]*>?\s*\)', r'\1', s)
    s = s.replace('**', '').replace('`', '')
    for ch in '「」『』':
        s = s.replace(ch, ' ')
    # 破折号与弯引号只是排版差异，不承载语义。不统一它们，会把
    # 「原文用的破折号和我打的不一样」误报成「引错了」——那是我的格式问题。
    for ch in '—–−':
        s = s.replace(ch, '-')
    for a, b in [('“', '"'), ('”', '"'), ('‘', "'"), ('’', "'")]:
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()


WIN, STRIDE = 8, 4


def _hit(x, normed, wsfree=''):
    """`x` 在语料里能不能找到。**返回命中等级**：`2` 逐字 / `1` 忽略空白 / `0` 没有。

    分两级是**被两轮假警报逼出来的**，两轮都不是页面的问题：

    - **第一轮：引号。** 页面引英文原句写 `*"To access all features …"*`，
      `_norm` 把弯引号统一成直引号，**却不把直引号去掉**——而语料里那句没有引号。
      于是每条带引号的引用都丢首窗尾窗，单窗的直接 **0%**。
      语料里的 `"` 是内容（`"readID1"`），**不能全局删**，只能在页面这一侧多试一次。
      连 `*` 一起剥：`_norm` 去的是 `**`（粗体），**不去单个 `*`**（斜体），
      只剥引号不动 `*` 的话首字符是 `*`，`strip` 一个都剥不掉。
    - **第二轮：空白。** `_norm` 把连续空白折叠成**一个空格**，于是
      `a, b`（语料）与 `a,b`（页面）**永远对不上**；列表被并成一句、
      代码缩进不同、多行会话被接成一行，同理。
      **这些是排版差异，不是编造**——但混在真缺陷里，人就得逐条去猜。

    所以第二级把两边空白全去掉再比。**判据仍然严格**：整窗必须完整出现，
    只是不要求空格位置一致。真缺陷（少个点、多个字）在这个口径下**照样露馅**——

    > 实测：`test-suite-control-api` 那句语料是 `-o t1.exe. main.o`（**t1.exe 后有个多余的句点**），
    > 本页初版写成了 `t1.exe main.o`。**忽略空白之后仍然对不上**，于是被抓住。
    """
    if x in normed:
        return 2
    # 连 `*` 一起剥：页面写英文引语的格式正是**斜体包直引号**。
    y = x.strip('*"\'')
    if y and y != x and y in normed:
        return 2
    if wsfree:
        z = re.sub(r'\s+', '', y or x)
        if z and z in wsfree:
            return 1
    return 0


def _windows(q):
    """把一个引用块切成重叠词窗。

    为什么不能整块查子串：页面会**把多篇文档的片段拼成一个示例块**
    （pin 页那个 DFPN 会话块就自注「逐字取自 A 与 B 与 C」）。
    拼接块的全文在任何单篇里都不可能连续出现——**整块查必然全判失败，
    而页面是诚实的**。滑窗能让「拼接」与「编造」分开：
    拼接处只丢一两个窗，编造处成片丢窗。
    """
    ws = q.split(' ')
    if len(ws) <= WIN:
        return [q]
    out = [' '.join(ws[i:i + WIN]) for i in range(0, len(ws) - WIN + 1, STRIDE)]
    out.append(' '.join(ws[-WIN:]))
    return out


def _cut_syntax_region(body):
    """切掉 `<!-- 语法节 begin -->`…`<!-- 语法节 end -->` 那一段。→ `(切后的正文, 切掉的字符数)`。

    **为什么切**：那一段是 `objscaffold.py` 写的（§4）。它**按设计就不逐字**——
    段内的语料内部链接被机械改写成 ``文本``（raw: `路径`），
    目的是让「文本和路径都留着」。**改写本身就是脚本的职责，不是错误。**

    不切，第七类就会稳定地报一条**它自己造成的**「对不上」。
    2026-09-18 建 `objects/pogocabling-section.md` 时实测撞上：
    该页 16 处引用块里**唯一**一处对不上就是这块。

    **不是「放过」，是交给更硬的口径**：第十二类查的是
    「页面与脚本当前产出**逐字节一致**」。同一段被两个检查管、
    一个用「逐字」一个用「逐字节」，**弱的那条只产生噪声**——
    而噪声淹掉真缺陷。

    返回切掉的字符数而不是布尔值，是为了让调用方**必须**把它印出来：
    静默缩小范围是本项目明令禁止的（见本类开头的「排除必须报出来」）。

    **标记串从 `objscaffold` 里 import，不在这儿重打一遍。**
    边界是**写它的人留的记号**（那句话是第十二类的教训，
    拿一次真实误删换来的）。这里重打一遍，两边就有两个真相：
    脚本哪天改了标记，**本函数会静默地切不到**——那正是「读者推断边界」那个病。
    """
    import objscaffold as osc   # 轻量：0.02 s，只取两个常量
    out, cut, inside = [], 0, False
    for line in body.split('\n'):
        st = line.strip()
        if inside:
            cut += len(line) + 1
            if st == osc.MARK_END:
                inside = False
            continue
        if st == osc.MARK_BEGIN:
            # 开标记本身也切掉：它是给脚本和第十二类认边界用的，不是引文。
            inside = True
            cut += len(line) + 1
            continue
        out.append(line)
    # **只有 begin 没有 end = 页面坏了。** 这里不修、不猜，
    # 原样交回去让第七类去报——**兜底不能变成掩盖**。
    if inside:
        return body, 0
    return '\n'.join(out), cut


def _extract_quotes(body):
    """抠出引用块（连续 `>` 行）与 fenced code block。

    只留规范化后 >= 40 字符、且**不含 CJK** 的——含中文的是页面自己的话
    （如开头那句一句话摘要），本来就不是引文，不该拿来判。

    返回 `(引文, 块后紧跟的 200 字符)`。那 200 字符是用来判**这页有没有声称「逐字」**的
    ——这是本类检验里唯一真正硬的一条：
    **声称逐字却没对上，是错误；没声称逐字只是转述，对不上是正常的。**
    """
    out, buf, pos, start = [], [], 0, 0

    kind = ['quote']

    def flush(end):
        if buf:
            q = _norm(' '.join(buf))
            if len(q) >= 40 and not re.search(r'[一-鿿]', q):
                out.append({'text': q, 'tail': body[end:end + 200],
                            'kind': kind[0],
                            'lines': [_norm(x) for x in buf
                                      if len(_norm(x)) >= 12]})
            buf.clear()

    lines = body.split('\n')
    offs, acc = [], 0
    for ln in lines:
        offs.append(acc)
        acc += len(ln) + 1

    in_fence = False
    for i, line in enumerate(lines):
        if re.match(r'^\s*```', line):
            flush(offs[i])
            in_fence = not in_fence
            kind[0] = 'fence' if in_fence else 'quote'
            continue
        if in_fence:
            buf.append(line)
            continue
        if line.lstrip().startswith('>'):
            buf.append(line.lstrip()[1:])
        else:
            flush(offs[i])
    flush(len(body))
    return out


docs_by_rel_cache = []


# 讲格式的**示例**，不是引用。白名单里只有两项，可以用眼睛核。
#
# 第一版这里是**剥掉所有行内代码跨度**，于是 `` `[[Test_Method_Project]]` ``
# 这类被反引号包住的 wikilink 全被当成示例藏了起来 ——
# 实测藏起来的有 **271 个引用 / 117 个目标，比露在外面的 234 个还多**。
# 检查只看得见不到一半的链接，还报「✅」。
#
# 正确的边界不是「在不在反引号里」，而是「是不是在讲格式」。
# 九页里 `涉及对象` 表把 wikilink 包进反引号（`results.md` 那张表却没包），
# 同一个 wiki 两种写法——**包不包反引号不该改变一个链接是不是链接**。
FORMAT_EXAMPLES = {'对象页名', '命令对象页'}


def _strip_code(body):
    """只剥围栏块，**保留行内代码跨度**——被反引号包住的 wikilink 仍是链接。"""
    body = re.sub(r'```.*?```', ' ', body, flags=re.S)
    return re.sub(r'~~~.*?~~~', ' ', body, flags=re.S)


def _links(body, page=None):
    """产出该页里的所有 wikilink。排除白名单格式示例，**以及整个语法节**。

    ---

    **⚠️ 2026-09-18 加「切语法节」：它此前是一条假红的来源。**

    实测：`concepts/command-reference.md` 的语法节里**逐字抄着** pattern master file
    的格式，而**那个格式自己就用 `[[ ]]`**：

        [path:

         [<relative_or_absolute_path_1 >]]

    第九类甲把这行读成一个名叫 `path:` 的 wikilink，报了
    「**1 个目标不合 §5**（下划线分隔）」——**目标是错的，页没有错**：
    那段是 §4 规定脚本写、LLM 一个字不许改的逐字原文，
    **里面的 `[[ ]]` 是语料的语法，不是本 wiki 的链接。**

    判据和第七类切它时是**同一条**（见 `_cut_syntax_region` 的注释）：
    语法节归第十二类管（页面 ↔ 脚本逐字节一致），
    **同一段被两个检查管、一个用「逐字」一个用「逐字节」，弱的那条只出噪声。**

    **排除必须报出来**（本文件头的规矩）：语法节还在的页**逐页记进 `STATS`**，
    由调用方印出去——静默缩小范围是本项目明令禁止的。
    """
    body, n_cut = _cut_syntax_region(body)
    if n_cut:
        # **按页记，不按调用次数记**：第八、九类各调一遍，记次数就会是两倍，
        # 而「有几页被排除」才是读的人要知道的那个数。
        STATS.setdefault('语法节不参与链接检查', set()).add(page or '(未传页名)')
    for m in RE_WIKILINK.finditer(_strip_code(body)):
        t = m.group(1).strip()
        # 空目标不可能是页名。实测来源：`log.md` 讲第八类时写的那句 `` `[[ ]]` ``——
        # **讲链接语法的散文**。不排除就多出一个名叫「」的悬空页，还会混进第九类。
        if not t or t in FORMAT_EXAMPLES:
            continue
        yield t


# 链接检查的**适用范围**：内容页（九页 + `index.md`）。`log.md` 不在内。
#
# 理由是硬的：`log.md` 是**记录**，记录必须能引用坏拼法而不因此被判违规
# ——「`[[Integrated_Result_Tool]]` 这种写法是错的」这句话本身是合规的。
# 把检查套到记录上，等于**逼人改历史**：记一条违规就制造一条违规。
# 但排除必须**报出来**，不许静默缩小范围（本文件头「抓不到」一节立的规矩）。
def _content_pages():
    return sorted(p for p in WIKI.rglob('*.md') if p.stem != 'log')


# **`_content_pages()` 和 `_skip_prose()` 不是同一个东西，别合并。**
#
# `_content_pages()` 是**链接检查**的范围（第八、九类）：它**包含**目录页——
# 目录页里的 `[[ ]]` 一样得指得到东西（这条不是我推的：`index.md` 里那个
# `[[versions/index]]` 就是靠它抓出来的）。
# `_skip_prose()` 是**散文检查**的范围（第七类「引文逐字」）：目录页是机器汇编的
# 清单，没有散文可查，**查了也只是空转**。两个口径确实不同，**不同就得有两个名字**。
# （反过来错的那次叫 `_other_pages()`：两处口径不同却共用一个函数，
#  于是第三类和第六类只能有一个数——见 `page_of_type()`。）
#
# 判据**按角色，不按文件名**：2026-09-18 之前这里写的是 `p.stem in ('log', 'index')`。
# 那两个名字当时确实只属于元文件，所以它一直是绿的——**但它是碰巧绿的**：
#   ① 将来任何一个叫 `index` 的内容页（比如讲「index」这个对象的页）会被**静默豁免**；
#   ② 反过来，把子索引改名（`index.md` → `index-versions.md`）会**静默把它拉进检查**。
# **「改个文件名就改变检查范围」本身就是缺陷**，不是风格问题。
# §7 已经把子索引命名为 `index-<类型>.md`，所以按**名字模式**认它们是稳的。
def _skip_prose(p):
    return (p.parent == WIKI and p.name in ('log.md', 'index.md')) \
        or p.name.startswith('index-')


def cat8_reachable(pages):
    """第八类 · **链接目标可达**。内容页的 `[[ ]]` 指向的页，找不找得到。

    三版：一版只扫九页（漏了 `index.md`）→ 二版扫全 wiki（把 `log.md` 也扫了，
    于是它记的那句 `` `[[ ]]` `` 成了空目标悬空链）→ 三版**只扫内容页**。
    """
    # 标题里原先写的是「**忽略代码跨度内的格式示例**」——**这句是假的，代码从来没这么干过**。
    # 口径是「**按名字白名单**排除格式示例」（`FORMAT_EXAMPLES`，两项，能眼睛核），
    # 代码跨度里的 wikilink **照样算链接**，而且必须算（理由见 `FORMAT_EXAMPLES` 上面那段）。
    # 假在哪：它把「排除两项白名单」说成了「排除一整类位置」。前者能核，后者不能——
    # **一个没法核的口径描述，会让下一个人以为反引号是免检的**，
    # 于是他自己写的解释性句子会被算成悬空目标，而他会去怀疑代码。
    #
    # 这个坑 2026-09-18 真踩了：`cross-card-ganging-requires-ddic.md` 里我写
    # 「所以按 §9.1 **本页不写 `[[ddic]]`**」——**讲「不链它」的散文本身链了一个**，
    # `ddic` 于是成了 refs=1 的悬空目标，总数 257 而不是 256。
    # 处置：① 散文改写成不写双方括号的形状（已写进 §9.1）；② **不改检查**
    # ——漏报比误报危险，`FORMAT_EXAMPLES` 那段已经栽过一次 271 个引用。
    w('## 第八类 · 链接目标可达（**抓断链；排除项是名字白名单两项，'
      '行内代码跨度里的 wikilink 照样算**）')
    w()
    files = _content_pages()
    have = {p.stem for p in WIKI.rglob('*.md')}
    refs, where = defaultdict(int), defaultdict(set)
    for p in files:
        for t in _links(p.read_text(encoding='utf-8'), p.stem):
            refs[t] += 1
            where[t].add(p.stem)
    dang = {t: n for t, n in refs.items() if t not in have}
    w(f'- 内容页共 **{len(files)}** 页，引用 **{len(refs)}** 个目标，'
      f'其中 **{len(dang)}** 个找不到对应页。')
    # 口径指纹：本类第一版报 247、改完后报 243，**两个数不可比**——
    # 因为中间同时改了口径（log.md 进/出、空目标跳/不跳）**和** slug 拼法，
    # 中间态没留，那 4 的差再也复现不出来。
    # 教训：**一次只改一个口径**，否则自己的数字先对不上账。
    # 这行把口径钉成可复算的——变了就是变了，不会再和上一版混着比。
    fp = hashlib.sha256()
    for p in files:
        fp.update(p.read_bytes())
    w(f'- 口径指纹：内容页 {len(files)} 个文件、白名单 {len(FORMAT_EXAMPLES)} 项、'
      f'空目标跳过、`log.md` 不计入，`sha256[:12] = {fp.hexdigest()[:12]}`。')
    w()
    if dang:
        w('> **这不是页面的缺陷，是建页 backlog。** 它列的是**脊椎已经要求**的页——')
        w(f'> 比按 `in_src` 排的「{STATS["cand"]} 个高入度对象」更有用：那些只是"语料里常出现"，')
        w('> 这些是"流程页已经伸手去要了"。')
        w()
        w('| 悬空目标 | 被引 | 引用它的 stage |')
        w('|---|---|---|')
        for t, n in sorted(dang.items(), key=lambda x: (-x[1], x[0])):
            w(f'| `{t}` | {n} | {", ".join(sorted(where[t]))} |')
        w()
        # 工作单由**产出这个数的同一段代码**写。原先的 `dangling.csv` 是早先手敲命令
        # 生成的，没有任何脚本认领它——于是它停在 244 行，而报告已经报 252，
        # 里面还留着 `tpi-program-routines`、`test-suite-control-api` 两个**已经建好**的页。
        # **一份没人认领的工作单，会一直绿着骗人**（本项目的老毛病）。
        # 写完断言行数 == 报告里的数：清单和报告永远是同一个数（同 `unowned.py`）。
        with (OUTDIR / 'dangling.csv').open('w', encoding='utf-8', newline='') as f:
            wr = csv.writer(f)
            wr.writerow(['slug', 'refs', 'stages'])   # **表头必须在第 1 行**
            f.write('# 第八类产出：内容页伸手要、但还不存在的页。**由 verify_stages.py 写，不许手改。**\n')
            f.write('# 判据见 `wiki/schema.md` §9.1；refs = 被引处数，stages = 引用它的页。\n')
            for t, n in sorted(dang.items(), key=lambda x: (-x[1], x[0])):
                wr.writerow([t, n, ' '.join(sorted(where[t]))])
        # 注释行要显式跳过再数——**`csv.DictReader` 会把第 1 行当表头**，
        # 若注释写在表头之前，它就拿注释当字段名（`wiki-plan.csv` 栽过：`KeyError: 'slug'`）。
        n_rows = 0
        with (OUTDIR / 'dangling.csv').open(encoding='utf-8', newline='') as f:
            rd = csv.reader(l for l in f if not l.startswith('#'))
            next(rd)                                  # 表头
            n_rows = sum(1 for r in rd if r)
        assert n_rows == len(dang), f'工作单 {n_rows} 行 != 报告 {len(dang)} 个：两者必须同源同数'
    # 顺便：九页互链是否成环（脊椎必须成链）
    w('> 九页之间的互链见第五类；本类只看**指向未建页**的链接。')
    w()
    return True


# §5 的合法 slug：小写 + 连字符（点号留给版本页如 `7.10.3`）。
SLUG_RX = re.compile(r'[a-z0-9]+(?:[-.][a-z0-9]+)*')


def cat9_naming(pages):
    """第九类 · **命名是否合规**（schema §5）。

    **三件独立的事。后两件 2026-09-18 才补上：**

    - **甲 · 链接目标**：`[[ ]]` 里写的名字合不合 §5。
    - **乙 · 文件名本身**：页面自己的文件名合不合 §5。
    - **丙 · stem 不许撞**：两个文件不许共用一个 stem。

    甲早就有了；乙丙**一直没有**。于是这一类名叫「命名合规」，
    **实际只查「被链到的名字」**——**一个没人链的页叫什么名字，它一个字都不看。**

    这不是假设。`wiki/versions/index.md` 与 `wiki/index.md` **共用 stem `index`**，
    而全库的检查一律按 stem 建集合（第八/九类的 `have`、第六类的跳过、第十一类的
    `lookup`）——**两个文件在集合里是同一个东西**，谁遮谁取决于遍历顺序。
    它挂了半天没被发现，直到我在 `index.md` 里写下 `[[versions/index]]`（想链它），
    **甲**才报 ❌。**报的是那个链接，不是那个文件**——把链接换个写法，它就又绿了。
    **丙**才是直接查那个文件的那一条；它当时就该红。

    > 本仓库那个病的**第十次**：**检查比它自称的范围窄，而窄掉的那块一直是绿的。**
    > （前九次见 `schema.md` §13.1。第一到九次全是「范围」，第十次是**「判据的对象」**
    > ——前九次漏的是**哪些页/哪些块**，这次漏的是**同一批页的另一个属性**。）
    """
    w('## 第九类 · 命名合规（**schema §5**）')
    w()
    all_pages = sorted(WIKI.rglob('*.md'))

    # ── 乙：文件名本身 ──
    bad_file = [p for p in all_pages if not SLUG_RX.fullmatch(p.stem)]

    # ── 丙：stem 撞名 ──
    by_stem = defaultdict(list)
    for p in all_pages:
        by_stem[p.stem].append(p.relative_to(WIKI).as_posix())
    dup = {k: v for k, v in by_stem.items() if len(v) > 1}

    # ── 甲：链接目标 ──
    have = set(by_stem)                 # 按 stem——**所以丙必须先红，甲才可信**
    bad = defaultdict(set)
    n_tgt = 0
    for p in _content_pages():
        for t in _links(p.read_text(encoding='utf-8'), p.stem):
            n_tgt += 1
            if t in have:
                continue
            if SLUG_RX.fullmatch(t):
                continue
            if re.search(r'[一-鿿]', t):
                bad['含中文（§5：文件名必须 ASCII）'].add(t)
            elif t.upper() == t and re.search(r'[A-Z]', t):
                bad['全大写（§5：本名小写，如 psfc 不是 PSFC）'].add(t)
            elif '_' in t and not t.startswith('02.'):
                bad['下划线分隔（§5：连字符分隔）'].add(t)
            else:
                bad['其它不合 kebab-case 的写法'].add(t)

    # 三个数都报出来：**「查了几个」和「红了几个」一样重要**——
    # 一个 0 命中的检查，读者有权知道它到底过了多少个对象。
    w(f'- **乙 · 文件名本身**：**{len(all_pages)} 个文件**逐个验过，'
      f'**{len(bad_file)} 个不合 §5**。')
    w(f'- **丙 · stem 唯一**：{len(all_pages)} 个文件占 **{len(by_stem)} 个 stem**，'
      f'**{len(dup)} 个撞名**。')
    w(f'- **甲 · 链接目标**：内容页引用 **{n_tgt}** 处，'
      f'其中 **{sum(len(v) for v in bad.values())} 个目标不合 §5**。')
    # **排除必须报出来**（本文件头的规矩）。2026-09-18 加：语法节整段不再参与链接检查，
    # 而它是**逐字原文**——里面本来就可能出现 `[[ ]]`（语料自己的语法）。
    # 不报这一行，读者会以为「查了全库每一个 `[[ ]]`」，而其实有些页有一大段没查。
    _ex = sorted(STATS.get('语法节不参与链接检查') or ())
    if _ex:
        w(f'- ⚠️ **语法节整段不参与链接检查**：**{len(_ex)} 页**有脚本写的语法节，'
          '已整段切掉（' + '、'.join(f'`{s}`' for s in _ex[:8])
          + ('…' if len(_ex) > 8 else '') + '）。')
        w('  **理由**：那一段是 §4 规定**脚本写、LLM 一个字不许改**的逐字原文，'
          '它由**第十二类**用更硬的口径管（页面 ↔ 脚本逐字节一致）。'
          '实测 `concepts/command-reference.md` 的语法节里抄着 pattern master file 的格式，'
          '而**那个格式自己就用 `[[path: …]]`**——不切，甲就会报一个名叫 `path:` 的'
          '「下划线分隔」违规，**而那是假红**。')
    w()
    if bad_file:
        w(f'❌ **文件名不合 §5 的 {len(bad_file)} 个**——**这一条此前根本不存在**，')
        w('它抓的是「没人链的页起了个非法名字」，**正是甲看不见的那块**：')
        w()
        for p in bad_file:
            w(f'- `{p.relative_to(WIKI).as_posix()}`')
        w()
    if dup:
        w(f'❌ **{len(dup)} 组文件共用同一个 stem**——**页面身份就是 stem**，')
        w('全库检查都按 stem 建集合，**两个文件在集合里是一个东西**。')
        w('谁遮谁取决于遍历顺序，**而且没有任何一处会报错**（§13 那条「老建重复页」的反面）。')
        w()
        for k, v in sorted(dup.items()):
            w(f'- `{k}` ← {", ".join("`" + x + "`" for x in sorted(v))}')
        w()
    if not bad:
        w('- ✅ 甲无违规。')
    else:
        tot = sum(len(v) for v in bad.values())
        w(f'- ❌ **{tot} 个目标不合 §5。** 同一个对象在不同页被写成不同 slug，')
        w('  建页时就会建出重复页——**这正是 §13 说的「老建重复页」，要在建页前收掉。**')
        w()
        for reason, slugs in sorted(bad.items(), key=lambda x: -len(x[1])):
            w(f'**{reason}**（{len(slugs)} 个）：')
            w()
            for x in sorted(slugs):
                w(f'- `{x}`')
            w()
    # 第一版这里无条件 `return True`，于是报告里同时出现
    # 「❌ 21 个目标不合 §5」和汇总行的「✅ 通过」——**自相矛盾的报告比没有报告更坏**。
    # §5 是硬约束，页面违反了就是页面错，返回 False。
    return not bad and not bad_file and not dup


def cat10_dedup(pages):
    """第十类 · **重复投放**（语料结构事实，影响枢纽计数与 sources 计数）。

    TDC 把同一篇页投放在多个章下：字母序命令索引、各专题章、GUI 工具章。
    判据是 frontmatter 的 `source_topic`，去掉 `_2` `_3` 这类后缀后相同即同一篇。
    """
    w('## 第十类 · 语料重复投放')
    w()
    docs = [json.loads(l) for l in open(OUTDIR / 'docs.jsonl', encoding='utf-8')]

    def canon(d):
        t = ((d.get('frontmatter') or {}).get('source_topic') or '').strip()
        if not t:
            return None
        if t.lower().endswith('.htm'):
            t = t.rsplit('.', 1)[0]
        return re.sub(r'_\d+$', '', t)

    by = defaultdict(list)
    n_ofm = 0
    for d in docs:
        c = canon(d)
        if not c:
            n_ofm += 1
            continue
        by[c].append(d['rel'])
    dups = {k: v for k, v in by.items() if len(v) > 1}
    extra = sum(len(v) - 1 for v in dups.values())
    w(f'- 物理文档 **{len(docs):,}** 篇 → 唯一 TDC 页 **{len(by):,}** 个'
      f'（无 `source_topic` 的 {n_ofm} 篇是各章 `index.md`）。')
    w(f'- 重复投放：**{len(dups)}** 个页，涉及 {sum(len(v) for v in dups.values()):,} 篇，'
      f'**冗余 {extra} 篇**。')
    w()
    w('**为什么这件事必须记下来：**')
    w()
    w('1. `hubs.csv` 的 `in_src` 会被灌水——同一篇页存在 5 份，就有 5 份引用各记一次。')
    w('   实测 `WSUS` 121 → **62**、`PSFC` 119 → 约六成。**index.md 的建页优先级表按旧数排的。**')
    w('2. 页面 `sources:` 里同篇列两个路径，会让「677 条来源」这种计数虚高。')
    w('3. 「两篇文档都说 X」可能只是**一篇被投了两次**——§10 的冲突判定必须先做这一步。')
    w()
    top = sorted(dups.items(), key=lambda x: -len(x[1]))[:5]
    w('| source_topic | 份数 | 投放位置 |')
    w('|---|---|---|')
    for k, v in top:
        w(f'| `{k}` | {len(v)} | {"<br>".join(x.split("/")[-1] for x in v)} |')
    w()
    w('> **§10 冲突判定的前置步骤：先查是不是同篇重复投放，再谈版本、再谈并列。**')
    w()
    return True


RE_TABLEROW = re.compile(r'^\|(.+)\|\s*$', re.M)
RE_SEP = re.compile(r'^\|[\s\-:|]+\|$')


def _object_table(body):
    """把「## 涉及对象」下的对象与层读出来，**两种形态都吃**：

    1. 表格：`| [[dfpn]] | L1 | 说明 |`
    2. 列表：`- `[[dfpn]]` `L1` — 说明` 或 `- [[x]]（file，…) — 说明`

    第一版只吃表格，于是 `pin.md` / `pattern.md` 的该节被判「不是表格」，
    机器读不到层——**那不是页面的毛病，是我的解析器窄**。
    （九页里两种形态并存是真的，属于该归一的地方；但**为了检查去改内容**是本末倒置，
    所以先让解析器都吃，形态归一单独记 backlog。）
    """
    seg = _section_body(body, '涉及对象')
    rows = [m.group(1) for m in RE_TABLEROW.finditer(seg)]
    if rows:
        cells = [[c.strip() for c in r.split('|')] for r in rows]
        return [c[:3] for c in cells
                if len(c) >= 3 and not RE_SEP.match('|' + '|'.join(c) + '|')]
    out = []
    for line in seg.split('\n'):
        if not line.lstrip().startswith(('-', '*')):
            continue
        links = RE_WIKILINK.findall(line)
        if not links:
            continue
        tail = line.split(']]', 1)[1] if ']]' in line else ''
        m = (re.search(r'`(L1|L2|L3|file|gui|concept)', tail)
             or re.search(r'[（(](L1|L2|L3|file|gui|concept)', tail))
        if not m:
            continue
        out.append([links[0].strip(), m.group(1), tail.strip()])
    return out or None


def cat11_layer(pages):
    """第十一类 · **层断言的一致性**（不是「层判得对不对」）。

    先把这条检验**做不到什么**写清楚，免得又有人（包括我）再造一遍：

    **「对象属于哪层」不能靠查文档章节判。** 第一版这么干，4 条全是误报：
    `run()` 是 L2 API，而讲它的教学文档在 `01.06`；`FW_TASK` 是 L1 命令，
    而讲「怎么从 test method 调它」的文档在 `02.07`。
    **对象属于哪层**和**讲它的文档在哪章**是两件事，章节结构里没有这个信息。
    而且这跟本文件头那句话是一回事：机器引对了文档，不等于引对了层。

    能机械判的是另一件事：**同一对象在两个页里被标成不同层**。
    这是纯内部一致性——不需要知道哪层对，只需要知道两页不一致。
    归一规则：取层单元格开头的受控 token（`L1`/`L2`/`L3`/`file`/`gui`/`concept`），
    其后的字（`L2 参数类型`、`L2 + file`）算补充说明，不参与比较；
    但**仍然把原始写法印出来**——措辞漂移本身值得看见。
    """
    w('## 第十一类 · 层断言的一致性（**跨页**）')
    w()
    own = defaultdict(list)      # 对象 -> [(页, 原始层写法)]
    nrows = 0
    notables = []
    for s in STAGES:
        if s not in pages:
            continue
        _, body = pages[s]
        tbl = _object_table(body)
        if tbl is None:
            notables.append(s)
            continue
        for c in tbl[1:]:
            nrows += 1
            for t in RE_WIKILINK.findall(c[0]):
                own[t.strip()].append((s, c[1]))
    if notables:
        w(f'- ⚠️ **{len(notables)} 页的「涉及对象」不是表格，没有层列**：'
          f'{", ".join("`" + x + "`" for x in notables)} —— '
          f'这些页的对象**机器读不到层**，只能人读。')
        w()
    def _tok(lay):
        # **必须取 `group(0)`**：第一版直接往集合里放 `re.match(...)` 的返回值，
        # 而 Match 对象即使匹配同一段文字也互不相等——于是 `level=L1 | timing=L1`
        # 这种**两边完全一样**的行被报成「层不一致」，22 条全是假的。
        # 又一次「检查的错被当成页面的错」。
        m = re.match(r'(L1|L2|L3|file|gui|concept)', lay)
        return m.group(0) if m else None

    clash = {o: v for o, v in own.items()
             if len({t for t in (_tok(x[1]) for x in v) if t}) > 1}
    drift = {o: v for o, v in own.items()
             if len({x[1] for x in v}) > 1 and o not in clash}
    w(f'- 覆盖 {len(own)} 个对象、{nrows} 行。')
    if clash:
        w(f'- ❌ **{len(clash)} 个对象的层在两页里不一致**（归一后仍是不同的层）：')
        w()
        w('| 对象 | 各页的写法 |')
        w('|---|---|')
        for o, v in sorted(clash.items()):
            w(f'| `{o}` | {"<br>".join(f"{p}={lay}" for p, lay in v)} |')
        w()
    else:
        w('- ✅ 没有对象在两页里被标成**不同的层**。')
    if drift:
        w(f'- ℹ️ {len(drift)} 个对象只是**措辞不同、层相同**：')
        for o, v in sorted(drift.items()):
            w(f'    - `{o}`：{" / ".join(f"{p}={lay}" for p, lay in v)}')
    w()
    return not clash and _layer_vs_object_pages(own, _tok)


def _layer_vs_object_pages(own, _tok):
    """**同一对象页的 `layer:` 字段，和 stage 页表格里那一行，说的是不是同一层。**

    不补这一条，第十一类就有个说不通的盲区：它的整个存在理由是「别让同一个对象
    在两个地方被标成两层」，而对象页恰恰是**新出现的一个「地方」**——
    页里 `layer:` 是正儿八经的层断言，比表格单元格还正式（那是 §6 的必填字段）。
    只查表格不查字段，等于**新开的那个口子没人看**。

    匹配用 `norm()`（同 cat6）：对象页的 `title` 归一后去撞表格里的 wikilink 文本。
    **撞不上不算错**——表格收的是流程相关对象，对象页可以不在任何一段的表格里
    （§12 那批「不属于任何 stage」的正是如此）。撞上了才比。
    """
    w('### 第十一类续 · 对象页 `layer:` vs 舞台页表格')
    w()
    pages = _other_pages()
    if not pages:
        w('*（还没有这类页）*')
        w()
        return True
    def _norm(x):
        return re.sub(r'[^a-z0-9]', '', x.lower())
    lookup = defaultdict(list)
    for o, v in own.items():
        lookup[_norm(o)].append((o, v))
    ok, rows, miss = True, [], []
    for p in pages:
        fm, _ = parse_page(p)
        lay = fm.get('layer')
        if not lay:
            continue
        title = fm.get('title') or p.stem
        hit = lookup.get(_norm(title)) or lookup.get(_norm(p.stem))
        if not hit:
            miss.append((p.parent.name + '/' + p.name, title, lay))
            continue
        for o, v in hit:
            other = sorted({x[1] for x in v})
            same = all(_tok(x) == _tok(lay) for x in other)
            ok &= same
            rows.append((p.parent.name + '/' + p.name, title, lay,
                         ' / '.join(f'{s}={x}' for s, x in v), same))
    if rows:
        w('| 对象页 | 对象 | 页里 `layer:` | stage 表格里写的 | 一致 |')
        w('|---|---|---|---|---|')
        for a, b, c, d, same in rows:
            w(f'| `{a}` | {b[:40]} | `{c}` | {d} | {"✅" if same else "❌"} |')
        w()
    else:
        w('- 没有对象页的名称能撞上任何 stage 页的「涉及对象」表格。')
        w('    **这不代表检查坏了**：拿表格里的真名（`technology-file`、`shmoo-tool` …）'
          '当合成标题探过，都能命中并取到层写法。')
        w('    空的原因是**这一批 6 页恰好全是「九页一个字都没提」的那批对象**'
          '（第六类的「已建页」正是从「未归属」里出列的）——')
        w('    也就是说，**它们本来就没有第二处层断言可比**。'
          '等建到「stage 页已经提过、又补了对象页」的对象时，这条才会开始出力。')
        w()
    if miss:
        w(f'- ℹ️ {len(miss)} 页的层**没有第二处可以对照**（表格里没有它）——'
          '这不是错，是「**这层只有页自己说了算，机器无从复核**」：')
        for a, b, c in miss:
            w(f'    - `{a}` — `layer: {c}`')
        w()
    return ok


def cat12_syntax_fresh():
    """第十二类 · **页面里脚本写的那一节，和脚本现在的产出，是不是同一个东西**。

    **为什么补这一条（2026-09-18）**：§4 把一页劈成两半——语法节是脚本的，
    散文是 LLM 的。**脚本改了抽取逻辑之后，没有任何一条检查会告诉你哪些页面过期了**；
    `--refresh-syntax` 得**先知道**要刷哪几个 slug，而**手工挑就会漏，漏掉的页面看上去完全正常。**

    这一天真的发生了：修 `verbatim_sections` 的盲区（全语料 256 篇受影响）之后，
    我是**手工挑了两个 slug** 去刷的，靠 `check_syntax_fresh.py` 才发现实际有
    **4 个**页面过期——其中两个（`data-navigation-views`、
    `cct-multiport-sequencer-synchronizer-api`）的语法节**原本是「无」**，
    而它们的「无」**是从抽取器的盲区推出来的**。

    **它查的是前三面镜子都没照到的那一面**：页面 ↔ 产出它的脚本。
    """
    import check_syntax_fresh as csf
    print('第十二类：语法节新鲜度…')
    stale = csf.main()
    # **从 dict 里按名字取，不做位置解包。** 原来写的是
    # `n_fresh, _, n_missing = csf.LAST_COUNTS`——2026-09-18 加第四项
    # （「该有语法节却没有」）时才发现那是个 `ValueError` 陷阱：
    # **位置解包和硬编码数字是同一个病**，结论的形状被写死在读的人那里。
    # 装的是**清单**，`len()` 由读的人自己算——数字和名单不可能对不上。
    L = csf.LAST
    unmarked = L['unmarked']
    w('## 第十二类 · 语法节与抽取器当前产出一致（**页面 ↔ 脚本**）')
    w()
    if not stale and not unmarked:
        w(f'✅ **{len(L["fresh"])} 个已建页的 `## 语法 / 参数` 与 `objscaffold.py` '
          '现在的产出逐字一致。**')
        w()
        w(f'> **这一条查了哪些、没查哪些，都写出来**（§13.1 第 ⑥′ 问）：'
          f'逐字比了 **{len(L["fresh"])}** 页；'
          f'**{len(L["prose"])}** 页是纯散文页（`constraint` / `error` / `stage`），'
          f'按设计没有脚本写的一节，**不参与比较**；'
          + (f'**{len(L["missing"])}** 页 plan 里有、文件未建。' if L['missing'] else ''))
        w('> 判据是**两个方向都封死**的：`object` / `concept` 页**必须**带'
          '`<!-- 语法节 begin -->` 标记（没有就是红——旧写法会**静默跳过**它，'
          '那正是本文件头说的「检查比自称的范围窄」），'
          '带标记的页**一律逐字比**。')
    else:
        if stale:
            w(f'❌ **{len(stale)} 个页面的语法节已过期**（脚本换了，页面没跟上）：')
            w()
            w('| 页 | 页面里 | 抽取器现在 | 差 |')
            w('|---|---|---|---|')
            for s, a, b in stale:
                w(f'| `{s}` | {a:,} | {b:,} | {b - a:+,} |')
            w()
            w('修法：`python objscaffold.py --refresh-syntax ' +
              ' '.join(s for s, _, _ in stale) + '`')
            w()
        if unmarked:
            w(f'❌ **{len(unmarked)} 个脚本出骨架的页面（`object` / `concept`）'
              '里没有 `<!-- 语法节 begin -->` 标记。**')
            w()
            w('| 页 | type | 情况 |')
            w('|---|---|---|')
            for s, t, what in unmarked:
                w(f'| `{s}` | `{t}` | {what} |')
            w()
            w('**为什么这条单列**：这 30 页里每一页的语法节都是 `objscaffold.py` '
              '写的（§4）；标记一没，本脚本就**无从判断该从哪里比到哪里**，'
              '于是旧写法**直接跳过它**——')
            w('**检查会变绿，不是因为查过了，是因为它根本没查到东西**（§13.1 第 ⑥′ 问）。')
            w('修法：`python objscaffold.py --refresh-syntax <slug>` 会把整节连标记重写一遍。')
            w()
    w()
    w('> **判据是逐字相等**，不是「看起来差不多」——这一节是脚本写的，'
      '它和脚本的输出**必须**是同一个东西。')
    w('> 边界靠页面里的 `<!-- 语法节 begin/end -->` 标记认。'
      '**没有标记时 `refresh()` 会过一道互锁**：要替换的区间里如果有'
      '「非标准小节」，它**拒绝执行**而不是猜边界——这条互锁是拿一次真实误删换来的'
      '（`cct-multiport-sequencer-synchronizer-api` 被删掉 6 节，已从会话记录恢复）。')
    w('> **底下的教训比这条检查值钱**：脚本对「页面长什么样」的假设，'
      '写成判据就会变成删数据的刀。**边界必须由写它的人留记号，不能由读者推断。**')
    w()
    return not stale and not unmarked


def cat13_version_fresh():
    """第十三类 · 版本页的**两句自我声明**是不是真的。

    版本页页首写着两句：「**机械汇编，没有一句是模型写的**」和「**条目原样转录**」。
    这两句此前**一条检查都没有**——第七类只抠 `>` 引用块和代码块，
    而版本页的条目是**普通列表项**，连第七类的门都进不去。

    **同一个病的第九次**：本 wiki 里唯一一处成规模声称逐字的地方，
    正好落在唯一一类检查之外；而它一直是绿的。

    判据两条独立：甲 = 页面 == `versions.render()` 当前输出；
    乙 = 每条条目**直接回 raw** 找完全子串（不经过 `sections.jsonl`，
    否则抽取器错了它跟着错）。详见 `check_version_fresh.py`。
    """
    import check_version_fresh as cvf
    print('第十三类：版本页新鲜度…')
    n_bad, info = cvf.main(quiet=True)
    w('## 第十三类 · 版本页与抽取器一致、且条目逐字回得到 raw（**页面 ↔ 脚本 ↔ raw**）')
    w()
    if not n_bad:
        w(f'✅ **{info["n_page"]} 个版本页没有一个字偏离 `versions.py` 的当前产出**；'
          f'**{info["n_item"]:,} 条条目全部逐字回得到 raw 的 '
          '`## Functional changes` 段落**。')
        w()
        w('> **这只证明「转录忠实」，不证明「分对了组」。**'
          '把某一条记到错的版本号底下，这一条一样是绿的——'
          '而**分组判据（`- SmarTest X: …` 的 `X`）就在原文里写着，机器只认字面**。'
          '真要查分组，得人拿几条回原文看。')
    else:
        w(f'❌ **{n_bad} 处对不上**：')
        for line in info['lines'][:20]:
            w(f'- {line}')
    w()
    return not n_bad


# `index.md` 里**逐页列出**的六个节，以及它们分别对应哪个目录（§7）。
#
# **`版本` 不在表里，这是有意的**：142 个版本页不由 `index.md` 逐页列出——
# 它只带一行指针 `[[index-versions]]`，而那 143 个文件由**第十三类**管
# （与 `versions.render()` 逐字节一致 + 条目逐字回 raw）。
# **排除必须报出来**，所以下面报告里会单独印一行说它被谁接管了。
IDX_SECTIONS = [
    ('阶段', 'stages'), ('概念', 'concepts'), ('约束', 'constraints'),
    ('映射', 'mappings'), ('对象', 'objects'), ('排错', 'errors'),
]

# 数字声明靠**标记**读，不靠正则猜散文。
#
# `<!-- index-count: 概念 = 8 -->`，写在它描述的那一节里。
# **为什么不用正则去猜散文里的数字**：散文会被改写，而**改写了正则就找不到**——
# 找不到时若判「通过」，检查就自己消失了；若判「红」，那每次润色都变红。
# 两条路都坏。**边界必须由写它的人留记号**——这句话是第十二类拿一次真实误删换来的
# （`objscaffold` 的 `<!-- 语法节 begin/end -->`，见那条注释）。
IDX_COUNT_RX = re.compile(r'<!--\s*index-count:\s*([^=]+?)\s*=\s*(\d+)\s*-->')

# 散文里仍然**逐条登记**的几处数字声明：`(正则, 捕获组转换器, 真值函数, 说明)`。
# 这三条是本次手工捞出的假账里能被正则稳稳抓住的部分。
# **正则不匹配时不判错，但要计数并印出来**——见函数里的 `n_miss`。
#
# **真值一律从目录现数，不从散文里再读一遍**——否则就是在拿散文核散文。
_CN_NUM = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6,
           '七': 7, '八': 8, '九': 9, '十': 10}


def _cn2int(s):
    """`一`…`十` → 整数。**认不出来就是 `None`**，由调用方判错，不猜。"""
    return _CN_NUM.get(str(s).strip())


IDX_PROSE_CLAIMS = [
    # **`（五条）` 里没有空格**——第一版照着脑子里那句写成 `（N 条）`，
    # 于是它永远匹配不上，而报告里只会印一行 ℹ️「这句没找到」。
    # **那就是丙这一条的失败模式本身**：措辞猜错了，检查静默失效。
    (r'(?m)^## 已知缺口（([一二三四五六七八九十]+)条）',
     _cn2int, lambda c: c['缺口条数'], '已知缺口（N 条）'),
    (r'## 阶段（脊椎，(\d+)）',
     int, lambda c: len(c['stages']), '阶段（脊椎，N）'),
    # ⚠️ **这一条 2026-09-20 删掉了**（原来是「对象 N 页 + 概念 N 页（下一节）= N 页」）。
    # 两个理由，都值得记：
    # ① **它的正则和原文差一个字**——登记写「（**下一节**）」，原文是「（**上一节**）」，
    #    于是这条声明**一直印「这句没找到」、一直没被查过**。**和 §13.1 第十六次一模一样**
    #    （那次是 `（N 条）` 多了个空格）。**措辞猜错 = 声明静默死亡。**
    # ② 那句话本身**是历史数**（「98 页 + 22 页 = 120 页」，后面的批次一建就过期），
    #    而它下面自己就写着「这个数不必手写」。**那就别写数**——
    #    已把散文改成不声明数字，登记项随之删掉。
    #
    # **换上来的是下面这一条**：`index.md` 开头那行括号里**六个分类的现值**。
    # 它此前**完全没人管**（丙 的报告自己写着「没登记进表的散文数字本类一概不管」），
    # 而它**正好在 2026-09-20 就是错的**（写着对象 143，实际 146）——
    # **又一次「一处声称 X 的地方，正好落在唯一一类检查之外」。**
    (r'（脊椎 (\d+) / 概念 (\d+) / 约束 (\d+) / 对象 (\d+) / 排错 (\d+) / 映射 (\d+)）',
     lambda *g: tuple(int(x) for x in g),
     lambda c: (len(c['stages']), len(c['concepts']), len(c['constraints']),
                len(c['objects']), len(c['errors']), len(c['mappings'])),
     '（脊椎 N / 概念 N / 约束 N / 对象 N / 排错 N / 映射 N）'),
]


def cat14_index_claims():
    """第十四类 · **`index.md` 自己的声明是不是真的**（目录页 ↔ 目录）。

    **为什么补这一条（2026-09-18）**：填「约束」「排错」两节时顺手核了一遍，
    **一趟手工捞出四处假账**，四处**都没有灯看着**：

    | 原文写 | 实际 | 根因 |
    |---|---|---|
    | `### 已知缺口（六条）` | 五条 | 没有第六条；`log.md` 里也找不到它的来历 |
    | `对象 21 页 + 概念 7 页 = 28 页` | 22 / 8 / 30 | **两页建好了没人填进这张目录** |
    | `第二批（13 页）` | 它自己只列了 12 条 | 批次标题的数字和它列的内容对不上 |
    | 悬空表 `model-file 4 页` | 9 | 上一批建完页没更新 |

    **第八类抓不到这些**：它只问「`[[ ]]` 指不指得到东西」。
    「页面建好了但目录里没列」对它来说是**完全正常的**——那个链接压根不存在，
    它没得可查。**这正是 §7 那条「每次 ingest 后更新」的规则没有检查看着的样子。**

    三件事，判据不同：

    - **甲 · 漏列**（硬）：`wiki/<目录>/` 里每一页，都必须在 `index.md` 对应节里被列出。
      这是**这次真正抓到东西**的那一条（`pogocabling-section` / `hv-protection` 建好没登记）。
    - **乙 · 标记数**（硬）：每一节 + `已知缺口` 都要有一个 `<!-- index-count: … -->` 标记，
      **数必须等于实际**。缺标记、重复标记、对不上——三种都红。
    - **丙 · 散文数字**（硬，但正则不匹配时**只计数不判错**）：
      三条登记在 `IDX_PROSE_CLAIMS` 里的声明，逐条回真值。

    **不查的**：`版本`（第十三类接管，理由见 `IDX_SECTIONS` 上面）、
    以及「节里列了一个别的类型目录下的页」——那是合法的交叉引用，只 ℹ️ 提示。

    **⚠️ 这一条只保证「目录和目录里的文件对得上」，不保证「目录里那句介绍写得对」。**
    一句话有没有说错、`related` 指得对不对，**机器判不了，还是得人读**。
    """
    w('## 第十四类 · 手写文件的自我声明是不是真的（`index.md` / `wiki-plan.csv` / token 预算）')
    w()
    ok = True
    txt = (WIKI / 'index.md').read_text(encoding='utf-8')
    # 按 `## ` 切节。**用二级标题切，不按顺序猜**——节序会变，标题不会。
    parts = re.split(r'(?m)^## ', txt)
    secs = {}
    for chunk in parts[1:]:
        name = chunk.split('\n', 1)[0].strip()
        secs[name] = chunk
    have_dirs = {d: sorted((WIKI / d).glob('*.md')) for _, d in IDX_SECTIONS}
    allstems = {p.stem for p in WIKI.rglob('*.md')}

    # ---- 甲 · 漏列 ----
    w('### 甲 · 每一页都在它那一节里被列出了吗')
    w()
    w('| 节 | 目录 | 目录里有 | 节里列了 | 漏列 | 列了但不存在 | 列了别的类 |')
    w('|---|---|---|---|---|---|---|')
    n_missing_tot = 0
    for name, d in IDX_SECTIONS:
        sec = None
        for k, v in secs.items():
            if k.startswith(name):
                sec = v
                break
        if sec is None:
            w(f'| `{name}` | `{d}/` | — | — | ❌ **整节不见了** | — |')
            ok = False
            continue
        listed = set(_links(sec))
        files = {p.stem for p in have_dirs[d]}
        missing = sorted(files - listed)
        ghost = sorted(t for t in listed if t not in allstems)
        # **「多出来的」不是罪，但必须点名。** 节里除了本类的页，还会交叉引用别的类的页
        # （`概念` 里引一个 `constraint` 是正常的）。不印出来的话，
        # 「目录里有 8、节里列了 9」这行就**没法解释**——而没法解释的数
        # 和错数长得一样，读的人只能当没看见。
        foreign = sorted(t for t in listed if t in allstems and t not in files)
        n_missing_tot += len(missing)
        w(f'| `{name}` | `{d}/` | {len(files)} | {len(listed)} | '
          + (f'❌ {", ".join("`" + m + "`" for m in missing)}' if missing else '✅ 无')
          + ' | '
          + (f'❌ {", ".join("`" + g + "`" for g in ghost)}' if ghost else '✅ 无')
          + ' | '
          + (', '.join(f'`{f}`' for f in foreign) if foreign else '—')
          + ' |')
        if missing or ghost:
            ok = False
    w()
    # **被接管的边要说出来**，否则「没查」和「查了没问题」长得一样。
    w('> **本类不查 `版本` 节**：它不逐页列出——`index.md` 只带一行指针 `[[index-versions]]`，'
      '那 143 个文件由**第十三类**管（与 `versions.render()` 逐字节一致 + 条目逐字回 raw）。'
      '**被接管的范围要报出来，不然它和「没人管」长得一样。**')
    w()
    w('> **「列了但不存在」与第八类重叠**，这里是**按节**再看一遍：'
      '第八类只知道「有个 `[[ ]]` 指不到东西」，不知道**它写在哪个节里**——'
      '而「写在对象节里却指到别处」和「写在正文里指到一个还没建的页」是两件事。')
    w()

    # ---- 乙 · 标记数 ----
    w('### 乙 · `<!-- index-count: … -->` 标记的数对不对')
    w()
    marks = defaultdict(list)
    for k, v in IDX_COUNT_RX.findall(txt):
        marks[k.strip()].append(int(v))
    w('| 声明 | 标记写的 | 实际 | 结果 |')
    w('|---|---|---|---|')
    # `已知缺口` 的数：数 `**一、` 这种段落。**判据和下面丙里那条同源**，只算一次。
    gap_n = len(re.findall(r'(?m)^\*\*[一二三四五六七八九十]、', txt))
    truth = {name: len(have_dirs[d]) for name, d in IDX_SECTIONS}
    truth['已知缺口'] = gap_n
    for key in [n for n, _ in IDX_SECTIONS] + ['已知缺口']:
        got = marks.get(key, [])
        if not got:
            w(f'| `{key}` | ❌ **没有标记** | {truth[key]} | ❌ |')
            ok = False
        elif len(got) > 1:
            w(f'| `{key}` | ❌ **有 {len(got)} 个标记** | {truth[key]} | ❌ |')
            ok = False
        else:
            good = got[0] == truth[key]
            w(f'| `{key}` | {got[0]} | {truth[key]} | {"✅" if good else "❌"} |')
            ok &= good
    # **多余的标记也要报**：写错了节名（`概念 ` 多一个空格）会变成一个谁也不认的标记，
    # 而上面那张表只会说「`概念` 没有标记」——**说出的是症状，不是原因**。
    extra = sorted(set(marks) - {n for n, _ in IDX_SECTIONS} - {'已知缺口'})
    if extra:
        w()
        w(f'> ⚠️ **还有 {len(extra)} 个对不上任何声明的标记**：'
          + '、'.join(f'`{e}`（{marks[e]}）' for e in extra)
          + '。**多半是节名写错了**（多一个空格、或者改了节名没改标记）——'
            '上面表里的「没有标记」就是这么来的。')
    w()

    # ---- 丙 · 散文数字 ----
    w('### 丙 · 散文里逐条登记的数字声明')
    w()
    # **按键是目录名，不是节的中文名。** `IDX_PROSE_CLAIMS` 里的真值函数写的是
    # `c['stages']`——它认的是**目录**（那是「实际有几个文件」的来源），
    # 而 `阶段` 只是印给人看的标签。第一版按中文名建字典，
    # 于是三条声明里两条**在取真值时就 KeyError 崩掉**。
    ctx = {d: have_dirs[d] for _, d in IDX_SECTIONS}
    ctx['缺口条数'] = gap_n
    w('| 声明 | 写的 | 实际 | 结果 |')
    w('|---|---|---|---|')
    n_miss = 0
    for rx, conv, fn, label in IDX_PROSE_CLAIMS:
        mm = re.search(rx, txt)
        if not mm:
            n_miss += 1
            w(f'| {label} | — | {fn(ctx)} | ℹ️ **这句没找到**（措辞可能改了） |')
            continue
        t = fn(ctx)
        got = conv(*mm.groups())
        if got is None:
            w(f'| {label} | `{mm.groups()}` | `{t}` | ❌ **这个数读不出来**（转换器认不出） |')
            ok = False
            continue
        good = got == t
        w(f'| {label} | `{got}` | `{t}` | {"✅" if good else "❌"} |')
        ok &= good
    w()
    w(f'> **登记了 {len(IDX_PROSE_CLAIMS)} 条散文声明，本次找到 {len(IDX_PROSE_CLAIMS) - n_miss} 条'
      f'{"、**" + str(n_miss) + " 条没找到**" if n_miss else "、全部找到"}。**'
      '**「没找到」不判错**（散文会被改写），**但必须印出来**——'
      '否则改一次措辞，这条声明就**静默地不再被检查**，而报告照样全绿。')
    w('> 没登记进表的散文数字**本类一概不管**：`index.md` 里还有很多「N 页」「N 个」的说法，'
      '**它们没有检查**。这一条只覆盖登记在 `IDX_PROSE_CLAIMS` 里的那些。')
    w()

    # ---- 丁 / 戊 · `wiki-plan.csv` 自己的声明 ----
    # **为什么并进这一类**：这张表的表头写着「**这份文件是「建什么」的唯一记录**」，
    # 而 2026-09-18 实测它两处都不真（20 行 status 是假的、29 行压根没有）。
    # **它和 `index.md` 是同一种东西**：手写的、自我声明的、没人看着的。
    # 差别只是它声明的是「建了没有」，`index.md` 声明的是「列了几页」。
    w('### 丁 / 戊 · `wiki-plan.csv`（「建什么」的唯一记录）和实际对不对')
    w()
    plan_p = OUTDIR / 'wiki-plan.csv'
    ok_plan = True
    if not plan_p.exists():
        w(f'❌ `{plan_p.name}` 不在了——**这张表没了，丁/戊 两条就都没得查**。')
        ok = False
    else:
        w('| 检查 | 判据 | 结果 |')
        w('|---|---|---|')
        # **必须按行切再喂给 DictReader**：表头是第一行，注释在它后面，
        # 直接 DictReader 会把注释行当数据（字段名对不上就 KeyError）。
        raw_lines = plan_p.read_text(encoding='utf-8').split('\n')
        hdr = next(l for l in raw_lines if l.startswith('slug,'))
        body = [l for l in raw_lines
                if l.strip() and not l.startswith('#') and not l.startswith('slug,')]
        prows = list(csv.DictReader([hdr] + body))
        plan_dirs = ['stages', 'objects', 'concepts', 'constraints', 'errors', 'mappings']
        # **值是 `Path`，不是目录名**（2026-09-18 改）：丁 要把这个页面喂给
        # `plan_sync.status_of()` 读正文。原先只存目录名，**那就只能判「文件在不在」**——
        # 而「正文写没写」需要那个文件本身。只用到键的地方（戊）不受影响。
        pdir = {p.stem: p for d in plan_dirs for p in (WIKI / d).glob('*.md')}

        # 丁 · status 跟着文件走
        #
        # **2026-09-18 改：判据从两个值变三个值，而且不再在这里实现。**
        # 原来这里写的是 `'done' if r['slug'] in pdir else 'todo'`——
        # **本类自己实现了一遍 `plan_sync` 的判据**，于是那 71 页骨架
        # 两边都记成 `done`、两边一致地错，**这条检查照样绿**。
        # 「两处实现同一个判据」正是本文件反复记的那个病；
        # 现在两边都调 `plan_sync.status_of()`，**同一个答案只有一个来源**。
        import plan_sync as PS
        wrong_status = []
        for r in prows:
            want = PS.status_of(pdir.get(r['slug']))
            if (r.get('status') or '').strip() != want:
                wrong_status.append(f'{r["slug"]}（写 `{r.get("status")}`，应是 `{want}`）')
        ok &= not wrong_status
        w(f'| **丁** · `status` 和实际进度一致 | 表里每一行 | '
          + ('✅ 一致' if not wrong_status else
             f'❌ **{len(wrong_status)} 行不符**：' + '、'.join(wrong_status[:6])
             + ('…' if len(wrong_status) > 6 else '')) + ' |')

        # 戊 · 每一页都有登记行
        no_row = sorted(set(pdir) - {r['slug'] for r in prows})
        ok &= not no_row
        w(f'| **戊** · 六个类型目录里每一页都在表里 | 目录 ↔ 表，双向 | '
          + ('✅ 都有' if not no_row else
             f'❌ **{len(no_row)} 页没有登记行**：' + '、'.join(f'`{s}`' for s in no_row[:6])
             + ('…' if len(no_row) > 6 else '')) + ' |')
        # **反向也印出来**：表里有、页面不在的行是「计划的**未来**」，那是正常的
        # （下一批就靠它），所以**不判错，但要说清有几行**——
        # 不然「表比页多」看起来和「表坏了」一样。
        future = sorted({r['slug'] for r in prows} - set(pdir))
        w(f'| （反向，**不判错**）表里有、页面还没有 | = 待建 | '
          f'ℹ️ {len(future)} 行{"：" + "、".join(future[:6]) + ("…" if len(future) > 6 else "") if future else ""} |')
        w()
        w('> **为什么 戊 不算多此一举**：`index.md` 的甲抓「建好了没登记进目录」，'
          '戊 抓「建好了没登记进**计划**」——**是两份不同的账**。'
          '上一批真正踩到的坑（`pogocabling-section` / `hv-protection`）'
          '**两份账同时漏**，而当时两条检查都不存在。')
        w('> **`plan_sync.py` 会回填缺的行**（从页面 frontmatter 抄 type/layer/stage）——'
          '**回填不削弱 戊**：它抓的是**下一次**：新页建了却没跑同步、也没进表，照样红。')
        w()

    # ---- 己 · `index.md` 的 token 预算（§7 的硬约束）----
    # **待办 ⑯，2026-09-18 做掉。** 这条硬约束此前「有判据、有量法、有数字、
    # 没有任何检查」——正是本项目反复栽的那个形状。
    # ⚠️ **2026-09-21 修**：这一段原来把预算**硬编码成 15,000**，而 §7 在 2026-09-20
    # 已把它上调到 25,000（`check_index_budget.py` 的 `BUDGET` 就是 25,000）。
    # 于是**判定对、印出来的数错**：`over` 取自 `cib.main`（25,000，判没超），
    # 表里和「余」那一行却按 15,000 算，印出 `余 -1,388`。
    # **这正是本项目反复记的那个形状——「检查的错被当成页面的错」**：
    # 读到那行的人（包括我）会以为 index.md 超了预算。现在预算只从 `cib.BUDGET` 取一处。
    import check_index_budget as cib
    w('### 己 · `index.md` 装得下一个 context window 吗'
      f'（§7 硬约束 < {cib.BUDGET:,} token）')
    w()
    # **把被测文件指到本模块的 `WIKI` 去**，不让它用自己写死的常量——
    # 否则反向测试把 WIKI 搬走之后，「量的是临时那份、比的是真的那份」。
    ok_己, over = cib.main(path=WIKI / 'index.md')
    ok &= ok_己
    got = cib.LAST['measured']
    if got is None:
        w('❌ **未量。** 没装 `tiktoken`，量不出 token 数——')
        w('**分不清「没超」和「没量」的检查等于没有检查**（§13.1 第 ⑥′ 问），')
        w('所以这条按红算。装：`pip install tiktoken`。')
    else:
        top_enc = max(got, key=lambda k: got[k])
        top = got[top_enc]
        dec = cib.LAST['declared'] or {}
        w(f'| 编码器 | 实测 | 页面自己写的 | 对 {cib.BUDGET:,} |')
        w('|---|---|---|---|')
        for k in got:
            d = dec.get(k)
            flag = '' if (d and str(d).lstrip('-').isdigit() and int(d) == got[k]) else ' ❌'
            w(f'| `{k}` | {got[k]:,} | {(f"{d}{flag}" if d else "❌ 没写")} | '
              f'{"**超 %s**" % f"{got[k] - cib.BUDGET:,}" if got[k] > cib.BUDGET else f"+{cib.BUDGET - got[k]:,}"} |')
        bad = {k: got[k] - int(v) for k, v in dec.items()
               if str(v).lstrip('-').isdigit() and k in got and got[k] != int(v)}
        w()
        w(f'**取大的那个当上界：`{top_enc}` = {top:,}，余 {cib.BUDGET - top:,}。**'
          + ('❌ **超了**——按 §7 拆子索引。' if over else ''))
        # ⚠️ **2026-09-21 补**：§7 里除了 25,000 的预算，还有一条 **22,000 的触发线**
        # （「到 22,000 token、或对象到 300 页时，**必须回来重定**」）。
        # 这条此前**没有任何检查在看**，于是报告只印「余 8,612」——
        # **读的人看不出已经越过重定线了**。同 §13.1 第十七次：规格里写了两个数，检查只认一个。
        # **它不判红**：越线不是错，是「该做一次人的决定」；但**要印出来**。
        if top >= cib.TRIGGER:
            w(f'⚠️ **已越过 §7 的触发线 {cib.TRIGGER:,}**（现值 {top:,}，超 {top - cib.TRIGGER:,}）——'
              f'§7 说的是「**必须回来重定**」。**这不是红**（越线不是错），'
              f'**但在没重定之前，它一直挂在这里**——不印就等于把它变成「先放着」。')
        if bad:
            w(f'❌ **页面自己写的数和实测不符**：'
              + '、'.join(f'`{k}` 差 {d:+,}' for k, d in bad.items())
              + '。修法：`python -X utf8 extract/check_index_budget.py --write`。')
        w()
        w('> **这是代理，不是本体**：`tiktoken` 是 OpenAI 的编码器，读这份文件的是 Claude，')
        w('> **两家的切分不同**。所以它的用法是「**能证伪『超了』，不能证明『离得远』**」——'
          '**那正是这条检查要的**（它只判超没超）。')
        w('> **为什么取两个编码器里大的**：宁可虚报，不许漏报。')
        w('> **量不出来时计入红**（不是「跳过」）：本机 `tiktoken` 是现装的，'
          '换台机器就没有——**那时这条会红，而它应该红**，')
        w('> 因为「不知道」和「没超」不是一回事。')
    w()
    w('**修法**：`python -X utf8 extract/check_index_budget.py --write` 会把页面里的')
    w('`<!-- index-token: … -->` 刷成实测值（**换位数时要跑两次才收敛**，')
    w('因为标记自己的字符也算在里面）。**超了才拆子索引**——')
    w('§7 明令「别把『拆了更整齐』当成『拆』的理由」。')
    w()
    # ---- 庚 · 页面里的「N 字节，M 行」对得上 raw 吗（2026-09-20 补）----
    # **又一处「声称 X 的地方正好落在唯一一类检查之外」。** 页面里凡写
    # `（TDC `98546.htm`，2,561 字节，134 行）。**整篇读完**`，
    # 就是对 raw 下了一条**可机械复核**的断言——**和引文、和边数是同一类**，
    # 而它此前**一类检查都没有**（引文有第七/十四类看着，边数没有）。
    #
    # **实测结果比预想的大**：22 条带行数的断言里 **14 条错**，
    # 而且 **13 条错法完全一样**（=`wc -l` + 1）——**那不是笔误，是一个抄错的口径**：
    # 本语料 9,398 篇**末行都带换行**，`wc -l` 就是行数，`+1` 恒错。
    # 另有 3 条字节数 = `st_size − 行数`（把 `\r\n` 当 `\n` 数出来的），
    # **正是「读文本还是读字节」这条口径在数字上留下的指纹**。
    w('### 庚 · 页面里的「N 字节，M 行」对得上 raw 吗')
    w()
    import check_doc_stats as cds
    rows_ds, missing_ds, dup_ds, covered_ds, scanned_ds = cds.scan(wiki=WIKI)
    c_ds = cds.classify(rows_ds)
    w(f'- 页里「N 字节…」形态 **{scanned_ds}** 条；**认到 TDC 号、真被比过** '
      f'**{covered_ds}** 条；**够不着、没比的 {scanned_ds - covered_ds} 条**。')
    w(f'- 比过的里面带行数的 **{len(c_ds["withn"])}** 条。')
    w(f'- 字节：✅ 对得上文件实际大小的 **{len(c_ds["b_ok"])}**；'
      f'**口径不同但页面写明了**的 **{len(c_ds["b_named"])}**（不算错）；'
      f'**值错的 {len(c_ds["b_bad"])}**。')
    w(f'- 行数：错 **{len(c_ds["bad_n"])} / {len(c_ds["withn"])}**'
      f'（真值取 `wc -l`）。')
    for r_ in c_ds['b_named']:
        k = [k for k, v in r_['var'].items() if k != 'st_size' and v == r_['b_claim']][0]
        w(f'  - ⚪ `{r_["page"]}`：{r_["b_claim"]:,} = **{k}**（页面写明了，**不算错**）')
    for r_ in c_ds['b_bad'][:12]:
        hit = [k for k, v in r_['var'].items() if v == r_['b_claim']]
        w(f'  - ❌ `{r_["page"]}` `{r_["tdc"]}.htm`：页称 {r_["b_claim"]:,}，'
          f'实际 {r_["b_true"]:,}'
          + (f'——**等于「{hit[0]}」而页面没写这个口径**' if hit else '——**哪个口径都对不上**'))
    for r_ in c_ds['bad_n'][:12]:
        w(f'  - ❌ `{r_["page"]}` `{r_["tdc"]}.htm`：页称 {r_["n_claim"]} 行，'
          f'`wc -l` = {r_["wc"]}')
    w()
    w('> **为什么这一条要单独有一节。** 它和「引文逐字」是同一类东西：'
      '**可机械复核的断言**。')
    w('> 2026-09-20 那批页里出过 **6 处「两篇互为出边」全错**，教训写成了'
      '「**能核而不核的，迟早是假的**」——')
    w('> 字节和行数和边数一样**就在那儿、一数就知道**，而它此前**一处检查都没有**。')
    w('> **两条已知限界**（不藏着）：① 只认「附近有 TDC 号」的写法，'
      f'**{scanned_ds - covered_ds} 条够不着**（文档写成纯路径的认不出）；')
    w('> ② 它**不改**页面——改法是 `python -X utf8 extract/fix_doc_stats.py --write`。')
    w()
    ok &= not (c_ds['b_bad'] or c_ds['bad_n'] or missing_ds)
    if not ok:
        w('**修法**：把 `index.md` 里的数字改成实际值，或者把标记补上／删掉多余的；'
          '`wiki-plan.csv` 的 status/缺行跑 `python -X utf8 extract/plan_sync.py --write`；'
          '「字节/行数」跑 `python -X utf8 extract/fix_doc_stats.py --write`。'
          '**不许反过来改判据去迁就页面**——这些数字的意义就是「和实际一致」。')
        w()
    return ok


def cat15_skeleton():
    """第十五类 · **散文有没有真的写**（骨架占位符残留）。

    **为什么补（2026-09-18）。** 第四批 71 页的做法是「脚本出骨架、LLM 填散文」：
    `objscaffold.py` 建出 frontmatter + 语法节 + 五个 `（待补）` 的空节。
    而**此前没有任何一类检查看得见那个 `（待补）`**——
    一页只要 frontmatter 齐、语法节对、五个小节标题都在，
    它在第一到第十四类里**全是绿的**，哪怕正文一个字都没有。

    这不是假想。这批页是**分给若干 agent 写的**，而 agent 中途断线是常态：
    本次实测 **9 次派发先后全断**（`UNKNOWN_CERTIFICATE_VERIFICATION_ERROR` /
    `ECONNRESET`），一次都没写成。**断在半路的一页，正好长成上面那个样子**——
    frontmatter 和语法节是脚本写的、必定齐，**缺的恰恰只有散文**。
    于是「agent 白跑了」和「页写好了」在全部现有检查里**输出同一个绿**。

    本仓库记过多次「一处声称 X 的地方，正好落在唯一一类检查之外」。
    这次换了面镜子：前几次是**判据在动而绿不变**、**说明与行为不符**，
    这次是**产出缺失在格式检查里是隐形的**——
    格式检查问的是「该有的结构在不在」，而占位符**自己就是那个结构**。

    **判据两条，都是硬红**（两个 marker 都来自 `plan_sync`，
    **不在本文件里重写一遍**，见那里 `is_skeleton()` 的注释）：
    1. 正文里还有 `（待补）` / `(待补)`；
    2. 骨架注释 `<!-- 骨架由 … -->` 还在（规格要求补完删掉）。

    ---

    **它查了哪些、没查哪些**（§13.1 第 ⑥′ 问）：

    - 查的是**每一页的正文**，范围 = 内容页减去 `_skip_prose()` 的目录页
      （`log.md` / `index.md` / `index-*.md` 是机器汇编的清单，没有散文可查）。
    - **判不出「写得对不对」。** 一页把五个 `（待补）` 换成五句废话，这里照样绿。
      **所以这条绿只说明「有人写过」，不说明「写对了」。**
    - **薄不薄只列出来，不参与判红。** 实测 `constraints/` 里有两节正文只有
      **76 / 99 字符**，而**内容是真的**（标题里就带着 `[[ ]]` 链接）——
      拿长度当判据会**误红**，而误红会把人训练成不看报告。
      所以「最薄的十页」印在下面，**由人扫一眼**，不设阈值。
    """
    import plan_sync as PS
    print('第十五类：骨架占位符残留…')
    w('## 第十五类 · 散文有没有真的写（**骨架占位符**）')
    w()
    skel, done, thin = [], [], []
    for p in [x for x in _content_pages() if not _skip_prose(x)]:
        fm, body = parse_page(p)
        label = f'{p.parent.name}/{p.stem}'
        if PS.is_skeleton(p):
            n = len(PS.RE_TODO.findall(body))
            why = []
            if n:
                why.append(f'`（待补）` × {n}')
            if PS.SKEL_COMMENT in body:
                why.append('骨架注释还在')
            skel.append((label, '＋'.join(why), len(body)))
            continue
        done.append(label)
        # 最薄的那一节（只看结构节，`## ` 级）。**用 `_section_body` 数出来的长度**，
        # 和上面 `is_skeleton` 的口径无关——这一栏是给人看的，不进判据。
        for name, ln in _section_lens(body):
            thin.append((ln, label, name))
    ok = not skel
    if not skel:
        w(f'✅ **{len(done)} 页的正文都写过了**（没有 `（待补）`，也没有残留的骨架注释）。')
    else:
        w(f'❌ **{len(skel)} 页的正文还是骨架**（`objscaffold.py` 出的 `（待补）` '
          '一个都没被换掉，或者骨架注释没删）：')
        w()
        w('| 页 | 还缺什么 | 正文字节 |')
        w('|---|---|---|')
        for label, why, n in sorted(skel):
            w(f'| `{label}` | {why} | {n:,} |')
        w()
        w(f'（另 **{len(done)} 页**已写完。）')
    w()
    thin.sort()
    w('> **最薄的十节**（只列，不判——理由见本类开头）：')
    w('>')
    w('> | 字符 | 页 | 节 |')
    w('> |---|---|---|')
    for ln, label, name in thin[:10]:
        w(f'> | {ln} | `{label}` | `{name}` |')
    w()
    w('> **为什么这一条不能只看文件在不在**：`wiki-plan.csv` 的 `status` '
      '曾经只有 `todo` / `done` 两个值，判据是「文件在不在」——'
      '**于是 68 页骨架也记成 `done`**。现在它是三个值'
      '（`todo` / `skeleton` / `done`），判据和本类**同一处实现**'
      '（`plan_sync.is_skeleton()`），第十四类丁 也调它。')
    w()
    return ok


def _section_lens(body):
    """每一节 `## X` 的正文长度（字符）。节名原样返回。"""
    hs = [(m.start(), m.end(), m.group(1).strip())
          for m in re.finditer(r'^##\s+(.+?)\s*$', body, re.M)]
    out = []
    for i, (s, e, name) in enumerate(hs):
        stop = hs[i + 1][0] if i + 1 < len(hs) else len(body)
        out.append((name, len(body[e:stop].strip())))
    return out


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    docs = [json.loads(l) for l in
            (OUTDIR / 'docs.jsonl').open(encoding='utf-8')]
    docs_by_rel = {d['rel']: d for d in docs}
    docs_by_rel_cache.extend(docs_by_rel)
    catnos = set()
    for d in docs:
        stem = d['rel'].split('/')[-1][:-3]
        m = re.match(r'(\d+(?:\.\d+)*)_', stem)
        if m:
            s = m.group(1).split('.')
            for i in range(1, len(s) + 1):
                catnos.add('.'.join(s[:i]))
    # **必须用去重表**。第一版读的是 `hubs.csv`（未去重），于是第六类的候选报 153，
    # 而 `index.md` 用去重表报 125 —— 同一个口径两个数，因为**去重是后来发现的，
    # 第六类没跟着改**。现在两边同源：`hubs-dedup.csv`。
    hubs = list(csv.DictReader((OUTDIR / 'hubs-dedup.csv').open(encoding='utf-8')))

    # **标题里的范围曾经是假的**（2026-09-18 改）。原文写「对象：`wiki/stages/*.md`，九页」——
    # 那是本文件刚出生时的范围。后来第七类扩到了 `wiki/` 下全部页面、第六类扩到了
    # 38 个 stage 之外的页、第十三批又加了 143 个版本页，**标题一句都没跟着改**。
    # 于是报告自称「九页」，而它实际印的是 **200 多页**的结果——
    # **同一个病：说明与行为不符**（第十一次是检查的自我说明，这次是报告的抬头）。
    # 改法不是把「九页」换成新数字（数字还会变），而是**让标题只说它管什么类型的检查**，
    # 范围由**每类自己的开头**declare —— 那几处是逐类写的，改起来跟着代码走。
    w('# 页面格式与出处对账报告')
    w()
    w('对象：**`wiki/` 下各类型页面**（范围与跳过项由**每一类自己的开头**写明）。'
      '依据：`schema.md` §2 / §5 / §6 / §9 / §11。')
    w()
    w('> **本文件覆盖十五类检查**，其中 `stages/*.md` 只是**第一类**的对象。'
      '标题里原先写的「九页」是本文件出生时的范围，早就不是了。')
    w('> **退出码是有意义的**：参与总闸的那几类里只要有一类红，进程就非 0 退出'
      '（第八、十类标着「— 记录」，不参与）。**这条 2026-09-18 才补上**——'
      '在此之前退出码**永远是 0**，而它看起来像「表是绿的」。')
    w()

    ok1, pages = cat1_files()
    ok2 = cat2_frontmatter(pages)
    ok3 = cat3_sources(pages, docs_by_rel)
    ok4 = cat4_catno(pages, catnos)
    ok5 = cat5_chain(pages)
    ok6 = cat6_coverage(pages, hubs, docs_by_rel)
    ok7 = cat7_quotes(pages)
    ok8 = cat8_reachable(pages)
    ok9 = cat9_naming(pages)
    ok10 = cat10_dedup(pages)
    ok11 = cat11_layer(pages)
    ok12 = cat12_syntax_fresh()
    ok13 = cat13_version_fresh()
    ok14 = cat14_index_claims()
    ok15 = cat15_skeleton()
    w('## 汇总')
    w()
    w('| 检验 | 结果 |')
    w('|---|---|')
    for k, v in [('第一类 九页与十节齐备', ok1), ('第二类 frontmatter 必填', ok2),
                 ('第三类 sources 可追溯', ok3), ('第四类 分类号存在', ok4),
                 ('第五类 下一步链', ok5), ('第六类 候选归属覆盖', ok6),
                 ('第七类 引文逐字', ok7), ('第八类 链接目标可达', ok8),
                 ('第九类 命名合规', ok9), ('第十类 重复投放', ok10),
                 ('第十一类 层断言一致性', ok11),
                 ('第十二类 语法节新鲜度', ok12),
                 ('第十三类 版本页新鲜度', ok13),
                 ('第十四类 自我声明', ok14),
                 ('第十五类 散文已写（无骨架占位符）', ok15)]:
        label = ('— 记录' if k.startswith(('第八类', '第十类'))
                 else ('✅ 通过' if v else '❌ 未通过'))
        w(f'| {k} | {label} |')
    w()
    # 报告里不许出现**没有归宿的红**。第六类的 ❌ 是**待决事项**，不是页面缺陷——
    # 不写这一行，下一个读报告的人（或下一个我）会以为九页有错。
    #
    # **但这段必须跟着第六类的实际结果走。** 2026-09-18 那批 object 页建完之后
    # 第六类转绿，这段却还印着「**第六类为什么是 ❌**：0 个……」——
    # **0 个未归属配一个 ❌ 的标题，是报告在说假话**，而且是往坏里说。
    # 和第十二类那行硬编码「12 个已建页」是同一个病：**结论写死，判据在动。**
    if not ok6:
        # **2026-09-20 第三次修这个坑。** 上一版这里写 `STATS['unassigned']`
        # （=「九页里一个字都没提的」），**而 ❌ 的判据 2026-09-20 已经改成了 `no_page`**
        # （=「还没有页的」，`in_src >= 20` 那一档）。于是报表出现
        # 「表里写着 ❌ **还没有页的：1**，紧接着一句「**0 个**……一个字都没提」」——
        # **一个 0 配一个 ❌，是报告在说假话**，而且正是本项目反复栽的那个形状：
        # **一处声称 X 的地方，正好落在唯一一类检查之外**（这次落在「结论句和判据不同源」上）。
        # 所以现在**从判据自己的那个变量取数**，不再从旁边的统计里借。
        w(f'**第六类为什么是 ❌**：`in_src >= 20` 的候选里，'
          f'**{STATS.get("no_page", "?")} 个还没有页**。')
        if STATS.get('no_page_names'):
            w('')
            w('| in_src | 对象 | 语料里的那一篇 |')
            w('|---|---|---|')
            for nm, src_ in STATS['no_page_names']:
                w(f'| — | {nm} | `{src_}` |')
        w('**「还没有页」和「没提到」是两件事**，判据要的是前者'
          '（`unassigned` 那一档现在是 '
          f'{STATS.get("unassigned", "?")}，**它空着才是对的**）。')
        w('这不是页面写错了，是**它们不属于任何一段流程**（硬件规格 / 存储专用测试 / 程序管理）。')
        w('**处置已定（2026-09-18）：为它们建 stage 之外的 `object` 页**，'
          '清单 `extract/unowned.csv`。❌ 会一直亮到那些页建出来为止。')
        w()
    else:
        # **数量现数，不写死。** 这是同一课第三次了（前面两次：cat12 的
        # 「12 个已建页」、这段自己的 ❌）。**报告里的每一个数字都得有出处。**
        #
        # **而且得数对**（2026-09-18 第二次修）：原来数的是 `_other_pages()`，
        # 142 个版本页一建出来，这句话就变成「建了 **171 个**页把候选认领了」——
        # **数字涨了，可认领候选的其实还是那 28 页**。
        # 数变大了不是因为活儿干了更多，是因为**我把机械汇编页也算进了分母**。
        # 改成只数「讲对象」的页，并把版本页单独说一句。
        n_real = len(page_of_type(real=True))
        n_mech = len(page_of_type(real=False))
        w(f'**第六类的 ❌ 是怎么灭的（2026-09-18）**：建了 **{n_real} 个 `stage` 之外的页**，'
          '由各页 frontmatter 的 `sources:` 把候选逐个认领。')
        w(f'（另有 **{n_mech} 个文件在 `wiki/versions/`**——142 个版本页 + 一个目录页。'
          '它们的 `sources:` 意思是「这篇文档里有一条这个版本的变更记录」，'
          '**不是「本页讲的是它」**，所以**不参与第六类**，见 `MECH_TYPES`。）')
        w('**这一条不用再盯了**——但注意它**只证明「每个高入度候选都有归宿」，'
          '不证明「当归宿的那页写得对」**。')
        w()
    w('**十五类全绿只证明：格式齐、引的文档真的存在、引的句子真的在原文里、候选没漏、'
      '链接不悬空、命名统一、同一对象没被两页标成不同层、脚本写的那一节和脚本的产出是同一个东西、'
      '版本页的条目逐字回得到 raw、`index.md` 每节列出的页和目录里的文件互相都对得上、'
      '**每一页的散文都真的写过了（不是 `（待补）` 骨架）**。**')
    w('**不证明内容对。**「文档事实 / 推断 / 建议」分得对不对、'
      '**层判得对不对**、边界（testflow vs run、run vs results）守得对不对——')
    w('这些机器判不了，**必须人读**。读之前别把 stage 页当可信输入。')
    w()
    w('> **注意区分**：第十一类只判「两页说法一不一致」，**不判「哪层对」**。')
    w('> 「对象属于哪层」试过用文档章节推，4 条全是误报——章节结构里没有这个信息。')
    w('> 所以「层判得对」仍在「必须人读」那一栏里。')
    w()
    w('> 第八、九、十类报的多是**建页 backlog 与结构事实**，不是页面错误：')
    w('> 第八类的悬空目标是「脊椎已经伸手去要的页」；')
    w('> 第九类是「同一对象被写成多个 slug」——建页前不收掉就会建出重复页（§13 那条）；')
    w('> 第十类是语料自身的重复投放，影响一切计数。')
    w()

    with open(OUTDIR / 'stage-report.md', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(R) + '\n')

    # **工作单由产出报告的那次运行自己写。**
    #
    # 为什么（2026-09-18）：`unowned.csv` 曾经是「记得去跑 `unowned.py`」才更新的，
    # 于是它**过期了 26 行**——里面每个对象都已经有页了，而第六类早就转绿。
    # **一份没人认领的工作单，会一直绿着骗人**（`dangling.csv` 已经栽过一次，同一个病）。
    #
    # 所以放到这里：报告刚写完，**同一个进程、紧接着**，把它摊成清单。
    # 「忘了跑」这个状态从今天起不存在了。
    #
    # **清单由这次运行写，但算它的代码是另一份**：`unowned.refresh()` 是独立实现，
    # 自己从 `hubs-dedup.csv` + `stage-map.csv` 重算，再和上面这份报告里的数**必须相等**，
    # 不等就抛 `SystemExit`。两件事都要——前者防过期，后者防「报告算错了清单跟着错」。
    import unowned
    n_un, _ = unowned.refresh(quiet=True)
    print(f'✅ 工作单已随报告重算：extract/unowned.csv，{n_un} 个未归属'
          f'（**和上面报告里那个数相等，否则这次运行会直接失败**）')

    # **候选表也一样**（2026-09-18 加）。理由是同一条：`constraint-candidates.csv`
    # 的 `disposition` / `n_doc` / `前置词` 三列是**派生的**，
    # 而 `constraints.py` 只写它那五个原料列——**上游一重跑，归宿列就静默消失**，
    # 表看着还在、还完整，**只是又变回一张没归宿的表**。这比过期更阴：
    # 过期的表数字是旧的，这个表是**少了三列而没人看得出来**。
    #
    # 所以每次出报告都重算一遍。第 2 档（版本事实漏网）**非 0 就报红**——
    # 那一档是「上游改了判据而这里没跟上」的信号，不是语料问题。
    import constraint_dispose
    c_buckets, _ = constraint_dispose.dispose()
    # **三个档都要印，包括 0。** `Counter` 只记命中过的键，直接遍历它会把
    # 「第 2 档是 0」和「第 2 档不存在」印成同一个样子——而这一档的**全部意义就是它是 0**。
    print(f'✅ 候选表归宿已随报告重算：extract/constraint-candidates.csv，'
          f'{sum(c_buckets.values())} 行（'
          + '、'.join(f'{k} {c_buckets.get(k, 0)}'
                      for k in ('1-重复投放', '2-版本事实(应恒为0)', '3-非约束（补集）'))
          + '）')
    if c_buckets.get('2-版本事实(应恒为0)', 0):
        raise SystemExit(
            f'❌ 候选表第 2 档有 {c_buckets["2-版本事实(应恒为0)"]} 行：'
            f'`constraints.py` 的 `NOT_CONSTRAINT` 和 `constraint_dispose` 同源，'
            f'出现非 0 说明上游判据改了而下游没跟上。**这不是语料问题，是代码问题。**')

    # ---- 退出码的总闸（2026-09-18 补）----
    #
    # **为什么补**：此前 `main()` **从来不返回退出码**，也**从不把 `ok1…ok13` 合起来**——
    # 它只把结论打进报告。唯一会让进程非 0 退出的，是第十二/十三类**内部**那几个
    # `raise SystemExit`。于是出现这个形状：
    #
    #     汇总表里印着 **❌ 未通过**，而 `echo $?` 是 **0**。
    #
    # **而我自己正是这么用它的**：前几批汇报里写「十三类全绿，EXIT=0」，
    # 把 `EXIT=0` 当成「表是绿的」的证据。**它不是。** 它只说明「没有断言炸掉」。
    # 两个信号看起来同向，其实强弱差一大截——**这就是本项目反复记的那个病**：
    # 一个信号覆盖的范围比它看起来小，而它一直是绿的。
    #
    # **负测试**（改之前先证旧行为，不然改了也不知道改对没有）：
    # 在临时副本里删掉 `objects/tp360.md` 的 `tags:` 整行 → 汇总表出现
    # 「第二类 ❌ 未通过」，**而退出码仍是 0**。改完之后同一注入必须非 0。
    #
    # **口径**：第八、十类是「— 记录」（语料事实与建页 backlog，不是页面缺陷），
    # **不参与总闸**——它们返回的也一直是 `True`，写在这里是为了把意图写明。
    hard = [('第一类', ok1), ('第二类', ok2), ('第三类', ok3), ('第四类', ok4),
            ('第五类', ok5), ('第六类', ok6), ('第七类', ok7),
            ('第九类', ok9), ('第十一类', ok11),
            ('第十二类', ok12), ('第十三类', ok13), ('第十四类', ok14),
            ('第十五类', ok15)]
    bad = [k for k, v in hard if not v]
    print(f'{"✅ 参与总闸的 " + str(len(hard)) + " 类全绿" if not bad else "❌ 红的：" + "、".join(bad)}'
          f'（第八、十类是「记录」，不参与）')
    if bad:
        raise SystemExit(f'❌ {"、".join(bad)} 未通过——详见 extract/stage-report.md')


if __name__ == '__main__':
    main()
