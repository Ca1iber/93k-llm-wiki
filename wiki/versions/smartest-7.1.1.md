---
type: version
title: SmarTest 7.1.1 — 版本页
tags: [version, smartest]
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.16_Protocol_Aware_preference_page.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.03.01.05_DUT_interface_layout_-_A-Test_Head_with_DUT_Scale_interface.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.03.01.06_DUT_interface_layout_-_Compact_Test_Head_with_DUT_Scale_interface.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.04_UHC4___UHC4T_capacitor_requirements.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03.04_PS1600_DC_value_measurements.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.02_JSCF__JSCF__-__Jitter_Set_ConFiguration.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.01.06_How_to_handle_ARRAY_x_data_type.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.08.01_BADC_PIN_MEASURE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.09_BADC_SETTING.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.122.01_JITTER_INJECTION_PINS.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.176_PutDebugGraph.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.197_SCAN_TEST_RESULT.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.01.07_TMU_PINS.getAThreshold.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.01.08_TMU_PINS.getBThreshold.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.01.17_TMU_PINS.setAThreshold.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.01.18_TMU_PINS.setBThreshold.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02.02_ARRAY_D.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02.03_ARRAY_COMPLEX.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01.01_Frequency_byDigitalCapture.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01.02_FunctionalTest.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01.03_JitterHistogram.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01.04_JitterSeparation.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01.06_JitterStardust.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01.07_ParametricFunctionalTest.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01.08_SetBasedSpecSearch.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01.09_Shmoo.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01.10_SpecSearch.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.02.01_Continuity.md
  # 本页共涉及 68 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.1.1

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（84 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.1.1:` 前缀，**那是原文的一部分，没有去掉**。

- [Protocol Aware preference page](<01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.16_Protocol_Aware_preference_page.md>) —— SmarTest 7.1.1: Added new option to control Test Program Exlplorer's behavior upon un-/loading protocol definition.
- [UHC4 / UHC4T capacitor requirements](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.04_UHC4___UHC4T_capacitor_requirements.md>) —— SmarTest 7.1.1: Update on capacitor examples
- [PS1600 DC value measurements](<02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03.04_PS1600_DC_value_measurements.md>) —— SmarTest 7.1.1: Modified connect function to switch BADC relays
- [JSCF, JSCF? - (Jitter Set ConFiguration)](<02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md>) —— SmarTest 7.1.1: WAVEFORM parameter SINUS changed to SINUSOIDAL
- [JSCF, JSCF? - (Jitter Set ConFiguration)](<02_System_reference/02.06_Command_Reference/02.06.16.02.02_JSCF__JSCF__-__Jitter_Set_ConFiguration.md>) —— SmarTest 7.1.1: WAVEFORM parameter SINUS changed to SINUSOIDAL
- [How to handle ARRAY_x data type](<02_System_reference/02.07_Test_Method_Reference/02.07.03.01.06_How_to_handle_ARRAY_x_data_type.md>) —— SmarTest 7.1.1: splitInto() has been obsoleted, refer to enhanced functions MEAS_DEF().getWaveform() and MEAS_DEF().getComplexWaveform().
- [BADC_PIN_MEASURE](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.08.01_BADC_PIN_MEASURE.md>) —— SmarTest 7.1.1: Modified connect function to switch BADC relays
- [BADC_SETTING](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.09_BADC_SETTING.md>) —— SmarTest 7.1.1: Modified connect function to switch BADC relays
- [JITTER_INJECTION_PINS](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.122.01_JITTER_INJECTION_PINS.md>) —— SmarTest 7.1.1: New member function JITTER_INJECTION_PINS& setAllowedNoise(int allowed_noise);
- [JITTER_INJECTION_PINS](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.122.01_JITTER_INJECTION_PINS.md>) —— SmarTest 7.1.1: JITTER_INJECTION_PINS& setWaveFormSinus(DOUBLE amplitude, DOUBLE period); member function changed to JITTER_INJECTION_PINS& setWaveFormSinusoidal(DOUBLE amplitude, DOUBLE period);
- [LEVEL_SPEC](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.md>) —— SmarTest 7.1.1: Change function for a specific pin / pin list added
- [PutDebugGraph](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.176_PutDebugGraph.md>) —— SmarTest 7.1.1: setObject() has been made thread safe.
- [SCAN_TEST_RESULT](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.197_SCAN_TEST_RESULT.md>) —— SmarTest 7.1.1: New member function setTestConditionList()
- [SCAN_TEST_RESULT](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.197_SCAN_TEST_RESULT.md>) —— SmarTest 7.1.1: New member function setLabelName()
- [TMU_PINS.getAThreshold()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.01.07_TMU_PINS.getAThreshold.md>) —— SmarTest 7.1.1: Renamed to getAThreshold().
- [TMU_PINS.getBThreshold()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.01.08_TMU_PINS.getBThreshold.md>) —— SmarTest 7.1.1: Renamed to getBThreshold().
- [TMU_PINS.setAThreshold()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.01.17_TMU_PINS.setAThreshold.md>) —— SmarTest 7.1.1: Renamed to setAThreshold().
- [TMU_PINS.setBThreshold()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.01.18_TMU_PINS.setBThreshold.md>) —— SmarTest 7.1.1: Renamed to setBThreshold().
- [ARRAY_D](<02_System_reference/02.07_Test_Method_Reference/02.07.04.02.02_ARRAY_D.md>) —— SmarTest 7.1.1: splitInto() has been obsoleted, refer to enhanced functions MEAS_DEF().getWaveform() and MEAS_DEF().getComplexWaveform()
- [ARRAY_COMPLEX](<02_System_reference/02.07_Test_Method_Reference/02.07.04.02.03_ARRAY_COMPLEX.md>) —— SmarTest 7.1.1: splitInto() has been deprecated, refer to enhanced functions MEAS_DEF().getWaveform() and MEAS_DEF().getComplexWaveform()
- [Frequency_byDigitalCapture](<02_System_reference/02.07_Test_Method_Reference/02.07.05.01.01_Frequency_byDigitalCapture.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [FunctionalTest](<02_System_reference/02.07_Test_Method_Reference/02.07.05.01.02_FunctionalTest.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [JitterHistogram](<02_System_reference/02.07_Test_Method_Reference/02.07.05.01.03_JitterHistogram.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [JitterSeparation](<02_System_reference/02.07_Test_Method_Reference/02.07.05.01.04_JitterSeparation.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [JitterStardust](<02_System_reference/02.07_Test_Method_Reference/02.07.05.01.06_JitterStardust.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [ParametricFunctionalTest](<02_System_reference/02.07_Test_Method_Reference/02.07.05.01.07_ParametricFunctionalTest.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [SetBasedSpecSearch](<02_System_reference/02.07_Test_Method_Reference/02.07.05.01.08_SetBasedSpecSearch.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [Shmoo](<02_System_reference/02.07_Test_Method_Reference/02.07.05.01.09_Shmoo.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [SpecSearch](<02_System_reference/02.07_Test_Method_Reference/02.07.05.01.10_SpecSearch.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [Continuity](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.01_Continuity.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [Continuity](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.01_Continuity.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [Continuity](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.01_Continuity.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [DpsConnectivity](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.02_DpsConnectivity.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [DpsConnectivity](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.02_DpsConnectivity.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [DpsConnectivity](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.02_DpsConnectivity.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [DpsStatus](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.03_DpsStatus.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [DpsStatus](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.03_DpsStatus.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [DpsStatus](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.03_DpsStatus.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [DVM](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.04_DVM.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [DVM](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.04_DVM.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [DVM](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.04_DVM.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [GeneralPMU](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.05_GeneralPMU.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [GeneralPMU](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.05_GeneralPMU.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [GeneralPMU](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.05_GeneralPMU.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [HighZ](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.06_HighZ.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [HighZ](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.06_HighZ.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [HighZ](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.06_HighZ.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [Leakage](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.07_Leakage.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [Leakage](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.07_Leakage.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [Leakage](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.07_Leakage.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [OperatingCurrent](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.08_OperatingCurrent.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [OperatingCurrent](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.08_OperatingCurrent.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [OperatingCurrent](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.08_OperatingCurrent.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [OutputDC](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.09_OutputDC.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [OutputDC](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.09_OutputDC.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [OutputDC](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.09_OutputDC.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [ProductionIddq](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.10_ProductionIddq.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [ProductionIddq](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.10_ProductionIddq.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [ProductionIddq](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.10_ProductionIddq.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [StandbyCurrent](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.11_StandbyCurrent.md>) —— SmarTest 7.1.1: Test table is supported in TML 2.1.1.
- [StandbyCurrent](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.11_StandbyCurrent.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [StandbyCurrent](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.11_StandbyCurrent.md>) —— SmarTest 7.1.1: New parameter testName is added in TML 2.1.1.
- [Continuity](<02_System_reference/02.07_Test_Method_Reference/02.07.05.03.01_Continuity.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [DpsConnectivity](<02_System_reference/02.07_Test_Method_Reference/02.07.05.03.02_DpsConnectivity.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [DpsStatus](<02_System_reference/02.07_Test_Method_Reference/02.07.05.03.03_DpsStatus.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [GeneralPMU](<02_System_reference/02.07_Test_Method_Reference/02.07.05.03.04_GeneralPMU.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [Leakage](<02_System_reference/02.07_Test_Method_Reference/02.07.05.03.05_Leakage.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [OperatingCurrent](<02_System_reference/02.07_Test_Method_Reference/02.07.05.03.06_OperatingCurrent.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [OutputDC](<02_System_reference/02.07_Test_Method_Reference/02.07.05.03.07_OutputDC.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [ProductionIddq](<02_System_reference/02.07_Test_Method_Reference/02.07.05.03.08_ProductionIddq.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [ScanTest (scan_tml)](<02_System_reference/02.07_Test_Method_Reference/02.07.05.05_ScanTest__scan_tml.md>) —— SmarTest 7.1.1: Mixed usage of test table and testflow limits in one testflow is supported in TML 2.1.1.
- [Current cycle and pattern](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.03.02.01_Current_cycle_and_pattern.md>) —— SmarTest 7.1.1: Displaying the current pattern and its cycle number
- [Error map tabs](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.03.02.03_Error_map_tabs.md>) —— SmarTest 7.1.1: Displaying the current pattern and its cycle number
- [View control area](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.03.02_View_control_area.md>) —— SmarTest 7.1.1: Displaying the current pattern and its cycle number
- [Elements of the Error Map Tool](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.03_Elements_of_the_Error_Map_Tool.md>) —— SmarTest 7.1.1: Displaying the current pattern and its cycle number
- [File menu](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.10.03.01_File_menu.md>) —— SmarTest 7.1.1: Save values for configured channels
- [Configured channels](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.10.03.03.01_Configured_channels.md>) —— SmarTest 7.1.1: Save values for configured channels
- [How to create and execute the client application with HVM API](<02_System_reference/02.09_Test_Program_Management/02.09.01.10.02.06_How_to_create_and_execute_the_client_application_with_HVM_API.md>) —— SmarTest 7.1.1: More libraries are needed to build the program.
- [LotSummaryGenerator](<02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md>) —— SmarTest 7.1.1: Support the option -w waferIDVariable
- [LotSummaryGenerator](<02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md>) —— SmarTest 7.1.1: Add FF/TF/TT to the output file
- [LotSummaryGenerator](<02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md>) —— SmarTest 7.1.1: Start LotSummaryGenerator automatically when executing test program/testflow
- [Configuring the contents of the STDF file](<02_System_reference/02.10_Data_Logging/02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md>) —— SmarTest 7.1.1: New configuration options lowLimitFormatString, highLimitFormatString, and adjust_STR_PAT_NUM
- [Parametric Test Record (PTR)](<02_System_reference/02.10_Data_Logging/02.10.03.05.22_Parametric_Test_Record__PTR.md>) —— SmarTest 7.1.1: The values of the C-RESFMT, C_LLMFMT, and C_HLMFMT fields are no longer hardcoded.
- [Multiple-Result Parametric Record (MPR)](<02_System_reference/02.10_Data_Logging/02.10.03.05.23_Multiple-Result_Parametric_Record__MPR.md>) —— SmarTest 7.1.1: The values of the C-RESFMT, C_LLMFMT, and C_HLMFMT fields are no longer hardcoded.


## 这一版新引入（10 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [DUT interface layout - A-Test Head with DUT Scale interface](<02_System_reference/02.03_DUT_board_design_reference/02.03.03.01.05_DUT_interface_layout_-_A-Test_Head_with_DUT_Scale_interface.md>) —— Introduced in SmarTest 7.1.1
- [DUT interface layout - Compact Test Head with DUT Scale interface](<02_System_reference/02.03_DUT_board_design_reference/02.03.03.01.06_DUT_interface_layout_-_Compact_Test_Head_with_DUT_Scale_interface.md>) —— Introduced in SmarTest 7.1.1
- [DriftEyeOpening](<02_System_reference/02.07_Test_Method_Reference/02.07.05.07.01_DriftEyeOpening.md>) —— Introduced in SmarTest 7.1.1
- [Frequency](<02_System_reference/02.07_Test_Method_Reference/02.07.05.07.02_Frequency.md>) —— Introduced in SmarTest 7.1.1
- [Jitter (TIE)](<02_System_reference/02.07_Test_Method_Reference/02.07.05.07.03_Jitter__TIE.md>) —— Introduced in SmarTest 7.1.1
- [PropDelay](<02_System_reference/02.07_Test_Method_Reference/02.07.05.07.04_PropDelay.md>) —— Introduced in SmarTest 7.1.1
- [PulseWidth](<02_System_reference/02.07_Test_Method_Reference/02.07.05.07.05_PulseWidth.md>) —— Introduced in SmarTest 7.1.1
- [RiseFallTime](<02_System_reference/02.07_Test_Method_Reference/02.07.05.07.06_RiseFallTime.md>) —— Introduced in SmarTest 7.1.1
- [Pin Scale 1600 Card](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.01.04.01_Pin_Scale_1600_Card.md>) —— Introduced in SmarTest 7.1.1
- [Migrating TIA per pin to per TMU per pin](<03_Use_cases_and_application_papers/03.12_SmarTest_Program_Migration_Framework/03.12.06_Migrating_TIA_per_pin_to_per_TMU_per_pin.md>) —— Introduced in SmarTest 7.1.1


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 94 条**，涉及 **68 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
