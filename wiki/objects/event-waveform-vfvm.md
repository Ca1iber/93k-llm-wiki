---
type: object
title: EVENT_WAVEFORM_VFVM
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39_EVENT_WAVEFORM_VFVM.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# EVENT_WAVEFORM_VFVM

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,237 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39_EVENT_WAVEFORM_VFVM.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
class EVENT_WAVEFORM_VFVM : public EVENT_BASE

    EVENT_WAVEFORM_VFVM(const STRING & id);
    EVENT_WAVEFORM_VFVM(      INT      id);
    EVENT_WAVEFORM_VFVM();
```

This constructs an object of the EVENT_WAVEFORM_VFVM class. The class derives from the `EVENT_BASE`（raw: `02.07.04.01.63.01_EVENT_BASE.md`） class.

When using the EVENT_WAVEFORM_VFVM() constructor, the event ID is implicitly derived from the name of the assigned ANALOG_WAVEFORM. The event ID will look like: WAV_waveformName

Parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116926.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Example

- Describes the waveform of a voltage ramp:

```
ANALOG_WAVEFORM rampUp("rampUp");

rampUp.definition(TM::RAMP)
      .direction(TM::POS)
      .samples(4)
      .min(0.1).max(1.6);
```

- Defines a force voltage ramp waveform:

```
EVENT_WAVEFORM_VF rampUpEvent("ramp_0.1V_1.6V");
rampUpEvent.vForce(rampUp);
rampUpEvent.sampleVectorDistance(64);
```

- Requests validation of reached force voltage for each step. The allowed low voltage deviation is -10 mV. The upper value is not checked.

```
rampUpEvent.vForceCheckLow(-10 mV);
rampUpEvent.iClampChecks(false, true);
```

<!-- 语法节 end -->

## 是什么

`EVENT_WAVEFORM_VFVM` 是**组合式 force/measure 波形类**之一。原文对整族功能的说法是：

> 「Combined force/measure waveform classes provide functionality to define events, which generate
> waveforms, and measure at the same point in time when the samples are applied to the frontend.」

**两个专门的类：**

| 类 | 全称 |
|---|---|
| **`EVENT_WAVEFORM_VFVM`** | Voltage Force / **Voltage Measure** Waveform |
| `EVENT_WAVEFORM_VFIM` | Voltage Force / **Current Measure** Waveform |

**继承自 `EVENT_BASE`**；头文件 `/opt/hp93000/soc/prod_com/include/MAPI/Events.h`。

**三个构造函数**：`EVENT_WAVEFORM_VFVM(const STRING & id)`、`(INT id)`、以及无参的 `()`。
**`id` 可以是整数或字符串。**

> **无参构造那一个有个副作用值得记**：用它的时候，**event ID 是从被指派的
> `ANALOG_WAVEFORM` 的名字隐式推出来的**，形状是 **`WAV_waveformName`**。

**19 个子主题**（原文 `#### Subtopics` 的清单，**每一条都指向一篇独立文档**）：

`vForce()`、`sampleVectorDistance()`、`getSampleVectorDistance()`、
`getSamples()`、`averages()`、`getAverages()`、`vForceCheckLow()`、`vForceCheckHigh()`、
`getVForceCheckLow()`、`getVForceCheckHigh()`、`clearVForceCheck()`、`clampChecks()`、
`getClampChecks()`、`iClampChecks()`、`getIClampChecks()`、`outOfRangeCheck()`、
`getOutOfRangeCheck()`、`getRepeatCount()`。

> ⚠️ **上面这一串是 18 个，原文清单里是 19 个。** 差的那一条是**第二条**，
> 它挂的是 **`EVENT_WAVEFORM_VFIM.getVForce()`——另一个类（`VFIM`）的函数**，
> 而其余 18 条**全是本类 `EVENT_WAVEFORM_VFVM.*`**。
> **原文如此，本页没替它改，也没替它判断这是不是笔误**（原文对此一个字都没说）。

## 典型用法

原文 Example 分三步，**逐字照抄**：

**1. 先定义模拟波形**（电压斜坡）：

```c
ANALOG_WAVEFORM rampUp("rampUp");

rampUp.definition(TM::RAMP)
      .direction(TM::POS)
      .samples(4)
      .min(0.1).max(1.6);
```

**2. 定义 force voltage 的斜坡波形**：

```c
EVENT_WAVEFORM_VF rampUpEvent("ramp_0.1V_1.6V");
rampUpEvent.vForce(rampUp);
rampUpEvent.sampleVectorDistance(64);
```

**3. 要求每一步都校验达到的 force 电压**（允许的低压偏差 `-10 mV`；**上限不检查**）：

```c
rampUpEvent.vForceCheckLow(-10 mV);
rampUpEvent.iClampChecks(false, true);
```

> ⚠️ **原文例子里用的是 `EVENT_WAVEFORM_VF`，不是本页这个 `EVENT_WAVEFORM_VFVM`。**
> 这两个名字**大小写和字母都不同**（`VF` vs `VFVM`）。**这是原文如此，不是本页抄错。**
> 例子到底该用哪个类，**原文没说**——**本页不猜**。

## 和谁有关

- `EVENT_BASE`（**未建**）— 本类的基类
- `EVENT_WAVEFORM_VFIM`（**未建**）— 同一族的「电压 force / **电流** measure」
- `ANALOG_WAVEFORM`（**未建**）— **波形本身的定义**在这一族里；本类是往它上面挂 event 与控制项
- `EVENT_WAVEFORM_VF` / `EVENT_WAVEFORM_VM` / `EVENT_VALUE_INT`（**均未建**）— 原文 `Related information` 列的兄弟
- [[testmethod]] — MAPI（Test Method API）类，本页 `stage: testmethod` 由此而来
- [[pattern]] — 波形与 pattern 的关系在那边；**本页不判两者边界**

## 版本

- **Introduced in SmarTest 6.5.2**
- **SmarTest 7.4.0**：新增成员函数 `clampChecks()` 与 `getClampChecks()`

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39_EVENT_WAVEFORM_VFVM.md`

**本页没做的**：

- **19 个子主题只列了名字，一个签名都没抄。** 每一条原文都有自己的专页
  （`02.07.04.01.63.39.01_EVENT_WAVEFORM_VFVM.vForce.md` 等 19 篇），**本页一篇都没读**。
- **`Related information` 那六个兄弟类，一个都没读**（`EVENT_BASE`、`EVENT_VALUE_INT`、
  `EVENT_WAVEFORM_VF`、`EVENT_WAVEFORM_VM`、`EVENT_WAVEFORM_VFIM`、`ANALOG_WAVEFORM`）。
- **本类的语法节是脚本逐字抽的**（见上），**本页散文部分不重复它**——
  要构造函数的完整形态看上面那一节。

`verified: doc-only`
