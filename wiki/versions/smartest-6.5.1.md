---
type: version
title: SmarTest 6.5.1 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.243_TestNumGen.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.30_TESTSET__.testtext.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.05.01_Hiding_the_upload_of_the_error_map.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.05_Hidden_Error_Map_Upload.md
  - 02_System_reference/02.10_Data_Logging/02.10.03.03.09.02_Logging_text_data_in_the_TEST_TXT_field.md
  - 02_System_reference/02.10_Data_Logging/02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md
  - 03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.05.02_Hidden_Data_upload.md
  - 03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.05.04.01.01_Hiding_the_upload_of_the_error_map.md
  - 03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.05.04.01_Hidden_Error_Map_Upload.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 6.5.1

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（10 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 6.5.1:` 前缀，**那是原文的一部分，没有去掉**。

- [DFTD, DFTD? (DeFine Test Data)](<02_System_reference/02.06_Command_Reference/02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md>) —— SmarTest 6.5.1: For double or integer attributes, a base or derived variable can be specified instead of a constant
- [TestNumGen](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.243_TestNumGen.md>) —— SmarTest 6.5.1: New parameter TestNumFieldPos for the isDuplicateNum() function
- [TESTSET().testtext()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.30_TESTSET__.testtext.md>) —— SmarTest 6.5.1: testtext can append text to or overwrite the content of TEST_TXT.
- [TESTSET](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.md>) —— SmarTest 6.5.1: testtext() text can replace the content of Test_TXT or be appended to it
- [TMLimits](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md>) —— SmarTest 6.5.1: dump() function removed
- [TMLimits](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md>) —— SmarTest 6.5.1: load() can now be called without parameters
- [TMLimits](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md>) —— SmarTest 6.5.1: New function setTestMode()
- [Logging text data in the TEST_TXT field](<02_System_reference/02.10_Data_Logging/02.10.03.03.09.02_Logging_text_data_in_the_TEST_TXT_field.md>) —— SmarTest 6.5.1: testtext() text can replace the content of TEST_TXT or be appended to it
- [Configuring the contents of the STDF file](<02_System_reference/02.10_Data_Logging/02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md>) —— SmarTest 6.5.1: New configuration options disableTestTxtOverride, TEST_TXT_Test_Separator, PRR_X_COORD_SRC, PRR_Y_COORD_SRC
- [Hidden Data upload](<03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.05.02_Hidden_Data_upload.md>) —— SmarTest 6.5.1: Hidden digital upload


## 这一版新引入（4 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Hiding the upload of the error map](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.05.01_Hiding_the_upload_of_the_error_map.md>) —— Introduced in SmarTest 6.5.1
- [Hidden Error Map Upload](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.05_Hidden_Error_Map_Upload.md>) —— Introduced in SmarTest 6.5.1
- [Hiding the upload of the error map](<03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.05.04.01.01_Hiding_the_upload_of_the_error_map.md>) —— Introduced in SmarTest 6.5.1
- [Hidden Error Map Upload](<03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.05.04.01_Hidden_Error_Map_Upload.md>) —— Introduced in SmarTest 6.5.1


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 14 条**，涉及 **12 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
