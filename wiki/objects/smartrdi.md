---
type: object
title: SmartRDI
layer: L2
stage: testmethod
tags: [testmethod, smartrdi, rdi, test-method-api, execution-mode, burst-pattern, multiport, hidden-upload]
related: [testmethod, pattern, sequencer, hidden-upload, level, timing, dc-scale-xps256-card, xps256-status-flags, ps1600, ps5000]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# SmartRDI

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **112,213 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.13.04.01_Example_of_keyword_setups_in_the_RDI_Configure_file.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.04.02_getRdiConfig.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.06.01_rdi.getInfoLevel.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.06.02_rdi.setInfoLevel.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.02_execute.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.03_id.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.04_RDI_BEGIN.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.05_RDI_END.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.06_RDI_INIT.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.07_RDI_UNIT_INIT.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.08_RDI_WAIT_TEST_DONE.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02_Changing_the_default_pin_status_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.04.01_digCapBurstSiteUpload.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05.01_fastSyncOff.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05.02_fastSyncOn.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05.03_fastSyncPortNum.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.01_getBuildDate.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.02_Macros_to_get_the_SmartRDI_version_number.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.03_rdi.getActiveRdiRev.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.04_rdi.getCompileRdiRev.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.07.01_Automatic_masking_on_inactive_sites.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.07.02_Active_site_on_hold.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.01_port.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.02_portSync.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.03_RDI_PORT_BEGIN.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.04_RDI_PORT_END.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.09_Pass_Fail_per_label.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.10.01_burstPostfix.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.11.01_rdi.pureGenerationMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12_Register_Access_library.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.13.04_RDI_SEMI_PARALLEL_TEST_BEGIN.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.13.05_RDI_SEMI_PARALLEL_TEST_END.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14_Setting_and_retrieving_the_setup_name_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.16.01_rdi.disableWarning.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.16.02_rdi.enableWarning.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17_Sync_group_support_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.01_Using_hidden_upload_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20_Using_Offline_Result_Emulation_in_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21.01_wait.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21.02_waitCycle.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01_Alarm_setup_file.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02_Alarm_handling_commands.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10_SmartRDI__d2s-like_protocol_test_setup.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01_Using_a_DC_resource_as_an_AWG_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.02_Runtime_DC_waveform.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.03_DC_waveforms_per_site.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04_Using_a_DC_resource_as_a_digitizer_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.05_Using_a_DC_Scale_resource_as_a_digitizer_while_sourcing_a_waveform_on_th.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.06_Serial_Semi-parallel_execution_of_BADC_as_digitizer_over_sites.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.07_DC_waveform_and_sampling_in_parallel.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.08_Parallel_pulse_actions_with_measurement_and_sampling.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01_Setting_up_PPMU_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02_Setting_up_Board_ADC_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03_Setting_up_SPMU_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.01_Generating_a_new_digital_capture_pattern_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.02_Inserting_digital_capture_actions_in_an_existing_pattern_with_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.03_Using_Immediate_Upload_in_SmartRDI.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.04_addVecRange.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.05_bitPerWord.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.06_burstUpload.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.07_capMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.08_copyLabel.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.09_enPassFail.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.10_format.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.11_initDiscard.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.12_interSkip.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.13_label.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.14_pin.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.15_samples.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.16_vecVar.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.17_vecVarOnly.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.18_getVector.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.19_getVectorBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.20_rdi.id__.getVectorFromVV.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.21_getVecVar.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.14_SmartRDI__Digital_channel_relay_control.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.01.01_Routing_Tools_-_Global_Setup_editor.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.01.04_Routing_Tools_-_State_Setup_editor.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05_rdi.route.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16_SmartRDI__Error_map_results_from_user_patterns.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17_Functional_test_setup.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.18_SmartRDI__Level_and_timing_set_changes.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.01_Structures_of_multiple_cogo___nodes.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.20.03_postBurst.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.01_getLabelCycleNum.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.02.01_setGlobalVar.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.02.02_getGlobalVar.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.03_dtos.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.04_itos.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.05_itos_hex.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.06_reverseBits.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.07_getCommentCycleNum.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.08_getCommentVectorNum.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23_SmartRDI__Utility_lines_control.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.02_bitLength.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.04_burstUpload.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.05_comment.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.06_copyLabel.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.07_defaultBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.08_defaultVec.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.09_download.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.10_emapLocation.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.11_enPassFail.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.12_expectBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.13_expectData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.14_failCount.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.15_failCyc.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.16_failNode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.17_FFC.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.18_fillBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.19_fillVec.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.20_insertJmpe.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.21_insertSub.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.22_label.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.23_labelName.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.24_multiFFC.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.25_passNode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.26_pMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.27_pModeStrobe.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.28_readBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.29_readData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.30_rdi.smartVec__.readMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.31_repeat.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.32_repeatSub.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.33_rdi.smartVec__.vecEditMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.34_vecLength.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.35_writeBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.36_writeData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.37_writeDataBurst.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.38_writeParData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.39_writeParDataBurst.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.40_writePat.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.41_writeVec.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.42_xMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.43_getFailCount.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.44_getFailCyc.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.45_getFFC.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.46_rdi.id__.getMultiFFC.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.47_getReadBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.48_getReadData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.03_Retrieving_match_loop_results.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 RDI Configure file › Example of keyword setups in the RDI Configure file）

```
// UTIL setup
UTIL_BLOCK = 12,34,5,6,7,8
UTIL_FRAM = UL_FRAM1,UL_FRAM3,UL_FRAM5,UL_FRAM6,UL_FRAM7,UL_FRAM8
UTIL_SCLK = UL_SCLK,UL_SCLK3,UL_SCLK,UL_SCLK,UL_SCLK,UL_SCLK
UTIL_SINP = UL_SINP,UL_SINP3,UL_SINP,UL_SINP,UL_SINP,UL_SINP
UTIL_SOUT = UL_SOUT,UL_SOUT3,UL_SOUT,UL_SOUT,UL_SOUT,UL_SOUT
UTIL_CTRL_MAX_SPEED = 2e6
UTIL_DYN_MASK_UNSPECIFIED_PIN = FALSE
UTIL_DYN_MASK_INACTIVE_SITE = TRUE
# UTIL_PADDING_RPTV_FLAT

// SmartVec setup
VEC_EDIT_MODE = VTT
DEFAULT_EMAP_LOCATION = TP
DEFAULT_SMV_READ_MODE = EMAP
SMV_DIGCAP_AUTO_BURSTUPLOAD = FALSE
SMV_VEC_MEM_TYPE = SHMEM
USER_NAMED_PATTERN_CONTENT_CHECK = FALSE

// Default pin status
DEFAULT_STATUS_PIN = pinA,pinB
DEFAULT_STATUS_INDEX = 0,1

// Setup name
ANALOG_SET_NAME_MD5 = TRUE
BURST_NAME_MD5 = TRUE

// PPMU setup
PPMU_DEFAULT_RELAY = NO
PPMU_DEFAULT_VALUE_MODE = SA

// Pass or fail per label
PER_LABEL_FUNC_RESULT_MODE = FLBL
PER_LABEL_FUNC_RESULT_NO_BREAK_VEC = TRUE

// ORE setup
ORE_FILE = " "
ENABLE_ORE = FALSE
ORE_TEMPLATE_BY_USER_CODE = TRUE

// Upload
DC_BURST_SITE_UPLOAD = TRUE
DIGCAP_ADAPTIVE_RESULT_SIZE = TRUE
DIGCAP_BURST_SITE_UPLOAD = TRUE

// Debug
REPORT_RESULT_IN_SINGLE_MODE = TRUE
ENABLE_RDI_INFO_LOG_FILE = TRUE

// SMC execution
DISABLE_SMC_EXEC_GLOBAL = TRUE
DISABLE_SMC_EXEC_SHORT_BURST = TRUE

// Production
SETUP_UPTODATE = TRUE

// Alarm handling for DCVI
ALARM_HANDLING_DCVI_ENABLE = TRUE
ALARM_HANDLING_DCVI_SETUP_FILE = "testmethod/RDI_Alarm_setup"

// Others
VEC_MODE_SAMPLING_WAIT = MSET
PURE_GENERATION_MODE = TRUE
ROUTING_SETUP_FILE = "testmethod/routing_tool_states_1.xml"
# ROUTING_SETUP_FILE = ./routing/Routing_Configure.xml
ALLOW_SAME_RESULT_ID_ACROSS_RDI_BLOCK = TRUE
# TMU_TIMEOUT_50ms = FALSE
```

### Syntax（取自子主题 RDI Configure file › getRdiConfig）

```
string rdi.getRdiConfig(string optionName);
```

Parameter
| Parameter | Description |
|---|---|
| optionName | The option name to be queried. |

### Return Value（取自子主题 RDI Configure file › getRdiConfig）

The option value returns.

### Example（取自子主题 RDI Configure file › getRdiConfig）

```
rdi.getRdiConfig("RF_CAL_DEFAULT");
```

For the option RF_CAL_DEFAULT, one of the three values will return: ON, OFF, and SYSTEM_CAL.

### Syntax（取自子主题 RDI INFO LEVEL › rdi.getInfoLevel）

```
int getInfoLevel();
```

### Example（取自子主题 RDI INFO LEVEL › rdi.getInfoLevel）

Changing the RDI_INFO_LEVEL to 2

```
...
cout<<"RDI_INFO_LEVEL ="rdi.getInfoLevel()<<endl;
rdi.setInfoLevel(2);

RDI_BEGIN();
  rdi.dc().pin("DATA1").vForce(3 V).execute();
  rdi.dc().pin("DATA2").iForce(0 mA).vMeas().measWait(100 us).execute();
RDI_END();

cout<<"RDI_INFO_LEVEL ="rdi.getInfoLevel()<<endl;

rdi.setInfoLevel(0);
```

 In the SmarTest UI report window:

```
RDI_INFO_LEVEL = 0

Total:                                 26.071 msec
  Setup Generation:                      15.631 msec
    Action pattern & Dc generation:        14.090 msec
    Burst pattern gen:                      0.080 msec
    Other init & check:                     0.069 msec
    Pattern Cycle Calculation:              1.376 msec
    User Code:                              0.016 msec
  Setup Command:                         6.044 msec
    DC Setup:                              5.839 msec
    Other Command:                         0.205 msec
  Pattern Execution:                     3.278 msec
  Result Upload:                         1.043 msec
    DC Result Upload:                      1.023 msec
  Others:                                0.075 msec

RDI_INFO_LEVEL = 2
```

### Syntax（取自子主题 RDI INFO LEVEL › rdi.setInfoLevel）

```
void setInfoLevel(int val);
```

### Example（取自子主题 RDI INFO LEVEL › rdi.setInfoLevel）

Setting the RDI_INFO_LEVEL to 2 for a block:

```
...
cout<<"RDI_INFO_LEVEL ="rdi.getInfoLevel()<<endl;
rdi.setInfoLevel(2);

RDI_BEGIN();
  rdi.dc().pin("DATA1").vForce(3 V).execute();
  rdi.dc().pin("DATA2").iForce(0 mA).vMeas().measWait(100 us).execute();
RDI_END();

cout<<"RDI_INFO_LEVEL ="rdi.getInfoLevel()<<endl;

rdi.setInfoLevel(0);
```

 The SmarTest UI report window shows the level 2 information:

```
RDI_INFO_LEVEL = 0

Total:                                 26.071 msec
  Setup Generation:                      15.631 msec
    Action pattern & Dc generation:        14.090 msec
    Burst pattern gen:                      0.080 msec
    Other init & check:                     0.069 msec
    Pattern Cycle Calculation:              1.376 msec
    User Code:                              0.016 msec
  Setup Command:                         6.044 msec
    DC Setup:                               5.839 msec
    Other Command:                          0.205 msec
  Pattern Execution:                     3.278 msec
  Result Upload:                         1.043 msec
    DC Result Upload:                       1.023 msec
  Others:                                0.075 msec

RDI_INFO_LEVEL = 2
```

### Syntax（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › execute）

```
execute();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › execute）

```
rdi.util().pin("upin_A").setOn().pin("upin_B").setOff().execute();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › id）

```
XXX(data type) result = rdi.id().getXxxx();
```

### Example（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › id）

```
const ARRAY_D &Result = rdi.id("cap").getWaveform("DATA_1");
```

```
ARRAY_D results = rdi.id("meas").getMultiValue("pinA");
```

```
rdi.id("id").getAlarmPassFail("A");
```

### Syntax（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI BEGIN）

```
RDI_BEGIN();
RDI_BEGIN(mode);
```

Parameter
 |

Parameter

 |

Description

 |
 |

mode

 |

The optional execution mode. It can be:

-

TA::BURST: Pattern-based execution mode. This is the default mode.

-

TA::SINGLE: Single step execution mode for debugging.

-

TA::PROD: Production mode. No new setups will be generated. The saved setups from the pattern‑based mode will be used.

 |

### Example 1: Minimum code（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI BEGIN）

The following example shows the minimum code for a RDI block. The ellipses ("...") are to be replaced with your code.

```
RDI_BEGIN();
    ...
    ...
RDI_END();
```

### Example 2: Optional curly brackets（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI BEGIN）

The example utilizes an optional pair of curly brackets "{" and "}". These optional curly brackets are used for simplifying the correct indentation with assistance of the related Eclipse tool.

```
RDI_BEGIN();
{
    ...
    ...
}
RDI_END();
```

 Note The two use options (with or without curly brackets) should not be mixed in one test method class.

### Syntax（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI END）

```
RDI_END();
RDI_END(mode);
```

Parameter
 |

Parameter

 |

Description

 |
 |

mode

 |

The optional execution mode. If mode is not specified, the blocking pattern execution is used by default.

-

TA::BLOCKING is to be used to start the blocking pattern execution at the end of the RDI block. No other action can be performed while the pattern burst is running.

This is the default option.

-

TA::NON_BLOCKING is to be used to start the non-blocking pattern burst execution at the end of the RDI block. Other actions can be performed while the pattern burst is running.

The command `RDI_WAIT_TEST_DONE()`（raw: `02.07.13.08.01.08_RDI_WAIT_TEST_DONE.md`） is to be used to align the end of the non-blocking pattern execution.

 |

### Example 1: Minimum code（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI END）

The following example shows the minimum code for a RDI block. The ellipses ("...") are to be replaced with your code.

```
RDI_BEGIN();
    ...
    ...
RDI_END();
```

### Example 2: Optional curly brackets（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI END）

The example utilizes an optional pair of curly brackets "{" and "}". These optional curly brackets are used for simplifying the correct indentation with assistance of the related Eclipse tool.

```
RDI_BEGIN();
{
    ...
    ...
}
RDI_END();
```

 Note The two use options (with or without curly brackets) should not be mixed in one test method class.

### Example 3: Non-blocking execution（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI END）

```
RDI_BEGIN();
    ...
RDI_END(TA::NON_BLOCKING); // Execution of the pattern burst starts.

//
// Actions during pattern burst execution
//
...
...

RDI_WAIT_TEST_DONE(); // Wait for end of pattern burst.
```

If RDI_END() is used instead of RDI_END(mode), the RDI block is executed in a blocking way, which means no other jobs can be executed while the pattern burst is running.

### Syntax（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI INIT）

```
RDI_INIT();
```

RDI_INIT() must be called before `ON_FIRST_INVOCATION_BEGIN();`（raw: `02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md`）.

### Syntax（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI UNIT INIT）

Note RDI_UNIT_INIT() is required for both pattern‑based and code‑based commands including pure code‑based commands.

```
RDI_UNIT_INIT(const string &sName);
```

Parameter
| Parameter | Description |
|---|---|
| sName | A string as an identifier. |

For a "live-branch" case, the `RDI_UNIT_INIT(string)` is for this purpose.

```
   RDI_BEGIN(TA::BURST);
      .... // do block1 actions
   RDI_END();
   if (skip_block) {
           // do nothing
   } else {
       RDI_UNIT_INIT("anystring");
       RDI_BEGIN(TA::BURST);
      .... // do block2 actions
       RDI_END();
   }
   RDI_BEGIN(TA::BURST);
      .... // do block3 actions
   RDI_END();
```

 Note RDI can only have 1000 runtime branches in one test suite.

### Example 1（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI UNIT INIT）

```
 if(user_variable)
    {
      RDI_UNIT_INIT("string1");
      rdi.dc().pin("DATA1").iForce(1 mA).execute();

      RDI_BEGIN();
        rdi.dc().pin("DATA1").vForce(1.5 V).execute();
        rdi.dc().pin("DATA2").iForce(0 mA).vMeas().execute();
      RDI_END();
    }
 else
    {
      RDI_UNIT_INIT("string2");
      rdi.dc().pin("DATA1").iForce(2 mA).execute();

      RDI_BEGIN();
        rdi.dc().pin("DATA1").vForce(2.5 V).execute();
        rdi.dc().pin("DATA2").iForce(0 mA).vMeas().execute();
      RDI_END();
    }
```

### Example 2（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI UNIT INIT）

```
 while(user_variable)
        {
            RDI_UNIT_INIT("string1");
            RDI_BEGIN();
            rdi.dc().pin("DATA1").vForce(1.5 V).execute();
            rdi.dc().pin("DATA2").iForce(0 mA).vMeas().execute();
            RDI_END();
         }
```

### Example 3（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI UNIT INIT）

You can put a result retrieval command of a measurement anywhere for RDI_UNIT_INIT().

```
static int lastResult=2;

ON_FIRST_INVOCATION_BEGIN();
If (lastResult>2.0)
{
RDI_UNIT_INIT("string1");
RDI_BEGIN();
  rdi.dc("d1").vMeas().execute();
RDI_END();

FOR_EACH_SITE_BEGIN();
  rdi.id("d1").getValue(); // You can put the getXXX() command here.
FOR_EACH_SITE_END();
}

lastResult++;
if(lastResult==4) { lastResult =0;}
...
ON_FIRST_INVOCATION_END();

rdi.id("d1").getValue(); // You also can put the getXXX() command here.
```

### Syntax（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI WAIT TEST DONE）

```
RDI_WAIT_TEST_DONE();
```

### Example（取自子主题 SmartRDI  General topics and functions › General SmartRDI functions › RDI WAIT TEST DONE）

```
RDI_BEGIN();
    ...
RDI_END(TA::NON_BLOCKING);    //Non-blocking execution starts.

...    //actions during pattern execution

RDI_WAIT_TEST_DONE();    //Non-blocking execution ends.
```

### Example 1（取自子主题 SmartRDI  General topics and functions › Changing the default pin status with SmartRDI）

```
RDI_BEGIN();
  rdi.setPinStatus("pinA",3);
  rdi.digCap("mcsame1_DATA1_0").pin("DATA2").samples(30).execute();
  rdi.clearPinStatus("pinA");
RDI_END();
```

### Example 2（取自子主题 SmartRDI  General topics and functions › Changing the default pin status with SmartRDI）

Do not use `setPinStatus()`（raw: `02.07.13.08.02.02_setPinStatus.md`） and `clearPinStatus()`（raw: `02.07.13.08.02.01_clearPinStatus.md`） in the `burstLabel`（raw: `02.07.13.24.03_burstLabel.md`） block of `smartVec`（raw: `02.07.13.24_SmartRDI__Vector_and_protocol_programming.md`）.

Wrong position:

```
RDI_BEGIN();
  rdi.smartVec().burstLabel("labelName").begin();
    ...
    rdi.setPinStatus("A",1); // This is not allowed.
    ...
  rdi.smartVec().burstLabel().end();
RDI_END();
```

  Correct position:

```
RDI_BEGIN();
  rdi.setPinStatus("A",1); // This is correct.
  rdi.smartVec().burstLabel("labelName").begin();
    ...
    ...
  rdi.smartVec().burstLabel().end();
RDI_END();
```

### Example 1: DC test - Using different values for different sites（取自子主题 SmartRDI  General topics and functions › Changing the parameter value at runtime with SmartRDI）

```
ARRAY_D rtv_arr(4); // Define a variable for quad-site tests
rtv_arr.init(0.0);

ON_FIRST_INVOCATION_BEGIN();

    rtv_arr[0]=1.0; rtv_arr[1]=1.1; rtv_arr[2]=1.2; rtv_arr[3]=1.3;

    rdi.runTimeVal("rtv",rtv_arr);

    rdi.dc().pin("A").vForce("rtv").execute();  // Both code‑based or pattern‑based modes are supported.

ON_FIRST_INVOCATION_END();
```

### Example 2: RF stimulus - Using the different values for different sites（取自子主题 SmartRDI  General topics and functions › Changing the parameter value at runtime with SmartRDI）

```
ARRAY_D power(4); // Define a variable for quad-site tests
power.init(0.0);

power[0]=-10;power[1]=-11;power[2]=-12;power[3]=-13;

ON_FIRST_INVOCATION_BEGIN();

    rdi.runTimeVal("ppp",power);

    RDI_BEGIN();

        rdi.rfs().pin("A").signal(TA::CW).power("ppp").freq(1e9).execute();

    RDI_END();

ON_FIRST_INVOCATION_END();
```

### Example 3: Protocol test - Changing the write data at runtime（取自子主题 SmartRDI  General topics and functions › Changing the parameter value at runtime with SmartRDI）

```
ARRAY_I write_data(2); // Define a variable for dual-site test
write_data.init(0);

write_data[0]=0x1;
write_data[1]=0x2;

rdi.runTimeVal("data",write_data); // Site data array

RDI_BEGIN();

    rdi. protocol().pname("i2c").write(0x4,"data").execute();

RDI_END();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Controlling burst site upload › digCapBurstSiteUpload）

```
digCapBurstSiteUpload(bool digCapBurstSiteUpload);
```

List of parameters
| Parameter | Description |
|---|---|
| digCapBurstSiteUpload | Whether to use burst site upload for the following digital capture test. It can be true or false. The default value is false.<br><br>If it is set to true, the maximum sample number is 8192. |

List of available options of parameter: hwDecimation
| Option | Description |
|---|---|
| true | Use burst site upload. |
| false | Do not use burst site upload. |

### Example（取自子主题 SmartRDI  General topics and functions › Controlling burst site upload › digCapBurstSiteUpload）

```
rdi.digCapBurstSiteUpload(true);
RDI_BEGIN();
  rdi.digCap(1).pin("DATA1").samples(1024).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Fast Sync setup with SmartRDI › fastSyncOff）

```
void fastSyncOff()
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Fast Sync setup with SmartRDI › fastSyncOn）

```
void fastSyncOn()
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Fast Sync setup with SmartRDI › fastSyncPortNum）

```
void fastSyncPortNum(int number)
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Getting the SmartRDI revision information › getBuildDate）

```
string rdi.getBuildDate();
```

### Return Value（取自子主题 SmartRDI  General topics and functions › Getting the SmartRDI revision information › getBuildDate）

This function returns a string which holds the build data of the beta revision. For example, it returns a string 20160520, which presents May 20, 2016.

  Note This command is not thread-safe. DO NOT put this function into the SMC_BackgroundProcessing() function.

### Example（取自子主题 SmartRDI  General topics and functions › Getting the SmartRDI revision information › Macros to get the SmartRDI version number）

In the following example, the test method code in between will be compiled only when the SmartRDI version number is not less than 2.4.4.

```
#if ((RDI_VERSION_MAJOR ==2)&&(RDI_VERSION_MINOR>4))| |
  ((RDI_VERSION_MAJOR ==2)&&(RDI_VERSION_MINOR ==4)&&(RDI_VERSION_QUALITY >=4))
  //test method code
  ...
#endif
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Getting the SmartRDI revision information › rdi.getActiveRdiRev）

```
string rdi.getActiveRdiRev();
```

 Note This command is not thread-safe. DO NOT put it into the SMC_BackgroundProcessing() function.

### Examples（取自子主题 SmartRDI  General topics and functions › Getting the SmartRDI revision information › rdi.getActiveRdiRev）

```
string active_rdi_rev=rdi.getActiveRdiRev();
```

   Note

### Syntax（取自子主题 SmartRDI  General topics and functions › Getting the SmartRDI revision information › rdi.getCompileRdiRev）

```
string rdi.getCompileRdiRev();
```

 Note This command is not thread-safe. DO NOT put it into the SMC_BackgroundProcessing() function.

### Example（取自子主题 SmartRDI  General topics and functions › Getting the SmartRDI revision information › rdi.getCompileRdiRev）

```
string compile_rdi_rev=rdi.getCompileRdiRev();
```

### Example（取自子主题 SmartRDI  General topics and functions › Site masking › Automatic masking on inactive sites）

### Defining a dummy label for inactive sites

```
rdi.assignLabelOnInactiveSites("userlabel","pt1");

RDI_BEGIN();
  rdi.port("pt1")....execute();  // For pt1, use a user label.
  rdi.port("pt2")....execute();  // For pt2, run a dummy label created by RDI.
RDI_END()
```

### Example（取自子主题 SmartRDI  General topics and functions › Site masking › Active site on hold）

### Setting sites to be on hold, assigning labels to the sites,

```
ON_FIRST_INVOCATION_BEGIN();

// Set sites to be on hold and assign labels to these sites.
ARRAY_I holdSites(2);
holdSites[0] = 2;
holdSites[1] = 4;
rdi.setOnHoldSites(holdSites);
rdi.assignLabelOnHoldSites("holdLabel","pt1");

RDI_BEGIN();
  rdi.port("pt1").smartVec("id1").pin("pinA").writeData()
                                 .pin("pinB").readData().execute();
  rdi.port("pt2").emap()....execute();
RDI_END();

ON_FIRST_INVOCATION_END();

rdi.id("id1").getOnHoldSites(); // Return array_I={2,4}
If(!rdi.id("id1").getOnHoldSitesStatus())
{
      rdi.id("id1").getReadData("pinB"); // Site 1 and site 3 return {xx}
}
else
{
     // For on hold sites, RDI gives dummy results.
     rdi.id("id1").getReadData("pinB"); // Sites 2 and 4 return{} 鈫?dummy
}

rdi.clearOnHoldSites(); // Sites 2 and 4 return back to normal state.
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Multiport handling › port）

```
port(const string& sPort);
```

Parameter List
| Parameter | Description |
|---|---|
| sPort | The port name. |

### Example（取自子主题 SmartRDI  General topics and functions › Multiport handling › port）

```
rdi.port("ptDATA_half1").func().label("funcPass_half1").execute();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Multiport handling › portSync）

```
portSync(const string &port);
portSync();
portSync(mode);
```

List of parameters
| Parameter | Description |
|---|---|
| port | The ports to be synchronized, separated by comma.<br><br>If not specified, the patterns of all ports will be synchronized. |
| mode | The execution mode.<br><br>TA::CTIM: Used to insert patterns with `CTIM (Change TIMing)`（raw: `../02.06_Command_Reference/02.06.07.01.08.03.01_Changing_the_timing_set__CTIM.md`） instructions for multiple ports synchronization.<br><br>The CTIM instructions change test setup to the current timing set and achieve port synchronization. |

### Example 1（取自子主题 SmartRDI  General topics and functions › Multiport handling › portSync）

```
RDI_BEGIN();
  rdi.port("ptDATA").func().label("lpDcap").execute();
  rdi.port("ptDATA2").digCap("mcsame1").pin("DATA2").samples(30).execute();
  rdi.port("ptDATA").wait(10 ms);
  rdi.portSync();
  rdi.port("ptDATA2").digCap("mcsame2").pin("DATA2").samples(80).execute();
RDI_END();

```

Synchronizing selected ports:

```
RDI_BEGIN();
  rdi.port("pt_DATA1").dc().pin("DATA1").vForce(1 V).execute();
  rdi.port("pt_DATA1").wait(30 us);
  rdi.port("pt_DATA2").dc().pin("DATA2").iForce(0 mA).vMeas().execute();
  rdi.port("pt_DATA3").hwRelay().pin("DATA3").setOn("ALL").execute();
  rdi.port("pt_DATA4").hwRelay().pin("DATA4").setOn("ALL").execute();
  rdi.port("pt_DATA4").wait(10 us);
  rdi.portSync("pt_DATA1,pt_DATA2");  // synchronize the ports "pt_DATA1","pt_DATA2" only
  rdi.port("pt_DATA1").func().label("label_sync").execute();
  rdi.port("pt_DATA2").digCap().pin("DATA2").samples(16).execute();
RDI_END();
```

Note rdi.portSync() cannot handle the port synchronization after the execution of sequencer instructions with unpredictable cycle counts, as in match loops and conditional jumps. Alternatively, you can use an rdi.port().wait() to achieve the synchronization manually. In other cases, you can use a CTIM command. See Topic 10558 `Changing the timing set`（raw: `../02.06_Command_Reference/02.06.07.01.08.03.01_Changing_the_timing_set__CTIM.md`）. In case of FastSync, you must split the pattern into two runs.

### Example 2（取自子主题 SmartRDI  General topics and functions › Multiport handling › portSync）

Starting from 2.4.5, SmartRDI can insert CTIM instructions to patterns for multiport synchronization. See example below.

 !`portSync()_with_CTIM`（raw: `../../../../agent-html/153097.png`）

Use portSync(TA::CTIM) to provide synchronization for the following cases, where a standard "port synchronization with dummy loops" execution cannot be performed:

-  Ports with different period lengths that are not an integer multiple of each other.
-  Patterns with match loops or cogo actions.

portSync(TA::CTIM) can only synchronize all ports and does not support synchronization for selected ports.

Note CTIM can generate non-cycle-based behavior.

### Example 3（取自子主题 SmartRDI  General topics and functions › Multiport handling › portSync）

For MSETs, use portSync(TA::CTIM) to achieve port synchronization.

```
RDI_BEGIN();
  rdi.port("pA").smartVec().pin("a1").writePat("1,0").execute();
  rdi.port("pB").smartVec().pin("b1").writePat("1111,0000").execute();
  rdi.portSync();
  rdi.port("pA").dc().pin("a2",TA::BADC).vMeas().average(1).execute();
  rdi.portSync(TA::CTIM);
  rdi.port("pA").smartVec().pin("a1").writePat("1,1").execute();
  rdi.port("pB").smartVec().pin("b1").writePat("0000,0000").execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Multiport handling › RDI PORT BEGIN）

```
RDI_PORT_BEGIN(const string& sPort);
```

List of parameters
| Parameter | Description |
|---|---|
| sPort | The port to set up. |

### Example（取自子主题 SmartRDI  General topics and functions › Multiport handling › RDI PORT BEGIN）

```
RDI_BEGIN();
  RDI_PORT_BEGIN("ptDATA");
    rdi.protocol().pname("i2c").write(0x03,0x04).execute();
    rdi.protocol().pname("i2c").read(0x03).execute();
  RDI_PORT_END();
  RDI_PORT_BEGIN("ptDATA2");
    rdi.protocol(3).pname("i2c").read(0x03).execute();
  RDI_PORT_END();
RDI_END();
```

In this example, the actions in the `RDI_PORT_BEGIN("ptDATA")`/`RDI_PORT_END()` block equal to the following code without `RDI_PORT_BEGIN()`/`RDI_PORT_END()` block:

```
rdi.port("ptDATA").protocol().pname("i2c").write(0x03,0x04).execute();
rdi.port("ptDATA").protocol().pname("i2c").read(0x03).execute();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Multiport handling › RDI PORT END）

```
RDI_PORT_END();
```

### Example（取自子主题 SmartRDI  General topics and functions › Multiport handling › RDI PORT END）

```
RDI_BEGIN();
  RDI_PORT_BEGIN("ptDATA");
    rdi.protocol().pname("i2c").write(0x03,0x04).execute();
    rdi.protocol().pname("i2c").read(0x03).execute();
  RDI_PORT_END();
  RDI_PORT_BEGIN("ptDATA2");
    rdi.protocol(3).pname("i2c").read(0x03).execute();
  RDI_PORT_END();
RDI_END();
```

### Examples（取自子主题 SmartRDI  General topics and functions › Pass Fail per label）

### Returning functional test results per label

```
RDI_BEGIN();
  rdi.smartVec("1").pin("Pin2")
                   .expectData(20,2)
                   .execute();
  rdi.dc("2").label("pat1")
             .insertSub(10)
             .pin("VI1")
             .vForce(1)
             .enPassFail()
             .execute();
  rdi.func("3").label("Label1")
               .execute();
RDI_END();
```

### No ID, no Pass/Fail result per label

```
RDI_BEGIN();
  rdi.smartVec().pin("Pin1")
                .writeData(20,8,2)
                .pin("Pin2")
                .expectData(20,2)
                .execute();
  rdi.func().label("Label1")
            .execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Postfix in burst pattern names › burstPostfix）

```
burstPostfix(string);
```

### Example（取自子主题 SmartRDI  General topics and functions › Postfix in burst pattern names › burstPostfix）

```
rdi.burstPostfix("AAA");
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Pure generation mode › rdi.pureGenerationMode）

```
rdi.pureGenerationMode(bool);
```

### Example（取自子主题 SmartRDI  General topics and functions › Pure generation mode › rdi.pureGenerationMode）

```
rdi.pureGenerationMode(true);
RDI_BEGIN();
  rdi.smartVec().pin("A").writeData(0x12,8).labelName("label_A").execute();
RDI_END();

rdi.pureGenerationMode(false);

```

### Example 1（取自子主题 SmartRDI  General topics and functions › Register Access library）

RA operations without register structure definitions

```
RDI_BEGIN();

  // Write register
  RA_WRITE(0x1234, 0x55);
  // Read a register under ID : READ_ID_1
  RA_READ("READ_ID_1", 0x1234);
  // Read a register and compare against expected value without mask
  RA_COMPARE(0x1234, 0x55);
  // Read a register and compare against expected value with mask
  RA_COMPARE(0x1234, 0x55, 0xFE);
  // Write run time per site data
  RA_WRITE_DYNAMIC("DYN_ID_1", 0x1234);
  // Read a register again
  RA_READ("READ_ID_2", ADDR1);
  // Compare by reading register
  RA_COMPARE("COMP_ID_1", ADDR1, DATA1);

  rdi.wait(10 ms);

RDI_END();
```

### Example 2（取自子主题 SmartRDI  General topics and functions › Register Access library）

RA operations with register structure definitions

```
MultiSite<ULONG64> dynData;
dynData[0] = 0x7E;  dynData[1] = 0x01;
RA_SET_DYNAMIC_DATA("DynID1", dynData);

RDI_BEGIN();
  rdi.dc().pin("VDD").vForce(3.3).execute();
  reg.PERIPHERAL0().REGISTER0().setValue(0x5E).write();               // Write Register
  reg.PERIPHERAL0().REGISTER1().setField_FIELDA(1).write();           // Write Field (RMW)
  reg.PERIPHERAL0().REGISTER1().read("readID1");                      // Read Register
  reg.PERIPHERAL0().REGISTER0().setValue(0x5E).compare("CompareID1"); // Read and Compare
  reg.PERIPHERAL0().REGISTER2().writeDynamic("DynID1");               // Write a per site runtime register value

  // Other RDI operations
  rdi.wait(2 ms);
  rdi.dc("rdiID1").pin("D1").iForce(0).vMeas().execute();
  ...
RDI_END();

ULONG64 regValue = RA_GET_READ_RESULT("readID1");
bool comparePF = RA_GET_COMPARE_RESULT("CompareID1").getPassFail()
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Semi-parallel tests with SmartRDI › RDI SEMI PARALLEL TEST BEGIN）

```
RDI_SEMI_PARALLEL_TEST_BEGIN(SEMI_PARALLEL_CONFIG &semiParallelConfig);
```

List of parameters
| Parameter | Description |
|---|---|
| semiParallelConfig | The semi-parallel group to be executed in the semi-parallel testing block. |

### Example（取自子主题 SmartRDI  General topics and functions › Semi-parallel tests with SmartRDI › RDI SEMI PARALLEL TEST BEGIN）

```
SEMI_PARALLEL_CONFIG semiparallel;
semiparallel.group(1).add(1).add(3);
semiparallel.group(2).add(2).add(4);

RDI_INIT( );

ON_FIRST_INVOCATION_BEGIN();
    CONNECT();
    rdi.dc().pin("PVI8").vForce(2).execute();

  RDI_BEGIN();
    rdi.func().label("TestMode_Enable").execute();
    rdi.wait(1 ms);

    RDI_SEMI_PARALLEL_TEST_BEGIN(semiparallel);
      if (GET_CURRENT_SEMI_PARALLEL_GROUP_NUMBER() == 1)
        rdi.pmux().pin("010102").selectOn().execute();
    else
        rdi.pmux().pin("010101").selectOn().execute();

    rdi.dc("semi").pin("PVI8").vMeas().execute();
    RDI_SEMI_PARALLEL_TEST_END();

    rdi.func().label("TestMode_disable").execute();
  RDI_END();

  rdi.dc().pin("PVI8").disconnect().execute();

ON_FIRST_INVOCATION_END();
rdi.id("semi").getValue();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Semi-parallel tests with SmartRDI › RDI SEMI PARALLEL TEST END）

```
RDI_SEMI_PARALLEL_TEST_END();
```

See the example in the `RDI_SEMI_PARALLEL_TEST_BEGIN()`（raw: `02.07.13.08.13.04_RDI_SEMI_PARALLEL_TEST_BEGIN.md`） topic for its usage.

### Example（取自子主题 SmartRDI  General topics and functions › Setting and retrieving the setup name with SmartRDI）

Retrieving the analog set name

```
string analogSetName = rdi.id("AWG_1").getAnaSet();
string pAnalogSetName = rdi.getPriAnalogset();
```

Setting the analog set name and pattern burst name

```
rdi.setAnaSet("set1");
rdi.setPatBurst("pattBurst1");
RDI_BEGIN();
  ...
RDI_END();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › SmartRDI warning handling › rdi.disableWarning）

```
rdi.disableWarning();
```

Return value

There is no return value.

### Example（取自子主题 SmartRDI  General topics and functions › SmartRDI warning handling › rdi.disableWarning）

```
rdi.disableWarning();
   RDI_BEGIN();
      ...
   RDI_END();
```

### Syntax（取自子主题 SmartRDI  General topics and functions › SmartRDI warning handling › rdi.enableWarning）

```
rdi.enableWarning();
```

Return value

There is no return value.

### Example（取自子主题 SmartRDI  General topics and functions › SmartRDI warning handling › rdi.enableWarning）

```
rdi.enableWarning();
   RDI_BEGIN();
      ...
   RDI_END();
```

### Example（取自子主题 SmartRDI  General topics and functions › Sync group support with SmartRDI）

```
rdi.syncGroup("sg1").addPort("ptA");
rdi.syncGroup("sg2").addPort("ptB").addPort("ptC");

RDI_BEGIN();
  rdi.port("ptA")...
  rdi.port("ptB")...
  rdi.port("ptC")...
RDI_END();
```

### Example（取自子主题 SmartRDI  General topics and functions › Using SmartCalc  SMC  with SmartRDI › Using hidden upload with SmartRDI）

RF and DC

```
virtual void run()
{
    RDI_INIT();

    ON_FIRST_INVOCATION_BEGIN();
    {
        rdi.hiddenUpload(TA::ALL);

        RDI_BEGIN();
        {
            rdi.rfm("id1").pin("A").signal(TA::MOD_OUT).freq(1e9).bw(2e6).execute();
            rdi.dc("id2").pin("A").iForce(1 mA).vMeas().execute();
            rdi.dc("id3").pin("B").vForce(1 V).iMeas().average(5).execute();
        }
        RDI_END();
    }
    ON_FIRST_INVOCATION_END();

    SMC_ARM();

    return;
}

public:

void SMC_backgroundProcessing()
{
    double pwr = rdi.id("id1").getPower();
    double r1 = rdi.id("id2").getValue();
    double r2 = rdi.id("id3").getValue();
}
```

 Digitizer and digital capture

```
virtual void run()
{
    RDI_INIT();

    ON_FIRST_INVOCATION_BEGIN();
    {
        rdi.hiddenUpload(TA::ALL);

        RDI_BEGIN();
        {
            rdi.dgt("id1").pin("A").samples(1024).filter(1e6).FS(20e6).execute();
            rdi.digCap("id2").pin("A").samples(1024).execute();
        }
        RDI_END();
    }
    ON_FIRST_INVOCATION_END();

    SMC_ARM();

    return;
}

public:

void SMC_backgroundProcessing()
{
    ARRAY_D wave1 = rdi.id("id1").getWaveform();
    ARRAY_I bits  = rdi.id("id2").getVectorBit();
}
```

 Error map

```
virtual void run()
{
    RDI_INIT();

    ON_FIRST_INVOCATION_BEGIN();
    {
        rdi.hiddenUpload(TA::ALL); // Include the EMAP mode

        RDI_BEGIN();
        {
            rdi.smartVec("rb").pin("A").readBit(100).execute();
            rdi.emap("fc").label("bbb").pin("A").failCyc().execute();
        }
        RDI_END();
    }
    ON_FIRST_INVOCATION_END();

    SMC_ARM();

    return;
}

public:

void SMC_backgroundProcessing()
{
    rdi.id("rb").getReadBit();
    rdi.id("fc").getFailCyc();
}
```

### Example（取自子主题 SmartRDI  General topics and functions › Using Offline Result Emulation in SmartRDI）

ORE file locations must be loaded before RDI_INIT() in the first test suite.

```
virtual void run()
{
  static int i = 0;
  string oreFile[4];

// Load ORE files before RDI_INIT() in the first test suite.
  oreFile[0] = "./demo1.xml";
  oreFile[1] = "./demo2.xml";
  oreFile[2] = "./demo3.xml";
  oreFile[3] = "./demo4.xml";

  SET_USER_STRING("RDI_ORE_FILE", oreFile[i]);

  RDI_INIT();

  ON_FIRST_INVOCATION_BEGIN();

    RDI_BEGIN();
      rdi.emap("emap").label("funcPass").pin("DATA2").failCount(2).execute();
    RDI_END();

  i++;

  ON_FIRST_INVOCATION_END();

  cout<<"in run "<<i<<" , ore getFailCout result"<< rdi.id("emap").getFailCount()<<endl;

  return;
}
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Wait time in SmartRDI › wait）

```
wait(double dWait);
wait(const TA::WAIT_ACTION& waitAction);
```

List of parameters
| Parameter | Description |
|---|---|
| dWait | The time period to wait. |
| waitAction | The action to wait. |

List of available options of parameter: waitAction
| Option | Description |
|---|---|
| TA::WAIT_DGT | Wait for the digitizer to finish. |
| TA::WAIT_AWG | Wait for the AWG to finish. |
| TA::WAIT_RFAWG | Wait for the RF source waveform to finish. |
| TA::WAIT_RFDGT | Wait for the RF measurement to finish. |
| TA::WAIT_DCDGT | Wait for DC-DGT to finish. |

### Example（取自子主题 SmartRDI  General topics and functions › Wait time in SmartRDI › wait）

```
rdi.wait(TA::WAIT_DGT);
rdi.wait(5 ms);
```

### Syntax（取自子主题 SmartRDI  General topics and functions › Wait time in SmartRDI › waitCycle）

```
void waitCycle(unsigned long long iCycle);
```

List of parameters
| Parameter | Description |
|---|---|
| iCycle | The number of cycles. |

### Example（取自子主题 SmartRDI  General topics and functions › Wait time in SmartRDI › waitCycle）

```
rdi.waitCycle(10);
```

### Example 1（取自子主题 SmartRDI  Alarm handling for DCVI › Alarm setup file）

An alarm setup file

```
DEBUG_VALUE = TRUE  # This must be the first setup entry in the file.

SET DEFAULT  # Applied by default
    GlobalLimitRelForce = 10%
    GlobalLimitMinDisForce = 10 mV
    GlobalLimitRelClamp = 10 mV

    PINS UB_AVI VDD_AVI VDD_PVI
    # No local limit value defined means that global values are applied.

SET A1
    # Alarm checks on VDD_AVI are skipped.

    PINS UB_AVI
    LimitRelForce = 10%
    LimitMinDisForce = 5 mV
    # Used for vForce checks.
    # vClamp settings are used for vClamp checks.

    PINS VDD_PVI
    GlobalLimitRelForce = 10% #
    GlobalLimitMinDisForce = 10 mV
    # Used for vForce checks.

    LimitRelClamp = 100 mV
    # Used for vClamp checks.

SET A2
    # Alarm checks on both VDD_AVI and VDD_PVI are skipped.

    PINS UB_AVI
    LimitLo = 4.7  # default V
    LimitHi = 5.3
    # Used for both vForce and vClamp checks.
...
```

### Example 2（取自子主题 SmartRDI  Alarm handling for DCVI › Alarm setup file）

DEBUG_VALUE setting allows more information shown in the UI report window

Starting from 7.5.2, SmartRDI provides more information in the UI report window when the DEBUG_VALUE is enabled in the alarm setup file.

burst:: _rdi_burst_AVI64_Alarm_handling_Test_bk2

Alarm DC Result ::

Site [1]

ID:alarm_pass_fail_pin_AVI2_AVI4 , AVI2 = 3.00034, AVI4 = 2.00040 << F << (2.80000,3.20000),

ID:func_fail2 , AVI2 = 2.999909, AVI4 = 2.00036 << F << (2.80000,3.20000),

=============================================

Site [2]

ID:alarm_pass_fail_pin_AVI2_AVI4 , AVI2 = 2.999226, AVI4 = 1.99909 << F << (2.80000,3.20000),

ID:func_fail2 , AVI2 = 3.00074, AVI4 = 2.00028 << F << (2.80000,3.20000),

=============================================

### Examples（取自子主题 SmartRDI  Alarm handling for DCVI › Alarm handling commands）

```
rdi.alarm().applySet("abc"); // Use an alarm handing set "abc"

RDI_BEGIN();
  rdi.class(id)... // Each measurement with "id" triggers an alarm compare event after it
  ...
  rdi.alarm().check().execute(); // Add an alarm check point
RDI_END();

rdi.id("id").getAlarmPassFail("pinA"); // Alarm result of pinA, and any result "id" in burst
rdi.id("id").getAlarmPassFail();       // Alarm result for all alarm pins.
```

   Each of these commands takes effect in its test suite and subsequently keeps valid no matter where it is located, inside or outside an RDI_BEGIN-RDI_END block in the test suite.

```
RDI_BEGIN();
  rdi.alarm().globalLimitRelForcePercent(0.1);
...
RDI_END();

RDI_BEGIN();
... // the globalLimitRelForcePercent also takes effect.
RDI_END();
```

### Examples（取自子主题 SmartRDI  d2s-like protocol test setup）

### Basic data reading and writing

```
ON_FIRST_INVOCATION_BEGIN();
  RDI_BEGIN();
    rdi.protocol().pname("i2c").write(0x1,0x2).execute();
    rdi.protocol("id2").pname("i2c").read(0x1).execute();
    rdi.protocol("id3").pname("i2c").readExpect(0x1,0x03).execute();
    rdi.protocol("id4").pname("i2c").readExpect(0x1,0x03,0x1).execute();
  RDI_END( );
ON_FIRST_INVOCATION_END();
int result=rdi.id("id2").getData();
int pf=rdi.id("id3").getPassFail();
```

Burst data reading and writing

```
ARRAY_I data(3);
data[0]=0x9; data[1]=0xa; data[2]=0x7;
ON_FIRST_INVOCATION_BEGIN();
  RDI_BEGIN();
    rdi.protocol().pname("prt").writeBurst(0x1,data).execute();
    rdi.protocol("id1").pname("prt").regNum(3).read(0x01).execute();
 RDI_END( );
ON_FIRST_INVOCATION_END();
ARRAY_I result=rdi.id("id1").getDataStream();
```

### Runtime data writing

```
ARRAY_I write_data(2);
write_data[0]=0x1;
write_data[1]=0x2;
rdi.runTimeVal("data",write_data);  // site data array
RDI_BEGIN();
  rdi.protocol().pname("i2c").writeBurst(0x4,"data").execute();
RDI_END();
```

### Example（取自子主题 SmartRDI  DC resource AWG DGT usage › Using a DC resource as an AWG with SmartRDI）

```
anaWaveform vwav ("UP_V");
vwav.definition(TM::SINE).periods(3).amplitude(3 V).offset(0.5 V).samples(2048);
...
rdi.dc().pin("VI32_1").waveform(vwav).FS(10 KHz).execute();
rdi.dc().pin("VI32_1").vForce().waveform(vwav).FS(10 KHz).execute();
rdi.dc().pin("DPS32_SIG_1").vForce().waveform(vwav).FS(10 KHz).execute();
rdi.port("ptPin1").dc().pin("DATA1").waveform(vwav).samplePeriod(100 us).execute();
rdi.port("ptPin1").dc().pin("DATA1").iForce().waveform(vwav).sampleCycle(1000).execute();
```

### Example（取自子主题 SmartRDI  DC resource AWG DGT usage › Runtime DC waveform）

```
ARRAY_I sites;
Int siteNum = GET_CONFIGURED_SITES(sites); // To get all Configured Sites
vector<anaWaveform> siteWav(siteNum); // Runtime waveform array for multisite testing.

for(int i=0;i<siteNum;i++)
{
  anaWaveform tmpWave("tmpWave");
  tmpWave.definition(TA::SINE).samples(1024).offset(offset).periods(12).amplitude(1);
  siteWav[i]=tmpWave;
}
rdi.runtimeVal("rtWave",siteWav); // Runtime waveform matches run time ID.

RDI_BEGIN();
  rdi.port("ptPin").dc().pin("pinA").vForce().waveform("rtWave").FS(10 KHz).execute();
  // Waveform downloading happens before each execution.
RDI_END();
```

### Example（取自子主题 SmartRDI  DC resource AWG DGT usage › DC waveforms per site）

```
vector<anaWaveform> siteWav(siteNum); // Per site waveform array.

FOR_EACH_SITE_BEGIN();
  anaWaveform tmpWave("tmpWave");
  tmpWave.definition(TA::SINE).samples(1024).offset(offset).periods(12).amplitude(1);
  siteWav[CURRENT_SITE_NUMBER()-1]=tmpWave;
FOR_EACH_SITE_END();

rdi.perSiteVal("rtWave",siteWav); // Per site waveform matches perSiteVal ID.

RDI_BEGIN();
  rdi.port("ptPin").dc().pin("pinA").vForce().waveform("rtWave").FS(10 KHz).execute();
  // Waveform downloading happens before each execution.
RDI_END();
```

### Example（取自子主题 SmartRDI  DC resource AWG DGT usage › Using a DC resource as a digitizer with SmartRDI）

```

rdi.dc().pin("DPS128_1")
        .iForce(2 mA).vMeas().samples(1024).FS(10 KHz).execute();

rdi.dc().pin("DATA1")
        .vForce(1 V).iMeas().samples(1024).capMode(TA::VEC)
        .valueMode(TA::BADC).FS(10 KHz).execute();

rdi.dc().pin("DATA1")
        .vMeas().samples(1024).capMode(TA::VEC)
        .valueMode(TA::SA).FS(1 KHz).execute();

rdi.port("ptPin1").dc().pin("DATA1")
        .samples(1024).capMode(TA::TRIG)
        .valueMode(TA::BADC).FS(10 KHz).execute();

rdi.port("ptPin1").dc().pin("DATA1",TA::BADC)
        .samples(1024).capMode(TA::TRIG).FS(10KHz).execute();
```

### Example（取自子主题 SmartRDI  DC resource AWG DGT usage › Using a DC Scale resource as a digitizer while sourcing a waveform on th）

```
rdi.dc("id").pin().vForce().iMeas().waveform(wav).FS(10 KHz).execute();
rdi.dc("id").pin().vForce().vMeas().waveform(wav).FS(10 KHz).execute();
rdi.dc("id").pin().iForce().iMeas().waveform(wav).samplePeriod(100 us).execute();
rdi.dc("id").pin().iForce().vMeas().waveform(wav).sampleCycle(1000).execute();
```

### Example（取自子主题 SmartRDI  DC resource AWG DGT usage › Serial Semi-parallel execution of BADC as digitizer over sites）

We assume Pin "DATA36" shares one BADC on sites1 & 2 (pogo 103) and another BADC on sites 3 & 4 (pogo 104).

Example for a semi-parallel execution of digitizing by BADCs shared over sites. For pin "DATA36", sites 1 & 3 are executed at first followed by sites 2 & 4. Below are the example code as well as the code logic illustration.

```
SEMI_PARALLEL_CONFIG semi;
semi.group(1).add(1).add(3);
semi.group(2).add(2).add(4);

RDI_BEGIN();
  RDI_SEMI_PARALLEL_TEST_BEGIN(semi);
    rdi.dc().pin("DATA36").vMeas().samples(1024).FS(10 KHz).execute();
  RDI_SEMI_PARALLEL_TEST_END();
RDI_END();
```

 !`Serial/Semi-parallel execution of BADC as digitizer over Sites.`（raw: `../../../../agent-html/152310.png`）

### Examples（取自子主题 SmartRDI  DC resource AWG DGT usage › DC waveform and sampling in parallel）

### Forcing a waveform on a pin and taking samples on another pin

```
RDI_BEGIN();
rdi.port("portC").dc().pin("A").waveform(sine).FS(100 KHz)
                      .pin("B").samples(1024).FS(100 KHz)
                      .execute();
RDI_END();
```

### Forcing a waveform and taking samples in parallel on multiple pins

```
RDI_BEGIN();
  rdi.dc().pin("AVI1").vForce().waveform(sine1).sampleCycle(1000)
          .pin("AVI2").iForce().waveform(sine2).sampleCycle(1000).execute();
RDI_END();
```

### Forcing a waveform and taking samples on the same DC Scale pin

```
RDI_BEGIN();
  rdi.dc("id1").pin().vForce().iMeas().waveform(wav).FS(10 KHz).execute();
  rdi.dc("id2").pin().vForce().vMeas().waveform(wav).FS(10 KHz).execute();
  rdi.dc("id3").pin().iForce().iMeas().waveform(wav).FS(10 KHz).execute();
  rdi.dc("id4").pin().iForce().vMeas().waveform(wav).FS(10 KHz).execute();
RDI_END();
```

### Example（取自子主题 SmartRDI  DC resource AWG DGT usage › Parallel pulse actions with measurement and sampling）

```
rdi.dc().pin("A").vPulse(5 V,2 V,2000 us)
        .pin("B").vMeas().measWait(800 us)
        .pin("C").iPulse(1 mA,0.5 mA,2000 us).vMeas().measWait(800 us)
        .execute();
```

### Example（取自子主题 SmartRDI  DC test setup › DC test with digital channels › Setting up PPMU with SmartRDI）

```
ON_FIRST_INVOCATION_BEGIN();
  RDI_BEGIN();
    rdi.dc("id1").pin("PinA").vForce(0 V).valueMode(TA::BADC).iMeas().execute();
    rdi.dc("id2").pin("pinB").iForce(1 mA).vMeas().execute();
  RDI_END();
ON_FIRST_INVOCATION_END();

double res1=rdi.id("id1").getValue();
double res2=rdi.id("id2").getValue();
```

### Example（取自子主题 SmartRDI  DC test setup › DC test with digital channels › Setting up Board ADC with SmartRDI）

```
ON_FIRST_INVOCATION_BEGIN();
  RDI_BEGIN();
    rdi.dc("rly1").pin("DATA1",TA::BADC).vMeas().execute();
  RDI_END();
ON_FIRST_INVOCATION_END();
double val;
val=rdi.id("rly1").getValue("DATA1");
```

### Example（取自子主题 SmartRDI  DC test setup › DC test with digital channels › Setting up SPMU with SmartRDI）

```
ON_FIRST_INVOCATION_BEGIN();
  rdi.dc(0).pin("DATA1",TA::SPMU).iForce(2 mA).vMeas().execute();
ON_FIRST_INVOCATION_END();
double val;
val=rdi.id(0).getValue("DATA1");
```

### Examples（取自子主题 SmartRDI  DC test setup › Setting up DC Scale pins with SmartRDI）

### PMU (SIG) operating mode

```
rdi.dc().pin("DCS_SIG").vForce(2 V).vForceRange(25 V).iForceRange(100 uA).execute();

RDI_BEGIN();

    rdi.dc().pin("DCS_SIG").iMeasRange(100 uA).execute();
    rdi.dc().pin("DCS_SIG").vForce(10 V).execute();
    rdi.dc().pin("DCS_SIG").iMeas().execute();
    rdi.dc().pin("DCS_SIG").vForce(8 V).execute();
    rdi.dc().pin("DCS_SIG").iMeas().execute();

RDI_END();

rdi.dc().pin("DCS_SIG").disconnect().execute();
```

### DPS operating mode

```
rdi.dc().pin("DCS_DPS").connect().execute();

RDI_BEGIN();

    rdi.dc().pin("DCS_DPS").vForce(10 V).execute();
    rdi.dc().pin("DCS_DPS").iMeas().execute();
    rdi.dc().pin("DCS_DPS").vForce(8 V).execute();
    rdi.dc().pin("DCS_DPS").iMeas().execute();

RDI_END();

rdi.dc().pin("DCS_DPS").disconnect().execute();
```

### Examples（取自子主题 SmartRDI  Digital capture test setup › Generating a new digital capture pattern with SmartRDI）

### Digital capture without hidden upload

```
ON_FIRST_INVOCATION_BEGIN();
  RDI_BEGIN();
    rdi.digCap("cap").pin("DO").samples(100).initDiscard(10).interSkip(1,2).execute();
  RDI_END( );
ON_FIRST_INVOCATION_END();
const  ARRAY_I& aiData = rdi.id("cap").getVector("DO");
```

### Digital capture with hidden upload

```
run()
{
  ON_FIRST_INVOCATION_BEGIN();
    rdi.hiddenUpload(TA::DIGCAP);
    RDI_BEGIN();
      rdi.digCap("id2").pin("A").samples(1024).execute();
    RDI_END();
  ON_FIRST_INVOCATION_END();
  SMC_ARM();
}
...
public:
void SMC_backgroundProcessing()
{
  ARRAY_I bits = rdi.id("id2").getVectorBit();
}
```

### Example（取自子主题 SmartRDI  Digital capture test setup › Inserting digital capture actions in an existing pattern with SmartRDI）

```
RDI_BEGIN();
  rdi.digCap("mps").label("lpDcap_new").pin("DATA2,DATA6").addVecRange(3,15).samples(10).execute();
RDI_END();
```

In this example, the digital capture actions will be inserted in the vector range (3,15) of the pattern `lpDcap_new` for the pin `DATA2` and `DATA6`. 10 samples are captured for each pin. The following two figures shows the existing pattern and the pattern generated after inserting the digital capture actions.

!`Existing pattern`（raw: `../../../../agent-html/144585.png`） !`After inserting capture actions`（raw: `../../../../agent-html/144586.png`）

### Examples（取自子主题 SmartRDI  Digital capture test setup › Using Immediate Upload in SmartRDI）

### Using immediate upload for data upload only

In the example below, `digCapImmediateUpload()` is used alone to upload digital capture data immediately while the test is running. The upload of the captured data referenced by "resultId" is started while the burst is executed.

```
rdi.digCapImmediateUpload("resultId");

RDI_BEGIN();
   rdi.digCap("resultId").samples(...)...execute();
   ...
RDI_END(); // Raw Result upload within pattern run

rdi.id("resultId").getVector();
```

### Using immediate upload for data upload and result calculation

In the example below, `digCapImmediateUpload()` is used together with `getImmediateVector()` to upload digital capture data as well as hide result calculation while the test is running.

```
rdi.digCapImmediateUpload("resultId");

RDI_BEGIN();
    rdi.digCap("resultId").samples(SAMPLE_SIZE).bitPerWord(BPW).execute();
RDI_END( TA::NON_BLOCKING);

bool dataIsRemaining;
ARRAY_I resultChunk;
ARRAY_I uploadDataOffset(MAX_SITE_NUM);

while (dataIsRemaining)
    {dataIsRemaining = false;
    FOR_EACH_SITE_BEGIN()
    site = CURRENT_SITE_NUMBER();
    if (uploadDataoffset[site] < SAMPLE_SIZE/BPW-1)
    {resultChunk=rdi.id("resultId").getImmediateVector(uploadDataOffset[site]);
    uploadDataOffset[site] += resultChunk.size();
    dataIsRemaining = true;
//-------------- calculation e.g. fill histogram array  ---------------------------------
    }
    FOR_EACH_SITE_END()锛?}
RDI_WAIT_TEST_DONE();
```

`getImmediateVector()` returns an array of vectors. The array size in SER mode is calculated by dividing sampleSize with bitPerWord. So in this example, the maximum array size equals to SAMPLE_SIZE divided by BPW. Pay attention that in serial mode, the default setting for bitPerWord is 32.

In offline mode, the chunk size from each `getImmediateVector()` upload is 0. A working online code may cause an endless loop in offline execution. It is recommended to define an extra end loop criterion, for example, define the maximum number of loop executions.

Important: With SmarTest7.4.3.0 and 7.4.3.1, immediate upload only allows ONE result id in a pin.

### Syntax（取自子主题 SmartRDI  Digital capture test setup › addVecRange）

```
addVecRange(int iRangeBf, int iRangeAft);
```

Parameter List
| Parameter | Description |
|---|---|
| iRangeBf | The start vector to do the digital capture. |
| iRangeAft | The end vector to do the digital capture. |

### Examples（取自子主题 SmartRDI  Digital capture test setup › addVecRange）

### Generic example

```
rdi.digCap("norm").label("lpDcap_new").pin("DATA2").addVecRange(3,15).samples(10).execute();
```

Please note that `addVecRange()` should always be used together with `rdi.digCap().label()`.

### For multiple positions with cont()

```
rdi.digCap().pin("A").samples(100).cont();
rdi.digCap().pin("A").addVecRange(3,6).cont();
rdi.digCap().pin("A").addVecRange(10,20).cont();
rdi.digCap().execute();
```

### For multiple positions without cont()

```
rdi.digCap().pin("A").samples(100)
                    .addVecRange(3,6)
                    .addVecRange(10,20)
                    .execute();
```

### A range from a parameter list

```
rdi.digCap().pin("A").samples(100).cont();
   for (i = 0; i < listSize(); i++)
     rdi.digCap().pin("A").addVecRange(beginVec[i],endVec[i]).cont();
rdi.digCap().execute();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › bitPerWord）

```
bitPerWord(int iBit);
```

Parameter List
| Parameter | Description |
|---|---|
| iBit | The number of bits. The default value is 32. |

### Example（取自子主题 SmartRDI  Digital capture test setup › bitPerWord）

```
rdi.digCap("norm").label("lpDcap_new").pin("DATA2").addVecRange(3,15).samples(10).bitPerWord(4).execute();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › burstUpload）

```
burstUpload();
```

### Examples（取自子主题 SmartRDI  Digital capture test setup › burstUpload）

### Common upload with separated results retrieval

This example uses `burstUpload()` to combine multiple results into a common upload, and retrieves results one by one through individual result ID.

```
RDI_BEGIN();
 ...
   rdi.digCap().burstUpload().begin();
      rdi.smartVec();             // register setting 1
      rdi.digCap("10M").pin(A).samples(1000).execute();
      rdi.smartVec();            // register setting 2
      rdi.digCap("20M").pin(A).samples(2000).execute();
      rdi.smartVec();            // register setting 3
      rdi.digCap("30M").pin(A).samples(4000).execute();
   rdi.digCap().burstUpload().end();
 ...
RDI_END();

ARRAY_I vec1,vec2,vec3;
vec1=rdi.id("10M").getVectorBit();
vec2=rdi.id("20M").getVectorBit();
vec3=rdi.id("30M").getVectorBit();
```

### Common upload with combined results retrieval

This example uses `burstUpload()` to combine multiple results into a common upload, and retrieves combined results through a common result ID.

```
RDI_BEGIN();
 ...
   rdi.digCap("bid").burstUpload().begin();
      rdi...
      rdi.digCap().pin(A).samples(1000).execute();
      rdi...
      rdi.digCap().pin(A).samples(2000).execute();
      rdi...
      rdi.digCap().pin(A).samples(4000).execute();
   rdi.digCap().burstUpload().end();
 ...
RDI_END();

rdi.id("bid").getVector();
rdi.id("bid").getVectorBit();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › capMode）

```
capMode(TA::DCAP_MODE mode);
```

List of parameters
| Parameter | Description |
|---|---|
| mode | The digital capture mode. |

List of available options of parameter: mode
| Option | Description |
|---|---|
| TA::SER | The serial digital capture mode.<br><br>A vector variable is created for each capture pin with the specified number of bits per word. |
| TA::PAR | The parallel digital capture mode.<br><br>A vector variable is created for all capture pins with one sample per word. |

### Example（取自子主题 SmartRDI  Digital capture test setup › capMode）

```
rdi.digCap("cap").pin("DATA1,DATA2").capMode(TA::SER).samples(100).execute();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › copyLabel）

```
label("Label").copyLabel(boolVar);
```

List of parameters
| Parameter | Description |
|---|---|
| boolVar | Specifies whether to edit an existing pattern, or create a copy from an existing pattern and edit the copied pattern. |

List of available options of parameter: bool
| Option | Description |
|---|---|
| true | Make a copy of an existing pattern and edit the copied pattern.<br><br>This is the default value. |
| false | Edit an existing pattern. |

Return value

There is no return value.

### Example（取自子主题 SmartRDI  Digital capture test setup › copyLabel）

```
RDI_BEGIN();
...
  rdi.digCap().label("Label").copyLabel(false).pin("A").addVecRange(0,100).samples(100).execute();
...
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › enPassFail）

```
enPassFail();
```

### Example（取自子主题 SmartRDI  Digital capture test setup › enPassFail）

```
RDI_BEGIN();
  rdi.tmu("a").label("label1").pin("A")....enPassFail().execute()
  rdi.dc("b").label("label2").pin("B")....enPassFail().execute();
  rdi.digCap("c").label("label3").pin("C")....enPassFail().execute();
RDI_END();

rdi.id("a").getPassFail();
rdi.id("b").getPassFail();
rdi.dc("c").getPassFail();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › format）

```
format(enum format);
```

List of parameters
| Parameter | Description |
|---|---|
| format | A data format to be used in a digital capture test.<br><br>The data format can be one of:<br><br>BIN, COMP1, COMP2, MOD_COMP1, SYMM, MOD_SYMM, GRAY, BCD, ALAW, MOD_ALAW, and MSB.<br><br>For more information about the format definition, see `Code Format Tables`（raw: `02.07.04.04_Code_Format_Tables.md`）. |

### Example（取自子主题 SmartRDI  Digital capture test setup › format）

```
RDI_BEGIN()
rdi.digCap("id1").pin("pinA").format(TA::COMP).samples(1024).bitPerWord(16).execute();
rdi.digCap("id2").pin("GroupB").format(TA::GRAY).capMode(TA::PAR).samples(1000).execute();
RDI_END();
rdi.id("id1").getVector();
rdi.id("id2").getVector();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › initDiscard）

```
initDiscard(long iInitSkipSamples);
```

List of parameters
| Parameter | Description |
|---|---|
| iInitSkipSamples | The number of initial samples to be skipped.<br><br>For different types of cores, default values are different:<br><br>- LF core: Default value is 64.<br>- VHF or IQ core: With oversampling, the default value 64; without oversampling, the default value is 0.<br>- Other cores: Default value is 0. |

### Example（取自子主题 SmartRDI  Digital capture test setup › initDiscard）

```
rdi.digCap("cap").pin("DATA1").samples(100).initDiscard(10).interSkip(1,2).execute();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › interSkip）

```
interSkip(int iBlockLength ,int iInterSkipSamples);
```

Parameter List
| Parameter | Description |
|---|---|
| iBlockLength | The number of samples to capture |
| iInterSkipSamples | The number of samples to discard |

### Example（取自子主题 SmartRDI  Digital capture test setup › interSkip）

```
rdi.digCap("norm").label("lpDcap_new").pin("DATA2").samples(100).interSkip(2,3).execute();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › label）

```
label(const string& sLabelName);
```

Parameter List
| Parameter | Description |
|---|---|
| sLabelName | The label name |

### Example（取自子主题 SmartRDI  Digital capture test setup › label）

```
RDI_BEGIN();
  rdi.digCap("norm").label("lpDcap_new").pin("DATA2").addVecRange(3,15).samples(10).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › pin）

```
pin(const string& sPin);
```

List of parameters
| Parameter | Description |
|---|---|
| sPin | The digital capture pin. |

### Example（取自子主题 SmartRDI  Digital capture test setup › pin）

```
rdi.digCap("cap").pin("DO").samples(100).execute();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › samples）

```
samples(long iSamples);
```

List of parameters
| Parameter | Description |
|---|---|
| iSamples | The number of samples. |

```

```

### Example（取自子主题 SmartRDI  Digital capture test setup › samples）

```
rdi.digCap("cap").pin("DATA1").samples(100).execute();
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › vecVar）

```
vecVar(string);
```

### Example（取自子主题 SmartRDI  Digital capture test setup › vecVar）

```
RDI_BEGIN();
  rdi.digCap("id").label("userLabel").vecVar("vvName1").vecVar("vvName2").execute();
RDI_END(); // "vvName1" and "vvName2" must already exist in the user pattern.

ARRAY_I ary = rdi.id("id").getVectorFromVV("vvName1");
ARRAY_I ary2 = rdi.id("id").getVectorFromVV("vvName2");
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › vecVarOnly）

`vecVarOnly()`

### Example（取自子主题 SmartRDI  Digital capture test setup › vecVarOnly）

```
RDI_BEDIN();
  rdi.digCap("dcap").vecVarOnly().pin("pinA").samples(100).execute();
  rdi.func("id2").label("label").execute();
RDI_END();

const ARRAY_I& aiData = rdi.id("dcap").getVector()
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › getVector）

```
ARRAY_I& getVector(const string& pin);
```

Parameter
| Parameter | Description |
|---|---|
| pin | The pin to query. |

### Return value（取自子主题 SmartRDI  Digital capture test setup › getVector）

The reference to an ARRAY_I object containing the captured data of words.

### Examples（取自子主题 SmartRDI  Digital capture test setup › getVector）

```
const ARRAY_I& aiData = rdi.id("cap").getVector("DATA1");
```

```
...
// gpDATA is a pin group which has DATA1 and DATA2.
rdi.digCap("cap").pin("gpDATA").samples(100).execute();
...
// Do not use a pin group name here and must use a pin list.
ARRAY_I ar = rdi.id("cap").getVector("DATA1,DATA2");
```

 Note For the parallel transfer mode, the pin list must be used in getVector() even though the pin group has been used in the setup part.

### Syntax（取自子主题 SmartRDI  Digital capture test setup › getVectorBit）

```
ARRAY_I& getVectorBit(const string& pin);
```

Parameter List
| Parameter | Description |
|---|---|
| pin | The pin to retrieve. |

### Example（取自子主题 SmartRDI  Digital capture test setup › getVectorBit）

```
ARRAY_I arr;
arr=rdi.id("norm").getVectorBit("pinA");
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › rdi.id  .getVectorFromVV）

```
ARRAY_I& getVectorFromVV(string variableName);
```

### Example（取自子主题 SmartRDI  Digital capture test setup › rdi.id  .getVectorFromVV）

```
RDI_BEGIN();
  rdi.digCap("id").label("userLabel").vecVar("vvName1").vecVar("vvName2").execute();
RDI_END();

ARRAY_I ary = rdi.id("id").getVectorFromVV("vvName1");
ARRAY_I ary2 = rdi.id("id").getVectorFromVV("vvName2");
```

### Syntax（取自子主题 SmartRDI  Digital capture test setup › getVecVar）

```
string getVecVar(const string& pin);
```

List of parameters
| Parameter | Description |
|---|---|
| pin | The pin to query. |

### Example（取自子主题 SmartRDI  Digital capture test setup › getVecVar）

```
rdi.id("dc_hidden_4pins").getVecVar("DATA2");
```

### Example（取自子主题 SmartRDI  Digital channel relay control）

```
RDI_BEGIN();
  rdi.hwRelay().pin("pinA").setOn("DC,AC").setOff("PPMU").execute();
  rdi.hwRelay().pin("pinB").setOff("ALL").execute();
RDI_END();
```

See `setOn()`（raw: `02.07.13.14.05_setOn.md`） for more information about AMUX_PPMU and AMUX_BADC relay options.

### Example（取自子主题 SmartRDI  DUT board connections control by Routing Tools › Routing Tools editors › Routing Tools - Global Setup editor）

The following code shows the contents of an XML file that has been generated by clicking on the Save button with no other settings defined.

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE DocType>
<switchtool>
  <global version="" timestamp="2017-04-12 17:15:28.154" checksum="" sitecount="8">
    <utility pogoblocksize="16" maxclockrate="" />
    <pmux failsitehandling="" failsitestate="" maxclockrate="" />
  </global>
  <utility>
    <ucontrol>
      <block number="1" mode="static" group="" fram="" sclk="" sinp="" sout="" port="" />
      <block number="2" mode="static" group="" fram="" sclk="" sinp="" sout="" port="" />
      <block number="3" mode="static" group="" fram="" sclk="" sinp="" sout="" port="" />
      <block number="4" mode="static" group="" fram="" sclk="" sinp="" sout="" port="" />
      <block number="5" mode="static" group="" fram="" sclk="" sinp="" sout="" port="" />
      <block number="6" mode="static" group="" fram="" sclk="" sinp="" sout="" port="" />
      <block number="7" mode="static" group="" fram="" sclk="" sinp="" sout="" port="" />
      <block number="8" mode="static" group="" fram="" sclk="" sinp="" sout="" port="" />
    </ucontrol>
    <uconfig />
  </utility>
  <pmux>
    <pcontrol>
      <module number="1" pogo1="865" id="01" group="" sda="" scl="" port="" />
      <module number="2" pogo1="867" id="02" group="" sda="" scl="" port="" />
      <module number="3" pogo1="869" id="03" group="" sda="" scl="" port="" />
      <module number="4" pogo1="871" id="04" group="" sda="" scl="" port="" />
      <module number="5" pogo1="873" id="09" group="" sda="" scl="" port="" />
      <module number="6" pogo1="875" id="10" group="" sda="" scl="" port="" />
      <module number="7" pogo1="877" id="13" group="" sda="" scl="" port="" />
      <module number="8" pogo1="879" id="14" group="" sda="" scl="" port="" />
      <module number="9" pogo1="881" id="05" group="" sda="" scl="" port="" />
      <module number="10" pogo1="883" id="06" group="" sda="" scl="" port="" />
      <module number="11" pogo1="885" id="07" group="" sda="" scl="" port="" />
      <module number="12" pogo1="887" id="08" group="" sda="" scl="" port="" />
      <module number="13" pogo1="889" id="11" group="" sda="" scl="" port="" />
      <module number="14" pogo1="891" id="12" group="" sda="" scl="" port="" />
      <module number="15" pogo1="893" id="15" group="" sda="" scl="" port="" />
      <module number="16" pogo1="895" id="16" group="" sda="" scl="" port="" />
    </pcontrol>
    <pconfig />
  </pmux>
  <setup>
    <header sequence="" offWait="" onWait="" wait="">
      <list />
    </header>
    <states />
  </setup>
</switchtool>
```

### Example 2: shortcut menu - Fill data（取自子主题 SmartRDI  DUT board connections control by Routing Tools › Routing Tools editors › Routing Tools - State Setup editor）

| !`Routing Tools - State Setup editor Context menus Fill states`（raw: `../../../../agent-html/343031.png`） | To select multiple cells: Click the upper left cell, press Shift and click the lower right cell. |
|---|---|

### Example 3: shortcut menu - Move column（取自子主题 SmartRDI  DUT board connections control by Routing Tools › Routing Tools editors › Routing Tools - State Setup editor）

|

!`Routing Tools - State Setup editor Context menus Move columns`（raw: `../../../../agent-html/343028.png`）

  | Moving columns is also supported by clicking the related cell of the header row (A, B, C, 鈥? and dragging the column to the new position. |

### Example 4: shortcut menu - Move row（取自子主题 SmartRDI  DUT board connections control by Routing Tools › Routing Tools editors › Routing Tools - State Setup editor）

|

!`Routing Tools - State Setup editor Context menus Move columns`（raw: `../../../../agent-html/346495.png`）

   | Moving rows is also supported by clicking the related cell of the first column (1, 2, 3, 鈥? and dragging the row to the new position. |

### Syntax（取自子主题 SmartRDI  DUT board connections control by Routing Tools › rdi.route）

Usage of the function:

- The function can be called in the code‑based mode or in the pattern‑based mode. For more information, refer to `Pattern-based mode`（raw: `02.07.13_SmartRDI.md#_142069__dle_Pattern-based_mode`） and `Code-based mode`（raw: `02.07.13_SmartRDI.md#_142069__dle_Code-based_mode`） in topic `SmartRDI`（raw: `02.07.13_SmartRDI.md`）.

```
routeGroup& route(const int id);
routeGroup& route(const string& id="");
```

List of parameters
| Parameter | Description |
|---|---|
| id | Optional ID for the following setups.<br><br>The parameter can be defined as int or as string.<br><br>Default value: Empty string "" |

### Return value（取自子主题 SmartRDI  DUT board connections control by Routing Tools › rdi.route）

A reference to the routeGroup object.

### Example 1（取自子主题 SmartRDI  DUT board connections control by Routing Tools › rdi.route）

```
RDI_INIT();
...
...
ON_FIRST_INVOCATION_BEGIN();
{
    ...
    ...
    RDI_BEGIN();
    {
        ...
        ...
        rdi.route().applyState("Connect_load").execute();
        ...
        ...
    }
    RDI_END();
    ...
    ...
}
ON_FIRST_INVOCATION_END();
...
...
```

### Example（取自子主题 SmartRDI  Error map results from user patterns）

This diagram shows an error map example.

 !`emap result`（raw: `../../../../agent-html/149581.png`）

In this example, results are:

- `failCount`= 3
- `failCyc`= 10, 14, 17
- `pfMap`= 1,1,1,1,0,1,1,1,0,1,1,0,1
- `FFC`= 10

The cycle number starts from "0".

The following example includes all functions of the emap() class:

```
ON_FIRST_INVOCATION_BEGIN();
rdi.emapLocation(TA::RAM);
RDI_BEGIN();
   rdi.emap("a").label("label1").pin("pA").failCount().pfMap()
                                .pin("pC").failCyc(5).execute();
   rdi.emap("b").label("label2").pin("pB").FFC(150).execute();
RDI_END();
ON_FIRST_INVOCATION_END();

int fcount=rdi.id("a").getFailCount("pA");
ARRAY_BOOL map=rdi.id("a").getPfMap("pA");
ARRAY_LL fcPostion=rdi.id("a").getFailCyc("pC");
int ffc=rdi.id("b").getFFC();
```

### Example（取自子主题 Functional test setup）

```
ON_FIRST_INVOCATION_BEGIN();
  RDI_BEGIN();
      rdi.func("f1").label("PATT1").execute();
      rdi.func().burst("BURST1").execute();
  RDI_END();
ON_FIRST_INVOCATION_END();
int result1 = rdi.id( "f1" ).getPassFail(); //result for PATT1
int result2 = rdi.getBurstPassFail(); // result for PATT1 and BURST1
```

### Example（取自子主题 SmartRDI  Level and timing set changes）

```
RDI_BEGIN();
  rdi.level().set(1);
  rdi.func().label("aaa").execute();
  rdi.timing().set(1);
  rdi.func().label("bbb").execute();
RDI_END();
```

### Example（取自子主题 SmartRDI  Pattern-based conditional jump - cogo › Structures of multiple cogo   nodes）

```
RDI_BEGIN();
  rdi.cogo().node("a",TA::ROOT).passNode("b").failNode("c").begin();
    rdi.func().label("abc").execute(); // Pass/fail judgment.
    rdi.cogo().wait(30 us);            // System-reserved waiting time.
  rdi.cogo().node().end();

  rdi.cogo().node("b").passNode("RETURN").failNode("RETURN").begin();
    rdi.dc().pin("VDD").iMeas().limit(0,1 mA).execute(); // Pass/fail judgment.
    rdi.cogo().wait(20 us);                    // System-reserved waiting time.
  rdi.cogo().node().end();

  rdi.cogo().node("c").passNode("RETURN").failNode("RETURN").begin();
    rdi.smartVec().pin("D1").expectData(0x55,8).execute(); // Pass/fail judgment.
    rdi.cogo().wait(30 us);                      // System-reserved waiting time.
  rdi.cogo().node().end();
RDI_END();
```

Each structure needs at least one ROOT node.

### Examples（取自子主题 SmartRDI  Pattern-based conditional jump - cogo › Sequencer-controlled searching with cogo）

### A binary search in a TRIM test

```
RDI_BEGIN();
  rdi.cogo("trim").search(TA::BINARY).pathPin("pinA")
                  .start(0).stop(0xff).init(0x88).step(4).blockBegin();
     rdi.smartVec().pin("SDA").writeData(0x53,8,0)
                              .writeData(rdi.searchInput(),8,16)
                              .execute();
     rdi.wait(100 us);
     rdi.dc().pin("LDO").vMeas().limit(0,5).execute(); // Pass/fail judgment.
     rdi.cogo().wait(100 us); // Time long enough for pass/fail judgment.
  rdi.cogo().search().blockEnd();
RDI_END();

rdi.id("trim").getSearchResult();
```

### A linear search in a Hysteresis test

```
RDI_BEGIN();
  rdi.cogo("cogo_hyst_linear").search(TA::HYST_LINEAR)
                              .pathPin("DATA3")
                              .start(0).stop(3).step(5).blockBegin();
      rdi.dc().pin("DATA1").vForce(rdi.searchInput()).execute();
      rdi.dc().pin("DATA2").iForce(0 mA).vMeas()
                           .measWait(100 us).limit(1.2,2.2).execute();
      rdi.wait(2 ms);
  rdi.cogo().search().blockEnd();
RDI_END()锛?
rdi.id("cogo_hyst_linear").getSearchResult();
```

### Result retrieval with pathPin()

```
RDI_BEGIN();
  rdi.cogo("cogo_sVec_linear").search(TA::LINEAR)
                              .pathPin("DATA11")
                              .start(0).stop(0xff).step(4).blockBegin();
     rdi.smartVec().pin("DATA1").writeData(rdi.searchInput(),8,16)
                   .pin("DATA2").expectData(0xAA,8,16).execute();
     rdi.cogo().wait(1 ms);
  rdi.cogo().blockEnd();
RDI_END();

rdi.id("cogo_sVec_linear").getSearchResult();

```

See also `pathPin()`（raw: `02.07.13.19.02.02_pathPin.md`）.

### Result retrieval without pathPin()

```
RDI_BEGIN();
  rdi.cogo("cogo_linear_wo_pathPin").search(TA::LINEAR)
                           .start(0).stop(0xff).step(4).blockBegin();
      rdi.smartVec().pin("DATA1 ").writeData(rdi.searchInput(),8,16)
                    .pin("DATA2").expectData(0xAA,8,16).execute();
      rdi.cogo().wait(1 ms);
  rdi.cogo().blockEnd();
RDI_END()

rdi.id("cogo_linear_wo_pathPin").getSearchResult();
```

See also `pathPin()`（raw: `02.07.13.19.02.02_pathPin.md`）.

### Syntax（取自子主题 SmartRDI  Testflow level burst and concurrency tests › postBurst）

```
postBurst()
```

### Example（取自子主题 SmartRDI  Testflow level burst and concurrency tests › postBurst）

This is a template for the code structure of concurrent test framework in SmartRDI.

```
#include "rdi.hpp"

class UserClassName: public CCTestMethod_SYNC
{
protected:
...
  virtual void preStart()
  {  // Static commands before burst pattern execution
  }
  virtual void burstRun()
  {  // Pattern-based SmartRDI commands
  }
  virtual void postBurst()  // New in SmartRDI 2.5.1
  {  // Static commands after the burst pattern execution
   }
  virtual void postProcess()
  {  // Result retrieval, calculation, and datalog
   }
...
};
REGISTER_TESTMETHOD("UserClassName", UserClassName);
```

### Examples（取自子主题 SmartRDI  TMU test setup）

### Creating an independent TMU measurement

```
RDI_BEGIN();

    rdi.tmu("1").pin("PVI8_1")
            .vth(3.0 V, 5.0 V)
            .samples(4)
            .measMode(TA::PULSE_HIGH)
            .execute();

    rdi.wait(1 ms);

RDI_END();
```

The `execute()` here means the start of the TMU measurement. The TMU measurement takes place in the next event within this RDI_BEGIN/END() block.

### Inserting a TMU measurement into an existing pattern

```
RDI_BEGIN();

    rdi.tmu("id").label("func1").pin("DATA1")
            .insertVec(200)
            .vth(1.5 V)
            .samples(2)
            .measMode(TA::RISE_FALL)
            .execute();

RDI_END();
```

In this example, a TMU measurement is inserted into a copy of the func1 pattern.

### Syntax（取自子主题 SmartRDI  Tool functions › getLabelCycleNum）

```
int getLabelCycleNum(string Label);
```

List of parameters
| Parameter | Description |
|---|---|
| Label | A single label's name. |

Return value

There is no return value.

 Note This command is not thread-safe. DO NOT put it into the `SMC_backgroundProcessing()`（raw: `02.07.04.01.231.01_SMC_ARM.md#_120107__s_SMC_backgroundProcessing`） function.

### Example（取自子主题 SmartRDI  Tool functions › getLabelCycleNum）

```
int iCycle=rdi.getLabelCycleNum("Label");
```

### Syntax（取自子主题 SmartRDI  Tool functions › Global variables › setGlobalVar）

```
void rdi.setGlobalVar(variable_name, value)
```

List of parameters
| Parameter | Description |
|---|---|
| variable_name | The name of the variable to which you want to assign the value. A string. |
| value | The value to assign to the variable. The value must have one of these data types:<br><br>- int<br>- double<br>- ARRAY_I<br>- ARRAY_D<br>- vector<ARRAY_I><br>- vector<ARRAY_D> |

### Example（取自子主题 SmartRDI  Tool functions › Global variables › setGlobalVar）

This example assigns the value of a program variable (myVar) to the SmartRDI variable abc.

```
int myVar = 100;
rdi.setGlobalVar("abc",myVar);
```

### Syntax（取自子主题 SmartRDI  Tool functions › Global variables › getGlobalVar）

```
bool rdi.getGlobalVar(variable_name,value);
```

Parameters
| Parameter | Description |
|---|---|
| variable_name | The name of the variable to which you want to assign the value. A string. |
| value | The value to assign to the variable. The value must have one of these data types:<br><br>- int<br>- double<br>- ARRAY_I<br>- ARRAY_D<br>- vector<ARRAY_I><br>- vector<ARRAY_D> |

### Return Value（取自子主题 SmartRDI  Tool functions › Global variables › getGlobalVar）

This function returns true if the specified SmartRDI variable exists. Otherwise, it returns false.

### Example（取自子主题 SmartRDI  Tool functions › Global variables › getGlobalVar）

```
if (rdi.getGlobalVar("abc",b))  cout<<b<<end;
```

### Syntax（取自子主题 SmartRDI  Tool functions › dtos）

```
string rdi.dtos(double)
```

### Example（取自子主题 SmartRDI  Tool functions › dtos）

```
double d =100.001;
string str=rdi.dtos(d); // str = "100.001"
```

### Syntax（取自子主题 SmartRDI  Tool functions › itos）

```
string rdi.itos(integerVal);
```

### Example（取自子主题 SmartRDI  Tool functions › itos）

```
long long l = 100;
string str = rdi.itos(l); // str = "100"
```

### Syntax（取自子主题 SmartRDI  Tool functions › itos hex）

```
string rdi.itos_hex(integerVal);
```

### Syntax（取自子主题 SmartRDI  Tool functions › reverseBits）

```
long long rdi.reverseBits(long long data, int bitLen);
```

List of parameters
| Parameter | Description |
|---|---|
| bitLen | Bit length. |

### Syntax（取自子主题 SmartRDI  Tool functions › getCommentCycleNum）

```
int& rdi.getCommentCycleNum(string labelName,string comment);
```

Parameters
| Parameter | Description |
|---|---|
| labelName | The name of the pattern in which you want to retrieve a comment's cycle number. A string. |
| comment | The string of the comment for which you want to retrieve its cycle number in the pattern specified with labelName. |

### Return Value（取自子主题 SmartRDI  Tool functions › getCommentCycleNum）

This function returns a cycle number in integer.

 Note This command is not thread-safe. DO NOT put it into the SMC_BackgroundProcessing() function.

### Example（取自子主题 SmartRDI  Tool functions › getCommentCycleNum）

```
// Return the cycle number of the comment string "trigger" in label "modeSet".
int trigCyc=rdi.getCommentCycleNum("modeSet","trigger");

// If necessary, use waitCyc() to align the action with the position of a comment in a pattern.
RDI_BEGIN();
    rdi.port("A").func().label("modeSet").execute();
    rdi.port("B").waitCycle(trigCyc);
    rdi.port("B").dc().pin(VI).samples(1000).FS(50 KHz).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Tool functions › getCommentVectorNum）

```
int& rdi.getCommentVectorNum(string labelName,string comment);
```

Parameters
| Parameter | Description |
|---|---|
| labelName | The name of the pattern in which you want to retrieve a comment's vector number. A string. |
| comment | The string of the comment for which you want to retrieve its vector number in the pattern specified with labelName. |

### Return Value（取自子主题 SmartRDI  Tool functions › getCommentVectorNum）

This function returns a vector number in integer.

 Note This command is not thread-safe. DO NOT put it into the SMC_BackgroundProcessing() function.

### Example（取自子主题 SmartRDI  Tool functions › getCommentVectorNum）

```
// Return the vector number of the comment string "trigger" in label "modeSet".
int trigCyc=rdi.getCommentVectorNum("modeSet","trigger");

// If necessary, use waitCyc() to align the action with the position of a comment in a pattern.
RDI_BEGIN();
    rdi.port("A").func().label("modeSet").execute();
    rdi.port("B").waitCycle(trigCyc);
    rdi.port("B").dc().pin(VI).samples(1000).FS(50 KHz).execute();
RDI_END();
```

### Example（取自子主题 SmartRDI  Utility lines control）

```
class RDI_STAT_UTIL: public testmethod::TestMethod
{
    protected:

    string sMode;
    STRING_VECTOR utilitylineStatus_1,utilitylineStatus_2,utilitylineStatus_3;

    virtual void initialize()
    {
        addParameter("RDIMode","string",&amp;sMode, testmethod::TM_PARAMETER_INPUT).setOptions("SINGLE:BURST:PROD").setDefault("BURST");
    }

    virtual void run()
    {
        RDI_INIT();

        ON_FIRST_INVOCATION_BEGIN();

            //
            // Select smartRDI Mode
            //
            TA::USER_RUN_MODE mode;

            if      (sMode == "SINGLE") mode     = TA::SINGLE;
            else if (sMode == "BURST")  mode = TA::BURST;
            else if (sMode == "PROD")   mode = TA::PROD;

            utilitylineStatus_1 = GET_UTILITY_LINES_STATUS(0);

            //
            // Set 4 util lines of util block 2-9 defined in pin file
            //
            rdi.util().pin("SEQ_LED_201,SEQ_LED_207, SEQ_LED_209,SEQ_LED_215").setOn().execute();
            rdi.wait(2 ms);
            utilitylineStatus_2 = GET_UTILITY_LINES_STATUS(0);

            //
            // Reset 4 util lines of util block 2-9 defined in pin file
            //
            rdi.util().pin("SEQ_LED_201,SEQ_LED_207,SEQ_LED_209,SEQ_LED_215").setOff().execute();
            rdi.wait(4 ms);
            utilitylineStatus_3 = GET_UTILITY_LINES_STATUS(0);

        ON_FIRST_INVOCATION_END();

        //
        // Datalog
        //
        cout << "after reset" << endl;

        for(int i=1; i<9;i++)
        {
            cout << "STAT_UTIL" << i << " = " << utilitylineStatus_1[i-1] << endl;
        }

        cout << "after set on" << endl;

        for(int i=1; i<9;i++)
        {
            cout << "STAT_UTIL" << i << " = " << utilitylineStatus_2[i-1] << endl;
        }
        cout << "after set off" << endl;

        for(int i=1; i<9;i++)
        {
            cout << "STAT_UTIL" << i << " = " << utilitylineStatus_3[i-1] << endl;
        }

        return;
    }

    virtual void postParameterChange(const string&amp; parameterIdentifier)
    {
        return;
    }

    virtual const string getComment() const
    {
        string comment = "please add your comment for this method.";
        return comment;
    }
};
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › bitLength）

```
bitLength(int length);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

length

 |

The length of the bit stream.

   | Note If the pattern contents exceed the length defined by the bitLength() parameter, the length of the generated pattern refers to the actual contents' length.

### Example（取自子主题 SmartRDI  Vector and protocol programming › bitLength）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").defaultBit(0).bitLength(10).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › burstLabel）

```
burstLabel(const string &labelName);
burstLabel(const string &labelName,TA::MD5_OPTION);
```

List of parameters
| Parameter | Description |
|---|---|
| labelName | The specified name of the big label.<br><br>The label name can be as long as 128 characters at maximum. |
| TA::MD5_OPTION | The option which defines to use an MD5 postfix string or not in the label name. |

List of available options of parameter: <TA::MD5_OPTION>
| Option | Description |
|---|---|
| TA::MD5_ON | With an MD5 postfix string in the label name. This is the default value.<br><br>With MD5_ON, the maximum length of a valid "targetLabelName" in the generated pattern name is 74. |
| TA::MD5_OFF | Withou an MD5 postfix string in the label name.<br><br>With MD5_OFF, the maximum length of a valid "targetLabelName" in the generated pattern name is 111. |

### Example 1（取自子主题 SmartRDI  Vector and protocol programming › burstLabel）

```
...
RDI_BEGIN();
  rdi.smartVec().burstLabel("burstlabel").begin();
    rdi.smartVec().pin("DATA1").writeVec("01",2).execute();
    rdi.smartVec().pin("DATA3").fillBit(1,8,4).execute();
    rdi.smartVec().pin("DATA7").writeData(0x54,8,4).execute();
  rdi.smartVec().burstLabel().end();
RDI_END();

// Allow repeat() and wait() in burstLabel() in SmartRDI 2.3.1
RDI_BEGIN();
  rdi.smartVec().burstLabel("burstlabel").begin();
    rdi.smartVec().pin("DATA1").writeVec("01",2).repeat(2).execute();
    rdi.wait(1 ms);
    rdi.smartVec().pin("DATA3").fillBit(1,8,4).repeat(3).execute();
    rdi.wait(1 ms);
    rdi.smartVec().pin("DATA7").writeData(0x54,8,4).repeat(4).execute();
  rdi.smartVec().burstLabel().end();
RDI_END();

// Allow to get the Pass-Fail result with burstLabel() in SmartRDI 2.3.1
RDI_BEGIN();
  rdi.smartVec("pf_result").burstLabel("burstlabel").enPassFail().begin();
    rdi.wait(1 ms);
    rdi.smartVec().pin("DATA3"). writeData(0x54,8,4)
                  .pin("DATA4"). expectData(0x54,8,4)
                  .repeat(3).execute();
    rdi.wait(1 ms);
rdi.smartVec().pin("DATA5"). writeData(0x55,8,24)
                  .pin("DATA6"). expectData(0x55,8,24)
                  .repeat(3).execute();
    rdi.smartVec().burstLabel().end();
RDI_END();
...
int passfail_result=rdi.id("pf_result").getPassFail();
```

Note The resulting "big pattern" is automatically reusable. If the content is changed, the postfix of the pattern name will be changed and a new pattern will be created. If the content is not changed, SmartRDI will reuse the existing pattern. An md5 postfix string will be added to the created label.

### Example 2（取自子主题 SmartRDI  Vector and protocol programming › burstLabel）

```
burstLabel("abc")              // The default is with an MD5 postfix
burstLabel("abc",TA::MD5_ON)   // With an MD5 postfix
burstLabel("abc",TA::MD5_OFF)  // Without an MD5 postfix
```

Note In case that the MD5 postfix option is OFF, make sure that if the content is different, the label name must be different.

### Example 3（取自子主题 SmartRDI  Vector and protocol programming › burstLabel）

```
RDI_BEGIN();
  ...
  rdi.smartVec("pf").burstLabel("abc").enPassFail().begin();
    rdi.smartVec()...
    ...
  rdi.smartVec().burstLabel().end();
  ...
RDI_END();

Rdi.id("pf").getPassFail();
```

### Example 4（取自子主题 SmartRDI  Vector and protocol programming › burstLabel）

Since SmartRDI 2.4.4, the combination of run-time accesses for the VTT mode within a `burstLabel().begin()`/`burstLabel().end()` block is supported.

```
rdi.smartVec().vecEditMode(TA::VTT);
rdi.runTimeVal("rtData",rtData);

RDI_BEGIN();
  rdi.smartVec().burstLabel("abc").begin();
  for(int k=0;k<64;k++)  // 64 vector segments to edit in run time
  {
    rdi.smartVec().pin("DATA1").writeData("rtData",16,0).vecLength(160).execute();
  }
  rdi.smartVec().burstLabel().end();
RDI_END();
```

There should be no instructions like MACT, RPTV, JSUB inside the burst label.

### Example 5（取自子主题 SmartRDI  Vector and protocol programming › burstLabel）

Before SmartRDI 2.4.5, the `rdi.smartVec().burstLabel().begin()/rdi.smartVec().burstLabel().end()` block can only be used for a single port.

SmartRDI 2.4.5 supports the combination of multiple parallel `execute()` commands for specified ports by `rdi.port().smartVec().burstLabel()`. It also supports the combined usage with `portSync()`. See example below.

 !`burstLabel()_for_ports_with_portSync()`（raw: `../../../../agent-html/153089.png`）

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › burstUpload）

```
burstUpload();
```

### Example（取自子主题 SmartRDI  Vector and protocol programming › burstUpload）

```
// you can get a combined result of all readBit()/readData() inside burstUpload.begin()/end() from only one id.
ON_FIRST_INVOCATION_BEGIN();

rdi.smartVec().readMode(TA::EMAP);  // TA::DIGCAP

RDI_BEGIN();
rdi.smartVec("id").burstUpload().begin();
rdi.smartVec(id1).pin("DATA2").readBit(2,2).execute();
rdi.smartVec(id2).pin("DATA2").readBit(4,4).execute();
rdi.smartVec(id3).pin("DATA4").readData(8,8).execute();
rdi.smartVec(id4).pin("DATA4").readData(8,12).execute();
rdi.smartVec().burstUpload().end();
RDI_END();

ON_FIRST_INVOCATION_END();

ARRAY_I bitResult=rdi.id("id").getReadBit("DATA2");
ARRAY_LL dataResult=rdi.id("id").getReadData("DATA4");
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › comment）

```
comment(const string &comment, int vecNum);
```

List of parameters
| Parameter | Description |
|---|---|
| comment | The content to be added. |
| vecNum | The position of the vector. |

See `SMV_IGNORE_COMMENT`（raw: `02.07.13.04_RDI_Configure_file.md#_146692__row_SMV_IGNORE_COMMENT`）, which can be used in the `RDI_Configure file`（raw: `02.07.13.04_RDI_Configure_file.md`） to globally disable comment output in pattern generation.

### Examples（取自子主题 SmartRDI  Vector and protocol programming › comment）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeData(0x54,8).comment("MSB",0).comment("LSB",8).execute();
RDI_END();
```

   Note Adding comments significantly increases the time for pattern generation (first-run). To reduce the first-run time, you can remove the comment commands from your code after the pattern generation and debugging have been finished.

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › copyLabel）

```
label("Label").copyLabel(boolVar);
```

List of parameters
| Parameter | Description |
|---|---|
| boolVar | Specifies whether to edit an existing pattern, or create a copy from an existing pattern and edit the copied pattern. |

List of available options of parameter: bool
| Option | Description |
|---|---|
| true | Make a copy of an existing pattern and edit the copied pattern.<br><br>This is the default value. |
| false | Edit an existing pattern. |

Return value

There is no return value.

### Example（取自子主题 SmartRDI  Vector and protocol programming › copyLabel）

```
RDI_BEGIN();
...
 rdi.smartVec().label("label4").copyLabel(false).pin("D3").writeData(0x55,8,0).execute();
...
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › defaultBit）

```
defaultBit(int bit);
defaultBit(string bit);
```

List of parameters
| Parameter | Description |
|---|---|
| bit | The bit or string you want to write into the pattern. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › defaultBit）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").bitLength(20).defaultBit(0).execute();
RDI_END();
```

Supporting a string

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").bitLength(20).defaultBit("L").execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › defaultVec）

```
defaultVec(int index);
defaultVec(string dvc);
```

List of parameters
| Parameter | Description |
|---|---|
| index | The physical index you want to write to the pattern . |
| dvc | The device cycle you want to write to the pattern. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › defaultVec）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").defaultVec(0).vecLength(10).execute();   // index
rdi.smartVec().pin("DATA3").defaultVec("1").vecLength(10).execute(); // device cycle
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › download）

```
download();
```

 A statement example that download() works together with write...() and expect...() commands:

```
rdi.smartVec().pin(pName).write...("rtData",...).download();
```

```
rdi.smartVec().pin(pName).expect...("rtData",...).download();
```

### Examples（取自子主题 SmartRDI  Vector and protocol programming › download）

### download() code structure

```
ARRAY_LL rtData = ...
rdi.runTimeVal("rtD", rtData);

//Download value into the existing pattern label "abc"
rdi.smartVec().label("abc").copyLabel(false).pin("D1").writeData("rtD",8).download();

//Create a new label "cde" based on code and download runtime data in it.
rdi.smartVec().pin("D2").defaultBit(1).writeData("rtD",8,10).labelName("cde").download();

```

### Hidden vector download

```
ARRAY_LL rtData= ...
rdi.runTimeVal("rtData", rtData);

RDI_BEGIN();
...
RDI_END(TA::NON_BLOCKING);

rdi.smartVec().pin(pinA).writeData("rtData",8).labelName("abc").download();
...
RDI_WAIT_TEST_DONE();
```

### Using copyLabel(false) and download() together

```
RDI_BEGIN();
  rdi.func("id1").label("label1").execute(); // measurement
  rdi.digCap().pin(A).samples(5).execute();  // measurement
RDI_END(TA::NON_BLOCKING);

rdi.smartVec().label("abc").copyLabel(false).pin("pinA").writeData("rtD",8).download();
// HVD to the existing pattern "abc" without creating a new pattern.

RDI_WAIT_TEST_DONE();
```

### NON_BLOCKING starts at the second run

```
RDI_BEGIN()
  rdi.dc().pin("dig").vForce(1).iMeas().execute();
RDI_END(TA::NON_BLOCKING)

rdi.smartVec() label("abc").copyLabel(false).pin("pinA").writeData("rtD",8).download();

RDI_WAIT_TEST_DONE();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › emapLocation）

```
emapLocation(TA::EMAP_LOCATION loc);
```

List of parameters
| Parameter | Description |
|---|---|
| TA::EMAP_LOCATION loc | The location where error maps are stored. |

List of available options of parameter: <TA::EMAP_LOCATION loc>
| Option | Description |
|---|---|
| TA::TP | The location is the test processor on the card. The default value. |
| TA::RAM | The location is the unused vector memory on the tester. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › emapLocation）

```
rdi.emapLocation(TA::RAM);
rdi.smartVec().readMode(TA::EMAP)

RDI_BEGIN();
  rdi.smartVec().pin("A").readBit(10000).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › enPassFail）

```
enPassFail(bool val = true)
```

### Example（取自子主题 SmartRDI  Vector and protocol programming › enPassFail）

```
RDI_BEGIN();
  rdi.smartVec("a").label("label1").pin("A")....enPassFail(true).execute();
  rdi.smartVec("b").label("label2").pin("B")....enPassFail().execute();
RDI_END();

rdi.id("a").getPassFail();
rdi.id("b").getPassFail();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › expectBit）

```
expectBit(ARRAY_I bitStream,int startBit=0);
expectBit(string rtv, int startBit=0); // For runtime setup
```

Relationship of bit to DVC:

- X1 mode: bit 0 to DVC "L", 1 to "H", and 2 to "X".
- Xn mode: 0101 to "LHLH" and 0112 to "LHHX".
  SmartRDI always deals with 0, 1, and 2 for DVC "L", "H", and "X".

List of parameters
| Parameter | Description |
|---|---|
| bitStream | The expected bit stream you need to get from the captured pin. |
| startBit | The starting position of the bits to be compared. If the startBit parameter is not specified, the default value is 0. |
| rtv | The value to be used at runtime. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › expectBit）

```
ARRAY_I bitStream(4);
bitStream[0]=1;
bitStream[1]=0;
bitStream[2]=1;
bitStream[3]=1;

ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();
  rdi.smartVec(1).pin("DATA7").expectBit(bitStream,2).execute();
RDI_END();

ON_FIRST_INVOCATION_END();

int pf_result=rdi.id(1).getPassFail();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › expectData）

```
expectData(long long data, int bitLength, int startBit=0);
expectData(string rtv, int bitLength, int startBit=0);
```

List of parameters
| Parameter | Description |
|---|---|
| data | The expected data you want to get from the captured pin. |
| bitLength | The length of the bits (data will be automatically converted into bits) to be written. |
| startBit | The starting position of the bits to be compared. If the startBit parameter missing, the default value is 0. |
| rtv | The value to be used at runtime. |

### Example 1（取自子主题 SmartRDI  Vector and protocol programming › expectData）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA3").expectData(0x54,8,2).execute();
RDI_END();
```

### Example 2（取自子主题 SmartRDI  Vector and protocol programming › expectData）

This example demonstrates how to use `expectData()` at runtime.

```
ARRAY_I outputSite = ...
rdi.runTimeVal("rtValue", outputSite);
RDI_BEGIN();
  ...
  rdi.smartVec("a").pin("pinA").expectData("rtValue",8).execute();
  ...
RDI_END();

int result = rdi.id("a").getPassFail();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › failCount）

```
failCount(int startCyc,int cycRange);
failCount(int startCyc);
failCount();
```

List of parameters
| Parameter | Description |
|---|---|
| startCyc | Start cycle. |
| cycRange | Cycle range. |

Return value

There is no return value.

  Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports xMode directly.
- The xMode parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when xMode is set to be greater than 1.
- For one pin, xMode must remain the same in different labels in burst; otherwise the results might be wrong.

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › failCyc）

```
failCyc(int startCyc,int cycRange);
failCyc(int startCyc);
failCyc();
```

List of parameters
| Parameter | Description |
|---|---|
| startCyc | Start cycle. |
| cycRange | Cycle range. |

Return value

There is no return value.

  Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports xMode directly.
- The xMode parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when xMode is set to be greater than 1.
- For one pin, xMode must remain the same in different labels in burst; otherwise the results might be wrong.

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › failNode）

```
failNode();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 SmartRDI  Vector and protocol programming › failNode）

```
RDI_BEGIN();
...
  rdi.smartVec...
	.insertJmpe(2).failNode().pin("DATA1").writeData(0xf,8,0)...execute();
...
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › FFC）

```
FFC(int startCyc);
FFC();
```

List of parameters
| Parameter | Description |
|---|---|
| startCyc | The number of the first cycle in a cycle range in which fails are counted.<br><br>An integer. Cycle counting starts from zero.<br><br>This is an optional parameter. If it is omitted, the cycle range starts with the first cycle. |

Return value

There is no return value.

  Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports xMode directly.
- The xMode parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when xMode is set to be greater than 1.
- For one pin, xMode must remain the same in different labels in burst; otherwise the results might be wrong.

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › fillBit）

```
fillBit(int bit,int bitLength,int startBit);
fillBit(const string bit,int bitLength,int startBit);
```

List of parameters
| Parameter | Description |
|---|---|
| bit | The bit or string that you want to write to the pattern. |
| bitlength | The length of the bits to be filled. |
| startBit | The starting position of the bit to be written. If you do not specify a starting position, the default value is 0. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › fillBit）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").fillBit(1,4,2).execute(); // index
RDI_END();
```

Supporting a string

```
RDI_BEGIN()
  rdi.smartVec().pin("A").defaultBit(0).fillBit("p",4,1)
                         .xMode(2).bitLength(6)
                         .execute();
RDI_BEGIN();
```

You must define device cycles in the corresponding wavetable.

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › fillVec）

```
fillVec(int index,int vecLength,int startVec);
fillVec(string dvc,int vecLength,int startVec);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

index

 |

The physical index you want to write to the pattern .

 |
 |

dvc

 |

The device cycle you want to write to the pattern.

 |
 |

vecLength

 |

The length of the vector to be filled.

 |
 |

startVec

 |

The starting position of the vector to be written. If the startVec parameter missing, the default value is 0.

   | Note You must define the device cycles' names in the corresponding wavetables.

### Example（取自子主题 SmartRDI  Vector and protocol programming › fillVec）

```
RDI_BEGIN()
rdi.smartVec().pin("DATA1").fillVec(3,1).execute();       // physical index= 3
rdi.smartVec().pin("DATA3").fillVec("0101",4).execute();  // device cycle
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › insertJmpe）

```
insertJmpe(int vecLine, int level);
```

List of parameters
| Parameter | Description |
|---|---|
| vecLine | Number of the vector line where you want to insert the subroutine. |
| level | Subroutine level. This refers to the target level at which you want to insert a new subroutine.<br><br>The default value is 1, which means the first level subroutine and actually refers to the main pattern. To insert a subroutine into another subroutine, you should specify a level larger than 1. |

Return value

There is no return value.

### Example 1（取自子主题 SmartRDI  Vector and protocol programming › insertJmpe）

```
RDI_BEGIN();
  rdi.smartVec(). pin("DATA1").writeData(0x1,8,0)// the content in main pattern
     .insertJmpe(2).passNode().pin("DATA1").writeData(0x0,8,0) // the content of pass branch label of JMPE in main pattern
                   .failNode().pin("DATA1").writeData(0xf,8,0).execute(); // the content of fail branch label by JMPE in main pattern
RDI_END();
```

This code example inserts two subroutines into the pattern at vector 2: one subroutine for pass node and the other for fail node. See the figure below.

 !`insertJmpe`（raw: `../../../../agent-html/152409.png`）

### Example 2（取自子主题 SmartRDI  Vector and protocol programming › insertJmpe）

You can use `insertJmpe()` inside `insertSub()`（raw: `02.07.13.24.21_insertSub.md`）. Below is an example.

```
RDI_BEGIN();
...
  rdi.smartVec().pin()...pin()...
                      .insertSub(3).repeatSub()...
                      .insertJmpe(5,2).passNode()...
                                      .failNode()...
                      .execute();
...
RDI_END();
```

### Example 3（取自子主题 SmartRDI  Vector and protocol programming › insertJmpe）

You can also use `insertSub()`（raw: `02.07.13.24.21_insertSub.md`） inside `insertJmpe()`. Below is an example.

```
RDI_BEGIN();
...
  rdi.smartVec().pin()...pin()...
                       .insertJmpe(3)
                            .passNode()...
                               .insertSub(5,2).repeatSub()...
                            .failNode()...
                      .execute();
...
RDI_END();
```

### Example 4（取自子主题 SmartRDI  Vector and protocol programming › insertJmpe）

You can insert JSUB and JMPE in the same vector line of a label. The JSUB instruction is invoked before the JMPE instruction in this case. Below is an example.

```
RDI_BEGIN();
    rdi.smartVec("id5").pin("DATA1").writeData(0x1,8,0)
        .insertSub(2).pin("DATA1").writeData(0x1,8,0)
        .insertSub(2).pin("DATA1").writeData(0x2,8,0)
        .insertJmpe(2).passNode().pin("DATA1").writeData(0x3,8,0)
                  .failNode().pin("DATA1").writeData(0x4,8,0)
        .execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › insertSub）

```
insertSub(int vecLine);
insertSub(int vecLine, int level);
```

List of parameters
| Parameter | Description |
|---|---|
| vecLine | Number of the vector line where you want to insert the subroutine. |
| level | Subroutine level. This refers to the target level at which you want to insert a new subroutine.<br><br>The default value is 1, which means the first level subroutine and actually refers to the main pattern. To insert a subroutine into another subroutine, you should specify a level larger than 1. |

Return value

There is no return value.

### Example 1（取自子主题 SmartRDI  Vector and protocol programming › insertSub）

```
RDI_BEGIN();
    rdi.smartVec("id2").pin("DATA1").writeData(0x1,8,0);    // the content of the main pattern
        .insertSub(3).pin("DATA1").writeData(0x3,8,0);    // the content of sublabel A which is inserted in the main pattern
        .insertSub(6).pin("DATA1").writeData(0x6,8,0);    // the content of sublabel B, which is inserted in the main pattern
        .insertSub(9,2).pin("DATA1").writeData(0x9,8,2).execute();    // the content of sublabel C which is inserted in sublabel B
RDI_END();
```

In the example above, subroutines A and B are inserted into the main pattern at vector lines 3 and 6. subroutine C is inserted into a level 2 subroutine at vector line 9. Because the insertion is always made in the closest label when multiple subroutines exist at the target insertion level, subrountine C is inserted into subroutine B which is closer than A. The created pattern structure is as follows.

 !`2016-11-09_16-28-25`（raw: `../../../../agent-html/152255.png`）

### Example 2（取自子主题 SmartRDI  Vector and protocol programming › insertSub）

Below is an example of using `label()`（raw: `02.07.13.24.22_label.md`）, for example `label("abc")`, within `insertSub()`:

```
RDI_BEGIN();
...
rdi.smartVec().pin()...pin()... // the content in the main pattern
           .insertSub(10).label("abc")    // label "abc" is inserted in the main pattern with JSUB
              .insertSub(5 ).label("abc").pin()...pin()... // sublabel A (copied and edited from "abc") is inserted in the main pattern with JSUB
...
RDI_END();
```

In this example,

- If there are no `pin()...pin()...` settings after `label()`, the label "abc" will be directly called by JSUB.
- If there are `pin()...pin()...` settings after `label()`, the label "abc" will be copied and edited, then called by JSUB.
- If the label "abc" is not a subroutine, SmartRDI will clone it to a subroutine, then call it by JSUB and give a warning.

### Example 3（取自子主题 SmartRDI  Vector and protocol programming › insertSub）

Below is an example when `insertSub()` is put in to `label()`（raw: `02.07.13.24.22_label.md`）, for example `label("abc")`:

```
RDI_BEGIN();
    rdi.smartVec().label("abc").pin()...pin()...  // the content in the main pattern
          .insertSub(5).pin()...pin()... // the content in sublabel A, which is inserted in the main pattern
RDI_END();
```

In this example,

- If `copyLabel()`（raw: `02.07.13.12.01.01.04_copyLabel.md`） is set to true, the JSUB will be inserted into the copy of label "abc"; if `copyLabel()`（raw: `02.07.13.12.01.01.04_copyLabel.md`） is set to false, the JSUB will be inserted directly into label "abc".
- Following the general rule, omitting the `copyLabel()`（raw: `02.07.13.12.01.01.04_copyLabel.md`） command by default makes a copy of the label "abc" and inserts the modification. The copied label name will hold the content of the actions. It ensures the right content in the right pattern.

### Example 4（取自子主题 SmartRDI  Vector and protocol programming › insertSub）

`insertSub(`) can be used inside a `burstLabel().begin()`/`burstLabel().end()` block, as long as it is not inserted into a user label. Below is an example.

```
RDI_BEGIN();
    rdi.smartVec().burstLabel("smv").begin();
    rdi.smartVec().pin("DATA1").readData(2,0)
        .insertSub(3).repeatSub(5).pin("DATA1").writeData(0x86,8,3).execute();
    rdi.smartVec()
        .insertSub(10).pin("DATA1").writeData(0x86,8,3).execute();
    rdi.smartVec().burstLabel().end();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › label）

```
label(const string& sLabelName);
```

List of parameters
| Parameter | Description |
|---|---|
| sLabelName | The label to be executed / pattern on which measurement is performed. |

Return value

There is no return value.

### Example（取自子主题 SmartRDI  Vector and protocol programming › label）

```
RDI_BEGIN();
...
  rdi.smartVec().label("label4").pin("D3").writeData(0x55,8,0).execute();
...
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › labelName）

```
labelName(const string &name);
labelName(const string &name, TA::MD5_OPTION);
```

List of parameters
| Parameter | Description |
|---|---|
| name | User specified name for the label. |
| TA::MD5_OPTION | The option which defines to use an MD5 postfix string or not. |

List of available options of parameter: <TA::MD5_OPTION>
| Option | Description |
|---|---|
| TA::MD5_ON | With an MD5 postfix string in the label name.<br><br>With MD5_ON, the maximum length of a valid "targetLabelName" in the generated pattern name is 74. |
| TA::MD5_OFF | Without an MD5 postfix string in the label name. This is the default value.<br><br>With MD5_OFF, the maximum length of a valid "targetLabelName" in the generated pattern name is 111. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › labelName）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3").writeData(0x54,8,2).readData(8,20).labelName("label_name").execute();
RDI_END();
```

Note If a label with the same name exists, the pattern will not be re-generated. So make sure that the label name will change if the content changes.

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › multiFFC）

```
multiFFC(int startCycle, int FailNumber);
```

List of parameters
| Parameter | Description |
|---|---|
| startCycle | The number of the first cycle to start the action. |
| FailNumber | The number of failing cycles within a pattern to acquire. |

Use the following functions to collect the result:

- getMultiFFC(string resultPin)
- getMultiFFC():Use this command if only one result pin exists.
   Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports `xMode`（raw: `02.07.13.24.42_xMode.md`） directly.
- The `xMode`（raw: `02.07.13.24.42_xMode.md`） parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when `xMode`（raw: `02.07.13.24.42_xMode.md`） is set to be greater than 1.
- For one pin, `xMode`（raw: `02.07.13.24.42_xMode.md`） must remain the same in different labels in burst; otherwise the results might be wrong.

### Example（取自子主题 SmartRDI  Vector and protocol programming › multiFFC）

```
RDI_BEGIN();
   rdi.emap("mffc").label("abc")
                   .pin("inA")
                   .multiFFC(0,100)
                   .execute();
   /* For smartVec():
   rdi.smartVec("mffc").label("abc")
                       .pin("inA")
                      .multiFFC(0,100)
                     .execute();
   */

RDI_END();

rdi.id("mffc").getMultiFFC();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › passNode）

```
passNode();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 SmartRDI  Vector and protocol programming › passNode）

```
RDI_BEGIN();
...
    rdi.smartVec...
    .insertJmpe(2).passNode().pin("DATA1").writeData(0x0,8,0)...execute();
...
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › pMode）

```
pMode(int Pmode);
```

List of parameters
| Parameter | Description |
|---|---|
| Pmode | The number of tester cycles per device cycle. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › pMode）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").fillBit(1,4,2).pMode(2).execute();
  rdi.smartVec().pin("DATA3").readBit(4,2).pMode(2).execute();
  rdi.smartVec().pin("DATA5").writeData(0x54,8,4).pMode(4).execute();
  rdi.smartVec().pin("DATA7").readData(8,4).pMode(4).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › pModeStrobe）

```
pModeStrobe(int strobePos);
```

List of parameters
| Parameter | Description |
|---|---|
| strobePos | The strobe position within pMode cycles. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › pModeStrobe）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA7").readData(8,4).pMode(4).pModeStrobe(3).execute();
RDI_END();
```

The following code illustrates the operation of pModeStrobe.

```
rdi.smartVec().pin("A").expectBit(arr).pMode(4).pModeStrobe(2).execute();
```

expect bit : 001-> LLH

vec: XLXXXHXXXHXX

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › readBit）

```
readBit(int bitLength,int startBit);
```

List of parameters
| Parameter | Description |
|---|---|
| bitLength | The length of the bits to be read |
| startBit | The starting position of the bits to be read. If the "startBit" parameter missing, the default value is 0. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › readBit）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").readBit(4,2).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › readData）

```
readData(int bitLength,int startBit);
```

List of parameters
| Parameter | Description |
|---|---|
| bitLength | The length of the bits (data will be automatically converted into bits) to be read. |
| startBit | The starting position of the bits to be read. If the startBit parameter missing, the default value is 0. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › readData）

```
RDI_BEGIN();
  rdi.smartVec("result").pin("DATA1").readData(4,2).execute();
RDI_END();
...
ARRAY_LL data_result = rdi.id("result").getReadData("DATA1");
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › rdi.smartVec  .readMode）

```
readMode(TA::MEAS_TYPE mode);
```

List of parameters
| Parameter | Description |
|---|---|
| mode | The read mode. |

List of available options of parameter: <mode>
 |

Option

 |

Description

 |
 |

TA::EMAP

 |

The error map as the read mode.

In this mode, for each pin, the ERROR_MAP_TEST API is used to get all failed positions. A post processing is done afterward.

 |
 |

TA::DIGCAP

 |

The digital capture as the read mode.

In this mode, a dummy pattern with a digital capture variable is created. It cannot be mixed with the digCap() class inside a burstUpload-begin()/end() block.

   | Note The option TA::EMAP cannot be used together with a match loop in label.

### Example（取自子主题 SmartRDI  Vector and protocol programming › rdi.smartVec  .readMode）

```
rdi.smartVec().readMode(TA::EMAP);

RDI_BEGIN();
  ...
  rdi.smartVec().pin("A").read...().execute();
  ...
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › repeat）

```
repeat(int rptNum);
repeat(int rptNum, int vecSize, int startVec); // relevant only for the Vector class
```

List of parameters
| Parameter | Description |
|---|---|
| rptNum | The loop / repeat number. |
| vecSize | Only Vector class: Vector size. Used together with startVec to define the sector for repetition. |
| startVec | Only Vector class: Start vector. Used together with vecSize to define the sector for repetition. |

### Example 1（取自子主题 SmartRDI  Vector and protocol programming › repeat）

```
// Have some content repeats in pattern, for example, clock signal
RDI_BEGIN();
rdi.port("clk").smartVec().pin("CLK").writePat("0,1,1").repeat(1000).execute();
RDI_END();
// readBit()/readData() with a huge number
RDI_BEGIN();
rdi.smartVec().pin("dout").readBit(10000).execute(); // original
RDI_END();
RDI_BEGIN();
rdi.smartVec().pin("dout").readBit(1).repeat(10000).execute();
RDI_END();
```

### Example 2（取自子主题 SmartRDI  Vector and protocol programming › repeat）

```
RDI_BEGIN();
  rdi.smartVec()...repeat(5,10,2).repeat(4,5,20).execute();
  // add RPTV to 2 different segments of the pattern
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › repeatSub）

```
repeatSub(int repeatNum);
```

List of parameters
| Parameter | Description |
|---|---|
| repeatNum | number of repeated subroutine calls. |

Return value

There is no return value.

### Example（取自子主题 SmartRDI  Vector and protocol programming › repeatSub）

```
RDI_BEGIN();
    rdi.smartVec(). pin("DATA1").writeData(0x1,8,0)    // the content in the main pattern
       .insertSub(5).repeatSub(5).pin("DATA1").writeData(0x3,8,0).execute(); //  the content in sublabel 1, RPTJ 5, which is inserted in the main pattern
RDI_END();
```

With the above code, you add the target subroutine at the vector 5 for five times, as the figure below shows.

 !`repeatSub`（raw: `../../../../agent-html/152408.png`）

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › rdi.smartVec  .vecEditMode）

```
rdi.smartVec().vecEditMode(TA::Mode);
```

List of parameters
| Parameter | Description |
|---|---|
| TA::Mode | The mode to be used for one piece of pattern. |

List of available options of parameter: <TA::Mode>
| Option | Description |
|---|---|
| TA::VECD | The VECD firmware command mode, which calls the VECD FW command for vector editing. |
| TA::VTT | The VEC_TRANSFER_TASK API mode. |

### Example 1（取自子主题 SmartRDI  Vector and protocol programming › rdi.smartVec  .vecEditMode）

To change the edit mode across `RDI_BEGIN()`/`RDI_END()` blocks:

```
rdi.smartVec().vecEditMode(TA::VECD);
RDI_BEGIN();
   ...
   rdi.smartVec() ... execute(); // Runtime editing
   ...
RDI_END();

rdi.smartVec().vecEditMode(TA::VTT);
RDI_BEGIN();
   ...
   rdi.smartVec() ... execute(); // Runtime editing
   ...
RDI_END();
```

### Example 2（取自子主题 SmartRDI  Vector and protocol programming › rdi.smartVec  .vecEditMode）

To change edit mode inside the `RDI_BEGIN()`/`RDI_END()` block:

```
RDI_BEGIN();
    rdi.smartVec().vecEditMode(TA::VECD);
    rdi.smartVec()...;// run-time edit
    rdi.smartVec().vecEditMode(TA::VTT);
    rdi.smartVec()...;// run-time edit
RDI_END();
```

### Example 3（取自子主题 SmartRDI  Vector and protocol programming › rdi.smartVec  .vecEditMode）

Use only the VTT mode for editing vectors when `copyLabel()`（raw: `02.07.13.24.06_copyLabel.md`） is used for the label.

```
rdi.smartVec().vecEditMode(TA::VTT);

RDI_BEGIN();
  rdi.smartVec().label("sLabel").copyLabel(false).pin(A)
                                .writeData("rt",8,0).execute();
  rdi.smartVec().label("sLabel").copyLabel(false).pin(A)
                                .writeData("rt",8,8).execute(); // a different position
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › vecLength）

```
vecLength(int length);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

length

 |

The length of the pattern.

   | Note If the pattern contents exceed the length defined by the vecLength() parameter, the length of the generated pattern refers to the value of the vecLength() parameter. The overhang will be cut off.

### Example（取自子主题 SmartRDI  Vector and protocol programming › vecLength）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").defaultVec(0).vecLength(10).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › writeBit）

```
writeBit(ARRAY_I bitStream,int startBit);
writeBit(const string &sData, int startBit);  // application for runtime
writeBit(vector<ARRAY_I> perSiteBitStream, int startBit);
```

For pattern generation with bit streams per site, the sizes of all elements in ARRAY_I must be the same. The value for a site can be different from the value for another site. The values for all sites cannot be changed at runtime.

For more information about bits versus DVCs, see `Relationship between bits and device cycles`（raw: `02.07.13.24.01_Relationship_between_bits_and_device_cycles.md`）.

List of parameters
| Parameter | Description |
|---|---|
| bitStream | The bit stream to be written to the pattern. |
| sData | The sData of the parameter that can be changed at runtime. |
| startBit | The bit position in pattern, starting from which the specified bit stream or sData to be written on.<br><br>If the startBit parameter is not specified, the default value is 0. |
| perSiteBitStream | The bit stream per site. |

### Examples（取自子主题 SmartRDI  Vector and protocol programming › writeBit）

```
...
ARRAY_I bitStream(4);
bitStream[0]=1;
bitStream[1]=0;
bitStream[2]=1;
bitStream[3]=1;

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeBit(bitStream,4).execute();
  rdi.smartVec().pin("DATA1").writeBit(bitStream).execute(); // The value of the "startBit" is 0.
RDI_END();
```

  Application for runtime

```
...
// This data type for writeBit() runtime
vector<ARRAY_I> runtime_vec_ARRAY_I;
//Initialize the array with required data
rdi.runTimeVal("string_runtime_vec_ARRAY_I", runtime_vec_ARRAY_I);

// This data type for writeBit() runtime
ARRAY_I runtime_ARRAY_I;
//Initialize the array with required data
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeBit("string_runtime_vec_ARRAY_I",2).execute();
  rdi.smartVec().pin("DATA3").writeBit("string_runtime_ARRAY_I",4).execute();
RDI_END();
```

   Pattern generation with per-site data

```
...
vector<ARRAY_I> perSiteBitStream_1,perSiteBitStream_2;
ARRAY_I dataBit(8);
dataBit[0] = 1;
...
RDI_BEGIN();
  rdi.smartVec().pin("DATA3").writeBit(perSiteBitStream_1,0).writeData(0x55,8,20).execute();
  ...
RDI_END();
ARRAY_I bitStream(20),bitStream_2(20);
...
perSiteBitStream_1.push_back(bitStream);
perSiteBitStream_2.push_back(bitStream_2);
...
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeBit(perSiteStream_1,0).defaultBit(0)
                .pin("DATA2").readData(4,0).execute();
    ...
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › writeData）

```
writeData(long long data,int bitLength,int startBit);
writeData(const string &sData, int bitLength, int startBit); // application for runtime
writeData(ARRAY_LL perSiteData, int bitLength, int startBit); // values for all sites must be different each other and cannot be changed at runtime
```

List of parameters
| Parameter | Description |
|---|---|
| data | The data block you want to write to the pattern. |
| bitLength | The length of the bits (data will be automatically converted into bits) to be written. |
| sData | The sData of the parameter that can be changed at runtime. |
| startBit | The starting position of the bits to be written. If the startBit parameter is not specified, the default value is 0. |
| perSiteData | The array of data. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › writeData）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeData(0x54,8,4).execute();
rdi.smartVec().pin("DATA3").writeData(0x54,8).execute();  // the value of the "startBit" is 0.
RDI_END();

// application for runtime
static int runtime=0;
ARRAY_I runtime_ARRAY_I;     // this data type for writeData() runtime is supported
ARRAY_LL runtime_ARRAY_LL;   // this data type for writeData() runtime is supported
int runtime_int;// this data type for writeData() run-time is supported
long long runtime_longlong;  // this data type for writeData() runtime is supported
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);
rdi.runTimeVal("string_runtime_ARRAY_LL", runtime_ARRAY_LL);
rdi.runTimeVal("string_runtime_int", runtime_int);
rdi.runTimeVal("string_runtime_longlong", runtime_longlong);

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeData("string_runtime_ARRAY_I",8,2).execute();
  rdi.smartVec().pin("DATA3").writeData("string_runtime_ARRAY_LL",8,4).execute();
  rdi.smartVec().pin("DATA5").writeData("string_runtime_int",4,2).execute();
  rdi.smartVec().pin("DATA7").writeData("string_runtime_longlong",64,4).execute();
RDI_END();

// Pattern generation with different data per site.
ARRAY_LL Data(4);  // four sites are used
Data[0]=1;
Data[1]=2;
Data[2]=3;
Data[3]=4;

RDI_BEGIN();
  rdi.smartVec().pin("DATA2").writeData(Data,4).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › writeDataBurst）

```
writeDataBurst(ARRAY_I data, ARRAY_I bitLength, ARRAY_I startBit);
writeDataBurst(ARRAY_I data, int bitLength, int bitDistance, int startBit);
writeDataBurst(ARRAY_I data, int bitLength); // startBit =0,bitDistance=bitLength
writeDataBurst(ARRAY_LL data, ARRAY_I bitLength, ARRAY_I startBit);
writeDataBurst(ARRAY_LL data, int bitLength, int bitDistance, int startBit);
writeDataBurst(ARRAY_LL data, int bitLength); // startBit =0,bitDistance=bitLength
```

List of parameters
| Parameter | Description |
|---|---|
| data | The array of data you want to write to the pattern. |
| bitLength | The length of the bits (data will be automatically converted into bits) to be written. |
| bitDistance | The bit distance between one data and the next data. |
| startBit | The starting position of the bits to be written. If the startBit parameter missing, the default value is 0. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › writeDataBurst）

```
ARRAY_I array_data_1(4); // data array
array_data_1[0]=0x1;
array_data_1[1]=0x23;
array_data_1[2]=0x456;
array_data_1[3]=0x7890;
ARRAY_I bitLength(4);   // bitLength array
bitLengt[0]=4;
bitLengt[1]=8;
bitLengt[2]=12;
bitLengt[3]=16;
ARRAY_I startBit(4);   // startBit array
startBit[0]=0;
startBit[1]=4;
startBit[2]=12;
startBit[3]=24;
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeDataBurst(array_data_1,bitLength,startBit).execute();
RDI_END();
ARRAY_I array_data_2(4);
array_data_2[0]=0x12;
array_data_2[1]=0x34;
array_data_2[2]=0x56;
array_data_2[3]=0x78;
RDI_BEGIN();
rdi.smartVec().pin("DATA3").writeDataBurst(array_data_2,8,4).execute(); // the default value of "startBit" is 0
rdi.smartVec().pin("DATA5").writeDataBurst(array_data_2,8).execute();   // startBit=0,bitDistance=bitLength
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › writeParData）

```
writeParData(long long Data, int startBit);
writeParData(const string &sData, int startBit); // application for runtime
writeParData(ARRAY_LL perSiteData, int startBit);
```

For pattern generation with different data per site, values for all sites must be different each other and cannot be changed at runtime.

List of parameters
| Parameter | Description |
|---|---|
| data | The array of data you want to write to the pattern. |
| sData | The sData of the parameter that can be changed at run-time. |
| startBit | The starting position of the bits to be written. If the startBit parameter is not specified, the default value is 0. |
| perSiteData | The array of data. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › writeParData）

```
// 11(Dec) = 1011(Bin), "1011" will be assigned into the four pins successively,
// DATA1=1,DATA3=0,DATA5=1,DATA7=1
// 6(Dec) = 110(Bin), "110" will be assigned into the three pins successively,
// DATA9=1,DATA11=1,DATA13=0
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParData(11,4).execute();
rdi.smartVec().pin("DATA9,DATA11,DATA13").writeParData(6,4).execute();
RDI_END();

//application for runtime
static int runtime=0;
ARRAY_I runtime_ARRAY_I(4);//parallel data array, this data type for writeParData() run-time is supported
ARRAY_LL runtime_ARRAY_LL(4);//parallel data array, this data type for writeParData() run-time is supported
int runtime_int;//this data type for writeParData() run-time is supported
long long runtime_longlong;//this data type for writeParData() run-time is supported
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);
rdi.runTimeVal("string_runtime_ARRAY_LL", runtime_ARRAY_LL);
rdi.runTimeVal("string_runtime_int", runtime_int);
rdi.runTimeVal("string_runtime_longlong", runtime_longlong);
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParData("string_runtime_ARRAY_I",2).execute();
rdi.smartVec().pin("DATA9,DATA11,DATA13,DATA15").writeParData("string_runtime_ARRAY_LL",4).execute();
rdi.smartVec().pin("DATA17,DATA19,DATA21,DATA23").writeParData("string_runtime_int",6).execute();
rdi.smartVec().pin("DATA25,DATA27,DATA29,DATA31").writeParData("string_runtime_longlong",8).execute();
RDI_END();

// Pattern generation with different data per site.
ARRAY_LL perSiteData(4);  // four sites are used
...
RDI_BEGIN();
  rdi.smartVec().pin("GP").writeParData(perSiteData).execute();
RDI_END();

```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › writeParDataBurst）

```
writeParDataBurst(ARRAY_I data, int bitDistance, int startBit);
writeParDataBurst(ARRAY_I data); // bitDistance=1, startBit=0
writeParDataBurst(ARRAY_LL data, int bitDistance, int startBit);
writeParDataBurst(ARRAY_LL data);// bitDistance=1, startBit=0
```

List of parameters
| Parameter | Description |
|---|---|
| data | The array of data you want to write to the pattern. |
| bitDistance | The bit distance between one data and the next data. |
| startBit | The starting position of the bits to be written. If the startBit parameter missing, the default value is 0. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › writeParDataBurst）

```
ARRAY_I I_ParDataBurst(4); // parallel data array
I_ParDataBurst[0]=0x01;
I_ParDataBurst[1]=0x05;
I_ParDataBurst[2]=0x09;
I_ParDataBurst[3]=0x0B;
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(I_ParDataBurst,2,4).execute();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(I_ParDataBurst).execute();
RDI_END();
ARRAY_LL LL_ParDataBurst(4); // parallel data array
LL_ParDataBurst[0]=0x01;
LL_ParDataBurst[1]=0x05;
LL_ParDataBurst[2]=0x09;
LL_ParDataBurst[3]=0x0B;
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(LL_ParDataBurst,2,4).execute();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(LL_ParDataBurst).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › writePat）

```
writePat(const string &dvc,int startVec);
```

List of parameters
| Parameter | Description |
|---|---|
| dvc | The device cycle you want to write into the pattern. |
| startVec | The starting position of the vector to be written. If the startVec parameter missing, the default value is 0. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › writePat）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writePat("0,1,Z,Z,H",1).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › writeVec）

```
writeVec(vector<string> dvcList, int startVec);
writeVec(ARRAY_I indexList, int startVec);
writeVec(const string &sData, int startVec); // application for runtime
writeVec(vector<ARRAY_I> perSiteIndex, int startVec);
writeVec(vector<vector<string>> perSiteDvc, int startVec);
```

For pattern generation with per-site data, the sizes of all elements in ARRAY_I or vector<string> must be the same. The value for a site can be different from the value for another site. The values for all sites cannot be changed at runtime.

List of parameters
| Parameter | Description |
|---|---|
| dvcList | The device cycle list you want to write to the pattern. |
| indexList | The physical index list you want to write to the pattern. |
| sData | The sData of the parameter that can be changed at runtime. |
| startVec | The starting position of the vector to be written. If the startVec parameter is not specified, the default value is 0. |
| perSiteIndex | The index list per site. |
| perSiteDvc | The device cycle list per site. |

### Examples（取自子主题 SmartRDI  Vector and protocol programming › writeVec）

```
vector<string> dvcList;
dvcList.push_back("1"); // device cycle
dvcList.push_back("0");

ARRAY_I indexList(3);
indexList[0]=0;         // physical index
indexList[1]=1;
indexList[2]=2;
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeVec(dvcList,1).execute();   // dvcList
  rdi.smartVec().pin("DATA3").writeVec(indexList,4).execute(); // indexList
RDI_END();
```

  Application for runtime

```
vector<ARRAY_I> runtime_vec_ARRAY_I;  // this data type for writeData() runtime is supported
rdi.runTimeVal("string_runtime_vec_ARRAY_I", runtime_vec_ARRAY_I);

// This data type for writeData() run-time is supported
ARRAY_I runtime_ARRAY_I;
//Initialize the array with required data
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeVec("string_runtime_vec_ARRAY_I",2).execute();
  rdi.smartVec().pin("DATA3").writeVec("string_runtime_ARRAY_I",4).execute();
RDI_END();
```

   Pattern generation with per-site data

```
// The sizes of ARRAY_I index1, index2, index3, and index4 must be the same:
ARRAY_I index1(8), index2(8), index3(8), index4(8);
vector<ARRAY_I> perSiteIndex;
perSiteIndex.push_back(index1);
...
RDI_BEGIN();
  rdi.smartVec().pin("A").writeVec(perSiteIndex,2).execute();
RDI_END();
```

```
...
vector<string> vec_s;
vec_s.push_back("0");
vec_s.push_back("1");
vec_s.push_back("0");
vec_s.push_back("1");

vector<string> vec_s1;
vec_s1.push_back("1");
vec_s1.push_back("0");
vec_s1.push_back("1");
vec_s1.push_back("0");

vector<vector<string> > vec_vec_s;
vec_vec_s.push_back(vec_s);
vec_vec_s.push_back(vec_s1);
vec_vec_s.push_back(vec_s);
vec_vec_s.push_back(vec_s1);

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeVec(vec_vec_s).execute();
RDI_END();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › xMode）

```
xMode(int Xmode);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

Xmode

 |

The number of device cycles in each tester cycle.

   |   Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports xMode directly.
- The xMode parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when xMode is set to be greater than 1.
- For one pin, the xMode must remain the same in different labels in burst; otherwise the results might be wrong.
 Note For correctly retrieving the results of error map data:

- For a specified pin, in one RDI_BEGIN/RDI_END block, its xMode number must remain the same value, no matter it is for a SmartRDI command or in the user pattern.
- In the wavetable, the length of the device cycle name must align with the xMode() value. For example, if you set xMode to xMode(2), the dvc must correspondingly have two letters, such as "LL", "00", "11", "LL". Even the dvc of the physical index f, which normal value is "." with SmartRDI, must be ".." for xMode(2). Otherwise SmarTest cannot recognize the correct xMode value from pattern.

### Example（取自子主题 SmartRDI  Vector and protocol programming › xMode）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").fillBit(1,4,2).xMode(2).execute();
  rdi.smartVec().pin("DATA3").readBit(4,2).xMode(2).execute();
  rdi.smartVec().pin("DATA5").writeData(0x54,8,4).xMode(4).execute();
  rdi.smartVec().pin("DATA7").readData(8,4).xMode(4).execute();
RDI_END();
```

Data from `readBit()`（raw: `02.07.13.24.28_readBit.md`）, `readData()`（raw: `02.07.13.24.29_readData.md`）, `expectBit()`（raw: `02.07.13.24.12_expectBit.md`）, or `expectData()`（raw: `02.07.13.24.13_expectData.md`） can cross over device cycles.

```
RDI_BEGIN();
  rdi.smartVec().pin("A").expectData(0,4,1).defaultBit(0)
                         .xMode(2).bitLength(8)
                         .execute();
RDI_END();
```

The result vector:

 !`xMode crossover borders`（raw: `../../../../agent-html/151539.png`）

Supporting a string from `fillBit()`（raw: `02.07.13.24.18_fillBit.md`） and `defaultBit()`（raw: `02.07.13.24.07_defaultBit.md`）.

```
RDI_BEGIN();
  rdi.smartVec().pin("A").defaultBit(0).fillBit("p",4,1)
                         .xMode(2).bitLength(6)
                         .execute();
RDI_END();
```

The result vector:

 !`string_support by fillbit and defaultBit`（raw: `../../../../agent-html/151540.png`） Note You must define device cycle names in the corresponding wavetable.

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › getFailCount）

```
int getFailCount(string pin);
```

List of parameters
| Parameter | Description |
|---|---|
| pin | Specifies a pin for which to get the fail count. |

### Return value（取自子主题 SmartRDI  Vector and protocol programming › getFailCount）

The return value is an integer indicating the number of errors.

### Example（取自子主题 SmartRDI  Vector and protocol programming › getFailCount）

```
ON_FIRST_INVOCATION_BEGIN();

  RDI_BEGIN();
    rdi.smartVec("a").pin("pA").writePat("0,1,1,H,H,H,L").failCount().execute();
  RDI_END();

ON_FIRST_INVOCATION_END();

int fcount=rdi.id("a").getFailCount("pA");
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › getFailCyc）

```
ARRAY_LL getFailCyc(string pin);
```

List of parameters
| Parameter | Description |
|---|---|
| pin | Specifies a pin for which to get all failing cycles' positions. |

### Return value（取自子主题 SmartRDI  Vector and protocol programming › getFailCyc）

The return value is an ARRAY_LL indicating all failing cycles' positions.

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › getFFC）

```
int getFFC(string pin);
```

List of parameters
| Parameter | Description |
|---|---|
| pin | Specifies a pin for which to get the first failing cycle. |

### Return value（取自子主题 SmartRDI  Vector and protocol programming › getFFC）

The return value is an integer indicating the first failing cycle.

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › rdi.id  .getMultiFFC）

```
ARRAY_LL getMultiFFC(string pin);
ARRAY_LL getMultiFFC(); // if only one result pin exists.
```

List of parameters
| Parameter | Description |
|---|---|
| pin | The pin for which to retrieve the number of failing cycles. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › rdi.id  .getMultiFFC）

```
RDI_BEGIN();
   rdi.emap("mffc").label("abc")
                   .pin("inA")
                   .multiFFC(0,100)
                   .execute();
RDI_END();

rdi.id("mffc").getMultiFFC();
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › getReadBit）

```
ARRAY_I getReadBit(const string &pin);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

pin

 |

The pin to query.

   | Note If the pin parameter is missing, the default pin will be used.

### Example（取自子主题 SmartRDI  Vector and protocol programming › getReadBit）

```
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
rdi.smartVec("result").pin("DATA1").readBit(4,2).execute();
RDI_END();
ON_FIRST_INVOCATION_END();
ARRAY_I bit_result = rdi.id("result").getReadBit("DATA1");
```

### Syntax（取自子主题 SmartRDI  Vector and protocol programming › getReadData）

```
ARRAY_LL  getReadData(const string &pin);
```

List of parameters
| Parameter | Description |
|---|---|
| pin | The pin to query. |

### Example（取自子主题 SmartRDI  Vector and protocol programming › getReadData）

```
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
   rdi.smartVec("result").pin("DATA1").readData(4,2).execute();
RDI_END();
ON_FIRST_INVOCATION_END();
ARRAY_LL data_result = rdi.id("result").getReadData("DATA1");
```

### Example（取自子主题 SmartRDI  Vector and protocol programming › Match loop support › Retrieving match loop results）

```
RDI_BEGIN();
 rdi.smartVec("abc").pin("pinA").defaultBit(0)
             .matchData(0x36,8,10).matchCycle(10)
             .readMatchCount("pinA")
             .readMatchPassFail("pinA").execute();
RDI_END();
 int pf = rdi.id("abc").getMatchPassFail();
 int cnt= rdi.id("abc").getMatchCount();
```

<!-- 语法节 end -->

## 是什么

**SmartRDI（Rapid Development Interface）是 93K 的「高层测试方法 API」——把原来要自己写 sequencer 指令、
自己拼 burst pattern、自己生成 analog set 的测试，收成一条链式调用。**

> 「SmartRDI (Rapid Development Interface) provides a high level of programming interface to create your test method program. Use the classes listed below to setup your tests.」

本篇自己给的定位是这五条（**逐字，bullet 标记照抄**）：

> 「It is a new V93000 API set to provide:
>
> - simple and common programming interface
> - automated sequencer based pattern burst generation for DC test, Analog/RF trigger, digital capture, error map, protocol, utility line control.
> - automated burst Analog/RF set generation
> - result retrieving with transparent hidden upload
> - simple way to debug」

**第二条是全篇的定位句**：`automated sequencer based pattern burst generation` ——
**你写的是「要做什么测试」，burst pattern 由 SmartRDI 生成，不是手画**（机制见下面「两种执行模式」）。
**第四条是另一个卖点**：结果靠 `transparent hidden upload` 取回，**取结果的时机不用你自己安排**。

### 14 个 class 就是全部入口

> 「SmartRDI provides classes to set up different types of tests, including dc, digital capture, functional test, protocol, mixed signal, RF, utility control, timing and level. For each class, functions are provided to set up the test and retrieve the test result.」

本篇把每个 class 指到哪一篇，逐条列了（**左列是 class 名，右列是本篇给它的链接文本**）：

| class | 本篇指到的那一篇 |
|---|---|
| `cogo()` | SmartRDI: Pattern-based conditional jump - cogo |
| `dc()` | SmartRDI: DC test setup ＋ Using a DC resources as an AWG/DGT with SmartRDI |
| `digCap()` | SmartRDI: Digital capture test setup |
| `emap()` | Getting error map information from user pattern |
| `func()` | Functional test setup |
| `hiddenUpload()` | Using hidden upload with SmartRDI |
| `hwRelay()` | SmartRDI: Digital channel relay control |
| `level()` / `timing()` | SmartRDI: Level and timing set changes |
| `protocol()` | Setting up protocol tests with SmartRDI |
| `route()` | rdi.route() |
| `smartVec()` | Generating vector with SmartRDI |
| `tmu()` | SmartRDI: TMU test setup |
| `util()` | Controlling the utility lines with SmartRDI |
| `alarm()` | SmartRDI: Alarm handling for DCVI |

**这 14 个 class 的行为，本页这一篇一个都没写**——**它只给名字和去处**（见 `## 出处`）。
**能读出来的一件事**：`level()` 和 `timing()` 是**同一个 class**（本篇写作 `level()/timing()`）；
`smartVec()` 管「生成 vector」，`emap()` 管「error map」——**这三条的边界正好落在本 wiki 的
level / timing / pattern / error-map 几个 stage 上**（**这是本页的读法，不是本篇的措辞**）。

### 两种执行模式（**本页最该记住的一张表**）

> 「SmartRDI enables the API鈥慴ased sequencer鈥慶ontrolled test with user鈥慺riendly interface. Its target is to speed up the time to market with competitive throughput. SmartRDI provides two execution modes, the pattern鈥慴ased mode and the code鈥慴ased mode.」

（**上面这句里的 `鈥慴` / `鈥慶` / `鈥慺` 是坏字，读法见 `## 出处` ⚠️①。**）

| | **code-based mode** | **pattern-based mode** |
|---|---|---|
| **定位** | —— | `This is the target mode for the program with SmartRDI.` |
| **谁在执行** | `The execution is controlled by the workstation.` | 生成出来的 burst pattern |
| **生成什么** | `There is no generation of burst patterns and analog sets.` | 「will generate a burst pattern with the DC events and analog hardware trigger and generate an analog set for all the specified analog tests」 |
| **代码放哪** | `Put the code to be executed in the code-based mode outside of the RDI_BEGIN()/RDI_END() block.` | 放在 `RDI_BEGIN()` / `RDI_END()` block **里面** |
| **setup 从哪来** | `The setups are based on normal test method APIs.` | 由 SmartRDI 生成 |

**两者不是「新旧」关系，是分工**——**因为 pattern-based 覆盖不全**：

> 「The pattern鈥慴ased mode described below cannot cover all features of the hardware. Some functions are therefore available only in code鈥慴ased mode.」

> **⚠️ 原文没有列出「哪些功能只在 code-based 里有」**——
> **这是本页最想知道的细节而语料没给的一句**（§10 不替它补）。

### burst pattern 的命名与生成时机

> 「The generated burst pattern is named as "_rdi_burst_" + test_suite_name + RDI_block_number_in_testsuite. The burst pattern will be executed when RDI_END() is executed.」

**命名是可推导的**：`_rdi_burst_` ＋ **test suite 名** ＋ **在这个 test suite 里第几个 RDI block**。
**一个 test method 里可以有多个 RDI block**，编号就是它们。

> 「You can have multiple RDI_BEGIN()/RDI_END() blocks in one test method. The burst pattern and the analog set will only be generated for the first run of the test method after it is built. Build the test method again when the device setups are reloaded or modified.」

**最后一句是本篇第一个操作陷阱**：**生成只发生在 build 之后的第一跑**，
**改了 device setup 必须重新 build**，否则跑的还是旧 setup——**原文的动词是 `Build the test method again`**。

### 三种跑法：burst / single / production

| 模式 | 原文 |
|---|---|
| **burst** | `The burst mode is used by default.` |
| **single（调试用）** | 「the single mode is provided for the pattern鈥慴ased execution. In this mode, the pattern will be executed when the corresponding code is executed.」 |
| **production** | 「To avoid the generation of setups in the production site, the production mode is provided. In this mode, no new setup files will be generated. SmartRDI will use the setups generated from the burst mode in the execution.」 |

**production 模式带一条前置条件**：

> 「Keep the test method code and the device setup aligned before executing in the production mode.」

**它和上面那条「改了 setup 要重新 build」是一对**：pattern-based 靠 build 生成 setup，
production 靠现成 setup 跑——**两边的代码和 setup 必须是同一版**。

> **本篇只给了这三个名字，没给 API 记号。**
> 本页 `## 语法 / 参数` 的 `RDI BEGIN` / `RDI END` 段（脚本从子主题抽的）里有 `mode` 的取值表，
> **但那一段是子主题的内容、本页没读那个子主题**，所以**不在这里把它当文档事实引用**；
> **要记取值请直接看本页语法节。**

### multiport 与那个 900 秒

> 「For multiport tests, a multiport burst pattern will be generated. Tests on the same port will be executed serially and tests on different ports will be executed in parallel. The function portSync() can be used to synchronize the time among all the ports.」

**同 port 串行、不同 port 并行**——**这是默认行为，不是你配出来的**；`portSync()` 是**对齐时间**用的。

> 「Note that the default sequencer timeout is 900 s. For long sequences use SQTO, SQTO? - (SeQuencer TimeOut) to increase the SmarTest Work Center.」

**默认 900 秒是 sequencer 的超时，不是你这条测试的时间上限**——**长序列要动 `SQTO`**
（raw: `../02.06_Command_Reference/02.06.02.02.242_SQTO__SQTO__-__SeQuencer_TimeOut.md`，**本页没读那一篇**）。

> **这一句的宾语值得记一笔**：原文 `increase` 的宾语写的是 **`the SmarTest Work Center`**，
> **不是 `the timeout`**。**本页照实抄，不替它改，也不据此推断 `SQTO` 到底改的是什么**（§11）。
> **后果：本页答不上来「`SQTO` 该怎么写才够我的长序列跑完」**——那要看那一篇。

### 支持的硬件（**本篇最实的一节**）

> 「SmartRDI supports the following hardware cards:
>
> - Digital cards: PS1600, PS5000
> - DC Scale and VI cards: DPS128, UHC4T, XPS256」

**数字卡两张、DC Scale / VI 卡三张**——**这就是本篇给出的全部支持列表**。
**注意这一节的成员和 `## Functional changes` 的成员不一样**，见 `## 出处` ⚠️③。

### 本篇没写的（**指到别处去了**）

- **`RDI_BEGIN()` / `RDI_END()` 的代码结构**：本篇只说「放里面 / 放外面」，
  **真正的结构定义它推给 `Code structure with SmartRDI`**（`02.07.13.05`，**本页没读**）。
- **两种模式的细节**：推给 `Code-based and pattern-based programming`（`02.07.01.01.02`，**本页没读**）。
- **`RDI_INFO_LEVEL` 是什么**：本篇那一节全文就一句
  「See RDI_INFO_LEVEL for more information about information levels.」——**等于没写**
  （`02.07.13.06`，**本页没读**）。

## 典型用法

**⚠️ 先说清楚这一节的成色**：本篇**没有 `## Procedure`、没有 `## Before you begin`、没有任何分步说明**。
正文只有「类表 ＋ `## Execution mode` 两段 ＋ 三节指路 ＋ 支持硬件 ＋ 版本」。
**所以下面每一条都是从这两段描述和类表里读出来的，不是照原文步骤抄的。**

**1. 先决定「这段代码放哪」——放错位置那个模式就不生效：**

| 你要的 | 代码放哪 | 本篇逐字 |
|---|---|---|
| 走 **pattern-based**（生成 burst pattern ＋ analog set） | **`RDI_BEGIN()` / `RDI_END()` 里面** | 「generate a burst pattern … in a RDI_BEGIN()/RDI_END() block」 |
| 走 **code-based**（不生成，工作站逐条执行） | **block 外面** | `Put the code to be executed in the code-based mode outside of the RDI_BEGIN()/RDI_END() block.` |

**这是本篇唯一一条「位置」规矩。**「放反了不报错、只是不生效」是**本页的推断**——
依据是两处措辞（code-based 的代码 `outside`、pattern-based 的生成 `in a … block`），
**原文没有说放错了会怎样**。

**2. 一个 test method 里可以有多个 block：**
`You can have multiple RDI_BEGIN()/RDI_END() blocks in one test method.`——
**每个 block 在 burst pattern 名字里占一个编号**（`_rdi_burst_` ＋ suite 名 ＋ block 号）。
**但 setup 只在 build 后第一跑生成一次**，**所以「多 block」不等于「多生成一次」**。

**3. 四条会咬人的前提（全部出自本篇）：**

| 前提 | 本篇原文 | 不满足会怎样 |
|---|---|---|
| **改了 device setup 要重新 build** | `Build the test method again when the device setups are reloaded or modified.` | **原文没说**；按上一句推断＝跑旧 setup |
| **长序列要调大 sequencer timeout** | `For long sequences use SQTO, SQTO? - (SeQuencer TimeOut) …`（默认 `900 s`） | **原文没说**（语料未写） |
| **production 模式前要对齐代码与 setup** | `Keep the test method code and the device setup aligned before executing in the production mode.` | **原文没说**；production 不生成 setup，**推断＝拿旧 setup 跑新代码** |
| **multiport 要同步时间得自己调 `portSync()`** | 「The function portSync() can be used to synchronize the time among all the ports.」 | **不同 port 默认并行**——**不对齐就会错位** |

**4. 挑 class**：要做什么测试就用类表里那一个
（DC 用 `dc()`、数字捕获用 `digCap()`、功能测试用 `func()`、协议用 `protocol()`、
RF / mixed signal 在 `dc()` 那条指到的 AWG/DGT 篇里……）。**每一个 class 的用法都不在本页。**

**5. 调试时可以先切 single mode**：`the pattern will be executed when the corresponding code is executed`
——**代码走到哪，pattern 就执行到哪**。**但「怎么切」本篇没给**（见 `## 是什么` 里那段提示）。

**6. 本页答不上来的（语料未写 / 本页未读）：**
- **初始化调在哪、什么时候调**——**本篇 117 行里没有 `RDI_INIT`**（它只出现在本页语法节里）。
- **一个 block 里能放几条 `execute()`、有没有上限**——本篇没写。
- **有没有一个完整的、能照着抄的最小 SmartRDI test method**——本篇没给，
  它把这件事推给 `Code structure with SmartRDI`（**本页没读**）。

## 和谁有关

### 本篇亲自点名的硬件（**文档事实**）

| 本篇写的 | 链 | 本篇一共说了什么 |
|---|---|---|
| `PS1600`（Digital cards） | [[ps1600]] | **只有「被支持」三个字** |
| `PS5000`（Digital cards） | [[ps5000]] | 同上；另外 `## Functional changes` 说它在 SmarTest 7.10.2 加进来 |
| `XPS256`（DC Scale and VI cards） | [[xps256-status-flags]]、[[dc-scale-xps256-card]] | **只有「被支持」**——**本篇没有说 XPS256 的 status flags 或 DC Scale 用法和 SmartRDI 有什么关系** |
| `DPS128`、`UHC4T` | **反引号**（不在 allowlist） | 只有「被支持」 |

> **这四条关系薄得只有一层**：本篇是「支持列表」，**不是「怎么用」**。
> **本页不替它补**——**「SmartRDI 怎么驱动 XPS256」这类问题，本篇一个字都没有**（§10）。

### 本篇亲自点名的其他东西（**文档事实**）

- [[hidden-upload]]——**本篇点名了两次**：五条定位里的
  `result retrieving with transparent hidden upload`，以及类表里的
  `hiddenUpload()` class → *Using hidden upload with SmartRDI*。
  **所以「SmartRDI 和 hidden upload 是一体的」是文档事实，不是本页推的。**
- [[sequencer]]——本篇点名两次：`automated sequencer based pattern burst generation`
  与 `the default sequencer timeout is 900 s`。**SmartRDI 生成的就是 sequencer 要跑的东西。**
- [[pattern]]——本篇的核心动词都在 pattern 上：`burst pattern`、`pattern-based mode`、
  `The generated burst pattern is named as "_rdi_burst_" …`。
- [[level]] 与 [[timing]]——**本篇类表里 `level()/timing()` 是同一个 class**，
  指向 *SmartRDI: Level and timing set changes*。**这是本篇唯一一次点名这两个 stage。**
- [[testmethod]]（**本页的 `stage`**）——依据是本篇第一句
  `… to create your test method program`；`## Execution mode` 里又写
  `The setups are based on normal test method APIs.`
- [[results]]——依据是本篇
  `For each class, functions are provided to set up the test and retrieve the test result.`
  **只有这一句**；**本篇没有讲任何结果格式、判定或数据结构。**
- [[error-map]]——依据是五条定位里的 `error map`（夹在那一串 pattern burst 的宾语里）。
  **本篇没有展开它。**
- [[test-method-class]]——**⚠️ 本篇没有出现这个词组**：
  它写的是 `test method program` / `test method APIs` / `test method`。
  **这个名字是从 allowlist 得知存在的**，本页**不据此声称任何关系**。
- [[pin]]——**⚠️ 本篇里 `pin` 只作为卡名的一部分出现**（`Pin Scale 5000 card added.`，
  `## Functional changes` 最后一条），**不是 pin 这个 stage 的意思**。
  **本页不因为「stage 邻居」把它链成对象关系。**

### 本篇点名、但没有页、故用反引号 ＋ raw 路径的

- `SQTO, SQTO?`（raw: `../02.06_Command_Reference/02.06.02.02.242_SQTO__SQTO__-__SeQuencer_TimeOut.md`）
  ——**本篇唯一一条指到 L1 固件命令的链接。本页没读那一篇。**
- `portSync()`——**本篇正文只给了名字**；它的语法在本页 `## 语法 / 参数` 的
  *Multiport handling › portSync* 段里（**脚本从子主题抽的，本页没读那个子主题**）。

### 本页没链的（**因为本篇一个字都没提**）

- [[smartcalc]]——**本篇 117 行里没有 `SmartCalc`、没有 `SMC`**。
  **⚠️ 但本页 `## 语法 / 参数` 里有一段的段名是「Using SmartCalc SMC with SmartRDI」**
  ——**那是脚本从子主题抽来的**，**本页没读那个子主题**，
  **所以这里只记「那一节存在」，不写它们的关系。**
- [[testflow]] / [[project]]——本篇只说 `test suite` / `test method`，**这两个词没有出现**。
- [[test-suite-control-api]] / [[tpi-program-routines]]——**本篇没有任何一处提到外部控制**
  （TSCA / TPI / HVM 一个都没出现）。**这一条在本页还有第二个用处**：见 `## 出处` 的「待复核」。
- [[pogo-block-compatibility]]——**它不是对象关系**，是坏字对照表的去处，只在 `## 出处` ⚠️① 里链一次。

## 版本

**本文档有 `## Functional changes` 段，四条（逐字）：**

- `Introduced in SmartRDI 2.1.0`
- `SmartRDI 2.4.2: DC Scale AVI64 card added.`
- `SmartRDI 7.5.0: DC Scale FVI16 card added.`
- `SmarTest 7.10.2: Pin Scale 5000 card added.`

**读法（这是本篇最需要注意的一节）：**

| 要点 | 说明 |
|---|---|
| **不是 §11.2 ② 那个哨兵** | 本篇写的是 `Introduced in SmartRDI 2.1.0`——**带了产品名和号**，**不是 `Introduced before SmarTest 6.3.2` 那种「覆盖之前就有」的哨兵**。**所以本篇这四条可以直读**，不需要做那一层解读。 |
| **两套产品线号混在一张表里** | 三条 `SmartRDI x.y.z`（`2.1.0` / `2.4.2` / `7.5.0`），一条 `SmarTest 7.10.2`。**原文没有给这两套号的对应关系**（§11.2 ④）。**别把 `SmartRDI 2.4.2` 读成 `SmarTest 2.4.2`。** |
| **四条里有三条是「加了张卡」** | `AVI64` / `FVI16` / `Pin Scale 5000`——**SmartRDI 这个 API 本身的语法变更，本篇一条都没记**。 |
| **7.10.3 上没有新增条目** | 本 wiki 面向 7.10.3，而**最后一条是 `SmarTest 7.10.2`**——**照这一节读，7.10.2 到 7.10.3 之间 SmartRDI 的功能没变过**（这是对「本节只有四条」的读法，**不是原文明说**）。 |

**本页答不上来的版本问题**：**「哪些 SmarTest 版本真的支持 SmartRDI」本篇只给了一个链接**
——`See [Supported SmarTest Versions](<02.07.13.01.11_Supported_SmarTest_Versions.md>)`，
**那一篇本页没读**。**所以 7.10.3 上 SmartRDI 要装什么、是什么状态，本页一个字都没有。**

> **本页语法节里还有别的版本句**（那些是脚本从子主题抽的，**本页没读那些子主题**，
> **故不列、也不当证据**）：例如「Starting from 2.4.5, SmartRDI can insert CTIM instructions…」、
> 「Important: With SmarTest7.4.3.0 and 7.4.3.1, immediate upload only allows ONE result id in a pin.」、
> 「Starting from 7.5.2, SmartRDI provides more information in the UI report window…」。
> **这三句说明「版本信息主要在子主题里」，不在本页这一篇里。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md`
（TDC `142069.htm`，**116 行**）

**本页没做的（按缺口大小排）：**

- **147 个子主题，一篇都没读。** 本页 `## 语法 / 参数` 的抬头自己列了 **147 条路径**
  （`02.07.13.01` … `02.07.13.24.49.03`），**它的 307 个 `###` 段全是从这些子主题抽的，
  共 112,533 字符**。**这是本页最大的缺口**：**那 14 个 class 的行为、`RDI_BEGIN` 的 `mode` 取值、
  `portSync` 的约束，全在那些子主题里，本页一个字都没读。**
  本篇自己列的**直接**子主题是 **24 个**（`#### Subtopics`，第 10–33 行）。
- **三张图没看**（本篇共三张）：第 80 行 `../../../../raw/146718.png`（alt `Pattern鈥慴ased mode`）；
  第 92 行有两个——`../../../../raw/142927.png`（alt `single execution`）
  与 `../../../../raw/142928.png`（alt `burst mode`）。
  **后果：「single mode 和 burst mode 在时序上到底差在哪」本页只有文字，图里的信息一条都没有。**
- **五篇被本篇指过去、本页没读的文档**：
  `02.07.13.01.11_Supported_SmarTest_Versions`、`02.07.13.05_Code_structure_with_SmartRDI`、
  `02.07.13.06_RDI_INFO_LEVEL`、`02.07.01.01.02_Code-based_and_pattern-based_programming`、
  `../02.06_Command_Reference/02.06.02.02.242_SQTO__SQTO__-__SeQuencer_TimeOut`。
- **没有 `## Procedure` / `## Before you begin`**——本篇正文只有
  Subtopics / 简介 / `## SmartRDI classes` / `## Execution mode` / `## RDI_INFO_LEVEL` /
  `## Supported hardware` / `## Supported SmarTest versions` / `## Functional changes`。
  **所以 `## 典型用法` 是照两段模式描述和类表拼的，不是照原文步骤抄的。**
- **本篇没有语法段**（没有 `Syntax` / `Parameters` 这类段标记），**所以本页正文里没有手抄的语法块**
  ——**这一页与 `[[jsdf]]` / `[[jspr]]` 那两页不同**，那两页是脚本漏抽、由正文手抄补进去的。
- **没有在任何真实机台上跑过 SmartRDI**（`verified: doc-only`）。
  **`_rdi_burst_` 的命名是不是真的这么拼、900 s 是不是真的、production 模式跑起来什么样，
  本页只能保证「文档这么写」（§11）。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 全篇 12 处坏字，全部集中在「…-based」这几个词上。** 坏的是
> **「短横 ＋ 后面那个字母」被一起编码坏了**这一族（§11.2 ①）。本篇实际用到三种：
>
> | 语料里 | 实际是 | 验算 | 处数 / 行号 |
> |---|---|---|---|
> | `鈥慴` | `-b` | `pattern鈥慴ased` = *pattern-based* | **10 处**（66 ×3、70 ×2、72 ×2、80 ×1、90 ×2） |
> | `鈥慶` | `-c` | `sequencer鈥慶ontrolled` = *sequencer-controlled* | 1 处（66） |
> | `鈥慺` | `-f` | `user鈥慺riendly` = *user-friendly* | 1 处（66） |
>
> **已有的对照表在 `[[pogo-block-compatibility]]`**（那里有 `鈥慸`=`–d`、`鈥慼`=`–h`、`鈥慴`=`–b`）；
> **`鈥慶`=`-c` 与 `鈥慺`=`-f` 是那张表里还没有的两行**（§11.2 ① 记过 `鈥慶`=`‑c`）。
> **⚠️ 别只把 `鈥慴` 替成一个短横**——**它把后面那个字母一起吃了**，
> 只替短横会得到 `pattern-ased` 这种残词。
> **这是语料的问题，不是抽取的 bug，raw 只读不许改（§1.1）。**
>
> **② 第 35 行的内部锚点和它要跳的标题不一致。**
> 第 35 行逐字是 `Use the [classes](<02.07.13_SmartRDI.md#_142069__s_SRDI_classes>) to setup your tests.`，
> 而它要跳的标题、第 45 行逐字是 `## SmartRDI classes`
> ——**锚点里写的是 `SRDI`，标题里是 `SmartRDI`，少了一个 `mart`。**
> **这一处是不是真的跳不过去，本页没有验**：**`.htm` 不在 `sources:` 里，本页没打开它**，
> 而锚点最终由 HTML 那边决定。**能确定的只有一件事：本篇自己给的两串字不一样。**
>
> **③ `## Supported hardware` 与 `## Functional changes` 两张名单的成员不同。**
> `## Supported hardware`（第 102–106 行）列的是
> Digital cards `PS1600`, `PS5000`、DC Scale and VI cards `DPS128`, `UHC4T`, `XPS256`；
> `## Functional changes`（第 113–116 行）另外提到 **`AVI64`（2.4.2）** 与 **`FVI16`（7.5.0）**，
> 两条都写作 **`DC Scale … card`**。
> ——**这两张 DC Scale 卡都不在 `## Supported hardware` 的 DC Scale 名单里**；
> **而 `PS5000` 在名单里，它的引入记在 `## Functional changes` 最后一条。**
> **原文没有说这两处该怎么对上**（§10：本页不替它调和）。
> **推断（标明是推断）**：`## Supported hardware` 这一节看起来没有随 `## Functional changes` 一起更新；
> **但这只是一种解释**，另一种是「AVI64 / FVI16 支持但没列全」。**本页不选一个当答案。**
>
> **④ `SQTO` 那一句的宾语可疑**：第 84 行逐字是
> `For long sequences use SQTO, SQTO? - (SeQuencer TimeOut) to increase the SmarTest Work Center.`
> ——**`increase` 的宾语写的是 `the SmarTest Work Center`，不是 `the timeout`。**
> **照实记，本页不替它改，也不据此推断 `SQTO` 改的到底是什么**（要说得看那一篇）。
>
> **⑤ 三张图的路径都是从语料树里往上爬了四级**（`../../../../raw/…`）——
> 而本篇位于 `02_System_reference/02.07_Test_Method_Reference/`，
> **四级之上已经不是语料树里文档的位置了**（同类现象在 `[[smartcalc-framework]]` 那一页也记过）。
> **本页没有打开这三张图**，所以**只记路径的形状，不判断它到底指到哪。**
>
> **⑥ §11.2 ② 那个哨兵在本篇没有出现。** 记这一条是为了**把「查过」和「没查」分开**：
> 本篇版本段第一条是 `Introduced in SmartRDI 2.1.0`，**是明确的产品 ＋ 版本号**。
> **本页确实去看了这一节，且这一节确实不是哨兵**——
> **这和第 ⑥′ 条教训（检查绿是因为查到了、还是因为什么都没查）是两件事，所以分开写。**
>
> **⑦ 本页在本篇里没有发现第三种坏字**（`渭` / `碌` / `掳` 那一类 **µ**、**°** 一个都没出现）。
> **但这是「本页读到的」，不是「本篇干净」**（§13.1 第 ⑥′）。
> **本篇只有 117 行、且 12 处坏字全挤在同一个词族里**——**能出坏字的面积本身就小**，
> **把「没发现」写成「没有」，正是这一系列教训里反复出现的那一步。**

> **待复核（这不是语料瑕疵，是本页对骨架字段的疑问，本页没有改它）**：
> 本页 frontmatter 是 **`layer: L3`**。**按规矩本页不许改 `layer`**，故原样留着。
> **但本篇的定位与 `L3` 对不上**：
> - `schema.md` 第 81–94 行把 **`L3 — 外部控制`** 定义成三样：
>   **Test suite control API（`02.09.01.14`）/ TPI（`02.09.01.09`）/ HVM API（`02.09.01.10`）**，
>   判据是「**调用者是外部进程**」；
> - 而 `schema.md` 第 84 行把 **`L2 — Test Method API`** 定义成「本阶段在 C++ 测试方法里对应的 API」；
> - **本篇逐字说 SmartRDI 是 `a high level of programming interface to create your test method program`**；
> - **本篇的文档位置在 `02_System_reference/02.07_Test_Method_Reference/`（Test Method Reference）下**；
> - **同类的 [[hidden-upload]] 那一页（SmartRDI 的 hidden upload）在 wiki 里就是 `layer: L2`、`stage: testmethod`**。
>
> **推断（不是文档事实）：`layer` 应为 `L2`。** 上面五条是本页能给的推理链，**本页没有改字段**。
> **另一条旁证**：本篇 117 行里**没有任何一处提到外部控制**（TSCA / TPI / HVM 一个都没出现）——
> `layer: L3` 若正确，本篇本该是介绍那个接口的地方。

`verified: doc-only`
