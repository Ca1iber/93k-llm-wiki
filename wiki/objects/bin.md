---
type: object
title: Bins
layer: n/a
stage: testflow
tags: [bin, bins, binning, testflow, stop-bin, otherwise-bin, floating-bin, multibin, yield, gui]
related: [testflow, mapping-testflow, flow-sequence-editor, flow-data-editor, testflow-file, test-suites-page, test-suite, special-test-suites, results, hardware-bin-summary-tab, software-bin-summary-tab]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# Bins

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **260 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

If for some reason your production run should stop unexpectedly, all devices that have not ended up in either a good or bad bin will be assigned to the otherwise bin. This bin is also included in yield calculations, as it can be defined as a good or a bad bin.

<!-- 语法节 end -->

## 是什么

**Bins 是 testflow 给器件分类的机制：每个器件跑完，按结果被扔进某一个 bin。** 原文第一句就是来由：

> 「During a test, the tested devices normally need to be sorted according to their test results.」

> 「This is done by assigning the devices to different bins. For example, all devices that fail in a certain test suite will end up in one bin and not be tested any further.」

**一个 bin 能产生的东西是定死的两个**：

> 「A bin in a testflow can generate exactly one hardware bin and one software bin.」

**这是原文里唯一一句解释 hardware bin 与 software bin 关系的**——**两个 bin 号怎么算、谁统计哪个，本篇没有写**（它把多 site 与 Multibin SmartDisconnect 两个话题直接推给了两篇别的文档，见「和谁有关」）。

### 三型 bin

原文 `There are several types of bins:` 底下是一张三行的表。**这张表在 raw 里被压平成一串 ` | ` 管道行**（名字一行、说明一行，中间夹空行），**不是 markdown 表格**——所以它没有被收进本页的「语法 / 参数」节，本页在这里逐条写出：

| 型 | 原文的定义 | 在 testflow 里显不显示 |
|---|---|---|
| **stop bin** | 放「全好」或「全坏」器件的 bin，**插在 testflow 的某些点上** | **显示**——三角形绿色 good bin 或八角形红色 bad bin |
| **otherwise bin** | `A bin for all devices that do not fall into a stop bin.` | **不显示**（原文：`This bin node is not displayed in the testflow.`） |
| **floating bin** | 在 [[flow-data-editor]] 的 `Bins page` 里定义，**用作 multi-bin 的预定义 bin** | **自己不显示**，但它关联的 multibin 会显示 |

stop bin 的形态原文写得很具体：

> 「Stop bins are inserted at points in the testflow, and appear as either」

> 「- triangular green good bins, or」

> 「- octagonal red bad bins.」

**stop bin 的 good / bad 是插的时候定的**：

> 「When using the Flow Sequence Editor to insert the stop bin into your testflow, you can define it to be a good bin, or bad bin. The number of parts falling into these bins are included in yield calculations.」

（那句话里 `parts ... are` 主谓不一致，**原文如此**——见「出处」⚠️①。本页照原样引。）

**floating bin 是「先定义、后插入」两件事**：

> 「The floating bin is defined in the Bins page of the Flow Data Editor and is used as a predefined bin for the multi-bin.」

> 「The floating bin is not displayed in the Flow Sequence Editor but the associated multibin that you subsequently insert (using the Flow Sequence Editor) does show up.」

### otherwise bin：意外停机时的收容站

三型里只有它，原文单独给了一个 `Example`（**这一段就是本页「语法 / 参数」节里那 260 字符**）：

> 「If for some reason your production run should stop unexpectedly, all devices that have not ended up in either a good or bad bin will be assigned to the otherwise bin. This bin is also included in yield calculations, as it can be defined as a good or a bad bin.」

**读法**：otherwise bin 平时是空的，**只有 testflow 异常中断时才会装进东西**；**判据是「还没进过任何一个 good / bad bin」，不是「测试失败」。**

### ⚠️ 一处语料自相矛盾（照实并列，不替它调和）

上面那段 `Example` 说 otherwise bin `can be defined as a good or a bad bin`；而「三型 bin」那一行里写「可以定义成 good 或 bad」的是 **stop bin**（`you can define it to be a good bin, or bad bin`）。**otherwise bin 自己的定义只有两句，没有这一句。**
**两处都在同一篇里，本页并列、不判哪个对。**

### 为什么「语法 / 参数」节只有一小段

`Bins.md` **没有 `Syntax` / `Parameters` 这类段标记**，只有一个 `## Example`；脚本按段标记收，**所以只收到了那 260 字符**——三型 bin 的说明、`## Related information`、`Functional changes` 都没进去。**这不是本页删的**（§4：没有段标记时脚本一个字都不收，见语法节页首那五行）。

## 典型用法

**插 bin 的动作，原文只给了两个入口，而且都没给步骤。**

| 你要插什么 | 在哪插 | 原文的措辞 |
|---|---|---|
| **stop bin** | [[flow-sequence-editor]] | `When using the Flow Sequence Editor to insert the stop bin into your testflow, you can define it to be a good bin, or bad bin.` |
| **floating bin** | **先在 [[flow-data-editor]] 的 `Bins page` 里定义**，再用 [[flow-sequence-editor]] 插它关联的 multibin | 见上面 floating bin 那两句 |

**两条顺序（文档事实）**：

- **floating bin 是先定义、后插入**——它是 `a predefined bin for the multi-bin`，**没定义就没有可插的东西**。
- **stop bin 的 good / bad 是插入那一刻定的**（`you can define it`）——**同一个节点两种去向，取决于你当时怎么填。**

**本篇没有 `## Before you begin`，也没有 `## Procedure`。** `## Related information` 指的那篇
`Inserting a bin into the testflow`（`02.08.04.32.02.01.05`）**本页没读**——**「插一个 bin 的具体步骤」本页一个字没有。**

## 和谁有关

- [[testflow]] / [[mapping-testflow]] — **本页 `stage: testflow` 的理由**。[[mapping-testflow]] 主表第 113 行「插 stop bin / otherwise bin / floating bin」把这一件事分到了五个格：**GUI 格 = [[flow-sequence-editor]] 的 `goodbin` / `badbin` / `Multi Bin` 与 [[flow-data-editor]] 的 `Bins page`；文件格 = [[testflow-file]] 的 `test_flow`（`stop_bin`）与 `binning` section；L1 格 `—`；L2 格 `SET_MULTIBIN`；L3 格 `?`**。**本页只写 bin 是什么；那些跨层落点全在对照表里，本页不搬。**
- [[flow-sequence-editor]] — **插 stop bin 的地方**（原文点名）。**那页本页没读**，所以**它在 GUI 上长什么样、`goodbin` / `badbin` 是不是它的节点名，本页不写**（那两个名字来自 [[mapping-testflow]]，不是本页的出处）。
- [[flow-data-editor]] — **定义 floating bin 的地方**（原文点名 `the Bins page of the Flow Data Editor`）。那页的八个页签里就有一个 `Bins`。**那页本页没读**；`mapping-testflow` ⑩ 说它有一张图 `122906.png`，**本页也没看**。
- [[test-suites-page]] / [[test-suite]] / [[special-test-suites]] — 与 bin 直接相关的两个 **special test suite** 是 `bin_disconnect` 与 `multi_bin_decision`；[[mapping-testflow]] 把它们的 L2 格分别填成 `DISCONNECT` 与 `SET_MULTIBIN`。**这两个名字在本页的出处文档里一个字都没有**——**本页不把它们写成 bin 的机制**。
- `Multibin SmartDisconnect test suite`（**未建**）— 原文第二句就点名的一篇；**本页没读**（`mapping-testflow` 主表另有一行给它，L2 格是 `GET_DISCONNECT_CONTEXT()`）。
- `Inserting a bin into the testflow`（**未建**）— `Related information` 指的那篇；**插 bin 的步骤在那篇里**。
- `Use of bins with multisite tests`（**未建**）— 原文第二句点名的另一篇；**多 site 场景下 bin 怎么算，本页一个字没有**。
- `Multibin Disconnect` / `Multi Bin`（**均在 [[flow-sequence-editor]] 那侧，未建**）— **floating bin 的落点**（原文：`the associated multibin that you subsequently insert`）。
- [[hardware-bin-summary-tab]] / [[software-bin-summary-tab]]— 原文只说了「一个 bin 生成各一个 hardware bin 与 software bin」；**那两个 bin 在结果侧怎么看，在那两页里**（**推断**，依据只有页名与 `hardware bin` / `software bin` 同词，**本页没有读过它们**）。
- [[results]] — **bin 是结果侧统计的对象**（原文两处点名 yield 计算用它）。**本页没有读任何 results 页**，所以**「yield 怎么算」本页答不了**。
- **只写反引号、不写链接的名字**：`Bins page`、`Multi Bin`、`goodbin` / `badbin`、`bin_disconnect`、`multi_bin_decision`、`SET_MULTIBIN`、`stop_bin`、`binning`、`test_flow`、`hardware bin` / `software bin`——**它们都不在 `extract/prose-allowlist.txt` 里**，按 §9.1 一律反引号。

## 版本

本文档**有** `## Functional changes` 段，两条：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.2: The floating bin.`

**第一条是哨兵值，不是「6.3.2 的变更」**（`schema.md` §11.2②）：`Introduced before` 说的是「**在本文档集覆盖范围开始之前就已经有了**」——**照字面读会生成一条「6.3.2 新增了 bins」，那是错的。**

**第二条只钉住 floating bin 这一型**，而且它**是一个没有动词的残句**（见「出处」⚠️④）：

> 「SmarTest 6.5.2: The floating bin.」

**照字面只能读出「floating bin 与 6.5.2 有关」**——**是新增还是改动，原文没说，本页不替它补动词。**

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.md`
  （TDC `20229.htm`，2,113 字节 / 60 行）。
- **本页「语法 / 参数」节的来源就是这一篇自己**（节首没有「取自子主题」后缀），
  节里那 260 字符就是原文唯一的 `## Example`。

### 本页读的图：**0 张，因为这一篇一张图都没有**

**实测该篇对 `raw/` 的图片引用 0 处**（`grep -o 'raw/[0-9]*\.\(png\|jpg\)'` 零命中）。
**这不是「图够不着」，是这一篇本来就不带图**——所以本页**没有任何来自图的结论**，
也没有任何一处需要标「④ 图证」。

### 本页没做的

- **原文点名的五篇一篇没读**：`Use of bins with multisite tests`（`03.02.02.06.08`）、
  `Multibin SmartDisconnect test suite`（`02.08.04.32.01.02.01.04`）、
  `Inserting a bin into the testflow`（`02.08.04.32.02.01.05`）、
  `Flow Sequence Editor`、`Flow Data Editor`。
  **所以「多 site 怎么分 bin」「Multibin SmartDisconnect 怎么用」「插 bin 的步骤」本页一个字都没有。**
- **`Bins page` 那篇（`02.08.04.32.03.01.04`）没读**——**floating bin 在那一页上要填哪几格、
  `Software Bin` / `Hardware Bin` 那些列是什么，本页答不了**。
  （`mapping-testflow` ⑩ 里那张 `122906.png` 就是那一页的截图，**本页没有开它**。）
- **`hardware bin` 与 `software bin` 的关系只到「各一个」为止**——那 1:1 是怎么落地的，
  本篇没有第二句。
- **`special-test-suites` 那篇没读**——`bin_disconnect` / `multi_bin_decision` 两个 special
  test suite 的正文本页没有。
- **没有实跑。** 没有开过 testflow、没有插过任何 bin、没有跑过 production run，
  也就没有见过 `otherwise bin` 真的被用到。**`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **写这页时没有动 `wiki/index.md`、也没有把本页挂进 [[testflow]] 那页**；**两者已由本批收尾统一挂入**（`index.md` 的 `n/a/testflow` 条、`stages/testflow.md:128`）。（**2026-09-20 更正**：原文写「没有挂进」——**收尾之后已经不成立**。）

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 一处主谓不一致：`The number of parts falling into these bins are included in yield calculations.`**
主语中心词是 `number`，动词该是 `is`。**本页正文引了这一句，一处没动。**

**② 一处跨段的说法不一致：otherwise bin 能不能定义成 good / bad。**
`Example` 说它能（`it can be defined as a good or a bad bin`），
而三型表里把这句写给了 **stop bin**，otherwise bin 自己的定义没有这一句。
**本页在「是什么」里并列两处，没有替语料选一个。**

**③ 一处拼法不统一：同一个东西在同一段里三种写法。**
`multi-bin`（`a predefined bin for the multi-bin`）、`multibin`（`the associated multibin`）、
`Multibin SmartDisconnect test suite`——**逐字如此，本页照原样写，不统一。**

**④ 版本条目是一个没有动词的残句**：`SmarTest 6.5.2: The floating bin.`
**它既没说「新增」也没说「改了」**——本页不替它补。（同批的 `SmarTest 6.5.2: Testtree page is removed.`
是有动词的，**所以这不是版本条的固定格式**。）

**⑤ 三型 bin 的那张表在 raw 里是压平的管道行**，不是 markdown 表格
（形如单独一行 ` | `、值一行、说明一行）。**这与 `xps256-status-flags` 那页记的
「18 张表」是同一类现象**：HTML 转 markdown 时被拆开了。**逐字没丢，只是没法当表读。**

**⑥ 本页这一篇没有编码坏字（§11.2① 那一族）**：用 `[一-鿿]` 实测零命中；
**也没有 §11.2⑤ 那个整词替换**（`DC/DC power units` 实测 0 命中）。
**这不是「没找到」，是查过、结果为零。**

`verified: doc-only`
