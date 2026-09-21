---
type: version
title: SmarTest 7.2.3 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.05_PMU_operating_mode_of_DC_Scale_cards.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.193_PSLC__PSLC__-__Power_Supply_Load_Capacitance.md
  - 02_System_reference/02.06_Command_Reference/02.06.08.01.04.01_Defining_connect_disconnect_sequences.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.12.01.03_Doing_retest_with_the_concurrent_test_framework.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.34_CCTsetMaxRetestCount.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.36_CCTsetRetest.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.168_PROB_HND_CALL.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.198_SCATTER_LOG.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.44_SMC_SYNCHRONIZE_WITHOUT_BINNING.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.02_Excluding_data_from_evaluation.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.03_Displaying_test_results_in_analysis_views.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.02_Wafer_summary_tab.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.03_Device_summary_tab.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.01_Raw_data_views.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.02_Stream_data_view.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.02_Load_capacitance_connected_to_the_DC_Scale_DPS128_DPS64.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03.01_Communication.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03.02_Components.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03_How_the_prober_handler_driver_functions.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.01_Communication_between_Equipment_and_System_controller.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.02.01_Driver_Structure.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.04.01_Parameters_for_interface_identification.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.04.02_Parameters_for_LAN_communication.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.04_Debugging_a_LAN_driver_configuration.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.05.05.04_Parameter__interface_type.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.05.05.05_Parameter__symbolic_interface_name.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.04_Conventions_for_GPIB_LAN_communication.md
  # 本页共涉及 63 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.2.3

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（67 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.2.3:` 前缀，**那是原文的一部分，没有去掉**。

- [PMU operating mode of DC Scale cards](<02_System_reference/02.05_Test_Head_Cards/02.05.05.05_PMU_operating_mode_of_DC_Scale_cards.md>) —— SmarTest 7.2.3: SmarTest startup behavior changed
- [PSLC, PSLC? - (Power Supply Load Capacitance)](<02_System_reference/02.06_Command_Reference/02.06.02.02.193_PSLC__PSLC__-__Power_Supply_Load_Capacitance.md>) —— SmarTest 7.2.3: Support of DCS_capacitance parameter starts with 7.2.3 patch version
- [Defining connect/disconnect sequences](<02_System_reference/02.06_Command_Reference/02.06.08.01.04.01_Defining_connect_disconnect_sequences.md>) —— SmarTest 7.2.3: SmarTest startup behavior changed
- [Doing retest with the concurrent test framework](<02_System_reference/02.07_Test_Method_Reference/02.07.02.12.01.03_Doing_retest_with_the_concurrent_test_framework.md>) —— SmarTest 7.2.3: Supports the retest of test suite using SMC.
- [Doing retest with the concurrent test framework](<02_System_reference/02.07_Test_Method_Reference/02.07.02.12.01.03_Doing_retest_with_the_concurrent_test_framework.md>) —— SmarTest 7.2.3: Supports specifying the maximum execution times of retest.
- [CCTsetRetest()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.36_CCTsetRetest.md>) —— SmarTest 7.2.3: New parameter enableSMC.
- [SCATTER_LOG](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.198_SCATTER_LOG.md>) —— SmarTest 7.2.3: In patch 1, supports the constructor syntax SCATTER_LOG(const ARRAY_LL & xseries, const ARRAY_LL & yseries).
- [SCATTER_LOG](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.198_SCATTER_LOG.md>) —— SmarTest 7.2.3: In patch 1, supports the syntax SCATTER_LOG & xAxis(const ARRAY_LL & xseries).
- [SCATTER_LOG](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.198_SCATTER_LOG.md>) —— SmarTest 7.2.3: In patch 1, supports the syntax SCATTER_LOG & yAxis(const ARRAY_LL & yseries).
- [SMC_SYNCHRONIZE_WITHOUT_BINNING()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.44_SMC_SYNCHRONIZE_WITHOUT_BINNING.md>) —— SmarTest 7.2.3: Introduced in patch 8.
- [SPMU_PIN_TASK.loadCap()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.md>) —— SmarTest 7.2.3: Support of load capacitance parameter with 7.2.3.2 patch.
- [SPMU_PIN_TASK.mode()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md>) —— SmarTest 7.2.3: Support of IFVM_UNGANGED parameter with 7.2.3.1
- [Excluding data from evaluation](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.02_Excluding_data_from_evaluation.md>) —— SmarTest 7.2.3: The Include and Exclude commands were converted into into submenus.
- [Displaying test results in analysis views](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.03_Displaying_test_results_in_analysis_views.md>) —— SmarTest 7.2.3: Added option to enable or disable dynamic updates for system data log stream charts.
- [Test summary tab](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.md>) —— SmarTest 7.2.3: Added option to enable or disable dynamic updates for system data log stream charts.
- [Wafer summary tab](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.02_Wafer_summary_tab.md>) —— SmarTest 7.2.3: Added shortcut menu command to enable or disable dynamic updates for system data log stream charts.
- [Device summary tab](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.03_Device_summary_tab.md>) —— SmarTest 7.2.3: Added Part ID and Part Txt columns.
- [Raw data views](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.01_Raw_data_views.md>) —— SmarTest 7.2.3: Added Part ID and Part Txt columns.
- [Raw data views](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.01_Raw_data_views.md>) —— SmarTest 7.2.3: The Include and Exclude commands were converted into submenus.
- [Stream data view](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.02_Stream_data_view.md>) —— SmarTest 7.2.3: Added Part ID and Part Txt columns.
- [Load capacitance connected to the DC Scale DPS128/DPS64](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.02_Load_capacitance_connected_to_the_DC_Scale_DPS128_DPS64.md>) —— SmarTest 7.2.3: Support of load capacitance parameter with 7.2.3.2 patch
- [Communication](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03.01_Communication.md>) —— SmarTest 7.2.3: LAN supported
- [Components](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03.02_Components.md>) —— SmarTest 7.2.3: LAN supported
- [How the prober/handler driver functions](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03_How_the_prober_handler_driver_functions.md>) —— SmarTest 7.2.3: LAN supported
- [Communication between Equipment and System controller](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.01_Communication_between_Equipment_and_System_controller.md>) —— SmarTest 7.2.3: LAN supported
- [Driver Structure](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.02.01_Driver_Structure.md>) —— SmarTest 7.2.3: Removed RS-232 support
- [Driver Structure](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.02.01_Driver_Structure.md>) —— SmarTest 7.2.3: LAN supported
- [Parameters for interface identification](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.04.01_Parameters_for_interface_identification.md>) —— SmarTest 7.2.3: Changed in Patch 2
- [Parameters for LAN communication](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.04.02_Parameters_for_LAN_communication.md>) —— SmarTest 7.2.3: Changed in Patch 2
- [Debugging a LAN driver configuration](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.04_Debugging_a_LAN_driver_configuration.md>) —— SmarTest 7.2.3: Changed in Patch 2
- [Parameter: interface_type](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.05.05.04_Parameter__interface_type.md>) —— SmarTest 7.2.3: No support for RS-232
- [Parameter: interface_type](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.05.05.04_Parameter__interface_type.md>) —— SmarTest 7.2.3: LAN supported
- [Parameter: symbolic_interface_name](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.05.05.05_Parameter__symbolic_interface_name.md>) —— SmarTest 7.2.3: LAN supported
- [Conventions for GPIB/LAN communication](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.04_Conventions_for_GPIB_LAN_communication.md>) —— SmarTest 7.2.3: LAN supported
- [Conventions for GPIB/LAN communication](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.03_Conventions_for_GPIB_LAN_communication.md>) —— SmarTest 7.2.3: LAN supported
- [Supported probers](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.04.01.02_Supported_probers.md>) —— SmarTest 7.2.3: Support the WDF 12DP/F12 model.
- [Configuration at the prober](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.06.02.01_Configuration_at_the_prober.md>) —— SmarTest 7.2.3: (Patch 2) Removed ignored prober SRQ 0x59
- [Configuration at the prober](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.06.02.01_Configuration_at_the_prober.md>) —— SmarTest 7.2.3: (Patch 2) Removed STB code setting 71
- [Configuration at the prober](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.06.02.01_Configuration_at_the_prober.md>) —— SmarTest 7.2.3: (Patch 2) Removed STB code setting 76
- [Configuration at the prober](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.06.02.01_Configuration_at_the_prober.md>) —— SmarTest 7.2.3: (Patch 2) Removed STB code setting 85
- [Configuration at the prober](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.06.02.01_Configuration_at_the_prober.md>) —— SmarTest 7.2.3: (Patch 2) Removed STB code setting 87
- [Configuration at the prober](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.06.02.01_Configuration_at_the_prober.md>) —— SmarTest 7.2.3: (Patch 2) Removed STB code setting 118
- [Configuration at the prober](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.06.02.01_Configuration_at_the_prober.md>) —— SmarTest 7.2.3: (Patch 2) New STB code setting 66
- [Configuration at the prober](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.06.02.01_Configuration_at_the_prober.md>) —— SmarTest 7.2.3: (Patch 2) New STB code setting 101
- [GPIB communication flow for TSK probers](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.06.03_GPIB_communication_flow_for_TSK_probers.md>) —— SmarTest 7.2.3: (Patch 2) Removed ignored prober SRQ 0x59.
- [Recipe file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.01_Recipe_file.md>) —— SmarTest 7.2.3: Supports passing arguments to the script in TCCT 1.5.
- [Recipe file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.01_Recipe_file.md>) —— SmarTest 7.2.3: Supports relative file path for testflow in TCCT 1.5
- [Recipe file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.01_Recipe_file.md>) —— SmarTest 7.2.3: Supports executing a test suite after testflow loaded in a specific state in TCCT 1.5
- [Recipe file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.01_Recipe_file.md>) —— SmarTest 7.2.3: Supports starting SmarTest in TCCT 1.5
- [Lot configuration file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.04_Lot_configuration_file.md>) —— SmarTest 7.2.3: Added the Device Information dialog in TCCT 1.5
- [Production configuration file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.05_Production_configuration_file.md>) —— SmarTest 7.2.3: New property env to set the SmarTest environment values in TCCT 1.5
- [Production configuration file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.05_Production_configuration_file.md>) —— SmarTest 7.2.3: New property ui_config_file to specify the UI configuration file in TCCT 1.5
- [Production configuration file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.05_Production_configuration_file.md>) —— SmarTest 7.2.3: New property break_device_lock to control the pop-up of the break device lock dialog in TCCT 1.5.
- [Widgets of TCCT](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.06.01_Widgets_of_TCCT.md>) —— SmarTest 7.2.3: Changed in TCCT 1.5
- [TCCT UI configuration file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.06_TCCT_UI_configuration_file.md>) —— SmarTest 7.2.3: Changed in TCCT 1.5
- [TCCT Preferences](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.07_TCCT_Preferences.md>) —— SmarTest 7.2.3: New preference page for Device Lock Notify in TCCT 1.5
- [Scan Test Record (STR)](<02_System_reference/02.10_Data_Logging/02.10.03.05.17_Scan_Test_Record__STR.md>) —— SmarTest 7.2.3: STRs are now also created when there are no failures.
- [Introduction](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.01_Introduction.md>) —— SmarTest 7.2.3: Added the STIL Reader window.
- [Installing STIL Reader](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.02_Installing_STIL_Reader.md>) —— SmarTest 7.2.3: Added stilreader_gui.
- [Converting STIL files](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.04.01_Converting_STIL_files.md>) —— SmarTest 7.2.3: Added stilreader_gui.
- [Creating a STIL Reader setup file](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.04.02_Creating_a_STIL_Reader_setup_file.md>) —— SmarTest 7.2.3: Added the STIL Reader window.
- [Using concurrent (multiport) testing](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.04.05_Using_concurrent__multiport__testing.md>) —— SmarTest 7.2.3: Added extra_pattern_comment parameter.
- [Comparing the disconnect methods](<03_Use_cases_and_application_papers/03.04_How_to_do_disconnect/03.04.01.01_Comparing_the_disconnect_methods.md>) —— SmarTest 7.2.3: SmarTest startup behavior changed
- [Effects of user-defined disconnect sequence](<03_Use_cases_and_application_papers/03.04_How_to_do_disconnect/03.04.01.03.01_Effects_of_user-defined_disconnect_sequence.md>) —— SmarTest 7.2.3: SmarTest startup behavior changed
- [User-defined disconnect sequence](<03_Use_cases_and_application_papers/03.04_How_to_do_disconnect/03.04.01.03_User-defined_disconnect_sequence.md>) —— SmarTest 7.2.3: SmarTest startup behavior changed
- [Overview of various disconnect methods](<03_Use_cases_and_application_papers/03.04_How_to_do_disconnect/03.04.01_Overview_of_various_disconnect_methods.md>) —— SmarTest 7.2.3: SmarTest startup behavior changed.
- [How to do disconnect](<03_Use_cases_and_application_papers/03.04_How_to_do_disconnect/03.04_How_to_do_disconnect.md>) —— SmarTest 7.2.3: SmarTest startup behavior changed


## 这一版新引入（21 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [CCTsetMaxRetestCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.34_CCTsetMaxRetestCount.md>) —— Introduced in SmarTest 7.2.3
- [PROB_HND_CALL()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.168_PROB_HND_CALL.md>) —— Introduced in SmarTest 7.2.3
- [SPMU_PIN_TASK.loadCap()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.md>) —— Introduced in SmarTest 7.2.3
- [Load capacitance connected to the DC Scale DPS128/DPS64](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.02_Load_capacitance_connected_to_the_DC_Scale_DPS128_DPS64.md>) —— Introduced in SmarTest 7.2.3
- [Parameters for interface identification](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.04.01_Parameters_for_interface_identification.md>) —— Introduced in SmarTest 7.2.3
- [Parameters for LAN communication](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.04.02_Parameters_for_LAN_communication.md>) —— Introduced in SmarTest 7.2.3
- [Debugging a LAN driver configuration](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.04_Debugging_a_LAN_driver_configuration.md>) —— Introduced in SmarTest 7.2.3
- [General information about the Advantest GPIB handler driver](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.05.02.01_General_information_about_the_Advantest_GPIB_handler_driver.md>) —— Introduced in SmarTest 7.2.3
- [Default GPIB configuration](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.05.02.02_Default_GPIB_configuration.md>) —— Introduced in SmarTest 7.2.3
- [GPIB communication flow for Advantest handlers](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.05.02.03_GPIB_communication_flow_for_Advantest_handlers.md>) —— Introduced in SmarTest 7.2.3
- [General information about the MCT GPIB handler driver](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.10.01.01_General_information_about_the_MCT_GPIB_handler_driver.md>) —— Introduced in SmarTest 7.2.3
- [Default driver configuration](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.10.01.02_Default_driver_configuration.md>) —— Introduced in SmarTest 7.2.3
- [GPIB communication flow for MCT handlers](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.10.01.03_GPIB_communication_flow_for_MCT_handlers.md>) —— Introduced in SmarTest 7.2.3
- [MCT Handlers](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.10_MCT_Handlers.md>) —— Introduced in SmarTest 7.2.3
- [STRIP_COMPLETED](<02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.56_STRIP_COMPLETED.md>) —— Introduced in SmarTest 7.2.3
- [STRIP_STARTED](<02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.57_STRIP_STARTED.md>) —— Introduced in SmarTest 7.2.3
- [GetTestflowInformation()](<02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.12.03_GetTestflowInformation.md>) —— Introduced in SmarTest 7.2.3
- [Configuring the layout of the Test Cell Control Tool](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.09_Configuring_the_layout_of_the_Test_Cell_Control_Tool.md>) —— Introduced in SmarTest 7.2.3
- [Widgets of TCCT](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.06.01_Widgets_of_TCCT.md>) —— Introduced in SmarTest 7.2.3
- [TCCT UI configuration file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.06_TCCT_UI_configuration_file.md>) —— Introduced in SmarTest 7.2.3
- [STIL Reader window reference](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.05.01_STIL_Reader_window_reference.md>) —— Introduced in SmarTest 7.2.3


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 88 条**，涉及 **63 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
