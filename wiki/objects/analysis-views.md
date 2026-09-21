---
type: object
title: Displaying test results in analysis views
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.03_Displaying_test_results_in_analysis_views.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Displaying test results in analysis views

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**analysis view（分析视图）是数据日志的一种展示形态。** 原文第一句就是全部机制：

> 「Test results are displayed as analysis views by **selecting summary rows in data navigation
> views** and **choosing the desired view type from the shortcut menu**.」

**动作只有两步：选中若干行 → 右键 → `Show In` → 选视图类型。**
原文对目的的说明是：`Display numeric data log summaries as graphs or tables to more easily
detect interesting or problematic data points or get a global overview of the results.`

### 十二种视图，**差别全在「要选几行」**

这是本页最实用的一张表。**每一种视图对「选中什么」的要求都不一样**，
**选错了就不会出图**：

| 视图 | 要选几行 | 额外的硬条件 |
|---|---|---|
| **Trend chart** | **1 行或更多** | — |
| **Histogram** | 1 行或更多 | **所有行必须同 test suite / test method / test** |
| **Probability chart** | 1 行或更多 | **同上** |
| **Box chart** | 1 行或更多 | **同上** |
| **FFC Pareto chart** | **恰好 1 行** | — |
| **Parametric wafer map** | **恰好 1 行** | — |
| **Shmoo plot** | **恰好 1 行** | **必须是「汇总 shmoo 测试结果」的那一行** |
| **Scan view** | **恰好 1 行** | **结果 type 必须是 `Scan`** |
| **Protocol Monitor view** | 1 行或更多 | **结果 type 必须是 `Protocol`** |
| **Scatter chart** | **恰好 2 行** | **两行必须同 device**；另有附加条件（见该视图专页） |
| **Range chart** | **3 行或更多** | 是 **scatter chart 的一个特殊模式**；**2 行也行，但要再点 scatter chart 里的 `Switch` 按钮** |
| **Bin wafer map** | 1 行或更多 | **要在 `Wafer summary tab` 里选**（**唯一一个不用 Test summary 的**） |

**两处最容易读错的地方：**

> **① 「同 test suite / test method / test」这条要求，对 Trend chart 不是必须的。**
> Histogram / Probability / Box 写的是 **`All rows must share …`（必须）**；
> 而 Trend chart 只写了 **`If all rows share …, the limits are displayed in the graph.`**
> ——**那是「满足了才画限值」，不是「不满足就不让选」。**
> 原文把这同一句话在四种视图下面各抄了一遍，**读快了会把 Trend chart 也当成「必须」。**

> **② 十一种视图都在 `Test summary tab` 里选，`Bin wafer map` 是个例外**，
> 它在 **`Wafer summary tab`** 里选。**原文只在那一行写了这件事**，没有另起一节强调。

### 出图之后的几条通用规则

| 规则 | 原文要点 |
|---|---|
| **同名视图已经开着** | 选中内容**自动**显示进去——**除非那个视图被 pin 住了**（见下） |
| **行数上限** | 一张图同时能显示的行数**有上限**，值在 **Result Tool preferences** 里设 |
| **限值画不画** | 见上面①：**行同属一个 suite/method/test 才画限值** |

### 两个按钮：`Pin` 冻住、`Link` 解冻

这是最容易用错的一处，原文讲得很细：

- **默认行为**：分析视图**始终显示最前面那个 data navigation view 里当前选中的内容**。
  **选中变了，视图跟着变。**
- **点 `Pin` 按钮** → **这个动态更新被打断**，
  视图**继续显示同一批数据，哪怕 summary tab 里的选中变了**。
- **点 `Link` 按钮** → **解冻**，显示**重新跟着选中走**。

**一句话：`Pin` = 冻住，`Link` = 解冻。** 原文用了 `freeze` / `unfreezes` 这两个词。

### 系统数据日志流：默认**不**自动更新

**如果你显示的是 system data log stream**，原文说：

> 「the view is **by default not updated when new log entries arrive**」

**要开自动更新得自己在右键菜单里选**：

| 在哪个 tab | 选哪条命令 |
|---|---|
| `Test summary tab` | **`Auto Update Chart`** |
| `Wafer summary tab` | **`Auto Update Wafer Chart`** |

> **⚠️ 两条命令都不适用于 EDL 或 STDF 数据日志文件**
> （原文：`These commands do not apply to EDL or STDF data log files.`）。
> **也就是说这一整套「自动更新」只对 system data log stream 有意义。**

### 另外两个子菜单与一个按钮

- **Parametric wafer map 和 Shmoo plot**：右键图 → **`Accumulation`** 子菜单 →
  选显示 **最小值 / 均值 / 最大值**。
- **Shmoo plot 另有两个**：**`Pin`** 子菜单（选哪个 pin 的结果）+ **`Result Types`** 子菜单。
- **`New` 按钮**（在图视图里）：**再开一张同类型的图**，
  好让「同一类型、不同数据」并排看。

### 一条版本门槛

> **Shmoo plot 要求数据日志是 SmarTest 7.2.0 或更高版本创建的。**
> `The Integrated Result Tool cannot create shmoo plots from logs created with SmarTest 7.1.4
> or earlier.`
> **即：7.1.4 及更早的日志，做不出 shmoo plot。这条看日志版本，不看当前软件版本。**

## 典型用法

**1. 完整流程**（原文四节拼起来）：

**打开数据日志**（`## Before you begin` 要求的）→
**在 data navigation view 里选中行**（按上表对号）→
**右键 → `Show In` → 选类型** → 需要时再调 `Accumulation` / `Pin` / `Result Types` → 结果出图。

**2. 什么时候用哪种**：

- **看趋势 / 找离群点** → Trend / Histogram / Probability / Box。
- **看两颗 DUT 或两个测试的关系** → Scatter（**2 行、同 device**）；
  要三个以上 → Range。
- **看良率构成** → FFC Pareto（**1 行**）。
- **看 shmoo / scan 这类特殊测试** → 各自的专用视图（**都要 1 行且类型对**）。
- **看 wafer 分布** → Bin wafer map（**要在 Wafer summary tab 选**）。

**3. 下一步**：原文 `## What to do next` 指向
`Set chart display options`（**那篇本页没读**）。

**4. 一条时间上的前提**：**要往图里放大批数据时，先看那个「行数上限」**——
它在 Result Tool preferences 里，**超了不会全画**。

## 和谁有关

- [[results]] — 本页 `stage: results` 的理由：**它是结果数据的展示侧**
- [[shmoo-tool ]] — shmoo 的生成侧；本页只讲**怎么把已有的 shmoo 结果画出来**
- [[timestamp-attr-type]] — 同批建的 `results` 阶段页，讲的是**数据里的时间字段**
- [[tp360]] — 同批建的 `gui` 页
- `Trend chart view` / `Histogram view` / `Probability chart view` / `Box chart view` /
  `Scatter chart view` / `FFC Pareto chart view` / `Protocol Monitor view` / `Shmoo view` /
  `Parametric wafer map view` / `Scan view` / `Bin wafer map view`（**均未建**）—
  **每一种视图自己的专页**；**本页只有「要选几行」，没有它们各自的功能**
- `Test summary tab` / `Wafer summary tab` / `Data navigation views`（**均未建**）—
  选行的两个场所；**它们长什么样本页不知道**
- `Integrated Result Tool`（**未建**）— 这些视图跑在它里面
- `EDL` / `STDF`（**均未建**）— **数据日志的另一种格式**；
  **上面「自动更新不适用」那条正是靠这两种格式划界的**

## 版本

- **Introduced in SmarTest 7.2.0**
- **SmarTest 7.2.1**：`Multiple data series can be displayed for some graph types`
- **SmarTest 7.2.2**：**新增 scan view**
- **SmarTest 7.2.2**：**range chart 支持两个测试**（`Added range charts for two tests.`）
- **SmarTest 7.2.3**：**新增「系统数据日志流图表开/关动态更新」的选项**
- **SmarTest 7.3.2**：**新增 Protocol Monitor view**

> **上面 `7.2.2` 那一条值得和正文对一下**：版本记录写的是
> `Added range charts for **two tests**`，而正文里 Range chart 的要求是
> **`Three or more rows`**（或两行 + 点 `Switch`）。
> **两者不矛盾**——「两个测试」说的是**它支持两行这个情形**，
> 正文说的「三行或更多」是**常规路径**。**本页把两处并列，不替它们调和措辞。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.03_Displaying_test_results_in_analysis_views.md`

**本页没做的**：

- **十二种视图的专页一篇都没读。** 所以：
  **每种视图长什么样、坐标轴是什么、有什么专属选项，本页一个字都没有**——
  本页只有「**要选几行**」和原文在**这一篇里**顺带提到的那几条。
- **四张图一张没看**（`137362.png` Pin 按钮、`137363.png` Link 按钮、
  `137364.png` New 按钮，以及若干内嵌小图）。**本页没有任何来自图的结论**——
  连 `Pin` / `Link` / `New` 三个按钮**长什么样都不知道，只知道名字**。
- **`Related information` 那两篇没读**：
  `Excluding data from evaluation`、`Working with result data tables`。
- **`What to do next` 指的 `Set chart display options` 没读。**
- **`Open a data log`（`Before you begin` 指的那篇）没读**——
  **所以「怎么先把数据日志打开」本页没有。**
- **`Result Tool preferences` 那篇没读**，**那个「行数上限」是多少本页不知道**。

> ⚠️ **本篇的三处语料瑕疵，本页照实记下、一处都没替它改**：
> ① `## Results` 一节写的是 **`The selected information form the summary tabs`**
> ——**`form` 应为 `from`**（本页正文没有引用这一句，故未受影响）；
> ② 「系统数据日志流」那一段里，**一句话以**小写 `if` **开头**：
> `…not updated when new log entries arrive. if you want to enable dynamic updates…`；
> ③ **`Range chart` 那一条链接指向的是 `Scatter_chart_view.md`**，
> **和 `Scatter chart` 那一条的链接目标完全一样**。
> 原文自己说 Range chart 是 `(special scatter chart mode)`，
> **所以这个链接可能是故意的、也可能是漏了它自己的专页——原文没说，本页不判。**

`verified: doc-only`
