---
type: object
title: DFUP, DFUP? - (DeFine Utility Purpose)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DFUP, DFUP? - (DeFine Utility Purpose)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,060 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFUP

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### DFUP?

```
DFUP? {(purpose_name)}
```

returns

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### Parameters

| ch_No_list |

Utility line channel numbers to be defined as the members of a utility purpose and specified with five digits. The channels must be separated with a comma.

In the five鈥慸igit format, the first three digits of the channel numbers specify the utility pogo block. For valid pogo blocks, refer to `DUT interface layout`（raw: `../02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md`） and to `Utility pogo block mapping`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md#_347642__s_Utility_pogo_block_mapping`） in `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`）.

The legacy three鈥慸igit format is also supported: The first digit (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.

The last two digits specify the channel number 01 ... 32 of the utility line.

On the utility pogo blocks, an offset of -1 is to be considered and the channel number is URW00 ... URW31.

When reading the defined utility lines with the DFUP? command, the data returned always have the five鈥慸igit format. The same applies to the `PALS?`（raw: `02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md`） command.

The channel numbers 16515 and 16516 should not be used. They should only be accessed with the `I2CA`（raw: `02.06.02.02.142_I2CA__I2CA__-__I2CA_bus.md`）or the `BDID`（raw: `02.06.02.02.09_BDID__BDID__-__BoarD_ID.md`）firmware command.

 |
 | setting |

Output states for each channel in the ch_No_list. Specify the setting of each utility line with the following specifiers:

- 0: sets the corresponding (write) channel to high (high impedance state)
- 1: sets the corresponding (write) channel to low
- X (x): no action

Specify the setting values corresponding to the definition order of the ch_No_list parameter.

The number of characters must be equal to the number of the utility line channels in the ch_No_list parameter.

Note that the settings must be explicitly activated with `UPST`（raw: `02.06.02.02.305_UPST__UPST__-__Utility_Purpose_STate.md`） and `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`）.

 |
 | purpose_name |

Name of the utility purpose. In the query you can use the symbol @ to list all defined utility purposes.

This parameter can have up to 16 alphanumeric characters and must not contain blank spaces, or any of the following characters: `# ; ( ' ' ) ? @ ,`

 |

### Example

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

This example defines a utility purpose AWG_CNCT and activates its standard settings.

The members and the setting values are as follows:

```
Member:      16501  16502  16503  16504
---------------------------------------
Setting:     0      1      1      0
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The channel number is out of range.
- The given name is already assigned to a digital pin, analog pin, DPS pin, or utility name.
- The specified channel has already been defined in the DFUT command as READ ONLY capability.
- Incompatible settings are specified for a channel (for example, `DFUP (101,101),"10", (bad)`).
- The setting contains characters other than "0", "1" and "X (or x)".
- The number of characters in the setting is not equal to that of the channel list.

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
