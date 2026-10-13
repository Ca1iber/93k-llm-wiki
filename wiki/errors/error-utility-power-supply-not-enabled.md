---
type: error
title: 外部 utility 电源的输出使不了能
tags: [error, troubleshooting, utility-power, dut-board, diagnostics]
related: [[sequencer-controlled-utility-lines]], [[utility-line-assignments]], [[pogo-block-compatibility]], [[dut-board-grounding]], [[smartest-7.2.0]]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05.06.03_External_utility_power_supply_-_Installation__diagnostics__troubleshooti.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# 外部 utility 电源的输出使不了能

## 症状

**不是一条报错文本，是一种现象**：外部 utility 电源（external utility power supply）
的**输出没能被使能**。文档的原文入口句：

> In case, the power outputs of the external utility power supply are not enabled, do the following:

**这是本页和别页最不一样的地方**：它没有可搜的报错串，**只有现象**。
所以本页是给「现象 → 检查项」用的。

**先确认它是不是你要找的东西**：这块电源是**选件**——

> The external utility power supply unit is an optional device. As such, its installation takes place at the customer site.

> ⚠️ 原文里这句和下一句之间插了一行 ` |  Supported V93000 systems…`——
> **那是被摊平的表/注记边栏**，不是正文断句（同 §11.2 ① 那类抽取瑕疵）。
> 本页只引连续的那两句。

## 触发条件

**这块电源要能被使能，前提条件不止「接上电」**——文档的检查清单本身就是触发条件表。
**尤其注意最后一条：它要求 DUT 板上两个 pogo pin 被接到 UGND**，
也就是说**这块电源只有在「DUT 板已接上」时才会开**。**这是最容易漏的一条。**

## 怎么办

**按原文顺序，七条（照抄，含列表符 `- `）：**

> - Ensure that the external utility power supply has its power cord connected.

> - Ensure that the external utility power supply is turned on: There is a small switch near the AC input terminal.

> - Ensure that the model file of SmarTest 7 or the tester.model file of SmarTest 8 is configured for active wiring board; one line should look similar to the following one: `utility_lines = ..., type=sequencer_controlled, pogo_size=32`

> - When turning on the test head, the fan of the external utility power supply should start running for a short time and afterward it stops.

> - Start the software and load a device that uses 32 utility lines per block (this is a prerequisite to run the diagnostic with all 4-row utility block features).

> - Start the diagnostic (at least the utility line test) with an E7010F Diagnostics Interconnect board (there are different versions of E7010F, that should all work - any older interconnect board up to E7010E will not test the external utility power supply).

> - Check the log files to ensure that the external utility power supply was tested. When the diagnostic fails or when the external utility power supply is not tested at all you have to check the power supply and the cabling.

**第七条后面紧跟一个 Note，本页分开引**（原文里 `cabling.Note` 是粘着的）：

> Note The external utility power supply is not configured in the model file. Diagnostics measures therefore the impedance of the supply outputs. The actual tests of the output voltage are performed only if the supply has been detected by the impedance measurements.

**这一条解释了诊断为什么可能「什么都没测」**：诊断**先量输出阻抗**，
阻抗看着不对（＝没检测到这块电源）就**根本不做电压测试**。
**所以日志里「没测」和「测了不通过」是两件事**——前者是没认出硬件，后者才是真失败。

**最后一条是最容易漏的**（原文独立一段）：

> When the external utility power supply tests are passing you have to check your DUT board: Pogo pins "DSC" and "POG4R" of the utility pogo blocks must be connected to UGND. These pins indicate that the DUT board is connected and that 4-row pogo blocks are used that is a prerequisite to turning on the power supply.

→ [[dut-board-grounding]]、[[pogo-block-compatibility]]、[[utility-line-assignments]]

**还有一个「反过来的坑」**（原文独立一段，本页照抄）：

> Note that the external power supply cannot be easily activated when the E7010F Diagnostics Interconnect board is docked: interface: The connectivity of the "DSC" and "POG4R" pogo pins is also tested by the diagnostic and these lines are not at low level by default!

**意思是：诊断板插着的时候，这块电源反而不容易使能**——因为诊断也在测那两个 pin，
而它们默认不是低电平。**「插上诊断板去查为什么使不了能」这个动作本身会干扰现象。**
（原文 `docked: interface:` 这处粘连是 raw 的排版缺陷，本页照抄不修。）

## 诊断工具

> The UTIL - Utility connectivity test checks the correct functioning of the external utility power supply.

**跑它有个前提**（原文里 `supply.Note` 粘着，本页分开引）：

> Note To run the test you must dock the E7010F interconnection board.

**注意这条和上面那个「坑」是同一件事的两面**：
诊断**必须**插 E7010F 才能跑，**而插着 E7010F 时电源本身又不容易使能**。
**所以诊断能跑通 ≠ 电源能被使能**——两件事。

## 文档没写清的地方

1. **「输出没被使能」的具体表现文档没写。** 是量不到电压？是软件报错？是 DUT 不上电？
   **本次未找到**。这是本页最大的空白——**症状描述只有那一句条件句**。
2. **`type=sequencer_controlled` 这个写法要求哪一版起，本篇没写**
   （本篇的 `## Functional changes` 只有 `- Introduced in SmarTest 7.2.0`，
   讲的是**外部电源这个选件**，不是这一行配置）。→ [[sequencer-controlled-utility-lines]]
3. **`pogo_size=32` 的 32 与「32 utility lines per block」是不是必须是同一个 32，
   文档没说。** 两处都写了 32，**看着是同一件事，但本页不把它写成文档事实。**

## 出处

| 说法 | raw |
|---|---|
| 选件性质、症状入口句、七条检查清单、两个 Note、最后那条 DUT 板检查 | `02.03.05.06.03_External_utility_power_supply_-_Installation__diagnostics__troubleshooti.md` |
| `UTIL - Utility connectivity test` 与它要插 E7010F 的前提 | 同上 |
| `- Introduced in SmarTest 7.2.0` | 同上（**这条不是哨兵值**，是真版本，见 §11.2 ②） |

文档事实，`verified: doc-only`。
**本篇同族的兄弟页**：`02.03.05.06.01`（能力与行为）、`02.03.05.06.02`（配置与 DUT 板设计）、
`02.03.05.06`（总览）。**都没有 wiki 页**，故写文件名不写 wikilink（§9.1）。

## 相关

- [[sequencer-controlled-utility-lines]]——`type=sequencer_controlled` 那一行配置讲的就是它。
- [[utility-line-assignments]]——「32 utility lines per block」与 `pogo_size` 属于这个主题。
- [[pogo-block-compatibility]]、[[dut-board-grounding]]——最后那条 DUT 板检查直接落在这两页上。
- [[smartest-7.2.0]]——本篇 `Functional changes` 说的就是这一版引入的选件。
