---
type: object
title: How to create a universal test method class
layer: L2
stage: testmethod
tags: [testmethod, parameter-type, filestring, file-name, wizard, smartest-7.2.1]
related: [how-to-create-a-universal-test-method-class, test-method-class, pin-string, option-list, context-pins, smartest-7.2.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# How to create a universal test method class

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**FileString 是 test method 参数的一种类型。**

**原文对它的全部说明只有一句话**：

> 「FileString is used to enter file names as the value of a test method parameter.」

**这句话能读出的三件事：**

| 原文片段 | 读出来的事 |
|---|---|
| `is used to enter file names as the value` | **它是值类型**——你在这个参数里**填一个值**（不是像 `ContextPins` 那样去定义一个别的参数） |
| `file names` | **填的值是文件名**（**注意原文用的是复数 `names`**，见下） |
| `of a test method parameter` | 它的**归属**：test method 的参数 |

**一句话记法：`FileString` = 「这个参数的值是一个文件名」。**

> **⚠️ 那个复数 `names` 值得单独说一句。** 原文写的是 `file names`（复数），
> **不是 `a file name`**。**这可能意味着一个参数能填多个文件名，也可能只是英文的一般性表达。**
> **原文没有给例子、也没有说分隔符是什么**——
> **所以本页不把这个复数解释成「支持多个文件」（推断，且依据不足）。**
> **取值到底几个、怎么分隔：语料未写。**

### 它是这族里最后加进来的一个

原文列类型的那一句是：

> 「The type can be int, double, string, PinString, SpecVariable, SpecValue, ContextPins,
> OptionList or FileString.」

**两个「最后」都在它身上：**

- **在清单里它是最后一项**——**原文在它前面用的是 `or`**，前面各项之间都是逗号
  （`int, double, string, PinString, SpecVariable, SpecValue, ContextPins, OptionList or FileString.`）。
- **在版本上它是最后一个引入的**——见「版本」节：**SmarTest 7.2.1**，
  比 `ContextPins` / `OptionList`（7.2.0）还晚一个小版本。

**这两件事合起来说明：FileString 是向导 `Type` 下拉里的后来者。**
（**推断**；依据是版本条目与清单位置一致，**但原文没有这么说**。）

### 一条时限上的坑（**本页最有用的一条**）

原文 `## Before you begin` 写的门槛是：

> 「Make sure you are using SmarTest 6.3 or later, and a test method project has been created.」

**而 FileString 是 SmarTest 7.2.1 才加的。**
**所以：在一台 6.3 ~ 7.2.0 的机器上，门槛那句话成立，但 `Type` 栏里不会出现 FileString。**
**读「Before you begin」那一句不足以判断这个类型在不在**——**要看版本页**。
（**推断**；两条依据都是原文：`Before you begin` 的 `6.3 or later`，
与 `Functional changes` 的 `SmarTest 7.2.1: New parameter type FileString`。）

### 语料明说没有的四件事（**不是本页漏了，是原文没写**）

| 想知道 | 语料怎么说 |
|---|---|
| **填的文件名是什么形态**（绝对路径 / 相对路径 / 相对谁） | **语料未写**。原文只有 `file names` 两个词 |
| **能不能填多个**、分隔符是什么 | **语料未写**（见上面那个复数的讨论） |
| **文件不存在 / 路径不合法会怎样** | **语料未写**。本篇没有 `## Errors` 段 |
| **这个文件名在 test method 里怎么被打开/用掉** | **语料未写**。原文只说「作为参数的值输入」 |

**⚠️ 上面四格本页不替它补。** 想答这几问，唯一的去处是
`FileString` 自己那一篇（`02.07.02.13.01`）——**那篇本页没读**。

## 典型用法

**本页不重复「怎么建类」的流程**——那是 [[how-to-create-a-universal-test-method-class]] 的活。
本页只说**「FileString 在哪里被选到、被谁填」**：

1. **在 `Create a new Test Method class` 向导的参数区点 `Add`**，
   弹出 **`Add a new parameter`** 窗口。
2. **在这个窗口的 `Type` 栏选 `FileString`**，`Identifier` 栏填参数名：
   > 「Identifier: The parameter name to be shown in the testflow editor.」
   > 「Type: The parameter type.」
3. **`OK` 之后参数进类**；**变量名自动生成**——原文：
   > 「Variable: The variable name used in the `run()` function of the test method.
   > It is automatically set as "m" plus parameter name. It can also be changed.」
4. **填值的地方不在向导里，在 test suite / testflow 那一侧**——
   原文对 `Default` 字段写的是 `(Optional) The default value of the parameter.`，
   **即默认值可以在参数上加**；**真正改值是在 testflow editor 里**
   （`Identifier` 那一栏的说明就是 `The parameter name to be shown in the testflow editor.`）。
5. **改完参数要重新 build 工程**；build 完 **Properties view 会变灰**，
   点右上角 `Inconsistency Check` 按钮更新它
   （原文：`this view is grayed because the parameters displayed in this view are not consistent
   with those in the test method code`）。

**语料未写的那一步**：**FileString 参数在代码里怎么取到那个文件名、怎么用**——
**原文一个字都没写**（它只讲了 `Variable` 字段的命名规则）。

**一条搭配上的提醒**：原文 `Options` 字段写的是
`(Optional) The value candidates of the parameter. The separator between the candidates is a colon (:).`
—— **那是「给候选值」的机制，不是文件选择器**。
**原文没有说 FileString 有没有配一个文件浏览按钮。**（**这一点原文未写，本页不猜。**）

## 和谁有关

- [[how-to-create-a-universal-test-method-class]] — **上位页（前提）**：
  向导怎么走、六个字段各填什么、build 之后 Properties view 为什么变灰，全在那一页。
  **本页只讲 FileString 这一个类型。**
- [[test-method-class]] — **参数被加进去的那个类的来源**：
  `New > Test Method Class` 向导。**FileString 是那个向导 `Type` 栏的一个选项。**
- [[pin-string]] / [[option-list]] / [[context-pins]] — **同一篇 raw 的姊妹类型**，
  各有一页。**四页（含本页）共用同一篇 `sources:`**，
  **各页只写自己那一个类型——这是本批的硬分工，不是内容重复。**
- [[smartest-7.2.1]] — **引入版本页**：FileString 是这一版新增的参数类型
  （也是本 wiki 里 [[smartest-7.2.0]] 的下一站）。
- [[testmethod]] — **stage 归属**。frontmatter 的 `stage: testmethod` 是**「最近的一段」**，
  不是「归属」——参数类型是给 test method 那一段用的。
- `FileString`（`02.07.02.13.01_FileString.md`，**未读**）——
  **这一篇是 FileString 自己的专页**，原文在两处（类型清单、解释句）都链到它。
  **它的取值形态、约束、报错，全在该篇；本页一句都没有。**

> 上面每一条都来自本页读的那一篇 raw。**本页没有查 `edges.jsonl`，也没有从别的文档补事实。**

## 版本

本篇 `## Functional changes` **共 8 条**，**与 FileString 直接相关的只有一条**：

- **SmarTest 7.2.1**：`New parameter type FileString`

**三条读法**：

1. **FileString 从 SmarTest 7.2.1 起才有**；本 wiki 面向的 **7.10.3 上在**。
2. **它是这批参数类型里最后一个加的**——`PinString` / `SpecVariable` 是 6.5.0，
   `SpecValue` 是 6.5.2，`ContextPins` / `OptionList` 是 7.2.0，**FileString 是 7.2.1**。
3. **对照 `Before you begin` 的 `SmarTest 6.3 or later`**——**那一句门槛管不住这个类型**
   （见「是什么」里那条时限上的坑）。

**其余 7 条与本类型无关，本页不重复列出**——**它们逐条列在
[[how-to-create-a-universal-test-method-class]] 的「版本」节里**（那一页是这条流程的主页）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md`

**本页没做的**：

- **`FileString` 自己的专页没读**（`02.07.02.13.01_FileString.md`）——
  **这是本页最大的空缺**：原文在两处都链到它，而本页只有原文那一句解释。
  **所以「填什么形态的路径、能不能填多个、文件不存在会怎样、代码里怎么用」，
  本页一个字都没有。**
- **`Subtopics` 列的两篇没读**：`Working with Content Assist`、
  `Working with Test Method Panel`。**本页正文也没提它们。**
- **两张图一张没看**：`116534.png`（参数层次在 Properties view 里长什么样）、
  `118556.png`（`Inconsistency Check` 按钮）。**本页没有任何来自图的结论**——
  **本页不用「图够不着」当理由（§11.4）：是没看，不是看不到。**
- **「怎么建类」的完整流程本页刻意不写**——那是
  [[how-to-create-a-universal-test-method-class]] 的内容，本页只写选类型这一步。
- **`## Results` 段（库落在 `Debug/` 子目录）本页没有展开**——那属于那条流程主页。
- **本页没有查任何别的 `FileString` 用法**（例如命令参考、测试方法参考里有没有同名概念）——
  **所以若语料别处还有叫 FileString 的东西，本页不知道。**

> ⚠️ **本篇的语料瑕疵，照实记录，一处都没替它改**：
> ① **清单末项的连接词不齐**：类型清单写成
>    `int, double, string, PinString, SpecVariable, SpecValue, ContextPins, OptionList or FileString.` ——
>    **前面各项之间全是逗号，只有最后一项用 `or`**。**原文如此。**
> ② **拼写**：原文写的是 `In Templates filed, select:` —— **`filed` 应为 `field`**
>    （同一段里 `In the Class Name field` 拼对了）。
> ③ **`Note` 与上一句之间没有空格、也没有换行**，直接黏在一起，例如：
>    `A string set as the parameter comment.Note Parameter hierarchies are supported.`
>    和 `The Create a new Test Method class wizard will pop up.Note You can separate the header file and source file`。
>    **这是全文性的排版问题，不是某一处笔误。**
> ④ **同一件事两种缩写**：讲 concurrent test method 时原文**同时用了 `CTF` 和 `CCF`**
>    （`CTF-based test method` / `ccf_tml` / `CCF_FocusedPins`）。
>    **与本页的 FileString 无关，但同在一篇里，记在这里备查。**
> ⑤ **`Before you begin` 与 `Functional changes` 之间有一处小张力**：
>    前者写 `Make sure you are using SmarTest 6.3 or later`，
>    后者有 `Introduced before SmarTest 6.3.2` 一条。
>    **两者不必然矛盾，但原文没有解释这个差别，本页也不替它调和**——
>    这一条对 FileString 尤其要紧（见「版本」节第 3 条读法）。

`verified: doc-only`
