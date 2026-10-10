---
type: object
title: Timing Setup Tool
layer: gui
stage: timing
tags: [gui, timing, timing-setup-tool, timing-setup-window, equation-based-timing, wavetable, timing-equation-set, timing-specification, waveform-set, timing-set, mode-context, device-cycle, spec-set, wavetable-editor]
related: [timing, mapping-timing, spec-tool, wavetable, wavetable-file, timing-equation-set, timing-specification, timing-file, timing-master-file, waveform-set, test-program-explorer, timing-diagram-tool, setup-management-tool, level-setup-tool, smartest-6.3.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34_Timing_Setup_Tool.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Timing Setup Tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **49,352 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34_Timing_Setup_Tool.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.02_Data_organization_of_equation_based_timing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.05_Defining_the_timing_specification.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.01_APRM_-__Activate_PRiMary_sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.02_BWDF__BWDF__-__Break_Waveform_DeFinition.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.03_BWDS__BWDS__-__Break_Waveform_Definition_String.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.04_CDCP__-__Cycle_Device_Cycle_Parameter.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.05_CLKR__CLKR__-__CLocK_Resolution.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.06_DCDT__DCDT__-__Device_Cycle_DefaulT.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.07_DCUD_-__Device_Cycle_UnDefine.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.08_DFCR__DFCR__-__DeFine_Clock_Routing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.09_DPRT__DPRT__-__Default_PRimary_Timing_sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.10_DSCP__DSCP__-__Define_System_Control_Parameter.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.11_EDDC__-__EDge_in_Device_Cycle.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.12_EDSP__EDSP__-__EDge_SPecification.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.13_EQFS_-__EQuation_FileS_command_transfer.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.14_EQSP__EQSP__-__EQuation_SPecification_transfer.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.15_ETDS__ETDS__-__Edge_Timing_Definition_String.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.16_ETIM__ETIM__-__Edge_TIMing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.17_EUDS__-__Edge_Usage_Definition_String.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.18_EVCK__-__EVent_ClocK.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.19_FTCG__FTCG__-__Functional_Test_ConfiGure.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.20_PCLK__PCLK__-__Pin_CLocK.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.21_PDIV__-__Period_DIVider.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.22_RCLK__-__Reference_CLocK_source.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.23_RSET_-__ReSET.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.24_SCLK__-__System_CLocK_query.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.25_SDSC__-__Set_number_DeSCriptions.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.26_SPCP__-__SPeCification_Port_list.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.27_SPEC__-__SPECification.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.28_SPRM__SPRM__-__Set_PRiMary_sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.29_SPST__-__SPecset_STatus.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.30_STRS__-__Spec_TRansition_Search.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.32_TSUS__TSUS__-__Timing_Sets_USed.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.33_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.34_UPTD__UPTD__-__UP_To_Date.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.35_VCLK__-__Verify_CLocK.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.36_VDCG__-__Verify_Device_Cycle_for_Group.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.37_VTIM__-__Verify_TIMing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.38_VWFG__-__Verify_WaveForms_in_Groups.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.39_VWFS__-__Verify_WaveForm_Sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.40_WAVE__WAVE__-__WAVEform.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.41_WFDF__WFDF__-__WaveForm_DeFinition.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.42_WFDS__WFDS__-__WaveForm_Definition_String.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.43_WFUD_-__WaveForm_UnDefine.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.44_WRST_-__Waveform_ReSeT.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.45_WSDM__WSDM__-__Waveform_Set_Display_Mode.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.46_WSUS__WSUS__-__Waveform_Sets_USed.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.01_Data_organization_of_equation_based_timing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05.01_Master_file_format_for_timing_setup.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06_Using_the_Timing_Setup_Tool.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Timing Setup Commands › Concepts of timing setup › Data organization of equation based timing）

The following figure exemplifies the structure of equation based timing by a schematic setup:

 !`Timing Specifications`（raw: `../../../../raw/10596.png`）

### Example（取自子主题 Timing Setup Commands › Concepts of timing setup › Defining the timing specification）

The following is a simple example of a `single-port timing specification`（raw: `02.08.04.34.04.01_Single-port_timing_setup.md`）:

```
EQNSET 1 "default"

WAVETBL "table1"
CHECK all

SPECSET 1 "sp1"

# SPECNAME *****ACTUAL***** *****MINIMUM**** *****MAXIMUM**** UNITS COMMENT
f          100                                                [MHz]
```

This specification uses spec set 1 for equation set 1. It will be identified to the firmware commands by 101. The base variable f is set to 100. The `CHECK all statement`（raw: `02.08.04.34.04.03.05.01_CHECK_Statement_Options.md`） activates all consistency checks (see `Consistency checks for edge delays`（raw: `../02.06_Command_Reference/02.06.06.01.05.01_Consistency_checks_for_edge_delays.md`）).

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › APRM -  Activate PRiMary sets）

```
APRM {mode}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › APRM -  Activate PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98485_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：mode | Selects the activation mode:

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › APRM -  Activate PRiMary sets）

```
APRM CNL
```

### BWDF（取自子主题 Timing Setup Commands › List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### BWDF?（取自子主题 Timing Setup Commands › List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF? {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {(pinlist)}
```

returns:

```
BWDF {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98497_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number …
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

This example defines a pulse for waveform set 1, and for pins D0 to D3, driving to 1 at edge action 4 and to 0 at edge action 5. The tri-state formatter is not used.

### BWDS（取自子主题 Timing Setup Commands › List of timing setup commands › BWDS  BWDS  -  Break Waveform Definition String）

```
BWDS {wvf_set}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

### BWDS?（取自子主题 Timing Setup Commands › List of timing setup commands › BWDS  BWDS  -  Break Waveform Definition String）

```
BWDS? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {(pinlist)}
```

returns:

```
BWDS {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98498_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. Enter PRM for the Primary waveform set. The maximum number is determined by…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `WFDS, WFDS? - (WaveForm Definition String)`（raw: `../02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › BWDS  BWDS  -  Break Waveform Definition String）

```
> BWDS? 1,,,(@)
< BWDS 1,,,"",(io)
< BWDS 1,,,"d1:F00 d5:F10",(clk)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › CDCP  -  Cycle Device Cycle Parameter）

```
CDCP? {start_cycle}, {no_of_cycles}, {strt_disp}, {disp_length}, {(pinlist)}
```

returns:

```
CDCP {cycle}, {dev_cyc_name}, {dev_cyc_len}, {DD1}, {DD2}, {ED1}, {ED2}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › CDCP  -  Cycle Device Cycle Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98499_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle to be analyzed. The range of values for this parameter depends on the analysis mode: In the Start …

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › CDCP  -  Cycle Device Cycle Parameter）

```
> CDCP? 0,8,0,8,(S0_1)
< CDCP 0,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 1,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 2,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 3,"MYDC",2,F00,N,N,N,(S0_1)
< CDCP 5,"MYDC",2,F10,N,N,N,(S0_1)
< CDCP 7,"DNRZ",1,F10,N,N,N,(S0_1)
> CDCP? 2,6,4,2,(S0_1)
< CDCP 5,"MYDC",2,F10,N,N,N,(S0_1)
< CDCP 7,"DNRZ",1,F10,N,N,N,(S0_1)
```

In the second call of CDCP? (the first call just serves to display the underlying situation) the range of interest starts at vector 6. Note that the reply starts with vector 5, and that the first occurrence of MYDC, which lies between vector 2 and vector 6, is not displayed.

### CLKR（取自子主题 Timing Setup Commands › List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res}
```

### CLKR?（取自子主题 Timing Setup Commands › List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

```
CLKR?[type,] {waveform_set|specset_id|"multi-port_spec"}
```

returns:

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res|clock_res}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98504_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `Automatic calculation of period resolution for single-port setups`（raw: `../02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

```
> CLKR 1,,10
> CLKR? 1
< CLKR 1,1000,10

```

This example sets and queries the period resolution (10 ns) for waveform set 1. Ignore the returned value of the ref_period parameter.

```
> CLKR? "spec_port_1_port_2"
< CLKR "spec_port_1_port_2",50,5.555555556
```

This example queries the period resolution for the multi-port specification `spec_port_1_port_2`.

### DCDT（取自子主题 Timing Setup Commands › List of timing setup commands › DCDT  DCDT  -  Device Cycle DefaulT）

```
DCDT {waveform_set}, {"default_name"}
```

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DCDT  DCDT  -  Device Cycle DefaulT）

```
DCDT 1,"HOLD"
```

This example defines the default device cycle name HOLD for Waveform Set 1.

```
DCDT? "fast_ARM",(ARMPort)
DCDT "fast_ARM","Cycle",(ARMPort)
```

This example queries the default device cycle name for the ARMPort port in the multi-port specification fast_ARM.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › DCUD -  Device Cycle UnDefine）

```
DCUD {waveform_set},{"dev_cyc_name"},{(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › DCUD -  Device Cycle UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98529_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DCUD -  Device Cycle UnDefine）

```
DCUD 1,"WRITE"
```

This example deletes the device cycle `WRITE` for waveform set 1 from the device cycle table.

### DFCR（取自子主题 Timing Setup Commands › List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

```
DFCR {source_group},{dest_group}
```

### DFCR?（取自子主题 Timing Setup Commands › List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

```
DFCR?
```

returns (for every group except G4):

```
DFCR {source_group},{dest_group}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98541_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：source_group | specifies the hardware group whose local clock is to be routed to dest_group. The format is Gx, where x is the group number.

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

```
> DFCR?
<
> DFCR G1,G8
> DFCR?
< DFCR G4,G3
< DFCR G4,G1
< DFCR G4,G5
< DFCR G1,G6
< DFCR G1,G2
< DFCR G1,G8
< DFCR G1,G7
```

This example changes the default routing (DFCR? gives an empty reply). Note that the inherited clocks of G6 and of all successors of G6 are also changed.

### DPRT（取自子主题 Timing Setup Commands › List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT {"multi-port_spec"}, [timing_set_no|"timing_set_list"][,(port)]
```

### DPRT?（取自子主题 Timing Setup Commands › List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT?
```

returns:

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT?
```

returns:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT? [(port)]
```

returns:

```
DPRT {"multi-port_spec"}, {timing_set_no|"timing_set_list"}[,(port)]

```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98570_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number.
> 表内引用（1 条，供检索）：`TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT?
```

returns:

```
DPRT 3,4
```

On sending a query the system reports that the default primary waveform set is 3 and the default primary timing set is 4.

### DSCP（取自子主题 Timing Setup Commands › List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP `[device_cycle`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_device_cycle`）], `[waveform_set`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）], `[timing_set`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_timing_set`）], `[level_set`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_level_set`）], `[dps_set`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_dps_set`）], `[pmu_set`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_pmu_set`）],
                        `[devicecycle_set`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_devicecycle_set`）], `[routing_set`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_routing_set`）], `[period_res_prec`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_period_res_prec`）],

```

### DSCP?（取自子主题 Timing Setup Commands › List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP?
```

returns:

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
       {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
       [period_res_compatibility_model]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98578_5.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：device_cycle | The device_cycle parameter is an integer that defines the absolute maximum number of device cycles that you can create for one pin.Default: 256Ma…
> 表内引用（2 条，供检索）：`waveform sets and wavetables`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） · `waveform_set`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › EDDC  -  EDge in Device Cycle）

```
EDDC? [waveform_set], [timing_set], {edge_spec},
[dev_cyc_name], [dc_ref], [direction], {(pinlist)}
```

returns:

```
EDDC {edge_number}, {dev_cyc_name}, [reuse_flag], {(pinlist)}
```

### EDSP（取自子主题 Timing Setup Commands › List of timing setup commands › EDSP  EDSP  -  EDge SPecification）

The edge_spec parameter specifies a physical edge (d1 through d8 or r1 through r8):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}
```

The edge_spec parameter is a data parameter (D1, D2, C1, C2, E1, or E2):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}
```

### EDSP?（取自子主题 Timing Setup Commands › List of timing setup commands › EDSP  EDSP  -  EDge SPecification）

```
EDSP? [dc_ref], {(pinlist)}
```

returns:

```
EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98589_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set | Specifies a waveform set number for a fixed timing setup.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › EQFS -  EQuation FileS command transfer）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98592_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification to use:

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

This example loads the level equation file from /tmp/level_equation.

### EQSP（取自子主题 Timing Setup Commands › List of timing setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP {spec_type}, {part}, {#spec(data)}
```

### EQSP?（取自子主题 Timing Setup Commands › List of timing setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP?{spec_type}, {part}
```

returns:

```
EQSP {spec_type}, {part}, {#spec(data)}
```

if these are not empty, for backward compatibility.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98593_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：spec_type | The mandatory parameter defines which specification type to use. Use: LEV to specify levels TIM to specify timing

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

The following example queries the current wavetables:

```
> EQSP? TIM,WVT
< EQSP TIM,WVT,#9000000127WAVETBL table1  # derived from waveform set 1

  PINS Pin1 Pin2
  WFDS 0  "d1:D11"
  1    0   .   .   .
  2    1   .   .   .
  BWDS ""

  @
```

### ETDS（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### ETDS?（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

ETDS? {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {(pinlist)}

returns:

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98599_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `Defining waveforms for Pin Scale 9G pins`（raw: `../02.06_Command_Reference/02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`） · `Selecting and ordering edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

```
> ETDS 1,1,,"e1:0 e2:2 e3:6 e4:4",(io)
> ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
> ETDS? 1,1,,(@)
< ETDS 1,1,,"d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4",(io)
< ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
```

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

The following example shows the various possibilities for using ETDS with fast pins:

```
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5 d3:10 d4:15",(CP)
> ETDS 401,1,,"d2:5.5",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5.5 d3:10 d4:15",(CP)
> ETDS 401,1,,"pdiv:4 d1:3 d3:14",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:14 d4:18",(CP)
> ETDS 401,1,DELTA,"d3:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:12 d4:18",(CP)
> ETDS 401,1,DELTA,"pdiv:4 d1:0 d2:1 d4:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:6 d3:10 d4:14",(CP)
```

Note in particular the effect of the first instance of the command in DELTA mode. The negative offset is not applied to the actual value of d3, which is 14, but to the calculated default value, which is 13.

### Example 3（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

This example shows how to set and retrieve a delay of a multi-port specification:

```
> ETDS? "mu_timing",2,,(In1)
< ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ETDS "mu_timing",2,,"d1:0.5",(In1)
> ETDS? "mu_timing",2,,(In1)
< ETDS "mu_timing",2,,"d1:0.5",(In1)
```

The specification name and the pin name identify the port (no pin may occur in more than one port within the same specification). Then the port and the specification identify the equation set.

### ETIM（取自子主题 Timing Setup Commands › List of timing setup commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

### ETIM?（取自子主题 Timing Setup Commands › List of timing setup commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM? {waveform_set}, {timing_set}, {(pinlist)}
```

returns:

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

or:

```
ETIM? {specset_id}, {timing_set_no}, {(pinlist)}
```

returns:

```
ETIM {specset_id}, {timing_set_no}, [t1], [t2], [t3], [t4], [t5], [t6],{(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98600_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `ETIM, ETIM? - (Edge TIMing)`（raw: `../02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM 1,1,2,4,8,6,10,,(DATA)
```

This example sets the edge delays for the pin group DATA specified for waveform set 1 and timing set 1. Edges 1 to 5 are set to 2,4,8,6 and 10 ns respectively, edge 6 is unused. If no previous setting for edge 6 exists in waveform set 1 and timing set 1, then its delay remains at 0.0 ns.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › EUDS  -  Edge Usage Definition String）

```
EUDS? {waveform_set}, [mode], {(pinlist)}
```

returns:

```
EUDS {waveform_set}, {definition_string}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › EUDS  -  Edge Usage Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98601_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter ALL for all defined waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The wa…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › EUDS  -  Edge Usage Definition String）

```
EUDS? 1,,(@)
EUDS 1,"d1 d2 d3 r4",(io)
EUDS 1,"d1 d2 d3 d4 d5 d6 d7 d8",(clk)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › EVCK  -  EVent ClocK）

```
EVCK? {"multi-port_spec"}, {(port_list)}
```

returns:

```
EVCK {"multi-port_spec"}, event_clock_per, {(port)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › EVCK  -  EVent ClocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126417_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：multi-port_spec | Name of a multi-port timing specification.

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › EVCK  -  EVent ClocK）

```
>  SCLK? "mu_burst"
<  SCLK "mu_burst",480
>  EVCK? "mu_burst",(@@)
<  EVCK "mu_burst",2448,(PortA)
<  EVCK "mu_burst",2448,(PortB)
<  EVCK "mu_burst",480,(PortD)
<  EVCK "mu_burst",480,(PortE)
```

This example returns the system clock period and the event clock periods for the multi-port timing specification `mu_burst`. The event clock periods of `PortD` and `PortE` equal the system clock period, those of `PortA` and `PortB` are different.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › FTCG  FTCG  -  Functional Test ConfiGure）

FTCG

```
FTCG {parameter}, {mode}, {(portlist)}
```

  FTCG?

```
FTCG? {parameter}, {(@@)}
```

returns:

```
FTCG {parameter}, {mode}, {(portlist)}
```

  Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98606_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：parameter | The parameter to be used is SKPR (SKip PRimaries).

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › FTCG  FTCG  -  Functional Test ConfiGure）

The following example illustrates the dependence of the FTCG command on the current sequencing group definitions.

```
> SQLB "MP_burst1",MPBU,28,31,"SG1",(clock)
> SQLB "MP_burst1",MPBU,28,29,"SG2",(data1)
> SQLB "MP_burst1",MPBU,31,32,"SG2",(data2)
> SQLB "MP_burst2",MPBU,32,33,"SG1",(clock)
> SQLB "MP_burst2",MPBU,30,31,"SG1",(data1)
> SQLB "MP_burst2",MPBU,33,34,"SG2",(data2)
> FTCG SKPR,ON,(clock)
> FTCG SKPR,NEVER,(data2)
> SPRM "cont_clock",,,
> SQSL "MP_burst1"
> SQGB ACQF,0
> FTST?
...
> SQSL "MP_burst2"
> FTST?
...
```

In the first functional test, sequencing group `SG1` only contains the port `clock`, and therefore activation of primary sets is suppressed at the start of `MP_burst1` only for `clock`, whereas it is enforced for ports `data1` and `data2`. In the second test, `SG1` contains both `clock` and `data1`, and therefore activation is suppressed for both these ports at the start of `MP_burst2`, and enforced only for `data2`.

### PCLK（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

Fixed timing:

```
PCLK{waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### PCLK?（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

Fixed timing:

```
PCLK?{waveform_set},{timing_set},{(pinlist)} [,query_mode]
```

returns:

```
PCLK {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK? {specset_id|"multi-port_spec"}, {timing_set}, {(pinlist|portlist)} [,query_mode]
```

returns:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98682_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

```
PCLK 101,1,20,(@)
```

This example sets the test system period for specification 101 to 20 ns.

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

```
PCLK 101,1,40,(S1)
```

This example sets the test system period of pin S1 for specification 101 to 40 ns.

The `VCLK?`（raw: `../02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md`） query checks whether a PCLK command with the specified parameter values was accepted with or without auto-correction.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › PDIV  -  Period DIVider）

```
PDIV? {specset_id|"multi-port_spec"|"wavetbl"} [,spec_type][,(pinlist)]
```

returns:

```
PDIV {specset_id|"multi-port_spec"}, {period_div}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › PDIV  -  Period DIVider）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98684_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：specset_id | Identifier of a timing specification, which is derived as follows: 100 * equation_set_no + specset_no

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › PDIV  -  Period DIVider）

```
> PDIV? "fast",WFT,(I1)
< PDIV "fast",WFT,6,(I1)
```

This example queries the implicit period divider of the fast pin I1 in the wavetable `fast`. The factor is 6.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › RCLK  -  Reference CLocK source）

```
RCLK?
```

returns:

```
RCLK {clock_string}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › RCLK  -  Reference CLocK source）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98715_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：clock_string | The string shows which clock source is used as reference clock. Possible values are: EXTERNAL INTERNAL

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › RCLK  -  Reference CLocK source）

```
RCLK?
```

returns:

```
RCLK INTERNAL
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › RSET -  ReSET）

```
RSET {specifier}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › RSET -  ReSET）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98723_5.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：specifier | The specifier can be:
> 表内引用（1 条，供检索）：`UHCM`（raw: `../02.06_Command_Reference/02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › RSET -  ReSET）

```
RSET TIM
```

This example resets all waveform sets and timing sets and loads the hardware with the default vector rate and edge placement values. Only waveform set 1 and timing set 1 in waveform set 1 is active.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SCLK  -  System CLocK query）

```
SCLK? {wf_set|specset_id|"multi-port_spec"|ALL|PRM}
```

returns:

```
SCLK {wf_set|specset_id|"multi-port_spec"} {sclk_val}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SCLK  -  System CLocK query）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98728_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：wf_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? - …
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › SCLK  -  System CLocK query）

```
> SCLK? 401
< SCLK 401,480
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SDSC  -  Set number DeSCriptions）

```
SDSC? {spec_type}, {type}, [setup_comp_1], [setup_comp_2], ["description"]
```

returns:

```
SDSC {spec_type}, {type}, [setup_comp_1], [setup_comp_2], {"description"}
```

Alternatively, for multiport specifications:

```
SDSC? {TIM}, {type}, [setup_comp_1], {"multi-port_spec"}, ["description"][, (portlist)]
```

returns:

```
SDSC {TIM}, {type}, [setup_comp_1], {"multi-port_spec"}, {"description"}, {(port)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：21 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

The following table explains the interpretation of the setup_comp_1 and setup_comp_2 parameters for every accepted value pair of the spec_type and type parameters:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729_4.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 4 列。
> 首行（上游原文）：spec_type | type | setup_comp_1 | setup_comp_2

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,,,
< SDSC TIM,EQN,1,,"gross_func_eqn"
< SDSC TIM,EQN,2,,"specs_search_eqn"
< SDSC TIM,EQN,3,,"speed_eqn"
```

This example returns all defined equation sets.

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,2,"spec_port_1_port_2",,(port_1)
< SDSC TIM,EQN,1,"spec_port_1_port_2",
     "gross_func_eqn",(port_1)
```

This example returns the equation set that is associated with port port_1 in the multiport specification

spec_port_1_port_2. Note that the setup_comp_1 parameter is ignored.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SPCP  -  SPeCification Port list）

```
SPCP? {"multi-port_spec"|ALL}
```

returns:

```
SPCP {"multi-port_spec"}, {(portlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SPCP  -  SPeCification Port list）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98738_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：multi-port_spec | Defines the multi-port specification for which the ports are to be queried. You can enter ALL in order to display the ports for all defined mu…

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › SPCP  -  SPeCification Port list）

```
> SPCP? ALL
< SPCP "spec_port_1_port_2",(port_1,port_2)
< SPCP "spec_ClkP_P1_P2",(ClockPort,p_CP_1,p_CP_2)
< SPCP "spec_ssearch_port_1_port_2",(port_1,port_2)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SPEC  -  SPECification）

```
SPEC? {"module:resource"},["details"],[context], [(pinlist)]
```

returns:

```
SPEC {"module:resource"},["details"],[context], {answer},[(pinlist)]
```

   Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98739_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 3 列。
> 首行（上游原文）：module:resource | Specifies the module and the resource about which information is to be returned. Currently, the following values are allowed:

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › SPEC  -  SPECification）

```
SPEC? "Result:Xmodes",,,(@)
```

returns

```
SPEC "Result:Xmodes",,,"1,2,4,6,8",(...)
```

This example queries which x-modes are possible for the result module on a Smart Scale system. On a Pin Scale system, x-mode 6 would be omitted in the reply.

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › SPEC  -  SPECification）

The second example queries the termination modes that can be specified with the `TERM`（raw: `../02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） command for pin "PS1600_pin" and level set 1:

```
SPEC? "Level:Term",,1,(PS1600_pin)
```

returns

```
SPEC "Level:Term",,1,"OFF,T,H,L,A,C,CT,HV,DIFHIZ",(PS1600_pin)
```

### Example 3（取自子主题 Timing Setup Commands › List of timing setup commands › SPEC  -  SPECification）

The third example queries the range of the fixture delay:

```
SPEC? "Timing:FxdlRange",,"Global",
```

returns

```
SPEC "Timing:FxdlRange",,"Global","-0.015000,13.200000",()
```

The query returns the range for Pin Scale systems.

Note: Parameter pinlist is irrelevant for this query and may be omitted.

### SPRM（取自子主题 Timing Setup Commands › List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

```
SPRM [waveform_set_no], [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or:

```
SPRM {timing_specset_id}, [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or, for multiport specifications:

```
SPRM {"multi-port_spec"}, [timing_set_no|"timing_set_list"], [level_set_id|level_set_no],[dps_set_id|dps_set_no] [,(port)]
```

### SPRM?（取自子主题 Timing Setup Commands › List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

```
SPRM?
```

returns:

```
SPRM {waveform_set_no}, {timing_set_no}, {level_set_no|level_set_id}, {dps_set_no|dps_set_id}
```

or:

```
SPRM {timing_specset_id}, {timing_set_no}, {level_set_id|level_set_no}, {dps_set_id|dps_set_no}
```

or, for multiport specifications:

```
SPRM? [(port)]
```

returns:

```
SPRM {"multi-port_spec"}, {timing_set_no|"timing_set_list"}, {level_set_id|level_set_no},{dps_set_id|dps_set_no} [,(port)]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98742_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set_no | The identification number of the waveform set. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum num…
> 表内引用（6 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `CONF, CONF? - (CONFiguration)`（raw: `../02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DSCP`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `LSUS, LSUS? - (Level Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`） · `DSUS, DSUS? - (Dps Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

The following example shows how to define and query primary timing sets for the multi-port specification spec_ClockP_P1_P2, which contains three ports:

```
> SPRM "spec_ClockP_P1_P2","2,1,2",,
> SPRM?
< SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003
> SPRM "spec_ClockP_P1_P2",2,,,(port_1.CP_1)
> SPRM?
< SPRM "spec_ClockP_P1_P2",2,101002,101003
> SPRM? (port_1.CP_1)
< SPRM "spec_ClockP_P1_P2",2,101002,101003,(port_1.CP_1)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

```
SPST? {spec_type}, {equation_set_no}, {specset_no}
```

returns:

```
SPST {spec_type}, {equation_set_no}, {specset_no}, {status}
```

or, for multiport specifications:

```
SPST? {spec_type}, , {"multi-port_spec"}
```

or

```
SPST? {spec_type}, PRM,
```

returns:

```
SPST {spec_type},, {"multi-port_spec"}, {status}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

Status bits for the status parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743_4.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：Bit | Description | Value
> 表内引用（10 条，供检索）：`ETIM`（raw: `../02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`） · `ETDS`（raw: `../02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） · `PCLK`（raw: `../02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） · `CLKR`（raw: `../02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md`） · `DRLV`（raw: `../02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`） · `RCLV`（raw: `../02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`） · `TERM`（raw: `../02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） · `PSLV`（raw: `../02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`） · `SHVL`（raw: `../02.06_Command_Reference/02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md`） · `SVLR`（raw: `../02.06_Command_Reference/02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`）

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

```
> SPST? lev,all,all
< SPST LEV,1,1,0
```

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

```
> SPST? tim,all,all
<  SPST TIM,1,1,0
< SPST TIM,2,22,0
```

### Example 3（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

```
> SPST? TIM,,"mu_burst"
< SPST TIM,,"mu_burst",6
```

In this last example, a multi-port specification is queried. The answer says that bits 1 and 2 have been set. This has the effect that a drive or receive period 1 limit violation will be ignored, and only a period 2 limit violation will be recorded.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › STRS  -  Spec TRansition Search）

```
STRS? ["exec_context",] [start], [stop], {mode}, [(pinlist)], {spec_type}, {"spec_name[@port[@UNCHANGED]]"}, [stepwidth], {resolution}
```

returns:

```
STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › STRS  -  Spec TRansition Search）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98762_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts .
> 表内引用（4 条，供检索）：`Using execution contexts`（raw: `../02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） · `DFGP`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） · `Global and local scope of base variables`（raw: `../02.06_Command_Reference/02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`） · `Modifying the period for a search or shmoo in a multi-port setup`（raw: `../02.06_Command_Reference/02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › STRS  -  Spec TRansition Search）

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98764_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:
> 表内引用（1 条，供检索）：`Global and local scope of base variables`（raw: `../02.06_Command_Reference/02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The following example queries the values of the spec variable f in a setup where both single-port and multi-port specifications occur:

```
> SVLR? TIM,ALL,ALL,"f"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",35
< SVLR TIM,,"spec_p_1_p_2","f@p_2",33
< SVLR TIM,1,1,"f",37
```

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The next example queries in which equation sets the spec variable f occurs:

```
> SVLR? TIM,ALL,,"f"
< SVLR TIM,1,,"f",
< SVLR TIM,2,,"f",
```

### Example 3（取自子主题 Timing Setup Commands › List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

For this example assume that the primary timing is a multi-port specification which contains the two ports p_1 and p_2, and that p_1 and p_2 share the spec variable f in this specification. Assume further that f has been set to scope global for the port p_1. Now query the current value of f for p_1, change it globally, and query it again:

```
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",33
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",43
```

Since f is global for p_1, its value has been modified. Now change the value a second time, but this time locally, and then try to change it globally again:

```
> SVLR TIM,PRM,,"f@p_1",53
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",53
```

The second global command has no effect because f has only local scope after issuing the local command.

### TSUS（取自子主题 Timing Setup Commands › List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS {waveform_set},{timing_set}
```

### TSUS?（取自子主题 Timing Setup Commands › List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS? {waveform_set}
```

returns:

```
TSUS {waveform_set},{timing_set}
```

Or:

```
TSUS? {specset_id}
```

returns:

```
TSUS {specset_id},{timing_set}
```

Or, for multiport specifications:

```
TSUS? {"multiport_spec"}[,(portlist)]
```

returns:

```
TSUS {"multiport_spec"},{timing_set}[,(port)]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98817_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS 3,7
```

This example defines a maximum of 7 timing sets in waveform set 3.

```
TSUS? "spefc",(ARMPort)
TSUS "spefc",3,(ARMPort)
```

This example queries the number of timing sets defined for port ARMPort in the multiport specification spefc.

### TSUX（取自子主题 Timing Setup Commands › List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

```

TSUX {waveform_set},{timing_set}
```

### TSUX?（取自子主题 Timing Setup Commands › List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

```

TSUX? {waveform_set}
```

returns:

```
TSUX {waveform_set},{timing_set}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98818_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter ALL for all waveform sets in the query command.
> 表内引用（1 条，供检索）：`TSUS`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

### UPTD（取自子主题 Timing Setup Commands › List of timing setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD {status}, {flag}
```

### UPTD?（取自子主题 Timing Setup Commands › List of timing setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD? {status}
```

returns:

```
UPTD {status}, {flag}
```

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD? CONF
```

This example requests if the pin configuration data has been changed since the file was last loaded or saved. If the data has not changed, the response is:

```
UPTD CONF,1
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VCLK  -  Verify CLocK）

```
VCLK? {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

returns:

```
VCLK {autocorrect}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VCLK  -  Verify CLocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98844_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VCLK  -  Verify CLocK）

```
VCLK? 1,1,20,(@)
```

This example checks if a period of 20 ns will cause auto-correction to the edge placements in Timing Set 1 of Waveform Set 1 on any pin. If no auto-correction will occur the following string is returned:

```
VCLK 0
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VDCG  -  Verify Device Cycle for Group）

```
VDCG? {waveform_set}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {waveform_set}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {specset_id}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {specset_id}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {wavetable_name}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {wavetable_name}, {dev_cyc_name}, {dev_cyc_len}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VDCG  -  Verify Device Cycle for Group）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98846_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 4 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VDCG  -  Verify Device Cycle for Group）

```
VDCG? 1,ALL,(inputs)
```

returns:

```
VDCG 1,ALL,SLEN
```

This example checks the consistency of all device cycles for pins in the pin group "inputs" in waveform set 1. The test system replies that all device cycles for the specified group are consistently defined.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VTIM  -  Verify TIMing）

```
VTIM? {waveform_set},{timing_set},{(pinlist)}
```

returns:

```
VTIM {status}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VTIM  -  Verify TIMing）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98862_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VTIM  -  Verify TIMing）

The following example illustrates the working of VTIM? in a multi-port setup. The pins S1_1 and DS0_1 belong to the same port, and S1_2 belongs to another one.

```
> ETDS? "spec_port_1_port_2",ALL,,(S1_1,DS0_1,S1_2)
< ETDS "spec_port_1_port_2",1,,"d1:0 d2:30",(S1_1,DS0_1)
< ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(S1_1)
< ETDS "spec_port_1_port_2",2,,"d1:1 d2:12",(DS0_1)
< ETDS "spec_port_1_port_2",1,,"d1:-0.67 d2:1.33 d3:9.3",(S1_2)
```

This call of `ETDS?`（raw: `../02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） shows that the edge timings of S1_1 and DS0_1 are the same in timing set 1, but not in timing set 2 of the port to which these pins belong.

```
> PCLK? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< PCLK "spec_port_1_port_2",1,50,(S1_1)
< PCLK "spec_port_1_port_2",2,20,(S1_1)
< PCLK "spec_port_1_port_2",1,50,(DS0_1)
< PCLK "spec_port_1_port_2",2,20,(DS0_1)
< PCLK "spec_port_1_port_2",1,16.667,(S1_2)
```

This call of `PCLK?`（raw: `../02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） shows that the periods of S1_1 and DS0_1 are the same in the two timing sets of the port.

```
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 0
```

VTIM? returns 0 because of the different timings for S1_1 and DS0_1 in timing set 2.

```
> ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(DS0_1)
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 1
```

After changing the edge timing of DS0_1 in timing set 2 to the values of S1_1 with a call of `ETDS`（raw: `../02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`）, VTIM? returns 1 although DS0_1 has a different timing in timing set 1 and in timing set 2, and S1_2, which belongs to another port, has different values altogether.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VWFG  -  Verify WaveForms in Groups）

There are three different ways to call VWFG?:

```
VWFG? {waveform_set}, ["dev_cyc_name"], {(pinlist)}
VWFG? {specset_id},["dev_cyc_name"],{(pinlist)}
VWFG? {wavetable_name}, ["dev_cyc_name"], {(pinlist)}
```

All three forms return:

```
VWFG {status}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VWFG  -  Verify WaveForms in Groups）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98863_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VWFG  -  Verify WaveForms in Groups）

```
> VWFG? "spec_search_wtb","SBC",(ser_in)
< VWFG 1
> VWFG? "spec_search_wtb",,(ser_in)
< VWFG 0
```

According to this example, the waveform and device cycle definition for device cycle SBC are the same for the pins in the group ser_in within the wavetable spec_search_wtb, but this does not hold for all device cycles that are defined for the pins of this group.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VWFS  -  Verify WaveForm Sets）

```
VWFS? {waveform_set_1},{waveform_set_2},{(pinlist)}
```

returns:

```
VWFS {status}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VWFS  -  Verify WaveForm Sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98864_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：waveform_set_x | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, …
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VWFS  -  Verify WaveForm Sets）

```
VWFS? 1,2,(DATA)
```

This example checks whether waveform sets 1 and 2 are the same for the pins in the group DATA. If they are the same the following string is returned:

```
VWFS 1,(DATA)
```

### WAVE（取自子主题 Timing Setup Commands › List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
WAVE {wvf_set}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
WAVE {specset_id|"multiport_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}, ALLOW_EQ
```

### WAVE?（取自子主题 Timing Setup Commands › List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
WAVE? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {(pinlist)}
```

returns:

```
WAVE {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WAVE  WAVE  -  WAVEform）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98869_3.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? …
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

This example first defines a logical waveform with the index 2 for waveform set 1. The waveform uses the data parameter D11, the fixed action 0, and the complement C11 of D11. Then two physical waveforms are defined for logical waveform 2, which are referenced by the physical waveform DC/DC power units 4 and 5. Waveform 4 drives to 0 at edge d1, to 0 at d3, and to 1 at d4. Waveform 5 drives to 1 at edge d1, to 0 at d3, and to 0 at d4.

### WFDF（取自子主题 Timing Setup Commands › List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
WFDF {wvf_set}, {wfIndex}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### WFDF?（取自子主题 Timing Setup Commands › List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
WFDF? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDF {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98871_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 4 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…
> 表内引用（4 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `WAVE`（raw: `../02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） · `Restrictions for drive edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.02.01_Restrictions_for_drive_edges.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
> WFDF 1,2,N,N,D11,N,N,N,(D0,D2,D2,D3)
```

This example defines a waveform referenced by waveform index 2. The waveform uses the drive data and tri-state parameter 1. Edge number 3 provides the timing for this waveform. The definitions are made for waveform set 1 and for pins D0 to D3.

### WFDS（取自子主题 Timing Setup Commands › List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

```
WFDS {wvf_set}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
WFDS {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### WFDS?（取自子主题 Timing Setup Commands › List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

```
WFDS? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDS {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98872_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 4 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

```
> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)
> WFDS 1,1,,"r4:EE1",(io)
> WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)

> WFDS? 1,ALL,,(@)
< WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)
< WFDS 1,1,,"r4:EE1",(io)
< WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › WFUD -  WaveForm UnDefine）

```
WFUD {wvf_set},{wfIndex},{(pinlist)}
WFUD {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WFUD -  WaveForm UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98875_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WFUD -  WaveForm UnDefine）

```
WFUD 1,2,(D0,D2,D2,D3)
```

This example deletes a logical waveform defined for waveform set 1 and for pins `D0` to `D3`, referenced by waveform index 2.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › WRST -  Waveform ReSeT）

```
WRST {waveform_set}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WRST -  Waveform ReSeT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98876_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WRST -  Waveform ReSeT）

```
WRST 3
```

This example resets all waveform and timing entries for all pins for waveform set 3.

### WSDM（取自子主题 Timing Setup Commands › List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

```
WSDM {waveform_set}, {display_mode}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98877_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum nu…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

```
> WSDM? "spec_1", (port_1)
< WSDM  "spec_1", 0
```

This example queries the display mode of port port_1 in the multiport specification spec_1. The reply shows that it is set to the "classic" display mode.

### WSUS（取自子主题 Timing Setup Commands › List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS {waveform_set}
```

### WSUS?（取自子主题 Timing Setup Commands › List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS?
```

returns:

```
WSUS {waveform_set}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98878_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number. This is the highest number currently allocated to a waveform set or the highest number of a set you want to load. The number…
> 表内引用（1 条，供检索）：`DSCP`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS 3
```

This example sets the number of used waveform sets to 3.

### Example（取自子主题 Equation based timing setup › Structure of an equation based timing setup › Data organization of equation based timing）

The following figure exemplifies the structure of equation based timing by a schematic setup:

 !`Timing Specifications`（raw: `../../../../raw/10596.png`）

### Example（取自子主题 Equation based timing setup › Timing setup master file › Master file format for timing setup）

The following is an example of a timing master file:

```
hp93000,timing_master_file,0.1
# this is a comment
testerfile: demo.tim

EQNSET 1: files/part1.tim
EQNSET 2 [PIN_ALIAS_SET usb_set]: files/eqnset02.tim

WAVETABLE wtbl_1: files/part1.tim
WAVETABLE wtbl_2: files/wtbl_2.tim

MULTIPORT_SPEC "spec_1":files/part1.tim
MULTIPORT_SPEC "spec_2":files/spec_2.tim
DEFINES: files/defines.tim
```

In the assembled level setup file `demo.tim`, the alias set `usb_set` is used in the equation set 2. When `demo.tim` is splitted, the alias set `usb_set` is removed from the generated sub-file `eqnset02.tim` and package pin names are used.

### Example scenario（取自子主题 Using the Timing Setup Tool）

A chip has the following timing relationship between some of its pins:

 !`Timing Relationship in Example Device`（raw: `../../../../raw/17831.png`）

where,

- clkout is an output clock from the device
- data represents a group of data pins
- e1, e2, & e6 are edges at which actions occur
- ref is the reference delay at which the data valid signal is based.
- clkr is identical to ref, and is the first parameter to be measured. Once determined, the value is assigned to ref.
- sp1 is the point at which data is valid. Before it can be determined, ref must be known.
- sp2 is the point at which data becomes invalid. Before it can be determined, ref must be known.
- T is the period.

An equation based timing setup will be used to determine the values for ref, sp1 and sp2.

<!-- 语法节 end -->

## 是什么

**Timing Setup Tool 是 SmarTest 里定义与编辑器件 timing 的那套 GUI**：period、device cycle、
waveform、方程式的 timing set、spec 值，都在这一套窗口里做。它在语料里**不是「一个页面」，
而是以 `02.08.04.34` 为根的一棵树**（该目录下 228 篇）。

**定义文档自己只有一句导语加一份任务清单。** 原文：

> 「This section gives you the information you need to set up the timing for your tested device: background information, interface descriptions, and task related information.」

接着它说明这棵树要覆盖哪些任务：

> 「This section also gives you the basic tools needed to set up equation based timing tests, before going on to describe the use of the Timing Setup tool to perform the following tasks:」

那些任务逐条是（原文是列表，本页逐条引、**没有用省略号接过去**）：

> 「- setting the system period and clock source」

> 「- generating and editing device cycles by:」

> 「- keeping track of the system resources」

> 「- making compatibility checks」

> 「- displaying the pins/pin groups of interest via the Table Format」

> 「- manipulating the Timing Setup window to suit your requirements」

> 「- working with waveform and timing sets」

第二条之下还有三个二级项：`defining device cycles`、`placing edges`、`creating waveforms`。
**这份清单是「本页管什么」的第一手事实**，下面几节按它展开。

这棵树的收尾在哪，定义文档也说了：

> 「The section then ends with a brief discussion of the Timing Setup window (the user interface) so that you obtain an insight into its mechanics.」

**即「窗口本身」是最后一节（`.07`），不是第一节**——这与通常「先讲界面再讲操作」的组织方式相反，
本页照实记录。

### 三层模型：device cycle ← waveform ← action at edge

`.01_Description_of_the_Timing_System` 说 timing 硬件「可以 per-pin 编程」，并用三句话给出全部层级：

> 「- Device cycles are made up of waveforms in test system cycles.」

> 「- Waveforms are made up of actions occurring at edges.」

> 「- Edges are positioned at a delay measured from the start of a test system cycle.」

**自下往上读**：edge 是「距测试系统周期起点的一个 delay」；waveform 是「edge 上发生的 action 的有序序列」；
device cycle 是「测试系统周期里的 waveform」。**没有第四层。**

同篇另一句把「per-pin」钉住：

> 「The figure below shows the block diagram of the timing system hardware. The hardware lets you program the timing on a per-pin basis.」

（那张图是 `21792.png`，alt 是 `Timing System Hardware Overview (per pin)`。**本页没看它**，见「出处」。）

### 两种时序：fixed 与 equation based

`.02_Timing_Setup_Commands` 是这棵树的命令总纲。它先给 timing setup 下定义：

> 「The timing setup for a device defines the waveforms that can be sent to the pins of the DUT during a test, and the possible period lengths, that is, the possible lengths of the tester cycle, which is the time span used for executing one waveform.」

然后分出**两种形态**，并明说哪一种是标准：

> 「The standard timing setup of SmarTest is equation based. This means that you can use variables in the definitions of edge positions and period lengths, which considerably enhances the flexibility of the setup. It is also possible to define a fixed timing where edge positions and period length are defined as constants.」

| | 边沿位置与 period 怎么写 | 怎么进硬件 |
|---|---|---|
| **fixed timing** | 写成**常量** | 「each setup element is defined by calling a firmware command」 |
| **equation based**（标准） | 写成**变量与表达式** | 「the setup elements are part of larger data blocks that are downloaded to the tester as a whole」 |

两句原文逐字：

> 「With fixed timing, each setup element is defined by calling a firmware command. With equation based timing, the setup elements are part of larger data blocks that are downloaded to the tester as a whole.」

**这条分界决定了下游的一切**：fixed timing 是「一条命令一个设置」，
equation based 是「整块下载」——**所以本页后面说的「下载」，单位是块，不是条。**

### 三件构成物，「第三件是连接层」

`.04_Equation_based_timing_setup` 把 equation based 的工作拆成三件：

> 「Defining a timing setup involves the following tasks:」

> 「- Generate a Wavetable.」

> 「- Generate a Timing Equation Set.」

> 「- Generate a Timing Specification, linking the wavetables and timing equations.」

**第三件不产出新数据，它只做「连接」**——把前两件绑在一起。`.02` 把三件的分工说全：

> 「In equation based timing, waveform shapes are defined in a wavetable, and edge positions are defined in an equation set. Wavetable and equation set are brought together in a timing specification. In a multi-port setup, this must be done separately for every involved port.」

三件里能用的语言元素也定了，而且**与 level 侧是同一套**：

> 「These elements have the same definition and syntax as those of level equation.」

（那句之上是 `to set up timing based on equations, you use the following elements:`，元素列的是
`Expressions`、`equation variables`、`spec variables`。）

### ④ 图证（a）：`10596.png` 画出四件正文没写的事

「语法 / 参数」节引了一张图 `10596.png`（alt `Timing Specifications`，出自 `.02.01.02`）。
**它整张画的是「一个 equation based timing 长什么样」，不是截图。本页读了它。**
**图上逐字可见的框与标签**：

| 图上可见 | 在图上的位置 |
|---|---|
| `Equation set 1` | 上下两个蓝框的标题（**两个框同名，见下**） |
| `Spec variables`、`Equations` | 每个蓝框内部的两个子框 |
| `Timing Set 1`、`Timing Set 2` | 第一个蓝框内另两个子框（绿框） |
| `Specification 101`、`Specification 102`、`Specification 103` | 三个红框的标题 |
| `Specset 1`、`Specset 2`、`Specset 3` | 三个红框内各一个子框 |
| `Specification 201` | 第二个方程集引出的红框，内装 `Specset 1` |
| `Wavetable A`、`Wavetable B` | 两个橙框 |

**正文一个字都没写、图给出了的四件事**：

1. **timing set 画在 equation set 的框内部**（`Timing Set 1` / `Timing Set 2` 是蓝框的子框）。
   正文侧的对应证据是 `.06.02` 的代码块（`TIMINGSET` 段写在方程集正文里），**图把它画成了层级**。
2. **一个 equation set 可以挂多条 specification**：图上第一个方程集引出一条括号线，分叉到三个红框。
   **这是「基数」信息**——正文只说第三件任务是 linking，**没说是一条还是多条**。
3. **多条 specification 汇到同一个 wavetable**（`Wavetable A`）。
   即 **wavetable 是被共用的那一层，specification 才是挂 specset 的那一层**。
4. **编号本身是信息**：`101` / `102` / `103` / `201`。本页「语法 / 参数」节里 `BWDF` 的参数表写着
   这个编号的算法（`100 *` equation_set_no `+ ` specset_no），同节那段单端口例子又写
   `It will be identified to the firmware commands by 101`——**图是这两处文字唯一的一幅图形佐证**：
   `101` = 方程集 1 + specset 1，`201` = 方程集 2 + specset 1。

**图里的字在 raw 里 grep 不到**（本页实测 9,398 篇 raw md）：
`Specification 101`、`Specification 102`、`Specification 103`、`Specification 201`、`Wavetable A`、
`Wavetable B`、`Specset 1`、`Specset 2` **均 0 命中**（`Specset` 单独搜有 8 篇命中，**都不是这几个标签**）。
**按 §11.4，这张图构成图证。** 图上另几个字**是搜得到的**（`Spec variables` 8 篇、`Timing Set 1` 11 篇、
`Equation set 1` 5 篇、`Wavetable` 104 篇），**本页不把它们算进图证**。

**图自己的一处不一致，本页照实记、不判**：图上**第二个方程集的标题与第一个同名**（都读作 `Equation set 1`），
而它引出的 specification 是 `Specification 201`——按上面那条 `100 * equation_set_no + specset_no` 的规则，
`201` 该属**方程集 2**。两个说法只能对一个：要么标题漏改，要么编号抄错。
**本页没有依据判哪一个**（**本页倾向「标题漏改」，但这只是猜测，语料里没有一个字支持**）。

**这张图答不了的**：图上没有 specset 的正文、没有任何一条固件命令、没有 period 分辨率、没有 `CHECK`。
**它画的是结构，不是格式。**

### mode context：每个方程集、每个 wavetable 都绑一个

`.05_Mode_context_in_timing_setup` 先定义 mode context，并说明它管多宽：

> 「A mode context specifies, for every defined pin, the type (input or output or both) and operating mode. Every test is associated with a mode context, and every execution of the CONF command applies to exactly one mode context. If you use user defined mode contexts in the pin configuration and timing setup, you must also define the timing for these contexts.」

两条规则**直接约束前面的三件构成物**：

> 「The timing setup specifies mode contexts in the timing equation sets and in the wavetables. That is, every timing equation set and every wavetable is associated with a mode context.」

> 「 Note The specification of a primary timing setup must include a pointer to a timing equation set and to a base wavetable of the same mode context. You cannot define a specification pointing to a wavetable and an equation set of different mode contexts.」

（第二条原文以 ` Note` 起头——**`Note` 前有一个空格、没有另起段**，本页照原样引，见「出处」。）

**继承方向**：`The mode context attribute of the timing equation set (which must be identical to the mode context attribute of the base wavetable) determines the overall mode context of a primary timing setup (timing context) containing that equation set.`
——**primary timing setup 的 context 从 equation set 继承，不是自己写的。**

**默认值与命名**：`If you do not explicitly specify a mode context, the mode context "DEFAULT" is set.`；
自定义时 `Any arbitrary name can be used as a context name (except "DEFAULT").`（例子用的是 `differential`）。

文件里的写法（**两个硬约束：加在两处、必须跟在 `EQNSET` 行之后**）：

> 「The mode context can be specified by keyword MODECONTEXT followed by the context name in quotes. This line must follow the line with the EQNSET keyword and is to be added to the timing equation set and the wavetable.」

多端口时变成三段（`MODECONTEXT` 改跟在 `DEFINES` 行之后）：

```
EQNSET ...
DEFINES ...
MODECONTEXT "..."
...
```

GUI 侧只有**一个显示位**：

> 「The mode context defined in the timing equation set is displayed in the Context field of the Timing Setup editor (see below).」

（`(see below)` 之后那张图是 `56204.png`，alt `Context in the Timing Setup editor`；**本页没看它**。）

### waveform set 与 timing set：两个容器

`.03_Waveform_and_timing_sets` 给的是**容器**：

> 「A waveform set is a logical entity stored in system memory that holds:」

装的东西分两级——**对全部 pin**：`System clock period`、`Default device cycle name`；
**per pin**：device cycle 表里的 device cycle 定义、physical waveform 表里的波形定义、**一到多套 timing set**。
**timing set 自己只装两样**：

> 「- The test system period」

> 「- Edge placement delays for the configured pins」

**注意「stored in system memory」这个措辞**：它说的是 waveform set 存在哪，
**没有说它在文件里是哪一行**——本页的语料里也确实找不到那一行（见「出处」的取材边界）。

### 窗口的三个区

`.07_The_Timing_Setup_Window` 是这棵树的最后一节：

> 「The following sections give a brief description of the Timing Setup Window, which allows you to set up the "Fixed Timing". You will be introduced to the elements of the window that you are likely to use most often.」

> 「The Timing Setup window is shown in the figure below. It consists of three areas:」

> 「- The Global Information area.」

> 「- The Timing Entry area.」

> 「- The Device Cycle Edit Area.」

**⚠️ 这里有一处要紧的措辞张力，本页照实并列、不判**：`.07` 说这个窗口是拿来设 **`Fixed Timing`** 的
（原文给 `Fixed Timing` 加了双引号），而 `.06_Using_the_Timing_Setup_Tool` 说同一套操作是用来
`create equation based timing setup and how to edit the timing settings in the Timing Setup window` 的。
**两篇都在本页的读入范围内，本页判不了哪一句是现行定位**；能确定的是**窗口只有一套**——
`.06` 读到的所有入口（`edit wavetables` / `Edit Equations` / `Edit Specifications` / `period` / `Edge Delay`）
**都在这一个窗口的 `Select` 菜单里**。

`.07.01_The_Global_Information_Area` 把第一区逐个点名：

> 「This is the first area in the window, directly below the pulldown menu bar. The parameters that are displayed, or that you can enter or modify are:」

四个 **entry field**：`WFset #`、`Tset #`、`Def. DevCyc:`、`cycles:`。
**这四个名字是「哪个框」的文档事实**，本页「典型用法」里两次用到。

（`.07` 另外五个子主题是 `The Timing Entry Area`、`The Period Overlay`、`The Edge Delays Overlay`、
`The Cursor and Marker Overlay`、`Device Cycle Edit Area`。**本页一篇没读**——
所以第二、三区的内部布局，本页一个字都没有。）

### ④ 图证（b）：`17831.png` 画的是「谁跟谁对齐」

「语法 / 参数」节最后一段引了这张图（alt `Timing Relationship in Example Device`，出自 `.06`）。
正文对它的说明只有一行 `A chip has the following timing relationship between some of its pins:` 加一份 `where,` 清单。
**清单解释的是「每个量是什么」，图补的是「每个量从哪条线量到哪条线」**：

| 图上画的 | 正文只说了 |
|---|---|
| 三条竖线，自左至右标注 `e1`、`e2`、`e6`；`T (period)` 在最底，**左端是一条更靠左的竖线（周期起点），右端与 `e6` 对齐** | 「e1, e2, & e6 are edges at which actions occur」、「T is the period」 |
| `clkr` 与 `ref` 是**两条等宽的双箭头**，右端都落在 `e1` 那条线上；`clkr` 那条紧贴 `clkout` 的上升沿 | 「clkr is identical to ref」、「ref is the reference delay at which the data valid signal is based」 |
| `clkout` 画成梯形（有上升/下降沿），`data` 画成**一条线加一个矩形** | 「clkout is an output clock from the device」、「data represents a group of data pins」 |
| `sp1` 与 `sp2` 的**左端都落在 `e1` 线上**；`sp1` 的右端落在 `e2` 线上（`e2` 正对矩形的左沿），`sp2` 伸到矩形右沿附近 | 「sp1 is the point at which data is valid」、「sp2 is the point at which data becomes invalid」 |

**三条「从哪量起」是图给的、正文没有的**：`ref`/`clkr` 量的是**周期起点到 `e1`**；
`sp1`/`sp2` 量的是**从 `e1` 起**（不是从周期起点，也不是从彼此）。
**这一条与 `.06.02` 的代码对得上**：那里写 `e5 = ref + sp1 + acc`——`ref + sp1` 正是「先量 ref、再从 ref 量 sp1」。
**本条是（推断），依据是图上的箭头端点 + 那句代码的两个加数。**（图是位图，端点位置是本页肉眼读的。）

**图里的字 grep 不到**：`T (period)` **0 命中**（实测 9,398 篇）。**按这一条，图构成图证。**
但 `clkout`（11 篇）、`sp1`（9 篇）、`sp2`（4 篇）、`clkr`（3 篇）、`ref` **都搜得到**，
**本页不把它们算进图证**。

**⚠️ 图与代码块的一处对不上**：图里中间那条边沿标的是 **`e2`**，
而 `.06.02` 的例子里「数据有效」那个边沿用的是 **`e5`**（`e5 = ref + sp1 + acc`）；
`.06` 的场景段又写 `e1, e2, & e6 are edges at which actions occur`。
**三处里两处说 `e2`、一处写 `e5`**，本页照实并列，**不判哪一个是笔误**。

**图答不了的**：图上没有任何 period 值、没有 pin 名、没有 device cycle 名、没有边的顺序号
——**它是一张几何关系图，不是那份 setup 的实录**。

## 典型用法

**三步是严格的先后，而且文档用「每篇的第一句」把这个顺序串起来了**：

| 步 | 文档 | 第一句（逐字） |
|---|---|---|
| 1 | `.06.01_Setting_up_the_wavetables` | `The first part of defining the timing is setting up the wavetable.` |
| 2 | `.06.02_Defining_the_equation_sets` | `Having setup your wavetables, you must define the equations that will form the backbone of your test.` |
| 3 | `.06.03_Defining_the_spec_sets` | `You are now ready to define a set/sets of values for the variables you have just declared - a SPECSET, or specification set.` |

**第三步用的不是本工具**：`This is done using a dedicated tool - the Spec Tool.`——
但入口还在本窗口（`Select > Edit Specifications`）。

### 一个贯穿全篇的例子

`.06` 交代了它为什么要先给例子：

> 「To simplify the explanation of equation based testing, the following example is used.」

> 「This example demonstrates a realistic application of equation based testing, yet it is very simple.」

场景量（逐条引自 `where,` 清单）：`clkout`（器件的输出时钟）、`data`（一组数据 pin）、
三个边沿 `e1`/`e2`/`e6`、`ref`（数据有效信号的基准延迟）、`clkr`（**先量出来、量到就赋给 `ref`**）、
`sp1`/`sp2`（数据有效/失效点）、`T`（period）。收束句：

> 「An equation based timing setup will be used to determine the values for ref, sp1 and sp2.」

**这句值得单独记**：这个例子的**产物是三个 spec 值，不是波形本身**——
**这正是「equation based」的含义：几何量用方程写，具体值走 spec。**

### 第一步：生成 wavetable（`.06.01`）

| # | 动作 | 原文要点 |
|---|---|---|
| 1 | 打开 Timing Setup 窗口 | |
| 2 | `Select > edit wavetables` | 打开 **Wavetable Editor**：`an ASCII based editor, where you define a format description of the pins - the shapes, window edges, etc.` |
| 3 | 点 `Generate` | NEditor 走 `Shell > Generate`，或按 `F5`；`This creates an ASCII description of your Timing Setup.` |
| 4 | 选 waveform set 与 pin，点 `create` | `By default all pins and waveform sets are selected.` |
| 5 | `Shell > Download` | 下到测试系统 |
| 6 | 有错就查 report window | `If errors are generated in the report window, debug if necessary` |
| 7 | 存 Timing Setup | `as it will now be out of date` |

**两个必须记住的警告**（原文 Note，逐字）：

> 「 Note By default, the wavetable editor displays the last wavetable file you were working on, and has nothing to do with the current Timing Setup. If you did not already have an existing description of your timing, this screen is blank.」

> 「 Note Remember that the wavetable file is a temporary one. If you want to make it available at a later stage, you must either save it from within the wavetable editor (using vi, for example), or save the Timing Setup.」

**「wavetable 文件是临时文件」是这一节的信息量所在**：编辑器里那份 ASCII 文件**不自动留下**；
留它只有两条路——**在编辑器里另存一份**，或者**存整个 Timing Setup**。

### 第二步：定义 equation set（`.06.02`）

`Select > Edit Equations` → 点 `Generate`（`This enables you to get the fixed timing values from the existing setup.`）
→ 再按段写。**period 分辨率默认自动定**：

> 「By default the software automatically determines the best period resolution (for example, for a period of 20.4 ns results in the software selecting 10.2 ns). However, in certain applications - if multiple timing sets do not have the same period - you can force the period to your own value.」

段的顺序与内容（原文代码块，本页逐字抄）：

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

三处要点：

- **timing set 可以用号或名字引用**：`The timing set can be referenced by either a number (1 in the example) or a description (only one used, in the example).`
- **`acc` 是常量变量**：`In equation set 1, acc is defined as a constant variable (it always has the same value for all specsets of that equation set) and represents an accuracy guard band of 0.1 ns`
  ——**`constant` 的确切含义是「对这一方程集的所有 specset 都同值」**（不是「对全器件同值」）。
- **收尾与第一步同款**：`Shell > Download`，`Upon download, the syntax of your description is checked`，
  错误进 report window；**equation 文件同样是临时文件**（Note 与第一步同款）。

### 第三步：定义 spec set（`.06.03`，用 Spec Tool）

入口 `Select > Edit Specifications`。这一节对窗口本身的说明是：

> 「Within this window you define which equation set you are using, which wavetable, which specification set, and the values you are using for each specification set.」

步骤（按原文 Procedure 的顺序）：`Change > Create New Specification` → 选方程集 → `create`
→ **从 `Unused Numbers`（`1 to 99`）里挑号**（`By default the first unused number will be highlighted.`）
→ 填 description（`It might typically be a reference to the speed used in the specification settings; 40MHz std, for example.`）
→ `done` → 选 wavetable（`A specification set must have an associated equation set and wavetable.`）
→ 在底部表里逐个变量填 **Actual / Minimum / Maximum**（`double-click the Actual field` → 回车）
→ 单位列：`If the unit of measurement is specified in the Equation file, the Unit column will already have been filled in, and remains non-editable.`
→ Download → 保存。

**单位冲突的警告框**（原文逐字，含尖括号占位符）：

```
WARNING: Unit for spec variable "<variable>" in EQNSET <no>, SPECSET <no> is not consistent (EQNSET unit: [<unit>], SPECSET unit: [<unit>]).
Only EQNSET units will be used. To overwrite SPECSET units with EQNSET units, press "Download" and then save the setup.
To keep SPECSET units, edit EQNSETs and set the same units as in SPECSETs.
```

**默认方向要记住**：`Only EQNSET units will be used.` ——
**冲突时方程集的单位赢**；想保留 specset 的单位，得回去改方程集。
文档还说明了这种冲突常见于哪：`after importing setups converted by STIL reader with version 2.1 or earlier`。

### 生成一个 device cycle：四步

> 「In order to generate a device cycle you have to go through several discrete steps. You have to:」

> 「- define your device cycle」

> 「- select the necessary edges」

> 「- position the edges」

> 「- create the required waveform」

### 下载：两套机制，一套显式、一套隐式

| 机制 | 原文 |
|---|---|
| **显式** | wavetable 编辑器与 Spec Tool 里的 `Shell > Download`（`.06.01` / `.06.02`）、`File > Download`（`.06.03`） |
| **隐式** | `.06.06.06`：`When you finish creating the waveform, enter it into the firmware by clicking a different device cycle.` |

**隐式那条是本页读到的最反直觉的一句**：**在 Device Cycle 编辑区切换 device cycle 这个动作，
本身就等于把波形写进固件。**下载失败的判据也在同一篇：

> 「If you've used up more resources than are available, the system refuses to download your setup and issues an error message in the report window.」

### 其余常用操作

| 想做什么 | 怎么做 | 出处 |
|---|---|---|
| 设 period | `Select > period` → `Enter the desired period (in ns) into the period entry field.`；允许范围看系统类型 | `.06.05` |
| 新建 waveform set | 往 `WFset #` 里填号；`Tset #` 自动显示 `1`，**Device Cycle 编辑区被清空** | `.06.11.01` |
| 新建 timing set | 往 `Tset #` 里填号；`The system copies the timing to the new timing set.` | `.06.11.01` |
| 改边沿 | 拖动边沿；或 `Select > Edge Delay` | `.06.03` |
| 看方程与 spec 结果 | `File > Show Eqns & spec Results` | `.06.03` |
| 做检查 | `The system has several features that let you check whether your new timing and tests that you've put together will actually be capable of executing.` | `.06.12` |
| 拆/合多个文件 | 见 [[timing-master-file]]（`.04` 的子主题；**本页没读**） | `.04.05` |

**两点硬规矩**（`.06.11.01` 的 Note，逐字）：

> 「 Note Remember, you can change the period and edge delays from one timing set to another, not the waveforms or the edge order. If you change a waveform in one timing set (assign a different shape), or swap a pair of edges round, the change affects all the other timing sets within their waveform set.」

**即：timing set 之间可改的只有 period 与边沿延迟；波形与边沿顺序是 waveform set 级共享的。**

period 改小的后果（`.06.05` 的 Note，逐字）：

> 「 Note If you have already set up some timing settings and subsequently changed the period to a smaller value, SmarTest may automatically correct the existing settings. In this case SmarTest displays a message in the report window.」

### 入口一览

`Select` 菜单上的五条路径，是本页读到的**全部** GUI 入口：
`edit wavetables`（第一步）、`Edit Equations`（第二步）、`Edit Specifications`（第三步）、
`period`（设 period）、`Edge Delay`（改边沿）。**五条都在 Timing Setup 窗口里。**
另外两条不在 `Select` 里的：wavetable 编辑器的 `Shell > Generate` / `Shell > Download`，
Spec Tool 的 `Change > Create New Specification` 与 `File > Download`。

## 和谁有关

- [[spec-tool]] —— **下游：第三步的执行者**。`Select > Edit Specifications` 打开的就是它；
  spec 值、单位、Actual/Minimum/Maximum 都在那边编辑。**本页只写「从哪进、进去干什么」。**
- [[wavetable]] / [[wavetable-file]] —— **第一步的产物**。本页只写了编辑器里的动作与那条
  「临时文件」警告；wavetable 的部件结构与文件格式**不在这两页**。
- [[timing-equation-set]] —— **第二步的产物**。`SPECS` / `TIMINGSET` / `PINS` / `EQUATIONS`
  四段的语义与语法不在本页（本页只抄了 `.06.02` 的示例）。
- [[timing-specification]] —— **第三件构成物，也就是「连接层」**。
  本页的图证（a）补的是它的**基数**：**一个方程集可以挂多条 specification**。
- [[timing-file]] —— **三块数据的落点**。本页提到的 `wavetable file` / `equation file` /
  `timing specification file` 三种叫法指向哪个文件，在那一页；本页只写了「它们是临时文件」。
- [[timing-master-file]] —— **`.04` 声明的一个子主题**，管「把一个 setup 拆成多个文件」。
  **本页没读那一篇**，所以 master file 的格式本页一个字没有。
- [[waveform-set]] —— **容器**。`A waveform set is a logical entity stored in system memory`；
  timing set 是它的一部分。**关系是「整体—部分」，不是「两者并列」。**
- [[spec-set]] —— **第三步产出的东西**。本页只写「怎么建、编号从哪挑、值填在哪三列」，
  spec set 在文件里的形态在那一页。
- [[test-program-explorer]] —— **保存落点**。三篇 Procedure 的收尾都写「在 Test Program Explorer 里保存 Timing Setup」，
  而 `.06.01` 的警告说**不保存 Timing Setup 就等于丢掉那份临时文件**——
  **所以这一页与本页是「产物—落点」的关系，不是「同类工具」。**
- [[mapping-timing]] —— **同阶段的对照表**。它把本页填在 GUI 列的若干格里
  （wavetable 编辑器、`Context` 字段、`WFset #` / `Tset #`、`Select > period`）。
  **本页与它一致**；它另把 [[timing-diagram-tool]]（结果侧目视核对）与 [[setup-management-tool]]（拆合文件）
  放在同一阶段，**这两篇本页都没读**。
- [[level-setup-tool]] —— **同源（level 侧的对照）**。文档明说 equation based 的元素
  `have the same definition and syntax as those of level equation`，`.06.03` 的 Related information
  也直接链到 `Equation based level setup`（raw: `02.08.04.14.02_Equation_based_level_setup.md`）。
  **本页没读 level 侧那几篇**——所以这只是「语法同源」这一句文档事实，不是本页的类比。
- [[smartest-6.3.2]] —— **版本那一节的哨兵值**（见下）。

**文档自己链出去、但不在 `extract/prose-allowlist.txt` 里的三篇**（按规矩用反引号 + raw 路径）：

- `Waveform Editor`（raw: `02.08.04.26.02.05.05.01.01_Waveform_Editor.md`）与
  `Editing Device Cycles and Waveforms`（raw: `02.08.04.34.06.07_Editing_Device_Cycles_and_Waveforms.md`）
  —— 出现在 `.03` 的 `## Related information` 里。**是另一个编辑器**，本页没读。
- `How to set up a multiport timing specification`（raw: `02.08.04.30.02.16_How_to_set_up_a_multiport_timing_specification.md`）
  —— **定义文档唯一的 `## Related information` 目标**。本页没读它，所以多端口的做法本页只有
  `.02` 与 `.05` 里那两句原则（「每个 port 分开做」「`MODECONTEXT` 跟在 `DEFINES` 之后」）。

## 版本

**定义文档 `02.08.04.34_Timing_Setup_Tool.md` 没有 `## Functional changes` 段**——
这是事实，不是缺陷：它以一句 `## Related information` 收尾。

它声明的七个子主题里**六篇有该段，且六篇的条目逐字相同**：

- `- Introduced before SmarTest 6.3.2`

**本页读到的十八篇里，有该段的共十篇**——`.01` 到 `.06` 这六篇，加上 `.06.01`、`.06.02`、`.06.03`、`.06.05`
——**十条逐字相同，全是上面那一句**。**另外八篇没有这一段**：定义文档本身、`.07`、
`.06.06`、`.06.06.06`、`.06.11`、`.06.11.01`、`.06.12`、`.07.01`。

**⚠️ 这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 Timing Setup Tool」。**
它的意思是**在本文档集覆盖范围开始之前就已经有了**。照字面读会造出一条格式齐整的假信息。
参见 [[smartest-6.3.2]]。

**所以本页能说的只有一句**：**Timing Setup Tool 在这套文档覆盖的版本上存在，
而且它的出现早于该范围；具体哪个版本引入，语料没说。**

## 出处

`sources:` **一篇**：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34_Timing_Setup_Tool.md`
（TDC `17774.htm`，**2.3 KB / 43 行**）。**整篇读完**。
它全部内容是：一句导语、七条 `Subtopics`、一段任务清单、一句 `## Related information`、frontmatter、
以及一句收尾说明。**它没有 `## Functional changes` 段，没有一个字的操作正文，也没有一张图**
（实测该篇对 `raw/` 的引用 **0 处**）。

**为什么另外读了十七篇**：定义文档是「节总览」，机制全在它声明的子主题里。本页读的是——

- **它 `## Subtopics` 声明的七篇，一篇不落**：`.01`、`.02`、`.03`、`.04`、`.05`、`.06`、`.07`；
- **其中两篇再往下一层、与本页主题直接相关的十篇**：`.06.01`、`.06.02`、`.06.03`、`.06.05`、
  `.06.06`、`.06.06.06`、`.06.11`、`.06.11.01`、`.06.12`、`.07.01`。

**这十七篇全部读的是 raw 原文**（`Read` 工具或 `cat` 直接打开），**没有一篇是只看 `context` 字段得来的**。
**没有读这棵树以外的任何文档**：`02.06` / `02.07` / `02.09` / `01_Getting_started` **一篇没读**。

**本页的「语法 / 参数」节有 11.1 万字符，其中绝大部分是 `02.08.04.34.02.02_List_of_timing_setup_commands`
之下的命令参数表。本页正文一个字都没有复述它们**——那是命令侧的活。

**看了两张图**，就是本页「语法 / 参数」节里出现的两张，**逐张整张看完，并把小字放大核过**：

- `10596.png`（`F:\master-dev\dorm-wsl-sytest\tdc-html\raw\10596.png`，alt `Timing Specifications`）
  —— 结论见「是什么」④ 图证（a）。**它是本页唯一一张画出「结构基数」的图。**
- `17831.png`（同目录，alt `Timing Relationship in Example Device`）—— 见「是什么」④ 图证（b）。

两张图上的字**逐条回 9,398 篇 raw md 里查过 grep 命中**；本页凡写「grep 不到」的都是实测 0 命中，
凡写「搜得到」的都给了篇数。

**本页没做的**：

- **没有读命令页。** `02.08.04.34.02.02_List_of_timing_setup_commands` 之下四十余篇
  （`APRM` / `EQSP` / `EQFS` / `WSUS` / `TSUS` / `SPST` / `UPTD` / `SVLR` 等）**一篇没读**，
  虽然它们全躺在「语法 / 参数」节里。**所以本页一个命令参数、一条语法都没有。**
- **没有读 `.01` 之下的三篇**（`Timing edges`、`Waveforms`、`Device Cycles`）、`.03.01` / `.03.02`、
  `.04.01` / `.04.02` / `.04.03` / `.04.04` / `.04.05`（含 master file 两篇）、`.06.04`（复杂 device cycle 方法论）、
  `.06.07` 到 `.06.10`、`.06.11.02`、`.06.12.01` / `.06.12.02`、`.07.02` 到 `.07.06`，以及它们之下更深的一层。
  **「检查」那一族的实际检查项（边沿顺序、周期检查、波形集合容性）本页因此一个字没有**，
  只抄了 `.06.12` 的一句总述。
- **窗口的第二、三区本页一个字没有**：只读了 `.07` 的总述与 `.07.01`（Global Information area），
  三个 overlay 与 Device Cycle 编辑区的四篇没读。
- **这棵树里还有别的图，本页没看。** 只读了「语法 / 参数」节里出现的那两张。同树里另有
  `21792.png`（timing 硬件框图）、`17845.png`（`Timing Setup Components`）、`56199` / `56203` / `56204`
  （mode context 三张）、`21811.png`（窗口全图）、`21812.png`（Global Information area），
  以及 `.06.*` 里的十几张对话框与编辑器截图。**这份未看清单里，`17845.png`（组件图）与
  `56203.png`（据 [[mapping-timing]] 是该树里唯一画出文件内容的一张）最值得下一次补看**——
  本页的结论不依赖它们，但「equation set / specset / wavetable 三者的**文件侧**长什么样」这一层，
  本页因此只到了图证（a）的粒度。
- **没有实跑**：没有开过 Timing Setup 窗口、没有 `Generate` 过 wavetable、没有 `Download` 过、
  没有改过 period、没有建过 spec set。`verified: doc-only` 指的就是这件事。
- **写这页时没有动 `wiki/index.md`、也没有把本页挂进 `wiki/stages/timing.md`**；**两者已由本批收尾统一挂入**（`index.md` 的对应条目、`stages/timing.md`）。（**2026-09-20 更正**：原文写「没有挂进」——**收尾动作之后它不成立了**。）
- **没有跑 `verify_stages.py`**。

**§10 的重复投放，本页遇到六处**（判据：frontmatter 的 `source_topic` 去掉 `_N` 后相同）：

| 本页读的 | 同一 TDC 页的另一个投放 |
|---|---|
| `02.08.04.34.02_Timing_Setup_Commands` | `02.06_Command_Reference/02.06.06_Timing_Setup_Commands.md` |
| `02.08.04.34.03_Waveform_and_timing_sets` | `01_Getting_started/01.07.01.04_Waveform_and_timing_sets.md` |
| `02.08.04.34.04_Equation_based_timing_setup` | `01_Getting_started/01.07.01.04.01_Equation_based_timing_setup.md` |
| `02.08.04.34.06.01_Setting_up_the_wavetables` | `01_Getting_started/01.07.01.04.02_Setting_up_the_wavetables.md` |
| `02.08.04.34.06.02_Defining_the_equation_sets` | `01_Getting_started/01.07.01.04.03_Defining_the_equation_sets.md` |
| `02.08.04.34.06.03_Defining_the_spec_sets` | `01_Getting_started/01.07.01.04.04_Defining_the_spec_sets.md` |

**这六处不是「两处独立证据」，是同一篇文档挂了两个章号**（§10 第 0 条），本页按一篇用。
**尤其要注意「三步流水线」那三篇：它们同时是 Getting Started 的入门教程**——
「第一步 / 第二步 / 第三步」这个顺序不是本页拼的，是那三篇自己的第一句给的（见「典型用法」开头的表）。
**引文的逐字性不受影响**（同一 TDC 页的副本内容相同）。

**⚠️ 语料瑕疵，本页一处都没替它改（§11.2）**：

- **`.06.03`：`On the Spec Tool click the Downloadbutton.`** —— `Download` 与 `button` 之间**缺一个空格**。
  （本页读到的 `01.07.01.04.04` 副本里这一句逐字相同。）
- **`.06.03`：`Repeat step 7 to 11 until all variables have been set up appropriately.`** ——
  该篇的步骤是**不带编号的圆点列表**，**文里没有 7 到 11 号步骤**。
- **`.06.03`：`for each testing speed. for example), and click done when satisfied with your setup.`**
  （本页只摘中间这一小段，**两端没有加省略号**）—— 句号之后的 `for` 是小写，本该另起一句。
- **`.06.03`：`The final part of defining the SPECSET, is giving values`** ——
  `SPECSET` 与 `is` 之间多一个逗号。
- **`.06.03`：`double-click the Actual field to the right it and key in an initial value`** ——
  `to the right it` 读不通（缺 `of`）。
- **`.06.02`：`Having setup your wavetables, you must define the equations that will form the backbone of your test.`** —— `setup` 当动词用（同篇别处用 `Setting up`）。**本页照原样引。**
- **`.04`：小标题 `## Elements of the equations based timing setup` 之后第一句以小写开头**：
  `to set up timing based on equations, you use the following elements:`。
- **`.05` 的小标题 `## Mode context "DEFAULT"` 与 `.05` 正文的引号写法不一致**：
  标题里 `DEFAULT` 带双引号，正文 `If you do not explicitly specify a mode context, the mode context "DEFAULT" is set.`
  也带；而下一小节标题写 `## User defined mode context`（无引号）——**同一篇内引号用法不统一**。
- **六篇的 `Note` 前面多一个空格、且没有另起段**：`.05`、`.06.01`、`.06.02`、`.06.03`、`.06.05`、`.06.11.01`
  各一处（形如 ` Note ...`）。**本页引它们时一律照原样带那个空格。**
- **`.06.01` 里两次给 NEditor 的指令不一样**：先写
  `(In case you use the NEditor, you find the bottom line commands in the Shell menu.)`，后写
  `(In case you use the NEditor, open the Shell menu and click Generate. Alternatively you may press the F5 key.)`
  —— **同一篇、同一个软件，两处说法不同**。

**本页检查过、但本页的十八篇里没有遇到的瑕疵**（照 spec-tool 那一页的写法，把「查过没有」也记上）：

- **§11.2 ① 的编码坏字**：`碌` / `渭` / `卤` / `惟` / `鈥` 一族**实测 0 处**。
  检测方法在别的篇上是能命中的——[[mapping-timing]] 记的 `can be up to 卤 6ns` 就在同章的
  `02.08.04.34.03.02_Implications_when_running_tests`，**那一篇本页没读**。
- **§11.2 ⑤ 的整词替换**：`DC/DC power units`（被替换坏的 `Index`）**实测 0 处**。
  **本页因此没有需要避开的坏标识符，代码块里也没有。**

**与 [[spec-tool]] 的两处措辞差异，本页照实并列、不替任何一方改（§10）**：

- **同一个菜单路径归属哪个窗口**：本页读的 `.06.03` 说入口在 **Timing Setup 窗口**
  （`in the Timing Setup window, click the menu Select > Edit Specifications.`），
  而 [[spec-tool]] 那一页记的是 **Level Setup tool**（`In the Level Setup tool, select the menu item Select > Edit Specifications.`）。
  **两处说的是同一个菜单路径、同一句措辞的下半截。本页判不了是哪一个窗口，也不改它。**
- **Download 的形态**：本页读的 `.06.03` 里**两种写法同时存在**——
  `On the Spec Tool click the Downloadbutton.`（图标）与
  `click Download from within the File pulldown menu`（菜单路径）。
  [[spec-tool]] 那一页读到的那一篇只有前一种形态，**所以它把同阶段那张对照表 `mapping-level` 里的
  `File > Download` 判成「待查」**。**本页的语料里菜单路径那种写法是有的，就在 `.06.03` 收尾那一步。**
  —— **这可能是那一页那个待办的一半答案；本页只报事实，不下结论。**

**本页不动 `layer: gui` 的理由**：Timing Setup Tool 是 GUI 侧的工具，它的入口、字段、菜单都在窗口上
（§6 的六值枚举里 `gui` 就是这一层）。**本页没有替它改 `stage: timing`**。

`verified: doc-only`
