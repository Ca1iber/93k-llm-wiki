"""给 ③ 的候选表**逐行定归宿**。机械，零 LLM，零网络。

## 它解决的是什么

`schema.md` §12 让脚本先抽「哪些约束存在」，产出 `constraint-candidates.csv`。
问题是这张表**没有完成判据**：「253 行建了 6 页」听起来像欠着 247 页，
而 247 页显然不该建（§3：不镜像目录树）。**「先放着」不算归宿**（本项目立过的规矩），
所以要么按候选建，要么**给每一行一个说得清的归宿**。这个脚本做后者。

## 归宿是怎么定的（**规则就三条，按顺序第一条命中即止**）

| # | 判据 | 归宿 | 依据 |
|---|---|---|---|
| 1 | `n_doc == 1` | **重复投放**——候选的「≥4 篇」全部来自**同一篇文档**在多个分类树里的副本。**不建页。** | §11.2 ④ / 第十类 |
| 2 | 命中版本事实正则 | **版本事实**——归宿是 `wiki/versions/` 的 142 页。**这类根本不该出现在表里。** | 见下 |
| 3 | 其余 | **非约束**（参数语法样板 / 单对象属性）——归宿是**它所属对象的页**，不单独建页。 | §2.4 / §4 |

- **第 2 档恒为 0，非 0 就是红的。** `constraints.py` 的 `NOT_CONSTRAINT` 就在上游把这类滤掉了；
  本脚本**导入同一个正则对象**（不是照抄一份），所以两处判据不会漂移。
  这里出现非 0，只可能是「上游改了而这里没跟上」，**不是语料问题**。
- **`n_doc` 不是 `docs`。** `docs` 数的是**文件**；语料把同一篇文档重复投放在多个分类树下，
  所以 `docs` 会虚高。`n_doc` 数的是**去掉分类号前缀后的标题**，即真正的独立文档。
  折掉投放后，**253 行里有 27 行的「独立文档数」是 1**——
  即它们连「≥4 篇文档复现」这个入选理由本身都是假的。

## ⚠️ 第 3 档是**补集**，不是「我判定了它不是约束」

这个区别必须说清，否则这一列就是假的。**我没有可检验的「是不是约束」分类器**：

- 试过写一个「含前置关系词」的正则，拿 6 个已建 `constraints/` 页的引文当阳性对照，
  跑出 5/8。**但查下去发现，3 个漏判是「我的对照组抽取器」抽错了引文，
  不是正则漏了约束。** 也就是说我连它的**真阳性率都还没测准**。
- 与其出厂一个**误差率未知**的分类器再把它叫「归宿」，不如说清楚：
  第 3 档 = **不属于前两档的行**。它里面**一定混着真约束**。

## ⚠️ 反过来：**表里没有 ≠ 语料里没有**

`constraints.py` 的入选门槛是「≥4 篇文档复现」。真约束**会被它漏掉**：
`wiki/constraints/pin-config-locked-during-test.md` 的 `⚠️` 记着一条实例——
「固件在测试运行中不接受任何配置改动」这条真规矩**只出现在 2 篇文档里、
且都写在章首 Note**，按 `docs` 排序进不了候选头部。
**所以建页时不许把 253 行当全集，也不许把「不在表里」当成「没有这条规矩」。**

## 为什么不按「已建页认领了它的文档」定归宿（旧版就栽在这）

第一版规则是 `cov` = 候选的文档落在某个已建页 `sources:` 里的比例。跑出来：

- **第 2 档（`cov >= 1.0`）恒为空**——6 个 constraint 页各只认领几篇文档，
  而候选动辄横跨 20 篇，**全额认领几乎不可能**。规则里的一档**根本不存在**。
- 第 3 档印成「**部分认领：`stages/run.md`（还差 19 篇没页）**」。这句话
  **读起来像归宿，实际是巧合**：它的意思只是「这 20 篇里有一篇正好是 `run.md` 的出处」，
  和「这条约束归 `run.md` 管」**不是一件事**。

**一个印出来的数不支撑它旁边那句话，就是假绿。** 所以那一版作废，
换成现在这条**不依赖 `sources` 图**的规则。

## `前置词` 那一列：**旁证，不是判据。** 归宿不由它决定。

留着它只是给手工过滤 253 行的人一个**透明的**抓手——「这句话里有没有第二个对象
或时间关系」。**它的误判率没有度量过**（见上），所以列名是 `前置词`
而不是 `归宿`，`disposition` 也不看它。
"""
import collections
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDS = HERE / 'constraint-candidates.csv'

sys.path.insert(0, str(HERE))
import constraints as C          # **同一个正则，不是照抄一份**（见 docstring 第 2 档）

# 「有第二个对象 / 有时间关系」的粗筛。**旁证。**
PREREQ = re.compile(
    r'(?:\b(?:before|after|not\s+until|ahead\s+of|already|'
    r'in\s+order\s+(?:to|for)|while|during|as\s+long\s+as)|'
    r'\bthe\s+same\b|\bmust\s+match|\bmust\s+be\s+identical\b|\bconsistent\b|'
    r'\bmust\s+have\s+been\b|\bhas\s+to\s+have\s+been\b|\bneed(?:s)?\s+to\s+have\s+been\b|'
    r'\bonly\s+(?:be\s+)?issued\s+after|\bcan\s+only\s+be\s+used\s+after|'
    r'\bmust\s+be\s+used\s+before|\bbefore\s+any\s+other|\bmust\s+be\s+in\s+the)', re.I)

DERIVED = ('n_doc', 'disposition', '前置词')


def title_of(rel):
    """去掉分类号前缀的标题——**这一篇文档的身份**，重复投放的副本共享它。"""
    s = rel.rsplit('/', 1)[-1]
    if s.endswith('.md'):
        s = s[:-3]
    return re.sub(r'^\d+(\.\d+)*_', '', s)


def dispose():
    # **本列是派生的，不是原料。** 上一次跑留下的三列要**先丢掉再算**——
    # 否则第二次跑会读到自己上次写的 `n_doc`，然后**再追加一遍**，
    # `DictWriter` 拿到重复的 `fieldnames` 就崩（或者更糟：静默写歪）。
    # 这条同时保证**重跑幂等**：同一份 `constraints.py` 产出，跑几次都是同一张表。
    raw = list(csv.DictReader(CANDS.open(encoding='utf-8')))
    base_fields = [k for k in raw[0] if k not in DERIVED]
    rows = [{k: v for k, v in r.items() if k in base_fields} for r in raw]

    out, buckets = [], collections.Counter()
    for r in rows:
        rels = [x for x in r['rels'].split(';') if x]
        n_doc = len({title_of(x) for x in rels})
        pre = bool(PREREQ.search(r['text']))

        if n_doc == 1:
            disp, bucket = '重复投放（同一篇的副本；不建页）', '1-重复投放'
        elif C.NOT_CONSTRAINT.search(r['text']):
            # 恒为 0。非 0 = 上游改了判据而这里没跟上，**报红，不许当语料问题记**。
            disp, bucket = ('**上游漏网**：版本事实不该出现在这里'), '2-版本事实(应恒为0)'
        else:
            disp = '非约束（语法样板/单对象属性）→ 归宿是它所属对象的页'
            bucket = '3-非约束（补集）'
        buckets[bucket] += 1
        out.append({**r, 'n_doc': n_doc, 'disposition': disp,
                    '前置词': '有' if pre else ''})

    fields = base_fields + list(DERIVED)
    with CANDS.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    return buckets, out


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    buckets, out = dispose()
    n = sum(buckets.values())
    print(f'✅ 候选表归宿已重算：{CANDS.name}，{n} 行，'
          f'**每一行都有一档**（没有第四档）：')
    for k in sorted(buckets):
        print(f'    {k:24} {buckets[k]:4} 行')
    leak = buckets.get('2-版本事实(应恒为0)', 0)
    print(('    ✅ 第 2 档为 0——上游 `NOT_CONSTRAINT` 与本脚本同源，没有漏网。'
           if not leak else
           f'    ❌ **第 2 档 {leak} 行**：上游漏了版本事实，去查 `constraints.py`。'))
    pre = sum(1 for r in out if r['前置词'])
    print(f'\n旁证：{n} 行里 **{pre} 行**含前置关系词（`before`/`the same`/`must have been`…）。'
          f'\n  **这一列是旁证不是判据，误判率没度量过**——见脚本文档字符串。'
          f'\n  它 **不参与** `disposition`；列名不叫「归宿」就是为了这个。')
    print('\n> **第 3 档是补集，不是「我判定了它不是约束」**——它里面一定混着真约束；'
          '\n> **而表里没有也不等于语料里没有**（`docs≥4` 会漏掉只写在 2 篇里的真规矩）。')
    return buckets


if __name__ == '__main__':
    main()
