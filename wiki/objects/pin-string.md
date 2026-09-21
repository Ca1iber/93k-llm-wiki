---
type: object
title: How to create a universal test method class
layer: L2
stage: testmethod
tags: [testmethod, parameter-type, pinstring, pin-list, pin-group, wizard, smartest-6.5.0]
related: [how-to-create-a-universal-test-method-class, test-method-class, file-string, option-list, context-pins, spec-value, spec-variable, pin, pin-group-editor, pin-utility, universal-test-method-library, testflow, test-method-project, testmethod, smartest-6.5.0, smartest-6.5.2, smartest-7.2.0, smartest-7.2.1]
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

**`PinString` 是 test method 参数的一种类型。**

**原文对它的全部说明只有一句话**：

> 「PinString is used for pins, pin lists or pin groups.」

**这句话能读出的三件事：**

| 原文片段 | 读出来的事 |
|---|---|
| `is used for` | **它「用于」什么**——注意句式：不是 `is used to enter … as the value`（[[file-string]] 那种「值类型」），也不是 `is used to define …`（`ContextPins` 那种） |
| `pins, pin lists or pin groups` | **它的对象是三种粒度的针集合**：单针 / 针的列表 / pin group |
| （没有别的了） | **填进去的是什么形态、分隔符是什么、能不能混写——这一句一个都没说** |

**一句话记法：`PinString` = 「这个参数的值是一撮针」，而「一撮」有三个粒度。**

**三种粒度值得单独标出来**，因为它是这句唯一的实质：

| # | 原文 | 粒度 |
|---|---|---|
| 1 | `pins` | **单针** |
| 2 | `pin lists` | **针的列表**（复数 `lists`，**所以列表也可能不止一个**——⚠️ 见下） |
| 3 | `pin groups` | **pin group**（**复数**） |

**⚠️ 三个都是复数形式，而第一个是「pins」**——**原文没有给任何一个例子、没有给分隔符、
没有说三种能不能混在一个值里。**（**这一段本页不替它补，见「语料明说没有的四件事」。**）

### 它在这张类型清单里的位置

原文列类型的那一句是：

> 「The type can be int, double, string, PinString, SpecVariable, SpecValue, ContextPins,
> OptionList or FileString.」

**九个类型，`PinString` 排第四**：

| 位置 | 类型 | 是不是 C++ 原生 |
|---|---|---|
| 1–3 | `int` / `double` / `string` | **是**（三个语言原生类型） |
| **4** | **`PinString`** | **不是**——**它是第一个 SmarTest 自己的类型** |
| 5–9 | `SpecVariable` / `SpecValue` / `ContextPins` / `OptionList` / `FileString` | 都不是 |

**（推断）所以 `PinString` 是「专用类型」这一段的头一个**——
**依据只是清单里它紧跟在三个原生类型之后、且前面三项都是小写的语言关键字；
原文没有把清单分组，也没有给这个分法命名。**

⚠️ **同一张清单里大小写不齐**：`int` / `double` / `string` 全小写，
`PinString` / `SpecVariable` / … / `FileString` 全驼峰。**原文如此，本页照抄。**

### ⚠️ 先划一条界线：本页讲的是参数类型，不是命令

**本页的 slug 是 `pin-string`，而它是「test method 参数类型」的页。**
**本篇 raw 里没有任何一条命令**——本页逐字查过：

| 查什么 | 本篇次数 |
|---|---|
| `PinString` | **3** |
| `pin string`（小写、带空格） | **0** |
| `PADS` | **0** |

**所以：在这篇文档里，唯一存在的形态是驼峰写法 `PinString`，它从头到尾没有被当成命令，
也没有被拆成两个词写过。** 本页 `## 出处` 里说明了本页没有读哪些篇；
**若按词面（`pin string`）去别处找，指到的东西与 `PinString` 是不是同一个，
本页没有依据判断**——**本篇一个字都没有把它和任何命令联系起来。**

### 它是这族里最早的一批（两个同时）

`## Functional changes` 里与本类型直接相关的**只有一条**，逐字：

- **SmarTest 6.5.0**：`New parameter types: PinString, SpecVariable`

**两个类型是在同一条里一起加的**（`PinString, SpecVariable`）。
**所以 `PinString` 是这九个类型里最早的一批之一。**

**这决定了本页与其他五页的关系**：[[file-string]] / [[option-list]] / [[context-pins]] /
[[spec-value]] / [[spec-variable]] 五页与本页**共用同一篇 `sources:`**，
**但它们的引入版本不一样**（见「版本」）。

### 语料明说没有的四件事（**不是本页漏了，是原文没写**）

| 想知道 | 语料怎么说 |
|---|---|
| **值的形态**：是 `A,B,C` 这样逗号分隔的一大串？还是一个名字？ | **语料未写**。原文只有 `pins, pin lists or pin groups` 三个词 |
| **三种粒度能不能混写**（例如 `A,B` + 一个 group 名，甚至组名里含 `.` 或表达式） | **语料未写** |
| **填了不存在的针 / 名字写错会怎样** | **语料未写**。本篇没有 `## Errors` 段 |
| **这个值在 `run()` 里怎么被用掉**（怎么取到针的清单） | **语料未写**。原文只讲了 `Variable` 字段的命名规则 |

**⚠️ 上面四格本页不替它补。** **而且这几问在本篇里连一个出口都没有**——
**本篇 raw 里 `PinString` 从头到尾没有被做成链接**（本页逐字查过：`PinString]` 出现 **0** 次），
而 `SpecVariable` / `SpecValue` / `OptionList` / `FileString` 四个都带链接。
**所以「它自己的那一篇在哪」，本篇 raw 没说**（**本页在语料目录里找过，结果见 `## 出处`**）。

## 典型用法

**本页不重复「怎么建类」的流程**——那是 [[how-to-create-a-universal-test-method-class]] 的活。
本页只说 **`PinString` 在哪里被选到、被谁填**：

1. **在 `Create a new Test Method class` 向导的参数区点 `Add`**，
   弹出 **`Add a new parameter`** 窗口。
2. **在这个窗口的 `Type` 栏选 `PinString`**，`Identifier` 栏填参数名：
   > 「Identifier: The parameter name to be shown in the testflow editor.」
   > 「Type: The parameter type.」
3. **`OK` 之后参数进类**；**变量名自动生成**——原文：
   > 「Variable: The variable name used in the `run()` function of the test method.
   > It is automatically set as "m" plus parameter name. It can also be changed.」
   ——**（推断）所以一个叫 `pins` 的 PinString 参数，在代码里的变量默认叫 `mpins`**
   （**依据就是这句 `"m" plus parameter name`，原文举的是规则不是例子**）。
4. **填值的地方不在向导里**：`Default` 是 `(Optional) The default value of the parameter.`，
   **真正改值是在 testflow 那一侧**（`Identifier` 那句写的就是 `shown in the testflow editor`）。
5. **改完参数要重新 build 工程**；build 完 **Properties view 会变灰**，
   点右上角的 `Inconsistency Check` 按钮更新它——原文：
   `this view is grayed because the parameters displayed in this view are not consistent with
   those in the test method code`。
   **那个按钮在本篇有一张图**（`118556.png`）：**逐格看就是一个灰底圆角按钮、
   上面一个蓝色对勾图标**——**它就是原文那句 `click the Inconsistency Check button … on the top
   right` 指的控件**，**图里没有文字，按钮名只在正文里。**

**一条与 PinString 直接相关的坑（**本页最有用的一条**）**：

> 原文 `## Before you begin` 写的门槛是：
> 「Make sure you are using SmarTest 6.3 or later, and a test method project has been created.」

**而 `PinString` 是 SmarTest 6.5.0 才加的。**
**所以：在一台 6.3 ~ 6.5.0 之前的机器上，门槛那句话成立，但 `Type` 栏里不会出现 `PinString`。**
**读 `Before you begin` 那一句不足以判断这个类型在不在——要看版本页。**
（**推断**；两条依据都是原文：`Before you begin` 的 `6.3 or later`，
与 `Functional changes` 的 `SmarTest 6.5.0: New parameter types: PinString, SpecVariable`。）

**另一条机制上的提醒**：原文 `Options` 字段写的是
`(Optional) The value candidates of the parameter. The separator between the candidates is a colon (:).`
——**注意那个冒号**：**候选值的分隔符是 `:`，而针名清单的分隔符原文一个字没写**。
**两件事不要混**（**本页不猜 PinString 的值用什么分隔**）。

## 和谁有关

- [[how-to-create-a-universal-test-method-class]] — **上位页（前提）**：
  向导怎么走、六个字段各填什么、build 之后 Properties view 为什么变灰，全在那一页。
  **本页只讲 `PinString` 这一个类型。**
- [[test-method-class]] — **参数被加进去的那个类的来源**：`New > Test Method Class` 向导。
  **`PinString` 是那个向导 `Type` 栏的一个选项。**
- [[file-string]] / [[option-list]] / [[context-pins]] — **与 `PinString` 同出一篇 raw 的姊妹类型**。
  **这三页与本页共用同一篇 `sources:`**（**这是本页从 wiki 那三页的 frontmatter 里看到的，
  不是本篇 raw 写的**——本页没有读那三页的正文）。**各页只写自己那一个类型。**
- [[spec-value]] / [[spec-variable]] — **同族，但**它们的 `sources:` **是各自的专页**
  （`02.07.02.13.03_SpecValue.md` / `02.07.02.13.04_SpecVariable.md`，
  **同样是本页从 wiki 那两页的 frontmatter 里看到的**）。
  **⚠️ 这两篇专页的存在说明：同族五个类型里，`SpecValue` / `SpecVariable` 有专页，
  而 `PinString` 本页没有找到专页**（见 `## 出处`）。**本页没有读那两页。**
- [[pin]] — **`pins` 那个词的所指**（类型说明里的第一个粒度）。
  **pin 是什么、有哪些属性，在那页；本页只有「它可以当参数值」这一个事实。**
- [[pin-group-editor]] — **`pin groups` 那个词的所指**（第三个粒度）。
  **本页只有「pin group 名可以当参数值」这一条；怎么建组在那页。**
- [[pin-utility]] — **（推断）名字近，可能是下游**。本页的 `PinString` 值是
  `pins, pin lists or pin groups`，而 [[pin-utility]] 从页名看是
  **把 pin list（含 pin group 名）展开成具体 pin 名**的那一类东西——
  **两者像是同一件事的两侧（一个是「参数值」，一个是「展开它」）。**
  **但依据只是页名；本篇 raw 里 `pin-utility` 这类名字 0 次，
  本页也没有读那页，所以这是推断，不是原文明写的。**
- [[testflow]] — **参数值被改的那一侧**（`shown in the testflow editor`）。
  **本页只有这一句，testflow 里参数长什么样本页没有。**
- [[test-method-project]] / [[universal-test-method-library]] — **（推断）上下游**：
  `## Before you begin` 要求 `a test method project has been created`，
  `## Results` 说库落在 `Debug` 子目录。**两条都是原文，但那两页本页没读。**
- [[testmethod]] — **stage 归属**。frontmatter 的 `stage: testmethod` 是**「最近的一段」**，
  不是「归属」——参数类型是给 test method 那一段用的。
- `Select the pin string for test method parameter`
  （`99_Unlisted_or_Unreferenced/99.0065_Select_the_pin_string_for_test_method_parameter.md`，
  **未读、未建**）——**本页是在语料目录里按文件名找到它的**（**不是本篇 raw 写的**；
  **本篇 raw 里 `PinString` 没有链接**）。
  **从文件名看它讲的是「为 test method 参数挑 pin string」**，
  但**本页没有读它**，所以**它讲的是不是本页这个 `PinString` 类型、里面有什么，本页一个字都不知道。**
  **⚠️ 注意它的文件名用的是小写带空格的 `pin string`**——**正是词面匹配会指错的那种写法**（见 `## 出处` ②）。
- `Working with Content Assist` / `Working with Test Method Panel`（**两篇，均未读、均未建**）—
  `#### Subtopics` 列的两篇。**本页正文也没提它们。**

> 上面每一条**凡不标「不是本篇 raw」的**，都来自本页读的那一篇 raw。
> **本页没有查 `edges.jsonl`，也没有从别的文档补事实。**

## 版本

本篇 `## Functional changes` **共 8 条**，**与 `PinString` 直接相关的只有一条**：

- **SmarTest 6.5.0**：`New parameter types: PinString, SpecVariable`

**三条读法**：

1. **`PinString` 从 SmarTest 6.5.0 起才有**；本 wiki 面向的 **7.10.3 上在**。
2. **它是这批参数类型里最早的一批**（与 `SpecVariable` 同一条同时加）。
   后面依次是：`SpecValue`（6.5.2）、`ContextPins` / `OptionList`（7.2.0）、
   `FileString`（7.2.1）。**八个版本条目里，`PinString` 那条的版本号最小。**
3. **对照 `Before you begin` 的 `SmarTest 6.3 or later`**——**那一句门槛管不住这个类型**
   （见「典型用法」里那条时限上的坑）。

**第一条条目是 §11.2 ② 那个哨兵值**（`Introduced before SmarTest 6.3.2`）——
**它说的是这篇文档，不是 `PinString`**：**「早于语料覆盖范围」，
不是「6.3.2 新增」，更不是「`PinString` 是 6.3.2 加的」**。
**`PinString` 的引入版本只有 6.5.0 那一条，与哨兵值不是同一件事。**

**其余 6 条与本类型无关**（`New Build Test Method reminding dialog`、
`Supports selecting Template…`、`Added a new class template: Customized shmoo test method class`
等），**本页不重复列出**——**它们逐条列在
[[how-to-create-a-universal-test-method-class]] 的「版本」节里**（那一页是这条流程的主页）。

详见 [[smartest-6.5.0]]（`PinString` 的引入版本）。
另见 [[smartest-6.5.2]] / [[smartest-7.2.0]] / [[smartest-7.2.1]]（后面那几批类型的版本）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md`
（`98956.htm`，94 行）——**整篇读完**。

**本页做了什么**：

- **读了本篇两张图**（`116534.png`、`118556.png`）——
  **这是本页与同批 [[file-string]] 的一处不同，那页两张图都没看。**
  逐格读过之后，两张图的内容是：
  - `116534.png`：**`Properties` 视图**，列是 `Property` / `Value`，
    一棵树 `Test Method Parameters`（计数 **17**）底下一行 `title` / `Example`，
    再底下是被红框圈出的 `x`，其下四行 `start` / `0`、`stop` / `10`、`step` / `1`、
    `scale` / `Linear`——**这正是原文那句「用 `.` 建层次」的例子
    （`x.start` / `x.stop` / `x.step` / `x.scale`）在界面上的样子。**
    ⚠️ **但图上 `title` / `Example` 那一行，原文一个字没提**（那是图上才有的）。
  - `118556.png`：**一个灰底圆角按钮、蓝色对勾图标，图里没有文字**——
    对应原文的 `click the Inconsistency Check button … on the top right`。
  - **两张图都与 `PinString` 这个类型无关**（一张讲参数层次、一张讲那个按钮），
    **所以本页没有从图里得到任何 `PinString` 的事实**——上面两条只是照实记录「图上是什么」。
- **为了核「本页该怎么定位、与哪些页同批」这一句，读了 wiki 的
  `wiki/objects/file-string.md`**（**是 wiki 页，不是 raw**）——
  只用来看同批那页是怎么划范围的（它把「怎么建类」推给 [[how-to-create-a-universal-test-method-class]]）。
  **本页正文没有引用它的任何事实。**

**本页没做的**：

- **`PinString` 的专页没有读，因为本页没有找到它——这是本页最大的空缺。**
  本页做过两件事，照实说清：
  1. **本篇 raw 里 `PinString` 一个链接都没有**（逐字核过：`PinString]` **0** 次）。
     **而 `FileString` / `SpecVariable` / `SpecValue` / `OptionList` 四个都有链接**
     （`ContextPins` 那一节链的是另一个东西 `CCF_FocusedPins`）。
     **所以本篇自己没给出这个类型的出口。**
  2. **本页按文件名在整个语料目录下搜过 `PinString` / `Pin_String`**，
     **唯一的命中是 `99_Unlisted_or_Unreferenced/99.0065_Select_the_pin_string_for_test_method_parameter.md`**
     ——**那篇本页没读**（**它不在本页 `sources:` 里，本页只许读 `sources:` 里那一篇**）。
     **所以「`PinString` 有没有自己的专页」，本页只能说「按文件名没有找到」，
     不能说「语料里没有」**——那篇 99.0065 讲的可能就是它。
  **取值形态、能不能混写、报错、代码里怎么用——本页一个字都没有。**
- **`Subtopics` 列的两篇没读**：`Working with Content Assist`、
  `Working with Test Method Panel`。**本页正文也没提它们。**
- **「怎么建类」的完整流程本页刻意不写**——那是
  [[how-to-create-a-universal-test-method-class]] 的内容，本页只写选类型这一步。
- **`## Results` 段（库落在 `Debug` 子目录）本页没有展开**——那属于那条流程主页。
- **没有去 02.06 的命令参考里找「pin string」** —— **这是本页刻意不做的**：
  本页 `sources:` 只有这一篇，**而本篇 raw 里没有任何命令**（`PADS` 0 次）。
  **所以本页不写「`PinString` 与某条命令是不是一回事」**——
  **这个判断需要读那一侧，本页没读，也不据词面去猜。**
- **本页没有查任何别的 `PinString` 用法** —— 所以若语料别处还有叫 `PinString` 的东西，
  **本页不知道，也不声称「只有这一个」。**
- **没有实跑。** 没有在 SmarTest 里建过带 `PinString` 参数的类、没有填过值。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/testmethod.md`。

> ⚠️ **本页特有的两处，照实记、一处都没替它改**：
>
> **① 本页 slug 与 `title` 不是同一个东西。** slug 是 `pin-string`，
> 而 `title` 是 `How to create a universal test method class`——
> **因为本篇文档是一篇 how-to，`PinString` 只是它里面九行类型清单里的一行。**
> **`title` 本页不许动**（§4/§6 的规矩），**所以这个错位保留着**：
> **按文件名找 `PinString` 会找到一篇讲怎么建类的页。**
> （**同批的 [[file-string]] / [[option-list]] / [[context-pins]] 三页是同一个形态**
> ——`title` 也是 `How to create a universal test method class`；
> **而 [[spec-value]] / [[spec-variable]] 两页有自己的 `title`**（`SpecValue` / `SpecVariable`），
> 因为它们有各自的专页。**这三句本页是从 wiki 那几页的 frontmatter 里看到的，
> 不是本篇 raw 写的。**）
>
> **② 本篇 raw 里 `PinString` 出现 3 次，形态只有一个：驼峰 `PinString`。**
> 本页逐字查过：**`pin string`（小写、带空格）0 次、`PADS` 0 次。**
> **所以词面匹配在这篇里是死路**——**要找 `PinString`，只能搜它的驼峰写法。**
> **本页把这个事实记在这儿，不替它加小写别名。**
>
> ⚠️ **本篇的语料瑕疵（与同批 [[file-string]] 那页记的重叠，但本页照实再记一遍）**：
>
> **③ `Note` 与上一句之间没有空格、也没有换行，直接黏在一起。** 例如逐字：
> `A string set as the parameter comment.Note Parameter hierarchies are supported.`
> 和 `The Create a new Test Method class wizard will pop up.  Note You can separate the header
> file and source file by checking the box before Separate Header File and Source file.`
> ——**这是全文性的排版问题，不是某一处笔误。**（**`PinString` 那一句旁边没有 `Note`，
> 所以这一条不落在本页的正文上，但它就在同一段里。**）
>
> **④ 拼写：`In Templates filed, select:` —— `filed` 应为 `field`。**
> （同一段里 `In the Class Name field` 拼对了。）
>
> **⑤ 清单末项的连接词不齐**：类型清单写成
> `… ContextPins, OptionList **or** FileString.` ——
> **前面各项之间全是逗号，只有最后一项用 `or`。**
> **`PinString` 在这张清单里是用逗号隔开的**（`string, PinString, SpecVariable,`），
> **所以它没有这个毛病；这个问题在末尾那一项上。**
>
> **⑥ 同一件事两种缩写**：讲 concurrent test method 时原文**同时用了 `CTF` 和 `CCF`**
> （`CTF-based test method` / `ccf_tml` / `CCF_FocusedPins`）。
> **与本页的 `PinString` 无关，但同在一篇里，记在这里备查。**
>
> **⑦ §11.2 ① 那种编码损坏本篇没有。** 本页查过：**本篇只有 ASCII**——
> CJK 字符 0 个、U+00A0 0 个、`鈥` 0 个、`鈭` 0 个。
> **§11.2 ⑤ 那个整词替换（`DC/DC power units`）本篇 0 命中。**

`verified: doc-only`
