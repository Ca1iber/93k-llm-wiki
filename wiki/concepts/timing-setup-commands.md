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

> 本节 **91,854 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.md>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.03.01_Defining_waveform_shapes_for_Pin_Scale_standard_pins.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.06.01_Avoiding_rounding_problems_with_the_fract___function.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.06.02_Avoiding_rounding_problems_with_different_clock_groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.01_APRM_-__Activate_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.02_BWDF__BWDF__-__Break_Waveform_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.03_BWDS__BWDS__-__Break_Waveform_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.04_CDCP__-__Cycle_Device_Cycle_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.05_CLKR__CLKR__-__CLocK_Resolution.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.06_DCDT__DCDT__-__Device_Cycle_DefaulT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.07_DCUD_-__Device_Cycle_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.08_DFCR__DFCR__-__DeFine_Clock_Routing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.09_DPRT__DPRT__-__Default_PRimary_Timing_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.10_DSCP__DSCP__-__Define_System_Control_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.11_EDDC__-__EDge_in_Device_Cycle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.13_EQFS_-__EQuation_FileS_command_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.14_EQSP__EQSP__-__EQuation_SPecification_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.15_ETDS__ETDS__-__Edge_Timing_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.16_ETIM__ETIM__-__Edge_TIMing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.17_EUDS__-__Edge_Usage_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.18_EVCK__-__EVent_ClocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.19_FTCG__FTCG__-__Functional_Test_ConfiGure.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.20_PCLK__PCLK__-__Pin_CLocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.21_PDIV__-__Period_DIVider.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.22_RCLK__-__Reference_CLocK_source.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.23_RSET_-__ReSET.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.24_SCLK__-__System_CLocK_query.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.25_SDSC__-__Set_number_DeSCriptions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.26_SPCP__-__SPeCification_Port_list.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.27_SPEC__-__SPECification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.28_SPRM__SPRM__-__Set_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.29_SPST__-__SPecset_STatus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.30_STRS__-__Spec_TRansition_Search.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.32_TSUS__TSUS__-__Timing_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.33_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.34_UPTD__UPTD__-__UP_To_Date.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.35_VCLK__-__Verify_CLocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.36_VDCG__-__Verify_Device_Cycle_for_Group.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.37_VTIM__-__Verify_TIMing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.38_VWFG__-__Verify_WaveForms_in_Groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.39_VWFS__-__Verify_WaveForm_Sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.40_WAVE__WAVE__-__WAVEform.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.41_WFDF__WFDF__-__WaveForm_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.42_WFDS__WFDS__-__WaveForm_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.43_WFUD_-__WaveForm_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.44_WRST_-__Waveform_ReSeT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.45_WSDM__WSDM__-__Waveform_Set_Display_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.46_WSUS__WSUS__-__Waveform_Sets_USed.md>`。**不是转述。**
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

| mode  | Selects the activation mode: |
 | FRC  | Forced activation. Primary sets are always activated. |
 | CNL  | Conditional activation, depends on previous activation performed by APRM or by any of the commands in the second list above. |

### Example（取自子主题 List of timing setup commands › APRM -  Activate PRiMary sets）

```
APRM CNL
```

### Parameters（取自子主题 List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

|

wvf_set

 |

Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 *` equation_set_no `+ ` specset_no

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes.

 |
 |

multiport_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

a1..a6

 |

Edge action. The actions you can define are:

 |
 |

N

 |

no action

 |
 |

F0N

 |

drive 0, no tri-state action

 |
 |

F1N

 |

drive 1, no tri-state action

 |
 |

FN0

 |

no drive action, tri-state off

 |
 |

FNZ

 |

no drive action, tri-state on

 |
 |

F00

 |

drive 0, tri-state off

 |
 |

F0Z

 |

drive 0, tri-state on

 |
 |

F10

 |

drive 1, tri-state off

 |
 |

F1Z

 |

drive 1, tri-state on

 |
 |

pinlist

 |

The name of the pin or pins for which break waveform definitions are to be made or read back. The symbol @ can be used to specify all configured input and IO pins. If more than one pin is to be included, the names must be separated with a comma.

 |

### Example（取自子主题 List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

This example defines a pulse for waveform set 1, and for pins D0 to D3, driving to 1 at edge action 4 and to 0 at edge action 5. The tri-state formatter is not used.

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

|

start_cycle

 |

This is an integer that defines the first cycle to be analyzed. The range of values for this parameter depends on the analysis mode:

- In the Start Analysis mode enter a positive value between 0 and 248. The system responds by counting cycles forwards from the first cycle of the test and returns a positive number. The Start Analysis mode is the default setting.
- In the Stop Analysis enter a negative number between -248 and -1. The system responds by counting cycles backwards relative to the end of the test at -1 cycle and returns a negative number. This mode is used by the system for Stop-on-Error tests.
 |
 |

cycle

 |

In the query, the consecutive number of the displayed cycle.

 |
 |

no_of_cycles

 |

This is an integer that defines the number of cycles to be analyzed. The range for this parameter is 0 to 1000.

 |
 |

strt_disp

 |

This parameter defines the offset of your range of interest from start_cycle. The actual display starts with the last device cycle that does not begin before start_cycle and does not end before start_cycle + strt_disp.

The purpose of this construction is to enable a correct device cycle reconstruction even if the first cycle you are interested in does not lie at a device cycle boundary (a device cycle can generate up to 16 cycles).

 |
 |

disp_length

 |

Specifies the display length in cycles. This parameter determines the end of your range of interest. The actual display stops with the last device cycle that starts before start_cycle + strt_disp + disp_length.

If this parameter is larger than no_of_cycles, it is ignored.

 |
 |

pinlist

 |

The pin name or names for which a device cycle data transfer is to be made. If more than one pin is required, the names must be separated with a comma. The @ character can be used to download data for all configured pins.

 |
 |

dev_cyc_name

 |

A reply parameter, giving the name of the reconstructed device cycle.

 |
 |

dev_cyc_len

 |

A reply parameter, giving the length of the reconstructed device cycle. For SmarTest 7.10 this is always 1.

 |
 |

DD1 and DD2

 |

Drive Data parameters. They contain values for both drive data and tri-state. The values the system returns are:

 |
 |

F00

 |

drive 0, tri-state off

 |
 |

F10

 |

drive 1, tri-state off

 |
 |

F0Z

 |

drive 0, tri-state on

 |
 |

F1Z

 |

drive 1, tri-state on

 |
 |

N

 |

Not used. Returned if no drive data parameter is set to a drive and tri-state value.

 |
 |

UC

 |

Unclear. The system may return this value to indicate that the interpretation of the device cycle for that parameter is unclear, that is, the physical waveforms are inconsistent for the device cycle.

 |
 |

ED1 and ED2

 |

Expected Data Parameters. The values the system returns are:

 |
 |

F0

 |

compare to 0

 |
 |

F1

 |

compare to 1

 |
 |

FI

 |

compare to intermediate

 |
 |

FX

 |

compare to mask

 |
 |

FU

 |

compare to unstable

 |
 |

N

 |

Not used. Returned if no expected data parameter is set to a compare value.

 |
 |

UC

 |

Unclear. The system may return this value to indicate that the interpretation of the device cycle for that parameter is unclear, that is, the physical waveforms are inconsistent for the device cycle.

 |

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

### Parameters（取自子主题 List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

|

waveform_set

 |

Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets.

 |
 |

specset_id

 |

Derived as follows:

100 * equation_set_no + specset_no

 |
 |

multi-port_spec

 |

To set or query the resolution of a multi-port timing specification, specify the name of the specification.

 |
 |

ref_period

 |

Not used. (Ignored)

 |
 |

period_res

 |

The period resolution (in ns) for the specified specification or waveform set.

If necessary, period_res is rounded to nine digits after the decimal point. The allowable maximum period resolution is the maximum tester period value. The minimum period resolution is determined by the hardware (see `Automatic calculation of period resolution for single-port setups`（raw: `02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md`）).

 |
 |

type

 |

In the query, the type parameter specifies which resolution is queried. The allowed values are:

VIRTUAL: The period resolution (period_res) is queried. This is the default.

EXACT: The clock resolution (clock_res) is queried.

 |
 |

clock_res

 |

In the answer to the query, the clock resolution is returned if type is set to EXACT in the query.

 |

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

|

waveform_set

 |

Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

dev_cyc_name

 |

The device cycle name. Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes. Enter ALL for the removal of all device cycles from the device cycle table.

 |
 |

pinlist

 |

The name of the pin or pins for which device cycle definitions are to be deleted. This parameter can also include groups previously created by the `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.

 |

### Example（取自子主题 List of timing setup commands › DCUD -  Device Cycle UnDefine）

```
DCUD 1,"WRITE"
```

This example deletes the device cycle `WRITE` for waveform set 1 from the device cycle table.

### Parameters（取自子主题 List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

|

source_group

 |

specifies the hardware group whose local clock is to be routed to dest_group. The format is Gx, where x is the group number.

 |
 |

dest_group

 |

specifies the hardware group whose inherited clock is to be changed.

 |

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

### Parameters（取自子主题 List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

|

waveform_set

 |

Waveform set number.

 |
 |

specset_id

 |

Derived as follows:

100 * equation_set_no + spec_set_no

Note that the spec set ID identifies the primary wavetable in equation based testing.

 |
 |

multi-port_spec

 |

In a multi-port setup, a primary multiport specification can be specified.

 |
 |

timing_set

 |

The identification number of the timing set. Enter an integer in the range 1 to the maximum number of allowed timing sets (of the selected waveform set or timing specification). The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of timing sets allowed (as defined by DSCP).

In a multiport setup, the timing set number applies to all ports of the specification if no port is specified. Otherwise, the number applies to the specified port.

 |
 |

timing_set_list

 |

In a multi-port setup, you can specify primary timing sets for all ports of the specification by entering a list of numbers separated by commas.

In the query, the numbers of the primary timing sets are returned in a list for all ports of the primary specification unless the numbers are identical for all ports or a port has been specified in the query.

 |
 |

port

 |

In a multi-port setup, you can specify a port of the specification that was entered as the first parameter. In this case, the timing set number specified as the second parameter will only be applied to the specified port. The port parameter is ignored if a timing set list is specified.

 |

### Example（取自子主题 List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT?
```

returns:

```
DPRT 3,4
```

On sending a query the system reports that the default primary waveform set is 3 and the default primary timing set is 4.

### Parameters（取自子主题 List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

| device_cycle  | The device_cycle parameter is an integer that defines the absolute maximum number of device cycles that you can create for one pin.

Default: 256

Maximum: 16384

Note that the total number of device cycles gets evenly divided between the combined number of waveform sets and wavetables. If you use the default values, then 256 device cycles divides into the total number of 32 `waveform sets and wavetables`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） to give you 8 device cycles per waveform set/wavetable. If you choose values that do not divide evenly, then the number of device cycles will be rounded up to the next multiple of the `waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） parameter.

 |
 | devicecycle_set |

The devicecycle_set parameter is an integer that defines the maximum number of device cycle sets that you can create. Device cycle sets are needed for selective digital capture.

Default: 1

Maximum: 128

 |
 | dps_set |

The dps_set parameter is an integer that defines the maximum number of DPS sets you can create.

Default: 32

Maximum: 256

 |
 | level_set |

The level_set parameter is an integer that defines the combined total of level sets for fixed and equation based levels that you can create.

Default: 32

Maximum: 256

 |
 | period_res_prec |

This parameter defines the precision with which the period resolution is calculated by the system. It has no effect on a user defined period resolution (using, for example, the period_res keyword in the equation set).

The default is 4, if the .technology file does not contain this parameter.

If it does, the value of the .technology file is the default.

This value is set to 9, the greatest possible value, when a device is created.

 |
 |

pmu_set

 |

The pmu_set parameter is an integer that defines the maximum number of actions that can be contained in all measurement sets of all PPMU DC sets.

Default: 1024

Maximum: 12800

 |
 | routing_set |

Defines the number of routing sets managed by the firmware, provided by the MCD.

Default: 256

Maximum: 512

 |
 | timing_set |

The timing_set parameter is an integer that defines the maximum combined total of timing sets for fixed and equation based timing you can create.

Default: 256

Maximum: 999

The number of timing sets must be equal to or greater than the number of waveform sets, as there must be at least one timing set per waveform set.

 |
 | waveform_set |

The waveform_set parameter defines the maximum combined total of waveform sets (fixed timing) and wavetables (equation based timing) you can create. Thus, if you specify a value of 32, you could, for example, create 10 waveform sets and 22 wavetables.

Default: 32

Maximum: 128

 |

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

### Syntax（取自子主题 List of timing setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]
```

### Parameters（取自子主题 List of timing setup commands › EQFS -  EQuation FileS command transfer）

|

spec_type

 |

Which specification to use:

 |
 |

LEV

 |

to specify levels, or

 |
 |

TIM

 |

to specify timing.

 |
 |

part

 |

Which part of the specification type to use:

 |
 |

WVT

 |

to specify wavetable (only for spec_type = TIM),

 |
 |

EQN

 |

to specify equations, or

 |
 |

SPS

 |

to specify specs.

 |
 |

operation

 |

Use LOAD or SAVE.

 |
 |

eqn_filename

 |

The absolute filename of the temporary equation based timing file.

 |
 |

error_filename

 |

The absolute filename of the file to which error reports are written.

Use UI_REPORT to direct error reports to the report window.

If this parameter is not specified, only a summarized error message is reported.

 |

### Example（取自子主题 List of timing setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

This example loads the level equation file from /tmp/level_equation.

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

### Parameters（取自子主题 List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query, you can also enter ALL for all waveform sets.

 |
 |

specset_id

 |

Derived as follows:

`100 *`equation_set_no `+ `specset_no

 |
 |

multi-port_spec

 |

For a multi-port setup, specify the name of a multi-port specification.

Note that the multi-port specification uniquely determines an equation set for every pin of pinlist, because no pin can belong to more than one port within a multi-port specification.

 |
 |

timing_set

 |

Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by TSUS.

 |
 |

mode

 |

The operating mode. For the query, you can enter ALL for all modes or BIDIR for bidirectional mode, that is, for edges that serve both as drive and receive edges.

With fast pins, you can specify the mode DELTA for both the command and the query. In this mode, the delays specified for edges with an index > 1 are interpreted as offsets from the calculated default values.

 |
 |

definition_string

 |

The definition string consists of a sequence of items each of which associates a delay with a drive or compare edge. On Pin Scale 800/3600 boards, drive edges are denoted by dn. On Pin Scale 9G boards, there are two kinds of drive edges, which are denoted by fn and sn, respectively; for details see `Defining waveforms for Pin Scale 9G pins`（raw: `02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`）. You can also use the dn notation for Pin Scale 9G channels, but mixing both notations in one string is not allowed. Receive edges are always denoted by rn.

Unless you employ the pdiv statement for fast pins (see below), all edges which are not explicitly set remain unchanged.

The range of the edge delay is -8000 ns to +24000 ns (or -4 to +12 test system periods) for the Pin Scale 3600/800.

On Pin Scale 800/3600 boards, the restrictions for edge ordering must be observed both in fixed and equation based timing. For example, you cannot assign a greater delay to d1 than to d3 if d1 precedes d3 in a waveform definition. For more information, see `Selecting and ordering edges`（raw: `02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）.

Note that with equation based timing, ETDS returns no error message when the edge order restrictions are violated.

On Pin Scale 9G boards, ordering of drive edges is not restricted in any way.

 |
 |

 |

Special Rules for Fast Pins:

If a pin is configured as a fast pin in the context of the specification given by the first parameter, you can specify the period divider at the start of the definition string. The format is pdiv:n, where n must be the same value as the period_div value of the pins in pinlist within the timing set specified by the timing_set parameter.

If you specify pdiv:nand a delay for the first edge, ETDS calculates delays for the following n-1 edges except those that are specified explicitly in the string. Note that for n = 3, the edges with index 1, 3, 5 are used for internal reasons.

If you omit either pdiv or the first edge, only the specified edges are modified. However, with receive edges this is only possible for r1.

The calculated delays are determined for the ith edge by the following formula:

 1st_edge_delay + (i-1) * (period/pdiv)

1st_edge_delay is the delay specified for the first edge (d1 or r1; the generic notation e1 is not allowed for fast pins). If the first edge is not specified in the string, its delay is set to 0. An example for the calculation will be given below.

Note that when both the period divider and a delay for the first edge are present in the definition string, then the delays for all the edges required by the period divider will be overwritten.

When a delay is explicitly specified for one of the edges, this delay overrides the calculated default. There are two formats to specify overrides. You can either define absolute delays or the offsets from the default delays.

If you want to use the second, relative format, you must specify DELTA for the modeparameter. Note that you can also specify negative offsets in the DELTA mode.

 |
 |

pinlist

 |

The name of the pin or pins for which edge delays are to be set or read back. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.

In a multi-port setup, every pin must belong to a port of the specified specification.

 |

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

|

waveform_set

 |

Waveform Set Number. Enter ALL for all defined waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The waveform set must have previously been defined. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. Enter PRM to select the primary waveform set. Equation specs (101 to 9999) can be used for queries.

 |
 |

mode

 |

Not used.

 |
 |

specset_id

 |

Derived as follows:

 |
 |

100 * equation_set_no + specset_no

Thus, the specset ID consists of 3 or 4 digits, where the first two digits specify the equation set number, and the following two digits the spec set number.

 |
 |

multi-port_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

wavetable_name

 |

The name of the wavetable. It must be enclosed in double quotes.

 |
 |

definition_string

 |

Edge usage definition string which consists of a list of all used edges. These are given as d1 through d8 (f1 through f8 and s1 through s8 on Smart Scale cards), and r1 through r8.

 |
 |

pinlist

 |

The name of the pin or pins for which edge usage definitions are to be read back. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.

 |

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

|

multi-port_spec

 |

Name of a multi-port timing specification.

 |
 |

port_list

 |

This query parameter specifies a list of ports that belong to the respective multi-port timing specification.

 |
 |

port

 |

This reply parameter specifies a port that belongs to the respective multi-port timing specification.

 |
 |

event_clock_per

 |

This reply parameter returns the event clock period of the respective port.

 |

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

 |

parameter

 |

The parameter to be used is SKPR (SKip PRimaries).

 |
 |

mode

 |

Specifies different activation conditions. This option can take the following values:

 |
 |

ON

 |

Suppresses activation of all primary sets at the start of a functional test for the sequencing groups of the ports specified by the portlist parameter. This option serves to keep a PLL alive across functional tests.

 |
 |

OFF

 |

Allows activation for the ports specified by the portlist parameter. This is the default.

 |
 |

 |

NEVER

 |

By this option, the primary sets will always be loaded at the start of a test for all ports of the sequencing groups to which the ports specified by the portlist parameter belong.

 |
 |

portlist

 |

In the command, specify a list of ports, separated by commas. Note that the ports are treated as representatives of their sequencing groups. Activation will be suppressed, allowed, or enforced not only for the specified ports, but for all member ports of the sequencing groups to which the specified ports belong in the current setup.

In the query, specify @@, which stands for all ports.

 |

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

### Parameters（取自子主题 List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets.

 |
 |

specset_id

 |

Used for equation based timing. It is derived as follows:

100 * equation_set_no + specset_no

Note that if you change the period for an equation based timing setup, PCLK will only change the runtime value, not the setup value specified in the timing set.

 |
 |

multi-port_spec

 |

In the command, you cannot enter a multi-port specification unless the specification is associated with the default port, and no other ports are configured. This restriction does not apply to the query.

 |
 |

timing_set

 |

Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）.

 |
 |

period

 |

Enter the test system period in ns. The period range depends on the model. For the Pin Scale 800, the range is 2.5 ns to 31250 ns. All values entered (or queried regardless of query_mode) are in ns and will be rounded to nine digits after the decimal point (atto-seconds) according to the accuracy of the firmware. The power-on default value for all configured pins also depends on the model.

 |
 |

pinlist

 |

The name of the pin or pins whose period you want to define or read back. This parameter can also include groups previously created by `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to set or read the periods for all configured pins. If you do not use @, the firmware assumes asynchronous operation.

 |
 |

portlist

 |

In the query, you must specify a list of ports, if you have specified a multi-port specification for the first parameter.

 |
 |

query_mode

 |

In the query, you can specify whether the period specified by the user or the corrected period calculated by the system is to be returned. The allowed values are:

WANT: The period defined by the user is returned. This is also the default.

EXACT: The period calculated by the system is returned.

 |

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

|

specset_id

 |

Identifier of a timing specification, which is derived as follows:

100 * equation_set_no + specset_no

 |
 |

multi-port_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

wavetbl

 |

Name of a wavetable. This requires that spec_type is set to WFT.

 |
 |

period_div

 |

Possible values are -1 (for standard pins), 2, 3, 4, 6, 8 (only for fast pins).

 |
 |

spec_type

 |

Possible values are:

 |
 |

TIM

 |

Returns the period divider of the timing sets (fast pins). If not all timing sets have the same period divider for the same fast pin, PDIV? returns an error.

 |
 |

WFT

 |

Returns the implicit period divider of the wavetable specified as the first parameter.

 |
 |

pinlist

 |

This parameter is only applicable to fast pins. For standard pins,`-1` is returned.

 |

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

|

clock_string

 |

The string shows which clock source is used as reference clock. Possible values are:

EXTERNAL

INTERNAL

 |

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

|

specifier

 |

The specifier can be:

 |
 |

DPS

 |

Loads the default power supply setup for standard DPSs.

 |
 |

FCR

 |

Loads the default clock routing.

 |
 |

LEV

 |

Loads the default power supply setup for standard DPSs.

Level: 0 V

Current: 50 mA

Off state: minimum current

Setup time: 0 ms

This default states are:

UHC4T

- Connect state: normal
- Level: 0 V
- Range: 4 V
- Clamp: 4 A
- Clamp-Range: 40 A
- Disconnect state: HIZ
- Voltage drop force: 250 mV
- Voltage drop return: 250 mV
- Clamp mode: limit (see `UHCM`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）)
- DUT capacitor mode: off

Fast preload: 0 ms

 |
 |

TIM

 |

Loads the default timing setup. The settings are:

Timing Sets

- Defined Timing Sets: 1
- Allowed Timing Sets: 256

Waveform Sets

- Defined Waveform Sets: 1
- Allowed Waveform Sets: 16

Waveforms: not defined

Breakwaveform: defined

Events

- Action: NOP
- Timing: 0 ns

Min Period: 4 ns

- This is dependent on the test system hardware configuration.

Device Cycles: not defined

Default Device Cycle: ""

 |
 |

VEC

 |

Loads the default vector setup. The Vector Memory contains:

No vectors

No tests (and therefore no labels)

No comments

No sequencer programs (no instructions)

 |
 |

ATR

 |

Loads the default edge attributes.

Pin attribute: set to 0

 |
 |

PDL

 |

Loads the default path delay attributes.

Cable assembly delay attribute: set to 0

Fixture delay attribute: set to 0

System attribute: set to 0

 |
 |

CAL

 |

Loads the default calibration data.

Level calibration data

Timing calibration data

 |
 |

MTPP

 |

Resets memory test and per-pin sequencer subroutine data.

 |

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

|

wf_set

 |

Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 *`equation_set_no `+ `specset_no

 |
 |

multi-port_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

sclk_val

 |

The SCLK period of the respective setup in ns.

 |
 |

ALL

 |

Returns the SCLK values for all waveform sets.

 |
 |

PRM

 |

Returns the value for the primary waveform set or specification (set by SPRM).

 |

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
 |

spec_type

 |

Which specification type to use. Use:

 |
 |

LEV

 |

to specify levels

 |
 |

TIM

 |

to specify timing. This is the only possible value for multi-port specifications.

 |
 |

ANA

 |

to specify analog setup

 |
 |

type

 |

The possible values and their meaning are as follows:

 |
 |

EQN

 |

equation sets

 |
 |

SPS

 |

specsets

 |
 |

WVT

 |

wavetables (equation based)

 |
 |

T

 |

timing sets (equation based)

 |
 |

L

 |

logical level sets (equation based)

 |
 |

WSET

 |

waveform sets (non-equation based)

 |
 |

TSET

 |

timing sets (non-equation based)

 |
 |

LSET

 |

level sets (non-equation based)

 |
 |

DSET

 |

digital sets

 |
 |

ASET

 |

analog sets (for analog setup)

 |
 |

RSET

 |

routing sets (for analog setup)

 |
 |

setup_comp_1

 |

An integer in the range 1 to 99 that refers to a setup component of a certain type (for example, an equation set or waveform set). The component type is determined by the values of spec_type and type according to the table below. If no value is specified, all components of the respective type are processed.

If you specify the name of a multi-port specification for the setup_comp_2 parameter, the setup_comp_1 parameter will be ignored.

 |
 |

setup_comp_2

 |

An integer that refers to a setup component of a certain type (for example, a timing set or spec set). The component type is determined by the values of spec_type and type according to the table below. If no value is specified, all components of the respective type are processed.

 |
 |

multi-port_spec

 |

In a multi-port setup, enter the name of a specification instead of a component number, but only for spec_type TIM. In this case, the setup_comp_1 parameter will be ignored.

 |
 |

description

 |

Maximum 60 characters. Can be also a substring of a description, in which case all components containing this string in their description are returned.

 |
 |

portlist

 |

With multi-port specifications, you can specify a list of ports. If you do, only those components will be displayed that are associated with one of the specified ports.

If you specify a port list, the setup_comp_1 parameter will be ignored.

 |

The following table explains the interpretation of the setup_comp_1 and setup_comp_2 parameters for every accepted value pair of the spec_type and type parameters:

 |

spec_type

 |

type

 |

setup_comp_1

 |

setup_comp_2

 |
 |

TIM

 |

EQN

 |

equation set

 |

Not allowed

 |
 |

TIM

 |

WVT

 |

equation set timing specset

 combined into a specset_id

 |
 |

TIM

 |

SPS

 |

equation set

 |

timing specset

 |
 |

TIM

 |

T

 |

equation set

 |

timing set

 |
 |

TIM

 |

WSET

 |

waveform set

 |

Ignored

 |
 |

TIM

 |

TSET

 |

waveform set

 |

timing set

 |
 |

LEV

 |

EQN

 |

equation set

 |

Ignored

 |
 |

LEV

 |

SPS

 |

equation set

 |

level specset

 |
 |

LEV

 |

L

 |

equation set

 |

level set

 |
 |

LEV

 |

LSET

 |

level set

 |

Ignored

 |
 |

ANA

 |

ASET

 |

Not allowed

 |

analog set

 |
 |

ANA

 |

RSET

 |

Not allowed

 |

routing set

 |

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

|

multi-port_spec

 |

Defines the multi-port specification for which the ports are to be queried. You can enter ALL in order to display the ports for all defined multi-port specifications.

 |
 |

portlist

 |

Displays the ports to which the specification applies.

 |

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

 | module:resource  | Specifies the module and the resource about which information is to be returned. Currently, the following values are allowed: |
 | Level:Term  | Queries the termination modes that can be specified with the `TERM, TERM? - (TERMination mode)`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） command for the specified pins and level setup. |
 | Level:Rcvrange  | Queries the minimum logic 0 threshold and the maximum logic 1 threshold that can be specified with the `RCLV, RCLV? - (ReCeive LeVel)`（raw: `02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`） command for the specified pins and level setup. |
 | Level:UnterminatedModes  | Query returns unterminated termination modes for the given pin or pins, see pinList parameter (these modes have no leakage). |
 | Level:Pulldown  | Query the termination modes that support a pulldown resistor. |
 | Timing:FxdlRange  | Queries the range of the fixture delay, as defined by `FXDL, FXDL? - (FiXture DeLay)`（raw: `02.06.02.02.128_FXDL__FXDL__-__FiXture_DeLay.md`）, for the current system. |
 | HiRes:Mode  | Queries the possible options for determining High and Low of a differential pin. One of these options must be used for param2 of the `HROL, HROL? - (High Resolution Option and Level)`（raw: `02.06.02.02.140_HROL__HROL__-__High_Resolution_Option_and_Level.md`） command. |
 | pattern:testPoints |

Queries the minimum number of vectors that must be inserted between any of the following two points:

- Two test points,
- Vector 0 of the containing label and the first test point,
- A test point and the preceding instruction.

This applies only to testpoints defined with `TPSE, TPSE? - (Test Point SEquence)`（raw: `02.06.02.02.268_TPSE__TPSE__-__Test_Point_SEquence.md`）.

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

### Parameters（取自子主题 List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

|

waveform_set_no

 |

The identification number of the waveform set. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of waveform sets allowed - as defined by `CONF, CONF? - (CONFiguration)`（raw: `02.06.02.02.31_CONF__CONF__-__CONFiguration.md`）.

 |
 |

timing_specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

Note that the spec set ID also identifies the primary wavetable in equation based testing.

 |
 |

multi-port_spec

 |

For a multi-port setup, specify a primary multi-port specification.

 |
 |

timing_set_no

 |

The identification number of the timing set. Enter an integer in the range 1 to the maximum number of allowed timing sets (of the selected waveform set or timing specification). The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of timing sets allowed (as defined by `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）).

In a multiport setup, the timing set number applies to all ports of the specification if you do not specify a port. If you do, the number applies to the specified port.

 |
 |

timing_set_list

 |

In a multi-port setup, you can specify primary timing sets for all ports of the specification by entering a list of numbers separated by commas. The order of the timing sets must correspond to the order of the ports in the multi-port timing specification.

In the query, the numbers of the primary timing sets are returned in a list for all ports of the primary specification unless the numbers are identical for all ports or a port has been specified in the query.

 |
 |

level_set_no

 |

The identification number of the level set. Enter an integer in the range 1 to the maximum number of allowed level sets. The maximum number is determined by `LSUS, LSUS? - (Level Sets USed)`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of level sets allowed (as defined by `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）).

 |
 |

dps_set_no

 |

The identification number of the DPS set. Enter an integer in the range 1 to the maximum number of allowed DPS sets. The maximum number is determined by `DSUS, DSUS? - (Dps Sets USed)`（raw: `02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`）. The number you enter must be less than or equal to the maximum number of DPS sets allowed (as defined by `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）).

 |
 |

level_set_id

 |

Derived as follows:

`100000 * equation_set_no + 1000 * specset_no + level_set_no`

 |
 |

dps_set_id

 |

Derived as follows:

`100000 * equation_set_no + 1000 * specset_no + 1`

 |
 |

port

 |

In a multiport setup, you can specify a port of the specification that was entered as the first parameter. In this case, the timing set number specified as the second parameter will only be applied to the specified port. The port parameter is ignored if a timing set list is specified.

 |

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

|

spec_type

 |

Which specification type to use. Use:

 |
 |

LEV

 |

to specify levels, or

 |
 |

TIM

 |

to specify timing.

 |
 |

equation_set_no

 |

Equation set number. An integer in the range 0 to 256.

Use ALL to refer to all defined equation sets. Use PRM to specify the primary equation set. In the latter case, the specset_no parameter is ignored.

Equation set 0 is used for compatibility with a non-equation based testing environment. In this case, when equation set 0 is used and spec_type is LEV, specset_no is meaningless, while when equation set 0 is used and spec_type is TIM, specset_no is interpreted as the number of a waveform set.

 |
 |

specset_no

 |

Spec set number. An integer in the range 1 to 99. Use ALL to refer to all defined spec sets.

 |
 |

multi-port_spec

 |

In a multi-port setup, enter the name of a specification instead of a spec set number. In this case, the equation_set_no parameter must be left empty.

 |
 |

status

 |

An integer that indicates the settings of the status bits. Every set bit is represented by a power of 2, as described in the table below. The integer is the sum of these powers.

For example, if 768 = 512 + 256 is returned, then bits 8 and 9 are set, and all other bits are cleared.

 |

Status bits for the status parameter
 |

Bit

 |

Description

 |

Value

 |
 |

0

 |

Not available/defined.

 |

1

 |
 |

1

 |

Drive 1 period limit violation.

 |

2

 |
 |

2

 |

Receive 1 period limit violation.

 |

4

 |
 |

3

 |

Drive 2 period limit violation.

 |

8

 |
 |

4

 |

Receive 2 period limit violation.

 |

16

 |
 |

5

 |

Drive edge order violation.

 |

32

 |
 |

6

 |

Tri-state edge order violation.

 |

64

 |
 |

7

 |

Window edge order violation.

 |

128

 |
 |

8

 |

It is possible to modify the timing or level data with `ETIM`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）(`ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`）), `PCLK`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`）, `CLKR`（raw: `02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md`）, `DRLV`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`）, `RCLV`（raw: `02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`）, `TERM`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`）, and `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`）. If any of these commands are executed, this bit is set automatically for the affected specset, and the restore should bring back the original SPST status.

 |

256

 |
 |

9

 |

Modified with `SHVL`（raw: `02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md`）.

 |

512

 |
 |

10

 |

Modified with `SVLR`（raw: `02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`）.

 |

1024

 |
 |

12

 |

Absolute range violation.

 |

2048

 |
 |

13

 |

Relative range violation

 |

4096

 |
 |

14

 |

Drive 10 period limit violation

 |

8192

 |
 |

15

 |

Receive 10 period limit violation

 |

16384

 |

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

|

exec_context

 |

An execution context. For more information on execution contexts see `Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） .

 |
 |

start

 |

Double float with up to 5 digits after the decimal point defining the value of spec_name at the start of the search. The maximum valid range is -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values defined with the spec. If the parameter is omitted, the minimum value as defined in the spec set will be used.

The start value can be greater than the stop value. In this case the search will be in the negative direction.

 |
 |

stop

 |

Double float with up to 5 digits after the decimal point defining the value of spec_name where you want the search to end. The maximum valid range is -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values defined with the spec. If the parameter is omitted, the maximum value as defined in the spec set will be used.

The stop value can be smaller than the start value. In this case the search will be in the negative direction.

 |
 |

mode

 |

Search mode. Use:

L to specify a linear search,

LB to specify linear/binary search,

B to specify a binary search.

 |
 |

pinlist

 |

The name of the pin or pins for which the value of the spec variable is to be modified. This parameter may also include groups previously created by the `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） command. If more than one pin is to be included, the names must be separated with a comma.

The @ character indicates all pins. This is the default.

 |
 |

spec_type

 |

Which specification type to use. Use :

LEV to specify levels, or

TIM to specify timing.

 |
 |

spec_name

 |

A string of up to 64 alphanumeric characters (upper or lower case) enclosed in double quotes.

If you use the option @port`[`@UNCHANGED`]`, (see the port parameter), you must include this extension in the double quotes, too.

 |
 |

port

 |

In a multi-port setup, you can add a port name to the spec variable. This will have the effect that the value of the variable will be modified only for pins belonging to this port. This holds even if the variable has global scope for this port in the timing specification.

If you specify the spec variable without a port in a multi-port setup, its value will only be modified for a pin whose port has the spec variable set to global scope.

For more information on the scope of a variable see `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）.

Note that if a port that is specified with the name of the variable it is this port on which the value of the variable will be modified. The setup pins have no influence on this.

On a Pin Scale system, the specification of a port will have an additional effect:

If spec_name is used in the definition of the port period, this port will be temporarily used as the primary port. For more information see `Modifying the period for a search or shmoo in a multi-port setup`（raw: `02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）.

This switch can be suppressed by adding @UNCHANGED to the port name.

 |
 |

stepwidth

 |

The search step width in the unit specified with the corresponding spec. This is optional if mode is B.

 |
 |

resolution

 |

The smallest step size to be used in the search. Especially useful in a binary search of a range of floating point numbers, where the number of values between start and stop is infinite. The unit must be the same as defined with the spec.

 |
 |

res_spec

 |

LT (less than)

LE (less than or equal to)

EQ (equal to)

GE (greater than or equal to)

GT (greater than).

 |
 |

pass_meas_value

 |

A double float defining the passed measured value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647.

This parameter contains the last (in a PASS/FAIL transition) or the first (in a FAIL/PASS transition) value where the test passed.

 |
 |

fail_meas_value

 |

A double float defining the failed measured value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647.

This parameter contains the first (in a PASS/FAIL transition) or the last (in a FAIL/PASS transition) value where the test failed.

 |

### Example（取自子主题 List of timing setup commands › STRS  -  Spec TRansition Search）

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

### Parameters（取自子主题 List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

|

spec_type

 |

Which specification type to use. Use:

 |
 |

LEV

 |

to specify levels, or

 |
 |

TIM

 |

to specify timing.

 |
 |

equation_set_no

 |

Equation set number. An integer in the range 1 to 99.

Use PRM to specify the primary equation set, or, in a multi-port setup, the primary specification as defined with SPRM. In this case, the specset_no parameter is ignored.

In the query, use ALL to display all equation sets.

This parameter must be omitted if a multi-port specification is specified for the thirdparameter.

 |
 |

specset_no

 |

Specset number. An integer in the range of 1 to 99. In the query, use ALL to select all defined specsets.

If specset_no is not set, and equation_set_no is set to ALL or a number, only the spec names in the specified equation sets, but no values are returned.

 |
 |

multi-port_spec

 |

In a multi-port setup, enter the name of a specification instead of a spec set number. In this case, the secondparameter must be left empty.

 |
 |

spec_name

 |

The name of a base (spec) variable. In a multi-port setup, the same variable name can occur among the spec variables of more than one port within the same specification. In this case, you can qualify the variable name by a port name in the following format

<spec_name>@<port_name>,

if you want to modify the variable on that port only.

Note, however, that the scope of the variable will be set to local for the port in question after such a modification (even if it is set to global in the setup), until the setup is downloaded again.

Note also that in a multi-port setup, you cannot change the value of a variable globally (that is, without specifying a port) unless at least one of the variable instances has its scope set to global in the setup. For basic information on the local and global scope of spec variables in a multi-port setup see `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）.

 |
 |

spec_or_equ_name

 |

The name of a base (spec) or derived (equation) variable. An equation variable cannot be specified in the command or in a query which uses the extra parameter.

 |
 |

ALL

 |

Requires that the actual values of both base and derived variables are returned.

 |
 |

EQUA

 |

Requires that the actual values of only the derived (equation) variables are returned.

 |
 |

MAX

 |

Requires that the maximum values of all the base (spec) variables are returned.

This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the maximum value of the specified spec variable.

 |
 |

MIN

 |

Requires that the maximum of all the base (spec) variables are returned.

This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the minimum value of the specified spec variable.

 |
 |

SPEC

 |

Requires that the actual values of only the base (spec) variables are returned.

 |
 |

UNIT

 |

Requires that the units of all the base (spec) variables are returned.

This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the unit of the specified spec variable.

 |
 |

value

 |

Float with 5 possible decimal places.

 |
 |

pinlist

 |

By this extra parameter, you can modify the runtime definitions for an individual pin. Note that you cannot retrieve the pin specific values with SVLR?.

 Note You can use the pinlist parameter to modify the value of a spec variable of an individual pin, temporarily. If you make a new modification on a different spec variable, only the last modification is kept while the previous spec variable is reset to the setup value defined in the spec file. To make a permanent modification on a spec variable, specify all pins (that is, @) as the pinlist. Otherwise, to change the value of a spec variable of an individual pin permanently, you have to use a specset for each pin and modify the spec variable in that specset. |

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

### Parameters（取自子主题 List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

|

waveform_set

 |

Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets.

 |
 |

specset_id

 |

Derived as follows: `100 * `equation_set_no `+ `specset_no

 |
 |

multiport_spec

 |

To query a multiport specification, enter the name of the specification.

 |
 |

timing_set

 |

Timing set number. This is the highest number currently allocated to a timing set or the highest number of timing set you want to associate with a given waveform set. The number you enter must be less than or equal to the maximum number of timing sets allowed (as defined by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command). This number is automatically updated to include any new timing set as it is created. At power-on only one timing set (containing the default values and belonging to the single waveform set) is available.

 |
 |

portlist

 |

For multiport specifications, you can specify a list of the ports for which the number of the timing sets used is to be displayed.

 |

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

### Parameters（取自子主题 List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

|

waveform_set

 |

Waveform set number. Enter ALL for all waveform sets in the query command.

 |
 |

timing_set

 |

Timing set number. In the command, TSUX is set to this value for the specified waveform set, if the number is smaller than the current value of `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） for this set. Otherwise, it is set to the current value of TSUS.

 |
 |

SWAP

 |

This command parameter causes the values set by `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）and TSUX to be switched, that is, TSUS is set to the current value of TSUX , and TSUX to that of TSUS for the specified waveform set.

 |
 |

NONE

 |

This command parameter sets the value of TSUX back to 1 for the specified waveform set.

 |

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

|

waveform_set

 |

Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

multi-port_spec

 |

To enter a multi-port specification is only possible if the specification is associated with the default port and if no other ports are configured.

 |
 |

timing_set

 |

Timing set number. Enter PRM for the primary timing set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）.

 |
 |

period

 |

Enter the test system period in ns for which you wish to check whether auto-correction will take place or not. period must be within the maximum and minimum test system periods of the model.

 |
 |

pinlist

 |

The name of the pin or pins whose period you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The @ symbol can be used to check all configured pins.

 |
 |

autocorrect

 |

The auto-correction flag returned by the system. It can be:

 |
 |

0

 |

No auto-correction will occur.

 |
 |

1

 |

Auto-correction will occur.

 |

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

|

waveform_set

 |

Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes.

 |
 |

dev_cyc_name

 |

The device cycle name. Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes.

Alternatively, you can enter:

 |
 |

 |

ALL

 |

With this specifier the command checks that:

- The pins in pinlist have exactly the same device cycle names.
- For each device cycle, each pin defines the device cycle with the same length.
 |
 |

 |

FDC

 |

With this specifier the command checks that the first device cycle in the device cycle definition table for each pin in the pinlist has the same length.

 |
 |

pinlist

 |

The pin name or names whose device cycles are to be checked. If more than one pin is required, the names must be separated with a comma. The @ character can be used to read all configured pins.

 |
 | dev_cyc_len  | Always 1 for SmarTest 7.10. |

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

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

multi-port_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

timing_set

 |

Specifies the timing sets to be checked. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）.

In a multi-port setup, the check is performed for those pins from pinlist that belong to the same port. If you specify a number, a timing set with this number must be present in every equation set that is associated with a port of the multi-port specification.

 |
 |

pinlist

 |

The name of the pin or pins to be checked. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.

In a multi-port setup, the pins can belong to more than one port. Only those pins are considered that belong to one of the ports of the specification.

 |
 |

status

 |

The system returns:

 |
 |

0

 |

The timing is not the same.

 |
 |

1

 |

The timing is the same.

 |

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

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes.

 |
 |

dev_cyc_name

 |

If you specify the name of a device cycle, only this device cycle will be checked. Enter ALL for all device cycle names in the device cycle table.

 |
 |

pinlist

 |

The name of the pin or pins whose definitions you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.

 |
 |

status

 |

The system returns:

0: The definitions are not the same.

1: The definitions are the same.

 |

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

|

waveform_set_x

 |

Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

pinlist

 |

The name of the pin or pins for which you wish to check waveform set compatibility. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.

 |
 |

status

 |

The system returns:

 |
 |

 |

0

 |

The waveform sets are not compatible.

 |
 |

 |

1

 |

The waveform sets are compatible.

 |

### Example（取自子主题 List of timing setup commands › VWFS  -  Verify WaveForm Sets）

```
VWFS? 1,2,(DATA)
```

This example checks whether waveform sets 1 and 2 are the same for the pins in the group DATA. If they are the same the following string is returned:

```
VWFS 1,(DATA)
```

### Parameters（取自子主题 List of timing setup commands › WAVE  WAVE  -  WAVEform）

|

wvf_set

 |

Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed by double quotes.

 |
 |

multiport_spec

 |

To change or query a multiport specification, enter the name of the specification.

 |
 |

wfIndex

 |

Logical waveform index. This index identifies the logical waveform for which a physical waveform is to be created. The values specified for the DD1, DD2, ED1, and ED2 parameters must be in accordance with the format of this logical waveform.

 |
 |

DD1 and DD2

 |

First and second drive data parameter. These are optional parameters and contain values for both drive data and tri-state. The values you can define are:

 |
 |

F0N

 |

drive 0

 |
 |

F1N

 |

drive 1

 |
 |

FN0

 |

tri-state off

 |
 |

FNZ

 |

tri-state on

 |
 |

F00

 |

drive 0, tri-state off

 |
 |

F0Z

 |

drive 0, tri-state on

 |
 |

F10

 |

drive 1, tri-state off

 |
 |

F1Z

 |

drive 1, tri-state on

 |
 |

ED1 and ED2

 |

First and second receive data parameter. These are optional parameters. The values you can define are:

 |
 |

F0

 |

compare to 0

 |
 |

F1

 |

compare to 1

 |
 |

FI

 |

compare to intermediate

 |
 |

FX

 |

compare to mask

 |
 |

FU

 |

compare to unstable

 |
 |

C

 |

capture digital data

 |
 |

D

 |

do not capture digital data

 |
 |

The values C and D are used for selective digital capture. The following rules apply to these values:

- A waveform that is used for selective digital capture cannot contain more than one compare action. Therefore, if you specify C or D for one of ED1 or ED2, you cannot specify a value for the other Expected Data parameter.
- If you issue more than one instance of the WAVE command for the same logical waveform, the values you specify for the same Expected Data parameter in these different WAVE instances must be homogeneous; that is, either all or none of them must be C or D. You cannot, for instance, set ED1 to C in one of these WAVE instances, and set it to F1 in another.
 |
 |

pwfIndex

 |

Physical waveform index. Enter an integer between 0 and 31 (0 and 255 on the Pin Scale Digital systems) for each physical waveform . The index is stored in the vector area and references the physical waveform in the physical waveform table.

 |
 |

pinlist

 |

The name of the pin or pins for which physical waveform states are to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated by commas.

 |
 |

ALLOW_EQ

 |

This extra parameter allows you to define physical waveforms for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.

Note also the following:

- Every runtime change will affect all specifications that use the respective wavetable.
- Since the new waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.
- The runtime definitions are not checked for consistency. It is up to the user to ensure this.
 |

### Example（取自子主题 List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

This example first defines a logical waveform with the index 2 for waveform set 1. The waveform uses the data parameter D11, the fixed action 0, and the complement C11 of D11. Then two physical waveforms are defined for logical waveform 2, which are referenced by the physical waveform DC/DC power units 4 and 5. Waveform 4 drives to 0 at edge d1, to 0 at d3, and to 1 at d4. Waveform 5 drives to 1 at edge d1, to 0 at d3, and to 0 at d4.

### Example（取自子主题 List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
> WFDF 1,2,N,N,D11,N,N,N,(D0,D2,D2,D3)
```

This example defines a waveform referenced by waveform index 2. The waveform uses the drive data and tri-state parameter 1. Edge number 3 provides the timing for this waveform. The definitions are made for waveform set 1 and for pins D0 to D3.

### Parameters（取自子主题 List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

|

wvf_set

 |

Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query you can also enter ALL for all waveform sets. Enter PRM to select the primary waveform set.

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

Waveform index. Enter an integer between 0 and 255. The index references a waveform in a device cycle. For the query you can also enter ALL for all waveform DC/DC power units. The waveform index is also used by the `WAVE, WAVE? - (WAVEform)`（raw: `02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） command.

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

The following table shows which data-dependent drive actions use the driver formatter, which use the tri-state formatter, and which use both. You have to consider this when assigning parameters to the `WAVE`（raw: `02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） command. See also `Specifying the actions`（raw: `02.06.06.01.03.01.01_Specifying_the_actions.md`）.

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

On Smart Scale systems, there are two types of drive edges, denoted by fi and si (1 鈮?i 鈮?8). For both of them, only the action codes 0, 1, and N are admitted. But the Smart Scale systems also support the old di syntax. For more information see `Defining waveforms for Smart Scale pins`（raw: `02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`）.

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

The name of the pin or pins for which the waveform is to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The @ symbol can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.

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

|

wvf_set

 |

Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes.

 |
 |

specset_id

 |

Derived as follows:

`100 *`equation_set_no `+ `specset_no

 |
 |

multiport_spec

 |

To change or query a multiport specification, enter the name of the specification.

 |
 |

wfIndex

 |

Logical waveform index. Enter an integer between 0 and 31 (255 on Pin Scale systems).

 |
 |

pinlist

 |

The name of the pin or pins for which the waveform is to be deleted. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The @ symbol can be used to specify all configured input pins. If more than one pin is to be included, the names must be separated with a comma.

 |
 |

ALLOW_EQ

 |

This extra parameter allows you to delete a logical waveform for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.

Note also the following:

- Every runtime change will affect all specifications that use the respective wavetable.
- Since the new or changed waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.
 |

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

|

waveform_set

 |

Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |

### Example（取自子主题 List of timing setup commands › WRST -  Waveform ReSeT）

```
WRST 3
```

This example resets all waveform and timing entries for all pins for waveform set 3.

### Parameters（取自子主题 List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

|

waveform_set

 |

Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

`Derived as follows:`

`100 * equation_set_no + specset_no`

 |
 |

multiport_spec

 |

To query a multiport specification, enter the name of the specification.

 |
 |

display_mode

 |

Sets the Vector Setup display mode. This can be:

 |
 |

0

 |

The "classic" display mode. A device cycle has the length of one test system cycle.

 |
 |

1

 |

The "single column" display mode. All pins use the same device cycles.

 |
 |

2

 |

The "multi column" display mode. All pins do not use the same device cycles, the device has two or more separate ports with independent signals.

 |
 |

portlist

 |

For multiport specifications, you can specify the ports for which the vector setup display mode is to be returned.

 |

### Example（取自子主题 List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

```
> WSDM? "spec_1", (port_1)
< WSDM  "spec_1", 0
```

This example queries the display mode of port port_1 in the multiport specification spec_1. The reply shows that it is set to the "classic" display mode.

### Parameters（取自子主题 List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

|

waveform_set

 |

Waveform set number. This is the highest number currently allocated to a waveform set or the highest number of a set you want to load. The number you enter must not exceed the maximum number of waveform sets allowed (defined by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command).

This number is automatically updated to include any new waveform set as it is created. At power-on, only one waveform set (containing one timing set and default values) is available.

 |

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
