# -*- coding: utf-8 -*-
"""第一步：只扫出「含坏字的文件」名单，落盘。不读上游、不占内存。"""
import io, os, sys, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T
FAM = '鈥鈮鈩鈼鈫锛鈭銆'
out = []
for dp, _, fns in os.walk(T.MD):
    for fn in fns:
        if not fn.endswith('.md'): continue
        p = os.path.join(dp, fn)
        s = T.read(p)
        if any(c in s for c in FAM):
            m = re.search(r'source_topic:\s*"([^"]+)"', s)
            out.append([m.group(1) if m else '', p])
io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_moji_files.json'),
        'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False))
print(f'含坏字的文件 {len(out)} 篇 → _moji_files.json')
