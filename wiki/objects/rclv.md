---
type: object
title: RCLV, RCLV? - (ReCeive LeVel)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# RCLV, RCLV? - (ReCeive LeVel)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,008 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### RCLV

```
RCLV {level_set_no | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### RCLV?

```
RCLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
RCLV {level_set | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### Parameters

|

level_set

 |

The identification number of the level set in which you want the low and high threshold levels to be included. The number must not exceed the maximum number of level sets allowed (as defined by `DSCP, DSCP? - (Define System Control Parameter)`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）). If you enter a level set number that is outside the used range of sets defined by the LSUS command, a new level set is created. Typing ALL in this field sets the low and high threshold levels for all existing level sets (except level set 0). Typing PRM sets the low and high threshold levels for the primary level set.

Standard level sets have a number greater than 0. Level set 0 is a dedicated level set for sequencer state OFF. For more information see `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`）.

 |
 |

level_set_id

 |

Used in equation based level setup. It is derived as follows:

100000 * equation_set_no + 1000 * specset_no + level_set_no

Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.

 |
 |

vth

 |

Output threshold for FAST comparator (single threshold as opposed to high and low). The expression must define a value in millivolts (mV).

 |
 |

logic_0_level

 |

An integer (in mV) which sets the logic 0 threshold level of the comparator. This parameter represents the point where the comparator distinguishes between logic 0 and an intermediate level.

 |
 |

logic_1_level

 |

An integer (in mV) which sets the logic 1 threshold level of the comparator. This parameter represents the point where the comparator distinguishes between logic 1 and an intermediate level.

 |
 |

range

 |

This extra parameter selects the receive range in mV.

This parameter is currently not available.

Ranges of the high-speed voltage comparator:

- -8000.0 ... 8000.0 selects the 8 V range
- -40000.0 ... 80000.0 selects the -40 V ... +80 V range

Ranges of the high-resolution voltage comparator:

- -3000.0 ... 3000.0 selects the 3 V range
- -10000.0 ... 10000.0 selects the 10 V range
- -30000.0 ... 30000.0 selects the 30 V range
- -40000.0 ... 80000.0 selects the -40 V ... +80 V range

If not specified the best fit range will be selected based on logic_0_level and logic_1_level if a voltage comparator is selected.

Range of the high-resolution current comparator:

- A fixed range of 200 mA is set.

The query returns the parameter only if it is defined for the queried level set.

 |
 |

pinlist

 |

The name of the pin or pins whose threshold level you want to set. This parameter can also include groups previously created by the command `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ sets or reads the threshold levels for all output pins. You can include O or IO pins in pinlist.

 |

For card specifications, like level ranges, see `Digital Cards`（raw: `../02.02_Specifications/02.02.04_Digital_Cards.md`）, for example:

- `Pin Scale 1600`（raw: `../02.02_Specifications/02.02.04.01.03_PS1600_driver.md`）
- `Pins Scale 5000`（raw: `../02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md`）

### Example 1

```
RCLV 1,-1300,-750,(Q0)
```

This example sets the low level compare threshold for pin Q0 to -1300 mV and the high level compare threshold to -750 mV.

### Example 2

```
TERM 1,,,,,,HRV,(avi64Pin1)
RCLV 1,-1300,-750,3000,(avi64Pin1)
```

This example for an AVI64 pin sets the low level compare threshold to -1300 mV, the high level compare threshold to -750 mV, and the range to the 3 V range.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md>` 的 `## Errors`、`## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The low level threshold is out of range.
- The high level threshold is out of range.
- The threshold swing is out of range.
- The level set number smaller than one.
- The level set number is outside the range defined by the DSCP command.
- For the query the level set number is outside the used range of sets defined by the LSUS command.
- The parameter "range" exceeds the hardware defined maximum range.

### Warnings

A warning is generated if

- Auto-correction of logic 1 or 0 threshold occurs.
- A range is defined for the high-resolution current comparator. This range will be ignored.

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
