---
type: version
title: MTP 2.4.0 — 版本页
tags: [version, mtp]
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.02_Preprocessor_statements.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.03_Conditional_execution.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.05_Variables.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.06_Values.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01_APG_program_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.01_Device_access_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.08.01_DC_event_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.09.01_Setting_up_cyclic_redundancy_checks.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.09_Cyclic_redundancy_checks.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.10.01_Setting_up_dynamic_bus_inversion.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.10_Dynamic_bus_inversion.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13.02_Setting_up_DC_event_sequences.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13_Controlling_power_supply_and_measurements.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# MTP 2.4.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（19 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `MTP 2.4.0:` 前缀，**那是原文的一部分，没有去掉**。

- [APG pattern file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md>) —— MTP 2.4.0: Floating-point values supported for :programParam:
- [APG pattern file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md>) —— MTP 2.4.0: Added :crc: keyword
- [APG pattern file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md>) —— MTP 2.4.0: Added :dbi: keyword
- [Variables](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.05_Variables.md>) —— MTP 2.4.0: Floating-point values supported in APG pattern file
- [Variables](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.05_Variables.md>) —— MTP 2.4.0: Global variables are now supported
- [Values](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.06_Values.md>) —— MTP 2.4.0: Floating-point numbers from APG pattern file are truncated
- [Macros and functions in program files](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md>) —— MTP 2.4.0: DC_EVENT_RANGE macro added
- [APG program file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01_APG_program_file_syntax.md>) —— MTP 2.4.0: Added preprocessor statements
- [APG program file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01_APG_program_file_syntax.md>) —— MTP 2.4.0: Added if statements
- [APG program file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01_APG_program_file_syntax.md>) —— MTP 2.4.0: Added DC_EVENT_RANGE call
- [Device access file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.01_Device_access_file_syntax.md>) —— MTP 2.4.0: :operation: column added to :apgAccess:
- [Macros and functions in device accesses](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md>) —— MTP 2.4.0: bitCount function added
- [Macros and functions in device accesses](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md>) —— MTP 2.4.0: crc macro added
- [Macros and functions in device accesses](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md>) —— MTP 2.4.0: dbi macro added
- [Device architecture file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md>) —— MTP 2.4.0: :crc: keyword and subordinate keywords added
- [Device architecture file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md>) —— MTP 2.4.0: :dbi: keyword and subordinate keywords added
- [Device architecture file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md>) —— MTP 2.4.0: :operationOrder: keyword added
- [DC event file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.08.01_DC_event_file_syntax.md>) —— MTP 2.4.0: Added :dcSequence: and subordinate keywords
- [Controlling power supply and measurements](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13_Controlling_power_supply_and_measurements.md>) —— MTP 2.4.0: Sequences of DC events introduced


## 这一版新引入（7 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Preprocessor statements](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.02_Preprocessor_statements.md>) —— Introduced in MTP 2.4.0
- [Conditional execution](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.03_Conditional_execution.md>) —— Introduced in MTP 2.4.0
- [Setting up cyclic redundancy checks](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.09.01_Setting_up_cyclic_redundancy_checks.md>) —— Introduced in MTP 2.4.0
- [Cyclic redundancy checks](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.09_Cyclic_redundancy_checks.md>) —— Introduced in MTP 2.4.0
- [Setting up dynamic bus inversion](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.10.01_Setting_up_dynamic_bus_inversion.md>) —— Introduced in MTP 2.4.0
- [Dynamic bus inversion](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.10_Dynamic_bus_inversion.md>) —— Introduced in MTP 2.4.0
- [Setting up DC event sequences](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13.02_Setting_up_DC_event_sequences.md>) —— Introduced in MTP 2.4.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 26 条**，涉及 **17 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
