---
type: object
title: DFUT, DFUT? - (DeFine UTility line)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DFUT, DFUT? - (DeFine UTility line)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,697 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFUT

```
DFUT {ch_No}, {type}, {(util_name)}
```

### DFUT?

```
DFUT? {(util_name)}
```

returns

```
DFUT {ch_No}, {type}, {(util_name)}
```

### Parameters

| ch_No |

Channel number of the utility line specified with five or three digits.

In the five鈥慸igit format, the first three digits specify the utility pogo block. For valid pogo blocks, refer to `DUT interface layout`（raw: `../02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md`） and to `Utility pogo block mapping`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md#_347642__s_Utility_pogo_block_mapping`） in `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`）.

In the legacy three鈥慸igit format, the first digit (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.

The last two digits specify the channel number 01 ... 32 of the utility line.

On the utility pogo blocks, an offset of -1 is to be considered and the channel number is URW00 ... URW31.

When reading the defined utility lines with the DFUT? command, the data returned always have the five鈥慸igit format. The same applies to the `PALS?`（raw: `02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md`） command.

For more information, see `Utility line assignments`（raw: `../02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.md`） and `DUT interface layout`（raw: `../02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md`）

 |
 | type |

Specifies the operating mode of the utility line with the following specifiers:

- W: Write-Only
- R: Read-Only
- RW: Read-Write

Utility lines of the optional `Utility Card`（raw: `../02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md`） can also be configured as safety lines or as global shutdown line for hardware鈥慶ontrolled shutdown of XPS256 pins:

- TRIGGER_IF_HIGH: Safety line
- TRIGGER_IF_LOW: Safety line
- TRIGGER_SITE_IF_HIGH: Global shutdown line
- TRIGGER_SITE_IF_LOW: Global shutdown line

For more information, refer to `XPS256 safety line and DUT board disconnect`（raw: `../02.05_Test_Head_Cards/02.05.05.03.03.06_XPS256_safety_line_and_DUT_board_disconnect.md`）.

 |
 | util_name |

Name of the utility line. For the query, it specifies the utility line name to be retrieved. @ can be used to list all defined utility lines.

This parameter can have up to 16 alphanumeric characters and must not contain blank spaces, or any of the following characters: `# ; ( ' ' ) ? @ ,`

 |

### Example

```
DFUT 16504,w,(filter)
```

This example assigns the name `filter` and operating mode w to utility line 4 of the first utility pogo block.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The channel number is out of range.
- The channel number is already used.
- The utility line name is out of range.
- The utility line name is already assigned to an analog or digital pin.

<!-- 报错节 end -->

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
