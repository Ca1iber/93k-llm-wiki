---
type: object
title: CLMP, CLMP? - (CLaMP level)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# CLMP, CLMP? - (CLaMP level)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,527 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CLMP

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### CLMP?

```
CLMP? {level_set|level_set_id}, {(pinlist)}
```

returns:

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### Parameters

|

level_set

 |

The identification number of the level set in which you want the levels to be included. The number must not exceed the maximum number of level sets allowed (as defined by the DSCP command). Specifying ALL sets the clamp levels for all existing level sets (except level set 0). Specifying PRM sets the clamp levels for the primary level set.

Standard level sets have a number > 0. Level set 0 is a dedicated level set for the high-Z state of digital pins. For more information see `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`）.

 |
 |

level_set_id

 |

Used in equation based level setup. It is derived as follows:

100000 * equation_set_no + 1000 * specset_no + level_set_no

Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.

 |
 |

clamp_mode

 |

ON | OFF

For the Pin Scale 3600, the clamps can be set to ON when std/fast mode is set to std, and termination mode is set to OFF or A (active load).

Pin Scale 9G cards do not have clamps. Setting clamp levels will be ignored.

For termination mode, see `TERM, TERM? - (TERMination mode)`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`）.

 |
 |

low_clamp_level

 |

An integer (in mV) which sets the low clamp level.

For the Pin Scale 800, the range is -1800 to 6800. At power-on this parameter assumes a default value of -250.

 |
 |

high_clamp_level

 |

An integer (in mV) which sets the high clamp level. For the Pin Scale 800, the range is -1800 to 6800, and the difference of high_clamp_level - low_clamp_level must be in the range 0 to 8.6 V.

 |
 |

pinlist

 |

The name of the pins for which the clamp levels are to be set. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. If more than one pin is to be included, the names must be separated by a comma. The symbol @ refers to all pins. You can include O and IO pin types in pinlist.

 |

### Example

```
CLMP 1,ON,-10,5100,(Q0,Q1,Q2,Q3)
```

This example sets the clamp levels for level set 1 for pins Q0, Q1, Q2 and Q3. The low clamp level is set to -10 mV, and the high clamp level is set to 5100 mV.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The high or low clamp level is out of range.
- The swing limitations are exceeded.
- The set number is out of range.
- The set number is out of the range defined by the DSCP command.
- The set number is out of the used range of sets (CLMP? only).

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
