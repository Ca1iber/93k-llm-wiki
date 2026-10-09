---
type: object
title: RESULT_CONFIGURATION
layer: L2
stage: results
tags: [result-configuration, results, error-map, l2, api, port, edge, result-width]
related: [results, error-map, error-map-tool, testmethod, port-editor, smartest-7.1.3]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.191_RESULT_CONFIGURATION.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# RESULT_CONFIGURATION

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,906 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.191_RESULT_CONFIGURATION.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

```
// Declare a new result configuration object:
RESULT_CONFIGURATION config1;
STRING exceptionPins("pin1,pin2");

// Use member functions to specify the needed settings for port "port1":
config1.setNumberOfResultsPerCycle( RESULT_CONFIGURATION::RPC8, "port1" );
config1.setResultWidth( RESULT_CONFIGURATION::_2Bit, "port1" );
config1.setResultStorageLocation( RESULT_CONFIGURATION::TP, "port1" );
config1.setResultGranularity( RESULT_CONFIGURATION::cycle, "port1" );

// Pins excepted from the above  storage locations settings:
config1.setResultStorageLocationExceptionPinList( exceptionPins );

// Global settings:
config1.setResultStorageIncompleteBehavior( RESULT_CONFIGURATION::ErrorImmediate );
config1.setMultipleExecutions( true );

// Enable the configuration specified in the object "config1":
config1.enable();

// Use convenience constructor to specify a new result configuration
// for a single port and the global settings:
STRING exceptionPins("pin1,pin2");
RESULT_CONFIGURATION config2( "port2",
                              RESULT_CONFIGURATION::RPC1,
                              RESULT_CONFIGURATION::_1Bit,
                              RESULT_CONFIGURATION::TP,
                              "",
                              RESULT_CONFIGURATION::edge,
                              "",
                              RESULT_CONFIGURATION::ErrorOnRequest,
                              false );

// Make some adjustments:
config2.setResultStorageLocationExceptionPinList( exceptionPins );

// Specify some additional settings for another port:
config2.setResultGranularity( RESULT_CONFIGURATION::cycle, "port1" );

// Enable the configuration specified in the object "config2":
config2.enable();

// A newly created configuration contains the default settings.
// This can be used to reset the result configuration:
RESULT_CONFIGURATION  defaultConfig;
defaultConfig.enable();

```

<!-- 语法节 end -->

## 是什么

**`RESULT_CONFIGURATION` 是「结果怎么记」的配置对象。**
它是一个 **L2 的 test method API**：一个对象里装着若干项设置，最后一次 `enable()` 把整套设置交给固件。

原文的定义句（逐字；段内链接已按 §11.1 ② 剥掉 markdown 链接标记）：

> 「This API serves to define the result configuration. For more information see `Result Configuration` and `Configuring the Error Map recording`.」

**那一句里两个链接的目标**（原文里是相对路径）分别是
`<../02.08_Setup_and_Result_Tools/02.08.04.08.04_Result_Configuration.md>` 与
`<../02.06_Command_Reference/02.06.11.01.02.01_Configuring_the_Error_Map_recording.md>`。
**这两个出口本页都没读**（见 `## 出处`）——**所以本页只有 API 这一侧，
「界面上长什么样」「Error Map 记录本身怎么配」本页一个字都没有。**

**头文件也明写了**，逐字：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/ResultConfiguration.h.」

**还有一条硬约束，写在 `enable()` 那一节里**（本页把它提到最前面，因为它是全篇唯一一条 `Only`）：

> 「Only one configuration can be active at a time.」

### 两个构造函数

`## 语法 / 参数` 节里逐字收着两个：

```cpp
RESULT_CONFIGURATION();
RESULT_CONFIGURATION( const STRING& portName,
                      const NumberOfResultsPerCycle& numberOfResultsPerCycle,
                      const ResultWidth& resultWidth,
                      const ResultStorageLocation& resultStorageLocation,
                      const STRING& edgeToResultMapping,
                      const ResultGranularity& resultGranularity,
                      const STRING& resultStorageLocationExceptionPinList,
                      const ResultStorageIncompleteBehavior& resultStorageIncompleteBehavior,
                      const bool& multipleExecutions );
```

**无参那个建出来是「默认设置」**——原文在例子的注释里明说（那是两行注释，本页分两段逐字引，各去掉行首的 `// `）：

> 「A newly created configuration contains the default settings.」

> 「This can be used to reset the result configuration:」

**九个参数那个是「便利构造」**，原文的注释把它叫 `convenience constructor`，
用途是 `to specify a new result configuration for a single port and the global settings`
（**即：一个 port 的 port 级设置 + 所有全局设置，一次给完**）。

### 九个参数逐个

原文 `## Class definition` 一节给出的是**这两个构造函数的参数表**（`Parameters` 标题下），九个参数逐条如下。
**取值一栏里凡是带 `RESULT_CONFIGURATION::` 前缀的，都是原文的写法，大小写照抄。**

| 参数 | 原文的说明（逐字，剥链接） | 取值 | 默认 |
|---|---|---|---|
| `portName` | The port for which the result configuration is to be defined. | port 名字符串 | 未写 |
| `numberOfResultsPerCycle` | The number of results per cycle for the specified port. | `RESULT_CONFIGURATION::RPCi,`，**`where i is 1, 2, 4, 6, or 8 for 1, 2, 4, 6, or 8 results. The default is RPC1.`** | **`RPC1`** |
| `resultWidth` | The result width for the specified port. | `RESULT_CONFIGURATION::_1Bit One bit code` / `RESULT_CONFIGURATION::_2Bit Two bit code. This is the default.` | **`_2Bit`** |
| `resultStorageLocation` | Defines whether the results of the specified port are stored in the internal Error Map or in the external memory (RAM). | `RESULT_CONFIGURATION::TP` / `RESULT_CONFIGURATION::RAM` | 未写 |
| `edgeToResultMapping` | 见下「只在 `RPC2` / `RPC4` 下才有意义」 | 一个字符串，格式见下 | **`RPC2` 与 `RPC4` 各有一个默认串** |
| `resultGranularity` | This parameter defines the system behavior for two aspects of gathering information on the edge level. | `RESULT_CONFIGURATION::edge` / `RESULT_CONFIGURATION::cycle` | **`cycle`** |
| `resultStorageLocationExceptionPinList` | A comma separated pin list containing pins whose results are to be stored in the internal Error Map even if they belong to a port whose results are to be stored in the external memory. If you want to remove all exceptions, specify an empty list. | 逗号分隔的 pin 名；**空表 = 清掉全部例外** | 未写 |
| `resultStorageIncompleteBehavior` | This parameter defines the behavior of the system when the `result storage location` is set to RAM, and result recording was aborted. | `ErrorImmediate` / `ErrorOnRequest` / `failOnRequest` | **`ErrorOnRequest`** |
| `multipleExecutions` | 见下「`Multiple Executions` 一节的两种取值」 | `true` / `false` | 未写 |

**四处的默认值分散写在正文里**（上面表里加粗的四格）：`RPC1` / `_2Bit` / `cycle` / `ErrorOnRequest`。
**其余五项本篇没有写默认值**——照实记，不替它补。

（表里 `result storage location` 那一处在原文里是一个指向 `setResultStorageLocation()` 的链接，
目标是 `02.07.04.01.191_RESULT_CONFIGURATION.md#_130383__dle_setResultStorageLocation`；本页只留链接文字。）

### 三个「三选一」的枚举，逐条

#### ① `resultStorageLocation`：记在哪（`TP` / `RAM`）

| 取值（逐字） | 原文的说明（逐字） |
|---|---|
| `RESULT_CONFIGURATION::TP` | Results are stored in the internal Error Map. The internal Error Map is located inside the test processor. |
| `RESULT_CONFIGURATION::RAM` | Results are stored in the external memory. External memory means the vector memory. |

**选 `RAM` 时才有「例外名单」**，原文：

> 「If you select RAM, you can define an exception list. The results of the pins in this list will be
> stored in the internal Error Map.」

**即：`RAM` 是「记在向量内存」，`TP` 是「记在测试处理器内部的 Error Map」；
例外名单把个别 pin 从 `RAM` 拉回 `TP`。**
（`internal Error Map` 这个对象本身见 [[error-map]]；**那一页本页没读**，本页只按本篇的两句陈述。）

#### ② `resultGranularity`：失败时重不重跑（`edge` / `cycle`）

| 取值（逐字） | 原文的说明（逐字） |
|---|---|
| `RESULT_CONFIGURATION::edge` | This option activates the following settings: |
| `RESULT_CONFIGURATION::cycle` | With this option, a failing test is not repeated, and any formally correct definition of the result combinations will be accepted. This is the default. |

**`edge` 那一条下面挂着两条并列的设定**（原文用 `-` 列表给的两条）：

> 「- You activate gathering result information for all 8 edges by repetition of a failing test if
> numberOfResultsPerCycle is set to RPC1 and resultWidth is set to _2Bit.」

> 「- You require the result combinations defined with edgeToResultMapping to satisfy the conditions
> for edge retrieval. For details see `Possible combinations of CYRM, CYRP, and DCRM`.」

（那一行里的链接目标是
`<../02.06_Command_Reference/02.06.11.01.02.01.02.05_Possible_combinations_of_CYRM__CYRP__and_DCRM.md>`。）

**第一条里的两个前提要读准**：**`RPC1` 与 `_2Bit` 同时成立**，才谈「靠重跑失败测试去凑齐 8 个 edge」。
**第二条把「哪些组合合法」推给了 `Possible combinations of CYRM, CYRP, and DCRM`（本页没读那篇）。**

#### ③ `resultStorageIncompleteBehavior`：记到一半被打断怎么办（三种）

**原文在这条上给了完整的三种行为，而且这是本页与 [[error-map]] 最直接的交汇点**——
因为它的前提就是「存到 `RAM` 的那一路被中断」：

| 取值（逐字，大小写照抄） | 原文的说明（逐字，剥链接） |
|---|---|
| `RESULT_CONFIGURATION::ErrorImmediate` | SmarTest issues an error message immediately after completion of the functional test. This message reports the channels, pins, and sites of all channel groups on which recording was aborted. |
| `RESULT_CONFIGURATION::ErrorOnRequest` | SmarTest does not issue an error message immediately after completion of the test, but only if a channel which is involved in a recording abort is queried for result data. **（这句原文还有下半句，见 `## 出处` ③）** |
| `RESULT_CONFIGURATION::failOnRequest` | SmarTest does not issue any error message. If a channel of a group on which recording was aborted is queried for result data, all its cycles will be reported as failing. |

⚠️ **第三个取值的写法是 `failOnRequest`——小写 `f`，和另外两个以 `Error` 开头的不是一个风格。**
**原文如此，本页照抄，见 `## 出处` ②。**

**`failOnRequest` 有一段专门的适用说明，逐字**：

> 「This option can be used in a production environment if the result data is recorded in acquire
> failure mode, since if any data is recorded with this recording mode, the device must in fact have
> failed. Actually, recording will only be aborted in case of a massive fail on several pins
> belonging to the same channel group.」

**读法**：**`failOnRequest` 只在「用 acquire failure 模式记录」时才适合生产**——
因为那种模式下「记到了数据」本身就等于「器件一定失败了」。

### `Multiple Executions`：两种取值

原文在 `setMultipleExecutions()` 一节逐字给出：

| 取值（逐字） | 原文的说明（逐字） |
|---|---|
| `true` | Repetition of a failing test is allowed. |
| `false` | Repetition of a failing test is not allowed. |

**它的取回侧原文是**：`This member function retrieves if multiple executions of a failing test are allowed at all.`
（`at all` 是原文的措辞）。

### `edgeToResultMapping`：只在 `RPC2` / `RPC4` 下才有意义

这一段原文在两个地方各抄了一遍（构造函数的参数表和 `setEdgeToResultMapping()` 一节），逐字：

> 「If `setNumberOfResultsPerCycle()` is set to RPC2 or RPC4, you can specify a string that defines
> which edges are to be combined in the 2 or 4 results. The format of the string is」

```
"c1: edge_list1 [c2: edge_list2 [c3: edge_list3 [c4: edge_list4]]]"
```

**两个默认串**，逐字：

| 场景 | 默认值 |
|---|---|
| `The default for RPC2 is:` | `"c1:1,2,3,4 c2:5,6,7,8"` |
| `The default for RPC4 is:` | `"c1:1,2 c2:3,4 c3:5,6 c4:7,8"` |

**⚠️ 取值集合里还有 `RPC6` 与 `RPC8`，但这一节只给了 `RPC2` / `RPC4` 的默认串**——
`RPC6` / `RPC8` 时 edge 怎么合，本篇没写（见 `## 出处`）。

### `portName` 的默认值 `"@@"` = 全部 port

**port 级那十个成员函数的签名里都写着 `const STRING& portName = "@@"`**，
而它们各自的参数表里都写着同一句话，**只是 `The port for which` 后面那一截随函数变**。
举 `getResultStorageLocation()` 那一处，逐字：

> 「The port for which the storage location of the results is to be retrieved. The default is @@, which stands for all ports.」

**后半句 `The default is @@, which stands for all ports.` 十处一字不差**（本页逐处核过）；
前一截按函数不同，例如 `getResultWidth()` 那处是
`The port for which the result width is to be retrieved.`。

**所以「不给 port 名」等于「所有 port 一起设」**，不是「随便挑一个」。

### 哪些是 port 级、哪些是全局

**这条区分在例子代码里看得出来**：`config1` 用注释把它分成了两段——
`// Use member functions to specify the needed settings for port "port1":` 与 `// Global settings:`。

| 范围 | 成员函数 | 判据 |
|---|---|---|
| **port 级**（10 个） | `getEdgeToResultMapping` / `setEdgeToResultMapping`、`getNumberOfResultsPerCycle` / `setNumberOfResultsPerCycle`、`getResultGranularity` / `setResultGranularity`、`getResultStorageLocation` / `setResultStorageLocation`、`getResultWidth` / `setResultWidth` | 签名带 `const STRING& portName = "@@"` |
| **全局**（9 个） | `enable()`、`getMultipleExecutions` / `setMultipleExecutions`、`getResultGranularityExceptionPinList` / `setResultGranularityExceptionPinList`、`getResultStorageIncompleteBehavior` / `setResultStorageIncompleteBehavior`、`getResultStorageLocationExceptionPinList` / `setResultStorageLocationExceptionPinList` | 签名里**没有** `portName` |

**本页要标出来的一处不对称**（**这是读签名读出来的，原文没有评述**）：
**`setResultStorageLocation()` 是 port 级的，而它配的那张例外名单
`setResultStorageLocationExceptionPinList()` 是全局的**——
所以「按 port 设记录位置」与「按 pin 设例外」两件事的作用域不一样。**原文没有解释这个不对称。**

### 十九个成员函数（全清单，逐字）

原文 `Member functions` 一段把它们列成一张表（`enable()` 加上 9 对 get/set），**本页照抄名字**：

| # | 名字（逐字） | 范围 | 一句话（原文逐字，剥链接） |
|---|---|---|---|
| 1 | `enable()` | 全局 | This member function activates the settings of the RESULT_CONFIGURATION object in the firmware. **（另有半句见下）** |
| 2 | `getEdgeToResultMapping()` | port | This member function retrieves the sub-cycle definition for the specified ports. |
| 3 | `getMultipleExecutions()` | 全局 | This member function retrieves if multiple executions of a failing test are allowed at all. It has no parameters. |
| 4 | `getNumberOfResultsPerCycle()` | port | This member function retrieves the result granularity, that is, the number of results per cycle, for the specified ports. |
| 5 | `getResultGranularity()` | port | This member function retrieves the behavior of the system for the specified ports if a test fails and one two bit result is requested per cycle for the respective port. |
| 6 | `getResultGranularityExceptionPinList()` | 全局 | This member function retrieves all pins for which only cycle results are recorded. It has no parameters. |
| 7 | `getResultStorageIncompleteBehavior()` | 全局 | This member function retrieves the behavior of the system if recording was aborted on a pin that stores its result in the external memory. It has no parameters. |
| 8 | `getResultStorageLocation()` | port | This member function retrieves the storage location for the specified ports. |
| 9 | `getResultStorageLocationExceptionPinList()` | 全局 | This member function retrieves the pins whose results are stored in the internal error map although they belong to a port whose storage location is set to the external memory. |
| 10 | `getResultWidth()` | port | This member function retrieves the result width for the specified ports. |
| 11 | `setEdgeToResultMapping()` | port | This member function defines the sub-cycles for the specified ports if the result granularity (number of results per cycle) is 2 or 4. |
| 12 | `setMultipleExecutions()` | 全局 | This member function defines if repetition of a failing test is allowed at all. |
| 13 | `setNumberOfResultsPerCycle()` | port | This member function defines the result granularity, that is, the number of results per cycle, for the specified ports. |
| 14 | `setResultGranularity()` | port | This member function defines the behavior of the system |
| 15 | `setResultGranularityExceptionPinList()` | 全局 | This member function defines the pins for which only cycle results are recorded when a failing test is repeated. |
| 16 | `setResultStorageIncompleteBehavior()` | 全局 | This member function defines the behavior of the system if recording was aborted on a pin that stores its result in the external memory. |
| 17 | `setResultStorageLocation()` | port | This member function defines the storage location of the results for the specified pins. **（原文写的是 `pins`，见 `## 出处` ①）** |
| 18 | `setResultStorageLocationExceptionPinList()` | 全局 | This member function defines the pins whose results are to be stored in the internal Error Map even if they belong to a port whose results are to be stored in the external memory. |
| 19 | `setResultWidth()` | port | This member function defines the width of the result, 1 bit or two bits. |

**第 14 条那一句在原文里是断开的**——`This member function defines the behavior of the system`
后面接两条 `-` 列表（第 ② 节里已逐字引过）。**原文不是一句完整的陈述句。**

**第 1 条还有半句**（上一节已引过两条），第三条逐字是：

> 「The activated settings will be valid until enable() is executed again. This function has no parameters.」

**即：`enable()` 之后设置一直有效，直到你再 `enable()` 一次。**

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`。**
「怎么用」只能从 `## Example` 那一节（本页 `## 语法 / 参数` 节逐字收着的那一段）和 19 个成员函数各自的说明里读出来。

### 两条路（都出自那一段例子）

**路径 A：默认构造 + 逐个 set + `enable()`**（`config1`）——
原文的注释把顺序写得很清楚，照抄：

| 步 | 原文注释（逐字） | 代码（逐字） |
|---|---|---|
| 1 | `// Declare a new result configuration object:` | `RESULT_CONFIGURATION config1;` |
| 2 | `// Use member functions to specify the needed settings for port "port1":` | `config1.setNumberOfResultsPerCycle( RESULT_CONFIGURATION::RPC8, "port1" );` 等四句 |
| 3 | `// Pins excepted from the above  storage locations settings:` | `config1.setResultStorageLocationExceptionPinList( exceptionPins );` |
| 4 | `// Global settings:` | `config1.setResultStorageIncompleteBehavior( RESULT_CONFIGURATION::ErrorImmediate );` + `config1.setMultipleExecutions( true );` |
| 5 | `// Enable the configuration specified in the object "config1":` | `config1.enable();` |

**路径 B：便利构造一次给完 + 再微调 + `enable()`**（`config2`）——
原文注释逐字：`// Make some adjustments:`、`// Specify some additional settings for another port:`，
最后同样是 `config2.enable();`。

### 一条「重置」惯用法

**这是那一段例子里最实用的一条**，原文注释逐字（两行，本页分两段引，各去掉行首的 `// `）：

> 「A newly created configuration contains the default settings.」

> 「This can be used to reset the result configuration:」

```
RESULT_CONFIGURATION  defaultConfig;
defaultConfig.enable();
```

**即：想回到默认设置，不必逐个 set 回去——建一个空的、`enable()` 它就行。**

### 用的时候要记住的三件事

| # | 事情 | 依据（原文逐字） |
|---|---|---|
| 1 | **`enable()` 之前什么都没生效** | `This member function activates the settings of the RESULT_CONFIGURATION object in the firmware.` |
| 2 | **同时只能有一份配置是 active 的** | `Only one configuration can be active at a time.` |
| 3 | **不给 port 名 = 设置所有 port** | `The default is @@, which stands for all ports.` |

**⚠️ 例子里的一个组合本页不裁定**：`config2` 的便利构造传的是
`RESULT_CONFIGURATION::edge` 配 `RESULT_CONFIGURATION::_1Bit`（且 `edgeToResultMapping` 传 `""`），
而 `edge` 那两条效果自己都带着前提（见「是什么」第 ② 节：**`RPC1` 与 `_2Bit` 同时成立**）。
**原文没有说明这个组合是什么意思，也没有说它合法还是非法——本页把两处并列，不替它调和。**

### 本页没给的

**「界面上这些设置在哪一页签」「怎么把设置存下来」「Error Map 本身怎么配」**——
本篇把这三件事分别推给了 `Result Configuration`（`02.08.04.08.04`）、`Configuring the Error Map recording`
（`02.06.11.01.02.01`）和 `Possible combinations of CYRM, CYRP, and DCRM`（`02.06.11.01.02.01.02.05`），
**三篇本页一篇都没读**（见 `## 出处`）。

## 和谁有关

- [[results]] —— **stage 页**。本页 `stage: results` 的理由：它配的就是「结果怎么记」。
  **本篇 raw 里没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分。
  [[results]] 那页把本页列在 L2，并且**记着一条本篇没有的事实**：要把 Result Configuration 界面的设置
  存下来、必须从本 API 建一个 test method——**那句话出自 `02.08.04.08.04`，本页没读那篇**，
  本页只把它记成「那一页这么写」。
- [[error-map]] —— **本页两个取值的落点**。`RESULT_CONFIGURATION::TP` 的说明逐字是
  `Results are stored in the internal Error Map. The internal Error Map is located inside the test processor.`，
  `::RAM` 的是 `External memory means the vector memory.`
  [[error-map]] 那页自己把「怎么配内部/外部」指给了 `Result Mode`（**那是 GUI 侧的那篇，本页没读**）——
  **两页说的是同一件事的两端：本页是 API 侧的 `TP`/`RAM`，那一页是界面侧的 `Result Mode`。**
- [[error-map-tool]] —— **同一支 GUI 侧的对口工具**。[[error-map-tool]] 那页自己列着
  「[[result-configuration]] —— 子主题 `Result Configuration` 对应的页」。
  **本页与它的关系是「配置 ↔ 使用」**：本页配的是记到哪、记多细，那一页消费记下来的 Error Map。
- [[testmethod]] —— **API 的调用场所**。原文的定义句只说 `This API serves to define the result configuration.`，
  **没有说「它是 test method API」**——这句话出自 `02.08.04.08.04`（本页没读那篇），
  [[results]] 与 [[mapping-results]] 两页都记着它。本页 `layer: L2` 是从**它所在的章**
  （`02.07_Test_Method_Reference`）和那条外部证据一起读出来的。
- [[port-editor]] / [[pin]] —— **（推断）配置的作用单位**。本页十个成员函数是 **port 级**的
  （`The default is @@, which stands for all ports.`），例外名单是 **pin 级**的。
  **本篇没有一句话提到 port 或 pin 的界面**——这条边是本页按「作用单位」接的，不是文档给的。这是推断。
- [[smartest-7.1.3]] —— **版本页**。本篇 `## Functional changes` 只有一条，指这一版；
  [[smartest-7.1.3]] 那页也把本篇列在自己的清单里。
- `Result Configuration`（**未建**）—— 本篇第一个出口（`02.08.04.08.04`），**GUI 侧**。**本页没读。**
- `Configuring the Error Map recording`（**未建**）—— 本篇第二个出口（`02.06.11.01.02.01`）。**本页没读。**
- `Possible combinations of CYRM, CYRP, and DCRM`（**未建**）—— **`edge` 那一路的合法组合表**，
  本篇链了它**两次**（`resultGranularity` 参数表与 `setResultGranularity()` 各一次）。**本页没读。**
- `Retrieving edge information by repeating the test`（**未建**）—— `setResultGranularity()` 正文里指的那篇，
  讲「靠重跑失败测试取 edge 信息」。**本页没读。**
- [[digital-capture-test]] —— **同章的另一条 L2 命令，本页不把它当同一个东西。**
  本页是**配置对象**（一个类，`enable()` 生效）；那一条是**执行命令**。
  **本篇没有提到它**，这条并列只是提醒别混（**取材边界**）。
- [[mapping-results]] —— **对照表页**。它把本页（`RESULT_CONFIGURATION` 的五个 set 函数）
  与 `Result Mode` 页签的五个设置项排在同一行，并注明那一行的 GUI 侧名字是**图证**。
  **那一页读的 raw 与本页不同**（它读的是 `02.08.04.08.04*`），**本页没读那几篇。**

## 版本

原文 `## Functional changes` 段**只有一行**，逐字：

- `Introduced in SmarTest 7.1.3`

**这一条不是哨兵值**（§11.2 ② 的哨兵是 `Introduced before SmarTest 6.3.2` 那种 `before` 写法）：
它带明确版本号、措辞是 `in`，**所以读成「7.1.3 引入了 `RESULT_CONFIGURATION`」** → [[smartest-7.1.3]]。

**本篇没有的东西**（照实记，不替它补）：**没有第二条**。
所以「`RPC6` / `RPC8` 是哪一版加的」「`failOnRequest` 是哪一版加的」「7.1.3 之后这套 API 改过什么」，
**本篇都答不了**。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.191_RESULT_CONFIGURATION.md`
（frontmatter `source_topic` = `130383.htm`；**24,081 字节 / 671 行**，**整篇读完**。
口径按 §11.5：字节是 `st_size`，行数是 `wc -l`，本语料末行带换行，两者恒等）

**本页的 `## 语法 / 参数` 节是脚本从这一篇抽的**（节首逐字写着来源，**只有这一篇，没有子主题**），**本页一个字没动**。

**本页没做的：**

- **本篇正文点名的三篇，一篇都没读**：`Result Configuration`（`02.08.04.08.04`）、
  `Configuring the Error Map recording`（`02.06.11.01.02.01`）、
  `Possible combinations of CYRM, CYRP, and DCRM`（`02.06.11.01.02.01.02.05`）。
  **后果说清**：**「界面上这些设置长什么样、怎么存下来」和「哪些 edge 组合是合法的」，
  本页一个字都没有**——本页只有 API 侧的参数与取值。
- **`setResultGranularity()` 正文里指的 `Retrieving edge information by repeating the test`
  （`02.06.11.01.02.02.01`）没读**，所以「重跑失败测试取 edge」那套机制本页没有。
- **本篇自己没有 `#### Subtopics` 段**（本页查过：`#### Subtopics` 出现 0 次）——
  它的出口是正文里那几条链接，**全部没读**。
- **一个图都没有。** 本篇里 `![` 出现 **0 次**（本页查过），**所以这一页不含任何图证，也不缺**。
  （⚠️ 对照：[[mapping-results]] 那页关于 `Result Mode` 页签的名字**是图证**——
  那些图在 `02.08.04.08.04*` 里，**不在本篇里，本页没看那些图**。）
- **一处代码没跑、一个 API 没调。** `verified: doc-only` 指的就是这件事（§11：文档里有 ≠ 这台机器上能用）。
  **尤其：`enable()` 之后到底哪些设置会互相冲突，本篇只说系统会接受，本页没有实机依据。**
- **本篇没有 `## Procedure` / `## Before you begin`**，也没有一条命令行、一个错误码。
- **没有 `## Errors` / `## Warnings` 段**，所以本页**没有「报错条件」节**——
  不是漏写（骨架里本来就没有这一节），是语料没有。
- **`layer: L2` / `stage: results` 不是本篇写的**——本篇没有 `## Application` 这类自我定位段，
  这两个值是本 wiki 的既有划分（`L2` 的依据见 `## 和谁有关` 里 [[testmethod]] 那一条）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **`setResultStorageLocation()` 那句把作用对象写成了 `pins`。** 逐字：
> `This member function defines the storage location of the results for the specified pins.`
> ——**同一个函数的参数表里写的是 port**（逐字：`The port for which the storage location is to be defined. The default is @@, which stands for all ports.`），**函数名也是按 port 取的**。
> **`pins` 与 `port` 在同一节里并存，原文如此。本页不替它改。**
> （本条另有一个更硬的旁证：**这个函数的签名里参数名叫 `resultWidth`**——见 ②。）
>
> ② **`setResultStorageLocation()` 的签名里，形参名是整个函数名的重复、而且是错的。** 逐字：
> `void setResultStorageLocation( const ResultStorageLocation& resultWidth, const STRING& portName = "@@" );`
> ——**第二个形参的类型是 `ResultStorageLocation`，名字却叫 `resultWidth`**，
> 而它下面参数表里的行头写的是 `resultStorageLocation`。
> **`resultWidth` 是隔壁 `setResultWidth()` 的参数名。本页照原样引，不替它改。**
>
> ③ **一句里的 `a all`。** 逐字（`ErrorOnRequest` 那一条的末句）：
> `In this case again, the channels, pins, and sites of a all channel groups on which recording was aborted will be reported.`
> ——**`a all` 多了一个冠词**（同节 `ErrorImmediate` 那条写的是 `of all channel groups`，没有 `a`）。
>
> ④ **第三个取值的名字与另外两个不同风格。** 逐字并列（同一个小节里）：
> `RESULT_CONFIGURATION::ErrorImmediate :` / `RESULT_CONFIGURATION::ErrorOnRequest :` /
> `RESULT_CONFIGURATION::failOnRequest :`
> ——**前两个是以 `Error` 开头的大驼峰，第三个是小写 `f` 开头的 `failOnRequest`。**
> **§11 说「命令大小写敏感、原样保留」，所以本页照抄 `failOnRequest`；这一处不对称原文没有说明。**
>
> ⑤ **`setNumberOfResultsPerCycle()` 的形参名与参数表对不上。** 逐字（签名）：
> `void setNumberOfResultsPerCycle( const NumberOfResultsPerCycle& xMode, const STRING& portName = "@@" );`
> ——**形参叫 `xMode`**，而它下面参数表的行头是 `numberOfResultsPerCycle`，
> 构造函数那一边用的也是 `numberOfResultsPerCycle`。**`xMode` 只在这一处出现。**
>
> ⑥ **同一节里 `internal Error Map` 与 `internal error map` 两种写法并存。** 逐字并列：
> `Results are stored in the internal Error Map. The internal Error Map is located inside the test processor.`
> 与 `This member function retrieves the pins whose results are stored in the internal error map although they belong to a port whose storage location is set to the external memory.`
> ——**后者两个词全小写。本页照原样并列。**
>
> ⑦ **`## Example` 那段代码里，同名变量被声明了两次。** 逐字（同一段代码里的两行，完全相同）：
> `STRING exceptionPins("pin1,pin2");`
> ——**第一处属于 `config1` 那一段，第二处属于 `config2` 那一段**（那两行之间隔着
> `RESULT_CONFIGURATION config1;` 与 `config1.enable();`）。**整段当成一个编译单元是通不过的。**
>
> ⑧ **`setResultWidth()` 那一句里两种数字写法混用。** 逐字：
> `This member function defines the width of the result, 1 bit or two bits.`
> ——**`1 bit` 用数字、`two bits` 用英文单词**，同一句里两套写法。
>
> ⑨ **成员函数的标题行前都粘着一个孤立的 `|`。** 逐字并列（`## Member functions` 一节）：
> `   |   Member functions` 与 `   |  getMultipleExecutions()`
> ——**`|` 本来属于上一张被压平的参数表**，压平之后留在了下一段的行首。
> 同样的形态在 `## Class definition` 一节里也有（参数表以 ` | portName  | The port for which the result configuration is to be defined. |` 起头，
> 表外还有一行整行只有一个 ` |`）。
> **本页按字段重排成表格的是「本页的转述」；要看原样，看 `## 语法 / 参数` 节。**
>
> ⑩ **`## Example` 那段代码的注释里有多余空格与单复数不一致。** 逐字并列：
> `// Pins excepted from the above  storage locations settings:`（`above` 后**两个空格**、
> `locations` 与 `settings` 都用复数）与 `RESULT_CONFIGURATION  defaultConfig;`（类名后**两个空格**）。
>
> ⑪ **`Constructor` 与 `Usage` 都是「带前导空格、没有标题标记」的裸行。** 逐字：
> `  Constructor`（两个前导空格）与 ` Usage`（一个前导空格）——
> 成员函数的每个小标题也是这个形态（如 `  enable()`）。
> **所以本篇在 markdown 里其实没有 `###` 级标题**，是这些裸行在充当小标题。
>
> ⑫ **本篇没有 §11.2 ① 那种编码损坏**（本页查过：全文汉字 **0** 个、`鈥` **0** 处、
> 非 ASCII 字符 **0** 个）。

`verified: doc-only`
