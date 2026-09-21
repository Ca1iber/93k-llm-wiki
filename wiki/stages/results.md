---
type: stage
title: Results — 结果数据与判定
tags: [results, edf, datalog, error-map, stdf, binning, tmlimits]
related: ["[[run]]", "[[testflow]]", "[[testmethod]]", "[[timing]]"]
sources:
  # --- 结果命令（L1 依据） ---
  - 02_System_reference/02.06_Command_Reference/02.06.11_Test_Result_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01_Concepts_of_test_result_processing.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.01_Global_result_queries.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02_Using_the_Error_Maps.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01_Configuring_the_Error_Map_recording.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.04_Configuration_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.06_Result_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.02_Reporting_the_results.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.03_Subsidiary_queries.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.04_Creating_a_high_resolution_timing_diagram.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.02_List_of_test_result_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.18_EMAP__-__Error_MAP.md
  # --- GUI 结果工具 ---
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01_Error_Map.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01.01_Detailed_error_map.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01.02_Setting_the_acquisition_mode.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.02_Using_the_Error_Map_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04_Result_Configuration.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.01_Result_Mode.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.06_Print_Error_Map_Data.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13_Integrated_Result_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.01_Principles_of_operation_of_the_Integrated_Result_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03_Integrated_Result_Tool_reference.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26_Signal_Analyzer.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25.03.02_Setting_up_a_shmoo_test_with_the_Shmoo_Tool.md
  # --- Data Logging / EDF ---
  - 02_System_reference/02.10_Data_Logging/02.10_Data_Logging.md
  - 02_System_reference/02.10_Data_Logging/02.10.01_Event_Data_Logging.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.01.01_Introduction.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.01.02_Event_concept.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.01.03_How_event_data_logging_works.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.01.04_Activating_event_data_logging.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.04_Data_Retrieval_Library.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.06_Event_Data_Logging_Format__EDF.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.06.01_EDF_data_organization.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.06.02_EDF_data_types.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.08_Managing_Test_Numbers.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.09_Appendix_A__Data_Logging_Flags.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.11_Appendix_C__File_Locations.md
  # --- Formatter（产物） ---
  - 02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.md
  - 02_System_reference/02.10_Data_Logging/02.10.02.03_Standard_output_of_the_Event_Formatter.md
  - 02_System_reference/02.10_Data_Logging/02.10.02.05_Fine_result_granularity.md
  - 02_System_reference/02.10_Data_Logging/02.10.03_SmarTest_Data_Formatter.md
  - 02_System_reference/02.10_Data_Logging/02.10.03.03_Formatting_V93000_Test_Results_to_STDF.md
  # --- 下游（章首页，用于判定归属） ---
  - 02_System_reference/02.11_Data_Conversion_and_Bridges/02.11_Data_Conversion_and_Bridges.md
  - 02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01_STIL_Reader.md
  - 02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02_ASCII_Interface.md
  - 02_System_reference/02.14_SmartProd/02.14_SmartProd.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16_ACS_TE-Cloud.md
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# Results — 结果数据与判定

> 把 [[run]] 阶段跑出来的原始测量变成**结构化的结果数据**：谁 pass 谁 fail、落在哪个 bin、失败在哪个 cycle、以及这些数据以什么格式落盘、怎样被下游消费。

**边界声明（先读这段）：** 本页只讲**数据侧**——结果的记录、组织、格式与判定。
「怎么把程序跑起来」「怎么在 GUI 里定位一个 bug」「怎么看波形」属于 [[run]]。
Timing Diagram Tool / Error Map Tool 两边都会出现：**本页只把它们当作结果数据的消费者与呈现者**，
不讲调试手法。结果判定的**定义**（limit 怎么声明）属于 [[testmethod]]，本页只讲
**limit 被拿来判定之后产生了什么结果、这些结果存在哪**。

## 目的

文档把这一块分成两条并行的主线，它们是同一个问题的两种表述：

1. **Test result processing（命令侧）** — `02.06.11_Test_Result_Commands` 开篇写明，
   这一章的命令是「**result tools 所使用的命令**」，分成三组：
   - global result commands（全局结果查询）
   - commands for managing the Error Maps（Error Map 管理）
   - subsidiary commands that do not require a previous test execution
     （不需要预先执行测试的辅助查询）

2. **Data logging（数据侧）** — `02.10_Data_Logging` 是数据的**落地与格式化**：
   Event Data Logging（事件数据日志，产生 EDF）、Event Formatter（事件报告生成）、
   SmarTest Data Formatter（把结果格式化成 STDF）。

一句话概括本阶段：**判定发生在测试执行期间（由 Error Map 记录失败周期、由 TMLimits
比对 limit 得到 pass/fail），而结果是事后通过一套查询命令、一份二进制日志、
和若干格式化工具取出来给人和机器用的。**

`02.10.01.01.01_Introduction` 把 event data logging 的定位讲得最清楚，值得抄下它的核心几条
（这些是文档**明写的设计目标**，不是我的评价）：

- 「**fully event based**」，因此 production test data **在测试跑的过程中一生成就立刻可取**。
- 日志流「**easily manageable**」——**不会撑爆系统内存或文件系统**。
- 记录下来的数据**已经是 C 数据类型**，可以**直接做后续处理，不需要再解析输出**。
- **可以完全关掉**（if not needed）。
- 与更早的、产 **GDF 输出**的日志机制**共存**，因此用户自己写的工具**不会因为新机制而作废**。

## 前置条件

来自 `02.06.11.01.03_Subsidiary_queries` 的**明写要求**（辅助查询虽然叫「不需要执行测试」，
但不是无条件可用）：

- 你关心的 label（pattern）**必须先由 `SQSL` 定义为 start label**。
- 你要用的 timing setup **必须已由 `SPRM` 声明为 primary timing**。

即：结果/查询这一层依赖 [[timing]] 与 [[pattern]] 阶段已完成的定义。
注意这里文档特意强调辅助查询用的是 **primary（不是 base）wavetable**（见 `CDCP?` 的说明）。

来自 `02.06.11.01.04_Creating_a_high_resolution_timing_diagram`：

- 使用 `HRIT` / `HREX?` 时，**指定的所有 pin 必须是 O 或 IO 类型**。
- 该功能「always uses edge compare」。

来自 `02.10.01.01.04_Activating_event_data_logging`（**这条最关键：日志默认不是开着的**）：

- **Before you begin：SmarTest software must be running。**
- 两种激活方式，文档明写**方式 1 是最简单也是推荐做法**：
  1. **用 data log profile**（推荐）——需要一个把 **`log_events_enable` 标志置为 `on`**
     的 profile，`datalog_ON.prf` 就是这样一个出厂 profile，加载它即可。
  2. **直接设标志** —— Operation Control 窗口 → `Production Settings` →
     Testflow Settings Mode 窗口 → `System Flags` → 把 `log_events_enable` 设为 `on`。
- **Results（文档原文）**：event data logging is turned on，**all new event data is
  written to the data log stream**。
- **What to do next（文档原文）**：Activating the Event Formatter 或
  Activating the STDF formatter。
  → 也就是说，**打开日志之后紧接着就是开 formatter**，这条文档路径本身就是
  [[run]] → results 的交接点。

来自 `02.08.04.08.02_Using_the_Error_Map_Tool`：

- 用 Error Map Tool 分析前，要先选定 **result mode**（`Result > Acquisition Mode`，
  三选一：Force Cycle Oriented / Force Failure Oriented / Follow Current Mode）
  和 **result granularity 与详细 error map 的位置**（`Result > Result Configuration`），
  然后 `Result > Execute` 才做测试。

**推断**：本阶段的其余部分（EDF、Formatter、STDF）前置是 [[run]] 已经真正执行过一次
测试——没有执行就没有事件、没有 data log stream。文档在 `02.10.01.02` 里用
「during test program execution」描述日志产生的时机，在 `02.10.01.01.01` 里说数据
「immediately accessible **after it was generated during the test run**」。

## 涉及对象

| 对象 | 层级 | 在本阶段干什么 |
|---|---|---|
| [[list-of-test-result-commands]] | L1 | 40 条结果命令的总清单，本页 L1 一节的全部依据 |
| [[error-map]] | file | 记录失败 cycle 的核心结构；分 detailed / overview 两种。**这一格原来写 `L1/file`，`L1` 无据**——[[error-map]] 页全文没有一处 `L1`，计划表里它的层也是 `file` |
| [[edf]] | file | Event Data Logging Format，事件数据日志流，二进制 |
| [[edl-file]] | file | 保存下来的 data log / 系统 event stream，离线分析的输入 |
| [[data-logging-profiles]] | file | `.prf` 文件，控制「记录哪些数据」的规则集合 |
| [[event-formatter]] | gui | 报告生成工具，把 EDF 转成可读报告 |
| [[smartest-data-formatter]] | gui/file | 把 V93000 结果格式化成 STDF |
| [[stdf]] | file | Standard Test Data Format，下游/客户通用的结果交换格式 |
| [[tmlimits]] | L2/file | 测试编号 + limit 的表格，产出的 pass/fail 判定依据 |
| [[data-retrieval-library]] | L2 | DRL，读二进制 data log stream 的 C 函数库（Linux only） |
| [[drldump]] | L1 | 用 DRL 写的样本工具，也是自写工具的模板 |
| [[lot-summary-generator]] | L1 | 从 EDL 文件或实时 event stream 生成 GDF 格式 lot summary |
| [[error-map-tool]] | gui | 分析 Error Map 的 GUI，所有结果分析工具里最底层的一个 |
| [[integrated-result-tool]] | gui | 统计/图形化评估 data log 文件与系统 data log stream（7.2.0 引入） |
| [[timing-diagram-tool]] | gui | 显示发给 DUT 的波形与 DUT 返回；标出收数与 pattern 期望不符的点 |
| [[signal-analyzer]] | gui | 波形查看环境（含 Smith Chart、解调） |
| [[shmoo-tool]] | gui | shmoo 测试的数据采集与呈现 |
| [[report-window]] | gui | 结果的交互式呈现入口；Event Formatter 挂在这里 |

### GUI 结果工具的分工（本页只记「它们消费什么数据」，不记怎么调试）

- **[[error-map-tool]]**（`02.08.04.08`）—— 文档明写它是
  「an application for the evaluation of errors」「the major tool for **low level** examination
  of the test results you obtain when performing functional tests」，且
  **「It uses the Error Map to generate its output」**。入口：`93000 > Results > Error Map`。
  它有两个 Tab：**Overview**（看哪些 cycle block 含错误）与 **Cycles** / **Edges**
  （取决于配置，用来细化）。文档给的典型用法是：Overview 里选中一个 cell → Execute →
  该 cell 被放大、详细 error map 的 8K memory 被后续 cell 的 cycles/failures 填充 →
  若错误不全在详细 error map 范围内，就在 Overview 里再选更靠后的 cycle block 重复。
- **[[integrated-result-tool]]**（`02.08.04.13`，**Introduced in SmarTest 7.2.0**）——
  「supports the **statistical and graphical** evaluation of **saved data log files** and the
  **system data log stream**」。可加载 **STDF 或 EDL** 文件到 Data Log Explorer；
  **系统 data log 总是被自动加载**。有五个 summary tab：Test / Wafer / Device /
  Hardware bin / Software bin（correlation data store 没有 Wafer 与 Device 两个 tab）。
  另有 Raw data view / Stream data view、Analysis views（Trend、Histogram、Probability、
  Box、Scatter、FFC Pareto、Shmoo、Scan、Parametric wafer map）。
  它与 [[testflow]] 工具双向联动：从 summary 可打开测试定义或 limit 定义；
  在 Testflow Tool 里右键一个 test 可直接打开它的结果。
- **[[timing-diagram-tool]]**（`02.08.04.33`）—— 文档定义为
  「the operating principles for the Timing Diagram **result analysis** tool」，
  显示实际发给 DUT 的波形与 DUT 输出的响应，**并标出收到数据与 Pattern Tool 中期望数据
  不符的波形点**。注意约束：它区分 executed pattern 用到的 pin 与没用到的 pin，
  只聚焦用到的；未用到的 drive pin 只显示前两个，且**不能被 format**；其余未用到的
  drive pin 与全部未用到的 receive pin **不显示**，此时 SmarTest 会在
  [[report-window]] 里发警告。
- **[[signal-analyzer]]**（`02.08.04.26`）—— 「a waveform viewing environment」。
- **[[shmoo-tool]]**（`02.08.04.25`）—— shmoo 测试的建立与数据呈现。

## L1 — Firmware / Setup Command

### 全局结果查询（Global result queries）

文档 `02.06.11.01.01` 明写：

- `FTST?` — 执行一次 functional test 并返回**全局 pass/fail**。
- `PASS?` — 需要**配置 pin 的子集**的组合结果时用这个。
- `CHER?` — 返回**每个指定 pin 各自**的结果（比 PASS? 更细）。
- `CHFA?` — 专门给**因为 match loop 失败**而 fail 的测试用，返回所选 pin
  最后一个 match loop cycle 的结果。**注意：这个信息无法从 Error Map 取到**，
  因为 **match loop cycles 不记录在 Error Map 里**。
- `MCNT?` — 另一个 match loop 相关查询，返回**取得 match 的那次 match loop pass 的编号**。

### Error Map 命令（管理 Error Maps）

来自 `02.06.11.01.02_Using_the_Error_Maps`：

- SmarTest 提供**两个** Error Map：**detailed**（细到 cycle 甚至 edge 级）和
  **overview**（把多个 cycle 合成一个结果，只要其中有一个 fail 就是 Failed）。
- overview Error Map 有**两种模式**：(a) 指定「固定多少个 cycle 用一个 bit 表示」；
  (b) 一个 burst 的**每个 main pattern 一个结果**——后者可以用来定位 burst 里哪些 pattern 失败。
- 两个 Error Map 都在 **test processor 内部**；**detailed Error Map 也可以放在 external memory**，
  默认用内部的。
- 命令分两组：**定义「记录什么」** 的命令，和 **定义「报告什么」** 的命令。
  文档强调：「everything that is reported must have been recorded, but the recorded data
  can be filtered and formatted in different ways for the reports.」

**容量约束（`02.06.11.01.02.01_Configuring_the_Error_Map_recording` 明写，这是理解整套
Error Map 机制的关键）**：

- **内部 detailed Error Map 「rather small」——最多只能容纳 8192 cycles 的信息。**
- 因此**通常不可能为整个测试记录详细结果**。要拿到需要的数据，必须适当配置
  **sequencer 的 termination mode** 和 **Error Map 的 recording parameters**。
- **overview Error Map 把多个 cycle 压缩成一个结果**，**压缩因子可由用户选择**，
  这样总能看到完整测试的概览。

> **两处「压缩粒度」写法看似冲突，但可调和（推断）**：
> `02.08.04.08.01_Error_Map` 写 overview map「combines **every 2000 or more cycles** into
> one result depending on the number of cycles of the test setup」；
> 而 `02.06.11.01.02.01` 写它「compresses **multiples of 16 cycles** into one result」。
> `02.06.11.01.02.01.04_Configuration_commands` 给了解释：compression factor
> 「defines **how many blocks of 16 cycles** are compressed into one result」——
> 即 **16 cycles 是压缩的原子单位，块数由用户选**；一个很长的测试（cycle 数远超
> overview map 的位数）自然会让「一个结果」覆盖到 2000 个 cycle 量级。
> 两处因此并不矛盾：**16 是步长，2000 是长测试下的实际落点**。
> 同一节还明写：也可以设成**把 burst 内每个 main label 的 cycle 压成一个结果**。

**报告内容的顺序（`02.06.11.01.02.02_Reporting_the_results` 明写）**：

- 可报告的数据有三类，**列表顺序大致就是取数的顺序**：
  1. 已记录的 cycle 区域（**第一步通常是用 `VALD?` 查实际记录到了哪个区域**——
     `VALD?` 对 detailed 和 overview Error Map 都可用）；
  2. error count；
  3. Error Map 内容。
- 计数类查询是 `ERCC?` / `ERCT?` / `ERCY?`；取内容是 `EMAP?` 与 `ERMP?`，
  **`EMAP?` 是 `ERMP?` 更强的版本**。
- **`PASS?` 的组合语义（文档明写）**：当一个 result 被报告给多个 pin 时，
  **只有该 cycle（若记录了 edge 则是该 edge）对所有那些 pin 都 passed，才返回 PASS**。
- `EARD?` 除了返回请求 cycle range 内所有已用 edge 的 drive 与 received compare data，
  **还能返回映射到同一个 HXA pin 的所有 Pin Scale pin 的组合结果**。
- `CYCI?` 返回测试进程的综合信息；`FFCI?` 返回**前 n 个 failing cycle 的 pin 特定信息**。

**`EMAP?` 的最小可用语法（从 `02.06.11.02.18` 抄录）**：

```
EMAP? {pin_res},{start_cycle},{no_of_cycles},{resolution_mode},[results_per_cycle],[bits],{rep_mode},{results_align},[byte_max], [MUX,] {(pinlist)}
```

- `pin_res` 取 `PPIN`（pin list 里**每个 pin 各自**的结果）或 `COMB`（**所有 pin 只有一个全局结果**）。
- `resolution_mode` 三选一：
  - `CYCL` — **每个 cycle 一个结果**；
  - `SCYC` — **按 `DCRM` 定义的结果组合（sub-cycle）原样报告**；
  - `EDGE` — **每个 cycle 返回全部 8 个 edge**（不只是记录了的），
    **未记录的 edge 按 passed 返回**，这样可以从「失败 edge 在返回串里的位置」反推它的 edge 编号。
    文档给的例子：若记录了 edge 2 和 7（且只请求 1 bit 结果），
    则一个两条 edge 都失败的 cycle 会返回 `0100 0010`。
- `bits` 取 `PF`（**只返回 1 bit 的 pass/fail**）或 `PFC`（**失败时返回更详细的 2 bit 码**）。
  文档明写：**2 bit 码只有在记录时就用了 2 bit 码（`DCRM` 的 `bits` 参数设为 `PFC`）才能报告**。
  收到数据可由 expected data 与 error code 重建；`I` = Intermediate，`U` = Unstable。
- **`EMAP?` 是 site 相关的：一次只能有一个 site 在 focus**。对 focus 中的 site，
  SmarTest 在 Testflow Editor 和结果工具里显示其结果；**任何 firmware 查询都只报告
  当前 focus 的那个 site 的 setup 与结果**。
- 文档明写 **`EMAP?` 只能报告真正记录了的东西**，记录选项由 **`DCRM`** 定义。

**`EDGE` 模式的两个前置条件组合（文档明写，二选一）**：

1. `DCRM` 的 `mode` 参数 > 1；且 `DCRM` 的 `sub_cycles` 参数指定的**任何结果组合都不含
   多于 1 个 edge**（这要求结果组合必须用 `DCRM` 指定）；且 `sub_cycles` 串里的
   **edge 必须按升序排列**。
2. `DCRM` 设为 `1,PFC`；`CYRM` 设为 `EDGE`；`CYRP` 设为 `MULT`（默认值）。

清单中属于这两组的命令（据 `02.06.11.02` 的子页标题）：

记录侧：`DCEL`（Digital Compare Exception List）、`DCGM`（Digital Compare Global Mode）、
`DCRM`（Digital Compare Result Mode）、`DCRP`（Digital Compare Result Positioning）、
`DCRS?`（Digital Compare Result Size）、`DCRT`（Digital Compare Result Target）、
`CYRM`（Cycle Resolution Mode）、`CYRP?` / `CYRS?`（Cycle Resolution Parameter / State）。
报告侧：`EMAP?`（Error MAP）、`ERMP?`（ERror MaP）、`ERCT?`（ERror CounT）、
`ERCY?`（ERror CYcle）、`ERCC?`（ERror in Cycle range Count）、
`FFCI?`（First Failed Cycle Information）、`FFPM?`（First Failing cycle information Pin Mapping）、
`EDGE?`（EDGE errors）。

> 推断：把命令划入「记录侧 / 报告侧」是我根据其名称与 `02.06.11.01.02` 对两组命令的
> 描述做的归类，文档 `02.06.11.02` 本身只是**平铺列出**，未逐条标注属于哪一组。
> 但 `DCRM` 属记录侧、`EMAP?`/`ERMP?`/`VALD?` 属报告侧，是文档正文**直接证实**的
> （`02.06.11.01.02.01.06_Result_commands` 与 `02.06.11.01.02.02`）。

**两条配置路线的取舍（`02.06.11.01.02.01.04` 明写）**：

- 配置 recording parameters 有**两条互相竞争的路线**：用 **`SQGB`**，或用
  **`DCGM` / `DCRM` / `DCRP` / `DCRT`** 这一组。
- **`SQGB` 把「控制 sequencer termination」与「配置 Error Map」两个功能合在一起，
  它只应该用来控制 sequencer termination**；作为配置 Error Map 的手段，
  **仅为兼容性保留，新应用应避免使用**。
- **`DCxx` 一组灵活得多**，而且 **Pin Scale / Smart Scale 数字卡的特殊功能
  （Error Map 位置、error code 分辨率）只能用它们才能启用**。
- 参数到命令的对应（文档原表）：

  | 参数 | 命令 | 备注 |
  |---|---|---|
  | Resolution of error code | `DCRM` | 与 result granularity 的依赖见 `Possible_combinations_of_CYRM__CYRP__and_DCRM` |
  | Location of detailed Error Map | `DCRT` | 用 `DCRS?` 查询 Error Map 大小 |
  | Recording mode for detailed Error Map | `DCGM` | 可自己选，也可交给 SmarTest 选 |
  | Recording position | `DCGM`, `DCRP` | **`DCRP` 指定记录位置，`DCGM` 定义怎么解释它** |
  | Result granularity | `DCRM` | 同上 |
  | Compression factor of the overview Error Map | `DCRM` | 多少个 16-cycle 块压成一个结果；也可设成按 burst 内 main label 压缩 |

**最小可用示例（`02.06.11.01.02.01.06_Result_commands` 原文抄录，这是本页最实的一段 L1）**：

```
# Put Error Map into cycle oriented mode (for
# quicker response of EMAP?) with start position:
DCGM ALL,STRT,NONE
# Start recording at first cycle:
DCRP EMAP,0,(@)
# Record 1 bit results on edge level:
DCRM EMAP,8,PF,(@)
# Put detailed Error Map into external memory:
DCRT RAM,(@)
# Execute functional test
FTST?
# Report on edge level. All 15000 cycles are returned
# in one reply (ERMP? can only return 2048 cycles):
EMAP? PPIN,0,15000,EDGE,8,PF,ALL,BYTE,,(@)
```

这段示例同时说明了几件事：`(@)` 指全部 pin；**`FTST?` 就是那个「执行 functional test」
的动作**；以及 **`ERMP?` 一次最多只能返回 2048 cycles，而 `EMAP?` 没有这个限制**
（示例一次取回 15000 cycles）。

### 辅助查询（Subsidiary queries）

`02.06.11.01.03` 明确把辅助查询分成两组：

第一组，返回**某 cycle range 的 setup 数据**：

- `CDCP?` — 用 **primary（不是 base）wavetable** 把物理波形 DC/DC power unit
  翻译成 device cycle 名和 data parameter。
- `EAEX?` — 返回请求 cycle range 内的 drive 与 expected edge action 数据。
- `GETV?` — 返回某个 cycle range 是由哪个 vector setup 生成的。
- `GETS?` — 返回某个 cycle range 用到的 timing 和 level set。

第二组，返回 **cycle 信息**：

- `GETC?` — 给一个 vector，返回 cycle number。
- `VCYC?` — 返回请求 cycle range 的物理波形 DC/DC power unit。
- `VRCS?` — 返回当前 start label 产生的 cycle 数。

`GETX?` **同属两组**：既能取某 vector 的 cycle number，也能取某 cycle 的 setup 信息。

清单里的其余结果查询（同属本层，按 `02.06.11.02` 子页标题）：

- 接收/期望数据对比：`EARD?`（Edge Action Result Data）、`EARE?`（Edge Action REceived data）、
  `EAEX?`（Edge Action EXpected data）、`WFEX?`（WaveForm EXpected data）、
  `WFRE?`（WaveForm REceived data）。
- 有效性判定：`VALD?`（VALid Data）、`VALR?`（VALid Range）、`VCYC?`、`VNEC?`
  （Valid Number of Executed Cycles）、`VRCS?`（Valid ReConStruction）。
- sequencer：`SQGB`（SeQuencer GloBal）、`SQIB`（SeQuencer Interrupt Behavior）。
- `CYCI?`（get CYCle Information）。

### 高分辨率时序图（HRIT / HREX?）

`02.06.11.01.04` 明写，用 `HRIT` 提供五个信息来创建：

- Start cycle number / Start cycle offset / End cycle number / End cycle offset /
  Total number of samples。

机制（文档原文）：**总是用 edge compare**，把 edge 移到参数定义的位置，做一次 functional test
并把采样值存下来；然后按 samples-per-cycle 参数定义的 resolution 增加 edge delay，逐步采样。
若 period 在测量过程中变化，**samples per cycle 保持不变**。
该参数**始终参照 Standard mode pins**。

**重要副作用（文档明写）**：执行 high resolution timing 测量**会删除指定 pin 的 Error Map 内容**。
如果通过 GUI 激活测量，测量完成后会**自动做一次 functional test 来恢复 Error Map 内容**；
**用 firmware 命令则不会**。
数据用 `HREX?` 取回，**返回 packed binary format**。

## L2 — Test Method API

- [[tmlimits]]（`02.07.04.01.250`）— limit 的**判定**接口。本页与 [[testmethod]] 的分工如下：
  - **limit 的定义**（怎么写、放哪、test table 怎么建）归 [[testmethod]]。
  - **limit 被用于判定后产生的结果**（pass/fail、bin）留在本页。
  - TMLimits 的 CSV 结构与 bin 列（`Bin_s_num` / `Bin_h_num` / `Bin_type` /
    `Bin_reprobe` / `Bin_overon`）见「产物」一节。
- [[result-configuration]]（`02.08.04.08.04` 明写）— 要把 Result Configuration 界面的
  设置**存下来，必须从 `RESULT_CONFIGURATION` test method API 建一个 test method**。
  文档给了界面设置与成员函数的完整对应表（这是本阶段最实的一张 L2 表）：

  | 界面 Tab | 分组 | 成员函数 |
  |---|---|---|
  | Result Mode | Result Width | `setResultWidth()` |
  | Result Mode | Number of Results/Cycle | `setNumberOfResultsPerCycle()` |
  | Result Mode | Edge to Result Mapping | `setEdgeToResultMapping()` |
  | Result Mode | Result Storage Location | `setResultStorageLocation()` |
  | Result Mode | Exception List | `setResultStorageLocationExceptionPinList()` |
  | Execution Mode | Multiple Executions | `setMultipleExecutions()` |
  | Execution Mode | Result Granularity | `setResultGranularity()` |
  | Execution Mode | Exception list | `setResultGranularityExceptionPinList()` |
  | Advanced | Behavior when Result Storage was Incomplete | `setResultStorageIncompleteBehavior()` |

  文档明写这些参数**都定义在 port 级**，默认是 **1 result per cycle、2 bit error code**；
  **error code resolution 与 result granularity 不独立**，系统会检查配置一致性，
  不一致就标红该 port 并禁用 OK 按钮；允许的组合清单见
  `02.06.11.01.02.01.02.05_Possible_combinations_of_CYRM__CYRP__and_DCRM`。
  Result Width 的取值语义是 **H / I / L = High / Intermediate / Low**。
- [[testset-testname]]（`02.07.04.01.244.23`）— Test summary tab 的 `Test` 列明写
  由它给出（以 `Test Suite` / `Test Method` / `Test#` 为兄弟列）。
- [[data-logging-profile-api]]（`02.10.01.02.08`）— 数据日志 profile 的编程接口。
  `02.10.01.02` 明写：可以**在 test method 内部监测 yield 下降**，失败数超过阈值时
  用「a simple function call from within a test method」现场激活 debug profile。
- [[data-retrieval-library]]（DRL，`02.10.01.04`）— 读 data log stream 的 C 函数库。
  文档明写三点：**runs only on Linux**；提供一组 **DRL functions**（读 event record、
  从中抽取数据、存进 DRL 数据类型）与一组 **DRL data types**（承载各种 attribute 的数据）；
  「Using the DRL **frees you from the need to write parsers for data log files**」。
  它还能把**整个 data log stream 存成文件**，之后再以同样方式访问该文件做离线分析。
  **Event Formatter 与 Line Formatter 都建在 DRL 之上。**

> **L2 汇总的一句话**：本阶段的 L2 是「配置记录什么（`RESULT_CONFIGURATION` +
> data logging profile API）」和「读回记录了什么（DRL）」两端，中间没有任何东西——
> 判定逻辑本身在 [[testmethod]] 侧的 TMLimits 里。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 文档事实：`TestsuiteProxy`
（`02.09.01.14.02.01`）的 33 个编号成员里，session / execute / `isPass` / `isExecuted` /
name / siteMatch 那几个是**横切面**，其余**天然按阶段分组**——这不是巧合，是文档自己的组织方式。
横切入口见 [[test-suite-control-api]]；产物文件接口见 [[tpi-program-routines]]（**同层、同样由外部客户端进程调用**，见该页「出处」）。

**本阶段有专属 L3，而且直接对口。** 文档事实：

### 1. 结果数据的实时读取 —— Data Retrieval Library

`02.09.01.16.02_How_to_capture_the_test_result_in_real_time`（章：`02.09.01.16`
Critical tasks in production environment）明写事件数据日志（EDL）就是为**从生产环境取出测试结果**
而提供的，并给出用 data retrieval library 实时抓取结果的流程；`02.09.01.16.04`
是用 **BLC API 控制 event data logging**。同章下还有
`02.09.01.16.02.05_Example_of_yield_monitor`、
`02.09.01.16.02.06_Example_of_analyzing_the_Iddq_measurement_results` —— 这两个例子
**就是本阶段在做的事**（良率监控、Iddq 结果分析），只是从外部程序侧做。

### 2. Error Map 的记录粒度由外部程序决定

`02.09.01.09.28_SetErrorMapMode`：

```
VOID SetErrorMapMode(INT32 mode);
```

> This routine lets you determine the mode in which the results are recorded for the result
> displays (for example, the Error Map) when executing a test.

- `ERROR_MAP_FAILURE_ORIENTED` — only failed cycles are logged
- `ERROR_MAP_CYCLE_ORIENTED` — all cycles are logged

即 **Error Map 是记 failed cycles 还是全部 cycles，可以在执行前由外部程序设定**。

### 3. 判定与执行状态的查询

`TestsuiteProxy.isPass()`（`.23`）与 `isExecuted()`（`.21`）——外部程序可查某 site 的
pass/fail 与是否执行过。

### 4. 事件流

HVM API 的 `GetLastEvent`（`02.09.01.10.03.02.02.25`）与 EDL 事件（如 die 完成事件）
构成结果数据的推送面。

### 5. 产物文件

`DataManager`（`02.09.01.09.02`）中与结果相关的文件标识：`dm_emap`（error map）、
`dm_fam`（fail map）、`dm_report`、`dm_scan_res`、`dm_dataform`，配 `dm_load` / `dm_save` /
`dm_merge` / `dm_copy_in` / `dm_delete`。

> **改判记录。** 本页上一版 L3 写「文档未覆盖」，理由是「`02.09_Test_Program_Management`
> 下的 HVM API / Test suite control API **文档未把它们与结果数据的读取关联起来**」。
> **那一句是错的**——`02.09.01.16.02` 的标题就是 "How to capture the test result in real
> time"，就在同一章 `02.09.01` 里。上一版没翻到 `02.09.01.16` 这一节就下了结论。已改。

### SmartShell 仍然不可用

`02.15_SmartShell` 的 Functional changes 明写 `Introduced in SmarTest 8.2.5`，
本 wiki 面向 7.10.3，该章仅 1 篇且正文全是 PDF 外链。**不拿它当可用的 L3 结果接口。**

## 产物

### 1. Data log stream / EDF（事件数据日志）

- **格式**：二进制。`02.10.01.06.01` 明写「for performance reasons, the data log
  information is written to the data log stream in a **binary format**」。
- **结构**（文档明写，这是本阶段最实质的对象）：
  - 每当一次 event 发生，就往 stream 里写一条 **event record**；整个 data log stream
    就是一系列 event record。
  - 每个 event record 分 **header + body**。header 两个元素：
    - `Record Length` — 4 字节，存的是 **event record body 的长度**，用来找下一条 event record 的起点；
    - `Event Type` — 2 字节，存 event 的符号名，定义在头文件 **`dcl_drl.h`** 里。
  - body 是**一串 attribute record**；attribute record 的数量与类型**取决于 event 的类型**。
  - 每个 attribute record 同样分 **header + body**。header 两个元素：
    - `Record Length` — 4 字节，存 **attribute record body 的长度**，用来找 body 内下一条 attribute record；
    - `Attribute Type` — 2 字节，存 attribute 的类型，例如 `DeviceAttrType`。
- **字节序**：**little-endian**（最低有效字节在前，即原生 Intel x86 顺序）。
  Functional changes 明写 **SmarTest 7.2.0 改为 little-endian**——
  即 7.10.3 上按 little-endian 读是对的。
- **类型系统**（`02.10.01.06.02`，全部 little-endian）：
  | 类型 | 含义 |
  |---|---|
  | `char` | 一字节有符号整数 |
  | `short` | 两字节有符号整数 |
  | `int` | 四字节有符号整数 |
  | `long long` | 八字节有符号整数 |
  | `unsigned char` | 一字节无符号整数 |
  | `unsigned short` | 两字节无符号整数 |
  | `unsigned int` | 四字节无符号整数 |
  | `real` | 八字节浮点，**IEEE 754 格式** |
  | `string` | null-terminated string |
- **类型定义位置**：`/opt/hp93000/soc/com/include/dcl_drl.h`
  （可用的 event type 与 attribute type 都在这里）。
- **组织维度**（`02.10.01.06` 的子页给出）：Event types（`02.10.01.06.03`，含
  `TestEventType`、`TestFunctionStart/End`、`TestSuiteStart/End`、`TestFlowStart/End`、
  `TestProgramStart/End`、`BinReachedEventType`、`IntermediateResultEventType`、
  `AppModelLevelStart/Loop/End`、`UserProcedure`、`ActionEventType`、
  `PrintToDatalogEventType`、`GenericDataEventType`、`ConfigurationChangedEventType`、
  `ManualExecutionEventType` 等约 22 种），以及 Attribute types（`02.10.01.06.05`，
  约 70 余种，含 `TestIdAttrType`、`TestNameAttrType`、`ValueResultAttrType`、
  `PassFailResultAttrType`、`BinAttrType`、`ErrorMapAttrType`、`ErrorOverviewAttrType`、
  `FailingCycleAttrType`、`SiteIdAttrType`、`TestSuiteNameAttrType`、
  `TestFunctionParametersAttrType`、`Shmoo*AttrType` 一族等）。
- **自建事件**：`02.10.01.06.04_Creating_your_own_custom_events_with_the_DCL_library`。

### 2. Data logging profile（`.prf`）

`02.10.01.02` 明写：

- 一个 profile 是**一组数据日志规则**，决定「系统内哪些数据被记录、怎么记录」。
- 出厂自带两个：**`datalog_OFF.prf`**（不记录任何数据，不写日志文件）和
  **`datalog_ON.prf`**（**per pin** 记录，**所有测试的 value result**）。
- 目录：**`<device directory>/profiles/`**（生产设置文件拷到这里即可当只读 profile 用）。
- 用途：为 production 中**优化过的 testflow 改 flag 设置而不破坏优化**；
  文档给的例子是「标准 profile 只记录所有测试的 pass/fail；debug profile 记录
  pin value result、first failing cycle 等细节」，yield 掉了就一键切 debug profile。
- 相关子页：Flags and data logging profiles、Loading/Unloading、Associating a profile
  with a testflow、Restoring defaults、**Profile Editor**、Data logging profiles and
  **sampling**（fixed 与 adaptive 两种效率模式）、Data logging profile API。

### 3. STDF（SmarTest Data Formatter）

`02.10.03` 明写这是把 V93000 测试结果**格式化成 STDF** 的工具。子页给出：
Standard Test Data Format (STDF) Overview、Starting and Stopping the Formatter、
Formatting V93000 Test Results to STDF、STDF Configuration、
Appendix A: STDF Record Types、Appendix B: The STDF Reader、Appendix C: Example Application Model。

`02.10.03.03_Formatting_V93000_Test_Results_to_STDF` 进一步列出 STDF 落地时必须处理的
**具体数据问题**（这些就是「判定结果怎么映射到 STDF」的清单）：
General data content options、Parametric or functional test types、
**Multiple pass/fail results from a single test**、**Pin results**、**Overon flag**、
**Test numbers**、**Reprobe data**、**The PART_ID field in the PRR**、Test methods、
Using MAP_SITE to specify alternate site numbers。

`02.10.01.11` 给出可执行文件位置：**`/opt/hp93000/soc/formatter/bin/STDFreader`**。

### 4. EDL 文件（保存下来的 data log）

- Integrated Result Tool 的 `Save and Clear` 命令/按钮明写可以
  「save the current system event stream as an **EDL file**」。
- `02.10.01.07_LotSummaryGenerator` 明写它接受「an offline data collection file
  (**EDL file**)」作为命令行输入。
  → **推断**：EDF 是这套事件日志的**格式名**，EDL 是它的**文件扩展名**
  （离线 data collection file）。文档没有一句话直接说明这个对应关系，
  是从两处上下文（`02.10.01.06.01` 讲 EDF 格式、Integrated Result Tool 与 LotSummaryGenerator
  都读 EDL 文件）拼出来的。

### 5. LotSummaryGenerator（`02.10.01.07`）

- 位置：**`/opt/hp93000/soc/formatter/bin`**。
- 作用：生成 **GDF 格式**的 test summary。
- 两种输入方式（文档明写）：
  - **离线**：命令行给一个 **EDL 文件**，它从文件里取数据，为文件中记录的**所有
    test program 与 testflow 执行**生成 lot summary。
  - **实时**：不给文件时，它会尝试**附着到当前 SmarTest session** 实时生成 lot summary；
    若没有 SmarTest 在跑，会打印错误信息。

### 6. Print Error Map Data 的输出（`02.08.04.08.06`）

- 位置：**文件保存到 `/device/report` 目录**（文档明写）。
- 输出列：前三列固定为 `Error number | Cycle number | Pinname`，
  后两列 `Expected data` / `Received data` 由窗口设置决定。
- **数据字符的含义（文档明写，这是判定结果的一个细节口径）**：
  `0` 数据为 0；`1` 数据为 1；`I` 数据是 **intermediate**；`U` 数据 **unstable**；
  `N` 数据**未重建**，因为一个 cycle 里有多个 compare edge（**x-mode 下测试时出现**）。

### 7. TMLimits CSV（测试编号 + limit 表）

`02.10.01.08.01.01.03.01` 明写：标准 CSV，**逗号分隔字段、换行分隔记录**，
结构是**两行 header + 每个 test 一行**：

- 第一行 = 列名；第二行 = **每列对应的 test mode**（第二行为空则该列值对所有 test mode 生效；
  第二行填了 test mode 则只在选中的 mode 下用）。GUI 里加 test mode 行的办法：
  在最上面插一空行，第一个单元格填 `Test mode`。
  可以指定任意多个 test mode；**可以有多个同名列**，只要第二行给的 test mode 不同
  （例：一个 `Lsl` 列 mode 为 `QA`，另一个 `Lsl` 列 mode 为 `DT`）。
  **key column 不许指定 test mode，也不许有多个版本。**
- **必需的最小列集**：identifying columns（通常 `Suite name` + `Test name`）、
  `Test number`、`Lsl`、`Usl`、`Units`。
- **key column 组合**（按优先级，前者存在就不用后者）：
  `Suite name + Test name + Pins` → `Suite name + Test name`（**推荐**，SmarTest 建 CSV 时用这个）
  → `Limit key + Pins` → `Limit key`。
- **判定相关的关键列**：
  - `Lsl` / `Usl`（下/上 spec limit）。**不填 Lsl 则假定 1e23，测试永远 fail**；
    **不填 Usl 则假定 -1e23，测试永远 fail**。
  - `Lsl_typ`：`GT`（必须大于）/ `GE`（必须大于等于，**默认**）/ `NA`（无下限）。
  - `Usl_typ`：`LT`（必须小于）/ `LE`（必须小于等于，**默认**）/ `NA`（无上限）。
  - `Offset`：在结果与 limit 比对之前，**加到结果上的固定值**。
  - `Units`：结果与 spec limit 的单位（可有多个，对应不同 test mode/stage）。
  - `Test number`：未指定时**赋 -1**。
- **bin 相关列**：
  - `Bin_s_num` / `Bin_s_name`（software bin 号与名），范围 **0–32767**。
    文档注：SmarTest 本身也支持 5 字符以内的其他字母数字串，但**只有 0–32767 的整数
    与 SmarTest Data Formatter 兼容**。
  - `Bin_h_num` / `Bin_h_name`（hardware bin 号与名），**未指定时假定 -1**。
  - `Bin_type`：good 或 bad，**缺省为 bad**。
  - `Bin_reprobe`：yes / no，**默认 no**。
  - `Bin_overon`：该 bin 是否适用 overon 行为（到达 stop bin 后继续测），
    yes / no，**默认 yes，非法值也当 yes**。
  - 文档明写：**要使用 multibinning，必须同时指定 software bin 号和 hardware bin 号**；
    且这些信息**只有在测试的 fail 分支里有 multibin 时才被求值**。
  - `Bin_s_name` / `Bin_h_name` **软件通常不求值**，主要给人看。
- 其他列：`Limit key`（行名）、`Pins`（附加 key）、`Test_remarks`（注释，软件不求值）、
  `Exec`（`Y` 执行 / `N` 不执行）。**支持用户自定义列**，取值与含义由用户自定。
- 文档给的示例（抄录）：

```
"Suite name",  "Test name",       "Test number", "Units", "Lsl",   "Usl",   "Test_remarks"
"Test mode",   "",                "",            "QA",    "QA",    "QA",    ""
"Continuity2", "DC_CONT_P",       "555",         "UNIT",  "-0.1",  "0.1",   "WalkZP"
"DC_FreeVI",   "IDD_Shutdown",    "575",         "uA",    "-1",    "6.88",  "FreerunVI"
"DC_FreeVI",   "FREG_OUT_PWR_ON", "595",         "V",     "1.6",   "2.1",   "FreerunVI"
```

Functional changes 明写 **Introduced in SmarTest 6.5.0**。

### 8. 其他文件位置（`02.10.01.11_Appendix_C__File_Locations`）

- DRL 头文件：`/opt/hp93000/soc/com/include/drl.h`；
  同目录还有 `dcl.h`、`dcl_drl.h`。文档明写这三个文件**对写自定义数据检索工具很重要**。
- DRLDump 可执行文件：`/opt/hp93000/soc/.service/bin/DRLDump`。
- DRLDump 源码 `main.c` 与 makefile：`/opt/hp93000/soc/.service/DRLDump/`。
  文档**建议**把它当模板写自己的数据检索工具。
- STDF reader：`/opt/hp93000/soc/formatter/bin/STDFreader`。

**三层对照表见 [[mapping-results]]** —— GUI 操作 ↔ 文件 ↔ L1 命令 ↔ L2 API ↔ L3 接口 的按目的对照
（`wiki/mappings/mapping-results.md`；证据分三档写明，**`?` 与 `—` 不同义**：前者是「本页没找到证据」，
后者是「这一层不存在这个对应物」）。

## 验证

- **Event Formatter 的 Report window** —— `02.10.02` 明写它是「a report generating tool
  used for interactive debugging」，有 Report Dialog window 可定制输出的格式与范围。
  该章列出可查的验证性内容：Standard output of the Event Formatter、
  Shmoo output、**Fine result granularity**、Appendix C: Event Formatter Output Examples。
  `02.10.02.03` 明写：**无论 Report Dialog 怎么设，报告输出总是包含 test program、
  application model levels、testflow 三块信息**，并给了 test program 段的固定格式示例
  （开头三行 `########## Started Testprogram <名> ...` / `Test program ... of device <目录>` /
  `started on <日期> at <时间> on <主机> by <用户>`，结尾 `Test program terminated after
  N seconds ...` / `########## Ended Testprogram ...`）。
- **`DRLDump`** —— 用 DRL 读二进制 data log stream 的样本工具（`02.10.01.10`），
  有 Usage 与 Sample output 子页，可用来确认 EDF 内容读得出来。
- **`STDFreader`** —— 读回 STDF 的官方工具（`02.10.01.11` 给路径）。
- **[[integrated-result-tool]]** —— 加载 **STDF 或 EDL** 文件后，五个 summary tab
  会自动生成统计汇总。可直接用的判定性字段（`02.08.04.13.03.02.01` 明写）：
  `Pass#` / `Pass%`（带绿色横条图示）、`Fail#` / `Fail%`（带红色横条图示）、
  `Device#`，以及质量指标 `Min` / `Max` / `Mean` / `Sdev` / `Cp` / `Cpk` / `Cpl` / `Cpu`。
  左边 annotation ruler 用图标标出该行是否有 fail / alert / 数据被 exclude / shmoo hole；
  右边 overview ruler 每一行失败或有 alert 就画一个彩色小方块（**默认：红=fail、
  蓝=exclusion、黄=alert、青=shmoo hole**），悬停出 tooltip 说明原因。
  文档明写这些**默认全部启用**，可在 Annotations preference page 逐类关闭。
- **命令侧自检**：`FTST?` / `PASS?` / `CHER?` 可以直接把全局或 per-pin 结果打回来，
  是判断「这次执行到底 pass 还是 fail」最直接的手段。
- **Error Map 对照**：`EMAP?` / `ERMP?` / `ERCT?` / `ERCY?` / `FFCI?` 报出的内容，
  应与 `CHER?` 的 per-pin 结论一致——`02.06.11.01.02` 明说不一致的情形存在：
  **match loop cycles 不记录在 Error Map 里**，所以 match-loop 类失败必须用 `CHFA?` /
  `MCNT?`，不能指望 Error Map。
- **Error Map Tool 的 Overview → Cycles/Edges 两级对照**（`02.08.04.08.02` 明写的过程）：
  在 Overview tab 看哪些 cycle block 含错误，切到 Cycles（或 Edges，取决于配置）细化；
  **若「不是所有错误都在详细 error map 范围内」，就在 Overview 里选更靠后的 cycle block
  重复第 4–5 步，直到覆盖为止**——这本身就是一条「结果是否取全了」的检查。
- **`LotSummaryGenerator`** —— 对同一份 EDL，离线跑出来的 lot summary 应与在线看到的
  一致；文档明写没有 SmarTest 在跑时会给错误信息，可用作环境检查。
- **`02.10.02.05_Fine_result_granularity` (FRG)** —— 文档明写 FRG 是
  「a mode that provides pass/fail results for **each edge** of a tester cycle」，
  不开则整个 cycle 只有一个 pass/fail。它是**验证「失败定位精度」是否足够**的手段：
  文档明说 FRG 定位更精确但**产生更多数据**。

## 常见错误

- **`HRIT`/`HREX?` 之后 Error Map 内容没了** —— 文档明写这是**预期行为**：
  执行 high resolution timing 测量会删除指定 pin 的 Error Map。
  走 GUI 时测量完会自动补一次 functional test 恢复；**用 firmware 命令不会自动恢复**，
  需要自己补跑。这是本阶段最容易踩的坑。
- **match loop 失败在 Error Map 里查不到** —— 文档明写 match loop cycles 不记录在
  Error Map 中，必须改用 `CHFA?`（取最后 match loop cycle 的结果）或 `MCNT?`。
- **详细 error map 里找不到错误**（`02.08.04.08.01.01` 明写两个触发条件）：
  1. 测试 cycle 数太大，导致 **overview folder 里的 block size 大于 2k**；
  2. acquisition mode 被设成 **Force Cycle Oriented Mode**。
  文档给的两个解法：改用 extended memory（见 Result Mode 的 location 一节），
  或在 Result 菜单把 Acquisition mode 设为 **Force Failure Oriented**。
- **Recording abort / 结果存不全**（`02.08.04.08.04` 明写）—— 当详细 error map 放在
  **external memory** 时，要写入的数据量超过内存带宽就会发生 recording abort，
  效果是**不是所有请求的结果都能存下来**。原因与补救见
  `02.06.11.01.02.01.05_Dealing_with_storage_problems_on_Smart_Scale_systems`。
  文档明写的一个高发场景：**当一个 port 的全部或大部分 pin 属于同一个 Smart Scale
  channel group 时**（PS9G 是 4-channel group，PS1600 是 8-channel group）。
  缓解手段：把**只需要内部 error map 的那些 pin 放进 exception list**，
  它们的结果改走内部 error map，很多情况下就能避免 abort。
  **注意 `02.08.04.08.04.01` 明写 exception list 是全局的**：一个 pin 一旦入选，
  它在**所有包含该 pin 的 port 上**详细 error map 都落在 test processor 内。
- **配置不一致点不了 OK** —— `02.08.04.08.04.01` 明写 error code resolution 与
  result granularity 不独立，系统检查一致性，不一致时**标红该 port 并禁用 OK 按钮**。
- **想要 edge 级结果但默认配置给不出来** —— 文档明写 result granularity 2 的默认是
  「edges 1–4 一组、edges 5–8 一组」各成一个 result combination；
  **要报 edge 级信息必须改这个默认**（在 Edge to Result Mapping 窗口里改）。
  每个 combination 可累积 8 个 edge 的任意子集，**允许编号有缺口，
  同一个 edge 也可以被包含在多个 result combination 里**。
- **Pin Scale 9G 上 PRBS 测试的 error map 无效**（`02.08.04.08.01` Functional changes 明写）：
  **SmarTest 7.0.1 起，用 Pin Scale 9G 的 pin 产生 prbs、或把 DUT 数据与 prbs 比较的测试，
  error map 不工作。**
- **TMLimits 里忘填 limit 导致「测试永远 fail」** —— 文档明写不填 `Lsl` 假定 `1e23`、
  不填 `Usl` 假定 `-1e23`，两者都会让测试**永远 fail**。
- **bin 号超出 0–32767** —— 文档明写 SmarTest 本身能接受 5 字符以内的字符串，
  但**只有 0–32767 的整数与 SmarTest Data Formatter 兼容**，超范围会在下游 formatter 处出问题。
- **只用了一半 multibin** —— 文档明写用 multibinning **必须同时给 software bin 号和
  hardware bin 号**，且**只有在 fail 分支里存在 multibin 时才被求值**。
- **系统 data log stream 图表拖慢系统** —— `02.08.04.13.03.02.01` 明写
  dynamic updates **默认是关闭的**，打开后「when the data log stream contains a large
  number of entries, performance may suffer」。

`02.06_03_Errors` 一类的专门错误章未在本阶段阅读范围内核实，**文档未覆盖**。

## 下一步

**results 是九段流程的最后一段。本页不指向第十个 stage。** 结果产出后，测试流程本身结束，
剩下的是**结果的消费与回流**。为避免误导，这里如实记录文档实际覆盖了什么：

### 1. 回流到 [[run]]（本阶段唯一形成闭环的去向，文档明确支持）

`02.10.01.02_Data_Logging_Profiles` 描述了一个完整闭环：
yield 掉 → 在 test method 内监测到失败数超过阈值 → **从 test method 内部用一个函数调用
现场激活 debug profile** → 系统记录更细的数据（pin value result、first failing cycle 等）→
再分析。即**结果分析会反过来改变下一次执行时的日志配置**。

### 2. 结果的机器可读出口

- **STDF** —— `02.10.03_SmarTest_Data_Formatter` 把 V93000 测试结果格式化成 STDF，
  这是给下游/客户的标准交换格式。`02.10.03.06_Appendix_B__The_STDF_Reader` 提供读回工具。
- **CSV** —— `02.08.04.13.03.06_CSV_Export_command_line_tool`（Integrated Result Tool 的
  CSV 导出命令行工具）。
- **EDL 文件** —— Integrated Result Tool 与 `LotSummaryGenerator` 都能离线加载。

### 3. 三个「下游」章的实情（**与预期不符，据实记录**）

我按要求读了这三章的章首页，结论是**它们都不是结果数据的下游消费者**：

- `02.11_Data_Conversion_and_Bridges` —— 实际只有两个子章：**STIL Reader**
  （导入 STIL）与 **ASCII Interface**（Timing Translation / Vector Translation /
  Binary to ASCII Conversion）。这是**输入侧**的格式转换，不是结果侧的下游。
- `02.14_SmartProd` —— 文档明写它是「external interface tool」，用途是
  **监控 switch_version 操作**（同一台 host 上两个 SmarTest 版本切换时通知客户端）。
  与测试结果无关。
- `02.16_ACS_TE-Cloud` —— Advantest 云平台，提供虚拟机与远程访问 tester 资源的
  测试工程环境。是**开发和运行环境的云端化**，文档未把结果数据消费列为它的子章。

**推断：** 结果数据的真正下游是 **STDF/CSV/EDL 文件本身**——它们被交给外部的
数据分析系统（YMS、数据库、客户侧工具），而这部分**在本 wiki 的语料范围之外，
文档未覆盖**。建议不要为「results 之后还有一段」硬造 stage 页。

### 4. 一个文档明确提到的离线回路

`02.10.01.10_Appendix_B__The_DRLDump_Tool` 与 `02.10.01.07_LotSummaryGenerator`
都能对**已保存的 EDL 文件**做离线分析；`LotSummaryGenerator` 的输出是
**GDF 格式的 test summary**——这是比 EDF 更早的一代日志格式，文档明写
event data logging 与它 **co-exists**，因此老的下游工具不会被新机制淘汰。
