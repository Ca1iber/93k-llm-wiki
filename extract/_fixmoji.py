# -*- coding: utf-8 -*-
"""表外乱码：用「坏字前面那个 ASCII 词」当锚，到上游取正字。
判据两条，缺一不可：① 锚在该篇上游里**唯一命中**；② 上游那个位置恰好**一个非空白字符**。"""
import io, os, sys, re, html, collections, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

FAM = '鈥鈮鈩鈼鈫锛鈭銆'
t2f = collections.defaultdict(list)
for dp, _, fns in os.walk(T.MD):
    for fn in fns:
        if not fn.endswith('.md'): continue
        p = os.path.join(dp, fn)
        m = re.search(r'source_topic:\s*"([^"]+)"', T.read(p))
        if m: t2f[m.group(1)].append(p)

cache = {}


def up_plain(topic):
    if topic not in cache:
        hp = os.path.join(T.HTM, topic)
        if not os.path.exists(hp): cache[topic] = ''
        else:
            h = T.read(hp)
            h = re.sub(r'<script\b.*?</script>', ' ', h, flags=re.S | re.I)
            h = re.sub(r'<[^>]+>', ' ', h)
            cache[topic] = re.sub(r'\s+', ' ', html.unescape(h))
    return cache[topic]


fixed = 0; skip = 0; files = 0
# ★ 先筛出真有乱码的文件，再取上游 —— 反过来会读遍 576MB 上游（实测 >10 分钟）
work = []
for topic, ps in sorted(t2f.items()):
    for p in ps:
        s0 = T.read(p)
        if any(c in s0 for c in FAM): work.append((topic, p, s0))
print(f'有乱码的文件 {len(work)} 篇')
for topic, p, s in work:
    U = up_plain(topic)
    if not U: continue
    if True:
        out = []; i = 0; ch = 0
        while i < len(s):
            if s[i] in FAM:
                # 锚：坏字前面最后一个 ≥3 字符的 ASCII 词
                j = i; k = i - 1
                while k >= 0 and (s[k] == '?' or not s[k].strip()): k -= 1   # 跳过 `?`
                e = k + 1
                while k >= 0 and (s[k].isalnum() or s[k] in '._-/'): k -= 1
                anc = s[k + 1:e]
                if len(anc) >= 3 and U.count(anc) == 1:
                    t = U.index(anc) + len(anc)
                    m = re.match(r'\W*(\S)', U[t:])          # 后面第一个非空白字符
                    if m:
                        out.append(m.group(1)); i = e; ch += 1; fixed += 1; continue
                skip += 1
            out.append(s[i]); i += 1
        if ch:
            io.open(p, 'w', encoding='utf-8', newline='').write(''.join(out)); files += 1
print(f'修复 {fixed} 处 / {files} 篇；判据不达标跳过 {skip} 处')
if fixed:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'表外乱码：锚+上游取正字，修 {fixed} 处 / {files} 篇'],
                   cwd=T.TDC, capture_output=True)
    print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                         text=True, encoding='utf-8').stdout.strip())
