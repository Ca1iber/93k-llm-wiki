# 待处置：`objscaffold.py` 的语法节漏掉「语法行」本身

发现时间：2026-09-21
发现方式：写 `wiki/objects/dtcp.md` 时，发现该页「语法 / 参数」节里**没有语法行**，
顺着查下去发现不是孤例。

## 现象

有些命令页的「语法 / 参数」节**只有 `### Parameters`（以及 `### Example(s)`），
完全没有那条 `CMD {参数}` 语法定义行**。

已核实的例子（都逐条回 raw 对过）：

| 页 | raw 里的语法行 | 语法节里有没有 |
|---|---|---|
| `dtcp` | `DTCP {"key"}, {"value"}` / `DTCP? {"key"}` | **没有** |
| `pste` | `PSTE {sites}` / `PSTE {sites\|"site_string"}` | **没有**（该页第 131 行那个是**写页人自己补的表格**，不是脚本抽的） |
| `pqfc` | `PQFC {site}` / `PQFC?` | **没有** |

## 原因

`extract/objscaffold.py` **只认 `Syntax` / `Parameters` / `Example` 三个段名**
（其注释第 6 行、第 190 行写明了这个设计）。

而语料里有一批命令页**不写 `## Syntax`**，而是把语法直接放在
**以命令名命名的二级标题**底下，例如：

```
## DTCP
```
DTCP {"key"}, {"value"}
```
## DTCP?
```

于是脚本认出同篇的 `## Parameters`、`## Examples`，**却认不出语法那一节**，
语法节就成了「有参数表、没有语法」的样子。

## 影响面

用「语法节区间里找不到 raw 那行语法」扫过全部 229 个带语法节的页，
命中 **22 页**（只查了每页第一条 source，因此是**下界**）：
`conf` `ctxt` `dfge` `dfgp` `dfpn` `dfps` `dfpt` `dscp` `dtcp` `eqsp` `jscf`
`jsdf` `jspr` `pals` `pqfc` `psfc` `pste` `sprm` `sqst` `svlr` `timing-equation-set` `uptd`。

**其中相当一部分是已经建好、且已经过 `check_syntax_fresh.py` 的页**
（`pste` / `psfc` / `dfgp` / `dscp` / `uptd` / `sprm` …）。
`check_syntax_fresh.py` **查不出这一类**——它比对的是「页面里的块 == 脚本会生成的块」，
而脚本生成的就是这个漏了语法行的版本，所以它一路报「过期 0」。

## 归类

按本工程的对账规矩，这是 **(a) 脚本 bug**——不是语料如此，也不是基线工具不精确。

## 建议的修法（**2026-09-24 已执行** —— 见文末「处置」）

1. `objscaffold.py` 的段名表里**增加一条**：二级标题等于本篇命令名
   （或「命令名 + `?`」）时，也当语法段处理；
2. 跑 `objscaffold.py --refresh-syntax`；
3. 重跑 `check_syntax_fresh.py`，并抽查上面那 22 页的语法节。

## 为什么没有当场就改

`--refresh-syntax` 会**一次性重写 229 页的语法节**。
此刻正有一批写页工作在落盘（本次运行中 55 页里已完成 51 页），
**这时候动全库的脚本生成块，会让「页里的块和脚本输出对不上」这个状态
出现在几十页上，且分不清是谁造成的**。
所以先落成这一份记录，把原因、影响面、修法都钉死，由主会话（或人）决定何时执行。


---

## 处置 —— 2026-09-24 已执行

**判据取文档自己，不取我的口味。** 段名要和正文**互相印证**，两条之一即可：

1. **正文首行就是段名本身**（跳过可有可无的开头围栏）—— `BDID {-1|0|2|3}, {"string"}`；
2. 段里有**代码围栏**—— `EDSP` 先是一句导语（"The edge_spec parameter specifies…"），
   围栏紧随其后。

**为什么必须有这层印证，不能只看段名。** 文档标题是**一串术语**时
（`Definitions, Vector, Pattern, Burst, …`），按逗号拆出来的名字会多出几个，
而它们在正文里是**别的小节**：`## Pattern` 的正文是
「A pattern is a sequence of vectors and sequencer instructions.」——**那是散文**。

**全语料候选 632 处 / 331 篇**（判据：H2 名 == 文档标题头里那串命令名之一）：

| | 处 |
|---|---|
| ① 正文首行即段名 | 614 |
| ② 只有围栏、首行不以段名开头 | 12（`EDSP` / `PCLK` / `PCLK?` / `DMAS?`） |
| ③ 两条都不满足 —— **不收** | 3（`Pattern` / `Burst` / `Virtual Pins editor`） |
| ④ 空段 —— 本来就不收 | 3 |

**改法与影响面**（`objpack.verbatim_sections` 加 `aliases` 参数，**默认空集 = 旧行为**）：

- 逐页对差：**22 页**的语法节要变，合计 **+266,552 字符**
  （`command-reference` 一页 +223,234；`timing-setup-tool` / `timing-setup-commands` 各 +19K）
- **没有一页掉段** —— 28 个候选里「掉了哪些段」那一列全空：
  原先走兜底（子主题 / 管道表格）的页**没有被挤掉**
- `--refresh-syntax` 重刷 22 页；**再刷一遍 22/22 报「无变化」**（幂等）
- **语料一个字没动** —— 这是脚本 bug，改的是下游
- `check_syntax_fresh.py`：一致 229 / **过期 0 / 该有却没有 0**；
  总闸 13 类全绿，EXIT=0

### 本节开头那张「22 页」的表，与本次变的 22 页**只重合 19**

差的 3 页**不是这一个病**，**一个字没动**：

| 页 | 症状 | 归类 |
|---|---|---|
| `jsdf` | 文档自己的二级标题写成 `## JDSF` / `## JDSF?`（**字母前后颠倒**），而标题与文件名都是 `JSDF` | **(c) 语料本身** —— 原厂笔误 |
| `svlr` | 语法藏在 `## For single-port specifications` / `## For multiport specifications` / `## For both types of specifications` 底下，**全篇没有以命令名命名的 H2** | **(a) 又一条脚本 bug，但是另一个形状** |
| `timing-equation-set` | 该文档**通篇没有语法**（只有 `## Related information` / `## Functional changes`），页面空着是**对的** | **(b) 基线工具不精确** —— 当初那次扫描从「页面没有语法行」推出了「文档有」 |

`jsdf` 要改的是 raw 里那个标题（§1.2：先摆证据、经人批准）；
`svlr` 要新写一条判据 ——「描述性标题底下的语法」没有现成的互证办法，
判宽了就是把散文当语法收。

**并记一个输出里的符号是反的**（**没有顺手改**，§1.2 的「不许顺手改旁边」）：
`refresh()` 印「整页 X → Y 字符，−N」，那个 N 算的是 `len(改前) − len(改后)` ——
**页面变长时它是负的**，于是「`115,885 → 138,305`，`-22,420`」这句话里，
箭头和数字**互相打脸**。
