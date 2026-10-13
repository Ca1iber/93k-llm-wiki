# -*- coding: utf-8 -*-
"""表外乱码 · 整篇对齐版。

判据两条（项目原有，不改）：
  ① 对齐给候选：整份 md 与上游去标签纯文本对齐，坏字所在的「对不上」空档，
     **上游侧去掉空白后恰好一个字符** → 候选。
  ② 坏字的字节定死区间：`鈮`.encode('gbk') = `E2 89` → 候选必须是 `E2 89 XX`。
两条都过才改；不过一律不动。"""
import io, os, sys, re, html, json, difflib, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

D = os.path.dirname(os.path.abspath(__file__))
FAM = '鈥鈮鈩鈼鈫锛鈭銆'
PRE = {c: (c.encode('gbk') if _try(c) else b'') for c in FAM} if False else {}
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


def md_plain_map(s):
    """md → 折叠空白后的文本 + 每个字符对应的原偏移"""
    out = []; mp = []; prev_sp = False
    for i, ch in enumerate(s):
        if ch.isspace():
            if not prev_sp: out.append(' '); mp.append(i); prev_sp = True
        else:
            out.append(ch); mp.append(i); prev_sp = False
    return ''.join(out), mp


work = json.load(io.open(os.path.join(D, '_moji_files.json'), encoding='utf-8'))
fixed = 0; cand_bad = 0; files = 0; samples = []
for topic, p in work:
    U = up_plain(topic)
    if not U: continue
    s = T.read(p)
    if not any(c in s for c in FAM): continue
    A, mp = md_plain_map(s)
    sm = difflib.SequenceMatcher(None, U, A, autojunk=False)
    edits = []          # (orig_start, orig_end, 新字)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': continue
        seg = A[j1:j2]
        if not any(c in FAM for c in seg): continue          # md 侧这处没有坏字
        up = U[i1:i2].replace(' ', '')
        if len(up) != 1: continue                            # 判据①：上游侧恰好一个字
        # 逐个坏字处理（一段里可能不止一个）
        k = 0
        for off, ch in enumerate(seg):
            if ch not in FAM: continue
            if ok_char(ch, up): 
                a0, a1 = mp[j1 + off], mp[j1 + off] + 1
                # 连同后面的 `?` 一起吃掉
                while a1 < len(s) and s[a1] == '?': a1 += 1
                edits.append((a0, a1, up)); fixed += 1
                if len(samples) < 6: samples.append((A[max(0,j1+off-12):j1+off], ch, up))
            else:
                cand_bad += 1
    if edits:
        out = []; cur = 0
        for a0, a1, ch in sorted(edits, key=lambda x: -x[0]):
            if a1 <= cur: continue
            out.append((a0, a1, ch))
        txt = s
        for a0, a1, ch in sorted(out, key=lambda x: -x[0]):
            txt = txt[:a0] + ch + txt[a1:]
        io.open(p, 'w', encoding='utf-8', newline='').write(txt); files += 1

print(f'修复 {fixed} 处 / {files} 篇；候选被字节判据挡下 {cand_bad} 处')
print('样例:', samples)
if fixed:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'表外乱码·整篇对齐：修 {fixed} 处 / {files} 篇'],
                   cwd=T.TDC, capture_output=True)
    print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC,
                         capture_output=True, text=True, encoding='utf-8').stdout.strip())
