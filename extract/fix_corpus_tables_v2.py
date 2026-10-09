#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""语料修复（第七批）：**换「怎么找候选」**，判据一个字不改。

用法：`--limit N` 试点 / 无参空跑 / `--apply` / `--verify-only`

## 为什么还要一批

前两批（A5 普通表 3,642 张、第六批合并格 362 张）都是**先按「孤立竖线 ≥2 行」筛文档**，
再在文档里找表。哪里漏了，两处：

1. **★ 口径漏了一整个子形态**：表格的行**短到能挤在一行**时（` | Force Voltage  | 1  | 1 mV |`），
   压平后**一行孤立竖线都不会产生** —— 于是整类落在候选集之外。
   实例 `raw/353719.htm`（`Executing_a_measurement`）那张 13 行表：
   判据**能过**（验过），只是「找」的那一步没找到它。
2. **★ 工具对已修文档是盲的**：我生成的 markdown 表**行首就是竖线**，
   而 `md_tokens` 把「任何行首竖线」当作【另一来源（Doxygen）】的签名 → **整篇跳过**。
   实测：A5 修过的 3,642 条，所在文档现在 **100%** 被跳过。
   → **已修文档里没修上的表，前两批之后再也没被看见过。**

## 这一批改的两处（**判据不变**）

- **候选怎么筛**：从「孤立竖线 ≥2 行」改成「**有压平形态的签名**」
  = 存在**行首的 ` |` token**（压平签名）。正常 markdown 表**不产生**这种 token：
  `| a | b |` 的行首竖线前面没有空格，行内的 ` |` 又不在行首。所以它对正常表是 0 命中。
- **token 扫描排除正常 markdown 表**：把「连续 `|` 行块、且块里有 `|---|` 分隔行」的行
  整段排除。于是 ① 我生成的表不会被当成压平表再改一遍（防自匹配），
  ② 「行首竖线」的 Doxygen 判据只认**表外**的行首竖线 —— 已修文档不再被整篇跳过。

**判据（逐格核对、区域有界、内容下限、噪声上限、挂账规则）原封不动** ——
这一批的正当性全押在这句上：**换的是「找」，不是「判」。**

## 产物

- `extract/findings-corpus-tables-v2-evidence.md`、`extract/_assign_tables_v2.json`
- 普通表沿用 A5 的写法（不加说明）；合并格沿用第六批的写法（**表下那句固定措辞的转录说明**，
  措辞与前一批**一字不差**）。
"""
import collections
import hashlib
import json
import pathlib
import re
import sys

sys.path.insert(0, r'F:\master-dev\understand-anything-wiki\extract')
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import fix_corpus_tables as F
import fix_corpus_tables_merged as G

WIKI, CORPUS, MD, RAW = F.WIKI, F.CORPUS, F.MD, F.RAW
EVID = WIKI / 'extract' / 'findings-corpus-tables-v2-evidence.md'
ASSIGN = WIKI / 'extract' / '_assign_tables_v2.json'

APPLY = '--apply' in sys.argv
LIMIT = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else None
DELIM = re.compile(r'^\|[\s:\-|]+\|$')


def md_table_lines(lines):
    """属于「正常 markdown 表」的行号集合：连续 `|` 行块里出现了 `|---|` 分隔行。"""
    out, i, n = set(), 0, len(lines)
    while i < n:
        if lines[i].startswith('|'):
            j = i
            while j < n and lines[j].startswith('|'):
                j += 1
            if any(DELIM.match(lines[k].strip()) for k in range(i, j)):
                out.update(range(i, j))
            i = j
        else:
            i += 1
    return out


def md_tokens_v2(text):
    """同 `F.md_tokens`，但**排除正常 markdown 表的行**；`col0` 只认**表外**的行首竖线。"""
    lines = text.splitlines(keepends=True)
    tbl = md_table_lines([l.rstrip('\r\n') for l in lines])
    spans, pos = [], 0
    for ln, L in enumerate(lines):
        if ln not in tbl:
            spans.append((pos, pos + len(L)))
        pos += len(L)
    outside = any(ln not in tbl and l.startswith('|') for ln, l in enumerate(lines))
    allt, bol, eol = [], [], set()
    for m in F.TOKEN.finditer(text):
        p = m.start()
        if not any(a <= p < b for a, b in spans):
            continue
        bolp = text.rfind('\n', 0, p) + 1
        if text[bolp:p].strip() == '':
            bol.append(len(allt))
        e = p + 1
        nl = text.find('\n', e)
        nl = len(text) if nl < 0 else nl
        if text[e:nl].strip() == '':
            eol.add(len(allt))
        allt.append(p)
    return allt, bol, eol, outside


def match_any(text, allt, bol, eol, u):
    """按上游表有没有合并格，选对应的判据。

    两个判据的候选形状不同（普通 4 元、合并格 8 元），这里**归一**成 6 元：
    `(start, end, cells, flat_up, merged, extra)`
    —— `extra` 普通表是 `(R, C, None, None)`，合并格是 `(R, C, expanded, placed)`。"""
    rows = u['rows']
    R, C = len(rows), len(rows[0])
    if u['skip'] == '合并格':
        c, r = G.match_merged(text, allt, bol, eol, rows)
        return [(x[0], x[1], x[2], x[3], True, (x[4], x[5], x[6], x[7])) for x in c], r
    c, r = F.match_table(text, allt, bol, eol, rows, R, C)
    return [(x[0], x[1], x[2], x[3], False, (R, C, None, None)) for x in c], r


def main():
    if '--verify-only' in sys.argv:
        return verify_only()

    fixed = set()
    for f in ('_assign_tables.json', '_assign_tables_merged.json'):
        fp = WIKI / 'extract' / f
        if fp.exists():
            for x in json.loads(fp.read_text(encoding='utf-8')):
                fixed.add((x['md'], x['tbl']))

    stat, tbl_stat, accepted = {}, {}, []

    def bump(d, k, n=1):
        d[k] = d.get(k, 0) + n

    docs = []
    for p in sorted(MD.rglob('*.md')):
        text = p.read_bytes().decode('utf-8', 'replace')
        allt, bol, eol, col0 = md_tokens_v2(text)
        if col0:
            bump(stat, '含行首竖线（另一来源，整篇）')
            continue
        if bol:
            docs.append((p, text, allt, bol, eol))
    print(f'有压平签名的文档：{len(docs):,} 篇')
    if LIMIT:
        docs = docs[:LIMIT]
        print(f'--limit {LIMIT} → 只跑前 {len(docs)} 篇')

    for p, text, allt, bol, eol in docs:
        nl = '\r\n' if '\r\n' in text else '\n'
        rel = p.relative_to(MD).as_posix()
        m = F.SOURCE_TOPIC.search(text)
        if not m:
            bump(stat, '无 source_topic')
            continue
        topic = m.group(1).replace('.htm', '')
        ups, why = F.upstream_tables(topic)
        if ups is None:
            bump(stat, why)
            continue
        by = {}
        for ui, u in enumerate(ups):
            if u['skip'] == '列数不齐':
                bump(tbl_stat, '上游列数不齐')
                continue
            if (rel, ui) in fixed:
                continue                       # 前两批已修
            mine, reason = match_any(text, allt, bol, eol, u)
            if mine:
                by[ui] = mine
            elif reason:
                bump(tbl_stat, reason)
        picked = []
        for ui, lst in sorted(by.items()):
            lst = sorted(lst, key=lambda c: -(c[1] - c[0]))
            keep, spans = [], []
            for c in lst:
                if any(not (c[1] <= s or c[0] >= e) for s, e in spans):
                    continue
                spans.append((c[0], c[1]))
                keep.append((ui,) + c)
            if len(keep) == 1:
                picked.append(keep[0])
            elif keep:
                bump(tbl_stat, '同表多处命中（分不清 → 整张不动）')
        if not picked:
            bump(stat, '无表对上')
            continue
        # picked 元素 = (ui, start, end, cells, flat_up, merged, extra)
        picked.sort(key=lambda c: -(c[2] - c[1]))
        chosen, spans = [], []
        for c in picked:
            if any(not (c[2] <= s or c[1] >= e) for s, e in spans):
                bump(tbl_stat, '同一段被两个上游表抢（弃一）')
                continue
            spans.append((c[1], c[2]))
            chosen.append(c)
        chosen.sort(key=lambda c: c[1])
        bump(stat, '有表对上')
        for ui, start, end, cells, flat_up, merged, extra in chosen:
            rec = build(p, text, topic, ui, merged, extra, cells, start, end, nl)
            if rec:
                accepted.append(rec)

    n_tbl = len(accepted)
    n_doc = len({x['path'] for x in accepted})
    print(f'\n✅ 可修 **{n_tbl:,} 张**，涉及 **{n_doc:,} 篇**')
    print('\n跳过（按类，**不许静默跳过**）：')
    for k, v in sorted({**stat, **tbl_stat}.items(), key=lambda kv: -kv[1]):
        print(f'   {k:<34} {v:,}')

    if LIMIT:
        print('\n[试点 --limit] 不写产物。')
        for x in accepted[:6]:
            print('=' * 74)
            print(f"{x['path'].relative_to(MD).as_posix()}  ← raw/{x['topic']}.htm 表#{x['tbl']}"
                  f"  {'合并格' if x['merged'] else '普通'}")
            for line in x['table'].split('\r\n')[:12]:
                print('  ' + line[:140])
        return

    if not F.guard(EVID, n_tbl, '证据表') or not F.guard(ASSIGN, n_tbl, '清单'):
        print('   （什么都没写，语料也没动。）')
        sys.exit(2)

    esc = lambda s: s.replace('\\', '\\\\').replace('|', '\\|').replace('\r\n', '⏎')
    with EVID.open('w', encoding='utf-8', newline='\n') as fh:
        fh.write('# 语料表格修复证据表 —— 第七批（换「怎么找候选」，判据不变）\n\n')
        fh.write(f'写于 2026-10-09。共 **{n_tbl:,}** 张 / **{n_doc:,}** 篇。\n\n')
        fh.write('前两批按「孤立竖线 ≥2 行」筛文档，漏了两处：\n'
                 '① 行能挤在一行的压平表**不产生孤立竖线**；\n'
                 '② 我生成的 markdown 表行首是竖线，被当成「另一来源」→ **已修文档整篇被跳过**。\n'
                 '本批把候选改成「**有压平形态的签名**」= 存在行首的 ` |` token，'
                 '并在 token 扫描里**排除正常 markdown 表的行**。**判据一个字没改。**\n\n')
        fh.write('**只改 `agent-markdown/`，上游 `raw/*.htm` 一个字节不动。**\n\n')
        fh.write('| # | markdown | 上游 | 表 | 类型 | 新表 |\n|---|---|---|---|---|---|\n')
        for n, x in enumerate(accepted, 1):
            rel = x['path'].relative_to(MD).as_posix()
            fh.write(f"| {n} | `{rel}` | `{x['topic']}.htm` | #{x['tbl']} | "
                     f"{'合并格' if x['merged'] else '普通'} | `{esc(x['table'])}` |\n")
    print(f'\n证据表 → {EVID}')

    _m = [dict(md=x['path'].relative_to(MD).as_posix(), topic=x['topic'], tbl=x['tbl'],
               R=x['R'], C=x['C'], merged=x['merged'], a=x['a'], e=x['e'],
               sha1_orig=hashlib.sha1(x['orig'].encode('utf-8')).hexdigest(),
               orig=x['orig'], new=x['table']) for x in accepted]
    ASSIGN.write_text(json.dumps(_m, ensure_ascii=False, indent=0), encoding='utf-8')
    print(f'机器可读清单 → {ASSIGN}（{len(_m):,} 条，本次全量重写）')

    if not APPLY:
        print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
        return

    per = {}
    for x in accepted:
        per.setdefault(x['path'], []).append(x)
    changed = 0
    for p, recs in sorted(per.items(), key=lambda kv: str(kv[0])):
        t = p.read_bytes().decode('utf-8', 'replace')
        crlf = t.count('\n') == t.count('\r\n')
        for x in sorted(recs, key=lambda r: -r['a']):
            assert t[x['a']:x['e']] == x['orig'], f"{p.name}: 区域与预期不符"
            t = t[:x['a']] + x['table'] + x['tail'] + t[x['e']:]
            changed += 1
        if crlf:
            assert t.count('\n') == t.count('\r\n'), f'{p.name}: 混入了裸 LF'
        p.write_bytes(t.encode('utf-8'))

    bad = F._replay_verify(per)
    if bad:
        print(f'\n⛔ 重放验证失败 {len(bad)} 篇，前 5：')
        for rel, why in bad[:5]:
            print(f'   {rel}: {why}')
        sys.exit(3)
    print(f"\n[已改] {changed:,} 张，涉及 {len(per):,} 篇（逐字节重放通过）")


def build(p, text, topic, ui, merged, extra, cells, start, end, nl):
    """生成记录。**两种写法与前两批一字不差**：

    - 普通表 → A5 的写法（不加说明）
    - 合并格 → 第六批的写法（**表下那句固定措辞的转录说明**）

    两道自校验都照跑（NUL / 裸 LF / 新表回解）。"""
    R, C, expanded, placed = extra
    a = text.rfind('\n', 0, start) + 1
    if merged:
        tbl = G.render(expanded, R, C, nl, topic)
        G.self_check(tbl, expanded, R, C, nl, p.name)
    else:
        tbl = F.render_table([F.clean_cell(c) for c in cells], R, C, nl)
        grid = [cells[r * C:(r + 1) * C] for r in range(R)]
        G.self_check(tbl, grid, R, C, nl, p.name)
    assert '\x00' not in tbl, f'{p.name}: 新表里有 NUL'
    assert '\n' not in tbl.replace(nl, ''), f'{p.name}: 新表里混进了裸 LF'
    e = end
    while e < len(text) and text[e] in ' \t':
        e += 1
    glued = e < len(text) and text[e] not in '\r\n'
    tail = ((nl + nl) if merged else nl) if glued else ''
    return dict(path=p, topic=topic, tbl=ui, merged=merged, R=R, C=C,
                table=tbl, orig=text[a:e], a=a, e=e, tail=tail)


def verify_only():
    _m = json.loads(ASSIGN.read_text(encoding='utf-8'))
    per = {}
    for x in _m:
        per.setdefault(MD / x['md'], []).append(
            dict(a=x['a'], e=x['e'], orig=x['orig'], table=x['new'], tail=x.get('tail', '')))
    print(f'清单 {len(_m):,} 条 / {len(per):,} 篇；对 `git show HEAD:` 逐字节重放…')
    bad = F._replay_verify(per)
    if bad:
        print(f'⛔ 失败 {len(bad)} 篇，前 10：')
        for rel, why in bad[:10]:
            print(f'   {rel}: {why}')
        sys.exit(3)
    print(f'✅ 重放一致：{len(per):,}/{len(per):,} 篇，逐字节相同。')


if __name__ == '__main__':
    main()
