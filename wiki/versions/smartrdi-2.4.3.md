---
type: version
title: SmartRDI 2.4.3 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04.02_getRdiConfig.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.01_cont.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.01_getBuildDate.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.13.04_RDI_SEMI_PARALLEL_TEST_BEGIN.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.13.05_RDI_SEMI_PARALLEL_TEST_END.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.13_Semi-parallel_tests_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.16.01_rdi.disableWarning.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.16.02_rdi.enableWarning.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.04_repeat.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.04_sampleCycle.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.07_viMeas.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.10_getCurrentWaveform.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.11_getVoltageWaveform.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04_Using_a_DC_resource_as_a_digitizer_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.07_iMeasRange.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.20_insertSub.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.04_addVecRange.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.02_rdi.func__.burstId.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.04_search.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.09_getSearchFallResult.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.10_getSearchPath.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.12_getSearchRiseResult.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.10_rdi.tmu__.measNum.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.07_defaultBit.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.18_fillBit.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.33_rdi.smartVec__.vecEditMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.42_xMode.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.4.3

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（13 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.4.3:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.4.3: New keywords ANALOG_SET_NAME_MD5, BURST_NAME_MD5, REPORT_RESULT_IN_SINGLE_MODE, and VEC_MODE_SAMPLING_WAIT.
- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.4.3: Support the generation of an RDI_Configure.Template file in the testmethod folder in the first run.
- [cont()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.01_cont.md>) —— SmartRDI 2.4.3: cont() supports addVecRange().
- [sampleCycle()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.04_sampleCycle.md>) —— SmartRDI 2.4.3: Minimum cylces for new function viMeas() added.
- [Using a DC resource as a digitizer with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04_Using_a_DC_resource_as_a_digitizer_with_SmartRDI.md>) —— SmartRDI 2.4.3: New functions viMeas(), getCurrentWaveform(), getVoltageWaveform().
- [insertSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.20_insertSub.md>) —— SmartRDI 2.4.3: Support for inserting subroutines with PPMU or BADC actions into an existing pattern.
- [addVecRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.04_addVecRange.md>) —— SmartRDI 2.4.3: Support cont() and a parameter list.
- [rdi.func().burstId()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.02_rdi.func__.burstId.md>) —— SmartRDI 2.4.3: Support a port ID.
- [search()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.04_search.md>) —— SmartRDI 2.4.3: Supported hysteresis linear search with a new HYST_LINEAR type.
- [Sequencer-controlled searching with cogo](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md>) —— SmartRDI 2.4.3: Support hysteresis linear searches.
- [defaultBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.07_defaultBit.md>) —— SmartRDI 2.4.3: Support for writing a string into a pattern.
- [fillBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.18_fillBit.md>) —— SmartRDI 2.4.3: Support for writing a string into a pattern.
- [xMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.42_xMode.md>) —— SmartRDI 2.4.3: Support for data crossing over device cycles and combining string into the vector.


## 这一版新引入（17 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [getRdiConfig()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04.02_getRdiConfig.md>) —— Introduced in SmartRDI 2.4.3
- [getBuildDate()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.01_getBuildDate.md>) —— Introduced in SmartRDI 2.4.3
- [RDI_SEMI_PARALLEL_TEST_BEGIN()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.13.04_RDI_SEMI_PARALLEL_TEST_BEGIN.md>) —— Introduced in SmartRDI 2.4.3
- [RDI_SEMI_PARALLEL_TEST_END()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.13.05_RDI_SEMI_PARALLEL_TEST_END.md>) —— Introduced in SmartRDI 2.4.3
- [Semi-parallel tests with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.13_Semi-parallel_tests_with_SmartRDI.md>) —— Introduced in SmartRDI 2.4.3
- [rdi.disableWarning()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.16.01_rdi.disableWarning.md>) —— Introduced in SmartRDI 2.4.3
- [rdi.enableWarning()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.16.02_rdi.enableWarning.md>) —— Introduced in SmartRDI 2.4.3
- [repeat()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.04_repeat.md>) —— Introduced in SmartRDI 2.4.3
- [viMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.07_viMeas.md>) —— Introduced in SmartRDI 2.4.3
- [getCurrentWaveform()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.10_getCurrentWaveform.md>) —— Introduced in SmartRDI 2.4.3
- [getVoltageWaveform()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.11_getVoltageWaveform.md>) —— Introduced in SmartRDI 2.4.3
- [iMeasRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.07_iMeasRange.md>) —— Introduced in SmartRDI 2.4.3
- [getSearchFallResult()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.09_getSearchFallResult.md>) —— Introduced in SmartRDI 2.4.3
- [getSearchPath()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.10_getSearchPath.md>) —— Introduced in SmartRDI 2.4.3
- [getSearchRiseResult()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.12_getSearchRiseResult.md>) —— Introduced in SmartRDI 2.4.3
- [rdi.tmu().measNum()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.10_rdi.tmu__.measNum.md>) —— Introduced in SmartRDI 2.4.3
- [rdi.smartVec().vecEditMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.33_rdi.smartVec__.vecEditMode.md>) —— Introduced in SmartRDI 2.4.3


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 30 条**，涉及 **29 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
