---
type: object
title: Flow Data Editor
layer: gui
stage: testflow
tags: [flow-data-editor, testflow, gui, testflow-tool, test-suite, bins, variables, flags, setups, tabular-editor]
related: [testflow, mapping-testflow, flow-sequence-editor, testflow-tool, testflow-file, test-suites-page, test-suite, test-suite-control-api, flags-page, bin, assign-value-node, testflow-properties-view, level-spec, svlr, spec-tool]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01_Flow_Data_Editor.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Flow Data Editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **164 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01_Flow_Data_Editor.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.05_Variables_page.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Variables page）

You can use a user flag to branch in a testflow, depending on the current value of the flag. This lets you control the testflow execution during a test program run.

<!-- 语法节 end -->

## 是什么

**Flow Data Editor 是 Testflow Tool 里那个「表格形态」的编辑器，一共八页。**
它的定义文档**只有一句话讲它自己**：

> 「The Flow Data Editor consists of eight pages.」

**这篇文档是一个目录页，不是说明书**：正文除了那句「八页」之外，就是一张截图、两份**逐字相同**的八页链接清单，再加两句 `Related information`。**八页各自的正文都不在这一篇里**（见「出处」）。

### 八个页签，以及它们在 wiki 里对应谁

原文 `#### Subtopics` 的清单（顺序与图上页签一致）：

| # | 页签 | 本 wiki |
|---|---|---|
| 1 | Test Suites page | [[test-suites-page]]（**已建**） |
| 2 | Parameters page | `Parameters page`（**未建**） |
| 3 | Tests page | `Tests page`（**未建**） |
| 4 | Bins page | `Bins page`（**未建**；[[bin]] 是 bin 这个概念，**不是这一页**） |
| 5 | Variables page | `Variables page`（**未建**） |
| 6 | Flags page | [[flags-page]]（**已建**） |
| 7 | Setups page | `Setups page`（**未建**） |
| 8 | Information page | `Information page`（**未建**） |

**「Test Suites page」与「Tests page」是两个不同的页签**，名字只差一个词——**原文两份清单里就是这么并列的**。

### 图：`raw/110689.png`（**本页 `sources:` 里唯一的一张图**）——**不算 ④**

alt 文字是 `Flow Data Editor`（**alt 是文本**）。
**这一张按 §11.4 的判据不算 ④**：图里读出来的字**逐个回语料里 grep 过，全都有命中**
（逐条见下面那张表）——**没有一个是 0 命中**，所以它**补了正文没写的结构，但不占 ④ 档**。
图里逐字可读的是：

- **窗口标题**：`testflow`
- **底部一排八个页签**，逐字与顺序：
  `Testsuites` → `Parameters` → `Tests` → `Bins` → `Variables` → `Flags` → `Setups` → `Information`
- **表头**：`Test Suite Name`，右边一个**跨三列的组头 `Timing`**，它下面三列 `Eqn` / `Desc` / `Spec/Waveform Set`
- **两行数据**：`1  continuity  1  gross_func_eqn  2`（第一行被选中高亮）与 `2  gross_func  1  gross_func_eqn  1`

**它解决掉的是两件事：**

| 图解决了什么 | 图里的字 grep 得到吗（逐条实测） |
|---|---|
| **「八个页签确实在窗口底部、而且顺序与子主题清单一致」** | 八个页签名**单个都能搜到**（`Testsuites` / `Parameters` / `Variables` / `Setups` 等在别篇有命中）——**但这一排的顺序在 raw 里没有一处这么写** |
| **Test Suites 页的表头结构**：`Test Suite Name` + 一个跨三列的 `Timing` 组（`Eqn` / `Desc` / `Spec/Waveform Set`） | `Spec/Waveform Set` 只在 `02.08.04.32.02.01.06` **一篇**里有（**不在本页 `sources:`，本页没读它**）；`Test Suite Name` 10 篇、`Desc` 2,010 篇、`Eqn` 29 篇、`Timing` 733 篇（**都不在 sources**）——**列名全都搜得到**，其中 **`Desc` 这一列在 `02.08.04.32.02.01.16` 的 CSV 导出例里逐字写着**（`Tim Eqn Desc` / `Tim Spec Desc`，**也不在 sources**）；**只有「`Timing` 是跨住这三个子列的组头」这一件 raw 里一处都没有** |

**所以这一张能贡献的、raw 里查不到的，只剩结构性的两件**：**窗口底部那一排页签的顺序**，
以及**「`Timing` 是跨三列的组头」**——**字符串层面的列名一个都不缺**（`Desc` 也包括在内）。
**读者要核这两件只能自己再开 `110689.png`**（§11.4：图证比①②③都硬，但不可检索；
**而这一张按「图里的字 grep 不到」那条判据不占 ④ 档**）。
**窗口标题 `testflow` 是常见串，不构成证据**，本页不拿它当结论。

### ⚠️ 一处图与正文的用词差（照实并列，不替语料统一）

图上页签逐字是 **`Testsuites`（一个词）**，而本篇正文一律写 **`Test Suites page`（两个词）**。
**本页正文跟着原文写两个词，图上那一个词的写法在这里照实记下。**
（按 grep，一个词的写法在语料别处的**图片 alt 文本**里也出现过，
那一篇是 `02.08.04.32.02.01.06`——**不在本页 `sources:`，本页没有读它**。）

### 「语法 / 参数」节那一段不是这一篇写的

语法节页首写明了：那 164 字符**取自子主题 `02.08.04.32.03.01.05_Variables_page.md`**
（也就是上面第 5 个页签）。**那片子主题本页没读**——
所以**那段 `Example`（用 user flag 在 testflow 里分支）的上下文，本页一个字没有**。

## 典型用法

**本篇没有 `## Procedure`，也没有 `## Before you begin`。** 正文给的动作只有两条：

| 想干什么 | 去哪里 | 原文 |
|---|---|---|
| 看八页各自的细节 | 点那八个链接 | `For details on the eight pages see the links below:` |
| 打开这个工具 | `Opening the Testflow Tool`（**未建，本页没读**） | `## Related information` 第一条 |
| 搞清它和 [[flow-sequence-editor]] 怎么同步 | `Synchronization between the Flow Data Editor and the Flow Sequence Editor`（**未建，本页没读**） | `## Related information` 第二条 |

**所以「怎么用这个编辑器」本篇不回答——它只回答「它由哪八页组成」。**
八页里**每一页填什么、有哪些列**，要么去那八个子页，要么去看 [[mapping-testflow]]。

**[[mapping-testflow]] 主表里本页出现三次**（那是**那一页**的结论，不是本页的）：

| 那一行的目的 | 那一行的 GUI 格 |
|---|---|
| 把 setup 文件挂进 testflow 并加载 | **本页的 `Setups page`**（`File` 列怎么写，那里标了「④ 图证」，看的是 `110701.png`） |
| 定义 testflow 变量与初值 | **本页的 `Variables page`**（同行的 L2 格是 `GET_USER_FLAG` / `GET_USER_STRING` / `GET_USER_DOUBLE`） |
| 插 stop bin / otherwise bin / floating bin | **本页的 `Bins page`** + [[flow-sequence-editor]] |

**那三张图（`110701.png` / `110705.png` / `122906.png`）本页一张没看**——本页只开了 `110689.png`。

## 和谁有关

- [[testflow]] / [[mapping-testflow]] — **本页 `stage: testflow` 的理由**，`layer: gui` 说明它是编辑器不是接口。
- [[flow-sequence-editor]] — **它的对手编辑器**。原文 `Related information` 第二条就是「两者之间的同步」——**那篇本页没读，所以同步的规则本页一个字没有**。[[mapping-testflow]] 把「插 test suite、编排流程顺序」整行给了它，把「挂 setup 文件」「定义变量」「插 bin」三行的 GUI 格给了本页的三个子页——**两个编辑器分工不同，本页不替它写流程**。
- [[testflow-tool]] — **本页所在的工具**（原文 `Related information` 第一条是 `Opening the Testflow Tool`）。**那页本页没读。**
- [[testflow-file]] — **文件侧**：[[mapping-testflow]] 把上面三行的文件格分别填成 `context` section、`declarations` section、`test_flow`（`stop_bin`）与 `binning` section。**本页没有出处文档能证实这些落点**，本页只转述对照表。
- [[test-suites-page]] — **第 1 个页签的页**（已建；它的出处是 `02.08.04.32.03.01.01`）。**本页没读它。**
- [[flags-page]] — **第 6 个页签的页**（已建；出处是 `02.08.04.32.03.01.06`）。**本页没读它。**
- [[bin]] — **floating bin 定义在本页的 `Bins page` 上**——**这句话写在 [[bin]] 的出处文档里，本页的出处文档没有说**。两页互补，本页不搬那一段。
- [[assign-value-node]] / [[level-spec]] / [[svlr]] / [[spec-tool]]（**`assign-value-node` 未建**）— **同阶段对照表把「运行期改 level / timing spec 值」那一行挂给 [[flow-sequence-editor]] 的两个向导**（`assign level value` / `assign timing value`），**不是本页**；本页与那件事的关系只有「`Variables page` 上定义变量、`Setups page` 上挂 setup 文件」这一层。**四页本页都没读。**
- [[testflow-properties-view]] / [[test-suite-control-api]]（**前者未建**）— 同属 testflow 这一段的相邻页；**本页的出处文档一个字没提它们**，本页只把它们列在 frontmatter 的 `related` 里指路。
- **只写反引号、不写链接的名字**：`Parameters page`、`Tests page`、`Bins page`、`Variables page`、`Setups page`、`Information page`、`Test Suite Name`、`Timing`、`Eqn`、`Desc`、`Spec/Waveform Set`、`Setups page` 上的 `File` 列——**它们都不在 `extract/prose-allowlist.txt` 里**，按 §9.1 一律反引号。

## 版本

本文档**有** `## Functional changes` 段，四条：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.2: Testtree page is removed.`
- `SmarTest 6.5.2: Test suites page replaces Testlist page.`
- `SmarTest 6.5.2: Tests page replaces Limits page.`

**第一条是哨兵值**（`schema.md` §11.2②）：`Introduced before` 的意思是「在本文档集覆盖范围开始之前就已经有了」——**不是「6.3.2 新增了 Flow Data Editor」。**

**后三条讲的是同一件事：这一版把页签重排了一遍。** 三条合起来读：

| 6.5.2 之前有过 | 6.5.2 之后 |
|---|---|
| Testtree page | （**removed**，八页里没有它了） |
| Testlist page | Test Suites page |
| Limits page | Tests page |

**「八页」是重排之后的结果**（**推断**，依据是「Testtree page is removed」+ 正文那句 `consists of eight pages` + 图上那八个页签）。
**6.5.2 之前一共几页、还删过别的没有，原文没说。**

> **⚠️ 一处要照实说的**：上面被替换掉的两个页名（`Testlist page`、`Limits page`）
> **都不在正文那份八页清单里**——**这不是矛盾**（它们正是被替换掉的那两个），
> **本页并列两处，不替语料选一个。**

**同批条目也收在 `wiki/versions/` 的 [[smartest-6.5.2]] 页里**——**那页不是本页建的**，这里只指路。

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01_Flow_Data_Editor.md`
  （TDC `99271.htm`，1,825 字节 / 43 行）。**这一篇很短，是一条目录页。**
- **本页「语法 / 参数」节不是这一篇写的**：节首写明那 164 字符
  **取自子主题 `02.08.04.32.03.01.05_Variables_page.md`**。
  **那片子主题本页没读**——**所以那段 `Example` 的上下文、`Variables page` 上还有什么，本页一个字没有。**

### 本页读的图：**1 张**（`sources:` 里唯一的一张）

`raw/110689.png`（alt 文字 `Flow Data Editor`）。逐条结论在「是什么」的图那一段。
**图上读到的字逐条回语料里查过 grep 命中，全部都有命中（0 个 0 命中）**——
所以**这一张不算 ④**；命中的是**哪一篇、本页有没有读过它**都逐条写在上面那张表里，
**本页没有把那些命中当依据**（它们都不在 `sources:` 里）。

### 本页没做的

- **八个子页一篇没读**（`02.08.04.32.03.01.01`–`.08`），**包括 `Variables page` 与 `Bins page`**。
  **所以「每一页上有什么字段、能填什么、填错了会怎样」，本页一个字都没有**——
  本页只有「有哪八页」和图上能看见的那点表头。
- **原文 `Related information` 的两篇没读**：`Opening the Testflow Tool`、
  `Synchronization between the Flow Data Editor and the Flow Sequence Editor`——
  **所以「怎么打开它」「两个编辑器怎么同步」本页答不了**。
- **[[mapping-testflow]] ⑩ 里那三张本页子页的图（`110701.png` Setups 页、
  `110705.png` Flags 页、`122906.png` Bins 页）本页没看**——那三张的内容在那一页里，
  本页只引了那一页的结论，**没有自己去开图**。
- **`Testflow Tool` 那一章的三篇（`02.08.04.32`、`.01.02`、`.02.01.01`）没读**——
  所以**本页在整个 Testflow Tool 里的位置**本页写不出来。
- **没有实跑。** 没有开过这个编辑器、没有点过任何一个页签、没有编过 test suite。
  **`verified: doc-only` 指的就是这件事**——**图是一张截图，不是本页跑出来的。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **写这页时没有动 `wiki/index.md`、也没有把本页挂进 [[testflow]] 那页**；**两者已由本批收尾统一挂入**（`index.md` 的 `gui/testflow` 条、`stages/testflow.md:122`）。（**2026-09-20 更正**：原文写「没有挂进」——**收尾之后已经不成立**。）

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 八页清单在 raw 里出现两次，逐字相同。**
一次在 `#### Subtopics` 导航块里，一次在正文 `For details on the eight pages see the links below:` 之后。
**两次的八行逐字一样**——**语料结构如此**（导航块是生成器加的），本页照实记，**没有把重复的八行算成两件事**。

**② 图与正文对同一个页签有两种写法**：图上 `Testsuites`（一个词），正文 `Test Suites page`（两个词）。
**本页在「是什么」里并列两处，没有替语料统一。**

**③ `## Functional changes` 里被替换掉的 `Testlist page` / `Limits page`，八页清单里没有。**
**这不是矛盾**（它们在 6.5.2 被替换掉了），**本页在「版本」里并列两处，没有替语料调和措辞。**

**④ 本篇没有编码坏字（§11.2① 那一族）**：用 `[一-鿿]` 实测零命中；
**也没有 §11.2⑤ 那个整词替换**（`DC/DC power units` 实测 0 命中）。
**这不是「没找到」，是查过、结果为零。**

**⑤ 本页引文里出现的字段名（`Test Suite Name` / `Timing` / `Eqn` / `Desc` / `Spec/Waveform Set`）
一处都没有进 `>` 引文块**——按 §11.4，**图里读到的字不许当引文**，它们只在表格与散文里出现。

`verified: doc-only`
