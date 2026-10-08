#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""语料修复（第二批）：**第三字节已丢**的那 8 族坏字，去上游 `.htm` 取正字。

用法：
    python -X utf8 extract/fix_corpus_mojibake2.py            # 空跑，只报数、只出证据表
    python -X utf8 extract/fix_corpus_mojibake2.py --apply    # 真改

## 病

第一批（120 族）的坏字**两个字节都还在**，`encode('gbk').decode('utf-8')` 就还原了。
这一批（8 族：`鈥` `鈮` `鈩` `鈼` `鈫` `锛` `鈭` `銆`）是**第三个字节被替换成了 `?`**，
信息**已经从 md 里永久丢了**：

  `≤` 是 `E2 89 A4`；按 GBK 读：`E2 89` → `鈮`，`A4` 凑不成合法对 → 写成 `?`。
  md 里剩 `鈮?` —— 只推得出「原字以 `E2 89` 开头」，那是 **64 个字**，定不出是哪个。

**只能去上游取。** 上游 `.htm` 没坏。

## 判据：三条独立校验叠加，缺一不可

1. **词锚定位**：拿坏字**前面那几个字母数字词**（`[A-Za-z0-9]+`）当锚。
   坏字是汉字，**天然不在字母数字词里** —— 所以锚**自动是干净的**
   （「整篇对齐」那版之前栽在「锚本身含坏字」上，这一条把那个洞堵死了）。
2. **锚必须全篇唯一命中**：那个词串在上游出现**恰好一次**才用。
   出现多次就放弃 —— 这一条堵死「同段文字重复时挑错」。
3. **坏字的字节自己定死区间**：`鈮`.encode('gbk') = `E2 89` → 原字必然是 `E2 89 XX`，
   即 **U+2240–U+227F**。候选**必须落在区间里**。
   这一条挡掉只看对齐时冒出来的假货（实测 `鈥 → '/'`，而 `/` 是 ASCII）。

## 只自动修「干净」的那些

有的位置坏字后面**还粘着被吃剩的实体残渣**（上游 `…&nbsp;` 在 md 里成了 `鈥?nbsp;`）。
直接换成 `…` 会**留下一个孤零零的 `nbsp;`** —— 那比不改更坏。
所以**只有「md 侧那一段恰好是 `坏字` + `?`」的才自动改**，其余一律不碰、报出来。

## 产物

- `extract/_assign_mojibake2.json`、`extract/findings-corpus-mojibake2-evidence.md`
"""
import json
import pathlib
import re
import sys

WIKI = pathlib.Path(r'F:\master-dev\understand-anything-wiki')
CORPUS = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html')
MD = CORPUS / 'agent-markdown' / 'by-category'
RAW = CORPUS / 'raw'
EVID = WIKI / 'extract' / 'findings-corpus-mojibake2-evidence.md'
ASSIGN = WIKI / 'extract' / '_assign_mojibake2.json'
APPLY = '--apply' in sys.argv

BAD = '鈥鈮鈩鈼鈫锛鈭銆'
BADRX = re.compile('[' + BAD + ']')
TAG = re.compile(r'<[^>]+>')
WORD = re.compile(r'[A-Za-z0-9]+')
KG = (8, 6, 5, 4, 3)          # 依次试的锚长度（词数）


def guard(path, n, what):
    if n or not path.exists() or path.stat().st_size == 0:
        return True
    print(f'\n⛔ 拦截：本次{what}为 0 条，而 {path.name} 已有 '
          f'{path.stat().st_size:,} 字节——**拒绝用空结果覆盖**。')
    return False


def htm_plain(p):
    t = p.read_bytes().decode('utf-8', 'replace')          # ★ 同上
    t = re.sub(r'(?is)<(script|style|head)\b.*?</\1>', ' ', t)
    t = TAG.sub(' ', t)
    for a, b in (('&nbsp;', '\u00a0'), ('&le;', '≤'), ('&ge;', '≥'), ('&amp;', '&'),
                 ('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'), ('&#39;', "'"),
                 ('&sup2;', '²'), ('&sup3;', '³'), ('&deg;', '°')):
        t = t.replace(a, b)
    return re.sub(r'\s+', ' ', t)


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    clean, messy, noanchor, nohtml = [], [], 0, 0

    for p in sorted(MD.rglob('*.md')):
        orig = p.read_bytes().decode('utf-8', 'replace')   # ★ 不用 read_text：它会把 CRLF 悄悄转成 LF
        if not BADRX.search(orig):
            continue
        m = re.search(r'^source_topic:\s*["\']?([^"\'\s]+)', orig, re.M)
        h = RAW / f"{m.group(1).replace('.htm', '')}.htm" if m else None
        if not h or not h.exists():
            nohtml += 1
            continue
        hp = htm_plain(h)
        # 上游的词 → 位置，以及 K 词串 → 位置表（每篇建一次）
        hw = [(x.group(0), x.start()) for x in WORD.finditer(hp)]
        hwords = [w for w, _ in hw]
        idx = {}
        for K in KG:
            d = {}
            for i in range(len(hwords) - K + 1):
                d.setdefault(' '.join(hwords[i:i + K]), []).append(i)
            idx[K] = d
        mw = [(x.group(0), x.start()) for x in WORD.finditer(orig)]

        for mm in BADRX.finditer(orig):
            pos = mm.start()
            # 坏字前面那几个字母数字词 —— **天然的干净锚**
            before = [w for w, o in mw if o < pos]
            hit = None
            for K in KG:
                if len(before) < K:
                    continue
                key = ' '.join(before[-K:])
                lst = idx[K].get(key, [])
                if len(lst) == 1:                    # ★ 必须全篇唯一
                    i = lst[0]
                    after = hw[i + K - 1][1] + len(hw[i + K - 1][0])
                    hit = hp[after:after + 24]
                    break
            if hit is None:
                noanchor += 1
                continue
            cand = hit.lstrip()[:1]
            b = mm.group(0).encode('gbk')
            lo = ((b[0] & 0x0F) << 12) | ((b[1] & 0x3F) << 6)
            if not (len(cand) == 1 and lo <= ord(cand) <= lo + 0x3F):
                messy.append((p, orig[pos:pos + 3], cand, '区间/取值不过'))
                continue
            run = orig[pos:pos + 2]
            if not re.fullmatch('[' + BAD + r']\?', run):
                messy.append((p, run, cand, 'md 侧带残渣'))
                continue
            clean.append((p, run, cand))

    print(f'✅ 干净可修（锚唯一 + 区间过 + md 侧恰好「坏字+?」）: **{len(clean):,} 处**')
    print(f'⚠️ 定位不到（锚不唯一 / 太短）                      : {noanchor:,} 处')
    print(f'⚠️ 定位到了但不能改（残渣 / 区间不过）              : {len(messy):,} 处')
    print(f'   没有 source_topic / htm 不在                      : {nohtml}')
    print()
    for p, a, b, w in messy[:6]:
        print(f'   （不动）{p.name[:34]:<36} {a!r:<10} 候选={b!r:<4} {w}')

    rows = []
    for p, bad, good in sorted(clean, key=lambda x: str(x[0])):
        t = p.read_bytes().decode('utf-8', 'replace')          # ★ 同上
        i = t.find(bad)
        rows.append((p.relative_to(MD).as_posix(), bad, good,
                     t[max(0, i - 50):i + 20].replace('\r', ' ').replace('\n', ' ')))

    if not guard(EVID, len(rows), '证据表') or not guard(ASSIGN, len(rows), '清单'):
        print('   （什么都没写，语料也没动。）')
        sys.exit(2)

    with EVID.open('w', encoding='utf-8', newline='\n') as fh:
        fh.write('# 语料坏字修复（第二批）证据表 —— 第三字节已丢的 8 族\n\n')
        fh.write('**md 推不回来**（第三字节被 `?` 顶掉），正字取自**上游 `.htm`**。\n')
        fh.write('判据三条叠加：① 词锚（字母数字词，天然干净）② 锚全篇唯一命中 '
                 '③ 候选落在坏字字节定死的区间里。\n')
        fh.write('**只改下游 md，上游 HTML 一个字节不动。**\n\n')
        fh.write(f'共 **{len(rows):,}** 处。\n\n')
        fh.write('| # | markdown | 坏字 | 正字 | 上下文 |\n|---|---|---|---|---|\n')
        for i, (rel, bad, good, ctx) in enumerate(rows, 1):
            q = lambda x: '`' + x.replace('|', '\\|') + '`'
            fh.write(f'| {i} | `{rel}` | {q(bad)} | {q(good)} | {q(ctx)} |\n')
    print(f'\n证据表 → {EVID}')

    _old = json.loads(ASSIGN.read_text(encoding='utf-8')) if ASSIGN.exists() else []
    _new = [dict(md=r[0], bad=r[1], good=r[2]) for r in rows]
    _seen, _m = set(), []
    for e in _new + _old:
        k = (e.get('md'), e.get('bad'), e.get('good'))
        if k in _seen:
            continue
        _seen.add(k)
        _m.append(e)
    if _m:
        ASSIGN.write_text(json.dumps(_m, ensure_ascii=False, indent=0), encoding='utf-8')

    if not APPLY:
        print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
        return

    per = {}
    for p, bad, good in clean:
        per.setdefault(p, []).append((bad, good))
    changed = nf = 0
    for p, items in sorted(per.items(), key=lambda kv: str(kv[0])):
        t = p.read_bytes().decode('utf-8', 'replace')          # ★ 同上
        for bad, good in items:
            assert t.count(bad) >= 1, f'{p.name}: 找不到 {bad!r}'
            t = t.replace(bad, good, 1)
            changed += 1
        p.write_bytes(t.encode('utf-8'))
        nf += 1
    print(f'\n[已改] {changed:,} 处，涉及 {nf} 篇')


if __name__ == '__main__':
    main()
