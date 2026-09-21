---
type: stage
title: Run / Debug — 执行与调试
tags: [run, debug, testflow-execution, flags, debugger]
related: ["[[testflow]]", "[[results]]", "[[testmethod]]", "[[pattern]]"]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01_Digital_test_setup_flow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.04_Task_4__Setting_up_a_Test.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.05_Task_5__Executing_a_Test_and_Obtaining_the_Results.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.05.01_Setting_up_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.05.02_Test_Debugging_and_Data_Logging.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.06_Task_6__Executing_a_Test_Flow_and_Obtaining_the_Results.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.01_Loop_configuration_settings.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.02_Using_the_Overon_feature_while_running_a_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.03_Checking_the_execution_flow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.04_Measuring_the_test_time.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.05_Adding_user_defined_testflows_to_the_Run_menu.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04_Debugging_a_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04.01_Single_step_testflow_debugging.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01_Preparing_Hardware_Response_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.03_Hardware_response_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.04_Supported_test_suites_and_test_method_APIs.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11.01_Narrow_selection_and_wide_selection.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07_Flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.02_Testflow_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.04_Test_suite_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.05_Site_control_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.06_Flag_priority.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33.01_Using_the_Timing_Diagram_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33.03_How_to_read_timing_diagrams__Unstable_signals.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.04_How_to_debug_a_universal_test_method.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.04.01_Issues_to_affect_the_test_method_debugger.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.04.02_Setting_up_Flags_for_Debugging.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.04.03_How_to_print_static_variable_value_in_debugging.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.08.07_Setting_Flags.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.08.08_Obtaining_Status_of_Flags.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.12_Offline_Result_Emulation.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04_Loops.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.11_Errors.md
  - 01_Getting_started/01.03_Using_SmarTest/01.03.03.01_Using_the_debugger.md
  - 01_Getting_started/01.03_Using_SmarTest/01.03.03.01.01_Debugging_test_methods__Finding_and_moving_to_information.md
  - 01_Getting_started/01.03_Using_SmarTest/01.03.03.01.02_Debugging_patterns_efficiently.md
  - 01_Getting_started/01.03_Using_SmarTest/01.03.04_Working_with_testflows_efficiently.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.04_Debug_perspective.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.06_Debug_View.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.01_Executing_a_measurement.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.02_Quick_measurements.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.03_Hardware_view_for_digital_pins.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.04_Hardware_view_for_DPS_and_VI_pins.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.04_Utility_Line_view.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.01_HVM_API_Introduction.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.02_Controlling_test_execution_with_HVM_API.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02_Test_suite_control_API_reference.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.07_Controlling_a_Production_Run.md
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.md
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# Run / Debug — 执行与调试

> 把前七个阶段配好的 setup 真正下到机台跑起来，拿到 pass/fail、波形与错误图，定位并修掉 bug，然后再跑一遍。

**边界声明（先读这段）：**

- **组装** testflow 的结构（插 test suite、铺 bin、连 flow control）属 `[[testflow]]`，本页不写。
- **结果数据的组织、日志格式、判定（pass/fail、bin、STDF/EDF）** 属 `[[results]]`，本页只用 wikilink 指过去。
- Timing Diagram Tool 与 Error Map Tool 两边都会用到：**本页只讲「怎么用它定位问题」，不讲它的数据格式。**
- flag 是 testflow 与 run 的接缝：`02.08.01.01.05.01_Setting_up_flags` 是共用的。**「在哪一级定义 flag」属 `[[testflow]]`；本页只讲「运行时怎么用 flag 控制与观察」。**

## 目的

文档事实（`02.08.01.01.05_Task_5__Executing_a_Test_and_Obtaining_the_Results`）：

> Build up a test, then execute the test using the Testflow Tool
>  - Set up the system/testflow/testsuite flags.
>  - Execute the test.
> Obtain the test results and debug the test using the Testflow Tool, Timing Diagram Tool, and Error Map Tool.
>  - Examine pass/fail results.
>  - Obtain the digital operation using the Result Analysis tools such as Timing Diagram, Error Map, and so on.
>  - If there are some bugs in the test, fix them and then execute it again.

`02.08.01.01.06_Task_6__Executing_a_Test_Flow_and_Obtaining_the_Results` 把它扩到整条 flow：

> Make a testflow which consists of complete tests and then execute all tests.
>  - Insert bin, flow control, assign value elements and so on.
>  - Finalize the system, testflow, and test suite flag settings.
>  - Execute all tests.
> Obtain the execution flow and debug the testflow.
>  - Verify the execution flow of the testflow.
>  - If there are some bugs in the testflow, fix them and then execute it again.

这条流程解决的是「**已经配好的东西到底对不对**」。`02.08.04.32.02.03_Running_a_testflow` 的 About this task 直接点明用途：

> The Testflow tool allows you to directly run the entire testflow or one or more individual test suites from it, which is useful when debugging the testflow, or when integrating new test suites into the testflow.

推断：`Digital test setup flow` 把 Task 5/6 都划在「Testflow Tool + Error Map Tool + Timing Diagram Tool」之下，而 Task 1–4 分别归 Pin Configuration Tool / Level Setup Tool / Timing Setup Tool / Pattern Tool / Test Method Perspective。也就是说 **run 阶段是唯一一个不引入新 setup 编辑器、只引入「执行器 + 观察器」的阶段**——这是本页与前面八个 stage 最本质的区别。

## 前置条件

以下逐条为文档明写。

**1. 六个前置 stage 全部完成。** `02.08.01.01_Digital_test_setup_flow` 的任务表把 Task 1–4（planning → `[[pin]]` → `[[level]]`/`[[timing]]`/`[[pattern]]` → `[[testmethod]]`+`[[testflow]]`）排在 Task 5/6 之前。`02.08.01.01.04_Task_4__Setting_up_a_Test` 说明 Task 4 要做完这几件事才算能跑：指定全部 setup 数据文件、插入 test suite、指定 primary set 与 vector label、选一个 test method 程序。

**2. testflow 已装载。** `02.08.04.32.02.03_Running_a_testflow` 的 `Before you begin`：

> Make sure the testflow has been loaded.

**3. test method 已成功 build。** `02.07.02.02.04_How_to_debug_a_universal_test_method` 的 `Before you begin`：

> Make sure you are using SmarTest 6.3 or later, and the universal test method has been successfully built. A testflow using the test method must be ready for execution.

**4. 调试 test method 时，build configuration 必须是 `Debug [Active]`。** 见「常见错误」第 2 条。

**5. 单步调试需先启用。** `02.08.04.32.02.04.01_Single_step_testflow_debugging` 的 `Prerequisites`：「Enable single step testflow execution, see Step 2 in Running a testflow.」

**6. 用 HWRE 离线跑时**（`02.08.04.32.02.06.01_Preparing_Hardware_Response_files` 的 `Before you begin`）：已连接测试系统、所需 SmarTest 版本已激活、SmarTest 已运行、所需 testflow 已装载且已执行 `Load all Setups`、testflow 已在 Flow Sequence Editor 中打开、所有需要离线可用的 site 都是 active。

**7. 用 Hardware view 做测量时**（`01.01.07.05.03.01_Executing_a_measurement` 的 `Before you begin`）：已在 Pin Browser view 更新硬件信息；Hardware view 里 `Link with Editor and Selection` 已选中。做 DPS force/sense 检查前，`01.01.07.05.03.04_Hardware_view_for_DPS_and_VI_pins` 另有一条硬约束：「make sure the test system is in the disconnected state」。

## 涉及对象

格式：`[[对象页名]]` — 层级 — 它在本阶段干什么。

| 对象 | 层级 | 在本阶段干什么 |
|---|---|---|
| `[[testflow-tool]]` | gui | 执行入口。`02.08.01.01.05`：「Build up a test, then execute the test using the Testflow Tool」 |
| `[[run-dialog]]` | gui | Run Configurations 对话框。设 Testflow (Full) / (Selection) / (User Defined)、Loop 区、Response Emulator 区 |
| `[[debug-perspective]]` | gui | test method 调试的工作台。`01.01.07.04_Debug_perspective` 列出 Project Explorer / Test Program Explorer / Editor / Problems / Firmware / Breakpoints / Console / Error Log / Waveform / Variables / Debug / Properties |
| `[[debug-view]]` | gui | testflow 与 test method 的执行控制台（Restart / Resume / Suspend / Terminate / Step over） |
| `[[flags-page]]` | gui | 设 system flag 与 testflow flag。test suite flag 从 test suite 右键菜单或 Test Suite Flags tool 设 |
| `[[report-window]]` | gui | 看结果的第一现场。debug_mode 决定它显示什么 |
| `[[flow-sequence-editor]]` | gui | 跑完后节点着色（绿=passe / 红=fail / 黄=bypass）；也可右键 Run Testflow / Run Selected |
| `[[test-suites-page]]` | gui | `Result > Pass/Fail` 单元格着色；多 site 结果的两种显示规则 |
| `[[timing-diagram-tool]]` | gui | 看实际发给 DUT 的波形与 DUT 回应，并标出「收到的数据与 Pattern Tool 里期望数据不符」的点 |
| `[[error-map-tool]]` | gui | 「the major tool for low level examination of the test results you obtain when performing functional tests」，按 label/cycle 定位失败 |
| `[[pattern-tool]]` | gui | 时序图/错误图的对照面。`01.03.03.01.02` 教从 Properties 的 `Test Suite > Primaries > Pattern` 按 F3 直接跳到失败 pattern |
| `[[site-control-window]]` | gui | 多 site 调试：「you need to identify passing and failing sites and view the results of individual site in the result tools」 |
| `[[hardware-view]]` | gui | 看/改选定 pin 的当前硬件设置，并就地做测量（Measure / Quick） |
| `[[utility-line-view]]` | gui | 查询 utility line 读/写状态、设写状态，「when you are debugging your test setup」 |
| `[[hardware-response-emulator]]` | gui | HWRE。离线跑时用预置数据代替真实硬件返回 |
| `[[hardware-response-file]]` | file | HWRE 的数据载体。文件名 `Testsuite;MAPI; call#; site#` |
| `[[testflow-file]]` | file | `<device_dir>/testflow` 下的文本文件。flag 的改动会回写到它的 `flags` / `test_suites` 段 |
| `[[execution-context]]` | concept | 一组带名字的 port 列表，用来独立并跑 multiport burst 的子集 |
| `[[offline-result-emulation]]` | concept | ORE。无器件时用器件规格造出测量结果，做 flow / test method / DSP 例程的离线验证与回归 |

### 归属判定

不是文档事实，是本次建页时的判断，写在这里供维护者复核。

**`[[execution-context]]` 归本页（曾与 `[[pattern]]` 有争议，已裁）。**
`pattern.md` 初稿主张构造定义权归它，理由是文档挂在 `Multi-port burst labels` 之下。
复核时逐字读了 `02.06.07.01.08.05.03.02.03` 全文后改判归本页：该篇五条 `Restrictions`
（端口须属当前 start label、两 context 不得共用 channel、先起者须用 `SQST RUN`、
主时钟重算会停掉用户定序器任务、含 DC Scale 通道者不能并行）、起测方式、错误行为
**全部是运行期语义**；`SQEC` / `SQRC` / `SQLC?` / `SQSC?` 是对**运行期对象**的操作，
execution context 不由 `SQLB` 定义、不进向量文件——它不是一个 label 构造。
**位置与内容冲突时以内容为准。** `[[pattern]]` 保留 multi-port burst **本身**（`MPBU`）。

**`FLUSH` 是横切命令，本页不独占。** `[[testmethod]]` 讲的是「进 extension block 前
必须先 `FLUSH`，否则固件命令与缓存里的 setup 冲突」（`02.07.03.10`），
本页讲的是「它把哪些缓冲的设置真正刷到硬件」。两处是同一个命令的两个侧面，都留。

**`[[timing-diagram-tool]]` / `[[error-map-tool]]` 与 `[[results]]` 共见。**
本页只把它们当作**调试手段**（怎么定位失败）；「结果数据长什么样、怎么落盘」归 `[[results]]`。
`[[results]]` 那边有同向的边界声明，两页方向一致。

**`[[offline-result-emulation]]` 与 `[[testmethod]]` 共见。** 本页讲怎么用它跑离线流程，
`[[testmethod]]` 讲它是「无真实器件时验证 test program」的手段。

## L1 — Firmware / Setup Command

本阶段真正会敲的固件命令集中在**「把测试跑起来」与「把缓冲的设置刷下去」**两组。

### 1. 起测与执行上下文

`02.06.07.01.08.05.03.02.03_Using_execution_contexts` 的 "Related firmware commands" 段给出完整的一组：

> An execution context is defined with the `SQEC` command and started by adding its name to the command/query that executes the test (for example `FTST?` or `SQST RUN`). Execution contexts are deleted with the `SQRC` command.
> There are two queries that inform about the execution contexts that were started last. `SQLC?` retrieves this information per port, `SQSC?` returns it over all ports.

文档给的最小可用示例（照抄，`$` 行是输入、`<` 行是回显）：

```
> SQSL?
< SQSL "mu_burst1"
> SQLB? "mu_burst1",MPBU,(@@)
< SQLB "mu_burst1",MPBU,6,7,,(PA)
< SQLB "mu_burst1",MPBU,6,7,,(PB)
< SQLB "mu_burst1",MPBU,10,11,,(PC)
< SQLB "mu_burst1",MPBU,4,5,,(PD)
> SQLB? "mu_burst2",MPBU,(@@)
< SQLB "mu_burst2",MPBU,3,4,,(PX)
< SQLB "mu_burst2",MPBU,8,9,,(PY)
> SQEC "c1",(PA,PD)
> SQEC "c2",(PY)
> SQST RUN,"c1"
> SQSL "mu_burst2"
> SQST RUN,"c2"
```

文档对这个例子的关键解说（**这是「执行时怎么走」的核心，不是组装**）：

- 若 `c1` 在 `c2` 启动时还没结束，且 `PA`/`PD`/`PY` 互不相交、至少一个 context 只含 Smart Scale 通道，则两者并行跑。
- 例子中 `SQST RUN` 到 `c2` 之间没有改 primary timing —— 若改了，大概率触发 master clock period 重算，**会停掉 `c1`**。
- 第一个 context **必须**用 `SQST RUN` 而不是 `FTST?`；用 `FTST?` 会阻塞固件接口直到 `c1` 执行完并返回全局 PASS/FAIL。

并行执行的限制（同篇 "Restrictions"，违反时报错且**后来者不启动、先跑者继续**）：

- 一个 execution context 只有在**它的全部 port 都包含在当前 start label 里**时才能跑。protocol port 例外——protocol port 不允许出现在 start label 里。
- 两个 context 只有在**不共享任何 channel** 时才能并行。
- 两个 context 只有在**先启动的那个用 `SQST RUN`**（或 test method API `START_TEST()`）时才可能并行；若用 `FTST()`（或 `FUNCTIONAL_TEST()` / `EXECUTE_TEST()`），第二个只会在第一个返回全局 PASS/FAIL 之后才启动。
- 两个 context **都含 DC Scale 通道的 port** 时不能并行。

### 2. 刷新缓冲的命令

`02.06.02.02.124_FLSH_-__FLuSH_buffered_commands`：

> The following commands for utility lines do not immediately set the hardware. Instead they are buffered in the MCD (Message Concentrator and Distributor).

被缓冲的是 `UPST`、`UPTI`、`UTST`、`UTTI` 四条 utility line 命令。语法：

```
FLSH {MUX}, {"init_flags"}
```

文档对 `MUX` 参数有一条**命令式的禁令**：

> The optional MUX parameter is designed to be used as an execution code of a testflow that is generated by the system software for disconnecting the particular sites (not for user programming). **Do not use this parameter for programming a user procedure or executing the FLSH command from the hpt.**

`Functional changes` 里有两条跟本阶段直接相关的版本行为：SmarTest 7.1.3 起支持 MBAV8+；**SmarTest 7.1.4 起「HW of analog modules cannot be accessed when the master clock is switched off. An error is issued and the message is displayed in the report window.」**

### 3. 执行时循环

`02.06.07.01.08.04_Loops` 说明 sequencer 语言提供三类循环（Endless / Counted / Match），「that can be executed within any type of label」。

**边界**：循环的**组装**（在 testflow 里铺 loop 节点）属 `[[testflow]]`。本页只取「执行时怎么走」——即 `02.08.04.32.02.03_Running_a_testflow` 交代的 loop 运行时语义：

> The testflow variables and user flags are not reset at the end of each loop execution; they are only reset when the loop execution is first started, on the first loop iteration.

> If running a testflow in a loop, disconnect always occurs at the end of each run. If running individual test suites in a loop, disconnect does not occur, unless users program disconnect in the test method.

`02.08.04.32.02.03.01_Loop_configuration_settings` 补一条版本约束：**SmarTest 6.5.2 起，loop 配置在 testflow 或 test suite 执行期间不可更改。**

### 4. 报错条件

`02.06.03.01.11_Errors` 列出会报错的六种情形，其中三条属于本阶段的操作面：

> - a test is running
> - the programmed resources are not installed
> - the programmed resources are already in use
> - there is no device power supply installed in the system
> - **the sequencer is not in the OFF state**
> - the resistive divider value is out of range

## L2 — Test Method API

### 1. 设/读 flag（运行时控制与观察的主接口）

`02.07.03.08.07_Setting_Flags` 给出三对 setter：

| 任务 | API |
|---|---|
| Provide access to the testflow flag | `SET_TESTFLOW_FLAG(params)` |
| Provide access to the system flag | `SET_SYSTEM_FLAG(params)` |
| Provide access to the testsuite flag | `SET_TESTSUITE_FLAG(params)` |

同篇有一条**时序约束**（这是最容易踩的坑）：

> Change of any flag state will be valid when the next testsuite is executed.

`02.07.03.08.08_Obtaining_Status_of_Flags` 给出三对 getter：`GET_TESTFLOW_FLAG` / `GET_SYSTEM_FLAG` / `GET_TESTSUITE_FLAG`。

文档明确 `check_testmethod_api` 这一个 flag 的读写可以走 API（`02.08.04.32.01.02.07.02_Testflow_flags`）：

> You can also set this flag using `SET_TESTFLOW_FLAG` API (test method), or `SetTestflowFlag` API (CI_CPI). You can determine the current setting of the flag using `GET_TESTFLOW_FLAG` API (test method), or `GetTestflowFlag` API (CI_CPI).

### 2. `FLUSH` —— 把缓冲的设置刷下去

`02.07.04.01.69_FLUSH` 的 Introduction 说清了它刷什么：

> This API reflects the changes specified by the following APIs to the setup data or hardware: `ROUTING_STATUS`
> And also, this reflects the changes specified by the following APIs to the MCD (firmware level), but does not reflect them to the hardware: `PRIMARY_STATUS`, `TIMING_SPEC` / `LEVEL_SPEC` / `SPECIFICATION`

**它主要就是给调试用的**——文档原话：

> The operation of the FLUSH API is contained in the behavior of the `EXECUTE_TEST`, `START_TEST`, `DIGITAL_CAPTURE_TEST`, and `NB_DIGITAL_CAPTURE_START` APIs. Therefore, in most cases, you do not need to call this API. **Mainly, this API is used for debugging your test method program.**

> In the same manner as above, if you specify the change of the spec values by using the member functions of the `LEVEL_SPEC` or `TIMING_SPEC` API (or `SPECIFICATION` API for multi-port testing), the changes are reflected to the desired spec data when the FLUSH API is called. Therefore, **if you debug a test method program with the Spec Tool, and you want to reflect the changes before any of the APIs listed in the next paragraph is executed, call the FLUSH API. During debugging, you can also change the spec values with the Spec Tool.**

语法（文档给的 7 个重载，照抄）：

```cpp
void FLUSH();
void FLUSH(const TM::FLUSH_POST_ACTION action);
void FLUSH(bool force);
void FLUSH(TM::FLUSH_POST_ACTION action, bool force);
void FLUSH(TM::FLUSH_SECTION_TYPE flush_section);
void FLUSH(bool force, TM::FLUSH_SECTION_TYPE flush_section);
void FLUSH(TM::FLUSH_POST_ACTION action, bool force, TM::FLUSH_SECTION_TYPE flush_section);
```

**两条硬约束**（都写进「常见错误」）：

> When using the `FLUSH(TM::APRM)` option, if your application is changing the same spec variable, it must be called after each change command. However, If your application is changing different spec variables, the `FLUSH(TM::APRM)` only needs to be called once at the last line.

> `FLUSH()` should be called before elements which should be "flushed" get out of scope. For example, if the elements to be flushed are declared inside an "if{}" block, then FLUSH() must also be declared within the same block. Otherwise, placing the FLUSH() outside the block will cause a `FLUSH()` error to occur.

`02.06.02.02.124` 的 `FLUSH`（L1）与这条 `FLUSH`（L2）的**归属判断**：两者都是「让缓冲的设置生效」，且都明确服务于调试；文档把 L2 版本直接定位成「mainly for debugging your test method program」。**推断：按本 wiki 的分工，二者都归 `run`，`[[flsh]]` 与 `[[flush]]` 各建一页。**

### 3. 执行上下文

`02.06.07.01.08.05.03.02.03_Using_execution_contexts` 的 "Related Test Method APIs" 列出三个：`SEQUENCER_CONTEXT`、`SEQUENCER_CONTEXT_ITEM`、`INDEPENDENT_TEST`（Protocol Aware）。

### 4. 真正触发执行的 API

由 `FLUSH` 篇列出「改动实际反映到硬件」的 API 清单可知，本阶段实际起测的 L2 入口是：`EXECUTE_TEST`、`START_TEST`、`DIGITAL_CAPTURE_TEST`、`NB_DIGITAL_CAPTURE_START`、`FUNCTIONAL_TEST`。

### 5. 调试观察类

- `PUT_DEBUG` — `02.07.02.02.04.02_Setting_up_Flags_for_Debugging`：`debug_analog` flag 打开时，「the `PUT_DEBUG` API transfers information to the Signal Analyzer Tool if you have already opened that tool. Even if the Signal Analyzer Tool is not open, you can view transferred information when you open the tool later.」
- `PUT_DATALOG` — 同篇：需 `Log MX Waveforms` + `log events enable` + `output on pass/fail` 三个 flag 同时成立，才把含 array data 的波形数据送进 event data log stream。**数据侧细节属 `[[results]]`。**
- Console 里的调试命令 — `02.07.02.02.04_How_to_debug_a_universal_test_method`：「you can change and query the variable value and test method execution status with the C/C++ functions and test method APIs. For example, `p variable1` prints the value of variable1 and `p testmethod_api` executes the `testmethod_api` and prints the execution returned value.」
- 打印静态变量 — `02.07.02.02.04.03_How_to_print_static_variable_value_in_debugging` 给出三种写法：文件级 `print 'MyTestMethod.cpp'::variableInFile`、类级 `print 'MyTestMethod::variableInClass'`、函数级 `print 'MyTestMethod::myFunc()::variableInMemberFunction'`。

### 6. `check_testmethod_api` 的运行时效果

这两个 flag 的行为差异直接影响本阶段能否查出问题，抄原文：

> When the Check Test Method API flag is set to "on", the software checks the pin name parameter in the TEST API and the PUT_DATALOG API. If the specified pin name parameter is not an existing, defined pin name, **a fatal error occurs during runtime**. (You can handle an exception error generated by the Check Test Method API feature using the `SET_EXCEPTION_HANDLER`.)

> When the Check Test Method API flag is set to "off" (this is the default), the pin name parameter is not checked... In this case, the user can enter any string for the pin name parameter without a resulting error during runtime.

文档还给了**为什么应该打开它**的工程理由：拼错的 pin name 会让转成 STDF 的数据丢失 TEST / PUT_DATALOG 里的 pin name 信息，「This makes STDF results analysis impossible. Therefore, the Check Test Method API flag should be set to "on" if Standard Test Data Format (STDF) will be used for test result data analysis.」——注意末句的尾巴：**它只检查单个 pin name，不检查 pin group。**

## L3 — 外部控制

**这一层在语料里比 L1/L2 薄，但确实有，且能跑通。**

### 1. HVM API（SmarTest 既有，7.10.3 可用）

`02.09.01.10.01_HVM_API_Introduction`：

> The High Volume Manufacture Integration API provides a set of application programming interfaces which allow external programs to interface with the SmarTest execution environment.

四大类里与本阶段直接相关的是 **Test Execution API**：「These commands set a device and test program, control the execution of the test program, test flow and BLC, generate the related event and notify the event to SmarTest.」

`02.09.01.10.02_Controlling_test_execution_with_HVM_API` 明确说 SmarTest run 有三种控制方式，并给出取舍：

> - control the SmarTest running with Application model
> - control the SmarTest running with Batch/Lot Control
> - control the SmarTest running with HVM API `ExecTestflow()`.
>
> Application model is the legacy production environment that is widely in use. BLC can implement the same functionality as application model in C++ with much more flexibility. **The `ExecTestFlow()` API executes the testflow directly and is simple to use.**

同篇还给了一条**清理用的 shell 命令**（这是本阶段少见的、文档明写的命令行接口）：

> Test method executor is not automatically terminated after testflow executions or application model runnings. This can avoid losing the information generated in the test method execution. To explicitly terminate the test method executor to release all resources and get a clean environment for next execution, you can execute the following command in a shell:
>
> ```
> $/opt/hp93000/soc/testmethod/bin/tmm_console -e stopAll
> ```

HVM API 的能力面（同篇）：start/terminate SmarTest session、get session info、download and execute a test program or testflow、control the running of a BLC client、notify customer client status、get hardware information、query calibration status、monitor production status。

### 2. Test suite control API（SmarTest 6.5.2 引入，7.10.3 可用）

`02.09.01.14.02_Test_suite_control_API_reference` 的能力清单：

> - attach to a SmarTest session and an active testflow
> - **retrieve and change the settings and flags of test suites**
> - attach a universal test method to a test suite
> - create, setup, execute and delete a floating test suite
> - get the test suite on focus site or on active sites, **execute the test suite and query the execution status**

入口对象 `TestsuiteProxy`，另有 `initializeSession()` / `detachSession()` / `exitProcess()` / `getTestsuite()` / `getAllTestsuiteNames()` / `getSpecialTestsuite()` / `createFloatingTestsuite()` / `deleteFloatingTestsuite()` / `selectTestmethodExecutor()` / `getTestmethodExecutorIndex()` / `setSiteInFocus()` / `getSiteInFocus()` / `setActiveSites()` / `getActiveSites()`。

**推断**：`setSiteInFocus` / `setActiveSites` 与 `[[site-control-window]]` 是同一件事的外部化——L3 可以在不点 GUI 的情况下切 focus site 与 active sites。

### 3. SmartShell —— **7.10.3 不可用**

`02.15_SmartShell` 描述的能力完全对口本阶段：

> SmartShell is an external scripting interface for SmarTest that allows external tools (for example, EDA tools or shell scripts) to control the test execution and receive the test results back.

**但它的 `Functional changes` 写着「Introduced in SmarTest 8.2.5」。** 本 wiki 面向 SmarTest 7.10.3，**所以 SmartShell 在本版本不存在**。此处记录，是为了防止 agent 把它当成可选方案。

### 4. 中止/暂停（生产侧控制）

`02.09.01.07_Controlling_a_Production_Run` / `02.08.04.32.02.03_Running_a_testflow` 的 "What to do next" 给出四个按钮及其**运行时语义**：

| 按钮 | 语义 |
|---|---|
| `ABORT` | 「Aborts the running testflow immediately at the end of the current testsuite and **stops also the loop execution**」 |
| `RESET` | 「Aborts the running testflow immediately at the end of the current testsuite, stops the loop execution, returns the software to its initial state, and **resets the downloaded settings in the tester**」 |
| `ABORT TESTFLOW` | 「halts the execution of a device test between the testsuites of the device test. **The loop execution is not stopped**: This means that the next run is immediately started if the looped execution is enabled」 |
| `PAUSE` | 「This sets the PAUSE flag. The application model evaluates this flag immediately after the execution of a device test.」 |

**干净中止 looped test 的三步**（文档明写，且带一条禁令）：

> - Click the PAUSE button and wait until the end of the execution.
> - Click the ABORT button.
> - Return to the PAUSE dialog window and press the Quit button.
> Note The Break button (stop sign) does not abort the loop execution.

另有两条版本事实：SmarTest 7.1.0 引入 single step execution mode；**SmarTest 7.1.2 起 Stop on Fail 改为「sequence 中任一 test suite 出现 overall fail 结果就停」，Stop on Pass 改为「sequence 中全部 test suite 都 pass 才停」**。

## 产物

**文档未覆盖**「run 阶段新建 setup 文件」这件事——**它本来就不新建**。

文档事实：run 阶段会**改动**的 setup 文件只有一个，就是 `[[testflow-file]]`（`<device_dir>/testflow`）。`02.08.04.32.01.02.07.04_Test_suite_flags` 与 `02.08.04.32.01.02.07.02_Testflow_flags` 都写了这条回写规则：

> If you change a flag from Production Settings, all current flag values are written to the working copy of the test flow. The associated testflow is marked as changed. **Saving the testflow overwrites the original testflow with the working copy and the current values become the new initial values of the testflow.**

> The changes made from the Test Suite Flags tool only apply to the settings of the changed run in memory (working copy of the test flow). No configuration file is changed until the test flow is saved.

**这是本阶段最需要注意的副作用**：改 flag 是「改测试行为」，保存 testflow 就把这次调试的临时设置固化成了 testflow 的初始值。`02.08.04.32.01.02.07.01_Alphabetical_list_of_flags` 也提到 `x_mode` 一类 flag 对吞吐的取舍说明，进一步说明 flag 值本身是被当作 testflow 的一部分保存的。

本阶段真正产出的是**结果与日志**：

| 产物 | 位置/形态 | 出处 |
|---|---|---|
| Report window 输出 | 屏幕；软件异常关闭时写到 `/tmp/ReportWindow.dump` | `01.01.13_Report_window` |
| HWRE 硬件响应文件 | 目录在 Run 配置的 Response Emulator 区指定，可加时间戳 | `02.08.04.32.02.06.01` / `.03` |
| 数据日志 | 由 event data logging 决定；目录/文件名在 `/etc/opt/hp93000/soc_common/datalog/global.conf` 与 application model 里 | `02.08.04.32.02.03.04_Measuring_the_test_time` |

**结果的组织、日志格式、判定（pass/fail、bin、STDF/EDF）一律详见 `[[results]]`，本页不复制。**

硬件响应文件的命名规则（文档明写的格式，属本页产物范围）：

```
Testsuite;MAPI; call#; site#
```

- `Testsuite` — executed test suite
- `MAPI` — name of the used test method API
- `call#` — 「A counter corresponding to how many times the test method API is called from the test suite」
- `site#` — 「A query focus site number」

文档给的具体例子：`TS1;Analog.DGT("a_out").getWaveform(1);1;1` 对应 `TS1` 里 site 1 上第一次调 `Analog.DGT("a_out").getWaveform()`。注意文档特意提醒：「a hardware response file name contains a default input value even if the value was not set in the related API. This is the reason why the file name contains `Waveform(1)` even if "1" is not set for the API.」

**取数范围有限**：`02.08.04.32.02.06.04_Supported_test_suites_and_test_method_APIs` 列出 emulator 只模拟这些 API —— `ANALOG`/`ANALOG_STATUS` 类的 `DGT`（`getWaveform`/`getComplexWaveform`/`getDebugWaveform`）与 `TIA`（`getResult`/`getMean`/`getMin`/`getMax`/`getJitter`）、`Vector.getVectors`、`SpecSearch`（`getResultSpec`/`getPassVal`/`getFailVal`）、`DC` API（`PMU_IFVM`/`PMU_VFIM`/`DPS_VFIM`/`PPMU_MEASURE`/`DPS_TASK`/`SPMU_TASK`）、`FW_TASK`、`GET_FUNCTIONAL_RESULT`、`TEST`、`SEARCH_FUNC_TASK`、`PATTERN_CONTROLLER`。**「The emulator does not support other member functions of the above APIs.」**

## 验证

### 1. 跑完立即看：Flow Sequence Editor 与 Test Suites page 的着色

`02.08.04.32.02.03_Running_a_testflow` 的 `Results` 段，这是本阶段最直接的验收信号：

> The results of the testflow are displayed in the report window.
> In the Flow Sequence Editor, the passed test suite nodes are **green**, the failed nodes are **red**, and the bypassed nodes are **yellow**.

Test Suites page 的 `Result > Pass/Fail` 单元格着色规则（同篇表格）：

| 显示 | 含义 |
|---|---|
| Green background | Passed test suite |
| Red background | Failed test suite |
| Green border | The test suite set to pass |
| Red border | The test suite set to fail |
| Yellow border | The test suite set to bypass |

**关键补充**：

> If you edit the testflow after the execution, the borders of all test suites become **dashed lines**.

多 site 的两种显示（同篇）：

- Test Suites page 设为显示 all sites 时：「the Test Suite Name cell is green only when all sites pass. If one site fails, this cell is displayed with red borders.」
- 设为只显示 site in focus 时：「the test suite border changes color according to the result of the site in focus... irrespective of the results of the sites not in focus.」

### 2. 确认执行流真的按预期走

`02.08.04.32.02.03.03_Checking_the_execution_flow` 解决「多路径 testflow 里，器件走了哪条路」。文档给两种办法，第二种有完整 procedure：

> - Previously setting the pass/fail state for each test suite by using HW response files for execution.
> - Inserting different Assign Value nodes in each individual path of the testflow, and have these logged, for example, by defining them in various bin descriptions.

Procedure 要点：在每条路径插 Assign Value 节点，变量自增（`path_1 + 1`）；在目标 bin 节点的 Properties 里改 Description，写成 `path_1=@{path_1}, path_2=@{path_2}` 这样的表达式。

`Results`（文档原话）：

> After execution, the data log file contains an entry showing how many times the particular paths were taken.

**注意**：这里已经越到「结果文件」了。日志格式属 `[[results]]`；本页只确认「这条办法能回答『执行流对不对』」。

### 3. 确认 loop / 执行时间

`02.08.04.32.02.03.01_Loop_configuration_settings` 给出 `Log Loop Number` 的可见证据：

> When this option is enabled, a message is output to the report window at the beginning of each testflow loop iteration, similar to this one: `Executing Test Flow Loop Iteration: 2`

> The current testflow loop number is displayed with the first iteration numbered as 1. No message is output when executing the test suites in a loop.
> If multisite testing is also enabled, the loop number is reported only at the beginning of the first tested site.

`02.08.04.32.02.03.04_Measuring_the_test_time` 的 `Results`：「The timing information for the complete test and for every level of the application model appears in the report window.」前提是把 `debug_mode` testflow flag 设成 `3` 或 `4`。

**测时间前必须做的准备**（文档逐条列出，是「验证」而不是「建议」）：把 GDF 相关的 system flag 全设 `off`；`debug_mode` 设 3 或 4；线性 testflow 时把 `global_overon` 与所有 stop bin 的 Overon 都设 `on`；在 model file 里关掉不需要的特性；用 `sublevel_dialog` application model；**以 supervisor mode 启动**（「If you start it in engineering mode, for example, from the testflow editor, execution will be slowed down by background processes, for example, of the Pattern Debug Tool」）；数据日志写到本地；用 `ps -ef` 确认无多余进程。

文档还给了一条**读数的陷阱**：

> Note that the first run usually takes considerably longer than the following repetitions.

### 4. Debug view 上应该看到什么

`02.08.04.32.02.04.01_Single_step_testflow_debugging` 的 Examples 给出可对照的现象：

- 启动后 Debug view 打开，显示执行节点 `Testflow (Full)`，子条目为 `Ftest (Testsuite_1)`。
- 点 Step Over 后，「The `Ftest (Testsuite_1)` child entry changes to the `Ftest (Testsuite_2)`.」
- 单步起步阶段「A WARNING window is displayed.」

`01.01.08.06_Debug_View` 定义每个图标的语义（Restart / Resume / Suspend / Terminate / Step over），其中两条值得记：

> Resume — Click Resume to continue testflow execution with no stops **unless there are enabled breakpoints in a test method**

> Step over — Click Step over to execute exact one (next) test suite in testflow

### 5. test method 调试成功的判据

`02.07.02.02.04_How_to_debug_a_universal_test_method` 的 `Results` 只有一句，但它是本阶段 L2 的终点：

> Your test method is bug free and ready to use.

### 6. Hardware view 上的验证

`01.01.07.05.03_Hardware_view`：

> After executing the test method, click this button [Refresh], the hardware setting in this view will be updated to the settings in the test method.

也就是说：**跑完 → Refresh → 显示的应当是 test method 里设的值**，这是「下载是否生效」的目视校验。

`01.01.07.05.03.01_Executing_a_measurement` 的 `Results`：measurement 结果在 Hardware view 与 Measurement window 里显示，site in focus 与 all active sites 两种视图。

`01.01.07.05.03.02_Quick_measurements`：跑过一次 measurement 后，在 Hardware view 点 `Quick` 即可对 focus site 重复测量，「without opening the Measurement window」。

### 7. 离线跑时的验证

`02.08.04.32.02.06.02_Using_hardware_response_files_for_execution`：

> Run a testflow. At the beginning of the test execution, the Hardware Response Emulator window opens. Confirm that the hardware response directory and target test suites are set correctly. If the settings are correct, click OK.

`02.08.04.32.02.06.01` 的 `Results`：「The hardware response files storing the hardware response data are generated in the specified hardware response directory.」——**看目录里有没有文件生成**，是最直接的验收。

## 常见错误

debug 章材料很厚。以下全部来自文档明写，按**症状**组织。

### A. 单独跑 pass、放进 testflow 就 fail（driver 毛刺）

`02.08.04.32.01.02.07.01_Alphabetical_list_of_flags` 的 `sqst_mode` 行：

> You may encounter tests that pass when executed as standalone but may fail when executed within a testflow. A glitch on the drivers may be present between pattern bursts when viewed with an oscilloscope. **If you experience this situation, check the `sqst_mode` testflow flag.**

该 flag 打开时「The user defined break waveforms are temporarily overridden and the drivers are set to tri-state mode between all tests in the testflow」。文档另一处提醒：「Set to off in typical applications to avoid side effects with keep alive and test time.」——**它是诊断用的，不是常开的。**

### B. Test Method Debugger 不工作 / 断点被跳过

`02.07.02.02.04.01_Issues_to_affect_the_test_method_debugger` 一次列出五个诱因，每个都带 Action：

| 症状 | 诱因 | 处置 |
|---|---|---|
| 调试器不工作或丢断点 | 被调试的 .cpp 没 build 过 | 「The debugger debugs only test method codes that have been built successfully.」 |
| 同上 | build configuration 不对 | C/C++ perspective 里右键项目 → Properties → C/C++ Build page → Configuration 选 `Debug [Active]`；若没有这项，点 `Manage Configuration...` 建 |
| 同上 | 两个 .so 不一致 | 设备的 .so 在 `<device>/testmethod/`，被测 test method 项目的 .so 在 `<the debugged test method project>/Binaries/`；用 Properties view 对比。修法：Clean Project 删 `<device>/testmethod/` 下所有 .so → 重建 test method 项目 → 重建 device 项目 |
| 断点不生效 | 断点没 enable | Breakpoints view 里选中 |
| .hpp 里断点不生效 | 对应 .cpp 里没设过断点 | 「First, set a breakpoint in the corresponding .cpp file. Second, set the desired breakpoints in the .hpp file.」之后再移除 .cpp 里的断点 |

### C. 断住的进程不是新进程 / 单步卡死

`02.07.02.02.04_How_to_debug_a_universal_test_method` 里两条独立的坑：

> Note A process is started when you start executing a test method. **The process will not be stopped after the execution.** If the process is stopped exceptionally, it will be started next time when you execute a test method. You need to pay more attention to the testflow variables when you start executing a test method from exceptional termination. Otherwise you may get wrong test result.

> When you step into a line, the debugger may hang up for several seconds and then pop up the error "**Target request failed: Target is not responding (time out).**" To avoid this, set a break point at the line where the error occurred and **close the variables view before stepping into this line**.

调试器显示的源文件不对：

> If the source files of your different projects have the same name, it may happen that the wrong source file is shown in the debugger. You can solve this problem by checking the **Search for duplicate source files on the path** option in the Source page of the default test method debugger.

退出调试的两条路：再点一次 `Start Test Method Debug` 图标；或 **Run > Terminate TestMethod Execution**（主菜单，SmarTest 6.5.2 新增）。另有硬限制：「Only one SOC Test Method debug session can be run at a time.」

### D. 单步调试的固有限制

`02.08.04.32.02.04.01_Single_step_testflow_debugging`：

> **Limitation**: You cannot start a full testflow execution (default name: `Testflow (Full)`) in the single step mode.
> **Solution**: Select the first test suite and click `Run and Hold after here`. After a hold flag stops the testflow execution, you can continue with the single step mode.

同篇还有一条**工具选择上的劝告**——文档明确不建议用 hold flag 做调试，理由是四条具体缺陷：

> Note Advantest does not recommend using hold flags for debugging, because this procedure has the following disadvantages:
> - Hold flags in a testflow changes its content. **You may unintentionally save a testflow including the hold flags.**
> - During testflow execution, pop-up windows are displayed... They require user interaction to proceed or stop the testflow execution. **These pop-up windows may be displayed behind the main window of SmarTest** and, therefore, may be not visible at a glance.
> - To resume the execution of a paused testflow execution you have to **unset all remaining hold flags**.
> - After using `Run and Hold after here` you still need to set the hold flags for each test suite if you want to step through the test suites one by one.
> - **Running a loop execution step-by-step is not possible.**

注意第一条与「产物」一节呼应：**调试用的 flag 会被固化进 testflow 文件。**

### E. 选了 test suite 但结果不对：narrow vs wide selection

`02.08.04.32.02.01.11.01_Narrow_selection_and_wide_selection` 与 `02.08.04.32.02.03_Running_a_testflow` 共同给出规则：

- **narrow selection（只选节点本身、不含 sub-branch）**：「they are executed based on the current status. That is, **the execution of each test suite is affected by the result from the previously executed test suite**.」
- **wide selection（含 sub-branch）**：「the selected test suites are constituted as a temporary testflow. Actually this testflow is executed.」「Running a wide selection behaves like running a testflow but **ignores binning**.」

`01.01.08.06` 与 `02.08.04.32.02.01.11.01` 都给了同一句结论：

> **Note: For a consistent display of PASS/FAIL result, you will need the wide selection for debugging.**

切换方式：「you can click the node with Ctrl pressed, or directly click Ctrl + Right or Ctrl + Left」。

另外，`02.08.04.32.02.03` 里还有一条容易忽略的：**narrow 执行时若 testflow 选了 pattern master file，则只加载用到的 pattern。**

### F. 执行上下文并行失败

症状：**后来启动的 context 没启动，先跑的继续跑，并给出错误信息。** `02.06.07.01.08.05.03.02.03_Using_execution_contexts` 的三条：

> If an execution context A is running and you try to start another execution context B that shares a channel with A, an error message to this effect will be issued, and B will not be started. A will continue to run.

> If two execution contexts both contain a port with a DC Scale channel, they cannot be run in parallel. ... then an error message to this effect will be issued, and B will not be started. A will continue to run.

> Recalculation of the master clock period will stop all user defined sequencer tasks. Therefore, changes of the primary timing involving such a recalculation must be avoided between the start of two execution contexts that are to run in parallel.

若第一个用 `FTST?` 启动，第二个不会并行，只会等第一个返回 PASS/FAIL —— **这是「看起来没并行」的经典原因**。

### G. testflow 装载期就报错

`02.08.04.32.01.02.07.02_Testflow_flags` 的原文警告：

```
Testflow flag "<flag_name>" is not defined.
```

```
Warning: Invalid flag statement encountered in testflow file,
in the "flags" section:
The flag "<bad_flag_name>" is not defined.
Use the "user" keyword to define a user flag.
```

`02.08.04.32.03.05_Testflow_file` 的 "Range check of parameters"：文件是文本格式可以手改，但「we recommend changing the settings only by the Testflow Tool」；参数越界的后果是**整个 testflow 装载中止**：

```
".../TestFlow", line ##, near ";": error: [;] Flag ... must be between ... and ...
ERROR: cannot parse shm setting from testflow '.../TestFlow'
```

### H. FLUSH 报错

两条，都在 `02.07.04.01.69_FLUSH`：

- **FLUSH() error** —— 元素在 `if{}` 块内声明，FLUSH 写到了块外。「`FLUSH()` should be called before elements which should be "flushed" get out of scope.」
- **时钟被强制关闭的告警** —— 与 `FTCG` 冲突时：

```
FTCG ON was specified for at least one port which cannot be retained unchanged now.
							The command "Flush" forces a clock off, resulting in a stop of all channels.
```

另有一条属 FLSH（L1）：`FLSH` 的 `Functional changes` 记「SmarTest 7.1.4: HW of analog modules cannot be accessed when the master clock is switched off. An error is issued and the message is displayed in the report window.」

### I. Hardware view 给出不可信的读数

`01.01.07.05.03_Hardware_view`，**这条特别容易误导人，因为它不是报错而是「看起来正常的错值」**：

> In offline mode, the Hardware view cannot always return the correct settings of the hardware. This is especially true when hardware settings depend on pattern-based conditional jumps and match loops.
> If SmarTest determines that the state of the hardware cannot be evaluated correctly, "**WARNING: ... - reported last DC state ... may not reflect online state.**" is issued in the ui_report window.

### J. 时序图上看不懂的现象

`02.08.04.33.03_How_to_read_timing_diagrams__Unstable_signals` 给的典型：波形出现多次跳变或模糊。文档的解释是时钟不稳，且**三种分辨率的行为不同**——Standard Size「draws the standard diagram from a single execution only」，所以「The results, retrieved from functional test execution, can shift from run to run」；Double Size 是「from multiple executions (800 points across 10 cycles)」；Scope Size 是「from 35 VOL levels, with 800 pts across 10 cycles each」。

**推断**：看到「同一波形跑两次不一样」时，第一条要查的不是 pattern，而是时序分辨率模式与时钟稳定性。

### K. 从失败 test suite 快速跳到源头

`01.03.03.01.01_Debugging_test_methods__Finding_and_moving_to_information` 给了一套定位入口（这是「排查入口」而非「原因」）：

- Test Suite tab 上：Annotation toolbar 按钮 / `Ctrl+.` / 点 annotation bar 的 marker → **快速跳到失败 test suite**
- `F3` → test suite → 源码 → 函数 → 声明，逐级下钻
- Task view / Bookmarks view / Breakpoints view 里选中行点 `Go to` → 跳到 test method 里对应行
- Search results view / Error log / Problems View 里**双击**消息行 → 跳到 test method 对应行

`01.03.03.01.02_Debugging_patterns_efficiently` 给 pattern 侧的对应路径：Properties view 里选 `Test Suite > Primaries > Pattern` → `F3` → Pattern explorer 打开 → 选失败的 pattern → 再 `F3` → 在 Pattern editor 里打开相关 pattern 或 subroutine。之后用 `Ctrl+.` 跳下一个 annotation、`Ctrl+L` 跳到信号或周期、`Ctrl+F` / `Ctrl+J` / `Shift+Ctrl+J` 查找。

### L. 模拟 crash 时的 site 去向

`02.08.04.32.01.02.07.01` 的 `tm_crash_as_fatal`：

> off (0) All sites of the current test suite are sent to the otherwise bin if they have not already been binned... on (1) All sites that have not already been binned are aborted and sent to the otherwise bin. **Lot testing is aborted and needs user interaction to restart production.**

**bin 的具体语义属 `[[results]]`；此处只记「crash 时 site 去哪」这个运行时行为。**

## 下一步

跑完就进 `[[results]]`。

**为什么是它**：`02.08.01.01.05` 的第三步是「If there are some bugs in the test, fix them and then execute it again」——**修 bug 再跑是本阶段内部的循环**，它不产生新的阶段。真正把流程往前推的是「结果已经拿到了」这个事实：`02.08.01.01.05.02_Test_Debugging_and_Data_Logging` 说观察测试结果的动作是「activating the boxes in the Report Dialog window opened from the report window」，而 `02.08.04.32.02.03_Running_a_testflow` 的 `Results` 第一句也是「The results of the testflow are displayed in the report window」。

也就是说，**本阶段的终点（结果出现在 report window / 日志里）正是下一阶段的起点**。结果怎么组织、用什么格式落盘、pass/fail 与 bin 怎么判、多 site 结果怎么合——这些都在 `[[results]]`。

同时提醒两条跨页线索：

- Timing Diagram Tool 与 Error Map Tool 在本页是**定位问题的手段**（看波形、找失败 label/cycle），在 `[[results]]` 里才是**结果数据的呈现格式**。两页都会链到 `[[timing-diagram-tool]]` / `[[error-map-tool]]`，但论述角度不同。
- 本阶段改过的 flag 会被保存进 `[[testflow-file]]`，成为 testflow 的初始值。`[[results]]` 里做数据判定时如果发现「和上次跑的不一样」，**先回头看 testflow 文件里的 `flags` 与 `test_suites` 段是不是被调试时的临时设置固化了**。
