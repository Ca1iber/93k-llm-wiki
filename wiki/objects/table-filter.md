---
type: object
title: Table filter
layer: gui
stage: results
tags: [table-filter, results, data-navigation, summary-tab, filter, gui]
related: [results, data-navigation-views, raw-data-views, test-summary-tab, wafer-summary-tab, hardware-bin-summary-tab, software-bin-summary-tab, device-summary-tab, smartest-7.2.0]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Table filter

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,313 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

In the fields of the table filter, you can enter:

- Plain text (for text columns).

Only those rows are displayed where the content in the filtered column contains the text you have entered.

- Regular expression (for text columns).

Only those rows are displayed where the content in the filtered column matches the regular expression. You can use Content Assist (Ctrl+Space) to insert common regular expression terms.

- Number (for number columns).

Only those rows are displayed where the content in the filtered column is exactly the number you entered.

- Range; two numbers separated by a ~ tilde (for number columns).

Only those rows are displayed where the content in the filtered column is greater than the first number you entered and less than the second number.

If you leave out one of the numbers, the range is open-ended. For example, entering ~2 displays all row with a value smaller than 2 in the column.

- Multiple numbers, separated by commas (for number columns).

Only those rows are displayed where the content in the filtered column is exactly any of the numbers you entered. (This is an "or" query.)

You can use both simple numbers and ranges. For example, 3~,3 finds all rows with values greater than 3 or equal to three. -1,-1~1,1 finds all numbers from -1 to 1, including -1 and 1.

<!-- 语法节 end -->

## 是什么

**Table filter 是表格最上面那一行，背景色是青色（`cyan`）。** 它出现在**三个地方**——
定义句一句话把作用域给全了，逐字：

> 「The table filter is the topmost row (with a cyan background) in every summary tab, raw data
> view, and stream data view.」

**三个地方是：每一个 `summary tab`、`raw data view`、`stream data view`。**
**它干的事**，同段下一句逐字：

> 「It lets you restrict the displayed record displayed in the table to those matching conditions
> you specify.」

**即：把表里显示的行，限制成「符合你给的条件」的那些。**
**⚠️ 这一句里 `displayed` 出现了两次（`the displayed record displayed`），原文如此，见 `## 出处` ①。**

### 怎么填：双击一格；条件是按**列**挂的

> 「Double-clicking a cell of the table filter lets you enter the desired condition for that column.
> (See below for the syntax.) It also displays a drop-down list at the right side of the cell from
> which you can choose recently entered conditions and, for some fields, predefined values.」

**三点：**

1. **双击某一列在 filter 行里那一格 → 给这一列填条件**（**所以「一个条件」=「一列」**）；
2. **那一格的右侧有一个下拉列表**；
3. **下拉里装着「最近填过的条件」，以及部分列才有的「预定义值」**——
   原文写的是 **`for some fields`**，**没说是哪些列**。

### 两个组合规则

| 你做的事 | 结果（**逐字**） |
|---|---|
| **在多个列里都填了条件** | `only records matching all of them are displayed`——**「全部满足」才显示，是 AND 不是 OR** |
| **点 filter 行最左边那一小格** | `removes all conditions; the table once again displays all rows`——**条件全清，表恢复显示所有行** |

**⚠️ 两句要连着读**：**条件之间是 AND**；**清空只有「最左边那一小格」这一个入口。**
**「怎么只清掉其中一列」本篇没写——语料未写**（见 `## 出处`）。

### 五种填法（`## Syntax` 一节）

**原文用一句领起**，逐字：`In the fields of the table filter, you can enter:`
**然后把五种形态列成五个列表项。** 归纳成表：

| 填什么（**逐字**） | 对哪些列（**原文的括注**） | 命中规则（**逐字**） |
|---|---|---|
| `Plain text` | `for text columns` | `the content in the filtered column contains the text you have entered`——**包含** |
| `Regular expression` | `for text columns` | `the content in the filtered column matches the regular expression`——**匹配** |
| `Number` | `for number columns` | `is exactly the number you entered`——**恰好等于** |
| `Range`（两数用 `~` 连接） | `for number columns` | `greater than the first number you entered and less than the second number`——**两端都是开区间** |
| `Multiple numbers`（逗号分隔） | `for number columns` | `is exactly any of the numbers you entered`——**多个数之间是 OR**（原文自己给了这个口径：`(This is an "or" query.)`） |

**正则那一项另带一个工具**，逐字：

> 「You can use Content Assist (Ctrl+Space) to insert common regular expression terms.」

**即：文本列填正则时，`Ctrl+Space` 能插入常用正则片段。**
**这一条只挂在正则那一项下面，别的项原文没给。**

### 一处最容易读错的地方：区间是**开**的

**「区间」那条的原文是 `greater than … and less than …`——两头都不含。**
**所以「从 -1 到 1、含两端」不是区间自己做到的。** 原文的例子逐字：

> 「You can use both simple numbers and ranges. For example, 3~,3 finds all rows with values
> greater than 3 or equal to three. -1,-1~1,1 finds all numbers from -1 to 1, including -1 and 1.」

**两个例子都得拆成几项读**：

| 例子 | 拆开 | 合起来 |
|---|---|---|
| `3~,3` | `3~`（大于 3）＋ `3`（等于 3） | **大于或等于 3** |
| `-1,-1~1,1` | `-1`（等于 -1）＋ `-1~1`（严格在 -1 与 1 之间）＋ `1`（等于 1） | **-1 到 1，含两端** |

**（推断）**依据就是同句里几项并列：**如果 `a~b` 本身含端点，第一个例子里的 `3`
和第二个例子里的 `-1` / `1` 就都是多余的。**原文没有明说「区间是开的、端点是另外两项凑出来的」——
**这是推断，不是原文的话。**

**开区间还可以省掉一端**，逐字：

> 「If you leave out one of the numbers, the range is open-ended. For example, entering ~2 displays
> all row with a value smaller than 2 in the column.」

**即 `~2` = 小于 2。**（**⚠️ 这句里 `all row` 原文如此，见 `## 出处` ②。**）
**（推断）反过来 `2~` 就是大于 2**——依据是上面 `3~,3` 那个例子里原文把 `3~` 读成 `greater than 3`；
**原文没有单给 `2~` 的例子。这是推断。**

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`。**
**它是「这一行怎么写条件」的说明，不是流程说明**——
下面这些是从正文与 `## Syntax` 两节里落出来的动作。

| 要做的 | 怎么做 | 依据（**原文**） |
|---|---|---|
| **给某一列加条件** | **双击那一列在 filter 行里的格子** | `Double-clicking a cell of the table filter lets you enter the desired condition for that column.` |
| **填以前填过的条件** | 双击后，从格子右侧的下拉列表里选 | `choose recently entered conditions` |
| **用预定义值** | 同上；**只有部分列有** | `for some fields, predefined values` |
| **只看文本里含某串的行** | 填纯文本 | `contains the text you have entered` |
| **按模式匹配文本** | 填正则；`Ctrl+Space` 插常用项 | `matches the regular expression` |
| **只看恰好等于某个数的行** | 填那个数 | `is exactly the number you entered` |
| **看某个数段** | 填 `a~b`（**开区间**）；省掉一端就是单边 | `greater than the first number … less than the second number` |
| **看若干散点值** | 逗号分隔多个数（**OR**） | `(This is an "or" query.)` |
| **同时限定多列** | 每列各填一个条件 | `only records matching all of them are displayed` |
| **把条件全清掉** | 点 filter 行最左边那一小格 | `removes all conditions` |

**原文自己给了两个可以直接抄的填法**：`3~,3`（大于 3 或等于 3）、
`-1,-1~1,1`（-1 到 1，含两端）。

**一条本篇没答的**：**怎么只清掉某一列的条件**——
**原文只给了「最左边那一小格 = 全清」这一个动作，没有给逐列清空的做法。语料未写。**

## 和谁有关

- [[results]] — 本页 `stage: results` 的理由：**它作用于结果数据的那几张表**。
  **⚠️ 但本篇正文没有点名 `Integrated Result Tool`，也没有点名任何一篇结果工具文档**——
  这条归属是本 wiki 的既有划分，**不是本篇写的**（见 `## 出处`）。
- [[data-navigation-views]] — **原文 `## Related information` 三个链接里的第一个**，
  目标是 `02.08.04.13.03.02_Data_navigation_views.md`——
  **（推断）从编号看本页（`…13.03.02.06`）与它同属 `13.03.02` 这一层**；
  **依据只是路径编号相邻，原文没有说两者的关系。这是推断。**
- [[raw-data-views]] — **（推断）本页作用域里的 `raw data view`**。
  本篇写的是单数 `raw data view`，而 wiki 页叫 [[raw-data-views]]
  （来源 `02.08.04.13.03.03.01_Raw_data_views.md`，**编号在另一个子层 `13.03.03`**）——
  **单复数与编号都不同，原文没有把两者对上。这是推断，那一页的 raw 本页没用。**
- [[test-summary-tab]] / [[wafer-summary-tab]] / [[hardware-bin-summary-tab]] /
  [[software-bin-summary-tab]] / [[device-summary-tab]] —
  **（推断）本页说的 `every summary tab` 就是这一族**。
  依据：原文用的是**复数**（`every summary tab`），**说明「summary tab」是一族**；
  **原文没有点名这一族里任何一个具体的 tab。这是推断，不代表它们结构与本页相同。**
- [[smartest-7.2.0]] — 版本页：本页的 `Introduced in SmarTest 7.2.0` 落在它上面（**见 `## 版本`**）。
- `Filtering test result data`（**未建、不在 allowlist，故用反引号**）——
  **原文 `## Related information` 的三个链接之一**，
  目标是 `02.08.04.13.02.03.02_Filtering_test_result_data.md`。**本页没读那一篇**——
  **所以「结果数据整体是怎么被筛的」本页没有，本页只有「这一个 filter 行怎么填」。**
- `Detail data views`（**未建**）— 同清单的第三个链接，
  目标 `02.08.04.13.03.03_Detail_data_views.md`。**本页没读。**
- `stream data view` / `summary tab` / `raw data view`（**三个，均未建**）——
  **本页作用域里的三个场所**，原文只在定义句里点了它们的名，
  **它们各自长什么样子，本页一个字都没有。**

## 版本

**本文档有 `## Functional changes` 段，一条**，逐字：

- **Introduced in SmarTest 7.2.0**

**⚠️ 这一条不是 §11.2 ② 那个哨兵值。** 哨兵写的是 `Introduced before SmarTest 6.3.2`
（关键词是 **`before`**），而这一条是 **`in`**——
**所以它确实就是「SmarTest 7.2.0 引入」，不是「早于语料覆盖范围」。** 详见 [[smartest-7.2.0]]。

**7.2.0 之后到 wiki 目标版本 SmarTest 7.10.3 之间有没有再改，本篇没有依据。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.md`
（TDC 主题号 `136500`；本地 raw md：**2,584 字节**、**50 行**——
**字节是磁盘上的字节数，行数是换行符个数**）

**本页没做的：**

- **一张图都没看。** 本篇**没有图**（查过：正文里一个 `![` 都没有）——
  所以上面「背景色 `cyan`」**只有文字依据，没有视觉依据**。
- **三个 `Related information` 链接一篇没读**：`Filtering test result data`、
  `Data navigation views`、`Detail data views`。
  **本页与它们的关系只有链接名与路径编号，没有从对面回校过。**
- **本页正文只用本篇的材料。** 本批别的页的 raw 不作为本页的依据——
  所以「filter 行在别的 tab 里怎么用」这一层，本页不写。
- **`layer: gui` / `stage: results` 不是本篇写的**——本篇没有 `## Application` 这类自我定位段，
  这个归属是本 wiki 的既有划分。**（推断）`gui` 与「一个表格里的输入行」相符，
  但这是本页的观察，不是原文说的。**
- **五种填法的「对哪些列有效」直接照抄了原文的括注**（`for text columns` / `for number columns`），
  **原文没有说列的类型由谁决定，也没有说文本列就不能填数字。**
- **`Ctrl+Space` 只有这一个出处**（正则那一项）——**别的项能不能用 Content Assist，本篇没写。**
- **原文没有 `## Procedure`、没有 `## Before you begin`**，
  所以 `## 典型用法` 那一张表**全部是从正文与 `## Syntax` 里落出来的**，不是原文的步骤清单。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 一句里 `displayed` 写了两遍。** 逐字：
> `It lets you restrict the displayed record displayed in the table to those matching conditions you specify.`
> ——`the displayed record displayed`。**（推断）应为 `the records displayed`**；
> **依据只是这一句自己的语法，原文没写对的是什么。本页引文照原样。**
>
> **② `all row` 少一个 `s`。** 逐字（开区间那一段的例子里）：
> `For example, entering ~2 displays all row with a value smaller than 2 in the column.`
> ——`all row`。**本页照原样引。**
>
> **③ 同一个数字，一句里一处写阿拉伯数字、一处写英文单词。** 逐字：
> `3~,3 finds all rows with values greater than 3 or equal to three.`
> ——前半是 `3`，后半是 `three`，**说的是同一个数。本页照实并列，不替它统一。**
>
> **④ `## Related information` 三个链接首尾相接，中间没有任何分隔符、没有列表符。** 逐字：
> `[Filtering test result data](<02.08.04.13.02.03.02_Filtering_test_result_data.md>)[Data navigation views](<02.08.04.13.03.02_Data_navigation_views.md>)[Detail data views](<02.08.04.13.03.03_Detail_data_views.md>)`
> ——**三个 markdown 链接连成一整行。**
> **（与 [[software-bin-summary-tab]] 那一页记的同类毛病同形；那一条本页引自那一页 wiki 页，不是本篇 raw。）**
>
> **⑤ 本篇没有 §11.2 ① 那种编码损坏**（查过：正文里汉字 0 个）。

`verified: doc-only`
