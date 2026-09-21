---
type: stage
title: Pin / Channel 配置
tags: [pin, channel, multisite, utility-line, dps, dc-scale]
related: [project, level, timing, pattern, pin-configuration-tool, pin-configuration-file, dfpn, conf, dfps, dfgp, dfpt, dfpr, dfut, dfup, pals, pste, psfc, stme, ddic, sqst, ganging]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03_Pin_configuration_setup_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01_Concepts_of_Configuration_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.01_Introduction.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.02_Assigning_a_pin_name_to_a_digital_channel.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.03_Configuring_pin_type_and_operating_mode_for_a_context.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.03.01_Mode_contexts.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.04_Assigning_a_pin_name_to_a_digital_or_DC_scale_channel.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.05_Defining_a_utility_line.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.06_Defining_pin_groups.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.07_Defining_ports.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.08_Defining_a_utility_purpose.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.09_Configuring_additional_sites_for_multi-site_testing.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10_Controlling_multiple_test_sites.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.01_Activating_and_masking_a_site.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.02_Setting_the_setup_focus.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.03_Defining_the_query_focus.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.04_Controlling_the_site_match_function.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.11_Errors.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.12_Pin_Configuration_Example.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02_List_of_configuration_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.01.05_Site_dependent_firmware_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.66_DFPT__DFPT__-__DeFine_PorT.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.180_PQFC__PQFC__-__Parallel_Query_FoCus.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.296_UDGP_-__UnDefine_GrouP.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.299_UDPT_-__UnDefine_PorT.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.01_CHIN__-__CHannel_INformation.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.06_DFLV__DFLV__-__DeFaultLeVel.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.07_DFPC__DFPC__-__DeFine_Pin_Comment.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.13_DSCP__DSCP__-__Define_System_Control_Parameter.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.14_GCTX__-__Get_ConTeXt.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.15_HWTY__-__HardWare_TYpe.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.18_PFND__-__Pin_FiND.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.20_PRLT__-__request_Parallel_ResuLTs.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.29_UDVP_-__UnDefine_Virtual_Pin.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.31_UPST__UPST__-__Utility_Purpose_STate.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.32_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md
  - 02_System_reference/02.06_Command_Reference/02.06.04_Routing_Setup_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.04.01_Concepts_of_routing_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.04.02_List_of_routing_setup_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.08_Relays_and_Control_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.08.01_Concepts_of_relay_control.md
  - 02_System_reference/02.06_Command_Reference/02.06.08.01.01_Connecting_the_DUT_to_the_test_system_resources.md
  - 02_System_reference/02.06_Command_Reference/02.06.12_Utility_Line_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.12.01_Accessing_Utility_Lines.md
  - 02_System_reference/02.06_Command_Reference/02.06.12.02_List_of_utility_line_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.06_UPOW__UPOW__-__Utility_POWer.md
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.12_UTSC__UTSC__-__UTility_line_Serial_Configuration.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07_Testing_a_Basic_Digital_Device.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01_Testing_a_basic_digital_device.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.02_Defining_the_pins.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.02_Task_2__Pin_Configuration_Setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01_Introduction_of_the_Pin_Configuration_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.02_Importing_the_pin_configuration_from_a_CSV_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.05_Applying_pin_configuration_data.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.06_Saving_a_modified_pin_configuration.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.03_Defining_a_context.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.04_Defining_additional_test_sites.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08_Working_with_pin_groups.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.10.01_Creating_a_utility_purpose.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.05_Utility_Purpose_Editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.01_Rules_for_defining_groups.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.02_Incompatible_pin_groups.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.06_DC_Scale_Limits_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.09_Ground_sense_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.12_State_indicator.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.09.01_Pin_configuration_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.147_PIN_UTILITY.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148_PinPropertyMonitor.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.01_HW_PIN_STATE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68_FLEX_RELAY.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.md
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.md
  - 02_System_reference/02.02_Specifications/02.02_Specifications.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03_DUT_board_design_reference.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04_Utility_lines.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05_Test_Head_Cards.md
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# Pin / Channel 配置

> 把「器件 pin 名」绑定到「测试机物理 channel」，并一次性定下每个 pin 的类型/工作模式、
> 分组、端口、utility line 与多 site 分配——这是整条流程里唯一不可跳过的一步。

## 目的

文档事实（`02.06.03_Pin_configuration_setup_commands.md`）：

> Configuring pins is the first step you must take when preparing a test. It is impossible
> to define level, timing, or vector parameters without the pin configuration.

文档事实（`02.08.04.18.01_Introduction_of_the_Pin_Configuration_Tool.md`）：

> The pin configuration file is the first setup file that must be completed before you can
> test a new device. If the pin configuration details have not been entered, the software
> will not let you enter details about the DUT in any other setup window.

文档事实（`01.07.01.02_Defining_the_pins.md` / `02.08.01.01.02_Task_2__Pin_Configuration_Setup.md`）：

> Define the relationship between resource pins and DUT board.

综合这三句，本阶段要解决的问题是：**建立 pin 名 ↔ 物理 channel 的映射**（这是后面
Level / Timing / Vector 全都能引用 pin 名的前提），并顺带把 pin 的类型（i/o/io/dc/off）、
工作模式（F160/FAST/…）、mode context、pin group、port、pin alias、utility line 与
utility purpose、以及多 site 的通道分配全部落盘成 `pin configuration file`。

本阶段**不涉及**：通道板卡的电气规格（那是 `02.02_Specifications` / `02.05_Test_Head_Cards`
的范围）、也不涉及运行期怎么开关 utility line（那是 [[run]] 阶段）。本阶段只做「定义」。

## 前置条件

- **`[[project]]` 已完成**：device 工程与目录已建好。`01.07_Testing_a_Basic_Digital_Device`
  给出的顺序是 Creating a new device → **Defining the pins** → Setting up your levels →
  Waveform and timing sets。pin configuration 文件落在 device 目录的 `configuration/`
  子目录下（`01.07.01.01.01_Device_directory_structure.md` 列出的目录清单里有 `configuration/`）。
- **物理位置信息已查清**：channel 号是 5 位数（前 3 位 = pogo block，后 2 位 = block 内
  channel 01–16），这个编号由通道板卡插在哪个槽决定。`02.06.03.01.02` 与 `Digital_Pins_editor`
  都指向 `02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md`。
  → 硬件侧资料（`02.03_*`、`02.05_*`、`02.02_*`）**不是本阶段的一部分**，而是本阶段的
  输入查表；边界判定见文末「归属判定」。
- **`DFLV` 必须在 `*RST` 之后、pin 配置之前**（文档事实，`02.06.03.02.06_DFLV` 原文：
  "The command must be issued after the reset of the system by *RST and before pins are
  configured."）。若你的程序不使用该默认电平机制可忽略，但顺序要求是明写的。
- **sequencer 必须是 OFF**。多个命令页明写：
  - `DFPN`："you can use the DFPN command only if the sequencer state is OFF (compare the
    SQST command)"（`02.06.03.01.02`、`02.06.02.02.63`）
  - `UDEF`：Errors 段 "An error is generated if you attempt to undefine pins while the
    sequencer is in the run or the break state"
  - `CONF`：Errors 段 "An error is generated if you attempt to configure pins while the
    sequencer is in the run or the break state"
  - `PALS`：Errors 段 "The sequencer is in RUN or BREAK mode."
  → 约束页种子：`[[pin-config-requires-sequencer-off]]`，关联 `[[sqst]]`。
- **测试不能正在运行**。文档事实，`02.06.03_Pin_configuration_setup_commands.md` 章首
  Note（同文见 `02.06.03.01.01_Introduction.md`）：

  > Note The firmware does not accept any configuration changes while a test is running.

  → 约束页种子：`[[pin-config-locked-during-test]]`。
- **多 site 的顺序**：先定 site 1，再 `PSTE`，再 `PALS`（文档事实，`02.06.03.01.09`：
  "Define the pin configuration for site 1 (which always exists) → Use the PSTE command to
  define the required number of sites → Use the PALS command to assign channels to the pins
  of the new sites. All the other configuration data will be shared with site 1."）。
- **`PALS` 要在任何其他 setup 命令之前**（文档事实，`02.06.02.02.173` 原文："Note that
  PALS must be used before any other setup command (including CONF)"）。
  推断：这条约束说的是「对该 site 的其他 setup」——因为 site 1 的 channel 是 `DFPN` 定的，
  而 `PSTE`/`PALS` 又必须在其它 setup 之前；两条合起来，多 site 配置应当放在整个配置的
  最前面（在 site 1 的 `DFPN` 之后、`CONF` 之前）。→ 约束页种子：`[[pals-before-other-setup]]`。
- **跨卡 ganging 之前必须先用 `DDIC` 使能连接**（文档事实，在 `DFPN`、`DFPS`、`PALS`
  三处重复）。→ 约束页种子：`[[cross-card-ganging-requires-ddic]]`，关联 [[ganging]]。
- **依赖指向 `[[project]]`**；本阶段是 `[[level]]` / `[[timing]]` / `[[pattern]]` 的前置
  （见「下一步」）。

## 涉及对象

层级标注：`L1`=固件/setup 命令，`L2`=C++ Test Method API，`L3`=外部控制，`file`=文件格式，
`gui`=GUI 工具。对象页多数尚未建立，wikilink 即待建清单。

**L1 — 定义型命令（本阶段的主体）**

- `[[dfpn]]` `L1` — 给数字 channel 或 DC Scale channel（PMU 模式）分配 pin 名与 pin 号；
  也是 ganging 的入口（channel list）。
- `[[conf]]` `L1` — 给已定义的 pin 设类型（I/O/IO/DC/OFF）与工作模式（F160/FAST/STDDIFF/
  FASTDIFF/CMON/DCSIGNAL/POWER），按 mode context 生效。
- `[[ctxt]]` `L1` — 定义/删除 mode context；新 context 是 DEFAULT 的副本。
- `[[dfps]]` `L1` — 把 DPS channel 或 DC Scale channel（DPS 模式）绑到器件 pin，并给极性；
  也是 DPS 侧 ganging 的入口。
- `[[dfgp]]` `L1` — 定义固定 pin 组（类型 I/O/DC/X）。
- `[[dfge]]` `L1` — 定义表达式型 pin 组（集合运算 `+ * -`）。
- `[[dfpt]]` `L1` — 定义 port（一组可独立跑不同 timing / 独立 sequencer 程序的 pin）。
- `[[dfpr]]` `L1` — 定义 pin alias（alias set ↔ package pin name）。
- `[[dfut]]` `L1` — 给 utility line 分配符号名与方向（W/R/RW，以及安全线/全局关机线关键字）。
- `[[dfup]]` `L1` — 定义 utility purpose（一组 utility line + 各自标准输出状态）。
- `[[pssl]]` `L1` — 给 DPS power pin 与 DC signal(PMU) pin 设电压/电流安全限值。
- `[[dfpc]]` `L1` — 给 pin 挂注释（Predependencies：pin 必须已由 `DFPN` 定义）。
- `[[vpin]]` `L1` — 定义虚拟 pin（不接 pogo，只用于记录结果；不能进 port 或 group）。
- `[[pste]]` `L1` — 声明配置多少个 site。
- `[[pals]]` `L1` — 给 site>1 的每个 pin 分配 channel。
- `[[udef]]` `[[udps]]` `[[udgp]]` `[[udpt]]` `[[udpr]]` `[[udut]]` `[[udup]]` `[[udvp]]` `L1`
  — 各自的 UnDefine 命令，成对出现。
- 查询：`[[dfpn]]?`、`CONF?`、`CTXT?`、`DFPS?`、`DFGP?`、`DFGE?`、`DFPT?`、`DFPR?`、
  `DFUT?`、`DFUP?`、`PSTE?`、`PALS?`、`PSFC?`、`PACT?`、`PQFC?` `L1` — 都在各自命令页里。

**L1 — 多 site 控制（本阶段只做"定义"，运行期用同一组命令）**

- `[[psfc]]` `L1` — 设置 setup focus：决定后续 setup 命令改哪些 site 的数据。
- `[[pqfc]]` `L1` — 设置 query focus：唯一能查 setup data / 看结果的 site。
- `[[pact]]` `L1` — 激活/屏蔽 site（ACTIVE / MASKED）。
- `[[stme]]` `L1` — site match function（ON/OFF/AUTO/FAST），决定各 site 是同时启动还是
  依次错开启动。
- `[[upas]]` `L1` — 给 site>1 的同一 utility purpose 指定不同标准状态。

**GUI**

- `[[pin-configuration-tool]]` `gui` — 覆盖本阶段全部操作的编辑器族。
- `[[digital-pins-editor]]` `gui` — 数字 pin 与 DC Scale(PMU) pin 的表格（Name/No/Type/
  Mode/Scaling/HW/Connection Set/Comment/Tester Channel）。
- `[[dps-pins-editor]]` `gui` — DPS pin 表格（Name/Pol/C[uF]/HW/Comment/Tester Channel）。
- `[[utility-pins-editor]]` `gui` — utility pin 的名字、方向、settling time、channel。
- `[[utility-purpose-editor]]` `gui` — 选 utility line 组成 purpose，逐 site 设 1/0/X。
- `[[pin-group-editor]]` `gui`、`[[port-editor]]` `gui`、`[[alias-set-editor]]` `gui`、
  `[[dc-scale-limits-editor]]` `gui`、`[[ground-sense-editor]]` `gui`。

**file**

- `[[pin-configuration-file]]` `file` — 本阶段的主产物，见「产物」。
- `[[pin-configuration-master-file]]` `file` — 把 pin 配置拆成 package file + alias files 后
  再由 Setup Management Tool 组装。

**辅助查询命令（验证用）**：`[[chin]]`(CHIN?)、`[[gctx]]`(GCTX?)、`[[hwty]]`(HWTY?)、
`[[pfnd]]`(PFND?)、`[[prlt]]`(PRLT?) —— `L1`，各自一句话见「验证」。

### 归属判定（本页与相邻 stage 的边界）

不是文档事实，是本次建页时的判断，写在这里供维护者复核：

- `02.06.04_Routing_Setup_Commands`（`DSCP` / `SRPR` / `UDRS`）：**不归本阶段**。
  推断：routing set 是运行期切换 DUT 板走线的机制，`DSCP` 是 sequencer memory 预留
  （且"每次调用都会清空 Sequencer Memory"，属于系统准备动作）。虽然 `DSCP` 出现在
  `02.06.03.02_List_of_configuration_commands.md` 这份列表里，但章首页
  `02.06.03_Pin_configuration_setup_commands.md` 自己的九组分组**不含** `DSCP`——以分组为准。
- `02.06.08_Relays_and_Control_Commands`（`RLYC` / `PSST` / `SQST`）：**不归本阶段**，
  归 `[[run]]`。但本阶段必须知道它的存在：`UDEF` 与 `CONF` 两页的 Note 都明写这两个命令会
  **打开**指定通道的 AC 继电器（pin electronics ↔ DUT）与 DC 继电器（DC rail ↔ DUT），
  要用 `RLYC` 重新闭合（`02.06.08` 的 connect 序列是 `RLYC AC,OFF,...` → `PSST ON` →
  `SQST BRK`）。
- `02.06.12_Utility_Line_Commands`：**拆分**。定义类（`DFUT`/`DFUP`/`UDUT`/`UDUP`/`UPAS`）
  归本阶段；运行期访问类（`UTST`/`UPST`/`UTOT`/`UTIN?`/`UTIX?`/`UTTI`/`UPTI`/`UTSC`/`UPOW`）
  归 `[[run]]`（`UPOW ON` 文档还要求"整个 testflow 执行期间只发一次"）。
- `02.03_DUT_board_design_reference` 一族（`DUT_interface_layout`、Utility lines、
  pogo pin assignment）、`02.05_Test_Head_Cards`（通道板卡）、`02.02_*`（Test heads、
  Card compatibility、PS1600 AWG、XPS256 overview）：**不归本阶段**。推断：这三块是
  **规格/硬件设计资料**，回答"这个 channel 在哪、那块卡有什么能力"，不回答"这一步该做什么"。
  它们在本阶段的作用是**查表输入**（channel 号、utility block 号、ganging 限制），
  已在「前置条件」「涉及对象」「L1」里按需引用。
- `DDIC`：**边界，倾向归本阶段**。它定义 DUT 板 trace、是跨卡 ganging 的前置，且出现在
  pin 配置文件的示例里；但它是电气设计规则的一部分。建议建对象页时标 `stage: pin`，
  并在 `[[ganging]]` 概念页里展开。


## L1 — Firmware / Setup Command

命令分组照抄章首页 `02.06.03_Pin_configuration_setup_commands.md` 的九组，不重排。

### 1. 数字 pin

`DFPN`（分配 pin 名）、`CONF`（设类型/模式）、`UDEF`（撤名）。

```
> DFPN 10101,"1",(Clock)
> DFPN 10102,"2",(D0)
> DFPN? (@)
< DFPN 10101,"1",(Clock)
< DFPN 10102,"2",(CD0)
> CONF IO,F160,(D0,D1)
> UDEF (Q3)
```
（示例逐字取自 `02.06.02.02.63_DFPN` 与 `02.06.02.02.31_CONF` 与 `02.06.02.02.295_UDEF`。）

`channelNo` 是 5 位：前 3 位 pogo block（首位 1–4；P-/Ce-/C-model 为 1–2；第 2、3 位
01–32），后 2 位 01–16。`pinName` 长度上限 16（32-bit SmarTest）/ 64（64-bit）。

### 2. Mode context

`CTXT` + `CONF`。

```
> CTXT? ALL
< CTXT DEFINE,"DEFAULT"
< CTXT DEFINE,"differential"
< CTXT DEFINE,"PdrvNPrcv"
```
（取自 `02.06.02.02.35_CTXT`。）

文档事实（`02.06.03.01.03`）：类型与工作模式**永远针对某个 mode context**；不指定时
落到 `DEFAULT`。同一个 pin 在不同 context 下可以有不同的方向与模式。

### 3. DPS pin

`DFPS` + `UDPS`。

```
DFPS 11,POS,(Vee)                     -- 外置/编号式 DPS channel
DFPS (10101, 10102),POS,(vee)         -- DC Scale 通道 ganging（逗号写法）
DFPS (10101-10102),POS,(vee)          -- 同上，区间写法
UDPS (Vee)
```

DC Scale 通道只允许 `POS`（文档事实：`DFPS` 参数页 "For DC scale channels, only POS is
allowed." / "NEG is not allowed for DC Scale channels."）。跨卡 ganging 的完整例子：

```
DDIC CONN, (104GO, 105GI)
DFPS (10403, 10404, 10501, 10502),POS,(vee)
```

### 4. DC Scale pin

`DFPN` / `UDEF` / `DFPS` / `UDPS` / `PSSL`。

关键分工（文档事实，`02.06.03.01.04`）：**DC Scale 通道的 PMU 模式用 `DFPN` 命名，
DPS 模式用 `DFPS` 命名；工作模式由此完全确定，不能用 `CONF` 改**（`CONF?` 只用于查询
模式）。这一点是「数字 pin / DPS pin / DC Scale pin」三类资源最容易混的地方。

```
PSSL OFF,OFF,OFF,OFF,(DPS_1)
PSSL -2,5,0.5,0.5,(DPS_2)
PSSL -1.5,3,0.5,0.5,(SIG_1A)
```

`PSSL` 的 `pin_list` 同时接受 `DFPS` 定义的 DPS power pin 和 `DFPN` 定义的 DC signal
(PMU) pin。默认全部 OFF。部分卡（DPS128/64、XPS256、UHC4T）另有硬件侧限值检查。

### 5. Utility line

`DFUT` / `UDUT` / `DFUP` / `UPAS` / `UDUP`。

```
DFUT 16504,w,(filter)
DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
UDUT (@)
UDUP (@)
```

`setting` 是逐 channel 的字符串：`0` = 写通道拉高（高阻），`1` = 拉低，`X`/`x` = 不动作；
**字符数必须等于 channel list 的长度**。`util_name` / `purpose_name` 上限 16 字，不得含
空格或 `# ; ( ' ' ) ? @ ,`。

多 site 差异化（取自 `02.06.02.02.304_UPAS` 的官方示例）：

```
> DFUP (101,102,103,104),"11XX",(AWG_CNCT)
> UPAS 2,"XX11",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "11XX", (AWG_CNCT)
> PSFC 2
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "XX11", (AWG_CNCT)
```

文档事实（`02.06.03.01.08` Note，`02.06.12.01` 复述）：`DFUP` 设的标准状态**只发 `FLSH`
不够**，必须先用 `UPST` 选中、再 `FLSH` 才真正下载到硬件；`UTST`/`UPST`/`UPTI`/`UTTI`
都是被 `FLSH` 缓冲的。

### 6. Utility DC pin

`CONF` / `DFPN` / `PALS`。utility DC channel 是三位的 utility block 号（用 utility line
block + 164；EXA Scale 第二块 utility 卡 + 264 得到 264 起），例：utility block 4 → 168。
文档事实（`02.06.02.02.63_DFPN`）：硬件上是 4 个 utility DC channel（DC-force、DC-sense、
ground-sense、guard），但因为成组引用，**一个 pin 名就够**。SmarTest 7.10.2 起支持。

### 7. Pin group 与 port

`DFGP` / `UDGP` / `DFPT` / `UDPT`。

```
DFGP O,(Q0,Q1,Q2,Q3),(outputs)
DFGP X,(SI1,SI2,SO1,SO2),(SCAN)
DFGE O,"SCAN * OUT",(SCAN_OUT)
DFGP? (SCAN_OUT)
< DFGP O,(SO1,SO2),(SCAN_OUT)
UDGP (Qout)
DFPT? (port_1, port_2)
UDPT (port_1)
```

（DFGE 示例取自 `02.06.03.01.06_Defining_pin_groups.md`。）

- 固定组类型：`I` / `O` / `DC` / `X`；表达式组类型：`I` / `O` / `IO` / `DC`。
- 表达式文法：pin 名或组名是合法表达式；`ex1 + ex2`（并）、`ex1 * ex2`（交）、
  `ex1 - ex2`（差）仍是合法表达式。
- 查成员用 `DFGP?`，`DFGE?` 返回的是定义表达式本身。
- 文档事实：`DFGP` **不做类型合理性检查**——把 o pin 加进 I 组固件不报错，只是后续对该组
  操作时只处理符合组类型的 pin。
- port 的约束（`02.06.03.01.07`）：port 名不能与 pin/pin group 同名；port 定义等价于固定组
  定义，**不支持表达式型**；port 没有类型，但每个 port 都可当 pin group 用。port 与 group
  都不能含模拟仪器 pin 和 DPS 通道。
- 最大组数 2400；同名复用会把新 pin 追加到原组。

### 8. Pin alias

`DFPR` / `UDPR`（SmarTest 6.5.2 新增）。

**往里加**（`02.06.02.02.64` Example 5）：

```
DFPR "TRANS","CLK",(CP)
```

**查出来的是这样**（同篇 Example 1：输入 `DFPR? DEF,(@)`，文档写「returns」）：

```
DFPR "FUNC","CLK",(CP)
DFPR "TRANS","Read",(S0)
```

**删**（`02.06.02.02.297_UDPR` 的三个例子，各删一层）：

```
UDPR "FUNC","CLK",(CP)
UDPR "FUNC","",(@)
UDPR "@","",(@)
```

> ⚠️ **这段初版是错的**（2026-09-18 改）。初版把「加 / 查返回 / 删」六行**混在一个块里**，
> 还给「返回」的行**加了我自己发明的 `<` 前缀**——**语料里没有任何文档用 `<` 表示返回**
> （全语料搜过，`<` 只出现在 `< 70% R. H.` 这类规格里）。
> 代码块本身就暗示「这是原文」，**再叠一个自造符号，读的人无处可查**。
> 现在按原文的三处例子分开列，**输入与返回的区分用文字说，不用符号编**。

文档事实（`02.06.02.02.64`）：使用 `DFPR` 前，**package pin name 必须已在 Pin Setting
Editors 里定义**；否则报错。`DFPR? ALL,...` 对没有 alias 的 pin 返回 package pin 名，
`DFPR? DEF,...` 只返回已定义 alias 的。

### 9. 多 site setup

`PACT` / `PALS` / `PQFC` / `PSFC` / `PSTE` / `STME`。

```
PSTE 3
PSTE? STR
< PSTE "101"                 -- 配了 3 个 site，只有 1 和 3 可用于测试
PALS 2,10201,,(Clock)
PALS 2,10202,,(D0)
PSFC "11111110"              -- 8 个 site，取消最后一个 site 的 setup focus
PQFC 2
PACT ACTIVE, 1
PACT MASKED, 2
STME AUTO,
STME?
< STME ON,
```

文档事实（`02.06.03.01.09`）：`PSTE` 声明的是**配置**了多少 site，实际可用于测试的可能更少
（某 site 用的 channel 被 MCDIgnore 文件禁用时该 site 不可用）；用 `PSTE? STR` 查。

`PSFC` 的语义要点（`02.06.02.02.191` 原文）：
- 只影响**遵守 setup focus 的命令**——timing 与 level setup 命令遵守；**大多数 vector
  setup 命令不遵守**（`VECD`/`VECC` 除外）。
- 默认所有 site 都有 setup focus。
- 文档 CAUTION：直接用 `PSFC` 可能导致 Site Control 窗口显示的 active/inactive 状态与实际
  不符，进而让"以为已停用"的 site 被 site control 固件命令改动，产生不良后果甚至损坏。
  文档建议：site control 尽量走 Site Control 窗口或 test method API，而不是裸 `PSFC`。
- `PSFC` 与 `PSTE`/`PACT`/`PQFC` 的 Errors 段都写着：**若某个 site 的 pin 没有全部由
  `PALS` 分配 channel，就报错**。

`STME` 的选择规则（`02.06.02.02.250` + `02.06.03.01.10.04`）：
- pattern 里有 match loop → 要 `ON`（各 site 独立判定 match）。
- 多个 site 共用同一数字 channel 去触发共享模拟模块 → 要 `OFF`（同时启动）。
- 两者同时存在时**不存在最优选择**（文档原话："an optimal selection is not possible"）。
- `AUTO` 是默认：检查配置里有没有共用的数字 channel，有则 OFF，无则 ON。
- 文档 CAUTION：跨 site 共享 BADC 时必须关掉 site matching。
- **超过 255 个 site 时 site match 必须为 off**，否则报错。

### 10. 本阶段内但不在九组里的命令

- `DFLV`（默认电平）——必须在 `*RST` 之后、pin 配置之前；它只把默认值存进表，pin 配置时
  无其他 level setup 信息才真正下发到硬件。
- `DFPC`（pin 注释）——Predependencies 明写"pin 必须已由 `DFPN` 定义"。
- `VPIN` / `UDVP`（虚拟 pin）。
- `CHIN?` / `HWTY?` / `GCTX?` / `PFND?` / `PRLT?` —— 见「验证」。
- `DDIC`（定义 DUT 板 trace，跨卡 ganging 的前置）——归属见文末「归属判定」。

## L2 — Test Method API

本阶段在 C++ test method 里**基本没有对应物**：pin 配置是 setup 期产物，运行期只能引用
pin 名/组名，不能改配置。语料里能找到的相关 API 如下（都不是"配置 pin"，而是"消费 pin 配置"）：

- `[[pin-utility]]` `L2` — 把 pin list（含 pin group 名）展开成具体 pin 名。文档明写它的
  前提是"all pins to be tested are defined using the Pin Configuration tool"，也就是说它
  直接消费本阶段的产物。
- `[[set-utility-lines]]` `L2` — 运行期设 utility line / utility purpose 状态，最多 512 条；
  名字取自 Utility Pins editor / Utility Purpose Editor 的定义。仅 UTM 可用。
- `[[get-utility-lines]]` `L2` — 读 utility line 状态；仅 UTM 可用。
- `[[flex-relay]]` `L2` — 运行期统一控制数字 channel 继电器与 utility line 驱动的用户继电器。
- `[[hw-state]]` / `[[hw-pin-state]]` `L2` — 只读查询指定 pin 的硬件状态（`HW_STATE::pin()`
  返回 `HW_PIN_STATE`；用前必须先调 `HW_STATE::getStatus()` 取硬件数据）。
- `[[pin-property-monitor]]` `L2` — 打印 pin 属性状态，偏调试。

**"在 C++ test method 里改写 pin 配置"这一类 API：文档未覆盖。**

## L3 — 外部控制

- **SmartShell**：文档事实（`02.15_SmartShell`）——它是 SmarTest 的外部脚本接口，但
  Functional changes 明写 "Introduced in SmarTest 8.2.5"。本 wiki 面向 **7.10.3**，
  **该接口在 7.10.3 下不适用**。（文档本体只有 PDF：Quick Start / User Guide /
  Command Reference。）
- **多 site 的 tpi 接口**：`PACT` 与 `PQFC` 两页都带 CAUTION——"This command implements the
  tpi interface for multisite testing. Use the tpi call instead of this firmware command.
  This is described in the manual Test Flow Programming in C." 文档事实是这个 CAUTION 存在；
  **tpi 调用的具体签名在本语料里没有**（指向另一本手册），不臆造。
- **HVM**：语料里的 HVM 全部指 `CONF` 的 `HV` 选项与 pin 的 HV 模式（"This command does not
  support pins in HV mode" 等），**不是外部控制接口**。
- **pin 配置本身的 L3 接口：有，两处。**
  - **`DataManager`（[[tpi-program-routines]]，`02.09.01.09.02`）**：文件标识里
    `dm_config` = pin configuration setup 文件、`dm_attrib` = pin attribute setup、
    `dm_catr` = channel attributes，配 `dm_load` / `dm_save` / `dm_merge` /
    `dm_copy_in` / `dm_delete` 五个操作。文档自述该接口是
    「the mirror image of the interactive interface」——**即 Pin Configuration GUI 的程序化镜像**。
  - **`HpFwTask`（`02.09.01.09.21`）**：文档事实是「allows direct access from a C program to
    the system hardware **at firmware level**」——即从 C 程序直接下发 pin 固件命令。
    注意同篇的注意事项：**它不像 test method API 那样自动处理 site focus**；
    不先下发 site focus 命令时，setup 类命令取默认 focus（通常所有 site），
    而查询类命令只返回默认 focus site 的结果，**于是各 site 的结果看起来一模一样**。

  调用方式见 `02.09.01.09` 章（TPI Program Routines）：在外部客户端程序里链接 TPI 例程，
  与 `02.09.01.14` 的 C++ 外部客户端是两条不同的通道。

> **改判记录。** 本页上一版把上面这条写成「文档未覆盖」，并另写了一句
> 「**tpi 调用的具体签名在本语料里没有**（指向另一本手册），不臆造」。
> **那一句是错的**：`02.09.01.09` 全章 31 篇就是 TPI（Test Program Interface）例程的签名，
> 例如 `02.09.01.09.14_GetSiteInFocus` 就有完整签名
> `VOID GetSiteInFocus(INT32 *site_in_focus);` 和用例；
> `02.06.10.01.07.01_Example` 也明写 SetSiteInFocus 属 "TPI (Test Program Interface)"。
> 正确说法是：**PACT / PQFC 的 CAUTION 指向的那本《Test Flow Programming in C》手册
> 不在本语料**，但**同样的 TPI 例程在本语料的 `02.09.01.09` 章里有签名**。已改。

**横切入口**（session / execute / `isPass`）见 [[test-suite-control-api]]——它不由本阶段独占，
本页不复述。

## 产物

- **pin configuration file**（文档事实，`02.08.04.18.04_Pin_configuration_file.md`）：
  位置 `<device_dir>/configuration`；内容是**一串与 Pin Configuration tool 里所设参数
  完全对应的固件命令**，首行为 `hp93000,config,0.1`。
  文件后缀是 `.cfg`（`02.09.02.03.02_File_and_parameter_settings.md` 举例 `mypins.cfg`）。

  最小完整示例（取自 `02.06.03.01.12_Pin_Configuration_Example.md`，注释是文档加的，
  文档同时明确 **固件命令文件本身不能写注释**）：

  ```
  hp93000,config,0.1
  DFPN 10101,"13",(CP)
  DFPN 10102,"7 ",(D3)
  DFGP I,(P3,P2,P1,P0,S2,S1,S0),(preset)
  DFGP O,(NQ3,NQ2,NQ1,NQ0),(NQ_out)
  CONF I,F160,(CP,D3,D0_NCET,MR,NCEP,P3,P2,P1,P0,S2,S1,S0)
  CONF O,F160,(NQ3,NQ2,NQ1,NQ0,NTC,Q3,Q2,Q1,Q0)
  RDIV 50,(NQ3,NQ2,NQ1,NQ0,NTC,Q3,Q2,Q1,Q0)
  DFPS 13,POS,(Vee)
  PSLC 4.7,(Vee)
  ```

  多 port 配置则在 `DFPN` 之后用 `DFPT` 定义 port（同上文件）。文档另注：
  **可以用文本编辑器直接写这个文件**，不必经 GUI。

  格式尾部常见 `NOOP "<version>",,,`（见 `02.08.04.18.04` 与 `02.08.04.18.05` 示例）。

- **pin configuration master file**（`02.08.04.18.05`，SmarTest 6.5.2 引入）：
  首行 `hp93000,config_master_file,0.1`，第二行 `testerfile: <tester_file_name>`，
  之后 `Package: <package_file.cfg>` 与 `<alias_set_name>: <alias_file.cfg>`。
  Setup Management Tool 用它把多个分文件组装成一个 pin 配置；组装前会校验四条规则
  （site 数一致、alias 文件的 channel 都出现在 package 文件里、除 DEFAULT 外 context
  不重复、package 文件里 I/O 方向的约束），违反则中止并报错。
  **master file 支持 `#` 行注释**（与 config 本体不支持注释不同）。

- **备份**：STPM 的 `enable_backup` 打开时，修改后的文件会在同目录的 `back/` 子目录留一份
  带时间戳的副本，例如 `<device_directory>/configuration/back/mypins_121102_214323.cfg`
  （`02.09.02.03.02`）。

- **CSV**：可从 CSV 导入/导出 pin 配置（`02.08.04.18.02.02`，SmarTest 6.5.0 引入；
  导入前要求"CSV 文件存在"且"已加载一个新的空 pin 配置"）。

- **MTP 侧另有 `.pin` 文件**（`02.12.03.03.09.01_Pin_configuration_file.md`）：
  扩展名 `.pin`，可被 Pin mapping file 用 `using pinconfig` 引用。推断：这是 Memory Test
  Plus 自己的 pin 配置文件，与 `02.08.04.18.04` 描述的 `<device_dir>/configuration/*.cfg`
  不是同一个产物，不要混为一谈。

**三层对照表见 [[mapping-pin]]** —— GUI 操作 ↔ 文件 ↔ L1 命令 ↔ L2 API ↔ L3 接口 的按目的对照
（`wiki/mappings/mapping-pin.md`；证据分三档写明，**`?` 与 `—` 不同义**：前者是「本页没找到证据」，
后者是「这一层不存在这个对应物」）。

## 验证

**GUI 侧**（`02.08.04.18.02.05_Applying_pin_configuration_data.md` + `02.08.04.18.03.12_State_indicator.md`）：

- 改完数据后 Square State Indicator 变黄（编辑器数据 ≠ 硬件数据）。
- 在 Test Program Explorer 里对 pin 配置文件右键 **Apply All**（或对单个组件 Apply），
  会在 `Confirm Apply` 窗口要求确认——文档明写该确认窗**只在 apply pin setting data 或
  整个 pin 配置文件时**出现。
- Apply 之后 Square State Indicator 变**绿** = 数据已下载到硬件。
- 保存后文件名后面出现 Asterisk State Indicator = **文件与硬件不一致**。
- 下一步动作是"Save the pin configuration file"。
- 多 site：给多个 site 分了**完全相同的数字 channel** 时，通道单元格背景变黄，文档要求
  仔细检查。

**固件查询侧**（各命令页的 query 形式）：

- `DFPN? (@)` — 列出所有由 `DFPN` 定义过的 pin 及其 channel 与 pin 号。
- `CONF? ("context"|ALL,) {(pinlist)}` / `CONF? (@)` — 列出 pin 的类型与工作模式；
  对 DC Scale pin 会返回 `DC,DCSIGNAL`（PMU 模式）或 `DC,POWER`（DPS 模式）。
- `CTXT? ALL` — 列出所有已定义的 mode context。
- `DFPS? {(pinlist)}` — 列出 DPS 通道、极性与 pin 号。
- `DFGP? (group)` — 列组成员；`DFGE? (group)` — 返回定义表达式；
  `DFPT? (portlist)` / `DFPT? (@@)` — 列出 port 定义；`DFPR? DEF|ALL,(...)` — alias 查询。
- `DFUT? (@)` / `DFUP? (@)` — utility line / utility purpose 定义查询。
- `PALS? {site},{(pinlist)}`（`ALL` / `PEND`）— 查各 site 的通道分配。
- `PSTE?`（site 数）/ `PSTE? STR`（哪些 site 真正可用）/ `PSFC? [STR]` / `PACT? [STR]` /
  `PQFC?` — 多 site 状态。
- `GCTX? {setup_type},[setup_comp]` — 查 timing/level/wavetable/label 等组件当前用的
  mode context（`TIM` / `LEV` / `WAVE` / `LBL` / `SPCF` / `CURR`）。
- `PFND? [PRT|DIFF,] {(pin)}` — 查某 pin 属于哪个 port；`DIFF` 则返回其差分对。
- `CHIN? {channel_nr|ALL}` — 查 channel 信息（类型、物理位置、board 号、clock board 等）。
- `HWTY?` — 查机台/测试头/DUT 接口类型，例 `HWTY VS,TH_4CC,SOC`。
- `PRLT?` — 一次取回所有 site 的全局 pass/fail（不必只取 query focus 的 site）；
  文档提醒它会被 `CSAS` / `PSAS` 失效，建议紧跟在功能测试之后、`CSAS`/`PSAS` 之前用。

**文档未给出**"配置正确性"的自动校验方法——没有校验命令能判断通道分配是否符合 DUT 板
实际接线；只能靠上面这些查询比对 + GUI 的黄色高亮。

## 常见错误

1. **测试运行中改配置** → 报错。出处：`02.06.03` 章首 Note；`02.06.03.01.11_Errors` 首条
   即 "a test is running"。排查入口：先 `SQST OFF`。
2. **sequencer 不在 OFF 状态** → `DFPN` / `UDEF` / `CONF` / `PALS` 都会报错。
   出处：`02.06.03.01.11_Errors` 列 "the sequencer is not in the OFF state"；各命令页
   Errors 段。关联 `[[sqst]]`、约束 `[[pin-config-requires-sequencer-off]]`。
3. **某个 site 的 pin 没有全部由 `PALS` 分配通道** → `PSFC` / `PSTE` / `PACT` / `PQFC`
   报错。出处：四页 Errors 段同一句话。
4. **改完 pin 配置立刻保存其他 setup** → 覆盖出无效数据。出处：`02.08.04.18.02.06` 的
   CAUTION 原文——"Setup data becomes invalid when there is a change in the pin
   configuration. Never save the setup (except the pin configuration) immediately after
   modifying the pin configuration!"。正确顺序：Apply → 保存 pin 配置 → **重新加载**其他
   所有 setup。
5. **通道号/资源不合法** → `02.06.03.01.11_Errors` 列出的其余条目：programmed resources
   未安装、已被占用、系统里没装 device power supply、resistive divider 值超范围。
   `DFPN` 另列：channel 号无效 / 未安装 / 已被分配 / pin 已定义 / pin 名已被组名占用 /
   DC Scale ganging 时并非所有通道都是 DC Scale。
6. **`DFPN` 与 `DFPS` 用错**（DC Scale 通道）→ 工作模式由命名命令决定，PMU 用 `DFPN`、
   DPS 用 `DFPS`，`CONF` 改不了。用 `CONF?` 复核返回值是 `DCSIGNAL` 还是 `POWER`。
7. **`DFPS` 的 `NEG` 用在 DC Scale 通道上** → 不允许（只有 `POS`）。
8. **`DFUP` 设了标准状态但没生效** → 只发 `FLSH` 不够，必须先用 `UPST` 选中再 `FLSH`。
   出处：`02.06.03.01.08` Note 与 `02.06.12.01`。
9. **`UPAS`/`DFUP` 的 setting 字符串长度与 channel list 不等** → 报错（两页 Errors 段都列）。
10. **同一个 utility purpose 用于多个 site 但要求并行执行** → 文档事实：
    "you can use the same utility purpose for different sites only if the sites are executed
    serially"（`02.06.12.01`）。
11. **裸用 `PSFC`** → Site Control 窗口显示与实际不一致，可能导致"以为已停用"的 site 被
    site control 固件命令改动。出处：`02.06.02.02.191` CAUTION。规避：走 Site Control
    窗口或 test method API。
12. **多 site 共用同一数字 channel 触发共享模拟模块却没关 site match** → 触发信号按编号最大
    的 site 的 timing 产生，模拟测量时序错误。出处：`02.06.03.01.10.04`。设 `STME OFF`。
13. **site 数 > 255 且 site match 为 on** → 报错。出处：`02.06.03.01.10.04`
    "Testing with high site counts"。
14. **`DFGP` 把不匹配类型的 pin 加进组** → 固件不报错（不做合理性检查），但后续对该组操作
    只处理符合组类型的 pin；GUI 侧 `02.08.04.18.03.02.02_Incompatible_pin_groups.md` 另列
    timing / level / vector setup 各自的组兼容性规则（如 level setup 不允许 O 与 io 混组）。
15. **组名与 pin 名冲突** → `DFGP` Errors："The intended group name is already being used
    for a pin."；`DFPN` Errors 也有反向的一条。
16. **在固件命令文件里写注释** → `02.06.03.01.12` Note 明说不可能（示例里的 `--` 注释只是
    文档为了讲解加的）。但 **master file 可以用 `#` 注释**。
17. **两份文档对"所有组的 pin 总数上限"给的值不同** —— 冲突记录（按 schema §10
    并列记录，**不自行裁定**）。三个来源，两个数：

    | 来源 | 值 | 原句 |
    |---|---|---|
    | `02.06.02.02.60` / `02.06.03.02.05`（`DFGP`，**同一篇被投放两次**） | **1,843,200** | "max. number of pins in all groups is 1843200" |
    | `02.06.02.02.59` / `02.06.03.02.04`（`DFGE`，同上） | **1,843,200** | 逐字相同 |
    | `02.08.04.18.03.02.01_Rules_for_defining_groups` | **1,228,800** | "The maximum number of the fixed groups is 2400. The maximum number of pins in all groups is 1,228,800." |

    两者**一致**的是「最大组数 2400」。

    **推断（未证实）**：1,228,800 = 2400 × 512，1,843,200 = 2400 × 768，比值 3:2——
    **不是笔误的量级**（笔误该差一位或差十倍）。02.08 那句把 2400 明确限定为
    *fixed groups*，而 `DFGE` 是按表达式（`I`/`O`/`IO`/`DC`）定义组、**一个 pin 可属多组**。
    若一个数「固定组」、另一个数「含表达式组的全部组」，两句可同时成立。
    推断链到此为止——**语料里没有一句话证实它**。

    **存疑，需上机确认。** 本条不据文档推断任何实际机台的行为。
18. **把 `HVM` 当成外部控制接口** —— 语料里的 HVM 全部是 `CONF` 的 `HV` 选项相关，
    不是接口名。

## 下一步

`[[level]]`。

原因（文档事实）：`02.06.03` 章首明写 "It is impossible to define level, timing, or vector
parameters without the pin configuration"；且 `DFLV` 的默认电平在 pin 配置时被真正下发到
硬件。pin 配置定完之后，电平才有作用的对象，因此下一步是 Level 电平配置，再往后是
`[[timing]]` 与 `[[pattern]]`。