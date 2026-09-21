---
type: mapping
title: Timing 配置的三层对照
layer: n/a
stage: timing
tags: [mapping, timing, wavetable, gui, firmware-command, test-method-api, external-api, timing-setup-file, timing-master-file]
related: [timing, timing-setup-tool, spec-tool, timing-diagram-tool, waveform-view, wavetable, wavetable-file, timing-equation-set, timing-specification, timing-file, timing-master-file, waveform-set, timing-spec, timing-set-selector, spec-set, spec-value, spec-variable, primary-status, spec-search, timing-setup-commands, wsus, tsus, tsux, eqfs, eqsp, sprm, aprm, svlr, spst, uptd, vclk, vtim, vwfg, vwfs, vdcg, ctim, edsp, strs, dprt, etim, etds, pclk, clkr, pdiv, dcdt, wfds, wave, bwdf, bwds, jscf, jsdf, jspr, jsud, jswf, mscf, msdf, jrst, ps1600, conf, ctxt, dfgp, dscp, test-program-explorer, setup-management-tool, device-directory, test-suite-control-api, tpi-program-routines]
sources:
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.02_Setting_up_the_wavetables.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.109_EQSP__EQSP__-__EQuation_SPecification_transfer.md
  - 02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02_List_of_timing_setup_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.01_APRM_-__Activate_PRiMary_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.13_EQFS_-__EQuation_FileS_command_transfer.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.28_SPRM__SPRM__-__Set_PRiMary_sets.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.29_SPST__-__SPecset_STatus.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.32_TSUS__TSUS__-__Timing_Sets_USed.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.34_UPTD__UPTD__-__UP_To_Date.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.46_WSUS__WSUS__-__Waveform_Sets_USed.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.01_Principles_of_jitter_injection.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.02_JSCF__JSCF__-__Jitter_Set_ConFiguration.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.02.01_Changing_spec_value_in_primary_timing_spec_set.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05_Wavetables.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05.01_Function_of_the_base_wavetable.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.01_The_Spec_Tool_window.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.10_Changing_the_Check_Options.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.14_Changing_Spec_Values.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.16.01_Global_and_local_spec_values__scope_of_the_spec_variable.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33.01_Using_the_Timing_Diagram_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34_Timing_Setup_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.03_Waveform_and_timing_sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.03.02_Implications_when_running_tests.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04_Equation_based_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.01_Single-port_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.02_Multiport_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.02.01_Verifying_a_multiport_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03_Structure_of_an_equation_based_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.02.02_Edge_action.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.03.04_Default_device_cycle.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.04.11_Period_resolution__period_res.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.04.12_Period_divisor__period_div.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.04.13_Timing_sets__TIMINGSET.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.05_Timing_Specifications_-_Reference.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.06_Error_Reporting.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.07_Glossary_of_terms_-_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.04_Example_of_the_equation_based_timing_setup_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.04.01_Timing_Wavetables_-_Example.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05_Timing_setup_master_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05.01_Master_file_format_for_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05.02_Editing_the_level_and_timing_subfiles.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.05_Mode_context_in_timing_setup.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06_Using_the_Timing_Setup_Tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.05_Setting_the_period.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.06.01_Watching_System_Resources.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.06.06_Downloading_Your_Timing_Setup_into_the_Firmware.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.07_Editing_Device_Cycles_and_Waveforms.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.11_Working_with_Multiple_Waveform_and_Timing_Sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.11.01_Creating_Waveform_and_Timing_Sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.11.02_Keeping_Waveform_Sets_Compatible.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.12_Performing_Timing_Checks.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.12.01_Checking_for_Compatible_Waveform_Sets.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.07_The_Timing_Setup_Window.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.07.01_The_Global_Information_Area.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.18_TestsuiteProxy.getTimingEquation.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.19_TestsuiteProxy.getTimingSet.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.20_TestsuiteProxy.getTimingSpec.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.22_TestsuiteProxy.isMultiportTiming.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.26_TestsuiteProxy.setEquationBasedTiming.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.27_TestsuiteProxy.setMultiportTiming.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Timing 配置的三层对照

## 这张表在说什么

Pin 那一页的结论是「GUI / 文件 / 命令**三套说法**其实是同一件事的三种写法」。
**Timing 这一页的语料把同一件事说得比 pin 更直白**——它不是「corresponding exactly to」
这种一句声明，而是**把三种写法摆在同一份文档里，互相指着对方**：

- 讲 **wavetable 部件**的那个词条，直接说它由哪个 GUI 工具创建、在哪条固件命令之后出现在文件里；
- **`EQFS` 命令自己的 `## Application` 段**写明了它的调用者是谁；
- 语料里**有一份完整的 timing setup file 例子**，里面逐行就是固件命令。

先看第三条。`02.08.04.34.04.04_Example_of_the_equation_based_timing_setup_file` 给的
例子文件以 `hp93000,timing,0.1` 开头，接着是一段固件命令。**它的开头这几行逐字如下**：

```
PCLK 1,1,1000,(@)
CLKR 1,1000,10
BWDS 1,,,"",(CP,DS7,DS0,S1,S0,_MR,I/O7,I/O6,I/O5,I/O4,I/O3,I/O2,I/O1,I/O0)
ETDS 1,1,,"",(CP,DS7,DS0,S1,S0,_MR,Q7,Q0,I/O7,I/O6,I/O5,I/O4,I/O3,I/O2,I/O1,I/O0)
DCDT 1,""
TSUX 1,1
EQSP TIM,WVT,#9000001922
```

**中间是本页略去的两大段**（wavetable 正文、equation set 正文；**本页没有把它们抄进来，
也没有用省略号接过去**）。略去部分结束后，跟着的是另外两条 `EQSP`，`02.08.04.34.04.04`
里各占一行，逐字如下：

```
EQSP TIM,EQN,#9000001444EQNSET 1 "gross_func_eqn"
```

```
EQSP TIM,SPS,#9000001339
```

**文件的最后一行**（同篇 `## Example` 代码块的收尾）逐字如下：

```
NOOP "6.5.3",,,
```

**这就是本页的地基**：timing setup file **不是**「某种中间格式」，**它本身就是一份固件命令脚本**，
三块数据（wavetable / equation set / spec set）以 `EQSP` 的字符串参数形式嵌在里面。
`02.08.04.34.04.05.02_Editing_the_level_and_timing_subfiles` 把这件事说成一句：

> 「Equation based level and timing setups are stored in the setup file as a string parameter of the EQSP firmware command, which serves to download the setup data to the tester.」

再看第二条——**`EQFS` 的 `## Application` 段回答「谁在用这条命令」**：

> 「- Editor tools」

> 「- The Spec tool」

（原文是两行连续的列表项，本页按「相邻 `>` 行必须隔空行」的规矩拆成两块；
`02.06.06.02.13` 里它们是紧挨着的两行。）

同篇还有一句把用途讲全：

> 「The EQFS command provides the load/save operations required by the editor tools for loading/saving the equation based testing files from/to temporary files.」

把两句话合起来：**GUI 的编辑器工具是 `EQFS` 的调用者**。这就是 pin 那页
`corresponding exactly to` 在 timing 这一段的等价物——**而且它是逐条可查的**。

第三条在 `02.08.04.34.04.03.07_Glossary_of_terms_-_timing_setup` 里，三个词条各自给出
「GUI ↔ 文件 ↔ 命令」三件事。**这三个词条是本页主表最硬的一档证据**：

> 「A timing setup component where timing equation sets are defined. Found after an `EQSP TIM, EQN` command in a the Timing Setup File. Created and modified using a text editor opened from the Timing Setup window.」

> 「A timing setup component where wavetables are defined. Found after an `EQSP TIM,SPS` command in a Timing Setup File. Created and modified using a text editor or the spec tool opened from the Timing Setup window.」

> 「A timing setup component where wavetables are defined. Found after an `EQSP TIM,WVT` command in a Timing Setup File. Created and modified using a text editor opened from the Timing Setup window.」

（第二、三条**都说自己装的是 wavetable**，这与 `EQSP` 的参数表冲突——见「对不上的地方」①。
`in a the Timing Setup File` 是语料自带的衍字，见②。**本页一处都没替它改**。）

**「三层」这个词在本页同样要放宽理解，但方向与 pin 那页相反。**
pin 那页 L2 几乎全空、L3 整列 `—`；**timing 这一页五列都有实料**：
L2 有 `TIMING_SPEC` / `TimingSetSelector`，L3 有 `TestsuiteProxy` 的六个 timing 成员
和 TPI `DataManager` 的 `dm_timing`。**但五列有料不等于每行都有料**——
下面「对不上的地方」逐条说明哪一列在哪一行是 `—`（不存在）、哪一行是 `?`（语料没说）。

## 对照表

**读法**：一格填了名字 = 有证据（证据是什么见下一节）；`?` = 语料没说，**本页不猜**；
`—` = 这一层不存在这个对应物（不是「没找到」）。**凡不是文档明说、而是本页按职责排的格，
在下节逐条标了（推断）。**
**带「（图证）」的格 = 这一格的 GUI 侧字面（或文件侧那一行）在 raw 的图上直接看得见**——
是哪张图、图里的字为什么搜不到，见证据节 **④** 与「对不上的地方」**⑪**。

| 目的 | GUI | 文件 | L1 命令 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 生成/编辑 wavetable 的物理波形表（PhyIndex / Action / DevCyc） | [[timing-setup-tool]] 的 wavetable editor（`Select > edit wavetables`） | [[wavetable-file]]（[[timing-file]] 里 `EQSP TIM,WVT` 之后的那一段） | [[wfds]] / `WFDF` + [[wave]] | ? | — |
| 给物理波形起 device cycle 名 / 设默认器件周期 | `Def. DevCyc:` 字段（Global Information Area） | [[wavetable-file]] 的 `DevCyc` 列、`DCDT <name>` | [[dcdt]] | ? | — |
| 定义 break waveform | ? | [[wavetable-file]] 的 `brk` 行 | [[bwds]] / [[bwdf]] | ? | — |
| 声明 equation set / wavetable 属于哪个 mode context | [[timing-setup-tool]] 的 `Context` 字段（图证） | `MODECONTEXT "<name>"`（equation set 与 wavetable 各一行）（图证） | [[conf]] | ? | — |
| 声明 spec 变量（`SPECS`，含单位） | [[spec-tool]]（只读显示变量名与单位） | [[timing-equation-set]] 的 `SPECS` 段（图证） | — | ? | — |
| 写派生量（`EQUATIONS`） | ? | [[timing-equation-set]] 的 `EQUATIONS` 段 | — | ? | — |
| 写 timing set 的 `period` 与边沿表达式（`d1`–`d8` / `r1`–`r8`） | [[timing-setup-tool]] 的 `Timing` / `Tset#` 字段 | [[timing-equation-set]] 的 `TIMINGSET` 段（图证） | — | ? | — |
| 设 period 分辨率与周期分频 | `Select > period` 的 period entry field | `period_res` / `period_div` / `period` 关键字（`period_div` 图证） | [[pclk]] / [[clkr]] / [[pdiv]] | ? | — |
| 把 wavetable + equation set + 一组 spec 值**绑成一条** specification | [[spec-tool]] 顶端的 Specification / Equation Sets / wavetable 三行（图证） | [[timing-file]] 的 `EQNSET n` / `WAVETBL "name"` / `CHECK` / `SPECSET n`（图证） | — | [[timing-spec]] 的构造参数 `TIMING_SPEC(eqnset, specset)` | — |
| 给 spec 值赋 actual / min / max | [[spec-tool]] 底部表（双击编辑，列名 `Actual` / `Minimum` / `Maximum`，图证）、`Edit > Change Spec Values` | [[timing-file]] 的 `*****ACTUAL*****` / `*****MINIMUM****` / `*****MAXIMUM****` 列 | — | [[timing-spec]] 的 `change()` / `restore()` / `getSpecValue()` | — |
| 运行时改 spec 值（**不落盘**） | ? | — | [[svlr]] | [[timing-spec]] 的 `change()` + `FLUSH` | — |
| 一致性检查：边沿间距与边沿顺序 | [[spec-tool]] 中区的 edge order 检查项（`Change > Change Check Status`）（图证：三组 `Edge order checks` / `Drive period checks` / `Receive period checks`） | [[timing-file]] 的 `CHECK all` / `1period` / `2period` / `10period` / `edgeorder` | [[spst]] / [[vtim]] / [[vwfs]] / [[vwfg]] / [[vclk]] / [[vdcg]] | ? | ? |
| 定义 waveform set 的个数 | `WFset #` entry field | ? | [[wsus]] | ? | — |
| 定义某个 waveform set 里 timing set 的个数 | `Tset #` entry field | ? | [[tsus]] / [[tsux]] | ? | — |
| 把三块数据下载 / 上传（EQN / SPS / WVT） | wavetable editor 的 `Shell > Download`、[[spec-tool]] 的 Download 按钮 | [[timing-file]] 里的三条 `EQSP` 指令（`TIM,EQN` / `TIM,SPS` / `TIM,WVT`） | [[eqfs]] / [[eqsp]] | ? | [[tpi-program-routines]]（`DataManager` 的 `dm_timing` + `dm_load` / `dm_save` / `dm_merge` / `dm_copy_in` / `dm_delete`） |
| 把一个 timing setup 拆成 / 合成多个文件 | [[setup-management-tool]] | [[timing-master-file]] | ? | ? | ? |
| 选定 primary set（哪个 testsuite 用哪套 timing） | ?（文档说在 testsuite editor 里指定，属 [[testflow]] 段的工具） | ? | [[sprm]] / [[aprm]] | [[primary-status]] 的 `timing()`、[[timing-set-selector]] | `TestsuiteProxy.setEquationBasedTiming()` / `.getTimingEquation()` / `.getTimingSpec()` / `.getTimingSet()` / `.isMultiportTiming()` / `.setMultiportTiming()` |
| 查 timing 与硬件是否一致（up-to-date） | [[test-program-explorer]] 的 up-to-date 指示 | ? | [[uptd]]（`UPTD? TIM`） | ? | [[tpi-program-routines]] 的 `DataManager`（`dm_utd` + `dm_timing`） |
| 抖动注入（本阶段的子专题） | ? | ? | [[jscf]] / [[jsud]] / [[jrst]] / [[jsdf]] / [[jspr]] / [[jswf]] / [[mscf]] / [[msdf]] | ? | ? |
| 结果侧目视核对实际波形 | [[timing-diagram-tool]]（`93000 > Results > Timing Diagram`） | timing diagram 文件（`dm_tdiag`） | ? | ? | [[tpi-program-routines]] 的 `dm_tdiag` |

**表里没有的**：`NOOP`（出现在上面那份例子文件的最后一行，`NOOP "6.5.3",,,`）。
它**不在 timing setup 命令的清单里**（`02.06.06.02_List_of_timing_setup_commands` 46 条，
无 `NOOP`），**本页不替它安一个位置**。`WFDF` **不在
`extract/prose-allowlist.txt` 里**，所以主表 L1 格里的它写成反引号、不写双方括号
（出处：`02.06.06.02.41_WFDF__WFDF__-__WaveForm_DeFinition.md`，
链接名出现在 `02.08.04.34.01.01.01` 与 `02.08.04.34.04.03.02.02` 两篇里）。

## 证据：哪几格是钉死的，哪几格只是「那边链过来了」

**证据分四档，本页不把它们混成一种。**

**① 语料明说三件事同指一个东西（最硬）** —— 就是开头那三段：`EQFS` 的调用者、
glossary 三条词条各自给出的两处措辞——「由哪条 `EQSP` 命令之后出现在文件里」与
「由哪个 GUI 工具创建修改」（**本页这里只是指路，三段全文见开头三块引文**）——
以及那份逐行是固件命令的例子文件。
**受益的行**：主表里 wavetable 那一行、三个数据块的行、以及「下载 / 上传」那一行——
**它们的 GUI / 文件 / L1 三列由这三段直接背书**。
同一档还有两条逐元素的句子：

> 「Edge actions get defined by the WFDF command, and are ultimately programmed into the hardware using the WAVE command.」

（`02.08.04.34.04.03.02.02_Edge_action`，文件格式参考篇自己点名 L1 命令。）

> 「Every test is associated with a mode context, and every execution of the CONF command applies to exactly one mode context.」

（`02.08.04.34.05_Mode_context_in_timing_setup`，GUI 侧的篇里点 `CONF`。）

**② 文档之间有链接（次硬，逐条可查）** —— 取自 `extract/edges.jsonl`。
**这一档必须先做一步去重**，否则整档都会是假的：**`02.08.04.34.02.*` 整棵子树是
`02.06.06.01.*` / `02.06.06.02.*` 的重复投放**（同一 TDC 页换了个章号再投一次，
判据是 frontmatter 的 `source_topic` 去掉 `_2` 之后相同——实测 504 个页 / 1,111 篇，
与 `schema.md` §10 的数一致）。**那棵子树里的「GUI 文档 → 命令页」链接是同一篇文档指向自己，
不是跨层证据**，本页全部剔除。剔完还剩 **53 条**真正的跨层出链：

| 源文档（GUI / 文件侧） | 链到 | 条数 |
|---|---|---|
| `02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool.md` | `APRM` | 1 |
| `02.08.04.30.02.16.01_…scope_of_the_spec_variable.md` | `SVLR` | 2 |
| `02.08.04.30.02.17_How_to_perform_a_measurement.md` | `SpecSearch`（L2） | 1 |
| `02.08.04.34.01.01.01_Drive_Edges_and_Actions.md` | `WFDF`、`WFDS` | 2 |
| `02.08.04.34.04.03.02.02_Edge_action.md` | `WFDF`、`WAVE` | 2 |
| `02.08.04.34.04.03.03.04_Default_device_cycle.md` | `DCDT` | 1 |
| `02.08.04.34.04.03.04.12_Period_divisor__period_div.md` | `PDIV?`、`Timing equation set reference` | 2 |
| `02.08.04.34.04.03.06_Error_Reporting.md` | `Command Reference` | 1 |
| `02.08.04.34.04.05.01_Master_file_format_for_timing_setup.md` | `Data organization of equation based timing` | 1 |
| `02.08.04.34.04.05.02_Editing_the_level_and_timing_subfiles.md` | `EQSP`、`DFTD` | 4 |
| `02.08.04.34.05_Mode_context_in_timing_setup.md` | `Mode contexts`、`Mode context in level setup`、`Timing equation set reference` | 3 |
| `02.08.04.34.04.02.01_Verifying_a_multiport_timing_setup.md` | `Incomplete multiport setups` | 1 |
| `02.08.04.34.06.05.01_Minimum_period___maximum_frequency_of_the_sequencer.md` | `Period resolution, clock resolution, and master clock period` | 1 |
| `02.08.04.34.04.02_Multiport_timing_setup.md` | `Dealing with rounding problems in multiport setups` | 1 |
| 其余 `02.08.04.34.04.03.*`（文件格式参考）指向 `02.06.06.01.*` 的 | 各篇 `Defining waveform shapes` / `Setting the edge delays` / `Defining the timing specification` 之类的章节名 | 约 28 |

**反方向的链接（L2 → GUI）也有，而且只有 L2 有**：
`02.07.04.01.249_TIMING_SPEC` 一章链到了
`02.08.04.34.04.03.05_Timing_Specifications_-_Reference`、
`02.08.04.34.04.04.03_Timing_Specifications_-_Example`、
`02.08.04.34.04.03.04.07_Timing_spec_set` 三篇。**L3 一篇都没链过来，GUI 也没有一篇链到 L3**
——实测：GUI 侧 timing 文档的出链里，落 `02.06` 的 **52** 条、落 `02.07` 的 **1** 条、
落 `02.09` 的 **0** 条。**这个分布本身就是一条信息，见「对不上的地方」③。**

**链接证的强度要说清**：一条链接**只证明「那篇文档认为读者该去看这一篇」**，
**不证明两个东西等价**——可能是「见也」、可能是「区别在这里」、也可能是「前提」。
本页只在主表的**同一行**里用它，**不跨行搬**。

**③ 只有一侧、另一侧是本页排的（标（推断））** —— 下面这几行的对应**不是文档明说的**，
是**本页按职责排的**，依据逐条写在后面：

| 行 | 哪一格是（推断） | 依据 |
|---|---|---|
| `WFset #` ↔ `WSUS` | GUI 格 | `WSUS` 说它是「sets the number of defined waveform sets to the given value」；`02.08.04.34.03.02` 说「Enter the number into the WFset entry field in the Timing Setup window.」（该句的上一句是 `you have to define the number of waveform sets that you actually want to use`，**本页把它截在这里，省略号没有出现在引文里**）。**语义相同，但语料里没有任何一条链接把两者钉在一起** |
| `Tset #` ↔ `TSUS` | GUI 格 | 同上：`TSUS` 是「defines the number of timing sets contained in a given waveform set」，GUI 侧是 `Tset #` entry field。**同样是语义相同、没有链接** |
| `Def. DevCyc:` ↔ `DCDT` | 文件格 | `DCDT` 是「Device Cycle DefaulT」，GUI 字段名是 `Def. DevCyc:`。`02.08.04.34.04.03.03.04_Default_device_cycle` **确实链到了 `DCDT`**（那一条进②档），**但「GUI 的那个字段 = 文件里那一行」是本页推的** |
| `Context` 字段 ↔ `MODECONTEXT` | GUI 格 | `02.08.04.34.05` 说「The mode context defined in the timing equation set is displayed in the Context field of the Timing Setup editor」——**这一条其实是文档明说的**，列在这里是提醒它与 `MODECONTEXT` 关键字同指一件事 |
| `period_res` / `period_div` / `period` ↔ `PCLK` / `CLKR` / `PDIV` | L1 格 | 文件侧的三个关键字有文档（`02.08.04.34.04.03.04.11` / `.12` / `.13`），L1 侧的三条命令有文档，**但「哪个关键字由哪条命令承接」语料没写**。`PDIV` 与 `period_div` 有链接（②档），`PCLK`/`CLKR` 没有 |
| `CHECK` ↔ `SPST` / `VTIM?` / `VWFS?` / `VWFG?` / `VCLK?` / `VDCG?` | L1 格 | `02.08.04.34.04.03.06_Error_Reporting` 把 `CKST?` / `SPST` / `SPST?` 与「level or timing resource violations」并列，其中 timing 资源逐项列为 `period_res` / `period` / `d1-d8` / `r1-r8`——**与 `CHECK` 检查同一批量**；成组校验查询命令的职责来自 [[timing]] 与各命令页。**这一行的 L1 整格是本页按职责排的** |
| 「选定 primary set」整行 | L1 / L2 / L3 三格的**对齐** | `SPRM` 与 `Primary.timing()` 都围绕「primary sets」这个概念（`SPRM` 说「define and change the primary sets in a test suite」，`TIMING_SPEC` 例 1 说「The second timing() member function defines the timing set "1" as the primary」），`TestsuiteProxy.setEquationBasedTiming` 说「sets the equation based timing for **the test suite**」。**三者同指「某个 testsuite 用哪套 timing」，但没有一条文档把它们互相链起来** |
| `DataManager(dm_utd, dm_timing)` | L3 格 | `dm_timing` 的说明是「timing setup」，`dm_utd` 的说明是「return up to date status for the file specified by Fid」；L1 侧 `UPTD?` 说它「read if the data in hardware has been changed since the current device file was last saved or loaded」。**同义，但没有文档说 `dm_utd` 就是 `UPTD?` 的门面** |
| wavetable editor 的 `Shell > Download` ↔ `EQSP` / `EQFS` | GUI 格 | ①档已经钉死「编辑器工具是 `EQFS` 的调用者」；**具体到「哪个按钮调哪条命令」是本页推的** |

**附：只有命令侧、没有 GUI 侧的证据** —— 主表里 **L1 列填了命令、而 GUI 列是 `?`** 的那几行
（**定义 break waveform**、**运行时改 spec 值**、**选定 primary set**、**抖动注入**）。
它们的命令事实来自各命令页与 [[timing]]，**但语料里没有一篇 GUI 文档链到它们**
（抖动注入那一族连 GUI 文档都没有），所以 **GUI 那一格是 `?`，不是 `—`**。
**反过来，GUI 列有值而 L1 列是 `—` 的那四行**（`SPECS`、`EQUATIONS`、`TIMINGSET` 表达式、
以及「绑成一条 specification」）**不是缺口，是
`The collections themselves cannot be edited with firmware commands.` 这句的直接后果**
——见「对不上的地方」④。

**另：这两组格子的分布本身就是结论。** L1 能碰的是**「集合的数目」（`WSUS`/`TSUS`）、
「整块的搬运」（`EQFS`/`EQSP`）、「激活与切换」（`SPRM`/`APRM`/`CTIM`）、
「运行期改值」（`SVLR`）**；L1 **碰不到的是三块数据的**正文**（②档那条
`cannot be edited with firmware commands`）。**主表里 `—` 的 19 格，
绝大多数就落在这条分界线上。**

**④ 图证（2026-09-20 加，本页用到了）** —— 从 raw 自带的图里读出来的。
（`schema.md` §2.5：**④ = 图证**。）

**本页 sources 里带图的文档共 24 篇 / 38 张。本页读了六张**，挑的是与主表待答格子
有关的那几张；**其余三十二张没看**（多数是图标、工具栏、对话框小图，如
`02.08.04.34.06` 的三张与 `02.08.04.34.07` 的两张）。
**结论先给**：**六张没有填掉主表里任何一个 `?`**（本页的 `?` 大半在 L2 列，
另有「`WSset #` / `Tset #` 的文件格」两个——图里既没有 API 名，也没有那两行文件），
**但其中三张把主表里几格的「GUI 侧字面」从「本页按职责排」提到了「字面可见」**，
**其中一张（`56203.png`）还是本页唯一一张画出文件内容的图**。逐张：

**（a）`56203.png`（`02.08.04.34.05`，alt `Context Defined in Timing Equation Set and Wavetable`）
—— 本页最有用的一张。** 它**不是截图，是两栏对照**：左栏标题 `Timing Equation File`，
右栏标题 `Wavetable`。图上逐字可读的**文件内容**是：

- 左栏：`EQNSET 1 "DIFF_fastI_fasto_x8"`，紧跟一行 `MODECONTEXT "DIFFERENTIAL"`；
  然后 `SPECS` 段（`TBit [ps]`、`Offset_10902 [ns]`、`Offset_10906 [ns]`、`Offset_10910 [ns]`、
  `Offset_10914 [ns]`、`JitterAmplitude [ps]`、`t_drv [ps]`、`t_rcv [ps]`、
  `t_dummy [ps]`）；再 `EQUATIONS`；再 `TIMINGSET 1 "eq DIFF_fastI_fasto_x8 ts 1"` +
  `period=0.001*8*TBit`；再 `PINS DrvAll_FIFo` + `period_div = 8` + `d1=0.001*t_drv`。
- 右栏：三行 `4a "r1:x r2:x r3:x r4:L" XXXX` / `4b ... H` / `4c ... X`；
  `WAVETBL "fastI_fasto"`，紧跟一行 `MODECONTEXT "DIFFERENTIAL"`；
  然后 `PINS DrvAll_FiFo` + 编号行 `0 "00000000" 00000000` … `d "00001101" 00001101`。
- 两个标注框：`Single ended pins using normal notation` 指左栏那三行 4a/4b/4c，
  `Context definition` 指向两栏里那**两行 `MODECONTEXT`**。

**它解决掉的格子（都由这一张背书）：**

- **「声明 equation set / wavetable 属于哪个 mode context」的 `文件` 格**
  （原写 `MODECONTEXT "<name>"`（equation set 与 wavetable 各一行））
  ——**图上正好各一行**，且 **equation set 那一行紧跟 `EQNSET 1 "DIFF_fastI_fasto_x8"` 之后**，
  与 `02.08.04.34.05` 正文那句 `This line must follow the line with the EQNSET keyword` 一致。
- **「声明 spec 变量（`SPECS`，含单位）」的 `文件` 格**（[[timing-equation-set]] 的 `SPECS` 段）
  ——图上 `SPECS` 段每个变量后面确实挂一个 `[…]` 单位。
- **「写 timing set 的 `period` 与边沿表达式」的 `文件` 格**（`TIMINGSET` 段）
  ——图上有 `TIMINGSET 1 "eq DIFF_fastI_fasto_x8 ts 1"` 与 `period=0.001*8*TBit` 两行。
- **「设 period 分辨率与周期分频」的 `文件` 格里的 `period_div`** ——图上 `PINS` 块里逐字有
  `period_div = 8`。

**图里的字在 raw 里 grep 不到**（本页逐条查过 9,398 篇 raw md，全 0 命中）：
`DIFF_fastI_fasto_x8`、`fastI_fasto`、`DrvAll_FIFo`、`DrvAll_FiFo`、`Offset_10902`、
`Single ended pins using normal notation`、`Context definition`。

**它答不了的**：图上**没有 `period_res`、没有 `CHECK`、没有 `EQSP` / `EQFS`、没有 `SPECSET` 正文**
——所以这几格的 `文件` 侧**图没帮上**；图里也**没有任何一条 L1 命令名**。

**（b）`56199.png`（`02.08.04.34.05`，alt `Context of a Primary Timing Setup`）—— 结构图。**
左半：`TIMING EQN SET 1` 里有 `MODECONTEXT *`、`SPECS`（`<spec 1>` … `<spec k>`）、
`EQUATIONS`、`TIMINGSET 1` … `TIMINGSET k`；其下 `WAVETABLE 1` 里有 `MODECONTEXT *`、`WAVEFORMS`；
左下角一行小字 `* Must be the same contexts`。右半是一个红框的 `Primary Timing Setup`：
里面有 `Pointer to TIMING SET`，以及一个 `Timing Specification` 框，框内是
`Pointer to TIMING EQN SET`、`Pointer to WAVETABLE`、`TIMING SPEC SET 2`（附
`<spec 1> = 4ns`、`<spec 2> = 7.5ns`、`<spec k> = 12ns`）。右上红色标注框逐字：
`Requirement for a valid Timing Specification:` / `Mode Context EQN SET = Mode Context WAVETABLE`。
**它解决掉的格子**：「把 wavetable + equation set + 一组 spec 值绑成一条 specification」
那一行的**结构**——**绑定是三枚指针加一个 spec set**；这**印证**了该行 `文件` 格里的
`EQNSET n` / `WAVETBL "name"` / `SPECSET n` 三样、以及 L2 格 `TIMING_SPEC(eqnset, specset)`
的两个参数。**但它用的是自己的词（`Pointer to TIMING EQN SET` 那一族），
不是文件里的关键字**，所以是**印证**不是新证据。
**grep 不到**：`Pointer to TIMING SET`、`Pointer to TIMING EQN SET`、`Pointer to WAVETABLE`、
`TIMING SPEC SET`、`Requirement for a valid Timing Specification`、`Must be the same contexts`（均 0 命中）。
**它答不了的**：图里没有 `EQNSET` / `WAVETBL` / `SPECSET` 这三个关键字，**所以「哪一行」还是不知道**。

**（c）`17845.png`（`02.08.04.34.04`，alt `Timing Setup Components`）—— 结构图。**
上半 `Timing Setup File`：`Wavetable`（多份）、`Specset`（多份）、`Equation Set`（多份）；
`Specset` 里是 `Pointer to a Wavetable`、`Pointer to an Equation set`、
`Spec assignments assigning initial, min & max values`；`Equation Set` 里是 `Spec declarations`、
`Equation definitions`、`Logical resource assignments`。下半 `Hardware`：`Wavetable`、
`Period Resolution`、`Pointer to a wavetable`、`Timing set`。
**它对本页最大的用处是「对不上的地方」①**：glossary 把 `EQSP TIM,SPS` 那一段说成
`where wavetables are defined`，而这张图显示 **`Specset` 里确实有一枚指向 wavetable 的指针**
——**那句 gloss 的来处就在这里**。**但「含一枚指针」与「定义 wavetable」不是一回事**，
**本页照旧两个说法并列（①已记），不替任何一方翻案。**
**grep 不到**：`Pointer to a Wavetable`、`Pointer to an Equation set`、`Spec assignments`、
`Logical resource assignments`、`Spec declarations`（均 0 命中；同页的 `Equation definitions`
有 2 命中，在别篇）。**它答不了的**：图里没有 `Wavetable` 框的列、没有 `Specset` 的正文，
**也没有 `EQSP TIM,WVT` / `TIM,SPS` 这两个参数**——**glossary 与 `EQSP` 参数表那处矛盾，
图不判**。

**（d）`22015.png`（`02.08.04.30.01`，alt 位置正文是 `The figure below shows a typical Spec Tool main
screen, with the main areas pointed out.`）—— 窗口截图，信息量仅次于（a）。**
窗口标题 `SpecTool`，菜单 `File Select Change Edit Sort Display Doc`，状态行 `Timing (modified,
download required)`。图上有四组标注指向四个区域：`Equation Set Number`、`Short-cut Icons`、
`Spec Set Number and Description`、`Run Test Pushbutton`；另三个在下方：
`Spec Name Area`、`Associated Wavetable / Equation Set Description`、`Check Setup Area`。
**逐字可见的控件是**：`Specification [1] [gross_func_specs_multi]`、
`[ ] automated swing adjustment`、`Edge order checks`（`drive` / `tristate` / `window`）、
`Drive period checks`（`none` / `one` / `two` / `ten`）、
`Receive period checks`（`none` / `one` / `two` / `ten`）、
`Wavetable [gross_func_wtb.multi]`、`Equation [1] [gross_func_eqn]`，以及底部一张表，
列名逐字 `Name | Actual | Minimum | Maximum | Measured | Unit | Comment`（例行 `tpd1Dx`，`Actual=0`）。
**它解决掉的格子（三处）：**

- **「把 wavetable + equation set + 一组 spec 值绑成一条 specification」的 GUI 格**
  ——原写「[[spec-tool]] 顶端的 Specification / Equation Sets / wavetable 三行」，
  **图上就是三行**：`Specification`、`Wavetable`、`Equation`，且有一个标注
  `Associated Wavetable / Equation Set Description` 正指向后两行。**GUI 格由这张图钉死。**
- **「给 spec 值赋 actual / min / max」那两格的对齐** ——GUI 侧原写「[[spec-tool]] 底部表（双击编辑）」，
  **图的底部表列名是 `Actual` / `Minimum` / `Maximum`**；该行 `文件` 格写的是
  `*****ACTUAL*****` / `*****MINIMUM****` / `*****MAXIMUM****`。
  **图把 GUI 侧三个列名钉到字面，与文件里那三行同名。**
  **但要说清这是哪一档**：**图里没有文件内容**，所以这是**「同名」**，
  **不是一条文档声明**——本页把它记成**图证级的字面对齐**，**不把它升成「文档明说」**。
- **「一致性检查：边沿间距与边沿顺序」的 GUI 格** ——原写「[[spec-tool]] 中区的 edge order 检查项
  （`Change > Change Check Status`）」，**图的中区就是三组检查项**（见上），整块被标注成
  `Check Setup Area`；该行 `文件` 格写的是 `CHECK all` / `1period` / `2period` / `10period` /
  `edgeorder`。**`one` / `two` / `ten` 与 `1period` / `2period` / `10period` 是同一条梯子**
  ——这是本页**图给出的最接近「一栏对一行」的一处**，**但仍然只是词面**（图里没有 `CHECK` 这一行）。

**grep 不到**：`Spec Name Area`、`Check Setup Area`、`Run Test Pushbutton`、`gross_func_specs_multi`、
`gross_func_wtb.multi`、`Associated Wavetable`、`Receive period checks`（均 0 命中；
`Edge order checks` / `Drive period checks` 各 1 命中，**都在 `02.12`（Memory Test Plus）里**，
**不在本页 sources**）。
**它答不了的**：`Edit > Change Spec Values` 这条菜单路径**图里没有**——图只有七个菜单名，
**没有展开任何菜单**；所以那一格照旧只有 `02.08.04.30.02.14` 的文字依据。

**（e）`56204.png`（`02.08.04.34.05`，alt `Context in the Timing Setup editor`）—— 窗口截图。**
标题栏 `Timing Setup`，文件页签 `test`。上部逐字有 `Eqn#` `SpS#` `Tset#` `Port:@` `Df. DC:`
`cyc:`，以及四个具名字段 `Specification` = `1.25Gbit - different`、`Equation` =
`timing_equation_set_`、`Wave Table` = `differential`、`Timing` = `timing_set_1_differe`；
`Context` = `differential` **被圈出并配了 `Context "differential"` 的标注框**。
下部是一张 `pin/group | DevCyc | i/o | cycle> 0 | 1` 的表（行 `xlink_a_n` / `xlink_a_p`，
`DevCyc` 值 `LLLHL`）。
**它解决掉的格子**：「声明 equation set / wavetable 属于哪个 mode context」的 **GUI 格**
（[[timing-setup-tool]] 的 `Context` 字段）——**图证明了 `Context` 字段确实在 Timing Setup 窗口里**，
而且**同一屏**就能看到 `Equation` 与 `Wave Table` 两个字段。**但 ③ 档已经写过「这一条其实是
文档明说的」，所以图是印证，不是新证据。**
**grep 不到**：`Df. DC`、`1.25Gbit`（0 命中）。
**它答不了**：**图里没有 `MODECONTEXT` 这一行**——「GUI 的 `Context` 字段 = 文件里的
`MODECONTEXT`」这个粒度，**图仍然答不了**（文件内容不在图上）；（a）答的是另一头。
**一处要照实记的**：这张图的上部字段是 `Eqn#` / `SpS#` / `Tset#` / `Port:` / `Df. DC:` / `cyc:`，
而（f）那张是 `WFset #` / `Tset #` / `Def. DevCyc:` / `cycles:`——**同一块区域，两张图给了两套字段名**。
两张图出自两篇不同文档（`.34.05` 与 `.34.07.01`），**语料的文字部分只说了后一套**
（`02.08.04.34.07.01` 逐字列了四个 `entry field`）。**本页照实并列，不判哪一套是现行版。**

**（f）`21812.png`（`02.08.04.34.07.01`）—— 这张不算图证，本页说清为什么。**
它是 Global Information Area 的单行截图，逐字 `WFset #` `1` `of 1`、`Tset #` `1` `of 1`、
`Def. DevCyc:`（空框）、`cycles:` `4`。**这张图上的字全部可以在 raw 里 grep 到**——
该篇正文**逐字**把四个 `entry field` 列出来了（`WFset #` / `Tset #` / `Def. DevCyc:` / `cycles:`）。
按 §11.4 的判据，**图证的门槛是「图里的字搜不到」**，所以这一张**不构成图证**，
它只说明这四个字段排在**同一行**里。**本页把它列出来，是为了说清它不算**，不是凑数。

**图证整体答不了的三件事，照实说：**

- **主表 L2 列的那些 `?`，一张图都没解决**——六张图里**没有任何一个 API 名**。
- **主表 L1 列的那些 `—` 与 `?`，一张图都没动**——六张图里**没有任何一条固件命令名**
  （`56203.png` 画的是**文件内容**，那里面也没有 `EQSP`）。
- **图是「某一次具体 setup」的截图，不是格式规范。** 「哪些关键字必填、哪些组合非法」
  **图答不了**——那是文本的事，而文本在这一点上也只写了一半。

## 对不上的地方

**① glossary 有两个词条自相矛盾。** `02.08.04.34.04.03.07` 里
「Timing Specifications」与「Timing Wavetables」**都写自己装的是 wavetable**：

> 「A timing setup component where wavetables are defined. Found after an `EQSP TIM,SPS` command in a Timing Setup File. Created and modified using a text editor or the spec tool opened from the Timing Setup window.」

> 「A timing setup component where wavetables are defined. Found after an `EQSP TIM,WVT` command in a Timing Setup File. Created and modified using a text editor opened from the Timing Setup window.」

**而 `EQSP` 自己的参数表把三块分得很清楚**（`02.06.02.02.109`）：

> 「- SPS to specify specs」

**所以按 `EQSP` 的参数表，`TIM,SPS` 那一段装的是 spec set，不是 wavetable。**
本页照实记下这个矛盾，**没替语料改字**，也没有据此去删任何一格。

同一篇里还有一处**读起来像从 level 章抄过来的**：

> 「Allocates timing sets and period resolution in hardware by applying spec values to the logical assignments set up in the level equation sets. Also allocates wavetables in hardware from the information supplied in the Timing Wavetables component.」

**这一条讲的是 timing 的 specset，中间却写着 `level equation sets`。**
它是不是笔误，**本页判不了**——只能记下，并标明这是**本页的怀疑、不是文档事实**。

**② glossary 有三处语料瑕疵，本页一处都没替它改。**
`in a the Timing Setup File`（衍字 `a`）；
`隆陋` 一处（`... referenced by a timing specset 隆陋 which is where ...`）——
这是 §11.2 ① 那类编码损坏，原字符应是破折号；
「Timing Equations」词条里 `a the Timing Setup File` 与「Timing Specifications」词条的
`a Timing Setup File` **用了两种写法**。**引文里一律照原样。**

**③ L3 只在两行有值，而且那两行都「只按名引用」，不定义内容——这是结论不是缺口。**
§6 把 L3 定义成「调用者是**外部进程**」（TPI / HVM / test suite control）。
本阶段 L3 的 timing 族是 `TestsuiteProxy` 的 `.18` / `.19` / `.20` / `.22` / `.26` / `.27`，
**六个成员的名字/签名显示它们收发的都是名字或编号**：
`.26` 的签名是三个 `const std::string&`（`timingEquation` / `timingSpec` / `timingSet`），
`.18` / `.19` / `.20` 的返回类型是 `const std::string`，`.22` 返回 `bool`。
**据此本页把「定义内容」那几行的 L3 判成 `—`**（wavetable 物理波形表、`SPECS`、
`EQUATIONS`、`TIMINGSET` 表达式、`period_res`/`period_div`、`CHECK`、spec 值、器件周期名、
break waveform）。**这是（推断）**，依据是上面那组签名/返回类型 + 本页读到的语料里
这个族只有这六个成员。**本页不对「L3 永远不能写内容」下全称断言**——
只对**本次读到的语料**负责。

**④ L1 在「内容定义」那几行是 `—`，这一条是文档明说的，不是推断。**
`02.06.06.01.02_Data_organization_of_equation_based_timing`：

> 「The data collections are downloaded with the EQFS and EQSP commands. The collections themselves cannot be edited with firmware commands. But you can query their content with firmware commands, and also change definitions at runtime.」

**`cannot be edited with firmware commands` 是 `—` 的全部依据。**
请把它与「下载 / 上传」那一行分开看：**那条命令能把整块搬进搬出，但搬的是成品，不是编辑。**

**⑤ 「运行时改 spec 值」的 `文件` 格是 `—`，也是文档明说的。**
`02.07.04.01.249_TIMING_SPEC`（与 `02.06.06.02.31_SVLR` 同一条 CAUTION）：

> 「In both cases, changing spec values takes effect without changing the level or timing file! If you want to change spec values permanently you must do so in the corresponding setup file itself.」

**⑥ 「定义 waveform set / timing set 的个数」的 `文件` 格是 `?`，本页没找到。**
`WSUS` 与 `TSUS` 都只说这个数是「自动更新的」，**没有一篇文档说它是 timing setup file 里的哪一行**。
`02.08.04.34.03_Waveform_and_timing_sets` 只说 waveform set 是

> 「A waveform set is a logical entity stored in system memory that holds:」

**`system memory` 不等于「文件里没有」**——所以这里是 `?`，不是 `—`。

**⑦ 语料在两处对「timing set 上限」给了一致性可疑的说法。**
GUI 侧 `02.08.04.34.03.02_Implications_when_running_tests`：

> 「The system lets you create up to 999 different timing sets.」

而 `02.06.06.02.32_TSUS`：

> 「The maximum number of timing sets for one waveform set is 256.」

**999 与 256 对不上。** 本页两种都照实并列，**不选一个当答案**（§10 第 3 条）；
谁对，要等实机或版本页。同一篇 `02.08.04.34.03.02` 另有
`can be up to 卤 6ns`（`卤` 是 `±` 的编码损坏）与 `If you Do not`（大写 D）两处瑕疵。

**⑧ 一处单位说法与其他文档冲突。**
`02.08.04.34.04.03.04.13_Timing_sets__TIMINGSET` 的 `expression` 参数写：

> 「A test system period value in milliseconds (ms) for pins specified by "PINS".」

而 GUI 侧 `02.08.04.34.06.05_Setting_the_period`：

> 「Enter the desired period (in ns) into the period entry field.」

L2 侧 `02.07.04.01.249_TIMING_SPEC`：

> 「In SmarTest, all timing values are in nanoseconds by default.」

**三处里「milliseconds」是一对二。** 本页照实三方并列，**没有替谁改单位**。

**⑨ 两个同形陷阱，必须显式记一笔。**
`02.08.04.34.04.03.04.15_Dealing_with_rounding_problems_in_multiport_setups` 里的
`SCLK` 指的是 **system clock 信号**（`Now the system clock (abbreviated "SCLK") period must be ...`），
**不是 `SCLK?` 那条查询命令**；
`02.08.04.30.02.12_Adding_a_New_Spec_Variable` 里的 `SPEC` 指的是 **`SPECS` 段**，
**不是 `SPEC?` 那条查询命令**。**这两处都不进 L1 列。**

**⑩ 一处 typo 与一处重复词，在 GUI 篇里。**
`02.08.04.34.04.02.01_Verifying_a_multiport_timing_setup`：

> 「The selected equation set defines one or more timing sets. By default, the first timing set is used and displayed in the fields Tset# (timings set number) and Timing (timing set name). To activate another timing set change the timing set number in the Tset# field.」

**`timings set number` 应为 `timing set number`。** 同篇下文还有
`primary multi-port multiport timing specification`（`multiport` 重复）。
**两处都照原样留在引文里。**

**⑪ 图能读，本页读了六张——原先这里写的「图在语料树之外」是错的，连「有三张图」这个数也是错的。**
（**2026-09-20 更正**）

原先这一段写着：语料里**至少有三张图是专门画「GUI 哪一栏对文件哪一行」的**
（`02.08.04.34.04.03.07` 的领域词条配图、`02.08.04.34.05` 的
`Context Defined in Timing Equation Set and Wavetable`、`02.08.04.34.04` 的
`Timing Setup Components`）。**两句话都站不住：**

- **`02.08.04.34.04.03.07_Glossary_of_terms_-_timing_setup.md` 一张图都没有**
  （实测该篇对 `raw/` 的引用 **0 处**）——**那个「领域词条配图」不存在**。
- 另外两个 **alt 名是对的**（`56203.png` / `17845.png`），**而且本页把 alt 名写对了却声称没去看图**
  ——这正说明**「图够不着」这个理由是编的**：**alt 文字本来就能搜到，图也能读到，中间没有障碍。**
- 真实数：本页 sources 里带图的文档共 **24 篇 / 38 张**。**本页读了六张**
  （`56203` `56199` `17845` `22015` `56204` `21812`），**其余三十二张没看**。

**读完之后，⑪ 原来的结论要拆成两半：**

- **「哪一栏对哪一行」这一半，图答了一部分，不再是零。** 三处被钉到字面（细节见证据节 ④）：
  ① **`56203.png` 是全页唯一一张画出文件内容的图**——`EQNSET` / `MODECONTEXT` / `SPECS` /
  `EQUATIONS` / `TIMINGSET` / `period_div` / `WAVETBL` 七样**同屏可见**，
  所以「mode context」「`SPECS` 带单位」「`TIMINGSET` 的 `period`」「`period_div`」四格的
  **文件侧**从「文件格式参考篇的文字」升到**字面可见**；
  ② **`22015.png`** 把 Spec Tool 的三行（`Specification` / `Wavetable` / `Equation`）、
  底部表的三个列名（`Actual` / `Minimum` / `Maximum`）与中区三组检查项钉死；
  ③ **`56199.png`** 把 primary timing setup 的组成（`Pointer to TIMING SET` +
  `Pointer to TIMING EQN SET` + `Pointer to WAVETABLE` + `TIMING SPEC SET n`）画出来了。
- **「一列对一行」这一半仍然做不到，而且原因换了。** 做不到**不是因为图够不着**，
  是因为**`56203.png` 是「某一份具体 setup」的截图，不是格式规范**：它只画了
  equation file 与 wavetable 两块，**没有 specset 的正文、没有 `EQSP` / `EQFS` / `CHECK` /
  `period_res`**。所以**主表里凡是要「文件里那一行长什么样」而 `56203.png` 没画到的格子，
  本页照旧答不了**——这一条结论不变，**变的只是理由**。

**⑫ `02.08.04.34.04.05.01` 里的 `EQNSET` 行与 `WAVETABLE` 行的语义容易读反。**
该篇的说法是：

> 「The subsequent lines in the timing master file associate the parts of the timing setup with a subfile.」

而 `02.08.04.34.04.04` 的例子文件里 `EQNSET 1` 是**方程式正文里的段头**。
**同一个词在两个文件里是两个东西**（master file 的引用行 vs setup file 的段头）——
本页在写「`EQNSET`」时每次都带上下文，**没有把它当成一个东西**。

## 出处

`sources:` **六十八篇**，**全部读的是 raw 原文**（`Read` 工具或 `sed` 直接打开），
**没有一篇是只看 `context` 字段得来的**——§11.1 明令 `context` 是抽取器处理过的，
不是逐字原文，本页每一句引文都回 raw 复读过。
其中**大多数是整篇读的**（含 glossary、`EQSP`、`EQFS`、`TSUS`、`WSUS`、`UPTD`、`SPRM`、
`APRM`、`SPST`、`TIMING_SPEC`、`TimingSetSelector`、`DataManager`、六篇
`TestsuiteProxy` 成员、例子 setup file、两份 master file 格式、两篇 GUI 工具篇）。
**四篇只读了开头一节**：`02.06.16.02.02_JSCF`（Mode of operation 一段）、
`02.06.16.01`、`02.06.06.02.34_UPTD`、`02.06.06.02.29_SPST`。
**另有一篇不在这六十八篇里、只用 `grep` 看过一行**：`02.08.04.34.04.03.04.15`——
就是 ⑨ 那处 `SCLK`；**它没进 `sources:`，因为它只贡献了一处反例的核对**。

**这六十八篇里有 17 篇本身是重复投放**（判据同「证据」②：`source_topic` 去掉 `_N` 后相同），
例如 `02.06.06.02.13_EQFS` 在语料里有 4 份、`02.06.06.02.01_APRM` 有 4 份。
**这不影响引文的逐字性**（同一 TDC 页的副本内容相同），**但影响一件更要紧的事**：
本页开头那句地基——「`timing setups are stored in the setup file as a string parameter of the
EQSP firmware command`」——**出自 `02.08.04.34.04.05.02`，而它是 level 章
`02.08.04.14.02.05.02` 的副本**。同理，本页引 `CKST?` / `SPST` 的那篇
`02.08.04.34.04.03.06_Error_Reporting` 是 `02.08.04.14.02.03.10` 的副本。
**换句话说：timing 与 level 在这个点上是同一篇文档，不是两篇说法一致**——
**本页不把它当成「两处独立证据」**（§10 第 0 条）。

**本页没做的**：

- **看了六张图（2026-09-20 加）。** 就是 `56203.png`、`56199.png`、`17845.png`、`22015.png`、
  `56204.png`、`21812.png`（各自出自哪篇见「证据」④ 与「对不上的地方」⑪）。
  **六张都整张看完**，图上读到的字**逐条回 9,398 篇 raw md 里查过 grep 命中**——
  本页凡写「grep 不到」的，都是实测 0 命中。**本页 sources 里带图的文档共 24 篇 / 38 张，
  其余三十二张没看**（多数是图标、工具栏、对话框小图，例如 `02.08.04.34.06` 的三张）。
  **原先本页在「对不上的地方」⑪ 里写着图「在语料树之外」——那是错的**，见 ⑪ 的更正。
- **没有实跑。** 没有在机台上开过 Timing Setup 窗口、没有 Generate 过 wavetable、
  没有 Download 过 setup、没有拆过 master file。`verified: doc-only` 指的就是这件事。
- **`02.06` 的命令页只读了主表 L1 列用到的那些**（`EQFS` / `EQSP` / `WSUS` / `TSUS` /
  `SPRM` / `APRM` / `UPTD` / `SPST` / `PCLK` / `CLKR` / `PDIV` / `DCDT` / `WFDS` / `WAVE` /
  `BWDS` / `BWDF` / `SVLR` 及抖动族）。**其余三十多条 timing setup 命令一条没读**，
  所以主表里没有它们的位置——**这是本页的取材边界，不是它们不属于本阶段**。
- **L2 列只读了四篇**（`TIMING_SPEC`、`TimingSetSelector`、`02.07.03.03.02.01`、
  以及作为链接目标出现的 `SpecSearch`）。**`02.07.11.01.05.*`（协议侧的
  `Timing_equation_file` / `Wavetable_file` / `Equation_system`）只在链接里见过**，
  它们链到了 `02.08.04.34.04.03.03_Timing_Wavetables_-_Reference`，
  **但本页没读正文，所以没往 L2 列里填**。这一条**值得后续单独查一次**。
  —— 同一个待办还适用于 `02.07.04.02.17` 之外的所有 `TimingSetSelector` 用法。
- **L3 列只读了 `02.09.01.14.02.01` 的六个 timing 成员与 `02.09.01.09.02_DataManager`。**
  `TestsuiteProxy` 的 33 个成员里其余 27 个、以及 TPI 那 31 篇里的其余 30 篇，
  **本页一篇没读**——它们属不属于 timing，本页不判。
- **`02.09_Test_Program_Management` 那 1,213 篇没有地毯式查过。**
  所以本页 L3 列的 `—` **只是「这六个成员覆盖不到」**，
  **不是「L3 里没有别的东西」**（schema §2.1 的硬规矩二）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/timing.md`。
  后者是**待办**：[[timing]] 那页目前不知道本页存在。
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。

**本页 `layer: n/a` 的理由**：§6 要求 mapping 页必填 `layer`，而本页**本身不属于任何一层接口**
（它是对照表，不是接口）——`n/a` 是这个六值枚举里为这种情况准备的值。

`verified: doc-only`
