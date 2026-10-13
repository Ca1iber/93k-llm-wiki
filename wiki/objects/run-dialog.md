---
type: object
title: Running a testflow
layer: gui
stage: run
tags: [gui, run, run-dialog, testflow, test-suite, loop, response-emulator, debug, report-window]
related: [run, testflow, testflow-tool, testflow-file, flow-sequence-editor, test-suite, test-suites-page, site-control-window, report-window, flags-page, alphabetical-list-of-flags, hardware-response-emulator, special-test-suites, bin]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# Running a testflow

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,879 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.04_Measuring_the_test_time.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Measuring the test time）

A simple testflow comprises two test suites, cont and func, in this order. cont performs a continuity test and func a functional test. Both test suites only ask for a global PASS/FAIL result. The testflow is executed three times for two sites, resulting in six devices.

When the testflow is not optimized, the output of the debug mode 3 is shown as below.

 !`Debug 3 Output for unoptimized testflow`（raw: `../../../../raw/94560.png`）

Observe the following points in the listing:

- The `# of measure.` column in the `TESTFLOW INFORMATION` specifies the number of testflow repetitions. The number of measurements that is specified on the test suite level in the `seq setup` and `test suite exec.` rows specifies how often the respective test suites are executed. If the testflow is not optimized, this number is the number of testflow repetitions multiplied by the number of sites. The reason for this is that the two sites are processed serially in an unoptimized testflow, so that the test suite must be called twice in every testflow repetition.
- The time spent for executing connect and disconnect sequences is not explicitly specified in an unoptimized testflow. It is included in the test suite execution time. This is in contrast to the output for optimized testflows, as explained below. In both optimized and unoptimized testflows a test suite executes a connect or disconnect sequence only if this is necessary.
- The test suites are ordered as they are defined in the testflow file.
- The total time for running the testflow is greater than the sum of all total test suite times. There are several reasons for this. For example, the testflow can contain nodes which are not test suites, such as Assign Value nodes.

The second figure displays the results after the testflow has been optimized:

 !`Debug mode 3 output for optimized testflow`（raw: `../../../../raw/94561.png`）

Observe the following points in this listing:

- An additional line `set connect` is specified for the test suite `func`, but not for `cont`. This shows that a connect or disconnect sequence is executed for `func`, but not for `cont`. In fact, since the tester is in the DISCONNECTED state at the start of a testflow, and the continuity test of the first test suite must be executed in the DISCONNECTED state, it is not necessary to disconnect it again. But the functional test of func must be executed in the CONNECTED state, and therefore a connect sequence must be executed at the start of the second test suite.
- The benefit of downloading the setup data only once can be seen in the `seq setup` line of `cont`. The advantage of executing all sites in parallel can be seen in the `test suite execution` lines of both test suites. The parallel execution of the two sites is also reflected in the number of measurements for the `seq setup` and `test suite execution` rows (three instead of six).

<!-- 语法节 end -->

## 是什么

**Run dialog 是「跑 testflow」这件事的唯一配置面板。** 原文把它是什么、怎么打开放在同一段：

> 「The configuration is set in the Run dialog. To open this dialog, in the SmarTest Work Center,
> choose Run > Run configurations.」

**它上面挂着的是 Testflow tool 的执行侧**——原文第一句说的是 Testflow tool 能干什么，
**能干的那些事全在 Run dialog 里配**：

> 「The Testflow tool allows you to directly run the entire testflow or one or more individual
> test suites from it, which is useful when debugging the testflow, or when integrating new test
> suites into the testflow.」

**所以这一页讲三件事**：**左栏选「跑什么」**、**右栏配「怎么跑」**、**跑完怎么看结果**。

> **页名对不上，先说清楚**：本页的 slug 是 `run-dialog`，**但 title 和 source 文档都叫
> `Running a testflow`**（batch 里的页文件路径也是 `wiki/objects/run-dialog.md`）。
> **本页讲的是那个对话框**——原文的操作节 `### Step 2` 标题就是
> **`Step 2: Set the configuration of the testflow execution`**。
> **`Running a testflow` 这个名字覆盖的比对话框大一点**（还包含设 flag、怎么看结果）。

### 左栏：三个节点决定「跑什么」

| 左栏节点 | 跑什么 | 原文的入口 |
|---|---|---|
| **`Testflow (Full)`** | **整条 testflow** | 直接选它 |
| **`Testflow (Selection)`** | **选中的那几个 test suite** | 直接选它 |
| **`Testflow (User Defined)`** | **自己拼一条** | **右键 `New`** → 生成一个叫 `Testflow` 的节点 |

**`Testflow (User Defined)` 是唯一一个要先建的**：

> 「In the Run dialog, right-click Testflow (User Defined) in the left list and select New.
> A node named "Testflow" is created.」

### 右栏：三种模式**不是**同一组控件

**这是本页最值得先看的一张表。** 原文对每种模式各写了一小节，
**但没有把差别列出来**——下面这张表是**从原文三节对比出来的**（本页整理，不是原文的表）：

| 右栏的区 | `Testflow (Full)` | `Testflow (Selection)` | `Testflow (User Defined)` |
|---|---|---|---|
| **`Loop` 区** | ✅ 有 | ✅ **「与 full 相同」** | ✅ **「与 full 相同」** |
| **`Response Emulator` 区** | ✅ 有 | ✅ **「与 full 相同」** | ✅ **「与 full 相同」** |
| **`Site in Focus` 复选框** | ❌ **原文没提** | ✅ 有 | ✅ 有 |
| **`Enable 'single step' execution mode`** | ❌ **原文没提** | ✅ 有 | ✅ 有 |
| **`Name` 文本框**（默认 `Testflow`） | ❌ | ❌ | ✅ **独有** |
| **选哪条 testflow**（`Use current testflow` / `Select`） | ❌ | ❌ | ✅ **独有** |
| **`Scope` 区**（`Whole Flow` / `Testsuite(s)` / `Group(s)`） | ❌ | ❌ | ✅ **独有** |

> **「与 full 相同」这句原文抄了两遍**，写法几乎一样：
> `The configuration of the Loop area and the Response Emulator area is same as that of the full
> testflow execution.`
> **所以 `Loop` 与 `Response Emulator` 两区的细节只需读一遍**——
> 它们在三处是同一套。**这也意味着：本页只要讲清 full 的那一遍就够了。**

**`Site in Focus` 的语义原文写了两遍（Selection 与 User Defined 各一次），措辞一致**：

> 「Select the Site in Focus checkbox if you want to run the selected test suites on the focus site.
> If this checkbox is cleared, the selected test suites are executed on all active sites.」

**即：勾 = 只跑 focus site；不勾 = 所有 active site 都跑。**
（注意 Selection 那一节里还插了一句 `Note Refer to the paragraph When you run test suites with
their sub-branches further down in this topic.`——**它把「勾不勾」和「选得窄不窄」两件事绑在了一起**，
见下面的「窄选 vs 宽选」。）

### `Loop` 区：七个控件

**原文用一个二级列表把七个控件平铺出来**（本页按原文顺序整理）：

| # | 控件 | 原文说的效果 |
|---|---|---|
| 1 | **`Enable`** 复选框 | **循环的总开关**——不勾，下面六条都没意义 |
| 2 | **`Count`** + 一个整数 | **跑固定的次数**（`The testflow will be executed for the specified number of times.`） |
| 3 | **`Loop Indefinitely`** | **一直跑**，直到你**在 `Operation Control window` 里下 `Abort` 命令**，**或**满足下面 `Stop On Fail` / `Stop On Pass`（**前提是你勾了对应的框**） |
| 4 | **`Stop On Fail`** | **跑到出现一个 fail bin 为止**（`until a fail bin is reached`） |
| 5 | **`Stop On Pass`** | **跑到「某一轮里所有测试都过」为止**（`until there is a loop iteration in which all tests pass`） |
| 6 | **`Log Loop Number`** | **把轮次号打进 report window** |
| 7 | **`Pause between loops:`** + 毫秒数 | **每轮之间等一段时间**，单位 **`millisecond (ms)`** |

**第 2 与第 3 是互斥的两条路**：**要么跑固定次数（`Count`），要么跑不停（`Loop Indefinitely`）**。
**但原文没有明确写「选了一个就不能选另一个」**——它只说「如果你想 A 就选 A，如果你想 B 就点 B」。

**第 4、5 两条是 `Loop Indefinitely` 的刹车**，原文的括号里写清了依赖：
`if you activate the respective checkboxes`。

> **⚠️ 原文在这一段的末尾把一张截图并进了最后一个列表项**（逐字）：
> `- If you want to add a wait time between consecutive loop executions, select the Pause between
> loops: checkbox. In the text box next to it, specify a time interval in millisecond (ms).
> ![Run dialog for full testflow execution](<../../../../raw/119958.png>)`
> —— **图片语法直接接在句号后面**，本页按「图是独立的东西」处理。

### `Response Emulator` 区：本篇只给一句话

原文对这一区**只写了「在这里设选项」**，然后推到两篇专文：

> 「If you use Response Emulator, set the options in the Response Emulator area. For details, see
> [Preparing the Hardware Response files](…) and [Using hardware response files for execution](…)」

**所以 `Response Emulator` 区长什么样、有哪几个控件，本篇一个字都没有**（见 [[hardware-response-emulator]]）。

### `Testflow (User Defined)` 独有的三个控件组

| 控件组 | 原文说的 |
|---|---|
| **`Name`** | 给这套配置起个名，**默认就是 `Testflow`**，用来标识你这套配置 |
| **选哪条 testflow** | 勾 `Use current testflow` = 用当前的；**清掉勾再点 `Select`，可以从 `device_directory/testflow` 里挑另一条** |
| **`Scope` 区** | 三种：**`Whole Flow`**（整条当前 testflow）/ **`Testsuite(s)`**（点 `Select` 开 `Select Testsuites` 窗口，**选 test suite 并定它们的执行顺序**）/ **`Group(s)`**（点 `Select` 开 `Select Groups` 窗口，同样可选并定顺序） |

**`Scope` 是这一节里最「做出一条新 flow」的地方**：`Testsuite(s)` 与 `Group(s)`
**都允许你自己定执行顺序**（`define their execution order`）。

### 跑之前先设一个 flag

**`### Step 1` 不是打开对话框，是设 flag。** 原文：

> 「To output the result to the report window, set the debug_mode testflow flag to any value
> except off on the Flags page.」

**两个要点**：① **要看结果，`debug_mode` 必须不是 `off`**（`any value except off`——**原文没说设成几**）；
② 它是在 **[[flags-page]]** 上设的，不是在这个对话框里。

### 结果怎么看：四套颜色，两处地方

**结果输出在 [[report-window]]**（`The results of the testflow are displayed in the report window.`）。
颜色分两处：

**① `Flow Sequence Editor` 里的节点**（三色，直接对应结果）：

| 颜色 | 意思 |
|---|---|
| **绿** | passed test suite node |
| **红** | failed node |
| **黄** | **bypassed** node |

**② `Test Suites` 页的 `Result > Pass/Fail` 单元格**（**背景色与边框色是两套语义**，
这是最容易混的一处）：

| 形状 | 意思 |
|---|---|
| **绿背景** | Passed test suite |
| **红背景** | Failed test suite |
| **绿边框** | **The test suite set to pass**（被设成 pass） |
| **红边框** | **The test suite set to fail** |
| **黄边框** | **The test suite set to bypass** |

> **背景 = 实际结果，边框 = 被设成什么。** 原文用 `Green background` / `Green border`
> 这两个词把两套区分开，**但两套是并排列在同一张表里的**，读快了会当成一回事。

**一条时间上的规则**：

> 「If you edit the testflow after the execution, the borders of all test suites become dashed lines.」

**即：跑完之后再改 testflow，边框全部变虚线**——**这是一眼看出「结果已经和当前 flow 不同步」的标志。**

### 多 site 时的两种显示口径

| `Test Suites` 页设成 | 颜色按谁算 |
|---|---|
| **显示所有 site 的结果** | **`Test Suite Name` 单元格只有全部 site 都过才是绿的**；**只要有一个 site fail，就显示红边框** |
| **只显示 focus site 的结果** | **边框颜色按 focus site 的结果走**，passed 绿边框、failed 红边框，**与不在 focus 的 site 无关** |

### 「窄选」与「宽选」：选 test suite 的两种选法，行为完全不同

**这是本篇里最实用、也最容易忽略的一节。** 原文把它放在两个小标题下
（`When you run test suites without their sub-branches` / `When you run test suites with their sub-branches`）：

| | **不带子分支**（narrow selection） | **带子分支**（wide selection） |
|---|---|---|
| 执行依据 | **按当前状态跑**——`the execution of each test suite is affected by the result from the previously executed test suite` | **所选 test suite 被拼成一条「临时 testflow」**（`constituted as a temporary testflow`），**实际跑的是它** |
| 与 testflow 的关系 | 不是一条 flow | **`behaves like running a testflow`** |
| binning | 照常 | **`ignores binning`**（忽略分 bin） |
| pattern 加载 | **如果 testflow 选了 pattern master file，只加载用到的 pattern**（`only the used patterns are loaded`） | 原文没写 |
| 一条硬规则 | **任何一个 test suite 里发生 `If a sequencer SmarTest Work Center occurs in any test suite, that particular test suite is regarded as having failed.`**（⚠️ 这句原文如此，见「出处」） | 原文没写 |

**一句话记法**：**带子分支 = 当一条 testflow 跑（但不分 bin）；不带子分支 = 顺着当前状态往下跑。**

### 循环跑时的两条行为

原文 `### When you run a testflow or individual test suites in a loop` 一节：

| 问题 | 答案 |
|---|---|
| 和普通跑有什么不同？ | **几乎一样**：`the testflow is run in a similar way to a normal, non-looping execution`；**多 site 配置照用，每一轮都在所有 active site 上跑**；报告与分 bin 与普通测试相同 |
| **testflow 变量与 user flag 什么时候复位？** | **每一轮结束都*不*复位**——`they are only reset when the loop execution is first started, on the first loop iteration`。**即只在第一轮开始时复位一次** |
| **disconnect 什么时候发生？** | **跑 testflow 循环：每一轮结束都 disconnect。** 跑单个 test suite 循环：**不 disconnect**，**除非你在 test method 里自己写了 disconnect** |

**最后一条是原文单独用 `Note` 标出来的**，也是循环跑里最容易出问题的地方。

### 怎么停下来：四个按钮 + 一条「干净中止」流程

原文 `## What to do next` 一节全在讲停止。**四个按钮的功能差别很大**：

| 按钮 | 原文说的 |
|---|---|
| **`ABORT`** | **在当前 test suite 结束时**立刻中止，**并且停掉循环** |
| **`RESET`** | 同样在**当前 test suite 结束时**中止、**停掉循环**，**并且把软件退回初始状态、复位测试机里已下载的设置** |
| **`ABORT TESTFLOW`** | **在 test suite 之间**停下设备测试；**但循环不停**——`the next run is immediately started if the looped execution is enabled` |
| **`PAUSE`** | **切换键**。点它**置 PAUSE flag**；**application model 在一次 device test 执行完之后立刻读这个 flag** |

> **`ABORT TESTFLOW` 与 `ABORT` 的差别是这一页最要紧的一条**：
> **`ABORT TESTFLOW` 不停循环，而 `ABORT` / `RESET` 停。**
> **循环跑的时候按错，表现就是「停了又自己跑起来」。**

**原文另外给了一条「干净中止循环」的流程**（用 `Note` 引出前提）：

> 「Some devices or the needs of recording data require that looped test flows are cleanly aborted:
> The aborted loop must run through to the end of the current execution and then stop.」

| 步骤 | 动作 |
|---|---|
| 1 | **点 `PAUSE`，等到本次执行结束** |
| 2 | **点 `ABORT`** |
| 3 | **回到 PAUSE 对话框，按 `Quit`** |

> **⚠️ 原文紧接着写：`Note The Break button (stop sign) does not abort the loop execution.`**
> **——`Break` 按钮（那个停止标志）不能中止循环。** 这是这条流程存在的原因。

## 典型用法

**原文有完整的操作节**：`## Before you begin` + `### Step 1` / `### Step 2` / `### Step 3` + `## Results`。

### 前提

> 「Make sure the testflow has been loaded.」

**就这一句。** 原文没有说怎么加载（那在 [[testflow-tool]] / [[flow-sequence-editor]] 那边）。

### 三步

**Step 1 — 设 flag**：到 [[flags-page]] 把 **`debug_mode`** 设成 **`off` 以外的任何值**（否则结果不进 report window）。

**Step 2 — 在 Run dialog 里配**：`Run > Run configurations` →
左栏选 `Testflow (Full)` / `Testflow (Selection)` / `Testflow (User Defined)` 之一 →
右栏按上面那张对照表配（`Loop` 区、`Response Emulator` 区，按需再配 `Site in Focus` /
`single step` / 用户自定义那三项）。

**Step 3 — 跑**：

> 「After you have set the configuration in the Run dialog, keep the dialog open, click Run.」

**注意 `keep the dialog open`**——**按 `Run` 的那个瞬间对话框要开着。**

### 对话框关掉之后照样能跑（两条右键路径）

| 想跑什么 | 怎么做 |
|---|---|
| **整条当前 testflow** | **在 `Flow Sequence Editor` 上右键 → `Run Testflow`** |
| **选中的那几个 test suite** | **在 `Flow Sequence Editor` 上右键 → `Run Selected`** |

**这两条是 `Testflow (Full)` 与 `Testflow (Selection)` 的快捷方式**——
**绕开了 Run dialog**。**原文没写用户自定义的那条有没有对应的右键路径。**

### 什么时候用哪种（本页按原文覆盖范围整理）

| 场景 | 选谁 |
|---|---|
| 调试整条 flow / 刚把新 test suite 集成进来 | **`Testflow (Full)`**（原文第一句说的 `useful when debugging … or when integrating new test suites`） |
| 只想跑几个 test suite | **`Testflow (Selection)`**（再决定勾不勾 `Site in Focus`） |
| 要换一条 testflow / 只跑某些 group / 自己定 test suite 顺序 | **`Testflow (User Defined)`** 的 `Scope` 区 |
| 要反复跑到失败或全过 | **`Loop` 区** + `Stop On Fail` / `Stop On Pass` |
| 离线调试、要喂假数据 | **`Response Emulator` 区**（细节见 [[hardware-response-emulator]]） |

**下一步（原文 `## What to do next`）**：停下来用 `ABORT` / `RESET` / `ABORT TESTFLOW` / `PAUSE`
（见上）。

## 和谁有关

- [[run]] — **本页 `stage: run` 的理由**：它是「执行」那一段的配置面板。
- [[testflow]] — **本页跑的宾语**；原文 `Before you begin` 只要求「已经加载」。
- [[testflow-tool]] — **原文第一句的主语就是它**（`The Testflow tool allows you to directly run …`）。
  **本页是它的执行侧配置**；它自己的结构（Flow Data Editor / Flow Sequence Editor / Test Suites page）在它那一页。
- [[flow-sequence-editor]] — **关掉对话框之后的两条右键路径都在它上面**（`Run Testflow` / `Run Selected`）；
  跑完的**节点三色**也显示在它里面。
- [[test-suite]] — `Testflow (Selection)` 选的、`Scope: Testsuite(s)` 排的、循环跑时 disconnect 行为不同的，
  **都是它**；**「窄选 vs 宽选」那一节讲的就是「选 test suite 时带不带子分支」**。
- [[test-suites-page]] — **结果颜色第二处**（`Result > Pass/Fail` 单元格的背景色与边框色）。
- [[report-window]] — **结果的第一输出处**；也是 `Log Loop Number` 打轮次号的地方。
- [[flags-page]] — **`### Step 1` 就是在这里设 `debug_mode`**。
- [[alphabetical-list-of-flags]] — 《Running a testflow》原文把它列在 `Related information` 第一条；
  **`debug_mode` 这个 flag 自己的定义在那一边。**
- [[hardware-response-emulator]] — **`Response Emulator` 区背后的那套东西**；
  本篇只写「在这一区设选项」并把细节推给了两篇专文。
- [[special-test-suites]] 与 [[bin]] — **原文 `Related information` 里的两条**：
  `Special test suites` 与 `Binning`。**本页正文里出现过 `bin` 这个词两次**
  （`Stop On Fail` 的 `until a fail bin is reached`、宽选的 `ignores binning`），
  **但 bin 是什么、怎么分，本页不讲。**
- [[site-control-window]] — **本页出现的词是 `focus site` 与 `Site in Focus` 复选框**；
  **它和 [[site-control-window]] 是什么关系，本篇没说**，本页不替它连。
- **清单外、本页不链（用反引号写名字）**：`Loop configuration settings`、
  `Single step testflow debugging`、`Debugging a testflow`、`Narrow selection and wide selection`、
  `Controlling a Production Run`、`Operator Control window`、`Operation Control window`、
  `Select Testsuites`、`Select Groups`、`Pattern master file`
  —— **这些名字都不在 `prose-allowlist.txt` 里**。

## 版本

原文 `## Functional changes` 段五条（**按原文顺序**）：

| 条目 | 读法 |
|---|---|
| `Introduced before SmarTest 6.3.2` | **哨兵值，不是「6.3.2 的变更」**——意思是「**在本文档集覆盖范围开始之前就已经有了**」（§11.2 ②）。**不是一条真变更。** |
| `SmarTest 6.5.3: The procedure of running a testflow is changed.` | **6.5.3 改了流程**——**但原文没有说改成什么**。**本页不能写「改了哪一步」。** |
| `SmarTest 7.1.0: Single step execution mode for debugging testflows introduced` | **`single step` 那个复选框是 7.1.0 才有的**——**它解释了为什么正文里 `Enable 'single step' execution mode` 只出现在 `Selection` 与 `User Defined` 两节**（**推断**：原文这两节写于 7.1.0 之后；**关于 Full 那一节本篇没有类似句子，原文也没说 Full 有没有这个选项**）。 |
| `SmarTest 7.1.2: Stop on Fail now stops when any test suite in a sequence has an overall fail result and Stop on Pass now stops when all of the test suites in a sequence pass.` | **这一条把两个复选框的语义收紧了**：**7.1.2 之前不是这个判据**。**注意原文这里写的是 `Stop on Fail` / `Stop on Pass`（小写 `on`），而正文里写的是 `Stop On Fail` / `Stop On Pass`（大写 `On`）**——逐字如此，本页不统一（见「出处」⚠️ ④） |
| `SmarTest 7.4.1: For Testflow (Full), Testflow (Selection) and Testflow (User Defined), a new option "Pause between loops" allows user to specify a wait time between consecutive executions.` | **`Pause between loops` 是 7.4.1 加的三个模式通用选项**——**这是本篇唯一一条点名了三个模式全体的变更** |

**一条对不上、本页不替它调和的地方**：版本段 `SmarTest 7.1.2` 那条用的是
**`Stop on Fail` / `Stop on Pass`**，正文用的是 **`Stop On Fail` / `Stop On Pass`**。
**原文两处不一致**，本页**照原样分别引用**。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md`（TDC `98810.htm`）

**本页没做的**：

- **五个子主题一篇没读**：`02.08.04.32.02.03.01_Loop_configuration_settings`、
  `02.08.04.32.02.03.02_Using_the_Overon_feature_while_running_a_testflow`、
  `02.08.04.32.02.03.03_Checking_the_execution_flow`、
  `02.08.04.32.02.03.04_Measuring_the_test_time`、
  `02.08.04.32.02.03.05_Adding_user_defined_testflows_to_the_Run_menu`。
  **所以 `Loop` 区七个控件的深入语义（尤其是 `Overon`）、执行流的检查、
  以及「怎么把自定义 testflow 加到 Run 菜单」，本页都没有。**
  **本页的 `Loop` 一节只有原文在 `Step 2` 里顺带给的那七条。**
- **`Related information` 的七篇一篇没读**：`Loop configuration settings`、
  `Alphabetical list of flags`、`Debugging a testflow`、`Narrow selection and wide selection`、
  `Binning`、`Controlling a Production Run`、`Special test suites`。
  **本页对「窄选/宽选」只有原文那两段；两个术语的正式定义在没读的那一篇里。**
- **四张图一张没看**：`119958.png`（full testflow 的 Run dialog）、
  `119959.png`（selection 的）、`119963.png`（user defined 的）、`151602.png`（Operator Control window）。
  **本页没有任何来自图的结论**——**对话框的左右分栏长什么样、控件怎么排，都不知道**。
  **本页那张「三种模式对照表」是从原文文字里对出来的，不是从图里看的。**
- **`## 语法 / 参数` 节的两段 Example 不是本篇 source 的内容**：
  它们逐字来自子主题 `02.08.04.32.02.03.04_Measuring_the_test_time.md`（**本页没读**），
  讲的是 `debug mode 3` 输出里的 `# of measure.` 那一列怎么读。
  **本页正文一个字都没有用它**——**这一页讲的是对话框，不是 debug mode 3 的输出。**
- **本页没在真机上跑过 testflow**（`verified: doc-only`）。
  **所有结果颜色、按钮行为、循环行为都是文档事实，不是本机事实。**

> **一条口径差异，先记下来**：批次的提示里把这个对话框的菜单路径写成
> `Run > Open Run Dialog`，**而原文写的是 `Run > Run configurations`**
> （逐字：`in the SmarTest Work Center, choose Run > Run configurations`）。
> **本页以原文为准。** 原文里同一个对话框还有第二个名字：
> `In the Run configurations dialog, select Testflow (Full) …`——
> **「Run dialog」与「Run configurations dialog」在原文里混用。**

> ⚠️ **本篇的五处语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **`If a sequencer SmarTest Work Center occurs in any test suite, that particular test suite is
> regarded as having failed.`** —— **`a sequencer SmarTest Work Center` 不成话**：
> 「SmarTest Work Center」是一个产品界面的名字，**放在 `a sequencer` 后面接 `occurs` 讲不通**。
> **本页照原样引，不猜原文是什么。** —— **⚠️ 按 §11.2 ⑤ 的口径，这类「看起来完全正常、
> 其实错」的损坏是存在的，而且它坏在上游 `.htm` 里、救不回来。本页只指出它讲不通，不判定原文。**
>
> ② **三个名字指同一个窗口**：`Operation Control window`（`Loop Indefinitely` 那一句）、
> `Operator Control window`（`## What to do next` 的标题句与按钮说明）、
> `Operation Control screen`（`PAUSE` 那一条）。**逐字分别是**：
> `until you give an Abort command (in the Operation Control window)`、
> `To stop the testflow execution, click ABORT in the Operator Control window.`、
> `simply click the PAUSE toggle button in the Operation Control screen`。
> **本页不替它们统一。**
>
> ③ **`Note` 与被注的句子之间没有分隔**（三处，逐字）：
> `…are executed on all active sites.Note Refer to the paragraph…`、
> `…press the Quit button.Note The Break button (stop sign)…`、
> 以及表格单元格里的 `| Note Some devices or the needs of recording data require that looped test
> flows are cleanly aborted:…`。**`Note` 直接粘在句号后面或管道符后面。**
>
> ④ **按钮/标志的大小写在同一篇里不一致**：
> `Stop On Fail`（正文）对 `Stop on Fail`（版本段）；`ABORT`（按钮）对 `Abort command`（正文里那句
> `until you give an Abort command`）。**本页两处都照原样写。**
>
> ⑤ **两张表在语料里被压平成「管道行 + 空行」**：`## Results` 那四行颜色表
> （逐字形状是 ` |` / `Green background` / ` |` / `Passed test suite` / ` |`）、
> 以及 Operator Control 那张（`| ![Operator Control window in engineering mode](…) |`）。
> **本页上面那两张颜色表是按「颜色 → 释义」的相邻关系复原的，不是原文的排版。**

`verified: doc-only`
