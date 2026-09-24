---
type: object
title: EDSP, EDSP? - (EDge SPecification)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# EDSP, EDSP? - (EDge SPecification)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,730 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### EDSP

The edge_spec parameter specifies a physical edge (d1 through d8 or r1 through r8):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}
```

The edge_spec parameter is a data parameter (D1, D2, C1, C2, E1, or E2):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}
```

### EDSP?

```
EDSP? [dc_ref], {(pinlist)}
```

returns:

```
EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}
```

Parameters
 |

waveform_set

 |

Specifies a waveform set number for a fixed timing setup.

 |
 |

specset_id

 |

Specifies a spec set ID for an equation based setup. The spec set ID is derived from an equation set number and a spec set number as follows:

100 * equation_set_no + specset_no

 |
 |

multi-port_spec

 |

Specifies the name of a multiport specification for a multi-port setup. PRM is the default value.

 |
 |

timing_set

 |

Specifies the number of the a timing set. PRM is the default value.

 |
 |

edge_spec

 |

The edge specifier can either be a physical edge (d1 through d8 or r1 through r8), or one of the data parameters D1, D2, C1, C2 (drive parameters) or E1, E2 (receive parameters).

 |
 |

edge_number

 |

In the query reply, this parameter contains the edge that is used as leading or trailing edge.

 |
 |

dev_cyc_name

 |

Specifies the name of a logical device cycle that uses the data parameter given as the edge_spec. It must be defined for all pins in pinlist. If you do not enter a name in this parameter, the first device cycle in the device cycle table is used.

 |
 |

dc_ref

 |

This parameter specifies the input edge. The input edge determines the algorithm according to which the trailing edge is selected. The two options are LE (for "leading edge") and TE (for "trailing edge").

The leading edge will always be the first edge that is associated with the specified data parameter within the specified device cycle, regardless of whether LE or TE is specified.

For the trailing edge the following rules apply:

- When you specify LE, trailing and leading edge will be identical.
- When you specify TE, then drive parameters and receive parameters are treated differently.

  - Drive parameter: The trailing edge will be the first drive edge after the leading edge thats performs a data or tri-state action. Note that this trailing edge need not be associated in any way with the data parameter of the leading edge.
  - Receive parameter: If the action of the leading edge is an edge compare, leading and trailing edge will be identical. If it is the start action of a window compare, then the associated window close edge will be the trailing edge.

For both cases, see the example below.

In the query, you can also specify both. In this case both the leading and the trailing edge will be returned for the pins in pinlist.

 |
 |

direction

 |

This parameter can be in or out. If in is selected to define an input edge, then the edge_spec parameter must be D1, D2, C1, or C2. If out is selected to define a receiver edge, then the edge_spec parameter must be E1 or E2. If either in or out is selected along with an edge_spec parameter of 1,2...6, then a check is performed to ensure that the edges of all pins are in the required direction. If no entry is made in this parameter, the measuring edges of the pin in pinlist can have any direction or be unused.

 |
 |

pinlist

 |

The parameters of the EDSP command are applied to all pins named in this parameter. If more than one pin is used, the names must be separated by a comma.

In a multi-port setup, all pins must belong to the same port of the specification that was entered as the first parameter.

 |

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The edge_spec parameter specifies a drive edge, but the direction parameter specifies a compare edge, or the other way round.
- Pins of different periods are included in the pin list.
- You select an unused edge.
- The edge direction of the selected edge is not the same for all pins in the pin list.

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
