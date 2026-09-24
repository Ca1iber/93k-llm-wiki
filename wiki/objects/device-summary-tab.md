---
type: object
title: Device summary tab
layer: gui
stage: results
tags: [device-summary-tab, summary-view, data-store, device, shortcut-menu, table-filter, annotation-ruler, overview-ruler, results-gui]
related: [test-summary-tab, wafer-summary-tab, hardware-bin-summary-tab, software-bin-summary-tab, data-navigation-views, table-filter, integrated-result-tool, raw-data-views, edl-file, analysis-views, bin, results, smartest-7.2.0, smartest-7.2.1, smartest-7.2.2, smartest-7.2.3, smartest-7.3.1]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.03_Device_summary_tab.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Device summary tab

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**定义句逐字（本篇正文第 1 句）：**

> 「The device summary tab of the summary view for a data store shows the consolidated
> results for all tests in the data store by device, displaying basic statistical evaluations
> for each device.」

**这一句里有四层：**

| # | 原句（**逐字**） | 含义 |
|---|---|---|
| 1 | `the summary view for a data store` | **它是 `data store` 的 `summary view` 里的一个 tab** |
| 2 | `shows the consolidated results for all tests in the data store` | **显示 data store 里所有测试的合并结果** |
| 3 | `by device` | **汇总的口径是「一颗 device 一行」** |
| 4 | `displaying basic statistical evaluations for each device` | **每颗 device 给一套基本统计** |

**第 3 层是这一页的分界线**：它和 [[wafer-summary-tab]] 的定义句**除 `by device` / `by wafer`
一词外逐字同形**（两篇的逐字对照见 `## 和谁有关`）。

**第 2 句把这一页分成三块**，逐字：

> 「In addition to the columns describing each device, a device summary tab contains configurable
> fail and alert marks in the left and right margins, and it has a shortcut menu. All three
> elements are described below.」

**三个部件：「一套描述每颗 device 的列」+「左右两条边距上的可配置标记」+「一个快捷菜单」。**
**原文说的是 `All three elements`（三个），本篇正文正好三节**
（`## Table` / `## Marks in the annotation and overview rulers` / `## Shortcut menu`）——
**本页按这三块分。**

### 部件一：表格（`## Table`）

**原文逐字（`## Table` 一节开头）：**

> 「The table in a device summary tab display in each row a summary for all test executions
> for a particular device. Clicking any field in a row selects the entire row (for example,
> for copying it).」

**即：一行一颗 device；点行里任何一格就选中整行**（原文举的用途是「为了复制它」）。
**⚠️ 这句里的 `display` 是原文的形态，见 `## 出处` ②。**

**表格最上面那一行不是表头，是过滤器**，逐字：

> 「The topmost row in the table (with a cyan background) is the table filter that lets you
> restrict which rows are displayed in the table by entering conditions. See Table filter
> for details.」

**三点：位置在最上面、背景色是 `cyan`、作用是按条件限制显示哪些行。**
**怎么写条件在 [[table-filter]] 那一篇里**（**那一篇的规则不在本页**）。

#### 12 个列，逐字

**原文逐字开场**：`A device summary tab can display these columns:`

| # | 列名（**逐字**） | 原文说明（**逐字**） |
|---|---|---|
| 1 | `Device` | `The number of the device. This number is assigned automatically by the Integrated Result Tool.` |
| 2 | `Device ID` | `The device ID from the data log.` |
| 3 | `Part ID` | `The part ID from the data log.` |
| 4 | `Part Txt` | `The part description text (PART_TXT) from the data log.` |
| 5 | `Testflow` | `The testflow number, which is created by the Integrated Result Tool and increases by 1 every time the testflow is run.` |
| 6 | `Wafer` | `The number of the wafer on which the device is located.` |
| 7 | `Site` | `The number of the site to which the device belongs.` |
| 8 | `P/F` | `Whether the device ended up in a good bin (Pass) or bad bin (Fail).` |
| 9 | `SW Bin` | `The number of the software bin in which the device was put by the test.` |
| 10 | `HW Bin` | `The number of the hardware bin in which the device was put by the test.` |
| 11 | `Time` | `The sum of all test execution times for this device.` |
| 12 | `All Fail Bins` | `A comma-separated list of all software fail bins into which this device was put. This is useful if testing was done with overon enabled and a device may have reached multiple fail bins.` |

**四条要单独记的：**

- **`Device` 那一列没有「不可取消」的说明。**
  [[wafer-summary-tab]] 的 `Wafer` 列多一句 `This column cannot be deselected, that is, it is
  always visible in the view.`，**本篇同一位置的 `Device` 列没有这句**——
  **本页只能照实说「本篇没写」，不能替它推「所以能取消」。**
- **`Time` 那一列没有括号说明。** [[wafer-summary-tab]] 的 `Time` 列带一句
  `(Due to algorithmic overhead, this number may not be the exact actual execution time.)`，
  **本篇的 `Time` 列只有 `The sum of all test execution times for this device.`**
  **⚠️ 这是两篇逐字比对出来的差别，原文没有解释为什么。**
- **`Part Txt` 那一格把内部字段名也写了出来**：逐字
  `The part description text (PART_TXT) from the data log.`——
  **`PART_TXT` 是大写，本篇别处没有这个串。**
- **`All Fail Bins` 那一格是唯一一处提到 `overon` 的地方**：逐字
  `This is useful if testing was done with overon enabled and a device may have reached multiple
  fail bins.`——**`overon` 是什么，本篇没有定义**（**这个出处本页没读**）。

#### 列的两个「终点」：bin 与 wafer

12 列里有 5 列指回别的页：

| 列 | 指向 |
|---|---|
| `SW Bin` | [[bin]] 的**软件**那一侧 → 汇总在 [[software-bin-summary-tab]] |
| `HW Bin` | [[bin]] 的**硬件**那一侧 → 汇总在 [[hardware-bin-summary-tab]] |
| `P/F` | `a good bin (Pass) or bad bin (Fail)`——**`P/F` 是 `SW Bin` 的一个粗化** |
| `Wafer` | 这一列是 [[wafer-summary-tab]] 的汇总单位 |
| `Site` | 与 [[hardware-bin-summary-tab]] 的 `Site` / `Site%` 同名 |

**（这一段的对应关系是本页的推断）**：**依据只是这几个列名与 wiki 里已有页的名字相同，
本篇没有一句话把它们连起来**——**本页没有读那三篇的 raw，也没有读 [[bin]] 的 raw。**

#### 列的显示与顺序由偏好设置决定

**原文逐字：**

> 「Which columns are displayed and the order in which they are displayed can be set in the
> preferences.」

**这里的 `the preferences` 是一个链接**，目标是
`02.08.04.13.03.05.05_Device_Summary_preference_settings.md`。
**⚠️ 同一个目标在本篇里有三个显示名**（见 `## 出处` ⑥）。**本页没读那一篇**——
**所以「默认显示哪几列」「默认顺序是什么」本页一个字都没有。**

#### 排序：点列标题三下

**原文逐字（`## Table` 一节末段；下面按原句断开成三块引——
因为原句中间夹着两张插图，插图不能进引文块，见 `## 出处` ⑪）：**

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

**⚠️ 原文那句 `Clicking a column title sort the table` 里 `sort` 没有 `s`**，见 `## 出处` ③。
**两个三角形各是一张图**：`raw/136425.png`（**朝上**的深色三角）、
`raw/136426.png`（**朝下**的深色三角）。**本页两张都看过，方向与题注对得上。**
**⚠️ 这两张图的文件号与题注，与 [[wafer-summary-tab]] 那一篇完全相同**——
**是同一对图被两篇共用，不是哪一篇抄错了。**

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

> **⚠️ 第一条说明与 `## Table` 一节直接矛盾，而且在本篇里比在
> [[wafer-summary-tab]] 里更离谱。**
> `## Table` 明文写着**一行是一颗 `a particular device`**，而这一条说的是
> **`The test summarized in this row`**——**把这一行的主语写成了 `test`。**
> **（推断）这一整节是从 test summary tab 那一篇整段搬过来的**，
> **依据：`## Marks in the annotation and overview rulers` 这一整节在
> [[wafer-summary-tab]] 与 [[device-summary-tab]] 两篇里逐字相同**
> （两篇本页都读过，逐字比过）。
> **原文没有承认也没有否认。本页照原样引，不替它改。**
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

**⚠️ 同一位行，这一节换了个说法叫 `each row with a failed device`**——
**这一句在 [[wafer-summary-tab]] 里一字不差地出现，而那一篇的行是 wafer。**
**一篇之内，一行的主语出现了 `test` / `device` 两个词**（本篇的行本来就是 device，
所以这一节里只有 `test` 那个词是错位的）。

**颜色与开关**，逐字：

> 「You can choose the colors in the Annotations preference page and disable one or both kinds
> of indicators. By default, indicators for alerts are yellow and indicators for fails are red;
> both kinds are enabled.」

**默认值两条**：**alert = 黄、fail = 红，两类都开。**
**配置细节的出口是 `Highlighting specific data`**，逐字：

> 「For more information on configuring fail indicators and alerts, see Highlighting specific data.」

### 部件三：快捷菜单（`## Shortcut menu`）

**引导句逐字（这一句写的是 `device`，与本篇标题一致）：**

> 「The shortcut menu of a device summary tab contains these commands:」

**11 个顶层命令，逐字：**

| # | 命令（**逐字**） | 原文说明（**逐字**） | 条件 |
|---|---|---|---|
| 1 | `Refresh` | `Updates the system data log stream display with the latest logged data when it is paused (see below), but does not turn on automatic updating again, like Resume does.` | 前五条共有（见下） |
| 2 | `Pause` | `Stops automatic updating of tables displaying the system data log stream.` | 同上 |
| 3 | `Resume` | `Restarts automatic updating of the system data log stream.` | 同上 |
| 4 | `Clear` | `Removes all current entries from the system data log stream display in the Integrated Result Tool and clears the system event stream.` | 同上 |
| 5 | `Save and Clear` | `Displays a standard Save dialog in which you can save the current system event stream as an EDL file. After you have saved the file, all current entries from the system data log stream display in the Integrated Result Tool are removed and the system event stream is cleared.` | 同上 |
| 6 | `Show In` | `The command in this submenu lets you display the selected rows in the raw data view.` | —— |
| 7 | `Exclude` | `This submenu lets you specify which records to exclude from the evaluation of the data store and display in the summary tabs. Records that you exclude in this tab are also excluded in other tabs.` | —— |
| 8 | `Width` | `This submenu includes the Autofit command that lets you make each column just wide enough to show all of its contents.` | —— |
| 9 | `Copy` | `Copies the selected rows to the clipboard as tab-separated text.` | —— |
| 10 | `Alerts` | `Opens the Alerts preference page.` | —— |
| 11 | `Preferences` | `Opens the Device Summary preference page.` | —— |

**前五条（`Refresh` / `Pause` / `Resume` / `Clear` / `Save and Clear`）共用一个条件**，
原文在每一条后面各写一遍，**五遍逐字相同**：

> 「This command is available only when the system data log stream is displayed in the tab.」

**即：这五条只在「这个 tab 正在显示 `system data log stream`」时才可用**——
**它们管的不是「这个 tab 的 device」，而是那个流。**
**（推断）所以这一页有两个身份**：一个是 **data store 的 device 汇总**（定义句说的），
另一个是 **`system data log stream` 的一个显示位**（前五条命令说的）。
**依据就是这两组文字并排在一篇里，而原文没有把这两种用途分开说。这是推断。**

#### ⚠️ 这一族里唯一**没有**图表自动更新命令的那一个 tab

**本页与 [[wafer-summary-tab]] 逐条比过**（两篇都读了）：**快捷菜单的差只有一条**——

| 命令 | [[wafer-summary-tab]] | **本页** |
|---|---|---|
| `Auto Update Wafer Chart`（管 system data log stream 的图要不要跟着新事件动） | **有** | **本篇的清单里没有** |

**⚠️ 本页只能这么写**：**本篇的快捷菜单清单里没有这条命令。**
**至于这个 tab 在界面上是真的没有它、还是本篇漏写了，原文一个字都没说**——
**（推断）** 若读 [[analysis-views]] 那一页的口径，**开自动更新的位置是「哪个 tab 显示这个流，
就在那个 tab 里开」**（那一页给的对照是 `Test summary tab` → `Auto Update Chart`、
`Wafer summary tab` → `Auto Update Wafer Chart`），
**按这个读法，device tab 也该有一条同类命令**——**但这是从另一篇 wiki 页推的，不是本篇说的。
本页不当结论用。**（**[[analysis-views]] 那一页本页读过；它引的 raw 本页没读。**）

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
  `The command in this submenu lets you display the selected rows in the raw data view.`
  **目标是 `02.08.04.13.03.03.01_Raw_data_views.md`，也就是 [[raw-data-views]]**——
  **⚠️ 这和 [[wafer-summary-tab]] 的 `Show In` 指向的不是一个东西**
  （那一篇指向 bin wafer map）。**两个 tab 的 `Show In` 各去一处，本篇没说为什么。**
- **`Exclude` 的作用范围跨 tab**：逐字
  `Records that you exclude in this tab are also excluded in other tabs.`
  **它自己没有「条件」那一格——所以排除是任何时候都能做的。**
  **⚠️ 但它的两个子项说的是 `tests`，而这一节讲的宾语是 `records` / `device`**，见 `## 出处` ⑤。
- **`Exclude` 有三个子项，逐字**：

  | 子项（**逐字**） | 说明（**逐字**） |
  |---|---|
  | `Selection` | `Excludes the tests summarized in the selected rows.` |
  | `Other` | `Excludes all tests except those summarized in the selected rows.` |
  | `None` | `No test are excluded. If there are any exclusions currently in effect, they are ended.` |

- **`Alerts` 与 `Preferences` 是纯出口**，分别打开 `the Alerts preference page`
  （`02.08.04.13.03.05.01_Alerts_preference_settings.md`）与
  `the Device Summary preference page`（`02.08.04.13.03.05.05_Device_Summary_preference_settings.md`）。**本页两个都没读。**

### 图里看到的（`## Example` 那一张截图）

`## Example` 一节整段只有一张图，题注 `Data log summary view_Device Summary`、
文件 `raw/136417.png`。**本页看过这一张**（§11.4：raw 里的图该读），它给出的文字之外的信息有五条：

| 看到的 | 说明 |
|---|---|
| **标题栏写着 `ONLINEVALIDCOR1.edl`** | 这个 tab 当时显示的是一个 **`.edl` 数据日志**（**图里的证据，正文没有说**） |
| **屏幕上的列只有 8 个，不是 12 个** | 可见的是 `Device` / `Device ID` / `Wafer` / `Site` / `P/F` / `SW Bin` / `HW Bin` / `Time`——**清单里的 `Part ID` / `Part Txt` / `Testflow` / `All Fail Bins` 四个列在图上都没有** |
| **这张图因此比 7.2.3 / 7.3.1 早** | **（推断）** 版本段说 `Part ID` / `Part Txt` 是 7.2.3 加的、`All Fail Bins` 是 7.3.1 加的，**图上这三个列都不在**；**依据只是「版本段点名了这三个列」+「图上没有它们」，原文没有说这张图是什么版本截的。这是推断。**（`Testflow` 列不在图上，本篇没有版本条目能解释） |
| **`P/F` 列里是 `Pass` / `Fail` 两个词，不是 `P` / `F`** | **（推断）** 与 `P/F: Whether the device ended up in a good bin (Pass) or bad bin (Fail).` 的括号用词一致；**这是本页从图上读的，正文没有说格子里的字是 `Pass`** |
| **底部有五个 tab，`Device Summary` 是选中的那个** | 逐字读出：`Test Summary` / `Wafer Summary` / `Device Summary` / `HW Bin Summary` / `SW Bin Summary`——**这坐实了「summary tab 是一族」，也给出了这一族的成员与顺序**（**与 [[wafer-summary-tab]] 那一张截图读出来的五个名字逐字相同**） |

**左右两条边距在图里都看得到**：左边一列红色标记（annotation ruler），右边一列小红块（overview
ruler），**与 `## Marks in the annotation and overview rulers` 一节的文字对得上**；最上面那一行确实是**另一套底色的空行**（table filter）。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`，没有一个命令行。**
**它是「这个 tab 里有什么」的说明，不是「怎么用」的说明**——
**下面这些是从原文的 `## Table` / `## Marks in the annotation and overview rulers` / `## Shortcut menu` 三节里落出来的动作。**

| 要做的 | 依据（**原文**） |
|---|---|
| **逐颗 device 看结果** | 一行一颗 device；12 个列全在上面那张表里 |
| **只想看某些 device 的行** | 最上面那一行是过滤器（背景 `cyan`），`by entering conditions`；规则在 [[table-filter]] |
| **按某列排序 / 取消排序** | 点列标题一下升序、两下降序、三下取消；两个三角形各是一张图 |
| **复制若干行** | 点行选中整行，`Copy` 把选中行以制表符分隔的文本放进剪贴板 |
| **一眼看出哪几行有失败 / 有 alert** | 左边界面的图标（红旗 / 黄三角 / 两者）；**图标可在偏好里关掉** |
| **跳到某一行** | 点右边界面的小色块；悬停看 alert 的原因；悬停右上角小方块看两类行的总数 |
| **改标记的颜色 / 关掉某一类标记** | 在 `Annotations preference page` 里改 |
| **把某些记录排除在评估之外** | 右键 `Exclude` → `Selection`（排除选中的这些）/ `Other`（反过来）/ `None`（取消所有排除）；**排除是跨 tab 生效的** |
| **看某颗 device 的原始数据** | 右键 `Show In` → **[[raw-data-views]]**（**本页没读那一篇**） |
| **看正在跑的流** | `Pause` / `Resume` / `Refresh`——**前提是这个 tab 正在显示 `system data log stream`** |
| **把这个流存成文件** | `Save and Clear`——存成 `an EDL file`；**存完流会被清空** |
| **清掉流** | `Clear`——**注意它同时清掉 [[integrated-result-tool]] 里的显示与 `system event stream`** |
| **让列自动调到够宽** | 右键 `Width` → `Autofit` |
| **改显示哪些列、按什么顺序** | 在偏好设置里改（原文把它叫 `the preferences`，**本页没读那篇**） |
| **改 alerts / 改这个 tab 的偏好** | `Alerts` / `Preferences` 两条命令各打开一个偏好页 |

**三处本页要提醒的**：

1. **`Save and Clear` 会把流清掉**——「存」和「清」是同一个命令的两半，原文没有给「只存不清」的选项。
2. **想看 SW Bin / HW Bin 的汇总，不在这一页**——本篇的 `SW Bin` / `HW Bin` 只是**每颗 device
   落在哪个 bin**；**一整个 bin 的统计在 [[software-bin-summary-tab]] 与 [[hardware-bin-summary-tab]]**
   （**那两篇本页没读，这一句是本页按页名与列名给的指向，是推断。**）
3. **`All Fail Bins` 只在开了 `overon` 的测试里才有意义**——逐字
   `This is useful if testing was done with overon enabled and a device may have reached multiple
   fail bins.`

## 和谁有关

- [[test-summary-tab]] — **同族的第 1 个**（它的路径是 `02.08.04.13.03.02.01`，本页是 `.03`）。
  **本篇正文从头到尾没有点过它。**
  **（推断）两者的父页都是 [[data-navigation-views]]，依据是路径编号；那一页本页没读。**
- [[wafer-summary-tab]] — **姊妹页**（路径 `02.08.04.13.03.02.02`，紧挨着本页）。
  **本篇从头到尾没有点过它。**
  **（推断）两篇是同一份模板的两次实例化，依据是本页两篇都读了、逐字比过**：
  第 2 句（三部件那句）、`## Table` 的开头、排序那一段、
  `## Marks in the annotation and overview rulers` **整节**、快捷菜单前五条的条件句，
  **都是逐字相同的**；差异只有五处：定义句的 `by device`/`by wafer`、列清单、
  `Show In` 的目标、**本页少一条 `Auto Update Wafer Chart`**、
  以及 `Wafer` 列与 `Time` 列那两句说明的有无。**哪一篇是复制源，原文没有说。这是推断。**
  **⚠️ 这篇没有 `[[wafer-summary-tab]]` 这个链接**——本篇正文一次都没提它，
  这条关系是本页自己按编号与逐字比对得出的（推断），不是原文给的。
- [[hardware-bin-summary-tab]] / [[software-bin-summary-tab]] — **同族的第 4、5 个**
  （路径 `02.08.04.13.03.02.04` / `.05`）。
  **（推断）依据是路径编号，以及上面那张 `136417.png` 里读出的五个 tab 名**。
  **它们与本页的**实质**关系是本页的 `HW Bin` / `SW Bin` 两个列**：那两页各自是一整个 bin 的汇总，
  **而本页是「每颗 device 落进哪个 bin」**。**本篇没有一句话把这三页连起来。这是推断。**
- [[data-navigation-views]] — **本篇的上级**。原文 `## Related information` 只有两个链接，
  **第一个就是 `Data navigation views`**，链到 `02.08.04.13.03.02_Data_navigation_views.md`——
  **（推断）从编号看本页（`.03`）确实是它的子项。
  依据只是路径编号 + 这一条 `## Related information` 链接，原文没有说两者的关系。那一篇本页没读。**
- [[table-filter]] — **原文逐字 `See Table filter for details.`**
  （表格过滤行的说明）。**本页只有「有这么一个东西、它管什么」——
  filter 那一行怎么写条件，不在本页的范围内。**
- [[raw-data-views]] — **`Show In` 唯一的目标**。原文逐字
  `The command in this submenu lets you display the selected rows in the raw data view.`
  **本页只有这一句，那个视图自己是什么本页没有。**
- [[integrated-result-tool]] — **三处点名**：`Device` 与 `Testflow` 两列的编号
  （`assigned automatically by the Integrated Result Tool` / `created by the Integrated Result
  Tool`）、`Clear` 与 `Save and Clear` 的作用面。
  **那一篇本页没读。**
- [[edl-file]] — **`Save and Clear` 的产物**（`you can save the current system event stream
  as an EDL file`），**以及上面那张示例截图标题栏里的 `ONLINEVALIDCOR1.edl`**。
  **本页只有这两处证据，EDL file 自己是什么本页没有。**
- [[bin]] — **（推断）`SW Bin` / `HW Bin` / `P/F` / `All Fail Bins` 四列的主体**。
  依据只是：这四列的说明里都以 bin 为对象，而 wiki 另有一页叫 [[bin]]；
  **本篇没有点过 `bin` 这个页面名，也没有说硬件 bin 与软件 bin 的定义差别**——
  **那一页本页没读。这是推断。**
- [[analysis-views]] — **本页与它的接口是一条「没有的命令」**：
  [[analysis-views]] 说 system data log stream 的图要开自动更新得在 tab 里选命令，
  **而本篇的快捷菜单清单里没有那条命令**（见上面那一小节）。
  **（本页读过 [[analysis-views]] 那一页；它引的 raw 本页没读。）**
- [[results]] — 本页 `stage: results` 的理由：**它是结果数据的一处汇总显示**。
  **⚠️ 本篇没有 `## Application` 这类自我定位段**，这条归属是本 wiki 的既有划分。
- [[smartest-7.2.0]] / [[smartest-7.2.1]] / [[smartest-7.2.2]] / [[smartest-7.2.3]] /
  [[smartest-7.3.1]] — **版本页**。本页 `## 版本` 五条各落一个。
- `Device Summary preference settings`（**未建、不在 allowlist，故用反引号**）——
  本篇里被链了 3 次的那个偏好页，
  `02.08.04.13.03.05.05_Device_Summary_preference_settings.md`。
  **⚠️ 同一个目标在本篇里有三个显示名**（见 `## 出处` ⑥）。**本页没读。**
- `Alerts preference page` / `Annotations preference page`（**均未建**）——
  `Alerts` 命令与标记配置的两个出口，
  `02.08.04.13.03.05.01_Alerts_preference_settings.md` 与
  `02.08.04.13.03.05.02_Annotations_preference_settings.md`。**本页两个都没读。**
- `Highlighting specific data`（**未建**）— 标记配置细节的出口，
  `02.08.04.13.02.03.03_Highlighting_specific_data.md`。**本页没读。**
- `system data log stream` / `system event stream`（**两个，均未建**）——
  **快捷菜单前五条命令操作的那两个东西**。
  **注意原文用的是两个名字**：`system data log stream`（前五条的条件句与 `Refresh` / `Pause` /
  `Resume` 的宾语）与 `system event stream`（`Clear` 与 `Save and Clear` 的宾语）。
  **两者是不是同一个东西，本篇没有说。**
- `overon`（**未建**）— `All Fail Bins` 那一列里出现的唯一一个未定义术语。**本页没查它的出处。**

## 版本

**本文档有 `## Functional changes` 段，五条**，逐字：

- **Introduced in SmarTest 7.2.0**
- **SmarTest 7.2.1: Renamed some columns.**
- **SmarTest 7.2.2: Added several shortcut menu commands.**
- **SmarTest 7.2.3: Added Part ID and Part Txt columns.**
- **SmarTest 7.3.1: Added All Fail Bins column**

**⚠️ 第一条**不是** §11.2 ② 那个哨兵。**
哨兵写的是 `Introduced before SmarTest 6.3.2`（**`before`**），
而这一条写的是 `Introduced in SmarTest 7.2.0`（**`in`**）——
**所以这个 tab 确实是 SmarTest 7.2.0 引入的，不是「早于语料覆盖范围」。**
**判据是 `in` / `before` 这个词本身**（§11.2 ②），**不需要看别处。**

**后四条里，有两条点名了具体的列**——**这是这一族里少见的**：

| 版本 | 改了什么（**逐字**） | 本页能对上的东西 |
|---|---|---|
| `SmarTest 7.2.1` | `Renamed some columns.`——**改了列名，但没说是哪几个** | **对不上**：旧名本篇没给 |
| `SmarTest 7.2.2` | `Added several shortcut menu commands.` | **对不上**：哪些是 7.2.2 新加的，本篇没有标记 |
| `SmarTest 7.2.3` | `Added Part ID and Part Txt columns.` | **对得上**：上表第 3、4 列就是 `Part ID` / `Part Txt`，**名字逐字一致** |
| `SmarTest 7.3.1` | `Added All Fail Bins column` | **对得上**：上表第 12 列就是 `All Fail Bins` |

**⚠️ 最后一条 `Added All Fail Bins column` 句末没有句点**，
而它上面四条**都有**（含同位置的 `Added Part ID and Part Txt columns.`）
——**同一节里五个列表项，标点只有这一条不一样。本页照原样引。**

**（推断）本篇正文那张 12 列的清单，是 7.3.1 加完之后的状态**，
**而那 11 条快捷菜单命令是 7.2.2 加完之后的状态。**
**依据：版本段说了加过列、加过命令，但没有一句把版本段和那两张清单对上；
「哪些是 7.2.2 新加的」本篇没有标记。原文没有承认也没有否认。这是推断。**

**与 wiki 目标版本（SmarTest 7.10.3）的关系**：
**本篇最后一条是 7.3.1，7.3.1 到 7.10.3 之间有没有再改，本篇没有依据。**
**但本篇的第一条是 7.2.0（`in`，不是哨兵），所以「这个 tab 从哪一版开始有」本篇给得出答案。**

详见 [[smartest-7.2.0]] / [[smartest-7.2.1]] / [[smartest-7.2.2]] / [[smartest-7.2.3]] /
[[smartest-7.3.1]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.03_Device_summary_tab.md`
（TDC 主题号 `136416`；本地 raw md：**7,412 字节**、**105 行**——
**字节是磁盘上的字节数，行数是换行符个数**）

**本页没做的：**

- **文字之外的六张图，本页看了五张**：`raw/136405.png`（红旗带白叉）、
  `raw/136406.png`（黄色警告三角）、`raw/136407.png`（红旗 + 黄三角叠在一起）、
  `raw/136425.png`（朝上的三角）、`raw/136426.png`（朝下的三角），
  以及 `## Example` 那一张 `raw/136417.png`（**这是本页唯一一张「整个 tab 长什么样」的依据**）。
  **三张标记图的图形与题注是对得上的**（见上面「左边（annotation ruler）」那段），
  **两个排序三角的方向也与题注对得上**。**没有发现 `hardware-view` 那种题注错位/重复。**
- **`## Example` 那一节是空的（就一张图），所以脚本一个字都没收。**
  本篇**有** `## Example` 段，但整段只有一行图——脚本对「去掉图片就什么都不剩」的段一律不收。
  **⚠️ 但 `## 语法 / 参数` 节的样板话写的是「定义文档里没有 `Syntax` / `Parameters` / `Example`
  这类段标记」——这句话对本篇不准**：本篇**有** `## Example` 这个标题，
  它是「收了但里面只剩图片、所以什么都没收」，不是「没有这个段」。
  **这是样板话比脚本的实际判据说得宽**（§13.1 那类「说明与判据不是同一件事」），
  **不是语料的错。[[hardware-bin-summary-tab]] 与 [[wafer-summary-tab]] 两页记的是同一条。**
- **`Table filter` 的规则不在本页** —— 原文只把出口指给它。
  **所以过滤器那一行怎么写条件、支持哪些条件，本页一个字都没有。**
- **`Device Summary preference settings` 没读** ——
  **所以「默认显示哪些列、什么顺序」「还有哪些偏好项」本页都没有；
  而这个目标在本篇里被链了 3 次，是本篇出现次数最多的出口。**
- **`Alerts preference page` / `Annotations preference page` / `Highlighting specific data`
  三个出口都没读** —— **所以标记的颜色能不能随便改、alert 是怎么产生的，本页没有。**
- **[[raw-data-views]] 没读** —— **所以 `Show In` 之后长什么样，本页一个字都没有。**
- **`overon` 的出处没查** —— **所以 `All Fail Bins` 那一列里那个词是什么意思，本页没有。**
- **`Data navigation views` 没读** —— **所以本页在那一组视图里的位置，本页只有路径编号作依据。**
- **`system data log stream` / `system event stream` 这两个东西是什么，本篇没写、本页也没有** ——
  **本页只知道快捷菜单前五条命令在它们上面动作，以及可以把流存成 EDL file。**
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其 [[table-filter]] / [[integrated-result-tool]] / [[edl-file]] / [[bin]] /
  [[raw-data-views]] 的 raw 都没读**——
  **本页与它们的关系全部取自本篇这一篇的正文，没有从对面回校过。**
- **本页与 [[wafer-summary-tab]] 的「姊妹页」关系，是两篇都读了之后逐字比出来的**——
  **本页没有读任何第三篇来佐证「哪一篇是模板」，也没有读 test summary tab 那一篇
  （所以「这一节是从它那里搬来的」只是推断，不是比对结果）。**
- **`layer: gui` / `stage: results` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分
  （**（推断）`gui` 与「一个带表格、两条边距和右键菜单的 tab」相符，但这是本页的观察，不是原文说的**）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 本篇没有 `#### Subtopics` 目录块。** 本篇正文第 1 行就是定义句，
> **没有子主题清单、没有目录。**
>
> **② 一句里主语与谓语数不一致。** 逐字：
> `The table in a device summary tab display in each row a summary for all test executions for a particular device.`
> ——**主语 `The table` 是单数，谓语写成了 `display`（应为 `displays`）。本页引文照原样。**
>
> **③ 同样的毛病在排序那一句里。** 逐字：
> `Clicking a column title sort the table by this column in ascending order`
> ——**`sort` 应为 `sorts`。本页照原样引。**
>
> **④ 又一处：`No test are excluded.`** 逐字（`Exclude` › `None` 那一条）：
> `None: No test are excluded. If there are any exclusions currently in effect, they are ended.`
> ——**`No test are` 应为 `No tests are`；同一句后半 `If there are any exclusions currently in
> effect, they are ended` 又是对的。本页照原样引。**
>
> **⑤ 这一节的宾语一会儿是 `records`、一会儿是 `tests`，而这一页的主题是 `device`。**
> 逐字并列三处：`Exclude` 那条写
> `This submenu lets you specify which records to exclude from the evaluation of the data store`，
> 而它的两个子项写 `Excludes the tests summarized in the selected rows.` /
> `Excludes all tests except those summarized in the selected rows.`
> ——**同一条命令的三个句子，宾语换了两个词**（`records` → `tests`）。
> **一种读法是这些说明是从 test summary 那一篇复制过来的遗留，
> 另一种读法是「被排除的记录」就是「测试」——两种原文都没有承认或否认，
> 本篇不替它改，也不据此断定。**
>
> **⑥ 同一个偏好页在本篇里有三个显示名。** 三处的目标文件是同一个
> （`02.08.04.13.03.05.05_Device_Summary_preference_settings.md`），显示名逐字分别是：
>
> - `the preferences`（正文：`can be set in the [preferences](<02.08.04.13.03.05.05_Device_Summary_preference_settings.md>).`）
> - `the Device Summary preference page`（`Preferences: Opens the [Device Summary preference page](<02.08.04.13.03.05.05_Device_Summary_preference_settings.md>).`）
> - `Device Summary preference settings`（`## Related information` 那个链接）
>
> **同一篇里同一个目标三种叫法。本页照实并列，不替它统一。**
>
> **⑦ 一行的主语在同一篇里出现两个词（`test` / `device`），而且 `test` 那一个是错的。**
> 逐字并列两处：
> `in each row a summary for all test executions for a particular device`（`## Table`）
> 与
> `The test summarized in this row failed for at least one device.`（左边界面的图标说明）。
> ——**后一句把一个「按 device 汇总」的 tab 的行说成了 `The test`。**
> **这一处本页没有替它改，也没有据此断定哪一处才对**（见 `## 是什么` 里那一段）。
> **⚠️ 同一个句子在 [[wafer-summary-tab]] 那一篇里逐字相同**——
> **所以这不是本篇独有的笔误，是一整节被整段复用了。**
>
> **⑧ `## Related information` 两个链接粘在一起，中间没有任何分隔符。** 逐字：
> `[Data navigation views](<02.08.04.13.03.02_Data_navigation_views.md>)[Device Summary preference settings](<02.08.04.13.03.05.05_Device_Summary_preference_settings.md>)`
> ——**两个 markdown 链接首尾相接，`]` 后面直接是 `[`。**
> **（与 [[table-filter]] 那一篇记的同类毛病同形；本页只记本篇这一处。）**
> **这一节还漏了本篇正文点名的四个出口**：`Table filter`、`raw data view`、
> `Alerts preference page`、`Annotations preference page` **都没进这份清单。本页照实并列。**
>
> **⑨ 六张图的题注共用同一个前缀 `Data log summary view_`。** 逐字：
> `Data log summary view_Ascending triangle` / `Data log summary view_Descending triangle` /
> `Data log summary view_Fail test icon` / `Data log summary view_Alert icon` /
> `Data log summary view_Alert and fail icon` / `Data log summary view_Device Summary`。
> ——**六张图来自同一个「视图」，前缀被写进了题注里，而题注本身读起来像
> 「视图名 + 下划线 + 图名」的拼接串。本页照实并列。**
> **⚠️ 其中 `Fail test icon` 那个题注里的 `Fail test` 与它自己说明里的
> `failed for at least one device` 也不是一套词**（见第 ⑦ 条）。
>
> **⑩ 版本段最后一条句末缺句点**，逐字：
> `- SmarTest 7.3.1: Added All Fail Bins column`
> ——**它上面四条都带句点**（`SmarTest 7.2.1: Renamed some columns.` /
> `SmarTest 7.2.2: Added several shortcut menu commands.` /
> `SmarTest 7.2.3: Added Part ID and Part Txt columns.`）
> ——**第一条 `Introduced in SmarTest 7.2.0` 不带，
> 但那是「Introduced」那一类，与后四条不同类**）。**本页照原样引。**
>
> **⑪ 一句话中间夹着插图，和别的毛病不是一类，但引文会被它绊到，所以记在这里。**
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
>
> **⑫ 本篇没有 §11.2 ① 那种编码损坏**（查过：正文里汉字 0 个、`鈥` 0 处、
> U+2026 的省略号 0 处、ASCII 的三个句点 0 处）。

`verified: doc-only`
