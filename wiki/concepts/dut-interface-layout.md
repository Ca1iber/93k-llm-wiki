---
type: concept
title: DUT interface layout
layer: n/a
stage: project
tags: [concept, dut-interface, pogo-block, layout, numbering, exa-scale, model-file]
related: [dut-board-design-reference, layout-information-dut-board, logical-boards, utility-lines, utility-line-assignments, pogocabling-section, pogo-block-compatibility, pogo-pad-and-via-design, utility-card]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# DUT interface layout

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,538 字符逐字取自** `<02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Group 7 | Group 7 |  | Group 8 | Group 8 |  | Group 2 | Group 2 |  | Group 6 | Group 6 |
|---|---|---|---|---|---|---|---|---|---|---|
| DPS 7<br><br>(272) | UTIL 8<br><br>(172) |  | DPS 8<br><br>(268) | UTIL 4<br><br>(168) |  | DPS 2<br><br>(267) | UTIL 3<br><br>(167) |  | DPS 6<br><br>(271) | UTIL 7<br><br>(171) |
| 424 | 420 |  | 432 | 428 |  | 316 | 312 |  | 416 | 412 |
| 224 | 220 |  | 232 | 228 |  | 116 | 112 |  | 216 | 212 |
| 423 | 419 |  | 431 | 427 |  | 315 | 311 |  | 415 | 411 |
| 223 | 219 |  | 231 | 227 |  | 115 | 111 |  | 215 | 211 |
| 422 | 418 |  | 430 | 426 |  | 314 | 310 |  | 414 | 410 |
| 222 | 218 |  | 230 | 226 |  | 114 | 110 |  | 214 | 210 |
| 421 | 417 |  | 429 | 425 |  | 313 | 309 |  | 413 | 409 |
| 221 | 217 |  | 229 | 225 |  | 113 | 109 |  | 213 | 209 |
|  |  |  |  |  |  |  |  |  |  |  |
| `MUX cards pogo blocks`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_MUX_cards`）<br><br>or<br><br>`Wave Scale interface modules`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_Wave_scale`）`1)`（raw: `#_20811__fn_SmarTest_8_only_EXA_Scale`） | `MUX cards pogo blocks`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_MUX_cards`）<br><br>or<br><br>`Wave Scale interface modules`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_Wave_scale`）`1)`（raw: `#_20811__fn_SmarTest_8_only_EXA_Scale`） | `MUX cards pogo blocks`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_MUX_cards`）<br><br>or<br><br>`Wave Scale interface modules`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_Wave_scale`）`1)`（raw: `#_20811__fn_SmarTest_8_only_EXA_Scale`） | `MUX cards pogo blocks`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_MUX_cards`）<br><br>or<br><br>`Wave Scale interface modules`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_Wave_scale`）`1)`（raw: `#_20811__fn_SmarTest_8_only_EXA_Scale`） | !`DUT interface layout - RF only`（raw: `../../../../raw/347950.png`）<br><br>`High-Density Port Scale RF solution`（raw: `02.03.07.08.01_High-Density_Port_Scale_RF_solution.md`）`2)`（raw: `#fntarg_2`） | !`DUT interface layout - RF only`（raw: `../../../../raw/347950.png`）<br><br>`High-Density Port Scale RF solution`（raw: `02.03.07.08.01_High-Density_Port_Scale_RF_solution.md`）`2)`（raw: `#fntarg_2`） | !`DUT interface layout - RF only`（raw: `../../../../raw/347950.png`）<br><br>`High-Density Port Scale RF solution`（raw: `02.03.07.08.01_High-Density_Port_Scale_RF_solution.md`）`2)`（raw: `#fntarg_2`） | `MUX cards pogo blocks`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_MUX_cards`）<br><br>or<br><br>`Wave Scale interface modules`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_Wave_scale`）`1)`（raw: `#_20811__fn_SmarTest_8_only_EXA_Scale`） | `MUX cards pogo blocks`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_MUX_cards`）<br><br>or<br><br>`Wave Scale interface modules`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_Wave_scale`）`1)`（raw: `#_20811__fn_SmarTest_8_only_EXA_Scale`） | `MUX cards pogo blocks`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_MUX_cards`）<br><br>or<br><br>`Wave Scale interface modules`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_Wave_scale`）`1)`（raw: `#_20811__fn_SmarTest_8_only_EXA_Scale`） | `MUX cards pogo blocks`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_MUX_cards`）<br><br>or<br><br>`Wave Scale interface modules`（raw: `02.03.03.01_DUT_interface_layout.md#_20811__r_Wave_scale`）`1)`（raw: `#_20811__fn_SmarTest_8_only_EXA_Scale`） |
|  |  |  |  |  |  |  |  |  |  |  |
| 125 | 129 |  | 117 | 121 |  | 101 | 105 |  | 201 | 205 |
| 325 | 329 |  | 317 | 321 |  | 301 | 305 |  | 401 | 405 |
| 126 | 130 |  | 118 | 122 |  | 102 | 106 |  | 202 | 206 |
| 326 | 330 |  | 318 | 322 |  | 302 | 306 |  | 402 | 406 |
| 127 | 131 |  | 119 | 123 |  | 103 | 107 |  | 203 | 207 |
| 327 | 331 |  | 319 | 323 |  | 303 | 307 |  | 403 | 407 |
| 128 | 132 |  | 120 | 124 |  | 104 | 108 |  | 204 | 208 |
| 328 | 332 |  | 320 | 324 |  | 304 | 308 |  | 404 | 408 |
| UTIL 5<br><br>(169) | DPS 4<br><br>(269) |  | UTIL 1<br><br>(165) | DPS 3<br><br>(265) |  | UTIL 2<br><br>(166) | DPS 1<br><br>(266) |  | UTIL 6<br><br>(170) | DPS 5<br><br>(270) |
| Group 4 | Group 4 |  | Group 3 | Group 3 |  | Group 1 | Group 1 |  | Group 5 | Group 5 |

### Tables（脚本逐字抽取，第 2 张）

 | Group  | Pogo block range  | Usage |
 | Cable pogo block area of the DUT scale interface  | 101, 102, 103, 104, 105, 106, 107, 108  | S1 pogo blocks of group 1 |
 | 109, 110, 111, 112, 113, 114, 115, 116  | S1 pogo blocks of group 2 |
 | 117, 118, 119, 120, 121, 122, 123, 124  | S1 pogo blocks of group 3 |
 | 125, 126, 127, 128, 129, 130, 131, 132  | S1 pogo blocks of group 4 |
 | 201, 202, 203, 204, 205, 206, 207, 208  | S1 pogo blocks of group 5 |
 | 209, 210, 211, 212, 213, 214, 215, 216  | S1 pogo blocks of group 6 |
 | 217, 218, 219, 220, 221, 222, 223, 224  | S1 pogo blocks of group 7 |
 | 225, 226, 227, 228, 229, 230, 231, 232  | S1 pogo blocks of group 8 |
 | 301, 302, 303, 304, 305, 306, 307, 308  | S2 pogo blocks of group 1 |
 | 309, 310, 311, 312, 313, 314, 315, 316  | S2 pogo blocks of group 2 |
 | 317, 318, 319, 320, 321, 322, 323, 324  | S2 pogo blocks of group 3 |
 | 325, 326, 327, 328, 329, 330, 331, 332  | S2 pogo blocks of group 4 |
 | 401, 402, 403, 404, 405, 406, 407, 408  | S2 pogo blocks of group 5 |
 | 409, 410, 411, 412, 413, 414, 415, 416  | S2 pogo blocks of group 6 |
 | 417, 418, 419, 420, 421, 422, 423, 424  | S2 pogo blocks of group 7 |
 | 425, 426, 427, 428, 429, 430, 431, 432  | S2 pogo blocks of group 8 |
 | Alternate designation of UTIL 1 …nbsp;8 and DPS 1 …nbsp;8 pogo blocks of the V93000 EXA Scale system.  | 165, 166, 167, 168, 169, 170, 171, 172  | Alternate designation for UTIL 1 …UTIL 8. |
 | 265, 266, 267, 268, 269, 270, 271, 272  | Alternate designation for DPS 1 …DPS 8`3)`（raw: `#fntarg_3`）. |
 | `MUX cards`（raw: `02.03.06.05_Pogo_pin_assignment_-_MUX_cards.md`） in the central area of the DUT interface. For the pogo block numbering, refer to `MUX cards pogo block numbering`（raw: `02.03.06.05.03_MUX_cards_pogo_block_numbering.md`）.  | 881, 883, 885, 887, 889, 891, 893, 895  | Block A of cards 05, 06, 07, 08, 11, 12, 15, 16 in the left frame |
 | 882, 884, 886, 888, 890, 892, 894, 896  | Block B of cards 05, 06, 07, 08, 11, 12, 15, 16 in the left frame |
 | 865, 867, 869, 871, 873, 875, 877, 879  | Block A of cards 01, 02, 03, 04, 09, 10, 13, 14 in the right frame |
 | 866, 868, 870, 872, 874, 876, 878, 880  | Block B of cards 01, 02, 03, 04, 09, 10, 13, 14 in the right frame |
 | Wave Scale `RFIM-6`（raw: `02.03.06.07.05_Wave_Scale_RF_with_RFIM-6_RFIM-8_pogo_pin_assignment.md`） and `RFIM-18`（raw: `02.03.06.07.06_Wave_Scale_RF_with_RFIM-18_pogo_pin_assignment.md`） interface modules in the central area of the DUT interface (SmarTest 8 only)  | 901, 902, 903, 904, 905, 906  | RF interface modules in the left frame |
 | 909, 910, 911, 912, 913, 914  | RF interface modules in the right frame |

### Tables（脚本逐字抽取，第 3 张）

   | 4128 ... 7426  | Resources of the DUT Scale interface |
 | 9901 ... 9912  | RFIM-6 and RFIM-18 ports |
 | 190901 ... 890208  | RF ports of the Remote Mixing Modules (RMM) |

### Tables（脚本逐字抽取，第 4 张）

   | 501, 502, 503, 504, 505, 506, 507, 508  | Virtual S1 pogo blocks of group 1 |
 | 509, 510, 511, 512, 513, 514, 515, 516  | Virtual S1 pogo blocks of group 2 |
 | 517, 518, 519, 520, 521, 522, 523, 524  | Virtual S1 pogo blocks of group 3 |
 | 525, 526, 527, 528, 529, 530, 531, 532  | Virtual S1 pogo blocks of group 4 |
 | 601, 602, 603, 604, 605, 606, 607, 608  | Virtual S1 pogo blocks of group 5 |
 | 609, 610, 611, 612, 613, 614, 615, 616  | Virtual S1 pogo blocks of group 6 |
 | 617, 618, 619, 620, 621, 622, 623, 624  | Virtual S1 pogo blocks of group 7 |
 | 625, 626, 627, 628, 629, 630, 631, 632  | Virtual S1 pogo blocks of group 8 |
 | 701, 702, 703, 704, 705, 706, 707, 708  | Virtual S2 pogo blocks of group 1 |
 | 709, 710, 711, 712, 713, 714, 715, 716  | Virtual S2 pogo blocks of group 2 |
 | 717, 718, 719, 720, 721, 722, 723, 724  | Virtual S2 pogo blocks of group 3 |
 | 725, 726, 727, 728, 729, 730, 731, 732  | Virtual S2 pogo blocks of group 4 |
 | 801, 802, 803, 804, 805, 806, 807, 808  | Virtual S2 pogo blocks of group 5 |
 | 809, 810, 811, 812, 813, 814, 815, 816  | Virtual S2 pogo blocks of group 6 |
 | 817, 818, 819, 820, 821, 822, 823, 824  | Virtual S2 pogo blocks of group 7 |
 | 825, 826, 827, 828, 829, 830, 831, 832  | Virtual S2 pogo blocks of group 8 |

### Tables（脚本逐字抽取，第 5 张）

  | 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148 |
 | 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164 |
 | 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248 |
 | 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264 |
 | 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348 |
 | 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364 |
 | 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448 |
 | 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464 |
 | 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548 |
 | 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564 |
 | 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648 |
 | 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664 |
 | 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748 |
 | 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764 |
 | 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848 |
 | 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864 |

<!-- 语法节 end -->

## 是什么

**这一页不教怎么测，它给的是 DUT 接口上的「块位编号」——也就是 model file 里要写的那个号。**

原文开篇两句把关系和用途都交代了：

> 「The V93000 test head can be configured with different combinations of different types of cards to meet specific test requirements. Cabling within the test head connects the cards and the infrastructure resources like utility lines and utility power supplies to one or more pogo pin blocks of the DUT interface.」

> 「The POGOCABLING section of the model file (SmarTest 7) and the CARD_CONFIGURATION section of the tester.model file (SmarTest 8) map the physical card cage location of a card with the corresponding pogo block position of the DUT interface.」

**第二句是本页和测试工程师之间唯一的那根线**：`POGOCABLING`（SmarTest 7）/ `CARD_CONFIGURATION`（SmarTest 8）做的那个映射，**用的就是本页这套号**。
所以本页是「写 model file / DUT board description file 时回来查号」的地方——**它不是测试流程的一环，是编号约定的一环**。

原文自己列的四节，本页四节都覆盖：

| 节 | 给什么 |
|---|---|
| `Pogo block locations` | 位置表：每个 group 里哪两块叫 DPS、哪两块叫 UTIL，以及各自的备用号 |
| `Structure of the DUT interface layout` | group 1–8 的可用范围、DPS/UTIL 的含义、S1/S2 的 +200 |
| `List of all pogo blocks` | 全部物理块号区间（含中央区域与 WSMM） |
| `Virtual pogo blocks` | 超过 16 通道的块怎么派生虚拟块号（偏移 400 / 32 / 432） |

### group 1–8：每 group「16 + 2」块

> 「- Group 1 鈥?8:The pogo blocks are organized in eight groups, each providing 16 + 2 pogo blocks:
>
> - Groups 1, 2, 3, and 8 are available on all DUT interfaces.
> - Groups 4, 5, 6, and 7 are available on the large DUT interface and on the DUT Scale interface.」

**「哪些 group 有」这一条直接决定你手上那台机器的接口大小**：small 接口只有 1 / 2 / 3 / 8 四个 group，
**只有 large 接口与 DUT Scale 接口才有 4 / 5 / 6 / 7**。

**「16 + 2」是什么**：16 个 cable pogo 块（S1 八个 ＋ S2 八个）＋ 2 个（一个 DPS ＋ 一个 UTIL）。
依据：S1/S2 清单里 group 1 是 `101, 102, 103, 104, 105, 106, 107, 108` 与
`301, 302, 303, 304, 305, 306, 307, 308`（8 + 8），而位置表里 group 1 那两格是 `UTIL 2 (166)` 与 `DPS 1 (266)`。
**（这是推断：原文只写 `16 + 2`，没有把加法写出来。）**

### S1 / S2：相邻两块，号差 200

> 「Adjacent pogo blocks are sometimes referred as S1 and S2 pogo block. The number of the S2 pogo block is the number of the S1 block plus an offset of 200.」

**④ 图证（`347951.png`）**：图里画的是**上下相邻的两排块位**，两排的右端各有一个
`orientation mark` 用箭头指出，右侧另给了一个算例 —— `S1 = 204` / `S2 = S1 + 200 = 404`。
**图上这三处字（`orientation mark`、`S1 = 204`、`S2 = S1 + 200 = 404`）在 raw 里 grep 不到**
（已核：对该篇 raw 搜 `orientation mark` 与 `S1 = 204` 均无匹配），**所以它们是图证、不是文本**。

这张图把两件事钉实了：

| 图答了什么 | 依据 |
|---|---|
| `+ 200` 具体长什么样：`204` 与 `404` 同属 **group 5** | 清单表里 S1 的 group 5 是 `201` 到 `208`、S2 的 group 5 是 `401` 到 `408`；图给的算例与它对得上 |
| **DUT 接口上有一个方向标记** | **原文正文里没有 `orientation mark` 这个词**——这件事只有图里有 |

**⚠️ 图不解决的问题**：`S1 = 204` 是一个「任意取」的例子还是某个特定配置，图上没说；
而且这张图**没有版本标注**，接口上的标记位置是不是 7.10.3 上的样子，**本页答不了**。

### DPS 1–8 与 UTIL 1–8

两组位置的含义都写在同一节里，**但 DPS 1–8 的含义按系统代次分三档**：

| 系统 / SmarTest | `DPS 1 鈥?8` 这些位置是什么 |
|---|---|
| Pin Scale / Smart Scale（SmarTest 7） | 原文：这些块留给 `Pogo pin assignment - DPS-slot device power supplies` 与 `Internal Utility Power Supply (SE-UDPS)` |
| Smart Scale（SmarTest 8） | 原文：`reserved for future use`；DPS128/64 的 MS-DPS 风格 pogo 块与 SE-UDPS **也可以**装在这些位置 |
| EXA Scale（SmarTest 7.10 及以上，及 SmarTest 8） | 原文：留给**第二张可选 Utility Card 的 utility pogo 块**，**必须用备用号 `265 鈥?nbsp;272` 在 DUT board description file 里定义** |

> 「These pogo block positions are reserved for utility pogo blocks of the second optional Utility Card. The alternate pogo block numbers 265 鈥?nbsp;272 must be used to define these utility blocks in the DUT board description file.」

**「必须用备用号」是这一节里唯一的硬要求 `must`**，而且它把测试工程师拉回来了：
**同一个物理位置，写进文件时用哪个号，取决于系统代次**。

`UTIL 1 鈥?UTIL 8` 的定义只有一句：

> 「These are the utility pogo blocks that provide connections to the Utility lines, the Utility power supplies, and some other resources of the V93000 infrastructure.」

**注意这句话的宾语是三样**——utility line 只是其中之一，**utility line 本身不在本页**
（见 `Utility lines`，raw: `02.03.04_Utility_lines.md`）。

### ⚠️ 备用号 265–272 的配对要小心（**本节最值钱的一条**）

位置表把每个位置和它的备用号成对列出来了，**照位置表读出来的配对是这样的**：

| group | 位置表里的两块（原文写作「DPS n / UTIL n」＋圆括号里的备用号） |
|---|---|
| Group 1 | `UTIL 2 (166)`、`DPS 1 (266)` |
| Group 2 | `DPS 2 (267)`、`UTIL 3 (167)` |
| Group 3 | `UTIL 1 (165)`、`DPS 3 (265)` |
| Group 4 | `UTIL 5 (169)`、`DPS 4 (269)` |
| Group 5 | `UTIL 6 (170)`、`DPS 5 (270)` |
| Group 6 | `DPS 6 (271)`、`UTIL 7 (171)` |
| Group 7 | `DPS 7 (272)`、`UTIL 8 (172)` |
| Group 8 | `DPS 8 (268)`、`UTIL 4 (168)` |

**照这张表，`265` 配的是 `DPS 3`，`268` 配的是 `DPS 8`——都不是顺序对应的。**
而同一篇的 pogo 块清单里写着
`265, 266, 267, 268, 269, 270, 271, 272` → `Alternate designation for DPS 1 鈥?DPS 8`，
**照那一条顺读会得到「265 = DPS 1」——那是错的。**
原文自己知道，在脚注里点破了：

> 「Note: The sequence of block 265 ... 272 and DPS 1 鈥?DPS 8 differs. For the correct assignment from block 265 ... 272 to DPS 1 鈥?DPS 8, refer to the Pogo_block_locations_table above.」

（`...` 是**原文自己写的**三个 ASCII 点，不是本页加的省略号。）

**所以：给 EXA Scale 的第二张 Utility Card 定义 utility 块时，号不能顺推，要回位置表查。**

### 中央区域与 WSMM 的块号

清单表另外给了三类不属于 S1/S2 的号：

| 区域 | 块号 | 原文写的用途 |
|---|---|---|
| 中央区域的 `MUX cards` | `881, 883, 885, 887, 889, 891, 893, 895` | 左框里 05/06/07/08/11/12/15/16 卡的 Block A |
| 同上 | `882, 884, 886, 888, 890, 892, 894, 896` | 左框里同样那些卡的 Block B |
| 同上 | `865, 867, 869, 871, 873, 875, 877, 879` | 右框里 01/02/03/04/09/10/13/14 卡的 Block A |
| 同上 | `866, 868, 870, 872, 874, 876, 878, 880` | 右框里同样那些卡的 Block B |
| 中央区域的 Wave Scale RFIM-6 / RFIM-18（SmarTest 8 only） | `901, 902, 903, 904, 905, 906` | 左框里的 RF 接口模块 |
| 同上 | `909, 910, 911, 912, 913, 914` | 右框里的 RF 接口模块 |
| WSMM（SmarTest 8 only）资源号 | `4128 ... 7426` / `9901 ... 9912` / `190901 ... 890208` | DUT Scale 接口资源 / RFIM-6 与 RFIM-18 端口 / RMM 的 RF 端口 |

**④ 图证（`347950.png`）**：图里是一个圆形轮廓，边沿一圈十几个空心圆点（块位），右下角写着 `RF only`。
它**答不了**的问题要说清：**图上没有任何编号**，所以「`881`–`896` 里哪几个落在左框、哪几个落在右框」
**这张图给不出**——左右框的对应关系只能照清单表的文字读。
（`RF only` 三个字在 raw 里以图片 alt 文字出现过，**所以它本身不是图证**；
图证是「图上没有编号」这一件。）

### 虚拟 pogo 块：超过 16 通道的块怎么编号

> 「SmarTest divides physical pogo blocks of more than 16 channels into 16 channel units called logical boards. The first logical board is assigned to the physical pogo block. The other logical boards are assigned to so-called virtual pogo blocks.」

> 「These virtual blocks are used for physical pogo blocks providing more than 16 channels and therefore covering minimum two logical boards. An offset of 400 is to be added to the position of the physical block to obtain the number of the virtual pogo block.」

**四逻辑板的物理块再多两块**，用的是另一个偏移：

> 「For physical pogo blocks covering four logical boards, two more virtual pogo blocks are reserved using an offset of
>
> - 32 to the position of the physical block and an offset of
> - 432 to the position of the physical block respectively an offset of 32 to the position of the first virtual block.」

**这句话后半截原文就是绕的**（`and an offset of 432 to the position of the physical block respectively an offset of 32 to the position of the first virtual block`），
**本页照原样引，不替它拆解**。

原文还点了一条容易被漏掉的适用面：

> 「An offset of 400 or 432 for virtual pogo blocks is also used for some DPS128 pogo cable assemblies. For more information, refer to "E8023PB" (SmarTest 8 only), "E8023PC" and "E8023PD" in DPS128 and DPS64 pogo cabling and model file configuration.」

**所以「虚拟块号 = 物理号 + 400」不是一条通则**：DPS128 的某些 pogo cable assembly 也在用同一套偏移。

## 典型用法

**先说成色：原文没有 `## Procedure`，也没有 `## Before you begin`。** 下面五步是从四节内容里读出来的，**不是照原文步骤抄的**。

**1. 先确定系统代次——因为 `DPS 1 鈥?8` 的含义三代不同。**
EXA Scale 上这些位置是**第二张 Utility Card 的 utility 块**；Pin Scale / Smart Scale（SmarTest 7）上是 device power supply 与 SE-UDPS；
Smart Scale（SmarTest 8）上 `reserved for future use`。**查号之前先定代次**。

**2. 按 group 定位物理块。** small 接口只有 group 1/2/3/8；large 与 DUT Scale 接口才有 group 4/5/6/7。

**3. S2 号 = S1 号 + 200**（原文一句，图 `347951.png` 给的算例是 `204 → 404`）。

**4. DPS / UTIL 用备用号 165–172 与 265–272。**
**⚠️ 265–272 与 DPS 1–8 的顺序不同**（见上是那张配对表，原文脚注点名要回位置表查）。

**5. 写进该写的地方。** 原文把「卡笼位置 ↔ pogo 块位置」这件事交给了两处，**而这两处都在本页之外**：

| 你要写哪份东西 | 原文指向 |
|---|---|
| model file（SmarTest 7） | `POGOCABLING` section |
| `tester.model`（SmarTest 8） | `CARD_CONFIGURATION` section |
| DUT board description file（EXA Scale 第二张 Utility Card 的 utility 块） | **必须用备用号 `265 鈥?nbsp;272`** |

**本页答不上的（语料未写 / 本页未读）：**

- **每张卡该插在哪个卡笼、哪块板用哪几个块**——**本页一个都没有**，那是 `POGOCABLING` / `CARD_CONFIGURATION` 两篇的事，**本页没读那两篇**。
- **接口的机械尺寸、块位的物理位置**——**本页一个字没有**（七个 test head 子主题本页没读）。
- **`MUX cards pogo block numbering` 里那套 881/865 的编号规则**——原文把编号规则推给了那一篇，**本页没读**。

## 和谁有关

- [[dut-board-design-reference]] — **上级**：本页在 raw 里归在 `02.03_DUT_board_design_reference/` 的第 3 支（路径事实），是该支的第 1 篇
- [[layout-information-dut-board]] — **同族、同一支的邻居**：那一页给的是**图纸包清单**（`.zip` / `.dxf` / `.pdf`），
  本页给的是**编号体系**；**两页都不含尺寸**，差别在「拿图」与「查号」
- [[logical-boards]] — **上游概念**：本页的虚拟块号建立在「16 通道 = 一个 logical board」这条规则上，**规则本体在那一页**
- `Utility lines`（raw: `02.03.04_Utility_lines.md`）— **下游**：`UTIL 1 鈥?UTIL 8` 正是 utility line 的落点
  （原文的宾语里点名了 `Utility lines`）。**⚠️ 这个名字不在 `extract/prose-allowlist.txt` 里**
  （本页 frontmatter 的 `related` 里留着它，因为那一页确实存在、slug 就是 `utility-lines`），
  **所以正文里只写反引号 ＋ raw 路径，不写成 wikilink**（§9.1）
- [[utility-line-assignments]] — **同族的另一面**：块的**容量**（16 线 / 32 线、2 排 / 4 排）在那一页，**编号在本页**
- [[pogocabling-section]] — **下游、原文点名**：`POGOCABLING` 把卡笼位置映到块位，**用的就是本页的号**；**本页没读那一篇**
- [[utility-card]] — **原文点名的硬约束**：EXA Scale 的第二张 Utility Card 的 utility 块，**只能用备用号定义**
- [[pogo-block-compatibility]] — 同组邻居（pogo 块）；**本页原文一个字没提它**，本页不据此声称关系
- [[pogo-pad-and-via-design]] — 同组邻居；**本页原文同样没提**
- `CARD_CONFIGURATION section`（raw: `../02.04_Model_File_and_Licensing/02.04.01.03.01.02_CARD_CONFIGURATION_section.md`）
  — **原文点名的另一处**（SmarTest 8 的 `tester.model`）；`CARD_CONFIGURATION` 这个名字不在 allowlist 里，故用反引号
- `Pogo pin assignment - DPS-slot device power supplies`（raw: `02.03.06.04_Pogo_pin_assignment_-_DPS-slot_device_power_supplies.md`）、
  `Internal Utility Power Supply (SE-UDPS)`（raw: `02.03.05.07_Internal_Utility_Power_Supply__SE-UDPS___V93000_systems.md`）、
  `Internal Utility Power Option`（raw: `02.03.05.04_Internal_Utility_Power_Option__V93000_EXA_Scale_systems.md`）
  — 都是**原文点名、本页没读**的资源篇
- `MUX cards`、`Wave Scale RFIM-6`、`Wave Scale RFIM-18`、`WSMM Card Cage DUT Interface`、`Pogo mapping`
  — **原文点名、本页没读**（中央区域与 WSMM 的编号规则在这些篇里）
- **八个 group 名（`Group 1` 到 `Group 8`）与块型名（`S1` / `S2` / `DPS n` / `UTIL n`）不是 wiki 页面**，只是本页里的编号——**它们不该链、也没有页**

## 版本

原文**有** `## Functional changes`，四条（逐字）：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.4: CTH with DUT Scale interface introduced`
- `SmarTest 7.1.0: Support of A-Test Head (ATH)`
- `SmarTest 8.3.4: Alternate UTIL and DPS pogo block numbers for V93000 EXA Scale systems added.`

读法上三件事要记：

| 要点 | 说明 |
|---|---|
| **第一条是哨兵，不是「6.3.2 的变更」** | `Introduced before SmarTest 6.3.2` 按 §11.2 ② 读＝「在本文档集覆盖范围开始之前就已经有了」，**不是「6.3.2 新增了这个页面」** |
| **最后一条决定本页的「哪个号能用」** | **备用号 165–172 / 265–272 是 SmarTest 8.3.4 才加的**；照这一节读，**8.3.4 之前的 EXA Scale 上这套号还不存在** |
| **一条 `SmarTest 8.3.4` 出现在一份面向 7.10.3 的 wiki 里** | 本 wiki 面向 **SmarTest 7.10.3**，而这一条讲的是 **SmarTest 8** 的变更。**两条产品线号，本页不替它换算**（§11.2 ④） |

**本页答不上来的版本问题**：**「7.10.3 上到底有没有这套备用号」本篇没写**——
它只写了 `SmarTest 8.3.4: Alternate UTIL and DPS pogo block numbers for V93000 EXA Scale systems added.`，**对 7.10.x 一个字没说**。**本页不推。**

## 出处

`sources:` 一篇：
`02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md`
（TDC `20811.htm`，**213 行**，**整篇读完**）

**本页没做的（按缺口大小排）：**

- **七个子主题，一篇都没读**：`02.03.03.01.01` – `02.03.03.01.07`
  （A-Test Head / Compact / Small / Large 四种 test head，以及其中三种的 **with DUT Scale interface** 变体）。
  **后果：每种 test head 的接口长什么样、有几块、怎么排，本页一个字都没有**——本页只有编号规则。
- **两张图都读了**（**这是本页与同批多数页不同的地方**）：
  `../../../../raw/347951.png`（alt 写作 `DUT interface layout - S1 and S2`）与
  `../../../../raw/347950.png`（alt 写作 `DUT interface layout - RF only`）。
  **但两张图都没有版本标注**，所以从图里读到的 `orientation mark` **不能当「7.10.3 上就有这个标记」的证据**（§11.4 那条坑）。
- **五篇被本篇指过去、本页没读的文档**：
  `Pogo mapping`（`../02.05_Test_Head_Cards/02.05.01.04_Pogo_mapping.md`）、
  `Model file sections`（7.6.x 与 7.10.x 两条）、
  `SmarTest 8: CARD_CONFIGURATION of tester.model`、
  `Layout information: DUT board`（`02.03.12.01.08`）。
  **所以「号怎么落到 model file 的哪一行」本页一个字没有**，只有原文那句
  `map the physical card cage location of a card with the corresponding pogo block position of the DUT interface`。
- **中央区域三篇与 WSMM 一篇没读**：`MUX cards pogo block numbering`、`WSMM Card Cage DUT Interface`、
  `Pin Scale 1600 pogo pin mapping`、`Wave Scale MX pogo pin assignment and model file configuration`、
  `XPS256 specific setup tasks`、
  `DPS128 and DPS64 pogo cabling and model file configuration`、
  `Pin Scale 5000 card configuration in the model file`。
  **虚拟块号那一段的「For more information refer to」五条，本页一条都没读。**
- **没有 `## Procedure` / `## Before you begin`**——本篇正文只有四节 ＋ `Related information` ＋ `Functional changes`。
  **所以 `## 典型用法` 是照四节内容拼的，不是照原文步骤抄的。**
- **没有在任何真实机台上查过号**（`verified: doc-only`）。
  **`265` 到底配 `DPS 3` 还是 `DPS 1`、备用号在 7.10.3 上有没有，本页只能保证「文档这么写」（§11）**——
  **而文档自己的两处写法是冲突的**，见下 ⚠️②。
- **上表那张「配对表」是本页从位置表的单元格逐格读出来重排的**（那是把散在 `|` 分隔行里的
  `DPS 3` / `(265)` 成对读出）。**重排不丢字，但它是本页做的整理，原文没有这张表。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `鈥` 族坏字 13 处 / 8 行**（第 38、184、189、201、205、234、235、327 行）。
> 按 §11.2 ①，这一类是**三字节字符的第三字节丢了**，**只许报区间（U+2000–U+203F），不许当映射用**。
> 本篇实际出现的两种形态：
>
> | 形态 | 例（逐字） | 行 |
> |---|---|---|
> | `鈥?nbsp;`（第三字节被换成 `?`，**并且吃掉了 `&nbsp;` 的 `&`**） | `the DPS 1 鈥?nbsp;8 and UTIL 1 鈥?nbsp;8 pogo blocks` | 38 |
> | `鈥?`（同上，后面是空格） | `- Group 1 鈥?8:The pogo blocks are organized in eight groups` | 184 |
>
> **⚠️ 不要只把它当成「一个短横」**：`鈥?nbsp;` 里那个 `?` 和后面残缺的 `nbsp;` 都是坏字的一部分，
> **把 `鈥` 替成 `-` 会得到 `- ?nbsp;` 这种残形**。**照原样引，并记在这儿。**
>
> **② 两处写法冲突：265–272 与 DPS 1–8 的顺序。**
> 位置表给的是 `DPS 3` 配 `(265)`、`DPS 8` 配 `(268)`；
> 而清单表写的是 `265, 266, 267, 268, 269, 270, 271, 272` → `Alternate designation for DPS 1 鈥?DPS 8`。
> **原文没有把两处调和**，只在脚注 [3)] 里说
> `Note: The sequence of block 265 ... 272 and DPS 1 鈥?DPS 8 differs. For the correct assignment from block 265 ... 272 to DPS 1 鈥?DPS 8, refer to the Pogo_block_locations_table above.`
> **本页照实记，并采用位置表**（因为原文明确要求以它为准）。
>
> **③ 第 184 行冒号后没有空格**：`- Group 1 鈥?8:The pogo blocks are organized` —— `8:The` 之间**没有空格**。原文如此。
>
> **④ `## Related information` 那一整段链接与文字粘连。** 第 319 行逐字开头是
> `[Pogo mapping](<../02.05_Test_Head_Cards/02.05.01.04_Pogo_mapping.md>)SmarTest 7.6.x: Model file sections[SmarTest 7.10.x: Model file sections](<../02.04_Model_File_and_Licensing/02.04.01.03_Model_file_sections.md>)`——
> **四条之间一个分隔符都没有**；而且 **`SmarTest 7.6.x: Model file sections` 这一条根本没有链接**，
> **7.10.x 那一条有**。**原文如此，本页不替它补链接也不替它补空格。**
> （`layout-information-dut-board` 那页记的 `Files of the package:` 粘连、`special-test-suites` 那页的 `Note` 粘连，是同一形态。）
>
> **⑤ `Virtual pogo blocks` 那张表被压坏了：表头下面没有数据行。**
> 第 256–257 行的表头逐字是 `|   | Group  | Pogo block range  | Usage |`，
> **紧接着的不是 16 行数据，而是 `For more information refer to` 的三条列表**；
> 真正的 16 行数据（`501` 到 `832`）**在列表之后才出现**。
> 同时，**「四逻辑板的物理块再多留两个虚拟块、用偏移」那一段被切进了列表项的中间**
> （原文那一句的完整逐字见 `## 是什么` 里那一处引文）。
> **原文如此（这是 HTML 表格被压平的形态），本页不改结构、只照实记。**
>
> **⑥ 「本节包含什么」那个表只有一格。** 第 24–28 行逐字是 ` |` 单独一行，
> 七条内部链接实际是以列表形式散在它前后，**不是表格内容**。
>
> **⑦ 一处本页不判的写法**：WSMM 那一行的两个端点是 `190901 ... 890208`——
> **两个端点看起来不同族**，原文没有解释它们是什么区间。
> **本页照实引，不当它错、也不替它反推**（§11）。
>
> **⑧ §11.2 ⑤ 那族「整词替换」（`DC/DC power units`）在本篇没有出现。**
> 记这一条是为了**把「查过」和「没查」分开**（§13.1 ⑥′）：
> 本页确实去找了，**只找到 ① 那一族**。

`verified: doc-only`
