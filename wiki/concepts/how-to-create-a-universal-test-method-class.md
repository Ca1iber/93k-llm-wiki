---
type: concept
title: How to create a universal test method class
layer: n/a
stage: testmethod
tags: [testmethod, project, wizard, parameter, gui]
related: [testmethod, test-method-class, test-method-project, universal-test-method-library, testflow, file-string, spec-variable, spec-value, option-list, context-pins]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md
created: 2026-09-18
updated: 2026-09-20
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

**这一页是「用向导建一个 test method class」的完整操作流程**，不是 test method 的原理页。
原文自己的一句话把范围钉死了：

> 「This topic shows how to create a test method class **step by step** in SmarTest.」
> 建它用 **Create a new TestMethod class wizard**。

**页码性质说清楚**：本页的正文几乎全部是**向导里那几个字段填什么**——
**「test method 是什么」不在这里**（那是 [[testmethod]] 的活）。

### 向导里有三个模板，选错就是另一种东西

原文 `Templates` 字段给三项，**它们产出的不是同一种 test method**：

| 模板 | 对应什么 |
|---|---|
| **Normal test method class** | 普通 test method |
| **Concurrent test method class** | **CTF 基础的** test method（CTF = concurrent test framework） |
| **Customized shmoo test method class** | 定制的 shmoo test method |

> **原文另有一条管理上的建议**（不是硬限制）：
> 「To easily manage the test methods, **it is not recommended** to put normal test methods and
> concurrent test methods in one project.」

### 参数类型是一张封闭清单——这是本页最有用的一张表

参数在向导的 `Parameters` 区点 `Add` 加，`Type` 字段可选的值**原文逐个解释了**：

| 类型 | 用来填什么 |
|---|---|
| `int` / `double` / `string` | 基本类型 |
| **`PinString`** | **pins、pin lists 或 pin groups** |
| **`SpecVariable`** | **timing 或 level 文件里定义的 spec variable** |
| **`SpecValue`** | **格式是 `"value[unit]"`** |
| **`ContextPins`** | 用来定义 CTF 里的参数 `CCF_FocusedPins` |
| **`OptionList`** | **一个参数可以有多条候选值** |
| **`FileString`** | **文件名**当参数值用 |

**其中四个（`SpecVariable` / `SpecValue` / `OptionList` / `FileString` / `ContextPins`）
原文都链到了各自的专页**——本页只给一句定义。

### 每个参数要填六个字段

| 字段 | 是什么 | 必填 |
|---|---|---|
| **Identifier** | **参数名，会显示在 testflow editor 里** | 是 |
| **Type** | 上面的类型清单 | 是 |
| **Variable** | **`run()` 里用的变量名** | 是 |
| **Default** | 默认值 | 否（原文标 Optional） |
| **Options** | **候选值，分隔符是冒号 `:`**；在 test suite view 里改参数值时显示 | 否 |
| **Comment** | 参数字符串注释 | 否 |

**两条容易漏的：**

> **① `Variable` 是自动生成的**——原文写
> `It is automatically set as "m" plus parameter name. It can also be changed.`
> **即参数 `vcc` 默认生成变量 `mvcc`。** 这个 `m` 前缀不知道就会在 `run()` 里找不到变量。

> **② 参数可以用 `.` 分层**——原文：
> `Parameter hierarchies are supported. You can use "." to create a parameter hierarchy.`
> 例：定义 `x.start` / `x.stop` / `x.step` / `x.scale`，**在 Properties view 里会按层次显示**
> （原文配了一张图 `116534.png`，**本页没看那张图**）。

### 类名有一条硬规则

> 「It must **start with an upper case character**. Otherwise an error message is displayed.」

**首字母必须大写，否则向导直接报错。**
原文另给一条**避免**型的建议：`Avoid using the same class name for different UTM projects.`
——**真要用同名，就把源文件放进不同的子目录**，靠相对路径区分。

### 加完参数之后会撞上的那个坑：Properties view 变灰

这是本页最值得记的一条**操作后果**，原文用 `Note` 写在一个不起眼的位置：

> 「After you add or remove the parameters and rebuild the test method project, open the
> Properties view for the test suite using this test method, you will see that **this view is
> grayed because the parameters displayed in this view are not consistent with those in the
> test method code**. To activate the Properties view, click the **Inconsistency Check button**
> on the top right to update the parameter settings in the view according to the test method code.」

**即：改了参数 → Properties view 变灰 → 点右上角 `Inconsistency Check` 按钮才恢复。**
**灰不是坏了，是「视图里显示的参数和代码里的对不上」。**

### 输出：库落在哪

原文 `## Results` 只给了一句 + 一个例子路径：

> 「You will find the test method library in the **`Debug` sub-directory** of the test method
> project directory.」例：`/home/demo/devices/act299_tml/Debug/`

**注意这是原文给的例子路径，不是所有工程的固定路径。**

## 典型用法

原文的 `## Procedure` 是一条顺序步骤，本页照它的顺序列：

**前置（`## Before you begin`）**：**SmarTest 6.3 或更高** + **已经建好一个 test method project**。

1. **`C/C++` perspective 里右键 test method project → `New > Test Method Class`**，
   向导弹出。原文顺带一句：勾 `Separate Header File and Source file` 可把头文件和源文件分开。
2. **在 `Templates` 里选** 三个模板之一（见上表）。
3. **`Class Name` 填类名**——**首字母必须大写**。
4. **加输入参数**：`Parameters` 区右侧 `Add` → 填六个字段 → `OK`。**要几个加几个。**
5. **加输出参数**：从 `result0` / `result1` / `result2` / `result3` 里选。
6. **加 limit**：`Limits` 区右侧 `Add` → **只填 limit 名字** → `OK`。
   **limit 的值不在这里设**，在 tabular testflow editor 里设
   （原文指向 `Limits tab` / `Properties View` 两篇，**本页都没读**）。
7. **`Finish`** → 看到类源文件模板。
8. **写代码**：normal test method 写在 `run()` 函数里；
   concurrent test method 按另一篇的说明实现（`How to implement a concurrent test method`，
   **本页没读**）。
9. **`Build Project`**（右键工程 → `Build Project`）。
   会弹一个对话框提醒：**build 或 clean 工程**不会让它的库**对当前 device 生效**。
   也可以**通过 build 引用了它的 device project 来建它**。
10. **有错就改源文件重 build**。编译信息在 `Console view` 的 **C-Build console** 里；
    **build 了多个工程时，在 Project Explorer 里高亮某个工程，就能只看它的编译信息。**

**Concurrent 模板多一步**：`Finish` 之前可以点 `Next` 选导入的 `ccf_tml` 的存放路径。
**已导入过 `ccf_tml` 时会比版本**——版本和当前 SmarTest 自带的一样就不再导入，
不一样会弹警告问你要不要替换原来的。

**下一步（`## What to do next`）**：**Create a testflow.**（一句话，没展开。）

**一条「什么时候要回来改」的提醒**：原文 `Note` 说**参数加了/删了之后可以直接改 test method 源文件**
——不一定要重走向导。

## 和谁有关

- [[testmethod]] — 本页 `stage: testmethod` 的理由：**它是建 test method 的第一道工序**
- [[test-method-class]] / [[test-method-project]] — 本页建的东西 / 建它的前提
- [[universal-test-method-library]] — **本页第 9–10 步 `Build Project` 产出的就是它**
- [[testflow]] — **`## What to do next` 指向它**：建完类要去建 testflow 才跑得起来
- [[file-string]] / [[spec-variable]] / [[spec-value]] / [[option-list]] / [[context-pins]] —
  **参数类型清单里那五个各有专页的类型**；本页只给一句话定义，细节在它们那里
- [[how-to-create-a-universal-test-method-class]] 之外，
  `Working with Content Assist` / `Working with Test Method Panel`（**均未建**）—
  原文列在 `Subtopics` 里的两篇，**本页没读、也没提**
- `Create a new TestMethod class wizard` / `Properties view` / `Inconsistency Check`（**均未建**）—
  **本页三个只在正文里被点名、没有专页的东西**
- `Limits tab` / `Properties View`（**均未建**）— 第 6 步里 limit 值真正被设的地方
- `Console view` / `Project Explorer`（**均未建**）— 第 10 步看编译信息的地方

## 版本

- Introduced before SmarTest 6.3.2
- **SmarTest 6.5.0**：New parameter types: **PinString, SpecVariable**
- **SmarTest 6.5.2**：New **Build Test Method reminding dialog**
- **SmarTest 6.5.2**：New parameter type **SpecValue**
- **SmarTest 7.1.3**：Supports **selecting Template of test method class in the wizard**
- **SmarTest 7.2.0**：Added a new class template: **Customized shmoo test method class**
- **SmarTest 7.2.0**：New parameter types: **ContextPins, OptionList**
- **SmarTest 7.2.1**：New parameter type **FileString**

> **这张表和正文对得非常整齐**：正文那张七个参数类型的清单，
> 正是 6.5.0 → 6.5.2 → 7.2.0 → 7.2.1 四次版本累加出来的；
> 正文 `Templates` 里三个模板里的第三个（`Customized shmoo`）正好是 7.2.0 加的。
> **也说明 6.3 时代的向导比现在少很多东西**——`Before you begin` 只要求 6.3。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md`

**本页没做的**：

- **`Subtopics` 列的两篇一篇没读**：`Working with Content Assist`、
  `Working with Test Method Panel`。**本页正文里也没提它们**。
- **图一张没看**：`116534.png`（参数层次在 Properties view 里长什么样）、
  `118556.png`（`Inconsistency Check` 按钮）。**本页没有任何来自图的结论**——
  **`Inconsistency Check` 按钮长什么样、在哪，本页只知道「右上角」和名字。**
- **正文里链出去的好几篇没读**：`FileString` / `SpecVariable` / `SpecValue` /
  `OptionList` / `How to implement a concurrent test method` / `How to create a
  universal-test-method-based testflow` / `Limits tab` / `Properties View` / `Console view` /
  `CCF_FocusedPins` / `Test method parameters`。**所以本页只有一句话级别的类型说明。**
- **`## Results` 给的 `/home/demo/devices/act299_tml/Debug/` 是原文的例子路径**，
  **本页照抄，没有说这是通用路径**。
- **`## Before you begin` 里的「a test method project has been created」没展开**
  ——**怎么建那个 project 本页没有**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`Templates filed` 应为 `Templates field`**——原文写的是
> `In Templates filed, select:`，**`filed` 是 `field` 的笔误**。
> ② **`## Procedure` 的步骤是「破折号 + 空格」开头的列表项**
> （`-  In the C/C++ perspective, right-click…`），
> 和本语料其它同型文档的写法一致，但**和 `## Procedures`（复数）那种标题用法混用**。
> ③ **`## What to do next` 只有三个词**（`Create a testflow.`），
> 没有链接也没有路径——**指向的文档得自己找**。
> ④ **`Comment` 那一条和紧跟其后的 `Note` 之间没有换行**，原文是
> `Comment: (Optional) A string set as the parameter comment.Note Parameter hierarchies are
> supported.`——**`comment.` 和 `Note` 直接粘在一起，句号后面没有空格。**
> **这条 `Note` 讲的是参数分层，和 `Comment` 字段无关**，
> 粘在一起读起来像是 `Comment` 的补充说明。

`verified: doc-only`
