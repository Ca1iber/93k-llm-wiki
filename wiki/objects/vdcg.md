---
type: object
title: VDCG? - (Verify Device Cycle for Group)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.321_VDCG__-__Verify_Device_Cycle_for_Group.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VDCG? - (Verify Device Cycle for Group)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,017 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.321_VDCG__-__Verify_Device_Cycle_for_Group.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VDCG? {waveform_set}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {waveform_set}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {specset_id}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {specset_id}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {wavetable_name}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {wavetable_name}, {dev_cyc_name}, {dev_cyc_len}
```

### Parameters

|

waveform_set

 |

Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes.

 |
 |

dev_cyc_name

 |

The device cycle name. Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes.

Alternatively, you can enter:

 |
 |

 |

ALL

 |

With this specifier the command checks that:

- The pins in pinlist have exactly the same device cycle names.
- For each device cycle, each pin defines the device cycle with the same length.
 |
 |

 |

FDC

 |

With this specifier the command checks that the first device cycle in the device cycle definition table for each pin in the pinlist has the same length.

 |
 |

pinlist

 |

The pin name or names whose device cycles are to be checked. If more than one pin is required, the names must be separated with a comma. The @ character can be used to read all configured pins.

 |
 | dev_cyc_len  | Always 1 for SmarTest 7.10. |

### Example

```
VDCG? 1,ALL,(inputs)
```

returns:

```
VDCG 1,ALL,SLEN
```

This example checks the consistency of all device cycles for pins in the pin group "inputs" in waveform set 1. The test system replies that all device cycles for the specified group are consistently defined.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.321_VDCG__-__Verify_Device_Cycle_for_Group.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The waveform set is outside the valid range as set by `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid.
- specset_id does not reference a defined wavetable.
- wavetable_name does not reference a defined wavetable.

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
