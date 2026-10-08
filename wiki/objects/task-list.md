---
type: object
title: TASK_LIST
layer: L2
stage: testmethod
tags: [testmethod, l2, api, task-list, ppmu, sequencing, mset, offline-result-emulation, flexible-dc]
related: [test, dps-task, dps-aux-task, flex-relay, get-functional-result, dc-test-programming, offline-result-emulation, on-first-invocation-begin, for-each-site-end, mapping-testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# TASK_LIST

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,700 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Usage

For creating an object:

```
TASK_LIST <object>;
```

For setting up tasks to be performed:

```
<object>.add(task1).add(task2)...add(taskN);
```

For downloading the settings in tasks:

```
<object>.setup();
```

For downloading the settings in tasks and performing the tasks:

```
<object>.execute();
```

| <object> | Object name to be defined |
|---|---|
| task1-N | Object name of the PPMU_SETTING, PPMU_RELAY or PPMU_MEASURE class to specify a task to be performed. A task list can contain up to 10 tasks. |

### Example

In the following example, the task setting, precharge, relay_on, relay_off, ppmuMeasure, clamp_on and clamp_off are defined and added to the task list. Then a PPMU measurement is performed by executing the task list.

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

The following example shows how to measure a current on a device pin and then use it as a force value for a following measurement for multi-sites. The result value of the first measurement differs from site to site.

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

<!-- 语法节 end -->

## 是什么

**`TASK_LIST` 是一个「任务队列」：把若干个 PPMU 类的任务按顺序装进一个容器，然后一次性下到硬件、或者一次性执行。** 原文第一段就把成员和顺序都定了：

> 「The TASK_LIST class is a data container holding PPMU_SETTING, PPMU_RELAY, and PPMU_MEASURE tasks to be performed.」

> 「Tasks to be performed with this class are defined with the PPMU_SETTING, PPMU_RELAY and PPMU_MEASURE class. Each task will be performed in order of the definition of the task list.」

**「按定义的顺序执行」这句话在本篇出现了三次**（`## Class definition` 一次、`setup()` 一次、`execute()` 一次）——**它不是一个可选的细节，是这个类的语义**。

**定义在哪个头文件**：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/TaskList.h.」

### 一个构造函数 + 三个成员函数

| 成员 | 语法 | 干什么（原文） |
|---|---|---|
| 构造 | `TASK_LIST();` | 「This constructor defines a task list that holds task names to be executed.」 |
| `add()` | `TASK_LIST & add(const TASK& task);` | 「This function adds the specified task to the task list. Added tasks are performed sequentially.」 |
| `setup()` | `void setup();` | **只下载设置，不执行**（见下） |
| `execute()` | `void execute();` | 「This function performs a test by executing the task list. The tasks of the task list are executed sequentially in the registered order.」 |

**`setup()` 与 `execute()` 的区别是这一页最实用的一条**（原文）：

> 「This function downloads settings defined in the task list. The tasks of the task list are executed sequentially in the registered order. It is used when the input parameters of the task are changed during the test method execution. It can change the parameters of an exisiting MSET and reuse it to avoid running out of MSETs.」

**即：`setup()` 存在的理由是「参数要在测试中途改」**——**改一个**已经下过设置的 `MSET`（DC set）并复用，**避免把 MSET 用光**（原文括号里把 `FlexDC` 与 `Managing DC Tests with Variable Parameters` 两篇指了出来）。

### 四种用法语句（文档 `## Usage` 一节的全部内容）

| 要做的事 | 语句 |
|---|---|
| 建对象 | `TASK_LIST <object>;` |
| 往里加任务 | `<object>.add(task1).add(task2)...add(taskN);` |
| **只下载设置**（不执行） | `<object>.setup();` |
| **下载设置并执行** | `<object>.execute();` |

**构造函数自己带一句**：`Parameters` 那一栏写的是「There are no parameters associated with this function.」——**建的时候什么都不用给**，内容全靠 `add()` 攒。

**三个硬限制（都会在运行时咬人）**

**① 一个 list 最多 10 个任务**：

> 「Object name of the PPMU_SETTING, PPMU_RELAY or PPMU_MEASURE class to specify a task to be performed. A task list can contain up to 10 tasks.」

**② `execute()` 之后，没进过这个 list 的 pin 就不能再下任务了**：

> 「Note After the execute() function is performed, you cannot define any tasks for the digital pin that is not included to the performed task.」

原文给了正反两个例子——**同一个 pin 改值是 OK 的**（`setting1.pin("pin1").vForce(2.5 mV); // OK`），**换一个没进过 list 的 pin 就报错**：

> 「However, error occurs if the following program is performed because tasks for "pin2" is not defined in the "tasks" task list.」

**③ 别把它定义成全局对象**（这一条最隐蔽，**它的代价是「越跑越慢」而不是报错**）：

> 「Note If you define a TASK_LIST object as global, the object will not be destroyed when the test method is completed. This will have the effect that the list grows longer with every testflow repetition, so that the test time is increased with every repetition.」

**读法**：**全局对象不会被析构 → 每重复一次 testflow，队列里就多加一批任务 → 测试时间随重复次数递增。**（**语料没写「那该怎么办」**——本页不替它给建议。）

### 离线结果仿真：`add()` 多了一个重载

> 「Measurements can be made by using DPS_TASK, SPMU_TASK, and PPMU_MEASURE objects directly (by calling their execute() member functions) or be put in a TASK_LIST object which queues up tasks to be executed (by calling the execute() method on the TASK_LIST object rather than on the task objects themselves).」

**两种排队方式并存**，仿真需要后者多带一个测量名：

> 「This requires an enhancement also on the TASK_LIST add() method which takes a measurement name as additional parameter.」

> 「Associate the measurement that will be executed by calling task_list.execute() with offline data.」

**即：`add(task, measurementName)` 的那个 `measurementName` 是给离线数据用的**（不是给硬件用的），机制在 `Parametric offline result emulation` 那篇里（**本页没读**，见 [[offline-result-emulation]]）。

## 典型用法

**文档没有 `## Procedure` 段**；Example 1 是一份完整可抄的骨架，本页把它拆成七步（**拆分是本页做的（推断）**，句子的出处都标了）。

**1. 声明所有任务对象 + 一个 `TASK_LIST`**（Example 1 的开头）：`PPMU_SETTING` / `PPMU_RELAY` / `PPMU_MEASURE` / `PPMU_CLAMP` 各一个或几个，再加 `TASK_LIST taskList_1;`。

**2. 配 `PPMU_SETTING`**：每个 pin 一行链式调用（`pin(...).iRange(...).min(...).max(...).iForce(...)` 或 `vForce(...)`）。**`iForce` 与 `vForce` 二选一，就是「强行灌电流」还是「强行灌电压」。**

**3. 配 `PPMU_RELAY`**：`status("PPMU_ON")` / `status("AC_ON")`，**继电器动作之后可以 `wait(...)`**（例子里是 `wait(1.3 ms)`）。

**4. 配 `PPMU_MEASURE`**：`pin("S0,S1").execMode(TM::PVAL)`——**量什么由 `execMode` 定**。

**5. 配 `PPMU_CLAMP`**（例子里注释写明是为了 `avoid hot switching on the current force setup`）：`status("CLAMP_ON").low(2.6 V).high(2.9 V)` / `status("CLAMP_OFF")`。

**6. 按执行顺序 `add()`，然后 `execute()`**——**`add()` 返回自身，所以能链式写**：

> 「This function adds the specified task to the task list. Added tasks are performed sequentially.」

**例子里 `add` 的顺序是**：setting → clamp_on → relay_on → clamp_off → measure → relay_off（**每一步为什么在这个位置，原文只给了注释，没有解释**）。

**7. 取结果 + 判定**：`execute()` 之后从测量对象上取（`ppmuMeasure.getValue("S0")`），再交给 [[test]]（例子里是 `TEST("DC_Test",ppmuMeasure, true);`）。**注意这两件事都在 `ON_FIRST_INVOCATION_END()` 之后。**

### 要在中途改参数：`setup()` + 逐 site 改 + 最后一个 `execute()`

Example 2 是一份「第一次测量的值当第二次的激励」的例子（原话：`The result value of the first measurement differs from site to site.`）。它的形状值得单独记：

1. **第一次测量**：建 `multiDeltaFlexDc1` → `add(setting).add(relay).add(measure)` → **`execute()`**（**这一步就出值了**）；
2. **第二次测量的「骨架」**：建 `multiDeltaFlexDc2` → `add(...)` → **`setup()` 而不是 `execute()`**；
3. **在 [[for-each-site-end]] 块里逐 site 改参数**：把 `ppmuMeasure1.getValue("I/O1")` 的结果写进 `ppmuSetting2` 的 `iForce` / `iRange`；
4. **最后 `execute()`**。

**第 3 步之所以能改，就是第 2 步用了 `setup()`**——**这也是 `setup()` 那句话（`It is used when the input parameters of the task are changed during the test method execution.`）在代码里的样子。**

### 三条硬限制的现场记法

| 限制 | 现场表现 |
|---|---|
| **最多 10 个任务** | 超过就不在文档承诺范围内（**文档只写了「最多 10」，没写超了会报什么**） |
| **`execute()` 后不许给没进过 list 的 pin 下任务** | **报错**（原文 `// error`），而且**是同一段代码换个 pin 名就报** |
| **全局 `TASK_LIST` 对象** | **不报错，只是每重复一次 testflow 就慢一点** |

## 和谁有关

**入边 44 条 / 31 篇（含 1 条 `index.md` 的 toc 与 3 条本页自己的锚点链接），出边 13 条 / 10 个目标**——取自 `extract/edges.jsonl`（`resolved=true`；**链接证，不是本页 sources 的正文**）。

- [[test]] — **下游**：Example 1 的最后一行就是 `TEST("DC_Test",ppmuMeasure, true);`——**测量对象既是 `TASK_LIST` 的成员，又是 TEST 的入参**（同一个对象两次出现）。**另外入边里有一条链接是错的**：`02.07.03.14.02.04_Pass_fail_judgment_of_test_method_based_test_suite_in_a_testflow.md` 里写着 `[TEST](<02.07.04.01.240_TASK_LIST.md>)`——**链接文字是 `TEST`、目标却是本页（TASK_LIST）**，见「出处」⑥。**本页不把它当成一条正常的关系证据。**
- [[get-functional-result]] — **上游读数**：`GET_FUNCTIONAL_RESULT()` 那篇的 Example 2 用 `TASK_LIST Ppmu_task;` + `Ppmu_task.execute()` 触发测量（**那一篇不在本页 `sources:`，本页只记这个事实**）。**「互为出边」不成立**：实测 `extract/edges.jsonl`，本页 13 条出边的 10 个目标里没有它（那 10 个是 `PPMU_MEASURE` / `PPMU_SETTING` / `PPMU_RELAY` / `DPS_TASK` / `SPMU_TASK` / 离线仿真两篇 / `FlexDC` / `Managing DC Tests with Variable Parameters` / 本页自己）。
- [[dps-task]] / `SPMU_TASK`（**清单外**）/ `PPMU_MEASURE`（**清单外**）— **离线仿真的入口族**：原文点名这三个可直接 `execute()`，也可以塞进 `TASK_LIST`（出边三条）。
- [[dps-aux-task]] — **入边 3 条**（`DPS_AUX_TASK` 与 `DPS_AUX_TASK.setup`）：**那一族的 `setup()` / `execute()` 与 `TASK_LIST` 的两个同名成员函数是同一套说法**（**这只是链接证的读法，本页没有读那一篇**）。
- [[flex-relay]]/ [[dc-test-programming]] — **入边最密的一族**：`02.07.03.02_DC_Test_Programming.md` 1 条、`02.07.03.02.02_DC_Test_Programming_with_PPMU.md` **7 条**（全页最密）、`FLEX_RELAY` 2 条；**PPMU 侧的三篇（`PPMU_SETTING` / `PPMU_RELAY` / `PPMU_MEASURE`）也各自链回本页**。
- [[offline-result-emulation ]] — **出边指向它两篇**（`Offline Result Emulation` 与 `Parametric offline result emulation`），**而入边里有一篇的名字直接叫 `Offline_result_emulation_for_Class_TASK_LIST`**——**这个类在离线仿真里是一等公民**。
- [[on-first-invocation-begin]] / [[for-each-site-end]] — **结构上的邻居**：两个 Example 的 `add()` / `setup()` / `execute()` 全部写在 `ON_FIRST_INVOCATION` 块里，Example 2 的改参数循环写在 `FOR_EACH_SITE` 块里。
- `LEV_TRANSFER_TASK` / `VEC_TRANSFER_TASK` / `LOOPBACK_OPERATION_TASK` / `UTILITY_*` / `TIMING_OFFSET_SEARCH_TASK` / `DIGITAL_OFFSET_SEARCH_TASK`（**均清单外**）— **入边里的一大票其它 TASK 族**：说明 `TASK_LIST` **不只是 PPMU 用的**，别的任务族也把它当队列用（**这一条只有链接证**）。
- [[mapping-testmethod]] — 那张跨层对照表把「多 site 并行 setup 块」与「逐 site setup 块」两行放在 `ON_FIRST_INVOCATION` / `FOR_EACH_SITE` 两族 API 上，**本页不在那两行里**——**本页管的是「一批任务按顺序下硬件」，不是块结构**。

## 版本

`## Functional changes` 段两条（逐字）：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.3: Offline result emulation introduced`

**第一条是哨兵值，不是「6.3.2 新增」**（`wiki/schema.md` §11.2②：全语料 2,677 条可用性行都写同一个版本号、措辞都是 `before`，意思是「本套文档集覆盖范围开始之前就有了」）。

**第二条能落地**：**离线仿真（也就是 `add(task, measurementName)` 那个重载）是 SmarTest 7.1.3 引入的**——**7.1.3 之前只有单参数的 `add()`**。

## 出处

`sources:` 一篇，**整篇读完**（298 行 / 8,307 字节）：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.md`
  （TDC topic `29792.htm`，头文件 `MAPI/TaskList.h`）

**本页怎么读的这一篇**：`## Class definition`、`## Usage`、`## Member functions`（`add()` / 离线变体 / `setup()` / `execute()`）、`## Example`（两个）、`## Functional changes`（两条）**全部读过**；引文没有一句来自本页 sources 之外。

**本页没做的**：

- **没有读任何一篇任务对象**：`PPMU_SETTING` / `PPMU_RELAY` / `PPMU_MEASURE` / `PPMU_CLAMP` / `DPS_TASK` / `SPMU_TASK` **一篇都没读**。**所以 `pin("S0,S1")`、`execMode(TM::PVAL)`、`status("PPMU_ON")` 这些成员各自能取什么值，本页一个字都没有**——本页只把它们按例子里的字面抄下来。
- **没有读 `setup()` 那句括号里指的两篇**（`FlexDC`、`Managing DC Tests with Variable Parameters`），**也没有读离线仿真那两篇**：**「MSET 用光了会怎样」「`measurementName` 怎么和离线数据对上」本页都答不了。**
- **没有读 [[dps-aux-task]] / [[flex-relay]] / `DIGITAL_OFFSET_SEARCH_TASK` 那一票入边**——「别的任务族怎么用它」只有链接证的份量。
- **没有开过图**：**这一篇的 raw（md 与上游 `raw/29792.htm`）里一张图都没有**——实测 `<img>` 0 个、`.png` 引用 0 个，**所以本页没有任何图证可写**。**不是「图够不着」**（`wiki/schema.md` §11.4 已更正那条错说法），**是这一篇里没有图**。
- **没有实跑**：没写过一条 `TASK_LIST` 链、**没有量过「全局对象让测试时间变长」到底变多少**、**没有撞过 `pin2` 那个 error**。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/testmethod.md`。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **`exisiting` 拼错**：`It can change the parameters of an exisiting MSET and reuse it to avoid running out of MSETs.`——**应为 `existing`**。

> ② **`add()` 的参数说明少一个 `to`**：`Object name of the PPMU_SETTING, PPMU_RELAY or PPMU_MEASURE class to specify a task be performed.`——**同样是这句话，`## Usage` 那张表里写的是 `to specify a task to be performed.`（对的）**，**两处并存，本页原样引两处、不替它补**。

> ③ **`However, error occurs` 少冠词、且主谓不一致**：`However, error occurs if the following program is performed because tasks for "pin2" is not defined in the "tasks" task list.`——**`error` 前少 `an`，且 `tasks` 后面跟的是 `is`**。**本页原样引。**

> ④ **同一个函数两个重载的写法不一致**：`TASK_LIST & add(const TASK& task);`（`&` 前有空格）与 `TASK_LIST& add(const TASK& task, const string& measurementName)`（`&` 前没有空格）；**而且后者用的是小写 `string`，本篇其余地方一律用大写 `STRING`**（**全文没有出现过 `STRING&` 的重载，所以哪一种才是正式写法，语料没说**）。

> ⑤ **`included to` 应为 `included in`**：`After the execute() function is performed, you cannot define any tasks for the digital pin that is not included to the performed task.`（**同一句里那个 `Note` 的挂法也怪**：它挂在 `execute()` 的 `Parameters` 之后，**而它举的例子是「下面这段程序」**，那两小节代码紧跟在它下面。）

> ⑥ **入边里有一条链接指错——链接文字与目标不是一个东西**（**这一条不是本页 source 里的，是 `extract/edges.jsonl` 里那条边自带的 `context`**）：`02.07.03.14.02.04_Pass_fail_judgment_of_test_method_based_test_suite_in_a_testflow.md` 里写的是 `[TEST](<02.07.04.01.240_TASK_LIST.md>)`——**文字说 `TEST`，目标指到 TASK_LIST**（`02.07.04.01.241_TEST.md` 才是 TEST 那一篇）。**那一篇本页没有读**，**所以本页不知道它是笔误、还是那一篇真的在讲 `TASK_LIST`**——照实记，不判。（同一个现象在 `wiki/mappings/mapping-testmethod.md` 里也记过一类：**一条链接只证明「那篇认为读者该去看这一篇」，不证明两个东西等价**。）

**本页三类话的边界**（§11 的三分）：`文档事实` = 所有 `> 「…」` 引文，以及表里标了「原文」的格；`推断` = 正文里每一处标了（推断）的句子（含「七步拆法」与「按语义读成一张表」两处，**除这些以外本页没有别的主张**）；`建议` = **本页一句都没有**——**全局对象那条陷阱的「那该怎么办」，原文没写、本页也没给。**

`verified: doc-only`
