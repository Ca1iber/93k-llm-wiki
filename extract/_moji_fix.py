# -*- coding: utf-8 -*-
"""第二步：只读 _moji_files.json 的名单，逐篇修。
判据三条缺一不可：① 锚是坏字前最后一个 ≥3 字符 ASCII 词；② 该锚在这一篇上游里唯一命中；
③ 上游那个位置往后的第一个非空白字符就是正字。不达标一律跳过、报出来。"""
import io, os, sys, re, html, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

D = os.path.dirname(os.path.abspath(__file__))
FAM = '鈥鈮鈩鈼鈫锛鈭銆'
# ★ 第二条判据（项目原有，我第一版漏了它）：
#   坏字 `X` 的 GBK 字节 = 原字 UTF-8 字节的**前 1~2 个**。
#   所以候选正字必须满足 `c.encode('utf-8').startswith(X.encode('gbk'))`。
#   没有这条，`D`、`1`、`i` 这种都会被放过 —— 实测 14 处全错。
PRE = {}
for _c in FAM:
    try: PRE[_c] = _c.encode('gbk')
    except Exception: PRE[_c] = b''


def ok_char(bad, c):
    p = PRE.get(bad) or b''
    if not p: return False
    try: return c.encode('utf-8').startswith(p)
    except Exception: return False
work = json.load(io.open(os.path.join(D, '_moji_files.json'), encoding='utf-8'))
cache = {}


def up_plain(topic):
    if not topic:
        return ''
    if topic not in cache:
        hp = os.path.join(T.HTM, topic)
        if not os.path.exists(hp):
            cache[topic] = ''
        else:
            h = T.read(hp)
            h = re.sub(r'<script\b.*?</script>', ' ', h, flags=re.S | re.I)
            h = re.sub(r'<[^>]+>', ' ', h)
            cache[topic] = re.sub(r'\s+', ' ', html.unescape(h))
    return cache[topic]


fixed = 0; skip = 0; files = 0; samples = []
for topic, p in work:
    U = up_plain(topic)
    s = T.read(p)
    out = []; i = 0; ch = 0
    while i < len(s):
        if s[i] in FAM:
            k = i - 1
            while k >= 0 and (s[k] == '?' or not s[k].strip()): k -= 1
            e = k + 1
            while k >= 0 and (s[k].isalnum() or s[k] in '._-/:'): k -= 1
            anc = s[k + 1:e]
            if len(anc) >= 3 and U and U.count(anc) == 1:
                t = U.index(anc) + len(anc)
                m = re.match(r'\W*(\S)', U[t:])
                if m and ok_char(s[i], m.group(1)):
                    # ★ 必须跳到【坏字及其后面的 `?` 之后】。
                    # 写成 `i = e`（e 是前面那个词的结尾、比 i 还靠前）会原地打转，
                    # out 无限增长 —— 实测把内存顶到 949MB。
                    out.append(m.group(1)); ch += 1; fixed += 1
                    j = i + 1
                    while j < len(s) and s[j] == '?': j += 1
                    i = j
                    if len(samples) < 6: samples.append((anc, m.group(1)))
                    continue
            skip += 1
        out.append(s[i]); i += 1
    if ch:
        io.open(p, 'w', encoding='utf-8', newline='').write(''.join(out)); files += 1

print(f'修复 {fixed} 处 / {files} 篇；判据不达标跳过 {skip} 处')
print('样例(锚 → 正字):', samples)
if fixed:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'表外乱码：锚+上游取正字，修 {fixed} 处 / {files} 篇'],
                   cwd=T.TDC, capture_output=True)
    print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC,
                         capture_output=True, text=True, encoding='utf-8').stdout.strip())
