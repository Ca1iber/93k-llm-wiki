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

> 本节 **141,163 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34_Timing_Setup_Tool.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.02_Data_organization_of_equation_based_timing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.05_Defining_the_timing_specification.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.01_APRM_-__Activate_PRiMary_sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.02_BWDF__BWDF__-__Break_Waveform_DeFinition.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.03_BWDS__BWDS__-__Break_Waveform_Definition_String.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.04_CDCP__-__Cycle_Device_Cycle_Parameter.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.05_CLKR__CLKR__-__CLocK_Resolution.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.06_DCDT__DCDT__-__Device_Cycle_DefaulT.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.07_DCUD_-__Device_Cycle_UnDefine.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.08_DFCR__DFCR__-__DeFine_Clock_Routing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.09_DPRT__DPRT__-__Default_PRimary_Timing_sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.10_DSCP__DSCP__-__Define_System_Control_Parameter.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.11_EDDC__-__EDge_in_Device_Cycle.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.12_EDSP__EDSP__-__EDge_SPecification.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.13_EQFS_-__EQuation_FileS_command_transfer.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.14_EQSP__EQSP__-__EQuation_SPecification_transfer.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.15_ETDS__ETDS__-__Edge_Timing_Definition_String.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.16_ETIM__ETIM__-__Edge_TIMing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.17_EUDS__-__Edge_Usage_Definition_String.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.18_EVCK__-__EVent_ClocK.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.19_FTCG__FTCG__-__Functional_Test_ConfiGure.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.20_PCLK__PCLK__-__Pin_CLocK.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.21_PDIV__-__Period_DIVider.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.22_RCLK__-__Reference_CLocK_source.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.23_RSET_-__ReSET.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.24_SCLK__-__System_CLocK_query.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.25_SDSC__-__Set_number_DeSCriptions.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.26_SPCP__-__SPeCification_Port_list.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.27_SPEC__-__SPECification.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.28_SPRM__SPRM__-__Set_PRiMary_sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.29_SPST__-__SPecset_STatus.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.30_STRS__-__Spec_TRansition_Search.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.32_TSUS__TSUS__-__Timing_Sets_USed.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.33_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.34_UPTD__UPTD__-__UP_To_Date.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.35_VCLK__-__Verify_CLocK.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.36_VDCG__-__Verify_Device_Cycle_for_Group.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.37_VTIM__-__Verify_TIMing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.38_VWFG__-__Verify_WaveForms_in_Groups.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.39_VWFS__-__Verify_WaveForm_Sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.40_WAVE__WAVE__-__WAVEform.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.41_WFDF__WFDF__-__WaveForm_DeFinition.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.42_WFDS__WFDS__-__WaveForm_Definition_String.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.43_WFUD_-__WaveForm_UnDefine.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.44_WRST_-__Waveform_ReSeT.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.45_WSDM__WSDM__-__Waveform_Set_Display_Mode.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.46_WSUS__WSUS__-__Waveform_Sets_USed.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.01_Data_organization_of_equation_based_timing.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05.01_Master_file_format_for_timing_setup.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06_Using_the_Timing_Setup_Tool.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Timing Setup Commands › Concepts of timing setup › Data organization of equation based timing）

The following figure exemplifies the structure of equation based timing by a schematic setup:

 !`Timing Specifications`（raw: `../../../../agent-html/10596.png`）

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

| mode | Selects the activation mode: | Selects the activation mode: |
|---|---|---|
| mode | FRC | Forced activation. Primary sets are always activated. |
| mode | CNL | Conditional activation, depends on previous activation performed by APRM or by any of the commands in the second list above. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98485_4.htm`。

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

| wvf_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|---|
| specset_id | Derived as follows:<br><br>`100 *` equation_set_no `+ ` specset_no | Derived as follows:<br><br>`100 *` equation_set_no `+ ` specset_no |
| wavetable_name | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. |
| multiport_spec | To query a multi-port specification, enter the name of the specification. | To query a multi-port specification, enter the name of the specification. |
| a1..a6 | Edge action. The actions you can define are: | Edge action. The actions you can define are: |
| a1..a6 | N | no action |
| a1..a6 | F0N | drive 0, no tri-state action |
| a1..a6 | F1N | drive 1, no tri-state action |
| a1..a6 | FN0 | no drive action, tri-state off |
| a1..a6 | FNZ | no drive action, tri-state on |
| a1..a6 | F00 | drive 0, tri-state off |
| a1..a6 | F0Z | drive 0, tri-state on |
| a1..a6 | F10 | drive 1, tri-state off |
| a1..a6 | F1Z | drive 1, tri-state on |
| pinlist | The name of the pin or pins for which break waveform definitions are to be made or read back. The symbol @ can be used to specify all configured input and IO pins. If more than one pin is to be included, the names must be separated with a comma. | The name of the pin or pins for which break waveform definitions are to be made or read back. The symbol @ can be used to specify all configured input and IO pins. If more than one pin is to be included, the names must be separated with a comma. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98497_3.htm`。

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
| wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. Enter PRM for the Primary waveform set. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|
| wavetable_name | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. wavetable_name can only be specified in the query. |
| specset_id | Derived as follows:<br><br>100 * equation_set_no + specset_no<br><br>specset_id can only be specified in the query. |
| multi-port_spec | To query a multi-port specification, enter the name of the specification. |
| break_waveform_index | Enter DEF for the default break waveform or an integer in the range 0 to 3. This parameter is optional in release 2.0 and can only be used to select the default break waveform (DEF). |
| mode | NOT USED. |
| definition_string | The definition string consists of a sequence of items each of which associates a drive action with a drive edge.<br><br>Receive edge are always denoted by rn.<br><br>All edges which are not explicitly specified are set to N. In the query only those edges that are used are printed.<br><br>For details of the syntax see `WFDS, WFDS? - (WaveForm Definition String)`（raw: `../02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）. |
| pinlist | The name of the pin or pins for which break waveform definitions are to be made or read back. The symbol @ can be used to specify all configured input and IO pins. If more than one pin is to be included, the names must be separated with a comma. |

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

| start_cycle | This is an integer that defines the first cycle to be analyzed. The range of values for this parameter depends on the analysis mode:<br><br>- In the Start Analysis mode enter a positive value between 0 and 2^48. The system responds by counting cycles forwards from the first cycle of the test and returns a positive number. The Start Analysis mode is the default setting.<br>- In the Stop Analysis enter a negative number between -2^48 and -1. The system responds by counting cycles backwards relative to the end of the test at -1 cycle and returns a negative number. This mode is used by the system for Stop-on-Error tests. | This is an integer that defines the first cycle to be analyzed. The range of values for this parameter depends on the analysis mode:<br><br>- In the Start Analysis mode enter a positive value between 0 and 2^48. The system responds by counting cycles forwards from the first cycle of the test and returns a positive number. The Start Analysis mode is the default setting.<br>- In the Stop Analysis enter a negative number between -2^48 and -1. The system responds by counting cycles backwards relative to the end of the test at -1 cycle and returns a negative number. This mode is used by the system for Stop-on-Error tests. |
|---|---|---|
| cycle | In the query, the consecutive number of the displayed cycle. | In the query, the consecutive number of the displayed cycle. |
| no_of_cycles | This is an integer that defines the number of cycles to be analyzed. The range for this parameter is 0 to 1000. | This is an integer that defines the number of cycles to be analyzed. The range for this parameter is 0 to 1000. |
| strt_disp | This parameter defines the offset of your range of interest from start_cycle. The actual display starts with the last device cycle that does not begin before start_cycle and does not end before start_cycle + strt_disp.<br><br>The purpose of this construction is to enable a correct device cycle reconstruction even if the first cycle you are interested in does not lie at a device cycle boundary (a device cycle can generate up to 16 cycles). | This parameter defines the offset of your range of interest from start_cycle. The actual display starts with the last device cycle that does not begin before start_cycle and does not end before start_cycle + strt_disp.<br><br>The purpose of this construction is to enable a correct device cycle reconstruction even if the first cycle you are interested in does not lie at a device cycle boundary (a device cycle can generate up to 16 cycles). |
| disp_length | Specifies the display length in cycles. This parameter determines the end of your range of interest. The actual display stops with the last device cycle that starts before start_cycle + strt_disp + disp_length.<br><br>If this parameter is larger than no_of_cycles, it is ignored. | Specifies the display length in cycles. This parameter determines the end of your range of interest. The actual display stops with the last device cycle that starts before start_cycle + strt_disp + disp_length.<br><br>If this parameter is larger than no_of_cycles, it is ignored. |
| pinlist | The pin name or names for which a device cycle data transfer is to be made. If more than one pin is required, the names must be separated with a comma. The @ character can be used to download data for all configured pins. | The pin name or names for which a device cycle data transfer is to be made. If more than one pin is required, the names must be separated with a comma. The @ character can be used to download data for all configured pins. |
| dev_cyc_name | A reply parameter, giving the name of the reconstructed device cycle. | A reply parameter, giving the name of the reconstructed device cycle. |
| dev_cyc_len | A reply parameter, giving the length of the reconstructed device cycle. For SmarTest 7.10 this is always 1. | A reply parameter, giving the length of the reconstructed device cycle. For SmarTest 7.10 this is always 1. |
| DD1 and DD2 | Drive Data parameters. They contain values for both drive data and tri-state. The values the system returns are: | Drive Data parameters. They contain values for both drive data and tri-state. The values the system returns are: |
| DD1 and DD2 | F00 | drive 0, tri-state off |
| DD1 and DD2 | F10 | drive 1, tri-state off |
| DD1 and DD2 | F0Z | drive 0, tri-state on |
| DD1 and DD2 | F1Z | drive 1, tri-state on |
| DD1 and DD2 | N | Not used. Returned if no drive data parameter is set to a drive and tri-state value. |
| DD1 and DD2 | UC | Unclear. The system may return this value to indicate that the interpretation of the device cycle for that parameter is unclear, that is, the physical waveforms are inconsistent for the device cycle. |
| ED1 and ED2 | Expected Data Parameters. The values the system returns are: | Expected Data Parameters. The values the system returns are: |
| ED1 and ED2 | F0 | compare to 0 |
| ED1 and ED2 | F1 | compare to 1 |
| ED1 and ED2 | FI | compare to intermediate |
| ED1 and ED2 | FX | compare to mask |
| ED1 and ED2 | FU | compare to unstable |
| ED1 and ED2 | N | Not used. Returned if no expected data parameter is set to a compare value. |
| ED1 and ED2 | UC | Unclear. The system may return this value to indicate that the interpretation of the device cycle for that parameter is unclear, that is, the physical waveforms are inconsistent for the device cycle. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98499_4.htm`。

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

| waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. |
|---|---|
| specset_id | Derived as follows:<br><br>100 * equation_set_no + specset_no |
| multi-port_spec | To set or query the resolution of a multi-port timing specification, specify the name of the specification. |
| ref_period | Not used. (Ignored) |
| period_res | The period resolution (in ns) for the specified specification or waveform set.<br><br>If necessary, period_res is rounded to nine digits after the decimal point. The allowable maximum period resolution is the maximum tester period value. The minimum period resolution is determined by the hardware (see `Automatic calculation of period resolution for single-port setups`（raw: `../02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md`）). |
| type | In the query, the type parameter specifies which resolution is queried. The allowed values are:<br><br>VIRTUAL: The period resolution (period_res) is queried. This is the default.<br><br>EXACT: The clock resolution (clock_res) is queried. |
| clock_res | In the answer to the query, the clock resolution is returned if type is set to EXACT in the query. |

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

| waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|
| dev_cyc_name | The device cycle name. Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes. Enter ALL for the removal of all device cycles from the device cycle table. |
| pinlist | The name of the pin or pins for which device cycle definitions are to be deleted. This parameter can also include groups previously created by the `DFGP`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma. |

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

| source_group | specifies the hardware group whose local clock is to be routed to dest_group. The format is Gx, where x is the group number. |
|---|---|
| dest_group | specifies the hardware group whose inherited clock is to be changed. |

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

| waveform_set | Waveform set number. |
|---|---|
| specset_id | Derived as follows:<br><br>100 * equation_set_no + spec_set_no<br><br>Note that the spec set ID identifies the primary wavetable in equation based testing. |
| multi-port_spec | In a multi-port setup, a primary multiport specification can be specified. |
| timing_set | The identification number of the timing set. Enter an integer in the range 1 to the maximum number of allowed timing sets (of the selected waveform set or timing specification). The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of timing sets allowed (as defined by DSCP).<br><br>In a multiport setup, the timing set number applies to all ports of the specification if no port is specified. Otherwise, the number applies to the specified port. |
| timing_set_list | In a multi-port setup, you can specify primary timing sets for all ports of the specification by entering a list of numbers separated by commas.<br><br>In the query, the numbers of the primary timing sets are returned in a list for all ports of the primary specification unless the numbers are identical for all ports or a port has been specified in the query. |
| port | In a multi-port setup, you can specify a port of the specification that was entered as the first parameter. In this case, the timing set number specified as the second parameter will only be applied to the specified port. The port parameter is ignored if a timing set list is specified. |

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

| device_cycle | The device_cycle parameter is an integer that defines the absolute maximum number of device cycles that you can create for one pin.<br><br>Default: 256<br><br>Maximum: 16384<br><br>Note that the total number of device cycles gets evenly divided between the combined number of waveform sets and wavetables. If you use the default values, then 256 device cycles divides into the total number of 32 `waveform sets and wavetables`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） to give you 8 device cycles per waveform set/wavetable. If you choose values that do not divide evenly, then the number of device cycles will be rounded up to the next multiple of the `waveform_set`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） parameter. |
|---|---|
| devicecycle_set | The devicecycle_set parameter is an integer that defines the maximum number of device cycle sets that you can create. Device cycle sets are needed for selective digital capture.<br><br>Default: 1<br><br>Maximum: 128 |
| dps_set | The dps_set parameter is an integer that defines the maximum number of DPS sets you can create.<br><br>Default: 32<br><br>Maximum: 256 |
| level_set | The level_set parameter is an integer that defines the combined total of level sets for fixed and equation based levels that you can create.<br><br>Default: 32<br><br>Maximum: 256 |
| period_res_prec | This parameter defines the precision with which the period resolution is calculated by the system. It has no effect on a user defined period resolution (using, for example, the period_res keyword in the equation set).<br><br>The default is 4, if the .technology file does not contain this parameter.<br><br>If it does, the value of the .technology file is the default.<br><br>This value is set to 9, the greatest possible value, when a device is created. |
| pmu_set | The pmu_set parameter is an integer that defines the maximum number of actions that can be contained in all measurement sets of all PPMU DC sets.<br><br>Default: 1024<br><br>Maximum: 12800 |
| routing_set | Defines the number of routing sets managed by the firmware, provided by the MCD.<br><br>Default: 256<br><br>Maximum: 512 |
| timing_set | The timing_set parameter is an integer that defines the maximum combined total of timing sets for fixed and equation based timing you can create.<br><br>Default: 256<br><br>Maximum: 999<br><br>The number of timing sets must be equal to or greater than the number of waveform sets, as there must be at least one timing set per waveform set. |
| waveform_set | The waveform_set parameter defines the maximum combined total of waveform sets (fixed timing) and wavetables (equation based timing) you can create. Thus, if you specify a value of 32, you could, for example, create 10 waveform sets and 22 wavetables.<br><br>Default: 32<br><br>Maximum: 128 |

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
| waveform_set | Specifies a waveform set number for a fixed timing setup. |
|---|---|
| specset_id | Specifies a spec set ID for an equation based setup. The spec set ID is derived from an equation set number and a spec set number as follows:<br><br>100 * equation_set_no + specset_no |
| multi-port_spec | Specifies the name of a multiport specification for a multi-port setup. PRM is the default value. |
| timing_set | Specifies the number of the a timing set. PRM is the default value. |
| edge_spec | The edge specifier can either be a physical edge (d1 through d8 or r1 through r8), or one of the data parameters D1, D2, C1, C2 (drive parameters) or E1, E2 (receive parameters). |
| edge_number | In the query reply, this parameter contains the edge that is used as leading or trailing edge. |
| dev_cyc_name | Specifies the name of a logical device cycle that uses the data parameter given as the edge_spec. It must be defined for all pins in pinlist. If you do not enter a name in this parameter, the first device cycle in the device cycle table is used. |
| dc_ref | This parameter specifies the input edge. The input edge determines the algorithm according to which the trailing edge is selected. The two options are LE (for "leading edge") and TE (for "trailing edge").<br><br>The leading edge will always be the first edge that is associated with the specified data parameter within the specified device cycle, regardless of whether LE or TE is specified.<br><br>For the trailing edge the following rules apply:<br><br>- When you specify LE, trailing and leading edge will be identical.<br>- When you specify TE, then drive parameters and receive parameters are treated differently.<br><br>- Drive parameter: The trailing edge will be the first drive edge after the leading edge thats performs a data or tri-state action. Note that this trailing edge need not be associated in any way with the data parameter of the leading edge.<br>- Receive parameter: If the action of the leading edge is an edge compare, leading and trailing edge will be identical. If it is the start action of a window compare, then the associated window close edge will be the trailing edge.<br><br>For both cases, see the example below.<br><br>In the query, you can also specify both. In this case both the leading and the trailing edge will be returned for the pins in pinlist. |
| direction | This parameter can be in or out. If in is selected to define an input edge, then the edge_spec parameter must be D1, D2, C1, or C2. If out is selected to define a receiver edge, then the edge_spec parameter must be E1 or E2. If either in or out is selected along with an edge_spec parameter of 1,2...6, then a check is performed to ensure that the edges of all pins are in the required direction. If no entry is made in this parameter, the measuring edges of the pin in pinlist can have any direction or be unused. |
| pinlist | The parameters of the EDSP command are applied to all pins named in this parameter. If more than one pin is used, the names must be separated by a comma.<br><br>In a multi-port setup, all pins must belong to the same port of the specification that was entered as the first parameter. |

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › EQFS -  EQuation FileS command transfer）

| spec_type | Which specification to use: | Which specification to use: |
|---|---|---|
| spec_type | LEV | to specify levels, or |
| spec_type | TIM | to specify timing. |
| part | Which part of the specification type to use: | Which part of the specification type to use: |
| part | WVT | to specify wavetable (only for spec_type = TIM), |
| part | EQN | to specify equations, or |
| part | SPS | to specify specs. |
| part | operation | Use LOAD or SAVE. |
| eqn_filename | The absolute filename of the temporary equation based timing file. | The absolute filename of the temporary equation based timing file. |
| error_filename | The absolute filename of the file to which error reports are written.<br><br>Use UI_REPORT to direct error reports to the report window.<br><br>If this parameter is not specified, only a summarized error message is reported. | The absolute filename of the file to which error reports are written.<br><br>Use UI_REPORT to direct error reports to the report window.<br><br>If this parameter is not specified, only a summarized error message is reported. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98592_4.htm`。

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
| spec_type | The mandatory parameter defines which specification type to use.<br><br>Use:<br><br>- LEV to specify levels<br>- TIM to specify timing |
|---|---|
| part | The mandatory parameter defines which part of the specification type to use.<br><br>Use:<br><br>- EQN to specify equations<br>- SPS to specify specs<br>- WVT to specify a wavetable<br><br>part can only be set to WVT, EQN, or CLK if spec_type is set to TIM. |
| #spec(data) | An equation based set of data (for example wavetables) in binary format.<br><br>This parameter enables you to define the length of the data (in bytes) and the data itself to be transferred. It has the following format:<br><br>- A # to mark the start of the data block.<br>- One digit indicating how many digits make up the data length specifier.<br>- A number of digits indicating the length (in bytes) of the data to follow.<br>- A number of characters which make up the specified equation based testing file. This stream of characters must be terminated with a @ character. |

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

| waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query, you can also enter ALL for all waveform sets. |
|---|---|
| specset_id | Derived as follows:<br><br>`100 *`equation_set_no `+ `specset_no |
| multi-port_spec | For a multi-port setup, specify the name of a multi-port specification.<br><br>Note that the multi-port specification uniquely determines an equation set for every pin of pinlist, because no pin can belong to more than one port within a multi-port specification. |
| timing_set | Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by TSUS. |
| mode | The operating mode. For the query, you can enter ALL for all modes or BIDIR for bidirectional mode, that is, for edges that serve both as drive and receive edges.<br><br>With fast pins, you can specify the mode DELTA for both the command and the query. In this mode, the delays specified for edges with an index > 1 are interpreted as offsets from the calculated default values. |
| definition_string | The definition string consists of a sequence of items each of which associates a delay with a drive or compare edge. On Pin Scale 800/3600 boards, drive edges are denoted by dn. On Pin Scale 9G boards, there are two kinds of drive edges, which are denoted by fn and sn, respectively; for details see `Defining waveforms for Pin Scale 9G pins`（raw: `../02.06_Command_Reference/02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`）. You can also use the dn notation for Pin Scale 9G channels, but mixing both notations in one string is not allowed. Receive edges are always denoted by rn.<br><br>Unless you employ the pdiv statement for fast pins (see below), all edges which are not explicitly set remain unchanged.<br><br>The range of the edge delay is -8000 ns to +24000 ns (or -4 to +12 test system periods) for the Pin Scale 3600/800.<br><br>On Pin Scale 800/3600 boards, the restrictions for edge ordering must be observed both in fixed and equation based timing. For example, you cannot assign a greater delay to d1 than to d3 if d1 precedes d3 in a waveform definition. For more information, see `Selecting and ordering edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）.<br><br>Note that with equation based timing, ETDS returns no error message when the edge order restrictions are violated.<br><br>On Pin Scale 9G boards, ordering of drive edges is not restricted in any way. |
|  | Special Rules for Fast Pins:<br><br>If a pin is configured as a fast pin in the context of the specification given by the first parameter, you can specify the period divider at the start of the definition string. The format is pdiv:n, where n must be the same value as the period_div value of the pins in pinlist within the timing set specified by the timing_set parameter.<br><br>If you specify pdiv:nand a delay for the first edge, ETDS calculates delays for the following n-1 edges except those that are specified explicitly in the string. Note that for n = 3, the edges with index 1, 3, 5 are used for internal reasons.<br><br>If you omit either pdiv or the first edge, only the specified edges are modified. However, with receive edges this is only possible for r1.<br><br>The calculated delays are determined for the ith edge by the following formula:<br><br>1st_edge_delay + (i-1) * (period/pdiv)<br><br>1st_edge_delay is the delay specified for the first edge (d1 or r1; the generic notation e1 is not allowed for fast pins). If the first edge is not specified in the string, its delay is set to 0. An example for the calculation will be given below.<br><br>Note that when both the period divider and a delay for the first edge are present in the definition string, then the delays for all the edges required by the period divider will be overwritten.<br><br>When a delay is explicitly specified for one of the edges, this delay overrides the calculated default. There are two formats to specify overrides. You can either define absolute delays or the offsets from the default delays.<br><br>If you want to use the second, relative format, you must specify DELTA for the modeparameter. Note that you can also specify negative offsets in the DELTA mode. |
| pinlist | The name of the pin or pins for which edge delays are to be set or read back. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.<br><br>In a multi-port setup, every pin must belong to a port of the specified specification. |

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
| waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. |
|---|---|
| specset_id | Derived as follows:<br><br>`100 *`equation_set_no `+ `specset_no |
| timing_set | Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by TSUS. |
| t1..t6 | Edge delay in ns. Note that the positions of some edges may be affected by the use and position of previously defined edges as explained in "Restrictions" in `ETIM, ETIM? - (Edge TIMing)`（raw: `../02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）. |
| pinlist | The name of the pin or pins for which edge delays are to be set or read back. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma. |

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

| waveform_set | Waveform Set Number. Enter ALL for all defined waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The waveform set must have previously been defined. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. Enter PRM to select the primary waveform set. Equation specs (101 to 9999) can be used for queries. |
|---|---|
| mode | Not used. |
| specset_id | Derived as follows: |
| specset_id | 100 * equation_set_no + specset_no<br><br>Thus, the specset ID consists of 3 or 4 digits, where the first two digits specify the equation set number, and the following two digits the spec set number. |
| multi-port_spec | To query a multi-port specification, enter the name of the specification. |
| wavetable_name | The name of the wavetable. It must be enclosed in double quotes. |
| definition_string | Edge usage definition string which consists of a list of all used edges. These are given as d1 through d8 (f1 through f8 and s1 through s8 on Smart Scale cards), and r1 through r8. |
| pinlist | The name of the pin or pins for which edge usage definitions are to be read back. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98601_3.htm`。

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

| multi-port_spec | Name of a multi-port timing specification. |
|---|---|
| port_list | This query parameter specifies a list of ports that belong to the respective multi-port timing specification. |
| port | This reply parameter specifies a port that belongs to the respective multi-port timing specification. |
| event_clock_per | This reply parameter returns the event clock period of the respective port. |

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

| parameter | The parameter to be used is SKPR (SKip PRimaries). | The parameter to be used is SKPR (SKip PRimaries). |
|---|---|---|
| mode | Specifies different activation conditions. This option can take the following values: | Specifies different activation conditions. This option can take the following values: |
| mode | ON | Suppresses activation of all primary sets at the start of a functional test for the sequencing groups of the ports specified by the portlist parameter. This option serves to keep a PLL alive across functional tests. |
| mode | OFF | Allows activation for the ports specified by the portlist parameter. This is the default. |
|  | NEVER | By this option, the primary sets will always be loaded at the start of a test for all ports of the sequencing groups to which the ports specified by the portlist parameter belong. |
| portlist | In the command, specify a list of ports, separated by commas. Note that the ports are treated as representatives of their sequencing groups. Activation will be suppressed, allowed, or enforced not only for the specified ports, but for all member ports of the sequencing groups to which the specified ports belong in the current setup.<br><br>In the query, specify @@, which stands for all ports. | In the command, specify a list of ports, separated by commas. Note that the ports are treated as representatives of their sequencing groups. Activation will be suppressed, allowed, or enforced not only for the specified ports, but for all member ports of the sequencing groups to which the specified ports belong in the current setup.<br><br>In the query, specify @@, which stands for all ports. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98606_4.htm`。

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

| waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. |
|---|---|
| specset_id | Used for equation based timing. It is derived as follows:<br><br>100 * equation_set_no + specset_no<br><br>Note that if you change the period for an equation based timing setup, PCLK will only change the runtime value, not the setup value specified in the timing set. |
| multi-port_spec | In the command, you cannot enter a multi-port specification unless the specification is associated with the default port, and no other ports are configured. This restriction does not apply to the query. |
| timing_set | Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. |
| period | Enter the test system period in ns. The period range depends on the model. For the Pin Scale 800, the range is 2.5 ns to 31250 ns. All values entered (or queried regardless of query_mode) are in ns and will be rounded to nine digits after the decimal point (atto-seconds) according to the accuracy of the firmware. The power-on default value for all configured pins also depends on the model. |
| pinlist | The name of the pin or pins whose period you want to define or read back. This parameter can also include groups previously created by `DFGP`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to set or read the periods for all configured pins. If you do not use @, the firmware assumes asynchronous operation. |
| portlist | In the query, you must specify a list of ports, if you have specified a multi-port specification for the first parameter. |
| query_mode | In the query, you can specify whether the period specified by the user or the corrected period calculated by the system is to be returned. The allowed values are:<br><br>WANT: The period defined by the user is returned. This is also the default.<br><br>EXACT: The period calculated by the system is returned. |

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

| specset_id | Identifier of a timing specification, which is derived as follows:<br><br>100 * equation_set_no + specset_no | Identifier of a timing specification, which is derived as follows:<br><br>100 * equation_set_no + specset_no |
|---|---|---|
| multi-port_spec | To query a multi-port specification, enter the name of the specification. | To query a multi-port specification, enter the name of the specification. |
| wavetbl | Name of a wavetable. This requires that spec_type is set to WFT. | Name of a wavetable. This requires that spec_type is set to WFT. |
| period_div | Possible values are -1 (for standard pins), 2, 3, 4, 6, 8 (only for fast pins). | Possible values are -1 (for standard pins), 2, 3, 4, 6, 8 (only for fast pins). |
| spec_type | Possible values are: | Possible values are: |
| spec_type | TIM | Returns the period divider of the timing sets (fast pins). If not all timing sets have the same period divider for the same fast pin, PDIV? returns an error. |
| spec_type | WFT | Returns the implicit period divider of the wavetable specified as the first parameter. |
| pinlist | This parameter is only applicable to fast pins. For standard pins,`-1` is returned. | This parameter is only applicable to fast pins. For standard pins,`-1` is returned. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98684_3.htm`。

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

| clock_string | The string shows which clock source is used as reference clock. Possible values are:<br><br>EXTERNAL<br><br>INTERNAL |
|---|---|

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

| specifier | The specifier can be: | The specifier can be: |
|---|---|---|
| specifier | DPS | Loads the default power supply setup for standard DPSs. |
| specifier | FCR | Loads the default clock routing. |
| specifier | LEV | Loads the default power supply setup for standard DPSs.<br><br>Level: 0 V<br><br>Current: 50 mA<br><br>Off state: minimum current<br><br>Setup time: 0 ms<br><br>This default states are:<br><br>UHC4T<br><br>- Connect state: normal<br>- Level: 0 V<br>- Range: 4 V<br>- Clamp: 4 A<br>- Clamp-Range: 40 A<br>- Disconnect state: HIZ<br>- Voltage drop force: 250 mV<br>- Voltage drop return: 250 mV<br>- Clamp mode: limit (see `UHCM`（raw: `../02.06_Command_Reference/02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）)<br>- DUT capacitor mode: off<br><br>Fast preload: 0 ms |
| specifier | TIM | Loads the default timing setup. The settings are:<br><br>Timing Sets<br><br>- Defined Timing Sets: 1<br>- Allowed Timing Sets: 256<br><br>Waveform Sets<br><br>- Defined Waveform Sets: 1<br>- Allowed Waveform Sets: 16<br><br>Waveforms: not defined<br><br>Breakwaveform: defined<br><br>Events<br><br>- Action: NOP<br>- Timing: 0 ns<br><br>Min Period: 4 ns<br><br>- This is dependent on the test system hardware configuration.<br><br>Device Cycles: not defined<br><br>Default Device Cycle: "" |
| specifier | VEC | Loads the default vector setup. The Vector Memory contains:<br><br>No vectors<br><br>No tests (and therefore no labels)<br><br>No comments<br><br>No sequencer programs (no instructions) |
| specifier | ATR | Loads the default edge attributes.<br><br>Pin attribute: set to 0 |
| specifier | PDL | Loads the default path delay attributes.<br><br>Cable assembly delay attribute: set to 0<br><br>Fixture delay attribute: set to 0<br><br>System attribute: set to 0 |
| specifier | CAL | Loads the default calibration data.<br><br>Level calibration data<br><br>Timing calibration data |
| specifier | MTPP | Resets memory test and per-pin sequencer subroutine data. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98723_5.htm`。

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

| wf_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|
| specset_id | Derived as follows:<br><br>`100 *`equation_set_no `+ `specset_no |
| multi-port_spec | To query a multi-port specification, enter the name of the specification. |
| sclk_val | The SCLK period of the respective setup in ns. |
| ALL | Returns the SCLK values for all waveform sets. |
| PRM | Returns the value for the primary waveform set or specification (set by SPRM). |

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
| spec_type | Which specification type to use. Use: | Which specification type to use. Use: |
|---|---|---|
| spec_type | LEV | to specify levels |
| spec_type | TIM | to specify timing. This is the only possible value for multi-port specifications. |
| spec_type | ANA | to specify analog setup |
| type | The possible values and their meaning are as follows: | The possible values and their meaning are as follows: |
| type | EQN | equation sets |
| type | SPS | specsets |
| type | WVT | wavetables (equation based) |
| type | T | timing sets (equation based) |
| type | L | logical level sets (equation based) |
| type | WSET | waveform sets (non-equation based) |
| type | TSET | timing sets (non-equation based) |
| type | LSET | level sets (non-equation based) |
| type | DSET | digital sets |
| type | ASET | analog sets (for analog setup) |
| type | RSET | routing sets (for analog setup) |
| setup_comp_1 | An integer in the range 1 to 99 that refers to a setup component of a certain type (for example, an equation set or waveform set). The component type is determined by the values of spec_type and type according to the table below. If no value is specified, all components of the respective type are processed.<br><br>If you specify the name of a multi-port specification for the setup_comp_2 parameter, the setup_comp_1 parameter will be ignored. | An integer in the range 1 to 99 that refers to a setup component of a certain type (for example, an equation set or waveform set). The component type is determined by the values of spec_type and type according to the table below. If no value is specified, all components of the respective type are processed.<br><br>If you specify the name of a multi-port specification for the setup_comp_2 parameter, the setup_comp_1 parameter will be ignored. |
| setup_comp_2 | An integer that refers to a setup component of a certain type (for example, a timing set or spec set). The component type is determined by the values of spec_type and type according to the table below. If no value is specified, all components of the respective type are processed. | An integer that refers to a setup component of a certain type (for example, a timing set or spec set). The component type is determined by the values of spec_type and type according to the table below. If no value is specified, all components of the respective type are processed. |
| multi-port_spec | In a multi-port setup, enter the name of a specification instead of a component number, but only for spec_type TIM. In this case, the setup_comp_1 parameter will be ignored. | In a multi-port setup, enter the name of a specification instead of a component number, but only for spec_type TIM. In this case, the setup_comp_1 parameter will be ignored. |
| description | Maximum 60 characters. Can be also a substring of a description, in which case all components containing this string in their description are returned. | Maximum 60 characters. Can be also a substring of a description, in which case all components containing this string in their description are returned. |
| portlist | With multi-port specifications, you can specify a list of ports. If you do, only those components will be displayed that are associated with one of the specified ports.<br><br>If you specify a port list, the setup_comp_1 parameter will be ignored. | With multi-port specifications, you can specify a list of ports. If you do, only those components will be displayed that are associated with one of the specified ports.<br><br>If you specify a port list, the setup_comp_1 parameter will be ignored. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98729_4.htm`。

The following table explains the interpretation of the setup_comp_1 and setup_comp_2 parameters for every accepted value pair of the spec_type and type parameters:

| spec_type | type | setup_comp_1 | setup_comp_2 |
|---|---|---|---|
| TIM | EQN | equation set | Not allowed |
| TIM | WVT | equation set timing specset<br><br>combined into a specset_id | equation set timing specset<br><br>combined into a specset_id |
| TIM | SPS | equation set | timing specset |
| TIM | T | equation set | timing set |
| TIM | WSET | waveform set | Ignored |
| TIM | TSET | waveform set | timing set |
| LEV | EQN | equation set | Ignored |
| LEV | SPS | equation set | level specset |
| LEV | L | equation set | level set |
| LEV | LSET | level set | Ignored |
| ANA | ASET | Not allowed | analog set |
| ANA | RSET | Not allowed | routing set |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98729_4.htm`。

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

| multi-port_spec | Defines the multi-port specification for which the ports are to be queried. You can enter ALL in order to display the ports for all defined multi-port specifications. |
|---|---|
| portlist | Displays the ports to which the specification applies. |

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

 | module:resource  | Specifies the module and the resource about which information is to be returned. Currently, the following values are allowed: |
 | Level:Term  | Queries the termination modes that can be specified with the `TERM, TERM? - (TERMination mode)`（raw: `../02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） command for the specified pins and level setup. |
 | Level:Rcvrange  | Queries the minimum logic 0 threshold and the maximum logic 1 threshold that can be specified with the `RCLV, RCLV? - (ReCeive LeVel)`（raw: `../02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`） command for the specified pins and level setup. |
 | Level:UnterminatedModes  | Query returns unterminated termination modes for the given pin or pins, see pinList parameter (these modes have no leakage). |
 | Level:Pulldown  | Query the termination modes that support a pulldown resistor. |
 | Timing:FxdlRange  | Queries the range of the fixture delay, as defined by `FXDL, FXDL? - (FiXture DeLay)`（raw: `../02.06_Command_Reference/02.06.02.02.128_FXDL__FXDL__-__FiXture_DeLay.md`）, for the current system. |
 | HiRes:Mode  | Queries the possible options for determining High and Low of a differential pin. One of these options must be used for param2 of the `HROL, HROL? - (High Resolution Option and Level)`（raw: `../02.06_Command_Reference/02.06.02.02.140_HROL__HROL__-__High_Resolution_Option_and_Level.md`） command. |
 | pattern:testPoints |

Queries the minimum number of vectors that must be inserted between any of the following two points:

- Two test points,
- Vector 0 of the containing label and the first test point,
- A test point and the preceding instruction.

This applies only to testpoints defined with `TPSE, TPSE? - (Test Point SEquence)`（raw: `../02.06_Command_Reference/02.06.02.02.268_TPSE__TPSE__-__Test_Point_SEquence.md`）.

 |
 | Result:Xmodes  | Queries which x-modes are available to the result module on the current hardware. |
 | details |

Specifies a string containing a comma separated list. This parameter is required for the following module/resource combination

- Result:Mode: Specify `fail,8`
- HiRs:Mode: Specify ResultVerdictMode
 |
 | context |

Specifies further restrictions on the required information. This parameter is required for the following module/resource combinations:

- Level:Term and Level:Rcvrange to specify the level setup.

For a fixed level setup, enter a number from 1 to 99, or specify PRM to query the primary level set.

For an equation based level setup, specify a level setup ID. The level setup ID is derived as follows:

`100000 * equation_set_no + 1000 * specset_no + level_set_no`

- Timing:FxdlRange

Global is currently the only allowed value.

 |
 | answer |

Returns the requested information. In the answer for Level:Rcvrange, the minimum 0 threshold precedes the maximum 1 threshold.

Note that the structure of the replies may change from release to release.

 |
 | pinlist  | A list of pins, separated by commas. This parameter is irrelevant for Result:Mode, but must be specified for the other queries.  |  Application Error map, level setup.

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

| waveform_set_no | The identification number of the waveform set. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of waveform sets allowed - as defined by `CONF, CONF? - (CONFiguration)`（raw: `../02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md`）. |
|---|---|
| timing_specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no`<br><br>Note that the spec set ID also identifies the primary wavetable in equation based testing. |
| multi-port_spec | For a multi-port setup, specify a primary multi-port specification. |
| timing_set_no | The identification number of the timing set. Enter an integer in the range 1 to the maximum number of allowed timing sets (of the selected waveform set or timing specification). The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of timing sets allowed (as defined by `DSCP`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）).<br><br>In a multiport setup, the timing set number applies to all ports of the specification if you do not specify a port. If you do, the number applies to the specified port. |
| timing_set_list | In a multi-port setup, you can specify primary timing sets for all ports of the specification by entering a list of numbers separated by commas. The order of the timing sets must correspond to the order of the ports in the multi-port timing specification.<br><br>In the query, the numbers of the primary timing sets are returned in a list for all ports of the primary specification unless the numbers are identical for all ports or a port has been specified in the query. |
| level_set_no | The identification number of the level set. Enter an integer in the range 1 to the maximum number of allowed level sets. The maximum number is determined by `LSUS, LSUS? - (Level Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of level sets allowed (as defined by `DSCP`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）). |
| dps_set_no | The identification number of the DPS set. Enter an integer in the range 1 to the maximum number of allowed DPS sets. The maximum number is determined by `DSUS, DSUS? - (Dps Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`）. The number you enter must be less than or equal to the maximum number of DPS sets allowed (as defined by `DSCP`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）). |
| level_set_id | Derived as follows:<br><br>`100000 * equation_set_no + 1000 * specset_no + level_set_no` |
| dps_set_id | Derived as follows:<br><br>`100000 * equation_set_no + 1000 * specset_no + 1` |
| port | In a multiport setup, you can specify a port of the specification that was entered as the first parameter. In this case, the timing set number specified as the second parameter will only be applied to the specified port. The port parameter is ignored if a timing set list is specified. |

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

| spec_type | Which specification type to use. Use: | Which specification type to use. Use: |
|---|---|---|
| spec_type | LEV | to specify levels, or |
| spec_type | TIM | to specify timing. |
| equation_set_no | Equation set number. An integer in the range 0 to 256.<br><br>Use ALL to refer to all defined equation sets. Use PRM to specify the primary equation set. In the latter case, the specset_no parameter is ignored.<br><br>Equation set 0 is used for compatibility with a non-equation based testing environment. In this case, when equation set 0 is used and spec_type is LEV, specset_no is meaningless, while when equation set 0 is used and spec_type is TIM, specset_no is interpreted as the number of a waveform set. | Equation set number. An integer in the range 0 to 256.<br><br>Use ALL to refer to all defined equation sets. Use PRM to specify the primary equation set. In the latter case, the specset_no parameter is ignored.<br><br>Equation set 0 is used for compatibility with a non-equation based testing environment. In this case, when equation set 0 is used and spec_type is LEV, specset_no is meaningless, while when equation set 0 is used and spec_type is TIM, specset_no is interpreted as the number of a waveform set. |
| specset_no | Spec set number. An integer in the range 1 to 99. Use ALL to refer to all defined spec sets. | Spec set number. An integer in the range 1 to 99. Use ALL to refer to all defined spec sets. |
| multi-port_spec | In a multi-port setup, enter the name of a specification instead of a spec set number. In this case, the equation_set_no parameter must be left empty. | In a multi-port setup, enter the name of a specification instead of a spec set number. In this case, the equation_set_no parameter must be left empty. |
| status | An integer that indicates the settings of the status bits. Every set bit is represented by a power of 2, as described in the table below. The integer is the sum of these powers.<br><br>For example, if 768 = 512 + 256 is returned, then bits 8 and 9 are set, and all other bits are cleared. | An integer that indicates the settings of the status bits. Every set bit is represented by a power of 2, as described in the table below. The integer is the sum of these powers.<br><br>For example, if 768 = 512 + 256 is returned, then bits 8 and 9 are set, and all other bits are cleared. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98743_4.htm`。

Status bits for the status parameter
| Bit | Description | Value |
|---|---|---|
| 0 | Not available/defined. | 1 |
| 1 | Drive 1 period limit violation. | 2 |
| 2 | Receive 1 period limit violation. | 4 |
| 3 | Drive 2 period limit violation. | 8 |
| 4 | Receive 2 period limit violation. | 16 |
| 5 | Drive edge order violation. | 32 |
| 6 | Tri-state edge order violation. | 64 |
| 7 | Window edge order violation. | 128 |
| 8 | It is possible to modify the timing or level data with `ETIM`（raw: `../02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）(`ETDS`（raw: `../02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`）), `PCLK`（raw: `../02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`）, `CLKR`（raw: `../02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md`）, `DRLV`（raw: `../02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`）, `RCLV`（raw: `../02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`）, `TERM`（raw: `../02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`）, and `PSLV`（raw: `../02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`）. If any of these commands are executed, this bit is set automatically for the affected specset, and the restore should bring back the original SPST status. | 256 |
| 9 | Modified with `SHVL`（raw: `../02.06_Command_Reference/02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md`）. | 512 |
| 10 | Modified with `SVLR`（raw: `../02.06_Command_Reference/02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`）. | 1024 |
| 12 | Absolute range violation. | 2048 |
| 13 | Relative range violation | 4096 |
| 14 | Drive 10 period limit violation | 8192 |
| 15 | Receive 10 period limit violation | 16384 |

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

| exec_context | An execution context. For more information on execution contexts see `Using execution contexts`（raw: `../02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） . |
|---|---|
| start | Double float with up to 5 digits after the decimal point defining the value of spec_name at the start of the search. The maximum valid range is -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values defined with the spec. If the parameter is omitted, the minimum value as defined in the spec set will be used.<br><br>The start value can be greater than the stop value. In this case the search will be in the negative direction. |
| stop | Double float with up to 5 digits after the decimal point defining the value of spec_name where you want the search to end. The maximum valid range is -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values defined with the spec. If the parameter is omitted, the maximum value as defined in the spec set will be used.<br><br>The stop value can be smaller than the start value. In this case the search will be in the negative direction. |
| mode | Search mode. Use:<br><br>L to specify a linear search,<br><br>LB to specify linear/binary search,<br><br>B to specify a binary search. |
| pinlist | The name of the pin or pins for which the value of the spec variable is to be modified. This parameter may also include groups previously created by the `DFGP`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） command. If more than one pin is to be included, the names must be separated with a comma.<br><br>The @ character indicates all pins. This is the default. |
| spec_type | Which specification type to use. Use :<br><br>LEV to specify levels, or<br><br>TIM to specify timing. |
| spec_name | A string of up to 64 alphanumeric characters (upper or lower case) enclosed in double quotes.<br><br>If you use the option @port`[`@UNCHANGED`]`, (see the port parameter), you must include this extension in the double quotes, too. |
| port | In a multi-port setup, you can add a port name to the spec variable. This will have the effect that the value of the variable will be modified only for pins belonging to this port. This holds even if the variable has global scope for this port in the timing specification.<br><br>If you specify the spec variable without a port in a multi-port setup, its value will only be modified for a pin whose port has the spec variable set to global scope.<br><br>For more information on the scope of a variable see `Global and local scope of base variables`（raw: `../02.06_Command_Reference/02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）.<br><br>Note that if a port that is specified with the name of the variable it is this port on which the value of the variable will be modified. The setup pins have no influence on this.<br><br>On a Pin Scale system, the specification of a port will have an additional effect:<br><br>If spec_name is used in the definition of the port period, this port will be temporarily used as the primary port. For more information see `Modifying the period for a search or shmoo in a multi-port setup`（raw: `../02.06_Command_Reference/02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）.<br><br>This switch can be suppressed by adding @UNCHANGED to the port name. |
| stepwidth | The search step width in the unit specified with the corresponding spec. This is optional if mode is B. |
| resolution | The smallest step size to be used in the search. Especially useful in a binary search of a range of floating point numbers, where the number of values between start and stop is infinite. The unit must be the same as defined with the spec. |
| res_spec | LT (less than)<br><br>LE (less than or equal to)<br><br>EQ (equal to)<br><br>GE (greater than or equal to)<br><br>GT (greater than). |
| pass_meas_value | A double float defining the passed measured value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647.<br><br>This parameter contains the last (in a PASS/FAIL transition) or the first (in a FAIL/PASS transition) value where the test passed. |
| fail_meas_value | A double float defining the failed measured value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647.<br><br>This parameter contains the first (in a PASS/FAIL transition) or the last (in a FAIL/PASS transition) value where the test failed. |

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › STRS  -  Spec TRansition Search）

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

| spec_type | Which specification type to use. Use: | Which specification type to use. Use: |
|---|---|---|
| spec_type | LEV | to specify levels, or |
| spec_type | TIM | to specify timing. |
| equation_set_no | Equation set number. An integer in the range 1 to 99.<br><br>Use PRM to specify the primary equation set, or, in a multi-port setup, the primary specification as defined with SPRM. In this case, the specset_no parameter is ignored.<br><br>In the query, use ALL to display all equation sets.<br><br>This parameter must be omitted if a multi-port specification is specified for the thirdparameter. | Equation set number. An integer in the range 1 to 99.<br><br>Use PRM to specify the primary equation set, or, in a multi-port setup, the primary specification as defined with SPRM. In this case, the specset_no parameter is ignored.<br><br>In the query, use ALL to display all equation sets.<br><br>This parameter must be omitted if a multi-port specification is specified for the thirdparameter. |
| specset_no | Specset number. An integer in the range of 1 to 99. In the query, use ALL to select all defined specsets.<br><br>If specset_no is not set, and equation_set_no is set to ALL or a number, only the spec names in the specified equation sets, but no values are returned. | Specset number. An integer in the range of 1 to 99. In the query, use ALL to select all defined specsets.<br><br>If specset_no is not set, and equation_set_no is set to ALL or a number, only the spec names in the specified equation sets, but no values are returned. |
| multi-port_spec | In a multi-port setup, enter the name of a specification instead of a spec set number. In this case, the secondparameter must be left empty. | In a multi-port setup, enter the name of a specification instead of a spec set number. In this case, the secondparameter must be left empty. |
| spec_name | The name of a base (spec) variable. In a multi-port setup, the same variable name can occur among the spec variables of more than one port within the same specification. In this case, you can qualify the variable name by a port name in the following format<br><br><spec_name>@<port_name>,<br><br>if you want to modify the variable on that port only.<br><br>Note, however, that the scope of the variable will be set to local for the port in question after such a modification (even if it is set to global in the setup), until the setup is downloaded again.<br><br>Note also that in a multi-port setup, you cannot change the value of a variable globally (that is, without specifying a port) unless at least one of the variable instances has its scope set to global in the setup. For basic information on the local and global scope of spec variables in a multi-port setup see `Global and local scope of base variables`（raw: `../02.06_Command_Reference/02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）. | The name of a base (spec) variable. In a multi-port setup, the same variable name can occur among the spec variables of more than one port within the same specification. In this case, you can qualify the variable name by a port name in the following format<br><br><spec_name>@<port_name>,<br><br>if you want to modify the variable on that port only.<br><br>Note, however, that the scope of the variable will be set to local for the port in question after such a modification (even if it is set to global in the setup), until the setup is downloaded again.<br><br>Note also that in a multi-port setup, you cannot change the value of a variable globally (that is, without specifying a port) unless at least one of the variable instances has its scope set to global in the setup. For basic information on the local and global scope of spec variables in a multi-port setup see `Global and local scope of base variables`（raw: `../02.06_Command_Reference/02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）. |
| spec_or_equ_name | The name of a base (spec) or derived (equation) variable. An equation variable cannot be specified in the command or in a query which uses the extra parameter. | The name of a base (spec) or derived (equation) variable. An equation variable cannot be specified in the command or in a query which uses the extra parameter. |
| ALL | Requires that the actual values of both base and derived variables are returned. | Requires that the actual values of both base and derived variables are returned. |
| EQUA | Requires that the actual values of only the derived (equation) variables are returned. | Requires that the actual values of only the derived (equation) variables are returned. |
| MAX | Requires that the maximum values of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the maximum value of the specified spec variable. | Requires that the maximum values of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the maximum value of the specified spec variable. |
| MIN | Requires that the maximum of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the minimum value of the specified spec variable. | Requires that the maximum of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the minimum value of the specified spec variable. |
| SPEC | Requires that the actual values of only the base (spec) variables are returned. | Requires that the actual values of only the base (spec) variables are returned. |
| UNIT | Requires that the units of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the unit of the specified spec variable. | Requires that the units of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the unit of the specified spec variable. |
| value | Float with 5 possible decimal places. | Float with 5 possible decimal places. |
| pinlist | By this extra parameter, you can modify the runtime definitions for an individual pin. Note that you cannot retrieve the pin specific values with SVLR?.<br><br>Note You can use the pinlist parameter to modify the value of a spec variable of an individual pin, temporarily. If you make a new modification on a different spec variable, only the last modification is kept while the previous spec variable is reset to the setup value defined in the spec file. To make a permanent modification on a spec variable, specify all pins (that is, @) as the pinlist. Otherwise, to change the value of a spec variable of an individual pin permanently, you have to use a specset for each pin and modify the spec variable in that specset. | By this extra parameter, you can modify the runtime definitions for an individual pin. Note that you cannot retrieve the pin specific values with SVLR?.<br><br>Note You can use the pinlist parameter to modify the value of a spec variable of an individual pin, temporarily. If you make a new modification on a different spec variable, only the last modification is kept while the previous spec variable is reset to the setup value defined in the spec file. To make a permanent modification on a spec variable, specify all pins (that is, @) as the pinlist. Otherwise, to change the value of a spec variable of an individual pin permanently, you have to use a specset for each pin and modify the spec variable in that specset. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98764_4.htm`。

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

| waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. |
|---|---|
| specset_id | Derived as follows: `100 * `equation_set_no `+ `specset_no |
| multiport_spec | To query a multiport specification, enter the name of the specification. |
| timing_set | Timing set number. This is the highest number currently allocated to a timing set or the highest number of timing set you want to associate with a given waveform set. The number you enter must be less than or equal to the maximum number of timing sets allowed (as defined by the `DSCP`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command). This number is automatically updated to include any new timing set as it is created. At power-on only one timing set (containing the default values and belonging to the single waveform set) is available. |
| portlist | For multiport specifications, you can specify a list of the ports for which the number of the timing sets used is to be displayed. |

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

| waveform_set | Waveform set number. Enter ALL for all waveform sets in the query command. | Waveform set number. Enter ALL for all waveform sets in the query command. |
|---|---|---|
| timing_set | Timing set number. In the command, TSUX is set to this value for the specified waveform set, if the number is smaller than the current value of `TSUS`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） for this set. Otherwise, it is set to the current value of TSUS. | Timing set number. In the command, TSUX is set to this value for the specified waveform set, if the number is smaller than the current value of `TSUS`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） for this set. Otherwise, it is set to the current value of TSUS. |
| timing_set | SWAP | This command parameter causes the values set by `TSUS`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）and TSUX to be switched, that is, TSUS is set to the current value of TSUX , and TSUX to that of TSUS for the specified waveform set. |
| timing_set | NONE | This command parameter sets the value of TSUX back to 1 for the specified waveform set. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98818_3.htm`。

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

| waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|---|
| specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no` | Derived as follows:<br><br>`100 * equation_set_no + specset_no` |
| multi-port_spec | To enter a multi-port specification is only possible if the specification is associated with the default port and if no other ports are configured. | To enter a multi-port specification is only possible if the specification is associated with the default port and if no other ports are configured. |
| timing_set | Timing set number. Enter PRM for the primary timing set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. | Timing set number. Enter PRM for the primary timing set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. |
| period | Enter the test system period in ns for which you wish to check whether auto-correction will take place or not. period must be within the maximum and minimum test system periods of the model. | Enter the test system period in ns for which you wish to check whether auto-correction will take place or not. period must be within the maximum and minimum test system periods of the model. |
| pinlist | The name of the pin or pins whose period you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The @ symbol can be used to check all configured pins. | The name of the pin or pins whose period you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The @ symbol can be used to check all configured pins. |
| autocorrect | The auto-correction flag returned by the system. It can be: | The auto-correction flag returned by the system. It can be: |
| autocorrect | 0 | No auto-correction will occur. |
| autocorrect | 1 | Auto-correction will occur. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98844_3.htm`。

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

| waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|---|
| specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no` | Derived as follows:<br><br>`100 * equation_set_no + specset_no` |
| wavetable_name | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. |
| dev_cyc_name | The device cycle name. Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes.<br><br>Alternatively, you can enter: | The device cycle name. Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes.<br><br>Alternatively, you can enter: |
|  | ALL | With this specifier the command checks that:<br><br>- The pins in pinlist have exactly the same device cycle names.<br>- For each device cycle, each pin defines the device cycle with the same length. |
|  | FDC | With this specifier the command checks that the first device cycle in the device cycle definition table for each pin in the pinlist has the same length. |
| pinlist | The pin name or names whose device cycles are to be checked. If more than one pin is required, the names must be separated with a comma. The @ character can be used to read all configured pins. | The pin name or names whose device cycles are to be checked. If more than one pin is required, the names must be separated with a comma. The @ character can be used to read all configured pins. |
| dev_cyc_len | Always 1 for SmarTest 7.10. | Always 1 for SmarTest 7.10. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98846_4.htm`。

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

| waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|---|
| specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no` | Derived as follows:<br><br>`100 * equation_set_no + specset_no` |
| multi-port_spec | To query a multi-port specification, enter the name of the specification. | To query a multi-port specification, enter the name of the specification. |
| timing_set | Specifies the timing sets to be checked. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）.<br><br>In a multi-port setup, the check is performed for those pins from pinlist that belong to the same port. If you specify a number, a timing set with this number must be present in every equation set that is associated with a port of the multi-port specification. | Specifies the timing sets to be checked. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）.<br><br>In a multi-port setup, the check is performed for those pins from pinlist that belong to the same port. If you specify a number, a timing set with this number must be present in every equation set that is associated with a port of the multi-port specification. |
| pinlist | The name of the pin or pins to be checked. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.<br><br>In a multi-port setup, the pins can belong to more than one port. Only those pins are considered that belong to one of the ports of the specification. | The name of the pin or pins to be checked. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.<br><br>In a multi-port setup, the pins can belong to more than one port. Only those pins are considered that belong to one of the ports of the specification. |
| status | The system returns: | The system returns: |
| status | 0 | The timing is not the same. |
| status | 1 | The timing is the same. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98862_3.htm`。

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

| waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|
| specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no` |
| wavetable_name | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. |
| dev_cyc_name | If you specify the name of a device cycle, only this device cycle will be checked. Enter ALL for all device cycle names in the device cycle table. |
| pinlist | The name of the pin or pins whose definitions you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins. |
| status | The system returns:<br><br>0: The definitions are not the same.<br><br>1: The definitions are the same. |

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

| waveform_set_x | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|---|
| pinlist | The name of the pin or pins for which you wish to check waveform set compatibility. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins. | The name of the pin or pins for which you wish to check waveform set compatibility. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins. |
| status | The system returns: | The system returns: |
|  | 0 | The waveform sets are not compatible. |
|  | 1 | The waveform sets are compatible. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98864_3.htm`。

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

| wvf_set | Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. | Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. |
|---|---|---|
| specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no` | Derived as follows:<br><br>`100 * equation_set_no + specset_no` |
| wavetable_name | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed by double quotes. | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed by double quotes. |
| multiport_spec | To change or query a multiport specification, enter the name of the specification. | To change or query a multiport specification, enter the name of the specification. |
| wfIndex | Logical waveform index. This index identifies the logical waveform for which a physical waveform is to be created. The values specified for the DD1, DD2, ED1, and ED2 parameters must be in accordance with the format of this logical waveform. | Logical waveform index. This index identifies the logical waveform for which a physical waveform is to be created. The values specified for the DD1, DD2, ED1, and ED2 parameters must be in accordance with the format of this logical waveform. |
| DD1 and DD2 | First and second drive data parameter. These are optional parameters and contain values for both drive data and tri-state. The values you can define are: | First and second drive data parameter. These are optional parameters and contain values for both drive data and tri-state. The values you can define are: |
| DD1 and DD2 | F0N | drive 0 |
| DD1 and DD2 | F1N | drive 1 |
| DD1 and DD2 | FN0 | tri-state off |
| DD1 and DD2 | FNZ | tri-state on |
| DD1 and DD2 | F00 | drive 0, tri-state off |
| DD1 and DD2 | F0Z | drive 0, tri-state on |
| DD1 and DD2 | F10 | drive 1, tri-state off |
| DD1 and DD2 | F1Z | drive 1, tri-state on |
| ED1 and ED2 | First and second receive data parameter. These are optional parameters. The values you can define are: | First and second receive data parameter. These are optional parameters. The values you can define are: |
| ED1 and ED2 | F0 | compare to 0 |
| ED1 and ED2 | F1 | compare to 1 |
| ED1 and ED2 | FI | compare to intermediate |
| ED1 and ED2 | FX | compare to mask |
| ED1 and ED2 | FU | compare to unstable |
| ED1 and ED2 | C | capture digital data |
| ED1 and ED2 | D | do not capture digital data |
| ED1 and ED2 | The values C and D are used for selective digital capture. The following rules apply to these values:<br><br>- A waveform that is used for selective digital capture cannot contain more than one compare action. Therefore, if you specify C or D for one of ED1 or ED2, you cannot specify a value for the other Expected Data parameter.<br>- If you issue more than one instance of the WAVE command for the same logical waveform, the values you specify for the same Expected Data parameter in these different WAVE instances must be homogeneous; that is, either all or none of them must be C or D. You cannot, for instance, set ED1 to C in one of these WAVE instances, and set it to F1 in another. | The values C and D are used for selective digital capture. The following rules apply to these values:<br><br>- A waveform that is used for selective digital capture cannot contain more than one compare action. Therefore, if you specify C or D for one of ED1 or ED2, you cannot specify a value for the other Expected Data parameter.<br>- If you issue more than one instance of the WAVE command for the same logical waveform, the values you specify for the same Expected Data parameter in these different WAVE instances must be homogeneous; that is, either all or none of them must be C or D. You cannot, for instance, set ED1 to C in one of these WAVE instances, and set it to F1 in another. |
| pwfIndex | Physical waveform index. Enter an integer between 0 and 31 (0 and 255 on the Pin Scale Digital systems) for each physical waveform . The index is stored in the vector area and references the physical waveform in the physical waveform table. | Physical waveform index. Enter an integer between 0 and 31 (0 and 255 on the Pin Scale Digital systems) for each physical waveform . The index is stored in the vector area and references the physical waveform in the physical waveform table. |
| pinlist | The name of the pin or pins for which physical waveform states are to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated by commas. | The name of the pin or pins for which physical waveform states are to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated by commas. |
| ALLOW_EQ | This extra parameter allows you to define physical waveforms for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.<br><br>Note also the following:<br><br>- Every runtime change will affect all specifications that use the respective wavetable.<br>- Since the new waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.<br>- The runtime definitions are not checked for consistency. It is up to the user to ensure this. | This extra parameter allows you to define physical waveforms for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.<br><br>Note also the following:<br><br>- Every runtime change will affect all specifications that use the respective wavetable.<br>- Since the new waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.<br>- The runtime definitions are not checked for consistency. It is up to the user to ensure this. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98869_3.htm`。

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
| wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. |
|---|---|---|---|
| wavetable | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. |
| specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no` | Derived as follows:<br><br>`100 * equation_set_no + specset_no` | Derived as follows:<br><br>`100 * equation_set_no + specset_no` |
| multiport_spec | To query a multiport specification, enter the name of the specification. | To query a multiport specification, enter the name of the specification. | To query a multiport specification, enter the name of the specification. |
| wfIndex | Waveform index. Enter an integer between 0 and 31. The index references a waveform in a device cycle. For the query command you can also enter ALL for all waveform DC/DC power units. The waveform index is also used by the `WAVE`（raw: `../02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） commands. | Waveform index. Enter an integer between 0 and 31. The index references a waveform in a device cycle. For the query command you can also enter ALL for all waveform DC/DC power units. The waveform index is also used by the `WAVE`（raw: `../02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） commands. | Waveform index. Enter an integer between 0 and 31. The index references a waveform in a device cycle. For the query command you can also enter ALL for all waveform DC/DC power units. The waveform index is also used by the `WAVE`（raw: `../02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） commands. |
| a1 to a6 | Drive and compare actions, one per edge. There are drive actions that are fixed (drive to a certain fixed level) and receive actions that are fixed (compare to a certain fixed level). You can also drive to two drive data parameters (DD1 and DD2), and compare to two expected data parameters (ED1 and ED2).<br><br>Note that no tri-state actions, either defined or implied, are allowed on edges 2 or 5. For details, refer to `Restrictions for drive edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.02.01_Restrictions_for_drive_edges.md`）.<br><br>On the drive data side the actions you can define are:<br><br>- N: No action<br>- F0N: Drive 0, no tri-state action<br>- F1N: Drive 1, no tri-state action<br>- FN0: No drive action, tri-state off<br>- FNZ: No drive action, tri-state on<br>- F00: Drive 0, tri-state off<br>- F0Z: Drive 0, tri-state on<br>- F10: Drive 1, tri-state off<br>- F1Z: Drive 1, tri-state on<br>- D1N: Drive parameter 1 (DD1), no tri-state action<br>- D1N: Drive parameter 2 (DD2), no tri-state action<br>- C1N: Drive complement of parameter 1 (DD1), no tri-state action<br>- C2N: Drive complement of parameter 2 (DD2), no tri-state action<br>- DN1: No drive action, tri-state parameter 1 (DD1)<br>- DN2: No drive action, tri-state parameter 2 (DD2)<br>- D11: Drive parameter 1 (DD1), tri-state parameter 1 (DD1)<br>- C11: Drive complement of parameter 1 (DD1), tri-state parameter 1 (DD1)<br>- D22: Drive parameter 2 (DD2), tri-state parameter 2 (DD2)<br>- C22: Drive complement of parameter 2 (DD2), tri-state parameter 2 (DD2)<br><br>The following table shows which data-dependent drive actions use the driver formatter, which use the tri-state formatter, and which use both. You have to consider this when assigning parameters to the `WAVE`（raw: `../02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） command. | Drive and compare actions, one per edge. There are drive actions that are fixed (drive to a certain fixed level) and receive actions that are fixed (compare to a certain fixed level). You can also drive to two drive data parameters (DD1 and DD2), and compare to two expected data parameters (ED1 and ED2).<br><br>Note that no tri-state actions, either defined or implied, are allowed on edges 2 or 5. For details, refer to `Restrictions for drive edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.02.01_Restrictions_for_drive_edges.md`）.<br><br>On the drive data side the actions you can define are:<br><br>- N: No action<br>- F0N: Drive 0, no tri-state action<br>- F1N: Drive 1, no tri-state action<br>- FN0: No drive action, tri-state off<br>- FNZ: No drive action, tri-state on<br>- F00: Drive 0, tri-state off<br>- F0Z: Drive 0, tri-state on<br>- F10: Drive 1, tri-state off<br>- F1Z: Drive 1, tri-state on<br>- D1N: Drive parameter 1 (DD1), no tri-state action<br>- D1N: Drive parameter 2 (DD2), no tri-state action<br>- C1N: Drive complement of parameter 1 (DD1), no tri-state action<br>- C2N: Drive complement of parameter 2 (DD2), no tri-state action<br>- DN1: No drive action, tri-state parameter 1 (DD1)<br>- DN2: No drive action, tri-state parameter 2 (DD2)<br>- D11: Drive parameter 1 (DD1), tri-state parameter 1 (DD1)<br>- C11: Drive complement of parameter 1 (DD1), tri-state parameter 1 (DD1)<br>- D22: Drive parameter 2 (DD2), tri-state parameter 2 (DD2)<br>- C22: Drive complement of parameter 2 (DD2), tri-state parameter 2 (DD2)<br><br>The following table shows which data-dependent drive actions use the driver formatter, which use the tri-state formatter, and which use both. You have to consider this when assigning parameters to the `WAVE`（raw: `../02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） command. | Drive and compare actions, one per edge. There are drive actions that are fixed (drive to a certain fixed level) and receive actions that are fixed (compare to a certain fixed level). You can also drive to two drive data parameters (DD1 and DD2), and compare to two expected data parameters (ED1 and ED2).<br><br>Note that no tri-state actions, either defined or implied, are allowed on edges 2 or 5. For details, refer to `Restrictions for drive edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.02.01_Restrictions_for_drive_edges.md`）.<br><br>On the drive data side the actions you can define are:<br><br>- N: No action<br>- F0N: Drive 0, no tri-state action<br>- F1N: Drive 1, no tri-state action<br>- FN0: No drive action, tri-state off<br>- FNZ: No drive action, tri-state on<br>- F00: Drive 0, tri-state off<br>- F0Z: Drive 0, tri-state on<br>- F10: Drive 1, tri-state off<br>- F1Z: Drive 1, tri-state on<br>- D1N: Drive parameter 1 (DD1), no tri-state action<br>- D1N: Drive parameter 2 (DD2), no tri-state action<br>- C1N: Drive complement of parameter 1 (DD1), no tri-state action<br>- C2N: Drive complement of parameter 2 (DD2), no tri-state action<br>- DN1: No drive action, tri-state parameter 1 (DD1)<br>- DN2: No drive action, tri-state parameter 2 (DD2)<br>- D11: Drive parameter 1 (DD1), tri-state parameter 1 (DD1)<br>- C11: Drive complement of parameter 1 (DD1), tri-state parameter 1 (DD1)<br>- D22: Drive parameter 2 (DD2), tri-state parameter 2 (DD2)<br>- C22: Drive complement of parameter 2 (DD2), tri-state parameter 2 (DD2)<br><br>The following table shows which data-dependent drive actions use the driver formatter, which use the tri-state formatter, and which use both. You have to consider this when assigning parameters to the `WAVE`（raw: `../02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） command. |
|  | Data-dependent Drive Action | Driver | Tri-state |
|  | D1N, D2N, C1N, C2N | yes | no |
|  | DN1, DN2 | no | yes |
|  | D11, C11, D22, C22 | yes | yes |
|  | On the expected data side the actions you can define are:<br><br>- N: No action<br>- E0: Edge compare to 0<br>- E1: Edge compare to 1<br>- EI: Edge compare to intermediate<br>- EX: Edge compare to mask<br>- EU: Edge compare to unstable<br>- C: Capture digital data (selective digital capture)<br>- D: Do not capture digital data (selective digital capture)<br><br>Note that waveforms that are to be used for selective digital capture must contain exactly one compare action.<br><br>- W0: Window open with compare to 0<br>- W1: Window open with compare to 1<br>- WI: Window open with compare to intermediate<br>- WX: Window open with compare to mask<br>- WU: Window open with compare to unstable<br>- WC: Window close<br>- EE1: Edge compare to parameter 1 (ED1)<br>- EE2: Edge compare to parameter 1 (ED2)<br>- WE1: Window open with compare to parameter 1 (ED1)<br>- WE2: Window open with compare to parameter 1 (ED2) | On the expected data side the actions you can define are:<br><br>- N: No action<br>- E0: Edge compare to 0<br>- E1: Edge compare to 1<br>- EI: Edge compare to intermediate<br>- EX: Edge compare to mask<br>- EU: Edge compare to unstable<br>- C: Capture digital data (selective digital capture)<br>- D: Do not capture digital data (selective digital capture)<br><br>Note that waveforms that are to be used for selective digital capture must contain exactly one compare action.<br><br>- W0: Window open with compare to 0<br>- W1: Window open with compare to 1<br>- WI: Window open with compare to intermediate<br>- WX: Window open with compare to mask<br>- WU: Window open with compare to unstable<br>- WC: Window close<br>- EE1: Edge compare to parameter 1 (ED1)<br>- EE2: Edge compare to parameter 1 (ED2)<br>- WE1: Window open with compare to parameter 1 (ED1)<br>- WE2: Window open with compare to parameter 1 (ED2) | On the expected data side the actions you can define are:<br><br>- N: No action<br>- E0: Edge compare to 0<br>- E1: Edge compare to 1<br>- EI: Edge compare to intermediate<br>- EX: Edge compare to mask<br>- EU: Edge compare to unstable<br>- C: Capture digital data (selective digital capture)<br>- D: Do not capture digital data (selective digital capture)<br><br>Note that waveforms that are to be used for selective digital capture must contain exactly one compare action.<br><br>- W0: Window open with compare to 0<br>- W1: Window open with compare to 1<br>- WI: Window open with compare to intermediate<br>- WX: Window open with compare to mask<br>- WU: Window open with compare to unstable<br>- WC: Window close<br>- EE1: Edge compare to parameter 1 (ED1)<br>- EE2: Edge compare to parameter 1 (ED2)<br>- WE1: Window open with compare to parameter 1 (ED1)<br>- WE2: Window open with compare to parameter 1 (ED2) |
| pinlist | The name of the pin or pins for which the waveform is to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The @ symbol can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with commas. | The name of the pin or pins for which the waveform is to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The @ symbol can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with commas. | The name of the pin or pins for which the waveform is to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The @ symbol can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with commas. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98871_3.htm`。

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

|

wvf_set

 |

Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query you can also enter ALL for all waveform sets. Enter PRM to select the primary waveform set.

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed by double quotes.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

multiport_spec

 |

To query a multiport specification, enter the name of the specification.

 |
 |

wfIndex

 |

Waveform index. Enter an integer between 0 and 255. The index references a waveform in a device cycle. For the query you can also enter ALL for all waveform DC/DC power units. The waveform index is also used by the `WAVE, WAVE? - (WAVEform)`（raw: `../02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） command.

Note that the index must be specified decimally here, whereas in the wavetable, it is coded hexadecimally.

 |
 |

mode

 |

Not used.

 |
 |

definition_string

 |

Edge action definition string which consists of drive actions for the drive/ bidirectional edges only. On Pin Scale systems, there is only one drive edge type, which is denoted by di (1 鈮? i 鈮?8).

With these edges you can associate the following actions:

- N: No action
- F0N: Drive 0, no tri-state action
- F1N: Drive 1, no tri-state action
- FN0: No drive action, tri-state off
- FNZ: No drive action, tri-state on
- F00: Drive 0, tri-state off
- F0Z: Drive 0, tri-state on
- F10: Drive 1, tri-state off
- F1Z: Drive 1, tri-state on
- D1N: Drive parameter 1 (DD1), no tri-state action
- D1N: Drive parameter 2 (DD2), no tri-state action
- C1N: Drive complement of parameter 1 (DD1), no tri-state action
- C2N: Drive complement of parameter 2 (DD2), no tri-state action
- DN1: No drive action, tri-state parameter 1 (DD1)
- DN2: No drive action, tri-state parameter 2 (DD2)
- D11: Drive parameter 1 (DD1), tri-state parameter 1 (DD1)
- C11: Drive complement of parameter 1 (DD1), tri-state parameter 1 (DD1)
- D22: Drive parameter 2 (DD2), tri-state parameter 2 (DD2)
- C22: Drive complement of parameter 2 (DD2), tri-state parameter 2 (DD2)

All edges which are not explicitly set are set to N. In the query only those edges that are used are printed.

The following table shows which data-dependent drive actions use the driver formatter, which use the tri-state formatter, and which use both. You have to consider this when assigning parameters to the `WAVE`（raw: `../02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） command. See also `Specifying the actions`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.01_Specifying_the_actions.md`）.

 |
 |

 |

Data-dependent Drive Action

 |

Driver

 |

Tri-state

 |
 |

D1N, D2N, C1N, C2N

 |

yes

 |

no

 |
 |

DN1, DN2

 |

no

 |

yes

 |
 |

D11, C11, D22, C22

 |

yes

 |

yes

 |
 |

 |

On Smart Scale systems, there are two types of drive edges, denoted by fi and si (1 鈮?i 鈮?8). For both of them, only the action codes 0, 1, and N are admitted. But the Smart Scale systems also support the old di syntax. For more information see `Defining waveforms for Smart Scale pins`（raw: `../02.06_Command_Reference/02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`）.

 |
 |

 |

On the expected data side the actions you can define are:

- N: No action
- E0: Edge compare to 0
- E1: Edge compare to 1
- EI: Edge compare to intermediate
- EX: Edge compare to mask
- EU: Edge compare to unstable
- C: Capture digital data (selective digital capture)
- D: Do not capture digital data (selective digital capture)

Note that waveforms that are to be used for selective digital capture must contain exactly one compare action.

- W0: Window open with compare to 0
- W1: Window open with compare to 1
- WI: Window open with compare to intermediate
- WX: Window open with compare to mask
- WU: Window open with compare to unstable
- WC: Window close
- EE1: Edge compare to parameter 1 (ED1)
- EE2: Edge compare to parameter 1 (ED2)
- WE1: Window open with compare to parameter 1 (ED1)
- WE2: Window open with compare to parameter 1 (ED2)
 |
 |

pinlist

 |

The name of the pin or pins for which the waveform is to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The @ symbol can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.

 |
 |

ALLOW_EQ

 |

This extra parameter allows you to define or change logical waveforms for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.

Note also the following:

- Every runtime change will affect all specifications that use the respective wavetable.
- Since the new or changed waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.
- The runtime definitions are not checked for consistency. It is up to the user to ensure this.
 |

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

| wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|
| wavetable_name | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. |
| specset_id | Derived as follows:<br><br>`100 *`equation_set_no `+ `specset_no |
| multiport_spec | To change or query a multiport specification, enter the name of the specification. |
| wfIndex | Logical waveform index. Enter an integer between 0 and 31 (255 on Pin Scale systems). |
| pinlist | The name of the pin or pins for which the waveform is to be deleted. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `../02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The @ symbol can be used to specify all configured input pins. If more than one pin is to be included, the names must be separated with a comma. |
| ALLOW_EQ | This extra parameter allows you to delete a logical waveform for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.<br><br>Note also the following:<br><br>- Every runtime change will affect all specifications that use the respective wavetable.<br>- Since the new or changed waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow. |

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

| waveform_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|

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

| waveform_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `../02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|---|
| specset_id | `Derived as follows:`<br><br>`100 * equation_set_no + specset_no` | `Derived as follows:`<br><br>`100 * equation_set_no + specset_no` |
| multiport_spec | To query a multiport specification, enter the name of the specification. | To query a multiport specification, enter the name of the specification. |
| display_mode | Sets the Vector Setup display mode. This can be: | Sets the Vector Setup display mode. This can be: |
| display_mode | 0 | The "classic" display mode. A device cycle has the length of one test system cycle. |
| display_mode | 1 | The "single column" display mode. All pins use the same device cycles. |
| display_mode | 2 | The "multi column" display mode. All pins do not use the same device cycles, the device has two or more separate ports with independent signals. |
| portlist | For multiport specifications, you can specify the ports for which the vector setup display mode is to be returned. | For multiport specifications, you can specify the ports for which the vector setup display mode is to be returned. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98877_3.htm`。

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

| waveform_set | Waveform set number. This is the highest number currently allocated to a waveform set or the highest number of a set you want to load. The number you enter must not exceed the maximum number of waveform sets allowed (defined by the `DSCP`（raw: `../02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command).<br><br>This number is automatically updated to include any new waveform set as it is created. At power-on, only one waveform set (containing one timing set and default values) is available. |
|---|---|

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS 3
```

This example sets the number of used waveform sets to 3.

### Example（取自子主题 Equation based timing setup › Structure of an equation based timing setup › Data organization of equation based timing）

The following figure exemplifies the structure of equation based timing by a schematic setup:

 !`Timing Specifications`（raw: `../../../../agent-html/10596.png`）

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

 !`Timing Relationship in Example Device`（raw: `../../../../agent-html/17831.png`）

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
