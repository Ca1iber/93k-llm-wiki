---
type: object
title: Data navigation views
layer: gui
stage: results
tags: [results, integrated-result-tool, gui]
related: [results, integrated-result-tool, test-summary-tab, wafer-summary-tab, device-summary-tab, hardware-bin-summary-tab, software-bin-summary-tab, table-filter]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Data navigation views

> **一句话**：Integrated Result Tool 的 **Result 视角**里的结果总览视图。**每打开一个
> 数据存储（data store）就有一个**，用表格显示该存储的自动汇总与统计。

入度 **45**（`extract/hubs-dedup.csv`，仅 inline 边、两端已去重）——**stage 之外、入度最高的
未归属对象**，所以它有这一页。它不属于九段流程里的任何一段，是「跑完之后看结果」时用的
工具；`stage` 字段记 `results` 是**它服务于哪个阶段**，不是它被哪个阶段拥有。

## 是什么

- **载体**：Result 视角的 **data navigation 区**。原文：*"The data navigation section of the
  Result perspective contains one data navigation view for each opened data store."*
- **一个视图 = 一个打开的数据存储**。视图里最多五个 tab，每个 tab 一种汇总口径。
- **静态 vs 动态**（原文）：数据日志**文件**的视图是静态的（内容不变）；**system data log
  stream** 是动态的——正在跑测试时产生的新日志条目会立刻进到已打开的日志里，汇总和显示
  随之更新。

## 结构：五个 tab

原文 *"contains up to five tabs"*，其中两个对 **correlation data store 不存在**：

| tab | 对 correlation data store | 备注 |
|---|---|---|
| [[test-summary-tab]] | 有 | 工具栏的 Refresh / Pause / Resume / Clear / Save and Clear **只对它可用** |
| [[wafer-summary-tab]] | **没有** | |
| [[device-summary-tab]] | **没有** | |
| [[hardware-bin-summary-tab]] | 有 | 分组（group by site）可从快捷菜单用，**工具栏按钮置灰** |
| [[software-bin-summary-tab]] | 有 | 同上 |

另有 [[table-filter]]（表格过滤器）挂在这一族下。

## 工具栏

挂在 **SmarTest 主工具栏**上（不是独立工具条）。按钮：

- **Refresh** — 暂停状态下取最新日志数据更新显示，**但不会重新打开自动更新**（那是 Resume）
- **Pause** / **Resume** — 暂停 / 恢复 system data log stream 的更新，互斥切换
- **Clear** — 清空 Integrated Result Tool 里的 stream 显示，并清 system event stream
- **Save and Clear** — 先弹标准保存对话框把 system event stream 存成 **EDL 文件**，然后清空
- **Group by wafer / site / pin** — 把一行汇总拆成多行（按 wafer / site / pin 各一行）

**可用性约束（文档事实，逐字）**：前五个按钮 *"available only if the frontmost tab is the
test summary tab of the system data log stream"*；*"If the frontmost tab is not a test summary
tab, the buttons are disabled."* —— **即：最前面的 tab 不是（动态流的）test summary tab 时，
分组按钮也一起置灰。** 这是页面级互斥，不是单个按钮的毛病。

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,468 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.05_Software_bin_summary_tab.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Software bin summary tab）

Depending on your preference settings, the bin summary could look like this:

 !`Data log summary view_SW Bin Summary`（raw: `../../../../agent-html/136421.png`）

### Syntax（取自子主题 Table filter）

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

## 和谁有关

**上游（谁把它打开）**

- [[integrated-result-tool]] —— 它是这个工具的组成部分，原文把它列为 Result 视角的
  *"Data navigation views that display individual opened logs"*
- Data Log Explorer —— 双击 / 快捷菜单把已加载的日志开成一个 data navigation view；
  开一个日志会**自动**同时打开相应视图
- 数据日志的加载/卸载 —— 卸载日志时，**为它打开的 data navigation view 会被关掉**

**下游（谁跟着它动）**

- **analysis views 全部**（Trend / Histogram / Probability / Box / Scatter / FFC Pareto /
  Shmoo / Parametric wafer map / Scan / Bin wafer map）：每一篇的说明里都有一条
  *"Link: Links the display in the view to the selected row in the data navigation view."*
  ——**分析视图显示的是「最前面那个 data navigation view 里当前选中的行」**，选中变了显示就变。
- Raw data views / Protocol Monitor view：同一条 Link 机制，显示的是选中行背后的原始条目。
- `Detail data views`：汇总行的底层数据在 detail data view 里展开。
  （**不链**——它入度低、不在建页 backlog 里，链了就是造一个永远不会建的悬空目标。
  对象页的链接规则见 `schema.md` §2.2。）

**横向（谁改它的样子）**

- **集成结果工具的偏好设置**：`Enable autofit column width of table`；`Synchronize selections
  in navigation views`（勾上后**在一个视图里选中某个 test，其它所有打开的视图也一起选中**）
- Alerts / Annotations 偏好设置：决定哪些单元格高亮、哪些行被标注（例如「有被排除行的行」）

> 上面每一条都来自 `edges.jsonl` 里带原句的边，不是推断出来的关系。
> **唯一一条推断**：「工具栏按钮置灰 = 页面级互斥」是从两句原文（按钮可用性 + 按钮置灰）
> 合起来读的，文档没有把这句话直接写出来。

## 版本

原文 `Functional changes` 段：

- Introduced in **SmarTest 7.2.0**
- **SmarTest 7.2.2**：新增 "Refresh"、"Clear"、"Save and Clear" 三个按钮
- **SmarTest 7.2.2**：新增 Save and Clear 快捷菜单命令

本 wiki 面向 **7.10.3**，以上功能均在。

## 出处

- 定义文档：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.md`
  （TDC `136308.htm`，5,757 字节）
- 入边 45 篇的来源与原句：`extract/pack/01-data-navigation-views.md`
- ⚠️ **语法节的来历要更正**（2026-09-18）。本页初版这一节写的是
  **「无。这是 GUI 视图，不是命令、不是 API，没有参数表」**——
  **那句话不是从文档读出来的，是从「抽取器抽不到」推出来的。**
  按 `schema.md` §4 分工，抽取器抽不到就写「无」；**但抽取器当时有个盲区**：
  `## Examples` / `## Syntax` 底下的 `### 子段` 会被整段丢掉（详见
  `extract/objpack.py` 里 `verbatim_sections` 的注释，全语料 **256 篇 / +427,979 字符**
  受此影响）。修好之后本节立刻收到两段真货：
  **`Table filter` 的筛选语法**（纯文本 / 正则 / 数字 / `~` 范围 / 逗号多值「or」，
  原文 `Syntax` 段）+ **软件 bin 汇总 tab 的一句说明**。
  **「我没有」和「文档没有」是两件事**——这一页是拿前者当后者写的。
- 本页 `verified: doc-only` —— **只在 TDC 文档里确认存在**，未在任何真实机台上点过。
