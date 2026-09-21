---
type: object
title: SPMU_PIN_TASK
layer: L2
stage: testmethod
tags: [testmethod, dc-test, spmu, per-pin, data-container, badc, pmu, dc-scale, vfim, vm-hiz]
related: [spmu-task, spmu-pin-task-mode, pattern-controller, pin-utility, dc-result-accessor, dc-test-programming, smartest-6.5.3, smartest-7.3.1, smartest-7.4.0, smartest-7.5.0, smartest-7.5.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# SPMU_PIN_TASK

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,588 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Terminated high-impedance measurement with closed AC relay

This example configures and executes a terminated high-impedance measurement (VM_HIZ) with closed AC relay.

```
//
// Define SPMU_TASK object for high-impedance measurement
//
SPMU_TASK badc_task;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Configure high-impedance measurement with 1 ms waiting time for "pinName"
    // no force values required
    //
    badc_task.pin("pinName").mode("VM_HIZ").settling(1 ms);

    //
    // Configure terminated measurement (AC relay closed during measurement)
    // and define limits for P/F result
    //
    badc_task.pin("pinName").relay("TERM").min(0 V).max(5 V);

    //
    // Define value measurement and execute measurement
    //
    badc_task.preAction("NONE").execMode("PVAL").execute();

ON_FIRST_INVOCATION_END();

//
// Get results
//
cout << badc_task.getValue("pinName") << endl;
```

### Example 2: Pattern-controlled high impedance voltage measurement with voltage forced by pin PMU

This example shows a pattern-controlled high impedance voltage measurement. A voltage is forced with pin PMU on pin_force. This pin is cross-connected with pin_meas. The pin_meas uses the high impedance measurement path to measure the voltage of pin_force. The measurement path is configured with `SPMU_TASK`（raw: `02.07.04.01.234_SPMU_TASK.md`）.

```
virtual void run()
{
     DC_RESULT_ACCESSOR result;
     PATTERN_CONTROLLER pc;
     SPMU_TASK badcConnect;
     static STRING_VECTOR pinList;
     static STRING measPins = "pin_meas";

     ON_FIRST_INVOCATION_BEGIN();

        //
        // Connect BADC
        //
        badcConnect.pin(measPins).mode("VM_HIZ").relay("NT").connect();
        badcConnect.execute();

        //
        // Setup dynamic test, do it only one time
        // first_run is a protected variable "Boolean first_run;"
        // which is set to 'true' in initialize method
        //
        if (first_run)
        {
            PPMU_SETTING ppmuForce;
            PPMU_RELAY ppmuOn,ppmuOff;
            BADC_SETTING badcSetting;
            BADC_MEASURE badcMeasure;
            ppmuForce.pin("pin_force")
                 .vForce(forceVoltage.getValueAsTargetUnit("V"))
                 .iRange(1 uA).min(0 uA).max(2 uA);
            ppmuOn.pin("pin_force").status("PPMU_ON");
            ppmuOff.pin("pin_force").status("AC_ON");
            badcSetting.pin(measPins).min(0 V).max(5 V);
            badcSetting.wait(1 ms);
            badcMeasure.pin(measPins).numberOfSamples(16);
            badcMeasure.wait(100 us);

            pc.label("MeasBADC","@").add(ppmuForce)
                                .add(ppmuOn)
                                .add(badcSetting)
                                .add(badcMeasure)
                                .add(ppmuOff);
            pc.setup();

            first_run = false;
        }

        //
        // Execute test
        //
        FUNCTIONAL_TEST();

        result.uploadResult(measPins ,TM::RESULT_INDEX);

        pinList = PinUtility.getDigitalPinNamesFromPinList(measPins,TM::ALL_DIGITAL);

    ON_FIRST_INVOCATION_END();

    //
    // Results
    //
    int numberPins = pinList.size();
    for(int i=0; i<numberPins; i++)
    {
        ARRAY_D values = result.getValues(pinList[i]);
        int numberOfResults = values.size();
        for (int j = 0; j< numberOfResults; j++)
        {
            double value = values[j];
            cout << "PF: " << result.getPassFail() << endl;
            cout << "NumVal: " << result.getNumberOfAvailableResults(pinList[i]) << endl;
            cout << "FailInfo: " << result.getFailInfo() << endl;
            cout << "PPMU VMHIZ BADC Measurement result: " << value << endl;
        }
    }

    return;
}
```

<!-- 语法节 end -->

## 是什么

**一句话：`SPMU_PIN_TASK` 是「一个 pin 上这次 DC 测量怎么测」的数据容器。**
本篇原句只有这一行：

> 「This class is a data container to define per pin DC measurement conditions.」

**「数据容器」这四个字是它与 `SPMU_TASK` 的分工线**——本类**没有构造函数**，
也就**不能自己建对象、不能自己执行、不能自己取结果**：

> 「This class has no public constructor. The SPMU_PIN_TASK object can only be accessed via the
> SPMU_TASK.pin() function of the SPMU_TASK class.」

**即：唯一的入口是 `SPMU_TASK.pin()`**（那一篇不在本页 sources 里，
raw: `02.07.04.01.234_SPMU_TASK.md`，**本页没读它**）。

| 问题 | 本篇的答案 |
|---|---|
| 怎么拿到一个 `SPMU_PIN_TASK`？ | **只能经 `SPMU_TASK.pin()`**（原文如此） |
| 它自己有什么参数？ | `List of parameters There are no parameters. Return value There is no return value.` |
| 头文件？ | `This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/SpmuPinTask.h.` |
| 它在哪一层？ | 本篇没写；本页的 `layer: L2` / `stage: testmethod` 来自骨架的归类 |

### 它是一张「38 个旋钮」的清单，而文档只给了名字

本篇的 `Subtopics` 一节**逐条列了 38 个成员**（按 raw 的原顺序，逐字）：

`clamp()`、`compare()`、`connect()`、`connectState()`、`currentClampTimeToAlarm()`、
`currentClampTimeToDisconnect()`、`disconnect()`、`execMode()`、`forceDropMax()`、
`forceDropWarn()`、`highAccuracy()`、`iClampFilter()`、`iFilter()`、`iForce()`、
`iForceRange()`、`iMeasureRange()`、`iSlewRate()`、`limits()`、`loadCap()`、`loadStepMode()`、
`max()`、`measFilter()`、`min()`、`mode()`、`openLoopProtection()`、`preCharge()`、`pulldown()`、
`relay()`、`returnDropMax()`、`returnDropWarn()`、`samples()`、`settling()`、`vFilter()`、
`vForce()`、`vForceFilter()`、`vForceRange()`、`vMeasureRange()`、`vSlewRate()`

**⚠️ 这一篇对 38 个成员只有名字，一句说明都没有**——正文的 `## Class definition` 只讲构造，
`## Examples` 只给两个例子，`## Functional changes` 只列版本。
**所以「每个成员定什么」的答案全部在别处**（38 篇成员文档），**本页一篇没读**。

**按名字能看出的几族**（**这是本页的推断**，语料**没有分组**，
依据只是名字的前缀/构词）：`i*` = 电流侧（`iForce` / `iForceRange` / `iMeasureRange` / `iFilter` /
`iClampFilter` / `iSlewRate`）、`v*` = 电压侧（`vForce` / `vForceRange` / `vMeasureRange` /
`vFilter` / `vForceFilter` / `vSlewRate`）、`*Drop*` = 压降（`forceDropMax` / `forceDropWarn` /
`returnDropMax` / `returnDropWarn`）、`currentClampTimeTo*` = 电流钳位超时
（`Alarm` / `Disconnect`）、`connect*` / `disconnect` = 连接状态。
**本页不据此断言任何一个成员的含义。**

### 两个例子：一个静态、一个「模式 + 图形控制」

**Example 1**（标题逐字 `Terminated high-impedance measurement with closed AC relay`）
的说明逐字：

> 「This example configures and executes a terminated high-impedance measurement (VM_HIZ) with
> closed AC relay.」

**它的四条注释是这一篇里唯一的「参数含义」来源**（逐字，都在代码里）：

| 代码里的注释 | 它顺带说清的事 |
|---|---|
| `// Configure high-impedance measurement with 1 ms waiting time for "pinName"` + `// no force values required` | **高阻测量不用给 force 值**；`settling` 给的是**等待时间** |
| `// Configure terminated measurement (AC relay closed during measurement)` | **`relay("TERM")` 的注释解释是「测量期间 AC relay 闭合」** |
| `// and define limits for P/F result` | `min()` / `max()` 在这条链上是**判定限值**（注释说 `for P/F result`） |
| `// Define value measurement and execute measurement` | `execMode("PVAL")` 那一步是**值测量** |

**链的顺序**（原文逐字）：`pin("pinName").mode("VM_HIZ").settling(1 ms);` →
`pin("pinName").relay("TERM").min(0 V).max(5 V);` →（块外）`preAction("NONE").execMode("PVAL").execute();`
→ `getValue("pinName")`。
**注意它是分两条语句配同一个 pin 的**（不是一条长链），与 `SPMU_TASK` 那篇的例子写法不同。

**Example 2**（标题逐字 `Pattern-controlled high impedance voltage measurement with voltage forced
by pin PMU`）的说明逐字：

> 「This example shows a pattern-controlled high impedance voltage measurement. A voltage is
> forced with pin PMU on pin_force. This pin is cross-connected with pin_meas. The pin_meas uses
> the high impedance measurement path to measure the voltage of pin_force. The measurement path
> is configured with SPMU_TASK.」

**它比 Example 1 多出来的东西，全在「谁来触发」上**：

| 例子里的东西 | 本篇给出的信息 |
|---|---|
| `badcConnect.pin(measPins).mode("VM_HIZ").relay("NT").connect();` 紧跟 `badcConnect.execute();` | **`connect()` 是「先接上、再执行」的两步**（注释逐字 `// Connect BADC`）；`relay("NT")` 是这篇里出现的**另一个 relay 取值** |
| `PATTERN_CONTROLLER pc;` + `pc.label("MeasBADC","@").add(ppmuForce).add(ppmuOn).add(badcSetting).add(badcMeasure).add(ppmuOff);` + `pc.setup();` | **测量被挂到 pattern 的 label 上、由 pattern 触发**；`SETTING` / `RELAY` / `MEASURE` 三类对象是**注册进 `PATTERN_CONTROLLER` 的** |
| `PPMU_SETTING ppmuForce` / `PPMU_RELAY ppmuOn,ppmuOff` / `BADC_SETTING badcSetting` / `BADC_MEASURE badcMeasure` | 四条 `//` 注释之外，**本篇没有解释这四个类** |
| `FUNCTIONAL_TEST();` + `result.uploadResult(measPins, TM::RESULT_INDEX);` | **执行用的是一次 functional test**，不是 `execute()`；结果经 `DC_RESULT_ACCESSOR` 上传 |
| `PinUtility.getDigitalPinNamesFromPinList(measPins, TM::ALL_DIGITAL)` | 取结果的 pin 名单要**从 pin 字符串转出来** |
| `result.getValues()` / `getPassFail()` / `getNumberOfAvailableResults()` / `getFailInfo()` | 结果的四种读法，**本篇没有解释它们的返回** |
| `if (first_run)` + 注释 `// first_run is a protected variable "Boolean first_run;"` / `// which is set to 'true' in initialize method` | **pattern 的设置只做一次**（第二次进 `run()` 不再设） |

**一句话记法**：**Example 1 = 直接 `execute()` 测一次；Example 2 = 把测量注册进 pattern，由 `FUNCTIONAL_TEST()` 触发。**

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`，只有一个 `## Examples`。**
把两个例子合起来看，能落成动作的只有下面几条（**全部有引文或代码作依据**）：

| 要做什么 | 照哪个例子 | 关键步骤 |
|---|---|---|
| 测一个 pin 的高阻电压（`VM_HIZ`），带 P/F 判定 | Example 1 | `pin()` → `mode("VM_HIZ")` → `settling()` → `relay("TERM")` → `min()` / `max()` → `preAction("NONE").execMode("PVAL").execute()` → `getValue()` |
| 让测量由 pattern 控制、force 由别的 pin 的 pin PMU 给 | Example 2 | `pin().mode("VM_HIZ").relay("NT").connect()` + `execute()` 先接上 → 把 `PPMU_SETTING`/`PPMU_RELAY`/`BADC_SETTING`/`BADC_MEASURE` 经 `PATTERN_CONTROLLER` 注册（**只做一次**）→ `FUNCTIONAL_TEST()` → 取结果 |
| **不要**自己 `new` 一个 `SPMU_PIN_TASK` | `## Class definition` | **没有 public 构造函数**；只能经 `SPMU_TASK.pin()` |

**两条时序上的硬事实**（都来自 Example 2 的代码，不是推断）：

- **`connect()` 与 `execute()` 是两步**：`…relay("NT").connect();` 之后**另起一行** `badcConnect.execute();`。
- **`pc.setup()` 在注册完之后、`FUNCTIONAL_TEST()` 之前**——注册一次、跑多次。

**本篇一个字都没写的**：任何成员的取值清单（`mode()` 有哪几种、`relay()` 有哪几种）、
任何单位的默认值、任何报错条件。**所以照这一篇写代码是写不出来的**，
必须去 38 篇成员文档里翻——**本页因此只给「顺序」和「注释里顺带说清的那几条」。**

## 和谁有关

- `SPMU_TASK`（raw: `02.07.04.01.234_SPMU_TASK.md`）— **宿主对象，本篇唯一明说的关系**。
  原文：`The SPMU_PIN_TASK object can only be accessed via the SPMU_TASK.pin() function of the
  SPMU_TASK class.` —— **这就是「包含关系」在语料里的原话**：本类是 `SPMU_TASK` 的 per-pin 数据面，
  `SPMU_TASK` 是执行面。**本页没读那一篇**，所以 `SPMU_TASK` 自己有哪些成员、怎么执行，
  本页一个字都没有。
- `SPMU_TASK.pin()`（raw: `02.07.04.01.234.07_SPMU_TASK.pin.md`）— **唯一入口那一条链接的目标**。
  **本页没读它**，所以 `pin()` 的参数（能不能给多个 pin？用逗号？）本页答不出。
- [[spmu-pin-task-mode]] — **38 个成员里唯一在本 wiki 里有独立页的那一个**（`SPMU_PIN_TASK.mode()`）。
  例子里 `mode("VM_HIZ")` / `mode("VFIM")` 就是它。**本篇没有链接到它**，
  **本页正文也没有它的任何事实**——「有哪些模式可选」在那一页。
- 另外 37 个成员文档（`SPMU_PIN_TASK.clamp()` … `SPMU_PIN_TASK.vSlewRate()`；
  raw 路径见本篇的 38 条 `Subtopics`）— **本页一篇没读**。
  本页列出的 38 个名字**只有名字**，**没有一个字的含义**。
- [[pattern-controller]] / [[pin-utility]] / [[dc-result-accessor]] — **Example 2 里出现的三个类**，
  三个名字在本 wiki 里都有页。**本篇只给了它们在例子里的调用**，
  **没有一句话解释它们**；**本页没读这三页**，所以这几条关联只到「例子用了它」为止。
- `PPMU_SETTING` / `PPMU_RELAY` / `BADC_SETTING` / `BADC_MEASURE` / `TM::RESULT_INDEX` /
  `TM::ALL_DIGITAL`（**本篇只在 Example 2 的代码里出现，没有链接、没有说明**）—
  本页**只列名，不解释**。
- **⚠️ `SPMU_PIN_TASK` / `SPMU_TASK` / `spmu-pin-task` / `spmu-task` / `dps-task` 都不在
  `extract/prose-allowlist.txt` 里**，所以本页**只能写反引号 + raw 路径，不能写 `[[ ]]`**（§9.1）。
  **这是清单的现状，不是本页的选择**（同 `wiki/mappings/mapping-testmethod.md` ⑩ 的处理）。

## 版本

**本篇有 `## Functional changes` 段，共 12 条**（逐字，`- ` 是原文的列表符）：

> 「- Introduced before SmarTest 6.3.2」
> 「- SmarTest 6.5.3: New SPMU_PIN_TASK.connect(), SPMU_PIN_TASK.disconnect()」
> 「- SmarTest 6.5.3: New SPMU_PIN_TASK.vForceRange(), SPMU_PIN_TASK.iForceRange(),」
> 「- SmarTest 6.5.3: New SPMU_PIN_TASK.iMeasureRange(), SPMU_PIN_TASK.vMeasureRange()」
> 「- SmarTest 7.3.1: New SPMU_PIN_TASK.connectState()」
> 「- SmarTest 7.3.1: New SPMU_PIN_TASK.iClampFilter(), SPMU_PIN_TASK.vForceFilter()」
> 「- SmarTest 7.4.0: New SPMU_PIN_TASK.iSlewRate(), SPMU_PIN_TASK.vSlewRate()」
> 「- SmarTest 7.4.0: New SPMU_PIN_TASK.refPin(), SPMU_PIN_TASK.measFilter()」
> 「- SmarTest 7.4.0: New SPMU_PIN_TASK.iFilter(), SPMU_PIN_TASK.vFilter()」
> 「- SmarTest 7.5.0: New SPMU_PIN_TASK.forceDropMax() and SPMU_PIN_TASK.returnDropMax()」
> 「- SmarTest 7.5.0: New SPMU_PIN_TASK.vCompliance()」
> 「- SmarTest 7.5.1: New SPMU_PIN_TASK.dcPower() and SPMU_PIN_TASK.pulseEnergy()」

**第一条是 §11.2 ② 的哨兵值**（`Introduced before SmarTest 6.3.2` = 「早于语料覆盖范围」），
**不是「6.3.2 新增了本类」**。**其余 11 条都带 `New`**。

**按版本归并**（本页的整理，不是原文的分节）：

| 版本 | 新增了什么 |
|---|---|
| 6.5.3 | `connect()` / `disconnect()`；`vForceRange()` / `iForceRange()`；`iMeasureRange()` / `vMeasureRange()` |
| 7.3.1 | `connectState()`；`iClampFilter()` / `vForceFilter()` |
| 7.4.0 | `iSlewRate()` / `vSlewRate()`；`refPin()` / `measFilter()`；`iFilter()` / `vFilter()` |
| 7.5.0 | `forceDropMax()` / `returnDropMax()`；`vCompliance()` |
| 7.5.1 | `dcPower()` / `pulseEnergy()` |

**两条与 `Subtopics` 对不上的地方（本页核过，见 `## 出处` ②）：**
**版本段点名的 `refPin()`、`vCompliance()`、`dcPower()`、`pulseEnergy()` 四个成员，
在 `Subtopics` 那 38 条里一个都没有**。

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，本篇最后一条版本是 **7.5.1**——
**7.5.1 到 7.10.3 之间，本篇没有记过本类的任何变更**（**「没记」≠「没变」**）。

## 出处

`sources:` **一篇**：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md`
（TDC `55669.htm`，8,730 字节，198 行）。**整篇读完**（199 行全读）。

**本页没做的：**

- **`## 语法 / 参数` 节一个字没改**（§4）。里面 `### Example 1` / `### Example 2` 两段的层级、
  以及语料内部链接的改写（`SPMU_TASK`（raw: `02.07.04.01.234_SPMU_TASK.md`）那处）
  **都是 `extract/objscaffold.py` 干的，本页只读不改。**
- **38 个成员文档一篇没读**（`Subtopics` 的 38 条链接）。**这是本页最大的空缺**：
  本页有 38 个名字、有 2 个例子的调用顺序，**但没有一个成员的含义、取值、单位、默认值、报错**。
- **`SPMU_TASK` 与 `SPMU_TASK.pin()` 两篇没读**。所以
  「`SPMU_TASK` 怎么建、`pin()` 能不能一次给多个 pin、多个 pin 会不会合并测量」**本页答不出**。
- **Example 2 里那五个类没读**：`PATTERN_CONTROLLER`、`DC_RESULT_ACCESSOR`、`PPMU_SETTING`、
  `PPMU_RELAY`、`BADC_SETTING` / `BADC_MEASURE`，以及 `PinUtility` 与 `TM::RESULT_INDEX` /
  `TM::ALL_DIGITAL` 两个枚举值。**本页只列名字与调用位置。**
- **`## Related information` 一节本篇没有**（`SPMU_TASK` 那一篇有、本篇没有），
  所以「相关文档」这件事本页**只能从 `Subtopics` 与两个例子里读**。
- **一张图都没有。** 本篇 raw 里 `![` / `.png` / `.jpg` **命中 0**（我数过），
  **上游 `raw/55669.htm` 里 `<img>` 也是 0 个**。**所以本页没有任何来自图的结论**——
  **这不是「图够不着」，是这一篇没有图**（§11.4 ①）。
- **没有实跑**：没有在机台上跑过 `VM_HIZ`，没有接过 BADC，没有注册过 `PATTERN_CONTROLLER` 的 label。
  `verified: doc-only` 指的是这件事；**`Action` 里的每一条照文档抄，动手前先看现场。**

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改：**

> **① 版本段第三条以逗号结尾，像是少了一个成员。** 逐字：
> `- SmarTest 6.5.3: New SPMU_PIN_TASK.vForceRange(), SPMU_PIN_TASK.iForceRange(),`
> ——**`iForceRange(),` 后面那个逗号**在 12 条里**只此一处**，
> 读起来像「还有第三个名字被截掉了」。**本页照原样引，不替它补、也不替它删。**

> **② 版本段点名的四个成员不在 `Subtopics` 里。** 本页逐条核过：
> `refPin()`、`vCompliance()`、`dcPower()`、`pulseEnergy()` **只出现在 `## Functional changes`**，
> 在 38 条 `Subtopics` 里**一条都没有**。
> **同一篇文档的两节互相不认账**——**本页两处并列，不判哪个对、也不替它补链接。**

> **③ 两节被压进一行。** 逐字：
> `List of parameters There are no parameters. Return value There is no return value.`
> ——`List of parameters` / `Return value` **都没有段标记**（裸词行），
> **所以脚本只能当正文收进语法节**（同 `SPMU_PIN_TASK.mode()` 那一页的 ⑩）。

> **④ `#### Subtopics` 是 h4，比正文的 `##` 还低一级**，而它列的 38 条**是这一篇最重要的内容**
> （成员清单）。**层级与内容的权重不符**——本页把这份清单提到 `## 是什么` 里重排了一次。

> **⑤ 这一篇的 3,588 字语法节里没有签名。** 因为**本篇根本没有 `## Syntax` 段**
> （它的结构是 `#### Subtopics` → `## Class definition` → `## Examples` → `## Functional changes`），
> 而**本类没有 public 构造函数**，也就没有「语法」可抽。
> **所以本页语法节里的两个例子，就是这一篇全部可抽的内容**——**这不是脚本漏抽。**

> **⑥ 本篇没有 §11.2 ① 那种编码坏字，也没有 §11.2 ⑤ 那种整词替换。** 两条都实测过：
> 汉字 `[一-鿿]` **0 行命中**；`DC/DC power units` **0 命中**。

`verified: doc-only`
