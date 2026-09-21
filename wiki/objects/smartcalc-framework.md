---
type: object
title: SmartCalc framework
layer: L2
stage: testmethod
tags: [testmethod, smartcalc, smc, multithreading, l3, test-time, multisite, delayed-binning]
related: [smartcalc, hidden-upload, smc-background-process-locks-config, testmethod, test-method-class]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# SmartCalc framework

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,669 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.md>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.10.01_SmartCalc_multithreading_basics.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.04.04_Parallel_site_calculation.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.04.06_Hidden_calculation.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.04.07_Hidden_digital_upload_and_calculation.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.04.12_Terminate_SmartCalc_threads_after_binning.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.05_SmartCalc_recommendations.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 SmartCalc multithreading basics）

The following section shows a truncated output of the /proc/cpuinfo of a XW4400 system controller:

```
processor:          0
vendor_id:          GenuineIntel
cpu family:         6
model:              15
model name:         Intel(R) Core(TM)2 CPU  6700  @ 2.66GHz
stepping:           6
cpu MHz:            1596.000
cache size:         4096 KB
physical id:        0
siblings:           2
core id:            0
cpu cores:          2
....
processor:          1
vendor_id:          GenuineIntel
cpu family:         6
model:              15
model name:         Intel(R) Core(TM)2 CPU  6700  @ 2.66GHz
stepping:           6
cpu MHz:            1596.000
cache size:         4096 KB
physical id:        0
siblings:           2
core id:            1
cpu cores:          2
```

### Example（取自子主题 SmartCalc implementation › Parallel site calculation）

```
class runSNRtestMethod: public testmethod::TestMethod
{
     private:

    //
    // Definition of member variables,
    // can be accessed from all methods
    // inside the class
    //
    DOUBLE snr[MAX_SITES], sPow[MAX_SITES], nPow[MAX_SITES];
    ARRAY_D I_Capt[MAX_SITES];

    protected:

    virtual void run()
    {
        ON_FIRST_INVOCATION_BEGIN()

            //
            // Setup and execute your test as usual
            //
            DGT("pinDGT").enable();

            SMC_EXECUTE_TEST( 1.0 );

            //
            // Upload data per site and start calculation
            //
            FOR_EACH_SITE_BEGIN()

                //
                // Upload waveform
                //
                INT site = CURRENT_SITE_NUMBER();
                I_Capt[site] = DGT("pinDGT").getWaveform();

                //
               // Kick off calculation thread
               SMC_ARM();

            FOR_EACH_SITE_END()

        ON_FIRST_INVOCATION_END()

        //
        // Wait until all calculations are done
        //
        SMC_SYNCHRONIZE();

        INT site = CURRENT_SITE_NUMBER();

        //
        // Log all results
        //
        TEST("pinDGT","SNR", snr[site]);
        TEST("pinDGT","signalPow", sPow[site]);
        TEST("pinDGT","noisePow", nPow[site]);

    } // virtual void run()

    public:

    void SMC_backgroundProcessing(void)
    {
        //
        // Retrieve the thread specific site number from SmartCalc
        //
        INT site = SMC_SITE_NUMBER();

        //
        // Do your calculation
        //
        DSP_SNR(I_Capt[site],&snr[site],&sPow[site],&nPow[site], 1024, 1, 3, 0.0, 0);

    } // void SMC_backgroundProcessing(void)

} // class runSNRtestMethod: public testmethod::TestMethod
```

### Example（取自子主题 SmartCalc implementation › Hidden calculation）

```
class sunSNRtestMethod: public testmethod::TestMethod
{
    private:

    ARRAY_D I_Capt[MS_MAX_SITES];

    protected:

    virtual void initialize()
    {
        addLimit("test_limit");
    }

    virtual void run()
    {
        ON_FIRST_INVOCATION_BEGIN();

            //
            // Setup and execute test as usual
            //
            DGT("pinDGT").enable();
            ...
            SMC_EXECUTE_TEST(1.0);

            LIMIT lim = GET_LIMIT_OBJECT("test_limit");

            //
            // Upload data per site and start calculation
            //
            FOR_EACH_SITE_BEGIN();

                INT site = CURRENT_SITE_NUMBER();

                //
                // Upload waveform
                //
                I_Capt[site] = DGT("pinDGT").getWaveform();

                //
                // Kick off calculation thread
                //
                SMC_ARM(lim);

            FOR_EACH_SITE_END();

        ON_FIRST_INVOCATION_END();

    } // virtual void run()

    public:

    void SMC_backgroundProcessing(LIMIT lim)
    {
        int     hardBin;
        int     TestNumber;
        string  softBin;
        DOUBLE  snr;
        DOUBLE  sPow;
        DOUBLE  nPow;

        int     site = SMC_SITE_NUMBER();

        //
        // Do calculation
        //
        DSP_SNR(I_Capt[site],&snr,&sPow,&nPow, 1024, 1, 3, 0.0, 0);

        //
        // Do judgment using the syntax
        //
        // SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit,
        //           DOUBLE value, Boolean Continue = FALSE, INT testNumber = -1,
        //           const STRING& softbin= "", INT hardbin = -1);
        ...
        ...

        //
        //Assign bin (note: selected HW and SW bin must exist in the flow) and testnumber
        //
        hardBin = 5; softBin = "SNRTest"; TestNumber = 1000;

        SMC_TEST("pinDGT","SNR", lim, snr,TM::CONTINUE, TestNumber,softBin,hardBin);

        hardBin = 7; softBin = "SigPowTest"; TestNumber = 2000;

        SMC_TEST("pinDGT","signalPow", lim, sPow,TM::CONTINUE, TestNumber,softBin,hardBin);

        hardBin = 8; softBin = "NoisePowTest"; TestNumber = 3000;

        SMC_TEST("pinDGT","noisePow", lim, nPow,TM::CONTINUE, TestNumber,softBin,hardBin);

    } // void SMC_backgroundProcessing(LIMIT lim)

}; // class sunSNRtestMethod: public testmethod::TestMethod

class runDelayedBinLog: public testmethod::TestMethod
{
    protected:

    virtual void run()
    {
        //
        // Wait until all calculations are done
        //
        SMC_SYNCHRONIZE();
        ...
        ...
    }

}; // class runDelayedBinLog: public testmethod::TestMethod
```

For handling of data within the `SMC_backgroundProcessing()`（raw: `02.07.04.01.231.01_SMC_ARM.md#_120107__s_SMC_backgroundProcessing`） method, refer to `Passing data to the background process`（raw: `02.07.10.05_SmartCalc_recommendations.md#_119876__s_Passing_data_to_the_background_process`） in `SmartCalc recommendations`（raw: `02.07.10.05_SmartCalc_recommendations.md`）.

### Example（取自子主题 SmartCalc implementation › Hidden digital upload and calculation）

```
class runSNRtestMethod: public testmethod::TestMethod
{
     protected:
      virtual void initialize()
      {
         addLimit("test_limit");
      }
     virtual void run()
     {
          ON_FIRST_INVOCATION_BEGIN()
               // digital capture setup for hidden upload
               RESULT_AREA_CONFIG resConf("pin1"); //capture pin
               resConf.appendArea("1kBitArea", 3072).activate();

               // setup and execute your test as usual, but use the SMC_xxx API
               ...
               SMC_DIGITAL_CAPTURE_TEST("1kBitArea");
               LIMIT lim = GET_LIMIT_OBJECT("test_limit");

               FOR_EACH_SITE_BEGIN()
                    // kick off calculation thread
                    SMC_ARM("1kBitArea", lim);
               FOR_EACH_SITE_END();
          ON_FIRST_INVOCATION_END();
     }

     public:
     void SMC_backgroundProcessing(STRING area, LIMIT lim)
     {
          // trigger upload when SMC wrappers indicate non-blocking action
          // a reference to the captured data is copied here, as we
          // do not access the data outside this function
          // (or after SMC_SYNCHRONIZE())
          const ARRAY_I& data = SMC_GET_VECTORS("VectorVariable", area);

          // do your calculation
          DSP_SNR(data,&snr,&sPow,&nPow, 1024, 1, 3, 0.0, 0);

          // do judgment
          SMC_TEST("pinDGT","SNR", lim, snr,,"55");
          SMC_TEST("pinDGT","signalPow", lim, sPow,,"57");
          SMC_TEST("pinDGT","noisePow", lim, nPow,,"59");
     }
     (...)
}

class runDelayedBinLog: public testmethod::TestMethod
{
     protected:
     virtual void run()
     {
          // wait until all calculations are done
          SMC_SYNCHRONIZE();
          (...)
     }
}
```

### Example（取自子主题 SmartCalc implementation › Terminate SmartCalc threads after binning）

The following example code was created by following the description of `Using the special test suite bin_disconnect`（raw: `../../03_Use_cases_and_application_papers/03.04_How_to_do_disconnect/03.04.01.04_Special_test_suite_bin_disconnect.md`） and has been adapted for SmartCalc. It is valid for both thread per site and common thread (see `SmartCalc "Thread per site" and "Common thread"`（raw: `02.07.10.02.01_SmartCalc__Thread_per_site__and__Common_thread.md`）).

```
virtual void run()
{
 ...// example of a customized disconnect
    ARRAY_I enabledSites;
    INT numEnabledSites;
    INT hwBinNumber, goodBin, reprobe, overon, otherwiseBin;
    STRING hwBinDescription, swBinDesciption, swBinNumber;

    const string nonshareddisconnect="ACMD \"CNCT\",\"OFF\",(@NONSHARED@); \
    FLSH MUX;WSDN;DLSO(@NONSHARED@); \
    CNCT OFF,(@NONSHARED@);CHRS OFF; \
    BCMD \"\",ACTION,\"Update\",; \
    PSST OFF;RLYC IDLE,OFF,(@NONSHARED@);";
    const string finaldisconnect ="ACMD \"CNCT\",\"OFF\",(@);FLSH MUX;WSDN; \
    SQST OFF;CNCT OFF,(@);CHRS OFF; \
    BCMD \"\",ACTION,\"Update\",; \
    PSST OFF;RLYC IDLE,OFF,(@);";

    numEnabledSites = GET_ENABLED_SITES(enabledSites);

    SMC_CLEANUP(false); // kills running thread only

    if (numEnabledSites == 0)
    {
        FW_TASK(finaldisconnect); //last enabled site to be disconnected
    }
    else
    {
        //not the last site to be disconnected
        //only disconnect current site and keep shared resources connected
        FW_TASK(nonshareddisconnect);
    }

    return;
}
```

This example works regardless of the used pin `Mode contexts`（raw: `../02.06_Command_Reference/02.06.03.01.03.01_Mode_contexts.md`）.

### Example（取自子主题 SmartCalc recommendations）

### Exception handling

The following example shows how a customized exception handling can be coded in the `SMC_backgroundProcessing()`（raw: `02.07.04.01.231.01_SMC_ARM.md#_120107__s_SMC_backgroundProcessing`） method using catch().

```
void SMC_backgroundProcessing()
{
    ...
    try
    {
        ...
        call my_function_that_throws();
        ...
    }
    catch(myException& e)
    {
        //
        // Always catch user-defined exceptions
        // and do what is needed in this specific error.
        ...
    }
    ...
}

class myException {};

void my_function_that_throws()
{
    if (...)
    {
        throw myException();
    }
}
```

<!-- 语法节 end -->

## 是什么

**SmartCalc（缩写 `SMC`）是把「耗时的计算」和「测试数据上传」搬到后台线程去做的框架。**
它的目的只有一个：**在不改乱测试程序的前提下，把系统控制器的多核吃满，换测试时间。**

原文的立论段（**这是全页第一句实质内容**）：

> 「Today's system controller with multiple cores allow parallel execution of various tasks.
> The SmartCalc (SMC) framework allows you utilizing these resources to minimize the test time.
> The framwork provides the ability to move time consuming calculations and uploads of test data into
> separate background threads. These "hidden" threads run as far as possible in parallel to the
> foreground process of SmarTest.」

**三个词要划出来：**

| 词 | 含义 |
|---|---|
| **`SMC`** | SmartCalc 的缩写——**代码里的 API 前缀就是它**（`SMC_...`），**本页「语法 / 参数」节里的示例通篇是它** |
| **`hidden threads`** | **「隐藏」指的是「不占前台」**，不是「对用户不可见」 |
| **`as far as possible in parallel`** | **原文自己加了 `as far as possible`** ——**并行不是保证，是尽力** |

### 它要解决什么问题：**线程本身好用，但难写**

原文在讲框架之前**先讲了它的动机**，这段是本页最该读的一段：

> 「Multithreading is a form of parallel processing based on the architecture of the system controller
> that controls the test system. Independent threads can be executed in parallel on different CPU cores.
> This reduces test time and improves multisite efficiency. **Unfortunately, the usage of threads is
> not very user friendly. It requires major changes in coding and test flow.**」

> 「The purpose of SmartCalc is to overcome these limitations by providing high-level API commands.」

**所以 SmartCalc 的定位是一层「高层 API 包装」**——
**它不是新的并行机制，是把「手写线程」这套东西包起来，让你少改代码。**

### 六个卖点（原文逐字，`- ` 是原文的列表符）

> 「Through SmartCalc, the following can be achieved:
>
> - Ease of use, minimum impact on test code and program flow
> - Parallel (multithreaded) calculation for different sites
> - Automatic scaling with multi-site
> - Hiding of calculation and data upload with delayed binning
> - Minimum overhead and maximum multisite efficiency
> - Automatic assignment of threads and CPU cores」

**六条按「谁受益」分一下，读起来更清楚：**

| 卖点 | 谁受益 | 对应原文行 |
|---|---|---|
| **少改代码** | 写测试的人 | bullet 1（`Ease of use, minimum impact on test code and program flow`） |
| **每 site 并算** | 多 site 程序 | bullet 2（`Parallel (multithreaded) calculation for different sites`） |
| **随 site 数自动伸缩** | 多 site 程序 | bullet 3（`Automatic scaling with multi-site`） |
| **把计算和上传藏起来** | 测试时间 | bullet 4（`Hiding of calculation and data upload with delayed binning`） |
| **开销小、效率高** | 测试时间 | bullet 5（`Minimum overhead and maximum multisite efficiency`） |
| **线程与核的分配不用你管** | 写测试的人 | bullet 6（`Automatic assignment of threads and CPU cores`） |

> **bullet 4 里 `with delayed binning` 是关键词**：
> **「藏起来」靠的是「延迟分 bin」**——**把 upload 和计算推到 binning 之前的那一刻**。
> **具体机制本篇没展开**（**它的子主题里才有**，见 `## 出处`）。
> 本页有一篇同批的页 [[hidden-upload]] 讲这件事的另一面——**但本篇这一篇没有点名它**
> （**原文的措辞是 `Hiding of calculation and data upload`，不是 `hidden upload`**），
> **所以两者的关系本页只按主题指，不断言。**

### 它是一篇「章首导读」，不是命令手册

原文自己说了这一篇的性质：

> 「This chapter provides some background information to multithreading followed by a high level view of
> SmartCalc's API implementation into the test program.」

**这解释了两件事，都影响你怎么读这一页：**

| 现象 | 原因 |
|---|---|
| **`## Syntax` / `## Parameters` 一个都没有** | **这是一章的开头，不是一条命令的参考页**——**脚本因此一个字都没抽**（见「语法 / 参数」节顶上那段说明） |
| **`## 是什么` 讲的全是「为什么」** | **本篇就是写「为什么」的那一篇**；**「怎么做」在它的五个子主题里** |

### 本篇里唯一的一张图

原文正文插了一张图，`alt` 文本是 `Basic concept of multithreading`
（raw 链接 `../../../../raw/118785.png`）：**多线程的基本概念示意图**。
**本页没有看这张图**（**`sources:` 只有这一篇 md，图在 `raw/118785.png`，本页没有打开它**）——
**所以这张图画了什么、有几个线程、前台后台怎么摆，本页一个字都没有。**

## 典型用法

**本页**没有**可写的用法。这是本页最需要说清的一件事。**

- **本篇没有 `## Procedure`、没有 `## Before you begin`、没有 `## Example`** ——
  **它的五个子主题才是用法所在**（`SmartCalc multithreading basics` /
  `SmartCalc multithreading considerations` / `SmartCalc use models` /
  `SmartCalc implementation` / `SmartCalc recommendations`）。
- **这五篇本页一篇都没读**（**它们不在本页的 `sources:` 里**）。

**所以下面这三件事，本页一个字都不能给你：**

| 你想知道 | 在哪 |
|---|---|
| **`SMC_ARM()` 怎么调、参数是什么** | `SMC_... (SmartCalc API reference)`（**本页没读**） |
| **「thread per site」和「common thread」怎么选** | `SmartCalc "Thread per site" and "Common thread"`（**本页没读**） |
| **一个完整的 test method 怎么写** | `SmartCalc implementation` 一节（**本页没读**） |

**但有一件事必须在这里说明，否则读这一页的人会误判：**

> **本页的「语法 / 参数」节里是有代码的——六段 C++ 示例**，
> **而且它们是脚本从**子主题**抽来的**（脚本自己在段名里标了 `（取自子主题 …）`）。
> **它们不在本页的 `sources:` 里**，**所以本页正文一句都不拿它们当依据**。
> **代价是清楚的：这一页看上去有六段能跑的代码，而写它们的那些文档本页没读。**

**所以本页「典型用法」这一节的结论只有一句：**
**要动手，去读那五个子主题；本页只负责告诉你 SmartCalc 是什么、为什么存在。**

## 和谁有关

**同一族的页（本 wiki 里已建 / 将建的）：**

- [[smartcalc]] — **SmartCalc 的 API 参考那一侧**（**slug 在 allowlist 里；
  本页这一篇没有点名它**，它点名的是 `SMC_... (SmartCalc API reference)` ——**一个反引号里的名字**）。
  **分工：本页讲「为什么、是什么」，那一页讲「怎么调」。**
- [[hidden-upload]] — **bullet 4 那个「把上传藏起来」的专页**。
  **本页这一篇没有点名它**——**原文的措辞是 `Hiding of calculation and data upload with delayed binning`**。
  **两者的关系本页按主题指（都讲「藏上传」），不断言那一页讲的就是这一条 bullet。**
- [[smc-background-process-locks-config]] — **SMC 后台进程的配置锁约束页**。
  **本页这一篇一个字都没提「锁」或「配置」**——
  **这条关系是照 `SMC` 这个前缀指的**，**本页不声称它出自本篇。**

**用在 test method 里的那一侧（`stage: testmethod` 的理由）：**

- [[testmethod]] — **本页 `stage: testmethod` 的理由**：**SmartCalc 是写测试方法时用的东西**，
  **不是流水线上独立的一段**（§6：`stage` 填「最近的一段」）。
  **本页这一篇没有点名它**——**理由是本篇把 SmartCalc 说成 `high-level API commands`
  且要 `implementation into the test program`**（**推断，依据就是这两处措辞**）。
- [[test-method-class]] / [[test-method-project]] — **测试方法那一侧的对象页**。
  **本页这一篇一个字都没提它们。**

**本页 `layer: L3` 与同层页的关系（**这一条带一个待复核的问题，见 `## 出处`**）：**

- [[test-suite-control-api]] / [[tpi-program-routines]] — **§2.1 定义的 L3 三样里的两样**。
  **本页这一篇一个字都没提它们**——**列在这里只是因为 frontmatter 把本页标成了 `layer: L3`**。
  **而这个标法本身可疑，见 `## 出处` 末尾那一笔。**

**本页正文点名、但没有页、故不链的去处（反引号 + raw 路径）：**

- `SmartCalc multithreading basics`（`02.07.10.01`）、
  `SmartCalc multithreading considerations`（`02.07.10.02`）、
  `SmartCalc use models`（`02.07.10.03`）、
  `SmartCalc implementation`（`02.07.10.04`）、
  `SmartCalc recommendations`（`02.07.10.05`）——
  **本篇的五个子主题，也就是「怎么做」的全部内容。**
  **本页一篇都没读。**（**其中三篇被脚本抽进了本页的「语法 / 参数」节**——
  **抽进来的是代码，不是正文说明。**）
- `Multi-Site Efficiency and Throughput`
  （raw: `../../03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.10.03_Multi-Site_Efficiency_and_Throughput.md`）——
  `## Related information` 的第一条。
- `SmartCalc API overview`（`02.07.10.04.02`）——`## Related information` 的第二条。
- `SMC_... (SmartCalc API reference)`（`02.07.04.01.231`）——`## Related information` 的第三条。
  **「怎么调」的正主。**
- `SmartCalc test methods (smartCalc)`（`02.07.05.06`）——`## Related information` 的第四条。
  **注意这一篇的名字里带 `<smartCalc>`（小写 s）**——**语料自己的写法，本页照抄。**

## 版本

**本文档有 `## Functional changes` 段**，**只有一条**：

- **Introduced in SmarTest 6.5.3** — **SmartCalc 框架是 6.5.3 引进的**。
  **这是一条正常的版本条目，不是 §11.2 ② 那种哨兵**（**它写的是 `Introduced in`，
  不是 `Introduced before`**）。

**除这一条之外，本篇没有别的版本条目**——**没有记录 SmartCalc 在 6.5.3 之后被改过。**
**「没记录」不等于「没改过」**（§13.1 第 ⑥′）：**本页只报「本节只有一行」这个事实。**
**子主题里有没有各自的版本条目，本页没读，不知道。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.md`
（TDC `118783.htm`，41 行）

**本页没做的**：

- **五个子主题一篇都没读**（`02.07.10.01` / `.02` / `.03` / `02.07.10.04` / `.05`）。
  **这是本页最大的缺口**，而且缺口是**结构性的**：
  **本篇自己就是「导读」，把「怎么做」全推给了那五篇。**
  **所以本页能给的最有价值的东西，就是这份「哪件事在哪一篇」的清单**——
  **它在本页的 `## 和谁有关` 与 `## 典型用法` 里。**
- **一张图没看**（`raw/118785.png`，`alt` 是 `Basic concept of multithreading`）。
  **本页没有任何来自图的结论**——**连「有几个线程」都不知道。**
- **`## Related information` 里的四篇一篇都没读**（`Multi-Site Efficiency and Throughput`、
  `SmartCalc API overview`、`SMC_... (SmartCalc API reference)`、`SmartCalc test methods (smartCalc)`）。
- **`SMC_` 系列 API 的签名、参数、返回值，本页一个字都没有。**
  **本页「语法 / 参数」节里的六段示例里有 `SMC_ARM` / `SMC_SYNCHRONIZE` / `SMC_TEST` /
  `SMC_CLEANUP` / `SMC_EXECUTE_TEST` / `SMC_SITE_NUMBER` / `SMC_backgroundProcessing()` 这些名字**
  ——**它们来自子主题（脚本在段名里标了出处），不是本页读到的**，
  **所以本页正文不解释它们任何一个。**
- **`## Syntax` / `## Parameters` 在本篇里不存在**，**这不是脚本漏抽**：
  本篇是章首，**没有段标记**。**本页「语法 / 参数」节顶上的说明已经把这件事写清了。**
- **没有在任何真实机台上跑过 SmartCalc**（`verified: doc-only`）。
  **「并行能省多少时间」这件事本页一个字都不能保证**——
  **原文自己也只有一句 `This reduces test time and improves multisite efficiency.`，没有数。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 拼写错误：`framwork`。** 原文第 16 行逐字是
> `The framwork provides the ability to move time consuming calculations and uploads of test data into separate background threads.`
> —— **`framwork` 应为 `framework`**。
> **同一个词在第 16 行前面刚拼对过一次**（`The SmartCalc (SMC) framework allows you utilizing these resources`），
> **只有这一处错。本页正文引用这一句时按原样引，并在此注出正字。**
> **② `## Related information` 一节把四条链接挤成了一行。** 原文第 37 行逐字是
> `[Multi-Site Efficiency and Throughput](<...>)[SmartCalc API overview](<...>)[SMC_... (SmartCalc API reference)](<...>)[SmartCalc test methods (smartCalc)](<...>)`
> —— **四条链接之间**没有任何分隔符**（没有换行、没有空格、没有列表符、没有标点）**。
> **渲染出来会是四个连在一起的链接**。**本页照实记，不替它分行**
> （**本页在 `## 和谁有关` 里把它们拆成四条列出来，那是本页的整理，不是原文的形状**）。
> **③ 第 16 行有两处语法失手，都在同一段里**：
> `Today's system controller with multiple cores **allow** parallel execution of various tasks.`
> （主语是单数 `system controller`，**`allow` 应为 `allows`**）；
> `The SmartCalc (SMC) framework **allows you utilizing** these resources`
> （**应为 `allows you to utilize`**）。**本页照实引，一处都没替它改。**
> **④ 那张图的相对路径上溯了四级**（`../../../../raw/118785.png`）——
> **而本篇在 `02.07_Test_Method_Reference/` 下，四级上溯会跑到语料树外面**。
> **本页没去验证这个路径能不能解析**（**没读图**），**只把原文的写法记在这里。**
> **⑤ 本页在本篇里没有发现坏字（`鈥` / `渭` / `掳` 那一类）。**
> **但这是「本页读到的」，不是「本篇干净」**（§13.1 第 ⑥′）。

> **⚠️ 另有一处**待复核**（不是语料瑕疵，是骨架的标注）**：
> 本页 frontmatter 写着 **`layer: L3`**（**骨架生成，按规格本页原样保留、不许改**）。
> **但从本页能看到的证据看，这个标法值得复核**：§2.1 把 L3 定义为**外部控制**
> （Test suite control API / TPI / HVM），而**本页「语法 / 参数」节所引子主题示例的形状是
> 「写在 `testmethod::TestMethod` 的子类里」**——**那按 §2.1 更像 L2（Test Method API）。**
> **这是推断**（**依据只是本页语法节里那几段代码的形状，本页没读任何一篇 `SMC_` 的 API 文档**），
> **本页不改 frontmatter，只把这一笔留在这里供复核。**

`verified: doc-only`
