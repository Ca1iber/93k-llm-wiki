---
type: version
title: MTP 3.1.4 — 版本页
tags: [version, mtp]
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06.01_Logging_formats_and_data_types.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06.02_Configuring_data_logging_for_memory_tests.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06.03_Memory_test_data_log_event_structure.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06_Logging_memory_tests.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.01_Defining_MTL_arrays.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.02_Accessing_elements_of_an_MTL_array.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.03_Passing_MTL_arrays_to_functions_and_device_accesses.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.04_Restrictions_when_using_MTL_arrays.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05.01_Accessing_burst_data.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05.02_Random_address_patterns.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05.03_Random_scrambling_patterns.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05.04_Bank_interleaved_patterns.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05_Use_cases_for_MTL_arrays.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01_Using_MTL_arrays.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09_Array_in_MTL.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01_APG_program_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.01_Automatic_Map_Converter_operating_principles.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.02_Creating_a_map_converter_library_with_the_Automatic_Map_Converter.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.03_Device_property_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05_Automatic_Map_Converter.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.01.01_BfdGenerator.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.01.02_BfdGenerator.addFailmap.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.01_BfdGenerator.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.08_MTP_MEMORY_PATTERN.getFailingAddressList.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# MTP 3.1.4

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（10 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `MTP 3.1.4:` 前缀，**那是原文的一部分，没有去掉**。

- [Logging formats and data types](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06.01_Logging_formats_and_data_types.md>) —— MTP 3.1.4: Logging memory tests events is available both in MTP on HSM and MTP on SOC.
- [Configuring data logging for memory tests](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06.02_Configuring_data_logging_for_memory_tests.md>) —— MTP 3.1.4: Logging memory tests events is available both in MTP on HSM and MTP on SOC.
- [Memory test data log event structure](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06.03_Memory_test_data_log_event_structure.md>) —— MTP 3.1.4: Logging memory tests events is available both in MTP on HSM and MTP on SOC.
- [Logging memory tests](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.06_Logging_memory_tests.md>) —— MTP 3.1.4: Logging memory tests events is available both in MTP on HSM and MTP on SOC.
- [APG program file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01_APG_program_file_syntax.md>) —— MTP 3.1.4: Added array data type
- [Automatic Map Converter operating principles](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.01_Automatic_Map_Converter_operating_principles.md>) —— MTP 3.1.4: Redundancy analysis is now supported.
- [Creating a map converter library with the Automatic Map Converter](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.02_Creating_a_map_converter_library_with_the_Automatic_Map_Converter.md>) —— MTP 3.1.4: Redundancy analysis is now supported.
- [Device property file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.03_Device_property_file.md>) —— MTP 3.1.4: Added the redundancyAnalysis element and its subelements
- [Automatic Map Converter](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05_Automatic_Map_Converter.md>) —— MTP 3.1.4: Redundancy analysis is now supported.
- [MTP_MEMORY_PATTERN.getFailingAddressList()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.08_MTP_MEMORY_PATTERN.getFailingAddressList.md>) —— MTP 3.1.4: The capability to retrieve failing addresses for multiple pins is added.


## 这一版新引入（14 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Defining MTL arrays](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.01_Defining_MTL_arrays.md>) —— Introduced in MTP 3.1.4
- [Accessing elements of an MTL array](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.02_Accessing_elements_of_an_MTL_array.md>) —— Introduced in MTP 3.1.4
- [Passing MTL arrays to functions and device accesses](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.03_Passing_MTL_arrays_to_functions_and_device_accesses.md>) —— Introduced in MTP 3.1.4
- [Restrictions when using MTL arrays](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.04_Restrictions_when_using_MTL_arrays.md>) —— Introduced in MTP 3.1.4
- [Accessing burst data](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05.01_Accessing_burst_data.md>) —— Introduced in MTP 3.1.4
- [Random address patterns](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05.02_Random_address_patterns.md>) —— Introduced in MTP 3.1.4
- [Random scrambling patterns](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05.03_Random_scrambling_patterns.md>) —— Introduced in MTP 3.1.4
- [Bank interleaved patterns](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05.04_Bank_interleaved_patterns.md>) —— Introduced in MTP 3.1.4
- [Use cases for MTL arrays](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.05_Use_cases_for_MTL_arrays.md>) —— Introduced in MTP 3.1.4
- [Using MTL arrays](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01_Using_MTL_arrays.md>) —— Introduced in MTP 3.1.4
- [Array in MTL](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09_Array_in_MTL.md>) —— Introduced in MTP 3.1.4
- [BfdGenerator()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.01.01_BfdGenerator.md>) —— Introduced in MTP 3.1.4
- [BfdGenerator.addFailmap()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.01.02_BfdGenerator.addFailmap.md>) —— Introduced in MTP 3.1.4
- [BfdGenerator](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.01_BfdGenerator.md>) —— Introduced in MTP 3.1.4


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 24 条**，涉及 **24 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
