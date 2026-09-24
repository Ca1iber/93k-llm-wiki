---
type: object
title: TERM, TERM? - (TERMination mode)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# TERM, TERM? - (TERMination mode)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,689 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### TERM

```
TERM {level_set_no | level_set_id}, [term_mode], [term_pulldown,] [param_1], [param_2], [param_3],
 [l_range], [h_range], [hr_mode,] {(pinlist)}
```

### TERM?

```
TERM? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
TERM {level_set_no | level_set_id}, {term_mode}, [term_pulldown,] [param_1], [param_2], [param_3],
 [l_range], [h_range], [hr_mode,] {(pinlist)}
```

### Parameters

|

level_set_no

 |

The identification number of the level set in which you want the definitions to be included. The number must not exceed the maximum number of level sets allowed (as defined by `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）) and the level sets used (as defined by `LSUS`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`）). Entering ALL in this field sets the termination mode for all existing level sets (except level set 0). Entering PRM in this field defines the termination mode for the primary level set.

Standard level sets have a number > 0. Level set 0 is a dedicated level set for digital pins in high-Z state. For more information see `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`）.

 |
 |

level_set_id

 |

Derived as follows:

`100000 * equation_set_no + 1000 * specset_no + level_set_no`

 |
 |

term_mode

 |

The termination mode has dependencies to pin types and to the parameters (term_pulldown and param_1 to param_3 - see the syntax). The allowed combinations are shown in the Termination modes table, below.

Level set 0 only supports the termination modes OFF (the default), T, C, and A.

 |
 |

term_pulldown

 |

Extra parameter that defines the pull down mode. For more information refer to column term_mode of table Termination modes below.

The query returns the parameter only if it is defined for the queried level set.

 |
 |

param_1

 |

The use of this parameter depends on the termination mode as shown in the Termination modes table, below. When used, param_1 gives the termination voltage, active load commutation voltage, or the clamp low level voltage. The units are mV.

 |
 |

param_2

 |

The use of this parameter depends on the termination mode as shown in the Termination modes table, below. When used, param_2 defines the active load Iol current, or the clamp high level voltage. The units are mA or mV respectively.

When used, param_2 defines either

- the active load Iol current in 碌A,
- the clamp high level voltage in mV, or
- the receiver swing voltage in mV.

For the NP termination modes SP, SM, SEP, or SEM, param_2 defines the receiver threshold in mV.

 |
 |

param_3

 |

The use of this parameter depends on the termination mode as shown in the Termination modes table, below:

- For term_mode = A, param_3 defines the active load Ioh current. The units are 碌A.
- For term_mode = CT, param_3 defines the receiver offset in mV.
- For term_mode = bidir_receiver, param_3 defines the receiver offset in mV.
 |
 |

l_range

 |

For term_mode `=`A the low level current range.

This parameter can be

- I5E3: Defines the low current range of 0 to 5 mA.
- I3E4: Defines the high current range of 0 to 30 mA.
- AUTO: Lets the firmware automatically select the correct range. Whenever possible, the system selects the lower range.

This parameter is not supported for AVI64.

 |
 |

h_range

 |

For term_mode `=`A the high level current range.

This parameter can be

- I5E3: Defines the low current range of 0 to 5 mA.
- I3E4: Defines the high current range of 0 to 30 mA.
- AUTO: Lets the firmware automatically select the correct range. Whenever possible, the system selects the lower range.
 |
 |

pinlist

 |

The pin name or names of those power supply outputs which have already been defined. If more than one pin is required, the names must be separated with a comma. The @ character can be used to read all configured power supply pins.

 |

### Example 1

```
TERM 1,T,-1500,,,,,(Q1)
```

This example terminates the output pin Q1 to -1500 mV in level set 1.

### Example 2

```
TERM 3,A,3000,1500,1000,I3E4,I3E4,(out)
```

This example sets the active load level of the pin group out to 3V, and sets Iol and Ioh current to 1.5 and 1.0 mA respectively. The 0 to 30 mA range is used for both the low and the high range.

### Example 3

```
TERM 1,CT,2000,,,,,(o1,o1-)
```

This example terminates the differential output pair (the o1 and o1- pins) to 2000 mV with center tap termination in level set 1.

### Example 4

```
TERM 1,OFF,PULLDOWN,,,,,,(Q1,Q2)
```

On a PS1600 card, this example switches on the pulldown resistor on the specified pins.

```
TERM 1,OFF,NONE,,,,,,(Q1,Q2)
```

On a PS1600 card, this example switches off the pulldown resistor on the specified pins.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md>` 的 `## Errors`、`## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- You use the wrong current range for the selected current.
- You use an incorrect parameter combination.
- You use too many parameters for the selected mode.
- The clamp voltage is out of range.
- The active load voltage is out of range.
- The active load current is out of range.
- The termination voltage is out of range.
- The low level voltage is higher than the high level voltage in clamp mode.
- You use the termination mode H or L for an o pin. Use the termination mode T.
- Parameter hr_mode is used for instruments other than AVI64.

### Warnings

A warning is generated if:

- Auto-correction of high or low level clamp voltage occurs.
- The range is auto-corrected due to an incompatible range and current combination.
- You enter too many parameters for the selected termination mode (see the table above).

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
