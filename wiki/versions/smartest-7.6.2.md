---
type: version
title: SmarTest 7.6.2 — 版本页
tags: [version, smartest]
related: []
sources:
  - 01_Getting_started/01.02_SmarTest_workstation_administration/01.02_SmarTest_workstation_administration.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.02_Test_heads.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.01_Direct-Probe_probe_card_layout_information.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.04_INTERFACE_SECTION_section.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.11.01_Enabling_modern_C___support_for_SmarTest_7.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.190.08_Result_areas_and_vector_memory_consumption.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.01.01_Virtual_Machine_page.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.01.02_Tester_Booking_page.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.01.03_SSH_Key_page.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.01.04_Opening_the_TE-Cloud_dashboard.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.01_The_TE-Cloud_dashboard.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.02.01_Knowledge_Base.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.02.02_My_Area.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.02.03_Ticket_submission_page.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.02.04_Opening_the_help_center.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.02.05_Submitting_a_ticket.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.02.06_Replying_to_a_ticket.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.02.07_Closing_a_ticket.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.02_Help_Center.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.03.01_Generating_and_saving_key_files.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.03.02_Creating_a_TE-Cloud_virtual_machine.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.03.03_Configuring_a_remote_connection_to_a_virtual_machine.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.03.04_Connecting_to_a_virtual_machine_via_SSH.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.03.05_Setting_up_a_VNC_connection.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.03.06_Connecting_to_a_virtual_machine_via_VNC.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.03.07_Setting_up_a_site_to_transmit_files_to_and_from_the_virtual_machine_base.md
  - 02_System_reference/02.16_ACS_TE-Cloud/02.16.03.08_Transmitting_files_between_Linux_machines_with_command_line.md
  # 本页共涉及 45 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.6.2

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（10 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.6.2:` 前缀，**那是原文的一部分，没有去掉**。

- [Test heads](<02_System_reference/02.03_DUT_board_design_reference/02.03.02_Test_heads.md>) —— SmarTest 7.6.2 / 7.10.1 / 8.4.3: Support of LX test head of V93000 EXA Scale systems.
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md>) —— SmarTest 7.6.2 / 7.10.1 / 8.4.3: New design kit for the PMUX Wing Stiffener
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md>) —— SmarTest 7.6.2 / 7.10.3 / 8.4.4: Updated "Direct-Probe PMUX design kit" E8021-64170 from revision F to revision 8.
- [Direct-Probe probe card layout information](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.01_Direct-Probe_probe_card_layout_information.md>) —— SmarTest 7.6.2 / 7.10.2 / 8.4.4: Drawing N2360-90119 updated from revision D to revision 5.
- [Direct-Probe probe card layout information](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.01_Direct-Probe_probe_card_layout_information.md>) —— SmarTest 7.6.2 / 7.10.2 / 8.4.4: Drawing N2360-90120 updated from revision D to revision E.
- [Direct-Probe stiffener](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md>) —— SmarTest 7.6.2 / 7.10.2 / 8.4.4: Package "N2360-61097_H FABRICATION PACKAGE" updated to version "..._2021-06-02": N2360-90119 updated from revision D to revision 5. N2360-90120 updated from revision D to revision E.
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md>) —— SmarTest 7.6.2 / 7.10.1 / 8.4.3: New design kit for the PMUX Wing Stiffener
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md>) —— SmarTest 7.6.2 / 7.10.3 / 8.4.4: Updated "Direct-Probe PMUX design kit" E8021-64170 from revision F to revision 8.
- [INTERFACE_SECTION section](<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.04_INTERFACE_SECTION_section.md>) —— SmarTest 7.6.2: SICL removed
- [Enabling modern C++ support for SmarTest 7](<02_System_reference/02.07_Test_Method_Reference/02.07.02.11.01_Enabling_modern_C___support_for_SmarTest_7.md>) —— SmarTest 7.6.2: GNU Compiler Collection (GCC) version 10 support.


## 这一版新引入（38 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [SmarTest workstation administration](<01_Getting_started/01.02_SmarTest_workstation_administration/01.02_SmarTest_workstation_administration.md>) —— Introduced in SmarTest 7.6.2
- [Result areas and vector memory consumption](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.190.08_Result_areas_and_vector_memory_consumption.md>) —— Introduced in SmarTest 7.6.2
- [Virtual Machine page](<02_System_reference/02.16_ACS_TE-Cloud/02.16.01.01_Virtual_Machine_page.md>) —— Introduced in SmarTest 7.6.2
- [Tester Booking page](<02_System_reference/02.16_ACS_TE-Cloud/02.16.01.02_Tester_Booking_page.md>) —— Introduced in SmarTest 7.6.2
- [SSH Key page](<02_System_reference/02.16_ACS_TE-Cloud/02.16.01.03_SSH_Key_page.md>) —— Introduced in SmarTest 7.6.2
- [Opening the TE-Cloud dashboard](<02_System_reference/02.16_ACS_TE-Cloud/02.16.01.04_Opening_the_TE-Cloud_dashboard.md>) —— Introduced in SmarTest 7.6.2
- [The TE-Cloud dashboard](<02_System_reference/02.16_ACS_TE-Cloud/02.16.01_The_TE-Cloud_dashboard.md>) —— Introduced in SmarTest 7.6.2
- [Knowledge Base](<02_System_reference/02.16_ACS_TE-Cloud/02.16.02.01_Knowledge_Base.md>) —— Introduced in SmarTest 7.6.2
- [My Area](<02_System_reference/02.16_ACS_TE-Cloud/02.16.02.02_My_Area.md>) —— Introduced in SmarTest 7.6.2
- [Ticket submission page](<02_System_reference/02.16_ACS_TE-Cloud/02.16.02.03_Ticket_submission_page.md>) —— Introduced in SmarTest 7.6.2
- [Opening the help center](<02_System_reference/02.16_ACS_TE-Cloud/02.16.02.04_Opening_the_help_center.md>) —— Introduced in SmarTest 7.6.2
- [Submitting a ticket](<02_System_reference/02.16_ACS_TE-Cloud/02.16.02.05_Submitting_a_ticket.md>) —— Introduced in SmarTest 7.6.2
- [Replying to a ticket](<02_System_reference/02.16_ACS_TE-Cloud/02.16.02.06_Replying_to_a_ticket.md>) —— Introduced in SmarTest 7.6.2
- [Closing a ticket](<02_System_reference/02.16_ACS_TE-Cloud/02.16.02.07_Closing_a_ticket.md>) —— Introduced in SmarTest 7.6.2
- [Help Center](<02_System_reference/02.16_ACS_TE-Cloud/02.16.02_Help_Center.md>) —— Introduced in SmarTest 7.6.2
- [Generating and saving key files](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.01_Generating_and_saving_key_files.md>) —— Introduced in SmarTest 7.6.2
- [Creating a TE-Cloud virtual machine](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.02_Creating_a_TE-Cloud_virtual_machine.md>) —— Introduced in SmarTest 7.6.2
- [Configuring a remote connection to a virtual machine](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.03_Configuring_a_remote_connection_to_a_virtual_machine.md>) —— Introduced in SmarTest 7.6.2
- [Connecting to a virtual machine via SSH](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.04_Connecting_to_a_virtual_machine_via_SSH.md>) —— Introduced in SmarTest 7.6.2
- [Setting up a VNC connection](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.05_Setting_up_a_VNC_connection.md>) —— Introduced in SmarTest 7.6.2
- [Connecting to a virtual machine via VNC](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.06_Connecting_to_a_virtual_machine_via_VNC.md>) —— Introduced in SmarTest 7.6.2
- [Setting up a site to transmit files to and from the virtual machine based on SFTP](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.07_Setting_up_a_site_to_transmit_files_to_and_from_the_virtual_machine_base.md>) —— Introduced in SmarTest 7.6.2
- [Transmitting files between Linux machines with command line](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.08_Transmitting_files_between_Linux_machines_with_command_line.md>) —— Introduced in SmarTest 7.6.2
- [Authorizing another user for a virtual machine](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.09_Authorizing_another_user_for_a_virtual_machine.md>) —— Introduced in SmarTest 7.6.2
- [Revoking access to a virtual machine](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.10_Revoking_access_to_a_virtual_machine.md>) —— Introduced in SmarTest 7.6.2
- [Modifying the password of a virtual machine user account](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.11_Modifying_the_password_of_a_virtual_machine_user_account.md>) —— Introduced in SmarTest 7.6.2
- [Adding a user account to a virtual machine](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.12_Adding_a_user_account_to_a_virtual_machine.md>) —— Introduced in SmarTest 7.6.2
- [Accessing a virtual machine from another virtual machine](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.13_Accessing_a_virtual_machine_from_another_virtual_machine.md>) —— Introduced in SmarTest 7.6.2
- [Installing software to the virtual machine](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03.14_Installing_software_to_the_virtual_machine.md>) —— Introduced in SmarTest 7.6.2
- [Working with virtual machines](<02_System_reference/02.16_ACS_TE-Cloud/02.16.03_Working_with_virtual_machines.md>) —— Introduced in SmarTest 7.6.2
- [Getting contact information for an engineering test center](<02_System_reference/02.16_ACS_TE-Cloud/02.16.04.01_Getting_contact_information_for_an_engineering_test_center.md>) —— Introduced in SmarTest 7.6.2
- [Adding a public SSH key](<02_System_reference/02.16_ACS_TE-Cloud/02.16.04.02_Adding_a_public_SSH_key.md>) —— Introduced in SmarTest 7.6.2
- [Booking a tester for a specific time slot](<02_System_reference/02.16_ACS_TE-Cloud/02.16.04.03_Booking_a_tester_for_a_specific_time_slot.md>) —— Introduced in SmarTest 7.6.2
- [Connecting to a tester over the internet](<02_System_reference/02.16_ACS_TE-Cloud/02.16.04.04_Connecting_to_a_tester_over_the_internet.md>) —— Introduced in SmarTest 7.6.2
- [Transmitting files to the tester](<02_System_reference/02.16_ACS_TE-Cloud/02.16.04.05_Transmitting_files_to_the_tester.md>) —— Introduced in SmarTest 7.6.2
- [Accessing online testers](<02_System_reference/02.16_ACS_TE-Cloud/02.16.04_Accessing_online_testers.md>) —— Introduced in SmarTest 7.6.2
- [External tools needed for working with virtual machines](<02_System_reference/02.16_ACS_TE-Cloud/02.16.05_External_tools_needed_for_working_with_virtual_machines.md>) —— Introduced in SmarTest 7.6.2
- [ACS TE-Cloud](<02_System_reference/02.16_ACS_TE-Cloud/02.16_ACS_TE-Cloud.md>) —— Introduced in SmarTest 7.6.2


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 48 条**，涉及 **45 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
