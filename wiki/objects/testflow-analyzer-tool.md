---
type: object
title: The Testflow Analyzer Tool (TAT)
layer: L3
stage: project
tags: [project, licensing, device-license-file, hardware-definition-file, model-file, command-line-tool, testflow]
related: [project, testflow, testflow-file, model-file, technology-file-for-a-device, device-license-file]
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07_The_Testflow_Analyzer_Tool__TAT.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# The Testflow Analyzer Tool (TAT)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**TAT 回答的是「这套 testflow 最少需要买哪些 license」。** 它是个**命令行工具**，
输入是一个**已加载的 testflow** 加一份**硬件描述**，输出是一个 device license file。

> 「With the TAT you can generate device license files (DLF) for every hardware combination to determine the required license minimum. This information you can use to optimize your license usage.」

**它是「按硬件组合逐个算」的工具**——原文那句 `for every hardware combination`
说明用法是**换一种硬件组合就再算一次**，比出来的最小值就是你要买的量。

> 「The TAT generates a device license file (.licenses) based on the given testflow and the hardware definition file (HDF) or model file.」

（同一个东西，原文两种叫法：正文叫 device license file（DLF），扩展名 `.licenses`。
本页把它们当一件事，**这是本页的合并，不是原文的一句声明**。）

**输入里的硬件描述有两个来源，二选一**：

| 来源 | 原文怎么说 |
|---|---|
| **HDF**（hardware definition file） | 「The hardware definition file describes the hardware of your tester (type, cards, memory mode).」 |
| **model file** | 原文只说它和 HDF 一样能当输入，**没有再说它是干什么的**（那一篇是 `model-file`，本页没读） |

**一条依赖**：

> 「TAT is a command line tool. Some of its optional parameters require the installation of a line model encrypted database (smartest_aslmedb*).」

**即：只给必填参数跑得起来；要用某些可选参数，得先装那个加密数据库。**

### 产物：一份「最低配置」清单 + 四个用量计数

> 「The testflow analyzer tool (TAT) analyzes the testflow and generates a device license file (.licenses) in the current directory. The generated device license file lists only the minimum needed capabilities for the given testflow.」

**注意 `in the current directory`**——产物落在**你敲命令时所在的目录**，不是 device 目录。

除了清单本身，**它还顺带报四个计数**：

> 「Note TAT does not change and optimize the technology file, see Optimizing the technology file, but provides the number of used sets:」

> 「The Testflow Analyzer tool (TAT) provides the number of sets used by the current device in a comment section:」

四个计数是 `Level sets` / `DPS sets` / `Wavetables` / `Timing sets`，写在**文件里的一个注释段**，
原文给的例子逐字如下（**这是文档给的示例数字，不是你机器上的数**）：

```
################################################
# #
# Number of sets used by this device: #
# Level Sets: 220 #
# DPS Sets: 79 #
# Wavetables: 128 #
# Timing Sets: 726 #
# #
################################################
```

**而且「不改 technology file」是它明说的一句**：
它**只报数**，优化 technology file 是另一件事、另一篇文档（见「和谁有关」）。

### 它**不**列的三样功能

> 「TAT will not list the following SmarTest features:」

- `Per Pin TIA (ppTIA)`
- `Rapid Source Sync (RSS)`
- `Xpress Data Mode (xpressdata)`

**这三样不在这张 license 清单里**——原文没有说为什么，
所以**本页也不替它编一个理由**（是「不计费」还是「TAT 不认识」，原文没说）。

## 典型用法

**本文档没有 `## Procedure` / `## Before you begin` 段**，但**步骤是齐的**，只是散在正文里。
按原文顺序：

**1. 先满足两个前提**（原文 `Before starting TAT, make sure that:`）：

| 前提 | |
|---|---|
| `SmarTest is running` | SmarTest 在跑 |
| `A testflow is loaded` | 一个 testflow 已加载 |

> 「Before starting TAT, make sure that:」

**2. 敲命令**（原文 `To start TAT and generate the device license file enter the following:`）：

```
/opt/hp93000/soc/prod_pws/bin/tat -f <filename>
```

> 「-f is a must parameter. <filename> is either the hardware definition file (HDF), a model file, or an already existing device license file.」

**`-f` 是唯一的必填参数；它的值三选一**：HDF、model file、**或一份已经存在的 device license file**。
第三种用法原文没说目的——**本页不猜**。
**其余可选参数不在本页**，原文把读者指去 `How to generate and provide a device license file`（本页没读）。

**3. 读产物**：当前目录下的 `.licenses`；清单本身只列最低配置，
**注释段里有四个用量计数**（Level sets / DPS sets / Wavetables / Timing sets）。

**4. 一条容易踩的边界**：**别指望它顺手把 technology file 也优化了**——
原文明说它不改、也不优化，**只报数**。

## 和谁有关

**这一页的邻居几乎全在 `## Related information` 里**（原文列了五条），逐条说清关系：

- [[project]] —— 本页 `stage: project` 的依据：这份文档在
  `02.04_Model_File_and_Licensing` 章下，**licensing 是 project 阶段的事**。
- [[testflow-file]] —— **上游输入**：TAT 分析的是「一个已加载的 testflow」。
  注意口径：原文只说 `the given testflow` / `A testflow is loaded`，
  **`testflow-file` 这个文件名本文档一次都没出现**——这一条是按职责排的（**推断**）。
- [[model-file]] —— **上游输入之一**（与 HDF 二选一）。**`model file` 那一篇本页没读**，
  所以「model file 里有什么」本页一个字都没有。
- [[technology-file-for-a-device]] —— **下游 / 并列**：原文说 TAT **不**改也不优化 technology file，
  指过去的那一篇就是 `Optimizing the technology file`。
  **「谁优化、怎么优化」在本页的语料里一个字都没有。**
- `The hardware definition file (HDF)`（**未建**）—— **上游输入之二**；
  原文给它的全部描述只有一句 `describes the hardware of your tester (type, cards, memory mode)`。
- `Installing the line model encrypted database`（**未建**）—— **前置依赖**：
  要用某些可选参数就得先装它。**装不装得上、怎么装，本页不知道。**
- `The device license file`（**未建**）—— **产物的格式与语义**在那一篇里，
  **本页只到「它叫 `.licenses`、只列最低配置」为止。**
- `How to generate and provide a device license file`（**未建**）—— **可选参数清单**在那一篇里。
- [[device-license-file]] —— **就是产物本身**（`.licenses`）。
  这一条在 `related` 里保留，但要说清：**本文档没有把它作为一个"相关对象"点出来**，
  它只是产物文件的名字；**那一页讲的内容本页没读**。

## 版本

本文档有 `## Functional changes` 段，两条：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.2.1: Numbers of sets`

**第一条是哨兵值，不是「6.3.2 的变更」**（§11.2②）：`before` 的意思是
「在本文档集覆盖范围开始之前就已经有了」。

**第二条与正文对得上，这一条是本页的（推断）**：`Numbers of sets`
指的应当就是正文那个「注释段里报四个用量计数」的功能
（正文原句 `but provides the number of used sets`，例子代码块的表头写
`Number of sets used by this device:`）。**推断依据是措辞直接对上，而且正文里没有别的「数」**——
但**原文没有一句话把两者连起来**，所以本页标成推断，不标成文档事实。

**这条推断还有一个附带结论**：那张 `Level Sets: 220` 的示例块**是 7.2.1 之后才有形态**，
在 7.2.1 之前的 TAT 上不应当期望它出现。**这是本页从版本条目推的，不是文档说的。**

## 出处

`sources:` 一篇，**整篇读完**：
`02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07_The_Testflow_Analyzer_Tool__TAT.md`
（TDC `85446.htm`，**全文 3,681 字节**）。**没有读 `sources` 之外的任何文档。**

**本页没做的：**

- **四个子主题一篇没读**：`Installing the line model encrypted database`、
  `Optimizing the technology file`、`How to generate and provide a device license file`、
  `The hardware definition file (HDF)`。
  **所以本页没有：可选参数清单、HDF 的格式、那个加密数据库怎么装、technology file 怎么优化。**
- **`## Related information` 的五条里，四条没读**（只有 `The hardware definition file (HDF)`
  在正文里被顺带说了一句，那句话本页引了）。
- **一张图都没有。** 本文档对 `raw/` 下 `.png` 的引用是 **0 处**（逐处查过），
  所以**本页没有任何来自图的结论**——**不是图够不着，是这篇文档本来就没配图**（§11.4）。
- **没有实跑。** 没有装过 TAT、没有生成过 `.licenses`、没有比对过 license 用量。
  **示例代码块里那四个数（220 / 79 / 128 / 726）是文档的示例**，不是任何真实机台的读数。
  `verified: doc-only` 指的就是这件事。
- **写这页时没有动 `wiki/index.md`、也没有把本页挂进 `wiki/stages/project.md`**；**两者已由本批收尾统一挂入**（`index.md` 的 `L3/project` 条、`stages/project.md:134` 的层表）。（**2026-09-20 更正**：原文写「那是待办」——**收尾动作把它变成了假话**。）

**⚠️ 本页照实记下、一处都没替语料改的瑕疵：**

**① 同一份文档里同一个概念两种写法：`Level sets` 与 `Level Sets`。**
正文那四个列点的首项写 `Level sets`（小写 s），而例子代码块的表头写 `# Level Sets: 220 #`（大写 S）；
`DPS sets` / `Timing sets` 同样是这个差别。**本页两处都照原样引，不统一。**

**② 一个概念两种缩写**：正文第一句写 `device license files (DLF)`，
第三句写 `device license file (.licenses)`。**本页按「同一个东西」处理，并在正文里标明了这句合并是本页做的。**

**③ `Note TAT does not change and optimize...` 那一行在 raw 里行首有一个空格**
（raw 第 36 行以空格开头）。按 §11.1① 折叠空白，**本页引文里没有那个空格**。

**④ `layer` 已更正为 `L3`（2026-09-20）——判据是文档自己的一句原话。**
文档写着 **`TAT is a command line tool.`**，所以按 §6 的 `L3`（**调用者是外部进程**）它是 `L3`。
**原先这一格是 `gui`，错了**（建页时没人读到那句；**是建 `dps-pins-editor` 那页的 agent 查出来的**）。
**⚠️ 措辞更正**：本页初版写「**文档第一句**就是判据」——**那是错的**：
这句话在 raw 第 21 行，是**正文第三个段落的首句**；**文档第一句是**
`This topic describes the function and general usage of the Testflow Analyzer Tool (TAT).`（raw 第 15 行）。
**判据句本身逐字存在、结论不变，但「第一句」这个描述是编的**——由 reviewer 查出。
**更正过程照实记**：先前有人按「以对象页为准」的约定把 `wiki/stages/project.md` 的层格也改成了 `gui`——
**那是拿约定盖住了判据**。§6 能定案的时候，**约定不适用**；**这次是 §6 能定案的**。
两处现在都是 `L3`（页 + stage 表）。

**⑤ 编码坏字：零处。** 实测这一篇的 CJK 字符数是 **0**（§11.2① 那一族在这篇里一处都没有）；
**`DC/DC power units` 那一族（§11.2⑤）也是 0 处**。

`verified: doc-only`
