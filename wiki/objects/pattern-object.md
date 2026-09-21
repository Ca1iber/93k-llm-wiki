---
type: object
title: PATTERN
layer: L2
stage: pattern
tags: [pattern, l2, pattern-object, subpattern, pattern-controller, vec-events, dc-waveform, ppm, badc]
related: [pattern-controller, vec-events, pattern, on-first-invocation-begin, on-first-invocation-end]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142.01_PATTERN.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# PATTERN

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,995 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142.01_PATTERN.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1

The example shows how to lookup the force voltage at a specific vector in the "myRamp" pattern.

```
// Get the PATTERN the events will be placed on
PATTERN_CONTROLLER patternController;
PATTERN & pattern(patternController.label("myRamp"));

// Get the force voltage at vector 100
DOUBLE voltage;

if (pattern.getForceVoltage("Vdd", 100, voltage))
{
    cout << "Voltage at vector 100: " << voltage << " V" << endl;
}
```

### Example 2

The example shows how to add a DC waveform to the designated label.

```
//
// Define an analog waveform
//
ANALOG_WAVEFORM ramp("ramp");
ramp.definition(TM::RAMP)
    .direction(TM::POS)
    .min(-1 V)
    .max(5.5 V)
    .samples(2048);

//
// Integrate the analog waveform into the DC waveform
//
DC_WAVEFORM dcWaveform;

dcWaveform.vForce(ramp)
    .vRange(6 V)
    .iRange(1 mA)
    .sampleVectorDistance(1024);

//
// Add the DC waveform to a label
//
PATTERN_CONTROLLER patternControllerDcWaveForm;
patternControllerDcWaveForm.label("ppmuSubRamp","portPpmu").add(dcWaveform);
patternControllerDcWaveForm.setup(); //This function is only needed for the first run.
```

### Example 3

The example below shows how to get the last current clamp that was defined before or at the specified vector in a pattern.

```
PATTERN_CONTROLLER pc;
PATTERN & pattern(pc.label("patEvents", "@"));

EVENT_IC iClampEvent1("iClampEvent1");
EVENT_RANGE_RESTORE eventRangeRestore("eventRangeRestore");

ON_FIRST_INVOCATION_BEGIN();

    iClampEvent1.iClampLow(1 mA);

    pattern.vecEvents("dps1").clearAll().setup();

    pattern.vecEvents("dps1")
            .insert(32, iClampEvent1)
            .insert(150, eventRangeRestore);

    pc.setup();

ON_FIRST_INVOCATION_END();

DOUBLE current = 0.;

if ( pattern.getClampHighCurrent("dps1", 32, current) )
{
    cout << "High current clamp at vector 32 (expect 999999): " << current << " A" << endl;
}

if ( pattern.getClampLowCurrent("dps1", 32, current) )
{
    cout << "Low current clamp at vector 32 (expect 0.001): " << current << " A" << endl;
}
```

<!-- 语法节 end -->

## 是什么

**一句话：`PATTERN` 是「一个 subpattern 的元素容器」。** 原文第一句就是它的定义：

> 「The PATTERN class is a subsidiary data container that holds elements of individual
> subpatterns.」

**三个词都要抠**：
- **`subsidiary`（附属的）**——**它不是主角**；
- **`data container`（数据容器）**——**它装东西**；
- **`elements of individual subpatterns`（各个 subpattern 的元素）**——
  **一个 `PATTERN` 对象对应一个 subpattern 的那些元素**，不是整份 pattern file。

**它怎么拿到——这一句是全页最要紧的一句**：

> 「The API cannot be instantiated directly, but can only be accessed by the `label(...)`
> member function of the `PATTERN_CONTROLLER` class.」

**即：`PATTERN` 没有公有构造函数。**
**要拿到一个 `PATTERN&`，只能从 `PATTERN_CONTROLLER` 的 `label(...)` 出来。**
本页三个例子的第一行全是这个形状：

```cpp
PATTERN_CONTROLLER patternController;
PATTERN & pattern(patternController.label("myRamp"));
```

**头文件**（原文给了绝对路径）：

> 「This API is defined in the header file `/opt/hp93000/soc/prod_com/include/MAPI/Pattern.h`.」

### 为什么这一页叫 `pattern-object` 而不是 `pattern`

**`pattern` 这个 slug 已经归「脊椎」里的 pattern 阶段页**（§5：stage 名是保留 slug）。
**两个是不同的东西**：

| 页 | 讲什么 |
|---|---|
| [[pattern]] | **pattern 那一段流程**（pattern / vector 这一环怎么走） |
| **本页 [[pattern-object]]** | **`PATTERN` 这个 L2 类**——一个 subpattern 元素的容器 |

**按 §5 的规矩，对象页与九页撞名时加限定词 `-object`，**不改 stage 名**。
**所以本页的 slug 是 wiki 自己造的，不是语料里的名字**——
**语料里这个东西就叫 `PATTERN`（全大写）**。

### 它有哪些成员函数（**八个函数，七个条目**）

原文 `## Class definition` 列了 7 条，其中第 6 条是**两个函数写在一起**的，
**所以实际是 8 个函数**：

| # | 成员函数 | 干什么（原文要点） |
|---|---|---|
| 1 | `add(TASK)` | 让 Board ADC 测试和数字测试**并行**跑；**在不停 sequencer 的前提下**在数字 / PinPMU / Board ADC 之间切换 |
| 2 | `add(PPMU_TASK)` | 把一个 `PPMU_SETTING` / `PPMU_RELAY` / `PPMU_MEASURE` / `PPMU_CLAMP` 对象**指派给一个 subpattern** |
| 3 | `add(BADC_TASK)` | 按同上方式指派一个 `BADC_SETTING` / `BADC_MEASURE` 对象 |
| 4 | `add(DC_WAVEFORM)` | **把一个 DC waveform 指派给这个 pattern** |
| 5 | `vecEvents(...)` | 取回指定 pin 的**向量事件编辑接口**（`VEC_EVENTS`） |
| 6 | `getClampHighCurrent(...)` | **往回找**在指定 vector 之前（或就在该 vector）最后定义的那个 high current clamp |
| 7 | `getClampLowCurrent(...)` | 同上，low current clamp |
| 8 | `getForceVoltage(...)` | **往回找**指定 vector 之前（或就在该 vector）定义的 force voltage |

> **本页「语法 / 参数」节里没有这些签名**，只有三个 `Example` 段。
> **原因**：脚本只认 `Syntax` / `Parameters` / `Example` 这类**段标记**，
> 而本篇用的是 `## Class definition` / `## Member functions`——
> **没有段标记时「哪一段是语法」是猜，所以脚本不收录**（§4 的规矩）。
> **代价**：上面这张表是**我按原文语义重排的**；
> **逐字的签名在 raw 的 `## Member functions` 一节里**，本页只把要点列出来。

### `add(TASK)` 那条讲得最细，它是一条**并行**机制

原文对 `add(TASK)` 的说明是：

> 「This member function allows to execute Board ADC tests in parallel with digital test for
> different ports, and also to alternate (switch) between digital tests, PinPMU tests, and
> Board ADC tests in one pattern run without the need to stop the sequencer.」

**它做的三件事**（原文紧接着的三条 bullet）：

- `downloads measurement sets defined with the PPMU_xxx and BADC_xxx APIs.`
- `inserts instructions (which will execute these sets) into a predefined subpattern.`
- `executes the current primary sets.`

**顺序读出来就是：先把测量集下进去 → 把执行指令插进一个预定义 subpattern → 再执行。**

### 四条会咬人的规矩（**散在成员函数说明里，最容易被漏**）

原文把这些写在各成员函数的说明里，**不是集中在一节**：

| 规矩（原文逐字） | 它管什么 | 形态 |
|---|---|---|
| `The pins for which the task is defined **must be a subset of** the pins of the port to which the subpattern belongs.` | **`add(TASK)` / `add(PPMU_TASK)` / `add(BADC_TASK)` 三条的参数说明里各写了一遍** | **归属/包含关系** |
| `The interface is valid for **only one pinlist at a time**. It is valid as long as the pattern is not changed via `label()`, or until the next call to `vecEvents()`. Each call to `vecEvents()` **will invalidate a previously retrieved VEC_EVENTS reference**.` | `vecEvents(...)` 返回的那个引用**会失效** | **有效期** |
| `If the force current cannot be determined, `false` is returned. This might for instance happen if **no force event exists** or **an equation variable is referenced that cannot be resolved to a value**.` | `getClampHighCurrent` / `getClampLowCurrent` 什么时候返回 `false` | **失败条件** |
| `Note that this function operates on setup data only!` + `Be aware that this function operates on vectors, not cycles!` | `getForceVoltage(...)` 的作用域 | **作用域限制** |

**第二条最容易被踩**：`vecEvents()` 拿到的引用**不是一直有效的**——
**下一次 `vecEvents()`、或者用 `label()` 改了 pattern，都会让它作废**。
**原文的措辞是 `will invalidate`（一定会），不是「可能」。**

### 两个查询函数的默认值约定

`getClampHighCurrent` / `getClampLowCurrent` 的参数表里，**`current` 那一格**写着：

> 「The found force current value. If no value is set, return value is 999999 for iClampHigh
> and -999999 for iClampLow.」

**即：找不到 clamp 时，出参不是 0，而是两个哨兵值 `999999` / `-999999`。**
（**注意原文这里用的是 `iClampHigh` / `iClampLow` 两个名字，
而函数名是 `getClampHighCurrent` / `getClampLowCurrent`**——见「出处」的 ⚠️。）

**返回值语义**（原文的 `Return value` 表）：

| 值 | 含义 |
|---|---|
| `true` | `The force current was successfully resolved.` |
| `false` | `No force current between pattern start and refVector was found.` |

### 读 `getForceVoltage` 时的一句内部张力

同一条说明里，原文先给了用途、再给了限制：

> 「It may be used for fast setup backtracking, for example, to lookup the force voltage
> at a specific cycle. Be aware that this function operates on vectors, not cycles!」

**前一句说「按 cycle 查」，后一句说「它按 vector 算，不是 cycle」。**
**两句挨着，原文没有解释怎么统一**——见「出处」的 ⚠️。**本页不替它调和。**

## 典型用法

**原文没有 `## Procedure` 段**，但它给了三个例子，**正好是三条不同的用法路径**。

**所有用法的第 0 步都一样**：**先从 `PATTERN_CONTROLLER` 拿到 `PATTERN&`**——
`PATTERN` 不能直接 `new`（见「是什么」）。
**注意 `label(...)` 在例子里有两种写法**：Example 1 用**单参数** `label("myRamp")`，
Example 2 / 3 用**双参数** `label("ppmuSubRamp","portPpmu")` / `label("patEvents", "@")`
——**两种都能拿到 `PATTERN&`，原文没解释区别。**

### 用法一：查某个 vector 上的 force voltage（Example 1）

```cpp
// Get the PATTERN the events will be placed on
PATTERN_CONTROLLER patternController;
PATTERN & pattern(patternController.label("myRamp"));

// Get the force voltage at vector 100
DOUBLE voltage;

if (pattern.getForceVoltage("Vdd", 100, voltage))
{
    cout << "Voltage at vector 100: " << voltage << " V" << endl;
}
```

**读法**：`getForceVoltage(pin, vector, out)` **返回 `bool`**——
**先判真再用电平值**，这是原文例子的姿势。

### 用法二：把一个 DC waveform 加到某个 label 上（Example 2）

**三步：先定义模拟波形 → 把它并进 DC waveform → 把 DC waveform 交给 label。**

```cpp
//
// Define an analog waveform
//
ANALOG_WAVEFORM ramp("ramp");
ramp.definition(TM::RAMP)
    .direction(TM::POS)
    .min(-1 V)
    .max(5.5 V)
    .samples(2048);

//
// Integrate the analog waveform into the DC waveform
//
DC_WAVEFORM dcWaveform;

dcWaveform.vForce(ramp)
    .vRange(6 V)
    .iRange(1 mA)
    .sampleVectorDistance(1024);

//
// Add the DC waveform to a label
//
PATTERN_CONTROLLER patternControllerDcWaveForm;
patternControllerDcWaveForm.label("ppmuSubRamp","portPpmu").add(dcWaveform);
patternControllerDcWaveForm.setup(); //This function is only needed for the first run.
```

**两处值得抄下来**：
① **`.add(dcWaveform)` 是接在 `label(...)` 后面的**——
`label(...)` 返回的就是 `PATTERN&`，**所以 `add` 是挂在 `PATTERN` 上的**
（这正是「`PATTERN` 只能从 `label()` 拿到」那句话的实操形状）；
② **`setup()` 那句原文自己带了注释**：
`//This function is only needed for the first run.` —— **只在第一次跑的时候需要**。

### 用法三：先用 `vecEvents` 插事件，再回头查 clamp（Example 3）

这一例把两个成员函数串起来用了，**而且它整段包在 `ON_FIRST_INVOCATION_BEGIN()` /
`ON_FIRST_INVOCATION_END()` 里**：

```cpp
PATTERN_CONTROLLER pc;
PATTERN & pattern(pc.label("patEvents", "@"));

EVENT_IC iClampEvent1("iClampEvent1");
EVENT_RANGE_RESTORE eventRangeRestore("eventRangeRestore");

ON_FIRST_INVOCATION_BEGIN();

    iClampEvent1.iClampLow(1 mA);

    pattern.vecEvents("dps1").clearAll().setup();

    pattern.vecEvents("dps1")
            .insert(32, iClampEvent1)
            .insert(150, eventRangeRestore);

    pc.setup();

ON_FIRST_INVOCATION_END();

DOUBLE current = 0.;

if ( pattern.getClampHighCurrent("dps1", 32, current) )
{
    cout << "High current clamp at vector 32 (expect 999999): " << current << " A" << endl;
}

if ( pattern.getClampLowCurrent("dps1", 32, current) )
{
    cout << "Low current clamp at vector 32 (expect 0.001): " << current << " A" << endl;
}
```

**这一例的信息量最大，有三件事是别处没有的：**

1. **`vecEvents` 是链式用的**：`vecEvents("dps1").clearAll().setup()`、
   `vecEvents("dps1").insert(32, iClampEvent1).insert(150, eventRangeRestore)`。
   **⚠️ 但这两次 `vecEvents("dps1")` 是两次调用**——
   按上面那条「有效期」规矩，**第二次调用会让第一次拿到的东西失效**。
   **原文没有针对这个例子说明这一点**（见「出处」的 ⚠️）。
2. **`pc.setup()` 的时机**：插完事件之后才 `setup()`。
3. **两个查询的期望值不一样**：high clamp 没设过 → `expect 999999`
   （正是那个哨兵值）；low clamp 在 `ON_FIRST_INVOCATION` 里设了 `1 mA` →
   `expect 0.001`（单位是 A，**即 1 mA**）。

### 什么时候用哪个函数

| 你要干的事 | 用哪个 |
|---|---|
| 往这个 subpattern 里挂一个测量任务（PPMU / BADC） | `add(PPMU_TASK)` / `add(BADC_TASK)`，或合并用 `add(TASK)` |
| 让它和数字测试**并行**、**不停 sequencer** | `add(TASK)` |
| 挂一段 DC waveform | `add(DC_WAVEFORM)` |
| 在 DC Scale 通道的 vector 上定义事件 | `vecEvents(pinlist)` → `VEC_EVENTS` |
| 回查某个 vector 上的 force voltage | `getForceVoltage(...)` |
| 回查某个 vector 之前最后定义的 current clamp | `getClampHighCurrent(...)` / `getClampLowCurrent(...)` |

## 和谁有关

- [[pattern-controller]] — **唯一的上游，也是唯一的入口**：
  原文说 `PATTERN` `cannot be instantiated directly`，
  **只能由 `PATTERN_CONTROLLER` 的 `label(...)` 成员函数取出来**。
  **本页三个例子的第一行都是它。** 原文还在 `Class definition` 里把这个 `label(...)`
  精确到了 `PATTERN_CONTROLLER` 的一个锚点。
- [[vec-events]] — **`vecEvents(...)` 的返回类型**：
  原文说用 `VEC_EVENTS` **可以在 pattern 的 vector 上定义 DC Scale 通道的事件**。
  **本页只讲「怎么拿到它」，它自己能定义哪些事件、怎么插，是它那一页的事。**
- [[pattern]] — **slug 避撞的另一半**（见「是什么」里那张表）：
  那是 pattern 这一段流程，**本页是 `PATTERN` 这个类**。**两者不是同一个东西。**
- [[on-first-invocation-begin]] / [[on-first-invocation-end]] — **Example 3 把
  `vecEvents` + `insert` + `pc.setup()` 整段包在这一对里**。
  **所以「这段代码该在哪跑」有一条现成的答案：第一次调用时。**
- **原文 `## Related information` 的另外两篇**（**均未读**）：
  `VEC_EVENTS`（就是上面那一页）、`PATTERN_CONTROLLER`（就是上面那一页）、
  `DC_WAVEFORM`（**本页没读，也没有页**）——**原文那一行把三篇挤在一起写。**
- **`add(...)` 各重载吃进去的那些类**（**均未读、也没页**）：
  `PPMU_SETTING` / `PPMU_RELAY` / `PPMU_MEASURE` / `PPMU_CLAMP`、
  `BADC_SETTING`（`02.07.04.01.09`）/ `BADC_MEASURE`（`02.07.04.01.08`）。
  **原文只在 `add` 的说明里点了名，没有解释它们。**
- **Example 2 / 3 里出现、本页不解释的类**（**均未读、也没页**）：
  `ANALOG_WAVEFORM`、`DC_WAVEFORM`、`EVENT_IC`、`EVENT_RANGE_RESTORE`。
  **它们只在例子里出现，原文没有给说明。**
- **`TASK`** —— `add(TASK)` 的形参类型名。
  **原文对它没有任何解释**（参数说明里说的是「`PPMU_xxx` 或 `BADC_xxx` 的类对象」）——
  **见「出处」的 ⚠️。**

> 上面每一条都来自本页读的那一篇 raw。**本页没有查 `edges.jsonl`，也没有从别的文档补事实。**

## 版本

本篇 `## Functional changes` **四条，正好把这个类的能力按版本摊开了**：

| 版本 | 条目（逐字） | 对应到哪个成员函数 |
|---|---|---|
| **—** | `Introduced before SmarTest 6.3.2` | **哨兵值，见下** |
| **SmarTest 6.5.2** | `Additional member functions: vecEvents() and getForceVoltage()` | `vecEvents(...)`、`getForceVoltage(...)` |
| **SmarTest 7.2.0** | `Additional member function for assigning DC waveform: add().` | `add(DC_WAVEFORM)` 那一个重载 |
| **SmarTest 7.2.1** | `Additional member functions: getClampHighCurrent and getClampLowCurrent` | 两个 clamp 查询函数 |

**四条读法**：

1. **第一条是哨兵值**：`Introduced before SmarTest 6.3.2` 按 §11.2 ② 读成
   **「在本文档集覆盖范围开始之前就已经有了」**，
   **不许读成「6.3.2 新增了 PATTERN 这个类」。**
2. **`PATTERN` 这个类本身很早就有，但它的能力是分四次长出来的**——
   **6.5.2 / 7.2.0 / 7.2.1 各加了一批**。**在一台 6.5.2 之前的机器上，
   连 `vecEvents()` 和 `getForceVoltage()` 都没有。**
3. **`7.2.0` 那条只提了「assigning DC waveform」那一个 `add()`**——
   （**推断**）**另外三个 `add()` 重载（`TASK` / `PPMU_TASK` / `BADC_TASK`）
   不在任何版本条目里，说明它们早于 6.3.2 或与类同期**。
   **依据是「Functional changes 里没提」+「7.2.0 那条专门限定了 DC waveform」**；
   **原文没有直接说这句话。**
4. **`6.5.2` 那条把两个函数写在一句里**（`vecEvents() and getForceVoltage()`），
   **7.2.1 那条也把两个写在一句里**（`getClampHighCurrent and getClampLowCurrent`）
   ——**引用时别把两句拆成四条**。

**本 wiki 面向 SmarTest 7.10.3：四条里的能力全都在。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142.01_PATTERN.md`

**本页只挂了这一篇。** 本批工单对这一页有两条规定，都照办了：
① **slug 保持 `pattern-object`，不改成 `pattern`**（那是 stage 页的名字，§5）；
② **`sources:` 只挂上面这一篇**，没有并入任何同章的邻居文档。

**本页没做的**：

- **`## Related information` 的三篇没读**（它们在原文里挤在同一行）：
  `VEC_EVENTS`（`02.07.04.01.267`）、`PATTERN_CONTROLLER`（`02.07.04.01.142`）、
  `DC_WAVEFORM`（`02.07.04.01.29`）。
  **所以「`PATTERN_CONTROLLER` 还有哪些成员」「`VEC_EVENTS` 能定义什么事件」
  「`DC_WAVEFORM` 怎么配」，本页一个字都没有。**
- **`## Member functions` 一节里链出去的类一篇没读**：
  `PPMU_SETTING` / `PPMU_RELAY` / `PPMU_MEASURE` / `PPMU_CLAMP`、
  `BADC_SETTING`（`02.07.04.01.09`）、`BADC_MEASURE`（`02.07.04.01.08`）。
  **所以 `add(...)` 吃进去的那些对象怎么造，本页没有依据。**
- **例子里出现过、但原文没有解释的类，本页也没读**：
  `ANALOG_WAVEFORM`、`DC_WAVEFORM`、`EVENT_IC`、`EVENT_RANGE_RESTORE`。
  **本页只用它们在例子里的样子，不解释它们的语义。**
- **一张图没看**——**本篇 raw 里本来就没有图**（整篇 217 行，无 `![` 引用）。
- **`## Class definition` / `## Member functions` 两节不在本页「语法 / 参数」里**——
  脚本只认 `Syntax` / `Parameters` / `Example` 段标记，**本篇用的是别的段名**，
  **所以那两节一个字都没进那一节**。**本页正文那张成员函数表是我按语义重排的**；
  **逐字的签名要回 raw 看。**
- **本页 `verified: doc-only`**：**没有在任何真实 93K 上跑过这三个例子**——
  §11：文档里有 ≠ 你这台能用。**尤其 `add(TASK)` 那条「不停 sequencer」的说法，
  文档这么说，机器上是什么样本页不知道。**

> ⚠️ **本篇的语料瑕疵，照实记录，一处都没替它改**：
> ① **签名多一个右括号**：raw 里 `add(TASK)` 的签名写作
>    `PATTERN & add(TASK & task));` —— **末尾是 `))`，多了一个 `)`**。
>    （同一篇另外三个 `add` 重载的签名都只有一个 `)`。）
> ② **一句话断在半路**：`add(TASK)` 的说明写到
>    `without the need to stop the sequencer. The API` 就断了
>    （**原句从 `This member function allows to execute Board ADC tests` 起头，
>    本页只截了尾巴那一小段**），
>    **`The API` 后面直接接 bullet 列表**，**这句话没有谓语**。
> ③ **参数说明是从 `getForceVoltage` 抄过来的（疑似）**：
>    `getClampHighCurrent` / `getClampLowCurrent` 的参数表里，`refVector` 那一格写的是
>    `The vector for which the currently active **force voltage** will be searched.`
>    —— **这两个函数找的是 current clamp，不是 force voltage**；
>    而真正的 `getForceVoltage` 的参数表里反而只写了 `Reference vector.`
>    （**两处对调了**）。**原文如此，本页照记。**
> ④ **出参默认值那条用了两个别处不存在的名字**：
>    `If no value is set, return value is 999999 for **iClampHigh** and -999999 for **iClampLow**.`
>    —— **`iClampHigh` / `iClampLow` 在本篇别处没有出现**，
>    **函数名是 `getClampHighCurrent` / `getClampLowCurrent`**。**原文如此。**
> ⑤ **一句内部张力**：`getForceVoltage` 的说明先写
>    `to lookup the force voltage at a specific **cycle**`，
>    紧接着写 `Be aware that this function operates on **vectors, not cycles**!`
>    —— **前一句按 cycle 说、后一句说不是 cycle。原文没有解释，本页不替它调和。**
> ⑥ **`API's` 用了撇号**：`assigns a class object of one of the PPMU_SETTING, PPMU_RELAY,
>    PPMU_MEASURE, or PPMU_CLAMP **API's** to a subpattern.`
>    （同一篇别处写的是 `APIs`）。**原文如此。**
> ⑦ **两张参数表被压平了**（同 §11.2 那一类）：raw 里是
>    ` Parameter` 独占一行、接着 ` | task  |`（后面本该是说明文字）**与下一个成员函数名黏在同一行**，
>    **所以 `add(PPMU_TASK)` / `add(BADC_TASK)` / `add(DC_WAVEFORM)` / `vecEvents(...)`
>    这几个函数名都出现在上一张表的最后一个单元格里。**
>    **结果是「下一个函数从哪开始」在 raw 里是看不出来的**，
>    本页正文是按成员函数重新组织的。**逐字的那份在 raw 第 28–115 行。**
> ⑧ **`## Related information` 的三条链接之间没有分隔符**，在 raw 里是连着的一串：
>    `](<02.07.04.01.267_VEC_EVENTS.md>)[PATTERN_CONTROLLER](<02.07.04.01.142_PATTERN_CONTROLLER.md>)[DC_WAVEFORM](<02.07.04.01.29_DC_WAVEFORM.md>)`
> ⑨ **Example 3 里 `vecEvents("dps1")` 被调了两次**，而同一篇的 `vecEvents` 说明写着
>    `Each call to vecEvents() will invalidate a previously retrieved VEC_EVENTS reference.`
>    —— **例子和规矩之间怎么统一（是「第二次调用前第一次已经用完」还是别的），
>    原文没说，本页不判。**
> ⑩ **三个 Example 的说明句行首都多一个空格**：raw 里分别是
>    ` The example shows how to lookup the force voltage at a specific vector in the "myRamp" pattern.`、
>    ` The example shows how to add a DC waveform to the designated label.`、
>    ` The example below shows how to get the last current clamp that was defined before or at
>    the specified vector in a pattern.` ——
>    **三个都顶着行首空格**（本页「语法 / 参数」节里已经看不出来了）。**原文如此。**

`verified: doc-only`
