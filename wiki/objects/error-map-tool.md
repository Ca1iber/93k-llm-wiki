---
type: object
title: Error Map Tool
layer: gui
stage: results
tags: [error-map, results, functional-test, evaluation, gui]
related: [error-map, hidden-upload, result-configuration, results, integrated-result-tool]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Error Map Tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Error Map Tool 是一个「评估错误」的应用。** 主文档正文只有三句，全部机制就在里面：

> 「The Error Map Tool is **an application for the evaluation of errors**. It is **the major tool
> for low level examination of the test results** you obtain **when performing functional tests**.
> It **uses the Error Map to generate its output**.」

拆成三个可核对的事实：

| 原文 | 中文 | 边界 |
|---|---|---|
| `an application for the evaluation of errors` | 评估**错误**的应用 | **它的对象是 error**，不是笼统的「结果」 |
| `the major tool for low level examination of the test results … when performing functional tests` | 功能测试结果的**底层检查**主力工具 | **两个限定**：用途限于 `low level examination`，数据来源限于 `functional tests` |
| `It uses the Error Map to generate its output` | **靠 Error Map 产出输出** | **Error Map 是它画出来的东西，不是它的别名** |

**第三句是本页最要紧的一句。** 它把 `Tool` 和 `Map` 明确分成两样东西：
**Tool 是程序，Map 是程序产出的载体**。原文用的是 `uses … to generate`，**不是 `is`**。
子主题目录里这两个名字也各占一条（`Error Map` 和 `Using the Error Map Tool`），**印证了这个分法**（推断，依据是这两条子主题各自独立成篇）。

**两个限定词的份量**：

- **`low level examination`（底层检查）** —— 原文说它是干这个的 `major tool`。
  **「底层」是相对什么而言的，主文档没说**（推断：相对分析视图那类汇总展示而言，但本页没有依据，不写死）。
- **`when performing functional tests`（做功能测试时）** ——
  **这把适用范围收窄了**：原文说的是功能测试得到的结果，**没有说它对所有测试类型都适用**。

### 本页能拿到的全部结构：一张六条目录

主文档除了上面三句，剩下的就是 `## Subtopics` 那张目录。**六条子主题本身就是本工具的功能划分**：

| 子主题 | 从标题能读出的（**推断**——只读了标题，一篇没读） |
|---|---|
| `Error Map` | 工具产出物本身是什么 |
| `Using the Error Map Tool` | 怎么用 |
| `Elements of the Error Map Tool` | 界面由哪些元素构成 |
| `Result Configuration` | 结果的配置 |
| `Hidden Error Map Upload` | 一个「隐藏的」上传动作 |
| `Print Error Map Data` | 把 error map 数据打印出来 |

> **上表整列都是推断**，依据**只有标题的措辞**。**这六篇本页一篇都没读**，所以
> **每一格讲的具体是什么，本页一个字都不能担保。**

### 一条读目录的提醒

六个子主题的排列顺序（是什么 → 怎么用 → 界面 → 四项具体功能）**看起来像操作顺序，其实不是**：
它是**文档的阅读顺序**。原文没有 `## Procedure` 一节，**没有任何一句话讲先做哪步后做哪步**。
**把目录顺序当操作步骤是本页最容易犯的错。**

## 典型用法

**语料未写。** 主文档没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`，
正文只有「是什么」一节引的那三句。**这个工具怎么打开、怎么用、用了之后会看到什么，
主文档一个字都没说**——按标题判断，使用步骤在未读的子主题 `Using the Error Map Tool` 里（推断）。

**本页能给出的唯一「顺序」**是阅读顺序，不是操作顺序：

`Error Map`（先弄清产出物）→ `Using the Error Map Tool`（再看怎么用）→
`Elements of the Error Map Tool`（再看界面）→ 后三条按需查。

**这不是原文推荐的操作流程**——原文没有推荐过任何流程，**这只是目录的排列**（推断）。

## 和谁有关

- [[error-map]] — **上游，不是同义词。** 原文 `It uses the Error Map to generate its output`：
  **Map 是 Tool 的输出载体**；子主题里 `<02.08.04.08.01_Error_Map.md>` 单独成篇。
- [[hidden-upload]] — 子主题 `Hidden Error Map Upload` 对应的页。
  **`Hidden`（隐藏）指什么、为什么要隐藏上传，主文档没写**——本页只知道有这么一条。
- [[result-configuration]] — 子主题 `Result Configuration` 对应的页。
  **它配的是「结果」还是「error map 的结果」，本页分不出来**（推断：标题写的是 `Result`，不是 `Error Map Result`）。
- [[results]] — 本页 `stage: results` 的理由：它检查的对象是 `test results`。
- [[integrated-result-tool]] — 同批建的 `gui` + `results` 页；**原文没说两者关系**（推断：都在结果查看这条线上，但本页不写死）。
- `Using the Error Map Tool` / `Elements of the Error Map Tool` / `Print Error Map Data`（**均未建、未读**）—
  三个未读子主题：前两个是用法与界面，最后一个是打印。**本页和它们没有任何内容往来。**
- `functional test`（**未建**）— 原文用它划定本工具的适用范围；**本页没有它的任何定义**。

## 版本

`## Functional changes` 段有，只有一条：

> 「**Introduced before SmarTest 6.3.2**」

**这条给的是上界，不是引入版本。** 原文用的是 `before`：
它说的是「SmarTest 6.3.2 之前这个东西就已经存在」，
**没有说它是哪个版本引入的**。**所以更早的版本（6.5.0 / 7.0.0 等）里有没有它，语料未写。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.md`

**这就是本页的全部依据。整篇 17 行，去掉 frontmatter 和子主题目录，正文只有三句 + 一行版本记录。**

**本页没做的**：

- **六个子主题一篇都没读。** 它们是
  `<02.08.04.08.01_Error_Map.md>`、`<02.08.04.08.02_Using_the_Error_Map_Tool.md>`、
  `<02.08.04.08.03_Elements_of_the_Error_Map_Tool.md>`、`<02.08.04.08.04_Result_Configuration.md>`、
  `<02.08.04.08.05_Hidden_Error_Map_Upload.md>`、`<02.08.04.08.06_Print_Error_Map_Data.md>`。
  **结果是：这个工具的实际内容本页一点都没有**——
  它长什么样、怎么点、error map 画成什么形状、上传是传到哪、打印出什么，**全部不在本页**。
  本页只有**主文档自己的三句话**加**一张从标题推出来的表**。
- **一张图没看**：主文档正文没有内嵌图片，**本页没有任何来自图的结论**。
- **`Error Map` 本身是什么没读**（它是子主题之一）。所以
  **「error」在这里指哪种错误、error map 的坐标轴是什么，本页不知道**——
  上一节那张表里 `Error Map` 那一行的推断，**依据只有标题三个字**。
- **没有 `## Syntax` / `## Parameters` / `## Example` 这类段标记**，跟着 `Subtopics` 往下找一层也没有——
  **所以本页「语法 / 参数」节是脚本判定「不收录」的结论，不是本页的省略**（§4）。
- **没有查 `functional test` 的定义**，**也没有查它和 `Error Map Tool` 在别处还有没有别的说法**。

> ⚠️ **语料瑕疵，照实记下、一处没替它改**：
> **`## Functional changes` 的唯一一条用的是 `before`**：
> `Introduced before SmarTest 6.3.2`。
> **这是一句不可引用为「引入版本」的话**——它只给上界，**不给版本号**。
> 本页在 `## 版本` 一节里把这一点明写出来了，**没有把它转述成「SmarTest 6.3.2 引入」**。
>
> 除这一处外，**本篇没有发现错别字、大小写不一致或链接指向错误**；
> 六条子主题的相对链接（`<02.08.04.08.0N_*.md>`）**与条目名一一对应，未发现指错**。

`verified: doc-only`

