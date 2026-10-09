---
type: object
title: XPS256 status flags
layer: L2
stage: level
tags: [level, xps256, status-flags, protection, dps, pmu, test-head-card]
related: [level, xps256-pmu-operating-mode, xps256-programming-dps-operating-mode, dps-task, pin]
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.02_XPS256_status_flags.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# XPS256 status flags

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **22,398 字符逐字取自** `<02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.02_XPS256_status_flags.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Flag | Flag | Description | Description |
|---|---|---|---|
| Clamp distance too low | Clamp distance too low | Trigger: | The programmed distance between the upper and lower clamp voltage or between the sourcing and sinking clamp current is too low.<br><br>The flag is set if the clamp distance is continuously too small for a period of more than 400 μs. |
| Clamp distance too low | Clamp distance too low | Action: | The applied clamp values are adapted to the minimum clamp distance that is defined be the programmed hardware.<br><br>A warning is shown in the UI report window.<br><br>Note: In most cases, the flag will be set only if the violation of the minimum clamp distance is caused by DC events in a pattern. |
| Clamp distance too low | Clamp distance too low | Availability: | The flag is available per channel. |
| Clamp distance too low | Clamp distance too low | API: | `DPS_AUX_TASK.getClampDistanceTooLow()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.04_DPS_AUX_TASK.getClampDistanceTooLow.md`） |
| High voltage or current of surge tracker exceeded | High voltage or current of surge tracker exceeded | Trigger: | The `XPS256 surge tracker`（raw: `02.05.05.03.03.07_XPS256_surge_tracker.md`） has detected a voltage or current above the user defined upper limit.<br><br>Since the XPS256 surge tracker can simultaneously monitor the voltage and the current, this flag is always set in combination with one or both of the flags `High voltage of surge tracker reached`（raw: `02.05.05.03.10.02_XPS256_status_flags.md#_354167__r_HV_surge_tracker`） or `High current of surge tracker reached`（raw: `02.05.05.03.10.02_XPS256_status_flags.md#_354167__r_HC_surge_tracker`）. |
| High voltage or current of surge tracker exceeded | High voltage or current of surge tracker exceeded | Action: | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
| High voltage or current of surge tracker exceeded | High voltage or current of surge tracker exceeded | Availability: | The flag is available per channel. |
| High voltage or current of surge tracker exceeded | High voltage or current of surge tracker exceeded | API: | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
| High voltage of surge tracker reached | High voltage of surge tracker reached | Trigger: | The `XPS256 surge tracker`（raw: `02.05.05.03.03.07_XPS256_surge_tracker.md`） has detected a voltage above the user defined upper limit.<br><br>This flag is always set in combination with flag `High voltage or current of surge tracker exceeded`（raw: `02.05.05.03.10.02_XPS256_status_flags.md#_354167__r_High_surge_tracker`）. |
| High voltage of surge tracker reached | High voltage of surge tracker reached | Action: | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
| High voltage of surge tracker reached | High voltage of surge tracker reached | Availability: | The flag is available per channel. |
| High voltage of surge tracker reached | High voltage of surge tracker reached | API: | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
| High current of surge tracker reached | High current of surge tracker reached | Trigger: | The `XPS256 surge tracker`（raw: `02.05.05.03.03.07_XPS256_surge_tracker.md`） has detected a current above the user defined upper limit.<br><br>This flag is always set in combination with flag `High voltage or current of surge tracker exceeded`（raw: `02.05.05.03.10.02_XPS256_status_flags.md#_354167__r_High_surge_tracker`）. |
| High current of surge tracker reached | High current of surge tracker reached | Action: | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
| High current of surge tracker reached | High current of surge tracker reached | Availability: | The flag is available per channel. |
| High current of surge tracker reached | High current of surge tracker reached | API: | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
| Low voltage or current of surge tracker exceeded | Low voltage or current of surge tracker exceeded | Trigger: | The `XPS256 surge tracker`（raw: `02.05.05.03.03.07_XPS256_surge_tracker.md`） has detected a voltage or current below the user defined lower limit.<br><br>Since the XPS256 surge tracker can simultaneously monitor the voltage and the current, this flag is always set in combination with one of both of the flags `Low voltage of surge tracker reached`（raw: `02.05.05.03.10.02_XPS256_status_flags.md#_354167__r_LV_surge_tracker`） or `Low current of surge tracker reached`（raw: `02.05.05.03.10.02_XPS256_status_flags.md#_354167__r_LC_surge_tracker`）. |
| Low voltage or current of surge tracker exceeded | Low voltage or current of surge tracker exceeded | Action: | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
| Low voltage or current of surge tracker exceeded | Low voltage or current of surge tracker exceeded | Availability: | The flag is available per channel. |
| Low voltage or current of surge tracker exceeded | Low voltage or current of surge tracker exceeded | API: | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
| Low voltage of surge tracker reached | Low voltage of surge tracker reached | Trigger: | The `XPS256 surge tracker`（raw: `02.05.05.03.03.07_XPS256_surge_tracker.md`） has detected a voltage below the user defined lower limit.<br><br>This flag is always set in combination with flag `Low voltage or current of surge tracker exceeded`（raw: `02.05.05.03.10.02_XPS256_status_flags.md#_354167__r_Low_surge_tracker`）. |
| Low voltage of surge tracker reached | Low voltage of surge tracker reached | Action: | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
| Low voltage of surge tracker reached | Low voltage of surge tracker reached | Availability: | The flag is available per channel. |
| Low voltage of surge tracker reached | Low voltage of surge tracker reached | API: | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
| Low current of surge tracker reached | Low current of surge tracker reached | Trigger: | The `XPS256 surge tracker`（raw: `02.05.05.03.03.07_XPS256_surge_tracker.md`） has detected a current below the user defined lower limit.<br><br>This flag is always set in combination with flag `Low voltage or current of surge tracker exceeded`（raw: `02.05.05.03.10.02_XPS256_status_flags.md#_354167__r_Low_surge_tracker`）. |
| Low current of surge tracker reached | Low current of surge tracker reached | Action: | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
| Low current of surge tracker reached | Low current of surge tracker reached | Availability: | The flag is available per channel. |
| Low current of surge tracker reached | Low current of surge tracker reached | API: | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
| Measurement range change failed | Measurement range change failed | Trigger: | Automatic down‑ranging in DC measurement cannot set the target current measurement range. |
| Measurement range change failed | Measurement range change failed | Action: | A warning is shown in the UI report window. |
| Measurement range change failed | Measurement range change failed | Availability: | The flag is available per channel. |
| Measurement range change failed | Measurement range change failed | API: | `DPS_AUX_TASK.getRangeError()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.07.02_DPS_AUX_TASK.getRangeError.md`） |
| Range overflow | Range overflow | Trigger: | An overflow of the force range or the clamp range has been detected.<br><br>The flag is also set for comparator range overflows if the related measurement range is determined by the force or clamp range. |
| Range overflow | Range overflow | Action: | The applied value is limited to the maximum range specific value.<br><br>A warning is shown in the UI report window. |
| Range overflow | Range overflow | Availability: | The flag is available per channel. |
| Range overflow | Range overflow | APIs: | `DPS_AUX_TASK.getRangeOverflow()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.14_DPS_AUX_TASK.getRangeOverflow.md`） |
| Voltage drop force warning | Voltage drop force warning | Trigger: | The measured voltage drop on the force line (P#) exceeds the programmed warning threshold.<br><br>Default threshold for the force line is 150 mV.<br><br>For the DPS operating mode, see `warn_voltage_drop_force`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__warn_voltage_drop_force`） in `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）.<br><br>For the PMU operating mode, see `SPMU_PIN_TASK.forceDropWarn()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.234.01.10_SPMU_PIN_TASK.forceDropWarn.md`）. |
| Voltage drop force warning | Voltage drop force warning | Action: | The flag is for information only.<br><br>You should query the flags at least at the end of the testflow. |
| Voltage drop force warning | Voltage drop force warning | Availability: | The flag is available per channel. |
| Voltage drop force warning | Voltage drop force warning | APIs: | `DPS_AUX_TASK.getVoltageDropForceWarn()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.18_DPS_AUX_TASK.getVoltageDropForceWarn.md`） |
| Voltage drop return warning | Voltage drop return warning | Trigger: | The measured voltage drop on the common return line (GND) referenced to the ground sense line (GS#) exceeds the programmed warning threshold.<br><br>Default threshold for the return line is 50 mV.<br><br>For the DPS operating mode, see `warn_voltage_drop_return`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__warn_voltage_drop_return`） in `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）.<br><br>For the PMU operating mode, see `SPMU_PIN_TASK.returnDropWarn()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.234.01.30_SPMU_PIN_TASK.returnDropWarn.md`） |
| Voltage drop return warning | Voltage drop return warning | Action: | The flag is for information only.<br><br>You should query the flags at least at the end of the testflow. |
| Voltage drop return warning | Voltage drop return warning | Availability: | The flag is available per channel. |
| Voltage drop return warning | Voltage drop return warning | APIs: | `DPS_AUX_TASK.getVoltageDropReturnWarn()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.20_DPS_AUX_TASK.getVoltageDropReturnWarn.md`） |

### Tables（脚本逐字抽取，第 2 张）

| Flag | Description | Description |
|---|---|---|
| Constant current | Trigger: | The channel is in constant current operating mode and forces or clamps the current. |
| Constant current | Action: | The flag is for information only. |
| Constant current | Availability: | The flag is available per channel. |
| Constant current | APIs: | `DPS_AUX_TASK.getConstantCurrent()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.05_DPS_AUX_TASK.getConstantCurrent.md`）<br><br>`DPS_AUX_TASK.getStatusWithoutConstVol()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.03_DPS_AUX_TASK.getStatusWithoutConstVol.md`）<br><br>`DPS_AUX_TASK.getAllStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.01_DPS_AUX_TASK.getAllStatus.md`） |
| Constant voltage | Trigger: | The channel is in constant voltage operating mode and forces or clamps the voltage. |
| Constant voltage | Action: | The flag is for information only. |
| Constant voltage | Availability: | The flag is available per channel. |
| Constant voltage | APIs: | `DPS_AUX_TASK.getConstantVoltage()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.07_DPS_AUX_TASK.getConstantVoltage.md`）<br><br>`DPS_AUX_TASK.getStatusWithoutConstCur()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.02_DPS_AUX_TASK.getStatusWithoutConstCur.md`）<br><br>`DPS_AUX_TASK.getAllStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.01_DPS_AUX_TASK.getAllStatus.md`） |

### Tables（脚本逐字抽取，第 3 张）

| Flag | Description | Description |
|---|---|---|
| Current limit disconnect | Trigger: | The user defined time for constant current mode was reached.<br><br>For the DPS operating mode, `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`） parameter `ms_const_curr_time_to_alarm`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__ms_const_curr_time_to_alarm`） defines the delay time for a pin that is in constant current mode without interruption before this flag is triggered. Parameter `ms_const_curr_disconnect`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__ms_const_curr_disconnect`） defines the delay time until the channel is disconnected. The parameter ms_const_curr_disconnect must be defined in the level setup to enable the disconnection in case the current limit is exceeded. Parameter `disable_const_curr_check`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__disable_const_curr_check`） can be used to disable this status flag.<br><br>For the PMU operating mode, see `SPMU_PIN_TASK.currentClampTimeToAlarm()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.234.01.05_SPMU_PIN_TASK.currentClampTimeToAlarm.md`） and `SPMU_PIN_TASK.currentClampTimeToDisconnect()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.234.01.06_SPMU_PIN_TASK.currentClampTimeToDisconnect.md`）. |
| Current limit disconnect | Action: | The related channel or the entire ganging group is disconnected. |
| Current limit disconnect | Availability: | The flag is available per channel. |
| Current limit disconnect | API: | `DPS_AUX_TASK.getConstantCurrentLimitDisconnect()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.06_DPS_AUX_TASK.getConstantCurrentLimitDisconnect.md`） |
| DUT board disconnect | Trigger: | The channel has received `DUT board disconnect shutdown`（raw: `02.05.05.03.03.06_XPS256_safety_line_and_DUT_board_disconnect.md#_354940__s_DUT_board_disconnect_shutdown`） signal from an appropriately configured trigger source. |
| DUT board disconnect | Action: | All XPS256 channels are disconnected. |
| DUT board disconnect | Availability: | The flag is available per channel. |
| DUT board disconnect | API: | `DPS_AUX_TASK.getDutBoardDisconnect()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.09_DPS_AUX_TASK.getDutBoardDisconnect.md`） |
| DUT board disconnect | Note: | See also `XPS256 programming - Safety line and DUT board disconnect`（raw: `02.05.05.03.10.18_XPS256_programming_-_Safety_line_and_DUT_board_disconnect.md`）. |
| Overpower / Overcurrent / Power budget exceeded | Trigger: | An overpower or overcurrent condition has been detected.<br><br>The flag is triggered when the overcurrent condition has been detected for longer than 50 ms without interruption. |
| Overpower / Overcurrent / Power budget exceeded | Action: | The related channel is disconnected. |
| Overpower / Overcurrent / Power budget exceeded | Availability: | The flag is available per channel. |
| Overpower / Overcurrent / Power budget exceeded | API: | `DPS_AUX_TASK.getOvercurrent()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.11_DPS_AUX_TASK.getOvercurrent.md`） |
| Overtemperature | Trigger: | The temperature of the channel hardware is too high. |
| Overtemperature | Action: | The related channel is disconnected. |
| Overtemperature | Availability: | The flag is available per channel. |
| Overtemperature | API: | `DPS_AUX_TASK.getOvertemperature()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.12_DPS_AUX_TASK.getOvertemperature.md`） |
| Overvoltage | Trigger: | The applied voltage exceeds the maximum voltage of the active voltage range. |
| Overvoltage | Action: | The channel is disconnected. |
| Overvoltage | Availability: | The flag is available per channel. |
| Overvoltage | API: | `DPS_AUX_TASK.getOvervoltage()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.13_DPS_AUX_TASK.getOvervoltage.md`） |
| Safety line | Trigger: | The channel has received `Safety line shutdown`（raw: `02.05.05.03.03.06_XPS256_safety_line_and_DUT_board_disconnect.md#_354940__s_Safety_line_shutdown`） signal from an appropriately configured and assigned trigger source. |
| Safety line | Action: | Only XPS256 channels assigned to the trigger source are disconnected. |
| Safety line | Availability: | The flag is available per channel. |
| Safety line | API: | `DPS_AUX_TASK.getSafetyLine()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.15_DPS_AUX_TASK.getSafetyLine.md`） |
| Safety line | Note: | See also `XPS256 programming - Safety line and DUT board disconnect`（raw: `02.05.05.03.10.18_XPS256_programming_-_Safety_line_and_DUT_board_disconnect.md`）. |
| Unregulated | Trigger: | The XPS256 channel is in an unregulated state.<br><br>The flag is triggered when the output stage is at its limits for longer than 10 ms without interruption. |
| Unregulated | Action: | The channel is disconnected. |
| Unregulated | Availability: | The flag is available per channel. |
| Unregulated | API: | `DPS_AUX_TASK.getUnregulated()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.16_DPS_AUX_TASK.getUnregulated.md`） |
| Voltage drop force | Trigger: | The voltage drop on the force (P#) line on the DUT board exceeds the user defined limit.<br><br>Default threshold for the force line is 150 mV.<br><br>The flag is set if the threshold is exceeded without interruption for the time defined by the `Vdrop Hold time`（raw: `02.05.05.03.10.05_XPS256_programming_-_Default_values.md#_354611__r_Vdrop_hold_time`） parameter for the corresponding pin. Note that the Vdrop Hold time parameter can be set only in the `DC Scale Safety editor`（raw: `02.05.05.03.10.05_XPS256_programming_-_Default_values.md`）. The time can be set separately for the force line and for the return line.<br><br>For XPS256 channels in DPS operating mode, see `max_voltage_drop_force`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__max_voltage_drop_force`） in `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）.<br><br>For XPS256 channels in PMU operating mode, see `SPMU_PIN_TASK.forceDropMax()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.234.01.09_SPMU_PIN_TASK.forceDropMax.md`）. |
| Voltage drop force | Action: | By default, the channel remains connected.<br><br>The channel is disconnected if the `Vdrop Disco`（raw: `02.05.05.03.10.05_XPS256_programming_-_Default_values.md#_354611__r_Vdrop_Disco`） parameter is set to ON for the corresponding pin. Note that the Vdrop Disco parameter can be set only in the `DC Scale Safety editor`（raw: `02.05.05.03.10.05_XPS256_programming_-_Default_values.md`）. |
| Voltage drop force | Availability: | The flag is available per channel. |
| Voltage drop force | API: | `DPS_AUX_TASK.getVoltageDropForce()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.17_DPS_AUX_TASK.getVoltageDropForce.md`） |
| Voltage drop return | Trigger: | The voltage drop on the common return line (GND) on the DUT board exceeds the user defined limit.<br><br>Default threshold for the return line is 50 mV.<br><br>The flag is set if the threshold is exceeded without interruption for the time defined by the `Vdrop Hold time`（raw: `02.05.05.03.10.05_XPS256_programming_-_Default_values.md#_354611__r_Vdrop_hold_time`） parameter for the corresponding pin. Note that the Vdrop Hold time parameter can be set only in the `DC Scale Safety editor`（raw: `02.05.05.03.10.05_XPS256_programming_-_Default_values.md`）. The time can be set separately for the force line and for the return line.<br><br>For XPS256 channels in DPS operating mode, see `max_voltage_drop_return`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__max_voltage_drop_return`） in `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）.<br><br>For XPS256 channels in PMU operating mode, see `SPMU_PIN_TASK.returnDropMax()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.234.01.29_SPMU_PIN_TASK.returnDropMax.md`）. |
| Voltage drop return | Action: | By default, the channel remains connected.<br><br>The channel is disconnected if the `Vdrop Disco`（raw: `02.05.05.03.10.05_XPS256_programming_-_Default_values.md#_354611__r_Vdrop_Disco`） parameter is set to ON for the corresponding pin. Note that the Vdrop Disco parameter can be set only in the `DC Scale Safety editor`（raw: `02.05.05.03.10.05_XPS256_programming_-_Default_values.md`）. |
| Voltage drop return | Availability: | The flag is available per channel. |
| Voltage drop return | API: | `DPS_AUX_TASK.getVoltageDropReturn()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.19_DPS_AUX_TASK.getVoltageDropReturn.md`） |

### Tables（脚本逐字抽取，第 4 张）

 | 8  | Lost measurementstoBeChecked  | Set to 1 if not all measurement results were recorded because the test stopped earlier than expected. |
 | 9  | Type mismatch  | Set to 1 if at least one measurement has been executed in a range that does not match the requested measurement type. |
 | 10  | Wrong hardware state  | Set to 1 if the hardware switched into an unexpected state that caused the test to fail (for example, a disconnect for safety reasons). |

### Tables（脚本逐字抽取，第 5 张）

| Bit | Flag | Description |
|---|---|---|
| 0 (LSB) | Current sink limit is reached | Set to 1 if current sink limit is reached (Clamp low) for at least one measurement. |
| 1 | Current source limit | Set to 1 if current source limit is reached (Clamp high) for at least one measurement. |
| 2 | Clamp low was reached | Set to 1 if clamp low was reached during the test for a DC Scale pin where no measurement was executed. |
| 3 | Clamp high was reached | Set to 1 if clamp high was reached during the test for a DC Scale pin where no measurement was executed. |
| 4 | Range underflow | Set to 1 in case of a range underflow has been detected for at least one measurement. |
| 5 | Range overflow | Set to 1 in case of a range underflow or a range overflow has been detected for at least one measurement. |

<!-- 语法节 end -->

## 是什么

> **一句话**：**XPS256 这张卡自己的「仪表盘 + 保险丝」。**
> 卡内建了一套自保护机制和状态指示——**过压、过流、过热、压降过大、DUT 板被拔、
> 探针接触不良**等等，都会亮一个**标志（flag）**；有些标志还会**直接断开通道**。
> **读这一页的问题永远是同一个：「卡断了/报错了，是哪个标志亮了，我该做什么。」**
> `stage: level`——它管的是供电那一段的**保护与状态**。

### 标志分三大类（原文的目录结构）

| 类别 | 里头有什么 | 性质 |
|---|---|---|
| **Status flags and warnings** | surge tracker 的 7 个标志、量程切换失败、量程溢出、压降 warning ×2 | **警告**：告诉你情况不对 |
| **Operating state** | Constant current / Constant voltage | **状态**：现在工作在恒流还是恒压 |
| **Safety and self-protection** | Current limit disconnect、DUT board disconnect、Overpower/Overcurrent/Power budget exceeded、Overtemperature、Overvoltage、Safety line、Unregulated、Voltage drop force/return | **保护**：会**断通道** |

**每个标志原文都给了四个字段**（这是本页最有用的结构，逐条见上面「语法 / 参数」节）：
**`Trigger`（怎么触发）/ `Action`（该怎么办）/ `Availability`（什么条件下这个标志可用）/
`API`（用哪个函数读它）**。
—— **`Action` 那一栏才是出问题时真正要读的**；`API` 那一栏告诉你用哪段代码去读/清。

> **上面「语法 / 参数」节里是 18 张表，不是 1 张**——这不是脚本切错了，是**语料的原样**：
> 原文这张大表在 HTML 转 markdown 时被**拆成了 18 段连续的管道行**，段与段之间夹着散文
> （`Trigger:` 的说明、`Action:` 的说明…）。脚本只认**连续 ≥3 行**的管道表格，
> 所以抓成 18 张。**逐字没丢，只是被分段了**；要按标志读，**照标志名去搜**。
> 实测 `Action:` 出现 16 次、`Availability:` 20 次——**有几个标志的某一栏落在被拆散的
> 散文里，没进表**，那种情况得回 raw 看（`02.05.05.03.10.02`，第 49 行起）。

### 通道被断开之后（原文给了**两套**恢复流程，**别用错**）

**第一件事永远是：先确认断开的原因已经消除。** 之后分两种情况：

| 你当时在哪 | 要做什么 |
|---|---|
| **在 testflow 里**（跑测试时断的） | ①用 `DPS power flags - get...() functions` 那组 API 查标志状态；②**用 SmarTest 把通道 disconnect**（related 错误信息会进 report window，标志会被清掉）；③再 connect |
| **在 hardware view 里手工操作时断的** | **PMU 模式**的针：在 ADC 子面板里做一次 dummy measurement，relay action 设成 **`NT`**；**DPS 模式**的针：点 Eclipse Work Center 工具栏上的 **Disconnect**。之后同样 connect |

> **两套流程不能互换**，因为「怎么清掉标志」的机制不同——testflow 里靠 SmarTest 的
> disconnect，hardware view 里 PMU 靠 dummy 测量 + `NT`、DPS 靠工具栏 Disconnect。
> **这一步做错的表现是：标志一直不清，通道连不回去。**

## 典型用法

**排查路径（照这个顺序走）**：

1. **先分类**：亮的标志属于上表哪一类？是「警告」还是「保护（已断通道）」？
2. **读 `Action`**：上面「语法 / 参数」的表里，每个标志都带 `Action` 栏——**那是文档给的处置**。
3. **用对的 API 读**（原文在 `Status flags and warnings` 一节给了三个入口）：
   `DPS status flags - get...() functions` / `DPS power flags - get...() functions` /
   `DPS_AUX_TASK.getSurgeTrackerStatus()`
   （raw 路径见「语法 / 参数」节里各标志的 `API` 栏）。
4. **通道断了 → 按上面的两套流程之一恢复。**
5. **要看全局状态**：命令 **`TSST?`（TeSt STatus）**——见下。

### `TSST?` 和这些标志不是一回事（**容易混**）

原文（`DC event status` 一节）：`TSST?` 返回的是**上一次执行的测试**在 DC event 上的
**全局**信息，以及**所有已记录测量的累计状态**。三个要点：

- **前提**：必须已经跑过 test point pattern（DC Scale 针）。
- **累计信息在 functional test 开始时被清掉**，之后一直有效到下一次 functional test 开始。
- **`TSST?` 的回复是两段**：一段讲测试结果，一段讲测试状态。

**区别记法**：**本页的标志是「卡现在的状态」，`TSST?` 是「刚才那次测试攒下来的状态」。**
一个是卡在说话，一个是测试在说话。

## 和谁有关

**入边 79 条 / 22 篇**（`inline` 口径）——**这是 XPS256 章里入边最密的页之一**，
因为它同时被三种页引用：**保护相关的专题页、Hardware view 的按钮说明、特定 setup 任务页**。

**被谁当作入口**：

- `XPS256 specific setup tasks`（`02.05.05.03.10.01`）—— **一口气锚了 7 个标志**
  （Current limit disconnect / Overpower / Overtemperature / Overvoltage /
  Voltage drop force / Voltage drop return），**它是「出问题该去哪」的主导航**。
- [[xps256-programming-dps-operating-mode]] —— Hardware view 的 `Check Status Flags` 按钮指向本页。
- [[xps256-pmu-operating-mode]] —— **PMU 模式的 Hardware view 有同一个按钮**，
  所以**本页不是 DPS 专用的**（这一点从页名看不出来，必须写在这儿）。
- `XPS256 force and clamp voltages` / `XPS256 force and clamp currents` —— 讲 clamp 时
  引本页的 **Clamp distance too low**（原文：clamp 距离连续超过 **400 µs** 太小就置位）。
- `XPS256 arbitrary waveform generator (AWG)` —— 讲压摆率时引本页。

**并列（未建页，不链）**：`XPS256 sitemap`（导航）、`XPS256 surge tracker`（surge 机制的专页，
本页有 7 个标志是它的）、`XPS256 operating modes`。

**上游 API 页（未建页）**：`DPS status flags - get...() functions`、
`DPS power flags - get...() functions`、`DPS_AUX_TASK.getSurgeTrackerStatus` —— 
**「怎么用代码读标志」的答案在这三篇里**，本页只给标志的含义与处置。

> 上面每条都来自 `edges.jsonl` 里带原句的边。**本页没有推断。**

## 版本

- **Introduced in SmarTest 7.10.1**（和 [[xps256-pmu-operating-mode]]、
  [[xps256-programming-dps-operating-mode]] 同批引入）
- **SmarTest 7.10.2：新增 `DUT board disconnect` 与 `Safety line` 两个状态标志。**
  —— **这两个标志在 7.10.1 上是没有的**；在 7.10.3 上有。

## ⚠️ 语料里的坏字符

`more than 400 渭s` 里的 **`渭` 应为 `µ`**（微秒）。
同类的还有 [[pogo-pad-and-via-design]] 里的 `碌`——**µ 在这份语料里至少有两种坏法
（`渭` / `碌`）**，看到不认识的汉字夹在数字和单位之间，先怀疑它是 µ。
另见 `鈥慴`/`鈥慸`/`鈥慼`（短横 + 后一个字母被一起吃掉）：
`Standard鈥慸ensity` = *Standard-density*，对照表在 [[pogo-block-compatibility]]。
**语料问题，raw 只读不许改（§1.1）。**

## 出处

- 定义文档：`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.02_XPS256_status_flags.md`
  （TDC `354167.htm`，33,302 字节，247 行）
- **入边 79 条 / 22 篇**（`inline` 口径）——**本页的入边里有大量锚点**
  （`#_354167__r_…` 这种指到「某一个标志」的深层链接），
  这是它入边数高的一大原因：**同一篇文档会为每个标志各留一条链接**。
  **边数高不代表引用它的文档多**（79 条 / 22 篇，比例约 3.6:1）。
- 所属：**Test Head Cards → XPS256**（`02.05.05.03`）
- 本页 `verified: doc-only` —— **没有在任何真实 XPS256 上触发过这些标志**
  （§11：文档里有 ≠ 你这台会这样）。**`Action` 栏照文档抄，动手前先看现场。**
