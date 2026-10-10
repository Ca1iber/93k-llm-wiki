---
type: concept
title: Timing Setup Commands
layer: n/a
stage: timing
tags: [timing, command, firmware, waveform, wavetable, equation, multiport]
related: [timing, timing-specification, timing-equation-set, wavetable, waveform-set, timing-file, timing-master-file, timing-setup-tool, timing-set-selector, command-reference, pattern]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Timing Setup Commands

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **49,402 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.md>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.03.01_Defining_waveform_shapes_for_Pin_Scale_standard_pins.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.06.01_Avoiding_rounding_problems_with_the_fract___function.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.06.02_Avoiding_rounding_problems_with_different_clock_groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.01_APRM_-__Activate_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.02_BWDF__BWDF__-__Break_Waveform_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.03_BWDS__BWDS__-__Break_Waveform_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.04_CDCP__-__Cycle_Device_Cycle_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.05_CLKR__CLKR__-__CLocK_Resolution.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.06_DCDT__DCDT__-__Device_Cycle_DefaulT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.07_DCUD_-__Device_Cycle_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.08_DFCR__DFCR__-__DeFine_Clock_Routing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.09_DPRT__DPRT__-__Default_PRimary_Timing_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.10_DSCP__DSCP__-__Define_System_Control_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.11_EDDC__-__EDge_in_Device_Cycle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.12_EDSP__EDSP__-__EDge_SPecification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.13_EQFS_-__EQuation_FileS_command_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.14_EQSP__EQSP__-__EQuation_SPecification_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.15_ETDS__ETDS__-__Edge_Timing_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.16_ETIM__ETIM__-__Edge_TIMing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.17_EUDS__-__Edge_Usage_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.18_EVCK__-__EVent_ClocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.19_FTCG__FTCG__-__Functional_Test_ConfiGure.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.20_PCLK__PCLK__-__Pin_CLocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.21_PDIV__-__Period_DIVider.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.22_RCLK__-__Reference_CLocK_source.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.23_RSET_-__ReSET.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.24_SCLK__-__System_CLocK_query.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.25_SDSC__-__Set_number_DeSCriptions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.26_SPCP__-__SPeCification_Port_list.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.27_SPEC__-__SPECification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.28_SPRM__SPRM__-__Set_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.29_SPST__-__SPecset_STatus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.30_STRS__-__Spec_TRansition_Search.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.32_TSUS__TSUS__-__Timing_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.33_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.34_UPTD__UPTD__-__UP_To_Date.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.35_VCLK__-__Verify_CLocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.36_VDCG__-__Verify_Device_Cycle_for_Group.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.37_VTIM__-__Verify_TIMing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.38_VWFG__-__Verify_WaveForms_in_Groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.39_VWFS__-__Verify_WaveForm_Sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.40_WAVE__WAVE__-__WAVEform.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.41_WFDF__WFDF__-__WaveForm_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.42_WFDS__WFDS__-__WaveForm_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.43_WFUD_-__WaveForm_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.44_WRST_-__Waveform_ReSeT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.45_WSDM__WSDM__-__Waveform_Set_Display_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.46_WSUS__WSUS__-__Waveform_Sets_USed.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Concepts of timing setup › Data organization of equation based timing）

The following figure exemplifies the structure of equation based timing by a schematic setup:

 !`Timing Specifications`（raw: `../../../../raw/10596.png`）

### Example（取自子主题 Concepts of timing setup › Defining waveform shapes › Defining waveform shapes for Pin Scale standard pins）

```
WAVETBL "std"

PINS IN1
0  "d1:0"  ZERO
1  "d1:0 d2:1 d3:0"  ONE

PINS O1
0  "r1:L"   LOW
1  "r1:H"   HIGH
```

ZERO and ONE are the names for the waveforms 0 and 1 for pin `IN1`. These names will be displayed by the Pattern Debug tool.

### Example（取自子主题 Concepts of timing setup › Defining waveform shapes › Defining waveform shapes for Smart Scale pins）

The following example shows a wavetable fragment for a Smart Scale pin in its native format:

```
WAVETBL "wavetable 1"

PINS  DS0
  0 "10" "0."    110
  1 "101" "0.."  101

PINS DS1
  0 "0"  "0"     0

PINS  Q0
  0 "XXL"   "..." XXL
  1 "HLH"   "..." HLH
  2 "XLH"   "..." XLH
  3 "H.H"   "10." HCMP

PINS  IO1
TTMODE X4
  0 "...." "...." "LHLH"     LHLH
  1 "...." "...." "XLXH"     XLXH
  2 "0110" "0..." "XXXX"     0110
```

The dots stand for "no action".

If you retrieve these definitions with WFDS?, the reply will look as follows:

```
> wfds? 101,all,,(DS0)
< WFDS 101,0,,"f1:1 f2:0 s1:0",(DS0)
< WFDS 101,1,,"f1:1 f2:0 f3:1 s1:0",(DS0)

> wfds? 101,all,,(DS1)
< WFDS 101,0,,"f1:0 s1:0",(DS1)

> wfds? 101,all,,(Q0)
< WFDS 101,0,,"r1:EX r2:EX r3:E0",(Q0)
< WFDS 101,1,,"r1:E1 r2:E0 r3:E1",(Q0)
< WFDS 101,2,,"r1:EX r2:E0 r3:E1",(Q0)
< WFDS 101,3,,"r1:W1 r2:WC r3:E1",(Q0)

> wfds? 101,all,,(IO1)
< WFDS 101,0,,"r1:E0 r2:E1 r3:E0 r4:E1",(IO1)
< WFDS 101,1,,"r1:EX r2:E0 r3:EX r4:E1",(IO1)
< WFDS 101,2,,"f1:0 f2:1 f3:1 f4:0 s1:0 r1:EX r2:EX r3:EX r4:EX",(IO1)
```

Note that waveform 3 for pin `Q0` contains a window compare. Note also that the waveforms are returned in the modified standard format although they are coded in the pure Smart Scale format in the wavetable.

### Example（取自子主题 Concepts of timing setup › Defining the timing specification）

The following is a simple example of a `single-port timing specification`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.34.04.01_Single-port_timing_setup.md`）:

```
EQNSET 1 "default"

WAVETBL "table1"
CHECK all

SPECSET 1 "sp1"

# SPECNAME *****ACTUAL***** *****MINIMUM**** *****MAXIMUM**** UNITS COMMENT
f          100                                                [MHz]
```

This specification uses spec set 1 for equation set 1. It will be identified to the firmware commands by 101. The base variable f is set to 100. The `CHECK all statement`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.34.04.03.05.01_CHECK_Statement_Options.md`） activates all consistency checks (see `Consistency checks for edge delays`（raw: `02.06.06.01.05.01_Consistency_checks_for_edge_delays.md`）).

### Example（取自子主题 Concepts of timing setup › Dealing with rounding problems in multiport setups › Avoiding rounding problems with the fract   function）

See `Usage of the fract() function`（raw: `02.06.06.01.06.01.02_Usage_of_the_fract___function.md`）.

### Example 1（取自子主题 Concepts of timing setup › Dealing with rounding problems in multiport setups › Avoiding rounding problems with different clock groups）

We first show the results for a pure Smart Scale setup. In this case the clock resolutions (third parameter of CLKR) are as follows:

```
>  CLKR? EXACT,"mu_burst",(@@)
<  CLKR "mu_burst",12,1.5,(PortA)
<  CLKR "mu_burst",17,1.7,(PortB)
<  CLKR "mu_burst",20,1.25,(PortD)
<  CLKR "mu_burst",7.8,1.56,(PortE)
```

If no user defined clock groups exist, the result for the SCLK and EVCK periods is:

```
>  sclk? "mu_burst"
<  SCLK "mu_burst",13260
>  evck? "mu_burst",(@@)
<  EVCK "mu_burst",13260,(PortA)
<  EVCK "mu_burst",13260,(PortB)
<  EVCK "mu_burst",13260,(PortD)
<  EVCK "mu_burst",13260,(PortE)
```

SCLK? returns the SCLK period, EVCK? returns the EVCK periods. The SCLK period is rather large because it must be directly divisible by the clock resolutions of all 4 ports.

If `PortA` is in clock group "g1", and the other ports in the default clock group, one gets:

```
>  sclk? "mu_burst"
<  SCLK "mu_burst",480
>  evck? "mu_burst",(@@)
<  EVCK "mu_burst",480,(PortA)
<  EVCK "mu_burst",13260,(PortB)
<  EVCK "mu_burst",13260,(PortD)
<  EVCK "mu_burst",13260,(PortE)
```

The SCLK period is now at its minimal value (for the big testhead) because the SCLK period is no longer required to be directly divisible by any of the clock resolutions. Furthermore, this case shows, by the example of "g1", that if the SCLK period is directly divisible by the clock resolutions of all ports within a clock group, the SCLK period is taken as its EVCK period.

If both `PortA` and `PortB` are in clock group "g1", and `PortD` and `PortE` in the default clock group, one gets:

```
>  sclk? "mu_burst"
<  SCLK "mu_burst",480
>  evck? "mu_burst",(@@)
<  EVCK "mu_burst",2448,(PortA)
<  EVCK "mu_burst",2448,(PortB)
<  EVCK "mu_burst",3120,(PortD)
<  EVCK "mu_burst",3120,(PortE)
```

This example demonstrates how an appropriate grouping of the ports within the clock groups can make the test faster. By putting both `PortA` and `PortB` into the user defined clock group "g1" the maximal event clock period is 4 times smaller than in the previous setup. The disadvantage is that `PortB` is no longer synchronized with `PortD` and `PortE.`

### Syntax（取自子主题 List of timing setup commands › APRM -  Activate PRiMary sets）

```
APRM {mode}
```

### Parameters（取自子主题 List of timing setup commands › APRM -  Activate PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98485_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：mode | Selects the activation mode:

### Example（取自子主题 List of timing setup commands › APRM -  Activate PRiMary sets）

```
APRM CNL
```

### BWDF（取自子主题 List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### BWDF?（取自子主题 List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF? {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {(pinlist)}
```

returns:

```
BWDF {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### Parameters（取自子主题 List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98497_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number …
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

This example defines a pulse for waveform set 1, and for pins D0 to D3, driving to 1 at edge action 4 and to 0 at edge action 5. The tri-state formatter is not used.

### BWDS（取自子主题 List of timing setup commands › BWDS  BWDS  -  Break Waveform Definition String）

```
BWDS {wvf_set}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

### BWDS?（取自子主题 List of timing setup commands › BWDS  BWDS  -  Break Waveform Definition String）

```
BWDS? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {(pinlist)}
```

returns:

```
BWDS {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98498_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. Enter PRM for the Primary waveform set. The maximum number is determined by…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `WFDS, WFDS? - (WaveForm Definition String)`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）

### Example（取自子主题 List of timing setup commands › BWDS  BWDS  -  Break Waveform Definition String）

```
> BWDS? 1,,,(@)
< BWDS 1,,,"",(io)
< BWDS 1,,,"d1:F00 d5:F10",(clk)
```

### Syntax（取自子主题 List of timing setup commands › CDCP  -  Cycle Device Cycle Parameter）

```
CDCP? {start_cycle}, {no_of_cycles}, {strt_disp}, {disp_length}, {(pinlist)}
```

returns:

```
CDCP {cycle}, {dev_cyc_name}, {dev_cyc_len}, {DD1}, {DD2}, {ED1}, {ED2}, {(pinlist)}
```

### Parameters（取自子主题 List of timing setup commands › CDCP  -  Cycle Device Cycle Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98499_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle to be analyzed. The range of values for this parameter depends on the analysis mode: In the Start …

### Example（取自子主题 List of timing setup commands › CDCP  -  Cycle Device Cycle Parameter）

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

### CLKR（取自子主题 List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res}
```

### CLKR?（取自子主题 List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

```
CLKR?[type,] {waveform_set|specset_id|"multi-port_spec"}
```

returns:

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res|clock_res}
```

### Parameters（取自子主题 List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98504_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `Automatic calculation of period resolution for single-port setups`（raw: `02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md`）

### Example（取自子主题 List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

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

### DCDT（取自子主题 List of timing setup commands › DCDT  DCDT  -  Device Cycle DefaulT）

```
DCDT {waveform_set}, {"default_name"}
```

### Example（取自子主题 List of timing setup commands › DCDT  DCDT  -  Device Cycle DefaulT）

```
DCDT 1,"HOLD"
```

This example defines the default device cycle name HOLD for Waveform Set 1.

```
DCDT? "fast_ARM",(ARMPort)
DCDT "fast_ARM","Cycle",(ARMPort)
```

This example queries the default device cycle name for the ARMPort port in the multi-port specification fast_ARM.

### Syntax（取自子主题 List of timing setup commands › DCUD -  Device Cycle UnDefine）

```
DCUD {waveform_set},{"dev_cyc_name"},{(pinlist)}
```

### Parameters（取自子主题 List of timing setup commands › DCUD -  Device Cycle UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98529_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 List of timing setup commands › DCUD -  Device Cycle UnDefine）

```
DCUD 1,"WRITE"
```

This example deletes the device cycle `WRITE` for waveform set 1 from the device cycle table.

### DFCR（取自子主题 List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

```
DFCR {source_group},{dest_group}
```

### DFCR?（取自子主题 List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

```
DFCR?
```

returns (for every group except G4):

```
DFCR {source_group},{dest_group}
```

### Parameters（取自子主题 List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98541_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：source_group | specifies the hardware group whose local clock is to be routed to dest_group. The format is Gx, where x is the group number.

### Example（取自子主题 List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

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

### DPRT（取自子主题 List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

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

### DPRT?（取自子主题 List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

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

### Parameters（取自子主题 List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98570_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number.
> 表内引用（1 条，供检索）：`TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

### Example（取自子主题 List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT?
```

returns:

```
DPRT 3,4
```

On sending a query the system reports that the default primary waveform set is 3 and the default primary timing set is 4.

### DSCP（取自子主题 List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP `[device_cycle`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_device_cycle`）], `[waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）], `[timing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_timing_set`）], `[level_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_level_set`）], `[dps_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_dps_set`）], `[pmu_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_pmu_set`）],
                        `[devicecycle_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_devicecycle_set`）], `[routing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_routing_set`）], `[period_res_prec`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_period_res_prec`）],

```

### DSCP?（取自子主题 List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP?
```

returns:

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
       {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
       [period_res_compatibility_model]
```

### Parameters（取自子主题 List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98578_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：device_cycle | The device_cycle parameter is an integer that defines the absolute maximum number of device cycles that you can create for one pin.Default: 256Ma…
> 表内引用（2 条，供检索）：`waveform sets and wavetables`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） · `waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）

### Example（取自子主题 List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

### Syntax（取自子主题 List of timing setup commands › EDDC  -  EDge in Device Cycle）

```
EDDC? [waveform_set], [timing_set], {edge_spec},
[dev_cyc_name], [dc_ref], [direction], {(pinlist)}
```

returns:

```
EDDC {edge_number}, {dev_cyc_name}, [reuse_flag], {(pinlist)}
```

### EDSP（取自子主题 List of timing setup commands › EDSP  EDSP  -  EDge SPecification）

The edge_spec parameter specifies a physical edge (d1 through d8 or r1 through r8):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}
```

The edge_spec parameter is a data parameter (D1, D2, C1, C2, E1, or E2):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}
```

### EDSP?（取自子主题 List of timing setup commands › EDSP  EDSP  -  EDge SPecification）

```
EDSP? [dc_ref], {(pinlist)}
```

returns:

```
EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98589_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set | Specifies a waveform set number for a fixed timing setup.

### Syntax（取自子主题 List of timing setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]
```

### Parameters（取自子主题 List of timing setup commands › EQFS -  EQuation FileS command transfer）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98592_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification to use:

### Example（取自子主题 List of timing setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

This example loads the level equation file from /tmp/level_equation.

### EQSP（取自子主题 List of timing setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP {spec_type}, {part}, {#spec(data)}
```

### EQSP?（取自子主题 List of timing setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP?{spec_type}, {part}
```

returns:

```
EQSP {spec_type}, {part}, {#spec(data)}
```

if these are not empty, for backward compatibility.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98593_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：spec_type | The mandatory parameter defines which specification type to use. Use: LEV to specify levels TIM to specify timing

### Example（取自子主题 List of timing setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

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

### ETDS（取自子主题 List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### ETDS?（取自子主题 List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

ETDS? {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {(pinlist)}

returns:

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### Parameters（取自子主题 List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98599_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `Defining waveforms for Pin Scale 9G pins`（raw: `02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`） · `Selecting and ordering edges`（raw: `02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）

### Example 1（取自子主题 List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

```
> ETDS 1,1,,"e1:0 e2:2 e3:6 e4:4",(io)
> ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
> ETDS? 1,1,,(@)
< ETDS 1,1,,"d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4",(io)
< ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
```

### Example 2（取自子主题 List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

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

### Example 3（取自子主题 List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

This example shows how to set and retrieve a delay of a multi-port specification:

```
> ETDS? "mu_timing",2,,(In1)
< ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ETDS "mu_timing",2,,"d1:0.5",(In1)
> ETDS? "mu_timing",2,,(In1)
< ETDS "mu_timing",2,,"d1:0.5",(In1)
```

The specification name and the pin name identify the port (no pin may occur in more than one port within the same specification). Then the port and the specification identify the equation set.

### ETIM（取自子主题 List of timing setup commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

### ETIM?（取自子主题 List of timing setup commands › ETIM  ETIM  -  Edge TIMing）

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
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98600_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `ETIM, ETIM? - (Edge TIMing)`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）

### Example（取自子主题 List of timing setup commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM 1,1,2,4,8,6,10,,(DATA)
```

This example sets the edge delays for the pin group DATA specified for waveform set 1 and timing set 1. Edges 1 to 5 are set to 2,4,8,6 and 10 ns respectively, edge 6 is unused. If no previous setting for edge 6 exists in waveform set 1 and timing set 1, then its delay remains at 0.0 ns.

### Syntax（取自子主题 List of timing setup commands › EUDS  -  Edge Usage Definition String）

```
EUDS? {waveform_set}, [mode], {(pinlist)}
```

returns:

```
EUDS {waveform_set}, {definition_string}, {(pinlist)}
```

### Parameters（取自子主题 List of timing setup commands › EUDS  -  Edge Usage Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98601_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter ALL for all defined waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The wa…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 List of timing setup commands › EUDS  -  Edge Usage Definition String）

```
EUDS? 1,,(@)
EUDS 1,"d1 d2 d3 r4",(io)
EUDS 1,"d1 d2 d3 d4 d5 d6 d7 d8",(clk)
```

### Syntax（取自子主题 List of timing setup commands › EVCK  -  EVent ClocK）

```
EVCK? {"multi-port_spec"}, {(port_list)}
```

returns:

```
EVCK {"multi-port_spec"}, event_clock_per, {(port)}
```

### Parameters（取自子主题 List of timing setup commands › EVCK  -  EVent ClocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126417_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：multi-port_spec | Name of a multi-port timing specification.

### Example（取自子主题 List of timing setup commands › EVCK  -  EVent ClocK）

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

### Syntax（取自子主题 List of timing setup commands › FTCG  FTCG  -  Functional Test ConfiGure）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98606_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：parameter | The parameter to be used is SKPR (SKip PRimaries).

### Example（取自子主题 List of timing setup commands › FTCG  FTCG  -  Functional Test ConfiGure）

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

### PCLK（取自子主题 List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

Fixed timing:

```
PCLK{waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### PCLK?（取自子主题 List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

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

### Parameters（取自子主题 List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98682_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example 1（取自子主题 List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

```
PCLK 101,1,20,(@)
```

This example sets the test system period for specification 101 to 20 ns.

### Example 2（取自子主题 List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

```
PCLK 101,1,40,(S1)
```

This example sets the test system period of pin S1 for specification 101 to 40 ns.

The `VCLK?`（raw: `02.06.02.02.319_VCLK__-__Verify_CLocK.md`） query checks whether a PCLK command with the specified parameter values was accepted with or without auto-correction.

### Syntax（取自子主题 List of timing setup commands › PDIV  -  Period DIVider）

```
PDIV? {specset_id|"multi-port_spec"|"wavetbl"} [,spec_type][,(pinlist)]
```

returns:

```
PDIV {specset_id|"multi-port_spec"}, {period_div}
```

### Parameters（取自子主题 List of timing setup commands › PDIV  -  Period DIVider）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98684_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：specset_id | Identifier of a timing specification, which is derived as follows: 100 * equation_set_no + specset_no

### Example（取自子主题 List of timing setup commands › PDIV  -  Period DIVider）

```
> PDIV? "fast",WFT,(I1)
< PDIV "fast",WFT,6,(I1)
```

This example queries the implicit period divider of the fast pin I1 in the wavetable `fast`. The factor is 6.

### Syntax（取自子主题 List of timing setup commands › RCLK  -  Reference CLocK source）

```
RCLK?
```

returns:

```
RCLK {clock_string}
```

### Parameters（取自子主题 List of timing setup commands › RCLK  -  Reference CLocK source）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98715_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：clock_string | The string shows which clock source is used as reference clock. Possible values are: EXTERNAL INTERNAL

### Example（取自子主题 List of timing setup commands › RCLK  -  Reference CLocK source）

```
RCLK?
```

returns:

```
RCLK INTERNAL
```

### Syntax（取自子主题 List of timing setup commands › RSET -  ReSET）

```
RSET {specifier}
```

### Parameters（取自子主题 List of timing setup commands › RSET -  ReSET）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98723_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：specifier | The specifier can be:
> 表内引用（1 条，供检索）：`UHCM`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）

### Example（取自子主题 List of timing setup commands › RSET -  ReSET）

```
RSET TIM
```

This example resets all waveform sets and timing sets and loads the hardware with the default vector rate and edge placement values. Only waveform set 1 and timing set 1 in waveform set 1 is active.

### Syntax（取自子主题 List of timing setup commands › SCLK  -  System CLocK query）

```
SCLK? {wf_set|specset_id|"multi-port_spec"|ALL|PRM}
```

returns:

```
SCLK {wf_set|specset_id|"multi-port_spec"} {sclk_val}
```

### Parameters（取自子主题 List of timing setup commands › SCLK  -  System CLocK query）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98728_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：wf_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? - …
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 List of timing setup commands › SCLK  -  System CLocK query）

```
> SCLK? 401
< SCLK 401,480
```

### Syntax（取自子主题 List of timing setup commands › SDSC  -  Set number DeSCriptions）

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
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：21 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

The following table explains the interpretation of the setup_comp_1 and setup_comp_2 parameters for every accepted value pair of the spec_type and type parameters:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729_3.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 4 列。
> 首行（上游原文）：spec_type | type | setup_comp_1 | setup_comp_2

### Example 1（取自子主题 List of timing setup commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,,,
< SDSC TIM,EQN,1,,"gross_func_eqn"
< SDSC TIM,EQN,2,,"specs_search_eqn"
< SDSC TIM,EQN,3,,"speed_eqn"
```

This example returns all defined equation sets.

### Example 2（取自子主题 List of timing setup commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,2,"spec_port_1_port_2",,(port_1)
< SDSC TIM,EQN,1,"spec_port_1_port_2",
     "gross_func_eqn",(port_1)
```

This example returns the equation set that is associated with port port_1 in the multiport specification

spec_port_1_port_2. Note that the setup_comp_1 parameter is ignored.

### Syntax（取自子主题 List of timing setup commands › SPCP  -  SPeCification Port list）

```
SPCP? {"multi-port_spec"|ALL}
```

returns:

```
SPCP {"multi-port_spec"}, {(portlist)}
```

### Parameters（取自子主题 List of timing setup commands › SPCP  -  SPeCification Port list）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98738_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：multi-port_spec | Defines the multi-port specification for which the ports are to be queried. You can enter ALL in order to display the ports for all defined mu…

### Example（取自子主题 List of timing setup commands › SPCP  -  SPeCification Port list）

```
> SPCP? ALL
< SPCP "spec_port_1_port_2",(port_1,port_2)
< SPCP "spec_ClkP_P1_P2",(ClockPort,p_CP_1,p_CP_2)
< SPCP "spec_ssearch_port_1_port_2",(port_1,port_2)
```

### Syntax（取自子主题 List of timing setup commands › SPEC  -  SPECification）

```
SPEC? {"module:resource"},["details"],[context], [(pinlist)]
```

returns:

```
SPEC {"module:resource"},["details"],[context], {answer},[(pinlist)]
```

   Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98739_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 3 列。
> 首行（上游原文）：module:resource | Specifies the module and the resource about which information is to be returned. Currently, the following values are allowed:

### Example 1（取自子主题 List of timing setup commands › SPEC  -  SPECification）

```
SPEC? "Result:Xmodes",,,(@)
```

returns

```
SPEC "Result:Xmodes",,,"1,2,4,6,8",(...)
```

This example queries which x-modes are possible for the result module on a Smart Scale system. On a Pin Scale system, x-mode 6 would be omitted in the reply.

### Example 2（取自子主题 List of timing setup commands › SPEC  -  SPECification）

The second example queries the termination modes that can be specified with the `TERM`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） command for pin "PS1600_pin" and level set 1:

```
SPEC? "Level:Term",,1,(PS1600_pin)
```

returns

```
SPEC "Level:Term",,1,"OFF,T,H,L,A,C,CT,HV,DIFHIZ",(PS1600_pin)
```

### Example 3（取自子主题 List of timing setup commands › SPEC  -  SPECification）

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

### SPRM（取自子主题 List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

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

### SPRM?（取自子主题 List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

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

### Parameters（取自子主题 List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98742_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set_no | The identification number of the waveform set. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum num…
> 表内引用（6 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `CONF, CONF? - (CONFiguration)`（raw: `02.06.02.02.31_CONF__CONF__-__CONFiguration.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `LSUS, LSUS? - (Level Sets USed)`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`） · `DSUS, DSUS? - (Dps Sets USed)`（raw: `02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`）

### Example（取自子主题 List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

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

### Syntax（取自子主题 List of timing setup commands › SPST  -  SPecset STatus）

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

### Parameters（取自子主题 List of timing setup commands › SPST  -  SPecset STatus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

Status bits for the status parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743_3.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：Bit | Description | Value
> 表内引用（10 条，供检索）：`ETIM`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`） · `ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） · `PCLK`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） · `CLKR`（raw: `02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md`） · `DRLV`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`） · `RCLV`（raw: `02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`） · `TERM`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） · `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`） · `SHVL`（raw: `02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md`） · `SVLR`（raw: `02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`）

### Example 1（取自子主题 List of timing setup commands › SPST  -  SPecset STatus）

```
> SPST? lev,all,all
< SPST LEV,1,1,0
```

### Example 2（取自子主题 List of timing setup commands › SPST  -  SPecset STatus）

```
> SPST? tim,all,all
<  SPST TIM,1,1,0
< SPST TIM,2,22,0
```

### Example 3（取自子主题 List of timing setup commands › SPST  -  SPecset STatus）

```
> SPST? TIM,,"mu_burst"
< SPST TIM,,"mu_burst",6
```

In this last example, a multi-port specification is queried. The answer says that bits 1 and 2 have been set. This has the effect that a drive or receive period 1 limit violation will be ignored, and only a period 2 limit violation will be recorded.

### Syntax（取自子主题 List of timing setup commands › STRS  -  Spec TRansition Search）

```
STRS? ["exec_context",] [start], [stop], {mode}, [(pinlist)], {spec_type}, {"spec_name[@port[@UNCHANGED]]"}, [stepwidth], {resolution}
```

returns:

```
STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]
```

### Parameters（取自子主题 List of timing setup commands › STRS  -  Spec TRansition Search）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98762_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts .
> 表内引用（4 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） · `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`） · `Modifying the period for a search or shmoo in a multi-port setup`（raw: `02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）

### Example（取自子主题 List of timing setup commands › STRS  -  Spec TRansition Search）

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

### Parameters（取自子主题 List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98764_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:
> 表内引用（1 条，供检索）：`Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）

### Example 1（取自子主题 List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The following example queries the values of the spec variable f in a setup where both single-port and multi-port specifications occur:

```
> SVLR? TIM,ALL,ALL,"f"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",35
< SVLR TIM,,"spec_p_1_p_2","f@p_2",33
< SVLR TIM,1,1,"f",37
```

### Example 2（取自子主题 List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The next example queries in which equation sets the spec variable f occurs:

```
> SVLR? TIM,ALL,,"f"
< SVLR TIM,1,,"f",
< SVLR TIM,2,,"f",
```

### Example 3（取自子主题 List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

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

### TSUS（取自子主题 List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS {waveform_set},{timing_set}
```

### TSUS?（取自子主题 List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

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

### Parameters（取自子主题 List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98817_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS 3,7
```

This example defines a maximum of 7 timing sets in waveform set 3.

```
TSUS? "spefc",(ARMPort)
TSUS "spefc",3,(ARMPort)
```

This example queries the number of timing sets defined for port ARMPort in the multiport specification spefc.

### TSUX（取自子主题 List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

```

TSUX {waveform_set},{timing_set}
```

### TSUX?（取自子主题 List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

```

TSUX? {waveform_set}
```

returns:

```
TSUX {waveform_set},{timing_set}
```

### Parameters（取自子主题 List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98818_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter ALL for all waveform sets in the query command.
> 表内引用（1 条，供检索）：`TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

### UPTD（取自子主题 List of timing setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD {status}, {flag}
```

### UPTD?（取自子主题 List of timing setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD? {status}
```

returns:

```
UPTD {status}, {flag}
```

### Example（取自子主题 List of timing setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD? CONF
```

This example requests if the pin configuration data has been changed since the file was last loaded or saved. If the data has not changed, the response is:

```
UPTD CONF,1
```

### Syntax（取自子主题 List of timing setup commands › VCLK  -  Verify CLocK）

```
VCLK? {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

returns:

```
VCLK {autocorrect}
```

### Parameters（取自子主题 List of timing setup commands › VCLK  -  Verify CLocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98844_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 List of timing setup commands › VCLK  -  Verify CLocK）

```
VCLK? 1,1,20,(@)
```

This example checks if a period of 20 ns will cause auto-correction to the edge placements in Timing Set 1 of Waveform Set 1 on any pin. If no auto-correction will occur the following string is returned:

```
VCLK 0
```

### Syntax（取自子主题 List of timing setup commands › VDCG  -  Verify Device Cycle for Group）

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

### Parameters（取自子主题 List of timing setup commands › VDCG  -  Verify Device Cycle for Group）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98846_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 4 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 List of timing setup commands › VDCG  -  Verify Device Cycle for Group）

```
VDCG? 1,ALL,(inputs)
```

returns:

```
VDCG 1,ALL,SLEN
```

This example checks the consistency of all device cycles for pins in the pin group "inputs" in waveform set 1. The test system replies that all device cycles for the specified group are consistently defined.

### Syntax（取自子主题 List of timing setup commands › VTIM  -  Verify TIMing）

```
VTIM? {waveform_set},{timing_set},{(pinlist)}
```

returns:

```
VTIM {status}
```

### Parameters（取自子主题 List of timing setup commands › VTIM  -  Verify TIMing）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98862_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 List of timing setup commands › VTIM  -  Verify TIMing）

The following example illustrates the working of VTIM? in a multi-port setup. The pins S1_1 and DS0_1 belong to the same port, and S1_2 belongs to another one.

```
> ETDS? "spec_port_1_port_2",ALL,,(S1_1,DS0_1,S1_2)
< ETDS "spec_port_1_port_2",1,,"d1:0 d2:30",(S1_1,DS0_1)
< ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(S1_1)
< ETDS "spec_port_1_port_2",2,,"d1:1 d2:12",(DS0_1)
< ETDS "spec_port_1_port_2",1,,"d1:-0.67 d2:1.33 d3:9.3",(S1_2)
```

This call of `ETDS?`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） shows that the edge timings of S1_1 and DS0_1 are the same in timing set 1, but not in timing set 2 of the port to which these pins belong.

```
> PCLK? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< PCLK "spec_port_1_port_2",1,50,(S1_1)
< PCLK "spec_port_1_port_2",2,20,(S1_1)
< PCLK "spec_port_1_port_2",1,50,(DS0_1)
< PCLK "spec_port_1_port_2",2,20,(DS0_1)
< PCLK "spec_port_1_port_2",1,16.667,(S1_2)
```

This call of `PCLK?`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） shows that the periods of S1_1 and DS0_1 are the same in the two timing sets of the port.

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

After changing the edge timing of DS0_1 in timing set 2 to the values of S1_1 with a call of `ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`）, VTIM? returns 1 although DS0_1 has a different timing in timing set 1 and in timing set 2, and S1_2, which belongs to another port, has different values altogether.

### Syntax（取自子主题 List of timing setup commands › VWFG  -  Verify WaveForms in Groups）

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

### Parameters（取自子主题 List of timing setup commands › VWFG  -  Verify WaveForms in Groups）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98863_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 List of timing setup commands › VWFG  -  Verify WaveForms in Groups）

```
> VWFG? "spec_search_wtb","SBC",(ser_in)
< VWFG 1
> VWFG? "spec_search_wtb",,(ser_in)
< VWFG 0
```

According to this example, the waveform and device cycle definition for device cycle SBC are the same for the pins in the group ser_in within the wavetable spec_search_wtb, but this does not hold for all device cycles that are defined for the pins of this group.

### Syntax（取自子主题 List of timing setup commands › VWFS  -  Verify WaveForm Sets）

```
VWFS? {waveform_set_1},{waveform_set_2},{(pinlist)}
```

returns:

```
VWFS {status}, {(pinlist)}
```

### Parameters（取自子主题 List of timing setup commands › VWFS  -  Verify WaveForm Sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98864_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：waveform_set_x | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, …
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 List of timing setup commands › VWFS  -  Verify WaveForm Sets）

```
VWFS? 1,2,(DATA)
```

This example checks whether waveform sets 1 and 2 are the same for the pins in the group DATA. If they are the same the following string is returned:

```
VWFS 1,(DATA)
```

### WAVE（取自子主题 List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
WAVE {wvf_set}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
WAVE {specset_id|"multiport_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}, ALLOW_EQ
```

### WAVE?（取自子主题 List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
WAVE? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {(pinlist)}
```

returns:

```
WAVE {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
```

### Parameters（取自子主题 List of timing setup commands › WAVE  WAVE  -  WAVEform）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98869_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? …
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

This example first defines a logical waveform with the index 2 for waveform set 1. The waveform uses the data parameter D11, the fixed action 0, and the complement C11 of D11. Then two physical waveforms are defined for logical waveform 2, which are referenced by the physical waveform DC/DC power units 4 and 5. Waveform 4 drives to 0 at edge d1, to 0 at d3, and to 1 at d4. Waveform 5 drives to 1 at edge d1, to 0 at d3, and to 0 at d4.

### WFDF（取自子主题 List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
WFDF {wvf_set}, {wfIndex}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### WFDF?（取自子主题 List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
WFDF? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDF {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98871_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 4 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…
> 表内引用（4 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `WAVE`（raw: `02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） · `Restrictions for drive edges`（raw: `02.06.06.01.03.01.02.01_Restrictions_for_drive_edges.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
> WFDF 1,2,N,N,D11,N,N,N,(D0,D2,D2,D3)
```

This example defines a waveform referenced by waveform index 2. The waveform uses the drive data and tri-state parameter 1. Edge number 3 provides the timing for this waveform. The definitions are made for waveform set 1 and for pins D0 to D3.

### WFDS（取自子主题 List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

```
WFDS {wvf_set}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
WFDS {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### WFDS?（取自子主题 List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

```
WFDS? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDS {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
```

### Parameters（取自子主题 List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98872_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 4 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…

### Example（取自子主题 List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

```
> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)
> WFDS 1,1,,"r4:EE1",(io)
> WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)

> WFDS? 1,ALL,,(@)
< WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)
< WFDS 1,1,,"r4:EE1",(io)
< WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
```

### Syntax（取自子主题 List of timing setup commands › WFUD -  WaveForm UnDefine）

```
WFUD {wvf_set},{wfIndex},{(pinlist)}
WFUD {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### Parameters（取自子主题 List of timing setup commands › WFUD -  WaveForm UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98875_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 List of timing setup commands › WFUD -  WaveForm UnDefine）

```
WFUD 1,2,(D0,D2,D2,D3)
```

This example deletes a logical waveform defined for waveform set 1 and for pins `D0` to `D3`, referenced by waveform index 2.

### Syntax（取自子主题 List of timing setup commands › WRST -  Waveform ReSeT）

```
WRST {waveform_set}
```

### Parameters（取自子主题 List of timing setup commands › WRST -  Waveform ReSeT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98876_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 List of timing setup commands › WRST -  Waveform ReSeT）

```
WRST 3
```

This example resets all waveform and timing entries for all pins for waveform set 3.

### WSDM（取自子主题 List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

```
WSDM {waveform_set}, {display_mode}
```

### Parameters（取自子主题 List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98877_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum nu…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

```
> WSDM? "spec_1", (port_1)
< WSDM  "spec_1", 0
```

This example queries the display mode of port port_1 in the multiport specification spec_1. The reply shows that it is set to the "classic" display mode.

### WSUS（取自子主题 List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS {waveform_set}
```

### WSUS?（取自子主题 List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS?
```

returns:

```
WSUS {waveform_set}
```

### Parameters（取自子主题 List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98878_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number. This is the highest number currently allocated to a waveform set or the highest number of a set you want to load. The number…
> 表内引用（1 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS 3
```

This example sets the number of used waveform sets to 3.

<!-- 语法节 end -->

## 是什么

**这一页是「timing setup 命令」这一族的入口页**：它先讲 timing setup 是什么、
有哪两种做法，再指向那条长长的命令清单。

原文第一句把 timing setup 管的两样东西定死：

> 「The timing setup for a device defines **the waveforms that can be sent to the pins of the DUT**
> during a test, and **the possible period lengths**, that is, the possible lengths of the tester
> cycle, which is the time span used for executing one waveform.」

| 管什么 | 原文 |
|---|---|
| **波形**（能发给 DUT 引脚的） | `the waveforms that can be sent to the pins of the DUT` |
| **周期长度**（tester cycle 能有几种长度） | `the possible period lengths … the time span used for executing one waveform` |

### 波形的构成：action → edge → 位置

原文用三句话把波形拆成三层，**顺序不能颠倒**：

> 「Waveforms are defined as **ordered sequences of actions**. Every action is **associated with an
> edge**, and every edge **has a position within a tester cycle**. **The order of the actions
> defines the waveform shape.** These shapes are defined **independently of the edge positions**.」

**拆开：**

| 层 | 是什么 | 谁决定 |
|---|---|---|
| **action** | 一个动作 | 若干 action 的**顺序** |
| **edge** | 每个 action **关联一个 edge** | — |
| **position** | 每个 edge 在 tester cycle 里的**位置** | — |
| **waveform shape** | 波形形状 | **由 action 的顺序定义** |
| — | **形状和 edge 位置是分开定义的** | `defined independently of the edge positions` |

> **最后那句是本页最要紧的一句**：**「波形长什么样」和「边沿在哪儿」是两件事。**
> 所以下面的 `wavetable` / `equation set` 才会分成两个文件。

### 两种定义波形形状的格式

> 「There are two general formats for defining waveform shapes. You can either **define explicitly
> which edge is associated with which action**, or you can **only specify the actions in the
> definition**. In the latter case **the number of the associated edge will usually be determined by
> the position of the action within the action sequence**.」

| 格式 | 怎么定 edge |
|---|---|
| **显式** | **直接写明哪个 edge 关联哪个 action** |
| **隐式** | **只写 action**；edge 编号**由 action 在序列里的位置推出** |

> **注意原文用的是 `usually`（通常）**——不是「一定」。
> **本页照实保留这个词，不把它读成铁律。**

### 标准做法是 equation based，但 fixed 也存在

> 「**The standard timing setup of SmarTest is equation based.** This means that you can use
> **variables** in the definitions of edge positions and period lengths, which considerably enhances
> the flexibility of the setup. **It is also possible to define a fixed timing** where edge positions
> and period length are defined as **constants**.」

| 做法 | edge 位置 / 周期长度 |
|---|---|
| **equation based**（**SmarTest 的标准做法**） | 用**变量**定义 → 灵活性高 |
| **fixed** | 用**常量**定义 |

### 两种做法的机制差别：下载粒度

这是两种做法**最实质**的区别，原文最后一段：

> 「With **fixed** timing, **each setup element is defined by calling a firmware command**.
> With **equation based** timing, **the setup elements are part of larger data blocks that are
> downloaded to the tester as a whole**.」

| 做法 | 下发方式 |
|---|---|
| **fixed** | **一条命令定义一个 setup 元素** |
| **equation based** | **元素是一整块一起下发的** |

> **（推断）** 这和 [[equation-based-level-setup]] 里那句
> 「the setup elements are part of larger data blocks which are downloaded to the test system as a
> whole」**几乎是同一句话**（一个说 timing、一个说 level）。
> **依据**：两篇措辞一致，且都在讲「equation based 对上一次性命令」这组对立。
> **本页并列这两处，但不据此说 level 和 timing 共用同一套机制**——
> **两边都没有这么说。**

### equation based 下，三个东西各存在哪

> 「In equation based timing, **waveform shapes are defined in a wavetable**, and **edge positions
> are defined in an equation set**. **Wavetable and equation set are brought together in a timing
> specification.** **In a multi-port setup, this must be done separately for every involved
> port.**」

| 内容 | 存在哪 |
|---|---|
| **波形形状** | **wavetable** |
| **edge 位置** | **equation set** |
| **两者合起来** | **timing specification** |

> **⚠️ 多 port 是这一节唯一的坑**：`this must be done **separately for every involved port**`
> ——**上面的「合起来」在 multiport 下要对每个 port 各做一遍。**

### 语法节：这一页的正文全在脚本那一节里

`## 语法 / 参数` 一节有 **4800 行上下**，来自两篇子主题
（`Concepts of timing setup`、`List of timing setup commands`）——
里面有 `APRM`、`BWDF`、`BWDS`、`CDCP`、`CLKR`、`DCDT`、`DCUD`、`DFCR`、`DPRT` 等命令的
语法、参数表和例子。

**所以本页的读法是**：散文这一节讲**概念**，**命令清单和参数在脚本那一节**，
而那一节**逐字来自两篇本页没读的子主题**。

## 典型用法

**原文这篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**，
也没有步骤。**本页按原文能支撑的内容列两条：**

**1. 选做法**：

| 你要什么 | 用哪个 |
|---|---|
| 边沿位置/周期要用**变量**、要灵活 | **equation based**（**SmarTest 的标准做法**） |
| 边沿位置/周期就是**常量** | **fixed**（**用 firmware 命令逐条定义**） |

**2. equation based 下要准备的三个东西**：
**wavetable**（波形形状）+ **equation set**（edge 位置）→ **timing specification**（合起来）。
**multiport 的话，每个 port 各做一遍。**

**3. 命令清单在哪**：`Subtopics` 第 2 篇 `List of timing setup commands`
——**本页没读**，但它就是语法节里那 4800 行的来源。
**它是这一族命令的清单，和 [[command-reference]] 是父子关系**
（`Timing Setup Commands` 是 `Command Reference` 的 18 个子主题之一）。

## 和谁有关

- [[timing]] — 本页 `stage: timing` 的理由：**它是 timing 的命令侧**
- [[command-reference]] — **父页**：本页是它 18 个子主题里的第 6 个
- [[timing-specification]] — **本页的产出物**：wavetable + equation set 合起来就是它
- [[timing-equation-set]] / [[wavetable]] — **equation based 下的两个原料**
- [[waveform-set]] — 波形集合；**和 wavetable 是不是同一层，本页没说**（本页没读它）
- [[timing-file]] / [[timing-master-file]] — timing 的文件侧；**本页讲的是命令侧**
- [[timing-setup-tool]] / [[timing-set-selector]] — timing 的 GUI 侧；
  **本页讲的是「命令怎么写」，原文没提 GUI**
- [[pattern]] — **本页定义的波形最终要发给引脚**，那正是 pattern 做的事；
  **但原文没有把两者联系起来**
- [[equation-based-level-setup]] — **同一族做法的 level 侧**；见上面那条（推断）
- `Concepts of timing setup` / `List of timing setup commands`（**均未建**）—
  **本页 `Subtopics` 的两篇，本页一篇没读**；
  **语法节里那 4800 行就是它们被脚本抽出来的片段**

## 版本

- **Introduced before SmarTest 6.3.2**

（原文 `## Functional changes` 只有这一条，**没有后续版本条目**——
即这一族命令在 6.3.2 之后没有可查的变化记录。）

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.md`

**本页没做的**：

- **`Subtopics` 的两篇一篇没读**——**这是本页最大的缺口**。
  本页主文档只有五段概念说明，**而「有哪些命令、每个命令什么参数」
  全在那两篇里**。本页**只有概念，没有一条命令的用法**。
- **`## 语法 / 参数` 一节里的 4800 行，本页一条都没有验证过。**
  它们由脚本从两篇子主题逐字抄出，**本页没读那两篇**，
  所以无法判断**命令清单是否完整、有没有漏项、例子之间的上下文是否连续**。
- **图零张**（原文这篇没有图）。
- **`wavetable` 和 `waveform set` 是不是同一个东西，本页不知道**——
  原文这里用的是 `wavetable`，而 wiki 里另有 [[waveform-set]] 和 [[wavetable-file]] 两页。
- **`edge` 有几种、`action` 有几种，本页没读、没展开**——
  原文只说了这两层的**关系**，没说它们的**取值**。
- **原文没有 `## Procedure` / `## Before you begin` / `## What to do next` /
  `## Related information`**——四个都没有。**所以「典型用法」一节里
  没有一条来自原文的步骤。**
- **`fixed` timing 那一侧本页只有两句话**——原文对它的着墨就是
  「also possible」加「用 firmware 命令逐条定义」，**没有例子、没有指向任何一篇**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`usually` 这个词让「隐式格式」的规则不是确定的**——
> `the number of the associated edge will **usually** be determined by the position of the action
> within the action sequence`。**「通常」意味着有例外，而原文没有说例外是什么。**
> ② **`period length` 和 `period lengths` 单复数混用**——
> 第一段是 `the possible period lengths`（复数），
> 后面是 `the definitions of edge positions and period lengths`（复数），
> 再后面 `period length are defined as constants`（**单数**，且和 `edge positions` 并列）。
> ③ **`## Functional changes` 只有一条「Introduced before SmarTest 6.3.2」**，
> 而语法节里那 4800 行覆盖了几十条命令——**命令级的增删在这一篇里查不到**。
> ④ **本页 `Subtopics` 只有两篇，但语法节却从它们抽出 4800 行**——
> **说明第 2 篇 `List of timing setup commands` 是个很长的清单页**，
> 而本页正文完全没有提它的规模。

`verified: doc-only`
