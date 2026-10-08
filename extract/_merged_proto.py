#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""原型：**合并格表**的解析与展开（重复法）。只读，不改任何文件。

与 `fix_corpus_tables.py` 的唯一区别：
- 不要求「每行列数相同」——合并表每行的格子数本来就不同（rowspan 那几行少一格）
- 上游表**先按 colspan/rowspan 排成矩形网格**，再把被覆盖的位置填上跨格文字（= 重复法）
- token 数 P = Σ(每行格子数) + 行数

**逐格核对不变**：md 解析出来的格子，逐行逐格必须与上游 HTML 的格子一致。
"""
import pathlib
import re
import sys

sys.path.insert(0, r'F:\master-dev\understand-anything-wiki\extract')
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import fix_corpus_tables as F


def lay_out(rows):
    """把 HTML 的 rows（每格带 colspan/rowspan）排成矩形网格。

    返回 (R, C, expanded)。`expanded[r][c]` = 覆盖该位置的格子的文字
    （被合并格覆盖的位置**填上跨格文字** —— 这就是「重复法」）。
    """
    occupied, placed = {}, []
    for r, row in enumerate(rows):
        c = 0
        for cell in row:
            while (r, c) in occupied:
                c += 1
            cs, rs = cell['colspan'], cell['rowspan']
            for dr in range(rs):
                for dc in range(cs):
                    occupied[(r + dr, c + dc)] = cell
            placed.append((r, c, cell))
            c += cs
    R = len(rows)
    C = max(c for _, c, _ in placed) + 1 if placed else 0
    expanded = [['' for _ in range(C)] for _ in range(R)]
    for r, c, cell in placed:
        txt = ''.join(cell['txt'])
        for dr in range(cell['rowspan']):
            for dc in range(cell['colspan']):
                if r + dr < R and c + dc < C:
                    expanded[r + dr][c + dc] = txt
    return R, C, expanded


def try_merged(text, allt, bol_idx, eol_idx, rows):
    """返回 (候选列表, 原因)。每条候选 = (start, end, cells_md, cells_up, R, C, expanded)。"""
    n_i = [len(r) for r in rows]
    R = len(rows)
    P = sum(n_i) + R
    flat_up = [F.norm_up(''.join(c['txt'])) for r in rows for c in r]
    Rg, Cg, expanded = lay_out(rows)
    cands, fitted = [], False
    for i in bol_idx:
        r = F.parse_region(text, allt, eol_idx, i, P)
        if not r:
            continue
        chunks, start, end = r
        if chunks[0].strip() or chunks[-1].strip():
            continue
        # 逐行取 n_i 格，行间一个空档
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
        if any('```' in c for c in cells):
            return [], '格内有代码围栏', None
        if sum(len(F.norm_md(c)) for c in cells) < F.MIN_CONTENT:
            return [], '内容近于空', None
        cands.append((start, end, cells, flat_up, Rg, Cg, expanded))
    if cands:
        return cands, None, None
    return [], ('网格不等' if fitted else '窗口放不下'), None


def main():
    docs = []
    for p in sorted(F.MD.rglob('*.md')):
        t = p.read_bytes().decode('utf-8', 'replace')
        if sum(1 for l in t.splitlines() if F.LONE.fullmatch(l)) >= 2:
            docs.append(p)

    stat, tbl_stat = {}, {}
    accepted = []

    def bump(d, k, n=1):
        d[k] = d.get(k, 0) + n

    for p in docs:
        text = p.read_bytes().decode('utf-8', 'replace')
        allt, bol, eol, col0 = F.md_tokens(text)
        if col0:
            continue
        m = F.SOURCE_TOPIC.search(text)
        if not m:
            continue
        ups, why = F.upstream_tables(m.group(1).replace('.htm', ''))
        if not ups:
            continue
        merged = [u for u in ups if u['skip'] == '合并格']
        if not merged:
            continue
        by = {}
        for ui, u in enumerate(merged):
            mine, reason, _ = try_merged(text, allt, bol, eol, u['rows'])
            by[ui] = mine
            if reason:
                bump(tbl_stat, reason)
        picked = []
        for ui, lst in sorted(by.items()):
            rows = merged[ui]['rows']
            lst = sorted(lst, key=lambda c: -(c[1] - c[0]))
            keep, spans = [], []
            for c in lst:
                if any(not (c[1] <= s or c[0] >= e) for s, e in spans):
                    continue
                spans.append((c[0], c[1])); keep.append(c + (len(rows),))
            if len(keep) == 1:
                picked.append(keep[0])
            elif keep:
                bump(tbl_stat, '同表多处命中')
        if not picked:
            bump(stat, '无表对上')
            continue
        for c in picked:
            accepted.append(dict(path=p, R=c[4], C=c[5], cells=c[2], expanded=c[6],
                                 topic=m.group(1).replace('.htm',''), start=c[0], end=c[1]))

    n_tbl = len(accepted)
    n_doc = len({x['path'] for x in accepted})
    print(f'✅ 合并表可修 **{n_tbl:,} 张**，涉及 **{n_doc:,} 篇**')
    print('\n跳过（表侧）：')
    for k, v in sorted(tbl_stat.items(), key=lambda kv: -kv[1]):
        print(f'   {k:<24} {v:,}')
    print('\n--- 样例（含长跨度）---')
    show = sorted(accepted, key=lambda x: -max(
        (len(set(row)) == 1 and x['C'] > 1) * x['C'] for row in x['expanded']))[:3]
    for x in show[:3]:
        grid = x['expanded']
        print(f"\n### {x['path'].relative_to(F.MD).as_posix()}")
        print(f"    上游 {len(grid)} 行 × {x['C']} 列（展开后）")
        for row in grid[:14]:
            cells = [F.clean_cell(c) for c in row]
            print('    | ' + ' | '.join(c[:46] for c in cells) + ' |')


if __name__ == '__main__':
    main()
