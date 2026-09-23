#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""找 G 类：**符号 / 公式上标**的转换损失。只报不改（§1.2 第 1 步）。

「G」在分类表里是 1,255 处 / 218 篇，其中：
- **1,228 处是脚注标记**（`<sup>1)</sup>` → `1)`）——**忠实转换，不是损坏**，本脚本排除
- **27 处粘连**、**50 处整个丢了**——这两个才是要判的

本脚本按**「内容有没有进 markdown」**分：
- `丢了`：`<sup>` 的内容在下游找不到
- `粘连`：内容在，但紧贴在底字后面（无分隔）
- `分开`：内容在且正常书写 → 不是损坏

纯数字内容（A / D 类）与脚注标记（`\\d+\\)`）**直接排除**——它们已经处置过或本就不是病。
"""
import re, html, pathlib, collections

CORPUS = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html')
MD, HT = CORPUS / 'agent-markdown' / 'by-category', CORPUS / 'raw'

BODY = re.compile(r'<body\b[^>]*>(.*)</body\s*>', re.I | re.S)
TAG = re.compile(r'<[^>]+>')
SUP = re.compile(r'<sup\b[^>]*>(.*?)</sup\s*>', re.I | re.S)
FOOT = re.compile(r'^[\dA-Za-z]{1,3}\)$')          # 脚注标记：1) / a) / 12)


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

stats = collections.Counter()
rows = []
for f in sorted(HT.glob('*.htm')) + sorted(HT.glob('*.html')):
    mds = stem2md.get(f.stem)
    if not mds:
        continue
    t, _ = rd(f)
    m = BODY.search(t)
    seg = m.group(1) if m else t
    for mm in SUP.finditer(seg):
        inner = html.unescape(TAG.sub('', mm.group(1))).strip()
        if not inner:
            continue
        if re.fullmatch(r'\d{1,3}', inner):        # A / D 类：已处置
            stats['数字（A/D，已处置）'] += 1
            continue
        if FOOT.match(inner):                      # 脚注标记：忠实转换
            stats['脚注标记（不是损坏）'] += 1
            continue
        stats['符号/公式（G 候选）'] += 1
        pre_h = norm(TAG.sub('', seg[:mm.start()]))
        for md in mds:
            txt, _ = rd(md)
            # 定位：拿上游上文的最长后缀去 md 里找（同 A/D 的定位法）
            k, n = -1, 0
            for L in range(min(50, len(pre_h)), 9, -1):
                k = txt.find(pre_h[-L:])
                if k >= 0:
                    n = L
                    break
            if k < 0:
                rows.append((md, '定位失败', inner, f.name, pre_h[-45:]))
                continue
            p0 = k + n                                  # 底字之后的位置
            seg_md = txt[p0:p0 + 12]
            if inner[0] in seg_md[:6]:
                # ★ 粘连里必须再分：**序数后缀不是损坏**
                #   `3<sup>rd</sup>` → `3rd` 是**对的**（本来就是这么写）；
                #   `2<sup>n</sup>` → `2n` 才是损坏（读成「2 乘 n」）。
                #   不分开就会把 `3rd` 改成 `3^rd`——分类表 E 行的原话。
                cls = '粘连·序数后缀（不是损坏）' if re.fullmatch(r'(st|nd|rd|th)', inner, re.I) \
                    else '粘连·其它（候选）'
            elif inner in txt[p0:p0 + 200]:
                cls = '分开'                            # 内容在，但隔了点距离
            else:
                cls = '丢了·表格标记' if re.fullmatch(r'[●○◆■□▲△▽▼★☆]+', inner) \
                    else '丢了·其它'
            rows.append((md, cls, inner, f.name, pre_h[-45:]))

print('上游 <sup> 总览：')
for k, v in stats.most_common():
    print(f'  {k:<24} {v:>6}')

by = collections.Counter(r[1] for r in rows)
print('\nG 候选的处置分布：')
for k, v in by.most_common():
    print(f'  {k:<10} {v:>5}')

for cls in ('丢了·其它', '丢了·表格标记', '粘连·其它（候选）', '粘连·序数后缀（不是损坏）', '定位失败', '分开'):
    sel = [r for r in rows if r[1] == cls]
    if not sel:
        continue
    print(f'\n───── {cls}（{len(sel)} 处 / {len({r[0] for r in sel})} 篇）─────')
    for md, _, inner, hf, ctx in sel[:40]:
        print(f'  {md.name[:46]:<48} <{inner[:14]:<14}> ({hf})  …{ctx[-28:]}')
    if len(sel) > 40:
        print(f'  …还有 {len(sel)-40} 处')
