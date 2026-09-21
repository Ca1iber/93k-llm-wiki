---
type: version
title: SmarTest 8.2.5 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.01.01_Parts_list_for_RF_Pure_Clock_card.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.01_RF_Pure_Clock_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.02_WSMM_Card_Cage_pogo_via_design.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01_WSMM_Card_Cage_DUT_Interface.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.02.01_WSMM_Family_Board_E8027FAA_pogo_block_mapping.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.02.02_WSMM_Family_Board_E8027FAA_pogo_pin_mapping.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.02_WSMM_Family_Board_E8027FAA.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02_Wave_Scale_Millimeter_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01_Electrical_design_rules_-_DC_Scale_cards.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.02_Electrical_design_rules_-_DPS-slot_power_supplies.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.03_Electrical_design_rules_-_Digital_cards.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.05_Electrical_design_rules_-_Other_cards__DUT_interfaces__systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08_Electrical_design__Product-specific_rules.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.21_Wave_Scale_MM_PCB_layout_and_stiffener_info_for_Direct-Probe.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.22_Wave_Scale_MM_PCB_layout_and_stiffener_info_for_final_test.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.10.02_Activating_licenses_advanced.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.10_Activating_licenses.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.13.02.02_Uninstalling_the_FNE_license_client.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.13.03_FlexNet_Embedded_license_administration.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.13.04_Monitoring_license_servers_using_the_FNE_Server_Viewer.md
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 8.2.5

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（4 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 8.2.5:` 前缀，**那是原文的一部分，没有去掉**。

- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md>) —— SmarTest 7.5.2 / 8.2.5: E8021-64100_..._DesignKit_MUXStiffener.zip: E8021-24100 updated to revision D
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md>) —— SmarTest 7.5.2 / 8.2.5: E8021-96520_A_DesignKit_PMUX_DUT_board.zip: New files E8021-96520_A.pdf, E8021-96520_A_sheet_#.dxf, E8021-96520_A.ami, E8021-96520_A.pkg
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md>) —— SmarTest 7.5.2 / 8.2.5: E8021-64100_..._DesignKit_MUXStiffener.zip: E8021-24100 updated to revision D
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md>) —— SmarTest 7.5.2 / 8.2.5: E8021-96520_A_DesignKit_PMUX_DUT_board.zip: New files E8021-96520_A.pdf, E8021-96520_A_sheet_#.dxf, E8021-96520_A.ami, E8021-96520_A.pkg


## 这一版新引入（22 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Parts list for RF Pure Clock card](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.01.01_Parts_list_for_RF_Pure_Clock_card.md>) —— Introduced in SmarTest 8.2.5
- [RF Pure Clock pogo pin assignment](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.01_RF_Pure_Clock_pogo_pin_assignment.md>) —— Introduced in SmarTest 8.2.5
- [WSMM Card Cage RFIM18 / RFIM6 channel transformation](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md>) —— Introduced in SmarTest 8.2.5
- [WSMM Card Cage pogo via design](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.02_WSMM_Card_Cage_pogo_via_design.md>) —— Introduced in SmarTest 8.2.5
- [WSMM Card Cage DUT Interface](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01_WSMM_Card_Cage_DUT_Interface.md>) —— Introduced in SmarTest 8.2.5
- [WSMM Family Board E8027FAA pogo block mapping](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.02.01_WSMM_Family_Board_E8027FAA_pogo_block_mapping.md>) —— Introduced in SmarTest 8.2.5
- [WSMM Family Board E8027FAA pogo pin mapping](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.02.02_WSMM_Family_Board_E8027FAA_pogo_pin_mapping.md>) —— Introduced in SmarTest 8.2.5
- [WSMM Family Board E8027FAA](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.02_WSMM_Family_Board_E8027FAA.md>) —— Introduced in SmarTest 8.2.5
- [Wave Scale Millimeter pogo pin assignment](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02_Wave_Scale_Millimeter_pogo_pin_assignment.md>) —— Introduced in SmarTest 8.2.5
- [Electrical design rules - DC Scale cards](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01_Electrical_design_rules_-_DC_Scale_cards.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Electrical design rules - DPS-slot power supplies](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.02_Electrical_design_rules_-_DPS-slot_power_supplies.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Electrical design rules - Digital cards](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.03_Electrical_design_rules_-_Digital_cards.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Electrical design rules - Other cards, DUT interfaces, systems](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.05_Electrical_design_rules_-_Other_cards__DUT_interfaces__systems.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Electrical design: Product-specific rules](<02_System_reference/02.03_DUT_board_design_reference/02.03.08_Electrical_design__Product-specific_rules.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Wave Scale MM PCB layout and stiffener info for Direct-Probe](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.21_Wave_Scale_MM_PCB_layout_and_stiffener_info_for_Direct-Probe.md>) —— Introduced in SmarTest 8.2.5
- [Wave Scale MM PCB layout and stiffener info for final test](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.22_Wave_Scale_MM_PCB_layout_and_stiffener_info_for_final_test.md>) —— Introduced in SmarTest 8.2.5
- [Activating licenses advanced](<02_System_reference/02.04_Model_File_and_Licensing/02.04.10.02_Activating_licenses_advanced.md>) —— Introduced in SmarTest 8.2.5
- [Activating licenses](<02_System_reference/02.04_Model_File_and_Licensing/02.04.10_Activating_licenses.md>) —— Introduced in SmarTest 8.2.5
- [Uninstalling the FNE license client](<02_System_reference/02.04_Model_File_and_Licensing/02.04.13.02.02_Uninstalling_the_FNE_license_client.md>) —— Introduced in SmarTest 8.2.5
- [FlexNet Embedded license administration](<02_System_reference/02.04_Model_File_and_Licensing/02.04.13.03_FlexNet_Embedded_license_administration.md>) —— Introduced in SmarTest 8.2.5
- [Monitoring license servers using the FNE Server Viewer](<02_System_reference/02.04_Model_File_and_Licensing/02.04.13.04_Monitoring_license_servers_using_the_FNE_Server_Viewer.md>) —— Introduced in SmarTest 8.2.5
- [SmartShell](<02_System_reference/02.15_SmartShell/02.15_SmartShell.md>) —— Introduced in SmarTest 8.2.5


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 26 条**，涉及 **24 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
