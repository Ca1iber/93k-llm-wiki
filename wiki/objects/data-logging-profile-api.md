---
type: object
title: Data logging profile API
layer: n/a
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.02.08_Data_logging_profile_API.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Data logging profile API

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,362 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.02.08_Data_logging_profile_API.md>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.01.02.08.01_ProfileMgr_class.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.08.02_Profile_class.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.08.03_Rule_class.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.08.04_Property_class.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.08.05_Data_logging_profile_API_examples.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 ProfileMgr class）

See `Data logging profile API examples`（raw: `../02.07_Test_Method_Reference/02.07.04.01.169.05_Data_logging_profile_API_examples.md`）

### Example（取自子主题 Profile class）

See `Data logging profile API examples`（raw: `../02.07_Test_Method_Reference/02.07.04.01.169.05_Data_logging_profile_API_examples.md`）

### Example（取自子主题 Rule class）

See `Data logging profile API examples`（raw: `../02.07_Test_Method_Reference/02.07.04.01.169.05_Data_logging_profile_API_examples.md`）

### Example（取自子主题 Property class）

See `Data logging profile API examples`（raw: `../02.07_Test_Method_Reference/02.07.04.01.169.05_Data_logging_profile_API_examples.md`）

### Examples（取自子主题 Data logging profile API examples）

### Profile creation

```
// ProfileCreation.cpp
#include "tml_base.h"
extern CComModule _Module;
#include "tml_tcom.h"
#include "ProfileCreation.h"
#include "ProfileMgr.hpp"
#include "tpi_c.h" // TPI lib for GetCurrentDevice()
#include <stdio.h>
#if __GNUC__ >= 3
using namespace std;
#endif

#define PROFILE_FILENAME "ProfileTest.prf"

// This method creates and saves a sample profile programmatically.
// The profile is saved to the "profiles" subdir of the current device.

HRESULT CProfileCreation::createProfile(double _results[4])
{
    ProfileMgr* mgr = ProfileMgr::getInstance();

    // Create a profile and add sample rules to it:
    Profile* profile = mgr->createProfile(WildcardProfileType);

    // Test suite selector: AC test suites will log P/F results per pin:
    profile->createRule("ts:AC* . * . * . datalog_level = 3");
    profile->createRule("ts:AC* . * . * . datalog_detail = 1");

    // Test method selector for a custom property: logHistogram
    profile->createRule("* . evaluate* . * . logHistogram = 1");

    // Test name selector: The "shortsTest" will log per pin values:
    profile->createRule("* . * . name:shortsTest . datalog_level = 3");
    profile->createRule("* . * . name:shortsTest . datalog_detail = 2");

    // Test num selector: Log as much info as possible for test #'s 70-80:
    profile->createRule("* . * . tn:70-80 . datalog_level = 3");
    profile->createRule("* . * . tn:70-80 . datalog_detail = 5");

    // For all other tests (*.*.*) that Do not match one of the
    // above, use the following rules:
    profile->createRule("* . * . * . datalog_level = 3");
    profile->createRule("* . * . * . datalog_detail = 0");

    // Build the filename to save:
    char deviceStr[DM_MAX_DEVICE];
    GetDevPath(deviceStr);
    char filename[DM_MAX_DEVICE + 10 + DM_MAX_FILE + 1];
    sprintf(filename, "%s/profiles/%s", deviceStr, PROFILE_FILENAME);

    // Save the profile:
    profile->save(filename);

    return S_OK;
}
```

### Adaptive sampling

```
// SetProfile.cpp
#include "tml_base.h"
extern CComModule _Module;
#include "tml_tcom.h"
#include "SetProfile.h"
#include "ProfileMgr.hpp"
#include "tpi_c.h" // TPI lib for GetCurrentDevice()
#if __GNUC__ >= 3
using namespace std;
#endif
#define SAMPLING_ON_FILENAME        "datalog_ON.prf"
#define SAMPLING_OFF_FILENAME      "datalog_OFF.prf"
#define SAMPLE_SIZE                              100
static int          executionCount = 0;
static bool         initialized = false;
static ProfileMgr*  mgr = 0;
static Profile*     samplingOnProfile = 0;
static Profile*     samplingOffProfile = 0;

// This method shows an example of how to implement
// adaptive sampling based on an execution count
// approach. Data is only logged for every Nth device.
// Ideally, this method is called from a test suite at
// the start of a testflow.

HRESULT CSetProfile::setProfile(double _results[4])
{
    // Initialize the profiles:
    if (!initialized)
    {
      double results[4];
      init(results);
    }

    // Only log detailed results for the Nth device:
    if ((executionCount % SAMPLE_SIZE) == 0)
    {
        mgr->activateProfile(samplingOnProfile);
    }
    else
    {
        mgr->activateProfile(samplingOffProfile);
    }

    // Increment the testflow execution count:
    executionCount++;

    return S_OK;
}

// Initialization routine that is called only once

HRESULT CSetProfile::init(double _results[4])
{
    mgr = ProfileMgr::getInstance();

    // Build the filename to save:
    char deviceStr[DM_MAX_DEVICE];
    GetDevPath(deviceStr);
    char filename[DM_MAX_DEVICE + 10 + DM_MAX_FILE + 1];

    sprintf(filename, "%s/profiles/%s", deviceStr, SAMPLING_ON_FILENAME);
    samplingOnProfile = mgr->createProfile(filename);

    sprintf(filename, "%s/profiles/%s", deviceStr, SAMPLING_OFF_FILENAME);
    samplingOffProfile = mgr->createProfile(filename);

    initialized = true;

    return S_OK;
}
```

### Logging by test number

```
// EdlFfcDatalog.cpp
#include "tml_base.h"
extern CComModule _Module;
#include "tml_tcom.h"
#include "EdlFfcDatalog.h"
#include "ProfileMgr.hpp"
#include "tpi_c.h" // TPI lib for GetCurrentDevice()
#if __GNUC__ >= 3
using namespace std;
#endif
#define PROFILE_FILENAME "EdlFfcDatalog.prf"

// Here is an example on how to give a test number to your
// test using the TESTSET API, which will be used by the
// profile rule engine to determine if test number specific
// logging is desired or not.

HRESULT CEdlFfcDatalog::execute(double _results[4])
{
    if (profile)
    {
      TESTSET set;
      set.testname("EdlFfcDatalog");
      set.testnumber(900);

      FUNCTIONAL_TEST();

      // Note: Here we are calling judgeAndLog on the object 'set',
      // which is associated with the test name "EdlFfcDatalog" and
      // the test number 900.  This information is applied by
      // judgeAndLog to the active profile to determine if logging
      // should be performed.
      set.judgeAndLog_FunctionalTest();
    }
    return S_OK;
}
```

### Evaluating a custom property

```
// PropEvalBin.cpp
#include "tml_base.h"
extern CComModule _Module;
#include "tml_tcom.h"
#include "PropEvalBin.h"
#include "Property.hpp"
#if __GNUC__ >= 3
using namespace std;
#endif

// Here is a simple example of how to evaluate the value of
// a custom property based on the current execution context.
// If the profile defines the "logHistogram" property in this
// execution context, the specified rule value is returned.
// Otherwise, 0.

HRESULT CPropEvalBin::logHistogram(double _results[4])
{
    Property logHistogram("logHistogram");

    // Note that the following "if" call causes the profile rule engine
    // to calculate the propery's value based on the current execution
    // context:

    if (logHistogram)
    {
        drawHistogram();
    }
    return S_OK;
}
```

<!-- 语法节 end -->

## 是什么

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
