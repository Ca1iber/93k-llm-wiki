---
type: object
title: DPS_AUX_TASK
layer: L2
stage: level
tags: [dps-aux-task, l2, dps, dc-scale, surge-tracker, tmu, task, test-method-api, xps256, dps128-dps64, smartest-7.2.1]
related: [dps-aux-pin-task, task-list, dps-task, spmu-task, dps128-dps64-cards, dc-scale-xps256-card, dps-power-flags-get-functions, test-method-class, universal-test-method-library, smartrdi, smartrdi-tmu-test-setup, on-first-invocation-begin, for-each-site-begin, for-each-site-end, level, smartest-7.2.1, smartest-7.3.1, smartest-7.4.0, smartest-7.5.0]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43_DPS_AUX_TASK.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# DPS_AUX_TASK

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,197 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43_DPS_AUX_TASK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
DPS_AUX_TASK();
```

Creates an object of the DPS_AUX_TASK class.

Note Do not create static objects of the class in the test method and do not create test method member variables from this class.

List of parameters

There are no parameters.

### Return value

The constructor has no return value.

### Example 1

The example below sets current thresholds, activates the surge tracker, checks the status against the current thresholds, and retrieves the result.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Set the current thresholds to -1 mA/1 mA and switch on surge tracker
    //
    auxTask.pin("dps1")
        .selectISensorSetThresholds(-1 mA, 1 mA)
        .setMode(TM::SURGE_TRACKER);

    auxTask.execute();

    auxTask.pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH);

ON_FIRST_INVOCATION_END();

//
// Get the result of surge tracker
//
TM::SURGE_TRACKER_STATUS surgeTrackerStatus = auxTask.getSurgeTrackerStatus("dps1");

switch (surgeTrackerStatus)
{
    case TM::SURGE_TRACKER_NONE_DETECTED:

        cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_NONE_DETECTED"
             << endl << endl;

        break;

    case TM::SURGE_TRACKER_HIGH_DETECTED:

        cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_HIGH_DETECTED"
             << endl << endl;

        break;

    case TM::SURGE_TRACKER_LOW_DETECTED:

        cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_LOW_DETECTED"
             << endl << endl;

        break;

    case TM::SURGE_TRACKER_BOTH_DETECTED:

        cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_BOTH_DETECTED"
             << endl << endl;

        break;

    default:

        break;
};
```

### Example 2: Site鈥憇pecific thresholds for XPS256

The example activates both the voltage surge tracker and the current surge tracker of an `XPS256`（raw: `../02.02_Specifications/02.02.05.03_DC_Scale_XPS256_Universal_DPS_VI_Card.md`） pin. Common thresholds are defined in the `ON_FIRST_INVOCATION`（raw: `02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md`） block and replaced with site鈥憇pecific thresholds in the `FOR_EACH_SITE`（raw: `02.07.04.01.70_FOR_EACH_SITE_BEGIN.md`） loop.

To prevent `DPS_AUX_PIN_TASK.setMode()`（raw: `02.07.04.01.43.01.07_DPS_AUX_PIN_TASK.setMode.md`） from issuing a warning, this function is called only outside the FOR_EACH_SITE loop. `RDI_INIT()`（raw: `02.07.13.08.01.06_RDI_INIT.md`） is used at the very beginning as a prerequisite of the `SmartRDI`（raw: `02.07.13_SmartRDI.md`） code to be implemented for the DUT test. The surge tracker results are read within another FOR_EACH_SITE loop to comply with requirements of SmartRDI.

```
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
    DPS_AUX_TASK auxTask;

    //
    // Setup surge tracker
    //
    double vThresholdLow    = -0.5 V;
    double vThresholdHigh   =  3.5 V;
    double iThresholdLow    = -0.1 A;
    double iThresholdHigh   =  0.4 A;

    auxTask.pin("XPS256_PMU_1")
        .setMode                    (TM::SURGE_TRACKER)
        .selectVSensorSetThresholds (vThresholdLow, vThresholdHigh)
        .selectISensorSetThresholds (iThresholdLow, iThresholdHigh);

    FOR_EACH_SITE_BEGIN();
    {
        //
        // Set site specific thresholds
        //
        ...
        ...

        //
        // Apply site specific thresholds
        //
        auxTask.pin("XPS256_PMU_1")
            .selectVSensorSetThresholds (vThresholdLow, vThresholdHigh)
            .selectISensorSetThresholds (iThresholdLow, iThresholdHigh);
    }
    FOR_EACH_SITE_END();

    auxTask.execute();

    //
    // Setup and execute the DUT test
    //
    ...
    ...

    //
    // Check the state of the surge tracker for all sites
    //
    auxTask.pin("XPS256_PMU_1").checkSurgeTracker(TM::AGAINST_BOTH);

    FOR_EACH_SITE_BEGIN();
    {
        TM::SURGE_TRACKER_STATUS statusVoltage, statusCurrent;

        auxTask.getSurgeTrackerStatus("XPS256_PMU_1", statusVoltage, statusCurrent);

        cout << "Site " << CURRENT_SITE_NUMBER() << ", Voltage surge tracker: " << statusVoltage << endl;
        cout << "Site " << CURRENT_SITE_NUMBER() << ", Current surge tracker: " << statusCurrent << endl;
    }
    FOR_EACH_SITE_END();
}
ON_FIRST_INVOCATION_END();
```

<!-- 语法节 end -->

## 是什么

**`DPS_AUX_TASK` 是一个 C++ 类（L2 / Test Method API）：管**DC Scale 卡的 surge tracker 和 TMU**。**
原文定义句（逐字）：

> 「The DPS_AUX_TASK class controls the surge tracker and the TMU (Time Measure Unit) of DC Scale cards.」

**三个要点**：

| 格 | 原文 | 说明 |
|---|---|---|
| **它管什么** | `controls` | **不是「读」也不是「配一次」——原文用的是 `controls`** |
| **管哪两样** | `the surge tracker and the TMU (Time Measure Unit)` | **两样，不是一样** |
| **管谁的** | `of DC Scale cards` | **作用域是 DC Scale 卡**（不是所有卡） |

**它是**父类**：本篇的 `#### Subtopics` 里第一条就是 `DPS_AUX_PIN_TASK`，
而 [[dps-aux-pin-task]] 已有自己的一页**。
**（推断）两者的分工是「一个 task 对象管一批 pin」与「一个 pin」两档**——
**依据只是「父类叫 `DPS_AUX_TASK`、子主题叫 `DPS_AUX_PIN_TASK`」这个名字层级，
以及例子里的方法都是 `auxTask.pin("dps1").<方法>()` 这种「先选 pin 再操作」的形态；
原文没有一句话说明两类的继承关系或分工。** **本页没读 [[dps-aux-pin-task]] 那一页。**

### 支持哪些卡：原文是一张两行的名单

原文（逐字）引出：

> 「Supported DC Scale cards:」

| 功能 | 支持的卡（**原文逐字**） |
|---|---|
| **Surge tracker** | `DPS128/DPS64` 和 `XPS256`（**原文两条各是一个链接**） |
| **TMU (Time Measure Unit)** | `Currently not supported by any card.` |

**⚠️ 这张表有两处要留意**：

1. **TMU 那一行是「目前没有任何卡支持」**——
   **即：类定义里写它管 TMU，而 TMU 这一半目前没有硬件可用。**
   （**原文用 `Currently` 这个词**，所以它是一句有时效的话。
   **智能卡是否后来支持了 TMU，本篇没有说**——**版本段里也没有 TMU 条目**，见 `## 版本`。）
2. **版本段里出现了三个这张表里没有的卡**：`PVI8`（7.3.1）、`AVI64`（7.4.0）、
   `FVI16`（7.5.0）——**它们都写着 `card added`，而 `Supported DC Scale cards` 这两行里
   一个都没有。** **原文没有说这几张卡支持的是 surge tracker 还是 TMU，也没有说
   两处为什么对不上。本页并列，不替它合成一张表**（见 `## 出处`）。

### 它是一个 TASK：可以和别的 TASK 类一起进 TASK_LIST

原文两句（逐字）：

> 「The DPS_AUX_TASK can be added to TASK_LIST and work with other TASK-type classes.」

**`TASK_LIST` 是原文里的一个链接**（raw：`02.07.04.01.240_TASK_LIST.md`，[[task-list]]）。
——**所以它不是一个孤立的查询 API：它能和其它 TASK 型类排在一个清单里一起跑。**
**本页没读 [[task-list]]**，**所以「排进去之后谁调谁、顺序怎么定」，本页不知道。**

### 定义在哪个头文件

原文一句（逐字），**这是本页唯一一条「去哪儿找它」的硬信息**：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/DpsAuxTask.h.」

**路径逐字是 `/opt/hp93000/soc/prod_com/include/MAPI/DpsAuxTask.h`**——
**`hp93000` 全小写、头文件名是驼峰式 `DpsAuxTask.h`**。
**本页只保证「与原文逐字一致」**（§11.2 ⑥ 的判据：这类拿去做自动化输入的串
不能靠检查发现，只能回原文核）；**本页没有机台可核，所以不保证这个路径在机台上存在。**
**它下面的 `prod_com` / `MAPI` 两个目录名也是原文的写法，本页照抄。**

### 构造：没有参数，但有一条硬规矩

语法节里（**逐字**）：

```
DPS_AUX_TASK();
```

**原文接的两句**：`Creates an object of the DPS_AUX_TASK class.` 与
`There are no parameters.` / `The constructor has no return value.`
——**即：无参、无返回值、只是建一个对象。**

**⚠️ 紧跟着的那条 `Note` 是本页最要紧的一条限制**（逐字，**注意 `Note` 与句子之间没有分隔符**）：

> 「Note Do not create static objects of the class in the test method and do not create test method member variables from this class.」

**拆成两条禁止**：

| # | 禁止（**原文**） | 管的是 |
|---|---|---|
| 1 | `Do not create static objects of the class in the test method` | **不许在 test method 里建静态对象** |
| 2 | `do not create test method member variables from this class` | **不许拿这个类做 test method 的成员变量** |

**两条合起来的后果**：**这个对象只能建在**局部**（例子里的 `DPS_AUX_TASK auxTask;`
就建在 `ON_FIRST_INVOCATION_BEGIN()` 之后、块内部）**——
**它的生命周期不能跨调用、不能跨 test method 存续。**
**⚠️ 原文没有说为什么**（是硬件状态会漂、还是线程/站点相关问题），**本页不替它猜。**
**test method 本身是什么结构，见 [[test-method-class]] / [[universal-test-method-library]]**
（**本页两页都没读**）。

### 怎么用：`pin()` 选 pin，链式设置，`execute()` 生效，再查结果

**从两个例子里能读出的调用形态**（**下面是本页把例子的语句排出来的，不是原文的步骤**）：

| 阶段 | 例子里那一行（**逐字**） | 说明 |
|---|---|---|
| 1 建对象 | `DPS_AUX_TASK auxTask;` | **局部对象**（对上那条 `Note`） |
| 2 选 pin + 设阈值 + 定模式 | `auxTask.pin("dps1").selectISensorSetThresholds(-1 mA, 1 mA).setMode(TM::SURGE_TRACKER);` | **链式**：`pin()` 返回的东西上继续挂设置方法 |
| 3 生效 | `auxTask.execute();` | **单独一句**（**链式那一串的最后没有 `execute()`**） |
| 4 对照阈值检查 | `auxTask.pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH);` | **再选一次 pin**（`pin()` 可以重复调） |
| 5 取结果 | `TM::SURGE_TRACKER_STATUS surgeTrackerStatus = auxTask.getSurgeTrackerStatus("dps1");` | **这一句在 `ON_FIRST_INVOCATION_END()` 之后** |
| 6 判结果 | `switch (surgeTrackerStatus)` 四个 `case` | **四个状态见下表** |

**第 5、6 步的四个状态值（逐字，来自例子里的 `case` 标签）**：

| 状态枚举（**原文**） | 例子里的输出文案（**逐字**） |
|---|---|
| `TM::SURGE_TRACKER_NONE_DETECTED` | `SURGE_TRACKER_NONE_DETECTED` |
| `TM::SURGE_TRACKER_HIGH_DETECTED` | `SURGE_TRACKER_HIGH_DETECTED` |
| `TM::SURGE_TRACKER_LOW_DETECTED` | `SURGE_TRACKER_LOW_DETECTED` |
| `TM::SURGE_TRACKER_BOTH_DETECTED` | `SURGE_TRACKER_BOTH_DETECTED` |

**（推断）前三个与第四个是「单个越限」与「两侧都越限」的区别**——
**依据只是这四个名字的字面（`NONE` / `HIGH` / `LOW` / `BOTH`）；
原文没有用一句话解释这四个状态。**
**`TM::AGAINST_BOTH` 与 `TM::SURGE_TRACKER` 这类枚举出现在参数位上，
而原文没有给它们的取值表**——**它们属于 [[dps-aux-pin-task]] 那一路的成员函数，
本页没读那页。**

### Example 2 里的三条时序规矩（**这是本页最接近「约束」的部分**）

**Example 2 的题头句（逐字，含坏字，见 `## 出处` ①）**：

> 「### Example 2: Site鈥憇pecific thresholds for XPS256」

**它的说明段给了三条规矩，都是「为什么这么写」**（逐字）：

> 「To prevent DPS_AUX_PIN_TASK.setMode() from issuing a warning, this function is called only outside the FOR_EACH_SITE loop. RDI_INIT() is used at the very beginning as a prerequisite of the SmartRDI code to be implemented for the DUT test. The surge tracker results are read within another FOR_EACH_SITE loop to comply with requirements of SmartRDI.」

**三条拆开**：

| # | 规矩（**原文**） | 条件 → 做法 |
|---|---|---|
| 1 | `To prevent DPS_AUX_PIN_TASK.setMode() from issuing a warning, this function is called only outside the FOR_EACH_SITE loop.` | **要避免 `setMode()` 报警告** → **只在 `FOR_EACH_SITE` 循环**外面**调它** |
| 2 | `RDI_INIT() is used at the very beginning as a prerequisite of the SmartRDI code to be implemented for the DUT test.` | **要用 SmartRDI 写 DUT 测试** → **`RDI_INIT()` 放在最开头**（原文说它是 `a prerequisite`） |
| 3 | `The surge tracker results are read within another FOR_EACH_SITE loop to comply with requirements of SmartRDI.` | **读结果** → **必须放在另一个 `FOR_EACH_SITE` 循环里**，理由是 SmartRDI 的要求 |

**三条的形态与 §2.4 的约束四形态对得上**（**这是本页的归类，不是原文的话**）：
**第 1 条是 D4（位置/归属：这个调用必须放在循环**外**）**，
**第 2 条是 D1（顺序前置：先 `RDI_INIT()`）**，
**第 3 条是 D4（位置：读结果必须在循环**里**）**。
**⚠️ 三条都写在**例子**的说明段里，不在 `## Predependencies` 里**——
**本篇没有 `## Predependencies` 段**（见 `## 出处`）。
**[[smartrdi]] 那一页没读；[[on-first-invocation-begin]] / [[for-each-site-begin]] /
[[for-each-site-end]] 那三页也没读**——**本页只写这三条规矩本身，
循环块怎么用、SmartRDI 是什么，都在那几页。**

**⚠️ 第 1 条与第 3 条是同一件事的两面，值得并排看**：
**同一个功能（surge tracker）的设置要写在 `FOR_EACH_SITE`**外**、读取要写在**里**——
**原文给的理由不一样**（一条是「避免警告」，一条是「SmartRDI 的要求」），
**而两条的理由都不是「功能上行不行」。**

### 七条子主题：这个类还有什么

原文 `#### Subtopics` 列了**七条**（**逐字**）：

- `DPS_AUX_PIN_TASK`（`.01`）
- `DPS_AUX_TASK.execute()`（`.02`）
- `DPS_AUX_TASK.pin()`（`.03`）
- `DPS_AUX_TASK.setup()`（`.04`）
- `DPS_AUX_TASK.getSurgeTrackerStatus()`（`.05`）
- `DPS power flags - get...() functions`（`.06`）
- `DPS status flags - get...() functions`（`.07`）

**这七条里，例子用到了三条**（`pin()` / `execute()` / `getSurgeTrackerStatus()`），
**另外四条本页没有材料**（**其中 `setMode()` 与 `checkSurgeTracker()` 这两个方法
在例子里出现了，但它们不在这七条清单里**——**见 `## 出处` ⑧**）。

**⚠️ `setup()` 一次都没有出现在例子里**：`DPS_AUX_TASK.setup()` 是子主题之一，
**而两个例子都只用了 `pin()` / `execute()` / `checkSurgeTracker()` / `getSurgeTrackerStatus()`。
原文没有说 `setup()` 什么时候必须调、和 `execute()` 什么关系。**
**（推断）从名字看它是「先做一遍设置」这一档，但依据只有名字——
原文没有一句话说明它，所以这是推断。**

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## Predependencies`**——
**可依据的是两个 `### Example` 的代码与说明段。**
**两个例子的取向不同**：**Example 1 是「一个 pin 的最小流程」，
Example 2 是「多站点 + XPS256 的完整形态」。**

| # | 要做的事 | 依据（**原文/例子里逐字**） |
|---|---|---|
| 1 | **要测 surge tracker** | `The DPS_AUX_TASK class controls the surge tracker and the TMU (Time Measure Unit) of DC Scale cards.` |
| 2 | **确认你的卡在名单里** | `Surge tracker: DPS128/DPS64 and XPS256`（[[dps128-dps64-cards]] / [[dc-scale-xps256-card]]） |
| 3 | **别指望 TMU** | `TMU (Time Measure Unit): Currently not supported by any card.` |
| 4 | **把对象建在局部**（两条禁止，见 `## 是什么`） | `Note Do not create static objects of the class in the test method and do not create test method member variables from this class.` |
| 5 | **在 `ON_FIRST_INVOCATION_BEGIN()` 块里建与设置** | Example 1：`ON_FIRST_INVOCATION_BEGIN();` … `DPS_AUX_TASK auxTask;`（[[on-first-invocation-begin]]） |
| 6 | **用 `pin("…")` 选 pin，链式挂设置** | `auxTask.pin("dps1").selectISensorSetThresholds(-1 mA, 1 mA).setMode(TM::SURGE_TRACKER);` |
| 7 | **`setMode()` 只在 `FOR_EACH_SITE` 外调** | `To prevent DPS_AUX_PIN_TASK.setMode() from issuing a warning, this function is called only outside the FOR_EACH_SITE loop.` |
| 8 | **调 `execute()` 让它生效** | `auxTask.execute();` |
| 9 | **用 `checkSurgeTracker(TM::AGAINST_BOTH)` 对阈值检查** | `auxTask.pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH);` |
| 10 | **取结果放在 `ON_FIRST_INVOCATION_END()` 之后** | Example 1：`getSurgeTrackerStatus("dps1")` 在 `ON_FIRST_INVOCATION_END();` 下一段 |
| 11 | **多个站点时，结果要在 `FOR_EACH_SITE` 里逐个读** | `The surge tracker results are read within another FOR_EACH_SITE loop to comply with requirements of SmartRDI.` |
| 12 | **要用 SmartRDI，`RDI_INIT()` 放最开头** | `RDI_INIT() is used at the very beginning as a prerequisite of the SmartRDI code…` |
| 13 | **要让任务和别的 TASK 一起排队** | `The DPS_AUX_TASK can be added to TASK_LIST and work with other TASK-type classes.` |

**Example 2 里多站点的写法（逐字，只摘形态）**：

```
auxTask.pin("XPS256_PMU_1")
    .setMode                    (TM::SURGE_TRACKER)
    .selectVSensorSetThresholds (vThresholdLow, vThresholdHigh)
    .selectISensorSetThresholds (iThresholdLow, iThresholdHigh);
```

**从这一串能看到的四件事**（**都比 Example 1 多**）：
① **`setMode()` 也能挂在链式里**（Example 1 是把 `setMode` 挂在最后一位）；
② **多一个电压侧方法 `selectVSensorSetThresholds()`**（Example 1 只有电流侧的 `…ISensor…`）；
③ **阈值可以先用 `double` 变量存好再传**（`double vThresholdLow = -0.5 V;` 等四行）；
④ **每个方法的括号前对齐了空格**（`(TM::SURGE_TRACKER)` 等**前面留了多空格对齐**）
——**那是原文的排版，照抄时不必模仿。**

**Example 2 的结果读取用的是一个带两个出参的重载**（逐字）：

```
TM::SURGE_TRACKER_STATUS statusVoltage, statusCurrent;

auxTask.getSurgeTrackerStatus("XPS256_PMU_1", statusVoltage, statusCurrent);
```

**即：`getSurgeTrackerStatus()` 有两种调用形态**——
**一个字符串取一个状态（Example 1）**，或**两个出参分别取电压侧与电流侧（Example 2）**。
**两种形态的声明、参数个数、返回类型，原文都没有给**（**只有这两个例子**）。

**没有的东西**：本篇**没有 `Errors` 段、没有 `Warnings` 段、没有 `Limits` 段、
没有 `## Application` 段、没有 `## Predependencies` 段**。
**⚠️ 但正文里提到了「会报警告」**——
`To prevent DPS_AUX_PIN_TASK.setMode() from issuing a warning…`
——**警告文本是什么、在哪儿显示、不理会会怎样，原文一个字都没有。**

## 和谁有关

- [[dps-aux-pin-task]] — **子类（本页是父类）**。原文 `#### Subtopics` 第一条就是它，
  `## Related information` 第一条也是它（raw：`02.07.04.01.43.01_DPS_AUX_PIN_TASK.md`）。
  而且 Example 2 的说明段里出现的就是它自己的方法：
  `To prevent DPS_AUX_PIN_TASK.setMode() from issuing a warning…`
  ——**即：`setMode()` 挂在 `DPS_AUX_PIN_TASK` 名下，而例子里是从 `auxTask.pin(...)` 链式调到的。**
  **（推断）这就是两个类的关系：`DPS_AUX_TASK` 管整批、`DPS_AUX_PIN_TASK` 管单个 pin；
  依据是名字层级 + 例子里 `pin()` 之后那串方法的名字归属于子类。**
  **本页没读 [[dps-aux-pin-task]]**，**所以 `setMode()` 的取值、参数的完整清单，本页没有。**
- [[task-list]] — **它进的那个清单**。原文：
  `The DPS_AUX_TASK can be added to TASK_LIST and work with other TASK-type classes.`
  （**`## Related information` 也链了它**）。**本页没读那页**：
  **怎么加、加了之后谁按什么顺序调，本页不知道。**
- [[dps128-dps64-cards]] / [[dc-scale-xps256-card]] — **支持名单上的两种卡**。
  原文那两行是 `Surge tracker: DPS128/DPS64 and XPS256`——
  **两个各是一个链接**。**本页只写「它们在名单上」**；
  **卡的通道数、能力、surge tracker 的硬件规格，在它们各自的页（本页都没读）。**
- [[dps-task]] / [[spmu-task]] — **（推断）同族的两个 TASK 类**。
  原文那句说的是 `work with other TASK-type classes`，**没有点名任何一个**；
  **依据只是这两个页名都是 `*-task`（`dps-task` / `spmu-task`）。
  本页没读那两页，也不声称它们能一起用。**
- [[dps-power-flags-get-functions]] — **子主题 `.06` 的去处**
  （`DPS power flags - get...() functions`，**原文自己列的子主题**）。
  而且 `## 版本` 里有一条与它直接相关：
  `SmarTest 7.4.0: New member functions returning the DPS_POWER_FLAG_STATUS.`
  **本页没读那页**；`.07`（`DPS status flags - get...() functions`）**本 wiki 里没有同名页**
  （**只有 `XPS256` 的 status flags 那一页，名字不同，本页不敢说它们是同一件东西**）。
- [[smartrdi]] — **（推断）Example 2 里那三条规矩的宿主**。
  说明段两次点 SmartRDI：`as a prerequisite of the SmartRDI code to be implemented for the DUT test`
  与 `to comply with requirements of SmartRDI`；
  **而 `RDI_INIT()` / `FOR_EACH_SITE` 那些东西属于 SmartRDI 那一套**。
  **本页没读 [[smartrdi]]**——**所以「为什么结果必须在 FOR_EACH_SITE 里读」，本页只有那句转述。**
- [[smartrdi-tmu-test-setup]] — **名字里带 TMU 的一页，本页要把它当易混项说清**：
  本页明写 `TMU (Time Measure Unit): Currently not supported by any card.`，
  **而那一页是关于 TMU 测试设置的**——**两者名字对得上，但本页没有依据说它们是同一件事
  （本页没读那页）。列在这里是为了防下一个人拿它来「补」本页的 TMU 那一行。**
- [[on-first-invocation-begin]] / [[for-each-site-begin]] / [[for-each-site-end]] —
  **两个例子里包裹调用的三个块**（原文写的是 `ON_FIRST_INVOCATION` / `FOR_EACH_SITE`，
  **句子里的名字是简写、没有 `_BEGIN` / `_END` 后缀**）。
  **本页只写「哪一句该放在块里还是块外」**；**块本身的语义与用法在那三页（本页都没读）。**
- [[test-method-class]] / [[universal-test-method-library]] — **（推断）那个 `Note` 的语境**。
  两条禁止都写着 `in the test method` / `test method member variables`，
  **而「test method 是什么结构」在那两页**。
  **依据是那两句原文里的 `test method` 这个词组与这两页的名字。本页没读那两页。**
- [[level]] — **stage 页，最近的一段**（本页 `layer: L2`、`stage: level`）。
  **§6：`stage` 填的是「读者该去哪一段找它的用法」，不是「归属」**——
  **本页是 DC Scale 卡的 API，最近的一段是 level；本页不写流程叙述。**
- [[smartest-7.2.1]] / [[smartest-7.3.1]] / [[smartest-7.4.0]] / [[smartest-7.5.0]] — **版本页**，
  本页 `## 版本` 那八条条目的落点。
- `DPS_AUX_TASK.setup()` / `DPS_AUX_TASK.pin()` / `DPS_AUX_TASK.execute()` /
  `DPS_AUX_TASK.getSurgeTrackerStatus()` / `DPS status flags - get...() functions`（**均未建**）——
  **原文 `#### Subtopics` 里的五条**（前四条是同一个类的成员函数页）。
  **本页没有它们任何一条的内容**：**签名、参数、返回值全在那五篇里。**
- `TM::` 命名空间（**未建**）— **例子里所有枚举的归属**（`TM::SURGE_TRACKER`、
  `TM::AGAINST_BOTH`、`TM::SURGE_TRACKER_*`）。**原文没有解释 `TM` 是什么。**

## 版本

本文档**有** `## Functional changes` 段，**八条**（**逐字**）：

- **Introduced in SmarTest 7.2.1**
- **SmarTest 7.3.1: DC Scale PVI8 card added.**
- **SmarTest 7.4.0: DC Scale AVI64 card added.**
- **SmarTest 7.4.0: New member functions DPS_AUX_TASK.getBatteryFull().**
- **SmarTest 7.4.0: New member functions DPS_AUX_TASK.getPowerBudgetWarningAll().**
- **SmarTest 7.4.0: New member functions DPS_AUX_TASK.getPowerBudgetWarning1(), ...Warning2(), and ...Warning3().**
- **SmarTest 7.4.0: New member functions returning the DPS_POWER_FLAG_STATUS.**
- **SmarTest 7.5.0: DC Scale FVI16 card added.**

**第一条不是 §11.2 ② 那个哨兵**（哨兵写 `Introduced before SmarTest 6.3.2`）——
**`Introduced in SmarTest 7.2.1` 是常规引入条目：`DPS_AUX_TASK` 在 SmarTest 7.2.1 引入。**

**这八条能读出三件事**（**都是条目里直接写的**）：

| 读出的 | 依据 |
|---|---|
| **7.4.0 是它的功能大年**：六条里五条是 7.4.0 | 五条 `SmarTest 7.4.0:` 条目 |
| **7.3.1 / 7.4.0 / 7.5.0 各加了一张卡** | 三条 `card added` 条目 |
| **7.4.0 加了六个成员函数**（`getBatteryFull()` / `getPowerBudgetWarningAll()` / `…1()` / `…2()` / `…3()` / 返回 `DPS_POWER_FLAG_STATUS` 的那些） | 那三条 `New member functions` 条目 |

**⚠️ 三条 `card added` 与正文那张支持名单对不上**——**这是本页唯一一处「版本段与正文冲突」**：

| 卡 | 版本段说的 | 正文 `Supported DC Scale cards` 里 |
|---|---|---|
| `PVI8` | 7.3.1 `card added` | **没有** |
| `AVI64` | 7.4.0 `card added` | **没有** |
| `FVI16` | 7.5.0 `card added` | **没有** |

**两种可能，原文都没排除**：
**(a) 正文那张名单只列了「surge tracker / TMU 两种功能」的支持者，而这三张卡加的是别的功能；**
**(b) 正文那张名单没跟着版本更新。**
**本页 (a)(b) 并列，不判哪个对**（§10：两份说法不一致时不许自行选一个）。

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**7.2.1 / 7.3.1 / 7.4.0 / 7.5.0 都早于 7.10.3**——
**按文档的说法，上面八条在目标版本上都已经在**。
**注意 §11**：这只说明**文档这么写**，**不说明某台机台上能用、也没在机台上验过**
（本页 `verified: doc-only`）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43_DPS_AUX_TASK.md`

**本页没做的：**

- **只读了这一篇。七个 `#### Subtopics` 一条都没读**：
  `DPS_AUX_PIN_TASK` / `.execute()` / `.pin()` / `.setup()` / `.getSurgeTrackerStatus()` /
  `DPS power flags - get...() functions` / `DPS status flags - get...() functions`。
  **这是本页最大的空缺**：**每个方法的签名、参数、返回值、报错，全在那七篇里**；
  **本页只有例子里出现过的调用形态。**
- **[[dps-aux-pin-task]] 没读**——**所以 `setMode()` / `selectISensorSetThresholds()` /
  `selectVSensorSetThresholds()` / `checkSurgeTracker()` 这四个在例子里出现的方法，
  本页一个签名都没有**（**而且其中前三个不在这篇的七条子主题里**，见 ⑧）。**
- **`TM::` 命名空间没查**——**所以 `TM::SURGE_TRACKER` / `TM::AGAINST_BOTH` /
  `TM::SURGE_TRACKER_*` 的取值表，本页一个字都没有。**
- **[[task-list]] 没读**——**所以「加进 TASK_LIST 之后怎么跑」，本页只有那一句原文。**
- **[[smartrdi]] 没读，`RDI_INIT()` 那篇也没读**——
  **所以 Example 2 那三条规矩里 SmartRDI 那一侧的「为什么」，本页只能转述那一句。**
- **没有在机台上试过**：**没有建过 `DPS_AUX_TASK` 对象、没有触发过 surge tracker、
  没有见过那条「`setMode()` 的警告」长什么样**（本页 `verified: doc-only`）。
- **没有查过那三张版本段里出现的卡**（`PVI8` / `AVI64` / `FVI16`）——
  **它们支持的是哪种功能、为什么不在名单里，本页和原文一样没有答案。**
- **一张图都没看。** 本篇**没有图片引用**（`![` 0 处，本页核过）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：本页把三条时序规矩按 §2.4 的形态归了类（D4/D1/D4），
  那是本页的归类，原文没有用那套术语。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 本篇有 §11.2 ① 那种编码损坏，共 2 处。** 逐字：
> `### Example 2: Site鈥憇pecific thresholds for XPS256`（**标题里**）
> 与正文里的 `replaced with site鈥憇pecific thresholds in the FOR_EACH_SITE loop`。
> **坏字是 `鈥憇`**——它属于 §11.2 ① 里「**三字节的（第三个字节已丢，只能给区间）**」那一族：
> `鈥` 是某个 U+2000–U+203F 区间的字符的头两个字节，
> **而且紧跟其后的 ASCII 字母被并进了第二个坏字**（`憇` 里含着那个字母）。
> **所以原词应是 `Site` + 该字符 + `specific`**（**最可能是 U+2011 非断行连字符**），
> **但按 §11.2 的规矩，这一类只许报「它落在这个区间」，不许当映射用。**
> **⚠️ 拿它去搜时会踩到那个被吞掉的字母**：**`specific` 是搜不到的，要搜 `pecific`**；
> **本页引文照原样保留 `鈥憇`，不替它改字、也不替它补字母。**
>
> **② `DPS128/DPS64` 那个链接的文字与文件名对不上。** 逐字：链接文字是
> `DPS128/DPS64`，而它的链接目标是
> `02.05.05.01.03_DPS128____PS64_functionality_and_features.md`
> ——**文件名里那一截写的是 `PS64`（少了一个 `D`），而且用四个下划线代替了 `/`。**
> **两处在同一行里，原文没有说明哪个对。本页照实记**
> （**顺带一提：本 wiki 那一页的标题是 `DC Scale DPS128/DPS64 cards`，
> 与链接文字一致**）。
>
> **③ 「支持的卡」与版本段对不上（三条 `card added` 的卡不在名单里）。**
> 逐字并列：`Supported DC Scale cards:` 下面只有
> `- Surge tracker: DPS128/DPS64 and XPS256` 与 `- TMU (Time Measure Unit): Currently not supported by any card.`
> 两行，而版本段里有 `SmarTest 7.3.1: DC Scale PVI8 card added.` /
> `SmarTest 7.4.0: DC Scale AVI64 card added.` / `SmarTest 7.5.0: DC Scale FVI16 card added.`。
> **本页并列两处，不替它合成一张表、也不替它判谁过时**（见 `## 版本`）。
>
> **④ `Note` 与它后面的句子之间没有分隔符，而且 `Note` 前没有换行标记。** 逐字：
> `Note Do not create static objects of the class in the test method and do not create test method member variables from this class.`
> ——**`Note` 后面直接跟空格和正文**，没有冒号、没有加粗。
> **本页照原样引。**
>
> **⑤ `List of parameters` 是一个裸词行，既不是标题也不是列表项。** 逐字：
> `List of parameters` 单独一行，**下一段才是 `There are no parameters.`**
> ——**它在结构上与后面的段落没有从属关系**（**和 `dscp` 那篇的 `returns:` 是同一类问题**）。
> **语法节里看得见（`语法节` 逐字抽了这一段），本页照实记。**
>
> **⑥ `#### Subtopics` 的标题层级与同一篇里其它标题不一致。** 逐字：本篇的标题是
> `# DPS_AUX_TASK` / `#### Subtopics` / `## Syntax` / `## Return value` / `## Examples` /
> `### Example 1` / `### Example 2: …` / `## Related information` / `## Functional changes`
> ——**`Subtopics` 用了四级（`####`）**，而它前后是 `#` 与 `##`。
> **层级跳了两级。本页照实记。**
>
> **⑦ 头文件路径本页照抄了原文，抄写时要当心。** 逐字：
> `/opt/hp93000/soc/prod_com/include/MAPI/DpsAuxTask.h`
> ——**本页核过：这一行与原文逐字一致**（原文里就是这么写的）。
> **⚠️ 本页把它单列一条，是因为这类路径**拿去做自动化输入**时最怕抄错
> （§11.2 ⑥ 的判据：不能靠编码检测发现，只能回原文核）；
> **本页没有机台可核，所以只保证「与原文一致」，不保证「在机台上存在」。**
>
> **⑧ 例子里有三个方法不在 `#### Subtopics` 清单里。** 逐字：例子用了
> `selectISensorSetThresholds()` / `setMode()` / `checkSurgeTracker()`，
> **而子主题七条里没有它们的页**（七条是 `DPS_AUX_PIN_TASK` / `.execute()` / `.pin()` /
> `.setup()` / `.getSurgeTrackerStatus()` / `DPS power flags…` / `DPS status flags…`）。
> **（推断）它们属于子类 `DPS_AUX_PIN_TASK`，所以挂在那一条子主题底下——
> 依据是 Example 2 的说明段写的是 `DPS_AUX_PIN_TASK.setMode()`。**
> **原文没有把这条归属关系写出来，所以这是推断。**
>
> **⑨ 例子里的 `...` 是原文自己写的省略。** 逐字：Example 2 里有四处
> `...`（`Set site specific thresholds` 之后两行、`Setup and execute the DUT test` 之后两行），
> **它们是原文的占位省略，不是本页加的**——
> **本页引例时照原样保留**（§11.1：「`…` 出现在引文里的唯一合法场合，是原文自己就写着它」）。
> **注意原文这几处用的是三个 ASCII 点、不是 `…`（U+2026）。**
>
> **⑩ 例子里的缩进风格不统一。** 逐字对比：Example 1 用**四格**递进
> （`    auxTask.pin("dps1")`），而 Example 2 里又有
> `        .selectVSensorSetThresholds (vThresholdLow, vThresholdHigh);`（**八格**）
> 与 `auxTask.pin("XPS256_PMU_1")`（**顶格**）并列——
> **同一段代码里两种缩进并存。本页照原样引。**

`verified: doc-only`
