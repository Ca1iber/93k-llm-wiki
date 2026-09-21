---
type: concept
title: DC Test Programming
layer: n/a
stage: testmethod
tags: [testmethod, dc-measurement, pmu, dps, api, connect]
related: [testmethod, results, connect, disconnect, primary-status, level-spec, dc-result-accessor, dps128-dps64-cards, spmu-pin-task-mode, xps256-pmu-operating-mode, dc-scale-xps256-card, hv-protection]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02_DC_Test_Programming.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# DC Test Programming

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,825 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.03.02_DC_Test_Programming.md>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.03.02.01_Flex_DC.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.03.02.02_DC_Test_Programming_with_PPMU.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.03.02.04_DC_test_programming_with_DPS.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Flex DC）

The following shows a comparison of various measuring methods from a sample production test program:

- DC measurement using SPMU: 80 ms
- DC measurement using PPMU Flex DC with a value: 42 ms
- DC measurement using PPMU Flex DC with NO value: 12 ms

The reason for this saving, is that acquiring a measured value per pin is a serial operation (using the per board ADC).

The following APIs can be replaced by Flex DC to save test time:

- PMU_IFVM
- PMU_VFIM
- DPS_VFIM
- PMU_AUTORANGE

### Example（取自子主题 DC Test Programming with PPMU）

- The following example shows a multi-site measurement with different settings on different pins.

```
PPMU_MEASURE ppmuMeasure;
ON_FIRST_INVOCATION_BEGIN();
  PPMU_SETTING ppmuSetting;
  PPMU_RELAY   ppmuRelayOn, acRelayOn;
  TASK_LIST    simpleFlexDc;

  ppmuSetting.pin("I/O1").vForce(0 V).iRange(1 uA).max(1 uA).min(-1 uA);
  ppmuSetting.pin("I/O2").iForce(1 uA).iRange(1 uA).max(0.5 V).min(1 V);
  ppmuRelayOn.pin("I/O1,I/O2").status("PPMU_ON");
  ppmuRelayOn.wait(1.3 ms);
  ppmuMeasure.pin("I/O1").execMode(TM::PPF);
  ppmuMeasure.pin("I/O2").execMode(TM::PVAL);
  acRelayOn.pin("I/O1,I/O2").status("AC_ON");
  simpleFlexDc.add(ppmuSetting).add(ppmuRelayOn).add(ppmuMeasure).add(acRelayOn);
  simpleFlexDc.execute();
ON_FIRST_INVOCATION_END();
TESTSET().judgeAndLog_PpmuMeasure(ppmuMeasure);
```

- The following example shows how to measure a current on a device pin and then use it as a force value for a following measurement for multi-sites. The result value of the first measurement differs from site to site.

```
PPMU_MEASURE ppmuMeasure2;
ON_FIRST_INVOCATION_BEGIN();
  PPMU_MEASURE ppmuMeasure1;
  PPMU_SETTING ppmuSetting1,ppmuSetting2;
  PPMU_RELAY   ppmuRelayOn, acRelayOn;
  TASK_LIST multiDeltaFlexDc1, multiDeltaFlexDc2;
  // 1st measurement
  ppmuSetting1.pin("I/O1").vForce(0 V).iRange(1 uA).max(1 uA).min(-1 uA);
  ppmuRelayOn.pin("I/O1").status("PPMU_ON");
  ppmuRelayOn.wait(1.3 ms);
  ppmuMeasure1.pin("I/O1").execMode(TM::PVAL);
  acRelayOn.pin("I/O1").status("AC_ON");
  multiDeltaFlexDc1.add(ppmuSetting1).add(ppmuRelayOn).add(ppmuMeasure1);
  multiDeltaFlexDc1.execute();

  // dummy setting for avoiding DC set run out
  ppmuSetting2.pin("I/O1").iForce(0 uA).iRange(1 mA).max(0.5 V).min(-0.5 V);
  ppmuSetting2.wait(1 ms);
  ppmuMeasure2.pin("I/O1").execMode(TM::PVAL);
  multiDeltaFlexDc2.add(ppmuSetting2).add(ppmuMeasure2).add(acRelayOn);
  multiDeltaFlexDc2.setup();

  // 2nd measurement
  FOR_EACH_SITE_BEGIN();
    ppmuSetting2.pin("I/O1")
                .iForce(ppmuMeasure1.getValue("I/O1"))
                .iRange(ppmuMeasure1.getValue("I/O1"))
                .max(0.5 V)
                .min(-0.5 V);
  FOR_EACH_SITE_END();
  multiDeltaFlexDc2.execute();
ON_FIRST_INVOCATION_END();

TEST("I/O1",
     "multi_delta",
     ppmuMeasure2.getPassFail("I/O1")?TM::Pass:TM::Fail,
     ppmuMeasure2.getValue("I/O1"),
     true );
```

- The following example shows a PPMU IFVM test on the pin S0 and a PPMU VFIM test on the pin S1. Clamp is used to avoid hot switching in the IFVM test.

```
PPMU_SETTING   ppmuSetting;
PPMU_RELAY     ppmuRelay_on, ppmuRelay_off;
PPMU_MEASURE   ppmuMeasure;
PPMU_CLAMP     ppmuClamp_on, ppmuClamp_off;
TASK_LIST      taskList_1;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Setups for PPMU
    //
    ppmuSetting.pin("S0").iRange(1 mA).min(0 V).max(4.3 V).iForce(10 uA);
    ppmuSetting.pin("S1").iRange(10 mA).min(-10 uA).max(30 uA).vForce(3.3 V);

    //
    // Relay setups
    //
    ppmuRelay_on.pin("S0,S1").status("PPMU_ON");
    ppmuRelay_on.wait(1.3 ms);
    ppmuRelay_off.pin("S0,S1").status("AC_ON");

    //
    // Measurement setups
    //
    ppmuMeasure.pin("S0,S1").execMode(TM::PVAL);

    //
    // Hardware specific programming to avoid hot switching on the current force setup
    //
    ppmuClamp_on.pin("S0").status("CLAMP_ON").low(2.6 V).high(2.9 V);
    ppmuClamp_off.pin("S0").status("CLAMP_OFF");

    //
    // Build and execute the task list
    //
    taskList_1.add(ppmuSetting)
              .add(ppmuClamp_on)
              .add(ppmuRelay_on)
              .add(ppmuClamp_off)
              .add(ppmuMeasure)
              .add(ppmuRelay_off);

    taskList_1.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and Datalog
//
double VMeas, IMeas;

VMeas = ppmuMeasure.getValue("S0");
IMeas = ppmuMeasure.getValue("S1");

TEST("DC_Test",ppmuMeasure, true);
```

### Example（取自子主题 DC test programming with DPS）

The following example performs a DPS global pass/fail measurement on pin Vcc and Vee with the current primary set.

```
DPS_TASK dpsTask;
static STRING tsName;
ON_FIRST_INVOCATION_BEGIN();
  CONNECT();
  GET_TESTSUITE_NAME(tsName);
  dpsTask.pin("Vcc").min(0 A).max(0.1 A);
  dpsTask.pin("Vee").min(0 A).max(0.2 A);
  dpsTask.execMode(TM::GPF);
  dpsTask.trigMode(TM::INTERNAL);
  dpsTask.execute();
ON_FIRST_INVOCATION_END();
TESTSET().judgeAndLog_Dps(dpsTask);
```

<!-- 语法节 end -->

## 是什么

**本页讲的是「写一个 DC 测试程序」这件事的第一层：按资源类型选 API。**

原文第一句就把它定成一个选择题，不是一套流程：

> 「To create a DC test program, first, **set up the DC resources using the following APIs, depending
> on the DC resource type and your purpose**.」

**「resource type」和「your purpose」是两个自变量**——下面两张 API 表就是它们的组合结果。

### 先看一条总建议：优先 FlexDC

原文开头一个 `Note`，**这条比下面所有 API 清单都重要**：

> 「Use **FlexDC APIs** for dc test programming **to save test time**.」

**没有展开、没有给链接、没有说 FlexDC API 具体是哪个**（`Subtopics` 里有一篇
`Flex DC`，本页没读）。**本页只知道「有更省时间的写法」这件事。**

### 分支一：pin PMU

| 用途 | 单数 / 复数两个版本 |
|---|---|
| 设置 | `PPMU_SETTING` / `PPMU_PIN_SETTING` |
| 继电器 | `PPMU_RELAY` / `PPMU_PIN_RELAY` |
| 测量 | `PPMU_MEASURE` / `PPMU_PIN_MEASURE` |
| 任务列表 | `TASK_LIST` |

**能力**：`you can program an **individual force voltage or current value per pin**, apply it to
the pin, and perform a measurement.`

> **⚠️ 测完之后 pin PMU 不会自己停**——原文：
> 「After the measurement finishes, **the pin PMU remains connected to the pin and continues to
> output**. **Alternatively, you can set up your program such that the pin PMU stops the output and
> relays are disconnected after the measurement finishes.**」
> **即：默认是「继续输出」，要停得自己在程序里设。**

### 分支二：DPS

**只有两个 API**：`DPS_TASK` 和 `DPS_PIN_TASK`。原文给它们的好处是三条：

| 好处 | 原文 |
|---|---|
| **并行测量** | `allow you to make DPS measurements **in parallel** when performing single-site or multi-site testing. Parallel testing can help you achieve higher throughput.` |
| **不同种类的 DPS 测量也能并行** | `allow you to make **different kinds** of DPS measurements in parallel…` |
| **两种触发都支持** | `Both **external-triggered** and **software-triggered** DPS measurements are supported` |

### ⚠️ 什么时候**必须**换成 `DPS_VFIM`

这是本页唯一一条硬性的「必须」，原文写在一个 `Note` 里，**两个条件**：

> 「If you need **(a) auto-ranging in DPS current measurements** or **(b) need to suppress
> activation of the level/timing-related primaries that are specified in the Testsuite dialog in
> the DPS measurements**, you **must use the `DPS_VFIM` API**. In all other cases, it is
> recommended that you use the `DPS_TASK` and `DPS_PIN_TASK` APIs…
> (**Auto-ranging and preAction "NPRM" are not supported by the `DPS_TASK` API.**)」

**归纳成表：**

| 你要做的事 | 用什么 |
|---|---|
| 普通的 DPS 电流测量 | `DPS_TASK` / `DPS_PIN_TASK`（**推荐**） |
| **DPS 电流测量要 auto-ranging** | **`DPS_VFIM`（必须）** |
| **要抑制 Testsuite 对话框里指定的 level/timing 相关 primaries** | **`DPS_VFIM`（必须）** |

**括号里那句是对上的**：`DPS_TASK` 不支持 auto-ranging，
所以「要 auto-ranging」自然就得换 `DPS_VFIM`。
**但 `preAction "NPRM"` 这个说法原文没有定义**——它出现在括号里，前面没有任何解释。

### `DPS_TASK` 力哪个电压

> 「The `DPS_TASK` API **forces the voltage defined in the primary DPS set or primary level
> spec/equation sets** and performs the current measurement.」

**即：它不接一个「电压值」参数，力的是 primaries 里已经定好的那个电压。**
所以要改力值，**得改 primaries**，两条路原文都给了：

| 改什么 | 用哪个 API |
|---|---|
| 改 primaries | **`PRIMARY_STATUS`** |
| 改 level specification 的值 | **`LEVEL_SPEC`** |

> **⚠️ 测完之后 DPS 也不会自己停**（和 pin PMU 同样的问题）：
> 「the DPS **keeps the connection to the pin and continue to output the voltage**.
> If you want to stop the DPS outputs, **perform the `DISCONNECT` sequence**.」

### 一条贯穿全页的前置：`CONNECT` / `DISCONNECT`

原文最后一段那个 `Note`（和前一节的链接粘在一起，见「出处」的瑕疵条）说：

> 「You need to execute the **`CONNECT` sequence before the test**, to apply the power to DUT and
> connect the target pins to tester resources. To do this in a test method program, use the
> `CONNECT` API. If you perform **continuity tests** with the DC APIs, you must execute the
> **`DISCONNECT` sequence before the tests**. To do this in a test method program, use the
> `DISCONNECT` API.」

**拆开看，两条前置的方向是相反的：**

| 测试类型 | 前置动作 |
|---|---|
| 一般 DC 测试 | **测试前 `CONNECT`** |
| **continuity test** | **测试前 `DISCONNECT`** |

### 取结果

> 「To execute a DC test and retrieve the measurement results, use the appropriate **member function
> of the DC API**.」

**一句话，没说是哪个 member function**（本页只知 `DC API` 这个说法，
`Subtopics` 里也没有专门讲它的一篇；另有一页 `dc-result-accessor` 在 allowlist 里）。

## 典型用法

**1. 选路**（本页自己按原文整理）：

```
要写 DC 测试
  ├─ 用 pin PMU？        → PPMU_SETTING/RELAY/MEASURE（+ TASK_LIST）
  ├─ 用 DPS？
  │    ├─ 要 auto-ranging 或要抑制 primaries？ → DPS_VFIM（必须）
  │    └─ 否则                                  → DPS_TASK / DPS_PIN_TASK
  └─ 是不是 continuity test？ → 是的话，测试前要先 DISCONNECT
```

**2. `Before you begin`**：**原文这篇没有这一节**。
但正文给出了一条等价的前置：**测试前要 `CONNECT`**（continuity test 除外，见上表）。

**3. 顺序（本页按原文拼出来的）**：

1. **`CONNECT`**（continuity test 则先 `DISCONNECT`）
2. **按资源类型设 DC 资源**——pin PMU 走 `PPMU_*`，DPS 走 `DPS_TASK` / `DPS_PIN_TASK`
3. **（DPS）要改力值就改 primaries**——`PRIMARY_STATUS` 或 `LEVEL_SPEC`
4. **执行测量**（DPS `*_TASK` 自己力电压并测流）
5. **取结果**——DC API 的对应 member function
6. **收尾**——DPS 要停输出就走 `DISCONNECT` 序列；
   pin PMU 默认继续输出，**要停得自己在程序里设**

**4. 一段没写的部分**：原文自己把「和 AC 测试共通」的部分让出去了，指了两篇：
`Accessing Test Control Options`、`Computing Measurement Values`（**均未建，本页未读**）。

**5. `What to do next`**：**原文这篇没有这一节。**

## 和谁有关

- [[testmethod]] — 本页的所有 API 都写在 test method program 里
- [[connect]] / [[disconnect]] — **本页的前置和收尾**；`CONNECT` 在测试前，`DISCONNECT` 既是
  continuity test 的前置、也是 DPS 停输出的手段
- [[primary-status]] / [[level-spec]] — **改 `DPS_TASK` 力值的唯一两条路**
- [[dc-result-accessor]] — 取 DC 结果的那一侧；**本页只说「用 DC API 的 member function」，
  没说是哪一个**
- [[dps128-dps64-cards]] — `DPS_TASK` / `DPS_PIN_TASK` / `DPS_VFIM` 打交道的卡
- [[spmu-pin-task-mode]] — **per-pin 的 task 模式**；和本页 `DPS_PIN_TASK` 是同一族写法
- [[xps256-pmu-operating-mode]] — **pin PMU 的工作模式**；本页的 `PPMU_*` API 作用在它上面
- [[dc-scale-xps256-card]] / [[dc-scale-uhc4t-card]] — DC Scale 卡；本页没提，
  但它们在本 wiki 里是 DC 资源的另一半（**（推断）**，依据是同属 DC 测试资源，
  **本页原文一个字没说**）
- [[hv-protection]] — `Functional changes` 里 7.1.3 那条提到 `HV pins`，是它在 wiki 里的落点
- `Flex DC` / `FlexDC APIs`（**未建**）— **原文开头那条「省测试时间」的建议指的就是它**；
  **本页没读，所以不知道它是什么**
- `DC Test Programming with PPMU` / `DC test programming with DPS` /
  `Direct DMM high-accuracy voltage measurements via utility pogo block` / `Per Pin PMU` /
  `DC Test Methods, DC Sets, and Measurement Sets` / `Executing PPMU tests from a pattern` /
  `Setting up DC Connection for Analog Pin` / `Miscellaneous Considerations for DC tests`
  （**均未建**）— **本页 `Subtopics` 列的九篇，一篇没读**
- `Accessing Test Control Options` / `Computing Measurement Values`（**均未建**）—
  原文明确让出去的「和 AC 共通」的部分

## 版本

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.1.3**：`Added reference to HV pins`

> **7.1.3 那条只加了「引用」**——原文的措辞是 `Added reference to HV pins`，
> **不是「支持 HV pin」**。本页照实转述，**不把它读成能力变化**。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.03.02_DC_Test_Programming.md`

**本页没做的**：

- **`Subtopics` 列的九篇一篇没读**——**这是本页最大的缺口**。所以：
  **「DC 测试编程的每一步」原文说要靠 `Sub-sections` 讲，而本页只有主文档这一层。**
  原文自己写：`The sub-sections in DC Test Programming explain each step in typical DC test
  programming and show DC test-specific information only.`
  ——**那些「每一步」本页一篇都没有。**
- **`FlexDC` 一个字没读**——**本页最重要的一条建议（用 FlexDC 省时间）本页无法展开**，
  连 FlexDC API 叫什么名字都不知道。
- **三个 `Note` 里提到的 API 本页都没读**：`DPS_VFIM`、`PRIMARY_STATUS`、`LEVEL_SPEC`、
  `CONNECT`、`DISCONNECT`。**本页只有原文给它们的一句职责描述。**
- **`preAction "NPRM"` 是什么，原文没定义，本页也不知道。**
- **图零张**（原文这篇没有图）。
- **「DC API 的 member function」具体是哪个，原文没写**，本页照实说「不知道」。
- **原文这篇没有 `## Before you begin` / `## Procedure` / `## What to do next`**，
  所以「典型用法」那一节**是本页从正文里整理的顺序，不是原文的步骤**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`Flex DC` 和 `FlexDC` 两种写法在同一页里都出现**——
> `Subtopics` 里是 `Flex DC`（带空格），开头 `Note` 里是 `FlexDC APIs`（不带空格）。
> ② **`preAction "NPRM"` 这个术语全文没有解释**，
> 只出现在 `(Auto-ranging and preAction "NPRM" are not supported by the DPS_TASK API.)`
> 这一处括号里。
> ③ **`Note` 和它前面的内容之间没有换行**，原文最明显的一处是
> `[Computing Measurement Values](<…>)Note You need to execute the CONNECT sequence…`
> ——**链接收尾的 `)` 后面直接就是 `Note`**。
> ④ **`Subtopics` 里的 `Direct DMM high-accuracy voltage measurements via utility pogo block`
> 在正文里一个字都没提**——正文只讲了 pin PMU 和 DPS 两条路。
> ⑤ **`## To create a DC test program for pin PMUs` / `## To create a DC test program for DPSs`
> 这两个标题插在正文中间**，而它们和 `## Functional changes` 是同一级（H2）——
> **正文的层级被这两个「怎么做」的标题切开了。**

`verified: doc-only`
