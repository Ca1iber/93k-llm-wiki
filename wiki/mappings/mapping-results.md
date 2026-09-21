---
type: mapping
title: Results 段的五层对照
layer: n/a
stage: results
tags: [mapping, results, gui, firmware-command, test-method-api, external-interface, error-map, edf, stdf, datalog, tmlimits, shmoo]
related: [results, error-map-tool, error-map, result-configuration, hidden-upload, integrated-result-tool, event-formatter, smartest-data-formatter, report-window, data-logging-profile, data-logging-profiles, data-logging-profile-api, flags-page, alphabetical-list-of-flags, data-retrieval-library, drldump, lot-summary-generator, edf, edl-file, edf-data-organization, edf-data-types, stdf, tmlimits, structure-of-a-tmlimits-csv-file, test-summary-tab, raw-data-views, data-navigation-views, device-summary-tab, wafer-summary-tab, hardware-bin-summary-tab, software-bin-summary-tab, shmoo-tool, signal-analyzer, timing-diagram-tool, list-of-test-result-commands, testset, testset-testname, test-suite-control-api, offline-result-emulation, limit]
sources:
  # --- GUI 侧（02.08） ---
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01_Error_Map.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01.02_Setting_the_acquisition_mode.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.02_Using_the_Error_Map_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.03.01.04_Result_menu.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04_Result_Configuration.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.01_Result_Mode.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.05_Hidden_Error_Map_Upload.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.01_Raw_data_views.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25.03.02.02_Test_modes.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25.03.07_Saving_shmoo_plots_to_png_or_ASCII_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.02.02_Waveform_Graphs_Tool.md
  # --- L1 侧（02.06；只读了命令示例页与 CYRM 的三份投放，其余命令页没读，见「出处」） ---
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.06_Result_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.05_CYRM__CYRM__-__CYcle_Resolution_Mode.md
  - 02_System_reference/02.06_Command_Reference/02.06.09.02.01_CYRM__CYRM__-__CYcle_Resolution_Mode.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.37_CYRM__CYRM__-__CYcle_Resolution_Mode.md
  # --- L3 侧（02.09） ---
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.19_Set_the_data_logging_profiles.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.28_SetErrorMapMode.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.16.02_How_to_capture_the_test_result_in_real_time.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.16.04_How_to_control_event_data_logging_with_BLC_API.md
  # --- 文件侧（02.10） ---
  - 02_System_reference/02.10_Data_Logging/02.10.01.02.07_Data_logging_profiles_and_sampling.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.02.08_Data_logging_profile_API.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.01_Test_table_editor.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Results 段的五层对照

## 这张表在说什么

Results 这一段**和 pin 那一段的形态正好相反**。

pin 那一段，语料自己给了一句 `corresponding exactly to` 把「GUI ↔ 文件 ↔ 固件命令」整链钉死，
但 **L2 / L3 基本是空的**。results 这一段反过来：**语料没有给一句同级的统括句**，
可是 **五层（GUI / 文件 / L1 / L2 / L3）在语料里全都真的存在**，
而且存在的方式是**同一件事被三套文档各写了一遍**——命令侧一套、test method 侧一套、
外部进程侧一套。本页就是把这三套按「目的」并排放。

**本页能找到的最接近「统括句」的一段，只在 Result Configuration 这一格上成立**
（`02.08.04.08.04_Result_Configuration.md`，原文一整行、没有断行）：

> 「If you want to store the result configuration, you must create a test method from the RESULT_CONFIGURATION test method API. The following table indicates which member functions of this API correspond to the individual settings of the Result Configuration interface.」

**`correspond to the individual settings` 这句话只覆盖 Result Configuration 这一个 GUI 窗口**，
它**不覆盖 EDF、STDF、TMLimits、shmoo、波形这几块**。所以本页的地基比 pin 那页碎：
**每一行各找各的证据**，没有一句能用到底。这一点是本页与 `mapping-pin.md` 最大的差别。

**L3 侧的地基句**在 `02.09.01.16.02`（章 `02.09.01.16` Critical tasks in production environment）：

> 「In SmarTest, event data logging is provided to retrieve the test result data from the production environment.」

**这一句把「结果数据」与「外部生产环境」直接连起来**——results 段的 L3 不是补出来的，
是语料自己开的头。

**本页的书写约束（先说清，免得读者以为漏了东西）**：
**L1 列挂不出任何页间链接。** 结果命令（`EMAP?`、`DCRM`、`CYRM`…）
**没有一个名字在 `extract/prose-allowlist.txt` 里**，所以 L1 列**全部**是
「反引号包住的名字 + 文档号」。这不是本页偷懒，是 §9.1 那条规矩的直接后果。
L1 列唯一能挂链接的是**清单页** [[list-of-test-result-commands]]。

## 对照表

**读法**：一格填了名字 = 有证据（是哪一档证据见下一节）；`?` = 语料没说，
**本页不猜**（「本页没找到」）；`—` = 这一层**不存在**这个对应物（不是「没找到」）。
**带（图证）的格 = 那一格的名字在 raw 的图上直接看得见**——
是哪张图、图里的字为什么搜不到，见证据节 **④** 与「对不上的地方」**⑬**。

| 目的 | GUI | 文件 | L1 命令 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 配置 detailed error map 的粒度、error code 分辨率、存放位置 | [[result-configuration]]（`Result Mode` tab）（**图证**：页签与五个设置项的字面，见证据节 ④） | `?` | `CYRM, CYRM?`（`02.06.11.02.05`）、`CYRP`（`02.06.11.02.06`）、`DCRM`（`02.06.11.02.10`） | `RESULT_CONFIGURATION` 的 `setResultWidth()` / `setNumberOfResultsPerCycle()` / `setEdgeToResultMapping()` / `setResultStorageLocation()` / `setResultStorageLocationExceptionPinList()` | `?` |
| 决定 error map 记全部 cycle 还是只记 fail cycle | [[error-map-tool]]（`Result > Acquisition Mode`） | `?` | `?` | `Result areas for error map data`（`02.07.04.01.190.09`） | `?` |
| 取回 error map 内容与 error 计数 | [[error-map-tool]] | [[error-map]] | `EMAP?`（`02.06.11.02.18`）、`ERMP?`（`02.06.11.02.22`）、`ERCT?`（`02.06.11.02.20`）、`ERCY?`（`02.06.11.02.21`）、`FFCI?`（`02.06.11.02.23`） | `?` | `?` |
| 把 error map 的上传藏到一次 digital test 背后 | [[hidden-upload]]（`02.08.04.08.05`）（**图证**：例子 testflow 的节点顺序，见证据节 ④） | `?` | `Configuring the Error Map recording`（`02.06.11.01.02.01`） | `?` | `?` |
| 规定「记录哪些数据」「隔几颗记一颗」 | [[flags-page]] / [[alphabetical-list-of-flags]]（`datalog_sample_size`） | [[data-logging-profiles]]（`.prf`） | `?` | [[data-logging-profile-api]] | `SetSamplingProfiles`（`02.09.01.08.05.04.19`） |
| 测试编号与 limit 表 | `test table editor`（`02.10_Data_Logging/02.10.01.08.01.01.01_Test_table_editor.md`） | [[structure-of-a-tmlimits-csv-file]]（`02.10.01.08.01.01.03.01`） | `?` | [[tmlimits]]（`02.07.04.01.250`） | `?` |
| 把结果落成人读的报告与机器读的 STDF | [[event-formatter]] / [[smartest-data-formatter]] / [[report-window]] | [[stdf]]、`.formatterrc.def`（`02.10.02.13`） | [[lot-summary-generator]]（GDF test summary） | `TESTSET`（`02.07.04.01.244`）、`TESTSET::judgeAndLog_ScanTest`（`02.07.04.01.244.15`）、`TEST`（`02.07.04.01.241`）、`PUT_DATALOG`（`02.07.04.01.174`） | `02.09.01.16.04`（BLC API） |
| 实时 / 离线读回结果（data log stream） | [[integrated-result-tool]] | [[edf]] / [[edl-file]] | [[drldump]] | [[data-retrieval-library]] | `02.09.01.16.02`（How to capture the test result in real time） |
| 统计评估与下钻到单条记录 | [[integrated-result-tool]]（[[test-summary-tab]] / [[raw-data-views]]（**图证**：表头 `Test` / `Test#` / `Pin` / `Value` / `Unit` / `P/F`）/ [[device-summary-tab]] / [[wafer-summary-tab]] / [[hardware-bin-summary-tab]] / [[software-bin-summary-tab]]） | [[edl-file]] / [[stdf]] | `?` | [[testset-testname]]（`02.07.04.01.244.23`）、`PUT_DATALOG`、`TESTSET` | `?` |
| shmoo 测试的数据采集与呈现 | [[shmoo-tool]] | `.formatterrc.def`（`02.10.02.13`）、shmoo 图目录 | `?` | `SHMOO_RESULT`（`02.07.04.01.227`）、`TESTSET::judgeAndLog`、`Shmoo`（`02.07.05.01.09`） | `?` |
| 波形查看 | [[signal-analyzer]] | `?` | `?` | `Data Display API`（`02.07.04.01.22`） | `?` |
| 高分辨率时序图 | [[timing-diagram-tool]] | `?` | `?` | `?` | `?` |
| 结果的产物文件（外部程序取 / 存 / 合 / 删） | `?` | [[edf]] / [[error-map]] / [[stdf]] / [[edl-file]] | `?` | `?` | `dm_emap` / `dm_fam` / `dm_report` / `dm_scan_res` / `dm_dataform`（`02.09.01.09.02`） |

**格子计数**：13 行 × 6 列（`目的` + 五层）= **78 格**。
填了名字 **51 格**，`?` **27 格**，`—` **0 格**。

**表外的一句**：`02.09.01.16.04` 那一行的 L3 不是「一个接口」，是**一条路**——
它给的是一次执行里从 `IssueEDLEvent` 到 `MoveEDLStream` 的完整写法，
落点文件在代码里逐字写着：

```
inputParams["DEST_EDL_FILE"] = "/tmp/new_datalog_file.log";
```

## 证据：哪几行是钉死的，哪几行只是「那边链过来了」

**证据分四档，本页不把它们混成一种。**

**① 文档明说对应（最硬）** —— 只有一行拿到：

- **「配置 detailed error map」行。**
  `02.08.04.08.04` 明写**存这项配置的唯一办法**是建一个 `RESULT_CONFIGURATION`
  test method，并且**给了 GUI 设置 ↔ 成员函数的对应表**。这是本页唯一的「明说」级证据。
  它的 L1 格（`CYRM` / `CYRP` / `DCRM`）另有链接背书，见下档。

**② 文档之间有链接（次硬，逐条可查）** —— 取自 `extract/edges.jsonl`。
**范围说清**：源文档取本段的六族（`02.08.04.08` / `.13` / `.25` / `.26` / `.33` 与 `02.10.`），
**去掉 `02.08.04.34`（那是 `02.06.06.02` 的整章镜像，§10 已认定重复投放）**，
再取这些文档的**跨层**出入边，共 **478 条**（不含 `index.md`）。分方向：

| 方向 | 条数 | 典型例子 |
|---|---|---|
| GUI → L1 | 12 | `02.08.04.08*` 一族（11 条，含 `02.08.04.08.05` 与 `.05.01` 的 3 条）→ `CYRM`/`CYRP`/`DCRM` 组合表、`Location of the detailed Error Map`、`Dealing with storage problems on Smart Scale systems` |
| GUI → L2 | 38 | `02.08.04.25*` → shmoo 一族（25 条，其中 9 条到 `SHMOO_RESULT` 及其子页）；`02.08.04.26.02*` → `Data Display API`（8 条）；`02.08.04.13.03.03.01` / `.02` → `PUT_DATALOG` / `TESTSET`（4 条） |
| GUI → 文件 | 44 | `02.08.04.25.03.07` → `Event Formatter` 一族（14 条，含 `Appendix B: Event Formatter Defaults` 的 7 条）；`02.08.04.25.03.02` → `Structure of a TMLimits CSV file` |
| GUI → L3 | 1 | `02.08.04.26.02.05.05.10` → `SmarTest Program Manager`（**与结果无关，是 PPSG 那条线**） |
| 文件 → GUI | 60 | `02.10.01.09.01` / `.09.02`（data logging flags）→ `Alphabetical list of flags`（27 条） |
| 文件 → L2 | 68 | `02.10.01.02.08` → 四个 profile 类页（14 条）；`02.10.03.04.03` / `02.10.03.05.*` → `TESTSET` 一族（15 条） |
| 文件 → L3 | 12 | `02.10.01.02.07` → `Set the data logging profiles`；`02.10.02.07` → `Recommended implementation structure` |
| 文件 → L1 | 3 | `02.10.02.05.01`、`02.10.03.05.27.03` → `CYRM` |
| L2 → 文件 | 135 | `TMLimits` 一族、STDF 记录页一族 |
| L2 → GUI | 52 | `02.07.05.01.09_Shmoo` → `02.08.04.13` / `.25.*`；`SHMOO_RESULT` → shmoo 工具页 |
| L1 → GUI | 6 | `02.06.11.01.02.01.06` → `Error Map` / `Error Map Tool`；`FFCI?` / `FFPM?` → `Error Map` |
| L1 → 文件 | 1 | `02.06.01.03.05_Using_the_Trace_Function` → `02.10.01.01.04_Activating_event_data_logging`（**本页没用它**，那是 trace 那条线） |
| L3 → 文件 | 46 | `02.09.01.16.02.*` → `DRL*` 函数页、`Event types`、`Attribute types`、`EDF`、`DRLDump`、`Event Formatter` |

**链接证的强度要说清**（同 `mapping-pin.md`）：一条链接**只证明「那篇文档认为读者该去看这一篇」**，
**不证明两个东西等价**——可能是「见也」，也可能是「区别在这里」，也可能是「前提」。
本页只在主表的**同一行**里用它们，**不跨行搬**。

**③ 只有单侧证据** —— 主表里 L1 格填了命令、而 GUI 格是同一族但不是同一个窗口的那些行。
例如「取回 error map 内容」行的 L1（`EMAP?` 一族）有 `02.06.11.01.02.01.06`
反向链到 [[error-map-tool]] 背书，**但那条链接说的是「怎么用这些命令」，
没说「这个工具就是这些命令的 GUI」**——后者是本页按各工具职责排的（**推断**），
依据是 [[error-map-tool]] 自己的定位句
（`02.08.04.08.01`：**`All result analysis tools (Error Map Tool, Timing Diagram etc.) use the error map to generate different views to the results you obtain when performing tests.`**）。

**附：只有名字、没有链接** —— 主表里**唯一**一格是「决定 error map 记全部 cycle 还是只记 fail cycle」
那一行的 **L3**。本页**没有填它**（写的是 `?`），理由见「对不上的地方」④。

**④ 图证（2026-09-20 加，本页用到了）** —— 从 raw 自带的截图里读出来的。
（`schema.md` §2.5：**④ = 图证**。）

**本页 sources 里带图的文档共 8 篇 / 37 张**（数量集中在
`02.08.04.13.03.02.01` 与 `.13.03.03.01` 两篇的图标小图上）。**本页读了五张**，
挑的是与主表待答格子有关的那几张；**其余三十二张没看**。
逐张的内容与结论写在「对不上的地方」⑬。
**一句话交代结果：五张图没有填掉任何一个 `?`。**
**五张图里没有一处文件内容、没有一条命令名、没有一个 API 名**——
本页 `文件` / `L2` / `L3` 三列那些空着的格子，图一张都解决不了。

它们做的是两件事：

- **把主表第一行的 GUI 格钉到字面**（`Result Mode` 页签、`Result Width` 的 `P/F (1 bit)` /
  `H/L (2 bits)`、`Number of Results/Cycle` 的 `1 (Cycle mode)` … `8 (Edge mode)`）。
  这些串**在 9,398 篇 raw 里 grep 不到**。
- **把「隐藏上传」那一行的机制画出来**（`02.08.04.08.05` 的例子 testflow 节点顺序）。

**它比①②③都硬**（图是文档自带的，不是我的推断），**但它不可检索**——
**拿图里读到的字去 raw 里 grep 是 grep 不到的**；要核只能自己再去开那张图。

## 对不上的地方

**① 本页对照表里 `—` 用了 0 格，这是结论不是偷懒。**
`mapping-pin.md` 的 L3 整列是 `—`，因为 pin 定义是 setup 期动作、外部进程插不进来。
**results 段没有这种结构**：定义（error map / profile / limit）、落盘（EDF / STDF / CSV）、
读回（DRL / IRT）、外部控制（TPI / BLC / HVM）**四件事在语料里都找得到**。
所以主表里每个空着的格子**都是「本页没找到证据」，不是「这一层没有这个东西」**——
按 §2.5 的判据，它们只能写 `?`。
**这是本页与 `mapping-pin.md` 最重要的一处形态差异。**

**② `02.08.04.08.01.02` 有一处语料错字，本页照实记下、没替它改。**
正文那一句逐字是：

> 「This section describes the three options for controlling the acquisition of of test results with the Error Map Tool.」

**`of of` 是重复词**（应为 `acquisition of test results`）。
本页把它原样留在引文里（**引文不许替语料修字**，§11.2）。
同一篇还说这里是 **`three` options**，而它自己的 `Subtopics` **只列了两条**
（`Follow Current Mode` 与 `Analyzing Data in Cycle Oriented or Failure Oriented Mode`）——
**第三条只出现在兄弟篇里**（`02.08.04.08.02` 逐字列了三条：
`Force Cycle Oriented` / `Force Failure Oriented` / `Follow Current Mode`）。
**本页照记，不替它补齐。**

**③ `02.10.01.02.07` 的函数名与目标页对不上，本页照实记下、没替它改。**
`02.10.01.02.07_Data_logging_profiles_and_sampling.md` 的正文里，这个函数叫
**`setSamplingProfile`（单数）**：

> 「The setSamplingProfile CPI function lets you specify which data logging profiles to use for either case.」

而它链过去的 `02.09.01.08.05.04.19` 里，标题是 `Set the data logging profiles`，
签名逐字是：

```
void SetSamplingProfiles( const char * on_profile, const char * off_profile) ;
```

**`setSamplingProfile` / `SetSamplingProfiles`，语料自己两个名字。**
本页主表 L3 格填的是**目标页那个复数拼法**（因为它是带签名的那个），
**但没有替语料调和**——这一条值得后续单独查一次。

**④ `SetErrorMapMode` 与 GUI 的 Acquisition Mode 看着是同一件事，但语料一条链接都没给。**
`02.09.01.09.28` 明写它让我们在执行前决定 error map 怎么记：

> 「This routine lets you determine the mode in which the results are recorded for the result displays (for example, the Error Map) when executing a test.」

它只有两个取值，其中一个逐字是：

> 「ERROR_MAP_FAILURE_ORIENTED to set the error map to failure oriented mode (only failed cycles are logged in the error map).」

而 GUI 侧的 `Result > Acquisition Mode` 给的是
`Force Cycle Oriented` / `Force Failure Oriented` / `Follow Current Mode` 三选一，
并在 `02.08.04.08.03.01.04` 里被描述成

> 「Set how the error data will be acquired in the Error Map and displayed in the error map tool.」

**两边的词面高度重合（cycle oriented / failure oriented），但 `edges.jsonl` 里
`02.09.01.09.28` 与 `02.08.04.08.01.02` 之间一条链接都没有**——
两条链接都只指向本族内部（`02.09.01.09_TPI_Program_Routines.md` 与
`02.08.04.08.01_Error_Map.md` / `02.08.04.08.02`）。
按本任务「不许靠名字像不像配对」的规矩，**主表这一行的 L3 格是 `?`**，
`SetErrorMapMode` **不进表**。**这一条是本页最值得后续单独查的一格。**

**⑤ `CYRM` 一篇被投放了三次，本页按 §10 当同一篇处理。**
`02.06.02.02.37`、`02.06.09.02.01`、`02.06.11.02.05` 三个路径，
`source_topic` 分别是 `98515.htm` / `98515_2.htm` / `98515_3.htm`——
**去后缀后相同，判据命中**。三份正文逐字相同（本页 diff 过）。
**所以主表 `CYRM` 后面的文档号只写了一个**，不是漏列。

**⑥ 结果命令的文档整族是「重复投放」，数链接时不能直接数。**
`EMAP?` / `DCRM` / `DCGM` / … 同时存在于 `02.06.02.02.*`（字母序命令索引）
与 `02.06.11.02.*`（结果命令章）；`CYRM` 还多一个 `02.06.09.02.01`。
按 §10，**`edges.jsonl` 的入度在这里是被灌过水的**——本页凡引用命令文档，
**只引 `02.06.11.02.*` 那一份**。

**⑦ 主表「acquisition mode」行的 L1 格是 `?`，尽管示例里出现过 `DCGM`。**
`02.06.11.01.02.01.06` 的示例逐字写着

```
# Put Error Map into cycle oriented mode (for
# quicker response of EMAP?) with start position:
DCGM ALL,STRT,NONE
```

**注释里确实有 `cycle oriented mode` 这个词**，但**紧接着的 `DCGM` 参数是
`ALL,STRT,NONE`，里面没有 cycle / failure 的取向**。这一句注释**不足以证明
`DCGM` 就是 Acquisition Mode 的固件入口**，本页**不据此填格**。

**⑧ TMLimits 行的 L1 格是 `?`。** 语料把 TMLimits 写在 `02.07.04.01.250`（L2）
与 `02.10.01.08.*`（文件），**没有任何一篇把「测试编号 + limit」与某条固件命令连起来**。
**本页不猜哪条命令是它的 L1。**

**⑨ 「配置 detailed error map」行的「文件」格是 `?`，不是 `—`。**
语料明说这一项的**存法是「建一个 test method」**，
**它讲的是「存储载体」，不是「这一层没有文件」**——
而一个 test method 本身就是文件。**两句话不是一回事，所以按 `?` 记。**

**⑩ `02.08.04.08.01` 与 `02.06.11.01.02.01` 对 overview error map 的压缩粒度写法不同。**
前者逐字：

> 「The overview error map combines every 2000 or more cycles into one result depending on the number of cycles of the test setup.」

后者写的是「multiples of 16 cycles」。
**`wiki/stages/results.md` 已经调过这一处冲突**（16 是步长、2000 是长测试下的实际落点），
本页**照抄那个调和，并标明它是（推断）而不是文档事实**——原文没有一句话把这两个数连起来。

**⑪ 本页搬不动的那一条：`TestsuiteProxy.isPass()`。**
`wiki/stages/results.md` 的 L3 一节把 `TestsuiteProxy` 的 `isPass()` / `isExecuted()`
列为「外部程序可查某 site 的 pass/fail 与是否执行过」。
**本页没有为它单开一行**，因为**本页没有读 `02.09.01.14.02.01`**——
**照抄另一页的结论进对照表，就是在制造第二手证据**（§10）。那一条请回到 stage 页看。

**⑫ 本页的「链接条数」是按文档算的，不是按语料页算的。**
上表那 478 条里，**每一条都是一个物理文档里的一处 `](<...>)`**，
所以**同一篇被投放三次的文档，会把同一处链接记三次**（§10 的「入度灌水」）。
**本页没有做去重**——去重后的数在 `extract/stage-report.md` 第十类，
**本页不另算一遍**。用这张表时按「有多少篇文档提到了它」读，不要按「语料说了多少次」读。

**⑬ 图能读，本页读了五张——原先写的「图在语料树之外」是错的。**（**2026-09-20 更正**）
`../../../../raw/x.png` 往上四层正好是 `tdc-html/`，**图就在 `tdc-html/raw/` 里，读得出来**
（`schema.md` §11.4）。本页 2026-09-20 读了五张，逐张如下。
**凡本页说「grep 不到」的，都是在 9,398 篇 raw md 里逐条查过的**（0 命中）。

**（a）`128339.png` 与 `128334.png`（`02.08.04.08.04` / `02.08.04.08.04.01`，Result Configuration）**

- `128339.png` **只裁到标题栏与页签**：窗口叫 `Result Configuration`，三个页签是
  `Result Mode` / `Execution Mode` / `Advanced`。**图里没有别的东西**——
  本页原先把它写成「GUI 页里图片很多」的一个例子，实际它只贡献了三个页签名。
- `128334.png` 是整块 `Result Mode` 面板，逐字有：`Port` 列表（值 `@`）、
  `Result Width`（单选 `P/F (1 bit)` / `H/L (2 bits)`，选中后者）、
  `Number of Results/Cycle`（单选 `1 (Cycle mode)` / `2` / `4` / `6` / `8 (Edge mode)`，选中第一项）、
  `Edge to Result Mapping`（按钮，灰）、`Result Storage Location`（`Results in` 下拉，
  值 `Test Processor Memory`；`Exception List` 按钮，灰）。
- **它对主表的作用**：**印证第一行的 GUI 格**（`Result Mode` tab），
  并把 ① 档那张「GUI 设置 ↔ 成员函数」对应表的 **GUI 侧字面**摆出来。
  `P/F (1 bit)`、`H/L (2 bits)`、`(Cycle mode)`、`(Edge mode)`、`Test Processor Memory`
  这五个串**在 raw 里 0 命中**——**这一段只在图上**。
- **它答不了的**：第一行空着的两格（`文件`、L3）**图里都没有**。
  图里那句话 `Results in: Test Processor Memory` 说的是**运行时结果放在哪块内存**，
  **不是一个文件名**——按 ⑨ 的分辨方式，这**不构成「文件」格的证据**。

**（b）`128336.png`（`02.08.04.08.04.01`，Result Storage 窗口）**
标题 `Pins` / `Exception Pins`，两组框的逐字说明是
`with Results in Extended Memory` 与 `with Results in Test Processor Internal Memory`，
四个按钮 `Add >` / `Add All >>` / `< Remove` / `<< Remove All`。
**它是 L2 格 `setResultStorageLocationExceptionPinList()` 的 GUI 面**——
但要看清：**它给的是一张 pin 名单，不是文件位置**，所以**第一行的 `文件` 格照旧是 `?`**。
`Test Processor Internal Memory` 在 raw 里 **0 命中**。

**（c）`120006.png`（`02.08.04.08.05_Hidden_Error_Map_Upload`）—— 这一张真的答了一件事**
该篇正文逐字是：

> 「The figure below shows a test flow example that illustrates how the upload of the error map can be hidden behind a digital test.」

图里是一个 testflow（文件页签逐字 `hidden_demo.emap`），**节点顺序**逐字是：
`Start` → `AllocResAreas` → `Emap_100k` → `Emap_200k` → `Emap_300k` → `digital_test_st` →
`Upload_100k` → `Upload_200k` → `Upload_300k` → `digital_test_en`；
五个标注框逐字是 `Allocate Result Areas`、`Capture Error Map Data`、
`Start a digital test`、`Upload Emap Data`、`Wait until digital test is finished`。

**「藏」的机制就是这个顺序**：上传节点排在 `digital_test_st` **之后**、`digital_test_en`
**之前**，也就是说 **emap 上传是与那次 digital test 并发跑的**，流程到最后才等它结束。
**这一句是主表那一行的「目的」栏的展开**——正文只说「藏在背后」，**图说清了怎么藏**。

节点名、标注框里的字（`AllocResAreas` / `digital_test_st` / `hidden_demo` /
`Hide Emap uploads behind this test` / `Allocate Result Areas` / `Upload Emap Data`）
**在 raw 里全部 0 命中**。**唯一一处例外要照实说**：`Wait until digital test is finished`
在**另外三篇与本段无关的文档**里出现过（`02.07.03.13.10` 与它的两份副本），
**那三篇讲的是 label per site，不是 error map**——**同名不同物，本页不合并**。

**它仍然不填那一行的 `文件` / L2 / L3 三格**：图里没有一行文件内容、没有一个 API 名。

**（d）`136441.png`（`02.08.04.13.03.03.01_Raw_data_views`）**
Raw Data view 的窗口加五个标注（`Annotation ruler` / `Column title` / `Table filter` /
`Toolbar` / `Overview ruler` / `Annotation icon` / `Annotation indicator`），
表头逐字是 `Test | Test# | Wafer | Site | Pin | Device | Value | Unit | P/F | Time`。
**它印证「统计评估与下钻到单条记录」那一行的 GUI 格**（[[raw-data-views]]），
并把 L2 格里的 [[testset-testname]] 与表里那个 `Test` 列**对上了名字**——
**但同名不是一条声明**（§2.5「看起来像不算证据」），**本页不据此改任何一格**。

**图证整体答不了的三件事，照实说：**

- **五张图没有一张画出文件内容。** 所以本页 `文件` 列的 `?`（`?` 占 27 格里的 6 格）
  **一张都没解决**——这不是「图够不着」，是**本页 sources 里的图本来就没画文件**。
- **图是「某一次具体配置 / 某一次具体 testflow」的截图，不是格式规范。**
  「哪些设置必填、哪些组合非法」**图答不了**；那是文本的事，而文本在这一点上也没写全。
- **图回答的是「这个窗口长什么样」，不是「这个选项在固件层对应什么」。**
  所以 L1 列**一格都没能从图里取到**。

## 出处

`sources:` **二十四篇**，按层分四组（见 frontmatter）。**读过的方式不一样，要说清**：

- **整篇读完的 18 篇**：`02.08.04.08.01`、`02.08.04.08.01.02`、`02.08.04.08.04`、
  `02.08.04.08.04.01`、`02.08.04.08.05`、`02.08.04.13.03.02.01`、`02.08.04.13.03.03.01`、
  `02.08.04.25.03.02.02`、`02.08.04.25.03.07`、`02.08.04.26.02.02`、
  `02.06.11.01.02.01.06`、`02.09.01.08.05.04.19`、`02.09.01.09.28`、
  `02.09.01.16.02`、`02.09.01.16.04`、`02.10.01.02.07`、`02.10.01.02.08`、
  `02.10.01.08.01.01.01`。
- **只读了片段的 6 篇**：`02.08.04.08.02`（前 26 行）、`02.08.04.08.03.01.04`（菜单那几行）、
  `02.09.01.09.02_DataManager`（第 80–150 行的文件标识表）、
  `02.06.11.02.05` / `02.06.09.02.01` / `02.06.02.02.37`（只读 frontmatter，并做了一次 diff）。
- **引文只来自整篇读过的那一批**；每一句引文**都回 raw 校验过逐字**
  （校验办法：把候选句与 raw 同时做 §11.1 那六条规范化，再查子串）。

**本页没做的**：

- **`02.06.11.02.*` 的结果命令页一篇没读。** 主表 L1 列那些命令名与文档号，
  来自 `wiki/stages/results.md` 的「涉及对象 / L1」两节（那页建页时读的），
  **本页没有回到命令原文复核**。唯一回原文的是 `01.02.01.06`（示例页）与 `CYRM` 三份。
- **`02.07` 的 L2 页一篇没读。** 主表 L2 列里 `RESULT_CONFIGURATION` 的成员函数名
  是从 `02.08.04.08.04` 的对应表里取的；`SHMOO_RESULT`、`Data Display API`、
  `TESTSET::judgeAndLog`、`TMLimits`、四个 profile 类页**全部只见到链接**——
  **它们的参数、返回值、用法，本页一个字没有**。
- **`02.09.01.09.02_DataManager` 只读了文件标识那一段。** 所以 `dm_emap` 一族
  **本页只能给出「标识名 ↔ 一句话描述」**，`dm_load` / `dm_save` / `dm_merge` /
  `dm_copy_in` / `dm_delete` 的签名与语义**一个字没有**。
- **`02.09.01.14.02.01`（TestsuiteProxy）没读**，见「对不上的地方」⑪。
- **一条 L3 都没试过。** 没有跑过 `SetSamplingProfiles`、没有跑过 `MoveEDLStream`、
  没有在机台上开过任何一个结果工具。
- **图够得着，本页读了五张。** 本页原先在这里写着图片路径 `../../../../raw/`「在语料树之外」
  ——**那是错的**：往上四层正好是 `tdc-html/`，**图就在 `tdc-html/raw/` 里，读得出来**
  （`schema.md` §11.4）。2026-09-20 读了 `128339.png`、`128334.png`、`128336.png`
  （`02.08.04.08.04*`）、`120006.png`（`02.08.04.08.05`）、`136441.png`（`02.08.04.13.03.03.01`），
  逐张结论在「对不上的地方」⑬。**其中 `120006.png` 真的答了一件事**（隐藏在 digital test 背后的
  那个例子 testflow 的节点顺序）。
  **仍然答不了的是「GUI 的哪一列对应文件的哪一行」**——但理由换了：
  **不是图够不着，是这五张图里根本没有文件内容**（本页 sources 里没有一张图画出
  `.prf`、TMLimits CSV、`.formatterrc.def` 或 EDF）。
  `02.08.04.25.03.07`（shmoo 存 PNG / ASCII）那篇**一张图都没有**，
  本页原先把它列为「说明也依赖图」，**这一句也是错的**——它没有图可依赖。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/results.md`。
  后者是**待办**：results 那页目前不知道本页存在。

**本页 `layer: n/a` 的理由**：§6 要求 mapping 页必填 `layer`，而本页**本身不属于任何一层接口**
（它是对照表，不是接口）——`n/a` 是这个六值枚举里为这种情况准备的值。

**这一页值不值得单独建**：**值得，但它是「拼出来的」不是「读出来的」。**
理由：`wiki/stages/results.md` 已经把五层的内容分别写全了，
但它**没有在同一行里并排过**——读者想知道「IRT 的 Test 列到底由谁给」，
得在那一页里跨三节找。本页把这 13 行并排之后，**三处原本看不出来的东西显出来了**：
(a) L3 在 results 段是**真有的**（与 pin 段相反）；
(b) 采样那件事是**语料里唯一一处「同一目的、两条不同层的路」**（固定采样走 flag + CPI，
自适应走 L2 API）；
(c) `—` 在 results 段**一格都用不上**。
**代价是 L1 / L2 列的多数名字只有链接级证据**，`?` 占了 27/65——
这个比例说明**这一段的跨层对应，语料本来就只写了一半**。

`verified: doc-only`
