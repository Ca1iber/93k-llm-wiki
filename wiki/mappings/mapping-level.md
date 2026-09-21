---
type: mapping
title: Level 配置的三层对照
layer: n/a
stage: level
tags: [mapping, level, gui, firmware-command, test-method-api, level-file, level-master-file, spec-set, dps, dpspins]
related: [level, pin, timing, pattern, testmethod, level-file, level-master-file, level-equation-file, level-setup-tool, spec-tool, spec-set, test-program-explorer, dpspins-resources, equation-based-level-setup, report-window, hardware-view, lsus, dsus, dprl, sldo, spst, uptd, svlr, eqfs, eqsp, drlv, rclv, term, clmp, pslv, pssr, sqst, sprm, aprm, fw-task, level-spec, setup-level-set-0, primary-status, spec-search, test-suite-control-api, tpi-program-routines]
sources:
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03_Setting_up_your_levels.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04_Data_Organization_of_Equation_Based_Levels.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05_Data_Organization_of_Fixed_Levels.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02_List_of_level_setup_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.04_DPRL__DPRL__-__Default_PRimary_Level_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.05_DRLV__DRLV__-__DRive_LeVel.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.12_LSUS__LSUS__-__Level_Sets_USed.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.16_PSSR__PSSR__-_Power_Supply_Slew_Rate.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14_Level_setup_tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.01.03_Termination_types.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.01.06_Automatic_level_adjustment_for_series_resistance.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02_Equation_based_level_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.01_The_advantage_of_using_level_setup_file_to_store_all_the_level_sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03_Structure_of_an_equation_based_level_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.08_LEVELSET.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.08.01_IO_PINS_resources.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.09_Level_specifications.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.09.01_SPECSET.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.10_Error_Reporting.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05.01_Master_file_format_for_level_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05.02_Editing_the_level_and_timing_subfiles.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.03_Elements_of_the_Level_Setup_window.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.03.01_How_to_read_the_IO_Level_Setup_window.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04_Opening_and_using_the_Level_Setup_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.03_How_to_create_an_equation_set_using_the_Equation_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.05_How_to_set_the_driver_levels_for_differential_pins.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.06_How_to_set_the_driver_levels_for_single_ended_pins.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.11_Working_with_level_sets_and_DPS_sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.11.01_Setting_switching_order_modes_of_level_sets_and_DPS_sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.01.02.02_DPS_pins_with_voltage_ramps.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.01.03_Using_the_UNGANG_connect_state_with_DC_Scale_DPS_cards.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.02.06_Related_Firmware_Commands.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.16.01_Global_and_local_spec_values__scope_of_the_spec_variable.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.17_How_to_perform_a_measurement.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.06_TestsuiteProxy.getLevelSet.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.25_TestsuiteProxy.setEquationBasedLevel.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.03.04.12_Off_DC_levels_table.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Level 配置的三层对照

## 这张表在说什么

Level 这一段，语料里同样并存三套说法：Level Setup Tool / Spec Tool 上的操作（GUI）、
device 目录下的 level 文件（file）、以及 `02.06.05` 那一族固件命令（L1）。

**但和 pin 那一段不一样：level 语料里没有一句能覆盖整条链的总纲句。**
pin 的语料里有一句（`02.08.04.18.04_Pin_configuration_file.md`）：

> 「The file contains a set of firmware commands corresponding exactly to the parameters specified within the Pin Configuration tool.」

**level 这边没有这句话。** 本页在 level 家族的 GUI / 文件文档里 grep 过 `correspond`，
没有命中任何总纲式断言。level 是**逐点**给的，而且
**分两条路线给，两条的说法还不一样**。这两句话就是本页的地基：

**路线一 —— equation based（标准路线）：文件不是命令序列，是被整体下载的数据块。**
`02.08.04.14.02.05.02_Editing_the_level_and_timing_subfiles.md` 开头：

> 「Equation based level and timing setups are stored in the setup file as a string parameter of the EQSP firmware command, which serves to download the setup data to the tester.」

即：equation based 的 level setup 在文件里**不以固件命令的形态存在**，它是 `EQSP` 命令的
**一个字符串参数**。这一路线里「文件 ↔ L1」的关系不是「一行文件 = 一条命令」，
而是「**整个文件 = 一条 `EQSP` 的参数**」。

**路线二 —— fixed level setup：文件里的每一行就是一条固件命令。**
`02.06.05.01.05_Data_Organization_of_Fixed_Levels.md`：

> 「For a fixed level setup, you use firmware commands to specify the level values as constants within every level set.」

**两句合起来是本阶段的格式事实**：同一个 level 文件，equation based 时是数据块、
fixed 时是命令序列。所以主表里 L1 列填**具体命令**的那几行，
**只在 fixed 路线里成立**；equation based 路线对应的 L1 格是 `EQSP` / `EQFS`。
**这个分叉是语料自己写的，不是本页归纳的。**

（fixed 路线自 SmarTest 7.4.1T 起 discontinued，见 [[level]] 页「常见错误 10」。
本页照录它的写法，并在主表里标出它只服务于读老程序 / 调试。）

**「三层」这个词在本页要放宽理解**：§2.5 的格式给了五列（GUI / 文件 / L1 / L2 / L3），
而 level 这一段**前三层被语料钉得比较死**（链接证据见下一节），
**L2 在六个点上出现，L3 只在两个点上出现**。下面「对不上的地方」逐条说明。

## 对照表

**读法**：一格填了名字 = 有证据（证据是哪一档见下一节）；`?` = 语料没说，**本页不猜**；
`—` = 这一层不存在这个对应物（不是「没找到」）。**带（图证）的格 = 那一格的名字在 raw 的图上
直接看得见**——是哪张图、图里的字为什么搜不到，见证据节 **④** 与「对不上的地方」**⑧**。

| 目的 | GUI | 文件 | L1 命令 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 把 equation based level setup 下载到硬件 | Level Equation Editor 的 `Shell > Download` / **F8** | [[level-file]]（**整块**） | [[eqsp]] | ? | ? |
| 生成 equation set 骨架、LOAD / SAVE 临时文件 | Level Equation Editor 的 `Shell > Generate Level` / `Shell > Generate DPS` | [[level-equation-file]] | [[eqfs]] | ? | ? |
| 设驱动电平（`vil` / `vih`） | Level Setup window 的 `level [V] low/high` 列（**图证**）；level equations 里的 `vil` / `vih` | [[level-file]] 的 `PINS` 块 | [[drlv]] | ? | ? |
| 设比较阈值（`vol` / `voh` / `vth`） | 同上（`Select > Edit Equations` 打开 Level Equation Editor）（**图证**：同两列） | [[level-file]] 的 `PINS` 块 | [[rclv]] | ? | ? |
| 设端接方式（`term`） | Level Setup window 的 termination 列 / 面板（**图证**：列头逐字 `termination`） | [[level-file]] 的 `PINS` 块 | [[term]] | ? | ? |
| 设 clamp 电平（`vcl` / `vch`） | Level Setup window 的 clamp 面板（**图证**：图上不是「面板」而是两**列**，列头逐字 `clamp low[V]` / `clamp high[V]`——见「对不上的地方」⑧） | [[level-file]] 的 `PINS` 块 | [[clmp]] | ? | ? |
| 设 DPS 输出电压 / 电流限 / setting 时间 | Level Setup window 的 DPS pins view（**图证**：列头 `level [V]` / `current [A]`（`source` / `sink`）） | [[level-file]] 的 `DPSPINS` 块 | [[pslv]] | ? | ? |
| 设 DPS 断开后的 off 态电流（`offcurr`） | Level Setup window 的 DPS pins view（`Off-state current definition`）（**图证**：图上表头是缩写 `off cur.`，**不是** `Off-state current definition`） | [[level-file]] 的 `DPSPINS` 的 `offcurr` | [[pslv]] 的五个阻抗关键字 | ? | ? |
| DPS 的 connect state（含 `UNGANG`） | DPS Setup window 的 `conn state` 列（**图证**：列头逐字 `conn state`） | [[level-file]] 的 `DPSPINS` 的 `connect_state` | `PSLR`（+ `UHCM`、`DPSE`） | `DPS_PIN_TASK` 的 `measurementMode()` | ? |
| DPS 电压斜坡 / slew rate（`rise rate` 等八列） | DPS Setup window 的 `rise rate` / `rise settm` / `fall rate` / `fall settm` / `*_c2c` / `Tsetup` 列（**图证**：八列加 `Tsetup` 逐字可见） | [[level-file]] 的 `DPSPINS` 的 `vout_rise_t_ms_per_volt` 等 | [[pssr]] | ? | ? |
| 增删 level set / DPS set（个数与编号） | Level Setup window 的 `Lset #` / `DPSset #` 框；`Edit > copy set` / `Edit > delete set` | [[level-file]] 的 `LEVELSET` 块 | [[lsus]] / [[dsus]] | ? | ? |
| 把 Level Setup 工具**定位**到某个 set | Level Setup window 的 `Lset #` / `DPSset #` 框 | — | [[dprl]] | ? | ? |
| 在 testflow 里切 set 时的**先后顺序** | `Edit > Set Level Switching Order` | [[level-master-file]] 的 `GENERAL` 条目（`GENERAL.lev`） | [[sldo]] | [[fw-task]] | ? |
| 运行中切 level set | ? | — | pattern 指令 `CLEV` | [[primary-status]] | ? |
| 运行时改 spec 值并重算 | [[spec-tool]] 的 Download（`File > Download`） | [[level-file]] 的 `SPECS` / `SPECSET` 块 | [[svlr]] | [[level-spec]]、`Primary.getLevelSpec()` | ? |
| 把 primary 激活到硬件（frontend） | Firmware view 里敲 `APRM`（原文给的第三条路） | ? | [[sprm]] / [[aprm]] | ? | ? |
| 选「equation set + spec set + level set」三个坐标 | `Select > Select Specification`；`Lset #` | [[level-master-file]] 的 `EQNSET <n>: <file>` 条目 | ? | ? | `setEquationBasedLevel()` / `getLevelEquation()` / `getLevelSet()` / `getLevelSpec()` |
| 把整个 level 产物文件交给另一个进程 | [[test-program-explorer]] 的 Save | [[level-file]] / [[level-master-file]] | ? | ? | `DataManager` 的文件标识 `dm_level` |
| 验电平设置 / 查资源违例 | `Select > Show I/O Eqn. & Specs Results` 等三个结果窗口；report window | ? | [[uptd]] / [[spst]] / `RCLS?` / `CKST?` | ? | ? |
| 自动摆幅调整（mixed level device） | ? | ? | `ASWE` / `ASWM` / `SWNG` | ? | ? |
| Spec Tool 里做 search 测量 | [[spec-tool]] 窗口右上角的测量按钮 | ? | ? | [[spec-search]] | ? |
| level set 0（sequencer OFF 时的高阻态） | ? | [[level-file]]（**且只能是 fixed 形态**） | [[term]] / [[clmp]] / [[sqst]] | [[setup-level-set-0]] | ? |

**表里没有的**：`LSUX`、`DSCP`、`RSET` 这些**只在命令侧出现**的东西，本页不硬塞行；
`UPTD` / `SPST` / `LSUS` / `DSUS` 的 `?` 查询形式也不单独占行（它们与写形式同行）。
**凡是没有链接证据的命令，GUI 那一格的来源只有两种：文字平行（标推断）或 `?`**——
见「对不上的地方」③。

## 证据：哪几格是钉死的，哪几格只是「那边链过来了」

**证据分四档，本页不把它们混成一种。**

**① 文档明说对应（最硬）** —— 语料直接写出「A 与 B 是同一件事 / B 由 A 设」的句子，
不用我做任何配对。本页遇到**四处**，都不在 pin 那页那种总纲句的形式上，而是散在具体段落里：

`02.08.04.14.02.03.07_DPSPINS.md` 一句把 **GUI 列 + L1 命令 + 文件写法**三样并排给了：

> 「The default value norm of DPS pin resource connect_state can be selected for the conn state column in the DPS Setup window of the Level setup tool and can be programmed by the related command PSLR but cannot be programmed explicitly in the level setup equations.」

`02.08.04.14.06.01.03_Using_the_UNGANG_connect_state_with_DC_Scale_DPS_cards.md` 把
**文件写法（equation）+ L1 + L2** 三样并排：

> 「You can set the UNGANG mode with the connect_state parameter of an equation based level setup or with the PSLR firmware command:」

> 「The connect state UNGANG can be combined with an unganged current measurement (the MEASURE_CURRENT_UNGANGED parameter in the measurementMode() member function of the DPS_PIN_TASK API, or the template parameter "3" of the DPSE firmware command).」

`02.08.04.14.04.11.01_Setting_switching_order_modes_of_level_sets_and_DPS_sets.md` 把
**GUI 菜单 + 文件落点 + L1 + L2** 四层一次给全 —— **这是本页唯一一条四个层同时有文档依据的行**
（L3 那格仍是 `?`）：

> 「If you edit the settings in the level master file and save the file, the change will be saved in the GENERAL entry of the level master file.」

> 「If you want to apply different switching order modes during the execution of a testflow, execute firmware command "SLDO" by using FW_TASK API.」

`02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool.md` 给了 **Spec Tool ↔ `APRM`** 的直连：

> 「Unlike the Level setup tool, the Spec Tool does not automatically update the frontend of the hardware.」

> 「or invoke the FW command APRM in the Firmware view tab.」

**② 文档之间有链接（次硬，逐条可查）** —— 这些是语料里**实际存在的跨层链接**。
本页把「GUI 章 / 文件章」的文档链到 `02.06` / `02.07` / `02.09` 的边取出来，
**先把互相重复投放的剔除**（见「对不上的地方」②），剩 **60 条边 / 47 对**
（`extract/edges.jsonl`，源取 `02.08.04.14*` / `02.08.04.30*` / `01.07.01.03*`，
目标取 `02.06*` / `02.07*` / `02.09*`，再剔掉「源与目标同源」的那些）。
其中落在主表某一行上的：

| 源文档（GUI / 文件侧） | 链到 | 落在哪一行 |
|---|---|---|
| `02.08.04.14.01.03_Termination_types.md` | `TERM` | 设端接方式 |
| `02.08.04.14.03.01_How_to_read_the_IO_Level_Setup_window.md` | `TERM` | 设端接方式 |
| `02.08.04.14.04.08_How_to_set_the_termination_for_DUT_outputs.md` | `TERM` | 设端接方式 |
| `02.08.04.14.02.03.07.01_DPSPINS_resources.md` | `PSLV`（6 处）、`PSLR`、`UHCM` | DPS 电压 / off 态电流 |
| `02.08.04.14.02.03.07_DPSPINS.md` | `PSLR` | connect state |
| `02.08.04.14.06.01.03_Using_the_UNGANG_…_cards.md` | `PSLR`、`DPSE`、`DPS_PIN_TASK` / `measurementMode()` | connect state |
| `02.08.04.14.06.01.02.02_DPS_pins_with_voltage_ramps.md` | `SPRM` | primary 激活 |
| `02.08.04.14.06.02.06_Related_Firmware_Commands.md` | `ASWE` / `ASWM` / `SWNG`（**整篇正文就是这三条链接**） | 自动摆幅调整 |
| `02.08.04.14.02.05.02_Editing_the_level_and_timing_subfiles.md` | `EQSP`（4 处）、`DFTD` | 下载到硬件 |
| `02.08.04.14.02.05.01_Master_file_format_for_level_setup.md` | `DFTD` | 整块搬运 |
| `02.08.04.14.04.11.01_Setting_switching_order_…_sets.md` | `SLDO` | 切 set 顺序 |
| `02.08.04.30.02.16.01_Global_and_local_spec_values_….md` | `SVLR`（2 处） | 运行时改 spec 值 |
| `02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool.md` | `APRM` | primary 激活 |
| `02.08.04.30.02.17_How_to_perform_a_measurement.md` | `SpecSearch` | Spec Tool 测量 |

**反向的链接也有一批**（L1 / L2 那侧主动链过来），本页同样只看**同一行**：

| 源文档（L1 / L2 侧） | 链到 | 落在哪一行 |
|---|---|---|
| `02.06.05.02.16_PSSR` | `Voltage ramps`（`02.08.04.14.06.01.02.02.01`） | DPS 电压斜坡 |
| `02.06.02.02.197_PSSR`（字母序投放） | 同上 | 同上 |
| `02.06.05.01.04.02.05_DPS_module` | `DPSPINS` / `DPSPINS resources` | DPS 各行 |
| `02.06.05.01.04.02.03_Specs_module` / `.02.09_Spec_sets` | `Spec Tool` | 运行时改 spec 值 |
| `02.06.05.01.04.03.01_Verifying_the_level_settings` | `Opening and using the Level Setup Tool` / `Working with level sets and DPS sets` | 验电平设置 |
| `02.06.02.02.68_DFTD` | `Level setup master file` | 整块搬运 |
| `02.07.04.01.124_LEVEL_SPEC` | `SVLR` | 运行时改 spec 值 |
| `02.07.04.01.50.01_DPS_PIN_TASK` | `DPSPINS resources`（`capacitance` 等） | DPS 各行 |
| `02.07.04.01.167_PRIMARY_STATUS` | `CLEV` / `CTIM` 所在的 sequencer 指令页 | 运行中切 level set |
| `02.07.05.04.06_SetupLevelSet0` | `Controlling high-Z behavior…` / `Pull-down function` | level set 0 |
| `02.07.04.01.125_LEV_TRANSFER_TASK` / `.125.01` | `Equation based level setup` / `Level sets` | 下载到硬件 |
| `02.08.04.14.02.03.08.01_IO_PINS_resources` | `TERM`、`Supported level resources`、`Concepts of level setup` | 设端接方式 |
| `02.08.04.14.02.03.10_Error_Reporting` | `Command Reference`（**只到章级，没到具体命令**） | 验电平设置 |

**链接证的强度要说清**：一条链接**只证明「那篇文档认为读者该去看这一篇」**，
**不证明两个东西等价**——可能是「见也」，也可能是「区别在这里」，也可能是「前提」。
本页只在主表的**同一行**里用它们，**不跨行搬**。

**③ 只有一档文字证据、没有链接的（本页标为推断）** —— 这些行**必须标（推断）**，
理由是语料给了两侧各自的说法，**但没有任何一句把它们连起来**：

- **设驱动电平 / 设比较阈值 / 设 clamp 电平**（`vil`/`vih`、`vol`/`voh`、`vcl`/`vch` ↔
  `DRLV`/`RCLV`/`CLMP`）。依据是 `02.08.04.14.04.06` 明写「在 level equations 里设
  `vil = drive low level` / `vih = drive high level`」，而 `02.06.05.02.05_DRLV` 自述
  「defines the low and the high voltage levels for the driver amplifiers」——
  **两侧的资源名与职责对得上，但没有一句说「GUI 上这一列 = 这条命令」**。
  这一档里唯一到过链接的是「设端接方式」（`TERM`，三条链接）。
- **增删 level set / DPS set ↔ `LSUS` / `DSUS`**。依据是**两篇文档用了几乎同一句话**：
  GUI 侧 `02.08.04.14.04.11`：

  > 「If the level setup file that you want to load to hardware contains more level sets than you require for the test, you can delete the unwanted sets.」

  命令侧 `02.06.05.02.12_LSUS`：

  > 「If the level setup file that you want to load to hardware contains more level sets than you require, you can use the LSUS command to delete all the sets above the number you specify.」

  **同一段论证、同一个「删掉编号以上的所有 set」的操作**，只是 GUI 侧停在
  `Edit > delete set` + `delete sets above #`，命令侧落在 `LSUS`。
  **这仍属推断**：语料没写「GUI 的 delete set 就是 `LSUS`」。
- **把工具定位到某个 set ↔ `DPRL`**。`02.06.05.02.04_DPRL` 自述：

  > 「The DPRL (Default PRimary Level sets) command is used to place the level setup tool on the specified set.」

  **它自己就点名了「level setup tool」**，而 `Lset #` / `DPSset #` 框是那个工具上的东西——
  但**没有链接**，也没有一句说这两个是同一个动作。故标推断。
- **`offcurr` ↔ `PSLV` 的五个阻抗关键字**。这条其实**几乎是文档事实**：
  `02.08.04.14.02.03.07.01_DPSPINS_resources.md` 把五个取值**逐个**配了 `PSLV` 关键字：

  > 「Use min (minimum current) for high impedance (HIZ in the PSLV command).」

  > 「Use act (actual current) for low impedance (LOZ in the PSLV command).」

  > 「Using act_min is safer when changing the DUT or DUT board after a disconnect (LOZ_HIZ in the PSLV command).」

  > 「Using act_open is safer when changing the DUT or DUT board after a disconnect (LOZ_HIZ_R in the PSLV command).」

  （第五个 `open` ↔ `HIZ_R` 在同页另一处，本页不重复引。）
  **「文件取值 ↔ L1 关键字」这一层是明说的**；**「GUI 上这一格 = 文件的这一格」才是推断**——
  依据是 `02.08.04.14.03_Elements_of_the_Level_Setup_window` 的 DPS view 列了
  `Off-state current definition` 这一项。

**附：反向推论（有些行是「L1 侧有名字、GUI 侧没有」）** ——
主表里 GUI 列是 `?` 而那些行 L1 / L2 有值的（`CLEV`、`ASWE`/`ASWM`/`SWNG`、
自动摆幅那一行），**`?` 的意思是「本页没找到证据」，不是「不存在」**。
其中自动摆幅那一行有个细节值得记：`02.08.04.14.06.02.06_Related_Firmware_Commands.md`
**整篇正文就是三条命令的链接列表**，标题叫 `Related Firmware Commands`——
**它是一篇「GUI 章里的固件命令附页」，而不是一篇讲 GUI 的文档**。

**④ 图证（2026-09-20 加，本页用到了）** —— 从 raw 自带的截图里读出来的。
（`schema.md` §2.5：**④ = 图证**。）

**本页 sources 里带图的文档共 17 篇 / 27 张。本页读了三张**，**其余二十四张没看**
（多数是对话框与示意小图，另有 `25798.png` 那张 active load 电路图）。
**先给结论：level 这一页的图，收成比另外五页都薄。** 三张图**没有填掉任何一个 `?`**
（本页 `?` 几乎全在 L2 / L3 两列，**图里连一个 API 名都没有**），
**也没有把任何一格（推断）升成文档事实**——**因为三张图里都没有文件内容**。
它们**唯一**贡献的东西是一条**图上才有的字面**，见（a）末段。逐张：

**（a）`116503.png`（`02.08.04.14.03`，alt `Level Setup window displaying I/O pins`）
—— 同一张图也被 `02.08.04.14.03.01` 引用。** 图是 Level Setup 窗口的 **I/O pins 视图**。
**先记最要紧的一处**：**标题栏逐字是 `Level Setup`，右上角显示的文件名逐字是 `lev_format`。**
`lev_format` 这个串**在 9,398 篇 raw md 里 0 命中**——它**只在这张图上**。
**这恰好落在本页 `文件` 列要回答的那个问题上**（「GUI 在编哪个文件」），
**但它只给了文件名，没有给内容**——所以本页的 `文件` 列**一格都没有据此改动**。

图上其余逐字可读的是：字段 `Eqn# [1]`、`SpS# [1]`、`Lset# [1] of 1`、`Level: Nominal`、
`Specification: no_spec`、`Equation: NonSpec`，按钮 `Diff` / `Fast`；表头
`pin/group name | pin type | level [V] low | level [V] high | mode | lev/v3h | Iol[mA] | Ioh[mA] |
swing | termination | offsel | pulldown | H R mode | clamp low[V] | clamp high[V] | range [V/mA]`；
行有 `ser_in` / `ser_out` / `io_in` / `io_out` / `ctrl` / `aviPin`（`pin type` 为 `i` 或 `o`）。
**它印证了主表四行的 GUI 格**（已在表里标「（图证）」）：设驱动电平 / 设比较阈值（`level [V] low` /
`level [V] high` 两列）、设端接方式（`termination`）、设 clamp 电平（`clamp low[V]` /
`clamp high[V]`）。
**要分开说的是这三处哪一处算新证据：**
- `level [V] low` / `level [V] high` 与 `termination` **在本页 sources 的正文里都有**
  （`.14.04.05` / `.14.04.06` 的 `level [V] low and high columns`、`.14.03.01` 的
  `## termination` 小节）——**图在这里只是「同屏可见」，不算新证据**。
- **`clamp low[V]` / `clamp high[V]` 与 `offsel` / `Iol[mA]` 这几个串 raw 里 0 命中**
  （`clamp low` 只在别的篇里以 `clamp low` 的散字出现，**不是这个列头**）。
  `.14.03.01` 的 `## clamp` 一节写的是 **`The clamp panel shows the clamp mode and the two clamp
  voltages vcl and vch.`**——**正文说的是「面板」，图上排成两列**（见「对不上的地方」⑧）。
- **`H R mode` 这一串 grep 不到，但别上当**：正文里写的是 **`HR mode`**（`.14.03.01` 有
  `column HR mode`，`.14.03` 的 Functional changes 里有 `New columns "HR mode" and "range"`），
  图上那个表头是**分两行排的 `H R` / `mode`**。**本页不把换行当成语料差异。**

**（b）`21760.png` 与 `150668.png`（`02.08.04.14.06.01.02.02`）—— 一对 DPS pins 视图。**
两张的标题栏也是 `Level Setup`，右上角也是 `lev_format`（**与（a）同一窗口的另一个视图**）。
`21760.png` 的列是 `dps pin name | level [V] | current [A]`（下分 `source` / `sink`）`| off cur. |
V Range [V] | I Range [A] | V Bump / state`；`150668.png` 的列是 `dps pin name |
rise rate [ms/V] | rise settm [ms] | fall rate [ms/V] | fall settm [ms] | rise rate c2c [ms/V] |
rise settm c2c [ms] | fall rate c2c [ms/V] | fall settm c2c [ms] | Tsetup [ms] | cc check |
conn state`。两张都只有一个 `Vcc` 行与一个 `Vee` 行。
**它印证了主表三行的 GUI 格**（DPS 电压斜坡八列加 `Tsetup`、connect state 的 `conn state` 列、
off 态电流的 `off cur.` 列）。
**这三处里，只有一处算新证据**：`off cur.` 这个**缩写表头**——
本页 sources 的正文里那一格叫 **`Off-state current definition`**（`.14.03` 的 DPS 小节
与 `.14.03_Elements…` 的列表），**而 `off cur.` 这个缩写只出现在 `.14.03.02` 与
`.14.06.01.01` 两篇里，那两篇都不在本页 sources**——
**本页只从 grep 知道这个缩写在语料别处被用过，没有读过它的定义**。**八列 slew rate 与 `conn state`
在正文里都有**（`.14.06.01.02.02` 的九个列表项、`.14.02.03.07` 的
`conn state column in the DPS Setup window`）——**图不算新证据**。
**图里没有的东西要说清**：两张图里**没有任何一行的文件内容**——
`vout_rise_t_ms_per_volt` 之类的**文件关键字一个都没出现**。

**（c）三张图在 raw 里 grep 不到的字，汇总成一句**：
`lev_format`（0）、`offsel`（0）、`Iol[mA]`（0）、`clamp low[V]`（0）、`range [V/mA]`（0）
——**就这五个**。**其余表头在本页 sources 的正文里都能搜到**，
所以本页**不把它们算作图证**（§11.4 的判据是「拿图里的字去 raw 里 grep 是 grep 不到的」）。

**图证整体答不了的三件事，照实说：**

- **三张图没有一个文件关键字、没有一条固件命令名、没有一个 API 名。**
  所以本页 `L1` / `L2` / `L3` 三列**一格都没动**，③ 档里那些（推断）**全部留在原处**。
- **「GUI 的哪一列 = 文件的哪个关键字」三张图一张都没答**——**因为图里没有文件内容**。
  这一句正是原先 ⑧ 说错的地方，见「对不上的地方」⑧。
- **图是「某一次具体配置」的截图，不是格式规范。** 「哪些列必填、哪些组合非法」
  **图答不了**——那是文本的事，而 `.14.03.01` 里也只写了其中几列。

## 对不上的地方

**① 本页取不到 pin 那种总纲句，这是 level 这一段的结构事实。**
pin 用一句 `corresponding exactly to` 覆盖了整条链；level **没有这句**，
因为 level 有**两条互斥的路线**（equation based / fixed），两条的文件语义不同
（数据块 vs 命令序列）。所以本页的证据粒度只能**逐行**给，
**没有一行可以借用另一行的背书**。

**② 语料把同一篇页投放在多个章下，level 这一段尤其密——本页先把它们剔除。**
判据是 §10 的：`source_topic` 去掉 `_2` 之类的后缀后相同，就是同一篇。
实测本页证据涉及的文档里，**20 篇的某一份投放与另一份同源**；其中直接落在本页证据上的有：

| 同一篇 TDC 页的两份投放 | |
|---|---|
| `02.08.04.14.01_Basic_concepts_of_levels` | `02.06.05.01.01_Basic_concepts_of_levels` |
| `02.08.04.14.01.03_Termination_types` | `02.06.05.01.01.03_Termination_types` |
| `02.08.04.14.01.04_Clamping` | `02.06.05.01.03_Clamping` |
| `02.08.04.14.02.02_Elements_of_Equation_Based_Level_Setup` | `02.06.05.01.04.01_Elements_of_Equation_Based_Level_Setup` |
| `02.08.04.14.02.03.08.01_IO_PINS_resources` | `02.06.05.01.04.02.07_IO_PINS_resources` |
| `02.08.04.14.02.03.10_Error_Reporting` | `02.08.04.34.04.03.06_Error_Reporting` |
| `02.08.04.14.02.05.02_Editing_the_level_and_timing_subfiles` | `02.08.04.34.04.05.02_Editing_the_level_and_timing_subfiles` |
| `01.07.01.03_Setting_up_your_levels` | `02.08.04.14.04.01_Setting_up_your_levels` |
| `01.07.01.03.02_How_to_create_an_equation_set…` | `02.08.04.14.04.03_How_to_create_an_equation_set…` |
| `01.07.01.03.03_Creating_new_specification_sets` | `02.08.04.14.04.04_…` 与 `02.08.04.30.02.01_…`（**三份**） |
| `01.07.01.03.04_Verifying_the_level_settings` | `02.06.05.01.04.03.01_Verifying_the_level_settings` |

**为什么这件事必须先做**：`02.08.04.14.02.03.08.01_IO_PINS_resources` 里那 18 条指向
`vil` / `vih` / `vcl` / `term` … 的链接，**目标全是同一篇页的另一份投放**
（`02.06.05.01.04.02.07`）——**那不是「GUI 链到 L1」，那是一篇文档在自己内部跳锚点**
（链接目标带着 `#_16891__r_vil` 这样的锚）。**不剔除，本页的 L1 列会被这批假证据填满。**
同理，`02.08.04.14.01.03_Termination_types` 与 `02.06.05.01.01.03_Termination_types`
是同一篇，所以「哪一份算 GUI 章、哪一份算命令章」**在语料层面没有唯一答案**，
本页在证据表里**按路径前缀归章**，并把这个不确定性写在这里。

**③ L1 列只覆盖语料链过的那些命令。** `LSUS`、`DSUS`、`DPRL`、`EQFS`、`UPTD`、`SPST`、
`DSCP`、`RSET`、`LSUX` 这九条命令，**本页在 level 的 GUI / 文件侧文档里一条链接都没找到**
（查过 `extract/edges.jsonl`：这些命令页的入链全部来自 `02.06` 自己的命令列表页、
`index.md`、或其他命令页）。所以**靠这九条中的任何一条成行时，GUI 格要么来自文字平行
（本页标推断）、要么是 `?`**——`LSUS` / `DSUS` / `DPRL` 三行走的是前者（见「证据」节 ③），
其余一律 `?`。**这两种来源本页在表里长得一样，区别只写在证据节里，
读表时别把它们当同一种证据。**
**九条里 `EQFS` 是唯一 L1 格没留 `?` 的，理由方向不同**：它自己没有入链，但
`02.08.04.14.02.05.02` **链到了 `EQSP` 而不是 `EQFS`**——本页在「生成骨架 / LOAD·SAVE」
那一行填 `EQFS`，依据是 `02.06.05.02.09_EQFS` 自述：

> 「The EQFS command provides the load/save operations required by the editor tools for loading/saving the equation based testing files from/to temporary files.」

**它点名了 `the editor tools`，所以这一格是文档事实；但「编辑器里哪个动作」是推断。**

**④ L2 / L3 两列的 `?` 多于名字，这是 level 这一段与 pin 那一段最大的不同。**
pin 的对照页（`wiki/mappings/mapping-pin.md`）把 L3 整列判成 `—`，
给的理由是「pin 定义是 setup 期动作，外部进程插不进来」。
**level 不能照搬这个写法**——L3 在 level 上**确实有口**，而且有**两个**：

> 「This function sets the equation based level information to the test suite.」

（`setEquationBasedLevel(levelEquation, levelSpec, levelSet)`，SmarTest 6.5.2 引入）
以及 `getLevelEquation()` / `getLevelSet()` / `getLevelSpec()` 三个读口，
`02.09.01.14.02.01.06_TestsuiteProxy.getLevelSet.md` 的例子：

> 「This function gets the level set used in the test suite.」

第二个口是**整个文件**：`02.09.01.09.02_DataManager.md` 的文件标识表里有
`dm_level` 一行，意思是 `level setup`，挂 `dm_load` / `dm_save` / `dm_merge` /
`dm_copy_in` / `dm_delete` 五个操作。

**但除这两个口以外，本页一条 L3 证据都没有**（GUI / 文件侧文档**一条 02.09 链接都没有**；
唯一的 02.09 → level 文档的边来自 MTP 的 `offdclevels.csv`，见 ⑤）。
**本页因此把 L3 列写成 `?` 而不是 `—`**：
`—` 是「这一层不存在这个对应物」的断言，而本页**证不了**「L3 没有逐资源的电平接口」——
按 §2.1 的规矩，**全称否定句举证责任在写的人**，证不了就写「本次未找到」。
（**这一条与 pin 页的处理不同，但不是冲突**：pin 页给出的是「定义动作外部插不进来」这条
结构性理由；level 这一页**不去替 pin 页翻案**，只说明本页为什么不照搬那个写法。）

**⑤ 三个同形陷阱 —— 名字里有 level，但不是本阶段的 level。**
写在这里是因为它们极容易被拿去错误地「补」本页：

- **MTP 的 `offdclevels.csv`**（`02.09.03.04.12_Off_DC_levels_table.md`）：
  它的列名是 `vout` / `ilimit` / `offcurr`，取值是 `min` / `act` / `open`——
  **和本页 DPS 行用的词一模一样**。但它是 **MTPT（STPM MCM mapping tables）** 里给
  **inactive STP** 用的表，存在 MTPT 目录，由 `generate_template` 生成，
  **与 level 文件、Level Setup Tool 无关**。**词同、物不同，本页不合并。**
- **HVM 的 `GetLevelProfile`** 与 **BLC 的 `Level_control_API`**：见 [[level]] 页「L3 — 外部控制」
  的同一节——那是 **application model 的层级结构**与**产线层级（lot / wafer / die）**，
  不是电压 level。**本页未读这两篇原文，此处转录 [[level]] 页的判定。**

**⑥ 语料自带的编码损坏，本页照原样记下、一处都不替它改（§11.2）。**
本页读到的三处坏字**不是** §11.2 ① 记的 `鈥` 那一族——
本页在 level 家族里没引用到 `鈥`——而是**同一机制的另外三个字**：

| 本页读到的坏字 | 出处 | 按上下文应为什么（**推断**） |
|---|---|---|
| `碌A` | `02.08.04.14.06.01.03`（`100碌A`） | `µA` |
| `渭F` | `02.08.04.14.02.03.07.01_DPSPINS_resources`（`Capacitance in microfarads (渭F)`） | `µF` |
| `卤50 mV` | `02.08.04.14.02.03.07.01_DPSPINS_resources`（`reached 0 V (卤50 mV)`） | `±50 mV` |

**推断链**：三者都出现在「本该是 U+00B5 / U+03BC / U+00B1 的位置」，
且形态与 §11.2 ① 说的「UTF-8 被按 GBK 读」一致（`C2 B5` 按 GBK 读成 `碌`，
`CE BC` 读成 `渭`，`C2 B1` 读成 `卤`）。**本页据此判为同一类损坏，但这是推断，不是文档事实**——
§11.2 ① 列出的原字符里没有这三个，**本页不替它扩表**，只把本页读到的三处记在这里。
**引文中的这三处一律原样抄，不做修正。**

**⑦ 语料一处自相矛盾，本页照实记下、不选一个。**
`02.08.04.14.03_Elements_of_the_Level_Setup_window.md` 正文第一句：

> 「The Level Setup window contains four main views:」

**紧跟着列了五项**：`I/O pins`、`DPS pins`、`I/O pins with Equations and Specifications`、
`FAST pins with Equations and Specifications`、`DPS pins with Equations and Specifications`。
（**这五项是本页转述的，不是引文**——`four` 与五项的这一处不一致是语料原文如此，
本页**不改数、也不删项**。按 §10 并列记录，等实机确认。）

**⑧ 图能读，本页读了三张——原先这一节有两处错，都得改。**（**2026-09-20 更正**）

**错处一：理由不成立。** 原先写「raw 里的图片路径向上爬四层，在语料树之外」——
**路径是对的、图是读得出来的**：`../../../../raw/x.png` 往上四层正好是 `tdc-html/`，
图就在 `tdc-html/raw/` 里（`schema.md` §11.4）。**一个不成立的理由，
会把一整档证据永久关在门外。**

**错处二：原先那句「那两张图就直接画着『GUI 的哪一列 = 文件的哪个关键字』」——这话是假的。**
**三张图本页都开了，它们画的是纯 GUI。** 具体说：
`02.08.04.14.06.01.02.02` 那两张（`21760.png` / `150668.png`）里，
**只有一个 `Vcc` 行和一个 `Vee` 行两行数据、十来个列表头**——
**没有一个文件关键字、没有一行 `DPSPINS` 内容、没有一条固件命令**。
它们**证明不了「哪一列 = 哪个关键字」**，因为**对照的另一半根本不在图上**。
`116503.png` 同样只有 GUI（逐字内容见证据节 ④（a））。

**所以这一节的结论要拆成两半，而且两半都是新写的：**

- **「哪一列对哪个关键字」仍然是 `?` 级别的空白，但理由换了。**
  不是「图够不着」，是**这三张图里本来就没有文件内容**——
  本页 sources 里的图**一张都没画文件**。所以 ③ 档里那些（推断）
  **一律留在推断**，**本页一格都没升**。
- **图唯一给到的新字面是 `lev_format`**——三张图的标题栏都是 `Level Setup`，
  右上角都显示这个文件名。**这个串 raw 里 0 命中。**
  它**正好是本页 `文件` 列关心的那个位置**（「GUI 在编哪个文件」），
  **但它只是文件名，没有内容**，所以本页**没有据此改动任何一格**。

**一处要照实记的用词差**：本页表里「设 clamp 电平」那一行的 GUI 格写的是
**「clamp 面板」**（跟着 `.14.03.01` 正文的
`The clamp panel shows the clamp mode and the two clamp voltages vcl and vch.` 走），
**而图上是两列表头 `clamp low[V]` / `clamp high[V]`**。
**同一个东西，正文叫「面板」、图上排成两列**——**本页照实并列，不替语料改词**
（也**不据此断言**这两者一定指同一块地方）。

**另一处值得后续单独查的**：`02.08.04.14.06.01.02.02` 在两张 DPS 图后面逐字写着
`For a description of the columns in first figure see How to read the DPS Setup window.`，
指向 `02.08.04.14.03.02`——**那一篇不在本页 sources 里**。
所以图上那批**只在图里出现的列头**（`offsel` / `Iol[mA]` / `range [V/mA]` / `off cur.`）
**本页没有它们的定义**。**这一条值得后续单独查一次。**

## 出处

`sources:` 四十六篇（见 frontmatter）。**引用只来自其中十五篇**，
**另有三十一篇只用来取事实与链接、本页没有引它们一个字**。具体分工：

- **引用过的（15 篇，其中 1 篇只分段读）**：`02.08.04.14.02.05.02`、`02.08.04.14.02.03.07_DPSPINS`、
  `02.08.04.14.02.03.07.01_DPSPINS_resources`（**分段读，未通读**）、`02.08.04.14.03`、
  `02.08.04.14.04.11`、`02.08.04.14.04.11.01`、`02.08.04.14.06.01.03`、
  `02.08.04.18.04_Pin_configuration_file`、`02.08.04.30.02`、
  `02.06.05.01.05_Data_Organization_of_Fixed_Levels`、`02.06.05.02.04_DPRL`、
  `02.06.05.02.09_EQFS`、`02.06.05.02.12_LSUS`、
  `02.09.01.14.02.01.06_TestsuiteProxy.getLevelSet`、
  `02.09.01.14.02.01.25_TestsuiteProxy.setEquationBasedLevel`。
- **整篇读完、只取事实不引用（28 篇）**：level 工具族与 Spec Tool 族的其余 22 篇
  （`02.08.04.14`、`.14.01.03`、`.14.01.06`、`.14.02`、`.14.02.01`、`.14.02.03`、
  `.14.02.03.08`、`.14.02.03.08.01`、`.14.02.03.09`、`.14.02.03.09.01`、`.14.02.03.10`、
  `.14.02.05.01`、`.14.03.01`、`.14.04`、`.14.04.03`、`.14.04.05`、`.14.04.06`、
  `.14.06.01.02.02`、`.14.06.02.06`、`02.08.04.30`、`02.08.04.30.02.16.01`、
  `02.08.04.30.02.17`），加 `01.07.01.03_Setting_up_your_levels`、
  `02.06.05.01.04_Data_Organization_of_Equation_Based_Levels`、
  `02.06.05.02_List_of_level_setup_commands`、`02.06.05.02.05_DRLV`、
  `02.06.05.02.16_PSSR`、`02.07.04.01.124_LEVEL_SPEC`、
  `02.09.01.14.02.01_TestsuiteProxy`（只整读了它的成员清单）。
- **只读了头部或片段的（3 篇）**：`02.09.01.09.02_DataManager`（只读了文件标识表与
  `dm_*` 操作那两段，用来写 L3 那一格与 `dm_level` 的五个操作）、
  `02.09.03.04.12_Off_DC_levels_table`（只读了前 30 行，用来写陷阱 ⑤）、
  `02.08.04.14.02.03.07.01_DPSPINS_resources`（见上）。
  后两篇**都不在引用块里**。

**本页没做的**：

- **一条 `02.06` / `02.07` 命令页的参数表都没逐条核。** 主表 L1 / L2 列那些命令名与 API 名，
  依据是**它们自己的首段自述**与**链接关系**；参数、返回值、语法，
  **本页一个字没有**——那属于对象页（§2.2）。
- **没有读过任何一篇 `02.09.01.09`（TPI）的正文**，`dm_level` 只见到
  `02.09.01.09.02_DataManager` 里的一行表格、一个 `level setup` 说明，
  以及 `dm_load` / `dm_save` / `dm_merge` / `dm_copy_in` / `dm_delete` 五个操作的说明行。
  **「这五个操作对 `dm_level` 都适用」是本页的推断**（该表把操作与文件标识分两张表列，
  没有逐格给出交叉）——原文只给了操作各自的定义（如 `dm_load` = `replace current setup by file`）。
- **`02.07.11.01.05.01_Level_equation_file` 与 `02.07.13.12.02.38_ungang` 只见到链接，
  没读正文。** [[level]] 页把前者记成 level equation file 的定义页，
  而它的路径在 `02.07`（L2 章）下，**与「文件」这一层不一致**，
  **本页没查、也没敢合并**——这一条值得后续单独查一次。
- **看了三张图（2026-09-20 加）。** 就是 `116503.png`、`21760.png`、`150668.png`
  （各自出自哪篇、图里逐字有什么，见「证据」④ 与「对不上的地方」⑧）。
  **三张都整张看完**，图上读到的字**逐条回 9,398 篇 raw md 里查过 grep 命中**——
  本页凡写「grep 不到」的都是实测 0 命中。**本页 sources 里带图的文档共 17 篇 / 27 张，
  其余二十四张没看**。**原先本页在「对不上的地方」⑧ 里写着图「在语料树之外」——
  那是错的**，见 ⑧ 的更正。
- **没有实跑。** 没有在机台上开过 Level Setup Tool、没有生成过 level 文件、
  没有用 `extract/wiki-plan.csv` 之外的任何数据校对过本表。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/level.md`。
  后者是**待办**：level 那页目前不知道本页存在。

**本页 `layer: n/a` 的理由**：§6 要求 mapping 页必填 `layer`，而本页**本身不属于任何一层接口**
（它是对照表，不是接口）——`n/a` 是这个六值枚举里为这种情况准备的值。

**引文规范化的说明**：本页引用块里的英文，**除 §11.1 允许的六条**（折叠空白、
剥 markdown 链接标记、去 `**` 与反引号、去中日韩引号、统一破折号、统一弯引号）**之外，
一个字符都没动**。特别地：`02.08.04.14.02.05.02` 那句原文里 `EQSP` 是语料内部链接，
本页把**链接名放在引号外**（写成 `EQSP`），引号里只留纯文本；
`02.08.04.14.04.11.01` 那句原文里的 `"SLDO"` 带**直双引号**，**本页照原样保留**。

`verified: doc-only`
