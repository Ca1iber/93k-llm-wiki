---
type: object
title: JRST - (Jitter modulator ReseT)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.146_JRST_-__Jitter_modulator_ReseT.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# JRST - (Jitter modulator ReseT)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **315 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.146_JRST_-__Jitter_modulator_ReseT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
JRST {(pin_list)}
```

### Parameters

|

pin_list

 |

The pins for which the jitter modulator is to be reset. Typically, this must be done for all configured pins, so that you will usually specify @ for the pin list.

 |

### Example

```
JRST (@)
```

This example resets the jitter modulator of all configured pins to its default state OFF.

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
