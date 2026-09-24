---
type: object
title: DCDT, DCDT? - (Device Cycle DefaulT)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DCDT, DCDT? - (Device Cycle DefaulT)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **328 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DCDT

```
DCDT {waveform_set}, {"default_name"}
```

### Example

```
DCDT 1,"HOLD"
```

This example defines the default device cycle name HOLD for Waveform Set 1.

```
DCDT? "fast_ARM",(ARMPort)
DCDT "fast_ARM","Cycle",(ARMPort)
```

This example queries the default device cycle name for the ARMPort port in the multi-port specification fast_ARM.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the WSUS command.
- waveform_set is smaller than one.
- You enter an illegal device cycle name (a reserved name, a name containing illegal characters).
- wavetable_name does not reference a defined wavetable.
- specset_id does not reference a defined wavetable.
- specset_id is invalid because equation_set_no, specset_no or both are invalid.
- multi-port_spec does not reference a defined multi-port specification.

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
