---
type: object
title: HW_STATE
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117_HW_STATE.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# HW_STATE

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,847 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117_HW_STATE.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Query the status outside the ON_FIRST_INVOVATION block

The status is read from the hardware, stored in the HW_STATE object, and finally retrieved from the HW_STATE object for the site in focus outside of the `ON_FIRST_INVOCATION`（raw: `02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md`） block.

```
HW_STATE    hwState;
DOUBLE      forcedVoltage;
DOUBLE      clampCurrent;

ON_FIRST_INVOCATION_BEGIN();
{
    ...
    ...
}
ON_FIRST_INVOCATION_END();

hwState.getStatus ("PMU_pin_1, DPS_pin_1");

forcedVoltage = hwState.pin ("DPS_pin_1").getVoltageForce();
clampCurrent  = hwState.pin ("DPS_pin_1").getCurrentClampSource();

cout << "Current site: " << CURRENT_SITE_NUMBER() << ", pin \"DPS_pin_1\"" << endl;

cout << "\tForced voltage:       " << forcedVoltage << endl;
cout << "\tCurrent clamp source: " << clampCurrent  << endl;
```

### Example 2: Query the status in a FOR_EACH_SITE...WITH_QUERY block

The status is read from the hardware, stored in the HW_STATE object, and finally retrieved from the HW_STATE object for the site in focus within a FOR_EACH_SITE block in the `ON_FIRST_INVOCATION`（raw: `02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md`） block. The `FOR_EACH_SITE_BEGIN_WITH_QUERY`（raw: `02.07.04.01.71_FOR_EACH_SITE_BEGIN_WITH_QUERY.md`） API must be used to set the query focus within the FOR_EACH_SITE block.

```
HW_STATE    hwState;
DOUBLE      forcedVoltage;
DOUBLE      clampCurrent;

ON_FIRST_INVOCATION_BEGIN();
{
    ...
    ...

    FOR_EACH_SITE_BEGIN_WITH_QUERY();
    {
        hwState.getStatus ("PMU_pin_1, DPS_pin_1");

        forcedVoltage = hwState.pin ("PMU_pin_1").getVoltageForce();
        clampCurrent  = hwState.pin ("PMU_pin_1").getCurrentClampSource();

        cout << "Current site: " << CURRENT_SITE_NUMBER() << ", pin \"PMU_pin_1\"" << endl;

        cout << "\tForced voltage:       " << forcedVoltage << endl;
        cout << "\tCurrent clamp source: " << clampCurrent  << endl;
    }
    FOR_EACH_SITE_END();
}
ON_FIRST_INVOCATION_END();
```

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
