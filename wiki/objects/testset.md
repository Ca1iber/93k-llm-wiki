---
type: object
title: TESTSET
layer: L2
stage: testmethod
tags: [testmethod, testset, judge-and-log, test-number, test-name, datalog, smc-framework, l2-api]
related: [test, limit, tmlimits, smartcalc-framework, on-first-invocation-begin, for-each-site-begin, test-method-class, test-suite, testname-requires-matching-limits, mapping-testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# TESTSET

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **11,154 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Using the same condition for multiple tests

If you wish to use the same condition for multiple TEST member functions, you can program the condition for the class object of the TESTSET. In this example, the conditions are set in the first line and effective for all the following three tests.

```
double dIdd1, dIdd2, dIdd3;

TESTNUMBER sdc6 = GET_TESTNUMBER("SDC_6");

TestSet.cont(true).testnumber(sdc6);

TestSet.TEST("Vcc","test1",dIdd1);
TestSet.TEST("Vcc","test2",dIdd2);
TestSet.TEST("Vcc","test3",dIdd3);
```

### Example 2: Generating test numbers

The TESTSET class can be used as a programmable interface for generating test numbers for each test in a test suite by assigning offset and increment values that iterate based on the number of calls. The examples below use the offset and increment values as shown in the table below.


> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/58886.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：Test Name | Offset | Increment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/58886.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：Test Name | Offset | Increment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/58886.htm`
> 中**第 5 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：25 行 × 2 列。
> 首行（上游原文）：subtest Test Number

### Example 4: Judge and Log Examples

```
ON_FIRST_INVOCATION_BEGIN();

    FUNCTIONAL_TEST();

ON_FIRST_INVOCATION_END();

TESTSET().judgeAndLog_FunctionalTest();
```

The first three lines perform a functional test for multi-site parallel, and the last line performs the judging and logging for each site respectively.

```
double thd_result, snr_result;

TESTSET().cont(true).judgeAndLog_ParametricTest("dgtz_pin", "THD", thd_result);
TESTSET().judgeAndLog_ParametricTest("dgtz_pin", "SNR", snr_result);
```

The first judgeAndLog_ParametricTest() judges the thd_result data as pass or fail. Then, the second one judges the snr_result data as pass or fail because the `TESTSET().cont(true)` is called in advance. When the result of the first judgeAndLog_ParametricTest() is pass, the test will continue even if you do not call the `cont(true)` member function.

```
double low_limit, high_limit, thd_result;

TESTSET().judgeAndLog_ParametricTest("Aout", THD",LIMIT(TM::GT, low_limit, TM::LT, high_limit), thd_result);
```

The judgeAndLog_ParametricTest() compares the thd_result data with the limit range specified by the LIMIT API, then judges as pass or fail.

```
TESTSET().judgeAndLog_ParametricTest("I/O0","ft_test",tmLimits,VMeas);
```

In this example, Vmeas is the variable containing the measured value. The judgeAndLog_ParametricTest() compares the value of VMeas with the limit range of the test name ft_test in the loaded test table. To use tmLimits, add the following two lines to the test method:

```
#include "TMLimits.h"
using V93kLimits::tmLimits;
```

The following example illustrates the binning rule of tmLimits, which bins on the first fail.

```
TESTSET().cont(true).judgeAndLog_ParametricTest(pin,"param1",tmLimits,value1);
TESTSET().cont(true).judgeAndLog_ParametricTest(pin,"param2",tmLimits,value2);
```

with

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/58886.htm`
> 中**第 6 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：Test name | Bin_s_num | Bin_h_num

Final bin depending on the parameters results:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/58886.htm`
> 中**第 7 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：param1 result | param2 result | Final bin (software / hardware bin)

The following example logs the result of a group of pins in one MPR if the STDF configuration option `enableMPR` is set to True (See the description of `enableMPR` in `Configuring the contents of an STDF file`（raw: `../02.10_Data_Logging/02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md`）).

```
PMU_VFIM pmuVfim(Pins);

ON_FIRST_INVOCATION_BEGIN();

    pmuVfim.vForce(Vforce)
        .iClamp(IClp*1E-6)
        .limits("Idd")
        .preAction("NONE")
        .settling(SoakT*1E-3)
        .execute(TM::PVAL);

ON_FIRST_INVOCATION_END();

TESTSET VfIm;

VfIm.testnumber(505).cont(TRUE).judgeAndLog_PmuVfim(pmuVfim);
```

### Example 5: Using TESTSET() in SMC background processing

The example shows how to implement TESTSET() for SMC background processing. The example contains the code for two versions of the background process:

- SMC background process per site
- Common SMC background process for all active sites

The example requires that the test limits are defined by a CSV file. For more information refer to `TMLimits`（raw: `02.07.04.01.250_TMLimits.md`） and `Working with TMLimits`（raw: `../02.10_Data_Logging/02.10.01.08.02_Working_with_TMLimits.md`）.

 The following definition of test method member variables is required in the protected section of the test method class:

```
protected:
    string      mSMCMode;
    string      mPinList;
    string      mTestSuite;
    string      mTestName;
    int         mMeasurements;
    int         mOffline;
    ARRAY_I     mActiveSites;
```

 A DC value test is defined in the run() method of the test class. Result processing is performed in an SMC background process per site or in a common SMC background process for all active sites.

```

virtual void run()
{
    PATTERN_CONTROLLER patternCtrl;

    ON_FIRST_INVOCATION_BEGIN();
    {
        //
        // Prepare
        //
        mSMCMode        = "COMMON_THREAD"; // "THREAD_PER_SITE" or "COMMON_THREAD"
        mPinList        = "PS1600_1,PS1600_2";
        mTestName       = "Test 1";
        mMeasurements   = 1;

        GET_SYSTEM_FLAG("offline",&mOffline);
        GET_TESTSUITE_NAME(mTestSuite);

        RESULT_AREA_CONFIG_SET resultArea(mTestSuite);

        resultArea.pin(mPinList).setDcValueResultAreaSize(mMeasurements);

        //
        // Create setup for DC value measurement
        //
        ...
        ...

        //
        // Execute
        //
        resultArea.setAsPrimary();

        CONNECT();

        SMC_FUNCTIONAL_TEST();

        resultArea.deselectGlobally();

        //
        // Result processing
        //
        if (mSMCMode == "THREAD_PER_SITE")
        {
            //--------------------------------------------------------------
            // SMC background thread per site
            //--------------------------------------------------------------
            FOR_EACH_SITE_BEGIN();
            {
                SMC_ARM();
            }
            FOR_EACH_SITE_END();
        }
        else if (mSMCMode == "COMMON_THREAD")
        {
            //--------------------------------------------------------------
            // Common SMC background thread for all active sites
            //
            // Note:    The array of currently active sites must be stored
            //          in the member variable mActiveSites.
            //--------------------------------------------------------------
            GET_ACTIVE_SITES(mActiveSites);

            SMC_ARM();
        }
        else
        {
            cout << "Invalid SMC mode \"" << mSMCMode << "\"." << endl;
        }
    }
    ON_FIRST_INVOCATION_END();

    return;
}
```

 The SMC background processing method of the test class is to be defined in the public section:

```
//
// The SMC background processing method; armed by SMC_ARM() in the run() method above
//
virtual void SMC_backgroundProcessing()
{
    DC_RESULT_ACCESSOR  resultAccess(mTestSuite);
    STRING_VECTOR       pinVector;

    //
    // Prepare
    //
    pinVector = PinUtility.getDigitalPinNamesFromPinList(mPinList,TM::ALL_DIGITAL);

    cout << "SMC_backgroundProcessing for SMC mode \""
         << mSMCMode << "." << endl << flush;

    if (mSMCMode == "THREAD_PER_SITE")
    {
        //------------------------------------------------------------------
        // Thread per site
        //------------------------------------------------------------------
        TESTSET testSet;

        if (!mOffline)
        {
            resultAccess.uploadResult(mPinList, TM::RESULT_INDEX);
        }

        for (uint pinIndex = 0; pinIndex < pinVector.size(); pinIndex++)
        {
            ARRAY_D results = resultAccess.getValues(pinVector[pinIndex]);

            for (int resultIndex = 0; resultIndex < mMeasurements; resultIndex++)
            {
                cout << "\t\tProcessing data for site " << SMC_SITE_NUMBER()
                        << ", pin " << pinVector[pinIndex]
                        << ", result " << resultIndex + 1 << endl << flush;

                testSet.cont(true).judgeAndLog_ParametricTest(pinVector[pinIndex],
                        mTestName, V93kLimits::tmLimits,
                        (mOffline) ? 1 : results[resultIndex]);

            } // for (int resultIndex ...

        } // for (uint pinIndex ...
    }
    else if (mSMCMode == "COMMON_THREAD")
    {
        //------------------------------------------------------------------
        // Common thread for all active sites
        //
        // Note:    The common thread requires that the array mActiveSites
        //          has been filled in the calling run() method.
        //------------------------------------------------------------------
        for (int siteIndex = 0; siteIndex < mActiveSites.size(); siteIndex++)
        {
            if(!mOffline)
            {
                resultAccess.uploadResult(mActiveSites[siteIndex],
                        mPinList,TM::RESULT_INDEX,
                        TM::RESULT_RANGE(TM::RESULT_INDEX,0,mMeasurements));
            }

            //
            // Create new TESTSET using the current site as parameter
            //
            TESTSET testSet (false, mActiveSites[siteIndex]);

            for (uint pinIndex = 0; pinIndex < pinVector.size(); pinIndex++)
            {
                ARRAY_D results = resultAccess.getValues(mActiveSites[siteIndex],
                                                         pinVector[pinIndex]);

                for(int resultIndex = 0; resultIndex < mMeasurements; resultIndex++)
                {
                    cout << "\t\tProcessing data for site " << mActiveSites[siteIndex]
                            << ", pin " << pinVector[pinIndex]
                            << ", result " << resultIndex + 1 << endl << flush;

                    testSet.cont(true).judgeAndLog_ParametricTest(pinVector[pinIndex],
                            mTestName, V93kLimits::tmLimits,
                            (mOffline) ? 1 : results[resultIndex]);

                } // for (int resultIndex ...

            } // for (uint pinIndex ...

        } // for (int siteIndex ...
    }
    else
    {
        cout << "Invalid SMC mode \"" << mSMCMode << "\"." << endl;
    }

} // virtual void SMC_backgroundProcessing()

```

 Note

The example above contains several calls of cout in function `SMC_backgroundProcessing()`（raw: `02.07.04.01.231.01_SMC_ARM.md#_120107__s_SMC_backgroundProcessing`）. cout is not thread safe. In production test cout must never be used in a background process.

When using cout in a background process, you have to expect a mix up of the output in the ui_report window and possibly other unwanted behavior. For more information, refer to `Thread safety`（raw: `02.07.10.02.02_Thread_safety.md`）.

<!-- 语法节 end -->

## 是什么

**TESTSET 是 test method 侧「判定 + 写 datalog + 结果编号」的主入口。** 原文第一句就把它定位成一个**数据容器**：

> The TESTSET class accesses a data container holding information that defines numbering procedures for results in a given test suite.

头文件 `/opt/hp93000/soc/prod_com/include/MAPI/TestSet_r.h`。**它管三件事**：**结果编号**、**判定并写日志**、**一组「设一次、后面所有调用都继承」的开关**。下面按这三件事分开写。

> **本页不重抄示例。** 上面「语法 / 参数」节的内容对应原文的 `## Examples` 段（脚本记 12,896 字符；本页实测原文那一段 13,164 字符，**差额本页没有核**），Example 1–5 的代码与表格都已经在那里了。**本页补的是脚本没抽的那几节**：首段、`## Class definition`、`## Syntax descriptions`、`## Related information`、`## Functional changes`。

### 一、结果编号：offset + increment

> The testname() and testnumber() functions are used with TESTSET to assign user defined names and numbers to specific tests. The testnumber member functions are used with the TESTSET API to define test numbering procedures, such as defining default numbering procedures.

**编号不是凭空来的，它会和别处的参数打架：**

> Test numbers are affected by other factors in addition to those described in TESTSET, TESTNUMBER, and GET_TESTNUMBER API topics. For example, you can enter loop iterations and global increment numbering parameters by using the Testflow Editor and the Parameter Dialog.

**而且编号要求一个 flag 先开着：**

> In order for test numbering to proceed, the test_number_enable testflow flag in the Testflow Editor must be enabled, see Generating Test Numbers for instructions on the use of these flags.

**「subtest Test Number」的定义**（Example 2 的注里，**这一句在「语法 / 参数」节里**）：

> A "subtest Test Number" refers to the number that is stored in the EDL. The numbers assigned to a test result can be modified and are affected by default and user-selectable numbering parameters. In this sense these test numbers are temporary.

**条件 → 结果**（Example 3 那张表读出来的，表本身在上面「语法 / 参数」节里）：

| 调用 | 该 test suite 接下来的 subtest Test Number |
|---|---|
| 默认（offset 1000 / increment 20） | 1000 → 1020 → 1040 |
| `testnumber("Func")`（表里 offset 2000 / increment 50） | 2000 → 2050 → 2100 |
| `testnumber(3000)`（只给 offset，无 increment） | 3000 → 3000 → 3000 |
| `testnumber_none()` | `---` → `---` → `---`（**不编号**） |
| `TESTNUMBER testnumber(4000, 100)` | 4000 → 4100 → 4200 |
| `testnumber_default()` | **1060 → 1080 → 1100** |

**最后一行要单独说**：`testnumber_default()` 出来的数**不是从 1000 重新开始，而是接着默认序列走到 1060**——也就是它把编号**交还给默认规则**，而默认规则**继续按调用次数累加**。**（推断）**依据是同一张表里默认序列走到 1040、而 `testnumber_default()` 那三格是 1060/1080/1100；**表里没有一句文字说「交还并续算」**。

**一处语料未写**：Example 2/3 的 offset/increment 是**按 test name 查出来的**（`testnumber("ADC_1")` → 777/3），但**本篇没有一句说那张带 offset/increment 的表配置在哪儿**；原文只把读者指向 `Generating Test Numbers`（本页没读）。

### 二、判定并写日志：`judgeAndLog_*`

> The purpose of these APIs is to easily find the judge and log API for the specific test. The TEST() APIs are currently used for judging and logging test results. However, they require greater effort to choose the proper API to use for the specific test because they share the same name but differ in the parameter numbers and/or types.

**命名约定分两半**：

> The first part, "judgeAndLog", indicates that this API will judge the whole test suite P/F according to the test result and will log the test result.

> The second part identifies the type of test where this API should be used.

**共 11 个 `judgeAndLog_*` 加 1 个 `doLog_*`**（取自原文 `#### Subtopics` 的清单）：

| 成员函数 | 名字里指的测试类型 |
|---|---|
| `judgeAndLog_FunctionalTest()` | 功能测试 |
| `judgeAndLog_ParametricTest()` | 通用参量测试；**签名里可带 `const LIMIT&` 或 `V93kLimits::TMLimits&`** |
| `judgeAndLog_PmuIfvm()` / `judgeAndLog_PmuVfim()` | PMU 的 IFVM / VFIM 两种测量 |
| `judgeAndLog_Dps()` / `judgeAndLog_DpsVfim()` | DPS（`DPS_TASK` / `DPS_VFIM`） |
| `judgeAndLog_Spmu()` | SPMU |
| `judgeAndLog_PpmuMeasure()` | PPMU 测量 |
| `judgeAndLog_SpecSearch()` | spec search |
| `judgeAndLog_PptiaTask()` | ppTIA 测量 |
| `judgeAndLog_ScanTest()` | scan |
| `judgeAndLog_DcResultAccessor()` | DC 结果访问器 |
| `doLog_ShmooTest()` | shmoo（**只写日志，不判 P/F**，见下） |

**`doLog_ShmooTest()` 是个例外**：它的名字里没有 `judgeAndLog`，签名是 `void doLog_ShmooTest(const std::string &testname, const ShmooData& shmooData);`，**返回 `void` 而不是 `bool`**。**（推断）**：按上面那条命名约定（`judgeAndLog` 才判整个 test suite 的 P/F），它只负责写日志；依据是约定句 + 签名返回 `void`。

### 三、`member_func()`：设一次，后面都继承

这是 Example 1 那个用法的机制，原文两句：

> If you wish to use the same condition for multiple TEST member functions, you can program the condition for the class object of the TESTSET.

> If a function sets up a parameter, the parameter setting is kept until you reset it or return it to a default setting.

**四种用法形态**（原文 `## Syntax descriptions` 一节逐个列了）：

> Where member_func() is noted, you can use any of these member functions, individually or in combination:

> Because these member functions are optional, you can also omit them.

| 形态 | 写法 | 说明 |
|---|---|---|
| 临时对象 | `TESTSET().member_func().judgeAndLog_xxx(parameters);` | 一次性，每次都新建 |
| 临时对象 + 指定 site | `TESTSET(false, site).member_func().judgeAndLog_xxx(parameters);` | **文档里只有 SMC common thread 用这一种** |
| 系统预置对象 | `TestSet.member_func().judgeAndLog_xxx(parameters);` | 常规写法；**SMC 框架里不能用** |
| 用户对象 | `TESTSET obj;` 然后 `obj.member_func().judgeAndLog_xxx(parameters);` | 要长期复用同一套设定 |

`member_func()` 这个位置能放的 8 个成员函数（原文逐个列了）：`cont()`、`port()`、`reliabilty()`（⚠️ 原文如此，见「出处」）、`testname()`、`testname_default()`、`testnumber()`、`testnumber_default()`、`testnumber_none()`。

**`cont(true)` 的语义**（Example 4 的正文）——`cont(true)` = **后面的判定即使失败也继续**；而**前一次判定是 pass 时本来就继续**，所以可以不写：

> When the result of the first judgeAndLog_ParametricTest() is pass, the test will continue even if you do not call the cont(true) member function.

### 线程与 SMC：三条「不许」

> TESTSET class objects must not be shared across multiple threads.

> If used in SMC background processing, TESTSET class objects should be created and used only within the SMC_backgroundProcessing() method.

> The system-prepared object cannot be used within the SMC framework.

**再加两条 binning 规则。** 用 TESTSET 替代 `SMC_TEST` 时：

> If you use TESTSET within the SMC framework instead of SMC_TEST, binning happens in SMC_SYCHRONIZE according to the binning rules as for SMC_TEST.

**另一条**：SMC 框架与 TESTSET test suite **各自独立**时，binning 走另一套规则（原文指向 `Use of TESTSET and SMC_TEST() test suites with multibin`，本页没读）。

**`TESTSET(false, site)` 这个构造函数在文档里的唯一用途**是 Example 5 的 common thread——按 `mActiveSites` 逐个 site 建对象：

> This constructor creates the class object as defined above and additionally defines the site to be processed. The parameter withContext is to be set to false.

上面「语法 / 参数」节 Example 5 末尾还带一条 `cout` 警告（原文 `cout is not thread safe`），**那一节已经在了，本页不重复**。

## 典型用法

**A. 只想判定并写一条日志（最常见）**

1. **要编号的话，先确认 `test_number_enable` 这个 testflow flag 在 Testflow Editor 里开着**——不然编号那套整个不生效。
2. 挑对 `judgeAndLog_*`：**按测试类型对号**（上面第二节那张表）。这就是 TESTSET 存在的理由——原文说 `TEST()` 虽然也能判定，但「挑对重载」很费劲。
3. 一次要判几个量、又不想第二条在前一条 fail 时被跳过 → 前面挂 `.cont(true)`。
4. 要自己给 limit → 用带 `const LIMIT&` 或 `V93kLimits::TMLimits&` 的那个重载。

**B. 要自己定编号（Example 1–3 的路子）**

1. 先建编号量：`TESTNUMBER sdc6 = GET_TESTNUMBER("SDC_6");`，或者 `TESTNUMBER t(4000, 100);` 直接给 offset/increment。
2. `TestSet.cont(true).testnumber(sdc6);`（或 `obj.testnumber(...)`）——**这一步设的是「类对象上的条件」，后续调用都继承**。
3. 接下来所有 `TEST()` 调用都按这套规则编号，**直到你用 `testnumber_default()` 交还默认、或 `testnumber_none()` 关掉编号为止**。

**C. 要在 SMC 后台里判定（Example 5 的骨架，四步）**

1. test method class 的 `protected` 段备好 7 个成员：`mSMCMode` / `mPinList` / `mTestSuite` / `mTestName` / `mMeasurements` / `mOffline` / `mActiveSites`。
2. `run()` 里在 `ON_FIRST_INVOCATION_BEGIN()` … `ON_FIRST_INVOCATION_END()` 之间跑测量，并按模式分叉：
   - `THREAD_PER_SITE`：`FOR_EACH_SITE_BEGIN()` 里逐个 site 调 `SMC_ARM()`；
   - `COMMON_THREAD`：先 `GET_ACTIVE_SITES(mActiveSites);`（**把活动 site 存进成员变量**），再 `SMC_ARM();`。
3. `SMC_backgroundProcessing()` 里按同一个 `mSMCMode` 分支处理结果；**common thread 必须一个 site 建一个对象**：`TESTSET testSet (false, mActiveSites[siteIndex]);`。
4. **原文只说这三个可以在 SMC 框架里用**：`judgeAndLog_ParametricTest()`（7.1.4 起）、`judgeAndLog_FunctionalTest()` 与 `judgeAndLog_ScanTest()`（7.2.2 起）。**其余八个它没说**——本页**不替它下结论**说「不行」。

**D. 两种模式的结果处理差别**（Example 5 的代码里能直接看出，本页只照实记）：`THREAD_PER_SITE` 用 `SMC_SITE_NUMBER()` 取当前 site；`COMMON_THREAD` 用外层的 `mActiveSites[siteIndex]`。**offline 时两边都拿常数 `1` 顶替测量值**（`(mOffline) ? 1 : results[resultIndex]`）。

## 和谁有关

**入边 119 条 / 71 篇**（`edges.jsonl`，`inline` 口径；自指只有 1 条）。最密的几篇是 `02.07.04.01.242_TESTNUMBER.md`（5）、`03.02.02.06.07_Use_of_multibins.md`（5）、`02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md`（3）。**它们是「哪几篇文档主动链到本页」的证据，不是本页读过它们。**

- [[test]] — **上游／替代**：`judgeAndLog_*` 是 `TEST()` 的替代入口。原文说 `TEST()` 是「currently used」，`judgeAndLog_*` 是为了免去挑重载而加的（上一节那段引文）。
- [[limit]] — **文档事实**：TESTSET 自己的签名清单里有 `bool TESTSET::judgeAndLog_ParametricTest(const STRING &pin, const STRING &testname, const LIMIT& limit, DOUBLE value);`——**LIMIT 是本页判定入口的参数类型**。
- [[tmlimits]] — 同一个签名族里还有 `V93kLimits::TMLimits& tmLimit` 的版本；Example 4/5 用的就是它，**binning 规则也由它定**（`bins on the first fail`）。
- [[smartcalc-framework]] — **双向**：TESTSET 有三个函数可在 SMC 框架里用；SMC 侧两条 binning 规则又都指回 TESTSET。边数据里 `SMC_TEST`（6 条）也链到本页。
- [[on-first-invocation-begin]] / [[for-each-site-begin]] — 示例里的两个作用域块；**边是双向的**（`ON_FIRST_INVOCATION_BEGIN` 那篇链到本页）。
- [[test-method-class]] — **宿主**：TESTSET 对象活在 test method class 里，`SMC_backgroundProcessing()` 是它的成员函数（Example 5 的 `protected` / `public` 段就是这么分的）。
- [[test-suite]] — **作用域**：编号定义的是「a given test suite」的结果编号；`judgeAndLog_*` 判的也是**整个 test suite** 的 P/F。
- [[testname-requires-matching-limits]] — **（推断）**`testname()` 设的就是那条约束管的那个名字。依据：那条约束的标题与它自己的 `sources:`（本页只看了标题，**没有读它的正文**）。
- [[mapping-testmethod]] — 跨层对照那一页把 TESTSET 填在「判定并写 datalog」那行的 L2 格，并在同一格写了 [[test]] 与 [[limit]]。
- **33 个子主题**（`TESTSET().testnumber()` … `TESTSET().testtype_default()`，即 `02.07.04.01.244.01`–`.33`）**一篇没读、也都没有页**——这里只用反引号写名字，不给链接。
- **`task-list` / `event-value-double` / `event-value-int`：语料未写它们和 TESTSET 的关系。** 本页**没有替它们编**：本篇原文里 `TASK_LIST` 出现 **0** 次、`EVENT_VALUE` 出现 **0** 次（实测）。它们和本页同属 test method 参考，但那只是**目录位置相邻**，不是文档写的关联。

## 版本

原文 `## Functional changes` 共 20 条，逐条照录：

- **`Introduced before SmarTest 6.3.2`** —— ⚠️ 这一条是**哨兵值**，**不是「6.3.2 的变更」**：`before` 的意思是「**在本套文档集覆盖范围开始之前就已经有了**」（§11.2 ②）。
- **SmarTest 6.5.0**：新增成员函数 `judgeAndLog_ScanTest()`
- **SmarTest 6.5.1**：`testtext()` 的文本可以**替换** `Test_TXT` 的内容、也可以**追加**到它后面
- **SmarTest 6.5.2**：新增成员函数 `doLog_ShmooTest()`
- **SmarTest 6.5.2**：新增成员函数 `judgeAndLog_Dps()`
- **SmarTest 6.5.2**：新增成员函数 `judgeAndLog_Spmu()`
- **SmarTest 6.5.3**：新增成员函数 `hlmfmt()`、`llmfmt()`、`resfmt()`（⚠️ 原文全小写，见「出处」⑦）
- **SmarTest 7.0.3**：Removed test number manager
- **SmarTest 7.1.0**：Added specifications for judgeAndLog_FunctionalTest()
- **SmarTest 7.1.4**：`judgeAndLog_ParametricTest()` 增强，**可在 SMC 框架里用**
- **SmarTest 7.1.4**：新增成员函数 `combineMultiPortTests()`
- **SmarTest 7.2.0**：Removed test_number_manager flag
- **SmarTest 7.2.1**：新增成员函数 `suppressTestnameLoopCount()`
- **SmarTest 7.2.2**：`judgeAndLog_FunctionalTest()` 与 `judgeAndLog_ScanTest()` 增强，**可在 SMC 框架里用**
- **SmarTest 7.5.0**：新增成员函数 `addAlarm()`
- **SmarTest 7.5.1**：New signatures for testnumber()
- **SmarTest 7.5.2**：Renamed forceSTDFTestNam parameter to forceSTDFTestName

**两处值得对一下**：

- **`7.1.4` 与 `7.2.2` 那三条「可在 SMC 框架里用」和正文那句 Note 说的是同一批函数**——版本段与正文**对得上**（正文的 Note 列了 `judgeAndLog_ParametricTest()`、`judgeAndLog_FunctionalTest()`、`judgeAndLog_ScanTest()` 三个）。
- **`7.5.2` 那一条的两个名字原文都写成 `...Nam` / `...Name`**，本页照实并列，**不替它归一**（见「出处」⑧）。

**一条使用上的门槛**：上面 20 条里最后的日期是 `7.5.2`，**本 wiki 面向 7.10.3**——**这张表没有覆盖 7.5.2 之后的任何变更**（原文如此，不是本页漏抄）。

## 出处

`sources:` 一篇：`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.md`（TDC `58886.htm`，31,120 字节，588 行）。**整篇读完。**

**本页做了什么**

补的是脚本没抽的那几节：首段、`## Class definition`、`## Syntax descriptions`、`## Related information`、`## Functional changes`，以及 `#### Subtopics` 那张 33 项的清单。上面「语法 / 参数」节是原文 `## Examples` 段的内容，本页**没有重复抄它**，只在需要时说清「这一句在上面那一节里」。

**本页没做的**

- **33 个子主题一篇没读**（`02.07.04.01.244.01`–`.33`：`TESTSET().addAlarm()`、`TESTSET().cont()`、`TESTSET().testnumber()`……）。所以**每一个成员函数自己的参数、返回值、适用条件，本页都不知道**，只写了原文正文顺带提到的那几处。
- **`## Related information` 指的两篇没读**：`02.07.04.01.242_TESTNUMBER.md`、`02.07.04.01.99_GET_TESTNUMBER.md`。
- **正文链出去、本页没读的**：`Generating Test Numbers`（`02.10.01.08`）、`TMLimits`（`02.07.04.01.250`）、`Working with TMLimits`、`Thread safety`（`02.07.10.02.02`）、`Configuring the contents of the STDF file`、`Use of SMC_TEST() with multibin`、`Use of TESTSET and SMC_TEST() test suites with multibin`、`SMC_ARM`、`SMC_TEST`、`SMC_SYNCHRONIZE`、`DC_RESULT_ACCESSOR`、`PMU_VFIM`、`Alphabetical list of flags`。**「offset/increment 那张表配置在哪儿」这个缺口本页因此没答**——答案多半在那几篇里，本页没有依据。
- **没有实跑。** 没有建过 test method、没有编译过、没有跑过 test suite。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有动别的页。

**图（§11.4）**

**本页 sources 那一篇里没有图。** 判据（可核）：转换出来的 `.md` 里 `png` / `jpg` / `!` 开头的图片标记命中均为 **0**；**上游 `tdc-html/raw/58886.htm` 里 `<img` 命中 0**。所以本页**没有任何 ④ 图证——不是「图够不着」，是这篇文档本来就不带图。**

**编码与整词替换（照实记，一处都没替它改）**

- **汉字坏字 0 处**（判据 `[一-鿿]` 命中 0）。本页没有 `碌`/`渭`/`卤`/`惟` 那一族。
- **`DC/DC power units`（`Index` 被整词替换那一族）命中 0 处**——本页所有代码与标识符可以照抄。

**⚠️ 语料瑕疵（10 处，照实记，一处都没替它改）**

- **① `dac _1`**：Example 2 正文写成 `The dac _1 test suite is assigned only an offset value`——**`dac _1` 中间多一个空格**（代码里是 `dac_1`）。
- **② 代码块缺分号**：`dac_1.testnumber("DAC_1")` **后面没有 `;`**，而前一行的 `adc_1.testnumber("ADC_1").TEST(...);` 有。
- **③ 引号不成对**：`TESTSET().judgeAndLog_ParametricTest("Aout", THD",LIMIT(TM::GT, low_limit, TM::LT, high_limit), thd_result);` 里 **`THD"` 少一个左引号**。
- **④ 同一个名字两种拼法**：`## Syntax descriptions` 的 placeholder 清单写 **`reliabilty()`**，而 `## Class definition` 的成员函数清单写 **`reliability()`**（链接目标文件也叫 `..._reliability.md`）。**两条都在同一篇里。**
- **⑤ 链接文字拼错**：正文写 `[SMC_SYCHRONIZE](<02.07.04.01.231.43_SMC_SYNCHRONIZE.md>)`——**链接文字 `SMC_SYCHRONIZE` 少一个 `N`**，目标文件名是 `SMC_SYNCHRONIZE`。
- **⑥ `## Related information` 两个链接之间没有任何分隔**：原文是 `[TESTNUMBER](<…>)[GET_TESTNUMBER](<…>)`，渲染出来是 `TESTNUMBERGET_TESTNUMBER`。
- **⑦ 大小写不一致**：`## Functional changes` 写 `New member functions hlmfmt(), llmfmt(), resfmt()`（全小写），而两处成员函数清单写 `hlmFmt()` / `llmFmt()` / `resFmt()`。§11 要求大小写原样保留——**同一篇里两种写法，本页并列，不归一**。
- **⑧ 版本条目里的旧名**：`SmarTest 7.5.2: Renamed forceSTDFTestNam parameter to forceSTDFTestName`——**原文如此**。哪一个是笔误、旧名到底叫什么，语料没说。
- **⑨ `## Syntax descriptions` 里链接标记本身是坏的**：`TESTSET().[cont(true)](<…>).[judgeAndLog_FunctionalTest()](<…>);`——**`[` 跑到函数名中间去了**；脚本转成 `` `文本`（raw: `路径`） `` 之后这一行仍看得出。同一节里 `[judgeAndLog_Dps();](<…>)` **把分号包进了链接文字**，而别的条目没有。
- **⑩ 表格被压平**：Example 3 那张表在 HTML→markdown 里被拆成「一格一行 + 空行」的形态（上面「语法 / 参数」节能直接看到），**段间还夹着单独的 `   | |` 行**。

`verified: doc-only`
