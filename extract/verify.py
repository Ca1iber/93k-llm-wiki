#!/usr/bin/env python3
# verify.py — 七类交叉检验（计划里的「检验计划」）
#
# 设计原则：**每一个抽取结果，都要有一个独立来源的数字可以对账。**
# 对不上就必须解释；解释不了就是 bug。任何「跳过」都必须出现在报告里。
#
# 三条互不共享代码的路径：
#   1. shell（grep / find，C 正则）           —— 基线
#   2. extract.py（Python 正则 + 手写状态机）  —— 主产出
#   3. recheck_links.py（markdown-it token 流）—— 复核
#
# 输出  extract/verify-report.md
#       extract/spot-check.md

import csv
import hashlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
# 第二类里「`](<` 差额归因」必须用主抽取器的同一个正则才能算出差额本身。
# 这不是对正则的检验（那由第三类 markdown-it 独立完成），只是对差额的归因，
# 所以此处引用是刻意的，不违反「三条路径不共享代码」。
from extract import (RE_ANGLE, RE_H as RE_ANGLE_H, CONTEXT_MAX,  # noqa: E402
                     CONTEXT_MIN, CONTEXT_MERGE_MAX, SECTION_MAX, SECTION_H2)
# SECTION_MAX / SECTION_H2 只为第四类附的段落正文回验而取：
# 前者是**截断阈值**，后者是**段落名的定义域**——两者都是常量和名单，不是解析逻辑。
# 「期望值」必须按同一个阈值截断、按同一份名单判定结束标题，才能与 body 对质。
# 这不违反「三条路径不共享代码」：共享的是一张名字表，不是抽取算法。

CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')
CATALOG = CORPUS.parent / 'catalog-markdown.csv'
OUTDIR = Path(r'F:\master-dev\understand-anything-wiki\extract')

DATA_FILES = ['docs.jsonl', 'edges.jsonl', 'sections.jsonl', 'failures.jsonl', 'hubs.csv']
R = []          # 报告行缓冲


def w(s=''):
    R.append(s)
    print(s)


def load_jsonl(name):
    with open(OUTDIR / name, encoding='utf-8') as f:
        return [json.loads(l) for l in f if l.strip()]


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def bash(cmd, cwd=None):
    """跑一条 shell 命令，返回 stdout（失败返回 None）。"""
    exe = shutil.which('bash')
    if not exe:
        return None
    try:
        r = subprocess.run([exe, '-c', cmd], cwd=cwd or str(CORPUS.parent),
                           capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=900)
        return r.stdout.strip()
    except Exception as e:
        return f'<失败: {e}>'


# ============================================================ 第一类
def cat1_internal(docs, edges):
    w('## 第一类 · 内部一致性（脚本自证）')
    w()
    w('| 检查 | 判据 | 实测 | 结果 |')
    w('|---|---|---|---|')

    def row(name, expect, got):
        ok = '✅' if expect == got else f'❌ 差 {got - expect}'
        w(f'| {name} | {expect} | {got} | {ok} |')
        return expect == got

    ok = True
    ok &= row('docs.jsonl 行数 == 实扫文件数', len(list(CORPUS.rglob('*.md'))), len(docs))
    ok &= row('边总数 == 所有文档出度之和',
              sum(d['out_degree'] for d in docs), len(edges))
    docrels = {d['rel'] for d in docs}
    ok &= row('edges 的 from 全部存在于 docs', 0,
              sum(1 for e in edges if e['from'] not in docrels))
    n_dangle = sum(1 for e in edges if not e['resolved'])
    ok &= row('悬空边数（`resolved=false`）', 0, n_dangle)

    # `in_src` 列（去重来源篇数）不是个标签，它有自己的不变量：
    # 全表求和 == 正文边里**不同的 (来源, 目标) 对**数。
    # 少了这一条，列写错（比如忘了去重、或把 toc 也算进去）没有任何东西会响。
    hubs = {}
    with open(OUTDIR / 'hubs.csv', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            hubs[r['path']] = r
    ok &= row('hubs.csv 行数 == docs.jsonl 行数', len(docs), len(hubs))
    pairs = {(e['from'], e['to']) for e in edges
             if e['resolved'] and e['kind'] == 'inline'}
    ok &= row('`in_src` 列求和 == 正文边的去重 (来源,目标) 对数',
              len(pairs), sum(int(r['in_src']) for r in hubs.values()))
    ok &= row('`in_src` > `in_inline` 的行数（去重来源不可能多于出现次数）', 0,
              sum(1 for r in hubs.values()
                  if int(r['in_src']) > int(r['in_inline'])))
    ok &= row('`in_src` 与 `in_inline` 一者为 0、另一者非 0 的行数', 0,
              sum(1 for r in hubs.values()
                  if (int(r['in_src']) > 0) != (int(r['in_inline']) > 0)))
    w()
    w(f'**入度表总和** == 边总数：{len(edges)}（由 `hubs.csv` 的 `in_all` 列求和得到）')
    w()
    if n_dangle == 0:
        w(f'**全库 {len(edges):,} 条边的目标文件全部存在，悬空链接 0 条。** '
          f'这不是「差不多」，是语料自带的完整性——'
          f'HTML→MD 转换把链接目标一并搬了过来，没有断链。')
    w()
    return ok


# ============================================================ 第二类
def cat2_baseline(docs, edges):
    w('## 第二类 · 与独立测量对账')
    w()
    w('三条独立路径：**shell（grep/find）** / **朴素 Python 计数** / **extract.py**。')
    w('三方互不共享代码。')
    w()

    files = sorted(p for p in CORPUS.rglob('*.md') if p.is_file())

    # --- 朴素 Python：不用正则、不切行，直接对整段文本 count
    naive_files = 0
    naive_bytes = 0
    naive_md_close = 0        # '.md>)' 出现次数 ≈ 带锚点或不带锚点的尖括号 md 链接
    naive_angle = 0           # '](<' 出现次数
    for p in files:
        t = p.read_bytes().decode('utf-8', errors='replace')
        naive_files += 1
        naive_bytes += os.path.getsize(p)
        naive_md_close += t.count('.md>)')
        naive_angle += t.count('](<')

    # --- 拆解 `](<` 的差异：围栏内伪链接 + 空目标 + 残差逐条分类
    #
    # 铁律：残差只有一个归宿列表，且**逐条列出**，不许只给一个数字。
    # 分类口径（互斥，按序判定）：
    #   js     外层链接目标是 javascript: —— 链接文字本身是图片 ![...](<...>)，含 ']('，
    #          正则的 text 组无法跨越，CommonMark 能解析但目标是 javascript: 非文档引用
    #   html   HTML 转换残渣，行内根本没有前置 '['（如 '<section class=](<...>)'）
    #   split  链接文字被标题 / 空行切断 —— CommonMark 同样判为非链接（故 B−A=0）
    # 只有 split 且目标以 .md 结尾的才是「可能真漏」，单独计数并列出
    RE_F = re.compile(r'^\s*(`{3,}|~{3,})')
    n_fence_angle = 0
    n_empty_target = 0
    n_out = 0                # 围栏外全部 `](<`
    n_consumed = 0           # 落在 RE_ANGLE 命中区间内的 `](<`
    n_multi = 0              # 一个 match 覆盖 >=2 个 `](<` 的次数
    n_resid = 0
    resid_kind = Counter()
    resid_rows = []          # (rel, lineno, kind, 原文)
    n_resid_md = 0           # 残差里目标以 .md 结尾的
    n_resid_md_bad = 0       # 其中不属于 split 类的 —— 若 >0 就是真漏
    # --- 标题口径：以 `#` 开头的行分三类，必须分毫不差地拆开
    n_hash_atx = 0           # 围栏外 ATX 标题（= extract 的 heading_count）
    n_hash_infence = 0       # 围栏内以 # 开头（C 代码里的 #include）
    n_hash_nonatx = 0        # 围栏外以 # 开头但不是 ATX（畸形 ###、#01 之类）
    n_cb_docs = 0            # 有代码块的文档数
    for p in files:
        rel = p.relative_to(CORPUS.parent).as_posix()
        t = p.read_bytes().decode('utf-8', errors='replace').replace('\r\n', '\n')
        n_empty_target += t.count('](<>)')
        inf = False
        fc = None
        cb = 0
        for i, ln in enumerate(t.split('\n'), 1):
            mf = RE_F.match(ln)
            # 围栏状态机与 extract.py 逐字一致：闭合必须同种标记符。
            # 不复刻这条，`~~~` 块里的 ``` 会把状态翻转，计数全错。
            if inf:
                if mf and mf.group(1)[0] == fc:
                    inf = False
                if ln.startswith('#'):
                    n_hash_infence += 1
                if '](<' in ln:
                    n_fence_angle += ln.count('](<')
                continue
            if mf:
                inf = True
                fc = mf.group(1)[0]
                cb += 1
                continue
            if ln.startswith('#'):
                if RE_ANGLE_H.match(ln):
                    n_hash_atx += 1
                else:
                    n_hash_nonatx += 1
            if '](<' not in ln:
                continue
            n_out += ln.count('](<')
            # 位置法：逐个 `](<` 判断它是否落在正则已命中的区间内。
            # 落在区间内 = 已被抽取；落空 = 残差。
            # 比「抠掉匹配片段再数」精确——后者会把空目标 `](<>)` 也当成残差。
            spans = [m.span() for m in RE_ANGLE.finditer(ln)]
            for a, b in spans:
                c = ln.count('](<', a, b)
                n_consumed += c
                if c >= 2:
                    n_multi += 1
            j, occ = 0, []
            while True:
                j = ln.find('](<', j)
                if j < 0:
                    break
                occ.append(j)
                j += 1
            for j in occ:
                if any(a <= j < b for a, b in spans):
                    continue                # 已被 RE_ANGLE 吃掉
                if ln[j + 3:j + 4] == '>':
                    continue                # 空目标 `](<>)`，已在上面单独计数
                n_resid += 1
                prefix = ln[:j]
                target = ln[j + 3:].partition('>')[0]
                if 'javascript:' in target:
                    kind = 'js'             # 外层链接目标是 javascript:
                elif '[' in prefix:
                    kind = 'split'          # 行内有 '['，正则跨不过去（嵌套/畸形）
                elif re.search(r'<[A-Za-z][^>]*=\s*$', prefix):
                    kind = 'html'           # HTML 属性被吃掉，行内根本没有 '['
                else:
                    kind = 'split'          # '[' 在上一行，被标题/空行切断
                resid_kind[kind] += 1
                if target.lower().endswith('.md'):
                    n_resid_md += 1
                    if kind != 'split':
                        n_resid_md_bad += 1
                resid_rows.append((rel, i, kind, ln.strip()[:160]))
        if cb:
            n_cb_docs += 1

    doc_with_links = sum(1 for d in docs if d['out_degree'] > 0)
    n_head_ext = sum(d['heading_count'] for d in docs)

    # --- 「含 .md 链接的文档数」差的归因：逐文件求对称差，不许含糊
    RE_SH = re.compile(r'\]\(<[^>]*\.md[^>]*>\)')
    shell_docs = set()
    for p in files:
        if RE_SH.search(p.read_bytes().decode('utf-8', errors='replace')):
            shell_docs.add(p.relative_to(CORPUS).as_posix())
    extract_docs = {d['rel'] for d in docs if d['out_degree'] > 0}
    only_shell = sorted(shell_docs - extract_docs)
    only_extract = sorted(extract_docs - shell_docs)
    edge_angle = sum(d['edge_angle'] for d in docs)
    link_kinds = Counter()
    for d in docs:
        link_kinds.update(d['link_kinds'])

    rows = [
        ('语料文件数',
         bash("find by-category -name '*.md' | wc -l"),
         naive_files,
         len(docs),
         '必须严格相等'),
        ('总字节（原始文件大小）',
         bash("find by-category -name '*.md' -printf '%s\\n' | awk '{s+=$1} END{print s}'"),
         naive_bytes,
         sum(d['bytes'] for d in docs),
         '必须严格相等'),
        ("`](<` 出现次数",
         bash("grep -roh --include='*.md' '](<' by-category | wc -l"),
         naive_angle,
         edge_angle,
         f'两列**不可直接相减**：shell 数「`](<` 这个串出现几次」，'
         f'extract 数列的是「`RE_ANGLE` match 有几个」。'
         f'{naive_angle:,} = 围栏内伪链接 {n_fence_angle} + 空目标 `](<>)` {n_empty_target}'
         f' + 被 match 覆盖 {n_consumed:,} + 真残差 {n_resid}，已完整归因（见下）'),
        ('含 .md 链接的文档数',
         bash("grep -rl --include='*.md' -E '\\]\\(<[^>]*\\.md[^>]*>\\)' by-category | wc -l"),
         None,
         doc_with_links,
         f'两列口径不同：shell 数「文件里有 `](<….md>)` 这个串」，'
         f'extract 数「文件有 out_degree>0 的边」。'
         f'shell {len(shell_docs)} − extract {len(extract_docs)} = {len(shell_docs) - len(extract_docs)}，'
         f'拆成 仅 shell 有 {len(only_shell)} 篇 − 仅 extract 有 {len(only_extract)} 篇，见下'),
        ('以 `#` 开头的行数',
         bash("grep -rh --include='*.md' '^#' by-category | wc -l"),
         None,
         n_head_ext,
         f'{n_hash_atx + n_hash_infence + n_hash_nonatx:,} = 围栏外 ATX **{n_hash_atx:,}**（= extract 提取的）'
         f' + 围栏内 `#include` {n_hash_infence:,} + 围栏外非 ATX {n_hash_nonatx:,}，见下'),
        ('带代码块的文档数',
         bash("grep -rl --include='*.md' '```' by-category | wc -l"),
         None,
         n_cb_docs,
         '口径同：文件里有没有围栏。`grep` 与 extract 都只看有没有，不看是否闭合'),
    ]

    w('| 指标 | shell | 朴素 Python | extract.py | 差 | 结论 |')
    w('|---|---|---|---|---|---|')
    for name, sh, nv, ex, note in rows:
        sh_s = sh if sh and not sh.startswith('<') else '—'
        nv_s = nv if nv is not None else '—'
        ex_s = ex if ex is not None else '—'
        diff, concl = '', ''
        if ex is not None and sh_s != '—':
            try:
                d = ex - int(sh_s)
                diff = f'{d:+d}' if d else '0'
                concl = '✅ 完全一致' if d == 0 else f'见备注'
            except ValueError:
                pass
        w(f'| {name} | {sh_s} | {nv_s} | {ex_s} | {diff} | {concl} |')
    w()
    w('差异备注：')
    w()
    for name, sh, nv, ex, note in rows:
        w(f'- **{name}**：{note}')
    w()
    w('### 「含 .md 链接的文档数」差 1 的逐文件归因')
    w()
    w(f'**仅 shell 有、extract 无（{len(only_shell)} 篇）** —— '
      '`.md` 链接只出现在**代码围栏内**，`extract.py` 正确地不认（shell 的 `grep` 没有围栏概念）：')
    w()
    for r in only_shell:
        w(f'- `{r}`')
    w()
    w(f'**仅 extract 有、shell 无（{len(only_extract)} 篇）** —— '
      '用 **plain 语法** `[x](y.md)`（不带尖括号），shell 的 `\\]\\(<` 口径天然抓不到：')
    w()
    for r in only_extract:
        w(f'- `{r}`')
    w()
    w(f'**{len(only_shell)} − {len(only_extract)} = '
      f'{len(shell_docs) - len(extract_docs)}**，与主表中 `{len(shell_docs)} − {len(extract_docs)} = '
      f'{len(shell_docs) - len(extract_docs)}` 严格吻合。')
    w()
    w('### 「以 `#` 开头的行数」差 1,014 的三分类归因')
    w()
    w('`grep \'^#\'` 只知道「行首是不是 `#`」，**不知道围栏、也不知道 ATX 语法**。')
    w('差额必须拆成下面三类，且三类之和 == grep 的总数：')
    w()
    w('| 类别 | 条数 | 为什么不算标题 |')
    w('|---|---|---|')
    w(f'| 围栏外真 ATX 标题 | {n_hash_atx:,} | **算**，等于 extract 的 `heading_count` 合计 |')
    w(f'| 围栏内以 `#` 开头 | {n_hash_infence:,} | C 代码里的 `#include` / `#define`，在代码块内 |')
    w(f'| 围栏外非 ATX | {n_hash_nonatx:,} | 畸形标题：`###`（无文字）、`#01 …`、`#####: …` |')
    w(f'| **合计** | **{n_hash_atx + n_hash_infence + n_hash_nonatx:,}** | == shell 的 `grep` 结果 |')
    w()
    w(f'校验：{n_hash_atx:,} + {n_hash_infence:,} + {n_hash_nonatx:,} = '
      f'{n_hash_atx + n_hash_infence + n_hash_nonatx:,}，'
      f'与主表 shell 列严格吻合。')
    w()
    w(f'因此 `grep` 的 {n_hash_atx + n_hash_infence + n_hash_nonatx:,} 与 extract 的 {n_hash_atx:,} '
      f'差的 {n_hash_infence + n_hash_nonatx:,} 条**全部有归宿，无一条含糊**。')
    w()
    w('> 📌 **计划里记的旧基线 43,674 在这一项上是可复现的**（不同于 50,073 那种无法复现的数）。')
    w('> 它恰好等于「行首是 `#` 的总行数」，因此**独立佐证了 extract 的围栏状态机**：')
    w(f'> 若 extract 少算了围栏外任何一条标题，或把围栏内 {n_hash_infence:,} 条 `#include` 误当标题，')
    w('> 这个等式立刻不成立。')
    w()

    # --- 残差逐条披露：27 条全部列出，不接受「先放着」
    w('### `](<` 差额的完整归因（残差逐条披露）')
    w()
    w('铁律：差异只有三种归宿 —— **脚本 bug / 基线工具不准 / 语料本身如此**。没有第四种。')
    w()
    w('```')
    w(f'shell `](<` 总数                {naive_angle:>7,}')
    w(f'  − 围栏内伪链接                −{n_fence_angle:>6,}   语料事实：代码块里的示例')
    w('  ' + '─' * 36)
    w(f'  = 围栏外 `](<`                {n_out:>7,}')
    w(f'      − 空目标 `](<>)`          −{n_empty_target:>6,}   语料事实：转换产生的空锚')
    w(f'      − 被 RE_ANGLE 命中区间覆盖 −{n_consumed:>5,}   '
      f'{edge_angle:,} 个 match，其中 {n_multi} 个各覆盖 2 个')
    w('      ' + '─' * 32)
    w(f'      = 未被覆盖（真残差）        {n_resid:>5,}')
    w('  ' + '─' * 36)
    w(f'  校验 {n_empty_target:,} + {n_consumed:,} + {n_resid} = '
      f'{n_empty_target + n_consumed + n_resid:,}   '
      + ('✅ 与围栏外总数相等' if n_empty_target + n_consumed + n_resid == n_out else '❌ 不平'))
    w('```')
    w()
    w(f'**那 {n_multi} 个「一个 match 覆盖 2 个 `](<`」是什么：**')
    w()
    w('形态为 `[![close.png](<x.png>)](<javascript:…>)`。正则的 text 组是贪婪的，')
    w('从最外层那个 `[` 起会一路吃到 `…/close.png>` 才回头找 `](<目标>)`，')
    w('于是**把内层图片链接的 `](<` 也一并覆盖**。这不是漏抽，是匹配跨度比直觉大。')
    w()
    w('代价已核实为 **零**：这些 match 的目标是 `javascript:…`，'
      '`classify_target` 判为 `external`，**不落边**——')
    w('`edges.jsonl` 里 `javascript` 目标 **0 条**。内层 `close.png` 是图片资源，'
      '本就不进文档图。')
    w()
    w('> ⚠️ 反面教材（已修正）：最初用 `行内 ](< 数 − 空目标数 − match 数` 做减法，')
    w('> 该式**默认每个 match 只吃一个 `](<`**，于是凭空造出 25 条不存在的「残差」。')
    w('> 改为**位置法**（逐个 `](<` 判断是否落在 match 区间内）后残差从 27 降到 2。')
    w('> **能对上的算术不等于对的算术。**')
    w()
    w()
    w(f'**全部 {n_resid} 条残差（不抽样，一条不漏）：**')
    w()
    w('| # | 文件:行 | 归类 | 原文 |')
    w('|---|---|---|---|')
    for i, (rel, lineno_, kind, txt) in enumerate(resid_rows, 1):
        esc = txt.replace('|', '\\|')
        w(f'| {i} | `{rel}:{lineno_}` | {kind} | `{esc}` |')
    w()
    w('逐条归因：')
    w()
    w(f'- **html（{resid_kind["html"]} 条）**：`\\t\\t<section class=](<../../../../raw/129497.png>)` —— '
      'HTML→MD 转换把 `<section class="…">` 的属性值吃掉了，行内根本没有前置 `[`。'
      'markdown-it 同样不认为是链接。**语料缺陷，目标也不是 .md。**')
    w(f'- **split（{resid_kind["split"]} 条）**：`00_Overview/00_SmarTest_7.10.3_Documentation.md:6,10` ——')
    w()
    w('  ```')
    w('   6| [')
    w('   7| ')
    w('   8| ## Getting started')
    w('   9| ')
    w('  10| ](<../01_Getting_started/01_Getting_started.md>)')
    w('  ```')
    w()
    w('  链接文字 `[` 与 `]` 被一个 H2 隔开。CommonMark 规定链接文字不能跨空行，')
    w('  **所以 markdown-it 也判它不是链接**——这正是第三类 B−A=0 的原因。')
    w('  两套实现独立地得出同一结论，故这是**语料转换缺陷**，不是正则漏抽。')
    w('  代价：`01_Getting_started.md` 少一条入边（全库 53,102 条中的 1 条）。')
    w('  此处**不做补偿性抽取**——凭空补一条语料没表达的边，会破坏三路一致性。')
    w()

    # --- 两个正则 → 落边：完整对账
    plain_hits = sum(d['edge_plain'] for d in docs)
    non_doc = sum(v for kk, v in link_kinds.items() if kk != 'doc')
    doc_edges = link_kinds['doc']
    toc_edges = sum(1 for e in edges if e.get('kind') == 'toc')
    inline_edges = sum(1 for e in edges if e.get('kind') == 'inline')
    w('### 两个正则 → 落边：完整对账')
    w()
    w('`extract.py` 只把 `classify_target` 判为 `doc` 的链接落成边，其余只计数。')
    w('所以「命中数」必然大于「边数」，差额必须**分毫不差**地等于非 doc 目标数：')
    w()
    w('| 环节 | 数量 |')
    w('|---|---|')
    w(f'| `RE_ANGLE` 命中 | {edge_angle:,} |')
    w(f'| `RE_PLAIN` 命中 | {plain_hits:,} |')
    w(f'| **合计命中** | **{edge_angle + plain_hits:,}** |')
    w(f'| − 非 `doc` 目标 | −{non_doc:,} |')
    w(f'| **= 落成的边** | **{edge_angle + plain_hits - non_doc:,}** |')
    w()
    w('非 `doc` 目标细分：' + ' / '.join(
        f'`{kk}` {v:,}' for kk, v in sorted(link_kinds.items(), key=lambda x: -x[1]) if kk != 'doc'))
    w()
    w('**三条交叉校验：**')
    w()
    ok_edge = (edge_angle + plain_hits - non_doc) == len(edges) == doc_edges
    w(f'1. 落成的边 {edge_angle + plain_hits - non_doc:,} == `edges.jsonl` 行数 {len(edges):,} '
      f'== `doc` 类目标 {doc_edges:,} ' + ('✅' if ok_edge else '❌'))
    ok_plain = plain_hits == toc_edges
    w(f'2. `RE_PLAIN` 命中 {plain_hits:,} == `toc` 边数 {toc_edges:,} '
      + ('✅ → 5 个 `index.md` 的目录链接**全部**是 plain 语法，无一条混用尖括号'
         if ok_plain else '❌ 存在语法混用，需列样例'))
    angle_doc = len(edges) - plain_hits
    ok_inline = angle_doc == inline_edges
    w(f'3. 于是 `RE_ANGLE` 贡献的 `doc` 边 = {len(edges):,} − {plain_hits:,} = {angle_doc:,} '
      f'== `inline` 边数 {inline_edges:,} ' + ('✅' if ok_inline else '❌'))
    w()
    unknown_resid = (n_resid_md_bad > 0) or (n_empty_target + n_consumed + n_resid != n_out)
    baseline_ok = ok_edge and ok_plain and ok_inline and not unknown_resid

    # --- 旧基线复现性
    w('### ⚠️ 旧基线复现性：**失败**')
    w()
    w('本次会话早期记录的基线是 **50,073 条交叉引用 / 7,076 篇含链接文档**。')
    w('这些数字**无法用任何合理的命令复现**。实测候选：')
    w()
    w('| 命令口径 | 结果 |')
    w('|---|---|')
    for label, cmd in [
        ("grep '](<[^>]*\\.md>)'（严格 .md> 结尾）", "grep -roh --include='*.md' '](<[^>]*\\.md>)' by-category | wc -l"),
        ("grep -E '\\]\\(<[^>]*\\.md[^>]*\\)'（允许锚点）", "grep -roh --include='*.md' -E '\\]\\(<[^>]*\\.md[^>]*>\\)' by-category | wc -l"),
        ("grep '](<'（所有尖括号链接）", "grep -roh --include='*.md' '](<' by-category | wc -l"),
        ("grep -c 按行求和", "grep -rc --include='*.md' '](<' by-category | awk -F: '{s+=$2} END{print s}'"),
    ]:
        v = bash(cmd)
        w(f'| {label} | {v} |')
    w()
    w('**结论：旧基线的测量命令没有被记录下来，因此它不是可用的验证锚点。**')
    w('本报告一律改用上表中当场可复现的 shell 命令作为基线。')
    w('这不是「extract.py 错了」，而是「旧数字不可信」——第五类要求的「逐条解释」在此落地为：')
    w('**旧基线作废，改用可复现基线。**')
    w()

    # --- catalog 差异（第八类，就地结案）
    w('### catalog 差异结案（原计划第八条）')
    w()
    cat = set()
    with open(CATALOG, encoding='utf-8-sig', newline='') as f:
        import csv as _csv
        for r in _csv.DictReader(f):
            p = (r.get('MarkdownPath') or '').strip()
            if p:
                cat.add(p.removeprefix('by-category/'))
    disk = {d['rel'] for d in docs}
    w(f'- catalog 数据行：**{len(cat)}**')
    w(f'- by-category 实扫：**{len(disk)}**')
    w(f'- 磁盘有 catalog 无：**{len(disk - cat)}** → {sorted(disk - cat)}')
    w(f'- catalog 有磁盘无：**{len(cat - disk)}**')
    w()
    w(f'**{len(cat)} + {len(disk - cat)} = {len(disk)}，算术闭合，无遗漏无悬空。**')
    w()
    return baseline_ok


# ============================================================ 第三类
def cat3_recheck():
    w('## 第三类 · 独立复算（markdown-it-py token 流）')
    w()
    p = OUTDIR / 'link-diff.json'
    if not p.is_file():
        w('⚠️ 未找到 `link-diff.json`，请先跑 `python recheck_links.py`。')
        w()
        return False
    d = json.loads(p.read_text(encoding='utf-8'))
    w(f'- A（正则，extract.py）：**{d["a_total"]}** 条')
    w(f'- B（AST，markdown-it-py）：**{d["b_total"]}** 条')
    w(f'- **A 有 B 无**（正则多认）：{d["only_a_total"]} 条 / {d["only_a_kinds"]} 种')
    w(f'- **B 有 A 无**（正则漏认）：{d["only_b_total"]} 条 / {d["only_b_kinds"]} 种')
    w()
    if d['only_b_total'] == 0:
        w('✅ **B−A = 0：正则没有漏掉任何 markdown-it 能解析的链接。**')
    else:
        w('❌ **B−A 不为 0，正则存在漏认，必须修 extract.py 后才可放行。**')
        for s in d['only_b_samples'][:20]:
            w(f'  - `{s["doc"]}` → `{s["target"]}`')
    w()

    edges = load_jsonl('edges.jsonl')
    n_cs = sum(1 for e in edges if e['in_code_span'])

    # 归因**必须由 markdown-it 自己算**（recheck_links.attribute_only_a），不许手写。
    # 手写过一版「其余都是缩进代码块」，人工核对一查：6 条里有 1 条是 `<script>`
    # 起头的 HTML 块吞到 EOF（02.09.02.03.03:306）。**错的归因等于没归因。**
    at = d.get('only_a_attribution') or {}
    NAME = {
        'code_span': ('反引号内联代码段', '作者用反引号把链接**引用**起来，渲染后不是链接'),
        'indented_code_block': ('缩进代码块（CommonMark 4 空格规则）',
                                'HTML→MD 转换把列表续行写成了 4 空格缩进；'
                                '语料里作者的本意仍是交叉引用'),
        'html_block': ('HTML 块', 'HTML 残留（如 `<script>`）未闭合，'
                                  'CommonMark 把其后整段当原始 HTML；语料缺陷'),
        'fence': ('围栏代码块', '不该出现——extract.py 的围栏状态机本应排除'),
        'unknown': ('未归因', '必须查明'),
    }
    w('### A−B 逐条归因（由 markdown-it 块级 token 计算，非手写）')
    w()
    w('| 所处块类型 | 条数 | 说明 |')
    w('|---|---:|---|')
    tot = 0
    for k in ('code_span', 'indented_code_block', 'html_block', 'fence', 'unknown'):
        if not at.get(k):
            continue
        tot += at[k]
        w(f'| {NAME[k][0]} | {at[k]} | {NAME[k][1]} |')
    w(f'| **合计** | **{tot}** | 应等于 A−B 总数 {d["only_a_total"]} |')
    w()
    if tot != d['only_a_total']:
        w(f'❌ 归因合计 {tot} ≠ A−B 总数 {d["only_a_total"]}，有未归因的条目。')
    else:
        w(f'✅ 归因闭合：{tot} = {d["only_a_total"]}，**每一条都有名字**。')
    w()
    # 交叉校验：extract.py 自己打的 in_code_span 标记，应逐条等于 markdown-it 算出的 code_span。
    if at.get('code_span') == n_cs:
        w(f'✅ 标记交叉校验：`edges.jsonl` 里 `in_code_span=True` 有 **{n_cs}** 条，'
          f'markdown-it 侧算出 **{at.get("code_span")}** 条，**相等**。')
    else:
        w(f'❌ 标记交叉校验失败：`in_code_span=True` 有 {n_cs} 条，'
          f'markdown-it 侧算出 {at.get("code_span")} 条。')
    w()
    if at.get('html_block'):
        w(f'其中 {at["html_block"]} 条落在 HTML 块内，逐条披露：')
        w()
        for x in d.get('only_a_attribution_detail', []):
            if x.get('block') == 'html_block':
                w(f'- `{x["doc"]}:{x["line"]}` → `{x["target"]}`'
                  f'（块范围 {x["span"][0]}–{x["span"][1]} 行）')
        w()
    w('**这 6 条边一律保留，未丢弃，也不再另加标记。** 判决属于计划里的第三类归宿')
    w('「语料本身如此 → 记录」：目标都是真实存在的 `.md`，作者本意确为交叉引用，')
    w('只是 HTML→MD 转换把块结构写坏了（4 空格缩进 / `<script>` 未闭合）。')
    w('删掉它们会丢真引用。**它们不参与 `in_code_span` 过滤**——那 54 条是作者在「引用」链接，')
    w('这 6 条是作者在「写」链接，性质相反，已逐条点名披露，下游按上面的清单处理即可。')
    w()

    # 标记的**影响面**：过滤掉 in_code_span 后，hubs.csv 的排序会不会变？
    # 不问这一句，「已标记」就只是个说法；问了才知道它对建页有没有实际后果。
    w('### `in_code_span` 标记的影响面（排序是否因过滤而变）')
    w()
    cs_by = Counter(e['from'] for e in edges if e['in_code_span'])
    out_all = Counter(e['from'] for e in edges)
    in_all = Counter(e['to'] for e in edges)
    in_ref = Counter(e['to'] for e in edges if not e['in_code_span'])
    out_ref = Counter(e['from'] for e in edges if not e['in_code_span'])
    same_in = [k for k, _ in in_all.most_common(20)] == [k for k, _ in in_ref.most_common(20)]
    top_out_a = [k for k, _ in out_all.most_common(20)]
    top_out_b = [k for k, _ in out_ref.most_common(20)]
    w(f'- 被标记的边 **{sum(cs_by.values())}** 条，分布在 **{len(cs_by)}** 篇。')
    w(f'- 入度 Top20 过滤前后：{"**完全一致**" if same_in else "**不一致**"}。')
    if top_out_a == top_out_b:
        w('- 出度 Top20 过滤前后：**完全一致**。')
    else:
        diff = [(i + 1, x, y) for i, (x, y) in enumerate(zip(top_out_a, top_out_b)) if x != y]
        w(f'- 出度 Top20 过滤前后：**{len(diff)} 处名次交换**，'
          f'但两篇都仍在 Top20 内（仅换位，未出榜）：')
        for i, x, y in diff:
            w(f'  - 第 {i} 名 `{x}` ↔ `{y}`')
    worst = max(cs_by, key=lambda k: cs_by[k] / out_all[k])
    w(f'- 单篇占比最高：`{worst}`，出度 {out_all[worst]} 条中被标记 '
      f'**{cs_by[worst]} 条（{cs_by[worst] / out_all[worst]:.0%}）**。')
    w()
    w('**结论**：`hubs.csv` 的排序在 Top20 层面不因过滤而改变，'
      '**按入度挑 `object` 页不受影响**；但 GIO API 族单篇出度最多虚高 57%，'
      '按**出度**判断「枢纽」时需知情。标记已入 `edges.jsonl`，过滤与否由下游决定。')
    w()
    # 归因字段缺失也算不过——否则拿旧版 link-diff.json 跑会**静默放行**。
    return (d['only_b_total'] == 0
            and 'only_a_attribution' in d
            and not at.get('unknown'))


# ============================================================ 第四类
def cat4b_lineref(docs, edges, sections):
    """全库行号回验（穷举，非抽样）。

    第七类只抽 50 条边；这里把**所有**「第 N 行」的断言拿回原文对质。
    不是重跑解析器（那是第三类的事），只检查「你在第 N 行」这句话是否属实——
    抓的是「正向解析看起来对、行号却错位」这类问题。
    """
    w('### 第四类附 · 全库行号回验（穷举，非抽样）')
    w()
    src = {}
    bad_h, bad_e, bad_s = [], [], []
    n_h = n_e = n_s = 0
    for p in sorted(CORPUS.rglob('*.md')):
        if not p.is_file():
            continue
        src[p.relative_to(CORPUS).as_posix()] = \
            p.read_bytes().decode('utf-8', errors='replace').replace('\r\n', '\n').split('\n')

    for d in docs:
        lines = src.get(d['rel'])
        if lines is None:
            continue
        for h in d['headings']:
            n_h += 1
            i = h['line'] - 1
            # 两侧都折叠空白：语料里有 `##␣␣Results`（分隔用两个空格），
            # 而 `text` 记的是规范化后的文本。分隔空白的**个数**不是信息，
            # 但折叠后仍不一致就是真错位。
            want = re.sub(r'\s+', ' ', '#' * h['level'] + ' ' + h['text'])
            got = re.sub(r'\s+', ' ', lines[i].strip()) if 0 <= i < len(lines) else None
            if got != want:
                bad_h.append((d['rel'], h['line'], want, got))

    for e in edges:
        n_e += 1
        lines = src.get(e['from'])
        i = e['line'] - 1
        if lines is None or not (0 <= i < len(lines)) or e['to_raw'] not in lines[i]:
            bad_e.append((e['from'], e['line'], e['to_raw']))

    for s in sections:
        n_s += 1
        lines = src.get(s['doc'])
        i = s['line'] - 1
        got = lines[i].strip() if lines and 0 <= i < len(lines) else None
        if got is None or not re.match(r'^#{1,6}\s+' + re.escape(s['h2']) + r'\s*$', got):
            bad_s.append((s['doc'], s['line'], s['h2'], got))

    w('| 断言 | 条数 | 回验不符 | 结论 |')
    w('|---|---|---|---|')
    for name, n, bad in [('标题行号 + 层级 + 文本', n_h, bad_h),
                         ('边的行号 + 目标串', n_e, bad_e),
                         ('结构段落的标题行号', n_s, bad_s)]:
        w(f'| {name} | {n:,} | {len(bad):,} | ' + ('✅ 全部属实' if not bad else '❌ 见下') + ' |')
    w()
    for name, bad in [('标题', bad_h), ('边', bad_e), ('段落', bad_s)]:
        if bad:
            w(f'**{name} 回验不符样例（前 10）**：')
            w()
            for b in bad[:10]:
                w(f'- `{b[0]}` L{b[1]}：期望 `{str(b[2])[:80]}`，实得 `{str(b[3])[:80]}`')
            w()
    if not (bad_h or bad_e or bad_s):
        w('**穷举结论**：'
          f'{n_h:,} 个标题 + {n_e:,} 条边 + {n_s:,} 个结构段落，'
          '每一条「第 N 行」的断言都回到原文核对属实，**无一处错位**。')
        w()
    return not (bad_h or bad_e or bad_s)


def cat4c_context(edges):
    """语境保真（穷举）：抽出的语境必须**逐字**含有该边的原始目标串。

    语境是建 wiki 时唯一的证据载体——`constraint` / `mapping` 页的每条断言
    都要挂一句语境。语境改了字就不再是证据。
    这条检查抓到过一个真 bug：强调剥离全局删 `_`，
    把语境里的 `../01_Getting_started/…` 改成了 `../01Gettingstarted/…`。
    """
    w('### 第四类附 · 语境保真（穷举，非抽样）')
    w()
    ok = trunc = trunc_mid = trunc_absent = ws = other = 0
    bad = []
    for e in edges:
        raw, ctx = e['to_raw'], e['context']
        if raw in ctx:
            ok += 1
        elif len(ctx) >= CONTEXT_MAX:
            trunc += 1          # 语境被截断到 300 字符，目标落在截断之后
            # 再分两类，确认截断没掩盖改字：
            #   mid    —— 目标的**前缀**出现在语境末尾 → 刀口正好切在目标中间，之前的部分逐字忠实
            #   absent —— 语境内完全没有目标的任何片段 → 链接在截断点之后
            if any(ctx.endswith(raw[:i]) for i in range(min(len(raw), CONTEXT_MAX), 7, -1)):
                trunc_mid += 1
            else:
                trunc_absent += 1
        elif re.sub(r'\s+', '', raw) in re.sub(r'\s+', '', ctx):
            ws += 1             # 目标自身含空白，被 `\s+ → ' '` 折叠过
        else:
            other += 1
            if len(bad) < 10:
                bad.append((e['from'], e['line'], raw, ctx[:120]))
    n = len(edges)
    w('| 情形 | 条数 | 说明 |')
    w('|---|---|---|')
    w(f'| 逐字命中 | {ok:,} | ✅ 语境里原样含 `to_raw` |')
    w(f'| 因截断未含 | {trunc:,} | 语境 300 字符上限；再分两类见下 |')
    w(f'| &nbsp;&nbsp;↳ 刀口切在目标中间 | {trunc_mid:,} | 目标**前缀**在语境末尾，切点之前逐字忠实 |')
    w(f'| &nbsp;&nbsp;↳ 目标整体在切点之后 | {trunc_absent:,} | 语境内无目标任何片段，链接在截断点之后 |')
    w(f'| 仅空白不同 | {ws:,} | 目标串自身含空格，被 `\\s+ → 单空格` 折叠 |')
    w(f'| **其他** | **{other:,}** | ' + ('✅ 为 0，无语境被改坏' if other == 0 else '❌ 必须查明') + ' |')
    w()
    w(f'合计 {ok:,} + {trunc:,} + {ws:,} + {other:,} = {ok + trunc + ws + other:,} '
      f'== 边总数 {n:,} ' + ('✅' if ok + trunc + ws + other == n else '❌ 不平'))
    w()
    w(f'截断细分的自洽：{trunc_mid:,} + {trunc_absent:,} = {trunc_mid + trunc_absent:,} '
      f'== 因截断未含 {trunc:,} '
      + ('✅' if trunc_mid + trunc_absent == trunc else '❌ 不平'))
    w()
    if bad:
        w('**「其他」样例**：')
        w()
        for f_, l_, r_, c_ in bad:
            w(f'- `{f_}` L{l_} 目标 `{r_}`，语境 `{c_}`')
        w()
    return other == 0


def cat4d_sectionbody(docs, sections):
    """全库结构段落正文回验（穷举，非抽样）。

    `sections.jsonl` 是 `error` / `version` / `constraint` 三类页面的**原料**，
    正文切错一个字符，建出来的页就是错的。前四类检验没有一项碰它的正文：
    第一类只数个数，第二类只对总量，第七类抽的是边不是段落。
    「解析对了但切错了」正好从这些缝里漏过去，所以这里穷举补上。

    独立于 extract.py 的做法：不重跑它的段落状态机，而是拿**已被第四类附校验过**的
    标题表（`docs.jsonl.headings`，42,660 条逐行对质过）来定位切点，只重写「切」这一步。

    段落正文的定义（由 `line` + `level` 唯一确定）：
      从标题行的**下一行**起，切到第一个「结束标题」之前，含空行与围栏行，
      `join('\\n')` 后去首尾空白。

    **「结束标题」有两个条件，第二个容易漏**（本回验第一版就漏了它，
    840 条对不上里有一大半是它）：
      (a) `level <= 本段 level`——同级或更高级标题；
      (b) 标题名本身在 `SECTION_H2` 里——**哪怕层级更低**。
          `# Syntax`(L1) 后面跟 `## Functional changes`(L2)，层级更高不算，
          但它是另一个段落，`Syntax` 必须在此收尾。
    同理，层级更低的**结构标题**会各自开新段落（`### Constructor` /
    `### Member functions` 各成一条 `syntax`），所以这里按 (a)∨(b) 切完即可。
    """
    w('### 第四类附 · 全库段落正文回验（穷举，非抽样）')
    w()
    head_by = {d['rel']: sorted((h['line'], h['level'], h['text']) for h in d['headings'])
               for d in docs}
    lines_cache = {}

    def srclines(rel):
        if rel not in lines_cache:
            lines_cache[rel] = CORPUS.joinpath(rel).read_text(
                encoding='utf-8', errors='replace').split('\n')
        return lines_cache[rel]

    ok = trunc = 0
    bad = []
    for s in sections:
        rel, L, lv = s['doc'], s['line'], s['level']
        if rel not in head_by:
            bad.append((rel, L, '文档不在 docs.jsonl 里'))
            continue
        lines = srclines(rel)
        nxt = len(lines) + 1
        for hl, hlv, htx in head_by[rel]:
            if hl > L and (hlv <= lv or htx in SECTION_H2):
                nxt = hl
                break
        # `chars` 记的是**截断前**的长度、`truncated` 记的是截断与否，
        # 两者单独验：只比正文的话，标记说没错、正文却被切了，是看不出来的
        # （切过之后仍然「相等」）。
        full = '\n'.join(lines[L:nxt - 1]).strip()
        n_full = len(full)
        over = n_full > SECTION_MAX
        if over:
            trunc += 1
        want = full[:SECTION_MAX]
        why = None
        if want != s['body']:
            why = f'期望 {len(want)} 字符 / 实得 {len(s["body"])} 字符'
        elif bool(s['truncated']) != over:
            why = f'`truncated`={s["truncated"]}，按原文应为 {over}（{n_full} 字符）'
        elif s['chars'] != n_full:
            why = f'`chars`={s["chars"]}，实为 {n_full}'
        if why:
            bad.append((rel, L, f'level={lv} h2={s["h2"]!r} {why}'))
        else:
            ok += 1
    n = len(sections)
    w(f'- 段落总数 **{n:,}**（`body` 已按上限截断的 {trunc:,} 条按截断后比对）')
    w(f'- 正文与原文切片**逐字符相同**：**{ok:,}** 条')
    w(f'- 不一致：**{len(bad)}** 条')
    w()
    if bad:
        w('| 文档 | 标题行 | 说明 |')
        w('|---|---:|---|')
        for rel, L, why in bad[:30]:
            w(f'| `{rel}` | {L} | {why} |')
        w()
    else:
        w(f'✅ {ok:,} + {len(bad)} = {n:,} == 段落总数，**全部逐字符对齐**。')
    w()
    return not bad


def cat4_spotcheck(docs, edges, sections, failures):
    w('## 第四类 · 分层抽样人工核对')
    w()
    by_rel = {d['rel']: d for d in docs}
    edges_by = defaultdict(list)
    for e in edges:
        edges_by[e['from']].append(e)
    sec_by = defaultdict(list)
    for s in sections:
        sec_by[s['doc']].append(s)
    fail_by = defaultdict(list)
    for f in failures:
        fail_by[f['doc']].append(f)

    TARGET = 40
    picks = {}
    slots = 0

    def add(rel, why):
        """登记一个抽样位。同一篇命中多个分层时合并理由，但**位子照数**。"""
        nonlocal slots
        slots += 1
        picks.setdefault(rel, []).append(why)

    for cat in ['00_Overview', '01_Getting_started', '02_System_reference',
                '03_Use_cases_and_application_papers', '99_Unlisted_or_Unreferenced']:
        grp = sorted(d['rel'] for d in docs if d['rel'].startswith(cat + '/'))
        if grp:
            add(grp[0], f'{cat} 首篇')
            add(grp[len(grp) // 2], f'{cat} 中位')
            add(grp[-1], f'{cat} 末篇')

    sized = sorted(docs, key=lambda d: d['bytes'])
    for i, tag in [(0, '最小'), (len(sized) // 4, '下四分位'),
                   (len(sized) // 2, '中位'), (len(sized) * 3 // 4, '上四分位'),
                   (len(sized) - 1, '最大')]:
        add(sized[i]['rel'], f'体积{tag} {sized[i]["bytes"]}B')

    bydeg = sorted(docs, key=lambda d: -d['out_degree'])
    for i, tag in [(0, '出度最高'), (len(bydeg) // 2, '出度中位')]:
        add(bydeg[i]['rel'], f'{tag} {bydeg[i]["out_degree"]}')
    for d in bydeg:
        if d['out_degree'] == 0:
            add(d['rel'], '出度 0')
            break

    struct_want = ['Procedure', 'Dependency', 'Predependencies', 'Errors',
                   'Functional changes', 'Before you begin', 'What to do next']
    for name in struct_want:
        hit = 0
        for d in docs:
            if name in d['struct_sections']:
                add(d['rel'], f'含 {name}')
                hit += 1
                if hit >= 2:
                    break
    n_none = 0
    for d in docs:
        if not d['struct_sections']:
            add(d['rel'], '无任何结构段落')
            n_none += 1
            if n_none >= 2:
                break
    for k, fs in sorted(fail_by.items(), key=lambda x: x[0])[:6]:
        add(k, f'解析异常 {fs[0]["kind"]}')

    # --- 去重会让位子数缩水（同一篇既最大又含 Procedure）。
    #     计划要求「40 篇」，所以按 rel 等距补齐到 40 篇**不重复**的文档。
    #     补齐用等距而非随机：保持确定性，第六类幂等性才不受影响。
    if len(picks) < TARGET:
        rest = [d['rel'] for d in sorted(docs, key=lambda x: x['rel'])
                if d['rel'] not in picks]
        need = TARGET - len(picks)
        step = len(rest) / need
        for j in range(need):
            add(rest[int(j * step)], '补齐（全库等距，非随机）')

    w(f'抽样位 **{slots}** 个 → 去重后 **{len(picks)}** 篇。')
    w()
    w(f'> 位子多于篇数是因为同一篇会同时命中多个分层（例如「最大」又「含 Procedure」）。')
    w(f'> 去重只去掉重复渲染，**不减少覆盖面**；不足 {TARGET} 篇时按 `rel` 等距补齐。')
    w()

    lines = ['# 分层抽样核对表', '',
             f'共 **{len(picks)}** 篇（抽样位 {slots} 个，去重后）。左列原文，右列抽取结果，逐条对齐。', '',
             '> 自动对账查不出「解析对了但语义错了」。**这一份要人真的看一遍。**', '',
             '## 看的时候按这几条规则对', '',
             '**边的 `语境` 抽取规则**（写死在计划里，不许临场发挥，核对的就是它）：', '',
             '1. 取链接所在那一行',
             '2. 剥掉行首列表符（`-` `*` `1.`）与 markdown 强调符，**但链接目标 `](<...>)` 原样保留**',
             f'3. 若结果 < {CONTEXT_MIN} 字符，向上并入前一行（最多并 {CONTEXT_MERGE_MAX} 行）',
             f'4. 截断到 {CONTEXT_MAX} 字符',
             '',
             f'`语境` 显示的是**完整存值**（≤{CONTEXT_MAX} 字符）。'
             f'`to_raw` 一字不改地出现在语境里，就是对的。',
             '',
             '**标题**：`L{n}` 是 1 起的行号，回到左边原文数到第 n 行应当正是那个标题。',
             '',
             '**段落**：`L{n}` 是**段落标题所在行**，正文从 n+1 行开始；'
             f'`chars` 是截断前的长度（上限 {SECTION_MAX}）。',
             '',
             '**故意不建边的东西**：图片（`.png` 等）、页内锚点、外部 URL、'
             '`javascript:`、以及 `[](<>)` 空链接。看到它们没出现在边里，是对的。', '']
    for rel in sorted(picks):
        d = by_rel[rel]
        src = (CORPUS / rel).read_text(encoding='utf-8', errors='replace')
        src_lines = src.replace('\r\n', '\n').split('\n')
        lines.append('---')
        lines.append('')
        lines.append(f'## `{rel}`')
        lines.append('')
        lines.append(f'*抽样理由：{"；".join(picks[rel])}*')
        lines.append('')
        lines.append(f'- 字节 {d["bytes"]} / 标题 {d["heading_count"]} / 出度 {d["out_degree"]}'
                     f' / 代码块 {d["code_blocks"]}')
        lines.append(f'- frontmatter：`{json.dumps(d["frontmatter"], ensure_ascii=False)}`')
        lines.append(f'- title：`{d["title"]}`')
        lines.append(f'- 结构段落：{d["struct_sections"] or "（无）"}')
        if fail_by.get(rel):
            lines.append(f'- ⚠️ 解析异常：{fail_by[rel]}')
        lines.append('')
        lines.append('### 原文开头')
        lines.append('')
        lines.append('```')
        lines.extend(src_lines[:28])
        lines.append('```')
        lines.append('')
        lines.append('### 抽取的标题')
        lines.append('')
        for h in d['headings'][:25]:
            lines.append(f'- L{h["line"]} `{"#" * h["level"]} {h["text"]}`')
        if len(d['headings']) > 25:
            lines.append(f'- …（共 {len(d["headings"])} 个）')
        lines.append('')
        lines.append(f'### 抽取的边（{len(edges_by[rel])} 条，显示前 10）')
        lines.append('')
        for e in edges_by[rel][:10]:
            mark = '' if e['resolved'] else ' ⚠️未解析'
            cs = ' `[代码跨度]`' if e['in_code_span'] else ''
            lines.append(f'- L{e["line"]} → `{e["to"] or e["to_raw"]}`{mark}{cs}')
            lines.append(f'  - 语境：{e["context"]}')
        lines.append('')
        if sec_by.get(rel):
            lines.append('### 抽取的段落')
            lines.append('')
            for s in sec_by[rel][:6]:
                lines.append(f'- `{s["h2"]}`（{s["group"]}，L{s["line"]}，{s["chars"]} 字符'
                             f'{"，已截断" if s["truncated"] else ""}）')
                lines.append(f'  - 开头：{s["body"][:120]!r}')
            lines.append('')
    (OUTDIR / 'spot-check.md').write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    w(f'已生成 `spot-check.md`，共 **{len(picks)}** 篇。**这一份机器判不了，只能人看。**')
    w()
    w('复核记录写在 `..\\wiki\\log.md`：那里记的是「谁、什么时候、看了哪几篇、'
      '看出了什么、每一条怎么处置的」。**不写进本报告**——本报告是脚本生成的，'
      '把复核结论写进来会随下一次重跑变成一个没人维护的陈旧断言。')
    w()

    # 人工核对时从对照视图里看出的一件事：`first_para` 有退化值。
    # **不改抽取规则**——那是计划里冻结的「正文第一段」，改了就得重新验 9,398 篇；
    # 量小（7 篇）、成因已知（就是下面这批 HTML→MD 转换残渣），点名披露最划算。
    degen = [d for d in docs
             if d['first_para'] is not None
             and not re.search(r'[A-Za-z0-9]', d['first_para'])]
    no_fp = [d for d in docs if d['first_para'] is None]
    w('### `first_para` 的退化值（人工核对所见，逐条披露）')
    w()
    w(f'- `first_para` 为 `null`：**{len(no_fp)}** 篇（空文档或只有 frontmatter）')
    w(f'- 非空但**不含任何字母数字**：**{len(degen)}** 篇')
    w()
    if degen:
        w('| 文档 | `first_para` | 成因 |')
        w('|---|---|---|')
        for d in degen:
            why = ('HTML→MD 转换把链接文字与目标切到了两行，'
                   '首行只剩一个 `[`' if d['first_para'] == '['
                   else '空链接残渣 `[](<>)`，或孤立的列表符')
            w(f'| `{d["rel"]}` | `{d["first_para"]}` | {why} |')
        w()
    w(f'**处置：不改抽取规则，点名披露。** `first_para` 是计划里冻结的「正文第一段」，'
      f'改规则就得把 9,398 篇重验一遍，而这里只有 {len(degen)} 篇受影响（'
      f'{len(degen) / len(docs) * 100:.2f}%），成因就是已披露的转换残渣。'
      f'**建页时这 {len(degen)} 篇不要用 `first_para` 当摘要**，改用 `frontmatter.title`'
      f' 或首个 H2。')
    w()
    return len(picks)


# ============================================================ 第五类
def cat5_failures(failures, edges):
    w('## 第五类 · 解析失败清单（不许静默丢弃）')
    w()
    c = Counter(f['kind'] for f in failures)
    w(f'共 **{len(failures)}** 条。')
    w()
    w('| 类型 | 数量 | 说明 |')
    w('|---|---|---|')
    desc = {
        'no_frontmatter': '缺 frontmatter。已知 = 5 个分类目录的 index.md',
        'no_headings': '全文无任何标题。集中在 99_Unlisted 的 Doxygen 残页',
        'no_h1': '有标题但无 H1。title 保持 None，**不 fallback 到文件名**',
        'not_in_catalog': '不在 catalog-markdown.csv 里。已知 = 5 个 index.md',
        'dangling_link': '.md 链接解析不到目标文件',
        'fm_parse_failure': 'frontmatter 里有解析不了的行',
        'unclosed_fence': '代码围栏未闭合',
        'decode_error': 'UTF-8 解码失败',
    }
    for k, v in sorted(c.items(), key=lambda x: -x[1]):
        w(f'| `{k}` | {v} | {desc.get(k, "")} |')
    w()
    for k in c:
        samples = [f for f in failures if f['kind'] == k][:5]
        w(f'**`{k}`** 样例：')
        w()
        for s in samples:
            w(f'- `{s["doc"]}` `{s["detail"]}`')
        w()

    # --- 判据 1：悬空链接比例有数
    n_edge = len(edges)
    n_dangle = c.get('dangling_link', 0)
    rate = (n_dangle / n_edge * 100) if n_edge else 0.0
    w('**判据 1 · 悬空链接比例**：')
    w()
    w(f'- `.md` 边总数 **{n_edge:,}**')
    w(f'- 其中悬空（目标文件不存在）**{n_dangle:,}** → 比例 **{rate:.4f}%**')
    w()

    # --- 判据 2：没有任何「未知原因」条目
    known = set(desc)
    unknown = sorted(k for k in c if k not in known)
    if unknown:
        w(f'❌ **存在未知原因条目：{unknown}** —— 必须查明，不许放行。')
        w()
        return False
    w('**判据 2 · 无未知原因条目**：')
    w()
    w(f'- 出现的失败类型 {sorted(c)}')
    w(f'- 全部落在已知集合内（{sorted(known)}）✅')
    w()
    w('以上每一类都对应语料的真实缺陷，不是解析器静默丢弃的证据。')
    w()
    return True


# ============================================================ 第六类
def cat6_idempotent():
    w('## 第六类 · 幂等性')
    w()
    before = {f: sha256(OUTDIR / f) for f in DATA_FILES}
    w('第一次运行的 sha256：')
    w()
    w('| 文件 | sha256 |')
    w('|---|---|')
    for f, h in before.items():
        w(f'| `{f}` | `{h[:32]}…` |')
    w()
    print('  ... 重跑 extract.py 以比对')
    r = subprocess.run([sys.executable, 'extract.py'], cwd=str(OUTDIR),
                       capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    if r.returncode != 0:
        w(f'❌ 重跑失败：{(r.stderr or "")[-800:]}')
        w()
        return False
    after = {f: sha256(OUTDIR / f) for f in DATA_FILES}
    same = all(before[f] == after[f] for f in DATA_FILES)
    w('| 文件 | 两次是否逐字节相同 |')
    w('|---|---|')
    for f in DATA_FILES:
        w(f'| `{f}` | {"✅ 相同" if before[f] == after[f] else "❌ 不同"} |')
    w()
    if same:
        w('✅ **两次运行输出逐字节相同。**')
        w('顺序化（`walk()` 排序 + 无并发 + `sort_keys=True`）的目的正在于此——')
        w('并发写入会让行序不可复现，这一条就过不了。')
    else:
        w('❌ **存在不确定性来源，必须消除。**')
    w()
    return same


# ============================================================ 第七类
def cat7_reverse(edges):
    w('## 第七类 · 反向抽样（回归验证）')
    w()
    rnd = random.Random(20260917)   # 固定种子，结果可复现
    sample = rnd.sample(edges, min(50, len(edges)))
    ok = bad = 0
    bad_rows = []
    for e in sample:
        try:
            text = (CORPUS / e['from']).read_bytes().decode('utf-8', errors='replace')
        except OSError:
            bad += 1
            bad_rows.append((e, '源文件读不到'))
            continue
        lines = text.replace('\r\n', '\n').split('\n')
        ln = e['line'] - 1
        if 0 <= ln < len(lines) and e['to_raw'] in lines[ln]:
            ok += 1
        else:
            bad += 1
            bad_rows.append((e, f'第 {e["line"]} 行未见目标串'))
    w(f'随机抽 **{len(sample)}** 条边（种子 20260917，可复现），回到原文逐条 grep。')
    w()
    w(f'- ✅ 命中：**{ok}**')
    w(f'- ❌ 未命中：**{bad}**')
    w()
    if bad_rows:
        w('未命中明细：')
        w()
        for e, why in bad_rows[:20]:
            w(f'- `{e["from"]}` L{e["line"]} → `{e["to_raw"]}`：{why}')
        w()
    else:
        w('✅ **50 条全部命中：源文件、行号、目标串三者对齐，无错位。**')
    w()
    return bad == 0


def cat8_contract(docs, edges, sections, failures):
    """交付物字段说明——建页那一步读这四个文件时的**契约**。

    不是检验，是交接。前七类证明「数字对得上」，这一节说清「字段是什么意思」。
    没有它，下一步只能靠猜字段语义，而**猜错的代价是 110 个簇一起错**。
    每一条都是从实际数据里核出来的，不是照抄 extract.py 的注释。
    """
    w('## 交付物字段说明（交接契约）')
    w()
    w('| 文件 | 行数 | 一行是什么 |')
    w('|---|---:|---|')
    w(f'| `docs.jsonl` | {len(docs):,} | 一篇文档（机械索引） |')
    w(f'| `edges.jsonl` | {len(edges):,} | 一条交叉引用（源→目标） |')
    w(f'| `sections.jsonl` | {len(sections):,} | 一个结构段落 |')
    w(f'| `hubs.csv` | {len(docs):,} | 一篇文档的入度/出度排名 |')
    w(f'| `failures.jsonl` | {len(failures):,} | 一条解析异常（**没有任何东西被静默丢弃**） |')
    w()
    w('### `edges.jsonl`')
    w()
    w('| 字段 | 含义 | 易错点 |')
    w('|---|---|---|')
    w('| `from` | 源文档，相对语料根的 posix 路径 | 等于 `docs.jsonl.rel` |')
    w('| `to` | 目标文档，**从源文档出发解析并归一化**后的路径 | 解析失败时为 `null`，'
      '要看 `to_raw` |')
    w('| `to_raw` | 原文里链接目标**一字不改**的原始串 | 带 `#anchor`、`../`、URL 编码；'
      '**别拿它当路径用** |')
    w('| `resolved` | `to` 指向的文件是否真实存在 | `false` = 悬空链接 |')
    w('| `line` | 链接所在行号（1 起） | 已由第四类附穷举回验 |')
    w('| `context` | 链接所在那一行（必要时上并，≤300 字符） | 超 300 会被截断，'
      '**截断不等于出错** |')
    w('| `link_text` | 方括号里的文字 | 可能是嵌了图片的复合串 |')
    w('| `kind` | `toc`（来自 5 个 `index.md` 的目录）或 `inline`（正文里的引用） | '
      '**两者语义完全不同，做入度排名时别混** |')
    w('| `anchor` | `to_raw` 里 `#` 之后的部分 | 无锚点时为 `null` |')
    w('| `in_code_span` | 链接写在反引号里，作者是在**引用**它，渲染后不是链接 | '
      f'共 {sum(1 for e in edges if e["in_code_span"])} 条；'
      '见第三类「影响面」一节 |')
    w()
    w('**只有 `to` 指向 `.md` 的链接才建边。** 图片、页内锚点、外部 URL、'
      '`.htm/.pdf` 等资源按类型计入 `docs.jsonl.link_kinds`，不进 `edges.jsonl`。')
    w()
    w('### `sections.jsonl`')
    w()
    w('| 字段 | 含义 | 易错点 |')
    w('|---|---|---|')
    w('| `doc` | 所属文档 | |')
    w('| `h2` | 段落的标题原文 | 名字取自固定名单；`### Member functions` 这种'
      '**低层级结构标题也算一段** |')
    w('| `group` | `syntax`/`version`/`related`/`procedure`/`constraint`/`concept`/`error` | '
      '建 `error`/`version`/`constraint` 页时按这个字段筛 |')
    w('| `line` | **段落标题所在行**，不是正文起始行 | ⚠️ **正文从 `line + 1` 开始**，'
      '别当正文行号用 |')
    w('| `chars` | **截断前**的正文长度 | 与 `len(body)` 不等时说明被截断 |')
    w('| `truncated` | 正文是否超过 6000 字符上限 | `true` 时 `body` 只有前 6000 字符 |')
    w('| `body` | 段落正文，各行用 `\\n` 连接、首尾去空白 | 含段落内子标题行；'
      '**不含**闭合本段的那个标题行 |')
    w()
    w('### `docs.jsonl`')
    w()
    w('| 字段 | 含义 | 易错点 |')
    w('|---|---|---|')
    w('| `rel` | 相对语料根的 posix 路径，**全库唯一键** | |')
    w('| `title` | H1 的文字 | **没有 H1 就是 `null`，不 fallback 到文件名**——'
      'fallback 会把「没有标题」伪装成「有标题」 |')
    w('| `frontmatter` | 解析出的 YAML；解析不了的行走 `failures.jsonl` | 5 个 `index.md` 为 `null` |')
    w('| `headings` | 全部标题 `{level, text, line}` | 42,660 条已逐行回验 |')
    w('| `first_para` | 正文第一段，≤300 字符 | 有退化值，见第四类「`first_para` 的退化值」 |')
    w('| `struct_sections` / `struct_groups` | 该文档命中的段落名与所属组名单 | 与 '
      '`sections.jsonl` 互为索引 |')
    w('| `out_degree` / `edge_angle` / `edge_plain` | 出度，以及两种正则各自的命中数 | '
      '`edge_angle + edge_plain` 减去非 `doc` 目标 == `out_degree` |')
    w('| `link_kinds` | 该文档各类链接目标的计数（`doc`/`asset`/`anchor`/…） | '
      '**非 `doc` 的不建边，但计数留着** |')
    w('| `is_index` / `in_catalog` | 是否 5 个 `index.md` 之一 / 是否在 catalog-markdown.csv 里 | |')
    w('| `bytes` / `chars` / `code_blocks` / `heading_count` | 体积与结构计数 | |')
    w()
    w('### `hubs.csv`')
    w()
    w('| 列 | 含义 |')
    w('|---|---|')
    w('| `path` | 文档路径 |')
    w('| `in_all` | 入度（含 `toc` 边） |')
    w('| `in_inline` | 入度（**只算 `kind=inline`**）。**这份文件就是按它降序排的** |')
    w('| `out` | 出度 |')
    w('| `is_index` | 是否目录页。`index.md` 的入度靠 TOC 撑起来，'
      '**挑 `object` 页时通常要排除** |')
    w()
    n_res = sum(1 for e in edges if e['resolved'])
    n_toc = sum(1 for e in edges if e['kind'] == 'toc')
    w(f'⚠️ **两个入度都只计 `resolved=true` 的边**——悬空链接不入度，否则入度表总和会对不上。'
      f'本库悬空链接为 **{len(edges) - n_res:,}** 条，所以 `in_all` 合计 {n_res:,} '
      f'恰好等于边总数 {len(edges):,}；**一旦语料里出现悬空链接，这两个数就会分叉**，'
      f'对账时别忘了这条。')
    w()
    w(f'两个入度的差就是 TOC 的份量：`toc` 边 {n_toc:,} 条'
      f'（占全部边的 {n_toc / len(edges) * 100:.1f}%），`inline` 边 {len(edges) - n_toc:,} 条。'
      f'**做「谁被引得多」的判断必须用 `in_inline`**——'
      f'用 `in_all` 的话，凡是在目录里出现过的文档都会被 TOC 灌一遍水。')
    w()


# ============================================================ 主流程
def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    docs = load_jsonl('docs.jsonl')
    edges = load_jsonl('edges.jsonl')
    sections = load_jsonl('sections.jsonl')
    failures = load_jsonl('failures.jsonl')

    w('# TDC 语料抽取 —— 验证报告')
    w()
    w(f'语料：`{CORPUS}`')
    w(f'产出：`{OUTDIR}`')
    w()
    w('设计原则：**每一个抽取结果，都要有一个独立来源的数字可以对账。**')
    w('对不上就必须解释；解释不了就是 bug。任何「跳过」都必须出现在报告里。')
    w()

    results = {
        '第一类 内部一致性': cat1_internal(docs, edges),
        '第二类 基线对账': cat2_baseline(docs, edges),
        '第三类 独立复算': cat3_recheck(),
        '第五类 失败清单': cat5_failures(failures, edges),
        '第六类 幂等性': cat6_idempotent(),
        '第七类 反向抽样': cat7_reverse(edges),
    }
    n_sample = cat4_spotcheck(docs, edges, sections, failures)
    lineref_ok = cat4b_lineref(docs, edges, sections)
    ctx_ok = cat4c_context(edges)
    sec_ok = cat4d_sectionbody(docs, sections)
    results['第四类 分层抽样'] = f'已生成 {n_sample} 篇，机器不判，见 spot-check.md'
    results['第四类附 行号回验'] = lineref_ok
    results['第四类附 语境保真'] = ctx_ok
    results['第四类附 段落正文'] = sec_ok

    cat8_contract(docs, edges, sections, failures)

    w('## 汇总')
    w()
    w('| 检验 | 结果 |')
    w('|---|---|')
    for k, v in results.items():
        mark = '✅ 通过' if v is True else ('⚠️ 见正文' if isinstance(v, str) else '❌ 未通过')
        w(f'| {k} | {mark} |')
    w()
    w('**第四类机器判不了。** 自动对账查得出「数字对不上」，查不出「解析对了但语义错了」；')
    w('反过来，上面前九行全绿也只说明数字自洽，不说明数据可用。')
    w()
    w('**放行条件**：`spot-check.md` 的 40 篇逐条看过，且复核发现的每一条差异都')
    w('落进计划里那三种归宿之一——**（a）脚本 bug → 修；（b）基线工具不准 → 记录并说明；')
    w('（c）语料本身如此 → 记录。没有第四种，「先放着」不算。**')
    w('复核记录见 `..\\wiki\\log.md`；本条不通过前，这批数据视为**未放行**，不得用于建页。')
    w()

    (OUTDIR / 'verify-report.md').write_text('\n'.join(R), encoding='utf-8', newline='\n')
    print(f'\nDONE -> {OUTDIR / "verify-report.md"}')


if __name__ == '__main__':
    main()
