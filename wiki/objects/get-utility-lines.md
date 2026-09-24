---
type: object
title: GetUtilityLines
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# GetUtilityLines

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,259 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

|

Parameter

 |

Type

 |

Description

 |
 | blockId  | INT |

The utility pogo block to query.

The valid value is from 0 to 8.

If the three鈥慸igit format for pogo blocks is used, the valid range is 165 ... 172.

For the second optional `Utility Card`（raw: `../02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md`） of EXA Scale systems, the utility pogo blocks can be defined using only the three鈥慸igit format. The valid range for the second card is `265` ... `272`.

See also `Utility pogo block mapping`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md#_347642__s_Utility_pogo_block_mapping`） in `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`）.

0 means all utility line blocks and other valid number means the specified utility block.

 |

### Example

### Output for two utility cards of an V93000 EXA Scale system

 Output with parameter blockId of the test method set to 0. The pogo blocks of the second optional `Utility Card`（raw: `../02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md`） are listed as 265 to 272.

```
get utility block 1             =01111100101110100100010010011010
get utility block 2             =10000110110110010001101100111000
get utility block 3             =01110100010101011011111110110101
get utility block 4             =00111011101100011001010011110010
get utility block 5             =11010100110011111000100111100010
get utility block 6             =11101110100001011111010001010011
get utility block 7             =10010001011011000101101011010011
get utility block 8             =10001110010111000011001010111011
get utility block 265           =00001101000000110101001000000001
get utility block 266           =11000100010111010111011011111101
get utility block 267           =00000100110101111001100110111110
get utility block 268           =01000000100110101010011000111100
get utility block 269           =01001100010101101010011001100011
get utility block 270           =11100000010000000100100000111000
get utility block 271           =10001000000101000001110001010101
get utility block 272           =11101011100101100011100010011001
```

<!-- 语法节 end -->

## 是什么

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
