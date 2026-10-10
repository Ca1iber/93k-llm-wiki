---
type: object
title: Driver sharing 支撑 API（MTP）
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23_SHARED_LEAKAGE_PARALLEL_TEST.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Driver sharing 支撑 API（MTP）

<!-- `extract/wiki-plan.csv` 里本页 slug 是 `mtp-shared-test-commands`，
     但这一页收了**三个类**，H1 于是用族名而不是某一个类名。
     归类依据见「出处」。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,832 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.md>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.01_SHARING_CONFIGURATION.getInstance.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.02_SHARING_CONFIGURATION.hasLoaded.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.03_SHARING_CONFIGURATION.load.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.04_SHARING_CONFIGURATION.setRefPin.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.05_SHARING_CONFIGURATION.getModeContext.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.06_SHARING_CONFIGURATION.isFXDLIgnorePin.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.07_SHARING_CONFIGURATION.utilitySearchFirst.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.08_SHARING_CONFIGURATION.utilitySearchNext.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.09_SHARING_CONFIGURATION.utilityActionExecute.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.10_SHARING_CONFIGURATION.utilityGetApplicableSitesString.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.11_SHARING_CONFIGURATION.utilitySubstitutePins.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.12_SHARING_CONFIGURATION.domainsGetXSize.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.13_SHARING_CONFIGURATION.domainsGetYSize.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.14_SHARING_CONFIGURATION.domainsGetZSize.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.15_SHARING_CONFIGURATION.domainsGetApplicableSitesString.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.16_SHARING_CONFIGURATION.domainsGetSiteAtPos.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.17_SHARING_CONFIGURATION.getTerminatedPinList.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.18_SHARING_CONFIGURATION.getBufferPinMap.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.19_SHARING_CONFIGURATION.getDomain.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 SHARING CONFIGURATION.getInstance）

```
static SHARING_CONFIGURATION & getInstance() [static]
```

### Example（取自子主题 SHARING CONFIGURATION.getInstance）

This code fragment demonstrates how to use getInstance() to create the SHARING_CONFIGURATION object for using other member functions.

```
//You must first use getInstance() to get the only one active object of the SHARING_CONFIGURATION class.
SHARING_CONFIGURATION &sharingConfig = SHARING_CONFIGURATION::getInstance();

//Load sharing configuration file "default.cfg".
sharingConfig.load("default.cfg");
```

### Syntax（取自子主题 SHARING CONFIGURATION.hasLoaded）

```
bool hasLoaded() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.load）

```
void load(const string & config)
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131634.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Syntax（取自子主题 SHARING CONFIGURATION.setRefPin）

```
void setRefPin(const string & pinName)
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131635.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Syntax（取自子主题 SHARING CONFIGURATION.getModeContext）

```
const string & getModeContext() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.isFXDLIgnorePin）

```
bool isFXDLIgnorePin(const string & pinname) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131645.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Syntax（取自子主题 SHARING CONFIGURATION.utilitySearchFirst）

```
int utilitySearchFirst(const string & name) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131646.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description
> 表内引用（1 条，供检索）：`utility control block`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）

### Syntax（取自子主题 SHARING CONFIGURATION.utilitySearchNext）

```
int utilitySearchNext(const string & name) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131647.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description
> 表内引用（1 条，供检索）：`utility control block`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）

### Syntax（取自子主题 SHARING CONFIGURATION.utilityActionExecute）

```
int utilityActionExecute(int index) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131650.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description
> 表内引用（1 条，供检索）：`Sharing configuration file`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）

### Syntax（取自子主题 SHARING CONFIGURATION.utilityGetApplicableSitesString）

```
string utilityGetApplicableSitesString(int index) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131651.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description
> 表内引用（1 条，供检索）：`Sharing configuration file`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）

### Syntax（取自子主题 SHARING CONFIGURATION.utilitySubstitutePins）

```
void utilitySubstituePins(int index, const string & pinsFrom, string & pinsTo) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131652.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：Parameter | Description
> 表内引用（1 条，供检索）：`Sharing configuration file`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetXSize）

```
int domainsGetXSize() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetYSize）

```
int domainsGetYSize() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetZSize）

```
int domainsGetZSize() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetApplicableSitesString）

```
string domainsGetApplicableSitesString(int x, int y) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131660.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetSiteAtPos）

```
int domainsGetSiteAtPos(int x, int y, int z) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131661.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Syntax（取自子主题 SHARING CONFIGURATION.getTerminatedPinList）

```
string getTerminatedPinList(const string & vterm) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131664.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Syntax（取自子主题 SHARING CONFIGURATION.getBufferPinMap）

```
const map<int, string> & getBufferPinMap() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.getDomain）

```
vector <int> getDomain(int site) const
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131666.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description

<!-- 语法节 end -->

## 是什么

这一页收的是 **MTP 下 `driver sharing` 相关的三个支撑类**。
它们的共同点有三条，**每一条都是三篇文档各自明说的**：

1. **只对 MTP 可用**——三篇各有一句 `available only for MTP`。
2. **都是 C++ 类 API**，装在 `/opt/93000mts/mts/solution_tools/` 底下（不是 `soc/prod_com` 那一族）。
3. **都要自己写成 test method**，不像 `SharedContinuity` 那样直接有个现成的 test method 可用。

| 类 | 干什么 | 头文件 |
|---|---|---|
| **`SHARING_CONFIGURATION`** | **读** sharing configuration file 里的数据 | `…/solution_tools/import/SHARING_CONFIGURATION.h` |
| **`SHARED_CONTINUITY_TEST`** | 一次 pass 测完 shared / non-shared / cross-terminated **三类针的连通性与短路** | `…/solution_tools/common/include/SHARED_CONTINUITY_TEST.h` |
| **`SHARED_LEAKAGE_PARALLEL_TEST`** | 一次 pass **并行**测这三类针的**漏电** | `…/solution_tools/common/include/SHARED_LEAKAGE_PARALLEL_TEST.h` |

原文对后两个的定位各一句话：

> 「The `SHARED_CONTINUITY_TEST` class provides an API for checking the continuity and finding the
> short circuits for the DUTs with driver sharing. **It tests shared, non-shared, and
> cross-terminated pins in a single pass.**」

> 「The `SHARED_LEAKAGE_PARALLEL_TEST` class provides an API for doing parallel leakage test for the
> DUTs with driver sharing. **It tests non-shared pins, cross-terminated pins, and the shared pins
> terminated by a common DPS in a single pass.**」

**`SHARING_CONFIGURATION` 是另一回事**：它不测任何东西，只是把
[[sharing-configuration-file]] 的内容**读出来给你**。原文的用法门槛是硬性的：

> **必须先调 `getInstance()`，之后才能用其他成员函数。**

它的 19 个成员函数按原文自己分的两组：
**数据装载**（`hasLoaded` / `load` / `setRefPin`）与
**数据访问**（`getModeContext` / `isFXDLIgnorePin` / `utilitySearch*` / `utilityActionExecute` /
`utilityGetApplicableSitesString` / `utilitySubstitutePins` / `domainsGet*` /
`getTerminatedPinList` / `getBufferPinMap` / `getDomain`）。

### 同一个测试，MTP 给了三种做法

这是这三篇放在一起最该看出的一件事。**连通性和漏电各有一张三选一的表**，原文两篇各写了一遍：

| | 连通性 / 短路 | 漏电 |
|---|---|---|
| **① 现成的 test method** | `SharedContinuity` test method | `SharedLeakageParallel` test method |
| **② 自建 test method 用的 API** | **`SHARED_CONTINUITY_TEST`** | **`SHARED_LEAKAGE_PARALLEL_TEST`** |
| **③ 换条件用的 API** | `MTP_CONTINUITY_TASK` | `MTP_LEAKAGE_TASK` |

**怎么选**（原文的口径）：

- **①**：`Use it when you Do not have special requirements such as a customized testing algorithm
  or a special output format.` 原文还加了一句 **`It is the easiest way to develop a test.`**
- **②**（本页这两个类）：要**自建 test method**、要**定制输出**时。
- **③**：想在**同一个 test method 里用不同测试条件**测这些针时。
- ②和③的**具体差别**，原文写在 ③ 的专页里（`MTP_CONTINUITY_TASK` / `MTP_LEAKAGE_TASK`），
  **本页没读那两篇**。

### 用 ② 之前，test method 里必须先加三个 limit

**这些是字面字符串，拼错就不认**。原文两篇给的六个名字**格式不一样**，照实转述：

| 连通性（圆括号 + 小写 `mv`） | 漏电（方括号） |
|---|---|
| `"Shared Voltage(mv)"` | `"Leakage Current Shared Pins [uA]"` |
| `"Non-Shared Voltage(mv)"` | `"Leakage Current Non-Shared Pins [uA]"` |
| `"Cross-Terminated Voltage(mv)"` | `"Leakage Current Cross Pins [uA]"` |

> ⚠️ **两组命名风格不同**（一组 `(mv)`、一组 `[uA]`），
> **本页没有替它们统一**——它们是**要照着敲的字面量**，统一了就错。
> 另外原文写的是 **`mv`（小写）**，**不是 `mV`**；本页照抄原文。

## 典型用法

**`SHARED_CONTINUITY_TEST` / `SHARED_LEAKAGE_PARALLEL_TEST` 的调用形状是一模一样的四段：**

**`init()` → 链式 setup → `execute()` → 取结果。**

- **`init()` 必须第一个调**（原文注释：`Always do initialization at the beginning of test`）。
- **setup 函数全部返回类引用**，所以能一路 `.` 挂下去；**`execute()` 是 `void`**，链到头。
- **结果四个口**：`judgeAndLog()`（判 + 记）、`print()`（打到 UI Report Window）、
  `getPassFail()`（整体或按针）、`getValue()`（按针取值）。
- **setup 与 `execute()` 包在 `ON_FIRST_INVOCATION_BEGIN()` / `END()` 里**，
  **取结果在块外**。原文注释说明了原因：
  `The following block only executes for the first site of multi-site setup`。

**原文 `SHARED_LEAKAGE_PARALLEL_TEST` Example 1，逐字照抄**：

```c
#include "solution_tools.h"
#include "testmethod.hpp"
#include "mapi.hpp"

class CSharedLeakageParallel: public testmethod::TestMethod
{
    virtual void run()
    {
      // The following block only executes for the first site of
      // multi-site setup
      ON_FIRST_INVOCATION_BEGIN();
      {
        // Always do initialization at the beginning of test
        mTest.init();

        // hand over the parameters to the test class
        mTest.sharingConfigFile("default.cfg")
             .pinShared("Addr_Bus,Command_Bus")
             .pinNonShared("DQ_Bus,DQS_DiffBus,DM")
             .pinCross("Clock_Bus")
             .forceVoltage(1.2)
             .settlingTime(10)
             .prechargeTime(10);

        // execute the test
        mTest.execute();
      }
      ON_FIRST_INVOCATION_END();

      // set result
      mTest.judgeAndLog();
      // Print out in the UI Report Window.
      mTest.print();
    }

private:
    SHARED_LEAKAGE_PARALLEL_TEST mTest;
};
```

**从这段能读出来的三件事**：

1. **`sharingConfigFile("default.cfg")` 传的是相对文件名**，不是全路径。
   原文在 `load()` 的参数说明里给了落脚点：
   `The file must be located in the <device directory>/configuration/ directory.`
2. **三个 pin list 分别对应三类针**（`pinShared` / `pinNonShared` / `pinCross`），
   和上面那六个 limit 名字一一对上。
3. **`SHARED_CONTINUITY_TEST` 的同名 Example 1 形状相同**，差别只在 setup 链上——
   它多两个 force 函数（`forceCurrentNonShared()` / `forceCurrentCross()`）、
   多 `terminationDPS()` / `supplyDPS()` / `output()`，且 `pinShared` 配的是 `forceVoltage(1.1)`。
   **那一段本页没抄**，要看去 raw。

**`SHARING_CONFIGURATION` 的用法不一样**，它没有「执行」这一步。
上面的语法节里有原文 `getInstance()` 那段例子（**逐字，脚本抽的**），不再重复。

> **本页没有 `## 语法 / 参数` 之外的完整例子。** 两个类各自的 **Example 2（定制输出）**
> 本页没抄——它们演示的是用 `PinUtility.getDigitalPinNamesFromPinList()` 把 pin list
> 展开成逐针名再打印，**代码接近 40 行重复三遍**，要看请回 raw。

## 和谁有关

- [[sharing-configuration-file]] — `SHARING_CONFIGURATION` 读的就是它；
  原文 `Related information` 里只列了这一篇
- [[mtpt]] — 同属 MTP 的映射表，是本批一起建的 MTP 页
- [[mtp-maintenance-operations]] — 同上，另一篇 MTP 页
- `MTP_CONTINUITY_TASK` / `MTP_LEAKAGE_TASK`（**均未建**）— 上面三选一表里的 ③；
  **②和③的差别写在它们里面**
- `SharedContinuity` / `SharedLeakageParallel` test method 及各自 syntax（**均未建**）— 三选一表里的 ①
- [[testmethod]] — 本页 `stage: testmethod` 的理由：三个类都要在 test method 里用
- [[dps128-dps64-cards]]、[[xps256-status-flags]] — 漏电测试要力/测的那一端是 DPS；
  **本页不判哪种卡支持哪个函数**
- [[results]] — `judgeAndLog()` / `print()` / `getPassFail()` 的产物落到结果侧；
  本页只写函数名，**不写它们产出的数据长什么样**

## 版本

**⚠️ 首先一条：这一页的版本号是 MTP 版本号，不是 SmarTest 版本号。**
本 wiki 其他页写的多是 SmarTest（`6.5.2`、`7.2.0` 这种）；
**这里的三篇写的是 `MTP 3.1.x`，两套编号不可比。**

- **`SHARING_CONFIGURATION`**：`Introduced in MTP 3.1.5`
- **`SHARED_CONTINUITY_TEST`**：`Introduced in MTP 3.1.3`；
  `MTP 3.1.5: Added new API: MTP_CONTINUITY_TASK.`
- **`SHARED_LEAKAGE_PARALLEL_TEST`**：`Introduced in MTP 3.1.3`；
  `MTP 3.1.5: Added new member functions, precharge(), prechargeVoltage() preFunction(),
  for SHARED_LEAKAGE_PARALLEL_TEST.`；
  同一行还写着 `MTP 3.1.5: Added new API: MTP_LEAKAGE_TASK.`

> **注意上面前两条里有一类现象**：`MTP_CONTINUITY_TASK` / `MTP_LEAKAGE_TASK`
> **是别的 API**，它们的「新增」被记在了这两篇的 `## Functional changes` 底下。
> **本页照实转述，没有把它们挪走**——原文就是写在这儿的。

## 出处

`sources:` 三篇：

| 文档 | 讲什么 | `## Functional changes` |
|---|---|---|
| `…/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.md` | 类的定位、19 个成员函数清单、`getInstance()` 优先 | MTP 3.1.5 引入 |
| `…/02.12.06.21_SHARED_CONTINUITY_TEST.md` | 定位、6 个 limit 名、三选一、构造函数与 17 个成员函数、Example 1/2 | MTP 3.1.3 引入 |
| `…/02.12.06.23_SHARED_LEAKAGE_PARALLEL_TEST.md` | 同上，成员函数 16 个，多 `precharge*` / `preFunction` | MTP 3.1.3 引入 |

> **归类依据（本 wiki 加的判断，不是原文的）**：原文把这三篇平铺在
> `02.12_Memory_Test_Plus_7.10.2/` 底下，**没有把它们归成一族**。
> 本页把它们合并的依据是「都属 driver sharing 的 MTP 支撑 API」。
> **slug 里的 `test-commands` 因此偏窄**——`SHARING_CONFIGURATION` 不是测试命令，
> 是数据访问 API。**记在这里，不偷偷改 slug**（slug 是标识符，改了就断链）。

**本页没做的**：

- **三个类的成员函数只列了名字。** `SHARING_CONFIGURATION` 的 19 个子主题、
  `SHARED_CONTINUITY_TEST` 的 17 个、`SHARED_LEAKAGE_PARALLEL_TEST` 的 16 个，
  **一条签名都没抄**（`SHARING_CONFIGURATION` 那 19 条的语法由脚本进了上面的语法节，
  **另外两个类的成员函数签名本页一个字都没有**）。
- **两个类的 Example 2（定制输出）没抄**。
- **`Related information` 里的文档一篇都没读**：
  `SharedContinuity test method`、`SharedContinuity syntax`、
  `SharedLeakageParallel test method`、`SharedLeakageParallel syntax`、
  `MTP_CONTINUITY_TASK`、`MTP_LEAKAGE_TASK`、
  `Setting up for using driver sharing APIs`、`Sharing configuration file`。
- **`How to create a universal test method class` 没读**（原文让你去那儿看怎么加 limit）。
- **`/opt/93000mts/…/DriverSharing.tar.gz` 里的完整 test method 不在语料里**，
  原文两篇都指向它，**本页无从读起**。

### ⚠️ 这三篇里的语料笔误（照实列，本页一处都没替它改）

| # | 原文写的 | 位置 |
|---|---|---|
| 1 | **`utilitySubstituePins`** | `SHARING_CONFIGURATION` 的**语法代码块**里 |
| 2 | **`utilitySubstitutePins`** | **同一篇**的子主题链接、成员函数清单、**以及子主题文件名**里 |

> **第 1、2 条是同一篇文档里的两种拼法**，差一个字母（`Substitue` / `Substitute`）。
> 代码块里是 `-tue`，清单和文件名里是 `-tute`。**本页不判哪个是对的**——
> **要照着敲这个函数名，请回 raw 两边都看一眼。**

| # | 原文写的 | 位置 |
|---|---|---|
| 3 | `[domainsGetXSize () cons](<…>)t` | 成员函数清单：`const` 被**链接边界劈开**，末尾的 `t` 掉在链接外面 |
| 4 | `SHARED_LEAKAFE_PARALLEL_TEST & precharge (…)` 等**三条** | 漏电篇成员函数清单：`LEAKAFE`（**少一个 `G`**） |
| 5 | `SHARED_LEAKAGE_PARELLEL_TEST.execute()` | 漏电篇：子主题链接与清单里都是 `PARELLEL` |
| 6 | `SHARED_LEAKAGE_PARALLEL_TEST.judegeAndLog()` | 漏电篇：`judege`（应为 `judge`） |
| 7 | `SHARED_CONTNUITY_TEST` | 连通性篇 Examples 的 Note 里（**少一个 `A`**） |
| 8 | `SHARED_CONTINUITY_TEST__.print` | 子主题**文件名**里是**两个下划线** |
| 9 | 参数表第三行标签写作 **`y`**，描述却是 `The position in the **Z** dimension` | `domainsGetSiteAtPos` 的参数表；**语法行里是 `(int x, int y, int z)`** |
| 10 | 裸的 **` Note `** 标记 | 两篇都有：`…driver sharing APIs](<…>).Note The SHARED_… API is available only for MTP.`（**句子被 ` Note ` 劈开**） |
| 11 | `…API](<…>)Note To use the SHARING_CONFIGURATION API…` | 同一现象，见 `SHARING_CONFIGURATION` 篇 |

> **第 3、9 条就在本页上面的语法节里**——那一节是脚本逐字抽的、不许改（§4），
> **所以它保留了原文的错**。**这不是本页抄错，是脚本按规矩没有资格改它。**

`verified: doc-only`
