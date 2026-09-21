---
type: version
title: MTP 3.0.3 — 版本页
tags: [version, mtp]
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.01.09.07.01_Counted_match_loops.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.07_Creating_a_pattern_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.03.01_Parameters_for_the_ExecutionEngine_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.03_Address_Training_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.04_Address_Bus_Inversion_Training_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.05_Clock_Training_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.01_SourceSync_fast_mode.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.02_SourceSync_standard_mode.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05_Parameters_for_multistrobe_test_methods.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.02_Redundancy_analysis_on_multiple_test_suites.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.03.01_Redundancy_analysis_configuration_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.04_Using_RaServer_for_offline_analysis.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.05_Bit_fail_map_list_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.06_Physical_address-based_list_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01_Setting_up_and_performing_a_redundancy_analysis.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.02_Control_file_for_the_Successive_algorithm.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.03.01_Compiling_the_DUT_representation_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.03_DUT_representation_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.04_Output_of_the_redundancy_analysis_algorithm.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.05_Writing_a_custom_redundancy_analysis_algorithm.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03_Redundancy_analysis.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.05_Fail_bit_count.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.01_Device_access_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.08.01_DC_event_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.06_Counted_match_loops.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.09.01_Setting_up_cyclic_redundancy_checks.md
  # 本页共涉及 39 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# MTP 3.0.3

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（35 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `MTP 3.0.3:` 前缀，**那是原文的一部分，没有去掉**。

- [Counted match loops](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.01.09.07.01_Counted_match_loops.md>) —— MTP 3.0.3: Additional restrictions introduced for using match loops together with other features.
- [Creating a pattern file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.07_Creating_a_pattern_file.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) :countedMatchPadding: keyword changed to :countedMatchPad:
- [Parameters for the ExecutionEngine test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.03.01_Parameters_for_the_ExecutionEngine_test_method.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0.) ExecutionEngine supports redundancy repair analysis.
- [Parameters for the ExecutionEngine test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.03.01_Parameters_for_the_ExecutionEngine_test_method.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0.) Added bitmap_format parameter.
- [Address Training test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.03_Address_Training_test_method.md>) —— MTP 3.0.3: Added EmbeddedTraining option to the TrainingAlgorithm parameter and Yes (Embedded) option to the EdgeCentering parameter
- [Address Bus Inversion Training test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.04_Address_Bus_Inversion_Training_test_method.md>) —— MTP 3.0.3: Added EmbeddedTraining option to the TrainingAlgorithm parameter and Yes (Embedded) option to the EdgeCentering parameter
- [Clock Training test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.05_Clock_Training_test_method.md>) —— MTP 3.0.3: Added EmbeddedTraining option to the TrainingAlgorithm parameter and Yes (Embedded) option to the EdgeCentering parameter
- [SourceSync fast mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.01_SourceSync_fast_mode.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Added Sharing Config File parameter.
- [SourceSync standard mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.02_SourceSync_standard_mode.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Added Sharing Config File parameter.
- [Parameters for multistrobe test methods](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05_Parameters_for_multistrobe_test_methods.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Added Sharing ConfigFile parameter
- [Sharing configuration file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Added rapid source sync buffer pins section
- [Redundancy analysis configuration file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.03.01_Redundancy_analysis_configuration_file.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Added environment_info, result_root_path, ra_counting_enabling, ra_algorithm_enabling, and ra_counting_results_leverage parameters.
- [Redundancy analysis configuration file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.03.01_Redundancy_analysis_configuration_file.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Both XML and text files can now be used for both online and offline analysis.
- [Setting up and performing a redundancy analysis](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01_Setting_up_and_performing_a_redundancy_analysis.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Redundancy analysis is now performed via the ExecutionEngine test method.
- [Control file for the Successive algorithm](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.02_Control_file_for_the_Successive_algorithm.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Added output_level, count_limit_per_segment, and must_repair_iteration_number parameters.
- [Compiling the DUT representation file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.03.01_Compiling_the_DUT_representation_file.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Libraries compiled with MTP 2.x require recompilation
- [DUT representation file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.03_DUT_representation_file.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Libraries compiled with MTP 2.x require recompilation
- [Output of the redundancy analysis algorithm](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.04_Output_of_the_redundancy_analysis_algorithm.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Change to the naming of result files
- [Writing a custom redundancy analysis algorithm](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.02.05_Writing_a_custom_redundancy_analysis_algorithm.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) The cc_ra.sh script can be used to recompile legacy algorithms.
- [Redundancy analysis](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03_Redundancy_analysis.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Redundancy analysis is now performed via the ExecutionEngine test method.
- [APG pattern file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) :countedMatchPadding: keyword changed to :countedMatchPad:
- [APG pattern file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) :crc: and :dbi: keywords are now available in both MTP on HSM and MTP on SOC
- [APG pattern file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) :countedMatchPadding: keyword changed to :countedMatchPad:
- [Device access file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.01_Device_access_file_syntax.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) :countedMatchPadding: keyword changed to :countedMatchPad:
- [Macros and functions in device accesses](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) crc and dbi macros are now available in both MTP on HSM and MTP on SOC
- [DC event file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.08.01_DC_event_file_syntax.md>) —— MTP 3.0.3: Buses can be specified in the :pinlist: column.
- [DC event file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.08.01_DC_event_file_syntax.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) PMU type DC events are now available in both MTP on HSM and MTP on SOC
- [Counted match loops](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.06_Counted_match_loops.md>) —— MTP 3.0.3: Additional restrictions introduced for using match loops together with other features.
- [Setting up cyclic redundancy checks](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.09.01_Setting_up_cyclic_redundancy_checks.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Cyclic redundancy checks are now available in both MTP on HSM and MTP on SOC
- [Cyclic redundancy checks](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.09_Cyclic_redundancy_checks.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) cyclic redundancy checks are now available in both MTP on HSM and MTP on SOC
- [Setting up dynamic bus inversion](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.10.01_Setting_up_dynamic_bus_inversion.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Dynamic bus inversion is now available in both MTP on HSM and MTP on SOC
- [Dynamic bus inversion](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.10_Dynamic_bus_inversion.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Dynamic bus inversion is now available in both MTP on HSM and MTP on SOC
- [Maintenance operations](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) The sequencer mode is now available in both MTP on HSM and MTP on SOC
- [Specifying DC event details](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13.01.01_Specifying_DC_event_details.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) PMU type DC events are now supported in both MTP on HSM and MTP on SOC
- [Setting up a DC event](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13.01_Setting_up_a_DC_event.md>) —— MTP 3.0.3: (MTP on SOC 103.0.0) Controlling PMUs is now supported in both MTP on HSM and MTP on SOC


## 这一版新引入（8 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Redundancy analysis on multiple test suites](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.02_Redundancy_analysis_on_multiple_test_suites.md>) —— Introduced in MTP 3.0.3
- [Using RaServer for offline analysis](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.04_Using_RaServer_for_offline_analysis.md>) —— Introduced in MTP 3.0.3
- [Bit fail map list file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.05_Bit_fail_map_list_file.md>) —— Introduced in MTP 3.0.3
- [Physical address-based list file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.03.01.06_Physical_address-based_list_file.md>) —— Introduced in MTP 3.0.3
- [Fail bit count](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.07.05_Fail_bit_count.md>) —— Introduced in MTP 3.0.3
- [Using DPS Sharing Diagnostic](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.07.01_Using_DPS_Sharing_Diagnostic.md>) —— Introduced in MTP 3.0.3
- [DPS Sharing Diagnostic test scopes](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.07.02_DPS_Sharing_Diagnostic_test_scopes.md>) —— Introduced in MTP 3.0.3
- [DPS Sharing Diagnostic](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.07_DPS_Sharing_Diagnostic.md>) —— Introduced in MTP 3.0.3


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 43 条**，涉及 **39 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
