---
type: object
title: The V93000 Data Logging Architecture
layer: file
stage: results
tags: [edl-file, datacollection-file, event-data-log, event-stream, dcl, drl, data-logging, stdf, verigy-paper]
related: [data-retrieval-library, event-formatter, smartest-data-formatter, stdf, drldump, report-window, data-logging-profiles, edf, timestamp-attr-type, alphabetical-list-of-flags]
sources:
  - 03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.10.04_The_V93000_Data_Logging_Architecture.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# The V93000 Data Logging Architecture

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**`EDL file` 与 `DataCollection file` 是同一件东西的两个名字**——这是本文自己下的判断，
也是本页唯一可以拿来当定义用的一句。原文逐字：

> 「Since the physical file name of the event stream's implementation has traditionally been
> DataCollection, the terms "DataCollection file" and "EDL file" have become synonymous, in
> practice. The terms are used interchangeably throughout the rest of the document.」

**这一句里有三件事要拆开：**

| # | 原文说的 | 含义 |
|---|---|---|
| 1 | `the event stream's implementation` … `has traditionally been DataCollection` | **event stream 的「实现体」是一个文件；那个文件的物理文件名传统上就叫 `DataCollection`** |
| 2 | `the terms "DataCollection file" and "EDL file" have become synonymous` | **两个词变成同义**（注意原话带 `in practice`——**是「实践中」同义，不是「规范上定义为同义」**） |
| 3 | `The terms are used interchangeably throughout the rest of the document.` | **本文余下部分两个词混用**——所以读这篇时看到哪个都指同一个东西 |

**`EDL` 三个字母展开成 `Event Data Log`**（**不是别的**）。原文逐字：

> 「The main concept of event data logging is the event stream, which contains records coded in
> Event Data Log (EDL) format, illustrated in Figure 2.」

**即：`EDL` 是一种记录格式（`records coded in Event Data Log (EDL) format`），
而 `EDL file` 是「用这个格式写出来的那个文件」**——
**而那个文件在磁盘上的名字传统上叫 `DataCollection`，所以两个名字合流。**

**本页的 `title` 是 `The V93000 Data Logging Architecture`，而 slug 是 `edl-file`**——
**因为这一篇不是「EDL file 的说明」，是一篇讲整个数据记录架构的应用论文**，
`EDL file` 只是它中间一节里被点名定名的一个东西（见 `## 出处` ①）。

### 它在整条链上的位置

**这条链一共五环**（**五环的名字全是本页从原文 `## Event data logging architecture` 一节转述的**）：

| 环 | 名字（**逐字**） | 干什么（**逐字**） |
|---|---|---|
| 1 | `Data Collection Library (DCL)` | **写**：`The API used to write events into the event stream is the Data Collection Library (DCL). Its main responsibility is to synchronize the access of parallel processes to the event stream.` |
| 2 | `event stream` | **中转**：`The event stream forwards the event record to all clients that have subscribed to this particular type of event.` |
| 3 | **`DataCollection file` = `EDL file`** | **落盘**：`At the same time, the events are written to a DataCollection file, which can be saved for external processing.` |
| 4 | `Data Retrieval Library (DRL)` | **读**：`The library that is used to read from the event stream, the Data Retrieval Library (DRL), can also read the event records from DataCollection files.` |
| 5 | formatters | **转格式**：`A number of formatters - tools that translate the data log information into other formats - are delivered with SmarTest. They all utilize the DRL to obtain the event data.` |

**第 3 环就是本页**。
**注意第 3 环在原文的措辞里是「顺带」出现的**——`At the same time, the events are written to a
DataCollection file`——**它和「事件被转发给订阅者」是两件同时发生的事：
一份走内存给实时监控，一份落盘给外部处理。**原文逐字：

> 「Event records are forwarded to all clients immediately after they have been written to the event
> stream. Thus, it is possible to use the data also for real-time monitoring. At the same time, the
> events are written to a DataCollection file, which can be saved for external processing.」

### 文件里装什么

**两层容器**。原文逐字：

> 「Event records themselves are containers for attribute records. The attribute records, such as
> value result attributes or time stamp attributes, are the actual information containers.」

**`event record` 是容器，`attribute record` 才是装信息的那一层**（举例给了
`value result attributes` 与 `time stamp attributes` 两种）。

**两种 record 的结构是同一个套路**，逐字：

> 「Event records and attribute records consist of a header with type and length information and a
> body carrying the binary-encoded data. This format allows the introduction of new event and
> attribute types without interfering with the implementation of a client; the client will just skip
> unknown event and attribute records.」

**「header（type + length）+ 二进制 body」这个设计带来一个性质：
新增 event / attribute 类型不会打断已有 client——client 直接跳过不认识的 record。**
**这也是它替代 GDF 的理由之一**（见下「为什么要换掉 GDF」）。

### 它在哪、什么时候会没

**这是本页最要紧的一节，因为原文把它写成 `## Known drawbacks` 的第一条。** 逐字：

> 「The event stream is implemented as a file. This can have two potentially dangerous
> consequences. First, if not truncated, the file can grow boundlessly and exhaust the file system,
> making it impossible to log further test results. Second, when SmarTest shuts down, the
> DataCollection file is deleted since it is located in the SmarTest session's working directory
> under /var/opt/hp93000/soc/tmp. If the user has the strategy to copy and truncate this file on a
> lot or wafer basis and post-process it, the test results are lost. Although a simple work-around
> of creating a hard link to the DataCollection file to prevent deletion exists today (using the
> Unix command ln), this approach is not well known and the potential loss of the file in the temp
> directory remains a major drawback.」

**落成四条：**

| # | 事实（**逐字**） | 后果 |
|---|---|---|
| 1 | `if not truncated, the file can grow boundlessly and exhaust the file system` | **不截断就会一直长，撑爆文件系统，之后记不了任何结果** |
| 2 | `when SmarTest shuts down, the DataCollection file is deleted` | **SmarTest 一关就删掉它** |
| 3 | `it is located in the SmarTest session's working directory under /var/opt/hp93000/soc/tmp` | **它在 session 的临时目录里**——这是第 2 条的原因 |
| 4 | `a simple work-around of creating a hard link to the DataCollection file to prevent deletion exists today (using the Unix command ln)` | **变通办法是建硬链接（`ln`）**，但原文紧接着说 `this approach is not well known` |

**第 1 与第 2 是并列的两条，不是一条的两面**：一个是「太大」，一个是「会消失」。

**另一条独立的不满**（`## Known drawbacks` 第二条），逐字：

> 「Many end-users are only interested in viewing data collected during specific device executions,
> wafers, or lots. However, since the DataCollection file is a single entity that grows
> continuously, it is not easy to extract such specific production data once the file has reached a
> considerable size.」

**即：它是一个「只增不减的单体」，攒大之后想从里面挑出「某次执行 / 某片 wafer / 某个 lot」
的数据很困难。**（**这一条在 `## Outlook` 里被列为待解决——见下。**）

### 它和 STDF 的关系：**源与下游**

原文 `## STDF considerations` 一节逐字：

> 「Event data logging has been the native logging format of the V93000 platform for many years.
> Despite its advantages, it was never adopted widely as an input format for back-end tools. The ATE
> industry converged to STDF for production data logging, which is acknowledged as the de-facto
> standard. Because of this, the need to log STDF in addition to EDL became apparent.」

**两句话要说清：**

- **EDL 是 V93000 的原生格式（`native logging format`），但没被后段工具广泛接受**；
  行业收敛到 **STDF**（`the de-facto standard`），**所以才有「除了 EDL 还要出 STDF」的需求。**
- **转换的方向是单向的：从 EDL 生成 STDF。** 逐字：

> 「Both tools expect an EDL stream or file as input and generate the corresponding STDF file. It
> should be noted that more information is contained in the EDL file than can be mapped to STDF,
> making the EDL file the ultimate source for extracting additional 93000 specific data log
> information.」

**这一句里有三件本页要单独记住的事：**

| 原文 | 含义 |
|---|---|
| `expect an EDL stream or file as input` | **输入可以是「流」也可以是「文件」**——**EDL 不只以文件形态存在**（这一点与「EDL file = DataCollection file」那句并不冲突：文件只是它的一种落地形态） |
| `more information is contained in the EDL file than can be mapped to STDF` | **EDL 装得比 STDF 能表达的多**——**转成 STDF 会丢信息** |
| `making the EDL file the ultimate source for extracting additional 93000 specific data log information` | **所以要拿 93K 专有的额外数据，EDL 文件是最终来源**（`the ultimate source`） |

### 为什么要换掉 GDF（背景）

**EDL 是被造出来替代 GDF 的。** 原文 `## Historical Background` 逐字：

> 「When SmarTest was released on the HP83000 in the early 90s, the data log was written in a
> tabular ASCII format called the Generic Data Format (GDF). As the devices grew in terms of
> complexity, more and more data was logged. That's when GDF became problematic; the primary target
> audience of GDF, the human reader, couldn't deal with the sheer size anymore. Processing GDF with
> software tools, on the other hand, was extremely difficult for two reasons:」

**两条理由（原文 bullet，逐字）**：

> 「- The tabular format was hard to parse (see Figure 1).」
> 「- Each extension to the format resulted in adjustments to parsers maintained by customers or the field team」

**新架构要满足七条**（原文 `## Historical Background` 的 bullet，逐字）：

> 「- It should be possible to add new data entities without breaking the back-end infrastructure」
> 「- The data log information should be available immediately after it had been written to allow real-time processing, unlike GDF where the file was completed at lot end」
> 「- It should be possible to access the data log through an API to spare the user from having to write tedious parsers」
> 「- It should be possible to process data coming from the tester in real-time, as well as offline using the same tooling」
> 「- It should be easy to translate the format into any other format, for example, STDF or an ASCII format」
> 「- It should be possible to use the same tooling for interactive debug as well as for analyzing production data log files」
> 「- The overhead for data logging should be small and the file should be compact」

**收尾一句原文逐字**：`The result was the concept that is now called event data logging.`

**七条里有两条直接落在「文件」上**：第 2 条（`available immediately after it had been written`，
对比 GDF `the file was completed at lot end`）与第 7 条（`the file should be compact`）。
**其余五条落在 API 与工具链上。**

### SmarTest 6.2 起，这个「文件当事件流」的做法要被换掉

原文 `## Outlook` 逐字：

> 「To resolve the issues related to the file implementation, the file will be replaced starting with
> SmarTest 6.2 in favor of a central process (the event stream srver) that is responsible for the
> event record distribution and optionally logging EDL files for offline processing. Communication
> will go over Unix sockets, where the server distributes the events of interest on-the-fly to each
> of the DRL subscribers, which are typically formatters.」

**⚠️ 这句里的 `srver` 是原文的拼写（少一个 `e`），本页照原样引**（见 `## 出处` ②）。

**要分清的一点：被换掉的是「拿文件当事件流的实现体」，不是 EDL 文件本身**——
**同一句里 `EDL files` 还在**（`optionally logging EDL files for offline processing`）。
**即 6.2 之后 EDL 文件仍然会出现，只是由那个中心进程按策略去写。**

原文列的**四条对比文件实现的好处**（逐字）：

> 「- Processes that are waiting for data are idle and Do not consume processor cycles. With the previous file implementation, the processes had to poll periodically to check whether new events had arrived.」
> 「- Sending event records over Unix sockets is much faster than writing to a file, speeding up the test program execution.」
> 「- The event stream server can be configured to write the DataCollection files to a safe location outside of the SmarTest temp directory, preventing the issue with lost files.」
> 「- The event stream server can apply different policies when writing the events to a file, making it possible to specify how the DataCollection files should be generated. For example, one policy would be to stop writing to a particular DataCollection file every time that a TestProgramEndEvent is received, allowing a one-to-one mapping between a DataCollection file and one test execution. In addition, another policy would be to keep only the last n log files of interest, discarding any older ones to prevent the hard-disk from becoming full.」

**第 1 / 2 / 3 条分别对上 `## Known drawbacks` 的痛点**（轮询、慢、会丢文件）；
**第 4 条正面对上「单体文件挑不出某次执行」那条**——
**`one-to-one mapping between a DataCollection file and one test execution` 就是它的解法。**

### 那四种 formatter（本页只需知道它们都吃 EDL）

原文逐字（`They all utilize the DRL to obtain the event data.` 之后）：

> 「- The Dataformatter generates STDF V4 compliant data log files」
> 「- The Event Formatter is a plug-in to the report window that displays event content in ASCII format」
> 「- The Data Analysis Tool displays the test results in a graphical user interface and allows interactive statistical analysis on the data」
> 「- DRLDump is a simple command line formatter for debugging purposes that writes an ASCII representation of the event and attribute records to a terminal」

**四个都属于上面那条链的第 5 环，都通过 DRL 拿数据**——
**所以它们读的是同一份 event stream，无需各自解析文件。**

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`，也没有一个代码块**
（`## 语法 / 参数` 节已说明：这篇没有 `Syntax` / `Parameters` / `Example` 之类段标记，
所以脚本一个字都不收录）。
**但原文有好几节是「怎么做」的，下面把它们落成动作。**

| 要做的 | 依据（**原文**） |
|---|---|
| **写事件进 event stream** | 用 DCL。**但原文有保留**：`The DCL is primarily reserved for use by internal SmarTest processes; it should only be applied directly when no other logging means (for example, test method API) is available.` |
| **读 event stream / 读 DataCollection 文件** | 用 DRL。`The DRL provides a public C API to attach to event streams, read DataCollection files, decode binary attribute records into C structs or deal with memory management.` |
| **不想自己写 parser** | 同上——`Using this library eliminates the need for end users to write their own parsers.` |
| **要 STDF** | 两个可执行文件：`the legacy hp83_to_stdf formatter` 与 `the new STDF v4 compliant data formatter`；**两者的输入都是 `an EDL stream or file`** |
| **要 ASCII 看内容** | `DRLDump`（调试用，命令行）或 `Event Formatter`（report window 的插件） |
| **要自己的格式** | 直接挂在 DRL 上写自己的 formatter（见下） |
| **不想让文件被删** | 建硬链接（`ln`）——**原文同时说这招 `is not well known`** |
| **不想让它撑爆盘** | 按 lot / wafer 复制并截断——**原文同时说这样 `the test results are lost`（如果没先保住文件）** |
| **控制记多少数据** | 见下「三档配置手段」 |

### 三档配置手段（原文 `## Data logging configuration`）

**原文把「控制记什么」分成三档，顺序是从粗到细：**

| 档 | 手段 | 原文要点 |
|---|---|---|
| 1 | **预定义 flags** | 分布在 `system, testflow, and testsuite flags` 三级；**system / testflow 管整体**（例：`log_events_enable` 管「到底写不写事件」；**`stdf_generation` 从 SmarTest 6.2 起**管「这次执行生不生成 STDF」）；**testsuite flags 管单个 testsuite** |
| 2 | **直接编程 test method** | 逐字点名几个：`TEST()`, `judgeAndLog...()`, `PUT_DATALOG()`, 以及 `the methods of the TESTSET class` |
| 3 | **配置 formatter** | `The STDF data formatter gets its configuration from configuration files; the Event Formatter has a dedicated user interface raised by clicking the report dialog button in the report window's menu bar.` |

**第 2 档里有一条硬警告**，逐字：

> 「It is also possible to call the DCL directly from the test method code if a suitable test method
> API does not exist, which gives the user the ultimate control over the contents of the data log
> stream. However, this is not a recommended practice since the formatters that read from the event
> stream expect events in a certain order and with certain content. A malformed event stream could
> potentially cause the formatters to crash and thus cause loss of data.」

**即：绕过 test method API 直接调 DCL 会把「事件顺序与内容」的责任交给自己，
写坏了会让 formatter 崩、进而丢数据。**

**第 1 档里也有一条**（原文 `## Data logging configuration` 末段的意思）：
**testsuite flags 是 SmarTest 预定义的，有的测试根本用不上**——
逐字见 `## 出处` ⑥ 引的那条 `## Known drawbacks`。

### 性能：原文给了一张表，本页只记它的结论

**原文 `## Performance Considerations` 有 Table 1**（一张 PDF 压平的表，**见 `## 出处` ⑤**），
在一台 `Pin Scale` 系统的微控制器器件上、跑 50 次生产测试程序：

| 配置 | 执行时间（秒） | 额外开销 |
|---|---|---|
| 数据记录完全关（基准） | 137 | -- |
| event data log 开、testsuite flags 全关 | 137 | 0% |
| + output on pass / output on fail | 139 | 1.46% |
| + per pin on pass / per pin on fail | 147 | 7.30% |
| + value on pass / value on fail | 153 | 11.68% |
| + 100 failing cycles (FFC) | 569 | 415.33% |
| + 100 failing cycles + edge results (FRG) | 883 | 544.53% |
| + 100 failing vectors (drive + expected + received) (FFV) | 3943 | 2778.1% |

**两句话读这张表**：

- **`+ output on pass / output on fail` 只花 1.46%**，而失败周期的细粒度记录**涨到 4 倍到 28 倍**。
- **原文明说后三项是工程模式才用的**：`First Failing Cycles and Fine Result Granularity are
  used primarily in engineering mode due to the high cost`（另见 `## 出处` ⑤ 的脚注编号问题）。

**表里那三个缩写 `FFC` / `FRG` / `FFV` 是原文在括号里给出的**，
**但原文正文里用的是另外的词**（`First Failing Cycles` / `Fine Result Granularity` /
`First Failing Vectors`）——**同一件事两套写法，原文没有给对照，本页照实并列。**

### 原文自己的收口

逐字：`It is the responsibility of the test program developer to determine the appropriate level of
data log detail for each test that is executed.`
——**记多少是测试程序开发者的责任，原文不给默认值。**

## 和谁有关

- [[data-retrieval-library]] — **读本页那个文件的那一端**。
  原文逐字：`The library that is used to read from the event stream, the Data Retrieval Library
  (DRL), can also read the event records from DataCollection files.`
  **本页只有这一句与它的三项能力（attach 到流 / 读 DataCollection 文件 / 把二进制
  attribute record 解成 C struct）；DRL 自己的 API 清单本页没有，那一页本页也没读。**
- [[event-formatter]] — **四个 formatter 之一，也是本页那个文件的下游消费者**。
  原文逐字：`The Event Formatter is a plug-in to the report window that displays event content in
  ASCII format`；配置入口是 `clicking the report dialog button in the report window's menu bar`。
  **本页只有这两句，那一页怎么用本页没读。**
- [[stdf]] — **下游格式**。原文把「EDL → STDF」的方向、
  `more information is contained in the EDL file than can be mapped to STDF` 这条信息损失、
  以及 STDF 是 `the de-facto standard` 都写清了。**STDF 自己是什么、v4 的字段本页没有。**
- [[smartest-data-formatter]] — **（推断）可能指原文那个 `Dataformatter`**。
  依据：原文三个地方用三个名字指这个工具——
  `The Dataformatter generates STDF V4 compliant data log files`（`## Event data logging
  architecture`）、`the new STDF v4 compliant data formatter` 与
  `The STDF data formatter gets its configuration from configuration files`（后两处）。
  **原文没有把这三个名字对齐，本页也没有依据断定 [[smartest-data-formatter]] 就是它。
  这是推断，不是文档事实。**
- [[drldump]] — **四个 formatter 之一（命令行、调试用）**。
  原文逐字：`DRLDump is a simple command line formatter for debugging purposes that writes an
  ASCII representation of the event and attribute records to a terminal`。
  **本页只有这一句；原文另有一张图（`Figure 3`，见 `## 出处` ③）画它的 ASCII 输出，本页没看。**
- [[data-logging-profiles]] — **原文点名「SmarTest 6.2 引入」的控制手段**。
  原文逐字：`the new concept of data logging profiles (introduced with SmarTest 6.2)`；
  激活方式是 `via a new drop down combo box in the Operation Control UI, or programmatically via a
  new test method API`。**本页只有「它是什么、怎么激活」两句，
  profile 的语法（原文举了三条规则）本页没有，那一页本页也没读。**
- [[report-window]] — **Event Formatter 的宿主**（`a plug-in to the report window`），
  也是它的配置入口（`the report dialog button in the report window's menu bar`）。
  **本页只有这两处点名，那个窗口本页没读。**
- [[alphabetical-list-of-flags]] — **（推断）本页提到的 flags 的清单可能在那儿**。
  依据：原文点名了 `log_events_enable`、`stdf_generation`、`log_mx_waveform` 三个 flag，
  并说 flags `are distributed over system, testflow, and testsuite flags`；
  **本篇没有列清单，那一页收不收这三个、按什么分类，本页没有依据判断。**
- [[timestamp-attr-type]] — **（推断）本篇点名的 `time stamp attributes` 的对页**。
  依据：原文逐字 `The attribute records, such as value result attributes or time stamp attributes,
  are the actual information containers.`；
  **本篇只有这一个名词短语，attribute 的二进制结构在那篇——
  而那一页本页没读，所以两者是不是同一层的东西，本页没有依据断定。**
- [[edf]] — **（推断）同族，但本页没有依据把两者并成一件**。
  依据只是：本篇把格式叫 `Event Data Log (EDL)`，
  而 wiki 另有一页叫 `Event Data Logging Format (EDF)`——**名字同族**。
  **本篇一个字都没提 `EDF`，那一页本页也没读**——
  **按页名相邻列出，不代表同物**（取材自同一套规矩：[[uptd]] 那页对
  `alphabetical-list-of-flags` 也是这么处理的）。
- `Data Collection Library (DCL)`（**未建、不在 allowlist，故用反引号**）—
  **写那一端**，见上「它在整条链上的位置」第 1 环。
  **原文说它主要留给 SmarTest 内部进程用**，直接调它的条件是
  `no other logging means (for example, test method API) is available`。
- `Data Analysis Tool`（**未建**）— **四个 formatter 之一**，
  `displays the test results in a graphical user interface and allows interactive statistical
  analysis on the data`。**原文没有说它是不是等于 wiki 里的
  [[integrated-result-tool]] 或 [[data-navigation-views]]，
  本页不做这个推断**（**那两个名字本篇一次都没出现过**）。
- `event stream server (ESS)`（**未建**）— **SmarTest 6.2 起取代「文件实现」的那个中心进程**
  （`## Outlook`；**本文正文写的是 `the event stream srver`，见 `## 出处` ②**）。
- `hp83_to_stdf`（**未建**）— 原文点名的 `the legacy hp83_to_stdf formatter`，
  **另一个吃 EDL、出 STDF 的可执行文件**。**原文没有解释 `hp83` 是什么**
  （**（推断）指更早的平台型号**；**依据只是名字，原文没说，这是推断**）。
- `Generic Data Format (GDF)`（**未建**）— **EDL 之前的旧格式**，本篇 `## Historical Background`
  整节讲它。**本页只转述了原文给的取舍理由，GDF 自己的格式本页没有。**
- `TestProgramEndEvent`（**未建**）— **`## Outlook` 举策略例子时点名的唯一一个事件类型**，
  `stopping writing to a particular DataCollection file every time that a TestProgramEndEvent is
  received`。**原文没有解释它什么时候发、由谁发。**

## 版本

**本文档没有 `## Functional changes` 段。**
**但这篇论文正文里有三条与版本有关的事实**（都是 `SmarTest 6.2`）：

| # | 原文（**逐字**） | 说的什么 |
|---|---|---|
| 1 | `the new concept of data logging profiles (introduced with SmarTest 6.2)` | **data logging profiles 从 6.2 起有** |
| 2 | `or, starting with SmarTest 6.2, whether STDF is generated for the current test program execution (stdf_generation)` | **`stdf_generation` 这个 flag 从 6.2 起有** |
| 3 | `the file will be replaced starting with SmarTest 6.2 in favor of a central process (the event stream srver)` | **6.2 起「文件当事件流实现体」被换掉** |

**（推断）这三条说明这篇论文写的年代早于 6.2 发布。**
**依据是第 3 条用的是将来时 `will be replaced`**，而 `## Outlook` 一节的标题就是 `Outlook`
（展望）；**另外原文 `## Summary` 也把它写成「正在进行中的研发」
（`the R&D developments that are currently underway`）。**
**原文没有写论文的日期，所以这是推断。**

**与 wiki 目标版本（SmarTest 7.10.3）的关系**：**本篇最新只到 6.2，
7.x 一条都没有**——**所以 7.10.3 上 `EDL file` / `DataCollection file` 的现状，
本篇没有任何依据。**
**尤其原文把 6.2 当作「将来」讲，那么 6.2 之后文件到底还留不留、
留在哪、叫什么名字，本篇说的都是它写作当时的计划，不是既成事实。**

**⚠️ `SmarTest 6.2` 这个版本在 wiki 里没有版本页**
（allowlist 的 `smartest-*` 里没有 `smartest-6.2`），**所以本页这三条无处可链。**

## 出处

`sources:` 一篇：
`03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.10.04_The_V93000_Data_Logging_Architecture.md`

**这是一篇 10 节的应用论文**（`Abstract` / `Historical Background` /
`Event data logging architecture` / `Performance Considerations` / `Data logging configuration` /
`STDF considerations` / `Known drawbacks` / `Outlook` / `Summary` / `About the Authors`），
署名 `Ryan Lucy, Verigy`、`Gerd Bleher, Verigy`、`Yu Hu, Verigy`，`Paper ID: 105479`。

**本页没做的：**

- **本页讲的是 `EDL file` 这一个对象，而这一篇讲的是整个架构。**
  **所以「是什么」一节里凡是超出「EDL file 是哪个文件、装什么、在哪、和 STDF 什么关系」
  的内容（DCL / DRL / formatter 四个 / GDF 历史 / 性能表 / 配置手段），
  都是本页为了让这一个对象站住而转述的上下文，不是本页的主题。**
- **原文有四张图（`raw/105482.png`、`105484.png`、`105485.png`、`105487.png`），一张都没看。**
  §11.4 说 raw 里的图可读且该读。**其中第 3 张是 `ASCII Representation of binary EDL file using
  DRLDump`——按它的题注，它画的正是本页这个文件的 ASCII 样式，本页没有打开它。**
- **`## Performance Considerations` 正文只被本页取成了那张 8 行表**，
  **表前每一档的解释文字（`Different measurement algorithms and different tester resources` 等
  五条 bullet）本页只转述了与「文件」有关的结论**，其余没有展开。
- **`## Data logging configuration` 里 data logging profile 的三条示例规则**
  （`*leakage* . * . * . datalog_detail = 2` 等）**本页只在 `## 和谁有关` 里点了一句，没有抄录**
  ——**它们属于 [[data-logging-profiles]] 那一页的范围，而那一页本页没读。**
- **原文点名的 test method API 函数（`TEST()` / `judgeAndLog...()` / `PUT_DATALOG()` /
  `TESTSET` 类的方法）本页只列了名字**，**它们各收什么参数、什么时候调，
  本篇没有写，本页也没有**。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：[[data-retrieval-library]] / [[event-formatter]] / [[stdf]] / [[drldump]] /
  [[data-logging-profiles]] 这几页本页一篇都没读**——
  **本页与它们的关系全部取自本篇这一篇的正文，没有从对面回校过。**
- **`EDL` 与 `EDF` 是不是同一个东西，本页没有依据**（见 `## 和谁有关`）。
- **`layer: file` / `stage: results` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 页面 slug 与文档标题不是一回事。** 本页文件名是 `edl-file.md`，
> 而 `title` 与 H1 都是 `The V93000 Data Logging Architecture`——
> **`edl-file` 只是这篇论文里的一个对象，论文本身比它大得多。**
> **本页照实按 `edl-file` 写，并把范围声明放在 `## 出处`。**
>
> **② 三处拼写/语法错误，本页照原样引：**
>
> - **`srver`**（少一个 `e`）：`a central process (the event stream srver)`（`## Outlook`）。
> - **`Libarary`**（应为 `Library`）：`writers access the Data Collection Libarary (DCL)`
>   （`## Summary`）。**同一篇里 `Data Collection Library (DCL)` 在
>   `## Event data logging architecture` 一节是拼对的——两个拼法同篇并存。**
> - **`in the any desired format`**（多一个 `the`）：
>   `end-users can write their own custom formatters to convert the test result content in the any
>   desired format`（`## Summary`）。
>
> **③ 四张图里有一张没人引它。** 正文只出现 `Figure 1`（`## Historical Background`）、
> `Figure 2`（`## Event data logging architecture`）、`Figure 4`（`## Outlook`）——
> **`Figure 3` 一次都没被正文提到**，而图本身在文件里（题注
> `ASCII Representation of binary EDL file using DRLDump`）。
> **同文里 `Figure 4` 被引，那 `Figure 3` 是哪一张，原文没有交代。**
> **另一处：`Figure 1` 是正文里用 `see Figure 1` 指的，与其余两处的 `illustrated in` / 括号写法不同。**
>
> **④ 第一张图被粘在句尾，且它粘在一个 bullet 行上。** 逐字：
> `- Each extension to the format resulted in adjustments to parsers maintained by customers or the
> field team ![GDF File Excerpt](<../../../../raw/105482.png>)`
> ——**图片语法紧跟在 `team` 后面，中间连一个空格都没有**；
> **同篇另外三张图各自独占一行（行首有一个空格）。四张图两种写法。**
> **同一处还有：这条 bullet 的句子以 `field team` 结尾却没有句号，而它前面那条 bullet 有句号。**
>
> **⑤ Table 1 被压平，且脚注编号对不上。** 表里 8 行数据各带一个上标数字
> （`Data log completely off 1` … `(FFV) 8`），**而文末只有 6 段脚注**，
> 逐字开头分别是：`1` / `2` / `3` / **`4 5`** / **`5 7`** / `6`。
> ——**两段脚注各带两个数字，序列是 `1,2,3,4 5,5 7,6`，
> 而表里的标记一直到 `8`；没有一段脚注以 `7` 或 `8` 开头。**
> **同一处还有：表头四格之间是 ` |`，数据行之间夹两到三条 ` |`（与 [[edf]] 那页记的
> 同一个毛病同族）；第一列 `Production` / `Engineering (Debug)` 的分组在压平后只剩一行
> `Engineering` 加一行 `(Debug)`，跨行归并看不出来了。**
> **本页不替它重编号，也不替它猜哪段脚注对应哪个标记。**
>
> **⑥ 句中大写的 `Do`（两处）。** 逐字：
> `some of the flags Do not make sense`（`## Known drawbacks` 末条）与
> `Processes that are waiting for data are idle and Do not consume processor cycles.`
> （`## Outlook` 第一条）。**两处都在句子中间，`Do` 却大写**——
> **原文这样，本页照引，不改成 `do`。**
>
> **⑦ 编码损坏一处（§11.2 ①）。** 逐字：
> `- Joined the B枚blingen Instrument Division of HP in 1994.`（`## About the Authors`）
> ——**`B枚blingen` 里的 `枚` 是坏字：它的 GBK 字节 `C3 B6` 按 UTF-8 读就是 `ö`，
> 所以原文是 `Böblingen`**（德国城市，与作者单位相符）。
> **本篇正文其余部分没有坏字**（本页查过：汉字共 1 个，就是这一个；`鈥` 0 处）。
> **按 §11.2 的处置：本页引文照原样留着坏字，并在这里说明它本来是什么**——
> **拿 `Böblingen` 去 raw 里搜是搜不到的，要搜 `B枚blingen`。**
>
> **⑧ 三处指代同一个工具的三种名字。** 逐字并列：
> `The Dataformatter generates STDF V4 compliant data log files`（`## Event data logging
> architecture`）/ `the new STDF v4 compliant data formatter`（`## STDF considerations`）/
> `The STDF data formatter gets its configuration from configuration files`
> （`## Data logging configuration`，原句在分号处断，本页截到分号）。
> ——**`Dataformatter`（连写、首字母大写，像专名）、`data formatter`（分词）、
> `data formatter`（同一段里又写成 `the STDF data formatter`）；
> 而 `## STDF considerations` 里那个是 `an executable`、`## Data logging configuration` 里那个
> 有配置文件，原文没有说这是不是同一个程序。本页照实并列，不替它统一。**
>
> **⑨ 论文自称 `V93000`，署名却是 `Verigy`。** 三行署名逐字：`Ryan Lucy, Verigy` /
> `Gerd Bleher, Verigy` / `Yu Hu, Verigy`。**正文里 `V93000` 与 `HP83000` 混用**
> （`# The V93000 Data Logging Architecture` 对 `When SmarTest was released on the HP83000 in
> the early 90s`）。**这是本文的写作年代痕迹，不是错字；本页照实记。**

`verified: doc-only`
