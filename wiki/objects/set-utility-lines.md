---
type: object
title: SetUtilityLines
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# SetUtilityLines

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,814 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.md>`。**不是转述。**
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
 | type  | STRING |

The type of the utility line. It can be:

-

UtilitylineName: The utility line name defined in the `Pin setting editors`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.18.03.01_Pin_setting_editors.md`）.

 The utility lines to be set to on or to off can be defined by parameters

  - utilityLineNameOn,
  - utilityLineNameOff, or
  - utilityPurpose.

All three parameters can be filled with data at the same time.

-

UtilitylineChannel: Utility lines are defined by the channel number.

 The utility channels to be set to on or to off can be defined by parameters

  - utilityLineChannelOn or
  - utilityLineChannelOff.

Both parameters can be filled with data at the same time.

 |
 | utilityLineNameOn  | STRING |

A single utility pin or a comma鈥憇eparated list of utility pins to be set to on or to off.

Valid names are defined in the `Utility Pins editor`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.md`）.

 |
 | utilityLineNameOff |
 | utilityPurpose  | STRING |

A utility purpose or a comma鈥憇eparated list of utility purposes to be applied.

Valid names are defined in the `Pin setting editors`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.18.03.01_Pin_setting_editors.md`） and configured in the `Utility Purpose Editor`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.18.03.01.05_Utility_Purpose_Editor.md`）.

 |
 | utilityLineChannelOn  | STRING |

A single utility channel or a comma鈥憇eparated list of utility channels to be set to on or to off.

The utility channels are to be defined like `UTI101`, `UTI102`.

The format using three digits for the pogo blocks is also supported. For this format, the utility pins are to be defined as `UTI16501` or `UTI16502`, for example.

For the second optional `Utility Card`（raw: `../02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md`） of EXA Scale systems, the utility pins can be defined only using the three鈥慸igit format of the pogo blocks. The valid range for the second card is `UTI26501` ... `UTI27232`.

See also `Utility pogo block mapping`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md#_347642__s_Utility_pogo_block_mapping`） in `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`）.

 |
 | utilityLineChannelOff |
 | waittime  | DOUBLE |

The time to wait after controlling all relays. It must not be negative.

Default value is 0.0.

Units are seconds.

 |

For a coding example see the file /opt/hp93000/soc/testmethod/library/miscellaneous_tml/SetUtilityLines.cpp in `Miscellaneous test methods (miscellaneous_tml)`（raw: `02.07.05.04_Miscellaneous_test_methods__miscellaneous_tml.md`）

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
