# -*- coding: utf-8 -*-
"""给「描述语料里表格被压平」的那些页加一句标准说明 —— 不改原有文字。"""
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
WIKI = r"F:\master-dev\understand-anything-wiki\wiki"
KW = ('被拍平', '被摊平', '被压平', '一格一行')
NOTE = [
    '> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**',
    '> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**',
    '> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /',
    '> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，',
    '> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**',
    '',
]
n = 0
for dp, _, fns in os.walk(WIKI):
    for fn in fns:
        if not fn.endswith('.md'): continue
        p = os.path.join(dp, fn)
        if fn in ('log.md', 'index.md') or fn.startswith('index-'): continue
        s = io.open(p, encoding='utf-8', errors='replace').read()
        if not any(k in s for k in KW): continue
        if s.startswith('> ⚠️ **本页若干处记的是'): continue
        if '本页若干处记的是 2026-10-10' in s: continue
        m = re.match(r'^---\n.*?\n---\n', s, re.S)
        if not m: continue
        ins = m.end()
        out = s[:ins] + '\n' + '\n'.join(NOTE) + s[ins:]
        io.open(p, 'w', encoding='utf-8', newline='').write(out)
        n += 1
print(f'加了标准说明 {n} 篇')
