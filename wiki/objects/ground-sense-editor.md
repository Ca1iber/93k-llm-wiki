---
type: object
title: Ground sense editor
layer: gui
stage: pin
tags: [ground-sense-editor, gui, ground-sense, pin-scale-5000, pogo, pin-configuration, site]
related: [pin-configuration-tool, ps5000, digital-pins-editor, pogocabling-section, pogo-block-compatibility, pin, smartest-7.10.3]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.09_Ground_sense_editor.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Ground sense editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Ground sense editor 是 Pin Configuration Tool 里的一个 GUI 编辑器，给每个 site 配 ground sense pogo。**
原文第一句就是全部定义：

> 「The ground sense editor allows you to configure the ground sense pogo(s) for each sites, when using
> the Pin Scale 5000 card.」

⚠️ **`for each sites` 里的 `sites` 是复数，原文如此**（见 `## 出处` ①）。

**这一句里有三个限定，一个都不能漏：**

| 限定 | 原文（逐字） |
|---|---|
| 配的是什么 | `the ground sense pogo(s)` |
| 单位是什么 | `for each sites` |
| **前提是什么** | **`when using the Pin Scale 5000 card`** |

**第三行是本页最重要的一条归属：它是 Pin Scale 5000 卡专用的编辑器。**

### 它在界面上的位置：一个页签（**图证**）

本篇对 `raw/` 的引用**恰好一处**：`355947.png`（559 × 140，5,592 字节，**本页用 Read 工具打开看过**）。
**⚠️ 下面这一节的内容来自那张图，不是来自正文文字**——**图里的字搜不到**，
所以按 §11.4 单独标成**图证**。

| 图上看到的 | 说明 |
|---|---|
| **两个并排的页签：`Ground Sense` 与 `Digital Pins`** | **这个编辑器是一个页签**，左邻/右邻是 `Digital Pins` |
| 表格两列：`Site(s)` / `Ground Sense Pogo(s)` | **与正文那句 `consist of the following cells` 对得上** |
| **最左边还有一列行号 `1` / `2` / `3`** | **正文那两个单元格清单里没有它** |
| 三行数据：`1` → `10133,10233`；`2` → `30117,30217`；`3` → `Ground Sense Pogo(s)` 那一格是空的 | 见下两条推断 |

**两条从图上读出来、原文一个字没写的（推断）：**

| # | 推断 | 依据 |
|---|---|---|
| 1 | **一格（一个 site）可以填多个 channel ID，用逗号分隔** | 图上第 1、2 行的格子里各是两个数字、以逗号相连 |
| 2 | **那一格可以留空** | 图上第 3 行（site 3）的 `Ground Sense Pogo(s)` 格是空的 |

**第三条推断（更弱）**：图上四个值的**末两位**是 `33` / `33` / `17` / `17`，
而正文说 `Pin number 17 is the ground pin of SD and HD pogo blocks, while pin number 33 is the ground pin of VHD pogo blocks`——
**两者同形**，**（推断）那一串数字里带着 pogo pin 号**。
**依据只有「末两位对得上」这一点；原文没有把图和 pin 号连起来。这是推断。**

**⚠️ 这张图的版本要交代清楚**（§11.4 那条坑）：**图没有版本标注。**
本篇 `## Functional changes` 只有一条 `Introduced in SmarTest 7.10.3`、**没有改名记录**，
所以**核不出「`Ground Sense` / `Digital Pins` 这两个页签名是不是 7.10.3 的写法」**——
本页只声称「**这张图上写的是这两个名字**」，**不把它们当现名用**。
（**结构性的东西不受这条影响**：它是一个页签、有哪几列、左边多一列行号——这些不随版本变。）

### 两个单元格（正文逐字）

原文 `The ground sense editor consist of the following cells.` 之后给的是一张两行的表，逐字：

| 单元格（逐字） | 原文的说明（逐字） |
|---|---|
| `Site(s)` | `Test site(s).` |
| `Ground Sense Pogo(s)` | `Channel ID.` |

**第二格的说明只有两个词：`Channel ID.`**——**即那一格里填的是「channel ID」**，
这与图上的 `10133` / `10233` 这类五位数吻合（**推断**，依据是两处指的都是同一格）。
**⚠️ 那张表在语料里没有表头行、第二行还缺一个结尾的 `|`**，见 `## 出处` ④。

### 一条给出具体数字的事实：pin 17 与 pin 33

> 「Pin number 17 is the ground pin of SD and HD pogo blocks, while pin number 33 is the ground pin
> of VHD pogo blocks, see `Pin Scale 5000 pogo pin assignment`.」

（那一行末尾在原文里是一个链接，目标是
`<../02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md>`。）

| pin 号 | 是哪种 pogo block 的接地脚 |
|---|---|
| `17` | `SD and HD pogo blocks` |
| `33` | `VHD pogo blocks` |

**⚠️ 这两个数是「pogo block 上的 pin 号」，不是 channel ID**——
**图上填的是 channel ID（如 `10133`），两者不是同一个东西**（推断，
依据是正文把 `Pin number` 与表格里的 `Channel ID` 分开称呼）。
**`SD` / `HD` / `VHD` 三种 block 是什么、pin 号在 block 上怎么排，本篇一个字没有**（见 `## 出处`）。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有一条命令行、没有一个 API 签名。**
能落成步骤的只有「单元格清单 + pin 号那句 + 那张图」。**下面这条顺序是本页拼的**（**不是原文给的**）：

| 步 | 做什么 | 依据 |
|---|---|---|
| 1 | 前提：用的是 **Pin Scale 5000** 卡 | 正文 `when using the Pin Scale 5000 card` |
| 2 | 打开 Pin Configuration Tool 里的 **`Ground sense editor`**（一个页签） | 本篇的路径（`02.08.04.18.03.09`）+ **图证**（页签名 `Ground Sense`） |
| 3 | 在 `Site(s)` 列选中要配的 site | 表里第一格 `Site(s)` / `Test site(s).` |
| 4 | 在 `Ground Sense Pogo(s)` 列填该 site 的 channel ID | 表里第二格 `Ground Sense Pogo(s)` / `Channel ID.` |
| 5 | 要填多个就用逗号分开；不配就留空 | **图证（推断）**——原文一个字没有 |

**哪些是文档事实、哪些是推断，上表最后一列已经标了。** **第 5 步两条全出自图。**

### 本页没给的

**填完要不要保存、什么时候生效、一个 site 最多能填几个、填错了会怎样、能不能批量配多个 site**——
**本篇一篇都没有**，本页也不替它补（见 `## 出处`）。

## 和谁有关

- [[pin-configuration-tool]] —— **本页的父工具**。本篇的路径是 `02.08.04.18.03.09`，
  即挂在 `02.08.04.18.03`（Elements of the Pin Configuration Tool）下面；
  [[pin-configuration-tool]] 那页把 `Ground sense editor` 列在它的**十个编辑器**里，
  职责逐字是 `Select sites for ground sense pins.`
  （**那一页读的 raw 是 `02.08.04.18.03`，本页没读那篇**）。
  **那一页的版本行里还有 `SmarTest 7.10.3: Ground sense added`，与本篇的 `Introduced in SmarTest 7.10.3` 互相印证。**
- [[ps5000]] —— **本页的前提：只有这张卡用得上它**。原文 `when using the Pin Scale 5000 card`。
  **⚠️ 那一页在本 wiki 里还没建**（它是 `extract/dangling.csv` 上的悬空目标，
  按该文件的记载是 **7 处**引用；**这个数会随建页变**）。§9.1 允许链它。
- [[digital-pins-editor]] —— **同级的另一个编辑器，而且这条关系是图给的**：
  图上 `Ground Sense` 与 `Digital Pins` 两个页签并排。
  **⚠️ 正文一个字都没提它**；[[digital-pins-editor]] 那页本页也没读。
- [[pogocabling-section]] —— **`SD` / `HD` / `VHD` 这三个 pogo block 名词的对口页**。
  本篇要你认 pin 号，却**没有解释这三种 block**。**那一页本页没读**（取材边界）。
- [[pogo-block-compatibility]] —— **同族的 pogo block 页**（在 `concepts/` 下）。**本页没读**（取材边界）。
- [[dut-board-grounding]] —— **「接地」这件事的对口概念页**（在 `concepts/` 下）。
  **⚠️ 两页不是同一个东西**：本页讲的是**接地的 sense 线怎么指**，那一页讲的是**板级接地**。
  **本篇没有一句话提到它，本页也没读那一页**（取材边界）。
- [[pin]] —— **stage 页**。本页 `stage: pin` 的理由：它配的是 pin 配置里的一项。
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分；
  [[pin]] 那页的编辑器清单里也列着本页。
- [[smartest-7.10.3]] —— **版本页**。本篇 `Introduced in SmarTest 7.10.3`；
  [[smartest-7.10.3]] 那页也把本篇列在自己的清单里。
- `Pin Scale 5000 pogo pin assignment`（**未建**）—— **pin 17 / 33 那半句的出口**，
  也是**本篇正文链的唯一一个外部文档**。**本页没读**——
  所以「pin 号在 block 上怎么数、SD/HD/VHD 各占哪些脚」本页没有。
- `Pin Scale 5000 ground sensing`（**未建**）—— `## Related information` 里**唯一一条**。
  **本页没读**——**所以「ground sensing 这个机制本身是什么、为什么每 site 要指一个 pogo」本页没有。**
- `Ground Sense` / `Digital Pins`（**图里的字，不是文档名**）—— **图证**。
  这两个字符串在语料文本里另有出现（本页查过：分别是 **7 篇** / **37 篇**），
  **但「这两个页签并排」这件事只在那张图里**；而图里的 channel ID `10133` 在整篇语料里是 **0 篇**
  （本页查过）——**这就是图证与文本证的区别**（§11.4 ④）。

## 版本

原文 `## Functional changes` 段**只有一行**，逐字：

- `Introduced in SmarTest 7.10.3`

**这一条不是哨兵值**（§11.2 ② 的哨兵写法是 `Introduced before SmarTest 6.3.2`）：
它带明确版本号、措辞是 `in`。**所以读成「7.10.3 引入了 ground sense editor」。**

**它和本 wiki 面向的版本是同一个数**：本 wiki 面向 **SmarTest 7.10.3**——
**即这个编辑器是当前版本才有的东西。**
[[pin-configuration-tool]] 那页里同一条版本行（`SmarTest 7.10.3: Ground sense added`）
**把它写成「当前版本最新的一条」**。

**本篇没有的东西**（照实记，不替它补）：**没有第二条**。
所以「Pin Scale 5000 的 ground sensing 是哪一版有的」「`Ground Sense` 页签改过名没有」，
**本篇都答不了**——**后者正好是 §11.4 要求「从图上读到的名字必须去 `## Functional changes` 核一遍」的那一步，
本篇核不出来**（见 `## 出处`）。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.09_Ground_sense_editor.md`
（frontmatter `source_topic` = `355935.htm`；**959 字节 / 25 行**，**整篇读完**。
口径按 §11.5：字节是 `st_size`，行数是 `wc -l`，本语料末行带换行，两者恒等）

**本页读了的图**：本篇对 `raw/` 的引用**恰好一处**——
`![Ground sense editor](<../../../../raw/355947.png>)`。**该文件存在**
（`F:\master-dev\dorm-wsl-sytest\tdc-html\raw\355947.png`，**5,592 字节，559 × 140**），
**本页用 Read 工具打开看过**；`## 是什么` 里标成**图证**的几节就是从这张图读出来的。
**注意它搜不到**：拿图里的 `10133` 去 `by-category/` 下搜是 **0 篇**（本页查过），
**因为那是图里的字，不是文本。**

**本页没做的：**

- **`## Related information` 里唯一一篇没读**：`Pin Scale 5000 ground sensing`（`02.05.04.02.03.03`）。
  **后果说清**：**「ground sense 是干什么用的、为什么每 site 要指一个 pogo」本页一个字都没有**——
  本篇只说了**在哪填**，没说**为什么填**。
- **正文里 `see` 后面指的那篇没读**：`Pin Scale 5000 pogo pin assignment`（`02.05.04.02.06`）。
  **所以 pin 17 / 33 这两个数在 pogo block 上怎么排、`SD` / `HD` / `VHD` 三种 block 各是什么，本页没有。**
- **父文档 `02.08.04.18.03`（Elements of the Pin Configuration Tool）没读**——
  本页对「它是十个编辑器之一、职责是 `Select sites for ground sense pins.`」的了解，
  **全部来自 [[pin-configuration-tool]] 那个 wiki 页**（本页读过那一页），**不是来自 raw 交叉核对**。
- **本篇一个 `#### Subtopics` 段都没有**（本页查过：出现 **0** 次）——
  **所以本篇没有子页可读，也没有子页可漏。**
- **本篇没有 `## Procedure` / `## Before you begin` / `## Example` / `## Errors` / `## Warnings`，
  也没有一条命令行、一个 API 签名。**
  `## 语法 / 参数` 节因此是空的：**脚本的判据是「有没有 `Syntax` / `Parameters` / `Example` 段标记」，
  本篇一个都没有**——**这不是本篇缺内容，是它的「语法」只有那两个单元格**。
  没有 `## Errors` / `## Warnings` 段也意味着本页**没有「报错条件」节**
  （不是漏写——骨架里本来就没有这一节）。
- **一处没跑、一个界面没开。** `verified: doc-only` 指的就是这件事
  （§11：文档里有 ≠ 这台机器上能用）。**尤其：填错 channel ID 会怎样，语料一个字没有。**
- **`layer: gui` / `stage: pin` 不是本篇写的**——本篇没有 `## Application` 这类自我定位段，
  这两个值是本 wiki 的既有划分。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **`for each sites` 里的 `sites` 是复数。** 逐字：
> `The ground sense editor allows you to configure the ground sense pogo(s) for each sites, when using the Pin Scale 5000 card.`
> ——**`each` 后面跟复数**，按语法应是 `each site`。**同一句里 `pogo(s)` 却用了带括号的单复数写法，
> 一句里两种处理，本页照原样引。**
>
> ② **`consist` 缺第三人称单数。** 逐字：
> `The ground sense editor consist of the following cells.`
> ——**应是 `consists`。**
>
> ③ **图片与紧随其后那句话之间没有空格、没有换行。** 逐字（整行）：
> ` ![Ground sense editor](<../../../../raw/355947.png>)The ground sense editor consist of the following cells.`
> ——**`)` 后面直接跟 `The`**，中间一个字符都没有（行首另有一个前导空格）。
>
> ④ **那张「单元格」表不成形：没有表头行，第二行还少一个结尾的 `|`。** 逐字（三行原文）：
>
> ` | Site(s)  | Test site(s). |`
>
> ` | Ground Sense Pogo(s)  | Channel ID.`
>
> ` |`
>
> ——**第一行首尾都有 `|`；第二行只在开头和中间有，结尾那个 `|` 没了**；
> 表后面还单独占了一行，整行只有一个 `|`。
> **所以「这两列各叫什么」在这张表里没有表头可读**——列名的来源是**图**（见 `## 是什么`）。
>
> ⑤ **本篇没有 §11.2 ① 那种编码损坏**（本页查过：全文汉字 **0** 个、`鈥` **0** 处、
> 非 ASCII 字符 **0** 个）。

`verified: doc-only`
