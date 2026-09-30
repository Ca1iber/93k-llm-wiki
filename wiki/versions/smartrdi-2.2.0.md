---
type: version
title: SmartRDI 2.2.0 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.02_portSync.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.10.06_write.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.10.07_writeBurst.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.05_sampleCycle.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.06_samplePeriod.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.04_sampleCycle.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.05_samplePeriod.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.05_Using_a_DC_Scale_resource_as_a_digitizer_while_sourcing_a_waveform_on_th.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11_SmartRDI__DC_resource_AWG_DGT_usage.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.16_postWait.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.17_relay.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.10_postWait.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02_Setting_up_Board_ADC_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.12_iClampFilter.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.22_iPulse.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.31_postWait.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.32_preCharge.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.47_vPulse.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.2.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（8 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.2.0:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.2.0: New keywords RF_OPTMIZE_SEQUENCE and RF_STIM_PATH_LOSS_ADJUSTMENT.
- [portSync()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.02_portSync.md>) —— SmartRDI 2.2.0: Supports synchronizing selected ports.
- [write()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.06_write.md>) —— SmartRDI 2.2.0: Removed the functionality of burst write.
- [SmartRDI: DC resource AWG/DGT usage](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11_SmartRDI__DC_resource_AWG_DGT_usage.md>) —— SmartRDI 2.2.0: Supports using the DC Scale resource as a digitizer while sourcing a waveform on the same pin.
- [relay()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.17_relay.md>) —— SmartRDI 2.2.0: Supports the syntax relay(TA::PPMU_RELAY_ACTION rly_before)
- [valueMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md>) —— SmartRDI 2.2.0: Supports switching AMUX in the pattern‑based mode when measuring with board ADC on PS1600.
- [Setting up Board ADC with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02_Setting_up_Board_ADC_with_SmartRDI.md>) —— SmartRDI 2.2.0: Supports switching AMUX on PS1600 in the pattern‑based mode.
- [Setting up DC Scale pins with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) —— SmartRDI 2.2.0: New function preCharge().


## 这一版新引入（13 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [writeBurst()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.07_writeBurst.md>) —— Introduced in SmartRDI 2.2.0
- [sampleCycle()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.05_sampleCycle.md>) —— Introduced in SmartRDI 2.2.0
- [samplePeriod()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.06_samplePeriod.md>) —— Introduced in SmartRDI 2.2.0
- [sampleCycle()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.04_sampleCycle.md>) —— Introduced in SmartRDI 2.2.0
- [samplePeriod()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.05_samplePeriod.md>) —— Introduced in SmartRDI 2.2.0
- [Using a DC Scale resource as a digitizer while sourcing a waveform on the same pin](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.05_Using_a_DC_Scale_resource_as_a_digitizer_while_sourcing_a_waveform_on_th.md>) —— Introduced in SmartRDI 2.2.0
- [postWait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.16_postWait.md>) —— Introduced in SmartRDI 2.2.0
- [postWait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.10_postWait.md>) —— Introduced in SmartRDI 2.2.0
- [iClampFilter()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.12_iClampFilter.md>) —— Introduced in SmartRDI 2.2.0
- [iPulse()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.22_iPulse.md>) —— Introduced in SmartRDI 2.2.0
- [postWait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.31_postWait.md>) —— Introduced in SmartRDI 2.2.0
- [preCharge()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.32_preCharge.md>) —— Introduced in SmartRDI 2.2.0
- [vPulse()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.47_vPulse.md>) —— Introduced in SmartRDI 2.2.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 21 条**，涉及 **21 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
