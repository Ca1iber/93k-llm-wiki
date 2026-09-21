---
type: object
title: Shmoo Tool
layer: gui
stage: results
tags: [shmoo-tool, results, shmoo, testflow, gui]
related: [integrated-result-tool, testflow-tool, testflow, test-suite, report-window, smartest-7.2.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25_Shmoo_Tool.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Shmoo Tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Shmoo Tool 干两件事。** 原文第一句就是全部定义：

> 「The Shmoo Tool helps you to **create shmoo tests** and **view shmoo plots**.」

**这两个动词是本页的总纲，也是本页最容易被混掉的一处：**

| 动词 | 对象 | 是哪一侧 |
|---|---|---|
| `create` | **shmoo tests**（shmoo 测试本身） | **生成侧**——你要先造出一个测试 |
| `view` | **shmoo plots**（shmoo 图） | **查看侧**——跑完了看图 |

**原文用 `and` 把两侧并列写在一句里，说明同一个工具里两侧都有。**
**注意宾语不同：`test` 和 `plot` 是两个东西。** 造的是 test，看的是 plot。

### 六项能力

原文紧接着用 `You use the Shmoo Tool to:` 列了一张清单。**这张清单被两段正文打断了
（见 `## 出处` 的瑕疵④），本页把它拼回一张表**：

| 能力 | 原文 | 说明 |
|---|---|---|
| **对功能测试做 shmoo** | `Perform shmoo over a functional test` | 对象是 functional test |
| **对已有 test suite 做 shmoo** | `shmoo over an existing test suite or multiple test suites` | **一个或多个 test suite**（`or multiple`） |
| **MTP 的 fail bit count shmoo** | `fail bit count shmoo for MTP` | 一种专门的 shmoo |
| **自定义 shmoo 测试** | `customized shmoo tests` | 兜底项 |
| **多 site shmoo 测试** | `Peform multisite shmoo tests` | 见 `## 出处` 瑕疵①（原文这里拼错了） |
| **叠加 shmoo 图** | `Overlay shmoo plots` | **`Overlay`（叠加）——把多张图叠在一起看** |

**外加一条正面说明的附带能力**：

> 「When shmooing a test suite, you can **view value results on the shmoo plot**.」
>
> ——**对 test suite 做 shmoo 时，可以在图上看到 value 结果。**
> **注意它的适用范围：原文限定了 `When shmooing a test suite`**（推断：
> 对 functional test 做 shmoo 时有没有这一条，原文没说）。

### 三步生命周期：set up → execute → view

原文有一句把三篇子主题串起来的指路：

> 「For details, see **set up**, **execute** and **view** shmoo tests.」

**这三个动词是有序的，而且是本页唯一一条能站得住的流程**（见 `## 典型用法`）。
**注意第三个词是 `view shmoo tests`**——原文这里说的宾语是 `tests`，
而第一句说的是 `view shmoo plots`。**两处宾语不一致，本页照实并列，不调和**
（推断：`view` 的对象在这个工具里就是「测试的图」，但原文措辞确实不同）。

### 两道「必须先传到 testflow」的门槛

**这是本页最实用的一条，原文把它写了两遍**：

| 跨工具能力 | 原文的前置句 |
|---|---|
| **把 shmoo 数据写进 report window，并把 shmoo 图存成 PNG 或 ASCII** | 「To do this, you must **transfer the shmoo tests from the Shmoo Tool to a testflow first**.」 |
| **在 Integrated Result Tool 里显示 shmoo 图** | 「To do this, you must **transfer the shmoo tests from the Shmoo Tool to a testflow first**.」 |

> **两句的前置条件一字不差。** 原文用 `must`（必须）+ `first`（先）——
> **不是「建议」，是硬前置。** **所以这两件事在本工具里做不了，得先过 testflow 这道门。**

### 与 Testflow Tool 的三种来往

原文说 `Interact with the Testflow Tool` 是为了三件事，**三件的性质不同**：

| 目的 | 原文 | 要不要先传 |
|---|---|---|
| 显示某个 shmoo test suite 的 shmoo 图 | `Display the shmoo plot of a shmoo test suite` | — |
| **在 Shmoo Tool 和 test suite 之间传递 shmoo setup** | `Transfer a shmoo setup between the Shmoo Tool and a test suite` | — |
| 写报告窗 + 存 PNG/ASCII | `Log shmoo data into the report window and save shmoo plots as PNG or ASCII files` | **要** |

**第二条的 `between … and …` 是双向的**：setup 可以从工具传到 suite，也可以从 suite 传回来。
**这一点值得记：它和上面那条「tests 从工具传到 testflow」是两个不同方向、不同层次的东西**
（一个是 **setup**，一个是 **tests**）——**原文用了两个不同的词，本页不把它们当成同一件事。**

### 四条子主题

| 子主题 | 从标题能读出的（**推断**） |
|---|---|
| `Opening the Shmoo Tool` | **怎么打开它**——单列一条，说明「打开」本身有内容 |
| `The interface of the Shmoo Tool` | 界面 |
| `Using Shmoo Tool` | 用法 |
| `Appendix: Commands in the Shmoo Tool` | **一套命令的附录** |

> **第四条值得单独说一句**：标题写的是 `Commands`（命令），
> **说明这个工具有可以敲的命令**——但**本页「语法 / 参数」节是空的**
> （文档没有 `Syntax` / `Parameters` / `Example` 段标记，脚本一个字都没收）。
> **命令清单在哪、有多少条，本页一个字都不知道**——**它在那一篇没读的附录里。**

## 典型用法

**语料未写步骤细节。** 主文档没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`。

**本页能给出的流程只有一条，来自原文那句指路**：

> **`set up` → `execute` → `view`**
> （原文：`For details, see set up, execute and view shmoo tests.`）

**这条链的顺序是原文的语序给的**，**不是本页猜的**。但**每一步怎么做，原文一个字没说**——
三篇对应的子主题（`Setting up a shmoo test with the Shmoo Tool`、
`Executing shmoo tests with the Shmoo Tool`、`Viewing shmoo plots with the Shmoo Tool`）
**本页一篇都没读**。

**第二条要记的顺序规则：跨工具的两件事要先过 testflow。**
**顺序是**：造 shmoo 测试 → **传到 testflow** → 才能写报告窗 / 存 PNG·ASCII / 在 Integrated Result Tool 里看图。

**第三条：打开工具本身是第一步，而且是单列一篇的。**
原文把 `Opening the Shmoo Tool` 放在子主题第一条（推断：打开动作有前提或多种入口，
**但本页没读那篇，不知道是什么**）。

**常见的组合（推断，依据是原文的清单）**：
多个 site 一起 shmoo → 用 `Overlay` 把图叠起来看；
对 test suite 做 shmoo → 顺便看 value 结果。

## 和谁有关

- [[integrated-result-tool]] — **下游（显示侧），且有硬前置。**
  原文 `Interact with the Integrated Result Tool to display shmoo plots in the Integrated Result Tool`，
  **并且明写 `you must transfer the shmoo tests from the Shmoo Tool to a testflow first`**。
  **本页是 shmoo 的生成侧，那一篇是显示侧**——这是两页的分工。
- [[testflow-tool]] — **关键中间环节。** 原文把 `Interact with the Testflow Tool` 单列一条，
  **两道跨工具门槛都卡在它身上**。**没有它，本工具的两项输出能力都用不了。**
- [[testflow]] — 同上的落点：原文 `transfer the shmoo tests from the Shmoo Tool **to a testflow** first`。
- [[test-suite]] — **既是 shmoo 的对象，也是 setup 交换的另一端**：
  原文 `shmoo over an existing test suite or multiple test suites`、
  `Transfer a shmoo setup between the Shmoo Tool and a test suite`。
- [[report-window]] — **输出目的地之一**：原文 `Log shmoo data into the report window`。
  **同样要先传到 testflow。**
- [[mtp-memory-test]] — 原文有 `fail bit count shmoo for MTP` 一项。
  **原文只写了缩写 `MTP`、没有展开**，**本页把它接到这一页是推断**（依据是缩写与页名的对应），
  **`fail bit count shmoo` 具体是什么，本页讲不出来。**
- [[controlling-multiple-sites]] — 原文有 `Peform multisite shmoo tests` 一项。
  **本页没有「multisite 怎么配」的任何内容**（推断：这是同一主题的另一侧，**但原文没说**）。
- [[smartest-7.2.2]] — 本页 `## 版本` 的两条都落在它上面。
- `Opening the Shmoo Tool` / `The interface of the Shmoo Tool` / `Using Shmoo Tool` /
  `Appendix: Commands in the Shmoo Tool`（**均未建、未读**）— 本工具的四条子主题。
  **前三条是打开、界面、用法，最后一条是命令附录。本页对它们零覆盖。**
- `Setting up a shmoo test with the Shmoo Tool` / `Executing shmoo tests with the Shmoo Tool` /
  `Viewing shmoo plots with the Shmoo Tool` / `Viewing the test results of a test suite on the shmoo plot` /
  `Viewing the shmoo plots of different sites` / `Overlaying shmoo tests in the Shmoo Tool` /
  `Saving shmoo plots to png or ASCII files` / `Interaction with testflow` /
  `Interaction with the Integrated Result Tool`（**均未读**）— 原文正文内链直接指向的九篇。
  **本页的流程骨架就是它们串起来的，但内容一篇都没有。**
- [[analysis-views]] — 同批建的 `results` 页。**两页都讲 shmoo 图，但角度不同**：
  本页是**生成 shmoo**，那一页是**把已有的 shmoo 结果当一种视图画出来**
  （推断，依据是那一页的标题落在 analysis view 这一类里）。**原文没有说两者关系。**

## 版本

`## Functional changes` 段有，**两条，都落在同一个版本上**：

> 「SmarTest **7.2.2**: Introduces **shmoo over multiple test suites**.」
> 「SmarTest **7.2.2**: Saves shmoo plots and results as **ASCII files**..」（原文结尾有两个句点，见 `## 出处` 瑕疵②）

**两条都是 7.2.2 的新增，没有更早或更晚的条目。**

⚠️ **本页要特别指出一条：这一篇没有「Introduced in …」条目。**
（对比同批的 [[integrated-result-tool]] 写的是 `Introduced in SmarTest 7.2.0`，
[[error-map-tool]] 写的是 `Introduced before SmarTest 6.3.2`。）
**所以 Shmoo Tool 是哪个版本引入的，语料未写**——
**它 7.2.2 之前就在了**（推断，依据是 7.2.2 的两条都写着 `Introduces` / `Saves`，
即「新增能力」而不是「引入工具」），**但早到什么时候，本页不知道。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25_Shmoo_Tool.md`

**这就是本页正文的全部依据。整篇 39 行，正文约 15 行。**

**本页没做的**：

- **四条子主题一篇都没读**：`Opening the Shmoo Tool`（`02.08.04.25.01`）、
  `The interface of the Shmoo Tool`（`.02`）、`Using Shmoo Tool`（`.03`）、
  `Appendix: Commands in the Shmoo Tool`（`.04`）。
  **结果是：怎么打开、界面什么样、怎么操作、命令有哪些——本页一个字都没有。**
- **正文内链指向的九篇一篇没读**：`Setting up a shmoo test…`、`Executing shmoo tests…`、
  `Viewing shmoo plots…`、`Viewing the test results of a test suite on the shmoo plot`、
  `Viewing the shmoo plots of different sites`、`Overlaying shmoo tests in the Shmoo Tool`、
  `Saving shmoo plots to png or ASCII files`、`Interaction with testflow`、
  `Interaction with the Integrated Result Tool`。
  **`set up / execute / view` 这三步各自怎么做，本页全空**——
  **本页只有这三个动词，没有它们的任何一个细节。**
- **一张图没看**：主文档正文没有内嵌图片，**本页没有任何来自图的结论**——
  **shmoo plot 长什么样、overlay 之后什么样，本页不知道。**
- **「语法 / 参数」节是空的，这不是省略**：本文档没有 `Syntax` / `Parameters` / `Example`
  这类段标记，跟着 `Subtopics` 找一层也没有（脚本的判定，§4）。
  **但注意**：子主题里有一条叫 `Appendix: Commands in the Shmoo Tool`——
  **说明命令是存在的，只是不在本页**（推断，依据是那条标题用了 `Commands`）。
- **没有查 `MTP` 是什么**、**没有查 `fail bit count shmoo` 是什么**、
  **没有查 `multisite` 在本工具里怎么配**。
- **没有查 `SmarTest 7.2.2` 在版本线上的位置**，也没有读 [[smartest-7.2.2]] 那一页。

> ⚠️ **语料瑕疵，照实记下、一处没替它改**（§11.2）：
>
> **① 拼写错**（逐字引）：`- [Peform multisite shmoo tests](<02.08.04.25.03.04.07_Viewing_the_shmoo_plots_of_different_sites.md>).`
> ——**`Peform` 应为 `Perform`**。**本页在正文里引用它时保留了原文的错法并注明，没有替换成正确拼写。**
>
> **② 句尾双句点**（逐字引）：`- SmarTest 7.2.2: Saves shmoo plots and results as ASCII files..`
> ——**结尾有两个 `.`**。
>
> **③ 正文与版本段措辞不一致**，本页并列、**不调和**：
> 正文写 `Log shmoo data into the report window and **save shmoo plots as PNG or ASCII files**`；
> 版本段写 `Saves **shmoo plots and results** as **ASCII files**`。
> **两处差两点**：版本段多了 `and results`，正文多了 `PNG`。
>
> **④ 无序列表被正文打断**（逐字引证据）：
>
> ```
> You use the Shmoo Tool to:
>
> - Perform shmoo over a functional test, shmoo over an existing test suite or multiple test suites, fail bit count shmoo for MTP, and customized shmoo tests.
>
> When shmooing a test suite, you can [view value results on the shmoo plot](<...>).
>
> For details, see [set up](<...>), [execute](<...>) and [view](<...>) shmoo tests.
>
> - [Peform multisite shmoo tests](<...>).
> ```
>
> ——**`You use the Shmoo Tool to:` 引出的清单，第一条之后插进了两段正文，
> 列表到 `For details, see …` 之后才续上。** 所以这张清单在原文里是**断成两截的**。
> **本页在「是什么」里把它拼回一张表，并在此声明拼接是编辑动作，不是原文的样子。**
>
> **⑤ 同一件事的宾语不一致**（逐字引）：第一句 `view shmoo **plots**`，
> 指路句 `and [view](<...>) shmoo **tests**`。
> **本页并列两处措辞，不判哪个对。**

`verified: doc-only`

