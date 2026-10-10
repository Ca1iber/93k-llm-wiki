---
type: object
title: JSUD - (Jitter Set UnDefine)
layer: L1
stage: timing
tags: [timing, jitter, jitter-set, jsud, l1-command, firmware-command, undefine, ps1600]
related: [timing, jsdf, jscf, jspr, jswf, jrst, mscf, msdf, ps1600, mapping-timing, smartest-7.0.1]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.05_JSUD_-__Jitter_Set_UnDefine.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# JSUD - (Jitter Set UnDefine)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **255 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.16.02.05_JSUD_-__Jitter_Set_UnDefine.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
JSUD {"js_set_name"|ALL}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117930_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：js_set_name | Specifies the name of an existing jitter set.

### Example

```
> JSUD   "js_set1"
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.16.02.05_JSUD_-__Jitter_Set_UnDefine.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if no jitter set with this name exists.

<!-- 报错节 end -->

## 是什么

**`JSUD` 是 jitter set 的「注销」命令——它把已经定义的 jitter set 删掉。** 原文正文全部只有一句：

> 「JSUD deletes a jitter set.」

**它是这一族里唯一「往回走」的命令。** 同族的另外四条都在**建 / 配 / 指 / 查**（见「和谁有关」那张表），
**只有它做减法**——**所以它的读法也必须反过来问：「删掉之后会怎样？」**
（**而本篇对这个问题一个字都没写**，见下面「三处语料未写」。）

### 两种形态：删一个，或全删

语法（在「语法 / 参数」节里，本页不重复抄）只有一行，参数表只有两格，逐字如下：

| 参数 | 原文（逐字） | 意思 |
|---|---|---|
| `js_set_name` | `Specifies the name of an existing jitter set.` | **给名字 = 删这一个**。注意原文的词是 **`an existing`（已存在的）** |
| `ALL` | `This option removes all defined jitter sets.` | **`ALL` = 把所有已定义的 jitter set 全删**（`all defined jitter sets`） |

**两条读法**：

1. **`js_set_name` 必须是「已存在的」**——**这不是建议，是判据**：
   报错节那句逐字是 `An error is generated if no jitter set with this name exists.`
   （**报错节由脚本逐字取自本篇的 `## Errors` 段，本页不重复抄、也一个字没改**）。
2. **`ALL` 是这一族里唯一的「批量清理」手段**——**没有「按前缀删」之类的形态**
   （语法行只有这两个取值，**没有第三种**）。

### **它没有查询形态**——这是它与同族四条的一个硬区别

**同族另外四条都是「命令 + 查询」成对的**，从它们的页面标题就能看出来
（**下面这一列标题是本页从各页 frontmatter 的 `title` 里读到的**）：

| 命令 | 页面标题（逐字） | 有没有 `?` |
|---|---|---|
| `JSCF` | `JSCF, JSCF? - (Jitter Set ConFiguration)` | **有** |
| `JSDF` | `JSDF, JSDF? - (Jitter Set DeFinition)` | **有** |
| `JSPR` | `JSPR, JSPR? - (Jitter Set PRimary set)` | **有** |
| `JSWF?` | `JSWF? - (Jitter Set WaveForm)` | **有**（标题里就带 `?`） |
| **`JSUD`（本页）** | **`JSUD - (Jitter Set UnDefine)`** | **没有** |

**并且本页的语法行里也只有 `JSUD` 一种写法、没有 `JSUD?`**——
**所以「删完之后还剩哪些 jitter set」这件事，本篇没有给查询办法**（**这是本页的读法（推断）**，
依据是标题与语法行两处都没有 `?`；**「本篇没给」不等于「没法查」**——
**同族的 `JSDF?` / `JSPR?` 能不能拿来查，本页没读它们，不声称**）。

### `## Application` 全文只有两个词

本篇有一节叫 `## Application`，**全文逐字是**：

> 「Jitter test.」

**这就是本篇对「这条命令用在哪」的全部交代**——
**没有说它用在 setup 的哪一段、没有说它能不能在测试运行中执行、没有说它和 site 的关系。**

### 三处语料未写（**都写在明处，不替它推**）

| 想问的 | 本篇 |
|---|---|
| **删掉之后硬件里的 jitter set 格位会怎样**（同族的 `JSDF` 有「硬件最多存 128 个、超了 FIFO 替换」的机制，**那是 [[jsdf]] 那一页说的，不是本篇**） | **语料未写** |
| **删一个正被用作 primary 的 jitter set 会怎样**（`primary` 这件事是 [[jspr]] 那一页的，**本篇一个字没提 primary**） | **语料未写** |
| **一个 jitter set 都没有时，`ALL` 会不会报错**（报错句只覆盖「名字不存在」一种情形） | **语料未写** |

**本篇也没有 `## Predependencies` 段**——**所以「删之前必须先做什么」一个字的正面规定都没有**；
**唯一能倒推出来的前置是报错句那句**：**名字必须已经存在**（否则报错）。

## 典型用法

### 例子只有一行，而且只演示了两种形态中的一种

本篇 `## Example` 段全文逐字：

```
> JSUD   "js_set1"
```

**三处值得注意**：

1. **`>` 是命令行提示符**——**所以这是「在 hpt / 命令行里敲」的写法**，不是文件里的写法
   （**对照 [[jsdf]] 那页：它的例子也是 `>` 开头**——**这一族都用同一种例子形式**）。
2. **`JSUD` 与 `"js_set1"` 之间有三个空格**（逐字如此）。**本页照原样引，不替它压成一个。**
3. **`ALL` 那种形态没有例子**——**例子只有「删一个具名的」这一种。**

### 照本篇能确证的顺序（**只有两步**）

1. **确认那个 jitter set 的名字已经存在**（原文 `Specifies the name of an existing jitter set.`；
   不存在的后果就是报错）。
2. **`JSUD "<名字>"`**；要全清就 **`JSUD ALL`**。

**就这两步。** 本篇**没有**写「删之前要不要先解绑 primary」「删之后要不要重新下载」「要不要紧跟着做什么」
——**这三件事本页答不了**（见「三处语料未写」）。

### 这一族的大致链路（**同族的四页给出的，不是本篇**）

**下面是本页从同族四个页面（[[jsdf]] / [[jscf]] / [[jspr]] 的「是什么」段，
以及 [[jswf]] 的前景）读到的分工**——**本页的 raw 里没有这条链路**：

| 命令 | 干什么（**同族页面的说法，本页只转述**） |
|---|---|
| `JSDF` | **给 jitter set 起名（上户口）**：`JSDF creates a jitter set by defining a unique name for it.` |
| `JSCF` | **配置抖动注入**：`This command serves to define and query the jitter injection for the specified pins.`；且**它要求「目标 jitter set 必须已经用 `JSDF` 定义过」** |
| `JSPR` | **指定哪个 jitter set 是 primary**（primary 那一个才会在测试里自动被用到） |
| **`JSUD`（本页）** | **把 jitter set 删掉**（本篇原文只有这一句） |

**所以 `JSUD` 在这一族里的位置是链路的末端**：**`JSDF` 建 → `JSCF` 配 → `JSPR` 指 → `JSUD` 撤**。
（**「末端」是本文的读法（推断）**，依据是上面四条各自的职责；
**本篇没有描述过任何顺序关系**。）

## 和谁有关

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[jsdf]] | **上游 / 前置**。名字是 `JSDF` 给的；本页只能删「已存在的」那一个。**`JSUD` 与 `JSDF` 是同一族的「建—删」两端** | 本篇参数表 `an existing jitter set` + 报错句（**文档事实**）；`JSDF` 的职责来自 [[jsdf]]（**本页读过的 wiki 页**） |
| [[jscf]] | **同族（配置侧）**。它要求 jitter set 先用 `JSDF` 定义过——**本页是把这个集合删掉的那一步** | [[jscf]]（**本页读过的 wiki 页**）；**本篇一个字没提 `JSCF`** |
| [[jspr]] | **同族（primary 侧）**。它指定 primary jitter set；**「删掉 primary 会怎样」本页答不了** | [[jspr]]（**本页读过的 wiki 页**）；**本篇一个字没提 primary** |
| [[jswf]] | **同族，同一章的兄弟**（`02.06.16.02.06`，紧挨着本页的 `.05`）。**它的 raw 本页没读**（那是本批的另一页） | 目录号相邻（**文档事实：路径**） |
| [[jrst]] / [[mscf]] / [[msdf]] | **同章家族的其他成员**（`JRST` 抖动调制器复位、`MSCF` / `MSDF` 是 modulation set 那一对）。**三篇的 raw 本页都没读** | 家族清单来自 [[mapping-timing]] 的「抖动注入」一行与 [[timing]] 的 L1 子专题（**本页读过的 wiki 页**） |
| [[timing]] | **stage 页，而且它把本页认在这一段**。它的 L1「抖动注入（子专题）」一节逐字写着：`02.06.16_Commands_for_jitter_injection` 家族：[[jrst]] [[jscf]] [[jsdf]] [[jspr]] [[jsud]] [[jswf]] [[mscf]] [[msdf]]，并给出归属判断「属本阶段」 | [[timing]]（**本页读过的 wiki 页**）——**那一段的依据是 `02.06.16.01_Principles_of_jitter_injection`，那一篇本页没读** |
| [[mapping-timing]] | **跨层对照表，它已经在等本页**。它的「抖动注入（本阶段的子专题）」一行，L1 列里就写着 [[jscf]] / [[jsud]] / [[jrst]] / [[jsdf]] / [[jspr]] / [[jswf]] / [[mscf]] / [[msdf]]——**其余各列全是 `?`**（**即：这张表没有为抖动注入做出任何跨层对照**） | [[mapping-timing]] 的主表（**本页读过的 wiki 页**） |
| [[ps1600]] | **硬件侧的唯一允许型号**。[[timing]] 那一页的归属判断里写着抖动注入「仅 PS1600 支持、仅对 drive pin 有效」——**本页的 raw 里 `PS1600` 与 `pin` 都没出现** | [[timing]]（**本页读过的 wiki 页**）——**那一条的出处是 `02.06.16.01`，本页没读** |
| [[smartest-7.0.1]] | **版本页**：本篇 `## Functional changes` 的唯一一条 | 本篇版本段（**文档事实**） |
| [[jscf]] / [[jsdf]] / [[jspr]] | **它们是「本页存在」的旁证**：三页的「和谁有关」/「出处」里都记着「同族，但本页没读 `jsud` 那篇」——**本页是那三页在等的目标**；本页现在把这一格补上（**只补本页自己那篇 raw**，那三页的 raw 仍未读） | 三页的 `## 和谁有关` / `## 出处`（**本页读过的 wiki 页**） |

> **一条要注意的边界**：上表里凡是标「（本页读过的 wiki 页）」的，
> **都是别的 wiki 页的读法，不是本页 raw 的事实**。**本页的 raw 一共 686 字节**，
> 它只说了一件事——「删」。**别的都是族谱。**

## 版本

本文档**有** `## Functional changes` 段，段里**只有一条**：

- `Introduced in SmarTest 7.0.1`

> **这一条不是哨兵值**（**对照 §11.2 ②**）：它的措辞是 **`in`，不是 `before`**——
> **所以它真的说的是「`JSUD` 是 SmarTest 7.0.1 引进的」**
> （**§11.2 ② 那个哨兵写法是 `Introduced before SmarTest 6.3.2`，本批别的页里有实例**）。
> → [[smartest-7.0.1]]

**一条交叉印证（来自别的页，不是本页的 raw）**：[[timing]] 的 L1 抖动注入那一节写着
「SmarTest 7.0.1 引入」——**和本篇这一条是同一个版本号**。
（**那一页的依据是 `02.06.16.01_Principles_of_jitter_injection`，本页没读那一篇**；
**但两个来源给出同一个版本号，本页照实记下**。）

**版本段里没有的东西**（照实记，不替它补）：**没有第二条**。
所以「`ALL` 这个形态是哪一版加的」「7.0.1 之后这条命令改过没有」**在本篇里查不到**。

## 出处

`sources:` **一篇**：

- `02_System_reference/02.06_Command_Reference/02.06.16.02.05_JSUD_-__Jitter_Set_UnDefine.md`
  （frontmatter 的 `source_topic` 是 **`117930_2.htm`**，**833 字节 / 53 行，整篇读完**——
  按 §11.5 口径：字节是 `st_size`，行数是 `wc -l`）
- 本页的「语法 / 参数」节与「报错条件」节**都是脚本从这一篇抽的**（**本页一个字没动**）：
  语法节抽的是 `## Syntax` / `## Parameters` / `## Example` 三段，
  报错节抽的是 `## Errors` 段。
  **注意本篇的 `## Application` 段没有被抽进任何一节**——所以「Jitter test.」那句
  **是脚本视野之外的**，本页在正文里逐字引了一次。

**⚠️ 一处 §10 的「重复投放」，本页查了，并且差得很有意思**：本篇的 `source_topic` 带 **`_2`** 后缀
（`117930_2.htm`），**说明同一篇 TDC 页被投放了两份**。实测：

| | 路径 | `source_topic` | 字节 |
|---|---|---|---|
| **本页的出处** | `02_System_reference/02.06_Command_Reference/02.06.16.02.05_JSUD_-__Jitter_Set_UnDefine.md` | `117930_2.htm` | **686** |
| **同页的另一份** | `02_System_reference/02.06_Command_Reference/02.06.02.02.150_JSUD_-__Jitter_Set_UnDefine.md`（字母序命令索引章） | `117930.htm` | **685** |

**两份差 1 个字节。** 差在哪**本页没看**（**只核了另一份的 frontmatter 与大小，没有读它的内容**）。
**这个「差 1 字节」和 §11.5 那张口径表里记的 `WSUS` 是同一个形状**
（`02.06.02.02.342_WSUS` 与 `02.06.06.02.46_WSUS` **两篇差 1 字节**）——
**记在这里，供下一次遇到 `_2` 的人对照。**

**另一件值得记的（同一件事的另一面）**：**同族另外三页的 `sources:` 用的是 `02.06.02.02.14x` 那一份**
（[[jscf]] → `.147`、[[jsdf]] → `.148`、[[jspr]] → `.149`），
**而本页用的是 `02.06.16` 那一份**——
**所以本页与那三页的出处不是同一次投放。**
**这是「同一篇文档的两个路径」，不是「两篇文档」**（§10 第 0 步）。

**本页没做的**：

- **`02.06.16` 这一族其它篇的 raw 一篇没读**：`JRST` / `JSCF` / `JSDF` / `JSPR` / `JSWF?` /
  `MSCF` / `MSDF`，以及族首的 `02.06.16.01_Principles_of_jitter_injection`、
  `02.06.16.01.01_Two_ways_of_organizing_jitter_setup_data`、
  `02.06.16.02_List_of_commands_for_jitter_injection`。
  **所以「抖动注入整体是怎么回事、这八条命令怎么配合」本页一个字没有**——
  **本页只有「删」这一个动作，加一行「这族有谁」的名单。**
- **同族的 `jscf` / `jsdf` / `jspr` 三页读了（wiki 页）**，本页上表里凡引它们的话**都已标明是它们说的**；
  **本页没有读它们背后的 raw**（那是 `02.06.02.02.147`–`.149`）。
- **`JSDF` 的「硬件最多 128 个 jitter set、超了 FIFO 替换」这条机制本页没读原文**——
  它出现在上表里时已标明是 [[jsdf]] 那一页的读法。
- **`PS1600` / `pin` / `drive pin` 这些约束本页没读原文**——来自 [[timing]] 那一页的转述。
- **图**：**本篇对 `raw/` 的引用 0 处**——实测 `.png` / `.jpg` / `.gif` / `!\[` / `<img` / `raw/`
  六种写法在本篇里**全部 0 命中**。**所以本页没有任何来自图的结论，这张「没有图」是查过的事实，
  不是「够不着」。**
- **没有实跑。** 没在机台上删过 jitter set、没敲过 `JSUD ALL`、没看过删完之后的硬件状态。
  `verified: doc-only` 指的就是这件事。

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **参数表没有表头行。** 语法节里那张表**从一条空的第一格 ` | ` 直接开始**，
> 接着才是 `js_set_name` 与它的说明。
> **所以「第一列、第二列各叫什么」在本篇里没有**——
> **这与 [[wavetable]]、[[waveform-set]]、[[timing-specification]] 几篇是同一个形状**
> （**同一族文档的 HTML→md 压平共性**）。**本页照原样留它，没有补表头。**

> ② **例子里 `JSUD` 与参数之间有三个空格**：`> JSUD   "js_set1"`
> ——**多余的空格是原文的**，本页照原样引（在「典型用法」那节的代码块里）。
> **而且例子只演示了一种形态**（具名删除），**`ALL` 没有例子**——
> **这不是错，是例子的覆盖范围，记一笔免得下一个人去找不存在的第二个例子。**

> ③ **`## Application` 全文只有 `Jitter test.` 两个词**——
> **本篇没有解释这个 application 指什么、用在哪一段**。
> **本页照原样引，不替它展开**（**更不替它写「用在 setup 阶段」之类的话**）。

> ④ **报错句只覆盖一种情形**：`An error is generated if no jitter set with this name exists.`
> ——**它说的是「这个不存在」，没说 `ALL` 在没有 jitter set 时会怎样**。
> **这一句在「报错条件」节里（脚本逐字抽的），本页一个字没动**，只在这里指出它的覆盖范围。

`verified: doc-only`
