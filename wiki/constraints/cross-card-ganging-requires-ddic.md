---
type: constraint
title: 跨卡 ganging 之前必须先用 DDIC 使能连接
layer: L1
stage: pin
tags: [constraint, ganging, dut-board, pin-configuration]
related: [[pin]], [[ganging]], [[dfpn]], [[pals]], [[dps128-dps64-cards]], [[xps256-pmu-operating-mode]], [[pin-config-requires-sequencer-off]]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 跨卡 ganging 之前必须先用 DDIC 使能连接

## 约束是什么

**要让两块以上 DC Scale 卡上的通道 gang 在一起，必须先用 `DDIC` 把 DUT 板上的那条连接使能。**
不是「软件里把通道列在一起」就算 gang 上了——**硬件走线要先用命令描述出来**。

文档里**两处复现**（两篇不同文档，不是重复投放）：

> Before cross-card ganging can be used, the connection must be enabled by command DDIC.

> Before ganging between boards can be used, the connection must be enabled by DDIC.

`DDIC` 的职责原文（它自己那篇）：

> The DDIC (Define DUT Interface Connection) command describes the DUT board traces that are needed to support ganging across DC Scale cards (UHC4T). The command therefore specifies pogo pins, not pin names.

**注意最后半句：`DDIC` 的参数是 pogo pin，不是 pin 名。** 这是它和 `DFPN` / `DFPS` / `PALS`
最容易被搞混的地方——**前者描述板子走线，后两者描述通道归属**。

> `DDIC` 目前**没有对象页**（它不在 `extract/dangling.csv` 里，也不在 `extract/unowned.csv` 里，
> 所以按 §9.1 **本页不写它的 wikilink**——那是亲手造一个永远填不上的悬空目标）。
> raw：`02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md`

## 在什么条件下成立

**只对「跨卡」成立。** 同一张卡内 gang 不需要 `DDIC`：

> DPS128/64: Ganging is possible for any number of successive channels within a card, but not across cards.

**例外：XPS256 完全不需要 `DDIC`**（文档事实，`DDIC` 自己那篇，原句是连着的两句）：

> This command is not applicable for DC Scale XPS256 card. Ganging across XPS256 cards is controlled via internal data paths and need not to be defined separately.

## 同时生效的第二条约束：connectionSet 必须一致

**为跨卡 ganging 服务、由 `DDIC` 和 `DFPN` 定义的走线，必须带同一个 `connectionSet`**：

> All traces that are needed for a cross-card ganging group and are defined by the DDIC command and the DFPN command must have the same connectionSet defined.

**`connectionSet` 的默认值语义**（同篇）：

> Default connection set: The default connection set is defined if this extra parameter is not used or if an empty string is programmed. A DC Scale pin can be defined in only one default connection set.

> **⚠️ `DDIC` 那篇的参数表里，`connectionSet` 那两格读起来自相矛盾**——
> 一格写 "This parameter is currently not used."，另一格紧接着写它 "adds the ability to
> define several pins containing the same DC Scale channel in PMU mode"。
> **本页不引用这两句**：raw 的参数表是**被摊平成一串单元格的**，
> 「currently not used」很可能属于同一格里的另一行参数，**不能当文档矛盾用**。
> 判据：`DFPN` 那篇明确讲了 `connectionSet` 的行为（默认集合、一个 DC Scale pin
> 只能属于一个默认集合），**说明这个参数在被使用**。§10 第 0 步的同类处置：
> **先查是不是结构/投放造成的，再报冲突。**

## 哪些通道能 gang

**文档按卡族逐条列出**（原文是 `DFPS` 参数表里的分条列表，本页照抄）：

> - DPS128/64: Ganging is possible for any number of successive channels within a card, but not across cards.

> - XPS256: Only channels on the same HLA can be ganged.

> - UHC4, UHC4T: For UHC4 or UHC4T ganging is possible for any number of successive channels within a card and any number of cards within a test head. The combination of UHC4 and UHC4T within the same ganging group is not supported. The maximum current per card cannot be exceeded.

`PALS` 那篇把 UHC4/UHC4T 的**物理相邻要求**写得更细：

> For UHC4 / UHC4T the channels must be physically adjacent on the same board, or be the last (the 4th) channel of a board and the first of another UHC4 / UHC4T board. You cannot gang UHC4 and UHC4T boards.

**工程含义**：`UHC4` 与 `UHC4T` 不能混 gang，且跨板时只能「第 4 通道 → 下一板第 1 通道」这样首尾相接。

`DFPS` 还有一条同族的（`DPS128/64`）：

> DPS128/DPS64 channels must be of the same type (HC or HV).

## 违反了会怎样

**`DFPN` 的 Errors 段有一条直接判这个**：

> Ganging is defined for DC Scale channels, and not all specified channels are DC Scale channels.

> **⚠️ 反过来的情形文档没写。** 「忘了先 `DDIC`」「`connectionSet` 不一致」
> 这两种违反**在文档里找不到报错描述**——本次未找到。本页不猜。

## DDIC 怎么写

语法（`DDIC` 自己那篇，原文代码块）：

```
DDIC ["connectionSet",] {"circuitry_type"}, {(cp1,cp2)}
```

```
DDIC? {"circuitry_type"}
```

`circuitry_type` 的取值。**原文是一张「取值 | 说明」两列表，抽取时被摊平成一行一格**——
所以下面**取值与说明是两格，本页分开引，不合成一行**：

> CONN

> A simple direct connection between the given pogo pins.

`CONN` 那一格里紧接着还有一段（**同一格**，原文另起一行）：

> Two pogo pins on one or two DC Scale cards (UHC4T) must be given: One GANG_IN (pppGI) pogo and one GANG_OUT pogo (pppGO).

> CLR

> Clears all previously defined circuitry.

> ALL

> Only for queries:

> Returns all previously defined circuitry.

> ⚠️ **本页原先在这里写的是三行 `- CONN — …` / `- CLR — …` / `- ALL — …`。那三行是我编的。**
> raw 里**没有那种行**——原文就是上表摊平后的**一格一行**，
> 既没有 `- ` 列表符，也没有 `— ` 破折号。**把两格合成一行、再补上列表符，
> 那就不再是引文**（§11.1；想合成得写成转述）。改法就是现在这样：取值、说明分开引，原样。
> 这件事记在 §13.1 **第十二次**。

`PALS` 那篇给了一段**实际顺序**的例子，里面含 `DDIC`（原文代码块，**注意 `DDIC` 在 `PALS` 之前**）：

```
DDIC CONN, (104GO, 105GI)
DDIC CONN, (105GO, 107GI)
PALS 2,(10403, 10404, 10501, 10502, 10503, 10504, 10701, 10702),,(dc1)
```

紧跟着的原文说明：

> This example defines a master/slave configuration for DC Scale UHC4 channels across boards. The first channel is the master.

**这段例子是本页约束最直接的例证**：先 `DDIC` 连接，再 `PALS` 分配。

## 出处

| 说法 | raw |
|---|---|
| 跨卡 ganging 要先 `DDIC`（措辞一） | `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md` |
| 跨板 ganging 要先 `DDIC`（措辞二） | `02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md` |
| `DDIC` 的职责、XPS256 例外、语法、`circuitry_type` | `02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md` |
| `connectionSet` 一致、默认集合、Errors 一条 | `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md` |

文档事实，`verified: doc-only`。

## 相关约束

- [[pin-config-requires-sequencer-off]]——`DFPN` / `PALS` / `DFPS` 都在那条锁的管辖内。
- [[ganging]]——概念页（**尚未建立**，是 `extract/dangling.csv` 里的悬空目标）。
