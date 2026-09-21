---
type: version
title: SmartRDI 7.5.2 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.03_Template_file_from_online_test_results.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.03_The__dc__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.06_The__emap__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.10_The__smartVec__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20_Using_Offline_Result_Emulation_in_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01_Alarm_setup_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.10_insertSub.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01_DC_test_with_digital_channels.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.20_insertSub.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.16_vecVar.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.20_rdi.id__.getVectorFromVV.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.14.04_setOffRunTime.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.14.06_setOnRunTime.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.02_rdi.route__.downloadPmuxMemSet.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.03_rdi.func__.burstRunTime.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.07_rdi.func__.perLabelPassFail.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.18_rdi.id__.getMultiPassFail.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.09_download.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 7.5.2

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（14 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 7.5.2:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 7.5.2: New keywords ALARM_FAIL_WARNING and ORE_FOLDER; new value TRUE_OFFLINE for ENABLE_ORE.
- [The <dc> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.03_The__dc__element.md>) —— SmartRDI 7.5.2: New multiValue syntax for ARRAY_D& getMultiValue(pin).
- [The <emap> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.06_The__emap__element.md>) —— SmartRDI 7.5.2: More attributes and syntax are supported.
- [The <smartVec> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.10_The__smartVec__element.md>) —— SmartRDI 7.5.2: More attributes and syntax are supported.
- [Using Offline Result Emulation in SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20_Using_Offline_Result_Emulation_in_SmartRDI.md>) —— SmartRDI 7.5.2: Testflow variable RDI_ORE_FILE
- [Alarm setup file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01_Alarm_setup_file.md>) —— SmartRDI 7.5.2: SmartRDI provides more information in the UI report window when the DEBUG_VALUE is enabled.
- [SmartRDI: Alarm handling for DCVI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md>) —— SmartRDI 7.5.2: Alarm checking can trigger a hidden port synchronization with portSync() after alarm compare.
- [insertSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.10_insertSub.md>) —— SmartRDI 7.5.2: Support both an existing sublabel to be inserted to a user-defined pattern and DC actions to be inserted to the sublabel.
- [DC test with digital channels](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01_DC_test_with_digital_channels.md>) —— SmartRDI 7.5.2: Execution times for PPMU and BADC are changed.
- [insertSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.20_insertSub.md>) —— SmartRDI 7.5.2: Support an existing sublabel to be inserted to a user-defined pattern and DC actions to be inserted to a sublabel.
- [Setting up DC Scale pins with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) —— SmartRDI 7.5.2: Execution times for some actions are changed.
- [setOffRunTime()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.04_setOffRunTime.md>) —— SmartRDI 7.5.2: This function can be used in the static mode.
- [setOnRunTime()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.06_setOnRunTime.md>) —— SmartRDI 7.5.2: This function can be used in the static mode.
- [rdi.route().downloadPmuxMemSet()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.02_rdi.route__.downloadPmuxMemSet.md>) —— SmartRDI 7.5.2: downloadPmuxMemSet().xMode() to reduce vector memory consumption.


## 这一版新引入（7 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Template file from online test results](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.03_Template_file_from_online_test_results.md>) —— Introduced in SmartRDI 7.5.2
- [vecVar()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.16_vecVar.md>) —— Introduced in SmartRDI 7.5.2
- [rdi.id().getVectorFromVV()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.20_rdi.id__.getVectorFromVV.md>) —— Introduced in SmartRDI 7.5.2
- [rdi.func().burstRunTime()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.03_rdi.func__.burstRunTime.md>) —— Introduced in SmartRDI 7.5.2
- [rdi.func().perLabelPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.07_rdi.func__.perLabelPassFail.md>) —— Introduced in SmartRDI 7.5.2
- [rdi.id().getMultiPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.18_rdi.id__.getMultiPassFail.md>) —— Introduced in SmartRDI 7.5.2
- [download()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.09_download.md>) —— Introduced in SmartRDI 7.5.2


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 21 条**，涉及 **21 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
