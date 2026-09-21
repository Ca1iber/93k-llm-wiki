---
type: concept
title: HV (High-Voltage) protection
layer: n/a
stage: pin
tags: [concept, dut-board, high-voltage, protection, compliance-range, avi64, fvi16]
related: [[dut-board-grounding]], [[utility-line-assignments]], [[sequencer-controlled-utility-lines]], [[pogo-block-compatibility]], [[pin]]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03_HV__High-Voltage__protection.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.01_HV_protection_-_Root_causes_for_high-voltage_damages.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.02_HV_protection_-_Compliance_range.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.03_HV_protection_-_Recommended_protection_circuitry.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.03.01_HV_protection_-_Clamp_diodes.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.03.02_HV_protection_-_Clamp_regulator.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.03.03_HV_protection_-_DC_supply.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.04_HV_protection_-_Impact_on_stimulations_and_measurements.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.04.01_HV_protection_-_Impact_on_leakage_current_example.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.04.02_HV_protection_-_Impact_on_rise_time_example.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.01.05_AVI64_HV__High-Voltage__protection.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# HV (High-Voltage) protection

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**高压卡能烧掉低压卡，所以低压卡要在 DUT 板上加保护电路。**

> High-voltage (HV) test head cards, like the "DC Scale AVI64" for example, provide enough energy to damage low-voltage cards if both are connected via defective DUTs or unintentionally closed connections. Therefore, the low-voltage cards must be protected.

**为什么机台自带的保护不够**——文档把这条说得很直白，两句：

> All test head cards provide basic protection against electrostatic discharge (ESD) but require additional protection against unintentionally applied pulses of high-voltage cards.

> Note All test head cards provide a basic protection against electrostatic discharge (ESD) but this protection cannot absorb the energy coming from a high-voltage card.

**第一条要点**：ESD 保护是**防静电**的，它**吸收不了高压卡的能量**——
这两件事在参数表里长得很像，实际不是一回事。

### 什么情况下会被打坏

> There are two main situations in which high-voltage test head cards damage low-voltage cards:

> - A defective DUT may connect high-voltage input pins to pins, where low-voltage cards are connected.

> - Unintentionally closed connections can connect high-voltage pins directly to pins of low-voltage cards.

**第二条又拆出三种触发方式**（原文另一个小标题下）：

> - Both relays are closed unintentionally while creating and debugging an application.

> - Overlapped switching of the relays is programmed and the high-voltage card is already connected.

> - One of the relays on the DUT board is sticking.

> **⚠️ 第一句里那条「坏 DUT 也可能已经过了低压隔离测试」值得单独记**：
> 原文写的是 `A defective DUT may be the root cause for high-voltage transients even if
> the DUT already has passed low voltage isolation tests.`——
> **「过了隔离测试」不构成保护**。

## 什么时候需要它：合规范围（compliance range）

**判据是「编程电压会不会超过被保护卡的最大外部输入电压」**：

> The protection is required in case a high-voltage card is set to a voltage that exceeds the maximum external input voltage (compliance range) of the low-voltage cards.

**两张范围不要混**：每张卡有 `Operating range`（正常能用）和 `Compliance range`（**加了也不该超过**），
后者比前者宽一点——**中间那一圈余量就是保护电路存在的意义**。

下表**是转述，不是引文**：raw 里这张表**被摊平成一行一格**（单元格被拆散、跨多行），
本页按语义重排成表格，**数值逐格照抄**，**排版是我的**（§11.1：想合成得写成转述）。
原文位置：`02.03.07.03.02_HV_protection_-_Compliance_range.md` 的
`Maximum external input voltage (compliance range) of test head cards` 表。

| Test head card | Operating min | Operating max | Compliance min | Compliance max |
|---|---|---|---|---|
| DC Scale AVI64 | −40.0 V | +80.0 V | −44.0 V | +84.0 V |
| DC Scale DPS128/DPS64 HC | −2.5 V | +7.0 V | −6.0 V | +12.0 V |
| DC Scale DPS128/DPS64 HV | −6.0 V | +15.0 V | −7.0 V | +16.0 V |
| DC Scale FVI16 | −60.0V | +120.0 V | −200.0 V | +200.0 V |
| DC Scale PVI8 | −80.0 V | +80.0 V | −160.0 V | +160.0 V |
| DC Scale UHC4 / UHC4T | 0.0 V | +4.0 V | −3.0 V | +10.0 V |
| DC Scale XPS256 | −2.5 V | +7.0 V | −4.5 V | +7.5 V |
| MBAV8+ measuring units | −4.0 V | +4.0 V | −5.0 V | +5.0 V |
| MBAV8+ source units | −3.5 V | +3.5 V | −5.0 V | +5.0 V |
| PS 1600 | −1.5 V | +6.5 V | −3.0 V | +8.0 V |
| PS 1600 BADC | −3.0 V | +8.0 V | −3.0 V | +8.0 V |
| PS 1600 HV | 0.0 V | +13.4 V | −6.0 V | +16.0 V |

> **⚠️ raw 里这张表带脚注，本页转述时丢掉了**：FVI16 / PVI8 / UHC4 / MBAV8+ 两行标着
> 「SmarTest 7 only」，XPS256 标着「SmarTest 8 only」。
> 原文是 `[1)](<>) SmarTest 7 only[2)](<>) SmarTest 8 only` 这种**散在表末的脚注**，
> **摊平后哪一行挂哪个脚注，靠行号推**——**本页不替它推**，只在这里说明它们存在。

**哪些是"低压卡"（需要保护的一侧）**，原文给了一份清单（**原文分两类列的**）：

- Low-voltage digital cards、Analog cards、Device power supplies (DC Scale cards)、
  DPS-slot device power supplies of SmarTest 7、Port Scale RF cards of SmarTest 7
  与 Wave Scale RF cards of SmarTest 8、Utility cards。

**哪边"高压"也有一份清单**：DC Scale 侧的 AVI64 / DPS128-DPS64 HV version / FVI16，
以及 Pin Scale 与 Smart Scale 数字侧的 PS 1600 HV（high voltage mode）。

> **⚠️ 高压卡之间也会互相打**，不只是高压打低压：
> `The high-voltage cards provide enough voltage and energy to damage low-voltage cards
> but the combination of different high-voltage cards must also be checked carefully.`
> 后面列了四种**高压卡之间**的冲突例子（工作范围与合规范围不兼容、高压 DPS/VI 卡与
> 高压 Pin Scale/Smart Scale 数字卡组合、与浮空通道如 PVI8 叠用、浮空通道反极性连接）。
> **`02.03.08.01.01.05_AVI64_HV__High-Voltage__protection.md` 整篇就是为这一条写的**
> （保护 AVI64 不被 FVI16 打坏）。

## 保护电路怎么构成

> The recommended high-voltage protection circuitry for the production mode consists of the clamp diodes, the clamp regulators, and a DC supply with an additional voltage reference.

三大件，各自的作用（**引脚级细节在三个子文档里，本页只记骨架和判据**）：

| 件 | 干什么 | 数量 |
|---|---|---|
| **clamp diodes** | 把高压脉冲泄放到 clamp rail 上，同时为低压提供隔离 | **每条被保护线、每个 rail 各一个二极管** |
| **clamp regulators** | 把 rail 电压钳在设定值，**并吸收高压脉冲的能量** | **每个 rail 一个**（正一个、负一个） |
| **DC supply** | 供 clamp regulator，并给参考电压 | 通常正负 rail **各一个**；**一个 DC-to-DC 转换器可带四对 regulator** |

**钳位电压是算出来的，不是选的**（两条公式，原文给了）：

```
VClampRail = VReference * ( ( R02 / R03 ) + 1)      ← 正 rail
VClampRail = -1.0 * VReference * R08 / R07          ← 负 rail
```

> The circuit requires a +5.0 V reference voltage for clamp voltages above +5.0 V or a +2.5 V reference voltage for clamp voltages between +2.5 V and +5.0 V.

> **⚠️ 两条 Note 是本页最该记住的一句**（出现在正负两节里，措辞对称）：
> `The forward voltage of the clamp diodes must be added to the calculated value to get the
> actual (positive) voltage on the protected line.`（负侧是 `subtracted`）——
> **算出来的是 rail 电压，线上实际电压还要加减二极管的正向压降。**
> 文档在参考电阻表里**假设了 `Uf = 1.0 V`**，并明说 `The actual forward voltage depends
> on the current through the diodes.`

**电流代价**（原文给了实数）：

> The 24 V current consumption of the circuitry above is about 4.5 mA for each positive or negative clamp regulator. This results in a required current of about 30 mA at the +5 V input of the DC-to-DC converter if an efficiency of 75 % is assumed.

**电从哪来**（这一句把本页接到 utility 电源上）：

> The input of the DC-to-DC converter must be connected to a +5 V utility power supply on the DUT board.

→ [[utility-line-assignments]]、[[sequencer-controlled-utility-lines]]

**还有一个可选的诊断支路**：一个常闭开关 + 一个电阻，让被保护通道**用自身资源**去查
「二极管这条通路通不通」：

> The switch is to be controlled by a utility line or another adequate control signal.

→ [[sequencer-controlled-utility-lines]]

## 它带来的代价：保护电路会改变测量结果

**这是这一族最实用的一节**——装保护不是免费的：

> Additional circuitry on a DUT board always will have an impact on the stimulation and the measurements performed in a test.

**DC 侧两条**：

> - Leakage current measurements may show a minimally increased result.

> - The settling time may increase a little.

**AC 侧两条**：

> - The maximum usable frequency may be reduced a little.

> - The waveform quality may reflect the additional disturbances.

**文档给了两个实测例子**（都在 PS1600 通道上量）：

| 例子 | 结论（原文） | 测法 |
|---|---|---|
| 漏电流 | `The difference between the measurement with and without protection circuitry is less than 1 nA.` | 同一 pogo pin，开/接保护各量一次，128 次平均，settling 5.0 ms |
| 上升时间 | `The rise time is increased by 0.3 ns if the protection circuit is connected.` | 同一 pogo pin，示波器直接量 |

> **⚠️ 上升时间那个例子的 `VIH = 5.0 V` / `VIL = 0.0 V`** 在 raw 里是**被拆成三行的**
> （`Test voltages:` 一格、两个值各占一行），**本页照抄成一句**——
> **这里是转述，不是引文。**

**还有一条影响是"可用范围被吃掉"**：

> The "Resulting voltage" will reduce the usable operating voltage range of the PS1600 BADC from -3.0 V ... 8.0 V to -2.0 V ... 7.0 V.

（**`...` 是原文自己的写法**，本页照抄，§11.1。）

## 文档没写清 / 两篇对不上的地方

1. **高压损伤的"成因条数"，主文档说两条、AVI64 分册说三条，而分册那句主语是错的。**
   主文档：`There are two main situations in which high-voltage test head cards damage
   low-voltage cards:`（后面两条）。
   AVI64 分册：`There are three main situations in which high-voltage test head cards
   damage low-voltage cards:`（后面三条，**多出 `High-voltage pulses created through
   switching off an inductive load.`**）。
   **⚠️ 但 AVI64 那一页整篇讲的是"高压卡打高压卡"**，句子却写 "damage low-voltage cards"——
   **看着是从主文档复制过来、没改主语**。**这是推断，本页不替它裁决**；
   能确证的是**两篇的条数一个 2 一个 3，且多出来那条只在分册里**。
2. **"哪些卡要保护"没有一张完整清单。** 原文给的是**类别**（低压数字卡、模拟卡、
   DC Scale DPS、RF 卡、utility 卡…），**不是型号级清单**。要判断某一台机台的具体配置，
   得逐卡去对上面的合规范围表。**本次未找到型号级的完整清单。**
3. **诊断支路该怎么用，文档只说了"能查"，没说"怎么判"。** 原文说这条支路让被保护通道
   可以检查二极管通路，**但没给判据**（读到什么算通、什么算不通）。**本次未找到。**
4. **保护电路的失效模式文档没写。** 钳位二极管自己坏了会怎样、有没有可测的前兆——
   **本次未找到**。这一条和第 3 条是同一个缺口的两面。
5. **`02.03.07.03.03.02` 的参考电阻表里，某些卡的正负两侧参考电压不是同一个**
   （例如 MBAV8+ 用 `+2.5 V`，PS 1600 用 `+5.0 V`）——表里写着，**但为什么不同，文档没说**。
6. **⚠️ 语料瑕疵（§11.2 ①）**：这一族多篇含 GBK mojibake——
   `卤`（应为 `±`）、`渭`（应为 `μ`）、`惟`（应为 `Ω`）出现在
   DC supply 的 `up to 卤20 V`、电阻表的 `10 k惟`、`1 渭F` 等处。
   **本页避开了含这些字符的行**（`DC supply` 那句"设计到 ±20 V"因此**没引原文**，
   只在此说明）；**raw 一个字节没动**。AVI64 分册的物料表同样含 `卤` / `渭`，
   所以本页只引了它**没有坏字符**的那几段。

## 和谁有关

- [[dut-board-grounding]]——保护电路的泄放路径**归到 DUT 板地**，两页讲的是同一张板子上的事。
- [[utility-line-assignments]]、[[sequencer-controlled-utility-lines]]——
  DC supply 的输入要接 **+5 V utility 电源**；诊断支路要**由 utility line 控制**。
- [[pogo-block-compatibility]]、[[pogo-pad-and-via-design]]、[[inter-layer-via-design]]——
  布线那几条建议（低阻低感、二极管靠近 pogo pin）落在这些页的范围内。
- [[pin]]——脊椎里的 pin 段；**本页是板子设计侧的事，不是测试程序里能改的东西**。
- **AVI64 卡、DPS128/DPS64 卡、PS1600 卡**：[[dps128-dps64-cards]] 有页；
  `AVI64` 与 `ps1600` 目前没有专页（`ps1600` 在 `extract/dangling.csv` 里，**有页会建**）。

> **本页为什么不写成 `constraint` 页。** 「用高压卡时 DUT 板上要加保护电路」形式上是条要求，
> 但 §2.4 的四种形状（顺序前置 / 状态前提 / 一致匹配 / 位置归属）**指的是两个东西之间的关系**，
> 而这里**只有"一块板子要满足一个电气条件"**——没有第二个对象。
> 且原文自报是 `This guideline shows how to implement protection circuitry`，
> **主体是"怎么设计"**（电路、公式、物料、布线），**理解错了才会做错**——这是 §2.3 的 `concept` 判据。
> **同族先例**：[[dut-board-grounding]] 也是板级设计要求，建的就是 `concept`。

## 版本

- 整族（主文档 + 根因 + 合规范围 + 电路三件套）：`Introduced in SmarTest 7.3.1 / 8.1.0`；
  电路在 `SmarTest 7.4.3` 优化过，并**新增了诊断继电器**。
- **AVI64 那套（TVS 二极管方案）是另一版**：`Introduced in SmarTest 7.5.4`——
  **比通用方案晚两版**，说明它不是同一批东西。

> 各篇的 `Functional changes` 还含若干**版本号哨兵值以外的真版本**
> （7.4.0 加 AVI64、7.5.0 加 FVI16、7.6.0 / 8.3.4 加 XPS256）——
> **要查某个功能哪版起，看 [[index-versions]]，不看本页**（§4：机械汇编归脚本）。

## 出处

| 说法 | raw |
|---|---|
| "高压卡能烧低压卡"、ESD 保护不够、组件三条、电流 4.5 mA / 30 mA | `02.03.07.03_HV__High-Voltage__protection.md` |
| 两条成因、三种继电器触发方式、坏 DUT 也过了隔离测试 | `02.03.07.03.01_…Root_causes_for_high-voltage_damages.md` |
| 合规范围表、高压卡/低压卡清单、四种高压卡互打 | `02.03.07.03.02_…Compliance_range.md` |
| 三大件、钳位公式、参考电压、诊断支路、`+5 V utility` | `02.03.07.03.03_…Recommended_protection_circuitry.md` |
| 二极管数量、布线建议、物料 | `02.03.07.03.03.01_…Clamp_diodes.md` |
| 正负公式、两条 forward voltage 的 Note、参考电阻表、BADC 范围被吃掉 | `02.03.07.03.03.02_…Clamp_regulator.md` |
| DC-to-DC、一个转换器带四对 regulator、诊断开关 | `02.03.07.03.03.03_…DC_supply.md` |
| DC/AC 各两条影响 | `02.03.07.03.04_…Impact_on_stimulations_and_measurements.md` |
| `< 1 nA` | `02.03.07.03.04.01_…Impact_on_leakage_current_example.md` |
| `0.3 ns`、`VIH`/`VIL` | `02.03.07.03.04.02_…Impact_on_rise_time_example.md` |
| AVI64 被 FVI16 打坏、三条成因、TVS 方案、`Introduced in SmarTest 7.5.4` | `02.03.08.01.01.05_AVI64_HV__High-Voltage__protection.md` |

**本页的 `## 语法 / 参数` 节是空的**（脚本判定"没有加标记的语法段"）——
**这不是漏了**：这一族没有 `## Syntax` / `## Parameters` 段，
表格散在正文里，**脚本按 §4 拒收**。上面两张表因此是本页手写的**转述**，标注如上。

文档事实，`verified: doc-only`。
