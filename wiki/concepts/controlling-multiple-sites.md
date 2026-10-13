---
type: concept
title: Controlling Multiple Sites
layer: n/a
stage: run
tags: [testmethod, multisite, parallel, focus, site, api]
related: [testmethod, testflow, results, run, on-first-invocation-begin, on-first-invocation-end, for-each-site-begin, for-each-site-end, site-control-window, site-focus-required-before-command]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.13_Controlling_Multiple_Sites.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Controlling Multiple Sites

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **10,582 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.03.13_Controlling_Multiple_Sites.md>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.03.13.03.01.01_Sharing_Channels_Between_Several_Sites.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.03.13.03.02_Controlling_the_Setup-Focus_Manually.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.03.13.10_How_to_execute_separate_patterns_per_site__Label_per_site.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Site-Specific Setup › Controlling the Setup Query-Focus Automatically › Sharing Channels Between Several Sites）

The following code fragment gives an example:

```
PPMU_MEASURE m1;

ON_FIRST_INVOCATION_BEGIN();
{
    PPMU_SETTING s1;
    PPMU_RELAY r1;
    TASK_LIST t1;

    s1.pin("IN1").iRange("100uA");
    s1.pin("IN1").iForce(100 uA).min(50 mV).max(100 mV);

    r1.pin("IN1").status("PPMU_ON");

    m1.pin("IN1").execMode("GPF");

    t1.add(s1).add(r1).add(m1);
    t1.setup();

    FOR_EACH_SITE_BEGIN();
    {
        DOUBLE var = rand() % 6;

        s1.pin("IN1").min(var/1000 V).max((var+1)/1000 V);

        t1.execute(); // Execute measurements within the FOR_EACH_SITE block
    }
    FOR_EACH_SITE_END();
}
ON_FIRST_INVOCATION_END();

Boolean pf = m1.getPassFail();
```

In this example, pin IN1 is supposed to be associated with the same channel on all sites. The example uses the rand() function to assign different values to the variable var in offline mode for every repetition of the FOR_EACH_SITE loop. In practice, the value of the variable will usually be determined by a previous measurement.

### Example 1: Get, change, and restore the setup focus of a site（取自子主题 Site-Specific Setup › Controlling the Setup-Focus Manually）

```
ARRAY_I sites;
...
...
ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Get the site numbers of the currently setup-focused
    // sites and store them into the sites array.
    //
    GET_TEST_FOCUS(sites);

    //
    // Enable the setup focus on site 1.
    // Disable the setup focus on all other sites.
    //
    // Note: The setup focus for all other sites is disabled
    //       because the optional parameter "exclusive" is omitted.
    //       The default value = true is applied.
    //
    SET_TEST_FOCUS(1);

    //
    // Apply changes only to site 1.
    //
    AWG("ain").vOffset(5.0 V);

    FLUSH();

    ...
    ...

    //
    // Restores the state of all enabled sites to the original
    // state by using the contents of the sites array.
    //
    SET_TEST_FOCUS(sites);
}
ON_FIRST_INVOCATION_END();
```

### Example 2: Print list of setup-focused sites（取自子主题 Site-Specific Setup › Controlling the Setup-Focus Manually）

```
ARRAY_I sites;
...
...
ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Get the site numbers of the currently setup-focused
    // sites and store them into the sites array.
    //
    GET_TEST_FOCUS(sites);

    //
    // Print the size and the contents of the sites array
    //
    cout << endl;
    cout << sites.size() << " sites are setup-focused:" << endl;
    cout << endl;

    for (int index = 0; index < sites.size(); index++)
    {
        cout << "\tSite " << sites[index] << " is setup-focused" << endl;
    }

    cout << endl;
}
ON_FIRST_INVOCATION_END();
```

### Example 1（取自子主题 How to execute separate patterns per site  Label per site）

The following is an example of the structure of a test method API for performing the "Pattern per Site" feature.

Note that in the code the term "Label" is used for "Pattern".

- To select label per site, use the following TM-API, which sets up label per site within the "FOR_EACH_SITE_BEGIN" and "FOR_EACH_SITE_END" loop:

```
const STRING label[]={"label_s1","label_s2", ...};

ON_FIRST_INVOCATION_BEGIN();

   Primary.label(label[0]);            // Select default label for all sites

   FOR_EACH_SITE_BEGIN();              // Select label per site

        INT i = CURRENT_SITE_NUMBER() -1;
        Primary.assignLabelToCurrentSite(label[i]);

   FOR_EACH_SITE_END();

   FUNCTIONAL_TEST();                  // Execute label per site

ON_FIRST_INVOCATION_END();
```

- To assign shared pins to a site, use the following TM-API that uses assignPinToCurrentSite(… for this purpose:

```
const STRING pin[]={"pin_s1","pin_s2", ...};
const STRING label[]={"label_s1","label_s2", ...};

ON_FIRST_INVOCATION_BEGIN();

    Primary.label(label[0]);           // Select default label for all sites

   FOR_EACH_SITE_BEGIN();              // Select label and pin per site

        INT site = CURRENT_SITE_NUMBER() -1;
        Primary.assignLabelToCurrentSite(label[site]);
        Primary.assignPinToCurrentSite(pin[site]);

   FOR_EACH_SITE_END();

    FUNCTIONAL_TEST();                 // Execute label per site

    Primary.assignPinToCurrentSite();  // Restore site assignment
                                       // error if it is called outside with pins
    FLUSH(TM::APRM);

ON_FIRST_INVOCATION_END();
```

- To restore the site assignment of the shared pins, the following TM-API with an empty parameter list is called outside the FOR_EACH_SITE loop.

```
Primary.assignPinToCurrentSite();       // Restore site assignment
FLUSH(TM::APRM);
```

It is recommended that you restore the site assignment, when the test-method has finished.

To retain the ability of reusing the site assignments over several groups of test-suites, restoration of the site assignment is implemented via an extra TM-API.

### Example 2: Heterogeneous multisite test（取自子主题 How to execute separate patterns per site  Label per site）

This test method example shows a situation in which an MX-Signal pin gets multiplexed via a relay located on load-board controlled by utility line pin.

- The first section of the test method prepares the setup, so that an MXSignal Test is executed on sites 1 and 3 and a Digital Test is executed on sites 2 and 4.

```
static Boolean digitalResult[maxSites];

ON_FIRST_INVOCATION_BEGIN();

    //
    // Global settings
    //
    Analog.primary("name");              // Select Analog Primary
    Routing.pin("dgt_pin").connect();    // Connect analog instruments
    Primary.label("digital_test");       // Select global label

    //
    //
    // Prepare tests for all sites
    FOR_EACH_SITE_BEGIN();

        INT site = CURRENT_SITE_NUMBER() - 1;

        if (site == 0 || site == 2)                      // Analog Setting for site 1 & 3
        {
            Routing.util("relay_1").on();                // switch load board relay to site 1 & site 3
            Primary.assignLabelToCurrentSite("mx_test"); // assign label used for HW-Trigger
            Primary.assignPinToCurrentSite("TrigPin");   // assign trigger pin
        }
        else                                             // Digital setting for the other sites
        {
            Primary.assignLabelToCurrentSite("digital_test");
        }

    FOR_EACH_SITE_END();
    ...
    ...
```

- The next test method section executes the prepared test for site 1 and 3.

  - It enables the HW-Trigger
  - It sets the result Handle for Hidden Analog upload used in SmartCalc
  - It executes the Heterogeneous Test

```
Analog.requestResultHandle("handleSite_1_3");          // Select Result Handle for SmartCalc
DGT("dgt_pin").enable();                               // Enable HW-Trigger
SMC_EXECUTE_TEST();                                    // Execute Test
DGT("dgt_pin").disable();                              // Disable digitizer pin
```

- This part shows the result handling for the first part of this test.

```
    ...
    ...
    FOR_EACH_SITE_BEGIN();                             // Result Handling

        INT site = CURRENT_SITE_NUMBER() - 1;

        if (site == 0 || site == 2)
        {
            SMC_ARM("handleSite1_3");                  // Pass result handle to SmartCalc
        }
        else
        {
            digitalResult[site] = GET_FUNCTIONAL_RESULT(); // Store Functional Test Result
        }

    FOR_EACH_SITE_END();
    ...
    ...
```

- This part prepares the second part of this test.

```
    ...
    ...
    //
    // Prepare test for all sites
    //
    FOR_EACH_SITE_BEGIN();

        INT site = CURRENT_SITE_NUMBER() - 1;

        if (site == 1 || site == 3)
        {
            Routing.util("relay_1").off();                // Switch loadboard relay to site 2 & site 4
            Primary.assignLabelToCurrentSite("mx_test");  // Assign label used for HW-Trigger
            Primary.assignPinToCurrentSite("TrigPin");    // Assign trigger pin
        }
        else
        {
            Primary.assignLabelToCurrentSite("digital_test");
        }

    FOR_EACH_SITE_END();
    ...
    ...
```

- This part executes the prepared test for site 2 and 4.

  - it enables the HW-Trigger
  - it sets the result Handle for Hidden Analog upload used in SmartCalc
  - it executes the Heterogeneous Test

```
Analog.requestResultHandle("handleSite_2_4");          // Select Result Handle for SmartCalc
DGT("dgt_pin").enable();                               // Enable HW-Trigger
SMC_EXECUTE_TEST();                                    // Execute Test
DGT("dgt_pin").disable();                              // Disable HW-Trigger
```

- This part shows the result handling for the second part of this test.

```
    ...
    ...FOR_EACH_SITE_BEGIN();                                 // Result Handling

    INT site = CURRENT_SITE_NUMBER() - 1;

    if (site == 1 || site == 3)
    {
        SMC_ARM("handleSite2_4");                      // Pass result handle to SmartCalc
    }
    else
    {
        digitalResult[site] = GET_FUNCTIONAL_RESULT(); // Store Functional Test Result
    }

FOR_EACH_SITE_END();
```

- The final part does the following:

  - It disconnect the analog instruments
  - It outputs the functional test results

```
    ...
    ...
    Routing.pin("dgt_pin").disconnect();

ON_FIRST_INVOCATION_END();

INT site = CURRENT_SITE_NUMBER() -1;

if (digitalResult[site])
{
    cout << "Digital Result: Pass"<< endl;
}
else
{
    cout << "Digital Result: Fail"<<endl;
}
```

Note:

1. The above example uses SmartCalc to keep the structures simple and to hide the upload and calculations. However, you can do a hidden upload and hidden calculation without SmartCalc along the following lines:

- Use `DGT().getWaveform(...)` + Calculation in `FOR_EACH_SITE` loops
- Use static variables to store results
- Do data logging outside of `ON_FIRST_INVOCATION` block

2. If the digital test is longer than the Analog test, you can hide the upload & calculation by using `START_TEST` + `WAIT_TEST_DONE as follows`:

```
Analog.requestResultHandle("handleSite_1_3"); // Select Result Handle for SmartCalc
DGT("dgt_pin").enable();                      // Enable HW-Trigger
START_TEST();                                 // Execute Test
WAIT_TEST_DONE(TM::WAIT_DGT);                 // Wait until MX Test is finished
DGT("dgt_pin").disable();                     // Disable HW-Trigger

FOR_EACH_SITE_BEGIN();                        // Result Handling for MX, while digital test is running

    INT site = CURRENT_SITE_NUMBER() - 1;

    if (site == 0 || site == 2)
    {
        ...                                   // Upload Analog and calculate analog results
    }

FOR_EACH_SITE_END();

WAIT_TEST_DONE(TM::WAIT_DIGITAL);             // Wait until digital test is finished

FOR_EACH_SITE_BEGIN();                       // Result Handling for digital

    INT site = CURRENT_SITE_NUMBER() - 1;

    if (site == 0 || site == 2)
    {
        digitalResult[site] = GET_FUNCTIONAL_RESULT();  // Store Functional Test Result
    }

FOR_EACH_SITE_END();
```

<!-- 语法节 end -->

## 是什么

**本页讲的是：怎么让一个 test method program 真的并行跑多个 site。**

**核心结论一句话**：**光开两个 flag 不够，程序里还得加 API。**
原文把这个落差写得很直白：

> 「With SmarTest, you can run a test suite that has a test method program with multi-site testing
> by setting up the **Parallel Mode Enable testflow flag** and **Allow Parallel test suite flag**;
> also, you can run a test suite that has a test method or user procedure. **However, the test
> method program is run sequentially for all sites**, such as a user procedure. **This serial
> execution for all sites means that maximum performance is not achieved.**」

**即：那两个 flag 让 test suite 跑起来了，但 test method program 仍然是「一个 site 一个 site」地跑。**
要拿满性能，必须往程序里补 API：

> 「To achieve maximum performance, **some APIs must be added to optimize your test method
> program**.」

### 并行的是哪一段、串行的是哪一段

这是本页最该先记住的边界：

| 阶段 | 单 site / 多 site 下的行为 |
|---|---|
| **setup 和 test 的执行** | **并行**（优化之后） |
| **post-test processing**（取结果、计算、判断等） | **对所有 site 串行** |

原文：

> 「This optimization enables **parallel execution of setup and test** …
> Then, **post-test processing (getting result, computation, judgment, and so on) is achieved
> serially for all sites**.」

> ⚠️ **一条很容易反过来的限制**，原文用 `Note` 单独写了：
> 「**Optimizing the testflow has no effect on the parallel execution of the test method program.
> It only affects the DC measurements in the test method program.**」
> **即：优化 testflow 和优化 test method program 是两件事，不能互相替代。**

### `first-invocation` block：并行的发生地

> 「you can define a block for parallel execution, called the **`first-invocation` block**.
> **This block is executed for all sites when the program is run for the first tested site.**
> Hence, in this block, **the setup and execution APIs work in parallel for all sites**.」

**触发时机是「程序在第一个被测 site 上运行时」**——不是每个 site 各跑一次。

### 两个焦点：setup focus 与 query focus

原文把这一页的机制压缩成「两个焦点」，本页照它的说法列：

| 焦点 | 在哪一段起作用 | 行为 |
|---|---|---|
| **setup focus** | 程序在第一个被测 site 上运行时 | **可以把某些 site 聚焦**，做 site-specific setup |
| **query focus** | 程序为**每个 active site** 运行时 | **Result API 总是只对「当前被测的那一个 site」工作** |

**Result API 的两步机制**（原文写得很具体，值得逐字留）：

> 「They store the measurement data of all sites into the **cache temporarily when the program is
> run for the first tested site**. They **return the measurement data for the currently tested site
> from the cache at each execution**.」

**即：第一个 site 跑的时候把**所有** site 的数据都存进 cache，之后每次执行从 cache 里取当前 site 那份。**

### API 清单：三组

原文把控制这些状态的 API 分成三组。**「这些 API 控制后面的 API 寻址哪些 site」**——这是它们的作用。

**① 控制 setup focus / query focus 的块级 API：**

| API | 干什么 |
|---|---|
| `ON_FIRST_INVOCATION_BEGIN` | **声明并行块的开始**——在程序跑第一个被测 site 时，这个块里的 setup 和 test 对**所有 site 并行** |
| `ON_FIRST_INVOCATION_END` | 声明 `ON_FIRST_INVOCATION_BEGIN` 开的块结束 |
| `FOR_EACH_SITE_BEGIN` | 声明「**并行测试之前**对所有 site 顺序做 setup」的块开始 |
| `FOR_EACH_SITE_BEGIN_WITH_QUERY` | 同上，但**顺序做 setup 和 query** |
| `FOR_EACH_SITE_END` | 上面两个块共同的结束标记 |
| `FOR_SEMI_PARALLEL_TEST_BEGIN` | 声明**半并行**测试块开始；**半并行的分组由 `SEMI_PARALLEL_CONFIG ()` 定义** |
| `FOR_SEMI_PARALLEL_TEST_END` | 声明 `FOR_SEMI_PARALLEL_TEST_BEGIN` 开的块结束 |

> **注意 `FOR_EACH_SITE_END` 一个 API 收两个 begin**：
> 原文写 `started by FOR_EACH_SITE_BEGIN **or** FOR_EACH_SITE_BEGIN_WITH_QUERY`。

**② 给「有限几个 API」控制 setup focus 的（原文指到 `Site-Specific Setup` 那篇）：**

| API | 干什么 |
|---|---|
| `SET_TEST_FOCUS` | 把指定的 site 设成 **setup-focus**；**可以同时把除某个 site 外的所有 enabled site 设成 not-setup-focus**；**返回这些 site 之前的状态** |
| `UNSET_TEST_FOCUS` | 把指定的 site 从 setup-focus 里去掉；**同样返回之前的状态** |

**③ 取信息的 API：**

| API | 返回什么 |
|---|---|
| `GET_TEST_FOCUS` | **setup-focused 的 site 数量 + site 号** |
| `GET_CONFIGURED_SITES` | **pin configuration 里配过的 site 数量 + site 号** |
| `GET_ENABLED_SITES()` | 当前 **enabled** 的 site（用于多 site 测试） |
| `GET_ACTIVE_SITES()` | 当前 **active** 的 site（当前正要跑这个 test method program 的） |
| `CURRENT_SITE_NUMBER()` | **当前被测 site 的 site 号** |

### 单 site 兼容：什么被忽略

> 「The APIs listed above **except for** `GET_TEST_FOCUS`, `GET_CONFIGURED_SITES`,
> `GET_ENABLE_SITES`, `GET_ACTIVE_SITES`, and `CURRENT_SITE_NUMBER` **are ignored in single-site
> testing**. Thus, you can develop test method programs that are **compatible with both single-site
> and multi-site tests**.」

**即：块级 API 和 focus 控制 API 在单 site 时被静默忽略，五个查询 API 照常工作。**
原文把它说成一条升级路径：**先按单 site 写，需要时再升到多 site。**

### TIA 的一个特例：default core

> 「If **two TIA cores are connected to one front-end module** in the GP-TIA/HP-TIA, and these two
> TIA cores are **assigned to two sites** for multi-site testing, you need to select the special
> core identifier called the **default core**.」

- **默认 core 是什么**：`a TIA that was assigned to each site`
- **在哪定义**：**pin configuration 里**
- **哪三个 API 要指定它**：`ANALOG().TIA()`、`Analog.TIA()`、`Routing.pin().connect()`

## 典型用法

**1. 先分清你要的是「能跑」还是「跑得快」**（本页自己归纳，依据是原文前两段）：

| 目标 | 要做什么 |
|---|---|
| **多 site 能跑起来** | 开两个 flag：**Parallel Mode Enable**（testflow flag）+ **Allow Parallel**（test suite flag） |
| **跑得快** | 在上面之上，**往 test method program 里加块级 API**（`ON_FIRST_INVOCATION_BEGIN` / `END` 那组） |

**2. 优化的写法（块结构）**：

```
ON_FIRST_INVOCATION_BEGIN      ← setup + test 对所有 site 并行
    （setup / execution API 全部放这里）
ON_FIRST_INVOCATION_END
    ↓
每个 site 各跑一次：Result API 从 cache 里取当前 site 的结果   ← 这一段是串行的
```

**3. 什么时候用 `FOR_EACH_SITE_BEGIN` 而不是 `ON_FIRST_INVOCATION_BEGIN`**：
原文的措辞是 `setup sequentially for all sites **before** parallel test`
——**要在并行之前对所有 site 顺序做 setup 时用它**；
`..._WITH_QUERY` 那条则是**连 query 也要顺序做**时用。

**4. 半并行**：`FOR_SEMI_PARALLEL_TEST_BEGIN` / `END` 把 site 分成组，
**组怎么分要先由 `SEMI_PARALLEL_CONFIG ()` 定**。**顺序不能反。**

**5. 只给某几个 site 做 site-specific setup**：在并行块里用
`SET_TEST_FOCUS` 聚焦 → 做 setup → `UNSET_TEST_FOCUS` 恢复。
**两个 API 都会返回之前的状态**，所以「改完恢复」是可实现的。

**6. `Before you begin` / `What to do next`**：**原文这篇没有这两节**，
所以本页没有「前置条件」和「下一步」可转述。

## 和谁有关

- [[testmethod]] — 本页优化的是 **test method program**
- [[testflow]] — **两个 flag 里的 `Parallel Mode Enable` 是 testflow flag**；
  但原文明确说**优化 testflow 不影响 test method 的并行**，两者是分开的两件事
- [[results]] — **query focus 那一整套机制就是 Result API 的行为**；本页只讲「它怎么取数」，
  **没有讲它返回什么、有哪些 API**
- [[run]] — `run` 阶段下「程序对每个 site 各跑一次」正是 query focus 的触发点
- [[on-first-invocation-begin]] / [[on-first-invocation-end]] — **本页并行机制的两个核心 API**
- [[for-each-site-begin]] / [[for-each-site-end]] — 顺序 setup 的两个 API
- [[site-control-window]] — 原文 `Related information` 里指的两个 GUI 场所之一
- [[site-focus-required-before-command]] — 该约束页讲的是「某条命令要求先聚焦 site」，
  **正是本页 `SET_TEST_FOCUS` 那套机制的后果**
- `Site Select view` / `How to do Multi-Site Testing` / `Generic Test Program Setup` /
  `Multi-site access functions` / `Setting Flags for Parallel Execution` / `Allow Parallel`（**均未建**）—
  原文 `Related information` 和正文里链出去的几篇；**本页一篇没读**
- `Site-Specific Setup` / `Parallel Execution` / `Measurement Data Management` /
  `Getting the Site Numbers` / `Accessing Site-Specific Flags and User Variables` /
  `Site States and Test Method Programs` / `API Behavior on Multisite Testing` /
  `Important Points on Multisite Programming` / `Multi-site Test Example` /
  `How to execute separate patterns per site (Label per site)`（**均未建**）—
  **本页 `Subtopics` 列的十篇，本页一篇没读**

## 版本

- **Introduced before SmarTest 6.3.2**

（原文 `## Functional changes` 只有这一条。）

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.03.13_Controlling_Multiple_Sites.md`

**本页没做的**：

- **`Subtopics` 列的十篇一篇没读**——这是本页最大的缺口。所以：
  **并行执行到底怎么调度、测量数据怎么管、site-specific setup 具体能给哪些 API 用、
  site states 有哪些、多 site 编程有哪些坑、有没有完整例子，本页一个字都没有。**
  本页**只有主文档自己讲的那一层机制**。
- **图两张没看**：`47481.png`（Serial Execution and Parallel Execution）、
  `47482.png`（Test Method Programs for Parallel Execution）。
  **本页对「并行/串行」的描述全部来自文字**——
  原文那两张图里**可能有本页没覆盖的结构细节**。
- **`Related information` 里的五篇没读**（见上）。
- **三组 API 里，第二组原文自己就把细节让给了 `Site-Specific Setup`**——
  **`SET_TEST_FOCUS` 到底影响哪些 API，本页不知道**，只知道它返回之前的状态。
- **`SEMI_PARALLEL_CONFIG ()` 怎么用没读**——**半并行的分组规则本页没有。**
- **原文没有 `## Procedure` / `## Before you begin` / `## What to do next`**，
  所以「典型用法」那一节里**除「两个 flag」和「块结构」之外的内容是本页从正文里整理的，
  不是原文的步骤**。
- **`default core` 在 pin configuration 里怎么定义，本页没读**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **同一个 API 在同一页里有两个拼法**——清单里写的是
> **`GET_ENABLED_SITES()`**，而紧接着下一段的排除句里写的是
> **`GET_ENABLE_SITES`**（**少了 `D`**）。**本页正文按清单里的 `GET_ENABLED_SITES()` 写**，
> 这里把两处并列记下，**不替语料统一**。
> ② **同一组 API 的写法不统一**：有的带空括号（`GET_ENABLED_SITES()`、
> `CURRENT_SITE_NUMBER()`），有的不带（`GET_TEST_FOCUS`、`GET_CONFIGURED_SITES`、
> `SET_TEST_FOCUS`、`ON_FIRST_INVOCATION_BEGIN`）。**两个带括号的都在第③组里。**
> ③ **`Related information` 一节里五条链接之间没有任何分隔符**，原文是
> `[…Site_Control_Window.md)[Site Select view](…`——**两条链接直接粘在一起**。
> ④ **`Note` 段落和它前面的内容之间没有换行**，原文两处都是这样，例：
> `[Computing Measurement Values](<…>)Note You need to execute the CONNECT sequence…`
> ——**链接收尾的 `)` 后面直接就是 `Note`。**

`verified: doc-only`
