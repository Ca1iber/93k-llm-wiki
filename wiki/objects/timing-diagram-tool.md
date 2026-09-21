---
type: object
title: Timing Diagram Tool
layer: gui
stage: pattern
tags: [timing-diagram-tool, pattern, waveform, debugging, error-analysis, gui]
related: [pattern-tool, timing, timing-setup-tool, report-window, shmoo-tool, signal-analyzer, smartest-7.1.4]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Timing Diagram Tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **626 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33.01.09_Aligning_drive_and_receive_data_in_high_resolution_and_scope_mode.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33.02.04_Displaying_not_clearly_identified_areas__dotted_line.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Using the Timing Diagram Tool › Aligning drive and receive data in high resolution and scope mode）

The following example shows the effect of the re-alignment:

 !`Misaligned receive data`（raw: `../../../../raw/117987.png`）  !`Defining the offset`（raw: `../../../../raw/117988.png`）  !`Re-aligned receive data`（raw: `../../../../raw/117989.png`）

Note that this example is only intended to illustrate the shifting mechanism. It does not reflect the use case described above.

### Example（取自子主题 How data is displayed in the timing diagram › Displaying not clearly identified areas  dotted line）

!`Displaying not clearly identified areas (dotted line)`（raw: `../../../../raw/124998.png`）

The dotted lines starting at cycle 8143 for the pins a1 to a3 indicate that no emap data is available for them.

For the pin a0 the data is available for the whole displayed area.

<!-- 语法节 end -->

## 是什么

**Timing Diagram Tool 把「你发出去的波形」和「DUT 回来的波形」画在一起。** 原文：

> 「The Timing Diagram tool allows you to **view the actual waveforms that you are sending to the
> DUT**, and **the response from the DUT's outputs**.」

**两半，一个是发、一个是收：**

| 原文 | 中文 | 谁产生的 |
|---|---|---|
| `the actual waveforms that you are sending to the DUT` | **你实际发给 DUT 的波形** | 测试机 → DUT |
| `the response from the DUT's outputs` | **DUT 输出端回来的响应** | DUT → 测试机 |

**注意 `actual`（实际的）这个词**：它画的不是你写的期望波形，是**实际发出去/收回来**的那个
（推断，依据是 `actual` 与后文 `expected data` 的对照——**期望数据在 Pattern Tool 窗口里，不在这里**）。

**原文把它归类为 `result analysis tool`**（`the Timing Diagram **result analysis tool**`），
**但本页的 `stage` 是 `pattern`**——原文里它处理的是 `the executed pattern`、`the format
definition`、`the Pattern Tool window` 这些 pattern 侧的东西（推断，依据就是这几个词）。

### 它的主用途：让错误分析变简单

> 「To make the **error analysis** simpler, the Timing Diagram can indicate **the points in the
> waveform where the data received from the DUT did not coincide with the expected data that is in
> the Pattern Tool window**.」

**这一句给了它存在的理由，也给了「错在哪」的定义：**

| 项 | 原文 | 含义 |
|---|---|---|
| **判据** | `the data received from the DUT did not coincide with the expected data` | **收到的 ≠ 期望的** |
| **判据的期望值从哪来** | `the expected data that is in the **Pattern Tool window**` | **期望数据不在本工具里，在 Pattern Tool 窗口里** |
| **标注在哪** | `the points in the waveform` | **标在波形上的那些点上** |
| **目的** | `To make the error analysis simpler` | **为了让错误分析简单** |

> **第二行是本页一个跨工具的接口**：**要判「对不对」，期望值得到 Pattern Tool 窗口里去取。**
> **所以本工具不是自足的**（推断）——**这也是下面「和谁有关」里 link 到 Pattern Tool 的依据。**

### 哪些 pin 画、哪些不画（本页最细的一张表）

原文单起一节 `## Pins used and unused in executed pattern` 讲这件事，
**规则比想象的绕，因为它不是「用到的画、没用到的都不画」**：

| pin 的类别 | 画不画 | 原文细节 |
|---|---|---|
| **被执行 pattern 用到的 pin** | **画，而且是重点** | `The Timing Diagram **focuses on the used pins**.` |
| **格式定义里出现的头两个未使用 drive pin** | **画，但受限** | `displays the **first two unused drive pins** that appear in the format definition`；**但它们不能被 `formatted`**（原文引号是原文加的）；**除了 `the break waveform, if defined`（中断波形，如果定义了）之外不显示别的信息**，而且**用 dotted line 画** |
| **其余所有未使用的 drive pin** | **不画** | `All other unused drive pins … will not be displayed.` |
| **所有未使用的 receive pin** | **不画** | `… and all unused receive pins will not be displayed.` |

**三处要留意的：**

1. **「头两个」(the first two) 是个硬数目，原文没有解释为什么是两个。** **语料未写。**
2. **那一对 pin 之所以还被画出来，理由原文没明说**（推断：它们是只用来发 break 波形的，所以留着；
   **但原文没写，本页不写死**）。
3. **「不能被 formated」的 `formatted` 是原文打了引号的词**，**它的确切含义原文没解释**——
   **本页照抄它，不替它释义。**

**另有一条兜底机制，落在 Report window 上：**

> 「SmarTest issues **a warning message in the Report window** if any pin exists that it is not
> displayed.」
>
> ——**只要有 pin 没被显示，SmarTest 就在 Report window 里发一条警告。**
> **也就是说：本工具「少画了东西」这件事不会静默**（推断）。
> （这句话原文本身有语病，见 `## 出处` 瑕疵②。）

### 三条子主题

| 子主题 | 从标题能读出的（**推断**） |
|---|---|
| `Using the Timing Diagram Tool` | 怎么用 |
| `How data is displayed in the timing diagram` | **数据怎么被显示**——对应上面那张 pin 表 |
| `How to read timing diagrams: Unstable signals` | **怎么读图：不稳定信号**——**这是一篇「怎么不读错」的篇目** |

> **第三条值得单独记**：标题写的是 `How to read`（**怎么读**），不是 `How to use`——
> **说明这种图有会被读错的地方**，原文专门为它写了一篇（推断）。
> **本页一个字都没有它的内容**——那篇没读。

## 典型用法

**语料未写操作步骤。** 主文档没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`。

**但原文里有一条硬前提，这是本页最有价值的一条「用法」：**

> 「**Note** If you want to debug a **synchronized protocol test** with the Timing Diagram,
> you **must place a breakpoint in the test method code before calling the `unlink()` function**.」

拆开：

| 项 | 内容 |
|---|---|
| **什么时候适用** | 用本工具调试 **synchronized protocol test**（同步协议测试）时 |
| **必须做什么** | 在 **test method 代码**里、**调 `unlink()` 函数之前**，**下一个断点** |
| **强度** | 原文用的是 **`must`**——**不是建议，是前提** |

> **三个要点：**
> **① 这条只对 synchronized protocol test 成立**，原文用的是 `If you want to…`——
> **别的场景有没有类似前提，原文没说。**
> **② 断点的位置是「`unlink()` 之前」，不是「随便哪里」**——
> **为什么必须是之前，原文没解释**（**语料未写**）。
> **③ 这是一条「在别的工具里做的事」**：断点下在 **test method 代码**里，
> **不在本工具里**（推断）。**所以用它调试协议测试之前，得先去改测试代码。**

**另有一条顺序上的事情**：**期望数据在 Pattern Tool 窗口里**（见「是什么」）。
**所以要判「收到的对不对」，Pattern Tool 那一侧得是开着的**（推断，依据是原文
`the expected data that is in the Pattern Tool window` 这个定位短语）。

**原文的 `## Related information` 一节列了四篇**（见 `## 出处` 瑕疵③——它们被连排在一起）：

`Creating a new format`、`Shmoo Tool`、`Timing Setup Tool`、`Signal Analyzer`。
**原文只给了名字，没有说以什么方式相关**——**本页不替它编关系**。

## 和谁有关

- [[pattern-tool]] — **判据的来源，本页最要紧的一条关系。**
  原文说期望数据是 `the expected data that is in the **Pattern Tool window**`——
  **本工具只负责把「收到的」和「期望的」对不上的点标出来，期望值本身在那一侧。**
- [[timing]] — **本页 `stage: pattern` 的相邻面**：它看的是时序下的实际波形。
  **原文没有直接提 `timing` 这个字**（推断）。
- [[timing-setup-tool]] — **原文 `## Related information` 列了它**（连排四篇之一）。
  **原文没说是什么关系**（推断：一个是 setup 侧、一个是看图侧，**但这是推断**）。
- [[shmoo-tool]] — **原文 `## Related information` 列了它**。**同样没有说明关系。**
- [[signal-analyzer]] — **原文 `## Related information` 列了它**。**同样没有说明关系。**
- [[report-window]] — **兜底警告的落点**：原文 `SmarTest issues a warning message in the Report
  window if any pin exists that it is not displayed`。
- [[pattern]] — 它画的波形属于 `the executed pattern`；**未使用的 pin 是按「这个 pattern 用没用到」分的**。
- [[waveform-view]] — **同批建的页，讲波形的另一种看法**。
  **原文没有提过它**（推断：名字最近，但**关系是本页推的，不是原文写的**）。
- [[smartest-7.1.4]] — 本页版本段第二条落在它上面（`Modified display of pins`）。
- `Using the Timing Diagram Tool`（**未建、未读**）— 怎么用，**本页的 `## 典型用法` 的空缺主要在这里**。
- `How data is displayed in the timing diagram`（**未建、未读**）— 显示规则；
  **本页那张 pin 表是从主文档抄的，那一篇里还有多少规则本页不知道**。
- `How to read timing diagrams: Unstable signals`（**未建、未读**）— **怎么读图、哪些会读错**。
- `Creating a new format`（**未建、未读**）— `## Related information` 第一篇；
  **注意「format definition」正是决定「头两个未使用 drive pin」的那份东西**（推断，依据是
  主文档里 `that appear in the format definition` 和这一篇的标题）。
- `synchronized protocol test` / `unlink()` / `break waveform` / `emap`（**均未建**）—
  原文出现但本页无法展开的词，**本页一律用反引号写**。

## 版本

`## Functional changes` 段有，**两条**：

> 「**Introduced before SmarTest 6.3.2**」
> 「**SmarTest 7.1.4**: **Modified display of pins**」

| 条目 | 性质 | 本页能说的 |
|---|---|---|
| `Introduced before SmarTest 6.3.2` | **只给上界**（`before`） | **6.3.2 之前就有它；引入版本语料未写** |
| `SmarTest 7.1.4: Modified display of pins` | **确定的版本 + 一件确定的事** | **7.1.4 改了 pin 的显示方式** |

> **第二条和正文对得上**（推断）：正文里最细的一节就是 `## Pins used and unused in executed
> pattern`——**pin 怎么显示正是这一篇的重点**。
> **但原文没有把这两处连起来说**：`Modified display of pins` **没有说明改了什么、
> 改成什么样**。**所以本页只能说「7.1.4 改了 pin 的显示」，改的是什么，语料未写。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.md`

**这就是本页正文的全部依据。整篇 37 行，正文约 10 行。**

**本页没做的**：

- **三条子主题一篇都没读**：`Using the Timing Diagram Tool`（`.01`）、
  `How data is displayed in the timing diagram`（`.02`）、
  `How to read timing diagrams: Unstable signals`（`.03`）。
  **直接后果**：**怎么用、显示规则的全貌、哪些地方容易读错——本页都没有。**
  本页那张 pin 表**只是主文档自己写的那一段**，不是完整规则。
- **`## Related information` 列的四篇一篇没读**：`Creating a new format`、
  `Shmoo Tool`、`Timing Setup Tool`、`Signal Analyzer`。**它们和本工具是什么关系，
  本页一个字都讲不出来**——**原文也只给了名字。**
- **一张图没看。** 主文档里有一张
  `![The Timing Diagram window](<../../../../raw/59114.png>)`，
  本页「语法 / 参数」节里另有 4 个图占位
  （`117987.png` 未对齐的接收数据、`117988.png` 定义偏移、`117989.png` 重新对齐后的接收数据、
  `124998.png` 未明确识别的区域）。
  **本页没有任何来自图的结论**——**时序图长什么样、dotted line 画出来是什么样，
  本页一个字都不知道。**
- **「语法 / 参数」节那 626 字符本页没有当作依据。** 那一节是脚本从**两篇子主题**
  （`…33.01.09_Aligning_drive_and_receive_data_in_high_resolution_and_scope_mode.md`、
  `…33.02.04_Displaying_not_clearly_identified_areas__dotted_line.md`）**逐字抽的**（§4），
  **那两篇本页没读**。本页在正文里只引了它一次（当作 `dotted line` 的旁证，见下），
  **没有把 `re-alignment`、`emap` 那些内容写进正文**。
- **没有查 `emap` 是什么**、**没有查 `high resolution and scope mode` 是什么**
  （那两种模式只出现在未读子主题的标题里）。
- **没有查 `synchronized protocol test` 是什么**，**没有查 `unlink()` 属于哪套 API**，
  **也没有查「断点为什么必须下在 `unlink()` 之前」**。

> ⚠️ **语料瑕疵，照实记下、一处没替它改**（§11.2）：
>
> **① 一句语法坏掉的句子**（逐字引）：
> `Note SmarTest issues a warning message in the [Report window](<...>) if any pin exists that it is not displayed.`
> ——**`any pin exists that it is not displayed` 讲不通**：
> 从句里的 `it` 没有可指代的对象，读不出「谁没被显示」。
> **按上下文推测应读作「存在没有被显示的 pin」**（推断），
> **但原文写的就是这样，本页不替它改写**——所以本页在正文里只保留了
> `if any pin exists that it is not displayed` 的引文并把这一点指出来。
>
> **② 两处 `Note` 没有成段/成行**（逐字引两处开头）：
> ` Note If you want to debug a synchronized protocol test with the Timing Diagram, you must place a breakpoint…`
> 与
> `Note SmarTest issues a warning message in the [Report window](<...>) …`
> ——**第一处前面是一个空格、`Note` 后面直接接 `If`**，**两处都没有换行或标点把它与正文分开**，
> **在 Markdown 里会被并进同一段**。**本页在正文里用引用块引用它们时，是按它本意当独立提示用的**——
> **这是排版动作，本页在此声明。**
>
> **③ `## Related information` 四个链接连排、无任何分隔**（逐字引全行）：
> `[Creating a new format](<02.08.04.33.01.07_Creating_a_new_format.md>)[Shmoo Tool](<02.08.04.25_Shmoo_Tool.md>)[Timing Setup Tool](<02.08.04.34_Timing_Setup_Tool.md>)[Signal Analyzer](<02.08.04.26_Signal_Analyzer.md>)`
> ——**四个链接首尾相接，中间没有空格、逗号或换行**。
> **本页没有替它加分隔符**，而是在正文里把四个名字**逐个写出来**。
>
> **④ 一个本页不判的用词冲突**（两处都逐字引）：
> 主文档说**未使用的 drive pin** 上只画 `the break waveform, if defined, **with a dotted line**`；
> 而本页「语法 / 参数」节从子主题抽出的那句是
> `The **dotted lines** starting at cycle 8143 for the pins a1 to a3 indicate that **no emap data is
> available** for them.`
> ——**两处的 dotted line 含义不同**：一处是「中断波形」，一处是「数据不可用」。
> **它们是不是同一套约定（比如「虚线 = 信息不全」这个总规则下的两种情形），原文没有说。
> 本页不判，也不替它们调和。**
>
> **⑤ 版本段的 `before` 写法**（逐字引）：`- Introduced before SmarTest 6.3.2`
> ——**只给上界，不是引入版本**；本页在 `## 版本` 里已把这一点写明。
>
> 链接指向方面：`## Related information` 的四条路径
> （`02.08.04.33.01.07` / `02.08.04.25` / `02.08.04.34` / `02.08.04.26`）
> **与四条子主题的编号体系自洽，本页未发现指错**；
> 三条子主题的链接（`<02.08.04.33.0N_*.md>`）**也与条目名一一对应**。

`verified: doc-only`

