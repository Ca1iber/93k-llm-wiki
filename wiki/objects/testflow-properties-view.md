---
type: object
title: Testflow Properties view
layer: gui
stage: testflow
tags: [testflow-properties-view, gui, testflow, test-suite-properties, site-control, inconsistency-check, utm-parameters, flags, primaries]
related: [testflow, mapping-testflow, mapping-testmethod, flow-sequence-editor, testflow-tool, flow-data-editor, testflow-file, test-suite, test-suites-page, flags-page, alphabetical-list-of-flags, test-program-explorer, spec-variable, spec-value, pin-string, smartest-6.3.2, smartest-6.5.0, smartest-6.5.2, smartest-6.5.3]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.04_Testflow_Properties_view.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Testflow Properties view

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Testflow Properties view 是 Testflow Tool 里那个「选中什么、就显示什么属性」的视图。** 原文第一句：

> 「The Properties view is part of the Testflow and other tools.」

**它有两档，区别只看你在哪里选**（原文第二、三句）：

> 「When you select the testflow item in the Test Program Explorer, the Properties view shows the information of the current testflow.」

> 「When you choose a test suite, bin, group, flow control node, Assign Value node, or Print node in the testflow, this view displays that element's settings and you can edit them.」

| 你选中的是什么 | 这个视图给你什么 | 能不能改 |
|---|---|---|
| **testflow 项本身**（在 [[test-program-explorer]] 里选） | **当前 testflow 的信息** | 原文这一句**没说能不能改** |
| test suite / bin / group / flow control node / Assign Value node / Print node | **那个元素的设置** | **明文：`you can edit them`** |

**「testflow 那一档到底显示哪几项」原文没写**，但图上有（`110713.png`）——**那一格按 §11.4 的判据不够干净，理由见下面「图证」一节。**

### test suite 那一档：四个分组（原文的列表项）

原文 `## Test suite properties view` 一节先给一句总纲：

> 「The test suite properties view shows all properties of the test suite that is currently selected in the Flow Sequence Editor.」

（那句话里的 `Flow Sequence Editor` 在原文里是**语料内部链接**，指向 [[flow-sequence-editor]]——**本页没读那一篇**。）

然后是四个列表项，**这就是这个视图的分组结构**：

| 分组 | 原文（逐字） | 能不能改 |
|---|---|---|
| `Test Suite` | 「Shows the comment, the primary settings, the test type and the test method used in this test suite. You can modify all these settings except the test type.」 | **除 `Test Type` 外都能改** |
| `Flags` | 「Shows the settings of all the test suite flags. You can modify the settings of the test suite flags.」 | 能改 |
| `Site Control` | 「Controls the multi-site test sequence of this test suite.」 | 原文只有 `Controls`，没说能不能改 |
| `Results(Site in Focus)` | 「Shows the test results of the site in focus.」 | 原文只有 `Shows`，没说能不能改 |

**`Test Suite` 那一组的「primary settings」到底有哪几项**：原文正文没列，**图上有**（`355677.png` 里 `Primaries` 展开是 `Timing` / `Level` / `Analog` / `Pattern` / `Context`），见「图证」。

### `Site Control` 那一组的子项（原文列了四类设置 + 一条 `Note`）

| 子项 | 原文（逐字） |
|---|---|
| `Site Match` | 「controls the site match function of the test suite」 |
| `Allow Parallel` | 「controls whether the parallel execution of the test suite is allowed. If you do not check the option Allow Parallel, all the sites will be excuted in serial and the site control settings below will not work.」 |
| `Site Control` | 「controls the multi-site execution mode of the test suite. It can be PARALLEL, SERIAL, SEMIPARALLEL, OTHER or UNDEF.」 |
| `Size and Cycle` | 「The parameters Size and Cycle are only useful if you choose to execute the sites in SEMIPARALLEL mode. Refer to Expanded Site Control window for the details of these parameters.」 |
| `execution sequence (#1, #2, #3, #4)` | 「applies only for the OTHER mode. You can specify the site number in the text editor after the execution sequence.」 |

**原文还写着：这五个名字的定义都在别处**——`Site Match` / `Allow Parallel` / `Site Control` /
`Size and Cycle` / `execution sequence` **五个名字在原文里逐个链到 `Alphabetical list of flags`
（`02.08.04.32.01.02.07.01`）的锚点**。**那是这一篇自己给的指路，本页没读那篇**（[[alphabetical-list-of-flags]]）。

**`Allow Parallel` 那一条是本页里最实用的一句**：**不勾它，下面那一堆 site control 设置全都不起作用**。

**`OTHER` 与 `UNDEF` 两个模式只能在这里设**（原文那条 `Note`）：

> 「Note You can set the modes OTHER and UNDEF in the Testflow Properties view only. You cannot set them in the Expanded Site Control window.」

**这句话把本页的位置钉死了**：`OTHER` / `UNDEF` 这两个模式的**唯一入口**就是 Testflow Properties view。

**默认值那两句把串并行为推给了 test method**：

> 「UNDEF is used by default when you create a test suite. If you Do not change it, the test suite of different sites will be executed serially or parallel according to whether it is implemented serially or parallel in the test method.」

**即：不动这个视图，多 site 的串并行为由 test method 自己怎么写决定。**

### 三个 `## ` 小节：本页真正讲「显示与编辑行为」的地方

**① `## Invalid primary set display`**

> 「The invalid primary set will be displayed with a yellow background and a warning icon, if you select the Automatic Validate Setups checkbox in the Test Suites preference page.」

| 条件 | 结果 |
|---|---|
| 勾了 `Automatic Validate Setups`（`Test Suites preference page`，`01.01.14.26`，**本页没读**） | 无效 primary set **黄底 + 警告图标** |
| 没勾 | **原文未写** |

**② `## Universal test method parameter display and modification`——三个属性与它们盖来盖去的顺序**

> 「Universal test method parameters have three properties. They can be valid or invalid, enabled or disabled, visible or invisible.」

| 属性 | 视图上的样子（原文逐字） |
|---|---|
| `invalid` | 「it is displayed with a yellow background and a warning icon in the Properties view.」 |
| `disabled` | 「it is grayed out in the Properties view.」 |
| `invisible` | 「it is not displayed in the Properties view.」 |

**优先级原文写死了两句**：

> 「The invisible property overrides the invalid and disabled properties. The disabled property overrides the invalid property.」

**排出来就是 `invisible` > `disabled` > `invalid`**（即：不可见盖掉一切；在可见的前提下，`disabled` 盖掉 `invalid`）。
**这个排序是本页把上面两句并起来读的（推断）**，依据是 `overrides` 两两之间的传递关系——**原文没有画成一条链。**

**两个边界**（同一段里，原文自己给的）：

> 「If a parameter value is a testflow variable or expression, all parameters are visible and assumed to be enabled and valid.」

> 「For a hierarchy parameter tree, you cannot see the annotation at the root when some or all of its child parameters are invalid, disabled or invisible.」

**第一句是一条反直觉的规则**：**参数值一旦是 testflow 变量或表达式，那三个属性就全都不作数了**（**原文：`all parameters are visible and assumed to be enabled and valid`**）。
**第二句是另一条边界，管的是层级参数树**：子参数被标成 `invalid` / `disabled` / `invisible` 时，**根节点上看不到那个标注**。

**怎么改值**：

> 「To modify a parameter value, you can type in a value directly or select a value from the defined options. For parameters of SpecVariable, SpecValue, or PinString, you can also select a value from the defined spec variables and pins by clicking the ... button.」

**三类参数多一个入口**：`SpecVariable` / `SpecValue` / `PinString`（对象页分别是 [[spec-variable]] / [[spec-value]] / [[pin-string]]）**多一个 `...` 按钮**，可以从**已定义的 spec variable 与 pin** 里挑。

**③ `## Test method parameter and limit inconsistency check`——改了 test method 之后怎么同步**

> 「If you modified the parameter or limit definition of a test method which is used by a test suite, the Properties view will be grayed out after you build the test method. The Inconsistency Check button will be enabled.」

> 「Click the Inconsistency Check button, check the changes of parameters or limits and click OK. The changes of parameters or limits in the test method will be reflected in the Properties view.」

| 你做了什么 | 视图的状态 | 该做什么 |
|---|---|---|
| 改了某 test method 的**参数或 limit 定义**，并 build 了它 | **视图变灰**；`Inconsistency Check` 按钮**变为可用** | 点 `Inconsistency Check` → 看参数/limit 的变更 → `OK` → **改动反映进视图** |
| 没改 / 没 build | 原文未写 | 原文未写 |

**这一节的顺序要读准**：**变灰不是在改的时候发生的，是 `after you build the test method`**——原文把因果写死在那一句里。
**图证**：弹出来的不是一个「确定/取消」框，是一个 `Text Compare` 窗口（见「图证」）。

### 图证（④ 档）：本篇六张图，一张没漏

**本页 `sources:` 那一篇对 `raw/` 的图片引用正好 6 处**，逐张读过。**先给结论：四张图补上了原文没写的东西，
两张主要是复述正文。**

| 图 | 原文里的 alt | 图上逐字读到的 | 图里的字在 raw 里 grep 得到吗 |
|---|---|---|---|
| `110713.png` | `Properties view showing testflow information` | 列头 `Property` / `Value`；一行 `device`，下面缩进三行 `external` = `false`、`path` =（空）、`saved` = `false` | **三个字段名是普通英文词，别处都有——这一格不是干净的 ④**（见下） |
| `355677.png` | `Testflow Properties view` | `Test Suite` = `Test_1`；`Comment` = `...`；`Primaries` = `...`，展开是 `Timing` = `1, 1, 1`、`Level` = `1, 1, 1`、`Analog`(折叠)、`Pattern` = `Test_1_pattern`、`Context` = `DEFAULT`（灰）；`Test Type` = `M`；`Test Method` = `TML.Test_1`，展开是 `Parameters` = `456, 1`、`tmParameter_1` = `456`、`tmParameter_2` = `1`、`Limits` = `...`；`Flags` = `...`；`Site Control` = `...`；`Results (Site in Focus)` = `Fail, 0` | **`TML.Test_1` / `tmParameter_1` / `tmParameter_2` 均 0 命中**；`Test_1_pattern` 1 命中、`tmParameter` 2 命中，**都在别的篇里** |
| `119756.png` | `Properties view displaying test suite information` | `Test Suite` = `Continuity_Neg_DVI`；`Level` = `1, 1, 5`；`Equation` = `1 [digital_pin_level]`；`Spec/DPS` = `1 [vdd_nom]`；`Set` = `5`（**黄底**）；`Pattern` = `"dummy"`；`Context` = `DEFAULT`；**树节点上带红色警示图标** | **`Continuity_Neg_DVI` / `digital_pin_level` / `vdd_nom` 均 0 命中**；`Invalid primary set` 有 1 命中，**是本篇自己的小节标题 `## Invalid primary set display`** |
| `111394.png` | `Universal test method parameter display and modification` | `Test Suite` = `current_variable`；`Test Method` = `myutm.Class1`；`Parameters` = `normal, disable, -1, pinlist, spec`（灰）；五行参数 `normal_parameter` = `normal`、`disable_parameter` = `disable`（**灰**）、`invalid_parameter` = `-1`（**黄底 + 警示图标**）、`pinlist_parameter` = `pinlist`（**格子右侧带 `...` 按钮**）、`spec_parameter` = `spec` | **`normal_parameter` / `disable_parameter` / `invalid_parameter` / `pinlist_parameter` / `spec_parameter` / `current_variable` 均 0 命中**（`myutm` 1 命中，在别篇） |
| `119669.png` | `Inconsistency check` | 视图**整体变灰**，可见项 `Limits` / `Flags` / `Test Number` / `Test Level` = `0` / `Bypass` / `Set pass`；工具栏上一个按钮带**浮出的提示框**，逐字 `Inconsistency Check`；顶部有 `type filter text`；页签 `Properties` / `Outline` / `Make Targets` | `Inconsistency Check` 有 3 命中（**都在正文里，就是那个按钮的名字**）；**`type filter text` 0 命中** |
| `119670.png` | `Adjust testflow to parameter changes in test method library`（**这句是 alt、正文里搜得到，所以它本身不算图证**） | 窗口里的字样 `Text Compare`；左栏标题 `Test Method parameters and/`（被裁）+ `defined limits in testflow`；右栏标题 `Test Method parameters and/or limits in library`；左栏行 `1Parameters: 3` / `2  vForce_high` / `3  vForce_low` / `4  settling_time` / `5Limits: 0`；右栏同样五行、`5Limits: 1`、`6  leakage_limit N/A X N/A::`；按钮 `OK` / `Cancel` | **`Text Compare` / `leakage_limit` / `N/A X N/A` 均 0 命中**；`vForce_high` 3 命中、`settling_time` 7 命中，**都在别篇、都不是这个对话框** |

**⚠️ 六张图上都有红色的英文注记**（`Invalid primary set`、`disabled parameter`、`invalid parameter`、`button`、`editable text`）
——**那些是截图时加上的箭头与说明，不是界面上的字**，**本页没有把它们当控件名**
（`Invalid primary set` 例外地与本篇的小节标题重合，已在上表注明）。

**图解决掉的三件事**（原文没写、图上有）：

1. **testflow 那一档显示哪几项**——`110713.png` 上是 `external` / `path` / `saved`，挂在 `device` 之下。
   **这一格要照实标**：那三个名字是普通英文词，语料别处也有，**grep 无法把它们与这张图对上**
   （判据 §11.4 要求「图里的字 grep 不到」，**这一格不满足**）——
   **所以本页把它当「图补上了粒度」记，不当成干净的 ④ 档。**
2. **三个属性在视图上长什么样**——`111394.png` **一张图里同时出现** `invalid` 的黄底 + 警示图标、
   `disabled` 的灰、以及 `PinString` 那一格右侧的 `...` 按钮，**正好对上正文那三段文字**。
3. **「参数/limit 不一致」时弹的是一个 `Text Compare` 窗口**，两栏分别是
   `…defined limits in testflow` 与 `…limits in library`，差的那一条是 `leakage_limit`，右栏给它标了 `N/A`
   ——**原文只写了 `check the changes of parameters or limits and click OK`，没写这个窗口叫什么、长什么样。**

**图上读到的名字，回 `## Functional changes` 核过（§11.4 的规矩）**：

- `SmarTest 6.5.0: Parameter property is displayed in Testsuite view.` —— 图上确实有 `Parameters` 这一项
  （`355677.png` / `111394.png`）。**这条版本记录说它 6.5.0 才出现**，**图上没有版本标注，本页不判这两张图的版本。**
- `SmarTest 6.5.3: The function of choosing which items can be shown in the Properties view is removed.`
  —— `119756.png` / `111394.png` / `119669.png` **三张图的顶部都有一个 `type filter text` 输入框**。
  **「这个过滤框是不是 6.5.3 删掉的那个『选择显示哪些项』的功能」原文没说，本页不判**（图没有版本标注）。
- `SmarTest 6.5.2: Properties view replaces Testsuite view.` —— **六张图上的页签逐字都是 `Properties`**，
  而版本记录里这个视图在 6.5.0 / 6.5.2 两条里都叫 `Testsuite view`。
  **两者一致**（`Properties` 是 6.5.2 之后的名字）——**这是（推断）**，依据是页签名与那条版本记录；
  **图上没有版本号，所以这只是「一致」，不是「证明这些图是 6.5.2 之后截的」。**
- 剩下的 `Introduced before SmarTest 6.3.2` 是哨兵值（见「版本」），**不影响图上任何名字**。

**图答不了的（照实说）**：

- **`110713.png` 那三个字段的取值含义**（`external` = `false` 是什么意思）**语料未写**。
- **`355677.png` 上的 `Test Type` = `M`**：`M` 是哪一种类型，本页的出处文档没写
  （它只说 `Test Type` **能看不能改**）。
- **`119670.png` 里 `N/A X N/A::` 那三段的含义**语料未写，**本页不猜**。
- **图是「某一次具体配置」的截图，不是格式规范**：哪些字段必填、哪些组合非法，**图答不了**。

## 典型用法

原文**没有** `## Procedure`，也**没有** `## Before you begin`——**怎么打开这个视图本页答不了**
（`Related information` 里的 `Opening the Testflow Tool` 与 `Editing a test suite in the Flow Data Editor` 两篇，**本页都没读**）。
把原文几节拼起来，可用的路径只有这些：

1. **选什么看什么**：在 [[test-program-explorer]] 里选 testflow 项 → 看当前 testflow 的信息；
   在 testflow 里选 test suite / bin / group / flow control node / Assign Value node / Print node → 看并改那个元素。
2. **test suite 那一档**：按四个分组读（`Test Suite` / `Flags` / `Site Control` / `Results(Site in Focus)`）；
   **`Test Type` 只能看不能改**。
3. **多 site 串并**：`Site Control` → 先勾 `Allow Parallel`（**不勾则全串行、下面那些设置全不起作用**）
   → 再选模式（`PARALLEL` / `SERIAL` / `SEMIPARALLEL` / `OTHER` / `UNDEF`）
   → 只有 `SEMIPARALLEL` 才用 `Size and Cycle`、只有 `OTHER` 才用 `execution sequence`。
   **默认是 `UNDEF`**，那时串并由 test method 自己决定。
4. **test method 改了参数/limit 之后**：build test method → 视图变灰 → 点 `Inconsistency Check` → 看 diff → `OK`。
5. **改参数值**：直接输入、或从已定义的选项里选；`SpecVariable` / `SpecValue` / `PinString` 三种还可以点 `...` 按钮。

| 想干什么 | 去哪一组 | 依据 |
|---|---|---|
| 看/改 comment、时序与电平设置、用哪个 test method | `Test Suite` | 那一组的原文 |
| 看/改 test suite flag | `Flags` | 同上 |
| 让这个 test suite 能并行跑 | `Site Control` → `Allow Parallel` | 那一组的第一条 |
| 指定站点执行顺序 | `Site Control` → `execution sequence`（**只对 `OTHER`**） | 同上 |
| 看当前聚焦 site 的结果 | `Results(Site in Focus)` | 那一组的原文 |
| 参数/limit 改了之后让视图重新生效 | `Inconsistency Check` 按钮 | 那一节 |

**原文一处也没写「操作步骤」**，**上表是本页按原文那一节的归属关系排的（推断）**——每一格的依据都是那一组自己的原文句子。

## 和谁有关

- [[testflow]] / [[mapping-testflow]] — **本页 `stage: testflow` 的理由**。**[[mapping-testflow]] 的主表里没有一格填本页**（本页核对过：`testflow-properties-view` 在那页**只出现在 frontmatter 的 `related:` 里**）；它的 `sources:` 里倒是有本页这一篇，但**它自己声明只读了那一篇的前 30 行**。**两页没有冲突，只是分工不同。**
- [[mapping-testmethod]] — **「limit 的**值**」那一行（主表第 10 行）的 GUI 格写的就是本页与 [[test-suites-page]]**，并在那里标了「（**图证**）：`Lower Limit` 列在 Tests 页签里」。**照实说一句**：那个图证来自**另一篇文档的图**（`110086.png` 的 Tests 页签），**不在本页这六张里**——**本页这六张图里没有 `Lower Limit` 列**，所以那一格本页没有核过。
- [[flow-sequence-editor]] — **原文指名**：这个视图显示的是**在 Flow Sequence Editor 里当前选中的那个 test suite** 的全部属性。**本页没读那一篇**，所以「选中是怎么传过来的」本页没有。
- [[testflow-tool]] / [[flow-data-editor]] / [[testflow-file]] — `extract/dangling.csv`（**2026-09-20 的读数**）里写着 `testflow-properties-view` 这个名字（该页记录本名字 **8 处引用、跨 7 个 stage**，其中就有这三个）。**本页没有读它们。**
- [[alphabetical-list-of-flags]] / [[flags-page]] — `Site Control` 与 `Flags` 两组里那些设置项**自己的定义在别处**：原文正文里把 `Site Match` / `Allow Parallel` / `Site Control` / `Size and Cycle` / `execution sequence` **五个名字逐个链到 `Alphabetical list of flags` 的锚点**。**本页没读那一篇**，也没读 [[flags-page]]。
- [[test-suite]] — 本页显示与编辑的对象。**原文没有链它**，本页只按「显示的是什么」链。
- [[spec-variable]] / [[spec-value]] / [[pin-string]]（**最后一个未建**）— 原文点名的三种参数类型；`SpecVariable` / `SpecValue` / `PinString` 那三个名字就是它们。**三篇本页都没读**，所以**它们各自是什么本页没有**。
- `Expanded Site Control window`（`02.08.04.27.02`，**未建**）— 原文两次点名它：`Size and Cycle` 的细节在那篇里；`OTHER` / `UNDEF` **不能在它里面设**。**本页没读那篇**，**也没有判它与 [[site-control-window]] 是不是同一个窗口**——**两个名字，本页不合并、也不说它们是同一个东西。**
- `Test Suites preference page`（`01.01.14.26`，**未建**）— `Automatic Validate Setups` 那个复选框在它里面。**本页没读**，所以那个复选框的完整语义本页没有。
- `Tests page`（`02.08.04.32.03.01.03`，**未建**）— [[mapping-testmethod]] 的「limit 的值」那一行**同时写了它与本页**。**本页没读它**，也没核对「limit 的**值**到底能不能在本页改」。
  （**2026-09-20 更正**：本页初版写「[[mapping-testmethod]] **与 [[mapping-testflow]]** 都写了」——
  **错了**。实测 `mapping-testflow` 里那一行 **0 次**、`mapping-testmethod` 里 3 次。
  **是写这页的 agent 在断线前自己查出来的，它没来得及改。**）
- **入边（`extract/edges.jsonl`，2026-09-17 的快照）**：链到本页出处文档的边 **40 条 / 22 篇**（**全部 `resolved`**；39 条 `inline` + 1 条 `toc`；**0 条落在代码跨度里**）。最密的几篇：`02.07.04.01.03_addParameter`（4）、`02.07.02.13.05_TestMethodParameterProxy`（4）、`02.07.04.02.16_TestMethodParameterProxy`（4）、`02.08.04.32.01.02.07.01_Alphabetical_list_of_flags`（4）、`02.08.04.27.02_Expanded_Site_Control_window`（3）、`02.07.02.02.02_How_to_create_a_universal_test_method_class`（1）。**这 22 篇的正文，本页一条没读**，只用了计数。
- **只写反引号、不写链接的名字**：`Properties view`（视图本身）、`Testflow Properties view` / `Test suite properties view` / `Testsuite view`（同一篇里的三个写法）、`Primaries`、`Timing` / `Level` / `Analog` / `Pattern` / `Context`、`Test Type`、`Test Method`、`Parameters`、`Limits`、`Flags`、`Site Control`、`Site Match`、`Allow Parallel`、`Size and Cycle`、`execution sequence`、`Results(Site in Focus)`、`Test Number`、`Test Level`、`Bypass`、`Set pass`、`Inconsistency Check`、`type filter text`、`Text Compare`、`Automatic Validate Setups`、模式取值 `PARALLEL` / `SERIAL` / `SEMIPARALLEL` / `OTHER` / `UNDEF`、参数类型名 `SpecVariable` / `SpecValue` / `PinString` ——**都不在 `extract/prose-allowlist.txt` 里**，按 §9.1 一律反引号。

## 版本

本文档**有** `## Functional changes` 段，**四条**，逐条照录，并写明它落在本页哪一处：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.0: Parameter property is displayed in Testsuite view.`
- `SmarTest 6.5.2: Properties view replaces Testsuite view.`
- `SmarTest 6.5.3: The function of choosing which items can be shown in the Properties view is removed.`

| 版本 | 原文条目 | 落在本页哪一处 |
|---|---|---|
| — | `Introduced before SmarTest 6.3.2` | **哨兵值，不是「6.3.2 的变更」**（`schema.md` §11.2②）——**照字面读会读成「6.3.2 新增了 Testflow Properties view」，那是错的** |
| **6.5.0** | `Parameter property is displayed in Testsuite view.` | **`Parameters` 这一项的来历**：本页正文那个「参数三态」小节、以及 `111394.png` / `355677.png` 上的 `Parameters` 行，**在 6.5.0 之前不存在** |
| **6.5.2** | `Properties view replaces Testsuite view.` | **本页的页名来历**：这个视图**以前叫 `Testsuite view`**——这解释了为什么 6.5.0 那条里写的是 `Testsuite view`（**本页照实并列两个名字，没有替它统一**） |
| **6.5.3** | `The function of choosing which items can be shown in the Properties view is removed.` | **本页正文没有任何一处接得住它**——**那个被删掉的功能长什么样、能选哪些项，语料未写**（图上倒是有一个 `type filter text` 框，但原文没说两者是同一件事，见「图证」） |

**四条里没有一条提到 `Site Control` 或 `Results(Site in Focus)`**——那两组是本页正文有、版本段没有的东西。

同批条目也收在 `wiki/versions/` 的 [[smartest-6.5.0]] / [[smartest-6.5.2]] / [[smartest-6.5.3]] 页里（**那三页不是本页建的**，这里只指路）；哨兵那一条见 [[smartest-6.3.2]]。

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.04_Testflow_Properties_view.md`
  （TDC `99279.htm`，6,587 字节 / 87 行）。
- **本篇没有重复投放**：全语料按 `source_topic` 查 `99279.htm`，**只有这一个文件**。
- **本页「语法 / 参数」节：一个字都没有**——**原文没有 `Syntax` / `Parameters` / `Example`
  这类段标记**（脚本的判据，见上面那一节的话）。**本页不是 API 页，所以这不是缺陷**：
  本页的参数与取值一律在正文的表里，**那些表是本页按原文排的转述 + 引文，不是脚本抽的参数表。**

### 本页读的图：**6 张，一张没漏**

`110713.png`、`355677.png`、`119756.png`、`111394.png`、`119669.png`、`119670.png`——
**本篇对 `raw/` 的图片引用正好 6 处，本页逐张读过**，读到什么、哪些字 grep 不到、哪些**不是**图证，
逐条见上面「图证」那一节。**图片路径 `../../../../raw/<n>.png` 从 md 往上四层正好是 `tdc-html/`，
文件在 `tdc-html/raw/`**（`schema.md` §11.4）。
**六张图里没有 `Lower Limit` 列**（[[mapping-testmethod]] 在「limit 的值」那一行标的那个图证来自另一篇文档的图）。

### 本页没做的

- **`## Related information` 六篇一篇没读**：`Using the site control`、`Expanded Site Control window`
  （`02.08.04.27.02`）、`Selecting the sites to run your test`（`02.08.04.27.04`）、
  `Editing a test suite in the Flow Data Editor`（`02.08.04.32.02.01.06`）、
  `Opening the Testflow Tool`（`02.08.04.32.02.01.01`）、`Alphabetical list of flags`（`02.08.04.32.01.02.07.01`）
  ——**所以「怎么打开这个视图」「那些 flag 各自什么含义」「`Size and Cycle` 的两个参数是什么」本页一个字没有。**
- **入边那 22 篇一篇没读**（`addParameter`、两篇 `TestMethodParameterProxy`、`Expanded_Site_Control_window`、
  `Alphabetical_list_of_flags`、`Adding_a_limit_in_the_Properties_view` 等）——
  **「别的文档怎么用这个视图」本页只有边数，没有内容。**
- **[[spec-variable]] / [[spec-value]] / [[pin-string]] 三篇没读**——三种参数类型各是什么，本页没有。
- **`Test Suites preference page` 没读**——`Automatic Validate Setups` 这个复选框的完整语义本页没有。
- **没有实跑。** 没有开过 Testflow Tool、没有选过 test suite、没有点过 `Inconsistency Check`、
  没有改过参数值。**六张图是「某一次具体配置」的截图，不是格式规范**（§11.4）；
  **`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[testflow]] 那页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 一处编码坏字：`鈥?`。** 原文 `## Test suite properties view` 那一段（第 38 行）：

> 「The test suite of different sites will be executed serially or semi-parallel in the order of the execution numbers that you specify in #1, #2, #鈥? .」

**那个 `鈥?` 属于 §11.2① 的第三族**：`鈥`（U+9225）是某个三字节 UTF-8 字符的头两个字节，
**第三个字节已经丢了、被换成一个 `?`**；`extract/encoding-map.csv` 把它归在
「**原字符在 U+2000–U+203F 之间**」那一类，**反解不出唯一的一个字**。
**本页正文没有引这一句**（它只在上面那张 `Site Control` 的表里以**转述**出现），
**坏字留在本条记录里**——§11.2 明令：不许替语料改，也不许假装没看见。

**② 一处错字：`excuted`。**

> 「If you do not check the option Allow Parallel, all the sites will be excuted in serial and the site control settings below will not work.」

**`excuted` 应为 `executed`。本页正文引了这一句，一处没动。**

**③ 一处句中的大写：`If you Do not change it`。**

> 「UNDEF is used by default when you create a test suite. If you Do not change it, the test suite of different sites will be executed serially or parallel according to whether it is implemented serially or parallel in the test method.」

**句中的 `Do` 不应大写。原文如此，引文里原样保留。**

**④ 一处「图与 `Note` 挤在同一行」：第 64 行。** 原文里那张图的方括号后面**直接接 `Note`**
（同一行、中间只有一个空格；其余五张图都独占一行）：

```
 ![Universal test method parameter display and modification](<../../../../raw/111394.png>) Note If a parameter value is …
```

**这是「两个块被压成一行」那一类毛病**（`connect` 那篇的 `state.Note`、`flush` 那篇的 `flush.You` 是同一族）。
**本页正文引那句 `Note` 时从 `Note` 起引，没有把图片路径抄进引文。**

**⑤ 同一篇里这个视图有三个名字。** 页名（H1）写 `Testflow Properties view`，
正文那一节的标题写 `## Test suite properties view`，版本记录写 `Testsuite view`——
**三种写法指同一个视图**。**本页照实并列三个，没有替它统一成一个。**

**⑥ 一处列表项括号前缺空格：`- Results(Site in Focus)`。** 原文那四个分组里最后一项写作
`Results(Site in Focus)`（**`Results` 与括号之间没有空格**）。**本页正文里那一行照原样写。**

**⑦ 第 18 行是一条「没有表头也没有分隔行」的管道行。** 那一行以空格开头、用 `|` 分成三格，
装着一句正文与一张图，**但整篇里没有它的表头行与 `---` 分隔行**，紧跟其后的是四个列表项
——**所以它在 markdown 里不是表，是一条被 `|` 包起来的正文。本页没有把那一行当表格抄。**

**⑧ 本篇没有 §11.2⑤ 那个整词替换**（`DC/DC power units` 实测 0 命中）——**查过、结果为零。**

`verified: doc-only`
