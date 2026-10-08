---
type: object
title: Test Suite Control API
layer: L3
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Test Suite Control API

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **10,642 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.md>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.01.14.01_How_to_use_the_test_suite_control_API.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.01_TestsuiteProxy.attachTestmethod.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.02_TestsuiteProxy.executeActiveSites.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.03_TestsuiteProxy.executeSiteInFocus.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.04_TestsuiteProxy.getAnalogSet.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.05_TestsuiteProxy.getLevelEquation.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.06_TestsuiteProxy.getLevelSet.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.07_TestsuiteProxy.getLevelSpec.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.08_TestsuiteProxy.getName.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.09_TestsuiteProxy.getSequencerLabel.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.10_TestsuiteProxy.getSiteMatch.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.11_TestsuiteProxy.getTestmethodDefaultLimitNames.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.12_TestsuiteProxy.getTestmethodLimitValue.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.13_TestsuiteProxy.getTestmethodName.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.14_TestsuiteProxy.getTestmethodParameterNames.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.15_TestsuiteProxy.getTestmethodParameterValue.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.16_TestsuiteProxy.getTestmethodUserDefinedLimitNames.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.17_TestsuiteProxy.getTestsuiteFlag.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.18_TestsuiteProxy.getTimingEquation.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.19_TestsuiteProxy.getTimingSet.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.20_TestsuiteProxy.getTimingSpec.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.21_TestsuiteProxy.isExecuted.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.22_TestsuiteProxy.isMultiportTiming.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.23_TestsuiteProxy.isPass.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.24_TestsuiteProxy.setAnalogSet.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.25_TestsuiteProxy.setEquationBasedLevel.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.26_TestsuiteProxy.setEquationBasedTiming.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.27_TestsuiteProxy.setMultiportTiming.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.28_TestsuiteProxy.setName.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.29_TestsuiteProxy.setSequencerLabel.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.30_TestsuiteProxy.setSiteMatch.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.31_TestsuiteProxy.setTestmethodLimits.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.32_TestsuiteProxy.setTestmethodParameterValues.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.33_TestsuiteProxy.setTestsuiteFlag.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.02_detachSession.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.03_exitProcess.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.04_initializeSession.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.05_getTestsuite.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.06_getAllTestsuiteNames.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.07_getSpecialTestsuite.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.08_createFloatingTestsuite.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.09_deleteFloatingTestsuite.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.10_selectTestmethodExecutor.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.11_getTestmethodExecutorIndex.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.12_setSiteInFocus.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.13_getSiteInFocus.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.14_setActiveSites.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.15_getActiveSites.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples（取自子主题 How to use the test suite control API）

### Executing an existing test suite

The following example executes an existing test suite in the current test flow.

```
#include "testsuitecontrol_api.hpp"
#include <iostream>
#include <stdexcept>

using namespace std;
using namespace testsuitecontrol;

int main(int argc, char** argv)
{
int nRet = -1;

try
{
initializeSession();
TestsuiteProxy ts = getTestsuite("mysuite");
//execute it on site 1,3,5
set<int> sites;
sites.insert(1);
sites.insert(3);
sites.insert(5);
setActiveSites(sites);

ts.executeActiveSites();

for(set<int>::const_iterator it = sites.begin(); it != sites.end(); ++it)
{
int siteNum = *it;
if (ts.isPass(siteNum))
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": PASSED."<<endl;
}
else
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": FAILED."<<endl;
}
}
detachSession();
nRet = 0;
}
catch(runtime_error& error)
{
cerr<<error.what()<<endl;
}
return nRet;
}
```

### Create, Setup and execute a test suite

The following example creates a floating test suite, setup and execute the floating test suite.

```
#include "testsuitecontrol_api.hpp"
#include <iostream>
#include <stdexcept>

using namespace std;
using namespace testsuitecontrol;

int main(int argc, char** argv)
{
int nRet = -1;
try
{
//default session: the SmarTest session of the current display
//default UTM executor: the first one (i.e. TestMethodManager).
initializeSession();

TestsuiteProxy ts = createFloatingTestsuite("floating");
ts.attachTestmethod("ac_tml.AC_TEST.FunctionalTest");

//setup this testsuite
ts.setEquationBasedLevel("2","1","3");
ts.setEquationBasedTiming("3","2","2");
ts.setSequencerLabel("\"MATCH_LOOP\"");

//execute it on currently active site
ts.executeActiveSites();
set<int> sites = getActiveSites();
for(set<int>::const_iterator it = sites.begin(); it != sites.end(); ++it)
{
int siteNum = *it;
if (ts.isPass (siteNum))
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": PASS."<<endl;
}
else
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": FAILED."<<endl;
}
}
detachSession();
nRet = 0;
}
catch(runtime_error& error)
{
cerr<<error.what()<<endl;
}

return nRet;
}
```

### Delete a test suite

The following example deletes a floating test suite.

```
#include "testsuitecontrol_api.hpp"
#include <iostream>
#include <stdexcept>

using namespace std;
using namespace testsuitecontrol;

int main(int argc, char** argv)
{
int nRet = -1;
try
{
initializeSession();
bool isRemoved =deleteFloatingTestsuite("dummy");
if (isRemoved)
{
cout<<"\"dummy\" testsuite was removed: succeed."<<endl;
}
else
{
cout<<"\"dummy\" testsuite was removed: failed."<<endl;
}

detachSession();
nRet = 0;
}
catch(runtime_error& error)
{
cerr<<error.what()<<endl;
}

return nRet;

```

}

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.attachTestmethod）

```
bool attachTestmethod(const std::string& name);
```

Parameters
| name | The full name of the test method like "ac_tml.AcTest.FunctionalTest". |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.executeActiveSites）

```
void executeActiveSites();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.executeSiteInFocus）

```
void executeSiteInFocus();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getAnalogSet）

```
const std::string getAnalogSet();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getLevelEquation）

```
const std::string getLevelEquation ();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getLevelSet）

```
const std::string getLevelSet();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getLevelSpec）

```
const string getLevelSpec ();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getName）

```
const std::string getName();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getSequencerLabel）

```
const std::string getSequencerLabel();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getSiteMatch）

```
SiteMatchValue getSiteMatch();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTestmethodDefaultLimitNames）

```
const std::vector<std::string> getTestmethodDefaultLimitNames() const;
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTestmethodLimitValue）

```
const LimitValue getTestmethodLimitValue(const std::string& name) const;
```

Parameters
| name | The limit name to query. If the name is invalid, empty `LimitValue ` will be returned with an error message sent out. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTestmethodName）

```
const std::string getTestmethodName();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTestmethodParameterNames）

```
const std::vector<std::string> getTestmethodParameterNames();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTestmethodParameterValue）

```
const std::string getTestmethodParameterValue(const std::string& name) const;
```

Parameters
| name | The parameter to query. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTestmethodUserDefinedLimitNames）

```
const std::vector<std::string> getTestmethodUserDefinedLimitNames() const;
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTestsuiteFlag）

```
int getTestsuiteFlag(const TestsuiteFlag name) const;
```

Parameters
| name | The test suite flag to query. It can be one of the options of `TestsuiteFlag` enumeration as defined in the above table. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTimingEquation）

```
const std::string getTimingEquation();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTimingSet）

```
const std::string getTimingSet();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.getTimingSpec）

```
const std::string getTimingSpec();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.isExecuted）

```
bool isExecuted(const int site);
```

Parameters
| site | The site to query. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.isMultiportTiming）

```
bool isMultiportTiming();
```

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.isPass）

```
bool isPass(const int site) const;
```

Parameters
| site | The site to query. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setAnalogSet）

```
bool setAnalogSet(const std::string& setName);
```

Parameters
| value | The analog set. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setEquationBasedLevel）

```
bool setEquationBasedLevel(const std::string& levelEquation,
const std::string& levelSpec,
const std::string& levelSet);
```

Parameters
| levelEquation | The level equation. |
|---|---|
| levelSpec | The level spec. |
| levelSet | The level set. |

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setEquationBasedTiming）

```
bool setEquationBasedTiming(const std::string& timingEquation,
const std::string& timingSpec,
const std::string& timingSet);
```

Parameters
| timingEquation | The timing equation. |
|---|---|
| timingSpec | The timing spec. |
| timingSet | The timing set. |

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setMultiportTiming）

```
bool setMultiportTiming(const std::string& multiportSpec, const std::string& timingSet);
```

Parameters
| multiportSpec | The multi-port spec. |
|---|---|
| timingSet | The timing set. |

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setName）

```
bool setName(const std::string& name);
```

Parameters
| name | The test suite name. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setSequencerLabel）

```
bool setSequencerLabel(const std::string& value);
```

Parameters
| value | The sequencer label to use. It must be in the format of "\"label_name\"". |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setSiteMatch）

```
bool setSiteMatch(const SiteMatchValue value);
```

Parameters
| value | The site match value. It can be one of the options of SiteMatchValue enumeration defined below:<br><br>`enum SiteMatchValue`<br><br>`{`<br><br>`SITEMATCH_OFF = 0,`<br><br>`SITEMATCH_ON,`<br><br>`SITEMATCH_AUTO,`<br><br>`SITEMATCH_UNDEFINED`<br><br>`};` |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setTestmethodLimits）

```
void setTestmethodLimits(const LimitNameValueMap& userDefinedLimits,
const LimitNameValueMap& defaultLimits = LimitNameValueMap ());
```

Parameters
| userDefinedLimits | The name-value pair for limits defined in test method source code. If the name does not exist, the pair will be ignored and a warning message will be sent out. |
|---|---|
| defaultLimits | The name-value pair for limits defined in test method API, for example `"DEFAULT FUNCTIONAL TEST"`, `"DEFAULT GENERAL TEST"`, `"DEFAULT PMUTEST"`, `"DEFAULT DPS TEST"`, `"DEFAULT SPEC SEARCH"` and `"DEFAULT TIA TEST"`.<br><br>If the limit is not used in the test suite, it will be added. If the limit does not exist, it will be ignored and a warning message will be sent out. |

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setTestmethodParameterValues）

```
void setTestmethodParameterValues(const std::map<std::string, std::string>& params);
```

Parameters
| params | The name-value pair of the test method parameters. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › TestsuiteProxy › TestsuiteProxy.setTestsuiteFlag）

```
bool setTestsuiteFlag(const TestsuiteFlag name, const int value);
```

Parameters
| name | The test suite flag name. It can be one of the options of `TestsuiteFlag` enumeration defined below :<br><br>`enum TestsuiteFlag`<br><br>`{`<br><br>`TESTSUITEFLAG_BYPASS = 0,`<br><br>`TESTSUITEFLAG_SET_PASS,`<br><br>`TESTSUITEFLAG_SET_FAIL,`<br><br>`TESTSUITEFLAG_HOLD,`<br><br>`TESTSUITEFLAG_HOLD_ON_FAIL,`<br><br>`TESTSUITEFLAG_OUTPUT_ON_PASS,`<br><br>`TESTSUITEFLAG_OUTPUT_ON_FAIL,`<br><br>`TESTSUITEFLAG_VALUE_ON_PASS,`<br><br>`TESTSUITEFLAG_VALUE_ON_FAIL,`<br><br>`TESTSUITEFLAG_PER_PIN_ON_PASS,`<br><br>`TESTSUITEFLAG_PER_PIN_ON_FAIL,`<br><br>`TESTSUITEFLAG_SET_BREAK_POINT,`<br><br>`TESTSUITEFLAG_FORCE_SERIAL,`<br><br>`TESTSUITEFLAG_LOG_MX_WAVEFORMS,`<br><br>`TESTSUITEFLAG_FAIL_PER_LABEL,`<br><br>`TESTSUITEFLAG_FFC_ENABLE,`<br><br>`TESTSUITEFLAG_FFC_SCAN_INFO_ENABLE,`<br><br>`TESTSUITEFLAG_LOG_FIRST,`<br><br>`TESTSUITEFLAG_FFV_ENABLE,`<br><br>`TESTSUITEFLAG_FRG_ENABLE,`<br><br>`TESTSUITEFLAG_FRG_SINGLE_SHOT,`<br><br>`TESTSUITEFLAG_HW_DSP_DISABLE,`<br><br>`TESTSUITEFLAG_TEST_LEVEL,`<br><br>`TESTSUITEFLAG_UNDEFINED`<br><br>`};` |
|---|---|
| value | The value to set. It must be 0 or 1 except for TESTSUITEFLAG_LOG_FIRST and TESTSUITEFLAG_TEST_LEVEL. |

### Syntax（取自子主题 Test suite control API reference › detachSession）

```
void detachSession();
```

### Syntax（取自子主题 Test suite control API reference › exitProcess）

```
void exitProcess(const int exitCode);
```

Parameters
| I | exitCode | The exit code of the process. It has the same meaning with the parameter status of exit(). (Type `man 3 exit` in the shell to see the details.) |
|---|---|---|

```

```

### Syntax（取自子主题 Test suite control API reference › initializeSession）

```
void initializeSession(const std::string& sessionId = "",
const int testmethodExecutor = 1);
```

Parameters
| sesionId | The ID of the SmarTest session to work with. Default value is empty, which means the API will automatically gets the SmarTest session ID of the current display. |
|---|---|
| TestmethodExecutor | The test method executor to be used for execution. Default is the first one. |

### Syntax（取自子主题 Test suite control API reference › getTestsuite）

```
TestsuiteProxy getTestsuite(const std::string& name);
```

Parameters
| name | The test suite name. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › getAllTestsuiteNames）

```
const std::vector<std::string> getAllTestsuiteNames();
```

### Syntax（取自子主题 Test suite control API reference › getSpecialTestsuite）

```
TestsuiteProxy getSpecialTestsuite (const std::string& name);
```

Parameters
| name | The name of the special test suite. It can be "init", "abort", "download", "pause", "reset", "exit", or "bin_disconnect". |
|---|---|

### Syntax（取自子主题 Test suite control API reference › createFloatingTestsuite）

```
TestsuiteProxy createFloatingTestsuite(const std::string& testsuiteName);
```

Parameters
| testsuiteName | The test suite name. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › deleteFloatingTestsuite）

```
bool deleteFloatingTestsuite(const std::string& name);
```

Parameters
| name | The test suite to delete. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › selectTestmethodExecutor）

```
bool selectTestmethodExecutor( const int executor);
```

Parameters
| executor | The index number of the UTM executor to use. It can be:<br><br>1: the first executor for production execution.<br><br>2: the second executor for debug purpose and non-production execution. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › getTestmethodExecutorIndex）

```
int getTestmethodExecutorIndex();
```

### Syntax（取自子主题 Test suite control API reference › setSiteInFocus）

```
void setSiteInFocus(const int site);
```

Parameters
| site | The site to set in focus. |
|---|---|

### Syntax（取自子主题 Test suite control API reference › getSiteInFocus）

```
int getSiteInFocus();
```

### Syntax（取自子主题 Test suite control API reference › setActiveSites）

```
void setActiveSites(const std::set<int>& sites);
```

Parameters
| sites | The site number stored in `set<int>`. |
|---|---|

### Example（取自子主题 Test suite control API reference › setActiveSites）

```
set<int> sites;
sites.insert(1);
sites.insert(3);
setActiveSites(sites);
```

In this example, site 1 and 3 are set to active.

### Syntax（取自子主题 Test suite control API reference › getActiveSites）

```
const std::set<int> getActiveSites();
```

### Example（取自子主题 Test suite control API reference › getActiveSites）

The following example executes the test suite `mysuite` and print the test result of each active site.

```
TestsuiteProxy ts = getTestsuite("mysuite");
ts.executeActiveSites();
set<int> sites = getActiveSites();
for(set<int>::const_iterator it = sites.begin(); it != sites.end(); ++it)
{
  int siteNum = *it;
  if (ts.isPass (siteNum))
  {
    cout<<"\"mysuite\" was executed on site"<<siteNum<<": PASS."<<endl;
  }
  else
  {
    cout<<"\"mysuite\" was executed on site"<<siteNum<<": FAILED."<<endl;
  }
}
```

<!-- 语法节 end -->

## 是什么

> **一句话**：**在 testflow 工具之外，直接控制 test suite 的一套 API。**原文：
> *"Test suite control API is used to directly control the test suites **outside of the testflow tool**.
> Only **UTM-based** test suites are supported with these APIs."*

**三个限制是硬性的，原文写明，本页照录：**

1. **只支持 UTM-based 的 test suite**。
2. **不能在 test method 编程里用**（*"They cannot be used in test method programming"*）——
   也就是说它**不是** [[testmethod]] 阶段能用的东西。
3. **不能与 HVM API、BLC API 被同一个 client 进程并行使用**
   （*"also cannot be used in parallel with HVM API and BLC API by the same client process"*）。

**还有一条方向相反的警告**（原文的 `Note`，很容易被忽略）：

> The actions in the testflow tool like creating a test suite, deleting a test suite, changing the
> test suite setup and changing testflow, will impact the behavior of the running test suite control
> API. And the behaviors of the running test suite control API like creating a test suite, deleting a
> test suite and changing the test suite setup, will be reflected in the testflow tool.
> **Running test suite control API interactively with testflow UI tool is NOT recommended.**

**双向影响**：GUI 上的动作会打到正在跑的 API，API 的动作也会反映到 GUI；
**原文明确不建议一边开着 testflow UI 一边交互式地跑这个 API**。

**它的形状分两块**（`02.09.01.14` 全章 **51 篇**）：

| 块 | 分类号 | 内容 |
|---|---|---|
| 怎么用 | `02.09.01.14.01` | C++ 客户端程序的编译、链接、执行（见「典型用法」） |
| 参考 | `02.09.01.14.02` | **1 个句柄 + 33 个成员 + 14 个会话级函数**，每个成员一篇 |

**句柄是 `TestsuiteProxy`**，**会话级函数是平铺的**（`initializeSession()` / `getTestsuite()` /
`setActiveSites()` …）——**两级**：先开会话拿到句柄，再在句柄上设参数、执行、查结果。

### 33 个成员**天然按 stage 分组**（这是文档自己的组织方式，不是我的归纳）

> 这条对应关系由 `schema.md` §3 记录，**是九个 stage 页写 L3 那一节的依据**：
> 读者想找「本阶段能从这个 API 里拿到什么」，查这张表就行。

| stage | `TestsuiteProxy` 成员 |
|---|---|
| `level` | `TestsuiteProxy.getAnalogSet()`、`TestsuiteProxy.getLevelEquation()`、`TestsuiteProxy.getLevelSet()`、`TestsuiteProxy.getLevelSpec()`、`TestsuiteProxy.setAnalogSet()`、`TestsuiteProxy.setEquationBasedLevel()` |
| `timing` | `TestsuiteProxy.getTimingEquation()`、`TestsuiteProxy.getTimingSet()`、`TestsuiteProxy.getTimingSpec()`、`TestsuiteProxy.isMultiportTiming()`、`TestsuiteProxy.setEquationBasedTiming()`、`TestsuiteProxy.setMultiportTiming()` |
| `testmethod` | `TestsuiteProxy.attachTestmethod()`、`TestsuiteProxy.getTestmethodDefaultLimitNames()`、`TestsuiteProxy.getTestmethodLimitValue()`、`TestsuiteProxy.getTestmethodName()`、`TestsuiteProxy.getTestmethodParameterNames()`、`TestsuiteProxy.getTestmethodParameterValue()`、`TestsuiteProxy.getTestmethodUserDefinedLimitNames()`、`TestsuiteProxy.setTestmethodLimits()`、`TestsuiteProxy.setTestmethodParameterValues()` |
| `pattern` | `TestsuiteProxy.getSequencerLabel()`、`TestsuiteProxy.setSequencerLabel()` |
| `testflow` | `TestsuiteProxy.getTestsuiteFlag()`、`TestsuiteProxy.setTestsuiteFlag()` |
| `run / results（两段共用）` | `TestsuiteProxy.executeActiveSites()`、`TestsuiteProxy.executeSiteInFocus()`、`TestsuiteProxy.getName()`、`TestsuiteProxy.getSiteMatch()`、`TestsuiteProxy.isExecuted()`、`TestsuiteProxy.isPass()`、`TestsuiteProxy.setName()`、`TestsuiteProxy.setSiteMatch()` |

**另有 14 个会话级函数**（`02.09.01.14.02.02`–`.15`，**不属于任何 stage，是横切的**）：
`detachSession()`、`exitProcess()`、`initializeSession()`、`getTestsuite()`、
`getAllTestsuiteNames()`、`getSpecialTestsuite()`、`createFloatingTestsuite()`、
`deleteFloatingTestsuite()`、`selectTestmethodExecutor()`、`getTestmethodExecutorIndex()`、
`setSiteInFocus()`、`getSiteInFocus()`、`setActiveSites()`、`getActiveSites()`。

> **注意 `setSiteInFocus()` / `setActiveSites()` 在两边都出现**（会话级 14 个里有，
> `TestsuiteProxy` 的横切成员里也有）——**同名不同级**：一个作用于会话，一个作用于句柄。
> 原文分两篇写（`.02.12` 与 `.02.01` 系），**别以为重复**。

## 典型用法

**这不是「配一下就能用」的东西，是「写一个 C++ 程序去控制测试机」。**
原文的四步（`02.09.01.14.01`），**照抄命令**：

1. **写一个 C++ 程序**：include 头文件，用命名空间。

```cpp
#include "testsuitecontrol_api.hpp"
using namespace testsuitecontrol;
```

2. **在 run shell 里编译它**（原文：*"You must build your program from within the run shell"*）。

```
$/opt/hp93000/soc/system/bin/run -S
```

3. **编译 + 链接**（32 位示例；64 位把 `-m32` 换成 `-m64` 或整个去掉）：

```
g++ -I/opt/hp93000/soc/prod_com/include/ -m32 -c -o main.o main.cpp
g++ -m32 -L /opt/hp93000/soc/prod_com/sh_lib/ -Wl,-rpath /opt/hp93000/soc/prod_com/sh_lib/ -ltestsuitecontrol_api -o t1.exe. main.o
```

> ⚠️ 第二行的 `t1.exe.` **后面那个句点是原文自带的**（`02.09.01.14.01` 的
> `Link options` 段），**照录不改**（§11）。本页初版把它**悄悄去掉了**——
> 那是我改写了文档事实，已按原文改回（2026-09-18）。
> 照着敲的时候该不该带这个点，**文档没说**，本页不替它决定。

> ⚠️ **另有一套 Red Hat 3 专用的选项**（原文单独列了），多带
> `-I /opt/openoffice.org/OpenOffice2.0_SDK/include/stl/` 与
> `-DGXX_INCLUDE_PATH=/usr/include/c++/3.2.3/`。
> **那是很老的系统**（编译器 3.2.3、OpenOffice 2.0 SDK），
> **在本 wiki 面向的 7.10.3 环境上还要不要这一套，文档没说——本次未查。**

4. **执行**：

```
/opt/hp93000/soc/system/bin/run -x user_executable_program
```

**三个完整例子在语法节末尾**（段名 `Examples（取自子主题 How to use the test suite control API）`）：
① 执行一个已有的 test suite；② 建一个 floating test suite、配好、执行；③ 删掉一个 floating test suite。

> **这三个例子是补进来的**（2026-09-18）：它们住在 `.14.01` 的 `## Examples` 底下，
> 而抽取器**当时不认这种形状**——`## Examples` 开段、`### 子标题` 立刻把它关掉，
> 正文全丢。本页初稿因此写了一句**假的**「三个完整例子已随语法节逐字抽进本页」：
> **页面里一个都没有。** 改成「抽取器只认 `## Syntax` / `### Example`」之后
> 才真的抽进来。**修的是脚本，不是这句话。**（详见 `objpack.verbatim_sections` 的注释）

**前两个例子共用同一个骨架，这就是标准用法**：

```
initializeSession();
... getTestsuite(...) / createFloatingTestsuite(...)
... ts.setEquationBasedLevel(...) / setSequencerLabel(...) / attachTestmethod(...)
... setActiveSites(...); ts.executeActiveSites();
for (每个 site) ts.isPass(siteNum)
detachSession();
```

**第三个例子是例外**：它只 `initializeSession()` → `deleteFloatingTestsuite("dummy")` →
`detachSession()`，**不执行任何 test suite、不取 `isPass()`**——删一个 suite 不需要跑它。

**三点**：① 全程包在 `try { } catch(runtime_error& error)` 里，错误走 `what()`；
② **`isPass()` 是逐站点的**——多站点场景要按 site 循环取，不是一次拿总判定；
③ ⚠️ **第三个例子的代码围栏在原文里就提前闭合了**——`return nRet;` 还在围栏内，
**`main()` 的最后一个 `}` 落在围栏外**，在页面里显示为围栏后孤零零一个 `}`。
**这是原文自带的**（`02.09.01.14.01` L206/208），不是本页转录错。

## 和谁有关

**它是一个「横切入口」，八个 stage 页都伸手要它：**

| 口径 | 数 |
|---|---|
| **本 wiki 内的引用** | **8 处 / 8 个 stage 页**（level、pattern、pin、project、results、run、testmethod、timing 各 1） |
| **语料内指向根文档的边** | **1 条 inline**（来自父章）+ 1 条 `toc`（章节目录） |
| **语料内指向本章任意一篇的边** | **144 条 / 20 篇** |

**和 [[tpi-program-routines]] 一样：「建这一页的理由」是第三种——八个 stage 页已经伸手要它**
（九个 stage 页里，除 [[testflow]] 外都引了它）。根文档在语料里几乎没人直接引（1 条），
而 wiki 里被引 8 处。**是 wiki 自己要它，不是语料在要它。**

**两页是一对，读者要一起看**：

| | 本页 | [[tpi-program-routines]] |
|---|---|---|
| 层级 | `L3`（原文：outside of the testflow tool） | `L3`（原文：attach to SmarTest process） |
| 形状 | **句柄 + 方法**（`TestsuiteProxy`） | **平铺的 C 函数** |
| 语言 | C++（`testsuitecontrol_api.hpp`） | C（`tpi_c.h`） |
| **怎么起** | `run -S` 进 run shell 里编译，`run -x <program>` 执行 | `run -S` 起 supervisor mode，交 `run_supervisor` 启动 |
| **文档怎么称呼这个模式** | **run shell** | **supervisor mode**（同一个 `-S` 开关） |
| 会话骨架 | `initializeSession()` / `detachSession()` | `HpInit()` / `HpTerm()` |
| **重叠的名字** | `setSiteInFocus()`、`setActiveSites()` | `SetSiteInFocus`、`SetActiveSites` |
| **能否共存** | **不能与 HVM API / BLC API 同一 client 进程并行** | 文档未说；**没说就是没说**（§4） |

**[[run]] 页把它列为自己的 L3 第 2 项**，给了完整的能力清单
（attach 到会话与 testflow、读写 test suite 的设置与标志、挂 UTM、
建/配/执行/删 floating test suite、按 focus site 或 active sites 执行并查状态）。

**这是一条 `constraint` 页的种子**（本 wiki 暂无该类页）：「test method 编程里不能用」
+「不能与 HVM/BLC 并行」+「不建议与 testflow UI 交互式同用」——**三条都是使用前必须知道的前提**。
**本页先记在这儿，等 `constraint` 类型开建时再移过去。**

**不链的**：33 个成员 + 14 个会话级函数**一个都没建页**，也不在任何可建页清单里，
按 §9.1 写成反引号。**它们的签名与参数已经在上面语法节里逐字抽进来了**（47 个 `## Syntax`）。

## 版本

- **Introduced in SmarTest 6.5.2**（本 wiki 面向 7.10.3，**可用**）
- **SmarTest 6.5.3**：新增 `detachSession()`；**移除了 `terminateSession()`**
- **SmarTest 7.3.2**：Added run shell guidance（即「必须在 run shell 里编译」那一段）

> **第二条对读老代码有用**：7.10.3 里**没有** `terminateSession()`，
> 对应的是 `detachSession()`。看到老例子里写 `terminateSession()`，
> **那是 6.5.2 的写法，在 7.10.3 上编译不过**。

## 出处

- 定义文档：`02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.md`
  （TDC `111196.htm`）
- 全章 **51 篇**（`02.09.01.14` + `.01`、`.02` 及其下 **48 篇**成员/函数）
- **语法节逐字取自 48 篇**（**段正文合计 10,401 字符**；页面里这一节共 **20,593 字符**——
  两个数都对，只是量的东西不同）——**取自孙辈**：
  定义文档自己、`.14.01`、`.14.02`、`.14.02.01` **都没有 `## Syntax`**，
  语法在 `.14.02.01.01`–`.33`（`TestsuiteProxy` 成员）和 `.14.02.02`–`.15`（会话级函数）里。
  **抽取器为此加了「在声明的 `Subtopics` 树里递归」，最多 3 层**（`objpack.SUBTREE_MAX`）——
  这一页就是那个改动的原因，**上一版它的语法节是空的**。
- **`.14.01` 那一篇是第二次栽在抽取器上**（2026-09-18 修）。它没有 `## Syntax`，
  但有 **`## Examples` + 三个 `### 子标题`**——而抽取器的状态机**遇到子标题就把段关掉**，
  于是那 2,714 字符（`段正文`）**一直在，一直没被收**。实测全语料
  **229 篇 / +427,979 字符**受此影响，**减少 0**（新逻辑是严格超集）。
  修完之后本页的段数 **49 → 50**、来源 **47 → 48 篇**。
  **教训与第一次同形：抽取器声称收 `example`（`SEC_HEADS` 里有），实际只收
  「H2 底下、第一个 H3 之前」那几行。范围比自称的窄，而窄掉的那块是绿的。**
- **wiki 内引用 8 处 / 8 页**；**语料内根文档入边 1 条 inline**（见上表）
- `layer: L3` **是文档事实**：原文自述 *"outside of the testflow tool"*。
  `schema.md` §3 原把 L3 枚举成 Test suite control API + HVM API 两个入口——
  **那份枚举漏了 [[tpi-program-routines]] 的 31 篇**，2026-09-18 已改正（67 → 98 篇）。
- `stage: run` 填的是**「最近的一段」，不是「归属」**（§6）。§6 给的判据是
  **「读者该去哪一段里找它的用法」**，按这个判据填 [[run]]：
  ①**三个官方例子里有两个以执行为结尾**——执行已有 test suite、建 floating test suite→配→执行，
  这两个都按 site 循环取 `isPass()`；第三个是**删**一个 suite，**不执行也不取判定**。
  （**初稿在这里写过「三个都以执行为结尾」，与它自己括号里的「删」矛盾，已改**。
  这一条不影响判 [[run]]：两条执行例 + ②③ 够判。）
  ②[[run]] 页里有这一族**完整的能力清单**，是全 wiki 唯一给出它的地方——
  读者实际的去处就是它；
  ③33 个成员里最大的一组是 run/results 共用（8 个）。
  **本页横切八个 stage，`stage` 字段只能填一个，承载不了这个事实**，所以写在这里。
- 本页 `verified: doc-only`。**参数表在语料里已被转换拆散**（实测 **100 处**孤立 `|` 行），
  内容不缺、形状缺，**原样保留不回填**（理由同 [[tpi-program-routines]]）。
- **一处语料格式异常，记录在此**：`TestsuiteProxy.getTimingSpec ()` ——
  **括号前多一个空格**，是 33 个成员里唯一一个这么写的。
  脚本按「0–1 个空格」宽容匹配所以收全了 33 个；
  **但按字面写链接会指向一个不存在的文件名**，所以本页按标准拼写写、不照抄那处异常。
