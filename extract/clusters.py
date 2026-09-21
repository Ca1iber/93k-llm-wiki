#!/usr/bin/env python3
# clusters.py — 把语料切成 ingest 的「簇」（schema.md §12 步骤 3）
#
# 簇的定义（两条，缺一不可）：
#   边界  取自语料自带的前缀分类号——免费、内聚、零 token，不需要 LLM 聚类
#   切法  前缀树上的**体量封顶割**——装得下就整块拿走，装不下才分叉，
#         分完再把同父下相邻的簇合并回去。目标是让每簇尽量贴近预算上限。
#
# 为什么不用聚类算法：
#   割**天然保证「每篇恰好属于一个簇」**。聚类给不出这个保证，
#   而且要多花 LLM 调用去判归属——那是拿钱买一个免费的保证。
#
# 为什么必须自底向上（第一版踩过的坑，记一笔）：
#   逐级下钻版在 100k 预算下切出 2,808 簇、**中位簇只有 1k token**。
#   原因是分类号深度普遍 5~7 段（实测），下钻必然钻到单篇——
#   等于按文档 ingest，正是 schema §12 第一条要避免的。
#   改成「装得下就整块拿走」之后，同样预算下是 101 簇、中位 81k。
#
# 输入  extract/docs.jsonl（不读原始语料——索引已经过十类检验，且这一步只做分组）
# 输出  extract/clusters.jsonl
#
# 预算 BUDGET_TOKENS = 100_000，用户 2026-09-17 定。
# 全域零 LLM、零网络、零并发 —— 输出天然确定，第六类幂等性白送。

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

OUTDIR = Path(r'F:\master-dev\understand-anything-wiki\extract')

BUDGET_TOKENS = 100_000
BYTES_PER_TOKEN = 3.5      # 英文技术文档保守取 3.5（宁可高估 token，不可低估）
MAX_DEPTH = 12             # 分类号最深 11 段（实测），12 是兜底

RE_PREFIX = re.compile(r'(\d+(?:\.\d+)*)_')
NO_PREFIX = '\u00b7'       # 「·」：前缀不够长 / 根本没前缀的文档挂在这一桶


def load_docs():
    """读索引。只留 rel / bytes / is_index / seg —— 这一步不需要别的字段。"""
    p = OUTDIR / 'docs.jsonl'
    if not p.is_file():
        sys.exit('先跑 extract.py')
    docs = []
    with open(p, encoding='utf-8') as f:
        for line in f:
            d = json.loads(line)
            stem = d['rel'].split('/')[-1][:-3]          # 去 .md
            m = RE_PREFIX.match(stem)
            docs.append({'rel': d['rel'],
                         'bytes': d['bytes'],
                         'is_index': d['is_index'],
                         'seg': m.group(1).split('.') if m else []})
    return docs


def tokens(docs):
    return sum(d['bytes'] for d in docs) / BYTES_PER_TOKEN


def binpack(ds):
    """前缀已经分不动了（全是同一段，或都挂在父节点上），按大小贪心装箱。

    装不下的单篇自己成簇——它会超预算，但**不许静默丢弃**：
    超预算的簇在报告里逐条列出，那是语料本身的长文档（最大的 78k token，未超）。
    """
    bins, cur = [], []
    for x in sorted(ds, key=lambda x: (-x['bytes'], x['rel'])):
        if cur and tokens(cur) + x['bytes'] / BYTES_PER_TOKEN > BUDGET_TOKENS:
            bins.append(cur)
            cur = []
        cur.append(x)
    if cur:
        bins.append(cur)
    return [{'docs': b, 'how': 'binpack'} for b in bins]


def merge_fit(parts):
    """把同父下**相邻**的簇合并，只要不超预算。

    相邻 = 兄弟子树的字典序相邻。合并兄弟不破坏语义——
    它们本来就属于同一个父节点，只是各自的子树装不下预算才分开的。
    少了这一步，簇数会从 101 涨回 300 多：每个装不满的小子树都自成一簇。
    """
    out = []
    for p in parts:
        if out and tokens(out[-1]['docs']) + tokens(p['docs']) <= BUDGET_TOKENS:
            out[-1] = {'docs': out[-1]['docs'] + p['docs'],
                       'how': 'merged' if out[-1]['how'] != 'binpack' else 'binpack'}
        else:
            out.append(p)
    return out


def cut(ds, depth):
    """前缀树上的体量封顶割。返回 [{'docs': [...], 'how': '...'}, ...]。

    递归三态，顺序不能换：
      1. 整块装得下        -> 拿走，**不下钻**（这是自底向上的关键）
      2. 前缀已到底（只有「·」桶）-> 装箱
      3. 还有子段可分      -> 分叉递归，回来再合并
    """
    if tokens(ds) <= BUDGET_TOKENS:
        return [{'docs': ds, 'how': 'subtree'}]
    if depth >= MAX_DEPTH:
        return binpack(ds)

    g = defaultdict(list)
    for x in ds:
        g[x['seg'][depth] if len(x['seg']) > depth else NO_PREFIX].append(x)

    keys = sorted(g)
    if keys == [NO_PREFIX]:
        return binpack(ds)                 # 前缀到底，分不动了
    if len(keys) == 1:
        return cut(ds, depth + 1)          # 只有一个子段，再下一层看分不分得开

    parts = []
    for k in keys:
        # 「·」桶是前缀不够长、挂在父节点上的概览页，不再下钻
        parts += [{'docs': g[k], 'how': 'subtree'}] if k == NO_PREFIX \
            else cut(g[k], depth + 1)
    return merge_fit(parts)


def lcp(seglists):
    """簇的前缀 = 簇内所有文档分类号的最长公共前缀。空列表 -> 无前缀。"""
    if not seglists or not seglists[0]:
        return []
    out = list(seglists[0])
    for s in seglists[1:]:
        i = 0
        while i < len(out) and i < len(s) and out[i] == s[i]:
            i += 1
        out = out[:i]
        if not out:
            break
    return out


def cut_all(content):
    """切全库。单独成一个函数是为了让检验脚本能在**不同预算**下重跑同一条路径——
    敏感性表必须走真正的入口，另写一份就成了解释而不是证据。
    """
    # 顶层按第一段分叉。没有前缀的（5 篇）单独一桶——它们不属于任何分类号，
    # 但也**不许扔**：扔了就破坏覆盖性，而覆盖性是这个脚本唯一的不变量。
    top = defaultdict(list)
    for d in content:
        top[d['seg'][0] if d['seg'] else NO_PREFIX].append(d)

    clusters = []
    for k in sorted(top):
        clusters += (binpack(top[k]) if k == NO_PREFIX else cut(top[k], 1))
    return clusters


def finalize(clusters):
    """补齐派生字段并按确定性顺序发 id。"""
    for c in clusters:
        ds = sorted(c['docs'], key=lambda x: x['rel'])
        segs = [d['seg'] for d in ds]
        c['docs'] = [d['rel'] for d in ds]
        c['n_docs'] = len(ds)
        c['bytes'] = sum(d['bytes'] for d in ds)
        c['tokens'] = round(c['bytes'] / BYTES_PER_TOKEN)
        c['prefix'] = '.'.join(lcp(segs))
        c['is_index'] = False
        # 横跨几个二级/三级分支。这是**披露字段，不是错误指标**：
        # 合并步骤按体量把相邻兄弟装在一起，必然跨子主题——簇是**打包单位**，
        # 不是主题单位。实测 101 簇里 89 个 span2==1。
        # 留着它是因为「归属是否合理」机器判不了，但「跨度有没有突然变大」机器判得了，
        # 下次重跑时它是一条回归警戒线。
        c['span2'] = len({'.'.join(s[:2]) for s in segs})
        c['span3'] = len({'.'.join(s[:3]) for s in segs})

    # id 在**确定性排序之后**才发，保证两次运行同一簇拿同一个 id。
    # 排序键用 (前缀, 首篇路径)：与体量无关，所以语料小改动不会让 id 大搬家。
    clusters.sort(key=lambda c: (c['prefix'], c['docs'][0]))
    for i, c in enumerate(clusters, 1):
        c['id'] = f'c{i:04d}'
    return clusters


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    docs = load_docs()
    content = [d for d in docs if not d['is_index']]
    index_docs = [d for d in docs if d['is_index']]

    clusters = finalize(cut_all(content))

    with open(OUTDIR / 'clusters.jsonl', 'w', encoding='utf-8', newline='\n') as f:
        for c in clusters:
            f.write(json.dumps(c, ensure_ascii=False, sort_keys=True) + '\n')

    ts = sorted(c['tokens'] for c in clusters)
    over = [c for c in clusters if c['tokens'] > BUDGET_TOKENS]
    print(f'预算 {BUDGET_TOKENS:,} token（{BYTES_PER_TOKEN} 字节/token ≈ '
          f'{BUDGET_TOKENS * BYTES_PER_TOKEN / 1024:.0f} KB）')
    print(f'进簇 {len(content):,} 篇，排除 {len(index_docs)} 个 index.md 目录页')
    print()
    print(f'clusters.jsonl  {len(clusters)} 簇')
    print(f'  体量  中位 {ts[len(ts)//2]:,} / 最小 {ts[0]:,} / 最大 {ts[-1]:,} token')
    print(f'  篇数  中位 {sorted(c["n_docs"] for c in clusters)[len(clusters)//2]}')
    n1 = sum(1 for c in clusters if c['span2'] == 1)
    print(f'  跨度  只在一个二级分支内的 {n1}/{len(clusters)} 簇；'
          f'其余 {len(clusters)-n1} 个跨章打包（见 cluster-report.md）')
    print(f'  超预算 {len(over)} 簇')
    for c in over:
        print(f'    ❌ {c["id"]}  {c["tokens"]:,} token  {c["n_docs"]} 篇  {c["prefix"]}')
    print()
    print('最小 5 簇（不是 bug，是语料本来就零散，列出来是为了别装作没看见）:')
    for c in sorted(clusters, key=lambda c: c['tokens'])[:5]:
        print(f'    {c["tokens"]:>7,} token  {c["n_docs"]:>3} 篇  {c["id"]}  {c["prefix"] or "<无前缀>"}')
    print()
    print(f'DONE -> {OUTDIR / "clusters.jsonl"}')


if __name__ == '__main__':
    main()
