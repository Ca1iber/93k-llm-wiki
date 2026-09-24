---
type: object
title: ETIM, ETIM? - (Edge TIMing)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# ETIM, ETIM? - (Edge TIMing)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,005 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### ETIM

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

### ETIM?

```
ETIM? {waveform_set}, {timing_set}, {(pinlist)}
```

returns:

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

or:

```
ETIM? {specset_id}, {timing_set_no}, {(pinlist)}
```

returns:

```
ETIM {specset_id}, {timing_set_no}, [t1], [t2], [t3], [t4], [t5], [t6],{(pinlist)}
```

Parameters
 |

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets.

 |
 |

specset_id

 |

Derived as follows:

`100 *`equation_set_no `+ `specset_no

 |
 |

timing_set

 |

Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by TSUS.

 |
 |

t1..t6

 |

Edge delay in ns. Note that the positions of some edges may be affected by the use and position of previously defined edges as explained in "Restrictions" in `ETIM, ETIM? - (Edge TIMing)`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）.

 |
 |

pinlist

 |

The name of the pin or pins for which edge delays are to be set or read back. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.

 |

### Example

```
ETIM 1,1,2,4,8,6,10,,(DATA)
```

This example sets the edge delays for the pin group DATA specified for waveform set 1 and timing set 1. Edges 1 to 5 are set to 2,4,8,6 and 10 ns respectively, edge 6 is unused. If no previous setting for edge 6 exists in waveform set 1 and timing set 1, then its delay remains at 0.0 ns.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）command.
- timing_set is greater than the range allowed by the `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）command.
- The selected primary timing set is not defined for the specified waveform set.
- The edge order is wrong; for instance a window open must come before a window close - a mismatch exists between edge delays of the selected timing set and the waveform definition - `WFDF, WFDF? - (WaveForm DeFinition)`（raw: `02.06.02.02.334_WFDF__WFDF__-__WaveForm_DeFinition.md`）, or the break waveform definition - `BWDF, BWDF? - (Break Waveform DeFinition)`（raw: `02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md`）.
- Edge placement is outside the allowed range.
- All edges of the same direction in the specified timing set do not lie within one period.
- specset_id does not reference a defined wavetable.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid.

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
