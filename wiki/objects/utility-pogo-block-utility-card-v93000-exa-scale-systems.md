---
type: object
title: Utility pogo block - Utility Card (V93000 EXA Scale systems)
layer: n/a
stage: project
tags: [utility-pogo-block, utility-card, exa-scale, pogo-pin-assignment, dut-board, sequencer, utility-lines, hardware]
related: [utility-card, utility-power-supplies, utility-line-assignments, utility-line-view, utility-pins-editor, sequencer-controlled-utility-lines, digital-pins-editor, pin-utility, pogo-block-compatibility, pogo-pad-and-via-design, dut-board-grounding, smartest-8.3.4, smartest-7.10.2, smartest-8.4.4]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Utility pogo block - Utility Card (V93000 EXA Scale systems)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,677 字符逐字取自** `<02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

 | Block 1 |
 |   | c  | a  | b  | d |
 | 1  | XPP5V  | URW00  | UGND  | URW16 |
 | 2  | XPP5V  | UGND  | URW01  | URW17 |
 | 3  | XPP5V  | URW02  | URW03  | URW18 |
 | 4  | XPP5Vs  | URW04  | UP5V  | URW19 |
 | 5  | UGNDs  | UP5V  | URW05  | URW20 |
 | 6  | UGND  | URW06  | URW07  | URW21 |
 | 7  | XPM5V  | URW08  | UGND  | URW22 |
 | 8  | XPM5V  | DSC  | URW09  | URW23 |
 | 9  | XPM5Vs  | URW10  | UGND  | UGND |
 | 10  | UGND  | UGND  | URW11  | URW24 |
 | 11  | POG4R  | URW12  | UGND  | URW25 |
 | 12  | XPP3V3  | SINP  | URW13  | URW26 |
 | 13  | XPP3V3  | URW14  | SOUT  | URW27 |
 | 14  | XPP3V3s  | UGND  | URW15  | URW28 |
 | 15  | PGND  | PDCS  | PDCF  | URW29 |
 | 16  | NC  | PGDS  | PGRD  | URW30 |
 | 17  | XDCGD  | FRAMn  | SCLK  | URW31  | |

### Tables（脚本逐字抽取，第 2 张）

 | Block 2 and 8 |
 |   | c  | a  | b  | d |
 | 1  | XPP5V  | URW00  | UGND  | URW16 |
 | 2  | XPP5V  | UGND  | URW01  | URW17 |
 | 3  | XPP5V  | URW02  | URW03  | URW18 |
 | 4  | XPP5Vs  | URW04  | UP5V  | URW19 |
 | 5  | UGNDs  | UP5V  | URW05  | URW20 |
 | 6  | UGND  | URW06  | URW07  | URW21 |
 | 7  | XPM5V  | URW08  | UGND  | URW22 |
 | 8  | XPM5V  | DSC  | URW09  | URW23 |
 | 9  | XPM5Vs  | URW10  | UGND  | UGND |
 | 10  | UGND  | UGND  | URW11  | URW24 |
 | 11  | POG4R  | URW12  | UGND  | URW25 |
 | 12  | XPP3V3  | SINP  | URW13  | URW26 |
 | 13  | XPP3V3  | URW14  | SOUT  | URW27 |
 | 14  | XPP3V3s  | UGND  | URW15  | URW28 |
 | 15  | UGND  | UPP15Vs  | UPP15V  | URW29 |
 | 16  | NC  | UPP15V  | UPP15V  | URW30 |
 | 17  | XDCGD  | FRAMn  | SCLK  | URW31 |

### Tables（脚本逐字抽取，第 3 张）

 | Block 3 and 5 |
 |   | c  | a  | b  | d |
 | 1  | XPP5V  | URW00  | UGND  | URW16 |
 | 2  | XPP5V  | UGND  | URW01  | URW17 |
 | 3  | XPP5V  | URW02  | URW03  | URW18 |
 | 4  | XPP5Vs  | URW04  | UP5V  | URW19 |
 | 5  | UGNDs  | UP5V  | URW05  | URW20 |
 | 6  | UGND  | URW06  | URW07  | URW21 |
 | 7  | XPM5V  | URW08  | UGND  | URW22 |
 | 8  | XPM5V  | DSC  | URW09  | URW23 |
 | 9  | XPM5Vs  | URW10  | UGND  | UGND |
 | 10  | UGND  | UGND  | URW11  | URW24 |
 | 11  | POG4R  | URW12  | UGND  | URW25 |
 | 12  | XPP3V3  | SINP  | URW13  | URW26 |
 | 13  | XPP3V3  | URW14  | SOUT  | URW27 |
 | 14  | XPP3V3s  | UGND  | URW15  | URW28 |
 | 15  | UGND  | UPM15Vs  | UPM15V  | URW29 |
 | 16  | NC  | UPM15V  | UPM15V  | URW30 |
 | 17  | XDCGD  | FRAMn  | SCLK  | URW31 |

### Tables（脚本逐字抽取，第 4 张）

 | Block 4 |
 |   | c  | a  | b  | d |
 | 1  | XPP5V  | URW00  | UGND  | URW16 |
 | 2  | XPP5V  | UGND  | URW01  | URW17 |
 | 3  | XPP5V  | URW02  | URW03  | URW18 |
 | 4  | XPP5Vs  | URW04  | UP5V  | URW19 |
 | 5  | UGNDs  | UP5V  | URW05  | URW20 |
 | 6  | UGND  | URW06  | URW07  | URW21 |
 | 7  | XPM5V  | URW08  | UGND  | URW22 |
 | 8  | XPM5V  | DSC  | URW09  | URW23 |
 | 9  | XPM5Vs  | URW10  | UGND  | UGND |
 | 10  | UGND  | UGND  | URW11  | URW24 |
 | 11  | POG4R  | URW12  | UGND  | URW25 |
 | 12  | XPP3V3  | SINP  | URW13  | URW26 |
 | 13  | XPP3V3  | URW14  | SOUT  | URW27 |
 | 14  | XPP3V3s  | UGND  | URW15  | URW28 |
 | 15  | UGND  | F24VAs  | F24VA  | URW29 |
 | 16  | NC  | F24VARs  | F24VAR  | URW30 |
 | 17  | XDCGD  | FRAMn  | SCLK  | URW31 |

### Tables（脚本逐字抽取，第 5 张）

 | Block 6 |
 |   | c  | a  | b  | d |
 | 1  | XPP5V  | URW00  | UGND  | URW16 |
 | 2  | XPP5V  | UGND  | URW01  | URW17 |
 | 3  | XPP5V  | URW02  | URW03  | URW18 |
 | 4  | XPP5Vs  | URW04  | UP5V  | URW19 |
 | 5  | UGNDs  | UP5V  | URW05  | URW20 |
 | 6  | UGND  | URW06  | URW07  | URW21 |
 | 7  | XPM5V  | URW08  | UGND  | URW22 |
 | 8  | XPM5V  | DSC  | URW09  | URW23 |
 | 9  | XPM5Vs  | URW10  | UGND  | UGND |
 | 10  | UGND  | UGND  | URW11  | URW24 |
 | 11  | POG4R  | URW12  | UGND  | URW25 |
 | 12  | XPP3V3  | SINP  | URW13  | URW26 |
 | 13  | XPP3V3  | URW14  | SOUT  | URW27 |
 | 14  | XPP3V3s  | UGND  | URW15  | URW28 |
 | 15  | UGND  | F24VBs  | F24VB  | URW29 |
 | 16  | NC  | F24VBRs  | F24VBR  | URW30 |
 | 17  | XDCGD  | FRAMn  | SCLK  | URW31 |

### Tables（脚本逐字抽取，第 6 张）

 | Block 7 |
 |   | c  | a  | b  | d |
 | 1  | XPP5V  | URW00  | UGND  | URW16 |
 | 2  | XPP5V  | UGND  | URW01  | URW17 |
 | 3  | XPP5V  | URW02  | URW03  | URW18 |
 | 4  | XPP5Vs  | URW04  | UP5V  | URW19 |
 | 5  | UGNDs  | UP5V  | URW05  | URW20 |
 | 6  | UGND  | URW06  | URW07  | URW21 |
 | 7  | XPM5V  | URW08  | UGND  | URW22 |
 | 8  | XPM5V  | DSC  | URW09  | URW23 |
 | 9  | XPM5Vs  | URW10  | UGND  | UGND |
 | 10  | UGND  | UGND  | URW11  | URW24 |
 | 11  | POG4R  | URW12  | UGND  | URW25 |
 | 12  | XPP3V3  | SINP  | URW13  | URW26 |
 | 13  | XPP3V3  | URW14  | SOUT  | URW27 |
 | 14  | XPP3V3s  | UGND  | URW15  | URW28 |
 | 15  | UGND  | RES.  | RES.  | URW29 |
 | 16  | NC  | RES.  | RES.  | URW30 |
 | 17  | XDCGD  | FRAMn  | SCLK  | URW31 |

### Tables（脚本逐字抽取，第 7 张）

 | PDCS  |   | I  | analog  | High sense line of the internal DC rail or high sense input of the DMM |
 | PGDS  |   | I  | analog  | Ground sense line of the internal DC rail or ground sense input of the DMM |
 | PGRD  |   | O  | analog  | Guard line of the internal DC rail |
 | PGND  |   |   | analog  | Ground / return line of the internal DC rail |
 | POG4R  | |

### Tables（脚本逐字抽取，第 8 张）

 | XPP3V3  |   | O  | power  | +3.3 V output of the Utility power supply - XP pins |
 | XPP5V  |   | O  | power  | +5 V output of the Utility power supply - XP pins |
 | XPM5Vs  |   | I  | power sense  | -5 V sense input of the Utility power supply - XP pins |

### Tables（脚本逐字抽取，第 9 张）

   | EXA Scale |
 | Utility block  |   | |
 | 1  |   | UTIL 1  | 165  |   | DPS 3  | 265 |
 | 2  |   | UTIL 2  | 166  |   | DPS 1  | 266 |
 | 3  |   | UTIL 3  | 167  |   | DPS 2  | 267 |
 | 4  |   | UTIL 4  | 168  |   | DPS 8  | 268 |
 | 5  |   | UTIL 5  | 169  |   | DPS 4  | 269 |
 | 6  |   | UTIL 6  | 170  |   | DPS 5  | 270 |
 | 7  |   | UTIL 7  | 171  |   | DPS 6  | 271 |
 | 8  |   | UTIL 8  | 172  |   | DPS 7  | 272 |

### Tables（脚本逐字抽取，第 10 张）

 | Supply  | Voltage  | Current  | Pins  | Block |
 | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8 |
 | `UP5V pins`（raw: `02.03.05.01_Utility_power_supply_-_UP5V_pins__V93000_EXA_Scale_systems.md`）  | +5.0 V  | 8.0 A  | UP5V  | X  | X  | X  | X  | X  | X  | X  | X |
 | `XP pins`（raw: `02.03.05.02_Utility_power_supply_-_XP_pins__V93000_EXA_Scale_systems.md`）  | +5.0 V  | 12.8 A  | XPP5V  | X  | X  | X  | X  | X  | X  | X  | X |
 | +3.3 V  | 6.0 A  | XPP3V3  | X  | X  | X  | X  | X  | X  | X  | X |
 | -5.0 V  | 6.0 A  | XPM5V  | X  | X  | X  | X  | X  | X  | X  | X |
 | `UPP15V UPM15V F24V pins`（raw: `02.03.05.03_Utility_power_supply_-_UPP15V___UPM15V___F24V_pins__V93000_EXA_Scale_sys.md`）  | +15.0 V  | 3.0 A  | UPP15V  |   | X  |   |   |   |   |   | X |
 | -15.0 V  | 3.0 A  | UPM15V  |   |   | X  |   | X  |   |   | |
 | 24 V  | 1.0 A  | F24VA  |   |   |   | X  |   |   |   | |
 | 24 V  | 1.0 A  | F24VB  |   |   |   |   |   | X  |   | |
 | Utility pogo block on `DUT interface`（raw: `02.03.03.01_DUT_interface_layout.md`） |
 | 1st Utility Card |

<!-- 语法节 end -->

## 是什么

**这是「装了 Utility Card 的 EXA Scale 系统」上一块 4 行 utility pogo block 的
pin 分配表 + 板上接线规则。** 原文第一句：

> 「V93000 EXA Scale systems can be equipped with the optional Utility Card (EK051A) that
> provides 256 dynamically controlled utility lines and several utility power supplies per card.
> The 256 utility lines and the utility power supplies are routed to eight 4-row utility pogo
> blocks.」

**一句里三个数**：**一张卡 `256` 条动态控制的 utility 线**、**`8` 个 4 行 utility pogo block**、
**每个卡 `EK051A`**。**线和电源一起从这 8 个 block 出去。**

**支持的机型**（原文那张一行小表）：`EXA Scale (SmarTest 7+8)`。

> **不装 Utility Card 的情况不在本页**，原文明确指向另一篇：
> `For the utility pogo pin assignment of a V93000 EXA Scale system that is not equipped with the
> optional Utility Card, refer to Utility pogo block - Basic configuration (V93000 EXA Scale
> systems).` ——**那是「基本配置」，本页是「装了卡的配置」，两者 pin 分配不同。**

### 一句话铁律：**4 行 utility block 的行序是 `c-a-b-d`，不是 `a-b-c-d`**

**这是全页最重的一条**，原文用 `CAUTION` 标出、逐字如下：

> 「CAUTION The 4-row utility block uses the row sequence c-a-b-d for compatibility with the 2-row
> utility block. This sequence is different to the row sequence a-b-c-d of other 4-row pogo
> blocks. Do not use the wrong row sequence a-b-c-d for the 4-row utility block. Use only the
> correct row sequence c-a-b-d for the 4-row utility block. Violating this rule results in
> unusable DUT boards.」

**后果写明是 `unusable DUT boards`（DUT 板报废）。**
**原因也写明了：为了和 2 行 utility block 兼容。**

**（推断）这条为什么容易犯**：原文说**别的 4 行 pogo block 都是 `a-b-c-d`**，
**只有 utility block 是 `c-a-b-d`** ——
**依据就是这句 `This sequence is different to the row sequence a-b-c-d of other 4-row pogo
blocks.`**。**也就是「同一个测试头上两种 4 行块，行序不一样」。**

### 八个 block：**第 1–14 行全同，差别全在第 15–17 行**

原文给了 8 张 block 的 pin 表（`Block 1` / `Block 2 and 8` / `Block 3 and 5` / `Block 4` /
`Block 6` / `Block 7`，**八块表被分成六张**）。**本页把 8 张表对齐后的结论如下。**

**第 1–14 行在八个 block 上一模一样**（`c` / `a` / `b` / `d` 四列）：

| 行 | c | a | b | d |
|---|---|---|---|---|
| **1–3** | `XPP5V` ×3 | `URW00` / `UGND` / `URW02` | `UGND` / `URW01` / `URW03` | `URW16` / `URW17` / `URW18` |
| **4** | `XPP5Vs` | `URW04` | **`UP5V`** | `URW19` |
| **5** | `UGNDs` | **`UP5V`** | `URW05` | `URW20` |
| **6** | `UGND` | `URW06` | `URW07` | `URW21` |
| **7–8** | `XPM5V` ×2 | `URW08` / `DSC` | `UGND` / `URW09` | `URW22` / `URW23` |
| **9** | `XPM5Vs` | `URW10` | `UGND` | `UGND` |
| **10–11** | `UGND` / `POG4R` | `UGND` / `URW12` | `URW11` / `UGND` | `URW24` / `URW25` |
| **12–14** | `XPP3V3` ×3 | `SINP` / `URW14` / `UGND` | `URW13` / **`SOUT`** / `URW15` | `URW26` / `URW27` / `URW28` |

**第 15–17 行才是「每块不一样」的地方**，**一列说清**：

| Block | 15 行（c / a / b / d） | 16 行（c / a / b / d） | 17 行 |
|---|---|---|---|
| **1** | **`PGND`** / `PDCS` / `PDCF` / `URW29` | `NC` / `PGDS` / `PGRD` / `URW30` | `XDCGD` / `FRAMn` / `SCLK` / `URW31` |
| **2 and 8** | `UGND` / **`UPP15Vs`** / **`UPP15V`** / `URW29` | `NC` / **`UPP15V`** / **`UPP15V`** / `URW30` | 同左 |
| **3 and 5** | `UGND` / **`UPM15Vs`** / **`UPM15V`** / `URW29` | `NC` / **`UPM15V`** / **`UPM15V`** / `URW30` | 同左 |
| **4** | `UGND` / **`F24VAs`** / **`F24VA`** / `URW29` | `NC` / **`F24VARs`** / **`F24VAR`** / `URW30` | 同左 |
| **6** | `UGND` / **`F24VBs`** / **`F24VB`** / `URW29` | `NC` / **`F24VBRs`** / **`F24VBR`** / `URW30` | 同左 |
| **7** | `UGND` / **`RES.`** / **`RES.`** / `URW29` | `NC` / **`RES.`** / **`RES.`** / `URW30` | 同左 |

**原文把这张差别的说法统一成模板**，每个 block 后面都跟着同一段（**只换电源名**）：

> 「Differences to block 1:
> - "PDCS", "PDCF", "PGDS", "PGRD" on pins a15, a16, b15, b16 changed to "UPP15V" and "UPP15Vs".
> - "PGND" on pin c15 changed to "UGND".」

**注意 block 4 与 block 6 那句里写的是 `"F24VA..."` / `"F24VB..."`（带省略号）**，
**其余几块写全名**——**本页照原样引，不替它补全。**

**三处要点：**

1. **`UP5V` 在每块上占 4 行 5 列两个 pin（`b4` 和 `a5`）而 `UP5V` 的电源映射表说它在
   全部 8 块上都有**（`Pins` 列写 `UP5V`，Block 1–8 全是 `X`）——
   **即 `+5 V` 是八块都带的那一路。**
2. **`URW##` 从 `URW00` 到 `URW31` 铺满 8 块**：`c` 列不出现 `URW`，
   **`a` 列有 `URW00`–`URW15`（`URW01` / `URW03` / `URW05` / `URW07` / `URW09` / `URW11` /
   `URW13` / `URW15`），`b` 列有 `URW02` / `URW04` / `URW06` / `URW08` / `URW10` / `URW12` /
   `URW14`（加上 `URW00`），`d` 列是 `URW16`–`URW31`。**
3. **`RES.`（block 7）与 `NC` 是两回事**：原文 pin 说明里把两者合成一条
   （`NC / RES.` → `Not connected / Reserved for future use`），
   **一块上出现 `RES.` 的地方在 block 1 上是 `PDCS` / `PDCF` / `PGDS` / `PGRD` 那五个内部
   DC rail pin。**

### 电源在哪些 block 上：**`±15 V` 与 `24 V` 都不满配**

原文 `## Utility power supply mapping of the Utility Card` 表（**本页重排，数值逐字**）：

| 电源 | 电压 | 电流 | Pins | 在哪些 block 上 |
|---|---|---|---|---|
| `UP5V pins` | `+5.0 V` | **`8.0 A`** | `UP5V` | **1–8 全有** |
| `XP pins` | `+5.0 V` | **`12.8 A`** | `XPP5V` | **1–8 全有** |
| `XP pins` | `+3.3 V` | **`6.0 A`** | `XPP3V3` | **1–8 全有** |
| `XP pins` | `-5.0 V` | **`6.0 A`** | `XPM5V` | **1–8 全有** |
| `UPP15V UPM15V F24V pins` | `+15.0 V` | **`3.0 A`** | `UPP15V` | **只有 block 2 和 8** |
| 同上 | `-15.0 V` | **`3.0 A`** | `UPM15V` | **只有 block 3 和 5** |
| 同上 | `24 V` | **`1.0 A`** | `F24VA` | **只有 block 4** |
| 同上 | `24 V` | **`1.0 A`** | `F24VB` | **只有 block 6** |

**这张表是本页唯一的「电流数字」来源**：
**`+5 V` 那一路 XPP5V 是 12.8 A，UP5V 是 8.0 A，两路是分开的。**
**（推断）block 1 和 7 没有任何 `±15 V` / `24 V` 输出**——
**依据是上表那四行的 `X` 都没落在 1 和 7 上**，**而原文那张表就是用 `X` 标有无的**。

### 八个 block 映射到 DUT 接口的哪一块：**两张卡不一样**

**这是 `## Mapping of pin groups and utility pogo blocks` 与 `## Utility pogo block mapping`
两节讲的事**，原文：

> 「The assignment of the eight utility pogo blocks to the pogo blocks on the DUT interface is
> different for the first and second Utility Card. The mapping affects also the availability of
> the utility supplies on UPP15V / UPM15V / F24V pins.」

| Utility block | **第 1 张 Utility Card**：老机型 → / **EXA Scale** → | **第 2 张 Utility Card**：老机型 → / **EXA Scale** → |
|---|---|---|
| 1 | `UTIL 1` / **165** | **`DPS 3`** / **265** |
| 2 | `UTIL 2` / **166** | **`DPS 1`** / **266** |
| 3 | `UTIL 3` / **167** | **`DPS 2`** / **267** |
| 4 | `UTIL 4` / **168** | **`DPS 8`** / **268** |
| 5 | `UTIL 5` / **169** | **`DPS 4`** / **269** |
| 6 | `UTIL 6` / **170** | **`DPS 5`** / **270** |
| 7 | `UTIL 7` / **171** | **`DPS 6`** / **271** |
| 8 | `UTIL 8` / **172** | **`DPS 7`** / **272** |

**两处要点：**

1. **第 2 张卡不是按顺序映射的**：`DPS 3, 1, 2, 8, 4, 5, 6, 7`——
   **block 1 落到 `DPS 3`，block 4 落到 `DPS 8`。**
   **（推断）这就是原文说的「mapping affects also the availability of the utility supplies on
   UPP15V / UPM15V / F24V pins」的机制**——
   **`+15 V` 只在 block 2/8、`-15 V` 只在 3/5、`24 V` 只在 4/6，
   而第 2 张卡上这些 block 又映射到 `DPS 1`/`DPS 7`/`DPS 2`/`DPS 5`/`DPS 8`/`DPS 6`
   这些非顺序的位置上**；**依据是「block → 电源分布」与「block → DPS 映射」两张表的交叉**。
   **原文只说了「有影响」，没说怎么影响，所以这是推断。**
2. **老机型那一列共用同一个编号**：`UTIL 1 … 8` 是第 1 张卡，
   `DPS 1 … 8` 是第 2 张卡；**原文说这是因为 `DPS 1 … DPS 8` 这些 legacy pogo block
   在 EXA Scale 上「要么给第 2 张 Utility Card、要么给 `Internal Utility Power Option` 用」**：
   > 「In V93000 EXA Scale systems, the legacy pogo blocks DPS 1 鈥?nbsp;DPS 8 are used either for the
   > optional 2nd Utility Card or for the Internal Utility Power Option.」

   **⚠️ 上面引文里的 `鈥?nbsp;` 是原文就有的**（**编码损坏的破折号**，
   本页**没有替它还原**，按 §11.2 照实引；同一处损坏在「出处」里另有逐字记录）。

### 板上接线规则：原文 `## Wiring rules and notes` 五条 + 每个 pin 的 Notes 列

**五条集中列的规则**（**逐字**）：

| 规则 |
|---|
| 「Connect all pogo pins of all blocks of a utility supply output to a **separate power plane** on the DUT board.」 |
| 「Connect all sense pins of all blocks of a utility supply output to the related power plane.」 |
| 「**Utility power supply pogo pins of different Utility Cards must not be connected together.**」 |
| 「Maximum offset of utility ground to system ground: **±0.5 V**」 |
| pins `URW14` 和 `URW15`（**utility block 1 / `UTIL 1`**）**内部连到系统的 DUT Interface EEPROM**，可用来再控最多三个 EEPROM；**不能挪作他用**，否则 DUT Interface EEPROM 的读出可能损坏（如 EDC dump 进行中 dock 板子） |

**第三条在 pin 说明里被逐路重复了四遍**（`UP5V` / `UPP15V` / `UPM15V` / `XP...` 各一遍），
**每次的说法是 `Do not connect … power output pins of different Utility Cards together.`**

**每个 pin 自己那格里的硬要求，拣最要紧的：**

| Pin | 要求（**逐字或紧贴原文**） |
|---|---|
| **`POG4R`** | **「Every POG4R pin has to be connected to UGND on a DUT board that utilizes 4-row utility pogo blocks.」**；2 行板上**要留空焊盘**；**只有接了 UGND，系统才认这是 4 行 block** |
| **`DSC`** | **「The DSC pin of every utility block has to be connected to UGND on the DUT board.」**；低=板子已连，高/悬空=未连 |
| **`UGND`** | **「Provides the return path for all utility power supplies and all utility lines」**；**每块上的每个 `UGND` 都要接到板上公共地平面** |
| **`UGNDs`** | 所有 utility pogo block 的 `UGNDs` 都接到公共 `UGND` 地平面 |
| **`UP5V`** | **一张卡所有 pogo block 的两个 `UP5V` pin 要在板上连在一起**；**输出电压是在 pogo 线缆组件的 pogo pin 处内部感测的** |
| **`UPP15V` / `UPM15V`** | **同一张卡的两块 block** 的电源输出接到公共电源平面；**不同卡不要连一起** |
| **`XDCGD`** | XP pins 电源的 Power OK：**低=全部已稳定，高=至少一路未稳定**；**默认 EXA Scale 行为下这个 pin 没有功能、恒为低** |
| **`FRAMn` / `SCLK` / `SINP` / `SOUT`** | **SmarTest 7 + `EK051A` 上**：功能与 V93000 Pin Scale / Smart Scale 相同；**SmarTest 8 上**：utility 线走内部数据连接，**这四个 pin 没有功能、不必连**（老板子还能 dock，数据会自动改道） |
| **`NC` / `RES.`** | **「Do not connect these pins on the DUT board.」** |
| **`PDCF` / `PDCS` / `PGDS` / `PGRD` / `PGND`** | 内部 DC rail 的一组；**「The five pins are reserved for future use and require the optional Utility Card to be installed.」** |

**（推断）「那五个 pin」指的是 `PDCF` / `PDCS` / `PGDS` / `PGRD` / `PGND`**——
**依据是那句旁边只有 `PDCF` 那一格写着 `The five pins`，
而 block 1 上非通用、非电源的 pin 正好是这五个**（`a15` `a16` `b15` `b16` `c15`）。

### pin 编号方案：**三套叫法**

原文在 `## Wiring rules and notes` 里给了 `URW##` 的三种记法：

| 谁 | 记法 |
|---|---|
| **pin 名** | `URW00 ... URW15`（2 行 block）或 `URW00 ... URW31`（4 行 block） |
| **SmarTest 8** | `#01 – #16` 或 `#01 – #32`，`#` = utility pogo block 号 `1 ... 8`；**三位数的 pogo pin 号要在 DUT board description file 里定义** |
| **SmarTest 7** | `UTI#01 ... UTI#16` 或 `UTI#01 ... UTI#32`，`#` 同上 |
| **EXA Scale（7 和 8 都是）** | `###01 ... ###32`，`###` = **`Utility pogo block mapping` 里那个三位 block 号** |

> **最后一条带一句 `Note`，是最容易漏的一处**：
> 「Note An offset of 1 is to be considered for transferring the utility pogo pin definitions of
> this section to SmarTest.」
> ——**即：本节表格里的编号搬到 SmarTest 时要加 1。**

### 还有一组 pin：Utility DC pins（**只给 SmarTest 7.10**）

原文 `## Utility DC pins` 一节：

> 「The utility DC pins support connection of utility card pins via the DC rail to external
> instruments connected to the test-head. The following channel specifications are used in the
> Digital pins editor:」

| `Digital Pins Editor` 里的 Utility DC pin | 对应 |
|---|---|
| `UTIDC165` | **第 1 张 utility card** |
| `UTIDC265` | **第 2 张 utility card** |

**＋一句 `Note`：`The Utility DC pins are supported only in SmarTest 7.10.`**

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`。** 它把用法写成了
**「五个 specific setup tasks」的清单**（页首列的）：

| Setup task | 对应本页哪一节 |
|---|---|
| `Mapping of pin groups and utility pogo blocks` | 八个 block 与 DUT 接口的映射（+ 那张 `351272.png` 布局图） |
| `Mapping of pins on a 4-row utility pogo block` | **8 张 block pin 表**（本页 `## 是什么` 里对齐过了） |
| `Pin description` | **pin 说明表** |
| `Utility pogo block mapping` | **`UTIL n` / `DPS n` / 三位编号**那张表 |
| `Utility power supply mapping of the Utility Card` | **电源 → block** 那张表 |

**所以这块的做法就是「查表 + 守规则」，能落成动作的有下面这些：**

**1. 画板子之前先定行序**：**utility block 用 `c-a-b-d`**，
**别照别的 4 行块写 `a-b-c-d`**——**原文说违反这条会得到 `unusable DUT boards`。**

**2. 板上必须接地的两个「认板」pin**：`POG4R`（**系统靠它认 4 行块**）和 `DSC`（**系统靠它认板子在不在**），
**两者都必须接 `UGND`**。

**3. 电源平面按「同一张卡」划**：
**同一张卡的所有 block 的同一路输出接到公共平面；不同卡的输出绝不相连。**
**地平面单独一条**：所有 `UGND` 接到公共地平面，**utility 地对系统地最大偏移 `±0.5 V`。**

**4. 感测线照电源平面接**：所有 block 的 sense pin 接到对应输出的电源平面；
**那一路不用就把 sense pin 空着。**

**5. 留 `URW14` / `URW15`（block 1）给 EEPROM**：
它们内部连着系统的 DUT Interface EEPROM，**不能挪作他用**。

**6. 用 `URW` 的编号时记住两层偏移**：
**先查 `Utility pogo block mapping` 拿三位 block 号（第 2 张卡不是顺序的），
搬到 SmarTest 时再加 1。**

**7. 如果板子要在 SmarTest 7 和 8 上都用**：
`FRAMn` / `SCLK` / `SINP` / `SOUT` 这四个 pin **在 SmarTest 8 上无功能**——
**原文说老板子仍可 dock、数据会自动改道到内部连接**，
**所以这四个 pin 不必为了 SmarTest 8 改板。**

## 和谁有关

- [[utility-card]] — **上游，硬件本体**。本页第一句说的就是那张卡的 256 条线与几路电源；
  **本页讲的是「这些资源从哪八个 block 出去、pin 怎么定义」，
  那张卡讲「卡本身提供什么」。**
- [[utility-power-supplies]] — **上游，电源侧**。
  本页那张「电源 → block」表里的 `UP5V pins` / `XP pins` /
  `UPP15V UPM15V F24V pins` **三条链接直接指向它**；
  **电压/电流的规格与开关行为在那页，本页只有「在哪些 block 上」。**
- [[sequencer-controlled-utility-lines]] — **最直接的下游**。
  `FRAMn` / `SCLK` / `SINP` / `SOUT` 四个 pin 的说明**两处**指向它；
  **本页只说这四个 pin 是「用于 sequencer 控制 utility 线的串行接口」，
  怎么用在那页。**
- [[utility-line-view]] / [[utility-line-assignments]] / [[utility-pins-editor]] —
  **软件侧**。原文在讲 `URW##` 编号时把 `Utility Line view` 与
  `Defining a utility line` 点出来；**本页是 pin 级的物理定义，
  那几页是软件里怎么分配与查看。**
- [[digital-pins-editor]] — **同族的另一个编辑器**。
  `## Utility DC pins` 一节明说那两个通道名
  （`UTIDC165` / `UTIDC265`）**是「used in the Digital pins editor」**；
  **本页只有这两个名字与它们对应第几张卡。**
- [[pin-utility]] — **对象侧同类**。本页的 `URW##` 是 utility 线在 pogo 上的落点；
  **utility 线自身的电气特性本页没有**（原文指向 `Utility line characteristics`）。
- [[pogo-block-compatibility]] / [[pogo-pad-and-via-design]] — **板上设计侧同族**。
  本页只给「哪个 pin 在哪一格」与接线规则，**pogo 的机械兼容性与 pad/via 设计不在本页。**
- [[dut-board-grounding]] — **直接相关**。`UGND` 那一格的 Notes 明确指向
  `Grounding` 与 `Connecting the different grounds on the DUT board`；
  **本页只有「接到公共地平面」与「最大偏移 ±0.5 V」两条。**
- [[smartest-8.3.4]] / [[smartest-7.10.2]] / [[smartest-8.4.4]] — **版本页**。
  本页 `## 版本` 两条的落点。
- `Utility pogo block - Basic configuration (V93000 EXA Scale systems)`（**未建**）—
  **对照组**：**没装 Utility Card 时的 pin 分配**。原文用一句话把读者分流过去；**本页没读它。**
- `Internal Utility Power Option` / `DUT interface layout` / `Utility lines` /
  `Utility line characteristics` / `Utility Lines and DUT Board EEPROMs` /
  `Grounding` / `Connecting the different grounds on the DUT board` /
  `DUT board description file reference` / `Controlling utility lines` /
  `Defining a utility line` / `Utility Card specific setup tasks`（**均未建**）—
  原文点名的那一批。**尤其 `DUT interface layout`（那张 `351272.png` 布局图所在的文档）
  没读，所以「八个 block 在测试头上怎么排」本页只有编号、没有布局。**
- `SmarTest 7.10` / `EDC dump`（**均未建/不在清单**）— 原文提到的两个名字。

## 版本

本文档**有** `## Functional changes` 段，**两条**：

- **Introduced in SmarTest 8.3.4**
- **`SmarTest 7.10.2 / 8.4.4: Block 1, pin c15 changed from "UGND" to "PGND".`**

> **这两条要对着看，因为它们对不上**：
> 引入写的是 **SmarTest 8.3.4**（**SmarTest 8 的版本号**），
> 而第二条把一个变更同时记在 **SmarTest 7.10.2**（**SmarTest 7 的版本号**）和 **8.4.4** 上。
> **7.10.2 早于 8.3.4** —— **一条 7.x 的变更记在一个 8.x 才引入的功能上。**
> 而页首那张小表写的是 `Supported V93000 systems : EXA Scale (SmarTest 7+8)`，
> 正文里也反复出现 `running SmarTest 7` 的说法，**说明它在 SmarTest 7 上确实存在**。
> **本页并列三处，不替它们调和，也不判哪一条写错了。**
>
> **第二条也解释了正文里一个不一致**：block 1 的 pin 表第 15 行 `c` 列写的是 `PGND`，
> **而其他七个 block 的同一格写的是 `UGND`**（每条 `Differences to block 1` 都写着
> `"PGND" on pin c15 changed to "UGND".`）。
> **这正是那条 7.10.2 / 8.4.4 变更留下的痕迹。**

> ⚠️ **段末粘着脚注定义**（`[1)](<>) Internal pull up resistor[2)](<>) Except the Internal Utility
> Power Option (V93000 EXA Scale systems).`）——
> **又是 §11.2 ③ 那个现象**：`## Functional changes` 是最后一个 `## ` 段。
> **两个脚注定义还挤在同一行、中间没有分隔符**，**照字面读像一个脚注**。
> **它们不是版本条目**：`[1]` 是 `DSC` / `POG4R` / `XDCGD` 那几格里的 `digital` 标注，
> `[2]` 是 `UGND` / `UGNDs` 那两格的例外说明。

## 出处

`sources:` 一篇：
`02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`

**本页没做的：**

- **pin 说明表没有一个字搬进本页正文。** 本页只把**每个 pin 那格里最要紧的一句**
  抽成了一张表（`POG4R` / `DSC` / `UGND` / `UP5V` / `XDCGD` / `FRAMn` 等），
  **其余 pin（`F24VA` / `F24VAs` / `F24VAR` / `F24VARs` / `PDCF` / `PDCS` / `PGDS` /
  `PGRD` / `PGND` / `UPM15Vs` / `UPP15Vs` / `XPM5Vs` / `XPP3V3s` / `XPP5Vs` 等）
  各自的完整说明、以及每个 pin 的 `Type` 列（`I` / `O` / `I/O` / `n/a`）
  与电气类别列（`digital` / `analog` / `power` / `power sense` / `floating power` /
  `TTL and OC` / `LVTTL`），本页没有逐条展开。**
- **8 张 block 表本页是「对齐后重排」的，不是照抄。**
  **第 1–14 行那张表是本页压缩过的**（`URW` 那一列压成了区间写法），
  **要看某一行某个 pin 的确切名字，得回原文或看本页「语法 / 参数」节里脚本逐字抽的
  第 1–6 张表。**
- **那张 `351272.png` 布局图没看。** alt 文本是
  `Layout of utility and DPS blocks - Utility Card configuration of V93000 EXA Scale systems.`
  ——**所以八个 block 在测试头上怎么排、`UTIL` / `DPS` / 三位编号之间的空间关系，
  本页完全不知道。** 原文有一节专门讲它的映射，**本页只有那张数字表。**
  **还有 `153013.png`（`Utility block 4-row`）也没看** —— **4 行 block 长什么样本页不知道。**
- **`Utility pogo block - Basic configuration`（未装卡的配置）没读** ——
  所以**两张配置的 pin 差异本页给不出**，只知道原文说要去那篇看。
- **`DUT interface layout` 没读** —— 所以 `DPS 1 … DPS 8` / `UTIL 1 … 8` 在测试头上的位置，
  以及「`DPS 1…8` 要么给第 2 张卡、要么给 `Internal Utility Power Option`」这条怎么落地，
  **本页只有那句转述。**
- **`Sequencer-controlled utility lines` 没读** —— 所以
  `FRAMn` / `SCLK` / `SINP` / `SOUT` 这条串行口怎么用、sequencer 怎么控线，**本页没有。**
- **`Utility line characteristics` 没读** —— **`URW##` 的电气特性（`TTL and OC` 到底什么含义）
  本页没有**，只知道类型列写着 `TTL and OC`。
- **`Utility Lines and DUT Board EEPROMs` 没读** ——
  所以 `URW14` / `URW15` 怎么控那三个 EEPROM，**本页只有那一句警告。**
- **`Utility Card specific setup tasks` 没读** —— 所以 `XDCGD` 那句里提到的
  `utility_power_featureset`（`Global compatibility settings` 里的参数）**本页不知道在哪儿设。**
- **`DUT board description file reference` / `Controlling utility lines` /
  `Defining a utility line` 都没读** ——
  **所以「三位数 pogo pin 号在 DUT board description file 里怎么写」这个动作本页没有。**
- **`Grounding` / `Connecting the different grounds on the DUT board` 没读。**
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 编码损坏：`鈥` 形态 9 行，`卤` / `鈥憆` 等同类 5 行。**
> **这一篇里就有 §11.2 ① 举例用的那个词**——`Sequencer鈥慶ontrolled utility lines`
> （**= `Sequencer-controlled`，两处**）。**逐字再举几个本页正文用到的**：
> - `In V93000 EXA Scale systems, the legacy pogo blocks DPS 1 鈥?nbsp;DPS 8 are used …`
>   （**`鈥?nbsp;` 是那个范围破折号**）；
> - `The 4鈥憆ow utility block uses the row sequence c-a-b-d`（**= `4-row`**）、
>   `compatibility with the 2鈥憆ow utility block`（**= `2-row`**）；
> - `Maximum offset of utility ground to system ground: 卤0.5 V`（**`卤` = `±`**）；
> - `#01 鈥?nbsp;#16 or #01 鈥?nbsp;#32`、`URW00 鈥?nbsp;URW31`、
>   `The three鈥慸igit pogo pin number`（**= `three-digit`**）、
>   `the three鈥慸igit utility pogo block number`。
> **代价照 §11.2 ① 写清楚：拿修好的 `4-row` / `Sequencer-controlled` 去 raw 里搜是搜不到的。**
> **本页正文里凡是要写这些词的地方，都用的是修好的写法；引文里一律照原样。**
>
> **② 映射表的表头把 `Utility` 拼成了 `Utilty`。** 逐字：
> `|   | 1st Utility Card  |   | 2nd Utilty Card |`
> ——**`2nd Utilty Card` 少一个 `i`。本页正文按正确的 `Utility` 写，引文照原样。**
>
> **③ 脚本把这一篇抽成了 10 张「表」，而其中第 7、8 两张是同一张 pin 说明表被切剩下的碎片。**
> 看 `## 语法 / 参数` 节：第 7 张只剩 `PDCS` / `PGDS` / `PGRD` / `PGND` 四行加一行 `| POG4R  | |`，
> 第 8 张只剩 `XPP3V3` / `XPP5V` / `XPM5Vs` 三行，
> **第 9 张是 `Utility block → UTIL/DPS/三位号` 那 8 行，第 10 张是「电源 → block」表
> 但只抽到第 1 张卡的行头就断了**（以 `| 1st Utility Card |` 结尾）。
> **这不是脚本的错，是原文的表格结构碎了**：
> `## Pin description` 那张 6 列表的每一行都被空行、多行单元格和
> `|` 分隔符切散（例如 `| POG4R  | |` 下面单独一行写 `I`，再一行写 `|`，
> 再一行才写 `digital[1)]`）。
> **本页 `## 是什么` 里对 pin 说明的概括，是照着原文的散段读出来的，不是照语法节。**
>
> **④ `POG4R` 那一行的类型列被拆成了四行。** 逐字：
> ` | POG4R  | |` / `I` / ` |` / `digital[1)](<#_347642__d6071e426>)`
> ——**同一格的内容散在四行里。** 本页正文把它当 `I` / `digital` 讲。
>
> **⑤ `PGND` 那一行的 `Type` 列是空的。** 逐字：
> ` | PGND  |   |   | analog  | Ground / return line of the internal DC rail |`
> ——**`analog` 前面那一格（`Type`）是空的**，而同一组里 `PDCS` / `PGDS` 写 `I`、
> `PGRD` / `PDCF` 写 `O`。**本页照实说「类型列空着」，不替它填。**
>
> **⑥ `Note` 又被粘在正文后面，中间没有分隔符。**
> 逐字：`…refer to Utility Lines and DUT Board EEPROMs.Note Utility pins URW14 and URW15 on
> utility block 1 are not to be used for a purpose other than EEPROM access otherwise the
> readout from the DUT Interface EEPROM may become corrupted.`
> ——**`EEPROMs` 和 `Note` 之间连空格都没有。**
>
> **⑦ `## Utility DC pins` 里那个 `Note` 被放进了第三个表格单元。**
> 逐字：` | UTIDC265  | 2nd utility card  |  Note The Utility DC pins are supported only in
> SmarTest 7.10.`
> ——**那张表只有两列**，这条 `Note` 成了第三格。**本页把它当独立的一句讲。**
>
> **⑧ 语法错误两处，逐字**：
> - `The functionality of the pin depends of the compatibility settings for the XP pins utility
>   power supply:` ——**`depends of` 应为 `depends on`**；
> - `Leave both sense pins of UPP15V unconnected if the related output is not used`
>   ——**句末没有句号**（同一格里 `UPP15Vs` 的说明最后一格）。
>
> **⑨ `## Related information` 一节里 4 个链接全粘在一起**，**中间没有任何分隔符**。
>
> **⑩ `EEPROMS` 与 `EEPROMs` 两种写法并存**：同一段里先写
> `can be used to control up to three more EEPROMS on the DUT board or probe card`，
> 后面又写 `the readout from the DUT Interface EEPROM`。
> **本页不替它统一大小写。**
>
> **⑪ 引脚表里 `UP5V` 的 `Type` 列是空的**（`| UP5V  |   |   | power  | …`），
> 而同组的 `UPP15V` / `UPM15V` / `XPM5V` 都写 `O`。
> **本页照实说，不替它填。**
>
> **⑫ 原文的 `Note` 与 `CAUTION` 这两个词后面没有冒号或换行**，
> 直接接正文（`Note The assignment of …`、`CAUTION The 4-row utility block uses …`）。
> **本页引文照原样，正文里加了分隔。**
>
> **⑬ 一条可能被读漏的版本事实（不是瑕疵，但原文没给它醒目的位置）**：
> `## Utility DC pins` 里那句 `The Utility DC pins are supported only in SmarTest 7.10.`
> ——**它是一条可用性声明，但 `## Functional changes` 段里没有对应的条目。**
> **本页并列两处，不判这是漏记还是「7.10」指的是 7.10.x 全系。**

`verified: doc-only`
