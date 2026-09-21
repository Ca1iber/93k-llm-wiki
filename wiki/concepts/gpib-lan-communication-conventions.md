---
type: concept
title: Conventions for GPIB/LAN communication
layer: L3
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.04_Conventions_for_GPIB_LAN_communication.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Conventions for GPIB/LAN communication

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**这一页不是 GPIB/LAN 的说明，是一张记号表。** 原文第一句就把范围说死了：

> 「The conventions in the table below are used **in this chapter** to describe
> GPIB/LAN communication」

也就是说：**它定义的是「本章后面那些命令行文里的符号各是什么意思」**，
不是命令本身、不是协议、不是接线。

**十一个符号**（照原文表转述；原文表在语料里是碎成一行一个 `|` 的形态，见「出处」）：

| 符号 | 原文定义 |
|---|---|
| `a_word:` | Defines an action name.（一个动作名） |
| `<a_word>` | Placeholder for a sub-action as defined later.（后面才定义的子动作占位） |
| `0x..` | **Answer SRQ code from the handler, sent as hex value.**（handler 回送的 SRQ 码，十六进制） |
| `[0x..]` | **An optional (ignored) answer SRQ code from the handler.**（可选的、会被忽略的 SRQ 码） |
| **`\|`** | **OR sign (for alternatives).**（或） |
| `string` | A command or answer string. |
| `.` | **An arbitrary character.**（任意一个字符） |
| *Italic letters* | A placeholder for variables, such as binning, positions an so on. `s = site, b = binning data` |
| `(...)` | A sub-expression. |
| `+` | The previous expression may be generated several times, but is generated **at least once (1-n)**. |
| `*` | The previous expression may be generated several times, **or it may not occur (0-n)**. |

**最该记住的一条限制**（原文以 `Note` 形式单列）：

> **Note The SRQ related conventions are not available for the LAN communication.**

**即：`0x..` 与 `[0x..]` 这两条只对 GPIB 有效，LAN 下用不上。**
这张表其余九条 GPIB / LAN 通用。

> **两个容易读漏的地方**：
> ① **`+` 是「1 到 n」，`*` 是「0 到 n」**——差别只在**能不能一次都不出现**。
> 原文对 `+` 的措辞是 `may be generated several times, but is generated at least once`，
> **读快了会以为两者一样的**。
> ② **`.` 是「任意一个字符」，不是「句号」**。原文写的是
> `An arbitrary character.`——**这一条表里只有它也长成标点的样子。**

## 典型用法

**1. 什么时候翻这一页**：在 GPIB/LAN 那一章里**读命令行法读不懂**的时候，
回来查某个符号是什么意思。它是**读别的东西时用的对照表**，不是操作步骤。

**2. 和 wiki 里其他页的分工**：本页**只解释符号**。
**具体有哪些命令、每个命令怎么拼，本页一个字都没有**——
原文说这张表是给 **`this chapter`** 用的，**而那一章本页一篇都没读**（见「出处」）。

**3. 判断「这个语法 LAN 下能不能用」时**：先看它有没有出现 `0x..` / `[0x..]`。
有，就是 GPIB 专有。

## 和谁有关

- [[project]] — 本页 `stage: project` 的理由：GPIB/LAN 是**测试程序对外通信**这一侧的事，
  不落在九个工艺阶段的任何一个上
- [[preprocessing-and-postprocessing-scripts]] — 同属
  `02.09_Test_Program_Management`，是同一章里另一篇「程序和外部怎么打交道」的页
- [[mtpt]] — 同属 `02.09_Test_Program_Management`，同批建页
- **未建的**：`GPIB` / `LAN` 通信本身的页，本 wiki 里**目前没有**

> **本页在交叉引用图里是个孤点**：这篇文档**一条 `](<…>)` 链接都没有**，
> **既没链出去、也没有别篇链进来**（本页 `sources:` 之外）。
> 它是**一整章的记号表**，位置决定它是叶子。

## 版本

- **Introduced in SmarTest 7.0.4**
- **SmarTest 7.2.3**：`LAN supported`
  （对照上面那条 `Note`：**7.0.4 引入时只有 GPIB，LAN 是 7.2.3 加的**——
  原文没有把这两件事写在一起，**这个对照是本页拼出来的，属推断**）

## 出处

`sources:` 一篇：
`02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.04_Conventions_for_GPIB_LAN_communication.md`

**本页没做的**：

- **这一篇只有一张表、一段 Note、两条版本记录，没有别的。** 本页把它全部转述了，
  **没有可"再读"的剩余部分**——但**表里每一条的定义本页都只用了原文那一句**，
  **没有替任何一条举例、也没有替任何一条推断它在命令里的实际效果**。
- **它所属的那一章（`02.09.01.03.06.01`）本页一篇都没读**：
  这张表是给那一章用的，**而那一章讲什么，本页不知道**。
- **`02.09_Test_Program_Management` 底下其余篇本页没读**。

> ⚠️ **本篇在语料里的形态**：那张表**不是 markdown 表格**，
> 是**碎成一行一个 `|` 的形态**（`Symbol` / 空行 / `|` / 空行 / `Definition` …），
> 和 [[mtp-shared-test-commands]] 语法节里那些参数表同一个毛病——这是语料转换的产物。
> 另有两处文字瑕疵，**本页都没替它改**：
> **`positions an so on`**（应为 `and so on`）、
> **`|`（OR）那一行的「符号」单元格在语料里是空的**——因为 `|` 本身撞上了表格语法。

`verified: doc-only`
