---
type: object
title: TEST
layer: L2
stage: testmethod
tags: [testmethod, l2, api, judgment, datalog, limit, reliability, flexible-dc, spec-search, judgeandlog]
related: [testset, limit, tmlimits, get-functional-result, spec-search, dc-result-accessor, on-first-invocation-begin, for-each-site-begin, event-formatter, alphabetical-list-of-flags, mapping-testmethod, testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.241_TEST.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# TEST

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **10,217 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.241_TEST.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

For functional tests:

```
Boolean TEST(Boolean continue = FALSE);
Boolean TEST(Boolean continue, TM::RELIABILITY reliability);
```

Note It can only retrieve and log the latest functional test result when no other sequencer based tests have been executed between `FUNCTIONAL_TEST` and `TEST`.

The following is also available for multiport testing only:

```
Boolean TEST(const STRING& port, Boolean continue = FALSE);
Boolean TEST(const STRING& port, Boolean continue, TM::RELIABILITY reliability);
```

For AC tests or any tests:

```
Boolean TEST(const STRING& pin, const STRING& testname,                                DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname,                                DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& pin, const STRING& testname,                                DOUBLE value, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname, const LIMIT& limit,            DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname, const LIMIT& limit,            DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& pin, const STRING& testname, const LIMIT& limit,            DOUBLE value, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
```

The following are also available for multiport testing only:

```
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname,                                DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname,                                DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, const LIMIT& limit,            DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, const LIMIT& limit,            DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
```

For DC tests:

```
Boolean TEST(const PMU_IFVM& dc,  Boolean continue = FALSE);
Boolean TEST(const PMU_IFVM& dc,  Boolean continue,         TM::RELIABILITY reliability);
Boolean TEST(const PMU_VFIM& dc,  Boolean continue = FALSE);
Boolean TEST(const PMU_VFIM& dc,  Boolean continue,         TM::RELIABILITY reliability);
Boolean TEST(const DPS_VFIM& dps, Boolean continue = FALSE);
Boolean TEST(const DPS_VFIM& dps, Boolean continue,         TM::RELIABILITY reliability);
```

For flexible DC tests:

```
Boolean TEST(const PPMU_MEASURE& dc, Boolean continue = FALSE);
Boolean TEST(const PPMU_MEASURE& dc, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const PPMU_MEASURE& dc, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const PPMU_MEASURE& dc, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& port, const PPMU_MEASURE& dc, Boolean continue, TM::RELIABILITY reliability);
```

For DC dynamic tests:

```
Boolean TEST(DC_RESULT_ACCESSOR& dcResultAccessor, Boolean continue = FALSE);
```

For spec searches:

```
Boolean TEST(const SPEC_SEARCH& specSearch, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const SPEC_SEARCH& specSearch, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue, TM::RELIABILITY reliability);
```

For ppTIA measurements:

```
Boolean TEST(const PPTIA_TASK& pptia, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const PPTIA_TASK& pptia, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& port, const PPTIA_TASK& pptia, Boolean continue = FALSE);
Boolean TEST(const STRING& port, const PPTIA_TASK& pptia, Boolean continue, TM::RELIABILITY reliability);
```

Parameters
 |

I/O

 |

Parameter

 |

Description / Range

 |
 |

I

 |

continue

 |

(Option.) This parameter controls whether the test should be continued if the TEST API returns FAIL. If it is set to TRUE, the test is continued in spite of a FAIL result. If it is set to FALSE (this is the default), the test is terminated. Instead of TRUE or FALSE, you can also use the enumerator TM::CONTINUE. If the TEST API returns PASS, the test is always continued.

Note that the API behaves differently for the first site in a multi-site setup. In this special situation, the test is always continued, even if the TEST API returns FAIL and the continue parameter is set to FALSE. For the following sites, the test is terminated under these conditions.

You can omit this parameter. However, you must specify it if you also specify the reliability parameter.

 |
 |

I

 |

reliability

 |

(Option.) This parameter is used to indicate the reliability of the test result for data logging. To indicate the test is reliable, specify TM::RELIABLE. To indicate the test is unreliable, specify TM::UNRELIABLE.

You can omit this parameter. If so, use the syntax without this parameter. At that time, it is the same as specifying TM::RELIABLE.

 |
 |

I

 |

port

 |

For multi-port testing only. The port name whose functional test result or Flexible DC test result is judged and logged. Note that any pin group cannot be specified in the TEST API.

 |
 |

I

 |

pin

 |

The pin name (single pin name).

 |
 |

I

 |

testname

 |

The test name that can be referred from the Properties view. Test names can reference limits on the `Tests`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.32.03.01.03_Tests_page.md`） page.

 |
 |

I

 |

value

 |

The test result value.

 |
 |

I

 |

limit

 |

The optional limit value to be used for the judgment. This parameter is a `LIMIT`（raw: `02.07.04.01.126_LIMIT.md`） API's class object. Hence, you can specify TM::Pass or TM::Fail to make the test result pass or fail intentionally.

You can omit this parameter.

 |
 |

I

 |

logTestNumber

 |

An optional test number.

If this test number is provided, it overrides the actual test number. If it is not provided, the actual test number is logged.

 |
 |

I

 |

softBin

   | The software bin number of the multibin. For details see the `SET_MULTIBIN`（raw: `02.07.04.01.212_SET_MULTIBIN.md`） API. |
 |

I

 |

hardBin

   | The hardware bin number of the multibin. For details see the `SET_MULTIBIN`（raw: `02.07.04.01.212_SET_MULTIBIN.md`） API. |
 |

I

 |

tmLimit

 |

Specifies the optional `TMLimits`（raw: `02.07.04.01.250_TMLimits.md`）`object`（raw: `02.07.04.01.250_TMLimits.md`） from which the limit data are taken.

 |
 |

I

 |

dc

 |

`PMU_IFVM`（raw: `02.07.04.01.151_PMU_IFVM.md`） or `PMU_VFIM`（raw: `02.07.04.01.152_PMU_VFIM.md`） constructor which specifies a DC test to be judged, or an object of `PPMU_MEASURE`（raw: `02.07.04.01.157_PPMU_MEASURE.md`） API which specifies a Flexible DC test to be judged and logged.

 |
 |

I

 |

dcResultAccessor

 |

The `DC_RESULT_ACCESSOR`（raw: `02.07.04.01.28_DC_RESULT_ACCESSOR.md`） object from which the test data is taken.

 |
 |

I

 |

dps

 |

`DPS_VFIM`（raw: `02.07.04.01.51_DPS_VFIM.md`） constructor which specifies a DC test to be judged.

 |
 |

I

 |

specSearch

 |

The `SPEC_SEARCH`（raw: `02.07.04.01.233_SPEC_SEARCH.md`） API's class object to specify a spec search measurement to be judged.

 |
 |

I

 |

pptia

 |

`PPTIA_TASK`（raw: `02.07.04.01.165_PPTIA_TASK.md`） object from which the test data is taken

 |

### Example 1

```
double thd_result;
TEST("dgtz_pin", "THD", thd_result);
```

The TEST API compares the thd_result data with the limit range specified in the Properties view, then judges it as pass or fail.

### Example 2

```
double thd_result;
double snr_result;
TEST("dgtz_pin", "THD", thd_result,TM::CONTINUE);
TEST("dgtz_pin", "SNR", snr_result);
```

The first TEST API judges the thd_result data as pass or fail. Then the second TEST API judges the snr_result data as pass or fail because the TM::CONTINUE is described in the last parameter of the first notation. When the result of the first TEST is pass, the test will continue even if the you do not set the continue flag to TRUE.

### Example 3

```
double thd_result;
double low_limit, high_limit;
TEST("Aout", "THD", LIMIT(TM::GT, low_limit,TM::LT, high_limit), thd_result);
```

First of all, the TEST API compares the thd_result data with the limit range specified by the LIMIT API, then judges as pass or fail.

### Example 4

```
TEST(PMU_VFIM("PIN1"));
```

The TEST API retrieves the pass/fail judgment of the `PMU_VFIM("PIN1")` which specifies the limits and result of the current measurement test using Pin PMU connected to PIN1.

### Example 5

```
int Time_out,Trig_state;
START_TEST();
WAIT_TEST_DONE(1 sec, &Time_out, &Trig_state);

if(Trig_state == 1){
 cout << "One or more digitizers has not received any trigger." << endl;
 TEST("","",TM::Fail,0,TM::CONTINUE,TM::UNRELIABLE);
}
```

If the used digitizers cannot receive the predictable starting trigger correctly, the TEST API always judges the dummy result "0" as "Fail" by indicating the "unreliable" state.

<!-- 语法节 end -->

## 是什么

**TEST 是 L2 的判定 API：把一个测量值按限值判成 pass/fail，并把这次判定写进数据日志。** 定义文档的第一句就是这三件事：

> 「This API judges the test data as pass/fail and logs it.」

**这一页最该先看到的是文档自己给的继任者。**（原文逐字）

> 「The judgeAndLog APIs replace the existing TEST APIs for improved usability. It is recommended that you use the judgeAndLog APIs.」

> 「The TEST APIs are reserved for backward compatibility and may be removed from a future release.」

**那些 `judgeAndLog_***` 属于 `TESTSET` 那一族**（原文：`Refer to the description for the TESTSET API for information about the judgeAndLog APIs that are also used to judge and log test data.`）→ 见 [[testset]]。**所以这一页写的是「还能跑、但新代码不该再写」的接口。**

### 两个不许用的地方

> 「The TEST API cannot be used within a first-invocation block, not even inside an "each site" loop block.」

**即 `ON_FIRST_INVOCATION_BEGIN/END` 块里不能调 TEST，`FOR_EACH_SITE_BEGIN/END` 里也不能** → [[on-first-invocation-begin]] / [[for-each-site-begin]]。**同一批文档里的 [[limit]] 与 [[get-functional-result]] 也各写了一条方向相同的禁令**（那两个都要求待在块外），**但三篇是各写各的、没有一句总纲**——本页只记 TEST 这一句，不替它们归纳。

**定义在哪个头文件**：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/TestControl.h.」

### 九个语法族，差别是「判什么」

逐字见上面 `## 语法 / 参数` 节：**functional / multiport functional / AC 或任意测试 / multiport AC / DC / Flexible DC / DC dynamic / spec search / ppTIA**。**每一族都返回 `Boolean`**；`continue` 各族都有，`reliability` 是它后面的那个可选参数。参数表 **16 行**（`continue` / `reliability` / `port` / `pin` / `testname` / `value` / `limit` / `logTestNumber` / `softBin` / `hardBin` / `tmLimit` / `dc` / `dcResultAccessor` / `dps` / `specSearch` / `pptia`）。

### `continue`：FAIL 之后还走不走

> 「If it is set to TRUE, the test is continued in spite of a FAIL result. If it is set to FALSE (this is the default), the test is terminated.」

> 「Instead of TRUE or FALSE, you can also use the enumerator TM::CONTINUE.」

> 「You can omit this parameter. However, you must specify it if you also specify the reliability parameter.」

**多 site 时第一条 site 是例外，而且这条例外是「无条件」的**：

> 「Note that the API behaves differently for the first site in a multi-site setup. In this special situation, the test is always continued, even if the TEST API returns FAIL and the continue parameter is set to FALSE. For the following sites, the test is terminated under these conditions.」

### `reliability`：只用来标「这次结果不可信」

> 「You can omit this parameter. If so, use the syntax without this parameter. At that time, it is the same as specifying TM::RELIABLE.」

> 「Note that the TEST API does not log the reliable state even if the reliability parameter is set to TM::RELIABLE.」

**即：`TM::RELIABLE` 是默认值，而且它什么都不写日志；只有 `TM::UNRELIABLE` 才会在 event data log 里留痕。** 而系统自带的 Event Formatter **连这个痕迹也不写进 report window**：

> 「The system-supplied Event Formatter does not write the unreliable state on the event data log stream to the report window. However, the pass/fail result for each test on the displayed data log indicates a blank for an unreliable result.」

> 「It is available for the global pass/fail result only of a DC test or functional test. To write the unreliable state, you need to develop an original report formatter.」

**颗粒度也有限**：

> 「For a DC test or functional test, the TEST API logs the unreliable state for the global pass/fail result only, not for the per-pin results.」

### 连着调几次：返回值是 AND

> 「You can use the continue parameter to call the TEST API several times in succession and return an overall result of all these calls. The final return value to the testflow is computed as the logical conjunction (AND) of all TEST calls; so, if at least one call returns FAIL, the overall result will be FAIL. This computation is performed at the end of all of the remaining statements.」

**再加上第一条 site 的那条例外，多 site 下「哪些 TEST 真的跑了」与 continue 无关**：

> 「If you call the TEST API repeatedly in a multi-site setup, you must take into account that for the first site, the test will be continued after every TEST call, even if it has the continue parameter set to FALSE and returns FAIL.」

### 限值从哪来（四档，优先级由「参数给没给」决定）

| 调用里给的 | 判定用哪个限值 |
|---|---|
| **什么都不给** | **Properties view 里这个 `testname` 的限值** |
| `const LIMIT& limit` | 该 [[limit]] 对象（见上面参数表的 `limit` 行） |
| `V93kLimits::TMLimits& tmLimit` | 该 [[tmlimits]] 对象 |
| `TM::Pass` / `TM::Fail` | **不看实测值**，恒 pass / 恒 fail |

原文（这两句一起读才看得出四档是互斥的）：

> 「If the parameter limit is not specified, the limit values specified in the Properties view will be used. If you specify the Pass class object of the LIMIT API, the pass is always returned regardless of the actual test result. If you specify the Fail class object for the LIMIT API, fail is always returned regardless of the actual result.」

> 「Whenever the limit parameter is supported, you can also supply a TMLimits object, as noted above in the AC test syntax descriptions.」

**`testname` 不是一个普通字符串，它指向 GUI 上的限值表**：

> 「The test name that can be referred from the Properties view. Test names can reference limits on the Tests page.」

（`Tests` 页 = raw 里的 `../02.08_Setup_and_Result_Tools/02.08.04.32.03.01.03_Tests_page.md`，**不在本页 sources，本页没读它**。）

### 强制 pass / 强制 fail：两个惯用法

> 「If you need to make a test result fail intentionally, you can use the statement TEST ("","",TM::Fail,0). This statement makes a test result fail forcedly.」

> 「In contrast to this, if you need to pass, you can use the statement TEST ("","",TM::Pass,0).」

> 「Where, TM::Fail and TM::Pass are the LIMIT API class objects and 0 is a dummy value of the test result.」

（`TM::Fail` / `TM::Pass` 是 [[limit]] 的两个**常量对象**——`always pass` / `always fail`。空字符串那两个参数就是上面参数表里的 `pin` 与 `testname`。）

### 功能测试的判定：TEST 只取「最近一次」

> 「Note It can only retrieve and log the latest functional test result when no other sequencer based tests have been executed between FUNCTIONAL_TEST and TEST.」

**要按 pin 看结果就得换 API**：

> 「To get the pass/fail result in a specific pin, use the GET_FUNCTIONAL_RESULT API.」

**而「最近一次功能测试」可以由这些 API 产生**（也就是说 TEST 不关心它是谁跑的）：

> 「The functional test can be executed by the FUNCTIONAL_TEST, DIGITAL_CAPTURE_TEST, NB_DIGITAL_CAPTURE_START, PMU_VFIM, PMU_IFVM, or DPS_VFIM APIs.」

### spec search 与 Flexible DC 各有一条特殊判定

**spec search 判的不是限值，是「跃迁」**：

> 「For judgment of spec search, the TEST API judges the last spec search test result and produce a data log event. If a pass/fail or fail/pass transition is found the return value is TRUE else it returns FALSE. If the spec search is not performed prior to this API call, an error occurs.」

**Flexible DC 按 GPF 判，并且一个限值条件一条 event 写进 EDL**：

> 「TEST API for Flexible DC judges the test result based on the Global Pass Fail (GPF) result.」

> 「However, only one multiple-limit condition is allowed in a Multiple Result Parametric (MPR) Record. Therefore, TEST API for Flexible DC creates a test event for each limit condition, and outputs the test results of each test event for each limit condition to the Event Data Log stream (EDL).」

> 「Then the test results of the Flexible DC test are placed into the MPR record for each limit condition and are recorded in converted STDF.」

（`EDL` / `STDF` 两个缩写的专页本页没读——见「出处」。）

### STDF 转换前的一条硬前提

> 「If you will be converting the test data from the event data log to Standard Test Data Format (STDF) for test data analysis, the entry for the pin parameter specified for AC Test or Any test and for DC Test must be an existing, defined pin name.」

> 「With the Check Testmethod API flag set to "on", a fatal error will occur at runtime if the pin parameter is not an existing, defined pin name.」

**即：想把这份 log 转成 STDF，`pin` 参数必须是已定义的 pin 名；把 `Check Testmethod API flag` 打开之后，写错 pin 名会在运行时变成 fatal error。**（flag 的清单在 [[alphabetical-list-of-flags]]；那句里的 `Check Testmethod API flag` 在 raw 里是那篇的一个锚点。）

### datalog 侧要动的东西

> 「To log test data by using the TEST API and display the test report by using the logged data, you must set the report formatter to the EventFormatter and enable the required flags.」

> 「If you develop original report formatter for event data logging, you should understand that the TEST API produces a data log event of the type "TestEventType".」

**这一条决定了两件事**：① 用 TEST 写的日志要看得见，得先配 report formatter（见 [[event-formatter]]，**未建**）与相关 flag；② 自己写 formatter 的话，要认的事件类型是 `TestEventType`。

## 典型用法

**文档里没有 `## Procedure` 段。下面五条是本页按 `## Important points` 与五个 Example 的依赖关系排的（推断），每条的出处都标了。**

**1. 最基础的一次判定：`testname` + 结果值。**（Example 1）

> 「The TEST API compares the thd_result data with the limit range specified in the Properties view, then judges it as pass or fail.」

**注意它是「去 Properties view 拿限值」——所以 `testname` 必须在那儿有对应的限值行**，否则这四档里的第一档就没有来源。

**2. 一连串判定：用 `continue` 串起来。**（Example 2）

> 「The first TEST API judges the thd_result data as pass or fail. Then the second TEST API judges the snr_result data as pass or fail because the TM::CONTINUE is described in the last parameter of the first notation.」

**3. 调用里直接带着限值：把 `LIMIT` 对象塞进第三参。**（Example 3）

> 「First of all, the TEST API compares the thd_result data with the limit range specified by the LIMIT API, then judges as pass or fail.」

**4. DC 测量直接判：参数是测量对象本身。**（Example 4 是 `TEST(PMU_VFIM("PIN1"))`）

> 「The TEST API retrieves the pass/fail judgment of the PMU_VFIM("PIN1") which specifies the limits and result of the current measurement test using Pin PMU connected to PIN1.」

**5. 硬件没准备好时，主动判一个「不可信」的 fail。**（Example 5：trigger 没收齐）

> 「If the used digitizers cannot receive the predictable starting trigger correctly, the TEST API always judges the dummy result "0" as "Fail" by indicating the "unreliable" state.」

**常见组合的记法**：**判定本身只有「限值从哪来」这一个自由度**（上表四档）；**`continue` 管流程**、**`reliability` 管日志**、**`logTestNumber` / `softBin` / `hardBin` 管编号与分 bin**——后四个都只影响这次判定的登记方式，不影响判据。

## 和谁有关

**入边 44 条 / 38 篇（含 1 条 `index.md` 的 toc），出边 40 条 / 20 个目标**——两边都取自 `extract/edges.jsonl`（`resolved=true`，**不是本页 sources 的正文**，本页只当链接证用）。

- [[testset]] — **继任关系**：文档第一段点名 `judgeAndLog_***` 取代 TEST API，且「recommended」。**入边里 `TESTSET.*` 一组占了 5 条**（`TESTSET__.testname`、`.testnumber`、`.judgeAndLog_ScanTest` 等），**说明这一族确实在拿 TEST 当参照物**。
- [[limit]] — **参数类型**：`limit` 那一档就是 LIMIT 类的对象；**LIMIT 那篇的三处示例全部写在 `TEST` 的调用里**（互相指）。
- [[tmlimits]] — 同一位置可换 `V93kLimits::TMLimits&`（`## Important points` 明写「whenever the limit parameter is supported」）。
- [[get-functional-result]] — **分工**：TEST 判「最近一次整体」，按 pin 取结果要换它。**⚠️ 2026-09-20 更正**：本页初版写「两篇**互为出边**（各 1 条）」——**那是假的**。实测 `extract/edges.jsonl`：**`TEST → GFR` 2 条、`GFR → TEST` 0 条**，是**单向**的。（同一天在 `get-functional-result` 与 `task-list` 两页上各有一处同型的假话，都已由并发的写页 agent 修正。）
- [[on-first-invocation-begin]] / [[for-each-site-begin ]] — **禁区**：TEST 不许出现在这两个块里。
- [[spec-search]]/ [[dc-result-accessor]] — **语法族的参数类型**：`SPEC_SEARCH` 是 spec search 那一族的入参，`DC_RESULT_ACCESSOR` 是 DC dynamic 那一族的入参（两者在本页各只出现一次）。
- [[event-formatter]]、[[edl-file]]、[[stdf ]] — **日志侧**：TestEventType / EDL / 转 STDF 三条都在讲「这次判定去了哪」。
- [[alphabetical-list-of-flags]] — `Check Testmethod API flag` 的清单在那里。
- [[dps-aux-pin-task]] — **顺序上的对手**：GFR 那篇要求 `DPS_AUX_PIN_TASK.check...()` 必须在 GFR 之前，而本页的 `## Related information` **没有链它**（**这一条依据的是 GFR 那篇，不是本页**，写在这里只为让顺序约束有个落脚点）。
- [[mapping-testmethod]] — 本 wiki 的跨层对照表把本页放在 L2 的「判定并写 datalog」那一行，同行还有 [[testset]] 与 [[limit]]。

**离本页最近的邻居都是 `02.07.04.01.*` 这一族**（`02.07.04.01_APIs_in_alphabetical_order.md` 那条索引也链了本页）；**外面进来的最密的是 `03.02_How_to_do_Multi-Site_Testing`**（`03.02.04.10_API_Behavior_on_Multisite_Testing.md` 2 条）——**多 site 的例外行为正是那篇要讲的事**。

## 版本

`## Functional changes` 段两条（逐字）：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.5.3: Optional logTestNumber, softBin, and hardBin parameters added to some variants of TEST().`

**读第一条要注意**：`Introduced before SmarTest 6.3.2` 是**哨兵值，不是「6.3.2 新增」**——全语料 2,677 条可用性行都写同一个版本号、措辞都是 `before`，意思是「本套文档集覆盖范围开始之前就已经有了」（`wiki/schema.md` §11.2②）。**本页照原样抄，不把它读成 6.3.2 的变更。**

**第二条是能落地的**：`logTestNumber` / `softBin` / `hardBin` 三个参数**在 7.5.3 才加到部分 TEST() 变体上**——**即 7.5.3 之前那些变体没有这三个参数**，而上表参数里它们只是「some variants of TEST()」有的。

## 出处

`sources:` 一篇，**整篇读完**（449 行 / 18,730 字节）：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.241_TEST.md`
  （TDC topic `29803.htm`，头文件 `MAPI/TestControl.h`）

**本页怎么读的这一篇**：`## Syntax`（九个语法族 + 16 行参数表）、`## Important points`（13 条）、`## Examples`（5 个）、`## Related information`（12 个目标）、`## Functional changes`（2 条）**全部读过**；上面的引文全部出自这几节，**没有一句来自本页 sources 之外**。

**本页没做的**：

- **没有读 [[testset]] 那篇（`02.07.04.01.244_TESTSET.md`）。** 所以「继任者到底怎么用」**本页一个字都没有**——本页只有「文档说该换它」这一句。
- **没有读 `Related information` 那 12 个目标里的任何一个**（`Alphabetical list of flags` / `Event Data Logging Concepts` / `Event Formatter` / `TESTSET` / `GET_FUNCTIONAL_RESULT()` / `FUNCTIONAL_TEST()` / `DIGITAL_CAPTURE_TEST` / `NB_DIGITAL_CAPTURE_START` / `PMU_VFIM` / `PMU_IFVM` / `DPS_VFIM` / `LIMIT`）。**它们的链接名本页照 raw 的写法写，内容的判断一概没有。**
- **没有读 `Tests` 页（`02.08.04.32.03.01.03`）**——`testname` 与那张限值表怎么对应，**本页不知道**。
- **没有开过图**：**这一篇的 raw（md 与上游 `raw/29803.htm`）里一张图都没有**——实测 `<img>` 0 个、`.png` 引用 0 个，**所以本页没有任何图证可写**。**不是「图够不着」**（`wiki/schema.md` §11.4 已更正那条错说法），**是这一篇里没有图**。
- **没有实跑**：没建过 test method、没跑过 testflow、没看过 report window 里 `unreliable` 的空白格长什么样。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/testmethod.md`。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**（raw 一个字节不动，§11.2）：

> ① **`allTEST` 少一个空格**：`Thus allTEST calls will be executed for the first site. regardless of their continue settings and return values.`——`all` 与 `TEST` 之间没有空格，且**这一句的句号后面又跟了一个小写开头的 `regardless`**（同一句里两处排版毛病，本页原样引）；

> ② **`the you` 多一个词**：`When the result of the first TEST is pass, the test will continue even if the you do not set the continue flag to TRUE.`（Example 2 的说明句）；

> ③ **`produce` 少了第三人称 s**：`the TEST API judges the last spec search test result and produce a data log event`（spec search 那一条）；

> ④ **参数表在 raw 里是被压平的**：`## Syntax` 下面那张表的每一格都单独成行、行间夹空行（本页 `语法 / 参数` 节里能看见这个形状）。**这是语料的形状，不是脚本切错**（§4）；本页按语义把它读成一张表。

> ⑤ **同一个参数两种大小写**：语法块里写 `INT hardbin = -1`（全小写），而参数表的行头与 `## Functional changes` 里都写 `hardBin`（大写 `B`）。**同一篇文档里两种写法并存**（`softBin` 反而前后一致，两处都是大写 `B`）。**本页一个都不改**，`语法 / 参数` 节保留脚本抽出来的 `hardbin`，本页散文里按参数表写 `hardBin`——**两个写法指的是同一个参数，这是本页的读法（推断），语料没有解释哪一个是正式的。**

**本页三类话的边界**（§11 的三分）：`文档事实` = 所有 `> 「…」` 引文，以及表里标了「原文」的格；`推断` = 正文里每一处标了（推断）的句子（**除这些以外本页没有别的主张**）；`建议` = **本页一句都没有**——**文档自己说的那句「recommended」本页只当文档事实转述，不算本页的建议。**

`verified: doc-only`
