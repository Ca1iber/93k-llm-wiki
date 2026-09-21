---
type: version
title: SmarTest 7.5.2 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05.05_Internal_utility_power_supply__V93000_systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05_Utility_power_supplies.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.07_PSSL_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.04.07_Grounding_concept_for_power_applications.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.01_Electrical_design_rules_-_DC_Scale_cards.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.02_Electrical_design_rules_-_DPS-slot_power_supplies.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.03_Electrical_design_rules_-_Digital_cards.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.05_Electrical_design_rules_-_Other_cards__DUT_interfaces__systems.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08_Electrical_design__Product-specific_rules.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.03_IOCHANNEL_section.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.277_TSRC__-__Time_Stamping_Results_Computed.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.278_TSRS__-__TMU_Set_ReSults.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.279_TSRW__-__TMU_Set_RaW_results.md
  - 02_System_reference/02.06_Command_Reference/02.06.13.02.08_TSRC__-__Time_Stamping_Results_Computed.md
  - 02_System_reference/02.06_Command_Reference/02.06.13.02.09_TSRS__-__TMU_Set_ReSults.md
  - 02_System_reference/02.06_Command_Reference/02.06.13.02.10_TSRW__-__TMU_Set_RaW_results.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.21.01_Printing_tester_status_from_system_control.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.21.02_Printing_tester_status_from_testflow.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.21.03_Printing_tester_status_from_test_method.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148.01_PinPropertyMonitor.printStatus.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148.02_PinPropertyMonitor.printStatus2File.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148_PinPropertyMonitor.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.25_TESTSET__.testnumber.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10.02.01.01_SmartCalc_thread_per_site_example.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10.02.01.02_SmartCalc_common_thread_example.md
  # 本页共涉及 32 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.5.2

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（18 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.5.2:` 前缀，**那是原文的一部分，没有去掉**。

- [PSSL pogo cable assembly, pogo pin layout and model file configuration](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.07_PSSL_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md>) —— SmarTest 7.5.2: Added Pin Scale SL 15G (E8080C) and Pin Scale SL 16G (E8080E)
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md>) —— SmarTest 7.5.2 / 8.2.5: E8021-64100_..._DesignKit_MUXStiffener.zip: E8021-24100 updated to revision D
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md>) —— SmarTest 7.5.2 / 8.2.5: E8021-96520_A_DesignKit_PMUX_DUT_board.zip: New files E8021-96520_A.pdf, E8021-96520_A_sheet_#.dxf, E8021-96520_A.ami, E8021-96520_A.pkg
- [Direct-Probe stiffener](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md>) —— SmarTest 7.5.2 / 8.2.2: E7018-64170_revJ_Direct_Probe_Universal_Stiffener-3rd_Party_Fabrication_Package.zip updated to revision K
- [Direct-Probe stiffener](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md>) —— SmarTest 7.5.2 / 8.2.3: E5150-60221_revD_SECRON_Direct_Probe_Digital_Stiffener_-_3rd_Party_Fabrication_Package.zip updated to revision G
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md>) —— SmarTest 7.5.2 / 8.2.5: E8021-64100_..._DesignKit_MUXStiffener.zip: E8021-24100 updated to revision D
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md>) —— SmarTest 7.5.2 / 8.2.5: E8021-96520_A_DesignKit_PMUX_DUT_board.zip: New files E8021-96520_A.pdf, E8021-96520_A_sheet_#.dxf, E8021-96520_A.ami, E8021-96520_A.pkg
- [IOCHANNEL section](<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.03_IOCHANNEL_section.md>) —— SmarTest 7.5.2: Added PSSL15G, HSM15G
- [TSRC? - (Time Stamping Results Computed)](<02_System_reference/02.06_Command_Reference/02.06.02.02.277_TSRC__-__Time_Stamping_Results_Computed.md>) —— SmarTest 7.5.2: New extra parameter: sitesToBeDone
- [TSRS? - (TMU Set ReSults)](<02_System_reference/02.06_Command_Reference/02.06.02.02.278_TSRS__-__TMU_Set_ReSults.md>) —— SmarTest 7.5.2: New extra parameter: sitesToBeDone
- [TSRW? - (TMU Set RaW results)](<02_System_reference/02.06_Command_Reference/02.06.02.02.279_TSRW__-__TMU_Set_RaW_results.md>) —— SmarTest 7.5.2: New extra parameter: sitesToBeDone
- [TSRC? - (Time Stamping Results Computed)](<02_System_reference/02.06_Command_Reference/02.06.13.02.08_TSRC__-__Time_Stamping_Results_Computed.md>) —— SmarTest 7.5.2: New extra parameter: sitesToBeDone
- [TSRS? - (TMU Set ReSults)](<02_System_reference/02.06_Command_Reference/02.06.13.02.09_TSRS__-__TMU_Set_ReSults.md>) —— SmarTest 7.5.2: New extra parameter: sitesToBeDone
- [TSRW? - (TMU Set RaW results)](<02_System_reference/02.06_Command_Reference/02.06.13.02.10_TSRW__-__TMU_Set_RaW_results.md>) —— SmarTest 7.5.2: New extra parameter: sitesToBeDone
- [TESTSET().testname()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.md>) —— SmarTest 7.5.2: Renamed forceSTDFTestNam parameter to forceSTDFTestName
- [TESTSET().testnumber()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.25_TESTSET__.testnumber.md>) —— SmarTest 7.5.2: Renamed forceSTDFTestNam parameter to forceSTDFTestName
- [TESTSET](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.md>) —— SmarTest 7.5.2: Renamed forceSTDFTestNam parameter to forceSTDFTestName
- [Configuring the contents of the STDF file](<02_System_reference/02.10_Data_Logging/02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md>) —— SmarTest 7.5.2: New parameter bypassLoggingAfterFirstFailing.


## 这一版新引入（17 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Internal utility power supply (V93000 systems)](<02_System_reference/02.03_DUT_board_design_reference/02.03.05.05_Internal_utility_power_supply__V93000_systems.md>) —— Introduced in SmarTest 7.5.2
- [Utility power supplies](<02_System_reference/02.03_DUT_board_design_reference/02.03.05_Utility_power_supplies.md>) —— Introduced in SmarTest 7.5.2
- [Grounding concept for power applications](<02_System_reference/02.03_DUT_board_design_reference/02.03.07.04.07_Grounding_concept_for_power_applications.md>) —— Introduced in SmarTest 7.5.2 / 8.2.3
- [Electrical design rules - DC Scale cards](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.01_Electrical_design_rules_-_DC_Scale_cards.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Electrical design rules - DPS-slot power supplies](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.02_Electrical_design_rules_-_DPS-slot_power_supplies.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Electrical design rules - Digital cards](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.03_Electrical_design_rules_-_Digital_cards.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Electrical design rules - Other cards, DUT interfaces, systems](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.05_Electrical_design_rules_-_Other_cards__DUT_interfaces__systems.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Electrical design: Product-specific rules](<02_System_reference/02.03_DUT_board_design_reference/02.03.08_Electrical_design__Product-specific_rules.md>) —— Introduced in SmarTest 7.5.2 / 8.2.5
- [Printing tester status from system control](<02_System_reference/02.07_Test_Method_Reference/02.07.03.21.01_Printing_tester_status_from_system_control.md>) —— Introduced in SmarTest 7.5.2
- [Printing tester status from testflow](<02_System_reference/02.07_Test_Method_Reference/02.07.03.21.02_Printing_tester_status_from_testflow.md>) —— Introduced in SmarTest 7.5.2
- [Printing tester status from test method](<02_System_reference/02.07_Test_Method_Reference/02.07.03.21.03_Printing_tester_status_from_test_method.md>) —— Introduced in SmarTest 7.5.2
- [PinPropertyMonitor.printStatus()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148.01_PinPropertyMonitor.printStatus.md>) —— Introduced in SmarTest 7.5.2
- [PinPropertyMonitor.printStatus2File()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148.02_PinPropertyMonitor.printStatus2File.md>) —— Introduced in SmarTest 7.5.2
- [PinPropertyMonitor](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148_PinPropertyMonitor.md>) —— Introduced in SmarTest 7.5.2
- [SmartCalc thread per site example](<02_System_reference/02.07_Test_Method_Reference/02.07.10.02.01.01_SmartCalc_thread_per_site_example.md>) —— Introduced in SmarTest 7.5.2
- [SmartCalc common thread example](<02_System_reference/02.07_Test_Method_Reference/02.07.10.02.01.02_SmartCalc_common_thread_example.md>) —— Introduced in SmarTest 7.5.2
- [SmartCalc "Thread per site" and "Common thread"](<02_System_reference/02.07_Test_Method_Reference/02.07.10.02.01_SmartCalc__Thread_per_site__and__Common_thread.md>) —— Introduced in SmarTest 7.5.2


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 35 条**，涉及 **32 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
