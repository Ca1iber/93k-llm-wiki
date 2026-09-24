---
type: object
title: VCLK? - (Verify CLocK)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VCLK? - (Verify CLocK)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,951 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VCLK? {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

returns:

```
VCLK {autocorrect}
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

multi-port_spec

 |

To enter a multi-port specification is only possible if the specification is associated with the default port and if no other ports are configured.

 |
 |

timing_set

 |

Timing set number. Enter PRM for the primary timing set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）.

 |
 |

period

 |

Enter the test system period in ns for which you wish to check whether auto-correction will take place or not. period must be within the maximum and minimum test system periods of the model.

 |
 |

pinlist

 |

The name of the pin or pins whose period you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The @ symbol can be used to check all configured pins.

 |
 |

autocorrect

 |

The auto-correction flag returned by the system. It can be:

 |
 |

0

 |

No auto-correction will occur.

 |
 |

1

 |

Auto-correction will occur.

 |

### Example

```
VCLK? 1,1,20,(@)
```

This example checks if a period of 20 ns will cause auto-correction to the edge placements in Timing Set 1 of Waveform Set 1 on any pin. If no auto-correction will occur the following string is returned:

```
VCLK 0
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The period is outside the given range.
- waveform_set is outside the valid range.
- timing_set is outside the valid range.

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
