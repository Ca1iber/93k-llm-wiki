---
type: version
title: SmartRDI 2.4.2 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.07_RDI_UNIT_INIT.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05.01_fastSyncOff.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05.02_fastSyncOn.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05.03_fastSyncPortNum.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05_Fast_Sync_setup_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.01_Using_hidden_upload_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.07_iClamp.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.04_connectSense.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.11_iClamp.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.15_iFilter.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.17_iForceRange.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.23_iSlewRate.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.26_loadCap.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.28_measFilter.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.32_preCharge.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.35_restoreRange.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.39_vClamp.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.40_vFilter.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.42_vForceRange.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.48_vSlewRate.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.14.03_setOff.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.14.05_setOn.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.09_rdi.tmu__.measMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.13_rdi.tmu__.samples.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.4.2

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（22 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.4.2:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_UNIT_INIT()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.07_RDI_UNIT_INIT.md>) —— SmartRDI 2.4.2: No location limitation for a result retrieval command.
- [Changing the parameter value at runtime with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md>) —— SmartRDI 2.4.2: Support vClamp() in DC tests.
- [Using hidden upload with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.01_Using_hidden_upload_with_SmartRDI.md>) —— SmartRDI 2.4.2: No unique result ID requirement and non-hidden upload result retrieval commands in SMC_BackgroundProcessing.
- [rdi.hiddenUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md>) —— SmartRDI 2.4.2: A new option TA::EMAP for error map hidden upload.
- [iClamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.07_iClamp.md>) —— SmartRDI 2.4.2: Variations of the syntax and AVI64 added.
- [connectSense()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.04_connectSense.md>) —— SmartRDI 2.4.2: AVI64 added.
- [iClamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.11_iClamp.md>) —— SmartRDI 2.4.2: Variations of the syntax and AVI64 added.
- [iForceRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.17_iForceRange.md>) —— SmartRDI 2.4.2: AVI64 added.
- [loadCap()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.26_loadCap.md>) —— SmartRDI 2.4.2: DC Scale AVI64 card added.
- [preCharge()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.32_preCharge.md>) —— SmartRDI 2.4.2: DC Scale AVI64 card added.
- [restoreRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.35_restoreRange.md>) —— SmartRDI 2.4.2: DC Scale AVI64 card added.
- [vForceRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.42_vForceRange.md>) —— SmartRDI 2.4.2: AVI64 added.
- [Setting up DC Scale pins with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) —— SmartRDI 2.4.2: New functions iFilter(), vFilter(), iSlewRate(), vSlewRate().
- [Setting up DC Scale pins with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) —— SmartRDI 2.4.2: New functions mode(), refPin(), measFilter(), vClamp().
- [setOff()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.03_setOff.md>) —— SmartRDI 2.4.2: AVI64 added.
- [setOn()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.05_setOn.md>) —— SmartRDI 2.4.2: AVI64 added.
- [rdi.tmu().measMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.09_rdi.tmu__.measMode.md>) —— SmartRDI 2.4.2: AVI64 added.
- [rdi.tmu().samples()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.13_rdi.tmu__.samples.md>) —— SmartRDI 2.4.2: DC Scale AVI64 card added.
- [SmartRDI: TMU test setup](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md>) —— SmartRDI 2.4.2: DC Scale AVI64 card added
- [SmartRDI: TMU test setup](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md>) —— SmartRDI 2.4.2: New functions compHyst(), compMode(), ith()
- [burstLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md>) —— SmartRDI 2.4.2: enPassFail() in the command line with burstLable().
- [SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md>) —— SmartRDI 2.4.2: DC Scale AVI64 card added.


## 这一版新引入（10 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [fastSyncOff()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05.01_fastSyncOff.md>) —— Introduced in SmartRDI 2.4.2
- [fastSyncOn()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05.02_fastSyncOn.md>) —— Introduced in SmartRDI 2.4.2
- [fastSyncPortNum()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05.03_fastSyncPortNum.md>) —— Introduced in SmartRDI 2.4.2
- [Fast Sync setup with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.05_Fast_Sync_setup_with_SmartRDI.md>) —— Introduced in SmartRDI 2.4.2
- [iFilter()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.15_iFilter.md>) —— Introduced in SmartRDI 2.4.2
- [iSlewRate()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.23_iSlewRate.md>) —— Introduced in SmartRDI 2.4.2
- [measFilter()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.28_measFilter.md>) —— Introduced in SmartRDI 2.4.2
- [vClamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.39_vClamp.md>) —— Introduced in SmartRDI 2.4.2
- [vFilter()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.40_vFilter.md>) —— Introduced in SmartRDI 2.4.2
- [vSlewRate()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.48_vSlewRate.md>) —— Introduced in SmartRDI 2.4.2


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 32 条**，涉及 **30 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
