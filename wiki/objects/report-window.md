---
type: object
title: Report window
layer: gui
stage: results
tags: [gui, report-window, results, logging, datalog, x-window]
related: [results, model-file, testflow, test-suite, run, data-logging-profiles]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Report window

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,485 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.md>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.13.03_Configuring_the_messages_printed_in_the_Report_Window.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples（取自子主题 Configuring the messages printed in the Report Window）

### Printing messages for passed and failed sites in the Report Window

This example shows how you can configure the .testflow.ReportUiOutput.user_def file to print messages in the Report Window for all passed and failed sites after a testflow is executed:

```
<passed>Site: %site -> Bin: %bin -> PASS (Cool)
<failed>Site: %site -> Bin: %bin -> FAIL (Bad)
#<text> This is an example for a commented line (using "#" at the beginning)
```

The messages that are printed in the Report Window are as in the following figure:

!`Printing messages for passed and failed sites in the Report Window`（raw: `../../../../agent-html/345529.png`）

### Printing messages for failed sites only in the Report Window

This example shows how you can configure the .testflow.ReportUiOutput.user_def so that only messages for the failed sites are printed in the Report Window:

```
<failed>Site : %site -> Bin: %bin -> FAIL (Bad)
```

!`Printing messages for failed sites only in the Report Window`（raw: `../../../../agent-html/345530.png`）

### Printing messages in the Report Window for the failed sites after a test suite is executed

This example shows how you can configure your .testflow.ReportUiOutput.user_def file to print a message in the Report Window for the failed sites after a test suite is executed:

```
<failed>TestSuite: %testSuiteName -> Site: %site -> FAIL
```

!`Printing messages in the Report Window for failed sites only after a test suite is executed`（raw: `../../../../agent-html/345531.png`）

<!-- 语法节 end -->

## 是什么

**report window 是 SmarTest 的「常驻播报台」。** 原文第一段：

> The report window provides constant and immediate feedback about what is happening on the system. Two lines at the top of this window constantly monitor hardware status and system performance.

**两个词是关键：`constant and immediate` 和 `constantly`。** 它不是「你需要的时候去打开的窗口」，
**它是常驻的、实时刷新的**。下面那句把生命周期说死了：

> The report window opens as soon as you start the software, and stays open as long as you use SmarTest. If the software shuts down unexpectedly it writes the logged data to /tmp/ReportWindow.dump.

| 事件 | report window 的行为 |
|---|---|
| 启动软件 | **自己打开**（不是手动开） |
| 用 SmarTest 期间 | **一直开着** |
| 软件**意外退出** | **把已记录的数据写进 `/tmp/ReportWindow.dump`** |

**第三条是它唯一的「事后」能力**：崩了之后现场在这份 dump 里。
（文档只写了写到哪里，**怎么读它、它是什么格式，语料未写**。）

**顶部那两行是固定的**（原句 `Two lines at the top of this window`），监控两件事：
**hardware status / system performance**。
**这两行显示什么字段、能不能配，文档一个字没写。**

### 四个可配置的面（原文的四个小节）

| 小节 | 能配什么 | 怎么配 |
|---|---|---|
| **X window** | 窗口的**大小与位置** | 改 `/opt/hp93000/soc/pws/data/.Xdefaults` 里 report window 的 `Geometry` 资源 |
| **X window** | 窗口保留的**行数** | 改同一处的 `XReport.purgeLines` 与 `XReport.maxLines` |
| **logging panes** | **数据日志播报段**：值记录开关、bin 统计显示、清 bin | 用 **`Datalog` 菜单** |
| **printed messages** | **testflow / test suite / run configuration 手工执行完之后打印什么** | 配上文语法节里的 `.testflow.ReportUiOutput.user_def`（**那部分来自子主题，本页没读**） |

**行数那条给了默认值**（逐字）：

> The number of lines in the report window is always kept between 5000 and 10000. Should you wish to change these defaults, you must modify the XReport.purgeLines and XReport.maxLines resources in the above files.

**5000–10000 是「保留多少行」这个意义上的默认区间。**
**`purgeLines` 与 `maxLines` 分别管什么，文档没有解释**——从名字看是「清到多少行」与「最多留多少行」
（**推断，依据只是资源名本身**；**文档没写这两个资源各自的语义**）。

**改完 X 资源还有一步，原文单独一句：**

> If you have modified any X resources, you must provide the new values to your system controller.

**「provide the new values to your system controller」——把文件改了不算完。**

### logging panes：数据日志播报段

> When you perform characterization tests, the data log report section is where the measurement values are reported.

> The Datalog menu allows you to turn value logging on or off. This will override similar settings that have already been made. You can also display the bin statistics and clear the bins from the Datalog menu.

**两句要留意：**

- **`This will override similar settings that have already been made.`**——
  `Datalog` 菜单里的开关**会覆盖别处已经做过的同类设置**。
  **换句话说，在它面前别的设置不作数。**（**文档没有说「别处」具体指哪里**。）
- **`Datalog` 菜单管三件事**：值记录开关、显示 bin 统计、清 bin。

### 可配置的打印消息

> You can configure the messages that are printed on the Report Window after a testflow, test suite, or run configuration is manually executed.

**`manually executed` 这个词把适用范围限住了**：文档说的是**手工执行**之后。
**自动跑（比如批处理 / 生产外壳里跑）之后会不会打印，本文档没有写**——
**本页不替它推广。**

**具体怎么写**见上面「语法 / 参数」节那三个例子
（`<passed>` / `<failed>` / `<text>` 三种标签 + `%site` / `%bin` / `%testSuiteName` 占位符，
文件是 `.testflow.ReportUiOutput.user_def`）。**那些例子逐字来自子主题 `01.01.13.03`，
本页没读那篇**——所以**标签与占位符的完整清单、这个文件放在哪、什么时候被重新读，本页一个字都没有。**

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
按用途分四条路走（每条都标出依据）：

1. **只是想看**——**不用做任何事**。原句：`The report window opens as soon as you start the software`。
   顶部两行看 hardware status / system performance。
2. **调窗口本身**（大小、位置、行数）——改 `/opt/hp93000/soc/pws/data/.Xdefaults` 里的
   `Geometry` / `XReport.purgeLines` / `XReport.maxLines`，
   **再把新值 `provide` 给 system controller**（原文单独一句，**这一步别漏**）。
3. **调内容**——
   - **数据日志那一段**：用 **`Datalog` 菜单**（开/关值记录、显示 bin 统计、清 bin）。
   - **执行完打印什么**：配 `.testflow.ReportUiOutput.user_def`（**细节本页没读，见「出处」**）。
4. **出事后**——软件意外退出时，去 `/tmp/ReportWindow.dump` 拿已记录的数据。

**下面两件事本页文档没写，列出来免得被当成「文档说了」：**

- **窗口里内容按什么顺序出现、有没有分页 / 过滤**——语料未写（除了「顶部两行固定」这一条）。
- **`/tmp/ReportWindow.dump` 怎么打开**——语料未写。

## 和谁有关

- [[results]] — **`stage: results` 的落点**。report window 是结果回给人看的那一面，
  这个字段说的是「读者该去哪一段里找它」（§6）。
- [[model-file]] — **上电时最紧的一条关系**。模型文件那篇写的是：SmarTest 上线时读 model file，
  并把探测到的测试系统硬件**报在 report window 的 `MAXIMUM POSSIBLE CONFIGURATION` 表里**；
  离线则显示 model file 请求的配置。**这条关系写在 model-file 的文档里，不在本页的文档里**——
  本页文档只在 `#### Subtopics` 里有一个 `Printing the hardware configuration and license checkout information`。
- [[testflow]] / [[test-suite]] / [[run]] — **打印消息的触发点**。
  本页原句是 `after a testflow, test suite, or run configuration is manually executed`；
  **这三个词指的是「执行这件事」，不是那三页本身**——放在这里是为了说明本页和它们相邻。
- [[data-logging-profiles]] — **同一功能域的相邻页**。本页讲到「data log report section 里报测量值」，
  而 data logging 的 profile 配置是它的上游。**本页的文档没有指向那一页**，
  这条关系是同一功能域上的邻接，**不是文档给出的引用**。
- `Console view` / `Console view: System console` / `Console view: Data log console`（均未建）—
  `## Related information` 段的前三条。**它们是另一套「看输出」的窗口**。
  **本页文档没有解释两者的分工**——「report window 是常驻概览、console 是分门别类的输出」
  **是本页的推断**，依据只有「`Related information` 把它们列在一起」这一件事。
- `Collecting log files if SmarTest crashed`（未建）— `## Related information` 的第四条。
  **它和本页 `/tmp/ReportWindow.dump` 那句很可能是同一件事的两半**
  （**推断**：两处都讲崩溃后取现场）。**但那篇本页没读。**
- `Loading Progress Meter` / `Printing the hardware configuration and license checkout information`（均未建）—
  本页 `#### Subtopics` 里的两个子主题，**本页都没读**。

## 版本

本文档有 `## Functional changes` 段，**只有一条**：

- `Introduced before SmarTest 6.3.2`

**按哨兵值读**（§11.2 ②）：意思是「**在本文档集覆盖范围开始之前就已经有了**」，
**不是「SmarTest 6.3.2 新增了 report window」**。

> **和 [[model-file]] 对一下会看到一个现象**：那边同一段里有一条
> `SmarTest 6.5.4: Report window lists the referenced model file.`——
> **report window 的一处功能变更记在 model file 的版本段里，不在本页。**
> 两篇的 `## Functional changes` 不是同一批条目。**本页照实记这一点，不把那条搬进来当自己的版本条目**（§11）。

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.md`

**本页没做的：**

- **三个子主题一篇都没读**（它们只出现在原文的 `#### Subtopics` 列表里）：
  `Loading Progress Meter`（`01.01.13.01`）、
  `Printing the hardware configuration and license checkout information`（`01.01.13.02`）、
  `Configuring the messages printed in the Report Window`（`01.01.13.03`）。
  **⚠️ 第三条尤其要紧**：本页「语法 / 参数」节那三个例子
  （`.testflow.ReportUiOutput.user_def` 的 `<passed>` / `<failed>` / `<text>` 写法）
  **逐字来自 `01.01.13.03`，本页没有读过那篇**——所以
  **标签的完整清单、占位符的完整清单、这个文件放在哪、什么时候被重新读，本页一个字都没有。**
- **一张图没看**（`raw/21571.png`，就是 `![Report window]` 那一张）。
  **所以 report window 长什么样、顶部那两行显示哪些字段、`Datalog` 菜单里到底有哪些项，
  本页一个都不知道——只知道名字。**
- **`Console view` 三篇没读**（`## Related information` 前三条），
  **`Collecting log files if SmarTest crashed` 没读**（第四条）。
- **`/tmp/ReportWindow.dump` 的格式与读法：语料未写。**
- **`XReport.purgeLines` 与 `XReport.maxLines` 各自的语义：语料未写**——
  本页只写了「是这两个资源」，**分别管什么是本页的推断，已标注**。
- **`.Xdefaults` 里除了 `Geometry` 还能改什么：本页的文档只提了这一个资源名。**
- **顶部两行显示什么字段：语料未写。**

> ⚠️ **语料瑕疵，照实记下，一处都没替它改**：
> ① **同一件事在一篇里有两种写法（`on` / `in`）。**
> 小节的标题是 `## Configuring the messages printed on the Report Window`（**`on`**），
> 而同一节正文里指向的子主题、`#### Subtopics` 里那一行、
> `## Related information` 里那一行，写的**都是 `in`**：
> `Configuring the messages printed in the Report Window`。
> **同一篇里 `in` 写了三处，`on` 只出现在小节标题上。**
> ② **`in the above files` 用的是复数，但上文只给了一个文件**——
> `/opt/hp93000/soc/pws/data/.Xdefaults`。原文如此，**本页不替它改成单数**。

`verified: doc-only`——**本页没有在任何真实 SmarTest 上看过 report window**
（§11：文档里有 ≠ 这台机器上能看到）。
