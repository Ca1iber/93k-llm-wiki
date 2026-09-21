---
type: mapping
title: 建工程 / Device 配置的三层对照
layer: n/a
stage: project
tags: [mapping, project, gui, firmware-command, test-method-api, technology-file, device-directory, device-license-file, stpm]
related: [project, pin, new-device-wizard, change-device-wizard, technology-file-for-a-device, device-directory, device-technology-directory, workspace, project-explorer-view, test-program-explorer, setup-perspective, org-file, model-file, device-license-file, dscp, dtcp, psfc, pqfc, prlt, hidden-upload, uptd, global-section, stpm, stpm-control-file, stpm-merge-rules-file, tpt-generate-device-dir, tpt-import-from-device, setup-management-tool, testflow-analyzer-tool, switch-version-command-line-tool, level-master-file, timing-master-file, testflow-master-file]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.03_Technology_file_for_a_device.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.03_Technology_file_for_a_device.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.01_Creating_a_new_device.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.03_Editing_technology_data.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01_Creating_a_new_device.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15_New_Device_wizard.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03_Change_Device_wizard.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.03_Device_Directories.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.01_Device_Technology_Directory.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.02.02_Specifying_the_Device_Path.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.93_DTCP__DTCP__-__Define_Technology_Control_Parameters.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.306_UPTD__UPTD__-__UP_To_Date.md
  - 02_System_reference/02.06_Command_Reference/02.06.01.02_Firmware_view.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.125_LEV_TRANSFER_TASK.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.270_VEC_TRANSFER_TASK.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.190.09_Result_areas_for_error_map_data.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10.04.05_Hidden_upload.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04_Setup_Management_Tool.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.02_Using_the_Setup_Management_Tool_from_the_Test_Program_Explorer.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.03_Using_the_Setup_Management_Tool_from_the_Command_Line.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.14_tpt_generate_template.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.01.02.03_Test_program_template.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07_The_Testflow_Analyzer_Tool__TAT.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07.02_Optimizing_the_technology_file.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.03.02_Switch_version_command_line_tool.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.12_ChangeDevice.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.16_GetTechPath.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# 建工程 / Device 配置的三层对照

## 这张表在说什么

建工程这一段，语料把同一件事写成三套：New Device / Change Device 向导里的字段（GUI）、
device 根目录下的 `.technology` 文件（file）、固件命令（L1）。
**这三套是不是同一个东西的三种写法——语料自己回答了，而且是明说的。
它就写在 `.technology` 参数表的表头上。**

`01.01.07.02.01.02_Technology_file_for_a_device.md` 的 `## Parameters of the .technology file` 一节，
先给列定义，再给表：

> 「The table below describes the parameters in detail. The following values are defined:」

> 「- Change Device wizard: The corresponding field of the Edit Device page.」

> 「- DSCP command: The corresponding parameter of command DSCP in the Command Reference manual」

**这三行是本页的地基。** 它的意思是：参数表里的**每一个参数**，
都有一格写它在向导里的哪个字段、一格写它对应 DSCP 的哪个参数——
**不是「有关」，是逐行给出**。所以本页的主表**不是我归纳出来的**，
是**语料自己按行钉的**，本页只把它换一个维度（按「目的」而不是按参数）排出来。

（引文说明：上面第二、三行原文里各带一个语料内部链接，
`[Edit Device page](<01.01.10.03.03_Editing_technology_data.md>)` 与
`[DSCP](<…02.06.02.02.90_DSCP…>)`、`[Command Reference](<…02.06_Command_Reference.md>)`。
**本页按 §11.1 的规范化第 ② 条剥掉了链接标记**，引号里是剥完的字。）

GUI 那一侧说同一件事，`01.01.10.03.03_Editing_technology_data.md`：

> 「All values entered in the Edit Device page are written to the .technology file of the selected device. Refer to rows "Change Device wizard" of table Parameters of the .technology file in Technology file for a device for the relationship between the fields of the Edit Device page and the .technology file.」

**这句把「哪一列是权威」说死了**：GUI 字段与文件参数的对应，
**就是参数表里叫 `Change Device wizard` 的那一列**。
两篇文档互相引用，指的都是同一张表——**这条链是闭环的，不是单边声明**。

固件那一侧，`02.06.02.02.90_DSCP…` 自己交代了它与文件的关系：

> 「DSCP is called every time you switch to another device. You can specify the parameter values of this call in the technology file (.technology), which is located in the main directory of every device.」

还有一句是**反向**的（`01.01.07.02.01.02` 的 `## Changing the .technolog file` 一节）：

> 「Changes made in this window are saved in the .technology file and communicated immediately to the firmware using the DSCP (Define System Control Parameter) and other firmware commands.」

**注意这句里的 `and other firmware commands`——它不是客套。**
本页下面会看到（「对不上的地方」⑧）：`extended_dram_factor` 和 `testpoints`
**都不走 DSCP，走的是 DTCP**。所以「L1 列 = DSCP 列」这个等式**不成立**，
L1 列必须把 DTCP 也算进来。

**「三层」这个词在本页要放宽理解**：§2.5 给了五列（GUI / 文件 / L1 / L2 / L3），
而 project 这一段**只有三列被语料逐行钉住**（GUI / 文件 / L1），
**L2 只在两行上有名字，L3 那几行则完全不在 `.technology` 表里**（靠的是阶段页列的几条命令行工具）——
下面「证据」与「对不上的地方」逐条说明。

## 对照表

**读法**：一格填了名字 = 有证据（证据是什么见下一节）；`?` = 语料没说，**本页不猜**；
`—` = 这一层不存在这个对应物（不是「没找到」）。

**主表的 GUI 与 L1 两列，口径完全照抄 `.technology` 参数表的两列**
——`Change Device wizard` 列的字段名、`DSCP command` 列的参数名。
所以这两列的每一格**都有出处**，不是本页排的。

### 第一组：`.technology` 参数表逐行钉住的（GUI 字段 ↔ 文件参数 ↔ DSCP 参数）

| 目的 | GUI（`Change Device wizard` 列） | 文件（`.technology` 参数） | L1（`DSCP command` 列 + 其它） | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 定 device cycle 上限 | `Device cycles` | `device_cycles` | [[dscp]] 的 `device_cycle` | — | — |
| 定 waveform set 上限 | `Waveform sets` | `waveform_sets` | DSCP 的 `waveform_set` | — | — |
| 定 timing set 上限 | `Timing sets` | `timing_sets` | DSCP 的 `timing_set` | — | — |
| 定 level set 上限 | `Level sets` | `level_sets` | DSCP 的 `level_set` | — | — |
| 定 DPS set 上限 | `DPS sets` | `dps_sets` | DSCP 的 `dps_set` | — | — |
| 定 device cycle set 上限（selective digital capture 用） | `PDC sets` | `pdc_sets` | DSCP 的 `devicecycle_set` | — | — |
| 定 PPMU measurement set 上限 | `M sets` | `m_sets` | DSCP 的 `pmu_set`；原文另点 `MSET`、`MEAS`、`PMUR`、[[psfc]]、[[pqfc]]、[[prlt]]、`GNOS?` | — | — |
| 定 period resolution precision | （向导里没有这个字段） | `period_res_precision` | DSCP 的 `period_res_prec` | — | — |
| 定 testpoints 的内存上限 | `Testpoints` | `testpoints` | [[dtcp]] + `*RST` | — | — |
| 定向量区与其它区的内存比 | （向导里是 `n/a`） | `extended_dram_factor` | DTCP 的 `key` = `extended_dram_factor`，配 `*RST` | — | — |
| 定 error map 结果区大小 | `Result Area Size` | `digital_default_result_area_size` | `DMAS? MFRE`（**查询**，不是设定值） | `Result areas for error map data`（`02.07.04.01.190.09`）、[[hidden-upload]] | — |
| 定 Fast Transfer Buffer | `Fast Transfer Buffer Size` | `fast_transfer_buffer_size` | —（参数表这一行写 `n/a`） | `VEC_TRANSFER_TASK`、`LEV_TRANSFER_TASK`、`PPMU_SETTING` | — |
| 定每个 pogo block 的 utility line 数 | `Utility block size` | `utility_lines_per_pogoblock` | —（`n/a`） | `?` | — |
| 指定 device license file | `Licensing file` | `.technology` 的 `licensing_file` → [[device-license-file]] | —（`n/a`） | — | [[testflow-analyzer-tool]]（**生成** `.licenses`，不是指定） |
| 预初始化向量内存 | `Preinitialize vector memory to value` | `init_vectors_with_value` | —（`n/a`） | — | — |
| 选技术源目录（进而定 device 子目录结构与默认 level） | `Device technology` | `/dev_tech/cmos 或 /dev_tech/ecl` | —（`n/a`） | `?` | — |
| 一组 device 级开关（`himem`、`pulldown_in_level_set_0`、`pulldown_not_configured_pins`、`pretty_printed_analog`、`optimized_multiport_memory_allocation`、`fast_bi_directional_capability`、`mset_program_memory_preallocation`、`check_compatibility_with_smart_scale`、`check_exa_scale_seq_restrictions`、`enforce_smart_scale_dc_sync_compatibility`） | 向导里的一组复选框——**标签是释义，不是这些参数名**（上一版写「同名」是错的；**① 档依据是参数表那一列本身**，**④ 图证**另给出一个与它不一致的说法，见「对不上的地方」⑬） | 同名参数 | —（这 10 条全部写 `n/a`） | `?` | — |

**这一组十七行里没有一行是本页排的**：GUI 格与 L1 格的字面来自参数表的
`Change Device wizard` / `DSCP command` 两列，文件格来自参数名那一列。
**唯一的加工是「目的」那一列**——那是本页给每行起的标题，为了让人能按事找**（推断）**。

**这十七行里有一处例外，得说清**：最后一行（那一组 device 级开关）在参数表里是**十行**
（十个参数各占一行，GUI 格各写各的释义），本页**把它们合成了一行**——
所以那一行的 GUI 格**不是任何一格的逐字**，而是本页对这一组的概括（**推断**）。
**2026-09-20 那一格的措辞改过一次**（上一版写「同名复选框」），理由与图证见「对不上的地方」⑬。

### 第二组：建 / 激活 device 与目录本身（这一组不在 `.technology` 表里）

| 目的 | GUI | 文件 | L1 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 建一个 device 目录并链进 workspace | [[new-device-wizard]] | [[device-directory]] | `?` | `?` | [[tpt-generate-device-dir]] |
| 激活一个已有的 device | [[change-device-wizard]] | [[technology-file-for-a-device]] | [[dscp]]（每次切 device 都被调） | `?` | `?` |
| 在 GUI 里看 device 目录 / setup 结构 | [[project-explorer-view]]、[[test-program-explorer]]、[[setup-perspective]] | [[device-directory]] | `?` | — | — |
| 判断硬件里的 setup 数据是不是比文件新 | [[test-program-explorer]]（`UPTD` 那篇的 `## Application` 只点名它） | — | [[uptd]] | — | — |
| 定 device path 的根 | `?` | [[org-file]] | — | — | `?` |
| 定系统资源底账与 licensing 底账 | `?` | [[model-file]] | `?` | `?` | — |
| 提供 technology 模板（cmos / ecl）目录结构 | `?` | [[device-technology-directory]] | — | — | — |

### 第三组：`setup` 管理与几条命令行通道（阶段页把这一组归在 L3）

| 目的 | GUI | 文件 | L1 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| setup 组件的拆分与合并（master file） | [[setup-management-tool]]（**从 [[test-program-explorer]] 走**） | `.mfh` master file + 子文件（分量见 [[level-master-file]]、[[timing-master-file]]、[[testflow-master-file]]） | — | — | `smartest_mfh`（`assemble` / `split` / `assemble_all` / `split_all` / `create`）——**与 GUI 格是同一个工具**；调用格式 `smartest_mfh <操作> <参数>`（**④ 图证**，见「对不上的地方」⑬） |
| 从 test program template 生成 device 目录 | `?` | [[stpm-control-file]]、[[stpm-merge-rules-file]] | — | — | [[tpt-generate-device-dir]] |
| 反向：从已有 device 目录导出 template | `?` | 同上 | — | — | [[tpt-import-from-device]] |
| 统计当前 device 实际用掉多少 set | `?` | — | — | — | [[testflow-analyzer-tool]] |
| 由 TAT 的数回头改 `.technology`（闭环） | [[change-device-wizard]] | [[technology-file-for-a-device]] | [[dscp]] | — | [[testflow-analyzer-tool]] |
| 切 SmarTest 版本 | `?` | — | — | — | [[switch-version-command-line-tool]] |

**第三组第二、三行有一个共同的落点**：两条命令作用的是 **device 目录**这一层
（`tpt_generate_device_dir` 建出来、`tpt_import_from_device` 读出来），
它们**不是** `.technology` 的读写者——见「对不上的地方」⑩。

**表里没有的**：

- `02.06.02.02.306_UPTD…` 是**本页找到的唯一一条真正的 L1 → GUI 边**（`## Application` 一节
  只写 [[test-program-explorer]] 一篇；`Test_Program_Explorer` 收到 3 条，来自这篇的三个投放）。
  它的正文讲的是「硬件里的数据是不是比文件新」，**与建工程不是同一件事**——
  本页**没有把它塞进别的行凑数**，而是为它单开了一行（第二组第 4 行），
  让读者自己判断要不要用。
- `02.06.02.02.79_DMAS…`、`02.06.02.02.137_GNOS…`、`02.06.02.02.311_UTOT…`、
  `02.06.02.02.08_BCMT…` 等**从 L1 那一侧链回 `.technology` 那篇**（见证据 ② 的反方向那张表），
  但**参数表给这些参数（`himem` 等）的 DSCP 格全是 `n/a`**——
  **「那边链过来了」不等于「这条命令设这个参数」**（§2.5：不许猜）。
  所以它们只出现在证据节，**不进主表**。

## 证据：哪几格是钉死的，哪几格只是「那边链过来了」

**证据分四档，本页不把它们混成一种。**
（**2026-09-20 归一**：本页上一版把「链接」拆成了正、反两节，于是编号比 `schema.md` §2.5 多一位，
**图证那一节没有号可挂**。现在按 §2.5 / §11.4 的四档编号：① 语料明说 / ② 链接（含反方向）/
③ 只有一侧 / ④ 图证。**拆开的那两节仍然分开写**——它们是同一批边的两个方向，读法不同。）

**① 语料明说对应（最硬）** —— 就是「这张表在说什么」里那两处声明：
参数表的 `Change Device wizard` / `DSCP command` 两行列定义，
加上 `01.01.10.03.03` 那句 `Refer to rows "Change Device wizard" …`。
**它覆盖主表第一组的全部 17 行、51 格**（17 行 × GUI/文件/L1 三格）。
这一档是**逐行的**，不是「这一族大致对应」——**这是它比 pin 那页更硬的地方**。

**② 文档之间有链接（次硬，逐条可查）** —— 这些是语料里**实际存在的跨层链接**，
取自 `extract/edges.jsonl`：

| 源文档（GUI / 文件侧） | 链到 | 条数 |
|---|---|---|
| `01.01.07.02.01.02_Technology_file_for_a_device.md` | L1 侧：[[dscp]]（2 条）、[[dtcp]]（2 条）、`*RST`、`DMAS`、`MSET`（2 条）、`MEAS`、`PMUR`、[[psfc]]、[[pqfc]]、[[prlt]]、`GNOS?`、`02.06_Command_Reference`（2 条） | 16 |
| 同上 | L2 侧：`VEC_TRANSFER_TASK`、`LEV_TRANSFER_TASK`、`PPMU_SETTING`、`Result areas for error map data`（2 条）、[[hidden-upload]] | 6 |
| `02.06.02.02.306_UPTD…`（**反方向**：L1 → GUI） | [[test-program-explorer]] | 1 |
| `01.01.10.03.01_Creating_a_new_device.md`（GUI） | [[technology-file-for-a-device]]（其中一条原文带行锚点 `#_49363__row_init_vectors_with_value`） | 3 |
| `02.09.02.03.16_tpt_generate_device_dir.md`（L3） | [[stpm-control-file]]、[[tpt-import-from-device]]、`Preprocessing and postprocessing scripts`（2 条） | 4 |
| `02.09.02.03.15_tpt_import_from_device.md`（L3） | [[stpm-control-file]]、[[tpt-generate-device-dir]]、预处理/后处理脚本（2 条） | 4 |
| `02.09.02.03.14_tpt_generate_template.md`（L3） | **`.technology` 那篇**（同一行里还链了 testflow file 与 pin configuration file，两篇都在 `02.08`，不算跨层） | 1 |
| `02.04.05.07_The_Testflow_Analyzer_Tool__TAT.md`（L3） | **`.technology` 那篇** | 1 |

**链接证的强度要说清**：一条链接**只证明「那篇文档认为读者该去看这一篇」**，
**不证明两个东西等价**——可能是「见也」，也可能是「区别在这里」，也可能是「前提」。
本页只在主表的**同一行**里用它，**不跨行搬**。
上表里 16 + 6 = 22 条那一行，**只用在第一组 L1/L2 两列里语料点名过的那几行**。

**②（续）反方向：谁链回了 `.technology` 那篇。** `extract/edges.jsonl` 里指向
`01.01.07.02.01.02_Technology_file_for_a_device.md`（含它的行锚点）的边有 **224 条 / 59 个不同来源**，
其中来自 `02.06`（L1）/`02.07`（L2）/`02.04`（文件）/`02.09`（L3）的是这些：

| 方向 | 来源 | 条数 |
|---|---|---|
| L1 → 文件 | `02.06.02.02.90_DSCP`、`02.06.03.02.13_DSCP`、`02.06.04.02.01_DSCP`、`02.06.06.02.10_DSCP`（**同一篇的四个投放**） | 2 + 2 + 2 + 2 |
| L1 → 文件 | `02.06.02.02.93_DTCP` | 4 |
| L1 → 文件 | `02.06.02.02.79_DMAS`、`02.06.07.02.13_DMAS` | 1 + 1 |
| L1 → 文件 | `02.06.02.02.137_GNOS`、`02.06.10.02.06_GNOS` | 1 + 1 |
| L1 → 文件 | `02.06.02.02.311_UTOT`、`02.06.12.02.11_UTOT` | 1 + 1 |
| L1 → 文件 | `02.06.02.02.08_BCMT`、`02.06.07.02.03_BCMT` | 1 + 1 |
| L1 → 文件 | `02.06.05.01.05.06_Pull-down_function`、`02.06.07.01.08.04.03.01_Counted_match_loops` | 1 + 2 |
| L2 → 文件 | `02.07.04.01.270_VEC_TRANSFER_TASK` | 3 |
| L2 → 文件 | `02.07.04.01.125_LEV_TRANSFER_TASK` | 1 |
| L2 → 文件 | `02.07.04.01.160_PPMU_SETTING` | 2 |
| 文件 → 文件 | `02.04.01.03.02.01_GLOBAL_section`、`02.04.01_The_model_file`、`02.04.05.07.02_Optimizing_the_technology_file`、`02.04.05.07_The_Testflow_Analyzer_Tool__TAT` | 4 + 1 + 2 + 1 |
| L3 → 文件 | `02.09.02.01.02.03_Test_program_template`、`02.09.02.03.14_tpt_generate_template` | 1 + 1 |

**这张表里最要紧的是「L2 → 文件」那三行**。它们说明 L2 列并不全是空的：
`VEC_TRANSFER_TASK` / `LEV_TRANSFER_TASK` / `PPMU_SETTING` 三篇**自己链到
`fast_transfer_buffer_size` 那一行的锚点**，并在正文里说它们「用」这个 buffer。
**这是双向的**（`.technology` 那篇也链回它们），是本页 L2 列唯一硬的两格。
原文（`fast_transfer_buffer_size` 那一段，逐字）：

> 「Defines the buffer for modification of」

> 「- vector data with the VEC_TRANSFER_TASK API,」

> 「- level specs with the LEV_TRANSFER_TASK API, and」

> 「- PPMU settings with the PPMU_SETTING API.」

> 「Note The VEC_TRANSFER_TASK and LEV_TRANSFER_TASK APIs can be used only with SmartScale test head cards. |」

**末一条末尾那个 `|` 是原文里的表格单元格边界**，**本页没有替它删掉**——
§11.1 只允许剥链接标记与折叠空白，**表格符不在那张清单里**。

**③ 只有一侧有名字的格子** —— 主表里的 `?` 与 `—`：

- L1 列写 `—` 的行（第一组里有六行：`fast_transfer_buffer_size`、`utility_lines_per_pogoblock`、
  `licensing_file`、`init_vectors_with_value`、`/dev_tech/cmos 或 /dev_tech/ecl`、那一组 device 级开关）：
  **`—` 不是「本页没找到」，是参数表那一行明写 `n/a`**——
  「DSCP 没有这个参数」是**文档事实**。这一点与 pin 那页不同：
  pin 的 `—` 是结构判断，本页的 `—` 大多**有字面依据**。
- **上面那条有一个例外，是 `digital_default_result_area_size` 那一行**：
  它的 `DSCP command` 格同样写 `n/a`，但**同一行的 `Note` 里点名了一条 L1 `DMAS? MFRE`**
  （原文：`You can use the [DMAS? MFRE](<…>) query to determine the available memory.`）。
  本页把这条填进 L1 格并注明是**查询**——**这是「语料在这一行点名了」的口径，不是「DSCP 列」的口径**。
  两种口径在同一张表里并存，所以 L1 格写 `—` 时读作「DSCP 没有」，写名字时要看它是不是 DSCP。
- L2 列写 `—` 的行：**本页的理由是阶段页已核过的一条文档事实**——
  「`02.07_Test_Method_Reference` 里没有任何一篇是把 C++ Test Method API 用于建工程 / 建 device 目录的」。
  即**本阶段在 L2 层没有动作**，L2 格填的是「**谁在消费这个上限**」，
  语料只对 `fast_transfer_buffer_size` 与 `digital_default_result_area_size` 两个参数点名了消费者。
- L3 列写 `—` 的行：理由同上一档，且**有一条正面证据**——
  TAT 那篇的正文里明写它**不改** `.technology`：

> 「Note TAT does not change and optimize the technology file, see Optimizing the technology file, but provides the number of used sets:」

  **`does not change and optimize` 是语料自己说的**，不是本页的推断。

**链接证的强度要说清（第二遍，因为这一档最容易被读多）**：
`02.06.02.02.79_DMAS` 链回 `.technology` 那篇，是**因为 `SMEXT` 内存类型「used only when himem is enabled」**；
`02.06.02.02.08_BCMT` 链回去，是因为 `HIMEM` 参数要配 `himem:on`。
**两条都只是「读者该去看那一篇」，参数表的 DSCP 格对 `himem` 写的是 `n/a`。**
所以本页**不把 `DMAS` / `BCMT` 填进 `himem` 那一行的 L1 格**。

**④ 图证（2026-09-20 加，本页用到了）** —— 从 raw 自带的截图里读出来的。
本页 `sources:` 32 篇里**共引 26 处图**（**17 张不同的 `.png`** + **2 张 `.svg`**，另有三张各被引两次），**都看了**；
逐张的结论在「对不上的地方」⑬。这一档**比①②③都硬**（图是文档自带的，不是我的推断），
**但它不可检索**——**理由与写法见 `schema.md` §11.4**；要点是：
**必须写清是哪张图，并说明图里的字 grep 不到。**
本页**最要紧的一张是 `354784.png`**：它是 Edit Device 页的整屏截图，
**把「GUI 的哪一个控件 ↔ 文件的哪一个参数」在第一组 17 行里钉死了 13 行**——
**这个粒度的问题，文本只能靠参数表的两个列名回答，图回答得更好。**

**一个反向的例外要说清：那两张 `.svg` 不是 ④ 档。** `46345.svg` / `46346.svg` 是**矢量图**，
**它们里面的标签就是文件里的文字**（`<DUT_PATH>`、`<INSTALLED_DUT_PATH>`、`testflow`、
`dataset`、`wafertype`、`testprogram` …）——**grep 得到，所以它们属于②档的取材，不属于④档**。
**「图」这个词在本节只指读不出来的位图。**

> **这一档是被一个假说法挡了很久才补上的。** 本页原先写着「raw 里的图片路径向上爬四层
> （`../../../../raw/`），**在语料树之外**，所以**本页没有任何来自图的结论**」——
> **路径是对的、图是读得出来的**（§11.4）。
> **一个不成立的理由，会把一整档证据永久关在门外。**

## 对不上的地方

**① 本页的 `—` 比 pin 那页多，含义也不同，别混着读。**
pin 的 `—`（L3 整列）是**结构判断**；本页第一组的 L1 列 `—` 是**参数表的字面 `n/a`**，
第二、三组 L3 列的 `—` 才是结构判断，而且**有 TAT 那句正面证据**。
**同一个符号在两张页里承载两种依据**——引用本页时请连着依据一起引。

**② `.technology` 那篇的节标题有一个语料错字，本页照实记下、没替它改**：

> 「## Changing the .technolog file」

**`technolog` 应为 `technology`**（少了 `y`）。本页把它原样留在引文里（§11.2：引文不许替语料修字），
并在上面「这张表在说什么」里**按坏掉的拼法**写它，以便读者拿这个字去 raw 里搜得到。

**③ 同一篇文档有三处投放，三份的跨层出链完全相同。**
`.technology` 那篇在 raw 里有**三份**：

- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md`（30,403 字节）
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.03_Technology_file_for_a_device.md`（33,278 字节）
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.03_Technology_file_for_a_device.md`（33,278 字节）

三份**正文不相同**（字节数就不一样），但它们**各自都有 22 条指向 `02.06`/`02.07` 的出链，
且目标集合一模一样（17 个不同目标）**。所以本页的证据**不因为读哪一份而变**。
**但计数会变**：`edges.jsonl` 里这三份是三条独立的边源。

**④ 同一篇文档还有另两份「兄弟投放」，它们的内部链接指自己那一支。**
`02.08.04.15.02_Editing_technology_data.md` 与 `02.08.04.03.02_Editing_technology_data.md`
是 `01.01.10.03.03_Editing_technology_data.md` 的另两个投放（5,102 / 5,102 vs 5,042 字节），
`02.08.04.15.01_Creating_a_new_device.md` 与 `02.08.04.03.01_…Change_Device_button.md` 同理。
**它们的内容差异主要是内部链接的目标变了**（指自己那一支的兄弟页）。
**§10 的第 0 步（先查重复投放）在本阶段必须做**，否则会把一篇数的链接数成一族。

**⑤ DSCP 命令页在 raw 里有五个投放，其中四个 body 完全相同。**
`02.06.02.02.90` / `02.06.03.02.13` / `02.06.04.02.01` / `02.06.06.02.10` 四份
**正文逐字节相同**（只有 frontmatter 的 `source_html` 不同）；
第五份 `02.08.04.34.02.02.10_DSCP…` 是另一个 body。
**GUI 文档只链第一个（`02.06.02.02.90`）**，本页主表 L1 格里的 `DSCP 的 device_cycle` 等
说的都是这一篇。**用 DSCP 当 key 去 raw 里找，会找到五篇。**

**⑥ `ChangeDevice` 与 Change Device wizard 名字像，但语料里两边没有任何链接——本页不许合并。**
`02.09.01.10.03.02.02.12_ChangeDevice.md`（HVM 远程控制命令，「sets the designated device for a SmarTest session」）与
GUI 的 [[change-device-wizard]] **词面相同、位置不同（`02.09.01.10` vs `02.08.04.03`）**。
HVM 那篇的出链**只有它自己的两个事件页**（`DEVICE_CHANGE_STARTED` / `DEVICE_CHANGE_COMPLETED`），
**一条都不指向 wizard**；wizard 那边的七条出链也**一条都不指向 HVM**。
**看起来像同类，但「看起来像」不算证据**——§2.5 的规矩是不许猜。
所以「激活一个已有的 device」那一行的 **L3 格留 `?`**，不是 `—`：**本页没找到证据，不是不存在。**

**⑦ 同一件事的两个名字：`GetTechPath` 也一样。**
`02.09.01.09.16_GetTechPath.md`（TPI 例程，取当前 technology path）**出链为零**。
它和 `.technology` 那篇**没有任何链接**。本页主表里**没有它的位置**。

**⑧ `extended_dram_factor` 那一行证明「L1 列 = DSCP 列」不成立。**
参数表这一行的 `Change Device wizard` 格是 `n/a`、`DSCP command` 格**也是 `n/a`**——
按参数表读，它在 L1 层**不存在**。但 `02.06.02.02.93_DTCP…` 明说：

> 「Currently, the only supported control parameters are testpoints and extended_dram_factor.」

**即它是 DTCP 在设，而且只有 DTCP。** 同理 `testpoints` 也是 DTCP（参数表那一行同样写 `n/a`）。
**所以主表的 L1 列必须把 DTCP 单列出来**，否则 `testpoints` / `extended_dram_factor`
两行会被错读成「L1 不存在」。DTCP 那篇还把这两个 key 直接链到 `.technology` 表的**行锚点**上
（`#_49363__row_testpoints`、`#_49363__row_extended_dram_factor`）——**这是逐参数钉的**。

**⑨ 参数表的 GUI 列只钉 Change Device wizard，没钉 New Device wizard——但 New Device wizard 里有同一组字段。**
`01.01.10.03.01_Creating_a_new_device.md`（New Device 路线）原文：

> 「- Expand the extra options and edit the device settings.」

> 「- Enter the maximum values for certain system parameters. These values determine the amount of memory reserved for the respective data structures.」

后面还逐个点了 `Utility block size` 与 `Fast Transfer Buffer Size`。
**但参数表里那一列只叫 `Change Device wizard`，`01.01.10.03.03` 也只说 `Edit Device page`。**
所以主表 GUI 格写 Change Device wizard 是**照参数表口径**。
**「New Device wizard 的 extra options 里有同一组字段」这一条 2026-09-20 从「推断」升成「④ 图证」。**
上一版在这里写的是「这是本页的推断（依据：上面两句原文 + 三个同名字段），**不是文档钉的**」——
**那句话已过时**：`354785.png` / `353431.png` 两张 extra options 展开图把它钉住了
（详见「对不上的地方」⑬）。**钉住它的是图，不是文档**——**图不可检索，这一点要说清。**

**⑩ 语料从没把 STPM 路线与 New Device wizard 路线并起来说过——但有一条侧面证据。**
`tpt_generate_device_dir` 那篇**没有 `## Related information` 节**，全文不提 wizard。
不过 `02.09.02.03.14_tpt_generate_template.md` 明说：

> 「When executing the command, STPM creates the files that make up a test program template. However, it does not create the device-specific files (Testflow file, Pin configuration file, .technology file). You will have to add those files manually before you convert the template to a new testflow device directory.」

**推断（不是文档直说）**：既然 template 里没有 `.technology`，
而 `tpt_generate_device_dir` 是「fills it with a testflow and related files, **as specified in the template**」，
那么 STPM 路线建出的 device 目录**应当缺 `.technology`**，
还得再走一次 Change Device 才完整。**这条推断链有三步，本页只写到「应当缺」，没有更多。**
（阶段页把这一点列为「最需要实机确认的一点」——本节给出的是**语料侧的最近答案**，不是确认。）

**⑪ 本页与 [[project]] 阶段页有一处标签对不上（在本 wiki 内部，不在语料）。**
阶段页的「涉及对象」表把 [[stpm]] 记成 `gui`，同一行的说明却写「命令行工具」；
本页按阶段页**正文**（L3 一节）与 `02.09.02.06` 的语法段，
把 `stpm` 归在 **L3**。[[setup-management-tool]] 则是真的**两个入口都有**
（`02.08.04.15` 那族的 .02 篇明说 `It is intended to be used from the Test Program Explorer (although it can also be started from the command line…)`），
所以它在主表第三组第一行**同时出现在 GUI 格与 L3 格**——**这是全表唯一一行同格两填**。

**⑫ raw 的目录位置不代表层——本页的链接证据是按前缀取的，所以这个坑要说出来。**
`02_System_reference/02.06_Command_Reference/02.06.01.02_Firmware_view.md` **在 `02.06` 目录里，
讲的却是 GUI**：`You can directly enter firmware command in the Task text box…`，
末尾的 `## Related information` 链的是 [[setup-perspective]]，不是命令页。
**即：拿 `02.06` 这个前缀当「L1」用，会把一篇 GUI 文档算成 L1。**
本页的做法是**逐条回原文核过才填格**（证据 ② 的正反两张表里的每一条都看过源文档），
**不是只按前缀分类**——① 到 ⑫ 里凡是标了「本页没读正文」的地方，也就是本页不敢往前推的地方。

**⑬ 图能读，这一页读了——原先这条写的是「本页一张图都没看 / 在语料树之外」，那是错的。**（**2026-09-20 更正**）

raw 里的图片路径 `../../../../raw/<n>.png` 从 md **往上四层正好是 `tdc-html/`**，
所以图在 `tdc-html/raw/`（该目录 5,193 张 png）。本页 `sources:` 32 篇里**共引 26 处图**
（**17 张不同的 `.png` + 2 张 `.svg`**，页面原先只点了 `354784.png`、`354785.png`
和「各有四张 New Device wizard 截图」——**数少了，`01.01.10.03.01` 与 `01.07.01.01` 各引六处、
五个不同文件**），**都看了**。

**`354784.png` 就是这一页要的那张**（`01.01.10.03.03`，alt 文字就是 `technology data`）：
整屏 Edit Device 页。它把**「GUI 的哪一个控件 ↔ 文件的哪一个参数」**在第一组里钉死了
**13 行**——这 13 个控件名里有 **12 个**与参数表 `Change Device wizard` 那一列**逐字相同**
（唯一不同的是 `Utility Block Size`：参数表写 `Utility block size`，**只差 `block` 的大小写**）：
`Device cycles` / `Waveform sets` / `Timing sets` / `Level sets` / `PDC sets` / `DPS sets` /
`M sets` / `Testpoints` / `Result Area Size` / `Fast Transfer Buffer Size` / `Utility Block Size` /
`Device technology` / `Licensing file`。
（图里还给了每个控件的**当时取值**：`256` / `16` / `256` / `32` / `1` / `32` / `1024` / `0` / `0` /
`0` / `16` / `cmos` / `NONE`，以及 `Device:` 栏的一个 workspace 路径
——**图里字小，本页只读到尾部是 `…/93000/src/test/devices/offline`**。）

**两个跟着图走的结论：**

- **「参数表那一列叫 `Change Device wizard`、正文说 `Edit Device page`」的来历**：`354784.png`
  的**窗口标题是 `Change Device - @jscbcm844>`，页眉才是 `Edit Device`**——
  **两个名字指的是同一个窗口**。`354785.png` 的标题则是 `New Device - @jscbcm843>`。
  （`@jscbcm…` 这两个串全语料 **0 命中**。）
- **正文说「向导里没有这个字段」「n/a」的两行，图里确实没有对应控件**：
  `period_res_precision`（正文：向导里没有这个字段）与 `extended_dram_factor`（正文：`n/a`）。
  **这是互证，不是新证据**——记在这里是为了说明**图的缺席也读过了，不是没看。**

**⑨ 的那条推断升级成 ④ 档。** ⑨ 原先写「『New Device wizard 的 extra options 里有同一组字段』
是本页的推断」——**`354785.png` 与 `353431.png`（New Device wizard 的 extra options 展开图）
把这条推断了结**：那个 `Extra options` 区里的字段标签与 Edit Device 页**逐个相同**
（`Device cycles` … `Utility Block Size` 一个不差）。
**要注明两件事**：① `Extra options` 这个**首字母大写的标签全语料 0 命中**（正文写的是小写 `extra options`）；
② `Licensing file` 那一栏在图里是**灰的**，格子里写着
`Licensing file cannot be selected at device creation`（**0 命中**）——**「建 device 时不能选 licensing file」
这个限制，正文没写，只有图里有。**

**两张 New Device 截图自己不一致，照实记、不替语料选一个**：`354785.png` 的开关区是**三行**
（含 `High memory support`），`353431.png` 只有**两行**（**没有 `High memory support`**）；
`Utility Block Size` 一张是 `32`、另一张是 `16`。

**一处要改，而纠正它的第一手证据不是图、是参数表自己：第一组最后一行的 `GUI` 格原先写「向导里的一组同名复选框」。**
参数表 `Change Device wizard` 那一列对这十个开关写的就是**释义**，**不是参数名**
（`Himem`、`Pretty-printed analog control file`、`Smart Scale compatibility checker`、
`Exa Scale check of sequencer program restrictions`、`SmartScale enforce DC sync compatibility`、
`MSET memory pre-allocation`、`Optimized Multiport Memory Allocation`、`Pulldown in level set 0`、
`Pulldown not configured pins`、`Fast bidirectional capability`）——**「同名」是上一版写的，错在措辞**。
**图给出的是第三个说法，而且与参数表在两处对不上**：

| 参数 | 参数表的 GUI 列（raw 文本） | 图里的复选框标签（`354784.png`） | 两处一致吗 |
|---|---|---|---|
| `himem` | `Himem` | `High memory support` | **不一致**（`Himem` 只在三份 `.technology` 投放里有；`High memory support` **0 命中**） |
| `pulldown_in_level_set_0` | `Pulldown in level set 0` | `Pulldown in level set 0` | 一致 |
| `pulldown_not_configured_pins` | `Pulldown not configured pins` | `Pulldown not configured pins` | 一致 |
| `optimized_multiport_memory_allocation` | `Optimized Multiport Memory Allocation` | `Optimized Multiport Memory Allocation` | 一致 |
| `fast_bi_directional_capability` | `Fast bidirectional capability` | `Fast bidirectional capability` | 一致 |
| `mset_program_memory_preallocation` | `MSET memory pre-allocation` | `MSET memory pre-allocation` | 一致 |

（另外那条 `Preinitialize vector memory to value` 是**复选框 + 取值框**，对应 `init_vectors_with_value`
那一行，**图里的框是空的**。**十个开关里有四个在图上找不到对应控件**
——`pretty_printed_analog`、`check_compatibility_with_smart_scale`、`check_exa_scale_seq_restrictions`、
`enforce_smart_scale_dc_sync_compatibility`——**它们四个的 GUI 标签参数表里有**（见上），
**只是不在这一屏**；**本页不推断为什么**，可能是不在那一屏，也可能是版本的差别。）

**一处不能拿图去填的格**：图里有个 `Device path:`（`354785.png`，New Device wizard）与
`Device:`（`354784.png`，Edit Device 页）——**那是器件自己的目录**，
**不是 org 定的那个根**。所以本页**没有**拿它去填第二组「定 device path 的根」那一行的 `?`
——`?` 的意思是「本页没找到证据」，而图上这个控件**不是那个东西**。

**`91496.png`（`01.01.07.02.02.04.03`）——本页原先明说「那张图没看、所以参数顺序写不出」，现在看了。**
图是一张 railroad 图：`smartest_mfh` 后面接 `split` / `assemble` / `create` / `assemble_all` /
`split_all` 之一，再接一个参数；**`split` 与 `assemble` 接 `<master_file>`、`create` 接 `<file_type>`、
`assemble_all` 与 `split_all` 接 `<directory>`**——即 `smartest_mfh <操作> <参数>`。
**图里的 token（`split`、`<master_file>`…）正文里都有，但「谁接谁」这层结构只在图里**：
正文那句 `It must be called in the following format:` **后面直接就是这张图，格式串 grep 不到**。
（`<file_type>` 的合法值 `level, timing, analog_control, waveform, routing, testflow, testtable`
是正文写的——**所以主表那一行的 L3 格现在填细了**。）

**那两张 `.svg` 不是 ④ 档，照实说清**：`46345.svg`（`Single Level File Structure`）与
`46346.svg`（`File Structure With an Extra Level`，`01.02.02.02.02`）是**矢量图**，
**标签就是文件里的文字**（`<DUT_PATH>`、`<INSTALLED_DUT_PATH>`、`testflow`、`dataset`、
`wafertype`、`testprogram` …）——**grep 得到**，所以按 §11.4 的判据它们**不属于「不可检索」那一档**。
它们画的是 device path 的两种目录布局，与第二组「定 device path 的根」那一行有关
（**`<DUT_PATH>` 与 `<INSTALLED_DUT_PATH>` 这两个名字正文里有**）。

**另外两张把第二组的 GUI 格从「名字」变成「名字 + 目录长什么样」：**
`91705.png`（Project Explorer view）把 device 目录下的子目录逐个摆出来
（`analog_control`、`applicat`、`calibration`、`ch_attributes`、`configuration`、`data_set`、
`di_report`、`error_map`、`format`、`levels`、`license`、`pin_attributes`、`profiles`、`report`、
`routing`、`scan_res`、`shmoo`、`testflow`、`testfunc`），根节点标着 `74ACT299 (current device)`；
`123063.png`（Test Program Explorer view）是同一个 device 的 setup 视图
（`<Testflow...>`、`<Pin Configuration...>`、`<Levels...>` …）加一条路径栏
`/home/v93k1/Digital_Training/74ACT299`。
**这一处要说清哪一部分是 ④ 档**：那些**目录名逐个在 `01.01.07.02.01.01` 的目录表里都有**
（表里连描述都给了：`applicat` = `Application data for production mode`），**所以目录名是互证**；
**只有图上那两个字符串是 ④ 档**——`74ACT299 (current device)` 与那条路径
`/home/v93k1/Digital_Training/74ACT299`（**都 0 命中**）。
**顺带一处语料瑕疵，图与文本一致、本页照实抄**：`applicat` **raw 的目录表里就是这么写的**
（不是 `application`）——**这是语料自己的截断，不是控件截断**，图只是把它照实画出来了。

**`02.06.01.02` 那四张（Firmware view）是 ⑫ 那一处的图证**：图里是一个 `Task >` 输入框、
一块标着 `FW Return Area` 的区域、以及历史下拉里的 `DFPN? (Q7)` / `DFPN? (CP)` 两条
——**「`02.06` 目录里放着一篇讲 GUI 的文档」这件事，看图就能确认**。
（`FW Return Area` 搜得到；**`(Q7)` 0 命中**。）

**图答不了的，照实说：**

- **四张是局部截图，只复述正文，答不了「控件 ↔ 参数」**：`353373.png`（一条错误横幅
  `No device path specified`，**0 命中**）、`353374.png`（一个控件 `Fast Transfer Buffer Size`
  的局部，值 `1`）、`353375.png`（错误横幅
  `Fast Transfer Buffer Size value is out of range (zero or 131072 - 16777216)`，**0 命中**
  ——它给的是**报错文案与一条范围检查**，不是对应关系）、`111034.png`（一个下拉按钮）。
- **`350664.png` / `111193.png` / `111110.png`（Select device 对话框与 Change Device 第一页）
  内部就不一致**：同一对话框的两张图字段名不同（`350664.png` 写 `Folder name:`、
  `111193.png` 写 `File Name:`）；错误横幅 `Selected directory is not a valid device`、
  筛选框 `All directories` 都 **0 命中**；`350664.png` 上另有两个**画在图上的黄底注记**
  （`Step1: type device name in this field` / `Step2: click Create device`，**0 命中**）。
  `111110.png` 上那三行说明文字（`Press 'Finish' to change to the selected device.` 等）
  **也全部 0 命中**——**它们是画在图里的**。**但同一件事的语义正文有**
  （`01.01.10.03.03` 写着 `enter the name and the full path of the device project in the Device text box. Then click Next.`，
  后面还有一步 `Click Finish.`）——**所以这一处是「图的字搜不到、内容有文本兜底」**，
  本页把它归在**互证**那一类，**不算 ④ 档**。
- **图是「某一次具体配置」的截图，不是规范。**「哪些参数必填、范围是什么」**图答不了**
  （唯一的例外是 `353375.png` 那一条范围文案）。
- **图没有翻转任何一格。** 主表里 `?` 的格子（第二组两处 `?`、「激活一个已有的 device」那一行的
   L3 格、以及 `GetTechPath` 无处可放这件事）**没有一格因为看图变成有名字**——
   ⑬ 里唯一的「填」是 `smartest_mfh` 的**调用格式**（那一格原先已经有命令名，缺的是格式）。

## 出处

`sources:` 三十二篇（见 frontmatter）。**分三档说清楚哪一档读到了什么**：

- **通读的**：`.technology` 那篇（`01.01.07.02.01.02`，含它那张参数表**全部 27 行**的五行格；
  主表第一组用了其中 **26** 行，`tester_model` 一行没收——它的 GUI 格与 DSCP 格原文都写 `n/a`，
  本页找不到第二个落点，**与其填三个 `—` 占一行，不如说在这里**）、
  `DSCP`、`DTCP`、`tpt_generate_device_dir`、`tpt_import_from_device`、`tpt_generate_template`、
  TAT、`Optimizing the technology file`、`Switch version command line tool`、
  New Device / Change Device wizard 两篇、Setup Management Tool 那三篇、
  `Specifying the Device Path`、`Device Directories`、
  `Creating a new device`（两篇）、`Editing technology data`、`Test program template`。
- **只读了头部或关键行的**：`02.08.04.15.03` 与 `02.08.04.03.03`（两份 `.technology` 投放，
  只用于核对「三份投放出链相同」）、`LEV_TRANSFER_TASK`、`VEC_TRANSFER_TASK`、
  `Result areas for error map data`、`Hidden upload`、`UPTD`、`ChangeDevice`、`GetTechPath`、
  `Device Technology Directory`、`Device directory structure`、`Firmware view`（`02.06.01.02`，
  只读了头部与 `## Related information`——它就是「对不上的地方」⑫ 那个例子）。
- **只见过链接、没读正文的**：证据 ② 两张表里除上面两档之外的每一篇
  （`MSET`、`MEAS`、`PMUR`、`GNOS`、`DMAS`、`UTOT`、`BCMT`、`Pull-down function`、
  `Counted_match_loops`、`PPMU_SETTING`、`GLOBAL section`、`The model file`、
  `Test_program_template` 等）。**它们在主表里的作用只有「被链到」这一条事实。**

**本页没做的**：

- **一条 L2 API 文档都没读透。** 主表 L2 列里那三个名字
  （`VEC_TRANSFER_TASK`、`LEV_TRANSFER_TASK`、`PPMU_SETTING`）**是从链接里取的**，
  **它们的构造函数、参数、用法，本页一个字没有**。
  `Result areas for error map data` 与 [[hidden-upload]] 同样——**只读到名字与链接**。
- **L1 命令页只读了两篇。** `DSCP` 与 `DTCP` 是通读的；
  `MSET`/`MEAS`/`PMUR`/`GNOS?` 四条**只见到 `m_sets` 那一行的 `Note:` 里列了它们**，
  **本页没有回到它们的原文复核**。
- **`smartest_mfh` 的命令行语法看了（2026-09-20）。** 原文的语法是**一张图**
  （`01.01.07.02.02.04.03` 的 `91496.png`：`Syntax of smartest_mfh`）。
  **上一版写的是「本页没看那张图——所以 `assemble` / `split` / … 的参数顺序本页写不出」**；
  现在**看了**，`smartest_mfh <操作> <参数>` 这层结构已写进主表第三组第一行与「对不上的地方」⑬。
  选项名与各自的说明文字**仍然只来自正文**（图的 token 与正文一致，多出来的只有结构）。
- **图看了（2026-09-20）。** 本页 `sources:` 32 篇里共引 **26 处图**（**17 张不同的 `.png`** + 2 张 `.svg`），
  **都看了**，逐张结论在「对不上的地方」⑬。
  **上一版写的「raw 里的图片路径向上爬四层，在语料树之外，所以本页没有任何来自图的结论」
  是错的，那句已删**。
  读图补上的是**「GUI 的哪一个控件 ↔ 文件的哪一个参数」这个粒度**（`354784.png` 一张就钉了第一组十三行），
  并把 ⑨ 的那条推断**升级成 ④ 档**；**但它没有翻转主表任何一格**——
  `?` 的格仍然是 `?`，⑬ 里唯一的「填」是 `smartest_mfh` 的**调用格式**。
  **图与图、图与文本不一致的地方（⑬ 里四处）本页照实并列，没有替语料选一个。**
- **没有实跑。** 没有开过任何向导、没有手改过 `.technology`、没有跑过 `DSCP?` / `DTCP?`、
  没有跑过 `stpm` / `smartest_mfh` / `tat` / `switch_version`。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/project.md`。
  后者是**待办**：project 那页目前不知道本页存在。
- **没有跑 `verify_stages.py`**（本批按批次分工，避免抢同一个文件）。

**本页 `layer: n/a` 的理由**：§6 要求 mapping 页必填 `layer`，而本页**本身不属于任何一层接口**
（它是对照表，不是接口）——`n/a` 是这个六值枚举里为这种情况准备的值。

`verified: doc-only`
