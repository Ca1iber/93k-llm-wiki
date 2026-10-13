---
type: object
title: SHARING_CONFIGURATION
layer: n/a
stage: pin
tags: [pin, mtp, sharing, fixture-delay, utility-control, domains, mts, api]
related: [pin, sharing-configuration-file, utility-line-assignments, mtp-memory-test, mtp-shared-test-commands, mtp-3.1.5]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.md
  # 2026-10-13 补：本页两处「逐字」引文（`The name of the sharing configuration file
  # which you want to load.` / `The file must be located in the <device directory>/configuration/
  # directory.`）实际出自**子主题** .load，原先没列。
  # 2026-10-10 表格换成指针后，第七类回上游核引文时才显出来。
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.03_SHARING_CONFIGURATION.load.md
created: 2026-09-24
updated: 2026-10-13
verified: doc-only
---

# SHARING_CONFIGURATION

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

**`SHARING_CONFIGURATION` 是读 `Sharing configuration file` 那份文件的 C++ API，
而且只在 MTP 里有。** 主篇的定义句：

> The SHARING_CONFIGURATION class provides an API for accessing the data contained in the Sharing configuration file.

**紧跟其后的一条 Note 划死了它的适用面**（逐字）：

> Note The SHARING_CONFIGURATION API is available only for MTP.

头文件：`/opt/93000mts/mts/solution_tools/import/SHARING_CONFIGURATION.h`。

> **本页 `layer: n/a` 的依据**（**这一步是（推断）**，依据只有路径与那条 Note）：
> 这个头文件以 **`/opt/93000mts/mts/`** 开头——MTS（Memory Test System）那一棵树，
> 而 93K 的 Test Method API 那一族以 **`/opt/hp93000/soc/`** 开头。
> 加上「available only for MTP」那条 Note，**它不属于 93K 的三层接口**，
> 于是 §6 里那个 `n/a` 就是它该填的值。
> **本篇没有说它是 L1 / L2 / L3 中的任何一层，也没有说它在哪一版 93K 上可用。**

### 入口只有一条：`getInstance()`

主篇那条 Note 把用法顺序写死了（逐字）：

> Note To use the SHARING_CONFIGURATION API, you must first call getInstance(). Then you can use other member functions. See the example in SHARING_CONFIGURATION.getInstance().

**子主题 `getInstance()` 那一篇说得更硬**（逐字）：

> You must call this member function first before you can use any other member functions of the SHARING_CONFIGURATION API.

**它返回的是「唯一那一个对象」**——`returns the reference to the only object of the SHARING_CONFIGURATION class.`
（**「单例」两个字是（推断）**，依据是 `the only object` 这句与 `getInstance()` 这个名字；
**本篇没有用这个词。**）

### 19 个成员函数，主篇自己分了三组

主篇的 `## Class definition` / `### Member functions` 一节把 19 个函数**按用途分组**——
**这是文档自己的分类，不是本页分的**：

| 组（原文标题） | 成员 |
|---|---|
| **入口** | `getInstance()` |
| **`Data loading functions:`** | `hasLoaded()` / `load()` / `setRefPin()` |
| **`Data accessing functions:`** | `getModeContext()` / `isFXDLIgnorePin()` / `utilitySearchFirst()` / `utilitySearchNext()` / `utilityActionExecute()` / `utilityGetApplicableSitesString()` / `utilitySubstitutePins()` / `domainsGetXSize()` / `domainsGetYSize()` / `domainsGetZSize()` / `domainsGetApplicableSitesString()` / `domainsGetSiteAtPos()` / `getTerminatedPinList()` / `getBufferPinMap()` / `getDomain()` |

**19 个成员函数的签名全在「语法 / 参数」节里**
（那是脚本从 19 个子主题逐字取的，**本页不重抄**）。
下面只写**签名表里看不出来的东西**。

### 载入那三个函数：一套「只加载一次」的规矩

**这是本页最要紧的一节——三个函数之间有一条规矩，原文在每一篇里各写了一遍。**

| 情况 | `load(config)` | `setRefPin(pinName)` |
|---|---|---|
| **还没有任何 sharing configuration 被加载** | 从**文件**加载 | 从**那个 pin 的物理连接**解析出来 |
| **已经加载过了** | **不加载**：`load() dose not load the specified file if a sharing configuration has already been down loaded.` | **不加载**：`The setRefPin() dose not load the specified configuraiton if a configuration has already been loaded.` |

**`hasLoaded()` 就是给这两条用的**（逐字）：

> The hasLoaded() member function of SHARING_CONFIGURATION returns "true" if a configuration file has been loaded, and "false" if not.

- **返回 `true` 时**：① `You can use the data-accessing member functions of SHARING_CONFIGURATION to read the data.`；
  ② `The load() and setRefPin() member functions do not load the specified configuration.`
- **返回 `false` 时**：`You can use either load() or setRefPin() to load a sharing configuration. Then you can read its data via the data-accessing member functions of SHARING_CONFIGURATION.`

**换句话说：这是一个「先到先得」的加载口**——
**第一个成功的 `load()` 或 `setRefPin()` 定下数据，之后两个函数都不再改变它。**
（**这一步是本页的（推断）**，依据是把上面两条 `does not load` 合起来读；
**「之后想换一份怎么办」本篇一个字都没写——语料未写。**）

**`load()` 的文件位置是硬要求**（参数表逐字）：

> The name of the sharing configuration file which you want to load.

> The file must be located in the <device directory>/configuration/ directory.

**`setRefPin()` 有一条「兜底」的 Note**（逐字）：

> Note If you are not sure about the pin's physical connections, use the load() member function to load the configuration from the sharing configuration file.

**两条 `does not load` 的原文各有各的错字**（`dose` / `configuraiton`）——
**本页照原样引，见「出处」⚠️①②。**

### 索引从 0 开始，五处一致

**「第几行」「第几格」这件事，原文在五处都写明了从 0 起**：

| 函数 | 原文 |
|---|---|
| `utilitySearchFirst()` | `If it is the first line, 0 will be returned.` |
| `utilityActionExecute()` | `0 represents the first line.` |
| `utilityGetApplicableSitesString()` | `0 represents the first line.` |
| `utilitySubstitutePins()` | `0 represents the first line in the utility_control block.` |
| `domainsGetApplicableSitesString()` / `domainsGetSiteAtPos()` | `The position in the X dimension, starts from 0.`（Y / Z 同句） |

**`utilitySearchFirst()` 与 `utilitySearchNext()` 是一对**（两篇各写一遍，措辞只换了主语）：

> The utilitySearchFirst() and utilitySearchNext() member functions of SHARING_CONFIGURATION find the locations of the specified utility control line within the utility_control block in the Sharing configuration file. If it is the first line, 0 will be returned.

> utilitySearchFirst() returns the first matched location; utilitySearchNext() returns the next matched location.

**即：同名行有多条时，用 `First` 起头、用 `Next` 往下走。**

### `utilitySubstitutePins()` 那一篇有两处说不通（**照实记，不替它改**）

**① 签名少一个 `t`：**

```
void utilitySubstituePins(int index, const string & pinsFrom, string & pinsTo) const
```

**页名与主篇的成员清单写的都是 `utilitySubstitutePins()`（有 `t`），签名写的是 `Substitue`。**
**上游核过：两种拼法在 `131652.htm` 里都在**（见「出处」⚠️③）。

**② 散文说 `returns`，而签名返回 `void`：**

> The utilitySubstitutePins() member function of SHARING_CONFIGURATION returns the names which will replace the other pins's names as defined in the specified utility control line.

**那一句里还有一个 `pins's names`（双重所有格）**。
**签名是 `void` + 第三个参数 `string & pinsTo`**——**「返回」实际是走这个引用出去的**
（**这一步是本页的（推断）**，依据只是 `void` 与 `string &` 这两个类型；
**参数表自己也说** `This variable stores the returned new names which replace the pin names in pinsFrom.`）。

### 这些函数各读文件里的哪一块（**本页的推断，逐条给依据**）

**主篇只说「访问那份文件里的数据」，没有给对照表。**
但**参数说明里出现了几个块名**，把成员函数与文件的段对起来是可能的：

| 函数族 | 原文里出现的块名 | 对得上文件里的哪一段 | 依据强度 |
|---|---|---|---|
| `utilitySearchFirst` / `utilitySearchNext` / `utilityActionExecute` / `utilityGetApplicableSitesString` / `utilitySubstitutePins` | **`utility_control` block** | `utility_control` 段 | **原文点名**（这个串在 5 篇的参数表里各出现一次） |
| `getTerminatedPinList()` | **`topology` block** | `topology` 段 | **原文点名** |
| `domainsGetXSize()` / `domainsGetYSize()` / `domainsGetZSize()` / `domainsGetApplicableSitesString()` / `domainsGetSiteAtPos()` | `the domains structure` | `domains` 段 | **原文点名** |
| `isFXDLIgnorePin()` | `the ignore list of the fixture delay settings` | `fxdl_ignore_pins` 段 | **（推断）**——名字与语义都对得上，**但本类这一篇没有出现 `fxdl_ignore_pins` 这个词** |
| `getBufferPinMap()` | `The buffer pin map maps site numbers to buffer pin lists.` | `rss_buffer_pins` 段 | **（推断）**——「site 号 → buffer pin 列表」的形状对得上 |
| `getModeContext()` | `the mode context in the loaded sharing configuration` | `pin_configuration` 段里的 `<context>` | **（推断）**，且**这一条最弱**：原文只说「loaded sharing configuration」，**没有指出在哪一段** |

**后面三个段名（`fxdl_ignore_pins` / `rss_buffer_pins` / `pin_configuration`）
不是本类这一篇给的**——它们来自本 wiki 的 [[sharing-configuration-file]] 那一页
（**本页读了那一页**；**它那一篇的 raw 本页没读**，
所以那三个段名**本页核不了原文**）。

## 典型用法

**本篇没有 `## Procedure` 段、没有 `## Before you begin` 段、没有 `## Important points` 段。**
**19 个子主题里只有一个带 `## Example` 段**——`getInstance()` 那一篇。
**所以本页能确证的用法只有那一段代码，其余 18 个函数的「怎么调」只能靠参数表读。**

那段例子逐字（**它就是「语法 / 参数」节里 `### Example` 那一块，本页不重抄**）：

```
//You must first use getInstance() to get the only one active object of the SHARING_CONFIGURATION class.
SHARING_CONFIGURATION &sharingConfig = SHARING_CONFIGURATION::getInstance();

//Load sharing configuration file "default.cfg".
sharingConfig.load("default.cfg");
```

**排成步骤：**

| # | 做什么 | 依据 |
|---|---|---|
| 1 | **`getInstance()` 拿唯一那个对象**（例子里同时把它绑到一个引用上） | `getInstance()` 那一篇的 `## Example`；主篇的 Note |
| 2 | **载入**：`load("<文件名>")` 或 `setRefPin("<pin 名>")` | `load()` / `setRefPin()` 两篇 |
| 3 | （可选）**先问 `hasLoaded()`** 再决定要不要载 | `hasLoaded()` 那一篇 |
| 4 | **用那 16 个 data-accessing 函数读** | 主篇的分组 |

**几点照实说明：**

- **例子里载的是 `"default.cfg"`**，而 `load()` 的参数说明要求文件在
  `<device directory>/configuration/` 下——**所以那个文件名指的是「device 目录下 configuration/ 里的
  `default.cfg`」**（**这一步是（推断）**：原文没有把这两句连起来说）。
- **其余 18 个成员函数一个调用例子都没有。** 「`index` 从哪来」这一问只有一条线索：
  `utilitySearchFirst()` / `utilitySearchNext()` 返回的**行号**，就是
  `utilityActionExecute()` / `utilityGetApplicableSitesString()` / `utilitySubstitutePins()`
  要的那个 `index`（**（推断）**，依据是五处 `0 represents the first line.`
  与两处 `find the locations` 的措辞一致）。
- **`domains*` 那一族要 `x` / `y` / `z` 三个坐标**——
  **「坐标怎么定、domain 是什么」本篇一个字都没有**（**语料未写**）。
- **`utilitySubstitutePins()` 的 `pinsFrom` / `pinsTo` 两个方向是反的**（原文逐字）：
  `pinsFrom` 是 `The pin names which will be substituted with new names.`，
  而 `pinsTo` 是 `This variable stores the returned new names which replace the pin names in pinsFrom.`
  ——**「被替换的」进 `pinsFrom`，新名字从 `pinsTo` 出来**。

## 和谁有关

- [[pin]] — **stage 页**。本页 `stage: pin` 指的是「最近的一段」而不是「归属」（§6）。
  依据是 [[sharing-configuration-file]] 那一页（**本页读了那一页**）：
  它把这份文件归到「load board 的引脚与 sharing 结构 → pin」。
  **本类这一篇自己只说「那份文件里的数据」，没有说那份文件属于哪一段。**
- [[sharing-configuration-file]] — **本类读的那份文件**。
  主篇 `## Related information` 一节**整节只有它一条**，主篇第一句也点它。
  关系是**单向的「访问器 ↔ 被访问的文件」**：
  [[sharing-configuration-file]] 那一页的 `related` 里也已经列了本页
  （**本页读了那一页**；**它那一篇的 raw 本页没读**）。
- [[utility-line-assignments]] — **`utility_control` 段里那些 line 是什么**。
  本类的 `utility*` 一族读的是文件里的 `utility_control` block（**原文点名**，见上面那张表），
  而**「utility line 本身怎么编号、有几根、上拉到哪」不在本篇**。
  **那一页本页没读**；**本条关系来自 [[sharing-configuration-file]] 那一页，不是本篇。**
- [[mtp-memory-test]] / [[mtp-shared-test-commands]] — **MTP 那一章里的两页**。
  本类 `available only for MTP`（原文 Note），而本页的 raw 就在
  `02.12_Memory_Test_Plus_7.10.2` 章下——**这两条按章名与页名并列**。
  **两页本页都没读**；**本篇也没有点名 MTP 章里任何一个别的对象。**
- [[mtp-3.1.5]] — **版本页**：本篇 `## Functional changes` 唯一的落点。
- `fd_merge.pl` / `OnlineCompensation` — **与 fixture delay 有关的两个工具**
  （这两个名字**出自 [[sharing-configuration-file]] 那一页**，**本类这一篇没有出现它们**；
  本类这一篇只给了 `isFXDLIgnorePin()` 那句 `ignored by the fixture delay settings`）。
  **它们的文档本页没读。**（**不在 allowlist，故不链。**）
- `Sharing configuration file` 那一篇 raw（`02.12.02.05.06.07.07.02`）—— **本页没读**。
  **本页与那份文件的所有关系，都只到「这个类是它的访问器」这一层**；
  **文件本身的语法、段名、例子，本页一处都没有。**
- **本篇没有点名任何一个 test method、也没有点名任何固件命令。**
  所以「谁在用这份文件、用了之后行为怎么变」——**本页一个字都没有**（**语料未写**）。

## 版本

主篇有 `## Functional changes` 段，**只有一条**：

- **Introduced in MTP 3.1.5**

**这是一条正常的 `Introduced in`，不是 §11.2 ② 那个 `Introduced before` 哨兵**——
所以它**可以照字面读**：**MTP 3.1.5 之前没有这个类**。

**19 个子主题每一篇的 `## Functional changes` 都是同一条 `Introduced in MTP 3.1.5`**
（**本页把 19 篇都读了，逐篇核过**）——
**没有一个成员函数是后来单独加的**（**这一步是本页的（推断）**：
依据是 19 篇的版本行完全相同；**「版本行相同」不等于「同一次改动」，但本页没有别的证据**）。

**两条边界：**

- **本篇没有说这个类在 SmarTest 上从哪一版可用**——它写的是 **MTP 的版本号**。
  （§11.2 ④：`Functional changes` 里不止 SmarTest 一条产品线，**版本号要带产品前缀**。）
- **3.1.5 之后有没有再改过、有没有被废弃——这 20 篇一个字都没有。**
  **「没记录」不等于「没改过」**（§13.1 第 ⑥′）。

## 出处

`sources:` 一篇：

`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.md`
（TDC `131630.htm`，**73 行 / 5,043 字节**）。

### 这一篇是「壳」，所以读了它的 19 个子主题（**逐条声明**）

**主篇自己没有一个 `Syntax` 段、没有 `Parameters` 段、没有一个 `Example`**——
它的 4,120 字符语法节里**每一段的标题都带「（取自子主题 〈子主题名〉）」这个后缀**。
**主篇的散文只有四块**：一条 19 行的 `Subtopics` 清单、两句定义 / Note、
一组按用途分组的成员清单、一条 `getInstance()` 优先的 Note——**机制全推给了子主题**。

**所以按 PROSE-SPEC 的例外，本页读了那 19 篇子主题。**
理由：**本页的「语法 / 参数」节（脚本产）已经逐字引了它们**，
而主篇本身给不出「这些函数各干什么」——不读子主题，「是什么」这一节只能写「语料未写」。
**逐条如下**（行数 / 字节数实测，口径见 §11.5：行 = `wc -l`，字节 = `st_size`）：

| # | 子主题（`02.12.06.25.` 前缀略） | 行 | 字节 |
|---|---|---|---|
| 1 | `01_SHARING_CONFIGURATION.getInstance.md` | 36 | 1,209 |
| 2 | `02_SHARING_CONFIGURATION.hasLoaded.md` | 29 | 1,478 |
| 3 | `03_SHARING_CONFIGURATION.load.md` | 47 | 1,533 |
| 4 | `04_SHARING_CONFIGURATION.setRefPin.md` | 45 | 1,427 |
| 5 | `05_SHARING_CONFIGURATION.getModeContext.md` | 22 | 641 |
| 6 | `06_SHARING_CONFIGURATION.isFXDLIgnorePin.md` | 41 | 874 |
| 7 | `07_SHARING_CONFIGURATION.utilitySearchFirst.md` | 43 | 1,499 |
| 8 | `08_SHARING_CONFIGURATION.utilitySearchNext.md` | 43 | 1,435 |
| 9 | `09_SHARING_CONFIGURATION.utilityActionExecute.md` | 43 | 1,070 |
| 10 | `10_SHARING_CONFIGURATION.utilityGetApplicableSitesString.md` | 43 | 1,103 |
| 11 | `11_SHARING_CONFIGURATION.utilitySubstitutePins.md` | 65 | 1,772 |
| 12 | `12_SHARING_CONFIGURATION.domainsGetXSize.md` | 22 | 825 |
| 13 | `13_SHARING_CONFIGURATION.domainsGetYSize.md` | 22 | 825 |
| 14 | `14_SHARING_CONFIGURATION.domainsGetZSize.md` | 22 | 825 |
| 15 | `15_SHARING_CONFIGURATION.domainsGetApplicableSitesString.md` | 50 | 1,028 |
| 16 | `16_SHARING_CONFIGURATION.domainsGetSiteAtPos.md` | 59 | 1,050 |
| 17 | `17_SHARING_CONFIGURATION.getTerminatedPinList.md` | 41 | 990 |
| 18 | `18_SHARING_CONFIGURATION.getBufferPinMap.md` | 22 | 685 |
| 19 | `19_SHARING_CONFIGURATION.getDomain.md` | 41 | 720 |

**合计 19 篇 / 20,989 字节。全部整篇读完。**

### 本页没做的

- **`Sharing configuration file` 那一篇 raw（`02.12.02.05.06.07.07.02`）没读**——
  **这是本页最大的缺口**：本类的每一个函数都在读它，而**它本身一个字都不在本页**。
  （**本页读了本 wiki 的 [[sharing-configuration-file]] 那一页**，
  上面那张对照表里三个推断档的段名来自它；**它的 raw 本页没读，所以那些段名本页核不了原文**。）
- **任何一个 test method（sharing 那一族）的 raw 都没读**——
  所以「谁在用这份文件、用了之后怎么变」本页没有。
- **`fd_merge.pl` / `OnlineCompensation` 的文档没读**——
  本页只有 `isFXDLIgnorePin()` 那句 `ignored by the fixture delay settings`。
- **一张图都没看——因为这 20 篇里没有图。** 实测 20 个文件全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论**（§11.4：没看图就写「本页没用图」，理由不编）。
- **没有实跑。** 没有在任何 MTP 环境里 `load()` 过一份 sharing configuration，
  也没有验证过「加载过之后再 `load()` 真的不加载」。`verified: doc-only` 指的就是这件事。
- **`<device directory>/configuration/` 这个路径没有核过**——
  §11.5 的口径只覆盖「文档字节 / 行数」，**目录路径不在本页能核的范围内**。

> ⚠️ **这一族的语料瑕疵，本页照实记下、一处都没替它改。**
> **回上游核过 9 个 `.htm`**：`131630.htm`（主篇，12,861 字节 / 39 行）、
> `131631.htm`（`getInstance`）、`131634.htm`（`load`）、`131635.htm`（`setRefPin`）、
> `131645.htm`（`isFXDLIgnorePin`）、`131646.htm` / `131647.htm`（`utilitySearchFirst` / `Next`）、
> `131652.htm`（`utilitySubstitutePins`）、`131661.htm`（`domainsGetSiteAtPos`）。
> **结论：①–④、⑥–⑩ 全是「上游就有的」，不是转换损坏；只有 ⑧ 那一处是转换丢的块边界。**
>
> ① **两处 `dose`（应为 `does`）**：
>    `load() dose not load the specified file if a sharing configuration has already been down loaded.`
>    与 `The setRefPin() dose not load the specified configuraiton if a configuration has already been loaded.`
>    **上游核过**：`131634.htm` 里逐字是 `dose not load the`；
>    `131635.htm` 里逐字是 `dose not load the specified configuraiton if a`。
>    同一条里还有 `configuraiton`（应为 `configuration`）。**两处都是上游的错字。**
> ② **`down loaded` 分成两个词**（`has already been down loaded`）——**上游核过**，`131634.htm` 如此。
> ③ **签名与页名拼法不一致**：签名是
>    `void utilitySubstituePins(int index, const string & pinsFrom, string & pinsTo) const`
>    （`Substitue`，少一个 `t`），页名与主篇清单都是 `utilitySubstitutePins()`。
>    **上游核过：`131652.htm` 里两种拼法都在**（`utilitySubstituePins` 与 `utilitySubstitutePins`）。
>    同一篇里还有 `the other pins's names`（双重所有格）——**上游核过**：
>    `131652.htm` 里 `pins&#39;s names` 逐字如此。
> ④ **正文里的函数名大小写不一致**：
>    `The domainsGetSiteatPos() member function of SHARING_CONFIGURATION returns the site at the specified (x, y, z) position.`——
>    **`SiteatPos` 的小写 `a` 与页名 / 签名里的 `SiteAtPos` 不同**。
>    **上游核过：`131661.htm` 里 `domainsGetSiteatPos` 出现 2 次、`domainsGetSiteAtPos` 出现 4 次**——
>    **文档自己两处写法并存。**
> ⑤ **主篇的成员清单里有一条链接文本被从中间切开**：
>    `- [domainsGetXSize () cons](<02.12.06.25.12_SHARING_CONFIGURATION.domainsGetXSize.md>)t`
>    ——**锚文本是 `domainsGetXSize () cons`，`t` 落在 `</a>` 外面**。
>    **上游核过：`131630.htm` 第 28 行逐字就是 `>domainsGetXSize () cons</a>t`**——
>    **切开发生在上游的锚文本里，`t` 本来就在 `<a>` 外面。这一处也是上游就有的。**
> ⑥ **`domainsGetSiteAtPos` 的参数表把第三个参数的标签写成 `y`**：
>    三行说明依次是 X / Y / Z 三个维度，**而标签是 `x` / `y` / `y`**（第三行该是 `z`）。
>    **上游核过：`131661.htm` 那张表的 `keyword` 元素依次是
>    `x` / `y` / `z` / `x` / `y` / `y`**——**本函数那张表（第二张）的第三行确实是 `y`。**
> ⑦ **`isFXDLIgnorePin` 的签名写 `pinname`、参数表写 `pinName`**：
>    签名 `bool isFXDLIgnorePin(const string & pinname) const`，表里那格是 `pinName`。
>    **上游核过：`131645.htm` 里两个拼法都在。**
> ⑧ **主篇在成员清单末尾那条 Note 是「粘」上去的**：
>    `- [getDomain (int site) const](<02.12.06.25.19_SHARING_CONFIGURATION.getDomain.md>)` 之后
>    **没有空行**，紧接着就是
>    `Note To use the SHARING_CONFIGURATION API, you must first call getInstance(). Then you can use other member functions.`。
>    **上游核过：`131630.htm` 里那条 Note 是一个独立的 `<div class="note">`，
>    紧跟在 `</ul>` 之后**——**所以这一处是转换丢了块边界（文本一字未少），
>    渲染时那个 Note 会并进最后一条列表项里。**
> ⑨ **`getInstance()` 的签名把 `static` 写了两遍**：
>    `static SHARING_CONFIGURATION & getInstance() [static]`——一次是关键字、一次在方括号里。
>    **上游核过：`131631.htm` 里逐字如此。**
> ⑩ **`Subtopics` 清单里 `utilitySearchNext` 少了那对括号**：
>    `- [SHARING_CONFIGURATION.utilitySearchNext](<02.12.06.25.08_SHARING_CONFIGURATION.utilitySearchNext.md>)`，
>    而它前后 18 条都带 `()`。
>    **该子主题的标题也照抄了这个缺失**——
>    **上游核过：`131647.htm` 的 `<h1>` 是 `SHARING_CONFIGURATION.utilitySearchNext`，
>    而 `131646.htm` 的 `<h1>` 是 `SHARING_CONFIGURATION.utilitySearchFirst()`。**
> ⑪ **20 篇都没有坏字。** 用 `[一-鿿]` 实测 **0 处非 ASCII 字符**
>    （没有 `鈥` / `渭` / `碌` 那一族）。
>    **这是「本页量过的」，判据是这 20 个文件**；§11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何 MTP 环境里 load 过一份 sharing configuration**
（§11：文档里有 ≠ 这台机器上能用；尤其「加载过之后再 `load()` 不加载」这条，
**动手前先照实机核对**）。
