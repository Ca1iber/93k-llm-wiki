# -*- coding: utf-8 -*-
"""第七轮：给「上游有表、md 里没有」的那些补逐条指针。
定位改用【它前面最近的那个标题】—— 上游有 <h2>/<h3>，md 里也有同样的标题，
比散文锚稳（散文会被转换改写，标题不会）。"""
import io, os, re, sys, html, collections, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

up = T.enumerate_upstream()
have = collections.defaultdict(set); cur = None
t2f = collections.defaultdict(list)
for dp, _, fns in os.walk(T.MD):
    for fn in fns:
        if not fn.endswith('.md'): continue
        p = os.path.join(dp, fn); s = T.read(p)
        m = re.search(r'source_topic:\s*"([^"]+)"', s)
        if m: t2f[m.group(1)].append(p)
        cur = None
        for l in s.split('\n'):
            mm = re.search(r'raw/([^`]+)`', l)
            if mm and '表格指针' in l: cur = mm.group(1)
            m2 = re.search(r'第 (\d+) 个有格子的', l)
            if m2 and cur: have[cur].add(int(m2.group(1)))
miss = collections.defaultdict(list)
for k, t in up.items():
    if (t['idx'] + 1) not in have.get(k[0], set()): miss[k[0]].append(t)
print(f'待补 {sum(len(v) for v in miss.values())} 张 / {len(miss)} 篇')

HEAD = re.compile(r'<h([1-4])[^>]*>(.*?)</h\1>', re.S | re.I)


def norm_txt(s):
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip().lower()


ok = 0; nohead = 0; nohw = 0; files = 0
for topic, ts in sorted(miss.items()):
    ps = t2f.get(topic, [])
    if not ps: continue
    p = ps[0]
    h = T.read(os.path.join(T.HTM, topic))
    heads = [(m.start(), int(m.group(1)), norm_txt(m.group(2))) for m in HEAD.finditer(h)]
    spans = []
    n = 0
    for tag, s0, e0 in T.upstream_tables(h):
        cs = T.up_cells(h[s0:e0])
        if not cs or len(T.norm(''.join(cs))) < T.MIN_TEXT: continue
        spans.append((n, s0)); n += 1
    lines, nl = T.split_lines(T.read(p))
    if lines is None: continue
    mdz = [norm_txt(l.lstrip('#').strip()) if l.lstrip().startswith('#') else None for l in lines]
    ins = collections.defaultdict(list)
    for t in sorted(ts, key=lambda x: x['idx']):
        st = next((s0 for k, s0 in spans if k == t['idx']), None)
        if st is None: nohead += 1; continue
        pre = [x for x in heads if x[0] < st]
        if not pre: nohead += 1; continue
        _, lvl, txt = pre[-1]
        cand = [i for i, z in enumerate(mdz) if z == txt and lines[i].lstrip().startswith('#')]
        if len(cand) != 1: nohw += 1; continue
        ins[cand[0]].append(t); ok += 1
    if ins:
        for i, ts2 in sorted(ins.items(), key=lambda x: -x[0]):
            blk = [''] + '\n'.join(T.pointer_block(t) for t in ts2).split('\n') + ['']
            lines[i + 1:i + 1] = blk
        io.open(p, 'w', encoding='utf-8', newline='').write(nl.join(lines)); files += 1

print(f'补上 {ok} 张 / {files} 篇；标题对不上 {nohw}；找不到前置标题 {nohead}')
if files:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'表格指针化第七轮：用前置标题定位，补逐条指针 {ok} 张 / {files} 篇'],
                   cwd=T.TDC, capture_output=True)
    print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                         text=True, encoding='utf-8').stdout.strip())
