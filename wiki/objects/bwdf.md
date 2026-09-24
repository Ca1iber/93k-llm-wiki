---
type: object
title: BWDF, BWDF? - (Break Waveform DeFinition)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# BWDF, BWDF? - (Break Waveform DeFinition)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,820 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### BWDF

```
BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### BWDF?

```
BWDF? {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {(pinlist)}
```

returns:

```
BWDF {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### Parameters

|

wvf_set

 |

Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 *` equation_set_no `+ ` specset_no

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes.

 |
 |

multiport_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

a1..a6

 |

Edge action. The actions you can define are:

 |
 |

N

 |

no action

 |
 |

F0N

 |

drive 0, no tri-state action

 |
 |

F1N

 |

drive 1, no tri-state action

 |
 |

FN0

 |

no drive action, tri-state off

 |
 |

FNZ

 |

no drive action, tri-state on

 |
 |

F00

 |

drive 0, tri-state off

 |
 |

F0Z

 |

drive 0, tri-state on

 |
 |

F10

 |

drive 1, tri-state off

 |
 |

F1Z

 |

drive 1, tri-state on

 |
 |

pinlist

 |

The name of the pin or pins for which break waveform definitions are to be made or read back. The symbol @ can be used to specify all configured input and IO pins. If more than one pin is to be included, the names must be separated with a comma.

 |

### Example

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

This example defines a pulse for waveform set 1, and for pins D0 to D3, driving to 1 at edge action 4 and to 0 at edge action 5. The tri-state formatter is not used.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

- waveform_set is greater than the range allowed by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.
- There is a mismatch between the edge actions and edge order in the specified waveform.
- A tri-state action is defined or implicitly required on edge 2 or 5.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid, or because specset_id does not reference a defined wavetable.

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
