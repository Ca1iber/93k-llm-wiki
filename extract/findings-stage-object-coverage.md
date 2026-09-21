# 待处置：70 个对象页，没被「自己那个阶段」的脊椎页点名

发现时间：2026-09-21
发现方式：查 `stages/` 与 `objects/` 怎么连起来时顺手量的——
**十五类检查一个都不管这件事**（不是漏报，是根本没这一类）。

## 现象

`objects/` 共 **196 页**。其中 **70 页**没出现在它 `stage:` 字段所指那页脊椎页的
「涉及对象」节里。

| 阶段 | 没被点名的 | 该阶段对象总数 |
|---|---|---|
| testmethod | **22** | 38 |
| pattern | **13** | 22 |
| level | **9** | 24 |
| project | **8** | 26 |
| pin | **7** | 28 |
| results | **7** | 18 |
| testflow | **2** | 13 |
| run | **2** | 12 |
| timing | **0** | 15 |
| **合计** | **70** | 196 |

**这 70 样不是空的、也不是缺页**——页都建好了、内容都在。缺的是**从阶段页走过去的路**。
抽样（完整清单见文末复核脚本的输出）：

- 命令：`conf`（CONF）、`ctxt`（CTXT）、`sqst`、`pste`、`psas`
- 文件格式：`apg-pattern-file`、`pin-mapping-file`、`structure-of-a-tmlimits-csv-file`
- API：`smartrdi`（**164 KB，全库最大的一页**）、`smartcalc`
- GUI：`pattern-tool`、`protocol-editor`、`analysis-views`、`raw-data-views`

**反向的数**：九页脊椎页的「涉及对象」节合计点名 **250 次**，
其中 **147 次**指向真实存在的页，**103 次**是悬空的（与 [[findings-dangling-backlog]] 那笔账同源）。

## 这算不算错——**规矩没定，所以判不了**

`schema.md:70` 对「涉及对象」一节的原文只有一句：

> 本阶段用到的命令 / API / 文件 / 工具，链接到各自的 [[object]] 页，并标明层级。

**说了「要链接、要标层级」，没说「必须列全」。**

而 `stage:` 这个字段（`schema.md` §6）的定义是**「读者该去哪一段里找它的用法」**。
按这个读法，那 70 页当然算「本阶段用到的」，该列。

**两种读法都通，规矩自己没定死。** 这不是「作者偷懒」，是**规格没有覆盖到这个问题**——
和 [[findings-stale-unbuilt-marks]] 里那条「判据查的是有没有悬空，错的是声称悬空」是同一个形状：
**错落在所有判据的缝里，而这一次连「错」都还没定义。**

## 一个能确定的好消息

**这 70 页没有变成孤儿。** 196 页全部列在 `wiki/index.md` 的对象节里
（第十四类甲在管这件事），**从入口都走得到**。所以这是「少了一条路」，不是「找不到」。

## 复核办法

```bash
cd F:\master-dev\understand-anything-wiki\wiki
python -X utf8 - <<'PY'
import re, pathlib, collections
obj = {}
for p in pathlib.Path('objects').glob('*.md'):
    fm = p.read_text(encoding='utf-8')[4:].split('\n---\n', 1)[0]
    g = lambda k: (re.search(r'^' + k + r':\s*(.*)$', fm, re.M) or [None, ''])[1].strip()
    obj[p.stem] = (g('stage'), g('layer'), g('title'))
miss = collections.defaultdict(list)
for k, (st, ly, ti) in sorted(obj.items()):
    if not st: continue
    if f'[[{k}]]' not in pathlib.Path('stages', st + '.md').read_text(encoding='utf-8'):
        miss[st].append((k, ly, ti))
n = sum(len(v) for v in miss.values())
print('没被点名的：', n, '/', len(obj))
for st in ['project','pin','level','timing','pattern','testmethod','testflow','run','results']:
    for k, ly, ti in miss[st]:
        print(f'  {st:<11} {k:<44} [{ly:<4}] {ti[:40]}')
PY
```

## 处置 —— **未处置**

两条路，**选哪条是人的决定**，因为它是取舍不是对错：

- **(a) 补路**：把 70 个补进各自阶段页的「涉及对象」节。
  代价：九页会变长，而「涉及对象」是**读的人用来快速找入口**的，
  列全 38 个反而可能淹掉真正重要的那几个。
- **(b) 定规矩**：在 `schema.md` §6 写明「脊椎页不要求列全，只列主用的」，
  并说明怎么算「主用」。代价：`stage:` 字段「去哪一段找它」的用处打折——
  有 70 样东西，读者按阶段找是找不到的。

**在选定之前，这 70 页只能靠 `index.md` 和页间的 `[[双链]]` 找到，不能靠阶段页。**

## 与另外两件事的关系

- [[findings-dangling-backlog]]：那边是「清单里有、页没有」（**要建的没建**）；
  这边是「页有了、阶段页没链过去」（**建好的没挂上**）。
- [[findings-duplicate-titles]]：同一批页面的 `title` 问题，同一轮查出来的。
