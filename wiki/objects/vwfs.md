---
type: object
title: VWFS? - (Verify WaveForm Sets)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VWFS? - (Verify WaveForm Sets)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,094 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VWFS? {waveform_set_1},{waveform_set_2},{(pinlist)}
```

returns:

```
VWFS {status}, {(pinlist)}
```

### Parameters

|

waveform_set_x

 |

Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

pinlist

 |

The name of the pin or pins for which you wish to check waveform set compatibility. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.

 |
 |

status

 |

The system returns:

 |
 |

 |

0

 |

The waveform sets are not compatible.

 |
 |

 |

1

 |

The waveform sets are compatible.

 |

### Example

```
VWFS? 1,2,(DATA)
```

This example checks whether waveform sets 1 and 2 are the same for the pins in the group DATA. If they are the same the following string is returned:

```
VWFS 1,(DATA)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.

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
