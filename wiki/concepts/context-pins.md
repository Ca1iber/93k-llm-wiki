---
type: concept
title: How to create a universal test method class
layer: L2
stage: testmethod
tags: [testmethod, parameter-type, contextpins, ccf, concurrent-test-framework, wizard]
related: [how-to-create-a-universal-test-method-class, test-method-class, option-list, file-string, pin-string, smartest-7.2.0]
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

**ContextPins 是 test method 参数的一种类型。**

**原文对它的全部说明只有一句话**——这一页后面所有内容都是对这一句的拆解：

> 「ContextPins is used to define the parameter `CCF_FocusedPins` in the concurrent test framework.」

**这句话里有三个信息，缺一个都读不准：**

| 原文片段 | 读出来的事 |
|---|---|
| `is used to define the parameter` | **它的用途是「定义出一个参数」**——不是给一个值，是把一个参数**引进来** |
| `the parameter CCF_FocusedPins` | **定义出来的那个参数有固定名字**：`CCF_FocusedPins` |
| `in the concurrent test framework` | **它只在 concurrent test framework 里有意义** |

**所以它和 `int` / `double` / `string` 不是一类东西。** 那三个是**值类型**（你填一个值），
ContextPins 是**把一个框架规定的参数钩进来**。**类型名里的 `Context` 属于 concurrent 框架的语境，
不是测试执行期的运行上下文**——这一条很重要，见下。

### 它在参数类型清单里的位置

原文列清单的那一句是：

> 「The type can be int, double, string, PinString, SpecVariable, SpecValue, ContextPins,
> OptionList or FileString.」

**一共 9 个名字，分两族：**

| 族 | 成员 | 说明 |
|---|---|---|
| **C++ 内建类型（3 个）** | `int` / `double` / `string` | 原文没有另作解释 |
| **SmarTest 自己的参数类型（6 个）** | `PinString` / `SpecVariable` / `SpecValue` / **`ContextPins`** / `OptionList` / `FileString` | 原文对其中 5 个各给了一句解释 |

**ContextPins 在这 6 个里排第 4（整张清单里排第 7）。**
**注意它是唯一一个「解释句里指向别处一篇文档」的类型**：
其余几个的解释句讲的是「这个值长什么样」，而 ContextPins 的解释句讲的是
**「它会定义出哪个参数」**，并把读者引向 `CCF_FocusedPins`（`02.07.08.04`，**本页没读**）。

### 语料明说没有的三件事（**不是本页漏了，是原文没写**）

| 想知道 | 语料怎么说 |
|---|---|
| **ContextPins 填进去的值长什么样**（几个 pin、怎么分隔、能不能填 pin group） | **语料未写**。原文对它的解释只有上面那一句，**没有像 `PinString` 那样写 `is used for pins, pin lists or pin groups`** |
| **`CCF_FocusedPins` 是不是必须叫这个名、Identifier 能不能另起** | **语料未写** |
| **它和 concurrent test method 的哪一步对接** | **语料未写**。原文只说「在 concurrent test framework 里」，**没说在哪个环节用** |

**⚠️ 本页不替它补。** 上面三格里任何一格填上内容，都是编（§11）。
**想知道 `CCF_FocusedPins` 是什么，只有去读 `02.07.08.04_Test_method_parameters.md`——
那篇本页没读**（它不在这页的 `sources:` 里）。

### 一个必须防的同名陷阱

**`ContextPins` 里的 `Context` 指的是 concurrent test framework 的语境**（原文：
`in the concurrent test framework`），**不是「测试运行时的执行上下文」**。
本 wiki 里另有一族讲「执行上下文」的页，**两者名字相近、出处不同、用途也不同**。
**本页不给出那几页的链接**（理由见「出处」），**只在这里点明别把它们当成一回事。**

## 典型用法

**本页不重复「怎么建类」的流程**——那是 [[how-to-create-a-universal-test-method-class]] 的活。
本页只说**「在哪个环节选到 ContextPins」**这一步：

1. **在 `Create a new Test Method class` 向导里，参数是在 `Parameters` 区加的**：
   点 `Add` → 弹出 **`Add a new parameter`** 窗口。
2. **在那个窗口里填 `Identifier` 与 `Type`**，**`ContextPins` 是在 `Type` 这一栏里选的**：
   > 「Identifier: The parameter name to be shown in the testflow editor.」
   > 「Type: The parameter type.」
3. **`OK` 之后参数进到类里**；**变量名会自动生成**——原文那句是：
   > 「Variable: The variable name used in the `run()` function of the test method.
   > It is automatically set as "m" plus parameter name. It can also be changed.」
4. **改完参数必须重新 build 工程**，然后 **Properties view 会变灰**，
   要点右上角的 `Inconsistency Check` 按钮把它更新过来
   （原文：`this view is grayed because the parameters displayed in this view are not consistent
   with those in the test method code`）。**这一步对所有参数类型都一样，不是 ContextPins 专属。**

**两条和 ContextPins 有关的搭配（都是从它那一句解释读出来的）**：

- **它是 concurrent test framework 的类型 → 类模板要选 concurrent 那一个。**
  向导 `Templates` 字段里的一项是 `Concurrent test method class for CTF-based test method`。
  **（推断）**：既然 ContextPins 只在 concurrent test framework 里有意义，
  **那把它加到一个 `Normal test method class` 上大概率是无意义的**——
  **但原文没有这句话，本页不把它写成规矩。**
- **原文特意劝过一句不要混项目**：
  > 「To easily manage the test methods, it is not recommended to put normal test methods
  > and concurrent test methods in one project.」

**语料未写的那一步**：**ContextPins 类型的参数加好之后，在测试方法的代码里怎么取值、怎么用**——
**原文一个字都没写**（它只讲了 `Variable` 字段的命名规则）。

## 和谁有关

- [[how-to-create-a-universal-test-method-class]] — **上位页（前提）**：
  「向导怎么走、六个字段各填什么、类名有什么硬规则、build 之后 Properties view 为什么变灰」
  **全在那一页**。**本页只讲 ContextPins 这一个类型**，不重复流程。
- [[test-method-class]] — **参数被加进去的那个类的来源**：`New > Test Method Class` 向导。
  **ContextPins 是那个向导 `Add a new parameter` 窗口里 Type 栏的一个选项。**
- [[option-list]] / [[file-string]] / [[pin-string]] — **同一篇 raw 的姊妹类型**，
  各有一页。**四页（含本页）共用同一篇 `sources:`**，
  **各页只写自己那一个类型——这是本批的硬分工，不是内容重复。**
- [[smartest-7.2.0]] — **引入版本页**：ContextPins 是 SmarTest 7.2.0 新增的两个参数类型之一。
- [[testmethod]] — **stage 归属**。frontmatter 的 `stage: testmethod` 是**「最近的一段」**，
  不是「归属」——参数类型是给 test method 那一段用的。
- `CCF_FocusedPins`（`02.07.08.04_Test_method_parameters.md`，**未读**）——
  **ContextPins 就是用来定义它的那一个参数**。**它是什么、取值是什么，本页答不了。**
- `How to implement a concurrent test method`（`02.07.02.12.01.01`，**未读**）——
  原文在讲 concurrent test method 时指向它。**本页没有它的任何内容。**

> 上面每一条都来自本页读的那一篇 raw（或它的 `sources:` 同样的那一篇）。
> **本页没有查 `edges.jsonl`，也没有从别的文档补事实。**

## 版本

本篇 `## Functional changes` **共 8 条**，**与 ContextPins 直接相关的只有一条**：

- **SmarTest 7.2.0**：`New parameter types: ContextPins, OptionList`

**读法**：**ContextPins 从 SmarTest 7.2.0 起才有**；
**它和 `OptionList` 是同一条记录里一起加的**（两个类型同批引入）。
本 wiki 面向的 **7.10.3 上在**。

**同一条记录里还有个对照**：`FileString` 是 **7.2.1** 才加的
（`SmarTest 7.2.1: New parameter type FileString`）——
**即 ContextPins 比 FileString 早一个小版本。**

**其余 7 条**（6.3.2 之前的哨兵值、6.5.0 / 6.5.2 / 7.1.3 / 7.2.0 的模板、7.2.1 FileString 等）
**与本类型无关，本页不重复列出**——**它们逐条列在
[[how-to-create-a-universal-test-method-class]] 的「版本」节里**（那一页是这条流程的主页）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md`

**本页没做的**：

- **`CCF_FocusedPins` 那一篇没读**（`02.07.08.04_Test_method_parameters.md`）——
  它是 ContextPins 那一句解释**唯一指向的目标**。
  **所以「CCF_FocusedPins 是什么、有几个、取值怎么给」，本页一个字都没有。**
- **`How to implement a concurrent test method`（`02.07.02.12.01.01`）没读**——
  **所以「concurrent test method 怎么写」本页没有**，
  本页只有「ContextPins 属于那个框架」这一句。
- **`Subtopics` 列的两篇没读**：`Working with Content Assist`、
  `Working with Test Method Panel`。**本页正文也没提它们。**
- **两张图一张没看**：`116534.png`（参数层次在 Properties view 里长什么样）、
  `118556.png`（`Inconsistency Check` 按钮）。**本页没有任何来自图的结论**——
  **本页不用「图够不着」当理由（§11.4）：是没看，不是看不到。**
- **两类东西本页刻意不写**：
  ① **「怎么建类」的完整流程**——那是
     [[how-to-create-a-universal-test-method-class]] 的内容，本页只写选类型这一步；
  ② **讲「执行上下文」的那些页的链接**——**本页不建那条互链**
     （那几页讲的是另一件事，链上去会把两个不同的东西绑在一起）。
     **这条只是「不写链接」，不是说它们不存在。**
- **`## Results` 段（库落在 `Debug/` 子目录、示例路径 `/home/demo/devices/act299_tml/Debug/`）
  本页没有展开**——那是「建完类之后产物在哪」，属于那条流程主页。

> ⚠️ **本篇的语料瑕疵，照实记录，一处都没替它改**：
> ① **同一件事两种缩写**：讲 concurrent test method 时，原文**同时用了 `CTF` 和 `CCF`**——
>    `Concurrent test method class for **CTF**-based test method`、
>    `If one **ccf_tml** is already imported in the project`、
>    `**CCF**_FocusedPins`、`the imported **ccf_tml**`。
>    **两个缩写指的是不是同一个东西、谁是谁的正式写法，原文没说，本页不判。**
>    本页引 ContextPins 那一句时用的是原文的 `concurrent test framework`（全称），不是缩写。
> ② **拼写**：`In **Templates filed**, select:` —— **`filed` 应为 `field`**
>    （同一段里 `In the Class Name **field**` 拼对了）。
> ③ **`Note` 与上一句之间没有空格、也没有换行**，直接黏在一起，例如：
>    `A string set as the parameter comment.Note Parameter hierarchies are supported.`
>    和 `The Create a new Test Method class wizard will pop up.Note You can separate the header file and source file`。
>    **这是全文性的排版问题，不是某一处笔误。**
> ④ **清单末项的连接词不齐**：类型清单写成
>    `int, double, string, PinString, SpecVariable, SpecValue, ContextPins, OptionList or FileString.` ——
>    **前面全是逗号，最后一项才用 `or`**。**原文如此。**
> ⑤ **`Before you begin` 与 `Functional changes` 之间有一处小张力**：
>    前者要求 `Make sure you are using SmarTest 6.3 or later`，
>    后者有一条 `Introduced before SmarTest 6.3.2`。
>    **两者不必然矛盾**（`6.3` 与 `6.3.2` 是不同的版本号），
>    **但原文没有解释这个差别，本页也不替它调和。**

`verified: doc-only`
