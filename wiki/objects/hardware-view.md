---
type: object
title: Hardware view
layer: gui
stage: run
tags: [hardware-view, gui, run, pin-browser, hardware-perspective, dc-profiling, icons, measurement]
related: [run, pin, sequencer-controlled-utility-lines, utility-lines, waveform-view, dps128-dps64-cards, dc-scale-xps256-card, dc-scale-uhc4t-card, smartest-6.3.2, smartest-6.5.0, smartest-6.5.2]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Hardware view

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,146 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.05_Profiling_of_DC_Scale_cards_with_Hardware_view.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Profiling of DC Scale cards with Hardware view）

### Utility serial configuration for DC profiling

The following screen shot shows a part of the DPS128 Hardware view.

 !`Profiling in Hardware view`（raw: `../../../../raw/353618.png`）

The Profile button at the bottom is marked in red and opens the DPS Profile dialog.

  !`DPS profile with`（raw: `../../../../raw/353741.png`）

You can define the configuration of sequencer鈥慶ontrolled utility lines, which is programmed to hardware before any pattern execution.

The UTSC firmware syntax is one of the following:

- `UTSC [1-8],[RW|RD][,MASK]`
- `UTSC ([-,1-8),[RW|RD][,MASK]`

For example:

UTSC 1,RW; UTSC (2,3),RW,MASK; UTSC (5-8),RD

After the pattern finishes, SmarTest applies: UTSC ALL,OFF.

Multiple serial buses are supported. Each bus can range from 1 single utility block to up to 8 consecutive blocks.

For example:

- Single bus: 1-8. (Block 1 is master. Blocks 2-8 are slaves)
- Two buses: 2-3,5-7 (Blocks 2 and 5 are masters. Others are slaves)

If the Seq Ctrl'd Util Blocks field is empty, no sequencer control is enabled during profiling.

The content of the Seq Ctrl'd Util Blocks field is not stored/restored after closing the dialog.

<!-- 语法节 end -->

## 是什么

**Hardware view 是「选中一个 pin，看它这一刻的硬件设定」的那张视图。**
定义文档第一句就把它挂在了两个地方上，逐字：

> 「The Hardware view is part of the Hardware Perspective and is associated with the Pin Browser
> view.」

**即：它在 `Hardware Perspective` 里，和 `Pin Browser view` 是一对。**

**它的输入、输出、以及「谁跟着谁动」，原文一段给全了**，逐字：

> 「When you select a pin in the Pin Browser, on the top of the Hardware view, the site number,
> pin name, and channel number for this pin are displayed. And the diagram in the Hardware view
> shows the test system circuitry relevant to the chosen pin.」

| 你做的事 | Hardware view 上出现什么 |
|---|---|
| **在 Pin Browser 里选中一个 pin** | **顶上**：`the site number, pin name, and channel number` |
| **同上** | **图里**：`the test system circuitry relevant to the chosen pin`——**与这个 pin 相关的那部分测试系统电路** |

### ⚠️ 那张图不是实物图

> 「Note The schematic shown in the Hardware view is a simplified diagram and does not provide an
> exact representation of the actual hardware in your system.」

**这一句是 `Note`，很容易读漏**：**它是简化示意图，不精确代表你系统里的实际硬件。**
**拿它当接线依据是错的。**（**本页只有这一句，原文没有再说别的。**）

### 一张图讲完「谁在第几步」

原文给了一个编号的流程示意，逐字：

> 「For a pin selected in the Pin Browser (1), executing the measurement code (2), the results are
> displayed in the Hardware view (3).」

> 「If updates are required, a warning is displayed at the bottom of the screen (4). To update the
> displays, click the Refresh buttons (5).」

**五个编号（1)–(5)）指的是本篇那张示意图 `raw/353726.png` 上的标注**（**本页没看那张图**）。
**能读出来的动作链是：选中 pin → 跑测量代码 → 结果进视图 → 需要更新时底部出 warning →
点 Refresh 按钮更新。** 注意原文说的是 **`buttons`（复数）**。

### 三个「用途」（原文 `###` 之上的四条功能清单）

原文逐字列的四个功能：

- `Shows the current settings for the selected pin` —— **显示选中 pin 的当前设定**
- `Allows you to change some of the settings for debugging purposes` —— **允许改一部分设定，用途写明是调试**
- `Allows you to evaluate your changes (make current or voltage measurements)` ——
  **允许直接量电流/电压来验证你的改动**（**与下面的 DC profiling 是同一件事的两个入口**，见 `## 典型用法`）
- `Allows you to compare the settings by Opening multi Hardware Views of different pins` ——
  **开多个 Hardware view 来**对比**不同 pin 的设定**

**第三条是这一页和「只读视图」的分界线**：**它不只显示，它还能测量。**

### 离线模式下它不一定知道硬件真实状态

> 「In offline mode, the Hardware view cannot always return the correct settings of the hardware.
> This is especially true when hardware settings depend on pattern鈥慴ased conditional jumps and
> match loops.」

**两个条件叠加时才最不准**：**离线 + 设定依赖「按 pattern 的条件跳转与 match loop」**。
**⚠️ `pattern鈥慴ased` 是语料的编码损坏（= `pattern-based`），见 `## 出处` ①——本页引文照原样。**

**更重的一句在下面**，逐字：

> 「If SmarTest determines that the state of the hardware cannot be evaluated correctly, "WARNING: ...
> - reported last DC state ... may not reflect online state." is issued in the ui_report window.」

**两个 `...` 是原文自己写的**（§11.1：省略号只许出现在原文本来就有的地方）——
**即这条警告信息的中间部分本篇没给全。**
**要记的是那句的结论**：**报出来的「最后一次 DC 状态」可能不是在线状态。**

### 右上角那一排图标（本篇最有实用价值的一节）

**原文逐字开场**：
`The figure below shows the function of each of the icons at the right top of the Hardware view.`

**⚠️ 这一节的题注（alt）与功能对不上，见 `## 出处` ②。下表左栏的「题注」照抄语料原样，
右栏是原文给的功能。**

| 题注（**逐字，语料如此**） | 图片 | 功能（**逐字**） |
|---|---|---|
| `Refresh button` | `raw/106958.png` | `Refresh the hardware information in this view.` + `After executing the test method, click this button, the hardware setting in this view will be updated to the settings in the test method.` |
| `Zoom in button` | `raw/106959.png` | `Link with editor and selection.` + `When this button is pressed, click a pin in the Pin Browser view, the Hardware view is updated to the setting of this pin immediately.` |
| `Zoom in by large step button` | `raw/106962.png` | `Pin this view.` + `When the Hardware View displays a pin's setting, click this button, the display of the Hardware View is pinned to the current pin.` |
| `Open new Hardware View button` | `raw/111158.png` | `Open new Hardware view.` + `When the Hardware view displays a pin's setting, click this button, a new Hardware view displaying the setting of the same pin opens. You can use this feature to compare the settings of different pins.` |
| `Zoom out button` | `raw/106960.png` | `Zoom out on the Hardware view.` |
| `Zoom in button` | `raw/106961.png` | `Zoom in on the Hardware view.` |
| `Resize to default button` | `raw/106963.png` | `Resize the graph to it's default size.` |
| `Resize to fit screen button` | `raw/106964.png` | `Resize the graph to fit the screen.` |
| `Setup preferences button` | `raw/106965.png` | `Setup preferences.` |
| `1` | `raw/114855.png` | `Show or hide properties.` + `The button is active only for RF pins. Clicking this button shows or hides a tabular in the Hardware view, which displays current hardware state of an RF board.` |

**三条要单独记的：**

1. **`Link with editor and selection`（`raw/106959.png`）是「跟着 Pin Browser 走」的开关**——
   `click a pin in the Pin Browser view, the Hardware view is updated to the setting of this pin
   immediately`。**它的题注却写着 `Zoom in button`（见 `## 出处` ②）。**
2. **`Pin this view`（`raw/106962.png`）是「钉住」**——**钉住之后显示不再跟着 Pin Browser 动**。
   **⚠️ 这一条本页是从这一句读出来的：「pinned to the current pin」＋上一行按钮的「立即更新」对照。**
   **原文没有写「钉住之后 Pin Browser 就不再影响它」这句话。这是推断。**
3. **最后一个按钮只对 RF pin 有效**——原文逐字 `The button is active only for RF pins.`，
   它开合的是 `a tabular … which displays current hardware state of an RF board`。

## 典型用法

**定义文档里没有 `## Procedure`、没有 `## Before you begin`**——
**它的 `## 典型用法` 只能从功能清单与那张流程示意图里落出来。**
**但本篇 `## 语法 / 参数` 节里逐字收了一个子主题
（`Profiling of DC Scale cards with Hardware view`），那一篇有完整的 `## Before you begin`
与 `## Procedure`**——**下面第二节是它的。**（**那篇子主题本页读了，见 `## 出处`。**）

### 用法一：改设定并立刻验证（定义文档给的）

1. **在 Pin Browser 里选中一个 pin**（`the site number, pin name, and channel number` 会显示出来）。
2. **改设定**（`Allows you to change some of the settings for debugging purposes`）。
3. **测量电流或电压来验证**（`make current or voltage measurements`）。
4. **需要更新显示时点 `Refresh`**（`raw/106958.png`）——
   原文给的时机是 `After executing the test method`。
5. **要和另一个 pin 对比 → 点 `Open new Hardware view`**（`raw/111158.png`）开第二张。

**两个开关要知道**：`Link with editor and selection`（跟着 Pin Browser 走）、
`Pin this view`（钉住）。**两者是相反方向的动作。**

### 用法二：DC profiling（`## 语法 / 参数` 节里那个子主题）

**那篇子主题的第一句就给这个工具定了名与位置**，逐字：

> 「Profiling (DC profiling) allows you to measure and display current and voltage waveforms
> during pattern execution. The tool is also known as DC Profiler and is available in the Hardware
> perspective.」

**即：它是 Hardware perspective 里的一个工具，在 pattern 执行期间量并显示电流/电压波形。**
**`## Before you begin` 三条**，逐字：

- `Change to the Hardware perspective.`
- `In the Primary view of the Hardware perspective, select the primaries and the pattern.`
- `The DC Scale pin must be connected to the DUT.`

**`## Procedure` 的路径**（原文逐条）：

| 步 | 原文（**逐字**） |
|---|---|
| 1 | `To generate a current or voltage profile waveform, open the Hardware view of your DC Scale card.` |
| 2 | `Make sure the AC_Sense and AC_Force relays are closed (connection to DUT).` |
| 3 | `In the Hardware view, at the bottom, click Profile. The DPS Profile dialog opens.` |
| 4 | 在 `DPS Profile` 对话框里给五个选项（见下表） |
| 5 | `To start the profiling click MEAS.` |
| 6 | `When the calculation is completed, the Waveform view displays the resulting waveform.` |
| 7 | `To close the DPS Profile dialog click DONE.` |

**第 4 步的五个选项**，逐字：

- `Measure Range (V): The expected measurement value in volt.`
- `Sampling Rate (ms): The sampling period in milliseconds:`——**它的上限随卡不同**（见下）
- `Average Factor: The number of measurements per sample.`
- `Current Measurement or Voltage Measurement`
- `Single Measurement or Looped Measurement`

**`Sampling Rate` 的那张表，按卡分**（原文表的列是 `DC Scale card` / `Condition` /
`Max. rate` / `Min. period`）：

| 卡 | 条件 | `Max. rate` | `Min. period` |
|---|---|---|---|
| `DPS128` | `1` | `100 ksps` | `0.010 ms` |
| `DPS128` | `2 ... 8` | `50 ksps` | `0.020 ms` |
| `UHC4T` | `1` | `100 ksps` | `0.010 ms` |
| `UHC4T` | `2 ... 4` | `50 ksps` | `0.020 ms` |
| `XPS256` | （**原文这一格是空的**） | `1 Msps` | `0.001 ms` |

**⚠️ 这张表的 `Condition` 栏与卡名栏在语料里错位了**（原文里 `1` 与 `100 ksps` 之间夹着
`channels per test processor` 与 `channels par card` 两句被压平的文字），见 `## 出处` ④。
**上面这张表是按原文字面重排的，本页没有替它修。**

**`Looped Measurement` 是持续重复**，逐字：
`If you have selected the Looped Measurement option, the profiling is constantly repeated until you
either close the DPS Profile dialog or select the Single Measurement option.`

**跑完还有一个副产品**，逐字（`## Results` 一节）：
`The sequence also generates sample test method code for the executed measurement in the Sample Code
view. You can directly copy and paste the code from the view into your test method program.`
**即：可以直接把生成的代码抄进测试方法程序。**

**卡之间行为有差异**（`## About this task` 一节给的）：

| 卡 | 差异（**逐字**） |
|---|---|
| `DPS128/64` 与 `UHC4T` | `profiling for multiport setups does not stop when the DPS part is finished. On these cards, profiling stops when the longest running port is finished.` |
| `DPS128/64` 与 `UHC4T` | `On these cards you can also do profiling when the pattern contains CLEV or CTIM commands.` |
| `DPS128` | `changing the current measurement range for profiling is not supported.`——**`the measureRange parameter` 在 `measureType` 为 `TM::CURRENT` 时被忽略** |
| `XPS256` | `changing the voltage range or the current range during profiling is supported, and the currently active range is also taken into account for profiling.`——**`measureRange` 同样被忽略，但 `still has to be set to a valid XPS256 range`** |

**一条 `Note` 要记**，逐字：
`DC profiling of the current is not supported if a pin is in UNGANG mode.`

### 用法三：给 profiling 配 sequencer 控制的 utility line（子主题的 `## Example`）

**这一节就是本页 `## 语法 / 参数` 节里逐字收的那一段**（段名 `### Example（取自子主题 …）`）。
**它的对象是 `the Seq Ctrl'd Util Blocks` 那个字段**——**即
[[sequencer-controlled-utility-lines]]**。要点：

- **UTSC 固件语法两种**：逐字 `` `UTSC [1-8],[RW|RD][,MASK]` `` 与 `` `UTSC ([-,1-8),[RW|RD][,MASK]` ``
- **例子**逐字：`UTSC 1,RW; UTSC (2,3),RW,MASK; UTSC (5-8),RD`
- **pattern 结束后 SmarTest 自己下一条**：逐字 `After the pattern finishes, SmarTest applies: UTSC ALL,OFF.`
- **一条总线最多 8 个连续 block**；**每条总线 1 个 master**，逐字
  `Single bus: 1-8. (Block 1 is master. Blocks 2-8 are slaves)` /
  `Two buses: 2-3,5-7 (Blocks 2 and 5 are masters. Others are slaves)`
- **字段空着 = 不做 sequencer 控制**，逐字
  `If the Seq Ctrl'd Util Blocks field is empty, no sequencer control is enabled during profiling.`
- **⚠️ 字段内容不保存**，逐字
  `The content of the Seq Ctrl'd Util Blocks field is not stored/restored after closing the dialog.`

## 和谁有关

- [[run]] — 本页 `stage: run` 的理由：**它是「跑的时候」用的视图**（改设定、量值、抓波形）。
  **⚠️ 本篇没有 `## Application` 这类自我定位段**，这条归属是本 wiki 的既有划分。
- [[pin]] — **本页的输入就是一个 pin**：原文 `When you select a pin in the Pin Browser…`
  与 `Shows the current settings for the selected pin`。**那一页本页没读。**
- [[sequencer-controlled-utility-lines]] / [[utility-lines]] —
  **本页 `## 语法 / 参数` 节里那段 UTSC 讲的就是它们**：
  逐字 `You can define the configuration of sequencer鈥慶ontrolled utility lines, which is
  programmed to hardware before any pattern execution.`
  **（⚠️ 那个词是编码损坏，见 `## 出处` ⑤。这两页的 raw 本页都没读——
  这条关系是从「子主题这一段在讲什么」看出来的，不是从对面回校的。）**
- [[waveform-view]] — **profiling 的产出去处**，原文逐字
  `When the calculation is completed, the Waveform view displays the resulting waveform.`
  **那一页本页没读。**
- [[dps128-dps64-cards]] / [[dc-scale-xps256-card]] / [[dc-scale-uhc4t-card]] —
  **profiling 那一节按卡讲差异，点名的就是这三种卡**
  （原文写的是 `DPS128/64 and UHC4T`、`DPS128`、`XPS256`）。
  **（推断）这三个名字与 wiki 里这三页对得上**——
  **依据只是名字；原文给的是链接名 `DC Scale DPS128/DPS64 cards` / `DC Scale XPS256 card`
  这类写法，本页没有点开核过目标路径。这是推断，那三页本页都没读。**
- [[smartest-6.3.2]] — **本页版本段第一条那个哨兵值里的版本号**（`Introduced before
  SmarTest 6.3.2`）。**⚠️ 它是哨兵，不是「6.3.2 的变更」，见 `## 版本`。**
- [[smartest-6.5.0]] / [[smartest-6.5.2]] — 本页另外五条版本记录各落在这两版上。
- `Hardware Perspective`（**未建**）— 本页所属的 perspective，原文第一句就点名。
  **本页没读那一篇，所以那个 perspective 里还有什么本页不知道。**
- `Pin Browser view`（**未建**）— **与本页成对的那张视图**，是本页的输入来源。
- `Profiling of DC Scale cards with Hardware view`（**未建**）— **本篇 `Subtopics` 清单里的第五项，
  也是本页 `## 语法 / 参数` 节逐字收的那一段的来源。**（**本页读了这一篇。**）
- 本页 `Subtopics` 清单里**另外 10 篇本页一篇没读**：`Executing a measurement`、
  `Quick measurements`、`Hardware view for digital pins`、`Hardware view for DPS and VI pins`、
  `Opening additional signals`、`Opening additional measurements`、
  `Changing settings in multiple Measurement windows`、`Finding non-matching settings across sites`、
  `Opening multiple Hardware views of different pins`、`Hardware view preference page`。
  **所以「不同 pin 类型的 Hardware view 长什么样」本页一个字都没有。**
- `DPS operating mode of DC Scale cards` / `PMU operating mode of DC Scale cards` /
  `DC_PROFILING_DEFINE` / `DC_PROFILING_ENABLE` / `DC_PROFILING_ON` / `DC_PROFILING_OFF` /
  `Sample Code view`（**均未建**）— **profiling 子主题 `## Related information` 那一行里的出口**
  （**7 个链接首尾相接，见 `## 出处` ⑦**）。**本页都没读**——
  **所以「怎么用 API 做 profiling」本页没有，本页只有界面那条路。**
- `ui_report window`（**未建**）— **离线警告的落点**，原文逐字
  `is issued in the ui_report window`。
  **⚠️ wiki 里另有一页叫 [[report-window]]，但原文写的是 `ui_report window`**，
  **两者是不是同一个东西，本篇没有说——本页不链它，也不替它认定。**

## 版本

**本文档有 `## Functional changes` 段，六条**，逐字：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 6.5.0: Added Link with editor and selection button.**
- **SmarTest 6.5.0: Added Pin this view button.**
- **SmarTest 6.5.0: Multi Hardware views can be opened.**
- **SmarTest 6.5.2: Added Open new Hardware view button.**
- **SmarTest 6.5.2: Added RF hardware state button.**

**⚠️ 第一条是 §11.2 ② 那个哨兵值，不是「6.3.2 的变更」。**
它写的是 `before`（**`Introduced before SmarTest 6.3.2`**），意思是
**「在本文档集覆盖范围开始之前就已经有了」**——**照字面读会生成一条
「6.3.2 新增了 Hardware view」的假信息。详见 [[smartest-6.3.2]]。**

**后五条**都能在正文里找到落点**——**每一条都是「加了哪个按钮/哪种能力」：

| 版本（**逐字**） | 正文里的落点 |
|---|---|
| `SmarTest 6.5.0: Added Link with editor and selection button.` | 图标表第 2 行（`raw/106959.png`） |
| `SmarTest 6.5.0: Added Pin this view button.` | 图标表第 3 行（`raw/106962.png`） |
| `SmarTest 6.5.0: Multi Hardware views can be opened.` | 功能清单第 4 条 `Allows you to compare the settings by …` |
| `SmarTest 6.5.2: Added Open new Hardware view button.` | 图标表第 4 行（`raw/111158.png`） |
| `SmarTest 6.5.2: Added RF hardware state button.` | 图标表第 10 行（`raw/114855.png`，`The button is active only for RF pins.`） |

**（推断）上表这五条「落点」是本页对出来的**——
**依据是版本记录里的按钮名与图标表里的功能名逐字相同；
但原文没有把版本段和图标表对上。这是推断。**
**尤其：`Multi Hardware views can be opened.` 这一条本页对到的是功能清单第 4 条，
而不是某一颗按钮**——**原文没有说它对应哪一行。**

**子主题另有一条，不属于本篇**：`Profiling of DC Scale cards with Hardware view` 那一篇自己的
`## Functional changes` 写的是 `Introduced in SmarTest 7.2.0`（**`in`，不是哨兵**）——
**那是 DC profiling 的引入版本，不是 Hardware view 的。**
**本页分开写，不把两者混成一条。**

**与 wiki 目标版本（SmarTest 7.10.3）的关系**：
**本篇最后一条是 6.5.2，6.5.2 到 7.10.3 之间有没有再改，本篇没有依据。**

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md`
（TDC 主题号 `69687`；本地 raw md：**5,273 字节**、**118 行**——
**字节是磁盘上的字节数，行数是换行符个数**）

**另外读了一篇：本篇 `Subtopics` 清单里的第五项、也正是本页 `## 语法 / 参数` 节自己声明
「取自」的那一篇**——
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.05_Profiling_of_DC_Scale_cards_with_Hardware_view.md`
（TDC 主题号 `136105`；本地 raw md：**6,951 字节**、**117 行**）。
**理由：定义文档只有 `Subtopics` 清单加一节正文，而本页 `## 语法 / 参数` 节逐字收的那一段
全部出自这一篇**——
**不读它，`## 典型用法` 只能写定义文档那一节，而 profiling 是本页唯一有步骤的部分。**
**⭐ 这一篇是 `sources:` 之外读的，特此声明；除此之外没有读第三篇。**

**本页没做的：**

- **定义文档的 11 张图，一张都没看**：`raw/353726.png`（那张带 (1)–(5) 编号的示意图）、
  `raw/106958.png` / `106959.png` / `106960.png` / `106961.png` / `106962.png` /
  `106963.png` / `106964.png` / `106965.png` / `111158.png` / `114855.png`（图标）。
  **所以「那一排图标长什么样」本页一个字都没有**，上面那张表只有题注与功能文字。
  §11.4 说 raw 里的图可读且该读。
- **子主题里的两张图也没看**：`raw/353618.png`（`Profiling in Hardware view`）、
  `raw/353741.png`（`DPS profile with`），以及 `## Results` 那两张
  `raw/136112.png` / `raw/142042.png`——**那是本页唯一能确认 `DPS Profile` 对话框长相的依据。**
- **`Subtopics` 清单里另外 10 篇一篇没读**（清单见 `## 和谁有关`）——
  **所以 digital pin / DPS 与 VI pin 的 Hardware view、多开视图、跨 site 找不一致设定，
  本页都没有。**
- **profiling 子主题 `## Related information` 那 7 个出口一个没读**——
  **所以「用 API 做 profiling」「Sample Code view 是什么」本页都没有。**
- **`Hardware Perspective` / `Pin Browser view` 没读** ——
  **本页与它们的关系只有本篇第一句话。**
- **没有交叉验证任何别处的文档**（§11：本页只写读到的两篇里有的）。
  **尤其：[[sequencer-controlled-utility-lines]] / [[utility-lines]] / [[waveform-view]] /
  [[pin]] 的 raw 都没读**——**本页与它们的关系是从「本页这两篇里那句话在讲什么」看出来的，
  没有从对面回校过。**
- **`layer: gui` / `stage: run` 不是本篇写的**——**本篇没有 `## Application` 这类自我定位段**，
  这个归属是本 wiki 的既有划分
  （**（推断）`run` 与「改设定、量值、抓波形」相符，但这是本页的观察，不是原文说的**）。

> ⚠️ **这两篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 编码损坏（§11.2 ① 那一族）：`鈥慴` = 被吃掉的 `-b`。** 逐字（定义文档）：
> `This is especially true when hardware settings depend on pattern鈥慴ased conditional jumps and
> match loops.`
> ——`pattern鈥慴ased` 就是 **`pattern-based`**：**`鈥` 是 U+2011 那类字符 UTF-8 三字节的头两个字节，
> 第三个字节被吃掉，而紧跟的 ASCII `b` 并进了第二个坏字**（所以拿 `based` 去 raw 里搜是搜不到的，
> 要搜 `鈥慴ased`）。**本页引文照原样留着坏字。**
>
> **② 同一个题注 `Zoom in button` 挂了两张不同的图，而两张图的功能都不是「放大」。** 逐字并列：
> `![Zoom in button](<../../../../raw/106959.png>)` 的功能是 `Link with editor and selection.`；
> `![Zoom in button](<../../../../raw/106961.png>)` 的功能是 `Zoom in on the Hardware view.`；
> 另外 `![Zoom in by large step button](<../../../../raw/106962.png>)` 的功能是 `Pin this view.`
> ——**三处错位叠加**：`106959.png` 与 `106961.png` 题注**逐字相同**，而其中只有后者的功能真是放大；
> `106962.png` 的题注写「大步放大」，功能却是 `Pin this view`。
> **（推断）题注是整列错位的（`106959` / `106962` 两个「放大」类题注被留给了前面两个非放大按钮）**；
> **依据只是这三行的错位形态，原文没有承认也没有否认。本页不替它改题注，也不据此改功能文字。**
>
> **③ 一个题注是光秃秃的 `1`。** 逐字：`![1](<../../../../raw/114855.png>)`
> ——功能写的是 `Show or hide properties.`（**只对 RF pin 有效**）。
> **本页照实并列。**
>
> **④ `Sampling Rate` 那张表在语料里被压平，列与卡名错位。** 逐字（原样）：
> ` | DPS128  | 1  |   | channels per test processor[1)](<#_136105__d2708e223>) |` /
> `100 ksps` / `   | 0.010 ms |` / ` | 2 ... 8  | 50 ksps  | 0.020 ms |` /
> ` | UHC4T  | 1  |   | channels par card  | 100 ksps  | 0.010 ms |`
> ——**两个问题**：**① 单元格被折成了多段连续行**（`100 ksps` 单起一行）；
> **② `channels par card` 里的 `par` 应为 `per`**（同处上文写的是 `channels per test processor`）。
> **XPS256 那一行的条件格是空的，而它下面没有 `2 ...` 那几行——即它只有一档。**
> **本页那张表是按字面重排的，一个字没改。**
>
> **⑤ 同一族编码损坏的第二处：`鈥慶` = `-c`。** 逐字（profiling 子主题）：
> `You can define the configuration of sequencer鈥慶ontrolled utility lines, which is programmed to
> hardware before any pattern execution.`
> ——`sequencer鈥慶ontrolled` 就是 **`sequencer-controlled`**（`鈥慶` 里的 `c` 被并进去了）。
> **这一句同时出现在本页 `## 语法 / 参数` 节里（脚本逐字收的），所以这一处在页面上看得见两次。**
>
> **⑥ `XPS256:For` 冒号后面没有空格。** 逐字（profiling 子主题的 `## About this task` 一节）：
> `- XPS256:For [DC Scale XPS256 card](<../../02_System_reference/02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>), changing the voltage range or the current range during profiling is supported, …`
> ——**同节的另外两条（`DPS128/64 and UHC4T:` / `DPS128:`）冒号后都换了行，只有这一条粘住了。**
> **本页照原样引。**
>
> **⑦ `## Related information` 七个链接首尾相接，中间没有任何分隔符。** 逐字（开头三节）：
> `[DPS operating mode of DC Scale cards](<../../02_System_reference/02.05_Test_Head_Cards/02.05.05.04_DPS_operating_mode_of_DC_Scale_cards.md>)[PMU operating mode of DC Scale cards](<…>)[DC_PROFILING_DEFINE](<…>)[DC_PROFILING_ENABLE](<…>)[DC_PROFILING_ON](<…>)[DC_PROFILING_OFF](<…>)[Sample Code view](<01.01.07.05.07_Sample_Code_view.md>)`
> ——**七个 markdown 链接连成一整行**（与 [[table-filter]] 、[[software-bin-summary-tab]]
> 那两页记的同类毛病同形；那两条本页引自那两页 wiki 页，不是本页这两篇 raw）。
> **这一行里还有个漏**：正文引过 `DC_PROFILING_DEFINE` 与 `DC_PROFILING_ON`，
> 而 `DC_PROFILING_ENABLE` / `DC_PROFILING_OFF` **只在 `Related information` 里出现**。
>
> **⑧ 子主题末尾的脚注被算进了 `## Functional changes` 段**（§11.2 ③ 那个现象），
> **而且脚注标记本身是坏的、句子语法也是坏的。** 逐字（子主题最后一行）：
> `[1)](<>) A test processors controls eight consecutive channels on DPS128.`
> ——**三个问题**：① **标记写成 `[1)`（缺右方括号），语料里其它地方是 `1)` 这种形态**；
> ② **`A test processors controls` 数不一致**（应为 `A test processor controls`）；
> ③ **它讲的是表格里 `[1)` 那个上标**（`channels per test processor` 那格），
> **却被挂在文件最后、落在 `## Functional changes` 之后。**
> **本页脚注处引文照原样。**
>
> **⑨ 代码块没有围栏。** 逐字（子主题 `## Example` 一节，UTSC 那一段）：
> `UTSC 1,RW; UTSC (2,3),RW,MASK; UTSC (5-8),RD`
> ——**这一行与 `After the pattern finishes, SmarTest applies: UTSC ALL,OFF.` 都是裸文本，
> 没有代码围栏**；同节的 UTSC 语法那两行原文用反引号包了。
> **本页正文里给这两行加了 `逐字` 与反引号，是为了可读；语料里它们不是代码块。**
>
> **⑩ 本篇没有 §11.2 ① 之外的别的损坏**（查过：定义文档正文里 1 处坏字，就是第 ① 条那一处；
> 子主题正文里 1 处，就是第 ⑤ 条那一处）。

`verified: doc-only`
