---
type: version
title: SmartRDI 2.4.0 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.06_RDI_INFO_LEVEL.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.01_cont.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.10.01_burstPostfix.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.10.02_RDI_BURST_POSTFIX.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.10_Postfix_in_burst_pattern_names.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21.01_wait.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.02_Runtime_DC_waveform.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.08_wait.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.05_enPassFail.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.15_pin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.04_enPassFail.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.09_pin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.10_pin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.07_enPassFail.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.30_pin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.09_enPassFail.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.02_emapLocation.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.03_failCount.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.04_failCyc.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.05_FFC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.07_label.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.09_pfMap.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.10_rdi.func__.startVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.13_getFailCount.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.14_getFailCyc.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.15_getFFC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.16_getPfMap.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16_SmartRDI__Error_map_results_from_user_patterns.md
  # 本页共涉及 80 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.4.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（11 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.4.0:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.4.0: New keywords SETUP_UPTODATE and VEC_EDIT_MODE.
- [Code structure with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md>) —— SmartRDI 2.4.0: Support cont() to separate command lines.
- [RDI_INFO_LEVEL](<02_System_reference/02.07_Test_Method_Reference/02.07.13.06_RDI_INFO_LEVEL.md>) —— SmartRDI 2.4.0: Support RDI_INFO_LEVEL 2.
- [wait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21.01_wait.md>) —— SmartRDI 2.4.0: One option TA::WAIT_DCDGT is added.
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.15_pin.md>) —— SmartRDI 2.4.0: Supports a port name as a pin group.
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.09_pin.md>) —— SmartRDI 2.4.0: Supports a port name as a pin group.
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.10_pin.md>) —— SmartRDI 2.4.0: Support a port name as a pin group.
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.30_pin.md>) —— SmartRDI 2.4.0: Support a port name as a pin group.
- [burstLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md>) —— SmartRDI 2.4.0: A label name with or without an MD5 postfix option.
- [expectBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.12_expectBit.md>) —— SmartRDI 2.4.0: Support run-time expectBit().
- [expectData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.13_expectData.md>) —— SmartRDI 2.4.0: Support runtime expectData().


## 这一版新引入（69 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [cont()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.01_cont.md>) —— Introduced in SmartRDI 2.4.0
- [burstPostfix()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.10.01_burstPostfix.md>) —— Introduced in SmartRDI 2.4.0
- [RDI_BURST_POSTFIX](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.10.02_RDI_BURST_POSTFIX.md>) —— Introduced in SmartRDI 2.4.0
- [Postfix in burst pattern names](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.10_Postfix_in_burst_pattern_names.md>) —— Introduced in SmartRDI 2.4.0
- [Runtime DC waveform](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.02_Runtime_DC_waveform.md>) —— Introduced in SmartRDI 2.4.0
- [wait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.08_wait.md>) —— Introduced in SmartRDI 2.4.0
- [enPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.05_enPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [enPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.04_enPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [enPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.07_enPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [enPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.09_enPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [emapLocation()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.02_emapLocation.md>) —— Introduced in SmartRDI 2.4.0
- [failCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.03_failCount.md>) —— Introduced in SmartRDI 2.4.0
- [failCyc()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.04_failCyc.md>) —— Introduced in SmartRDI 2.4.0
- [FFC()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.05_FFC.md>) —— Introduced in SmartRDI 2.4.0
- [label()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.07_label.md>) —— Introduced in SmartRDI 2.4.0
- [pfMap()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.09_pfMap.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.func().startVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.10_rdi.func__.startVec.md>) —— Introduced in SmartRDI 2.4.0
- [getFailCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.13_getFailCount.md>) —— Introduced in SmartRDI 2.4.0
- [getFailCyc()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.14_getFailCyc.md>) —— Introduced in SmartRDI 2.4.0
- [getFFC()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.15_getFFC.md>) —— Introduced in SmartRDI 2.4.0
- [getPfMap()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.16_getPfMap.md>) —— Introduced in SmartRDI 2.4.0
- [SmartRDI: Error map results from user patterns](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16_SmartRDI__Error_map_results_from_user_patterns.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.func().labelRunTime()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.06_rdi.func__.labelRunTime.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.func().readMatchCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.09_rdi.func__.readMatchCount.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.func().readMatchPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.10_rdi.func__.readMatchPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.func().startVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.11_rdi.func__.startVec.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.id().getLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.15_rdi.id__.getLabel.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.id().getMatchCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.16_rdi.id__.getMatchCount.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.id().getMatchPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.17_rdi.id__.getMatchPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [Retrieving match loop results from user patterns](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.02_Retrieving_match_loop_results_from_user_patterns.md>) —— Introduced in SmartRDI 2.4.0
- [failNode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.01.01_failNode.md>) —— Introduced in SmartRDI 2.4.0
- [node()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.01.02_node.md>) —— Introduced in SmartRDI 2.4.0
- [passNode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.01.03_passNode.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.cogo().wait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.01.04_rdi.cogo__.wait.md>) —— Introduced in SmartRDI 2.4.0
- [Structures of multiple cogo() nodes](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.01_Structures_of_multiple_cogo___nodes.md>) —— Introduced in SmartRDI 2.4.0
- [init()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.01_init.md>) —— Introduced in SmartRDI 2.4.0
- [pathPin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.02_pathPin.md>) —— Introduced in SmartRDI 2.4.0
- [resolution()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.03_resolution.md>) —— Introduced in SmartRDI 2.4.0
- [search()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.04_search.md>) —— Introduced in SmartRDI 2.4.0
- [searchInput()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.05_searchInput.md>) —— Introduced in SmartRDI 2.4.0
- [start()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.06_start.md>) —— Introduced in SmartRDI 2.4.0
- [step()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.07_step.md>) —— Introduced in SmartRDI 2.4.0
- [stop()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.08_stop.md>) —— Introduced in SmartRDI 2.4.0
- [getSearchResult()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.11_getSearchResult.md>) —— Introduced in SmartRDI 2.4.0
- [Sequencer-controlled searching with cogo](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md>) —— Introduced in SmartRDI 2.4.0
- [SmartRDI: Pattern-based conditional jump - cogo](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19_SmartRDI__Pattern-based_conditional_jump_-_cogo.md>) —— Introduced in SmartRDI 2.4.0
- [CCTestMethod_SYNC](<02_System_reference/02.07_Test_Method_Reference/02.07.13.20.01_CCTestMethod_SYNC.md>) —— Introduced in SmartRDI 2.4.0
- [CCTestMethod_ISR](<02_System_reference/02.07_Test_Method_Reference/02.07.13.20.02_CCTestMethod_ISR.md>) —— Introduced in SmartRDI 2.4.0
- [SmartRDI: Testflow level burst and concurrency tests](<02_System_reference/02.07_Test_Method_Reference/02.07.13.20_SmartRDI__Testflow_level_burst_and_concurrency_tests.md>) —— Introduced in SmartRDI 2.4.0
- [rdi.tmu().enPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.03_rdi.tmu__.enPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [setGlobalVar()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.02.01_setGlobalVar.md>) —— Introduced in SmartRDI 2.4.0
- [getGlobalVar()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.02.02_getGlobalVar.md>) —— Introduced in SmartRDI 2.4.0
- [dtos()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.03_dtos.md>) —— Introduced in SmartRDI 2.4.0
- [itos()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.04_itos.md>) —— Introduced in SmartRDI 2.4.0
- [itos_hex()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.05_itos_hex.md>) —— Introduced in SmartRDI 2.4.0
- [reverseBits()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.06_reverseBits.md>) —— Introduced in SmartRDI 2.4.0
- [emapLocation()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.10_emapLocation.md>) —— Introduced in SmartRDI 2.4.0
- [enPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.11_enPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [instruction()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.01.01_instruction.md>) —— Introduced in SmartRDI 2.4.0
- [Inserting MACT and MRPT in a smartVec label](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.01_Inserting_MACT_and_MRPT_in_a_smartVec_label.md>) —— Introduced in SmartRDI 2.4.0
- [matchBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.02.01_matchBit.md>) —— Introduced in SmartRDI 2.4.0
- [matchCycle()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.02.02_matchCycle.md>) —— Introduced in SmartRDI 2.4.0
- [matchData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.02.03_matchData.md>) —— Introduced in SmartRDI 2.4.0
- [Creating a match loop pattern from logical data](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.02_Creating_a_match_loop_pattern_from_logical_data.md>) —— Introduced in SmartRDI 2.4.0
- [getMatchPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.03.02_getMatchPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [readMatchCount()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.03.03_readMatchCount.md>) —— Introduced in SmartRDI 2.4.0
- [readMatchPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.03.04_readMatchPassFail.md>) —— Introduced in SmartRDI 2.4.0
- [Retrieving match loop results](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.03_Retrieving_match_loop_results.md>) —— Introduced in SmartRDI 2.4.0
- [Match loop support](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49_Match_loop_support.md>) —— Introduced in SmartRDI 2.4.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 80 条**，涉及 **80 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
