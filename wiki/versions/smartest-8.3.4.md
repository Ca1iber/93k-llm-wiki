---
type: version
title: SmarTest 8.3.4 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.03.02_DUT_Scale_interface.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.03.04_Remote_control_unit__V93000_EXA_Scale_system.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.02.01_Utility_lines__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.06_Setting_up_sequencer_control_of_utility_lines.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.05_Sequencer-controlled_utility_lines.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05.01_Utility_power_supply_-_UP5V_pins__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05.02_Utility_power_supply_-_XP_pins__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05.03_Utility_power_supply_-_UPP15V___UPM15V___F24V_pins__V93000_EXA_Scale_sys.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05.04_Internal_Utility_Power_Option__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05_Utility_power_supplies.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.09_E8023PK_pogo_cable_assembly__4_VHD_pogo_blocks__DPS128.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07.01_XPS256_pogo_cable_assembly_EK751HDA__16_HD_pogo_blocks__256_channels.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07.02_XPS256_pogo_cable_assembly_EK751VHDA__8_VHD_pogo_blocks__256_channels.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02_Pogo_pin_assignment_-_DC_Scale_cards.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.09.01_Internal_Utility_Power_Option_pogo_pin_assignments__V93000_EXA_Scale_sys.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.01.03_Connecting_DPS_channels_in_parallel.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.02_HV_protection_-_Compliance_range.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.02.02_DPS128___DPS64_recommendations_for_use.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.01_XPS256_pogo_pins.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.02_XPS256_capacitor_requirements.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.03_XPS256_recommendations_for_use.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md
  # 本页共涉及 41 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 8.3.4

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（17 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 8.3.4:` 前缀，**那是原文的一部分，没有去掉**。

- [DUT interface layout](<02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md>) —— SmarTest 8.3.4: Alternate UTIL and DPS pogo block numbers for V93000 EXA Scale systems added.
- [DUT Scale interface](<02_System_reference/02.03_DUT_board_design_reference/02.03.03.02_DUT_Scale_interface.md>) —— SmarTest 7.6.0 / 8.3.4: Support of V93000 EXA Scale test heads.
- [Utility line characteristics](<02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md>) —— SmarTest 8.3.4: Utility line characteristics for V93000 EXA Scale systems added
- [Setting up sequencer control of utility lines](<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.06_Setting_up_sequencer_control_of_utility_lines.md>) —— SmarTest 8.3.4: Support of sequencer‑controlled utility lines on V93000 EXA Scale systems.
- [Sequencer-controlled utility lines](<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05_Sequencer-controlled_utility_lines.md>) —— SmarTest 8.3.4: Support of sequencer‑controlled utility lines on V93000 EXA Scale systems.
- [Utility power supplies](<02_System_reference/02.03_DUT_board_design_reference/02.03.05_Utility_power_supplies.md>) —— SmarTest 8.3.4: Utility power supplies for V93000 EXA Scale systems added
- [DPS128… DPS64 pogo cable assemblies and pogo pin assignments](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md>) —— SmarTest 7.5.4 / 8.3.4: Support of E8023PB and E8023PK VHD pogo cable assemblies
- [Pogo pin assignment - DC Scale cards](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.02_Pogo_pin_assignment_-_DC_Scale_cards.md>) —— SmarTest 7.6.0 / 8.3.4: DC Scale XPS256 card added.
- [Pogo pin assignment - Utility pogo blocks](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.md>) —— SmarTest 8.3.4: Utility pogo pin layout for V93000 EXA Scale systems added
- [Connecting DPS channels in parallel](<02_System_reference/02.03_DUT_board_design_reference/02.03.07.01.03_Connecting_DPS_channels_in_parallel.md>) —— SmarTest 7.10.1 / 8.3.4: DC Scale XPS256 card added.
- [HV protection - Compliance range](<02_System_reference/02.03_DUT_board_design_reference/02.03.07.03.02_HV_protection_-_Compliance_range.md>) —— SmarTest 7.6.0 / 8.3.4: DC Scale XPS256 card added.
- [Wave Scale RF PCB layout and stiffener info for Direct-Probe](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.23_Wave_Scale_RF_PCB_layout_and_stiffener_info_for_Direct-Probe.md>) —— SmarTest 7.6.0 / 8.3.4: Drawing N2605-64170 updated from rev. E to rev. G
- [DUT Scale interface](<02_System_reference/02.05_Test_Head_Cards/02.05.01.01.01_DUT_Scale_interface.md>) —— SmarTest 7.6.0 / 8.3.4: Support of V93000 EXA Scale test heads.
- [DPS128… DPS64 pogo cable assemblies and pogo pin assignments](<02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md>) —— SmarTest 7.5.4 / 8.3.4: Support of E8023PB and E8023PK VHD pogo cable assemblies
- [DPS128 and DPS64 pogo cabling and model file configuration](<02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.md>) —— SmarTest 7.5.4 / 8.3.4: Support of E8023PB and E8023PK VHD pogo cable assemblies
- [Setting up sequencer control of utility lines](<03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01.05_Setting_up_sequencer_control_of_utility_lines.md>) —— SmarTest 8.3.4: Support of sequencer‑controlled utility lines on V93000 EXA Scale systems.
- [Sequencer-controlled utility lines](<03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md>) —— SmarTest 8.3.4: Support of sequencer‑controlled utility lines on V93000 EXA Scale systems.


## 这一版新引入（24 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Remote control unit (V93000 EXA Scale system)](<02_System_reference/02.03_DUT_board_design_reference/02.03.03.04_Remote_control_unit__V93000_EXA_Scale_system.md>) —— Introduced in SmarTest 7.6.0 / 8.3.4
- [Utility lines (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.04.02.01_Utility_lines__V93000_EXA_Scale_systems.md>) —— Introduced in SmarTest 7.10.0 / 8.3.4
- [Utility power supply - UP5V pins (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.05.01_Utility_power_supply_-_UP5V_pins__V93000_EXA_Scale_systems.md>) —— Introduced in SmarTest 7.10.0 / 8.3.4
- [Utility power supply - XP pins (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.05.02_Utility_power_supply_-_XP_pins__V93000_EXA_Scale_systems.md>) —— Introduced in SmarTest 7.10.0 / 8.3.4
- [Utility power supply - UPP15V / UPM15V / F24V pins (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.05.03_Utility_power_supply_-_UPP15V___UPM15V___F24V_pins__V93000_EXA_Scale_sys.md>) —— Introduced in SmarTest 7.10.0 / 8.3.4
- [Internal Utility Power Option (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.05.04_Internal_Utility_Power_Option__V93000_EXA_Scale_systems.md>) —— Introduced in SmarTest 8.3.4
- [E8023PB pogo cable assembly: 2 VHD pogo blocks](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks.md>) —— Introduced in SmarTest 7.5.4 / 8.3.4
- [E8023PK pogo cable assembly: 4 VHD pogo blocks (DPS128)](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.09_E8023PK_pogo_cable_assembly__4_VHD_pogo_blocks__DPS128.md>) —— Introduced in SmarTest 7.5.4 / 8.3.4
- [XPS256 pogo cable assembly EK751HDA: 16 HD pogo blocks, 256 channels](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07.01_XPS256_pogo_cable_assembly_EK751HDA__16_HD_pogo_blocks__256_channels.md>) —— Introduced in SmarTest 8.3.4
- [XPS256 pogo cable assembly EK751VHDA: 8 VHD pogo blocks, 256 channels](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07.02_XPS256_pogo_cable_assembly_EK751VHDA__8_VHD_pogo_blocks__256_channels.md>) —— Introduced in SmarTest 8.3.4
- [XPS256 pogo pin assignment](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md>) —— Introduced in SmarTest 7.10.1 / 8.3.4
- [Utility pogo block - Basic configuration (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.md>) —— Introduced in SmarTest 8.3.4
- [Utility pogo block - Utility Card (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md>) —— Introduced in SmarTest 8.3.4
- [Internal Utility Power Option pogo pin assignments (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.09.01_Internal_Utility_Power_Option_pogo_pin_assignments__V93000_EXA_Scale_sys.md>) —— Introduced in SmarTest 8.3.4
- [DPS128 / DPS64 recommendations for use](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.02.02_DPS128___DPS64_recommendations_for_use.md>) —— Introduced in SmarTest 7.6.0 / 8.3.4
- [XPS256 pogo pins](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.01_XPS256_pogo_pins.md>) —— Introduced in SmarTest 8.3.4
- [XPS256 capacitor requirements](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.02_XPS256_capacitor_requirements.md>) —— Introduced in SmarTest 8.3.4
- [XPS256 recommendations for use](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.03_XPS256_recommendations_for_use.md>) —— Introduced in SmarTest 7.6.0 / 8.3.4
- [XPS256 VHD pogo pad and via design](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md>) —— Introduced in SmarTest 8.3.4
- [XPS256 ganged wiring](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.05_XPS256_ganged_wiring.md>) —— Introduced in SmarTest 8.3.4
- [DC Scale XPS256 card](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07_DC_Scale_XPS256_card.md>) —— Introduced in SmarTest 8.3.4
- [MUX cards layout recommendations](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.05_MUX_cards_layout_recommendations.md>) —— Introduced in SmarTest 7.5.4 / 8.3.4
- [E8023PB pogo cable assembly: 2 VHD pogo blocks](<02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks.md>) —— Introduced in SmarTest 7.5.4 / 8.3.4
- [E8023PK pogo cable assembly: 4 VHD pogo blocks (DPS128)](<02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.09_E8023PK_pogo_cable_assembly__4_VHD_pogo_blocks__DPS128.md>) —— Introduced in SmarTest 7.5.4 / 8.3.4


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 41 条**，涉及 **41 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
