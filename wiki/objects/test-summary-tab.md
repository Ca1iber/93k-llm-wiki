---
type: object
title: Test summary tab
layer: gui
stage: results
tags: [test-summary-tab, results, data-navigation, table-filter, grouping, evaluation, gui]
related: [data-navigation-views, table-filter, raw-data-views, integrated-result-tool, testflow-tool, analysis-views]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Test summary tab

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Test summary tab 是「数据导航视图」里的一个 tab，一行 = 一个 test 的汇总。** 原文：

> 「The test summary tab of the **data navigation view** for a **data store** shows the
> **consolidated results** for the tests in the data store, displaying **basic statistical
> evaluations for all executions of a particular test**.」

**把这句话拆开，一行的粒度就定死了：**

| 原文 | 含义 |
|---|---|
| `of the data navigation view` | **它不是独立窗口，是导航视图里的一个 tab** |
| `for a data store` | 它面向的是 **data store**（本文档只说这个，**不区分文件还是流**） |
| `the consolidated results for the tests` | 合并后的结果 |
| `basic statistical evaluations for **all executions of a particular test**` | **一行 = 某一个 test 的全部执行** ——**不是一次执行一行** |

> **最后一行最容易读错。** 一行不是一个 DUT、不是一次 run，**是一个 test 的所有执行合起来**。
> **这也是 `Device#` / `Pass#` / `Min` / `Max` / `Mean` 这些列存在的原因**——
> 它们都是「对这一行里合起来的那些执行」做统计。

### 三个组成部分

原文明确说这个 tab 由**三块**构成（`All three elements are described below.`），
**它自己的三个 `##` 节就是这三块**：

| 块 | 原文的叫法 | 本文档的节 |
|---|---|---|
| **表** | `the columns describing each test` | `## Table` |
| **两侧的标记** | `configurable fail and alert marks in the left and right margins` | `## Marks in the annotation and overview rulers` |
| **快捷菜单** | `it has a shortcut menu` | `## Shortcut menu` |

### 表的 27 列

**列分七组**，分开看比连排看有用：

| 组 | 列 |
|---|---|
| **标识**（6） | `Test Suite` / `Test Method` / `Test` / `Test#` / `Type` / `Pattern Name` |
| **位置**（3） | `Wafer` / `Site` / `Pin` |
| **限值与单位**（3） | `Lower` / `Upper` / `Unit` |
| **统计量**（4） | `Min` / `Max` / `Mean` / `Sdev` |
| **能力指数**（4） | `Cp` / `Cpk` / `Cpl` / `Cpu` |
| **计数**（5） | `Device#` / `Pass#` / `Pass%` / `Fail#` / `Fail%` |
| **时间**（2） | `Time` / `TS Time` |

**三条要单独记的：**

1. **`Test` 列的值来自别处**：原文说它是 `The test name as specified by the
   TESTSET.testname()` 函数——**列的内容不是本 tab 定的，是那个函数的返回值**。
2. **`Type` 只有四种取值**：`parametric, functional, shmoo, or unknown`。
   **注意第四种是 `unknown`**——原文为「认不出来」留了一档。
3. **`Pass%` 和 `Fail%` 不只是数字，还带色条**：
   `Pass%` 用**绿色横条**画在本格里，`Fail%` 用**红色横条**。
   原文给了两个例子：三分之一通过 → 格子左边三分之一是绿的；三分之二失败 → 左边三分之二是红的。

**时间列带一句免责**：`Time` 和 `TS Time` 两条**各自**都跟着同一句
`(Due to algorithmic overhead, this number may not be the exact actual execution time.)`——
**即：这两个数不是精确的执行时间**，原文自己说了原因（`algorithmic overhead`）。
**同一句在本篇里出现了两遍**（一次给 `Time`、一次给 `TS Time`）。

**列的显示与顺序是可配的**：原文说 `Which columns are displayed and the order in which they are
displayed can be set in the preferences`（指向 `Test Summary preference settings`）。
**另有一条例外**：**如果这个 tab 属于 correlation view，会多出一些列**
（原文指向 `Correlation data store structure`）——**多出哪些列，本页没读那篇，不知道。**

### 左右两条标尺：名字、图标、颜色

原文把左右两侧叫 **ruler（标尺）**，并给出了对应关系——
**这一对术语要记牢，因为正文里两个词混着用（`margins` 和 `rulers`）：**

| 侧 | 原文的名字 | 原文给的等价说法 | 装什么 |
|---|---|---|---|
| **左** | **annotation ruler** | `(the left margin)` | **图标** |
| **右** | **overview ruler** | `(right margin)` | **小块色矩形** |

**左侧四个图标**（每行可能不止一个，**多个时图标互相重叠**；**鼠标悬停出 tooltip**，含失败数与告警数）：

| 图标 | 含义（原文） |
|---|---|
| fail 图标 | `The test summarized in this row failed for at least one device.` |
| alert 图标 | `This row contains a cell with an alert.` |
| exclusion 图标 | `Data records for this test have been excluded in the raw data view.` |
| **shmoo hole 图标** | `The test summarized in this row contains a shmoo hole.` |

**右侧的色矩形**：**每个「有失败器件的行」和「有 alert 的行」各一个小矩形**；
**点矩形 → 选中表里对应的行**；**悬停 → 出 tooltip 讲 alert 的原因**；
**悬停在视图右上角那个小色块上 → 出总数**（失败行数、含被排除数据集的行数、有 alert 的行数）。

**默认配色（原文逐条给出）：**

| 标记 | 默认颜色 |
|---|---|
| fails | **红** `red` |
| exclusions | **蓝** `blue` |
| alerts | **黄** `yellow` |
| shmoo holes | **青** `cyan` |

**四类默认全开**（`all kinds are enabled`），
**颜色可在 Annotations preference page 里改，也可逐类关掉。**

> ⚠️ **这里有一处原文自己的不齐**（见 `## 出处` 瑕疵②）：
> 左侧那一节的开头说图标 `indicating rows with **fails, exclusions and alerts**`（**三样**），
> **紧接着的清单却列了四项**（多一个 shmoo hole）。
> **本页照实并列两处，不替原文补齐。**

### 快捷菜单：哪条命令在什么条件下才在

**这是本页最实用的一张表。原文把条件写得很死，而且条件句是被拆到每条命令下面单独写的：**

| 命令 | 条件（原文） |
|---|---|
| `Refresh` | **只在 tab 里显示 system data log stream 时可用** |
| `Pause` | 同上 |
| `Resume` | 同上 |
| `Clear` | 同上 |
| `Save and Clear` | 同上 |
| `Auto Update Chart` | 同上 |
| `Open Definition` | **要求 testflow 已载入 SmarTest**（`This requires the testflow to be loaded in SmarTest.`） |
| `Open Test Limit` | **同样要求 testflow 已载入** |
| `Show In` / `Exclude` / `Filter` / `Width` / `Group By` / `Yield Calculator` / `Cpk Limit Calculator` / `Copy` / `Alerts` / `Preferences` | **原文没有给条件** |

> **前六条的条件句原文写得一模一样**（`This command is available only when the system data log
> stream is displayed in the tab.`），**在原文里重复了六遍**。
> **换句话说：这六条命令在「加载的是普通数据日志文件」时根本不在菜单里**
> （推断，依据就是这句条件）。

**两处最容易混的命令对：**

**① `Refresh` ≠ `Resume`。** 原文的对照写得很清楚：

> 「**Refresh**: Updates the system data log stream display with the latest logged data **when it is
> paused**, but **does not turn on automatic updating again, like Resume does**.」

| 命令 | 它做什么 | 它不做什么 |
|---|---|---|
| `Refresh` | **在暂停状态下**把显示刷到最新 | **不重新打开自动更新** |
| `Resume` | **重启自动更新** | — |

**② `Clear` 和 `Save and Clear` 的差别在「要不要先存」：**

| 命令 | 原文 |
|---|---|
| `Clear` | `Removes all current entries from the system data log stream display in the Integrated Result Tool and clears the system event stream.` |
| `Save and Clear` | **先弹一个标准的 Save 对话框，把当前 system event stream 存成 EDL 文件**，**存完再**移除并清空 |

> **注意命令名与动作的错位**：`Save and Clear` 的原文语序是 **save → 然后 clear**，
> **而且 clear 这件事和 `Clear` 干的是同一件**（推断）。

**`Open Test Limit` 有两条分支，按「testflow 用不用 test tables」分：**

| 情形 | 结果 |
|---|---|
| testflow **用** test tables | **打开 test table，并把对应行高亮** |
| testflow **不用** test tables | **打开 `Tests page`，并把该行高亮** |

**两条 `Open *` 命令都会「打开 Testflow Tool」**——
**它们是本 tab 通往 testflow 的出口**（推断，依据是两句都以 `Opens the Testflow Tool and displays…` 开头）。

### `Show In` 子菜单：10 项

原文列了 **10 项**，**注意其中混着一张「表」**：

| # | 原文 | 是图还是表 |
|---|---|---|
| 1 | `Trend chart` | 图 |
| 2 | `Histogram` | 图 |
| 3 | `Probability chart` | 图 |
| 4 | `Box chart` | 图 |
| 5 | `Scatter chart` | 图 |
| 6 | `FFC Pareto chart` | 图 |
| 7 | **`Raw data view`** | **表**——原文这句自己写的是 `result graphs **and tables**` |
| 8 | `Shmoo plot` | 图 |
| 9 | `Scan view` | 图 |
| 10 | `Parametric wafer map` | 图 |

**`Show In` 的作用是「把选中的行显示到这些图/表里去」。** 原文这句有一个限定：
它说的是 `display the **selected rows**`——**所以选了什么，决定了能出什么图**
（**具体每种图要选几行，本页一个字都没有**：那在每一篇视图自己的文档里，本页没读）。

### 一个必须分清的点：两种「自动更新」

原文里 **`Auto Update Chart`** 这条命令带着一句极易被忽略的划界：

> 「It **does not affect** the automatic update of any chart views **when different rows are
> selected** in the test summary tab.」

**两个机制是不同的东西：**

| 现象 | 由谁控制 |
|---|---|
| **选中的行变了，图跟着变** | **不是 `Auto Update Chart`** ——原文明说它 `does not affect` 这个 |
| **数据流里来了新条目，图自动跟着变** | **`Auto Update Chart`**，**默认是关的**（`By default, these dynamic updates are deactivated.`） |

**并且原文给了一条性能警告**：
`when the data log stream contains a large number of entries, performance may suffer.`

## 典型用法

原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`，
**但三个 `##` 节里散着的操作足够拼出下面这些。以下每条都是原文的直接意思。**

**1. 排序：点列标题，点三次一个循环**（原文写得很完整）

| 第几次点 | 结果 | 标志 |
|---|---|---|
| 1 | **升序**（`smaller values come first`） | 向上三角 `136425.png` |
| 2 | **降序** | 倒三角 `136426.png` |
| 3 | **取消排序**，回到 `the order in which they occur in the data store` | — |

**2. 选中一行**：`Clicking any field in a row selects the entire row`
——**原文给了它的用途：`for example, for copying it`**（配合下面的 `Copy`）。

**3. 过滤，有两条路**

| 路 | 怎么做 |
|---|---|
| **表内过滤行** | 表**最上面一行（青色背景）就是 table filter**，在里面输条件 |
| **`Filter` → `Show Similar`** | **限制成「与选中行同 test suite + 同 test name」的行** |

> **原文明说 `Show Similar` 是前者的快捷方式**：
> `this command is a shortcut for entering the test suite and test names in the table filter row`。
> **要恢复全部行**：`click at the very left of the table filter row (which clears all filters)`。

**4. 排除数据（`Exclude` 子菜单）**

| 选项 | 效果（原文） |
|---|---|
| `Pass` | `Excludes all test summaries that contain only passed tests.` |
| `Fail` | `Excludes all test summaries that contain at least one failed test.` |
| `None` | **不排除任何东西；如果当前有排除在生效，就结束它** |

> **这条命令有一点必须记住**：原文说
> `Records that you exclude in this tab are **also excluded in other tabs**.`
> ——**在这个 tab 里排除，别的 tab 也跟着排除。它不是本 tab 的局部显示开关。**

**5. 分组（`Group By`）**

| 项 | 原文 |
|---|---|
| 三个可选类别 | `Wafer` / `Site` / `Pin` |
| 分组后一行的含义 | **每个 test 的每个 wafer/site/pin 一行**（`one row per wafer, site, or pin for each test`），**不是每个 test 一行** |
| 顺带效果 | **会显示出对应的列**（`Wafer` / `Site` / `Pin`） |
| **能不能多级** | **能**：`You can group by multiple categories`，**此时一行 = 一个组合**（原文例：`test, wafer, and site` 的每种组合） |
| **怎么取消** | **再选一次同类命令**（`choosing the corresponding command from the submenu again removes the grouping`） |

**6. `Copy` 与 `Width`**

- `Copy`：把选中的行**以「tab 分隔的文本」**放进剪贴板（`as tab-separated text`）。
- `Width` → `Autofit`：**把每列调到刚好放得下全部内容**。

**7. 两个计算器（两条子主题就是它们）**

| 命令 | 打开什么 |
|---|---|
| `Yield Calculator` | `Yield Calculator`——**从 limits 算 yield** |
| `Cpk Limit Calculator` | `Cpk and limit calculator`——**从 limits 算 Cpk，或反过来** |

> ⚠️ **注意命令名与它打开的东西名字不同**：命令叫 `Cpk Limit Calculator`，
> 打开的是 `Cpk and limit calculator`（且子主题文件叫 `Cpk___Limit_Calculator`）。
> **原文没有解释这两个名字的关系**（见 `## 出处` 瑕疵⑥）。

**8. 出图**：选中行 → `Show In` → 选上表 10 项之一。

**9. 开数据流时的四条操作**（**前提：tab 里显示的是 system data log stream**）：
`Pause` 停自动更新 → `Refresh` 手动刷一次 → `Resume` 恢复自动更新 → `Save and Clear` 存成 EDL 再清空。

## 和谁有关

- [[data-navigation-views]] — **上位**：原文第一句就写它是 `The test summary tab of the data
  navigation view`。**本 tab 是那种视图里的一个 tab，不是独立工具。**
- [[table-filter]] — **表的第一行就是它**：原文 `The topmost row in the table (with a cyan
  background) is the table filter`，并直接指向了那一篇。**本页的 `## Table` 一节点名要它。**
- [[raw-data-views]] — **两个方向的关系都有**：
  ① `Show In` 里有一项就是它（**它是一张表，混在九个图中间**）；
  ② 左侧的 exclusion 图标说的是
  `Data records for this test have been excluded **in the raw data view**`——
  **排除动作发生在那一侧，本 tab 只是把结果标出来**（推断，依据是这句的定位短语）。
- [[integrated-result-tool]] — **宿主**：原文两条命令的描述里出现
  `the system data log stream display **in the Integrated Result Tool**`，
  **说明这个 tab 跑在它里面**。**主文档没有一处直接写「本 tab 属于它」**（推断，依据就是这两句）。
- [[testflow-tool]] — **两条命令的出口，且带硬前提**：
  `Open Definition` 和 `Open Test Limit` 都 `Opens the Testflow Tool`，
  **且都 `requires the testflow to be loaded in SmarTest`**。
- [[analysis-views]] — **同类页**：那一页讲的是「选中行 → 出分析视图」的规则，
  **而「选中行」这个动作发生在本 tab 里**（推断：两页是同一条链的两端，
  **依据是 [[data-navigation-views]] / `Show In` 这些共同的名字**；**原文没有直接写这层关系**）。
- [[tmlimits]] — `Open Test Limit` 的两条分支里，**「用 test tables」那一支走的就是它**
  （原文 `If the testflow uses test tables, the test table is opened and the appropriate row is
  highlighted`）。**原文用的是小写 `test tables`，本页把它接到 [[tmlimits]] 是推断。**
- [[testset-testname]] — `Test` 列的值来自 `TESTSET.testname()` 函数。
- [[smartest-7.2.0]] / [[smartest-7.2.1]] / [[smartest-7.2.2]] / [[smartest-7.2.3]] —
  本页版本段前九条落在它们上面。
- `Yield Calculator` / `Cpk & Limit Calculator`（**均未建、未读**）— **本 tab 的两条子主题**，
  分别对应 `Yield Calculator` 与 `Cpk Limit Calculator` 两条快捷菜单命令。**本页对它们零覆盖。**
- `Trend chart` / `Histogram` / `Probability chart` / `Box chart` / `Scatter chart` /
  `FFC Pareto chart` / `Shmoo plot` / `Scan view` / `Parametric wafer map`（**均未建、未读**）—
  `Show In` 里的九个图。**本页只有它们的名字和链接，没有任何内容**——
  **每种图要选几行、画什么，本页一个字都没有。**
- `Annotations preference page` / `Alerts preference page` / `Test Summary preference page` /
  `Test Correlation preference settings`（**均未建、未读**）— 四处偏好设置。
  **本页只讲了「默认值是什么」，没讲「怎么改」。**
- `Excluding data from evaluation` / `Highlighting specific data` /
  `Correlation data store structure`（**均未建、未读**）— 原文点名的三篇延伸阅读。

## 版本

`## Functional changes` 段有，**十条**：

> - Introduced in **SmarTest 7.2.0**
> - **SmarTest 7.2.1**: Open Test Limit now selects the appropriate row.
> - **SmarTest 7.2.1**: Renamed some columns.
> - **SmarTest 7.2.1**: Test summaries with excluded rows or shmoo holes are now indicated.
> - **SmarTest 7.2.2**: Added menu command for yield calculator.
> - **SmarTest 7.2.2**: Added Pattern Name column.
> - **SmarTest 7.2.2**: Added Save and Clear shortcut menu command.
> - **SmarTest 7.2.2**: The Clear shortcut menu command now also clears system event stream.
> - **SmarTest 7.2.3**: Added option to enable or disable dynamic updates for system data log stream charts.
> - **SmarTest 7.50**: Added alarm count in tooltip.

**几条能和正文对上的**（推断，依据是正文里对应内容的措辞）：

| 版本条目 | 正文里的对应处 |
|---|---|
| `Added Pattern Name column` | 27 列里的 `Pattern Name`（**说明这一列是 7.2.2 才有的**） |
| `Added Save and Clear shortcut menu command` | 快捷菜单里的 `Save and Clear` |
| `The Clear shortcut menu command now also clears system event stream` | `Clear` 的原文里那句 `and clears the system event stream` |
| `Added option to enable or disable dynamic updates for system data log stream charts` | `Auto Update Chart` 命令；**这也解释了它为什么默认是关的**（推断） |
| `Test summaries with excluded rows or shmoo holes are now indicated` | 左侧那四个图标（**7.2.1 起才有**） |
| `Added alarm count in tooltip` | 左侧图标悬停 `displays a tooltip with additional information such as fail and alarm counts` |
| `Renamed some columns` | **改了哪些列、改成什么，原文没写** |

> **注意最后一条的写法** `SmarTest 7.50`——**同一份文档里其他九条都写三段式**
> （`7.2.0` / `7.2.1` / `7.2.2` / `7.2.3`），**只有这一条写 `7.50`**。
> **本页不判它是不是 `7.5.0` 的排印问题**，照实记（见 `## 出处` 瑕疵⑤）。
> **另需注意：本 wiki 的允许清单里 `smartest-7.50` 与 `smartest-7.5.0` 是两个名字**，
> **所以本页不替它二选一，也不给这一条加链接。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.md`

**这就是本页正文的全部依据。整篇 189 行——本批八页里最长的一篇，正文、三个 `##` 节、
`## Example`、`## Related information`、`## Functional changes` 俱全。**
**所以本页的 `## 是什么` 比同批其他页厚得多**：这是原文厚，不是本页加料。

**本页没做的**：

- **两条子主题一篇都没读**：`Yield Calculator`（`…03.02.01.01`）、
  `Cpk & Limit Calculator`（`…03.02.01.02`）。
  **所以两个计算器怎么算、输入输出是什么，本页只有原文那一句「从 limits 算 yield / 算 Cpk」。**
- **`Show In` 那九篇图文档一篇没读**（另加一张 `Raw data view`）：
  `Trend_chart_view`、`Histogram_view`、`Probability_chart_view`、`Box_chart_view`、
  `Scatter_chart_view`、`FFC_Pareto_chart_view`、`Raw_data_views`、`Shmoo_view`、`Scan_view`、
  `Parametric_wafer_map_view`。
  **本页只有它们的名字。** **「选中几行才能出哪种图」这条规则本页完全没有**。
- **原文点名要读的延伸篇目一篇没读**：`Table filter`、`Excluding data from evaluation`、
  `Highlighting specific data`、`Correlation data store structure`、
  `TESTSET.testname()`（`…02.07.04.01.244.23_TESTSET__.testname.md`）。
  **其中 `Table filter` 尤其要紧**——**表的第一行就是它，而它的写法规则本页一个字都没有。**
- **四处偏好设置页一篇没读**：`Annotations preference page`（原文出现两次）、
  `Alerts preference page`、`Test Summary preference page`、`Test Correlation preference settings`。
  **所以「默认配色是什么」本页有，「怎么改」本页没有。**
- **一张图没看。** 原文里有 **9 处图**：`## Example` 的 `136411.png`（Test Summary）、
  排序三角 `136425.png` / `136426.png`、四个图标 `136405.png` / `136406.png` /
  `140971.png` / `141950.png`。
  **本页没有任何来自图的结论**——**四个图标长什么样、色条怎么画，本页全不知道，
  只知道它们的含义文字。**
- **没有查 `data store` 的定义**，**没有查 `shmoo hole` 是什么**
  （它只出现在图标含义和版本条目里），**没有查 `EDL` 是什么**。
- **没有把本页与 [[analysis-views]] 的视图清单做过对照**——
  **那一页列了哪些视图、与本页 `Show In` 的 10 项是否一致，本页没有核**
  （§：本页只写自己读了的那一篇里有的）。

> ⚠️ **语料瑕疵，照实记下、一处没替它改**（§11.2）：
>
> **① 主语与动词数不一致**（逐字引，本篇出现**两处**）：
> `Clicking a column title **sort** the table by this column in ascending order` ——**应为 `sorts`**；
> `**Show In**: The commands in this submenu **lets** you display the selected rows` ——
> **复数 `commands` 配了单数 `lets`**。
> 另有一处同类：`**Group By**: This commands in this submenu **lets** you group the displayed
> summaries by wafer, site, or pin.`——**`This commands` 应为 `The commands` 或 `This command`**。
>
> **② 一处「说三样、列四项」**（逐字引两处对照）：
> 小节开头写 `The annotation ruler (the left margin) contains icons indicating rows with
> **fails, exclusions and alerts**:`（**三样**，
> 另见本篇第二段 `configurable fail and alert marks`，**那样只有两样**），
> 紧接着的清单却是**四项**：fail、alert、exclusion、**shmoo hole**
> （`The test summarized in this row contains a shmoo hole.`）。
> **本页把四项都照列，并在「是什么」里把这一处不齐标了出来**——
> **没有替原文把开头那句补成四项，也没有删掉 shmoo hole 那一项。**
>
> **③ 主谓不一致（否定句）**（逐字引）：
> `**None**: No test are excluded.`——**`No test are` 应为 `No tests are`**。
>
> **④ 图标 alt 文本里的拼写错**（逐字引）：
> `![Data log summary view_**Exclusiont** icon](<../../../../raw/140971.png>)`
> ——**`Exclusiont` 应为 `Exclusion`**。
>
> **⑤ 版本号写法与全篇不一致**（逐字引）：
> `- SmarTest **7.50**: Added alarm count in tooltip.`
> ——**同一节另外九条都是三段式**（`7.2.0` / `7.2.1` / `7.2.2` / `7.2.3`），
> **只有这一条写 `7.50`**。**本页不判它是不是 `7.5.0` 的排印问题**，照实记。
>
> **⑥ 同一件东西三个名字**（逐字引三处）：
> 快捷菜单命令 `**Cpk Limit Calculator**`；
> 它的说明 `Opens the [Cpk and limit calculator](<…>)`；
> 子主题文件名 `02.08.04.13.03.02.01.02_**Cpk___Limit_Calculator**.md`。
> ——**`Cpk Limit Calculator` / `Cpk and limit calculator` / `Cpk & Limit Calculator`
> 三者指同一个东西**，原文没有说明。
> **本文档另有一处名字不齐**：`Test Summary preference settings`
> （`## Related information` 里）与 `Test Summary preference page`
> （`Preferences` 命令的说明里）——**指向同一个文件，叫法不同**。
>
> **⑦ `## Related information` 三个链接连排、无分隔**（逐字引全行）：
> `[Data navigation views](<02.08.04.13.03.02_Data_navigation_views.md>)[Test Summary preference settings](<02.08.04.13.03.05.21_Test_Summary_preference_settings.md>)[Test Correlation preference settings](<02.08.04.13.03.05.20_Test_Correlation_preference_settings.md>)`
> ——**三个链接首尾相接，中间没有空格、逗号或换行**。
> **本页没有替它加分隔符。**（这是本批里第二次遇到同一种排版缺失，见 [[timing-diagram-tool]]。）
>
> 链接指向方面：本页未发现指错——三条子主题与 `Show In` 的十条路径
> （`…13.03.04.01` ~ `.10`、`…13.03.03.01_Raw_data_views.md`）
> **编号连续且与条目名对应**（`Raw data view` 那一条指向 `Raw_data_views.md`，**文件名是复数、
> 链接文字是单数**，这一处不齐本页照记，但不影响指向）。

`verified: doc-only`

