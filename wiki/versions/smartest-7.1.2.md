---
type: version
title: SmarTest 7.1.2 — 版本页
tags: [version, smartest]
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.03_Editing_technology_data.md
  - 01_Getting_started/01.05_SmarTest_character_and_number_limits/01.05_SmarTest_character_and_number_limits.md
  - 02_System_reference/02.02_Specifications/02.02.02.07_Power_requirements.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.01.03_MBAV8___MCE__pogo_pin_assignment.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.03_IOCHANNEL_section.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03.04_PS1600_DC_value_measurements.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.233_SQIB__SQIB__-__SeQuencer_Interrupt_Behavior.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.42_DCEL__DCEL__-__Digital_Compare_Exception_List.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.08_DFPN__DFPN__-__DeFine_Pin_Name.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.03_Defining_edge_delays_for_a_pattern__ased_SmartLoop_test.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.05_Dealing_with_storage_problems_on_Smart_Scale_systems.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.08_DCEL__DCEL__-__Digital_Compare_Exception_List.md
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.32_SQIB__SQIB__-__SeQuencer_Interrupt_Behavior.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.05_Retrieving_AC_Test_Results.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.16.03_Error_Handling_on_Missing_Trigger_Input.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.08.01_BADC_PIN_MEASURE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.09_BADC_SETTING.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.151_PMU_IFVM.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.152_PMU_VFIM.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.217_SET_TESTFLOW_FLAG.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.251_TMU_RESULTS.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.01_TMU_PINS.errorState.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.03_TMU_PINS.getPinsFinishedButMayFailed.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.04_TMU_PINS.getPinsFinishedNotFailed.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.05_TMU_PINS.getPinsFailed.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.06_TMU_PINS.getPinsNotFinished.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.96_GET_TESTFLOW_FLAG.md
  # 本页共涉及 84 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.1.2

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（40 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.1.2:` 前缀，**那是原文的一部分，没有去掉**。

- [Editing technology data](<01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.03_Editing_technology_data.md>) —— SmarTest 7.1.2: New option: Period resolution compatibility model
- [Power requirements](<02_System_reference/02.02_Specifications/02.02.02.07_Power_requirements.md>) —— SmarTest 7.1.2: Adapted maximum power consumption for small and large test head, and need for autotransformer conditions
- [IOCHANNEL section](<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.03_IOCHANNEL_section.md>) —— SmarTest 7.1.2: Renamed: HSM4000 is now HSM4G
- [PS1600 DC value measurements](<02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03.04_PS1600_DC_value_measurements.md>) —— SmarTest 7.1.2: Added functions: badcSetting.xxx and badcMeasure.xxx
- [DFPN, DFPN? - (DeFine Pin Name)](<02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md>) —— SmarTest 7.1.2: For 64-bit systems: Number of of characters for pinName extended.
- [DFPN, DFPN? - (DeFine Pin Name)](<02_System_reference/02.06_Command_Reference/02.06.03.02.08_DFPN__DFPN__-__DeFine_Pin_Name.md>) —— SmarTest 7.1.2: For 64-bit systems: Number of of characters for pinName extended.
- [Defining the wavetable for a pattern鈥慴ased SmartLoop test](<02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md>) —— SmarTest 7.1.2: All x-modes are now supported. Pattern鈥慴ased SmartLoop can now also be combined with transition tracking in x6-mode.
- [Defining edge delays for a pattern鈥慴ased SmartLoop test](<02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.03_Defining_edge_delays_for_a_pattern__ased_SmartLoop_test.md>) —— SmarTest 7.1.2: Pattern鈥慴ased SmartLoop can now also be combined with transition tracking in x6-mode.
- [Retrieving AC Test Results](<02_System_reference/02.07_Test_Method_Reference/02.07.03.03.05_Retrieving_AC_Test_Results.md>) —— SmarTest 7.1.2: Support of MBAV8+.
- [Error Handling on Missing Trigger Input](<02_System_reference/02.07_Test_Method_Reference/02.07.03.16.03_Error_Handling_on_Missing_Trigger_Input.md>) —— SmarTest 7.1.2: Support of MBAV8+.
- [BADC_PIN_MEASURE](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.08.01_BADC_PIN_MEASURE.md>) —— SmarTest 7.1.2: Reduced to numberOfSamples() function
- [BADC_SETTING](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.09_BADC_SETTING.md>) —— SmarTest 7.1.2: Added functions: badcSetting.xxx and badcMeasure.xxx
- [PMU_IFVM](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.151_PMU_IFVM.md>) —— SmarTest 7.1.2: PMU in MCE is supported.
- [PMU_VFIM](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.152_PMU_VFIM.md>) —— SmarTest 7.1.2: PMU in MCE is supported.
- [SET_TESTFLOW_FLAG()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.217_SET_TESTFLOW_FLAG.md>) —— SmarTest 7.1.2: Removed rf_cal_enable flag
- [TESTSET().testname()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.md>) —— SmarTest 7.1.2: Added forceSTDFTestNam parameter
- [TMU_RESULTS](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.251_TMU_RESULTS.md>) —— SmarTest 7.1.2: New member function getPinsFinishedButMayFailed()
- [TMU_RESULTS](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.251_TMU_RESULTS.md>) —— SmarTest 7.1.2: New member function getPinsFinishedNotFailed()
- [TMU_RESULTS](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.251_TMU_RESULTS.md>) —— SmarTest 7.1.2: New member function getPinsFailed()
- [TMU_RESULTS](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.251_TMU_RESULTS.md>) —— SmarTest 7.1.2: New member function getPinsNotFinished()
- [TMU_PINS.errorState()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.01_TMU_PINS.errorState.md>) —— SmarTest 7.1.2: New option NOT_FINISHED added to TMU::ERROR_TYPE.
- [GET_TESTFLOW_FLAG()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.96_GET_TESTFLOW_FLAG.md>) —— SmarTest 7.1.2: Removed rf_cal_enable flag
- [Editing technology data](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.02_Editing_technology_data.md>) —— SmarTest 7.1.2: New option: Period resolution compatibility model
- [Detailed error map](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01.01_Detailed_error_map.md>) —— SmarTest 7.1.2: Bandwidth related settings introduced
- [Result menu](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.03.01.04_Result_menu.md>) —— SmarTest 7.1.2: Configuration window Bandwidth Related Settings introduced
- [Help menu](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.03.01.05_Help_menu.md>) —— SmarTest 7.1.2: Online help integrated into the Eclipse Workcenter
- [Editing technology data](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.02_Editing_technology_data.md>) —— SmarTest 7.1.2: New option: Period resolution compatibility model
- [Tools Menu](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.02.05.05_Tools_Menu.md>) —— SmarTest 7.1.2: Demodulation introduced
- [Alphabetical list of flags](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md>) —— SmarTest 7.1.2: Removed rf_cal_enable flag
- [Testflow flags](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.02_Testflow_flags.md>) —— SmarTest 7.1.2: Removed rf_cal_enable flag
- [Loop configuration settings](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.01_Loop_configuration_settings.md>) —— SmarTest 7.1.2: Stop on Fail now stops when any test suite in a sequence has an overall fail result and Stop on Pass now stops when all of the test suites in a sequence pass.
- [Running a testflow](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md>) —— SmarTest 7.1.2: Stop on Fail now stops when any test suite in a sequence has an overall fail result and Stop on Pass now stops when all of the test suites in a sequence pass.
- [Defining the wavetable for a pattern鈥慴ased SmartLoop test](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md>) —— SmarTest 7.1.2: All x-modes are now supported. Pattern鈥慴ased SmartLoop can now also be combined with transition tracking in x6-mode.
- [Defining edge delays for a pattern鈥慴ased SmartLoop test](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.03.03_Defining_edge_delays_for_a_pattern__ased_SmartLoop_test.md>) —— SmarTest 7.1.2: Pattern鈥慴ased SmartLoop can now also be combined with transition tracking in x6-mode.
- [Communication with a GPIB interface](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.02_Communication_with_a_GPIB_interface.md>) —— SmarTest 7.1.2: PoE LAN switch E7033B for gateway E7032A (E5810A) introduced
- [LotSummaryGenerator](<02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md>) —— SmarTest 7.1.2: New application variable LOT_SUMMNARY_PATH_NAME and FORCE_SUMMARY_GENERATION_FOR_LEVEL
- [LotSummaryGenerator](<02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md>) —— SmarTest 7.1.2: Support generating lot summary for incomplete data collection file
- [LotSummaryGenerator](<02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md>) —— SmarTest 7.1.2: Support using with BLC program
- [LotSummaryGenerator](<02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md>) —— SmarTest 7.1.2: Remove the option -w waferIDVariable
- [TTT tool](<03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.06.01.01_TTT_tool.md>) —— SmarTest 7.1.2: Parameter --pause introduced


## 这一版新引入（50 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [SmarTest character and number limits](<01_Getting_started/01.05_SmarTest_character_and_number_limits/01.05_SmarTest_character_and_number_limits.md>) —— Introduced in SmarTest 7.1.2
- [MBAV8+ (MCE) pogo pin assignment](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.01.03_MBAV8___MCE__pogo_pin_assignment.md>) —— Introduced in SmarTest 7.1.2
- [SQIB, SQIB? - (SeQuencer Interrupt Behavior)](<02_System_reference/02.06_Command_Reference/02.06.02.02.233_SQIB__SQIB__-__SeQuencer_Interrupt_Behavior.md>) —— Introduced in SmarTest 7.1.2
- [DCEL, DCEL? - (Digital Compare Exception List)](<02_System_reference/02.06_Command_Reference/02.06.02.02.42_DCEL__DCEL__-__Digital_Compare_Exception_List.md>) —— Introduced in SmarTest 7.1.2
- [Dealing with storage problems on Smart Scale systems](<02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.05_Dealing_with_storage_problems_on_Smart_Scale_systems.md>) —— Introduced in SmarTest 7.1.2
- [DCEL, DCEL? - (Digital Compare Exception List)](<02_System_reference/02.06_Command_Reference/02.06.11.02.08_DCEL__DCEL__-__Digital_Compare_Exception_List.md>) —— Introduced in SmarTest 7.1.2
- [SQIB, SQIB? - (SeQuencer Interrupt Behavior)](<02_System_reference/02.06_Command_Reference/02.06.11.02.32_SQIB__SQIB__-__SeQuencer_Interrupt_Behavior.md>) —— Introduced in SmarTest 7.1.2
- [TMU_PINS.getPinsFinishedButMayFailed()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.03_TMU_PINS.getPinsFinishedButMayFailed.md>) —— Introduced in SmarTest 7.1.2
- [TMU_PINS.getPinsFinishedNotFailed()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.04_TMU_PINS.getPinsFinishedNotFailed.md>) —— Introduced in SmarTest 7.1.2
- [TMU_PINS.getPinsFailed()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.05_TMU_PINS.getPinsFailed.md>) —— Introduced in SmarTest 7.1.2
- [TMU_PINS.getPinsNotFinished()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.252.02.02.06_TMU_PINS.getPinsNotFinished.md>) —— Introduced in SmarTest 7.1.2
- [List of transaction based protocol test APIs](<02_System_reference/02.07_Test_Method_Reference/02.07.11.01.03_List_of_transaction_based_protocol_test_APIs.md>) —— Introduced in SmarTest 7.1.2
- [Result Mode](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.01_Result_Mode.md>) —— Introduced in SmarTest 7.1.2
- [Execution Mode](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.02_Execution_Mode.md>) —— Introduced in SmarTest 7.1.2
- [Advanced](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.03_Advanced.md>) —— Introduced in SmarTest 7.1.2
- [Result Configuration](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04_Result_Configuration.md>) —— Introduced in SmarTest 7.1.2
- [Adding synchronization markers](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.19_Adding_synchronization_markers.md>) —— Introduced in SmarTest 7.1.2
- [Removing synchronization markers](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.20_Removing_synchronization_markers.md>) —— Introduced in SmarTest 7.1.2
- [Demodulation (Signal Analyzer)](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.02.05.05.09_Demodulation__Signal_Analyzer.md>) —— Introduced in SmarTest 7.1.2
- [Accessing the demodulation tool](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.04.01_Accessing_the_demodulation_tool.md>) —— Introduced in SmarTest 7.1.2
- [Specifying waveform and standard](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.04.02_Specifying_waveform_and_standard.md>) —— Introduced in SmarTest 7.1.2
- [Editing input parameters](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.04.03_Editing_input_parameters.md>) —— Introduced in SmarTest 7.1.2
- [Executing demodulation](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.04.04_Executing_demodulation.md>) —— Introduced in SmarTest 7.1.2
- [Verifying results](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.04.05_Verifying_results.md>) —— Introduced in SmarTest 7.1.2
- [Configuring parameter list](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.04.06_Configuring_parameter_list.md>) —— Introduced in SmarTest 7.1.2
- [Demodulation in the Signal Analyzer](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.04_Demodulation_in_the_Signal_Analyzer.md>) —— Introduced in SmarTest 7.1.2
- [Changing Compatibility Options](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.07_Changing_Compatibility_Options.md>) —— Introduced in SmarTest 7.1.2
- [DRLTestConditionAttr](<02_System_reference/02.10_Data_Logging/02.10.01.04.02.86_DRLTestConditionAttr.md>) —— Introduced in SmarTest 7.1.2
- [DRLTestCondition](<02_System_reference/02.10_Data_Logging/02.10.01.04.02.87_DRLTestCondition.md>) —— Introduced in SmarTest 7.1.2
- [TestConditionAttrType](<02_System_reference/02.10_Data_Logging/02.10.01.06.05.54_TestConditionAttrType.md>) —— Introduced in SmarTest 7.1.2
- [Prerequisites](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.01_Prerequisites.md>) —— Introduced in SmarTest 7.1.2
- [Understanding the terms of protocol based testing](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.02_Understanding_the_terms_of_protocol_based_testing.md>) —— Introduced in SmarTest 7.1.2
- [Protocol based terms put into perspective](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.03_Protocol_based_terms_put_into_perspective.md>) —— Introduced in SmarTest 7.1.2
- [Modifying an existing protocol definition](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.04.03_Modifying_an_existing_protocol_definition.md>) —— Introduced in SmarTest 7.1.2
- [Example: Defining a MDIO protocol](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.04.05_Example__Defining_a_MDIO_protocol.md>) —— Introduced in SmarTest 7.1.2
- [Defining a protocol](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.04_Defining_a_protocol.md>) —— Introduced in SmarTest 7.1.2
- [List of transaction based protocol test APIs](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05.01_List_of_transaction_based_protocol_test_APIs.md>) —— Introduced in SmarTest 7.1.2
- [Example: Writing a protocol based UTM without using protocol wrapper](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05.02.01_Example__Writing_a_protocol_based_UTM_without_using_protocol_wrapper.md>) —— Introduced in SmarTest 7.1.2
- [Implementing protocol based tests to the test program](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05.02_Implementing_protocol_based_tests_to_the_test_program.md>) —— Introduced in SmarTest 7.1.2
- [Example: Writing a protocol based UTM using protocol wrapper](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05.03.01_Example__Writing_a_protocol_based_UTM_using_protocol_wrapper.md>) —— Introduced in SmarTest 7.1.2
- [Implementing protocol wrappers to the test program](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05.03_Implementing_protocol_wrappers_to_the_test_program.md>) —— Introduced in SmarTest 7.1.2
- [Adding synchronization markers](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05.04.01_Adding_synchronization_markers.md>) —— Introduced in SmarTest 7.1.2
- [Removing synchronization markers](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05.04.02_Removing_synchronization_markers.md>) —— Introduced in SmarTest 7.1.2
- [Example: Using sync markers within test methods](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05.04.03_Example__Using_sync_markers_within_test_methods.md>) —— Introduced in SmarTest 7.1.2
- [Synchronizing transactions to vectors](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05.04_Synchronizing_transactions_to_vectors.md>) —— Introduced in SmarTest 7.1.2
- [Using transaction based protocol test APIs in UTMs](<03_Use_cases_and_application_papers/03.11_How_to_do_transaction_based_protocol_testing/03.11.01.05_Using_transaction_based_protocol_test_APIs_in_UTMs.md>) —— Introduced in SmarTest 7.1.2
- [Test number conversion procedure](<03_Use_cases_and_application_papers/03.12_SmarTest_Program_Migration_Framework/03.12.09.01_Test_number_conversion_procedure.md>) —— Introduced in SmarTest 7.1.2
- [Test number conversion rules](<03_Use_cases_and_application_papers/03.12_SmarTest_Program_Migration_Framework/03.12.09.02_Test_number_conversion_rules.md>) —— Introduced in SmarTest 7.1.2
- [Test number conversion use cases](<03_Use_cases_and_application_papers/03.12_SmarTest_Program_Migration_Framework/03.12.09.03_Test_number_conversion_use_cases.md>) —— Introduced in SmarTest 7.1.2
- [Migrating test number](<03_Use_cases_and_application_papers/03.12_SmarTest_Program_Migration_Framework/03.12.09_Migrating_test_number.md>) —— Introduced in SmarTest 7.1.2


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 90 条**，涉及 **84 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。

## ⚠️ 本页出现的语料编码损坏

本页条目里有 **4 处**「`鈥`」字样：`鈥慴`（4 处）。

**这是 raw 自带的编码损坏，不是本页打错、也不是转录出错。**损坏的成因与对照表见 [[pogo-block-compatibility]]，同族实例见 [[dps128-dps64-cards]] 与 [[xps256-programming-dps-operating-mode]]。

**本页照原样转录**（raw 一个字节不动，schema §1.1）。**代价是：拿修好的字去 raw 里搜是搜不到的**，要搜坏掉的那个形态。
