---
type: object
title: MSCF, MSCF? - (Modulation Set ConFiguration)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# MSCF, MSCF? - (Modulation Set ConFiguration)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **829 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### MSCF

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### MSCF?

```
MSCF? {"modulation_set_name"|ALL}, {"property"|ALL}
```

returns:

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### Parameters

|

modulation_set_name

 |

Specifies the name of a modulation set that must have been defined with MSDF.

 |
 |

property

 |

Specifies a property of the modulation set. For a list see the table below.

 |
 |

ALL

 |

This value can be specified in the query to retrieve the configuration data of all modulation sets.

 |
 |

property_value

 |

Specifies the value for the specified property. The values that are admitted for the individual properties are listed in the table below.

 |

### Example

```
> MSCF? "mod1",ALL
< MSCF "mod1",SHAPE,SINE
< MSCF "mod1",PERIOD,250
< MSCF "mod1",PHASE,180
< MSCF "mod1",AMPLITUDE,305
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if no modulation set with the specified name exists.

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
