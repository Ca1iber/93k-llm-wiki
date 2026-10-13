# -*- coding: utf-8 -*-
"""链接文字里的乱码：真相就在【目标篇的 title:】里（实测那里是干净的）。
逐字符同步走：md 侧遇到坏字（连同 `?`/私用区残渣）时，从 title 侧取一个字。
仍走第二条判据：候选必须与坏字的 GBK 字节对得上。"""
import io, os, re, sys, json, subprocess
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
fixed = 0; files = 0; bad = 0; samples = []
for topic, p in json.load(io.open(os.path.join(D, '_moji_files.json'), encoding='utf-8')):
    s = T.read(p)
    if not re.search('[' + FAM + ']', s): continue
    repl = []
    for m in re.finditer(r'\[([^\]]*)\]\(' + r'<([^>]+)>' + r'\)', s):
        txt, tgt = m.group(1), m.group(2)
        if not re.search('[' + FAM + ']', txt): continue
        tp = os.path.normpath(os.path.join(os.path.dirname(p), tgt))
        if not os.path.exists(tp): continue
        ti = re.search(r'^title:\s*"(.*?)"', T.read(tp), re.M)
        if not ti: continue
        ti = ti.group(1)
        out = []; i = j = 0
        while i < len(txt):
            if txt[i] in FAM:
                bad_c = txt[i]
                i += 1
                while i < len(txt) and (txt[i] == '?' or 0xE000 <= ord(txt[i]) <= 0xF8FF): i += 1
                # title 侧取一个字（跳过空白）
                while j < len(ti) and ti[j].isspace(): out.append(ti[j]); j += 1
                if j < len(ti) and ok(bad_c, ti[j]):
                    out.append(ti[j]); j += 1
                    if len(samples) < 6: samples.append((txt[:40], bad_c, ti[j-1]))
                else:
                    bad += 1; out.append(bad_c)
            else:
                out.append(txt[i]); i += 1
                if j < len(ti) and ti[j] == txt[i - 1]: j += 1
        new = ''.join(out)
        if new != txt: repl.append((m.start(1), m.end(1), new))
    if repl:
        t2 = s
        for a0, a1, new in sorted(repl, key=lambda x: -x[0]): t2 = t2[:a0] + new + t2[a1:]
        io.open(p, 'w', encoding='utf-8', newline='').write(t2)
        fixed += len(repl); files += 1

print(f'改了 {fixed} 条链接 / {files} 篇；候选不合字节区间 {bad}')
for x in samples: print('   ', x)
if fixed:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'链接文字乱码：从目标篇 title 取正字，改 {fixed} 条 / {files} 篇'],
                   cwd=T.TDC, capture_output=True)
    print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                         text=True, encoding='utf-8').stdout.strip())
