---
type: version
title: SmarTest 7.0.4 — 版本页
tags: [version, smartest]
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.02_Customizable_Scripts.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.01_The_System_.lic_license_files.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.157_PPMU_MEASURE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.273_Wave.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50_DPS_TASK.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03.01_Communication.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03.02_Components.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03_How_the_prober_handler_driver_functions.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.01_Communication_between_Equipment_and_System_controller.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.02.01_Driver_Structure.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.05.05.04_Parameter__interface_type.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.05.05.05_Parameter__symbolic_interface_name.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.04_Conventions_for_GPIB_LAN_communication.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.03_Conventions_for_GPIB_LAN_communication.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.01.01_About_SmarTest_Program_Manager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.01.02.01_SmarTest_Program_Manager_concepts.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.01.02.02_Using_STPM_with_test_program_templates.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.01.02.03_Test_program_template.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.01.02_SmarTest_Program_Manager_operating_principles.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.01.03_Installing_SmarTest_Program_Manager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.02.01_Creating_and_editing_an_STPM_control_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.02.02_Optimizing_SmarTest_Program_Manager_performance.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.02_Using_SmarTest_Program_Manager.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.04_write_tp.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.05_add_test.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.07_add_test_to_burst.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.09_remove_test.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.10_replace_test.md
  # 本页共涉及 71 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.0.4

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（9 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.0.4:` 前缀，**那是原文的一部分，没有去掉**。

- [Customizable Scripts](<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.02_Customizable_Scripts.md>) —— SmarTest 7.0.4: Script license_checkout_failure introduced
- [The System .lic license files](<02_System_reference/02.04_Model_File_and_Licensing/02.04.05.01_The_System_.lic_license_files.md>) —— SmarTest 7.0.4: Script license_checkout_failure introduced
- [PPMU_MEASURE](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.157_PPMU_MEASURE.md>) —— SmarTest 7.0.4: New member function wait().
- [Wave](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.273_Wave.md>) —— SmarTest 7.0.4: Enhanced initRealImag() and initMagnitudePhase().
- [DPS_TASK](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50_DPS_TASK.md>) —— SmarTest 7.0.4: New member function primaryActivation().
- [Logging formats and data types](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06.01_Logging_formats_and_data_types.md>) —— SmarTest 7.0.4: Logging memory tests events is available only in MTP on HSM.
- [Configuring data logging for memory tests](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06.02_Configuring_data_logging_for_memory_tests.md>) —— SmarTest 7.0.4: Logging memory tests events is available only in MTP on HSM.
- [Memory test data log event structure](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06.03_Memory_test_data_log_event_structure.md>) —— SmarTest 7.0.4: Logging memory tests events is available only in MTP on HSM.
- [Logging memory tests](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06_Logging_memory_tests.md>) —— SmarTest 7.0.4: Logging memory test evens is available only in MTP on HSM.


## 这一版新引入（62 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Communication](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03.01_Communication.md>) —— Introduced in SmarTest 7.0.4
- [Components](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03.02_Components.md>) —— Introduced in SmarTest 7.0.4
- [How the prober/handler driver functions](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.01.03_How_the_prober_handler_driver_functions.md>) —— Introduced in SmarTest 7.0.4
- [Communication between Equipment and System controller](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.01_Communication_between_Equipment_and_System_controller.md>) —— Introduced in SmarTest 7.0.4
- [Driver Structure](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.02.01_Driver_Structure.md>) —— Introduced in SmarTest 7.0.4
- [Parameter: interface_type](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.05.05.04_Parameter__interface_type.md>) —— Introduced in SmarTest 7.0.4
- [Parameter: symbolic_interface_name](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.05.05.05_Parameter__symbolic_interface_name.md>) —— Introduced in SmarTest 7.0.4
- [Conventions for GPIB/LAN communication](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.04_Conventions_for_GPIB_LAN_communication.md>) —— Introduced in SmarTest 7.0.4
- [Conventions for GPIB/LAN communication](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.02.03_Conventions_for_GPIB_LAN_communication.md>) —— Introduced in SmarTest 7.0.4
- [About SmarTest Program Manager](<02_System_reference/02.09_Test_Program_Management/02.09.02.01.01_About_SmarTest_Program_Manager.md>) —— Introduced in SmarTest 7.0.4
- [SmarTest Program Manager concepts](<02_System_reference/02.09_Test_Program_Management/02.09.02.01.02.01_SmarTest_Program_Manager_concepts.md>) —— Introduced in SmarTest 7.0.4
- [Using STPM with test program templates](<02_System_reference/02.09_Test_Program_Management/02.09.02.01.02.02_Using_STPM_with_test_program_templates.md>) —— Introduced in SmarTest 7.0.4
- [Test program template](<02_System_reference/02.09_Test_Program_Management/02.09.02.01.02.03_Test_program_template.md>) —— Introduced in SmarTest 7.0.4
- [SmarTest Program Manager operating principles](<02_System_reference/02.09_Test_Program_Management/02.09.02.01.02_SmarTest_Program_Manager_operating_principles.md>) —— Introduced in SmarTest 7.0.4
- [Installing SmarTest Program Manager](<02_System_reference/02.09_Test_Program_Management/02.09.02.01.03_Installing_SmarTest_Program_Manager.md>) —— Introduced in SmarTest 7.0.4
- [Creating and editing an STPM control file](<02_System_reference/02.09_Test_Program_Management/02.09.02.02.01_Creating_and_editing_an_STPM_control_file.md>) —— Introduced in SmarTest 7.0.4
- [Optimizing SmarTest Program Manager performance](<02_System_reference/02.09_Test_Program_Management/02.09.02.02.02_Optimizing_SmarTest_Program_Manager_performance.md>) —— Introduced in SmarTest 7.0.4
- [Using SmarTest Program Manager](<02_System_reference/02.09_Test_Program_Management/02.09.02.02_Using_SmarTest_Program_Manager.md>) —— Introduced in SmarTest 7.0.4
- [Structure of an STPM control file](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.md>) —— Introduced in SmarTest 7.0.4
- [File and parameter settings](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.md>) —— Introduced in SmarTest 7.0.4
- [write_tp](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.04_write_tp.md>) —— Introduced in SmarTest 7.0.4
- [add_test](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.05_add_test.md>) —— Introduced in SmarTest 7.0.4
- [add_test_to_burst](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.07_add_test_to_burst.md>) —— Introduced in SmarTest 7.0.4
- [remove_test](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.09_remove_test.md>) —— Introduced in SmarTest 7.0.4
- [replace_test](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.10_replace_test.md>) —— Introduced in SmarTest 7.0.4
- [tpt_generate_template](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.14_tpt_generate_template.md>) —— Introduced in SmarTest 7.0.4
- [tpt_import_from_device](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md>) —— Introduced in SmarTest 7.0.4
- [tpt_generate_device_dir](<02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md>) —— Introduced in SmarTest 7.0.4
- [STPM control file](<02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.md>) —— Introduced in SmarTest 7.0.4
- [STPM merge rules file syntax](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.01_STPM_merge_rules_file_syntax.md>) —— Introduced in SmarTest 7.0.4
- [new_digital_pin](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.02_new_digital_pin.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_digital_pin_no](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.03_overwrite_digital_pin_no.md>) —— Introduced in SmarTest 7.0.4
- [merge_digital_pin_dir](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.04_merge_digital_pin_dir.md>) —— Introduced in SmarTest 7.0.4
- [new_dps_pin](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.05_new_dps_pin.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_dps_pin_polarity](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.06_overwrite_dps_pin_polarity.md>) —— Introduced in SmarTest 7.0.4
- [new_pin_group](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.07_new_pin_group.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_pin_group](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.08_overwrite_pin_group.md>) —— Introduced in SmarTest 7.0.4
- [new_port](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.10_new_port.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_port](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.11_overwrite_port.md>) —— Introduced in SmarTest 7.0.4
- [new_site](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.12_new_site.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_channel](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.13_overwrite_channel.md>) —— Introduced in SmarTest 7.0.4
- [new_timing_equation_set](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.14_new_timing_equation_set.md>) —— Introduced in SmarTest 7.0.4
- [new_waveform](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.15_new_waveform.md>) —— Introduced in SmarTest 7.0.4
- [modify_waveform_index](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.16_modify_waveform_index.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_statemap](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.17_overwrite_statemap.md>) —— Introduced in SmarTest 7.0.4
- [new_level_resource](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.18_new_level_resource.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_level_resource](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.19_overwrite_level_resource.md>) —— Introduced in SmarTest 7.0.4
- [new_level_equation_set](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.20_new_level_equation_set.md>) —— Introduced in SmarTest 7.0.4
- [new_level_set](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.21_new_level_set.md>) —— Introduced in SmarTest 7.0.4
- [new_ac_specset](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.22_new_ac_specset.md>) —— Introduced in SmarTest 7.0.4
- [new_dc_specset](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.23_new_dc_specset.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_ac_spec_typ](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.24_overwrite_ac_spec_typ.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_ac_spec_minmax](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.25_overwrite_ac_spec_minmax.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_dc_spec_typ](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.26_overwrite_dc_spec_typ.md>) —— Introduced in SmarTest 7.0.4
- [overwrite_dc_spec_minmax](<02_System_reference/02.09_Test_Program_Management/02.09.02.04.27_overwrite_dc_spec_minmax.md>) —— Introduced in SmarTest 7.0.4
- [STPM merge rules file](<02_System_reference/02.09_Test_Program_Management/02.09.02.04_STPM_merge_rules_file.md>) —— Introduced in SmarTest 7.0.4
- [Test suite table of a TPT](<02_System_reference/02.09_Test_Program_Management/02.09.02.05.01_Test_suite_table_of_a_TPT.md>) —— Introduced in SmarTest 7.0.4
- [Bin table of a TPT](<02_System_reference/02.09_Test_Program_Management/02.09.02.05.02_Bin_table_of_a_TPT.md>) —— Introduced in SmarTest 7.0.4
- [Test flag table of a TPT](<02_System_reference/02.09_Test_Program_Management/02.09.02.05.05_Test_flag_table_of_a_TPT.md>) —— Introduced in SmarTest 7.0.4
- [OpenOffice spreadsheet for editing the CSV files](<02_System_reference/02.09_Test_Program_Management/02.09.02.05.07_OpenOffice_spreadsheet_for_editing_the_CSV_files.md>) —— Introduced in SmarTest 7.0.4
- [Test program template files](<02_System_reference/02.09_Test_Program_Management/02.09.02.05_Test_program_template_files.md>) —— Introduced in SmarTest 7.0.4
- [STPM command line options](<02_System_reference/02.09_Test_Program_Management/02.09.02.06_STPM_command_line_options.md>) —— Introduced in SmarTest 7.0.4


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 71 条**，涉及 **71 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
