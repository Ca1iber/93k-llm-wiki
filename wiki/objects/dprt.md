---
type: object
title: DPRT, DPRT? - (Default PRimary Timing sets)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.83_DPRT__DPRT__-__Default_PRimary_Timing_sets.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DPRT, DPRT? - (Default PRimary Timing sets)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,308 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.83_DPRT__DPRT__-__Default_PRimary_Timing_sets.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DPRT

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT {"multi-port_spec"}, [timing_set_no|"timing_set_list"][,(port)]
```

### DPRT?

```
DPRT?
```

returns:

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT?
```

returns:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT? [(port)]
```

returns:

```
DPRT {"multi-port_spec"}, {timing_set_no|"timing_set_list"}[,(port)]

```

### Parameters

|

waveform_set

 |

Waveform set number.

 |
 |

specset_id

 |

Derived as follows:

100 * equation_set_no + spec_set_no

Note that the spec set ID identifies the primary wavetable in equation based testing.

 |
 |

multi-port_spec

 |

In a multi-port setup, a primary multiport specification can be specified.

 |
 |

timing_set

 |

The identification number of the timing set. Enter an integer in the range 1 to the maximum number of allowed timing sets (of the selected waveform set or timing specification). The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of timing sets allowed (as defined by DSCP).

In a multiport setup, the timing set number applies to all ports of the specification if no port is specified. Otherwise, the number applies to the specified port.

 |
 |

timing_set_list

 |

In a multi-port setup, you can specify primary timing sets for all ports of the specification by entering a list of numbers separated by commas.

In the query, the numbers of the primary timing sets are returned in a list for all ports of the primary specification unless the numbers are identical for all ports or a port has been specified in the query.

 |
 |

port

 |

In a multi-port setup, you can specify a port of the specification that was entered as the first parameter. In this case, the timing set number specified as the second parameter will only be applied to the specified port. The port parameter is ignored if a timing set list is specified.

 |

### Example

```
DPRT?
```

returns:

```
DPRT 3,4
```

On sending a query the system reports that the default primary waveform set is 3 and the default primary timing set is 4.

<!-- 语法节 end -->

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
