---
type: object
title: PSSL, PSSL? (Power Supply Safety Limits)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PSSL, PSSL? (Power Supply Safety Limits)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **776 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSSL

```
PSSL [min_voltage | OFF], [max_voltage | OFF], [max_source_current | OFF], [max_sink_current | OFF], {(pin_list)}
```

### Parameters

|

min_voltage

 |

Lowest allowed voltage in V. Must be 鈮?0.

 |
 |

max_voltage

 |

Highest allowed voltage in V. Must be 鈮?0.

 |
 |

max_source_current

 |

Highest allowed source current in A. Must be > 0.

 |
 |

max_sink_current

 |

Highest allowed sink current in A. Must be > 0.

 |
 |

pin_list

 |

Comma separated list of DPS power pins, previously defined by the `DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） command, and of DC signal (PMU) pins defined by the `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） command.

 |

### Example

```
PSSL OFF,OFF,OFF,OFF,(DPS_1)
PSSL -2,5,0.5,0.5,(DPS_2)
PSSL -1.5,3,0.5,0.5,(SIG_1A)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md>` 的 `## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Warnings

The firmware displays an error message when the safety limits specified by PSSL are exceeded by other firmware commands (for example `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`）).

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
