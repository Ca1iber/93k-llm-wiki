---
type: stage
title: Level — 电平配置
tags: []
related: [project, pin, timing, pattern, testmethod, testflow, run, results, ctxt, level-setup-tool, spec-tool, level-spec, level-file, clamping, level-set-0]
sources:
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03_Setting_up_your_levels.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.01_Specifying_the_context_for_levels.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.02_How_to_create_an_equation_set_using_the_Equation_editor.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.03_Creating_new_specification_sets.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.04_Verifying_the_level_settings.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.03.03_Pin_Scale_5000_level_setup.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.03.03.02_Definition_of_contexts_in_level_file.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.01_Introduction.md
  - 02_System_reference/02.06_Command_Reference/02.06.05_Level_Setup_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01_Concepts_of_level_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01_Basic_concepts_of_levels.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01.01_Drive_Levels.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01.02_Compare_Levels__Thresholds.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01.03_Termination_types.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.02_DPS__Device_Power_Supply__pins.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.03_Clamping.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04_Data_Organization_of_Equation_Based_Levels.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.01_Elements_of_Equation_Based_Level_Setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02_Structure_of_an_equation_based_level_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.02_Mode_context_in_level_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.05_DPS_module.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.06_Level_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.06.02_Additional_pin_qualifier__diff.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.08_Supported_level_resources.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.03_Testing_with_equation_based_level_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.03.01_Verifying_the_level_settings.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.04_Example_of_an_equation_based_level_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05_Data_Organization_of_Fixed_Levels.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.01.03_Set_fixed_clamping_levels.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.06_Pull-down_function.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.07_Example_of_a_Fixed_Level_Setup_File.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02_List_of_level_setup_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.02_CLMP__CLMP__-__CLaMP_level.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.04_DPRL__DPRL__-__Default_PRimary_Level_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.05_DRLV__DRLV__-__DRive_LeVel.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.06_DSUS__DSUS__-__Dps_Sets_USed.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.12_LSUS__LSUS__-__Level_Sets_USed.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.13_LSUX__LSUX__-__Level_Sets_Used_eXtended.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.15_PSLV__PSLV__-__Power_Supply_LeVel.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.16_PSSR__PSSR__-_Power_Supply_Slew_Rate.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.17_RCLS__-__ReCeive_Level_Sensitivity.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.18_RCLV__RCLV__-__ReCeive_LeVel.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.19_RSET_-__ReSET.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.20_SDSC__-__Set_number_DeSCriptions.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.21_SLDO_-__Switch_Level_and_Dps_Order.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.23_SPST__-__SPecset_STatus.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.25_TERM__TERM__-__TERMination_mode.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.03_SpecValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.02.02_Changing_spec_value_in_primary_level_spec_set.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.02_CCTchangeLevelSpec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.123_LevelSetSelector.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02.14_SpecValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.06_SetupLevelSet0.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.01_Level_equation_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14_Level_setup_tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.01.04_Clamping.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.01.04.01_Pin_Scale_1600_Card.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02_Equation_based_level_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.01_The_advantage_of_using_level_setup_file_to_store_all_the_level_sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03_Structure_of_an_equation_based_level_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.01_EQNSET__Level_equation_set_header.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.03_Level_spec_set.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.09_Level_specifications.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.10_Error_Reporting.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.04_Equation_based_level_setup_example.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05_Level_setup_master_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05.01_Master_file_format_for_level_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.03_Elements_of_the_Level_Setup_window.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04_Opening_and_using_the_Level_Setup_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.05_How_to_set_the_driver_levels_for_differential_pins.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.06_How_to_set_the_driver_levels_for_single_ended_pins.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.07_How_to_set_the_driver_levels_for_DUT_inputs.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08_How_to_set_the_termination_for_DUT_outputs.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08.01_Using_the_clamp_for_termination.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08.02_Using_the_active_load_for_termination.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08.03_Using_the_cross_termination.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08.04_Using_the_bidir_receiver_termination_for_full_swing_in_fast_mode.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.09_How_to_set_the_comparator_thresholds_for_single-ended_pins.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.10_How_to_use_the_Dynamic_Driver_High_Level_Shift__v3h__feature_for_fast_mo.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.11_Working_with_level_sets_and_DPS_sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.11.01_Setting_switching_order_modes_of_level_sets_and_DPS_sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06_Level_setup_related_use_cases.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.01_Setting_up_the_Device_Power_Supply.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.02_Use_case__testing_Mixed_Level_Devices.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.02.05_Using_Automatic_Swing_Adjustment.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.01_Context_list.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.18_How_to_restore_the_equation_settings_after_you_change_them_in_the_Timing.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.md
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.md
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# Level — 电平配置

> Level 这一步定义「DUT 的每个 pin 在电气上被驱动、比较、端接、加载到什么电压/电流」，并把它们打包成可被 pattern 与 testflow 引用的 level set。

## 目的

`02.06.05_Level_Setup_Commands` 章首页把本阶段的内容面一次说清：

> 「Each channel of a channel card includes a driver, a dual level comparator, an active load, and clamps.
>
> You program these resources in the level setup. That is, you assign values to the following level resources:
> - drive levels,
> - compare levels,
> - termination modes,
> - load currents,
> - clamp levels, and
> - power supply voltage.」

**这六类资源就是本阶段的全部内容面**——本页以下所有条目都归属到这六类之一。

> ⚠️ **上面这条引文 2026-09-18 修过一次。** 原稿把原文那个**六项列表拍平成一句话**
> （去掉了每行开头的 `- `），又自作主张给六项加了粗体。**引文里的格式也是原文的一部分**——
> 拍平列表就少抄了字符，加粗则是页面的主张冒充原文的主张。现已恢复原列表逐行形态。

同一篇给出两条实现路线的定性：

> 「The easiest way to achieve this is to assign fixed values to these level resources.」
>
> 「However, this approach does not satisfy the requirements of many applications. For this reason, SmarTest also provides the more powerful equation-based approach to level setup.」

走查 `01.07.01.03_Setting_up_your_levels` 的 `About this task` 把 equation based 路线拆成两件事：

> 「The process for setting up equation based levels is **very similar** to that for setting up equation based timing. — Set up the equations for levels. — Define the specifications.」

即：**方程（equation set）** + **规格值（spec set）**两件套，与 [[timing]] 阶段同构。

数据组织方式（`02.06.05.01.04_Data_Organization_of_Equation_Based_Levels` / `.01.05_Data_Organization_of_Fixed_Levels`）：

| 路线 | 数据怎么进机器 | 状态 |
|---|---|---|
| equation based | 数据是「larger data blocks that are downloaded to the tester as a whole」 | 标准路线 |
| fixed | 「each setup element is defined by calling a firmware command」，值是常量 | **「The support for fixed level setups is discontinued with SmarTest version 7.4.1T.」** |

**两者不互斥**（文档明写，`02.06.05_Level_Setup_Commands`）：

> 「Note that fixed and equation based level setups **do not exclude each other**. You can define a fixed level setup and an equation based level setup in the same level file.」

## 前置条件

1. **Pin configuration 必须先做完。** `02.06.03.01.01_Introduction`：「Configuring pins is the first step you must take when preparing a test. **It is impossible to define level, timing, or vector parameters without the pin configuration.**」→ [[pin]]
2. **测试运行中固件不接受配置改动。** 同篇：「Note The firmware does not accept any configuration changes while a test is running.」
3. **若要用 mode context**，context 必须已在 pin configuration 里用 `CTXT` 定义（`02.06.05.01.04.02.02_Mode_context_in_level_setup`）。约束页见 [[constraint-level-mode-context-match]]；本页只讲 level 侧的用法。
4. **建 spec set 之前必须先有 equation set**，且该 spec set 必须关联到一个 equation set（`01.07.01.03.03_Creating_new_specification_sets`）。
5. **编程 level set 0 之前，level setup file 必须已 load 进固件**（`02.06.05.01.05.05_Controlling_high-Z_behavior...`）。
6. **差分 / FAST 模式必须走 equation based**（`02.06.05.01.04.02.02`）。
7. **每个 level set 必须包含 pin configuration 里定义的全部 pin 的信息**（`01.07.01.03.02`：「every level set must contain information for all pins defined in your pin configuration」）。
8. **`v3h` 相关能力要先在 Edit Device 对话框里勾上对应 capability flag**（`02.08.04.14.04.08.04` 对 fast bidirectional 的 `Before you begin` 明写这一步）。

## 涉及对象

### 文件 / 数据对象

| 对象 | 层 | 在本阶段干什么 |
|---|---|---|
| [[level-file]] | file | 本阶段主产物：`EQNSET` / `SPECS` / `EQUATIONS` / `DPSPINS` / `LEVELSET`+`PINS`，可含 `MODECONTEXT` 与 `MODULATION` |
| [[level-master-file]] | file | device 的 level 总入口，指向各 eqnset subfile 与 defines |
| [[level-equation-file]] | file | 单条 equation set 落盘的形式（`hp93000,level,0.1`；带 `USE_PROTOCOL` 时是 `.prot_lev`） |
| [[spec-set]] | L2 | 由 Spec Tool 生成的一组具名 spec 变量值（含单位），编号 1–99 |
| [[technology-file]] | file | 提供 `pulldown_in_level_set0: off` 这个开关（见常见错误 8） |

### L1 命令

| 对象 | 层 | 在本阶段干什么 |
|---|---|---|
| [[lsus]] | L1 | 设 **level set 个数**；范围 1…最大（默认 32，上限 256，由 `CONF` 定）；也可用来删多余 set |
| [[lsux]] | L1 | level set 计数的扩展形式，**system 专用**（Test Flow Optimizer 内部生成优化 level set），不要从 hpt 手工执行 |
| [[dsus]] | L1 | 设 **DPS set 个数**（默认 32，上限 256）；同样可用来删多余 set |
| [[dprl]] | L1 | Default PRimary Level sets——「used to place the level setup tool on the specified set」，`DPRL {level_set}, {dps_set}, [screen_select]` |
| [[dscp]] | L1 | Define System Control Parameter——level set 数量上限等系统参数；**所有 `UPTD?` 标志被它清零** |
| [[eqfs]] | L1 | 把 equation set / spec set **LOAD / SAVE 到文件**（如 `EQFS LEV,EQN,LOAD,"/tmp/level_equation"`） |
| [[eqsp]] | L1 | 直接 **下载 / 查询** 这些数据块（`EQSP?` 被 Test Program Explorer 用来把 setup 存成文件） |
| [[sprm]] | L1 | 把 level equation set + spec set + level set 指成 **primary** |
| [[aprm]] | L1 | 把 primary set **真正激活到硬件**（`FRC` / `CNL` 决定是否强制） |
| [[svlr]] | L1 | **运行时**改 spec 变量值并重算；也是 `DRLV`/`RCLV` 类改动落地的激活手段 |
| [[uptd]] | L1 | `UPTD {status},{flag}` / `UPTD? {status}`——查数据与 device file 是否一致（1/0）；上电或 `*RST`/`DSCP` 后全置 0 |
| [[spst]] | L1 | Specset STatus——查询状态字（是否被 `DRLV`/`RCLV`/`TERM` 等改过、是否有 range/order 违例） |
| [[sldo]] | L1 | Switch Level and Dps Order——两个 level set / DPS set 之间切换时的**先后顺序**（`FDSL` 先 DPS / `CVDL` 视升降而定），带 report 模式 `ALL`/`FLSD`/`AMBI`/`NONE` |
| [[drlv]] | L1 | fixed 路线：设 **drive levels**（driver） |
| [[rclv]] | L1 | fixed 路线：设 **compare levels**（comparator 阈值） |
| [[pslv]] | L1 | fixed 路线：设 **DPS 输出电压 / 电流限 / 阻抗模式 / settling time** |
| [[pssr]] | L1 | Power Supply **Slew Rate**（电压斜坡）；**与 `PSLV` 的 settling time / `t_ms` 互斥** |
| [[term]] | L1 | fixed 路线：设 **termination mode**（含 pulldown 参数、`l_range`/`h_range`） |
| [[clmp]] | L1 | fixed 路线：设 **clamp levels**（`vcl`/`vch`） |
| [[sqst]] | L1 | 配合 level set 0 使用（`SQST BRK` / `SQST OFF` 时 level set 0 生效） |
| [[rset]] | L1 | `RSET {LEV|DPS|FCR}`——把硬件载入该类型文件的**上电默认值**（`RSET LEV`：0 V / 50 mA / off 最小电流 / 0 ms） |

### L2 API

| 对象 | 层 | 在本阶段干什么 |
|---|---|---|
| [[level-spec]] | L2 | `LEVEL_SPEC(eqnset, specset)`——改/读 primary level spec set 的 spec 值 |
| [[primary-status]] / `Primary.getLevelSpec()` | L2 | 从 test method 里拿当前 primary 的 level spec |
| [[level-set-selector]] | L2 | `DIGITAL_OFFSET_SEARCH_TASK` / `DIGITAL_OFFSET_SEARCH_PINS` 里选 level set（7.2.1 引入） |
| [[setup-level-set-0]] | L2 | Test Method，6.5.3 引入，处理 level set 0 场景 |
| [[cct-change-level-spec]] | L2 | `CCTchangeLevelSpec(spec, value)`，CCTestMethod.hpp，7.2.0 引入 |
| [[spec-value]] / [[spec-variable]] | L2 | UTM 参数类型：spec 值怎么作为参数进出 test method |

### GUI

| 对象 | 层 | 在本阶段干什么 |
|---|---|---|
| [[level-setup-tool]] | gui | 本阶段主工具：多个 view 编 level / DPS / equation / spec，跑 Download |
| Level Equation Editor（NEdit） | gui | `Select > Edit Equations` 打开；`Shell > Generate Level` / `Shell > Generate DPS` 生成骨架，`Shell > Download` / **F8** 下发 |
| [[spec-tool]] | gui | `Select > Edit Specification` 打开；建 spec set、给 spec 变量赋值、`File > Download` |
| Test Program Explorer | gui | 保存 level setup / level equation file（**File > Save 在 NEdit 里不管用**，见常见错误 1） |
| Level Setup window | gui | 看/改各个 level set 的当前值；**在这里直接改值只临时覆盖文件**，见常见错误 2 |

### 归属判断

- **clamping 归属本阶段**：它属于六类资源里的 clamp levels，L1 是 `CLMP`，文件侧是 `PINS` 块里的 `vch` / `vcl`。**注意不要与 pin electronics 的 PMU current/voltage clamp 混淆**——后者是 PPMU/SPMU 的量程保护，另一套对象，与本页的 `vch`/`vcl` 不是同一件事（此判断为推断：两类文档走的是不同的分类前缀，正文互不引用）。
- **context（CTXT）** 归属 [[pin]]，本页只写它在 level 侧的用法与约束。
- **DPS** 归属本阶段（同在 `02.06.05` 章），但与 level set 是两套并行的编号体系，不要合并（见 L1「level set 与 DPS set 是两套」）。
- **Spec Tool** 是跨 level / timing 的共用工具，本页只写 level 侧操作。

## L1 — Firmware / Setup Command

### 路线一：equation based（标准路线）

**最小可用示例**（文档原文，`01.07.01.03.02_How_to_create_an_equation_set_using_the_Equation_editor`）：

```
EQNSET 1 "NonSpecs"
DPSPINS Vcc
 vout = 4.5
 ilimit = 1000
 t_ms =4
 offcurr = act
LEVELSET 1 "nominal"
PINS ctrl ser_in
 vil = 0
 vih = 4.3
PINS ser_out
 vol = 2.4
 voh = 2.6
```

**完整骨架**（`02.06.05.01.04.02_Structure_of_an_equation_based_level_setup` / `02.08.04.14.02.03`）：

```
EQNSET <n> "<description>"        ← 块头
[MODECONTEXT "<name>"]            ← 可选，必须紧跟 EQNSET 行
SPECS / SPECSET                   ← spec 变量定义
EQUATIONS                         ← 派生 spec（可含表达式）
DPSPINS <pin> ...                 ← DPS 模块
LEVELSET <n> "<desc>"
PINS <pinlist>
 <resource> = <值或表达式>
```

模块要素（`02.06.05.01.04.01_Elements_of_Equation_Based_Level_Setup`）：**表达式 / equation 变量 / spec 变量**三类。spec 变量与本地定义的差别就是「值由 Spec Tool 给」，例：`vih = Vcc - 0.5`。

**编号公式**（`02.06.05.02.25_TERM`、`02.07.04.01.123` 等多篇重复给出）：

- level set id：`100000 * equation_set_no + 1000 * specset_no + level_set_no`
- DPS set id：`100000 * equation_set_no + 1000 * specset_no + 1`
- **两者是两条独立编号**：同一个 specset 下 level set 用 `level_set_no`，DPS 用固定 `1`。

**容量**：

- `LSUS` / `DSUS` 的范围是 1…上限，**默认 32、最大 256**（`02.06.05.02.12` / `.02.06`）。
- equation set 号 1–99；每个 equation set 内 **最多 99 个 level set**（`02.08.04.14.02.03`）。
- 「There is a limit of **256 level sets across all equation sets**」（`02.06.05.01.04.02.06_Level_sets`）。
- level set 描述可选，**≤ 60 字符**（同上）。

**DPS 模块字段**（`02.06.05.01.04.02.05_DPS_module`）：`vout`、`ilimit`、`t_ms`（settling time）、`offcurr`、`vbump`、`vout_b`。

**差分 pin 的附加限定**（`02.06.05.01.04.02.06.02_Additional_pin_qualifier__diff`）：`PINS clkout_p@diff cadout_n@diff` 形式，配 `term center_tap`、`Vt=spec1`。**该写法在 GUI 里不可用。**

**切换 / 激活 / 运行期**：

- 选 primary：`SPRM` 把 set 指成 primary；`APRM`（可带 `FRC`/`CNL`）把它激活到硬件。文档说明 `FTST`/`RCLS`/`SQST RUN`/`PSST` 会隐式做这件事。
- 模式串切换：pattern 指令列里的 `CLEV`（change level set）与 `CTIM`（change timing set）。`CLEV` 是 pattern 侧改 level set 的手段（`02.08.04.14.02.01`）。
- 切换顺序：`SLDO {FDSL|CVDL}, [ALL|FLSD|AMBI|NONE]`；也可在 GUI 里 `Edit > Set Level Switching Order` 设，**存进 level 文件的 `GENERAL` 条目**（`02.08.04.14.04.11.01`）。
- 运行时改值：`SVLR`。
- 从文件装载：`EQFS LEV,EQN,LOAD,"/tmp/level_equation"`；另有 `EQSP` 直接下载/查询。
- 三个 set 的选择是**同时**的（`02.06.05.01.04.03_Testing_with_equation_based_level_sets`）：「you must select: one level equation set, one level set of the selected equation set, one spec set」。

**level set 0**（`02.06.05.01.05.05_Controlling_high-Z_behavior...`）：数字型 pin 在 sequencer OFF 状态下专用的一套高阻 level set。规则：

- 只能用 **fixed level setup** 定义，不能是 equation based；
- 不能做 SPRM 的 primary，且被排除在 `ALL` 之外（`TERM`/`CLMP` 里 `ALL` 表示「all existing level sets **except level set 0**」）；
- `TERM`/`CLMP` 只在其对应 sequencer 状态（BRK）下生效；
- **只支持 termination mode `OFF`（默认）、`T`、`C`、`A`**（`02.06.05.02.25_TERM`）；
- 文档给的最小写法：

```
TERM 0,A,vcom,iol,ioh,,,(@)
CLMP 0,ON,vcl,vch,(@)
```

配合 `SQST BRK` / `SQST OFF` 观察。

**pull-down**（`02.06.05.01.05.06_Pull-down_function`）：`TERM 0,OFF,NONE,,,,,,(pin_group)`，配 `SQST BRK` / `SQST OFF`；technology 侧开关 `pulldown_in_level_set0: off`。

### 路线二：fixed level setup

**文档给出的完整文件示例**（`02.06.05.01.05.07_Example_of_a_Fixed_Level_Setup_File`）：

```
hp93330,level,0.1
PSLV 1,-4.5,0.4,HIZ,10,(Vee) - set Power Supply LeVels
DRLV 1,-1700,-950,(CP,D3,D0_NCET,MR,NCEP,P3,P2,P1,P0,S2,S1,S0)-set DRiver LeVels
RCLV 1,-1300,-750,(NQ3,NQ2,NQ1,NQ0,NTC,Q3,Q2,Q1,Q0) - set ReCeiver LeVels
TERM 1,a,-800,3000,4000,I5E3,I5E3,(Q0,Q1,Q2,Q3) - set TERMination mode
```

> ⚠️ **这四行现在与原文逐字一致，初版不是**（2026-09-18 改回）：
> 初版把 pin 清单**缩写成 `(CP,D3,...)` / `(NQ3,...)`**，
> 又把 `-set` 补成 `- set`——**那是我在改文档事实**（§11）。
> 原文 `DRLV` 那行**确实是 `-set`，没有空格**，其余三行是 `- set`，**照录**。

各命令最小示例：

| 命令 | 示例（文档原文） | 备注 |
|---|---|---|
| `DRLV` | `DRLV 1,-1750,-850,(Q0,Q1,Q2,Q3)` | 「Each call of the DRLV FW command requires an **activation of the level set**」→ 用 `SVLR` 触发；**`DRLV` 置位 `SPST?` 的 bit 8** |
| `RCLV` | `RCLV 1,-1300,-750,(NQ3,...)` | 同上 |
| `PSLV` | `PSLV 1,5.2,0.5,HIZ,15,(Vee)` | 语法 `PSLV {set}, voltage, current_limit, impedance, settling_time, (pinlist)`；impedance ∈ `LOZ` / `HIZ` / `HIZ_R` / `LOZ_HIZ` / `LOZ_HIZ_R` |
| `PSSR` | `PSSR {dps_No\|dps_set_id}, rise_tm_per_v, rise_settm, fall_tm_per_v, ...` | **与 `PSLV` 的 settling time / `t_ms` 互斥**；时间值分辨率为微秒 |
| `TERM` | `TERM 1,a,-800,3000,4000,I5E3,I5E3,(Q0,Q1,Q2,Q3)` | 完整语法 `TERM {level_set_no\|level_set_id}, [term_mode], [term_pulldown,] [param_1..3], [l_range], [h_range], [hr_mode,] {(pinlist)}`；`l_range`/`h_range` ∈ `I5E3`/`I3E4`/`AUTO` |
| `CLMP` | `CLMP 1,ON,-10,5100,(Q0,Q1,Q2,Q3)` | 语法 `CLMP {level_set\|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}`；clamp_mode ∈ `auto` / `on` |

`CLMP` 硬件边界（`02.06.05.02.02_CLMP`）：PS800 低钳范围 −1800…6800，**高钳 − 低钳 ≤ 8.6 V**；**PS9G 无 clamp**。

**termination mode 全表**在 `02.06.05.02.25_TERM` 与 `02.06.05.01.01.03_Termination_types`：`OFF` / `OFF,PULLDOWN`（PS1600、PS5000）/ `OFF,NONE`（PS1600）/ `DIFHIZ` / `CT`(center_tap) / `X`(cross) / `XSE`(single-ended cross) / `T`(term) / `H`/`L`(high/low) / `A`(active load) / `C`(clamp) / `bidir_receiver`。

### 六类资源 ↔ I/O pin 资源名

| 六类资源 | I/O pin 上叫什么 | 出处 |
|---|---|---|
| drive levels | `vih` / `vil`（i 与 i/o pin） | `02.06.05.01.01.01_Drive_Levels` |
| compare levels | `voh` / `vol`（o 与 i/o pin） | `02.06.05.01.01.02_Compare_Levels__Thresholds` |
| termination modes | `TERM` 的 term_mode + `vt`（commutation / third level） | `02.06.05.01.01.03`、`.14.04.08.02` |
| load currents | `iol` / `ioh`（active load） | `02.08.04.14.04.08.02` |
| clamp levels | `vcl` / `vch` | `02.08.04.14.04.08.01` |
| power supply voltage | DPS：`vout` | `02.06.05.01.02_DPS...` |

**文档给出的各种端接写法**（都在 `PINS` 块里，`02.08.04.14.04.08.*`）：

```
# 用 clamp 做端接
vcl = clamp low level
vch = clamp high level

# 用 active load 做端接（Pin Scale 5000：仅 std 模式单端 pin）
vt  = commutation voltage
iol = output low current
ioh = output high current

# 单端 std 的 cross 端接
term single_ended_cross
vol = logic 0 threshold
voh = logic 1 threshold

# 单端 fast 的 cross 端接
term single_ended_cross
vth = voltage single threshold

# 差分的 cross 端接（std 与 fast 相同）
PINS A1@diff
term cross
rec_swing  = the swing voltage
rec_offset = the offset voltage

# fast 双向全摆幅（低通道号做 o pin）
term bidir_receiver
vth        = voltage single threshold
rec_offset = receiver offset voltage
rec_swing  = receiver swing voltage
```

FAST 模式附加（PS5000，`02.05.04.02.07.03.03_Pin_Scale_5000_level_setup`）：四电平驱动，`v3h`、`v3l = v3h - (vih - vil)`、`vth`、`term center_tap`。`02.06.05.01.04.02.08_Supported_level_resources` 给出各卡 / 各 termination mode / 各 pin 类型的可用性表。

### level set 与 DPS set 是两套（不要合并）

**生成时是两条不同菜单**，走查原文：

> 「On the menu, click, depending on whether you want to generate equations for level or DPS pins: — `Shell > Generate Level` — `Shell > Generate DPS`.」

> 「If you need to specify both level and DPS sets, repeat steps step 3 to step 5, **generating the other required sets**.」

即：**要两套就得走两遍**。编号分开（`level_set_id` vs `dps_set_id`），计数命令分开（`LSUS` vs `DSUS`），查询分开（`UPTD? LEV` vs `UPTD? DPS`），装载分开（`EQFS LEV` / `EQFS DPS`）。GUI 里 `DPRL {level_set},{dps_set}` 把工具同时定位到两个 set 上。

**推断：** 文档把两者并列写在同一个 level 文件里，但没有给出一张「何时用哪个」的对照表，这个判断留给工程经验。

## L2 — Test Method API

**主 API：`LEVEL_SPEC(eqnset, specset)`**（`02.07.04.01.124_LEVEL_SPEC`，头文件 `/opt/hp93000/soc/prod_com/include/MAPI/LevelSpec.h`）。

```
LEVEL_SPEC(1, 2);                                  // 选 equation set 1 / spec set 2
Primary.level(spec1);                              // 按名字取 spec 值
Primary.getLevelSpec().change("v_low", -2.1 V);    // 改单个 spec
Primary.getLevelSpec().change("vdde", 4.4, "VCC"); // 按 DPS pin 限定改
FLUSH(TM::APRM);                                   // 让改动落到硬件
FOR_EACH_SITE { ... }                              // 逐 site
Primary.getLevelSpec().getSpecValue("v_low");      // 读
```

同族方法：`getEquation` / `getSpec` / `getSpecValue` / `change` / `restore`。

**文档 CAUTION（原句）**：

> 「Never mix the LEVEL_SPEC or TIMING_SPEC API and firmware commands modifying values for other reasons than debugging purposes (see note below)!」

**其余 L2 入口**：

- `02.07.03.03.02.02_Changing_spec_value_in_primary_level_spec_set`——在 primary level spec set 上改值的走查式说明。
- `02.07.04.01.123_LevelSetSelector`——`DIGITAL_OFFSET_SEARCH_TASK` / `DIGITAL_OFFSET_SEARCH_PINS` 里选 level set。类可指「a single level set or all fixed level sets」；构造 `LevelSetSelector(INT levelSetId)`，文档复述同一公式「`equset * 100000 + specset * 1000 + level_set_no`」；头文件 `MAPI/DigitalOffsetSearchTypes.h`；**7.2.1 引入**。
- `02.07.05.04.06_SetupLevelSet0`——Test Method，**6.5.3 引入**。
- `02.07.04.01.14.02_CCTchangeLevelSpec`——`void CCTchangeLevelSpec(const string& old_spec, DOUBLE value)`，定义在 `/opt/hp93000/soc/testmethod/include/CCTestMethod.hpp`；**7.2.0 引入**，7.2.1 由 `CCT_changeLevelSpec` 改名而来。

### `02.07.02_SpecValue` 与 level 的 spec set 是什么关系（**判定**）

`SpecValue` **不是** level setup 的组成部分，它是 **UTM（Universal Test Method）参数类型**：一个「数值 + 单位」的值，形如 `"3800[mV]"`（`02.07.02.13.03_SpecValue` / `02.07.04.02.14_SpecValue`）。

真正把 test method 参数**绑定到 level 文件里的 spec 变量**的，是**同族的另一个类型 `SpecVariable`**（`02.07.02.13.04_SpecVariable`），其取值格式是：

```
"LEV.<equationSetNumber>.<specName>[unit]"     例："LEV.1.fooSpec[mV]"
"TIM.3.barSpec@port1[A]"                       例（timing 侧同构）
```

所以三者的分工是：

| 东西 | 是什么 | 在本阶段干什么 |
|---|---|---|
| `SpecValue` | UTM 参数类型（值 + 单位） | 承载「一个 level spec 值」进出 test method |
| `SpecVariable` | UTM 参数类型（指向 level/timing 文件里某个 spec 变量的**引用**） | 把参数**绑到** level 文件的 spec 变量上 |
| `LEVEL_SPEC` | L2 C++ API | 在运行时**读/改** primary level spec set 的值 |

**结论：`SpecValue` 本身不构成「与 level spec set 的关系」，它是通用参数类型。**「SpecValue 与 level 的 spec set 是什么关系」这一问，正解是：**关系落在同族的 `SpecVariable` 上，`SpecValue` 只是它承载的值形态**。因此本页把三者一起写进 L2，不为 `SpecValue` 单独立一节。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 文档事实：`TestsuiteProxy`
（`02.09.01.14.02.01`）的 33 个编号成员里，session / execute / `isPass` / `isExecuted` /
name / siteMatch 那几个是**横切面**，其余**天然按阶段分组**——这不是巧合，是文档自己的组织方式。
横切入口见 [[test-suite-control-api]]；产物文件接口见 [[tpi-program-routines]]（**同层、同样由外部客户端进程调用**，见该页「出处」）。

### 本阶段专属读写口

文档事实（`02.09.01.14.02.01`）：level 一族是 `.05` `getLevelEquation()` /
`.06` `getLevelSet()` / `.07` `getLevelSpec()` / `.04` `getAnalogSet()` /
`.24` `setAnalogSet()` / `.25` `setEquationBasedLevel()`。

其中 `.25`（`02.09.01.14.02.01.25_TestsuiteProxy.setEquationBasedLevel`）：

```
bool setEquationBasedLevel(const std::string& levelEquation,
                           const std::string& levelSpec,
                           const std::string& levelSet);
```

> This function sets the equation based level information to the test suite.

三个参数依次是 level equation / level spec / level set，与 `.05` / `.07` / `.06` 三个
getter 一一对应。调用方式见 `02.09.01.14.01_How_to_use_the_test_suite_control_API`：
建外部 C++ 客户端，include `testsuitecontrol_api.hpp`、`using namespace testsuitecontrol;`，
编译 `-I/opt/hp93000/soc/prod_com/include/ -m32`、链接 `-ltestsuitecontrol_api`，
经 `/opt/hp93000/soc/system/bin/run -x <program>` 启动。该族 `Introduced in SmarTest 6.5.2`，
7.10.3 可用。

同层的产物文件接口（[[tpi-program-routines]]，`02.09.01.09` 全章 31 篇）：`DataManager`
（`02.09.01.09.02`）的文件标识 `dm_level` 就是 **level setup 文件**，配 `dm_load` /
`dm_save` / `dm_merge` / `dm_copy_in` / `dm_delete` 五个操作；`GetEQVariableValue`
（`02.09.01.09.10`）读 equation 变量值。

> **改判记录。** 本页上一版 L3 写的是「文档未覆盖」，并断言 Test suite control API
> 「它控制的是 test suite 的执行，**不提供任何 level 值接口**」。**那一句是错的**——
> `setEquationBasedLevel()` 就是 level 值接口，`getLevelEquation/Set/Spec` 就是读口。
> 该断言已删。错的断言比缺的断言更危险：缺的会被发现，错的会被当成「查过了，没有」。

### 两个同形陷阱 —— 名字里有 level，但不是本阶段的 level

写在这里是因为它们极容易被拿去错误地「补」本页：

- **HVM `GetLevelProfile`**（`02.09.01.10.03.02.02.26`）：文档事实是「returns all the variable
  names and values contained in the specified level」。但这里的 level 是 **application model
  的层级结构**，与 `IssueEDLEvent()` / `IssueHVMExecutionEvent()` 同族——`02.09.01.11.03.02`
  明写「maintain the application model file **level structure** in the BLC」。**不是电压 level。**
- **BLC `Level_control_API`**（`02.09.01.11.03.02`）的 `StartLevel()` / `LoopLevel()` /
  `CompleteLevel()`：同上，是产线层级（lot / wafer / die）的维护接口。

**不许拿 L1 命令或 L2 API 冒充 L3。**

## 产物

**产品（`02.06.05_Level_Setup_Commands` 末句）**：

> 「The level file resides in the **level** sub-directory of the device directory.」

**冲突（按 `schema.md` §10 并列记录，不自行选一个）**：`01.07.01.01.01_Device_directory_structure` 给出的 device 目录 `ls -al` 实测清单里，该目录名是 **`levels`（复数）**，同级的还有 `timing` / `vectors` / `testflow` 等。

| 说法 | 出处 |
|---|---|
| `<device>/level` | `02.06.05_Level_Setup_Commands`（正文末句） |
| `<device>/levels` | `01.07.01.01.01_Device_directory_structure`（目录清单） |

**推断：** 讲路径的其余文档都写 `level`，`levels` 只在目录清单里出现一次，倾向认为是文档笔误；但按 §10 不自行裁定，等实机确认。

**产物清单**：

| 产物 | 内容 | 备注 |
|---|---|---|
| level file | `EQNSET` / `SPECS` / `EQUATIONS` / `DPSPINS` / `LEVELSET`+`PINS`（+ `MODECONTEXT` / `MODULATION` / `GENERAL`） | 放 `<device>/level`(s)；首行 `hp93000,level,0.1` |
| level master file | 指向各 subfile | 首行 `hp93000,level_master_file,0.1`，次行 `testerfile: <name>`，条目形如 `EQNSET <n>: <file>`；文档给的自动命名 `eqnset_<n>.lev`、`defines.lev`；环境变量前缀 `VERIGY93000_MFH_PREFIX` |
| level equation file | 单条 equation set | `02.07.11.01.05.01`：header 同为 `hp93000,level,0.1`；带 `USE_PROTOCOL` 时落成 `.prot_lev` |
| spec set | 一组具名 spec 变量值（含单位） | 由 Spec Tool 生成，编号 1–99，必须关联到 equation set |

**是否落盘取决于你存不存**（两处 NOTE，走查原文）：

> 「Do not use the File > Save option of NEdit. In order to save your work you must first download the changed data, and then save them from the Test Program Explorer.」

> 「Remember that, if you want to have your level equation file available at a later stage, you must either save it from within the Level Equation Editor, or save the Level Setup.」

**三层对照表见 [[mapping-level]]** —— GUI 操作 ↔ 文件 ↔ L1 命令 ↔ L2 API ↔ L3 接口 的按目的对照
（`wiki/mappings/mapping-level.md`；证据分三档写明，**`?` 与 `—` 不同义**：前者是「本页没找到证据」，
后者是「这一层不存在这个对应物」）。

## 验证

**主路径：三个 GUI 结果窗口**（`01.07.01.03.04_Verifying_the_level_settings`，`02.06.05.01.04.03.01` 是同文）：

| 菜单项 | 看什么 |
|---|---|
| `Select > Show I/O Eqn. & Specs Results` | std I/O pin 的 equation / spec 求值结果；可改 `Eqn#` / `Sps#` / `Lset#` 逐个核对 |
| `Select > Show DPS Eqn. & Specs Results` | DPS 侧同样，可改 `Eqn#` / `Sps#` |
| `Select > Show FAST Eqn. & Specs Results` | FAST 模式（`v3h`、`vth`、`rec_swing` 等）的求值结果 |

**该页的 CAUTION（原句，必须一起读）**：

> 「If you modify a value in the Level Setup Editor, the level setup file will not be changed, but the entry in the Level Setup Editor will **temporarily override** what was specified in the level file.」

即：**在编辑器里看到"对了"不等于文件对了**——这既是验证手段的边界，也是常见错误的来源（见下）。

**各 `Results` 小节给的具体验收现象**（`02.08.04.14.04.08.*`，即「GUI 上该看到什么」）：

| 做了什么 | Level Setup 窗口里应看到 |
|---|---|
| 设 clamp | clamp mode 列显示 `on`，clamp low [V] / clamp high [V] 列显示所设值 |
| 设 active load | termination mode 列显示 `load`，termination lev/v3h、Iol [mA]、Ioh [mA] 列显示所设值 |
| 单端 cross（std） | termination mode 列显示 `scross` |
| 单端 cross（fast） | termination mode 列显示 `scross`，receiver [V] 的 vth 列显示阈值 |
| 差分 cross | termination mode 列显示 `cross`，swing / offset 列显示所设值 |
| fast 双向全摆幅 | termination mode 列显示 `bi_rcv`，receiver [V] 的 vth / swing / offset 列显示所设值 |

**context 的验证**（`01.07.01.03.01_Specifying_the_context_for_levels`）：用 `Select > Show I/O Eqn. & Specs Results` 确认当前生效的 equation set 属于期望的 context。

**L1 查询命令**：

| 命令 | 确认什么 |
|---|---|
| `UPTD? {status}`（`LEV` / `DPS`） | 硬件里的数据自 device file 上次保存/装载以来是否被改过（1/0）；上电或 `*RST`/`DSCP` 后全为 0 |
| `SPST?` | Specset STatus：被 `DRLV`/`RCLV`/`TERM`/`PSLV` 等改过 = bit 8（256）；`SVLR` 改过 = bit 10（1024）等 |
| `TERM? {set},{(pinlist)}` / `CLMP? {set},{(pinlist)}` / `DRLV? {set},{(pinlist)}` / `RCLV? {set},{(pinlist)}` / `PSLV? {dps_No\|dps_set_id},{(pinlist)}` | **回读**某个 level / DPS set 的对应资源设置 |
| `RCLS? {H\|L}, {pass_value}, [limit], {(pinlist)}` | **实测**：扫比较器阈值，测出 DUT 输出 pin 的高/低电平门限（返回 `RCLS {value_specifier}, {result_value}`）——这是本阶段少见的**测量型**验证 |
| `SDSC? {LEV\|TIM\|ANA}, {EQN\|SPS\|L\|LSET\|DSET\|...}, [setup_comp_1], [setup_comp_2], ["description"]` | 由描述查编号 / 由编号查描述；`LEV` + `EQN`/`SPS`/`L` 覆盖 level 侧——**用来确认"我改的到底是哪个 set"** |
| `EQSP?` | 读回 equation / spec 数据块 |
| `LSUS?` / `DSUS?` / `LSUS? [equation_set_no]` | 当前 level set / DPS set 的个数 |
| `SLDO? [operation]` | 查当前切换顺序设置 |
| `PSSR? {dps_No\|dps_set_id}, (pinlist)` | 查 DPS 的 slew rate 设置 |
| `DPRL?` | 查 level setup tool 当前定位在哪个 level set / DPS set |

**错误报告**（`02.08.04.14.02.03.10_Error_Reporting`）：下载时可把报告导到文件（`CKST?` / `EQFS`），报告里按 **DPS 资源 / I-O 资源 / Timing 资源**三类分别列违例，且 spec 会**分别按 setup 值、min、max 求值**（求值顺序在文档里写明）。

**Level Setup 窗口的状态指示**（`02.08.04.30.02.18`）：在别处（如 Timing 侧）改了 equation 后，Level Setup 窗口会显示 **`EDITED`** 标记；用 `Edit > Restore` 恢复。

**推断：** 文档没有给出一条单一的「level 验收清单」；上面这套（三个 Show 窗口 + `UPTD?`/`SPST?` + 回读命令 + `RCLS?` + 错误报告）是文档分散给出的判据的合成。

## 常见错误

### 1. 在 NEdit 里 File > Save 保存 equation —— **存了等于没存**

出处：`01.07.01.03_Setting_up_your_levels`（Procedure 末）与 `01.07.01.03.02_How_to_create_an_equation_set_using_the_Equation_editor`（两处）。文档用 NOTE 强调：

> 「**Do not use the File > Save option of NEdit.** In order to save your work you must first download the changed data, and then save them from the Test Program Explorer.」

**正确顺序**：Level Equation Editor 里 `Shell > Download`（或 **F8**）→ 关闭编辑器 → **在 Test Program Explorer 里保存 level setup**。spec 值同理：Spec Tool 里 `File > Download` → 再存 Level Setup。

**症状**：改了 equation、看着也在编辑器里生效，但重启 / 重新 load 后改动没了。

### 2. 在 Level Setup 窗口里直接改值 —— 只临时覆盖，文件没变

这条被文档反复警告，至少三处：

- `01.07.01.03.04_Verifying_the_level_settings` 的 CAUTION（原句见「验证」节）。
- `02.08.04.14.04.08.01_Using_the_clamp_for_termination`：「However, this will result in the **inconsistence between the setting in the Level Setup window and the content of the level equation file**.」
- `02.08.04.14.04.08.02_Using_the_active_load_for_termination`：同句，并直接链到 `02.08.04.30.02.18` 的恢复方法。

**症状**：当下测出来是对的，离开编辑器 / 重载后又变回文件里的旧值。**排查入口**：确认改动是否已通过 Download + Save 落到 level 文件；窗口出现 `EDITED` 时用 `Edit > Restore`。

### 3. `SVLR`/`DRLV` 类改动没生效 —— 缺少激活

`02.06.05.02.05_DRLV`：「Each call of the DRLV FW command requires an **activation of the level set**... use the `SVLR` FW command」。**排查入口**：`SPST?` bit 8 是否被置位。

### 4. 资源超限 → 系统拒绝下载

`02.08.04.14.02.03` / `.03.10_Error_Reporting`：超出 level set 数量上限（每 equation set 99、全库 256）、或触到 DPS / I-O / Timing 资源上限时，**系统拒绝下载并在 report window 报错**。**排查入口**：report window + `LSUS?`/`DSUS?`/`DSCP`。

### 5. 设了 termination 之后，原来的比较阈值可能不再适用

`02.08.04.14.04.08_How_to_set_the_termination_for_DUT_outputs`：文档明确指出，加了端接之后，为**未端接传输线**设的比较阈值「may not longer work」。**症状**：功能测试 pass/fail 翻转。**排查入口**：按 `02.08.04.14.04.09` 重算 `voh`/`vol`。

### 6. 比较阈值与驱动摆幅的电气边界

- `02.08.04.14.04.09`：比较器四态（logic 0 / logic 1 / intermediate / **unstable**）；**两阈值最小间隔 100 mV**，低于此文档给 warning。
- `02.08.04.14.04.06`：单端驱动**最小摆幅 0 V，但 "the specified accuracy is only valid down to 200 mV"**。
- `02.06.05.01.03_Clamping` / `02.08.04.14.01.04.01_Pin_Scale_1600_Card`：**Pin Scale 1600 上 clamp level 与 driver level 必须落在同一个 9.0 V 电压窗内（−2.0 V … 7.0 V）**；PS1600 的 clamp 集成在 driver 里；clamp mode ∈ `auto` / `on`；该 clamping 特性 **Introduced in SmarTest 7.10.0**。**PS9G 无 clamp。**
- `PSLV` 的 settling time 与 `PSSR` 的 rise/fall 参数、`t_ms` 方程参数**互斥**，同时用会冲突（`02.06.05.02.16_PSSR` 的 Note）。

### 7. 自动摆幅调整与 `CLEV` 冲突

`02.08.04.14.06.02.05_Using_Automatic_Swing_Adjustment`：**`CTIM` 可以伴随自动调整，`CLEV`（切 level set）不行**。**症状**：切 level set 后摆幅没有跟上。

### 8. level set 0 的几条硬限制

见「L1」节：不能 equation based、不能做 primary、被排除在 `ALL` 之外、只能用 fixed 定义、只支持 `OFF`/`T`/`C`/`A`、`TERM`/`CLMP` 只在 BRK 生效、使用前 level setup file 必须先 load。**症状是「高阻态下 pin 行为不符合预期」而不是一条明确报错**，排查入口是 technology 文件的 `pulldown_in_level_set0` 开关。

### 9. DPS modulation 必须用 Level Equation 做

`02.08.04.14.06.01_Setting_up_the_Device_Power_Supply`：DPS 的 modulation 必须通过 Level Equation 实现，不能走别的方式。

### 10. fixed level setup 在 7.4.1T 之后不再支持

`02.06.05.01.05_Data_Organization_of_Fixed_Levels`：「The support for fixed level setups is **discontinued with SmarTest version 7.4.1T**.」——本 wiki 面向 7.10.3。**建议：** 文档只说 discontinued、没说不能读，所以 fixed 路线宜作为读老程序 / 调试时的知识，不作为新程序的写法。

## 下一步

[[timing]]。

**文档事实依据**（两处）：

- `01.07.01.03_Setting_up_your_levels` 的 `About this task`：「The process for setting up equation based levels is **very similar** to that for setting up equation based timing.」两者共享同一套 `EQNSET` + `SPECS`/`EQUATIONS` + spec set 的数据组织与 Spec Tool 编辑机制。
- `02.08.04.14.04.08.04` 的 `What to do next`：「**Set up the timing, waveform and pattern as usual.**」

另有一条 context 约束把两者绑在一起（`02.08.04.18.03.01.01_Context_list`）：**同一个 `MODECONTEXT` 必须同时覆盖 level equation set、timing equation set、wavetable 与 vector label 才构成有效 setup**——先做 level 再做 timing，可以把 context 一次定好，避免两次返工。

**推断：** level 与 timing 之间文档没有写硬性顺序（不像 [[pin]] → level 那样明写 "It is impossible to define level ... without the pin configuration"），谁先谁后都可以；此处按走查章节顺序（levels 在 wavetables 之前）与「context 一次定好」的工程理由排在 level 之后。
