---
type: object
title: VPIN, VPIN? - (Virtual PIN)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VPIN, VPIN? - (Virtual PIN)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **696 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### VPIN

```
VPIN (pinlist)
```

### VPIN?

```
VPIN? ([(pinlist) | @]}
```

### Parameters

|

pinlist

 |

The name to be allocated to the pin. The query returns the name of the virtual pins that have been defined. The @ symbol can be used with the VPIN? query to list all pins previously defined by the VPIN command. If you query a non-existent pin name, the system returns nothing.

 |

### Example

- To define a virtual pin:

```
> VPIN (VPIN1)
```

- To define multiple virtual pins:

```
> VPIN (VPIN2,VPIN3)
```

- To list all defined virtual pins:

```
> VPIN? (@)
```

Returns:

```
< VPIN (VPIN1,VPIN2,VPIN3)
```

- To check for the existence of specific virtual pins:

```
> VPIN? (VPIN2,VPIN4,VPIN6)
```

Returns:

```
< VPIN (VPIN2)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error occurs if:

- The specified pin name has already been defined for another pin (virtual or not), port, or group.

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
