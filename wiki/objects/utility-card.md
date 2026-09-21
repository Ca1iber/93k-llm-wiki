---
type: object
title: Utility Card
layer: n/a
stage: pin
tags: [utility-card, exa-scale, test-head-card, utility-lines, utility-power-supplies, pogo-block, hardware]
related: [utility-power-supplies, utility-pins-editor, utility-line-assignments, utility-line-view, utility-purpose-editor, sequencer-controlled-utility-lines, set-utility-lines, get-utility-lines, utility-pogo-block-utility-card-v93000-exa-scale-systems, pogo-block-compatibility, smartest-7.10.0]
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Utility Card

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Utility Card 是一张 V93000 EXA Scale 的 utility 资源卡：一块板子上给 256 条 utility 线
和几路 utility 电源。** 原文第一句：

> 「The Utility Card provides 256 utility lines and several utility power supplies on eight 4-row
> pogo blocks. The cards can reside in any slot of a V93000 EXA Scale system.」

**三件事一起来的**：**256 条线**、**几路电源**、**它们都从八个 4 行 pogo block 出去**。
**插槽不限**（`any slot`）。**注意是 EXA Scale 系统的卡，不是所有 V93000。**

### 两个型号，差别是「配哪个 SmarTest」

| 型号 | 用在哪个 SmarTest |
|---|---|
| `EK051` | **只有 SmarTest 8** |
| `EK051A` | **SmarTest 7（7.10 及以上）和 SmarTest 8 都用** |

> 原文：`There are two variants available, EK051 and EK051A. The EK051 Utility card is used in
> SmarTest 8 only. The EK051A Utility card is used in both SmarTest 7 (SmarTest version 7.10 and
> higher) and SmarTest 8.`

**（推断）选型只看一件事：你跑不跑 SmarTest 7。**
跑 SmarTest 7 就只能 `EK051A`——**依据是上面那句里 7.10+ 只出现在 `EK051A` 那一句**。
**注意文档说的是 SmarTest 7.10 及以上，不是 7.x 全部**。

### 它是「可选的替换件」——替换掉的是系统自带的那点 utility 资源

**这个定位是本节最重要的一条**，因为原文用了 `optional` 和 `replaces` 两个词。
基本配置的 EXA Scale 系统自带**少量**内部 utility 资源：

| 基本配置自带（`internal utility resources`） | 数量 |
|---|---|
| 静态控制的 utility 线 | **32 条** |
| `+5 V` utility 电源 | 1 路 |
| legacy `SE-UDPS` 供电的替代 | 1 处 |

**装上 Utility Card 之后，替换掉的是**：

> 「The optional Utility Card, replaces the internal utility lines and the internal +5 V utility
> power supply and provides」

| Utility Card 提供 | 对比 |
|---|---|
| **256 条动态控制的 utility 线** | **32 条静态 → 256 条动态** |
| **1 路 `+5 V` utility 电源，电流更大** | 换掉内部那路 `+5 V` |
| **legacy `External utility power supply` 的替代** | **换掉外置那套** |
| **1 路提供 `+15 V` / `-15 V` 的 utility 电源** | 基本配置里没有 |
| **2 路浮空 `24 V` utility 电源** | 基本配置里没有 |
| **可装多张** | **`Multiple Utility Cards can be installed.`** —— 原文：`This enables high scalability of the provided utility resources.` |

**两个词值得盯住**：**「静态控制」→「动态控制」**（32 → 256 那一步不只是数量），
和 **「浮空」**（`floating` 那两路 24 V）。

> ⚠️ 上面那张表最后两行在原文里是一条 bullet 被换行切成两条的
> （第 4 条以 `and` 结尾，第 5 条是 `two floating 24 V utility power supplies.`）。
> **本页按「一路 ±15 V 电源」+「两路浮空 24 V 电源」读，
> 但这个断行让「一路电源同时提供 +15/-15/两个 24V」在字面上也读得通**——
> **原文没说清，本页不替它定。逐字见 `## 出处`。**

### 出口：八个 4 行 pogo block

> 「The utility lines and utility power supplies of a Utility Card are routed to eight 4-row
> utility pogo blocks.」

**线和电源是同一个出口**（`utility lines and utility power supplies` 一起 route 过去），
**所以 pogo block 上既有信号也有电源**。
**它的排布与走线约束在 pogo block 那几页里，本页没有**（见 `## 和谁有关`）。

### 这一页是「族首页」，四篇子主题它一篇都没展开

原文的 `#### Subtopics` 列了四篇，**本页一句它们的正文都没有**：

| 子主题 | 本该讲什么（**按标题**） |
|---|---|
| `Utility Card sitemap` | **这一族文档的地图** |
| `Utility Card specifications` | **规格** |
| `Utility Card functionality and features` | **功能与特性** |
| `Utility Card specific setup tasks` | **这张卡专属的设置任务** |

**（推断）「256 条线怎么用、引脚怎么分配、电源怎么开」都在那四篇里**——
**依据只是这四个标题的字面**。**本页只有「它是什么、有几个型号、替换掉什么、从哪儿出去」。**

## 典型用法

**原文**没有 `## Procedure`、没有 `## Before you begin`、没有 Example。
**本页因此没有操作步骤可写**——**这不是本页漏了，是这篇文档没有**。

**能从上文推出来的只有三条「选型/装配」层面的结论：**

| 你要做的 | 依据（**都在原文里**） |
|---|---|
| **配 SmarTest 7** | 只能 `EK051A`（`EK051` 是 SmarTest 8 专用） |
| **要更多 utility 资源** | **装多张**——原文说 `Multiple Utility Cards can be installed.` 且 **任意插槽** |
| **要动态控制的线** | **必须上这张卡**——基本配置只有 32 条静态线 |

**真正的用法（怎么用那些线、怎么开那些电源）在四篇子主题里，本页没读。**

## 和谁有关

- [[utility-power-supplies]] — **同族的电源侧**。本页说卡上有 `+5 V`、`+15 V` / `-15 V`、
  两路浮空 `24 V`；**那一路电源具体怎么配、怎么开，在本页之外**
  （**（推断）**：那页讲的就是本页列出的这几路电源，**依据只是页名**）。
- [[utility-pins-editor]] / [[utility-line-assignments]] / [[utility-line-view]] /
  [[utility-purpose-editor]] — **软件侧的四个入口**。
  本页说卡提供 **256 条动态控制的 utility 线**；**这些页是「怎么分配/怎么看这些线」的地方**。
  **本页只有线的数量与「动态控制」这四个字，没有任何编辑或查看界面。**
- [[sequencer-controlled-utility-lines]] / [[set-utility-lines]] / [[get-utility-lines]] —
  **线的两种控制方式**。本页只说「动态控制」；**哪几条归 sequencer 管、命令怎么写，
  在这三页里，不在本页。**
- [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] — **最直接的下游**。
  本页说线的电源「routed to eight 4-row utility pogo blocks」，
  **那个 pogo block 自己的引脚排布与设计规则在那页里**。
- [[pogo-block-compatibility]] / [[pogo-pad-and-via-design]] — **板上设计侧**。
  本页只出现 `pogo blocks` 这个词组一次，**pogo 的兼容性与 pad/via 设计本页一个字都没有。**
- [[pin-utility]] — **对象侧同类**。utility 线是 pin 的一种；
  **本页没有讲任何 pin 属性。**
- [[smartest-7.10.0]] — **版本页**。本页 `## 版本` 唯一的落点。
- [[error-utility-power-supply-not-enabled]] — **错误侧**。**（推断）**：
  它讲的是「utility 电源没开」这个错误，**和本页那几路电源是同一批对象**；
  **依据只是页名。本页没有关于这个错误的任何事实。**
- `Utility Card specifications` / `Utility Card functionality and features` /
  `Utility Card specific setup tasks` / `Utility Card sitemap`（**均未建**）—
  **本页的四篇子主题，一篇都没读**（见 `## 出处`）。
- `Internal utility resources - V93000 EXA Scale systems`（**未建**）—
  **对照组**。本页说的「替换掉什么」全靠它作基准（32 条静态线 / 一路 `+5 V` / `SE-UDPS`）。
  **本页没读它，所以那三项在基本配置里长什么样本页不知道。**
- `External utility power supply`（**未建**）— **legacy 外置电源**，本页说卡把它替换掉。
  **本页没读它。**
- `SE-UDPS`（**未建**）— **legacy 内部电源**，同样只是被本页提了一次。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- **Introduced in SmarTest 7.10.0**

**即：整张 Utility Card 是 SmarTest 7.10.0 引入的**，此后到本 wiki 面向的 **7.10.3** 之间
**没有别的变更条目**。

> **这条和正文里的型号说明要对着看**：版本说 7.10.0 引入，
> 而型号那条说 `EK051` **只有 SmarTest 8 用**、`EK051A` 从 **SmarTest 7.10 及以上**起用。
> **两者不矛盾**——`Introduced in` 说的是这张卡的整体，**不是某个型号**。
> **本页并列两处，不替它们调和措辞。**

## 出处

`sources:` 一篇：
`02_System_reference/02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md`

**本页没做的：**

- **四篇子主题一篇都没读**：`Utility Card sitemap`、`Utility Card specifications`、
  `Utility Card functionality and features`、`Utility Card specific setup tasks`。
  **这是本页最大的空缺**——**规格（电压/电流范围、精度）、功能清单、
  这张卡专属的设置步骤，本页一个字都没有**，
  本页只有原文那**三段正文**（第一句 + 内部资源对比 + pogo 出口）。
- **`## 语法 / 参数` 节是空的，而且这是脚本的正确行为。**
  骨架那几句说的是：定义文档里**没有** `Syntax` / `Parameters` / `Example` 这类段标记，
  跟着 `Subtopics` 找一层也没有。**本页照它原样留着**（§4：不许 LLM 补语法节）。
  **所以本页的「语法 / 参数」为空，不等于「这张卡没有参数」，而是「这篇文档没有段标记」。**
- **一张图看了没有：没有。** 原文有一张 `353302.png`（alt 文本 `Utility Card photo`），
  **本页没看它** —— **所以这张卡长什么样、有几个连接器、板子多大，本页完全不知道。**
- **`Internal utility resources - V93000 EXA Scale systems` 没读** ——
  所以「32 条静态线 / 一路 `+5 V` / `SE-UDPS` 替代」这三项**本页只有数量与名字**，
  它们怎么用、区别在哪，**本页不知道**。
- **`External utility power supply` 与 `SE-UDPS` 都没读。**
- **`Related information` 段不存在于本篇**，所以本页没有「原文推荐接着读什么」这条线索。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：本页 `layer: n/a`，所以本页没有去别处找它的层级定位。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① bullet 断行，导致「一路还是两路电源」读不通。** 原文最后两条 bullet 逐字：
> `- one utility power supply providing +15 V, -15 V and`
> `- two floating 24 V utility power supplies.`
> **第 4 条以 `and` 结尾、第 5 条另起一个 bullet** ——
> 照字面连读是「**一路** utility 电源，提供 +15 V、-15 V 和**两路**浮空 24 V 电源」，
> **一路电源不可能同时是三个东西**；
> 拆开读是「一路 ±15 V 电源」+「两路浮空 24 V 电源」。
> **两种读法都成立，原文没说哪个对。本页按拆开读，并在 `## 是什么` 里标了这个歧义。**
>
> **② 「替换 legacy `SE-UDPS`」那一项在两句里说了两遍，措辞不同。**
> 讲内部资源时是：`a replacement of the legacy SE-UDPS supply`；
> 讲卡提供的清单时是：`a replacement of the legacy External utility power supply`。
> **同一个「替换掉 legacy 什么」的位置，一处写 `SE-UDPS`、
> 一处写 `External utility power supply`** —— **两个不同的东西被放在同一个位置上。**
> **本页照原文分别引，不替它们统一。**
>
> **③ 那张 bullet 清单第一句的主谓不接。** 原文逐字：
> `The optional Utility Card, replaces the internal utility lines and the internal +5 V utility
> power supply and provides`
> ——**`The optional Utility Card,` 后面多一个逗号**（读起来像插入语，但没有后半个逗号），
> 句子到 `provides` 就断了，直接接 bullet 列表。**本页照原样引。**
>
> **④ 图片被吞进 bullet 里。** 原文最后一条 bullet 的下一行紧跟着
> `   ![Utility Card photo](<../../../../raw/353302.png>)`，
> **缩进使它成了 bullet 内容的一部分**——**结构上那张卡的照片成了「两路 24 V 电源」这一条的内容。**
>
> **⑤ `EK051` / `EK051A` 与 SmarTest 版本的那句里，
> 「SmarTest 7」和「SmarTest version 7.10 and higher」并列。**
> 原文：`used in both SmarTest 7 (SmarTest version 7.10 and higher) and SmarTest 8`
> ——**先写 `SmarTest 7`，再在括号里缩到 `7.10 and higher`**，
> **照外层读会以为 7.x 全系列都能用。本页在正文里按括号里的那个限制写。**
>
> **⑥ 本篇没有 §11.2 ① 那种 `鈥` 形态的编码损坏**（本页查过 `鈥` / `渭` / `卤` / `鈮`，0 处）。

`verified: doc-only`
