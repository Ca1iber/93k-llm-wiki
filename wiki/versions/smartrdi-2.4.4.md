---
type: version
title: SmartRDI 2.4.4 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.02_Macros_to_get_the_SmartRDI_version_number.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.09.01_Pass_Fail_per_label_with_digital_capture.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.06_Serial_Semi-parallel_execution_of_BADC_as_digitizer_over_sites.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.07.02_Forcing_waveform_on_a_pin_and_sampling_on_another_pin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.04_copyLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.10_insertSub.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.03_copyLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.08_measWait.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.09_pin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.04_disconnect.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.05_copyLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.06_disconnect.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.08_copyLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.08_rdi.tmu__.label__.copyLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.22.01_getLabelCycleNum.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.06_copyLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.14_failCount.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.15_failCyc.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.16_failNode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.17_FFC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.20_insertJmpe.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.21_insertSub.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.22_label.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.25_passNode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.31_repeat.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.32_repeatSub.md
  # 本页共涉及 34 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.4.4

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（11 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.4.4:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.4.4: New keywords ALLOW_SAME_RESULT_ID_ACROSS_RDI_BLOCK, COMBINED_FREQ_LIST, DEFAULT_SMV_READ_MODE, and UTIL_CTRL_MAX_SPEED.
- [Changing the parameter value at runtime with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md>) —— SmartRDI 2.4.4: Support vtl() and ith() in TMU tests.
- [rdi.hiddenUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md>) —— SmartRDI 2.4.4: Supports the new API for PVI8/AVI64 hidden upload (SMT 7.4.1); supports the new API for common thread upload of TMU results (SMT 7.4.1).
- [insertSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.10_insertSub.md>) —— SmartRDI 2.4.4: Support multiple insertSub() calls in one vector line.
- [measWait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.08_measWait.md>) —— SmartRDI 2.4.4: For BADC-HIZ measurements via the DC-relay, the measWait() time is effective before every measurement.
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.09_pin.md>) —— SmartRDI 2.4.4: Supports a single .execute() call for shared BADCs over pins, and for shared BADCs over sites in a BADC-HIZ measurement.
- [disconnect()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.04_disconnect.md>) —— SmartRDI 2.4.4: Adds disconnect(min, max) for ganged pins to avoid warning message.
- [disconnect()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.06_disconnect.md>) —— SmartRDI 2.4.4: Adds disconnect(min, max) for ganged pins to avoid warning message.
- [burstLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md>) —— SmartRDI 2.4.4: Supports the combination of run-time accesses for the VTT mode within a burstLabel().begin()/burstLabel().end() block.
- [repeat()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.31_repeat.md>) —— SmartRDI 2.4.4: Enhanced flexibility by adding repeat(int rptNum, int vecSize, int startVec) to allow selecting a sector for repetition and adding multiple RPTV invocations into a pattern.
- [rdi.smartVec().vecEditMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.33_rdi.smartVec__.vecEditMode.md>) —— SmartRDI 2.4.4: Supports changing edit mode inside an RDI_BEGIN()/RDI_END() block.


## 这一版新引入（23 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Macros to get the SmartRDI version number](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.02_Macros_to_get_the_SmartRDI_version_number.md>) —— Introduced in SmartRDI 2.4.4
- [Pass/Fail per label with digital capture](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.09.01_Pass_Fail_per_label_with_digital_capture.md>) —— Introduced in SmartRDI 2.4.4
- [Serial/Semi-parallel execution of BADC as digitizer over sites](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.06_Serial_Semi-parallel_execution_of_BADC_as_digitizer_over_sites.md>) —— Introduced in SmartRDI 2.4.4
- [Forcing waveform on a pin and sampling on another pin](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.07.02_Forcing_waveform_on_a_pin_and_sampling_on_another_pin.md>) —— Introduced in SmartRDI 2.4.4
- [copyLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.04_copyLabel.md>) —— Introduced in SmartRDI 2.4.4
- [copyLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.03_copyLabel.md>) —— Introduced in SmartRDI 2.4.4
- [copyLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.05_copyLabel.md>) —— Introduced in SmartRDI 2.4.4
- [copyLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.08_copyLabel.md>) —— Introduced in SmartRDI 2.4.4
- [rdi.tmu().label().copyLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.08_rdi.tmu__.label__.copyLabel.md>) —— Introduced in SmartRDI 2.4.4
- [getLabelCycleNum()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.01_getLabelCycleNum.md>) —— Introduced in SmartRDI 2.4.4
- [copyLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.06_copyLabel.md>) —— Introduced in SmartRDI 2.4.4
- [failCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.14_failCount.md>) —— Introduced in SmartRDI 2.4.4
- [failCyc()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.15_failCyc.md>) —— Introduced in SmartRDI 2.4.4
- [failNode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.16_failNode.md>) —— Introduced in SmartRDI 2.4.4
- [FFC()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.17_FFC.md>) —— Introduced in SmartRDI 2.4.4
- [insertJmpe()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.20_insertJmpe.md>) —— Introduced in SmartRDI 2.4.4
- [insertSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.21_insertSub.md>) —— Introduced in SmartRDI 2.4.4
- [label()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.22_label.md>) —— Introduced in SmartRDI 2.4.4
- [passNode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.25_passNode.md>) —— Introduced in SmartRDI 2.4.4
- [repeatSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.32_repeatSub.md>) —— Introduced in SmartRDI 2.4.4
- [getFailCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.43_getFailCount.md>) —— Introduced in SmartRDI 2.4.4
- [getFailCyc()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.44_getFailCyc.md>) —— Introduced in SmartRDI 2.4.4
- [getFFC()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.45_getFFC.md>) —— Introduced in SmartRDI 2.4.4


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 34 条**，涉及 **34 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
