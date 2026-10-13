# -*- coding: utf-8 -*-
"""第五轮：上游有表、md 里既无内容也无指针的 → 用「表前那段散文」定位，补一条指针。"""
import io, os, sys, re, html, collections, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

up = T.enumerate_upstream()
have = collections.defaultdict(set)
for dp, _, fns in os.walk(T.MD):
    for fn in fns:
        if not fn.endswith('.md'): continue
        cur = None
        for l in T.read(os.path.join(dp, fn)).split('\n'):
            m = re.search(r'raw/([^`]+)`', l)
            if m and '表格指针' in l: cur = m.group(1)
            m2 = re.search(r'第 (\d+) 个有格子的', l)
            if m2 and cur: have[cur].add(int(m2.group(1)))
miss = [(k, t) for k, t in up.items() if (t['idx'] + 1) not in have.get(k[0], set())]
print(f'上游有表、md 无指针的：{len(miss)}')


def anchor_before(h, st):
    """上游那张表【前面】的最后一段散文（去标签、解实体）。"""
    seg = h[max(0, st - 3000):st]
    seg = re.sub(r'<script\b.*?</script>', ' ', seg, flags=re.S | re.I)
    seg = re.sub(r'<[^>]+>', ' ', seg)
    seg = re.sub(r'\s+', ' ', html.unescape(seg)).strip()
    return seg[-140:]


tabs_by_topic = collections.defaultdict(list)
for k, t in up.items(): tabs_by_topic[k[0]].append(t)
t2f = collections.defaultdict(list)
for dp, _, fns in os.walk(T.MD):
    for fn in fns:
        if not fn.endswith('.md'): continue
        p = os.path.join(dp, fn)
        m = re.search(r'source_topic:\s*"([^"]+)"', T.read(p))
        if m: t2f[m.group(1)].append(p)

ok = 0; noanchor = 0; left = []
edits = collections.defaultdict(list)
for (topic, idx), t in miss:
    ps = t2f.get(topic, [])
    if not ps: left.append((topic, idx, '无 md')); continue
    h = T.read(os.path.join(T.HTM, topic))
    # 找该表在上游的位置
    spans = T.upstream_tables(h); k = -1; st = None
    for tag, s0, e0 in spans:
        cs = T.up_cells(h[s0:e0])
        if not cs or len(T.norm(''.join(cs))) < T.MIN_TEXT: continue
        k += 1
        if k == idx: st = s0; break
    if st is None: left.append((topic, idx, '上游找不到该表')); continue
    anc = T.norm(anchor_before(h, st))
    if len(anc) < 20: noanchor += 1; left.append((topic, idx, '锚太短')); continue
    placed = False
    for p in ps:
        lines, nl = T.split_lines(T.read(p))
        nlz = [T.norm(l) for l in lines]
        for i, l in enumerate(nlz):
            if anc and anc in l:
                edits[p].append((i + 1, i + 1, T.pointer_block(t).split('\n') + ['']))
                ok += 1; placed = True; break
        if placed: break
    if not placed: left.append((topic, idx, '锚在 md 里找不到'))

print(f'  补上 {ok}   仍缺 {len(left)}（锚太短 {noanchor}）')
for p, items in edits.items():
    lines, nl = T.split_lines(T.read(p))
    for a, b, blk in sorted(items, key=lambda x: -x[0]): lines[a:b] = blk
    io.open(p, 'w', encoding='utf-8', newline='').write(nl.join(lines))
print(f'  改了 {len(edits)} 篇')
if edits:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'表格指针化第五轮：上游有表而 md 缺的，用表前散文定位补指针 {ok} 条'],
                   cwd=T.TDC, capture_output=True)
    print('  ', subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                               text=True, encoding='utf-8').stdout.strip())
print('  仍缺抽样:', [x for x in left[:6]])
