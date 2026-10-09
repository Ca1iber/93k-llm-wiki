---
type: object
title: Data organization of equation based timing
layer: file
stage: timing
tags: [timing, timing-file, equation-set, wavetable, specset, timing-set, eqsp, eqfs, spec-variable, timing-specification, duplicate-investment]
related: [timing, mapping-timing, timing-equation-set, timing-specification, wavetable, wavetable-file, timing-master-file, spec-set, spec-variable, timing-spec, timing-setup-tool, spec-tool, eqsp, eqfs]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.01_Data_organization_of_equation_based_timing.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.04_Example_of_the_equation_based_timing_setup_file.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Data organization of equation based timing

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **149 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.01_Data_organization_of_equation_based_timing.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The following figure exemplifies the structure of equation based timing by a schematic setup:

 !`Timing Specifications`（raw: `../../../../raw/10596.png`）

<!-- 语法节 end -->

## 是什么

**这一页讲的不是一个工具，而是一份文件怎么组织**：equation based timing（基于方程的时序）
把一次 timing 拆成**三块数据**——**equation set（方程集）/ wavetable（波形表）/ spec set（值集）**——
本页说清这三块各装什么、谁指谁、以及在文件里长什么样。`layer: file` / `stage: timing`。

原文第一句就是这套东西存在的理由：

> 「With equation based timing, you can use variables in the definitions of edge positions and period lengths. This allows you, for example, to define general relations between period length and edge delays which are preserved when the value of the variable is changed (for example, place an edge in the middle of a tester cycle for different cycle lengths).」

**一句话：把「边沿位置 / 周期长度」写成含变量的表达式；变量一改，关系不变。**
原文举的那个例子就是典型诉求——**让边沿永远落在 tester cycle 的正中间，不管周期多长。**
这也是「方程」两个字在这份文件里的实际含义：**存的是关系，不是数值。**

三块数据的清单：

> 「Equation based timing setups consist of three main types of data collections:」

| # | 数据块 | 装什么 | 原文给的指路（那三篇本页都没读） |
|---|---|---|---|
| 1 | **equation set** | timing set 与变量定义 | `Setting delays and periods` |
| 2 | **wavetable** | 波形 | `Defining waveform shapes` |
| 3 | **specification set（spec set）** | 变量的值 | `Defining the timing specification` |

**一块文件里三样都可以有很多份，而「这次用哪一份」由 timing specification 说**：

> 「One timing setup file can contain several instances of each of these three types. A timing specification defines which equation set, wavetable, and value set for the variables is to be used in a test. A timing setup file can contain several timing specifications.」

### 一条硬边界：能下载、能查、能运行期改，**就是不能靠固件命令编辑**

> 「The data collections are downloaded with the EQFS and EQSP commands. The collections themselves cannot be edited with firmware commands. But you can query their content with firmware commands, and also change definitions at runtime.」

| 想干的事 | 能不能 |
|---|---|
| 把三块数据**下载**进去 | 能——用 [[eqfs]] / [[eqsp]] |
| **查询**它们的内容 | 能——原文 `you can query their content` |
| **运行期改**定义 | 能——原文 `also change definitions at runtime` |
| 用固件命令**编辑正文** | **不能**——`cannot be edited with firmware commands` |

**这一句把「固件层能做什么」划得很清楚**：能搬整块、能查内容、能改运行期定义——
**就是不能编辑那三块数据的正文**。**「正文怎么改、这些文件由谁写」不在本页**——
**本页两篇 sources 里一个字都没提 GUI 编辑器工具。**

### 三块数据各自的规定

#### ① equation set：三个板块，**顺序固定，只有一种必填**

原文给的顺序是 `Their main building blocks are in this order:`，三块：

| 顺序 | 段 | 必填？ | 装什么 |
|---|---|---|---|
| 1 | `SPECS` | **可选** | **base variables（也叫 spec variables）**——只声明、**不赋值** |
| 2 | `EQUATIONS` | **可选** | **derived variables**——形式是 `var_name = expression` |
| 3 | timing set | **至少一个** | 边沿延迟与周期（见下） |

> 「Timing sets are the only mandatory part of an equation set. They are identified by a number that counts all the timing sets of a given equation set. They define edge delays and a period (tester cycle) by assigning expressions, which can contain base variables and derived variables, to keywords identifying edges.」

**timing set 里的值是表达式**，可以用 base 变量、也可以用 derived 变量。**编号是「这份 equation set 里第几个 timing set」**。

两处细节，都是实际写文件时会绊到的：

- **`SPECS` 段里的单位只是给 GUI 看的**：

  > 「The units in brackets are displayed in the graphical user interface; this is their only purpose.」

  ——**`[ns]` / `[MHz]` 不参与计算、不做换算**，原文把这一点单独写成一句。
- **`EQUATIONS` 段内部有先后依赖，只能引用前面已经定义过的**：
  原文的说法是 derived 变量可以由「constants、base variables、以及**前一条语句里定义过的** derived variables」组成，
  并在例子后补了一句

  > 「Note that the second and third definition use the variable `p` that was defined in the first statement.」

  **即：段内顺序不能随便调。**

#### ② wavetable：名字规则是硬规定

> 「Wavetables define waveforms and device cycles. They are identified by a name. The name can consist of up to 40 characters. If it contains spaces, it must be enclosed by double quotes. It must not contain a semicolon.」

| 条件 | 结果 |
|---|---|
| 名字长度 | **最多 40 个字符** |
| 名字里有空格 | **必须用双引号包起来** |
| 名字里有分号 | **不允许**（`It must not contain`） |
| 编号方式 | **不是编号，是名字**（equation set 与 spec set 都是数字，只有它是名字） |

#### ③ spec set 与 timing specification：**三块数据的绑定**

> 「Specification sets (briefly spec sets) assign fixed values to the base variables that are defined in the equation set. They are identified by a number that counts the specification sets for a given equation set, starting from 1; up to 99 spec sets can be defined for one equation set.」

> 「Spec sets are defined within a so-called timing specification, which in addition contains pointers to an equation set and a wavetable, thus defining a complete timing.」

**两句话交代了两层**：spec set 自己只是「一组值」；**它必须活在一条 timing specification 里**，
而那条 specification 同时握着**两枚指针**（指 equation set、指 wavetable）。**三样凑齐才是一条完整的 timing。**

接着是最容易读漏的一段——**为什么 spec set 的编号必须算得这么小心**：

> 「Note that specification sets only exist within a specification. If two different specifications point to the same equation set, their specification sets must have a different specification set number. Due to this, every pair of equation set and specification set numbers uniquely identifies the wavetable of the specification, so that timing specifications can be identified by their equation set number and specification set number.」

拆成「条件 → 结果」：

| 条件 | 结果 |
|---|---|
| **两条 specification 指向同一个 equation set** | **它们的 spec set 编号必须不同** |
| 满足上一条之后 | **「equation set 编号 + spec set 编号」这一对唯一确定那条 specification 用的 wavetable** |
| 于是 | **两条编号就能当 ID 用**——固件命令里就是这么引用一条 timing specification 的 |

那个 ID 的算法原文给了公式：

> 「In the firmware commands, you refer to a timing specification through its specset ID, a number that is generated as follows:」

```
(equation_set_nr * 100) + specification_set_nr
```

**换算成实际数字**：equation set 1 的 99 个 spec set → `101` 到 `199`；
equation set 2 的第一个 → `201`。**乘 100 那两个 0 就是留给 spec set 的两位数**，
这也解释了原文那句 `up to 99 spec sets`——**是 99（两位）撑满，不是随便定的数。**
（这条换算是本页按公式算的，**原文只给了公式**——属（推断），依据即公式本身与 `starting from 1` / `up to 99` 两句。）

### 文件长什么样：`02.08.04.34.04.04` 给了一份完整的例子

本页的第二篇 sources 几乎全是**一个代码块**——一份真实的 equation based timing setup file。
它的骨架是**三条 `EQSP` 命令**，每条后面跟着它搬运的那一块正文：

| 段 | 起头的行 | 装的内容 |
|---|---|---|
| wavetable | `EQSP TIM,WVT,#9000001922` | 两个 `WAVETBL`（`gross_func_wtb` / `spec_search_wtb`）与它们的 `PINS` 块 |
| equation set | `EQSP TIM,EQN,#9000001444` | 两个 `EQNSET`：`1 "gross_func_eqn"` 只有 `SPECS` + `TIMINGSET`（**没有 `EQUATIONS`**），`2 "spec_search_eqn"` 三块齐全（`SPECS` / `EQUATIONS` / `TIMINGSET`）——**例子本身就演示了前两块可选** |
| spec set | `EQSP TIM,SPS,#9000001339` | **两段**，每段四行：「`EQNSET n` + `WAVETBL "<名字>"` + `CHECK all` + `SPECSET n "<名字>"`」（两个 equation set 各一段） |

**第三块就是 timing specification 的实形**：一行 `EQNSET` + 一行 `WAVETBL` + 一段 `SPECSET`
——正好对上前面那句 `contains pointers to an equation set and a wavetable`。
**`EQNSET` 这个词在这份文件里出现两次、是两个角色**：在 `TIM,EQN` 段里它是**段头**，
在 `TIM,SPS` 段里它是**指针**。（这一条与 [[mapping-timing]] 里那句
「同一个词在两个文件里是两个东西」是同一件事，**本页照它并列、不替谁统一**。）

**例子文件里能看到、而正文没写的一件事**：spec set 的正文表不只装「固定值」，
它有 `ACTUAL` / `MINIMUM` / `MAXIMUM` **三列**（原文对 spec set 的定义只说了
`assign fixed values`）。**例子文件里每个变量后面带的是值域，不是单值**——
`ts_Sx_CP` 那一行填的是 `7 3 10`（actual / min / max）。**这是文档事实（例子就在语料里），但「为什么一个叫『值集』的东西要带 min/max」本页不展开**，那属于 [[spec-value]] 那一线。

## 典型用法

**本页两篇 sources 都没有 `## Procedure`，也没有 `## Before you begin`。**
下面这张顺序表**不是文档给的流程**，是**把「三块数据各自的规定」与例子文件里三条 `EQSP` 的先后拼出来的**
——**（推断），依据逐行写在最后一列**。

| # | 做什么 | 依据 |
|---|---|---|
| 1 | 在 equation set 里声明 base 变量（`SPECS`，**可选**，写不写单位都行——单位只给 GUI 看） | `This (optional) part of the equation set is identified by the keyword SPECS.` |
| 2 | 写派生量（`EQUATIONS`，**可选**）——**只能引用前面已经定义过的变量** | `defined in a previous statement` + `Note that the second and third definition use the variable p` |
| 3 | 写至少一个 timing set（**唯一必填**），把边沿 keyword 赋成含变量的表达式 | `Timing sets are the only mandatory part of an equation set.` |
| 4 | 写 wavetable：**名字 ≤ 40 字符**，有空格要加引号，不能有分号 | `Wavetables define waveforms and device cycles.` |
| 5 | 在一个 spec set 里给 base 变量填值（**一份 equation set 最多 99 个**，编号从 1 起） | `starting from 1; up to 99 spec sets` |
| 6 | 用「`EQNSET` + `WAVETBL` + `SPECSET`」把三样绑成一条 **timing specification** | `contains pointers to an equation set and a wavetable` + 例子文件的 `TIM,SPS` 段 |
| 7 | 用 [[eqfs]] / [[eqsp]] 把三块**下载**进去 | `The data collections are downloaded with the EQFS and EQSP commands.` |

**三条实际用的提醒：**

- **同一份 equation set 被两条 specification 指向时，spec set 编号必须错开**——
  这不是风格问题，是 ID 公式能唯一的前提（见上面那张「条件 → 结果」表）。
- **要改值，改 spec set；要改关系，改 `EQUATIONS` 的表达式**——这是「方程」这套东西的用法分野。
- **运行期改定义是允许的**（`also change definitions at runtime`），
  **但那不落盘**：原文只说了能改，**没说改完怎么保存**，**这一条本页不展开**（见「出处」）。

## 和谁有关

- [[timing]] — **stage 页**（timing 这一段的总页）。本页是 timing 定义侧的**文件组织**那一面。
- [[mapping-timing]] — **同阶段的对照表页，而且与本页共用同一份底稿。**
  它引的核心那一句（`The collections themselves cannot be edited with firmware commands.`）
  出自 `02.06.06.01.02_Data_organization_of_equation_based_timing`，
  **而那一篇与本页第一篇 sources 是同一个 TDC 页 `10597.htm` 的两份投放**
  （详见「出处」的重复投放那一节）——**两页引的不是两处独立证据，是同一篇**。
  **三层（GUI / 文件 / L1）怎么对，一律记在那一页**；本页只负责「文件里这三块是什么」。
- [[timing-equation-set ]] — equation set 的**逐项参考**（`SPECS` / `EQUATIONS` /
  `TIMINGSET` 每个关键字怎么写）。**本页只给「有哪几块、哪块必填」，逐项语法不在本页。**
- [[timing-specification]]/ [[timing-spec ]] — timing specification 是什么、
  L2 侧怎么用它。**本页给的是它的组成（两枚指针 + 一个 spec set）与那个 ID 公式。**
- [[spec-set]] / [[spec-variable]]/ [[spec-value ]] — spec set / base 变量 /
  spec 值三个概念各自。**本页只说 spec set「给 base 变量赋值」以及三者的编号关系。**
- [[wavetable]] / [[wavetable-file ]] — wavetable 是什么、文件格式怎么排。
  **本页只说它「定义波形与 device cycle」，以及名字的三条硬规定。**
- [[eqsp]] / [[eqfs]] — **下载这三块数据的命令**，原文点名。
  **这两条命令自己的页本页没读**——参数、返回值、错误行为本页一个字没有。
- [[timing-master-file ]] — 把一份 timing setup 拆成多个文件的东西。
  **本页两篇 sources 都没提它。**
- [[timing-setup-tool]]/ [[spec-tool]] — GUI 侧那两个入口。
  **本页两篇 sources 里一个字都没提这两个工具**——所以「哪块数据在哪个窗口里编辑」
  **本页答不了**（[[mapping-timing]] 那一头有）。

## 版本

**两篇 sources 都有 `## Functional changes` 段，而且各只有一条，内容相同：**

- 定义文档（`34.04.03.01`）：`Introduced before SmarTest 6.3.2`
- 例子文件（`34.04.04`）：`Introduced before SmarTest 6.3.2`

**这一条是哨兵值，不是「6.3.2 的变更」。** 按 `schema.md` §11.2②，
`Introduced before` 这一整类说法的意思是「**在本文档集覆盖范围开始之前就已经有了**」——
**照字面读会读成「6.3.2 新增了 equation based timing」，那是错的。**
全语料有 2,677 条可用性行都写这个版本号、措辞全是 `before`，**这一页只是其中两条。**

**除此之外，这两篇没有任何版本条目。** 所以：

- **`flush_section` 那类「某版本新增了某个参数」的记录，这两篇一条都没有**；
- **「spec set 上限 99」是哪个版本起的、「`CHECK all` 是什么时候有的」，本页答不了**——
  **这两篇没写**。

**（一处值得记的对照）**：`02.08.04.34.04.03.01` 的第三次投放这件事本身**不是版本差异**
——三份投放的正文逐字相同（见「出处」），**它们之间没有先后关系，只是同一页挂了三个章号。**

## 出处

`sources:` **两篇，都整篇读过**：

| 篇 | 字节 / 行 | TDC `source_topic` | 它在文件里是什么 |
|---|---|---|---|
| `02.08.04.34.04.03.01_Data_organization_of_equation_based_timing.md` | 6,500 / 119 | `10597_3.htm` | 定义文档（三块数据的规定 + 那个 ID 公式 + 图） |
| `02.08.04.34.04.04_Example_of_the_equation_based_timing_setup_file.md` | 5,854 / 219 | `16956.htm` | 例子文件（**几乎全是一个代码块**） |

**两篇都只有 `## Functional changes` 一条实质内容之外的散文极少**：
定义文档有 `## Equation sets` / `## Wavetables` / `## Specification sets and timing specifications` /
`## Example` / `## Functional changes`；**例子文件除了代码块就只有 `## Functional changes`**。

### ⚠️ 重复投放：本页第一篇是同一个 TDC 页的**第三次**投放

**判据用 `schema.md` §10 的那一条**（`frontmatter` 的 `source_topic` 去掉 `_N` 后相同）。
按 `10597` 前缀查全语料，同一个 TDC 页 `10597.htm` 有**三份**投放：

| 投放 | 路径 | `source_topic` |
|---|---|---|
| 第 1 份 | `02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.md` | `10597.htm` |
| 第 2 份 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.02_Data_organization_of_equation_based_timing.md` | `10597_2.htm` |
| **第 3 份（本页 sources 用的这一份）** | `02_System_reference/02.08_Setup_and_Result_Tools/` 下的 `34.04.03.01_Data_organization_of_equation_based_timing.md` | **`10597_3.htm`** |

**实测（`diff`，跳过 frontmatter）**：三份的正文**逐字相同**，
差别只有两处——① 每份里那些**内部相对链接的前缀**（`02.06.06.01.04` 对 `../02.06_Command_Reference/02.06.06.01.04`）；
② **`Subtopics` 那一行挂的后继不同**：本页这一份挂 `Multiport timing specifications`，
第 1 份挂 `Timing equation set reference`。**同一页在三个章里挂的后继不是同一个**，照实记。

**两件必须说清的事：**

- **本页引的每一句英文，三份投放里都一样**——所以引文的逐字性不受影响。
- **`wiki/mappings/mapping-timing.md` 引的是第 1 份（`02.06.06.01.02`），本页引的是第 3 份。**
  按 §10 第 0 条，**这不构成「两处独立证据」**——两页引的是同一个 TDC 页。**本页把它标明。**
- 第二篇 sources（例子文件，`16956.htm`）**没有重复投放**：全语料只此一份。

### 本页「语法 / 参数」节的来源

那一节只有 149 字符，**全部来自定义文档自己的 `## Example` 段**（不是子主题）：
一句 `The following figure exemplifies the structure of equation based timing by a schematic setup:`
加一张图 `10596.png`（alt 是 `Timing Specifications`）。
**本页是少数「语法节来自定义文档本人」的页之一**——因为这一篇刚好有 `## Example` 这个段标记。

### 本页读的图（1 张，sources 里的图一共只有这 1 张）

- `10596.png`（定义文档 `## Example` 段那张，alt `Timing Specifications`）——**整张看完**，逐字见「图证」一节。
- **例子文件一张图都没有**（实测该篇对 `raw/` 的引用 0 处）。
- 图上读到的字**逐条回 9,398 篇 raw md 里查过 grep 命中**——本页凡写「grep 不到」的都是实测 0 命中。

### 图证：`10596.png`（④ 图证）

**它不是截图，是一张结构示意图**，画的是三块数据怎么互相指。逐字可读的是：

- 左上一个大框，标题 `Equation set 1`，框内四格：`Spec variables`、`Equations`、`Timing Set 1`、`Timing Set 2`；
- 左下一个框，**标题也写作 `Equation set 1`**，框内只有 `Spec variables` 与 `Equations`（**没有 timing set**）；
- 中间三框：`Specification 101` / `Specification 102` / `Specification 103`，
  各含一个内框 `Specset 1` / `Specset 2` / `Specset 3`；
- 右侧两框：`Wavetable A` / `Wavetable B`；
- 下半一框 `Specification 201`，内含 `Specset 1`，一侧连 `Wavetable B`，另一侧连左边那个 equation set。

**它答掉的三件事（都由这一张背书）：**

1. **把那个 ID 公式算了一遍。** equation set 1 的三个 spec set 在图上长成 `Specification 101` / `102` / `103`，
   equation set 2 的那个长成 `Specification 201` ——`(1*100)+1/2/3` 与 `(2*100)+1`。
   **「编号怎么长的」这一点，原文只有公式，图给了实形。**
2. **一份 equation set 可以挂多条 specification。** 三个 `Specification 10N` 框并列，
   各自向同一个 equation set 连线。
3. **specification 的两头各连一边**：一侧汇到 wavetable，一侧连 equation set
   ——即原文那句 `contains pointers to an equation set and a wavetable` 的图形版。

**grep 不到的字**（逐条实测 0 命中）：`Specification 101`、`Specification 201`、`Specset 1`、
`Wavetable A`、`Wavetable B`。
（`Spec variables` / `Timing Set 1` / `Equation set 1` 三个串**能搜到，但搜到的是别处的正文**，
**不是这张图**——所以本页不拿子串命中冒充命中。）

**它答不了的，照实说：**

- **图里一个关键字名都没有。** 没有 `EQNSET`、没有 `WAVETBL`、没有 `SPECSET`、没有 `EQSP`——
  所以「图上的框 = 文件里哪一行」**这张图不管**，那一头靠的是例子文件。
- **图里没有文件名、没有扩展名。** 这份文件叫什么、扩展名是什么（`.tim`？）**图不答，原文也没写。**
- **图用的是自己的一套词**：`Spec variables` 对文件里的 `SPECS`、`Equations` 对 `EQUATIONS`
  ——**两套词，本页并列不判。**
- **图答不了「哪个框对应哪条固件命令」**：图上一个命令名都没有。

**一处照实记的图内矛盾（本页不替它改）**：下半那个 equation set 框的标题**逐字是 `Equation set 1`**，
**与上面那个框同名**；而它右边写着 `Specification 201`（按公式 `201` 只能是第 2 个 equation set）。
**图上写的确实是 `1`。**（推断：该处应是 `Equation set 2`；依据是 ID 公式与 `201` 这个编号。
**本页只记这一处不一致，不动图、也不改字。**）

### 本页没做的

- **子主题一篇没读**：`02.08.04.34.04.03.01.01_Multiport_timing_specifications`
  （定义文档 `Subtopics` 唯一那一篇）——**multiport 的 equation based timing 本页一个字没有。**
- **例子文件的三个子主题一篇没读**：`02.08.04.34.04.04.01_Timing_Wavetables_-_Example`、
  `.02_Timing_Equations_-_Example`、`.03_Timing_Specifications_-_Example`
  ——**例子文件里那三段正文的逐行解释在它们那里，本页只有原文本身。**
- **定义文档正文里链的六篇命令文档一篇没读**：`Setting delays and periods`、
  `Defining waveform shapes`、`Defining the timing specification`、
  `Defining the global period`、`Setting the edge delays`、`Timing equation set reference`。
  **所以本页没有「某个关键字怎么写」的语法细节。**
- **`EQSP` / `EQFS` 两条命令自己的页没读**（它们的名字与链接只出现在本页「语法 / 参数」节与例子里）。
- **`02.06.06.01.02`（同一 TDC 页的第 1 份投放）没有通读**——**只做了逐行 `diff`**
  （见上面「重复投放」那一节）。**它正文里的三段引文，本页是从本页那一份读的。**
- **没有实跑。** 没有在机台上加载过任何 timing setup file、没有下载过 `EQSP`、
  没有改过任何 spec 值。**`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[timing]] 那页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 例子文件里有一行把命令和内容粘在了一起（第 92 行）。** 原文逐字是：

> 「EQSP TIM,EQN,#9000001444EQNSET 1 "gross_func_eqn"」

**`#9000001444` 后面直接跟着 `EQNSET`，中间既没有空格也没有换行**；
同一个文件里另外两条 `EQSP`（`TIM,WVT` 与 `TIM,SPS`）**都是另起一行**的。
**本页没替它断行。**

**② 同一份表格里星号左右不对称（第 189 行与第 200 行，两处）。** 原文逐字是：

> 「# SPECNAME       *****ACTUAL***** *****MINIMUM**** *****MAXIMUM**** UNITS COMMENT」

（**那一串星号是原文自己的，不是本页的加粗标记**——原文这里是文件里的一行注释，
星号是排版出来的分隔符。本页原样转录，没有替它去掉，也没有替它补对称。）
**`ACTUAL` 两边各 5 个星号，`MINIMUM` 与 `MAXIMUM` 右边只有 4 个。**
**两处一模一样，本页照录**（[[mapping-timing]] 也引了这三个串，**两页引的是同一份文件里同一行**）。

**③ 单位写法在同一份文件里不统一。** `SPECS` 段写的是 `[ns]` / `[MHz]`（无空格），
而 `SPECSET` 表的 `UNITS` 列写的是 `[ ns]`（有空格，逐字如 `ts_Sx_CP         7                3                10               [ ns]`）。
**两种写法并存，本页照录不判。**

**④ 一处缩进不一致（第 75 行）。** 同一个 `WAVETBL` 里
其余 `PINS` 块都缩进两格（`  PINS CP`、`  PINS _MR`），而 `PINS ser_in` 顶格写。
**原文如此。**

**⑤ 两篇都没有编码坏字（§11.2① 那一族）。** 用 `[一-鿿]` 对两篇实测零命中
——对照 §11.2① 的全语料 1,053 / 9,398 篇含坏字，**这两篇属于没有的那一批**。
**这不是「没找到」，是查过、结果为零。**

**⑥ 两篇都没有 §11.2⑤ 那个整词替换（`DC/DC power units`）。** 实测两篇各 0 命中。
（§11.2⑤ 说规模是 128 篇，**本页这两篇不在其中**。）

`verified: doc-only`
