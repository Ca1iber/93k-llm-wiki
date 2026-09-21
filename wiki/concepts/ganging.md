---
type: concept
title: Ganging utility blocks
layer: n/a
stage: pin
tags: [concept, ganging, utility-lines, sequencer, dut-board]
related: [sequencer-controlled-utility-lines, utility-line-assignments, utility-card, cross-card-ganging-requires-ddic]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.03_Ganging_utility_blocks.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Ganging utility blocks

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**ganging（串接）就是把多个 utility block 的串行接口级联起来，让一个串行接口驱动不止一个 block。** 原文第一句：

> 「A serial interface for sequencer-controlled utility lines can handle the data stream for more than one utility block. This cascading of serial interfaces of utility blocks is called "ganging" in the context of the sequencer-controlled utility lines.」

**注意术语的落点**：原文特意加了 `in the context of the sequencer-controlled utility lines`——
**`ganging` 这个词只在「受 sequencer 控制的 utility line」这个语境里成立。**
（**下一节 `## 和谁有关` 会用到这一点**：本 wiki 里另有一个名字带 ganging 的页，讲的是别的东西。）

### 先确认适用性：原文的 `Note` 圈了范围，并且排除了一个情形

原文先给一条 `Note`，再给一句排除说明。**合起来是这样一张表：**

| 系统 | SmarTest | 是否在本文范围内 |
|---|---|---|
| V93000 Pin Scale | SmarTest 7 | **是** |
| V93000 Smart Scale | SmarTest 7 | **是** |
| V93000 Pin Scale | SmarTest 8 | **是** |
| V93000 Smart Scale | SmarTest 8 | **是** |
| V93000 EXA Scale（装 `optional Utility Card`） | SmarTest 7 | **是** |
| V93000 EXA Scale（装 `optional Utility Card`） | SmarTest 8 | **不是** |

**排除的理由原文写得很清楚：**

> 「On V93000 EXA Scale systems running SmarTest 8 and equipped with the optional Utility Card, the pattern sequencer controls utility lines via an internal data path.」

**即：那种机器上走的是内部数据通路，压根没有「级联串行接口」这回事**——
**所以不是「不支持 ganging」，而是「不需要 ganging」。**
**原文没有说这种机器上还能不能配出等价的效果**，本页不替它推。

### 六条规则（原文逐条给）

> 「The following rules are to be considered for ganging utility blocks:」

| # | 原文 | 要点 |
|---|---|---|
| 1 | `The ganged utility blocks must be contiguous.` | **必须连续** |
| 2 | `Up to eight pogo blocks can be controlled by a single serial interface.` | **一个串行接口上限 8 个 pogo block** |
| 3 | `The block with the lowest number becomes the master.` | **号最小的那块当 master** |
| 4 | `Only the serial interface pins on the master must be connected to the digital pins that you will be using to supply the control signals.` | **只接 master 的接口引脚** |
| 5 | `The interface pins of the slave utility blocks must be left floating. The required connections for ganging the slave blocks are routed internally.` | **slave 引脚必须悬空**；内部已经连好 |
| 6 | （EXA Scale + SmarTest 7 + 多于一块 `optional Utility Card`）`ganging utility blocks across Utility cards is not supported.` | **跨 Utility Card 串接不支持** |

**第 3 条与第 4 条合起来是一条硬约束**：**你只能从「号最小的那块」往外接线**——
**接线位置本身就决定了谁是 master，没有第二个选择。**

**第 1 条在下面「怎么定义」那里又出现了一次**（SmarTest 8 那条要求 `minimum two contiguous utility pogo blocks`）。

### 数据是怎么过去的：先进硬件寄存器，再并行发出去

> 「The serially transferred data are internally stored in a hardware register and transferred in parallel to all utility lines of the controlled group of ganged blocks:」

| # | 原文 | 含义 |
|---|---|---|
| 1 | `Utility lines are not toggled while the data are transferred via the serial interface is in progress.` | **传输过程中不翻转**（**这句原文语法是坏的，见 `## 出处` ⚠️②**） |
| 2 | `All lines change the state in parallel as soon as the transfer via the serial interface has been finished.` | **传完一起翻转** |
| 3 | `Because the time required for this hardware based dynamic switching is negligible, latency can be disregarded.` | **这条硬件的开销可忽略，延迟不用考虑** |

**第 2 条是 ganging 最要紧的语义**：**一组里的 utility line 是「一起」翻转的，不是先到先翻。**
**（推断）这对「多根线必须同时动作」的场景是关键**——依据是第 2 条的 `in parallel` 加上第 3 条的
`latency can be disregarded`；**但原文没有说这条特性是为哪个场景设计的。**

### 怎么定义：SmarTest 7 和 8 **落在完全不同的地方**

**这是本页最实用的一节。** 原文把两条分开写：

| SmarTest | 在哪定义 | 原文 |
|---|---|---|
| **8** | **DUT board description file 的 `utilityControl` 元素**，且**至少两个连续**的 utility pogo block | `The ganged utility blocks are to be defined by element utilityControl of the DUT board description file with minimum two contiguous utility pogo blocks defined.` |
| **7** | **`UTILITY_SEQ_MODE.pogoBlock()` 这个 test method API** | `The ganged utility blocks are to be defined by the UTILITY_SEQ_MODE.pogoBlock() test method API.` |

**一句话记住差别**：**SmarTest 7 是「程序里的一行 API」，SmarTest 8 是「DUT board description file 里的一个声明」。**

**两条都另有出边**：SmarTest 8 那条指向 `Controlling utility lines`；
SmarTest 7 那条指向 `Setting up sequencer control of utility lines`（**原文说那里有 ganging 的例子**）。
**两篇本页都没读。**

### 可以同时配多组

> 「It is possible to configure more than one ganged group. For example, you can set up digital control of utility blocks 1,2,3 via a set of three digital channels and at the same time set up digital control of utility blocks 4,5,6,7 via another set of three digital channels. Sequencer control of the groups of utility blocks can be switched on and off independently.」

**两组互不干扰，能分别开关。** 注意原文那个例子：**3 个 block 一组、4 个 block 一组，两组各用三个数字通道**——
**通道数不跟着 block 数涨**（**（推断）**：一组无论几个 block 只占一套串行接口引脚，
依据是下面「数据宽度」那段的 `by three (or four) digital pins`）。

### 数据宽度：ganging 到底买到了什么

> 「Ganging of utility blocks allows you to expand the data width beyond that of a single word (either 16 or 32 bits), where the number of ganged utility blocks multiplies the available word width.」

| 情形 | 宽度 | 原文 |
|---|---|---|
| 一块 16-bit（2-row）block | 16 | — |
| **串三块 16-bit block** | **48** | `by ganging three utility blocks of 16 bits each a data width of 48 bits is produced which can be controlled by a single burst of digital serial data` |
| **8 块 32-bit（4-row）block** | **256 根 utility line** | `it is possible to control up to 256 utility lines (8 utility blocks with 32 utility lines each) by three (or four) digital pins` |

**三个数对得很齐**：**48 = 3 × 16**、**256 = 8 × 32**，**而 8 正是规则 2 的上限。**
**所以「ganging 的上限」就是规则 2 那句 `Up to eight pogo blocks`。**

**而且宽度是你自己选的：**

> 「You determine the word width yourself by fitting either 2-row or 4-row utility pogo blocks to your DUT interface, refer to Utility line assignments.」

**这里有个用词上的滑动值得点出来**：原文一处说 `16 or 32 bits`（**word width**），
另一处说 `256 utility lines (8 utility blocks with 32 utility lines each)`（**lines**）——
**原文把「一个 block 的 word width」和「一个 block 的 utility line 数」当同一个量在用**
（**（推断）**，依据是两句里 `32 bits` 与 `32 utility lines` 指的是同一批 4-row block）。

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`。** 从这一页能排出五步：

1. **先对适用表**：你的系统 + SmarTest 组合在不在范围里。
   **EXA Scale + SmarTest 8 + Utility Card 不在**（它走内部数据通路）。
2. **算需要多少根线 → 定 block 数与每块宽度**：2-row 是 16、4-row 是 32；
   **block 必须连续，最多 8 块。**
3. **接线**：**只把「号最小的那块」（master）的串行接口引脚接到你要用的数字通道**；
   **slave 的接口引脚全部悬空**（内部已经连好，不要再接）。
4. **在软件里定义**：SmarTest 8 写 DUT board description file 的 `utilityControl` 元素；
   SmarTest 7 用 `UTILITY_SEQ_MODE.pogoBlock()`。
5. **要几组就配几组**，每组可以独立开关。

**原文没有 `## Related information` 段**（本篇没有这一节），
**也没有 `## What to do next`**——**出边只有那两篇指向文档**（`Controlling utility lines` 与
`Setting up sequencer control of utility lines`），**本页都没读**。

**一条本页必须交代的前提**：**`utilityControl` 元素写在哪、语法是什么，本页给不出**——
原文只说「用它定义」，**没给写法**。

## 和谁有关

- [[sequencer-controlled-utility-lines]]（**已建**）— **父概念**：本页讲的是它的一个子话题；
  **原文那句 `in the context of the sequencer-controlled utility lines` 就是把 ganging 钉在它下面的**
- [[utility-line-assignments ]] — **原文点名的**：要在 DUT interface 上装 2-row 还是 4-row，
  决定了 word width，**细节在那篇**
- [[utility-card ]] — **适用性的关键件**：EXA Scale + SmarTest 7 **必须装它**才在范围内；
  **EXA Scale + SmarTest 8 装了它反而不走这条路**
- [[cross-card-ganging-requires-ddic]]（**已建**）— **⚠️ 名字撞车，别搞混**：
  那一页的名字里也有 ganging，**但本页原文把 `ganging` 限定在 utility block 的串行接口级联上**
  （`in the context of the sequencer-controlled utility lines`），**两者不是同一支**。
  **本页没有读它的全文，也不引用它的内容**——**这里只提醒：看到 `ganging` 这个词要先看语境。**
- `UTILITY_SEQ_MODE.pogoBlock()`（**未建**）— **SmarTest 7 的定义入口**；
  **原文只给了它的名字，没给参数**，**本页也没读它那篇**
- `Controlling utility lines` / `Setting up sequencer control of utility lines`（**均未建**）—
  **原文分别指向的两篇**（前者给 SmarTest 8，后者给 SmarTest 7 且含 ganging 例子）；**本页都没读**

## 版本

原文**有** `## Functional changes`，两条：

- **Introduced in SmarTest 7.1.0**
- **SmarTest 7.2.0**：`256 sequencer-controlled utility lines introduced on ATH/CTH/STH DUT Scale and on LTH`

**三点从这两条读出来的：**

| 观察 | 说明 |
|---|---|
| **两次变更都记在 SmarTest 7 名下** | **7.1.0 引入、7.2.0 把上限抬到 256 行**（正文里那个 `256 utility lines` 就是这一条） |
| **SmarTest 8 那边一条都没有** | 而正文的适用表**一半是 SmarTest 8**——**8 上的 ganging 是什么时候有的，本篇没记** |
| **`ATH/CTH/STH DUT Scale` 与 `LTH` 在正文里一个都没出现** | **原文没说它们是什么**（**（推断）是 test head / DUT scale 的型号名，但原文没有定义，本页不展开**） |

## 出处

`sources:` 一篇：
`02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.03_Ganging_utility_blocks.md`

**本页没做的**：

- **源文档里没有图**——本篇正文里**没有任何插图**，**所以本页没有任何来自图的结论**；
  **连 ganging 的接线示意图都没有**（原文只用文字说「只接 master、slave 悬空」）。
- **`Controlling utility lines`、`Setting up sequencer control of utility lines` 两篇没读**——
  所以 **SmarTest 8 的 `utilityControl` 元素怎么写、SmarTest 7 的 ganging 例子长什么样，本页一个字没有**。
- **`UTILITY_SEQ_MODE.pogoBlock()` 那篇没读**——**参数、返回值、能不能只传一部分 block，本页给不出**。
- **`optional Utility Card` 那篇没读**——它长什么样、有几块、怎么判断「多于一块」，本页给不出。
- **`Utility line assignments` 那篇没读**——**2-row / 4-row 怎么装、装在哪，本页给不出**。
- **没有 `## Procedure` / `## Before you begin`**，**没有在真机上配过 ganging**——
  `verified: doc-only` 指的就是这件事。
- **`ATH` / `CTH` / `STH DUT Scale` / `LTH` 是什么，原文没说，本页不猜。**
- **`utilityControl` 元素所在的 DUT board description file 是哪一篇文档管的，本篇没说**，
  **本页也没去找**。

> ⚠️ **本篇的语料瑕疵五处，本页照实记下、一处都没替它改**：
>
> ① **编码损坏（§11.2 ①），共 6 处 `鈥`（U+9225）**：
> - `sequencer鈥慶ontrolled` —— **3 处**（正文第一句 2 处、版本记录 1 处）；
> - `4鈥憆ow` —— **2 处**、`2鈥憆ow` —— **1 处**（都在「数据宽度」那一段，原文指的是 4-row / 2-row）。
> **本页正文引用到的那两处（第一句、数据宽度那句）照坏字原样抄**；
> **要拿这些词去 raw 里搜，得搜坏掉的形态。**
>
> ② **一句话的语法是坏的（本页最实的一处）**：
> `Utility lines are not toggled while the data are transferred via the serial interface is in progress.`
> ——**`while` 从句里两个谓语挤在一起**：`the data are transferred via the serial interface`
> 和 `is in progress` **各自都像主句的谓语，拼不成一个完整句子**。
> **原文如此；本页正文引用它时逐字照抄，没有替它修。**
>
> ③ **`Note` 和它的正文挤在同一行**：原文那一行是 `  Note This section applies to`
> ——**`Note` 前面有两个空格，后面直接跟句子**，**它要管的那个三条列表在下一行才开始**。
>
> ④ **一处双空格**：`of the DUT board description file  with minimum two contiguous utility pogo blocks`
> ——**`file` 与 `with` 之间是两个空格**。
>
> ⑤ **`- SmarTest 8:` / `- SmarTest 7:` 两条列表项后面各跟着一整段正文**，
> **段与列表项之间没有任何缩进关系**——列表项和段落在这篇里是混排的。原文如此。

`verified: doc-only`
