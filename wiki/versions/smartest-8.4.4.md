---
type: version
title: SmarTest 8.4.4 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.05.01.01_Installing_HD_pins_to_Accretech_prober_s_headstage.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.09_Semics_OPUS3_compatibility.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.01_Direct-Probe_probe_card_layout_information.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.21_Wave_Scale_MM_PCB_layout_and_stiffener_info_for_Direct-Probe.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.22_Wave_Scale_MM_PCB_layout_and_stiffener_info_for_final_test.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.25_Stiffener_and_PCB_layout__Keep-out-zone_KOZ___for_Bridge_Beam_Direct_Pro.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.01.01_PS1600_DC_offset.md
  - 02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.05.01_Adding_a_project_to_the_Java_build_path.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 8.4.4

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（10 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 8.4.4:` 前缀，**那是原文的一部分，没有去掉**。

- [Utility pogo block - Basic configuration (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.md>) —— SmarTest 7.10.2 / 8.4.4: Block 1, pin c15 changed from "UGND" to "NC".
- [Utility pogo block - Utility Card (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md>) —— SmarTest 7.10.2 / 8.4.4: Block 1, pin c15 changed from "UGND" to "PGND".
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md>) —— SmarTest 7.6.2 / 7.10.3 / 8.4.4: Updated "Direct-Probe PMUX design kit" E8021-64170 from revision F to revision 8.
- [Direct-Probe probe card layout information](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.01_Direct-Probe_probe_card_layout_information.md>) —— SmarTest 7.6.2 / 7.10.2 / 8.4.4: Drawing N2360-90119 updated from revision D to revision 5.
- [Direct-Probe probe card layout information](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.01_Direct-Probe_probe_card_layout_information.md>) —— SmarTest 7.6.2 / 7.10.2 / 8.4.4: Drawing N2360-90120 updated from revision D to revision E.
- [Direct-Probe stiffener](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md>) —— SmarTest 7.6.2 / 7.10.2 / 8.4.4: Package "N2360-61097_H FABRICATION PACKAGE" updated to version "..._2021-06-02": N2360-90119 updated from revision D to revision 5. N2360-90120 updated from revision D to revision E.
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md>) —— SmarTest 7.6.2 / 7.10.3 / 8.4.4: Updated "Direct-Probe PMUX design kit" E8021-64170 from revision F to revision 8.
- [Wave Scale MM PCB layout and stiffener info for Direct-Probe](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.21_Wave_Scale_MM_PCB_layout_and_stiffener_info_for_Direct-Probe.md>) —— SmarTest 8.4.4: Direct-probe WSMM probe card specifications E8027-96570 updated from version "B" to "B_(2019-04-09)_2": Changes on pages 4, 5, and 8.
- [Wave Scale MM PCB layout and stiffener info for final test](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.22_Wave_Scale_MM_PCB_layout_and_stiffener_info_for_final_test.md>) —— SmarTest 8.4.4: File names of package E8027-96550_A_(2019-09-26).zip corrected. Content of the files not changed.
- [PS1600 DC offset](<02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.01.01_PS1600_DC_offset.md>) —— SmarTest 8.4.4: Addition of two test program configuration variables to control the pull-down of PS1600(B) signals.


## 这一版新引入（4 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Installing HD pins to Accretech prober's headstage](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.05.01.01_Installing_HD_pins_to_Accretech_prober_s_headstage.md>) —— Introduced in SmarTest 8.4.4
- [Semics OPUS3 compatibility](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.09_Semics_OPUS3_compatibility.md>) —— Introduced in SmarTest 8.4.4
- [Stiffener and PCB layout (Keep-out-zone[KOZ]) for Bridge Beam Direct Probe for special WSRF, PMUX and WSMM (E8016BBMM)](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.25_Stiffener_and_PCB_layout__Keep-out-zone_KOZ___for_Bridge_Beam_Direct_Pro.md>) —— Introduced in SmarTest 8.4.4
- [Adding a project to the Java build path](<02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.05.01_Adding_a_project_to_the_Java_build_path.md>) —— Introduced in SmarTest 8.4.4


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 14 条**，涉及 **13 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
