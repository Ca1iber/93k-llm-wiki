# -*- coding: utf-8 -*-
"""第六轮：上游有表、md 里既无内容也无指针，且逐条定位不到的 →
在本篇顶部加一条【文件级】说明（位置无关，只指出真结构在哪）。"""
import io, os, sys, re, collections, subprocess
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

n = 0
for topic, ts in sorted(miss.items()):
    for p in t2f.get(topic, []):
        lines, nl = T.split_lines(T.read(p))
        if lines is None: continue
        idxs = [t['idx'] + 1 for t in sorted(ts, key=lambda x: x['idx'])]
        L = (f'> ⚠️ 上游表格说明（非原文）：本篇对应的上游 `tdc-html/raw/{topic}` 里还有 '
             f'**{len(idxs)} 张表**本 md 没有逐条转出'
             f'（第 {"、".join(str(i) for i in idxs[:20])} 张'
             f'{"…" if len(idxs) > 20 else ""}）。真表见上游文件。')
        # 插到 frontmatter 之后、第一个 `# ` 之前
        k = 0
        if lines and lines[0].strip() == '---':
            k = next((i + 1 for i in range(1, len(lines)) if lines[i].strip() == '---'), 0)
        while k < len(lines) and not lines[k].strip(): k += 1
        lines[k:k] = L.split('\n') + ['']
        io.open(p, 'w', encoding='utf-8', newline='').write(nl.join(lines))
        n += 1
print(f'加了文件级说明 {n} 篇（涉及 {len(miss)} 个上游文件）')
subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
subprocess.run(['git', 'commit', '-q', '-m', f'表格指针化第六轮：{n} 篇加上游表格说明（逐条定位不到的那些）'],
               cwd=T.TDC, capture_output=True)
print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                     text=True, encoding='utf-8').stdout.strip())
