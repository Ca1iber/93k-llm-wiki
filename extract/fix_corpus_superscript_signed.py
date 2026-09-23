#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""D 类修复：带符号指数被拍平——`10<sup>-9</sup>` → `10-9`（读成「10 减 9」）。

与 A 类**同一个机制**，只是上标内容带正负号，所以 A 类那个脚本的正则
（`\\d{1,3}`）漏掉了这 3 处。判据、定位算法与 `fix_corpus_superscript.py` 一致。

用法：
    python -X utf8 fix_corpus_superscript_signed.py            # 空跑
    python -X utf8 fix_corpus_superscript_signed.py --apply    # 真改

依据：schema.md §1.2。上游唯一，逐字对得出来。
"""
import re, sys, json, html, pathlib

WIKI = pathlib.Path(r'F:\master-dev\understand-anything-wiki')
CORPUS = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html')
MD, HT = CORPUS / 'agent-markdown' / 'by-category', CORPUS / 'raw'
EVID = WIKI / 'extract' / 'findings-corpus-superscript-loss-evidence-signed.md'
ASSIGN = WIKI / 'extract' / '_assign_signed.json'
APPLY = '--apply' in sys.argv

def guard(path, n, what):
    """**互锁：不许用空结果覆盖非空产物。**

    这个坑咬过两次：`fix_corpus_superscript.py` 把 151 条清单清空过；
    它的 G 版又被第二轮的少结果盖过一次。**修的时候只修了咬人的那一个，
    所以换一个脚本就又咬一次**——现在三处统一。
    """
    if n or not path.exists() or path.stat().st_size == 0:
        return True
    print(f'\n⛔ 拦截：本次{what}为 0 条，而 {path.name} 已有 '
          f'{path.stat().st_size:,} 字节——**拒绝用空结果覆盖**。')
    return False


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

hits = []
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
            offs = [om.start() for om in re.finditer(re.escape(lit), txt)
                    if (lambda pm: any(pre_h[-k:] == pm[-k:] for k in range(50, 9, -1)
                                       if k <= len(pre_h) and k <= len(pm)))(
                        norm(txt[max(0, om.start() - 200):om.start()]))]
            # **必须唯一**——两处以上就停下问人，不猜（A 类那次「串」的教训）
            # ★ **0 处 = 已经修过了**，跳过；不能断言。
            # 第一版直接 assert ==1，修完再跑必崩——**脚本不可重跑**，
            # 而它没覆盖产物只是**因为崩在写盘之前**，不是因为有防护。
            if not offs:
                continue
            assert len(offs) == 1, f'{md.name}: `{lit}` 命中 {len(offs)} 处，需人工判位置'
            hits.append((md, offs[0], base, inner, lit, f.name, txt))

print(f'上游 <sup> 带符号命中：{len(hits)} 处 / {len({h[0] for h in hits})} 篇')
for md, off, base, inner, lit, hf, txt in hits:
    print(f'  {md.name[:56]:<58} {lit} → {base}^{inner}   ({hf})')

if not hits:
    sys.exit(0)

rows = []
for md, off, base, inner, lit, hf, txt in hits:
    L = len(lit)
    before = txt[max(0, off - 60):off + L + 30].replace('\r', ' ').replace('\n', ' ')
    after = (txt[max(0, off - 60):off] + base + '^' + inner + txt[off + L:off + L + 30]
             ).replace('\r', ' ').replace('\n', ' ')
    rows.append((md.relative_to(MD).as_posix(), hf, f'{base}^{inner}', before, after))

if not guard(EVID, len(rows), '证据表'):
    print('   （什么都没写。）')
    sys.exit(2)

with EVID.open('w', encoding='utf-8', newline='\n') as fh:
    fh.write('# D 类修复证据表 —— 带符号指数被拍平（`10<sup>-9</sup>` → `10-9`）\n\n')
    fh.write('与 A 类**同一个机制**，只是上标带正负号，A 类的正则（`\\d{1,3}`）漏掉了它们。\n')
    fh.write('**只改 markdown，HTML 不动。**判据与流程见 `schema.md` §1.2。\n\n')
    fh.write(f'共 **{len(rows)}** 处。\n\n')
    fh.write('| # | markdown | 源 HTML | 指数 | 改前 | 改后 |\n|---|---|---|---|---|---|\n')
    for i, (rel, hf, ex, b, a) in enumerate(rows, 1):
        q = lambda s: '`' + s.replace('|', '\\|') + '`'
        fh.write(f'| {i} | `{rel}` | `{hf}` | `{ex}` | {q(b)} | {q(a)} |\n')
print(f'证据表 → {EVID}')

# ★ **清单要合并，不能只写本次结果。** 跑两轮时，第二轮会把第一轮盖掉。
# 键里必须带 `offset`——同文件里两处形态相同时，不带会**静默丢条目**。
_new = [dict(layer='md', md=str(md), offset=off, base=base, exp=inner, lit=lit, html=hf,
             rel=md.relative_to(MD).as_posix()) for md, off, base, inner, lit, hf, _ in hits]
_old = json.loads(ASSIGN.read_text(encoding='utf-8')) if ASSIGN.exists() else []
_merged, _seen = [], set()
for _e in _new + _old:
    _k = (_e['layer'], _e['md'], _e['lit'], _e['offset'])
    if _k in _seen:
        continue
    _seen.add(_k)
    _merged.append(_e)
if _merged:
    ASSIGN.write_text(json.dumps(_merged, ensure_ascii=False, indent=0), encoding='utf-8')
    print(f'清单 {len(_merged)} 条（本次 {len(_new)} + 已有 {len(_old)}）')
else:
    print('清单：本次 0 条且已有为空，不写。')

if not APPLY:
    print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
    sys.exit(0)

per = {}
for md, off, base, inner, lit, hf, txt in hits:
    per.setdefault(md, (txt, []))[1].append((off, base, inner, lit))
changed = 0
for md, (txt, items) in sorted(per.items(), key=lambda kv: str(kv[0])):
    if txt.encode('utf-8') != md.read_bytes():
        print(f'  !! 跳过（utf-8 往返不安全）：{md.name}')
        continue
    for off, base, inner, lit in sorted(items, key=lambda x: -x[0]):
        assert txt[off:off + len(lit)] == lit, f'{md.name}@{off} 期望 {lit!r}'
        txt = txt[:off] + base + '^' + inner + txt[off + len(lit):]
        changed += 1
    md.write_bytes(txt.encode('utf-8'))
print(f'\n[已改] {changed} 处 / {len(per)} 篇')
