---
type: object
title: PSLV, PSLV? - (Power Supply LeVel)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PSLV, PSLV? - (Power Supply LeVel)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,671 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSLV

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

  Note If equation based testing is being used, you specify a DPS set ID instead of a DPS set number.  Note PSLV ALL only applies changes to all non-equation-based DPS sets.

### PSLV?

```
PSLV? {dps_No|dps_set_id}, {(pinlist)}
```

returns:

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

 Note PSLV? ALL returns information for non-equation-based DPS sets only.

### Parameters

Note The settling time parameter (setup_time) of the PSLV command and the rise_... and fall_... parameters of the `PSSR, PSSR? -(Power Supply Slew Rate)`（raw: `02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md`） command exclude each other. This also applies to the t_ms equation parameter (see `DPSPINS`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md`） and `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）).

 |

dps_No

 |

Needed for non-equation-based setup.

 |
 |

dps_No

 |

The identification number of the DPS set which you want to modify. The number must not exceed the maximum number allowed (as defined by the DSCP (Define System Control Parameter) command.

 |
 |

ALL

 |

Modifies all the existing fixed DPS sets.

 |
 |

PRM

 |

Modifies the primary DPS set.

 |
 |

ACT

 |

(Only for PSLV?) Displays the settings of the actual enabled DPS set.

 |
 |

dps_set_id

 |

Needed for equation-based setup.

This parameter is derived as follows:

`100000*equation_set_no + 1000*specset_no+1`

 |
 |

voltage

 |

The optional parameter voltage defines the output voltage (in V) of the DPS. Applicable value depends on the DPS type.

 |
 |

source_current

 |

The optional parameter defines the source current limit (ilimit_source) in [A]. The applicable value depends on the DPS type.

The parameter defines the source and the sink current limit if both values are equal.

The parameter defines only the source current limit if the sink_current parameter is used.

 |
 | sink_current |

The extra parameter defines the sink current limit (ilimit_sink) in [A].

The parameter is required only if the source and sink current limits are set to different values. This parameter defines then the sink current limit while the source current limit is defined by the above source_current parameter.

The parameter is not required if the current limits are programmed symmetrically to the same (absolute) value. Both, the source and the sink value are then defined by the source_current parameter.

The query answer shows the sink_current parameter only if the programmed sink current limit is not symmetrical to the source current limit.

 |
 |

impedance

 |

The optional parameter sets the DPS output impedance. You can select:

- LOZ sets the DPS output impedance to low when the test system is in the disconnect state. The current limit remains at the same level as in the active state, while the force voltage is set to 0 V.
- HIZ sets the DPS output to high impedance when the test system is in the disconnect state. This sets the channel to the minimum possible current limit. HIZ is the default state for DPS-slot types. If it is applied to DC Scale cards, HIZ_R is used instead of HIZ.
- HIZ_R sets the DPS output to high impedance by switching the output relay off when the test system is in the disconnect state.

Note that relay switching is slower than with HIZ.

- LOZ_HIZ combines LOZ with HIZ. First, the DPS is switched to 0 V with an unchanged current limit (just like in LOZ mode). After the output voltage has reached 0 V (卤50 mV) or after a timeout of 1 second, the DPS pin is switched to high impedance. This combines the advantages of both modes. A capacitor on the load board is quickly discharged and then the DPS pin is switched to high impedance. This is safer when changing the DUT or DUT board after a disconnect.
- LOZ_HIZ_R combines LOZ with HIZ_R. First, the DPS is switched to 0 V with an unchanged current limit (just like in LOZ mode). After the output voltage has reached 0 V (卤50mV) or after a timeout of 1 second, the DPS pin is switched to open. This combines the advantages of both modes. A capacitor on the DUT board is quickly discharged and then the DPS pin is switched to high impedance. This is safer when changing the DUT or the DUT board after a disconnect.
 |
 |

setup_time

 |

The optional parameter is an integer which specifies the settling time (in ms) of the DPS. All DPS's are synchronized so that they finish their settling periods at the same point in time. This is the point when the system is switched to the connect state. If there are, for example, two DPS's, one with a settling time of 10 ms, and the other with a settling time of 4 ms, then the second DPS will be started 6 ms after the first:

   !`Synchronizing Different DPS Settling Times`（raw: `../../../../raw/93235.png`）

The range is from -2147483647 up to 2147483646 ms.

 The default value is 0.Note setup_time has a resolution of ms (floating point values are rounded to nearest integer). |
 |

pinlist

 |

pinlist must contain the names of pins previously defined by the `DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） command. If more than one pin is specified, the names must be separated by commas. The character @ can be used to set the levels for all DPS pins.

 |

### Example

```
PSLV 1,5.2,0.5,HIZ,15,(Vee)
```

This example sets the following parameters for device pin Vee:

- DPS set 1
- A voltage of 5.2 V
- A current limit of 0.5 A
- Minimum current limit when the test system is disconnected
- A setup time of 15 ms

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The DPS set number is out of range.
- The programmed voltage is out of range.
- The programmed current is out of range.
- A communication error with the DPS occurs.
- The programmed voltage reaches the overvoltage limit.

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
