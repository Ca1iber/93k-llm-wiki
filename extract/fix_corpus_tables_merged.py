#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""语料修复：**带合并格的表被压平**（A5 的同族，上一批整张跳过的那些）。

用法：
    python -X utf8 extract/fix_corpus_tables_merged.py                # 空跑
    python -X utf8 extract/fix_corpus_tables_merged.py --limit 15     # 试点（不写产物）
    python -X utf8 extract/fix_corpus_tables_merged.py --apply        # 真改
    python -X utf8 extract/fix_corpus_tables_merged.py --verify-only  # 只跑逐字节重放

## 与上一批（`fix_corpus_tables.py`）的唯一区别

上一批遇到上游带 `colspan`/`rowspan` 的表**整张跳过**，因为 markdown 表格表达不了合并格。
这一批专门处理它们。

**判据完全不变，而且更强的那一半原封不动**：
md 里**每一行的格子数与上游 HTML 逐行一一对应**（合并格那几行本来就少一格），
所以「逐格核对」照旧 —— 解析出来的格子，逐行逐格必须与上游的格子一致，
**对不上就整张不动**。变的只有两处：

1. **不再要求「每行列数相同」**（那正是合并格的签名），改成按**每行各自的格子数**切；
   token 数 `P = Σ(每行格子数) + 行数`。
2. **生成时要把「展开」写出来**：上游一格跨了 N 行/列，要写成 N 个相同的格子。

## 为什么用「重复」而不是别的（三条别的路都量过）

- **原生 `<table>`**：语料会出现**第二种链接写法**（`<a href>`）——
  而 `extract.py` 只认 markdown 形式（`RE_ANGLE` / `RE_PLAIN`），**边会丢**；
  且 HTML 块里的 markdown 不被解析，链接只能写成 HTML。语料现状是
  **52,135 个 markdown 链接 / 0 个 HTML 链接**，不能开这个口子。
- **框线图**（代码块里画）：结构**活在空白对齐里**，任何重排静默错位；
  列宽 = 整列最大值，改一格可能重画整张；围栏里的链接不渲染成链接。
- **重复法**：链接一个字不动、结构显式（`|` 定界）不会坏。
  代价是**重复出来的格子**：实测平均 **25%**（最坏 68%）。
  所以**重复格占比 > 45% 的整张挂账**（`MAX_DUP_RATIO`），不让噪声失控。

## 转录说明（**本工程第一次让修复器往语料里写自己的话**）

每张展开过的表下面加一句**固定措辞**的说明。它**只描述做过什么 + 指出真结构在哪**，
**不宣称一条能反推结构的规矩** —— 因为「相邻相同 = 合并格」实测会误判：
已修的 3,642 张**不含**合并格的表里，**594 张（16%）**本来就有相邻相同的格子
（如计划文档里那张 `operating / operating`）。**误差率已知 16% 的判据不许出厂。**

## 边界规则

| 情况 | 处置 |
|---|---|
| 重复格占比 > 45% | **整张不动**并计数（噪声封顶） |
| 格子净内容 < 4 字符 | 整张不动（判据太弱，会到处误撞 —— 同 A5） |
| 区域「无界」（前后 token 只隔一层换行） | 整张不动 —— **这条是安全阀，实测不能放宽**（见 `PLAN-未修清单.md` A6） |
| 格内有代码围栏 | 整张不动 |
| 同一张表在一篇里对上 ≥2 处 | 整张不动（分不清重复投放还是撞上） |
| 上游 `.htm` 不在 / 文档含行首竖线（另一来源） | 整篇跳过 |

## 换行规矩

一律 `read_bytes()` / `write_bytes()`；改完跑 `--verify-only` 逐字节重放。
**注意本仓 `core.autocrlf=true`**（git 存 LF、工作区 CRLF），重放前必须对齐换行。
"""
import collections
import hashlib
import json
import pathlib
import sys

sys.path.insert(0, r'F:\master-dev\understand-anything-wiki\extract')
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import fix_corpus_tables as F          # ★ 共享：解析、规范化、判据、重放验证

WIKI = F.WIKI
CORPUS = F.CORPUS
MD = F.MD
RAW = F.RAW
EVID = WIKI / 'extract' / 'findings-corpus-tables-merged-evidence.md'
ASSIGN = WIKI / 'extract' / '_assign_tables_merged.json'

APPLY = '--apply' in sys.argv
LIMIT = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else None
MAX_DUP_RATIO = 0.45          # 重复格占比上限；超过就整张挂账


def note_for(topic, nl):
    """**固定措辞**的转录说明。只描述做过什么 + 指出真结构在哪，不宣称可反推的规矩。

    ★ 行尾用**文件自己的** `nl`（本仓 CRLF）—— 写死 `\\n` 会往 CRLF 文件里注入裸 LF。"""
    return ("> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；" + nl +
            "> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。"
            f"真结构见 `tdc-html/raw/{topic}.htm`。")


# ------------------------------------------------------------------ 排布与展开

def lay_out(rows):
    """把 HTML 的行（每格带 colspan/rowspan）排成矩形网格。

    返回 `(R, C, cover, placed)`：
    - `cover[r][c]` = 覆盖该位置的格子的**序号 k**（按行优先，与 md 切出来的格子一一对应）
    - `placed` = 实际存在的格子数（算重复格占比用：`R*C - placed`）

    ★ **只给序号，不给文字** —— 展开时要用 **md 原文的格子**（`cells[k]`）填，
    不能用上游解析出来的文字：上游那侧图片被折成了 `\\x00alt\\x00` 标记，
    直接填会把 NUL 写进语料，而且会丢掉链接的原文形式。"""
    occupied, placed = {}, []
    for r, row in enumerate(rows):
        c = 0
        for cell in row:
            while (r, c) in occupied:
                c += 1
            for dr in range(cell['rowspan']):
                for dc in range(cell['colspan']):
                    occupied[(r + dr, c + dc)] = len(placed)
            placed.append((r, c, cell))
            c += cell['colspan']
    R = len(rows)
    C = max((c for _, c, _ in placed), default=-1) + 1
    cover = [[None] * C for _ in range(R)]
    for r, c, cell in placed:
        for dr in range(cell['rowspan']):
            for dc in range(cell['colspan']):
                if r + dr < R and c + dc < C:
                    cover[r + dr][c + dc] = occupied[(r, c)]
    return R, C, cover, len(placed)


def expand_from_md(cover, cells, R, C):
    """展开网格：**用 md 原文的格子**填（`cells` 与 `cover` 的序号一一对应）。

    `cover[r][c] is None` = 上游那一行**没有占到这一列**（行不满宽）。
    markdown 要求每行列数一致，只能补空格 —— 空位在渲染上是**可见**的，
    所以不需要在转录说明里交代（见 `holes`）。"""
    return [[cells[cover[r][c]] if cover[r][c] is not None else '' for c in range(C)]
            for r in range(R)]


def match_merged(text, allt, bol_idx, eol_idx, rows, blocked=None):
    """返回 (候选列表, 跳过原因)。候选 = (start, end, cells, flat_up, R, C, expanded, placed)。

    ★ `blocked` 传一个 list 时，被规则挡下的那次**也把区域交出来**（见 `F.match_table`）。"""
    n_i = [len(r) for r in rows]
    R = len(rows)
    P = sum(n_i) + R                       # ★ 每行各自的格子数 + 换行竖线
    flat_up = [F.norm_up(''.join(c['txt'])) for r in rows for c in r]
    Rg, Cg, cover, placed = lay_out(rows)
    cands, fitted = [], False
    for i in bol_idx:
        r = F.parse_region(text, allt, eol_idx, i, P)
        if not r:
            continue
        chunks, start, end = r
        if chunks[0].strip() or chunks[-1].strip():
            continue
        cells, idx, ok = [], 1, True
        for ri in range(R):
            for _ in range(n_i[ri]):
                cells.append(chunks[idx]); idx += 1
            if ri < R - 1:
                if chunks[idx].strip():
                    ok = False
                    break
                idx += 1
        if not ok:
            continue
        fitted = True
        if [F.norm_md(c) for c in cells] != flat_up:
            continue
        expanded = expand_from_md(cover, cells, Rg, Cg)      # ★ 用 md 原文展开
        cand1 = (start, end, cells, flat_up, Rg, Cg, expanded, placed)
        if any('```' in c for c in cells):
            if blocked is not None:
                blocked.append(cand1)
                return blocked, '格内有代码围栏'
            return [], '格内有代码围栏'
        if sum(len(F.norm_md(c)) for c in cells) < F.MIN_CONTENT:
            if blocked is not None:
                blocked.append(cand1)
                return blocked, '内容近于空'
            return [], '内容近于空'
        if Rg * Cg and (Rg * Cg - placed) / (Rg * Cg) > MAX_DUP_RATIO:
            if blocked is not None:
                blocked.append(cand1)
                return blocked, f'重复格占比 >{MAX_DUP_RATIO:.0%}'
            return [], f'重复格占比 >{MAX_DUP_RATIO:.0%}'
        cands.append((start, end, cells, flat_up, Rg, Cg, expanded, placed))
    if cands:
        return cands, None
    return [], ('网格不等' if fitted else '窗口放不下')


def split_row(ln):
    """按未转义的 `|` 切一行（**不用正则**，免得反斜杠在 shell 里被吃）。"""
    ln = ln.strip()
    if ln.startswith('|'):
        ln = ln[1:]
    if ln.endswith('|'):
        ln = ln[:-1]
    parts, cur, i = [], [], 0
    while i < len(ln):
        # ★ 只有 `\|` 算转义（那是我们自己加的）；**别的反斜杠是原文内容，要留着**
        #   —— 格子里有原文自带的字面量，如 `is '\x00' with`。
        if ln[i] == '\\' and i + 1 < len(ln) and ln[i + 1] == '|':
            cur.append('|'); i += 2; continue
        if ln[i] == '|':
            parts.append(''.join(cur)); cur = []; i += 1; continue
        cur.append(ln[i]); i += 1
    parts.append(''.join(cur))
    return [x.strip() for x in parts]


def self_check(tbl, expanded, R, C, nl, name):
    """★ 把生成的新表**再解析一遍**，必须还原出上游的**展开网格**。

    这一道抓「转义 / `<br>` / 行列编排」写错，独立于上面那次逐格核对。"""
    lines = [l for l in tbl.split(nl) if l.startswith('|') and not l.startswith('|---')]
    assert len(lines) == R, f'{name}: 新表行数 {len(lines)} ≠ {R}'
    for r, ln in enumerate(lines):
        got = split_row(ln)
        assert len(got) == C, f'{name}: 第 {r} 行列数 {len(got)} ≠ {C}'
        for c in range(C):
            back = F.norm_md(got[c].replace('<br>', '\n'))
            want = F.norm_md(expanded[r][c])
            if back != want:
                k = 0
                while k < min(len(back), len(want)) and back[k] == want[k]:
                    k += 1
                raise AssertionError(
                    f'{name}: 第 {r} 行第 {c} 格回解不回上游（第一个不同在 {k}）\n'
                    f'  原文格子={expanded[r][c][:200]!r}\n'
                    f'  回解    ={back[max(0, k - 40):k + 60]!r}\n'
                    f'  上游    ={want[max(0, k - 40):k + 60]!r}')


def render(expanded, R, C, nl, topic):
    out = []
    for ri in range(R):
        out.append('| ' + ' | '.join(F.clean_cell(c) for c in expanded[ri]) + ' |')
        if ri == 0:
            out.append('|' + '---|' * C)
    out.append('')
    out.append(note_for(topic, nl))
    return nl.join(out)


# --------------------------------------------------------------------------- 主流程

def main():
    if '--verify-only' in sys.argv:
        return verify_only()

    docs = []
    for p in sorted(MD.rglob('*.md')):
        t = p.read_bytes().decode('utf-8', 'replace')
        if sum(1 for l in t.splitlines() if F.LONE.fullmatch(l)) >= 2:
            docs.append(p)
    print(f'候选文档（孤立竖线 ≥2 行）：{len(docs):,} 篇')
    if LIMIT:
        docs = docs[:LIMIT]
        print(f'--limit {LIMIT} → 只跑前 {len(docs)} 篇')

    stat, tbl_stat = {}, {}
    accepted = []

    def bump(d, k, n=1):
        d[k] = d.get(k, 0) + n

    for p in docs:
        text = p.read_bytes().decode('utf-8', 'replace')
        nl = '\r\n' if '\r\n' in text else '\n'
        allt, bol, eol, col0 = F.md_tokens(text)
        if col0:
            bump(stat, '含行首竖线（另一来源的表格）')
            continue
        m = F.SOURCE_TOPIC.search(text)
        if not m:
            bump(stat, '无 source_topic')
            continue
        topic = m.group(1).replace('.htm', '')
        ups, why = F.upstream_tables(topic)
        if ups is None:
            bump(stat, why)
            continue
        merged = [u for u in ups if u['skip'] == '合并格']
        if not merged:
            bump(stat, '本族无可修（没有合并格表）')
            continue

        by = {}
        for ui, u in enumerate(merged):
            mine, reason = match_merged(text, allt, bol, eol, u['rows'])
            by[ui] = mine
            if reason:
                bump(tbl_stat, reason)
        picked = []
        for ui, lst in sorted(by.items()):
            lst = sorted(lst, key=lambda c: -(c[1] - c[0]))
            keep, spans = [], []
            for c in lst:
                if any(not (c[1] <= s or c[0] >= e) for s, e in spans):
                    continue
                spans.append((c[0], c[1]))
                keep.append((ui,) + c)
            if len(keep) == 1:
                picked.append(keep[0])
            elif keep:
                bump(tbl_stat, '同表多处命中（分不清 → 整张不动）')
        if not picked:
            bump(stat, '无表对上')
            continue
        picked.sort(key=lambda c: -(c[2] - c[1]))
        chosen, spans = [], []
        for c in picked:
            if any(not (c[2] <= s or c[1] >= e) for s, e in spans):
                bump(tbl_stat, '同一段被两个上游表抢（弃一）')
                continue
            spans.append((c[1], c[2]))
            chosen.append(c)
        chosen.sort(key=lambda c: c[1])
        bump(stat, '有表对上')

        for ui, start, end, cells, flat_up, Rg, Cg, expanded, placed in chosen:
            a = text.rfind('\n', 0, start) + 1
            tbl = render(expanded, Rg, Cg, nl, topic)
            assert '\x00' not in tbl, f'{p.name}: 新表里有 NUL（上游解析的标记漏进来了）'
            assert '\n' not in tbl.replace(nl, ''), f'{p.name}: 新表里混进了裸 LF'
            self_check(tbl, expanded, Rg, Cg, nl, p.name)
            e = end
            while e < len(text) and text[e] in ' \t':
                e += 1
            tail = (nl + nl) if (e < len(text) and text[e] not in '\r\n') else ''
            accepted.append(dict(path=p, topic=topic, tbl=ui, R=Rg, C=Cg, placed=placed,
                                 table=tbl, orig=text[a:e], a=a, e=e, tail=tail))

    n_tbl = len(accepted)
    n_doc = len({x['path'] for x in accepted})
    print(f'\n✅ 可修 **{n_tbl:,} 张**，涉及 **{n_doc:,} 篇**')
    print('\n跳过（按类，**不许静默跳过**）：')
    for k, v in sorted(stat.items(), key=lambda kv: -kv[1]):
        print(f'   {k:<30} {v:,} 篇')
    print('表侧：')
    for k, v in sorted(tbl_stat.items(), key=lambda kv: -kv[1]):
        print(f'   {k:<30} {v:,} 张')

    if LIMIT:
        print('\n[试点 --limit] 不写证据表 / 清单。')
        for x in accepted[:8]:
            print('=' * 74)
            print(f"{x['path'].relative_to(MD).as_posix()}   ← raw/{x['topic']}.htm 表#{x['tbl']}"
                  f"   {x['R']}×{x['C']}（真格 {x['placed']}）")
            for line in x['table'].split('\r\n'):
                print('  ' + line[:150])
        return

    if not F.guard(EVID, n_tbl, '证据表') or not F.guard(ASSIGN, n_tbl, '清单'):
        print('   （什么都没写，语料也没动。）')
        sys.exit(2)

    esc = lambda s: s.replace('\\', '\\\\').replace('|', '\\|').replace('\r\n', '⏎')
    with EVID.open('w', encoding='utf-8', newline='\n') as fh:
        fh.write('# 语料表格修复证据表 —— **带合并格的表**（A5 同族，上一批跳过的）\n\n')
        fh.write(f'写于 2026-10-08。共 **{n_tbl:,}** 张 / **{n_doc:,}** 篇。\n\n')
        fh.write('**每张都逐格核对过**：md 的**每一行格子数与上游 HTML 逐行一一对应**，'
                 '解析出来的格子必须与上游一致，对不上整张不动。\n\n')
        fh.write('**展开是「重复」**：上游一格跨 N 行/列 → 写成 N 个相同格子。'
                 '实测平均 25% 的格子是重复出来的；**占比 >45% 的整张挂账**。\n\n')
        fh.write('**只改 `agent-markdown/`，上游 `raw/*.htm` 一个字节不动。**\n\n')
        fh.write('| # | markdown | 上游 | 表 | 展开后 | 真格 | 重复 | 新表 |\n')
        fh.write('|---|---|---|---|---|---|---|---|\n')
        for n, x in enumerate(accepted, 1):
            rel = x['path'].relative_to(MD).as_posix()
            tot = x['R'] * x['C']
            fh.write(f"| {n} | `{rel}` | `{x['topic']}.htm` | #{x['tbl']} | "
                     f"{x['R']}×{x['C']} | {x['placed']} | {tot - x['placed']} | "
                     f"`{esc(x['table'])}` |\n")
    print(f'\n证据表 → {EVID}')

    _m = [dict(md=x['path'].relative_to(MD).as_posix(), topic=x['topic'], tbl=x['tbl'],
               R=x['R'], C=x['C'], placed=x['placed'], a=x['a'], e=x['e'],
               sha1_orig=hashlib.sha1(x['orig'].encode('utf-8')).hexdigest(),
               orig=x['orig'], new=x['table']) for x in accepted]
    ASSIGN.write_text(json.dumps(_m, ensure_ascii=False, indent=0), encoding='utf-8')
    print(f'机器可读清单 → {ASSIGN}（{len(_m):,} 条，本次全量重写）')

    if not APPLY:
        print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
        return

    per = {}
    for x in accepted:
        per.setdefault(x['path'], []).append(x)
    changed = 0
    for p, recs in sorted(per.items(), key=lambda kv: str(kv[0])):
        t = p.read_bytes().decode('utf-8', 'replace')
        crlf_only_before = t.count('\n') == t.count('\r\n')
        for x in sorted(recs, key=lambda r: -r['a']):
            assert t[x['a']:x['e']] == x['orig'], f"{p.name}: 区域与预期不符"
            t = t[:x['a']] + x['table'] + x['tail'] + t[x['e']:]
            changed += 1
        if crlf_only_before:
            assert t.count('\n') == t.count('\r\n'), f'{p.name}: 混入了裸 LF'
        p.write_bytes(t.encode('utf-8'))

    bad = F._replay_verify(per)
    if bad:
        print(f'\n⛔ 重放验证失败 {len(bad)} 篇，前 5：')
        for rel, why in bad[:5]:
            print(f'   {rel}: {why}')
        sys.exit(3)
    print(f"\n[已改] {changed:,} 张，涉及 {len(per):,} 篇（逐字节重放 {len(per):,}/{len(per):,} 通过）")


def verify_only():
    _m = json.loads(ASSIGN.read_text(encoding='utf-8'))
    per = {}
    for x in _m:
        key = MD / x['md']
        per.setdefault(key, []).append(
            dict(a=x['a'], e=x['e'], orig=x['orig'], table=x['new'], tail=x.get('tail', '')))
    print(f'清单 {len(_m):,} 条 / {len(per):,} 篇；对 `git show HEAD:` 逐字节重放…')
    bad = F._replay_verify(per)
    if bad:
        print(f'⛔ 失败 {len(bad)} 篇，前 10：')
        for rel, why in bad[:10]:
            print(f'   {rel}: {why}')
        sys.exit(3)
    print(f'✅ 重放一致：{len(per):,}/{len(per):,} 篇，逐字节相同。')


if __name__ == '__main__':
    main()
