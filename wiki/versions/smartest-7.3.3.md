---
type: version
title: SmarTest 7.3.3 — 版本页
tags: [version, smartest]
related: []
sources:
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.02.04_SmarTest_environment_variables.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.02.01_DPS128___DPS64_capacitor_requirements.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.05_ETC_section.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.33_CSAS__-__Channel_Slot_Accumulated_Status.md
  - 02_System_reference/02.06_Command_Reference/02.06.10.02.01_CSAS__-__Channel_Slot_Accumulated_Status.md
  - 02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.07_AWG_Trig.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.01_CCTaddPAResultId.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.10_CCTgetDCResults.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.19_CCTgetPAResultId.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.25_CCTMultiportSync.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.33_CCTsetExecMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.144_PH_DOWNLOAD_PROFILE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.145_PH_QUERY_PROFILE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.146_PH_SELECT_PROFILE_BY_SITE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.15_CCT_TEST.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27.01_SMC_PIN_ERROR_MAP.getFirstFailingTesterCycles.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27.02_SMC_PIN_ERROR_MAP.getFirstFailingXmodeCycles.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27.03_SMC_PIN_ERROR_MAP.getGlobalErrorCount.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.28.01_SMC_PIN_ERROR_MAP_ACCESSOR.getSmcPinErrorMap.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.28_SMC_PIN_ERROR_MAP_ACCESSOR.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.31_DGT_Trig.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.09.04.03.01_Configuring_general_parameters.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.08.01_2nd_level_protocol_wrapper_tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.10.11.01_Generating_protocol_wrappers_using_the_2nd_level_protocol_wrapper_tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25.03.04.01_Colors_in_shmoo_plots.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.05.02.01_General_information_about_the_Advantest_GPIB_handler_driver.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.05.02.02_Default_GPIB_configuration.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.05.02.03_GPIB_communication_flow_for_Advantest_handlers.md
  # 本页共涉及 46 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.3.3

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（17 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.3.3:` 前缀，**那是原文的一部分，没有去掉**。

- [SmarTest environment variables](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.02.04_SmarTest_environment_variables.md>) —— SmarTest 7.3.3: New workstation Z640
- [ETC section](<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.05_ETC_section.md>) —— SmarTest 7.3.3: Added parameter info for "output_at_rf_connector".
- [PSAS? - (Power Supply Accumulated Status)](<02_System_reference/02.06_Command_Reference/02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.md>) —— SmarTest 7.3.3: New extra parameter "msMode".
- [CSAS? - (Channel Slot Accumulated Status)](<02_System_reference/02.06_Command_Reference/02.06.02.02.33_CSAS__-__Channel_Slot_Accumulated_Status.md>) —— SmarTest 7.3.3: New extra parameter "msMode".
- [CSAS? - (Channel Slot Accumulated Status)](<02_System_reference/02.06_Command_Reference/02.06.10.02.01_CSAS__-__Channel_Slot_Accumulated_Status.md>) —— SmarTest 7.3.3: New extra parameter "msMode".
- [PSAS? - (Power Supply Accumulated Status)](<02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.md>) —— SmarTest 7.3.3: New extra parameter "msMode".
- [CCTMultiportSync()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.25_CCTMultiportSync.md>) —— SmarTest 7.3.3: Supports multiple digital captures for different digital capture ports (DigitalCapturePort).
- [CCTsetExecMode](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.33_CCTsetExecMode.md>) —— SmarTest 7.3.3: New execution mode EXM_SMC_FUNCTIONAL_TEST.
- [CCT_TEST](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.15_CCT_TEST.md>) —— SmarTest 7.3.3: Supports Hidden_datalog_mode= 2.
- [Configuring general parameters](<02_System_reference/02.07_Test_Method_Reference/02.07.09.04.03.01_Configuring_general_parameters.md>) —— SmarTest 7.3.3: Added getPatternStoragePath() member function.
- [Colors in shmoo plots](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25.03.04.01_Colors_in_shmoo_plots.md>) —— SmarTest 7.3.3: Customized color mapping introduced
- [General information about the Advantest GPIB handler driver](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.05.02.01_General_information_about_the_Advantest_GPIB_handler_driver.md>) —— SmarTest 7.3.3: Driver enhancement to support YUSHAN handlers.
- [Default GPIB configuration](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.05.02.02_Default_GPIB_configuration.md>) —— SmarTest 7.3.3: New enhancement to support YUSHAN handlers.
- [GPIB communication flow for Advantest handlers](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.05.02.03_GPIB_communication_flow_for_Advantest_handlers.md>) —— SmarTest 7.3.3: New enhancement to support YUSHAN handlers.
- [Installing the operator console](<02_System_reference/02.09_Test_Program_Management/02.09.01.05.06.01_Installing_the_operator_console.md>) —— SmarTest 7.3.3: New system controller Z640
- [Recipe file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.01_Recipe_file.md>) —— SmarTest 7.3.3: Added force_execute attribute for the smartest element.
- [ait command line parameters](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.08.01_ait_command_line_parameters.md>) —— SmarTest 7.3.3: Added the s and F options for the -M switch.


## 这一版新引入（29 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [DPS128 / DPS64 capacitor requirements](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.02.01_DPS128___DPS64_capacitor_requirements.md>) —— Introduced in SmarTest 7.3.3
- [AWG_Trig](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.07_AWG_Trig.md>) —— Introduced in SmarTest 7.3.3
- [CCTaddPAResultId()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.01_CCTaddPAResultId.md>) —— Introduced in SmarTest 7.3.3
- [CCTgetDCResults()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.10_CCTgetDCResults.md>) —— Introduced in SmarTest 7.3.3
- [CCTgetPAResultId()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.19_CCTgetPAResultId.md>) —— Introduced in SmarTest 7.3.3
- [PH_DOWNLOAD_PROFILE()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.144_PH_DOWNLOAD_PROFILE.md>) —— Introduced in SmarTest 7.3.3
- [PH_QUERY_PROFILE()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.145_PH_QUERY_PROFILE.md>) —— Introduced in SmarTest 7.3.3
- [PH_SELECT_PROFILE_BY_SITE()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.146_PH_SELECT_PROFILE_BY_SITE.md>) —— Introduced in SmarTest 7.3.3
- [SMC_PIN_ERROR_MAP.getFirstFailingTesterCycles()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27.01_SMC_PIN_ERROR_MAP.getFirstFailingTesterCycles.md>) —— Introduced in SmarTest 7.3.3
- [SMC_PIN_ERROR_MAP.getFirstFailingXmodeCycles()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27.02_SMC_PIN_ERROR_MAP.getFirstFailingXmodeCycles.md>) —— Introduced in SmarTest 7.3.3
- [SMC_PIN_ERROR_MAP.getGlobalErrorCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27.03_SMC_PIN_ERROR_MAP.getGlobalErrorCount.md>) —— Introduced in SmarTest 7.3.3
- [SMC_PIN_ERROR_MAP_ACCESSOR.getSmcPinErrorMap()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.28.01_SMC_PIN_ERROR_MAP_ACCESSOR.getSmcPinErrorMap.md>) —— Introduced in SmarTest 7.3.3
- [SMC_PIN_ERROR_MAP_ACCESSOR](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.28_SMC_PIN_ERROR_MAP_ACCESSOR.md>) —— Introduced in SmarTest 7.3.3
- [DGT_Trig](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.31_DGT_Trig.md>) —— Introduced in SmarTest 7.3.3
- [2nd level protocol wrapper tool](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.08.01_2nd_level_protocol_wrapper_tool.md>) —— Introduced in SmarTest 7.3.3
- [Generating protocol wrappers using the 2nd level protocol wrapper tool](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.10.11.01_Generating_protocol_wrappers_using_the_2nd_level_protocol_wrapper_tool.md>) —— Introduced in SmarTest 7.3.3
- [Generating per-pin test numbers](<02_System_reference/02.10_Data_Logging/02.10.01.08.04_Generating_per-pin_test_numbers.md>) —— Introduced in SmarTest 7.3.3
- [General risks](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.05_General_risks.md>) —— Introduced in SmarTest 7.3.3
- [Check pin setups](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.07_Check_pin_setups.md>) —— Introduced in SmarTest 7.3.3
- [Check level setups](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.09_Check_level_setups.md>) —— Introduced in SmarTest 7.3.3
- [Check timing setups](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.10_Check_timing_setups.md>) —— Introduced in SmarTest 7.3.3
- [Check vector setups](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.11_Check_vector_setups.md>) —— Introduced in SmarTest 7.3.3
- [Check test table setups](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.12_Check_test_table_setups.md>) —— Introduced in SmarTest 7.3.3
- [Check testflow setups](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.13_Check_testflow_setups.md>) —— Introduced in SmarTest 7.3.3
- [Check test method](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.14_Check_test_method.md>) —— Introduced in SmarTest 7.3.3
- [Check warning/error of flow execution](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.15_Check_warning_error_of_flow_execution.md>) —— Introduced in SmarTest 7.3.3
- [Central profile](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.12.01_Central_profile.md>) —— Introduced in SmarTest 7.3.3
- [Module profile](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.12.02_Module_profile.md>) —— Introduced in SmarTest 7.3.3
- [TP360 Profile](<03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.12_TP360_Profile.md>) —— Introduced in SmarTest 7.3.3


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 46 条**，涉及 **46 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
