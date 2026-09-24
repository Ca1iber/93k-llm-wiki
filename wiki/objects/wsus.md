---
type: object
title: WSUS, WSUS? - (Waveform Sets USed)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# WSUS, WSUS? - (Waveform Sets USed)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **676 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### WSUS

```
WSUS {waveform_set}
```

### WSUS?

```
WSUS?
```

returns:

```
WSUS {waveform_set}
```

### Parameters

|

waveform_set

 |

Waveform set number. This is the highest number currently allocated to a waveform set or the highest number of a set you want to load. The number you enter must not exceed the maximum number of waveform sets allowed (defined by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command).

This number is automatically updated to include any new waveform set as it is created. At power-on, only one waveform set (containing one timing set and default values) is available.

 |

### Example

```
WSUS 3
```

This example sets the number of used waveform sets to 3.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the DSCP command.
- waveform_set is smaller than one.

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
