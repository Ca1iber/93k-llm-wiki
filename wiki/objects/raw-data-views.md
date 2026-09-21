---
type: object
title: Raw data views
layer: gui
stage: results
tags: [raw-data-views, results, data-navigation, table-filter, evaluation, gui]
related: [data-navigation-views, table-filter, test-summary-tab, integrated-result-tool, analysis-views, testflow-tool]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.01_Raw_data_views.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Raw data views

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Raw data view 是「汇总行」的展开。** 原文第一句：

> 「The raw data view displays **all individual records that are summarized in the selected row**
> of a **loaded data log**. You can use the raw data view to **examine in detail the results for a
> particular test, device, wafer, or bin**.」

**这句话的关节是 `summarized in`：**

| 角色 | 是谁 |
|---|---|
| **源头** | **data navigation view 里当前选中的那一行**（汇总） |
| **本视图** | **那一行背后的全部单条记录**（明细） |

**所以它不是独立的数据源**——**没有选中的行，它就没有内容**（推断，依据是 `the selected row`
这个定位）。**它能看什么，原文列了四种：`a particular test, device, wafer, or bin`。**

### 四个组成部分

原文说这个视图由**四块**构成（`All four elements are described below.`），
**它自己的三个 `##` 节加「列」就是这四块**：

| 块 | 原文的叫法 | 本文档的节 |
|---|---|---|
| 列 | `the columns describing each data log entry` | （在 `## Table` 一节里） |
| **工具栏** | `a toolbar` | `## Toolbar` |
| 两侧的标记 | `configurable fail and alert marks in the left and right margins` | `## Marks in the annotation and overview rulers` |
| 菜单 | `a **context** menu` | `## Shortcut menu` |

> ⚠️ **第三、四块的名字对不上**（见 `## 出处` 瑕疵③）：
> 总述用的是 **`context menu`**，**节标题和整节正文用的都是 `shortcut menu`**。
> **两个名字指同一个东西，原文没有说明。本页照实并列。**
>
> 另外总述那句里 `the left and right margins of **the tab**`——**这里说的是「tab」，
> 但本篇讲的是 view**，也是同一类残留（见 `## 出处` 瑕疵②）。

### 表的 25 列，分三块看

**列清单比同类的 summary tab 长，而且有三列是「没有标题文字」的**（原文自己这么叫）：

**（一）常规列（22 列）**

| 组 | 列 |
|---|---|
| **标识**（6） | `Test Suite` / `Test Method` / `Test` / `Test#` / `Pattern Name` / `Testflow` |
| **位置**（3） | `Wafer` / `Site` / `Pin` |
| **器件标识**（4） | `Device` / `Device ID` / `Part ID` / `Part Txt` |
| **限值与实测**（4） | `Lower` / `Upper` / `Value` / `Unit` |
| **判定**（1） | `P/F` |
| **时间**（2） | `Time` / `TS Time` |
| **文本**（2） | `Print to Datalog` / `Test Text` |

**（二）三个「没有标题文字」的列**（原文把它们写成 `Unlabeled column` 与 `Checkmark column`）

| 首发 | 原文的叫法 | 装什么 |
|---|---|---|
| 1 | `Unlabeled column (LS)` | **下限的比较运算符**（`The comparison operator for the lower limit`） |
| 2 | `Unlabeled column (US)` | **上限的比较运算符** |
| 3 | `Checkmark column (Include/Exclude)` | **勾选框：这个 test 的结果算不算进 summary 视图** |

> **第三列是本页的枢纽**：**上下文菜单里的 `Analyze Selection` / `Include` / `Exclude`
> 全都是这一列的另一种做法**——原文每一条都补了一句
> `This is equivalent to (un)checking the checkbox in the checkmark column …`
> （**原文这一组句子里混用了 `checkbox` 和 `check box` 两种写法**，见 `## 出处` 瑕疵⑤）。

**（三）两条时间列带同一句免责**：`Time` 与 `TS Time` 后面**各自**跟着
`(Due to algorithmic overhead, this number may not be the exact actual execution time.)`。

**四条能从列的定义里直接读出来的事实：**

| 列 | 原文要点 |
|---|---|
| `Testflow` | 是 **`the testflow number`**，**由 Integrated Result Tool 生成**，**每跑一次 testflow 加 1** |
| `Device` | **由 Integrated Result Tool 自动分配** |
| `Print to Datalog` | 装的是 **`PUT_DATALOG` API 的 comment 参数记进去的文本** |
| `Test Text` | 装的是 **`TEST_TXT` 字段**里的数据 |

**列的显示与顺序可配**（原文指向 `Raw Data preference settings`）。
**排序规则与 summary tab 完全相同**：点列标题**升序**（向上三角 `136425.png`）→
再点**降序**（倒三角 `136426.png`）→ 再点**取消排序**，回到 data store 里的原始顺序。

### 工具栏八个按钮——其中两个是一对开关

| 按钮 | 原文 | 要点 |
|---|---|---|
| **`Link`** | `Links the display in the view to the selected row in the data navigation view.` | **跟着选中走**：`if the selection in the data navigation view changes, the display updates automatically` |
| **`Pin`** | `**Freezes** the display in the view.` | **冻住**：`keeps displaying the rows it currently displays, even when the selection … changes`；**解冻要靠再点 `Link`** |
| `New` | `Creates a new raw data view.` | 再开一个 |
| `Statistics` | `Displays the summary of the currently displayed rows.` | 把「当前显示的这些行」的汇总显示出来；原文说它 `is similar to the contents of the selected row in the data navigation view` |
| `Preferences` | 开 `Raw Data preference page` | — |
| `Next Annotation` | 跳到**下一个带注解的行**（fail 指示 或 alert） | 带下拉清单，**可勾/取消勾注解类型** |
| `Previous Annotation` | 同上，往前 | 下拉清单同 |
| `Follow Data` | `Whether the view automatically scrolls to the bottom when new data is added.` | **是个高亮开关**：亮 → 自动滚到底看新数据；不亮 → 不自作主张滚动 |

> **`Link` / `Pin` 这一对是同一个机制的两面**，原文用了 `Freezes` 和 `resumed`：
> **`Pin` = 冻住，`Link` = 解冻。** **默认在 `Link` 那一侧**（推断——
> 原文把 `Link` 写在第一条，且 `Pin` 的说明里写 `Dynamic updating can be resumed by clicking
> the Link button`）。
>
> **`Next` / `Previous Annotation` 的下拉勾选有个直接后果**，原文给了例子：
> `if Failed Test is not checked in the drop-down list, SmarTest jumps only to rows containing
> alerts.` ——**没勾的类型，跳转时会被跳过。**

### 左右两条标尺

**术语与颜色约定和汇总侧一致：**

| 侧 | 原文的名字 | 等价说法 | 装什么 |
|---|---|---|---|
| 左 | **annotation ruler** | `(the left margin)` | **图标** |
| 右 | **overview ruler** | `(right margin)` | **小色矩形** |

**左侧四个图标**（多个时**互相重叠**；**悬停出 tooltip**）：

| 图标 | 含义（原文） |
|---|---|
| fail | `The test summarized in this row failed for at least one device.` |
| alert | `This row contains a cell with an alert.` |
| exclusion | `This row has been excluded from the summary.` |
| shmoo hole | `The test summarized in this row contains a shmoo hole.` |

**右侧色矩形**：**每个「有失败器件的行」和「有 alert 的行」各一个**；
**点它 → 选中表里对应的行**；**悬停 → 出 alert 原因的 tooltip**；
**悬停视图右上角的小色块 → 出总数**（失败行数、被排除行数、有 alert 的行数）。

**默认配色**：**红 = fails，蓝 = exclusions，黄 = alerts，青 = shmoo holes；四类全开。**

> ⚠️ **本节有两处是从汇总侧文档照搬过来的残留**（见 `## 出处` 瑕疵②）：
> ① 开头一句写的是 `The left and right margins of **the tab**`——**本篇讲的是 view，不是 tab**；
> ② **六个图的 alt 文本里有五个以 `Data log summary view_` 打头**
> （fail / alert / exclusion / shmoo hole 四个图标，加上两个排序三角），
> **而这里明明是 raw data view**；**只有 shmoo hole 那一个写的是
> `Data log summary view|Raw data view_Shmoo Hole icon`**（两个名字叠在一起）。

### 上下文菜单：一条**最容易读错**的界线

**这是本页最要紧的一条。** 原文在 `Filter` 子菜单的说明里把话说得很死：

> 「**Filter**: This submenu lets you restrict the display to either passed or failed tests.
> Note that **this is purely a display effect; hidden records are not excluded from evaluation**
> as with the Exclude command described above.」

**所以「看不见」有两种，后果完全相反：**

| 命令 | 原话 | 对**评估**的影响 |
|---|---|---|
| **`Filter` → `Show Only Pass` / `Show Only Fail`** | `purely a display effect` | **不影响** ——`hidden records are not excluded from evaluation` |
| **`Exclude` → …** | 每条都写 `…are removed from the summaries` | **影响** ——**从汇总里真的去掉了** |
| **`Analyze Selection`** | `Includes the selected rows into the summaries … and **exclude all rows that are not selected**` | **影响**，而且是**最狠的一条** |

**换句话说**：**用 `Filter` 藏起来的行还在数据里；用 `Exclude` 去掉的行不在数据里了。**
**这两个命令的名字都像「过滤」，但它们改的不是同一样东西**——
**一个改你看见什么，一个改汇总里有什么**（推断，依据就是上面那句 `purely a display effect`）。

**`Analyze Selection` 的完整含义**（原文写得比命令名清楚）：

> 「Includes the selected rows into the summaries based on the data log in which they are
> contained and exclude all rows that are not selected. In other words, the values in the data
> navigation view (and the graphs in any charts based on them) will only include the selected rows.」
>
> ——**一句「把选中的行留下，别的全去掉」**，**等价于**：
> `checking the checkbox in the checkmark column for these rows and unchecking all other rows`。

**`Include` 与 `Exclude` 两个子菜单**（注意两边分组不对称）：

| 子菜单 | 选项 | 效果 |
|---|---|---|
| **`Include`** | `Selection` | 选中的行**加进**汇总 |
| | `All` | 视图里**所有行**加进汇总 |
| **`Exclude`** | `Selection` | 选中的行**移出**汇总 |
| | `Pass` | **所有 pass 的行**移出汇总 |
| | `Fail` | **所有 fail 的行**移出汇总 |
| | `All` | 视图里**所有行**移出汇总 |
| **`Filter`** | `Show All` | 显示全部（**默认状态**） |
| | `Show Only Pass` | 只显示 pass 的行 |
| | `Show Only Fail` | 只显示 fail 的行 |

> **`Exclude` 比 `Include` 多两档**（`Pass` / `Fail`），**`Filter` 没有 `Pass`/`Fail` 的反向组合**。
> **这些不对称原文没有解释**（推断：`Exclude` 是「筛掉哪一类」，`Filter` 是「只看哪一类」，
> **但这是推断**）。

**菜单里其他命令：**

| 命令 | 原文要点 |
|---|---|
| `Open Definition` | **打开 testflow editor，并选中产生这条日志条目的 test suite**；**前提是 `The testflow must already be loaded into SmarTest.`** |
| `Open With` | 子菜单里只有一条：**`Protocol Monitor`**——**把选中行代表的数据在 Protocol Monitor view 里打开** |
| `Width` → `Autofit` | 每列调到刚好放得下内容 |
| `Copy` | 选中的行以 **tab 分隔的文本**进剪贴板 |
| `Alerts` / `Preferences` | 开两个偏好设置页 |

> **注意本页没有 `Show In` 子菜单**——**它出图的出口只有 `Open With` → `Protocol Monitor` 这一条**
> （对比：汇总侧的 tab 有 `Show In` 那一串）。**这是两页一个明显的差别**（推断，依据是
> 本页菜单清单里确实只有 `Open With`）。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## What to do next`。
下面每条都是从三个 `##` 节里直接读出来的。**

**1. 最常用的两步**：**在 data navigation view 里选中一行 → 本视图显示它背后的全部记录。**
**要它别跟着变**，就点 `Pin`；**要它重新跟着变**，点 `Link`。

**2. 想把「只看这一批」变成「就按这一批算」**

| 你想要 | 该用哪条 | 为什么 |
|---|---|---|
| **只是不想看见** pass 的行 | `Filter` → `Show Only Fail` | **`purely a display effect`**，评估不受影响 |
| **不想让 pass 的行算进汇总** | `Exclude` → `Pass` | 这些行 `are removed from the summaries` |
| **只想让当前选中的这批算进汇总** | **`Analyze Selection`** | 一条命令同时做「加选中 + 去其余」 |

**3. 一条一步到位的命令行**：`Analyze Selection`——**它等价于勾上选中的行、取消勾所有其他行**。

**4. 在表里手动逐行决定**：直接动 `Checkmark column (Include/Exclude)` 那一列的勾选框。
**命令与勾选框是同一件事的两种做法**（原文每条命令后面都写了 `This is equivalent to …`）。

**5. 排序**：点列标题 → 升序 → 再点 → 降序 → 再点 → **取消排序**（回 data store 原序）。

**6. 只显示某几行**：表**最上面一行（青色背景）就是 table filter**。
**注意它和 `Filter` 子菜单不是一回事**：**一个在表里输条件，一个在菜单里选 pass/fail**
（推断，原文只说前者是 `the table filter`，没有把两者放在一起比过）。

**7. 快速找问题行**：用 `Next Annotation` / `Previous Annotation` 在带注解的行之间跳；
**先在下拉清单里取消掉你不想跳的类型**（例：不勾 `Failed Test`，就只跳 alert）。

**8. 看一批行的汇总**：点 `Statistics`——显示当前显示的那些行的汇总。

**9. 数据流在滚的时候**：把 `Follow Data` 点亮，让它自动跟到底。

**10. 从一条记录跳去别处**：右键 → `Open Definition`（**前提：testflow 已载入**）→
跳到 testflow editor 里产生这条记录的 test suite；
或右键 → `Open With` → `Protocol Monitor` → 在 Protocol Monitor view 里看这条记录代表的数据。

**11. 拿去做别的**：`Copy` 拿 tab 分隔文本；`Width` → `Autofit` 把列宽理顺。

## 和谁有关

- [[data-navigation-views]] — **上游，而且是唯一来源。**
  原文两处都用 `the selected row in the data navigation view` / `the frontmost data navigation
  view` 来定义本视图显示什么。**换了选中行，本视图的内容就换。**
- [[table-filter]] — **表的第一行就是它**：原文 `The topmost row in the table (with a cyan
  background) is the table filter`，并直接指向那一篇。**本页有它，但写法规则本页没有。**
- [[test-summary-tab]] — **最直接的姊妹页。** 两者**共用一整套约定**：
  青色背景的 table filter 行、左右两条 ruler、四个图标、四个默认颜色、
  `Width`/`Copy`/`Alerts`/`Preferences` 这几条命令、排序的三连点规则。
  **差别在方向**：**汇总页一行 = 一个 test 的全部执行；本页一行 = 一条日志记录**
  （推断，依据是两篇各自的第一句）。**原文没有把两页放在一起比过。**
- [[analysis-views]] — **`Pin` / `Link` 这一对机制的另一处出现**：
  那一页也讲 `Pin` 冻住、`Link` 解冻。**两页讲的是同一个交互，但对象不同**
  （那边冻的是图，这边冻的是表）——**原文没有互相引用过。**
- [[integrated-result-tool]] — **宿主**：列的定义里写着 `Testflow` 列与 `Device` 列
  **都是由 Integrated Result Tool 生成/分配的**，**说明本视图跑在它里面**。
- [[testflow-tool]] — **`Open Definition` 的出口**：原文说它 `Opens the testflow editor`，
  **且要求 `The testflow must already be loaded into SmarTest.`**
- [[bin]] — 原文开头列了本视图能细看的四种对象之一：`…for a particular test, device, wafer,
  or **bin**`。**本页没有 bin 相关的任何机制**（推断：那是汇总侧的 tab 在做的事）。
- [[edl-file]] — 原文说数据来自 `a **loaded** data log`。
  **能加载哪些格式，本页没写**（那一篇没读），**所以这里不加内容。**
- [[smartest-7.2.0]] / [[smartest-7.2.1]] / [[smartest-7.2.2]] / [[smartest-7.2.3]] /
  [[smartest-7.10.1]] — 本页版本段的十条落在它们上面。
- `Protocol Monitor view`（**未建、未读**）— **本页唯一的出图出口**（`Open With` → `Protocol Monitor`）。
  **它长什么样、显示什么，本页一个字都没有。**
- `Detail data views` / `Examining the underlying data of a summary`（**均未建、未读**）—
  `## Related information` 的前两篇。**本页与它们的关系原文只给了名字。**
- `Raw Data preference settings` / `Raw Data preference page` / `Annotations preference page` /
  `Alerts preference page`（**均未建、未读**）— 偏好设置。
  **本页讲了默认值，没讲怎么改。**
- `Excluding data from evaluation` / `Highlighting specific data`（**均未建、未读**）—
  原文点名的两篇延伸阅读，**正对着本页最要紧的那条 `Exclude` / `Filter` 界线。**
- `PUT_DATALOG` / `TESTSET` / `PART_TXT` / `TEST_TXT`（**均未建**）— 四个列定义里提到的
  API 或字段名，**本页一律用反引号写，不展开。**

## 版本

`## Functional changes` 段有，**十条**：

> - Introduced in **SmarTest 7.2.0**
> - **SmarTest 7.2.1**: Added shortcut menu command Open Definition.
> - **SmarTest 7.2.1**: Added sorting of the table.
> - **SmarTest 7.2.1**: Renamed some columns.
> - **SmarTest 7.2.1**: Added indicators for excluded rows and shmoo holes.
> - **SmarTest 7.2.2**: Added Pattern Name column.
> - **SmarTest 7.2.2**: Added shortcut menu command Analyze Selection.
> - **SmarTest 7.2.3**: Added Part ID and Part Txt columns.
> - **SmarTest 7.2.3**: The Include and Exclude commands were converted into submenus.
> - **SmarTest 7.10.1**: Added Test Text column

**几条能和正文对上的**（推断，依据是正文里对应内容的措辞）：

| 版本条目 | 正文里的对应处 |
|---|---|
| `Added sorting of the table` | 「是什么」里那套三连点排序规则——**7.2.1 才有** |
| `Added indicators for excluded rows and shmoo holes` | 左侧四图标里的 exclusion 与 shmoo hole 两个 |
| `Added Pattern Name column` | 列清单里的 `Pattern Name` |
| `Added Part ID and Part Txt columns` | 列清单里的 `Part ID` / `Part Txt` |
| `The Include and Exclude commands were converted into submenus` | 现在 `Include` 与 `Exclude` 都带子项——**之前是平铺的单条命令** |
| `Added shortcut menu command Analyze Selection` | `Analyze Selection` 那条命令 |
| `Added Test Text column` | 列清单里的 `Test Text`（**7.10.1，本页最新的一条**） |
| `Renamed some columns` | **改了哪些、改成什么，原文没写** |

> **版本号写法**：这一篇的十条**都是三段式**（`7.2.0` / `7.2.1` / `7.2.2` / `7.2.3` / `7.10.1`），
> **没有出现同批 [[test-summary-tab]] 那条 `7.50` 那样的两段式**。
> **两篇的 `Added Pattern Name column` 都记在 7.2.2**（这是本页范围内可核的一条）。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.01_Raw_data_views.md`

**这就是本页正文的全部依据。整篇 179 行**——`## Toolbar`、`## Table`、
`## Marks in the annotation and overview rulers`、`## Shortcut menu`、`## Related information`、
`## Functional changes` **俱全，本批八页里第二长的一篇**。

**本页没做的**：

- **没有任何子主题可读**：本文档**没有 `## Subtopics` 一节**（这是本批次里唯一一篇没有子主题目录的）。
  **所以「本页没读的子主题」这项是空的**——**不是本页省略了，是原文没有。**
- **`## Related information` 的三篇一篇没读**：
  `Examining the underlying data of a summary`、`Detail data views`、`Raw Data preference settings`。
  **本页与它们的关系，本页一个字都讲不出来。**
- **`Open With` 指向的 `Protocol Monitor view` 没读**——
  **本页唯一的出图出口通向哪里，本页不知道。**
- **原文点名的延伸篇目没读**：`Excluding data from evaluation`、`Highlighting specific data`、
  `Table filter`、`Raw Data preference settings`/`page`、`Annotations preference page`、
  `Alerts preference page`。
  **其中 `Table filter` 尤其要紧**——**表的第一行就是它，而它的写法规则本页一个字都没有。**
  **`Excluding data from evaluation` 也尤其要紧**——它正对着本页那条 `Exclude` / `Filter` 界线。
- **`PUT_DATALOG`、`TESTSET`、`PART_TXT`、`TEST_TXT` 四篇 API/字段文档一篇没读**——
  **四个列的内容从哪来，本页只有原文那一句定义。**
- **一张图没看。** 原文里有 **9 处图**：`136441.png`（Raw data view）、
  `136444.png`（工具栏注解图）、四个图标 `136405.png` / `136406.png` / `140971.png` /
  `141950.png`、两个排序三角 `136425.png` / `136426.png`。
  **本页没有任何来自图的结论**——**工具栏长什么样、八个按钮怎么排，本页不知道，只有名字。**
- **没有查 `shmoo hole` 是什么**、**没有查 `data store` 的定义**、
  **没有查「loaded data log」支持哪些格式**。
- **没有把本页与 [[test-summary-tab]] 做过逐条对照**——
  **两页共用的那些段落是否一字不差，本页没有核**（见下面瑕疵②，那里只记了本页能自证的部分）。

> ⚠️ **语料瑕疵，照实记下、一处没替它改**（§11.2）：
>
> **① 主语与动词数不一致**（逐字引）：
> `Clicking a column title **sort** the table by this column in ascending order` ——**应为 `sorts`**。
> （**与同批 [[test-summary-tab]] 里那句错得一模一样**，本页照实记本页的这一处。）
>
> **② 从汇总侧照搬来的残留，三处**（逐字引）：
> a. `The left and right margins of **the tab** contain indicators for failed tests, alerts you have
> defined, and other special conditions.` ——**本篇讲的是 view，这句却写 `the tab`**。
> b. **六个图的 alt 文本里有五个以 `Data log summary view_` 打头**：
> `![Data log summary view_Fail test icon]`、`![Data log summary view_Alert icon]`、
> `![Data log summary view_Exclusiont icon]`、`![Data log summary view_Ascending triangle]`、
> `![Data log summary view_Descending triangle]`；
> **只有 shmoo hole 那一个写成 `Data log summary view|Raw data view_Shmoo Hole icon`**
> ——**两个视图名用 `|` 叠在一起**。**这一篇是 raw data view，不是 data log summary view。**
> c. 本节开头（原第二段）用 **`configurable fail and alert marks`（两类）**，
> 而紧接着的清单列了**四类**（fail / alert / exclusion / shmoo hole）。
>
> **③ 同一份文档里两个名字指同一样东西**（逐字引两处）：
> 总述写 `and it has a **context menu**`；
> 节标题与整节正文写 `## **Shortcut menu**` / `The **shortcut menu** of a raw data view contains
> these commands:`。**原文没有说明两者是同一样东西**，本页按同一样东西理解并已标注（推断）。
>
> **④ 拼写错，一处出现两遍**（逐字引两处）：
> `The drop-down list of the button lets you **check an uncheck** the annotation types.`
> ——**`Next Annotation` 与 `Previous Annotation` 两条下面各写了一遍**，
> **`check an uncheck` 应为 `check and uncheck`**。
>
> **⑤ 同一个词两种写法**（逐字引两处对照）：
> `This is equivalent to unchecking the **check box** in the checkmark column for these rows.`
> （`Exclude` 那条的总述句）
> 与同一节里另外六处的 `**checkbox**`
> （例：`This is equivalent to unchecking the **checkbox** in the checkmark column for the
> selected rows.`）。**`check box` 只出现这一次。**
>
> **⑥ `## Related information` 三个链接连排、无分隔**（逐字引全行）：
> `[Examining the underlying data of a summary](<02.08.04.13.02.04.01_Examining_the_underlying_data_of_a_summary.md>)[Detail data views](<02.08.04.13.03.03_Detail_data_views.md>)[Raw Data preference settings](<02.08.04.13.03.05.14_Raw_Data_preference_settings.md>)`
> ——**三个链接首尾相接，中间没有空格、逗号或换行**。
> **本页没有替它加分隔符。**（**本批里第三次遇到同一种排版缺失**，
> 另两处见 [[test-summary-tab]] 与 [[timing-diagram-tool]]。）
>
> **⑦ 子菜单里那一句的位置两边不一致**（逐字引两处对照）：
> `Include` 下面，`This is equivalent to …` 是**跟在每个子项后面**的（`Selection`、`All` 各一句）；
> `Exclude` 下面，`This is equivalent to unchecking the check box … for these rows.`
> 却**插在 `Exclude:` 这一条和它的子项 `Selection` 之间**。
> **两处排版不一致，原文没有说明。**
>
> 链接指向方面：本页未发现指错——四条子菜单/节内引用的相对路径
> （`…13.03.02_Data_navigation_views.md`、`…13.03.02.06_Table_filter.md`、
> `…13.03.04.07_Protocol_Monitor_view.md`、`…13.03.05.14_Raw_Data_preference_settings.md`）
> **与它们各自的名字对应**。

`verified: doc-only`

