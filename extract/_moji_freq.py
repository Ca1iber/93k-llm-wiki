# -*- coding: utf-8 -*-
"""按【全库频率 + 局部上下文】定正字。不靠上游 —— 语料自己就是证据。

鈩 (E2 84)  → ™   90%（Direct-Probe™ 在同一个文件里干净地出现过）
鈮 (E2 89)  → ≤   80%
鈥 (E2 80)  → 两边都紧邻字母数字 → ‑（非断行连字符）；否则 → …
鈫 (E2 86)  → →   语料里只有这一个
其余族样本太少 → 不动
"""
import io, os, re, sys, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

FAM = '鈥鈮鈩鈼鈫锛鈭銆'
PRE = {}
for _c in FAM:
    try: PRE[_c] = _c.encode('gbk')
    except Exception: PRE[_c] = b''
FIXED = {'鈩': '™', '鈮': '≤', '鈫': '→'}


def ok(bad, c):
    p = PRE.get(bad) or b''
    return bool(p) and c.encode('utf-8').startswith(p)


def pick(bad, s, i):
    if bad in FIXED:
        return FIXED[bad] if ok(bad, FIXED[bad]) else None
    if bad == '鈥':
        L = s[i-1] if i > 0 else ''
        R = s[i+1] if i+1 < len(s) else ''
        cand = '‑' if (L.isalnum() and R.isalnum()) else '…'
        return cand if ok(bad, cand) else None
    return None


D = os.path.dirname(os.path.abspath(__file__))
n = 0; files = 0; skip = 0; use = {}
for topic, p in json.load(io.open(os.path.join(D, '_moji_files.json'), encoding='utf-8')):
    s = T.read(p)
    if not re.search('[' + FAM + ']', s): continue
    out = []; i = 0; ch = 0
    while i < len(s):
        if s[i] in FAM:
            c = pick(s[i], s, i)
            if c:
                out.append(c); use[s[i]] = use.get(s[i], 0) + 1; ch += 1; n += 1
                i += 1
                while i < len(s) and (s[i] == '?' or 0xE000 <= ord(s[i]) <= 0xF8FF): i += 1
                continue
            skip += 1
        out.append(s[i]); i += 1
    if ch:
        io.open(p, 'w', encoding='utf-8', newline='').write(''.join(out)); files += 1

print(f'修了 {n} 处 / {files} 篇；无判据跳过 {skip} 处')
print('按族:', use)
if n:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'表外乱码·全库频率+上下文：修 {n} 处 / {files} 篇'],
                   cwd=T.TDC, capture_output=True)
    print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                         text=True, encoding='utf-8').stdout.strip())
