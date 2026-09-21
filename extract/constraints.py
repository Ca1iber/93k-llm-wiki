# -*- coding: utf-8 -*-
"""找**跨文档复现的约束** —— `constraint` 页的候选清单。

**为什么要有这个脚本（2026-09-18，它推翻了一次计划）。**

计划里写的是「constraint 页：727 段 → 30–60 页」。727 这个数是从
`sections.jsonl` 的 `group='constraint'` 数出来的，看着很硬。真去读才发现它由两块构成，
**两块都不长页**：

- `Before you begin` **558 段**，散布在 **558 篇不同的文档**里，开头句有 **444 种写法**，
  只有 5 种出现在 ≥4 篇文档里。**它们是一篇文档一条的一次性前置条件**
  （「确保 TCCT 已启动」「确保已装载 primary setup」），不是跨文档的规矩。
  按它们建页 = 444 页一句话 —— 正是 §13「第七次」记的那个病：
  **把语料摊平当成品，页数很好看，没有一页在回答「我该注意什么」。**
- `Dependency`/`Predependencies`/… **169 段**，散在 **160 篇文档**里，
  ≥2 段的文档只有 **9 篇**。它们是**某一条命令自己的前置条件**
  （「APDV 必须在 TSTL 选好 label 之后」）——归宿是**那条命令自己的页**，
  不是一张独立的 constraint 页。

**那真正的跨文档约束在哪？在参数/成员函数的正文里，反复出现，只是没人给它贴标签。**
这个脚本就是把它们捞出来：

- 全文扫，只取含约束标记词（`only supported` / `must` / `not supported` / `is required` …）的句子，
  **并剔掉版本事实**（`NOT_CONSTRAINT`，它们已有归宿：142 个版本页）；
- 归一化（剥链接、压空白、去括号、转小写）后**按词集相似度聚类**——
  因为同一句规矩在不同文档里写法不同（`with a comma` vs `by a comma`），
  不聚类就会把 87 篇的规矩拆成 87 个「1 篇」的噪音；
- **按「出现在多少篇不同文档里」排序**：一篇文档里的句子，再多也只是它自己的事；
  **多篇文档不约而同写同一句，那才是这张 wiki 该有的 constraint 页。**

这个脚本**只出候选和证据，不建页**（§4 铁律：脚本产出机械索引，LLM 产出页面）。
判定「哪几条够格立页、怎么合并、叫什么 slug」是人/LLM 的活，依据就是它出的报告。

## ⚠️ 这张表是**取材清单**，不是**待办清单**（2026-09-18 补）

`MARK` 是**故意放宽**的（见它上面那段），`MIN_DOCS = 4` 也只管「多少篇文档复现」。
两个宽口径叠起来的代价，此前**从没写下来过**：253 行里绝大部分**不是**
`§2.4` 意义上的约束（`<主体>-requires-<前置>`），而是——

- **参数语法样板**：`the names must be separated with a comma` /
  `must be enclosed in square brackets` / `must be a multiple of 8192`；
- **单对象属性**：`This member function is supported only for the DC Scale XPS256 card` /
  `The break waveform must not contain data dependent actions`；
- **重复投放的副本**（§11.2 ④）：同一篇文档换了分类树再放一遍，
  `docs` 数因此虚高（**折掉投放后 253 行里有 27 行的「独立文档数」是 1**）。

所以「253 行只建了 6 页」**不是欠着 247 页**。这张表的完成判据是
**每一行都说得出它为什么在表里、以及它为什么没变成页**，
而不是**每一行都变成一页**；后者等于按目录树摊平（§3 明令禁止）。

**反过来也成立，而且是更要紧的一半**：`docs ≥ 4` 这个门槛**会漏掉真约束**。
`wiki/constraints/pin-config-locked-during-test.md` 的 `⚠️` 记着一条实例——
「固件在测试运行中不接受任何配置改动」这条真规矩**只出现在 2 篇文档里、
且都写在章首 Note**，按 `docs` 排序它进不了候选头部。
**表里没有 ≠ 语料里没有。** 建页时不许把这张表当全集。

用：`python constraints.py` → `extract/constraint-candidates.csv` + `.md`
"""
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

OUT = Path(r'F:\master-dev\understand-anything-wiki\extract')
CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')

MIN_DOCS = 4        # 报告里只列「至少这么多篇文档都写了」的
SIM = 0.72          # 词集 Jaccard 相似度阈值：到了就并成一个候选
MIN_TOK = 4

# 约束标记词。**宁可宽一点**——这一层只是筛句子，窄了会漏掉整族规矩；
# 真正的过滤交给「多少篇文档复现」这个数。
MARK = re.compile(
    r'\b(?:only\s+(?:supported|available|possible|valid|allowed|works?|used|applies)'
    r'|not\s+(?:supported|possible|allowed|available|permitted|recommended)'
    r'|is\s+(?:not\s+)?(?:required|supported)'
    r'|(?:must|shall|has to|have to|need to|needs to|required to)'
    r'|cannot\s+be|can\s+only\s+be|may\s+not\s+be'
    r'|is\s+required|are\s+required|must\s+not)\b', re.I)

# 版本事实不属于本层。它们已经有归宿：142 个版本页 + `wiki/versions/`。
#
# **这个正则原来太窄**（2026-09-18 发现）。它只认「某版本引入」的五种写法
# （`introduced in` / `as of SmarTest N` / `new in SmarTest` / `was added in` /
# `since SmarTest N`），而语料里**同样是版本事实、同样该去版本页**的句子还写着：
#
#   `SmarTest 7.1.1: Test table is supported in TML 2.1.1.`
#   `Note: The HPPMU functionality is not supported in SmarTest 8.`
#   `Pogo cable assembly E8023PB is supported by SmarTest 7.5.4.4, 8.3.4.2, and higher.`
#   `Pattern debug not available in ST 7.6+`
#   `Starting with SmarTest 7.10 the system has to be recalibrated.`
#   `The High Precision PMU is no longer supported.`
#
# 六种，一种没被认出来，于是它们一路走进候选表，**占据了候选头部**
# （`n_doc` 前 20 名里有 6 名是版本事实）。这是**脚本 bug**，不是语料如此——
# 按计划里那条规矩，差异只有三种归宿，这一条属于 (a) 修。
#
# **第一版改法（`\b(?:smar?test|st|tml)\s*\d` 通吃）太钝，会误杀，我没采用。**
# 按那一版跑，263 行掉到 252 行，**11 行**。但把这 11 行逐行看过去，
# 其中一行是
#   `The specified fast_transfer_buffer_size must be a multiple of 8192 bytes for SmarTest 7.x.`
# ——那是一条**真要求**，只是适用范围带个版本号。「版本号出现在句子里」
# 和「这句话是版本事实」**不是一件事**。只看「少了几行」会把误杀当成收获。
#
# 所以真正的判据是**版本号出现在什么位置**：
#   ① 可用性谓词的宾语位 —— `is not supported in SmarTest 8` / `available in ST 7.6`
#      / `supported by SmarTest 7.5.4.4`
#   ② 句首标签后跟冒号 —— `SmarTest 7.1.1: ...` / `SmarTest 6.5.2: ...`
#   ③ 起始标记 —— `Starting with SmarTest 7.10`
#   ④ 无版本号的废弃事实 —— `is no longer supported`
# 而 `... for SmarTest 7.x` 是**范围限定**，四条都不沾，**留在表里**。
#
# **也不锚 `supported by` 后面的卡名**：`...are not supported by DC-Scale cards`
# 说的是**卡的类型**，不是版本。
#
# **误杀检查**（改之前跑的）：6 个已建 `constraints/` 页的 40 条英文引文，
# **一条都不命中**这条正则。**改判据必须两边都看。**
AVAIL = (r'(?:only\s+)?(?:supported|available|introduced|added|possible|valid|'
         r'allowed|enabled|disabled|recalibrat\w*|debug|required)')
NOT_CONSTRAINT = re.compile(
    r'(?:introduced\s+(?:in|before|with)|functional\s+change|'
    r'new\s+in\s+smar?test|was\s+added\s+in|has\s+been\s+added\s+in|'
    r'as\s+of\s+smar?test\s+\d|since\s+smar?test\s+\d'
    # ① 可用性谓词的宾语位
    r'|(?:' + AVAIL + r'|no\s+longer|starting\s+with|not\s+available)'
    r'[^.;]{0,40}?\b(?:smar?test|st|tml)\s*\d'
    # ② 句首标签 + 冒号
    r'|^\s*(?:note\s*:?\s*)?(?:smar?test|st|tml)\s*\d[\d.]*\s*:'
    # ④ 无版本号的废弃事实
    r'|no\s+longer\s+supported)', re.I)

STOP = set('''a an the of to in on for with and or is are was were be been being
that this these those it its as at by from if then than so such not no only
you your we our they their he she his her can could may might must shall should
will would do does did done has have had having there here when where which who
whom whose what how all any both each few more most other some own same very
one two three 0 1 2 3 4 5 6 7 8 9 use used using case cases following follows
described description refer reference see also note notes example examples'''.split())


def _skip_lines(txt):
    """剥 frontmatter 与代码块。

    代码块里的 `must` 是**示例代码的文本**，不是语料在陈述规矩。
    本仓库第三条铁律就是这个：`in_fence` 必须挡在一切解析之前
    （`extract.py` 里栽过一次，标题总数因此对不上基线）。
    """
    txt = re.sub(r'^---\n.*?\n---\n', '', txt, count=1, flags=re.S)
    return re.sub(r'```.*?```', ' ', txt, flags=re.S)


def sentences(txt):
    """粗切句：句号/问号/叹号后跟空白，或**行首的列表符/表格行**。

    表格行（`| ... |`）单独切，否则整张表会变成一句话，
    而表里每一行的约束是**各管各的**。
    """
    out = []
    for line in txt.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('|'):
            cells = [c.strip() for c in line.strip('|').split('|')]
            out.extend(c for c in cells if c)
            continue
        line = re.sub(r'^\s*[-*+]\s+', '', line)
        line = re.sub(r'^\s*\d+\.\s+', '', line)
        for s in re.split(r'(?<=[.!?])\s+', line):
            out.append(s.strip())
    return out


def norm(s):
    """归一化 —— 只用于**聚类和计数**，页面上引的永远是原文。"""
    s = re.sub(r'\[([^\]]*)\]\(<[^>]*>\)', r'\1', s)      # 链接 → 标签
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'\([^()]*\)', ' ', s)                      # 括号里多是举例/出处
    s = re.sub(r'[*_`#]', '', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    s = re.sub(r'^(?:note|please note|important|caution|warning)\s*[:,-]?\s*', '', s)
    s = re.sub(r'^(?:make sure that|make sure|ensure that|ensure|check that|'
               r'in this case,?|additionally,?|also,?)\s*', '', s)
    return s.rstrip(' .;:')


def toks(s):
    return frozenset(w for w in re.findall(r'[a-z0-9_]+', s)
                     if w not in STOP and len(w) > 1)


def similar(a, b):
    if not a or not b:
        return False
    inter = len(a & b)
    if inter < MIN_TOK:
        return False
    return inter / len(a | b) >= SIM


def cluster(items):
    """并查集。`items` = [(norm, toks, rel, verbatim)]。

    **不用「完全相同才算一条」**：同一句规矩在不同文档里写法有出入
    （`separated with a comma` / `separated by a comma` / `must be separated by a comma`），
    精确匹配会把它拆成一堆 1 篇的噪音，而它其实是**87 篇文档共有的写法约定**。
    这正是「按篇数排序」这个判据能不能work的前提，所以必须先合并。

    比对前先用倒排表剪枝：只在**共享一个稀有词**的句子之间比。
    全量两两比是 4,349²/2 ≈ 950 万次，跑得动但没必要。
    """
    n = len(items)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[max(rx, ry)] = min(rx, ry)

    inv = defaultdict(list)          # 词 → 句子下标
    for i, (_, tk, _, _) in enumerate(items):
        for w in tk:
            inv[w].append(i)
    rare = {w: ix for w, ix in inv.items() if 2 <= len(ix) <= 400}
    seen = set()
    for w, ix in rare.items():
        for a in range(len(ix)):
            for b in range(a + 1, len(ix)):
                p = (ix[a], ix[b])
                if p in seen:
                    continue
                seen.add(p)
                if similar(items[ix[a]][1], items[ix[b]][1]):
                    union(*p)
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return list(groups.values())


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    docs = [json.loads(l) for l in (OUT / 'docs.jsonl').open(encoding='utf-8')]
    items = []                        # (norm, toks, rel, verbatim)
    for d in docs:
        p = CORPUS / d['rel']
        if not p.exists():
            continue
        txt = _skip_lines(p.read_text(encoding='utf-8', errors='replace'))
        for s in sentences(txt):
            if not (25 <= len(s) <= 300) or not MARK.search(s):
                continue
            if NOT_CONSTRAINT.search(s):
                continue
            k = norm(s)
            if not (25 <= len(k) <= 300):
                continue
            tk = toks(k)
            if len(tk) < MIN_TOK:
                continue
            items.append((k, tk, d['rel'], re.sub(r'\s+', ' ', s).strip()))
    # **说明必须和代码是同一件事。** 这个数在第 239 行 `NOT_CONSTRAINT` **之后**，
    # 原来却写成「含约束标记的句子 N 条」——把版本事实那一层滤掉的事**没说**。
    # 是 2026-09-18 收紧 `NOT_CONSTRAINT` 时露的馅：同一份语料，
    # 钝版印 10566、准版印 10606，**+40**。只动了一个过滤器，数却变了，
    # 说明这个数**在过滤器下游**——那它旁边那句说明就一直是错的。
    print(f'含约束标记、且非版本事实的句子 {len(items)} 条（去重前）')

    groups = cluster(items)
    print(f'聚成 {len(groups)} 个候选')

    cands = []
    for g in groups:
        rels = {items[i][2] for i in g}
        if len(rels) < MIN_DOCS:
            continue
        # 代表句 = 覆盖文档数最多的那一句；并列时取更长的（信息更全）
        variants = defaultdict(lambda: {'docs': set(), 'text': ''})
        for i in g:
            k, _, rel, verb = items[i]
            variants[k]['docs'].add(rel)
            if len(verb) > len(variants[k]['text']):
                variants[k]['text'] = verb
        vs = sorted(variants.items(), key=lambda kv: (-len(kv[1]['docs']), -len(kv[0])))
        rep = vs[0][1]['text']
        cands.append({
            'docs': len(rels),
            'variants': len(vs),
            'sentences': len(g),
            'text': rep,
            'all_variants': [f"{len(v['docs'])}x :: {v['text']}" for _, v in vs],
            'rels': sorted(rels),
        })
    cands.sort(key=lambda c: (-c['docs'], -c['sentences'], c['text']))

    with (OUT / 'constraint-candidates.csv').open('w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['docs', 'variants', 'sentences', 'text', 'rels'])
        for c in cands:
            wr.writerow([c['docs'], c['variants'], c['sentences'], c['text'],
                         ';'.join(c['rels'])])
    print(f'✅ {len(cands)} 个候选（≥{MIN_DOCS} 篇文档）-> extract/constraint-candidates.csv')

    md = ['# constraint 页候选 —— **按「多少篇不同文档都写了这句规矩」排序**', '',
          f'由 `extract/constraints.py` 写。含约束标记、且非版本事实的句子 **{len(items)}** 条，'
          f'聚成 **{len(groups)}** 个候选，其中 **{len(cands)}** 个出现在 ≥{MIN_DOCS} 篇不同文档里。',
          '',
          '**怎么用**：一篇文档里的句子再多也只是它自己的事；'
          '**多篇文档不约而同写同一句，那才是该立页的 constraint。**'
          '`docs` = 复现它的文档数（判据），`variants` = 归一化后仍有几种写法（写法越多，'
          '越说明这条规矩散落在各处、没有一个地方讲全）。', '']
    for i, c in enumerate(cands, 1):
        md.append(f'## {i}. {c["docs"]} 篇 / {c["sentences"]} 句 / {c["variants"]} 种写法')
        md.append('')
        md.append(f'> {c["text"]}')
        md.append('')
        if c['variants'] > 1:
            md.append('<details><summary>全部写法</summary>')
            md.append('')
            for v in c['all_variants']:
                md.append(f'- {v}')
            md.append('')
            md.append('</details>')
            md.append('')
        md.append('出处（' + str(len(c['rels'])) + '）：')
        md.append('')
        for r in c['rels']:
            md.append(f'- `{r}`')
        md.append('')
    (OUT / 'constraint-candidates.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print(f'✅ 报告 -> extract/constraint-candidates.md（{sum(len(l) for l in md):,} 字符）')


if __name__ == '__main__':
    main()
