---
type: object
title: VEC_EVENTS
layer: L2
stage: pattern
tags: [pattern, l2, test-method-api, vec-events, dc-event, dc-scale, event, test-point, multisite, site-focus, incremental-change]
related: [pattern, pattern-object, pattern-controller, event-base, event-value-int, event-value-double, event-waveform-vfim, event-waveform-vfvm, dc-result-accessor, on-first-invocation-begin, for-each-site-begin, for-each-site-end, dc-scale-xps256-card, dc-test-programming, mapping-pattern, smartest-6.5.2, smartest-6.5.4]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.267_VEC_EVENTS.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VEC_EVENTS

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,470 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.267_VEC_EVENTS.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Insert events into a pattern, replace an event on a single site

This example shows how events can be inserted into a pattern and incrementally changed between test executions on a per site granularity. Three events (frc1V, frc2V, frc3Vmeas) drive a ramp, while only the second force voltage is measured via the third event (frc3Vmeas). In the example, the second event on site 2 is replaced by an event that additionally measures the first force voltage.

```
PATTERN_CONTROLLER patController;
DC_RESULT_ACCESSOR results;
ARRAY_D            values;

ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Insert events on pin Vdd1 in pattern "myRamp"
    //
    PATTERN & pattern(patController.label("myRamp"));

    //
    // Start from scratch with 2 force voltage events
    //
    EVENT_VF   frc1V("frc1V"); frc1V.vForce(1 V);
    EVENT_VF   frc2V("frc2V"); frc2V.vForce(2 V);
    EVENT_VFVM frc3Vmeas("frc3Vmeas"); frc3Vmeas.vForce(3 V);

    pattern.vecEvents("Vdd1")
           .clear()
           .insert(100, frc1V)
           .insert(200, frc2V)
           .insert(300, frc3Vmeas);

    //
    // Execute the pattern and upload results
    //
    patController.execute();

    results.uploadResult("Vdd1", TM::RESULT_INDEX);

    FOR_EACH_SITE_BEGIN()
    {
        //
        // Get measurement values for Vdd1 per site
        //
        results.getValues("Vdd1", values);
        ...
        ...
    }
    FOR_EACH_SITE_END();

    //
    // Now replace the event frc2V by frc2Vmeas on site 2 only
    //

    ARRAY_I oldSites;

    GET_TEST_FOCUS(oldSites); // Get current setup-focused sites

    if ( SET_TEST_FOCUS(2) )  // Select site 2 if available
    {
      VEC_EVENTS& site2_event(pattern.vecEvents("Vdd1"));

      site2_event.remove(200)
                 .insert(200, EVENT_VFVM("frc2Vmeas").vForce(2 V));
    }

    SET_TEST_FOCUS(oldSites); // Restore setup sites

    //
    // Execute the pattern and upload results
    //
    patController.execute();

    results.uploadResult("Vdd1", TM::RESULT_INDEX);
}
ON_FIRST_INVOCATION_END();

//
// Get measurement values for Vdd1 per site
//
results.getValues("Vdd1", values);

...
...
```

### Example 2: clearAll() member function

This example demonstrates the use of the `clearAll()` member function. Be careful! It removes all events, independent of whether they were defined by the API or manually.

```
PATTERN_CONTROLLER pc;

ON_FIRST_INVOCATION_BEGIN();
{
    PATTERN & pattern(pc.label("pat1", "@"));

    VEC_EVENTS & vecEvents(pattern.vecEvents("Vdd1"));

    // Schedules a forced clear of all events defined on the pin Vdd1.
    // All events will be removed, independent of whether they were defined
    // by the API or added manually. So be careful.
    vecEvents.clearAll();

    // Execute the removal step.
    // Actually you may have also new events defined before the setup() call.
    // Then the events will first be removed and the new ones will be defined afterwards.
    vecEvents.setup();

    // Instead of calling vecEvents.setup() you may also only call pc.setup(),
    // which will do the changes for all patterns at once. In this example here
    // the deletion of the events has happened already during vecEvents.setup().
    // Therefore pc.setup() has no effect and will be an NOP.
    pc.setup();
}
ON_FIRST_INVOCATION_END();
```

### Example 3: Setup per site

For an example that shows how to program an setup per site by DC events, refer to `DC event example: Setup per site`（raw: `../../03_Use_cases_and_application_papers/03.05_How_to_set_up_a_dynamic_DC_test/03.05.02.04_DC_event_example__Setup_per_site.md`）.

<!-- 语法节 end -->

## 是什么

**`VEC_EVENTS` 是「往 pattern 的 vector 上按时序摆事件」的编辑接口。** 原文第一句：

> VEC_EVENTS provides all functionality to place events time wise into a pattern, and to update or remove events defined via this API. Incremental changes are supported.

**这句话里三个词是全部机制**：`time wise`（**事件是按 vector 号定位的，不是按时间轴上的秒**）、
`update or remove`（**已定义的事件可以增量改，不必重写整张 pattern**）、
`defined via this API`（**它认自己定义的账**——这条正是 `clear()` 与 `clearAll()` 的分界，见下）。

### 它不能自己造——只能从 `PATTERN` 拿

> VEC_EVENTS cannot be created directly, but is maintained by the PATTERN instance.

**所以拿到它的路径是唯一的**（例子里逐字就是这个写法）：
`pattern.vecEvents("Vdd1")`——**先有 `PATTERN`，再用 pin 名把它取出来**。
`PATTERN` 怎么来（`PATTERN_CONTROLLER::label()`）不在本篇，见 [[pattern-object]] 与
[[pattern-controller]]（**那两篇本页没读**）。

**头文件**（原文给了绝对路径）：

> This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/VecEvents.h.

### **event 与 test point 是两样东西**——本页最要紧的一条

原文对八个成员函数各给了一句说明，**那八句里反复出现两个词**：
`event`（事件本身）与 `test point`（它在某个 vector 上的落点）。
**同一个 event 可以在多个位置被引用，而「删的到底是哪一个」正是这些函数的分工：**

| 成员函数（签名逐字见「语法 / 参数」节） | 造什么 / 删什么 | 原文给的前置条件 |
|---|---|---|
| `insert(INT vector, const EVENT_BASE & event)` | **event 与 test point 一起造** | `the event and the test point must not exist` |
| `reinsert(INT vector, const STRING & eventId)` | **只加一个 test point**，指向**已存在**的 event | `the event must exist but not the test point` |
| `update(const EVENT_BASE & event)` | 改**已有的 event 实例** | —（**改的是 event，不是 test point**） |
| `remove(INT vector)` | 删**一个 test point**；**若那个 event 再没人引用，连它一起删掉** | `the test point must exist` |
| `remove(const STRING & eventId)` | 删**一个 event，以及所有引用它的 test point** | `the event must exist` |
| `clear()` | 删**本 API 定义过的**全部 test point 与 event | — |
| `clearAll()` | 删 **pattern 里全部**（**含手工交互加进去的**） | —（见下：它是**延期**发生的） |
| `setup()` | **立即下载**已定义的 setup（返回 `void`，不是 `VEC_EVENTS&`） | — |

**逐字对照（这四句是这张表的骨头）：**

> This member function inserts an event at the specified anchor vector. Both, event and test point will be created. Note that the event and the test point must not exist.

> This member function inserts a test point referring to an existing event. Note that the event must exist but not the test point.

> This member function removes an existing test point. If the referenced event is no longer referenced by other test points, it will be removed. Note that the test point must exist.

> This member function removes an existing event and all test points that refer to this event. Note that the event must exist.

**两个 `remove` 靠参数类型区分**：`remove(INT vector)` **吃 test point 的位置**，
`remove(const STRING & eventId)` **吃 event 的 ID**。
**两条以 `Note that` 开头的说明，方向正好相反**（一个要求 test point 存在、一个要求 event 存在）——
**写错那一个，原文给的就是「前置条件不满足」**。

**`update` 的覆盖面比名字看起来大**：

> This member function updates an existing event instance. If the event has been inserted multiple times at different, vectors, all these locations will be affected.

**同一个 event 插在几个 vector 上，`update` 一次全改。**

### `clear()` / `clearAll()` / `setup()`：**删是延期的，下载是立即的**

这三条要连起来读，否则最容易踩：

| 函数 | 删什么 | **什么时候真的删掉** |
|---|---|---|
| `clear()` | **本 API 定义过的** test point 与 event | **没写**——原文只有 `This member function removes all test points and events defined by this API.` |
| `clearAll()` | **pattern 里的全部**，含手工加的 | **不是立刻**：`at the next call of VEC_EVENTS::setup(), PATTERN_CONTROLLER::setup(), or PATTERN_CONTROLLER::execute()` |
| `setup()` | —（它不删东西） | 它做的事是 `forces the immediate download of the defined setup` |

**`clearAll()` 那一句原文前面还有一句警告**：

> Use with care!

**完整那句（`clearAll()` 的定义）逐字是**：

> This member function removes all test points and events in the pattern, independent of whether they have been defined by this API or manually via user interaction, at the next call of VEC_EVENTS::setup(), PATTERN_CONTROLLER::setup(), or PATTERN_CONTROLLER::execute().

**⚠️ `clear()` 那一句没有说「什么时候生效」**——上面表里那一格本页写的是「没写」，
**不替它补成「和 clearAll 一样」**（两条的原文措辞本来就不同：`clearAll` 明写了三个触发点，
`clear` 一个字没有）。**这一步是语料未写。**

### 多 site：**改过 focus 之后必须重新取一次**

> For multi-site handling you can set the setup site focus by the standard SET_TEST_FOCUS() TM-API, or use the FOR_EACH_SITE_XXX() loops. All editing functions will respect it. After changing the test focus, VEC_EVENTS must be queried from PATTERN.

**三句话三个要点**：① 改 focus 用 `SET_TEST_FOCUS()` 或 `FOR_EACH_SITE_XXX()` 循环；
② **所有编辑函数都认这个 focus**；③ **改完之后 `VEC_EVENTS` 必须重新从 `PATTERN` 取一次**——
**手里那个旧引用不算数了**（Example 1 就是这么做的，见「典型用法」）。

> **这条与 [[pattern-object]] 那一页的记载能对上**：那一页记着它那一篇写着
> `Each call to vecEvents() will invalidate a previously retrieved VEC_EVENTS reference.`
> ——**两句说的是同一件事的两面**（一句从「改 focus」出发，一句从「再调一次 `vecEvents()`」出发）。
> **本页没有读 `PATTERN` 那一篇的 raw**，所以这里只登记「两处对得上」。

### 一条硬件门槛

> Note Only DC Scale cards support this kind of events.

**即：这套事件机制只在 DC Scale 卡上有。** 原文把 `Note` 和句子挤在一行里
（那一句以 `Note` 开头、与句子挤在一行里），**本页照原样引**，见「出处」⚠️①。
**哪些卡算 DC Scale、非 DC Scale 卡上调用会怎样——本篇都没有写。**

## 典型用法

**三个 Example 都已经在上面「语法 / 参数」节里逐字，本页不重抄**——
下面只说「读它时该看什么」。**本文档没有 `## Procedure` 段、也没有 `## Before you begin` 段。**

### Example 1：一趟完整的「插事件 → 执行 → 只改 site 2 → 再执行」

原文对它的说明逐字是：

> This example shows how events can be inserted into a pattern and incrementally changed between test executions on a per site granularity. Three events (frc1V, frc2V, frc3Vmeas) drive a ramp, while only the second force voltage is measured via the third event (frc3Vmeas). In the example, the second event on site 2 is replaced by an event that additionally measures the first force voltage.

**把它摊成步骤**（每一步的行都在上面「语法 / 参数」节里）：

| # | 做什么 | 看哪一行 |
|---|---|---|
| 1 | 取 `PATTERN`，**先 `clear()` 清干净**，再**链式**插三个事件 | `pattern.vecEvents("Vdd1").clear().insert(100, frc1V).insert(200, frc2V).insert(300, frc3Vmeas);` |
| 2 | `patController.execute();` 执行 pattern，再 `results.uploadResult("Vdd1", TM::RESULT_INDEX);` | 同名两行 |
| 3 | `FOR_EACH_SITE_BEGIN()` 里逐 site `results.getValues("Vdd1", values);` | 循环块 |
| 4 | **存下当前 focus**（`GET_TEST_FOCUS(oldSites);`）→ `SET_TEST_FOCUS(2)` **选 site 2** | `if ( SET_TEST_FOCUS(2) )` |
| 5 | **改 focus 之后重新取一次 `VEC_EVENTS`**，然后 `remove(200).insert(200, EVENT_VFVM("frc2Vmeas").vForce(2 V));` | `VEC_EVENTS& site2_event(pattern.vecEvents("Vdd1"));` |
| 6 | **把 focus 还回去**（`SET_TEST_FOCUS(oldSites);`），再 `execute()` 一次并重新 upload | 同名几行 |

**这一趟里最值得记的两处，都在代码注释里**（注释是原文的）：

| 注释（逐字） | 读出来的事 |
|---|---|
| `GET_TEST_FOCUS(oldSites); // Get current setup-focused sites` | **改 focus 之前先把旧的存下来**——因为待会儿要还原 |
| `SET_TEST_FOCUS(oldSites); // Restore setup sites` | **改完必须还回去**；`SET_TEST_FOCUS(2)` 的返回值被当成条件用（**site 2 不可用时那一块不执行**） |

**第 5 步是「改 focus 后必须重新取」那条规则的现场执行**：**同一个 `pattern` 对象，
再调一次 `vecEvents("Vdd1")`**——而不是接着用上面那个引用。

### Example 2：`clearAll()` 的三条点

原文的说明（注意它自己带了警告）：

> This example demonstrates the use of the `clearAll()` member function. Be careful! It removes all events, independent of whether they were defined by the API or manually.

**例子的注释里还有两条原文没在别处写过的**——它们**分两块**，
中间隔着 `vecEvents.setup();` 这一行代码（那一行在「语法 / 参数」节里，本页不重引）：

> // Execute the removal step.
> // Actually you may have also new events defined before the setup() call.
> // Then the events will first be removed and the new ones will be defined afterwards.

**然后是 `vecEvents.setup();`**，之后又一段注释：

> // Instead of calling vecEvents.setup() you may also only call pc.setup(),
> // which will do the changes for all patterns at once. In this example here
> // the deletion of the events has happened already during vecEvents.setup().
> // Therefore pc.setup() has no effect and will be an NOP.

**两块合起来读成三件事**：

| # | 事 |
|---|---|
| 1 | **`clearAll()` 只是「记账」**，真正删发生在 `setup()` / `PATTERN_CONTROLLER::setup()` / `execute()` |
| 2 | **在 `setup()` 之前先定义新事件是允许的**——**先删后加**（`the events will first be removed and the new ones will be defined afterwards`） |
| 3 | **`pc.setup()` 会把所有 pattern 一起处理**；但如果删除已经在 `vecEvents.setup()` 时发生了，**`pc.setup()` 就是 NOP** |

**选 `clear()` 还是 `clearAll()`，本篇给的信息只有一条**：
**要不要连「手工加的事件」一起删**（`clear()` 是 `defined by this API`，
`clearAll()` 是 `independent of whether they have been defined by this API or manually`）。
**别的取舍（性能、副作用）语料未写。**

### Example 3：只是一句指路

> For an example that shows how to program an setup per site by DC events, refer to DC event example: Setup per site.

**指的那一篇本页没读**（raw：`../../03_Use_cases_and_application_papers/03.05_How_to_set_up_a_dynamic_DC_test/03.05.02.04_DC_event_example__Setup_per_site.md`）。
**所以「按 site 分别做 setup 的完整例子」本页没有。**

## 和谁有关

- [[pattern]] — **stage 页，也是本页 `stage: pattern` 的理由。** 它那一页在 L2 一节里
  只给了本页**一行**：`[[vec-events]]（L2）— 向量事件。`——**它是那一节里唯一没带 raw 路径的一行**
  （别的行都带 `02.07.04.01.xxx`）。**所以本页与 stage 页之间没有更多可讲的**，
  那条流程不在本页（§2.2）。
- [[pattern-object]] — **本类的唯一入口**：`VEC_EVENTS` 由 `PATTERN` 维护
  （原文 `is maintained by the PATTERN instance`），例子里每一个 `vecEvents("Vdd1")` 都是 `PATTERN` 的
  成员函数。那一页记着两件与本页直接相关的事：① `vecEvents()` 返回的引用
  **在 `label()` 改 pattern 或下一次 `vecEvents()` 调用时失效**；② Example 3 把
  `vecEvents` + `insert` + `pc.setup()` 整段包在 [[on-first-invocation-begin]] / [[on-first-invocation-end]] 里。
  **本页没有读那一篇的 raw**，这两条是「那一页的记载」。
- [[pattern-controller]] — **`clearAll()` 的延期删除有三个触发点，其中两个是它的成员函数**
  （`PATTERN_CONTROLLER::setup()` / `PATTERN_CONTROLLER::execute()`）；Example 2 里那个
  `pc` 就是它。**本页没有读那一篇的 raw**，所以 `setup()` 与 `execute()` 各自还做什么，本页没有。
- [[event-base]] — **`insert()` 与 `update()` 的形参类型**（`const EVENT_BASE & event`）；
  原文把它写成基类名，**本页没有读那一篇**，所以「`EVENT_BASE` 下面有哪些子类」本页一个字都没有。
- [[event-value-int]] / [[event-value-double]] / [[event-waveform-vfim]] / [[event-waveform-vfvm]] —
  **同一族的兄弟页**。本页 raw 的 `## Related information` 点的是那一族的**索引**
  （`EVENT_... (DC events API reference)`，raw：`02.07.04.01.63_EVENT_...__DC_events_API_reference.md`），
  **不是这几个具体类**。**⚠️ 例子里的 `EVENT_VF` / `EVENT_VFVM` 与这几页的名字对不对得上，本篇没有写**
  （页名里带 `WAVEFORM`，例子里的类型名不带）——**本页不据此声称它们是同一个类。**
- [[dc-result-accessor]] — 例子里 `DC_RESULT_ACCESSOR results;` 与
  `results.uploadResult("Vdd1", TM::RESULT_INDEX);` / `results.getValues("Vdd1", values);` 都是它的。
  **本篇只用了它，没有解释它**；**本页没读那一篇的 raw**，所以 `TM::RESULT_INDEX` 之外还有哪些取值、
  `getValues` 的完整签名本页都没有。
- [[on-first-invocation-begin]] / [[on-first-invocation-end]] — **Example 1 与 Example 2 的整段代码
  都包在这一对里**（`ON_FIRST_INVOCATION_BEGIN();` 到 `ON_FIRST_INVOCATION_END();`）。
  **本篇没有一句解释这个块**——为什么这套编辑要放在第一次调用时，**本页答不出来**，见那两页。
- [[for-each-site-begin]] / [[for-each-site-end]] — 原文那句 `FOR_EACH_SITE_XXX() loops` 的落点；
  Example 1 里用的是 `FOR_EACH_SITE_BEGIN()` 到 `FOR_EACH_SITE_END()`。
  **本页没读那两篇 raw**，所以「它和 `SET_TEST_FOCUS` 怎么配合」本页没有。
- [[dc-scale-xps256-card]] / [[dc-scale-uhc4t-card]] — **`Only DC Scale cards support this kind of events.`
  那句的落点**（本 wiki 里 DC Scale 那一族的两张卡）。
  **本篇只写了 `DC Scale cards` 这个词，没有点任何卡名**——**按页名并列，不代表它枚举过这些卡。**
- [[site-focus-required-before-command]] / [[controlling-multiple-sites]] — **site focus 主题的邻近页**。
  本页那条「改 focus 后必须重新取 `VEC_EVENTS`」是同一主题在 L2 侧的一条；
  **两页的 raw 本页都没读**——**按主题并列，不代表同物。**
- [[dc-test-programming]] — 本类操作的 `DC Scale` 事件属于 DC 测试那一段；
  **本篇没有点名它**，**本页也没有读那一篇**。
- [[mapping-pattern]] — **pattern 那一段的跨层对照表**。**我核过它那一页：它里面没有 `VEC_EVENTS`
  这个词**（本页 raw 也没有提它）——所以**两页之间没有文档写的关系**，这里只记「同 stage」。
- [[smartest-6.5.2]] / [[smartest-6.5.4]] — **版本页**：本篇 `## Functional changes` 两条的落点。
- `SET_TEST_FOCUS()` / `GET_TEST_FOCUS()`（**均未建**，也不在 allowlist）— 原文点名的 focus 操作。
  **本篇没有给它们任何一个的 raw 路径**（原文只写了函数名），**本页也没有去别处查**——
  所以**它们各自要几个参数、返回什么**，本页一个字都没有。

## 版本

本文档有 `## Functional changes` 段，**两条**：

- `Introduced in SmarTest 6.5.2`
- `SmarTest 6.5.4: New member function with 6.5.4.9: clearAll()`

**两条都已收进版本页**（我核过：[[smartest-6.5.2]] 与 [[smartest-6.5.4]] 各收了本页一条）。

**第一条是正常的 `Introduced in`，不是 §11.2 ② 那个 `Introduced before` 哨兵**——
**所以它照字面读**：**6.5.2 之前没有这个类**。

**第二条要说三件事**：

| 项 | 说清 |
|---|---|
| **它说的是 `clearAll()`** | **只有这一个成员函数是 6.5.4 才有的**——**别的七个在 6.5.2 上就有**（这一点是本页把两条版本行对齐成员函数表读出来的，**原文没有一句话这么说**，故标（推断），依据是「第二条只点了 `clearAll()` 一个名字」）。 |
| **`with 6.5.4.9` 这个措辞奇怪** | 逐字是 `New member function with 6.5.4.9: clearAll()`——**`6.5.4.9` 是什么（补丁号？内部版本？）本篇没有解释**。**照录，不替它改**（见「出处」⚠️④）。 |
| **`clearAll()` 之前怎么办** | **本篇没有说 6.5.4 之前的人用什么替代**——语料未写。 |

**「没记录」不等于「没改过」**：两条之后**本篇没有别的版本行**，
所以**「6.5.4 之后它改了没有」本页答不出**。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.267_VEC_EVENTS.md`
（TDC `116944.htm`，230 行 / 7,239 字节）。**整篇读完。**

**本页没做的：**

- **`## Related information` 三篇一篇都没读**：`PATTERN`（`02.07.04.01.142.01`）、
  `PATTERN_CONTROLLER`（`02.07.04.01.142`）、`EVENT_... (DC events API reference)`（`02.07.04.01.63`）。
  **这是本页最大的缺口**：本类的入口（`PATTERN`）、延期删除的触发点（`PATTERN_CONTROLLER`）、
  以及**事件的类型族**都在那三篇里——**本页只能给「例子里出现的名字」**。
  （本 wiki 有 [[pattern-object]] / [[pattern-controller]] / [[event-base]] 等页，
  **那是别的批次建的，本页没有读它们的 raw**。）
- **Example 3 指的那一篇没读**：
  `03_Use_cases_and_application_papers/03.05_How_to_set_up_a_dynamic_DC_test/03.05.02.04_DC_event_example__Setup_per_site.md`
  ——**「按 site 做 setup」的完整例子本页没有。**
- **`SET_TEST_FOCUS` / `GET_TEST_FOCUS` / `FOR_EACH_SITE_*` / `ON_FIRST_INVOCATION_*`
  / `DC_RESULT_ACCESSOR` / `EVENT_VF` / `EVENT_VFVM` 的 raw 一篇都没读**——
  （其中 `FOR_EACH_SITE_BEGIN` / `ON_FIRST_INVOCATION_BEGIN` 与 `DC_RESULT_ACCESSOR`
  这三族**在 wiki 里另有页**，见「和谁有关」；另外几个名字**没有页**。）
  例子里每一个非本类的东西，本页都只给了名字。**那串代码照抄能跑不能跑，本页答不出来。**
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** 没在任何机台上插过一条 DC event，也没验证过
  「改 focus 后不重新取 `VEC_EVENTS` 会怎样」「`clear()` 到底什么时候生效」。
  `verified: doc-only` 指的就是这件事。
- **本文档没有 `## Procedure` / `## Before you begin` / `## Important points` 段**——
  上面「典型用法」里那几张表是**本页按三个 Example 与成员函数说明排出来的**，
  **不是文档给的编号流程**；**例子里的代码与注释都是原文逐字（已在「语法 / 参数」节里）。**
- **`reinsert()` 在三个 Example 里一次都没出现**——**它只有那一句说明**，
  所以「什么时候该用 `reinsert` 而不是 `insert`」本页只有原文那一句前置条件，**没有例子**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`Note` 和正文挤在一行**：`Note Only DC Scale cards support this kind of events.`
> ——**原文如此**（HTML 转 markdown 时标签被拍平了）。本页引它时**照原样连 `Note` 一起引**。
> ② **`Parameters` 那张小表位置错乱，而且表内有两处对不上**：
> 表贴在 `remove(const STRING & eventId)` 说明的**末尾**（在 `clear()` 之前），
> 表里两行逐字是 ` | vector  | Existing test point |` 与 ` | eventID  | ID of an existing event  |   clear()`——
> **(a) 参数名 `eventID` 与签名里的 `eventId` 大小写不一致**；
> **(b) `vector` 那一格的说明写的是 `Existing test point`**（拿 test point 去解释 `vector`）；
> **(c) `clear()` 这个函数名被粘在了第二行的末尾**（原文如此）。
> **三处本页都照录，不替它改、也不替它猜。**
> ③ **`Both, event and test point will be created.`** —— `Both` 后面那个逗号是原文的
> （正常写法不该有）。**照录。**
> ④ **`If the event has been inserted multiple times at different, vectors, all these locations will be affected.`**
> —— `at different, vectors` 里 `different` 后面多了一个逗号。**照录。**
> ⑤ **`For an example that shows how to program an setup per site by DC events` 这一句里
> **`an setup` 应为 `a setup`**。**照录**（这一句本页在「典型用法」里逐字引了，
> **引文里没有替它改**）。
> ⑥ **版本行 `SmarTest 6.5.4: New member function with 6.5.4.9: clearAll()` 里的 `6.5.4.9` 没有解释**
> ——**它是什么版本号本篇未写**。**照录**。
> ⑦ **`clearAll()` 那句里由 `at the next call of` 引出的三个触发点，有两个是别的类的成员函数**
> （`PATTERN_CONTROLLER::setup()` / `PATTERN_CONTROLLER::execute()`），
> **而 `PATTERN_CONTROLLER` 那篇不在本篇的 `sources` 里**——**本页只能照引，不能展开。**
> ⑧ **例子里 `pc.label("pat1", "@")` 的第二个实参 `"@"`，本篇没有解释**
> （Example 1 用的是 `patController.label("myRamp")`，**只有两个参数的那个写法**）。
> **同一成员函数的两种调用形态出现在同一篇里，而原文只解释了其中一个**——
> **本页不猜 `"@"` 的含义。**
> ⑨ **例 1 代码块末尾那几行三点省略号是原文自己写的**（块尾那几行），**不是本页加的省略号**。
> ⑩ **本篇没有坏字。** 实测全文 **0 处非 ASCII 字符**（没有 `鈥` / `渭` / `碌` 那一族）。
> **但这是「本页量过的」**，判据是本篇这一个文件；§11.2 ① 那族在别的篇里大量存在。
> ⑪ **wiki 内部的一处口径过时**（**不是 raw 的错，是本 wiki 自己的**，记在这里免得下一个人
> 拿它去「补」错）：[[event-value-int]] 那一页把 [[vec-events]] 记成「**未建**」，
> **而本页已经建了**。**本页只记这件事，不去改那一页**
> （按 §13.1 第 ⑥′，改判要带证据；那一页的 raw 本页没读）。

`verified: doc-only`——**本页没有在任何真实机台上插过一条 DC event**
（§11：文档里有 ≠ 这台机器上能用；尤其「`clear()` 何时生效」与「改 focus 后不重新取会怎样」，
**文档没写清，动手前先照实机核对**）。
