# -*- coding: utf-8 -*-
"""把第七类红的引文，逐条回上游 raw/ 核实。"""
import io, os, re, sys, html, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WIKI = r"F:\master-dev\understand-anything-wiki\wiki"
MD   = r"F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category"
HTM  = r"F:\master-dev\dorm-wsl-sytest\tdc-html\raw"

rep = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stage-report.md'),
              encoding='utf-8', errors='replace').read()
sec = rep.split('## 第七类')[1].split('## 第八类')[0]

cur = None; items = []
for ln in sec.split('\n'):
    m = re.match(r'- ❌ `([^`]+)`', ln)
    if m: cur = m.group(1); continue
    m = re.search(r'❌ \*\*自称逐字、覆盖率 \d+%\*\*｜`(.+)`\s*$', ln)
    if m and cur: items.append((cur, m.group(1)))
print(f"第七类里「自称逐字却对不上」的引文: {len(items)} 条，涉及 {len({p for p,_ in items})} 页")

def norm(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s)

# 上游全文（归一化后）按 topic 缓存
cache = {}
def up_text(topic):
    if topic not in cache:
        p = os.path.join(HTM, topic)
        cache[topic] = norm(io.open(p, encoding='utf-8', errors='replace').read()) if os.path.exists(p) else ''
    return cache[topic]

def md_topics(page):
    p = os.path.join(WIKI, page)
    if not os.path.exists(p): return []
    s = io.open(p, encoding='utf-8', errors='replace').read()
    head = s.split('---')[1] if s.startswith('---') else ''
    return re.findall(r'^\s+-\s+(.+\.md)\s*$', head, re.M)

found = notfound = nocand = 0; bad = []
for page, q in items:
    qn = norm(q).strip().rstrip('…').strip()
    if len(qn) < 12: nocand += 1; continue
    topics = []
    for rel in md_topics(page):
        mp = os.path.join(MD, rel.replace('/', os.sep))
        if os.path.exists(mp):
            m = re.search(r'source_topic:\s*"([^"]+)"', io.open(mp, encoding='utf-8', errors='replace').read())
            if m: topics.append(m.group(1))
    hit = any(qn in up_text(t) for t in topics)
    if hit: found += 1
    else:
        notfound += 1
        bad.append((page, q[:95]))
print(f"  上游能找到      : {found}")
print(f"  上游也找不到    : {notfound}   ← 这些才是可疑的")
print(f"  太短没法查      : {nocand}")
print()
for p, q in bad[:12]: print(f"   {p}\n      {q}")
