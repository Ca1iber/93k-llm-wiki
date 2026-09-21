---
type: stage
title: Timing / Wavetable — 波形与时序设置
tags: []
related: [project, pin, level, pattern, run, results, wavetable, timing-specification, timing-setup-tool, timing-diagram-tool, timing-spec, wsus, tsus]
sources:
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04_Waveform_and_timing_sets.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.01_Equation_based_timing_setup.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.02_Setting_up_the_wavetables.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.03_Defining_the_equation_sets.md
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.04_Defining_the_spec_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.01_Introduction.md
  - 02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01_Concepts_of_timing_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.01_Waveform_Shapes_and_Edge_Delays.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.02.01_Timing_equation_set_reference.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.02.01_Restrictions_for_drive_edges.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.02.02_Restrictions_for_receive_edges.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.02_Specifying_the_Period_Resolution.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05.01_Consistency_checks_for_edge_delays.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.06_Dealing_with_rounding_problems_in_multiport_setups.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.07_Fixed_timing.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02_List_of_timing_setup_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.01_APRM_-__Activate_PRiMary_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.05_CLKR__CLKR__-__CLocK_Resolution.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.09_DPRT__DPRT__-__Default_PRimary_Timing_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.12_EDSP__EDSP__-__EDge_SPecification.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.13_EQFS_-__EQuation_FileS_command_transfer.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.14_EQSP__EQSP__-__EQuation_SPecification_transfer.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.16_ETIM__ETIM__-__Edge_TIMing.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.20_PCLK__PCLK__-__Pin_CLocK.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.21_PDIV__-__Period_DIVider.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.28_SPRM__SPRM__-__Set_PRiMary_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.29_SPST__-__SPecset_STatus.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.30_STRS__-__Spec_TRansition_Search.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.32_TSUS__TSUS__-__Timing_Sets_USed.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.33_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.34_UPTD__UPTD__-__UP_To_Date.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.35_VCLK__-__Verify_CLocK.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.36_VDCG__-__Verify_Device_Cycle_for_Group.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.37_VTIM__-__Verify_TIMing.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.38_VWFG__-__Verify_WaveForms_in_Groups.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.39_VWFS__-__Verify_WaveForm_Sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.40_WAVE__WAVE__-__WAVEform.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.46_WSUS__WSUS__-__Waveform_Sets_USed.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.03.01_Changing_the_timing_set__CTIM.md
  - 02_System_reference/02.06_Command_Reference/02.06.14_Commands_for_Processing_Results_of_Source_Synchronous_Testing.md
  - 02_System_reference/02.06_Command_Reference/02.06.16_Commands_for_jitter_injection.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.01_Principles_of_jitter_injection.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.02_List_of_commands_for_jitter_injection.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.02_JSCF__JSCF__-__Jitter_Set_ConFiguration.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.05_JSUD_-__Jitter_Set_UnDefine.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.02.01_Changing_spec_value_in_primary_timing_spec_set.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.02_Timing_equation_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05_Wavetables.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.16.01_Global_and_local_spec_values__scope_of_the_spec_variable.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.18_How_to_restore_the_equation_settings_after_you_change_them_in_the_Timing.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.19_Error_Checking_Facilities.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33.01_Using_the_Timing_Diagram_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34_Timing_Setup_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.02.01_Verifying_a_multiport_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.06_Error_Reporting.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05.01_Master_file_format_for_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.05_Mode_context_in_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06_Using_the_Timing_Setup_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.05.01_Minimum_period___maximum_frequency_of_the_sequencer.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.06.06_Downloading_Your_Timing_Setup_into_the_Firmware.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.11.02_Keeping_Waveform_Sets_Compatible.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.12_Performing_Timing_Checks.md
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.md
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# Timing / Wavetable — 波形与时序设置

> Timing 这一步定义「DUT 的每个 pin 在 tester cycle 内能打出什么波形、边沿放在哪里、cycle 能有多长」，并把它们打包成可被向量引用的 waveform set / timing set。

## 目的

Timing setup 定义两件事（文档事实，`02.06.06_Timing_Setup_Commands`）：

- 「the waveforms that can be sent to the pins of the DUT during a test」——能送到 DUT pin 上的波形；
- 「the possible period lengths, that is, the possible lengths of the tester cycle, which is the time span used for executing one waveform」——tester cycle 的可能长度。

SmarTest 的标准做法是 **equation based timing**，它由三个任务组成（文档事实，`01.07.01.04.01_Equation_based_timing_setup`）：

1. Generate a Wavetable.（生成 wavetable）
2. Generate a Timing Equation Set.（生成 timing equation set）
3. Generate a Timing Specification, linking the wavetables and timing equations.（生成 timing specification，把 wavetable 和 timing equation 连起来）

**三个概念的关系**（文档事实，`02.06.06_Timing_Setup_Commands` 原句）：

> 「In equation based timing, **waveform shapes are defined in a wavetable**, and **edge positions are defined in an equation set**. Wavetable and equation set are brought together in **a timing specification**. In a multi-port setup, this must be done separately for every involved port.」

即：

| 概念 | 定义在哪 | 回答什么问题 |
|---|---|---|
| waveform shape | wavetable | 这个 cycle 里 pin 依次做什么动作（动作序） |
| edge position | equation set | 每个动作对应的边沿落在 cycle 内第几 ns |
| timing specification | 把上面两者 + 一组 spec 值合起来 | 某个 pin（组）在某组数值下用哪套形状、哪套边沿 |

**多端口时每个端口要分别做一遍**（同上，原句 "must be done separately for every involved port"）。单端口 spec 用两个整数标识（equation set 号 + spec set 号），多端口 spec 是**具名的**（`02.06.06.02.28_SPRM` 的多端口例子中出现 `timing_set_list`）。

另一条独立路线是 **fixed timing**（`02.06.06.01.07_Fixed_timing`，文档事实）：不走 equation，每个 setup 元素（某个 pin 的 waveform、edge 位置）各由一条 firmware 命令定义，值必须是常量：

> 「With fixed timing, each setup element is defined by calling a firmware command. With equation based timing, the setup elements are part of larger data blocks that are downloaded to the tester as a whole.」

> 本条与 [[level]] 阶段结构同构（都是 equation set + spec set 两件套，连「spec 变量作用域按位置定」这条规则都一样）。本页只讲 timing 侧，level 的具体内容见 [[level]]。

## 前置条件

- **Pin configuration 必须先做完**（文档事实，`02.06.03.01.01_Introduction`）：

  > 「Configuring pins is the first step you must take when preparing a test. **It is impossible to define level, timing, or vector parameters without the pin configuration.**」

  另：**测试运行期间 firmware 不接受任何配置改动**（同篇："The firmware does not accept any configuration changes while a test is running."）。见 [[pin]]。

- **equation set 与 base wavetable 的 mode context 必须一致**（文档事实，`02.08.04.34.05_Mode_context_in_timing_setup`）：

  > 「The specification of a primary timing setup must include a pointer to a timing equation set and to a base wavetable **of the same mode context**. You cannot define a specification pointing to a wavetable and an equation set of different mode contexts.」

  mode context 由 equation set / wavetable 自带的 `MODECONTEXT "..."` 行给出，默认上下文是 `"DEFAULT"`（即全部 std pin、非 FAST）。见 [[constraint-timing-mode-context-match]]。

- **改动 pin / waveform set 会把 timing 的 up-to-date 标志打回 0**（文档事实，`02.06.06.02.34_UPTD`）：

  > 「Use of the commands PCLK (Pin CLocK), DFPN (DeFine Pin Name), or CONF (CONFiguration) sets the flag to 0 until the setup is saved or loaded.」

  > ⚠️ 本页初版把这句**改写**成了「Use of the commands CONF, DFPN, or any of the
  > Timing Setup Commands set the flag to 0…」——**顺序反了、括号注释删了、`sets` 写成 `set`**，
  > 也就是说引号里装的是我的话（§11）。**已按原文改回**（2026-09-18）。
  > 原文点名的是 **PCLK / DFPN / CONF 三条**，不是「任何 Timing Setup 命令」。


  即 pin 配置一变，之前下载进 firmware 的 timing 就不再被认为与硬件一致。

- **改 spec 值必须走 timing 文件本身才是永久的**（文档事实，`02.06.06.02.31_SVLR`）：运行时改变 spec 值「takes effect without changing the level or timing file! If you want to change spec values permanently you must do so in the corresponding setup file itself.」

- 「You cannot start setting up vectors if the timing is not finished.」（文档事实，`02.08.04.34.06.11.02_Keeping_Waveform_Sets_Compatible`）——这是本阶段必须先于 [[pattern]] 完成的直接依据。

## 涉及对象

### 文件 / 数据对象

| 对象 | 层 | 在本阶段干什么 |
|---|---|---|
| [[wavetable-file]] | file | protocol wavetable 怎么进 device timing 文件——讲的是 `USE_PROTOCOL` 这条语句 |
| [[wavetable]] | n/a | 存 waveform shape（动作序），可被多个 timing set 复用。**它是内存里的数据实体，不落在 L1/L2/L3 任何一层**（见 [[wavetable]] 页） |
| [[timing-equation-set]] | file | 存 edge position / period 的表达式定义 |
| [[timing-specification]] / [[timing-file]] | file | 把 wavetable + equation set + 一组 spec 值绑成一个 spec set |
| [[timing-master-file]] | file | 一个 device 的 timing 总入口，指向各个 subfile |
| [[waveform-set]] | n/a | wavetable + device cycle table + 一个或多个 timing set 的集合体。**内存里的逻辑容器，不落在任何一层**（`concept` 是页面类型，不是层——schema §6 的合法值是 `L1\|L2\|L3\|file\|gui\|n/a`） |

### L1 命令

| 对象 | 层 | 在本阶段干什么 |
|---|---|---|
| [[wsus]] | L1 | 定义/删除 **waveform set 的个数** |
| [[tsus]] | L1 | 定义/删除某个 waveform set 里的 **timing set 个数** |
| [[tsux]] | L1 | timing set 计数的扩展形式（system only，Test Flow Optimizer 用） |
| [[eqfs]] | L1 | 从文件 **LOAD/SAVE** wavetable / equation set / spec set |
| [[eqsp]] | L1 | 直接 **下载/查询** 这三块数据（EQSP? 被 Test Program Explorer 用来生成 setup 文件） |
| [[sprm]] | L1 | 把 timing equation set + spec set 指成 primary set（多端口给 timing_set_list） |
| [[aprm]] | L1 | 把 primary set **真正激活到硬件** |
| [[dprt]] | L1 | Default PRimary Timing sets——**供系统使用，不要从 hpt 手工执行**；作用是 "position the timing setup tool on the given sets" |
| [[svlr]] | L1 | 运行时改 spec 变量值并重算（写 SPST bit 10） |
| [[spst]] | L1 | Specset STatus——查询状态字（是否被 ETIM/ETDS/PCLK/CLKR 改过、是否有 range/order 违例） |
| [[uptd]] | L1 | 查 timing 文件与硬件是否一致（`UPTD? TIM`） |
| [[vclk]] [[vdcg]] [[vtim]] [[vwfg]] [[vwfs]] | L1 | 成组的 timing 校验查询命令 |
| [[edsp]] | L1 | EDge SPecification——定义 timing search 用的 leading / trailing 搜索边沿 |
| [[strs]] | L1 | Spec TRansition Search——循环跑功能测试、在区间内扫某个 spec 变量，找 PASS↔FAIL 翻转点 |
| [[etim]] [[etds]] [[pclk]] [[clkr]] [[wave]] [[wfds]] [[bwds]] [[bwdf]] [[pdiv]] [[dcdt]] | L1 | fixed timing 路线：逐个元素定义 edge / period / waveform |

### L1 抖动注入（子专题）

`02.06.16_Commands_for_jitter_injection` 家族：[[jrst]] [[jscf]] [[jsdf]] [[jspr]] [[jsud]] [[jswf]] [[mscf]] [[msdf]]。

**归属判断：属本阶段**（文档事实，`02.06.16.01_Principles_of_jitter_injection`）：jitter injection 在**不切 CTIM、不改 spec** 的前提下，改变「the edge positions of the currently active timing set」；仅 **PS1600** 支持，仅对 **drive pin** 有效，SmarTest 7.0.1 引入。

### L2 API

| 对象 | 层 | 在本阶段干什么 |
|---|---|---|
| [[timing-spec]] | L2 | `TIMING_SPEC(eqnset, specset)`，改/读 spec set 的值 |
| [[primary-status]] / `Primary.getTimingSpec()` | L2 | 从 test method 里拿当前 primary 的 timing spec |
| [[timing-set-selector]] | L2 | `DIGITAL_OFFSET_SEARCH_TASK` 里选 timing set（7.2.1 引入） |
| [[spec-search]] | L2 | 与 `FLUSH` 配合执行 spec 搜索/量测 |

### GUI

| 对象 | 层 | 在本阶段干什么 |
|---|---|---|
| [[timing-setup-tool]] | gui | 本阶段的主工具：编 wavetable / equation set / spec set、下 Download、跑 timing check |
| [[spec-tool]] | gui | 与 Timing Setup Tool 共享 spec/edit 机制（全局/局部 spec 值、`E`/EDITED 指示、Edit > Restore） |
| [[waveform-view]] / wavetable editor | gui | 看/改物理波形表 |
| [[timing-diagram-tool]] | gui | **验证侧**：从 `93000 > Results > Timing Diagram` 打开，显示实际送到 DUT 的波形以及接收数据与期望不符的位置。**归属判断：主归属是 [[results]]**（文档称其为 "the Timing Diagram **result analysis** tool"），但可在本阶段用来目视核对波形。 |

### 归属判断

- **jitter injection（`02.06.16`）→ 归本阶段**（理由见上）。
- **source synchronous testing（`02.06.14`）→ 不归本阶段**。该篇自述："This chapter describes the use of the commands that allow to **process the results of source synchronous tests in the hardware**"——它讲的是结果处理（移动比较边沿 + 多 cycle 结果的 disjunctive 累积），归 [[results]] / [[run]]。

## L1 — Firmware / Setup Command

### 路线一：equation based timing（标准路线）

三块数据分别下载（`02.06.06.01.02_Data_organization_of_equation_based_timing`）：

> 「The data collections are downloaded with the EQFS and EQSP commands. The collections themselves cannot be edited with firmware commands. But you can query their content with firmware commands, and also change definitions at runtime.」

**specset_id 的算法**（文档事实，同篇）：`specset_id = 100 * equation_set_no + specset_no`；每个 equation set 最多 99 个 spec set；每个 setup 文件最多 256 个 equation set。

**equation set 正文的最小形态**（文档事实，`01.07.01.04.03_Defining_the_equation_sets` 的走查例子，照抄）：

```
SPECS
T    [ns] # cycle time
clkr    [ns] # rising time of clock
ref    [ns] # basic reference for the bus timing
sp1    [ns] # data valid
sp2    [ns] # data invalid
```

```
TIMINGSET 1 "only one used"
period = T

PINS clkout
e1 = clkr

PINS data
e1 = 0
e5 = ref + sp1 + acc
e6 = ref + sp2 - acc
```

```
EQUATIONS
acc = 0.1
```

（注意：该走查用的是 `e1/e5/e6` 记法；`02.06.06.01.02.01_Timing_equation_set_reference` 给出的正式文法是 `(d|r)<edge_no> = <expression>`，即 `d1..d8` 驱动边沿、`r1..r8` 接收边沿，`r7` 另用于 TMU。"Upon download, the syntax of your description is checked, and if you have made any errors you will be notified accordingly in the report window."）

**timing specification 的最小形态**（文档事实，`02.06.06.01.05_Defining_the_timing_specification`，照抄）：

```
EQNSET 1 "default"

WAVETBL "table1"
CHECK all

SPECSET 1 "sp1"

# SPECNAME *****ACTUAL***** *****MINIMUM**** *****MAXIMUM**** UNITS COMMENT
f          100                                                [MHz]
```

**容量与计数**——这是 `WSUS` / `TSUS` 两个枢纽命令的用途：

- `WSUS`（被 93 篇引用，`02.06.06.02.46`）：
  > 「The WSUS (Waveform Sets USed) command sets the number of defined waveform sets to the given value. The new value has to be an integer in the range of 1 to Maximum allowed waveform sets as set by DSCP, DSCP? - (Define System Control Parameter) (the default is 16, the maximum is 16).」
  >
  > 「You can use the WSUS command to delete sets.」

  语法 `WSUS {waveform_set}` / `WSUS?`；「At power-on, only one waveform set (containing one timing set and default values) is available.」示例 `WSUS 3`。

- `TSUS`（被 33 篇引用，`02.06.06.02.32`）：
  > 「The TSUS (Timing Sets USed) command defines the number of timing sets contained in a given waveform set. The number of defined waveform sets is not modified. The new value has to be an integer in the range of 1 to Maximum allowed timing sets as set by CONF, CONF? - (CONFiguration).」
  >
  > 「The maximum number of all timing sets belonging to all waveform sets is 512. The default number is 256.」
  >
  > 「The maximum number of timing sets for one waveform set is 256.」
  >
  > 「You can use the TSUS command to delete timing sets.」

  语法 `TSUS {waveform_set},{timing_set}`，equation based 场合用 `specset_id`。示例 `TSUS 3,7`。用户要求的「三个概念」在命令层的落点就是：**wavetable 由 WSUS 划出容器、timing set 由 TSUS 计数，specset_id 把 equation set 与 spec set 对上**。

  > ⚠️ **上面这两条引文 2026-09-18 修过一次。** 原稿把 WSUS 的首句用 `…` **掐成两截**
  > （写成 `the given value … range of 1 to`），把 TSUS 的**两段话并进同一个 「」**，
  > 还省掉了原文的 `DSCP, DSCP? - (Define System Control Parameter)` 这处注解。
  > **`…` 一旦出现在引文里，就等于承认中间有字没抄**——那就不再是引文，是转述。
  > 现在改成**一句一个 「」**，跨段不再合并。（第七类复核查出来的。）

- 一致性检查关键字（`02.06.06.01.05.01_Consistency_checks_for_edge_delays`）：`CHECK` 后跟 `1period` / `2period` / `10period`（`_drv` / `_rcv` 变体，查边沿间距）与 `edgeorder`（`_drv` / `_tri` / `_win`，查边沿顺序），`CHECK all` / `CHECK NONE`。**Smart Scale 数字板上最大间隔不得超过 10 个 user period；违反或关掉间距检查的 spec 不会被执行。**

- 激活链路：`SPRM`（设 primary set，多端口形如 timing_set_list；`specset_id = 100*eqn + specset`）→ `APRM`（激活到硬件；`FTST` / `RCLS` / `SQST RUN` / `PSST` 会隐式做）。

- 文件搬运：`EQFS {spec_type},{part},{operation},{"eqn_filename"},["error_filename"]`，其中 spec_type = `LEV`|`TIM`，part = `WVT`|`EQN`|`SPS`，operation = `LOAD`|`SAVE`；`EQSP` 走二进制串（`#<ndigits><len><data>@`）。

- period 上限/下限与卡型相关（`02.08.04.34.06.05.01`）：Pin Scale 1600 = 2.5 ns / 400 MHz；DPS128/DPS64 = 20 ns / 50 MHz；UHC4T = 2.5 ns；XPS256 = 20 ns。period 分辨率用 `period_res` 关键字声明（`02.06.06.01.04.01.02.02`）。

### 路线二：fixed timing

每个元素一条命令，值必须是常量。文档给出的成组例子（`02.06.06.01.07_Fixed_timing` 家族，照抄）：

```
PCLK 1,1,12,(@)
ETDS 1,1,,"d1:2 d2:4 d3:8 d4:6 d5:10",(IN1)
```

```
WFDS 1,0,,"d1:F00 d2:D11 d3:F0N",(IN1)
WAVE 1,0,F00,,,,0,(IN1)
WAVE 1,0,F10,,,,1,(IN1)
...
BWDS 1,,,"",(IN1)
```

即：`WFDS` 定义逻辑波形（动作序），`WAVE` 把逻辑动作映射成物理波形（`WAVE` 的前置条件是先有 `WFDS`/`WFDF`），`BWDS`/`BWDF` 定义 break waveform，`ETDS` 定义边沿延迟，`PCLK`（Pin CLocK）定义 pin / waveform set 的测试系统周期。

> 注：`ETIM` 自 release 2.1 起在 14 边沿场合被 `ETDS` 取代，且在边沿数超过 6 的 pin/waveform set 上被禁用（`02.06.06.02.16_ETIM`）。改动 timing 数据的命令会置位 `SPST?` 的 bit 8（值 256）（`02.06.06.02.29_SPST?`）。

### 运行期

- `CTIM` 在测试中切换 timing set：`SQPG 4,CTIM,2,,(@)`（`02.06.07.01.08.03.01`）；系统在 CTIM 前会先关闭已打开的 compare window；配套 CTOF 序列。
- `SVLR` 运行时设 spec 变量并重算：`SVLR TIM,PRM,,"f",43`；查询 `SVLR? TIM,ALL,ALL,"f"`；新值必须落在 min/max 之间。

## L2 — Test Method API

`02.07.04.01.249_TIMING_SPEC`（头文件 `/opt/hp93000/soc/prod_com/include/MAPI/TimingSpec.h`）：

- 构造：`TIMING_SPEC(INT eqnset, INT specset)`，正好对应本阶段的 equation set 号 + spec set 号。
- 成员：`getEquation()`、`getSpec()`、`getSpecValue(const STRING& spec)`（多端口用 `"spec@port"` 形式）、`change(const STRING& spec, DOUBLE value)`、`restore()`。
- 挂到 test 上：`TIMING_SPEC spec1(1, 2); Primary.timing(spec1);`
- 取值：`DOUBLE specValue = Primary.getTimingSpec().getSpecValue("Tp");`
- 改值：`Primary.getTimingSpec().change("T", 10);`

**生效时机**（文档事实，同篇）：`change()` 的结果「are actually reflected to the hardware when any of the following APIs is executed: EXECUTE_TEST, START_TEST, DIGITAL_CAPTURE_TEST, NB_DIGITAL_CAPTURE_START, FUNCTIONAL_TEST, FLUSH then SPEC_SEARCH.execute(), FLUSH then SEQUENCER_STATUS.run(), …」

**单位**：声明变量时必须写单位（`[ns]` 等）；「In SmarTest, all timing values are in nanoseconds by default.」

**已知陷阱（文档原文 CAUTION）**：

> 「Never mix the LEVEL_SPEC or TIMING_SPEC API and firmware commands modifying values for other reasons than debugging purposes (see note below)!」

相关：`02.07.03.03.02.01` 给出 `Primary.getTimingSpec().<memberFunction>;` 的 change/restore 用法；`02.07.04.02.17_TimingSetSelector`（7.2.1 引入）用于 `DIGITAL_OFFSET_SEARCH_TASK`；`02.07.11.01.05.02_Timing_equation_file` 给出 `USE_PROTOCOL "<protocolName>:<timingSegmentName>" [<portList>]`（7.1.0 引入，`.prot_tim` XML 存在 protocol 目录）。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 文档事实：`TestsuiteProxy`
（`02.09.01.14.02.01`）的 33 个编号成员里，session / execute / `isPass` / `isExecuted` /
name / siteMatch 那几个是**横切面**，其余**天然按阶段分组**——这不是巧合，是文档自己的组织方式。
横切入口见 [[test-suite-control-api]]；产物文件接口见 [[tpi-program-routines]]（**同层、同样由外部客户端进程调用**，见该页「出处」）。

### 本阶段专属读写口

文档事实（`02.09.01.14.02.01`）：timing 一族是 `.18` `getTimingEquation()` /
`.19` `getTimingSet()` / `.20` `getTimingSpec()` / `.22` `isMultiportTiming()` /
`.26` `setEquationBasedTiming()` / `.27` `setMultiportTiming()`。

其中 `.26`（`02.09.01.14.02.01.26_TestsuiteProxy.setEquationBasedTiming`）：

```
bool setEquationBasedTiming(const std::string& timingEquation,
                            const std::string& timingSpec,
                            const std::string& timingSet);
```

> This function sets the equation based timing for the test suite.

三参数依次是 timing equation / timing spec / timing set，与 `.18` / `.20` / `.19` 三个
getter 对应。`.22` / `.27` 是 multiport timing 的查询与设置——**与 [[pattern]] 的
multi-port burst 是同一件事的外部化**，见 [[run]] 的 `Using_execution_contexts`。

调用方式见 `02.09.01.14.01`：外部 C++ 客户端，链接 `-ltestsuitecontrol_api`，经
`run -x` 启动。该族 `Introduced in SmarTest 6.5.2`，7.10.3 可用。

同层的产物文件接口（[[tpi-program-routines]]，`02.09.01.09` 全章 31 篇）：`DataManager`
（`02.09.01.09.02`）中 `dm_timing` = timing setup 文件、`dm_tdiag` = timing diagram 文件、
`dm_mx_waveform` = multiport waveform，各配 `dm_load` / `dm_save` / `dm_merge` /
`dm_copy_in` / `dm_delete`。

> **改判记录。** 本页上一版 L3 写「文档未覆盖」，并断言「Test suite control API / HVM
> 在本次读到的语料里**没有覆盖 timing setup 的条目**」。**那一句是错的**——`.26` 就是
> timing 值接口。已删。

### 同形陷阱

- **HVM 侧的 timing**：`02.09.01.10`（HVM API）本阶段未见 timing 值接口；HVM 面向的是
  测试执行与会话控制。

**不许拿 L1 命令冒充 L3。**

## 产物

**device 目录布局**（文档事实，`01.07.01.01.01_Device_directory_structure` 的 `ls -al` 实测清单）：

```
<device>/timing/          ← timing specification 文件放这里
<device>/timing_dgrm/     ← timing diagram 相关文件
<device>/waveform/        ← waveform 相关文件
<device>/vectors/         ← 下一阶段（pattern）
```

`02.06.06.01.05_Defining_the_timing_specification` 原句：

> 「The timing specification file can be found here: `<device_folder>/timing`. The file can have any name that is suitable, for example, timingSpec1.」

**文件种类**：

| 产物 | 内容 | 备注 |
|---|---|---|
| timing file（timing specification） | `EQNSET` / `WAVETBL` / `CHECK` / `SPECSET` + spec 值表 | 放 `<device>/timing` |
| wavetable file | waveform shape（逻辑/物理波形表） | **是临时文件**——见下 |
| equation set | `MODECONTEXT` / `DEFINES` / `SPECS` / `EQUATIONS` / `TIMINGSET` | 可被多个 spec 复用 |
| spec set | 一组具名 spec 变量值（含单位） | 编号 1–99，必须关联到 equation set 与 wavetable |

**wavetable 是临时产物**（文档事实，`01.07.01.04.02_Setting_up_the_wavetables`）：

> 「Remember that the wavetable file is a temporary one. If you want to make it available at a later stage, you must either save it from within the wavetable editor (using vi, for example), or save the Timing Setup.」

且 wavetable editor「displays the last wavetable file you were working on, and has nothing to do with the current Timing Setup.」

**timing master file**（文档事实，`02.08.04.34.04.05.01_Master_file_format_for_timing_setup`）：首行 `hp93000,timing_master_file,0.1`，次行 `testerfile: <name>`，条目形如

```
WAVETABLE <wavetable_name> [PIN_ALIAS_SET <pin_alias_set_name>]: <file_name>
EQNSET <equationset_number> [PIN_ALIAS_SET <pin_alias_set_name>]: <file_name>
MULTIPORT_SPEC <"specification_name">: <file_name>
DEFINES: <file_name>
```

Setup Management Tool 会自动拆出 `eqnset_<n>.tim` / `wvt_<name>.tim` / `mport_<name>.tim` / `defines.tim`；前缀环境变量 `VERIGY93000_MFH_PREFIX`。

**三层对照表见 [[mapping-timing]]** —— GUI 操作 ↔ 文件 ↔ L1 命令 ↔ L2 API ↔ L3 接口 的按目的对照
（`wiki/mappings/mapping-timing.md`；证据分三档写明，**`?` 与 `—` 不同义**：前者是「本页没找到证据」，
后者是「这一层不存在这个对应物」）。

## 验证

**L1 查询命令**（全部来自 `02.06.06.02.*`）：

| 命令 | 确认什么 |
|---|---|
| `UPTD? TIM` | timing setup 文件与硬件是否一致（1 = 一致；CONF / DFPN / 任何 timing setup 命令把它打回 0，直到 save 或 load） |
| `VTIM?` | 指定 pin 组的 **period 与 edge timing 是否相等**（返回 0/1） |
| `VWFS?` | 两个 waveform set 是否兼容（返回 0/1） |
| `VWFG?` | 一组 pin 的 **device cycle 与 waveform 定义是否相同**（返回 0/1） |
| `VCLK?` | 该 period 是否会引起 auto-correction（会则报告被修正成什么值） |
| `VDCG?` | device cycle 在 pin 组内是否一致 |
| `SPST?` | Specset STatus：被 ETIM/ETDS/PCLK/CLKR/DRLV/RCLV/TERM/PSLV 改过 = bit 8（256）；SHVL = bit 9（512）；SVLR = bit 10（1024）；绝对范围违例 = bit 12（2048）；相对范围违例 = bit 13（4096） |
| `EQSP?` | 读回三块数据的内容（Test Program Explorer 用它将 setup 存成文件） |
| `SPEC? "Timing:FxdlRange"` | 查 spec 范围 |

`VTIM?` 的多端口用法在 `02.06.06.02.37` 给了完整例子，以 `VTIM 1` 收尾。

**GUI 侧**（`02.08.04.34_Timing_Setup_Tool` / `.04.02.01` / `.04.03.06`）：

- `Select > Show Eqn & Spec Results` —— 看 equation / spec 的求值结果；多端口再配合 `Select > Select Specification…` 与 `Select > Port…` 选端口、在 `Tset#` 字段选 timing set。
- **错误报告**：错误输出可以导到文件（`CKST?`、`EQFS` 都能指定输出文件）。报告里 timing 资源按 `period_res`、`period`、`d1`–`d8`、`r1`–`r8` 逐项列出；equation 会**分别按 setup 值、min、max** 各求值一遍。
- **Download**：在 Timing Setup Tool 里 Download 把 setup 送进 firmware。「If you've used up more resources than are available, the system refuses to download your setup and issues an error message in the report window.」（`02.08.04.34.06.06.06`）
- **Check 菜单**（`02.08.04.34.06.12_Performing_Timing_Checks`）：做 waveform set 兼容性检查；timing check 会在 device cycle 边界上检查最小 pulse / window 宽度，下限 **500 ps**。
- 走查里的说法（`01.07.01.04.03_Defining_the_equation_sets`）："Upon download, the syntax of your description is checked, and if you have made any errors you will be notified accordingly in the report window."

**波形目视**：wavetable editor 看物理波形表（PhyIndex / Action / DevCyc，向量里存的是指针）；时序图用 **Timing Diagram Tool**（`93000 > Results > Timing Diagram`），它显示实际送到 DUT 的波形、以及接收数据与期望不符的位置——**这是结果分析工具，主归属 [[results]]**，本阶段只把它当目视核对手段。

**推断：** 上述三条 GUI 路径（Show Eqn & Spec Results / Download 报错 / Check 菜单）加上 L1 的 `UPTD? TIM` 与校验查询族，构成文档给出的完整「timing 配对了没有」判据链；文档没有给出一条单一的「timing 验收清单」，这条链是合成的。

## 常见错误

### 1. EQNSET 与 SPECSET 单位冲突（文档明写的坑）

出处：`01.07.01.04.04_Defining_the_spec_sets`，小节 **Unit conflict between EQNSET and SPECSET**。下载时会报：

```
WARNING: Unit for spec variable "<variable>" in EQNSET <no>, SPECSET <no> is not
consistent (EQNSET unit: [<unit>], SPECSET unit: [<unit>]).
Only EQNSET units will be used. To overwrite SPECSET units with EQNSET units,
press "Download" and then save the setup.
To keep SPECSET units, edit EQNSETs and set the same units as in SPECSETs.
```

文档给出的成因：「This may happen, for example, after importing setups converted by STIL reader with version 2.1 or earlier.」两条修法（文档原文）：

- **以 EQNSET 单位为准** —— 在 Spec Tool 里点 `Download`，然后 `File > Save`。
- **以 SPECSET 单位为准** —— 手工编辑 equation based setup 文件，把 EQNSET 里的单位改成与 SPECSET 相同。

### 2. drive 边沿顺序违例，且跨平台表现不同

`02.06.06.01.03.01.02.01_Restrictions_for_drive_edges`：同一种动作类型的 drive 边沿必须与延迟先后顺序一致。**文档 CAUTION：同一份非法定义，在 Smart Scale 上得出 `0-0-0-0-0-1`，而在 Pin Scale 上得出 `0-0-1-1-1-0`。** 靠 `CHECK edgeorder_drv` 之类的检查抓。

### 3. receive 边沿顺序违例（window compare）

`02.06.06.01.03.01.02.02_Restrictions_for_receive_edges`：window compare 要求边沿在时间与编号上都递增，否则定义非法。

### 4. 多端口舍入问题

`02.06.06.01.06_Dealing_with_rounding_problems_in_multiport_setups`：period 定义里含除法会算出最多 9 位小数，必须舍入。纯 Smart Scale 端口下有两种症状：

- **System clock overflow** —— 各端口 ECLK 周期互质，最小公倍数（即 SCLK 周期）变得极大，轻则拖慢测试，重则超过允许的最大 SCLK 周期导致该 spec **不能使用**。
- **Distortion of ratios** —— 比例失真（文档用图说明偏移）。

两条规避路径：用 `fract()` 函数；或用不同的 clock group。

### 5. 在 Timing Setup 窗口里拖边沿改坏了 equation

`02.08.04.30.02.18`：拖过边沿后出现 `E` / EDITED 指示，表示图形化改动与 equation 不一致；用 `Edit > Restore` 恢复。**建议：** 改 timing 优先改 equation/spec 源文件，不要在图上拖。

### 6. 改了 wavetable 名字 / 删了 spec set 导致上传报错

`02.08.04.30.02.19_Error_Checking_Facilities`：upload 时会出现错误汇总屏；必须改正或删除。相关症状在 `02.08.04.34.04.03.06` 有报告文件的导出口。

### 7. timing 没定完就去搭向量

`02.08.04.34.06.11.02_Keeping_Waveform_Sets_Compatible`：**"You cannot start setting up vectors if the timing is not finished."** 该篇同时列出会让向量解释失效的「重大改动」：定义/改名/删除/复制 device cycle、定义 SCAN device cycle、改 receive pin 的参数值。**排查入口：** 向量结果莫名其妙时，先看 timing 是否在搭向量之后被动过。

### 8. mode context 不匹配

`02.08.04.34.05`：spec 指向的 wavetable 与 equation set 若 mode context 不同，定义直接非法。症状通常是下载/检查时报错而非静默出错。

### 9. 资源不够，下载被拒

`02.08.04.34.06.06.06`：用超了资源，系统**拒绝下载**并在 report window 报错。计数入口就是 `WSUS` / `TSUS` / `DSCP`（waveform set 上限默认 16、最大 16；全部 waveform set 的 timing set 总数默认 256、上限 512，单个 waveform set 最多 256）。

### 10. period 被自动修正

`02.06.06.01.04.01.02.02_Specifying_the_Period_Resolution`：`period_res` 没声明好时，period 会被自动修正（文档例子：35 ns / 5 ns → 26 修正为 25、49 修正为 50）。用 `VCLK?` 查是否会发生 auto-correction。

### 11. 在 API 与固件命令之间混改 spec

`02.06.06.02.31_SVLR` 与 `02.07.04.01.249_TIMING_SPEC` 两处都写了同一条 CAUTION：**「Never mix the LEVEL_SPEC or TIMING_SPEC API and firmware commands modifying values for other reasons than debugging purposes (see note below)!」** 另：`SVLR` 改的值不落盘，要永久生效必须改 setup 文件本身。

## 下一步

[[pattern]]

依据是文档的直接约束：「You cannot start setting up vectors if the timing is not finished.」（`02.08.04.34.06.11.02`）。向量里存的是指向物理波形表的指针（`02.08.04.16.04.05_Wavetables`：PhyIndex / Action / DevCyc），所以 timing 一改，既有向量的解释就变——必须先定死 timing 再搭 pattern。运行期若要换 timing set，用 [[ctim]] 在 sequencer 层面切换。

> 本阶段与 [[level]] 是并行的两个 setup 阶段，二者都必须在 [[pattern]] 之前完成；[[level]] 侧内容不在此复述。
