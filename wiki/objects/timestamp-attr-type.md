---
type: object
title: TimeStampAttrType
layer: file
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.06.05.65_TimeStampAttrType.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# TimeStampAttrType

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **485 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.06.05.65_TimeStampAttrType.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Field Name | Data Type | Description | Comments |
|---|---|---|---|
| length | int | Attribute length | These fields form the attribute header. |
| type | short | Attribute type | These fields form the attribute header. |
| secs | int | Seconds | Number of seconds and microseconds that passed since 01/01/1970 (standard time measurement in Linux) |
| usecs | int | Microseconds | Number of seconds and microseconds that passed since 01/01/1970 (standard time measurement in Linux) |

<!-- 语法节 end -->

## 是什么

**它是 EDF 数据里的一个属性类型（attribute type），装着「事件发生的时间」。**
原文全文只有一句定义：

> 「**Contains the time when an event occurred.** The data type is `DRLTimeStampAttr`.」

**四个字段，分两组：**

| 字段 | 类型 | 原文 Description | 原文 Comments |
|---|---|---|---|
| **`length`** | `int` | Attribute length | **These fields form the attribute header.** |
| **`type`** | `short` | Attribute type | （同上） |
| **`secs`** | `int` | Seconds | **Number of seconds and microseconds that passed since 01/01/1970（Linux 标准时间）** |
| **`usecs`** | `int` | Microseconds | （同上） |

> ⚠️ **上表最后两列的跨行是本页加的，原文的表是合并单元格。**
> 语料里这张表被压平成一维，**`These fields form the attribute header.` 看起来只属于 `length`、
> `Number of seconds and microseconds…` 看起来只属于 `secs`**——
> **不是的**：前者管的是 **`length` + `type` 两行**（头两个字段构成属性头），
> 后者管的是 **`secs` + `usecs` 两行**（两者合起来才是完整时间戳）。
> **本页按语义把它们摆回跨行位置，一个字没有增删。**
> **这个摆法是本页的判断，原文的形态是压平的**——两处都留在这里，谁要核都能核。

**时间基准**：**`secs` + `usecs` 两个数合起来，是从 `01/01/1970` 起经过的秒与微秒数**，
原文括注 `（standard time measurement in Linux）`。
**这是 Unix epoch**——原文没有写「epoch」这个词，**本页也不替它引入**。

## 典型用法

**1. 什么时候用它**：**解析 EDF 数据**、或要把日志里的时间戳还原成绝对时间时。

**2. 读法**：**先读 `length` 和 `type` 定位到这条属性，再读 `secs` / `usecs`。**
**不要只看 `secs`**——它不含微秒部分。

**3. 它是「属性类型」不是「记录」**：原文说它 `Contains the time when an event occurred`，
**但没说这条属性挂在哪些事件上**。**本页不知道**（见「出处」）。

## 和谁有关

- [[edf-data-types ]] — 原文 `Related information` 第一篇；
  本页只是这一族里的**一个**属性类型
- [[edf-data-organization ]] — 同上第二篇；
  属性在 EDF 里的组织方式在那边
- `DRLTimeStampAttr`（**未建**）— **本页的数据类型指向它**；
  **它是什么、和本页什么关系，原文只说了 `The data type is …` 这一句**
- [[results]] — 本页 `stage: results` 的理由：EDF 是数据日志侧的东西
- `layer: file` 的理由：它描述的是**数据文件里的字段结构**，不是代码、不是界面

## 版本

- **`Introduced before SmarTest 6.3.2`**（原文就写了 `before`，**没给准确版本**）

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.01.06.05.65_TimeStampAttrType.md`

**本页没做的**：

- **这篇文档只有 945 字节——一句话、一张图、一张四行的表、两条链接。**
  本页把它**全部**转述了；**但它没有的东西，本页一个字都补不出来**：
  - **`DRLTimeStampAttr` 是什么**（只知道是这个字段的数据类型）
  - **这条属性出现在 EDF 的哪些位置、一个记录里有几条**
  - **`length` / `type` 的取值怎么算**（原文只说 `Attribute length` / `Attribute type`）
- **一张图没看**（`97768.png` 的 `TimeStampAttrType structure`）。
  **上面那张表本页只用了原文的文字**，**没有任何来自图的结论**。
- **`Related information` 那两篇一篇都没读**：
  `EDF data types`、`EDF data organization`。
- **`02.10_Data_Logging` 底下其余篇本页没读。**

`verified: doc-only`
