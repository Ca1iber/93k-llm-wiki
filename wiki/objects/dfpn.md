---
type: object
title: DFPN, DFPN? - (DeFine Pin Name)
layer: L1
stage: pin
tags: [pin, dfpn, pin-configuration, ganging, channel, sequencer, dc-scale]
related: [pin, sqst, ganging, cross-card-ganging-requires-ddic, pin-config-requires-sequencer-off, dfup]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# DFPN, DFPN? - (DeFine Pin Name)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,154 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFPN

```
DFPN ["connectionSet",] {channelNo_1|(list_of_DC_scale_channels)}, ["pinNo"], {(pinName)}
```

### DFPN?

```
DFPN? {(pinlist)}
```

returns:

```
DFPN {channelNo_1|(list_of_DC_scale_channels)}, ["pinNo"], {(pinName)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98550.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：connectionSet | This parameter is currently not used. This extra string parameter adds the ability to define several pins containing the same DC Scale channel i…
> 表内引用（2 条，供检索）：`DDIC`（raw: `02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md`） · `Pogo pin assignment - Utility pogo blocks`（raw: `../02.03_DUT_board_design_reference/02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.md`）

### Example 1

```
> DFPN 10101,"1",(Clock)
> DFPN 10102,"2",(D0)
> DFPN? (@)
< DFPN 10101,"1",(Clock)
< DFPN 10102,"2",(CD0)
```

The above example allocates the `Clock` pin to channel 10101 and allocates pin `D0` to channel 10102, and then queries these definitions. The device pin numbers allocated are 1 and 2 respectively.

```
DFPN (11901, 11902),,(vee)
```

This example defines ganging for DC Scale channels in PMU mode.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The specified channel number is not valid.
- The specified channel is not installed.
- The specified channel has already been allocate.
- The specified pin has already been defined.
- The specified pin name is already used as a group name.
- The sequencer is in RUN or BREAK state.
- Ganging is defined for DC Scale channels, and not all specified channels are DC Scale channels.

<!-- 报错节 end -->

## 是什么

**`DFPN`（DeFine Pin Name）把「一个 pin 名」绑到一个物理通道上。** 原文第一句里塞了三件事：

> The DFPN command allocates a pin name to a digital or DC Scale channel. The DC Scale channel will be in PMU mode by this allocation. The pin name is the name by which the software identifies the pin. The DFPN? query returns a list of channels and their assigned pin names.

拆开看：

| 原文分句 | 含义 |
|---|---|
| `allocates a pin name to a digital or DC Scale channel` | **做的是「通道 → 名字」的绑定**，两个方向都收：数字通道、DC Scale 通道 |
| `The DC Scale channel will be in PMU mode by this allocation.` | **副作用**：被分配到的 **DC Scale 通道会进入 PMU 模式**——**这一步不是「顺便」，是分配本身带来的** |
| `The pin name is the name by which the software identifies the pin.` | **这个名字此后就是软件认这个 pin 的唯一标识**——不是备注，是身份 |
| `The DFPN? query returns a list of channels and their assigned pin names.` | 查询侧是**反向**的：给名字，回通道 |

**第二条能力写在正文第二段，单独一句：**

> You can also configure ganging for DC Scale channels in PMU mode with DFPN.

**即：`DFPN` 不只是「一个通道一个名字」，它还是配置 DC Scale PMU ganging 的命令入口。**（下面「ganging 那一半」展开。）

**本文档的 `## Application` 段只有一行**，把它归到哪一段说清了：

> Pin Configuration, see Configuration Setup Commands.

### 一条前置条件：sequencer 必须是 OFF

**它不是 `## Before you begin` 段，是正文里紧跟着第一段的一个 `Note`：**

> Note that before you can use the DFPN command the sequencer state must be OFF (see the SQST command).

**注意这句的归属**：它和 Errors 段里的 `The sequencer is in RUN or BREAK state.` **是两种说法**——
前者说「**不许用**」，后者说「**用了会报错**」。**文档没有写明检查发生在什么时候。**
（这一层 [[pin-config-requires-sequencer-off]] 已经拆得很细，本页不重复；本页只记它确实是 `DFPN` 自己的前置条件。）

### `channelNo_1` 怎么读——两种通道、两套位数

| 通道类型 | 位数 | 拆法 |
|---|---|---|
| **数字通道** | **五位** | 前三位 = pogo block（**也叫逻辑通道板的板号**），后两位 = 块内通道号（1–16） |
| **Utility DC 通道** | **三位** | 卡笼的 **utility block** 号 |

**数字通道**（逐字）：

> For a digital channel this is a five digit number. The first three digits specify the pogo block number, and the fourth and fifth digits specify the pin number in the pogo block. The first digit is 1 to 4, the second and third digits is 01 to 32, and the final two digits is 01 to 16. For example, 10105 is the digital channel whose pogo pin number is 05 in the pogo block 101.

> Each pogo block contains 16 digital channels. The pogo block numbers are determined by the slots in which the channel boards are installed.

> The first three digits are also called the board number of the logical channel board, and the last two digits are a channel number in the logical channel board, where each logical channel board contains 16 channels

**「前三位 = 板号」这一层是**「逻辑通道板」**这个概念在命令层的落点**——
pogo block 号不是随便编的，**由通道板插在哪个槽位决定**。

**Utility DC 通道**（逐字，注意换算规则）：

> For the utility DC pins, this is a three digit number, specifying the utility block of the card cage. The referenced utility pogo must be one which can be connected to the DC rail of the card-cage. To get the utility block number, add 164 (264 for the second utility line card on EXA Scale test systems) to the desired utility line block, such that for example utility block 4 has number 168. For compatibility with SmarTest 7.6x, "HPMU1" now maps to "UTIDC165" and so on (for Smart Scale test systems only).

**换算**：utility block 号 = utility line block + **164**（EXA Scale 上第二块 utility line 卡是 **+264**）。
例：utility line block 4 → **168**。

> The hardware knows 4 Utility DC channels (pogo pins): DC-force, DC-sense, ground-sense, and guard. But because they are referenced as a group, one pin name is sufficient to reflect all 4 channels.

**所以 utility DC 这边是「四通道一名」**：一个 pin 名覆盖 force / sense / ground-sense / guard 四条。

### ganging 那一半

**入口有两个写法，差别在括号。**

**① 一次给一批通道，gang 成一个 pin**——参数 `DC_channel_list`：

> You can define ganging for a set of DC Scale channels in PMU mode by specifying a list of DC Scale channels, separated by commas and enclosed by parentheses. The channels must be physically adjacent on the same board.

> Before cross-card ganging can be used, the connection must be enabled by command DDIC.

**第二条是硬前置**：跨卡 ganging **必须先用 `DDIC` 把 DUT 板上的走线使能**。→ [[cross-card-ganging-requires-ddic]]

**② `connectionSet`——同一个通道可以出现在多个 pin 定义里**：

> This extra string parameter adds the ability to define several pins containing the same DC Scale channel in PMU mode. A multiple defined DC Scale channel can be sequentially reused as single pin or in ganging groups. Note: The documentation for supported DC Scale cards knows this feature also as "Ganging on the fly".

**允许多个 pin 共用同一个通道，但有四条附带要求**（同格内逐条写的）：

| # | 要求（原文） |
|---|---|
| 1 | `Adding a different ganging combination (new pin), does not invalidate the setups for the existing pins.` — **加新 pin 不会废掉旧 pin 的 setup** |
| 2 | `The different pins containing the same channel must be part of the same ports.` |
| 3 | `The patterns, events and DC-setups of these pins do not overlap.` |
| 4 | （`DC_channel_list` 格）`The channels must be physically adjacent on the same board.` |

**跨卡 ganging 的走线，`DDIC` 和 `DFPN` 必须写同一个 `connectionSet`：**

> All traces that are needed for a cross-card ganging group and are defined by the DDIC command and the DFPN command must have the same connectionSet defined.

**默认集合的语义**（同格）：

> Default connection set: The default connection set is defined if this extra parameter is not used or if an empty string is programmed. A DC Scale pin can be defined in only one default connection set.

**即：不写 `connectionSet`（或写空串）= 落入默认集合；而一个 DC Scale pin 只能属于一个默认集合。**

文档还有一条**命名建议**（原文自己标了 `Recommendation:`，是建议不是要求）：

> Recommendation: If the DUT trace can be activated by utility lines, name it like the utility line (see DFUP command).

### `pinNo` 与 `pinName`

> This is the device pin number which is allocated to the specified channel. The number must be enclosed in double quotes.

> The name to be allocated to the pin. Maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.

**长度上限分两档：32 位 SmarTest 是 16 个字符，64 位是 64 个。**（`Functional changes` 里 7.1.2 那一条正是把 64 位这一档放宽的结果。）

### 查询：`@` 是「全部」，查不到就**什么都不返回**

> The symbol @ can be used with the DFPN? query to list all pins previously defined by the DFPN command. If a list of more than one pin is required, the pin names must be separated by a comma. If you query a non-existent pin, the system returns nothing.

**最后半句是实用信息**：`If you query a non-existent pin, the system returns nothing.`
**——不是报错，是空。**（工程含义，推断：拿「返回为空」当「这个 pin 没定义过」的判据是成立的，
但**脚本也要能区分「空」和「命令本身失败」**；文档没有写失败时返回什么。）

### Errors 段：七条

原文是「一个总起句 + 七条」，**这里照原样引出**（含原文自己的拼写）：

> An error is generated if:
> - The specified channel number is not valid.
> - The specified channel is not installed.
> - The specified channel has already been allocate.
> - The specified pin has already been defined.
> - The specified pin name is already used as a group name.
> - The sequencer is in RUN or BREAK state.
> - Ganging is defined for DC Scale channels, and not all specified channels are DC Scale channels.

**第三条原文写的是 `allocate`，不是 `allocated`**——**引文照抄，见「出处」的 ⚠️**。

**最后一条是 ganging 的唯一一条报错**：`Ganging is defined for DC Scale channels, and not all specified channels are DC Scale channels.`
**反过来（忘了先 `DDIC`、`connectionSet` 不一致）文档没有给报错**——那两种情形见
[[cross-card-ganging-requires-ddic]] 的「违反了会怎样」，那边明写了「本次未找到」。

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。** 下面是按正文的顺序约束 + 语法 + 两个 Example 拼出来的（**哪一步是文档明写的、哪一步是本页拼的，逐条标出**）。

1. **先确认 sequencer 是 OFF**（**文档明写**：`the sequencer state must be OFF (see the SQST command)`）。
   查状态用 `SQST`。→ [[sqst]]
2. **一条通道一个名字**（`Example 1` 前半，原文代码块）：

   ```
   > DFPN 10101,"1",(Clock)
   > DFPN 10102,"2",(D0)
   ```

   原文说明：`The above example allocates the Clock pin to channel 10101 and allocates pin D0 to channel 10102`。
   **注意 pin 名要写在括号里、`pinNo` 要写在双引号里**（`pinNo` 那格：`The number must be enclosed in double quotes.`）。
3. **一批通道 gang 成一个名字**（`Example 1` 后半，原文代码块）：

   ```
   DFPN (11901, 11902),,(vee)
   ```

   原文说明：`This example defines ganging for DC Scale channels in PMU mode.`
   **注意两个逗号之间是空的——`pinNo` 位留空**，只有 `channelNo` 列表和 `pinName`。
   **跨卡**时这一步之前必须先 `DDIC`（**文档明写**）。
4. **反查**（原文代码块）：`DFPN? (@)` —— `@` 列全部，多名字用逗号分隔。

**「本页拼的」那一步只有一条顺序**：把第 1 步放在最前面。**文档给的是条件句
（`Note that before you can use the DFPN command the sequencer state must be OFF (see the SQST command).`），
不是编号流程**——**本页不把它包装成文档的流程。**

## 和谁有关

- [[sqst]] — **前置条件的检查手段**。`DFPN` 的原文自己指向它（`see the SQST command`）。
- [[pin-config-requires-sequencer-off]] — **同一条锁的汇总页**。`DFPN` 是它收的篇目之一，
  那页把「条件句 vs 报错句」两种措辞分开列了，本页不重复。
- [[ganging]] — **同类概念页**。`DFPN` 是「在命令层配 DC Scale PMU ganging」的入口；
  概念那一层（哪些卡能 gang、物理相邻要求）不在本页。
- [[cross-card-ganging-requires-ddic]] — **本页的下游约束**。跨卡 ganging 的硬前置是 `DDIC`；
  那页还收了本页 `connectionSet` 一致那条原文，并明写「忘了先 `DDIC` 没有报错描述」。
- [[pin]] — **`stage` 归属**。本页 `## Application` 段自己写的：`Pin Configuration`。
  （`stage: pin` 填的是**最近的一段**，不是归属——§6。）
- [[dfup]] — **文档点名的一条边**：`Recommendation: If the DUT trace can be activated by utility lines, name it like the utility line (see DFUP command).`
  这是 `DFPN` 的 utility DC 那边的姐妹命令。
- `DDIC`（未建页）— **跨卡 ganging 的使能命令**，本页两处指向它。
  **它不在 allowlist 里，按 §9.1 本页只写反引号**；raw：
  `02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md`。
- [[conf]] / [[pals]] / `UDEF`（本 wiki 暂无对象页）— **同一个「sequencer 必须 OFF」命令族的兄弟**；
  本页的文档**没有**提到它们，这条关系来自 [[pin-config-requires-sequencer-off]]。

## 版本

本文档有 `## Functional changes` 段，**七条，逐条转录**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.2: For 64-bit systems: Number of of characters for pinName extended.`
- `SmarTest 7.3.1: Extended for DC Scale PVI8.`
- `SmarTest 7.3.1: New extra parameter connectionSet added.`
- `SmarTest 7.4.0: Support for DC Scale AVI64 card added.`
- `SmarTest 7.5.0: Support for DC Scale FVI16 card and new extra parameters channelNo_2 and channelNo_3 added.`
- `SmarTest 7.10.2: Support for utility DC pins added`

**三条要留意：**

- **第一条是哨兵值**（§11.2 ②）：`Introduced before SmarTest 6.3.2` 的意思是
  「**在本文档集覆盖范围开始之前就已经有了**」，**不是「SmarTest 6.3.2 新增了 `DFPN`」**。
- **7.5.0 那条说加了 `channelNo_2` 和 `channelNo_3`，但本文档现在的语法和参数表里只有 `channelNo_1`。**
  语法写的是 `{channelNo_1|(list_of_DC_scale_channels)}`，参数表也只有 `channelNo_1` 一格。
  **`channelNo_2` / `channelNo_3` 在本篇里没有对应的语法位与参数说明**（见「出处」的 ⚠️）。
- **7.10.2 那条「utility DC pins」正对应正文里的 utility DC 那一节**——
  **也就是说 utility DC 三位的通道号这套写法是 7.10.2 才有的**，更早的版本上按本文档写会不对。

> 上面三条里，只有「第一条是哨兵值」是 §11.2 的通用规矩；
> **另两条是本页把版本条目与正文对起来看发现的差异，本页并列写出，不替语料调和（§10）。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`

**本页没做的：**

- **`DDIC` 的文档没读**（`02.06.02.02.54`）。所以「`DDIC` 到底怎么写、`circuitry_type` 取什么值」
  本页一个字都没有——**本页只写了「跨卡 ganging 必须先 `DDIC`」这一条前置**，
  它是从**本页的**参数表里抄的。
- **`SQST` 的文档没读**。所以「怎么读 sequencer 状态、返回值长什么样」本页没有。
- **`DFUP` 的文档没读**。本页只有正文那一句命名建议。
- **`UDEF` / `CONF` / `PALS` 的文档没读**，本页提到它们只是为了说明「同一族的锁」，
  那句话的依据在 [[pin-config-requires-sequencer-off]]，不在本页的文档里。
- **`Pogo pin assignment - Utility pogo blocks`（02.03.06.08 及其子主题）没读**——
  本页的文档把 utility block 的细节指向了它，**本页只有「+164 / +264」这一条换算**。
- **`Configuration Setup Commands`（`## Application` 段指的那篇）没读。**
- **`DFPN` 的「任务页」（`02.06.03.01.02_Assigning_a_pin_name_to_a_digital_channel.md`）没读**——
  那是另一篇文档，里面也写了一遍 sequencer 前置条件（那一条的出处见 [[pin-config-requires-sequencer-off]]）。
- **本文档没有任何图**；`## Related information` 段只有一个链接（`DDIC`）。

> ⚠️ **语料瑕疵，照实记下，一处都没替它改**：
> ① **`Example 1` 自己前后不一致。** 发出去的命令是 `> DFPN 10102,"2",(D0)`，
> 查询回来的那一行却是 `< DFPN 10102,"2",(CD0)`——**`D0` 变成了 `CD0`**；
> 而紧跟的例子说明文字写的又是 `allocates pin D0 to channel 10102`。
> **三处里两处写 `D0`、一处写 `CD0`**，原文没解释。
> ② **Errors 段第三条是 `The specified channel has already been allocate.`**——
> **`allocate` 应为 `allocated`**。上面 Errors 的引文块里**照原样抄的就是这个拼法**。
> ③ **`Functional changes` 里 7.1.2 那一条写的是 `Number of of characters`**——
> **`of` 重复了一次**。版本那一节里照原样转录。
> ④ **参数表里 `connectionSet` 那格自己前后矛盾**：
> 开头是 `This parameter is currently not used.`，紧接着同一个格子里又写它
> `adds the ability to define several pins containing the same DC Scale channel in PMU mode`。
> **本页不引用「currently not used」这一句**——raw 的参数表是**被摊平成一串单元格的**，
> **「currently not used」有可能是同一格里另一行参数**（同一现象在 `DDIC` 那篇也有，
> 判定见 [[cross-card-ganging-requires-ddic]]）。**本页按可用处理，并把矛盾照实记在这里。**
> ⑤ **`The first three digits are also called the board number of the logical channel board,
> and the last two digits are a channel number in the logical channel board,
> where each logical channel board contains 16 channels`——这一句原文末尾没有句号。**
> 引文照原样，**不替它补标点**。
> ⑥ **`Example 1` 这个标题底下其实有两个例子**（单个 pin 分配 + ganging），
> **而且没有 `Example 2`**。原文如此，本页按「前半 / 后半」称呼它们。

`verified: doc-only`——**本页没有在任何真实机台上跑过 `DFPN`**
（§11：文档里有 ≠ 这台机器上能用；尤其 `channelNo_1` 的位数规则与 utility block 换算，
**动手前先照实机核对**）。
