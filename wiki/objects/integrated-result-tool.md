---
type: object
title: Integrated Result Tool
layer: gui
stage: results
tags: [integrated-result-tool, results, data-log, evaluation, gui]
related: [analysis-views, data-navigation-views, results, test-summary-tab, raw-data-views]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13_Integrated_Result_Tool.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Integrated Result Tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **11,083 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13_Integrated_Result_Tool.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.02.03_Merging_data_logs.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.02.04_Correlating_data_logs.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.02.06_Exporting_data_logs.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.01_Sorting_tables.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.03_Highlighting_specific_data.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.05_Separating_summary_results_by_wafer__site__or_pin.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.02_Excluding_data_from_evaluation.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.04_Examining_the_underlying_data_of_an_analysis_view.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.05_Software_bin_summary_tab.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.01_Alerts_preference_settings.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.06_CSV_Export_command_line_tool.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Using the Integrated Result Tool › Managing data logs › Merging data logs）

Source data log 1:

```
Test name   Device ID   Value   P/F
A           P1.1        0.1     P
B           P1.1        0.2     F
C           P1.1        0.3     F
D           P1.2        0.4     P
```

Source data log 2:

```
Test name   Device ID   Value
A           P1.1        0.5     F
B           P1.1        0.6     P
C           P1.1        0.7     F
D           P1.3        0.8     F
```

Merged data log with Do not overwrite the current result with new one option:

```
Test name   Device ID   Value   P/F
A           P1.1        0.1     P
B           P1.1        0.2     F
C           P1.1        0.3     F
D           P1.2        0.4     P
D           P1.3        0.8     F
```

Merged data log with Overwrite the current result unconditionally option:

```
Test name   Device ID   Value   P/F
A           P1.1        0.5     F
B           P1.1        0.6     P
C           P1.1        0.7     F
D           P1.2        0.4     P
D           P1.3        0.8     F
```

Merged data log with Overwrite only when the new result is Pass option:

```
Test name   Device ID   Value   P/F
A           P1.1        0.1     P
B           P1.1        0.6     P
C           P1.1        0.3     F
D           P1.2        0.4     P
D           P1.3        0.8     F
```

Merged data log with Keep both option:

```
Test name   Device ID   Value   P/F
A           P1.1        0.1     P
B           P1.1        0.2     F
C           P1.1        0.3     F
D           P1.2        0.4     P
A           P1.1        0.5     F
B           P1.1        0.6     P
C           P1.1        0.7     F
D           P1.3        0.8     F
```

### Example（取自子主题 Using the Integrated Result Tool › Managing data logs › Correlating data logs）

This sample report from the console describes the correlation of two data logs:

```
Test Summary Correlation Information:
Data log [A] summary information
    TS=myTestSuite,TM=IDD,T=IDD1,TN=343500
    TS=myOtherTS,TM=Die_Info,T=Die_X,TN=343600
Data log [B] summary information
  + TS=StdTS,TM=IO_v3,T=TPIO,TN=335700
  - TS=myOtherTS,TM=Die_Info,T=Die_X,TN=343600

HW Bin Summary Correlation Information:
Data log [A] summary information
    HB=1
    HB=2
Data log [B] summary information
    all data match 'A'

SW Bin Summary Correlation Information:
Data log [A] summary information
    HB=1,SB=7
    HB=1,SB=1078
    HB=1,SB=1079
    HB=2,SB=221
    HB=2,SB=1002
Data log [B] summary information
  - HB=2,SB=221
```

How to read this report:

- The base data log (data log [A]) contains two test suites, named "myTestSuite" and "myOtherTS". The first of these test suites uses the test method "IDD" and performs a test named "IDD1" that has the number 343500.

Data log [B], the first correlated data log (and the only one in this case) contains an additional test suite, named "StdTS" but does not contain the "myOtherTS" test method. (Any test methods from data log A that are not mentioned in the summary of data log B re also present in data log B.

- Data log A contains two hardware bins, numbered 1 and 2.

Data log B contains exactly the same bins, not more and not fewer.

- Data log A contains five software bins. The first one is numbered 7 and is connected to hardware bin 1.

Data log B contains all software bins from data log, except bin 221.

### Example（取自子主题 Using the Integrated Result Tool › Managing data logs › Exporting data logs）

If you export CSV file from the data log mylog.stdf and specify in the Export Data Log to CSV dialog that you want to export the test summary and the hardware bin summary, two files are created:

- mylog.stdf.hbin.csv
- mylog.stdf.tsum.csv

The following screen shot shows an example of correctly exported raw data (when the All Raw Data option is selected before exporting data log).

  !`Data Log Explorer view_Export RAW Data Example`（raw: `../../../../agent-html/353295.jpg`）

### Examples（取自子主题 Using the Integrated Result Tool › Working with result data tables › Sorting tables）

### Sorting by one column

Clicking the title of the Max column twice sorts the table in descending order by that column:

 !`Data log summary view_Sorting example`（raw: `../../../../agent-html/137064.png`）

### Sorting by multiple columns

To sort a table by the Device number column and sort all rows with the same device number by the Time column (both in ascending order):

- Click the title of the Device number column, so that it shows an upward-pointing triangle.
- Click the title of the Time column, so that it, too, shows an upward-pointing triangle.
 !`Data log summary view_Sorting example, multiple columns`（raw: `../../../../agent-html/147881.png`）

### Example（取自子主题 Using the Integrated Result Tool › Working with result data tables › Highlighting specific data）

If the display of fails in the left and right margins is switched on, the display of alerts is switched off, and this condition is defined:

 !`Preferences window_Alerts, sample condition`（raw: `../../../../agent-html/136455.png`）

Then a raw data view might look like this:

 !`Raw data view_Sample view`（raw: `../../../../agent-html/136456.png`）

### Example（取自子主题 Using the Integrated Result Tool › Working with result data tables › Separating summary results by wafer  site  or pin）

In the following image of a test summary tab grouped by wafer, the two highlighted rows display results from the same test but for different wafers (1 and 3). In an ungrouped tab, these results would be displayed as a single row.

 !`Data log summary view_Grouping example`（raw: `../../../../agent-html/137405.png`）

### Example（取自子主题 Using the Integrated Result Tool › Analyzing test results › Excluding data from evaluation）

In the example below, all but one row in the raw data view for the selected row in the test summary view have been deselected.

The Integrated Result Tool behaves as if these rows were not present. For example, the Device# column shows just one device (instead of three).

 !`Data log summary view|Raw data view_Sample deselected data`（raw: `../../../../agent-html/137005.png`）

### Example（取自子主题 Using the Integrated Result Tool › Analyzing test results › Examining the underlying data of an analysis view）

This image shows part of the underlying data of a trend graph.

 !`Trend Chart view_Sample statistics`（raw: `../../../../agent-html/137406.png`）

### Example（取自子主题 Integrated Result Tool reference › Data navigation views › Software bin summary tab）

Depending on your preference settings, the bin summary could look like this:

 !`Data log summary view_SW Bin Summary`（raw: `../../../../agent-html/136421.png`）

### Syntax（取自子主题 Integrated Result Tool reference › Data navigation views › Table filter）

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

### Example（取自子主题 Integrated Result Tool reference › Preference settings for the Integrated Result Tool › Alerts preference settings）

Check Enable Condition in the Condition 1 section and specify this condition:

- First drop-down list: Min
- Second drop-down list: <
- Text field: 2.4
- Color: !`Preferences window_Alerts_color patch`（raw: `../../../../agent-html/136331.png`）

All rows in the summary view will be highlighted in orange that have a value below 2.4 in the Min column.

### Syntax（取自子主题 Integrated Result Tool reference › CSV Export command line tool）

```
CsvExport -I <input_file>[-O <output_file>] -T <report>[-F <format>][-G <grouping>][-C columns][-h]
```

All commands options have an abbreviated and a descriptive form. (For example, `-h` or `--help`.) This table shows both forms:

| Parameter | Description |
|---|---|
| -I<input_file><br><br>--input<input_file> | The input file, including the full path.<br><br>EDL and STDF files are supported. They do not have to be loaded into the Data Log Explorer. |
| -O<output_file><br><br>--output<output_file> | The output CSV file, including the full path.<br><br>This parameter is optional. If it is not specified, the output file is saved in the same location as the input file and has the same name, just with the suffix .csv. |
| -T<report><br><br>--reporttype<report> | The desired summary report you want to export. Available types include:<br><br>- testsummary<br>- devicesummary<br>- binsummary<br>- wafersummary |
| -F<format><br><br>--reportformat<format> | Whether you want to export the summary with horizontal or vertical formatting:<br><br>- h: Horizontal orientation; groups are exported in adjacent columns.<br>- v: Vertical orientation; groups are exported in adjacent rows (the default).<br>- This setting has an effect only if the exported summary is grouped. (See the -G parameter, below.)<br><br>This is an optional parameter. If it is not specified, v is used. |
| -G<group><br><br>--group<group> | Whether and how the exported summaries should be `grouped`（raw: `02.08.04.13.02.03.05_Separating_summary_results_by_wafer__site__or_pin.md`）. These grouping options are available:<br><br>- wafer: Group by wafer. This is available for test summaries.<br>- site: Group by wafer. This is available for test summaries.<br>- pin: Group by wafer. This is available for test summaries.<br>- binsite: Group by site. This is available for bin summaries.<br><br>You can specify multiple grouping levels by separating the keywords with colons. For example, `site:pin` groups by site and pin.<br><br>This is an optional parameter. If it is not specified, exported summaries are not grouped. |
| -C<columns> | The columns you want the exported file to contain.<br><br><columns> is a string that contains the desired columns separated by colons. Each individual column is specified by these elements, separated by vertical bars \|:<br><br>- Field name: The title the column has in the summary tab in SmarTest.<br>- Format: If this value is set to 0, columns with group-related statistical data are shown besides each other.<br><br>This setting applies only to columns whose names begin with "statisticData.". It is ignored for other columns. It is also ignored when the -F flag is set to v.<br><br>- Title: The title the column has in the CSV file.<br><br>For example, `-C Sbin\|0\|softbin:Dev#\|0\|devices` exports two columns to the CSV file, one containing the id of the software bin (Sbin) with the title "softbin" and another containing the number of tested devices (Dev#) with the title "devices".<br><br>This is an optional parameter. If it is not specified, a default set of columns (depending on the type of summary that is exported) is included in the CSV file. The titles are the same as in the summary tabs in SmarTest. |
| -h<br><br>--help | Displays help information for the tool.<br><br>If -h or --help are specified, any other command line parameters are ignored and no export is performed. |

### Example（取自子主题 Integrated Result Tool reference › CSV Export command line tool）

`CsvExport -I ~/datalogs/myLog.std -O ~/Analysis/CSV/testSum.csv -T testsummary -F h -G site`: Exports the test summaries for the data log file myLog.std (located in the datalogs folder of your home directory) as the file testSum.csv (which is saved in the Analysis folder of your home directory). The summaries are grouped by site, and the data for each site are put into adjacent columns.

<!-- 语法节 end -->

## 是什么

**Integrated Result Tool 是「数据日志」的统计与图形评估工具。** 主文档正文只有两句，
**第一句就划清了它能评估哪两种东西**：

> 「The Integrated Result Tool supports the **statistical and graphical evaluation** of
> **saved data log files** and **the system data log stream**.」

**这句话里有两个二分，都要看清：**

| 二分 | 两半 | 差别 |
|---|---|---|
| **评估方式** | `statistical`（统计） / `graphical`（图形） | 原文用 `and` 并列——**两种都给，不是二选一** |
| **数据来源** | `saved data log files`（已存盘的文件） / `the system data log stream`（系统数据日志流） | **一个是落盘的，一个是流式的**（推断，依据是 `saved` 与 `stream` 两个词的对照） |

**「落盘 vs 流式」这个二分是本页最要紧的一条**：**两种来源在同一个工具里，
但原文把它们的名字并列写出来，说明工具知道自己在处理哪一种**。
**至于这两种来源在操作上有什么差别，主文档一个字没写**（推断：差别是有的，否则不必并列，
**但本页没有依据说差别是什么，所以不写**）。

### 第二句：一条三步链

> 「Using the tool, you can **load and open** data logs. The logs are **automatically summarized**,
> and you can **create a variety of result graphs** to easily spot data of interest.」

拆开就是本工具的工作链，**三步，顺序固定**：

| 步 | 原文 | 谁做 |
|---|---|---|
| **1. 载入并打开** | `you can load and open data logs` | **人** |
| **2. 自动汇总** | `The logs are automatically summarized` | **工具**——`automatically` 是原文的词 |
| **3. 造图** | `you can create a variety of result graphs` | **人** |

**第 2 步的 `automatically` 是这句的关节**：**汇总不是你要先做的事，是打开日志之后自动发生的**。
**所以这条链里人只有两个动作：打开、造图**，中间那一步被工具吃掉了。
**这也是本工具和「自己写脚本统计」的分界**（推断）。

**第 3 步的 `a variety of`（多种）没有列举是哪些图。** 主文档一个图名都没给——
**图名要到本页「语法 / 参数」节那些子主题段名里去才有，而那些子主题本页一篇没读**
（见 `## 出处`）。

**末尾 `to easily spot data of interest` 是目的**：造图不是为了出报告，
是为了**在数据里一眼看出值得看的地方**。**原文用的词是 `spot`（找出来），不是 `report`。**

### 本页能拿到的全部结构：三条子主题

主文档剩下的就是 `## Subtopics` 那张目录，**三条**：

| 子主题 | 从标题能读出的（**推断**） |
|---|---|
| `Principles of operation of the Integrated Result Tool` | 工作原理——**本工具怎么运转的** |
| `Using the Integrated Result Tool` | 怎么用 |
| `Integrated Result Tool reference` | 参考——**查表用的部分** |

> **上表整列都是推断**，依据**只有三条标题的措辞**。**这三篇本页一篇都没读。**

**这三条的分法本身有信息量**（推断）：**「原理 / 用法 / 参考」是手册的标准三分**，
所以本工具的知识被切成**「它为什么这样」/「你该怎么做」/「参数是什么」**三块，
**和本页「语法 / 参数」节那个 10,900 字符的大节遥相呼应**——
那一大节的段名全部带 `取自子主题` 后缀，**说明它是从 `reference` 和 `Using` 底下抽出来的**（推断）。

## 典型用法

**语料未写。** 主文档没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`。

**本页能给出的唯一流程就是「是什么」里那条三步链**，而且它只到骨架为止：

**打开数据日志 → （工具自动汇总）→ 造图看数据。**

**这条链有三处原文没交代，本页不替它补**：

| 缺什么 | 状态 |
|---|---|
| **怎么 load / open**（菜单在哪、支持哪些文件） | **语料未写**（子主题 `Using the Integrated Result Tool` 里可能有，**本页没读**） |
| **「汇总」汇总出什么**（一张表？几个 tab？） | **语料未写** |
| **能造哪些图、怎么造** | **语料未写**——主文档只说 `a variety of result graphs` |

> **本页刻意不引用「语法 / 参数」节里那些例子来当流程。**
> 那一节的例子（合并日志、关联日志、导出 CSV、排序、分组、过滤……）**来自 12 篇子主题**，
> **那 12 篇本页一篇都没读**（§11：不把没读的文档的内容写进正文）。
> **所以本页的 `## 典型用法` 是空的**——**这不是省略，是本页依据的文档里确实没有。**

## 和谁有关

**先说证据来源**：下面的关系分两类——
**① 来自主文档正文 / 子主题目录**（本页读了）；
**② 来自本页「语法 / 参数」节的段名与图题**（脚本逐字抽的文本，**本页读了这段文本，
但没有读它后面的那 12 篇子主题**）。**每一条都标出是哪一类。**

- [[analysis-views]] — **② 类证据**：本页「语法 / 参数」节的段名里出现了
  `…/02.08.04.13.02.04.02_Excluding_data_from_evaluation.md`、
  `…/02.08.04.13.02.04.04_Examining_the_underlying_data_of_an_analysis_view.md`，
  **路径都在 `02.08.04.13.02.04`（分析）这一段下面**。
  **所以：分析视图跑在本工具里**（推断，依据就是这份段名清单）。
  **主文档正文没有提过 analysis view 一个字。**
- [[data-navigation-views]] — **② 类**：同一条段名清单里出现 `…/02.08.04.13.02.03.05_…`，
  **和上面同属 `02.08.04.13.02`（Using the Integrated Result Tool）子树**（推断）。
- [[software-bin-summary-tab]] — **② 类**：段名里有一条 `…/02.08.04.13.03.02.05_Software_bin_summary_tab.md`。
  **它是主文档目录里 `Integrated Result Tool reference` 的孙辈**（推断，依据是路径层级）。
- [[test-summary-tab]] / [[raw-data-views]] — **② 类**：本页「语法 / 参数」节里出现了
  `Data log summary view`、`Raw data view` 这些**图题**（如 `` `Data log summary view_Sorting example` ``）。
  **它们是被截图的界面名，不是主文档正文提到的东西**（推断）。
- [[results]] — **① 类**：本页 `stage: results` 的理由——它评估的对象就是数据日志（测试结果）。
- [[stdf]] / [[edl-file]] — **② 类**：`## 语法 / 参数` 节的 `CsvExport` 段里写了
  `EDL and STDF files are supported`。**这是那一节里的话，主文档正文没提过这两种格式。**
- `Principles of operation of the Integrated Result Tool`（**未建、未读**）—
  主文档目录第一条。**本页讲不出本工具的原理**，原理全在那一篇里。
- `Using the Integrated Result Tool` / `Integrated Result Tool reference`（**均未建、未读**）—
  主文档目录的另外两条。**本页的 `## 典型用法` 之所以是空的，责任在这两篇身上。**
- [[error-map-tool]] / [[shmoo-tool]] / [[setup-management-tool]] / [[timing-diagram-tool]] / [[protocol-editor]] —
  同批建的 `gui` + `results` 页。**原文没有说它们和本工具的任何关系**——
  **本页不写「它们是本工具的一部分」这种话，因为没有依据。**

## 版本

`## Functional changes` 段有，只有一条：

> 「**Introduced in SmarTest 7.2.0**」

**这条是一个确定的版本号**（对比 `Error Map Tool` 那条写的是 `Introduced before SmarTest 6.3.2`，
**用的是 `before`、只给上界**）。**所以本页可以说：SmarTest 7.2.0 引入。**
**7.2.0 之后有没有变过，这篇 `## Functional changes` 一条都没记**——**语料未写**。

**另需注意**：本页「语法 / 参数」节里的子主题**各自还有自己的版本条目**（那 12 篇都可能有），
**本页一篇没读，所以本节只反映主文档这一条。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13_Integrated_Result_Tool.md`

**这就是本页正文的全部依据。整篇 21 行，去掉 frontmatter 和目录，正文只有两句 + 一行版本记录。**

**本页没做的**：

- **三条子主题一篇都没读**：`Principles of operation of the Integrated Result Tool`、
  `Using the Integrated Result Tool`、`Integrated Result Tool reference`。
  **本工具的原理、全部操作步骤、全部参数，本页一个字都没有。**
- **「语法 / 参数」节里那 12 篇更深一层的子主题也一篇没读**：
  `…Merging_data_logs.md`、`…Correlating_data_logs.md`、`…Exporting_data_logs.md`、
  `…Sorting_tables.md`、`…Highlighting_specific_data.md`、
  `…Separating_summary_results_by_wafer__site__or_pin.md`、`…Excluding_data_from_evaluation.md`、
  `…Examining_the_underlying_data_of_an_analysis_view.md`、`…Software_bin_summary_tab.md`、
  `…Table_filter.md`、`…Alerts_preference_settings.md`、`…CSV_Export_command_line_tool.md`。
  **本页正文没有使用它们的内容**——那一大节是脚本逐字抽的（§4），**不是我的转述**，
  **但也不是我的依据**。**这是本页篇幅明显小于「语法 / 参数」节的原因。**
- **一张图没看。** 「语法 / 参数」节里有 9 处图占位
  （`353295.jpg`、`137064.png`、`147881.png`、`136455.png`、`136456.png`、`137405.png`、
  `137005.png`、`137406.png`、`136421.png`、`136331.png`），**本页一处都没打开**。
  **所以本工具界面长什么样、图长什么样，本页没有任何来自图的结论。**
- **没有查 `system data log stream` 是什么**，**也没有查 `EDL` / `STDF` 的定义**。
- **没有查 `SmarTest 7.2.0` 在整条版本线上的位置**。

> ⚠️ **语料瑕疵。本节记的都是「语法 / 参数」节里的原文（本页一字未改，也没有改那一节的权力）。
> 本页只记录，不修正、不调和（§11.2）。**
>
> **① `-G` 三个分组关键字的说明全部写成「Group by wafer」**（逐字引，连续三行）：
>
> ```
> - wafer: Group by wafer. This is available for test summaries.
> - site: Group by wafer. This is available for test summaries.
> - pin: Group by wafer. This is available for test summaries.
> ```
>
> **`site` 与 `pin` 两条显然是复制粘贴没改**——按上下文应分别是 site、pin。
> **本页不替它改，也不假装没看见。**
>
> **② 关联日志示例里缺一个字母**（逐字引）：
> `(Any test methods from data log A that are not mentioned in the summary of data log B re also present in data log B.`
> ——**`re also` 应为 `are also`**，且**这句话末尾少一个右括号**。
>
> **③ Table filter 一处单复数不一致**（逐字引）：
> `For example, entering ~2 displays all row with a value smaller than 2 in the column.`
> ——**`all row` 应为 `all rows`**。
>
> **④ 合并日志示例里 `Source data log 2` 的表头少一列**（逐字引）：
>
> ```
> Test name   Device ID   Value
> A           P1.1        0.5     F
> ```
>
> ——**表头只有三列，数据行有四列**（`P/F` 那一列在表头里没有）。
> **同一节的 `Source data log 1` 表头是有 `P/F` 的**，两处不一致。
>
> **⑤ 一处本页判定「不能算错、但极易读错」的地方，本页不判**（逐字引两句）：
> `Only those rows are displayed where the content in the filtered column is greater than the first number you entered and less than the second number.`
> 与
> `-1,-1~1,1 finds all numbers from -1 to 1, including -1 and 1.`
> ——**前句说范围是开区间，后句的例子却说「包括 -1 和 1」**。
> **两者可以调和**：例子里的 `-1` 与 `1` 是**独立写出的精确值**，
> **不是范围的端点**（多值语法是「or」）。**但原文没有点破这一层**，
> **所以「范围到底含不含端点」读者只能靠自己推。本页把它标出来，不替原文下结论。**

`verified: doc-only`

