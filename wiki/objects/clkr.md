---
type: object
title: CLKR, CLKR? - (CLocK Resolution)
layer: L1
stage: timing
tags: [timing, period-resolution, multi-port, command, l1]
related: [timing, pclk, wsus, tsus, wavetable, timing-specification, timing-equation-set]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# CLKR, CLKR? - (CLocK Resolution)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,187 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CLKR

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res}
```

### CLKR?

```
CLKR?[type,] {waveform_set|specset_id|"multi-port_spec"}
```

returns:

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res|clock_res}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98504.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `Automatic calculation of period resolution for single-port setups`（raw: `02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md`）

### Example

```
> CLKR 1,,10
> CLKR? 1
< CLKR 1,1000,10

```

This example sets and queries the period resolution (10 ns) for waveform set 1. Ignore the returned value of the ref_period parameter.

```
> CLKR? "spec_port_1_port_2"
< CLKR "spec_port_1_port_2",50,5.555555556
```

This example queries the period resolution for the multi-port specification `spec_port_1_port_2`.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is less than 1.
- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- period_res is outside the allowed range.

<!-- 报错节 end -->

## 是什么

**`CLKR` 定义 period resolution（周期分辨率）。**

> 「The CLKR command defines the period resolution for a (single-port or multi-port) timing specification or a waveform set.」

**它对三类对象生效，语法式的三种写法就对应这三类**：

| 你给谁定义 | 怎么写 | 原文的约束 |
|---|---|---|
| 一个 waveform set | 写编号 | 「Enter an integer in the range 1 to the maximum number of allowed waveform sets.」——最大值由 [[wsus]] 定 |
| 一个 timing specification（equation-based） | 写 `specset_id` | 「100 * equation_set_no + specset_no」 |
| 一个 multi-port timing specification | 写它的名字（带引号） | 「To set or query the resolution of a multi-port timing specification, specify the name of the specification.」 |

### 两种分辨率：默认查 `period_res`，要 `clock_res` 得显式指定

`CLKR?` 可以查两种东西，由 `type` 选：

| `type` | 查什么 | 原文 |
|---|---|---|
| `VIRTUAL`（**默认**） | period resolution（`period_res`） | 「VIRTUAL: The period resolution (period_res) is queried. This is the default.」 |
| `EXACT` | clock resolution（`clock_res`） | 「EXACT: The clock resolution (clock_res) is queried.」 |

**默认是 `VIRTUAL`**，所以查 `clock_res` **必须显式写 `EXACT`**。
`type` 在语法式里的位置是**在 set 之前**（`CLKR?[type,] {…}`）。
**原文没有给 `EXACT` 的例子——语料未写。**

### `ref_period` 是保留位，**但查询会把它带回来**

参数节对它的全部说明就四个字：

> 「Not used. (Ignored)」

**而两个例子的返回值里它都有值**（`1000` 与 `50`）——
原文的处理方式是「忽略返回的那个值」（见 `## 典型用法`）。
**写的时候它是个空位、要用逗号占住；读的时候它是个要无视的字段。**
（它与 [[term]] 那种「空位必须占住」的位置参数是同一套写法。）

### `period_res` 的四条性质

> 「The period resolution (in ns) for the specified specification or waveform set.」

> 「If necessary, period_res is rounded to nine digits after the decimal point. The allowable maximum period resolution is the maximum tester period value. The minimum period resolution is determined by the hardware (see Automatic calculation of period resolution for single-port setups).」

| 性质 | 原文说的 | 本页能给数吗 |
|---|---|---|
| 单位 | ns | 能 |
| 舍入 | 必要时**取到小数点后 9 位** | 能（原文例子里返回 `5.555555556`，正好 9 位） |
| 上限 | = **最大 tester period 值** | **不能**——那个值是哪一篇/哪个参数给的，本篇没说 |
| 下限 | **由硬件决定**，原文指到 `Automatic calculation of period resolution for single-port setups` | **不能**——那一篇本页没读 |

**所以「我这台机的 period resolution 最小能到多少」本页答不了**——
**语料把答案放在专篇里，本页只负责指出在哪。**

### 最重要的一条：**定义过 `CLKR` 之后，自动重算就停了**

原文把这件事放在 `## Postdependencies` 一节：

> 「Note that if you define the period resolution with CLKR, the system will no longer recalculate it when you change the tester period of timing set 1 with the PCLK command globally, that is, for all pins.」

**机制**：**没**定义过时，改 timing set 1 的 tester period（用 `PCLK`，全局、对所有 pin）
会让系统**自动重算** period resolution；**一旦用 `CLKR` 显式定义了，这条自动重算就停掉**。
**后果**：之后改 tester period，period resolution **保持你写的那一个**。

**这是 `CLKR` 与 [[pclk]] 之间一条真实的耦合**，也是本页最该记住的一句：
**它不是「设一个值」那么简单，它同时关掉了一条自动机制。**
（原文没有写「怎么把它恢复成自动」——**语料未写**。）

### equation based timing 下：**只改运行时值，不改定义**

> 「Note also in connection with equation based timing that CLKR only changes the runtime value of the period resolution. A definition within an equation set (with the period_res keyword) will not be changed.」

**即：equation set 里 `period_res` 关键字写的那个定义仍然在**，
`CLKR` 改的只是**这一次运行用的值**。**于是两处会不一致**——
**这是原文明说的预期行为，不是矛盾**。相关页：[[timing-equation-set]]、[[timing-specification]]。

### 本章归属

`## Application` 一行：`Timing Setup, see `Timing Setup Commands`（raw: `02.06.06_Timing_Setup_Commands.md`）`，
对应 [[timing-setup-commands]]。

## 典型用法

**先说范围：这一篇没有 `## Procedure`，也没有 `## Before you begin`。**
唯一的过程线索是 `## Application` 那一行。**所以本页不写流程顺序**（那是 [[timing]] 的事）。

**1. 定义 + 查回来**（原文例 1，逐字）

```
> CLKR 1,,10
> CLKR? 1
< CLKR 1,1000,10
```

> 「This example sets and queries the period resolution (10 ns) for waveform set 1. Ignore the returned value of the ref_period parameter.」

**三个细节**：

- 设置时 `ref_period` 空着，**写成 `,,`**——保留位也要用逗号占住。
- 返回值 `CLKR 1,1000,10` 的第 2 个字段 `1000` **就是那个「Not used」的 `ref_period`**，
  文档专门写一句让你**忽略它**。
- **`CLKR? 1` 只给 set 编号，没给 `type`**——所以查的是默认的 `VIRTUAL`，即 `period_res`。

**2. 查多端口规格**（原文例 2，逐字）

```
> CLKR? "spec_port_1_port_2"
< CLKR "spec_port_1_port_2",50,5.555555556
```

> 「This example queries the period resolution for the multi-port specification spec_port_1_port_2.」

返回值 `5.555555556` 是 **9 位小数**，与参数节「rounded to nine digits after the decimal point」对得上。
**但这一例的说明没有提「忽略 `ref_period`」**（这一例里它是 `50`）——见 `## 出处` ⚠️①。

**3. 查 `clock_res`**：按语法式把 `type` 写在 set 之前、值为 `EXACT`。
**原文没有给这一种的例子——语料未写。**

**4. 顺序**：这一篇**没有写任何书写顺序要求**。
唯一带「之后」语义的是 `## Postdependencies` 那一句，而**那是「定义过之后自动重算不再发生」的状态后果**，
**不是「先写哪条命令」**——两件事不要混。

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[pclk]] | **耦合（本页最重要）**：定义过 `CLKR` 后，`PCLK` 全局改 tester period 不再触发 period resolution 的重算 | 本页文档 `## Postdependencies` |
| [[wsus]] | **上限来源**：`waveform_set` 的取值范围由 `WSUS` 定 | 本页文档参数节 + `## Errors` |
| [[timing-equation-set]] | **`CLKR` 改不动的东西**：equation set 里的 `period_res` 关键字定义 | 本页文档 `## Postdependencies` |
| [[timing-specification]] | **作用对象之一**：单口/多口的 timing specification | 本页文档第一句 |
| [[wavetable]] | **equation-based 下的对应物**：`specset_id` 指的就是 wavetable | 本页文档参数节（**推断**：原文只说 specset_id 的算法，**没有把 specset_id 与 wavetable 画等号**） |
| [[timing-setup-commands]] | **本章归属**：`## Application` 指向 Timing Setup 那一章 | 本页文档 |
| [[tsus]] | **同章同段的兄弟命令**：`TSUS` 定 timing set 的**数量**，`CLKR` 定 period resolution | 两篇各自的文档 |
| [[timing]] | **本页 `stage: timing` 的理由** | frontmatter |
| `Automatic calculation of period resolution for single-port setups`（raw: `02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md`） | **「最小 period resolution 是多少」的答案在那儿** | 本页文档参数节；**未读** |
| `Determining the period resolution`（raw: `02.06.06.01.04.01.02_Determining_the_period_resolution.md`） | **`## Related information` 唯一那一篇** | 本页文档；**未读** |

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，里面只有一行**：

- `Introduced before SmarTest 6.3.2`

**这一行是哨兵值，不是「6.3.2 新增了 CLKR」**——意思是「在本语料覆盖范围开始之前就已经有了」
（§11.2②，说明在 [[smartest-6.3.2]]）。**所以本页没有版本门槛可报。**
（推断）`CLKR` 在 **SmarTest 7.10.3** 上可用——依据是它早于 6.3.2 这条文档事实；
**这是推断，不是机台核对。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md`
（TDC `98504.htm`，2,781 字节，75 行）。**整篇读完。**

**本页没做的**：

- **文档里链到的五篇一篇都没读**：`WSUS, WSUS? - (Waveform Sets USed)`（`02.06.02.02.342`）、
  `PCLK, PCLK? - (Pin CLocK)`（`02.06.02.02.175`）、
  `Automatic calculation of period resolution for single-port setups`（`02.06.06.01.04.01.02.01`）、
  `Timing Setup Commands`（`02.06.06`）、
  `Determining the period resolution`（`02.06.06.01.04.01.02`）。
  **所以两个数本页给不出**：**period resolution 的下限**（在自动计算那一篇里）、
  **上限**（= 最大 tester period 值，那个值在哪一篇本篇没说）。
- **图一张没看**（本篇没有图）。
- **没有 `## Procedure` / `## Before you begin` 可读**，所以本页没有任何流程叙述。
- **没有用 `edges.jsonl`**，故不报入边/出边条数。

> ⚠️ **本篇的语料瑕疵，照实记下、一处都没替它改**：
>
> ① **`ref_period` 在正文与例子里的说法不一致**：参数节写「Not used. (Ignored)」，
> 而**两个例子的返回值里它都带着一个数**（`< CLKR 1,1000,10` 里的 `1000`、
> `< CLKR "spec_port_1_port_2",50,5.555555556` 里的 `50`）。
> **例 1 的说明写了**「Ignore the returned value of the ref_period parameter.」，
> **例 2 的说明一个字没提这件事**——**同一篇文档对同一个参数两种处理。**
> 本页把两处并列记下，**不判哪个是作者本意**。
> ② **同一个命令两种写法**：语法式是 `CLKR?[type,] {…}`（`?` 后**没有空格**），
> 而正文例子写的是 `CLKR? 1`（`?` 后**有空格**）；`CLKR` 那一侧则两处都有空格。
> **同一篇文档里排版不一致**，照实记。
> ③ **`## Errors` 只覆盖三种入参里的一种**：三条报错讲的都是 `waveform_set`
> （小于 1、超 `WSUS` 范围、`period_res` 超范围），
> **对 `specset_id` 与 `"multi-port_spec"` 两种写法没有给任何报错条件。**
> **这是「缺」，不是「错」**——但它意味着：**用 `specset_id` 写错时该期待什么报错，本篇查不到。**
> ④ **例 1 的代码块里多一个空行**：`< CLKR 1,1000,10` 之后、闭合围栏之前有一个空行，
> 例 2 的块里没有。排版不一致，照实记。
