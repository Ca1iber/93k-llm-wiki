---
type: object
title: VTIM? - (Verify TIMing)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VTIM? - (Verify TIMing)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,479 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VTIM? {waveform_set},{timing_set},{(pinlist)}
```

returns:

```
VTIM {status}
```

### Parameters

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

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

To query a multi-port specification, enter the name of the specification.

 |
 |

timing_set

 |

Specifies the timing sets to be checked. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）.

In a multi-port setup, the check is performed for those pins from pinlist that belong to the same port. If you specify a number, a timing set with this number must be present in every equation set that is associated with a port of the multi-port specification.

 |
 |

pinlist

 |

The name of the pin or pins to be checked. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.

In a multi-port setup, the pins can belong to more than one port. Only those pins are considered that belong to one of the ports of the specification.

 |
 |

status

 |

The system returns:

 |
 |

0

 |

The timing is not the same.

 |
 |

1

 |

The timing is the same.

 |

### Example

The following example illustrates the working of VTIM? in a multi-port setup. The pins S1_1 and DS0_1 belong to the same port, and S1_2 belongs to another one.

```
> ETDS? "spec_port_1_port_2",ALL,,(S1_1,DS0_1,S1_2)
< ETDS "spec_port_1_port_2",1,,"d1:0 d2:30",(S1_1,DS0_1)
< ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(S1_1)
< ETDS "spec_port_1_port_2",2,,"d1:1 d2:12",(DS0_1)
< ETDS "spec_port_1_port_2",1,,"d1:-0.67 d2:1.33 d3:9.3",(S1_2)
```

This call of `ETDS?`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） shows that the edge timings of S1_1 and DS0_1 are the same in timing set 1, but not in timing set 2 of the port to which these pins belong.

```
> PCLK? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< PCLK "spec_port_1_port_2",1,50,(S1_1)
< PCLK "spec_port_1_port_2",2,20,(S1_1)
< PCLK "spec_port_1_port_2",1,50,(DS0_1)
< PCLK "spec_port_1_port_2",2,20,(DS0_1)
< PCLK "spec_port_1_port_2",1,16.667,(S1_2)
```

This call of `PCLK?`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） shows that the periods of S1_1 and DS0_1 are the same in the two timing sets of the port.

```
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 0
```

VTIM? returns 0 because of the different timings for S1_1 and DS0_1 in timing set 2.

```
> ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(DS0_1)
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 1
```

After changing the edge timing of DS0_1 in timing set 2 to the values of S1_1 with a call of `ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`）, VTIM? returns 1 although DS0_1 has a different timing in timing set 1 and in timing set 2, and S1_2, which belongs to another port, has different values altogether.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The specified waveform set number is outside the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- The specified timing set number is outside the range allowed by the `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） command.

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
