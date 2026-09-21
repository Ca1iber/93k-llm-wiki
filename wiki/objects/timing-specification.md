---
type: object
title: Defining the timing specification
layer: file
stage: timing
tags: [timing, timing-specification, timing-equation-set, wavetable, spec-set, spec-tool, equation-based, timing-file]
related: [timing, timing-spec, timing-equation-set, wavetable, wavetable-file, spec-set, spec-value, spec-variable, spec-tool, eqfs, eqsp, svlr, timing-file, timing-master-file, timing-setup-tool, primary-status, mapping-timing, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Defining the timing specification

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **767 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The following is a simple example of a `single-port timing specification`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.34.04.01_Single-port_timing_setup.md`）:

```
EQNSET 1 "default"

WAVETBL "table1"
CHECK all

SPECSET 1 "sp1"

# SPECNAME *****ACTUAL***** *****MINIMUM**** *****MAXIMUM**** UNITS COMMENT
f          100                                                [MHz]
```

This specification uses spec set 1 for equation set 1. It will be identified to the firmware commands by 101. The base variable f is set to 100. The `CHECK all statement`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.34.04.03.05.01_CHECK_Statement_Options.md`） activates all consistency checks (see `Consistency checks for edge delays`（raw: `02.06.06.01.05.01_Consistency_checks_for_edge_delays.md`）).

<!-- 语法节 end -->

## 是什么

**timing specification 是「把波形形状、周期长度与边沿延迟、spec 取值这三样合成到一起」的那份东西——
它的产物是「一个 test 的完整 timing」。** 原文第一段就是全部机制，逐字如下：

> 「In equation based timing, waveform shapes, as defined in a wavetable, are combined with a
> period length and edge delays, as defined in an equation set, in a timing specification which
> provides a complete timing for a test. This specification also contains a spec set where values
> are assigned to the base variables of the equation set, and specifies which checks are to be
> performed on the edge delays.」

### 四样东西，各出自哪里

**这一段里出现了四个角色，读的时候最容易混。** 拆开：

| 角色 | 出自哪 | 原文里的话 |
|---|---|---|
| **波形形状**（waveform shapes） | **wavetable** | `waveform shapes, as defined in a wavetable` |
| **周期长度 + 边沿延迟**（period length and edge delays） | **equation set** | `a period length and edge delays, as defined in an equation set` |
| **base variable 的取值** | **spec set**（本 specification **自己包含**的） | `This specification also contains a spec set where values are assigned to the base variables of the equation set` |
| **对边沿延迟做哪些检查** | **本 specification 指定** | `and specifies which checks are to be performed on the edge delays` |

**两条要点**：

1. **wavetable 与 equation set 是「原材料」，timing specification 是「合成产物」**——
   原文用的是 `are combined with … in a timing specification`：
   **合并发生在 timing specification 里**（**推断**：`in a timing specification` 这个介词短语
   指向的是合并的场所/产物；**依据**是紧接着的定语从句 `which provides a complete timing for a test`——
   能「提供一个 test 的完整 timing」的是那个合成物，不是原料）。
2. **它不是只有 wavetable + equation set 两样**：**spec set 与「检查什么」也是它的组成部分**
   （`This specification also contains … and specifies …`）。
   **只记得「两样合成」会漏掉后两样。**

**一句限定必须照读**：整段的前提是 **`In equation based timing`**——
**本篇讲的是 equation based 那一侧的 timing**。**非 equation based 那一侧的对应物是什么样，
本篇一个字没写**（**本页也不替它推**）。

### 它落在哪、叫什么名字

> 「The timing specification file can be found here: `<device_folder>/timing`. The file can have any
> name that is suitable, for example, timingSpec1.」

| 事实 | 原文 |
|---|---|
| **目录** | `here: <device_folder>/timing`——**device 目录下的 `timing` 下** |
| **文件名** | **任意**（`can have any name that is suitable`），例子是 `timingSpec1` |

**「文件名任意」这一条是有后果的**：**同一个 device 下可以有多份 timing specification 文件**，
**所以「按名字找某一份 specification」这件事本篇没有给规则**（**这是本页读出来的（推断）**，
依据是 `can have any name that is suitable` 这句本身；**原文没有讨论多份的情形**）。

### 三条定义途径，**其中两条有硬要求**

> 「Usually, the specification is defined with the spec tool. However, if you want to download a
> specification with the EQFS or the EQSP command, you must specify it as it is coded in the
> timing setup file.」

| 途径 | 原文 | 读法 |
|---|---|---|
| **通常** | `Usually, the specification is defined with the spec tool.` | **[[spec-tool]]**（GUI）是常规入口 |
| **下载给固件** | `if you want to download a specification with the EQFS or the EQSP command, you must specify it as it is coded in the timing setup file.` | **用 [[eqfs]] / [[eqsp]] 下载时，必须按 timing setup file 里的写法写**——**`must`，不是建议** |
| **（第三处）** | 见 `## Example`：`EQNSET 1 "default"` / `WAVETBL "table1"` / `CHECK all` / `SPECSET 1 "sp1"` 那一小段 | **那一段就是「按 timing setup file 的写法」长什么样**（**推断**：它是 `## Example` 里给的 `single-port timing specification` 例子；**依据**是原文管它叫 example 并紧接着解释了 spec set 1 / equation set 1） |

**这三条的关系是本页最容易做错的一处**：**GUI 里定义是一回事，落成 timing setup file 里那几行是另一回事，
而只有后者能下载**。（**注意**：`EQFS` / `EQSP` / `spec tool` / `timing setup file` 这几样**本页都没读它们的 raw**，
见「出处」。）

### 一个编号：`101` 是怎么来的（**推断**）

例子后面那句原文是：

> 「This specification uses spec set 1 for equation set 1. It will be identified to the firmware
> commands by 101.」

**「spec set 1 + equation set 1 → 101」这个对应，本篇没有给公式。**
（**推断**）编号是 **`100 * equation_set_no + specset_no`**——
**依据**：① 例子里 `1` / `1` 两个编号得到 `101`，符合这个式子；
② 本 wiki 的 [[timing-spec]] 那一页在构造对象时用的就是 `TIMING_SPEC spec1(1, 2);`
（**equation set 号 + spec set 号**两个数），而 [[timing-setup-commands]] 的语法节里
`specset_id` 一栏逐字写着 `100 * equation_set_no + specset_no`。
**两条都是别的页，不是本篇**——**本篇只给了 `101` 这一个数，没给算法**。

### 与本 wiki 的 `timing-spec` 页分层：**一个是产物，一个是句柄**

**这两页名字只差几个字母，必须分清**：

| | `timing-specification`（**本页**） | [[timing-spec]] |
|---|---|---|
| 是什么 | **equation based timing 的产物**——wavetable + equation set + spec set 合成出来的那份配置 | **L2 的 `TIMING_SPEC` 类**：访问「已有 equation set 里的 spec set 内容」的**句柄** |
| 层次 | 骨架给的是 **`layer: file`**（**落盘在 `<device_folder>/timing`**） | `layer: L2` |
| 本篇有没有提它 | **本篇 raw 里 `TIMING_SPEC` 一次都没出现** | 那一页自己的 raw 是 `02.07.04.01.249`（**本页没读**） |
| 两页的关系 | **本页是「那份东西本身」，`timing-spec` 是「读/改它的一个 API 句柄」**——**这句是本页的读法（推断）**，依据是 [[timing-spec]] 那一页逐字写的 `accesses the data container holding the contents of an existing timing equation and spec set`（**本页读过的 wiki 页**） | 同左 |

**一句话：本页讲「规范本身怎么写出来、放哪儿」，`timing-spec` 讲「测试方法里怎么读改它」。**

### `## Related firmware commands` 那一节：改的是**运行期值**

原文这一节只有一句（加一个分号），逐字如下：

> 「You can query the current values of base and derived (spec and equation) variables with the
> SVLR? query. You can also change the runtime values (not the definitions in the spec set) of base
> variables for a specified timing specification with the SVLR command; in this case the whole
> timing equation system will be recalculated.」

**三件事，一件比一件重要**：

1. **查询**用 `SVLR?`，**改**用 `SVLR`（**[[svlr]]**，两条都是固件命令）。
2. **改的是「运行期值」，不是 spec set 里的定义**——原文用括号明写：
   `(not the definitions in the spec set)`。**所以 `SVLR` 不是「改配置」，是「改这一次运行用的值」。**
3. **改一个 base variable 的后果是「整个 timing equation system 重算」**——
   `the whole timing equation system will be recalculated`。**这是本篇给出的唯一一条运行期后果。**

## 典型用法

**先说清楚：本篇没有 `## Procedure`、没有 `## Before you begin`。** 它能给的用法，
全在 `## Example` 那一小段（**在「语法 / 参数」节里，本页不重复抄**）与 `## Related firmware commands` 那一句里。

### 例子逐行走一遍（**这是本页唯一能照着看的东西**）

| 行（逐字） | 它在干什么 | 依据 |
|---|---|---|
| `EQNSET 1 "default"` | **选定 equation set 1**，名字 `default` | 原文后面对这个例子的解释：`This specification uses spec set 1 for equation set 1.` |
| `WAVETBL "table1"` | **选定 wavetable `table1`** | 同上（原文只说了 `spec set 1 for equation set 1`，**wavetable 那一行没有单独解释**） |
| `CHECK all` | **打开全部一致性检查** | 原文：`The CHECK all statement activates all consistency checks` |
| `SPECSET 1 "sp1"` | **选定 spec set 1**，名字 `sp1` | 例子的解释句 |
| `f          100                                                [MHz]` | **给 base variable `f` 赋值 100**，单位 `[MHz]` | 原文：`The base variable f is set to 100.` |

**注意两处**：

- **`f` 这个变量被原文叫作 `base variable`，而它出现在 `SPECSET` 段里**——
  **赋值发生在 spec set，被赋值的变量属于 equation set**（原文第一段那句
  `a spec set where values are assigned to the base variables of the equation set` 说的正是这件事）。
- **`CHECK all` 与本页第一段那句 `specifies which checks are to be performed on the edge delays`
  对得上**——**「检查什么」就是由 `CHECK` 这一行指定的**（**推断**：依据是原文把 `CHECK all`
  解释成「激活所有一致性检查」，而第一段说 specification 「指定对边沿延迟做哪些检查」）。

### 三条使用路径（照本页「是什么」那节选）

| 你想干什么 | 走哪条 | 硬要求 |
|---|---|---|
| **平常建/改一份 specification** | **[[spec-tool]]** | 原文 `Usually, the specification is defined with the spec tool.` |
| **把它下载给固件** | **[[eqfs]]** 或 **[[eqsp]]** | **必须按 timing setup file 里的写法写**（`you must specify it as it is coded in the timing setup file`） |
| **在运行期改某个 base variable 的值** | **[[svlr]]**（查用 `SVLR?`） | **改的是运行期值，不改 spec set 定义**；**后果是整个 timing equation system 重算** |

### 顺序（**本篇只给了一条**）

**本篇唯一的顺序性陈述是这条**：**先有一份「按 timing setup file 写法写出来」的 specification，
才能用 `EQFS` / `EQSP` 下载它**（原文 `must specify it as it is coded in the timing setup file`）。
**除此之外本篇没有任何「先做什么再做什么」的话**——**「加载顺序」「激活顺序」本页一个字都没有**
（那些在 `APRM` / `SPRM` / `SVLR` 自己的篇里，**本页没读**）。

### 一条本页答不了、但用的人一定会问的

**「这份 specification 什么时候生效、怎么变成 primary」——本篇没写。**
它只说了 `SVLR` 改运行期值会让 equation system 重算，**没有说一份新 specification 怎么被启用**。
（本 wiki 里那件事在 [[primary-status]] / [[aprm]] / [[sprm]] 那一族，**本页都没读**。）

## 和谁有关

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[wavetable]] | **原材料一：波形形状**。原文 `waveform shapes, as defined in a wavetable`——**本页的一半定义就是它** | 本篇第一段（**文档事实**） |
| [[timing-equation-set]] | **原材料二：周期长度 + 边沿延迟**。原文 `a period length and edge delays, as defined in an equation set` | 本篇第一段（**文档事实**） |
| [[spec-set]] | **它的组成部分（不是外部依赖）**。原文 `This specification also contains a spec set where values are assigned to the base variables of the equation set`——**spec set 在 specification 内部** | 本篇第一段（**文档事实**） |
| [[spec-value]] / [[spec-variable]] | **被赋值的那个量**。例子里 `f 100 [MHz]` 就是给一个 spec 变量赋值；**这两个词本篇用的是 `base variable`**，不是 `spec value` | 本篇第一段 + `## Example`（**文档事实**） |
| [[spec-tool]] | **GUI 侧的常规定义入口**。原文 `Usually, the specification is defined with the spec tool.` | 本篇（**文档事实**） |
| [[eqfs]] / [[eqsp]] | **下载通道（下游）**。用它们下载时**必须按 timing setup file 的写法写** | 本篇（**文档事实**）；**这两篇 raw 本页没读** |
| [[svlr]] | **运行期改值通道**。查询用 `SVLR?`、改值用 `SVLR`；**改运行期值不改定义**，后果是整个 equation system 重算 | 本篇 `## Related firmware commands`（**文档事实**）；**那篇 raw 本页没读** |
| [[timing-file]] / [[timing-master-file]] | **落盘侧的同族**。本篇给的落点只有 `<device_folder>/timing` 与「文件名任意」——**timing file / master file 与它的关系本页没读，不声称** | 本页没读那两篇（**取材边界**） |
| [[timing-spec]] | **分层对照（最要紧的一对）**。本页是**产物**，那页是**读改它的 L2 句柄**（`TIMING_SPEC`） | [[timing-spec]]（**本页读过的 wiki 页**）；**本篇 raw 里没有 `TIMING_SPEC`** |
| [[timing-setup-commands]] | **L1 命令侧的入口**。`specset_id` 的算法（`100 * equation_set_no + specset_no`）与 `EQFS` / `EQSP` / `SVLR` / `CHECK` 的定义都在那一页的语法节里 | [[timing-setup-commands]]（**本页读过的 wiki 页**）——**本页的 `101` 只有一个数，算法是从那里核的** |
| [[timing-setup-tool]] | **GUI 侧的 timing 工具**（`spec tool` 与它是不是同一个，**本篇没写**）。**本页不把它和 `spec tool` 当成同一个** | 本页没读那篇（**取材边界**） |
| [[mapping-timing]] | **跨层对照表**（已建）。本页与 `timing-spec` 的分工在那张表里也是两行 | 本页没读那篇（**取材边界**） |
| [[timing]] | **stage 页**。本页 `stage: timing` 填的是「最近的一段」不是「归属」（§6） | frontmatter 约定 |
| [[smartest-6.3.2]] | **版本页**：本篇 `## Functional changes` 的唯一一条 | 本篇版本段（**文档事实**） |
| **`Consistency checks for edge delays`** / **`Changing the runtime values of base variables`** / **`Multiport timing specifications`**（**均未建，语料自己声明的子主题**） | **本篇的三个正式下钻**：检查规则、base variable 的运行期改值、多端口 specification。**三篇本页都没读**——**所以「检查具体查什么」「多端口长什么样」本页一个字没有** | 本篇 `#### Subtopics`（**文档事实：篇名与链接**）。**这三个篇名不在 `prose-allowlist.txt` 里**，故用反引号写，**没有做成链接**（§9.1） |

## 版本

本文档**有** `## Functional changes` 段，段里**只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 timing specification」。**
> 措辞是 `before`，意思是「在本套文档集覆盖范围开始之前就已经有了」。
> **所以只能说：7.10.3 上有，且它比 6.3.2 更老** → [[smartest-6.3.2]]。

**版本段里没有的东西**（照实记，不替它补）：**没有第二条**。
所以「`CHECK` 的取值是哪一版加的」「`SVLR` 改运行期值这条行为哪一版变过」
**在本篇里查不到**——要去 [[smartest-6.3.2]] 之后的各版本页，或去那几条命令自己的文档。

## 出处

`sources:` **一篇**：

- `02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.md`
  （frontmatter 的 `source_topic` 是 `56982.htm`，**3,247 字节 / 48 行，整篇读完**——按 §11.5 口径：
  字节是 `st_size`，行数是 `wc -l`）
- **重复投放检查做过**（§10 第 0 步）：全语料里 `source_topic: "56982...` **只有这一份**
  （实测 1 个文件命中），**所以本篇没有 `_2` 那样的第二投放**——
  这一点和同批的 [[waveform-set]] 那篇不同（那一篇的出处是 `17791_2.htm`）。
- 本页的「语法 / 参数」节是脚本从这一篇的 `## Example` 段逐字抽的（**本页一个字没动**）。
  **注意一件事**：这一节**只抽到 `## Example`**——本篇还有 `## Related firmware commands` /
  `## Related information` / `## Functional changes` 三段，**它们不在语法节里**。
  **`## Related firmware commands` 那一句本页在正文里逐字引了**（它是本篇唯一讲运行期行为的地方），
  **语法节一个字没动。**

**本页没做的**：

- **三个 `Subtopics` 一篇没读**：`Consistency checks for edge delays`、
  `Changing the runtime values of base variables`、`Multiport timing specifications`。
  **所以「一致性检查具体查哪几条」「多端口 specification 长什么样」本页一个字没有**——
  **而这两件事在本篇的标题与第一段里都被承诺了**（第一段说 specification 「指定对边沿延迟做哪些检查」）。
- **`## Related information` 那六条一篇没读**：`Timing Specifications - Reference`、
  `Timing Specifications - Example`、`EQFS`、`EQSP`、`SVLR`、`Consistency checks for edge delays`。
  **所以「一份完整的 specification 有哪些字段、spec set 的表格怎么写」本页没有**——
  **本页只有例子里那五行的形状。**
- **`EQFS` / `EQSP` / `SVLR` / `spec tool` / `CHECK` 各自的 raw 一篇没读**——
  本页只在**本篇**里见过它们的名字与那一两句话。
  其中 `specset_id` 的算法（`100 * equation_set_no + specset_no`）是回
  [[timing-setup-commands]]（**wiki 页**）**核的**，**不是从本篇读出来的**——
  正文里已把这一处标成推断并写明依据。
- **`Single-port timing setup`（`02.08.04.34.04.01`）没读**——例子里那个链接指向它
  （`a single-port timing specification`）。**所以「单端口与多端口的差别」本页没有。**
- **[[primary-status]] / [[aprm]] / [[sprm]] 那一族没读**——**「一份 specification 怎么被启用」
  本页答不了**（正文已明写）。
- **图**：**本篇对 `raw/` 的引用 0 处**——实测 `.png` / `.jpg` / `.gif` / `!\[` / `<img` / `raw/`
  六种写法在本篇里**全部 0 命中**。**所以本页没有任何来自图的结论，这张「没有图」是查过的事实，
  不是「够不着」。**
- **没有实跑。** 没在机台上建过 timing specification、没用 `EQFS`/`EQSP` 下载过、没跑过 `SVLR`
  去改运行期值。**「整个 equation system 重算」这句话本页只转录，没验过。**
  `verified: doc-only` 指的就是这件事。
- **本篇没有 `## Errors` / `## Warnings` 段**，所以本页**没有「报错条件」节**——
  这不是漏写（**本页的骨架里本来就没有那一节**），是语料没有。

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **`## Related information` 那六条链接挤在一行里、中间没有任何分隔。**
> 原文逐字：
>
> `[Timing Specifications - Reference](<../02.08_Setup_and_Result_Tools/02.08.04.34.04.03.05_Timing_Specifications_-_Reference.md>)[Timing Specifications - Example](<../02.08_Setup_and_Result_Tools/02.08.04.34.04.04.03_Timing_Specifications_-_Example.md>)[EQFS - (EQuation FileS command transfer)](<02.06.02.02.108_EQFS_-__EQuation_FileS_command_transfer.md>)[EQSP, EQSP? - (EQuation SPecification transfer)](<02.06.02.02.109_EQSP__EQSP__-__EQuation_SPecification_transfer.md>)[SVLR, SVLR? - (Spec VaLues at Runtime)](<02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>)[Consistency checks for edge delays](<02.06.06.01.05.01_Consistency_checks_for_edge_delays.md>)`
>
> **`](<` 紧接 `[`，六个条目之间没有逗号、没有换行、没有列表符。**
> **这不是孤例**：同批的 [[waveform-set]]（`02.08.04.34.03`）那一篇的 `## Related information`
> **是同一个形状**——**同一族文档的 HTML→md 压平都会这样**。**本页照原样引，没有替它断句。**

> ② **`base and derived (spec and equation) variables` 这个括号的对应关系不明。**
> 原文逐字：`You can query the current values of base and derived (spec and equation) variables with the SVLR? query.`
> **括号里是两类（spec / equation），括号外也是两类（base / derived）——
> 但「base 对 spec、derived 对 equation」还是反过来，本篇没有写。**
> **本篇别处只给了 `base variable` 一种说法**（`the base variables of the equation set`、
> `The base variable f is set to 100.`），**`derived variable` 在别处再没出现过**。
> **本页把两处并列摆着，不替它配对。**

> ③ **例子的 spec 表只剩表头与一行数据。** 语法节里那两行逐字是：
>
> `# SPECNAME *****ACTUAL***** *****MINIMUM**** *****MAXIMUM**** UNITS COMMENT`
>
> `f          100                                                [MHz]`
>
> **表头列了五个字段名（`SPECNAME` / `ACTUAL` / `MINIMUM` / `MAXIMUM` / `UNITS` / `COMMENT`，实际是六个），
> 而数据行只给了一个数 `100` 与单位 `[MHz]`**——**`MINIMUM` / `MAXIMUM` / `COMMENT` 三格对应的内容
> 在本篇里没有**。**这是原样压平的结果，本页没有替它补格、也没有替它对齐。**

> ④ **`SPECNAME` 那一行以 `#` 开头**（在代码块里是注释写法），
> **所以按 `^#` 扫标题会把这一行当成一级标题**——本页实测的标题清单里它确实混进来了
> （`# SPECNAME *****ACTUAL***** …`）。
> **这不是语料的错，是「`#` 在注释与标题里同形」造出来的观察陷阱**，记在这里免得下一个人误判。

`verified: doc-only`
