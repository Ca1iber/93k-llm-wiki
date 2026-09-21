---
type: concept
title: Setting chart display options
layer: n/a
stage: results
tags: [results, integrated-result-tool, gui, chart]
related: [analysis-views, integrated-result-tool, data-navigation-views, results, shmoo-tool, raw-data-views]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.05_Setting_chart_display_options.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Setting chart display options

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**本页讲的是 Integrated Result Tool 里「结果图的显示选项」分散在哪几个地方、各自怎么改。**

原文第一句就是全部范围：

> 「The display options of result charts in the Integrated Result Tool can be customized in
> **various ways**, using **shortcut menu command**, **property dialog options**, and
> **preference settings**.」

**三个入口，不是三种说法**——同一个「看起来像一类」的设置，改它的地方可能完全不同。
**找错入口是这一页要防的主要错误**，所以先把入口表列出来。

### 入口总表

| 想改什么 | 入口 | 具体位置 |
|---|---|---|
| 标题、轴标签 | **属性对话框** | 图上工具栏 `Properties` 按钮，或右键 → `Properties` → **`Titles`** 页 |
| 轴起止值 | **见 `Zooming the display of charts`** | 本页没读那篇，只给了指针 |
| 值类别（显示几个 / shmoo 里怎么定义） | **见 `Configuring value categories in result graphs`** | 本页没读那篇 |
| 图例显示 / 隐藏 | **Preferences** | `Window > Preferences` → `Advantest 93000 > Result Tool` → 选图类型 → `Show Legend` 勾/不勾 |
| 图例在右还是在图下方 | **工具栏按钮** | 两个按钮对切（见下） |
| 整图旋转 90° | **分图类型，三种不同做法** | 见下表 |
| 直方图上的均值 / 2σ / 3σ 线 | **图属性 ＋ 快捷菜单** | 同一件事两个入口 |
| box chart 的触须（whiskers）区间 | **图属性 `Whiskers` 页 或 右键菜单** | 同一件事两个入口 |
| shmoo 图里显不显示每格的值 | **shmoo preferences** | **这一项影响所有 shmoo 图**，不是单张 |
| 参数 wafer map 上标出某个 site 的所有 die | **属性 `Marks` 页 或 右键 `Mark site`** | 同一件事两个入口 |
| scan view 逐实例看 / 按 pin 或实例过滤 | **快捷菜单 / 属性 `Filter` 页** | 两条不同的功能，且**有依赖** |

**读这张表要抓的三件事：**

① 标题标签在**属性对话框**，图例在 **Preferences**——两个都是「图上看得见的东西」，
入口却在两个不同的窗口；
② 有几项**同一件事有两个入口**（属性页 ＋ 右键菜单），任选一个；
③ **「轴起止值」和「值类别」本页只给指针、没展开**——它们各自有一篇专文。

### 旋转 90°：三种图三种做法

| 图类型 | 做法 |
|---|---|
| **histogram** / **FFC Pareto chart** | 打开**该图类型的偏好页** → 选 **`Bar`** |
| **parametric wafer map** / **bin wafer map** | 打开该图类型的偏好页 → 勾 **`Exchange axes`** |
| **scatter chart** | **在图上右键 → `Swap Axes`**（**只有它不用偏好页**） |

> **偏好页的开法**原文不重复写，只说
> `see steps 1 to 3 of Displaying or hiding the legend, above`
> ——即 `Window > Preferences` → `Advantest 93000 > Result Tool` → 点图类型那一条。

### ⚠️ 定制会丢：两条重置规则

这是本页最该记住的坑，原文在标题标签那一节里用一整段讲：

> 「if the `Link` button in the toolbar is activated, **changing the selection in the data navigation
> view will reset the titles and labels to their defaults**, except when you select another grouped
> subitem from the same main item. **Changing the selection back also restores** the titles and
> labels to your customized versions. **When you unload a data log or quit SmarTest, the customized
> titles and labels are lost.**」

拆成四条：

| 情形 | 定制还在不在 |
|---|---|
| 工具栏 **`Link` 按钮激活**，你在 data navigation view 里**改选中**（换到别的主项） | **重置成默认** |
| 换的是**同一个主项下的另一个 grouped subitem** | **不重置**（原文把这个单独列成例外） |
| **选回原来那一项** | **定制恢复**（只是被顶掉，没丢） |
| **卸载数据日志 / 退出 SmarTest** | **真的丢了** |

**注意 `Link` 按钮**：这个按钮在 [[analysis-views]] 里是「**解冻**、让视图跟着选中走」的那个。
**它同时是这里的重置开关**——原文没有把这两件事联系起来讲，是本页并列出来的
（**（推断）**：两者是同一个按钮的同一个行为，依据是原文两处都把它写成「图跟着数据导航的选中走」）。

### 图例位置的两个按钮

图例默认在图的**右侧**。两个按钮对切：

- 图例在**右边**时，点「切到下方」按钮 → 图例移到图**下方**
- 图例在**下方**时，点「切到右侧」按钮 → 图例回到图**右边**

原文这两个按钮是两张图（`140972.png` / `140973.png`），
**本页没看这两张图，所以只知道功能、不知道按钮长什么样**。

### 几个「只对某一种图有效」的选项

| 图类型 | 选项 | 说明 |
|---|---|---|
| **histogram** | 均值线 / 2σ 线 / 3σ 线的显示与隐藏 | 图属性和快捷菜单里都有 |
| **box chart** | 触须（whiskers）代表哪个区间 | 图属性 `Whiskers` 页或右键菜单，**值自己填** |
| **shmoo plot** | 每格的值显不显示 | **在 shmoo preferences 里，对所有 shmoo 图生效** |
| **parametric wafer map** | 标出属于某个 site 的全部 die | 属性 `Marks` 页，或右键 `Mark site` |
| **scan view** | ① 按实例分组看 ② 只看某个 pin 或实例 | ① 右键 `Group by Instance`；② 属性 `Filter` 页 |

> **scan view 那两条有依赖**：原文写 `Filtering by instance has only an effect if
> Group by Instance is active`——即**②要①开着才有用**。

### 一句话的边界

> 「The chart display is updated according to your settings.」
> ——**改完即时生效，没有「应用」按钮。**

## 典型用法

**1. 前置**（原文 `## Before you begin` 只一条）：
**先有图**——从 data navigation view 里想要的行 **create a result chart**（**那篇本页没读**）。

**2. 改标题 / 轴标签**（原文唯一给了完整步骤的一段）：
图上点 `Properties`（或右键 `Properties`）→ **`Titles` 页** → 改 title / subtitle / 两个轴 → `OK`。

- **默认值是有的**：原文 `All charts are generated with default titles and axis labels.`
- **但标签不一定齐**：`In general, labels are available for a title, a subtitle, and both axes.
  However, some charts may have additional or fewer titles.`
  → **具体有哪几个，要看那张图类型的属性页**（原文指向 `chart type` 那篇，**本页没读**）。

**3. 改图例**：`Window > Preferences` → `Advantest 93000 > Result Tool` → 点图类型 →
勾/去勾 `Show Legend` → `OK`。
**注意原文的一句限制**：`not all chart types may have a preference page.`
→ **有的图根本没有偏好页，那条设置就无从改起。**

**4. 什么时候用哪个入口**（本页自己归纳）：

- **要改的是「这一张图上显示成什么样」** → 属性对话框 / 右键菜单
- **要改的是「这一类图以后都这样」**（图例开关）→ Preferences
- **要改的是「所有 shmoo 图」** → shmoo preferences

**5. 顺序上的提醒**：**先改定制、最后再动数据导航的选中**——
按上面那条重置规则，**开着 `Link` 时改选中会把定制顶掉**。

## 和谁有关

- [[results]] — 本页 `stage: results` 的理由：**它是结果数据的展示侧**
- [[analysis-views]] — **上游**：那页讲「怎么把图**做出来**」（要选几行、选哪种视图），
  本页讲「做出来之后**怎么调**」。**原文 `Before you begin` 指的正是那一页**
- [[integrated-result-tool]] — **容器**：这些图和这些设置都跑在它里面
- [[data-navigation-views]] — **重置规则的触发点**：改它的选中会顶掉本页的定制
- [[test-summary-tab]] / [[wafer-summary-tab]] — 选行的两个场所（`wafer-summary-tab` **未建**）
- [[shmoo-tool]] — shmoo 的生成侧；**本页的 shmoo 偏好设置落在它画出来的图上**
- [[raw-data-views]] — 同一 `results` 阶段下的另一种视图形态
- `Zooming the display of charts` / `Configuring value categories in result graphs`（**均未建**）—
  **本页明确让出去的两篇专文**：轴起止值、值类别
- `Trend chart view` / `Histogram view` / `Box chart view` / `Scatter chart view` /
  `FFC Pareto chart view` / `Parametric wafer map view` / `Bin wafer map view` / `Scan view` /
  `Shmoo view`（**均未建**）— **每种图的属性页 / 偏好页长什么样**；
  **本页只有「哪个选项在哪张图上有」，没有它们各自的功能**

## 版本

- **Introduced in SmarTest 7.2.0**
- **SmarTest 7.2.1**：`The location of the legend can now be switched.`
  ——**图例位置对切是 7.2.1 才有的**
- **SmarTest 7.3.2**：`Added grouping by instance in scan views.`
  ——**scan view 的 `Group by Instance` 是 7.3.2 才有的**

> **这三条和正文对得上**：正文里「图例位置两个按钮」对应 7.2.1 那条，
> 「scan view 按实例分组」对应 7.3.2 那条。**7.2.0 引进时这两项都还没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.05_Setting_chart_display_options.md`

**本页没做的**：

- **原文 `Related information` 里的四篇一篇没读**：`Zooming the display of charts`、
  `Configuring value categories in result graphs`、`Displaying test results in analysis views`、
  `Analysis views`。**所以「轴起止值怎么设」「值类别到底是什么」本页一个字都没有**，
  只有「这两件事各有一篇」这个指针。
- **`## Procedures` 下面有整整两节是纯指针**（`Setting up the axes` 和
  `Specifying the value categories`）——**原文自己就没在这篇里展开**，本页照实转述。
- **图一张没看**：`136931.png`（Properties 按钮）、`140972.png` / `140973.png`
  （两个图例位置按钮）。**本页没有任何来自图的结论**。
- **各图类型的属性页 / 偏好页一篇没读**——所以：
  **标题标签到底有几个、`Whiskers` 里能填什么、`Marks` 页长什么样、`Filter` 页怎么填，
  本页都不知道。**
- **原文没写 `Preferences` 里 `Result Tool` 那一级下面的完整页面清单**，
  只说了「点你要配的那张图类型」和「不是每张图都有偏好页」。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`scan view` 那一段有一处括号没闭合**——
> `(Filtering by instance has only an effect if Group by Instance is active.`
> **左括号有、右括号没有。**
> ② **小节标题是 `## Procedures`（复数）**，而本语料其它同型文档用的是
> `## Procedure`（单数）。
> ③ **`## About this task` 一节只有一句指路**
> （`For information on zooming chart displays to set the detail view as desired, see …`），
> **不是对任务的描述**——和这个标题在别处的用法不一样。

`verified: doc-only`
