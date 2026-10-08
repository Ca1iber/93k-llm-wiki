---
type: object
title: ETDS, ETDS? - (Edge Timing Definition String)
layer: L1
stage: timing
tags: [timing, edge-timing, etds, l1-command, firmware-command, fast-pin, pin-scale, delta-mode]
related: [etim, wsus, tsus, pdiv, dfgp, psfc, wfds, bwds, timing-setup-commands, waveform-set, timing]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# ETDS, ETDS? - (Edge Timing Definition String)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,724 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### ETDS

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### ETDS?

ETDS? {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {(pinlist)}

returns:

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### Parameters

| waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query, you can also enter ALL for all waveform sets. |
|---|---|
| specset_id | Derived as follows:<br><br>`100 *`equation_set_no `+ `specset_no |
| multi-port_spec | For a multi-port setup, specify the name of a multi-port specification.<br><br>Note that the multi-port specification uniquely determines an equation set for every pin of pinlist, because no pin can belong to more than one port within a multi-port specification. |
| timing_set | Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by TSUS. |
| mode | The operating mode. For the query, you can enter ALL for all modes or BIDIR for bidirectional mode, that is, for edges that serve both as drive and receive edges.<br><br>With fast pins, you can specify the mode DELTA for both the command and the query. In this mode, the delays specified for edges with an index > 1 are interpreted as offsets from the calculated default values. |
| definition_string | The definition string consists of a sequence of items each of which associates a delay with a drive or compare edge. On Pin Scale 800/3600 boards, drive edges are denoted by dn. On Pin Scale 9G boards, there are two kinds of drive edges, which are denoted by fn and sn, respectively; for details see `Defining waveforms for Pin Scale 9G pins`（raw: `02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`）. You can also use the dn notation for Pin Scale 9G channels, but mixing both notations in one string is not allowed. Receive edges are always denoted by rn.<br><br>Unless you employ the pdiv statement for fast pins (see below), all edges which are not explicitly set remain unchanged.<br><br>The range of the edge delay is -8000 ns to +24000 ns (or -4 to +12 test system periods) for the Pin Scale 3600/800.<br><br>On Pin Scale 800/3600 boards, the restrictions for edge ordering must be observed both in fixed and equation based timing. For example, you cannot assign a greater delay to d1 than to d3 if d1 precedes d3 in a waveform definition. For more information, see `Selecting and ordering edges`（raw: `02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）.<br><br>Note that with equation based timing, ETDS returns no error message when the edge order restrictions are violated.<br><br>On Pin Scale 9G boards, ordering of drive edges is not restricted in any way. |
|  | Special Rules for Fast Pins:<br><br>If a pin is configured as a fast pin in the context of the specification given by the first parameter, you can specify the period divider at the start of the definition string. The format is pdiv:n, where n must be the same value as the period_div value of the pins in pinlist within the timing set specified by the timing_set parameter.<br><br>If you specify pdiv:nand a delay for the first edge, ETDS calculates delays for the following n-1 edges except those that are specified explicitly in the string. Note that for n = 3, the edges with index 1, 3, 5 are used for internal reasons.<br><br>If you omit either pdiv or the first edge, only the specified edges are modified. However, with receive edges this is only possible for r1.<br><br>The calculated delays are determined for the ith edge by the following formula:<br><br>1st_edge_delay + (i-1) * (period/pdiv)<br><br>1st_edge_delay is the delay specified for the first edge (d1 or r1; the generic notation e1 is not allowed for fast pins). If the first edge is not specified in the string, its delay is set to 0. An example for the calculation will be given below.<br><br>Note that when both the period divider and a delay for the first edge are present in the definition string, then the delays for all the edges required by the period divider will be overwritten.<br><br>When a delay is explicitly specified for one of the edges, this delay overrides the calculated default. There are two formats to specify overrides. You can either define absolute delays or the offsets from the default delays.<br><br>If you want to use the second, relative format, you must specify DELTA for the modeparameter. Note that you can also specify negative offsets in the DELTA mode. |
| pinlist | The name of the pin or pins for which edge delays are to be set or read back. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.<br><br>In a multi-port setup, every pin must belong to a port of the specified specification. |

### Example 1

```
> ETDS 1,1,,"e1:0 e2:2 e3:6 e4:4",(io)
> ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
> ETDS? 1,1,,(@)
< ETDS 1,1,,"d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4",(io)
< ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
```

### Example 2

The following example shows the various possibilities for using ETDS with fast pins:

```
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5 d3:10 d4:15",(CP)
> ETDS 401,1,,"d2:5.5",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5.5 d3:10 d4:15",(CP)
> ETDS 401,1,,"pdiv:4 d1:3 d3:14",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:14 d4:18",(CP)
> ETDS 401,1,DELTA,"d3:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:12 d4:18",(CP)
> ETDS 401,1,DELTA,"pdiv:4 d1:0 d2:1 d4:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:6 d3:10 d4:14",(CP)
```

Note in particular the effect of the first instance of the command in DELTA mode. The negative offset is not applied to the actual value of d3, which is 14, but to the calculated default value, which is 13.

### Example 3

This example shows how to set and retrieve a delay of a multi-port specification:

```
> ETDS? "mu_timing",2,,(In1)
< ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ETDS "mu_timing",2,,"d1:0.5",(In1)
> ETDS? "mu_timing",2,,(In1)
< ETDS "mu_timing",2,,"d1:0.5",(In1)
```

The specification name and the pin name identify the port (no pin may occur in more than one port within the same specification). Then the port and the specification identify the equation set.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）command.
- timing_set is greater than the range allowed by the `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）command.
- The selected primary timing set is not defined for the specified waveform set.
- The edge order is wrong; for instance a window open must come before a window close - a mismatch exists between edge delays of the selected timing set and the waveform definition - `WFDS, WFDS? - (WaveForm Definition String)`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）, or the break waveform definition - `BWDS, BWDS? - (Break Waveform Definition String)`（raw: `02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md`）.
-  Eplacement is outside the allowed range.
-  All edges of the same direction in the specified timing set do not lie within one period.

<!-- 报错节 end -->

## 是什么

**ETDS 改的是「每条 edge 落在周期的哪一刻」——一个 timing set 里、选定的那些 pin 上的一组 edge delay。**
它**不管有几个 edge、也不管波形长什么样**。原文第一句：

> 「The ETDS(Edge Timing Definition String) command defines or modifies the edge delays for a timing set and selected pins within an already existing waveform set/specification.」

**`already existing` 是前提**：waveform set / specification **得先存在**（那是 `WSUS` 那边的事），
**ETDS 不建它**。

回读那一半只回**一部分**：

> 「The ETDS? query returns the current values, but only for those edges that are used in the wavetables of the specified waveform set/specification or have a value different from 0.」

**两个条件满足任一个才回**：① 这条 edge 在该 waveform set 的 **wavetable 里被用到**；
② 或者它的值**不等于 0**。
**所以「回读结果里没有某条 edge」≠「那条 edge 没被设置过」**——它也可能只是 0。
**这是本页最实用的一条读法。**

### 它替代 ETIM（**两篇的版本号对不上**）

> 「This command supersedes the command ETIMfrom release 2.0 for waveforms with more than 6 edges.」

**原文里 `ETIMfrom` 之间没有空格**（见「出处」⚠️①）。
**而 [[etim]] 那一篇写的是 `release 2.1`、条件是 `14-edge setups`** ——
**同一个替代关系，两篇给的版本号与范围都不一样**（见「和谁有关」与「出处」⚠️②）。

### 三条行为规则（`## Mode of operation`，逐字）

> 「The edge delays need not be defined for all edges. Missing delays are supplied by the system from a data base. Any delays not previously set default to 0.0 ns. No auto-corrections are performed, invalid values are rejected.」

| 规则 | 原文 |
|---|---|
| **不必把每条 edge 都写了** | `The edge delays need not be defined for all edges.` |
| **缺的由系统从数据库补** | `Missing delays are supplied by the system from a data base.` |
| **没设过的默认 `0.0 ns`** | `Any delays not previously set default to 0.0 ns.` |
| **不做 auto-correction；非法值直接拒** | `No auto-corrections are performed, invalid values are rejected.` |

**最后一条要单独记**：**ETDS 不会替你改正值**——不合法的值不是被修正，是**被拒绝**。
（本页只保证本篇这么写。**同族的 [[pclk]] 在这一点上的口径与本篇不同**——
**那一篇不在本页的 `sources:` 里**，要对比请去 [[pclk]] 那一页看。）

equation based 场合另有一条：

> 「In connection with equation based timing, note that ETDS only changes the runtime values, not the setup values specified in the timing set.」

**即：equation based 下 ETDS 只改 runtime 值，timing set 里的 setup 值不动。**
**本页只记本篇这一句**；**[[pclk]] 不在本页的 `sources:` 里**，
那一侧的口径请去 [[pclk]] 看，本页不为它背书。

### 什么时候生效：`## Postdependencies`（一节只有一句）

> 「After executing the command, the primary sets are reactivated with the new values at the start of the next functional test.」

**不在命令执行的那一刻生效，而是「下一次 functional test 开始时」**，
而且**被重新激活的是 primary sets**。**写完之后立刻回读会看到新值、但被测信号还没变**——
**这个时间差是本篇唯一交代「什么时候真的用上」的地方。**

### `definition_string`：edge 的记法、范围与顺序

**记法按板型分**（原文逐字）：

> 「On Pin Scale 800/3600 boards, drive edges are denoted by dn. On Pin Scale 9G boards, there are two kinds of drive edges, which are denoted by fn and sn, respectively; for details see Defining waveforms for Pin Scale 9G pins. You can also use the dn notation for Pin Scale 9G channels, but mixing both notations in one string is not allowed. Receive edges are always denoted by rn.」

| 板型 | drive edge | receive edge |
|---|---|---|
| **Pin Scale 800/3600** | `dn`（`d1`、`d2` 等） | `rn`（`r1`、`r2` 等） |
| **Pin Scale 9G** | **两种**：`fn` 与 `sn` | 同 `rn` |
| **Pin Scale 9G（也可）** | `dn` 记法**也能用**，但**同一个字符串里两种记法不许混** | — |

**未点名者的命运**：

> 「Unless you employ the pdiv statement for fast pins (see below), all edges which are not explicitly set remain unchanged.」

**范围**（只给了 800/3600）：

> 「The range of the edge delay is -8000 ns to +24000 ns (or -4 to +12 test system periods) for the Pin Scale 3600/800.」

**延迟可以是负数**——`-8000 ns` 到 `+24000 ns`。
**Pin Scale 9G 的范围本篇没写（语料未写）。**

**顺序限制**，以及**一处不报错的例外**：

> 「On Pin Scale 800/3600 boards, the restrictions for edge ordering must be observed both in fixed and equation based timing. For example, you cannot assign a greater delay to d1 than to d3 if d1 precedes d3 in a waveform definition.」

> 「Note that with equation based timing, ETDS returns no error message when the edge order restrictions are violated.」

> 「On Pin Scale 9G boards, ordering of drive edges is not restricted in any way.」

**三句话合起来是一条警告**：**800/3600 上顺序必须对，而且 fixed 与 equation based 都要**；
**但 equation based 下顺序错了不报错**。
**所以「没报错」在 equation based 场合不能当作「顺序对」的证据。**
（`## Errors` 里仍然有 `The edge order is wrong; for instance a window open must come before a window close` 一条——**两条并存，本页照记，不替它们调和。**）

### fast pin 与 `pdiv:n`：唯一会「替你算出一串延迟」的场合

这是 `definition_string` 那一格里最长的一段（原文标为 `Special Rules for Fast Pins:`）。要点：

> 「If a pin is configured as a fast pin in the context of the specification given by the first parameter, you can specify the period divider at the start of the definition string. The format is pdiv:n, where n must be the same value as the period_div value of the pins in pinlist within the timing set specified by the timing_set parameter.」

**`pdiv:n` 里的 `n` 不是自由值**——**它必须等于这些 pin 在这个 timing set 里的 `period_div` 值**。

> **对照**：`period_div` 这个 token 也是 `PDIV?` 的参数名，那一篇给它的取值是
> `-1 (for standard pins), 2, 3, 4, 6, 8 (only for fast pins)`。
> **这一条对照来自本批另一页 [[pdiv]] 的 raw，不是本篇**——
> **本篇从头到尾没出现 `PDIV` 这个命令名。**（见 [[pdiv]]）

**自动算延迟的公式**（原文单独一行）：

```
1st_edge_delay + (i-1) * (period/pdiv)
```

> 「1st_edge_delay is the delay specified for the first edge (d1 or r1; the generic notation e1 is not allowed for fast pins). If the first edge is not specified in the string, its delay is set to 0.」

**第一条 edge 就是基准**；**`e1` 这种通用记法在 fast pin 上不许用**（要么 `d1`、要么 `r1`）；
**没写第一条时它的延迟按 0 算**。

**三个附加条件，逐个都反直觉：**

| 条件 | 后果（原文） |
|---|---|
| `pdiv:n` 与第一条 edge 的延迟**都给**了 | 「ETDS calculates delays for the following n-1 edges except those that are specified explicitly in the string.」；并且「the delays for all the edges required by the period divider will be overwritten」（**算出来的会覆盖掉原有值**） |
| **`n = 3`** | 「the edges with index 1, 3, 5 are used for internal reasons」——**算的不是第 1、2、3 条，是第 1、3、5 条** |
| **`pdiv` 或第一条 edge 缺一个** | 「only the specified edges are modified. However, with receive edges this is only possible for r1.」——**receive 侧只有 `r1` 能这么用** |

**覆盖的两种写法**：

> 「When a delay is explicitly specified for one of the edges, this delay overrides the calculated default. There are two formats to specify overrides. You can either define absolute delays or the offsets from the default delays.」

> 「If you want to use the second, relative format, you must specify DELTA for the modeparameter. Note that you can also specify negative offsets in the DELTA mode.」

**`DELTA` 就是 `[mode]` 那一位上的取值，偏移可以是负的。**
（原文写的是 `modeparameter`，**中间没有空格**，见「出处」⚠️③。）

### `[mode]`：**写**命令那一半没有列出取值

> 「The operating mode. For the query, you can enter ALL for all modes or BIDIR for bidirectional mode, that is, for edges that serve both as drive and receive edges.」

> 「With fast pins, you can specify the mode DELTA for both the command and the query. In this mode, the delays specified for edges with an index > 1 are interpreted as offsets from the calculated default values.」

| 方向 | 能写什么 |
|---|---|
| **`ETDS?`（查询）** | `ALL`（所有 mode）、`BIDIR`（双向 edge） |
| **fast pin** | `DELTA`（**写和查都可以**） |
| **普通写命令（非 fast pin）** | **本篇没列**（**语料未写**） |

**`[mode]` 在语法式里是方括号 = 可选，所以最常见的写法是留空**——
**本篇三个示例里，每一次写命令都留空。**
**`DELTA` 那条还有一句要连着读**：`the delays specified for edges with an index > 1 are interpreted as offsets`
——**索引 1 的那条不受 DELTA 影响**（它是基准，不是偏移对象）。

### 三个示例各自证明什么

**例 1 —— `e` 记法会被展开成 `d` 与 `r` 两组**（原文逐字）：

```
> ETDS 1,1,,"e1:0 e2:2 e3:6 e4:4",(io)
> ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
> ETDS? 1,1,,(@)
< ETDS 1,1,,"d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4",(io)
< ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
```

**写进去的是 `e1:0 e2:2 e3:6 e4:4`，读回来成了 `d1:0 d2:2 d3:6 d4:4` 加 `r1:0 r2:2 r3:6 r4:4`。**
**四个 `e` 变成四个 `d` 加四个 `r`，数值逐个相同。**
（**推断**：「`e` = drive 与 receive 一起设的简写」是**本页从这一对输入/输出里读出来的**，
**原文没有一句话解释这个展开**；依据就是写 4 条 `e`、回 4 条 `d` 加 4 条 `r` 且数值一一对应。）
**`e` 记法在 fast pin 上不许用**（原文 `the generic notation e1 is not allowed for fast pins`）——
`io` 是普通 pin，所以这一例合法。

**例 2 —— fast pin、`pdiv:4` 的五步前后对照**（原文逐字）：

```
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5 d3:10 d4:15",(CP)
> ETDS 401,1,,"d2:5.5",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5.5 d3:10 d4:15",(CP)
> ETDS 401,1,,"pdiv:4 d1:3 d3:14",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:14 d4:18",(CP)
> ETDS 401,1,DELTA,"d3:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:12 d4:18",(CP)
> ETDS 401,1,DELTA,"pdiv:4 d1:0 d2:1 d4:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:6 d3:10 d4:14",(CP)
```

**把这五步按公式对一遍**（`pdiv:4`，而 `d1:0 → d2:5` 说明 **`period/4 = 5 ns`**，
所以相邻 edge 的间隔是 **5 ns**）：

| 步 | 写进去的 | 读回来 | 发生了什么 |
|---|---|---|---|
| ① 起始 | —（只查） | `d1:0 d2:5 d3:10 d4:15` | 默认态：从 0 起，每条 edge +5 |
| ② | `d2:5.5` | `d2:5.5`，其余三个不动 | **`pdiv` 与第一条 edge 都没给** → **只改点名的那一条** |
| ③ | `pdiv:4 d1:3 d3:14` | `d1:3 d2:8 d3:14 d4:18` | `pdiv` + `d1` 都在 → **`d2`/`d4` 被重算**（3、8、—、18），**`d3:14` 覆盖掉算出来的 13** |
| ④ | `DELTA,"d3:-1"` | `d3:12` | **`-1` 加在「算出来的默认值 13」上**，不是加在当时的实际值 14 上 |
| ⑤ | `DELTA,"pdiv:4 d1:0 d2:1 d4:-1"` | `d1:0 d2:6 d3:10 d4:14` | 先按 `pdiv` + `d1:0` 重算基线（0、5、10、15），**再在基线上**做 `d2:+1`、`d4:-1`；**没点名的 `d3` 停在重算后的 10** |

**第 ④ 步是原文自己点名的重点**（原文紧接在那段代码块之后）：

> 「Note in particular the effect of the first instance of the command in DELTA mode. The negative offset is not applied to the actual value of d3, which is 14, but to the calculated default value, which is 13.」

**「`DELTA` 加在谁身上」是本页最容易读错的一处**：
④ 的基准是**算出来的默认值**（13），不是**当前实际值**（14）；
⑤ 的基准也是**重算后的基线**，不是上一状态的实际值。
**两次都指向同一条：`DELTA` 的参照物是「本该是多少」，不是「现在是多少」。**

**例 3 —— multi-port：靠「规格名 + pin 名」反推 equation set**（原文逐字）：

```
> ETDS? "mu_timing",2,,(In1)
< ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ETDS "mu_timing",2,,"d1:0.5",(In1)
> ETDS? "mu_timing",2,,(In1)
< ETDS "mu_timing",2,,"d1:0.5",(In1)
```

> 「The specification name and the pin name identify the port (no pin may occur in more than one port within the same specification). Then the port and the specification identify the equation set.」

**两步定位**：① `规格名 + pin 名` → **port**（**同一个规格里，一个 pin 只能落在一个 port 里**）；
② `port + 规格` → **equation set**。

> **⚠️ 第一行返回里 `ETDS` 写了两次**（`< ETDS ETDS "mu_timing",2,,"d1:0",(In1)`）——
> **原文如此，本页照抄没改**（见「出处」⚠️④）。

**`pinlist` 的三种写法**（与 [[pclk]] 同一套）：

> 「The name of the pin or pins for which edge delays are to be set or read back. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.」

| 写法 | 意思 |
|---|---|
| pin 名，逗号分隔 | 点名的那几个 |
| [[dfgp]] 建的 group | 整组当 pinlist 用 |
| `@` | **所有已配置的 pin** |

multi-port 场合另加一条：

> 「In a multi-port setup, every pin must belong to a port of the specified specification.」

### 与 site 的关系：这套设置改的是「setup focus 里的那个 site」

参数节之后有两段（与 [[etim]] 那一篇逐字相同的说明段）：

> 「With this command you configure setups of those sites that have the setup focus: For more information, see also: PSFC, PSFC?.」

> 「With this command you can retrieve site specific information (only one site can be in focus at a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**三件事**：① 改的是**处于 setup focus 的那个 site**；
② **一次只能有一个 site 在 focus**；
③ **回读也只回那一个 site 的**（`any firmware queries report setup and results for the site currently in focus only`）。
机制页是 [[psfc]]（**那一篇本页没读**）。

## 典型用法

**先说范围**：本篇**没有 `## Procedure`、没有 `## Before you begin`**。
唯一的流程线索是 `## Application` 一节，全文一句：

> 「Timing Setup, see Timing Setup Commands.」

对应 [[timing-setup-commands]]（**那篇本页没读**）。
**所以「ETDS 在 timing setup 流程里排第几步」本篇没说**——本页不替它排。

**1. 写之前先确认三件事**：

| 项 | 从哪知道 |
|---|---|
| waveform set 存在、编号在范围内 | 上界由 `WSUS` 定（[[wsus]]） |
| timing set 编号在范围内 | 上界由 `TSUS` 定（[[tsus]]） |
| 这些 pin 在这个 timing set 里是不是 fast pin | 决定要不要写 `pdiv:n`、以及第一条 edge 写 `d1` 还是 `r1` |

**2. 三种定位方式对号入座**（出自语法式）：

| 场合 | 第一格写什么 |
|---|---|
| fixed timing | `{waveform_set}`（`PRM` 表示 primary） |
| equation based | `{specset_id}` —— 由 `100 * equation_set_no + specset_no` 算出 |
| multi-port | `"multi-port_spec"`（**带引号**） |

**3. 写之前想清楚「要不要让系统替你算」**：

- **普通 pin**：点名的 edge 被改，**没点名的保持原值**。
- **fast pin + 想要一串**：`pdiv:n` **并且**写第一条 edge 的延迟 → 中间那些被**算出来**。
- **fast pin + 只改一条**：`pdiv` 与第一条 edge **缺一个** → 只改点名那条
  （**receive 侧只支持 `r1`**）。

**4. 要相对调整就用 `DELTA`**（例 2 的 ④⑤）。
**记住基准是「算出来的默认值」**，不是「当前值」；**索引 1 那条不受 `DELTA` 影响**。

**5. 回读**：`ETDS? {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {(pinlist)}`。
**回读只回「wavetable 里用到的」或「值不为 0 的」edge**——
**别把回读结果当成「完整设置清单」**（见「是什么」第一段）。

**6. 生效时点**：写完**不会立刻生效**——`## Postdependencies` 说的是
**下一次 functional test 开始时** primary sets 才被重新激活。

**7. 报错时先看哪一条**：`## Errors` 六条，前两条是编号越界（`WSUS` / `TSUS`），
第三条是 primary timing set 没定义，第四条是 edge 顺序，第五、六条是位置与周期。
**第五条原文写的是 `Eplacement`**（见「出处」⚠️⑤）。

**8. 原文没给的**：没有示例演示「改完之后用 `ETDS?` 逐条核对顺序」，
**也没有任何一处讲怎么把 delay 和波形定义对应起来**——**那两件事本篇不管**。

## 和谁有关

- [[etim]] — **被 ETDS 替代的那条命令（前任/上游）**。本篇第一段明写 supersedes 它。
  **但两篇的版本号与替代范围对不上**：本篇 `from release 2.0 for waveforms with more than 6 edges`，
  [[etim]] 那一篇 `from release 2.1 onwards when 14-edge setups are used`。
  **本页两处并列照记，不替它们调和**（见「出处」⚠️②）。
- [[wsus]] — **上限来源（前置）**。`waveform_set` 的最大值由它定；
  本篇的参数节与 `## Errors` 第一条各点它一次。
- [[tsus]] — **另一条上限（前置）**。`timing_set` 的最大值由它定；
  参数节与 `## Errors` 第二条各点它一次。
- [[pdiv]] — **`pdiv:n` 里那个 `period_div` 的出处（并列/上游）**。
  **这一条对照来自本批另一页 [[pdiv]] 的 raw，不是本篇**——
  **本篇从未出现 `PDIV` 这个命令名。**
- [[dfgp]] — **`pinlist` 的另一种写法（并列）**：`groups previously created by the DFGP (DeFine GrouP) command`。
  **`DFGP` 那一篇本页没读。**
- [[psfc]] — **site 聚焦机制（上游）**。本篇两段 `setup focus` 的说明都指向它。
  **那一篇本页没读**，所以「focus 怎么设」本页没有。
- [[wfds]] / [[bwds]] — **`## Errors` 第四条把「edge 顺序」的两处判据指给这两条命令**
  （原文写的是 `mismatch exists between edge delays of the selected timing set and the waveform definition -` 后接这两条）。
  **两篇本页都没读**，所以**它们各自怎么定义顺序，本页没有。**
- [[timing-setup-commands]] — **本章归属（上游）**：`## Application` 指向 Timing Setup 那一章。
- [[waveform-set]] — **`already existing waveform set` 指的那个东西（前置概念）**。
  本篇只说「得先存在」，**不说它是什么、怎么建**。
- [[timing]] — **`stage: timing` 的依据**（frontmatter；§6：`stage` 填最近的一段，不是归属）。

**本篇点到名字、本页没读的还有三篇**（都用反引号，**未建页，§9.1**）：

- `Defining waveforms for Pin Scale 9G pins`（raw: `02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`）
  —— **9G 的 `fn`/`sn` 到底怎么用，在那篇**；本篇只给了一句「有两种 drive edge」。
- `Selecting and ordering edges`（raw: `02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）
  —— **edge 顺序的完整规则在那篇**；本篇只给了 `d1` 不能大于 `d3` 这一个例子。
- `WFDS, WFDS? - (WaveForm Definition String)` / `BWDS, BWDS? - (Break Waveform Definition String)`
  —— 见上；**整篇标题用反引号写，已经有页的那两条用双方括号链。**

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 ETDS」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 ETDS」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
所以「`DELTA` 是哪一版加的」「Pin Scale 9G 的 `fn`/`sn` 是哪一版加的」
「`pdiv` 那套自动算延迟是哪一版加的」**在本篇里查不到**。

**另一类「版本」本篇写了、但不在这一节里**：正文那句
`supersedes the command ETIM from release 2.0`。
**注意那是 `release`，不是 `SmarTest X.Y.Z` 形式**——
**它指的是哪一套版本号（SmarTest 的 release？还是别的？）本篇没说**，
而且**它和 [[etim]] 那一篇的 `release 2.1` 冲突**（**语料未写哪个对**）。

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`
  （frontmatter 的 `source_topic` 是 `98599.htm`；**9,828 字节 / 211 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **文档里链到的七篇一篇都没读**：`PSFC, PSFC?`、`WSUS`、`TSUS`、
  `Defining waveforms for Pin Scale 9G pins`、`Selecting and ordering edges`、
  `WFDS, WFDS? - (WaveForm Definition String)`、`BWDS, BWDS? - (Break Waveform Definition String)`。
  所以：**site focus 怎么设、9G 的 `fn`/`sn` 怎么用、edge 顺序怎么判、`WFDS`/`BWDS` 怎么定义波形
  ——本页一个字都没有。** 本页只保证「本篇分别点过它们的名字」。
- **`ETIM` 那一篇的 raw 不在本页的 `sources:` 里**——本页只读了自己这一篇。
  它的内容见 [[etim]] 那一页；**本页与它的两处冲突都来自「本页读的两篇」**——
  **`## 出处` 里那条 ⚠️② 的两句原文，一句取自本篇，另一句取自 [[etim]] 那一页的 raw**，
  **本页没有把 [[etim]] 的其它内容搬进来。**
- **`Timing Setup Commands` 那一篇没读。** 本篇 `## Application` 只给了它的标题。
  **所以「ETDS 在流程里排第几步」本页没有。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **这张「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上跑过 `ETDS` / `ETDS?`**（`verified: doc-only`）。
  **所以「例 2 那五步在真机上是不是这个结果」本页只能保证「文档这么写」（§11）。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的六条——不是漏写。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`（**本页的出处**） | `98599.htm` | 9,862 | — |
| `02.06_Command_Reference/02.06.06.02.15_ETDS__ETDS__-__Edge_Timing_Definition_String.md` | `98599_2.htm` | 9,863 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.15_ETDS__ETDS__-__Edge_Timing_Definition_String.md` | `98599_3.htm` | 10,144 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。

### 上游 `.htm` 核对（2026-09-24 做，这是本页**多出来的**一步）

**这四条本页全去上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\98599.htm`（18,785 字节）核过。
结论：①⑤ 是「上游就坏的」（§11.2 ⑥），②③④ 是「上游 HTML 就没有那个空格」（靠样式分界，不是转换丢的）。**
明细见下面每条 ⚠️。**核过的用处**：这四处**重做一次转换也救不回来**，
所以页面必须留着它们、而不是等谁来修。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `ETIMfrom`——少一个空格。** 原文逐字：
> `This command supersedes the command ETIMfrom release 2.0 for waveforms with more than 6 edges.`
> **`ETIM` 与 `from` 之间没有空格。**
> **上游核对**：`98599.htm` 正文里就是 `the command ETIMfrom release 2.0`，
> **纯文本、没有标签隔开** → **上游就坏的**。
> （markdown 这一侧另外把 `ETIM` 变成了链接，于是本页读到的形态是
> **链接的右括号直接顶着 `from`**——**换成了链接写法，但两个词之间还是没有空格**。）
>
> **② 替代关系的版本号与范围，两篇对不上。** 本篇逐字：
> `This command supersedes the command ETIMfrom release 2.0 for waveforms with more than 6 edges.`
> [[etim]] 那一篇逐字：
> `This command is replaced by the command ETDS, ETDS? from release 2.1 onwards when 14-edge setups are used.`
> **`2.0` vs `2.1`；`more than 6 edges` vs `14-edge setups`。**
> **上游核对**：两句分别在上游 `98599.htm` 与 `98600.htm` 里都是这样写的
> （`98599.htm` 里 `release 2.0` 出现 2 次，`98600.htm` 里 `release 2.1` 与 `14-edge` 各出现 3 次）
> → **上游就坏的，两边都是。本页两处并列照记，不判定哪个对。**
>
> **③ `modeparameter`——少一个空格。** 原文逐字：
> `If you want to use the second, relative format, you must specify DELTA for the modeparameter.`
> **上游核对**：`98599.htm` 里是
> `<span class="keyword">mode</span>parameter`——**两个 `<span>` 之间本来就没有空格字符**，
> 靠样式分界。**所以这不是转换丢的字符，是上游 HTML 自己没写空格。**
>
> **④ 例 3 的第一行返回里 `ETDS` 重复了一次。** 原文逐字：
> ```
> < ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ```
> **`<` 之后是 `ETDS ETDS`。**
> **上游核对**：`98599.htm` 里就是 `&lt; ETDS ETDS "mu_timing",2,,"d1:0",(In1)`
> → **上游就坏的。本页照抄，没删那一个。**
>
> **⑤ `Eplacement`——错字，应为 `Placement`。** 原文逐字（在 `## Errors` 段里）：
> ` Eplacement is outside the allowed range.`
> **既拼错了，前面还多一个空格。**
> **上游核对**：`98599.htm` 里是 `<li> Eplacement is outside the allowed range. </li>`
> → **上游就坏的**（§11.2 ⑥ 那一族：**看起来完全正常、其实错**）。
> **这一条在脚本抽的「报错条件」节里，本页一个字没动它**——
> **所以页面上的 `Eplacement` 是对的（照实转录），不要照它抄进任何自动化输入。**
>
> **⑥ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。
>
> **⑦ `pdiv:nand`——少一个空格。** 原文逐字：
> `If you specify pdiv:nand a delay for the first edge, ETDS calculates delays for the following n-1 edges except those that are specified explicitly in the string.`
> **`pdiv:n` 与 `and` 之间没有空格。**
> **上游核对**：`98599.htm` 里是
> `<span class="keyword">pdiv:</span><span class="keyword">n</span><em>and </em>a delay`——
> **两处标签之间没有空格字符，上游用 `<em>` 把 `and ` 标成斜体来分界。**
> **所以这是上游 HTML 的分界方式，不是转换丢的字符。**

`verified: doc-only`
