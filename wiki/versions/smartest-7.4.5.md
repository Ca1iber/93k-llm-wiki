---
type: version
title: SmarTest 7.4.5 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.169.05_Data_logging_profile_API_examples.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.62.01_PIN_ERROR_MAP_TEST.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.06.01.02_Setting_the_data_log_output_information_in_the_Datalog_Control_tool.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.03_Testflow_flags_for_data_logging.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.16_Exporting_a_testflow_to_a_CSV_file.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.17.08_Setting_up_the_data_log_information.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.17.10_Elements_of_the_Test_Cell_Control_Tool.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.02.06.03_Data_logging_profile_rule_syntax.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.02.08.05_Data_logging_profile_API_examples.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.02.08_Data_logging_profile_API.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.09.01_Testflow_flags_for_data_logging.md
  - 02_System_reference/02.10_Data_Logging/02.10.03.02.01_Starting_the_formatter.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.10.01_System_flags.md
  - 03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.07.01_Data_logging_settings.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.4.5

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（18 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.4.5:` 前缀，**那是原文的一部分，没有去掉**。

- [Data logging profile API examples](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.169.05_Data_logging_profile_API_examples.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [SMC_TEST()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.md>) —— SmarTest 7.4.5: Patch 1 - New syntax with parameter "testtest" defined as "const char *"
- [PIN_ERROR_MAP_TEST](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.62.01_PIN_ERROR_MAP_TEST.md>) —— SmarTest 7.4.5: Patch 4: New member function "getFirstFailingCycles(..., Boolean& fewerFailsReturnedDueToEmapFull)"
- [PIN_ERROR_MAP_TEST](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.62.01_PIN_ERROR_MAP_TEST.md>) —— SmarTest 7.4.5: Patch 4: Parameter "startCycle" of getFirstFailingCycles() / getFailingCyclesInRange() / getPassFailResultsInRange() must be within the recorded error map range or an error is thrown.
- [PIN_ERROR_MAP_TEST](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.62.01_PIN_ERROR_MAP_TEST.md>) —— SmarTest 7.4.5: Patch 4: Functions getFailingCyclesInRange() and getPassFailResultsInRange() throw an error if the requested range is longer than recorded by the error map and the error map is full.
- [Setting the data log output information in the Datalog Control tool](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.06.01.02_Setting_the_data_log_output_information_in_the_Datalog_Control_tool.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Alphabetical list of flags](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md>) —— SmarTest 7.4.5: Marked stdf_generation as legacy flag
- [Testflow flags for data logging](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.03_Testflow_flags_for_data_logging.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Exporting a testflow to a CSV file](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.16_Exporting_a_testflow_to_a_CSV_file.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Setting up the data log information](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.08_Setting_up_the_data_log_information.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Elements of the Test Cell Control Tool](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10_Elements_of_the_Test_Cell_Control_Tool.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Data logging profile rule syntax](<02_System_reference/02.10_Data_Logging/02.10.01.02.06.03_Data_logging_profile_rule_syntax.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Data logging profile API examples](<02_System_reference/02.10_Data_Logging/02.10.01.02.08.05_Data_logging_profile_API_examples.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Data logging profile API](<02_System_reference/02.10_Data_Logging/02.10.01.02.08_Data_logging_profile_API.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Testflow flags for data logging](<02_System_reference/02.10_Data_Logging/02.10.01.09.01_Testflow_flags_for_data_logging.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Starting the formatter](<02_System_reference/02.10_Data_Logging/02.10.03.02.01_Starting_the_formatter.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [System flags](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.10.01_System_flags.md>) —— SmarTest 7.4.5: Removed stdf_generation flag
- [Data logging settings](<03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.07.01_Data_logging_settings.md>) —— SmarTest 7.4.5: Removed stdf_generation flag


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 18 条**，涉及 **16 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
