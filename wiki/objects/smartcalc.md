---
type: object
title: SmartCalc framework
layer: L2
stage: testmethod
tags: [testmethod, smartcalc, smc, api, multithreading, multisite, test-time]
related: [smartcalc-framework, testmethod, test-method-class]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.md
created: 2026-09-21
updated: 2026-09-21
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

**SmartCalc（缩写 SMC）是 L2 的一层「高层 API 命令」**，用途只有一个：
**把耗时的计算和测试数据上传挪到后台线程去，好把测试时间压下来。**

原文第一句就是它的定位：

> 「Today's system controller with multiple cores allow parallel execution of various tasks.
> The SmartCalc (SMC) framework allows you utilizing these resources to minimize the test time.」

**关键机制是「藏」**：

> 「The framwork provides the ability to move time consuming calculations and uploads of test data
> into separate background threads. These "hidden" threads run as far as possible in parallel
> to the foreground process of SmarTest.」

**`"hidden"` 这个词是理解本页的钥匙**：线程确实在跑，但**它不在前台那条 testflow 主线里**。
所以「结果怎么记、bin 怎么判」得由**后台线程自己回写**——本页「语法 / 参数」节里那几段代码
就是这么写的：bin 与 test number 的判定（`SMC_TEST(...)`）**出现在后台那个函数里，不在前台函数里**。

### 为什么需要它：原生线程不好用

原文对原生多线程的评语很直白：

> 「Unfortunately, the usage of threads is not very user friendly. It requires major changes
> in coding and test flow.」

于是 SmartCalc 的立足点就是**把这层麻烦用 API 盖掉**：

> 「The purpose of SmartCalc is to overcome these limitations by providing high-level API commands.」

**注意「high-level API commands」这个措辞**：它声明的是**调用面**（命令级别），
不是「多线程本身」。**多线程是它内部的事**——这正是它相对原生线程的价值所在。
（**推断**；依据是原文 `Multithreading is a form of parallel processing based on the architecture
of the system controller that controls the test system.` 那一段把线程当作背景知识介绍，
紧接着说 SmartCalc 是来克服其局限的。）

### 它到底给什么：原文那六条

原文的引导句是 `Through SmartCalc, the following can be achieved:`，底下**六条**：

| 能力（原文，逐字） | 中译 |
|---|---|
| `Ease of use, minimum impact on test code and program flow` | **易用；对测试代码和程序流的改动最小** |
| `Parallel (multithreaded) calculation for different sites` | **按 site 并行（多线程）计算** |
| `Automatic scaling with multi-site` | **随多 site 自动扩展** |
| `Hiding of calculation and data upload with delayed binning` | **把计算与数据上传藏起来，配合延迟分 bin** |
| `Minimum overhead and maximum multisite efficiency` | **开销最小、multi-site 效率最高** |
| `Automatic assignment of threads and CPU cores` | **线程与 CPU 核自动分配** |

**六条里最能说明「怎么调」的是第四条 `delayed binning`（延迟分 bin）**：
它意味着 **bin 的判定与写入可以推到后台线程里做**——这与本页语法节代码里
`SMC_ARM(...)` 之后 `SMC_TEST(...)` 出现在后台函数里，是同一件事的两处写法。

**六条里最不需要你操心的是最后一条**：**线程和 CPU 核是自动分配的**，
所以调用侧不该去管「哪个核跑哪个 site」——原文把它列为 SmartCalc 替你做的事。

### 调用形状：三段式

本页「语法 / 参数」节里那几段完整示例（**脚本逐字抽来的，段名里标了它取自哪个子主题**）
给出的是同一个骨架。把它抽出来是三段：

| 段 | 在前台做什么 | 出现在示例里的东西 |
|---|---|---|
| **① 照常 setup 并执行** | 测试照跑，**但执行那一步要换成 `SMC_` 包装的版本** | `SMC_EXECUTE_TEST(1.0)`、`SMC_DIGITAL_CAPTURE_TEST("1kBitArea")` |
| **② 逐 site 起线程** | `FOR_EACH_SITE_BEGIN()` 里取数，然后 **arm** | `CURRENT_SITE_NUMBER()`、`SMC_ARM()` / `SMC_ARM(lim)` / `SMC_ARM("1kBitArea", lim)` |
| **③ 等算完** | `ON_FIRST_INVOCATION_END()` **之后**调同步 | `SMC_SYNCHRONIZE()` |

**后台那一半写在一个固定的成员函数里**，名字就叫 **`SMC_backgroundProcessing()`**。
示例里它的典型内容是三步：
**`SMC_SITE_NUMBER()` 取本线程的 site** → 自己做计算（示例用的是 `DSP_SNR(...)`）→ **`SMC_TEST(...)` 判 bin / test number**。

**三条从示例里读得出来的硬点**（**是对本页语法节代码的观察，不是原文的规则陈述**）：

1. **`SMC_ARM` 有三种重载形状**：无参、只带 limit、带 (area, limit)。
   示例里对应「纯计算」「要判限值的计算」「隐藏数字上传之后要判限值的计算」三种场合。
2. **`SMC_SYNCHRONIZE()` 在 `run()` 里、`ON_FIRST_INVOCATION_END()` 之外**——
   示例把它单独放在 `ON_FIRST_INVOCATION_END()` 之后，并有注释说明是「等所有计算完成」。
   另外示例里还单起了一个 `class runDelayedBinLog`，它的 `run()` **只做 `SMC_SYNCHRONIZE()`**——
   **即「等」这一步可以和「起」分开在不同的 test method 里做。**
3. **后台函数里拿到的引用不要在函数外再用**——digital 那一例的注释写着
   `a reference to the captured data is copied here, as we do not access the data outside
   this function (or after SMC_SYNCHRONIZE())`。

> ⚠️ **本页只到「形状」这一层。**
> `SMC_ARM` / `SMC_SYNCHRONIZE` / `SMC_TEST` / `SMC_GET_VECTORS` 各自的
> **参数表、返回值、报错条件，本页没有依据**——
> 它们在 `SMC_... (SmartCalc API reference)`（`02.07.04.01.231`）里，**那篇本页没读**。
> 本页给的只是**从本页语法节那几段示例里直接看得见的调用顺序与名字**。

### 本页和 `smartcalc-framework` 的分界

两页**共用同一篇 raw**（`02.07.10_SmartCalc_framework.md`），所以边界必须说死：

| 页 | 答的问题 |
|---|---|
| **本页 [[smartcalc]]** | **怎么调**——API 侧的调用形状、起步顺序、能力清单 |
| [[smartcalc-framework]] | **为什么、是什么**——多线程背景、线程模型、实现与建议 |

**两页的「语法 / 参数」节逐字相同**（同一个脚本、同一篇 raw 抽出来的）。
**这不是重复建页，是同一对象的两面**——读者按「我要调它 / 我要懂它」分流。

## 典型用法

**本篇没有 `## Procedure` 段，也没有 `## Before you begin` 段**——原文没给编号步骤。
可用的依据只有两处：**上面那六条能力清单**，和**本页「语法 / 参数」节里那几段示例代码**。

所以「怎么起步」只能从示例代码的形状反推。**以下是示例代码呈现的顺序，不是原文写的步骤**：

1. **在 test method class 里照常 setup**（示例里是 `DGT("pinDGT").enable()` 这一类）。
2. **把「执行测试」那一步换成 `SMC_` 包装的版本**（示例：`SMC_EXECUTE_TEST(1.0)`；
   数字捕获的例子用 `SMC_DIGITAL_CAPTURE_TEST("1kBitArea")`）。
   —— **这是真正的第一步改动**：不换成 `SMC_` 版本，「藏」就无从谈起。
   （**推断**；依据是 digital 那一段示例自己的注释：
   `setup and execute your test as usual, but use the SMC_xxx API`。）
3. **在 `FOR_EACH_SITE_BEGIN()` / `FOR_EACH_SITE_END()` 之间逐 site 取数，然后 `SMC_ARM(...)`。**
4. **在 `ON_FIRST_INVOCATION_END()` 之后调 `SMC_SYNCHRONIZE()`，等所有计算完成。**
5. **把后台逻辑写进 `SMC_backgroundProcessing()`**：
   `SMC_SITE_NUMBER()` 取 site → 计算 → `SMC_TEST(...)` 判 bin 与 test number。

**第 5 步有一个坑，示例里专门注了一行**：bin 与 test number 必须是**流程里真实存在的**——

> `//Assign bin (note: selected HW and SW bin must exist in the flow) and testnumber`

**怎么选线程模型、后台怎么传数据**：本页语法节里那段收尾示例的说明句写了，
它对 **thread per site** 和 **common thread** 两种模型都成立，并指向
`SmartCalc recommendations`。**那两篇本页都没读，所以「选哪种、怎么传」本页答不了。**

**下一步该读哪一篇**（这是原文 `## Related information` 自己列的次序）：

| 想知道什么 | 去哪篇 |
|---|---|
| SmartCalc 的 API 全貌 | `SmartCalc API overview`（`02.07.10.04.02`） |
| 每一条 `SMC_...` 命令怎么调 | `SMC_... (SmartCalc API reference)`（`02.07.04.01.231`） |
| 测试方法侧的入口 | `SmartCalc test methods (smartCalc)`（`02.07.05.06`） |
| 为什么值得这么做（吞吐/多 site 效率） | `Multi-Site Efficiency and Throughput`（`03.14.10.03`） |

## 和谁有关

- [[smartcalc-framework]] — **同一篇 raw 的另一面**（见上表的分界）：它讲为什么/是什么，
  本页讲怎么调。**两页的「语法 / 参数」节逐字相同**，是脚本从同一篇抽的。
- [[testmethod]] — **stage 归属**。frontmatter 的 `stage: testmethod` 是**「最近的一段」**，
  不是「归属」——SMC 的调用写在 test method 里，读者要去那一段找它的用法。
- [[test-method-class]] — **SMC 的调用点**。本页语法节里两段完整示例
  **都是 `class ... : public testmethod::TestMethod`**：
  `SMC_ARM` 写在 `run()` 里，后台逻辑写在 `SMC_backgroundProcessing()` 里。
  **「怎么建这个类」是另一页的事。**
- **本页语法节实际引到的子主题**（**均未读**）：
  `SmartCalc implementation › Parallel site calculation`、
  `SmartCalc implementation › Hidden calculation`、
  `SmartCalc implementation › Hidden digital upload and calculation`、
  `SmartCalc implementation › Terminate SmartCalc threads after binning`、
  `SmartCalc multithreading basics`、`SmartCalc recommendations`。
  **本页「语法 / 参数」节里的代码就是从这里逐字抽来的——出处写在每个段名里。**
- **原文 `## Related information` 的四篇**（**均未读**，见上表）：
  `Multi-Site Efficiency and Throughput`、`SmartCalc API overview`、
  `SMC_... (SmartCalc API reference)`、`SmartCalc test methods (smartCalc)`。
  **其中 `SMC_...` 那一篇是「怎么调」的最终答案所在，本页只能指过去。**
- **原文 `## Subtopics` 另外两篇**（**均未读**）：
  `SmartCalc multithreading considerations`、`SmartCalc use models`。
- `SmartCalc "Thread per site" and "Common thread"`（`02.07.10.02.01`，**未读**）——
  两种线程模型的专页，只在语法节的说明句里被点到一次。

> 上面每一条都来自**本页读的那一篇 raw 自己的** `## Subtopics` / `## Related information` / 正文句子，
> 或来自**本页自己的「语法 / 参数」节**（脚本产出，出处标在段名里）。
> **本页没有查 `edges.jsonl`，也没有从别的文档补事实。**

## 版本

原文 `## Functional changes` 只有一条：

- **Introduced in SmarTest 6.5.3**

**即 SmartCalc 从 SmarTest 6.5.3 起就有**；本 wiki 面向的 **7.10.3 上在**。
**原文没有给任何后续版本的变更条目**——所以「6.5.3 之后改了什么」本篇答不了，
要去 [[smartcalc-framework]] 的「版本」节或版本页看有没有别的依据。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.md`

**本页没做的**：

- **`## Subtopics` 五篇一篇都没读**（`SmartCalc multithreading basics` /
  `SmartCalc multithreading considerations` / `SmartCalc use models` /
  `SmartCalc implementation` / `SmartCalc recommendations`）。
  ⚠️ **这里要写清一个容易看错的点**：本页「语法 / 参数」节里**确实有**从那几篇抽来的代码
  （段名里标了 `（取自子主题 <子主题名>）`），**但本页正文没有读过那几篇的散文**——
  **凡是本页讲「代码形状」的地方，依据都是页面上那几段代码本身，不是那几篇的正文。**
- **`## Related information` 四篇一篇没读**——所以
  **`SMC_ARM` / `SMC_SYNCHRONIZE` / `SMC_TEST` / `SMC_GET_VECTORS` / `SMC_CLEANUP` 的
  参数表、返回值、报错，本页一个字都没有**；
  「thread per site 与 common thread 怎么选」「后台怎么传数据」「延迟分 bin 的细节」也没有。
- **一张图没看**：raw 里嵌了一张 `../../../../raw/118785.png`（alt 文字
  `Basic concept of multithreading`）。**本页没有任何来自图的结论**——
  **本页不用「图够不着」当理由（§11.4）：是没看，不是看不到。**
- **原文那句自我说明没有展开**：`This chapter provides some background information to multithreading
  followed by a high level view of SmartCalc's API implementation into the test program.`
  —— **「本章」那两半各落在哪些子主题里，本页没核。**
- **本篇没有 `## Syntax` / `## Parameters` 段**——定义文档自己**没有**完整语法段，
  本页「语法 / 参数」节里带 `（取自子主题 <子主题名>）` 后缀的段落全部来自子主题。
  **这不是本页的缺陷，是语料的形状**（骨架里那一行 ⚠️ 就是说的这件事）。

> ⚠️ **本篇的语料瑕疵，照实记录，一处都没替它改**：
> ① **拼写**：原文写的是 `The framwork provides the ability to` —— **`framwork` 应为 `framework`**
>    （同一篇的标题、`## Subtopics` 那一行、以及正文别处都写 `framework`）。
> ② **主谓不一致**：原文写的是 `Today's system controller with multiple cores allow parallel
>    execution of various tasks.` —— **`allow` 应为 `allows`**（主语是单数 `controller`）。
>    同一句里 `allows you utilizing these resources` 也不通（应为 `allows you to utilize`）。
>    **本页引了这一句，原样保留。**
> ③ **`## Related information` 的四条链接之间没有任何分隔符**，在 raw 里是连着的一串：
>    `](<../../03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.10.03_Multi-Site_Efficiency_and_Throughput.md>)[SmartCalc API overview](<02.07.10.04.02_SmartCalc_API_overview.md>)[SMC_... `
>    —— **四条链接挤在同一行、彼此直接相接，中间不空行也不加标点。**
> ④ **标题层级与别篇不同**：本篇用的是 `#### Subtopics`（四级标题），
>    而本 wiki 抽样到的其他文档多用 `##`。
> ⑤ **`Multithreading is a form of parallel processing based on the architecture of the system
> controller that controls the test system.` 那一段里有一句用词很松**：
>    `Unfortunately, the usage of threads is not very user friendly.` ——
>    **`usage` 作主语配 `friendly` 是口语搭配**，正式写法一般是 `the use of threads is not very user-friendly`。
>    **原文如此，本页照抄。**

`verified: doc-only`
