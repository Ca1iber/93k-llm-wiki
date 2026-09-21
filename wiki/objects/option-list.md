---
type: object
title: How to create a universal test method class
layer: L2
stage: testmethod
tags: [testmethod, parameter-type, optionlist, options, wizard, smartest-7.2.0]
related: [how-to-create-a-universal-test-method-class, test-method-class, pin-string, file-string, context-pins, smartest-7.2.0]
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

**OptionList 是 test method 参数的一种类型。**

**原文对它的全部说明只有一句话**：

> 「OptionList provides the possibility to enter multiple options as the value of a parameter
> in this type.」

**这句话能读出的两件事：**

| 原文片段 | 读出来的事 |
|---|---|
| `provides the possibility to enter **multiple** options` | **它和「选项」有关，而且原文用的是复数 `multiple options`** |
| `as the value of a parameter in this type` | **它的着力点是「这个参数的值」**——是这个类型本身的特性，不是外部给的 |

**一句话记法：`OptionList` = 「这个参数的值由一组选项构成」。**

> ⚠️ **那半句 `enter multiple options as the value` 是含糊的，本页不替它定死。**
> **它至少有两种读法：**
> **① 一个参数同时取多个选项（多选）；② 从一个选项清单里挑一个（单选但候选固定）。**
> **原文既没给例子、也没给分隔符、也没说能不能多选**——
> **所以本页不选任何一种读法。取值到底怎么给：语料未写。**

### 它和 `Options` 字段是什么关系（**这是本页最要紧的一处**）

原文讲参数要填的六个字段时，有一条叫 **`Options`**：

> 「Options: (Optional) The value candidates of the parameter. The separator between the
> candidates is a colon (:). These values are displayed when you try to change the parameter
> value in the test suite view.」

**两件事必须分开说，否则容易当成一件事：**

| | 它是什么 | 原文哪一句写的 |
|---|---|---|
| **`OptionList`** | **一个「参数类型」**，在 `Type` 栏里选 | `OptionList provides the possibility to enter multiple options as the value of a parameter in this type.` |
| **`Options`** | **一个「参数字段」**，`Add a new parameter` 窗口里的一栏，**对所有类型都在**（原文标了 `(Optional)`） | `The value candidates of the parameter. The separator between the candidates is a colon (:).` |

**（推断）**：**这两个名字指的是同一件事的两面——`OptionList` 是「值的形态」，
`Options` 是「候选值从哪来」。** 依据有两条：
① 两个词的语义完全重合（`option` / `options`），且原文都用「参数的值」来描述它们；
② `Options` 字段的说明句里给了**分隔符**和**显示时机**（`displayed when you try to change
the parameter value in the test suite view`），这两件事正好是「选项清单」这种值形态才需要的。
—— **但原文没有任何一句把两者连起来，所以这只是一条推断，不是文档事实。**

**⚠️ 因此本页不写「OptionList 必须配 `Options` 字段」这类规矩。**
**原文没这么写。**

### 它在清单里的位置与引入时间

原文列类型的那一句是：

> 「The type can be int, double, string, PinString, SpecVariable, SpecValue, ContextPins,
> OptionList or FileString.」

**OptionList 排第 8（9 个名字里的倒数第二）。**
**引入时间是 SmarTest 7.2.0**，**和 `ContextPins` 是同一条版本记录里一起加的**
（原文：`SmarTest 7.2.0: New parameter types: ContextPins, OptionList`）。
**比 `FileString`（7.2.1）早一个小版本。**

### 语料明说没有的三件事（**不是本页漏了，是原文没写**）

| 想知道 | 语料怎么说 |
|---|---|
| **能不能多选**、多选时怎么分隔 | **语料未写**（原文的 `multiple options` 措辞含糊，见上） |
| **`Options` 字段不填时这个类型怎么表现** | **语料未写** |
| **代码里读到的是字符串还是数组** | **语料未写**。原文只讲 `Variable` 字段的命名规则，没讲类型映射 |

**⚠️ 上面三格本页不替它补。** 想答这几问，唯一的去处是
`OptionList` 自己那一篇（`02.07.02.13.02`）——**那篇本页没读**。

## 典型用法

**本页不重复「怎么建类」的流程**——那是 [[how-to-create-a-universal-test-method-class]] 的活。
本页只说**「OptionList 在哪里被选到、值从哪来」**：

1. **在 `Create a new Test Method class` 向导的参数区点 `Add`**，
   弹出 **`Add a new parameter`** 窗口。
2. **在这个窗口的 `Type` 栏选 `OptionList`**，`Identifier` 栏填参数名：
   > 「Identifier: The parameter name to be shown in the testflow editor.」
   > 「Type: The parameter type.」
3. **在 `Options` 栏填候选值**（可选栏）——
   > 「Options: (Optional) The value candidates of the parameter. The separator between the
   > candidates is a colon (:). These values are displayed when you try to change the
   > parameter value in the test suite view.」

   **即：多个候选值之间用冒号 `:` 分隔**（**注意不是逗号**）。
   **这是本篇唯一一处给了具体分隔符的地方。**
4. **`OK` 之后参数进类**；**变量名自动生成**——原文：
   > 「Variable: The variable name used in the `run()` function of the test method.
   > It is automatically set as "m" plus parameter name. It can also be changed.」
5. **改值是在 test suite view 里**（`Options` 那一句说的 `displayed when you try to change
   the parameter value in the test suite view`）。
6. **改完参数要重新 build 工程**；build 完 **Properties view 会变灰**，
   点右上角 `Inconsistency Check` 按钮更新它
   （原文：`this view is grayed because the parameters displayed in this view are not consistent
   with those in the test method code`）。

**⚠️ 第 3 步要留个心眼**：**原文没有说 `Options` 栏是 OptionList 专属的**——
它的说明写在「六个字段」那一节里，**对所有类型都在**。
**所以「OptionList 一定要配 `Options`」这句话本页不写**（原文没说），
**只能给上面那条推断。**

**语料未写的那一步**：**OptionList 参数在代码里怎么取值**——
**原文一个字都没写**（它只讲了 `Variable` 字段的命名规则）。

## 和谁有关

- [[how-to-create-a-universal-test-method-class]] — **上位页（前提）**：
  向导怎么走、六个字段各填什么、build 之后 Properties view 为什么变灰，全在那一页。
  **本页只讲 OptionList 这一个类型。**
- [[test-method-class]] — **参数被加进去的那个类的来源**：
  `New > Test Method Class` 向导。**OptionList 是那个向导 `Type` 栏的一个选项。**
- [[pin-string]] / [[file-string]] / [[context-pins]] — **同一篇 raw 的姊妹类型**，各有一页。
  **四页（含本页）共用同一篇 `sources:`**，
  **各页只写自己那一个类型——这是本批的硬分工，不是内容重复。**
- [[smartest-7.2.0]] — **引入版本页**：OptionList 是这一版新增的两个参数类型之一
  （另一个是 [[context-pins]]）。
- [[testmethod]] — **stage 归属**。frontmatter 的 `stage: testmethod` 是**「最近的一段」**，
  不是「归属」——参数类型是给 test method 那一段用的。
- `OptionList`（`02.07.02.13.02_OptionList.md`，**未读**）——
  **这一篇是 OptionList 自己的专页**，原文在类型清单和解释句两处都链到它。
  **它的取值形态、能不能多选、约束，全在该篇；本页一句都没有。**

> 上面每一条都来自本页读的那一篇 raw。**本页没有查 `edges.jsonl`，也没有从别的文档补事实。**

## 版本

本篇 `## Functional changes` **共 8 条**，**与 OptionList 直接相关的只有一条**：

- **SmarTest 7.2.0**：`New parameter types: ContextPins, OptionList`

**三条读法**：

1. **OptionList 从 SmarTest 7.2.0 起才有**；本 wiki 面向的 **7.10.3 上在**。
2. **它和 `ContextPins` 是同一条记录里一起加的**——**两个类型同批引入**。
3. **`FileString` 比它晚一个小版本**（`SmarTest 7.2.1: New parameter type FileString`）——
   所以 7.2.0 那一版的 `Type` 栏里**有 OptionList、没有 FileString**。

**其余 7 条与本类型无关，本页不重复列出**——**它们逐条列在
[[how-to-create-a-universal-test-method-class]] 的「版本」节里**（那一页是这条流程的主页）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md`

**本页没做的**：

- **`OptionList` 自己的专页没读**（`02.07.02.13.02_OptionList.md`）——
  **这是本页最大的空缺**：原文在解释句和类型清单两处都链到它。
  **所以「能不能多选、代码里读到什么类型、有没有硬约束」，本页一个字都没有。**
- **`Subtopics` 列的两篇没读**：`Working with Content Assist`、
  `Working with Test Method Panel`。**本页正文也没提它们。**
- **两张图一张没看**：`116534.png`（参数层次在 Properties view 里长什么样）、
  `118556.png`（`Inconsistency Check` 按钮）。**本页没有任何来自图的结论**——
  **本页不用「图够不着」当理由（§11.4）：是没看，不是看不到。**
- **「怎么建类」的完整流程本页刻意不写**——那是
  [[how-to-create-a-universal-test-method-class]] 的内容，本页只写选类型这一步。
- **原文链出去的两篇 GUI 页没读**：`Limits tab`（`02.08.04.32.03.01.03_Tests_page.md`）、
  `Properties View`（`02.08.04.32.03.04_Testflow_Properties_view.md`）。
  **理由**：它们在原文里是**给 `Limits` 那一栏做指向的**，**与 OptionList 无关**，
  所以本页不引也不写。
- **`## Results` 段（库落在 `Debug/` 子目录）本页没有展开**——那属于那条流程主页。
- **本页没有查任何别的 `OptionList` 用法**（例如命令参考里有没有同名概念）——
  **所以若语料别处还有叫 OptionList 的东西，本页不知道。**

> ⚠️ **本篇的语料瑕疵，照实记录，一处都没替它改**：
> ① **拼写**：原文写的是 `In Templates filed, select:` —— **`filed` 应为 `field`**
>    （同一段里 `In the Class Name field` 拼对了）。
> ② **`Note` 与上一句之间没有空格、也没有换行**，直接黏在一起，例如：
>    `A string set as the parameter comment.Note Parameter hierarchies are supported.`
>    和 `The Create a new Test Method class wizard will pop up.Note You can separate the header file and source file`。
>    **这是全文性的排版问题，不是某一处笔误。**
> ③ **清单末项的连接词不齐**：类型清单写成
>    `int, double, string, PinString, SpecVariable, SpecValue, ContextPins, OptionList or FileString.` ——
>    **前面各项之间全是逗号，只有最后一项用 `or`**。**原文如此。**
> ④ **`Options` 那一句里的冒号写成「词 + 括号里的符号」**：
>    `The separator between the candidates is a colon (:).` ——
>    **先说 `a colon`、再用 `(:)` 把符号本身重复一遍**。
>    **本篇里 `(:)` 只出现这一次**（全篇 grep 只有这一处），
>    `SpecValue` 那句用的是另一种写法（`has the format "value[unit]"`）。
>    **原文如此，本页引时原样保留。**
> ⑤ **同一件事两种缩写**：讲 concurrent test method 时原文**同时用了 `CTF` 和 `CCF`**
>    （`CTF-based test method` / `ccf_tml` / `CCF_FocusedPins`）。
>    **与本页的 OptionList 无关，但同在一篇里，记在这里备查。**

`verified: doc-only`
