---
type: version
title: SmartRDI 7.5.1 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.01_cont.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.09.02_Pass_Fail_per_label_without_break_vectors.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.02_Template_file_based_on_user_code.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20_Using_Offline_Result_Emulation_in_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01_Alarm_setup_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.05_sampleCycle.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.07.03_Forcing_waveform_and_sampling_in_parallel_on_multiple_pins.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.10_insertSub.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.20_insertSub.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.21_insertVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.01_combinedFailCount.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.17_rdi.id__.getCombinedFailCount.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 7.5.1

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（15 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 7.5.1:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 7.5.1: New keyword ORE_TEMPLATE_BY_USER_CODE.
- [cont()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.01_cont.md>) —— SmartRDI 7.5.1: cont() supports insertVec().
- [Pass/Fail per label without break vectors](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.09.02_Pass_Fail_per_label_without_break_vectors.md>) —— SmartRDI 7.5.1: Added rdi.perLabelFuncPassFailNoBreakVec(bool) to change the flag in test method.
- [Using Offline Result Emulation in SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20_Using_Offline_Result_Emulation_in_SmartRDI.md>) —— SmartRDI 7.5.1: ORE master file
- [Alarm setup file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01_Alarm_setup_file.md>) —— SmartRDI 7.5.1: An alarm setup template file will be generated if the alarm handling is enabled in the RDI_Configure file.
- [Alarm setup file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01_Alarm_setup_file.md>) —— SmartRDI 7.5.1: A DEBUG_VALUE keyword in the alarm setup file to enable the display of voltage measurement results in the UI report window.
- [SmartRDI: Alarm handling for DCVI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md>) —— SmartRDI 7.5.1: Measurement can trigger alarm checking on other ports besides its own.
- [SmartRDI: Alarm handling for DCVI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md>) —— SmartRDI 7.5.1: Alarm handling can add alarm checking to the level of pulse after measurement.
- [SmartRDI: Alarm handling for DCVI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md>) —— SmartRDI 7.5.1: Alarm handling can automatically handle vMeasRange() and iMeasRange() on DPS128 and PVI8 cards.
- [sampleCycle()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.05_sampleCycle.md>) —— SmartRDI 7.5.1: AVI64 supports a sample vector distance of 8 for the high-speed voltage AWG
- [insertSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.10_insertSub.md>) —— SmartRDI 7.5.1: Support waveform sourcing and sampling.
- [insertSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.20_insertSub.md>) —— SmartRDI 7.5.1: Support waveform sourcing and sampling.
- [insertVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.21_insertVec.md>) —— SmartRDI 7.5.1: insertVec() supports cont() for the same pin.
- [Setting up DC Scale pins with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) —— SmartRDI 7.5.1: New functions dcPowerBudget(), pulseEnergyBudget().
- [SmartRDI: TMU test setup](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md>) —— SmartRDI 7.5.1: New function holdOffTime()


## 这一版新引入（4 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Template file based on user code](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.02_Template_file_based_on_user_code.md>) —— Introduced in SmartRDI 7.5.1
- [Forcing waveform and sampling in parallel on multiple pins](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.07.03_Forcing_waveform_and_sampling_in_parallel_on_multiple_pins.md>) —— Introduced in SmartRDI 7.5.1
- [combinedFailCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.01_combinedFailCount.md>) —— Introduced in SmartRDI 7.5.1
- [rdi.id().getCombinedFailCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.17_rdi.id__.getCombinedFailCount.md>) —— Introduced in SmartRDI 7.5.1


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 19 条**，涉及 **16 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
