---
type: mapping
title: Testflow 组装的三层对照
layer: n/a
stage: testflow
tags: [mapping, testflow, gui, testflow-file, testflow-flag, test-suite-flag, testflow-variable, bin, external-control]
related: [testflow, testflow-tool, flow-data-editor, flow-sequence-editor, testflow-properties-view, testflow-file, testflow-master-file, test-suite, test-suites-page, special-test-suites, bin, flag, flags-page, alphabetical-list-of-flags, flow-control-node, assign-value-node, print-node, group-node, built-in-functions, testflow-variable, setup-management-tool, stpm, stpm-control-file, stpm-merge-rules-file, ci-cpi, tpi-program-routines, test-suite-control-api, device-directory, run, results, project, pin, testmethod]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32_Testflow_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02_Testflow_components.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.04.01_Inserting_a_Multibin_SmartDisconnect_test_suite.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.02_Flow_control_nodes.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.02.01_Built-in_functions.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.03_Assign_Value_node.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.04_Print_nodes.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.02_Testflow_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.03_Testflow_flags_for_data_logging.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.04_Test_suite_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.02_Creating_a_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.03_Selecting_setup_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.05_Inserting_a_bin_into_the_testflow.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.01_Defining_variables.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.03_Assigning_values_to_variables.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.04_Assigning_a_level_or_timing_spec_value.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.05_Changing_spec_values_at_run_time.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.15_Importing_a_testflow_from_a_CSV_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.16_Exporting_a_testflow_to_a_CSV_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.05_Merging_the_testflows.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.04_Bins_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.05_Variables_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.07_Setups_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.06.02_Accessing_Testflow_Settings.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.06.02.01_Setting_User_Flags.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.01_Flag_Classifications.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.01.02_User_Flags.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.02.02_Production_Flags.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.12_GetLoadedTestflowName.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.17_GetTestflowRevisionInfo.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.17_TestsuiteProxy.getTestsuiteFlag.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.33_TestsuiteProxy.setTestsuiteFlag.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.03_Using_the_Setup_Management_Tool_from_the_Command_Line.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Testflow 组装的三层对照

## 这张表在说什么

Testflow 这一段的东西，语料里**同时存在三套说法**：Testflow Tool 两个编辑器里的表格（GUI）、
`<device_dir>/testflow` 下的 testflow 文件（file）、以及测试方法与外部程序里的 API（L2 / L3）。
**这三套是不是同一个东西的三种写法——语料自己回答了，而且是明说的。**

`02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` 讲 flag 表头两列的那几句：

> 「The first column shows two names for the flags:」

> 「The upper value is the name that is shown in the Flags page or in the Test suite properties view of the Testflow Tool.」

> 「The lower value is the keyword as it is stored in the Testflow file.」

**「同一个 flag 有两个名字」是本页的地基。** 它说的是：GUI 上显示的那个名字，和文件里存的那个关键字，
**是同一个对象的两种写法**——不是「有关」，是「两个名字」。

紧接着还给了**取值**的对照：

> 「Values on and off in the description are for the GUI. These values correspond to 1 and 0 in the testflow file or APIs. The same applies to other labels of the GUI drop-down lists: These labels are represented as integer values in the testflow file or APIs.」

**这一句把 API 也拉进来了** —— `in the testflow file or APIs`：GUI 的 `on` / `off`，
在**文件里与 API 里都是 `1` / `0`**。

（上面四段引文里 `Flags page`、`Test suite properties view`、`Testflow Tool`、`Testflow file`
在原文里都是**语料内部链接**，按 §11.1② 剥掉链接标记后保留字面——所以引文看着像普通名词，
**那不是本页改的**。）

flag 之外，语料在别处**逐个点名**了几条跨层对应，本页把它们当作独立的证据（见下一节）：

- **testflow 变量**：定义在 Variables page，读法是 `GET_USER_DOUBLE`（`02.08.04.32.02.01.12.01`）。
- **testflow flag 的 L2 与 L3 读写口**：同一句话里两个都点了名（`02.08.04.32.01.02.07.02`）。
- **user flag 的三层**：定义在 GUI、存在文件的 `flags` section（`02.09.01.08.05.01.02`）。
- **运行期改 level / timing spec 值**：固件命令 `SVLR` 与两个 GUI 向导并列（`02.08.04.32.02.01.12.05`）。

**「三层」这个词在本页要放宽理解**：§2.5 的格式给了五列（GUI / 文件 / L1 / L2 / L3），
而 testflow 这一段**L1 列几乎全是空的**、**L2 与 L3 列只在 flag / 变量 / bin 这三处被语料钉住**。
这不是我没找到——下面「对不上的地方」逐条说明，并给出量化的边数。

## 对照表

**读法。** 一格填了名字 = 有证据（证据是什么见下一节）；`?` = **本页没找到证据**，不猜；
`—` = **这一层不存在这个对应物**（不是「没找到」）——本页的 `—` 都带一条理由，理由全是**推断**，
逐格的理由在下面「对不上的地方」①里统一交代。

| 目的 | GUI | 文件 | L1 命令 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 新建 / 打开 / 保存 testflow | [[testflow-tool]]（`New Testflow` 窗口） | [[testflow-file]]（`<device_dir>/testflow`） | `—` | `—` | `?` |
| 把 setup 文件挂进 testflow 并加载 | [[flow-data-editor]] 的 `Setups page`（`File` 列怎么写，**④ 图证**，见⑩） | [[testflow-file]] 的 `context` section | `—` | `—` | `?` |
| 插 test suite、编排流程顺序 | [[flow-sequence-editor]] | [[testflow-file]] 的 `test_flow` / `test_suites` section | `—` | `—` | `?` |
| flow control 节点（if / repeat / while / for） | [[flow-control-node]] | [[testflow-file]] 的 `test_flow` section | `—` | `?` | `?` |
| 条件里取 testflow 内部数据 | [[built-in-functions]] | [[testflow-file]] 的 `<expression>` | `—` | `?` | `?` |
| 定义 testflow 变量与初值 | [[flow-data-editor]] 的 `Variables page` | [[testflow-file]] 的 `declarations` section | `—` | `GET_USER_FLAG` / `GET_USER_STRING` / `GET_USER_DOUBLE` | [[ci-cpi]] 的 `User Flags`（`02.09.01.08.05.01.02`） |
| 在流程某点给变量赋值 | [[assign-value-node]] | [[testflow-file]] 的 `test_flow` section（`<assignment>`） | `—` | 同上一行（读侧） | `?` |
| 运行期改 level / timing spec 值 | [[flow-sequence-editor]] 的 `assign level value` / `assign timing value` 向导 | [[testflow-file]] 的 `test_flow` section（`<assignment>`） | `SVLR` | `?` | `?` |
| 插 stop bin / otherwise bin / floating bin | [[flow-sequence-editor]] 的 `goodbin` / `badbin` / `Multi Bin`；[[flow-data-editor]] 的 `Bins page` | [[testflow-file]] 的 `test_flow`（`stop_bin`）与 `binning` section | `—` | `SET_MULTIBIN` | `?` |
| Multibin SmartDisconnect test suite | [[flow-sequence-editor]] 的 `Multibin Disconnect` | [[testflow-file]] 的 `test_flow` section（fail 分支） | `—` | `GET_DISCONNECT_CONTEXT()` | `?` |
| 往 Report / Datalog 插注释 | [[print-node]] | [[testflow-file]] 的 `test_flow` section（`print()` / `print_dl()`） | `—` | `?` | `?` |
| 把连续节点收成一组 | [[group-node]] | [[testflow-file]] 的 `test_flow` section（`{ … }` + `<compound_label>`） | `—` | `—` | `?` |
| `bin_disconnect` special test suite | [[test-suites-page]]（特殊 test suite 不在流程节点里） | `?` | connect/disconnect 命令文件（`02.06.08.01.04.01`，**仅链接**） | `DISCONNECT` | `?` |
| `multi_bin_decision` special test suite | [[test-suites-page]] | `?` | `?` | `SET_MULTIBIN` | `?` |
| test suite flag | [[test-suites-page]] / `Test Flags` 快捷菜单 / Test Suite Flags 工具 | [[testflow-file]] 的 `test_suites` section 的 `local_flags` | `?` | `GET_TESTSUITE_FLAG` / `SET_TESTSUITE_FLAG` | [[test-suite-control-api]] 的 `TestsuiteProxy.getTestsuiteFlag()` / `.setTestsuiteFlag()` |
| testflow flag | [[flags-page]] | [[testflow-file]] 的 `flags` section | `?` | `SET_TESTFLOW_FLAG` / `GET_TESTFLOW_FLAG` | [[ci-cpi]] 的 `SetTestflowFlag` / `GetTestflowFlag` |
| system flag（data logging flag） | [[flags-page]] | [[testflow-file]] 的 `flags` section | `?` | `?` | [[ci-cpi]] 的 `GetSystemFlag` / `SetSystemFlag` |
| `debug_mode` flag 打开后的调试信息收集 | [[flags-page]] | `flags` section 的 `debug_mode` | Trace Function（`02.06.01.03.05`，**仅链接**） | `?` | `?` |
| `fail_per_label` flag 打开后的 error map 记录粒度 | `?` | `flags` section 的 `fail_per_label` | `DCRM`（`02.06.02.02.46`，**仅链接**） | `?` | `?` |
| `site_match_mode` flag 的全局语义 | [[flags-page]] | `flags` section 的 `site_match_mode` | site match function（`02.06.03.01.10.04`，**仅链接**） | `?` | `?` |
| 把 testflow 拆成子文件 / 合并回 tester file | [[setup-management-tool]] | [[testflow-master-file]] | `—` | `—` | `smartest_mfh` CLI（`testflow` file_type）——**调用格式见「对不上的地方」⑩（④ 图证）** |
| 把 testflow 合并进 master test program | [[stpm]] | [[testflow-file]] | `—` | `—` | [[stpm-control-file]] 的 `mtp_device_testflow`；[[stpm-merge-rules-file]] 的 `overwrite_flow_var_value` |
| 外部程序读写 testflow 文件 | `?` | [[testflow-file]] | `—` | `—` | [[tpi-program-routines]] 的 `DataManager(dm_testflow, …)`、`GetLoadedTestflowName()`、`GetTestflowRevisionInfo()` |
| 导出 / 导入 CSV | Test Program Explorer 右键 `Export` / `Import` | CSV 文件 | `—` | `—` | `?` |

**表里没有的**：`special-test-suites` 那篇列了 **Abort / Reset / Pause / Exit / Init / Download / bin_disconnect / multi_bin_decision** 八项
（其中两项已入表），**Abort / Reset / Pause / Exit 四项目录里另有 L3 落点**
（`02.09.01.07.01`–`02.09.01.07.04`，见下面「对不上的地方」⑨），
**Init 与 Download 两项本页没找到任何跨层证据**，不塞进表里凑数。

## 证据：哪几格是钉死的，哪几格只是「那边链过来了」

**证据分四档，本页不把它们混成一种。**

**① 语料明说（最硬）。** 四句，本页把主表里对应的格子全挂在这四句上：

| 明说的内容 | 出处（raw 相对路径） | 背书了主表哪些格 |
|---|---|---|
| GUI 名 ↔ 文件关键字是**同一个 flag 的两个名字** | `02.08.04.32.01.02.07.01` | 三行 flag 的 GUI 列与文件列 |
| GUI 的 `on`/`off` 在**文件里与 API 里**都是 `1`/`0` | `02.08.04.32.01.02.07.01` | 三行 flag 的 L2 / L3 列的取值形态 |
| 同一个 flag 可用 `SET_TESTFLOW_FLAG`（test method）或 `SetTestflowFlag`（CI_CPI）写 | `02.08.04.32.01.02.07.02` | testflow flag 一行的 L2 与 L3 |
| user flag「定义在 Variables page …… 存在 Testflow file 的 flags section」 | `02.09.01.08.05.01.02` | 变量一行与 system flag 一行的 GUI / 文件列 |

testflow flag 那句是**同一句话里把 L2 与 L3 并排点名**，所以它是主表 L2 / L3 两列最硬的一格，
逐字如下（`02.08.04.32.01.02.07.02`）：

> 「You can also set this flag using SET_TESTFLOW_FLAG API (test method), or SetTestflowFlag API (CI_CPI). You can determine the current setting of the flag using GET_TESTFLOW_FLAG API (test method), or GetTestflowFlag API (CI_CPI).」

user flag 那一句是**一句话里三层**（`02.09.01.08.05.01.02`）：

> 「User Flags are defined in the Variables page of the Flow Data Editor and stored in the flags section of the Testflow file.」

**② 文档之间有链接（次硬，逐条可查）。** 取自 `extract/edges.jsonl`，
`02.08.04.32.*` 出去的**已解析链接共 662 条**，按落点分：

| 落点 | 条数 |
|---|---|
| `02.08`（Testflow 章内部） | 511 |
| `02.07`（L2） | 46（33 个不同目标） |
| `01`（Getting Started） | 29 |
| `02.09`（L3） | 28（17 个不同目标） |
| `02.10`（Data Logging） | 21 |
| `03`（用例） | 19 |
| **`02.06`（L1）** | **7（6 个不同目标）** |
| `02.11` | 1 |

**L1 那 7 条本页逐条看过**，全部列出（这就是主表 L1 列的全部实料来源）：

| 源文档（GUI 侧） | 链到 | 行 |
|---|---|---|
| `02.08.04.32.01.02.01.02_Special_test_suites.md` | `Defining connect/disconnect sequences` | 106 |
| `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` | `Using the Trace Function` | 130 |
| 同上 | `DCRM`（Digital Compare Result Mode） | 170 |
| 同上 | `Controlling the site match function` | 451 |
| `02.08.04.32.02.01.12.04_Assigning_a_level_or_timing_spec_value.md` | `02.06_Command_Reference`（章首页，不是某条命令） | 26 |
| `02.08.04.32.02.01.12.05_Changing_spec_values_at_run_time.md` | `SVLR`（Spec VaLues at Runtime） | 8 |

**这 7 条里只有 `SVLR` 那一条是「同一句话里点名」的**，其余 6 条都是
`For more information, refer to …` / `See …` 这种**「见也」链接**。
**链接证的强度要说清**：一条链接**只证明「那篇文档认为读者该去看这一篇」**，
**不证明两个东西等价**——可能是「见也」，也可能是「区别在这里」，也可能是「前提」。
所以主表 L1 列里那三格（Trace Function / `DCRM` / site match function）**本页都标了「仅链接」**。

`SVLR` 那一条不一样，它是**文档自己的陈述**（`02.08.04.32.02.01.12.05`）：

> 「Level and timing spec values can change at run time using the firmware command SVLR or in the New Assign Level Spec Wizard and New Assign Timing Spec Wizard windows in the Flow Sequence Editor.」

**一句话里把固件命令与两个 GUI 向导并列**——这一条是本页 L1 列唯一的「语料明说」。

**③ 只有单侧的证据（最弱）。** 主表里下面这些格，**只有一侧有名字，另一侧是 `?`**：

- **L3 侧有名字、GUI 侧是 `?`**：TPI 那一行（`DataManager` / `GetLoadedTestflowName()` /
  `GetTestflowRevisionInfo()`）。**语料里没有一篇 testflow 章文档链到 `02.09.01.09.*`**
  （那 28 条 L3 边全落在 `02.09.01.02`、`02.09.01.05`、`02.09.01.06`、`02.09.01.07`、`02.09.01.08`、`02.09.01.17` 上）。
- **L1 侧有三格只有链接**（证据② 那张 L1 表的最后三条），所以那三格**不算「语料明说」**。
- **`?` 的 33 格**（`multi_bin_decision` 的文件列、四行 flag 的 L1 列……其余是各行的 L2 / L3 列）。
  `?` 的意思是「**本页没找到证据**」，不是「不存在」。

**④ 图证（2026-09-20 加，本页用到了）** —— 从 raw 自带的截图里读出来的。
本页 `sources:` 那 42 篇里**一共引了 33 张不同的 `.png`**，**全部读了**（逐张结论见「对不上的地方」⑩）。
这一档**比①②③都硬**（图是文档自带的，不是我的推断），**但它不可检索**——
**理由与写法见 `schema.md` §11.4**；要点是：**必须写清是哪张图，并说明图里的字 grep 不到。**
**有四张图的内容大部分能在 raw 里 grep 到**（`110701.png` / `110705.png` / `111392.png` / `122906.png`）：
`02.08.04.32.02.01.16` 的 CSV 导出例把 Setups / Flags / Variables / Bins 四页的**文本逐字抄进了
raw 文本**——**那四张算「图与文本互证」，不算 ④ 档**，⑩ 里逐张分了类。

> **这一档是被一个假说法挡了很久才补上的。** 本页原先写着「图片路径向上爬四层（`../../../../raw/`），
> **在语料树之外**，所以**本页没有任何来自图的结论**」——**路径是对的、图是读得出来的**（§11.4）。
> **一个不成立的理由，会把一整档证据永久关在门外。**

## 对不上的地方

**① L1 整列几乎全空，而且 `—` 是本页最弱的一类断言。** 先说 `—` 的理由（**推断**）：
`02.08.04.32.03.05` 把「改 testflow 参数」的通道列成了两条——

> 「Since the testflow file is a text file, you can change parameters directly using a text editor. However, we recommend changing the settings only by the Testflow Tool of the SmarTest Work Center.」

——**「文本编辑器」和「Testflow Tool」，固件命令不在里面**。加上 `02.06_Command_Reference` 章内
**没有一条以 testflow 为主语的命令**（本页复核了 `02.06.02.02.*` 的命令名清单，逐个数过），
所以**组装动作**那一批格的 L1 写 `—`。

**但这个 `—` 有一个就在本阶段的现成反例：`SVLR`。**
它是固件命令，它出现在 testflow 章的 GUI 文档里（`02.08.04.32.02.01.12.05`，标题就叫
"Changing spec values at run time"）。**所以「testflow 阶段没有固件命令」是个全称否定句，它是错的**
（§2.1 四条硬规矩之二：全称否定句举证责任在写的人——本页证不了，只能把范围缩到「组装动作」）。
**三行 flag 的 L1 格因此写 `?` 而不是 `—`**：flag 背后明显有固件侧机制（下一档就是三条链接），
但语料没说哪条命令读或写 flag。

**② L2 与 L3 只被钉在少数几个点上，这个分布本身就是信息。** 主表二十四行里，L2 有名字的**只有八行**
（变量定义、变量赋值、插 bin、Multibin SmartDisconnect、`bin_disconnect`、`multi_bin_decision`、
test suite flag、testflow flag）；L3 有名字的**只有七行**（变量定义、test suite flag、testflow flag、
system flag、master file、STPM、TPI）。**这七行里「变量定义」以外的六行，全部是 flag 或文件级的东西。**
**testflow 的结构（插哪个 test suite、什么顺序、什么分支）在 L2 / L3 两列一格都没有**
——文档里没有任何 API 能增删 testflow 节点，**这是结构事实，不是缺口**。

**附：表里的计数（供复核）。** 二十四行 × 五列 = **120 格**，其中填了名字的 **64 格**、
`?` **33 格**、`—` **23 格**。**没有一行是五格全填满的。**

**③ testflow 文件的首行与 BNF 的 section 名单，和 `## Example` 对不上（语料自身的矛盾，照实记）。**
`02.08.04.32.03.05` 的 `<section>` 列了 17 个名字（`information` … `hardware_bin_descriptions`），
而同一篇的 `## Example` 里出现了 **BNF 名单里没有的 4 个 section**：
`implicit_declarations`、`testmethodparameters`、`testmethodlimits`、`testmethods`。
反过来，Example 里的 `override_tim_equ_set` / `override_lev_equ_set` / `override_tim_spec_set` /
`override_lev_spec_set` **也不在 BNF 的 `<test_suite_entry>` 里**（BNF 只有 `override_dpsset` /
`override_levset` / `override_seqlbl` / `override_timset` / `override_wvfset` / `override_testf`）。
**两条都对不上，本页不替语料选一个。**

**④ 同一个 flag 的 BNF 名与文件里的名，拼法不一致。** §11.2 明令照实记：

- `graphic_result_displ`（BNF）、`graphic_result_displa`（`## Example`）、`graphic_result_display`（CSV 导出例与 flags 文档的链接文本）——**三种拼法**；而 flags 文档那条链接的**锚点**又是 `#_342556__row_graphic_result_displa`。
- `ink wafer`（BNF，**空格**）vs `ink_wafer`（Example 与 CSV，**下划线**）。
- `<tflow_flag>` 的 BNF 名一律带空格（`set pass level` / `bypass level` / `debug mode`），Example 里一律带下划线（`set_pass_level` / `set_bypass_level` / `debug_mode`）。

**⑤ 四篇文档里的四处瑕疵（含错字、缺空格、语序），本页照原样抄、没替它改**（§11.2）：

> 「The STPM control file contains commands and setting for SmarTest Program manager (STPM) to use in a conversion. It's structure follows the conventions of the Python programming language.」

（`SmarTest Program manager` 的 `manager` 小写；`It's structure` 应为 `Its structure`。出处 `02.09.02.03.01`。）

> 「This function query the status of a test suite flag.」

（`query` 应为 `queries`。出处 `02.09.01.14.02.01.17`。）

> 「This function sets a value to a test suite flag. If it is successfully executed,true will be returned. Otherwise, false will be returned.」

（`executed,true` 逗号后缺空格。出处 `02.09.01.14.02.01.33`。）

> 「 To, for example, get the current value of the double type variable set above, use GET_USER_DOUBLE:」

（语序如此，`To, for example, get …`。出处 `02.08.04.32.02.01.12.01`——行首那个空格是 raw 里的，
本页引文按 §11.1① 折叠空白，**字符一个没动**。）

**⑥ special test suite 的「七」与「八」，以及两项目录里找不到落点。**
`02.08.04.32.01.02.01.02_Special_test_suites.md` 明写：

> 「There are seven types of special test suites.」

**但紧接着的表里列了八项**：Init、bin_disconnect、Abort、Reset、Pause、multi_bin_decision、Exit、Download。
**本页不替它选一个数。** 另外，`02.08.04.32.03.05` 的 BNF 17 个 section 名里
**没有 `bin_disconnect` 与 `multi_bin_decision` 的落点**——这两个 special test suite 确实存在，
但**本页读到的 raw 里找不到它们存进 testflow 文件的哪一段**，所以主表这两行的文件列是 `?`。

**⑦ 一处编码损坏（§11.2① 那一类，形态略有不同）。**
`02.08.04.32.01.02.07.01` 的 flag 表表头在 raw 里写作：

```
 | #1 鈥?#n
```

`鈥` 后面跟的是一个 `?`（本页**没有推断**它原来是什么字），
上下文看是「#1 到 #n」的区间写法。**raw 一个字节没动，本页也不改。**

**⑧ 「testflow optimization」在语料里有两说，本页并列、不判谁对。**
`02.08.04.32.03.05` 的 `Functional changes` 写着 `SmarTest 7.1.0: Testflow optimization function removed`；
而 `02.09.01.09.02_DataManager.md` 的 `Opc` 表里**仍然有** `dm_optimize`（`create an optimized testflow`）、
`dm_del_optimize`（`delete a optimized testflow`）、`dm_optimize_utd`。**两条都是 raw 原文。**

**⑨ 那 28 条 L3 边里，有 11 条落在 `02.09.01.07`（Production Run 控制：`Aborting a Production Run`、
`Resetting a Production Run`、`Aborting a Testflow`、`Pausing a Production Run`，加章首页共 5 个目标），
本页把它们记在「表里没有的」**——那四个名字同时也是本阶段的 special test suite
（Abort / Reset / Pause / Exit），但「属 `[[run]]` 还是属本阶段」**本页没判**
（判据要 `[[run]]` 那页来给）。

**⑩ 图能读，这一页读了——原先这里写的「图在语料树之外」是错的。**（**2026-09-20 更正**）

图片路径 `../../../../raw/<n>.png` 从 md（`tdc-html/agent-markdown/by-category/<分类>/x.md`）
**往上四层正好是 `tdc-html/`**，所以图在 `tdc-html/raw/`（该目录 5,193 张 png）。
本页 `sources:` 42 篇里**共引 33 张不同的 png**（页面原先只点了六张，还带一个 `…`），**逐张读了**。

**先给结论：没有一格因为看图从 `?` 变成有名字。**
三十三张图里**没有一张出现固件命令**，所以四行 flag 的 L1 格、`multi_bin_decision` 的文件列
**仍然是 `?`**——「L1 整列几乎全空」这条结论，**图改变不了**（① 里那个 `—` 的判断也不因图而变）。

**图真正补上的，是「GUI 的哪一列 ↔ 文件的哪一位」这个粒度**，四处：

| 图（出自哪篇） | 读到了什么 | 图里的字在 raw 里 grep 得到吗 |
|---|---|---|
| `110701.png`（Setups page，`02.08.04.32.03.01.07`） | 标签页名 `adc_dac_x2.tfl`；十行组件里**七行的 `File` 格有值且带扩展名**：`adc_dac_x2.pin` / `.lev` / `.tim` / `.vec` / `.ana` / `.wav` / `.rout`；第 9 行 Routing 被**标黄** | 列名 `Setup`/`File` 与十行组件名**搜得到**（CSV 导出例的 `$,Setups` 一节）；**`adc_dac_x2.*` 全语料 0 命中** |
| `122906.png`（Bin page，`02.08.04.32.03.01.04`） | 八个列名（`Software Bin` … `Bin OverOn`）与六行数据；标签页名写作 **`flow.tt`** | 列名搜得到；**数据行 `goodbin1` / `Analog_fail` / `USB_Rx_Diff_HV_fail` / `DFR_X_HV_Fail` 0 命中**，`flow.tt` 也 0 命中 |
| `110995.png`（New Assign Timing Spec Wizard，`02.08.04.32.02.01.12.05`） | 四个字段 `Equation Set` / `Spec Set` / `Variable Name` / `Variable Value`，值是 `2` / `2` / **`f@port_2`** / `65`；**图上另有三条红字注记**（`Numbers of equationset and spec set` / `Spec "f" will be changed for "port_2"` / `New value`） | 字段名搜得到；**`f@port_2` / `@port_2` / `Numbers of equationset` / `will be changed for` 全语料 0 命中**。**第三条 `New value` 这个两词串在语料别处出现过 6 次（与这张图无关）——本页不敢说它只在图里** |
| `110634.png`（New "For" 节点向导，`02.08.04.32.01.02.02`） | 六个字段 `Assign Var` / `Assign Expr` / `Condition` / `Increment Var` / `Increment Expr` / **`TestNum Incr`** | 前四个搜得到；**`TestNum Incr` 0 命中**（`110633.png` 的 While 向导同栏也一样） |

**`91496.png`（`01.01.07.02.02.04.03`，「Syntax of smartest_mfh」）——本页那格也因此填细了。**
图上是一张 railroad 图：`smartest_mfh` 后面接 `split` / `assemble` / `create` / `assemble_all` /
`split_all` 之一，再接一个参数；**`split` 与 `assemble` 接 `<master_file>`、`create` 接 `<file_type>`、
`assemble_all` 与 `split_all` 接 `<directory>`**。即调用格式是 `smartest_mfh <操作> <参数>`。
**图里的 token（`split`、`<master_file>`…）在正文里都有，但「谁接谁」这层结构只在图里**
——正文那一句 `It must be called in the following format:` **后面直接就是这张图**，
**格式串在整个 raw 里 grep 不到**。（`testflow` 是 `<file_type>` 的合法值之一，这一条是正文写的。）

**图与 raw 文本不一致的两处，本页照实并列、不替语料选一个：**

- **Setups 页的 `File` 列有两套写法，图是第三套。** raw 文本里**两处**给了这一列的内容：
  CSV 导出例的 `$,Setups` 一节（**只有四行**有文件：`pins_soc` / `levels` / `timing` / `all.binl`），
  与 `context` 例（`context_levels_file = "levels"` / `context_timing_file = "timing"` /
  `context_vector_file = "all.binl"` …）——**两处的值都不带扩展名**；
  而 `110701.png` 里**七行**有文件、**都带扩展名**（`adc_dac_x2.lev` / `.tim` / `.vec` / `.ana` / `.wav` / `.rout`）。
  **「哪几行有文件」与「带不带扩展名」两处都对不上——三个说法并列，本页不替语料选一个。**
- **Bin page 的 `Hardware Bin` 两处不一致。** CSV 导出例那一行写 `,1,Pass,,,good,Green,no,yes`
  （**`Hardware Bin` 与 `Hardware Bin Desc` 是空的**），`122906.png` 第一行却是
  `Software Bin=1`、`Hardware Bin=1`、`Software Bin Desc=goodbin1`、`Hardware Bin Desc=goodbin1`。

**另外三处图里特有的字**（下面逐条标了哪些 0 命中、哪些正文里本来就有）：

- **`Set Flags` 右键菜单**（`351363.png`，`02.08.04.32.01.02.07.04`）里的
  `Set Output Fail Value` / `Set Output Pass Value` / `Set Break Point` 三项。
  （同一菜单里的 `Bypass` / `Set Pass` / `Hold` / `Hold on Fail` 在 `02.08.04.32.01.02.07.01`
  的字母表里有，**只是大小写不同**：正文写 `Set pass`，图里是 `Set Pass`。）
- **`Testflow Settings Mode` 窗口的 `Testflow:` 栏**：一张图写 `testflow`（`46396.png`，
  `02.09.01.06.02`），另一张写 `B6_Short_409B11_415_Rov8.afh`（`351364.png`，**0 命中**）
  ——**同一栏两种写法**。`351364.png` 同时给出该窗口把 flag 分成**四类复选框**
  （System Flags / Testflow Flags / User Flags / Testsuite Flags，另有 Report Formatter），
  以及 Test Suite Flags 工具的列头（小写带空格：`set pass` / `fail value` / `per pin on pass` …）。
- **合并 testflow 时的变量对话框**（`147669.png`，`02.08.04.32.02.05`）里的变量名
  `CPR5_GLOBAL_V_DIG_SVS` / `CPR6_GLOBAL_V_DIG_SVS`（**0 命中**）；
  **`User Flags` 窗口**（`107005.png`，`02.09.01.06.02.01`）里的 `newvar` / `testvar2`（**0 命中**）。

**图为 ① 档那句话提供的是一个部分反例，照实记**：① 说「GUI 的 `on`/`off` 在文件里与 API 里是 `1`/`0`」，
而 `110705.png`（Flags page）的 `Value` 列**同一列里两种写法并存**：
`set_pass_level` / `set_fail_level` / `set_bypass_level` 三行**直接显示 `0`**，
`hold_on_fail` 那一行显示 `off`，system flag 各行显示 `on` / `off`。
**这一点在 raw 文本里也搜得到**（CSV 导出例的 `$,Flags` 一节逐行相同），**所以它不是 ④ 档**——
**它说明 ① 那句话的适用范围比字面窄，而本页把它当成了「整个 GUI 列」的地基。**

**图答不了的，照实说：**

- **`120104.png`（New MultiBin Wizard）里一个输入字段都没有**——只有标题 `New "MultiBin" Node`
  和一句 `Creating a multibin node`。所以 `multi_bin_decision` 那一行的**文件列保持 `?`**。
- **图是「某一次具体配置」的截图，不是格式规范。**「哪些字段必填、哪些组合非法」**图答不了**
  ——那是文本的事，而文本在这一点上也没写全。
- **图里有截断，那是图的截断、不是语料的截断**：`124702.png` 的 For 节点标签写到
  `@aVar=1; @aVar<10; @aVar=@aVa`**就没了**（图被裁掉一截）。**本页不把图的截断当成语料的事实**
  ——§13.1 第 6 问：**我引的这半句，是语料断了，还是印断了？**
- **其余二十来张图只复述正文已有的东西**：`124700.png`（两种 test suite 形状）、`124703.png`
  （三种 assign 节点）、`143753.png`（group 节点开合）、`124701.png`（四种 bin 形状）、
  `110636.png` / `110637.png`（两个 Print 向导）、`110968.png` / `111411.png`（变量与 level spec 向导）、
  `110943.png` / `353999.png` / `353654.png` / `353712.png`（Multibin 与 SmartDisconnect）、
  `110984.png` / `110987.png`（CSV Export / Import 两个对话框）、`120102.png`（New Bin Node）、
  `110985.png`（Testflow 例）。其中**唯一一条 raw 里没有的并存关系**来自
  `110985.png` 与 `353654.png` 合看：同一批节点在 **Palette 里全小写无空格**
  （`goodbin` / `badbin` / `multi_bin`）、**在 `Insert` 菜单里 Title Case**
  （`Good Bin` / `Bad Bin` / `Multi Bin`）——**「GUI 自己两处写法不同」这件事，raw 文本里没有一句写出来。**

## 出处

`sources:` 四十二篇，**全部读过正文**（不是只读链接）。逐字引用只来自其中**十篇**：
`02.08.04.32.01.02.07.01`、`02.08.04.32.01.02.07.02`、`02.08.04.32.01.02.01.02`、
`02.08.04.32.02.01.12.01`、`02.08.04.32.02.01.12.05`、`02.08.04.32.03.05`、
`02.09.01.08.05.01.02`、`02.09.01.14.02.01.17`、`02.09.01.14.02.01.33`、
`02.09.02.03.01`。

**本页没做的：**

- **一篇 `02.07` 的 API 页都没读。** 主表 L2 列里那些名字（`GET_USER_DOUBLE`、`SET_MULTIBIN`、
  `GET_TESTSUITE_FLAG` / `SET_TESTSUITE_FLAG`、`GET_DISCONNECT_CONTEXT`、`DISCONNECT`…）
  **是从 `02.08.04.32` 侧的链接与散文里取的**，**它们自己的签名、参数、返回值，本页一个字没有**。
- **`02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` 只读了头部与两处**（623 行）。
  主表里 flag 相关的格**没有覆盖那一篇的全部 flag**——只覆盖了它链到别的层的那几处。
- **`02.06` 的命令页一篇没读。** L1 列里那三个名字（Trace Function / `DCRM` / site match function）
  **是从链接文本里取的**；唯一逐字引的 `SVLR` 也是**只读了它被引用的那一句**，
  没读 `02.06.02.02.252` 自己。
- **`02.08.04.32.03.06.01_Top-level_control_structures.md` 没读**，所以 master file 的
  `if` / `for` / `while` / `repeat until` 顶层结构**在本页的对应物是空的**。
- **`Flow_Sequence_Editor` 与 `Flow_Data_Editor` 这两篇元素页正文没读**，也没读
  `02.08.04.32.01.03_Hierarchy_within_a_testflow.md`、`02.08.04.32.02.01.01_Opening_the_Testflow_Tool.md`。
- **图看了（2026-09-20）。** 本页引到的几篇里共引 **33 张不同的 `.png`**（页面原先只点了
  `110635.png`、`110705.png`、`110701.png`、`111392.png`、`120102.png`、`120104.png` 六张，
  后面跟一个 `…`），**逐张读过**，逐张的结论在「对不上的地方」⑩。
  **图片路径 `../../../../raw/` 从 md 往上四层正好是 `tdc-html/`，文件就在 `tdc-html/raw/`**
  ——**上一版写的「在语料树之外」是错的，那句已删**。
  读图补上的是**「GUI 的哪一列 ↔ 文件的哪一位」这个粒度**（Setups / Bins / 两个 spec 向导 / `smartest_mfh` 的调用格式），
  **但它没有翻转主表任何一格**：33 张图里**没有一张出现固件命令**，
  所以四行 flag 的 L1 格与 `multi_bin_decision` 的文件列**仍然是 `?`**。
  另外**有 4 张图（Setups / Flags / Variables / Bins 四页）的内容在 raw 文本里另有一份**
  （`02.08.04.32.02.01.16` 的 CSV 导出例把那四页抄成了文本）——**这 4 张是互证，不算 ④ 档**
  （其中 Bins 那张的数据行与文本不同，见⑩）。
- **没有实跑。** 没有开过任何编辑器、没有生成过 testflow 文件、没有调过 `smartest_mfh`、
  没有用 `extract/wiki-plan.csv` 之外的任何数据校对过本表。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/testflow.md`。
  后者是**待办**：testflow 那页目前不知道本页存在。

**与 `wiki/stages/testflow.md` 的一处差异，记在这里、不去改那页**：那页的
「L1 — Firmware / Setup Command」一节写的是「文档未覆盖」，并给了一句**推断**说
「没有任何一条固件命令以 testflow 为主语」。**本页在同一章里找到了 `SVLR`**（`02.08.04.32.02.01.12.05`，
固件命令与两个 GUI 向导并列），另有 6 条只到 L1 的链接。**那页的「以 testflow 为主语」这个限定仍然成立**
（`SVLR` 的主语是 spec value，不是 testflow），**但读者容易把那句话读成「testflow 段没有固件命令」，
那是错的**——本页上面①已把这条风险写明。

**本页 `layer: n/a` 的理由**：§6 要求 mapping 页必填 `layer`，而本页**本身不属于任何一层接口**
（它是对照表，不是接口）——`n/a` 是这个六值枚举里为这种情况准备的值。

`verified: doc-only`
