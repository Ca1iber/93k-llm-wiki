---
type: object
title: wavetable
layer: n/a
stage: timing
tags: [timing, wavetable, pure-waveform, pin-list, dfgp, timing-file, concept]
related: [timing, timing-file, timing-master-file, timing-equation-set, timing-specification, wavetable-file, waveform-set, dfgp, eqsp, timing-setup-tool, mapping-timing, smartest-6.3.2, smartest-6.5.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.03.07_wavetable.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# wavetable

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**wavetable 是「把纯波形（pure waveform）逐条贴到一串 pin 上」的那张表。** 原文第一句就是全部定义，
不带任何前置解释：

> 「A wavetable is used to apply pure waveforms to a list of pins. It is divided into one or
> more PINS sections. Within one PINS section, pure waveforms must be specified.」

拆成三条 **文档事实**：

| # | 原文（逐字） | 读法 |
|---|---|---|
| 1 | `A wavetable is used to apply pure waveforms to a list of pins.` | **它的用途是「施加纯波形」**；作用对象是**一串 pin** |
| 2 | `It is divided into one or more PINS sections.` | **它由 `PINS` 小节组成**，小节数**一到多个** |
| 3 | `Within one PINS section, pure waveforms must be specified.` | **一个小节里必须给出纯波形**——`must`，不是「可以」 |

**三条合起来就是它的形状：一张 wavetable = 若干个 `PINS` 小节，每个小节 = 一串 pin + 该串 pin 上的纯波形。**
**本篇没有再往下讲一层**：没有列、没有字段表、没有例子、没有 procedure（见「出处」）。

### 它的「语法」是一张图，不是一段加标记的文字

这是本页最容易读漏、也是「语法 / 参数」节为什么是空的一节的原因。原文对语法的交代只有一句：

> 「The syntax for this section is shown below:」

**紧跟其后的是一张 `.png`（`raw/21988.png`），正文里一行语法都没有。**
**所以「本篇没给语法」是错的——语法给了，在图里；「本篇没给可逐字抽的语法段」才是对的**
（§4：没有段标记时脚本一个字都不收，这是判据本身写着的口径，不是本篇缺内容）。

### 图上能读出的五个记号（**图证**）

**下面这一节的内容来自那张图，不是来自正文文字**——**图里的字搜不到**（拿记号名去 raw 里 grep 是 grep 不到的），
所以按 §11.4 单独标成**图证**。图是一张**语法铁路图**（railroad diagram），框里能看出的记号是五个：

| 图上的记号 | 本篇正文有没有定义它 |
|---|---|
| `PINS` | **没有**。正文只在「divided into one or more PINS sections」里用到这个词，**没解释它怎么写** |
| `pin_list` | **有**。参数表里唯一有说明的那一行（见下） |
| `#comment` | **没有** |
| `end_of_line_marker` | **没有** |
| `pure_waveforms` | **没有**。正文只说过 `pure waveforms must be specified`，**没给它的写法** |

**这五个记号里，唯一在正文里有文字说明的是 `pin_list`**——其余四个**只存在于图里**。
（**这是本页最实用的一条**：拿这四个名字去语料里搜，只会搜到这张图的名字记不下来。）

### 图的结构：两个循环（图证）

**图的连线形状能读出的只有一条**：这条语法**不是一条直线**，图上有**两个环**——

- **外圈那个环**：`PINS` → `pin_list` →（`#comment` 有旁路，可省）→ `end_of_line_marker` →
  回到 `pin_list` 之前**再走一遍**。（**推断**）它的意思是**「这一组可以重复出现，即一张 wavetable 里可以有多条 `pin_list` 行」**；
  **依据**是图上的回边 + 正文那句 `It is divided into one or more PINS sections`（一个 wavetable 有多于一个小节）。
- **里圈那个环**：单独圈着 `pure_waveforms`。（**推断**）它的意思是**「一个小节里纯波形可以有多条」**；
  **依据**是回边 + 正文那句 `pure waveforms must be specified` 用的是复数。

> **⚠️ 这两条是推断，不是原文。原文对这张图一个字都没解释**——
> 图上没有图例、没有说明、没有把记号名与正文的句子对上。**本页只摆图里读得出来的东西。**
> **另外，这张图没有版本标注**（§11.4 那条坑）：图上的记号名属**命名性**信息，
> **它是不是 7.10.3 的写法，本篇核不出来**——本页不把它当现名用。

### `pin_list`：本篇唯一有文字说明的参数

**它的定义在语法节的参数表里（本页不重复抄），要点只有两条：**

| 要点 | 原文（逐字） | 意思 |
|---|---|---|
| **它是「谁」** | `The name of the pin or pins for which the following pure waveforms are to be defined.` | **纯波形的施加对象**——pin 名，**可以多个**（`pin or pins`） |
| **它可以放什么** | `This may also include names of pin groups created using the DFGP command.` | **可以写 `DFGP` 建出来的 pin group 名**——注意措辞是 **`may`（可以）**，不是 `must` |

**第二条是本篇唯一一处把手伸到别的命令上的地方**：**pin 的名单来源之一是 [[dfgp]]。**
**但本篇没有说「必须先建组再用」**——它只说 `may also include`。
（按 §2.2 那四种约束形态判，这里**没有**出现 `before` / `must` 之类的词，
**所以本页不把它写成一条前置约束**。）

### 一条与版本条目互相印证的话（**推断**）

`## Functional changes` 里有一条写的是 **`Logical waveform is not supported.`**（6.5.2 起）。
正文那句是 `pure waveforms must be specified`——**两句方向一致：这个容器里只装纯波形，不装逻辑波形。**
（**推断**：本篇没有一句话把这两处连起来；依据是两处指的是同一个「一个小节里写什么」的位置。）

## 典型用法

**先说清楚一件事：本篇没有用法可抄。** 它没有 `## Procedure`、没有 `## Before you begin`、
没有 `## Example`、没有 `## What to do next`——**整篇是「一句定义 + 一张语法图 + 一个参数 + 两行版本」。**
所以本节能给的，全是**从上面那条语法形状里读出来的**，不是原文给的步骤。

**能从本篇确证的三件事（照这个顺序想）：**

1. **pin 得先存在。** `pin_list` 是 `The name of the pin or pins …`——
   **写的是名字，不是新定义**。名字从哪来本篇没写（pin 定义侧的文档**本页没读**），
   但它明说了**可以用 [[dfgp]] 建的 pin group 名**代替逐个列 pin。
2. **一个小节里必须给纯波形**（`must be specified`）——**只写 `PINS` 行、不给波形，本篇的措辞是不允许的**。
   （**这条是文档事实**，但**违反了会报什么，本篇没有 `## Errors` / `## Warnings` 段**——
   **所以本页没有「报错条件」节可写**，见「出处」。）
3. **一张 wavetable 里可以有多于一个小节**（`one or more PINS sections`）。

**本篇答不了、要去别处问的**：

| 想知道什么 | 本篇 | 去哪 |
|---|---|---|
| wavetable 在 timing setup file 里怎么写出来（`WAVETBL` / `DEFINES` 那些行） | **一个字没有** | [[wavetable-file]] 的语法节（**那是另一篇 raw，本页没读**）；[[timing-file]] / [[timing-master-file]]（**本页没读**） |
| wavetable 有哪些列、`PINS` 行的字段顺序 | **一个字没有** | 那一族参考文档（**本页没读**，见「出处」） |
| 纯波形自己怎么定义（`WAVE` / `WFDF` 那一族） | **一个字没有** | [[wave]] 等（**本页没读那几篇**） |
| GUI 上在哪编 wavetable | **一个字没有** | [[timing-setup-tool]]（**本页没读那篇**） |

**一句话**：**本页只是「wavetable 是什么」的定义页，不是「怎么用 wavetable」的操作页**——
**操作那一侧在本 wiki 里由 [[wavetable-file]] 与 [[timing-setup-tool]] 分担，而那两篇的 raw 本页都没读。**

## 和谁有关

**每条都写明是什么关系，以及这条关系是本篇读出来的、还是从别的 wiki 页看来的。**

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[dfgp]] | **上游（名单来源）**。`pin_list` 里可以写 `DFGP` 建出来的 pin group 名，代替逐个列 pin | 本篇参数表那句 `may also include names of pin groups created using the DFGP command.`（**文档事实**） |
| [[wavetable-file]] | **文件侧的姐妹页，分工相反**。那一页讲的是「协议 wavetable 怎么进 device timing 文件」（`USE_PROTOCOL`），并**自己声明**它不讲「wavetable 本身是什么」——**那句留给本页**。**本页兑现了「是什么」，兑现不了「有哪些列」**（那一页声明的那半句要读参考文档，见「出处」） | [[wavetable-file]] 的「是什么」与「出处」两节（**本页读过的 wiki 页**） |
| [[timing-specification]] | **下游（合成产物）**。wavetable 是合成 timing specification 的原料之一——**这条关系来自批次划分与那一页自己的定位**；**本页的 raw 里没有出现 `timing specification` 这个词** | 本页没读那篇（**取材边界，不是文档事实**） |
| [[timing-equation-set]] | **同级的另一半原料**（与 wavetable 一起合成 timing specification）。**本页的 raw 里一个字都没出现** | 本页没读那篇（**取材边界**） |
| [[timing-file]] / [[timing-master-file]] | **落盘的一侧**。wavetable 最终是写在 timing 文件里的东西；**本页没读这两篇**，所以「写在哪一行、什么段」本页给不出 | 本页没读（**取材边界**） |
| [[waveform-set]] | **同 stage 的兄弟页，不是同一个东西**。那一页讲的是**内存里的逻辑容器**（wavetable + device cycle table + 一个或多个 timing set 的集合体）——**本页讲的是 wavetable 本身**。**两页的 raw 不同，本页没读那一篇** | 批次划分（**取材边界**） |
| [[wave]] | **下游（纯波形的定义侧）**。本页反复出现 `pure waveform`，**但它是怎么写出来的，本篇没有一字** | 本篇（**取材边界**） |
| [[eqsp]] | **同族的 L1 分段命令**（`EQSP TIM,WVT` 把 timing 文件切出 wavetable 段）。**本篇没有出现 `EQSP`** | [[wavetable-file]] 与 [[mapping-timing]] 的记载（**本页读过的 wiki 页**） |
| [[timing-setup-tool]] | **GUI 侧的对口**（wavetable 的编辑入口）。**本篇提到的 GUI 是零个** | [[mapping-timing]] 的主表（**本页读过的 wiki 页**） |
| [[mapping-timing]] | **对照表页**。它把 wavetable 的「GUI ↔ 文件 ↔ L1」三列排在同一行 | **本页读过的 wiki 页** |
| [[timing]] | **stage 页**。本页 `stage: timing` 填的是「最近的一段」不是「归属」——wavetable 是 timing 数据的一部分（§6）。**⚠️ 这里曾有一处口径不一致，2026-09-21 已查明并解掉**：本页的 `layer: n/a`，而 [[timing]] 的「涉及对象」表原先把 wavetable 写成 `file`——`extract/stage-report.md` 的**第十一类**当时报这一处 ❌。**错的是那张表的格子，不是本页**：那张表把 `[[wavetable]]` 与 [[wavetable-file]] **并在一行共用一个层值**，而 [[wavetable-file]] 是 `file`、本页是 `n/a`；已拆成两行。**`layer` 按 PROSE-SPEC 第 2 条本页不许动，所以改的是对面那张表** | frontmatter 约定 + [[timing]] 的表格（**本页读过的 wiki 页**）+ `extract/stage-report.md` 第十一类 |
| [[smartest-6.3.2]] / [[smartest-6.5.2]] | **版本页**。本篇 `## Functional changes` 的两条分别指这两版 | 本篇版本段（**文档事实**） |

**一条本页答不住、只能记下来的边界**：本页 raw 只讲「容器由什么组成」，
**它和 timing 文件的接线、和 spec/equation 的合成、和 GUI 的关系，全在本页之外**——
上表里标「取材边界」的那几行**都不是本页读出来的**，写在这里只是为了让读者知道该去哪一页找。

## 版本

本文档**有** `## Functional changes` 段，段里**两条**，逐字如下：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.2: Logical waveform is not supported.`

**两条的性质完全不同，必须分开读：**

| 条目 | 是不是哨兵值（§11.2 ②） | 读法 |
|---|---|---|
| `Introduced before SmarTest 6.3.2` | **是**。措辞是 `before`，意思是「在本套文档集覆盖范围开始之前就已经有了」 | **不许读成「6.3.2 新增了 wavetable」**。只能说：**7.10.3 上有，且它比 6.3.2 更老** → [[smartest-6.3.2]] |
| `SmarTest 6.5.2: Logical waveform is not supported.` | **不是**。带版本号 + 冒号，是标准变更行 | **6.5.2 起 wavetable 里不支持逻辑波形** → [[smartest-6.5.2]]。**⚠️ 这句话没有主语**（见「出处」瑕疵②） |

**版本段里没有的东西**（照实记，不替它补）：**没有第三条**。
所以「`#comment` / `end_of_line_marker` 是哪个版本进来的」「`pin_list` 能不能写通配」这类问题，
**在本篇里查不到**——要去 [[smartest-6.3.2]] 之后的各版本页，或去别的文档。

## 出处

`sources:` **一篇**：

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.03.07_wavetable.md`
  （frontmatter 的 `source_topic` 是 `16909.htm`，**751 字节 / 27 行，整篇读完**——按 §11.5 口径：
  字节是 `st_size`，行数是 `wc -l`，本语料末行带换行，两者恒等）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。
  **它这一节是空的**，理由脚本自己写在节里：**本篇没有 `Syntax` / `Parameters` / `Example` 这类段标记**。
  **这不等于本篇不给语法**——**语法是一张图**（见「是什么」那一节）。**这个区别本页写进了正文，没有改语法节。**

**本页读了的图**：本篇对 `raw/` 的引用**恰好一处**——`![wavetable](<../../../../raw/21988.png>)`。
**该文件存在**（`F:\master-dev\dorm-wsl-sytest\tdc-html\raw\21988.png`，**2,507 字节**），**本页用 Read 工具打开看过**，
**上面「五个记号」「两个环」两节就是从这张图读出来的，标成图证**——
**注意它搜不到**：拿 `end_of_line_marker`、`pure_waveforms` 这些字符串去语料里 grep，**一篇都搜不到**，
**因为它们是图里的字，不是文本**。

**本页没做的**：

- **wavetable 的「列 / 字段」那一族一篇没读。** 所以「wavetable 有哪些列、`PINS` 行的字段怎么排、
  波形那一列写什么格式」，**本页一个字没有**。
  ⚠️ **这一条要点名说清**：[[wavetable-file]] 那页把它自己没收的那半句写成了
  「wavetable 本身是什么、有哪些列」——**那半句在本页的 raw 里同样没有**。
  **本页只能兑现「是什么」，「有哪些列」要读写列的参考文档**（`02.08.04.34.04.03.03` 那一族里
  讲 timing wavetable 参考的那一篇，篇名见 [[wavetable-file]] 的「出处」——**本页没读它**）。
  **本页不把「有哪些列」当已答。**
- **`WAVETBL` / `DEFINES` 这些行的写法没读**。它们出现在 [[wavetable-file]] 的语法节里
  （那是**另一篇 raw**：`02.07.11.01.05.03_Wavetable_file.md`），**本页没读那一篇**。
- **纯波形定义那一族（`WAVE` / `WFDF`）没读**，所以「pure waveform 怎么写出来」本页没有。
- **pin 定义侧没读**：`pin_list` 里的 pin 名从哪来、pin group 怎么建（[[dfgp]] 那一篇）**都没读**。
- **GUI 侧没读**（wavetable 编辑页签、[[timing-setup-tool]]）。**本篇提到的 GUI 是零个。**
- **没有实跑。** 没在机台上写过 wavetable、没验过「一个小节不给纯波形会怎样」。
  `verified: doc-only` 指的就是这件事。
- **本篇没有 `## Errors` / `## Warnings` 段**，所以本页**没有「报错条件」节**——
  这不是漏写（**别处的骨架有那一节，本页的骨架没有**），是语料本来就没有。

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **参数表没有表头行。** 语法节里那张表**从一条空的第一格 ` | ` 直接开始**，
> 接着才是 `pin_list` 和它的说明，末尾又是一条 ` | `。
> **所以「第一列、第二列各叫什么」在本篇里没有**——`Parameter` / `Description` 这类表头格
> **不在文本里**。（对照：`[[dfge]]` 那一篇的同形状表里表头也一样缺——
> **这是这一族文档的 HTML→md 压平的共性，不是本页的错**。）
> **本页照原样留它，没有补表头。**

> ② **`SmarTest 6.5.2: Logical waveform is not supported.` 没有主语。**
> **「什么」不支持逻辑波形，本篇没写。**（**推断**）按上下文应是「wavetable 里」，
> **依据**是同段正文那句 `Within one PINS section, pure waveforms must be specified.`——
> 两处说的是同一个位置。**本页把这处并列摆着，不替它补主语。**

> ③ **图上那五个记号，四个在正文里没有定义**（`PINS` / `#comment` / `end_of_line_marker` /
> `pure_waveforms`）。**这不是笔误，是这一篇的取材方式**：**定义靠图，文字只解释了 `pin_list` 一个。**
> **记这一条的用处是**：**光读文本会以为这篇只讲了 `pin_list`**，
> 而实际上语法全在图上——**本页把它当瑕疵记，是因为「文本自己读不出自己的语法」这一点很容易被当成「文档没写」。**

> ④ **图没有版本标注。** 图上记号名属**命名性**信息（§11.4），
> **本篇的 `## Functional changes` 核不了它**（两条都不是改名记录）。
> **所以本页不声称这五个记号名是 7.10.3 的写法**，只声称「这张图上写的是这五个」。

**一条工程内部口径的不一致，本页照实记下、不替它裁定**（**不是语料瑕疵，是 wiki 自己的**）：
本页骨架给的 `type` 是 `object`、目录在 `wiki/objects/`；
而 `schema.md` §2.3 把 **Wavetable** 举成 **`concept` 页**的例子，§5 又把 `wavetable.md` 当
**concept 页的命名例**。**本页 `type` 由骨架给定，按 PROSE-SPEC 第 2 条不许改**，故只记不判。

`verified: doc-only`
