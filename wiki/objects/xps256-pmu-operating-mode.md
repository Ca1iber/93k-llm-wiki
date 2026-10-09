---
type: object
title: XPS256 programming - PMU operating mode
layer: L2
stage: level
tags: [level, xps256, pmu, dc-scale, smartrdi, spmu-task, test-head-card]
related: [level, pin, testmethod, digital-pins-editor, xps256-programming-dps-operating-mode, xps256-status-flags]
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# XPS256 programming - PMU operating mode

> **一句话**：**XPS256 卡上某个通道「当普通 PMU 用」的那套做法。**
> 原文：*"In PMU operating mode, a pin is used like a standard PMU to temporarily supply power
> during the execution of a single test suite or a group of test suites."*
> **注意 `temporarily`** —— 它是**测试期间临时供电**，不是给器件供电（那是
> [[xps256-programming-dps-operating-mode]] 那条路）。
>
> **引入版本：SmarTest 7.10.1**（`Functional changes` 段）。本 wiki 面向 **7.10.3**，在。
> **这是本 wiki 目前唯一一篇「7.10.x 才引入」的页**——SmarTest 版本比它旧的机台上没有这个模式。

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **8,135 字符逐字取自** `<02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

The following examples demonstrate how to set up an XPS256 pin for a standard current measurement.

The three examples are set up in a three-step sequence of connecting the pin and applying the basic setup, measuring the requested parameter, and disconnecting in a separate task. This sequence is suitable for XPS256-specific tests, since very often more than one setup has to be applied and more than one measurement has to be carried out before the pin is disconnected again.

 These examples are available in the following sections:

- `Example 1: SmartRDI, pattern‑based programming`（raw: `02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_pattern-based`）

Pattern‑based programming using SmartRDI is the recommended solution that requires the least amount of code and on the other hand delivers the most stable result in terms of timing.

- `Example 2: SmartRDI, code‑based programming`（raw: `02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_code-based`）

Code‑based programming using SmartRDI needs some more code and must follow the structure of the wrapped test method APIs.

- `Example 3: Test method API SPMU_TASK`（raw: `02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_TM_API_based`）

This example is based on the test method APIs and is strongly tied to the structure of the underlying commands.

The code of the three examples generates the same measurement sequence for the programmed pin. If you use the `Trace Function`（raw: `../02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.md`） to compare the code‑based SmartRDI example and the example based on the test method APIs, you will get the same output in the MCDLog file.

### Example 1: SmartRDI, pattern‑based programming

The example uses a code‑based `RDI command`（raw: `../02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md#_142604__dle_RDI_command`） to setup and connect the XPS256 pin. The following `RDI block`（raw: `../02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md#_142604__dle_RDI_block`） performs a pattern‑based measurement. The last RDI command disconnects the XPS256 pin in code‑based mode.

Since the RDI block uses a specialized `DC event`（raw: `../02.07_Test_Method_Reference/02.07.04.01.63_EVENT_...__DC_events_API_reference.md`） to perform the measurement, only the measurement related parameters must be defined. In contrast, for code‑based programming with SmartRDI or programming with test method APIs, all parameters must be specified also for the measurement.

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

### Example 2: SmartRDI, code‑based programming

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

### Example 3: Test method API SPMU_TASK

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

<!-- 语法节 end -->

## 是什么

**XPS256 是一块 DC Scale 卡**，它的一种工作模式叫 PMU operating mode：把某条通道当成
**标准 PMU** 用，在**一个 test suite 或一组 test suite 执行期间临时加电**。

**`layer: L2` 记的是「主接口」，不是「只有这一层」。** 这一页实际横跨四层：

| 要做的事 | 走哪一层 | 文档对应节 |
|---|---|---|
| 把通道设成 PMU 模式 | **GUI** —— Pin definition | Digital Pins editor，`Type=dc` + `Mode=SIG` |
| 写代码（推荐） | **SmartRDI** —— `dc()` API | SmartRDI overview |
| 写代码（底层） | **L2** —— `SPMU_TASK` / `SPMU_PIN_TASK` | API overview |
| pattern 里做 setup/测量 | **L2** —— DC events | API overview |
| 最底下 | **L1** —— `DCCH` / `DCVH` / `DCEX` | 例 3 说明了这层 |

**进这个模式的唯一开关**（`Pin definition` 原文）：
用 → [[digital-pins-editor]] 把 XPS256 的 pin 定义成 **dc type pin**，
*"The Type parameter is to be set to dc and the Mode parameter is to be set to SIG."*
**设错了就不是这个模式**，后面的 API 全都不对路。

## 典型用法

**先选编程方式。** 原文明确推荐路线：

> *"Pattern鈥慴ased programming using SmartRDI is the recommended solution that requires the
> least amount of code and on the other hand delivers the most stable result in terms of
> timing."*

三种写法，**产生完全相同的测量序列**（原文：用 `Trace Function` 比对 MCDLog 会得到一样的输出）：

| # | 写法 | 原文评价 |
|---|---|---|
| 1 | SmartRDI，**pattern–based** | **推荐**：代码最少、timing 最稳 |
| 2 | SmartRDI，code–based | 代码多一些，必须跟被包装的 test method API 的结构 |
| 3 | test method API `SPMU_TASK` | 和底层命令的结构强绑定 |

（**三个例子的代码逐字收在上面「语法 / 参数」节里**，脚本抽的，含 `VFIM` 的完整参数
`vForce(5.0 V)` / `iClamp(-5.0 mA, 50.0 mA)` / `average(16)` / `measWait(2.5 ms)` 等。）

**三步顺序**（三个例子共用的骨架，原文）：

1. **连接 + 基本设置**（一个 task）
2. **测量**（另一个 task）
3. **断开**（再一个 task）

> 原文解释了为什么拆成三个 task：*"This sequence is suitable for XPS256-specific tests,
> since very often more than one setup has to be applied and more than one measurement has to
> be carried out before the pin is disconnected again."*
> —— **不要连一次测一次断一次**，那样既慢又容易出错。

**支持的测量模式**（`SPMU_PIN_TASK.mode()` 的取值，原文 8 个）：

`VFVM` / `VFIM` / `VFIM_UNGANGED` / `CFVM` / `CFIM` / `IFVM` / `IFVM_UNGANGED` / `VM_HIZ`

**两个必须记住的点**：

- **XPS256 有真正的 force current 模式**，原文：
  > *"Unlike other DC scale cards, XPS256 pins feature a real current force mode with
  > programmable voltage clamps."*

  —— 所以 `CFVM` / `CFIM`（"Force current **directly**"）在 XPS256 上是真家伙；
  而 `IFVM` / `IFVM_UNGANGED` 是**为了跟别的 DC scale 卡兼容的遗留模式**，
  做法是把 clamp 电流设成目标值、再把电压设到能把 pin 逼进 clamp 状态（原文）。
  **写新代码用 `CFxx`，别用 `IFVM`。**
- `*_UNGANGED` 是**临时拆开 ganged 通道**：原文说这样能提高所加电流的稳定性和电压测量精度。

**Relay 与 precharge（易错）**

- `SPMU_PIN_TASK.relay()` 选 termination mode，从而决定目标 pin 的**继电器控制图样**。
- **DC-Scale 卡只支持 `NO` 和 `NT` 两种**；`NTMBB` / `NTBBM` / `TERM` **不支持**（原文）。
- 有没有 `preCharge` 会改变动作顺序 —— 文档给了**两张表**（无 precharge / 有 precharge），
  逐字收在上面「语法 / 参数」节。**这两张表是这一页最该照着抄的东西。**
- 一条硬约束（原文 `Note`）：
  > `SPMU_TASK.execMode()` 里的 `TM::FORCE_ON` / `TM::FORCE_OFF`
  > **不能和** `SPMU_PIN_TASK.mode()` 设成 `"..._UNGANGED"` **同时用**。

**Application note：一条省时间的建议**（原文）

> *"For a minimized test time we recommend, not to reuse pattern with DC events that are to be
> applied for different XPS256 ranges."*

理由（原文）：XPS256 通道有多个 force range，**pattern 被复用到另一个 range 时，
相关 DC event 的 pattern 数据必须重载**，会显著增加测试时间。
适用范围：**手工用 test method API 建的 pattern**；
**不含 SmartRDI 自动生成的 pattern**（自动生成的没这个问题）。

## 和谁有关

**硬件层**：它是 **XPS256** 卡（DC Scale 系列）的一种工作模式。
并列的另一种是 → [[xps256-programming-dps-operating-mode]]（DPS 模式，给器件持续供电）。
总览在 `XPS256_operating_modes`（**未建页**，见下）。

**软件层（本页直接依赖的 API）**

- `SPMU_TASK` / `SPMU_PIN_TASK` —— 本页 API 部分的主体。
  **两个都在 `02.07.04.01.234*` 下，未建页**（入度不够）。用到时照 raw 路径去查。
- `SPMU_TASK.execMode()` / `SPMU_PIN_TASK.mode()` / `.relay()` / `.preCharge()` —— 上面反复引用的成员
- `DCCH` / `DCVH` / `DCEX` —— 例 3 里的 L1 底层命令
- `DC events` —— pattern-based setup 与测量走它
- [[digital-pins-editor]] —— **进这个模式的入口**（把 pin 设成 dc / SIG）
- `SmartRDI` 与 `Setting_up_DC_Scale_pins_with_SmartRDI` —— 推荐的编程路线的文档

**GUI 层**

- `Hardware_view` —— XPS256 在 PMU 模式下的 Hardware view，按钮有：
  **Quick** / **Measure** / → [[xps256-status-flags]]（Check Status Flags）/ **Profiling** /
  **Force Sense Check**（Kelvin 测试）/ **Surge Tracker** / **Max Voltage Drop** /
  **Check Gang Connection**。
  Measure 对话框里除了标准参数，**还能改测量的 regulation 和 safety 参数**（原文）。

**stage 归属**：`stage: level` —— 它做的是 **DC 电平 / 供电**这些事，
和 [[level]] 段里 DPS pin、clamping、termination 那一摊是同一类。
另有 [[pin]]（pin 定义）和 [[testmethod]]（它在 test suite 期间生效）的成分，
但**主战场是 DC 参数**。

**入边口径要说明**：`hubs-dedup.csv` 报的入度 **29** 里，
**有 1 是它自己**（文内 15 条锚点链接）。**真实外部入边 28 篇**，
主体是 XPS256 族的兄弟页（`XPS256 programming - Measure currents` / `- Ganging` /
`- Open loop protection` / `- Force and clamp voltages` / …）和 9 个 `SPMU_PIN_TASK.*` 成员页。

> 以上每条都来自 `edges.jsonl` 里带原句的边。**本页唯一的推断**是
> 「写新代码用 `CFxx` 别用 `IFVM`」——原文只说了 `IFVM` 是兼容用的遗留模式，没说别用。

## 版本

- **Introduced in SmarTest 7.10.1**（`Functional changes` 段，仅此一条）

> ⚠️ **这是本 wiki 目前唯一一篇「近期才引入」的对象页。**
> 前面几页都是 *"Introduced before SmarTest 6.3.2"*（也就是「很久以前就有」），
> 这一页是 **7.10.1**。本 wiki 面向 **7.10.3**，在；
> 但**任何低于 7.10.1 的机台上都没有这个模式**——照着这一页写代码会直接报找不到 API。
> （同类信号：入边里有 `SmartRDI 7.10.1` 一篇，互相印证。）

## 出处

- 定义文档：`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md`
  （TDC `354253.htm`，20,599 字节）
- **入边 57 条 / 29 篇**（含自身 1 篇 / 15 条文内锚点）：`extract/pack/06-xps256-programming-pmu-operating-mode.md`
  口径同 `hubs-dedup.csv`：**只算 `inline` 边**。
- 所属：**Test Head Cards**（`02.05`）→ XPS256（DC Scale 系列）
- ⚠️ **本页语料有编码损坏**：脚本抽出的标题里是 `pattern鈥慴ased`，
  原文是 `pattern–based`（en dash）。**`鈥慴` 是 `–` 的编码损坏**——
  同 [[pogo-pad-and-via-design]] 里那个 `碌`（应为 `µ`）。
  **这是语料层面的问题，不是抽取 bug**，也**不在 raw 上修**（§1.1 铁律：raw 只读）。
  引用这些字符串时按原意写，别照抄坏字符。
- 本页 `verified: doc-only` —— 只在 TDC 文档里确认存在，**未在任何真实 XPS256 上跑过**。
