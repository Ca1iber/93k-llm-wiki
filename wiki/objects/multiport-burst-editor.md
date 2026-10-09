---
type: object
title: Multiport Burst Editor
layer: gui
stage: pattern
tags: [multiport-burst-editor, multiport-burst, port-burst, sync-group, pattern-tool, gui-editor, overview-page, expanded-mode]
related: [pattern-tool, pattern-editor, pattern-explorer, port-editor, testflow, pattern, smartest-7.1.3, cct-multiport-sequencer-synchronizer-api]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03_Multiport_Burst_Editor.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Multiport Burst Editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,303 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03_Multiport_Burst_Editor.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Icon | Function |
|---|---|
| !`Expand/collapse button`（raw: `../../../../agent-html/99926.png`） | Expands / collapses the current editor page. The other pages of the editor are not affected. The expanded mode shows<br><br>- the number of cycles per port burst on the Overview page.<br>- the Vector#, Instruction, and Comment column on a port burst page.<br>- the vectors of a sync group aligned in timeline.<br>- fail information per pattern on the Overview and the sync pages.<br><br>To activate the icon you must execute the testflow. |
| !`Enable expand selection mode`（raw: `../../../../agent-html/129178.png`） | Available only for the burst pages of a multiport burst editor.<br><br>Enables / disables the expanding (!`Expand/collapse button`（raw: `../../../../agent-html/99926.png`）) of only the selected CALL instructions of a port burst (`or burst`（raw: `02.08.04.16.02_Pattern_Editor.md`）). If enabled, the expanded port burst page will show the "Expand Selection Mode" entry. |
| !`Hide/Show all Sync Group Tabs`（raw: `../../../../agent-html/128933.png`） | Hides / shows (toggles) the sync group tabs (pages) on the current multiport burst editor. |
| !`Hide/Show all PortBurst tabs`（raw: `../../../../agent-html/128934.png`） | Hides / shows (toggles) the port burst tabs (pages) on the current multiport burst editor. |

<!-- 语法节 end -->

## 是什么

**Multiport Burst Editor 是 pattern 工具里的一个编辑器，管的是 multiport burst，以及组成它的
port burst。** 原文首句逐字（**注意它自称 `multiport editor`，不是标题上的 `Multiport Burst
Editor`**，见 `## 出处` ②）：

> 「A multiport editor is one of the pattern tools. It gives access to multiport bursts and the
> individual port bursts. Port bursts are pattern sequences for a specific port (group of pins).
> A port burst is always part of a multiport burst.」

**这一段给了三件事**：

| 说法 | 原文 |
|---|---|
| 它是什么 | `one of the pattern tools` |
| port burst 是什么 | `pattern sequences for a specific port (group of pins)` |
| 两者的关系 | `A port burst is always part of a multiport burst.` |

**「一个 port 就是一组 pin」是原文用括注写的**：`a specific port (group of pins)`。
**port burst 与 multiport burst 是包含关系**——**port burst 永远属于某个 multiport burst，
原文没有「不在 multiport burst 里的 port burst」这种说法。**

### 窗口结构：一个 Overview 页 + 若干 tab 页

逐字：

> 「You can open any number of multiport burst editors. Every instance of the multiport burst
> editor provides an Overview page plus one or more tabbed pages. These tabbed pages display the
> individual port bursts and the sync groups.」

**三件事**：**可以同时开任意多个实例**（`any number`）→ **每个实例 = 一个 Overview 页 +
一个或多个 tab 页**（`one or more`）→ **tab 页里装的是 port burst 与 sync group**。

三个页面的分工与差别（**原文 `Overview page` 那一行行首被一个图片链接打断**，见 `## 出处` ①）：

| 页 | 原文 | 排序 | 能不能隐藏 |
|---|---|---|---|
| **Overview** | `Overview page is always visible and shows all port burst on one page.`（**句首的 `The` 与它之间夹着一个图标链接**，见 `## 出处` ⑨） | — | **不能**（`always visible`） |
| **port burst 页** | `show the individual port bursts` | `The port burst tabs are ordered alphabetically.` | `These pages can be hidden.` |
| **sync group 页** | `show the port bursts per assigned synchronization group` | `Multiple sync group tabs are ordered alphabetically.` | `These pages can be hidden.` |

**sync group 页有个默认名字**：逐字 `(named DEFAULT unless differently named)`
——**没另起名字的 sync group 就叫 `DEFAULT`。**

**Overview 页在 expanded 模式下的两列**，逐字：

> 「In expanded mode the Overview page can show start cycle and start time per call as additional
> columns (must be set as Appearance option on the Pattern Tool preference page). The tooltip of
> these columns will show cycle count and duration per call.」

- **多出来的是两列**：`start cycle` 与 `start time per call`。
- **有前提**：`must be set as Appearance option on the Pattern Tool preference page`
  ——**得先在 `Pattern Tool preference page` 上把它设成 Appearance 选项**，否则这两列不出现。
- **列上悬停（tooltip）显示的是** `cycle count` 与 `duration per call`。
- **两处都写 `per call`，而 `call` 在本篇没有定义**（见 `## 出处` ⑦）。

### 两个颜色标记

逐字：

> 「The blue-white marker ![Results](<../../../../raw/129291.png>) indicates a current primary and
> expandable item.」
> 「The red-green marker ![Results](<../../../../raw/129292.png>) indicates an item with results.」

| 标记 | 意思（原文） |
|---|---|
| **蓝白** | `a current primary and expandable item`——**当前的主项、且可展开** |
| **红绿** | `an item with results`——**这一项有结果** |

**两个 marker 的图片 alt 文本都是 `Results`**（见 `## 出处` ③）——**只读 alt 分不出颜色，
区分靠 `blue-white` / `red-green` 两个词。**

### 主工具栏：与 Pattern Editor 大体相同，另加四个图标

逐字（**`extend` 是原文的拼写，见 `## 出处` ①**）：

> 「To a large extend, the icons for the multiport burst editor functions on the main toolbar are
> identical to those for the Pattern Editor. That includes the red cell coloring and icons
> indicating failure data. The following icons are provided for the multiport burst editor in
> addition or have an additional function:」

**「大体相同」的对象是 [[pattern-editor]]**，**并且点名相同的两项**：
`the red cell coloring`（红底格子）与 `icons indicating failure data`（失败数据图标）。

**在此之上另有四个图标**（**「四个」是本页数的**，原文只说
`The following icons are provided for the multiport burst editor in addition or have an additional function:` 然后往下列）：

| 图标 | 功能（原文） | 可用条件 |
|---|---|---|
| **Expand/collapse** | `Expands / collapses the current editor page. The other pages of the editor are not affected.` | **`To activate the icon you must execute the testflow.`** |
| **Enable expand selection mode** | 前半 `Enables / disables the expanding` ＋ 后半 `of only the selected CALL instructions of a port burst ([or burst]).`（**两半之间夹着一个图标链接，原文是一个整句**，见 `## 出处` ⑤） | **`Available only for the burst pages of a multiport burst editor.`** |
| **Hide/Show all Sync Group Tabs** | `Hides / shows (toggles) the sync group tabs (pages) on the current multiport burst editor.` | — |
| **Hide/Show all PortBurst tabs** | `Hides / shows (toggles) the port burst tabs (pages) on the current multiport burst editor.` | — |

**两个 Hide/Show 图标的作用域都写明了 `on the current multiport burst editor`**
——**只影响当前这个实例，不动别的实例**（与 `You can open any number of multiport burst
editors.` 对得上）。

**`Enable expand selection mode` 是唯一一个「只展开选中的 CALL」的开关**：原文那句话是
`Enables / disables the expanding` ＋ 一个图标链接 ＋
`of only the selected CALL instructions of a port burst ([or burst]).`
（**本页在这里拆成两段引，是因为中间那个图片链接把句子切开了**，见 `## 出处` ⑤ 与 ⑩），
而且**开了之后展开页上会多一个条目**：`If enabled, the expanded port burst page will show the
"Expand Selection Mode" entry.`

### 展开模式（expanded mode）显示什么：四种页各不相同

原文是四条 bullet，**一条一个位置**：

| 在哪个页 | 展开后多出什么（原文） |
|---|---|
| **Overview** | `the number of cycles per port burst on the Overview page.` |
| **port burst 页** | `the Vector#, Instruction, and Comment column on a port burst page.` |
| **sync group 页** | `the vectors of a sync group aligned in timeline.` |
| **Overview 与 sync 页** | `fail information per pattern on the Overview and the sync pages.` |

**三条要点：**

**① 展开是「按页」的，不是全局的。** 逐字
`Expands / collapses the current editor page. The other pages of the editor are not affected.`
——**只影响当前这一页，同一实例里的别的页不动。**

**② 展开有个硬前提：先执行 testflow。** 逐字 `To activate the icon you must execute the
testflow.` ——**这句话在 raw 里是独立一段**（见 `## 出处` ⑧），
**位置在 Expand/collapse 那条说明与 Enable expand selection mode 那条之间**；
**所以它说的是哪个图标，本页按位置理解为 Expand/collapse——这是推断，不是原文明写的。**

**③ `fail information` 只在两处出现**：Overview 与 sync 页（`on the Overview and the sync
pages`）——**port burst 页那一条没有它。**

## 典型用法

**原文没有 `## Procedure`、也没有 `## Before you begin`。** 全篇是一页**界面说明**：
讲窗口有哪几页、每个图标干什么。**所以本节不是原文给的步骤，而是「从原文能落成的动作」
加上原文自己写明的两个前提。** 凡下表的「依据」列引自原文的，都是本篇明写的。

| 要做的 | 依据（原文） |
|---|---|
| **同时看多个 multiport burst** | `You can open any number of multiport burst editors.` |
| **一次看全部 port burst** | Overview 页 `is always visible and shows all port burst on one page` |
| **按名字找某个 port burst** | port burst 页 `are ordered alphabetically` |
| **看某个 sync group 里的 port burst** | 打开它的 sync group 页；**没改过名的就叫 `DEFAULT`** |
| **看 port burst 的 cycle 数** | ① 展开 Overview 页；② **先执行 testflow** |
| **看 `Vector#` / `Instruction` / `Comment` 三列** | ① 展开 port burst 页；② 先执行 testflow |
| **看 sync group 里各 vector 的时间线对齐** | ① 展开 sync group 页；② 先执行 testflow |
| **看 per pattern 的 fail 信息** | ① 展开 **Overview 或 sync** 页；② 先执行 testflow |
| **让 Overview 多出 start cycle / start time 两列** | 在 `Pattern Tool preference page` 上设成 Appearance 选项 |
| **只想展开选中的 CALL 指令** | 开 `Enable expand selection mode`（**只有 burst 页有**），展开页上会出现 `Expand Selection Mode` 条目 |
| **把 sync group 页收起来 / 放出来** | `Hide/Show all Sync Group Tabs`（toggle） |
| **把 port burst 页收起来 / 放出来** | `Hide/Show all PortBurst tabs`（toggle） |

**顺序上原文只给了一条硬前提**：**展开模式要先执行 testflow**
（`To activate the icon you must execute the testflow.`）——
**它写在 Expand/collapse 那个图标的说明里**，而展开模式显示的四类内容都经这个图标。

**另一条前提是「配置先于显示」**：Overview 那两列**不是默认有的**，
原文用括注强调它
`must be set as Appearance option on the Pattern Tool preference page`
——**即先改偏好设置，再回来看列。**

**本页给不出的一条**：**怎么创建一个 multiport burst / port burst、怎么把 port burst 分到
sync group 里**——**原文全篇没有一句讲创建或编辑动作，只有「页上有什么、图标干什么」**；
那部分在本篇 `Subtopics` 列的四篇子文档里，**本页一篇都没读**（见 `## 出处`）。

## 和谁有关

- [[pattern-tool]] — **父页 / 归属**。原文首句 `A multiport editor is one of the pattern tools.`
  ——**它是 pattern tools 里的一个**。**本页只有这一句归属；pattern tools 一共几个、
  另外几个各干什么，在那一页。**
- [[pattern-editor]] — **工具栏的对照物，原文两处点它**。
  ① 图标：`To a large extend, the icons for the multiport burst editor functions on the main toolbar are identical to those for the Pattern Editor.`；
  ② `Enable expand selection mode` 那格的 `([or burst])` **链接就是指向它**
  ——**「或 burst」的所指在那一页**。**本页没有那页的任何事实。**
- [[pattern-explorer]] — **原文 `## Related information` 里的第一个名字**。
  **本页只有这个名字**：它和本编辑器的分工（谁启动谁、能不能从它开始）**在本页没有**。
- [[port-editor]] — **（推断）名字近、未必同物**。原文全篇**没有 `port editor` 这个说法**，
  只有 `port burst` 与 `a specific port (group of pins)`。
  **依据只是页名相邻；本页不判两者是不是一回事。**
- [[testflow]] — **一条硬前提的宿主**。Expand/collapse 那格写
  `To activate the icon you must execute the testflow.` ——**要看展开模式，先得把 testflow
  跑起来**。**本页只有这一句，testflow 本身怎么执行在那一页。**
- [[pattern]] — **port burst 的构成物**。原文说 port burst 是
  `pattern sequences for a specific port (group of pins)` ——**一条 port burst 是一串 pattern 序列**。
  **本页只有这一句；pattern 本身是什么、序列怎么排，在那一页。**
- [[smartest-7.1.3]] — **版本页**。本篇 `## Functional changes` 唯一一条就是
  `Introduced in SmarTest 7.1.3`。
- [[cct-multiport-sequencer-synchronizer-api]] — **（推断）名字最近的一页，本页没有依据**。
  原文有 `synchronization group` / `sync group` 与 multiport burst，
  **但一个字都没提到 API、也没提到 sequencer**。
  **依据只是页名里的 `multiport` / `synchronizer` 两个词；本页不判两者是不是同一件事。**
- `Pattern Tool preference page`（**未建**）— **Overview 那两列 Appearance 选项的宿主**。
  原文只给了名字与它在 `01_Getting_started/01.01_SmarTest_Work_Center/` 下的相对路径。
  **那一页本页没读，所以那个选项具体叫什么、在哪一格，本页不知道。**
- `Creating a multiport burst` / `Creating and assigning a port burst` /
  `Editing a multiport burst setup` / `Working with sync groups`（**四篇，均未建**）—
  **本篇 `Subtopics` 列的四篇子文档，本页一篇都没读。**
  **「怎么创建、怎么编辑、sync group 怎么用」全在那四篇**——
  **这是本页最大的空缺**，本页只有窗口结构与图标。
- `Definitions: Vector, Pattern, Burst, etc. ...`（**未建**）— **原文 `## Related information`
  里链它**。**port burst / multiport burst 的正式定义可能在那一篇**；
  **本页能给的定义只有首段那三句。**
- `Converting an ASCII Scan Setup Into a Binary Multi-Port Setup`（**未建**）—
  `## Related information` 里的最后一个名字，**指数据转换那一章**。**本页没读。**

## 版本

原文 `## Functional changes` **只有一条**，逐字：

- Introduced in SmarTest 7.1.3

**这条不是 §11.2 ② 那个哨兵。** 哨兵的措辞是 `Introduced before SmarTest 6.3.2`，
**而这一条写的是 `Introduced in SmarTest 7.1.3`——没有 `before`**，
**所以照字面读就是「7.1.3 引入」，不是「早于语料覆盖范围」。**

**一处对照**：本批次另读了父页 `02.08.04.16_Pattern_Tools.md`（[[pattern-tool]] 的 source），
**它 `## Functional changes` 里写的是 `SmarTest 7.1.3: Multiport Burst Editor added`**
——**两篇措辞不同（本篇 `Introduced in SmarTest 7.1.3` 对父页 `SmarTest 7.1.3: Multiport Burst Editor added`）、所指相同**。
**那一条不在本篇 raw 里，本页引它是为了说明两篇对得上，不是本页的事实来源。**

**与 wiki 目标版本的关系**：本 wiki 面向 **SmarTest 7.10.3**。
**本篇最新一条就是 7.1.3**——**7.1.3 到 7.10.3 之间这个编辑器有没有再变，
本篇没有任何条目，语料里也没有依据。**

详见 [[smartest-7.1.3]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03_Multiport_Burst_Editor.md`

**本页没做的：**

- **`Subtopics` 列的四篇子文档一篇都没读**（`02.08.04.16.03.01_Creating_a_multiport_burst.md`、
  `02.08.04.16.03.02_Creating_and_assigning_a_port_burst.md`、
  `02.08.04.16.03.03_Editing_a_multiport_burst_setup.md`、
  `02.08.04.16.03.04_Working_with_sync_groups.md`）——**这是本页最大的空缺**：
  **本篇 raw 里没有一句创建 / 编辑动作，本页也就给不出「怎么做一个 multiport burst」。**
- **一张图都没看。** 原文有 10 处图片引用：`raw/128878.png`（窗口总览）、`128874.png`
  （Overview 页图标）、`120065.png`（port burst 图标）、`128935.png`（sync group 图标）、
  `129291.png` 与 `129292.png`（两个 marker）、`99926.png` / `129178.png` /
  `128933.png` / `128934.png`（工具栏四个图标）。
  **§11.4 说 raw 里的图可读、且该读，本页没读**——
  **所以每个图标实际长什么样、Overview 页的列布局、两个 marker 的颜色，
  本页只能照原文的文字描述转述，没有看过。**
- **`Pattern Tool preference page` 没读** —— 所以 Overview 那两列的 `Appearance` 选项
  具体在哪一格、叫什么、默认值是什么，**本页只有「必须设它」这一句**。
- **工作单（`extract/.batch/8.txt`）提示可追加
  `99_Unlisted_or_Unreferenced/99.0136_Working_with_the_multiport_burst_editor.md`
  为第二 source，本页没有读它。** **理由是本页的 `sources:` 按硬规矩 2 不许改**
  ——**只读不列进 `sources:` 就等于页里有找不到出处的句子（§10 追溯）。
  所以那一篇里有什么，本页完全不知道。**
- **没有打开过工具，也没有实机验证。** `verified: doc-only`：
  **本页任何一个图标点下去什么反应、展开模式在实机上的样子，本页只有文档依据。**
- **除了 `## 版本` 里明写的那一处对照（父页 `02.08.04.16_Pattern_Tools.md`），
  本页没有交叉验证任何别处的文档**（§11：本页只写读过的 raw 里有的）。
- **`## Main toolbar icons` 那张表在 raw 里是散架的**——
  **本页正文里的四行表是按语义重排的转述，不是逐字**（原样见下 ④）。
- **「四个额外图标」这个数字是本页数的**，原文只说
  `The following icons are provided for the multiport burst editor in addition or have an additional function:`
  然后往下列，**没有编号、也没有说总数。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `To a large extend`——`extend` 是原文的拼写。** 逐字：
> `To a large extend, the icons for the multiport burst editor functions on the main toolbar are identical to those for the Pattern Editor.`
> ——**应为 `extent`（`to a large extent`）**。**本页引文照原样，正文里仍写「大体相同」。**
>
> **② 首句自称与标题不一致——这是本篇最要紧的一处。** 逐字：
> `A multiport editor is one of the pattern tools.`
> ——**标题（H1、frontmatter `title`）是 `Multiport Burst Editor`，首句却写 `A multiport editor`，
> 少一个 `burst`；紧接的下一句又写 `It gives access to multiport bursts and the individual
> port bursts.`，同一段里 `multiport burst` 是对的。**
> **本篇别处一律写 `multiport burst editor`**（如
> `Every instance of the multiport burst editor provides an Overview page plus one or more tabbed pages.`）
> ——**只有首句是 `multiport editor`。本页逐字引用，不替它补 `burst`。**
>
> **③ 两个不同图标的图片 alt 文本相同，都是 `Results`。** 逐字：
> `The blue-white marker ![Results](<../../../../raw/129291.png>) indicates a current primary and expandable item.`
> `The red-green marker ![Results](<../../../../raw/129292.png>) indicates an item with results.`
> ——**蓝白标记是 `129291.png`、红绿标记是 `129292.png`，两个 alt 却都是 `Results`**。
> **只读 alt 分不出颜色。本页照录，不替它改 alt、也不替它猜哪个 alt 更该叫什么。**
>
> **④ 工具栏那张表在 raw 里是散架的。** 逐字（**注意每行只有一根竖线、` | ` 单独成行**）：
> ```
>  |
>
> Icon
>
>  |
>
> Function
>
>  |
>
>  |  ![Expand/collapse button](<../../../../raw/99926.png>) |
> ```
> ——**表头 `Icon` / `Function` 与每一条记录都被拆成独立行，分隔符 ` | ` 单独成行**。
> **这是整个语料的表格压平形态**（[[dscp]] 那页记过同一形态）。**本页正文按语义重排成表，
> 属转述；要精确到原文行，得回 raw。**
>
> **⑤ `([or burst])` 括号套括号。** 逐字：
> `of only the selected CALL instructions of a port burst ([or burst](<02.08.04.16.02_Pattern_Editor.md>))`
> ——**链接文本自己带方括号 `[or burst]`，外面又套了一层圆括号**；
> §11.1 ② 剥掉链接标记后剩下的是 `([or burst])`。**本页照录，不替它删括号。**
> **另外这一句在 raw 里是被 `Enables / disables the expanding` 与
> `of only the selected CALL instructions` 中间的图片链接截断的**（如下 ⑩）。
>
> **⑥ `## Related information` 的链接全部首尾相接，中间没有任何分隔符。** 逐字：
> ```
> [Pattern Explorer](<02.08.04.16.01_Pattern_Explorer.md>)[Pattern Editor](<02.08.04.16.02_Pattern_Editor.md>)[Working with sync groups](<02.08.04.16.03.04_Working_with_sync_groups.md>)[Definitions: Vector, Pattern, Burst, etc. ...](<02.08.04.16.04.01_Definitions__Vector__Pattern__Burst__etc.md>)[Converting an ASCII Scan Setup Into a Binary Multi-Port Setup](<../02.11_Data_Conversion_and_Bridges/02.11.02.03.03.07_Converting_an_ASCII_Scan_Setup_Into_a_Binary_Multi-Port_Setup.md>)
> ```
> ——**五个链接粘成一串，没有逗号、没有空格**；去掉链接标记就是一句没有标点的名字串。
> （[[dscp]] 那篇记的是「两个链接粘在一起」，**这一篇是五个**。）
>
> **⑦ `per call` 里的 `call` 本篇没有定义。** 逐字：
> `can show start cycle and start time per call as additional columns`
> 与 `The tooltip of these columns will show cycle count and duration per call.`
> ——**两处都写 `per call`，而本篇全篇没有一个字解释 `call` 指什么。**
> 后文 `Enable expand selection mode` 那格出现过 `CALL instructions`
> ——**两者是不是一回事，原文没说。本页并列两处，不替它下定义。**
>
> **⑧ `To activate the icon you must execute the testflow.` 在 raw 里是独立一段。**
> 逐字：`To activate the icon you must execute the testflow.`
> ——**它说的是 `the icon`，即哪一个图标靠上下文位置决定**
> （紧跟其后的是 `Enable expand selection mode` 那一条，紧跟其前的是 Expand/collapse 那一条）。
> **原文没有把它放进任何一格功能说明里**（raw 的表格已散架，见 ④）。
> **本页正文按位置理解为 Expand/collapse：这是推断**，依据只是「它在两条图标记录之间，
> 且展开模式与执行 testflow 相关」。
>
> **⑨ Overview 那一行行首被图片链接打断。** 逐字：
> `The ![Show Multiport Burst in Hierarchy](<../../../../raw/128874.png>) Overview page is always visible and shows all port burst on one page.`
> ——**`The` 与 `Overview page` 之间插着一个图标链接**，中间的 `Show Multiport Burst in Hierarchy`
> 是那张图的名字（也是那个按钮的名字），**但在这个句子里它把 `The` 与 `Overview page` 切成了两段**。
> **本页引文照原样。**
>
> **⑩ 功能说明里的图片链接把句子切开。** 四条图标说明各夹着一个图标链接
> （`99926.png` / `129178.png` / `128933.png` / `128934.png`），
> **其中 `Enable expand selection mode` 那一条被切成了两半：**
> 逐字前半 `Enables / disables the expanding`，紧接一个 `![Expand/collapse button](<../../../../raw/99926.png>)`
> 链接，再逐字后半 `of only the selected CALL instructions of a port burst ([or burst]).`
> ——**本页正文把那一条拆成两段引来引，没有用省略号省字**
> （§11.1：引文里出现省略号就等于承认中间有字没抄）。
>
> **⑪ 本篇没有 §11.2 ① 那种编码损坏。** **本页通读过这一篇，`[一-鿿]` 字符 0 处**
> ——**所以本篇的语料问题全是结构与措辞层面的，没有坏字。**
> （对照：[[dscp]] 那页记的 `鈥`／`鈮` 一类**本篇没有**。）

`verified: doc-only`
