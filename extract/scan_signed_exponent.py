#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""找「带符号指数」被拍平的处：上游 `<sup>-9</sup>`，下游粘连成 `10-9` 这类。

只**报告**，不改。这是 §1.2 五步的第 1 步（摆证据）。
判据、定位算法与 `fix_corpus_superscript.py` 一致——**同一套，不改判据**。
区别只有一个：上标内容允许带正负号（`-9` / `+3`），A 类那个脚本只认纯数字。
"""
import re, html, pathlib

CORPUS = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html')
MD, HT = CORPUS / 'agent-markdown' / 'by-category', CORPUS / 'raw'

BODY = re.compile(r'<body\b[^>]*>(.*)</body\s*>', re.I | re.S)
TAG = re.compile(r'<[^>]+>')
SUP = re.compile(r'<sup\b[^>]*>(.*?)</sup\s*>', re.I | re.S)


def rd(p):
    raw = p.read_bytes()
    try:
        return raw.decode('utf-8'), raw
    except UnicodeDecodeError:
        return raw.decode('cp1252', 'replace'), raw


def norm(s):
    s = re.sub(r'\[([^\]]*)\]\(\s*<[^>]*>\s*\)', r'\1', s)
    s = re.sub(r'\[([^\]]*)\]\(\s*[^)\s]*\)', r'\1', s)
    for ch in '**__`|':
        s = s.replace(ch, ' ')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


stem2md = {}
for p in MD.rglob('*.md'):
    t, _ = rd(p)
    m = re.search(r'^source_topic:\s*["\']?([^"\'\s]+)', t, re.M)
    if m:
        stem2md.setdefault(m.group(1).replace('.htm', '').replace('.html', ''), []).append(p)

found = 0
for f in sorted(HT.glob('*.htm')) + sorted(HT.glob('*.html')):
    mds = stem2md.get(f.stem)
    if not mds:
        continue
    t, _ = rd(f)
    m = BODY.search(t)
    seg = m.group(1) if m else t
    for mm in SUP.finditer(seg):
        inner = html.unescape(TAG.sub('', mm.group(1))).strip()
        if not re.fullmatch(r'[+\-\u2212]\d{1,3}', inner):     # ★ 只认带符号的
            continue
        pre = seg[:mm.start()]
        b = html.unescape(TAG.sub('', pre[-8:])).rstrip()
        if not b or not b[-1].isdigit():
            continue
        base, lit = b[-1], b[-1] + inner
        pre_h = norm(TAG.sub('', pre))[:-1].rstrip()
        for md in mds:
            txt, _ = rd(md)
            for om in re.finditer(re.escape(lit), txt):
                pre_m = norm(txt[max(0, om.start() - 200):om.start()])
                n = next((k for k in range(50, 9, -1)
                          if k <= len(pre_h) and k <= len(pre_m) and pre_h[-k:] == pre_m[-k:]), 0)
                if not n:
                    continue
                o = om.start()
                found += 1
                print(f'\n[{found}] {md.name}')
                print(f'    上游 {f.name}  : …{pre_h[-70:]}<{inner}>')
                print(f'    下游 markdown : …{txt[max(0,o-70):o].replace(chr(13)," ").replace(chr(10)," ")}'
                      f'[{lit}]…')
                print(f'    改后          : {base}^{inner}    锚 {n} 字符')
                break
print(f'\n共 {found} 处')
