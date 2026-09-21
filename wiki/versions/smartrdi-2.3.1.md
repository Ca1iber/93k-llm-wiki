---
type: version
title: SmartRDI 2.3.1 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.01.11_Supported_SmarTest_Versions.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.04_rdi.site.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.02_clamp.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.03_clampOff.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.07_iClamp.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.21_getBurstValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.11_iClamp.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.26_loadCap.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.49_getBurstValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.11_rdi.func__.stopVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.12_rdi.func__.stopVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.02_rdi.tmu__.disable.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.04_burstUpload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.27_pModeStrobe.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.31_repeat.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.3.1

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（5 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.3.1:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.3.1: New keywords PPMU_DEFAULT_VALUE_MODE and PPMU_DEFAULT_RELAY.
- [rdi.hiddenUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md>) —— SmartRDI 2.3.1: A new option TA::TMU for digital TMU measurements.
- [clamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.02_clamp.md>) —— SmartRDI 2.3.1: You can independently use clamp() to set the clamp with more flexibility.
- [valueMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md>) —— SmartRDI 2.3.1: You can add an option PPMU_DEFAULT_VALUE_MODE in the RDI_Configure file to set the default value mode for PPMU.
- [burstUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.04_burstUpload.md>) —— SmartRDI 2.3.1: Combine the result of all readBit()/readData() commands inside burstUpload.begin()/end().


## 这一版新引入（13 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Supported SmarTest Versions](<02_System_reference/02.07_Test_Method_Reference/02.07.13.01.11_Supported_SmarTest_Versions.md>) —— Introduced in SmartRDI 2.3.1
- [rdi.site()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.04_rdi.site.md>) —— Introduced in SmartRDI 2.3.1
- [clampOff()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.03_clampOff.md>) —— Introduced in SmartRDI 2.3.1
- [iClamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.07_iClamp.md>) —— Introduced in SmartRDI 2.3.1
- [getBurstValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.21_getBurstValue.md>) —— Introduced in SmartRDI 2.3.1
- [iClamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.11_iClamp.md>) —— Introduced in SmartRDI 2.3.1
- [loadCap()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.26_loadCap.md>) —— Introduced in SmartRDI 2.3.1
- [getBurstValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.49_getBurstValue.md>) —— Introduced in SmartRDI 2.3.1
- [rdi.func().stopVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.11_rdi.func__.stopVec.md>) —— Introduced in SmartRDI 2.3.1
- [rdi.func().stopVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.12_rdi.func__.stopVec.md>) —— Introduced in SmartRDI 2.3.1
- [rdi.tmu().disable()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.02_rdi.tmu__.disable.md>) —— Introduced in SmartRDI 2.3.1
- [pModeStrobe()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.27_pModeStrobe.md>) —— Introduced in SmartRDI 2.3.1
- [repeat()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.31_repeat.md>) —— Introduced in SmartRDI 2.3.1


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 18 条**，涉及 **18 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
