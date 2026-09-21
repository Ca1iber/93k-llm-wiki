# 建页资料包 05 — 02_System_reference/02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md

## 0. 元信息

- 标题（frontmatter）：Pogo pad and via design
- H1：Pogo pad and via design
- 字节：3203；出度：5；入边：55
- frontmatter：`{"source_html": "02_System_reference/02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.htm", "source_topic": "91610.htm", "title": "Pogo pad and via design"}`
- 标题结构：Pogo pad and via design / Subtopics / Functional changes

## 1. 定义文档全文（raw，禁止修改）

```markdown
---
title: "Pogo pad and via design"
source_topic: "91610.htm"
source_html: "02_System_reference/02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.htm"
---
# Pogo pad and via design

#### Subtopics

- [Pogo block compatibility](<02.03.07.07.01_Pogo_block_compatibility.md>)
- [Inter-layer via design](<02.03.07.07.02_Inter-layer_via_design.md>)
- [Pogo via examples](<02.03.07.07.03_Pogo_via_examples.md>)
- [Pogo via depth example](<02.03.07.07.04_Pogo_via_depth_example.md>)

The pogo pad and via connect the pogo pin to the signal trace on the DUT board. The design of the pogo pad and of the pogo via depends on the type of the pogo pin and on the stackup of the DUT board.

  This section covers the general rules for designing pog pads and pogo vias. For product-specific rules, refer to

- [XPS256 VHD pogo pad and via design](<02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md>)

When designing pogo pads and pogo vias for the V93000 you must respect certain mechanical requirements. You also have some variables that can be used to improve the pogo via performance. Both are listed below:

 | Minimum pad size: |

56 mil (~1.4 mm)

Recommendation: For pogo pin landing holes of digital and analog channels use a pad size of at least 1.4 mm to 1.5 mm, for utility and DPS channels at least 1.6 mm to 1.8 mm, with a maximum hole diameter of 0.7 mm. A smaller pad size will cause contact problems with the DUT interface.

 |
 | Signal pogo via drill size:  | 26 + 1/-3 mil finished hole size (~0.7 mm) |
 | Minimum pogo via length:  | 13 mil (~0.33 mm) |
 | Number of adjacent ground pogo vias:  | 4 |
 | Signal via to ground via pitch:  | 100 mil |
 | Removal of non-functional pads:  | Yes / No |
 | Back drilling:  | Yes / No |
 | Ground plane clearance or antipad:  | variable |
 | Power plane clearance or antipad:  | >= ground plane clearance |
 | Ground via thermal straps:  | No (direct connect to ground plane) |
 | Hard Au plating  | Min. 30 碌inches, Knoop hardness 130-200 |

A typical approach for a pogo via design is to optimize the via structure through an electromagnetic (EM) field simulation. The simulation uses a 3D model of the pogo pin and pogo via as shown in the figure below.

  ![Optimization of a pogo via design by 3D EM simulation](<../../../../raw/91615.png>)

For more information on this approach you may consult the following articles:

- Jose Moreira, Ming Tsai, Jonathan Kenton, Heidi Barnes, Don Faller, "PCB Loadboard Design Challenges for Multi-Gigabit Devices in Automated Test Applications", DesignCon 2006, Santa Clara USA.
- H. Barnes, J. Moreira, H. Ossoinig, M. Wollitzer, T. Schmid, M. Tsai, "Development of a Pogo Pin Assembly and Via Design for Multi-Gigabit Interfaces on Automated Test Equipment", Asia-Pacific Microwave Conference, APMC 2006, Yokohama Japan.

An electromagnetic field simulation is time consuming and not required for most applications. A pogo via design optimized for a given stackup can be reused on a different stack-up. Experience shows that the performance of the via will not change.

## Functional changes

- Introduced before SmarTest 6.3.2
```

## 2. 语法 / 参数段落（脚本逐字抽取，§4 —— 进页面时照抄，不重写）

*（这篇没有 `Syntax`/`Parameters` 这类段落——那就没有语法可抄，页面不许自己编一个）*

## 3. 入边 33 篇（谁引它、引它的原句 —— 「和谁有关」的唯一来源）

### ← UHC4 / UHC4T DUT board layout
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.06.01_UHC4___UHC4T_DUT_board_layout.md`（引 4 次）

- L14：For the recommended size of signal pogo pads, refer to [Minimum pad size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Minimum_pad_size>) and [Signal pogo via drill size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Signal_via_drill_size>) in [Pogo pad and via design](<02.03.07.07_Pogo_pad
- L14：For the recommended size of signal pogo pads, refer to [Minimum pad size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Minimum_pad_size>) and [Signal pogo via drill size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Signal_via_drill_size>) in [Pogo pad and via design](<02.03.07.07_Pogo_pad
- L14：For the recommended size of signal pogo pads, refer to [Minimum pad size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Minimum_pad_size>) and [Signal pogo via drill size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Signal_via_drill_size>) in [Pogo pad and via design](<02.03.07.07_Pogo_pad
- L38：[DC Scale UHC4 / UHC4T card](<../02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.md>)[UHC4 / UHC4T pogo pin assignment](<02.03.06.02.06_UHC4___UHC4T_pogo_pin_assignment.md>)[UHC4 / UHC4T low-level high-current design](<02.03.08.01.06.05_UHC4___UHC4T_low-level_high-current_design.md>)[Pogo pad

### ← PS5000 pogo pin assignment
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md`（引 4 次）

- L72：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L108：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L160：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row sequence a-e-b-f-c-g-d for compatibility with the 4-row STD block and HD block. This sequence is different to the row sequence a-b-c-d of the 4-row pogo blocks. Do not use the
- L298：[Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>): The standard recommendations for pogo pads and vias apply to all pogo block types of the Pin Scale 5000 pogo cable assemblies.

### ← UHC4 / UHC4T DUT board layout
`02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.02_UHC4___UHC4T_DUT_board_layout.md`（引 4 次）

- L14：For the recommended size of signal pogo pads, refer to [Minimum pad size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Minimum_pad_size>) and [Signal pogo via drill size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Signal_via_drill_size>) in [Pogo pad and via design](<02.03.07.07_Pogo_pad
- L14：For the recommended size of signal pogo pads, refer to [Minimum pad size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Minimum_pad_size>) and [Signal pogo via drill size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Signal_via_drill_size>) in [Pogo pad and via design](<02.03.07.07_Pogo_pad
- L14：For the recommended size of signal pogo pads, refer to [Minimum pad size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Minimum_pad_size>) and [Signal pogo via drill size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Signal_via_drill_size>) in [Pogo pad and via design](<02.03.07.07_Pogo_pad
- L38：[DC Scale UHC4 / UHC4T card](<../02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.md>)[UHC4 / UHC4T pogo pin assignment](<02.03.06.02.06_UHC4___UHC4T_pogo_pin_assignment.md>)[UHC4 / UHC4T low-level high-current design](<02.03.08.01.06.05_UHC4___UHC4T_low-level_high-current_design.md>)[Pogo pad

### ← Pin Scale 5000 pogo pin assignment
`02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md`（引 4 次）

- L66：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L102：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L154：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row sequence a-e-b-f-c-g-d for compatibility with the 4-row STD block and HD block. This sequence is different to the row sequence a-b-c-d of t
- L292：[Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>): The standard recommendations for pogo pads and vias apply to all pogo block types of the Pin Scale 5000 pogo cable assemblies.

### ← PS1600 pogo pin assignment
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md`（引 3 次）

- L82：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L118：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L172：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row sequence a-e-b-f-c-g-d for compatibility with the 4-row STD block and HD block. This sequence is different to the row sequence a-b-c-d of the 4-row pogo blocks. Do not use the

### ← PS1600 pogo pin assignment
`02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md`（引 3 次）

- L75：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L111：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L165：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row sequence a-e-b-f-c-g-d for compatibility with the 4-row STD block and HD block. This sequence is different to the row sequence a-b-c-d of t

### ← XPS256 pogo block specifications
`02_System_reference/02.02_Specifications/02.02.05.03.08_XPS256_pogo_block_specifications.md`（引 2 次）

- L41：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L88：| See also [XPS256 VHD pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md>) and [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← XPS256 pogo pin assignment
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md`（引 2 次）

- L95：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L152：| See also [XPS256 VHD pogo pad and via design](<02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md>) and [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row sequence a-e-b-f-c-g-d for compatibility with the 4-row HD block. This sequ

### ← Layout recommendations
`02_System_reference/02.03_DUT_board_design_reference/02.03.07.09.02_Layout_recommendations.md`（引 2 次）

- L15：For the recommended size of pogo pads, refer to [Minimum pad size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Minimum_pad_size>) in [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>).
- L15：For the recommended size of pogo pads, refer to [Minimum pad size](<02.03.07.07_Pogo_pad_and_via_design.md#_91610__r_Minimum_pad_size>) in [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>).

### ← Pin Scale 5000 card
`02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.01_Pin_Scale_5000_card.md`（引 2 次）

- L24：[Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>): The standard recommendations for pogo pads and vias apply to all pogo block types of the Pin Scale 5000 pogo cable assemblies.
- L43：[Pin Scale 5000 (Test head cards reference)](<../02.05_Test_Head_Cards/02.05.04.02_Pin_Scale_5000_card.md>)[PS5000 pogo pin assignment](<02.03.06.03.05_PS5000_pogo_pin_assignment.md>)[Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>)[High-speed DUT board design](<02.03.07.02_High-sp

### ← XPS256 pogo block specifications
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.08_XPS256_pogo_block_specifications.md`（引 2 次）

- L41：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L88：| See also [XPS256 VHD pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md>) and [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← XPS256 pogo pin assignment
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.04_XPS256_pogo_pin_assignment.md`（引 2 次）

- L90：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |
- L147：| See also [XPS256 VHD pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md>) and [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row seq

### ← AVI64 pogo pin assignment
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.01_AVI64_pogo_pin_assignment.md`（引 1 次）

- L75：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← E8023PA pogo cable assembly: 8 HD pogo blocks (Standard)
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.01_E8023PA_pogo_cable_assembly__8_HD_pogo_blocks__Standard.md`（引 1 次）

- L62：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← E8023PB pogo cable assembly: 2 VHD pogo blocks
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks.md`（引 1 次）

- L74：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row sequence a-e-b-f-c-g-d for compatibility with the 4-row HD block. This sequence is different to the row sequence a-b-c-d of the 4-row HD pogo block. Do not use the wrong row s

### ← E8023PE pogo cable assembly: 8 MS-DPS style pogo blocks (DPS128-HC only)
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.05_E8023PE_pogo_cable_assembly__8_MS-DPS_style_pogo_blocks__DPS128-HC_only.md`（引 1 次）

- L440：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← E8023PK pogo cable assembly: 4 VHD pogo blocks (DPS128)
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.09_E8023PK_pogo_cable_assembly__4_VHD_pogo_blocks__DPS128.md`（引 1 次）

- L74：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row sequence a-e-b-f-c-g-d for compatibility with the 4-row HD block. This sequence is different to the row sequence a-b-c-d of the 4-row HD pogo block. Do not use the wrong row s

### ← FVI16 pogo pin assignment
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.04_FVI16_pogo_pin_assignment.md`（引 1 次）

- L78：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← PVI8 pogo pin assignment
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.05_PVI8_pogo_pin_assignment.md`（引 1 次）

- L76：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← PSSL pogo cable assembly, pogo pin layout and model file configuration
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.07_PSSL_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md`（引 1 次）

- L413：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← HSM15/16G pogo cable assembly and pogo pin layout
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.10_HSM15_16G_pogo_cable_assembly_and_pogo_pin_layout.md`（引 1 次）

- L413：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← Link Scale USB3 pogo pin assignment
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.11_Link_Scale_USB3_pogo_pin_assignment.md`（引 1 次）

- L62：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← WSMM Card Cage pogo via design
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.02_WSMM_Card_Cage_pogo_via_design.md`（引 1 次）

- L12：[Pogo via examples](<02.03.07.07.03_Pogo_via_examples.md>)[Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>)

### ← Wave Scale RF pogo pin assignment (10 MHz clock)
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.04_Wave_Scale_RF_pogo_pin_assignment__10_MHz_clock.md`（引 1 次）

- L40：| See also [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← Pogo block compatibility
`02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.01_Pogo_block_compatibility.md`（引 1 次）

- L18：For dimensions and detailed drawings of the SD, HD and VHD pogo blocks, refer to [Layout information: DUT board](<02.03.12.01.08_Layout_information__DUT_board.md>). For newer test head cards, simple drawings also are available in section [Pogo pin assignment](<02.03.06_Pogo_pin_assignment.md>). For

### ← Electrical design: General rules
`02_System_reference/02.03_DUT_board_design_reference/02.03.07_Electrical_design__General_rules.md`（引 1 次）

- L16：[Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>)

### ← XPS256 VHD pogo pad and via design
`02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md`（引 1 次）

- L58：[XPS256 pogo pin assignment](<02.03.06.02.07_XPS256_pogo_pin_assignment.md>)[Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>)

### ← HSM DUT board design
`02_System_reference/02.03_DUT_board_design_reference/02.03.08.05.01_HSM_DUT_board_design.md`（引 1 次）

- L42：[Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>)

### ← Layout information: DUT board
`02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.08_Layout_information__DUT_board.md`（引 1 次）

- L14：For the pogo pin assignment of all available cards and additional dimensional drawings, refer to [Pogo pin assignment](<02.03.06_Pogo_pin_assignment.md>). For the default pogo pad layout and via design, refer also to [Pogo pad and via design](<02.03.07.07_Pogo_pad_and_via_design.md>).

### ← E8023PA pogo cable assembly: 8 HD pogo blocks (Standard)
`02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.01_E8023PA_pogo_cable_assembly__8_HD_pogo_blocks__Standard.md`（引 1 次）

- L62：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← E8023PB pogo cable assembly: 2 VHD pogo blocks
`02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks.md`（引 1 次）

- L74：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row sequence a-e-b-f-c-g-d for compatibility with the 4-row HD block. This sequence is different to the row sequence a-b-c-d of the 4-row HD po

### ← E8023PE pogo cable assembly: 8 MS-DPS style pogo blocks (DPS128-HC only)
`02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.05_E8023PE_pogo_cable_assembly__8_MS-DPS_style_pogo_blocks__DPS128-HC_only.md`（引 1 次）

- L440：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | |

### ← E8023PK pogo cable assembly: 4 VHD pogo blocks (DPS128)
`02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.09_E8023PK_pogo_cable_assembly__4_VHD_pogo_blocks__DPS128.md`（引 1 次）

- L74：| See also [Pogo pad and via design](<../02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>). | | CAUTION The 7-row VHD block uses the row sequence a-e-b-f-c-g-d for compatibility with the 4-row HD block. This sequence is different to the row sequence a-b-c-d of the 4-row HD po

## 4. 出边 5 个（它引谁）

- [[Pogo block compatibility]] → `02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.01_Pogo_block_compatibility.md`（Pogo block compatibility）
- [[Inter-layer via design]] → `02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.02_Inter-layer_via_design.md`（Inter-layer via design）
- [[Pogo via examples]] → `02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.03_Pogo_via_examples.md`（Pogo via examples）
- [[Pogo via depth example]] → `02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.04_Pogo_via_depth_example.md`（Pogo via depth example）
- [[XPS256 VHD pogo pad and via design]] → `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md`（XPS256 VHD pogo pad and via design）

## 5. 结构段落（Procedure / Dependency / Errors …）

### 〔related Subtopics〕（L8，2869 字符）

- [Pogo block compatibility](<02.03.07.07.01_Pogo_block_compatibility.md>)
- [Inter-layer via design](<02.03.07.07.02_Inter-layer_via_design.md>)
- [Pogo via examples](<02.03.07.07.03_Pogo_via_examples.md>)
- [Pogo via depth example](<02.03.07.07.04_Pogo_via_depth_example.md>)

The pogo pad and via connect the pogo pin to the signal trace on the DUT board. The design of the pogo pad and of the pogo via depends on the type of the pogo pin and on the stackup of the DUT board.

  This section covers the general rules for designing pog pads and pogo vias. For product-specific rules, refer to

- [XPS256 VHD pogo pad and via design](<02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design.md>)

When designing pogo pads and pogo vias for the V93000 you must respect certain mechanical requirements. You also have some variables that can be used to improve the pogo via performance. Both are listed below:

 | Minimum pad size: |

56 mil (~1.4 mm)

Recommendation: For pogo pin landing holes of digital and analog channels use a pad size of at least 1.4 mm to 1.5 mm, for utility and DPS channels at least 1.6 mm to 1.8 mm, with a maximum hole diameter of 0.7 mm. A smaller pad size will cause contact problems with the DUT interface.

 |
 | Signal pogo via drill size:  | 26 + 1/-3 mil finished hole size (~0.7 mm) |
 | Minimum pogo via length:  | 13 mil (~0.33 mm) |
 | Number of adjacent ground pogo vias:  | 4 |
 | Signal via to ground via pitch:  | 100 mil |
 | Removal of non-functional pads:  | Yes / No |
 | Back drilling:  | Yes / No |
 | Ground plane clearance or antipad:  | variable |
 | Power plane clearance or antipad:  | >= ground plane clearance |
 | Ground via thermal straps:  | No (direct connect to ground plane) |
 | Hard Au plating  | Min. 30 碌inches, Knoop hardness 130-200 |

A typical approach for a pogo via design is to optimize the via structure through an electromagnetic (EM) field simulation. The simulation uses a 3D model of the pogo pin and pogo via as shown in the 

### 〔version Functional changes〕（L52，34 字符）

- Introduced before SmarTest 6.3.2
