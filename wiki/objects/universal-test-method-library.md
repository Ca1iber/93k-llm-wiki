---
type: object
title: Developing a universal test method library
layer: file
stage: testmethod
tags: [testmethod, utm, universal-test-method-library, library, file, build, project, debug, testflow]
related: [testmethod, test-method-project, test-method-class, testflow, how-to-create-a-universal-test-method-class, mapping-testmethod, project-explorer-view, pin-string, spec-variable, spec-value, file-string, option-list, context-pins]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02_Developing_a_universal_test_method_library.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Developing a universal test method library

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **146 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.02.02_Developing_a_universal_test_method_library.md>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.02.02.04.03_How_to_print_static_variable_value_in_debugging.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 How to debug a universal test method › How to print static variable value in debugging）

The following figure shows the how to use the commands mentioned above.

 !`Print static variables in the debugging`（raw: `../../../../raw/121921.png`）

<!-- 语法节 end -->

## 是什么

**UTM 库（universal test method library）是「一整套 UTM 流程」的产物**；
**本篇是这一章的章首页**，它只做一件事：**把「从零到有一个能用的库」拆成四步，并说明前置条件**。
原文第一句就钉住了它的定位：

> 「This section describes the procedure of developing a universal test method library in SmarTest.」

**`section` 这个词要划出来**——**它不是一个命令、不是一个类、也不是一种文件格式**，
而是**一组步骤的总称**。frontmatter 给它 `layer: file`（**推断**：库是产物、是文件，
依据是本篇把「库」当成 `## Results` 里的结论，而不是当成交互接口；**原文没有一句说它是文件**）。

### 两条路：从零建，或从 classic 转

原文 `## About this task` 一次给了两条路：

> 「The procedure is to create a universal test method library from scratch. If you have already some
> classic test method libraries, you can convert them to universal test method libraries.」

**第二条路的说明不在本篇**：原文只给了一个链接
`How to convert a classic test method project to universal test method project`
（raw: `02.07.02.04.01_How_to_convert_a_classic_test_method_project_to_universal_test_method_pr.md`）
——**那一篇本页没读**。**所以「classic 和 universal 差在哪、转换要动什么」本页一个字没有。**

### 前置条件只有两条

> 「Make sure you are using SmarTest 6.3 or later, and the device primary setups are ready to use.」

| 条件 | 原文 |
|---|---|
| **SmarTest 6.3 或更高** | `using SmarTest 6.3 or later` |
| **device 的 primary setups 已可用** | `the device primary setups are ready to use` |

**第二条容易读错**：它要求的**不是「有一个 test method 工程」**，而是
**device 的 primary setups 已经能用**——**即：库最终要挂到某个 device 上，本篇的起点在那之后。**
**「primary setups 具体指哪些文件」本篇没展开**：`primary setup` 这个词**本篇只出现这一次**。

### 四步，一步不少

原文 `## Procedure` 是四个列表项，**每一项就是一个链接**。**逐字照抄链接名与顺序**：

| # | 步骤（原文的链接文字） | 指向的文档（raw 相对路径） |
|---|---|---|
| 1 | `Create a universal test method project` | `02.07.02.02.01_How_to_create_a_universal_test_method_project.md` |
| 2 | `Create a universal test method class for the universal test method project` | `02.07.02.02.02_How_to_create_a_universal_test_method_class.md` |
| 3 | `Create a universal-test-method-based testflow` | `02.07.02.02.03_How_to_create_and_execute_a_universal-test-method-based_testflow.md` |
| 4 | `Debug a universal test method` | `02.07.02.02.04_How_to_debug_a_universal_test_method.md` |

> **这四步的顺序，是本篇唯一的「流程信息」**：**先建工程 → 再建类 → 再建 testflow → 再调试**。
> **每一步的内容本篇一个字都没写**——`## Procedure` 里**连一个动词都没有加**，
> **每一项只是「链接 + 句号」**。**所以这一页能给你的就是这张表：有哪四步、按什么顺序、去哪一篇。**

### 产物在哪：**语料未写**

**这是本页最该交代的一件事。** 原文 `## Results` 只有一句：

> 「The universal test method libraries are error free and ready to use.」

**它说的是「什么样的库算做完了」（`error free` + `ready to use`），
不是「库文件叫什么、落在哪个目录」。** 本篇里：

| 你可能想知道的 | 本篇写了没有 |
|---|---|
| 库文件叫什么名字（`.so`？`lib*.so`？） | **没有**——**`.so` 这个串本篇 0 次** |
| 落在哪个目录 | **没有**——**本篇没有 `Debug/` 这个目录名**（`Debug` 只以第 4 步的链接名 `Debug a universal test method` 这一个形态出现一次） |
| 怎么验证它 `ready to use` | **没有**——只有上面那一句结论 |

> **⚠️ 本批任务单给本页的提示是「最终产物 `lib<工程名>.so`，落在 `Debug/`」，
> 而这两件事在本篇 raw 里都**找不到**。按本页的规矩（只写 `sources:` 里有的），
> 本页不把它们写进正文**——它们的真实出处见 `## 出处` 末尾那一笔。

### 「语法 / 参数」节里那一句 + 一张图，不来自本篇正文

本页「语法 / 参数」节顶上的说明写着：本节 146 字符，**取自本篇**及其**子主题**
`How to print static variable value in debugging`。节里的内容是**一句导语 + 一张图的引用**：

> 「The following figure shows the how to use the commands mentioned above.」

**`the commands mentioned above` 不在本节里**——**它在本页没读的那个子主题里**
（`02.07.02.02.04.03`）。**图 `raw/121921.png` 本页也没看。**
**本篇自己没有 `Syntax` / `Parameters` / `Example` 段**；「语法 / 参数」节能有那 146 字符，
是脚本从子主题抄来的（**脚本在段名里标了出处**）。

## 典型用法

**本篇给不出可执行的细节，只给顺序。** 照上表四步走：

1. **先确认前置条件**：SmarTest 6.3 或更高 + device primary setups 可用。
2. **建 UTM 工程** → `How to create a universal test method project`（**本页没读**）。
3. **建 UTM 类**。这一步 wiki 里已有两页：[[how-to-create-a-universal-test-method-class]] 与
   [[test-method-class]]——**那两页读的是另外两篇文档**，**本篇对第 2 步一个字没展开**。
4. **建基于 UTM 的 testflow** → `How to create and execute a universal-test-method-based testflow`
   （**本页没读**）。
5. **调试** → `How to debug a universal test method`（**本页没读**）。

**本章另挂了四篇工具类子主题**（只在 `Subtopics` 里，`## Procedure` 里没有它们）：
`How to use the Cppcheck tool` / `How to use valgrind with UTM` / `How to use callgrind with UTM` /
`How to develop UTM library outside of SmarTest`——**四篇本页都没读**。
**它们不在四步流程里**——**（推断）**按这个位置关系，它们是**可选工具**；
依据只是「它们在 `Subtopics` 而不在 `## Procedure`」，**原文没有一句话说它们是可选或必需**。

**下一步**：**本篇没有 `## What to do next` 段**——四步走完、库 `ready to use`，本篇就结束了。

## 和谁有关

- [[testmethod]] — **本页 `stage: testmethod` 的理由**：库里的东西是 test method，
  `## Before you begin` 里的 `device primary setups` 也在 test method 那一侧
  （**推断**，依据是本篇把库摆在 device 与 testflow 之间）。
- [[test-method-project]] — **第 1 步的产物 / 第 2 步的前提**。
  **本篇只给链接名，没给内容。**
- [[test-method-class]] / [[how-to-create-a-universal-test-method-class]] — **第 2 步的两页专页**。
  **它们读的是 `01.06.02.02` 与 `02.07.02.02.02` 两篇，不是本篇**；
  **本篇对第 2 步一个字都没有**。
- [[testflow]] — **第 3 步的产物**。**本篇对它的限定说法是
  `universal-test-method-based testflow`**——**即用 UTM 建的那种 testflow，不是普通那种**；
  **这个区别本篇没有展开**，只有链接名里的 `universal-test-method-based` 这几个字。
- [[mapping-testmethod]] — **本页在 wiki 里的位置**：那张对照表里「编译出 UTM 库」一行的
  **「文件」格写的就是本页**，同格的 GUI 侧写的是 [[project-explorer-view]] 右键 → `Build Project`。
  **那页不是本页建的，它的「`Build Project`」这一格在本篇里没有依据**
  （**本篇 0 次出现 `Build Project`**）——**本页只指路，不声称那一格出自本篇。**
- [[project-explorer-view]] — **如果库真是「右键 → Build Project」出来的，那就在它里面**
  （**依据是 [[mapping-testmethod]]，不是本篇**）。
- **参数类型那一族**（[[pin-string]] / [[spec-variable]] / [[spec-value]] / [[file-string]] /
  [[option-list]] / [[context-pins]]）——**它们是「库里的 test method 有哪些入参类型」**。
  **本篇一个字没提任何参数类型**；这条关系是照 [[mapping-testmethod]] 与
  [[how-to-create-a-universal-test-method-class]] 的行位指的（**推断**）。
- **`Subtopics` 里那八篇（均未建、本页均未读）**：`How to create a universal test method project`、
  `How to create a universal test method class`、`How to create and execute a
  universal-test-method-based testflow`、`How to debug a universal test method`、
  `How to use the Cppcheck tool`、`How to use valgrind with UTM`、`How to use callgrind with UTM`、
  `How to develop UTM library outside of SmarTest`。**本篇的全部实质内容都在它们那里。**
- **`About this task` 里点名的一篇（未建、本页未读）**：
  `How to convert a classic test method project to universal test method project`
  （raw: `02.07.02.04.01_How_to_convert_a_classic_test_method_project_to_universal_test_method_pr.md`）。

## 版本

**本文档没有 `## Functional changes` 段。** 这是事实，不是缺陷——
本篇是章首页，**一行版本记录都没有**。

**由此能说什么、不能说什么**：

- **能说**：本篇没说 UTM 库是哪一版引进的，也没说它改过。
- **不能说**：「UTM 库是 6.3 引进的」——**`## Before you begin` 那句 `SmarTest 6.3 or later`
  是「你要用 6.3 以上才走得了这套流程」，不是「库是 6.3 新增的」。**
  **两句话读起来像，含义完全不同，本页不把它们合并。**
- **旁证（wiki 内部，不在本页 `sources:` 里）**：第 2 步那两篇专页的版本段里都有
  `Introduced before SmarTest 6.3.2` 这一条——**按 §11.2 ②，那是哨兵值**，
  意思是「**在本文档集覆盖范围开始之前就已经有了**」，**不是「6.3.2 新增」**。
  **那两页不是本页建的，这里只指路。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.02.02_Developing_a_universal_test_method_library.md`
（TDC `98951.htm`，38 行 / 2,350 字节）——**整篇读完**。

**本页没做的**：

- **`Subtopics` 里那八篇一篇没读**（`.02.01` / `.02.02` / `.02.03` / `.02.04` / `.02.05` /
  `.02.06` / `.02.07` / `.02.08`）。**这是本页最大的缺口，而且是结构性的**：
  **本篇自己就是章首，四步的全部内容都推给了它们。**
- **一张图没看**（`02.07.02.02.04.03` 里的 `raw/121921.png`）。
  **本页没有任何来自图的结论**——连那张图画的是哪些命令都不知道。
- **`About this task` 链到的那一篇没读**（`02.07.02.04.01`，classic → universal 的转换）。
  **所以「classic 和 universal 的差别」本页一个字都没有。**
- **没有实编译过任何 UTM 库**（`verified: doc-only`）。
  **`error free and ready to use` 是原文的结论，不是本页验证过的。**
- **没有跑 `verify_stages.py`**（按本批分工，避免抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[testmethod]] 页。

> **⚠️ 一处「任务单与 raw 对不上」的照实交代（不是语料瑕疵，是本页的来源声明）**：
> 本批任务单给本页的提示写着「本阶段最终产物 `lib<工程名>.so`，落在 `Debug/`」。
> **本页回 raw 核过本篇全文**：**`.so` 这个串 0 命中**；
> **`Debug` 只在第 4 步的链接名 `Debug a universal test method` 里出现过一次，
> 没有作为目录名的 `Debug/`**。
> **所以这句提示不是出自本页的 source。** 它实际出自 wiki 里已有的两页：
> [[mapping-testmethod]] 的「文件」格（写 `lib<工程名>.so`，落在 `Debug/` 子目录）与
> [[how-to-create-a-universal-test-method-class]] 的 `## Results`（`Debug` 子目录 +
> 例子路径 `/home/demo/devices/act299_tml/Debug/`）。**那两处各有自己的出处。**
> **本页按规矩只写 `sources:` 里有的，所以正文里不写这两个名字**——
> **要它们的人去那两页看。**

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**：
> ① **`Subtopics` 用的是 H4（`#### Subtopics`）**，而本篇其余节标题
> （`## About this task` / `## Before you begin` / `## Procedure` / `## Results`）都是 H2
> ——**同一篇里两种标题级别**。**语料里同型文档普遍如此**，**本页照实记，不替它统一。**
> ② **`## Procedure` 的四项只有「链接 + 句号」，没有动词也没有宾语。**
> 逐字是 `-  [Create a universal test method project](<02.07.02.02.01_How_to_create_a_universal_test_method_project.md>).`
> 这种形状。**读起来像「步骤名」，其实只是把四篇文档的标题当成了列表项**——
> 第 2 项的链接文字是 `Create a universal test method class for the universal test method project`，
> **而目标文档的标题是 `How to create a universal test method class`**，
> **两者不是同一个字符串**。**本页照原样引链接名，不替它统一成目标文档的标题。**
> ③ **`## Results` 用复数**（`The universal test method libraries are error free and ready to use.`），
> 而本篇标题、`## About this task`、`## Procedure` 第 1 项用的都是单数
> （`a universal test method library`）。**同一篇里单复数并存，本页并列，不替它统一。**
> ④ **本页在本篇里没有发现坏字**（`鈥` / `渭` / `掳` 那一类）。
> **但这是「本页读到的」，不是「本篇干净」**（§13.1 第 ⑥′）。

`verified: doc-only`
