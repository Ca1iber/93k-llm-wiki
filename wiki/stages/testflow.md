---
type: stage
title: Testflow 组装
tags: []
related: ["run", "testmethod", "pattern", "pin", "level", "timing", "project", "results"]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32_Testflow_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01_Introduction_of_the_Testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.01_Testflow_methodologies.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02_Testflow_components.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01_Test_suites.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.01_Run__and__Run_and_Branch__test_suites.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.03_Floating_test_suite.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.04.01_Inserting_a_Multibin_SmartDisconnect_test_suite.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.02_Flow_control_nodes.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.02.01_Built-in_functions.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.03_Assign_Value_node.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.04_Print_nodes.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.05_Group_node.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07_Flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.02_Testflow_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.03_Testflow_flags_for_data_logging.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.04_Test_suite_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.05_Site_control_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.06_Flag_priority.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.03_Hierarchy_within_a_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.04_Multiple_Sites_Execution.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02_Using_the_Testflow_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01_Editing_a_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.01_Opening_the_Testflow_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.02_Creating_a_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.03_Selecting_setup_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.04_Inserting_a_test_suite_into_the_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.04.03_Creating_a_floating_test_suite.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.05_Inserting_a_bin_into_the_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.06_Editing_a_test_suite_in_the_Flow_Data_Editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.01_Defining_variables.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.15_Importing_a_testflow_from_a_CSV_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.16_Exporting_a_testflow_to_a_CSV_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.03_Checking_the_execution_flow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.05_Merging_the_testflows.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.05.01_Source_and_target_testflows.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03_Elements_of_the_Testflow_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01_Flow_Data_Editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.01_Test_Suites_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.04_Bins_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.07_Setups_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.08_Information_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.03_Synchronization_between_the_Flow_Data_Editor_and_the_Flow_Sequence_Edito.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.04_Testflow_Properties_view.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06.01_Top-level_control_structures.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.01_Concept_of_the_Setup_Management_Tool.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.03_Using_the_Setup_Management_Tool_from_the_Command_Line.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05.01_Collision_handling_for_the_level_master_file.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05.04_Collision_handling_for_the_testflow_master_file.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.05_Loading_a_testflow_and_all_setup_components.md
  - 01_Getting_started/01.03_Using_SmarTest/01.03.04_Working_with_testflows_efficiently.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.04_Task_4__Setting_up_a_Test.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.05.01_Setting_up_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.06_Task_6__Executing_a_Test_Flow_and_Obtaining_the_Results.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.04_STPM_merge_rules_file.md
  - 02_System_reference/02.06_Command_Reference/02.06.07_Vector_Setup_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04_Loops.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05_Command_Set_Programming_Interface.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.01_Flag_Classifications.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.02_Access_Routines.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.02.02_Production_Flags.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.02_Testflow_Flag.md
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# Testflow 组装

> 把已经做好的 setup 文件、test suite、bin 和流程控制节点，组装成一个能完整测一遍器件的 testflow。

## 目的

文档原文（`02.08.04.32`）：Testflow Tool 用于 "develop and debug a testflow"。本页只取其中的 **develop**（组装）；debug 属 `[[run]]`。

文档对 testflow 本身的定义（`02.08.04.32.01`）："A testflow is an interconnected collection of individual tests, each one testing a particular parameter. These tests can be interconnected in a multitude of different ways - sequentially, dependent on the previous/another result, while something is valid, etc. Together, all these tests form the complete test of your device."

本阶段要交付的四件事，原文列在 `02.08.01.01.04_Task_4__Setting_up_a_Test`：

- Specify all setup data files used in the whole device tests.
- Insert a test suite.
- Specify the primary sets and vector label to be used.
- Select one of your test method programs.

开发范式是 top-down（`02.08.04.32.01.01`）："consider the flow of tests you want to perform, create the flow based on the test suites, and then fill in the details for each test suite"。

**本页与 `[[run]]` 的分界。** 判据是「组装 vs 执行」：哪些 test suite、什么顺序、什么条件分支、用哪组 primary set —— 属本页；build、execute、看波形、停下来改 —— 属 `[[run]]`。文档自身也是这么切的：Testflow Tool 的两个编辑器（Flow Data Editor / Flow Sequence Editor）负责组装，"Running a testflow"、"Debugging a testflow"、"Hardware Response Emulator" 三节另立。本页凡涉及执行侧的现象，都显式标出需 `[[run]]`。

## 前置条件

逐条列出，各自注明出处：

1. **93000 Setup perspective 已打开** —— `02.08.04.32.02.01.01` 的 `Before you begin`："Make sure that the 93000 Setup perspective is opened."（Test Program Explorer 视图在其中，Testflow Tool 从这里打开）。见 `[[project]]`。
2. **全部 setup 文件已创建** —— 文档事实：`02.08.04.32.02.01.03` 的 `Before you begin` 要求 "the setup files have been created"；同页 `Functional changes` 记明 **SmarTest 6.5.2 起："You cannot create setup files with the Testflow Tool."** 即 `[[pin]]`、`[[level]]`、`[[timing]]`、`[[pattern]]` 四步必须先完成，本阶段只是把它们**挂进** testflow，不是造它们。
3. **所需 test method 已 build** —— 文档事实：`02.08.04.32.02.01.02` 的 `Before you begin`："All the required test methods have been built."；`02.08.04.32.02.01.04` 的 `Before you begin`："the required test method has been built."。见 `[[testmethod]]`。
4. **primary setup files 已加载** —— 文档事实：`02.08.04.32.02.01.04` 与 `02.08.04.32.02.01.04.03` 的 `Before you begin` 都要求 "the primary setup files have been loaded"。加载动作本身在本阶段做（见下「产物」前的流程）。
5. **要用 flow control node 前，变量必须先建好** —— 文档事实：`02.08.04.32.01.02.02` 的 Note："Before you can use flow control nodes you have to create variables"。
6. **device 目录中已有 testflow 项** —— 文档事实：`02.08.04.32.02.01.02` 说明 New Testflow 窗口里 "The directory of the testflow file is automatically set to device_directory/testflow and uneditable"。见 `[[project]]`。

**推断：** 上述 2–4 的顺序是硬的 —— 文档把「选 setup 文件」放在「插入 test suite」之前（`02.08.04.32.02.01.02` 的 Procedure 就是先 Setups page 后 Flow Sequence Editor），因为插入 test suite 时要填的 timing/level/analog set 号和 pattern 名都来自已加载的 setup 文件。

## 涉及对象

| 对象 | 层级 | 在本阶段干什么 |
|---|---|---|
| `[[testflow-tool]]` | gui | 组装 testflow 的主工具，"used to develop and debug a testflow" |
| `[[flow-data-editor]]` | gui | 表格视图，八页（Test Suites / Parameters / Tests / Bins / Variables / Flags / Setups / Information）。挂 setup 文件、批量改属性、设 flag 在这里 |
| `[[flow-sequence-editor]]` | gui | 流程图视图。**插入节点的唯一入口**（Palette 上的 Run Test / Run and Branch / goodbin / badbin / Multi Bin 等） |
| `[[testflow-properties-view]]` | gui | 显示并编辑当前选中元素（test suite、bin、group、flow control node、Assign Value node、Print node）的属性 |
| `[[testflow-file]]` | file | testflow 的存储文件，位于 `<device_dir>/testflow`。两个编辑器处理的是同一个文件 |
| `[[testflow-master-file]]` | file | 把 testflow 拆成多个子文件时的主文件，供多人并行开发 |
| `[[test-suite]]` | n/a | 本阶段的基本积木。含 timing/level set、equation 和一组 test suite flag |
| `[[bin]]` | n/a | 分选落点。stop bin / otherwise bin / floating bin 三类 |
| `[[flag]]` | n/a | 三级 flag（system / testflow / test suite）+ site control flag，见下方专段。**`flag` 是概念页，不落在任何一层接口**（`concept` 是页面类型，不是层——§6 的层值是 `L1\|L2\|L3\|file\|gui\|n/a`） |
| `[[flow-control-node]]` | gui | if…then / repeat…until / while…do / for…do，testflow 的分支与循环 |
| `[[assign-value-node]]` | gui | 在流程某点给变量赋值 |
| `[[print-node]]` | gui | 往 Report window（Print）或 Datalog（Print to Datalog）插注释 |
| `[[group-node]]` | gui | 把同一层级里连续若干节点收成一组，便于阅读 |
| `[[built-in-functions]]` | gui | 在 flow control 条件里取内部数据：`pass()` / `fail()` / `has_run()` / `tf_result()` / `lsus()` / `tsus()` 等 |
| `[[testflow-variable]]` | file | testflow 变量，分 Userflag / String / Double 三型 |
| `[[setup-management-tool]]` | gui | `smartest_mfh`，对 testflow master file 做 assemble / split |
| `[[ci-cpi]]` | L3 | Command Set Programming Interface，运行期读写三级 flag 与变量 |
| `[[stpm]]` | L3 | SmarTest Program Manager，把 testflow 合并进 master test program |

### flag 的三级（本阶段的实质内容之一）

文档事实（`02.08.04.32.01.02.07`）："The Testflow Tool provides four types of flags for debugging and controlling the execution of a test." —— testflow flags、testflow flags for data logging、test suite flags、site control flags。

三级各自的**设置位置、生效范围、存储位置**：

| 级别 | 在哪里设 | 生效范围 | 存在 testflow 文件的哪一段 |
|---|---|---|---|
| system flag | Flags page（`02.08.04.32.03.01.06`） | 整个测试程序 | `flags` section（`02.08.04.32.03.05`） |
| testflow flag | Flags page（同上） | 单个 testflow | `flags` section |
| test suite flag | Test suites page 或 Properties view 或右键 Test Flags（`02.08.04.32.02.01.06`） | 单个 test suite | `test_suites` section |
| site control flag | 同上（Test suites page） | 单个 test suite（多 site 相关） | `test_suites` section |

来源：`02.08.04.32.03.01.06`（"On this page, you can set the system flags and testflow flags"）、`02.08.04.32.01.02.07.02`（"The testflow flags are stored in the `flags` section"）、`02.08.04.32.01.02.07.04`（"The test suite flags are stored in the `test_suites` section"）、`02.08.04.32.01.02.07.05`（同上）。

**优先级**（文档事实，`02.08.04.32.01.02.07.06`）：

- "Should a pass level and fail level in the testflow flags be in conflict, the pass level has priority."
- "The individual test suite flags, Set pass, Set fail and Bypass have priority over the global testflow flags."

**默认值**（文档事实，`02.08.04.32.01.02.07.04`）："By default, all test suite flags are inactive."

**改动的落盘时机**（文档事实，`02.08.04.32.01.02.07.04`）：从 Production Settings 或 Testflow editor 改 flag，只改内存里的 working copy，testflow 会被标成 changed；**保存 testflow 才写回原文件并成为新的初始值**。

**注意边界：** flag 的调试用法（`global_hold` 单步、`hold_on_fail` 停在失败处、`debug_mode`）属 `[[run]]`。本阶段只负责「在哪一级设、设成什么、什么时候生效」。系统 flag 与 testflow flag 也可从 Operation Control 窗口（经 Production Settings，engineering mode）访问，但文档要求 "To actually make changes to the flags, all windows must be set to Testflow settings mode (not to Production settings mode)"（`02.08.04.32.03.01.06`）。

**建议：** 组装阶段先把 flag 全部留默认，等 `[[run]]` 阶段按调试需要再开 —— 文档只说 flag 影响执行期行为，没有要求组装时定死。

## L1 — Firmware / Setup Command

文档未覆盖

说明（**推断**）：通读 `02.06_Command_Reference` 全章的目录后，**没有任何一条固件命令以 testflow 为主语** —— `02.06.07` 虽名为 "Loops"，实为 `02.06.07_Vector_Setup_Commands`（Vector Setup Commands），其下的 `Loops` 是**定序器**层的 `LBGN`/`LEND`/match loop，属 `[[pattern]]`，不是 testflow 的 if/repeat/while/for。testflow 是 setup 层的软件构造（文件首行 `hp93000,testflow,0.1`），组装动作全部通过 Testflow Tool 落到 testflow 文件，没有对应的固件命令可给示例。

同样，`02.06.07.01.08.05.03.02.03_Using_execution_contexts`（`SQEC` / `SQST RUN` 并行执行 context）虽与「流程」二字沾边，但它是**运行期并行执行**的机制，归 `[[run]]`，本阶段不涉。

## L2 — Test Method API

test method 是「被 testflow 调用」的一方。**推断：** L2 侧只能读写 flag/变量、选 bin，**不能改流程结构** —— 文档里没有任何 test method API 能增删 testflow 节点。

| API | 作用 | 出处 |
|---|---|---|
| `SET_TESTFLOW_FLAG` / `GET_TESTFLOW_FLAG` | 读写 testflow flag | `02.08.04.32.01.02.07.02` |
| `SET_TESTSUITE_FLAG` / `GET_TESTSUITE_FLAG` | 读写 test suite flag | `02.08.04.32.01.02.07.04` |
| `SET_USER_FLAG` / `GET_USER_FLAG` / `GET_USER_DOUBLE` / `GET_USER_STRING` | 读写 testflow 变量 | `02.08.04.32.02.01.12.01` |
| `SET_MULTIBIN` | 在 test method 里指定 multibin 落到哪个 bin | `02.08.04.32.02.01.05` |
| `GET_DISCONNECT_CONTEXT` | 判断本 test method 是作为普通 test suite 还是 Multibin SmartDisconnect test suite 在跑 | `02.08.04.32.01.02.01.04.01` |

最小可用示例（从 `02.08.04.32.02.01.12.01` 抄录，读一个 double 型 testflow 变量）：

```cpp
    ...
    DOUBLE print_example ;
    GET_USER_DOUBLE("X", &print_example);
    report_stream << "User-defined variable: " << print_example << endl;
    ...
```

`SET_MULTIBIN` 的示例（从 `02.08.04.32.02.01.05` 抄录，多 site 分 bin）：

```cpp
bool passed=true;

ON_FIRST_INVOCATION_BEGIN();
    CONNECT();
    FUNCTIONAL_TEST();
ON_FIRST_INVOCATION_END();

if (!TESTSET().cont(true).judgeAndLog_FunctionalTest())
//Functional results are cached for each site by the API
    {SET_MULTIBIN("abc", 12);
    //The devices which fail at the first functional test fall in bin 12.
    passed = false;
    }
```

文档事实：`SET_MULTIBIN` 选的 bin 必须已在 testflow 或 test table 里定义；**若 SET_MULTIBIN 选的 bin 不存在，multibin 对象会落到 otherwise bin**（`02.08.04.32.02.01.05`）。

## L3 — 外部控制

### CI_CPI — Command Set Programming Interface

文档事实（`02.09.01.08.05`）："The Command Set Programming Interface (CPI) provides a set of routines for accessing SmarTest flags and variables during the execution of a test program, plus a number miscellaneous utilities."

**这是三级 flag 的外部读写口**，`02.09.01.08.05.02.02_Production_Flags` 给出完整签名。
**下面 10 个函数的顺序与签名逐字照 raw，没有重排**（每组五个：Testsuite → Testflow → System）：

```
long GetTestsuiteFlag(char *tsname, char *flag, long *value)
long GetTestsuiteFlagOfSite(char *tsname, char *flag, long site, long *value)
long GetTestflowFlag(char *flag, long *value)
long GetSystemFlag(char *flag, long *value)
long GetSystemFlagOfSite(char *flag, long site, long *value)

long SetTestsuiteFlag(char *tsname, char *flag, long value)
long SetTestsuiteFlagOfSite(char *tsname, char *flag, long site, long value)
long SetTestflowFlag(char *flag, long value)
long SetSystemFlag(char *flag, long value)
long SetSystemFlagOfSite(char *flag, long site, long *value)
```

> ⚠️ **本页这一块 2026-09-20 更正过**（建 `mapping-testflow` 时查出来的）：
> 原写法把函数按 Testflow → System → Testsuite 重排了，**并且漏了 `SetSystemFlagOfSite`**——
> 只列了 9 个，raw 里是 10 个。**重排与漏项都违反了「条目原样转录、不重写」**（§2.7 对版本页的规矩，
> 本页引签名同理）。**根因是照抄时按「哪个是主角」排了序**——本页主角是 testflow，
> 于是 Testflow 那两个被提到了最前。**排序看起来只是排版，实际上是把语料的组织顺序换成了我的。**
>
> ⚠️ **另记一处语料自身的不一致，本页没替它改**：`SetSystemFlagOfSite` 的最后一个参数
> 在 raw 里是 `long *value`（**指针**），而它同组的另外四个 Set 例程都是 `long value`。
> **本页按 raw 逐字抄成 `long *value`**，不判哪个对。

`02.09.01.08.05.04.02_Testflow_Flag` 另给 flag 的符号常量（`*CI_SET_PASS_LEVEL`、`*CI_SET_FAIL_LEVEL`、`*CI_SET_BYPASS_LEVEL`、`*CI_HOLD_ON_FAIL`、`*CI_DEBUG_MODE`、`*CI_GLOBAL_PARALLEL` 等），全部标 R/W。

文档事实：set 例程会做范围校验，"the value passed on by the user is validated to ensure that the range of the flag is not exceeded"（`02.09.01.08.05.02`）。

### Setup Management Tool CLI

文档事实（`01.01.07.02.02.04.03`）：可执行文件名为 `smartest_mfh`，位于 `/opt/hp93000/soc/com/SETUP_MAN`。模式有 `assemble`（把 master file 里的子文件合并成 tester file 并下载）、`split`（反向拆分）、`assemble_all` / `split_all`（对 device 目录下所有 master file）、`create`（建空 master file，此时必须给 `<file_type>`）。`<file_type>` 的可取值为：

```
level, timing, analog_control, waveform, routing, testflow, testtable
```

`testflow` 是其中之一 —— 这是 testflow 组装在命令行上的入口。

文档事实（`01.01.07.02.02.04.01`）：SmarTest 自身不支持这些 setup 组件的 master file 概念，所以 Setup Management Tool **必须先把子文件合并成单个 setup 文件才能下载进 tester memory**；反向保存时要再拆开，以便只回写被改动的部分。

### STPM — SmarTest Program Manager

文档事实（`02.09.02.03.01`）：STPM control file 里 `mtp_device_testflow` 指定要合并进去的 testflow；文档给的例子是 `mtp_device_testflow = '/home/user/93K_Device/project.tf'`。control file 是 Python 文件（"It's structure follows the conventions of the Python programming language"）。

文档事实（`02.09.02.04`）：merge rules file 用于 "fine-tune how test are integrated into existing master test programs (MTP)"，其中 `overwrite_flow_var_value` 是专门针对 testflow 变量的规则；未指定 merge rules file 时用默认规则集。

### SmartShell / HVM

文档事实：`02.15_SmartShell` 与 `02.09.01.10_HVM_API` 两章存在，但**两处都没有给出「组装 testflow」的接口**（HVM 面向的是测试执行的控制）。

**补：Test suite control API 的 flag 读写**（`02.09.01.14.02.01.17` / `.33`）

文档事实：`getTestsuiteFlag()` / `setTestsuiteFlag()` 是 test suite 级 flag 的外部读写口。
与上面 CI_CPI 的 `GetTestsuiteFlag` / `SetTestsuiteFlag`（`02.09.01.08.05.02.02`）
**是两套不同的接口**，都作用于 test suite flag：CI_CPI 从 testflow 程序内访问，
TestsuiteProxy 从外部客户端访问。不要把它们当成同一个。

**补：产物文件接口**（[[tpi-program-routines]]）

`DataManager`（`02.09.01.09.02`）的 `dm_testflow` = testflow 文件，配 `dm_copy_in` 等操作；
STPM control file 的 `mtp_device_testflow` 也指向 testflow 文件——**三套通道都指向同一个
`.tf` 产物**，见本页「产物」小节。

**建议：** 本阶段的 testflow 组装走 Testflow Tool（人）或直接改 testflow 文件 / `smartest_mfh`（自动化），不要指望 HVM 或 SmartShell。

## 产物

### 主产物：testflow 文件

文档事实（`02.08.04.32.03.05`、`02.08.04.32.03`）："the testflow file which is located in the `<device directory>/testflow` directory"。新建时目录自动设为 `device_directory/testflow` 且**不可编辑**（`02.08.04.32.02.01.02`）。

device directory 的实际结构里确有 `testflow` 子目录，见 `01.07.01.01.01` 的 `ls -al` 输出。

**文件扩展名 —— 文档自相冲突，两说并列（按 schema §10，不自行选一个）：**

- **`.tf`**：STPM control file 的例子写作 `mtp_device_testflow = '/home/user/93K_Device/project.tf'`（`02.09.02.03.01`）；迁移工具的例子里是 `device_directory/testflow/functional.tf`（`03.12.09.01`）；其他出现处如 `mtp_device/testflow/mtp_device.tf`、`/prj/MTP/testflow/rel.tf`。这些语境都是**设备目录里那个被加载/执行的 testflow 文件**。
- **`.tfl`**：B2A 配置页把 testflow 文件写作 `tfl_file demo.tfl`，并称 "all input files except the timing setup file are determined by the testflow file demo.tfl"（`02.11.02.04.04`）。

**推断：** 两说可能指向不同东西 —— `.tf` 是设备目录里那个 tester file；`.tfl` 另有明确出处是 **Setup Management Tool 自动生成的子文件命名格式 `group_<group_name>.tfl`**（`02.08.04.32.03.06`），master file 例子里的 `files/general.tfl`、`files/vars.tfl`、`files/group1.tfl` 都是子文件。即：`.tfl` 主要活在 master file 的子文件语境，`.tf` 活在设备目录语境。**但 B2A 页确实把 testflow 文件叫 `.tfl`，这一条无法用上述区分解释。** 两条证据都是文档原文，未实机核对，`verified: doc-only`。

### testflow 文件的格式

文档事实（`02.08.04.32.03.05`）：首行是 `hp93000,testflow,0.1`，随后是若干 section。BNF 里
每个 section 的写法都是 `X <x_section> end |`，可用的 section 名（**按原文顺序**）是：

`information`、`declarations`、`flags`、`tests`、`testfunctions`、`datasets`、`test_suites`、
`initialize`、`download`、`abort`、`pause`、`reset`、`exit`、`test_flow`、`binning`、
`context`、`hardware_bin_descriptions`

> **这里原先是代码块，已改**（2026-09-18）。原文的 BNF 是
> `information <information_section> end |` 一行一条，本页初版**把 `<…_section> end` 全删掉、
> 再用 `|` 拼成三行**塞进代码块——**那是我的改写，不是原文**，代码块又暗示逐字。
> 现在名字照抄、形式说明白，**别把这张名单当成原文的排版**。

其中：

- `test_flow` section 装流程本体：`run()` / `run_and_branch() ... then ... else ...` / `if...then...else` / `while...do` / `for...do` / `repeat...until` / `print()` / `print_dl()` / `stop_bin(...)` / 变量赋值。
- `test_suites` section 装每个 test suite 的 `override_*`（timing/level/analog set、seqlbl、testf）与 `local_flags`。
- `flags` section 装 system flag 与 testflow flag。
- `binning` section 装 otherwise bin。
- `context` section 装挂进来的各 setup 文件（`context_levels_file`、`context_timing_file`、`context_vector_file`、`context_config_file` 等）。

文档事实：**Init test suite 与 Download test suite 不出现在 Flow Sequence Editor 的节点里**，但出现在 Flow Data Editor 的 Test Suites page 末尾（`02.08.04.32.01.02.01.02`）。七种 special test suite：Init、bin_disconnect、Abort、Reset、Pause、multi_bin_decision、Exit、Download（同页）。

### 主文件（拆分存放时）

文档事实（`02.08.04.32.03.06`）：首行必须是 `hp93000,testflow_master_file,0.1`，第二行 `testerfile: <tester_file_name>`。能拆出去的最小部件是：test suite groups、information、flags、bins、setup、variables。

**关键约束（文档原文）：** "Note that individual test suites or bins cannot be stored in separate files. Therefore, all top level objects must be groups." —— 单个 test suite 或 bin **不能**单独存文件，所以顶层对象必须是 group。

自动生成的子文件名格式为 `group_<group_name>.tfl`，可用环境变量 `VERIGY93000_MFH_PREFIX` 加自定义前缀。top-level 还支持 `if` / `for` / `while` / `repeat until` 控制结构，这些结构在 split 时被忽略（`02.08.04.32.03.06.01`）。

### 其他产物

- **CSV 导出文件**（`02.08.04.32.02.01.16`）：Test Program Explorer 右键 testflow → Export，可导出 Testsuites / Parameters / Tests / Bins / Variables / Flags 等内容，用于存档与交付。
- **CSV 导入**（`02.08.04.32.02.01.15`）：反向操作，可 "build testflows based on other testflows or to exchange testflows among different test system platforms"。注意导入时 Setups 列表**任何一项都不能取消勾选**。
- **testflow 图形打印**（`02.08.04.32.02.01.13`，文档列有此主题，本页未展开）。

**三层对照表见 [[mapping-testflow]]** —— GUI 操作 ↔ 文件 ↔ L1 命令 ↔ L2 API ↔ L3 接口 的按目的对照
（`wiki/mappings/mapping-testflow.md`；证据分三档写明，**`?` 与 `—` 不同义**：前者是「本页没找到证据」，
后者是「这一层不存在这个对应物」）。

## 验证

**文档未提供一条「跑一下看对不对」的组装期校验命令。** 以下全部是文档里明写的 `Results` / `What to do next` 段落与 GUI 上的既有指示，未自行发明：

1. **每个 Procedure 都带 `Results` 段**，可逐条对照：
   - `02.08.04.32.02.01.02` → "The testflow has been created." / `What to do next`: "Debug the testflow."（→ `[[run]]`）
   - `02.08.04.32.02.01.03` → "The setup files for the testflow have been selected."
   - `02.08.04.32.02.01.04` → "A test suite has been inserted in the testflow."
   - `02.08.04.32.02.01.05` → "The bin has been inserted in the testflow."
2. **Setups page 的黄底**（文档事实，`02.08.04.32.03.01.07`）："Invalid setup files are highlighted with yellow (the setup files have not been loaded or do not exist)." —— 挂完 setup 文件后，Setups page 上不应有黄底。
3. **Test suites page 的黄底**（文档事实，`02.08.04.32.02.05`）：合并后若 primary settings 在目标 testflow 里无效（例：引用了目标 timing setup 文件里不存在的 spec 号），"its entry in the Test suites page highlighted in yellow"。组装完不应有黄底。
4. **两个编辑器自动同步**（文档事实，`02.08.04.32.03.03`）："The Flow Data Editor automatically keeps the test suite in focus synchronized with the Flow Sequence Editor, and vice versa."—— 可以用它交叉核对同一个 testflow 的表格视图与流程图视图是否一致。不生效时查 `02.08.04.32.02.07` 的配置。
5. **打开时的版本警告**（文档事实，`02.08.04.32.02.01.01`）：若启用了 "Check UTM test method library version when opening testflow editor" 偏好项，打开 testflow 时会检查所用 test method 库是否基于当前 SmarTest 版本构建，不符会弹警告。这是组装期能拿到的早期信号。
6. **Test Suites page 的 Result 列边框**（文档事实，`02.08.04.32.03.01.01`）：执行后，宽绿=passed、宽红=failed、窄绿=被 set to pass、窄红=被 set to fail、窄黄=被 bypass；**改过 testflow 之后所有边框变虚线**。⚠️ 这是执行后的现象，属 `[[run]]`，但它是「组装对不对」最直接的反馈。
7. **检查执行流程**（`02.08.04.32.02.03.03`）：在每条路径上插 Assign Value 节点累加计数，再在 bin 的 Description 里用 `path_1=@{path_1}, path_2=@{path_2}` 记进 datalog —— 文档给了这个方法，但它需要执行才能看到结果，归 `[[run]]`。

**建议：** 组装期的自检只能做到 2、3、4、5 四条静态检查；流程逻辑对不对必须留到 `[[run]]`。

## 常见错误

**症状：加载 testflow 报解析错。** 文档原文（`02.08.04.32.03.05`）：testflow 文件是文本文件，**可以直接用文本编辑器改，但文档建议只用 Testflow Tool 改**。参数越界会导致加载中止，ui_report 窗口出现：

```
".../TestFlow", line ##, near ";": error: [;] Flag ... must be between ... and ...
ERROR: cannot parse shm setting from testflow '.../TestFlow'
```

排查入口：检查 `flags` section 里各 flag 的取值是否超范围。

**症状：flag 未定义的警告。** 文档原文（`02.08.04.32.01.02.07.02`）：

```
Testflow flag "<flag_name>" is not defined.
```

以及 flags section 里写了未定义 flag 时：

```
Warning: Invalid flag statement encountered in testflow file,
in the "flags" section:
The flag "<bad_flag_name>" is not defined.
Use the "user" keyword to define a user flag.
```

排查入口：自定义 flag 要用 `user <user_flag_name> = <value>;` 形式。

**症状：test suite flag 勾不上，Work Center 底部报错。** 文档原文（`02.08.04.32.02.01.06`）："Setting the test suite flags FFV enable, FRG enable, FFC scan info enable and log first requires the test suite flag FFC enable to be activated. Setting the test suite flag H/L/I/U (multiple execution) requires the test suite flag FRG enable to be enabled. Otherwise, an error message appears at the bottom of the SmarTest Work Center."

**症状：bin 加不进去。** 文档原文（`02.08.04.32.02.01.05`）："it is not possible to add bins whose settings conflict with bin settings that already exist in the testflow. Two bins are considered to conflict if the SBin attribute is the same and any of the attributes listed below, except Notes, is different (empty attributes are ignored)."

**症状：setup 文件或 primary set 显示黄底。** 两个不同来源：Setups page 的黄底 = 该 setup 文件**未加载或不存在**（`02.08.04.32.03.01.07`）；Test suites page 的黄底 = 该 test suite 引用的 primary set 在**当前 setup 文件里不存在**（`02.08.04.32.02.05` 的 `DC_test` 例子：引用了 timing spec "12 f=20MHz"，但目标 timing setup 文件里没有 12 号 spec）。排查入口：前者右键 Load All Setups，后者重选一个存在的 set。

**症状：合并过来的片段变量丢失。** 文档事实（`02.08.04.32.02.05`）：若复制的 testflow 元素用了目标 testflow 没有的变量，SmarTest 弹 Add New Variables 窗口；选 OK 会以源 testflow 里的默认值为初始值创建，**选 Cancel 则元素根本不会被复制**。窗口里的 "Do not ask me again, add those variables automatically" 可在 Testflow Tool preference page 配置。

**症状：选不中想选的节点 / 剪切粘贴被拒。** 文档事实（`02.08.04.32.01.03`）：插入 branching node（run and branch、if…then 等）会产生新的 level；"the software will not allow you to perform any actions that involve nodes from more than one level" —— 可以选同一 level 内的多个节点，不能跨 level 选。

**症状：把 run-and-branch 改成 run 之后，fail 分支里的节点全没了。** 文档原文（`02.08.04.32.02.01.04`）："Converting a run-and-branch node to a run node, automatically removes the nodes in the failed branch of the converted node."

**症状：merge 时 master file 的 group 名冲突 / bind 对不上。** 文档事实（`01.01.07.02.02.04.05.04`）：testflow master file 的冲突是 **test group name collision**；Setup Management Tool 可按重命名策略自动改名，也可用 `REMAP` 关键字指定新名。**testflow 文件与其它 setup 文件之间的 Bind 必须在 master file 里手工指定**，格式：

```
Group 3 [open]: files/group3.tf
[Bind: ../../level/master.lmf: files/eqnset02.lev;../../timing/master.tmf: files/eqnset01.lev;...]
```

assemble 时工具会扫描 level/timing/analog control 等绑定对，若 group 3 里 test suite 用的 setup 因冲突处理被重映射到了新号/新名，会自动把 test suite 的 setup 改成新号/新名。

**症状：导入 CSV 失败。** 文档原文（`02.08.04.32.02.01.15`）："Do not uncheck any of the items in the Setups list. Doing so results in an error message and prevents importing the CSV file."（导出侧对应的一句在 `02.08.04.32.02.01.16`："If you want to import the exported file into SmarTest, all items in the Setups list must be checked."）

**症状：多 site 时某些 site 等到失败分支跑完才往下走。** 文档事实（`02.08.04.32.01.04`）："If all sites reach a test suite in parallel, then they all leave that test suite in parallel, unless they are binned."；且 "If the node contains a branch (like the run & branch node and all flow control nodes), then the false (failing) path is always executed first." —— 这是设计行为不是 bug，但排流程顺序时要算进去。

**文档未覆盖：** corpus 里没有专门针对 testflow 的 `Errors` 段（按 `sections.jsonl` 检索，`h2` 为 Error* 且文档名含 testflow 的段落数为 0）。上列各条都来自 Procedure 正文、Note 或 Functional changes，不是集中的错误章。

## 下一步

`[[run]]`

理由（文档事实，`02.08.04.32.02.01.02`）：创建 testflow 的 `What to do next` 只有一句 —— "Debug the testflow."。组装完的 testflow 必须 build / execute / 单步调试，才能确认流程逻辑正确；文档为此在 "Using the Testflow Tool" 下另立了 Running a testflow（`02.08.04.32.02.03`）、Debugging a testflow（`02.08.04.32.02.04`）、Hardware Response Emulator（`02.08.04.32.02.06`）三节。

`02.08.01.01.06_Task_6` 把两件事并排写：先「组装」（"Insert bin, flow control, assign value elements and so on. Finalize the system, testflow, and test suite flag settings."），后「执行并调试」（"Verify the execution flow of the testflow. If there are some bugs in the testflow, fix them and then execute it again."）—— 前者是本页，后者是 `[[run]]`。

组装阶段遗留的可选项，也在这里交接给后续：

- testflow 的 flag 设置此时已就位，执行期怎么用它们调试（`global_hold` 单步、`hold_on_fail`）—— `[[run]]`。
- bin 已插好，执行后落到哪个 bin、产出什么 datalog —— `[[results]]`。
