# -*- coding: utf-8 -*-
"""第四轮：① 空表(`|   |`)直接删；② 签名不同但重叠 ≥50% 且唯一的表块 → 指针。"""
import io, os, sys, re, subprocess, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

up = T.enumerate_upstream(); f2t, t2f = T.topic_to_md()
by = collections.defaultdict(list)
for k, t in up.items(): by[t['topic']].append(t)

n_empty = n_ptr = 0; plans = []; left = []
for dp, _, fns in os.walk(T.MD):
    for fn in fns:
        if not fn.endswith('.md'): continue
        p = os.path.join(dp, fn); s = T.read(p)
        tp = re.search(r'source_topic:\s*"([^"]+)"', s)
        tp = tp.group(1) if tp else None
        tabs = by.get(tp, [])
        lines, nl = T.split_lines(s)
        if lines is None: continue
        items = []
        for k, a, b in T.md_blocks(s):
            if k != 'table': continue
            cs = T.block_cells(lines, 'table', a, b)
            if len(cs) <= 1:
                items.append((a, b, [])); n_empty += 1; continue      # 空表 → 删
            if any(t['sig'] == T.sig(cs) for t in tabs): continue      # ① 已管，不该出现
            rc = {T.norm(c) for c in cs} - {''}
            best = []
            for t in tabs:
                tc = {T.norm(c) for c in T.up_cells_of(t)} - {''}
                if tc and len(tc & rc) / len(tc) >= 0.5: best.append((len(tc & rc) / len(tc), t))
            best.sort(key=lambda x: -x[0])
            if best and (len(best) == 1 or best[0][0] > best[1][0]):
                items.append((a, b, T.pointer_block(best[0][1]).split('\n'))); n_ptr += 1
            else:
                left.append((p, a, b))
        if items:
            plans.append((p, nl, sorted(items, key=lambda x: -x[0])))

for p, nl, items in plans:
    lines, _ = T.split_lines(T.read(p))
    for a, b, blk in items: lines[a:b] = blk
    io.open(p, 'w', encoding='utf-8', newline='').write(nl.join(lines))
print(f'删空表 {n_empty}   补指针 {n_ptr}   剩下 {len(left)}   涉及 {len(plans)} 篇')
subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
subprocess.run(['git', 'commit', '-q', '-m',
                f'表格指针化第四轮：删空表 {n_empty}，签名放宽后补指针 {n_ptr}'],
               cwd=T.TDC, capture_output=True)
print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                     text=True, encoding='utf-8').stdout.strip())
