---
type: object
title: DPS_TASK
layer: L2
stage: testmethod
tags: [testmethod, dc-test, dps, task-handle, per-pin, samples, trigger, offline-emulation, ganging, dc-scale]
related: [dps-aux-task, dps-aux-pin-task, dc-test-programming, offline-result-emulation, ganging, pin, xps256-programming-dps-operating-mode, dps128-dps64-cards, dc-scale-uhc4t-card, dc-scale-xps256-card]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50_DPS_TASK.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# DPS_TASK

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,048 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50_DPS_TASK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### DPS per-pin value measurement

```
DPS_TASK dpsTask;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Setup the measurement
    //
    CONNECT();

    dpsTask.pin("Vcc").min(0 A).max(0.1 A);
    dpsTask.pin("Vee").min(0 A).max(0.2 A);
    dpsTask.wait(5 ms); //available in SW6.3.3
    dpsTask.execMode(TM::PVAL);
    dpsTask.trigMode(TM::INTERNAL);

    //
    // Execute the measurement
    //
    FUNCTIONAL_TEST();

    dpsTask.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and datalog
//
double IMeas1, IMeas2;

IMeas1 = dpsTask.getValue("Vcc");
IMeas2 = dpsTask.getValue("Vee");

TEST("Vcc,Vee", "Idd_Test", dpsTask.getPassFail()?TM::Pass:TM::Fail, true);
```

In this example, a DPS per-pin value measurement is performed on the pin "Vcc" and "Vee". The measured current values are retrieved. The pass/fail result is judged and logged.

### DPS measurement with different settings for different sites

```
DPS_TASK dpsTask;

ON_FIRST_INVOCATION_BEGIN();

    CONNECT();

    //
    // Dummy initialization of a testflow variable
    //
    FOR_EACH_SITE_BEGIN();

        SET_USER_FLAG("DPS_DUMMY_VAR", CURRENT_SITE_NUMBER());

    FOR_EACH_SITE_END();

    dpsTask.pin("Vcc").min(0 A).max(0.1 A);

    dpsTask.execMode(TM::GPF);

    dpsTask.trigMode(TM::INTERNAL);

    //
    // The task will be changed.
    //
    dpsTask.setup();

    FOR_EACH_SITE_BEGIN();

        INT current;

        GET_USER_FLAG("DPS_DUMMY_VAR",&current);

        dpsTask.pin("Vcc").max(current A);

    FOR_EACH_SITE_END();

    dpsTask.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and datalog
//
TEST( "Vcc", "multiDeltaDps", dpsTask.getPassFail()?TM::Pass:TM::Fail, true);
```

In this example, different settings are defined for different sites through the user flag "DPS_DUMMY_VAR". Then a global pass/fail measurement is performed on all the sites in parallel. The measurement result is retrieved and logged.

### DPS measurement with external trigger

```
DPS_TASK     dpsTask;
ARRAY_D      valueArrayVcc, valueArrayVdd;
INT          i;
static       LIMIT limit;
MULTI_LIMITS templ;

ON_FIRST_INVOCATION_BEGIN();

    CONNECT();

    //
    // Create a Limit for each measurement
    //
    limit.unit("A");
    limit.low(TM::GE, -4 uA);
    limit.high(TM::LE, 175 uA);
    templ.add(limit,8);

    //
    // Make sure that your pattern issues 8 triggers,
    // otherwise you will get an error message
    //
    dpsTask.pin("Vcc").limits(templ);
    dpsTask.trigMode(TM::EXTERNAL).execMode(TM::PVAL);

    //
    // Execute the primary pattern
    //
    dpsTask.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and datalog
//
valueArrayVcc = dpsTask.getWaveform("Vcc");

for ( i = 0 ; i < valueArrayVdd.size(); i++ )
{
    TEST("Vcc", "extTrigDps", limit, valueArrayVcc[i], TRUE);
}
```

In this example, a DPS per-pin value test is performed on the pin "Vcc". The test is triggered by an external digital pin. Eight times of measurements are performed. Each measurement result is retrieved, judged and logged.

<!-- 语法节 end -->

## 是什么

**`DPS_TASK` 是 DPS 通道（或 DPS 工作模式下的 DC Scale 卡）的「任务句柄」**：
一个对象代表一批并行跑的 DC 测量，条件按 pin 挂上去，统一执行、统一取结果。
本篇第一句逐字：

> 「The DPS_TASK API enables you to set up and execute measurements and to retrieve the measured
> value for DPS channels or DC Scale cards in DPS operating mode.」

**它自己列的「Supported tasks」四条**（逐字）：

> 「- Define measurement conditions for each DPS」
> 「- Execute, in parallel, the measurements defined with this class」
> 「- Retrieve measurement results」
> 「- Support triggered and un-triggered DPS measurement」

**「in parallel」是这一族的共同点，`DPS_TASK` 与 `SPMU_TASK` 都这么写**——
但**本页只讲 `DPS_TASK`**，`SPMU_TASK` 那一篇不在本页 sources 里
（raw: `02.07.04.01.234_SPMU_TASK.md`），**本页没读它**。

### 它可以被塞进 `TASK_LIST`，这是与其他 DC 测量混跑的路子

> 「This class can be added to TASK_LIST, so all kinds of DC measurement (using PPMU, DPS and DC
> Scale pins) can be seamlessly executed.」

**并且 `execute()` 与 `setup()` 两节各写了一遍「如果本类被加进 `TASK_LIST`，
由 `TASK_LIST` 的同名成员函数来调我」**（引文见下面成员表）——
**这是本篇里「组合」这件事唯一的机制说明**。`TASK_LIST` 自己那一篇不在本页 sources 里
（raw: `02.07.04.01.240_TASK_LIST.md`），**本页没读它**。

### 头文件与构造

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/DpsTask.h.」

> 「This constructs an object of the DPS_TASK class that allows the user to define different
> measurement conditions for each DPS, to execute all the measurements in parallel, and to
> retrieve the results.」

> 「Do not create static objects of the class in the test method and do not create test method
> member variables from this class.」

**两条硬事实**：构造函数**无参数**；**不能建静态对象、不能建 test method 成员变量**。

### ⚠️ 一条硬顺序：`pin()` 之后不能再调 `DPS_TASK` 的成员

这是本篇**唯一一条明写的调用顺序约束**，逐字：

> 「A call to this function must be followed by calls to member functions of DPS_PIN_TASK class.
> You cannot call another DPS_TASK member function after calling pin().」

| 条件 | 结果 |
|---|---|
| 调了 `pin()` | **接下来只能调 `DPS_PIN_TASK` 的成员**（`.min()` / `.max()` / `.limits()` …） |
| 在 `pin()` 之后又调 `DPS_TASK` 的成员 | **原文说「不能」（`You cannot`）**——报什么错、是编译错还是运行错，**本篇没说** |

**所以「配一个 pin」的写法必然是「`pin(...)` 起头、把 per-pin 的都跟完」**；
要配下一个 pin 就再起一条 `pin(...)` 语句——**三个例子都是这个写法**（见 `## 典型用法`）。

### 17 个成员函数：配置类返回 `DPS_TASK &`，执行/取结果类返回别的

**下面这些签名不在本页语法节里**——脚本抽到语法节的是本篇的 `## Examples`（见 `## 出处` ⑤）。
**这一节是本页从原文 `## Member functions` 段转写的**，签名逐字取自原文。

| 成员 | 签名（逐字） | 本篇给的说明 |
|---|---|---|
| `pin()` | `DPS_PIN_TASK & pin(const STRING & pinlist);` | 「返回 `DPS_PIN_TASK` 类对象的引用」；**`pinlist` 可以用逗号给多个 pin** |
| `execMode()` | `DPS_TASK & execMode(const TM::DCTEST_MODE mode);` / `DPS_TASK & execMode(const STRING & mode);` | 「选择执行模式」，四档见下表 |
| `preAction()` | `DPS_TASK & preAction(const STRING & action);` | 「定义 DC 测量前要做的动作」，三档见下表 |
| `primaryActivation()` | `void DPS_TASK::primaryActivation(Boolean primaryActivation);` | 指定这次 DPS 测量**要不要激活 primaries** |
| `samples()` | `DPS_TASK & samples(size_t samples);` | **测量次数**，之后**取平均**；默认 1 |
| `setup()` | `void setup();` | 「把条件下载到 firmware 层」——**但 `execute()` 之前不落到卡上** |
| `trigMode()` | `DPS_TASK & trigMode(TM::TrigMode trig_mode);` | 内部触发 / 外部触发；默认 `TM::INTERNAL` |
| `wait()` | `DPS_TASK & wait(DOUBLE waitTime_s);` | 测量**前**的等待时间（秒） |
| `execute()` | `void execute();`（另有 2 个离线仿真重载，见下） | 先按需 `setup()`，再跑 DC 参数测试 |
| `measRangeMode()` | `DPS_TASK & measRangeMode(const TM::DPS_MEAS_RANGE_MODE& rangeMode);` | **「不再支持、静默忽略」——但同一节又叫你用它**，见下 |
| `getFunctionalResult()` | `Boolean getFunctionalResult() const;` / `Boolean getFunctionalResult(const STRING & pinlist) const;` | 取**功能预测试**的 P/F；**没跑过就报错** |
| `getNumberOfUsedChannelsFromLastMeasurement()` | `INT getNumberOfUsedChannelsFromLastMeasurement(const STRING & pin) const;` | 只在 `DPS_PIN_TASK.measurementMode()` 为 **`TM::MEASURE_CURRENT_UNGANGED`** 时有意义 |
| `getPassFail()` | `Boolean getPassFail() const;` / `Boolean getPassFail(const STRING & pinlist) const;` | 全局 / per-pin 的 P/F |
| `getValue()` | `DOUBLE getValue(const STRING & pin) const;` | 一个 pin 的值，**单位 [A] / [V]**；**非 `PVAL` 模式就报错** |
| `getValues()` | `const ARRAY_D getValues(const STRING & pin) const;` | **ganged 通道的全部通道值**，**按 gang 定义顺序**返回 |
| `getVbump()` | `DOUBLE getVbump(const STRING &pin);` | 指定 pin 的 **voltage bump** 值 |
| `getWaveform()` | `const ARRAY_D getWaveform(const STRING & pin) const;` / `const ARRAY_D getWaveform(const STRING & pin, INT channelIndex) const;` | **外部触发模式**下的一串测量值；第二个版本取 ganging 组里**指定通道序号** |

**归类看一眼就清楚**：**能链式的一律返回 `DPS_TASK &`**（`pin` / `execMode` / `preAction` /
`samples` / `trigMode` / `wait` / `measRangeMode`），**执行与取结果的返回 `void` / `Boolean` /
`DOUBLE` / `ARRAY_D`**。**`primaryActivation()` 是唯一的例外**——它返回 `void`，
**而且签名里带类名 `DPS_TASK::`，17 个成员里只此一处**（见 `## 出处` ④）。

### 四档执行模式：决定了「能取到什么结果」

| `execMode` | 字符串 | 原文说明 | 能取什么 |
|---|---|---|---|
| `TM::GPF` | `"GPF"` | 全局 pass/fail；**所有测量都过才算过** | `getPassFail()`。**这是默认值** |
| `TM:PPF` | `"PPF"` | per-pin pass/fail | `getPassFail(pinlist)`；**同时也能取全局** `getPassFail()` |
| `TM::PVAL` | `"PVAL"` | per-pin **值**测量 | `getValue(pin)`；**同时也能取全局与 per-pin 的 P/F** |
| `TM::DCTEST_AUTO` | `"DCTEST_AUTO"` | **按 test suite 的 flag 决定** | 见下面那张 flag 表 |

`TM::DCTEST_AUTO` 的三条判定（逐字的 flag 名）：

| test suite flag | 等效于 |
|---|---|
| `Pass value` 或 `Fail value` **on** | **`TM::PVAL`** |
| 上面两个都 off，且 `Per pin on pass` 或 `Per pin on fail` **on** | **`TM::PPF`** |
| 四个 flag **全 off** | **`TM::GPF`** |

**⚠️ 表里第二个模式的枚举写法是 `TM:PPF`（少一个冒号）**，同表的另外三档都是 `TM::`。
**本页照原样引，不替它改**（见 `## 出处` ②）。

### 三档 `preAction`：测量前要不要先跑一次 functional test

| `action` | 原文说明 | 能不能取到功能结果 |
|---|---|---|
| `"NONE"`（**默认**） | 内部触发模式下不做前置动作，**但 Testsuite dialog 里指定的 digital primaries 会被激活** | 外部触发模式下**它等同于 `"FTST"`** |
| `"FTST"` | 测量前跑一次 functional test（激活 digital primaries）；**用于「施加 primary set 里定义的 break vector 后再测」** | **可以**，用 `getFunctionalResult()` 取 |
| `"FTST_NO_RESULT"` | 跑 functional test **但不上传结果**；用于「只想用 preconditioning pattern 把 device 推到某个状态、不关心结果」 | 不上传 |

**两条容易被读漏的**：

- **外部触发模式下 `"NONE"` 就是 `"FTST"`**——逐字：`"NONE" is the same as "FTST" in the
  external trigger measurement mode.` **所以外部触发时你一定会跑一次 functional test**，
  不管你有没有写 `preAction`。
- **`"FTST"` / `"NONE"` 两档都带同一句**：`To activate the primaries specified with the
  PRIMARY_STATUS API or primary analog set, put the FLUSH API prior to this statement.`
  ——**要用 `PRIMARY_STATUS` 或 primary analog set 指定的 primaries，必须在这条语句前面放 `FLUSH`**
  （[[flush]] / [[primary-status]] 两页在 wiki 里都有；**本页没读它们**）。

### ⚠️ `measRangeMode()`：同一节里自己和自己矛盾

这是本篇最该记的一处。同一个成员函数的说明分三段，**三段的说法不一致**：

| 位置 | 逐字 | 读起来的意思 |
|---|---|---|
| 开头 | `This member function selects the measurement range mode. It is no longer supported and silently ignored.` | **不再支持、静默忽略** |
| 紧跟的 `Note` | `The regulation performance of the DPS is negatively affected by the current sense resistor. So after a low current measurement, use this function to restore the current measurement range to the highest possible range.` | **叫你用这个函数**去把量程恢复到最大 |
| 参数表末 | `For DPS128 and XPS256, the function is silently ignored and the measurement range is restored to the force or clamp range.` | **在两张卡上被忽略**，量程改为恢复到 force / clamp 量程 |

**同一段里既有「不再支持」又有「用它来恢复量程」。本页三处并列，不替它调和、也不判哪个对。**
参数本身给了两档（`TM::KEEP_RANGE` 默认 / `TM::RESTORE_RANGE` 恢复到 `1,5A`）——
**既然被静默忽略，这两档在 7.10 上还有没有作用，本篇没说。**

### 电流量程不会自己恢复：`execute()` 那条 `Note` 的工程后果

> 「The current range defined by the DPS_PIN_TASK minimum and maximum values remains after the
> DPS_TASK execute() member function is called. The regulation performance of the DPS is
> negatively affected by the current sense resistor and therefore the current measurement range
> should be restored to the highest possible range after a low current measurement. To reset the
> current range to the highest possible range, you must program the DPS_PIN_TASK minimum and
> maximum values accordingly and then call the DPS_TASK execute() member function again.」

**落成动作**：**测过小电流之后，量程会停在小的那一档**（因为 `DPS_PIN_TASK` 的 `min` / `max`
留下的就是那一档）；**要恢复就把 `DPS_PIN_TASK` 的 min/max 改成大档、再调一次 `execute()`**。
**注意这里和上面 `measRangeMode()` 的 `Note` 互相矛盾**：一条说用 `measRangeMode()` 恢复，
一条说用 `min`/`max` + 再 `execute()` 恢复。**本页两处并列，不调和。**

### `setup()` 与 `execute()`：谁把条件落到硬件上

| 函数 | 原文 | 后果 |
|---|---|---|
| `setup()` | `This function downloads the measurement conditions defined in DPS_TASK and DPS_PIN_TASK into the firmware layer, but they will not be applied to the test card hardware until the execute() member is called.` | **只下载，不上卡** |
| `execute()` | `This function calls the setup() member function if the measurement conditions have not downloaded to the firmware layer yet.` | **没下过就自己下**；**下过就不再下**——这正是第二个例子里「先 `setup()` 改条件、后 `execute()`」能成立的原因 |

**`execute()` 还给了两件事**：`When executing the test method, the primaries will be applied.`
（**执行时会施加 primaries**）；如果本类在 `TASK_LIST` 里，**由 `TASK_LIST::execute()` 来调它**。

### 离线结果仿真：`execute()` 多一个重载

> 「The execute() method of the DPS_TASK class takes a measurement name as additional parameter.
> The name is required to refer to the corresponding offline measurement result specified in the
> setup file.」

原文给了两种签名（逐字）：`virtual void execute(FwStream* = NULL)` 是「原有的执行方法」，
`virtual void execute(const string& measurementName)` 是带名字的那个；
参数表说 `measurementName` 的作用是 `Associate the measurement with offline data.`。
**细节在 `Parametric offline result emulation` 那一篇里**（本篇 `execute()` 一节链过去的），
**本页没读它**——那一族在本 wiki 里有 [[offline-result-emulation]] 一页。

### 触发、采样与等待：三件与「测几次」有关的事

- **`trigMode()`**：`TM::INTERNAL`（**默认**）内部触发；`TM::EXTERNAL` 外部触发，
  **`In this mode, the measurement continues as long as a trigger is sent to the DPS.`**
  外部触发模式**同样会强制先跑一次 functional test**，并且**可以用 `MULTI_LIMITS` API
  给目标 pin 定义多组电流/电压限值**。
- **`samples()`**：`This function specifies the number of measurements. An external DPS measurement
  triggers the pattern for every measurement. After the measurements, the average of the measured
  values will be calculated.` **默认 1**；**取的是平均值**。
  **⚠️ 你要的次数不一定是你得到的次数**——原文：`The real sample number of the measurement may
  not be the specified samples.` 按卡分三张表：

| 卡 | 项目 | 真实采样数 |
|---|---|---|
| **DPS128-HC / DPS64-HC** | 7 V 电压测量 | 4 与指定值**取大** |
| | 12.5µA – 250µA 电流 | 64 与指定值**取大** |
| | 1.25mA – 200mA 电流 | 16 与指定值**取大** |
| | 1A 电流 | 8 与指定值**取大** |
| **UHC4T** | 4 V 电压测量 | 8 与指定值**取大** |
| | 2mA 电流 | 256 与指定值**取大** |
| | ≥ 50mA 的量程 | 64 与指定值**取大** |
| **XPS256** | — | **就是指定的次数**（不打折） |

**上限**：DPS128 / DPS64 = **8192**；UHC4T = **16384**；XPS256 = **262144**。
**取整规则**：DPS128 / DPS64 与 UHC4T 上，真实采样数**不是 2 的幂就向上取到下一个 2 的幂**；
**XPS256 上 1 到上限之间任意值都可以**。
（上面三张表里的 `12.5µA` / `250µA` 在原 raw 里是**编码坏字**，见 `## 出处` ①。）
- **`wait()`**：测量**前**的等待时间（秒）；原文区分了静态与动态：
  `For static DPS measurement, internal settling time exists. But additional settling time may be
  needed because of load board design or large capacitor used. For dynamic DPS measurement, no
  internal settling time exists because it runs together with digital channels. You need to take
  care of the settling time within the pattern.`

### 取结果：每个函数都有前置条件，不满足就报错

| 取什么 | 函数 | 前置条件（原文） | 不满足 |
|---|---|---|---|
| 一个 pin 的值 | `getValue(pin)` | `if the appropriate measurement mode (PVAL) is specified` | `If not, an error occurs.` |
| 一串值（外部触发） | `getWaveform(pin)` | 同样要求 `PVAL` | `If not, an error occurs.` |
| 功能预测试的 P/F | `getFunctionalResult()` / `(pinlist)` | `if the functional pre-test ("FTST" or external trigger measurement) was executed` | `If not, an error occurs.` |
| 全局 / per-pin P/F | `getPassFail()` / `(pinlist)` | 本篇没写前置条件 | — |
| ganged 通道的各通道值 | `getValues(pin)` | 本篇没写前置条件；**返回顺序 = gang 定义顺序** | — |
| 用了几个通道 | `getNumberOfUsedChannelsFromLastMeasurement(pin)` | 只在 `measurementMode()` 为 `TM::MEASURE_CURRENT_UNGANGED` 时有意义 | 本篇没写 |

## 典型用法

**本篇有 `## Examples` 三段，没有 `## Procedure`、没有 `## Before you begin`。**
三段各自解决一个场景：

| 例子 | 场景 | 执行方式 | 取结果 |
|---|---|---|---|
| `DPS per-pin value measurement` | 两个静态 pin 的电流测量（`Vcc` / `Vee`） | `CONNECT()` → 配 pin → `FUNCTIONAL_TEST()` → `execute()` | `getValue()` ×2 |
| `DPS measurement with different settings for different sites` | **逐 site 给不同条件**（经 user flag） | 配 → `setup()` → 逐 site 改条件 → `execute()` | `getPassFail()` |
| `DPS measurement with external trigger` | **外部触发、8 次测量** | `CONNECT()` → `limits(templ)` → `trigMode(TM::EXTERNAL).execMode(TM::PVAL)` → `execute()` | `getWaveform()` → 逐点 `TEST()` |

**三段合起来能读出的通用顺序**（每一步都有代码作依据）：

1. `DPS_TASK dpsTask;`（块外）
2. `ON_FIRST_INVOCATION_BEGIN();`
3. **`CONNECT();`**——三段例子里**都有这一句，而且都在最前面**（第一段还带注释 `// Setup the measurement`）
4. 配 pin：`dpsTask.pin("Vcc").min(0 A).max(0.1 A);` —— **`pin()` 起头、per-pin 的跟完**
5. 配执行：`execMode(...)` / `trigMode(...)` / `wait(...)`
6. **`setup()`（可选）→ `execute()`**（第二段先 `setup()` 再逐 site 改条件再 `execute()`）
7. `ON_FIRST_INVOCATION_END();`
8. **块外**取结果：`getValue()` / `getPassFail()` / `getWaveform()`
9. **判定与写日志交给 `TEST`**——三段例子最后都有一句 `TEST(...)`
   （`TEST("Vcc,Vee", "Idd_Test", dpsTask.getPassFail()?TM::Pass:TM::Fail, true);`）

**三条只在例子里出现的实事**：

- **`wait(5 ms)` 旁边挂着版本注释**：`dpsTask.wait(5 ms); //available in SW6.3.3` ——
  **这一句注释就是本篇「`wait()` 对哪个版本可用」的唯一出处**（版本段也记了 6.3.3）。
- **外部触发的次数由 pattern 决定**，逐字注释：
  `// Make sure that your pattern issues 8 triggers,` + `// otherwise you will get an error message`
  ——**pattern 发几个 trigger 就必须测几次，否则报错**。
- **逐 site 改条件的那一段靠 `FOR_EACH_SITE_BEGIN()` / `SET_USER_FLAG()` / `GET_USER_FLAG()`**，
  并且**在改条件之前先调了一次 `setup()`**，注释逐字 `// The task will be changed.`。

**⚠️ 照抄第三段例子会踩的坑**（**例子的代码自身有错**，见 `## 出处` ③）：

```
valueArrayVcc = dpsTask.getWaveform("Vcc");

for ( i = 0 ; i < valueArrayVdd.size(); i++ )
{
    TEST("Vcc", "extTrigDps", limit, valueArrayVcc[i], TRUE);
}
```

`valueArrayVdd` 在例子开头声明了（`ARRAY_D valueArrayVcc, valueArrayVdd;`）**但从未赋值**，
而循环上界用的是 `valueArrayVdd.size()`、下标用的是 `valueArrayVcc[i]`。
**本页照原样引，不替它改**；照抄这段代码会拿到一个空的循环上界。

## 和谁有关

- `DPS_PIN_TASK`（raw: `02.07.04.01.50.01_DPS_PIN_TASK.md`）— **per-pin 条件容器，本篇唯一的 `## Related information` 链接**。
  `pin()` 的返回值就是它；三个例子里的 `min()` / `max()` / `limits()` / `measurementMode()` 都是它的成员。
  **本篇给了它与本类的分工**（`pin()` 之后不能再调 `DPS_TASK` 的成员），
  **但它自己有哪些成员、分别怎么用，本页没有**——**本页没读它**。
- `TASK_LIST`（raw: `02.07.04.01.240_TASK_LIST.md`）— **把多个 DC 测量串起来跑的组合器**。
  本篇**两处**写了「加进 `TASK_LIST` 后由它来调 `setup()` / `execute()`」，
  正文开头还说了加进去之后「PPMU / DPS / DC Scale 三种 pin 的 DC 测量可以无缝混跑」。
  **本页没读它。**
- [[offline-result-emulation]] — **离线结果仿真的入口页**。
  本篇 `execute()` 一节把读者指到 `Parametric offline result emulation` 与 `Offline Result Emulation` 两篇，
  **本页没读那两篇**，所以「`measurementName` 怎么写、setup 文件里怎么配」本页答不出。
- [[dc-test-programming]] — **（推断）上游的编程入口**。
  依据：本页讲的是「一个任务句柄怎么配、怎么跑」，而 wiki 里 DC 测试编程的整篇是那页；
  **本篇没有链接到它**，**本页没有它的事实**。
- [[ganging]] / [[pin]] — **（推断）两项前提概念**。
  依据：`getValues()` 与 `getWaveform(pin, channelIndex)` 的说明里反复出现
  `ganged channels` / `ganging group` / `gang definition`，而这两个概念在 wiki 里各有专页。
  **本篇没有链接到它们**，**本页没有它们的定义**。
- **被点名的卡**：本篇正文与版本段出现了 **DPS128 / DPS64 / DPS128-HC / DPS64-HC / UHC4T / XPS256 /
  PVI8 / AVI64 / FVI16** 九个名字。wiki 里有页的是
  [[dps128-dps64-cards]]、[[dc-scale-uhc4t-card]]、[[dc-scale-xps256-card]]
  与 [[xps256-programming-dps-operating-mode]]——**（推断）：按卡名对上的，本篇一个链接都没给。**
  **PVI8 / AVI64 / FVI16 在 wiki 里没有对应的卡页**（本页查过 `wiki/` 的页名）。
- `DPS_VFIM` / `DPS_PIN_TASK` / `TM::DCTEST_MODE` / `TM::TrigMode` / `TM::DPS_MEAS_RANGE_MODE` /
  `MULTI_LIMITS` / `PRIMARY_STATUS` / `FLUSH` / `ARRAY_D` / `TM::Pass` / `TM::Fail`（**本篇只提到名字**）—
  其中 `PRIMARY_STATUS` → [[primary-status]]、`FLUSH` → [[flush]] **在 wiki 里有页**
  （**（推断）：按名字对上**）；**本页没读它们**。
- [[dps-aux-task]] / [[dps-aux-pin-task]] / [[dps-power-flags-get-functions]] / [[dps-pins-editor]] —
  **（推断）同族的邻近页**。依据只有「同一个 `DPS` 前缀 + 同一批 DC Scale 文档」。
  **本篇一句话都没提到它们，本页也没有它们的事实**——列在这里只是为了说明**这一族不止本页**。
- **⚠️ `DPS_TASK` / `DPS_PIN_TASK` / `TASK_LIST` / `dps-task` / `dps-pin-task` / `spmu-task`
  都不在 `extract/prose-allowlist.txt` 里**，所以本页**只能写反引号 + raw 路径，不能写 `[[ ]]`**（§9.1）。
  **这是清单的现状，不是本页的选择**（同 `wiki/mappings/mapping-testmethod.md` ⑩）。

## 版本

**本篇有 `## Functional changes` 段，共 11 条**（逐字）：

> 「- Introduced before SmarTest 6.3.2」
> 「- SmarTest 6.3.3: New member function wait().」
> 「- SmarTest 6.3.3: New member function: measRangeMode(), (introduced with 6.1.5.0 and 6.3.3.).」
> 「- SmarTest 6.5.3: New member function getVbump().」
> 「- SmarTest 7.0.4: New member function primaryActivation().」
> 「- SmarTest 7.1.3: Offline result emulation introduced.」
> 「- SmarTest 7.2.1: samples() values for DPS128/64 added.」
> 「- SmarTest 7.3.1: samples() values for PVI8 added.」
> 「- SmarTest 7.4.0: samples() values for AVI64 added.」
> 「- SmarTest 7.5.0: samples() values for FVI16 added.」
> 「- SmarTest 7.5.3: New member function getNumberOfUsedChannelsFromLastMeasurement().」

**第一条是 §11.2 ② 的哨兵值**（`Introduced before SmarTest 6.3.2` = 「早于语料覆盖范围」），
**不是「6.3.2 新增了本类」**。其余 10 条都带 `New` / 明确动作。

**两处与正文对不上的地方（本页核过，都在 `## 出处` 里记了）：**

| 版本段说 | 正文说 | 冲突点 |
|---|---|---|
| 7.2.1 / 7.3.1 / 7.4.0 / 7.5.0 分别给 **DPS128/64、PVI8、AVI64、FVI16** 加了 `samples()` 值 | `samples()` 一节的真实采样数表按 **DPS128-HC / DPS64-HC、UHC4T、XPS256** 分档 | **版本段点名的 PVI8 / AVI64 / FVI16 在正文表里一个都没有；正文表里的 UHC4T 与 XPS256 在版本段里没有一次专门的 `samples()` 条目** |
| 6.3.3 「`measRangeMode()` 新」 | 同一个函数的正文写「不再支持、静默忽略」，而紧跟的 `Note` 又叫你用它 | **版本段记它「新」，正文说它「废」** |

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，本篇最后一条版本是 **7.5.3**——
**7.5.3 到 7.10.3 之间，本篇没有记过本类的任何变更**（**「没记」≠「没变」**）。

## 出处

`sources:` **一篇**：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50_DPS_TASK.md`
（TDC `55630.htm`，13,227 字节，328 行——**本批五篇里最长的一篇**）。**整篇读完**（567 行全读）。

**本页没做的：**

- **`## 语法 / 参数` 节一个字没改**（§4）。里面三段例子的层级与链接改写
  **都是 `extract/objscaffold.py` 干的，本页只读不改。**
- **`DPS_PIN_TASK` 那一篇没读**（`02.07.04.01.50.01`）。**这是本页最大的空缺**：
  例子里 `min()` / `max()` / `limits()` / `measurementMode()` 全是它的成员，
  而**本页对它们的含义一个字都没有**——连「`min`/`max` 是限值还是量程」本页都不判
  （`measRangeMode()` 那节里原文自己一会儿说限值一会儿说量程）。
- **`TASK_LIST` 没读**，所以「多个任务串起来跑时执行顺序、错误传播」本页没有。
- **离线仿真的两篇没读**（`Parametric offline result emulation` 与 `Offline Result Emulation`），
  所以 `execute(measurementName)` 的 `measurementName` 从哪来、setup 文件怎么写，本页答不出。
- **没读 `PRIMARY_STATUS` / `FLUSH` / `primary analog set` / `MULTI_LIMITS` 的任何一篇**，
  所以「primaries 怎么指定、`FLUSH` 放前面为什么必要、`MULTI_LIMITS` 怎么建」本页一个字都没有。
- **九张被点名的卡一张没读**（DPS128 / DPS64 / DPS128-HC / DPS64-HC / UHC4T / XPS256 / PVI8 / AVI64 / FVI16）。
  正文的采样数与上限表**照文档转写**，**没有和卡自己的文档核对过**。
- **一张图都没有。** 本篇 raw 里 `![` / `.png` / `.jpg` **命中 0**（我数过），
  **上游 `raw/55630.htm` 里 `<img>` 也是 0 个**。**所以本页没有任何来自图的结论**——
  **这不是「图够不着」，是这一篇没有图**（§11.4 ①）。
- **没有实跑**：没有在 DPS 通道上跑过测量，没有跑过外部触发，没有用过离线仿真。
  **`samples()` 那三张「真实采样数」表本页照文档抄，动手前请在机台上验一次。**
  `verified: doc-only`。

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改：**

> **① 编码坏字一处。** 逐字：
> ` | Current Measurement  | 12.5碌A - 250碌A   | The maximum between 64 and the specified samples. |`
> ——**`碌` 应为 `µ`**（微安）。按 `extract/encoding-map.csv`，`碌`=µ 是**确定的映射**，
> 全语料 1,424 处。**上面这句引文照原样保留 `碌`，一处都没替它改**；
> **本页 `## 是什么` 的采样表里写的是解出来的 `12.5µA` / `250µA`**——
> **要回 raw 搜，得搜坏掉的那个形态（`12.5碌A`）。**

> **② `TM:PPF` 少一个冒号。** 逐字：`TM:PPF` / `"PPF"`——同一张表另外三档都是
> `TM::GPF` / `TM::PVAL` / `TM::DCTEST_AUTO`。**本页照原样引，不替它补冒号。**

> **③ 第三个例子的代码自身有错。** 逐字：
> `valueArrayVcc = dpsTask.getWaveform("Vcc");`
> `for ( i = 0 ; i < valueArrayVdd.size(); i++ )`
> ——**循环上界用了从未赋值的 `valueArrayVdd`，下标用的是 `valueArrayVcc[i]`**；
> 更前面那句 `static LIMIT limit;` 与 `MULTI_LIMITS templ` 也没对上
> （`dpsTask.pin("Vcc").limits(templ);` 给的是 8 组的 `templ`，
> 最后 `TEST(...)` 传的是单组的 `limit`）。**本页照原样引，一处都没替它改。**

> **④ `primaryActivation()` 的签名带类名。** 逐字：
> `void DPS_TASK::primaryActivation(Boolean primaryActivation);`
> ——17 个成员里**只有它带 `DPS_TASK::`**，别的都是裸函数名。**本页照原样引。**

> **⑤ 成员函数的「小标题」不是标题。** 原文里 `pin()` / `execMode()` / `setup()` …
> 这些名字是**带前导空格的裸词行**（例：` setup()`、` pin()`），而且**有的粘在上一段表格的末尾**
> （`samples()` 那一节最后就粘着 ` setup()`）。
> **所以本篇没有一处 `###` 级的成员小节**——脚本按段标记抽语法时，**只能抽到 `## Examples`**，
> 本页的语法节因此**只有三段例子、没有一个签名**。**这是原文的结构问题，不是脚本漏抽。**

> **⑥ `## Related information` 只有一个链接**（`DPS_PIN_TASK`），
> **没有分隔符问题**——本批五篇里只有这一篇的关联段是干净的。

> **⑦ `Note` 后面没有分隔符**，本篇多处，逐字开头如
> `Note A call to this function must be followed by calls …`、
> `Note The current range defined by the DPS_PIN_TASK minimum and maximum values remains …`、
> `Note The regulation performance of the DPS is negatively affected …`、
> `Note Do not create static objects of the class …`。

> **⑧ 数字写法不一致。** 同一篇里 `1,5A`（逗号当小数点，欧洲写法）与 `12.5碌A`、`0.1 A`
> 并存。**本页照原样引，不统一。**

> **⑨ 一处错字。** 逐字：`This option forcibly executes a functional test prior to the DC
> measurement, with activation of the curren digital primaries specified in the Testsuite dialog.`
> ——**`curren` 应为 `current`**。**本页正文照原样引。**

> **⑩ 本篇没有 §11.2 ⑤ 那种「整词替换」。** 实测：`DC/DC power units`（`Index` 被替换出来的那串）
> **0 命中**；`Index` / `index` 的命中只有 `channelIndex`、`labelIndex`、`Index of the label within
> the burst` 这些正当形态。**§11.2 ① 那种编码坏字只有 ① 那一处。**

`verified: doc-only`
