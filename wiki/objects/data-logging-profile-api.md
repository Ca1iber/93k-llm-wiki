---
type: object
title: Data logging profile API
layer: n/a
stage: results
tags: [data-logging-profile-api, data-logging, profile, api, rule, property, results, testmethod]
related: [data-logging-profiles, results, testmethod, testset, execution-context, device-directory, flag, smartest-7.4.5]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.02.08_Data_logging_profile_API.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Data logging profile API

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

**Data logging profile API 是「数据记录 profile」的 C++ 编程接口。**
profile 本身是一组「记什么、怎么记」的规则（那一侧见 [[data-logging-profiles]]）；
本页是**在 test method 里用代码把它建出来、灌上规则、存进文件、激活、以及从里面读属性值**的那一侧。

原文的定义句（逐字；段内链接已按 §11.1 ② 剥掉 markdown 链接标记）：

> 「With the data logging profile API you can create and handle data logging profile and their
> rules and properties. It consists of the following classes:」

⚠️ **`data logging profile and their rules` 里的 `profile` 是单数，原文如此**（见 `## 出处` ①）。

**它由四个类组成**，原文紧随那两行之后的四条链接逐字是：
`ProfileMgr class` / `Profile class` / `Rule class` / `Property class`。

### 对象模型：三层的「零到多个」

原文把四个类的关系单独起了一句（`The classes model the various profile-related objects and their relationships:`），底下三条逐字：

> 「- The ProfileMgr instance contains zero or more Profile instances.」

> 「- A Profile instance contains zero or more Rule instances.」

> 「- A Rule instance contains a logging definition in the form of a string, such as "*leakage*.*.*.datalog_detail=2"」

| 层 | 装什么 | 原文的量化词 |
|---|---|---|
| `ProfileMgr` | `Profile` | `zero or more` |
| `Profile` | `Rule` | `zero or more` |
| `Rule` | 一条「字符串形式的记录定义」，例 `"*leakage*.*.*.datalog_detail=2"` | —— |

**最上面那一层是单例**，原文逐字：`There is just one ProfileMgr object that serves as the repository for all profiles.`

### 四个类各干什么（逐个）

#### `ProfileMgr`：单例仓库 + 五个动作

> 「With the ProfileMgr (profile manager) class, you can create, activate, load, save, and delete
> data logging profiles. There is just one ProfileMgr object that serves as the repository for all
> profiles.」

**五个动作**：create / activate / load / save / delete。

**入口是 `getInstance()`，而且原文说「应该先调它」**：

> 「The ProfileMgr interface provides an access method to obtain the singleton instance
> `getInstance()` which should be called first:」

```
ProfileMgr* mgr = ProfileMgr::getInstance();
```

**用完可以释放——是 `optionally`，不是必须**：

> 「The instance can optionally be freed at anytime with a call to `freeInstance()`.」

⚠️ 本页后文 `activateProfile` 那两段代码里用的是 **`profileMgr->`**，不是这里定义的 **`mgr`**——
同一个对象在同一篇文档里出现了两个名字，见 `## 出处` ⑥。

#### `Profile`：一个 profile 的建 / 载 / 存 / 改规则

> 「The Profile class encapsulates the core functionality that is associated with a data logging
> profile, such as creating, loading, saving, and manipulating rules that are part of the profile」

（**这句原文结尾没有句号**，见 `## 出处` ②。）

**两种建法：**

| 建法 | 代码（逐字） | 原文的说明 |
|---|---|---|
| 建空 profile | `Profile* profile = mgr->createProfile(WildcardProfileType);` | `A typical starting point is to create a profile via the following call:` |
| 从已有文件建 | `Profile* profile = mgr->createProfile(<filename>);` | `a profile can be created and automatically populated when a profile already exists on the file system` |

**类型只能用 `WildcardProfileType`**——这是这一节里唯一一条 `Always`：

> 「Always use the `WildcardProfileType`. The only other option, `ProdSettingProfileType`, is used
> internally by SmarTest for compatibility with the production settings feature.」

**灌规则用 `createRule()` 直接传字符串。** 原文举了三句，并说这三句合起来**就是出厂默认 profile `datalog_ON.prf` 的内容**：

> 「For example, the following three calls together create the content of the default data logging
> profile `datalog_ON.prf`:」

```
profile->createRule("*.*.*.log_events_enable=1");
profile->createRule("*.*.*.datalog_level=3");
profile->createRule("*.*.*.datalog_detail=2");
```

**这三句是本页与 [[data-logging-profiles]] 的交汇点**：那一页说 `datalog_ON.prf` 是出厂随 SmarTest 带的两个 profile 之一；
本页给出的，是**它的内容是怎么被写进去的**。

#### `Rule`：一条规则 = 上下文 + 属性名 + 属性值

> 「The Rule class is an abstract interface that contains all of the variables and methods
> necessary to store and manipulate the content of a general property rule, such as the context
> information, the property name, and its value.」

**规则字符串自己的语法不在本篇**，原文把它推给了另一篇：

> 「The rule string passed to the constructor is described in `Data logging profile rule syntax`.」

**那一句在原文里末尾是一个链接，目标是 `<02.10.01.02.06.03_Data_logging_profile_rule_syntax.md>`。**
（**那一篇本页没读**——所以「一条规则字符串怎么写」本页答不了。）

**也可以建一条空规则、再逐个 `set`**：

> 「An empty rule can be created and then populated by calling the set methods offered by the Rule
> class one by one:」

```
Rule* rule = profile->createRule();
rule->setTestSuite("*leakage*");
rule->setTestMethod("*");
rule->setTestName("*");
rule->setPropName("per_pin_on_fail");
rule->setPropValue(1);
```

**五个 `set` 正好对应上面那句里的三块**：`setTestSuite` + `setTestMethod` + `setTestName` 是**上下文**，
`setPropName` + `setPropValue` 是**那一对名值**。

**取用是对称的**，原文：

> 「The Rule class also includes corresponding get methods for the categories listed above (for example, `getTestSuite()`).」

#### `Property`：在 test method 里问「这一项现在记不记」

这是四个类里唯一**运行期读**的一个。原文两句：

> 「The Property class is used by the test methods to determine the value of a particular data
> logging property within the current execution context. The property instance determines its
> value by first obtaining the active profile and then by querying the value of the property
> within that profile.」

**第二句就是机制**：一个 Property 的值 = **先取当前 active 的 profile，再在那个 profile 里查这个属性**。
**它自己不带存储**——它是一层查询。（那个坐标 `current execution context` 见 [[execution-context]]，**那一页本页没读**。）

**两种读法**，原文各给一段代码：

| 读法 | 代码（逐字） |
|---|---|
| 静态便利方法 | `int datalog_detail = Property::value("datalog_detail");` |
| 建对象、当整数用 | `Property datalog_detail("datalog_detail");` |

第一段的引导句逐字是：`The value of a property can be obtained directly using the static value() convenience method of the class:`（原文 `value()` 带反引号，此处按 §11.1 ③ 去掉）。
第二段后面原文补了一句：

> 「Notice that, in the second case, the Property's int cast operator maps to the `value()` method,
> allowing you to treat the Property object as an integer.」

⚠️ 建对象那一段的引导句里 **`can be obtained` 出现了两次**，见 `## 出处` ③。

**属性分两种**，原文：

> 「There are predefined system properties, and you can define your own user defined properties.
> For a description of the predefined system properties see `Data logging profile rule syntax`.」

（**那一句里的链接目标同上**，也是 `02.10.01.02.06.03_Data_logging_profile_rule_syntax.md`。）
**即：预定义属性清单也在那一篇里，本篇不给。**（那篇本页没读。）

### 改 / 遍历一个 profile 里已有的规则

| 要做的 | 用什么 | 原文（逐字；按 §11.1 ③ 去掉了反引号） |
|---|---|---|
| 遍历全部规则 | `getRuleCount()` + `getRule(i)` | The individual rules in a profile can be accessed using the getRule() method. This can also be done using a for loop: |
| 覆盖某一位置的规则 | `setRule(i, rule)` | The rule content of a particular position can be overwritten using a call to setRule(i, rule); |

⚠️ 上面第二句原文**以分号结尾**（同段其余句子都是句号），见 `## 出处` ④。

遍历那段的代码里有两行**各自只有一个 `.`**：

```
for (int i=0; i<profile->getRuleCount(); i++)
{
Rule* rule = profile->getRule(i);
.
.
}
```

**那两个 `.` 是语料自带的省略记号**，不是本页写上去的省略号——这正是 §11.1 说的
「引文里的省略号只许出现在原文自己就有的地方」的那种地方，见 `## 出处` ⑦。

### 「在内存里」和「在文件系统上」是两件事（**本页最要紧的一条**）

原文把它写成单独一段，而且是这一节的转折点：

> 「At this point, the profile and its rules are stored in memory, but are not yet visible to other
> processes via the file system. To save the content of the profile to the file system, call the
> `save` method:」

**即：`createProfile()` + `createRule()` 做完之后，profile 只在内存里，别的进程（包括 SmarTest 自己）看不见它。**
要让它可见，必须 `save`：

```
profile->save(<filename>);
```

**存到哪也有讲究**：

> 「Ideally, the file name indicates the name of the device and the profiles subdirectory to make
> sure the profile is visible to SmarTest.」

**`the profiles subdirectory` 具体是什么形态，本篇正文没说。** [[data-logging-profiles]] 那页从它自己的 raw 里
引出的形态是 `<device directory>/profiles/`（**那一页本页读过**）；本页 `## 语法 / 参数` 节里的例子代码
写的是 `sprintf(filename, "%s/profiles/%s", deviceStr, PROFILE_FILENAME);`——
**两处指的是同一个位置（推断）**，依据是两处的路径末段都是 `profiles/`、且都挂在设备目录下。
**本篇正文没有写这个路径。**（[[device-directory]] 是那个「设备目录」。）

**存完才谈「激活」**：

> 「After a profile has been saved, it can be activated, which means the rules in the profile apply
> to the next test execution. This is done by calling the `activateProfile` method:」

**`apply to the next test execution` 这句要读准：激活不是立刻生效，是对下一次执行生效。**

**激活可以给对象、也可以给文件名**（原文 `Alternatively, the file name can be specified instead of the profile instance:`）：

```
profileMgr->activateProfile(profile);
profileMgr->activateProfile(<filename>);
```

**一句话收束：`save` 管「别人看不看得见」，`activate` 管「下一次跑用不用它」。**

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有一条命令行。**
能落成步骤的只有原文那几段代码本身。**下面这条链是把它们按原文的叙述顺序拼起来的**
（**不是原文给的单一步骤表**——原文没有那种表）：

| 步 | 做什么 | 代码 / 原文（逐字） |
|---|---|---|
| 1 | 取单例（`should be called first`） | `ProfileMgr* mgr = ProfileMgr::getInstance();` |
| 2 | 建 profile（只能 `WildcardProfileType`） | `Profile* profile = mgr->createProfile(WildcardProfileType);` |
| 3 | 灌规则（一句一条字符串，或建空规则再逐个 `set`） | `profile->createRule("*.*.*.datalog_level=3");` |
| 4 | **落盘**（不落盘别的进程看不见） | `profile->save(<filename>);` |
| 5 | 激活（对**下一次**执行生效） | `profileMgr->activateProfile(profile);` |
| 6 | 在 test method 里读属性值 | `int datalog_detail = Property::value("datalog_detail");` |

### 「怎么用」的第二个答案：`## 语法 / 参数` 节里那四段带代码的例子

**注意来源**：这四段**取自子主题**（节名里逐字写着取自哪一篇），**不是定义文档自己写的**，
**而那几篇子主题本页一篇都没读**（见 `## 出处`）。

| 例子（节名逐字） | 干什么 |
|---|---|
| `Profile creation` | 建 profile、灌规则、存到 `<device>/profiles/ProfileTest.prf` |
| `Adaptive sampling` | 按执行计数，每隔 N 颗器件切一次 profile |
| `Logging by test number` | 给 test 一个 test number，让规则引擎按它决定记不记 |
| `Evaluating a custom property` | 在 test method 里问一个自定义属性的值 |

**四段里能直接抄走的几条**（引 `## 语法 / 参数` 节里那几段例子的注释；`// ` 是代码注释符，此处是行首截取）：

- `Profile creation` 那段自己交代了它做什么：`This method creates and saves a sample profile programmatically.`
  以及落点：`The profile is saved to the "profiles" subdir of the current device.`
- `Adaptive sampling` 那段自己写了它的适用位置：`Ideally, this method is called from a test suite at the start of a testflow.`
- `Logging by test number` 那段说明了 test number 的作用：它会被 profile 规则引擎用来判断「是否要按 test number 记录」。
- `Evaluating a custom property` 那段说明了「属性没被定义时读回什么」：profile 在当前 execution context 里
  定义了 `logHistogram` 时返回规则里给的值，否则返回 `0`。

**⚠️ 上表第三、四条本页是转述，不是逐字引**——那两句注释在 raw 里跨了三行/两行，
逐字引要连注释符一起引，本页不把转述包成引文（§11.1）。

### 本页没给的

**规则字符串的语法、预定义属性清单、profile 与 testflow 的关联、Profile Editor 界面、
`getInstance()`/`freeInstance()` 之外的资源管理细节**——**全在本页没读的那几篇里**（见 `## 出处`）。

## 和谁有关

- [[data-logging-profiles]] —— **上游，同时是本页服务的对象**。
  本篇第一句就以 `With the data logging profile API` 开头，而那个链接指向的正是那一篇
  （`02.10.01.02_Data_Logging_Profiles.md`）；那一篇的 `#### Subtopics` 里也列了 `Data logging profile API`——
  **两篇是父子**。**「profile 是什么、两个出厂 profile、采样」那一页管；「用代码怎么建、怎么激活」本页管。**
  （**那一页的 wiki 页本页读过；它自己的 raw 本页没读。**）
- [[results]] —— **stage 页**。本页 `stage: results` 的理由：profile 决定的是**记录什么结果**。
  **本篇 raw 里没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分。
  [[results]] 那页把本页列在 L2 一栏，并引了 `02.10.01.02` 里一句「可以在 test method 内监测 yield 下降、
  现场激活 debug profile」的话——**那句话出自另一篇，本页没读那篇**，本页只把它记成「那一页这么写」。
- [[testmethod]] —— **本页 API 的调用场所**。原文两句点名：
  `The Property class is used by the test methods` 那一句与
  `To query the logging configuration from within a test method, use the Property class.`
  `## 语法 / 参数` 节的例子里也出现 `FUNCTIONAL_TEST()` 与 `judgeAndLog_FunctionalTest()`（**那一段来自子主题**）。
- [[testset]] —— **（推断）`## 语法 / 参数` 节里 `Logging by test number` 那段的主角**。
  那段代码写的是 `TESTSET set;` + `set.testname("EdlFfcDatalog");` + `set.testnumber(900);`。
  **依据只是这段代码的写法与 wiki 里那一页同名；本篇正文一次都没有点过 `TESTSET`。这是推断。**
- [[execution-context]] —— **`Property` 查值时的那个坐标**。原文逐字 `within the current execution context`，
  `## 语法 / 参数` 节的例子里还有 `based on the current execution context`。
  **那一页本页没读**——所以「execution context 是怎么算出来的」本页没有。
- [[device-directory]] —— **profile 文件该落的地方**。原文只说 `the profiles subdirectory`
  与 `the name of the device`；`<device directory>/profiles/` 这个形态出自 [[data-logging-profiles]]
  （**本页读过的 wiki 页**），例子代码里的 `"%s/profiles/%s"` 与之同形（**推断**）。
- [[flag]] —— **关系只有一处，而且很弱**。本篇 raw 里 `flag` 这个词**只出现一次**，
  在版本段：`Removed stdf_generation flag`。
  **所以「profile 实际改的是 flag」这条边不是本篇给的**——它出自 [[data-logging-profiles]]
  （本页读过那页，**那一页自己也把这条标成了推断**）。
- [[smartest-7.4.5]] —— **版本页**。本篇 `## Functional changes` 的第二条指这一版。
- [[smartest-6.3.2]] —— **版本页，读法是「更老」**。本篇第一条写的是
  `Introduced before SmarTest 6.3.2`（**哨兵值**，§11.2 ②：意思是「在本套文档集覆盖范围开始之前就已经有了」）。
- `Data logging profile rule syntax`（**未建**）—— **规则字符串与预定义属性的唯一出口**，
  本篇链了它**两次**（`Rule class` 与 `Property class` 各一次）。**本页没读。**
- `ProfileMgr class` / `Profile class` / `Rule class` / `Property class` / `Data logging profile API examples`
  （**5 篇子主题，均未建、均未读**）—— **本篇自己声明的全部子页**。
  ⚠️ **前四个类名在本篇里各被链了两次、指向两个不同路径**（`#### Subtopics` 指本目录的
  `02.10.01.02.08.0X`，正文的类清单指 `../02.07_Test_Method_Reference/02.07.04.01.169.0X`）——
  **那一节的「See `Data logging profile API examples`」也指 `../02.07_…/02.07.04.01.169.05`**。
  这两个位置是两篇物理文档（`source_topic` 号不同），标题却完全一样；
  **它们是不是 §10 说的「重复投放」，本篇一篇判不了，本页不裁定**（见 `## 出处` ⑤）。
- `ProfileCreation.cpp` / `SetProfile.cpp` / `EdlFfcDatalog.cpp` / `PropEvalBin.cpp`（**四个例子的源文件名**）——
  `## 语法 / 参数` 节里四段代码的头部注释；**它们不是语料里的文档**，本页没有去查。
- [[run]] —— **（推断）`activate` 生效的那个时刻**。原文 `apply to the next test execution`；
  `## 语法 / 参数` 节的例子里还有 `the start of a testflow`。
  **本篇没有把这件事与 [[run]] 连起来。这是推断。**

## 版本

原文 `## Functional changes` 段**两条**，逐字：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.4.5: Removed stdf_generation flag`

**两条性质完全不同，必须分开读：**

| 条目 | 是不是哨兵值（§11.2 ②） | 读法 |
|---|---|---|
| `Introduced before SmarTest 6.3.2` | **是**，措辞是 `before` | **不许读成「6.3.2 引入了这套 API」**。只能说：**7.10.3 上有，且它比 6.3.2 更老** → [[smartest-6.3.2]] |
| `SmarTest 7.4.5: Removed stdf_generation flag` | 不是，带版本号加冒号 | **7.4.5 起 `stdf_generation` 这个 flag 被移除** → [[smartest-7.4.5]] |

**第二条同时是本篇全文里 `flag` 出现的那唯一一次。**

**本篇没有的东西**（照实记，不替它补）：**没有第三条**。
所以「四个类分别是哪一版进来的」「`WildcardProfileType` 什么时候加的」「7.4.5 移除的那个 flag 原本管什么」
这类问题，**本篇答不了**。

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.01.02.08_Data_logging_profile_API.md`
（frontmatter `source_topic` = `105090.htm`；**7,213 字节 / 156 行**，**整篇读完**。
口径按 §11.5：字节是 `st_size`，行数是 `wc -l`，本语料末行带换行，两者恒等）

**本页读了的：只有这一篇。**
`## 语法 / 参数` 节是**脚本**从这一篇加它的五个子主题逐字抽的（**来源逐字写在节首**），**本页一个字没动**。

**本页没做的：**

- **本篇自己声明的 5 个子主题，一篇都没读**：`02.10.01.02.08.01_ProfileMgr_class.md` /
  `02.10.01.02.08.02_Profile_class.md` / `02.10.01.02.08.03_Rule_class.md` /
  `02.10.01.02.08.04_Property_class.md` / `02.10.01.02.08.05_Data_logging_profile_API_examples.md`
  （清单见 `## 语法 / 参数` 节首的说明）。
  **后果说清**：`## 语法 / 参数` 节里那四段带代码的例子（`Profile creation` / `Adaptive sampling` /
  `Logging by test number` / `Evaluating a custom property`）**就是从这些子主题抄的**——
  **本页对它们的了解，只到 `## 语法 / 参数` 节里逐字收的那几段为止**；
  那几段之外它们还写了什么（上下文、别的例子、别的选项），**本页一个字都没有**。
- **`Data logging profile rule syntax`（`02.10.01.02.06.03`）没读。** 本篇链了它两次
  （规则字符串的语法、预定义属性清单）。**所以「规则怎么写、有哪些预定义属性」本页答不了。**
- **`Data Logging Profiles`（`02.10.01.02`）那一篇的 raw 没读**——
  本页对它的了解全部来自 [[data-logging-profiles]] 那个 **wiki 页**（本页读过那一页，
  正文里凡出自它的地方都标了）。**所以本页与那一页之间只对齐到「wiki 页」这一层，没有 raw 级交叉核对。**
- **一个图都没有。** 本篇里 `![` 出现 **0 次**（本页查过），**所以这一页不含任何图证，也不缺**。
- **一处代码没跑、一次 API 没调。** `verified: doc-only` 指的就是这件事（§11：文档里有 ≠ 这台机器上能用）。
- **本篇没有 `## Procedure` / `## Before you begin` / 一条命令行 / 一条错误码。**
- **没有 `## Errors` / `## Warnings` 段**，所以本页**没有「报错条件」节**——
  不是漏写（骨架里本来就没有这一节），是语料没有。
- **`layer: n/a` / `stage: results` 不是本篇写的**——本篇没有 `## Application` 这类自我定位段，
  这两个值是本 wiki 的既有划分。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **第一句里 `profile` 是单数。** 逐字（句中连续片段）：
> `you can create and handle data logging profile and their rules and properties`
> ——**`profile` 后面紧跟 `their`**，按语法应是 `profiles`。**原文如此。**
>
> ② **`Profile` 那一段的最后一句没有句号。** 逐字（该段连续片段，行首截取）：
> `such as creating, loading, saving, and manipulating rules that are part of the profile`
> ——**`profile` 之后直接换段，没有 `.`。**
>
> ③ **`Property` 那一节里 `can be obtained` 出现了两次。** 逐字：
> `Or you can obtain the value of a property can be obtained by creating a Property object and using it directly:`
> ——**`you can obtain` 与 `can be obtained` 前后都用了一次**，一句话里两套主谓。
>
> ④ **`setRule` 那句以分号结尾。** 逐字：
> `The rule content of a particular position can be overwritten using a call to setRule(i, rule);`
> （原文 `setRule(i, rule)` 带反引号，本页按 §11.1 ③ 去掉了）——
> **相邻句子都以 `.` 结尾，只有这句是 `;`。**
>
> ⑤ **同一个类名被链了两次、指向两个不同路径。** 逐字（`#### Subtopics` 里）：
> `- [ProfileMgr class](<02.10.01.02.08.01_ProfileMgr_class.md>)`；
> 逐字（正文的类清单里）：`- [ProfileMgr class](<../02.07_Test_Method_Reference/02.07.04.01.169.01_ProfileMgr_class.md>)`。
> **四个类都是这个形态。哪一个是正本、它们是不是同一篇被投放两次，本篇没说，本页不裁定。**
>
> ⑥ **同一个工厂对象在一篇里有两个名字。** 逐字并列（同一篇文档里）：
> `ProfileMgr* mgr = ProfileMgr::getInstance();`（`ProfileMgr class` 一节）
> 与 `profileMgr->activateProfile(profile);`（`Rule class` 一节）——
> **`mgr` 与 `profileMgr` 指同一个东西**，原文没有说明。
>
> ⑦ **遍历那段代码里有两行各是一个 `.`。** 逐字（`for` 循环那一段，按原文断行）：
> `Rule* rule = profile->getRule(i);` / `.` / `.` / `}`
> ——**那是语料自带的省略记号。** 本页照原样引，没有把它改写成 `…` 或 `...`（§11.1）。
>
> ⑧ **`#### Subtopics` 是 4 级标题，却是本篇最顶层的结构段**——
> 它出现在 `## ProfileMgr class` 这些 2 级标题**之前**，级别却比它们深。
> **全语料同此形态**（[[data-logging-profiles]]、[[apg-pattern-file]]、[[device-access-file]] 也是 `#### Subtopics`），
> **不是本篇独有**（推断）。
>
> ⑨ **`## Related information` 那一行是五个链接首尾相接、中间一个字符都没有。** 逐字（该行的连续片段）：
> `[Rule class](<../02.07_Test_Method_Reference/02.07.04.01.169.03_Rule_class.md>)[Property class](<../02.07_Test_Method_Reference/02.07.04.01.169.04_Property_class.md>)`
> ——**两条链接直接粘在一起，没有空格、没有分隔符**。
> （[[waveform-mapping]] 那篇的 `## Related information` 是同一个毛病。）
>
> ⑩ **本篇没有 §11.2 ① 那种编码损坏**（本页查过：全文汉字 **0** 个、`鈥` **0** 处、
> 非 ASCII 字符 **0** 个）。

`verified: doc-only`
