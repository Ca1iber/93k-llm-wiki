#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""G 类修复：**符号 / 公式上标**的转换损失，**按层处置**。

规矩（2026-09-23 用户定）：**哪一层错就改哪一层。**
- `raw/` 自己写错 → **改 raw**（下面 `RAW_FIX`，**具名 + 写明证据**）
- `raw/` 是对的、markdown 丢了上标 → **改 markdown**

**不靠通用正则判「raw 有没有错」**——那会把正常写法卷进来。
第一版的正则就把 **1,237 个脚注标记** `<sup>1)</sup>` 判成了缺陷。
改成**逐条具名**：每条都要说得出「凭什么说它错」（通常是**同一文件里别处的写法**）。

用法：
    python -X utf8 fix_corpus_superscript_symbol.py            # 空跑
    python -X utf8 fix_corpus_superscript_symbol.py --apply    # 真改
"""
import re, sys, json, html, pathlib

WIKI = pathlib.Path(r'F:\master-dev\understand-anything-wiki')
CORPUS = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html')
MD, HT = CORPUS / 'agent-markdown' / 'by-category', CORPUS / 'raw'
APPLY = '--apply' in sys.argv

BODY = re.compile(r'<body\b[^>]*>(.*)</body\s*>', re.I | re.S)
TAG = re.compile(r'<[^>]+>')
A_TAG = re.compile(r'<a\b[^>]*>.*?</a\s*>', re.I | re.S)
SUP = re.compile(r'<sup\b[^>]*>(.*?)</sup\s*>', re.I | re.S)
FOOT = re.compile(r'^[\dA-Za-z]{1,3}\)$')
NOT_EXP = re.compile(r'^(\[[a-zA-Z]\]|TM|®|©)$')

# ── 一层：raw 自己写错 —— **具名，逐条有据** ────────────────────
# 判据不是「我觉得」，是**同一文件里别处的写法**（或显而易见的标点错位）。
RAW_FIX = [
    ('98749.htm', '2<sup>32-1</sup>', '2<sup>32</sup>-1',
     '同文件另有 12 处写 `2<sup>31</sup>-1`（`-1` 在上标外）——此处 `-1` 被包进去了'),
    ('98749.htm', '2<sup>16-1</sup>', '2<sup>16</sup>-1', '同上'),
    ('98749_2.htm', '2<sup>32-1</sup>', '2<sup>32</sup>-1', '同上（重投件）'),
    ('98749_2.htm', '2<sup>16-1</sup>', '2<sup>16</sup>-1', '同上'),
    ('125001.htm', '(2<sup>n).</sup>', '(2<sup>n</sup>).',
     '`)` `.` 被包进上标，渲染成 2 的「n).」次方'),
    ('125003.htm', '(2<sup>n).</sup>', '(2<sup>n</sup>).', '同上（重投件）'),
]

# ── 二层：**纯数字里要破例处理的**（具名）──────────────────────
# 这 4 处是**我自己的 raw 修复造出来的**：`2<sup>32-1</sup>` → `2<sup>32</sup>`
# 之后上标成了纯数字 `32`，被「纯数字 = A/D 已处置」那条跳过，可 md 还是 `232-1`。
MD_FORCE = {('98749.htm', '32'), ('98749.htm', '16'),
            ('98749_2.htm', '32'), ('98749_2.htm', '16')}

# ── 二层：md 里**不该动**的（具名，写明理由）────────────────────
MD_SKIP = {
    ('118592.htm', 'xj'): '该篇把 `<sup>` 当**下标**用（`c1*x1` / `x3` / `x0`），展平是对的',
    ('118592.htm', 'xj-1'): '同上——`c<sup>j-1</sup>*x<sup>j-1</sup>` 是下标 j-1',
    ('46266.htm', 'yx'): '「y^x 序列」还是「y_x 序列」判不出 → **停下问人**',
    ('344019.htm', '2n-1'):
        'raw 写 `2<sup>n-1</sup>` = 2^(n-1)，**raw 是对的**；写成 `2^n-1` 会读错，'
        '得写 `2^(n-1)`——**这个写法要人定**（语料现有约定是 `(Hz)^1/2`，括号包底数不包指数）',
}


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


def scan_md():
    """扫 markdown 丢上标的处。**必须在 raw 修完之后跑**（`n).` 那种改完才知道指数是 `n`）。"""
    stem2md = {}
    for p in MD.rglob('*.md'):
        t, _ = rd(p)
        m = re.search(r'^source_topic:\s*["\']?([^"\'\s]+)', t, re.M)
        if m:
            stem2md.setdefault(m.group(1).replace('.htm', '').replace('.html', ''), []).append(p)
    hits, skipped = [], []
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
            # 纯数字（A、D 类）默认跳过。**但有具名例外 MD_FORCE**：
            # raw 的 `2<sup>32-1</sup>` 被修成 `2<sup>32</sup>` 之后，上标内容就成了纯数字，
            # 会被这一条顺带跳过，而它的 md（`232-1`）还没改——**漏改 4 处**。
            #
            # **修法是具名列出这 4 处，不是放宽判据。** 试过放宽成「看 md 里还有没有
            # 粘连形态」，一下卷进来 **91 处**——`I<sup>2</sup>`、`m<sup>2</sup>`、
            # `x<sup>5</sup>` 全进来了，那是**表里 B/E 类待判的那批**，不是 G。
            # **想用放宽判据去兜几个具体处，就会把它没打算管的东西一起兜进来。**
            is_num = bool(re.fullmatch(r'[+\-\u2212]?\d{1,3}', inner))
            if is_num and (f.name, inner) not in MD_FORCE:
                continue
            head = seg[max(0, mm.start() - 400):mm.start()]
            if A_TAG.search(head[-200:]):
                skipped.append((f.name, inner, '脚注（<a> 包裹）'))
                continue
            if FOOT.match(inner) or NOT_EXP.match(inner):
                skipped.append((f.name, inner, '脚注 / 引用 / 商标'))
                continue
            if re.fullmatch(r'(st|nd|rd|th)', inner, re.I):
                skipped.append((f.name, inner, '序数后缀（本来就对）'))
                continue
            pre = seg[:mm.start()]
            b = html.unescape(TAG.sub('', pre[-8:])).rstrip()
            if not b:
                continue
            base, lit = b[-1], b[-1] + inner
            if (f.name, lit) in MD_SKIP:
                skipped.append((f.name, lit, '★ 具名排除：' + MD_SKIP[(f.name, lit)]))
                continue
            pre_h = norm(TAG.sub('', pre))[:-1].rstrip()
            for md in mds:
                txt, _ = rd(md)
                ctx = lambda o: norm(txt[max(0, o - 200):o])
                offs = [om.start() for om in re.finditer(re.escape(lit), txt)
                        if any(pre_h[-k:] == ctx(om.start())[-k:] for k in range(50, 9, -1)
                               if k <= len(pre_h) and k <= len(ctx(om.start())))]
                if len(offs) != 1:
                    skipped.append((md.name, lit, f'定位到 {len(offs)} 处，需人工'))
                    continue
                hits.append((md, offs[0], base, inner, lit, f.name, txt))
    return hits, skipped


print('【一层】raw 自己写错 —— 具名清单：')
for f, a, b, why in RAW_FIX:
    print(f'    {f:<15} {a}  →  {b}')
    print(f'        └ {why}')

hits, skipped = scan_md()
print(f'\n【二层】markdown 丢上标：{len(hits)} 处 / {len({h[0] for h in hits})} 篇')
for md, off, base, inner, lit, hf, txt in sorted(hits, key=lambda h: str(h[0])):
    print(f'    {md.name[:52]:<54} {lit} → {base}^{inner}   ({hf})')

print(f'\n【排除】{len(skipped)} 处')
agg = {}
for n, inner, why in skipped:
    agg.setdefault(why.split('：')[0], []).append(f'{n[:38]}:{inner}')
for why, ex in sorted(agg.items(), key=lambda kv: -len(kv[1])):
    print(f'    {why:<28} {len(ex):>4} 处   例 {ex[0]}')

if not APPLY:
    print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
    sys.exit(0)

# ── 先改 raw，再扫 md（顺序不能反）──────────────────────────────
for f, a, b, _ in RAW_FIX:
    p = HT / f
    t, _ = rd(p)
    if b in t and a not in t:
        continue                                  # 已经改过（脚本可重跑）
    assert t.count(a) == 1, f'{f}: {a!r} 命中 {t.count(a)} 次'
    p.write_bytes(t.replace(a, b, 1).encode('utf-8'))
print(f'[已改 raw] {len(RAW_FIX)} 处')

hits, _ = scan_md()
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
print(f'[已改 md] {changed} 处 / {len(per)} 篇')

# ★ **清单要合并，不能只写本次结果。**
# 本批跑了两轮 --apply（先 14 处 md、后 4 处），第二轮把第一轮的 14 条**覆盖掉了**——
# 清单只剩 10 条。**和 `_assign.json` 被空表覆盖是同一类毛病。**
# 合并键：层 + 文件 + 改前形态。
_AP = WIKI / 'extract' / '_assign_symbol.json'
_new = ([dict(layer='raw', file=f, before=a, after=b, why=why) for f, a, b, why in RAW_FIX] +
        [dict(layer='md', md=str(md), offset=off, base=base, exp=inner, lit=lit, html=hf,
              rel=md.relative_to(MD).as_posix()) for md, off, base, inner, lit, hf, _ in hits])
_old = json.loads(_AP.read_text(encoding='utf-8')) if _AP.exists() else []
_merged, _seen = [], set()
for _e in _new + _old:
    # ★ 键里必须带 offset：同一文件里**两处形态相同**时（`37494.htm` 有两个 `n^m`），
    # 不带 offset 就会被并成一条——**去重键不够唯一 = 静默丢条目**。
    _k = (_e['layer'], _e.get('md') or _e.get('file'),
          _e.get('lit') or _e.get('before'), _e.get('offset'))
    if _k in _seen:
        continue
    _seen.add(_k)
    _merged.append(_e)
_AP.write_text(json.dumps(_merged, ensure_ascii=False, indent=0), encoding='utf-8')
print(f'清单合并后 {len(_merged)} 条（本次 {len(_new)} + 已有 {len(_old)}）')
print('清单 → extract/_assign_symbol.json')
