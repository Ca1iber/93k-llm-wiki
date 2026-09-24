---
type: object
title: PCLK, PCLK? - (Pin CLocK)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PCLK, PCLK? - (Pin CLocK)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,374 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PCLK

Fixed timing:

```
PCLK{waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### PCLK?

Fixed timing:

```
PCLK?{waveform_set},{timing_set},{(pinlist)} [,query_mode]
```

returns:

```
PCLK {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK? {specset_id|"multi-port_spec"}, {timing_set}, {(pinlist|portlist)} [,query_mode]
```

returns:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### Parameters

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets.

 |
 |

specset_id

 |

Used for equation based timing. It is derived as follows:

100 * equation_set_no + specset_no

Note that if you change the period for an equation based timing setup, PCLK will only change the runtime value, not the setup value specified in the timing set.

 |
 |

multi-port_spec

 |

In the command, you cannot enter a multi-port specification unless the specification is associated with the default port, and no other ports are configured. This restriction does not apply to the query.

 |
 |

timing_set

 |

Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）.

 |
 |

period

 |

Enter the test system period in ns. The period range depends on the model. For the Pin Scale 800, the range is 2.5 ns to 31250 ns. All values entered (or queried regardless of query_mode) are in ns and will be rounded to nine digits after the decimal point (atto-seconds) according to the accuracy of the firmware. The power-on default value for all configured pins also depends on the model.

 |
 |

pinlist

 |

The name of the pin or pins whose period you want to define or read back. This parameter can also include groups previously created by `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to set or read the periods for all configured pins. If you do not use @, the firmware assumes asynchronous operation.

 |
 |

portlist

 |

In the query, you must specify a list of ports, if you have specified a multi-port specification for the first parameter.

 |
 |

query_mode

 |

In the query, you can specify whether the period specified by the user or the corrected period calculated by the system is to be returned. The allowed values are:

WANT: The period defined by the user is returned. This is also the default.

EXACT: The period calculated by the system is returned.

 |

### Example 1

```
PCLK 101,1,20,(@)
```

This example sets the test system period for specification 101 to 20 ns.

### Example 2

```
PCLK 101,1,40,(S1)
```

This example sets the test system period of pin S1 for specification 101 to 40 ns.

The `VCLK?`（raw: `02.06.02.02.319_VCLK__-__Verify_CLocK.md`） query checks whether a PCLK command with the specified parameter values was accepted with or without auto-correction.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- timing_set is greater than the range allowed by the `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） command.
- The period lies outside the given range.

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
