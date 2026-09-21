---
type: version
title: SmarTest 8.3.0 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.07_Utility_line_compatibility__configuration__and_capability.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.08_PSHX_card_pogo_assembly_and_channels.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.03_Wave_Scale_Millimeter_PCB_space.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.02.02_Pin_assignment_for_the_Pin_Scale_HX_standard_configuration.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.05.01.05_Pin_assignment_for_the_Pin_Scale_HX_standard_configuration.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.01_Bridge_Beam_Direct_Probe_for_Digital_and_Mixed_Signal__E8016BBD.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.03_Bridge_Beam_Direct_Probe_for_WSRF_and_PMUX__E8016BBWS.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04_Direct-Probe_bridge_beams.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.03_Docking_handler_info.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.07_Clock_boards.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 8.3.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（5 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 8.3.0:` 前缀，**那是原文的一部分，没有去掉**。

- [PSHX card pogo assembly and channels](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.08_PSHX_card_pogo_assembly_and_channels.md>) —— SmarTest 7.5.3 / 8.3.0: The name of several pogo pins has been adapted to the pin description and to the behavior of SmarTest.
- [Pin assignment for the Pin Scale HX standard configuration](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.02.02_Pin_assignment_for_the_Pin_Scale_HX_standard_configuration.md>) —— SmarTest 7.5.3 / 8.3.0: Names of pogo pins adapted to the names in topic 91505 "Pin Scale HX card pogo assembly and channels".
- [Pin assignment for the Pin Scale HX standard configuration](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.05.01.05_Pin_assignment_for_the_Pin_Scale_HX_standard_configuration.md>) —— SmarTest 7.5.3 / 8.3.0: Names of pogo pins adapted to the names in topic 91505 "Pin Scale HX card pogo assembly and channels".
- [Docking handler info](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.03_Docking_handler_info.md>) —— SmarTest 7.5.3 / 8.3.0: Drawing E7015-23261 updated from revision H to revision I.
- [Clock boards](<02_System_reference/02.05_Test_Head_Cards/02.05.07_Clock_boards.md>) —— SmarTest 8.3.0: Term "NIST traceable calibration" replaced


## 这一版新引入（6 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Utility line compatibility, configuration, and capability](<02_System_reference/02.03_DUT_board_design_reference/02.03.04.07_Utility_line_compatibility__configuration__and_capability.md>) —— Introduced in SmarTest 7.5.3 / 8.3.0
- [Wave Scale Millimeter PCB space](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.03_Wave_Scale_Millimeter_PCB_space.md>) —— Introduced in SmarTest 8.3.0
- [Bridge Beam Direct Probe for Digital and Mixed Signal (E8016BBD)](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.01_Bridge_Beam_Direct_Probe_for_Digital_and_Mixed_Signal__E8016BBD.md>) —— Introduced in SmarTest 7.5.3 / 8.3.0
- [Bridge Beam Direct Probe for PSRF (E8016BBRF)](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md>) —— Introduced in SmarTest 7.5.3 / 8.3.0
- [Bridge Beam Direct Probe for WSRF and PMUX (E8016BBWS)](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.03_Bridge_Beam_Direct_Probe_for_WSRF_and_PMUX__E8016BBWS.md>) —— Introduced in SmarTest 7.5.3 / 8.3.0
- [Direct-Probe bridge beams](<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04_Direct-Probe_bridge_beams.md>) —— Introduced in SmarTest 7.5.3 / 8.3.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 11 条**，涉及 **11 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
