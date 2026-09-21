---
type: stage
title: 建工程 / Device / 目录结构
tags: [stage, project, device, workspace, technology-file, stpm]
related: [[pin]], [[testflow]], [[technology-file]], [[device-directory]], [[new-device-wizard]], [[change-device-wizard]], [[stpm]], [[tpt-generate-device-dir]], [[setup-management-tool]], [[model-file]], [[device-license-file]]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.04_SmarTest_workspaces.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.04.01_Creating_and_opening_a_workspace.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.04.02_Warnings_and_error_messages_when_starting_SmarTest.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01_Device_Technology_Defaults.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.01_Device_Technology_Directory.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02_Test_Program_Explorer.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.07_Merging_and_splitting_pattern_files.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.01_Concept_of_the_Setup_Management_Tool.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.03_Using_the_Setup_Management_Tool_from_the_Command_Line.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05_Collision_handling.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02_Project_Explorer_view.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.01.01_Importing_a_device_into_your_workspace.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.01.02_Changing_the_device_in_the_Project_Explorer_view.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.01.03_Removing_a_Device_from_your_Workspace.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.03_Device_Directories.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.04_SmarTest_lock_mechanism.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.01_Creating_a_new_device.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.02_Changing_the_device_with_the_Change_Device_button.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.03_Editing_technology_data.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.01_SmarTest_Prerequisites.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.02.01_SmarTest_Software_Base_Directory.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.02.02_Specifying_the_Device_Path.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.02.03_Setting_up_Workorder_Directories.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.02.04_SmarTest_environment_variables.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.03.01_Switching_between_SmarTest_versions.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01_Creating_a_new_device.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.02_SmarTest_directory_structure.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03_DUT_board_design_reference.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.04.01_Model_file_and_Device_license_file.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06_The_device_license_file.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07_The_Testflow_Analyzer_Tool__TAT.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07.02_Optimizing_the_technology_file.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07.03_How_to_generate_and_provide_a_device_license_file.md
  - 02_System_reference/02.06_Command_Reference/02.06.01.04_System_preparation_by_firmware_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.79_DMAS__DMAS__-__Define_Memory_Area_Size.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.93_DTCP__DTCP__-__Define_Technology_Control_Parameters.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.137_GNOS__-__GetNumberofOccupiedSets.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.190.09_Result_areas_for_error_map_data.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03_Change_Device_wizard.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15_New_Device_wizard.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.02_Editing_technology_data.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01_Managing_Test_Programs_with_SmarTest.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.01_Test_Program_Introduction.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08_Creating_production_functions_with_command_set_interface.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02_SmarTest_Program_Manager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.01.01_About_SmarTest_Program_Manager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.01.03_Installing_SmarTest_Program_Manager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.02_Using_SmarTest_Program_Manager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.02.01_Creating_and_editing_an_STPM_control_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.02.03_Creating_a_test_table_from_a_test_program_template.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.04_write_tp.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.04_STPM_merge_rules_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.06_STPM_command_line_options.md
  - 02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.02_Introduction_to_the_GIO_library_API.md
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.md
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# 建工程 / Device / 目录结构

> 在 workspace 里建出一个 device 目录、把它激活，并把设备级的资源上限（.technology）定下来——后面七个阶段的每一个产物文件，都落在这个目录里。

## 目的

文档事实：本阶段做的事是「create a new device directory and a link to your workspace」（`01.07.01.01_Creating_a_new_device`）。**这里的 device 指的是被测器件（DUT）的工程目录，不是一个测试程序文件**——文档原话是「The system stores device-specific setup data in device directories. Each device that you configure on the V93000 has its own device directory.」（`01.01.08.02.03_Device_Directories`）。

文档事实：device 是 Eclipse 意义上的 project，被装在一个 workspace 里。「A workspace is an Eclipse environment, which contains the configuration settings and your projects you are currently working on. The workspace contains a collection of device projects, device folders, and device files. ... A workspace can have any number of device projects.」（`01.01.04_SmarTest_workspaces`）

文档事实：本阶段同时确定设备级的资源上限。「The `.technology` file defines the source directory for technology-related settings, some device specific system parameters and some maximum values for certain system parameters. The maximum values for certain system parameters determine the amount of memory reserved for the respective data structures.」（`01.01.07.02.01.02_Technology_file_for_a_device`）这一步是后面 Pin / Level / Timing / Vector 能做多少套的前提——上限一旦定小，后续阶段直接撞墙。

文档事实：一个完整的生产测试由 Test Program + 运行环境组成，而 Test Program 本身包含 device-specific information（Testflow、User Procedure 目录、Wafer Description 文件）与 testfloor-specific information（Application、Prober/Handler、Execution Input、Data Bridge）。本阶段建的就是承载 device-specific 那部分的容器。（`02.09.01.01_Test_Program_Introduction`）

## 前置条件

1. **SmarTest 已安装且操作系统受支持。** 文档事实：SmarTest 要求 Advantest 提供的专用 RHEL，只有 Advantest 认可的 OS 与内核补丁可用；支持的 workstation 型号为 Z620 / Z640VM / Z4 G4，各自有 RAM 与 BIOS 版本要求。支持矩阵里 SmarTest 7.10 一行只列了 Z4 G4 + RHEL 7.4（Z620 与 Z640VM 为 `-`）。（`01.02.01.01_SmarTest_Prerequisites`）

2. **多版本共存时要先切到正确的版本。** 文档事实：切换版本用 `Start > Applications > Advantest V93000 > Switch Version`，或命令行 `/opt/hp93000/soc_common/bin/switch_version`；切换前必须满足「Two or more versions of SmarTest are installed」且「SmarTest or other tools, such as TML, MTP, and RDI, are not running」。（`01.02.02.03.01_Switching_between_SmarTest_versions`）

3. **workspace 先存在且合规。** 文档事实（Rules 原文）：workspace 目录不能放在 project 目录里面，反之亦然；workspace 不能多人共享、同一用户也不能同时开两次；workspace 不向下兼容主版本，必须用带主版本号的目录名（如 `workspace_7.1`）。（`01.01.04_SmarTest_workspaces`）

4. **device path 的根是环境级的，不是本阶段能随便定的。** 文档事实：SmarTest 解析位于 `/etc/opt/hp93000/soc/` 的 org 文件，从中取出用户可定义的 device path 根，取值为 `DUT_PATH` 或 `INSTALLED_DUT_PATH`（后者比前者多一级目录，便于做 revision control）。（`01.02.02.02.02_Specifying_the_Device_Path`）推断：新建 device 时 Device Path 文本框里填的路径，应当落在 org 文件指的那个根之下，否则 Workorder / 生产流程找不到它。（此推断来自上述 org 文件机制与 Workorder 目录约定两处文档的合并。）

5. **License 侧的前置。** 文档事实：SmarTest 先根据 model file 生成 license 请求再向 license server 结账；**若存在 device license file，则只评估它的参数，model file 里的 licensing 参数被忽略**。（`02.04.04.01_Model_file_and_Device_license_file`）文档事实：device license file 的值通过 `.technology` 文件的 `licensing_file` 参数指定，为空表示不用。（`01.01.07.02.01.02_Technology_file_for_a_device`）

6. **在已有 device 上继续工作后要建新 device 时。** 文档事实（`Before you begin` 原文）：「If you have worked on another device before, perform the following actions before creating a new device: Save the setup data. Stop or finish any active test.」（`01.07.01.01_Creating_a_new_device`）

7. **（仅模板路线）STPM 需要额外许可与安装。** 文档事实：STPM 随 STDL RPM 交付，`rpm -ivh <package>` 安装到 `/opt/93000/stdl/bin/`；「STPM requires a license that must be entered in your licensing file」。（`02.09.02.01.03_Installing_SmarTest_Program_Manager`）

8. **改已有 device 的 technology data 时**，文档只要求「Make sure that the device project exists.」（`01.01.10.03.03_Editing_technology_data`）

本阶段没有上游 stage，流程从 [[project]] 开始。

## 涉及对象

| 对象 | 层级 | 在本阶段干什么 |
|---|---|---|
| [[new-device-wizard]] | gui | 建 device 的唯一 GUI 入口（`93000 > Device > New Device`，或 `File > New > Project > 93000 > New Device`） |
| [[change-device-wizard]] | gui | 激活另一个 device，并编辑它的 technology data |
| [[technology-file]] | file | device 根目录下的隐藏文件 `.technology`，定 technology 源目录 + 资源上限 + license 文件 |
| [[device-directory]] | file | device 工程目录本身；它的子目录结构是后面七个阶段的落点 |
| [[device-technology-directory]] | file | `/opt/hp93000/soc/dev_tech` 下的 cmos / ecl 模板，建 device 时用它初始化 device 目录里的子目录结构 |
| [[workspace]] | gui | 装 device project 的 Eclipse 容器；本阶段往里面加一个 project |
| [[project-explorer-view]] | gui | 层次化显示 device 目录；在这里 import / remove / activate device |
| [[test-program-explorer]] | gui | 层次化显示 setup 数据，是后面各阶段 setup 工具的启动台 |
| [[setup-perspective]] | gui | 默认 perspective，含上述两个 view |
| [[org-file]] | file | `/etc/opt/hp93000/soc/` 下的一行文件，定 device path 根（DUT_PATH / INSTALLED_DUT_PATH） |
| [[model-file]] | file | 定义测试系统资源的配置与特性，是 license 请求的来源 |
| [[device-license-file]] | file | per-device 的 license 定义，存在时覆盖 model file 的 licensing 参数 |
| [[dscp]] | L1 | 把 `.technology` 里的上限真正下给固件；每次切 device 都会被调用 |
| [[dtcp]] | L1 | 设置 `testpoints` / `extended_dram_factor`，需 `*RST` 激活 |
| [[stpm]] | L3 | 命令行工具，做 MTP ↔ TPT 的合并、生成与清理 |
| [[stpm-control-file]] | file | 用 Python 语法写的 STPM 控制脚本 |
| [[stpm-merge-rules-file]] | file | 控制 STPM 合并时如何复用已有 setup 元素 |
| [[tpt-generate-device-dir]] | L3 | 从 test program template 直接生成一个新的 device 目录 |
| [[tpt-import-from-device]] | L3 | 反向：从已有 device 目录导出 test program template |
| [[setup-management-tool]] | gui | `smartest_mfh`，把 setup 组件按 master file 拆分 / 合并 |
| [[testflow-analyzer-tool]] | L3 | 统计当前 device 实际用掉的 set 数，用来优化 `.technology` / 生成 device license file |
| [[switch-version-command-line-tool]] | L3 | `/opt/hp93000/soc_common/bin/switch_version`，切换 SmarTest 版本 |

## L1 — Firmware / Setup Command

**[[dscp]]（DSCP / DSCP?）是本阶段的核心 L1 命令。** 文档事实：它「serves to define the maximal number of instances for the different types of so called parameter sets, and to reserve the necessary space for them in the Sequencer Memory」，并取代旧命令 `CNTR`/`CNTR?`。文档事实（关键耦合）：「**DSCP is called every time you switch to another device.** You can specify the parameter values of this call in the technology file (`.technology`), which is located in the main directory of every device.」——即本阶段写的 `.technology` 文件，正是固件 DSCP 的入参来源。

最小可用示例（照抄文档 Example 一节）：

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

查询用法（照抄文档 Syntax 一节）：

```
DSCP?
```

返回：

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
       {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
       [period_res_compatibility_model]
```

各参数与 `.technology` 的对应关系（文档事实，取自 technology file 的 "DSCP command" 行）：

| 参数 | `.technology` 参数 | 默认 / 最大 |
|---|---|---|
| `device_cycle` | `device_cycles` | 256 / 16384 |
| `waveform_set` | `waveform_sets` | 32 / 128 |
| `timing_set` | `timing_sets` | 256 / 999 |
| `level_set` | `level_sets` | 32 / 256 |
| `dps_set` | `dps_sets` | 32 / 256 |
| `pmu_set` | `m_sets` | 1024 / 12800 |
| `devicecycle_set` | `pdc_sets` | 1 / 128 |
| `routing_set` | （`.technology` 无对应参数） | 256 / 512 |
| `period_res_prec` | `period_res_precision` | 建 device 时置为 9（上限） |

来源：`02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter`、`01.01.07.02.01.02_Technology_file_for_a_device`。

注意（文档事实，前后两处必须一起看）：`02.06.01.04_System_preparation_by_firmware_commands` 写「When you execute DSCP, all sequencer instructions and all existing sets are reset to the power-on defaults」，而 DSCP 页写「Every call of DSCP deletes all data that were previously contained in the Sequencer Memory. Therefore, you have to reload the device setup after changing parameters using the DSCP command.」——同一个破坏性副作用，两种说法一致。

**[[dtcp]]（DTCP / DTCP?）补充 DSCP。** 文档事实：语法为 `DTCP {"key"}, {"value"}` / `DTCP? {"key"}`；「Currently, the only supported control parameters are `testpoints` and `extended_dram_factor`」；定义值必须用 `*RST` 激活，「The DTCP? query returns the currently selected value ... this is not the active value, if a new value has been defined, but not yet been activated with *RST.」（`02.06.02.02.93_DTCP__DTCP__-__Define_Technology_Control_Parameters`）

## L2 — Test Method API

文档未覆盖。

文档事实核查：`02.07_Test_Method_Reference` 里**没有任何一篇是把 C++ Test Method API 用于建工程 / 建 device 目录的**。本阶段的动作全部在 GUI、文件与固件命令三层完成，不写 C++ 代码。

本阶段与 L2 唯一有文档记载的耦合是**参数尺寸约束**，不是「本阶段调用 API」：

- 文档事实：`.technology` 的 `fast_transfer_buffer_size` 定义的是三个 L2 API 用的缓冲区——`VEC_TRANSFER_TASK`（向量数据修改）、`LEV_TRANSFER_TASK`（level spec 修改）、`PPMU_SETTING`（PPMU 设置）；且「The `VEC_TRANSFER_TASK` and `LEV_TRANSFER_TASK` APIs can be used only with SmartScale test head cards.」（`01.01.07.02.01.02_Technology_file_for_a_device`）
- 文档事实：`.technology` 的 `digital_default_result_area_size` 的说明直接指到 Test Method Reference 的 `02.07.04.01.190.09_Result_areas_for_error_map_data`；单位是 bytes，「One byte is one vector」，该区域在每个 digital pin 上预留（DPS pin 与配成 PMU/DPS 模式的 DC Scale pin 不预留），且「The reserved area counts against the license limit.」

推断：建工程时把这两个值定小了，会在 [[timing]] / [[level]] / [[testmethod]] 阶段以 L2 API 报错的形式暴露出来（Buffer 不足 / 上传超出预留区域），而不是在本阶段报错。**这是推断，不是文档结论。**

## L3 — 外部控制

本阶段的 L3 是**文档里真正存在、并且真的能建出 device 目录的**两条命令行路线，外加一个 setup 文件管理工具。

### 1. STPM —— 从模板生成 device 目录（这是本阶段最完整的 L3 通道）

文档事实：[[tpt-generate-device-dir]]「lets you create a new device directory from a test program template」——即用命令行把整个 device 目录建出来，绕过 New Device wizard。语法照抄文档：

```
tpt_generate_device_dir(
    tpt_dir = <tpt_directory>,
    device_dir = <directory>,
[device_name = <device_name>, ]
[pre_proc = <pre_proc>, ]
    post_proc = <post_proc>]
)
```

文档事实：`device_dir`「must either not exist yet (in which case STPM creates it) or it must be empty」；`device_name` 省略时用 `"device"`；若之前用 `tpt_import_from_device` 的 `copy_static_content` 导入过静态目录，这里会一并拷进新 device 目录。

配套命令（同属本阶段）：

- [[tpt-import-from-device]]——反向，从已有 device 目录导出 template。文档事实：`copy_static_content` 只能列名字、不能带路径，且必须是 device 目录顶层的条目；「If you include standard directories in this list (testflow, timing, levels, configuration, vectors, testtable), STPM generates a warning and does not copy the contents.」这句反过来给出了 STPM 认定的**标准目录清单**。
- `write_tp`——把改好的 MTP 写回磁盘；文档事实：「A control file can contain multiple write_tp statements. In that case, each one creates a separate file.」（`02.09.02.03.04_write_tp`）
- `clear_duplicated` / `clear_unused` / `extract_subflow` / `merge_subflow` / `remove_subflow`——清理与协作拆分，见 [[stpm-control-file]] 的分组清单。

调用方式与入口（文档事实）：

```
stpm[-help][-version][-timestamp][-licwait][-progress][-debug][-template][-setup <control_file>]
```

> 照原文的写法是 `stpm[-help]`——**`stpm` 与 `-help` 之间没有空格**（`02.09.02.06` 的 `Syntax` 段）。
> 本页初版在这里多打了一个空格，是**我改写了文档事实**，已按原文改回（2026-09-18）。

安装在 `/opt/93000/stdl/bin/`，二进制为 `stpm` 与 `stpm-mcm`。`-template` 会在当前目录的 `templates/` 下生成四个模板文件：`stpm_core_setup_template.setup`（管 MTP）、`stpm_tpt_admin_setup_template.setup`（建/改 TPT）、`stpm_tpt_tpgen_setup_template.setup`（从 TPT 生成 TP）、`stpm_merge_rules_template.setup`（合并规则模板）。（`02.09.02.06_STPM_command_line_options`、`02.09.02.01.03_Installing_SmarTest_Program_Manager`、`02.09.02.02.01_Creating_and_editing_an_STPM_control_file`）

控制文件是 Python 语法，文档事实：「STPM control files are Python files and as such support all standard conventions of the Python programming language. You can therefore use the usual programming constructs like conditional statements or loops.」控制文件可以有任意文件名、任意位置、无强制扩展名（`.setup` / `.py` 常见）。

### 2. Setup Management Tool（`smartest_mfh`）—— setup 组件的拆分与合并

文档事实：程序文件名为 `smartest_mfh`，位于 `/opt/hp93000/soc/com/SETUP_MAN`。操作模式有 `assemble` / `split` / `assemble_all` / `split_all` / `create`；`create` 模式必须给 `file_type`，可选值为 `level, timing, analog_control, waveform, routing, testflow, testtable`。`assemble_all` / `split_all` 作用于一个 device 目录下的全部 master file；若不是在 device 根目录下调用，目录要在最后一个参数给出。（`01.01.07.02.02.04.03_Using_the_Setup_Management_Tool_from_the_Command_Line`）

文档事实（概念）：工具把 timing / testflow 这类 setup 组件拆成子文件存进 repository，靠一个 master file 串起来；**关键区别**——「A pattern master file can be passed to SmarTest as it is. This does not hold for the setup components that can be handled by the Setup Management Tool. SmarTest by itself does not support the concept of a master file for these components. Therefore the Setup Management Tool must merge the subfiles listed in the master file into a single setup file before they can be downloaded into the tester memory.」（`01.01.07.02.02.04.01_Concept_of_the_Setup_Management_Tool`）

文档事实（冲突处理）：assemble 时子文件之间可能出现定义碰撞，工具用 `REMAP` 关键词自动改名，`Bind` 关键词指定碰撞解决后需要一起更新的文件；「All the changed content during the collision handling will be logged in the file `changelog.txt`, which locates in the same directory with the setup master file.」（`01.01.07.02.02.04.05_Collision_handling`）

### 3. 版本切换

文档事实：[[switch-version-command-line-tool]] 即 `/opt/hp93000/soc_common/bin/switch_version`。文档明确建议：「Use the command line form when executing the switch_version tool in a script.」（`01.02.02.03.01_Switching_between_SmarTest_versions`）

### 明确不在本阶段的 L3（文档事实核查）

- [[smartshell]]：文档事实存在，是「an external scripting interface for SmarTest that allows external tools ... to control the test execution and receive the test results back」，有网络服务器组件，可从 Python 脚本或终端访问。但 `02.15_SmartShell` 正文只说「The SmartShell documentation is available as PDFs: Quick start guide / User guide / Command reference」——**具体命令在语料正文里文档未覆盖**（只有 PDF 链接）。文档也没有把 SmartShell 与建 device 关联起来。
- [[gio-library-api]]（`02.13`）：文档事实是「allows for the connection of external instruments in SmarTest to the system controller」，用途是外部仪器通信，调用方可以是 7.5 及以上的 test program 或 SmarTest 之外的任意应用。文档没有把它用于建 device。
- [[test-suite-control-api]]（`02.09.01.14`）：文档事实是「used to directly control the test suites outside of the testflow tool. Only UTM-based test suites are supported with these APIs ... They cannot be used in test method programming and also cannot be used in parallel with HVM API and BLC API by the same client process.」——是运行期控制，不是建工程。

推断：这三个接口属于 [[run]] / [[results]] 阶段的候选 L3，而不是本阶段；本阶段的 L3 就是 STPM + smartest_mfh + switch_version。

### 补：同层的产物文件接口（[[tpi-program-routines]]）

文档事实（`02.09.01.09.02_DataManager`）：`DataManager` 提供从程序内访问 SmarTest Test
Program Explorer 的接口，「the mirror image of the interactive interface」。与本阶段相关的
文件标识是 `dm_testprog`（test program 文件）与 `dm_testflow`（testflow 文件），
配 `dm_copy_in` / `dm_load` / `dm_save` / `dm_merge` / `dm_delete`。
`DataManager` 的 Opc 参数取值即 `dm_load` / `dm_save` / `dm_merge` / `dm_copy_in` / `dm_delete`。

这与本页上面第 1 条的 STPM 是**两条不同的通道**：STPM 是命令行工具（生成/管理 device 目录），
`DataManager` 是从程序内操作产物文件。

### 层归属（**推断**，留待复核）

`02.09.01.09` 章自述 TPI 例程是「available for writing test flow programs」，
而本 wiki 的 L3 定义是「外部控制」。把它记在 L3 的理由：①它自述是 GUI 的**程序化镜像**，
操作的是整个测试程序的产物文件集，不是执行期 test method 内的 API；②`HpFwTask` 明写
「will not automatically handle site focus **as test method APIs do**」——**文档自己把它和
L2 的 test method API 对立起来**。**存疑**：文档未明说调用者是 testflow 程序还是外部程序。

## 产物

### 一个 device 目录 = 一个被测器件的工程

文档事实：新建 device 的**唯一**产物落地方式是「SmarTest creates a set of data for your new device and activates the device. The values you entered during this task are written to the Technology file for a device.」（`01.07.01.01_Creating_a_new_device`）

### 根目录下的文件

| 文件 | 放什么 |
|---|---|
| `.project` | Configuration of the device project（Eclipse project 描述） |
| `.settings/vectors` | Layout data for the Pattern Debug Tool and Pattern Explorer |
| `.technology` | device 的 technology file：源目录 + 系统参数最大值 + `licensing_file` |
| `lock_file` | Lock file for the device |

文档事实（lock 机制）：「If a device directory is being used by a user (normally the superuser) with write permission for that directory, then a lock file is created in the directory. This prevents other users from using that device software. Only a user with write permission can run the device software a second time. Note that you can work on a write-protected device, but must save all changes to another directory.」（`01.01.08.02.04_SmarTest_lock_mechanism`）

### 子目录清单（这是后面七个阶段的落点）

下表的「放什么」一列，全部照抄 `01.01.07.02.01.01_Device_Technology_Directory` 的 Contains 表原文；「后续阶段」一列是**推断**，来自目录名与各阶段职责的对应，不是文档原话。

| 子目录 | 放什么（文档事实） | 后续阶段（推断） |
|---|---|---|
| `analog_control` | Analog setup file | — |
| `applicat` | Application data for production mode | [[run]] |
| `calibration` | Calibration data（ACTCatr 文件见 `02.08.04.04.01.01_ACTCatr`） | — |
| `ch_attributes` | Channel attributes files | [[pin]] |
| `configuration` | **Pin file** | [[pin]] |
| `data_set` | (Reserved) | — |
| `di_report` | (Reserved) | — |
| `error_map` | Exported error maps in ASCII format | [[results]] |
| `format` | Pin display information for GUI tools | [[pin]] |
| `levels` | **Level file** | [[level]] |
| `license` | License file | — |
| `pin_attributes` | Edge delays for each pin, used for calibration | [[pin]] |
| `profiles` | Date logging configuration | [[results]] |
| `report` | Log file | [[results]] |
| `routing` | Analog and relay routing information | — |
| `scan_res` | (Reserved) | — |
| `shmoo` | Shmoo setup and result files | [[results]] |
| `testflow` | **Testflow file** | [[testflow]] |
| `testfunc` | Customer-defined connect and disconnect sequences | — |
| `testmethod` | **Test method file** | [[testmethod]] |
| `testprog` | Test program file | [[run]] |
| `testtable` | Test table file | [[testmethod]] / [[results]] |
| `timing` | **Timing file** | [[timing]] |
| `timing_dgrm` | (Reserved) | — |
| `vectors` | **Vector file** | [[pattern]] |
| `vectors/.cache` | Cached pattern file dependencies | [[pattern]] |
| `wafertyp` | Wafer description file | [[run]] |

### 文档内部不一致（按 schema §10 并列记录，不自行裁决）

`01.07.01.01.01_Device_directory_structure` 给出的 `ls -al` 实际输出里，还多出两个目录：

- `waveform`——`ls -al` 里有（`drwxr-xr-x 3 … Apr 30 2010 waveform`），但上面那张 Contains 表**没有列它**。
- `waste`——同上，`ls -al` 里有，Contains 表没列。

两种说法并列，各自出处如下，本项目不选一个当正确答案，等实机验证：

- 说法 A（有 `waveform` / `waste`）：`01.07.01.01.01_Device_directory_structure` 的 `ls -al` 输出（该输出是 2010-2011 年的样本，含 `my_74ACT299_tp`）。
- 说法 B（未列 `waveform` / `waste`）：`01.01.07.02.01.01_Device_Technology_Directory` 的 "Subdirectories and files in the device technology directory" 表。

推断：`waveform` 与 equation-based timing 的 wavetable 有关（`.technology` 的 `waveform_sets` 参数说明是「Total of waveform sets (fixed timing) and wavetables (equation-based timing)」），`waste` 的用途文档未覆盖。

### device 目录里的子目录从哪来

文档事实：「Each device directory contains a `.technology` file.」「Defines the technology of the device by pointing to the corresponding directory structure (cmos or ecl) within the test system software data files. ... **This subdirectory structure is initialized from the corresponding dev_tech directory when the device is created.** Default levels are defined by the selected device technology.」（`01.01.07.02.01.02_Technology_file_for_a_device`）

文档事实：默认的 device technology 目录为 `cmos` 与 `ecl`，路径是 `/opt/hp93000/soc/dev_tech`。（`01.01.07.02.01.01_Device_Technology_Directory`）

文档事实（版本）：**SmarTest 7.2.2 起，建 device 时会创建 `testtable` 子目录。**（`01.07.01.01_Creating_a_new_device` 的 Functional changes；同一条也出现在 `01.07.01.01.01`）

### `.technology` 文件的格式

文档事实（照抄样例行）：

```
/dev_tech/cmos
device_cycles: 256
waveform_sets: 16
timing_sets: 256
level_sets: 32
dps_sets: 32
pdc_sets: 1
m_sets: 1024
period_res_precision: 9
testpoints: 10000
utility_lines_per_pogoblock: 16
tester_model: act
licensing_file:
init_vectors_with_value: 50
fast_transfer_buffer_size: 131072
```

文档事实：完整参数表（含取值、默认值、对应的 Change Device wizard 字段、对应的 DSCP 参数）在 `01.01.07.02.01.02_Technology_file_for_a_device` 的 "Parameters of the .technology file" 一节，共 24 个参数：`/dev_tech/cmos 或 /dev_tech/ecl`、`check_compatibility_with_smart_scale`、`check_exa_scale_seq_restrictions`、`device_cycles`、`digital_default_result_area_size`、`dps_sets`、`enforce_smart_scale_dc_sync_compatibility`、`extended_dram_factor`、`fast_bi_directional_capability`、`fast_transfer_buffer_size`、`himem`、`init_vectors_with_value`、`level_sets`、`licensing_file`、`m_sets`、`mset_program_memory_preallocation`、`optimized_multiport_memory_allocation`、`pdc_sets`、`period_res_precision`、`pulldown_in_level_set_0`、`pulldown_not_configured_pins`、`pretty_printed_analog`、`tester_model`、`testpoints`、`timing_sets`、`utility_lines_per_pogoblock`、`waveform_sets`。

### 怎么改这个文件

文档事实：`.technology` **通常不是手改的**——「The `.technology` file is normally updated by making changes in the Change Device dialog (on the menu, select 93000 > Change Device). Changes made in this window are saved in the `.technology` file and communicated immediately to the firmware using the DSCP (Define System Control Parameter) and other firmware commands. These changes are permanent and apply each time the device is selected thereafter.」

文档事实（手改的后果与补救）：「The parameters that are not present in the Change Device window can be changed permanently only by editing the `.technology` file directly. In this case, the DSCP command must be issued manually to define the new values to the firmware, or the device must be re-selected (which will reissue the DSCP command).」（`01.01.07.02.01.02_Technology_file_for_a_device`）

### workspace 侧的产物

文档事实：`Each time you use the system, a file called .device_inuse_soc@<hostname> is stored in your home directory. This file remembers which device you were using last, and sets a path to its device directory.`（`01.01.08.02.03_Device_Directories`）

文档事实：SmarTest 7.1.4 把该文件改名过（Functional changes 原文「Renamed .device_inuse_soc file」）。

### STPM 路线的产物

文档事实：`tpt_dir` 指向 TPT 文件与目录的生成位置——「If the directory does not yet exist, STPM creates it」；`tpt_generate_device_dir` 则生成完整 device 目录。（`02.09.02.03.15_tpt_import_from_device`、`02.09.02.03.16_tpt_generate_device_dir`）

推断：STPM 路线生成的 device 目录与 New Device wizard 生成的应当是同一套结构（`tpt_generate_device_dir` 的描述是「creates the directory structure for the device and fills it with a testflow and related files, as specified in the template」），但**文档没有逐目录列出 STPM 生成的目录清单**，也没有说它写不写 `.technology`。这是本页最需要实机确认的一点。

### DUT board 硬件侧（明确不在本阶段产物内）

`02.03_DUT_board_design_reference` 是**板级硬件设计**参考：DUT board design overview / Test heads / DUT interfaces / Utility lines / Utility power supplies / Pogo pin assignment / Electrical design rules / DUT board docking / stiffeners and inlay plates / Wafer prober interfaces。文档事实：它是设计 DUT board 用的，不是 tester 或 device 工程的配置。**判定：不计入本阶段。** 唯一沾边的接触点写在 `.technology` 侧——`utility_lines_per_pogoblock`（16 或 32 utility lines per pogo block）的说明指向 model file 的 GLOBAL section 里的 `utility_lines`，属于系统资源配置而非板级设计。（`01.01.07.02.01.02_Technology_file_for_a_device`）

**三层对照表见 [[mapping-project]]** —— GUI 操作 ↔ 文件 ↔ L1 命令 ↔ L2 API ↔ L3 接口 的按目的对照
（`wiki/mappings/mapping-project.md`；证据分三档写明，**`?` 与 `—` 不同义**：前者是「本页没找到证据」，
后者是「这一层不存在这个对应物」）。

## 验证

文档给出了明确的验证动作，按可信度从高到低：

1. **`ls -al` 比目录。** 文档事实（原文即为一条 Procedure）：「In a terminal window, change into the device project directory you just created (for example, `my_74ACT299_tp`) with the command `cd` and type the command `ls -al`.」然后与文档给出的期望输出对比。（`01.07.01.01.01_Device_directory_structure`）

2. **在 Project Explorer view 与 Test Program Explorer view 里看。** 文档事实：「From the SmarTest Setup Perspective observe the content of the structure in the Project Explorer view and in the Test Program Explorer view」。（`01.07.01.01.01_Device_directory_structure`）

3. **Project Explorer 上应看到 `(current device)` 标记。** 文档事实：「In the Project Explorer view, the activated device is tagged with the text "(current device)".」（`01.01.08.02.01.02_Changing_the_device_in_the_Project_Explorer_view`、`01.01.10.03.02_Changing_the_device_with_the_Change_Device_button`）

4. **切 device 时的引用检查应无警告。** 文档事实（原文 Results 段）：「After activating the selected device, the system checks if all the referenced projects of the device project exist in the workspace. If not, the Warning window appears to inform the users, that the required projects should be imported.」——看到这个 Warning，说明 device 引用的 test method project 还没 import，可点 `Import missing projects into workspace`。（同上两篇）

5. **Test Program Explorer 的显示约定（文档事实）。** 「If a file name is displayed instead of the component (for example, `<Levels...>`), the related data file is loaded. ... If the symbol `*` is displayed besides the file name, the data was changed and not yet saved. If the text `[external]` is displayed besides the file name, a component is loaded that does not belong to the active device.」（`01.01.07.02.02_Test_Program_Explorer`）

6. **固件侧回读：`DSCP?`。** 文档事实：「The DSCP? query returns the existing settings.」返回格式见 L1 小节。用它核对 `.technology` 里的值是否真的下给了固件。（`02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter`）

7. **可用内存查询：`DMAS? MFRE`。** 文档事实：`.technology` 文档在 `digital_default_result_area_size` 下明写「You can use the [DMAS? MFRE] query to determine the available memory.」（`01.01.07.02.01.02_Technology_file_for_a_device`）

8. **用 TAT 核对资源上限是否定得合理。** 文档事实：`02.04.05.07.02_Optimizing_the_technology_file` 说 TAT「provides the number of sets used by the current device in a comment section」，列出 Level sets / DPS sets / Wavetables / Timing sets 四个数（文档给了示例：Level Sets 220 / DPS Sets 79 / Wavetables 128 / Timing Sets 726）。用途原文是「To optimize the Technology file for a device, you can adapt the number of sets to the number of used sets.」——这是文档给的正规做法，但**它需要先有 testflow 内容，所以实际是后面阶段回过来调 `.technology` 的手段**。（推断：本阶段刚建完 device 时 set 数还是 0，这一步查不出东西。）

9. **由 TAT 生成 device license file。** 文档事实：「The testflow analyzer tool (TAT) analyzes the testflow and generates a device license file (`.licenses`) in the current directory.」前置是 SmarTest 起来（建议 offline）、load testflow 含 setups、并提供 HDF。（`02.04.05.07.03_How_to_generate_and_provide_a_device_license_file`）

10. **`.technology` 变更后的验证。** 文档事实（原文 Results）：「The values entered during this task are written to the `.technology` file of the selected device.」（`01.01.10.03.03_Editing_technology_data`、`02.08.04.15.02_Editing_technology_data`）

## 常见错误

1. **Create Device 按钮是灰的。** 文档事实：「even if there are valid SmarTest devices located in the selected directory, the Create Device button only becomes active after a new or empty directory is specified.」（`01.07.01.01_Creating_a_new_device`）

2. **New Device wizard 里参数值不合法。** 文档事实：「If a parameter value is specified that is not suitable, the associated value field is highlighted and an error message is displayed in the top pane.」文档举的例子是 Fast Transfer Buffer Size，并给出「A corresponding message with valid values is displayed in the top pane.」及要求「Set the Fast Transfer Buffer Size to a minimum of 131072.」（`01.07.01.01_Creating_a_new_device`）

3. **导入 device 时报 `does not have .technology file`。** 文档事实（原文 Note）：「When you select the device directory, you have to enter the device directory by double-clicking, otherwise you will get the error message `/<path>/<directory> does not have .technology file`.」（`01.01.08.02.01.01_Importing_a_device_into_your_workspace`）

4. **启动时报 `Workspace in use, choose a different one.`** 文档事实，排查入口两条：「Check if another user is working in the specified workspace.」「Check with your system administrator that on NFS mounted home directories file locks are allowed. If file locks are not allowed, create your workspace under `/var/...`.」（`01.01.04.02_Warnings_and_error_messages_when_starting_SmarTest`）

5. **启动时报 `java.io.IOException: No locks available`。** 同上，排查入口：NFS home 目录是否允许 file lock，不允许就把 workspace 建到 `/var/...` 下。（同上）

6. **启动时弹出 `Import missing projects into workspace` 警告。** 文档事实：SmarTest 启动时检查所有引用，包括 device 与它引用的 test methods，对任何未导入的 referenced project 都会问；点该按钮即可导入。（同上）

7. **删掉了当前 device。** 文档事实（原文 Note）：「**Do not remove the current device.** Removing the current device may result in an undefined state of the SmarTest software.」另一个坑：「If you select `Also delete contents under ...` the device directory and its content will be deleted permanently.」（`01.01.08.02.01.03_Removing_a_Device_from_your_Workspace`）

8. **改了 `.technology` 导致后面 load 不上 / 测不了。** 文档事实（原文 Note）：「Changing the `.technology` file may lead to problems when loading setup data or executing tests. Technology data specifies allocation of tester resources. **If such specification does not match the device's needs, the device cannot be edited or tested later on.**」（`01.01.10.03.03_Editing_technology_data`、`02.08.04.15.02_Editing_technology_data`）

9. **改了 `.technology` 但固件不知道。** 文档事实（补救手段，本条即是排错入口）：不在 Change Device 窗口里的参数，手改后「the `DSCP` command must be issued manually to define the new values to the firmware, or the device must be re-selected (which will reissue the `DSCP` command).」（`01.01.07.02.01.02_Technology_file_for_a_device`）

10. **DSCP 报错。** 文档事实（Errors 一节原文），出现以下任一情况会报错：device cycles 超出范围 / waveform sets 超出范围 / timing sets 超出范围 / level sets 超出范围 / DPS sets 超出范围 / 指定的 set 大小对当前内存配置过大 / **timing sets 小于 waveform sets**（文档在参数表里也重申：「The number of timing sets must be equal to or greater than the number of waveform sets, as there must be at least one timing set per waveform set.」）（`02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter`）

11. **DSCP 把已有设置清空。** 文档事实：「Every call of DSCP deletes all data that were previously contained in the Sequencer Memory. Therefore, you have to reload the device setup after changing parameters using the DSCP command.」以及 `02.06.01.04` 的「all sequencer instructions and all existing sets are reset to the power-on defaults」。**因为切 device 会自动调 DSCP，所以每次切 device 之后都要重新 load setup。**（`02.06.02.02.90_DSCP`、`02.06.01.04_System_preparation_by_firmware_commands`）

12. **切换版本时 cal data 版本不匹配的警告。** 文档事实（原文 Note）：「For SmarTest 7.10.0 a warning is always given after a selection has been made for the Calibration Data (std). This warning, that the selected cal data version does not match the selected SmarTest version, must be ignored. Press 'y' to continue.」（`01.02.02.03.01_Switching_between_SmarTest_versions`）

13. **STPM 因无 license 直接退出。** 文档事实：「If this option is not used, STPM exits with an error message when no license is available.」——带 `-licwait` 可改为等待。（`02.09.02.06_STPM_command_line_options`）

14. **`tpt_generate_device_dir` 的目标目录非空。** 文档事实：`device_dir`「must either not exist yet … or it must be empty」，否则失败。（`02.09.02.03.16_tpt_generate_device_dir`）

15. **device 被别人的 lock 挡住。** 文档事实：有写权限的用户在使用 device 目录时会创建 lock file，「This prevents other users from using that device software. Only a user with write permission can run the device software a second time.」绕法（文档明写）：「you can work on a write-protected device, but must save all changes to another directory.」（`01.01.08.02.04_SmarTest_lock_mechanism`）

16. **device 目录丢失或损坏。** 文档事实：「If it [`.device_inuse_soc@<hostname>`] is not present in your home directory, or if the device directory is either missing or corrupt, the system displays the Select Device Folder window, where you can select an existing device or create a new device with default settings inside an empty folder.」（`01.01.08.02.03_Device_Directories`）

## 下一步

[[pin]]。

文档事实：device 目录建好之后，承载 pin 分配的 `configuration` 子目录里放的是 **Pin file**，`ch_attributes`、`pin_attributes`、`format` 也都是 pin 相关的落点（`01.01.07.02.01.01_Device_Technology_Directory` 的 Contains 表）。New Device wizard 里设的只是资源上限（能开多少 level set、timing set、多少 device cycle），并没有分配任何一个具体的 pin。

推断：device 目录建出、`.technology` 定下上限之后，第一个要填的 setup 组件就是 pin 配置，因为它是 [[level]] / [[timing]] / [[pattern]] 的共同前置（这条约束已在 `schema.md` §2.4 的约束页清单里登记）。

（另：若本阶段是用 STPM 的 template 路线建的 device，`tpt_generate_device_dir` 会连带写入一个 testflow，此时 [[pin]] 与 [[testflow]] 的入口都已就位，但填充顺序不变。）
