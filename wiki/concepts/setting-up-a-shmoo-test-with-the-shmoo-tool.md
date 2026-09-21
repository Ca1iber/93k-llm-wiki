---
type: concept
title: Setting up a shmoo test with the Shmoo Tool
layer: n/a
stage: results
tags: [shmoo, shmoo-tool, results, setup, properties-view, test-method, test-suite, mtp]
related: [shmoo-tool, mapping-results, testflow, test-suite, results, mtp-memory-test, structure-of-a-tmlimits-csv-file, smartest-7.2.0, smartest-7.2.1, smartest-7.2.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25.03.02_Setting_up_a_shmoo_test_with_the_Shmoo_Tool.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Setting up a shmoo test with the Shmoo Tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**这一页讲的是「怎么配出一次 shmoo 测试」这件事，不是 Shmoo Tool 是什么。**
工具本身（它能造哪几类 shmoo、它和 testflow / Integrated Result Tool 怎么来往）在 [[shmoo-tool]]，**本页不重复**。

配完的产物，原文 `## Results` 一句话：

> 「A shmoo test is set up with the Shmoo Tool.」

**唯一的入口是 Properties view。** 原文第一句就把它点死了：

> 「Use the Properties view of a shmoo page to set up a shmoo test.」

**操作的位置是「先选页面、再看属性」**：

> 「In the editor view, select a shmoo page. In the relative Properties view, set up a shmoo test by configuring the parameters as the steps below.」

**`editor view` 与 `Properties view` 这两个词是本页所有步骤的坐标系**——在 editor view 里选 shmoo page，在 Properties view 里改参数。原文用 `relative` 限定那个 Properties view（**它是相对当前选中的页面显示的**）。

> ⚠️ **「用 Properties view 设置」这件事本身是有版本的。** 7.2.1 之前 shmoo page 里有自己的 setup panel，7.2.1 把它移除了（逐字见 `## 版本`）。**所以本页描述的是 7.2.1 之后的形态**（推断，依据是版本段那一条 `The setup panel of the Shmoo Tool is removed from the shmoo page. Instead, use the Properties view to set up a shmoo test.`）。

### 四类 shmoo 测试，**设置路径按类型分岔**

原文 `## About this task` 说这台工具能造四种：

> 「Use the Shmoo Tool to create:」

- 对功能测试做 shmoo（`Shmoo over functional tests`）
- 对一个或多个 test suite 做 shmoo（`Shmoo over one or multiple test suites`）
- 自定义 shmoo 测试（`Customized shmoo tests`）——前提是**你已经建过**自定义 shmoo test method
- MTP 的 fail bit count shmoo（`Fail bit count shmoo tests for MTP`）

**这四类在设置上的差别，就是下面那五步的走法差别**：

| 类型 | 走 step 1 吗 | `Testmethod` 字段选什么 | 额外的硬条件 |
|---|---|---|---|
| shmoo over functional tests | **跳过** | `ac_tml.AcTest.Shmoo` | **Pattern 必须选** |
| shmoo over one or multiple test suites | **step 1 是专给它写的**，走完直接跳 step 4 | `ac_tml.AcTest.Shmoo` | **`testMode` 必须是 pass/fail** |
| customized shmoo test | **语料未写** | 你自己建的那个 test method | Analog 只有这一类才要设 |
| fail bit count shmoo（MTP） | **跳过** | `MTP_FailBitCountShmoo.Execute` | 必须已装 MTP 软件；`resultPins` 必须含 dq pin |

> **「跳过 step 1」是原文自己写的，而且只点了两类**（这一句在语料里的形态是坏的，见 `## 出处` 瑕疵③）：
>
> > 「Note Skip step 1 to create shmoo over functional tests or fail bit count shmoo tests for MTP.」
>
> **customized shmoo test 要不要跳 step 1，本篇没有说**——**本页把它记成「语料未写」，不替它填**。

### 关键机制：填了 `shmooTestSuite`，**Primaries 组就消失**

**这是本页最该记住的一条**，它解释了「为什么对 test suite 做 shmoo 不用设 primaries」：

> 「In the shmooTestSuite field, select one or more test suites that have the same primaries (multiple test suite names should be separated with ";"). After that, the Primaries group in the current Properties view will disappear. When shmooing, the shmoo test will automatically use the primaries of the shmooed test suites.」

三点：① 多个 suite 名用 `;` 分隔；② **必须同 primaries**；③ 填完之后 **Primaries 组从当前 Properties view 里消失**——因为 shmoo 会自动用被 shmoo 的 suite 的 primaries。**step 1 末尾那句 `Go to Step 4.` 的道理就在这儿：Primaries 不用你设了。**

### 多 suite 的判定语义：**一格一 Pass/Fail，Fail 取「至少一个」**

> 「Entering one test suite name will shmoo over this test suite.」

> 「Entering multiple test suite names will shmoo over each of these test suites one by one and generate a pass/fail shmoo plot. Each shmoo cell is filled up with either Pass or Fail. Pass indicates all test suites are pass at this cell. Fail indicates at least one test suite is failed at this cell.」

> 「Note that to shmoo over multiple test suites, you must select pass/fail in the testMode field.」

**「至少一个 fail 就整格 fail」这条决定了多 suite 图的读法**——图上写着 Fail，不代表每个 suite 都 fail。**并且它要求 `testMode` 必须是 pass/fail**（原文用 `must`）。**为什么必须，语料没写**（本页不推）。

### step 4：展开 `Testmethod` 组要设的参数

原文第 4 步把参数列成一串。**九个**（外加一条指向 MTP 专篇的指路）：

| 参数 | 默认 | 要点 |
|---|---|---|
| `title` | `"shmoo"` | shmoo 图的标题；**执行后才显示在图上** |
| `shmooTestSuite` | — | 要被 shmoo 的 suite 名；**functional 与 fail bit count 要跳过它**；customized 时视自定义 test method 而定 |
| `x` / `y` | — | X / Y 轴设置。**详情全在另一篇**（`The parameters for the x/y-axis setups for a shmoo test`），**本页一个字没有** |
| `isYAxisFirst` | `OFF` | `ON` = 先变 y，`OFF` = 先变 x |
| `testName` | `Shmoo` | 取值可以来自 test table 或 testflow limits |
| `Testmode` | `pass/fail` | 决定图上显示哪类结果；**可多选**；MTP fail bit count 时默认是 `fail bit count on device` |
| `resultPins` | 所有 pin（`@`） | **只用于** functional 与 MTP fail bit count；选了 `@` 就不能把 `perPinResult` 设 `ON` |
| `perPinResult` | `OFF` | **只用于** functional；`ON` 时能逐 result pin 看图 |

几条逐字的：

> 「title: The title of a shmoo plot. The default title is "shmoo". The title will be displayed on the shmoo plot after execution.」

> 「ON or OFF to create or not create a Y-first shmoo (the y parameter is varied first, then the x parameter). OFF will create an X-first shmoo (the x parameter is varied first, then the y parameter).」

> 「You can enter a test name which has been defined in the test table or testflow limits.」

> 「The modes selected here determine what kinds of test results will be displayed on the shmoo plot, such as pass/fail, error numbers, or measured values.」

> 「You can select multiple modes here. After execution, to view the shmoo plots of different modes, right-click the shmoo plot, select Test Modes and select one test mode.」

> 「Pins that contribute to the shmoo result. The default is all pins (@).」

> 「If you select @, you cannot select ON in the perPinResult field (see next parameter).」

> 「For fail bit count shmoo tests for MTP, the result pins must include dq pins. Otherwise, no numbers will be disaplayed on the shmoo plot.」

> 「ON or OFF enables or disables you to view the shmoo plot of each result pin that is selected in the resultPins field (see the above parameter).」

> 「If you select ON, to view the shmoo plot of different result pins, right-click the shmoo plot, select Result Pin, and select a desired pin.」

**两条适用范围要单独说**（原文对这两个字段各写了 `Used only for`）：

- **`resultPins` / `perPinResult` 只对 functional 与 MTP fail bit count 生效。** 要给 **shmoo over test suite** 或 customized 建 result pins，原文把你指到另一篇去：

> 「Note that, to create result pins for shmoo over test suite, or for customized shmoo tests, see Viewing the test results of a test suite on the shmoo plot.」

**这一点和 `## 版本` 里 7.2.1 那条对得上**（7.2.1 起，对 shmoo over test suite 的设置，`resultPins` 与 `perPinResult` 是**不可见的**）。

> **一处照记、不调和**：`title` 的默认值是 **`"shmoo"`（小写）**，而 `testName` 的默认值是 **`Shmoo`（大写）**。**两个不同的字段、两种写法，原文如此，本页照记。**

## 典型用法

### 前置：原文 `## Before you begin` 四条

| # | 原文 |
|---|---|
| 1 | 「In SmarTest, open a testflow and load its full setups.」 |
| 2 | 「Open the Shmoo Tool and make sure a shmoo page is displayed in the shmoo editor.」 |
| 3 | 还没有 shmoo page 的话先建一个：**右键 shmoo editor 的底栏，用 `New` 命令** |
| 4 | 只有做 MTP 的 fail bit count shmoo 时才要：**必须已装 MTP 软件** |

第 3、4 条的原文：

> 「To create a shmoo page, use the New command after you right-click the bottom bar of the shmoo editor.」

> 「If you want to create a fail bit count shmoo test for MTP, make sure the MTP software is installed.」

**第 1 条是整件事的地基**：shmoo 是**在 testflow 语境里**配的（先开 testflow、加载全部 setups）——这和你只想打开工具看界面是两回事。

### 两条路径

**路径 A —— 对 test suite 做 shmoo**（`## Procedure` 的 step 1，走完直接跳 step 4）

1. `Testmethod` 字段选 `ac_tml.AcTest.Shmoo`：

> 「In the Testmethod field, choose the ac_tml.AcTest.Shmoo test method.」

2. **展开 `Testmethod` 组**，在 `shmooTestSuite` 里填 suite（一个或多个，`;` 分隔，**必须同 primaries**）。填完 Primaries 组消失。
3. **`Go to Step 4.`** —— 跳过 Primaries，直接进参数。

**路径 B —— 其余三类**（step 2 → step 3 → step 4）

1. **展开 `Primaries` 组**，设五组 primaries：

> 「Expand the Primaries group and set up the Timing, Level, Analog, Context, and Pattern primaries.」

其中三类是**必须**的：

> 「For Timing, Level, and Context, you must select a timing set, a level set, and a context.」

Analog 只有 customized 才设：

> 「For Analog, only set it up when you create a customized shmoo test which has analog settings.」

Pattern 分情况：

> 「Do select a pattern for shmoo over functional tests and fail bit count shmoo tests for MTP.」

> 「It is optional for customized shmoo tests, depending on whether the shmoo test uses a pattern or not.」

（`Do select` 是原文的强调用法，**不是笔误**；本页照实引。）

2. **在 `Testmethod` 字段里挑测试方法**，三选一（原文第 3 步）：

> 「A system provided test method, which can perform shmoo functional test and shmoo over test suite.」

> 「A customized shmoo test method, which is available only if you have created it: Select it for setting up a customized shmoo test.」

> 「MTP_FailBitCountShmoo.Execute (available only for MTP): Select it for setting up a fail bit count shmoo test in memory testing.」

**第一项 `ac_tml.AcTest.Shmoo` 是默认**（原文在它后面标了 `(default)`）。

3. **展开 `Testmethod` 组**，设 `## 是什么` 里那九个参数。

> **两条路径在第 1 步和第 3 步上看着像重复**：`Testmethod` 字段在 step 1 与 step 3 里都出现，`ac_tml.AcTest.Shmoo` 在两处都能选。**原文没有解释为什么**——推断：step 1 是 test-suite 路径的入口（选完就跳走），step 3 是其余三类共用的入口。**本页把这个观察写出来，不替原文改结构。**

### 配完之后：原文 `## What to do next` 三条

- **执行 + 看图**（`Executing shmoo tests with the Shmoo Tool` / `Viewing shmoo plots with the Shmoo Tool`）
- **保存这个 shmoo 测试**（`Saving shmoo tests in the Shmoo Tool`）
- **再建新的 shmoo page 去配别的 shmoo 测试**（`Creating multiple shmoo tests in the Shmoo Tool`）

**第三条单列**，说明这个工具的用法是**「一个页面一次测试，多测多页」**（推断，依据是那一条标题、以及 `New` 命令的存在）。**这三篇本页一篇没读**，所以每一步怎么做，**本页一个字没有**。

## 和谁有关

- [[shmoo-tool]] — **上游对象页，也是本页的存在理由。** 那一页给出的是 `set up` → `execute` → `view` 三步链**和这三个动词本身**，并且明写那三篇子主题「一篇都没读」——**本页就是那条链的第一环**。**分工**：那一页讲工具是什么，本页讲「怎么配一次测试」。**本页不重复工具介绍。**
- [[mapping-results]] — **同 stage 的对照页。** 它的表里「shmoo 测试的数据采集与呈现」那一行的 **GUI 格是 [[shmoo-tool]]**；本页是那一格 GUI 动作的展开。**注意一处**：那一页的 `sources:` 里收了本页文档的**子篇** `02.08.04.25.03.02.02_Test_modes.md`（`Test modes`），**本页没读它**。
- [[testflow]] — **硬前置。** 原文 `## Before you begin` 第一条：`In SmarTest, open a testflow and load its full setups.` **没有 testflow，这一步做不了。**
- [[test-suite]] — **`shmooTestSuite` 的取值来源，也是「同 primaries」这条约束的作用对象。** 多 suite 时它们必须共享 primaries。
- [[mtp-memory-test]] — **四种 shmoo 里唯一有专属测试方法（`MTP_FailBitCountShmoo.Execute`）与专属前置（装 MTP 软件）的一类。**
- [[results]] — 本页 `stage: results` 的归属：这是结果侧的动作（配置一个测量 / 判定任务）。
- [[structure-of-a-tmlimits-csv-file]] — **`testName` 的取值来源之一。** 原文说 test name 必须是「在 test table 或 testflow limits 里定义过的」；本篇的链接指向的就是这张表的结构文档。
- [[smartest-7.2.0]] / [[smartest-7.2.1]] / [[smartest-7.2.2]] — `## 版本` 五条的落点。
- `The parameters for the x/y-axis setups for a shmoo test`（**未建、未读**）— **`x` / `y` 两组参数的详情全在那一篇**；本页只知道「有这么两组、要展开」。
- `Test modes`（**未建、未读**）— **`Testmode` 的可选值清单在那一篇**；本页只有「pass/fail、error numbers、measured values」这三个例子。
- `The interface of the Shmoo Tool`（**未建、未读**）— **Properties view 长什么样、`Primaries` / `Testmethod` 这两组怎么折叠，本页不知道**。
- `Shmoo tests in the Shmoo Tool`（**未建、未读**）— 四种 shmoo 的**定义**在那一篇；本页只有它们的**设置差别**。
- `Creating a customized shmoo test method`（**未建、未读**）— customized 路径的前置：**得先有那个 test method**。
- `Fail bit count shmoo test method`（**未建、未读**）— MTP 那条路径的**额外参数**在那一篇。
- `Viewing the test results of a test suite on the shmoo plot`（**未建、未读**）— **`resultPins` / `perPinResult` 够不着的那些场合，答案在那一篇**。
- `Opening the Shmoo Tool` / `Commands in the bottom bar of the Shmoo Tool` / `Context list` / `Tests page`（**均未建、未读**）— 分别回答「怎么打开」「底栏有哪些命令（含 `New`）」「Context 选什么」「testflow limits 页在哪」；**本页只有对它们的链接**。
- `Executing shmoo tests with the Shmoo Tool` / `Viewing shmoo plots with the Shmoo Tool` / `Saving shmoo tests in the Shmoo Tool` / `Creating multiple shmoo tests in the Shmoo Tool`（**均未建、未读**）— **`## What to do next` 的四篇，本页一篇没读**。
- `Shmoo`（raw: `02.07_Test_Method_Reference/02.07.05.01.09_Shmoo.md`，**未建、未读**）— `ac_tml.AcTest.Shmoo` 这个测试方法自己的文档。**本页只知道它的名字与一句定位。**
- [[analysis-views]] — 同 `stage: results` 的另一视角：**本页造 shmoo，那一页把已有的 shmoo 结果当一种视图画出来**（推断，依据是那一页标题落在 analysis view 一类里；**原文没有说两者的关系**）。

## 版本

`## Functional changes` 段有，**五条**：

| 版本 | 条目（逐字） |
|---|---|
| **SmarTest 7.2.0** | `Introduced in SmarTest 7.2.0` |
| **SmarTest 7.2.1** | `The setup panel of the Shmoo Tool is removed from the shmoo page. Instead, use the Properties view to set up a shmoo test.` |
| **SmarTest 7.2.1** | `For the shmoo over test suite setup, the Primaries group in the Properties view disappears.` |
| **SmarTest 7.2.1** | `For the shmoo over test suite setup, the resultPins and perPinResult parameters are invisible.` |
| **SmarTest 7.2.2** | `The shmooTestSuite parameter accepts multiple test suite names to support shmoo over multiple test suites.` |

**三条 7.2.1 是同一批界面搬家**：setup panel 从 shmoo page 里移走 → 改用 Properties view → 于是「对 test suite 做 shmoo」时 Primaries 组消失、`resultPins` / `perPinResult` 不可见。**这三条正是本页正文描述的那个界面的由来**（推断，依据就是这三条本身；**正文「填了 `shmooTestSuite`，Primaries 组就消失」那句与第 2 条说的是同一件事**）。

**7.2.2 那条和正文对得上**：正文里 `shmooTestSuite` 能填多个 suite、用 `;` 分隔——**这个「多个」是 7.2.2 才有的**。**所以 7.2.2 之前的机上，`shmooTestSuite` 只能填一个**（推断，依据是这一条里的 `accepts multiple test suite names`）。

**这一篇没有 `Introduced before SmarTest 6.3.2` 那种哨兵写法**——它写的是 `Introduced in SmarTest 7.2.0`，即**真新增**（对比：[[dfgp]] 那一篇的 `## 版本` 就只有哨兵值一条）。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25.03.02_Setting_up_a_shmoo_test_with_the_Shmoo_Tool.md`
（TDC `136294.htm`，9,520 字节，130 行）。**整篇读完**，本页引文全部来自这一篇。

**本页没做的**：

- **`sources` 之外一篇没读。** 上面「和谁有关」里列出的那十六个未读目标，**一个都没读**。所以：
  `x` / `y` 两组参数**有哪些、怎么设**，`Testmode` 的**完整取值清单**，
  **Properties view 的界面形态**，四种 shmoo 的**定义**，MTP 的**额外参数**，
  **shmoo over test suite 的 result pins 怎么建**，以及**执行 / 看图 / 保存 / 建多页**——
  **本页一个字都没有**，只有原文在这一篇里给出的链接。
- **两张子篇（`The parameters for the x/y-axis setups for a shmoo test`、`Test modes`）没读**，
  而它们是本文档 `## Subtopics` 列出的**全部**子篇。**本页的「语法 / 参数」节是空的**——
  脚本判定：本文档没有 `Syntax` / `Parameters` / `Example` 这类**段标记**（§4）。
  **这不是省略**：这一篇本身就是个任务页，参数分散在 `## Procedure` 的步骤里。
- **图：本篇文档没有内嵌图片**，所以**本页没有 ④ 图证**。
  判据可核：本篇 md 里 `png` / `jpg` / `![` **0 命中**，
  其上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\136294.htm` 里 `<img` 与 `.png` **也 0 命中**。
  **不是「图够不着」，是这篇文档本身不带图**——**所以「Properties view 长什么样」本页的图证是零**。
- **没有实跑。** 没有在 SmarTest 里开过 Shmoo Tool、没有建过 shmoo page、没有配过任何一种 shmoo。
  `verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/results.md`。

> ⚠️ **本篇的语料瑕疵，照实记下、一处都没替它改**（§11.2）：
>
> **① 拼写错**（逐字引）：`For fail bit count shmoo tests for MTP, the result pins must include dq pins. Otherwise, no numbers will be disaplayed on the shmoo plot.`
> ——**`disaplayed` 应为 `displayed`**。**本页正文引这一句时保留了原文的错法，没有替换成正确拼写。**
>
> **② 同一字段两种大小写**（逐字引）：第 1 步里写的是 **`testMode`**
> （`Note that to shmoo over multiple test suites, you must select pass/fail in the testMode field.`），
> 第 4 步的参数清单里写的是 **`Testmode`**（`Testmode: The default mode is pass/fail.`）。
> **同一个字段、原文两种拼法。本页并列，不调和。**
>
> **③ `Note` 标签被压平进正文。** 逐字是：
> `To create shmoo over one or multiple test suites: Note Skip step 1 to create shmoo over functional tests or fail bit count shmoo tests for MTP.`
> ——**`Note` 是那个提示框的标签，它和提示的第一句粘在了一起**，
> 看起来像 step 1 的正文里插了半句话。**上游 htm 里它本来是个独立的提示块**（`<div class="note">` 里带一个 `Note` 标签），
> **标签与正文是分开的两个元素**。**所以这是转换造成的**（§11.2 那张表的「转换坏的」那一栏），**不是上游写错**。
> **本页照实记，不改。**
>
> **④ `## Related information` 的五条链接首尾相接、中间没有分隔符**。逐字引其中两条：
> `[Shmoo tests in the Shmoo Tool](<02.08.04.25.03.01_Shmoo_tests_in_the_Shmoo_Tool.md>)[Shmoo](<../02.07_Test_Method_Reference/02.07.05.01.09_Shmoo.md>)`
> ——**两个 `](<` 之间一个字符都没有**（前一个链接的右括号之后紧跟着下一个链接的左括号）。
> 其余三条（`Creating a customized shmoo test method`、`Fail bit count shmoo test method`、
> `The parameters for the x/y-axis setups for a shmoo test`）同样首尾相接。
> **原文应是列表或被分隔的条目。本页照实记，不替它补分隔符。**

`verified: doc-only`
