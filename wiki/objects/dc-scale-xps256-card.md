---
type: object
title: DC Scale XPS256 card
layer: n/a
stage: pin
tags: [test-head-card, dc-scale, dps, vi-card, exa-scale, ganging]
related: [dc-scale-uhc4t-card, xps256-status-flags, xps256-pmu-operating-mode, xps256-programming-dps-operating-mode, ganging, hv-protection]
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# DC Scale XPS256 card

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **10,659 字符逐字取自** `<02_System_reference/02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>` 及其子主题 `<02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.10_XPS256_programming_-_Ganging.md>`、`<02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>`、`<02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.17_XPS256_programming_-_Surge_tracker.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 XPS256 programming overview › XPS256 programming - Ganging）

### Check gang connection example

The following code shows a standard example for a gang connection test using the fast parallel test and the detailed test on the site in focus only.

```
SPMU_TASK   spmuTask;
HW_STATE    hwState;
ARRAY_I     goNogoResultArray;
ARRAY_I     perPinResultArray;

STRING      pinList = "XPS256_PMU_GANG,XPS256_DPS_GANG";
int         samples = 10;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Disconnect the tested pins
    //
    spmuTask.pin("XPS256_PMU_GANG").disconnect();

    spmuTask.execMode(TM::FORCE_OFF).execute();

    DISCONNECT();

    //
    // Perform the gang connection test in parallel on all active sites
    //
    hwState.checkGangConnectionParallel("XPS256_PMU_GANG,XPS256_DPS_GANG", samples, goNogoResultArray);

    //
    // Evaluate the go/no-go results, re-test failing sites
    //
    FOR_EACH_SITE_BEGIN_WITH_QUERY();
    {
        cout << "Parallel gang connection test, GoNogo result for site " << CURRENT_SITE_NUMBER() << ": ";

        if (goNogoResultArray[CURRENT_SITE_NUMBER() -1] == 1)
        {
            cout << "PASS" << endl;
        }
        else
        {
            cout << "FAIL" << endl;

            //
            // Serial test identifies failing pins
            //
            hwState.checkGangConnection("XPS256_PMU_GANG,XPS256_DPS_GANG", samples, perPinResultArray);

            for (int arrayIndex = 0; arrayIndex < perPinResultArray.size(); arrayIndex++)
            {
                cout << "\tDetailed result for site " << CURRENT_SITE_NUMBER()
                     << ", pin " << arrayIndex + 1 << ": " << perPinResultArray[arrayIndex] << endl;
            }
        }
    }
    FOR_EACH_SITE_END();
}
ON_FIRST_INVOCATION_END();
```

### Examples（取自子主题 XPS256 programming overview › XPS256 programming - PMU operating mode）

The following examples demonstrate how to set up an XPS256 pin for a standard current measurement.

The three examples are set up in a three-step sequence of connecting the pin and applying the basic setup, measuring the requested parameter, and disconnecting in a separate task. This sequence is suitable for XPS256-specific tests, since very often more than one setup has to be applied and more than one measurement has to be carried out before the pin is disconnected again.

 These examples are available in the following sections:

- `Example 1: SmartRDI, pattern鈥慴ased programming`（raw: `02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_pattern-based`）

Pattern鈥慴ased programming using SmartRDI is the recommended solution that requires the least amount of code and on the other hand delivers the most stable result in terms of timing.

- `Example 2: SmartRDI, code鈥慴ased programming`（raw: `02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_code-based`）

Code鈥慴ased programming using SmartRDI needs some more code and must follow the structure of the wrapped test method APIs.

- `Example 3: Test method API SPMU_TASK`（raw: `02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_TM_API_based`）

This example is based on the test method APIs and is strongly tied to the structure of the underlying commands.

The code of the three examples generates the same measurement sequence for the programmed pin. If you use the `Trace Function`（raw: `../02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.md`） to compare the code鈥慴ased SmartRDI example and the example based on the test method APIs, you will get the same output in the MCDLog file.

### Example 1: SmartRDI, pattern鈥慴ased programming（取自子主题 XPS256 programming overview › XPS256 programming - PMU operating mode）

The example uses a code鈥慴ased `RDI command`（raw: `../02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md#_142604__dle_RDI_command`） to setup and connect the XPS256 pin. The following `RDI block`（raw: `../02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md#_142604__dle_RDI_block`） performs a pattern鈥慴ased measurement. The last RDI command disconnects the XPS256 pin in code鈥慴ased mode.

Since the RDI block uses a specialized `DC event`（raw: `../02.07_Test_Method_Reference/02.07.04.01.63_EVENT_...__DC_events_API_reference.md`） to perform the measurement, only the measurement related parameters must be defined. In contrast, for code鈥慴ased programming with SmartRDI or programming with test method APIs, all parameters must be specified also for the measurement.

```
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
    rdi.dc().pin("XPS256_PMU_1")
            .vForce         ( 5.0 V)          .vForceRange(7.0 V).preCharge(0.0 V)
            .iClamp         (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .execute        ();

    RDI_BEGIN();
    {
        rdi.dc("iMeasXPS256").pin("XPS256_PMU_1")
                .iMeas      ()
                .average    (16)
                .measWait   (2.5 ms)
                .execute    ();
    }
    RDI_END();

    rdi.dc().pin("XPS256_PMU_1").disconnect().execute();
}
ON_FIRST_INVOCATION_END();

double resultIMeasXPS256;

resultIMeasXPS256 = rdi.id("iMeasXPS256").getValue("XPS256_PMU_1");
```

### Example 2: SmartRDI, code鈥慴ased programming（取自子主题 XPS256 programming overview › XPS256 programming - PMU operating mode）

The first `RDI command`（raw: `../02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md#_142604__dle_RDI_command`） connects and sets the XPS256 pin: DC Scale pins in PMU operating mode are automatically connected if `iForce()`（raw: `../02.07_Test_Method_Reference/02.07.13.12.02.16_iForce.md`） or `vForce()`（raw: `../02.07_Test_Method_Reference/02.07.13.12.02.41_vForce.md`） are used within the RDI command. For more information, see also `Setting up DC Scale pins with SmartRDI`（raw: `../02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md`）.

The second RDI command contains a measurement iMeas(). The programmed pin remains connected after the measurement.

The third RDI command contains no measurement but the disconnect() function: Output relays are controlled again and the pin is disconnected.

In this example, SmartRDI is mainly a wrapper for the test method API `SPMU_TASK`（raw: `../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md`）. The structure is therefore tied to the SPMU_TASK and to the corresponding low level commands as mentioned in `Example 3: Test method API SPMU_TASK`（raw: `02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_TM_API_based`） below.

```
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
    rdi.dc().pin("XPS256_PMU_1")
            .vForce         ( 0.0 V)          .vForceRange(7.0 V).preCharge(0.0 V)
            .iClamp         (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .execute        ();

    rdi.dc("iMeasXPS256").pin("XPS256_PMU_1")
            .vForce         ( 5.0 V)          .vForceRange(7.0 V)
            .iClamp         (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .iMeas          ()
            .average        (16)
            .measWait       (2.5 ms)
            .execute        ();

    rdi.dc().pin("XPS256_PMU_1").disconnect().execute();
}
ON_FIRST_INVOCATION_END();

double resultIMeasXPS256;

resultIMeasXPS256 = rdi.id("iMeasXPS256").getValue("XPS256_PMU_1");
```

### Example 3: Test method API SPMU_TASK（取自子主题 XPS256 programming overview › XPS256 programming - PMU operating mode）

XPS256 measurements, created by the test method API `SPMU_TASK`（raw: `../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md`） are based on the low-level commands `DCCH`（raw: `../02.06_Command_Reference/02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md`） and `DCVH`（raw: `../02.06_Command_Reference/02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md`） in combination with `DCEX`（raw: `../02.06_Command_Reference/02.06.02.02.43_DCEX_-__DC_set_EXecute.md`）. These commands define complete measurement sequences including connecting and disconnecting the programmed pins.

 The tasks spmuTask_connect as well as spmuTask_measure of the example must therefore define the same mode() and connectState() and ensure that the same ranges are used, although the first task is used only to connect and activate the pin while the second task is used only for the measuring:

- spmuTask_connect: The combination of `relay("NT")` and `execMode(TM::FORCE_ON)` of the connect task enables switching of the output relays and activation of the pin. A measurement is not supported by this task.
- spmuTask_measure: Relay control is set to "NO" to inhibit actions of the output relays. The pin remains therefore connected after the task has been performed. `execMode(TM::PVAL)` causes that the requested value is measured and returned as per pin value and pass/fail results.
- spmuTask_disconnect: The combination of `relay("NT")` and `execMode(TM::FORCE_OFF)` causes that the pin is disconnected. Although no more measurements are performed, some parameters such as `min()` and `max()` must be defined for a valid setup.

```
SPMU_TASK spmuTask_connect;
SPMU_TASK spmuTask_measure;
SPMU_TASK spmuTask_disconnect;

ON_FIRST_INVOCATION_BEGIN();
{
    spmuTask_connect.pin("XPS256_PMU_1")
            .mode           ("VFIM")
            .vForce         ( 0.0 V)          .vForceRange(7.0 V).preCharge(0.0 V)
            .clamp          (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .min            (-5.0 mA)
            .max            (50.0 mA)
            .relay          ("NT");

    spmuTask_measure.pin("XPS256_PMU_1")
            .mode           ("VFIM")
            .vForce         ( 5.0 V)          .vForceRange(7.0 V)
            .clamp          (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .min            (-5.0 mA)
            .max            (50.0 mA)
            .relay          ("NO")
            .settling       (2.5 ms)
            .samples        (16);

    spmuTask_disconnect.pin("XPS256_PMU_1")
            .vForce         ( 0.0 V)
            .min            ( 0.0 mA)
            .max            (10.0 uA)
            .relay          ("NT");

    spmuTask_connect   .execMode(TM::FORCE_ON) .execute();
    spmuTask_measure   .execMode(TM::PVAL)     .execute();
    spmuTask_disconnect.execMode(TM::FORCE_OFF).execute();
}
ON_FIRST_INVOCATION_END();

double resultIMeasXPS256;

resultIMeasXPS256 = spmuTask_measure.getValue("XPS256_PMU_1");
```

### Example（取自子主题 XPS256 programming overview › XPS256 programming - Surge tracker）

### Simultaneously tracking the voltage and the current

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();
{
    auxTask.pin("XPS256_PMU_1")
            .setMode                    (TM::SURGE_TRACKER)
            .selectVSensorSetThresholds (-0.5 V, 3.5 V)
            .selectISensorSetThresholds (-0.1 A, 0.4 A);

    auxTask.execute();

    ...
    ...

    auxTask.pin("XPS256_PMU_1").checkSurgeTracker(TM::AGAINST_BOTH);
}
ON_FIRST_INVOCATION_END();

TM::SURGE_TRACKER_STATUS statusVoltage, statusCurrent;

auxTask.getSurgeTrackerStatus("XPS256_PMU_1", statusVoltage, statusCurrent);

cout << "Site " << CURRENT_SITE_NUMBER() << ", Voltage surge tracker: " << statusVoltage << endl;
cout << "Site " << CURRENT_SITE_NUMBER() << ", Current surge tracker: " << statusCurrent << endl;

```

<!-- 语法节 end -->

## 是什么

**XPS256 是一张「高密度、可扩展」的 DUT 电源与 V/I 卡。** 原文第一句：

> 「The XPS256 is a **high-density scalable DUT power supply and V/I card** for all SOC test
> applications. The card belongs to the **DC Scale family** and **can reside in any channel card slot
> of a V93000 EXA Scale system**.」

**三个身份信息一次说清**：

| 维度 | 值（原文） |
|---|---|
| 族 | **DC Scale family** |
| 系统 | **V93000 EXA Scale** |
| 插槽 | **any channel card slot**（任意通道卡槽） |

### 规格：**256 路，四象限，-2.5 V 到 +7.0 V，每路 1 A**

原文第二段：

> 「The card features **256 full 4 quadrant VI sources**, each of them capable to **force or sink
> -2.5 V to +7.0 V at up to 1 A**. **Ganging for higher currents is supported.**」

| 项 | 值 |
|---|---|
| 源数 | **256**（`256 full 4 quadrant VI sources`） |
| 每源能力 | **force 或 sink**（四象限） |
| 电压范围 | **-2.5 V 到 +7.0 V** |
| 电流 | **最高 1 A** |
| 想更大电流 | **ganging**（`Ganging for higher currents is supported.`） |

> ⚠️ **这一句在 raw 里有两个坏字，见下「出处」⚠️①。**
> **原文的 `鈥哣` 是两个坏字符，解出来是「一个 U+2006 六分之一全角空格 + 字母 `V`」**
> ——也就是说**原文要写的是单位 `V`（伏）**，中间那个空格是排版用的窄空格。
> **本页正文里的 `-2.5 V` / `+7.0 V` 是我按这个解释写的**（推断，附字节依据见「出处」）。

**「full 4 quadrant」是这张卡的定位关键**——**能 force 也能 sink**，
所以它同时是「供电」和「吸收电流」的卡（即源/灌两用）（推断：
四象限在电源语境里就是 force/sink 两个方向，**原文在括号外没有展开解释这个词**）。

### 它长什么样（**④ 图证，2026-09-20 补**）

`350665.png`（图注 `XPS256 card photo`，550×413）——**本篇自带的那张实物照片**。
**照片上没有一个字**，所以下面这些**在 raw 里 grep 不到**，要核只能自己开
`F:\master-dev\dorm-wsl-sytest\tdc-html\raw\350665.png`：

- 卡是**长条形**的，顶面覆盖着**成排的长方形黑色盖板**（板与板之间是细缝，每块用若干十字螺钉压住）。
  **块数本页数不出**：缝很细，又是斜视角——**数出来的数不敢写**。
- 一端的前缘有**两组多针连接器**（黑色外壳、密集针阵），旁边压着**一条银色金属压条**（带螺钉）。
- 照片里还有**两根白色半透明软管**，末端是**带蓝色塑料卡箍的金属圆柱接头**。
- 卡的一侧露出**绿色 PCB 与一条铜色边条**，边上有一排贴边的小器件。

**这张图答不了的**：`256` 路在哪、精度 / 噪声 / 动态响应、每卡功耗与散热、
以及**这张卡属于哪个系统**——**我放大看过的那几处（顶面、前缘、两个接头）都没有可读文字**，
照片上也没有看到可读的型号丝印。

### 它和同族 UHC4T 不是一个量级

| | **XPS256**（本页） | **UHC4T**（[[dc-scale-uhc4t-card]]） |
|---|---|---|
| 通道数/卡 | **256** | **4** |
| 每通道电流 | **1 A** | **40 A** |
| 电压范围 | **-2.5 V 到 +7.0 V** | **本篇未写** |
| 定位 | **高密度、可扩展** | **超高电流** |

> **这张表是「两篇各自的正文拼出来的」**——**两篇原文都没有互相提对方**。
> UHC4T 那一列的值来自 [[dc-scale-uhc4t-card]] 的 `sources:` 那一篇，**不是本篇**（推断）。

### 语法节里给了什么（**都是子主题的，不是本篇的**）

本页「语法 / 参数」节 **10,659 字符**，来源不是定义文档本身，而是**三个子主题**（骨架段名里写明了）：

| 取自 | 段名 |
|---|---|
| `…03.10.10_XPS256_programming_-_Ganging.md` | `### Example（取自子主题 … Ganging）` |
| `…03.10.15_XPS256_programming_-_PMU_operating_mode.md` | 同节内 |
| `…03.10.17_XPS256_programming_-_Surge_tracker.md` | 同节内 |

**所以本页的「语法 / 参数」是「XPS256 编程」那一族的代码示例**，不是这张卡的参数表。
**三段子主题原文本页都没读**（见「出处」）。

**其中最值得注意的一段**（在语法节里，**逐字**）是
`### Check gang connection example` 的第一句：

> 「The following code shows a standard example for a gang connection test using **the fast parallel
> test and the detailed test on the site in focus only**.」

**它给的是 gang 连接测试的两级做法**：先全体并行快测，再只对 focus site 细测（推断，
依据是代码里先 `checkGangConnectionParallel(...)`、再用
`FOR_EACH_SITE_BEGIN_WITH_QUERY()` 挑失败 site 重测）。
**本页不逐行讲那段代码**——**它不属于本页的 `sources:`**。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` 段，也没有一条命令或代码。**
本篇是一张卡的「入口页」，用法全在它 `#### Subtopics` 列的十个子页里：

| 子页 | 管什么（**按标题读，本页都没读**） |
|---|---|
| `XPS256 sitemap` | 导航 |
| `XPS256 specifications` | 规格 |
| `XPS256 functionality and features` | 功能与特性 |
| `XPS256 pogo pin assignment` | pogo 针分配 |
| `XPS256 operating modes` | 工作模式 |
| `XPS256 force, clamp, and measure voltages` | 电压的 force / clamp / 测量 |
| `XPS256 force, clamp, and measure currents` | 电流的 force / clamp / 测量 |
| `XPS256 ganged` | **ganging（本文正文唯一提到的机制，详解在这一篇）** |
| `XPS256 load step response` | 负载阶跃响应 |
| `XPS256 programming overview` | **编程总览——「怎么写代码用它」的答案在这一篇** |

**本篇正文能读出的「怎么用」只有一句**：
**`Ganging for higher currents is supported.`**——
**要超过 1 A 就用 ganging，具体规则在 `XPS256 ganged` 那一篇**（**没读**）。

**DUT 板设计侧的两个入口**（`## Related information` 原文列的两条）：
`DC Scale XPS256 card (Electrical design rules)` 与 `HV (High-Voltage) protection`。

### 两张硬件视图的图（**④ 图证，2026-09-20 补**）

**先说来源**：这两张图**不在本篇 `sources:` 那篇里**——它们在
`02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md` 里，
也就是**本页「语法 / 参数」节逐字复制的那篇子主题**。
**那篇的正文本页仍然没读，只读了它的两张图。**

| 图 | 大小 | 图上看得出的东西（**多数是像素、raw 里 grep 不到**——**但有两个例外，见下**） |
|---|---|---|
| `354251.png`（图注 `HW view of XPS256 in PMU operating mode`） | 641×458 | 抬头 `Site: 1` / `Pin: XPS256_PMU_1` / `Channel: 41701` / `DC-Scale: XPS256` / `PinType: DC-Signal`；字段有 `Mode: Force Voltage`、`Connect State: NORM`、`Status: disconnect`（红字）、`Force Voltage Range: 6.5 V`、`Clamp Current Range: 1 A`，以及一节安全限制（`Drop Force Limit: 150 mV`、`Open Loop Protection: DIODE`、`CC H:Time To Alarm: 1 ms`…）；按钮有 `Check Status Flags` / `Profiling` / `Force Sense Check` / `Surge Tracker`（下挂 `Voltage` 与 `Current` 两个结果框）/ `Max Voltage Drop`（下挂 `Force` / `Return`）/ `Check Gang Connection`（下挂 `Pos Result`） |
| `355135.png`（图注 `XPS256 HW view PMU Measure dialog`） | 450×626 | 一个标题为 `DC Signal Measurement - XPS256 PMU_1` 的对话框：`Channel Mode: VF`、`Force Voltage Range (mV): 6.5 V`、`Clamp Current Range (uA): 1 A`、`Pass_max` / `Pass_min`、四个测量类型单选（`Current Measurement` 被选中）、`High Accuracy [-0.5V;1.5V]` 复选框、`Regulation` 与 `Safety` 两节、`Setting Time (ms): 1 ms`、`Number of Samples: 100`、`Execution Mode: SER - serial`、`Relay Action: NT`、`Single Measurement` / `Looped Measurement` 单选，下面一个 `Result 0 A` 的大框 |

> ⚠️ **表里有两个例外，别把它们当图证**：`Surge Tracker`（全语料 **5 篇**）与 `Check Gang Connection`
> （**2 篇**）**在 raw 文本里搜得到**——它们只是「图与文本互证」，**不是 ④ 图证**
> （§11.4 对图证的定义是「**只存在于图里**」）。表头那句「都是像素、grep 不到」对这两个不成立，
> **2026-09-20 已收窄。**
> **纠正的来由**：拿 `Surge Tracker` 回 raw 数了一下，数出 5 篇。
> **这条判据是可以机械复核的**——**凡标 ④ 的格，都该这么数一遍**（本轮 6 条「0 命中」是这么验的）。

**这两张图解决掉的**：
1. **`Check Gang Connection` 确实是硬件视图上的一个按钮**——本页「语法 / 参数」节里那段
   gang 连接测试代码（`checkGangConnectionParallel(...)` / `checkGangConnection(...)`）
   在 GUI 上对应的入口就是它（**这个对应是推断**：图上只有一个按钮名，
   **没有一处说明它调哪个 API**）。
2. **`Surge Tracker` 也确实是硬件视图上的一个按钮**，且带 `Voltage` / `Current` 两个结果框
   ——本页此前只在语法节里见过 `TM::SURGE_TRACKER` 这个名字（**对应关系同样是推断**）；
   本页 出处里那句「`Surge tracker` / `current monitor` 等机制本页都没读」**现在有一半可以补上了**：
   **名字之外，还知道它在 GUI 上长什么样**；**机制本身仍然没读**。
3. **PMU 工作模式下 `Mode` 与 `Connect State` 是可设字段**，`Status` 会显示 `disconnect`
   ——但**图只给了 `Force Voltage` 这一个取值**，
   **「这张卡有哪几种工作模式」本页仍然答不了**（答案在未读的子页 `XPS256 operating modes`）。

**图上还有一处不自洽，照实记、不替它改**：几个字段的单位后缀和框里的值对不上——
`Force Voltage Range (mV)` 里填的是 `6.5 V`，`Clamp Current Range (uA)` 里填的是 `1 A`。
**图上如此，本页不解释**（图里没有一句说明这些后缀是什么意思）。

## 和谁有关

- [[dc-scale-uhc4t-card]] — **同族、同批建的兄弟页**（DC Scale 另一张 DPS 卡）。
  **规格量级相反**：本页是 256×1 A 的高密度卡，UHC4T 是 4×40 A 的超高电流卡。
  **两篇原文都没提对方**——这条关系是**同族归属**推出来的（推断）
- [[xps256-status-flags]] — **同一张卡的状态/保护那一面**。
  **那是 XPS256 章里入边最密的页之一**；**本页是「卡是什么」、那一页是「卡报什么」**
  （推断，仅指关系；**那页本页没读**）
- [[xps256-pmu-operating-mode]] / [[xps256-programming-dps-operating-mode]] —
  **本卡两种工作模式的专页**（**都没读**）。
  **注意**：语法节里就有一段取自 `XPS256_programming_-_PMU_operating_mode.md`
  （**那段的原文我没读，只有脚本抄进来的那份**）——
  **2026-09-20 补：那篇的正文仍然没读，但它的两张图读了**，
  见上「两张硬件视图的图（④ 图证）」
- [[ganging]] — **本页正文唯一提到的机制**（`Ganging for higher currents is supported.`）；
  详解在 `XPS256 ganged` 那一篇（**未建 / 未读**）
- [[cross-card-ganging-requires-ddic]] — **ganging 的跨卡前提**（**那页本页没读**）。
  **本页的 `## 语法 / 参数` 里有 gang 连接测试的示例代码**，
  **但「跨卡要先 DDIC」这条本篇一个字没写**（推断，仅指关系）
- [[hv-protection]] — **`## Related information` 指到的 DUT 板侧页**（**没读**）
- `DC Scale XPS256 card (Electrical design rules)`（**未建**）—
  **⚠️ 注意重名**：这一篇的**标题和本页一模一样**，但它是 DUT 板设计规则里的一篇，
  **不是本页**。原文两条链接并排时很容易点错（见下「出处」⚠️④）
- `XPS256 current monitor`（**未建**）— 语法节里出现过（**没读**）
- [[pin]] / [[dc-test-programming]] — **同主题的页**，**本篇没有一句把它们连起来**（推断，仅指归属）
- **十个子页一篇都没读**（见上表）

## 版本

原文 `## Functional changes` 只有一条：

- **`Introduced in SmarTest 7.10.1`**

**就这一条，没有别的。**

> **这一条不是哨兵值**（不是 `Introduced before SmarTest 6.3.2`）——
> **所以它是一条真版本事实：XPS256 是 SmarTest 7.10.1 引入的。**
>
> **本篇没有任何 MTP / SmartRDI / TP360 的条目**——§11.2④ 说的产品线撞车在本篇没有出现。
> **也没有 7.10.1 之后的条目**——**所以「7.10.1 之后这张卡的规格有没有变过」本篇答不了**（推断）。

## 出处

`sources:` 一篇：
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md`
（`350661.htm`，1,785 字节，33 行）——**整篇读完**。**这是本批最少的几篇之一。**

**本页做了什么、没做什么**：

- **「语法 / 参数」节不是 `sources:` 那篇抽的。** 那篇自己**没有语法段**，
  脚本改从**三个子主题**抄了 **10,659 字符**（骨架段名里写明了）：
  `…03.10.10_XPS256_programming_-_Ganging.md`、
  `…03.10.15_XPS256_programming_-_PMU_operating_mode.md`、
  `…03.10.17_XPS256_programming_-_Surge_tracker.md`。
  **这三篇本页一篇都没有读原文**——本节凡引语法节内容，依据是**页内那段逐字拷贝**。
- **十个子页一篇都没读。**
  **所以「这张卡有哪些工作模式、怎么 force/clamp/measure、ganging 的规则是什么、
  编程怎么写」本页一个字都没有**——**本页只有「它是什么规格」这一段。**
  （**2026-09-20 补**：其中「这几样在 GUI 上长什么样」**图证补上了一小块**，
  见上文「两张硬件视图的图（④ 图证）」；**规则本身与编程仍然一个字没有。**）
- **三张图都看了（2026-09-20 补）**——**上一版这里写的是「一张图都没看」，
  并由此写下「本页没有任何来自图的结论」；那句话现在是错的，按实际改动如下**：
  - **`350665.png`（`XPS256 card photo`）——看了**，见上文「它长什么样（④ 图证）」。
    **照片上没有可读文字**，它能给的只有形态。
  - **`354251.png` / `355135.png`——看了**，见上文「两张硬件视图的图（④ 图证）」。
    **这两张不在本篇 `sources:` 里**，它们在语法节那篇子主题
    `02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md` 里——
    **上一版的「本页没做的」根本没想到它们，这次一并补上。**
  - **图上那些字在 raw 里 grep 不到**（`DSO+` 那类写法全语料 0 命中、`DC-Signal` 0 命中），
    要核只能自己开 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\` 下对应的那张 `.png`。
- **`## Related information` 的两篇都没读**（`DC Scale XPS256 card (Electrical design rules)`、
  `HV (High-Voltage) protection`）。
- **规格细节一律没有**：精度、噪声、动态响应、每卡功耗、散热——
  **本篇只写了「256 路 / 四象限 / -2.5 V..+7.0 V / 1 A」这四个数**。
- **「EXA Scale 之外的系统能不能用」本篇没写**——原文只说
  `can reside in any channel card slot of a V93000 EXA Scale system`（**推断：没提别的系统，
  但也没说「只能」**）。
- **`Surge tracker` / `current monitor` 等机制本页都没读**——
  只在语法节里见过名字（对照：[[xps256-status-flags]] 有 7 个标志是 surge tracker 的，
  **但那不是本页的 sources**）（推断）。

> ⚠️ **本篇的语料瑕疵，照实记、一处没替它改**：
> ① **同一个坏字组合出现两次：`鈥哣`**。原文逐字：
>    `each of them capable to force or sink -2.5鈥哣 to +7.0鈥哣 at up to 1 A`
>    ——**`鈥哣` 是 §11.2① 说的那种编码损坏**（UTF-8 标点被按 GBK 读了）。
>    **本页查了字节**：这两个字在 GBK 里是 `E2 80 86 56`，
>    还原成 UTF-8 就是 **`U+2006`（SIX-PER-EM SPACE，六分之一全角空格）+ `V`**。
>    **所以原文要写的是电压单位 `V`**，中间那个是排版用的窄空格。
>    **⚠️ 拿 `2.5 V` 去 raw 里搜是搜不到的，要搜 `2.5鈥哣`**（§11.2① 的处置）。
>    **本页正文写作 `-2.5 V` 是解释后的结果，已在上文标明是推断并给了字节依据。**
> ② **`capable to` 应为 `capable of`**。原文：
>    `each of them capable to force or sink …` —— **`capable to do` 不是英语用法。**
> ③ **`4 quadrant` 缺连字符**：原文 `256 full 4 quadrant VI sources`，
>    通常写作 `4-quadrant`。**本页照抄 `full 4 quadrant` 的写法。**
> ④ **`## Related information` 两条链接之间没有分隔符**，原文逐字是一整行：
>    `[DC Scale XPS256 card (Electrical design rules)](<…>)[HV (High-Voltage) protection](<…>)`
>    —— **首尾相连，中间没有空格也没有换行**。
>    **⚠️ 而且第一条链接的文字也是 `DC Scale XPS256 card`——和本页标题逐字相同**，
>    但它是 DUT 板设计规则里的一篇。**同名两篇，容易点错。**
> ⑤ **`#### Subtopics` 的标题层级是 4 级**，比正文还深（**全语料同此形态**，
>    见 [[dc-scale-uhc4t-card]] / [[apg-pattern-file]] 的同一处）（推断）。

`verified: doc-only`
