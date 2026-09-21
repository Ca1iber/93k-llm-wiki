---
type: mapping
title: Run / Debug 的三层对照
layer: n/a
stage: run
tags: [mapping, run, debug, testflow-execution, flags, execution-context, hardware-response-emulator, site-focus, utility-line]
related: [run, testflow, results, testmethod, testflow-tool, run-dialog, flow-sequence-editor, test-suites-page, flags-page, debug-view, debug-perspective, report-window, site-control-window, hardware-view, utility-line-view, hardware-response-emulator, hardware-response-file, testflow-file, execution-context, timing-diagram-tool, error-map-tool, offline-result-emulation, flsh, flush, sqst, ci-cpi, test-suite-control-api, controlling-multiple-sites, tpi-program-routines, pattern-tool, special-test-suites, signal-analyzer, spec-tool]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.01_Loop_configuration_settings.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.04_Measuring_the_test_time.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04_Debugging_a_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01.06_Pass_Fail_type_and_ERROR_MAP_type.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.03_Hardware_response_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.02_Testflow_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.04_Test_suite_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.01_Defining_variables.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.03_Changing_the_site_in_focus.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.01_Result_Mode.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.02_Execution_Mode.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.01_Primary_view.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.05_Profiling_of_DC_Scale_cards_with_Hardware_view.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.05_Using_the_Utility_Line_View.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.06_Debug_View.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.03_Run_menu.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.03_Defining_the_query_focus.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04_Loops.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.08.07_Setting_Flags.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.07_Controlling_a_Production_Run.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.07.01_Aborting_a_Production_Run.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.01_HVM_API_Introduction.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.02_Controlling_test_execution_with_HVM_API.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02_Test_suite_control_API_reference.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Run / Debug 的三层对照

## 这张表在说什么

Pin 那一段的地基是语料自己的一句话（`corresponding exactly to`），**run 这一段没有这种整段声明**。
所以本页**不搬那句话**，也不假装有。这一段的证据形态与 pin 段不同，先把差别说清：

**① run 段确实有「明说对应」的话，但只在两个点上，而且是逐条说的。**
它们都在 Hardware Perspective 的 GUI 文档里：

`01.01.07.05.05_Using_the_Utility_Line_View.md`：

> - Right-click and select Write Mode to query the write state of the pins in the selected block (this corresponds the firmware command UTOT?).

同一篇还给了另外两条同型的话（`Read Mode` ↔ `UTIX?`、`Apply Write` ↔ `UTOT`），
以及一条把读状态在 GUI 与标准 test method 之间对齐的说明：

> Note that the Utility Line View displays the read states using L (TTL Low) and H (TTL High). L corresponds to read state 1 in the standard test method and firmware command (where negative logic is used), and H corresponds to read state 0 in the standard test method and firmware command (where negative logic is used).

（第一句里 `this corresponds the firmware command` **少了一个 `to`**，是**语料自己的语法错**，见「对不上的地方」⑥。）

`01.01.07.05.01_Primary_view.md`：

> - Execute functional tests with the current primaries and retrieve Pass/Fail result returned by the FTST? - (Functional TeST) firmware command.

**② 除此之外，run 段跨层对照的证据形态是「链接」，不是「声明」。**
也就是说：**GUI 文档链到命令/API 文档**——这只证明「那篇文档认为读者该去看这一篇」，
**不证明两个东西等价**（见「证据」一节的强度说明）。本页把这两类证据分开写，不混成一种。

**附：本段的结构事实——run 阶段不新建 setup 文件。** 这一条 `wiki/stages/run.md` 的「产物」节已经记了
（原文：「**文档未覆盖**「run 阶段新建 setup 文件」这件事——**它本来就不新建**」）。
所以本表「文件」列很空：**本阶段唯一的回写对象是 `[[testflow-file]]`**。
这一列填 `—` 表示**这个动作不对应任何文件**（理由逐行给在「证据」一节），填 `?` 表示**语料没说清**。

**另：「执行类」动作与「观察类」动作的证据密度差得很远。**
起测、flag、focus site、execution context 这几行有实链；Timing Diagram / Debug view 这类**看结果**的 GUI
**一条跨层链接都没有**，它们整行只剩 GUI 一格有名字。**这不是我没找，是语料在那个方向上没链。**

## 对照表

**读法**：一格填了名字 = 有证据（证据是什么见下一节）；`?` = 语料没说，**本页不猜**；
`—` = 这一层不存在这个对应物（不是「没找到」）。名字后面带 `（推断）` 的，
**是本页按职责排的对应，不是文档明说的**——依据逐条写在「证据」一节。
**带（图证）的格 = 那一格的名字在 raw 的图上直接看得见**——
是哪张图、图里的字为什么搜不到，见证据节 **④** 与「对不上的地方」**⑧**。

| 目的 | GUI | 文件 | L1 命令 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 跑整条 testflow / 选中的 test suite | [[testflow-tool]]、[[run-dialog]]（**图证**：配置树四档）、[[flow-sequence-editor]] | [[testflow-file]] | `SQST RUN` | `START_TEST()` / `EXECUTE_TEST()` / `FUNCTIONAL_TEST()` | `ExecTestflow()`（推断）、[[test-suite-control-api]]（推断） |
| 就地跑一次 functional test，取 PASS/FAIL | `Primary view`（`01.01.07.05.01`） | `?` | `FTST?` | `?` | `?` |
| 中止 / 暂停 / 复位正在跑的 testflow | Operator Control window 四按钮（`02.09.01.07`） | `?` | `?` | `?` | `?` |
| 设 / 读 testflow 与 system flag | [[flags-page]]（**图证**：`Flag Type` 列逐字有 `SYSTEM` 与 `TESTFLOW` 两种取值） | [[testflow-file]]（`flags` 段） | `?` | `SET_TESTFLOW_FLAG` / `GET_TESTFLOW_FLAG`、`SET_SYSTEM_FLAG` / `GET_SYSTEM_FLAG` | [[ci-cpi]]（`SetTestflowFlag` / `GetTestflowFlag`） |
| 设 / 读 test suite flag | Test Suite Flags tool（`02.08.04.32.01.02.07.04`） | [[testflow-file]]（`test_suites` 段） | `?` | `SET_TESTSUITE_FLAG` / `GET_TESTSUITE_FLAG` | [[ci-cpi]]（`SetTestsuiteFlag`）、[[test-suite-control-api]]（`setTestsuiteFlag()`）（推断） |
| execution context：并行跑 multiport burst 的子集 | `?` | `—` | `SQEC` / `SQRC` / `SQLC?` / `SQSC?` | `SEQUENCER_CONTEXT` / `SEQUENCER_CONTEXT_ITEM` / `INDEPENDENT_TEST` | `?` |
| 把缓冲的设置真正刷到硬件（调试用） | `?` | `—` | [[flsh]] | [[flush]] | `?` |
| 选 site / 改 focus site | [[site-control-window]] | `?` | `PQFC` | [[controlling-multiple-sites]] | `setSiteInFocus()` / `setActiveSites()`（推断） |
| 运行期查 / 写 utility line | [[utility-line-view]] | `—` | `UTOT?` / `UTIX?` / `UTOT` | `?` | `?` |
| 离线跑（用预置数据代替真实硬件） | [[hardware-response-emulator]]（**图证**：Run dialog `Main` 页里的 `Response Emulator` 区，两个单选 `Import` / `Store`） | [[hardware-response-file]] | `?` | `GET_FUNCTIONAL_RESULT()` / `TEST()` | `?` |
| 看错误图 / 配置 error map 记录 | [[error-map-tool]] | `?` | `CYRM` / `CYRP` / `DCRM`、`FTST?` | `?` | `?` |
| Hardware view 上就地测量 / DC profiling | [[hardware-view]] | `—` | `UTSC` | `DC_PROFILING_DEFINE` / `_ENABLE` / `_ON` / `_OFF` | `?` |
| 调试 testflow（单步 / Debug view） | [[debug-view]]、[[debug-perspective]] | `—` | `?` | `02.07.02.02.04_How_to_debug_a_universal_test_method` | `?` |
| 看实际发给 DUT 的波形 | [[timing-diagram-tool]] | `—` | `?` | `?` | `?` |
| 把整条 testflow 反复跑（Loop 区） | [[run-dialog]]（Loop 区）（**图证**：`Enable` / `Count` / `Loop Indefinitely` / `Stop On Pass` / `Stop On Fail` / `Log Loop Number` / `Pause between loops` 七项同屏） | `?` | `?` | `?` | `?` |

**表里没有的两类东西**：

- **testflow 变量 / user flag**（`02.08.04.32.02.01.12.01_Defining_variables` 明链 `GET_USER_DOUBLE` /
  `GET_USER_STRING` / `GET_USER_FLAG`）——它的 GUI 是 Flow Data Editor 的 Variables page，
  而 **Variables page 与 `[[testflow-variable]]` 属 `[[testflow]]` 段**，本页不抢。
- **`ABORT` / `RESET` / `ABORT TESTFLOW` / `PAUSE` 的运行期语义**——`wiki/stages/run.md` 已收，
  **且已裁「层是 `gui`，不是 L3」**，本页只在第 3 行留一格 `?` 记这个缺口，不重复铺开。

## 证据：哪几格是钉死的，哪几格只是「那边链过来了」

**证据分四档，本页不把它们混成一种。**

**① 文档明说对应（最硬）——只有 4 条，全在 GUI↔L1。**
就是开篇那两句所在的**同一批句子**，出自 `01.01.07.05.05`（3 条）与 `01.01.07.05.01`（1 条），
对应主表的**第 2 行 L1 格**与**第 9 行 L1 格**。这 4 条是**逐条点名**的，
比「链接」硬，但**只覆盖这两个 GUI、四个命令**，不覆盖整段。

**② 文档之间有链接（次硬，逐条可查）——取自 `extract/edges.jsonl`。**
筛选口径：`from` 落在 `wiki/stages/run.md` 的 `sources:` 那 64 篇里，`to` 落在
`02.06` / `02.07` / `02.09` 三个跨层区。命中如下（**只列主表用到的**）：

| 源文档（本页读过的） | 链到 | 进主表哪一格 |
|---|---|---|
| `01.01.07.05.05_Using_the_Utility_Line_View.md` | `UTOT?`、`UTIX?`、`UTOT`（`02.06.02.02.311` / `.310`） | 第 9 行 L1 |
| `01.01.07.05.01_Primary_view.md` | `FTST?`（`02.06.02.02.127`） | 第 2 行 L1 |
| `02.08.04.27.03_Changing_the_site_in_focus.md` | `Controlling Multiple Sites`（`02.07.03.13`） | 第 8 行 L2 |
| `02.08.04.27.03_Changing_the_site_in_focus.md` | `Site dependent firmware commands`、`Defining the query focus`（`02.06.03.01.10.03`） | 第 8 行 L1 |
| `02.08.04.32.01.02.07.02_Testflow_flags.md` | `SET_TESTFLOW_FLAG`、`GET_TESTFLOW_FLAG`（正文点名，非超链接） | 第 4 行 L2 / L3 |
| `02.08.04.32.01.02.07.04_Test_suite_flags.md` | `GET_TESTSUITE_FLAG`、`SET_TESTSUITE_FLAG` | 第 5 行 L2 |
| `02.08.04.32.02.06.01.06_Pass_Fail_type_and_ERROR_MAP_type.md` | `GET_FUNCTIONAL_RESULT`、`TEST` | 第 10 行 L2 |
| `01.01.07.05.03.05_Profiling_of_DC_Scale_cards_with_Hardware_view.md` | `DC_PROFILING_DEFINE` / `_ENABLE` / `_ON` / `_OFF`（`02.07.04.01.24`–`.27`） | 第 12 行 L2 |
| `02.08.04.08.04.01_Result_Mode.md` | `Possible combinations of CYRM, CYRP, and DCRM`（`02.06.11.01.02.01.02.05`） | 第 11 行 L1 |
| `02.08.04.08.04.02_Execution_Mode.md` | 同上，并**正文点名 `FTST?`** | 第 11 行 L1 |
| `02.08.04.32.02.04_Debugging_a_testflow.md` | `How to debug a universal test method`（`02.07.02.02.04`） | 第 13 行 L2 |
| `02.08.04.32.02.06_Hardware_Response_Emulator.md` | `Offline Result Emulation`（`02.07.12`） | 第 10 行（见下「弱在哪」） |
| `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md` | `SEQUENCER_CONTEXT`、`SEQUENCER_CONTEXT_ITEM`、`INDEPENDENT_TEST` | 第 6 行 L2 |
| `02.07.04.01.69_FLUSH.md` | `FLSH`、`SQST`、`APRM`、`WSDN`、`FTCG` | 第 7 行 L1 |
| `02.09.01.10.02_Controlling_test_execution_with_HVM_API.md` | `ExecTestflow()`（`02.09.01.10.03.02.02.22`） | 第 1 行 L3 |

**链接证的强度必须说清，而且这一段的链接比 pin 段更弱**：pin 段的链接多落在**同一件事的两侧**
（编辑器文档 ↔ 它自己那条命令）；run 段的跨层链接里，**有相当一部分是「见也」式的**
（`Debugging_a_testflow` → `How to debug a universal test method` 的上下文是
「For debugging individual test methods, see How to debug a universal test method.」，即**换一件事**；
`Hardware_Response_Emulator` → `Offline Result Emulation` 也是并列的两种离线手段，不是同一个东西）。
**本页只在主表同一行里用它们，不跨行搬；「见也」型的已在行内标清。**

**③ 本页按职责排的对应（推断）——四处，分三条写，依据逐一给出。**

- **第 4 行 L3（`[[ci-cpi]]`）**：依据是 `02.08.04.32.01.02.07.02` 的**正文原话**，
  它把 testflow flag 的两个外部入口点了名：

  > You can also set this flag using SET_TESTFLOW_FLAG API (test method), or SetTestflowFlag API (CI_CPI). You can determine the current setting of the flag using GET_TESTFLOW_FLAG API (test method), or GetTestflowFlag API (CI_CPI).

  **`CI_CPI` 属 L3 不是本页定的**——`wiki/stages/testflow.md` 的「涉及对象」表已把它记成 `L3`。
  本页只是把它接到 run 段这一行上。

- **第 5 行 L3（`[[test-suite-control-api]]` 那一格）**：依据是 `02.09.01.14.02` 的能力清单第一条相关项：

  > - retrieve and change the settings and flags of test suites

  **但 `02.08.04.32.01.02.07.04`（GUI 那篇）里没有任何一条链到它**，
  所以这一格是**推断**，不是链接证。`wiki/stages/testflow.md` 另有一句要记住：
  **CI_CPI 的 `GetTestsuiteFlag` 与 TestsuiteProxy 的 `getTestsuiteFlag()` 是两套不同的接口**
  （前者从 testflow 程序内访问，后者从外部客户端访问）——**本页把它们分列，没有合并**。

- **第 1 行 L3 与第 8 行 L3**：`02.09.01.10.02` 的取舍句与 `wiki/stages/run.md` 已有的推断句
  （「`setSiteInFocus` / `setActiveSites` 与 `[[site-control-window]]` 是同一件事的外部化」）。
  两行的 GUI 侧**都有一条链到 L3 区，但链到的是「同一件事的说明页」，不是 API 页**：
  `02.08.04.32.02.03` 链向 `02.09.01.07.0x`（Aborting / Resetting / Pausing a Production Run），
  而那几篇讲的是 **GUI 按钮**，不是 API。**所以这两格标（推断），不标「文档明说」。**

**附：`—` 那 6 格的逐行理由**（这一列是本页判断，写在这里供复核）：

| 行 | 为什么「文件」层不存在对应物 |
|---|---|
| 第 6 行（execution context） | `wiki/stages/run.md` 已裁：execution context **不由 `SQLB` 定义、不进向量文件**，由 `SQEC` 在运行期建立 |
| 第 7 行（`FLSH` / `FLUSH`） | `02.06.02.02.124` 明说被缓冲的是 **MCD（Message Concentrator and Distributor）**里的状态，不是文件 |
| 第 9 行（utility line） | `UTOT` / `UTIX` 读写的对象是**硬件输出状态**（`02.06.02.02.311` / `.310`），不经文件 |
| 第 12 行（DC profiling） | 文档自己说这份配置不落盘：「The content of the Seq Ctrl'd Util Blocks field is not stored/restored after closing the dialog.」 |
| 第 13 行（Debug view） | `01.01.08.06` 只描述执行控制（Restart / Resume / Suspend / Terminate / Step over），无文件对象 |
| 第 14 行（Timing Diagram Tool） | `02.08.04.33` 说它画的是 **actual waveforms**（发出去的与 DUT 回来的），不是某个 setup 文件 |

**主表里全部 6 个 `—` 都在这张表里**（即「文件」列），**其余四列一格 `—` 都没有**。
特别是 **L3 列一格 `—` 都没有**——run 段的 L3 三个入口（HVM / test suite control / TPI）
覆盖的是「跑什么、跑哪几个 site、跑完怎么样」，**本页找不到任何一行能像 pin 那页那样
从结构上断言「外部进程插不进来」**，所以宁可留 `?`。

**另：`?` 最多的三行（第 3、14、15 行）有一个共同点：它们都是「只有一个入口、没有第二个视角」的动作。**
中止/暂停只从 GUI 按钮发起、Timing Diagram 只从 GUI 打开、Loop 区只从 Run dialog 设——
**语料没有从命令侧或 API 侧再讲一遍同一件事**，所以三行只剩 GUI 一格有名字。
**这不是「这些动作没有命令侧」，是「语料没从命令侧写它们」**——这两句的区别就是 `?` 与 `—` 的区别。

**④ 图证（2026-09-20 加，本页用到了）** —— 从 raw 自带的截图里读出来的。
（`schema.md` §2.5：**④ = 图证**。）

**本页 sources 里带图的文档共 23 篇 / 59 张**（**数量第二多**——因为 `01.01.07.05.03_Hardware_view`
一篇就带 11 张图标、`01.01.08.06_Debug_View` 带 7 张）。**本页只读了两张**，
挑的是**能看见一整组控件**的两张；**其余五十七张没看**。逐张：

**（a）`119959.png`（`02.08.04.32.02.03`，alt `Run dialog for the selected testflow execution`）
—— Run dialog，本页信息量最大的一张。** 窗口标题栏逐字是
`Create, manage, and run configurations`，右上角一个绿色运行按钮。
左列是一棵配置树，逐字有 `C/C++ Application`、`Launch Group`、
`Testflow (Full)`（两项）、`Testflow (Selection)`（两项）、`Testflow (User Defined)`、`Testflow`；
底下一行 `Filter matched 8 of 8 items`。右半是配置面板：`Name:` = `Testflow (Selection)`，
页签 `Main`，其下四组逐字是：

- `Site in Focus (for selection of test suites only)`（勾选框）
- `Loop`：`Enable` + `Count:` = `1`、`Loop Indefinitely`、`Stop On Pass`、`Stop On Fail`、
  `Log Loop Number`、`Pause between loops:` = `0.0` `ms`
- `Single Step Execution`：`Enable 'single step' execution mode`
- `Response Emulator`：`Enable` + 两个单选 `Import` / `Store`

底下按钮 `Apply` / `Revert` / `Run` / `Close`。

**它印证主表的三行**（表里已标「（图证）」）：跑整条 testflow（配置树四档就是那四档）、
把整条 testflow 反复跑（Loop 区七个控件同屏）、**离线跑**。
**其中「离线跑」那一行是本页唯一被图改写过内容的一格**：原文正文只说
`If you use Response Emulator, set the options in the Response Emulator area.`
**而没说这个区在哪个窗口、里面有什么**；**图上它在 Run dialog 的 `Main` 页里，
两个选项逐字是 `Import` / `Store`**——也就是「读一份已经存好的响应文件」与「把响应存下来」
两个方向。**本页据此把那一行的 GUI 格从 `[[hardware-response-emulator]]`
补成「Run dialog `Main` 页的 `Response Emulator` 区」**。
**要标清这是图证不是文档事实**：`Import` / `Store` 这两个选项名**在本页 sources 的正文里查不到**
（正文只有 `set the options in the Response Emulator area` 这一句外加两条外链）。
**grep 不到**：`Create, manage, and run configurations`（0 命中）。
**它答不了的**：**图里没有 `SEQUENCER_CONTEXT`、没有 `SQEC`、没有 `ExecTestflow`**——
那一行的 L1 / L2 / L3 三格**图一格都没动**；`Stop On Pass` 之类在正文里也都写得到，
所以**图上真正搜不到的只有标题栏那句**。

**（b）`110705.png`（`02.08.04.32.03.01.06_Flags_page`，alt `Flags page`）—— Flags 页。**
文件页签 `adc_dac_x2.tfl`，表头逐字三列 `Flags | Flag Type | Value`，
可见的行逐字有 `calib_age_monitor` / `diag_monitor` / `current_monitor` / `log_events_enable` /
`stdf_generation` 五条 `SYSTEM`、`tm_crash_as_fatal` `SYSTEM` `off`，
以及 `set_pass_level` / `set_fail_level` / `set_bypass_level` / `hold_on_fail` 四条 `TESTFLOW`；
底部页签逐字 `Test Suites | Parameters | Tests | Bins | Variables | Flags | Setups | Information`。
**它印证主表「设 / 读 testflow 与 system flag」那一行的 GUI 格**，
并把 L2 格里的 `SET_SYSTEM_FLAG` / `SET_TESTFLOW_FLAG` 与表里那两种 `Flag Type` 取值对上了字面。
**这里有一条「图能看、但不能推」的界线，必须写明**：
**表格是滚动过的**（最上面一行的行号是 `14`），**所以这张图不能用来断言
「旗标只有 SYSTEM 与 TESTFLOW 两种、没有 TESTSUITE 那种」**——
被滚上去的行在图上不存在。**本页因此没有拿它去动第 5 行（test suite flag）那一格。**
**grep 不到**：`adc_dac_x2`（0 命中）、`Flag Type` 这个**列头**（全库只有 1 命中，在
`02.08.04.32.02.01.16`，**那一篇不在本页 sources**）。
其余旗标名在 `.32.01.02.07.01` / `.32.01.02.07.02` / `.32.03.05` 里都搜得到，
**而 `.32.01.02.07.02` 与 `.32.03.05` 就在本页 sources 里**——**所以那些名字不算图证。**

**图证整体答不了的三件事，照实说：**

- **两张图没有出现一条固件命令名。** 主表 L1 列的 `?`（中止/暂停的 `?`、flag 的 `?`、
  Loop 的 `?`）**一格都没动**。
- **两张图没有出现一个 L3 API 名。** `ExecTestflow()` / `setSiteInFocus()` /
  `setTestsuiteFlag()` 那些（推断）**全部留在原处**。
- **图是「某一次具体配置」的截图，不是规范。** 「Loop 区哪些组合合法」「`Import` 与 `Store`
  能不能同时选」**图答不了**——那是文本的事，而文本在这一点上也没写全。

## 对不上的地方

**① 第 3 行（中止/暂停/复位）整行只有一个名字，这是本页最空的一行，缺口写在这里。**
四个按钮的**运行期语义**在 `02.08.04.32.02.03` 的 `What to do next` 与 `02.09.01.07` 里写得很全，
但那两处**都是 GUI 侧**；L1/L2/L3 三格**一条证据都没有**。而 `wiki/stages/run.md` 已经**裁过**：
这一组是 `gui` 层，**不是 L3**——**本页沿用那个裁定，没有把它塞进 L3 格充数。**

**② Loop 那一行（第 15 行）四格全 `?`，而且有一个同名不同物的陷阱。**
`02.06.07.01.08.04_Loops`（L1）讲的 **Endless / Counted / Match loops** 是
**「that can be executed within any type of label」**的定序器循环；
而 Run dialog 的 Loop 区（`02.08.04.32.02.03.01`）是**把整条 testflow 反复跑**。
**两者词面都是「loop」，位置与作用都不同。** 本页**没有把 `[[match-loops]]` 填进第 15 行的 L1 格**——
看起来像不算证据。**这一条值得后续单独查一次**（`02.08.04.32.02.03.01` 的
`Functional changes` 里还有一条版本约束：**SmarTest 6.5.2 起 loop 配置在执行期间不可更改**）。

**③ `[[timing-diagram-tool]]` 与 `[[error-map-tool]]` 两行的证据密度差得离谱，原因不在我。**
Error Map 那一行有 L1（`02.08.04.08.04.01` / `.02` 明链 `CYRM` / `CYRP` / `DCRM`，
`Execution_Mode` 正文还点名 `FTST?`）；**Timing Diagram 那一行一条跨层链接都没有**——
`02.08.04.33` 的 `Related information` 只链到 `Creating a new format` / `Shmoo Tool` /
`Timing Setup Tool` / `Signal Analyzer`，**全在同层或别的段**。
**两篇文档的形态差异是语料事实，不是本页漏查。**

**④ 「离线」在 run 段有两套东西，本页只填了其中一套，另一套的位置说明如下。**
`[[hardware-response-emulator]]`（HWRE，本页第 10 行）与 `[[offline-result-emulation]]`（ORE，`02.07.12`）
是**两套不同的离线手段**：`02.08.04.32.02.06` 把 ORE 放在 `Related information` 里，
是**并列**关系，不是从属关系。`wiki/stages/run.md` 把 ORE 记成 `concept` 层，
**本页因此没有把 ORE 填进第 10 行的 L2 格**——那一格填的是 HWRE 对话框自己点名的两个 API。

**⑤ `02.08.04.32.02.03.04_Measuring_the_test_time` 链到了 `02.09.01.05.01` / `02.09.01.05.05.01`（workorder），
本页没有为它开行。** 理由：那两篇讲的是**建 workorder、从操作面板跑 workorder**，
属**生产流程**而不是 run 段的一个动作；`wiki/stages/run.md` 的「涉及对象」也没收它。
**先把链接记在这里，免得下次有人重新发现一遍。**

**⑥ 语料自己的错字 / 瑕疵，本页照实记下，一处都没替它改**（§11.2）：

- `01.01.07.05.05` 里 **`this corresponds the firmware command`** 出现 **1 次**（`Write Mode` 那一处，
  链到 `UTOT?`），**少了 `to`**（应为 `corresponds to`）。本页引文原样保留。
  **⚠️ 同一篇里另外两处是写对的**：`Read Mode`（链 `UTIX?`）与 `Apply Write`（链 `UTOT`）
  都写 `this corresponds to the firmware command`。**所以这不是「全篇漏字」，是三处里错一处**——
  **别把「有一处错」记成「处处都错」**（本页第一版就是这么记的，回原文逐处数过才改）。
- `01.01.11.03_Run_menu.md` 里同一条：

  > The emulator can be used to debug a testflows or test suites.

  **`a testflows` 应为 `a testflow`。** 这一句上面的引文块**逐字照抄了它**，
  **本页没有把它当证据用**（它只是这条瑕疵的实例）。
- `01.01.07.05.03_Hardware_view` 里 **`pattern鈥慴ased`**（U+2011 被按 GBK 读坏，`鈥慴` = `‑b`），
  §11.2 ① 已记该类现象 528 篇 / 2,816 处。**本页正文没有引用句**；
  记一笔是为了说明：**拿修好的 `pattern-based` 去 raw 里搜是搜不到的**，要搜坏掉的原形态。

**⑦ 「结果」不是本页的事。** Report window 的输出、Flow Sequence Editor / Test Suites page 的着色、
数据日志、STDF/EDF、bin 判定，**一律归 `[[results]]`**；
`wiki/stages/run.md` 的边界声明已经这么划了，本页不复制、不重排。

**⑧ 图能读，本页读了两张——原先写的「图在语料树之外」是错的。**（**2026-09-20 更正**）
`../../../../raw/x.png` 往上四层正好是 `tdc-html/`，**图就在 `tdc-html/raw/` 里，读得出来**
（`schema.md` §11.4）。本页读了 `119959.png`（Run dialog）与 `110705.png`（Flags 页），
逐张见证据节 ④。**两张都是窗口截图，都没有小图标。**
**读完之后的账要算清：**

- **新拿到的只有两格，都在 GUI 列**：第 10 行「离线跑」的 GUI 格——**这一格被图补全了**
  （`Response Emulator` 区在 Run dialog 的 `Main` 页里，两个选项 `Import` / `Store`，
  **正文没说，图上才有**）；第 15 行「Loop 区」的 GUI 格——**图上七个控件同屏**
  （但七个名字正文里都写得到，所以**这一格是「同屏可见」，不是新证据**）。
- **一个字都没换来的是 `?`**：主表里那些 `?` **一个都没填**——
  两张图里**没有固件命令名、没有 L3 的 API 名、没有一行文件内容**。
- **两处「图能看、但不能推」的界线本页写明了**：
  ① Flags 页那张**表格是滚动过的**（首行行号 `14`），**不能拿它断言「旗标只有两种类型」**；
  ② Run dialog 那张**只画了 `Testflow (Selection)` 这一档**，
  **`Testflow (Full)` / `Testflow (User Defined)` 两档的 `Main` 页长什么样，图里没有**——
  正文说三档的 Loop 区与 Response Emulator 区配置相同，**但那是文字说的，不是图上看的**。
  **本页没有把这条正文的话说成图证。**
- **一处措辞本页照实记、没替语料改**：正文把那个窗口叫 `Run configurations dialog`
  （`Run > Run configurations`），**而图上标题栏逐字是 `Create, manage, and run configurations`**。
  **两个名字都留着**，主表里本页用的仍是 `[[run-dialog]]`（那是个 wikilink 名，不是文档原话）。

## 出处

`sources:` 三十六篇，**全部是 `raw` 里的相对路径**（见 frontmatter）。
其中**进了引文块的只有 5 篇（共 6 处）**：`01.01.07.05.05`（2 处）、`01.01.07.05.01`、
`02.08.04.32.01.02.07.02`、`02.09.01.14.02`、`01.01.11.03`；
另有**一句英文短语**引自 `02.06.07.01.08.04_Loops`（在正文里，不在引文块）。
**其余各篇只读了正文以取「链接」与「有没有这件事」，没有逐字引用。**
（`02.09.01.07.01` 单读，是为了核「第 3 行那几篇讲的是 GUI 按钮不是 API」这句判断是否成立——
**核完成立**：正文原话是「click the ABORT toggle button in the Operation Control window」。）

**本页没做的**：

- **L1 侧只读了 4 篇，而且没有一篇是「一条命令自己的页」。**
  读的是 `02.06.07.01.08.05.03.02.03`（execution contexts）、`02.06.03.01.10.03`（query focus）、
  `02.06.07.01.08.04`（Loops）、`02.06.02.02.124`（`FLSH`）——**这 4 篇里后两篇算命令页，
  前两篇是「用法说明」页**。主表 L1 列里的 `SQST RUN`、`SQEC`、`PQFC`、`CYRM` / `CYRP` / `DCRM`、
  `UTOT` / `UTIX` / `UTSC` **各自己的页一篇没读**，名字是从**引用它们的 GUI / L2 文档**里取的；
  **它们的参数、返回值、错误行为，本页一个字没有。**
- **L2 侧只读了 2 篇。** `02.07.04.01.69_FLUSH`（[[flush]] 那一页，读全了）与
  `02.07.03.08.07_Setting_Flags`（只读了三对 setter 的表）。
  `START_TEST()`、`EXECUTE_TEST()`、`FUNCTIONAL_TEST()`、`SET_TESTFLOW_FLAG`、
  `GET_FUNCTIONAL_RESULT()`、`DC_PROFILING_*` **各自的页一篇没读**——
  **它们是不是真的「同一条链上的下一环」，本页只按链接出现的位置判，没有核对语义。**
- **`[[ci-cpi]]` 与 `[[test-suite-control-api]]` 的页面没读**（前者尚不存在）。
  本页用的是 `wiki/stages/testflow.md` 里已有的分层判断，**没有回 `02.09.01.08.05` 原文复核**。
- **`02.09.01.10.03.02.02.22_ExecTestflow.md` 没读**——只见到链接。
- **看了两张图（2026-09-20 加）。** 就是 `119959.png`（Run dialog）与 `110705.png`（Flags 页）
  ——各自出自哪篇、图里逐字有什么，见「证据」④ 与「对不上的地方」⑧。
  **两张都整张看完**，图上读到的字**逐条回 9,398 篇 raw md 里查过 grep 命中**——
  本页凡写「grep 不到」的都是实测 0 命中。**本页 sources 里带图的文档共 23 篇 / 59 张，
  其余五十七张没看**（`01.01.07.05.03_Hardware_view` 一篇就带 11 张图标）。
  **原先本页在这里写着图片路径「在语料树之外」——那是错的**，见「对不上的地方」⑧ 的更正。
- **「GUI 的哪一列对应命令的哪个参数」这个粒度的问题，本页仍然答不了。**
  **但理由换了**：不是「图够不着」，是**这两张图里没有固件命令名、没有 L3 的 API 名**。
  两张图**唯一**补全的一格是第 10 行「离线跑」的 GUI 格（`Response Emulator` 区的位置与两个选项）。
- **没有实跑。** 没有在机台上跑过 testflow、没有开过任何编辑器、没有生成过任何 response 文件。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/run.md`。
  后者是**待办**：run 那页目前不知道本页存在。

**本页 `layer: n/a` 的理由**：§6 要求 mapping 页必填 `layer`，而本页**本身不属于任何一层接口**
（它是对照表，不是接口）——`n/a` 是这个六值枚举里为这种情况准备的值。

**与 pin 那页的关系**：`wiki/mappings/mapping-pin.md` 是本页的格式样板。
**那页有「语料明说」的地基，本页没有**——这是两页最实质的差别，
本页把这件事写在最前面，就是为了**不让读者以为两页的证据强度一样**。

`verified: doc-only`
