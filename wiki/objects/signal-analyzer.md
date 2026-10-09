---
type: object
title: Signal Analyzer
layer: gui
stage: results
tags: [gui, results, waveform, debugging, smith-chart, demodulation, rf, user-defined-function]
related: [results, mapping-results, timing-diagram-tool, raw-data-views, test-summary-tab, integrated-result-tool, shmoo-tool, data-retrieval-library]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26_Signal_Analyzer.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Signal Analyzer

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **177 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26_Signal_Analyzer.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.03.04_Rectangular_Plot.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Smith Chart Tool › Rectangular Plot）

The following picture illustrates an S-Parameter rectangular plot in the Smith Chart Tool.

 !`S11 Rectangular Plot in the Smith Chart Tool`（raw: `../../../../agent-html/123252.png`）

<!-- 语法节 end -->

## 是什么

**Signal Analyzer 是 SmarTest 里看波形的那个环境。** 原文一句就把它讲完了：

> 「The Signal Analyzer provides a waveform viewing environment that creates customizable, easy-to-use graphical display and analysis capabilities to debug test applications effectively.」

**关键词是 `debug test applications`**——它是**调试侧**的工具，不是结果判定侧。
它出现在 `stage: results`，是「最近的一段」而不是归属（§6）。

### 主窗就是两块：WNT + WGT

> 「The main window of the Signal Analyzer is divided into two sub panels:」

> 「The Waveform Navigator Tool (WNT) displays the list of waveforms stored in the current device file directory.」

> 「The Waveform Graphs Tool (WGT) is used to create, view, download, upload, and analyze waveforms. This tool not only shows setup data, but also result data in a unified manner.」

**三件事值得抠出来：**

- **WNT 列的是「当前 device file 目录下」的波形**——所以波形看不全时，
  第一件要怀疑的事是**目录选错了**（**推断**，依据就是 `stored in the current device file directory` 这半句；
  **原文没说怎么切目录**）。
- **WGT 一个面板同时管 `setup data` 和 `result data`**——`in a unified manner` 是原文自己的话。
  这句话解释了它为什么既像 setup 工具又像结果工具。
- **WGT 的动词有五个**：`create` / `view` / `download` / `upload` / `analyze`。
  **`download` / `upload` 是往硬件侧走**——工具条分组里有一组就叫 `Hardware Access`。

> 「The Navigator allows users to start applications. This window can be collapsed to maximize the size of the other panels.」

**面板可折叠**，这是原文唯一一条讲「界面怎么摆」的话。

### 功能入口：菜单栏 + 六组工具条

> 「The functions of the Signal Analyzer are accessed via the menu bar.」

> 「The main window of the Signal Analyzer also provides toolbars for viewing and modifying waveforms, setting cursor functions, and setting marker functions in the WGT:」

`02.08.04.26.02` 把这些工具条分成了**六个小节**——**这六个小节名就是它的功能分类**：

| 组 | 小节标题（原文逐字） |
|---|---|
| 图形缩放 | `Graph Customization` |
| 硬件访问 | `Hardware Access` |
| 光标 | `Cursor Functions` |
| 标记 | `Marker Functions` |
| 斜率标记 | `Slope Marker Functions` |
| 用户函数 | `User Defined Functions` |

### User Defined Panel：**功能可以用代码自己加**

> 「These functions are programmable using the Data Display API and DSP Test Method API. These functions are independent of the test method program.」

> 「Much of the functionality can also be controlled programmatically using the Data Display API.」

**这两句是本页与 L2 的接口**：入口是 `Data Display API`。
**`independent of the test method program` 是它的定位**——UDF 不挂在你那个 test method 上，
所以它可以在不跑测试的情况下改。

### 它能干的事（`02.08.04.26.01` 逐条给的清单）

| 要干什么 | 入口（原文给的链接名，逐字） |
|---|---|
| 加载一个数据日志文件、从里面选波形 | `Load Datalog...` 与 `Select Waveform...` |
| 造任意波形 | `Generate` |
| 改波形 | `Test Mask...` / `Translate...` / `Inject Jitter...` / `Cable Simulation...` |
| 算谐波失真与互调频率 | `Harmonics...` |
| 给 DSM 测试配矢量 | `DSM...` |
| 复制粘贴波形 | `Copy/Paste Waveforms` |
| 清空 `Result Waveforms` 表里列出的所有波形 | `Delete All` |
| 挂一个自定义分析函数 | `Assign User Defined Function` |

（左列是原文的分类，右列是**原文自己给的链接名**。
**这 8 条各有一篇专页，本页一篇没读**——所以每一项**怎么做**，本页一个字没有。）

### 三个「图型」，各自有版本门槛

| 图型 | 是什么 | 引入版本 |
|---|---|---|
| **Smith Chart** | `a graph type introduced in the Signal Analyzer`；画在**复反射系数平面**上 | **SmarTest 7.0.3** |
| **Rectangular Plot** | Smith Chart 的一个 UDF：**`magnitude [dB]` 对 `frequency [Hz]`**，把相位丢掉 | **SmarTest 7.0.3** |
| **Demodulation** | RF 波形的解调界面；**依赖 demodulation library** | **SmarTest 7.1.2** |

**Smith Chart 那段值得逐字抄两句**，因为它解释了**为什么同一条迹要有两个图型**：

> 「Since the reflection coefficient is always frequency dependent, the data trace in Smith Chart is actually 3-dimensional.」

> 「Smith Chart grid is made up of circles and arcs representing real and imaginary parts of normalized impedance or normalized admittance, respectively.」

**「迹实际是三维的」这句话是 Rectangular Plot 存在的理由**：
要看 `magnitude 对 frequency` 就得换一个二维图（**推断**，
依据是 Rectangular Plot 那篇自己写的 `if you are not interested in the phase information`）。

**Rectangular Plot 的用法原文写得很具体**：

> 「This new User Defined Function (UDF) can be accessed via right-click shortcut menu Analysis ->Show Rectangular Plot.」

> 「If there are multiple traces in the Smith Chart a dialog box will be displayed which allows you to select the target trace.」

**Demodulation 有一条前置事实**（不是约束，是「你看到的版本取决于库」）：

> 「Note The Demodulation tool relies on the demodulation library. Demodulation library revision can be found in Help menu About in Signal Analyzer.」

## 典型用法

**本页给不出「从零到看到波形」的步骤，这是文档事实而不是缺口。**
`02.08.04.26.01` 把自己的用法拆成了四条子过程——
`Starting Up Signal Analyzer`、`Passing Waveform into Signal Analyzer`、
`Downloading waveform patterns from the Signal Analyzer`、
`Converting existing waveforms to the new ASCII format`——
**这四条本页一条没读。**

能确认的只有三件：

**1. 进波形的两条来路**（各有一句依据）：

| 来路 | 依据 |
|---|---|
| **从数据日志** | 原文清单第一条：`Loading a data log file and selecting the waveform contained in the file (`Load Datalog...` and `Select Waveform...`)` |
| **从硬件 / pattern 侧** | WGT 的五个动词里有 `download` / `upload`，工具条有一组叫 `Hardware Access` |

**2. 「当前有哪些波形」以 `Result Waveforms` 表为准。**
依据是原文对 `Delete All` 的描述：它删的是
`all (see Delete All) waveforms listed in the Result Waveforms table`。
**那张表长什么样、有哪几列，正文没有——图里有**（见「出处」的图证）。

**3. Rectangular Plot 的四步**（原文完整，唯一一处写全的操作）：

| 步 | 做什么 |
|---|---|
| 1 | 在 Smith Chart 的迹上**右键** |
| 2 | 选 **`Analysis` → `Show Rectangular Plot`** |
| 3 | 迹多于一条时**弹框选目标迹** |
| 4 | 出图：`magnitude [dB]` 对 `frequency [Hz]` |

**一条用法上的边界**（**推断**，依据是那篇自己的 `Given a trace in a Smith Chart`）：
**Rectangular Plot 是从 Smith Chart 的一条迹上开出来的**，
所以它是 Smith Chart 的附属视图，不是独立的图型入口。

## 和谁有关

| 页 / 名字 | 关系是什么 |
|---|---|
| [[results]] | 本页 `stage: results` 的理由。**「最近的一段」，不是归属**（§6） |
| [[mapping-results]] | 那张五层对照表里「波形查看」一行的 GUI 格填的就是本页，**L2 格是 `Data Display API`**。**本页没有复核那一格** |
| [[timing-diagram-tool]] | **同类**：另一个看波形的工具。**两篇原文互相没有链接**，本页不比较（那篇没读） |
| [[raw-data-views]] / [[test-summary-tab]] / [[integrated-result-tool]] | **上游**：结果数据的展示与下钻侧，和本页同属 `02.08.04` 这一族 |
| [[shmoo-tool]] | 同族：另一个结果图形工具（本页没读它，不比较） |
| [[data-retrieval-library]] | `Load Datalog...` 读的就是数据日志——**但本页没读那条链上的任何一篇**，所以「日志从哪来」本页没有依据 |
| `Data Display API`（raw: `02.07.04.01.22`） | **L2 入口**（原文两处指向它）。**本页没读它**——它的参数、返回值一个字没有 |
| `DSP Test Method API` | 只会出现在与上一行同一句里。**它是什么、在哪，本页没有依据** |
| `Smith Chart Tool` / `Demodulation in the Signal Analyzer` / `Waveform Navigator Tool` / `Waveform Graphs Tool` / `User Defined Panel` / `Menu Bar` / `Tool Bars` / `Waveform Navigator Tool` 的子页 | 本页声明的子主题与它们各自的子节。**均未建页**，本页只有父篇里那几句 |
| `Load Datalog...` / `Select Waveform...` / `Generate` / `Test Mask...` / `Translate...` / `Inject Jitter...` / `Cable Simulation...` / `Harmonics...` / `DSM...` / `Copy/Paste Waveforms` / `Delete All` / `Assign User Defined Function` | **本页「是什么」那张表右列的 12 个入口**，**各有一篇专页，全部未建、全部没读** |

**一条必须写明的**：本页的 `sources:` 只有一篇，而**它的正文只有一句话**。
「是什么」以下的内容，**全部来自它自己声明的 4 条 `Subtopics`**
（§9.1 允许链的第 4 类目标）。这些路径不在 `sources:` 那一行里，本页明说这件事。

## 版本

**定义文档 `02.08.04.26_Signal_Analyzer.md` 没有 `## Functional changes` 段**（事实，
它的正文只有一句 `The Signal Analyzer provides a waveform viewing environment that creates customizable, easy-to-use graphical display and analysis capabilities to debug test applications effectively.`）。**这不是缺陷。**
条目分散在它声明的子主题里，逐篇转录（**出处写在每行**）：

| 哪一篇 | 条目（逐字） |
|---|---|
| `02.08.04.26.01` Using the Signal Analyzer Tool | **没有 `## Functional changes` 段** |
| `02.08.04.26.02` Elements of the Signal Analyzer Tool | `Introduced before SmarTest 6.3.2` / `SmarTest 6.5.3: The size of the waveform, which is analyzed using FFT, can be any integer.` |
| `02.08.04.26.03` Smith Chart Tool | `Introduced in SmarTest 7.0.3` |
| `02.08.04.26.03.04` Rectangular Plot | `Introduced in SmarTest 7.0.3` |
| `02.08.04.26.04` Demodulation in the Signal Analyzer | `Introduced in SmarTest 7.1.2` |

**⚠️ `Introduced before SmarTest 6.3.2` 是哨兵值，不是「6.3.2 新增」**（§11.2 ②）。
它的意思是「**在本文档集覆盖范围开始之前就已经有了**」。
**只有 `Introduced in SmarTest X.Y.Z` 那种写法才是「那一版新加的」**——
上表里 Smith Chart / Rectangular Plot / Demodulation 三条都是后者。

**一条值得注意的分布**：**三个图型里有两个（Smith Chart 与 Rectangular Plot）同为 7.0.3**。
原文没有说它们是同一次发布，**本页不合并这两条**——
`02.08.04.26.03` 与 `02.08.04.26.03.04` 是两篇，各写各的。

## 出处

**读了什么**：

- **`sources:` 里那一篇 `02.08.04.26_Signal_Analyzer.md`（`source_topic` `50664.htm`）整篇读完**——
  但它**正文只有 1 句** + 四条 `Subtopics`。**它是一张目录，不是一个文档。**
- **所以本页的事实来自它自己声明的 `Subtopics`**（§9.1 允许链的第 4 类目标）。
  **这些路径不在 `sources:` 那一行里，本页明说这件事。**
  **整篇读完的 5 篇**：`02.08.04.26.01`（Using the Signal Analyzer Tool）、
  `02.08.04.26.02`（Elements of the Signal Analyzer Tool）、
  `02.08.04.26.03`（Smith Chart Tool）、`02.08.04.26.03.04`（Rectangular Plot）、
  `02.08.04.26.04`（Demodulation in the Signal Analyzer）。**引文只来自这 5 篇。**

**本页没做的**：

- **`02.08.04.26.01` 的 4 条子过程一条没读**（`Starting Up Signal Analyzer`、
  `Passing Waveform into Signal Analyzer`、`Downloading waveform patterns from the Signal Analyzer`、
  `Converting existing waveforms to the new ASCII format`）。
  **所以「怎么启动、怎么把波形送进来、怎么下载回硬件、旧格式怎么转」本页一个字没有**——
  这是本页最大的一个缺。
- **`02.08.04.26.02` 的 5 个子主题一条没读**（`Waveform Navigator Tool`、`Waveform Graphs Tool`、
  `User Defined Panel`、`Tool Bars`、`Menu Bar`）。
  **所以六个工具条各有什么按钮、菜单栏有哪几个菜单、WGT 怎么用，本页都没有**——
  本页只有它们的**分组名**。
- **`02.08.04.26.03` 的另外 5 个子主题一条没读**（`Smith Chart format setting`、
  `Reflection Coefficient representation`、`Data File`、`Impedance Matching`、`Port Extension`）。
  **`Data File` 那一条尤其要紧**——Smith Chart 的数据从哪来，**本页因此没有依据**。
- **`02.08.04.26.04` 的 6 个子主题一条没读**（`Accessing the demodulation tool`、
  `Specifying waveform and standard`、`Editing input parameters`、`Executing demodulation`、
  `Verifying results`、`Configuring parameter list`）。
- **那 12 个功能入口的专页一篇没读**（`Generate` / `Test Mask...` / `Translate...` /
  `Inject Jitter...` / `Cable Simulation...` / `Harmonics...` / `DSM...` /
  `Copy/Paste Waveforms` / `Delete All` / `Assign User Defined Function` /
  `Load Datalog...` / `Select Waveform...`）。
  **「是什么」那张表右列的 12 个名字是原文逐字给的，它们做什么本页只有原文那一句短语。**
- **`Data Display API`（`02.07.04.01.22`）没读。** 所以「用代码控制这个工具」怎么调，本页一个字没有。
- **没有实跑。** 没在机台上开过 Signal Analyzer、没跑过解调、没做过 Smith Chart。
  `verified: doc-only`。

### ④ 图证：读了 3 张，逐张如下

（§11.4 / §2.5：**④ = 图证**，**从 raw 自带的图里读出来的**。
**它比「文档间链接」硬**——图是文档自带的，不是我的推断；**但它不可检索**，
要核只能自己再去开那张图。**图里的字本页一处都没有放进 `>` 引文块**。）

| 图 | 出处篇（alt 文字） | 读到了什么 | 解决了什么 |
|---|---|---|---|
| `353435.png` | `02.08.04.26.02`（`Main Screen`） | 主窗的**图上标注**逐字是 `Waveform Navigator` 与 `Waveform Graphs`；左导航栏路径逐字 `Navigator` > `Work Center` > `Signal Analyzer`；两张表的表头逐字 `Test Suite` / `TS No` / `Pin` / `Label` / `Site`（`Result Waveforms` 表）与 `Test Suite` / `Pin` / `Label` / `Site` / `Trace`（`Quick Viewer` 表）；菜单栏逐字 `File Edit View Insert Format Tools Actions Window Help` | **`Result Waveforms` 表的列名**（正文只说有这张表、不说列）；**两个子面板的图上名字**（见下） |
| `123252.png` | `02.08.04.26.03.04`（`S11 Rectangular Plot in the Smith Chart Tool`） | 窗口标题 `Graph #2`；图内标题 `Pin: NA; Rectangular Plot #1(S11)`；纵轴 `Magnitude [dB]`（0 到 -6）；横轴 `Frequency [Hz]`（刻度从 `1E9` 到 `9E9`，每 `1E9` 一格） | **把正文那句 `magnitude [dB] versus frequency [Hz]` 落到字面**；并说明**一个迹一张图、图标题里带 S 参数名** |
| `123242.png` | `02.08.04.26.03`（`Smith Chart`） | 窗口标题 `Graph #1`；图内标题 `sxgraph.s2p`；一圈一圈的圆与弧 | Smith Chart 的数据来源**在界面上标成一个以 `.s2p` 结尾的文件名** |

**这三张图里，回 9,398 篇 raw 逐条数过、命中为 0 的串**：

| 串（图里的写法） | raw 命中篇数 |
|---|---|
| `Magnitude [dB]`（**首字母大写**的那个写法） | **0** |
| `Rectangular Plot #1` | **0** |
| `sxgraph.s2p` | **0** |
| `Pin: NA` | **0** |
| `Graph #2` | **1**——**这一条要照实说**：命中的那一篇是 `03.14.06.09`（讲复杂波形文件处理的），**与本页无关**；**本页三张图里只有 `123252.png` 的窗口标题是 `Graph #2`**，而那个串在 raw 里没有作窗口标题用过 |
| `Graph #1` | 见下：**本页没有单独查它**，所以不填数字 |

**另一处要照实说的**：`123252.png` 图内标题里那个 `S11`，**本页没有单独查过它的命中数**，
所以不写数；图内标题的完整串（`Pin: NA; Rectangular Plot #1(S11)`）**在 raw 里 0 命中**。

**⚠️ 一处数字要说准**：正文里写的是**小写** `magnitude [dB]`
（1 篇命中 = `02.08.04.26.03.04` 自己），**所以「首字母大写」那个写法只在图上**；
而 `s2p` 这个**后缀单独**在 3 篇里出现过——**「0 命中」这句只对完整串 `sxgraph.s2p` 成立**。

**⚠️ 图证挖出一处正文与界面不一致，照实记**：`02.08.04.26.02` 的正文把两个子面板写成
`Waveform Navigator Tool (WNT)` 与 `Waveform Graphs Tool (WGT)`，
而图上两个标注框逐字是 **`Waveform Navigator`** 与 **`Waveform Graphs`**——**少了 `Tool`**。
**本页不判哪个是「真名」**，两处并列。
（说清判据强度：`Waveform Navigator` 这个串在 raw 里 **24 篇**命中、
`Waveform Graphs` **36 篇**命中——**所以「少 Tool」这件事文本里也有，不是图独有的**；
**只有 `Tool (WNT)` / `Tool (WGT)` 那两个连写形态在 raw 里分别是 17 / 21 篇**。
**本页因此不把它当「图证」单独记账，只当一处不一致记下来。**）

**图证答不了的（照实说）**：

- **`.s2p` 那个文件是谁生成的、Smith Chart 从哪读它，图答不了**——
  正文这几篇**一个字都没提 `.s2p`**（`Data File` 那篇本页没读）。
  **「它是某种 S 参数文件格式」这种话本页不写**——**语料未写，本页不拿常识填。**
- **图上没有一条 API 名、没有一条命令名、没有一份文件内容。**
  所以「波形查看」那一行的 L1 / L2 两格，**图一张都没填**。
- **Demodulation 一条图都没有**（`02.08.04.26.04` 那篇 0 张图）——
  **所以解调界面长什么样，本页不知道**。
- **图是「某一次具体会话」的截图，不是功能规范。**
  「哪些操作必填、哪些组合非法」图答不了。

### 语料瑕疵

**本页读的 6 篇（`02.08.04.26` 与它的 5 条子主题）逐篇查过**：

- **坏字（§11.2 ①，判据 `[一-鿿]`）：0 处。** 查过，不是没看。
- **整词替换（§11.2 ⑤，`DC/DC power units`）：0 命中。**
- **一处不是错、但会被误读的**：`02.08.04.26.03.04` 的标题行与 `Functional changes` 都是
  `Introduced in SmarTest 7.0.3`，而它的**父篇** `02.08.04.26.03`（Smith Chart Tool）
  **也是** `Introduced in SmarTest 7.0.3`。
  **两篇说同一个版本号，可能是同一件事、也可能是两件事**——
  **原文没说，本页不合并**（同一形态的另一条见「版本」那节）。

`verified: doc-only`
