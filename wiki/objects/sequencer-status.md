---
type: object
title: SEQUENCER_STATUS - (Sequencer)
layer: L3
stage: pattern
tags: [sequencer, run-status, stopcycle, stopvector, endless-loop, abort, global-run, multiport, digital-only]
related: [sequencer, primary-status, execution-context, sqst, flush, dps128-dps64-cards, cct-multiport-sequencer-synchronizer-api, on-first-invocation-begin]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.204_SEQUENCER_STATUS_-__Sequencer.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# SEQUENCER_STATUS - (Sequencer)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,915 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.204_SEQUENCER_STATUS_-__Sequencer.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

For running the sequencers until the specified cycle

Sequencer.stopCycle(num).run(mode);

For running the sequencers until the specified vector

Sequencer.stopVector(num).run(mode);

For other operations of the sequencers

Sequencer.member_func;

Parameters
 |

num

 |

Tester cycle number or vector number

 |
 |

mode

 |

Execution mode of the sequencers. You can also set the `run` member function separately as shown below:

Sequencer.run(mode)

 |
 |

member_func

 |

Member function of the `SEQUENCER_STATUS` API

 |

### Example 1

Given the following pattern, the member functions `stopVector` and `stopCycle` behave as follows.

 !`Pattern tool_SEQUENCER_STATUS`（raw: `../../../../raw/144837.png`）

- `Sequencer.stopCycle(13).run();`

The sequencer stops after executing cycle number 13 (p1 set to 1)

- `Sequencer.stopCycle(14).run();`

The sequencer stops after executing cycle number 14 (p1 set to 0)

- `Sequencer.stopVector(9).run();`

The sequencer stops after executing vector number 9 (p1 set to 1)

- `Sequencer.stopVector(10).run();`

The sequencer stops after executing vector number 10 (p1 set to 0)

### Example 2

The following example will perform a DC measurement using FlexDC. First, it prepares the needed flex dc settings, then it starts the sequencer and pauses on tester cycle 15 to perform the DC measurement at pin "pin1".

```
virtual void run()
 {
    PPMU_SETTING setting1;
    TASK_LIST tasks;
    PPMU_RELAY relay_on, relay_off;
    PPMU_MEASURE ppmu_meas;
    PPMU_CLAMP clamp_on, clamp_off;

    double VMeas_seq1;
ON_FIRST_INVOCATION_BEGIN();
    setting1.pin("pin1").vForce(2.1 mV);
    setting1.pin("pin1").iRange("10uA");
    setting1.pin("pin1").min(0.1 uA).max(25.0 uA);

    relay_on.pin("pin1").status("PPMU_ON");
    relay_on.wait(1.3 ms);
    relay_off.pin("pin1").status("AC_ON");

    clamp_on.pin("pin1").status("CLAMP_ON").low(2.6 V).high(2.9 V);
    clamp_off.pin("pin1").status("CLAMP_OFF");

    ppmu_meas.pin("pin1"). execMode(TM::PVAL);

    tasks.add(setting1).add(clamp_on).add(relay_on).add(clamp_off). add(ppmu_meas).add(relay_off);
    Sequencer.stopCycle(15).run();
    tasks.execute();
    ON_FIRST_INVOCATION_END();
    VMeas_seq1 = ppmu_meas.getValue("pin1");
Sequencer.reset();

    return;
  }
```

### Example 3

```
Sequencer.run(TM::ENDLESS_PATTERN_LOOP);
DPS_VFIM("@").execute();
Sequencer.abort();
```

This example achieves an operating current test of the DPS with the test method. First, it starts the sequencer in an endless pattern loop. Then it performs a current measurement at a random device cycle. Then it aborts the sequencer.

### Example 4

```
Sequencer.reset();
PMU_IFVM("@").preAction("FTST").execute();
```

This example resets the sequencer before performing a functional test that is a pre-action of the DC test. However, It is recommended to use FLEX DC instead of PMU_IFVM and use SEQUENCER_STATUS APIs to execute a functional pattern as pre action if required as shown in above example 1.

<!-- 语法节 end -->

## 是什么

**`SEQUENCER_STATUS` 是「数字 sequencer 的运行状态容器 + 运行控制」这个 API。**

> 「The SEQUENCER_STATUS API accesses the data container holding the digital sequencer status.
> You can access the sequencers using the member functions.」

**它是本文档集里「怎么让 pattern 跑到第 N 个 cycle 就停下让我做点别的」的答案**——
测电流、做 DC 测量、临时停一下——**靠的都是它。**

**定义在头文件** `/opt/hp93000/soc/prod_com/include/MAPI/SequencerStat.h`。

### 三条限制（原文一开头就列，**都是「不许」**）

> 「You have to use the system-prepared class object Sequencer when using the member functions.
> You cannot create any class object of the SEQUENCER_STATUS API.」

> 「The SEQUENCER_STATUS API does not affect the analog sequencers.」

> 「The SEQUENCER_STATUS API does not support execution contexts (for which see
> Using execution contexts). You can only start a global sequencer run (executing the current
> start label) with the member function run(), and only abort globally all active sequencer runs
> with the member function abort().」

| 限制 | 后果 |
|---|---|
| **对象只能用系统的 `Sequencer`** | 语法永远是 `Sequencer.xxx()`；**没有构造，也没有析构** |
| **不管 analog sequencer** | **数字侧能停，不等于模拟侧停了**——`isRunning()` 问的也只是数字侧（见下） |
| **不支持 execution context** | **只有「全局 run」和「全局 abort」两个动作**——**没有「只对某个 context 跑 / 只停某个 context」这回事** |

**「只能全局」这条要连着读**：`run()` 执行的是 **the current start label**，
**而它一旦跑起来就是全局的**。**想按 site / 按 context 分开控制，这个 API 给不了**——
这一点直接连到 [[execution-context]]（**支持 execution context 的是另一套东西**）。

### 一条容易撞上的前置条件：**已经有人在跑，你就起不来**

> 「Note also that run() will start a global sequencer run only if no sequencer is already
> running (for example, in an endless loop). If there is, you must stop all the active runs with
> abort() before you can start the new one.」

**记法：`run()` 不是「开始跑」，是「开始跑——前提是现在没在跑」。**
**`TM::ENDLESS_LOOP` / `TM::ENDLESS_PATTERN_LOOP` 起的就是「永远在跑」的状态**，
**所以那两种模式下 `run()` 会一直失败，直到 `abort()`。**

### 八个成员函数，按用途分四组

原文 `## Class definition` 里的声明块是**原样的**（**注意 `run()` 和 `abort()` 两行没写返回类型，
和另外六个不一样——见「出处」的 ⚠️**）：

```
SEQUENCER_STATUS& stopCycle(int num);
SEQUENCER_STATUS& stopCycle(int num, const STRING& portName);
SEQUENCER_STATUS& stopVector(int num);
SEQUENCER_STATUS& reset();
run(TM::RUN_STATUS status = TM::NORMAL);
abort();
Boolean isRunning();
const STRING getSequencerStatus() const;
```

| 组 | 函数 | 干什么 |
|---|---|---|
| **定「停在哪」** | `stopCycle()` `stopVector()` | **设定「跑到第几个 cycle / 第几个 vector 就停」**——**是链式写法的前一半** |
| **跑 / 停** | `run()` `abort()` | **全局启动 / 全局打断**；`run()` 带回车键参数 `TM::RUN_STATUS` |
| **清设置** | `reset()` | **把 `stopCycle` / `stopVector` 设的东西清掉**——**不改「现在跑不跑」** |
| **读状态** | `isRunning()` `getSequencerStatus()` | 前者是 `Boolean`，后者是 `OFF` / `RUN` / `HALT` / `BRK` 四选一 |

### **`stopCycle` / `stopVector` 的「第 N 个」是「含 N」**（最容易差一个的地方）

> 「This member function specifies a tester cycle after which the sequencers will stop
> (the specified cycle is the last cycle that is executed, see Example section)」

> 「the `stopVector()` member function specifies a vector number after which the sequencer stops
> (the specified vector is the last vector in this execution, see Example section).」

**「停在 cycle 13 之后」= cycle 13 是**执行过的最后一个**。**不是「从 13 开始不执行」。**
原文 Example 1 用一张图 + 四行给死了这件事（**那张图本页没看，见「出处」**）：

| 写法 | 原文结论 |
|---|---|
| `Sequencer.stopCycle(13).run();` | `The sequencer stops after executing cycle number 13 (p1 set to 1)` |
| `Sequencer.stopCycle(14).run();` | `The sequencer stops after executing cycle number 14 (p1 set to 0)` |
| `Sequencer.stopVector(9).run();` | `The sequencer stops after executing vector number 9 (p1 set to 1)` |
| `Sequencer.stopVector(10).run();` | `The sequencer stops after executing vector number 10 (p1 set to 0)` |

> **注意 cycle 13 → `p1` 是 `1`、cycle 14 → `p1` 是 `0`**：**同一个「停」落在 cycle 还是
> 落在它后面一格，`p1` 的状态是反的**——**这四行存在的意义就是让你别差这一格。**

### 这个设置**不止管 `run()`**，而且**会一直留着**

> 「The setting of this function affects not only the `run()` member function but also the
> EXECUTE_TEST, START_TEST, FUNCTIONAL_TEST, DIGITAL_CAPTURE_TEST, NB_DIGITAL_CAPTURE_START
> API, and pre-action of the DC APIs.」

> 「This function is provided to change the behavior of the sequencer execution temporarily.
> However the setting of this function is effective until all settings are reset by the reset()
> member function of this API. Therefore you should reset the setting by using the reset()
> member function at the end of the test suite or before starting the sequencer for the other
> test.」

**这两句合起来是本页最实用的一条：**
**「临时停一下」的设置会**留到下次**，而且下次可能是某个你没想到的 API 触发的 sequencer 运行。**
**所以 `reset()` 不是可选项——原文用的是 `you should`。**

### `reset()` 有两个**额外**的坑

**坑一：`reset()` 不是立即生效的，它要等下一次 sequencer run。**

> 「Note that Sequencer.reset() will clear the settings done by stopCycle() and stopVector() but
> this will only take effect (that is, it will only be flushed, that is, downloaded) before the
> next sequencer run initiated through the test methods APIs listed above under the stopCycle()
> member function. If the reset is to take effect earlier, FLUSH must be called explicitly.」

**坑二：`reset()` 清的是「设置」，不是「现在跑不跑」。**

> 「Note also that reset() does not affect the current sequencer status. If you want to stop the
> sequencers, you must call Sequencer.abort().」

**还有一条 AC 测试专用的：**
> 「Note In an AC test, you need to clear the sequencer settings before the measurement.」

| 你想干的事 | 该调谁 | **别调错** |
|---|---|---|
| **清掉 `stopCycle` / `stopVector` 的设置** | **`Sequencer.reset()`** | 它**停不了**正在跑的 pattern |
| **把正在跑的 pattern 停掉** | **`Sequencer.abort()`** | 它**清不了**设置 |
| **让 `reset()` 立刻生效** | **显式调 `FLUSH`**（[[flush]]，**未建**） | **不调就一直等到下次 run** |

### `run()` 的五种 `TM::RUN_STATUS`

原文把五种模式列在 `run()` 的参数里，**这是本页第二张要紧的表**：

| 模式 | 原文要点 |
|---|---|
| **`TM::NORMAL`**（**默认**） | `The sequencer executes the pattern.` |
| **`TM::ENDLESS_LOOP`** | `repeats the complete test, including primary activation and multiport synchronization, in an endless loop and can only be stopped by a break action`；另见 `SQGB` 的 **`EL` mode** |
| **`TM::ENDLESS_PATTERN_LOOP`** | **只重复 pattern 里用户写的 sequencer program**——`This avoids critical holds during measurement for example, for IDD operating currents` |
| **`TM::STOPONERROR`** | `The sequencer stops when an error occurs in the execution.` |
| **`TM::STOPONERROR_LOOP`** | `The sequencer stops when an error occurs in an endless loop.` |

> **`ENDLESS_LOOP` 与 `ENDLESS_PATTERN_LOOP` 的差别是「重复的范围」**：
> 前者**重跑完整 test（连 primary 激活和多端口同步一起重做）**，
> 后者**只重跑 pattern 里那段用户 sequencer program**。
> **原文给后者的理由是「避免测量期间的 critical hold」**——**所以测 IDD 工作电流要用后者。**
> （「primary activation」指的正是 [[primary-status]] 那一套，见「和谁有关」。）

**多端口的一条警告**（挂在 `ENDLESS_PATTERN_LOOP` 那条下面）：

> 「In case of multiport testing, ports may run with different frequencies. Using the ELPT mode in
> this case, can lead to the situation, that for loop counts >1 the synchronization is no longer
> executed. See also the ELPT mode in SQGB, SQGB? - (SeQuencer GloBal)」

**即：多端口 + 各端口频率不同 + `ELPT` 模式 + 循环次数 > 1 → 同步就不做了。**

### 两个读状态的函数，**口径不同**

| 函数 | 读什么 | 取值 |
|---|---|---|
| `isRunning()` | **「数字 sequencer 在不在跑」** | `Boolean` |
| `getSequencerStatus()` | **当前 sequencer 状态** | **`OFF` / `RUN` / `HALT` / `BRK`** |

**原文还给了一个「想连模拟一起问」的出口**：
> 「You can also use the IS_TEST_RUNNING API that returns whether either the analog or digital
> sequencer is running.」

**所以这三个的口径是层层放大的：**
**`isRunning()` = 只有数字 → `IS_TEST_RUNNING` = 数字或模拟 → `getSequencerStatus()` = 数字那一个的具体状态。**

## 典型用法

**1. 停在一个 cycle 上做 DC 测量**（原文 Example 2 的骨架，**这是本 API 的主用法**）：

**准备 FlexDC 设置**（`PPMU_SETTING` / `PPMU_RELAY` / `PPMU_CLAMP` / `PPMU_MEASURE` 装进一个 `TASK_LIST`）
→ **`Sequencer.stopCycle(15).run();`** → **`tasks.execute();`** → **取测量值** → **`Sequencer.reset();`**

> 原文对这一例的说明：`The following example will perform a DC measurement using FlexDC.
> First, it prepares the needed flex dc settings, then it starts the sequencer and pauses on
> tester cycle 15 to perform the DC measurement at pin "pin1".`

**顺序是硬的：`stopCycle(...).run()` 必须在 `tasks.execute()` 之前**——
**因为 sequencer 得先跑到那格停下来，测量才有意义。**

**2. 测 DPS 工作电流**（原文 Example 3，逐字）：

```
Sequencer.run(TM::ENDLESS_PATTERN_LOOP);
DPS_VFIM("@").execute();
Sequencer.abort();
```

> 「First, it starts the sequencer in an endless pattern loop. Then it performs a current
> measurement at a random device cycle. Then it aborts the sequencer.」

**三步：** 起无限循环 → 在随机 cycle 上测 → **`abort()`**。
**最后那步不能省**（上面「已经有人在跑」那条）。**注意这里用的是 `ENDLESS_PATTERN_LOOP` 而不是 `ENDLESS_LOOP`**——
**和「避免测量期间的 critical hold」那条理由对得上。**

**3. DC 测试前先跑一段 functional**（原文 Example 4，逐字）：

```
Sequencer.reset();
PMU_IFVM("@").preAction("FTST").execute();
```

> 「This example resets the sequencer before performing a functional test that is a pre-action of
> the DC test. However, It is recommended to use FLEX DC instead of PMU_IFVM and use
> SEQUENCER_STATUS APIs to execute a functional pattern as pre action if required as shown in
> above example 1.」

> **这一例里原文给了一条明确建议**：**别用 `PMU_IFVM` 做 pre-action，
> 用 FLEX DC + `SEQUENCER_STATUS`**（即例 1 的写法）。
> **原文自己把这一例标成了「不推荐的老写法」——照它的口径，例 1 才是正路。**

**4. 一条练习上的顺序**：**任何用过 `stopCycle` / `stopVector` 的 test suite，
结束前（或开始下一个测试前）`reset()`。** 依据就是原文那句 `you should reset the setting … at
the end of the test suite or before starting the sequencer for the other test.`

**5. 要「现在就生效」**：**`reset()` 之后补一次显式 `FLUSH`**（[[flush]]，**未建**）。

## 和谁有关

**上游 / 同一件事的另一半（start label）**：

- [[primary-status]] — **双向关系，两边原文都点了名**：
  ① 本页 `run()` 执行的是 **the current start label**，而 **start label 正是
  `Primary.label()` 设的那个 primary**；
  ② 反向，`primary-status` 那篇把 **`FLUSH then SEQUENCER_STATUS.run()`**
  列进了「让 primary 改动生效到硬件」的 API 清单。
  **另外 `TM::ENDLESS_LOOP` 的说明里那句 `including primary activation` 说的也是它。**
  **一句话：primary 是「哪一套」，本页是「让那一套跑起来并停在第几格」。**

**明确「不支持」的那一个（**反向关系，也是本页最该记住的边界**）**：

- [[execution-context]] — 原文说 **`The SEQUENCER_STATUS API does not support execution
  contexts`**，并因此**只剩全局 `run()` 与全局 `abort()`**。
  **所以「要按 context 控制 sequencer」在这条路上是走不通的**——
  **该页讲的是另一套机制，本页没读它**。

**firmware 侧的对应物（同层的另一种实现）**：

- [[sqst]] — **`SQST RUN`** 是 firmware 侧的「启动 sequencer」命令，原文在
  **DPS128/DPS64 那条**里把它和本页的 `run()` 并列（见下）。
  **一层是 L3 API、一层是 L1 命令，办的是同一件事。**
  （**注意本页的 `getSequencerStatus()` 返回 `OFF/RUN/HALT/BRK`，
  与 `SQST` 的状态词是不是同一套，本页没读那篇，不作断言。**）

**下游 / 用到本页的别的东西**：

- [[dps128-dps64-cards]] — 原文的警告是针对这张卡说的：
  `the DPS128/DPS64, when starting the sequencer with the run() member function or with the
  SQST RUN firmware command, cannot execute dynamic and static DC actions in parallel. Use
  profiling for measurements in parallel to a dynamic pattern.`
  **即：这张卡上「动态 pattern 和静态 DC 动作」不能并行——要并行得改用 profiling。**
- [[cct-multiport-sequencer-synchronizer-api]] — **多端口同步那一侧的机制**；
  原文两处提到 multiport：`stopCycle` 要求 **start label 是 multiport burst 时须指定 port**，
  以及 **`ELPT` 模式下循环 >1 次同步失效**。**同步是怎么实现的，本页没有，在那一边。**
- [[flush ]] — **`reset()` 要提前生效就得显式调它**（原文：`If the reset is to take
  effect earlier, FLUSH must be called explicitly.`）
- [[on-first-invocation-begin]] / [[on-first-invocation-end ]] — 原文 Example 2
  把整段设置包在 `ON_FIRST_INVOCATION_BEGIN()` / `ON_FIRST_INVOCATION_END()` 里；
  **它们的作用本页没读**，只记「例子里用了」。

**被本页点名但本页没读的（均未建，不链）**：
`EXECUTE_TEST` / `START_TEST` / `FUNCTIONAL_TEST` / `DIGITAL_CAPTURE_TEST` /
`NB_DIGITAL_CAPTURE_START` / `DPS_VFIM` / `PMU_IFVM` / `TASK_LIST` / `PPMU_SETTING` /
`PPMU_RELAY` / `PPMU_CLAMP` / `PPMU_MEASURE` / `IS_TEST_RUNNING` / `SQGB` / `FLUSH`。

> **本页的「和谁有关」全部来自这一篇原文里点到的名字，没有一条来自别处文档。**

## 版本

本文档有 `## Functional changes` 段，**全部内容五条**：

- **`Introduced before SmarTest 6.3.2`**
- **`SmarTest 6.5.2: New parameter option TM::STOPONERROR and TM::STOPONERROR_LOOP for the member function run().`**
- **`SmarTest 6.5.2: New member function getSequencerStatus().`**
- **`SmarTest 6.5.2: New parameter portName for the member function stopCycle().`**
- **`SmarTest 6.5.4: New TM::ENDLESS_PATTERN_LOOPparameter option for the run() member function.`**

> **第一条 `Introduced before SmarTest 6.3.2` 是哨兵值，不是「6.3.2 新增」。**
> 按 §11.2 ②，`before` 的意思是「**在本文档集覆盖范围开始之前就已经有了**」，
> 全语料 2,677 条可用性行都这么写。**本页不把它读成一条版本变更。**
>
> **能确定的三条版本事实**（都与 `run()` 有关，全在 6.5.2 / 6.5.4）：
> **6.5.2 加了 `STOPONERROR` / `STOPONERROR_LOOP` 两种模式、`getSequencerStatus()`、`stopCycle` 的 `portName` 参数；
> 6.5.4 加了 `TM::ENDLESS_PATTERN_LOOP`。**
> **即：本页最实用的「无限循环 + 停」那条路（例 3）在 6.5.4 之前写不出来。**
>
> **对照页**：[[smartest-6.5.2]] / [[smartest-6.5.4]]（**均未建**）——
> **这两版的覆盖范围本页没读。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.204_SEQUENCER_STATUS_-__Sequencer.md`
（raw 的 `source_topic: "29701.htm"`）。

**本页没做的**：

- **Example 1 的那张图本页没看**（raw 里是 `![Pattern tool_SEQUENCER_STATUS](<../../../../raw/144837.png>)`）。
  **所以上面那张「cycle 13/14、vector 9/10 分别停在哪个 `p1`」的表，
  本页是照原文的四行文字抄的，图里画了什么我不知道。**
  **那四行的意思是靠图定的，本页只有文字那一半依据。**
- **被本页点名的 API 一篇都没读**：`EXECUTE_TEST` / `START_TEST` / `FUNCTIONAL_TEST` /
  `DIGITAL_CAPTURE_TEST` / `NB_DIGITAL_CAPTURE_START` / `DPS_VFIM` / `PMU_IFVM` /
  `TASK_LIST` / `IS_TEST_RUNNING` / `FLUSH`。**「它们也会被 `stopCycle` 的设置影响」这句是原文说的，
  但影响成什么样、为什么，本页不知道。**
- **`SQGB` 的 `EL` / `ELPT` 两个模式没读**（原文两处指过去）。
  **所以「`ENDLESS_LOOP` 与 `SQGB` 的 `EL` 是什么关系」本页不判。**
- **`SQST RUN` 那篇（[[sqst]]）没读**——**firmware 侧那半只有原文这一句转述。**
- **`Using execution contexts` 那篇（[[execution-context]]）没读**——
  **所以「不支持 execution context」的具体后果（哪些场景会撞上）本页不知道，只知道这条禁令存在。**
- **`Profiling of DC Scale cards with Hardware view` 没读**——
  **DPS128/DPS64 那条说要改用 profiling，profiling 是什么本页没有。**
- **FlexDC 那一套（`PPMU_SETTING` / `PPMU_RELAY` / `PPMU_CLAMP` / `PPMU_MEASURE` /
  `TASK_LIST`）本页一个字都没讲**——**Example 2 的代码里它们占了绝大部分行数，
  本页只说了「它们在 `stopCycle(...).run()` 之前准备好」这一件事。**
- **`ON_FIRST_INVOCATION_BEGIN` / `END` 的作用本页没读。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `## Class definition` 的声明块里，八个函数有六个带返回类型、两个不带。** 逐字：
> `SEQUENCER_STATUS& reset();` 有，而它下一行是 `run(TM::RUN_STATUS status = TM::NORMAL);`、
> 再下一行是 `abort();`——**这两行没有返回类型**，`## Member functions` 一节的小标题里
> 也是同样的写法（`run(TM::RUN_STATUS status = TM::NORMAL);` / `abort();`）。
> **本页照引，不补类型。**
>
> **② 同一篇里小节标题大小写不一致。** `## Class definition` 下面是
> `### Member Functions`（**大写 F**），而后面一节是 `## Member functions`（**小写 f**）。
> **同一件事两个标题。**
>
> **③ `## Functional changes` 最后一条少一个空格。** 逐字：
> `SmarTest 6.5.4: New TM::ENDLESS_PATTERN_LOOPparameter option for the run() member function.`
> ——**`TM::ENDLESS_PATTERN_LOOPparameter` 之间没有空格。**
>
> **④ Example 4 的说明里，句子中间的 `It` 大写。** 逐字：
> `However, It is recommended to use FLEX DC instead of PMU_IFVM and use SEQUENCER_STATUS APIs
> to execute a functional pattern as pre action if required as shown in above example 1.`
>
> **⑤ Example 2 的代码里有「点号后带空格」的写法**（不是本页加的）。逐字：
> `ppmu_meas.pin("pin1"). execMode(TM::PVAL);` 与
> `tasks.add(setting1).add(clamp_on).add(relay_on).add(clamp_off). add(ppmu_meas).add(relay_off);`
> ——**`). execMode` 与 `). add(` 各多一个空格。** 同一段里 `relay_on.wait(1.3 ms);`
> 与 `setting1.pin("pin1").vForce(2.1 mV);` 又是**数字与单位之间带空格**（这在 93K 的
> 带单位字面量里是正常写法，本页不当作错）。
>
> **⑥ 语法节的「Parameters」是一张被拆行的大表**（`num` / `mode` / `member_func` 三行各占多行），
> **和 [[xps256-status-flags]] 里那 18 张表是同一个成因**：HTML 表格转 markdown 时被拆成
> 一列一行，脚本只认连续 ≥3 行的管道行。**逐字没丢，只是形状变了。**
>
> **⑦ Example 1 的图在「语法 / 参数」节里被渲染成了行内代码**
> （`!`Pattern tool_SEQUENCER_STATUS`（raw: `../../../../raw/144837.png`）`）——
> **这是抽取器的渲染结果，不是原文长这样。原文是一个 `![]()` 图片引用。**
> **本页不改这一节，只在此记录。**

`verified: doc-only`
