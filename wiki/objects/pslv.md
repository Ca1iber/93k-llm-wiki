---
type: object
title: PSLV, PSLV? - (Power Supply LeVel)
layer: L1
stage: level
tags: [pslv, l1, firmware-command, level, dps, power-supply, fixed-levels, equation-based, impedance, sink-current, site-focus]
related: [level, dfps, dscp, dsus, pssr, psfc, site-focus-required-before-command, drlv, rclv, dpspins-resources]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PSLV, PSLV? - (Power Supply LeVel)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,767 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSLV

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

  Note If equation based testing is being used, you specify a DPS set ID instead of a DPS set number.  Note PSLV ALL only applies changes to all non-equation-based DPS sets.

### PSLV?

```
PSLV? {dps_No|dps_set_id}, {(pinlist)}
```

returns:

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

 Note PSLV? ALL returns information for non-equation-based DPS sets only.

### Parameters

Note The settling time parameter (setup_time) of the PSLV command and the rise_... and fall_... parameters of the `PSSR, PSSR? -(Power Supply Slew Rate)`（raw: `02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md`） command exclude each other. This also applies to the t_ms equation parameter (see `DPSPINS`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md`） and `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）).

| dps_No | Needed for non-equation-based setup. | Needed for non-equation-based setup. |
|---|---|---|
| dps_No | dps_No | The identification number of the DPS set which you want to modify. The number must not exceed the maximum number allowed (as defined by the DSCP (Define System Control Parameter) command. |
| dps_No | ALL | Modifies all the existing fixed DPS sets. |
| dps_No | PRM | Modifies the primary DPS set. |
| dps_No | ACT | (Only for PSLV?) Displays the settings of the actual enabled DPS set. |
| dps_set_id | Needed for equation-based setup.<br><br>This parameter is derived as follows:<br><br>`100000*equation_set_no + 1000*specset_no+1` | Needed for equation-based setup.<br><br>This parameter is derived as follows:<br><br>`100000*equation_set_no + 1000*specset_no+1` |
| voltage | The optional parameter voltage defines the output voltage (in V) of the DPS. Applicable value depends on the DPS type. | The optional parameter voltage defines the output voltage (in V) of the DPS. Applicable value depends on the DPS type. |
| source_current | The optional parameter defines the source current limit (ilimit_source) in [A]. The applicable value depends on the DPS type.<br><br>The parameter defines the source and the sink current limit if both values are equal.<br><br>The parameter defines only the source current limit if the sink_current parameter is used. | The optional parameter defines the source current limit (ilimit_source) in [A]. The applicable value depends on the DPS type.<br><br>The parameter defines the source and the sink current limit if both values are equal.<br><br>The parameter defines only the source current limit if the sink_current parameter is used. |
| sink_current | The extra parameter defines the sink current limit (ilimit_sink) in [A].<br><br>The parameter is required only if the source and sink current limits are set to different values. This parameter defines then the sink current limit while the source current limit is defined by the above source_current parameter.<br><br>The parameter is not required if the current limits are programmed symmetrically to the same (absolute) value. Both, the source and the sink value are then defined by the source_current parameter.<br><br>The query answer shows the sink_current parameter only if the programmed sink current limit is not symmetrical to the source current limit. | The extra parameter defines the sink current limit (ilimit_sink) in [A].<br><br>The parameter is required only if the source and sink current limits are set to different values. This parameter defines then the sink current limit while the source current limit is defined by the above source_current parameter.<br><br>The parameter is not required if the current limits are programmed symmetrically to the same (absolute) value. Both, the source and the sink value are then defined by the source_current parameter.<br><br>The query answer shows the sink_current parameter only if the programmed sink current limit is not symmetrical to the source current limit. |
| impedance | The optional parameter sets the DPS output impedance. You can select:<br><br>- LOZ sets the DPS output impedance to low when the test system is in the disconnect state. The current limit remains at the same level as in the active state, while the force voltage is set to 0 V.<br>- HIZ sets the DPS output to high impedance when the test system is in the disconnect state. This sets the channel to the minimum possible current limit. HIZ is the default state for DPS-slot types. If it is applied to DC Scale cards, HIZ_R is used instead of HIZ.<br>- HIZ_R sets the DPS output to high impedance by switching the output relay off when the test system is in the disconnect state.<br><br>Note that relay switching is slower than with HIZ.<br><br>- LOZ_HIZ combines LOZ with HIZ. First, the DPS is switched to 0 V with an unchanged current limit (just like in LOZ mode). After the output voltage has reached 0 V (±50 mV) or after a timeout of 1 second, the DPS pin is switched to high impedance. This combines the advantages of both modes. A capacitor on the load board is quickly discharged and then the DPS pin is switched to high impedance. This is safer when changing the DUT or DUT board after a disconnect.<br>- LOZ_HIZ_R combines LOZ with HIZ_R. First, the DPS is switched to 0 V with an unchanged current limit (just like in LOZ mode). After the output voltage has reached 0 V (±50mV) or after a timeout of 1 second, the DPS pin is switched to open. This combines the advantages of both modes. A capacitor on the DUT board is quickly discharged and then the DPS pin is switched to high impedance. This is safer when changing the DUT or the DUT board after a disconnect. | The optional parameter sets the DPS output impedance. You can select:<br><br>- LOZ sets the DPS output impedance to low when the test system is in the disconnect state. The current limit remains at the same level as in the active state, while the force voltage is set to 0 V.<br>- HIZ sets the DPS output to high impedance when the test system is in the disconnect state. This sets the channel to the minimum possible current limit. HIZ is the default state for DPS-slot types. If it is applied to DC Scale cards, HIZ_R is used instead of HIZ.<br>- HIZ_R sets the DPS output to high impedance by switching the output relay off when the test system is in the disconnect state.<br><br>Note that relay switching is slower than with HIZ.<br><br>- LOZ_HIZ combines LOZ with HIZ. First, the DPS is switched to 0 V with an unchanged current limit (just like in LOZ mode). After the output voltage has reached 0 V (±50 mV) or after a timeout of 1 second, the DPS pin is switched to high impedance. This combines the advantages of both modes. A capacitor on the load board is quickly discharged and then the DPS pin is switched to high impedance. This is safer when changing the DUT or DUT board after a disconnect.<br>- LOZ_HIZ_R combines LOZ with HIZ_R. First, the DPS is switched to 0 V with an unchanged current limit (just like in LOZ mode). After the output voltage has reached 0 V (±50mV) or after a timeout of 1 second, the DPS pin is switched to open. This combines the advantages of both modes. A capacitor on the DUT board is quickly discharged and then the DPS pin is switched to high impedance. This is safer when changing the DUT or the DUT board after a disconnect. |
| setup_time | The optional parameter is an integer which specifies the settling time (in ms) of the DPS. All DPS's are synchronized so that they finish their settling periods at the same point in time. This is the point when the system is switched to the connect state. If there are, for example, two DPS's, one with a settling time of 10 ms, and the other with a settling time of 4 ms, then the second DPS will be started 6 ms after the first:<br><br>!`Synchronizing Different DPS Settling Times`（raw: `../../../../raw/93235.png`）<br><br>The range is from -2147483647 up to 2147483646 ms.<br><br>The default value is 0.Note setup_time has a resolution of ms (floating point values are rounded to nearest integer). | The optional parameter is an integer which specifies the settling time (in ms) of the DPS. All DPS's are synchronized so that they finish their settling periods at the same point in time. This is the point when the system is switched to the connect state. If there are, for example, two DPS's, one with a settling time of 10 ms, and the other with a settling time of 4 ms, then the second DPS will be started 6 ms after the first:<br><br>!`Synchronizing Different DPS Settling Times`（raw: `../../../../raw/93235.png`）<br><br>The range is from -2147483647 up to 2147483646 ms.<br><br>The default value is 0.Note setup_time has a resolution of ms (floating point values are rounded to nearest integer). |
| pinlist | pinlist must contain the names of pins previously defined by the `DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） command. If more than one pin is specified, the names must be separated by commas. The character @ can be used to set the levels for all DPS pins. | pinlist must contain the names of pins previously defined by the `DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） command. If more than one pin is specified, the names must be separated by commas. The character @ can be used to set the levels for all DPS pins. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/98702.htm`。

### Example

```
PSLV 1,5.2,0.5,HIZ,15,(Vee)
```

This example sets the following parameters for device pin Vee:

- DPS set 1
- A voltage of 5.2 V
- A current limit of 0.5 A
- Minimum current limit when the test system is disconnected
- A setup time of 15 ms

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The DPS set number is out of range.
- The programmed voltage is out of range.
- The programmed current is out of range.
- A communication error with the DPS occurs.
- The programmed voltage reaches the overvoltage limit.

<!-- 报错节 end -->

## 是什么

**`PSLV` 是 fixed（非方程）路线上的 DPS 设定命令：给 `DFPS` 定义过的电源通道设电压、电流限、断连阻抗与建立时间。**
原文第一句就把**它和 `DFPS` 的先后关系**写死了：

> 「The PSLV (Power Supply LeVel) command allows you to make DPS settings for channels previously defined by the DFPS command. The PSLV? query returns the existing settings.」

**`PSLV` 写、`PSLV?` 读，两个方向各一条命令。**
「有哪几个位」在「语法 / 参数」节（脚本逐字抽的）；
这一节讲**原文正文里有、语法节抽不到**的几条语义。

### 六个位：**单位不是一个系的**

| 位 | 参数 | 单位 | 原文要点 |
|---|---|---|---|
| 1 | `dps_No` / `dps_set_id` | — | 两套寻址，见下 |
| 2 | `voltage` | **V** | `The optional parameter voltage defines the output voltage (in V) of the DPS.` |
| 3 | `source_current` | **A** | `ilimit_source` |
| 4 | `sink_current` | **A** | `ilimit_sink`；**源、汲限对称时不给**（见下） |
| 5 | `impedance` | — | 五种模式（见下） |
| 6 | `setup_time` | **ms** | 整数；范围与默认值见下 |

> **⚠️ 一条单位陷阱：`voltage` 是 V，而 [[drlv]] / [[rclv]] 的电平参数是 mV。**
> 同一份 level 设置里两种单位并存——本篇例子里写 `5.2` 是 5.2 V，
> [[drlv]] 例子里写 `-1750` 是 -1750 mV。**差三个量级，填错不是小错。**

### 寻址：两套编号 + 三个关键字

| 写什么 | 用在哪条路线 | 原文要点 |
|---|---|---|
| `dps_No` | **非**方程路线 | `Needed for non-equation-based setup.`；上限由 `DSCP` 定 |
| `dps_set_id` | 方程路线 | `Needed for equation-based setup.`；`100000*equation_set_no + 1000*specset_no+1` |
| `ALL` | 两条都有 | `Modifies all the existing fixed DPS sets.`——**只动 non-equation-based 的 set** |
| `PRM` | 两条都有 | `Modifies the primary DPS set.` |
| `ACT` | **只有 `PSLV?`** | `(Only for PSLV?) Displays the settings of the actual enabled DPS set.` |

两条 Note 逐字（一条在语法行下，一条在 `PSLV?` 节里）：

> 「If equation based testing is being used, you specify a DPS set ID instead of a DPS set number.  Note PSLV ALL only applies changes to all non-equation-based DPS sets.」

> 「 Note PSLV? ALL returns information for non-equation-based DPS sets only.」

**`ALL` 的排除规则对写和读同时成立**——写只改非方程 set，读也只报非方程 set。

**另外注意 `dps_set_id` 的公式末项**：DPS 固定 `+1`，
而 [[drlv]] / [[rclv]] 的 `level_set_id` 是 `+ level_set_no`。
**两条编号是分开的**（同一个 equation set + specset 下，level set 按 `level_set_no` 编，DPS 固定取 1）。

### 「立刻生效」**只对 primary DPS set 成立**

> 「If this command is applied to the primary DPS set, the settings specified with this command will be activated on the hardware immediately.」

**这是 `PSLV` 与 [[drlv]] 的一个重要差别。** `DRLV` 那边原文写的是
「**每次调用都需要激活 level set**」；`PSLV` 这边明写 primary 是**立即**落到硬件。
**非 primary 的 set 生效与否，本篇没有写**（见「出处」）。

### `sink_current`：省不省，看对称不对称

原文给了四条规则，**读成一张表**：

| 情形 | 要写几个电流值 | 结果 |
|---|---|---|
| 源限与汲限**相同** | 只给 `source_current` | 它**同时**定义源限与汲限 |
| 源限与汲限**不同** | `source_current` + `sink_current` | `source_current` 只定义源限，汲限由 `sink_current` 给 |
| **查询**时两者对称 | — | 回读里**不出现** `sink_current` |
| **查询**时两者不对称 | — | 回读里**出现** `sink_current` |

逐字三条：

> 「The parameter defines the source and the sink current limit if both values are equal.」

> 「The parameter defines only the source current limit if the sink_current parameter is used.」

> 「The query answer shows the sink_current parameter only if the programmed sink current limit is not symmetrical to the source current limit.」

**一句话记法：对称就一个值，不对称就两个值，回读只在不对称时才把第二个吐回来。**

### `impedance`：五种模式，说的**全是「断开时怎么办」**

**五种取值都只在 `the disconnect state`（系统断开态）下起作用**——
它们不是「现在怎么输出」，而是「断连那一刻这个 DPS 变成什么」。

| 取值 | 断开时做什么 | 原文补充 |
|---|---|---|
| `LOZ` | 阻抗拉到低；**电流限保持 active 态那一个**，force voltage 设成 0 V | `The current limit remains at the same level as in the active state, while the force voltage is set to 0 V.` |
| `HIZ` | 拉到高阻；**通道被设成最小可能的电流限** | **`HIZ is the default state for DPS-slot types.`**；**加在 DC Scale 卡上时实际走的是 `HIZ_R`** |
| `HIZ_R` | **断开输出继电器**来实现高阻 | `Note that relay switching is slower than with HIZ.` |
| `LOZ_HIZ` | 先 `LOZ`（0 V、电流限不变），电压到 0 V（**卤50 mV**）**或**超时 1 秒后 → 再切高阻抗 | 电容被快速放电，**换 DUT 或 DUT board 时更安全** |
| `LOZ_HIZ_R` | 同 `LOZ_HIZ`，但最后**切到 open** | 原文写的是 `switched to open` |

**`HIZ` 与 `HIZ_R` 不是偏好问题，是卡种问题**，逐字：

> 「HIZ is the default state for DPS-slot types. If it is applied to DC Scale cards, HIZ_R is used instead of HIZ.」

**即：同一个 `HIZ` 写在命令里，落到 DC Scale 卡上时执行的是 `HIZ_R`。**
（`卤50 mV` 里的 `卤` 是语料坏字，应为 `±`，见「出处」⚠️ ③。**本页照原样引。**）

### `setup_time`：**所有 DPS 的建立期同步在同一个时刻结束**

> 「The optional parameter is an integer which specifies the settling time (in ms) of the DPS. All DPS's are synchronized so that they finish their settling periods at the same point in time. This is the point when the system is switched to the connect state.」

**各自可以设不同的时间，但结束时刻被对齐到「系统切到 connect 态」那一点。**
原文紧接着给了一个两 DPS 的算例：

> 「If there are, for example, two DPS's, one with a settling time of 10 ms, and the other with a settling time of 4 ms, then the second DPS will be started 6 ms after the first:」

| 项 | 值（原文） |
|---|---|
| 范围 | `The range is from -2147483647 up to 2147483646 ms.` |
| 默认 | `0` |
| 分辨率 | **ms**；`floating point values are rounded to nearest integer` |

**这个算例后面挂着一张图**（`Synchronizing Different DPS Settling Times`，`raw/93235.png`），
**本页没看那张图**（见「出处」）。

### 一条互斥：`setup_time` ↔ `PSSR` 的 rise/fall 与方程里的 `t_ms`

`## Parameters` 一节开头的 Note 逐字：

> 「The settling time parameter (setup_time) of the PSLV command and the rise_... and fall_... parameters of the PSSR, PSSR? -(Power Supply Slew Rate) command exclude each other. This also applies to the t_ms equation parameter」

**`setup_time` 有两个对头**：`PSSR`（[[pssr]]）的 `rise_` / `fall_` 参数，
**以及方程路线里的 `t_ms`**。`t_ms` 在 `DPSPINS` / `DPSPINS resources` 那两篇里
（`DPSPINS` 未建、也不在 allowlist 里；[[dpspins-resources]] 有页）。

### 两段 site 相关的标准段落

原文同一位置有两段**在所有站点焦点命令里都出现**的话：

> 「With this command you configure setups of those sites that have the setup focus:」

> 「With this command you can retrieve site specific information (only one site can be in focus at a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**要紧的是括号里那半句**：**同一时刻只有一个 site 在焦点里**——
所以 `PSLV?` 在多 site 下**只能逐 site 轮着查**，拿不到「一次全给」。
这条前因后果见 [[site-focus-required-before-command]]。

## 典型用法

**1. 顺序：`DFPS` 在前，`PSLV` 在后。** 前置写死在 `pinlist` 的说明里：

> 「pinlist must contain the names of pins previously defined by the DFPS command.」

即：DPS pin 先在 [[dfps]] 里定义出来，`PSLV` 才认得出它。

**2. 完整例子**（原文 `## Example`，也是本篇唯一一个例子）：

```
PSLV 1,5.2,0.5,HIZ,15,(Vee)
```

原文对自己这个例子的逐条解释（**列表符是原文的一部分**）：

> 「This example sets the following parameters for device pin Vee:」

> 「- DPS set 1」

> 「- A voltage of 5.2 V」

> 「- A current limit of 0.5 A」

> 「- Minimum current limit when the test system is disconnected」

> 「- A setup time of 15 ms」

**照位置对回去**：`1` = `dps_No`、`5.2` = `voltage`（V）、`0.5` = `source_current`（A）、
`HIZ` = `impedance`、`15` = `setup_time`（ms）。
**`sink_current` 没给**——这正好用上「源汲对称就省掉」那条规则（0.5 A 两边一样）。

> 原文对 `HIZ` 的那句解释是 `Minimum current limit when the test system is disconnected`，
> 与 `HIZ` 的定义句（`This sets the channel to the minimum possible current limit.`）**对得上**。

**3. 读回**：`PSLV? {dps_No|dps_set_id}, {(pinlist)}`。

| 想知道什么 | 写什么 |
|---|---|
| **当前真正生效**的那个 set 的设置 | `PSLV? ACT, ...` |
| 某一个 set 的设置 | `PSLV? {dps_No\|dps_set_id}, (pinlist)` |
| **全部** set 的设置 | `PSLV? ALL, ...`——**只有非方程的那些会被报出来** |

**4. 出错时的五种情况**在下面的「报错条件」节（脚本从原文 `## Errors` 逐字取）。
本页不重复那五条，只提醒一句：**其中一条是通信错误**
（`A communication error with the DPS occurs.`）——**参数填得再对也可能报它。**

**5. 归属**：原文 `## Application` 一节全文只有一句——
`Level Setup, see Level Setup Commands.`
（`Level Setup Commands` 那篇本页没读。）

## 和谁有关

- [[level]] — **`stage: level` 指的是「最近的一段」，不是归属**（§6）。
  依据是原文 `## Application` 那唯一一句 `Level Setup, see Level Setup Commands.`
- [[dfps]] — **上游 / 前置**：`pinlist` 里的 pin 必须是它定义过的 DPS pin。
  `PSLV` 回答的是「定义完之后设什么值」。
- [[dscp]] — **上游 / 上限的定义方**：`dps_No` 的允许范围由 `DSCP` 给出。
- [[dsus]] — **同类、作用面不同**：`DSUS` 设「**有几个** DPS set」，
  `PSLV` 设「**某一个 set 里是什么**」。两者同属 level setup 那一章。
- [[pssr]] — **互斥**：`PSLV` 的 `setup_time` 与 `PSSR` 的 `rise_...` / `fall_...` 不能同时用，
  与方程里的 `t_ms` 也不能。
- [[psfc]] — **另一条前置**：本命令只配置 `setup focus` 里的 site，焦点由 `PSFC` 设；
  **这条前置踩错的后果见 [[site-focus-required-before-command]]。**
- [[drlv]] / [[rclv]] — **同批同族**：都是 fixed 路线的 level 命令。
  `DRLV` 管驱动电平、`RCLV` 管比较阈值、`PSLV` 管 DPS 供电。
  **三条命令的 `## Application` 指向同一篇章首页**；`PSLV` 与另外两条的差别是
  **单位（V / A / ms 对 mV）**与**「primary 立即生效」**这两条。
- `DPSPINS`（**未建、且不在 allowlist 里**）与 [[dpspins-resources]] ——
  方程路线的 DPS 模块；`t_ms` 在那里，**它与 `setup_time` 互斥**。**两篇本页都没读。**
- `Level Setup Commands`（**未建、且不在 allowlist 里**）—— 章首页，原文指定的应用出处。

## 版本

本文档**有** `## Functional changes` 段，四条，**逐字**：

| 条目 | 和正文对得上吗 |
|---|---|
| `Introduced before SmarTest 6.3.2` | **是 §11.2 ② 的哨兵值**，见下① |
| `SmarTest 6.5.3: Excluding dependency with PSSR command.` | 对应正文那条互斥 Note，**但措辞不同**，见下② |
| `SmarTest 7.1.3: Additional impedance modes: LOZ_HIZ and LOZ_HIZ_R` | **对得上**：这两种模式在正文的 `impedance` 列表里 |
| `SmarTest 7.2.0: New parameter: sink_current` | **对得上**：`sink_current` 是正文的一个参数 |

**① `Introduced before SmarTest 6.3.2` 不是「6.3.2 的变更」。** 按 §11.2 ②，
它是「**早于本文档集覆盖范围**」的哨兵——**所以 `PSLV` 到底成立于哪个版本，这份语料里没有。**

**② 6.5.3 那条与正文措辞不一致，本页并列，不替它们调和。**
版本段写 `Excluding dependency with PSSR command.`（**解除**某种依赖），
正文 Note 写的是两者 `exclude each other`（**互相排斥**）。
`excluding dependency` 与 `exclude each other` **不是一件事**，
**原文没说这两句在讲同一个改动。**

**③ 与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
而这一篇的版本段**停在 7.2.0**——**7.2.0 之后 `PSLV` 有没有变，语料里没有。**
`LOZ_HIZ` / `LOZ_HIZ_R` / `sink_current` 在 7.10.3 上**有**（正文写着），
但这是**文档事实**，不是「这台机器上能用」（§11）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVeL.md`

**本页没做的：**

- **一张图没看。** 原文 `setup_time` 那格挂着
  `Synchronizing Different DPS Settling Times`（`raw/93235.png`）——
  「各 DPS 结束时刻对齐」本页**只有文字，图里的时序没看**。
- **`Level Setup Commands`（`02.06.05`）那篇章首页没读** ——
  所以 `## Application` 那一句指向的是什么内容面，本页不知道。
- **`DFPS` 没读** —— 所以 DPS pin 是怎么定义出来的、`@` 之外还有哪些写法，本页没有。
- **`DSCP` 没读** —— 所以 `dps_No` 的上限**具体是多少**（默认值与最大值）本页不知道；
  本页只有「上限由 `DSCP` 定」这一句。
- **`PSSR` 没读** —— 那条互斥的另一半（`rise_` / `fall_` 参数长什么样）**本页一个字都没有**。
- **`DPSPINS` 与 `DPSPINS resources` 都没读** —— 方程路线的 DPS 模块、
  以及 `t_ms` 与 `setup_time` 具体怎么冲突，本页只有那句 Note。
- **`PSFC` 没读** —— 「怎么设焦点」本页不知道，只有「本命令受焦点影响」。
- **没在真实机台上跑过任何一条 `PSLV`**（`verified: doc-only`）——
  §11：**文档里有 ≠ 这台机器上能用**。尤其那五种 `impedance` 在具体卡上走哪条路
  （`HIZ` 还是 `HIZ_R`），**要照现场卡种看**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 一个括号不配对。** 逐字：
> `The number must not exceed the maximum number allowed (as defined by the DSCP (Define System Control Parameter) command.`
> ——**两个左括号、一个右括号**，`(Define System Control Parameter)` 没有闭合。
>
> **② `dps_No` 在参数表里出现两次，同名两行。** 逐字（第一行只给一句）：
> ```
> dps_No
>
>  |
>
> Needed for non-equation-based setup.
> ```
> 紧接着又是 `dps_No` 一行，说明写的是
> `The identification number of the DPS set which you want to modify.`
> ——**同一个参数名占了两个条目，两条内容还不重复**（一条讲「什么时候要写」，
> 一条讲「它是什么」）。**本页照实并列，不替它合并。**
>
> **③ `±` 被读成了 `卤`，而且同一段里两种写法。** 逐字：
> `After the output voltage has reached 0 V (卤50 mV) or after a timeout of 1 second`
> 与 `After the output voltage has reached 0 V (卤50mV) or after a timeout of 1 second`
> ——`卤` 是 `±`（§11.2 ① 的确定映射），**一处 `50 mV`、一处 `50mV`，空格不一致**。
>
> **④ 一句话被两个 `Note` 粘住了。** 逐字：
> ` The default value is 0.Note setup_time has a resolution of ms (floating point values are rounded to nearest integer).`
> ——**`0.` 与 `Note` 之间没有任何分隔符**（同篇另一处的 `Note` 是正常起句的，
> 形如 ` Note The settling time parameter...`）。
>
> **⑤ 表格里有一行的分行方式与全表不同。** 其余每个参数都是「名字 / 空行 / 竖线 / 值」，
> **只有 `sink_current` 那行把竖线写在名字同一行**，逐字：
> ```
>  | sink_current |
> ```
> ——**这就是「语法 / 参数」节里那行孤零零的 `| sink_current |` 的来源。**
> **本页照实说，不替它改版式。**
>
> **⑥ 同一批 set 在正文里有两个名字：`non-equation-based` 与 `fixed`。** 逐字三条：
> `Needed for non-equation-based setup.`（`dps_No` 那一格）
> / `Modifies all the existing fixed DPS sets.`（`ALL` 那一格）
> / `PSLV ALL only applies changes to all non-equation-based DPS sets.`（语法行下的 Note）
> ——**说的是同一批 set，措辞在两句之间来回换。**
>
> **⑦ 同篇引 `PSSR` 时，连字符的空格与自己的标题不一致。** 本篇标题逐字是
> `PSLV, PSLV? - (Power Supply LeVeL)`（`-` 两边都有空格），
> 正文引的那篇写成 `PSSR, PSSR? -(Power Supply Slew Rate)`（`-` 后没有空格）；
> **文件名也是后一种形态**（`..._PSSR__PSSR__-_Power_Supply_Slew_Rate.md`）。
>
> **⑧ `## Related information` 三个链接粘在一起，中间没有分隔符。** 逐字：
> ```
> [DPSPINS](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md>)[DPSPINS resources](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md>)[PSSR, PSSR? -(Power Supply Slew Rate)](<02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md>)
> ```
> ——**三个链接名首尾相接**，不带分隔读起来是一条长名字。
>
> **⑨ 本篇没有 `## Warnings` 段**（只有 `## Errors`）。
> 脚本的报错节抬头写的是 `## Errors` / `## Warnings` 两个段名，
> **对本篇来说 `## Warnings` 是空的**（对照 [[drlv]] 与 [[rclv]]，那两篇有）。
>
> **⑩ `## Parameters` 那张表的第一个格子是一个孤立的 ` | `**，逐字：
> ```
>  |
>
> dps_No
> ```
> ——**表头位置只有一个竖线**，`dps_No` 是第一格的名字。
> **「语法 / 参数」节里那个孤立的 ` | ` 就是它。本页照实说。**
>
> **⑪ 同一个名字，标题一个写法、正文另一个写法。** 逐字：
> 标题（`title:` 与 H1）是 `PSLV, PSLV? - (Power Supply LeVeL)`（末位**大写 `L`**），
> 而正文第一句是 `The PSLV (Power Supply LeVel) command allows you to make DPS settings…`
> （末位**小写 `l`**）。
> **本页两处引文各照各的**——引标题写 `LeVeL`，引正文写 `LeVel`，**没有替它统一**（§11.2）。
> 这不是笔误造成的分歧，是原厂同一篇里就两种写法。

`verified: doc-only`
