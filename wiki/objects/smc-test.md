---
type: object
title: SMC_TEST()
layer: L2
stage: testmethod
tags: [testmethod, l2, test-method-api, smartcalc, smc, datalog, binning, multibin, multisite, tmlimits]
related: [smartcalc, smartcalc-framework, hidden-upload, smc-background-process-locks-config, testset, limit, tmlimits, for-each-site-begin, for-each-site-end, on-first-invocation-begin, on-first-invocation-end, mapping-results, testmethod, test-method-class, smartest-6.5.3, smartest-7.3.4, smartest-7.4.5, smartest-7.5.3]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# SMC_TEST()

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **13,988 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void SMC_TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue = FALSE, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean  Continue = FALSE, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "", INT logTestNumber = -1);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, const STRING& testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean  Continue = FALSE, const STRING& testtext= "");
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT logTestNumber = -1, const STRING& softbin = "", INT hardbin = -1);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, const STRING& testtext);
```

Additional interface which allows specifying the site:

```
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue = FALSE, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean  Continue = FALSE, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, const STRING& testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean  Continue = FALSE, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, const STRING& testtext= "");
```

To avoid ambiguity when a `const char *` (string) is given as testtext parameter we provide explicit versions of all of those signatures with default parameters as well (as the compiler would otherwise prefer conversion to a Boolean (i.e. Continue parameter), over conversion via STRING constructor with `const char *`):

```
void SMC_TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean  Continue, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean  Continue, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, const char * testtext);
```

Additional interface which allows specifying the site:

```
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean  Continue, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean  Continue, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, const char * testtext);
```

This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/SMART_CALC2.h.

 Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/120084.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Example 1: General usage

SMC_TEST() compares the thd_result data with the limit range specified in the parameter dialog of `SMC_SYNCHRONIZE()`（raw: `02.07.04.01.231.43_SMC_SYNCHRONIZE.md`）, then judges it as pass or fail.

```
SMC_TEST("dgtz_pin", "THD", thd_result);
```

The first SMC_TEST() call judges the thd_result data as pass or fail. Then the second SMC_TEST() judges the snr_result data as pass or fail because the TM::CONTINUE is set int the first SMC_TEST(). When the result of the first SMC_TEST() is pass, the test will continue even if you do not set the Continue parameter to TRUE.

```
SMC_TEST("dgtz_pin", "THD", thd_result, TM::CONTINUE);
SMC_TEST("dgtz_pin", "SNR", snr_result);
```

SMC_TEST() compares the thd_result data with the limit range specified by the `LIMIT`（raw: `02.07.04.01.126_LIMIT.md`） API, then judges as pass or fail.

```
SMC_TEST("Aout", "THD", LIMIT(TM::GT, low_limit,TM::LT, high_limit), thd_result);
```

SMC_TEST() compares the thd_result data with the limit range specified by the `LIMIT`（raw: `02.07.04.01.126_LIMIT.md`） API, then judges as pass or fail. In fail case it will bin into the specified softbin and hardbin.

```
SMC_TEST("Aout", "THD", LIMIT(TM::GT, low_limit,TM::LT, high_limit), thd_result, false, testNumber, "softbin", hardbin);
```

### Example 2: Using hidden data logging

The following example shows how hidden data logging can be implemented using the `LIMIT`（raw: `02.07.04.01.126_LIMIT.md`） class, without having the hidden_datalog_mode testflow flag enabled.

```
#include "testmethod.hpp"
#include "mapi.hpp"

using namespace std;

class hiddenDatalogWLimit: public testmethod::TestMethod
{
protected:

    virtual void initialize()
    {
        addLimit("TestName");
    }

    virtual void run()
    {
        ON_FIRST_INVOCATION_BEGIN();
        {
            SMC_EXECUTE_TEST( 1.0 );

            LIMIT lim = GET_LIMIT_OBJECT("TestName");

            FOR_EACH_SITE_BEGIN()
            {
                SMC_ARM(lim);
            }
            FOR_EACH_SITE_END();
        }
        ON_FIRST_INVOCATION_END();

        return;
    }

public:

    void SMC_backgroundProcessing(LIMIT lim)
    {
        INT    site   = SMC_SITE_NUMBER();
        double result = ...;

        cout << "Site: <" << site << "> " << endl;

        SMC_TEST(site, "PinName","TestName", lim, result);
    }
};
REGISTER_TESTMETHOD("hiddenDatalogWLimit", hiddenDatalogWLimit);
```

 Note

The example above contains a call of cout in function `SMC_backgroundProcessing()`（raw: `02.07.04.01.231.01_SMC_ARM.md#_120107__s_SMC_backgroundProcessing`）. cout is not thread safe. In production test cout must never be used in a background process.

When using cout in a background process, you have to expect a mix up of the output in the ui_report window and possibly other unwanted behavior. For more information, refer to `Thread safety`（raw: `02.07.10.02.02_Thread_safety.md`）.

### Example 3: Using test tables

The following two examples show how to use the limits and bins that a user has defined in a test table ( *.csv file). tmLimits causes SMC_TEST() to look at the loaded test table file and to compare the value contained in result to the limits of "PowerOut0" and to bin the result accordingly.

```
SMC_TEST("dgtPinName", "PowerOut0", tmLimits, result, true);
SMC_TEST("dgtPinName", "PowerOut0", V93kLimits::tmLimits, result, true);
```

Do not use the following code for background processing, because this will use the system prepared TestSet object, which is not thread safe!

```
SMC_TEST("dgtPinName", "PowerOut0", tmLimits.getLimitObj("PowerOut0"), result, true);
```

### Example 4: Handling large numbers of sites

The following example shows how to speed up the SMC_TEST() execution when the large numbers of sites increase the total computing time.

The transfer of the required data from function run() to function backgroundProcessing() is done via member variables mResultArray and mActiveSitesArray. Transferring the data as parameter of SMC_ARM() is also supported but this will increase the test time because all data that are transferred to the background process must be copied by SMC_ARM(). The array mActiveSitesArray must be updated in function run() before function SMC_backgroundProcessing() is called to ensure that only activated sites are processed.

```
#include "testmethod.hpp"
#include "mapi.hpp"

using namespace std;

class hiddenDatalogSequential: public testmethod::TestMethod
{
protected:

    ARRAY_D mResultArray;
    ARRAY_I mActiveSitesArray;

    virtual void initialize()
    {
    }

    virtual void run()
    {
        ON_FIRST_INVOCATION_BEGIN();
        {
            //
            // Initialize the result array for all configured sites
            //
            ARRAY_I configuredSitesArray;

            mResultArray.resize (GET_CONFIGURED_SITES(configuredSitesArray));
            mResultArray.init   (-1.0);

            //
            // Start functional test and retrieve the result for active sites
            //
            FUNCTIONAL_TEST();

            FOR_EACH_SITE_BEGIN()
            {
                Boolean result = GET_FUNCTIONAL_RESULT();

                mResultArray[CURRENT_SITE_NUMBER()-1] = (double) result;
            }
            FOR_EACH_SITE_END();

            //
            // Show the result array
            //
            cout << "Result array:";

            for (int index = 0; index < mResultArray.size(); index++)
            {
                cout << " " <<  mResultArray[index];
            }

            cout << endl;

            //
            // Get and show active sites
            //
            GET_ACTIVE_SITES(mActiveSitesArray);

            cout << "Active sites:";

            for (int index = 0; index < mActiveSitesArray.size(); index++)
            {
                cout << " " << mActiveSitesArray[index];
            }

            cout << endl;

            //
            // Arm the SMC_backgroundProcessing() method
            //
            // Note: Data are transferred by member variables mResultArray[] and mActiveSitesArray[].
            //
            SMC_ARM();
        }
        ON_FIRST_INVOCATION_END();

    } // virtual void run()

public:

    void SMC_backgroundProcessing()
    {
        //
        // Parse the resultArray array for all active sites
        //
        for (int index = 0; index < mActiveSitesArray.size(); index++)
        {
            double result = mResultArray[mActiveSitesArray[index] - 1];

            cout << "SMC - Processing site " << mActiveSitesArray[index] << " - Result = " << result << endl;

            SMC_TEST(mActiveSitesArray[index], "PinName", "TestName", result);
        }

    } // void SMC_backgroundProcessing ...

}; // class hiddenDatalogSequential: public testmethod::TestMethod

REGISTER_TESTMETHOD("hiddenDatalogSequential", hiddenDatalogSequential);
```

Note

The example above contains a call of cout in function `SMC_backgroundProcessing()`（raw: `02.07.04.01.231.01_SMC_ARM.md#_120107__s_SMC_backgroundProcessing`）. cout is not thread safe. In production test cout must never be used in a background process.

When using cout in a background process, you have to expect a mix up of the output in the ui_report window and possibly other unwanted behavior. For more information, refer to `Thread safety`（raw: `02.07.10.02.02_Thread_safety.md`）.

 In offline mode, the example above results in the following output in the ui_report window if eight sites are configured, sites 3 and 7 are deactivated:

```
Result array: 1 1 -1 1 1 1 -1 1
Active sites: 1 2 4 5 6 8
SMC - Processing site 1 - Result = 1
Testsuite: Test_2 PASSED on site 1
SMC - Processing site 2 - Result = 1
SMC - Processing site 4 - Result = 1
SMC - Processing site 5 - Result = 1
SMC - Processing site 6 - Result = 1
SMC - Processing site 8 - Result = 1
Testsuite: Test_2 PASSED on site 2
Testsuite: Test_2 PASSED on site 4
Testsuite: Test_2 PASSED on site 5
Testsuite: Test_2 PASSED on site 6
Testsuite: Test_2 PASSED on site 8
```

<!-- 语法节 end -->

## 是什么

**`SMC_TEST()` 是 SmartCalc（`SMC`）框架里「判一条测量值 + 记账」的那一个函数。**

> The API judges the test data as pass/fail and logs it. It holds information that defines numbering procedures for results in a given test suite.

> The testname and testNumber parameters are used to assign user defined names and numbers to specific tests. In addition SMC_TEST() also supports the usage of soft- and hardbins.

**它在后台线程里被调用**（在 `SMC_backgroundProcessing()` 里），判的是**已经算完的值**，
判完**不立刻落盘**。头文件是 `/opt/hp93000/soc/prod_com/include/MAPI/SMART_CALC2.h`。

### 最关键的一条机制：**它当场不写日志，写日志发生在 `SMC_SYNCHRONIZE()`**

> SMC_TEST() buffers the data log values and outputs them as soon as the synchronization point (SMC_SYNCHRONIZE()) is reached in the order as the different background threads are started. The first fail will decide about the fail bin in which SMC_SYNCHRONIZE() will bin.

**这句话拆成三件事，每件都会影响你怎么写程序**：

| 事实 | 后果 |
|---|---|
| **buffers**（先缓存） | `SMC_TEST()` 返回时，**data log 里还没有这条记录** |
| **按后台线程启动的顺序输出** | 日志里的**次序由线程启动顺序定**，不由你调 `SMC_TEST()` 的先后定 |
| **`The first fail will decide about the fail bin`** | **多 site 的 fail bin 由「第一个 fail」决定**——不是逐条各分各的 |

**推论（本页的推断，依据就是上面那句）**：`SMC_TEST()` 与 `SMC_SYNCHRONIZE()`
**不是两个可以随便分开用的 API，是一对**——前者排队、后者结算。
**`SMC_SYNCHRONIZE()` 那一页才是「什么时候真的落盘」的答案**（**本页没读那篇**，见「出处」）。

### 它把两件事合在了一个函数里，因此带来一条前置条件

> SMC_TEST() combines functionalities of TESTSET.judgeAndLog_ParametricTest() and SET_MULTIBIN(). Since SMC_TEST() inherently uses SET_MULTIBIN(), it is required to define multibins in the test flow at the test suite that contains the SMC_SYNCHRONIZE() command (usually the last test suite in the testflow). Failure to insert multibins will lead to anomalies in behavior.

**条件 → 结果**：

| 情形 | 结果 |
|---|---|
| 在**含 `SMC_SYNCHRONIZE()` 的那个 test suite**（通常是 testflow 里最后一个）**定义了 multibin** | 正常 |
| **没定义 multibin** | **行为异常**（原文：`anomalies in behavior`） |

**注意这个责任的落点很反直觉**：`SMC_TEST()` 的**调用点**在后台线程里，
**而它要的前置条件却在另一个 test suite 上**——**「在哪调」和「在哪配」不是同一个地方**。

### 线程安全：**`TestSet` 不能用，这是这一页最硬的一条禁令**

> The system-prepared object TestSet is not thread safe! Do not use it with SmartCalc.

**合法的两条路**：用 `SMC_TEST()`，或用**动态创建的** `TESTSET().judgeAndLog_...()`。
**限制的来源是「对象是谁造的」**：**系统预备的那个 `TestSet` 对象不是线程安全的**，
而后台线程是并行的。这条禁令在例子里出现了两次（Example 2 与 Example 3），
Example 3 说得更具体：

> Do not use the following code for background processing, because this will use the system prepared TestSet object, which is not thread safe!

**同一个家族的另一条，是 `cout`**（**两处 Note**，逐字相同）：

> cout is not thread safe. In production test cout must never be used in a background process.

**两句合起来读**：**后台线程里不能用 `TestSet`、不能用 `cout`**——
**所以示例里那些 `cout` 都是「给人看流程」的，不是能进生产的写法**（原文自己点了这件事）。

### 与 `TESTSET` 混用时的分 bin 归属（**一处语料拼写错误**）

> If you use TESTSET within the SMC framework instead of SMC_TEST, binning happens in SMC_SYCHRONIZE according to the binning rules as for SMC_TEST.

**`SMC_SYCHRONIZE` 少了一个 `H`**（正确是 `SMC_SYNCHRONIZE`）——**本页照录，不替它改**（§11.2）。
语义上这条说的是：**换用 `TESTSET` 不影响「谁在哪分 bin」**，规则同 `SMC_TEST`。

### `reliability` 参数：**能标不可靠，但可靠它不记**

原文给了两半，**必须一起读**：

- 「不可靠」会**连 `TEST` API 一起**记进 event data log：

> With the reliability parameter set to TM::UNRELIABLE, the TEST API also logs the unreliable state to the event data log stream with the test data such as pass/fail, result values, and so on.

- 而「可靠」**根本不写**（参数表里的 Note）：

> SMC_TEST() does not log the reliable state even if the parameter is set to TM::RELIABLE.

**两半合起来的实际含义：`TM::RELIABLE` 与「省略该参数」在日志上等价**——
**它不是「确认可靠」的标记，它是默认态**。

### 大 site 数是一条性能分岔路

> If the number of sites is large (for example, 96 or more) the SMC_ARM() overhead time increases a lot. Consequently the SMC_TEST() will take longer to finish.

**文档给的解法**：**`SMC_ARM()` 只调一次（对所有 site）**，
然后**按 site 号顺序逐个调 `SMC_TEST()`**——即**从「每 site 一个后台线程」改成「顺序处理」**。
Example 4 就是这条路的完整写法（数据用成员变量传，详见「典型用法」）。

### 三族签名（脚本已逐字抄在上面，这里只解释「为什么有三族」）

| 族 | 区别 |
|---|---|
| **基础族** | 只有 `pin` / `testname`，没有 `site`——**在后台线程里用**（site 由线程自己带） |
| **`INT site` 前缀族** | 显式指定 site——**顺序处理时用**（Example 2 / 4 都是这一族） |
| **`const char *` 显式族** | 参数默认值全去掉的版本，**为绕开 C++ 重载歧义** |

**第三族存在的理由，原文自己写了**：

> To avoid ambiguity when a const char * (string) is given as testtext parameter we provide explicit versions of all of those signatures with default parameters as well (as the compiler would otherwise prefer conversion to a Boolean (i.e. Continue parameter), over conversion via STRING constructor with const char *):

**意思是**：`testtext` 这个位置**给一个字符串字面量**时，编译器**宁可把它转成 `Boolean Continue`**
（指针→布尔是标准转换），**也不走 `STRING` 的构造函数**——
**所以不写这一族显式重载，`testtext` 会被当成 `Continue` 用掉**。
**这是一条「为了不说错话而在 API 上打的补丁」，不是功能扩展。**

## 典型用法

**基本形状**（Example 1）：

```
SMC_TEST("dgtz_pin", "THD", thd_result);
```

**判据从哪来，有三条路**（**这一页给出的选择很明确**）：

| 写法 | 判据来自 | 出处 |
|---|---|---|
| `SMC_TEST(pin, testname, value)` | **含 `SMC_SYNCHRONIZE()` 的那个 test suite 的 properties view 里的 limits** | 参数表 `limit` 那一格 |
| `SMC_TEST(pin, testname, LIMIT(...), value)` | 显式 `[[limit]]` 对象 | Example 1 |
| `SMC_TEST(pin, testname, tmLimits, value)` | **测试表（`*.csv`）里用户定义的 limits 与 bins** | Example 3 |

**第三条路（测试表）的做法**：`tmLimits` 会让 `SMC_TEST()` **去看已加载的测试表文件**，
把结果值与 `"PowerOut0"` 的 limits 比、并据此分 bin。

**四个例子的分工**：

| 例子 | 讲什么 | 关键点 |
|---|---|---|
| **Example 1** | 一般用法 | 三条调用形态；`TM::CONTINUE` 让后续 `SMC_TEST()` 继续判；fail 时按指定的 softbin / hardbin 分 |
| **Example 2** | **hidden data logging**（**不用 `hidden_datalog_mode` testflow flag**） | 靠 `[[limit]]` 类实现；`SMC_ARM(lim)` 在 `[[for-each-site-begin]]` 循环里逐 site 武装；后台方法里 `SMC_TEST(site, "PinName", "TestName", lim, result)` |
| **Example 3** | **测试表（`*.csv`）** | `tmLimits` 写法；**并明确禁止**用 `tmLimits.getLimitObj(...)` 做后台处理 |
| **Example 4** | **大 site 数** | `SMC_ARM()` **只调一次**；结果数组用成员变量传给后台；**offline 模式的输出逐字给出** |

**Example 1 里那段「为什么第二个 `SMC_TEST()` 还会判」，语料写错了一个词**：

> The first SMC_TEST() call judges the thd_result data as pass or fail. Then the second SMC_TEST() judges the snr_result data as pass or fail because the TM::CONTINUE is set int the first SMC_TEST().

**`set int` 应为 `set in`**（详见「出处」⚠️②）。**语义本身是清楚的**：
**第一条是 pass 时，第二条自然继续**——**`Continue` 只在 FAIL 时才起作用**。

**几条顺序/前提**：

1. **先配 multibin**（在含 `SMC_SYNCHRONIZE()` 的 test suite 上）——**不配就是异常行为**。
2. **后台线程里只调 `SMC_TEST()` 或动态创建的 `TESTSET().judgeAndLog_...()`**——
   **不要碰系统预备的 `TestSet`，不要 `cout`**。
3. **判完不等于落盘**：**落盘在 `SMC_SYNCHRONIZE()`**（那一页）。
4. **site 多（96+）就换顺序路径**：`SMC_ARM()` 一次 + 按 site 号顺序调。
5. **要「不可靠」就显式给 `TM::UNRELIABLE`**——**`TM::RELIABLE` 与省略等价**。

**Example 4 的 offline 输出**（原文逐字给了这一段，可以拿来对数）：

> In offline mode, the example above results in the following output in the ui_report window if eight sites are configured, sites 3 and 7 are deactivated:

**它示范的是「deactivated site 不参与」**：结果数组里 site 3 / 7 是 `-1`，
`Active sites` 只列了 6 个，`SMC - Processing site …` 也只走了 6 次。
**判据是 `GET_ACTIVE_SITES()` 的结果，不是配置的 site 数。**

## 和谁有关

**同一族的那两层（**本页是 API 参考层，不是框架层**）**：

- [[smartcalc-framework]]（**本页读过它，但一句都不搬**）— **SmartCalc 的框架/导读层**：
  讲「为什么要有 SMC、它想省什么」。**它那篇自己没有 `SMC_TEST()` 的参数**，
  并且它把自己的 API 层指名到一个反引号里的名字 `SMC_... (SmartCalc API reference)`（`02.07.04.01.231`）。
  **分工：那一页讲「为什么」，本页讲「怎么调」。**
- [[smartcalc]]（**未建**，slug 在清单里）— **`SMC_...` 那一族的 API 参考侧**。
  本页是 `.231.45`，**是那一族里的一条**；**本篇没有点名它**，
  **这一条关系是按编号前缀指的，不是文档说的**。

**本页点名的 API 与页（全部是「文档事实」级的关系）**：

- [[testset]] — **两处点名**：① `SMC_TEST()` **合并了 `TESTSET.judgeAndLog_ParametricTest()` 的功能**；
  ② **系统预备的 `TestSet` 对象不是线程安全的**。
- [[limit]] — **判据可显式给一个 `LIMIT` 对象**；给 `TM::Pass` / `TM::Fail` 可**故意**让测试通过/失败。
  （原文在这里写了 `TM:Pass` / `TM:Fail`，**少一个冒号**，见「出处」⚠️①）。
- [[tmlimits]] — **`V93kLimits::TMLimits&` 一族重载**与 **Example 3 的测试表**。
  参数表里那一格写的是 `tmLimit`、签名里写的是 `limits`——**两个拼法都在语料里**（见「出处」⚠️⑤）。
- [[for-each-site-begin]] / [[for-each-site-end]] — **Example 2 / 4 里逐 site 武装 `SMC_ARM()` 的那个循环**。
- [[on-first-invocation-begin]] / [[on-first-invocation-end]] — **Example 2 / 4 里整条 setup 所在的作用域块**。
- [[test-method-class]] — **两段示例都是 `testmethod::TestMethod` 的子类**；
  `SMC_TEST()` 的**调用点在 `SMC_backgroundProcessing()`**，不在 `run()`。

**同族但在别处讲的两页（**本页没读，用 wikilink 指，不搬内容**）**：

- [[hidden-upload]]（**本页没读**）— SMC 家族里「把上传藏起来」的那一页。
  **本页出现的词是 `Hidden data logging` / `hidden_datalog_mode`，不是 `Hidden upload`**——
  **两者是不是同一件事，本页没有依据**，所以只指路、不断言。
- [[smc-background-process-locks-config]]（**本页没读**）— SMC 后台进程的**配置锁**约束页。
  **本页只由「后台线程里不能用非线程安全的对象」这一条与它相邻**；
  **那条约束的具体内容本页不搬。**

**这一页在 results 那段的位置**：

- [[mapping-results]]（**本页读过它**）— Results 段的五层对照表。
  **那张表 13 行 78 格里没有 `SMC_TEST()` 这一格**：它的「把结果落成人读的报告与机器读的 STDF」
  一行，L2 列写的是 `TESTSET` / `TESTSET::judgeAndLog_ScanTest` / `TEST` / `PUT_DATALOG`。
  **也就是说 results 的 L2 那一条路是「当场判、当场落」**，
  而 **`SMC_TEST()` 是另一条路：先排队、到同步点才落**。
  **那页自己也声明了「`02.07` 的 L2 页一篇没读」**——**本页就是它没读的那一族里的一个**。

**放进测试方法的那一段**：[[testmethod]]（本页 `stage: testmethod` 的理由）。

## 版本

**本文档有 `## Functional changes` 段，五条，全部照录**：

- **Introduced in SmarTest 6.5.3**
- **SmarTest 7.3.4: Patch 4 - New string parameter "testtest"**
- **SmarTest 7.4.5: Patch 1 - New syntax with parameter "testtest" defined as "const char *"**
- **SmarTest 7.5.3: New optional parameter logTestNumber for two variants of SMC_TEST, added softBin and hardBin parameters to one variant.**
- **SmarTest 7.5.3: Removed a redundant version of SMC_TEST.**

**怎么读这五条**：

- **第一条是正常的 `Introduced in`，不是 §11.2 ② 的哨兵**——`SMC_TEST()` 是 6.5.3 引进的。
- **第二、三两条里的 `"testtest"` 与签名里的参数名 `testtext` 对不上**（**两条里的拼法互相矛盾**：
  7.4.5 那条自己写的是 `testtext`）——**本页照录，不替语料选一个**（见「出处」⚠️④）。
  **两条合起来说的是**：`testtext` 先只有 `STRING` 版本，7.4.5 起有 `const char *` 的显式重载
  ——**这与「语法 / 参数」节里第三族签名的存在完全对得上**。
- **第四、五两条同为 7.5.3**：**加了 `logTestNumber`、给其中一个变体补了 softBin / hardBin，
  同时删掉了一个冗余重载**。**签名表里 `logTestNumber` 只出现在一条签名上**，
  与「for two variants」这句能对上（**这一步是本页的对读，属推断**）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.md`
（TDC `120084.htm`，332 行 / 21,816 字节）。**整篇读完**——**本篇长，是因为四个例子占了多半篇幅**，
而「语法 / 参数」节已经把签名与参数表逐字抄走了，**所以本页散文部分写的是机制与关系**。

**本页另外读过的两份 wiki 文件（不是 raw，读了只为指路，一句不搬）**：
`wiki/objects/smartcalc-framework.md`、`wiki/mappings/mapping-results.md`。

**本页没做的**：

- **`SMC_SYNCHRONIZE()`（`.231.43`）原文没读。** 这是本页**最要紧的一个缺口**：
  本页每讲一句「到同步点才落盘」，依据都只是 `SMC_TEST()` 这一篇里点名它的那两句；
  **同步点本身怎么工作（超时、计数、`forceErrorExitOnFail`）本页一个字没有**。
- **`SMC_ARM()`（`.231.01`）原文没读**，所以「武装一次 / 武装多次」的语义、参数与生命期本页没有；
  本页只说得出「它在大 site 数时开销会涨」。
- **`SET_MULTIBIN()`（`.212`）原文没读**，所以 multibin 怎么定义、号段怎么规划本页没有。
- **`TESTSET` / `TESTSET.judgeAndLog_ParametricTest()`（`.244` / `.244.10`）、`TEST()`（`.241`）、
  `GET_FUNCTIONAL_RESULT()`（`.88`）、`LIMIT`（`.126`）、`TMLimits`（`.250`）原文一篇没读**——
  **本页凡是提到它们的语义，都只在本篇自己写的那一两句范围内。**
- **两篇 bin 规则的 use case 没读**（`Use of bins with multisite tests`、`Use of multibins`，
  以及 `Use of SMC_TEST() with multibin` / `Use of TESTSET and SMC_TEST() test suites with multibin`）
  ——**「第一个 fail 决定 fail bin」的细节本页不展开**，因为原文把它推给了那几篇。
- **`Thread safety`（`02.07.10.02.02`）、`Hidden data logging`（`02.07.10.04.09`）、
  `Four-step SmartCalc implementation`（`02.07.10.04.03`）原文没读**——
  所以「到底什么算线程安全」「hidden data logging 的完整流程」本页没有。
- **一张图都没看——因为这一篇里没有图。** 实测：本篇全文 **0 处** `raw/`、
  **0 处** `.png` / `.jpg`。**所以本页没有任何来自图的结论**；
  **这不是「图够不着」，是这一篇里根本没有图**（§11.4）。
- **没有实跑。** 没有在任何机台上跑过 `SMC_TEST()`、没有建过 multibin、
  没有触发过一次 FAIL 路径。`verified: doc-only` 指的就是这件事。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 枚举值少一个冒号，2 处**：`If you specify TM:Pass within the LIMIT class, the test alway will pass, regardless of the actual test result.`
> 与 `If you specify TM:Fail within the LIMIT class, the test always will fail, regardless of the actual result.`
> —— **`TM:Pass` / `TM:Fail` 应为 `TM::Pass` / `TM::Fail`**；
> **而且第一句里的 `alway` 还少了一个 `s`**（第二句的 `always` 是对的）。
> **② 一处 `int` / `in` 之误**：`because the TM::CONTINUE is set int the first SMC_TEST()`。
> **③ 同一篇里两种错拼版本的 API 名**：`binning happens in SMC_SYCHRONIZE according to the binning rules as for SMC_TEST.`
> —— **`SMC_SYCHRONIZE` 少了 `H`**（正确拼法是 `SMC_SYNCHRONIZE`）。
> **本页正文照引这个错拼**，不替换。
> **④ `## Functional changes` 里的 `"testtest"` 出现 2 次**，
> 而签名与参数表里这个参数一律写作 `testtext`——**两个拼法都在语料里，本页不裁定**。
> **⑤ 参数名两个拼法**：参数表那一格写作 `tmLimit`，而签名里写作 `V93kLimits::TMLimits& limits`。
> **⑥ 参数表最后一格被压扁了**，逐字是：
> `| testtext  | Text be added to the data log stream for this SMC_TEST() call.  |    Return value There is no return value.`
> —— **`Text be added` 缺 `to`**（应为 `Text to be added`），
> **而且 `Return value There is no return value.` 被并进了同一张表、没有独立成节**。
> **本页照录。**
> **⑦ 本页未发现编码坏字，未发现 `DC/DC power units`。** 实测本篇 **0 处非 ASCII 字符**、
> **0 处** `DC/DC power units`。**但这是「本页量过的」，不是「语料干净」**（§13.1 第 ⑥′）。

`verified: doc-only`
