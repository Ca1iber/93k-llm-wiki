---
type: constraint
title: Pin configuration 命令要求 sequencer 处于 OFF
layer: L1
stage: pin
tags: [constraint, pin-configuration, sequencer]
related: [[pin]], [[sqst]], [[dfpn]], [[udef]], [[conf]], [[pals]], [[pin-config-locked-during-test]], [[sequencer]]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.02_Assigning_a_pin_name_to_a_digital_channel.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Pin configuration 命令要求 sequencer 处于 OFF

## 约束是什么

**改动 pin configuration 之前，sequencer 必须是 OFF 状态。** 这不是某一个命令的规矩，
而是**整个 pin configuration 命令族共有的前置条件**——`DFPN`、`UDEF`、`CONF`、`PALS`
各自的文档里都写了同一条，措辞不同。

`stage: pin` 填的是**最近的一段**，不是归属：这条约束的服务对象就是 pin configuration 本身
（§6：填「最近的一段」而不是「归属」）。

## 在什么条件下成立

适用于**所有会改动 pin configuration 的操作**，文档里逐条写明：

- **`DFPN`（给数字通道指派 pin 名）**——命令页原文：

  > Note that before you can use the DFPN command the sequencer state must be OFF (see the SQST command).

  同一句话在**另一篇文档**里也写了一遍（`source_topic` 不同，**不是重复投放**，
  见 §10 的判据）：

  > Note that you can use the DFPN command only if the sequencer state is OFF (compare the SQST command).

- **`UDEF`（取消 pin 定义）**——Errors 段。
- **`CONF`（配置 pin 类型与工作模式）**——Errors 段。
- **`PALS`（多 site 的通道分配）**——Errors 段。

**为什么是「改配置」这一类而不是某一个命令**：pin configuration 是 level / timing / pattern
的前置条件（见 [[pin]] 的「下一步」），所以这条锁保护的是**整条下游**——
配置在运行中被改掉，下游三类 setup 的前提就全不作数了。

## 违反了会怎样

文档给了两种说法，**都是文档事实**：

**① 条件句（`DFPN` 命令页、`DFPN` 任务页）**：sequencer 不是 OFF 就**不许用**这条命令。

**② 报错句（`UDEF` / `CONF` / `PALS`）**——这三条是原句：

> An error is generated if you attempt to undefine pins while the sequencer is in the run or the break state.

> An error is generated if you attempt to configure pins while the sequencer is in the run or the break state (see the SQST command).

> The sequencer is in RUN or BREAK mode.

第三句是 `PALS` 的 Errors 段里**错误条目列表中的一条**（原文如此，它写作 `mode`，
而 `UDEF` / `CONF` 写作 `state`——**这个措辞不一致在 raw 里，不在本页**，§11.2）。

> **⚠️ 两种说法不是同一件事，别合起来读。** ① 说的是「命令的可用条件」，
> ② 说的是「命令执行时报什么错」。**中间的差别是「什么时候检查」**——
> 文档没有写明检查发生在解析时还是执行时。**本次未找到**关于检查时机的描述。

**③ `DFPN` 的 Errors 段里还有一条与 ganging 有关的**（不是 sequencer 状态，
但同属那张错误列表，且它是 [[cross-card-ganging-requires-ddic]] 的一条佐证）：

> Ganging is defined for DC Scale channels, and not all specified channels are DC Scale channels.

## 怎么确认当前状态

用 `SQST` 查 sequencer 状态——`DFPN` 的两处原文都指向它（"see the SQST command" /
"compare the SQST command"）。→ [[sqst]]

## 出处

| 说法 | raw |
|---|---|
| `DFPN`「must be OFF」 | `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md` |
| `DFPN`「only if … is OFF」 | `02.06.03.01.02_Assigning_a_pin_name_to_a_digital_channel.md` |
| `UDEF` 报错句 | `02.06.02.02.295_UDEF_-__UnDEFine_pin.md` |
| `CONF` 报错句 | `02.06.02.02.31_CONF__CONF__-__CONFiguration.md` |
| `PALS` 错误条目 | `02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md` |

全部为**文档事实**，`verified: doc-only`（§11：「文档里有」≠「这台机器上能用」）。

## 相关约束

- [[pin-config-locked-during-test]]——**更强的一条**，说的是「测试运行中固件不接受
  任何配置改动」。两条一起看才是完整的前置条件：**OFF 是能改配置的窗口，
  但窗口开着也不等于可以随便改**。
- [[pals-before-other-setup]]——`PALS` 在命令族内部还多一层顺序要求。
- [[cross-card-ganging-requires-ddic]]——ganging 相关的前置条件。
