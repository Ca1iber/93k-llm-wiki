---
type: object
title: Hardware Response Emulator
layer: gui
stage: run
tags: [hardware-response-emulator, hwre, offline-debug, emulation, import-mode, store-mode, run]
related: [hardware-response-file, offline-result-emulation, run-dialog, testflow, test-suite, testmethod]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Hardware Response Emulator

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **726 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.03_Hardware_response_files.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Using hardware response files for execution）

When the hardware response file is not found for the execution of a test suite with the pass/fail result, the Hardware Response Emulator Pass/Fail Dialog window for the "Import" mode opens.

 !`Emulator dialog for setting pass/fail state for each testsuite`（raw: `../../../../agent-html/21635.png`）

### Example（取自子主题 Hardware response files）

The hardware response file `TS1;Analog.DGT("a_out").getWaveform(1);1;1` is related to the first execution of the `Analog.DGT("a_out").getWaveform()` API called on site 1 in the method program in the `TS1` test suite. Note that a hardware response file name contains a default input value even if the value was not set in the related API. This is the reason why the file name contains `Waveform(1)` even if "1" is not set for the API.

<!-- 语法节 end -->

## 是什么

**HWRE（Hardware Response Emulator，硬件响应仿真器）是 SmarTest 的一个后台工具：
离线调 testflow / test suite 时，它把「本来该由硬件给出的数据」按准备好的内容喂回去。**
原文逐字（**它明确是为了解决两个问题而存在的**）：

> 「When you debug a testflow or test suite offline, you may encounter the following two problems:」

> 「- Random and insignificant data is returned to the test method APIs.」

> 「- You cannot control the pass/fail results of each test suite easily.」

**两个问题**（逐字）：**① 回给 test method API 的是随机且无意义的数据；② 每个 test suite 的
pass/fail 结果不好控制。** 原文下一句就是它的定位：

> 「SmarTest provides a tool, Hardware Response Emulator (HWRE), to resolve the above problems.」

**缩写 `HWRE` 是原文自己给的**（`Hardware Response Emulator (HWRE)`），不是本页起的。

### 它做什么：后台、在「恰当的点」把预置数据喂回去

原文逐字：

> 「The HWRE runs in the background and returns already prepared data such as analog waveform data,
> measurement values, pass/fail results, and so on at appropriate points in the test.」

**三件事**：**跑在后台**（`runs in the background`）→
**喂的是「已经准备好的数据」**（`already prepared data`）→
**在测试里的恰当位置**（`at appropriate points in the test`）。

**能喂哪几类数据**（原文举的例）：`analog waveform data`、`measurement values`、`pass/fail results`，
原文用 `and so on` 收尾——**所以这份清单不是封闭清单。**

**它解决的是什么问题、怎么解决**，原文逐字：

> 「The HWRE helps you to debug your test method program using actual measurement data such as
> waveform data captured by digitizers. This tool also helps you to check the execution flow of the
> testflow easily by setting the pass/fail state for each test suite.」

| 原文那半句 | 用途 |
|---|---|
| `debug your test method program using actual measurement data such as waveform data captured by digitizers` | **用真实测量数据**（比如 digitizer 采到的波形）来调 test method 程序 |
| `check the execution flow of the testflow easily by setting the pass/fail state for each test suite` | **给每个 test suite 设 pass/fail 状态**，从而轻松查 testflow 的执行流 |

**同一个工具的两个用途，一个偏「数据」、一个偏「流程」。**

### 两个模式：Import 与 Store

原文用两个 `##` 节给它们下定义，**一节一句**：

| 模式 | 原文定义（逐字） | 数据往哪个方向走 |
|---|---|---|
| **`## Import mode`** | `In this mode, the emulator imports the data stored in a hardware response file and returns the data to the testflow or test method API during execution.` | **文件 → 测试**（`imports the data stored in a hardware response file and returns`） |
| **`## Store mode`** | `In this mode, the emulator creates the hardware response files from the measurement data during online execution or from user-provided data during offline execution.` | **测试 → 文件**（`creates the hardware response files from the measurement data`） |

**注意两个模式的适用范围不一样**：

- **Import mode 的定义里只提「执行时」**（`during execution`），**没有提在线还是离线**——
  **但从第一段那句 `When you debug a testflow or test suite offline` 看，它的主场是离线**（**这是（推断）**：
  依据是这篇开头把两个问题限定在 `offline` 下、而 HWRE 是为解决那两个问题而给的；
  **原文没有一句写「Import mode 只能离线用」。**）
- **Store mode 的定义里明写了两种来源**：`during online execution` 与
  `during offline execution` —— **所以 Store mode 在线、离线都覆盖。**

### 两个「触发点」（**图证给出了它们具体是哪儿**）

原文在 Store mode 里两次写到触发点，措辞一样：

> 「When running a testflow or test suite in online mode, the emulator automatically stores the test
> results (pass/fail) and hardware response data in different hardware response files when the
> execution reaches the end of the test suite or the test method API for retrieving hardware
> response data.」

> 「When running a testflow or test suite offline, the emulator opens a prompt window when the
> execution reaches the end of the test suite or the test method API for retrieving hardware
> response data.」

**两句里那个 `when` 从句**（`when the execution reaches` 那半句）**逐字相同**，
**只有主句不同**——在线那句接 `the emulator automatically stores`，离线那句接 `the emulator opens a prompt window`。

**即两个点**：**① test suite 的末尾**；**② 「取硬件响应数据的那个 test method API」**。

**图证把这句抽象的话画成了两处**（`raw/20979.png`、`raw/30579.png`、`raw/20980.gif` 三张流程图
的结构一致，**图里的字搜不到**）：

| 图里的元素 | 对应原文哪句 |
|---|---|
| 一条蓝带 `Test Execution`，上面套一个绿框 `Testsuite (Test Method Program)` | 原文的 `When running a testflow or test suite in online mode` / `When running a testflow or test suite offline` |
| 蓝带上两个黑点，各引出一个气泡：`API for retrieving hardware response` 与 `Judge pass/fail of testsuite` | **就是原文那两个触发点**——**第二个点在图里就是「判 test suite 的 pass/fail」** |
| 一条橙带 `Emulator (Import mode)` / `(Store mode)`，与蓝带平行 | `The HWRE runs in the background` |
| 橙带下面两个 `File` 圆柱，分列两处 | **数据分成两类文件**（见下） |
| 左侧一台测试机图案，虚线箭头标 `Not Access` | **离线时硬件不被访问**——**原文用文字说的是 `offline`，图里画的是 `Not Access`** |

**两个关键点，图证与原文对得上：**

- **两个触发点必须分开看**：一个是「test suite 末尾」（**判 pass/fail**），
  另一个是「取硬件响应数据的那个 API」（**给测量数据**）。
  **图里也正是两个点、两条独立的箭头链。**
- **Store mode 在线时，两个点各存一个文件、是两类不同的文件。** 原文逐字：
  `the emulator automatically stores the test results (pass/fail) and hardware response data in
  different hardware response files` ——**`in different hardware response files` 是原文写的，
  图证里也是两个分开的 `File` 圆柱**（一个标 `Store hardware response data`、
  一个标 `Store test result data (pass/fail)`）。

### Store mode 离线时：弹一个窗口让你填

原文逐字：

> 「When running a testflow or test suite offline, the emulator opens a prompt window when the
> execution reaches the end of the test suite or the test method API for retrieving hardware
> response data. In the window, you can specify the desired data as the virtual test result
> (pass/fail) or hardware response. You can also use the data files as virtual data in online mode.」

| 原文那半句 | 要点 |
|---|---|
| `the emulator opens a prompt window` | **它不自动存，而是弹窗**——**在线是自动存，离线是弹窗**，这是两个模式在 Store 里的唯一分岔 |
| `you can specify the desired data as the virtual test result (pass/fail) or hardware response` | 你在窗口里指定「虚拟结果」——**两类都指得出**（pass/fail 与硬件响应） |
| `You can also use the data files as virtual data in online mode.` | **这句在一段讲离线的段落里突然提在线模式**（见 `## 出处` ⚠️④） |

**图证**（`raw/20980.gif`，alt 是 `Storing User-Programmed Data using Emulator`）：
橙带标 `Emulator (Store mode)`，两个触发点各引出
`Open` → `Return Data` → 一个 **`Prompt Window`** 方框 → `Store` → 一个 `File` 圆柱；
而两个 `Prompt Window` 都由同一个 **`User Input`** 框供数据。**硬件那一侧仍然是 `Not Access` 虚线。**

**`Import mode` 那个对话框也有图**（`raw/21635.png`，**引自语法节**，见 `## 出处` ⑥）：
窗口标题 `Hardware Response Emulator  Pass/Fail Dialog`；输入框上方写着
`Testsuite; MAPI; call#; site#`，框里预填的是 `Functional_test;GET_FUNCTIONAL_RESULT();2;1`；
下面两个单选 `Pass` / `Fail`；再下面是 `Ok`、一个 `store HW Response Data` 复选框、
`Bypass Emulator` 与 `Emulator Off` 两个按钮。
**语法节抽到的那句说明了这个窗口什么时候开**——逐字（**在语法节里，本页不重复**）：
`When the hardware response file is not found for the execution of a test suite with the pass/fail
result, the Hardware Response Emulator Pass/Fail Dialog window for the "Import" mode opens.`

**即：Import mode 下找不到对应的 hardware response file 时，这个 pass/fail 对话框才开。**
**图里那两个按钮 `Bypass Emulator` / `Emulator Off`、那个复选框 `store HW Response Data`
在正文里一个字都没有**——**本页只能照图说它们在，说不出它们各自做什么。**

### 这篇的父子里结构

原文把自己那棵子树的入口列成了 `#### Subtopics`，**四条**（**其中第三条在本 wiki 里是一页**）：

| 子主题（逐字） | 本 wiki |
|---|---|
| `Preparing Hardware Response files`（raw: `02.08.04.32.02.06.01_Preparing_Hardware_Response_files.md`） | **未建** |
| `Using hardware response files for execution`（raw: `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.md`） | **未建** |
| `Hardware response files`（raw: `02.08.04.32.02.06.03_Hardware_response_files.md`） | [[hardware-response-file]] |
| `Supported test suites and test method APIs`（raw: `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.04_Supported_test_suites_and_test_method_APIs.md`） | **未建** |

**「哪几个 test suite / test method API 被支持」这件事，这篇正文一个字没有**——
**它整个在第四个子主题里**（**本页没读那篇**）。

### 这篇没有写的（一律「语料未写」）

原文**没有** `## Syntax`、`## Parameters`、`## Procedure`、`## Before you begin`、`## Errors`——
**这也是它语法节里只有两段 Example 的原因**（那两段还是从子主题借的，见页首语法节自己的声明）。
具体缺的：

| 问题 | 原文的状态 |
|---|---|
| 两个模式在哪选、怎么切 | **未写**（正文只定义了两个模式，没说入口） |
| HWRE 在 GUI 里的入口在哪 | **未写**（全文一次都没提 Run dialog / 菜单） |
| 怎么启动 / 停止 HWRE | **未写**（图里有 `Emulator Off` 按钮，**正文没有它的任何说明**） |
| hardware response file 放在哪个目录、叫什么 | **未写**（**子主题 `.03` 与语法节第二段 Example 提到文件名格式，正文没有**） |
| 哪些 test suite / API 支持 | **未写**（在子主题 `.04`） |
| 权限、限制、报错 | **一段都没有** |

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`。** 能落成动作的，只有从两个模式的定义
和那段 Store mode 描述里读出来的顺序。**下面每一步都标了依据；凡是原文没说的，本页不补。**

### 离线调试（用 Import mode：拿现成数据喂回去）

| 步骤 | 依据（原文） |
|---|---|
| **1. 先有 hardware response file** | `the data stored in a hardware response file` ——**文件怎么来，正文没说**（在子主题） |
| **2. 离线跑 testflow / test suite** | `When you debug a testflow or test suite offline` |
| **3. 执行到那两个点时，emulator 把文件里的数据回给 testflow 或 test method API** | `imports the data stored in a hardware response file and returns the data to the testflow or test method API during execution` |
| **4. 要是那个 suite 的 pass/fail 文件没找到** | **会开 `Pass/Fail Dialog`**（语法节那句 + 图证 `21635.png`） |

**（推断）第 4 步的窗口是「兜底」而不是「必经」**——依据是那句
`When the hardware response file is not found for the execution of a test suite with the pass/fail
result,` + `the Hardware Response Emulator Pass/Fail Dialog window for the "Import" mode opens.`
（**两句原文里是同一句，本页断开引以免加省略号**）——**条件是 `is not found`；
原文没有写「文件在的时候就静静过去」这句，所以这是推断。**

### 在线跑（用 Store mode：把真实数据存下来）

| 步骤 | 依据（原文） |
|---|---|
| **1. 在线跑 testflow / test suite** | `When running a testflow or test suite in online mode` |
| **2. 不用手动点存** | `the emulator **automatically** stores` ——**原文写的是自动** |
| **3. 到那两个触发点时，结果被存进两类不同的文件** | `stores the test results (pass/fail) and hardware response data in different hardware response files` |
| **4. 存下来的文件就是下次离线跑（Import mode）的输入** | **（推断）**：Import mode 的定义说它 `imports the data stored in a hardware response file`，而 Store mode 说它 `creates the hardware response files` **——同一个东西，一个写一个读** |

**第 4 步是（推断），依据是「`creates` 与 `imports` 的对象同名」这层文字对应；
原文没有一句写「Store 存的文件给 Import 用」。** 不过 Store mode 那段另有一句
`You can also use the data files as virtual data in online mode.` ——**它至少把「存下来的文件还能再用」
写出来了，但说的是 online mode**（⚠️ 见 `## 出处` ④）。

### 在线跑但要自己指定数据（Store mode 的离线分支）

| 步骤 | 依据（原文） |
|---|---|
| **1. 离线跑 testflow / test suite** | `When running a testflow or test suite offline` |
| **2. 执行到那两个点时，emulator 开一个 prompt window** | `the emulator opens a prompt window when the execution reaches the end of the test suite or the test method API for retrieving hardware response data` |
| **3. 在窗口里指定想用的数据**（作为虚拟的 pass/fail 结果，或作为硬件响应） | `you can specify the desired data as the virtual test result (pass/fail) or hardware response` |
| **4. 数据被存成文件** | 图证（`20980.gif`）：`Prompt Window` → `Store` → `File`；**正文没有写这一步，是图证补的** |

**三条（推断），依据都只是原文那一句：**

- **「同一个触发点，在线自动存、离线弹窗」**——依据是两段都用同一句
  `when the execution reaches the end of the test suite or the test method API for retrieving
  hardware response data`，而一段接 `automatically stores`、一段接 `opens a prompt window`。
  **原文没有把这句对比写出来，是本页并列两段得出的。**
- **窗口是「每个触发点各弹一次」**——图证里是两个 `Prompt Window`（对应两个点），
  **而原文用的是单数 `a prompt window`。两句并列，本页不判。**
- **「pass/fail 那条链」与「硬件响应数据那条链」是两条独立的链**——依据是原文的
  `in different hardware response files` 与图证里两个分开的 `File` 圆柱。
  **原文没写这两条会不会互相影响。**

## 和谁有关

- [[hardware-response-file]] — **本页的子主题之一，也是它的数据载体**。原文 `#### Subtopics` 第三条
  逐字是 `Hardware response files`，指向 `02.08.04.32.02.06.03_Hardware_response_files.md`。
  **两个模式都绕着它转**：Import 读它、Store 写它。
  **文件的格式、命名、放哪，都在那一页**——**本页只有「有这么一个文件」这件事**，
  唯一的细节来自本页语法节第二段 Example（那是从子主题抄的，**本页没读那篇**）。
- [[offline-result-emulation]] — **原文 `Related information` 第三个目标**，原文逐字只给了这个名字
  （`Offline Result Emulation`），**没有一句话说它和 HWRE 是什么关系**。
  **⚠️ 两件事不是同一个东西**：`Offline Result Emulation` 在原文里挂的是
  `02.07_Test_Method_Reference/02.07.12_Offline_Result_Emulation.md`（**Test Method Reference 章**），
  **而本页是 setup / result tools 章的一篇**；而且它列在 `Related information` 里、
  **不在 `Subtopics` 里**——**所以它不在本页的父子树内。**
  **本页没读它，不知道它做什么。凭名字把两者合并是错的。**
- `Checking the execution flow`（**未建**，raw: `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.03_Checking_the_execution_flow.md`）
  — **原文 `Related information` 第二个目标**。**这一条和本页正文有实质呼应**：
  原文说 HWRE 能 `check the execution flow of the testflow easily by setting the pass/fail state
  for each test suite` ——**这个用途与那一篇的标题是同一件事。**
  **但那一篇怎么查、看到什么，本页一个字都没有。**
- `Using hardware response files for execution`（**未建**，raw: `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.md`）
  — **本页第二个子主题，同时也是本页 `Related information` 的第一个目标**。
  **它被引了两次**（父子 + 相关），**说明「怎么用文件跑」这件事主要在它那儿，不在这儿。**
  **本页的语法节第一段 Example 就是从它那儿借的**（**本页没读那篇**）。
- [[run-dialog]] — **（推断）HWRE 在 GUI 里的入口所在的那一页**。依据两条：
  它自己的 raw 是 `02.08.04.32.02.03_Running_a_testflow.md`，**与本页同挂在 `02.08.04.32.02` 下**；
  而**本页正文一次都没说 HWRE 在界面上从哪开**。**⚠️ 这一篇里没有一个字提到 Run dialog，
  所以这是推断，不是文档事实。本页没读 [[run-dialog]]。**
- [[testflow]] / [[test-suite]] — **被调试的对象**。原文明写 HWRE 是为了
  `debug a testflow or test suite offline`，而且两个触发点之一就是
  `the end of the test suite`。**本页只有「HWRE 会在这两个对象上挂钩子」这层关系；
  testflow 怎么组织、test suite 是什么，在那两页。**
- [[testmethod]] — **数据的接收方**。原文说那两个问题之一是
  `Random and insignificant data is returned to the test method APIs.`，
  而 HWRE 把数据 `returns the data to the testflow or test method API`。
  **所以 test method API 是这条链的另一端。** **本页没有那页的任何事实。**
- `Preparing Hardware Response files`（**未建**，raw: `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01_Preparing_Hardware_Response_files.md`）
  — **本页第一个子主题**。**「文件怎么准备」这一步整个在它那儿**——
  **本页给不出任何一条「怎么造出一个 hardware response file」的做法。**
- `Supported test suites and test method APIs`（**未建**，raw: `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.04_Supported_test_suites_and_test_method_APIs.md`）
  — **本页第四个子主题**。**「哪些 test suite / API 被支持」是它的标题**，
  **而本页正文一个字都没提**——**想知道能不能用，必须去那一篇。**

## 版本

本文档**有** `## Functional changes` 段，**只有一条**（逐字）：

- `Introduced before SmarTest 6.3.2`

**这一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 HWRE 本身成立于哪个版本，这份语料里没有。**

**这一篇的版本段比同类的还薄，有两条值得写明：**

- **两个模式（`Import mode` / `Store mode`）在版本段里一条都没有。**
  正文把它们当作既成事实写，**哪个版本引入的、有没有先后，语料未写。**
- **`Pass/Fail Dialog`、`Bypass Emulator`、`Emulator Off`、`store HW Response Data` 这些界面元素
  在版本段里也没有一条**（**其中后三个在正文里根本没有出现过**，只有图证）。
  **它们是不是某个版本加的，语料里没有。**

**与 wiki 面向版本的关系**：本 wiki 目标是 **SmarTest 7.10.3**，
而这一篇的版本段**连一条 7.x 的条目都没有**——
**所以本页只能确认「6.3.2 之前就有 HWRE」；它在 7.10.3 时的行为是否与那时一致，语料里没有依据。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.md`

**本页没做的：**

- **本页读了这一篇的图**（§11.4）：`raw/20979.png`（Import mode 流程图）、
  `raw/30579.png`（Store mode 在线流程图）、`raw/20980.gif`（Store mode 离线流程图），
  **外加 `raw/21635.png`（Pass/Fail Dialog 截图）**。**四张都读得出来。**
  **图里读到的字在 raw 文本里搜不到**——拿 `Not Access`、`Prompt Window`、`User Input`、
  `Bypass Emulator`、`Emulator Off`、`store HW Response Data` 去这一篇 grep，
  **一处也没有**（`Not Access` 与后三个只在图的像素里）。**所以凡来自图的，本页都标了「图证」。**
- **`raw/21635.png` 不在这一篇正文里，它只在语法节里**（语法节自己声明那段 Example 取自子主题
  `02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.md`）。
  **所以那张图与语法节第一段 Example，本页都没有读它们所属的那篇 raw**——
  **读者要核这一段，得去子主题 `.02`，不是本篇。**
- **四个子主题一篇都没读**（`02.08.04.32.02.06.01` / `.02` / `.03` / `.04`）——
  **这是本页最大的空缺**，因为原文把三件要紧的事全推给了它们：
  **文件怎么准备（`.01`）**、**怎么用文件跑（`.02`）**、**哪些 test suite / API 支持（`.04`）**。
  **本页只能给出「有这四篇」，给不出其中任何一篇的内容。**
- **两组 `Related information` 目标没读**：`Checking the execution flow` 与
  [[offline-result-emulation]] ——**所以「查执行流」和「离线结果仿真」各自是怎么回事，本页不知道**
  （**只能确定它们不是本页的东西**，见 `## 和谁有关` 第二条）。
- **`run-dialog` 没读** —— **所以 HWRE 在 GUI 上从哪开、模式在哪选，本页答不了**。
  这是本页**最大的一个洞**：正文定义了两个模式，却没说入口。
- **没有任何 L1 / L2 / L3 材料** —— **这一篇全文没有出现过一条命令、一个 API、一个文件名**
  （唯一的例外是语法节第二段 Example 里那个 `Analog.DGT("a_out").getWaveform()`，
  **而那也是从子主题 `.03` 借的**）。**所以「怎么在自动化脚本里控制 HWRE」，本页一个字都给不出。**
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其本页 `stage: run` 填的是「最近的一段」（§6），不是「归属」**——
  **这一篇没有一句话说它属于哪一段流程**，`run` 是按「离线调试跑流程时用」这个时机填的。
- **`02.08.04.32.02.06.01.*` 底下那几篇 `*_type.md`（含一篇名字里带 `FW_TASK` 的）一篇都没读**——
  **本页只知道那一层存在（依据是语料的文件树，不是本篇正文）。**
  **⚠️ 名字里带 `FW_TASK` 的那一篇，和 L2 的 [[fw-task]] 是不是同一个东西，
  本页没有依据判断——不许凭名字合并。**
- **一张图之外的图都没有**，原文也没有别的图。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 文档标题跳了两级。** 正文第一个标题是 `#### Subtopics`（**四级**），
> 而文档标题是 `# Hardware Response Emulator`（一级）——
> **中间没有 `##` / `###`**。**本页照原样说它是 `#### Subtopics`，不替它降级或升级。**
>
> **② `Related information` 三个链接粘成一行，中间没有任何分隔符。** 逐字（**注意三个名字之间一个字都没有**）：
> `Using hardware response files for execution`＋`Checking the execution flow`＋`Offline Result Emulation`。
> ——**本页照实说，不替它加分号、逗号或换行。**（**同样的形状在本批另一页也出现了**，
> **说明这是语料的通病，不是这一篇的特例。**）
>
> **③ 图里的 `Not Access` 不是规范英文。** 三张流程图里，从测试机图案引出的虚线都标着 `Not Access`
> （按语义该是 `No Access` 或 `Not Accessed`）。**这是图里的字形，搜不到**，
> **本页引它时照原样，不替它改。**
>
> **④ 讲离线的那一段末尾突然提到在线模式。** 逐字：
> `You can also use the data files as virtual data in online mode.`
> ——**这一句在 `## Store mode` 讲「离线跑时弹窗」的那段的末尾**，
> 而 `online mode` 是这段前面才刚讲完的另一种情形。**两种读法原文都没排除**：
> **(a) 它是在说「离线里存出来的文件，在线时也能当虚拟数据用」**；
> **(b) 它是在补一句「在线模式下也可以把数据文件当虚拟数据」**（那它就该在前一段）。
> **本页把两种读法并列，不判哪个对，也不替它挪位置。**
>
> **⑤ 同一个触发点，原文用了单数 `a prompt window`，而图里画了两个窗口。** 原文逐字：
> `the emulator opens a prompt window when the execution reaches the end of the test suite or the
> test method API for retrieving hardware response data`
> ——**一个 `a`，后面跟 `or` 两个点**；而图证（`20980.gif`）里两个触发点各有一个 `Prompt Window`。
> **原文这句话本身也读得出两种意思**（每个点各弹一次 / 这一类点弹同一个窗口）。
> **本页并列两处，不替它改成复数、也不替它合并。**
>
> **⑥ 语法节那两段 Example 不是这篇正文里的。** 页首语法节自己声明了出处是子主题
> `02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.md` 与
> `02.08.04.32.02.06.03_Hardware_response_files.md`，
> **而这两篇都不在本页的 `sources:` 里**（`sources:` 只有父篇，见 §6.1 第 1 条）。
> **这是语料结构如此，不是错**；但**读本页的人要知道：语法节里那两段引文，
> 本页作者没有回原文核过**（**本页只核了它没有改动**）。
>
> **⑦ 正文里 `File` 的图注与原文用词不一致。** 图证里两个圆柱写的是
> `Store hardware response data` / `Store test result data (pass/fail)`，
> 而原文写的是 `stores the test results (pass/fail) and hardware response data`
> ——**图里用的是 `test result data`（单数 result），原文用的是 `test results`（复数）。**
> **本页并列两处，不替任何一处统一。**
>
> **⑧ `and so on` 让一份清单变成了开放清单。** 逐字：
> `returns already prepared data such as analog waveform data, measurement values, pass/fail
> results, and so on at appropriate points in the test.`
> ——**`such as` 加 `and so on`，所以这三类不是全部。**
> **没有别处给出完整清单**（**子主题 `.04` 的标题只管「哪些 suite / API 支持」，
> 不管「哪些数据类型」**）。**本页照实说它不封闭，不替它补全。**

`verified: doc-only`
