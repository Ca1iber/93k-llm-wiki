---
type: object
title: DC_RESULT_ACCESSOR
layer: L3
stage: testmethod
tags: [testmethod, dc-measurement, result-upload, api, dps, pmu, ganging]
related: [digital-pins-editor, dps-pins-editor, dc-test-programming, testmethod, results, limit, ganging]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.28_DC_RESULT_ACCESSOR.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# DC_RESULT_ACCESSOR

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,753 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.28_DC_RESULT_ACCESSOR.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Note

The examples provide various approaches for the use of the upload function uploadResult(). In the last example below, the uploadResult() is called inside the ON_FIRST_BLOCK. This reduces the test time considerably and, therefore, is the recommended approach.

### Example 1

```
virtual void run()
{
    ON_FIRST_INVOCATION_BEGIN();

    // a) Measurement setup
    // ...

    // b) Measurement execution
    // ...

    ON_FIRST_INVOCATION_END();

    // c) upload the results ...
    // ...
    STRING pin("dps1");

    // Declare a DC_RESULT_ACCESSOR object to access the results
    DC_RESULT_ACCESSOR results;

    // Which results are available?
    //
    // NOTE:
    // The returned result range contains the information about
    // available number of results for the pin. If more than
    // one pin is used for example, a group) the smallest common result
    // range for both pins is returned.

    TM::RESULT_RANGE resultRange =
        results.getRangeOfAvailableResults(pin, TM::RESULT_INDEX);

    if (resultRange.length > 0)
    {
        // Now upload the available results
        //
        // NOTE:
        // results.uploadResult(pin, TM::RESULT_INDEX);
        // would have the same effect, but calls
        // getRangeOfAvailablResults() internally again.
        // As this reduces performance, avoid this form of
        // uploadResult() if you already have determined
        // the range of available results.
        // Instead specify the range explicitly.

        results.uploadResult(pin, resultRange);

        // d) process the results ...

        // loop over the results ...
        // Note that both first and last represent valid RESULT_POINTS.
        // You must use "less or equal" (<=) in the comparison to include also the last
        // RESULT_POINT. Using a "<" or "!=" operator in the comparison would drop the
        // last result.

        RESULT_POINT currentPoint = results.getFirstResultPoint(pin);
        RESULT_POINT lastPoint    = results.getLastResultPoint(pin);

        while (currentPoint <= lastPoint)
        {
            // check for pass/fail at the current RESULT_POINT
            // As this example uploaded only fails, this condition
            // will always be true.

            if (! results.getPassFail(currentPoint))
            {
                // test at RESULT_POINT failed ...
                // obtain more information on the failed result ...
                // get the measurement value
                DOUBLE val = results.getValue(currentPoint);

                // obtain fail status information
                RESULT_FAIL_INFO status = results.getFailInfo(currentPoint);
                if (status.hasHighLimitFailed())
                {
                    // measure value is higher than the high limit
                    // ...

                }
                else if (status.hasLowLimitFailed())
                {
                    // ...

                }
                else if (status.hasMeasurementRangeViolation())
                {
                    // ...

                } // etc..

                // go to next result
                ++currentPoint;
            } // if
        } // while
    }

    // pass/fail judgment and datalog
    TEST(results);
}
```

### Example 2

Same as Example 1 above, except in block "c) upload the results":

```
virtual void run()
{
    STRING pin("dps1");
    DC_RESULT_ACCESSOR results;

    // This example uses the version of uploadResult() that returns the
    // result range. Hence it is not necessary to call
    // result.getRangeOfAvailablResults().
    // This simplifies the code example above to:

    TM::RESULT_RANGE resultRange = results.uploadResult(pin, TM::RESULT_INDEX);
    if (resultRange.length > 0)
    {
        // similar as in Example 1

    }
}
```

### Example 3

In this example, the upload function uploadResult() is used and hence all available results will be uploaded. The functions getFirstResultPoint() and getLastResultPoint() are used to obtain valid RESULT_POINTs, which are then used in a "for" loop to iterate over all uploaded results. In the "for" loop different extractor functions are used on the actual result in order to obtain pass/fail information, measured value, and status byte information.

```
virtual void run()
{
    // ...
    // Perform DC Dynamic measurement ....
    ON_FIRST_INVOCATION_BEGIN();

        // settings and relay switching ...
        FUNCTIONAL_TEST();

    ON_FIRST_INVOCATION_END();

    // ...

    STRING pin("dps1");

    // upload the results
    //
    // Define a result accessor object
    DC_RESULT_ACCESSOR allResults;

    // Upload all available results for the pin in RESULT_INDEX addressing scheme.
    // The variable "range" will contain the start index and the length of the uploaded
    // result range. For uploadResult() the length is equal to the number of uploaded
    // results but for uploadFailedResults() it is usually larger than the number of
    // failed results.
    // Before the result data can be accessed, they always first need to be uploaded from
    // hardware/firmware. Each uploadResult() will overwrite the last uploaded results.
    // (independent of the particular DC_RESULT_ACCESSOR object!).

    const TM::RESULT_RANGE range(allResults.uploadResult(pin, TM::RESULT_INDEX));
    if (range.length > 0)
    {
        // Use result accessor member functions getFirstResultPoint() and
        // getLastResultPoint() to obtain iterators (RESULT_POINT objects) to the
        // first and last uploaded results.

        const RESULT_POINT first(allResults.getFirstResultPoint(pin));
        const RESULT_POINT end  (allResults.getLastResultPoint(pin));

        // process the results

        // Loop over the uploaded results using the first and end iterators (RESULT_POINTs)
        // and the increment ("++") operator on an iterator (decrement is not supported).
        for ( RESULT_POINT p = first; p <= end; ++p )
        {
            const bool testPassed         = allResults.getPassFail(p);
            const TM::PHYSICAL_VALUE type = allResults.getMeasurementType(p);

            std::cout << "Test " << (testPassed ? " PASSED " : " FAILED ");
            std::cout << ", Measured value " << allResults.getValue(p);
            std::cout << ((type == TM::VOLTAGE) ? " V " : " A ");
            std::cout << " at point " << p.getIndex();
            std::cout << " at site "  << CURRENT_SITE_NUMBER() << endl;

            if (! testPassed)
            {
                // test has failed at this point
                // obtain the status info to examine the fail reason...
                const RESULT_FAIL_INFO failInfo = allResults.getFailInfo(p);

                // print out the status bits ...
                std::cout << " HighLimitFailed : " << failInfo.hasHighLimitFailed();

                // ...
            }
        }
    }

    // set the test result and send data to datalog ...
    TEST(allResults, TRUE);
}

```

### Example 4

This example shows how to use the uploadResult() function in a FOR_EACH_SITE_... block to upload the result of multiple sites. It utilizes the `DC_RESULT_ACCESSOR` constructor with string parameter, in order for `RESULT_AREA_CONFIG_SET` to reference it.

```
virtual void run()
{
    DC_RESULT_ACCESSOR result("dpsCurr");

    ON_FIRST_INVOCATION_BEGIN();

        RESULT_AREA_CONFIG_SET resSet("dpsCurr");
        resSet.pin("dps1").setDcValueResultAreaSize(8192);
        resSet.setAsPrimary();
        FUNCTIONAL_TEST();
        resSet.deselectGlobally();

        FOR_EACH_SITE_BEGIN();

            cout << "***Getting results for site: " << CURRENT_SITE_NUMBER() << endl;
            TM::RESULT_RANGE resultRange = result.uploadResult("dps1",TM::RESULT_INDEX);

            const RESULT_POINT first( result.getFirstResultPoint("dps1") );
            const RESULT_POINT end  ( result.getLastResultPoint("dps1") );
            DOUBLE mea;
            for (RESULT_POINT p = first; p <= end; p++)
            {
                mea = result.getValue("dps1", p);
                cout << "*** Result on site "
                     << CURRENT_SITE_NUMBER()
                     << ": " << mea << endl;
                cout << "*** P/F: " << result.getPassFail("dps1", p) << endl;
            }

            cout << "### P/F: " << result.getPassFail("dps1") << endl;

            cout << "All results array: " << result.getValues("dps1") << endl << endl;

        FOR_EACH_SITE_END();

    ON_FIRST_INVOCATION_END();

    return;
}
```

### Example 5

In this example the uploadResult() function is called inside the ON_FIRST_INVOCATION... block. This reduces the test time considerably and, therefore, is the recommended approach.

```
virtual void run()
{
    DC_RESULT_ACCESSOR result("dpsCurr");

    ON_FIRST_INVOCATION_BEGIN();

        FUNCTIONAL_TEST();

        TM::RESULT_RANGE range;
        range.first = 0;
        range.length = 200;
        result.uploadResult("dps1", TM::RESULT_INDEX, range);

    ON_FIRST_INVOCATION_END();

    const RESULT_POINT first( result.getFirstResultPoint("dps1") );
    const RESULT_POINT end  ( result.getLastResultPoint("dps1") );
    DOUBLE measuredValue;
    INT resPointNr = 1;

    cout << "Results for site " << CURRENT_SITE_NUMBER() << endl;

    for (RESULT_POINT p = first; p <= end; p++, resPointNr++)
    {
        measuredValue = result.getValue("dps1", p);
        cout << "*** Result point: " << resPointNr << endl;
        cout << "*** Measured value on dps1: "
             << measuredValue << endl;
        cout << "*** P/F: " << result.getPassFail("dps1", p) << endl;
    }

    cout << "P/F: " << result.getPassFail("dps1") << endl;
    cout << "All results: " << result.getValues("dps1") << endl << endl;

    return;
}
```

<!-- 语法节 end -->

## 是什么

**`DC_RESULT_ACCESSOR` 是「把测量结果取回来」的那一层 API。** 原文第一句：

> 「The DC_RESULT_ACCESSOR API allows the consistent handling of measurement results for
> different pin types and measurement types.」

**「不同的 pin 类型」与「不同的测量类型」是这句话的两个关键词**——
它存在的理由就是**用同一套取结果的写法**去对付 DPS / PMU 两种 pin、
电压 / 电流两种测量（原文 `So far the types TM::VOLTAGE and TM::CURRENT may be returned.`）。

**支持范围**（原文，两句拼起来）：

> 「The API supports both `DPS operating mode pins` (defined with the `DPS Pins editor`) and
> `PMU operating mode pins `(defined with the `Digital Pins editor`) and allows you to obtain the
> results from measurement set up through the `DPS_TASK` and `SPMU_TASK` APIs.」

> 「The API supports DC Scale DPS128 and XPS256 in DPS and PMU operating mode (for details see
> below). DC Scale UHC4T pins are supported in DPS operating mode. It does not support legacy DPS
> pins (which are also defined with the DPS Pins editor) and digital channel pins.」

| 卡 | DPS operating mode | PMU operating mode |
|---|---|---|
| DC Scale DPS128 | 支持 | 支持 |
| DC Scale XPS256 | 支持 | 支持 |
| DC Scale UHC4T | 支持 | **不支持** |
| legacy DPS pins | **不支持** | **不支持** |
| digital channel pins | **不支持** | **不支持** |

**注意最后一行 `legacy DPS pins` 的坑**：它**也是用 `DPS Pins editor` 定义的**，
但**这个 API 明确不支持它**——原文特意在括号里补了 `which are also defined with the DPS Pins editor`，
**就是防止你按「编辑器是同一个」推断它能用**（推断：这是本页对那句括号用意的解读）。

**结果从哪来**——原文列了三类来源：

| 来源 | 原文 |
|---|---|
| `DPS_TASK` / `SPMU_TASK` | `allows you to obtain the results from measurement set up through the DPS_TASK and SPMU_TASK APIs` |
| DC Dynamic 测量 | `The DC Dynamic measurement is mainly set up by DC event APIs.` |
| PPMU / BADC | `The API also supports measurements defined with the PPMU_... and BADC_... APIs.` |

**类结构**（原文 `## Class definition`）：

> 「The API consists of the central DC_RESULT_ACCESSOR class and following helper classes:
>
> - `RESULT_POINT`
> - `RESULT_POINT_LIST`
> - `RESULT_FAIL_INFO`」

**头文件路径**（原文逐字）：`/opt/hp93000/soc/prod_com/include/MAPI/DcResultAccessor.h`。

**两个构造器**，区别只在「要不要一份 result configuration set 的名字」：

| 构造器 | 原文说明 |
|---|---|
| `DC_RESULT_ACCESSOR()` | 无参 |
| `DC_RESULT_ACCESSOR(const STRING& dcResultConfigurationSetName)` | `Defines the result configuration set to be set before data uploading.` |

**带字符串的那个构造器是给 `RESULT_AREA_CONFIG_SET` 用的**——
原文只在 Example 4 里交代了这件事：
`It utilizes the DC_RESULT_ACCESSOR constructor with string parameter, in order for RESULT_AREA_CONFIG_SET to reference it.`
**「result configuration set」本身是哪个命令 / 哪个对象，本篇没有单独讲**。

**成员函数 12 个**（原文 `Member Functions` 列表，逐字）：
`uploadResult()`、`uploadFailedResult()`、`getRangeOfAvailableResults()`、
`getNumberOfAvailableResults()`、`getFirstResultPoint()`、`getLastResultPoint()`、
`getMeasurementType()`、`getPassFail()`、`getFailInfo()`、`getValue()`、`getValues()`、
`getExpectedResult()`。
**`getExpectedResult()` 是 7.3.1 新加的**（见「版本」）。

### 一条必须先知道的物理限制

原文单有一句 `Note`：

> 「The number of samples captured during DC profiling can slightly vary per pin. This is caused by
> the internal triggering of the profiling, which is not vector exact.」

**即：DC profiling 采到几个点，各个 pin 之间可能不一样，而且不是确定值。**
**这一条决定了你写循环时不能拿一个「事先算好的点数」当上界**——
要用 `getRangeOfAvailableResults()` 问出来的范围（推断：这是本页对该 Note 的用法解读，
**原文没有把它和下面那些循环写法连起来说**）。

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
用法全在 `## Examples` 一节——**5 个例子，全被脚本逐字收进了上面的「语法 / 参数」节**。
这里只说**要按什么顺序读它们、以及例子里的硬规矩**。

**先读 `### Note` 那句结论**（原文）：

> 「The examples provide various approaches for the use of the upload function uploadResult(). In
> the last example below, the uploadResult() is called inside the ON_FIRST_BLOCK. This reduces the
> test time considerably and, therefore, is the recommended approach.」

**即：官方推荐的写法是把 `uploadResult()` 放进 `ON_FIRST_INVOCATION…` 块里**
（Example 5 就是这一种）。**其余四个例子是「各种写法」，不是同等推荐。**

**五个例子各自教什么**（本页按原文各例的引言段归纳）：

| 例 | 原文引言里的定位 |
|---|---|
| Example 1 | 完整流程：先 `getRangeOfAvailableResults()` 拿范围，再 `uploadResult()`，再遍历 |
| Example 2 | `Same as Example 1 above, except in block "c) upload the results"`——用「返回范围的」那个重载省掉一次调用 |
| Example 3 | `all available results will be uploaded`，用 `for` 循环 + `getPassFail` / `getValue` / `getFailInfo` |
| Example 4 | 在 `FOR_EACH_SITE_...` 块里多 site 上传，用到带字符串参数的构造器 |
| Example 5 | `uploadResult()` 放在 `ON_FIRST_INVOCATION...` 块内——**推荐写法** |

**官方主流程**（Example 1 的骨架，本页照它的步骤列，**不是文档给的编号流程**）：

1. **问范围**：`results.getRangeOfAvailableResults(pin, TM::RESULT_INDEX)` → 得到 `TM::RESULT_RANGE`。
2. **上传**：`results.uploadResult(pin, resultRange)`（**把范围显式传进去**）。
3. **取两端**：`getFirstResultPoint(pin)` / `getLastResultPoint(pin)` → 两个 `RESULT_POINT`。
4. **遍历**：`while (currentPoint <= lastPoint) { … ++currentPoint; }`。
5. **取值 / 判定**：`getPassFail()` / `getValue()` / `getFailInfo()`。
6. **交结果**：`TEST(results);`（Example 3 用的是 `TEST(allResults, TRUE);`）。

**四条写在代码注释里的硬规矩**（原文逐字，都在 Example 1 / 3 的注释里）**——这几条最容易被跳过**：

- **循环上界必须用 `<=`**：
  `Note that both first and last represent valid RESULT_POINTS. You must use "less or equal" (<=) in the comparison to include also the last RESULT_POINT. Using a "<" or "!=" operator in the comparison would drop the last result.`
- **上传会覆盖上一次的结果，而且跨对象**：
  `Before the result data can be accessed, they always first need to be uploaded from hardware/firmware. Each uploadResult() will overwrite the last uploaded results. (independent of the particular DC_RESULT_ACCESSOR object!).`
- **能省一次调用就省**：
  `results.uploadResult(pin, TM::RESULT_INDEX); would have the same effect, but calls getRangeOfAvailablResults() internally again. As this reduces performance, avoid this form of uploadResult() if you already have determined the range of available results.`
- **`getRangeOfAvailableResults` 在多 pin 时给的是公共范围**：
  `The returned result range contains the information about available number of results for the pin. If more than one pin is used for example, a group) the smallest common result range for both pins is returned.`

**两条正文里的使用条件（比例子更要紧，因为写错了不会报错）**：

- **`getPassFail()` 只在「上传了全部结果」时才可信**，原文：
  > 「Use these methods only if the previous uploadResult() call specifies to upload ALL results
  > (uploadAllResults = TRUE), otherwise it will always return FAIL.」
- **取回来的值可能是无效的**，原文（`getValue()` 与 `getValues()` 两处各有一句 `CAUTION`）：
  > 「CAUTION The uploaded value can be invalid. Use `RESULT_FAIL_INFO` to check the reported value
  > is valid and not marked as fail.」

**还有一条只能从版本记录倒推的**：`SmarTest 7.3.1: New parameter site.`——
所以 7.3.1 之前那些带 `site` 的写法在这篇文档的语法里是新的（**旧版本能不能用，本篇没说**）（推断）。

## 和谁有关

- [[dps-pins-editor]] / [[digital-pins-editor]] — **pin 类型由这两处定义**。
  原文把两类 pin 与两个编辑器一一对应：
  `DPS operating mode pins (defined with the DPS Pins editor)` 与
  `PMU operating mode pins (defined with the Digital Pins editor)`。
  **这一条边是文档直接给的。**
- [[testmethod]] — **它的宿主**。本篇的 `stage` 是 `testmethod`，
  5 个例子全是 `virtual void run()` 里的代码（**那页本页没读**）。
- [[ganging]] — **`RESULT_RANGE` 里有一个 `gangIndex` 字段**。原文：
  `representing the gang index in case of ganged channels. It is usually used only when the RESULT_RANGE struct is an input parameter for a function. It is usually not returned (i.e. always set to '0') by functions returning the RESULT_RANGE struct.`
  —— **本页是 wiki 里少数直接写到 gang 索引的位置**（**[[ganging]] 那页本页没读**）。
- [[limit]] — **`getExpectedResult()` 取的就是 limits**。原文：
  `This function gets the test limits for the specified pin in the specified result.`
  并让你 `refer to RESULT_POINT and LIMIT for more information`（**[[limit]] 那页没读**）。
- [[results]] — **它取的对象的统称**（`measurement results`），
  也是本篇 `stage: results` 的来处（推断，仅指归属）。
- [[dc-test-programming]] — **DC 测量的编程主题**。
  本篇提到 `DC Dynamic measurement` 与 DC event APIs，
  **但没有一句话把它与那页连起来**（推断，仅指主题相邻）。
- **卡页**：[[dc-scale-xps256-card]]、[[dc-scale-uhc4t-card]]、[[dps128-dps64-cards]] ——
  本篇的支持矩阵里点了这三族卡（XPS256 / UHC4T / DPS128）。
  **但那三页本页一篇都没读**；**XPS256 的两种 operating mode 另有专页**
  （`xps256-programming-dps-operating-mode` / `xps256-pmu-operating-mode`，**均未读**）。
- `DPS_TASK` / `SPMU_TASK`（**未建、未读**）— 结果的**两个主要来源**，
  本篇说 `allows you to obtain the results from measurement set up through` 它们。
- `RESULT_POINT` / `RESULT_POINT_LIST` / `RESULT_FAIL_INFO`（**均未建、均未读**）—
  **三个 helper 类，也是 `## Related information` 里的前三条链接**。
  **本页凡提到它们，依据只是本篇那几句描述。**
- `ERRE?` / `DFTD, DFTD?` / `VALR?`（**均未建、均未读**）—
  `## Related information` 里另外三条链接（**本篇正文没提它们**）。
- `RESULT_AREA_CONFIG_SET`、`PPMU_...`、`BADC_...`、DC event APIs（**均未建、均未读**）—
  本篇提到但没有任何链接。
- [[for-each-site-begin]] / [[on-first-invocation-begin]] — **例子用到的两个宏**
  （Example 4 的 `FOR_EACH_SITE_BEGIN()`、Example 5 的 `ON_FIRST_INVOCATION_BEGIN()`）。
  **本篇没有链接它们**，是本页按宏名接的边（推断）。

## 版本

原文 `## Functional changes` 段共 **6 行**，**第 1 行是哨兵值**，其余 5 条是本文档自己的记录：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.3.1: New function getExpectedResult().`
- `SmarTest 7.3.1: New parameter site.`
- `SmarTest 7.3.1: DC Scale PVI8 card added.`
- `SmarTest 7.4.0: DC Scale AVI64 card added.`
- `SmarTest 7.10.1: DC Scale XPS256 card added.`

**第 1 行要按哨兵值读**（§11.2 ②）：它的意思是
「**在本文档集覆盖范围开始之前就已经有了**」，
**不是「SmarTest 6.3.2 引入了 `DC_RESULT_ACCESSOR`」**。
照字面读会造出一条假版本事实，而且格式齐整、看不出是哨兵。

**这个版本号对本次目标很有用**：wiki 的版本目标是 **SmarTest 7.10.3**，
而 **`DC Scale XPS256 card added` 记在 `7.10.1`**——
**即 XPS256 的支持是 7.10 线才加进来的，非常新**。

**注意版本记录与正文对不上**（详见「出处」③）：
版本里点了三张卡 `PVI8` / `AVI64` / `XPS256`，
而**正文的支持矩阵里只有 DPS128 / XPS256 / UHC4T——`PVI8` 与 `AVI64` 在正文里一次都没出现**。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.28_DC_RESULT_ACCESSOR.md`
（`99071.htm`，**28,229 字节 / 573 行**）——**整篇读完**。

**「语法 / 参数」节收了 9,753 字符**，逐字来自原文的 `## Examples` 一节（含 `### Note` 与
Example 1–5 的 5 段代码）。**它收的是例子，不是参数表**——
**参数表式的 `Parameters` 块在原文里散在每个成员函数下面，脚本没有把它们收进来**
（脚本只认 `Examples` 这类段标记）。

**本页没做的：**

- **`## Related information` 里的 6 篇一篇都没读**：
  `RESULT_POINT` / `RESULT_POINT_LIST` / `RESULT_FAIL_INFO` / `ERRE?` / `DFTD, DFTD?` / `VALR?`。
  **所以「`RESULT_POINT` 到底是什么、能不能自己构造、`RESULT_FAIL_INFO` 有哪些状态位」
  本页一个字都没有**——本页只有本篇文档里那几句描述。
- **`DPS_TASK` / `SPMU_TASK` / DC event APIs / `PPMU_...` / `BADC_...` /
  `RESULT_AREA_CONFIG_SET` 都没读。** 所以「结果是怎么产生的」那一半本页写不了，
  **本页只有「怎么把已经产生的取回来」这一半**。
- **正文提到的那几个类 / 宏没读**：`DPS Pins editor`、`Digital Pins editor`、
  `LIMIT`、`RESULT_POINT`、`ON_FIRST_INVOCATION_BEGIN/END`、`FOR_EACH_SITE_BEGIN/END`。
  **例子里的每一行代码本页都当作「原文这么写的」来读，没有去核对它们在别处是怎么定义的。**
- **`PVI8` / `AVI64` 两张卡的任何资料都没有**（本篇正文也没提它们，见下）。
- **本篇文档里没有 `## Errors` 段、没有 `## Procedure` 段、没有 `## Application` 段、没有任何图。**

> ⚠️ **语料瑕疵，照实记下，一处都没替它改**：
> ① **同一篇里 `addressing scheme` 的类型名有两个拼法。**
>    函数签名里一律是 `TM::RESULT_ADDRESSSING_SCHEME`（**`ADDRESSSING`，三个 `S`**），
>    而 `RESULT_RANGE` 的字段说明里写的是 `addressingScheme of type TM::ADDRESSING_SCHEME`
>    （**两个 `S`**）。**两种拼法都在原文里，本页照抄不调和。**
> ② **`uploadResult()` 的 5 个例子，没有一个用的是文档列出的签名。**
>    文档给的 `uploadResult` 两个重载都以 `const INT site` 开头
>    （`uploadResult(const INT site, const STRING& pins, const TM::RESULT_ADDRESSSING_SCHEME& addressingScheme)` 等），
>    而例子逐字写的是 `results.uploadResult(pin, resultRange)`、
>    `result.uploadResult("dps1",TM::RESULT_INDEX)`、
>    `result.uploadResult("dps1", TM::RESULT_INDEX, range)`——**都是不带 `site` 的短形式**。
>    同样的落差在 `getMeasurementType(p)`（文档列的是两参数的 `getMeasurementType(singlePin, resultPoint)`）、
>    `getPassFail("dps1", p)`、`getValues("dps1")` 上也各有一处。
>    —— **例子用的是一个比类定义更宽松的 API 面，原文没有一句话解释这个落差。**
> ③ **版本记录里有两张卡在正文里一次都没出现**：`SmarTest 7.3.1: DC Scale PVI8 card added.` 与
>    `SmarTest 7.4.0: DC Scale AVI64 card added.` ——
>    **正文的支持范围（第 12 行）只写了 `DC Scale DPS128 and XPS256` 与 `DC Scale UHC4T pins`。**
> ④ **一个悬空的参数名**：`getPassFail()` 的说明逐字写
>    `Use these methods only if the previous uploadResult() call specifies to upload ALL results (uploadAllResults = TRUE), otherwise it will always return FAIL.`
>    —— 可是**文档列出的任何一个 `uploadResult()` 签名里都没有叫 `uploadAllResults` 的参数**。
>    **这句话给出的操作办法（「就要设 `uploadAllResults = TRUE`」）读者根本无处可设。**
> ⑤ **一处代码注释与它自己的代码矛盾**：Example 1 里逐字写
>    `// As this example uploaded only fails, this condition will always be true.`
>    —— 可**同一段代码上面调的是 `results.uploadResult(pin, resultRange);`（上传全部结果），
>    不是 `uploadFailedResult()`**。注释说的「只上传了 fail」与代码不符。
> ⑥ **函数名在注释里被写错**：Example 3 的注释逐字写
>    `but for uploadFailedResults() it is usually larger than the number of failed results`
>    —— **API 里叫 `uploadFailedResult()`（单数），注释写成了 `uploadFailedResults()`（复数）。**
> ⑦ **括号不配对**：Example 1 注释逐字
>    `// one pin is used for example, a group) the smallest common result range for both pins is returned.`
>    —— **`a group)` 只有右括号，左括号丢了。**
> ⑧ **`Parameter` 帮助块的参数名与签名对不上，且同一件事被写了两个名字**：
>    `getFailInfo()` 的签名写 `listofResults`、帮助块写 `listofResult`；
>    `getValue()` 的帮助块同时列了 `result`（`The result (RESULT_POINT) to be considered.`）
>    与 `resultPoint`（`Specifies a test result point for which to return the specified result.`）
>    —— **两个名字描述的是同一个东西，而签名里根本没有 `resultPoint`。**
> ⑨ **一个从未定义过的类型**：`getFailInfo()` 的签名里出现了 `RESULT_POINT_ARRAY`
>    （`getFailInfo(const STRING& singlePin, const RESULT_POINT_ARRAY& listofResults)`），
>    **而 `## Class definition` 只列了 `RESULT_POINT` / `RESULT_POINT_LIST` / `RESULT_FAIL_INFO`
>    三个 helper 类**——`RESULT_POINT_ARRAY` 全篇只出现这一次。
> ⑩ **`Note` / `CAUTION` 被塞在正文中间、与前后句子首尾相连**，逐字如：
>    ` Note It is recommended to use the syntax forms with parameter RESULT_POINT or LIST as that they have the same functionality as those with the parameter singlePin.  CAUTION The uploaded value can be invalid.`
>    —— **`Note` 与 `CAUTION` 之间没有换行、没有标点**，`as that they have` 也是重复连接词。
>    **同一形态在 `getValues()` 一处重复出现。**
> ⑪ **`Parameters` 表格塌过**：构造器那段逐字是
>    ` | dcResultConfigurationSetName  | Defines the result configuration set to be set before data uploading.  |      Member Functions:`
>    —— **`Member Functions:` 这一行被并进了表格最后一格**，表结构在此断开。
> ⑫ **链接写法不一致**：`[PMU operating mode pins ](<…>)` **链接文字尾部多一个空格**，
>    紧跟其后的 `(defined with the …)` **与链接之间没有空格**，
>    而同一句里的 `DPS operating mode pins` 那个链接前后都是正常的。
> ⑬ **`### Note` 这个标题的层级可疑**：它挂在 `## Examples` 之下，
>    内容却是**对全部例子的总体建议**（`The examples provide various approaches…`），
>    **不是某一段的注解**——`### Example 1` 与它是平级。

`verified: doc-only` —— **本页的 API 没有在任何真实机台上调用过**
（§11：文档里有 ≠ 这台机器上能用；本篇是 API 参考，不是实测记录）。
