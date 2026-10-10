---
type: object
title: XPS256 programming - DPS operating mode
layer: L2
stage: level
tags: [level, xps256, dps, dpspins, smartrdi, level-setup, test-head-card]
related: [level, xps256-pmu-operating-mode, xps256-status-flags, dps-pins-editor, level-setup-tool, pin]
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# XPS256 programming - DPS operating mode

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

> **一句话**：**XPS256 这张卡在「DPS 工作模式」下怎么编程。**
> 一张 XPS256 卡能工作在几种模式下（PMU / DPS / …），**模式决定它是什么角色**：
> DPS 模式 = 它当**器件电源**（device power supply）用，给 DUT 供电。
> 姊妹页是 [[xps256-pmu-operating-mode]]（PMU 模式 = 它当参数测量单元用）。
> `stage: level`——因为**在哪一段用它 = 给它定电平/供电**。

**怎么把一根针变成 DPS 模式的针**（原文）：用 `DPS Pins editor` 把它定义成 device
power supply；**和所有其他 DC Scale 卡一样，参数 `Pol` 要设成 `POS`**。

**⚠️ 本页是 7.10.1 才有的**，且 **7.10.3 又改过 hardware view**（见下「版本」）。

### 三种编程入口（原文给的就是这三条）

| 入口 | 覆盖什么 | 何时用 |
|---|---|---|
| **Level setup** | force / clamp 设置 + 动态行为 | **基本设置走这里**（原文推荐） |
| **SmartRDI** | **dc() API 覆盖全部功能**，code-based 与 pattern-based 都支持 | 要在 pattern 里改的时候 |
| **API（`DPS_TASK`）** | 电压/电流**测量** | 测试方法里量值 |

原文的推荐组合是**「基本设置用 level setup，改动用 SmartRDI 的 pattern-based 模式或
DC events」**——**不是二选一，是分工**。

### Level setup 这一路有个硬条件（**本页最该记住的一句**）

> *"To access all features of the card you must use equations."*

**要吃到卡的全部功能，必须用 equations**（即 `Equation based level setup` +
`DPSPINS resources`），**在图形界面上点是不够的**。这是全栈自动化的直接约束：
想用满这张卡，配置得写成方程式。

原文按**九个族**组织支持的参数（族名照抄，**参数逐条见下面「语法 / 参数」节或回 raw**）：
Connections and timing / Current / Constant current check / Dynamic behavior /
Maximum voltage drop / Other / Voltage / Voltage settling time / Voltage slew rate。

### 连接状态 `connect_state` 有一个反直觉的限制（原文）

支持三种：`norm` / `ungang` / `himp`。其中默认值 `norm`：

- **可以在** DPS Setup window 里选，**也可以**用命令 `PSLR`（raw: `02.06_Command_Reference/02.06.02.02.194_PSLR__PSLR__-__Power_Supply_Level_Ranges.md`）编程；
- **但不能在 level setup 的 equation 里显式编程**——**要把值留成默认的 `norm`，
  就必须把 `connect_state` 这个参数整个省略掉**。

> 这是个**容易写错的地方**：写 `connect_state = norm` 和**不写** `connect_state`，
> 在文档的语义里不是一回事。**照文档办：要默认值就别写它。**

### Hardware view（7.10.3 的形态）

按钮共八个，分成「量」与「查」两类：

| 按钮 | 干什么 |
|---|---|
| Measure | 单次或循环的电压/电流测量 |
| Max Voltage Drop / Measure Voltage Drop | 读锁存的最大压降 / 做压降测量（force 与 return 两条线各一份） |
| Force Sense Check | sense 连接测试（Kelvin 测试） |
| Check Gang Connection | 对这根针的所有 ganged 通道做连接检查 |
| Check Status Flags | 读并清锁存的状态标志 → [[xps256-status-flags]] |
| Surge Tracker | 读并清 surge tracker 的锁存状态 |
| Profiling | 对电压/电流做 profiling 并显示采样波形 |

**7.10.3 新加的两样**（原文 `Functional changes`）：**site selection** 与 **multisite
results table**。

- `Focus Site Only` / `All Active Sites`：**注意作用范围**——它只管**子对话框里那些
  标成白色的字段**；站点间取值不同的字段会**高亮成黄色**，悬停显示差异。
- Multisite 结果表**只显示最后一次测量**，可按列排序、可用顶部蓝行的过滤词筛选，
  用工具栏的 Export 导出 CSV。

## 典型用法

**给一根 XPS256 针配成 DPS 并供电，最短路径**（全部来自原文）：

1. 在 `DPS Pins editor` 里把它定义为 device power supply；`Pol = POS`。
2. **基本 force / clamp 与动态行为写在 level setup 里**；要吃到全部功能**得用 equations**。
3. 电平范围相关用 `PSLR` 设；`connect_state` **要默认值就整个省略**。
4. 要在 pattern 里改 → SmartRDI 的 **dc() API**（code-based / pattern-based 都行）或 **DC events**；
   pattern 最高频率见 `Minimum period / maximum frequency of the sequencer`
   （raw: `02.08_Setup_and_Result_Tools/02.08.04.34.06.05.01_Minimum_period___maximum_frequency_of_the_sequencer.md`）。
5. 测量用 **`DPS_TASK`**。查卡的状态/保护标志用 **Check Status Flags** → [[xps256-status-flags]]。

**调试时**：Hardware view 除了标准参数，**还能为这次测量在 DUT board 上切一个电容**
（相关 utility pin、目标状态、目标电容都在 Measure 对话框里定）；
`DPS Protection` 子对话框可以改最大压降、内部 force-sense 连接的状态
（原文叫 `Open Loop Protection`）。

## 和谁有关

**入边 42 条 / 20 篇**（`inline` 口径）。

**姊妹与兄弟**：

- [[xps256-pmu-operating-mode]] —— **同一张卡的另一种模式**，两页互为 Related information
  的第一条。**读一页时必须知道另一页的存在**：卡的能力面是两页合起来才完整。
- [[xps256-status-flags]] —— 本页的 Hardware view 直接有 `Check Status Flags` 按钮；
  它也是保护/断开处理的入口。
- `XPS256 operating modes`（raw: `02.05_Test_Head_Cards/02.05.05.03.05_XPS256_operating_modes.md`）
  —— 模式的总览页，**未建页**。

**上游（谁来配置它）**：

- `DPS Pins editor`（**可建页**：在 `dangling.csv` 里）—— 决定一根针是不是 DPS 模式的就是它
- [[level-setup-tool]]（同样在 `dangling.csv` 里）—— 基本设置写在这儿
- `DPSPINS` / `DPSPINS resources`（raw: `02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）
  —— **equation 里那些参数名的定义都在这一篇**，本页的语法节反复指向它。**未建页**。

**引用它的上下文页**：`XPS256 sitemap`、`XPS256 in DPS operating mode`（`02.05.05.03.05.01`）、
`XPS256 measure currents`、`XPS256 profiling` —— 都是 XPS256 章内的导航与专题页。

**并列模式页**（未建页，不链）：`XPS256 programming - AWG`、`XPS256 programming - DGT`
—— 它们讲 AWG / DGT 时都要求「基本设置按 **PMU 模式**的 API 写」，**这个交叉要求值得注意**。

> 上面每条都来自 `edges.jsonl` 里带原句的边。**本页没有推断。**

## 版本

- **Introduced in SmarTest 7.10.1** —— 本页和 [[xps256-pmu-operating-mode]] 同批引入。
- **SmarTest 7.10.3：Hardware view 增加了 site selection 与 multisite results table。**
  —— **这条就是当前版本**，所以上面写的 site selection 行为在 7.10.3 上是有的；
  **在 7.10.1 / 7.10.2 上不要指望这两个功能**。
- 另有一条硬约束在 `02.01_Release_Information` 里也链了本页（发布信息把它列为新特性）。

## ⚠️ 语料里的坏字符（本文档内）

`pattern鈥慴ased` = *pattern-based*、`sub鈥慸ialogs` = *sub-dialogs*。
**`鈥慴` 不是「一个坏字」，是「短横 + 后面那个字母」一起被编码坏了**：
`鈥慴`=`–b`、`鈥慸`=`–d`、`鈥慼`=`–h`（对照表见 [[pogo-block-compatibility]]）。
**只按「换成 en dash」去替换会得到 `pattern-ased` 这种残词。** 语料问题，raw 不许改（§1.1）。

## 出处

- 定义文档：`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md`
  （TDC `354249.htm`，12,316 字节，126 行）
- **入边 42 条 / 20 篇**（`inline` 口径；其中 3 条是本文档自己指向自己的锚点链接，
  已从「篇」里扣掉——**自引不算被引用**）
- 所属：**Test Head Cards → XPS256**（`02.05.05.03`）
- 本页 `verified: doc-only` —— **没有在任何真实 XPS256 上配过、量过**（§11）。
