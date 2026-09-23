#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""
A 类语料修复：把 HTML→markdown 转换时被拍平的数字上标补回 `^`。

依据：schema.md §1.2（2026-09-22 立，人批准）。
上游对证：tdc-html/raw/ 的 HTML 里明写着 <sup>NN</sup>，markdown 里成了粘连字面量。
只改 agent-markdown/。**raw/ 的 HTML 一个字不动。**

用法：
    python -X utf8 fix_corpus_superscript.py            # 空跑，只报数、只出证据表
    python -X utf8 fix_corpus_superscript.py --apply    # 真改

改法：`2<sup>48</sup>` → `2^48`。
选 `^` 的依据（不是偏好，是语料自己的写法）：语料里已有 11 篇 / 64 处这样写指数
（`x^2+x^4+...`、`I^2`、`(Hz)^1/2`）；Unicode 上标 0 篇，行内 <sup> 0 篇。
"""
import re, sys, json, html, pathlib, hashlib

WIKI = pathlib.Path(r'F:\master-dev\understand-anything-wiki')
CORPUS = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html')
MD = CORPUS / 'agent-markdown' / 'by-category'
HT = CORPUS / 'raw'
EVID = WIKI / 'extract' / 'findings-corpus-superscript-loss-evidence.md'
APPLY = '--apply' in sys.argv

BODY = re.compile(r'<body\b[^>]*>(.*)</body\s*>', re.I | re.S)
TAG = re.compile(r'<[^>]+>')
SUP = re.compile(r'<sup\b[^>]*>(.*?)</sup\s*>', re.I | re.S)


def guard(path, n, what):
    """**互锁：不许用空结果覆盖非空清单。**

    2026-09-22 真发生过。修复完成后再空跑一次，151 处全报「未定位」，
    于是 `_assign.json` 与证据表**被覆盖成空**——两份都是未追踪文件，**git 救不回**。
    根因：产物写盘在 `if not APPLY` 判断**之前**。

    **不能简单地把写盘挪进 `--apply`**——空跑本来就该出证据表给人核对，
    挪进去等于把这个用处砍掉。所以改成**只拦空结果**：
    非空照写（可相互覆盖），空的而目标已有内容 → **拦下并报错**。

    这条规矩针对的是「空表覆盖」这一类，不是某一次事故：
    任何一次「以为在核对、其实在清空」都会撞上它。
    """
    if n or not path.exists() or path.stat().st_size == 0:
        return True
    print(f'\n⛔ 拦截：本次{what}为 0 条，而 {path.name} 已有 '
          f'{path.stat().st_size:,} 字节——**拒绝用空结果覆盖**。')
    print(f'   确要清空，先手工删掉 {path.name} 再跑。')
    return False


def mdplain(s):
    """把 markdown 的行内标记抹平，只留文字——比较上下文用，不用来定位。"""
    s = re.sub(r'\[([^\]]*)\]\(\s*<[^>]*>\s*\)', r'\1', s)
    s = re.sub(r'\[([^\]]*)\]\(\s*[^)\s]*\)', r'\1', s)
    for ch in '**__`|':
        s = s.replace(ch, ' ')
    return s


def norm(s):
    return re.sub(r'\s+', ' ', mdplain(html.unescape(s))).strip()


def rd(p):
    raw = p.read_bytes()
    try:
        return raw.decode('utf-8'), raw
    except UnicodeDecodeError:
        return raw.decode('cp1252', 'replace'), raw


def loadseg(f):
    t, _ = rd(f)
    m = BODY.search(t)
    return m.group(1) if m else t


# ---------- 1. 映射 ----------
stem2md = {}
for p in MD.rglob('*.md'):
    t, _ = rd(p)
    m = re.search(r'^source_topic:\s*["\']?([^"\'\s]+)', t, re.M)
    if m:
        stem2md.setdefault(m.group(1).replace('.htm', '').replace('.html', ''), []).append(p)

# ---------- 2. 定位 ----------
events = []   # 每个 HTML <sup> 一条
for f in sorted(HT.glob('*.htm')) + sorted(HT.glob('*.html')):
    mds = stem2md.get(f.stem)
    if not mds:
        continue
    seg = loadseg(f)
    for mm in SUP.finditer(seg):
        inner = html.unescape(TAG.sub('', mm.group(1))).strip()
        if not re.fullmatch(r'\d{1,3}', inner):
            continue
        pre = seg[:mm.start()]
        b = html.unescape(TAG.sub('', pre[-8:])).rstrip()
        if not b or not b[-1].isdigit():
            continue
        base, lit = b[-1], b[-1] + inner
        pre_h = norm(TAG.sub('', pre))[:-1].rstrip()
        for md in mds:
            txt, _ = rd(md)
            cands = []
            for om in re.finditer(re.escape(lit), txt):
                pre_m = norm(txt[max(0, om.start() - 200):om.start()])
                for n in range(50, 9, -1):
                    if n <= len(pre_h) and n <= len(pre_m) and pre_h[-n:] == pre_m[-n:]:
                        cands.append((n, om.start()))
                        break
            if not cands:
                # 兜底：上文尾部有乱码（`…` 被毁成 `鈥?`）→ 把尾部非 ASCII 部分切掉当锚，
                # 再取锚后 25 字符内的第一个 lit。
                tail = pre_h[-60:]
                cut = next((i for i, ch in enumerate(tail) if ord(ch) > 127), len(tail))
                anchor = tail[:cut].rstrip()
                for L in range(len(anchor), 3, -1):
                    k = txt.find(anchor[-L:])
                    if k < 0:
                        continue
                    j = txt.find(lit, k + L - 1, k + L + 25)
                    if j >= 0:
                        cands = [(L, j)]
                        break
            events.append(dict(md=md, base=base, exp=inner, lit=lit,
                               hf=f.name, pre_h=pre_h, cands=cands, txt=txt))

# ---------- 3. 消歧 ----------
assign = {}      # (md, offset) -> event
byctx = {}
unresolved = []
for e in events:
    if len(e['cands']) == 1:
        o = e['cands'][0][1]
        if (e['md'], o) in assign:
            raise SystemExit(f'冲突：{e["md"].name} @{o} 被两处争用')
        assign[(e['md'], o)] = e
    elif not e['cands']:
        unresolved.append(e)
    else:
        key = (e['md'], e['base'], e['exp'], tuple(sorted(c[1] for c in e['cands'])))
        byctx.setdefault(key, []).append(e)

for key, es in byctx.items():
    offs = sorted(key[3])
    if len(es) == len(offs) and offs:      # 同一句在文档里出现 N 遍，N 处都要改
        for e, o in zip(es, offs):
            e['cands'] = [(50, o)]
            assign[(e['md'], o)] = e
    else:
        unresolved += es

print(f'HTML 侧 <sup> 命中        : {len(events)} 处')
print(f'  已定位（可改）          : {len(assign)} 处')
print(f'  未定位（**不改**）      : {len(unresolved)} 处')
print(f'  涉及 markdown           : {len({k[0] for k in assign})} 篇')
for e in unresolved:
    print(f'    !! {e["md"].name[:50]:<52} {e["base"]}^{e["exp"]:<4} ({e["hf"]}) 候选{len(e["cands"])}')

# ---------- 4. 证据表 ----------
rows = []
for (md, off), e in sorted(assign.items(), key=lambda kv: (str(kv[0][0]), kv[0][1])):
    t = e['txt']
    L = len(e['lit'])
    before = t[max(0, off - 60):off + L + 30].replace('\r', ' ').replace('\n', ' ')
    after = (t[max(0, off - 60):off] + e['base'] + '^' + e['exp'] + t[off + L:off + L + 30]
             ).replace('\r', ' ').replace('\n', ' ')
    rows.append((md.relative_to(MD).as_posix(), e['hf'], f'{e["base"]}^{e["exp"]}', before, after))

if not guard(EVID, len(rows), '证据表') or not guard(WIKI / 'extract' / '_assign.json',
                                                       len(assign), '清单'):
    print('   （什么都没写，语料也没动。）')
    sys.exit(2)

with EVID.open('w', encoding='utf-8', newline='\n') as fh:
    fh.write('# A 类修复证据表 —— 151 处「数字上标被拍平」逐处对照\n\n')
    fh.write('上游：`tdc-html/raw/*.htm` 的 `<sup>NN</sup>`；下游：`agent-markdown/by-category/*.md`。\n')
    fh.write('**只改 markdown，HTML 不动**（HTML 是 A 类唯一的对证上游）。\n\n')
    fh.write(f'本次可定位并修复 **{len(rows)}** 处；未定位 {len(unresolved)} 处（见文末）。\n\n')
    fh.write('| # | markdown | 源 HTML | 指数 | 改前 | 改后 |\n|---|---|---|---|---|---|\n')
    for i, (rel, hf, ex, b, a) in enumerate(rows, 1):
        q = lambda s: '`' + s.replace('|', '\\|') + '`'
        fh.write(f'| {i} | `{rel}` | `{hf}` | `{ex}` | {q(b)} | {q(a)} |\n')
    if unresolved:
        fh.write('\n## 未定位（未改）\n\n')
        for e in unresolved:
            fh.write(f'- `{e["md"].name}` — `{e["base"]}^{e["exp"]}`（{e["hf"]}）'
                     f'候选 {len(e["cands"])} 个，需人工判位置\n')
print(f'\n证据表 → {EVID}')

# 机器可读的清单（供校验与日后重放）
(WIKI / 'extract' / '_assign.json').write_text(json.dumps(
    [dict(md=str(md), offset=off, base=e['base'], exp=e['exp'], lit=e['lit'],
          html=e['hf'], rel=md.relative_to(MD).as_posix())
     for (md, off), e in sorted(assign.items(), key=lambda kv: (str(kv[0][0]), kv[0][1]))],
    ensure_ascii=False, indent=0), encoding='utf-8')

# ---------- 5. 落盘 ----------
if not APPLY:
    print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
    sys.exit(0)

per = {}
for (md, off), e in assign.items():
    per.setdefault(md, []).append((off, e))
changed = 0
for md, items in sorted(per.items(), key=lambda kv: str(kv[0])):
    txt = items[0][1]['txt']
    if txt.encode('utf-8') != md.read_bytes():
        print(f'  !! 跳过（utf-8 往返不安全，含非法字节）：{md.name}')
        continue
    for off, e in sorted(items, key=lambda x: -x[0]):     # 从后往前，偏移不失效
        L = len(e['lit'])
        assert txt[off:off + L] == e['lit'], f'{md.name}@{off} 期望 {e["lit"]!r} 实得 {txt[off:off+L]!r}'
        txt = txt[:off] + e['base'] + '^' + e['exp'] + txt[off + L:]
        changed += 1
    md.write_bytes(txt.encode('utf-8'))
print(f'\n[已改] {changed} 处，涉及 {len(per)} 篇')
