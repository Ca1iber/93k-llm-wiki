---
type: object
title: DPS power flags - get...() functions
layer: L3
stage: run
tags: [dps, power-flags, dps-aux-task, status-flags, protection, test-method-reference]
related: [dps-aux-pin-task, dps-aux-task, dpspins-resources, xps256-status-flags, dps128-dps64-cards, xps256-pmu-operating-mode, xps256-programming-dps-operating-mode, connect, disconnect, smartest-7.4.0]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06_DPS_power_flags_-_get...___functions.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# DPS power flags - get...() functions

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **27,592 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06_DPS_power_flags_-_get...___functions.md>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.01_DPS_AUX_TASK.getAllStatus.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.02_DPS_AUX_TASK.getStatusWithoutConstCur.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.03_DPS_AUX_TASK.getStatusWithoutConstVol.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.04_DPS_AUX_TASK.getClampDistanceTooLow.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.05_DPS_AUX_TASK.getConstantCurrent.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.06_DPS_AUX_TASK.getConstantCurrentLimitDisconnect.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.07_DPS_AUX_TASK.getConstantVoltage.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.08_DPS_AUX_TASK.getCurrentLimiterProtectionDetected.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.09_DPS_AUX_TASK.getDutBoardDisconnect.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.10_DPS_AUX_TASK.getLowHeadroom.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.11_DPS_AUX_TASK.getOvercurrent.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.12_DPS_AUX_TASK.getOvertemperature.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.13_DPS_AUX_TASK.getOvervoltage.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.14_DPS_AUX_TASK.getRangeOverflow.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.15_DPS_AUX_TASK.getSafetyLine.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.16_DPS_AUX_TASK.getUnregulated.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.17_DPS_AUX_TASK.getVoltageDropForce.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.18_DPS_AUX_TASK.getVoltageDropForceWarn.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.19_DPS_AUX_TASK.getVoltageDropReturn.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.20_DPS_AUX_TASK.getVoltageDropReturnWarn.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 DPS AUX TASK.getAllStatus）

```
TM::DPS_POWER_FLAG_STATUS getAllStatus(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getAllStatus）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

 | Keyword  | Value  | State of the checked flags |
 | TM::POWER_FLAG_STATUS_PASS  | 0  | None of the checked flags is set. |
 | TM::POWER_FLAG_STATUS_FAIL  | 1  | Minimum one of the checked flags is set.  |  Note In offline mode, the "Constant voltage" accumulated power supply status flag is always set and this member function returns therefore TM::POWER_FLAG_STATUS_FAIL.

### Example（取自子主题 DPS AUX TASK.getAllStatus）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of all flags. The returned value is TM::POWER_FLAG_STATUS_FAIL if minimum one of the checked flags is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getAllStatus("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getAllStatus(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getAllStatus(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getStatusWithoutConstCur）

```
TM::DPS_POWER_FLAG_STATUS getStatusWithoutConstCur(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getStatusWithoutConstCur）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

 | Keyword  | Value  | State of the checked flags |
 | TM::POWER_FLAG_STATUS_PASS  | 0  | None of the checked flags is set. |
 | TM::POWER_FLAG_STATUS_FAIL  | 1  | Minimum one of the checked flags is set.  |  Note In offline mode, the "Constant voltage" accumulated power supply status flag is always set and this member function returns therefore TM::POWER_FLAG_STATUS_FAIL.

### Example（取自子主题 DPS AUX TASK.getStatusWithoutConstCur）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the read flags except the "Constant current" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if minimum one of the checked flags is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getStatusWithoutConstCur("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getStatusWithoutConstCur(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getStatusWithoutConstCur(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getStatusWithoutConstVol）

```
TM::DPS_POWER_FLAG_STATUS getStatusWithoutConstVol(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getStatusWithoutConstVol）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | None of the checked flags is set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | Minimum one of the checked flags is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getStatusWithoutConstVol）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the read flags except the "Constant voltage" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if minimum one of the checked flags is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getStatusWithoutConstVol("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getStatusWithoutConstVol(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getStatusWithoutConstVol(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getClampDistanceTooLow）

```
TM::DPS_POWER_FLAG_STATUS getClampDistanceTooLow(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getClampDistanceTooLow）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getClampDistanceTooLow）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Clamp distance too low" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getClampDistanceTooLow("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getClampDistanceTooLow(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getClampDistanceTooLow(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getConstantCurrent）

```
TM::DPS_POWER_FLAG_STATUS getConstantCurrent(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getConstantCurrent）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getConstantCurrent）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Constant current" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getConstantCurrent("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getConstantCurrent(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getConstantCurrent(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getConstantCurrentLimitDisconnect）

```
TM::DPS_POWER_FLAG_STATUS getConstantCurrentLimitDisconnect(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getConstantCurrentLimitDisconnect）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getConstantCurrentLimitDisconnect）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the Current limit disconnect" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getConstantCurrentLimitDisconnect("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getConstantCurrentLimitDisconnect(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getConstantCurrentLimitDisconnect(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getConstantVoltage）

```
TM::DPS_POWER_FLAG_STATUS getConstantVoltage(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getConstantVoltage）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

 | Keyword  | Value  | State of the checked flags |
 | TM::POWER_FLAG_STATUS_PASS  | 0  | The checked flag is not set. |
 | TM::POWER_FLAG_STATUS_FAIL  | 1  | The checked flag is set.  |  Note In offline mode, the "Constant voltage" accumulated power supply status flag is always set and this member function returns therefore TM::POWER_FLAG_STATUS_FAIL.

### Example（取自子主题 DPS AUX TASK.getConstantVoltage）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Constant voltage" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getConstantVoltage("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getConstantVoltage(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getConstantVoltage(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getCurrentLimiterProtectionDetected）

```
TM::DPS_POWER_FLAG_STATUS getCurrentLimiterProtectionDetected(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getCurrentLimiterProtectionDetected）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getCurrentLimiterProtectionDetected）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Current limiter protection detected" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getCurrentLimiterProtectionDetected("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getCurrentLimiterProtectionDetected(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getCurrentLimiterProtectionDetected(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getDutBoardDisconnect）

```
TM::DPS_POWER_FLAG_STATUS getDutBoardDisconnect(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getDutBoardDisconnect）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flag |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getDutBoardDisconnect）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "DUT board disconnect" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getDutBoardDisconnect("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getDutBoardDisconnect(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getDutBoardDisconnect(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getLowHeadroom）

```
TM::DPS_POWER_FLAG_STATUS getLowHeadroom(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getLowHeadroom）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getLowHeadroom）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Low headroom" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getLowHeadroom("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getLowHeadroom(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getLowHeadroom(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getOvercurrent）

```
TM::DPS_POWER_FLAG_STATUS getOvercurrent(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getOvercurrent）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getOvercurrent）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Overpower / Overcurrent / Power budget exceeded" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getOvercurrent("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getOvercurrent(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getOvercurrent(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getOvertemperature）

```
TM::DPS_POWER_FLAG_STATUS getOvertemperature(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getOvertemperature）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getOvertemperature）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Overtemperature" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getOvertemperature("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getOvertemperature(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getOvertemperature(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getOvervoltage）

```
TM::DPS_POWER_FLAG_STATUS getOvervoltage(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getOvervoltage）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getOvervoltage）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Overvoltage" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the 1st pin
//
if (dpsAuxTask_1.getOvervoltage("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getOvervoltage(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getOvervoltage(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getRangeOverflow）

```
TM::DPS_POWER_FLAG_STATUS getRangeOverflow(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getRangeOverflow）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getRangeOverflow）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Range overflow" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getRangeOverflow("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getRangeOverflow(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getRangeOverflow(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getSafetyLine）

```
TM::DPS_POWER_FLAG_STATUS getSafetyLine(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getSafetyLine）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getSafetyLine）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Safety line" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getSafetyLine("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getSafetyLine(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getSafetyLine(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getUnregulated）

```
TM::DPS_POWER_FLAG_STATUS getUnregulated(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getUnregulated）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getUnregulated）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Unregulated" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getUnregulated("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getUnregulated(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getUnregulated(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getVoltageDropForce）

```
TM::DPS_POWER_FLAG_STATUS getVoltageDropForce(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getVoltageDropForce）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getVoltageDropForce）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Voltage drop force" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getVoltageDropForce("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getVoltageDropForce(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getVoltageDropForce(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getVoltageDropForceWarn）

```
TM::DPS_POWER_FLAG_STATUS getVoltageDropForceWarn(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getVoltageDropForceWarn）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

### Syntax（取自子主题 DPS AUX TASK.getVoltageDropReturn）

```
TM::DPS_POWER_FLAG_STATUS getVoltageDropReturn(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getVoltageDropReturn）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.

### Example（取自子主题 DPS AUX TASK.getVoltageDropReturn）

The following example reads the actual state of all power flags, clears all flags and evaluates the state of the "Voltage drop return" flag. The returned value is TM::POWER_FLAG_STATUS_FAIL if the checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Read actual power flag status of two pins
    //
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
    dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getVoltageDropReturn("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getVoltageDropReturn(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getVoltageDropReturn(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS AUX TASK.getVoltageDropReturnWarn）

```
TM::DPS_POWER_FLAG_STATUS getVoltageDropReturnWarn(const STRING& pin);
```

Parameter
| Parameter | Description/Range |
|---|---|
| pin | Single pin for which the status flags should be retrieved. |

### Return value（取自子主题 DPS AUX TASK.getVoltageDropReturnWarn）

The member function returns one of the following values of the enumerated type DPS_POWER_FLAG_STATUS:

| Keyword | Value | State of the checked flags |
|---|---|---|
| TM::POWER_FLAG_STATUS_PASS | 0 | The checked flag is not set. |
| TM::POWER_FLAG_STATUS_FAIL | 1 | The checked flag is set. |

<!-- 语法节 end -->

## 是什么

**这 20 个成员函数是同一件事的 20 个入口：读 DPS 通道的累积电源状态标志
（accumulated power supply status flags）。** 它们全挂在 `DPS_AUX_TASK` 类上。
适用面由开头第一句定死：

> 「The DPS_AUX_TASK class features several member functions for reading the accumulated power
> supply status flags of the Device Power Supplies (DPS) in DPS operating mode, in PMU operating
> mode or in Digital I/O operating mode.」

**三种工作模式都算数**：DPS 模式、PMU 模式、Digital I/O 模式。

### 关键机制一：读的是「一段窗口内的累积」，不是「此刻的瞬时值」

窗口的两个边界，原文紧接着的第二句就写死了：

> 「The returned result will show the status flags that have been set on tests performed since
> the previous call of the DPS_AUX_PIN_TASK.checkPowerFlags() member function, or since the last
> connect or disconnect sequence was executed.」

| 窗口起点（**取更近的那个**） |
|---|
| 上一次 `checkPowerFlags()` 调用 |
| 上一次 connect / disconnect 序列执行 |

**这句话的实操含义：你读到的一个 FAIL，可能是几百个 test 之前留下的，不等于「现在正在过流」。**
**想要「此刻」的状态，必须自己先把窗口关掉**（见 `## 典型用法`）。

### 关键机制二：`get...()` 从不碰硬件

这是本节最容易搞错的一点。原文：

> 「Several get...() member functions are documented in this section. These member functions
> retrieve the value of all flags or of a single flag from the test method cache. The
> DPS_AUX_PIN_TASK.checkPowerFlags() member function must be called upfront for reading the flags
> from the hardware into the test method cache.」

**所以这是两级结构，顺序是硬性的：**

| 步骤 | 谁做 | 做什么 |
|---|---|---|
| 1 | `checkPowerFlags()` | **硬件 → test method cache**（**唯一读硬件的一步**） |
| 2 | `get...()` | **cache → 返回值**（**不碰硬件**） |

**不先调 `checkPowerFlags()`，这 20 个函数读到的就是上一次留下的旧 cache**——
**它们不会报错，只会给你过期数据。**

### 20 个函数 = 17 个单标志 + 3 个聚合读法

原文的子主题列了 **20 个**函数，标志表列了 **17 个 flag**（bit 0–16）。
多出来的 3 个是聚合式读法：

| 函数 | 读什么 |
|---|---|
| `getAllStatus(pin)` | **全部 flag** |
| `getStatusWithoutConstCur(pin)` | 全部 flag，**排除 `Constant current`** |
| `getStatusWithoutConstVol(pin)` | 全部 flag，**排除 `Constant voltage`** |

（推断：20 − 17 = 3，且这 3 个的名字都不指单个 flag，其余 17 个一对一——
**依据是子主题名单与标志表的条目数差**。）

**其余 17 个一对一，但函数名并不逐字等于 flag 名**，五处对不上：

| 函数名 | 它读的那个 flag（按标志表） |
|---|---|
| `getOvercurrent` | `Overpower / Overcurrent / Power budget exceeded` —— **一个函数名压了三个条件** |
| `getConstantCurrentLimitDisconnect` | `Current limit disconnect` |
| `getCurrentLimiterProtectionDetected` | `Current limiter protection detected` |
| `getVoltageDropForceWarn` | `Voltage drop force warning` |
| `getVoltageDropReturnWarn` | `Voltage drop return warning` |

另外 12 个（`getClampDistanceTooLow` / `getConstantCurrent` / `getConstantVoltage` /
`getDutBoardDisconnect` / `getLowHeadroom` / `getOvertemperature` / `getOvervoltage` /
`getRangeOverflow` / `getSafetyLine` / `getUnregulated` / `getVoltageDropForce` /
`getVoltageDropReturn`）名字与 flag 名只差大小写和空格。

### 签名只有一个参数，返回值只有两态

**20 个函数的签名形状完全一样**：`const STRING& pin` 进，`TM::DPS_POWER_FLAG_STATUS` 出。
**`pin` 是单个 pin**（原文：`Single pin for which the status flags should be retrieved.`）——
**同一行里要查两个 pin，就得调两次。**

> ⚠️ **注意和 `checkPowerFlags()` 的不对称**：例子里的 `checkPowerFlags()` 写的是
> `dpsAuxTask_1.pin("dps1,dps2")` —— **一次给两个 pin**；而 `get...()` 只吃一个。
> **批量读硬件、逐个取结果**。

返回值的定义在定义文档正文里，比子主题里的表述更全：

| Keyword | Value | State of the checked flags |
|---|---|---|
| `TM::POWER_FLAG_STATUS_PASS` | 0 | The checked single flag is not set or none of multiple checked flags is set. |
| `TM::POWER_FLAG_STATUS_FAIL` | 1 | The checked single flag is set or minimum one of multiple checked flags is set. |

**即：只有「有没有」两态，没有「有几个」。** 想知道**哪几个**成立，只能逐个调单标志函数。

### 17 个 flag 各是什么

原文的标志表（`## DPS flag description`）逐条：

| Flag | Description |
|---|---|
| `Constant voltage` | 恒压工作模式。通道正在 force 或 clamp 电压。**离线下这一位会被置 1。** |
| `Constant current` | 恒流工作模式。通道正在 force 或 clamp 电流。 |
| `Unregulated` | The channel is in an unregulated state. |
| `Overvoltage` | 检出过压。 |
| `Overpower / Overcurrent / Power budget exceeded` | 检出过功率 / 过流，或超出功率预算。 |
| `Overtemperature` | 通道硬件温度过高。 |
| `Voltage drop force` | DUT 板 high force 线上用户定义的压降过大。 |
| `Voltage drop return` | DUT 板 low force / return 线上用户定义的压降过大。 |
| `DUT board disconnect` | DUT 板已断开。 |
| `Safety line` | The interlock of the safety line is open. |
| `Current limit disconnect` | 恒流模式的用户定义时限到了。 |
| `Low headroom` | The energy supply provides not enough headroom for the proper function of the output buffer. |
| `Current limiter protection detected` | 限流保护模式被触发。 |
| `Range overflow` | force 或 clamp 量程溢出；comparator 量程溢出也算（前提是该测量量程由 force/clamp 量程决定）。 |
| `Clamp distance too low` | 上下 clamp 电压之间的距离、或 source/sink clamp 电流之间的距离，program 得太近。 |
| `Voltage drop force warning` | force 线（P#）上量到的压降超过 program 的警告阈值。 |
| `Voltage drop return warning` | 公共 return 线（GND）对地感线（GS#）量到的压降超过 program 的警告阈值。 |

**四个 flag 的阈值不在这篇文档里**，原文把它们指到 [[dpspins-resources]]：
`Voltage drop force` / `Voltage drop return` 指 `max_voltage_drop_force` /
`max_voltage_drop_return`（**只对 UHC4T 的 DPS 模式**），
`Current limit disconnect` 指 `ms_const_curr_disconnect`。

### 哪张卡支持哪个位：三张卡差得很远

原文的 `## DPS flag implementation` 表把 17 个 flag 摊到 bit 0–16 上，
再标三张卡支持不支持（`+` / `-`）：

| 支持几个位 | 卡 | 具体是哪些位 |
|---|---|---|
| **3** | **DPS128 / DPS64** | 0 `Constant voltage`、1 `Constant current`、5 `Overtemperature` |
| **12** | **UHC4T** | 0–10 全部，**加上 12** `Current limiter protection detected` |
| **15** | **XPS256** | 0–10 全部，**加上 13** `Range overflow`、**14** `Clamp distance too low`、**15 / 16** 两条 warning |

**三处要点：**

1. **`Low headroom`（bit 11）在三张卡上全是 `-`** —— **一张支持的都没有。**
2. **`DPS128 / DPS64` 只有 3 个位** —— 它是最小的那一档。
3. **`Safety line`（bit 9）UHC4T 那格写的是 `+`**，
   **而文件末尾的脚注说这一位「will never be set」** —— **格子和脚注互相打脸**（见 `## 出处`）。

### reset 规则：两个边界都清零，但「条件不成立」才真清

> 「All DPS status flags are reset to 0 at connect (PSST ON) and disconnect (PSST OFF).」

**清零不是无条件的**：

> 「Note that a reset to 0 is only effective if the condition for the flag is no longer true.
> The flag is not reset, if the condition is still true at the time of the connect/disconnect or
> a query by DPS_AUX_PIN_TASK.checkPowerFlags().」

**「清不掉」本身就是信号：条件还在。** 清了它，下一次读还是 1。

**`Constant voltage` 是个例外，原文说它「不是独立的」**：

> 「But when calling the DPS_AUX_PIN_TASK.checkPowerFlags(), the flag "Constant Voltage" is not
> independent. It is 1 when all other flags are 0.」

**也就是说 `Constant voltage` 实际是「其它 16 个全 0」的指示位。**

### 离线模式的坑：4 个函数恒返回同一个值

各子主题的 `Return value` 段对离线模式的说法**不统一**，摊开是这样：

| 离线下的返回值 | 函数 |
|---|---|
| **恒 `FAIL`** | `getAllStatus`、`getStatusWithoutConstCur`、`getConstantVoltage` |
| **恒 `PASS`** | `getStatusWithoutConstVol` |
| 写着 `Return value in offline mode is TM::POWER_FLAG_STATUS_PASS.` | 13 个单标志函数 |
| **一个字都没写** | `getVoltageDropForceWarn`、`getVoltageDropReturnWarn` |

前三个恒 `FAIL` 的原因原文写明了两处：标志表里 `Constant voltage` 那条写着
`Note: In offline mode of SmarTest, this flag will be set to 1.`；
`getAllStatus` / `getStatusWithoutConstCur` / `getConstantVoltage` 的返回值表里写着
`Note In offline mode, the "Constant voltage" accumulated power supply status flag is always
set and this member function returns therefore TM::POWER_FLAG_STATUS_FAIL.`

**（推断）为什么偏偏 `getStatusWithoutConstVol` 是 `PASS`**：
它是**唯一一个把那个恒 1 的位排除掉的读法**——**依据是上一条「`Constant voltage` 是 1
当且仅当其它 flag 全 0」加上「离线下它恒为 1」两条原文**。
**所以：在离线环境（无硬件）跑同一段程序，`getAllStatus()` 必然报 `FAIL`，
要一段离线也能过的代码就得用 `getStatusWithoutConstVol()`。**

## 典型用法

**1. 顺序**（原文 `## Member functions` 一节唯一给的操作要求）：

**调 `checkPowerFlags()`**（硬件 → cache）→ **调某个 `get...()`**（cache → 返回值）。
**中间不插别的东西，且 `checkPowerFlags()` 不能省。**

**2. 连调两次 `checkPowerFlags()`**：这是 20 个子主题的例子里**共有**的一段，
两行注释逐字是：

```
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
```

**第一遍读 latched（锁存的历史），第二遍读 actual（当前），两遍都清 flag。**

> **文档只给了这两行注释，没有解释为什么必须两次。**
> **（推断）**：结合上文的窗口定义与 reset 规则（「reset to 0 只在条件不再成立时才有效」），
> **第一遍把上一个窗口关掉并读走它累积的位，第二遍读到的才是「第一遍清完之后仍然成立」的那些位**
> ——**也就是此刻仍为真的那一批**。**推断依据只有这两行注释和 reset 规则那两句原文，
> `checkPowerFlags()` 自己的文档本页没读，所以这条推断没有第二来源。**
> **例子里两遍都写了 `clear all flags`，说明两遍都清。**

**3. 例子的骨架**（20 个子主题里 18 个给了 `Example`，骨架一模一样）：

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
    // 两遍 checkPowerFlags()
}
ON_FIRST_INVOCATION_END();

if (dpsAuxTask_1.getAllStatus("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
    cout << "dpsAuxTask_1.getAllStatus(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
    cout << "dpsAuxTask_1.getAllStatus(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

**注意两点**：`checkPowerFlags()` 在 `ON_FIRST_INVOCATION_BEGIN()/END()` 里
（**只在首次调用时跑一次**），`get...()` 在块**外面**；
**`DPS_AUX_TASK` 对象声明在块外**，所以块里的 cache 出去还能读。

**4. 选哪个函数：**

| 你要问的 | 用哪个 |
|---|---|
| **整体好不好**（有一个不对就算不对） | `getAllStatus()` |
| **某一个条件** | 对应的单标志函数（**名字不一定和 flag 名一样，见上表**） |
| **想细看是哪几个** | **只能逐个调单标志函数**——**聚合读法不告诉你「几个」** |
| **同一段代码要在离线环境也能跑通** | `getStatusWithoutConstVol()`（**否则必然 `FAIL`**） |
| **恒流跑太久 / 板上压降太大** | 各自的单标志函数；**阈值在 [[dpspins-resources]] 里** |

**5. 一条读数的前提**：**读到 `FAIL` 不等于「现在坏了」**，它覆盖的是
**上一个窗口内的全部历史**（见 `## 是什么` 的第一条机制）。**要缩短窗口，就多调 `checkPowerFlags()`。**

## 和谁有关

- [[dps-aux-pin-task]] — **前置，且是本页数据链的上游**。
  `checkPowerFlags()` 是这 20 个函数的**唯一数据来源**；**不先调它，本页的函数读的是旧 cache**。
  **本页只讲 `get...()` 这一侧，`checkPowerFlags()` 自己怎么工作、清哪些 flag，本页没读那篇文档。**
- [[dps-aux-task]] — **同类**。这 20 个函数都是 `DPS_AUX_TASK` 的成员函数。
  **（推断）`pin()` 是另一个入口**：例子写成 `dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags()`，
  **说明 `checkPowerFlags()` 长在 `pin()` 返回的对象上，而不直接长在 `DPS_AUX_TASK` 上**
  ——**依据只有例子的写法，本页没读 `DPS_AUX_TASK` 的类文档。**
- [[dpspins-resources]] — **上游，阈值定义处**。原文把三个 flag 的阈值指过去：
  `For UHC4T channels in DPS operating mode, see max_voltage_drop_force in DPSPINS resources.`、
  `See ms_const_curr_disconnect in DPSPINS resources.`
  **本页因此只有 flag 的语义，没有阈值的取值。**
- [[xps256-status-flags]] — **下游，卡专属细节**。原文说各卡 flags 的功能「largely the same」，
  详细的卡专属描述指向它：`For a card-specific detailed description of the flags refer to` →
  `XPS256 status flags`。**本页的实现表只给 `+` / `-`，不给 XPS256 每一位的具体行为。**
- [[dps128-dps64-cards]] — **实现表里的一列**。三列卡之一（**DPS128 / DPS64**），
  **只支持 3 个 flag 位**。**本页没有这两张卡的任何其他信息。**
- [[xps256-pmu-operating-mode]] / [[xps256-programming-dps-operating-mode]] — **模式侧**。
  本页开头那句把「DPS operating mode / PMU operating mode / Digital I/O operating mode」
  三种模式并列，**这两个页讲的是其中两种模式**；**本页一个字都没讲模式本身的细节**。
- [[connect]] / [[disconnect]] — **累积窗口的另一个边界**。
  原文说窗口起点是「上一次 `checkPowerFlags()`」**或**「上一次 connect / disconnect」，
  这是本页「读到的不一定是此刻」那条机制的直接依据。
- [[smartest-7.4.0]] — **版本页**。本页 `## 版本` 那一条的落点。
- [[utility-card]] — **同层硬件对象页**；**本页语料里的三列卡与它的关系，本页没读到**，故只列名。
- `PSAS? - (Power Supply Accumulated Status)`（**未建**）—
  原文 `Related information` 里和 `checkPowerFlags()` **并列**给的一条
  （链接路径在 `02.06_Command_Reference/` 下，**本页只从链接路径知道它在哪儿**）。
  **它和这 20 个函数是什么关系，本页不知道**——那篇没读。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- **Introduced in SmarTest 7.4.0**

**这条只说了这组函数从 7.4.0 起有；7.4.0 → 本 wiki 面向的 7.10.3 之间的变更，一条都没有。**

> ⚠️ **这一节末尾粘着一条脚注定义**（`[1)](<>) Due to the hardware structure of UHC4T …`），
> **它不是版本条目**，是 §11.2 ③ 那个现象的实例：
> 语料生成器把脚注定义挂在文件末尾，而 `## Functional changes` 正好是最后一个 `## ` 段。
> **本页照实引它，见 `## 出处` 的瑕疵 ①②。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06_DPS_power_flags_-_get...___functions.md`

**本页没做的：**

- **20 个子主题文档一篇都没读。** 本页「语法 / 参数」节里那 20 组
  `Syntax` / `Return value` / `Example` 是 `extract/objscaffold.py` 从子主题**逐字抽**的（§4），
  **不是本页读来的**；本页全部散文**只根据上面那一篇定义文档**。
  所以：**每个函数自己那篇的正文（有没有 `## Procedure`、有没有 `## Before you begin`）
  本页一个字都没有。** 上面 `## 典型用法` 里对例子的描述，
  **依据是「语法 / 参数」节里那些逐字代码块，不是子主题原文。**
- **`checkPowerFlags()` 那篇没读** —— 所以
  「它到底清哪些 flag、两遍连调之间 cache 里剩什么、能不能不调、它在哪种模式下合法」
  **本页不知道**。`## 典型用法` 第 2 条那整段**是推断**，已在原处标出。
- **`PSAS? - (Power Supply Accumulated Status)` 没读。**
- **`XPS256 status flags` 那篇没读** —— XPS256 各位的具体行为本页没有，
  实现表里的 `+` / `-` 是本页唯一的 XPS256 信息。
- **`DPSPINS resources` 没读** —— 所以 `max_voltage_drop_force` /
  `max_voltage_drop_return` / `ms_const_curr_disconnect` 三个阈值的
  **取值、单位、默认值、怎么设**，**本页都不知道**，只知道它们在那儿定义。
- **`DPS_AUX_TASK` 的类文档没读** —— `pin()` 的语义本页只有推断。
- **源文档里没有图**（定义文档没有图，**它的 20 篇子主题里也没有**——子主题那一层本页核过）。
  **本页没有任何来自图的结论。**
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。

> ⚠️ **本篇的七处语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **同一个 bit 映射，表内说「UHC4 和 UHC4T」，脚注说「只有 UHC4T」** —— 两处逐字：
> 表内：`This special mapping of the bit applies only to UHC4 and UHC4T.`
> 脚注：`This special mapping of the bit applies only to UHC4T.`
> **两句不可能同时为真。本页并列两处，不替它调和，也不判哪个是笔误。**
>
> ② **实现表 bit 9（`Safety line`）UHC4T 那格写 `+`，而脚注说这一位
> `will never be set`** —— **格子和脚注互相打脸。**
>
> ③ **`DUT board disconnect` 那一行多出第三个格子**：这一格本来只有
> Flag / Description 两列，而那一行的 Description 之后**又粘了一格** bit 映射说明
> （就是 ① 引的那句）。**这是一行坏行。**
>
> ④ **`Related information` 一节里两个链接之间没有任何分隔符**：
> `[DPS_AUX_PIN_TASK.checkPowerFlags()](<…>)[PSAS? - (Power Supply Accumulated Status)](<…>)`
> ——**没有空格、没有换行，两个链接直接粘在一起**，照字面读像一个链接。
>
> ⑤ **`Low headroom`（bit 11）在三张卡上全是 `-`**，
> **但文档为它单列了 `getLowHeadroom()` 函数，还配了完整 `Example`**
> ——**一个三张卡都不支持的 flag，有一个正式的读法。**
> **本页不判这是笔误还是给未来的卡留的位**（原文没说）。
>
> ⑥ **`getVoltageDropForceWarn` / `getVoltageDropReturnWarn` 两个子主题
> 没有 `Example` 段，返回值表里也没有那句「离线下返回 PASS」**
> ——**20 个子主题里只有这两个缺**（其余 18 个都有 Example，
> 其余 18 个的返回值表都多一行离线说明）。**这是「保持沉默」，不是「说了 PASS」**，
> 本页在上面那张离线表里单列了一行「一个字都没写」。
>
> ⑦ **三处小的不一致，都逐字抄在这里**：
> - `getConstantCurrentLimitDisconnect` 的 Example 说明句里**开引号丢了**：
>   `evaluates the state of the Current limit disconnect" flag`（**只有一个右引号**）；
> - `getOvervoltage` 的 Example 注释写 `// Evaluate the state of the 1st pin`，
>   **其余 19 个子主题都写 `first pin`**；
> - `getDutBoardDisconnect` 的返回值表表头写 `State of the checked flag`（**单数**），
>   **其余子主题都写 `flags`（复数）**。
>
> **以上七条都在「语法 / 参数」节内或来自该节，本页按 §4 一个字都没改。**
> **另：本篇没有 §11.2 ① 那种 `鈥` 形态的编码损坏（本页通篇查过，0 处）。**

`verified: doc-only`
