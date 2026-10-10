# -*- coding: utf-8 -*-
import io, os, re, sys, html
WIKI = r"F:\master-dev\understand-anything-wiki\wiki"
MD   = r"F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category"
HTM  = r"F:\master-dev\dorm-wsl-sytest\tdc-html\raw"

def n2(s, sep):
    s = re.sub(r'<[^>]+>', sep, s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s)

cache = {}
def variants(topic):
    if topic not in cache:
        p = os.path.join(HTM, topic)
        if not os.path.exists(p): cache[topic] = []
        else:
            raw = io.open(p, encoding='utf-8', errors='replace').read()
            cache[topic] = [n2(raw, ' '), n2(raw, ''), re.sub(r'[^0-9A-Za-z]', '', html.unescape(re.sub(r'<[^>]+>', '', raw)))]
    return cache[topic]

def all_topics():
    return [f for f in os.listdir(HTM) if f.lower().endswith(('.htm', '.html'))]

QS = [("objects/gctx.md","The context is only correct when all primary sets (defined by SPRM) and the current start label"),
      ("objects/level-equation-file.md","Must be defined for the protocol specified by protocolName."),
      ("objects/pin-configuration-tool.md","For a DC Scale pin in PMU operating mode, it must be SIG."),
      ("objects/sharing-configuration.md","The name of the sharing configuration file which you want to load."),
      ("objects/sharing-configuration.md","The file must be located in the <device directory>/configuration/ directory."),
      ("objects/spst.md","It is possible to modify the timing or level data with ETIM(ETDS), PCLK, CLKR, DRLV, RCLV, TERM")]

# 先只在本篇 sources 指向的上游里找；找不到再全库找
def md_topics(page):
    p = os.path.join(WIKI, page)
    s = io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''
    head = s.split('---')[1] if s.startswith('---') else ''
    out = []
    for rel in re.findall(r'^\s+-\s+(.+\.md)\s*$', head, re.M):
        mp = os.path.join(MD, rel.replace('/', os.sep))
        if os.path.exists(mp):
            m = re.search(r'source_topic:\s*"([^"]+)"', io.open(mp, encoding='utf-8', errors='replace').read())
            if m: out.append(m.group(1))
    return out

print("逐条找（先用本篇 sources 的上游，再全库）")
for page, q in QS:
    qn = re.sub(r'\s+',' ',q).strip()
    q_ascii = re.sub(r'[^0-9A-Za-z]', '', q)
    hit = None
    for t in md_topics(page):
        vs = variants(t)
        if any(qn in v or q_ascii in vs[2] for v in vs): hit = t; break
    if not hit:
        for t in all_topics():
            vs = variants(t)
            if q_ascii and q_ascii in vs[2]: hit = '全库:' + t; break
    print(f"  {'✓' if hit else '✗'} {page:38} {q[:58]}")
    if hit and hit != 'onpage': print(f"       → {hit}")
