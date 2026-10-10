---
type: object
title: DFPS, DFPS? - (DeFine Power Supply)
layer: L1
stage: pin
tags: [pin, dfps, dps, dc-scale, ganging, channel, polarity, power-supply]
related: [pin, dfpn, pals, pste, cross-card-ganging-requires-ddic, dps-pins-editor, mapping-pin, pin-configuration-file, dc-scale-xps256-card, dps128-dps64-cards, dc-scale-uhc4t-card, smartest-6.3.2, smartest-6.5.0, smartest-7.3.1, smartest-7.3.2, smartest-7.4.0, smartest-7.5.0]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# DFPS, DFPS? - (DeFine Power Supply)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,402 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFPS

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

### DFPS?

```
DFPS? {(pinlist)}
```

returns:

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98551.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：dps_channel | The test system channel number of the DPS channel to be configured. The channel is to be defined as follows: For external device power supplies, t…

### Example 1

```
DFPS 11,POS,(Vee)
```

This example connects device pin Vee to channel 1 of DPS board 1. The DPS output polarity is positive.

### Example 2

|


```
DFPS (10101, 10102),POS,(vee)
```

 |
 |

```
DFPS (10101-10102),POS,(vee)
```

 |

Both lines define the same master/slave configuration for DC Scale channels in DPS mode. They just use different notations. Note the five digit channel numbers.

### Example 3

```
DDIC CONN, (104GO, 105GI)
DFPS (10403, 10404, 10501, 10502),POS,(vee)
```

This example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across two boards.

### Example 4

```
DDIC CONN, (104GO, 105GI, 105GO, 106GI)
DFPS (10403, 10404, 10502, 10503, 10504, 10601),POS,(vee)
```

This example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across three boards.

### Example 5

```
DDIC CONN,(230GO, 227GI)
DFPS (23004, 22701),POS,(VDDCI)
```

This example specifies the ganging of channels across two DC Scale UHC4 cards.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

-  You define more than the number of installed DPS pins.
-  The requested DPS channel has already been allocated.
-  The requested DPS channel is not installed.
-  The addressed DPS is not installed.
-  The requested DPS channel number is not valid.
-  The requested DPS pin has already been defined.
-  You try to assign DPS channels in the connected state.

<!-- 报错节 end -->

## 是什么

**`DFPS`（DeFine Power Supply）告诉软件：哪个 DPS channel 接在哪个 device pin 上，以及这个 channel 的极性。**
`DFPS?` 是它的查询形态。原文第一段两句就是全部定义：

> 「The DFPS (DeFine Power Supply) command tells the software which DPS channel is connected to the specified device pin, and the polarity of the channel. The DFPS? query returns the existing channel, polarity and assigned pin number.」

**它有两副面孔**（原文接着写的两句，很多用法只用到第一副）：

> 「The DFPS command can also be used to configure one or more DC Scale channels for DPS mode.」

> 「Ganged configurations for DC Scale channels in DPS mode are defined with the DFPS command (by specifying a channel list for the first parameter, see below).」

| 面孔 | 干什么 | 第一个参数写什么 |
|---|---|---|
| **① 绑定** | 把**一个** DPS channel 绑到一根 device pin，并给极性 | **一个数字**（`dps_channel`） |
| **② 成组** | 把**一组 DC Scale channel 配成 DPS 模式并 gang 起来** | **括号包起来的一串**（`(DC_scale_channel_list)`） |

**第二个面孔是「用同一个命令的同一个参数位表达两种语义」**——原文自己说 `by specifying a channel list for the first parameter`。

### 语法（**这两行不在本页的「语法 / 参数」节里**）

raw 里它们挂在 `## DFPS` / `## DFPS?` 两个**自定义段名**下，不是 `## Syntax`——
脚本只抽 `## Syntax` / `## Parameters`，所以**本页的语法节里没有它们**。
**本页不改语法节，在这里逐字引一次**：

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

```
DFPS? {(pinlist)}
```

`DFPS?` 的返回形态原文也给了（**和 `DFPS` 自己的签名长得一样**）：

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

**参数顺序：channel → polarity → pin。**这一点钉得很死——理由见下节。

### 参数顺序已被三处独立钉死（**其中一处比图证更硬**）

| 证据 | 内容 |
|---|---|
| **① 原文自己的签名行**（**文档事实**） | 见上一节的代码块（`dps_channel` 先、`polarity` 次、`pin` 末）——**顺序就是原文写出来的那个样子** |
| **② 原文的 Example 1 正文**（**文档事实**） | `DFPS 11,POS,(Vee)` 配的话是 `This example connects device pin Vee to channel 1 of DPS board 1. The DPS output polarity is positive.`——**`11` 是 channel、`POS` 是 polarity、`Vee` 是 pin** |
| **③ [[mapping-pin]] 的图证**（**④ 档**） | 那页读的是 `02.08.04.18.04` 的三张截图，其中 DPS 那张 `105641.png`（`Name`=`VCC1`、`Polarity`=`POS`、`Tester Channel`=`DPS11`）对上同篇文件例子里那一行 `DFPS 11,POS,(VCC1)`，于是得出 `DFPS <Tester Channel 里的数字>,<Pol>,<Name>`（`DPS` 前缀**不进文件**） |

**三处一致。**（[[mapping-pin]] 那一页另记了一条 2026-09-20 的收窄：那批截图的**列名是 7.1.3 之前的旧名**
（`Polarity` → 现名 `Pol`），**但参数顺序的结论不受影响**——本页的 ①② 两处是文字，不涉及列名。）

> **本页为什么不担心跨 site 的情况**：[[mapping-pin]] 记着一条它自己覆盖不到的缺口——
> 「多 site 时 `DFPS` 那行怎么写，本页没有依据」。**本页的语料同样答不了**：
> 参数表把 `dps_channel` 说成 `The test system channel number of the DPS channel to be configured.`，
> **没有提 site**；五个例子**也全是单 site 形态**。→ **多 site 写法：语料未写。**

### 第一个参数：两种数字形态（**这是最容易配错的地方**）

| 接什么 | 数字形态 | 规则（原文逐字提炼） |
|---|---|---|
| **external device power supplies**（板外的电源） | **三位或四位整数** | 前一位或两位 = **外部电源编号**——原文建议 `using values above 8` 以避开内部电源，**最大值 16**；后两位 = **该电源的 channel 号**，**小于 10 要补前导 `0`** |
| **DC Scale channel（DPS 模式）** | **五位数**，格式同 digital I/O channel | 例子里全是五位数（`10101` / `10403` / `23004`…） |

**这两条形态差别就是「三/四位 vs 五位」**——写错了会撞上「`The requested DPS channel number is not valid.`」那条报错。

### 第二个参数：极性（`POS` / `NEG`）

| 取值 | 原文 | 使用条件 |
|---|---|---|
| **`POS`** | `Enter POS only if the DPS connections on the DUT board are as follows: The force is connected to power; the sink is connected to ground. The voltage supplied to the device will then be exactly as entered in the Level Setup, but the entry made there must be positive, otherwise the system returns an error.` | **是有条件的**：force 接电源、sink 接地；而且 **Level Setup 里填的必须是正值**，否则系统报错 |
| **`NEG`** | `NEG is not allowed for DC Scale channels.` | **DC Scale channel 只允许 `POS`** |

**所以「DC Scale 通道只能给 `POS`」是一条硬规矩**——原文在两处各说一遍
（`POS` 那一格写 `For DC scale channels, only POS is allowed.`，`NEG` 那一格再反着说一遍）。

### 第三个参数：pin 名；查询用的第四个名字是 `pinlist`

- `pin` = `Defines the pin name for the DPS channel.`
- `pinlist`（**`DFPS?` 用**）=

> 「The pin name or names of those power supply outputs which have already been defined. If more than one pin is required, the names must be separated with a comma. The @ character can be used to read all configured power supply pins.」

**`@` 可以一次读回所有已配置的 power supply pin**——
但**原文没有给一条 `DFPS? (@)` 的例子**（见「出处」瑕疵⑤）。

### ganging 的四种卡，限制各不同（**本页信息密度最高的一张表**）

| 卡 | ganging 范围 | 额外条件（原文逐字） |
|---|---|---|
| **DPS128/64** | 卡内**任意个连续 channel**，**不跨卡** | `DPS128/DPS64 channels must be of the same type (HC or HV).`；**每卡 ganging group 数上限 = channel 数的一半**；`The maximum current per card cannot be exceeded.` |
| **XPS256** | **只有同一 HLA 上的 channel 能 gang** | 无附加句 |
| **UHC4 / UHC4T** | 卡内任意个连续 channel **+ 一个 test head 内任意多张卡** | **`The combination of UHC4 and UHC4T within the same ganging group is not supported.`**；同上「每卡最大电流不得超」 |
| **（跨卡总前置）** | — | 原文：`Before cross-card ganging can be used, the connection must be enabled by command DDIC.` |

**读这张表时的两点注意：**

- **「任意个连续 channel」是 `DC_scale_channel_list` 那一格给的**，写法有两种：
  `either as comma separated list or as range, for example 10105-10106` ——**逗号列表和区间都行**。
- **跨卡那条前置不是建议，是硬条件**：原文用 `must be enabled by`。
  它对应本 wiki 的约束页 [[cross-card-ganging-requires-ddic]]，**本页是这条约束的命令侧出处之一**。
  （原文里那个 `DDIC` 是指向 `DDIC` 那一篇的**语料内部链接**；本页的「语法 / 参数」节里它已被脚本改写成
  `DDIC`（raw: `路径`）的形式——**本页一个字没动它**。）**`DDIC` 那一篇本页没读。**

### 多 site 不归它管

> 「Multi-site configurations are defined by the PALS and PSTE commands.」

**这是原文在 DFPS 自己这一篇里划的界**：`DFPS` 管 channel↔pin 的绑定与极性，
**多 site 的分配归 `PALS` / `PSTE`**。**别把两件事混在一个命令上。**

## 典型用法

### 五个例子，按「你要干什么」排成一张表

| 你要干什么 | 原文的那两/三行（逐字） | 原文的说明 |
|---|---|---|
| **单根针绑到内部 DPS** | `DFPS 11,POS,(Vee)` | `This example connects device pin Vee to channel 1 of DPS board 1. The DPS output polarity is positive.` |
| **两个 DC Scale channel gang（逗号写法）** | `DFPS (10101, 10102),POS,(vee)` | 与下一行**完全等价** |
| **同上（区间写法）** | `DFPS (10101-10102),POS,(vee)` | `Both lines define the same master/slave configuration for DC Scale channels in DPS mode. They just use different notations. Note the five digit channel numbers.` |
| **跨两张板 gang UHC4** | `DDIC CONN, (104GO, 105GI)`<br>`DFPS (10403, 10404, 10501, 10502),POS,(vee)` | `This example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across two boards.` |
| **跨三张板 gang UHC4** | `DDIC CONN, (104GO, 105GI, 105GO, 106GI)`<br>`DFPS (10403, 10404, 10502, 10503, 10504, 10601),POS,(vee)` | `This example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across three boards.` |
| **跨两张 UHC4 卡 gang** | `DDIC CONN,(230GO, 227GI)`<br>`DFPS (23004, 22701),POS,(VDDCI)` | `This example specifies the ganging of channels across two DC Scale UHC4 cards.` |

**从这五行里能读出来的三条（都是原文摆出来的，不是本页加的）：**

1. **跨卡 ganging 一定是两行**：先 `DDIC CONN` 使能连接，再 `DFPS` 配通道。**例 3/4/5 全是这个形状。**
2. **`DFPS` 的通道号是五位数、`DDIC` 的通道号带 `GO` / `GI` 后缀**——
   `104GO` 对 `10403` / `10404`，`105GI` 对 `10501` / `10502`。
   **这两个编号体系怎么换算，原文一个字没说**（见「出处」瑕疵⑤）——**照抄例子即可，别自己推。**
3. **例子 `DFPS` 那一行的 pin 名可以是小写 `(vee)`**（例 2/3/4）**也可以是大写 `(Vee)` / `(VDDCI)`**（例 1/5）。
   **原文在两种写法之间来回换，没有说大小写有没有区别。**

### 顺序规矩（**只有一个，但是硬条件**）

**先 `DDIC` 再 `DFPS`。**依据是原文那句 `Before cross-card ganging can be used, the connection must be
enabled by command DDIC.`——**`Before` 与 `must` 都在**。
（对应的约束页是 [[cross-card-ganging-requires-ddic]]。）

**形状就是例 3/4/5 那个形状**：第一行 `DDIC CONN, (<DDIC 通道列表>)`，
第二行 `DFPS (<DFPS 五位数通道列表>),POS,(<pin 名>)`。
**两行的通道编号体系不同（`GO`/`GI` vs 五位数），换算关系语料没说**——
**照抄例 3/4/5 的配对，别自己推。**

**注意范围**：这条前置**只管跨卡**（`cross-card`）。
**卡内 gang（例 2）原文没有要求先 `DDIC`**——例 2 就是两行 `DFPS`、没有 `DDIC`。

### `DFPS?` 怎么用

- **写 `@` 读回全部**：参数表的 `pinlist` 说明写了 `The @ character can be used to read all configured power supply pins.`
  ——所以 `DFPS? (@)` 是它的用法。**但原文没有给例子**（这一条是**本页按参数表推的，标（推断）**）。
- **列出若干根针**：参数表说 `If more than one pin is required, the names must be separated with a comma.`
- **返回形态**：就是 `DFPS` 的那一行签名（见「是什么」）——
  **即 `DFPS?` 的回复是可以直接抄回文件里的**。

### 报错了怎么办（**症状 → 先怀疑什么**）

七条报错在「报错条件」节里逐字列着。**按「你刚才大概做了什么」对号**：

| 报错（逐字） | 先怀疑什么 |
|---|---|
| `You define more than the number of installed DPS pins.` | **你定义的数量超了机上装的 DPS pin 数** |
| `The requested DPS channel has already been allocated.` | **这个 channel 已经分给别人了**（可能是前面某条 `DFPS` 用了） |
| `The requested DPS pin has already been defined.` | **这个 pin 名已经用过了** |
| `The requested DPS channel is not installed.` | **这个 channel 在机上不存在** |
| `The addressed DPS is not installed.` | **这块 DPS 板在机上不存在** |
| `The requested DPS channel number is not valid.` | **数字形态写错了**——回去对「三/四位（外部电源）vs 五位（DC Scale）」那张表 |
| `You try to assign DPS channels in the connected state.` | **通道已经 connected 了**——得先断开。**但「用哪条命令断开」，本篇没写**（见「出处」） |

**两条最容易看混的**：**`has already been allocated`（channel 被占了）** 与
**`has already been defined`（pin 名被占了）**——**一个说通道、一个说名字**。

### 一个本页答不了的（**照实说**）

**多 site 的时候 `DFPS` 那一行怎么写？**——**本篇答不了**：
`dps_channel` 的参数说明只说它是 `The test system channel number of the DPS channel to be configured.`，
**没有 site 维度**；五个例子**全是单 site 形态**。
原文反而把多 site 明确划给了别人：`Multi-site configurations are defined by the PALS and PSTE commands.`
——**但「`PALS`/`PSTE` 与 `DFPS` 在多 site 下怎么配合」，本篇没写。**

**「connected state 下不许分配」这条报错要用哪条命令解开**——**本篇也没写**
（原文只说了 `You try to assign DPS channels in the connected state.` 会报错）。

## 和谁有关

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[dfpn]] | **同族的前一条命令**（DeFine Pin Name）：`DFPN` 给**数字 channel** 分配 pin 名与 pin 号，`DFPS` 给 **DPS channel** 绑 pin 并给极性。两条都是 pin 配置期的命令、都落在同一个 pin 配置文件里 | [[mapping-pin]] 主表把两条排在同一段的前两行（**本页读过的 wiki 页**） |
| [[cross-card-ganging-requires-ddic]] | **本页是这条约束的命令侧出处**。原文那句 `Before cross-card ganging can be used, the connection must be enabled by command DDIC.` 就是它 | 本篇引文（**文档事实**） |
| [[pals]] / [[pste]] | **分工边界，不是同类**。原文逐字把多 site 配置划给这两条：`Multi-site configurations are defined by the PALS and PSTE commands.` | 本篇引文（**文档事实**） |
| [[dps-pins-editor]] | **GUI 侧的对口**。`DFPS` 在 pin 配置的三层对照里对应 DPS Pins 表 | [[mapping-pin]] 主表第二行（**本页读过的 wiki 页**） |
| [[mapping-pin]] | **对照表页**（已建）。它从截图得出的参数顺序与本页的签名行**一致**；**它的「多 site 覆盖不到」那条缺口，本页也只能确认「语料未写」** | 那页的 ④ 档与收窄记（**本页读过的 wiki 页**） |
| [[dc-scale-xps256-card]] | **限制条件点名的卡之一**：`XPS256: Only channels on the same HLA can be ganged.` | 本篇参数表（**文档事实**） |
| [[dps128-dps64-cards]] | **限制条件点名的卡之一**：同卡内不跨卡、必须同 HC/HV、group 数上限 = channel 数一半 | 本篇参数表（**文档事实**） |
| [[dc-scale-uhc4t-card]] | **限制条件点名的卡之一**：UHC4/UHC4T 不许混组 | 本篇参数表（**文档事实**） |
| [[pin-configuration-file]] | **它落地的文件**。原文的 `## Application` 段写 `Configuration Setup`，并链到 `02.06.03_Pin_configuration_setup_commands`（那一章的标题）——**本页只见到这一句，没读那份文件文档** | 本篇 `## Application`（**文档事实**；文件本身的格式**本页未读**） |
| [[pin]] | **stage 页**。本页 `stage: pin` 填的是「**最近的一段**」（§6）：`DFPS` 是 pin 配置期的动作 | frontmatter 约定 |
| [[timing]] / [[level]] | **下游**：`DFPS` 绑好通道、给好极性之后，**电压值本身**在 level 侧填（原文那句 `The voltage supplied to the device will then be exactly as entered in the Level Setup` 就是这条交界线） | 本篇引文（**文档事实**） |
| [[xps256-programming-dps-operating-mode]] / [[xps256-pmu-operating-mode]] | **DC Scale 通道的两种用法**——**本页未读这两篇**，所以「DPS 模式与 PMU 模式在命令侧怎么切」本页没有 | 本页未读（**取材边界**） |

**一条本页要显式记的同形陷阱**：`DFPS` 的 `DPS` **不进文件**——
`DFPS 11,POS,(Vee)` 里那个 `11` 就等于 GUI 上 `Tester Channel` 列里写的 `DPS11`
（[[mapping-pin]] 的图证 + 本页 Example 1 的正文，两处一致）。
**照 GUI 上的字面把 `DPS11` 抄进文件是错的。**

## 版本

本文档**有** `## Functional changes` 段，段里**六条**（逐字）：

| 版本 | 条目（逐字） | 意思 |
|---|---|---|
| **在 6.3.2 之前就有了** | `Introduced before SmarTest 6.3.2` → [[smartest-6.3.2]] | **哨兵值**（§11.2 ②），**不是「6.3.2 新增」** |
| **SmarTest 6.5.0** → [[smartest-6.5.0]] | `DC Scale UHC4 card added.` | 加 **UHC4** 卡 |
| **SmarTest 7.3.1** → [[smartest-7.3.1]] | `DC Scale PVI8 card added.` | 加 **PVI8** 卡 |
| **SmarTest 7.3.2** → [[smartest-7.3.2]] | `DC Scale UHC4T card added.` | 加 **UHC4T** 卡 |
| **SmarTest 7.4.0** → [[smartest-7.4.0]] | `DC Scale AVI64 card added.` | 加 **AVI64** 卡 |
| **SmarTest 7.5.0** → [[smartest-7.5.0]] | `DC Scale FVI16 card added.` | 加 **FVI16** 卡 |

**六条里有五条是同一句话的重复模板**（`DC Scale <卡名> card added.`）
——读它读出来的不是「DFPS 改过五次」，是「**DC Scale 卡是一张一张加进来的，
每加一张就在 `DFPS` 的版本段里记一笔**」。**所以 `DFPS` 这个命令的版本史，就是 DC Scale 卡的型号史。**
（这是本页的读法，**推断**；依据是六条的措辞完全同构。）

> **⚠️ 版本段与正文对不齐，照实记**：
> 版本段点了**五张卡**（UHC4 / PVI8 / UHC4T / AVI64 / FVI16），
> 而正文的 ganging 限制表里**只出现了 UHC4、UHC4T、XPS256、DPS128/64**——
> **PVI8 / AVI64 / FVI16 三张卡在正文里一条限制都没写**
> （UHC4 也算半个：它只以「UHC4 / UHC4T」的合称出现）。
> **本页不替它补**：这三张卡的 ganging 规则、能不能 gang，**本篇没写**。

**版本段里没有的东西**：**没有一条说「`DFPS` 这个命令本身在哪一版出现」的条目**——
第一条是哨兵值。原文的 `Related information` 与正文也没有补。**所以「它从哪一版开始有」本篇答不了。**

## 出处

### `sources:` 列了一篇，但语料里这一篇有**两份投放**——本页核过了

| | 第一份（**本页的 source**） | 第二份 |
|---|---|---|
| 路径 | `02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md` | `02_System_reference/02.06_Command_Reference/02.06.03.02.09_DFPS__DFPS__-__DeFine_Power_Supply.md` |
| `source_topic`（frontmatter） | `98551.htm` | `98551_2.htm` |
| 章 | **字母序命令索引**（`02.06.02.02`） | **专题章**（`02.06.03.02`，也就是原文 `## Application` 段链到的 `Pin configuration setup commands`） |

**核法与本页的结论**：把两份的 frontmatter 剥掉之后逐字节比较——
**正文完全相同**（两份都是 **5,691 字节**，`sha256` 同为
`5515c417d483bd215aed8e2acf0a406ebdacd235305650f761a3eff89990f14b`）；
`diff` 出来的差异**只有 frontmatter 的那两行**（`source_topic` 与 `source_html`）。

> **所以：这是同一篇 TDC 页被投放了两次，不是两处独立证据。**
> 判据就是 §10 第 0 条：**`source_topic` 去掉 `_2` 后缀后相同 → 同一篇**。
> **本页不把它当成「两篇文档都说 X」**——那会凭空造出一个假冲突（§10 三个后果里的第 3 条）。
> **第二份只做了去重核对（哈希 + diff），没有当成第二篇来源读。**

- 本页引的每一句都来自**上面第一份**（也就是本页 `sources:` 里那一篇），**整篇读完**
  （208 行 / 5,886 字节）。
- 本页的「语法 / 参数」节与「报错条件」节都是脚本从这一篇逐字抽的（**本页一个字没动**）。

### 本页没做的

- **`DDIC` 那一篇没读**：本页只知道「跨卡 ganging 前必须 `DDIC` 使能」，**不知道 `DDIC` 自己的参数怎么填**
  （`CONN` 之外还有哪些取值、`GO`/`GI` 是什么的缩写）。→ **`GO` / `GI` 与五位通道号的换算关系，本页给不出来。**
- **`PALS` / `PSTE` 两篇没读**：本页只知道多 site 「归它们管」，**不知道怎么写**。
- **`DFPN` / `DFPC` / `DFPR` / `DFPT` / `DFGP` / `DFGE` 等 `DF` 族命令一篇没读**——
  本页只从 [[mapping-pin]] 的对照表知道 `DFPN` 是「给数字 channel 分配 pin 名与 pin 号」，
  **没有回命令原文核过**。
- **DC Scale 各卡那几篇（XPS256 / DPS128/64 / UHC4T / PVI8 / AVI64 / FVI16）一篇没读**：
  本页的卡限制**只来自 `DFPS` 自己的参数表**，那些卡自己的文档里可能还有条件。
- **pin 配置文件那一篇没读**：所以「`DFPS` 行在文件里的位置、和别的命令的先后」本页没有。
- **图**：**本篇（两份投放都一样）对 `raw/` 的引用 0 处**——实测 `.png` / `.jpg` / `.gif` /
  `!\[` / `<img` / `raw/` 六种写法全部 **0 命中**。**所以本页没有任何来自图的结论。**
  **本页用的图证是 [[mapping-pin]] 那一页读的（`105641.png` 等三张），不是本页读的**——
  那一条已经标成 ③ 档并注明了出处。
- **没有实跑。** 没在机台上配过 DPS channel、没 gang 过、没触发过上面七条报错里的任何一条。
  `verified: doc-only` 指的就是这件事。

### ⚠️ 本篇的六处语料瑕疵，本页照实记下、一处都没替它改（① 回上游 `.htm` 核过）

> ① **编码坏字两处，都在参数表里**（**也就是在「语法 / 参数」节里，本页一个字没动**）：
> `this is a three鈥慸igit or four鈥慸igit integer`——`鈥慸` 是 **`‑d`** 的坏字
> （`extract/encoding-map.csv` 第 12 行：`鈥慸` = `‑d`，其中 `‑` 是 U+2011 非断行连字符，
> **字母 `d` 被一起吃进了第二个坏字里**）。原文应是 `three‑digit` / `four‑digit`。
> **上游 `98551.htm` 里写的是干净的 `three‑digit`**（实测）——
> **所以这一处属 §11.2 ① 那族（HTML→md 转换坏的、将来重做转换能救回来）**，
> **不是 ⑤/⑥ 那族（上游就坏）**。**要搜它得搜坏掉的那个形态 `鈥慸igit`，拿 `three-digit` 去搜是搜不到的。**

> ② **`## Errors` 段里五条列表项以两个空格开头**（例如 `You define more than the number of installed DPS pins.` 前面是 `-` 加两个空格）。
> **原文如此**（本页照原样，它在「报错条件」节里）。

> ③ **参数表里有一个孤立的 `-` 单独占一行**（`dps_channel` 说明的末尾）。
> 那是 HTML 列表被压平时与内容拆散的痕迹——**该行的内容其实在下一段**
> （`For DC Scale channels (in DPS mode) this is a five digit number in the same format as for digital I/O channels.`）。**原文如此。**

> ④ **`DFPS` / `DFPS?` 的两行签名不在本页的「语法 / 参数」节里**：
> raw 把它们挂在 `## DFPS` / `## DFPS?` 两个**自定义段名**下，不是 `## Syntax`，
> 脚本的抽取口径只认 `## Syntax` / `## Parameters`。
> **本页在正文里逐字引了一次（没有改语法节）**——**语法节里有 `Parameters` 与五个 `Example`，唯独没有签名。**

> ⑤ **`DFPS` 的通道号（五位数）与 `DDIC` 的通道号（带 `GO`/`GI`）怎么换算，原文没说。**
> 例子把两者并排摆着（`DDIC CONN, (104GO, 105GI)` 对
> `DFPS (10403, 10404, 10501, 10502),POS,(vee)`），**但没有一个字解释这层对应**。
> **本页照原样引，不推换算规则。**

> ⑥ **参数表里 `pinlist` 写了 `@` 能读回全部，但没有任何一条 `DFPS?` 的例子。**
> **「怎么用它读回全部」本篇没给例子**——本页在「典型用法」里标成（推断）。

`verified: doc-only`
