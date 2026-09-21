---
type: version
title: SmartRDI 2.3.0 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.12_label.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.13_limit.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.15_pin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.20_vMeas.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.22_rdi.id__.getMultiValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.23_getValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.01_amux.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.06_label.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.07_limit.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.09_pin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.13_getValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.14_getValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.21_insertVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.24_label.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.25_limit.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.50_getMultiValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.51_getValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.06_burstUpload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.14.05_setOn.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.02_rdi.func__.burstId.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.13_rdi.getBurstPassFail.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.14_rdi.id__.getBurstPassFail.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.01_rdi.tmu__.dataRate.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.04_rdi.tmu__.initDiscard.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.05_rdi.tmu__.insertVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.06_rdi.tmu__.interSkip.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.07_rdi.tmu__.label.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.09_rdi.tmu__.measMode.md
  # 本页共涉及 66 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.3.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（14 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.3.0:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.3.0: New keywords PPMU_PURE_VMEAS_2P2_COMPATIBLE_MODE and PMUX_X_CTRL.
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.15_pin.md>) —— SmartRDI 2.3.0: Supports high voltage pins in static DC measurement.
- [valueMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md>) —— SmartRDI 2.3.0: Supports high voltage pins.
- [valueMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md>) —— SmartRDI 2.3.0: When pins that share the same board ADC are measured with the BADC, these pins can be set in the same pin() function.
- [vMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.20_vMeas.md>) —— SmartRDI 2.3.0: Supports setting up the force current iForce() and vMeas() in different lines.
- [vMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.20_vMeas.md>) —— SmartRDI 2.3.0: Adds new keyword PPMU_PURE_VMEAS_2P2_COMPATIBLE_MODE to the RDI configuration file.
- [getValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.23_getValue.md>) —— SmartRDI 2.3.0: Adds a new function getMultiValue().
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.09_pin.md>) —— SmartRDI 2.3.0: Supports high voltage pins in static DC value measurements.
- [getValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.13_getValue.md>) —— SmartRDI 2.3.0: Adds a new function getMultiValue().
- [getValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.14_getValue.md>) —— SmartRDI 2.3.0: Adds a new function getMultiValue().
- [getValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.51_getValue.md>) —— SmartRDI 2.3.0: Adds a new function getMultiValue().
- [setOn()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.05_setOn.md>) —— SmartRDI 2.3.0: New options: AMUX_PPMU and AMUX_BADC.
- [rdi.getBurstPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.13_rdi.getBurstPassFail.md>) —— SmartRDI 2.3.0: Adds a new parameter, pin.
- [rdi.getBurstPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.13_rdi.getBurstPassFail.md>) —— SmartRDI 2.3.0: Supports the result retrieving from buffer.


## 这一版新引入（55 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [label()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.12_label.md>) —— Introduced in SmartRDI 2.3.0
- [limit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.13_limit.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.id().getMultiValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.22_rdi.id__.getMultiValue.md>) —— Introduced in SmartRDI 2.3.0
- [amux()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.01_amux.md>) —— Introduced in SmartRDI 2.3.0
- [label()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.06_label.md>) —— Introduced in SmartRDI 2.3.0
- [limit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.07_limit.md>) —— Introduced in SmartRDI 2.3.0
- [insertVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.21_insertVec.md>) —— Introduced in SmartRDI 2.3.0
- [label()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.24_label.md>) —— Introduced in SmartRDI 2.3.0
- [limit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.25_limit.md>) —— Introduced in SmartRDI 2.3.0
- [getMultiValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.50_getMultiValue.md>) —— Introduced in SmartRDI 2.3.0
- [burstUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.06_burstUpload.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.func().burstId()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.02_rdi.func__.burstId.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.id().getBurstPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.14_rdi.id__.getBurstPassFail.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.tmu().dataRate()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.01_rdi.tmu__.dataRate.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.tmu().initDiscard()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.04_rdi.tmu__.initDiscard.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.tmu().insertVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.05_rdi.tmu__.insertVec.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.tmu().interSkip()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.06_rdi.tmu__.interSkip.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.tmu().label()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.07_rdi.tmu__.label.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.tmu().measMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.09_rdi.tmu__.measMode.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.tmu().pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.11_rdi.tmu__.pin.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.tmu().preScaler()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.12_rdi.tmu__.preScaler.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.tmu().samples()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.13_rdi.tmu__.samples.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.id().getArm()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.14_rdi.id__.getArm.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.id().getInterSkip()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.15_rdi.id__.getInterSkip.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.id().getMultiArm()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.16_rdi.id__.getMultiArm.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.id().getPreScaler()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.17_rdi.id__.getPreScaler.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.id().getStamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.20_rdi.id__.getStamp.md>) —— Introduced in SmartRDI 2.3.0
- [SmartRDI: TMU test setup](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md>) —— Introduced in SmartRDI 2.3.0
- [bitLength()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.02_bitLength.md>) —— Introduced in SmartRDI 2.3.0
- [burstLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md>) —— Introduced in SmartRDI 2.3.0
- [burstUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.04_burstUpload.md>) —— Introduced in SmartRDI 2.3.0
- [comment()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.05_comment.md>) —— Introduced in SmartRDI 2.3.0
- [defaultBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.07_defaultBit.md>) —— Introduced in SmartRDI 2.3.0
- [defaultVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.08_defaultVec.md>) —— Introduced in SmartRDI 2.3.0
- [expectBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.12_expectBit.md>) —— Introduced in SmartRDI 2.3.0
- [expectData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.13_expectData.md>) —— Introduced in SmartRDI 2.3.0
- [fillBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.18_fillBit.md>) —— Introduced in SmartRDI 2.3.0
- [fillVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.19_fillVec.md>) —— Introduced in SmartRDI 2.3.0
- [labelName()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.23_labelName.md>) —— Introduced in SmartRDI 2.3.0
- [pMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.26_pMode.md>) —— Introduced in SmartRDI 2.3.0
- [readBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.28_readBit.md>) —— Introduced in SmartRDI 2.3.0
- [readData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.29_readData.md>) —— Introduced in SmartRDI 2.3.0
- [rdi.smartVec().readMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.30_rdi.smartVec__.readMode.md>) —— Introduced in SmartRDI 2.3.0
- [vecLength()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.34_vecLength.md>) —— Introduced in SmartRDI 2.3.0
- [writeBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.35_writeBit.md>) —— Introduced in SmartRDI 2.3.0
- [writeData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.36_writeData.md>) —— Introduced in SmartRDI 2.3.0
- [writeDataBurst()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.37_writeDataBurst.md>) —— Introduced in SmartRDI 2.3.0
- [writeParData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.38_writeParData.md>) —— Introduced in SmartRDI 2.3.0
- [writeParDataBurst()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.39_writeParDataBurst.md>) —— Introduced in SmartRDI 2.3.0
- [writePat()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.40_writePat.md>) —— Introduced in SmartRDI 2.3.0
- [writeVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.41_writeVec.md>) —— Introduced in SmartRDI 2.3.0
- [xMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.42_xMode.md>) —— Introduced in SmartRDI 2.3.0
- [getReadBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.47_getReadBit.md>) —— Introduced in SmartRDI 2.3.0
- [getReadData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.48_getReadData.md>) —— Introduced in SmartRDI 2.3.0
- [SmartRDI: Vector and protocol programming](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24_SmartRDI__Vector_and_protocol_programming.md>) —— Introduced in SmartRDI 2.3.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 69 条**，涉及 **66 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
