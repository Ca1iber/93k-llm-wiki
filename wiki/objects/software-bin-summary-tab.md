---
type: object
title: Software bin summary tab
layer: gui
stage: results
tags: [software-bin-summary-tab, summary-view, data-store, bin, shortcut-menu, table-filter, results-gui]
related: [hardware-bin-summary-tab, table-filter, integrated-result-tool, data-navigation-views, bin, device-summary-tab, test-summary-tab, wafer-summary-tab, edl-file, smartest-7.2.0, smartest-7.2.1, smartest-7.2.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.05_Software_bin_summary_tab.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Software bin summary tab

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **155 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.05_Software_bin_summary_tab.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

Depending on your preference settings, the bin summary could look like this:

 !`Data log summary view_SW Bin Summary`（raw: `../../../../agent-html/136421.png`）

<!-- 语法节 end -->

## 是什么

**定义句逐字（本篇正文第 1 句）：**

> 「The software bin summary tab of the summary view for a data store shows the consolidated
> results for all software bins in the data store, displaying basic statistical evaluations for
> each.」

**这一句里有四层：**

| # | 原句（**逐字**） | 含义 |
|---|---|---|
| 1 | `the summary view for a data store` | **它是 `data store` 的 `summary view` 里的一个 tab** |
| 2 | `shows the consolidated results for all software bins in the data store` | **显示 data store 里**所有** software bin 的**合并**结果** |
| 3 | `displaying basic statistical evaluations for each` | **每个 bin 给一套基本统计** |
| 4 | `software bin`（而非 `hardware bin`） | **它管的是软件 bin，不是硬件 bin** |

**第 4 层是这一页的分界线**：**它和 [[hardware-bin-summary-tab]] 是一对**——
**而本篇正文里 `hardware bin summary` 出现了 3 次，全部是用来给本页的列或菜单加条件的**
（见下「两列是条件显示的」与 `## 出处` ⑤）。

**第 2 句（本篇第 2 段）把这一页分成两块**，逐字：

> 「In addition to the columns describing each bin, a software bin summary tab has a shortcut
> menu. Both elements are described below.」

**两个部件：一列一套「描述每个 bin 的列」，一个「快捷菜单」。**
**本篇正文的两节就按这个分**（`## Table` 与 `## Shortcut menu`）——
**本页也按这个分。**

### 部件一：表格（`## Table`）

**原文逐字（`## Table` 一节开头）：**

> 「The table in a software bin summary tab display in each row a summary for a particular bin.
> Clicking any field in a row selects the entire row (for example, for copying it).」

**即：一行一个 bin；点行里任何一格就选中整行**（原文举的用途是「为了复制它」）。
**⚠️ 这句里的 `display` 是原文的形态，见 `## 出处` ②。**

**表格最上面那一行不是表头，是过滤器**，逐字：

> 「The topmost row in the table (with a cyan background) is the table filter that lets you
> restrict which rows are displayed in the table by entering conditions. See Table filter for
> details.」

**三点：位置在最上面、背景色是 `cyan`（原文给的颜色名）、作用是按条件限制显示哪些行。**
**它的说明在 [[table-filter]] 那一篇**（**本页没读**）。

#### 8 个列，逐字

**原文逐字开场**：`A software bin summary tab can display these columns:`

| # | 列名（**逐字**） | 原文说明（**逐字**） |
|---|---|---|
| 1 | `SW Bin` | `The number of the software bin.` |
| 2 | `Desc` | `The description string of the software bin (if it has been specified).` |
| 3 | `Site` | `The number of the tested site.` |
| 4 | `Site%` | `The percentage of devices tested in the site that have been put into this bin.` |
| 5 | `Device#` | `The number of devices that have been put into this bin.` |
| 6 | `Bin%` | `The percentage of devices that have been put into this bin. (This is the value from the Device# column divided by the total number of tested devices.)` |
| 7 | `Good Bin` | `Whether this bin is a good bin (Y) or bad bin (N).` |
| 8 | `Reprobe Bin` | `Whether this bin is a reprobe bin (Y) or not (N).` |

**两列是条件显示的**（原文在栏外用独立段落交代，**不在那一格的字里**）：

> 「This column is displayed only when the hardware bin summary is grouped by site.」

**逐字出现了两次**——**`Site` 与 `Site%` 各一次**。
**即：这两列显不显示，取决于 `hardware bin summary` 有没有按 site 分组**——
**是**另一个 tab** 的状态在决定**这一页**的列。**（这是本篇唯一一处跨 tab 的联动，原文没有再多解释。）**

#### `Bin%` 有两个表示：数字 + 蓝条

**原文逐字（`Bin%` 那一条下面的独立段落）：**

> 「This percentage is also shown graphically in the cell by a horizontal blue bar. For example,
> if a quarter of all tested devices have been put into this bin, the left quarter of the cell is
> blue and the rest has a normal background.」

**即：同一格里既给百分数，又画一条蓝色横条；4 分之 1 就填左边 4 分之 1。**

#### 排序：点列标题三下

**原文逐字（`## Table` 一节末段）：**

> 「Clicking a column title sort the table by this column in ascending order (rows with smaller
> values come first). This is indicated by a triangle. Clicking again sorts the table by the
> column in descending order, which is indicated by an upside-down triangle. Clicking again unsorts
> the table. (The rows are displayed in the order in which they occur in the data store.)」

**三次点击是一个循环**：

| 第几次点 | 结果（**逐字**） | 指示（**逐字**） |
|---|---|---|
| 第 1 次 | `ascending order (rows with smaller values come first)` | `a triangle` |
| 第 2 次 | `descending order` | `an upside-down triangle` |
| 第 3 次 | `unsorts the table` | ——**回到 `the order in which they occur in the data store`** |

**⚠️ 原文那句 `Clicking a column title sort the table` 里 `sort` 没有 `s`**，见 `## 出处` ③。
**两个三角形各是一张图**（`raw/136425.png`、`raw/136426.png`，**本页两张都没看**）。

#### 列的显示与顺序由偏好设置决定

**原文逐字：**

> 「Which columns are displayed and the order in which they are displayed can be set in the
> preferences.」

**另一处出口**（**只有这一句提到**），逐字：

> 「If the bin summary tab is part of a correlation view, additional columns are displayed. See
> Correlation data store structure for more information.」

**即：这个 tab 还能出现在 `a correlation view` 里，那时会多出列**——
**多出什么列，本篇推给了 `Correlation data store structure`**（**本页没读**）。

### 部件二：快捷菜单（`## Shortcut menu`）

**⚠️ 这一节的引导句写的是 `hardware`，见 `## 出处` ⑤。** 逐字：

> 「The shortcut menu of a hardware bin summary tab contains these commands:」

**12 个顶层命令，逐字：**

| # | 命令（**逐字**） | 原文说明（**逐字**） | 条件（**逐字**） |
|---|---|---|---|
| 1 | `Refresh` | `Updates the system data log stream display with the latest logged data when it is paused (see below), but does not turn on automatic updating again, like Resume does.` | 前五条共有（见下） |
| 2 | `Pause` | `Stops automatic updating of tables displaying the system data log stream.` | 同上 |
| 3 | `Resume` | `Restarts automatic updating of the system data log stream.` | 同上 |
| 4 | `Clear` | `Removes all current entries from the system data log stream display in the Integrated Result Tool and clears the system event stream.` | 同上 |
| 5 | `Save and Clear` | `Displays a standard Save dialog in which you can save the current system event stream as an EDL file. After you have saved the file, all current entries from the system data log stream display in the Integrated Result Tool are removed and the system event stream is cleared.` | 同上 |
| 6 | `Exclude` | `This submenu lets you specify which records to exclude from the evaluation of the data store and display in the summary tabs. Records that you exclude in this tab are also excluded in other tabs.` | —— |
| 7 | `Filter` | `This submenu contains the Show Similar command, which lets you restrict the display in the tab to only those bins that have the same software bin number as the selected bin.` | —— |
| 8 | `Width` | `This submenu includes the Autofit command that lets you make each column just wide enough to show all of its contents.` | —— |
| 9 | `Group By` | `This Site command in this submenu lets you group the displayed summaries by site.` | —— |
| 10 | `Copy` | `Copies the selected rows to the clipboard as tab-separated text.` | —— |
| 11 | `Alerts` | `Opens the Alerts preference page.` | —— |
| 12 | `Preferences` | `Opens the SW Bin Summary preference page.` | —— |

**前五条（`Refresh` / `Pause` / `Resume` / `Clear` / `Save and Clear`）共用一个条件**，
原文在每一条后面各写一遍，**五遍逐字相同**：

> 「This command is available only when the system data log stream is displayed in the tab.」

**即：这五条只在「这个 tab 正在显示 `system data log stream`」时才可用**——
**它们管的不是「这个 tab 的软件 bin」，而是那个流。**
**（推断）所以这一页有两个身份**：一个是**data store 的软件 bin 汇总**（定义句说的），
另一个是 **`system data log stream` 的一个显示位**（前五条命令说的）。
**依据就是这两组文字并排在一篇里，而原文没有把这两种用途分开说。这是推断。**

**四条的细节要单独记：**

- **`Clear` 与 `Save and Clear` 的作用面都在 [[integrated-result-tool]]**——
  原文两次点名 `the system data log stream display in the Integrated Result Tool`。
- **`Save and Clear` 会写一个 [[edl-file]]**：逐字 `you can save the current system event stream
  as an EDL file`。**这是本篇唯一一次出现 `EDL` 这个词。**
- **`Exclude` 的作用范围跨 tab**：逐字
  `Records that you exclude in this tab are also excluded in other tabs.`
  **它自己没有「条件」那一格**——**所以排除是任何时候都能做的。**
- **`Filter` 只是一个快捷方式**：逐字
  `Note that this command is a shortcut for entering the software bin number in the table filter
  row at the top of the table. To show all rows again, click at the very left of the table filter
  row (which clears all filters).`
  **即：它等价于在 [[table-filter]] 那一行里填软件 bin 号；
  要显示全部，点过滤行最左边（清掉所有过滤）。**

**`Exclude` 与 `Group By` 各有两个子命令/行为要记：**

| 命令 | 子项（**逐字**） | 说明（**逐字**） |
|---|---|---|
| `Exclude` | `Selection` | `Excludes the tests summarized in the selected rows.` |
| | `Other` | `Excludes all tests except those summarized in the selected rows.` |
| | `None` | `No test are excluded. If there are any exclusions currently in effect, they are ended.` |
| `Group By` | `Site` | `instead of displaying one row per bin, SmarTest displays one row per site for each bin. It also displays the Site column (see above).` |

**`Group By > Site` 是**开关**，不是单向动作**，逐字：
`If the display is already grouped by site, choosing Group by > Site again removes the grouping.`

**而它正好是上面那两条条件列（`Site` / `Site%`）的开关**——
**原文在这一节里说 `It also displays the Site column (see above)`，
而 `Site` 那一列的条件写的是 `the hardware bin summary is grouped by site`**。
**两处指的是不是同一件事（本 tab 分组 / 另一个 tab 分组），原文没有对齐**（见 `## 出处` ⑤）。

**`Alerts` 与 `Preferences` 是纯出口**：分别打开两个偏好设置页
（`the Alerts preference page`、`the SW Bin Summary preference page`，**本页都没读**）。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有一个命令行。**
**它是「这个 tab 里有什么」的说明，不是「怎么用」的说明**——
**下面这些是从原文的 `## Table` / `## Shortcut menu` 两节里落出来的动作。**

| 要做的 | 依据（**原文**） |
|---|---|
| **看某个 bin 的统计** | 一行一个 bin；`SW Bin` / `Desc` / `Device#` / `Bin%` / `Good Bin` / `Reprobe Bin` 六个列**无条件显示** |
| **只想看某些行** | 最上面那一行是过滤器（背景 `cyan`），`by entering conditions`；细节在 [[table-filter]] |
| **只看某个软件 bin 号的行** | 右键 `Filter` → `Show Similar`；**它等价于在过滤器行里填这个 bin 号** |
| **清掉所有过滤** | `click at the very left of the table filter row (which clears all filters)` |
| **按某列排序 / 取消排序** | 点列标题一下升序、两下降序、三下取消；两个三角形各是一张图 |
| **按 site 看** | 右键 `Group By` → `Site`（**`Site` 与 `Site%` 两列会跟着出现**）；**再选一次取消分组** |
| **复制若干行** | 点行选中整行，`Copy` 把选中行以制表符分隔的文本放进剪贴板 |
| **把某些测试排除在评估之外** | 右键 `Exclude` → `Selection`（排除选中的这些）/ `Other`（反过来）/ `None`（取消所有排除）；**排除是跨 tab 生效的** |
| **看正在跑的流** | `Pause` / `Resume` / `Refresh`——**前提是这个 tab 正在显示 `system data log stream`** |
| **把这个流存成文件** | `Save and Clear`——存成 `an EDL file`；**存完流会被清空** |
| **清掉流** | `Clear`——**注意它同时清掉 [[integrated-result-tool]] 里的显示与 `system event stream`** |
| **让列自动调到够宽** | 右键 `Width` → `Autofit` |
| **改显示哪些列、按什么顺序** | 在偏好设置里改（原文把它叫 `preferences`，**本页没读**） |
| **改 alerts / 改这个 tab 的偏好** | `Alerts` / `Preferences` 两条命令各打开一个偏好页 |

**一处本页要提醒的**：**`Save and Clear` 会把流清掉**——
逐字 `After you have saved the file, all current entries from the system data log stream display in
the Integrated Result Tool are removed and the system event stream is cleared.`
**也就是说「存」和「清」是同一个命令的两半，原文没有给「只存不清」的选项。**

## 和谁有关

- [[hardware-bin-summary-tab]] — **成对的那一页，而本篇正文点了它 3 次**。
  逐字三处：`This column is displayed only when the hardware bin summary is grouped by site.`
  （**`Site` 与 `Site%` 两列各一次**）与
  `The shortcut menu of a hardware bin summary tab contains these commands:`
  （**快捷菜单那一节的引导句**）。
  **前两处说明：本 tab 的两列由**那个 tab** 的分组状态决定。
  第三处是本篇的一处瑕疵（见 `## 出处` ⑤）。**
  **本页只有这三处点名，hardware 那一页本页没读**——
  **两页的列与命令有何异同，本页没有依据说。**
- [[table-filter]] — **原文两次把出口指向它**：
  `See Table filter for details.`（表格过滤行的说明）与
  `this command is a shortcut for entering the software bin number in the table filter row at the
  top of the table`（`Filter` 命令的等价物）。
  **本页只有「有这么一个东西、它管什么」，那一页怎么填条件本页没有（本页没读那一页）。**
- [[integrated-result-tool]] — **`Clear` 与 `Save and Clear` 的作用面**。
  原文两次点名 `the system data log stream display in the Integrated Result Tool`。
  **本页只有这两处点名，那个工具本页没读。**
- [[edl-file]] — **`Save and Clear` 的产物**。原文逐字
  `you can save the current system event stream as an EDL file`。
  **`EDL` 这个词在本篇只出现这一次**；**本页只有这一句，EDL file 自己是什么本页没有。**
- [[data-navigation-views]] — **本篇的上级**。
  原文 `## Related information` 只有两个链接，**第一个就是 `Data navigation views`**，
  链到 `02.08.04.13.03.02_Data_navigation_views.md`——
  **从编号看本页（`…13.03.02.05`）确实是它的子项**。
  **本页没读那一篇，所以这个 tab 在那组导航视图里的位置本页没有。**
- [[bin]] — **（推断）`SW Bin` 那一列的主体**。
  依据只是：本页八列里有三列（`SW Bin` / `Bin%` / `Good Bin`）以 bin 为对象，
  而 wiki 另有一页叫 [[bin]]；**本篇没有点过 `bin` 这个页面名，
  也没有说软件 bin 与硬件 bin 的定义差别**——**那一页本页没读。这是推断。**
- [[device-summary-tab]] / [[test-summary-tab]] / [[wafer-summary-tab]] — **（推断）同族的
  另外几个 summary tab**。
  依据：本篇原文用过 `the summary tabs` 这个复数说法
  （`which records to exclude from the evaluation of the data store and display in the summary tabs`），
  **说明「summary tab」是一族**；**但本篇只点了 `hardware bin summary` 与它自己，
  另外三个名字一次都没出现，那三页本页也都没读。这是推断，不代表它们的结构与本页相同。**
- [[smartest-7.2.0]] / [[smartest-7.2.1]] / [[smartest-7.2.2]] — **版本页**。
  本页 `## 版本` 三条各落一个（**这三个版本号是逐条对上的，见 `## 版本`**）。
- `SW Bin Summary preference settings`（**未建、不在 allowlist，故用反引号**）—
  **本篇里被链了 3 次的那个偏好页**，目标是
  `02.08.04.13.03.05.19_SW_Bin_Summary_preference_settings.md`。
  **⚠️ 同一个目标在本篇里有三个显示名**（`preferences` / `SW Bin Summary preference page` /
  `SW Bin Summary preference settings`，**见 `## 出处` ⑥**）。**本页没读。**
- `Alerts preference settings`（**未建**）— **`Alerts` 命令的出口**，
  目标 `02.08.04.13.03.05.01_Alerts_preference_settings.md`。**本页没读。**
- `Correlation data store structure`（**未建**）— **`correlation view` 里多出来的列**的说明出口，
  目标 `02.08.04.13.02.02.04.01_Correlation_data_store_structure.md`。**本页没读**——
  **所以「多出哪些列」本页一个字都没有。**
- `system data log stream` / `system event stream`（**两个，均未建**）—
  **快捷菜单前五条命令操作的那两个东西**。
  **注意原文用的是两个名字**：`system data log stream`（`Refresh` / `Pause` / `Resume` / `Clear` /
  `Save and Clear` 的条件句）与 `system event stream`（`Clear` 与 `Save and Clear` 的动作宾语）。
  **两者是不是同一个东西，本篇没有说。**
- `correlation view`（**未建**）— 本 tab 可以嵌进去的另一种视图（只有一处提到）。

## 版本

**本文档有 `## Functional changes` 段，三条**，逐字：

- **Introduced in SmarTest 7.2.0**
- **SmarTest 7.2.1: Renamed some columns.**
- **SmarTest 7.2.2: Added several shortcut menu commands.**

**⚠️ 第一条**不是** §11.2 ② 那个哨兵。**
哨兵写的是 `Introduced before SmarTest 6.3.2`（**`before`**），
而这一条写的是 `Introduced in SmarTest 7.2.0`（**`in`**）——
**所以这个 tab 确实是 SmarTest 7.2.0 引入的，不是「早于语料覆盖范围」。**
**（本页与 [[edf]] / [[error-map]] / [[stdf]] / [[event-formatter]] / [[data-retrieval-library]]
那几页里那条哨兵不是一回事；那几页的哨兵形态本页引自那几页，不是本篇 raw。）**

**后两条各改一处，都带具体对象**：

| 版本 | 改了什么（**逐字**） |
|---|---|
| `SmarTest 7.2.1` | `Renamed some columns.`——**改了列名，但没说是哪几个** |
| `SmarTest 7.2.2` | `Added several shortcut menu commands.`——**加了命令，但没说是哪几个** |

**（推断）本篇正文那张 8 列的清单，是 7.2.1 改名**之后**的状态。**
**依据：版本段说 7.2.1 改过列名，而正文列了 8 个列名；
但原文没有一句话把版本段和那张清单对上（也没给旧名）。这是推断。**
**同理（推断）那 12 条快捷菜单命令是 7.2.2 加完之后的状态**——
**依据同上；哪些是 7.2.2 新加的，原文没有标记。**

**与 wiki 目标版本（SmarTest 7.10.3）的关系**：
**本篇最后一条是 7.2.2，7.2.2 到 7.10.3 之间有没有再改，本篇没有依据。**
**但本篇有个好处：它的第一条是 7.2.0（`in`，不是哨兵），
所以「这个 tab 从哪一版开始有」这件事，本篇给得出答案。**

详见 [[smartest-7.2.0]] / [[smartest-7.2.1]] / [[smartest-7.2.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.05_Software_bin_summary_tab.md`

**本页没做的：**

- **三张图一张都没看**：`raw/136425.png`（升序三角）、`raw/136426.png`（降序三角）、
  `raw/136421.png`（`Data log summary view_SW Bin Summary`——
  **按题注它就是本页这个 tab 的样子**）。
  §11.4 说 raw 里的图可读且该读。**其中第三张是本页唯一的「这个 tab 长什么样」的依据，
  本页没有打开它**——**所以上面那张 8 列的表只有文字依据，没有视觉依据。**
- **`Table filter` 没读** —— **而它是原文两次指定的出口**。
  **所以过滤器那一行怎么写条件、支持哪些条件，本页一个字都没有。**
- **`SW Bin Summary preference settings` 没读** ——
  **所以「显示哪些列、什么顺序」「还有哪些偏好项」本页都没有；
  而这个目标在本篇里被链了 3 次，是本篇出现次数最多的出口。**
- **`Alerts preference settings` 没读。**
- **`Correlation data store structure` 没读** ——
  **所以 `correlation view` 里会多出哪些列，本页没有。**
- **`Data navigation views` 没读** —— **所以本页在那一组视图里的位置，本页只有路径编号作依据。**
- **[[hardware-bin-summary-tab]] 没读** ——
  **而本篇三处点了它**。**所以两个 tab 的列与命令的异同、
  以及「本 tab 的 `Site` 列由 hardware 那侧的分组决定」在实现上意味着什么，本页都没有。**
- **`system data log stream` / `system event stream` 这两个东西是什么，本篇没写、本页也没有** ——
  **本页只知道快捷菜单前五条命令在它们上面动作，以及可以把流存成 EDL file。**
- **一张表里两个颜色的描述（`cyan` 底、蓝色横条）都只有文字，本页没有核过实际界面。**
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：[[table-filter]] / [[integrated-result-tool]] / [[edl-file]] 都没读**——
  **本页与它们的关系全部取自本篇这一篇的正文，没有从对面回校过。**
- **`layer: gui` / `stage: results` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分
  （**（推断）`gui` 与「一个带表格和右键菜单的 tab」相符，但这是本页的观察，不是原文说的**）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 本篇没有 `#### Subtopics` 目录块。** 本篇正文第 1 行就是定义句，
> **没有子主题清单、没有目录**——**而本批另外几篇（[[edf]] / [[error-map]] /
> [[event-formatter]] / [[data-retrieval-library]]）的第一节都是 `#### Subtopics`。**
> **本篇的链接全散在正文里（6 条相对链接 + 3 张图）。**
> （**那几页的形态本页引自那几页，不是本篇 raw。**）
>
> **② 一句里主语与谓语数不一致。** 逐字：
> `The table in a software bin summary tab display in each row a summary for a particular bin.`
> ——**主语 `The table` 是单数，谓语写成了 `display`（应为 `displays`）。
> 本页引文照原样。**
>
> **③ 同样的毛病在排序那一句里。** 逐字：
> `Clicking a column title sort the table by this column in ascending order`
> ——**`sort` 应为 `sorts`。本页照原样引。**
>
> **④ 又一处：`No test are excluded.`** 逐字（`Exclude` › `None` 那一条）：
> `None: No test are excluded. If there are any exclusions currently in effect, they are ended.`
> ——**`No test are` 应为 `No tests are`；同一句后半 `If there are any exclusions …
> they are ended` 又是对的。本页照原样引。**
>
> **⑤ `## Shortcut menu` 那一节的引导句写的是 `hardware`，而本篇讲的是 `software`。**
> 逐字（这是本节第一句）：
> `The shortcut menu of a hardware bin summary tab contains these commands:`
> ——**两种读法，原文没有承认也没有否认，本页并列不判：**
>
> - **(a)（推断）这是从 hardware 那一篇复制过来的遗留。**
>   **依据：① 本篇标题与定义句都写 `software bin summary`；
>   ② 列在它下面的命令是 software 专属的——`Filter` 那一条写
>   `the same software bin number as the selected bin`，
>   `Exclude` 那一条写 `Records that you exclude in this tab are also excluded in other tabs`，
>   `Group By` 那一条写 `It also displays the Site column (see above)`，
>   而 `Site` 列本篇明说只在 `the hardware bin summary is grouped by site` 时显示。
>   ③ `hardware bin summary` 在本篇另外出现两次，都是当**条件**用的
>   （`This column is displayed only when the hardware bin summary is grouped by site.`），
>   都**没有**拿它当本页的主语。**
> - **(b) 这两个 tab 真的共用同一个快捷菜单**，原文只是把硬件那一版的描述搬来用。
>   **本篇没有一句话支持这一读法，但也排除不了。**
>
> **本页不替它改成 `software`，也不据此断定两页的菜单相同。**
>
> **⑥ 同一个偏好页在本篇里有三个显示名。** 三处的目标文件是同一个
> （`02.08.04.13.03.05.19_SW_Bin_Summary_preference_settings.md`），显示名逐字分别是：
>
> - `preferences`（正文：`can be set in the [preferences](<…>)`）
> - `SW Bin Summary preference page`（`Preferences: Opens the [SW Bin Summary preference page](<…>).`）
> - `SW Bin Summary preference settings`（`## Related information` 那个链接）
>
> **同一篇里同一个目标三种叫法。本页照实并列，不替它统一。**
>
> **⑦ `## Related information` 两个链接粘在一起，中间没有任何分隔符。** 逐字：
> `[Data navigation views](<02.08.04.13.03.02_Data_navigation_views.md>)[SW Bin Summary preference settings](<02.08.04.13.03.05.19_SW_Bin_Summary_preference_settings.md>)`
> ——**两个 markdown 链接首尾相接，`]` 后面直接是 `[`。**
> **（与 [[dscp]] 那篇记的 `## Related information` 毛病同族；那一条本页引自 [[dscp]] 页，
> 不是本篇 raw。）**
> **同一处还有：本篇正文点名的 `Table filter`、`Correlation data store structure`、
> `Alerts preference page` 三个出口都没进这份 `Related information` 清单。**
>
> **⑧ `Group By` 的大小写在同一节里不一致。** 逐字并列：
> 菜单项写 `- Group By: This Site command in this submenu lets you group the displayed summaries
> by site.`（**`Group By`**），
> 而同一条的末句写 `choosing Group by > Site again removes the grouping`（**`Group by`**）。
> **本页照实并列，不替它统一。**
>
> **⑨ `Group By` 那一条的第一句语序坏了。** 逐字：
> `Group By: This Site command in this submenu lets you group the displayed summaries by site.`
> ——**`This Site command` 读不通**（**（推断）应为 `The Site command in this submenu`**；
> **依据只是这一节里 `Exclude` / `Filter` / `Width` 三条的同位置措辞分别是
> `This submenu …` / `This submenu contains …` / `This submenu includes …`，
> 只有这一条多出 `Site` 那个词。这是推断，原文没写对的是什么。**）
> **本页引文照原样。**
>
> **⑩ 三张图的题注共用同一个前缀 `Data log summary view_`。** 逐字：
> `Data log summary view_Ascending triangle` / `Data log summary view_Descending triangle` /
> `Data log summary view_SW Bin Summary`。
> ——**三张图来自同一个「视图」，前缀被写进了题注里，而题注本身读起来像
> 「视图名 + 下划线 + 图名」的拼接串。本页照实并列。**
>
> **⑪ `Site` 列显不显示的条件，与 `Group By > Site` 说的不是同一句话。**
> 逐字并列：`Site` 那一列下面写
> `This column is displayed only when the hardware bin summary is grouped by site.`，
> 而 `Group By` 那一条写 `This Site command in this submenu lets you group the displayed
> summaries by site.` 加 `It also displays the Site column (see above).`
> ——**一处说的是**hardware** bin summary 的分组，一处说的是**这个 tab** 自己的分组，
> 原文（这里正是 `(see above)` 那个交叉引用）没有说这两件事是不是同一件。**
> **本页并列两处，不替它对齐。**
>
> **⑫ 本篇没有 §11.2 ① 那种编码损坏**（本页查过：汉字 0 个、`鈥` 0 处）。
> **本篇 6,341 个字符，是本批 7 页里信息密度最高的一篇。**

`verified: doc-only`
