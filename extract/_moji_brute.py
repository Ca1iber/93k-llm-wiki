# -*- coding: utf-8 -*-
"""逐个直接搜：把剩余坏字的上下文收集起来，一趟扫过全部上游，碰到就记。
判据仍是两条：① 上下文在上游里唯一命中 ② 候选与坏字的 GBK 字节对得上。"""
import io, os, re, sys, json, html, collections, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

FAM = '鈥鈮鈩鈼鈫锛鈭銆'
PRE = {}
for _c in FAM:
    try: PRE[_c] = _c.encode('gbk')
    except Exception: PRE[_c] = b''
def ok(bad, c):
    p = PRE.get(bad) or b''
    return bool(p) and c.encode('utf-8').startswith(p)

D = os.path.dirname(os.path.abspath(__file__))
NEED = 25          # 前后各取多少个字母数字空白字符当上下文


def ctx(s, i):
    """坏字前面【不含任何坏字/残渣】的那一段，保留标点（上游里标点也在）。"""
    j = i - 1
    while j >= 0:
        ch = s[j]
        if ch in FAM or ch == '?' or 0xE000 <= ord(ch) <= 0xF8FF:
            break
        j -= 1
    t = re.sub(r'\s+', ' ', s[j + 1:i]).strip()
    return t[-40:] if len(t) >= 12 else ''


# 1) 收集
jobs = []
for topic, p in json.load(io.open(os.path.join(D, '_moji_files.json'), encoding='utf-8')):
    s = T.read(p)
    for m in re.finditer('[' + FAM + ']', s):
        c = ctx(s, m.start())
        if c: jobs.append([p, m.start(), s[m.start()], c, None])
print(f'待查 {len(jobs)} 处')

# 2) 一趟扫上游
cache = collections.defaultdict(list)
for fn in sorted(os.listdir(T.HTM)):
    if not fn.lower().endswith(('.htm', '.html')): continue
    h = T.read(os.path.join(T.HTM, fn))
    h = re.sub(r'<script\b.*?</script>', ' ', h, flags=re.S | re.I)
    U = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h)))
    for jb in jobs:
        if jb[4] is not None: continue
        if jb[3] in U:
            pos = U.index(jb[3]) + len(jb[3])
            nxt = re.match(r'\W*(\S)', U[pos:])
            if nxt and ok(jb[2], nxt.group(1)):
                jb[4] = nxt.group(1); jb.append(fn)
            else:
                jb[4] = False
print(f'  上游命中并定出正字 {sum(1 for j in jobs if j[4] and j[4] is not False)}')

# 3) 落盘
done = collections.defaultdict(list)
for jb in jobs:
    if jb[4] and jb[4] is not False:
        done[jb[0]].append((jb[1], jb[2], jb[4]))
n = 0
for p, items in done.items():
    s = T.read(p)
    for i, bad, good in sorted(items, key=lambda x: -x[0]):
        if s[i] != bad: continue
        e = i + 1
        while e < len(s) and (s[e] == '?' or 0xE000 <= ord(s[e]) <= 0xF8FF): e += 1
        s = s[:i] + good + s[e:]; n += 1
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
print(f'改了 {n} 处 / {len(done)} 篇')
if n:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'表外乱码·逐个搜全库：修 {n} 处 / {len(done)} 篇'],
                   cwd=T.TDC, capture_output=True)
    print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                         text=True, encoding='utf-8').stdout.strip())
