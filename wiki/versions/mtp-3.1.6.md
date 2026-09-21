---
type: version
title: MTP 3.1.6 — 版本页
tags: [version, mtp]
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.03.01_Parameters_for_the_ExecutionEngine_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.01_Defining_MTL_arrays.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.01_Setting_up_a_maintenance_operation.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.02_Enabling_and_disabling_maintenance_operations_in_APG_program_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09.01_MTP_ADDRESS_FILTER.setRange.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09.02_MTP_ADDRESS_FILTER.setMode.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09.03_MTP_ADDRESS_FILTER.setDbits.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09.04_MTP_ADDRESS_FILTER.isValidAddress.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09_MTP_ADDRESS_FILTER.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.01_MTP_MEMORY_TEST.addAddressFilter.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.07_MTP_MEMORY_TEST.getMemoryPatternNamesList.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.24_MTP_MEMORY_TEST.setMultiPatternResultMode.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.18.01_MTP_MULTI_FILTER.addAddressFilter.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.18.02_MTP_MULTI_FILTER.isValidAddress.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.18_MTP_MULTI_FILTER.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# MTP 3.1.6

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（11 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `MTP 3.1.6:` 前缀，**那是原文的一部分，没有去掉**。

- [Parameters for the ExecutionEngine test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.03.01_Parameters_for_the_ExecutionEngine_test_method.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) New parameter Multi_Pattern_Result_Mode is added.
- [Macros and functions in program files](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) New commands in REFRESH_CTRL() are added for multiple refreshes maintenance operations.
- [Defining MTL arrays](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.01_Defining_MTL_arrays.md>) —— MTP 3.1.6: Additional restrictions are now flagged as errors by the compiler
- [Device architecture file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) New keyword static_maintop_time_x (x can be any given letter) is added in the :operation: column for multiple refreshes maintenance operations.
- [Setting up a maintenance operation](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.01_Setting_up_a_maintenance_operation.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) Multiple static refreshes maintenance operation is available
- [Enabling and disabling maintenance operations in APG program file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.02_Enabling_and_disabling_maintenance_operations_in_APG_program_file.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) New refresh control instructions for the multiple static refreshes maintenance operations are added.
- [Maintenance operations](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) Multiple static refreshes maintenance operation is available in both MTP on HSM and MTP on SOC
- [Maintenance operations](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) The static refresh supports multiport operation.
- [Maintenance operations](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) New keyword: static_maintop_time_x (x can be any given letter) is added for the multiple refreshes maintenance operation periods.
- [MTP_MEMORY_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) New member functions addAddressFilter() and getMemoryPatternNamesList() are added.
- [MTP_MEMORY_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.md>) —— MTP 3.1.6: (MTP on SOC 103.3.0) New member function setMultiPatternResultMode() is added.


## 这一版新引入（11 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [MTP_ADDRESS_FILTER.setRange()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09.01_MTP_ADDRESS_FILTER.setRange.md>) —— Introduced in MTP 3.1.6
- [MTP_ADDRESS_FILTER.setMode()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09.02_MTP_ADDRESS_FILTER.setMode.md>) —— Introduced in MTP 3.1.6
- [MTP_ADDRESS_FILTER.setDbits()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09.03_MTP_ADDRESS_FILTER.setDbits.md>) —— Introduced in MTP 3.1.6
- [MTP_ADDRESS_FILTER.isValidAddress()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09.04_MTP_ADDRESS_FILTER.isValidAddress.md>) —— Introduced in MTP 3.1.6
- [MTP_ADDRESS_FILTER](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.09_MTP_ADDRESS_FILTER.md>) —— Introduced in MTP 3.1.6
- [MTP_MEMORY_TEST.addAddressFilter()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.01_MTP_MEMORY_TEST.addAddressFilter.md>) —— Introduced in MTP 3.1.6
- [MTP_MEMORY_TEST.getMemoryPatternNamesList()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.07_MTP_MEMORY_TEST.getMemoryPatternNamesList.md>) —— Introduced in MTP 3.1.6
- [MTP_MEMORY_TEST.setMultiPatternResultMode()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.24_MTP_MEMORY_TEST.setMultiPatternResultMode.md>) —— Introduced in MTP 3.1.6
- [MTP_MULTI_FILTER.addAddressFilter()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.18.01_MTP_MULTI_FILTER.addAddressFilter.md>) —— Introduced in MTP 3.1.6
- [MTP_MULTI_FILTER.isValidAddress()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.18.02_MTP_MULTI_FILTER.isValidAddress.md>) —— Introduced in MTP 3.1.6
- [MTP_MULTI_FILTER](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.18_MTP_MULTI_FILTER.md>) —— Introduced in MTP 3.1.6


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 22 条**，涉及 **19 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
