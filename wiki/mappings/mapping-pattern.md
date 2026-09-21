---
type: mapping
title: Pattern 的三层对照
layer: n/a
stage: pattern
tags: [mapping, pattern, label, gui, firmware-command, test-method-api, vector-setup-file, pattern-master-file]
related: [pattern, pin, level, timing, testmethod, run, pattern-explorer, pattern-editor, multiport-burst-editor, pattern-master-file, vector-setup-file, timing-file, wavetable-file, sprm, sqst, ctim, primary-status, sequencer-status, smartrdi, sequencer, tpi-program-routines, test-suite-control-api]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.01_Opening_the_Pattern_Explorer.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.02_Creating_a_pattern.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.03_Viewing_and_editing_bursts_in_the_Pattern_Explorer.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.04_Creating_a_multiport_burst.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.05_Creating_and_assigning_a_port_burst.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.07_Moving_or_copying_pattern_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.09_Checking_pattern_references.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.10_Merging_and_splitting_pattern_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.11_Importing_patterns.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.12_Exporting_patterns.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.14_Editing_properties_in_the_Pattern_Explorer.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15_Working_with_pattern_master_files.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.01_Creating_a_pattern_master_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.05_Virtual_sequencer_instructions_for_protocol_patterns.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.04_Editing_patterns.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10_Inserting__editing__and_deleting_sequencer_instructions.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10.01_Inserting_counted_match_loops.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10.02_Sequencer_instructions.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.13_Displaying_failure_data.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.16_Creating_a_Digital_Source_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.17_Creating_a_Digital_Capture_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03_Multiport_Burst_Editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03.04_Working_with_sync_groups.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.01_Definitions__Vector__Pattern__Burst__etc.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.02_Editor_status_line.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05.01_Function_of_the_base_wavetable.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.06_How_Vectors_are_Stored_in_Sequencer_Memory.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.09_Protocol_pattern_specifics_of_the_Pattern_Explorer.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01.02_The_vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.04.01_Selecting_the_memory_type.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17_Sync_group_support_with_SmartRDI.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.09_TestsuiteProxy.getSequencerLabel.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.29_TestsuiteProxy.setSequencerLabel.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Pattern 的三层对照

## 这张表在说什么

Pattern 这一段的配置，语料里**同时存在三套说法**：Pattern Tools（Pattern Explorer /
Pattern Editor / Multiport Burst Editor，GUI）、`<device>/vectors` 下的向量文件与
pattern master file（file）、以及一组向量设置命令（L1）。**这三套是不是同一个东西的三种写法——
语料回答了，但回答的方式和 `[[pin]]` 那一段相反。**

同族那一页（`mapping-pin`，`wiki/mappings/mapping-pin.md`）的地基是
GUI 文档自己声明「文件里的固件命令与 GUI 参数逐条对应」。
**pattern 这一段没有这样一句。** 它给的地基是下面四块。

**(1) GUI 的 `pattern` 就是 L1 的 `label`。** `02.08.04.16.04.01`：

> 「A label is the name of a pattern.」

> 「In the context of the Pattern Debug Tool the terms label and vector label are often used as a synonym for pattern. To avoid confusion, the term label is not used in the Pattern Debug Tool documentation.」

这一段给了两件事：① 两层指的是同一个东西；② **Pattern Tools 的文档里刻意不用 `label` 这个词**。
所以「在 GUI 文档里搜不到 label」**不是缺口，是语料自己定的规矩**。

**(2) L1 命令自己的 `## Application` 段指着 Pattern Tool。** `02.06.07.02.28` 的 `## Application`
段全文只有一句：

> 「Download and edit command in the Pattern Tool.」

**(3) Pattern Editor 的 Instruction 列，与 `SQPG` 的 `instr` 参数是同一套指令**——
而且语料自己把**它们哪里不一样**写下来了（`02.08.04.16.02.06.10.02` 的脚注，`02.06.07.02.28` 有同一条）：

> 「The sequence of the two parameters is different for the SQPG command and the Sequencer instructions of the pattern editor: command SQPG utilizes the sequence "param_1 = label if error flag is not set" and "param_2 = label if error flag is set" for the two instructions COGO and JMPE; the reversed sequence "<pattern1> = error flag is set" and "<pattern2> = error flag is not set" is used for the two sequencer instructions COGO and JMPE of the pattern editor.」

**这句话只有在「两边是同一套指令」成立时才需要说。** 它写下来的理由就是「同一个指令、两套参数顺序」——
所以它同时证明了等价**和**不等价的边界。`[[pattern]]` 的「常见错误」里那条
「`SQPG` 与 Pattern Editor 对 `COGO`/`JMPE` 的参数顺序是相反的」，出处就是这一句。

**(4) GUI 操作会写进文件，这一句也是明说的。** `02.08.04.16.01.15.01`：

> 「Working with the Pattern Explorer on your test setup will complete the pattern master file with paths and file names.」

`02.08.04.16.01.02` 补了另一条：

> 「When saving the new pattern, it is automatically added to the pattern master file.」

**「三层」这个词在本页要放宽理解**：§2.5 的格式给了五列（GUI / 文件 / L1 / L2 / L3），
而这一段**L3 只有两格是真的、L2 只在五行上有值**——不是我没找到，见下面「对不上的地方」。

## 对照表

**读法**：一格填了名字 = 有证据（证据是什么见下一节）；`?` = 语料没说，**本页不猜**；
`—` = 这一层不存在这个对应物（不是「没找到」）。名字后带 `（推断）` 的，是本页按职责排的对应，
**不是文档明说的**，依据写在下一节。**带（图证）的格子 = 那一格的名字在 raw 的图上直接看得见**
——是哪张图、图里的字为什么搜不到，见证据节 **④** 与「对不上的地方」**⑬**。

**表内的 raw 路径只写分类号**（例：`02.06.07.02.28`），**全相对路径见「出处」一节**——
本页要引的 L1 指令名（`SQPG`、`SQSL`、`SQLB`、`SQLA`、`FLQU`、`BWDF`、`DQUE?`、`VCAT`、`TMUD`）
**都不在 `extract/prose-allowlist.txt` 里**，所以它们一律是反引号 + 分类号，不是 wikilink。
名字在清单里的那些（`pattern-explorer`、`pattern-editor`、`multiport-burst-editor`、
`vector-setup-file`、`pattern-master-file`、`timing-file`、`wavetable-file`、
`sprm`、`sqst`、`primary-status`、`sequencer-status`、`smartrdi`、`tpi-program-routines`）
才写成 wikilink，其余一律反引号。

| 目的 | GUI | 文件 | L1 命令 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 建一个 pattern（= L1 的 label）：类型 / 端口 / 所在目录 | [[pattern-explorer]]（`New > Pattern`）（**图证**：对话框六格，见证据节 ④） | [[vector-setup-file]]（`Folder` 默认 `../vectors`）（**图证**） | `SQLB`（02.06.07.02.27，**推断**） | — | — |
| 改 pattern 的类型 / wavetable / memory / Location，改名，删除 | [[pattern-explorer]]（properties 表）（**图证**：`Type` / `WaveTable` / `Memory` / `Location` 四列表头） | [[pattern-master-file]]（`Location` 列只在 pmfl setup 里） | ? | — | — |
| 插入 / 编辑 / 删除 sequencer instruction（Instruction 列） | [[pattern-editor]]（**图证**：Instruction 列的插入列表） | [[vector-setup-file]] | `SQPG` / `SQPG?`（02.06.07.02.28） | ? | — |
| counted match loop（`MACT` + 向量行 + `MRPT`） | [[pattern-editor]]（**图证**：`MACT 32` / `MRPT 5` / `REPEATED`） | [[vector-setup-file]] | `SQPG` 的 `MACT` / `MRPT`（02.06.07.02.28） | ? | — |
| 内存类型 SM / SHMEM | [[pattern-explorer]]（`Memory Type`）（**图证**：Explorer 的列头是 `Memory`，`Memory Type` 是 New Pattern **对话框**的字段名——见证据节 ④（b）） | [[vector-setup-file]] | `SQLA`（02.06.07.01.04.01 指名） | — | — |
| base wavetable（显示/编辑用）与 primary wavetable（执行用）分开 | [[pattern-explorer]]（base）；primary 在 testsuite dialog 或 testmethod 里指定 | [[timing-file]] | [[sprm]] | [[primary-status]]（**推断**到具体成员） | — |
| burst / port burst / multiport burst 的组成 | [[multiport-burst-editor]] / [[pattern-explorer]] | [[pattern-master-file]] | `SQPG` 的 `CALL`（GUI 显示成 `CALL pattern_name`）；`BEND`（GUI 侧不显示） | ? | — |
| sync group（端口同步） | [[multiport-burst-editor]]（sync group 页）/ [[pattern-explorer]]（`Sync Group` 列）（**图证**：列头逐字 `Sync Group`） | [[pattern-master-file]] | ? | [[smartrdi]] 的 `syncGroup()` / `addPort()` | — |
| Digital Source：DSRC label + VVC | [[pattern-editor]]（`New Setup` → Setup Wizard） | [[vector-setup-file]] | `SQPG` 的 `SSRC` / `SRCV` | — | — |
| 数据队列下溢的防护与查询 | `Data Queue`（02.08.04.16.04.08） | — | `FLQU` / `BWDF` / `DQUE?` | ? | — |
| protocol pattern（由 transaction 生成）的 instruction 列 | [[pattern-editor]] | [[vector-setup-file]] | — | `TRANSACTION_SEQUENCE` / `SYNCHRONIZED_TEST`（02.07.04.01.256 / .239） | — |
| digital capture pattern | [[pattern-editor]]（Digital Capture setup） | — | ? | `DIGITAL_CAPTURE_TEST` / `VECTOR`（02.07.04.01.35 / .269） | — |
| protocol pattern 在 Pattern Explorer 里被删掉 | [[pattern-explorer]] | — | `TMUD`（02.06.02.02.258） | — | — |
| 指定 X-mode | [[pattern-editor]] / [[pattern-explorer]] | [[wavetable-file]]（`STATEMAP` 段） | `VCAT`（02.06.02.02.318） | ? | — |
| pattern master file 的建立与维护 | [[pattern-explorer]] | [[pattern-master-file]] | — | — | [[tpi-program-routines]] 的 `DataManager` / `dm_vector` / `dm_pattern_master_file` / `dm_pload` / `dm_plinit` |
| 导出 / 导入 pattern（ASCII Interface / STIL） | [[pattern-explorer]] | `.avc` / `.tmf` / `.wtb`（ASCII）；`.pat.stil`（STIL） | — | — | ? |
| 执行一个 pattern / 指定 start label | ? | — | `SQSL` / [[sqst]]（`SQST RUN`） | [[primary-status]]（`label()`）/ [[sequencer-status]] | `TestsuiteProxy.getSequencerLabel()` / `.setSequencerLabel()` |

**表里没有的**：L1 侧六个 label 类型
（`MAIN` / `SVEC` / `BRST` / `MPBU` / `DSRC` / `SJMP`，出自 `02.06.07.01.01.01` 与
`02.06.07.01.08.05`，**那两篇本页没读，转自 `[[pattern]]`**）与 GUI 的 `New > Pattern`
类型表（`Main` / `SJMP` / `SubRoutine` / `Burst` / `DSRC`）**是两套词，只有部分重合**。
配对见「对不上的地方」②，**本页不把它塞进表里当证据**。

**主表里几处 `—` 是有出处的，不是省事**：

- 「protocol pattern 的 instruction 列」那一行的 L1 是 `—`，因为那些指令**按文档自己的说法不在固件层**：

  > 「The editor does not simply display the generated vector stream, but adds sequencer instructions in the Instruction column which are virtual in the sense that they do not exist on the firmware level.」

- 「数据队列」「digital capture」「执行一个 pattern」「导出 / 导入」四行的 `文件` 是 `—`，
  因为它们动的是**运行期数据、另一种格式的文件、或别的阶段的产物**，不是本阶段的 setup 产物文件。

## 证据：哪几格是钉死的，哪几格只是「那边链过来了」

**证据分四档，本页不把它们混成一种。**

**① 语料明说对应（最硬）** —— 就是上面那四块地基。它钉住的是**两件事**：

- **GUI 的 instruction 列 ↔ `SQPG` 的 `instr` 参数**（地基 2 + 3）。所以主表里
  「插入 instruction」「match loop」「burst 的组成」「Digital Source」「数据队列」几行的
  **L1 列由这一句背书**——列名是两边逐字相同的那一批。
- **GUI 操作 ↔ pattern master file 的内容**（地基 4，两句）。

**它没有钉住「哪个 GUI 字段对应哪条命令」。** 那一层在表里分两种接法：
**有链接接住的三格**（`SQLA`——GUI 的 `Memory Type` 字段链到 `02.06.07.01.04.01`，那一篇指名
`SQLA`；`VCAT`、`TMUD`，各有 GUI 文档直接链过去）标的是分类号；
**没有桥、只能按职责排的两格**（`SQLB` 与 `[[primary-status]]` 的具体成员）标了 `（推断）`。

**② 文档之间有链接（次硬，逐条可查）** —— 取自 `extract/edges.jsonl`。
这一段的方向**和 pin 那一段相反**：**GUI → 命令的链接只有 30 条，命令 → GUI 的链接有 63 条**，
而且后者才是承重的——**`SQPG` 自己把读者送回 GUI 的指令列表**。

**GUI 侧 → `02.06` / `02.07`（30 条，全部落在本阶段）：**

| 源文档（GUI 侧） | 链到 | 条数 |
|---|---|---|
| `02.08.04.16.01.02_Creating_a_pattern.md` | `Selecting the memory type` | 1 |
| `02.08.04.16.02.03_Pattern_editor_properties_view.md` | `Drive actions`、`Receive actions` | 2 |
| `02.08.04.16.02.04.03_STATEMAP_section_of_the_wavetable.md` | `Representing a pattern in device orientation` | 1 |
| `02.08.04.16.02.05_Virtual_sequencer_instructions_for_protocol_patterns.md` | `Protocol Aware ATE`、`TRANSACTION_SEQUENCE`、`SYNCHRONIZED_TEST`、`Vector based synchronization` | 4 |
| `02.08.04.16.02.06.10.01_Inserting_counted_match_loops.md` | `Match loops`、`Adjusting the junctions between match loop and surrounding label` ×2 | 3 |
| `02.08.04.16.02.06.10.02_Sequencer_instructions.md` | `MSET`、`SQPG` ×2、`FLBL`、`Fast Sync` ×2、`EPRC?` | 7 |
| `02.08.04.16.02.06.17_Creating_a_Digital_Capture_setup.md` | `DIGITAL_CAPTURE_TEST`、`VECTOR` | 2 |
| `02.08.04.16.04.07_X_Modes.md` | `VCAT` | 1 |
| `02.08.04.16.04.08_Data_Queue.md` | `DQUE?` ×2、`BWDF`、`Data queue considerations for the Pin Scale systems`、`Managing the data queue` | 5 |
| `02.08.04.16.04.09_Protocol_pattern_specifics_of_the_Pattern_Explorer.md` | `TMUD`、`Transaction based protocol testing` | 2 |
| `02.08.04.16.04.10.01_Reconstructing_transaction_signals.md` | `Parameter reconstruction` | 1 |

**命令 / API 侧 → GUI（63 条，只列落在本阶段的那些）：**

| 源文档（L1 / L2 侧） | 链到 | 条数 |
|---|---|---|
| `02.06.07.02.28_SQPG`（+ `02.06.02.02.237` 的同一篇副本） | `Sequencer instructions`（含脚注那条） | 4 |
| `02.06.02.02.164_MSET`（+ `02.06.10.02.08` 副本） | `Sequencer instructions`（`MEAS`） | 6 |
| `02.06.02.02.87_DQUE?`、`02.06.07.01.09_Managing_the_data_queue`、`02.06.07.01.09.03` | `Data Queue` | 4 |
| `02.06.07.01.10.01.01_Sequencing_groups_and_pattern_structure` | `Sequencer instructions`（`CLEV` / `CTIM` / `CONTINUE`） | 3 |
| `02.06.07.01.08.04.01_Endless_loops`、`02.06.07.01.08.04.02_Counted_loops`、`02.06.07.01.08.05.02_SVEC_subroutines` | `Creating a pattern` | 3 |
| `02.07.13.24.49.01.01_instruction` | `Sequencer instructions` / `Inserting counted match loops` | 3 |
| `02.06.02.02.68_DFTD`、`02.06.16.01_Principles_of_jitter_injection` | `Sequencer instructions` | 2 |
| `02.07.04.01.167_PRIMARY_STATUS` | `Sequencer instructions`（`CTIM` / `CLEV`） | 2 |
| `02.07.13.08.17_Sync_group_support_with_SmartRDI`（+ `.01_addPort`、`.02_syncGroup`） | `Working with sync groups` | 4 |
| `02.06.07.01.01.02_The_vectors` | `Function of the base wavetable` | 1 |
| `02.06.07.01.08.04.03.01_Counted_match_loops` | `Inserting counted match loops` | 1 |
| `02.06.07.01.08.04.03.03.01_How_to_use_Fast_Sync` | `Creating a multiport burst` | 1 |
| `02.07.04.01.76_FwGuard` | `Pattern Editor` | 1 |

**链接证的强度要说清**：一条链接**只证明「那篇文档认为读者该去看这一篇」**，
**不证明两个东西等价**——可能是「见也」，也可能是「区别在这里」，也可能是「前提」。
本页只在主表的**同一行**里用它们，**不跨行搬**。

**③ 只有命令侧 / API 侧证据** —— 主表最后一行「执行一个 pattern / 指定 start label」：
**GUI 格是 `?`，而 L1、L2、L3 三格都有名字**。它们的事实来自 `[[pattern]]`、
`02.06.07.01.07.04`、`02.07.04.01.167` 与两篇 L3 原文，**但语料里没有一篇 GUI 文档链到
执行 start label 的命令**——所以 GUI 那一格是 `?` 不是 `—`：`?` 的意思是「本页没找到证据」。

**其余九格 `?` 都是同一个意思，不是「不存在」**：L1 列三格（改 properties、sync group、
digital capture），L2 列五格（instruction 编辑、match loop、burst 组成、数据队列、X-mode），
L3 列一格（导出 / 导入）。**九处全是「本页没找到那一条桥」，一处都不是「语料说没有」。**

**附：本页的推断只有表里标了 `（推断）` 的两格**：`SQLB`（建 label 的命令——语料没有一句
把它与 GUI 的 `New > Pattern` 对话框连起来；依据是 `[[pattern]]` 的命令清单与
`02.06.07.01.07.01.01` 的低层建 label 例子，**那篇原文本页未读，转自 stage 页**），
与 `[[primary-status]]` 的具体成员（GUI 文档只说 primary wavetable「in a testmethod」，
没说哪个 API）。

**④ 图证（2026-09-20 加，本页用到了）** —— 从 raw 自带的截图里读出来的。
（`schema.md` §2.5：**④ = 图证**。）

**本页 sources 里带图的文档共 28 篇 / 114 张**（**全页六页里最多**——因为 `02.08.04.16.01`
与 `.16.02` 两族把每一个图标都截了一遍，`119794` / `128874` / `99926` 之类的**小图标**占了大半）。
**本页读了四张**，挑的是「能看见一列名字」的那四张；**其余一百一十张没看**。
**四张都是窗口截图，也都不是小图标。** 逐张：

**（a）`99506.png`（`02.08.04.16_Pattern_Tools`，alt `Pattern tools overview`）——
这一张把 Pattern Explorer 的列头全摆出来了。** 图是整个 workbench 的截图，
三个工具被黄框标出（`Pattern Explorer` / `Pattern Editor` / `Multiport Burst Editor`）。
下左的 Pattern Explorer 表**列头逐字是**：
`Name | Port | Sync Group | Type | WaveTable | Memory | State | Location`；
表里的行逐字有 `sbi-ports`、`testPA1`、`testPA`、`testParalell`、`arbFailPattern_s`、
`arbPassPattern_` 开头的两个（**列宽不够，图上被截断了**），
取值里有 `sbiB` / `sbiA`（Port）、`Main`（Type）、`eeprom`（WaveTable）、
`SM`（Memory）、`UpdateDate`（State）、`../vectors/`（Location）。
**它解决掉的格子：**

- **「改 pattern 的类型 / wavetable / memory / Location，改名，删除」的 GUI 格**
  ——原写「[[pattern-explorer]]（properties 表）」，**图上就是这四列**（`Type` / `WaveTable` /
  `Memory` / `Location`）。**GUI 格由这张图钉死。**
- **「建一个 pattern」那一行的 `文件` 格**（原写 `Folder` 默认 `../vectors`）
  ——图上 `Location` 列的值逐字是 `../vectors/`；**与（b）那张对话框里的 `Folder: ../vectors`
  互相印证**（但**两处的字面不同**：Explorer 叫 `Location`，对话框叫 `Folder`，见（b））。
- **「内存类型 SM / SHMEM」的 GUI 格**——**这里要照实纠一处**：本页表里写的是
  `[[pattern-explorer]]（`Memory Type`）`，而**图上 Pattern Explorer 的列头是 `Memory`**
  （值 `SM`）；`Memory Type` 是**（b）那张 New Pattern 对话框**的字段名。
  两处都不是笔误（`02.08.04.16.01.14` 正文写的是 `Change the memory`，
  `02.08.04.16.01.02` 的对话框字段写的是 `Memory Type`）——**本页在表里把两个名字都留着了**。
- **「sync group」那一行的 GUI 格**（原写 `[[pattern-explorer]]（`Sync Group` 列））
  ——**图上列头逐字 `Sync Group`**。**GUI 格由这张图钉死**；`L1` 那一格照旧是 `?`
  （**图里没有任何固件命令名**）。

**grep 不到的字**：`UpdateDate`（0 命中）、`testParalell`（0 命中）、`arbFailPattern`（0 命中）、
`sbi-ports`（0 命中）、`MACT 32` / `MRPT 5`（0 命中）。
`Sync Group` / `WaveTable` 能搜到，但**命中的是别处的正文，不是这张表**——
所以**「这些名字同时出现在同一张表里」这件事只有图上看得见**。

**（b）`99692.png`（`02.08.04.16.01.02_Creating_a_pattern`，alt `Creating a new pattern`）——
New Pattern 对话框。** 六格逐字是：`Pattern Name:` = `PatternName1`、
`Pattern Type:` = `Main`（下拉）、`Port:` = `@`、`Memory Type:` = `SM`（下拉）、
`Wavetable:` = `eeprom`、`Folder:` = `../vectors`（旁边 `Browse...`）；按钮 `Finish` / `Cancel`。
**它解决掉的格子**：「建一个 pattern（类型 / 端口 / 所在目录）」那一行的 **GUI 格**——
**这不是「看起来像」，是三个字段名与那三个词逐个对上**（`Pattern Type` ↔ 类型、
`Port` ↔ 端口、`Folder` ↔ 所在目录）。**同一格还由（a）的 `Location` 列印证。**
**它答不了的**：该行 `L1` 格里的 `SQLB` **仍然是（推断）**——**图里没有命令名**，
所以（推断）**本页没动**。
**grep 不到**：`PatternName1`（0 命中）、`eeprom`（0 命中）。

**（c）`112686.png`（`02.08.04.16.02.06.10_Inserting__editing__and_deleting_sequencer_instructions`）。**
图是 Pattern Editor 的一部分：上面是引脚信号列（`LM393_OUT (ID)` / `LM393_IN_POS (TP)` /
`LM393_IN_NEG (TP)`，两列 `X-Mode Area` 值 `(x1)`，`Protocol` 值 `1-bit`），
下面是 `Vector# | Instruction | Comment` 三列，值逐字有 `0 X`、`1 X`、`2 RPTV`、`3 RPTV 1`、
`4 LOOP`、`5 LOOPEND`、`6 JSUB`、`7 JPPS`、`8 MTST`、`9 SRCV`；
右侧一个**插入指令的列表框**（`RPTV` / `RPTV 1` / `LOOP` / `LOOPEND` / `JSUB` / `JPPS` /
`MTST` / `SRCV` …）加一个 `RPTV` 的悬浮说明框。
**它解决掉的格子**：「插入 / 编辑 / 删除 sequencer instruction（Instruction 列）」那一行的
**GUI 格**——原写「[[pattern-editor]]」，**图说明了「Instruction 列」是哪个列、插入是怎么弹出来的**。
**它答不了的**：那一行的 L1 格（`SQPG` / `SQPG?`）**图没帮上**；**列表框里也没有 `MACT` / `MRPT`**
——**所以「counted match loop」那一行靠的是（d），不是这一张。**

**（d）`122707.png`（`02.08.04.16.02.06.10.01_Inserting_counted_match_loops`，
alt `Counted match loop in pattern editor`）—— 这一张把 `MACT` / `MRPT` 钉到了 GUI 侧。**
图的 `Instruction` 列里逐字有：`MACT 32`（跨第 35–66 行）、第 67 行 `MACT` + `Comment` 列
`compare Event cmpHig`、第 68 行 `MRPT 5` + `Comment` 列 `dummy vector`、第 73 行 `REPEATED`；
紫色底纹横跨循环体；右下角一个 **Properties 面板**逐字是
`Event Name` = `cmpHig`、`Event Type` = `Compare`、`Event Group` = `docu`、
`Reference Count` = `1`、以及 `Setup` 下的 `Compare Type` = `High`。
**它解决掉的格子**：「counted match loop（`MACT` + 向量行 + `MRPT`）」那一行的 **GUI 格**
（原写「[[pattern-editor]]」）——**图把这三样在 GUI 上长什么样摆出来了**，
这**正是本页 ⑬ 原先说「只有图能答」的那一类问题**。`Comment` 列填的是
`compare vector` / `compare Event cmpHig` / `dummy vector`。
**它答不了的**：`L1` 格里的 `SQPG` 的 `MACT` / `MRPT` **是另一层的名字**，
**图里没有 `SQPG`**；Properties 面板里的 `Reference Count` **与 `MACT 32` 里的 `32`
是不是同一个数，图里看不出来**（图上是两个地方的两个数）——**本页不把它们对上。**

**grep 不到**：`REPEATED`（0 命中）、`Reference Count`（0 命中）、`cmpHig`（0 命中）；
`docu` 作为子串有 192 篇命中（**全是 `document` 之类的词**），
**但作为 `Event Group` 的那个取值查不到**——**本页不拿子串命中冒充命中**。
`MACT` / `MRPT` / `Compare Type` 能搜到（在命令页与同篇正文里），**但「GUI 的 Instruction 列
里长这样」只有图上看得见**。

**图证整体答不了的三件事，照实说：**

- **四张图没有一张出现固件命令名。** 所以主表 `L1` 列的 `?`（改 properties、sync group、
  digital capture 三格）**一格都没动**——**这不是「图够不着」，是图里本来就没有命令名。**
- **四张图没有一张画出文件内容。** `vector-setup-file` 与 `pattern-master-file` 里的东西
  **一个字都没在图上出现**，所以 `文件` 列**没有从图里拿到新证据**。
- **图是「某一次具体 setup」的截图，不是格式规范。** 「哪些字段必填、哪些组合非法」
  **图答不了**；`Port` 在（a）里是 `...`、在（b）里是 `@`，**图不解释这两种写法为什么不同**。

## 对不上的地方

**① 两套指令名，有几个逐字不同。** Pattern Editor 的 Instruction 列里写的是
`LOOP` / `LOOPEND` / `RETURN`（`02.08.04.16.02.06.10.02`），而 `SQPG` 的 `instr` 参数里对应的是
`LBGN` / `LEND` / `RSUB`（`02.06.07.02.28`）。**GUI 那份列表里查不到 `LBGN`/`LEND`/`RSUB` 三个名字。**
同理 `GENV` 在 GUI 侧是「隐式」的（`02.08.04.16.02.06.10.02` 开头）：

> 「The default instruction is `GENV` (GENerateVectors) for every vector, but the system does not display it and you do not have to enter it.」

而 L1 侧 `GENV` 必须显式写。**这一条是文档事实（两份列表都在语料里），不是我的推断。**

**反向还有一批只在 `SQPG` 侧有的名字**：`BEND`、`STVA`、`STSA`、`RSJP`、`RGOP`、
`MBGN` / `MEND` / `MJPE` / `WTER`（旧式 match loop）。**GUI 的指令列表里一个都没有。**
本页**不替它们编 GUI 侧对应物**。

**② GUI 的 pattern type 与 L1 的 label type 是两套词。** GUI 的 `New > Pattern` 对话框列的是
`Main` / `SJMP` / `SubRoutine` / `Burst` / `DSRC`，port burst 与 multiport burst 显示成
`PortBurst` / `MPBurst`，协议生成的显示成 `Protocol`（`02.08.04.16.01.02`、
`02.08.04.16.01.04`、`02.08.04.16.04.09`）。`[[pattern]]` 记的 L1 侧六个类型是
`MAIN` / `SVEC` / `BRST` / `MPBU` / `DSRC` / `SJMP`。
**`SubRoutine` 对 `SVEC`、`Burst` 对 `BRST`、`MPBurst` 对 `MPBU` 这三个配对是本页的推断**——
名字不同，语料里**没有一句把它们对起来**。
**`PortBurst` 本页没在 L1 侧找到对应物**（stage 页那六个类型里没有它）——
**「本页没找到」不等于「不存在」**，按 §2.1 的规矩只写前者。

**③ 谁创建 pattern master file，两篇说法不一样——按版本解释，不按冲突解释。**
GUI 侧（`02.08.04.16.01.15.01`）说：

> 「To create a pattern master file you use the New Pattern Setup wizard.」

L1 / 文件侧（`02.06.07.01.05`）说：

> 「The pattern master file must be created manually (or with the ASCII interface). The file itself must be located in the vectorssubdirectory of the current device.」

**照字面读像矛盾，按 §10 第 1 步查版本可解**：`02.08.04.16.01.15.01` 自己的
`Functional changes` 写着 `SmarTest 7.1.3: Pattern Master File option added to New Pattern Setup wizard.`
——**wizard 是 7.1.3 才有的**，而 `02.06.07.01.05` 那句的 `Introduced before SmarTest 6.3.2`。
两条并列记在这里，**本页不替语料选一个当正确答案**。

**④ `02.08.04.16.01.05` 有一处语料错字，本页照实记下、没替它改：**

> 「The naming syntax is `<MuliportBurstName>@<Port>.`」

**`MuliportBurstName` 应为 `MultiportBurstName`**（同一篇的正文里写的是
`the specified multiport burst`，拼对了）。引文里原样保留（§11.2）。

**⑤ 同一篇文档里的拼写不一致，一处：** `02.06.07.01.05` 上面写 `the vectors subdirectory of your current device`（有空格），
下面写 `vectorssubdirectory`（无空格，见 ③ 的引文）。**两个写法都在同一篇里，本页照录。**

**⑥ `02.08.04.16.02.06.10.02` 的 `CTIM` 那格拼错了参数名，照录：**

> 「CTIM <tming_set_number>」

**`tming` 应为 `timing`**——同一张表里 `CLEV` 那格写的是 `level_set_number`，拼对了。

**⑦ `02.08.04.16.02.06.10.01` 有一处括号没闭合，照录：**

> 「Double-click MACT and type the number of loops (the maximum number of unsuccessful repetitions, for example, 32.」

**左括号开了没有闭。** 这一句还说明 GUI 侧的 `MACT` 第一个参数的含义与 `SQPG` 的 `param_1` 是同一个
（「the maximum number of unsuccessful repetitions」对 `param_1 specifies the number of loops after which the whole test fails`，
`02.06.07.02.28`）——**这一条对应由两句原文并置得出，是本页的推断。**

**⑧ `02.09.01.09.02` 有一处重复词，照录：**

> 「Use dm_pattern_master_file only to save the updated patterns in in a new pattern master file. Using dm_pattern_master_file SmarTest does not save unchanged patterns.」

**`in in` 重复了。**

**⑨ L3 整列只有两格是真的，这是结论不是缺口。** `pattern` 与 `[[pin]]` 在这一列上**不一样**：
pin 的定义动作发生在 setup 期，外部进程插不进来，所以那一页整列是 `—`；
**pattern 有两个外部进程能碰的点**——`TestsuiteProxy` 的 `getSequencerLabel()` / `setSequencerLabel()`
（外部 C++ 客户端读写 test suite 的 sequencer label），以及 TPI `DataManager` 的文件标识。
两格的原文分别是：

> 「This function sets the sequencer label for the test suite.」

> 「Use dm_vector also to save a pattern master file.」

**但这两个点都不能编辑 label 的内容**——`setSequencerLabel` 只设名字，`DataManager` 只搬文件。
**「用 L3 写一个 pattern」在本页的证据里不存在**，所以其余各行 L3 是 `—`。

**⑩ L2 只有五行有值，这个分布本身是一条信息。** L2 是「在 test method 里调用」的动作，
而 pattern 这一段绝大多数动作是**定义**。有值的五行集中在
**「定义完了以后在测试里要用」的地方**：primary wavetable、protocol pattern、digital capture、
sync group、start label（两行——`PRIMARY_STATUS` 与两篇 L3 原文各占一行）。
**和 `mapping-pin` 那一页的分布是同一个形状。**

**⑪ start label 有一个 GUI 位置，但不在 Pattern Tools 里。** `02.07.04.01.167` 的优先级表里
出现「`Start label specified on Testsuite dialog window`」——**test suite 对话框能指定 start label**。
但那是 `[[testmethod]]` / `[[testflow]]` 侧的 GUI，**不是 Pattern Explorer**，所以主表
「执行一个 pattern」那一行的 GUI 格照旧是 `?`。**这一条值得后续单独查一次。**

**⑫ Pattern Explorer 显示的是「当前 primary pattern」，但那是显示不是指定。**
`02.08.04.16.01` 的图标表里有「`The current primary pattern.`」，
`02.08.04.16.02` 说「`Only the current primary pattern (start label) can be viewed in expanded mode.`」
——**GUI 能看见哪个 label 是 primary，但这两句都没说 GUI 能改它**，所以本页不据此填 GUI 格。

**⑬ 图能读，本页读了四张——原先这里写的「图在语料树之外」是错的。**（**2026-09-20 更正**）
`../../../../raw/x.png` 往上四层正好是 `tdc-html/`，**图就在 `tdc-html/raw/` 里，读得出来**
（`schema.md` §11.4）。**原先这一段的另一半说对了**：「哪个字段对应哪条参数」这个粒度的问题
**确实只有图能答**——**本页 2026-09-20 就把那四张开了**：

| 图 | 出处 | 它答了什么 |
|---|---|---|
| `99506.png` | `02.08.04.16_Pattern_Tools` | **Pattern Explorer 的列头**：`Name` / `Port` / **`Sync Group`** / `Type` / `WaveTable` / `Memory` / `State` / `Location`，取值里有 `Main`、`eeprom`、`SM`、`UpdateDate`、`../vectors/` |
| `99692.png` | `02.08.04.16.01.02_Creating_a_pattern` | **New Pattern 对话框六格**：`Pattern Name` / `Pattern Type` / `Port` / `Memory Type` / `Wavetable` / `Folder` |
| `112686.png` | `02.08.04.16.02.06.10_…sequencer_instructions…` | **Instruction 列 + 插入指令的列表框**（`RPTV` / `LOOP` / `LOOPEND` / `JSUB` / …） |
| `122707.png` | `02.08.04.16.02.06.10.01_Inserting_counted_match_loops` | **`MACT 32` / `MRPT 5` / `REPEATED` 在 Instruction 列里长什么样** + Properties 面板（`Event Name` / `Reference Count` / `Compare Type`） |

**这四张解决掉的格子**（表里已标「（图证）」）：建 pattern 那行的 GUI 格与 `文件` 格、
改 properties 那行的 GUI 格、Instruction 列那行的 GUI 格、counted match loop 那行的 GUI 格、
内存类型那行的 GUI 格、sync group 那行的 GUI 格。**逐张的边界写在证据节 ④**，
这里只记三件必须说清的事：

- **「（图证）」不是「文档明说」的同义词。** 图回答的是「这个窗口长什么样」，
  **本页据此只改 GUI 格的字面**，**L1 / L2 / L3 格一格都没动**——
  **四张图里没有一个命令名、没有一个 API 名。**
- **`SQLB` 那一格的（推断）本页没摘。** （b）那张图只画出对话框，**没有画出这个动作落到哪条命令**
  ——按 §2.5「看起来像不算证据」，**（推断）留在原处**。
- **内存类型那一格的名称，图与表对不齐，本页照实记、没替谁改。**
  Explorer 的列头是 `Memory`（（a）），New Pattern 对话框的字段是 `Memory Type`（（b）），
  而本页表里原来写的是 `[[pattern-explorer]]（`Memory Type`）`。
  `02.08.04.16.01.14` 正文写的是 `Change the memory`，`02.08.04.16.01.02` 写的是 `Memory Type`
  ——**两个词在语料里各自都有出处，本页两个都留着**，只在表里标出哪一个出自哪个窗口。

**图证答不了的三件事，照实说：**

- **四张图没有一张画出文件内容。** `vector-setup-file` 与 `pattern-master-file` 的正文
  **一个字都没在图上出现**——所以是「图里没有」，不是「图够不着」。
- **四张图没有一张出现固件命令名。** 主表 `L1` 列那三个 `?` 与两个（推断）**全部留在原处**。
- **图是「某一次具体 setup」的截图，不是格式规范。** 「哪些字段必填、哪些组合非法」图答不了；
  `Port` 在（a）里是 `...`、在（b）里是 `@`，**图不解释这两种写法为什么不同**，**本页也不猜**。

## 出处

`sources:` 四十篇，**全部真读过**（例外：`02.08.04.16.02.06.17` 只读了含 L2 链接的那一段）。
分四类：

- **GUI / 文件侧**（`02.08.04.16` 一族，31 篇）——主表 GUI 与文件两列的来源。
- **L1 侧**（4 篇）——`02.06.07.01.01.02`（`SPRM` 与 primary wavetable 的关系）、
  `02.06.07.01.04.01`（内存类型与 `SQLA`）、`02.06.07.01.05`（pattern master file 格式）、
  `02.06.07.02.28`（`SQPG` 全表）。
- **L2 侧**（2 篇）——`02.07.04.01.167`（`PRIMARY_STATUS`）、`02.07.13.08.17`（SmartRDI sync group）。
- **L3 侧**（3 篇）——`02.09.01.09.02`（`DataManager`）、`02.09.01.14.02.01.09`、`.29`。

**引文相对路径**（与 `sources:` 同名，**表里的分类号对的是这些完整路径**）：

| 分类号 | raw 相对路径 |
|---|---|
| `02.06.07.01.01.02` | `02_System_reference/02.06_Command_Reference/02.06.07.01.01.02_The_vectors.md` |
| `02.06.07.01.04.01` | `02_System_reference/02.06_Command_Reference/02.06.07.01.04.01_Selecting_the_memory_type.md` |
| `02.06.07.01.05` | `02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md` |
| `02.06.07.02.27` | `02_System_reference/02.06_Command_Reference/02.06.07.02.27_SQLB__SQLB__-__SeQuencer_LaBel_definition.md` |
| `02.06.07.02.28` | `02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md` |
| `02.06.02.02.258` | `02_System_reference/02.06_Command_Reference/02.06.02.02.258_TMUD__Tester_Memory_Utilization_set_Default_values.md` |
| `02.06.02.02.318` | `02_System_reference/02.06_Command_Reference/02.06.02.02.318_VCAT__VCAT__-__VeCtor_ATtachment.md` |
| `02.07.04.01.35` | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.35_DIGITAL_CAPTURE_TEST.md` |
| `02.07.04.01.167` | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.md` |
| `02.07.04.01.256` | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.256_TRANSACTION_SEQUENCE.md` |
| `02.07.04.01.269` | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.269_VECTOR.md` |
| `02.07.13.08.17` | `02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17_Sync_group_support_with_SmartRDI.md` |
| `02.08.04.16.01.02` | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.02_Creating_a_pattern.md` |
| `02.08.04.16.01.05` | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.05_Creating_and_assigning_a_port_burst.md` |
| `02.08.04.16.01.15.01` | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.01_Creating_a_pattern_master_file.md` |
| `02.08.04.16.02.06.10.01` | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10.01_Inserting_counted_match_loops.md` |
| `02.08.04.16.02.06.10.02` | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10.02_Sequencer_instructions.md` |
| `02.08.04.16.04.01` | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.01_Definitions__Vector__Pattern__Burst__etc.md` |
| `02.08.04.16.04.05.01` | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05.01_Function_of_the_base_wavetable.md` |
| `02.09.01.09.02` | `02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.md` |

**本页没做的**：

- **`02.06.07.02.27_SQLB`、`02.06.07.02.29_SQSL`、`02.06.07.02.30_SQST` 三条命令原文一篇没读。**
  主表里 `SQLB` / `SQSL` / `SQST` 三个名字转自 `[[pattern]]` 的「涉及对象」节
  （那页建页时读的），**本页没有回到命令原文复核**。`SQLB` 那一格标了 `（推断）`就是这个原因。
- **只读了 2 篇 L2 原文**：`PRIMARY_STATUS` 与 `Sync_group_support_with_SmartRDI`。
  主表里的 `DIGITAL_CAPTURE_TEST` / `VECTOR` / `TRANSACTION_SEQUENCE` / `SYNCHRONIZED_TEST`
  **只见到链接，正文一个字没读**，所以那两行的 L2 格只写了名字与分类号。
- **`02.07.11`（Protocol Aware ATE）整章没读。** 主表 protocol 那两行的 L2 格是从链接里取的。
- **看了四张图（2026-09-20 加）。** 就是 `99506.png`、`99692.png`、`112686.png`、`122707.png`
  （路径与结论见「证据」④ 与「对不上的地方」⑬）。**四张都整张看完**，
  图上读到的字**逐条回 9,398 篇 raw md 里查过 grep 命中**——本页凡写「grep 不到」的都是实测 0 命中。
  **本页 sources 里带图的文档共 28 篇 / 114 张，其余一百一十张没看**
  （大半是 `02.08.04.16.01` / `.16.02` 里的**单个图标截图**，如 `119794` / `128874` / `99926`）。
  **原先本页在「对不上的地方」⑬ 里写着图「在语料树之外」——那是错的**，见 ⑬ 的更正。
- **没有实跑。** 没有在机台上开过任何 pattern 工具、没有生成过 pattern master file、
  没有用 `extract/wiki-plan.csv` 之外的任何数据校对过本表。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pattern.md`。
  后者是**待办**：pattern 那页目前不知道本页存在。

**本页 `layer: n/a` 的理由**：§6 要求 mapping 页必填 `layer`，而本页**本身不属于任何一层接口**
（它是对照表，不是接口）——`n/a` 是这个六值枚举里为这种情况准备的值。

`verified: doc-only`
