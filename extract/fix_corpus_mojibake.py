#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""语料修复：把 `agent-markdown/` 里的**坏字**改回原字（`schema.md` §11.2 ①）。

用法：
    python -X utf8 extract/fix_corpus_mojibake.py            # 空跑，只报数、只出证据表
    python -X utf8 extract/fix_corpus_mojibake.py --apply    # 真改

## 病是什么

doc 的字节本来是 UTF-8，却被**按 GBK 读了一遍**。所以：
`µ`（UTF-8 `C2 B5`）被读成 GBK 的 `碌`。

## 为什么能修，而且不用猜

**因为映射是双向确定的**：把坏字 `encode('gbk')` 拿回原字节，再 `decode('utf-8')`，原字就出来了。

**判据取「往返两边都验过」**（照 `encoding_map.py` 里立的那把锁）：
解出来的东西**按 UTF-8 编回去、再按 GBK 读回来，必须一字不差地等于输入**。不等就放弃。
`encoding-map.csv` 里那 128 行过完这把锁，**120 行成立、8 行不成立**——
不成立的 8 行是「**第三字节已丢**」（原文里是个 `?`，不是原字节），
表里只给了区间（`鈮` → U+2240–U+227F）。**那 8 行本脚本一律不动**，
它们得去上游 `.htm` 取，是另一件事（见 `PLAN-未修清单.md` 的 A1）。

## 改的是下游，不是上游

§1.2（2026-09-23 用户改）：**哪一层错就改哪一层**。这一族的**上游 `.htm` 是干净的**
（实测 605 篇里 602 篇干净、上游也坏的 0 篇），坏的是转换后的 md。
**所以改 md，上游一个字节不动** —— 上游保持原样，每改一处都还**对得上证据**。

## 产物

- `extract/_assign_mojibake.json` —— 机器可读清单（供校验与重放），**合并、不重写**
- `extract/findings-corpus-mojibake-evidence.md` —— 逐处对照
"""
import csv
import json
import pathlib
import re
import sys

WIKI = pathlib.Path(r'F:\master-dev\understand-anything-wiki')
CORPUS = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html')
MD = CORPUS / 'agent-markdown' / 'by-category'
MAP = WIKI / 'extract' / 'encoding-map.csv'
EVID = WIKI / 'extract' / 'findings-corpus-mojibake-evidence.md'
ASSIGN = WIKI / 'extract' / '_assign_mojibake.json'
APPLY = '--apply' in sys.argv


def guard(path, n, what):
    """**互锁：不许用空结果覆盖非空清单。** 同 `fix_corpus_superscript.py` 的 `guard()`。"""
    if n or not path.exists() or path.stat().st_size == 0:
        return True
    print(f'\n⛔ 拦截：本次{what}为 0 条，而 {path.name} 已有 '
          f'{path.stat().st_size:,} 字节——**拒绝用空结果覆盖**。')
    print(f'   确要清空，先手工删掉 {path.name} 再跑。')
    return False


def load_map():
    """→ `[(坏字, 原字, 处数)]`，**只留往返两边都验得过的**。

    两把锁，缺一不可：
    ① **正向**：`坏字.encode('gbk').decode('utf-8')` == 原字；
    ② **反向**：原字 `.encode('utf-8').decode('gbk')` == 坏字。
    只验正向的话，「一段坏字恰好也像 UTF-8」这种巧合会被放进来；
    **反向才是「这条路走得回去」的证明**。
    """
    good, dropped = [], []
    for r in csv.DictReader(MAP.open(encoding='utf-8')):
        s, o = r['坏字'], r['本来是']
        try:
            fwd = s.encode('gbk').decode('utf-8') == o
            rev = o.encode('utf-8').decode('gbk') == s
        except Exception:                                   # noqa: BLE001
            fwd = rev = False
        (good if (fwd and rev) else dropped).append((s, o, r))
    return good, dropped


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    good, dropped = load_map()
    print(f'映射表：**{len(good)} 行**往返两边都验过（原字 + 坏字）')
    print(f'         {len(dropped)} 行**不动**（第三字节已丢，表里只有区间）')
    for s, o, r in dropped:
        print(f'           ↳ {s}  {r["处数"]:>5} 处  {o[:34]}')
    print()

    # 先扫一遍看数（不改）。
    #
    # ★ **一次扫描、最长优先**，不逐个子串 `count` 累加。
    # 逐子串累加会把**重叠**的算两次：表里有 5 对子串关系
    # （`渭惟` ⊃ `渭`、`渭惟` ⊃ `惟`、`蠅未` ⊃ `蠅`/`未`、`聽聽` ⊃ `聽`），
    # 于是「5,638」被数成「5,648」。
    # **两种数法改出来的文本一模一样**（`渭惟`→`μΩ` 正好等于 `渭`→`μ` + `惟`→`Ω`），
    # 差的是「算几处」——所以取最长优先，一处一次替换，证据表也与实际改动一一对应。
    #
    # ★ **不按文件名跳 `README.md` / `index.md`。** 语料里那 5 个 `index.md`
    # 是各章的导航页，**算在 9,398 篇里**（`find` 数出来的就是它们）；
    # 而表里的 5,638 = 5,617（正文）+ 21（这 5 个），**说明当初数的时候也算进去了**。
    # 跳掉它们，账就对不上。
    pat = re.compile('|'.join(
        re.escape(s) for s in sorted((s for s, _, _ in good), key=len, reverse=True)))
    good_of = {s: o for s, o, _ in good}
    hits = []          # (path, offset, bad, good)
    files = 0
    for p in sorted(MD.rglob('*.md')):
        b = p.read_bytes()
        try:
            t = b.decode('utf-8')
        except UnicodeDecodeError:
            print(f'  !! 跳过（非 UTF-8）：{p.name}')
            continue
        ms = list(pat.finditer(t))
        if ms:
            files += 1
            for m in ms:
                hits.append((p, m.start(), m.group(0), good_of[m.group(0)]))
    print(f'命中：**{len(hits):,} 处 / {files} 篇**')

    rows = []
    for p, off, s, o in sorted(hits, key=lambda x: (str(x[0]), x[1])):
        b = p.read_bytes()
        t = b.decode('utf-8')
        L = len(s)
        before = t[max(0, off - 55):off + L + 25].replace('\r', ' ').replace('\n', ' ')
        after = (t[max(0, off - 55):off] + o + t[off + L:off + L + 25]
                 ).replace('\r', ' ').replace('\n', ' ')
        rows.append((p.relative_to(MD).as_posix(), s, o, before, after))

    if not guard(EVID, len(rows), '证据表') or not guard(ASSIGN, len(rows), '清单'):
        print('   （什么都没写，语料也没动。）')
        sys.exit(2)

    with EVID.open('w', encoding='utf-8', newline='\n') as fh:
        fh.write('# 语料坏字修复证据表 —— 逐处对照\n\n')
        fh.write('上游：`tdc-html/raw/*.htm`（**干净**）；下游：`agent-markdown/by-category/*.md`。\n')
        fh.write('**只改 markdown。** 判据：坏字按 GBK 编码、再按 UTF-8 解码 = 原字，'
                 '**且反向也成立**。\n\n')
        fh.write(f'共 **{len(rows):,}** 处 / {files} 篇。\n\n')
        fh.write('| # | markdown | 坏字 | 原字 | 改前 | 改后 |\n|---|---|---|---|---|---|\n')
        for i, (rel, s, o, bf, af) in enumerate(rows, 1):
            q = lambda x: '`' + x.replace('|', '\\|') + '`'
            fh.write(f'| {i} | `{rel}` | {q(s)} | {q(o)} | {q(bf)} | {q(af)} |\n')
    print(f'证据表 → {EVID}')

    _new = [dict(layer='md', md=rel, bad=s, good=o, offset=None)
            for rel, s, o, _, _ in rows]
    _old = json.loads(ASSIGN.read_text(encoding='utf-8')) if ASSIGN.exists() else []
    _seen, _merged = set(), []
    for e in _new + _old:
        k = (e.get('md'), e.get('bad'), e.get('good'))
        if k in _seen:
            continue
        _seen.add(k)
        _merged.append(e)
    if _merged:
        ASSIGN.write_text(json.dumps(_merged, ensure_ascii=False, indent=0), encoding='utf-8')

    if not APPLY:
        print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
        return

    per = {}
    for p, off, s, o in hits:
        per.setdefault(p, []).append((off, s, o))
    changed = files2 = 0
    for p, items in sorted(per.items(), key=lambda kv: str(kv[0])):
        b = p.read_bytes()
        txt = b.decode('utf-8')
        for off, s, o in sorted(items, key=lambda x: -x[0]):     # 从后往前，偏移不失效
            assert txt[off:off + len(s)] == s, f'{p.name}@{off} 期望 {s!r} 实得 {txt[off:off+len(s)]!r}'
            txt = txt[:off] + o + txt[off + len(s):]
            changed += 1
        assert txt != b.decode('utf-8')
        p.write_bytes(txt.encode('utf-8'))        # ★ 字节级写，绕开 write_text 的换行转换
        files2 += 1
    print(f'\n[已改] {changed:,} 处，涉及 {files2} 篇')


if __name__ == '__main__':
    main()
