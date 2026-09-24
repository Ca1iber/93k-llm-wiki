---
type: object
title: TSUX, TSUX? - (Timing Sets Used eXtended)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.284_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# TSUX, TSUX? - (Timing Sets Used eXtended)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **881 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.284_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### TSUX

```

TSUX {waveform_set},{timing_set}
```

### TSUX?

```

TSUX? {waveform_set}
```

returns:

```
TSUX {waveform_set},{timing_set}
```

### Parameters

|

waveform_set

 |

Waveform set number. Enter ALL for all waveform sets in the query command.

 |
 |

timing_set

 |

Timing set number. In the command, TSUX is set to this value for the specified waveform set, if the number is smaller than the current value of `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） for this set. Otherwise, it is set to the current value of TSUS.

 |
 |

SWAP

 |

This command parameter causes the values set by `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）and TSUX to be switched, that is, TSUS is set to the current value of TSUX , and TSUX to that of TSUS for the specified waveform set.

 |
 |

NONE

 |

This command parameter sets the value of TSUX back to 1 for the specified waveform set.

 |

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
