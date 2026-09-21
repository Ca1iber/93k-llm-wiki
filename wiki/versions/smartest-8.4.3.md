---
type: version
title: SmarTest 8.4.3 — 版本页
tags: [version, smartest]
related: []
sources:
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.02_Using_the_Advantest_Software_Center.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.03_Downloading_and_installing_the_SmartInstall_add-on.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.04_Downloading_and_installing_SmarTest_software.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.05.01_Smart-install-3_command_examples.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.05_smart-install-3_command_line_tool.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.06_Searching_the_Software_Center.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.07_Downloading_SmarTest_software.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.08_Installing_software_products.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.09_Uninstalling_SmarTest_products.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01_Installing_SmarTest.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.04.01_Installing_SmarTest_Docker_images.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.04.02_Using_SmarTest_Docker_containers.md
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02.04_Running_SmarTest_in_a_container.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.02_Test_heads.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.03.02_DUT_Scale_interface.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.05_Sequencer-controlled_utility_lines.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05.04_Internal_Utility_Power_Option__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.11_Link_Scale_USB3_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.01_Pin_Scale_5000_card.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.03_Link_Scale_USB3_card.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.04_Bridge_Beam_Direct_Probe_for_special_WSRF__PMUX_and_WSMM__E8016BBMM.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.03_InstaCard_licensing.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.01.01.01_DUT_Scale_interface.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.01.01_PS1600_DC_offset.md
  - 03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 8.4.3

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（11 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 8.4.3:` 前缀，**那是原文的一部分，没有去掉**。

- [Test heads](<02_System_reference/02.03_DUT_board_design_reference/02.03.02_Test_heads.md>) —— SmarTest 7.6.2 / 7.10.1 / 8.4.3: Support of LX test head of V93000 EXA Scale systems.
- [DUT Scale interface](<02_System_reference/02.03_DUT_board_design_reference/02.03.03.02_DUT_Scale_interface.md>) —— SmarTest 8.4.3: Support of LX test head of V93000 EXA Scale systems.
- [Sequencer-controlled utility lines](<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05_Sequencer-controlled_utility_lines.md>) —— SmarTest 8.4.3: Support of LX test head of V93000 EXA Scale systems.
- [Internal Utility Power Option (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.05.04_Internal_Utility_Power_Option__V93000_EXA_Scale_systems.md>) —— SmarTest 8.4.3: Support of LX test head of V93000 EXA Scale systems.
- [PS5000 pogo pin assignment](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md>) —— SmarTest 8.4.3: Remote sensing is not applicable in SmarTest 8.4.3.
- [Utility pogo block - Basic configuration (V93000 EXA Scale systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.md>) —— SmarTest 8.4.3: Support of LX test head of V93000 EXA Scale systems.
- [Pin Scale 5000 card](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.01_Pin_Scale_5000_card.md>) —— SmarTest 8.4.3: Remote sensing is not applicable in SmarTest 8.4.3.
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md>) —— SmarTest 7.6.2 / 7.10.1 / 8.4.3: New design kit for the PMUX Wing Stiffener
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md>) —— SmarTest 7.6.2 / 7.10.1 / 8.4.3: New design kit for the PMUX Wing Stiffener
- [DUT Scale interface](<02_System_reference/02.05_Test_Head_Cards/02.05.01.01.01_DUT_Scale_interface.md>) —— SmarTest 8.4.3: Support of LX test head of V93000 EXA Scale systems.
- [Sequencer-controlled utility lines](<03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md>) —— SmarTest 8.4.3: Support of LX test head of V93000 EXA Scale systems.


## 这一版新引入（19 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Using the Advantest Software Center](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.02_Using_the_Advantest_Software_Center.md>) —— Introduced in SmarTest 8.4.3
- [Downloading and installing the SmartInstall add-on](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.03_Downloading_and_installing_the_SmartInstall_add-on.md>) —— Introduced in SmarTest 8.4.3
- [Downloading and installing SmarTest software](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.04_Downloading_and_installing_SmarTest_software.md>) —— Introduced in SmarTest 8.4.3
- [Smart-install-3 command examples](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.05.01_Smart-install-3_command_examples.md>) —— Introduced in SmarTest 8.4.3
- [smart-install-3 command line tool](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.05_smart-install-3_command_line_tool.md>) —— Introduced in SmarTest 8.4.3
- [Searching the Software Center](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.06_Searching_the_Software_Center.md>) —— Introduced in SmarTest 8.4.3
- [Downloading SmarTest software](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.07_Downloading_SmarTest_software.md>) —— Introduced in SmarTest 8.4.3
- [Installing software products](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.08_Installing_software_products.md>) —— Introduced in SmarTest 8.4.3
- [Uninstalling SmarTest products](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.09_Uninstalling_SmarTest_products.md>) —— Introduced in SmarTest 8.4.3
- [Installing SmarTest](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01_Installing_SmarTest.md>) —— Introduced in SmarTest 8.4.3
- [Installing SmarTest Docker images](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.04.01_Installing_SmarTest_Docker_images.md>) —— Introduced in SmarTest 8.4.3
- [Using SmarTest Docker containers](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.04.02_Using_SmarTest_Docker_containers.md>) —— Introduced in SmarTest 8.4.3
- [Running SmarTest in a container](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02.04_Running_SmarTest_in_a_container.md>) —— Introduced in SmarTest 8.4.3
- [Link Scale USB3 pogo pin assignment](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.11_Link_Scale_USB3_pogo_pin_assignment.md>) —— Introduced in SmarTest 8.4.3
- [DPS128 and UHC4 migration to XPS256](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md>) —— Introduced in SmarTest 7.10.1 / 8.4.3
- [Link Scale USB3 card](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.03_Link_Scale_USB3_card.md>) —— Introduced in SmarTest 8.4.3
- [Bridge Beam Direct Probe for special WSRF, PMUX and WSMM (E8016BBMM)](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.04_Bridge_Beam_Direct_Probe_for_special_WSRF__PMUX_and_WSMM__E8016BBMM.md>) —— Introduced in SmarTest 8.4.3
- [InstaCard licensing](<02_System_reference/02.04_Model_File_and_Licensing/02.04.03_InstaCard_licensing.md>) —— Introduced in SmarTest 8.4.3
- [PS1600 DC offset](<02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.01.01_PS1600_DC_offset.md>) —— Introduced in SmarTest 8.4.3


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 30 条**，涉及 **30 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
