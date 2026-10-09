---
type: object
title: CHIN? - (CHannel INformation)
layer: L1
stage: pin
tags: [chin, l1, firmware-command, pin, query-command, channel-information, hardware-control, channel-type, phys-location, board]
related: [pin, command-reference, dfpn, dfps, ps1600, ps5000, dps128-dps64-cards, dc-scale-xps256-card, dc-scale-uhc4t-card, smartest-7.10.2, smartest-7.10.3]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# CHIN? - (CHannel INformation)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,598 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
CHIN? {channel_nr|ALL}
```

returns:

CHIN {channel_nr}, {channel_type}, [phys_location], {board_no}, [clk_board], [chan_info_1], [chan_info_2]

### Parameters

| channel_nr | The number that identifies the channel.<br><br>Specify ALL if you want information about all channels.<br><br>For a digital channel, specify it with the test system channel number, which is five digits (see `DFPN, DFPN? - (DeFine Pin Name) for the number)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）.<br><br>For a DPS channel, specify it with the test system channel number, which is two digits (see `DFPS, DFPS? - (DeFine Power Supply)`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） for the number). | The number that identifies the channel.<br><br>Specify ALL if you want information about all channels.<br><br>For a digital channel, specify it with the test system channel number, which is five digits (see `DFPN, DFPN? - (DeFine Pin Name) for the number)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）.<br><br>For a DPS channel, specify it with the test system channel number, which is two digits (see `DFPS, DFPS? - (DeFine Power Supply)`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） for the number). |
|---|---|---|
| channel_type | Returns the type of the channel. It can be: | Returns the type of the channel. It can be: |
| channel_type | CPIO | Pin Scale 1600 digital channel |
| channel_type | PYIO | Pin Scale 5000 digital channel |
| channel_type | WZ_FDIFF_I | Fast differential input channel |
| channel_type | WZ_FDIFF_O | Fast differential output channel |
| channel_type | PPS | Precision Parallel Source channel |
| channel_type | HVP | High Voltage PMU |
| channel_type | DPS128HC | DC Scale DPS128-HC or DPS64-HC |
| channel_type | XPS256 | DC Scale XPS256 |
| channel_type | UHC4T | DC Scale UHC4T |
| phys_location | The channel's physical location.<br><br>NOTE: For PS1600 and DPS128 SmarTest returns always "-1"!<br><br>This format is TCSSPP.<br><br>Where: | The channel's physical location.<br><br>NOTE: For PS1600 and DPS128 SmarTest returns always "-1"!<br><br>This format is TCSSPP.<br><br>Where: |
| phys_location | T | test head (1) |
| phys_location | C | card cage (1 - 8) |
| phys_location | SS | slot (01 - 18) in the card cage |
| phys_location | PP | hardware pin number of the digital channel<br><br>For DPS, this is the channel number in the DPS board. |
| board_no | Board number of the board to which the channel belongs. For the DPS, this is the DPS board number. For details, see the board_no parameter in `*OPT? - (hardware OPTions)`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md`）. | Board number of the board to which the channel belongs. For the DPS, this is the DPS board number. For details, see the board_no parameter in `*OPT? - (hardware OPTions)`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md`）. |
| clk_board | Board number of the clock board in the card cage to which the channel belongs. | Board number of the clock board in the card cage to which the channel belongs. |
| chan_info_1 | First information of the channel. | First information of the channel. |
| chan_info_1 | For digital channels:<br><br>Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors).<br><br>DC Scale DPS channels behave like a digital channel and return the sequencer memory depth. | For digital channels:<br><br>Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors).<br><br>DC Scale DPS channels behave like a digital channel and return the sequencer memory depth. |
| chan_info_1 | For PPS channels:<br><br>Pattern memory depth in blocks of 1k words (16 bit). | For PPS channels:<br><br>Pattern memory depth in blocks of 1k words (16 bit). |
| chan_info_1 | For HVP channels:<br><br>DAC/ADC RAM depth in blocks of 1k words (16 bit). | For HVP channels:<br><br>DAC/ADC RAM depth in blocks of 1k words (16 bit). |
| chan_info_2 | Second information of the channel. | Second information of the channel. |
| chan_info_2 | For digital channels:<br><br>Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors). | For digital channels:<br><br>Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors). |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98502.htm`。

### Examples

```
CHIN? 10901
```

returns:

```
CHIN 10901,PSIO,120601,109,21,512,0
```

```
CHIN? ALL
```

  Return (for example):

```
CHIN 10101,PYIO,110301,101,11,3551,0
CHIN 10102,PYIO,110302,101,11,3551,0

CHIN 21701,DPS128HC,-1,217,31,191,0
CHIN 21702,DPS128HC,-1,217,31,191,0

```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if a wrong value is given for channel_nr.

<!-- 报错节 end -->

## 是什么

**`CHIN?`（CHannel INformation）是一条查询命令：把一条通道的信息报回来。** 原文第一句：

> 「The CHIN? (CHannel INformation) query returns information on a specified channel or on
> all channels. A result is returned for each individual pin.」

| 要点 | 原文 | 读出来是什么 |
|---|---|---|
| 是查询 | 命令名带 `?`；标题写 `CHIN? - (CHannel INformation)` | **只有查询形态**——本篇没有无问号的 `CHIN` 定义命令 |
| 输入 | `on a specified channel or on all channels` | **一条通道**，或 `ALL` |
| **输出粒度** | **`A result is returned for each individual pin.`** | **每个 pin 一行**——这就是 `CHIN? ALL` 会印出一串行的原因 |

**所以 `ALL` 不是「汇总成一条」，是「逐条列出来」。**
（**这是一句原文的直接结论，不是推断**：`A result is returned for each individual pin.`）

### 返回的七个字段，以及两种括号

原文的返回模板（逐字）：

```
CHIN {channel_nr}, {channel_type}, [phys_location], {board_no}, [clk_board], [chan_info_1], [chan_info_2]
```

**注意命令与应答的写法不同**：你发的是 **`CHIN?`（带问号）**，
回来的那一行以 **`CHIN`（不带问号）** 开头——和 `VPIN?` 那族的习惯一样。
**本篇没有解释这件事**（**语料未写**）。

| 字段 | 括号 | 逐字的说明 |
|---|---|---|
| `channel_nr` | `{}` | `The number that identifies the channel.` |
| `channel_type` | `{}` | `Returns the type of the channel. It can be:` |
| `phys_location` | **`[]`** | `The channel's physical location.` |
| `board_no` | `{}` | `Board number of the board to which the channel belongs.` |
| `clk_board` | **`[]`** | `Board number of the clock board in the card cage to which the channel belongs.` |
| `chan_info_1` | **`[]`** | `First information of the channel.` |
| `chan_info_2` | **`[]`** | `Second information of the channel.` |

**`{}` 与 `[]` 的分工，原文没有符号说明表**——**按返回值去读（推断）**：
**带 `[]` 的四个，正好是「可以退化成 `-1` 或 `0`」的那四个**。
依据是下面两张例子的返回值：`phys_location` 在 DPS 那两行是 `-1`（原文的 NOTE 也点了这件事），
而 `chan_info_2` **在四条例子里全是 `0`**；带 `{}` 的两个（`channel_nr` / `board_no`）
在全部例子里都是有意义的非零值。**这一步是本页的推断，不是文档事实。**

### 输入 `channel_nr`：数字通道五位、DPS 两位

| 通道种类 | 位数 | 逐字 |
|---|---|---|
| **数字通道** | **五位** | `For a digital channel, specify it with the test system channel number, which is five digits (see DFPN, DFPN? - (DeFine Pin Name) for the number).` |
| **DPS 通道** | **两位** | `For a DPS channel, specify it with the test system channel number, which is two digits (see DFPS, DFPS? - (DeFine Power Supply) for the number).` |
| **全部通道** | — | `Specify ALL if you want information about all channels.` |

**两处都把「号从哪来」推给了别处**：数字通道 → [[dfpn]]，DPS → [[dfps]]。
**「`channel_nr` 的取值范围是多少」本篇没有给**——报错条件只说
`An error is generated if a wrong value is given for channel_nr.`（**错的值是什么算错，本篇没有定义**）。

> ⚠️ **「两位」这一句与 `CHIN? ALL` 的例子对不上，这是本页最要紧的一处。**
> 原文说 DPS 通道的 `channel_nr` 是 `two digits`，
> **而 `CHIN? ALL` 的例子把 DPS128HC 通道返回成五位数**——
> 逐字：`CHIN 21701,DPS128HC,-1,217,31,191,0`（**`21701`**）与 `CHIN 21702,DPS128HC,-1,217,31,191,0`。
> **两处说的是不是同一个数（一个讲输入怎么写、一个讲返回怎么写），原文没有写。**
> **本页并列两处，不替它调和**（§11.2 / §10：两种说法并列、各自附出处）。
> **但有一件事是确定的**：**拿 `21701` 这个五位形态去当 DPS 的输入，
> 与 `which is two digits` 那句对不上。**

### `channel_type`：正文列了九个取值

> 「Returns the type of the channel. It can be:」

| 取值 | 逐字说明 |
|---|---|
| `CPIO` | `Pin Scale 1600 digital channel` |
| `PYIO` | `Pin Scale 5000 digital channel` |
| `WZ_FDIFF_I` | `Fast differential input channel` |
| `WZ_FDIFF_O` | `Fast differential output channel` |
| `PPS` | `Precision Parallel Source channel` |
| `HVP` | `High Voltage PMU` |
| `DPS128HC` | `DC Scale DPS128-HC or DPS64-HC` |
| `XPS256` | `DC Scale XPS256` |
| `UHC4T` | `DC Scale UHC4T` |

> ⚠️ **而 `CHIN? 10901` 那条例子返回的 `channel_type` 是 `PSIO`——不在上面九个里。**
> 逐字：`CHIN 10901,PSIO,120601,109,21,512,0`。
> **九个取值里离它最近的是 `CPIO`（同为 `Pin Scale 1600` 那一档的样子），
> 但原文没有说这两个是同一个东西的两种拼法。**
> **核过上游 `raw/98502.htm`：例子写的就是 `PSIO`、类型表写的就是 `CPIO`**（§11.2 ⑥）——
> **上游就是这样，不是转换坏的。本页不判。**
>
> **实操后果（本页的提醒，不是原文的话）**：**拿 `CPIO` 去判「这条通道是不是 Pin Scale 1600」
> 会漏掉例子里那种写法**；**该判哪些拼法等价，本篇没写。**

### `phys_location`：`TCSSPP` 六位，以及那条 NOTE

> 「This format is TCSSPP.」

| 位 | 逐字 |
|---|---|
| `T` | `test head (1)` |
| `C` | `card cage (1 - 8)` |
| `SS` | `slot (01 - 18) in the card cage` |
| `PP` | `hardware pin number of the digital channel` / `For DPS, this is the channel number in the DPS board.` |

> 「NOTE: For PS1600 and DPS128 SmarTest returns always "-1"!」

**这条 NOTE 在 DPS 那两条例子上成立**：`CHIN 21701,DPS128HC,-1,...` 里 `phys_location` 就是 `-1`。
**而 PS1600 那一半本篇核不了**：例子那条的类型是 `PSIO`，而 `PSIO` 不在类型表里（见上），
**所以「例子那条是不是 PS1600」本篇答不了。**

**另一个值得记的点**：**`-1` 不符合 `TCSSPP` 这个格式**——
`TCSSPP` 是六位，`-1` 是两位。
**所以「`TCSSPP`」只在这条通道真的有物理位置时成立**；
**拿 `-1` 去按 `TCSSPP` 拆位会拆出无意义的结果。**
（**这是本页按格式定义与例子并列后的读法，原文没有正面说这句话。**）

### `board_no` / `clk_board` / `chan_info_1` / `chan_info_2`

| 字段 | 逐字 | 备注 |
|---|---|---|
| `board_no` | `Board number of the board to which the channel belongs. For the DPS, this is the DPS board number. For details, see the board_no parameter in *OPT? - (hardware OPTions).` | **详情推给了 `*OPT?`**（本页没读） |
| `clk_board` | `Board number of the clock board in the card cage to which the channel belongs.` | — |
| `chan_info_1` | `First information of the channel.` | 见下面那张「按通道种类分」的表 |
| `chan_info_2` | `Second information of the channel.` | **⚠️ 见下** |

**`chan_info_1` 的含义按通道种类分三档**（原文逐字）：

| 通道种类 | 逐字 |
|---|---|
| **数字通道** | `Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors).` |
| **DC Scale DPS 通道** | `DC Scale DPS channels behave like a digital channel and return the sequencer memory depth.`（**所以 DPS 那一格也是 sequencer 深度**） |
| **PPS 通道** | `Pattern memory depth in blocks of 1k words (16 bit).` |
| **HVP 通道** | `DAC/ADC RAM depth in blocks of 1k words (16 bit).` |

**也就是说 `chan_info_1` 这一格的「单位」随通道种类变**：
数字通道与 DPS 是 **128k vectors / 块**，PPS 与 HVP 是 **1k words (16 bit) / 块**。
**跨通道种类直接比这两个数是没有意义的**——
**上面「语法 / 参数」节里那一格只写了一句数字通道的，另外三档散在压平的表里**（见「出处」⚠️ ⑤）。

**`chan_info_2` 那一格，原文写的是和 `chan_info_1` 数字通道部分逐字相同的一句话**：

> 「For digital channels: Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors).」

**即：`chan_info_1` 与 `chan_info_2` 两格对「数字通道」的说明一字不差，
而 `chan_info_2` 没有 PPS / HVP / DPS 三档。**
**核过上游 `raw/98502.htm`：htm 里两处就是同一句话**（§11.2 ⑥）——
**上游如此，不是压平造成的。**
**「那 `chan_info_2` 到底区别于 `chan_info_1` 在哪」，本篇答不了**——
**四条例子里 `chan_info_2` 全是 `0`，也帮不上忙。**

### 把五条例子的返回值摆在一起看

原文 `## Examples` 一共两段、给出五行返回（`CHIN? 10901` 一行，`CHIN? ALL` 四行）：

| 返回行（逐字） | 类型 | channel_nr | phys_location | board_no | clk_board | chan_info_1 | chan_info_2 |
|---|---|---|---|---|---|---|---|
| `CHIN 10901,PSIO,120601,109,21,512,0` | `PSIO` | 10901 | 120601 | 109 | 21 | 512 | **0** |
| `CHIN 10101,PYIO,110301,101,11,3551,0` | `PYIO` | 10101 | 110301 | 101 | 11 | 3551 | **0** |
| `CHIN 10102,PYIO,110302,101,11,3551,0` | `PYIO` | 10102 | 110302 | 101 | 11 | 3551 | **0** |
| `CHIN 21701,DPS128HC,-1,217,31,191,0` | `DPS128HC` | 21701 | **-1** | 217 | 31 | 191 | **0** |
| `CHIN 21702,DPS128HC,-1,217,31,191,0` | `DPS128HC` | 21702 | **-1** | 217 | 31 | 191 | **0** |

**从这五行能读出来的规律（推断，原文没有写这几条）**：

| 规律 | 依据 |
|---|---|
| **数字通道的 `channel_nr` 前三位 = `board_no`** | 10901→109、10101→101、10102→101（**三条全中**） |
| **数字通道的 `channel_nr` 后两位 = `phys_location` 的 `PP`** | 10901 的 `01` 对 `120601` 的 `PP=01`；10101 的 `01` 对 `110301` 的 `PP=01`；10102 的 `02` 对 `110302` 的 `PP=02`（**三条全中**） |
| **`chan_info_2` 与 `clk_board` 都不区分通道类型**（数字通道与 DPS 都给得出，DPS 的 `clk_board` 是 `31`） | 见上表 |
| **`chan_info_1` 只有量纲相同才可比**：PSIO 512、PYIO 3551、DPS128HC 191 **都是「128k vectors 的块数」** | 原文那三档说明（数字 + DPS 同一档） |

**再往下算一步的那条（推断，算式是本页写的）**：
按 `128k vectors / 块` 换算，`512` 块 = **67,108,864** 个 vectors（正好 64M），
`3551` 块 = **465,436,672**，`191` 块 = **25,034,752**。
**本页列出这三个数只是为了把口径说明白**——
**原文一条换算例子都没给，`3551` 这种非整数倍的数原文也没有解释。**

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法全部来自 `## Examples` 两段、`## Parameters` 那张（压平的）表、以及正文第一句。

```
① 先确定你要问哪条通道
   ├ 数字通道 → 五位号（号从 DFPN 来）      ← 依据：channel_nr 那格
   └ DPS 通道 → 两位号（号从 DFPS 来）      ← 依据：同上
② CHIN? <号>        或   CHIN? ALL
③ 一行一个 pin 读回来（七个字段）
```

| 要做的事 | 怎么写 | 依据 |
|---|---|---|
| **查一条通道** | `CHIN? 10901` | `## Examples` 第 1 段 |
| **查全部通道** | `CHIN? ALL` | `## Examples` 第 2 段 |
| 读返回那一行的七个字段 | 按上面「返回的七个字段」那张表对位 | `## Syntax` 的 returns 模板 |
| 判通道类型 | 看 `channel_type`——**注意 `PSIO` 不在类型表里**（见「是什么」⚠️） | `## Parameters` 的 `channel_type` 格 + 例子 |
| 判物理位置 | `phys_location`——**DPS 会给 `-1`，那时它不合 `TCSSPP` 格式** | 原文的 NOTE + 例子 |
| **判号和板子的对应** | `channel_nr` 前三位 ↔ `board_no`、后两位 ↔ `PP`（**推断**） | 上面那张规律表（本页从例子里读出来的） |
| 查 `board_no` 的详情 | **看 `*OPT?`**——本篇把这件事推给了它 | `For details, see the board_no parameter in *OPT? - (hardware OPTions).` |
| 判某条通道有没有被定义 / 号从哪来 | **看 [[dfpn]] / [[dfps]]** | `channel_nr` 那格两次点名它们 |
| **改动通道配置** | **不是本命令的事**——`CHIN?` 是只读的 | 命令名带 `?`、`## Errors` 只有「值给错」一条 |

**三条容易踩的约束**：

1. **位数要对**：数字通道五位、DPS 两位（**而 DPS 那条例外见「是什么」的 ⚠️**）。
2. **`ALL` 是逐条列、不是汇总**（`A result is returned for each individual pin.`）——
   **问 `ALL` 之前先想好输出量**，原文没有给任何过滤手段。
3. **`chan_info_1` 的单位随通道种类变**（128k vectors/块 vs 1k words/块）——
   **跨类型比这个数没有意义**。

**归属**：原文 `## Application` 一节只有两个字——`Hardware control.`
**⚠️ 和同族的 `UDEF` / `VPIN` 不同，这一节在本篇里没有任何链接**——
**所以「硬件控制」是**哪一篇、在哪一章，本篇没有说。**
**这一句（连同文档本身在 `02.06_Command_Reference` 下）是 [[pin]] 与 [[command-reference]]
两个 `related` 的依据。**

**出错时**：**本篇 `## Errors` 只有一条**——
`An error is generated if a wrong value is given for channel_nr.`
**本篇没有 `## Warnings` 段**（已核：0 命中）。
**注意这条报错只说 `channel_nr` 给错会报错，没说报什么、也没说取值范围是什么。**

## 和谁有关

- [[pin]] / [[command-reference]] —— **归属**：`stage: pin` 的依据是 `## Application`
  的 `Hardware control.`（**这一节没有链接**）；文档本身在 `02.06_Command_Reference` 下。
  （§6：`stage` 填的是**最近的一段**，不是归属。）
- [[dfpn]] —— **上游，原文点名**：数字通道那五位号从 `DFPN` 来。
  逐字：`For a digital channel, specify it with the test system channel number, which is five digits
  (see DFPN, DFPN? - (DeFine Pin Name) for the number).`
  **关系是「本页消费它定义出来的号」**——**`DFPN` 的语法本页没有。**
- [[dfps]] —— **上游，原文点名**：DPS 那两位号从 `DFPS` 来。逐字见上（`For a DPS channel, …`）。
- `*OPT? - (hardware OPTions)`（**未建**）—— **`board_no` 的详情在那里**
  （`For details, see the board_no parameter in *OPT? - (hardware OPTions).`），
  而且它也是本页 `## Related information` **唯一点名的一篇**。**本页没读。**
- [[ps1600]] / [[ps5000]] / [[dps128-dps64-cards]] / [[dc-scale-xps256-card]] / [[dc-scale-uhc4t-card]] ——
  **`channel_type` 取值背后的卡**。对应关系是**取值说明里逐字写着的**：
  `CPIO` → `Pin Scale 1600 digital channel`、`PYIO` → `Pin Scale 5000 digital channel`、
  `DPS128HC` → `DC Scale DPS128-HC or DPS64-HC`、`XPS256` → `DC Scale XPS256`、
  `UHC4T` → `DC Scale UHC4T`。
  **即：本页是「用命令行判这块卡在不在」的入口。**（那五页本页没读。）
- [[smartest-6.3.2]] / [[smartest-7.10.2]] / [[smartest-7.10.3]] —— **版本页**。
  **实测 `grep`：`wiki/versions/` 下共 12 页的 `sources:` 里含本篇的 rel 路径**
  （`smartest-6.3.2`、`6.5.0`、`7.1.0`、`7.1.3`、`7.2.0`、`7.2.1`、`7.3.1`、`7.3.2`、
  `7.4.0`、`7.5.0`、`7.10.1`、`7.10.2`）——**正好对应本篇版本段里 12 条带版本号的条目**。
  **关系是「本页是那些版本页条目的来源之一」**（§6.1 说的 `sources:` 的第二个含义）。
  [[smartest-6.3.2]] 对应那条 `New value LPN`，[[smartest-7.10.2]] 对应最后一条 `New card PS5000`。
- [[smartest-7.10.3]] —— 本 wiki 面向的版本；**本篇的版本段停在 7.10.2**（见「版本」④）。
- `WZ_FDIFF_I` / `WZ_FDIFF_O` / `PPS` / `HVP` —— **`channel_type` 里另外四个取值，
  它们背后没有能对上的卡页**（`Fast differential input/output` / `Precision Parallel Source` /
  `High Voltage PMU`）。**本页不硬凑链接**（§9.1：只链会存在的页）。
- `PSIO` —— **只出现在例子里，不在类型表里**（见「是什么」⚠️）。**本页不为它建任何关系。**

> **本页的 `（推断）` 有三处**：`{}` / `[]` 的分工、「`channel_nr` 前三位 = `board_no`、
> 后两位 = `PP`」那两条规律、以及 `chan_info_1` 的块数换算。
> **三处的依据都写在句子里，而且都是从例子的返回值读出来的**——**原文一条都没写。**
> **其余每条都能在本篇里指到原句。**

## 版本

本文档**有** `## Functional changes` 段，**13 条，逐字**：

| 条目 | 和正文对得上吗 |
|---|---|
| `Introduced before SmarTest 6.3.2` | **是 §11.2 ② 的哨兵值**，见下① |
| `SmarTest 6.3.2: New value LPN for the channel_type result element` | **⚠️ `LPN` 不在正文的类型表里**，见下② |
| `SmarTest 6.5.0: Extended for DC Scale UHC4` | **正文写的是 `UHC4T`**，见下② |
| `SmarTest 7.1.0: New card PS1600` | 正文无 `PS1600` 这个取值，见下③ |
| `SmarTest 7.1.3: Support of MBAV8+` | **不是一个卡名**，见下③ |
| `SmarTest 7.2.0: New card PS1600ME` | 同上 |
| `SmarTest 7.2.1: New card DPS128` | 正文取值是 `DPS128HC`，见下③ |
| `SmarTest 7.3.1: New card PVI8` | 同上 |
| `SmarTest 7.3.2: New card UHC4T` | **对得上**（正文有 `UHC4T`） |
| `SmarTest 7.4.0: New card AVI64` | 见下③ |
| `SmarTest 7.5.0: New card FVI16` | 见下③ |
| `SmarTest 7.10.1: New card XPS256` | **对得上**（正文有 `XPS256`） |
| `SmarTest 7.10.2: New card PS5000` | **对得上**（`PYIO` = `Pin Scale 5000 digital channel`） |

**① `Introduced before SmarTest 6.3.2` 不是「6.3.2 的变更」。**
按 §11.2 ②，它是「**早于本文档集覆盖范围**」的哨兵——
**所以 `CHIN?` 究竟成立于哪个版本，这份语料里没有。**

**② 版本段点名了两个正文里找不到的取值。**
`LPN` 逐字：`SmarTest 6.3.2: New value LPN for the channel_type result element`
——**而正文的 `channel_type` 表里九个取值没有 `LPN`**（已核：`LPN` 在本篇正文里
只出现在这一条版本记录中）。
`UHC4` 逐字：`SmarTest 6.5.0: Extended for DC Scale UHC4`
——**正文写的是 `UHC4T`（`DC Scale UHC4T`），版本段写的是 `UHC4`**，
**两者是不是同一块卡的两种写法，原文没说，本页不判。**
**⚠️ 后果：拿版本段去反推「`channel_type` 有哪些取值」会多出 `LPN` 这个正文没有的值。**

**③ 版本段点名了 13 张卡/特性，而正文的 `channel_type` 表只列 9 个取值。**
**两边的名字对不上的有五个**：`PS1600ME`（7.2.0）、`PVI8`（7.3.1）、`AVI64`（7.4.0）、
`FVI16`（7.5.0），以及 `MBAV8+`（7.1.3，**它不是「New card」，是「Support of」**）。
**另外三个名字也只是近似对应**：`PS1600` ↔ `CPIO`、`DPS128` ↔ `DPS128HC`、`PS5000` ↔ `PYIO`
（**这三条对应关系是本页从名字对出来的（推断），正文没有写这张对应表**）。

> **所以「某张卡在不在」这个问题，本篇给不出完整答案**：
> **正文的类型表是九个取值，版本段是十三个条目，两边没有一张对照表。**
> **本页把两边都原样列出来，不替它们合成第三张表。**

**④ 与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
**而这一篇的版本段停在 7.10.2**——**所以 7.10.2 之后 `CHIN?` 有没有变过、有没有新卡，语料里没有。**
**本页写的全部是 7.10.2 时点的说法。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.md`
（TDC `98502.htm`；**md 5,948 字节 / 276 行**，上游 htm 11,096 字节）。**整篇读完。**

**本页没做的**：

- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4）。
- **`*OPT?` 没读**——`board_no` 的详情与 `## Related information` 都指向它。
  **所以「板号怎么解释、一块板上有什么」本页没有。**
- **[[dfpn]] / [[dfps]] 的原文没读**——**所以「那五位 / 两位号是怎么定出来的、
  取值范围是多少」本页一个字没有**；本页只有本篇点名它们的那两句。
- **版本段里那五张在正文中无对应的卡（`PS1600ME` / `PVI8` / `AVI64` / `FVI16`）的文档没读**——
  **所以它们对应的 `channel_type` 是什么，本页答不了。**（§11.2 ② 的哨兵值那条处置。）
- **没有 `## Warnings` 段**（已核，0 命中），只有 `## Errors` 一条。
  **脚本那条报错节的抬头写的是 `## Errors` / `## Warnings` 两个段名——
  对本篇来说 `## Warnings` 是空的。**
- **`chan_info_2` 到底区别于 `chan_info_1` 在哪，本篇没有写**（两格说明逐字相同，见「是什么」）——
  **本页不拿别处的文档补这一块。**
- **`PSIO` 与 `CPIO` 是不是同一个类型，本篇没有写**——**本页不判。**
- **没有实跑。** 没有在机台上发过 `CHIN?` / `CHIN? ALL`、
  没有核对过任何一条通道的 `board_no` / `phys_location` / `chan_info_1`，
  **也没有验证过「DPS 通道到底该发两位还是五位」**（那正是本篇自相矛盾处）。
  `verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**（§11.2）。
> **本篇 md 的 CJK 字符数实测为 0**——**没有 §11.2 ① 那一族编码乱码。**
> **下面五条全部核过上游 `raw/98502.htm`：五条在 htm 里就是这样**——
> **所以这一族是 §11.2 ⑥ 那一类（上游就坏的），不是转换坏字，重做转换也救不回来。**
>
> **① `PSIO`（例子）对 `CPIO`（类型表）。** 逐字两处：
> `CHIN 10901,PSIO,120601,109,21,512,0`（`## Examples`）
> 对 `CPIO` / `Pin Scale 1600 digital channel`（`## Parameters` 的类型表）。
> **`PSIO` 在整篇里只出现这一次**（实测：类型表九个取值 + 版本段十三条，都没有 `PSIO`）。
> **本页不判这两者是不是同一个东西。**
>
> **② 版本段点名的 `LPN` 在正文类型表里不存在。** 逐字：
> `SmarTest 6.3.2: New value LPN for the channel_type result element`
> ——**而 `## Parameters` 那张类型表只有九个取值，没有 `LPN`。**
> **本篇没有解释这个值是什么时候、为什么从表里消失的**（或从来没进过表）。
>
> **③ `chan_info_2` 的说明与 `chan_info_1` 数字通道那一档逐字相同。** 逐字两处：
> `chan_info_1` 下的 `For digital channels: Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors).`
> 对 `chan_info_2` 下的**同一句**。
> **两处在本篇 raw 里就是同一个字符串**（实测 htm 里 `Sequencer memory` 出现 **2 次**，
> 两次的上下文分别是 `First information of the channel.` 与 `Second information of the channel.`）——
> **上游就是这样。本页照原样引，不替它改。**
>
> **④ DPS 的「两位」与 `CHIN? ALL` 例子的五位数对不上。** 逐字两处：
> `For a DPS channel, specify it with the test system channel number, which is two digits`
> 对 `CHIN 21701,DPS128HC,-1,217,31,191,0`（**DPS128HC 通道，号是五位**）。
> **两处都核过 htm，都是上游原文。**
> **本页并列，不替它调和**（这一条正是上面「是什么」里那个大 ⚠️）。
>
> **⑤ `## Parameters` 那张大表在 raw 里被压平，而且夹杂着空单元格。**
> 逐字（本篇 `## Parameters` 起头的**完整原文**）：
> ```
> ## Parameters
>
>  |
>
> channel_nr
>
>  |
>
> The number that identifies the channel.
>
> Specify ALL if you want information about all channels.
> …
>  |
>  |
>
> channel_type
> …
> ```
> ——**每一格独占一行，中间夹着孤立的 ` | `，而且有两行连续的空格 + ` | `（` | ` 后面紧跟一个只有 ` | ` 的行）**。
> **「语法 / 参数」节里那些孤零零的 ` | ` 就是它**（同批的 [[dfut]] / [[dfpr]] / [[pslv]] 同一形态）。
> **`chan_info_1` 的三档（数字 / PPS / HVP）与 `chan_info_2` 的一档也散在这些游离的 ` | ` 之间**——
> **说明文字一个字没丢**（上表已逐字收全），**但 `PPS` / `HVP` 那两档在脚本的语法节里
> 是和 `chan_info_1` 分开的段落**，要按通道种类读得对着看。
> **另外，本篇 raw 里没有表头行**（没有 `Parameter` / `Description` 之类）。
>
> **⑥ `## Application` 一节只有两个词、且没有链接。** 逐字：`Hardware control.`
> ——**同族的 `UDEF` / `VPIN` 那一节都带一个指向别处的链接**，
> **本篇这一节什么都没给**（这是事实陈述，不是缺陷指控）。
>
> **⑦ 同一篇文档在语料里投放了两份，本页只用了其中一份。**
> 另一份是 `02.06_Command_Reference/02.06.03.02.01_CHIN__-__CHannel_INformation.md`
> （`source_topic: "98502_2.htm"`，**5,952 字节**）。
> **实测 `diff`：两份正文逐行完全相同，差别只有 frontmatter 的第 3、4 行
> （`source_topic` / `source_html`）**。
> **两份上游也各有一个 `.htm`，而且 `cmp` 报 `98502.htm` 与 `98502_2.htm` 完全一致**
> （都是 11,096 字节）——**所以这是上游 TDC 就有的重复投放，不是转换产生的**（§11.2 ⑥ 的判法）。
> **本页的 `sources:` 用的是 `02.06.02.02.22` 那一份**；
> **另一份的内容本页没有另读一遍**（因为实测正文相同）。
> **⚠️ 而 `wiki/stages/pin.md` 的 `sources:` 列的是 `02.06.03.02.01` 那一份**——
> **两页指向同一篇文档的两份投放。这是语料的结构，不是谁引错了。**
> （同批的 [[udef]] 也是同一情形，只是方向相反：那一页 wiki 与 `stages/pin.md` 引的是同一份。）

`verified: doc-only`
