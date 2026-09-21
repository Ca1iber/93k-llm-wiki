---
type: object
title: Setup Management Tool
layer: gui
stage: project
tags: [setup-management-tool, project, parallel-development, master-file, setup]
related: [test-program-explorer, level-master-file, project, level, timing, testflow, tmlimits]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04_Setup_Management_Tool.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Setup Management Tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **70 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04_Setup_Management_Tool.md>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05_Collision_handling.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Collision handling）

See the examples in each kind of setup master file collision handling.

<!-- 语法节 end -->

## 是什么

**Setup Management Tool 解决的是「多人同时改同一份 setup」的问题。** 原文第一句是它的全部定位：

> 「The Setup Management tool enables **multiple users** to work on **different parts of the same
> setup component** in parallel **without interfering with each others work**.」

**这句话里有三个限定，缺一个就把它的适用范围理解错了：**

| 原文 | 含义 | 容易读错成 |
|---|---|---|
| `multiple users` | 多用户 | — |
| `different parts of **the same** setup component` | 分的是**同一个** setup component 的**不同部分** | 「每人各分一个 setup component」 |
| `in parallel … without interfering` | 并行，且互不干扰 | — |

> **第二行是本页最要紧的一条。** 它说的**不是**「把 setup 拆开分给不同的人」，
> 而是「**多个人共享同一个 setup component，各改各的那一部分**」。
> **粒度是「component 内部的一部分」，不是「component」。**

### 两个使用场景：一个有条件，一个没有

原文第一句给的是**无条件**的那一个（并行改不同部分）。紧接着的第二句给的是**分布式**场景，
**并且带了全文唯一一处硬条件**：

> 「It can be used for **distributed setup development and debugging** even if the individual users
> need access to **the complete setup component**, **provided that they do not change the same part
> of it**.」

**`provided that` 是这句话的关节。** 把它变成「条件 → 结果」：

| 情形 | 结果 | 依据 |
|---|---|---|
| 各人改**不同**的 part | **可以**——**哪怕每人都需要拿到完整 component** | 原文 `even if … the complete setup component, provided that …` |
| 各人改**同一个** part | **原文没说会怎样** | 原文只写了 `provided that they do not change the same part of it`，**没说违反了这个前提会如何** |

> **第二行是缺口，不是结论。** 原文只把「不许改同一部分」写成了前提，
> **没有写「改到同一部分时会发生什么」**。子主题里单列了一篇 `Collision handling`（碰撞处理），
> **按标题判断那就是这个问题的去处**（推断）——**但那篇本页没读，所以本页不填这个空。**

### 它管哪四种 setup component

原文给了一张清单，**四条**：

| # | 原文 |
|---|---|
| 1 | `Level setup` |
| 2 | `Timing setup` |
| 3 | `Testflow setup` |
| 4 | `TMLimits test table setup` |

> **这张清单是「6.5.3 之后」的样子。** 版本段写着
> `SmarTest 6.5.3: TMLimits setup is now supported`——
> **第 4 项是后来加进这份清单的**（推断，依据是这两处的对照）。
> **换句话说：6.5.3 以前，这份清单只有三项**——**但原文并没有为更早的版本保留一份旧清单**，
> 本页是从版本记录推出来的。

### 它怎么进入工作流：搭在 load / save 上

> 「The tool is **integrated into the Test Program Explorer** by means of **the scripts that are
> called when a setup component is loaded or saved**, but it can also be called from **the command
> line** or **by user programs**.」

**三种入口，性质完全不同：**

| 入口 | 原文 | 谁来触发 |
|---|---|---|
| **集成入口（主路径）** | `integrated into the Test Program Explorer by means of the scripts that are called when a setup component is loaded or saved` | **载入或保存 setup component 时自动调脚本**——**不是人去点某个菜单** |
| 命令行 | `it can also be called from the command line` | 人 |
| 用户程序 | `or by user programs` | 程序 |

> **第一行的机制值得单独记住：本工具是挂在 `load` / `save` 这两个动作上的脚本。**
> **所以它在 Test Program Explorer 里可能「感觉不到」**——你没有主动调用它，
> **它在你载入或保存 setup 时就被触发了**（推断，依据是 `by means of the scripts that are
> called when … loaded or saved`）。

**三种入口与五条子主题对不齐：** 子主题只为**前两种**各写了一篇
（`Using … from the Test Program Explorer`、`Using … from the Command Line`），
**第三种「用户程序」没有对应的子主题**（见 `## 出处`）。

### 五条子主题，以及「master file」这个词的真正来源

| 子主题 | 从标题能读出的（**推断**） |
|---|---|
| `Concept of the Setup Management Tool` | 概念/原理——**本工具怎么做到不互相干扰的** |
| `Using … from the Test Program Explorer` | 入口一 |
| `Using … from the Command Line` | 入口二 |
| `Creating a level master file` | **建一个 level 的 master file** |
| `Collision handling` | **碰撞处理**——对应上面那个「改到同一部分」的缺口 |

> ⚠️ **「master file」这个词，主文档正文里根本没有。** 它是从两处看来的：
>
> 1. **子主题标题** `Creating a level master file`；
> 2. **本页「语法 / 参数」节里那条 70 字的原文**：
>    「See the examples in each kind of **setup master file collision handling**.」
>    （这一条是脚本从子主题 `Collision handling` 逐字抽的）
>
> **把两处并起来可以断定两件事**（推断，依据就是上面两条）：
> **① 本工具的机制里存在「setup master file」这个东西；
> ② `collision` 是发生在 master file 上的。**
>
> **但 master file 是什么、它和 setup component 是什么关系、四种 component 是不是各有各的
> master file——本页一个字都讲不出来。** 那在未读的 `Concept of…` 与 `Collision handling` 里。

### 一个「stage」上的定位

**本页是 `stage: project`**，和同批的 `gui` + `results` 那些页（[[integrated-result-tool]]、
[[shmoo-tool]] 等）不同。**理由在原文里**：它管的是 setup（`Level` / `Timing` / `Testflow` /
`TMLimits`），而 setup 属于工程侧；**它不碰测试结果**（推断，依据是全文没有一处提到 result）。

## 典型用法

**语料未写步骤。** 主文档没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`。

**本页能站得住的只有「从哪进」这一张表：**

| 你在哪 | 走哪个入口 | 依据（原文） |
|---|---|---|
| 在 Test Program Explorer 里正常操作 | **不用特意做什么**——载入/保存 setup component 时脚本自动被调 | `by means of the scripts that are called when a setup component is loaded or saved` |
| 命令行 | 命令行入口 | `it can also be called from the command line` |
| 自己写的程序里 | 用户程序入口 | `or by user programs` |

**一条必须记住的前提条件**（这是本页唯一一条硬条件）：

> **多人要并行，前提是「不改同一个 part」（`provided that they do not change the same part of it`）。**
> **前提不成立时会怎样，本页不知道。**

**一条从版本段推出来的操作前提**（推断）：

> **要用它管 TMLimits setup，得是 SmarTest 6.5.3 或更高**——
> 版本段写着 `SmarTest 6.5.3: TMLimits setup is now supported`。

**本页说不出「建 master file 的步骤」「collision 怎么解」**——那分别在两条未读的子主题里。

## 和谁有关

- [[test-program-explorer]] — **主要挂载点。** 原文 `The tool is integrated into the Test Program
  Explorer by means of the scripts that are called when a setup component is loaded or saved`。
  **本工具没有自己的主界面，它寄生在那一侧的 load / save 上**（推断）。
- [[level]] — 四种受管 component 之一（`Level setup`），**排第一**。
- [[timing]] — 四种之一（`Timing setup`）。
- [[testflow]] — 四种之一（`Testflow setup`）。
- [[tmlimits]] — 四种之一（`TMLimits test table setup`）；**它是 6.5.3 才加进来的那一种**。
- [[level-master-file]] — **「master file」在本页唯一有直接证据的落点**：
  子主题标题 `Creating a level master file`。**这一页讲的是那种文件本身**，
  **本页讲的是「谁来建、怎么并存」**（推断：两页是同一对象的不同侧面，**但原文没说**）。
- [[timing-master-file]] / [[testflow-master-file]] / [[pin-configuration-master-file]] /
  [[pattern-master-file]] — **同族页。本页原文一个都没提**；
  把它们列在这里是**推断**，依据是「master file 这个命名族存在」。
  **同理，`TMLimits` 一侧本页找不到对应的 master file 页可链——语料未写。**
- [[project]] — 本页 `stage: project` 的落点：它管的是工程侧的 setup。
- [[level-setup-tool]] / [[timing-setup-tool]] / [[testflow-tool]] — **各自 setup 的编辑工具**。
  **原文没有提过它们一个字**（推断：本工具管的是这些 setup 的**多人并行**，
  **编辑本身仍然是那些工具的事**——**但这是推断，本页不写死**）。
- [[smartest-6.5.3]] — 本页版本段的第二条落在它上面（TMLimits 支持）。
- [[smartest-6.3.2]] — 本页版本段第一条提到的上界版本。
- `Concept of the Setup Management Tool`（**未建、未读**）— **本工具的原理**，含 master file 机制。
- `Using the Setup Management Tool from the Test Program Explorer` / `… from the Command Line`
  （**均未建、未读**）— 两种入口的具体操作。
- `Creating a level master file`（**未建、未读**）— 建 master file 的步骤。
- `Collision handling`（**未建、未读**）— **那个缺口（改到同一部分怎么办）的答案在这里。**

## 版本

`## Functional changes` 段有，**两条**：

> 「**Introduced before SmarTest 6.3.2**」
> 「**SmarTest 6.5.3**: **TMLimits setup is now supported**」

| 条目 | 性质 | 本页能说的 |
|---|---|---|
| `Introduced before SmarTest 6.3.2` | **只给上界**（`before`） | **只知道 6.3.2 之前就有它；引入版本语料未写** |
| `SmarTest 6.5.3: TMLimits setup is now supported` | **一个确定的版本号 + 一件确定的事** | **6.5.3 起支持 TMLimits setup** |

> **第一条用的是 `before`，不是版本号**——这和同批的 [[error-map-tool]] 是同一句写法。
> **本页没有把它转述成「SmarTest 6.3.2 引入」。**
>
> **第二条反过来是精确的**，所以本页敢用它推出「四种受管 component 的清单是 6.5.3 之后的形状」。

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04_Setup_Management_Tool.md`

**这就是本页正文的全部依据。整篇 29 行，正文约 5 句。**

**本页没做的**：

- **五条子主题一篇都没读**：`Concept of the Setup Management Tool`（`…04.01`）、
  `Using the Setup Management Tool from the Test Program Explorer`（`.02`）、
  `Using the Setup Management Tool from the Command Line`（`.03`）、
  `Creating a level master file`（`.04`）、`Collision handling`（`.05`）。
  **直接后果有两个**：
  **① 本工具「怎么做到互不干扰」的原理，本页没有**（在 `Concept of…` 里）；
  **② 改到同一部分时怎么办，本页没有**（在 `Collision handling` 里）。
- **「语法 / 参数」节只有 70 字符**，就是那句
  `See the examples in each kind of setup master file collision handling.`——
  **它是脚本从子主题 `Collision handling` 逐字抽的，那一篇本页没读**，
  **所以这 70 字本页没有当作依据用**，只在「是什么」里当作「master file 这个词存在的证据」引用了一次。
- **它的来源文档自己也没有 「Syntax」/「Parameters」/「Example」段标记**，
  跟着 `Subtopics` 往下找一层才捞到那一条 Example（§4）。
- **一条接口缺口，照实记**：原文列了**三种**入口
  （`integrated into the Test Program Explorer` / `from the command line` / `by user programs`），
  **子主题只为前两种各写了一篇，第三种没有对应的篇目**。
  **本页不把它算成语料瑕疵**（因为原文没有自相矛盾，只是没展开），**但它是本页的一个空洞。**
- **一张图没看**：主文档正文没有内嵌图片，**本页没有任何来自图的结论**。
- **没有查 `setup component` 的定义**，**没有查 `distributed` 在这里指什么**
  （是跨机器、跨 workspace 还是别的），**也没有查 master file 的文件格式**。
- **没有读 [[tmlimits]]、[[level-master-file]] 等页**——上一条关系里的对应都是按名字接的。

> ⚠️ **语料瑕疵，照实记下、一处没替它改**（§11.2）：
>
> **① 所有格缺撇号**（逐字引）：
> `…in parallel without interfering with each others work.`
> ——**`each others work` 应为 `each other's work`**。
>
> **② 同一个名字在同一篇里大小写不一致**（逐字引两处）：
> 标题（frontmatter 与本页 H1）是 `Setup Management Tool`，
> 而正文第一句是 `The Setup Management **tool** enables multiple users…`，
> 正文第四句又是 `The Setup Management **tool** can handle the following setup components:`。
> ——**标题用大写 `Tool`，正文两处都用小写 `tool`。**
> **本页在正文里引用时按原文的小写写，不改它。**
>
> **③ 版本段第一条用的是 `before`，不是一个可引用的版本号**（逐字引）：
> `- Introduced before SmarTest 6.3.2`
> ——**它只给上界**。**本页在 `## 版本` 里把这一点写明了，没有把它当成「6.3.2 引入」。**
>
> 除这三处外，**本篇没有发现链接指错**：五条子主题的相对链接
> （`<01.01.07.02.02.04.0N_*.md>`）**与条目名一一对应**。

`verified: doc-only`

