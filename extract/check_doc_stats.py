# -*- coding: utf-8 -*-
"""**待办：页面里的「N 字节，M 行」是「关于文档的可复核断言」，但从来没有一类检查看它。**

**它为什么是这类东西。** 页面里凡写

    （TDC `98546.htm`，2,561 字节，134 行）。**整篇读完**

就是对 raw 文档下了一条**可机械复核**的断言——**和引文、和边数是同一类**
（引文有第九/十四类看着，边数 2026-09-20 记过教训「能核而不核的，迟早是假的」）。
而这一条**一处检查都没有**：谁也数过 `2,561` 对不对，更没人数过 `134 行` 对不对。
又一次「**一处声称 X 的地方，正好落在唯一一类检查之外**」。

**这个脚本干什么。** 从 `wiki/**/*.md` 里把所有这种断言扫出来，
按 `source_topic` 找回 raw 那篇，**逐个比字节与行数**。

**行数按哪个口径**——这是本脚本要先量、再定的事（不许先定再量）：

| 口径 | 定义 |
|---|---|
| `wc -l` | 换行符个数 |
| `splitlines()` | 实际行数（末行无换行时 = `wc -l` + 1） |
| `+1` | 语料里曾经用过的写法：`wc -l` + 1 |

**实测结论（本脚本跑出来的，不是猜的）**：本语料那 9,398 篇 **末行都带换行**
（`wc -l == splitlines()`，抽查全部相等），**所以 `+1` 那个口径在这批文件上永远是错的**。
**行数的真值就是 `wc -l`。**

用：`python -X utf8 extract/check_doc_stats.py`
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(r'F:\master-dev\understand-anything-wiki')
WIKI = BASE / 'wiki'
CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')

# （TDC `98546.htm`，2,561 字节，134 行） / （`67572.htm`，2,971 字节，78 行）
#                              ↓ 行数可有可无——**只写字节的也是同一种断言**，
#                                原先只认「字节，N 行」，把 159 条里的大多数放过去了。
CLAIM = re.compile(
    r'`?([0-9]{4,6}(?:_[0-9]+)?)\.htm`?[^0-9]{0,60}?'
    r'(?:'
      r'([0-9][0-9,]*)\s*字节(?:[，,]\s*([0-9][0-9,]*)\s*行)?'   # 「N 字节，M 行」/「N 字节」
      r'|'
      r'([0-9][0-9,]*)\s*行'                                      # **只写「M 行」的**
      # ⚠️ 这一支**不要求前面有逗号**：骨架 `for-each-site-end.md` 写的是
      # 「`29350.htm`（TDC `29350.htm`）…全文 **41 行**」——**数前面是 `*` 不是逗号**，
      # 要求逗号就把它漏了（第二次放宽时又漏了一次）。**上一支的逗号可以没有，
      # 因为 `.htm` 与数字之间那段 `[^0-9]{0,60}?` 本来就能吞掉分隔符。**
    r')')
# ⚠️ **2026-09-20 第二次放宽，理由是一次真实的漏检。**
# 骨架 `for-each-site-end.md` 的「出处」写着 `29350.htm`「全文 **41 行**」，
# 真值是 **40**（`wc -l`）。而原来的正则**只认带「字节」的**——
# **那句话里一个「字节」都没有，于是它连解析都不解析，检查全绿。**
# 「一处声称 X 的地方，正好落在唯一一类检查之外」——**这一条自己犯了自己要防的病**
# （§13.1 第十七/十九次：先有「一类断言没有检查」，再有「检查比自称的窄」）。
# 现在两个分支并列：**带字节的**和**只写行数的**都收。
# **要求至少命中一个数**，不然 `.htm` 后面没东西也会被当一条断言收进来（那会全是假红）。
# 「（23,466 字节，961 行）」——**不带 TDC 号、文档写成路径的**，本次语料只有几条。
# 本脚本**不解析它**（要顺着上文找路径，正则做不可靠），**但要把条数报出来**，
# 免得「绿」是拿覆盖不到的样本换来的（§5 第五类：任何跳过都要出现在报告里）。
# 覆盖面用：**不管有没有 TDC 号，先把页里所有「数字 + 字节/行」形态数出来**。
# 两个分支对应 `CLAIM` 的两个分支——**两边必须同步**，
# 否则分母比分子小，「够不着几条」这句话就是错的（第十三次：印出来的数不支撑旁边那句话）。
CLAIM_LOOSE = re.compile(
    r'(?:[0-9][0-9,]*\s*字节(?:[，,]\s*[0-9][0-9,]*\s*行)?'
    r'|[，,]\s*[0-9][0-9,]*\s*行)')

_CORPUS = None


def corpus():
    """→ `{source_topic 去后缀: rel}`。**从 `docs.jsonl` 读，不重扫语料**。"""
    global _CORPUS
    if _CORPUS is None:
        _CORPUS = {}
        for line in (BASE / 'extract' / 'docs.jsonl').open(encoding='utf-8'):
            d = json.loads(line)
            st = str(((d.get('frontmatter') or {}).get('source_topic')) or '')
            if st.endswith('.htm'):
                _CORPUS.setdefault(st[:-4], []).append(d['rel'])
    return _CORPUS


HTM = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\raw')


def variants(rel):
    """→ `{口径标签: 值}`——**全部由实测算出**，不带「差不多像」的候选。

    每多一个口径，就多一种「页面的数其实对、只是量的不是同一个东西」的可能。
    **所以候选要穷举到能被证明的程度，一个不许凭印象加**：

    | 标签 | 怎么算的 | 什么时候是对的 |
    |---|---|---|
    | `st_size` | 文件字节数 | **本 wiki 的常态口径** |
    | `st_size − 行数` | 把 `\\r\\n` 当 `\\n` 数出来的 | 页面写「字符数」时；写「字节」时是**错的** |
    | `剥掉 frontmatter 后` | 去掉首尾 `---` 块再数 | 页面写明「剥掉 frontmatter」时（只有这种标注才算） |
    """
    st = stats(rel)
    if st is None:
        return None, None
    b, nl, sl = st
    v = {'st_size': b, 'st_size − 行数（CR 归一）': b - nl}
    p = Path(rel) if Path(rel).is_absolute() else CORPUS / rel
    if p.suffix == '.md':
        # **必须走字节**：`read_text()` 会把 `\r\n` 折成 `\n`，
        # 于是「剥 frontmatter 后」这一栏会跟着少掉「行数」个字节——
        # **那正是这一栏要抓的那个口径错，用错读法就自己犯一遍**。
        t = p.read_bytes().decode('utf-8', errors='replace')
        if t.startswith('---'):
            i = t.find('\n---', 3)
            if i > 0:
                v['剥掉 frontmatter 后'] = len(t[i + 4:].encode('utf-8'))
    return v, (b, nl, sl)


def stats(rel):
    """→ `(字节, wc-l, splitlines)`；文件不在返回 `None`。

    **`rel` 也可以是一个 `.htm` 的绝对路径**——页里有一类是量**上游 HTML**
    的（`raw/130563.htm` 10,418 字节），**那和量 md 是两回事**，
    所以宁可按原样去读那个 `.htm`，也不要随便换一个文件来对。
    """
    p = Path(rel) if Path(rel).is_absolute() else CORPUS / rel
    if not p.exists():
        return None
    raw = p.read_bytes()
    text = raw.decode('utf-8', errors='replace')
    return (len(raw), text.count('\n'), len(text.splitlines()))


def scan(wiki=None):
    """→ `(rows, missing, dup, covered, scanned)`。**只算不打印**。

    `verify_stages.py` 要拿这个结果进它自己的汇总表，所以扫描和打印必须分开——
    否则只能靠重定向 stdout 去接，**那种接法迟早接错**（第十四类那几节都栽过这个）。
    """
    idx = corpus()
    rows, missing, dup = [], [], []
    covered = scanned = 0
    # **相对路径要按传进来的那棵树算，不能按写死的 `BASE`。**
    # `_negtest_checks.py` 会把 `WIKI` 指到临时目录去跑——
    # 那时 `page.relative_to(BASE)` 直接抛 `ValueError`，**负测试一跑就崩**。
    # 这正是 `check_index_budget.main(path=…)` 那个口子的同一条教训：
    # **模块里写死的常量，在反向测试里就是错的常量。**
    root = (wiki or WIKI).parent
    for page in sorted((wiki or WIKI).rglob('*.md')):
        if page.name in ('log.md', 'index.md'):
            continue
        text = page.read_text(encoding='utf-8')
        covered += len(CLAIM.findall(text))
        scanned += len(CLAIM_LOOSE.findall(text))
        for m in CLAIM.finditer(text):
            tdc = m.group(1)
            b = int(m.group(2).replace(',', '')) if m.group(2) else None
            nl_raw = m.group(3) or m.group(4)          # 带字节的走 (3)，只写行数的走 (4)
            # ★ **「第 N 行」是「指到某一行」，不是「一共 N 行」。**
            # 实测两条：`setup-level-set-0` 写「上游核过 `121827.htm` 第 228 行」（文件 284 行）、
            # `sharing-configuration` 写「`131630.htm` 第 28 行」（文件 73 行）——
            # 两条都是**行号引用**，而正则把它们当成了行数声明，报成 `n-56` / `n-45`。
            # **判据要把「第」认出来**，否则每写一次行号就多一条假红。
            if nl_raw and m.group(4) and text[max(0, m.start(4) - 3):m.start(4)].count('第'):
                nl_raw = None
            n = int(nl_raw.replace(',', '')) if nl_raw else None
            # **同一个号，md 和上游 `.htm` 是两篇东西。**
            # 页面写「其上游 `...\tdc-html\raw\130563.htm`（10,418 字节）」时量的是 HTML，
            # 而 `130563` 在语料里**也有一篇 md**——**不按路径分辨就会把它判成错**。
            # （实测：7 条「上游」断言全对，是检查器自己配错了对。）
            pre = text[max(0, m.start() - 80):m.start()]
            # **「上游」也要算。** 判据原先只认路径里出现 `raw\` / `raw/`，
            # 而页面更常写的是中文的「回上游核过 `131630.htm`（12,861 字节）」——
            # 那种写法下检查器**把它配成了 md**，于是 4 条本来正确的
            # 「上游 htm 尺寸」全被报成 ❌（实测就是这 4 条）。
            # **一处声称 X 的地方落在判据之外，报出来的就是假红。**
            upstream = ('raw\\' in pre or 'raw/' in pre or '上游' in pre)
            rels = idx.get(tdc)
            if len(rels or ()) > 1 and not upstream:
                dup.append((page, tdc, len(rels)))
            if upstream:
                h = HTM / f'{tdc}.htm'
                rel = str(h) if h.exists() else None
            elif rels:
                rel = rels[0]
            else:
                h = HTM / f'{tdc}.htm'
                rel = str(h) if h.exists() else None
            var, st = variants(rel) if rel else (None, None)
            if var is None:
                missing.append((page, tdc, b, n))
                continue
            b2, nl, sl = st
            named = {k: (k.split('（')[0].strip() in m.group(0) or
                         any(w in m.group(0) for w in ('frontmatter',) if 'frontmatter' in k))
                     for k in var}
            rows.append({'page': (page.relative_to(root).as_posix()
                                  if page.is_relative_to(root) else page.as_posix()),
                         'tdc': tdc,
                         'b_claim': b, 'b_true': b2, 'var': var, 'named': named,
                         'upstream': upstream, 'pre': ' '.join(pre.split())[-60:],
                         # ★ **`rel` 原先没放进行字典**，而下面两处 ❌ 明细要印它
                         # （「← 对的是 …」）——于是**一旦真有不符的，脚本就
                         # `KeyError: 'rel'` 崩在打印那一步**：
                         # 报不出来 ≠ 没问题，而报告里看不出区别。
                         # **改页面的替换串必须拿 `hit_raw`，别拿 `hit`**（上面那句注释）。
                         'rel': rel,
                         'n_claim': n, 'wc': nl, 'sl': sl,
                         # **两份**：`hit` 是给人看的（空白归一，日志里一行放得下），
                         # `hit_raw` 是**原样的**——改页面必须拿这一份去替换。
                         # 拿归一过的那份去 `replace` 会找不到（实测栽过一次：
                         # `stpm-control-file` 那句话中间有换行，归一后对不上原文）。
                         'hit': ' '.join(m.group(0).split()),
                         'hit_raw': m.group(0)})
    return rows, missing, dup, covered, scanned


def classify(rows):
    """→ `(b_ok, b_named, b_bad, n_bad, n_all)`。**分类逻辑只写一处**，
    打印和 `verify_stages.py` 都读它——两处各写一遍，迟早有一处不一样。"""
    # **字节断言分三档，不是「对/错」两档。**
    # 页面写「字节」而量的是别的口径 → **数对不上，但值本身是真的**；
    # 只有**哪个口径都对不上**才是值错。**分不清这两件事，就会去改对的东西。**
    def cls(r):
        # **只写「N 行」的那一类不参与字节分档**（它没有字节可判）。
        # 不排除的话它会被判成 `wrong`——**一个不存在的错**，而修的时候无从下手。
        if r['b_claim'] is None:
            return 'nobytes'
        if r['b_claim'] == r['var']['st_size']:
            return 'ok'
        for k, v in r['var'].items():
            if k != 'st_size' and r['b_claim'] == v:
                return 'named' if r['named'].get(k) else 'unnamed'
        return 'wrong'

    b_ok = [r for r in rows if cls(r) == 'ok']
    b_other = [r for r in rows if cls(r) == 'ok' or cls(r) == 'named' or cls(r) == 'unnamed' or cls(r) == 'wrong']
    b_other = [r for r in b_other if cls(r) != 'ok']
    b_named = [r for r in b_other if cls(r) == 'named']
    b_bad = [r for r in b_other if cls(r) != 'named']
    b_none = [r for r in rows if cls(r) == 'nobytes']
    bad_b = b_bad
    withn = [r for r in rows if r['n_claim'] is not None]
    bad_n = [r for r in withn if r['n_claim'] != r['wc']]
    n_plus1 = [r for r in withn if r['n_claim'] == r['wc'] + 1]
    endnl = sum(1 for r in rows if r['wc'] == r['sl'])
    return {'b_ok': b_ok, 'b_named': b_named, 'b_bad': b_bad, 'bad_n': bad_n,
            'withn': withn, 'n_plus1': n_plus1, 'endnl': endnl,
            'b_none': b_none, 'rows': rows}


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    rows, missing, dup, covered, scanned = scan()
    c = classify(rows)
    (b_ok, b_named, b_bad, bad_n, withn,
     n_plus1, endnl) = (c['b_ok'], c['b_named'], c['b_bad'], c['bad_n'],
                        c['withn'], c['n_plus1'], c['endnl'])

    print('### 覆盖面（先说清这一次绿的是哪一部分）')
    print(f'- 页里「N 字节…」形态共 **{scanned}** 条；'
          f'能认到 TDC 号、因而**真被比过**的 **{covered}** 条；'
          f'**够不着、没比的 {scanned - covered} 条**。')
    print(f'- 解得出 raw 的 **{len(rows)}** 条里，带行数的 **{len(withn)}** 条、只带字节的 {len(rows) - len(withn)} 条。')
    print(f'- 其中 `wc -l == splitlines()` 的：**{endnl} / {len(rows)}**'
          f'（末行带换行 → 「`wc -l` + 1」那个口径**在这批文件上恒错**）。')
    print()

    print(f'### 字节：✅ 对得上 st_size **{len(b_ok)}** / 口径不同但**页面标注了** '
          f'**{len(b_named)}** / 其余 **{len(b_bad)}**')
    for r in b_named:
        k = [k for k, v in r['var'].items() if k != 'st_size' and v == r['b_claim']][0]
        print(f'  ⚪ {r["page"]}  `{r["tdc"]}.htm`：页称 {r["b_claim"]:,} = **{k}**'
              f'（标注了，不算错）')
    for r in b_bad:
        hit = [k for k, v in r['var'].items() if v == r['b_claim']]
        print(f'  ❌ {r["page"]}  `{r["tdc"]}.htm`：页称 {r["b_claim"]:,}，'
              f'st_size = {r["b_true"]:,}'
              + (f'——**等于「{hit[0]}」而页面没写这个口径**' if hit else '——**哪个口径都对不上**'))
        # **把命中的原串摆出来**——不然分不清「页面写错」和「检查器配错对」。
        # 本项目已经栽过一次：断言没数过就写。检查器同理，**不许只报结论**。
        print(f'     ↳ 上文：…{r["pre"]}  命中：`{r["hit"]}`  ← 对的是 {r["rel"]}')
    print()

    print(f'### 行数不符（真值取 `wc -l`）：**{len(bad_n)} / {len(withn)}**')
    for r in bad_n:
        d = r['n_claim'] - r['wc']
        tag = '**n+1**' if d == 1 else f'**n{d:+d}**'
        print(f'  ❌ {r["page"]}  `{r["tdc"]}.htm`：页称 {r["n_claim"]}，'
              f'wc-l = {r["wc"]}（{tag}）')
        # **行数也要摆证据**——不然分不清「页面写错」和「检查器配错对」。
        # 实测：放宽到「不要求逗号」之后就有配错的（`pin-configuration-tool` 那条 n-14）。
        print(f'     ↳ 上文：…{r["pre"]}  命中：`{r["hit"]}`  ← 对的是 {r["rel"]}')
    print()
    print(f'> 其中写成「`wc -l` + 1」的有 **{len(n_plus1)}** 条——'
          f'**如果这一批占多数，那它不是笔误，是一个抄错的口径**。')

    if missing:
        print()
        print(f'### ⚠️ 找不到 raw 的断言：**{len(missing)}**（不许静默丢）')
        for page, tdc, b, n in missing:
            print(f'  - {page.relative_to(BASE).as_posix()}  `{tdc}.htm` {b:,} 字节 {n} 行')
    if dup:
        print()
        print(f'### ⚠️ 一个 `source_topic` 对多篇的：**{len(dup)}**')
        for page, tdc, k in dup:
            print(f'  - {page.relative_to(BASE).as_posix()}  `{tdc}.htm` → {k} 篇')

    # 红 = 值错 / 行数错 / 认不出 raw。**「口径不同但页面写明了」不算红**——
    # 那是页面把话说清楚了，不是它写错了（§10 的「两种说法并列，各自附出处」）。
    return 0 if not (b_bad or bad_n or missing) else 1


if __name__ == '__main__':
    raise SystemExit(main())
