---
type: object
title: EDSP, EDSP? - (EDge SPecification)
layer: L1
stage: timing
tags: [timing, edsp, command, l1, search-edge, ac-test, site-dependent]
related: [timing, psfc, timing-equation-set, spec-set, timing-setup-commands, command-reference, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# EDSP, EDSP? - (EDge SPecification)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,730 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### EDSP

The edge_spec parameter specifies a physical edge (d1 through d8 or r1 through r8):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}
```

The edge_spec parameter is a data parameter (D1, D2, C1, C2, E1, or E2):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}
```

### EDSP?

```
EDSP? [dc_ref], {(pinlist)}
```

returns:

```
EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}
```

Parameters
 |

waveform_set

 |

Specifies a waveform set number for a fixed timing setup.

 |
 |

specset_id

 |

Specifies a spec set ID for an equation based setup. The spec set ID is derived from an equation set number and a spec set number as follows:

100 * equation_set_no + specset_no

 |
 |

multi-port_spec

 |

Specifies the name of a multiport specification for a multi-port setup. PRM is the default value.

 |
 |

timing_set

 |

Specifies the number of the a timing set. PRM is the default value.

 |
 |

edge_spec

 |

The edge specifier can either be a physical edge (d1 through d8 or r1 through r8), or one of the data parameters D1, D2, C1, C2 (drive parameters) or E1, E2 (receive parameters).

 |
 |

edge_number

 |

In the query reply, this parameter contains the edge that is used as leading or trailing edge.

 |
 |

dev_cyc_name

 |

Specifies the name of a logical device cycle that uses the data parameter given as the edge_spec. It must be defined for all pins in pinlist. If you do not enter a name in this parameter, the first device cycle in the device cycle table is used.

 |
 |

dc_ref

 |

This parameter specifies the input edge. The input edge determines the algorithm according to which the trailing edge is selected. The two options are LE (for "leading edge") and TE (for "trailing edge").

The leading edge will always be the first edge that is associated with the specified data parameter within the specified device cycle, regardless of whether LE or TE is specified.

For the trailing edge the following rules apply:

- When you specify LE, trailing and leading edge will be identical.
- When you specify TE, then drive parameters and receive parameters are treated differently.

  - Drive parameter: The trailing edge will be the first drive edge after the leading edge thats performs a data or tri-state action. Note that this trailing edge need not be associated in any way with the data parameter of the leading edge.
  - Receive parameter: If the action of the leading edge is an edge compare, leading and trailing edge will be identical. If it is the start action of a window compare, then the associated window close edge will be the trailing edge.

For both cases, see the example below.

In the query, you can also specify both. In this case both the leading and the trailing edge will be returned for the pins in pinlist.

 |
 |

direction

 |

This parameter can be in or out. If in is selected to define an input edge, then the edge_spec parameter must be D1, D2, C1, or C2. If out is selected to define a receiver edge, then the edge_spec parameter must be E1 or E2. If either in or out is selected along with an edge_spec parameter of 1,2...6, then a check is performed to ensure that the edges of all pins are in the required direction. If no entry is made in this parameter, the measuring edges of the pin in pinlist can have any direction or be unused.

 |
 |

pinlist

 |

The parameters of the EDSP command are applied to all pins named in this parameter. If more than one pin is used, the names must be separated by a comma.

In a multi-port setup, all pins must belong to the same port of the specification that was entered as the first parameter.

 |

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The edge_spec parameter specifies a drive edge, but the direction parameter specifies a compare edge, or the other way round.
- Pins of different periods are included in the pin list.
- You select an unused edge.
- The edge direction of the selected edge is not the same for all pins in the pin list.

<!-- 报错节 end -->

## 是什么

**`EDSP`（EDge SPecification）管的是「timing search 用哪条边」。**

> The EDSP (EDge SPecification) command defines the search edges for the timing searches. Conceptually, there are always two search edges, which are called the leading and the trailing edge.

**三条要点，全部来自开头那三段：**

1. **永远有两条搜索边**——leading 与 trailing。
2. **你只给其中一条**（原文叫它 `input edge`），**另一条由 `EDSP` 自己推出来**：

> You specify only one of these, the input edge, to the EDSP command; the other is inferred by EDSP.

3. **用哪条取决于测试**——原文举的例子是 data hold time test：

> Some AC Tests use the leading edge, the others (for example, the data hold time test) the trailing edge as their search edge.

**`## Application` 一节只有一行**，逐字是 `AC Tests`——**这就是它的适用面**，本篇没有更细的适用说明。

### 输入边的两种给法，物理后果完全不同

> The input edge can be specified explicitly, or implicitly by the combination of a data parameter and a logical device cycle. In the latter case, the wavetable must use logical waveforms.

| 怎么给输入边 | leading 与 trailing 的关系 | 附加要求 |
|---|---|---|
| **显式**：给物理边（`d1`–`d8` / `r1`–`r8`） | **物理上就是同一条边**——原文：`If you specify the input edge explicitly, the leading and the trailing edge will be physically identical.` | — |
| **隐式**：给 data parameter（`D1`/`D2`/`C1`/`C2`/`E1`/`E2`）+ logical device cycle | **`EDSP` 通常会挑出两条不同的物理边**——原文：`then EDSP will usually select different physical edges as the leading and trailing edge.` | **wavetable 必须用 logical waveforms** |

**两条语法形态正好对应这两种给法**（两行都在上「语法 / 参数」节里）：

| 语法行 | `edge_spec` 是哪一种 | 原文那句导语 |
|---|---|---|
| `EDSP …, {edge_spec}, , ,[direction], {(pinlist)}` | **物理边** | `The edge_spec parameter specifies a physical edge (d1 through d8 or r1 through r8):` |
| `EDSP …, {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}` | **data parameter** | `The edge_spec parameter is a data parameter (D1, D2, C1, C2, E1, or E2):` |

**（推断，依据是上面两行的逐字对比）**：第一行里那两个**空的逗号位**（`, , ,`）
正好落在第二行 `[dev_cyc_name]` 与 `[dc_ref]` 的位置上——
**只有「隐式给法」才需要 device cycle 名与 input edge 的选择**，所以那两个空位就是它俩。
**原文没有一句话说明这两个空位是什么**；这是本页按两行对齐推出来的，**不是文档事实**。

### `dc_ref`：trailing edge 怎么算（本页最细的一段）

> This parameter specifies the input edge. The input edge determines the algorithm according to which the trailing edge is selected. The two options are LE (for "leading edge") and TE (for "trailing edge").

**一条与 `LE`/`TE` 无关的总规则**（原文紧跟着这一句）：

> The leading edge will always be the first edge that is associated with the specified data parameter within the specified device cycle, regardless of whether LE or TE is specified.

**trailing edge 的分岔**（原文：`For the trailing edge the following rules apply:`）：

| 你写什么 | trailing edge 怎么定 |
|---|---|
| `LE` | **与 leading 相同**——原文：`When you specify LE, trailing and leading edge will be identical.` |
| `TE` + **drive parameter** | **leading 之后第一条做 data 或 tri-state 动作的 drive edge**——原文：`The trailing edge will be the first drive edge after the leading edge thats performs a data or tri-state action.`，紧接着补了一句：`Note that this trailing edge need not be associated in any way with the data parameter of the leading edge.` |
| `TE` + **receive parameter** | **看 leading 的动作**：是 **edge compare** → leading 与 trailing 相同；是 **window compare 的 start** → **关联的 window close edge 就是 trailing**。原文：`If the action of the leading edge is an edge compare, leading and trailing edge will be identical. If it is the start action of a window compare, then the associated window close edge will be the trailing edge.` |

**`EDSP?` 可以两个都要**：

> In the query, you can also specify both. In this case both the leading and the trailing edge will be returned for the pins in pinlist.

**三处原文没写：**

- **不写 `dc_ref` 会怎样——语料未写。** 语法里它是 `[dc_ref]`（方括号＝可选），但原文没有一句交代省略时的默认值。
- **`both` 的字面怎么写——语料未写。** 原文只说「可以两个都指定」，没有给写法。
- **这一位为什么叫 `input edge`——原文没解释。** 它写在参数节第一句，而紧跟着的总规则却说
  leading edge 与 `LE`/`TE` 无关；**两句话并列在同一段里**。本页**照原文并列，不替它调和**。

### `direction`：是 drive 还是 receive

> This parameter can be in or out. If in is selected to define an input edge, then the edge_spec parameter must be D1, D2, C1, or C2. If out is selected to define a receiver edge, then the edge_spec parameter must be E1 or E2.

**这里的「input」指 DUT 的输入（＝drive），不是边沿的斜率方向。** 原文自己把词摆明了：
`out` 配的是 `receiver edge`。

| `direction` | 配哪些 `edge_spec` | 原文说法 |
|---|---|---|
| `in` | `D1` / `D2` / `C1` / `C2` | `define an input edge` |
| `out` | `E1` / `E2` | `define a receiver edge` |
| **不写** | **`pinlist` 里各针的 measuring edge 可以是任意方向、也可以没被用到** | `If no entry is made in this parameter, the measuring edges of the pin in pinlist can have any direction or be unused.` |

**同一段里还有一条只在这里出现的检查**：

> If either in or out is selected along with an edge_spec parameter of 1,2...6, then a check is performed to ensure that the edges of all pins are in the required direction.

**`1,2...6` 这个写法对不上本篇别处任何一张清单**：`edge_spec` 在别处只有两种写法
（物理边 `d1`–`d8` / `r1`–`r8`，或 data parameter `D1`/`D2`/`C1`/`C2`/`E1`/`E2`，两边都不是 `1,2...6`）。
（推断）它指的是**那六个 data parameter**，**依据是「六个」这个数对得上**；原文没有点明。

### site focus：`EDSP` 是 site 相关的命令

原文用两段讲这件事，**落点不同**：

> With this command you configure setups of those sites that have the setup focus: For more information, see also: PSFC, PSFC?.

> With this command you can retrieve site specific information (only one site can be in focus at a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools. Also, any firmware queries report setup and results for the site currently in focus only.

**第一句写「写」，第二句写「读」**：配置只写有 setup focus 的 site；
读回来的信息也只属于当前 focus 的那个 site，**连 firmware query 也一样**。

### `EDSP?` 返回的是「哪条边」，不是时间值

> The EDSP? query returns the current settings.

返回行的形状在上「语法 / 参数」节里：`EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}`。
`edge_number` 的定义是 `In the query reply, this parameter contains the edge that is used as leading or trailing edge.`
——**它给的是边的编号**。**本篇没有一句讲边的时刻值**（本页只读了一篇，
所以这是「本页没见到」，不是「它不存在」）。

## 典型用法

**先把范围说清：本篇没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`。**
所以「先干什么再干什么」本页不写——按 §2.1，流程是 stage 页的事。
本篇能给的过程性材料只有三条：`## Application` 一行、参数之间的硬约束、以及一个**引不到的**例子。

**1. 适用面**：`## Application` 逐字是 `AC Tests`——**只管 AC 测试**。

**2. 三种形态**（下表**每一行都标了依据**）：

| 目的 | 形态 | 依据 |
|---|---|---|
| 用物理边指定搜索边 | `EDSP [waveform_set\|specset_id\|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}` | 本篇第一个语法行 |
| 用 data parameter + device cycle 指定 | `EDSP [waveform_set\|specset_id\|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}` | 本篇第二个语法行 |
| 问回当前设置 | `EDSP? [dc_ref], {(pinlist)}` | 本篇 `## EDSP?` 一节 |

**原文没有给任何一条带具体值的例子**，所以「一条真敲出来的 `EDSP` 长什么样」本页给不出。

**3. 三条硬约束（本篇写明的因果关系，只有这三条）**：

- **隐式给输入边时，wavetable 必须已经用 logical waveforms**——原文：`In the latter case, the wavetable must use logical waveforms.`
- **`dev_cyc_name` 必须对 `pinlist` 里每一根针都定义好**——原文：`It must be defined for all pins in pinlist.`；
  **不写就取 device cycle 表里的第一条**——原文：`If you do not enter a name in this parameter, the first device cycle in the device cycle table is used.`
- **多端口设置下，`pinlist` 里所有针必须属于第一个参数指定的那个 port**——原文：`In a multi-port setup, all pins must belong to the same port of the specification that was entered as the first parameter.`

**4. site 前提**：要**写** setup，那个 site 必须已经有 setup focus；要**读**，读到的只属于当前 focus 的那个 site（两段引文见「是什么」）。

**5. 报错边界**：四种情形（drive/compare 写反、`pinlist` 里针的周期不同、选了没被用到的边、各针边方向不一致）——**照上「报错条件」一节，本页不复述。**

**6. ⚠️ 本篇点名的那个例子，本篇里没有。** `dc_ref` 那一节末尾逐字写着
`For both cases, see the example below.`——**而全篇没有任何 `Example` 段**
（实测 `Example` 出现 **0** 次；上游 `.htm` 里也是 0 次，见「出处」）。**这句指引落空，本页照实记。**

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[timing]] | **本页 `stage: timing` 的理由**：它管的是 timing search 的边沿 | frontmatter |
| [[psfc]] | **本篇正文唯一链出去的一篇**（原文：`For more information, see also: PSFC, PSFC?`）。关系是**同一件事的两半**：`EDSP` 配的是「有 setup focus 的 site」，`PSFC` 管的是**怎么把 site 放到 focus 上** | 本篇正文（**文档事实**） |
| [[timing-equation-set]] | **`specset_id` 的算法里含 `equation_set_no`**——原文：`The spec set ID is derived from an equation set number and a spec set number as follows:` + `100 * equation_set_no + specset_no` | 本篇参数节（**文档事实**） |
| [[spec-set]] | **`specset_id` 就是 spec set ID**（原文：`Specifies a spec set ID for an equation based setup.`）。**它和 `waveform_set` 是一对**：那一栏写的是 `for a fixed timing setup`——**fixed 与 equation based 两种 setup 在这里分岔** | 本篇参数节（**文档事实**） |
| [[timing-setup-commands]] | **归属**：`EDSP` 被列在该章的 timing setup commands 清单里 | **对外核对**：`02.06.06.02_List_of_timing_setup_commands.md` 第 21 行（本页只 `grep` 了这一行，见「出处」） |
| [[command-reference]] | **本篇定义文档所在的章**（`02.06_Command_Reference`）。这一章**不逐篇建页**（§12.1），本页是这一章里被单独建页的少数之一 | §12.1 + 本页 `sources:` 的路径（**项目约定**） |
| [[smartest-6.3.2]] | **版本哨兵值**指向的版本页（见下节） | 本篇 `## Functional changes`（**文档事实**） |

**两条来自 `extract/edges.jsonl` 的线索**（**计数产物，不是文档事实**）：

| 谁 | 原句（`edges.jsonl` 的 `context` 栏） | 边数 | 本页的处置 |
|---|---|---|---|
| `EDDC` | `The EDDC? query is completely independent of the definitions made with EDSP` | **4**（4 份投放各 1 条） | **本页没读 `EDDC`**，所以「两者怎么算独立」答不了 |
| `TTRS` | `The edge used for the search is selected with EDSP, EDSP? - (EDge SPecification)` | **4**（2 份投放各 2 条） | **本页没读 `TTRS`**；这句只说「它用 `EDSP` 选出来的边」 |

`EDDC` 与 `TTRS` **两个名字都不在链名清单（`extract/prose-allowlist.txt`）里、也都还没有页**——
所以这里只能写反引号。

**本页答不住的**：除了原文举的 data hold time test，**还有哪些 AC 测试用 trailing edge**——本篇只举了一个例子。

## 版本

**本文档有 `## Functional changes` 段，里面只有一行**：

- `Introduced before SmarTest 6.3.2`

**这一行是哨兵值，不是「6.3.2 新增了 EDSP」。** 按 §11.2②，
`Introduced before SmarTest 6.3.2` 的意思是「**在本语料覆盖范围开始之前就已经有了**」——
语料里 2,677 条可用性行都写这同一个版本号，**照字面读会读出一条假信息**
（「6.3.2 一次新增了 2,677 个功能」）。**所以本页没有版本门槛可报**；
哨兵值本身的说明在 [[smartest-6.3.2]]。

**版本段里没有的东西**：**没有一条 `SmarTest X.Y.Z:` 形式的变更记录**。
所以「`both` 是哪个版本加的」「那两个空逗号位是哪个版本留的」**在本篇里查不到——语料未写**。

（推断）`EDSP` 在 **SmarTest 7.10.3** 上可用——依据是「它早于 6.3.2」这条文档事实，
加上 7.10.3 晚于 6.3.2；**本页没有在任何机台上印证过。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.md`
（TDC `98589.htm`）。**整篇读完。**

### 数是怎么量的（§11.5 的口径）

| 数 | 值 | 怎么量的 |
|---|---|---|
| 字节 | **5,967** | `len(path.read_bytes())`（即 `st_size`）。**不是** `len(read_text())` |
| 行数 | **171** | `wc -l`（**不 +1**；本语料末行都带换行） |
| 换行 | **171 个全 CRLF、裸 LF 0 个** | 所以 `len(read_text())` 会给出 **5,796**（**恰好少 171 = 行数**）——本页不拿 5,796 当字节数 |
| 代码块 | **4** | `docs.jsonl` 的 `code_blocks` |
| 标题 | **6**（1 个 H1 + 5 个 H2） | `docs.jsonl` 的 `heading_count` |
| 出边 | **1** | `docs.jsonl` 的 `out_degree: 1`、`link_kinds: {"doc": 1}`——**正文里只有一个链接**（指 `PSFC`） |

### 这一篇在语料里有 4 份投放（本页核过）

| 路径（相对 `by-category/` 的尾巴） | `source_topic` | `st_size` |
|---|---|---|
| **`…/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.md`（本页 source）** | **`98589.htm`** | **5,967** |
| `…/02.06_Command_Reference/02.06.06.02.12_EDSP__EDSP__-__EDge_SPecification.md` | `98589_2.htm` | 5,968 |
| `…/02.06_Command_Reference/02.06.09.02.05_EDSP__EDSP__-__EDge_SPecification.md` | `98589_3.htm` | 5,968 |
| `…/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.12_EDSP__EDSP__-__EDge_SPecification.md` | `98589_4.htm` | 6,006 |

**前三份剥掉 frontmatter 之后逐字节相同**（body 都是 **5,773** 字节，
`sha256` 前 16 位同为 `5bf4271ae54abec9`）；**第四份不同（body 5,800 字节）**，
差的那 **27** 字节是**链接前缀**：镜像那一份把
`[PSFC, PSFC?](<02.06.02.02.191_…>)` 写成了 `[PSFC, PSFC?](<../02.06_Command_Reference/02.06.02.02.191_…>)`
（多一层 `../`），**正文一个字没差**。
判据是 §10 第 0 条：`source_topic` 去掉 `_N` 后缀后相同 → 同一篇 TDC 页。

> **所以 `EDSP` 这一篇被投放了 4 次，不是 4 处独立证据。**
> **本页只把 `02.06.02.02.102` 当来源**；其余三份只做了哈希与逐行对差，**没有当成证据读**。

### 上游 `.htm` 核过：**逐字比对，内容一个字没丢**

四份对应的 `raw/98589.htm`、`98589_2.htm`、`98589_3.htm`、`98589_4.htm` **都存在，各 12,083 字节**。
把 `.htm` 与 md 都拆成词、取集合差，结果是：

| 只出现在 `.htm` 里 | 只出现在 md 里 |
|---|---|
| `Topic`、`98589`，以及 **`l eading`**（HTML 的 `<span>` 把 `leading` 拆断，**是 `.htm` 自己的断行，不是内容差异**） | **只有链接路径的字面**（`02`、`06`、`191_PSFC__PSFC__`、`__Parallel_Setup_FoCus`、`md` 这五段） |

**结论：这一篇 md 相对上游 `.htm` 没有内容丢失。** 所以下面三处瑕疵
**上游 `.htm` 里就是那样**——属于 §11.2 ⑥ 说的「**上游就坏的（救不回来）**」，
**不是** ① 那种转换损坏。

### 对外核对（本页唯一一处 `sources:` 之外的材料）

`EDSP` 属于哪一类命令，**本篇的 `## Application` 只写了 `AC Tests`**，答不了。
本页为了给「和谁有关」一个可核的归属，**只 `grep` 了同章一份索引的第 21 行**：

| 打开的是 | 读了什么 | 拿到什么 |
|---|---|---|
| `02_System_reference/02.06_Command_Reference/02.06.06.02_List_of_timing_setup_commands.md`（4,511 字节，55 行） | **只 `grep` 了含 `EDSP` 的那一行**（第 21 行） | 一行逐字：`- [EDSP, EDSP? - (EDge SPecification)](<02.06.06.02.12_EDSP__EDSP__-__EDge_SPecification.md>)` → **`EDSP` 在 timing setup commands 的清单里** |

**这一份是纯清单**（55 行，整篇就是命令名列表），**本页只取了上面那一条**，
**它的正文内容一个字节都没进本页**。处置与 `wiki/objects/eqsp.md` 的「对外核对」一节同一套。

### 本页没做的

- **没有实跑。** 没在机台上发过 `EDSP` / `EDSP?`，**没有验证过 leading / trailing 到底怎么挑**。
  `verified: doc-only` 指的就是这件事。
- **原文点名的那个例子本页没有**（因为它不存在）——见「典型用法」第 6 条。
- **`PSFC` 那一篇没读**——所以「怎么把 site 放到 setup focus 上」本页只有原文那一句指引。
- **`EDDC` / `TTRS` 两族没读**——它们与本页的关系只有 `edges.jsonl` 里那句原句。
- **`timing-setup-commands` 那一章整章没读**——本页只从那章的清单里取了 `EDSP` 这一行。
- **`Data hold time test` 那篇没读**——原文只把它当「用 trailing edge 的例子」提了一次。
- **图**：本篇对 `raw/` 的引用 **0 处**（`.png` / `.jpg` / `.jpeg` / `.gif` / `![` / `<img` / `raw/`
  七种写法**全部 0 命中**）——**所以本页没有任何来自图的结论，没有图证。**
- **没有动 `wiki/index.md`**，也没有动任何别的页。

### ⚠️ 本篇的三处瑕疵，本页照实记下、一处都没替它改

> **① 原文点名的例子不存在。** `dc_ref` 那一节末尾逐字写着
> `For both cases, see the example below.`——**而全篇 `Example` 出现 0 次**
> （上游 `raw/98589.htm` 里也数到 **0** 次）。**这句指引落空**：
> 读者按它去找例子，找不到。**上游如此，本页不替它补一个例子。**

> **② 两处语法笔误**（上游 `.htm` 逐字相同，见上「上游 `.htm` 核过」）：
> `Specifies the number of the a timing set.` 里的 **`the a`**；
> 以及 `The trailing edge will be the first drive edge after the leading edge thats performs a data or tri-state action.`
> 里的 **`thats performs`**。两处**本页引用时原样抄**，没有改成 `a` / `that performs`。

> **③ 第二个语法行在 `[dc_ref]` 与 `,[direction]` 之间多一个空格。**
> 逐字是 `[dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}`；
> **同篇第一个语法行的对应位置没有这个空格**（`{edge_spec}, , ,[direction], {(pinlist)}`）。
> **原文如此**，本页一个字没动——它在「语法 / 参数」节里，按 §4 不许改。

另记一处**不是瑕疵、是留白**：`direction` 参数里的 `1,2...6`
（`an edge_spec parameter of 1,2...6`）与本篇别处给的两套写法都对不上——**见「是什么」那一节**。
**这个 `...` 是原文自己的**，本页引用时**原样保留**，没有补全成 `1,2,3,4,5,6`。

`verified: doc-only`
