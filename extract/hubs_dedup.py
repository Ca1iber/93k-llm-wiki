# -*- coding: utf-8 -*-
"""枢纽排名（**去重版**）。

`hubs.csv` 的 `in_src` 有两个独立的灌水来源，都要去掉：

1. **引用方重复**：同一篇页存在 5 份，就有 5 份各记一次引用。
2. **被引方重复**：同一对象有 5 个副本路径，入度就散在 5 条路径上。

第一版只做 1，于是 `WSUS` 从 121 掉到 62 就以为完事了；其实 62 还是**其中一份副本**
的入度，另外四份各有一份。**两端都必须归一到 `source_topic`。**

产出 `hubs-dedup.csv`：canonical topic、代表路径、标题、去重 in_src / out_deg。
"""
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

OUTDIR = Path(r'F:\master-dev\understand-anything-wiki\extract')


def canon_topic(fm):
    t = ((fm or {}).get('source_topic') or '').strip()
    if not t:
        return None
    if t.lower().endswith('.htm'):
        t = t.rsplit('.', 1)[0]
    return re.sub(r'_\d+$', '', t)


def main():
    docs = [json.loads(l) for l in open(OUTDIR / 'docs.jsonl', encoding='utf-8')]
    edges = [json.loads(l) for l in open(OUTDIR / 'edges.jsonl', encoding='utf-8')]

    rel2topic, title = {}, {}
    for d in docs:
        t = canon_topic(d.get('frontmatter'))
        if t:
            rel2topic[d['rel']] = t
        # 取最短路径作代表——最短的那个通常是专题章，不是字母序索引
        if t and (t not in title or len(d['rel']) < len(title[t][0])):
            title[t] = (d['rel'], (d.get('title') or '').strip())

    refs, raw = defaultdict(set), defaultdict(set)
    toc, unres = 0, 0
    for e in edges:
        # **用 `kind` 字段，别自己推。** `toc` 边是 5 个章节目录页 `index.md` 把本章
        # 每篇链一次的目录链接（9,393 条，占全库 53,102 的 17.7%），
        # 语义是「这篇文章在目录里」，不是「正文引用了它」。
        # `edges.jsonl` 早就把这两种边分好了，`hubs.csv` 的 `in_src` 也只计 `inline`。
        # ——第一版这里靠「source 没有 topic」间接推断，绕了一圈，
        # 推出来的还是同一个 9,393。**数据里已有的字段，不要用手写规则重新发明。**
        if e.get('kind') != 'inline':
            toc += 1
            continue
        src, tgt = e.get('from'), e.get('to')
        if not tgt:
            continue
        raw[tgt].add(src)                       # 未去重（应等于 hubs.csv 的 in_src）
        cs, ct = rel2topic.get(src), rel2topic.get(tgt)
        if cs is None or ct is None:
            unres += 1
            continue
        refs[ct].add(cs)

    # ── 交叉验证：未去重的入度必须与 `hubs.csv` 的 `in_src` 逐行相等 ──
    # 两套独立实现（`extract.py` 与这里）算同一个量，不等就说明去重层建在沙子上。
    xcheck, bad = 0, []
    for r in csv.DictReader((OUTDIR / 'hubs.csv').open(encoding='utf-8')):
        mine = len(raw.get(r['path'], ()))
        theirs = int(r['in_src'])
        xcheck += 1
        if mine != theirs:
            bad.append((r['path'], theirs, mine))
    print(f'交叉验证：与 hubs.csv 逐行比对 {xcheck} 行，不符 **{len(bad)}** 行')
    for p, t, m in bad[:5]:
        print(f'    {p}: hubs.csv={t} 本脚本={m}')
    if bad:
        raise SystemExit('未去重入度对不上，去重结果不可信 —— 先查明再往下走')

    rows = []
    for t, s in refs.items():
        rel, ti = title.get(t, ('', ''))
        rows.append({'topic': t, 'rel': rel, 'title': ti, 'in_src': len(s)})
    rows.sort(key=lambda r: (-r['in_src'], r['topic']))

    out = OUTDIR / 'hubs-dedup.csv'
    with out.open('w', encoding='utf-8', newline='\n') as f:
        wr = csv.DictWriter(f, fieldnames=['topic', 'rel', 'title', 'in_src'])
        wr.writeheader()
        wr.writerows(rows)

    n20 = sum(1 for r in rows if r['in_src'] >= 20)
    print(f'唯一 topic {len(title)} 个；有入度的 {len(rows)} 个')
    print(f'剔除：目录边 {toc} 条（5 个 index.md 的 TOC）；'
          f'无 topic 的边 {unres} 条')
    print(f'in_src >= 20: {n20} 个；>= 10: '
          f'{sum(1 for r in rows if r["in_src"] >= 10)} 个；'
          f'>= 5: {sum(1 for r in rows if r["in_src"] >= 5)} 个')
    print()
    print('去重后前 20：')
    for r in rows[:20]:
        print(f'{r["in_src"]:>4}  {r["title"][:44]:<44} {r["topic"]}')
    print(f'\n-> {out}')


if __name__ == '__main__':
    main()
