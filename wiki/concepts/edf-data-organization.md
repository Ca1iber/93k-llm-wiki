---
type: concept
title: EDF data organization
layer: n/a
stage: results
tags: [results, data-logging, edf, binary-format, data-log-stream]
related: [edf, edf-data-types, data-retrieval-library, data-logging-profiles]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.06.01_EDF_data_organization.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# EDF data organization

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**这一页讲 event 与 attribute 数据在 data log stream 里怎么排。** 原文把读者钉得很准：

> 「This section describes how event and attribute data is organized. This background information is helpful for writing your own data logging tools that access the data stored in the data log stream.」

**读者是「要自己写工具去读 data log stream 的人」**——
**这是给解析器作者看的背景知识，不是给人看日志用的。**

### 三层嵌套：流 → event record → attribute record

> 「Whenever a new event occurs during the execution of a production test, a new event record (which holds the complete data for that event) is written to the data log stream. The data log stream thus consists of a series of event records. As every event is characterized by a number of attributes, every event record contains a set of attribute records.」

| 层 | 是什么 | 由什么组成 |
|---|---|---|
| **data log stream** | 整个流 | **一串 event record**（`a series of event records`） |
| **event record** | **一次 event 的全部数据** | header + **一串 attribute record** |
| **attribute record** | 一条 attribute | header + body |

> 「Both records consist of a header section and a body section.」

**「为什么是二进制」原文也交代了：**

> 「For performance reasons, the data log information is written to the data log stream in a binary format. This allows fast and compact data logging.」

**`For performance reasons` + `fast and compact`**——**这就是「为什么要拿工具去解、不能直接看」的原文答案。**

### event record 的 header：两个字段，定长

| 字段 | 长度 | 装什么 | 原文（要点） |
|---|---|---|---|
| **Record Length** | **4 字节** | **event record body 的长度** | `This is needed to find the beginning of the next event record.` |
| **Event Type** | **2 字节** | **event 的符号名**，定义在头文件 `dcl_drl.h` 里 | `holds the symbolic name of the event as defined in the header file dcl_drl.h` |

**body = 一串 attribute record**，而**这一串的长短是变的**：

> 「The number and the types of attribute records depend on the type of the event.」

**这句话对写解析器的人是硬约束**：**光有 Record Length 只能让你跳到下一条，要解释 body 里的内容必须按 event 类型分支。**

### attribute record 的 header：字段名和上面**一模一样**，长度也一样

| 字段 | 长度 | 装什么 | 原文（要点） |
|---|---|---|---|
| **Record Length** | **4 字节** | **attribute record body 的长度** | `This is needed to find the beginning of the next attribute record in the event record body.` |
| **Attribute Type** | **2 字节** | **attribute 的类型**，原文举的例子是 `DeviceAttrType` | `holds the type of the attribute, for example, DeviceAttrType.` |

**body = 按 attribute type 解释的数据**（`The body section holds the attribute data according to the attribute type.`）。

**两级 header 是同一个模子**：**都是「4 字节长度 + 2 字节类型」，而且那句 `This is needed to find the beginning of the next …` 在两级各写了一遍**
（一级是 `next event record`，一级是 `next attribute record in the event record body`）。
**所以「怎么遍历」这件事，原文其实用同一句话教你两遍**（**（推断）**：这就是本页最省事的读法——
**先按 4+2 跳过、再回头解释**；原文没有把这条读法写成一句话）。

### 怎么读：用 Data Retrieval Library（DRL）

> 「If you want to access data in the data log stream, you can use the functions of the Data Retrieval Library, which runs on Linux only.」

| 事实 | 原文 |
|---|---|
| **只在 Linux 上跑** | `which runs on Linux only` |
| **能读二进制流** | `The DRL functions let you read data from the binary data log stream.` |
| **还给你一整套类型** | `The library also provides a full set of data types to hold and process all the data read.` |

**两条访问数据时必须记住的全局设定：**

| 项 | 原文 |
|---|---|
| **字节序** | `Note that little-endian byte order is used, that is, the least significant byte is stored first, which is the native Intel x86 byte order.` |
| **类型定义在哪** | `The available event and attribute types are defined in the header file /opt/hp93000/soc/com/include/dcl_drl.h.` |

**注意 `dcl_drl.h` 在原文里出现了两次，两次写法不同**：
`Event Type` 那一格写的是**光文件名** `dcl_drl.h`，
DRL 这一段写的是**全路径** `/opt/hp93000/soc/com/include/dcl_drl.h`。
**两处本页都照原样留着**（见 `## 出处` ⚠️②）。

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`。** 能确定下来的只有四条：

1. **先决定要不要自己解。** 原文的定位对象是「写自己的 data logging 工具」的人，
   而它给出的正路是现成的库：`you can use the functions of the Data Retrieval Library`——
   **要读流里的数据，先考虑 DRL**（**原文只说「可以用」，没说「必须用」**）。
2. **要自己解，就按两级 header 走**：
   **读 4 字节 `Record Length` → 定位下一条**；**读 2 字节类型字段 → 决定 body 怎么解释**。
   **两级字段同名同长，这是遍历的全部依据。**
3. **字节序固定**：little-endian（最低有效字节在前）。
4. **类型名去 `/opt/hp93000/soc/com/include/dcl_drl.h` 查**——
   **可用的 event 类型和 attribute 类型都定义在那里。**

**两条原文给的边界，决定了「什么时候必须分支」：**

| 边界 | 后果 |
|---|---|
| **attribute record 的数量和类型随 event 类型变** | **解析器必须按 event type 分支**，不能一套代码走到底 |
| **DRL 只在 Linux 上跑** | 在别的平台上想读这个流，**就得自己解**（**（推断）**：依据就是 `runs on Linux only` 这一句加上整篇「怎么写自己的工具」的定位） |

**原文的 `## Related information` 只有两条**：`Event types` 与 `Attribute types`——**本页两条都没读**。
**原文没有 `## Example` 段**，所以**一个可运行的解析例子都没有**。 
**原文也没有 `## What to do next`。**

## 和谁有关

- [[edf-data-types]]（**未建**，与本页同批建）— **配套页**：**字段本身怎么解释**（`char` / `int` / `real` 各几字节、有符号还是无符号）那一页有；**本页只讲「记录怎么排」**。
  **这一条是（推断）**：两篇同属 `02.10.01.06`、标题成对，**本页原文没有提它**
- [[edf ]] — **父概念**（**同样只是命名与归属相邻，（推断）**）：
  **本页正文里一次都没有出现 `EDF` 这个词**——它只在标题和文件名里（见 `## 出处` ⚠️①）
- [[data-retrieval-library ]] — **原文点名的正路**：读流里的数据用它的函数；
  **它只在 Linux 上跑**。**本页没读它那篇**，所以**函数名、调用方式、怎么拿到流，本页一概没有**
- `Event types`（**未建，且不在本 wiki 的建页清单里**）— 原文 `Related information` 第一条；
  **`Event Type` 那 2 个字节里装的符号名清单在那儿**，**本页没读**
- `Attribute types`（**未建，且不在建页清单里**）— 原文 `Related information` 第二条；
  **`Attribute Type` 那 2 个字节的取值清单在那儿**（原文举的 `DeviceAttrType` 也是那里的），**本页没读**
- [[data-logging-profiles]]（**已建**）— `Data Logging Profiles` 总览页，
  同属 `results` 阶段（**只凭归属相邻，（推断）**），**本页原文没提它**。
  （原先这里链的是单数名的那个 wikilink（`data-logging-profile`）——**它永远不会被建**，
  见 [[data-logging-profiles]] 页里那条说明。
  **这里故意不把那个名字写成双方括号**：本库第八类把代码跨度里的 wikilink 也算作链接。）

## 版本

原文**有** `## Functional changes`，两条：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.2.0**：`Changed byte order to little-endian`

**① 第一条是哨兵值，不是「6.3.2 引入」。** 本 wiki 里 `Introduced before SmarTest 6.3.2`
的写法意思是「**在本文档集覆盖范围开始之前就已经有了**」（schema §11.2 ②）——
**照字面读会读成「6.3.2 新增了这套记录结构」，那是假的。**

**② 第二条是这一页最该记住的版本事实：字节序有门槛。**
`Changed byte order to little-endian` —— **「改成」little-endian 意味着 7.2.0 之前不是**。
**但原文没有写之前是什么字节序**——**本页不猜**。
（**（推断）**：正文那句把 little-endian 称作 `the native Intel x86 byte order`，
**读起来像是在解释「为什么改」**，但**原文并没有把因果写出来**。）

**③ 对本页的直接影响**：**正文里那条字节序说明（`Note that little-endian byte order is used …`）
描述的是 7.2.0 及之后的流**——
**读 7.2.0 之前的数据日志时，不能照这篇的字节序说明去解**（**（推断）**，依据就是 7.2.0 那条变更记录）。

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.01.06.01_EDF_data_organization.md`

**本页没做的**：

- **有一张图，本页没看**：原文里有一张
  `Data organization in the data log stream`（raw: `34648.png`）——
  **它画的正是 event record 与 attribute record 的内部结构**。
  **所以本页关于「两层 header 各两个字段」的说法全部来自文字描述，没有一个字节是对着图核过的**；
  **图里还有没有文字没提到的字段，本页不知道。**
- **`Event types` 与 `Attribute types` 两篇没读**——
  **所以事件和属性各有哪些类型、符号名怎么写、`DeviceAttrType` 是什么，本页一个字没有。**
- **`Data Retrieval Library` 那篇没读**——**函数名、头文件怎么引、怎么把流喂给它，本页给不出**。
- **`dcl_drl.h` 没有打开**（本机也没有）——**所以那些类型名和结构体，本页只是转述原文提到的名字。**
- **没有 `## Procedure` / `## Before you begin` / `## Example`**，
  **也没有写过一行解析代码、没有跑过 DRL**——`verified: doc-only` 指的就是这件事。
- **一个字节的小端/大端都没有实测过**，**Record Length 是 4 字节、Type 是 2 字节这两个数只来自文字。**
- **`data log stream` 存在哪里、怎么产生、和哪些命令有关，本篇没说**——
  **本页也没去找**。
- **「除了 event record 和 attribute record，流里还有没有别的记录」，原文没说，本页不知道。**

> ⚠️ **本篇的语料瑕疵两处，本页照实记下、一处都没替它改**：
>
> ① **正文里一次都没出现 `EDF` 这个词。** 标题是 `EDF data organization`，
> 而正文第一句写的是 `This section describes how event and attribute data is organized` ——
> **从头到尾用的都是 `event` / `attribute` / `data log stream`**。
> **所以 `EDF` 是什么的缩写，本篇没有说**（**本页正文里因此也不替它展开**）。
>
> ② **同一个头文件在原文里有两种写法**：`Event Type` 那一格写的是光文件名
> `… as defined in the header file dcl_drl.h`，而 DRL 那一段写的是全路径
> `… in the header file /opt/hp93000/soc/com/include/dcl_drl.h`。
> **一处给名字、一处给位置，原文没说哪个是对的、也没说两者是不是同一个文件**——
> **本页不判，两处都照原样留。**
>
> （另：`## Related information` 那两条链接**在原文里是紧贴着的**
> ——`[Event types](…)[Attribute types](…)`，**中间没有分隔符**。
> 形态与同批 `special-test-suites`、两篇 DUT board 图纸页里的「`Note` / `Files of the package:` 粘连」同源，
> **本页把它记在这里，不替原文加分隔。**）

`verified: doc-only`
