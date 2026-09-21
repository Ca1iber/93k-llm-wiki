---
type: version
title: SmarTest 7.4.2 — 版本页
tags: [version, smartest]
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.04_Mask_mode_of_sequencer-controlled_utility_lines.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.05_Sequencer-controlled_utility_lines.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.04.02_Pogo_pin_with_cone_shaped_tip.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08.01_Protecting_the_chuck_on_the_wafer_prober.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08.02_Installing_Direct-Probe_bridge_beam_on_TEL_Precio_wafer_prober.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08.03_Connecting_up_Direct-Probe_bridge_beam_on_TEL_Precio_wafer_prober.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08_Interfacing_the_test_system_to_TEL_Precio_wafer_prober.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.154_LBUD__LBUD__-__LaBel_User_Data.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.312_UTSC__UTSC__-__UTility_line_Serial_Configuration.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.12_UTSC__UTSC__-__UTility_line_Serial_Configuration.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.114_GPIB_SEND.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.03_HW_STATE.checkKelvinStatusParallel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117_HW_STATE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.120_IS_FIRST_RUN.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.24_SMC_IN_BACKGROUNDPROCESSING.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27_SMC_PIN_ERROR_MAP.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.265.01_UTILITY_SEQ_POGO_MODE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.266.01_UTILITY_SEQ_STATIC_POGO_MODE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.266.02_UTILITY_SEQ_STATIC_MASK.pogoBlock.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.266.03_UTILITY_SEQ_STATIC_MASK.execute.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.266_UTILITY_SEQ_STATIC_MASK.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.269_VECTOR.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07.01_EVENT_FILTER.setFilterType.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07.02_EVENT_FILTER.getFilterType.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07.03_EVENT_FILTER.setFilterValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07.04_EVENT_FILTER.getFilterValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07_EVENT_FILTER.md
  # 本页共涉及 47 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.4.2

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（28 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.4.2:` 前缀，**那是原文的一部分，没有去掉**。

- [Technology file for a device](<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md>) —— SmarTest 7.2.3.9 / 7.3.4.4 / 7.4.1.1 / 7.4.2: New parameter: mset_program_memory_preallocation
- [Sequencer-controlled utility lines](<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05_Sequencer-controlled_utility_lines.md>) —— SmarTest 7.4.2: New mask mode, controlled by API UTILITY_SEQ_STATIC_MASK allows masking utility lines.
- [UTSC, UTSC? - (UTility line Serial Configuration)](<02_System_reference/02.06_Command_Reference/02.06.02.02.312_UTSC__UTSC__-__UTility_line_Serial_Configuration.md>) —— SmarTest 7.4.2: New extra parameter maskMode.
- [DFTD, DFTD? (DeFine Test Data)](<02_System_reference/02.06_Command_Reference/02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md>) —— SmarTest 7.4.2: New element setFilterValue
- [UTSC, UTSC? - (UTility line Serial Configuration)](<02_System_reference/02.06_Command_Reference/02.06.12.02.12_UTSC__UTSC__-__UTility_line_Serial_Configuration.md>) —— SmarTest 7.4.2: New extra parameter maskMode.
- [GPIB_SEND](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.114_GPIB_SEND.md>) —— SmarTest 7.4.2: ACTION name changed to GPIB_ACTION
- [HW_STATE](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117_HW_STATE.md>) —— SmarTest 7.4.2: New member function checkKelvinStatusParallel()
- [SMC_PIN_ERROR_MAP](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27_SMC_PIN_ERROR_MAP.md>) —— SmarTest 7.4.2: Added new constructor.
- [SPMU_PIN_TASK.loadCap()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.md>) —— SmarTest 7.4.2: AVI64: The load capacitance can be set with connected or disconnected DPS channel.
- [UTILITY_SEQ_POGO_MODE](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.265.01_UTILITY_SEQ_POGO_MODE.md>) —— SmarTest 7.4.2: New options TM::SEQ_POGO_MASK_MODE_RW and TM::SEQ_POGO_MASK_MODE_RD.
- [VECTOR](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.269_VECTOR.md>) —— SmarTest 7.4.2: :New member function getImmediateVectors()
- [EVENT_... (DC events API reference)](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63_EVENT_...__DC_events_API_reference.md>) —— SmarTest 7.4.2: New EVENT_FILTER
- [GET_FUNCTIONAL_RESULT()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.md>) —— SmarTest 7.4.2: New syntax using parameter portlist
- [Technology file for a device](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.03_Technology_file_for_a_device.md>) —— SmarTest 7.2.3.9 / 7.3.4.4 / 7.4.1.1 / 7.4.2: New parameter: mset_program_memory_preallocation
- [Technology file for a device](<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.03_Technology_file_for_a_device.md>) —— SmarTest 7.2.3.9 / 7.3.4.4 / 7.4.1.1 / 7.4.2: New parameter: mset_program_memory_preallocation
- [Default GPIB configuration](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.15.04.02_Default_GPIB_configuration.md>) —— SmarTest 7.4.2: A new parameter hontech_request_barcode is added in the configuration.
- [GPIB communication flow for Seiko-Epson handlers](<02_System_reference/02.09_Test_Program_Management/02.09.01.03.06.01.15.04.03_GPIB_communication_flow_for_Seiko-Epson_handlers.md>) —— SmarTest 7.4.2: Adds barcode querying for HonTech handler.
- [The PART_ID field in the PRR](<02_System_reference/02.10_Data_Logging/02.10.03.03.08_The_PART_ID_field_in_the_PRR.md>) —— SmarTest 7.4.2: Introduced OverridePartIdForRetestDevice
- [Configuring the contents of the STDF file](<02_System_reference/02.10_Data_Logging/02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md>) —— SmarTest 7.4.2: New parameters useStandardTSR and generateStandardTsrTestLabel.
- [Test Synopsis Record (TSR)](<02_System_reference/02.10_Data_Logging/02.10.03.05.26_Test_Synopsis_Record__TSR.md>) —— SmarTest 7.4.2: Setting the useStandardTSR or generateStandardTsrTestLabel key in the configuration file changes the semantics of several fields.
- [Project-related STIL Reader setup options](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.05.03.01_Project-related_STIL_Reader_setup_options.md>) —— SmarTest 7.4.2: Removed stil_file option.
- [Test-processing STIL Reader setup options](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.05.03.02_Test-processing_STIL_Reader_setup_options.md>) —— SmarTest 7.4.2: Removed max_vector_buffer option.
- [Translation-related STIL Reader setup options](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.05.03.03_Translation-related_STIL_Reader_setup_options.md>) —— SmarTest 7.4.2: Added the allow_wavetbl_merge, combinations_allow_new_waveform, fix_failing_signals, force_edge_strobe, scan_pattern_start, scan_pattern_stop, stop_on_uninitialized_signals, unify_periods_boundary_edge_placement, unify_periods_signal_boundary_edge_placement options.
- [WGL-related STIL Reader setup options](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.05.03.07_WGL-related_STIL_Reader_setup_options.md>) —— SmarTest 7.4.2: Added wgl_purge_unused_timeplates, wgl_purge_unused_waveforms options. Removed wgl_purge_unused_timing.
- [STIL Reader setup file](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.05.03_STIL_Reader_setup_file.md>) —— SmarTest 7.4.2: Added allow_wavetbl_merge, combinations_allow_new_waveform, fix_failing_signals, force_edge_strobe, scan_pattern_start, scan_pattern_stop, stop_on_uninitialized_signals, unify_periods_signal_boundary_edge_placement, unify_periods_boundary_edge_placement, wgl_purge_unused_timeplates, wgl_purge_unused_waveforms options.
- [STIL Reader setup file](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.01.05.03_STIL_Reader_setup_file.md>) —— SmarTest 7.4.2: Removed max_vector_buffer, stil_file options. Removed wgl_purge_unused_timing.
- [ait command line parameters](<02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.08.01_ait_command_line_parameters.md>) —— SmarTest 7.4.2: Added the PSSL and oe options for the -z switch.
- [Sequencer-controlled utility lines](<03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md>) —— SmarTest 7.4.2: New mask mode, controlled by API UTILITY_SEQ_STATIC_MASK allows masking utility lines.


## 这一版新引入（20 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Mask mode of sequencer-controlled utility lines](<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.04_Mask_mode_of_sequencer-controlled_utility_lines.md>) —— Introduced in SmarTest 7.4.2
- [Pogo pin with cone shaped tip](<02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.04.02_Pogo_pin_with_cone_shaped_tip.md>) —— Introduced in SmarTest 7.4.2
- [Protecting the chuck on the wafer prober](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08.01_Protecting_the_chuck_on_the_wafer_prober.md>) —— Introduced in SmarTest 7.4.2
- [Installing Direct-Probe bridge beam on TEL Precio wafer prober](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08.02_Installing_Direct-Probe_bridge_beam_on_TEL_Precio_wafer_prober.md>) —— Introduced in SmarTest 7.4.2
- [Connecting up Direct-Probe bridge beam on TEL Precio wafer prober](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08.03_Connecting_up_Direct-Probe_bridge_beam_on_TEL_Precio_wafer_prober.md>) —— Introduced in SmarTest 7.4.2
- [Interfacing the test system to TEL Precio wafer prober](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08_Interfacing_the_test_system_to_TEL_Precio_wafer_prober.md>) —— Introduced in SmarTest 7.4.2
- [LBUD, LBUD? - (LaBel User Data)](<02_System_reference/02.06_Command_Reference/02.06.02.02.154_LBUD__LBUD__-__LaBel_User_Data.md>) —— Introduced in SmarTest 7.4.2
- [HW_STATE.checkKelvinStatusParallel()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.03_HW_STATE.checkKelvinStatusParallel.md>) —— Introduced in SmarTest 7.4.2
- [IS_FIRST_RUN()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.120_IS_FIRST_RUN.md>) —— Introduced in SmarTest 7.4.2
- [SMC_IN_BACKGROUNDPROCESSING()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.24_SMC_IN_BACKGROUNDPROCESSING.md>) —— Introduced in SmarTest 7.4.2
- [UTILITY_SEQ_STATIC_POGO_MODE](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.266.01_UTILITY_SEQ_STATIC_POGO_MODE.md>) —— Introduced in SmarTest 7.4.2
- [UTILITY_SEQ_STATIC_MASK.pogoBlock()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.266.02_UTILITY_SEQ_STATIC_MASK.pogoBlock.md>) —— Introduced in SmarTest 7.4.2
- [UTILITY_SEQ_STATIC_MASK.execute()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.266.03_UTILITY_SEQ_STATIC_MASK.execute.md>) —— Introduced in SmarTest 7.4.2
- [UTILITY_SEQ_STATIC_MASK](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.266_UTILITY_SEQ_STATIC_MASK.md>) —— Introduced in SmarTest 7.4.2
- [EVENT_FILTER.setFilterType()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07.01_EVENT_FILTER.setFilterType.md>) —— Introduced in SmarTest 7.4.2
- [EVENT_FILTER.getFilterType()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07.02_EVENT_FILTER.getFilterType.md>) —— Introduced in SmarTest 7.4.2
- [EVENT_FILTER.setFilterValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07.03_EVENT_FILTER.setFilterValue.md>) —— Introduced in SmarTest 7.4.2
- [EVENT_FILTER.getFilterValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07.04_EVENT_FILTER.getFilterValue.md>) —— Introduced in SmarTest 7.4.2
- [EVENT_FILTER](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.07_EVENT_FILTER.md>) —— Introduced in SmarTest 7.4.2
- [Mask mode of sequencer-controlled utility lines](<03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01.04_Mask_mode_of_sequencer-controlled_utility_lines.md>) —— Introduced in SmarTest 7.4.2


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 48 条**，涉及 **47 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
