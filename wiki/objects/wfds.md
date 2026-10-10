---
type: object
title: WFDS, WFDS? - (WaveForm Definition String)
layer: L1
stage: timing
tags: [timing, waveform, logical-waveform, wfds, l1-command, firmware-command, fixed-timing, equation-based-timing, wavetable, smart-scale]
related: [wave, wsus, wavetable, waveform-set, dfgp, etds, vclk, timing, timing-setup-commands]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# WFDS, WFDS? - (WaveForm Definition String)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,003 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### WFDS

```
WFDS {wvf_set}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
WFDS {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### WFDS?

```
WFDS? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDS {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98872.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 4 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…

### Example

```
> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)
> WFDS 1,1,,"r4:EE1",(io)
> WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)

> WFDS? 1,ALL,,(@)
< WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)
< WFDS 1,1,,"r4:EE1",(io)
< WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md>` 的 `## Errors`、`## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- wvf_set is greater than the range allowed by the WSUS command, or < 1
- The waveform index is outside the range of 0 - 256 (Pin Scale systems)
- There is a mismatch between the edge actions and edge order in the specified waveform
- You specify a drive action for an output pin
- You specify a receive action for an input pin
- There is a mismatch in edge direction between the waveform you have defined and existing waveforms
- There is a missing window close action between two window open actions
- There is a missing window open action between two window close actions

### Warnings

A warning is generated if edge delays are auto-corrected to fit in with the programmed waveform. The timing sets belonging to the affected waveform set are modified as necessary

<!-- 报错节 end -->

## 是什么

**WFDS 定义的是「逻辑波形」——一个 device cycle 里，每条 edge 做什么动作。**
原文第一句：

> 「The WFDS command defines a logical waveform within a waveform set (fixed timing). It can also
> be used to change the runtime definitions of logical or pure physical waveforms in an equation
> based timing. The WFDS? query returns existing definitions of logical or pure physical waveforms.」

**一句话里两个场合**：**fixed timing 下定义**、**equation based 下改 runtime 定义**；
**`WFDS?` 那一半只回读**。

**「逻辑波形 / 物理波形」这一对概念是本页的骨架**：WFDS 写的是**动作序列**
（这个 cycle 里有哪些动作、哪些由 data 参数决定、哪些是固定状态），
**真正的物理值由 [[wave]] 填**——**这一半的正文在 WAVE 那一页；本篇只在 `## Postdependencies` 里点名它。**

### 覆盖写：改一条逻辑波形 = 它的物理波形全部作废

`## Mode of operation` 的第一段讲的就是这个，**这是 WFDS 最容易踩的一处**：

> 「If the specified waveform index is already in use, WFDS overwrites the previous definition.
> This causes all previously defined physical waveforms for this logical waveform to be undefined.
> You have to define all of them again for the modified logical waveform (with the WAVE command).」

**三步因果，一步比一步重**：

| # | 原文 | 后果 |
|---|---|---|
| ① | `WFDS overwrites the previous definition` | **号已被占用就直接覆盖**——动词是 `overwrites`，不是 `fails` |
| ② | `This causes all previously defined physical waveforms for this logical waveform to be undefined` | **该逻辑波形下已有的物理波形全部变回未定义** |
| ③ | `You have to define all of them again for the modified logical waveform` | **改完必须把物理波形重新定义一遍**，修法是 `with the WAVE command` |

**`## Errors` 的八条里没有一条是为「覆盖」设的**（**推断**：覆盖不是错误，所以没有对应报错；
依据是 `## Errors` 只说「什么时候报错」，而 `## Mode of operation` 用的是 `overwrites` 这个动词；
**原文没有把这两件事连起来说**）。

### 「顺序不对」有两种结果，取决于那条 edge 在不在用

> 「The command will not be accepted if the edge order restrictions are not fulfilled for the used
> edges. If the position of an unused edge does not meet the order requirements implied by the new
> definition string, it will be auto-corrected. Edges which are already used in other waveforms
> will not be moved. Edge restrictions are discussed in Selecting and ordering edges.」

**三句话、三种对象**：

| 对象 | 结果 |
|---|---|
| **本次用到的 edge**（`the used edges`）不满足 edge order 限制 | **命令不被接受**（`will not be accepted`） |
| **没用到的 edge** 位置不满足新定义串隐含的顺序要求 | **自动改正**（`it will be auto-corrected`） |
| **别的波形已经在用的 edge** | **不动**（`will not be moved`） |

**所以「顺序不对」在 WFDS 里不是一种结果，是两种**——
**判据是那条 edge 有没有被用到**。
**`Selecting and ordering edges` 那一篇本页没读**（见「出处」）——
**「edge order 到底有哪些限制」本页一个字没有。**

### 后依赖：定义完必须接 [[wave]]

`## Postdependencies` 一节全文（逐字）：

> 「After you have defined the logical waveform with WFDS, you must specify the physical waveforms
> that are based on it with the WAVE command. This is required even if the logical waveform
> contains no data parameters.」

**`must` 加上 `This is required even if the logical waveform contains no data parameters.`**——
**「没有 data 参数」不等于「不用 WAVE」**。
（[[wave]] 那一篇里有对称的一句：`Only physical waveforms are downloaded to the hardware and
executed by the sequencer.`——**那一句在 WAVE 的 raw 里，本页读到的 [[wave]] 页引了它**。）

### `wfIndex`：0..255，而且**这里写十进制、wavetable 里是十六进制**

> 「Waveform index. Enter an integer between 0 and 255. The index references a waveform in a
> device cycle. For the query you can also enter ALL for all waveform DC/DC power units. The
> waveform index is also used by the WAVE, WAVE? - (WAVEform) command.」

> 「Note that the index must be specified decimally here, whereas in the wavetable, it is coded hexadecimally.」

**第二句是这一格唯一的坑**：**同一个号，命令里写十进制、wavetable 里写成十六进制。**

**⚠️ 第一句里的 `DC/DC power units` 是坏串**（上下文要求它是「index 的复数」）——
**这一处本页核过上游 `.htm`，是上游就坏的**，见「出处」⚠️ ①。

### `definition_string`：驱动侧与接收侧两套动作码

**先看它管哪些 edge**：

> 「Edge action definition string which consists of drive actions for the drive/ bidirectional
> edges only. On Pin Scale systems, there is only one drive edge type, which is denoted by
> di (1 鈮? i 鈮?8).」

**⚠️ 那句里的 `鈮?` 是坏字**（**这一处本页核过上游 `.htm`，`.htm` 里是干净的 `≤`**），见「出处」⚠️ ②。

**驱动侧的动作清单逐条见上面「语法 / 参数」节**（脚本逐字抽的）。
清单里有两处**同一栏内自相矛盾**的地方，本页照实引（详见「出处」⚠️ ③④）：

```
- D1N: Drive parameter 1 (DD1), no tri-state action
- D1N: Drive parameter 2 (DD2), no tri-state action
```

**同一个动作码 `D1N` 写了两遍，第二遍的说明是「parameter 2」**——
**按同表规律第二行应当是 `D2N`**（**推断**：依据是紧接着那张 formatter 表把这一族写成
`D1N, D2N, C1N, C2N`；**原文没有一句话说明**）。

```
- EE2: Edge compare to parameter 1 (ED2)
- WE1: Window open with compare to parameter 1 (ED1)
- WE2: Window open with compare to parameter 1 (ED2)
```

**`EE2` 与 `WE2` 的说明里都写着 `parameter 1`，而括号里是 `ED2`**——
**按 `EE1` / `WE1` 那两行的规律，这两行应当是 `parameter 2`**（**推断**，
依据是成对的 `EE1` / `EE2` 与 `WE1` / `WE2` 各指一个参数；**原文没有一句话说明**）。

**两张清单之外，还有一条约束只管 capture**：

> 「Note that waveforms that are to be used for selective digital capture must contain exactly one compare action.」

**它和 `## Errors` 里那两条 window 相关的报错是同一套动作码的正反面**：
`WC`（window close）与 `W0` / `W1` / `WI` / `WX` / `WU`（window open）在清单里，
而报错段里有 `There is a missing window close action between two window open actions`
与 `There is a missing window open action between two window close actions`。

### 哪几个 data 参数用 formatter（**这张表是给 [[wave]] 用的**）

> 「The following table shows which data-dependent drive actions use the driver formatter, which
> use the tri-state formatter, and which use both. You have to consider this when assigning
> parameters to the WAVE command. See also Specifying the actions.」

（本页「语法 / 参数」节里那张被压平的表，重排如下）

| Data-dependent Drive Action | Driver | Tri-state |
|---|---|---|
| `D1N, D2N, C1N, C2N` | `yes` | `no` |
| `DN1, DN2` | `no` | `yes` |
| `D11, C11, D22, C22` | `yes` | `yes` |

**这张表是 WFDS 与 [[wave]] 之间的接口**——
**「WFDS 里用了哪种 data 参数」决定了「WAVE 那边要分配几个 formatter 参数」**。
**它同时是本页判「`D1N` 那两行有一行是错的」的依据**（见上文与「出处」⚠️ ③）。

### 没写出来的 edge 一律是 `N`

> 「All edges which are not explicitly set are set to N. In the query only those edges that are used are printed.」

**这句话解释了回读为什么比写入短**——见「典型用法」里 `e1:` 与 `d1:` 那一处对不上。

### Smart Scale 上只认 `0` / `1` / `N`，而且是两种 edge

> 「On Smart Scale systems, there are two types of drive edges, denoted by fi and si (1 鈮?i 鈮?8).
> For both of them, only the action codes 0, 1, and N are admitted. But the Smart Scale systems
> also support the old di syntax. For more information see Defining waveforms for Smart Scale pins.」

**两句要分开读**：① **Smart Scale 有两种驱动 edge（`fi` / `si`），动作码只许三个**；
② **旧的 `di` 写法在 Smart Scale 上也还认**。
**`0` / `1` 两个裸码不在上面那张驱动动作清单里**（清单里最短的是 `N`）——
**清单与这一句用的是两套写法，本篇没有把它们对齐**（**这一条是本页的观察，不是裁定**）。
**`Defining waveforms for Smart Scale pins` 那一篇本页没读**（见「出处」）。

### `ALLOW_EQ`：equation based 下才加的那个开关

> 「This extra parameter allows you to define or change logical waveforms for an equation based
> timing. Note that only the runtime settings are affected; the definitions in the wavetable are
> not changed.」

**加了它的代价，原文列了三条**（逐字）：

> - Every runtime change will affect all specifications that use the respective wavetable.

> - Since the new or changed waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.

> - The runtime definitions are not checked for consistency. It is up to the user to ensure this.

| 代价 | 后果 |
|---|---|
| **波及面** | **改 runtime，同一个 wavetable 下的所有 spec 都跟着变** |
| **速度** | **每个用到该 wavetable 的 spec 都要重新求值并下载，所以慢** |
| **责任** | **这些 runtime 定义不做一致性检查，你自己保证** |

**同一族里 [[wave]] 的 `ALLOW_EQ` 讲的是同一件事**（措辞几乎一样），
**两篇各说一遍**（**本页只保证本篇这一处**；[[wave]] 那一篇的原文不在本页取材内）。

### `mode` 只有一个词：`Not used.`

参数表里 `mode` 一栏全文就是 `Not used.`——**但它在语法行里占一个位**（`[mode]`），
**所以省不得**：例子里那两个逗号之间就是空的（`1,0,,`，见「典型用法」）。

### `pinlist` 与 `@`

> 「The name of the pin or pins for which the waveform is to be defined or read back. This
> parameter can also include groups previously created by DFGP, DFGP? - (DeFine GrouP). The @
> symbol can be used to specify all configured pins. If more than one pin is to be included, the
> names must be separated with a comma.」

**`@` 在这里是「所有已配置的 pin」**；**回复里它会被展开**
（见「典型用法」：写的是 `(@)`，回来的是 `(io)` 与 `(clk)`）。

## 典型用法

**1. 三步顺序**（原文给的前两步是硬前提）：

| # | 做什么 | 拿什么做 |
|---|---|---|
| ① | **定义逻辑波形**（动作序列） | `WFDS`（本页） |
| ② | **定义物理波形**（data 参数的具体取值） | [[wave]]——**`must`，且 `even if the logical waveform contains no data parameters`** |
| ③ | **回读** | `WFDS?` / `WAVE?` |

**② 不能省**：原文的 `## Postdependencies` 用 `must` 写的（见「是什么」）。

**2. 原文示例（`## Example`，逐字）——三次定义、一次回读**：

```
> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)
> WFDS 1,1,,"r4:EE1",(io)
> WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)

> WFDS? 1,ALL,,(@)
< WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)
< WFDS 1,1,,"r4:EE1",(io)
< WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
```

**头三行逐位对一遍**（`1` 是 `wvf_set`、`0` / `1` 是 `wfIndex`、空的那格是 `mode`）：

| 行 | `wvf_set` | `wfIndex` | `mode` | `definition_string` | `pinlist` |
|---|---|---|---|---|---|
| 1 | `1` | `0` | 空 | `"e1:F00 e2:D1N e3:F00"` | `(io)` |
| 2 | `1` | `1` | 空 | `"r4:EE1"` | `(io)` |
| 3 | `1` | `0` | 空 | `"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00"` | `(clk)` |

**读这个例子有四处值得停一下**：

- **第 1 行与第 3 行的 `wfIndex` 都是 `0`，但不冲突**——`pinlist` 不同（`(io)` 与 `(clk)`），
  **波形号是按 pin 记的**（**推断**，依据是第 4 行的回读里两行 `1,0,` 各配一个 pinlist；
  **原文没有一句话讲「同一个号在不同 pin 上是否能并存」**）。
- **第 1 行写的是 `e1:` / `e2:` / `e3:`，回读出来是 `d1:` / `d2:` / `d3:`**——
  **`e` 与 `d` 对不上**（见「出处」⚠️ ⑤）。**第 3 行用的正是 `d1:`..`d8:`。**
- **第 2 行用的是 `r4:`**（`r` = receive）。**本篇的动作清单里没有解释 `r` 这个前缀**
  ——**它只讲了 `di`（驱动）与 `fi` / `si`（Smart Scale 驱动）**（**语料未写**）。
- **回读里 `(@)` 被展开了**：写的是 `(@)`，回来的是 `(io)` 与 `(clk)` 两行——
  **一行一个 pinlist**，而不是一行 `(@)`。

**3. `WFDS?` 也能按 wavetable / specset 回读。** 语法行第一位是
`{wvf_set|"wavetable"|specset_id|"multiport_spec"}`，
**参数表里 `wavetable_name` 那一栏的原文是** `The wavetable name. Enter a string of up to 40
alphanumeric characters (upper or lower case) enclosed by double quotes.`——
**两处的写法不一样**（语法行写 `"wavetable"`，参数表那一栏叫 `wavetable_name`，见「出处」⚠️ ⑥）。

**4. 要改一条已经存在的逻辑波形**（本页按 `## Mode of operation` 那一段排的，**顺序本身是建议**）：

1. **先想清楚代价**：覆盖会把该逻辑波形**已有的物理波形全部作废**。
2. `WFDS` 写新定义（**同一个 `wfIndex`**）。
3. **把物理波形全部重新定义一遍**（[[wave]]）。
4. 回读核对（`WFDS?` / `WAVE?`）。

**5. equation based 场合**：**在 `WFDS` 上加 `ALLOW_EQ`**，并且知道它那三条代价
（见「是什么」）。

**6. 报错来了先查这四处的哪一处**（本页按 `## Errors` 八条归类，**顺序本身是建议**）：

| 报错说的 | 先查 |
|---|---|
| `wvf_set is greater than the range allowed by the WSUS command, or < 1` | [[wsus]] 那边的上限 |
| `The waveform index is outside the range of 0 - 256 (Pin Scale systems)` | `wfIndex` 的范围（**注意这句写 `0 - 256`，参数表写 `0 and 255`，见「出处」⚠️ ⑦**） |
| `There is a mismatch between the edge actions and edge order in the specified waveform` / `There is a mismatch in edge direction between the waveform you have defined and existing waveforms` | `definition_string` 的动作与 edge 顺序（**后一条还包括「与已有波形比」**） |
| `You specify a drive action for an output pin` / `You specify a receive action for an input pin` | **pin 的方向**——**本篇没有说怎么查一个 pin 是 input 还是 output**（**语料未写**） |
| `There is a missing window close action between two window open actions` / `There is a missing window open action between two window close actions` | `W0`..`WU` 与 `WC` 的配对 |

**还有一条不是错误，是警告**（`## Warnings`，全文一条）：

> 「A warning is generated if edge delays are auto-corrected to fit in with the programmed waveform.
> The timing sets belonging to the affected waveform set are modified as necessary」

**它的后果比「一条警告」大**：**受影响 waveform set 底下的 timing sets 会被改**。

## 和谁有关

- [[wave]] — **下游，而且是硬前提（前置/下游）**。本篇 `## Postdependencies` 用 `must` 写的：
  `After you have defined the logical waveform with WFDS, you must specify the physical waveforms
  that are based on it with the WAVE command.` **分工是「WFDS 写动作序列 / WAVE 填 data 参数的具体值」。**
  **本篇另外还在两处点名它**：`wfIndex` 那一栏（`The waveform index is also used by the WAVE, WAVE? - (WAVEform) command.`）、
  以及那张 formatter 表（`when assigning parameters to the WAVE command`）。
  **WAVE 那一篇的正文不在本页取材内**——**所以「`DD1` / `ED1` 怎么填」本页只有那张表的 `yes` / `no`。**
- [[wsus]] — **`wvf_set` 上限的来源（前置）**。本篇一处点名（参数表）+ 一处报错。
- [[wavetable]] — **equation based 下的作用域（同类）**。
  `ALLOW_EQ` 那三条代价全都在讲 wavetable（`the definitions in the wavetable are not changed`、
  `all specifications that use the respective wavetable`）。**wavetable 本身的正文在那一页里。**
- [[waveform-set]] — **fixed timing 下的作用域（同类）**。本篇第一句就是
  `defines a logical waveform within a waveform set (fixed timing)`。
- [[dfgp]] — **`pinlist` 的另一种写法（并列）**：
  `This parameter can also include groups previously created by DFGP, DFGP? - (DeFine GrouP).`
- [[etds]] — **`## Related information` 一节里的两条之一**。**本篇没有说是什么关系**
  （那一节只有两个链接，没有一句说明）；**本页没读它**。
- [[timing-setup-commands]] — **上游入口**。本篇 `## Application` 全文一句：
  > 「Timing setup, see Timing Setup Commands.」
  **本篇没有说 WFDS 在 timing setup 流程里排第几步。**
- [[wave]] / [[etds]] 之外，**`## Related information` 一节的两条链接是首尾相连的**
  （中间没有分隔符，见「出处」⚠️ ⑧）——**本页照原样记**。
- [[vclk]] — **同章的另一族命令（并列）**。**本篇一次没提它**；
  同章的依据是两篇都在 `02.06_Command_Reference` 下（**两篇都是本页的取材**）。
  **分工完全不同**：本篇**写**逻辑波形，[[vclk]] **只查**一个周期会不会触发 auto-correction。
- [[timing]] — **stage 页**。本页 `stage: timing` 的依据是本篇 `## Application` 那句 `Timing setup`。
- `WFDF` / `WFUD` / `Selecting and ordering edges` / `Specifying the actions` /
  `Defining waveforms for Smart Scale pins`（**均未建，故用反引号，§9.1**）——
  **本篇点名的五条邻居**：`WFDF` 与 `WFUD` **本篇其实一次都没点名**
  （**WAVE 那一篇的报错段引了它们**，本页读到的 [[wave]] 页引了那两句），
  **另外三条是本篇正文点名但本页没读的**：edge 顺序（`Edge restrictions are discussed in Selecting and ordering edges.`）、
  动作分类（`See also Specifying the actions.`）、Smart Scale 波形（`For more information see Defining waveforms for Smart Scale pins.`）。
  **五篇的 raw 本页都没读。**

## 版本

**本文档有 `## Functional changes` 段，段里有两条**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.0.1: C/CE and P cards are not supported` → [[smartest-7.0.1]]

> **第一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 WFDS」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 WFDS」。**
>
> **第二条是真正的版本条目**，而且它是一条**「不再支持」**的记录：
> **从 7.0.1 起，C/CE 与 P 卡不支持**。
> **⚠️ 一处名词对不上**：版本段说 `C/CE` 与 `P` 卡，**而正文只区分 `Pin Scale` 与 `Smart Scale`**
> （`## Errors` 那一条也写 `Pin Scale systems`）——**两处用的不是一套名字**，
> **本篇没有把「C/CE / P 卡」与「Pin Scale / Smart Scale」对应起来**（**语料未写**）。
> **本页照两处的原样并列，不替它连线。**

**版本段里没有的东西（照实记，不替它补）**：没有第三条。
**所以「`ALLOW_EQ` 是哪一版加的」「`wfIndex` 上限 255 是哪一版定的」在本篇里查不到**——
**而 `ALLOW_EQ` 管的正是 equation based 下的运行时改写，看起来正是会被记进版本段的那类功能。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`
  （frontmatter 的 `source_topic` 是 `98872.htm`；**4,032 字节 / 288 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。
  **本篇没有 `## Syntax` 段**——它的两段语法挂在 `## WFDS` 与 `## WFDS?` 两个标题下，
  **两个标题与文档标题里的命令名逐字相同，所以它们进了语法节**
  （对比 [[msdf]] 那一页：那里的段标题拼错一个字母，两段语法就没进——**那是本页读到的 [[msdf]] 页**）。

**本页没做的**：

- **`WAVE` / `WFDF` / `WFUD` / `DFGP` / `WSUS` 五篇都没读。** 它们都只是本篇点名的邻居：
  **物理波形的 `DD` / `ED` 怎么填（WAVE）、另一种逻辑波形命令与删除命令长什么样（WFDF / WFUD）、
  group 怎么建（DFGP）、上限怎么算（WSUS），本页全无。**
- **`Selecting and ordering edges` / `Specifying the actions` /
  `Defining waveforms for Smart Scale pins` 三篇都没读。**
  **所以「edge order 的限制有哪些」「动作怎么分类」「Smart Scale 的 `fi` / `si` 怎么用」本页一个字没有**
  ——**而这三件事本篇都只留了一句 `see`。**
- **`## Mode of operation` 里那张 formatter 表本页重排了一遍**（原文里它是参数表内部的一张嵌套表，
  在页面的「语法 / 参数」节里被压平成管道行）。**要逐字核对请回 raw（第 131 行起）。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **「逻辑波形表长什么样、三种 formatter 各自长什么样」本页只有文字（§11.4）。**
- **没在机台上跑过 `WFDS` / `WFDS?`**（`verified: doc-only`）。
  **所以「覆盖之后物理波形真的全废了吗」本页只能保证「文档这么写」（§11）。**
- **`verified: doc-only` 之外的一条**：**本页的 `yes` / `no` 表、动作清单、报错八条，
  全部只有本篇一个来源**——**没有任何一条能交叉核对。**

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`（**本页的出处**） | `98872.htm` | 9,026 | — |
| `02.06_Command_Reference/02.06.06.02.42_WFDS__WFDS__-__WaveForm_Definition_String.md` | `98872_2.htm` | 9,027 | **`diff` 报 4 行差异——全部是 frontmatter 的 `source_topic` / `source_html` 两行** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.42_WFDS__WFDS__-__WaveForm_Definition_String.md` | `98872_3.htm` | 9,335 | **差异只有 frontmatter 与篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它） |

**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有逐字读它们的正文**（§12 不越取材边界）。
**所以「三份里那个坏串与那些坏字是不是都在」本页只核了第一份**（§13.1：没核 ≠ 没有）。

### ⚠️ 两处坏东西，本页分别核过上游的 `.htm`（`raw/98872.htm`）

> **—— 这两处不是一类，处置完全不同（§11.2 ① vs ⑤），所以分开写。**

> **① `DC/DC power units` 是「整词替换」损坏（§11.2 ⑤），而且是上游就坏的。**
> 逐字（**在 `wfIndex` 那一栏里；这一处同时出现在本页「语法 / 参数」节里，那一节本页一个字没动**）：
> ```
> For the query you can also enter ALL for all waveform DC/DC power units.
> ```
> **上下文要求这里是一个「waveform 的 index 的复数」**——同一句的上一句是
> `Enter an integer between 0 and 255.`，下一句是 `The waveform index is also used by the WAVE, WAVE? - (WAVEform) command.`
> **判据**：它出现在本该是 index 的位置（`ALL for all waveform ___`），
> **而正确的形态 `waveform index` 在同一栏的下一句里活着**。
> **同语料别处有干净的复数写法**（`The physical waveform indexes for that particular signal are displayed.`，
> 在 `02.08.04.16.02.02` 那一篇里）；**本页据此把原词推为 `indexes`（推断）**——
> **本篇自己没有一句干净的同句可对，所以「`indexes` 还是 `indices`」本页不下断言。**
> **本页核过 `raw/98872.htm`：这一串在 `.htm` 里就是这样**——
> **所以它是上游 TDC 的损坏，不是 HTML→md 转换造成的，救不回来（§11.2 ⑤）。**
> **代价写清楚：拿 `all waveform indexes` 去 raw 里搜是搜不到的，要搜坏掉的形态。**
> **这一族目前语料里共 128 篇含 `DC/DC power units`**（本页按语料数过），**本篇是其中一篇。**

> **② `鈮?` 是编码损坏（§11.2 ①），而且是**转换**坏的——`≤`。**
> 逐字（**共 4 处，落在 2 行上**）：
> ```
> On Pin Scale systems, there is only one drive edge type, which is denoted by di (1 鈮? i 鈮?8).
> ```
> ```
> On Smart Scale systems, there are two types of drive edges, denoted by fi and si (1 鈮?i 鈮?8).
> ```
> **`鈮` 是 U+922E，后面跟一个 ASCII 的 `?`（U+003F）**——
> 按 `extract/encoding-map.csv` 第 123 行，`鈮` 的反解记录是
> `原字符在 U+2240–U+227F 之间（第三字节已丢，只能给区间）`，
> **也就是说单看这一篇**，`鈮?` **只能定位到一个区间，定不到唯一一个字**。
> **但本页核过 `raw/98872.htm`：`.htm` 里写的是干净的 `(1 ≤ i ≤ 8)`（两处都是），
> 字符就是 `≤`（U+2264）**——
> **所以这个字是确定的，而且是转换时坏的（§11.2 ①：`.htm` 干净 = 能救）。**
> **两行还有一处细微差别**：第一行是 `(1 鈮? i 鈮?8)`（`鈮?` 与第二个 `i` 之间有空格），
> 第二行是 `(1 鈮?i 鈮?8)`（**没有空格**）。**本页照原样引。**

> **③ 驱动动作清单里 `D1N` 出现两遍。** 逐字（**清单在「语法 / 参数」节里，本页一个字没动**）：
> ```
> - D1N: Drive parameter 1 (DD1), no tri-state action
> - D1N: Drive parameter 2 (DD2), no tri-state action
> ```
> **第二行按规律应为 `D2N`**（**推断**，依据是同篇紧接着的 formatter 表写着
> `D1N, D2N, C1N, C2N`；**原文没有一句说明**）。**§11.1 明令不许改，本页照原样引。**

> **④ `EE2` / `WE2` 的说明写的是 `parameter 1`。** 逐字：
> ```
> - EE2: Edge compare to parameter 1 (ED2)
> ```
> ```
> - WE2: Window open with compare to parameter 1 (ED2)
> ```
> **括号里是 `ED2`，散文里却是 `parameter 1`**——
> **按上一行 `EE1: Edge compare to parameter 1 (ED1)` 的规律，这两处应是 `parameter 2`**（**推断**，
> 依据是 `EE1` / `EE2` 与 `WE1` / `WE2` 是成对的「1 配 1、2 配 2」；
> **原文没有一句说明**）。**本页照原样引。**

> **⑤ 例子里 `e1:` 进、`d1:` 出。** 第 1 行命令写的是
> `> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)`，
> 而回读出来的是 `WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)`——
> **同一个 `wfIndex`、同一个 pinlist，edge 前缀从 `e` 变成了 `d`。**
> **本篇没有解释 `e` 这个前缀**——它讲到 edge 前缀只有两处：
> 驱动侧讲的是 `di`（`On Pin Scale systems, there is only one drive edge type, which is denoted by di`），
> Smart Scale 那一句讲的是 `fi` 与 `si`；**`e` 与 `d` 的关系，本篇一个字没写**（**语料未写**）。
> ——**本页照原样引，并把它当瑕疵记下来，而不是当成「两种等价写法」。**

> **⑥ 语法行与参数表对同一个东西两种写法。** 语法行第一位写的是
> `{wvf_set|"wavetable"|specset_id|"multiport_spec"}`（**引号里是 `wavetable`**），
> 而参数表那一栏的名字是 **`wavetable_name`**（`The wavetable name. Enter a string of up to 40
> alphanumeric characters (upper or lower case) enclosed by double quotes.`）。
> **同一篇里两个名字**（**这一处在语法节里，本页一个字没动**）——**本页照原样引。**
> **另外本篇写的是 `multiport_spec`（不带连字符）**，而本页读到的 [[vclk]] / [[vtim]] 两篇写的是
> `multi-port_spec`（**带连字符**）——**三篇对同一件事的拼写不一致**（**三篇都是本页的取材**）。

> **⑦ `wfIndex` 的上限有两个数。** 参数表写 `Enter an integer between 0 and 255.`，
> 而 `## Errors` 第二条写 `The waveform index is outside the range of 0 - 256 (Pin Scale systems)`——
> **`255` 与 `256`，两处差一**（**报错那一处在「报错条件」节里，本页一个字没动**）。
> **本页两处并列照记，不替它裁定。**

> **⑧ `## Related information` 一节的两条链接首尾相连。** 逐字（按语料原来的写法）：
> ```
> [WAVE, WAVE? - (WAVEform)](<02.06.02.02.333_WAVE__WAVE__-__WAVEform.md>)[ETDS, ETDS? - (Edge Timing Definition String)](<02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md>)
> ```
> **两条之间一个分隔符都没有**——**本页照原样记（本页读到的那两个链接的 `文本` 分别是
> `WAVE, WAVE? - (WAVEform)` 与 `ETDS, ETDS? - (Edge Timing Definition String)`）。**

> **⑨ `## Warnings` 那一句末尾没有句点。** 逐字（**「报错条件」节里本页一个字没动**）：
> ```
> The timing sets belonging to the affected waveform set are modified as necessary
> ```
> **本页照原样引，不替它补句点。**

> **⑩ 坏字：本篇除上面那 4 处 `鈮?` 外，没有别的汉字。**
> 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇的汉字只有 `鈮` 这 4 个**——**但这是「本页读到的」，不是「本篇只有这些」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
