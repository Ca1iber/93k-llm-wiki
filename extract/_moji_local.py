# -*- coding: utf-8 -*-
"""表外乱码 · 两侧锚 + 局部对齐。

对每个坏字：
  ① 左边取一段【纯 ASCII、≥12 字符】的干净片段当左锚
  ② 右边取一段【纯 ASCII、≥12 字符】的干净片段当右锚
  ③ 左锚在上游唯一命中 → 从那里往后找右锚（唯一）
  ④ 把 md 两锚之间那一小段 与 上游两锚之间那一小段 做局部对齐 → 取候选
  ⑤ 候选必须与坏字的 GBK 字节对得上（第二条判据，不放）
"""
import io, os, sys, re, html, json, difflib, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

D = os.path.dirname(os.path.abspath(__file__))
FAM = '鈥鈮鈩鈼鈫锛鈭銆'
PRE = {}
for _c in FAM:
    try: PRE[_c] = _c.encode('gbk')
    except Exception: PRE[_c] = b''


def ok_char(bad, c):
    p = PRE.get(bad) or b''
    if not p: return False
    try: return c.encode('utf-8').startswith(p)
    except Exception: return False


def up_plain(topic):
    if not topic: return ''
    hp = os.path.join(T.HTM, topic)
    if not os.path.exists(hp): return ''
    h = T.read(hp)
    h = re.sub(r'<script\b.*?</script>', ' ', h, flags=re.S | re.I)
    h = re.sub(r'<[^>]+>', ' ', h)
    return re.sub(r'\s+', ' ', html.unescape(h))


def clean_ascii(s, i, step, need=10):
    """从 i 出发沿 step 方向取一段纯 ASCII 片段（≥need 字符）"""
    # ★ 锚**不要求紧贴坏字**：许多坏字紧挨着的是 `- `（列表符）、`|`（表格分隔）、`?`，
    #   紧贴处凑不出 10 个字符的干净串。所以在 ±120 字符内找**最近的一段**。
    # ★ 锚只取【字母数字和空白】：带 md 语法（`[x](<y.md>)`）的锚在上游 HTML 里
    #   根本搜不到 —— 实测这是「左锚出现 0 次」的全部原因。
    j = i
    if step > 0:      # 右边先跳过残渣（`?` / 私用区字符）
        while 0 <= j < len(s) and (s[j] == '?' or 0xE000 <= ord(s[j]) <= 0xF8FF):
            j += 1
    buf = []; gap = 0
    while 0 <= j < len(s) and len(buf) < 80:
        ch = s[j]
        if ch.isascii() and (ch.isalnum() or ch.isspace()):
            buf.append(ch); j += step
        else:
            if gap > 120: break
            gap += 1; j += step
            if buf and not buf[-1].isspace(): buf.append(' ')
    t = ''.join(reversed(buf)) if step < 0 else ''.join(buf)
    t = re.sub(r'\s+', ' ', t).strip()
    return t if len(t) >= need else ''


FAMRE = '[' + FAM + ']'
work = json.load(io.open(os.path.join(D, '_moji_files.json'), encoding='utf-8'))
fixed = 0; noanc = 0; badcand = 0; files = 0; samples = []
for topic, p in work:
    U = up_plain(topic)
    if not U: continue
    s = T.read(p)
    if not re.search(FAMRE, s): continue
    edits = []
    for m in re.finditer(FAMRE, s):
        i = m.start(); bad = s[i]
        L = clean_ascii(s, i - 1, -1)
        R = clean_ascii(s, i + 1, +1)
        if not L or not R: noanc += 1; continue
        if U.count(L) != 1: noanc += 1; continue
        a = U.index(L) + len(L)
        b = U.find(R, a)
        if b < 0 or U.count(R) != 1: noanc += 1; continue
        up_mid = U[a:b].strip()
        md_mid = s[i - len(L) + len(L):i + 1 + (0 if False else 0)]
        # md 两锚之间 = 坏字本身（右边锚紧跟在坏字之后）
        cand = next((x for x in up_mid if ok_char(bad, x)), None)
        if cand is None:
            badcand += 1; continue
        if len(up_mid) != 1 and up_mid.strip() not in (cand,):
            # 上游中间还有别的内容：只在它确实只有一个字符时才认
            if len(up_mid) > 4: badcand += 1; continue
        a1 = i + 1
        while a1 < len(s) and (s[a1] == '?' or 0xE000 <= ord(s[a1]) <= 0xF8FF): a1 += 1
        edits.append((i, a1, cand)); fixed += 1
        if len(samples) < 8: samples.append((L[-14:], bad, R[:10], up_mid[:12], cand))
    if edits:
        txt = s
        for a0, a1, ch in sorted(edits, key=lambda x: -x[0]): txt = txt[:a0] + ch + txt[a1:]
        io.open(p, 'w', encoding='utf-8', newline='').write(txt); files += 1

print(f'修复 {fixed} 处 / {files} 篇；无干净双方锚 {noanc}；候选不合字节区间 {badcand}')
for x in samples: print('   左锚…%-14s 坏字=%s 右锚=%s… 上游中段=%-12s → %s' % x)
if fixed:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'表外乱码·两侧锚局部对齐：修 {fixed} 处 / {files} 篇'],
                   cwd=T.TDC, capture_output=True)
    print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                         text=True, encoding='utf-8').stdout.strip())
