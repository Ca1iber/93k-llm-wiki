---
type: stage
title: Pattern / Vector — 标签（Label）与向量设置
tags: []
related: [project, pin, level, timing, testmethod, testflow, run, results, label, pattern-master-file, pattern-tools, pattern-editor, pattern-explorer, multiport-burst-editor, sequencer, sequencer-instruction, sqpg, sqlb, sqsl, sqst, tstl, apdv, apts, dmas, blup, vector-setup-file, pattern-master-file-format, execution-context, burst-label, multiport-burst-label, svec, ctim, clev, data-queue, sequencing-group]
sources:
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01_Testing_a_basic_digital_device.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.01.06_Displaying_the_ASCII_waveform_file_in_the_waveform_view.md
  - 01_Getting_started/01.03_Using_SmarTest/01.03.03.01.02_Debugging_patterns_efficiently.md
  - 02_System_reference/02.06_Command_Reference/02.06.07_Vector_Setup_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01_Concepts_of_vector_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01_The_structure_of_labels.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01.01_The_label_definition.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01.02_The_vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01.03_The_sequencer_program.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.02_Label_definition__sequencer_program__and_sequencer_area.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.03_Sequencer_areas_and_vector_areas.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.03.01_From_global_to_port_specific_vector_areas__Migration_and_compatibility.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.03.02_Missing_vector_data_and_migration_from_6.5_to_7.x.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.04_Addressing_the_vector_areas.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.04.01_Selecting_the_memory_type.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.04.02_Memory_pooling_within_channel_groups.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06_Overview_of_firmware_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.01_Low_level_and_high_level__edit__commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.02_Controlling_the_sequencers.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.03_Managing_the_sequencer_area.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.04_Downloading_vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.05_Managing_sequencer_constructs.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.06_Comments_on_vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07_Editing_and_executing_labels_at_firmware_level.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.01.01_Creating_a_label_with_low_level_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.01.02_Creating_a_label_with_edit_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.03.01_Inserting_a_sequencer_instruction.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.03.02_Deleting_a_sequencer_instruction.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.04_Executing_a_label.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08_Using_sequencer_instructions.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.01_Vector_generating_instructions.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.02_Address_instructions.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.03_Instructions_for_changing_the_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.03.01_Changing_the_timing_set__CTIM.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.03.02_Changing_the_level_set__CLEV.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04_Loops.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.01_Endless_loops.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.02_Counted_loops.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03_Match_loops.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.03_Fast_Sync.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05_Main_programs_and_subroutines.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.01_Main_labels.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.02_SVEC_subroutines.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03_Burst_labels_and_multi-port_burst_labels.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.01_Burst_labels.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02_Multi-port_burst_labels.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.09_Managing_the_data_queue.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.09.01_Data_transfer_from_the_vector_area_to_the_data_queue.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.10_Synchronizing_vectors_in_a_multi-port_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02_List_of_vector_setup_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.01_APDV_-__APpenD_Vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.02_APTS_-__APpend_TeSt.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.04_BLUP_-__BLock_UP_to_date.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.07_CNGV_-__CoNnect_Generate_Vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.13_DMAS__DMAS__-__Define_Memory_Area_Size.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.19_INGV_-__INsert_Generate_Vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.20_INSI_-__INsert_Instructions.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.27_SQLB__SQLB__-__SeQuencer_LaBel_definition.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.29_SQSL__SQSL__-__SeQuencer_Start_Label.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.30_SQST__SQST__-__SeQuencer_STate.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.34_TSTL__TSTL__-__TeST_Label.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.37_VDCP__VDCP___Vector_Device_Cycle_Parameter.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.39_VECD__VECD__-__VECtor_Download.md
  - 02_System_reference/02.06_Command_Reference/02.06.15_Commands_for_the_protocol_engine_per_pin.md
  - 02_System_reference/02.06_Command_Reference/02.06.15.01.02_Pattern_matching.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142.01_PATTERN.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.149_playPattern.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.204_SEQUENCER_STATUS_-__Sequencer.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.02_Creating_a_pattern.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.03_Viewing_and_editing_bursts_in_the_Pattern_Explorer.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.09_Checking_pattern_references.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15_Working_with_pattern_master_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.01_Creating_a_pattern_master_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.02_Loading_or_initializing_a_pattern_master_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.10_Merging_and_splitting_pattern_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03_Multiport_Burst_Editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.03_Dependencies_Between_the_Timing_Setup_and_the_Vector_Setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05.01_Function_of_the_base_wavetable.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.01.02.03_Relationship_to_Vector_Setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.11.02_Keeping_Waveform_Sets_Compatible.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.02.07.02.04.01_Creating_a_Pattern__Label.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.01_HVM_API_Introduction.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.01_How_to_use_the_test_suite_control_API.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.09_TestsuiteProxy.getSequencerLabel.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.29_TestsuiteProxy.setSequencerLabel.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04_Device_access_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06_Pin_mapping_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.md
  - 03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.11_Check_vector_setups.md
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# Pattern / Vector — 标签（Label）与向量设置

> 把 timing/level 已经定义好的波形，组装成定序器能逐周期发给 DUT 的**可执行指令流**（label / pattern），并把它落成 `<device>/vectors` 下的向量文件或 pattern master file——这是 testflow 与 run 能够"调用一个 pattern"的唯一接口。

## 目的

这一段流程解决的问题是：**timing 和 level 只描述了"一个周期长什么样"，还没有描述"哪些周期、按什么顺序、在什么条件下发出去"。** 后者由本阶段完成。

文档对 label 的定义（`02.06.07_Vector_Setup_Commands`）：

> A label is the basic processing unit of SmarTest. It consists of a sequence of instructions that serve to send a vector stream to the DUT, and is identified by a unique name.

**关键：label 不是"一块数据"，而是一段可执行的指令流。** 它由三个互相链接的部件组成（`02.06.07.01.01`）：

1. **label definition** — 名字、类型、基础 wavetable（base wavetable）、端口；
2. **vectors** — 一片物理波形数据（DC/DC 电源单元）数组，按索引寻址；
3. **sequencer program** — 一段指令序列，通过 `STVA` 指向那片数组，并决定它怎么被逐周期消费。

`02.06.07.01.01` 明确写了执行者：*"The tester channel module that interprets and executes the program is called sequencer."* 所以"写 pattern"= 写定序器程序 + 准备它要消费的向量数据，两件事必须同步做。

**本条决定了 testflow 怎么调 pattern（重要）：** 因为 label 是可执行指令流，"调用一个 pattern"在固件层就是 `SQSL "label"` 设定 start label，在 L2 层就是 `PRIMARY_STATUS::label()` 设定 primary 的 start label。它不是"把一段数据喂进去"。

## 前置条件

1. **pin 已定义** — 向量数据是按端口/引脚组织的，vector area 与 sequencer area 自 SmarTest 7.0.1 起都是**端口相关**的（`02.06.07.01.03`）。见 `[[pin]]`。
2. **level 已定义** — 向量里每个单元是驱动/比较的波形编号，波形编号要能解析到 level 定义。见 `[[level]]`。
3. **timing / wavetable 已完成** — `02.08.04.34.06.11.02_Keeping_Waveform_Sets_Compatible` 明写：*"You cannot start setting up vectors if the timing is not finished."* 见 `[[timing]]`。`02.08.04.16.04.03_Dependencies_Between_the_Timing_Setup_and_the_Vector_Setup` 描述了两边的具体依赖。
4. **wavetable 名字已存在** — `SQLB` 的 `wavetable` 参数引用一个波形表名；同一个 label 的 base wavetable 与运行期实际使用的 primary wavetable（由 `SPRM` 决定）*"must usually be identical"*（`02.06.07.01.01.01`）。
5. **设备目录下的 `<device>/vectors` 子目录存在** — 大的 vector setup 文件**必须**放在这里；pattern master file 本身**也必须**放在这里（`02.06.07.01.05`、`01.07.01.01.01`）。见 `[[project]]`。
6. **端口与 site 的规划已定** — 用 multi-port burst 或 execution context 时，端口集合需要事先定好（`02.06.07.01.08.05.03.02`）。

## 涉及对象

**文件 / 格式（file）**

- `[[vector-setup-file]]`（file，`.binl` / `.binl.gz`）— 装 label 与向量数据的载体；可以是"一个大文件装全部 label"，也可以是"一个 pattern 一个文件"（`02.06.07.01.05`）。
- `[[pattern-master-file]]`（file，`.pmfl`）— 本阶段的核心文件格式，列出要用到的 pattern 文件及其路径，**必须手工或用 ASCII 接口创建**，且必须位于 `<device>/vectors`（`02.06.07.01.05`）。
- `<device>/vectors` 目录（file）— 本阶段的产物目录（`01.07.01.01.01`）。

**GUI（gui）**

- `[[pattern-explorer]]`（gui）— 浏览已加载 setup 中的 pattern，新建/删除 pattern、port burst、multiport burst，编辑 burst，并启动 Pattern Editor / Multiport Burst Editor（`02.08.04.16`、`02.08.04.16.01`）。
- `[[pattern-editor]]`（gui）— 显示与**编辑** pattern；本页只覆盖"编辑/生成"这一半（`02.08.04.16.02`）。
- `[[multiport-burst-editor]]`（gui）— 专门的 multi-port burst 编辑器（`02.08.04.16.03`）。
- `[[timing-diagram-tool]]`（gui）— **分析/观察**工具，不是生成工具；与 Pattern Editor 的分工见下方「归属裁决」第 3 条。见 `[[timing]]`。

**L1 命令（L1）** — 见下节。

**L2 API（L2）** — 见「L2 — Test Method API」。

**L3（L3）** — 见「L3 — 外部控制」。

## L1 — Firmware / Setup Command

`02.06.07.02_List_of_vector_setup_commands` 列出本阶段全部 40 条命令：

`APDV`、`APTS`、`BCMT/BCMT?`、`BLUP`、`CMNT/CMNT?`、`CMVC`、`CNGV`、`CPYV`、`DELI`、`DELV`、`DLPP`、`DLTS`、`DMAS/DMAS?`、`DPPC`、`DPPS/DPPS?`、`DPSA/DPSA?`、`FTSM/FTSM?`、`GETA?`、`INGV`、`INSI`、`NODV?`、`RSET`、`SAOF/SAOF?`、`SPGV`、`SQGB/SQGB?`、`SQLA/SQLA?`、`SQLB/SQLB?`、`SQPG/SQPG?`、`SQSL/SQSL?`、`SQST/SQST?`、`SQTO/SQTO?`、`SREC/SREC?`、`TCMT/TCMT?`、`TSTL/TSTL?`、`VDCG?`、`VDCN`、`VDCP/VDCP?`、`VECC/VECC?`、`VECD/VECD?`、`VPAR?`

`02.06.07.01.06.01`–`.06` 把它们分成六组：低层/高层向量写命令、控制定序器命令、管理 sequencer area 命令、下载向量到 vector area 命令、管理 sequencer 构造命令、向量注释命令。

**高层（edit）与低层（low-level）的区别（`02.06.07.01.06.01`）：** 高层编辑命令**同步地**修改 sequencer area 与 vector area；多数高层编辑命令要求先用 `TSTL` 激活 label。

### 最小可用示例

**(a) 高层（edit 命令）方式创建 label**（抄自 `02.06.07.01.07.01.02`）：

```
APTS "test_2",MAIN,"table1"
TSTL "test_2",(@)
INGV 11,12
```

**(b) 低层方式创建 label**（抄自 `02.06.07.01.07.01.01`）：

```
DMAS?                        -- 查询可用内存
DMAS ...                     -- 定义内存区
SQLB "test_1",MAIN,4,8,"table1"
SQLA ...
DMAS? PARA ...
SQPG 0,STVA,0,,(@)
SQPG 1,GENV ...
$VECD ...                    -- 下载向量数据
```

**(c) label 定义命令 `SQLB` 的参数含义**（`02.06.07.01.01.01`，示例 `SQLB "test_1",MAIN,4,8,"table1"`）：名字、类型、端口/起始地址参数、长度、base wavetable 名。

### label 的六个类型（`02.06.07.01.01.01`、`02.06.07.01.08.05`）

| 类型 | 用途 |
|---|---|
| `MAIN` | 通用；只有关联**默认端口 `@`** 的 MAIN label 才能当 start label |
| `SVEC` | 向量子程序，可嵌套 7 层，由 `JSUB`/`JMPE`/`COGO` 调用，以 `RSUB`/`RETC` 结束 |
| `BRST` | burst，`CALL`…`BEND`，**不可嵌套** |
| `MPBU` | multi-port burst，**唯一一个名字在端口间不唯一**的类型，内部名字是 `<label>@<port_name>` |
| `DSRC` | digital source label，只被 `SSRC`/`SRCV` 使用，**不可执行** |
| `SJMP` | 旧类型，仅 Pattern Editor 里还能看到 |

### `SQPG` — 本阶段最重要的 L1 命令

`SQPG` 是写 sequencer program 的唯一入口，其 `instr` 参数覆盖全部 38 条定序器指令（`02.06.07.02.28`）。指令可分几族：

- **向量产生**：`GENV`（生成向量）、`RPTV`（重复向量）、`SRCV`（来自 source memory）
- **地址**：`STVA`（set vector address）、`STSA`（set start address）
- **结束**：`STOP`
- **循环**：`LBGN`/`LEND`（endless loop，只能是最外层）、`LBGN n`（counted loop，循环体内只允许 `GENV`/`SRCV`/`RPTV`/`NOP`）、`MACT`/`MRPT`（match loop）、`WTER`/`MBGN`/`MJPE`/`MEND`（旧式 timed match loop）
- **跳转/子程序**：`JSUB`/`JMPE`/`COGO`/`RSUB`/`RETC`/`RPTJ`/`RSJP`
- **burst**：`CALL`/`BEND`
- **setup 切换**：`CTIM`（换 timing set）、`CLEV`（换 level set）
- **其它**：`BRKV`、`WAIT`、`FLQU`（填数据队列）、`NOP`、`PRBS`/`LPBK`、`TMUA`、`JPPS`、`JTIN`、`MEAS`、`RGOP`、`XACT`

`STVA` 的地址寻址规则（`02.06.07.01.04`）：`param_1` 是全局地址，`param_2` 是端口相关地址；**必须是 8 的倍数**；padding / inactive 向量**也计入编号**；一个 label 内部的 **logical vector number** 从 0 开始只数 active 向量，且 `SRCV`、`JPPS`、`JSUB`、`MRPT`、`RPTJ` 都被算作逻辑向量。

**注意一个易错点**：`SQPG` 与 Pattern Editor 对 `COGO`/`JMPE` 的**参数顺序是相反的**（`02.06.07.02.28` 脚注）。

### 执行一个 label（`02.06.07.01.07.04`）

```
SQSL "test_2"
SPRM 101,1,101002,101003
FTST?
```

`SQSL` 指定 start label（必须是关联默认端口的 MAIN label，或者一个 burst / multi-port burst label）；`SPRM` 决定用哪套 timing/level 主集；`FTST?` 实际执行并返回全局 PASS/FAIL。若未发 `SPRM`，`FTST?` 默认用 waveform set 1 + timing set 1 + level set 1 + dps set 1。

### 归属裁决（本页与相邻 stage 的边界）

**裁决 1 — `Using_execution_contexts`（`02.06.07.01.08.05.03.02.03`）：归 `[[run]]`，本页只链过去。**

> **这一条是改判过的。** 本页初稿曾判它归本页（理由：文档位于 `Multi-port burst labels`
> 之下，且它由定序器族命令 `SQEC`/`SQRC`/`SQLC?`/`SQSC?` 操作）。
> 复核时逐字读了全文，**改判归 `[[run]]`**，理由如下。

文档自己怎么定位自己（逐字）：*"Execution contexts allow you to run subsets of one or even
more than one multiport burst **independently and in parallel**."* 全篇结构是：
它是什么（一段**具名端口列表**）→ 怎么起（把名字加到执行测试的命令上，如 `FTST?` /
`SQST RUN`）→ **Restrictions 五条**（端口必须属于当前 start label、两个 context 不得共用
channel、先起的必须用 `SQST RUN` 才能并行、主时钟重算会停掉所有用户定序器任务、
含 DC Scale 通道的 context 不能并行）。

**判据是内容不是位置**：五条限制、起测方式、错误行为——**整篇讲的都是运行期语义**。
`SQEC`（定义）/ `SQRC`（删）/ `SQLC?` / `SQSC?`（查询）这四条是**对运行期对象的操作**，
不是编进向量文件的 label 构造——execution context 不被 `SQLB` 定义，也不进向量文件。
初稿据「文档挂在 `Multi-port burst labels` 下」推定义权，那是**据位置判归属**；
位置与内容冲突时以内容为准。硬拆成「构造归 pattern、运行归 run」会造出一条假缝：
两半用的是同一份文档、同一组命令，没有可切的地方。

本页保留的接口是：multi-port burst **本身**（`MPBU`、`02.06.07.01.08.05.03.02`）归本页，
execution context 是**在它之上做并行执行**的机制，归 `[[run]]`。

**裁决 2 — burst label 与 multi-port burst label：归本页 `[[pattern]]`。**
理由：`BRST`/`MPBU` 是 label 类型（用 `SQLB` 定义），其内容是 `CALL`…`BEND` 写成的 sequencer program，产物是 `<device>/vectors` 下的向量文件；这全是本阶段的动作。旁证：`testflow.md` 已注明 `Loops` 一类定序器层构造"属 `[[pattern]]`"。

**裁决 3 — `CTIM` / `CLEV`：指令归本页，被切换的 timing set / level set 内容归 `[[timing]]` / `[[level]]`。**
理由：`CTIM`/`CLEV` 是 `SQPG` 的 `instr` 参数，写进 label 的 sequencer program，还牵涉 CTOF（Change Timing On the Fly）序列的块长度、与 match loop / sequencing group 的交互（`02.06.07.01.08.03.01`、`.03.02`），这些全是 pattern 侧知识。但"第 2 套 timing 长什么样"归 `[[timing]]`。文档给出的分界很清楚 —— `02.07.04.01.167_PRIMARY_STATUS` 注：*"note that the CTIM sequencer instruction changes the timing set, but does not change the definition of the primary"*。
另一条必须写下的文档事实：`02.06.07.01.08.03` 说*"These changes are global with respect to the current test; if you change the setup in a subroutine, the change remains valid after return to the calling routine."* —— 子程序里改了 timing set，返回后**不会自动恢复**。

**裁决 4 — APG（存储测试的 pattern）：跨 stage，不归本页。**
`02.12_Memory_Test_Plus_7.10.2` 里的 `02.12.03.03.02_APG_pattern_file`、`.03.03_APG_program_file`、`.03.04_Device_access_file`、`.03.06_Pin_mapping_file`、`02.12.06.17_MTP_MEMORY_TEST` 描述的是另一套机制：`.apg` master file + `.prog`（C 语言子集）程序，为存储器件编译执行。它与 label / sequencer / `SQLB` / `SQPG` **没有任何接口**，也不是"数值器件的 pattern"。**不要混写。** 本 wiki 的九个 stage 里没有 memory-test stage，因此这块目前无处安放，已在「存疑」中回报。

### 一个必须澄清的相邻概念

`02.06.15_Pattern_matching` **不是**本阶段的验证方法，也**不属于本阶段**。`02.06.15` 是 `Commands_for_the_protocol_engine_per_pin`（每引脚协议引擎命令）那一章；其中的 "pattern matching" 指运行期把收到的比特流与期望数据逐位比较（step width 为 1 个 data bit 或 1 个 token）。把它当作"检查 pattern 设置对不对"的手段是错的。

## L2 — Test Method API

- `[[PRIMARY_STATUS]]`（L2，`02.07.04.01.167`）— 本阶段与 testflow 的接合点。*"This member function specifies the (digital) sequencer start label name to be activated. … For multi-port testing, you can specify a multi-port burst label name as the start label."* 即：test method 通过 `PRIMARY_STATUS::label()` 指定要跑哪个 label。
- `[[SEQUENCER_STATUS]]`（L2，`02.07.04.01.204`）— 运行/停止定序器（`run()` / `abort()` / `stopCycle()` / `stopVector()`），运行模式 `TM::NORMAL`、`TM::ENDLESS_LOOP`、`TM::ENDLESS_PATTERN_LOOP`、`TM::STOPONERROR`、`TM::STOPONERROR_LOOP`。**文档明确：本 API 不支持 execution context**（见裁决 1）。
- `[[PATTERN_CONTROLLER]]` / `[[PATTERN]]`（L2，`02.07.04.01.142`、`.142.01`）— pattern 级控制对象。
- `[[playPattern]]`（L2，`02.07.04.01.149`）— 播放 pattern，多端口用 `PatternPort` / `CCTMultiportSync` 同步。
- `[[VEC_EVENTS]]`（L2）— 向量事件。
- `[[FW_TASK]]`（L2，`02.07.04.01.77`）— 用于在 test method 里直接下发固件命令；文档用它示范 match loop 的 buffer cycle 计算（配合 `EPRC?`）。
- `[[PRIMARY_STATUS]]::getTiming()` 与 `CTIM` 的关系见裁决 3。

## L3 — 外部控制

**SmartShell 在 7.10.3 不存在。** 全库唯一一篇 SmartShell 总述的 Functional changes 明写 `Introduced in SmarTest 8.2.5`，本 wiki 面向 7.10.3（该章共 1 篇，正文全是 PDF 外链）。**不得把它当作可用的 L3 接口。**

语料里本阶段唯一找到的真实 L3 材料是 **Test Suite Control API** 的两个访问器（`02.09.01.14.02.01.09`、`.29`）：

- `TestsuiteProxy.getSequencerLabel()` → `const std::string getSequencerLabel();` — *"This function retrieves the sequencer label used in the test suite."*
- `TestsuiteProxy.setSequencerLabel(const std::string& value)` → `bool` — *"This function sets the sequencer label for the test suite."* 参数格式要求：*"It must be in the format of \"label_name\""*（即带双引号）。

两者都标注 `Introduced in SmarTest 6.5.2`，因此 7.10.3 可用。使用方式见 `02.09.01.14.01_How_to_use_the_test_suite_control_API`：外部 C++ 客户端 include `testsuitecontrol_api.hpp`，`using namespace testsuitecontrol;`，编译需 `-I/opt/hp93000/soc/prod_com/include/ -m32`、链接 `-ltestsuitecontrol_api`，通过 `/opt/hp93000/soc/system/bin/run -x <user_executable_program>` 启动；典型调用链是 `initializeSession()` → `getTestsuite("mysuite")` → `setActiveSites(sites)` → `ts.executeActiveSites()` / `ts.isPass(siteNum)`。

即：**外部程序可以读/写 test suite 的 sequencer label**，但不能用这个 API 编辑 label 内容、sequencer program 或向量数据。

HVM API（`02.09.01.10.01`）面向的是执行事件与执行控制（*"access the SmarTest execution event information … control the execution"*），本阶段未见与 pattern/label 相关的接口。

**本阶段其余 L3 能力：**

文档未覆盖

## 产物

- **`<device>/vectors/`** — 本阶段的产物目录（`01.07.01.01.01_Device_directory_structure`）。
- **向量/pattern 文件**：`.binl` 或 `.binl.gz`。两种组织方式（`02.06.07.01.05`）：
  - 把所有 label 放进**一个大的 vector setup 文件**（必须位于 `<device>/vectors`）；
  - 或**一个 pattern 一个文件**，再用 pattern master file 指定用哪些。
- **pattern master file（`.pmfl`）** — 本阶段的标志性产物。格式（`02.06.07.01.05`）：

```
hp93000,pattern_master_file,0.1
-- The following file must reside in <device>/vectors:
files:
   sample1.binl

-- The following path points to <device>/vectors/pmfl_test:
path: ../vectors/pmfl_test

files:
  sample2.binl.gz
  sample3.binl.gz
```

  三条必须记住的规则：
  1. 文件本身**必须**放在 `<device>/vectors`；
  2. `path:` 默认是 `<device>/vectors`，但**一旦显式给出 path，相对路径的参考目录变成 `<device>/waste`** —— 所以 `<device>/vectors/sample` 要写成 `./vectors/sample`；
  3. 注释写在行首 `-- `（两个减号 + 一个空格）之后。

  使用 pattern master file 的好处是可以把 pattern 放在文件系统任意位置、且只加载/保存需要的那些；代价是引用的 pattern 数量很大时下载时间会很长（此时可以在 Test Program Explorer 里把它转成一个大 vector 文件）（`02.06.07.01.05`）。
- **comment（向量注释）** — 点级常量与块级注释，用 `CMNT`/`BCMT`/`TCMT` 系列管理（`02.06.07.01.06.06`）。
- **GUI 侧产物**：在 Pattern Explorer 里新建 pattern/port burst/multiport burst（`02.08.04.16.01.02`、`.01.05`、`.01.04`）；合并/拆分 pattern 文件（`02.08.04.16.01.10`）。

## 验证

以下全部是文档里写的检查手段，不是自行发明：

- **`FTST?` 返回全局 PASS/FAIL** — 执行 start label 后最直接的结果（`02.06.07.01.07.04`，其 `## Results` 段：*"FTST? returns a global PASS/FAIL result."*）。
- **`VCYC?` 检查 padding** — 向量按 8 的倍数送给 DUT，用户周期数不整除 8 时末尾补 break cycle；`VCYC?` 可以查当前 start label 的这个值（`02.06.07.01.07.04`）。
- **`BLUP` 的 state 参数** — `UPTD`（label 是最新的）/ `CHNG`（label 被改过）；用于查询/修改 label 的"是否最新"信息，文档提醒*"It should be used with care."*（`02.06.07.02.04`）。
- **Pattern Editor 显示** — 打开后可以显示已加载 setup 的 pattern 并编辑；波形画得对不对直接看这里（`02.08.04.16.02`）。
- **Waveform view** — 在 SmarTest Work Center 里右键 → Show In > Waveform，把 ASCII 波形文件显示到波形视图（`01.01.08.02.01.06`）。
- **检查 pattern 引用** — `02.08.04.16.01.09`：被别的 pattern 引用的 pattern 不能被删除；报错信息里点 `Show References` 会打开 Search 视图列出引用者。用于维护 pattern master file 结构的有效性。
- **Test Program 360 的 release check：Check vector setups** — 检查向量设置相关风险，文档列出的两类是：pattern 文件里缺引脚/引脚未定义、label 与 multiport burst 重名（`03.13.04.07.11`）。
- **数据队列检查** — `DQUE?` 可查数据队列的最小液位；`FLQU` 用于填充数据队列（`02.06.07.01.09`、`02.06.07.01.09.01`）。
- **`SQST?`** — 查询定序器状态（`02.06.07.02.30`）。
- **调试路径**（`01.03.03.01.02_Debugging_patterns_efficiently`）— 文档给出的高效调试 pattern 的操作序列与快捷键。

## 常见错误

- **用 `INSI` + `SQPG` 插入指令会打乱向量指针** — `02.06.07.01.07.03.01` / `.03.02` 记载：插入/删除定序器指令时，向量指针会被破坏；应改用 `INGV`/`DELV` 一类向量级操作。
- **`STVA` 地址不是 8 的倍数** — 会失败；`02.06.07.01.04` 明确要求 `STVA` 的地址必须是 8 的倍数，且 padding / inactive 向量也占编号。
- **多端口 burst label 名字冲突** — `MPBU` 是唯一名字在端口间不重复的类型，内部名字为 `<label>@<port_name>`；label 与 multiport burst 重名会被 Test Program 360 的 "Check vector setups" 报出来（`03.13.04.07.11`、`02.06.07.01.08.05.03.02`）。
- **删除被引用的 pattern** — 会被拒绝并弹错误信息（`02.08.04.16.01.09`）。
- **base wavetable 与 primary wavetable 不一致** — 前者只被 Pattern Editor 用来显示/编辑，后者（由 `SPRM` 给出）才是运行期用的；文档说两者*"must usually be identical"*（`02.06.07.01.01.01`、`02.08.04.16.04.05.01`）。
- **在子程序里改了 setup 忘了改回来** — `CTIM`/`CLEV` 的改动对当前测试是全局的，子程序返回后依然有效（`02.06.07.01.08.03`）。
- **sequencing group 名字 "Default" 被复用** — 自定义 sequencing group 不得占用 `Default` 这个名字（`02.06.07.01.10`）。
- **数据队列下溢** — Pin Scale 上需要至少 0.5 µs 的缓冲；`DQUE?` 可以检查最小液位（`02.06.07.01.09`）。
- **`SVEC` 嵌套超过 7 层** — `02.06.07.01.08.05.02` 给出嵌套深度上限。
- **counted loop 里放了不允许的指令** — `LBGN n` 的循环体内只允许 `GENV`/`SRCV`/`RPTV`/`NOP`（`02.06.07.01.08.04.02`）。
- **match loop 的必需指令序列写漏** — `02.06.07.02.28` 给出了 timed 与 counted 两类 match loop 的必需序列，漏掉会报错。
- **`SQPG` 与 Pattern Editor 的 `COGO`/`JMPE` 参数顺序相反** — 手写固件命令时容易搞反（`02.06.07.02.28` 脚注）。

各命令页的 `Errors` 段是逐条错误的权威入口（例如 `02.06.07.02.29_SQSL`、`.30_SQST`、`.27_SQLB`、`.34_TSTL`）。

## 下一步

`[[testmethod]]`

pattern 做完，链路进入"把 pattern 用起来"的一步：test method 通过 `PRIMARY_STATUS::label()` 指定要执行的 start label（多端口时可直接给一个 multi-port burst label 名），从而把 setup 数据与测试流程接起来。在此之前 pattern 只是磁盘上的文件，还没有任何执行语义。
