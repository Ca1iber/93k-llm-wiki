---
type: object
title: ETDS, ETDS? - (Edge Timing Definition String)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# ETDS, ETDS? - (Edge Timing Definition String)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,660 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### ETDS

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### ETDS?

ETDS? {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {(pinlist)}

returns:

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### Parameters

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query, you can also enter ALL for all waveform sets.

 |
 |

specset_id

 |

Derived as follows:

`100 *`equation_set_no `+ `specset_no

 |
 |

multi-port_spec

 |

For a multi-port setup, specify the name of a multi-port specification.

Note that the multi-port specification uniquely determines an equation set for every pin of pinlist, because no pin can belong to more than one port within a multi-port specification.

 |
 |

timing_set

 |

Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by TSUS.

 |
 |

mode

 |

The operating mode. For the query, you can enter ALL for all modes or BIDIR for bidirectional mode, that is, for edges that serve both as drive and receive edges.

With fast pins, you can specify the mode DELTA for both the command and the query. In this mode, the delays specified for edges with an index > 1 are interpreted as offsets from the calculated default values.

 |
 |

definition_string

 |

The definition string consists of a sequence of items each of which associates a delay with a drive or compare edge. On Pin Scale 800/3600 boards, drive edges are denoted by dn. On Pin Scale 9G boards, there are two kinds of drive edges, which are denoted by fn and sn, respectively; for details see `Defining waveforms for Pin Scale 9G pins`（raw: `02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`）. You can also use the dn notation for Pin Scale 9G channels, but mixing both notations in one string is not allowed. Receive edges are always denoted by rn.

Unless you employ the pdiv statement for fast pins (see below), all edges which are not explicitly set remain unchanged.

The range of the edge delay is -8000 ns to +24000 ns (or -4 to +12 test system periods) for the Pin Scale 3600/800.

On Pin Scale 800/3600 boards, the restrictions for edge ordering must be observed both in fixed and equation based timing. For example, you cannot assign a greater delay to d1 than to d3 if d1 precedes d3 in a waveform definition. For more information, see `Selecting and ordering edges`（raw: `02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）.

Note that with equation based timing, ETDS returns no error message when the edge order restrictions are violated.

On Pin Scale 9G boards, ordering of drive edges is not restricted in any way.

 |
 |

 |

Special Rules for Fast Pins:

If a pin is configured as a fast pin in the context of the specification given by the first parameter, you can specify the period divider at the start of the definition string. The format is pdiv:n, where n must be the same value as the period_div value of the pins in pinlist within the timing set specified by the timing_set parameter.

If you specify pdiv:nand a delay for the first edge, ETDS calculates delays for the following n-1 edges except those that are specified explicitly in the string. Note that for n = 3, the edges with index 1, 3, 5 are used for internal reasons.

If you omit either pdiv or the first edge, only the specified edges are modified. However, with receive edges this is only possible for r1.

The calculated delays are determined for the ith edge by the following formula:

 1st_edge_delay + (i-1) * (period/pdiv)

1st_edge_delay is the delay specified for the first edge (d1 or r1; the generic notation e1 is not allowed for fast pins). If the first edge is not specified in the string, its delay is set to 0. An example for the calculation will be given below.

Note that when both the period divider and a delay for the first edge are present in the definition string, then the delays for all the edges required by the period divider will be overwritten.

When a delay is explicitly specified for one of the edges, this delay overrides the calculated default. There are two formats to specify overrides. You can either define absolute delays or the offsets from the default delays.

If you want to use the second, relative format, you must specify DELTA for the modeparameter. Note that you can also specify negative offsets in the DELTA mode.

 |
 |

pinlist

 |

The name of the pin or pins for which edge delays are to be set or read back. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.

In a multi-port setup, every pin must belong to a port of the specified specification.

 |

### Example 1

```
> ETDS 1,1,,"e1:0 e2:2 e3:6 e4:4",(io)
> ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
> ETDS? 1,1,,(@)
< ETDS 1,1,,"d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4",(io)
< ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
```

### Example 2

The following example shows the various possibilities for using ETDS with fast pins:

```
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5 d3:10 d4:15",(CP)
> ETDS 401,1,,"d2:5.5",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5.5 d3:10 d4:15",(CP)
> ETDS 401,1,,"pdiv:4 d1:3 d3:14",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:14 d4:18",(CP)
> ETDS 401,1,DELTA,"d3:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:12 d4:18",(CP)
> ETDS 401,1,DELTA,"pdiv:4 d1:0 d2:1 d4:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:6 d3:10 d4:14",(CP)
```

Note in particular the effect of the first instance of the command in DELTA mode. The negative offset is not applied to the actual value of d3, which is 14, but to the calculated default value, which is 13.

### Example 3

This example shows how to set and retrieve a delay of a multi-port specification:

```
> ETDS? "mu_timing",2,,(In1)
< ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ETDS "mu_timing",2,,"d1:0.5",(In1)
> ETDS? "mu_timing",2,,(In1)
< ETDS "mu_timing",2,,"d1:0.5",(In1)
```

The specification name and the pin name identify the port (no pin may occur in more than one port within the same specification). Then the port and the specification identify the equation set.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）command.
- timing_set is greater than the range allowed by the `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）command.
- The selected primary timing set is not defined for the specified waveform set.
- The edge order is wrong; for instance a window open must come before a window close - a mismatch exists between edge delays of the selected timing set and the waveform definition - `WFDS, WFDS? - (WaveForm Definition String)`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）, or the break waveform definition - `BWDS, BWDS? - (Break Waveform Definition String)`（raw: `02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md`）.
-  Eplacement is outside the allowed range.
-  All edges of the same direction in the specified timing set do not lie within one period.

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
