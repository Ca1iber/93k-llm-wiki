---
type: object
title: UDEF - (UnDEFine pin)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# UDEF - (UnDEFine pin)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **427 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDEF {(pinlist)}
```

### Parameters

|

pinlist

 |

Consists of single or multiple pin names or the symbol @ which removes all pins. If more than one pin is required, the names must be separated with a comma.

 |

### Example

```
UDEF (Q3)
```

This example causes pin Q3 to be removed from the current configuration. If you subsequently redefine the channel using the same or a different name, it assumes its former operating mode and the pin type OFF.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if you attempt to undefine pins while the sequencer is in the run or the break state. See the command `SQST, SQST? - (SeQuencer STate)`（raw: `02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.md`） for details.

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
