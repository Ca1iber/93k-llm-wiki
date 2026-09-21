---
type: version
title: SmarTest 8.1.2 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.01_PMUX01_Power_MUX_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.02_MUX_cards_filling_rules.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.03_MUX_cards_pogo_block_numbering.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.05_Pogo_pin_assignment_-_MUX_cards.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.01.01_PMUX01_force_and_sense_pins.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.01.02_PMUX01_supply_pins.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.01.03_PMUX01_control_pins.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.01_PMUX01_Power_MUX.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.02_MUX_cards_interposer__MUXIP01.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.03_MUX_cards_stiffener__MUXSTIF01.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.08.04_Electrical_design_rules_-_MUX_cards.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.10.05_MUX_cards_stiffener__MUXSTIF01.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 8.1.2

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版新引入（14 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [PMUX01 Power MUX pogo pin assignment](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.01_PMUX01_Power_MUX_pogo_pin_assignment.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [MUX cards filling rules](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.02_MUX_cards_filling_rules.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [MUX cards pogo block numbering](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.03_MUX_cards_pogo_block_numbering.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [Pogo pin assignment - MUX cards](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.05_Pogo_pin_assignment_-_MUX_cards.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [PMUX01 force and sense pins](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.01.01_PMUX01_force_and_sense_pins.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [PMUX01 supply pins](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.01.02_PMUX01_supply_pins.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [PMUX01 control pins](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.01.03_PMUX01_control_pins.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [PMUX01 Power MUX](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.01_PMUX01_Power_MUX.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [MUX cards interposer (MUXIP01)](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.02_MUX_cards_interposer__MUXIP01.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [MUX cards stiffener (MUXSTIF01)](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.03_MUX_cards_stiffener__MUXSTIF01.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [Electrical design rules - MUX cards](<02_System_reference/02.03_DUT_board_design_reference/02.03.08.04_Electrical_design_rules_-_MUX_cards.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [MUX cards stiffener (MUXSTIF01)](<02_System_reference/02.03_DUT_board_design_reference/02.03.10.05_MUX_cards_stiffener__MUXSTIF01.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2
- [MUX cards design data](<02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md>) —— Introduced in SmarTest 7.3.2 / 8.1.2


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 14 条**，涉及 **14 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
