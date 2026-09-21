---
type: concept
title: EDF data types
layer: n/a
stage: results
tags: [results, data-logging, edf, data-types, binary-format]
related: [edf-data-organization, edf]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.06.02_EDF_data_types.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# EDF data types

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**这一页只有一件事：一张表，列出 event data logging 用的基本数据类型。** 原文全文开头就是：

> 「The table below describes the data types used for event data logging.」

**紧跟着是唯一的全局设定：**

> 「Little-endian byte order is used; the least significant byte is stored first.」

**所以这一页的性质很明确**：**它是「查表页」——查某个类型几字节、有没有符号**，
**不是「怎么用」的页**（见 `## 典型用法`）。

### 九个类型，一字不改地列在这里

| 类型 | 原文的描述 | 宽度 | 符号性 |
|---|---|---|---|
| `char` | `one-byte signed integer` | **1 字节** | **有符号** |
| `short` | `two-byte signed integer` | **2 字节** | **有符号** |
| `int` | `four-byte signed integer` | **4 字节** | **有符号** |
| `long long` | `eight-byte signed integer` | **8 字节** | **有符号** |
| `unsigned char` | `one-byte unsigned integer` | **1 字节** | **无符号** |
| `unsigned short` | `two-byte unsigned integer` | **2 字节** | **无符号** |
| `unsigned int` | `four-byte unsigned integer` | **4 字节** | **无符号** |
| `real` | `eight-byte floating point number in the IEEE 754 format` | **8 字节** | **浮点**（原文未提符号） |
| `string` | `null-terminated string` | **原文未给** | **变长** |

### 这张表里三处值得单独看一眼的地方

**① 整数是有符号 4 档、无符号 3 档——不对称。**

| | 1 字节 | 2 字节 | 4 字节 | 8 字节 |
|---|---|---|---|---|
| **有符号** | `char` | `short` | `int` | **`long long`** |
| **无符号** | `unsigned char` | `unsigned short` | `unsigned int` | **（表里没有）** |

**表里没有 `unsigned long long`**——**原文没有解释这个不对称，也没有说 8 字节无符号整数该怎么表达。**
**本页不替它补。**

**② 两个 8 字节类型：一个整、一个浮点。**

`long long`（8 字节有符号整数）和 `real`（8 字节 IEEE 754 浮点）**宽度相同、解释完全不同**——
**这一条对读二进制流的人是关键的**：**同样是 8 个字节，读成整数还是浮点，得看类型。**

**③ 表里没有 4 字节浮点。**

九个类型里有整数 1/2/4/8 字节四档，**浮点却只有 `real` 一种（8 字节）**——
**没有 `float`**。**原文没说这是「不支持」还是「没列出」。**

**另外一处需要点明的**：**`string` 是唯一不给字节数的类型**——
原文只写 `null-terminated string`（以空字符结尾的字符串），**所以它的长度只有到读的时候才知道**
（**（推断）**：由 `null-terminated` 这个定义直接得出）。

### 这份表的边界

**原文对这张表只有两句说明**（开头那两句），**此外什么都没有**：

| 原文有没有说 | 说明 |
|---|---|
| 这些类型用在 event data logging 上 | **说了**（`the data types used for event data logging`） |
| 字节序 | **说了**（little-endian，最低有效字节在前） |
| **哪个字段该用哪个类型** | **没说** |
| **这些类型是 C 的类型还是自造的别名** | **没说**（**类型名长得像 C，但原文没有说它们就是 C 的类型**——**本页不推**） |
| **`real` 之外的浮点、字符串的编码** | **没说** |

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## Example`。**
**这一篇本身就不含用法**——它是一张参照表，**用法只能是「查」**：

1. **手上有了一段二进制数据，要按字节解释它** → **先看这张表**：
   **名字决定宽度（1/2/4/8）、名字里的 `unsigned` 决定有没有符号。**
2. **多字节类型一律按 little-endian 读**（`the least significant byte is stored first`）。
3. **遇到 8 个字节要分清是 `long long` 还是 `real`**——**两者宽度一样，解释不一样。**

**三条必须说清的「本页给不出」**（都是原文的缺口，不是本页的疏漏）：

| 你要的 | 本页能不能给 |
|---|---|
| **这些类型用什么语法写**（声明、读写的 API） | **给不出**——原文只有名字与描述 |
| **它们出现在记录的哪个位置** | **给不出**——本页原文只把它们和 `event data logging` 关联起来，**没有提任何字段名或结构** |
| **`real` 的精度、字节序对小端浮点的具体影响** | **给不出**——原文只说了 IEEE 754 与 little-endian 两句 |

**原文的 `## Related information` 只有一条**：`EDF data organization`——
**原文这一句就是本页唯一一条出边**（**那篇本页没读**，见 `## 出处`）。

## 和谁有关

- [[edf-data-organization]]（**未建**，与本页同批建）— **配套页，而且是原文自己指的**：
  本页 `## Related information` 那一条就是它。**本页给类型，它给「记录怎么排」**；
  **两页各自独立，本页没有从它那里取任何内容**（见 `## 出处`）
- [[edf ]] — **父概念**。**这一条是（推断）**：
  两篇同属 `02.10.01.06` 一组、标题都带 `EDF`，
  **但本页原文除了标题之外没有出现 `EDF`，也没有提任何父概念**——**所以这只是命名上的归属**
- `EDF data organization` 之外的相关篇（`Event types`、`Attribute types`、`Data Retrieval Library` 等）
  **本篇一条都没提**，**本页也不从别页引进它们的名字**——
  **凡本页没写的名字，就是本篇原文没给的。**

## 版本

原文**有** `## Functional changes`，两条：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.2.0**：`Changed byte order to little-endian`

**① 第一条是哨兵值，不是「6.3.2 引入」。** 本 wiki 里 `Introduced before SmarTest 6.3.2`
的写法意思是「**在本文档集覆盖范围开始之前就已经有了**」（schema §11.2 ②）——
**照字面读会读成「6.3.2 新增了这些数据类型」，那是假的。**

**② 第二条决定这张表怎么用**：`Changed byte order to little-endian` ——**「改成」意味着 7.2.0 之前不是**，
**但原文没有写之前是什么**，**本页不猜**。

**③ 这条变更对本表的影响范围（（推断））**：本表里除 `char` / `unsigned char` 之外的七个类型
**都是多字节的**，所以**字节序这条变更对它们全都成立**——
**依据是正文那句 `Little-endian byte order is used` 是整篇的总述，没有把任何类型排除在外**；
**原文并没有逐类型说这件事。**

**④ 一处对不上的地方**：本表的九个类型**在版本记录里一个都没被点名**——
**两条变更记录说的都是「这套记录/字节序」，没有一条说「新增了某个类型」**。
**所以这九个类型是哪个版本齐的，本篇答不了。**

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.01.06.02_EDF_data_types.md`

**本页没做的**：

- **一张图都没有，也没看图**——本篇正文里**没有插图**，**所以本页没有任何来自图的结论**。
- **`EDF data organization` 那篇没读。** 它是原文 `Related information` 唯一指的一篇，
  **但本页不从它取内容**——**按本工程的规矩，一页只写自己 `sources` 里的那几篇**。
  **所以「这些类型用在记录的哪个字段」本页一个字都不给**，**那不是本页的依据范围。**
- **没有 `## Procedure` / `## Before you begin` / `## Example`**——
  **本篇除了一张表、两句说明、两条版本记录之外，没有别的段落。**
- **没有写过一行解析代码，没有实测过任何一个字段的宽度或符号性**——
  **表里的 1/2/4/8 字节、`signed` / `unsigned` 全部来自原文描述文字**；
  `verified: doc-only` 指的就是这件事。
- **`string` 占几个字节、编码是什么，原文没说，本页也没查。**
- **这些类型名是不是 C 语言的原生类型，原文没说，本页不推。**
- **`real` 的实际精度、byte order 对小端浮点的具体表现，原文没说。**

> ⚠️ **本篇的语料瑕疵两处，本页照实记下、一处都没替它改**：
>
> ① **正文里一次都没出现 `EDF` 这个词。** 标题是 `EDF data types`，
> 而正文写的是 `the data types used for event data logging` ——
> **`EDF` 只在标题和文件名里出现。所以它是什么的缩写，本篇没有说**
> （**本页正文因此也不替它展开**）。
>
> ② **这张表在原文里是被拍平的**：表格被拆成「一格一行」，
> 单元格分隔符 ` |` 自己占一行，标题行 `Type` / `Description` 也各占一行
> ——**形态和 `tpt_generate_device_dir` 那页的参数表完全一样**。
> **本页把内容按表重新排了一遍：那是转述，不是引文**（原文里没有这种排版）。
>
> （另：原文那张表前面只有一行 `Data type descriptions` 作为引语，
> **它和表格之间没有空行**，**原文没有把它写成 `## ` 段标题**——原文如此。）

`verified: doc-only`
