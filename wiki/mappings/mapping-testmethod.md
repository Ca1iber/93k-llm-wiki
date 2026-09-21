---
type: mapping
title: Test Method 的跨层对照
layer: n/a
stage: testmethod
tags: [mapping, testmethod, utm, gui, test-method-api, firmware-command, test-suite-control-api, tmlimits]
related: [testmethod, test-method-project, test-method-class, initialize, add-limit, on-first-invocation-begin, on-first-invocation-end, for-each-site-begin, for-each-site-end, connect, disconnect, test, testset, limit, tmlimits, fw-task, begin-extension, end-extension, flush, flsh, aprm, psfc, pqfc, universal-test-method-library, structure-of-a-tmlimits-csv-file, controlling-multiple-sites, site-control-window, test-suites-page, testflow-properties-view, project-explorer-view, command-reference, smartcalc-framework, how-to-create-a-universal-test-method-class, test-suite-control-api, tpi-program-routines, dc-test-programming, spec-value, spec-variable, pin-string, file-string, option-list, context-pins, testflow, run]
sources:
  - 01_Getting_started/01.06_Test_methods/01.06.02.01_1._Create_a_Test_Method_Project.md
  - 01_Getting_started/01.06_Test_methods/01.06.02.02_2._Create_a_Test_Method_Class.md
  - 01_Getting_started/01.06_Test_methods/01.06.02.03_3._Add_the_source_code.md
  - 01_Getting_started/01.06_Test_methods/01.06.02.04_4._Build_the_project_to_get_the_universal_test_method_library.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.01_How_to_create_a_universal_test_method_project.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02.01_Working_with_Content_Assist.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02.02_Working_with_Test_Method_Panel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.10_Editing_test_method_from_a_testflow.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.10_Executing_Firmware_Commands.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.md
  - 02_System_reference/02.06_Command_Reference/02.06.01.03.06_Executing_firmware_commands_from_within_a_program.md
  - 02_System_reference/02.06_Command_Reference/02.06.01.05_Site_dependent_firmware_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.03_Defining_the_query_focus.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.03_Changing_the_site_in_focus.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01.06_Pass_Fail_type_and_ERROR_MAP_type.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.03_Tests_page.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.04_Testflow_Properties_view.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.01_TestsuiteProxy.attachTestmethod.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.11_TestsuiteProxy.getTestmethodDefaultLimitNames.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.12_TestsuiteProxy.getTestmethodLimitValue.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.13_TestsuiteProxy.getTestmethodName.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.14_TestsuiteProxy.getTestmethodParameterNames.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.15_TestsuiteProxy.getTestmethodParameterValue.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.16_TestsuiteProxy.getTestmethodUserDefinedLimitNames.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.31_TestsuiteProxy.setTestmethodLimits.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.32_TestsuiteProxy.setTestmethodParameterValues.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01_Generating_test_numbers_from_the_SmarTest_GUI.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.02_Generating_test_numbers_from_a_test_method.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Test Method 的跨层对照

## 这张表在说什么

`mapping-pin`（`wiki/mappings/mapping-pin.md`）那一页有语料自己的一句
`corresponding exactly to` 兜底。**testmethod 这一段没有那样一句。**
这里的跨层关系**散在每一篇文档里**：GUI 侧写成了操作步骤，L2 侧写成了参考条目，
L1 侧**根本不在本阶段的正文里**（除了两条通道）。**所以本页每一格都要单独找证据，
不能靠一句总纲背书——这也是本页里 `?` 比 `mapping-pin` 多的原因。**

**能站住的主链是语料自己搭的。** Getting started 里那四步 GUI 走查
（`01.06.02.01`–`01.06.02.04`），**每一步的 `## Related information` 都链到 02.07 里对应的那一篇**：

- 建工程 → `02.07.02.02.01`；建类 → `02.07.02.02.02`；
- 建库 → `02.07.02.02.02`（`Results` 段）；
- 写源码那一步链得最多，一口气链到 `addLimit`、`SEARCH_FUNC_TASK`、`CONNECT`、
  `ON_FIRST_INVOCATION_BEGIN`、`ON_FIRST_INVOCATION_END`、`TEST` 六篇。

（上面这三条**不是引文**，是本页对 `edges.jsonl` 里那 9 条边的转述；
每条边的源文档与目标见下一节的表。）

**「层数」这个词本页不写进标题。** `mapping-pin` 叫「三层对照」，是因为 pin 那一段
**只有三层被语料钉住**；testmethod 这一段 **GUI / 文件 / L2 / L3 四层都有实料，
L1 只以「通道」的形式存在**（见下面第 12、13 行）。**给一个假数字不如不给。**

L2 侧那句总纲管的**不是** GUI↔L2，而是 **L1 通道**（`02.07.03.10`，逐字）：

> You can execute firmware command to control your hardware directly by using the FW_TASK, BEGIN_EXTENSION and END_EXTENSION APIs.

——本页把「通道」和「对应」**分开写在两处**。

## 对照表

**读法**：一格填了名字 = 有证据（是哪一档见下一节）；`?` = 语料没说，**本页不猜**；
`—` = 这一层不存在这个对应物（不是「没找到」）。**L3 那一列的三格全带（推断）**——
它们是本页**按 L3 文档自己列的成员职责排的**，不是文档明说的对应，
依据与代价见「对不上的地方」①。**带（图证）的格 = 那一格的名字在 raw 的图上直接看得见**——
是哪张图、图里的字为什么搜不到，见证据节 **④** 与「对不上的地方」**⑨**。

| 目的 | GUI | 文件 | L1 命令 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 建 test method 工程（UTM 库的容器） | [[test-method-project]]（`New > Test Method Project` 向导）（**图证**：向导六格） | 工程目录 `<工程名>/`（`.project`、`.cproject`）（**图证**：`Location` 默认落在 device 目录下） | — | — | ? |
| 建 test method 类：模板 / 类名 / 参数 | [[test-method-class]]（`Create a new TestMethod class wizard`） | 源文件 `.cpp` / `.h` | — | [[pin-string]] / [[spec-variable]] / [[spec-value]] / [[file-string]] / [[option-list]] / [[context-pins]] | ? |
| 在 `initialize()` 里注册 limit **名** | 向导 `Limits` 区（`Add` → 只填名字） | 源文件（`addLimit("limit");`） | — | [[add-limit]] | `getTestmethodDefaultLimitNames()` / `getTestmethodUserDefinedLimitNames()`（推断） |
| 在 `run()` 里写测量与执行体 | `test method editor`（`Content Assist`、`Test Method Panel`）（**图证**：`Content Assist` 候选框在源码里） | 源文件（**图证**：图上就是 `.cpp` 的正文） | — | `run()` | — |
| 给 DUT 上电 / 断电 | ? | — | ? | [[connect]] / [[disconnect]] | ? |
| 多 site 并行 setup 块 | `test method editor` | 源文件 | — | [[on-first-invocation-begin]] / [[on-first-invocation-end]] | — |
| 逐 site setup 块（嵌套在上面那个块里） | ? | 源文件 | — | [[for-each-site-begin]] / [[for-each-site-end]] | — |
| setup focus / query focus 控制 | [[site-control-window]]（`93000 > System > Site Control`） | — | [[psfc]] / [[pqfc]] | [[controlling-multiple-sites]]（`SET_TEST_FOCUS`、`GET_TEST_FOCUS`、`CURRENT_SITE_NUMBER()` 等） | ? |
| 判定并写 datalog | [[test-suites-page]]（`Test Name` 列）（**图证**：`Test Name` 那一列确实存在——但在 Tests **页签**里，见证据节 ④（b）） | 源文件 | — | [[test]]、[[testset]]（`judgeAndLog_***`）、[[limit]] | ? |
| limit 的**值** | [[test-suites-page]] / [[testflow-properties-view]]（**图证**：`Lower Limit` 列在 Tests 页签里） | ? | — | [[limit]] | `getTestmethodLimitValue()` / `setTestmethodLimits()`（推断） |
| 用外部 CSV 控 limits 与 test number | `Test table editor`（`02.10.01.08.01.01`）（**图证**：`Test Number` / `Lower Limit` 两列） | [[structure-of-a-tmlimits-csv-file]] | — | [[tmlimits]]、`TestTable` / `TestNumGen` | ? |
| 在 test method 里执行固件命令 | ? | — | [[command-reference]]（`02.06` 全域；命令以**字符串**传入） | [[fw-task]] / [[begin-extension]] / [[end-extension]] | ? |
| 把缓存里的 setup 下载到硬件 | ? | — | [[flsh]]（另发 `WSDN`；`TM::APRM` 选项下再发 [[aprm]]） | [[flush]] | — |
| 编译出 UTM 库 | [[project-explorer-view]]（右键 → `Build Project`）、`Console view` | [[universal-test-method-library]]（`lib<工程名>.so`，落在 `Debug/` 子目录） | — | — | ? |
| 从 testflow 侧反向打开 / 编辑 test method | `Open Test Method` 快捷菜单（flow data editor） | 源文件 / test method 库 | — | — | ? |
| 把计算挪到后台线程（SMC） | ? | — | — | [[smartcalc-framework]]（`SMC_ARM()`） | — |
| 外部进程侧：挂 test method、读写参数与 limits | `test suite view`（**L3 文档自己的用词**） | ? | — | — | `attachTestmethod()`；`getTestmethodName()` / `getTestmethodParameterNames()` / `getTestmethodParameterValue()` / `setTestmethodParameterValues()`；`getTestmethodLimitValue()` / `setTestmethodLimits()`（推断） |

**表里没有的**：`02.06_Command_Reference` 里被 02.07 文档链到的那一大批
API↔命令对（`DPS_PIN_TASK` ↔ `DPSE`、`LEVEL_SPEC` ↔ `SVLR`、`SEQUENCER_STATUS` ↔ `SQGB`、
`TRANSITION_TEST_PINS` ↔ `TTVD`、`CLOCKFORWARDING_SET` ↔ `CFPR`/`CFDF`、
`DIGITAL_OFFSET_SEARCH_PINS.DigitalOffsetResultCopy` ↔ `TORC`、`RESULT_AREA_CONFIG_SET` ↔ `MSET` 等
实测 `02.07 → 02.06` 共 **272** 条边）。**它们是「某个任务对象的 API 对应哪条固件命令」，
不是本阶段的流程对照**——本页只留了第 12、13 两行（`FW_TASK` 通道与 `FLUSH`），
**其余归各自的命令页与对象页**（§2.5 的粒度）。

## 证据：哪几格是钉死的，哪几格只是「那边链过来了」

**证据分四档，本页不把它们混成一种。**

**① 语料明说对应（最硬）** —— 只有两处，都在 L1 那一列：

`02.07.04.01.69_FLUSH` 把 `FLUSH()` 的参数**逐条对到固件命令上**（逐字）：

> When to execute the firmware command FLSH and WSDN. It can be:

同一篇还说 `TM::APRM` 选项下会发 `APRM`：

> When using the TM:APRM option, the command APRM with mode set to CNL will be issued following the normal FLUSH() actions.

（这两句里的 `FLSH` / `WSDN` / `APRM` 在原文里都是**语料内部链接**；本页把链接名放在引号外，
引号里保留逐字原文。**第二句里有一个语料错字**，见「对不上的地方」④。）

`02.06.01.03.06`（L1 侧那一章自己的正文）反过来点名 L2 的 `FW_TASK`（逐字）：

> You can execute a firmware command from a test method with the FW_TASK API.

**双向都有链接**：`02.06.01.03.06` → `FW_TASK`（2 条）与 `HpFwTask`（1 条）；
`02.07.03.10` 与 `02.07.04.01.77_FW_TASK` 各自 → `02.06_Command_Reference`。

**② 文档之间有链接（次硬，逐条可查）** —— 取自 `extract/edges.jsonl`
（`resolved=true`，路径为 raw 相对路径）。**本页主表里绝大部分格子靠这一档**：

| 源文档 | 层 | 链到（同名多条合并计数） | 条数 |
|---|---|---|---|
| `01.06.02.01_1._Create_a_Test_Method_Project.md` | GUI | `02.07.02.02.01` | 1 |
| `01.06.02.02_2._Create_a_Test_Method_Class.md` | GUI | `02.07.02.02.02` | 1 |
| `01.06.02.03_3._Add_the_source_code.md` | GUI | `addLimit`、`SEARCH_FUNC_TASK`、`CONNECT`、`ON_FIRST_INVOCATION_BEGIN`、`ON_FIRST_INVOCATION_END`、`TEST` | 6 |
| `01.06.02.04_4._Build_the_project_to_get_the_universal_test_method_library.md` | GUI | `02.07.02.02.02` | 1 |
| `02.07.02.02.02_How_to_create_a_universal_test_method_class.md` | L2 | `Tests_page`、`Testflow_Properties_view`、`Console_view` + 6 篇参数类型 | 13 |
| `02.07.04.01.241_TEST.md` | L2 | `02.08.04.32.03.01.03_Tests_page` | 1 / 共 40 |
| `02.08.04.27.03_Changing_the_site_in_focus.md` | GUI | `02.07.03.13`、`02.06.01.05`、`02.06.03.01.10.03`、`02.08.04.27.01` | 4 |
| `02.06.03.01.10.03_Defining_the_query_focus.md` | L1 | `PQFC`、`02.06.01.05`、`02.08.04.27.03`（**回指那篇 GUI**）、`02.08.04.27.01` | 4 |
| `02.07.03.13.03.01_Controlling_the_Setup_Query-Focus_Automatically.md` | L2 | `PSFC`、`PQFC`、`02.08.04.27.03`（**GUI**）、`ON_FIRST_INVOCATION_BEGIN` 等 | 15 / 12 个唯一目标 |
| `02.06.01.03.06_Executing_firmware_commands_from_within_a_program.md` | L1 | `FW_TASK`、`HpFwTask` | 3 |
| `02.07.04.01.77_FW_TASK.md` | L2 | `02.06_Command_Reference`、`DIAG`、`NOOP`、`02.06.01.01_V93000_Firmware_Overview` 等 | 17 / 9 个唯一目标 |
| `02.07.04.01.69_FLUSH.md` | L2 | `FLSH`、`WSDN`、`APRM`、`FTCG`、`SQST`、`CONNECT`、`PRIMARY_STATUS` 等 | 18 / 10 个唯一目标 |
| `02.07.04.01.126_LIMIT.md` | L2 | `ON_FIRST_INVOCATION_BEGIN`、`FOR_EACH_SITE_BEGIN` | 11 / 4 个唯一目标 |
| `02.08.04.32.02.06.01.06_Pass_Fail_type_and_ERROR_MAP_type.md` | GUI | `TEST`（2）、`GET_FUNCTIONAL_RESULT`（2）、`ARRAY_X_type` | 8 / 3 个唯一目标 |
| `02.10.01.08.01.02_Generating_test_numbers_from_a_test_method.md` | L2 | `TestTable`、`TestNumGen`、`TMLimits`、`Alphabetical_list_of_flags`、`Generating_test_numbers_from_the_SmarTest_GUI`（**GUI**） | 7 / 5 个唯一目标 |
| `02.10.01.08.01.01_Generating_test_numbers_from_the_SmarTest_GUI.md` | GUI | `Test_table_editor`、`Saving_test_numbers_as_TMLimits_CSV_files`、`Generating_test_numbers_from_a_test_method`（**L2**） | 7 / 6 个唯一目标 |
| `02.07.04.01.250_TMLimits.md` | L2 | `Structure_of_a_TMLimits_CSV_file`、`LIMIT`、`TEST`、`TESTSET`、`SMC_ARM` 等 | 54 / 10 个唯一目标 |
| `02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.md` | 文件 | `TMLimits` | 1 |
| `01.03.03.02.01_Editing_test_methods_efficiently.md` | GUI | `02.07.02.01`、`02.07.02.10` | 4 / 4 个唯一目标 |

**链接证的强度要说清**：一条链接**只证明「那篇文档认为读者该去看这一篇」**，
**不证明两个东西等价**——可能是「见也」，也可能是「区别在这里」，也可能是「前提」。
**本页只在主表的同一行里用它们，不跨行搬。** 最干净的一行是第 8 行（site focus）：
一篇 GUI 文档（Site Control 窗口）同时链到 L2 的 `02.07.03.13` 与 L1 的
`02.06.01.05`、`02.06.03.01.10.03`，**而 L1 那篇又链回这篇 GUI**——
**同一行的三列各有独立的链接，且互为回指。**

**③ 只有一侧、没有另一侧的证据** —— 主表里 L1 或 GUI 填了 `?` 的那些格：
`CONNECT`/`DISCONNECT`、`FOR_EACH_SITE_*`、`FLUSH`、`FW_TASK`、`SMC_ARM()` 的 **GUI 格**，
以及所有含 `?` 的 **L3 格**。**`?` 的意思是「本页没找到证据」，不是「不存在」**
（见「对不上的地方」①）。

**④ 图证（2026-09-20 加，本页用到了）** —— 从 raw 自带的截图里读出来的。
（`schema.md` §2.5 把图证列为第 **④** 档——**本页的 ④ 就是这一档，编号没有让位**。）

**本页 sources 里带图的文档共 12 篇 / 31 张。本页读了四张**，**其余二十七张没看**
（大半是 `02.07.02.10` 的六张警告框与 `02.10.01.08.01.01` 的三张）。
**先给结论，而且这一页的结论是六页里最不客气的**：
**四张图没有填掉任何一个 `?`，也没有把任何一格（推断）升成文档事实。**
本页的 `?` 全在 L1 的 `CONNECT`/`DISCONNECT` 与 L3 那几格上，
**四张图里既没有固件命令名、也没有 L3 的 API 名**（只有 L2 的 `PUT_DATALOG`/`PUT_DEBUG`，
而那一列本来就有名字）。逐张：

**（a）`113136.png`（`02.07.02.02.01`，alt `New Test Method Project wizard`）—— 向导截图。**
六格逐字是：`Project Name:` = `act299_tml`、`Use Default Location`（勾选）、
`Location:` = `/home/demo/devices/act299_tml`（灰）、
`Import a system Test Method project`（未勾）、`Please select:`（灰）、
`Referenced by current device`（勾选）；按钮 `Finish` / `Cancel`。
**它印证主表第一行的 GUI 格**（那个向导）**与 `文件` 格**——图上 `Location` 的默认值
`/home/demo/devices/act299_tml` 正好是「device 目录 + 工程名」，与 `.02.01` 正文那句
`The default location of the project is in the same directory with the device directory.` 对得上。
**但它一个字都没多说**：`Referenced by current device` 与 `Use Default Location` 在语料里都能搜到，
`act299_tml` 这个例子名**在本页 sources 的 `01.06.02.01` 里也有**——
**按 §11.4 的判据（图里的字搜不到才算图证），这一张的贡献接近于零。**

**（b）`110086.png`（`02.10.01.08.01.01`，alt `Clicking the Tests tab in the tabular testflow editor`）
—— 这一张有真东西。** 图是 tabular testflow editor 的 **`Tests` 页签**（文件页签 `utm_testflow`），
表头逐字是 `Testsuite Name | Test Name | Test Number | Lower Limit`（再往右还有列，被窗口裁掉），
行逐字有 `1 continuity / [TF]Continuity`、`2 meas_bandgap_bias / VDAC_IBIAS_1 / -1.1 / <=`、
`3 FW_FTCG_off2 / [TF]FW_escape`、`4 VDD_continuity2 / [TF]Standby Current`、
`6 FW_FTCG_off_again / [TF]FW_escape`、`7 FW_FTCG_off1 / [TF]FW_escape`、
`8 VDD_continuity1 / [TF]Standby Current`、`9 FW_FTCG_on1 / [TF]FW_escape`；
底部页签逐字是 `Testsuites | Testtree | Bins | Flags | Setups | Variables | Tests | Parameters |
Information`。
**它印证主表的三格**（表里已标「（图证）」）：判定并写 datalog 那行的 GUI 格
（`Test Name` 列确实存在）、limit 的值那行的 GUI 格（`Lower Limit` 存在）、
「用外部 CSV 控 limits 与 test number」那行的 GUI 格（`Test Number` 与 `Lower Limit` 同表）。
**同时它给出一处本页要照实记的用词差**：本页表里写的是 `Test table editor`，
**而图上这几个列所在的页签叫 `Tests`，所在窗口是 tabular testflow editor**
（该篇正文里逐字出现过 `the tabular testflow editor` 与 `Click the Tests tab.` 两处，
**本页只引这两个片段，没有用省略号接句子**）。
`Test table editor` 是**同一篇链出去的另一篇**（`02.10.01.08.01.01.01`），
**不在本页 sources**——**本页照实并列两个名，没有把 `Tests` 页签改写成 `Test table editor`。**
**grep 不到**：`utm_testflow`（0 命中）、`meas_bandgap_bias`、`VDAC_IBIAS_1`、
`VDD_continuity`、`FW_FTCG`（均 0 命中）。
**一处要照实说的例外**：`[TF]Continuity` 有 1 命中，在
`02.08.04.32.02.01.16_Exporting_a_testflow_to_a_CSV_file.md`——**那一篇不在本页 sources**，
**本页没有读它**，所以**不知道那里的 `[TF]` 与图上这个 `[TF]` 是不是同一个意思**。
`Standby Current` 有 2 命中，但两篇都不是本页 sources，**且都不是这张表**。
**它答不了的**：那一行 `文件` 格是 [[structure-of-a-tmlimits-csv-file]]，
**图里没有 CSV 的任何一行**。

**（c）`116534.png`（`02.07.02.02.02`）—— Properties 视图截图。**
逐字：`Property | Value` 两列，`Test Method Parameters` = `17`，`title` = `Example`，
以及一个参数 `x` 展开后是 `start` = `0`、`stop` = `10`、`step` = `1`、`scale` = `Linear`。
**它印证主表第二行**（建 test method 类：参数）**的一部分**——
**「向导里声明的参数最后出现在 Properties 视图里」这件事图上看得到**。
**但它不是那条链的第二半**：那个位置**应该是源文件 `.cpp` / `.h`**，
而**图上不是源文件**（见「对不上的地方」⑨）。
**grep 不到**：`Test Method Parameters` 只在 `03.02` 那三篇里出现，**不在本页 sources**。

**（d）`71093.png`（`02.07.02.02.02.01`，alt 位置正文是
`A list displays the candidates followed by the elements that start with the letter combination you typed.`）
—— 这一张画出了源文件。** 图是编辑器里按 `Ctrl+Space` 后的候选框：候选逐字有
`PUT_DATALOG(const STRING & comment)`、`PUT_DATALOG(const STRING & pin, const ST…`、
`PUT_DEBUG(const STRING & pin, const STRI…` 等多条；**框后面就是源码正文**，
可辨认的行有 `// Link to` 开头的一行注释、`num_` / `spec_` / `DSP_` 开头的几行
以及一行 `DB, ref_level_DAC, RECT, 0);`。
（**候选框里那几条半截的 `…` 不是我加的省略号，是图上列表框自己把长条目截断了**——
`PUT_DATALOG(const STRING & pin, const ST…` 到图上就到这里。）
**它印证主表第四行的 GUI 格与 `文件` 格**（`test method editor` 的 `Content Assist`、
产物是 `.cpp` 源文件）——**这是本页四张图里唯一一张同时出现「编辑器」与「源文件正文」的。**
**grep 不到**：`RECT, 0)`（0 命中）。**照实说一处**：`ref_level_DAC` 有 1 命中，在
`02.07.02.12.01.01_How_to_implement_a_concurrent_test_method.md`——**那一篇不在本页 sources，
本页没有读它**，所以**不知道那一行与图上这一行是不是同一段代码**。
**它答不了的**：候选框里**没有任何一个向导字段名**——所以它也**答不了**第 ⑨ 条那个问题。

**图证整体答不了的三件事，照实说：**

- **四张图没有一张出现固件命令名。** 主表 L1 列那两个 `?`（`CONNECT`/`DISCONNECT`）
  与 `FOR_EACH_SITE_*` 那一格，**图一格都没动**。
- **四张图没有一张出现 L3 的 API 名。** 所以 L3 那三格（推断）**全部留在原处**。
- **四张图里，只有（b）与（d）有「图里才有的字」**；（a）与（c）的字**在 raw 里都搜得到**
  ——**本页不把它们当图证充数**（§11.4 的判据是「拿图里的字去 raw 里 grep 是 grep 不到的」）。

## 对不上的地方

**① L3 那一列，跨层链接证据是零——这是本页最值得记的一条。** 实测：

- `02.09.01.14`（Test suite control API）全族 **92 条出链，一条都没有离开 `02.09`**；
- testmethod 那 9 个成员**逐条的入链只有两个来源，而且 9 条完全一样**：
  `02.09.01.14.02.01_TestsuiteProxy.md` 的成员函数清单，和
  `02_System_reference/index.md`（`02.09` 那一级的 index，不是 `02.09.01.14` 自己的）。
  **没有任何 GUI / 文件 / L1 / L2 文档链到它们。**

所以第 17 行是我**按 L3 文档自己的 `Subtopics` 清单排出来的**（**推断**，依据是
`02.09.01.14.02.01_TestsuiteProxy.md` 逐条列出的成员名与分类号），
**而 GUI / 文件两格留 `?`**——**我没找到它们和 GUI 的链接，不是语料说它们没关系。**

**② 第 17 行 GUI 格的 `test suite view` 是 L3 文档自己的用词，本页没有核对它是不是
`Tests page` 或 `Properties view`。** 原句（`02.09.01.14.02.01.31`，逐字）：

> This function sets values for the limits and test numbers defined in test method, test method API and test suite view.

**`test suite view` 在本页别处没有出现过**（第 10 行那两个 GUI 的名字来自另一篇文档）。
**本页按「同名不同物」处理：不合并、也不说它们是同一个东西。**

**③ 语料自己矛盾：同一个工程名，第 1 步和第 2、4 步不一样。** 三处逐字——

第 1 步（`01.06.02.01`）：

> The default project name is act299_tml.

第 2 步（`01.06.02.02`）：

> To create a new Test Method Class, right-click the project Utmmethod and select New > Test Method Class from the shortcut menu.

第 4 步（`01.06.02.04`）：

> In the Project Explorer, right-click the project Utmmethod and select Build Project from the shortcut menu.

**`act299_tml` 与 `Utmmethod` 是两个名字。** 本页照实记下、**一处都没替它改**；
**哪个是错的、`Utmmethod` 是什么，语料没说**——所以主表第 1、2、14 行的
「工程名」一律写成 `<工程名>` 占位，**不填任何一个具体名字**。

**④ `02.07.04.01.69` 有一处语料错字。** 同一篇里 `TM::APRM`（正确写法）与
`TM:APRM`（少一个冒号）**并存**：

> When using the TM:APRM option, the command APRM with mode set to CNL will be issued following the normal FLUSH() actions.

**`TM:APRM` 应为 `TM::APRM`。** 本页把它原样留在引文里（**引文不许替语料修字**，§11.2）。

**⑤ `02.10.01.08.01.02` 有一处语料漏字，本页照抄、也不替它补。**

> You can also export the entire TestTable object to a CSV file for use in a different tool using the writeCsvFile() function write the modified test numbers back to the testflow using writeTestflow().

**`function` 与 `write` 之间缺一个连接词**（读作 `function, or write` 才通）。
本页不替它补——补了就成了本页编的句子。

**⑥ `02.07.02.02.02` 有一处语料错字，本页只记它在本表第 2 行里的后果**：
`In Templates filed, select:` 里的 **`filed` 应为 `field`**（这条
`wiki/concepts/how-to-create-a-universal-test-method-class.md` 已记过一次，
本页不重复它的上下文）。**主表第 2 行 GUI 格引用了向导，所以它落进本页的证据链里。**

**⑦ `run()` 与 `initialize()` 不是 API 参考条目，主表第 4 行 L2 格的 `run()` 是（推断）。**
`02.07.04_API_Reference` 自己定的命名约定是三类：**API** 写成 `ApiName()`、
**Class** 写成 `ClassName`、**Member function** 写成 `ClassName.CMemberFunction()`——
**`run()` / `initialize()` 三个形状都不占**（它们是 test method class 的入口函数）。
把它们放进 L2 那一格是**本页按职责排的**（**推断**），依据是 `02.07.02.02.02` 那句
`For normal test method, enter your source code in the run() function.`——
**那句是文档事实，「`run()` 属 L2」这个归类是本页做的。**

**⑧ 第 5 行 L1 格是 `?`，第 6、7 行 L1 格是 `—`——这个区别是本页有意判的。**
`ON_FIRST_INVOCATION_*` 与 `FOR_EACH_SITE_*` 是**纯 test method 侧的作用域块**，
固件层没有对应物，所以给 `—`；而「连接 / 上电」在固件层**确实有东西**
（`02.06` 里的 routing / relay 一类命令在 `02.07.04.01.68.01_FLEX_PIN_RELAY` 那篇里就被链到过），
**但语料没说 `CONNECT()` 对应哪一条**——所以给 `?`。
**看起来像不算证据**（§2.5：不许猜）。

**⑨ 图能读，本页读了四张——原先写的「图在语料树之外」是错的；但那一句的结论本页查完之后仍然成立。**
（**2026-09-20 更正**）

`../../../../raw/x.png` 往上四层正好是 `tdc-html/`，**图就在 `tdc-html/raw/` 里，读得出来**
（`schema.md` §11.4）。**本页 sources 里带图的文档共 12 篇 / 31 张，本页读了四张**
（`113136.png` 向导、`110086.png` Tests 页签、`116534.png` Properties 视图、`71093.png` 源码候选框；
逐张见证据节 ④）。**读完之后的结论分两半，一半是新的，一半是旧结论被换了理由：**

- **新的一半**：**（b）`110086.png` 与（d）`71093.png` 给了本页原先没有的东西**——
  （b）把 limits 与 test number 在 GUI 上的**列名**（`Test Name` / `Test Number` / `Lower Limit`）
  与**页签名**（`Tests`）摆出来了，（d）把 `Content Assist` 的候选框**叠在源码正文上**画出来了。
  **两条已进主表（标「（图证）」）。**
- **旧结论仍然是旧结论，但理由换了**：**「向导里哪个字段对应文件里哪一行」这个粒度，
  四张图一张都没答。** 做不到**不是因为图够不着**，是因为**四张图里没有一张把「向导那一格」
  和「它生成的那一行源码」放在同一张图上**：（a）只有向导本身，（c）是 **Properties 视图**
  而不是源文件，（d）有源文件**但没有任何向导字段名**。
  **所以要答这一格，靠的不是再开图，是去找一份画着生成后源码、或写着生成规则的文档。**

**另外本页顺手改正一处用词**（也在证据节 ④（b）里记了）：本页表里「用外部 CSV…」那行写的是
`Test table editor`，**而（b）那张图上，那几个列所在的页签叫 `Tests`、窗口叫 tabular testflow editor**
——`Test table editor` 是**该篇链出去的另一篇**（`02.10.01.08.01.01.01`），**不在本页 sources**。
**本页照实并列两个名，没有把图上的 `Tests` 改写成 `Test table editor`。**

**⑩ `extract/prose-allowlist.txt` 里没有 `mapping-pin`。** 本页因此**不能**把
`mapping-pin` 写成 wikilink，只能写成 `` `mapping-pin` `` + 路径（见本文开头）。
**这是清单的现状，不是本页的选择**——记下来，免得下次有人以为是笔误。

## 出处

`sources:` 三十一篇，全部在 frontmatter 里。读的深浅不一样，分开说：

- **整篇读完的**：`01.06.02.01`–`01.06.02.04`（四步 GUI 走查，每篇 1 KB 上下）、
  `02.07.02.02.01`、`02.07.02.02.02`、`02.07.02.10`、`02.07.03.10`、`02.07.04.01.69`、
  `02.06.01.03.06`、`02.06.03.01.10.03`、`02.08.04.27.03`、
  `02.08.04.32.02.06.01.06`、`02.10.01.08.01.02`、`02.10.01.08.01.01.03.01`、
  `02.09.01.14.02.01` 及其 9 篇成员文档。
- **只读了开头几十行的**：`02.08.04.32.03.01.03`（`Tests page`，读了前 30 行）、
  `02.08.04.32.03.04`（`Testflow Properties view`，前 30 行）、
  `02.10.01.08.01.01`（前 20 行）、`02.07.02.02.02.01`（前 25 行）、
  `02.07.02.02.02.02`（前 20 行）。
  **这几篇只用到了它们开头那几句，本页没有它们后文的结论。**
  （`02.07.02.02.02.01` / `.02` 是 `Content Assist` 与 `Test Method Panel` 两篇，
  **主表第 4 行 GUI 格里那两个名字就是从它们的标题与首段取的**。）
- **`02.06.01.05` 读了命令表全文**（`Site dependent firmware commands`，1,400 余行），
  但**只取了它开头的定义句与 `PSFC`/`PQFC` 两行**。

**本页没做的**：

- **272 条 `02.07 → 02.06` 的边，只用了两条。** 其余的对（`DPSE`、`SVLR`、`SQGB` 等）
  **本页没有回到命令原文复核，也不打算复核**——它们是命令页的活（见「表里没有的」）。
- **L3 那一族只读了 9 篇成员 + 1 篇索引。** `02.09.01.14` 的其余四十来篇
  （session / execute / level / timing 那些）**一篇没读**——它们不属于本阶段。
- **`02.09.01.09`（TPI）只见到一条边。** `02.06.01.03.06` 链到了 `HpFwTask`，
  **`HpFwTask` 自己那篇没读**，所以本页对 TPI 侧 `?` 与 `—` 的判断**只覆盖 TestsuiteProxy 那一族**，
  **不构成「TPI 里没有对应接口」的断言**。
- **看了四张图（2026-09-20 加）。** 就是 `113136.png`、`110086.png`、`116534.png`、`71093.png`
  （各自出自哪篇、图里逐字有什么，见「证据」④ 与「对不上的地方」⑨）。**四张都整张看完**，
  图上读到的字**逐条回 9,398 篇 raw md 里查过 grep 命中**——本页凡写「grep 不到」的都是实测 0 命中，
  **凡有零星的别处命中，都在 ④ 里照实写了是哪一篇、以及本页有没有读过它**。
  **本页 sources 里带图的文档共 12 篇 / 31 张，其余二十七张没看。**
  **原先本页在「对不上的地方」⑨ 里写着图「在语料树之外」——那是错的**，见 ⑨ 的更正。
- **没有实跑。** 没有开过向导、没有建过 UTM 工程、没有编译过库、没有跑过 test suite。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/testmethod.md`。
  后者是**待办**：那页目前不知道本页存在。

**本页 `layer: n/a` 的理由**：§6 要求 mapping 页必填 `layer`，而本页**本身不属于任何一层接口**
（它是对照表，不是接口）——`n/a` 是这个六值枚举里为这种情况准备的值。

`verified: doc-only`
