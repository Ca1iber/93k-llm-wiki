---
type: object
title: Wafer summary tab
layer: gui
stage: results
tags: [wafer-summary-tab, summary-view, data-store, wafer, shortcut-menu, table-filter, annotation-ruler, overview-ruler, results-gui]
related: [test-summary-tab, device-summary-tab, hardware-bin-summary-tab, software-bin-summary-tab, data-navigation-views, table-filter, integrated-result-tool, edl-file, analysis-views, results, smartest-7.2.0, smartest-7.2.1, smartest-7.2.2, smartest-7.2.3]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.02_Wafer_summary_tab.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Wafer summary tab

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**定义句逐字（本篇正文第 1 句）：**

> 「The wafer summary tab of the summary view for a data store shows the consolidated
> results for all tests in the data store by wafer, displaying basic statistical evaluations
> for each wafer.」

**这一句里有四层：**

| # | 原句（**逐字**） | 含义 |
|---|---|---|
| 1 | `the summary view for a data store` | **它是 `data store` 的 `summary view` 里的一个 tab** |
| 2 | `shows the consolidated results for all tests in the data store` | **显示 data store 里所有测试的合并结果** |
| 3 | `by wafer` | **汇总的口径是「一颗 wafer 一行」** |
| 4 | `displaying basic statistical evaluations for each wafer` | **每颗 wafer 给一套基本统计** |

**第 3 层是这一页的分界线**：它和 [[device-summary-tab]] 的定义句**除 `by wafer` / `by device`
一词外逐字同形**（两篇的逐字对照见 `## 和谁有关`）。

**第 2 句把这一页分成三块**，逐字：

> 「In addition to the columns describing each wafer, a wafer summary tab contains configurable
> fail and alert marks in the left and right margins, and it has a shortcut menu. All three
> elements are described below.」

**三个部件：「一套描述每颗 wafer 的列」+「左右两条边距上的可配置标记」+「一个快捷菜单」。**
**原文说的是 `All three elements`（三个），本篇正文正好三节**
（`## Table` / `## Marks in the annotation and overview rulers` / `## Shortcut menu`）——
**本页按这三块分。**

> **⚠️ 部件的个数在这一族 tab 里不一样。** 本 wiki 已有的 [[hardware-bin-summary-tab]] 页
> 记的是 `Both elements`（**两个**：列 + 快捷菜单），**因为它没有边距标记那一节**。
> **（本页只核过 [[hardware-bin-summary-tab]] 那一页 wiki 页，它的 raw 本页没读。）**

### 部件一：表格（`## Table`）

**原文逐字（`## Table` 一节开头）：**

> 「The table in a wafer summary tab display in each row a summary for all test executions
> for a particular wafer. Clicking any field in a row selects the entire row (for example,
> for copying it).」

**即：一行一颗 wafer；点行里任何一格就选中整行**（原文举的用途是「为了复制它」）。
**⚠️ 这句里的 `display` 是原文的形态，见 `## 出处` ②。**

**表格最上面那一行不是表头，是过滤器**，逐字：

> 「The topmost row in the table (with a cyan background) is the table filter that lets you
> restrict which rows are displayed in the table by entering conditions. See Table filter
> for details.」

**三点：位置在最上面、背景色是 `cyan`、作用是按条件限制显示哪些行。**
**怎么写条件在 [[table-filter]] 那一篇里**（**那一篇的规则不在本页**）。

#### 8 个列，逐字

**原文逐字开场**：`A wafer summary tab can display these columns:`

| # | 列名（**逐字**） | 原文说明（**逐字**） |
|---|---|---|
| 1 | `Wafer` | `The number of the wafer. This number is assigned automatically by the Integrated Result Tool.` |
| 2 | `Wafer ID` | `The wafer ID from the data log.` |
| 3 | `Device#` | `The number of dies that were tested on the wafer.` |
| 4 | `Pass#` | `The number of devices on the wafer with a "pass" result.` |
| 5 | `Pass%` | `The percentage of devices on the wafer with a "pass" result.` |
| 6 | `Fail#` | `The number of devices on the wafer with a "fail" result.` |
| 7 | `Fail%` | `The percentage of devices on the wafer with a "fail" result.` |
| 8 | `Time` | `The sum of all test execution times for this wafer. (Due to algorithmic overhead, this number may not be the exact actual execution time.)` |

**只有 `Wafer` 那一列多出一句，原文用独立段落交代**（**不在那一格的字里**），逐字：

> 「This column cannot be deselected, that is, it is always visible in the view.」

**⚠️ 同一张表里 `die` 与 `device` 混用**：`Device#` 说的是
**`The number of dies that were tested on the wafer.`**，
而它上下的 `Pass#` 说的是 **`The number of devices on the wafer with a "pass" result.`**、
`Pass%` 说的是 **`The percentage of devices on the wafer with a "pass" result.`**。
**同一个量、同一张表、两个词（`dies` / `devices`）**，见 `## 出处` ③。

**⚠️ `Time` 那一条的括号是全篇唯一一处「这个数可能不准」的说明**——
而且它只挂在 `Time` 上（`Due to algorithmic overhead, this number may not be the exact actual
execution time.`），`Device#` / `Pass#` / `Fail#` 这三列**没有**同类说明。
**[[device-summary-tab]] 的 `Time` 列连这个括号都没有**（本页读过那一篇，见 `## 出处`）。

#### `Pass%` 与 `Fail%` 各有两个表示：数字 + 一条横条

**原文逐字（`Pass%` 那一条下面的独立段落）：**

> 「This percentage is also shown graphically in the cell by a horizontal green bar. For example,
> if one third of all devices pass, the left third of the cell is green and the rest has a normal
> background.」

**原文逐字（`Fail%` 那一条下面的独立段落）：**

> 「This percentage is also shown graphically in the cell by a horizontal red bar. For example,
> if two thirds of all devices fail, the left two thirds of the cell are red and the rest has a
> normal background.」

**两条的几何是同一个：横条**从格子左边起**按比例填，右边留正常底色**——
绿条配 `Pass%`、红条配 `Fail%`。**`136415.png` 那张示例截图里两条都在，颜色与左起的方向都对得上**
（见下面「### 图里看到的」）。

#### 列的显示与顺序由偏好设置决定

**原文逐字：**

> 「Which columns are displayed and the order in which they are displayed can be set in the
> preferences.」

**这里的 `the preferences` 是一个链接**，目标是
`02.08.04.13.03.05.23_Wafer_Summary_preference_settings.md`。
**⚠️ 同一个目标在本篇里有三个显示名**（见 `## 出处` ⑦）。**本页没读那一篇**——
**所以「还能显示哪些列」「默认顺序是什么」本页一个字都没有。**

#### 排序：点列标题三下

**原文逐字（`## Table` 一节末段；下面按原句断开成三块引——
因为原句中间夹着两张插图，插图不能进引文块，见 `## 出处` ⑫）：**

> 「Clicking a column title sort the table by this column in ascending order (rows with smaller
> values come first).」

> 「Clicking again sorts the table by the column in descending order」

> 「Clicking again unsorts the table. (The rows are displayed in the order in which they occur
> in the data store.)」

**三次点击是一个循环**：

| 第几次点 | 结果 | 指示 |
|---|---|---|
| 第 1 次 | **升序**（`rows with smaller values come first`） | 一张**朝上**的三角图，题注 `Data log summary view_Ascending triangle`（`raw/136425.png`） |
| 第 2 次 | **降序** | 一张**朝下**的三角图，题注 `Data log summary view_Descending triangle`（`raw/136426.png`） |
| 第 3 次 | **取消排序**（`unsorts the table`） | ——**回到 `the order in which they occur in the data store`** |

**⚠️ 原文那句 `Clicking a column title sort the table` 里 `sort` 没有 `s`**，见 `## 出处` ④。
**两个三角形各是一张图**：`raw/136425.png`（**朝上**的深色三角）、
`raw/136426.png`（**朝下**的深色三角）。**本页两张都看过，方向与题注对得上。**

### 部件二：左右两条边距上的标记（`## Marks in the annotation and overview rulers`）

**原文逐字（这一节开头）：**

> 「The left and right margins of the tab contain indicators for failed tests and cells
> containing alerts.」

**两条边距各是一把「尺子」**，原文各起了一个名字：

| 边距 | 原文的名字（**逐字**） | 放什么 |
|---|---|---|
| **左** | `The annotation ruler` | **图标**（icon），一行一个 |
| **右** | `The overview ruler` | **小色块**（`a small colored rectangle`） |

#### 左边（annotation ruler）：三个图标

**原文逐字（三个列表项）：**

| 图标题注（**逐字**） | 图 | 原文说明（**逐字**） |
|---|---|---|
| `Data log summary view_Fail test icon` | `raw/136405.png` | `The test summarized in this row failed for at least one device.` |
| `Data log summary view_Alert icon` | `raw/136406.png` | `This row contains a cell with an alert.` |
| `Data log summary view_Alert and fail icon` | `raw/136407.png` | `This row contains both an alert and at least one failing test.` |

> **⚠️ 第一条说明与 `## Table` 一节直接矛盾，这是本篇最该记的一处。**
> `## Table` 明文写着**一行是 `a particular wafer`**（`in each row a summary for all test
> executions for a particular wafer`），而这一条说的是 **`The test summarized in this row`**——
> **把这一行的主语写成了 `test`。**（`## Table` 一节的原文用的词是 `a summary`，
> 也没有出现过 `test` 作主语。）
> **（推断）这一节是从 test summary tab 那一篇整段搬过来的**，
> **依据：`## Marks in the annotation and overview rulers` 这一整节在两篇里逐字相同**
> （[[device-summary-tab]] 那一篇同样是 `The test summarized in this row failed for at least one
> device.`，而那一篇一行是一颗 **device**）。**原文没有承认也没有否认。本页照原样引，不替它改。**
> 三条图标本身本页都看过，**图形与题注是对得上的**（红旗带白叉 / 黄色警告三角 / 两者叠在一起）
> ——**错的是文字里的主语，不是图。**

**开关与默认值**，逐字：

> 「You can disable icons for fails and/or alerts in the Annotations preference page. By default,
> both are enabled.」

#### 右边（overview ruler）：小色块 + 一个总数提示

**原文逐字：**

> 「The overview ruler (right margin) contains a small colored rectangle for each row with a
> failed device and each row with an alert. Clicking a rectangle selects the corresponding row
> in the table. Hovering over a rectangle with the mouse displays a tooltip with the reason for
> the alert. Hovering over the small colored square in the upper right corner of the view
> displays a tooltip with the total numbers of failed rows and rows with alerts.」

**四件事**：

| 动作 | 结果（**逐字**） |
|---|---|
| 看 | 每个「有失败的行」和「有 alert 的行」各一个小色块 |
| 点一个色块 | `selects the corresponding row in the table` |
| 悬停在一个色块上 | `a tooltip with the reason for the alert` |
| 悬停右上角那个小方块 | `a tooltip with the total numbers of failed rows and rows with alerts` |

**⚠️ 同一位行，这一节换了个说法叫 `each row with a failed device`**（`## Table` 说的是
`a particular wafer`，左边那条图标说明说的是 `The test`）——
**一篇之内，一行的主语出现了 `test` / `device` / `wafer` 三个词。**

**颜色与开关**，逐字：

> 「You can choose the colors in the Annotations preference page and disable one or both kinds
> of indicators. By default, indicators for alerts are yellow and indicators for fails are red;
> both kinds are enabled.」

**默认值两条**：**alert = 黄、fail = 红，两类都开。**
**配置细节的出口是 `Highlighting specific data`**，逐字：

> 「For more information on configuring fail indicators and alerts, see Highlighting specific data.」

### 部件三：快捷菜单（`## Shortcut menu`）

**引导句逐字（这一句写的是 `wafer`，与本篇标题一致）：**

> 「The shortcut menu of a wafer summary tab contains these commands:」

**12 个顶层命令，逐字：**

| # | 命令（**逐字**） | 原文说明（**逐字**） | 条件 |
|---|---|---|---|
| 1 | `Refresh` | `Updates the system data log stream display with the latest logged data when it is paused (see below), but does not turn on automatic updating again, like Resume does.` | 前五条共有（见下） |
| 2 | `Pause` | `Stops automatic updating of tables displaying the system data log stream.` | 同上 |
| 3 | `Resume` | `Restarts automatic updating of the system data log stream.` | 同上 |
| 4 | `Clear` | `Removes all current entries from the system data log stream display in the Integrated Result Tool and clears the system event stream.` | 同上 |
| 5 | `Save and Clear` | `Displays a standard Save dialog in which you can save the current system event stream as an EDL file. After you have saved the file, all current entries from the system data log stream display in the Integrated Result Tool are removed and the system event stream is cleared.` | 同上 |
| 6 | `Show In` | `The command in this submenu lets you display the selected rows as a bin wafer map.` | —— |
| 7 | `Auto Update Wafer Chart` | `This command toggles whether any charts showing data from the data log stream are dynamically updated when new data log entries are created in the stream.` | **本命令独有（见下）** |
| 8 | `Exclude` | `This submenu lets you specify which records to exclude from the evaluation of the data store and display in the summary tabs. Records that you exclude in this tab are also excluded in other tabs.` | —— |
| 9 | `Width` | `This submenu includes the Autofit command that lets you make each column just wide enough to show all of its contents.` | —— |
| 10 | `Copy` | `Copies the selected rows to the clipboard as tab-separated text.` | —— |
| 11 | `Alerts` | `Opens the Alerts preference page.` | —— |
| 12 | `Preferences` | `Opens the Wafer Summary preference page.` | —— |

**前五条（`Refresh` / `Pause` / `Resume` / `Clear` / `Save and Clear`）共用一个条件**，
原文在每一条后面各写一遍，**五遍逐字相同**：

> 「This command is available only when the system data log stream is displayed in the tab.」

**即：这五条只在「这个 tab 正在显示 `system data log stream`」时才可用**——
**它们管的不是「这个 tab 的 wafer」，而是那个流。**
**（推断）所以这一页有两个身份**：一个是 **data store 的 wafer 汇总**（定义句说的），
另一个是 **`system data log stream` 的一个显示位**（前五条命令说的）。
**依据就是这两组文字并排在一篇里，而原文没有把这两种用途分开说。这是推断。**

#### `Auto Update Wafer Chart`：本篇唯一一个「条件句多一句」的命令

**它有一条别处没有的第二句条件**，逐字：

> 「This command is available only when the system data log stream is displayed in the tab.
> It does not affect the automatic update of any chart views when different rows are selected
> in the test summary tab.」

**⚠️ 两点：**

1. **别的命令的条件都只有第一句；只有这一条追加了第二句**——
   **即这一条命令的作用面和「换行选中」这件事无关**，原文特意点出了 **`the test summary tab`**
   （**本篇唯一一次点名另一个 tab**）。
2. **这一段里的 `test summary tab` 是本篇正文出现过的唯一一个同族 tab 名**，见 `## 和谁有关`。

**默认值与代价**，逐字：

> 「By default, these dynamic updates are deactivated. You can enable them to have the charts
> change automatically as new events are generated. However, when the data log stream contains
> a large number of entries, performance may suffer.」

**默认 `deactivated`（关着），要自己开；开着的代价是数据多时 `performance may suffer`。**

> **本页与 [[analysis-views]] 的接口就在这一条上**：[[analysis-views]] 说
> **system data log stream 的图默认不自动更新**，要开就得**在 `Wafer summary tab` 里选
> `Auto Update Wafer Chart`**。**本页是那条命令的所在地**（那一页的一句话是
> 「`Wafer summary tab` → `Auto Update Wafer Chart`」，本页给的是这条命令自己的原文说明）。
> **（那一页本页读过；它引的 raw 本页没读。）**

#### 几条要单独记的

- **`Clear` 与 `Save and Clear` 的作用面都在 [[integrated-result-tool]]**——
  原文两次点名 `the system data log stream display in the Integrated Result Tool`。
- **`Save and Clear` 会写一个 [[edl-file]]**：逐字
  `you can save the current system event stream as an EDL file`。
  **「存」与「清」是同一个命令的两半**——逐字
  `After you have saved the file, all current entries from the system data log stream display
  in the Integrated Result Tool are removed and the system event stream is cleared.`
  **原文没有给「只存不清」的选项。**
- **`Show In` 只有一个子命令，而原文用的是单数 `The command`**，逐字：
  `The command in this submenu lets you display the selected rows as a bin wafer map.`
  **目标是 `02.08.04.13.03.04.11_Bin_wafer_map_view.md`**（**本页没读**）。
  **⚠️ 而在 [[analysis-views]] 那一页的口径里，`Bin wafer map` 恰恰是「唯一一个不用
  Test summary 的视图」——两个 tab 的 `Show In` 各指向一个：本页指向 bin wafer map。**
- **`Exclude` 的作用范围跨 tab**：逐字
  `Records that you exclude in this tab are also excluded in other tabs.`
  **它自己没有「条件」那一格——所以排除是任何时候都能做的。**
  **⚠️ 但它的两个子项说的是 `tests`，而这一节讲的宾语是 `records` / `wafer`**，见 `## 出处` ⑤。
- **`Exclude` 有三个子项，逐字**：

  | 子项（**逐字**） | 说明（**逐字**） |
  |---|---|
  | `Selection` | `Excludes the tests summarized in the selected rows.` |
  | `Other` | `Excludes all tests except those summarized in the selected rows.` |
  | `None` | `No test are excluded. If there are any exclusions currently in effect, they are ended.` |

- **`Alerts` 与 `Preferences` 是纯出口**，分别打开 `the Alerts preference page`
  （`02.08.04.13.03.05.01_Alerts_preference_settings.md`）与
  `the Wafer Summary preference page`（`02.08.04.13.03.05.23_Wafer_Summary_preference_settings.md`）。**本页两个都没读。**

### 图里看到的（`## Example` 那一张截图）

`## Example` 一节整段只有一张图：题注 `Data log summary view_Wafer Summary`、文件 `raw/136415.png`。
**本页看过这一张**（§11.4：raw 里的图该读），它给出的文字之外的信息有四条：

| 看到的 | 说明 |
|---|---|
| **标题栏写着 `wafer_sample.edl`** | 这个 tab 当时显示的是一个 **`.edl` 数据日志**（**图里的证据，正文没有说**） |
| **列的顺序 = 上表 1→8 的顺序** | `Wafer` / `Wafer ID` / `Device#` / `Pass#` / `Pass%` / `Fail#` / `Fail%` / `Time`，**8 列全在，顺序与原文清单一致** |
| **绿条/红条确实左起** | `Pass%` 的绿条、`Fail%` 的红条都**从格子左边起**，右边留底色——与两条原文说明的几何一致 |
| **底部有五个 tab，`Wafer Summary` 是选中的那个** | 逐字读出：`Test Summary` / `Wafer Summary` / `Device Summary` / `HW Bin Summary` / `SW Bin Summary`——**这坐实了「summary tab 是一族」，也给出了这一族的成员与顺序** |

**左右两条边距在图里都看得到**：左边一列红色标记（annotation ruler），右边一列小红块（overview
ruler），**与 `## Marks in the annotation and overview rulers` 一节的文字对得上**；最上面那一行确实是**另一套底色的空行**（table filter）。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`，没有一个命令行。**
**它是「这个 tab 里有什么」的说明，不是「怎么用」的说明**——
**下面这些是从原文的 `## Table` / `## Marks in the annotation and overview rulers` / `## Shortcut menu` 三节里落出来的动作。**

| 要做的 | 依据（**原文**） |
|---|---|
| **看每颗 wafer 的统计** | 一行一颗 wafer；8 个列全在上面那张表里 |
| **只想看某些 wafer 的行** | 最上面那一行是过滤器（背景 `cyan`），`by entering conditions`；规则在 [[table-filter]] |
| **按某列排序 / 取消排序** | 点列标题一下升序、两下降序、三下取消；两个三角形各是一张图 |
| **复制若干行** | 点行选中整行，`Copy` 把选中行以制表符分隔的文本放进剪贴板 |
| **一眼看出哪几行有失败 / 有 alert** | 左边界面的图标（红旗 / 黄三角 / 两者）；**图标可在偏好里关掉** |
| **跳到某一行** | 点右边界面的小色块；悬停看 alert 的原因；悬停右上角小方块看两类行的总数 |
| **改标记的颜色 / 关掉某一类标记** | 在 `Annotations preference page` 里改 |
| **把某些记录排除在评估之外** | 右键 `Exclude` → `Selection`（排除选中的这些）/ `Other`（反过来）/ `None`（取消所有排除）；**排除是跨 tab 生效的** |
| **看某个 wafer 的 bin 分布** | 右键 `Show In` → **bin wafer map**（**本页没读那一篇**） |
| **看正在跑的流** | `Pause` / `Resume` / `Refresh`——**前提是这个 tab 正在显示 `system data log stream`** |
| **让流里的图自己动** | `Auto Update Wafer Chart`——**默认是关的**；开着的代价是数据多时变慢 |
| **把这个流存成文件** | `Save and Clear`——存成 `an EDL file`；**存完流会被清空** |
| **清掉流** | `Clear`——**注意它同时清掉 [[integrated-result-tool]] 里的显示与 `system event stream`** |
| **让列自动调到够宽** | 右键 `Width` → `Autofit` |
| **改显示哪些列、按什么顺序** | 在偏好设置里改（原文把它叫 `the preferences`，**本页没读那篇**） |
| **改 alerts / 改这个 tab 的偏好** | `Alerts` / `Preferences` 两条命令各打开一个偏好页 |

**两处本页要提醒的**：

1. **`Save and Clear` 会把流清掉**——「存」和「清」是同一个命令的两半，原文没有给「只存不清」的选项。
2. **`Auto Update Wafer Chart` 默认是关的**，而且**它只管「新事件进来时图要不要动」，
   不管「在别的 tab 里换选中时图要不要动」**——逐字
   `It does not affect the automatic update of any chart views when different rows are selected
   in the test summary tab.`

## 和谁有关

- [[test-summary-tab]] — **同族的第 1 个**（它的路径是 `02.08.04.13.03.02.01`，本页是 `02.08.04.13.03.02.02`）。
  **本篇正文点过 `the test summary tab` 一次**（在 `Auto Update Wafer Chart` 那条里）。
  **（推断）两者的父页都是 [[data-navigation-views]]，依据是路径编号；那一页本页没读。**
- [[device-summary-tab]] — **姊妹页**（路径 `02.08.04.13.03.02.03`，紧挨着本页）。
  **本篇从头到尾没有点过它。**
  **（推断）两篇是同一份模板的两次实例化，依据是本页两篇都读了、互相比过**：
  定义句、`## Table` 的开头、`## Marks in the annotation and overview rulers` **整节**、
  快捷菜单前五条的条件句，**都是逐字相同的**；
  差异只有四处：定义句的 `by wafer`/`by device`、列清单、`Show In` 的目标、
  以及**本页多一条 `Auto Update Wafer Chart`**。**哪一篇是复制源，原文没有说。这是推断。**
  **⚠️ 这篇没有 `[[device-summary-tab]]` 这个链接**——本篇正文一次都没提它，
  这条关系是本页自己按编号与逐字比对得出的（推断），不是原文给的。
- [[hardware-bin-summary-tab]] / [[software-bin-summary-tab]] — **同族的第 4、5 个**
  （路径 `02.08.04.13.03.02.04` / `02.08.04.13.03.02.05`）。**本篇没有点过它们。**
  **（推断）依据是路径编号，以及上面那张 `136415.png` 里读出的五个 tab 名。这是推断。**
- [[data-navigation-views]] — **本篇的上级**。原文 `## Related information` 只有两个链接，
  **第一个就是 `Data navigation views`**，链到 `02.08.04.13.03.02_Data_navigation_views.md`——
  **（推断）从编号看本页（`02.08.04.13.03.02.02`）确实是它的子项。
  依据只是路径编号 + 这一条 `## Related information` 链接，原文没有说两者的关系。那一篇本页没读。**
- [[table-filter]] — **原文逐字 `See Table filter for details.`**
  （表格过滤行的说明）。**本页只有「有这么一个东西、它管什么」——
  filter 那一行怎么写条件，不在本页的范围内。**
- [[integrated-result-tool]] — **三处点名**：`Wafer` 那一列的编号
  （`assigned automatically by the Integrated Result Tool`）、
  `Clear` 与 `Save and Clear` 的作用面（`the system data log stream display in the Integrated
  Result Tool`）。**那一篇本页没读。**
- [[edl-file]] — **`Save and Clear` 的产物**（`you can save the current system event stream
  as an EDL file`），**以及上面那张示例截图标题栏里的 `wafer_sample.edl`**。
  **本页只有这两处证据，EDL file 自己是什么本页没有。**
- [[analysis-views]] — **反向关系**：[[analysis-views]] 说 system data log stream 的图要开自动更新，
  得在 **`Wafer summary tab`** 里选 **`Auto Update Wafer Chart`**——
  **那条命令就是本页快捷菜单的第 7 条**。**本页给的是这条命令自己的原文说明。**
  **（本页读过 [[analysis-views]] 那一页；它引的 raw 本页没读。）**
- [[results]] — 本页 `stage: results` 的理由：**它是结果数据的一处汇总显示**。
  **⚠️ 本篇没有 `## Application` 这类自我定位段**，这条归属是本 wiki 的既有划分。
- [[smartest-7.2.0]] / [[smartest-7.2.1]] / [[smartest-7.2.2]] / [[smartest-7.2.3]] — **版本页**。
  本页 `## 版本` 四条各落一个（**四个版本号是逐条对上的**）。
- `Bin wafer map`（**未建、不在 allowlist，故用反引号**）— `Show In` 唯一的目标，
  `02.08.04.13.03.04.11_Bin_wafer_map_view.md`。**本页没读。**
- `Wafer Summary preference settings`（**未建**）— 本篇里被链了 3 次的那个偏好页，
  `02.08.04.13.03.05.23_Wafer_Summary_preference_settings.md`。
  **⚠️ 同一个目标在本篇里有三个显示名**（见 `## 出处` ⑦）。**本页没读。**
- `Alerts preference page` / `Annotations preference page`（**均未建**）——
  `Alerts` 命令与标记配置的两个出口，
  `02.08.04.13.03.05.01_Alerts_preference_settings.md` 与 `02.08.04.13.03.05.02_Annotations_preference_settings.md`。**本页两个都没读。**
- `Highlighting specific data`（**未建**）— 标记配置细节的出口，
  `02.08.04.13.02.03.03_Highlighting_specific_data.md`。**本页没读。**
- `system data log stream` / `system event stream`（**两个，均未建**）——
  **快捷菜单前五条命令操作的那两个东西**。
  **注意原文用的是两个名字**：`system data log stream`（前五条的条件句与 `Refresh` / `Pause` /
  `Resume` 的宾语）与 `system event stream`（`Clear` 与 `Save and Clear` 的宾语）。
  **两者是不是同一个东西，本篇没有说。**

## 版本

**本文档有 `## Functional changes` 段，四条**，逐字：

- **Introduced in SmarTest 7.2.0**
- **SmarTest 7.2.1: Renamed some columns.**
- **SmarTest 7.2.2: Added several shortcut menu commands.**
- **SmarTest 7.2.3: Added shortcut menu command to enable or disable dynamic updates for system data log stream charts.**

**⚠️ 第一条**不是** §11.2 ② 那个哨兵。**
哨兵写的是 `Introduced before SmarTest 6.3.2`（**`before`**），
而这一条写的是 `Introduced in SmarTest 7.2.0`（**`in`**）——
**所以这个 tab 确实是 SmarTest 7.2.0 引入的，不是「早于语料覆盖范围」。**
**判据是 `in` / `before` 这个词本身**（§11.2 ②），**不需要看别处。**

**后三条各改一处**：

| 版本 | 改了什么（**逐字**） | 本页能对上的东西 |
|---|---|---|
| `SmarTest 7.2.1` | `Renamed some columns.`——**改了列名，但没说是哪几个** | **对不上**：正文那张 8 列清单是**改名之后**的状态（推断），旧名本篇没给 |
| `SmarTest 7.2.2` | `Added several shortcut menu commands.` | **对不上**：哪些是 7.2.2 新加的，本篇没有标记 |
| `SmarTest 7.2.3` | `Added shortcut menu command to enable or disable dynamic updates for system data log stream charts.` | **对得上**：这就是 `Auto Update Wafer Chart`——**它的说明整段都在讲 `charts` 被 `dynamically updated`** |

**⚠️ 7.2.3 那条写的是 `command`（单数），而 7.2.2 那条写的是 `commands`（复数）**——
**单复数在四条里只对了这一处**：7.2.3 只加了一条命令（就是上表那一行）。

**（推断）本篇正文那张 8 列的清单，是 7.2.1 改名**之后**的状态**，
**而那 12 条快捷菜单命令是 7.2.2 + 7.2.3 加完之后的状态。**
**依据：版本段只说了「改了列名」「加了命令」，没有一句把版本段和那两张清单对上，也没给旧名。
原文没有承认也没有否认。这是推断。**

**与 wiki 目标版本（SmarTest 7.10.3）的关系**：
**本篇最后一条是 7.2.3，7.2.3 到 7.10.3 之间有没有再改，本篇没有依据。**
**但本篇的第一条是 7.2.0（`in`，不是哨兵），所以「这个 tab 从哪一版开始有」本篇给得出答案。**

详见 [[smartest-7.2.0]] / [[smartest-7.2.1]] / [[smartest-7.2.2]] / [[smartest-7.2.3]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.02_Wafer_summary_tab.md`
（TDC 主题号 `136412`；本地 raw md：**8,146 字节**、**115 行**——
**字节是磁盘上的字节数，行数是换行符个数**）

**本页没做的：**

- **文字之外的六张图，本页看了五张**：`raw/136405.png`（红旗带白叉）、
  `raw/136406.png`（黄色警告三角）、`raw/136407.png`（红旗 + 黄三角叠在一起）、
  `raw/136425.png`（朝上的三角）、`raw/136426.png`（朝下的三角），
  以及 `## Example` 那一张 `raw/136415.png`（**这是本页唯一一张「整个 tab 长什么样」的依据**）。
  **三张标记图的图形与题注是对得上的**（见上面「左边（annotation ruler）」那段），
  **两个排序三角的方向也与题注对得上**。**没有发现 `hardware-view` 那种题注错位/重复。**
- **`## Example` 那一节是空的（就一张图），所以脚本一个字都没收。**
  本篇**有** `## Example` 段，但整段只有一行图——脚本对「去掉图片就什么都不剩」的段一律不收。
  **⚠️ 但 `## 语法 / 参数` 节的样板话写的是「定义文档里没有 `Syntax` / `Parameters` / `Example`
  这类段标记」——这句话对本篇不准**：本篇**有** `## Example` 这个标题，
  它是「收了但里面只剩图片、所以什么都没收」，不是「没有这个段」。
  **这是样板话比脚本的实际判据说得宽**（§13.1 那类「说明与判据不是同一件事」），
  **不是语料的错。[[hardware-bin-summary-tab]] 那一页记的是同一条。**
- **`Table filter` 的规则不在本页** —— 原文只把出口指给它。
  **所以过滤器那一行怎么写条件、支持哪些条件，本页一个字都没有。**
- **`Wafer Summary preference settings` 没读** ——
  **所以「显示哪些列、什么顺序」「还有哪些偏好项」本页都没有；
  而这个目标在本篇里被链了 3 次，是本篇出现次数最多的出口。**
- **`Alerts preference page` / `Annotations preference page` / `Highlighting specific data`
  三个出口都没读** —— **所以标记的颜色能不能随便改、alert 是怎么产生的，本页没有。**
- **`Bin wafer map` 没读** —— **所以 `Show In` 之后长什么样，本页一个字都没有。**
- **`Data navigation views` 没读** —— **所以本页在那一组视图里的位置，本页只有路径编号作依据。**
- **`system data log stream` / `system event stream` 这两个东西是什么，本篇没写、本页也没有** ——
  **本页只知道快捷菜单前五条命令在它们上面动作，以及可以把流存成 EDL file。**
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其 [[table-filter]] / [[integrated-result-tool]] / [[edl-file]] 的 raw 都没读**——
  **本页与它们的关系全部取自本篇这一篇的正文，没有从对面回校过。**
- **本页与 [[device-summary-tab]] 的「姊妹页」关系，是两篇都读了之后逐字比出来的**——
  **本页没有读任何第三篇来佐证「哪一篇是模板」。**
- **`layer: gui` / `stage: results` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分
  （**（推断）`gui` 与「一个带表格、两条边距和右键菜单的 tab」相符，但这是本页的观察，不是原文说的**）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 本篇没有 `#### Subtopics` 目录块。** 本篇正文第 1 行就是定义句，
> **没有子主题清单、没有目录。**
>
> **② 一句里主语与谓语数不一致。** 逐字：
> `The table in a wafer summary tab display in each row a summary for all test executions for a particular wafer.`
> ——**主语 `The table` 是单数，谓语写成了 `display`（应为 `displays`）。本页引文照原样。**
>
> **③ 同一张列清单里 `die` 与 `device` 混用。** 逐字并列：
> `Device#: The number of dies that were tested on the wafer.`
> 与
> `Pass#: The number of devices on the wafer with a "pass" result.`
> ——**同一个量、同一张表、两个词（`dies` / `devices`）。本页照原样引。**
>
> **④ 同样的毛病在排序那一句里。** 逐字：
> `Clicking a column title sort the table by this column in ascending order`
> ——**`sort` 应为 `sorts`。本页照原样引。**
>
> **⑤ 又一处：`No test are excluded.`** 逐字（`Exclude` › `None` 那一条）：
> `None: No test are excluded. If there are any exclusions currently in effect, they are ended.`
> ——**`No test are` 应为 `No tests are`；同一句后半 `If there are any exclusions currently in
> effect, they are ended` 又是对的。本页照原样引。**
>
> **⑥ 这一节的宾语一会儿是 `records`、一会儿是 `tests`，而这一页的主题是 `wafer`。**
> 逐字并列三处：`Exclude` 那条写
> `This submenu lets you specify which records to exclude from the evaluation of the data store`，
> 而它的两个子项写 `Excludes the tests summarized in the selected rows.` /
> `Excludes all tests except those summarized in the selected rows.`
> ——**同一条命令的三个句子，宾语换了两个词**（`records` → `tests`）。
> **一种读法是这些说明是从 test summary 那一篇复制过来的遗留，
> 另一种读法是「被排除的记录」就是「测试」——两种原文都没有承认或否认，
> 本篇不替它改，也不据此断定。**
>
> **⑦ 同一个偏好页在本篇里有三个显示名。** 三处的目标文件是同一个
> （`02.08.04.13.03.05.23_Wafer_Summary_preference_settings.md`），显示名逐字分别是：
>
> - `the preferences`（正文：`can be set in the [preferences](<02.08.04.13.03.05.23_Wafer_Summary_preference_settings.md>).`）
> - `the Wafer Summary preference page`（`Preferences: Opens the [Wafer Summary preference page](<02.08.04.13.03.05.23_Wafer_Summary_preference_settings.md>).`）
> - `Wafer Summary preference settings`（`## Related information` 那个链接）
>
> **同一篇里同一个目标三种叫法。本页照实并列，不替它统一。**
>
> **⑧ 一行的主语在同一篇里出现三个词（`test` / `device` / `wafer`）**，
> 而且**其中 `The test summarized in this row` 与 `## Table` 一节的原文直接矛盾**。
> 逐字并列三处：
> `in each row a summary for all test executions for a particular wafer`（`## Table`）、
> `The test summarized in this row failed for at least one device.`（左边界面的图标说明）、
> `for each row with a failed device and each row with an alert`（右边边距的说明）。
> ——**这一处本页没有替它改，也没有据此断定哪一处才对**（见 `## 是什么` 里那一段）。
>
> **⑨ `## Related information` 两个链接粘在一起，中间没有任何分隔符。** 逐字：
> `[Data navigation views](<02.08.04.13.03.02_Data_navigation_views.md>)[Wafer Summary preference settings](<02.08.04.13.03.05.23_Wafer_Summary_preference_settings.md>)`
> ——**两个 markdown 链接首尾相接，`]` 后面直接是 `[`。**
> **（与 [[table-filter]] 那一篇记的同类毛病同形；本页只记本篇这一处。）**
> **这一节还漏了本篇正文点名的四个出口**：`Table filter`、`Bin wafer map`、
> `Alerts preference page`、`Annotations preference page` **都没进这份清单。本页照实并列。**
>
> **⑩ 六张图的题注共用同一个前缀 `Data log summary view_`。** 逐字：
> `Data log summary view_Ascending triangle` / `Data log summary view_Descending triangle` /
> `Data log summary view_Fail test icon` / `Data log summary view_Alert icon` /
> `Data log summary view_Alert and fail icon` / `Data log summary view_Wafer Summary`。
> ——**六张图来自同一个「视图」，前缀被写进了题注里，而题注本身读起来像
> 「视图名 + 下划线 + 图名」的拼接串。本页照实并列。**
> **⚠️ 其中 `Fail test icon` 那个题注里的 `Fail test` 与它自己说明里的
> `failed for at least one device` 也不是一套词**（见第 ⑧ 条）。
>
> **⑪ 本篇没有 §11.2 ① 那种编码损坏**（查过：正文里汉字 0 个、`鈥` 0 处、
> U+2026 的省略号 0 处、ASCII 的三个句点 0 处）。
>
> **⑫ 一句话中间夹着插图，和别的毛病不是一类，但引文会被它绊到，所以记在这里。**
> 排序那一整句原文是**一段连续的文字**，中间嵌了两张行内插图。逐字（**连插图标记一起**）：
> `Clicking a column title sort the table by this column in ascending order (rows with smaller
> values come first). This is indicated by a triangle ![Data log summary view_Ascending
> triangle](<../../../../raw/136425.png>). Clicking again sorts the table by the column in
> descending order, which is indicated by an upside-down triangle ![Data log summary view_Descending
> triangle](<../../../../raw/136426.png>). Clicking again unsorts the table. (The rows are
> displayed in the order in which they occur in the data store.)`
> ——**这不是语料的错，是「原文自己把图插在句子中间」这件事**；
> **本页按 §11.1「真要跳就断开成两个引文块」的办法处理**，
> **没有把插图标记塞进引文，也没有用省略号接过去**（上面「#### 排序」那三块）。

`verified: doc-only`
