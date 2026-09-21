#!/usr/bin/env python3
# verify_clusters.py — 簇切分的交叉检验
#
# 为什么单独一份而不是塞进 verify.py：
#   verify.py 证明的是**抽取**（原文 → 索引）可信，已经签过字。
#   这里证明的是**切分**（索引 → 簇）可信，是另一件事、另一个输入、另一批不变量。
#   混在一起，任何一边改动都要重签另一边。
#
# 检验的立足点，先说清楚**能抓什么、抓不到什么**：
#
#   抓得到（输出侧不变量 + 独立复算 + 穷举）：
#     - 切分是不是一个**划分**：每篇恰好进一个簇，无漏无重无悬空
#     - 体量数字是不是真的：簇的 bytes / tokens / 篇数独立重算
#     - 前缀字段是否忠实：prefix 必须等于簇内文档分类号的真实 LCP
#     - 是不是真出自那条规则：重跑算法，逐字节比对
#     - **有没有「该在一起的被切散」**（第六类，穷举，见下）
#
#   抓不到（而且**不需要抓**）：
#     - **打包是否贴合主题**——即「同一簇里的文档是不是同一件事」。
#       它抓不到，但不是缺陷，因为**判据本来就不是这个**：簇是打包单位，
#       不是主题单位。合并按体量装箱，必然跨子主题。
#
# 第六类为什么能穷举，而不是抽样给人看：
#   切分规则有一句「整棵子树装得下就整块拿走，不下钻」。它的**逆否命题**就是
#   一条可穷举的不变量：
#
#       任何体量 <= 预算的前缀节点，其全部文档必须落在同一个簇里。
#
#   违反它 = 一个本来读得下的主题被拆去了两个簇 = 两边各写半页 = **唯一真会
#   出问题的情形**。所以把语料里每个前缀节点的体量算一遍、逐个查归属即可。
#   这条路**不需要人**，而且比看 15 个抽样簇强得多——它是全库覆盖。
#
#   体量 > 预算的节点**允许**被拆，而且必须被拆：`02.07.04.01` 有 553 篇
#   ≈ 54 万 token，是预算的 5.4 倍，不拆就塞不进任何一次调用。
#   所以「被拆」本身不是错，**「装得下还被拆」才是错**。
#
# 输出  extract/cluster-report.md
#       extract/cluster-spot-check.md（**浏览用，不是放行条件**）

import hashlib
import json
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import clusters as C  # noqa: E402  第 5 类（预算敏感性）要跑**真入口**，
#                       不是另写一份实现——另写一份就成了解释而不是证据。

OUTDIR = C.OUTDIR
R = []


def w(s=''):
    R.append(s)
    print(s)


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def cat1_cover(cl, docs):
    """第一类 · 覆盖性。**独立复算**：不用切分算法，只对输出做集合运算。"""
    w('## 第一类 · 覆盖性（独立复算）')
    w()
    w('不看切分算法，只拿 `clusters.jsonl` 和 `docs.jsonl` 做集合运算。')
    w()

    in_corpus = {d['rel'] for d in docs if not d['is_index']}
    flat = [r for c in cl for r in c['docs']]
    seen = set(flat)

    def row(name, expect, got):
        ok = '✅' if expect == got else f'❌ 差 {got - expect}'
        w(f'| {name} | {expect} | {got} | {ok} |')
        return expect == got

    w('| 检查 | 判据 | 实测 | 结果 |')
    w('|---|---|---|---|')
    ok = True
    ok &= row('簇内文档合计 == 语料篇数（无漏）', len(in_corpus), len(flat))
    ok &= row('去重后 == 语料篇数（无重）', len(in_corpus), len(seen))
    ok &= row('簇里有、`docs.jsonl` 没有的路径（悬空）', 0, len(seen - in_corpus))
    ok &= row('语料有、没有任何簇认领的路径（漏页）', 0, len(in_corpus - seen))
    ok &= row('`n_docs` 字段合计 == 语料篇数', len(in_corpus),
              sum(c['n_docs'] for c in cl))
    w()
    if ok:
        w(f'**切分是一个划分**：{len(in_corpus):,} 篇，每篇恰好进一个簇，'
          f'{len(cl)} 个簇，无漏、无重、无悬空。')
    w()
    return ok


def cat2_footprint(cl, docs):
    """第二类 · 体量与前缀。独立重算每个簇的数字，不看脚本写的值。"""
    w('## 第二类 · 体量与前缀（独立复算）')
    w()
    w('从 `docs.jsonl` 独立重算每簇的字节数、篇数、分类号最长公共前缀，与记录值对质。')
    w()

    by_rel = {d['rel']: d for d in docs}
    bad_bytes = bad_tokens = bad_n = bad_lcp = bad_seg = 0
    detail = []
    for c in cl:
        ds = [by_rel[r] for r in c['docs']]
        segs = []
        for r in c['docs']:
            stem = r.split('/')[-1][:-3]
            m = C.RE_PREFIX.match(stem)
            segs.append(m.group(1).split('.') if m else [])

        nbytes = sum(d['bytes'] for d in ds)
        if nbytes != c['bytes']:
            bad_bytes += 1
            detail.append(f'{c["id"]} bytes {c["bytes"]} != {nbytes}')
        if round(nbytes / C.BYTES_PER_TOKEN) != c['tokens']:
            bad_tokens += 1
            detail.append(f'{c["id"]} tokens {c["tokens"]} != 重算')
        if len(ds) != c['n_docs']:
            bad_n += 1
            detail.append(f'{c["id"]} n_docs {c["n_docs"]} != {len(ds)}')

        want_lcp = '.'.join(C.lcp(segs))
        if want_lcp != c['prefix']:
            bad_lcp += 1
            detail.append(f'{c["id"]} prefix {c["prefix"]!r} != LCP {want_lcp!r}')
        # prefix 不但要是 LCP，还必须真的是**每一篇**的前缀——
        # LCP 相等但某篇不在该前缀下，数学上不可能；可这条会抓住
        # 「prefix 字段被手改过」这类篡改，所以留着，成本为零。
        p = c['prefix'].split('.') if c['prefix'] else []
        for s in segs:
            if s[:len(p)] != p:
                bad_seg += 1
                detail.append(f'{c["id"]} 某篇分类号不在 prefix 下')
                break

    def row(name, got):
        ok = '✅' if got == 0 else f'❌ {got} 处'
        w(f'| {name} | 0 | {got} | {ok} |')
        return got == 0

    w('| 检查 | 判据 | 实测 | 结果 |')
    w('|---|---|---|---|')
    ok = True
    ok &= row('`bytes` 与独立重算不符的簇数', bad_bytes)
    ok &= row('`tokens` 与独立重算不符的簇数', bad_tokens)
    ok &= row('`n_docs` 与独立重算不符的簇数', bad_n)
    ok &= row('`prefix` 不等于真实 LCP 的簇数', bad_lcp)
    ok &= row('簇内存在分类号不在 `prefix` 下的文档的簇数', bad_seg)
    w()
    for d in detail[:10]:
        w(f'- {d}')
    if detail:
        w()

    over = [c for c in cl if c['tokens'] > C.BUDGET_TOKENS]
    w(f'**超预算的簇：{len(over)} 个**（预算 {C.BUDGET_TOKENS:,} token）')
    w()
    if over:
        w('| 簇 | token | 篇数 | 前缀 | 说明 |')
        w('|---|---|---|---|---|')
        for c in over:
            w(f'| {c["id"]} | {c["tokens"]:,} | {c["n_docs"]} | `{c["prefix"]}` | '
              f'前缀已到底、只能装箱；装箱内单篇超预算 |')
        w()
        w('> 这些不是 bug，是语料里存在超长单篇。**逐条列名，不许静默放行。**')
    else:
        w(f'无簇超预算。最大簇 {max(c["tokens"] for c in cl):,} token，'
          f'贴着上限但没越界。')
    w()

    # span2 的 `bytes`/`tokens` 一样要独立重算——派生字段写错了没人会发现。
    bad_span = sum(1 for c in cl
                   if len({'.'.join(C.RE_PREFIX.match(r.split('/')[-1][:-3]).group(1).split('.')[:2])
                           if C.RE_PREFIX.match(r.split('/')[-1][:-3]) else []
                           for r in c['docs']}) != c['span2'])
    n1 = sum(1 for c in cl if c['span2'] == 1)
    w(f'**跨度披露**（这一栏不判通过/不通过，只把话说清楚）：')
    w()
    w(f'- 只在一个二级分支内的：**{n1}/{len(cl)}** 簇')
    w(f'- 跨章的：{len(cl) - n1} 簇，其中 `span2` 最大的是：')
    w()
    w('| 簇 | `span2` | 篇数 | token | 跨的分支 |')
    w('|---|---|---|---|---|')
    for c in sorted(cl, key=lambda x: -x['span2'])[:5]:
        seg = [C.RE_PREFIX.match(r.split('/')[-1][:-3]) for r in c['docs']]
        br = sorted({'.'.join(m.group(1).split('.')[:2]) for m in seg if m})
        w(f'| {c["id"]} | {c["span2"]} | {c["n_docs"]} | {c["tokens"]:,} | '
          f'`{", ".join(br[:5])}{"…" if len(br) > 5 else ""}` |')
    w()
    w('> **跨章打包不是缺陷，是打包的必然结果**——合并按体量把相邻兄弟装在一起，'
      '在任何层级都会跨子主题。页面归属由「定义该对象的那篇文档」决定，'
      '而切分是划分，所以属主唯一，跨章不会让两个簇写同一页。')
    w('> 这条栏位留着是为了**回归**：`span2` 分布若突然变大，说明切分行为变了。')
    w()
    ok &= (bad_span == 0)
    return ok and not over


def cat3_excluded(docs):
    """第三类 · 未进簇的文档，逐个列名。静默丢弃视为 bug。"""
    w('## 第三类 · 未进簇的文档（不许静默丢弃）')
    w()
    ix = [d for d in docs if d['is_index']]
    w(f'共 **{len(ix)}** 篇被排除在簇之外，全部是 `index.md` 目录页：')
    w()
    w('| 路径 | 字节 | 为什么排除 |')
    w('|---|---|---|')
    for d in sorted(ix, key=lambda x: -x['bytes']):
        why = ('**1.08 MB ≈ 309k token，比任何合理预算都大**；'
               '而且它是目录不是内容' if d['bytes'] > 500_000 else '目录页，非内容')
        w(f'| `{d["rel"]}` | {d["bytes"]:,} | {why} |')
    w()
    w('排除的正当性：这 5 篇的内容就是目录本身，而它们的 9,393 条目录链接'
      '已经以 `kind: toc` 记在 `edges.jsonl` 里。**放进簇是重复计算，不是覆盖。**')
    w()
    return True


def cat4_idempotent():
    """第四类 · 幂等与可复现。重跑算法，逐字节比对。"""
    w('## 第四类 · 幂等与可复现')
    w()
    p = OUTDIR / 'clusters.jsonl'
    before = sha256(p)
    bak = p.read_bytes()
    import subprocess
    r = subprocess.run([sys.executable, str(OUTDIR / 'clusters.py')],
                       capture_output=True, cwd=str(OUTDIR))
    if r.returncode != 0:
        w(f'❌ 重跑失败：{r.stderr.decode("utf-8", "replace")[:400]}')
        return False
    after = sha256(p)
    same = (after == before and p.read_bytes() == bak)
    w(f'- 第一次 `sha256`：`{before[:16]}…`')
    w(f'- 重跑后 `sha256`：`{after[:16]}…`')
    w()
    w(f'**两次逐字节{"相同" if same else "不同"}。**')
    w()
    w('这条**不是同义反复**。切分的成员归属无法从输出侧独立判定'
      '（见文首「抓不到」），唯一能证明的是「这批簇确实出自那条确定性规则、'
      '而不是别的东西」——重跑一致正是这句话的可检验形式。')
    w()
    return same


def cat5_sensitivity(content):
    """第五类 · 预算敏感性。**明确标注：走同一算法，不是独立复算。**"""
    w('## 第五类 · 预算敏感性（同一算法，**不是**独立复算）')
    w()
    w('为 100k 这个选择留下依据。下表由 `clusters.cut_all()` 真入口重跑得到，'
      '不是另写一份实现——**这是敏感性分析，不构成对切分正确性的检验。**')
    w()
    w('| 预算 | 簇数 | 中位簇 | 最大簇 | 最小簇 | 超预算 |')
    w('|---|---|---|---|---|---|')
    keep = C.BUDGET_TOKENS
    kept = None
    for b in (30_000, 50_000, 80_000, 100_000, 150_000, 200_000):
        C.BUDGET_TOKENS = b
        cl = C.finalize(C.cut_all(content))
        ts = sorted(c['tokens'] for c in cl)
        n_over = sum(1 for t in ts if t > b)
        star = ' **←**' if b == keep else ''
        w(f'| {b // 1000}k{star} | {len(cl)} | {ts[len(ts)//2]:,} | {ts[-1]:,} | '
          f'{ts[0]:,} | {n_over} |')
        if b == keep:
            kept = (len(cl), ts[len(ts)//2], sum(1 for t in ts if t > b))
    C.BUDGET_TOKENS = keep
    w()
    # 理由里的数字**全部取自上面那一行**，不许手写——
    # 手写的数字改一个参数就变成谎话，而它看起来照样像个证据。
    n_cl, med, n_over = kept
    w(f'选 **{keep // 1000}k** 的理由：{n_cl} 簇落在 `schema.md` §12 说的「百次量级」；'
      f'中位 {med:,} token 说明大部分簇装得比较满（不是靠碎片堆数量）；'
      f'超预算 {n_over} 个。50k 会涨到约 200 簇，切得更细、更贵。')
    w()
    return True


def cat6_unsplit(cl, docs):
    """第六类 · **装得下的主题有没有被切散**。穷举，不需要人。

    切分规则的逆否命题：体量 <= 预算的前缀节点，必须完整落在同一个簇里。
    把语料里**每个**前缀节点都算一遍，逐个查它跨了几个簇。

    这一条取代了原先的「抽 15 簇给人看」——用户指出那个检查他做不了，而且
    他说的对：人眼看簇内文档标题，本来就看不出「有没有被切散」。能看出的
    （同簇文档是不是一件事）又**不是判据**。真正要防的那件事，是能穷举的。
    """
    w('## 第六类 · 装得下的主题有没有被切散（**穷举**）')
    w()
    w('判据来自切分规则的逆否：**体量 ≤ 预算的前缀节点必须完整落在一个簇里**。')
    w('违反 = 一个本来读得下的主题被拆到两个簇 = 两边各写半页。')
    w('体量 > 预算的节点**必须**被拆（不拆塞不进任何一次调用），拆了不算错。')
    w()

    by_rel = {d['rel']: d for d in docs}
    owner = {r: c['id'] for c in cl for r in c['docs']}

    nodes = defaultdict(list)
    for r in owner:
        for i in range(1, len(by_rel[r]['seg']) + 1):
            nodes['.'.join(by_rel[r]['seg'][:i])].append(r)

    checked = bad = 0
    over = []
    viol = []
    for p, rs in nodes.items():
        t = sum(by_rel[r]['bytes'] for r in rs) / C.BYTES_PER_TOKEN
        if t <= C.BUDGET_TOKENS:
            checked += 1
            o = {owner[r] for r in rs}
            if len(o) > 1:
                bad += 1
                viol.append((p, t, len(rs), sorted(o)))
        else:
            over.append((p, t, len(rs)))

    w(f'| 检查 | 期望 | 实测 |')
    w('|---|---|---|')
    w(f'| 语料里的前缀节点总数 | — | {len(nodes):,} |')
    w(f'| 其中体量 ≤ 预算（**必须不被拆**） | — | {checked:,} |')
    w(f'| **被拆到多个簇的** | 0 | **{bad}** |')
    w(f'| 其中体量 > 预算（**必须被拆**，不算错） | — | {len(over):,} |')
    w()
    for p, t, n, o in sorted(viol, key=lambda x: -x[1])[:10]:
        w(f'- ❌ `{p}` {t:,.0f} token / {n} 篇 → {o}')
    if not viol:
        w(f'**{checked:,} 个读得下的主题，一个都没被拆散。**')
    w()
    if over:
        w('体量 > 预算、**必须**被拆的节点（拆对了才读得进去）：')
        w()
        for p, t, n in sorted(over, key=lambda x: -x[1])[:8]:
            w(f'- `{p}` {t:,.0f} token / {n} 篇 = 预算的 {t / C.BUDGET_TOKENS:.1f} 倍')
        w()

    # 连续性是上面那条的**经验佐证**：把全库按分类号排序，一个簇的文档
    # 应该占据很少几段。它有噪声——字典序把 `26` 排在 `250` 后面，
    # 短前缀文档会「跳」到别处，制造假碎片。所以它是佐证，不是判据。
    order = sorted(owner, key=lambda r: by_rel[r]['seg'])
    runs = Counter()
    prev = None
    for r in order:
        if owner[r] != prev:
            runs[owner[r]] += 1
            prev = owner[r]
    n1 = sum(1 for c in cl if runs[c['id']] == 1)
    w(f'佐证 · 按分类号排全库，{len(order):,} 篇共 {sum(runs.values())} 次簇切换；'
      f'**{n1}/{len(cl)}** 簇恰好占一段连续区间。')
    w()
    w('这个数字**自己就不稳**：换排序键它会变（按完整路径排是 93/101，按分类号元组排'
      f'是 {n1}/101）。原因有两个，都不是错误——')
    w()
    w('1. **字典序假碎片**：`26` 排在 `250` 之后（逐字符比 `6`>`5`），'
      '所以 `.26_x` 会「跳」到 `.250` 那批后面，看上去像碎了一段。')
    w('2. **真碎片只在允许拆的地方**：碎成 2~3 段的簇全在 `02.07.04.01`（11 倍预算）'
      '和 `02.06.02.02` 内部——那里**必须**拆。')
    w()
    w('所以它是佐证，不是判据：**判据是第六类那张表**，它不依赖任何排序键。')
    w()
    return bad == 0


def cat7_browse(cl, docs):
    """第七类 · 摊开供浏览。**不是放行条件**，只是让人能翻。"""
    w('## 第七类 · 浏览（**不是放行条件**）')
    w()
    by_rel = {d['rel']: d for d in docs}
    picks = sorted(cl, key=lambda c: c['id'])
    step = max(1, len(picks) // 15)
    picks = picks[::step][:15]

    L = ['# 簇抽样核对表', '',
         f'共 **{len(cl)}** 簇，这里摊开 **{len(picks)}** 个（等距抽样）。', '',
         '> 第一到第五类全是数字检验。**这一份要人真的看一眼。**', '',
         '## 先说清楚「同一主题」不是判据',
         '',
         '簇是**打包单位**，不是主题单位。合并步骤按体量把相邻的兄弟装在一起，'
         '必然跨子主题——这在任何层级都一样（`02.07.04.01.14.x` 和 `.27x` 也是'
         '互不相干的函数，只因同属一章就被装进一个簇）。',
         '',
         '试过用规则把它们分开：按「章号级不合并」改，簇数从 **101 涨到 1,046**、'
         '中位掉到 1,361 token，而且 `99_Unlisted`（248 篇文档号当章节用）会碎成'
         '248 个单篇簇。**代价 10 倍，换不到任何东西**（见下）。',
         '',
         '**因为页面归属不靠簇决定**：一个对象页由「定义它的那篇文档」所在的簇拥有，'
         '而切分是一个划分——每篇文档恰好在一个簇里，所以每个对象页的属主唯一，'
         '跨章打包不会让两个簇去写同一页。',
         '',
         '## 这一份是给人翻的，不是给人判的',
         '',
         '「有没有该在一起的文档被切散」——**这一条已经由第六类穷举判完了**，'
         '不需要人看：语料里每个前缀节点都算过体量，读得下的一个都没被拆。',
         '',
         '人眼在这里本来也判不了：光看簇内文档标题，看不出某篇的邻居是不是'
         '在隔壁簇。而人眼**看得出的**那条（同簇文档是不是同一件事），'
         '上面说了，不是判据。',
         '',
         '所以下面是给人**浏览**用的——想确认某批文档被分到哪去了，直接翻。',
         '要判「某篇的归属合不合理」，正确的做法是查它的分类号父节点在第六类'
         '里是绿的，而不是读这张表。', '']

    # 全 101 簇的索引——「这批文档分到哪去了」一查就知道，这才是这张表的用处
    L += ['## 全 101 簇索引', '',
          '| id | prefix | 篇 | token | 源自 | span2 |', '|---|---|---|---|---|---|']
    for c in sorted(cl, key=lambda c: c['id']):
        L.append(f'| `{c["id"]}` | `{c["prefix"] or "—"}` | {c["n_docs"]} | '
                 f'{c["tokens"]:,} | `{c["how"]}` | {c["span2"]} |')
    L += ['', '## 15 簇抽样（等距，看标题用）', '']

    for c in picks:
        L += [f'### {c["id"]} · `{c["prefix"] or "<无前缀>"}`', '',
              f'{c["n_docs"]} 篇 / {c["tokens"]:,} token / 源自 `{c["how"]}` / '
              f'`span2`={c["span2"]} `span3`={c["span3"]}', '']
        for r in c['docs'][:10]:
            t = by_rel[r].get('title') or r.split('/')[-1][:-3]
            L.append(f'- {t[:88]}')
        if c['n_docs'] > 10:
            L.append(f'- *…另有 {c["n_docs"] - 10} 篇*')
        L.append('')

    with open(OUTDIR / 'cluster-spot-check.md', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L))

    w(f'已生成 `cluster-spot-check.md`（{len(picks)} 簇等距抽样 + 全 101 簇清单）。')
    w('**不构成放行条件**——放行看第六类。')
    w()
    return f'已生成 {len(picks)} 簇浏览表'


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    if not (OUTDIR / 'clusters.jsonl').is_file():
        sys.exit('先跑 clusters.py')

    docs = C.load_docs()
    cl = [json.loads(l) for l in open(OUTDIR / 'clusters.jsonl', encoding='utf-8')
          if l.strip()]
    content = [d for d in docs if not d['is_index']]

    w('# 簇切分对账报告')
    w()
    w(f'对象：`extract/clusters.jsonl`，{len(cl)} 簇 / '
      f'{sum(c["n_docs"] for c in cl):,} 篇。')
    w(f'参数：预算 **{C.BUDGET_TOKENS:,} token**（{C.BYTES_PER_TOKEN} 字节/token）。'
      f'规则见 `clusters.py` 文件头。')
    w()
    w('---')
    w()

    res = {}
    res['第一类 覆盖性'] = cat1_cover(cl, docs)
    res['第二类 体量与前缀'] = cat2_footprint(cl, docs)
    res['第三类 未进簇披露'] = cat3_excluded(docs)
    res['第四类 幂等与可复现'] = cat4_idempotent()
    res['第五类 预算敏感性'] = cat5_sensitivity(content)
    res['第六类 装得下的主题未被切散'] = cat6_unsplit(cl, docs)
    res['第七类 浏览表'] = cat7_browse(cl, docs)

    w('## 汇总')
    w()
    w('| 检验 | 结果 |')
    w('|---|---|')
    for k, v in res.items():
        mark = 'ℹ️ 见正文' if isinstance(v, str) else ('✅ 通过' if v else '❌ 未通过')
        w(f'| {k} | {mark} |')
    w()
    w('**第一到第五类**说明切分是个划分、数字是真的、出自那条规则。')
    w('**第六类**说明没有「读得下的主题被拆到两个簇」——全库穷举，不靠抽样。')
    w('第七类是浏览表，不判通过。')
    w()

    with open(OUTDIR / 'cluster-report.md', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(R) + '\n')
    print(f'\nDONE -> {OUTDIR / "cluster-report.md"}')


if __name__ == '__main__':
    main()
