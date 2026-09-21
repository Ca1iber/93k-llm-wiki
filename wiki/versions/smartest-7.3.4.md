---
type: version
title: SmarTest 7.3.4 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.02_Test_heads.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.03.02_DUT_Scale_interface.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.06.03_UHC4___UHC4T_pogo_cable_assembly__E8024UHPS.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.03_MUX_cards_pogo_block_numbering.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.01.01.01_DUT_Scale_interface.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.01.01.02_Scalable_A-Class_test_head.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.01.01_Test_heads.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.177_PDMM__-__PDps_Miscellaneous_Measurement.md
  - 02_System_reference/02.06_Command_Reference/02.06.10.02.09_PDMM__-__PDps_Miscellaneous_Measurement.md
  - 02_System_reference/02.06_Command_Reference/02.06.13.01.05_Dealing_with_very_high_data_rates.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.33_CCTsetExecMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.44_SMC_SYNCHRONIZE_WITHOUT_BINNING.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.47_SMC_TMU_UPLOAD_APP_RESULTS.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.48_SMC_TMU_UPLOAD_PERIOD_RESULTS.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.49_SMC_TMU_UPLOAD_RAW_RESULTS.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.62_ERROR_MAP_TEST.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.02.01_Continuity.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.01_Recipe_file.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.3.4

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（20 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.3.4:` 前缀，**那是原文的一部分，没有去掉**。

- [Test heads](<02_System_reference/02.03_DUT_board_design_reference/02.03.02_Test_heads.md>) —— SmarTest 7.3.4: Support of Scalable A-Class.
- [DUT Scale interface](<02_System_reference/02.03_DUT_board_design_reference/02.03.03.02_DUT_Scale_interface.md>) —— SmarTest 7.3.4: Support of Scalable A-Class.
- [MUX cards pogo block numbering](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.03_MUX_cards_pogo_block_numbering.md>) —— SmarTest 7.3.4: New definition of the MUX cards in the model file.
- [GLOBAL section](<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md>) —— SmarTest 7.3.4: New definition: mux_boards
- [DUT Scale interface](<02_System_reference/02.05_Test_Head_Cards/02.05.01.01.01_DUT_Scale_interface.md>) —— SmarTest 7.3.4: Support of Scalable A-Class.
- [Test heads](<02_System_reference/02.05_Test_Head_Cards/02.05.01.01_Test_heads.md>) —— SmarTest 7.3.4: Support of Scalable A-Class.
- [PDMM? - (PDps Miscellaneous Measurement)](<02_System_reference/02.06_Command_Reference/02.06.02.02.177_PDMM__-__PDps_Miscellaneous_Measurement.md>) —— SmarTest 7.3.4: New extra parameter PRLT introduced in patch 4.
- [PDMM? - (PDps Miscellaneous Measurement)](<02_System_reference/02.06_Command_Reference/02.06.10.02.09_PDMM__-__PDps_Miscellaneous_Measurement.md>) —— SmarTest 7.3.4: New extra parameter PRLT introduced in patch 4.
- [Dealing with very high data rates](<02_System_reference/02.06_Command_Reference/02.06.13.01.05_Dealing_with_very_high_data_rates.md>) —— SmarTest 7.3.4: For Pin Scale SL and 1600 ME, input signal for the event discarding block has a different valid range 5.5 to 6.75ns instead of 3.6 to 4.4ns
- [CCTsetExecMode](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.33_CCTsetExecMode.md>) —— SmarTest 7.3.4: New execution mode EXM_START_TEST.
- [SMC_SYNCHRONIZE_WITHOUT_BINNING()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.44_SMC_SYNCHRONIZE_WITHOUT_BINNING.md>) —— SmarTest 7.3.4: Introduced in patch 1.
- [SMC_TEST()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.md>) —— SmarTest 7.3.4: Patch 4 - New string parameter "testtest"
- [SMC_TMU_UPLOAD_APP_RESULTS()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.47_SMC_TMU_UPLOAD_APP_RESULTS.md>) —— SmarTest 7.3.4: Added new parameter site.
- [SMC_TMU_UPLOAD_PERIOD_RESULTS()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.48_SMC_TMU_UPLOAD_PERIOD_RESULTS.md>) —— SmarTest 7.3.4: Added new parameter site.
- [SMC_TMU_UPLOAD_RAW_RESULTS()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.49_SMC_TMU_UPLOAD_RAW_RESULTS.md>) —— SmarTest 7.3.4: Added new parameter site.
- [TMLimits](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md>) —— SmarTest 7.3.4: New parameters for the load member function: LIMIT_WARNING_LEVEL
- [ERROR_MAP_TEST](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.62_ERROR_MAP_TEST.md>) —— SmarTest 7.3.4: Added new member function prepareForTest().
- [Continuity](<02_System_reference/02.07_Test_Method_Reference/02.07.05.02.01_Continuity.md>) —— SmarTest 7.3.4: New test flow variable CommutVtOffset introduced in patch 4.
- [Recipe file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.01_Recipe_file.md>) —— SmarTest 7.3.4: Added the rdi_version child element for the smartest element.
- [Recipe file](<02_System_reference/02.09_Test_Program_Management/02.09.01.17.10.01_Recipe_file.md>) —— SmarTest 7.3.4: Add the auto_start_lot attribute for the recipe element.


## 这一版新引入（2 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [UHC4 / UHC4T pogo cable assembly: E8024UHPS](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.06.03_UHC4___UHC4T_pogo_cable_assembly__E8024UHPS.md>) —— Introduced in SmarTest 7.3.4
- [Scalable A-Class test head](<02_System_reference/02.05_Test_Head_Cards/02.05.01.01.02_Scalable_A-Class_test_head.md>) —— Introduced in SmarTest 7.3.4


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 22 条**，涉及 **21 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
