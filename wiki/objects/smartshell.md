---
type: object
title: SmartShell
layer: n/a
stage: project
tags: [smartshell, external-control, scripting, api, server, python, terminal, smartest-8.2.5, not-in-7.10.3, pdf-only]
related: [project, run, pin, level, timing, pattern, results, testflow, test-suite-control-api, smartest-8.2.5]
sources:
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# SmartShell

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**SmartShell 是 SmarTest 的外部脚本接口。** 原文三句话就是全部机制：

> 「SmartShell is an external scripting interface for SmarTest that allows external tools
> (for example, EDA tools or shell scripts) to control the test execution and receive the test
> results back.」

> 「SmartShell consists of a network-capable server component that can control a running instance
> of SmarTest and modify settings and parameters.」

> 「The server is accessed either through simple APIs that can be used from external applications
> such as EDA software, or from user scripts (for example, written in Python). It can also be used
> interactively through a text-based terminal interface.」

**拆成四条事实**：

| 问题 | 原文的答案 |
|---|---|
| **给谁用** | **外部工具**——原文举的是 EDA 工具、shell 脚本 |
| **干什么** | **控制测试执行**（`control the test execution`），并**把测试结果收回来**（`receive the test results back`） |
| **靠什么** | **一个能联网的 server 组件**（`a network-capable server component`），它控制**一个正在运行的 SmarTest 实例**，**改设置与参数** |
| **怎么接** | ① 从**外部应用**（如 EDA 软件）调 **simple APIs**；② 从**用户脚本**（例：Python）；③ **交互式**，走 **text-based terminal interface** |

### ⚠️ 先说结论：**本 wiki 的目标版本上没有这个接口**

原文 `## Functional changes` **只有一条**：`Introduced in SmarTest 8.2.5`。
**本 wiki 面向 SmarTest 7.10.3**（schema §11）。

**8.2.5 晚于 7.10.3，所以 SmartShell 在 7.10.3 上不存在。**

**这一条比上面那三句话重要得多**，而它已经在别处被反复记过了：

| 页 | 它怎么说 |
|---|---|
| [[pin]] | L3 一节的原话是「该接口在 **7.10.3** 下**不适用**」 |
| [[run]] | 有一节的标题就是「SmartShell —— **7.10.3 不可用**」 |
| [[pattern]] | 原话是「**不得把它当作可用的 L3 接口**」 |
| [[results]] | 有一节的标题是「SmartShell **仍然不可用**」 |

**所以本页的用途不是「教你怎么用 SmartShell」，而是「记下它在 7.10.3 上不存在、别把它当方案」这件事。**
（[[project]] 那一页也记了同一件事。）

### 语料里有什么 / 没有什么

**有的**：上面那三段话 + `Functional changes` 一条。**没了。**

**没有的**：原文接下来只有一句 `The SmartShell documentation is available as PDFs:`，
后面跟三本 PDF——

| 文档 | md 里的链接目标 |
|---|---|
| `Quick start guide` | `../../../../pdf/SmartShell_7_Quick_Start.pdf` |
| `User guide` | `../../../../pdf/SmartShell_7_User_Guide.pdf` |
| `Command reference` | `../../../../pdf/SmartShell_7_Command_Reference.pdf` |

**这三本 PDF 不在本语料里**（实测见 `## 出处`）。
**所以真正「怎么用」的那一层——命令、API 签名、报文格式、版本要求——本页一个字都没有。**

### 这一章只有这一篇

`02.15_SmartShell` 章下**只有一个文件**（就是 `02.15_SmartShell.md` 自己），
**没有子主题、没有 `## Related information`、没有 `## Procedure`、没有 `## Example`**。
**所以本页短，是语料只有这一屏——不是本页偷懒，也不是本页没读。**

## 典型用法

**语料未写。**

本篇**没有 `## Procedure`、没有 `## Before you begin`、没有 `## Example`、没有一条命令**。
原文唯一的「怎么用」是把读者指向那三本 PDF，**而 PDF 不在语料里**。
**所以本页不写步骤。** 下面两条是本页的推断，**不是文档事实**：

- **（推断）三种入口是并列的，不是三个阶段。**
  依据是原文那一句用的是 `either` 加 `or` 的并列句式，后面又接 `It can also be used interactively`——
  **是三个入口，不是一条流水线。**
- **（推断）这套接口不该被当成 7.10.3 上的可选方案。**
  依据是 `Introduced in SmarTest 8.2.5` 这个版本标（§11「版本始终写明」＋本 wiki 面向 7.10.3），
  **不是本篇的哪一句话。**

## 和谁有关

**本篇自己一条链接都没有**（除了那三本 PDF），所以下面每一层关系都写明依据。

**① 把它收进 `sources:` 的阶段页**（最硬的一层，可核）：

| 阶段页 | 依据 |
|---|---|
| [[project]] | **本页 `stage: project` 的依据**——本篇在它 `sources:` 里 |
| [[run]] | 在 `sources:` 里；正文另有专节讲它 7.10.3 不可用 |
| [[pin]] | 在 `sources:` 里；L3 一节讲它 |
| [[level]] | 在 `sources:` 里（**正文没有再提**） |
| [[timing]] | 在 `sources:` 里（**正文没有再提**） |

**② 只在正文提到它、`sources:` 里没有的阶段页**：

| 阶段页 | 它提到什么 |
|---|---|
| [[pattern]] | 说 SmartShell 在 7.10.3 不存在 |
| [[results]] | 专节「SmartShell 仍然不可用」 |
| [[testflow]] | 把它和 HVM 并列，说两处都没有「组装 testflow」的接口 |

**③ 同族邻居（推断）**：[[test-suite-control-api]]——
`log.md` 记着 schema 的 L3 定义改过一次：**SmartShell 因 `Introduced in SmarTest 8.2.5` 被移出，
L3 改列 Test suite control API / HVM API**。
**本篇一个字没提它**，所以这是「同属外部控制一族」的位置关系，**不是调用关系**（推断）。

**④ 三本 PDF（均不在语料里）**：`SmartShell_7_Quick_Start.pdf` /
`SmartShell_7_User_Guide.pdf` / `SmartShell_7_Command_Reference.pdf`——
**真正的文档在这三本里，语料只存了链接。**

**⑤ 版本页**：[[smartest-8.2.5]]。

## 版本

原文 `## Functional changes` **只有一条**：

- **`Introduced in SmarTest 8.2.5`**

**没有 `before` 哨兵值，没有第二条。** 版本页在 [[smartest-8.2.5]]。

> **这一条就是本页的结论**：**7.10.3 上没有 SmartShell。**
> 注意这句话的性质——**它不是「文档没写」，是「文档明写了引入版本，而那个版本比目标版本新」。**
> 两件事不一样：前者是本 wiki 的覆盖缺口，**后者是这条接口在本版本下不存在**。
> **别把前者当成后者，也别反过来。**

## 出处

`sources:` 一篇：
`02_System_reference/02.15_SmartShell/02.15_SmartShell.md`
（`350345.htm`，**1,064 字节，22 行**）——**整篇读完**。

**这一章只有这一篇**：`02.15_SmartShell/` 目录下**只有 `02.15_SmartShell.md` 一个文件**
（实测该目录 `ls -la` 就这一项），**没有子主题**。
所以在这里，「读整篇」等于「读完整个 `02.15_SmartShell` 章」——
**本页的篇幅上限就是这一屏。**

**本页没做的（含一条「语料里就没有」）：**

- ⚠️ **三本 PDF 一本都读不了——因为它们不在语料里。** 实测三条：
  ① `tdc-html/pdf/` 目录**不存在**；
  ② `tdc-html/raw/pdf/` 目录**也不存在**；
  ③ 在 `tdc-html/` 下按名字找 `SmartShell*`，**返回 0 个结果**
  （该目录下共有 69 个 `.pdf`，**全在 `raw/` 里，没有一个叫 SmartShell**）。
  **md 里的 `../../../../pdf/SmartShell_7_*.pdf` 与上游 `.htm` 里的 `pdf/SmartShell_7_*.pdf`
  都指向不存在的位置。**
  **所以「快速上手 / 用户指南 / 命令参考」的内容，本语料一个字都没有**——
  这**不是「本页没读」，是「语料里没有」**。**两者必须分清。**
- **没有第四篇可读**：本篇没有 `#### Subtopics` 段，也没有 `## Related information`。
- **本文档没有 `## Procedure` / `## Before you begin` / `## Example` / `## Syntax` 中的任何一个**，
  所以「典型用法」写不出步骤来。
- **[[smartest-8.2.5]] 版本页本页没读**。
- **阶段页的正文本页没有逐字通读**：上面「和谁有关」①②两张表里的「在 `sources:` 里 / 提到什么」，
  依据是**对 `wiki/stages/` 的检索结果**（frontmatter 的 `sources:` 块 + 正文里的 `SmartShell` 字样），
  **口径是「那一页说了这句话」，不是「那一页只有这句话」。**

**图**：**本篇没有图**——`raw/350345.htm` 里 `src=` 只有 `tdc.js`，md 里 `.png` / `.jpg` 引用数为 0。
**所以本页没有图证，也没有「图够不着」这类话。**

**核了上游 `.htm`：`raw/350345.htm`（2,369 字节）。结论：**

- ✅ **那三句话（定位 / server 组件 / 三种访问方式）与上游逐字一致**，转换没有丢字。
- ✅ **`Introduced in SmarTest 8.2.5` 上游就有**，且是**唯一**一条 `Functional changes`。
- ⚠️ **PDF 的链接路径被转换改写过，而且两种写法都落空**：
  上游是 `href="pdf/SmartShell_7_Quick_Start.pdf"`（相对 `raw/` → `tdc-html/raw/pdf/`，**不存在**）；
  md 改写成了 `../../../../pdf/SmartShell_7_Quick_Start.pdf`
  （从 `by-category/02_System_reference/02.15_SmartShell/` 往上四层 → `tdc-html/pdf/`，**也不存在**）。
  **这属于「上游就不在」那一类**——**源 PDF 本身就没进语料库，不是转换丢的，救不回来。**
- ⚠️ **上游的链接文字被拆成了两行，md 折成了一行**：上游是
  `Quick start` + 换行 + `guide`、`User` + 换行 + `guide`、`Command` + 换行 + `reference`，
  md 里是 `Quick start guide` / `User guide` / `Command reference`。
  **这是 §11.1 ①「折叠空白」，属于允许的规范化，不是丢字符。**
- ⚠️ **md 里 `The SmartShell documentation is available as PDFs:` 这一行前面多一个前导空格**
  （`Read` 读出来是 ` The SmartShell documentation is available as PDFs:`）。
  上游这一行在 `<div class="p">` 块内、**没有这个前导空格**。**转换留下的，本页照实记，不替它改。**

`verified: doc-only`
