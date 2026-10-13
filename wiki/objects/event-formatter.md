---
type: object
title: Event Formatter
layer: gui
stage: results
tags: [event-formatter, report-formatter, interactive-debugging, report-window, shmoo-output, data-logging, results]
related: [report-window, smartest-data-formatter, edl-file, edf, data-retrieval-library, shmoo-tool, smartest-6.3.2]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# Event Formatter

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,051 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.md>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.02.04_Shmoo_output_of_the_Event_Formatter.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Shmoo output of the Event Formatter）

A shmoo data log shown with Event Formatter is similar to the one below.

```
======== Started Testsuite Shmoo_2D ============================================

******** Started Site : 1 ******************************************************
Equation Set 512; Spec Set 256; Timing Set 256
Equation Set 512; Spec Set 512; Level Set 512
Startlabel: spec_search

-------- Test Name:  714 parameters[1] -----------------------------------------
-------- Shmoo -----------------------------------------------------------------
Title:  714 parameters
Test Mode:  pass/fail,cycle error count
Result Pins:  @
Result Resolution:  1.000000
Description:

........ Shmoo Axis Information ................................................
X-Axis
TotalSteps: 10
LinearSteps: 1
Test Range:   [0.000000 ...  1.000000]
Scale: Linear
=> Step Ratio: 0.100000
PrimaryValue: 0.500000
Parameter: Spec Variable
Spec: LEV.2.VIL[V]
SetupPins: I/O0,I/O1
Description:

Y-Axis
TotalSteps: 10
LinearSteps: 1
Test Range:   [0.000000 ...  10.000000]
Scale: Linear
=> Step Ratio: 1.000000
PrimaryValue: 5.000000
Parameter: Spec Variable
Spec: TIM.2.tpd_CP_IOx[ns]
SetupPins: @
Description:

........ Shmoo Matrix ..........................................................
' '   = point not calculated
'.'   = point passed
'*'   = point failed
 'E'   = point returned an error

Shmoo Pin Number      : 1
Shmoo TestMode Number : 2
Shmoo Pin Names       : @;
Shmoo Test Modes      : pass/fail;cycle error count;

Number Of Cells       : 121

Pin: @, TestMode : pass/fail

          00000000001
          ...........
          01234567890
          00000000000
          00000000000
         +---------->
    0.000|...........
    1.000|...........
    2.000|...........
    3.000|...........
    4.000|...........
    5.000|...........
    6.000|...........
    7.000|...........
    8.000|...........
    9.000|...........
   10.000v...........

Pin: @, TestMode : cycle error count

             0   0   0   0   0   0   0   0   0   0   1
             .   .   .   .   .   .   .   .   .   .   .
             0   1   2   3   4   5   6   7   8   9   0
             0   0   0   0   0   0   0   0   0   0   0
             0   0   0   0   0   0   0   0   0   0   0
         +------------------------------------------->
    0.000|   0   0   0   0   0   0   0   0   0   0   0
    1.000|   0   0   0   0   0   0   0   0   0   0   0
    2.000|   0   0   0   0   0   0   0   0   0   0   0
    3.000|   0   0   0   0   0   0   0   0   0   0   0
    4.000|   0   0   0   0   0   0   0   0   0   0   0
    5.000|   0   0   0   0   0   0   0   0   0   0   0
    6.000|   0   0   0   0   0   0   0   0   0   0   0
    7.000|   0   0   0   0   0   0   0   0   0   0   0
    8.000|   0   0   0   0   0   0   0   0   0   0   0
    9.000|   0   0   0   0   0   0   0   0   0   0   0
   10.000v   0   0   0   0   0   0   0   0   0   0   0

Executed Testmethod ac_tml.AcTest.Shmoo on Site 1: PASSED
******** Ended   Site : 1 ******************************************************

******** Started Site : 2 ******************************************************
Equation Set 512; Spec Set 256; Timing Set 256
Equation Set 512; Spec Set 512; Level Set 512
Startlabel: spec_search

-------- Test Name:  714 parameters[1] -----------------------------------------
-------- Shmoo -----------------------------------------------------------------
Title:  714 parameters
Test Mode:  pass/fail,cycle error count
Result Pins:  @
Result Resolution:  1.000000
Description:

........ Shmoo Axis Information ................................................
X-Axis
TotalSteps: 10
LinearSteps: 1
Test Range:   [0.000000 ...  1.000000]
Scale: Linear
=> Step Ratio: 0.100000
PrimaryValue: 0.500000
Parameter: Spec Variable
Spec: LEV.2.VIL[V]
SetupPins: I/O0,I/O1
Description:

Y-Axis
TotalSteps: 10
LinearSteps: 1
Test Range:   [0.000000 ...  10.000000]
Scale: Linear
=> Step Ratio: 1.000000
PrimaryValue: 5.000000
Parameter: Spec Variable
Spec: TIM.2.tpd_CP_IOx[ns]
SetupPins: @
Description:

........ Shmoo Matrix ..........................................................
' '   = point not calculated
'.'   = point passed
'*'   = point failed
 'E'   = point returned an error

Shmoo Pin Number      : 1
Shmoo TestMode Number : 2
Shmoo Pin Names       : @;
Shmoo Test Modes      : pass/fail;cycle error count;

Number Of Cells       : 121

Pin: @, TestMode : pass/fail

          00000000001
          ...........
          01234567890
          00000000000
          00000000000
         +---------->
    0.000|...........
    1.000|...........
    2.000|...........
    3.000|...........
    4.000|...........
    5.000|...........
    6.000|...........
    7.000|...........
    8.000|...........
    9.000|...........
   10.000v...........

Pin: @, TestMode : cycle error count

             0   0   0   0   0   0   0   0   0   0   1
             .   .   .   .   .   .   .   .   .   .   .
             0   1   2   3   4   5   6   7   8   9   0
             0   0   0   0   0   0   0   0   0   0   0
             0   0   0   0   0   0   0   0   0   0   0
         +------------------------------------------->
    0.000|   0   0   0   0   0   0   0   0   0   0   0
    1.000|   0   0   0   0   0   0   0   0   0   0   0
    2.000|   0   0   0   0   0   0   0   0   0   0   0
    3.000|   0   0   0   0   0   0   0   0   0   0   0
    4.000|   0   0   0   0   0   0   0   0   0   0   0
    5.000|   0   0   0   0   0   0   0   0   0   0   0
    6.000|   0   0   0   0   0   0   0   0   0   0   0
    7.000|   0   0   0   0   0   0   0   0   0   0   0
    8.000|   0   0   0   0   0   0   0   0   0   0   0
    9.000|   0   0   0   0   0   0   0   0   0   0   0
   10.000v   0   0   0   0   0   0   0   0   0   0   0

Shmoo picture has been saved in: /home/Devices/74HC299/shmoo/shmooPNG/shmoo_2D
Executed Testmethod ac_tml.AcTest.Shmoo on Site 2: PASSED
******** Ended   Site : 2 ******************************************************

======== Ended Testsuite Shmoo_2D ==============================================
```

<!-- 语法节 end -->

## 是什么

**本篇是一个章的入口页，正文只有两段话加一串目录。定义句在第一段，逐字：**

> 「The Event Formatter is a report generating tool that is used for interactive debugging. With
> its own dialog window for customizing the format and scope of the data output, the Event
> Formatter is a powerful data logging tool.」

**拆成四件：**

| 原句（**逐字**） | 含义 |
|---|---|
| `a report generating tool` | **它是一个「产生报告」的工具**——**不是格式、不是文件、不是库** |
| `used for interactive debugging` | **用途是交互式调试** |
| `With its own dialog window for customizing the format and scope of the data output` | **它自带一个对话框**，用来定制输出的**格式（format）**与**范围（scope）** |
| `a powerful data logging tool` | **原文把它归为「数据记录工具」这一族** |

**第三件是本页的关键**：**它有两个可调的东西——`format` 与 `scope`**——
**即「输出长什么样」与「输出哪些数据」是两件独立的事，各由一个对话框控制。**

**第二件划出了它的地盘**：**`for interactive debugging`（交互式调试）**。
**本篇没有一句话提到 STDF，也没有提到生产数据记录**——
**本页只能说：本篇给它挂的用途是调试，别的没说**（见 `## 出处` ②）。

### 它和 report window 的关系：**它给 report window 加菜单**

**本篇正文第 2 段的第 2 条 bullet 逐字：**

> 「- How to use the new menus of the report window that are added by the Event Formatter」

**即：Event Formatter 会往 `report window` 上加新菜单**——
**这句话同时说了两件事：它依附于 report window，而它给 report window 添东西。**
**它自己还另有一个专门的控制窗口**（子主题 `Report Dialog window`，见下）。

### 本篇正文说本章覆盖五件事（**逐字**）

> 「This chapter describes:」
>
> 「- How to activate the Event Formatter」
> 「- How to use the new menus of the report window that are added by the Event Formatter」
> 「- How to use the Report Dialog window to control the output of the Event Formatter」
> 「- How result data is presented in that output」
> 「- How to customize the Event Formatter to your needs」

**五条里三条是 `How to …`（操作）、一条是 `How … is presented`（输出长相）、
一条是 `How to customize`（定制）。**

**本篇正文最后一段（第 3 段）逐字：**

> 「The final sections of this chapter provide background information on how the Event Formatter
> works in principle, and highlight important considerations when writing your own event-based
> report formatter.」

**两个出口**：**原理背景**，以及
**「写你自己的 event-based report formatter 时的注意事项」。**
**注意 `your own event-based report formatter` 这个说法**——
**原文把 `report formatter` 当成一类**可以自己写**的东西，Event Formatter 只是其中之一**
（**这与子主题里 `Running report formatters as standalone tools` 用的是复数 `formatters` 一致**）。

### 14 个子主题：本篇信息量最大的部分

**本篇正文只有 2 段 + 5 条 bullet，而 `#### Subtopics` 底下有 14 条链接。**
**这 14 个名字就是本页能给出的、关于这个工具覆盖面的全部信息**（**逐字**）：

| # | 子主题名（**逐字**） | 链到的文件 |
|---|---|---|
| 1 | `Activating the Event Formatter` | `02.10.02.01_Activating_the_Event_Formatter.md` |
| 2 | `Report window menus` | `02.10.02.02_Report_window_menus.md` |
| 3 | `Standard output of the Event Formatter` | `02.10.02.03_Standard_output_of_the_Event_Formatter.md` |
| 4 | `Shmoo output of the Event Formatter` | `02.10.02.04_Shmoo_output_of_the_Event_Formatter.md` |
| 5 | `Fine result granularity` | `02.10.02.05_Fine_result_granularity.md` |
| 6 | `Report Dialog window` | `02.10.02.06_Report_Dialog_window.md` |
| 7 | `How the Event Formatter works` | `02.10.02.07_How_the_Event_Formatter_works.md` |
| 8 | `Settings for the Event Formatter` | `02.10.02.08_Settings_for_the_Event_Formatter.md` |
| 9 | `Handling of test suite flags by the Event Formatter` | `02.10.02.09_Handling_of_test_suite_flags_by_the_Event_Formatter.md` |
| 10 | `Report window resources` | `02.10.02.10_Report_window_resources.md` |
| 11 | `Running report formatters as standalone tools` | `02.10.02.11_Running_report_formatters_as_standalone_tools.md` |
| 12 | `Appendix A: Event Formatter Files` | `02.10.02.12_Appendix_A__Event_Formatter_Files.md` |
| 13 | `Appendix B: Event Formatter Defaults` | `02.10.02.13_Appendix_B__Event_Formatter_Defaults.md` |
| 14 | `Appendix C: Event Formatter Output Examples` | `02.10.02.14_Appendix_C__Event_Formatter_Output_Examples.md` |

**（推断）这 14 条按语义可以分成五组，但原文没有分组、也没有小标题。**
**依据只是名字本身：**

| 组（**推断**） | 子主题 # | 依据（名字） |
|---|---|---|
| **怎么开** | 1、2、6 | `Activating` / `menus` / `Dialog window` |
| **输出长什么样** | 3、4、5、14 | `output` ×3、`granularity`、`Output Examples` |
| **怎么调** | 8、9、13 | `Settings` / `Handling of test suite flags` / `Defaults` |
| **原理与参考** | 7、10、12 | `How … works` / `resources` / `Files` |
| **独立使用** | 11 | `Running report formatters as standalone tools` |

**这个分法本页只标成推断，不当结论用。**

### 本页实际承载的最长内容是「输出长相」的一个样例（**而且它来自子主题**）

**`## 语法 / 参数` 节有 6,051 个字符**，**而本篇正文一共只有 2,249 个字符**——
**也就是说本页最长的那一节不是本篇抽的，是从子主题
`02.10.02.04_Shmoo_output_of_the_Event_Formatter.md` 抄的**
（**节首那行 ⚠️ 已写明，本页照它说**）。

**那一节是一份 shmoo 数据记录在 Event Formatter 里的完整文本输出**，本页只记它的骨架：

| 节里出现的（**逐字**） | 是什么 |
|---|---|
| `======== Started Testsuite Shmoo_2D ====…` / `======== Ended Testsuite Shmoo_2D ====…` | **首尾包住整份输出** |
| `******** Started Site : 1 ****…` / `******** Ended   Site : 1 ****…` | **按 site 分块**（节里给了 site 1 与 site 2 两块，两块内容几乎逐字相同，都是 `PASSED`） |
| `-------- Test Name:  714 parameters[1] ---…` / `-------- Shmoo ---…` | 测试名与块类型 |
| `Test Mode:  pass/fail,cycle error count` | **一份输出里并列两种 test mode** |
| `........ Shmoo Axis Information ....…` 下的 `X-Axis` / `Y-Axis` | **两条轴各自的 `TotalSteps` / `Test Range` / `Spec` 等**（`Spec: LEV.2.VIL[V]`、`Spec: TIM.2.tpd_CP_IOx[ns]`） |
| `........ Shmoo Matrix ....…` 下的四行图例 | `' '` = point not calculated / `'.'` = point passed / `'*'` = point failed / `'E'` = point returned an error |
| `Number Of Cells       : 121` | 矩阵格子数（**11 × 11**） |
| `Pin: @, TestMode : pass/fail` 与 `Pin: @, TestMode : cycle error count` | **同一格矩阵按两种 test mode 各画一遍** |
| `Shmoo picture has been saved in: /home/Devices/74HC299/shmoo/shmooPNG/shmoo_2D` | **它还会存一张图** |
| `Executed Testmethod ac_tml.AcTest.Shmoo on Site 1: PASSED` | **一行 test method 执行记录也被打进这份输出** |

**两处本页要提醒的：**

- **这一节是「样例」，不是「语法」**——**它的段名就叫 `### Example`**，
  **本篇定义文档自己一个 `Syntax` / `Parameters` 段都没有**（节首 ⚠️ 与 `## 语法 / 参数` 节都说了）。
  **所以别把它当格式规范读：它是「输出长这样」，不是「输出必须是这样」。**
- **`'E'` 那一行在图例里多一个行首空格**，前三条没有——
  **本页照实记，见 `## 出处` ⑦。**

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有一个可执行命令。**
**但本篇正文那 5 条 `How to …` 就是本章的用法目录**，
**而 14 个子主题把它们落到了具体篇目上。**
**下表全部是导航（本页没有读过其中任何一篇）：**

| 要做的 | 出口（**逐字**） | 出处 |
|---|---|---|
| **把它开起来** | `Activating the Event Formatter` | 子主题 1 |
| **用它加在 report window 上的菜单** | `Report window menus` + 正文 bullet 2 | 子主题 2；[[report-window]] 那页本页没读 |
| **用 Report Dialog window 控制输出** | `Report Dialog window` | 子主题 6 |
| **看默认输出长什么样** | `Standard output of the Event Formatter` | 子主题 3 |
| **看 shmoo 输出长什么样** | `Shmoo output of the Event Formatter` | 子主题 4；**本页 `## 语法 / 参数` 节里那份样例即出自此篇** |
| **看 min / max 级的细粒度结果** | `Fine result granularity` | 子主题 5 |
| **改它的设置 / 看默认值** | `Settings for the Event Formatter`、`Appendix B: Event Formatter Defaults` | 子主题 8、13 |
| **搞清它怎么对待 test suite flags** | `Handling of test suite flags by the Event Formatter` | 子主题 9 |
| **把它当独立工具跑（不起 SmarTest 的报告流程）** | `Running report formatters as standalone tools` | 子主题 11；**注意名字里是复数 `formatters`** |
| **知道它用到哪些文件 / report window 有哪些资源** | `Appendix A: Event Formatter Files`、`Report window resources` | 子主题 12、10 |
| **理解它的原理** | `How the Event Formatter works` | 子主题 7 |
| **写自己的 event-based report formatter** | **正文最后一段**（`highlight important considerations when writing your own event-based report formatter`） | **本篇没有给对应的子主题**——那段话指向的是「本章最后几节」，而最后几节是哪几节，本篇没有点名 |

**最后一格是本页要单独指出的**：**原文把「写自己的 formatter」推给
`The final sections of this chapter`，却没有说那是哪几节。**
**从 14 个子主题的名字看，最接近的是 7（`How … works`）与 11（`Running report formatters …`）
——但这只是（推断），依据只是名字，原文没有指名。**
（**见 `## 出处` ④。**）

## 和谁有关

- [[report-window]] — **本页最直接的一条关系，而且是原文自己写的**。
  逐字：`- How to use the new menus of the report window that are added by the Event Formatter`。
  **即：Event Formatter 依附于 report window，并往它上面加新菜单。**
  **另外子主题 2 是 `Report window menus`、子主题 10 是 `Report window resources`——
  14 个子主题里有 2 个是讲 report window 的。**
  **本页只有这两处点名，那个窗口本身怎么用本页没有（那一页本页没读）。**
- [[smartest-data-formatter]] — **（推断）同族的另一个 formatter，但本篇一个字没提它。**
  依据：两页的 frontmatter 同组（`layer: gui` / `stage: results`），
  且都叫 formatter；**本篇正文里 `STDF` 出现 0 次、`EDF` 出现 0 次**（本页查过），
  **所以两者的分工本页没有依据说。这是推断，不是文档事实。**
- [[shmoo-tool]] — **（推断）子主题 4 与它可能同指一件事**。
  依据：14 个子主题里有一个是 `Shmoo output of the Event Formatter`，
  而 wiki 另有一页叫 [[shmoo-tool]]；
  **前者说的是「Event Formatter 的 shmoo 输出」，后者是「shmoo 工具」，
  两个名字不是一回事，本篇也没有点 `shmoo tool` 这个名字**（**本页查过：本篇只有
  `Shmoo`（大写、专名），没有 `shmoo tool`**）。**本页不做这个等同。**
- [[edl-file]] / [[edf]] — **（推断）同章的数据来源，但本篇都没提**。
  依据只是路径：本篇 `sources:` 的前两级是 `02_System_reference/02.10_Data_Logging/`，
  **从路径看它们落在 Data Logging 这一章里**；
  **本篇正文里 `EDF` 0 次、`STDF` 0 次、`data log` 只以 `data logging tool`
  这个自述身份出现一次**——**它吃什么格式的数据，本篇一个字都没写。**
- [[data-retrieval-library]] — **（推断）同章**，依据同上（只有路径这一条）。
  **本篇没有提过它，也没有提过任何读库。**
- [[smartest-6.3.2]] — **版本页**。本页 `## 版本` 唯一那一条 `Introduced before SmarTest 6.3.2` 的落点。
- `Report Dialog window`（**未建、不在 allowlist，故用反引号**）—
  **它自己的控制窗口**，子主题 6，也是正文 bullet 3 的主角
  （`How to use the Report Dialog window to control the output of the Event Formatter`）。
  **它与 [[report-window]] 是两个东西**——**本篇把 `report window` 与
  `Report Dialog window` 写成两个名字，本页不把它们合并。**
- `Activating the Event Formatter`（**未建**）— **子主题 1**，
  对应正文 bullet 1 的 `How to activate the Event Formatter`。**本篇没有给启用步骤。**
- `Standard output of the Event Formatter` / `Shmoo output of the Event Formatter` /
  `Fine result granularity` / `Appendix C: Event Formatter Output Examples`
  （**四个，均未建**）— **「输出长什么样」那一组**。
  **其中 `Shmoo output …` 就是本页 `## 语法 / 参数` 节的来源。**
- `How the Event Formatter works` / `Settings for the Event Formatter` /
  `Handling of test suite flags by the Event Formatter` / `Report window resources` /
  `Report window menus` / `Running report formatters as standalone tools` /
  `Appendix A: Event Formatter Files` / `Appendix B: Event Formatter Defaults`
  （**八个，均未建**）— **上面 14 条表里剩下的八条**。
  **注意 `Handling of test suite flags …` 里的 `test suite flags`
  与 [[alphabetical-list-of-flags]] 那份清单是不是同一批 flag，
  本篇没有依据判断**（**本篇没有列任何 flag，也没有给任何一个 flag 的名字**）。
- `event-based report formatter`（**未建**）— **原文最后一段点名的那类东西**：
  `important considerations when writing your own event-based report formatter`。
  **本篇没有解释它是什么、和 Event Formatter 什么关系
  （（推断）从名字看是「你自己写的、同一族的 formatter」，但原文没说）。**

## 版本

**本文档有 `## Functional changes` 段，只有一条**，逐字：

- **Introduced before SmarTest 6.3.2**

**这一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 Event Formatter 本身成立于哪个版本，这份语料里没有。**

**本篇没有任何别的版本信息**：**正文 2 段 + 5 条 bullet、子主题 14 条，
一条版本号都没有**——**`SmarTest 6.3.2` 是本篇里唯一出现过的版本号。**

**与 wiki 目标版本（SmarTest 7.10.3）的关系**：
**本篇连一条 7.x 的条目都没有**——
**所以 7.10.3 上这个工具的行为、界面、可定制项，本篇给不出任何依据。**

**（推断）版本段只有这一条、而正文却有 14 个子主题的篇幅**——
**依据只是这个反差本身：一篇讲一个 GUI 工具的章，版本沿革一条都没记。
这是本页的观察，不是文档事实。**

详见 [[smartest-6.3.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.md`

**本页没做的：**

- **14 个子主题一篇都没读。** **这是本页最大的空缺**：
  **本篇正文只有两段话（定义 + 简介）与 5 条章节 bullet，
  这个工具的一切实际操作（怎么开、菜单怎么用、对话框怎么填、设置项有哪些、
  输出有哪几种、flag 怎么处理、怎么当独立工具跑）全在子主题里**，
  **本页一个都没有。**
- **`## 语法 / 参数` 节的来源子主题
  `02.10.02.04_Shmoo_output_of_the_Event_Formatter.md` 没读。**
  **那一节 6,051 个字符、是本页最长的一节，本页只按它逐字摆出来的内容转述骨架，
  没有回那一篇核过**——**所以上面那张「节里有什么」的表是转述，不是回原文核过的。**
- **本篇正文里的 `report window` 与 `Report Dialog window` 都没读**，
  **所以 Event Formatter 加的那几个菜单叫什么、对话框里有哪些项，本页一个字都没有。**
- **`test suite flags` 没读**——**所以子主题 9 讲的那些 flag 与
  [[alphabetical-list-of-flags]] 是不是同一批，本页没有依据判断。**
- **一张图都没有。** 原文没有图片（本页查过：0 处图片语法）——
  **本页 `## 语法 / 参数` 节里那份 shmoo 输出是纯文本，不是图。**
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：[[report-window]] / [[shmoo-tool]] / [[smartest-data-formatter]] 都没读**——
  **本页与它们的关系全部取自本篇这一篇的正文，没有从对面回校过。**
  **本页也刻意没有写「它吃什么格式的数据」「它和 STDF 什么关系」——
  本篇对这两件事一个字都没有。**
- **`layer: gui` / `stage: results` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分
  （**（推断）`layer: gui` 与定义句里那个 `dialog window` 相符，但这是本页的观察，不是原文说的**）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 一篇章的入口页，正文只有两段话。** 本篇 2,249 个字符里，
> **`#### Subtopics` 的 14 条链接占了大半**，剩下的是：一段定义（2 句）、
> `This chapter describes:` + 5 条 bullet、一段收尾（1 句）。
> **一篇讲一个 GUI 工具的章，自己一句操作说明都没有。本页照实说，不替它写。**
>
> **② `data logging` 这个自述身份与 `interactive debugging` 这个用途并列，
> 但本篇没有解释两者的关系。** 逐字：
> `a report generating tool that is used for interactive debugging` …
> `the Event Formatter is a powerful data logging tool`
> ——**同一段两句话，一句说用途是调试、一句说它是数据记录工具；
> 它记的是哪一份数据、记到哪去，本篇一个字都没写。**
> **（本页查过：本篇 `EDF` 0 次、`STDF` 0 次、`stream` 0 次。）**
>
> **③ `#### Subtopics` 是 H4，直接挂在 H1 下面。** 本篇的非 H1 标题只有这一个，
> 层级是 H4——**H2 与 H3 在本篇里不存在**。
> （**这是本批第三篇同形态的页；那两条本页引自 [[edf]] / [[error-map]] 页，不是本篇 raw。**）
>
> **④ 「最后几节」是一个没有兑现的指代。** 逐字：
> `The final sections of this chapter provide background information on how the Event Formatter
> works in principle, and highlight important considerations when writing your own event-based
> report formatter.`
> ——**`The final sections` 指的是哪几节，原文没有点名**；
> **而子主题列表是平铺的 14 条，也没有任何一条标着「最后」或「背景」。**
> **本页并列两处，不替它认领。**
>
> **⑤ 14 条子主题里两条带 `Appendix` 前缀，而且文件名里的空格变成了双下划线。** 逐字：
> `- [Appendix A: Event Formatter Files](<02.10.02.12_Appendix_A__Event_Formatter_Files.md>)`
> ——**链接文本里是 `Appendix A:`（冒号+空格），而文件名里是 `Appendix_A__Event_Formatter_Files`
> （`A` 后面两个下划线）**。**另两条 Appendix 同构。**
> **这是语料的命名约定（冒号与空格进不了文件名），不是错字，
> 但会让按显示名去找文件的人搜不到。**
>
> **⑥ 14 条链接一律是 `[文本](<文件名.md>)` 的写法**——**文件名外套尖括号、不带目录前缀**。
>
> **⑦ `## 语法 / 参数` 节里 shmoo 图例的第 4 行多一个行首空格。** 逐字（**注意 `'E'` 前面**）：
> `' '   = point not calculated` / `'.'   = point passed` / `'*'   = point failed` /
> ` 'E'   = point returned an error`
> ——**前三条从第 1 列开始，第 4 条缩进了一个空格；同时 `'E'` 这一条的等号
> 与前三条的等号也不在同一列上。**
> **（这一节是从子主题抽的，见节首 ⚠️；本页照实记，不替它对齐。）**
>
> **⑧ 节里同一份 shmoo 输出被完整重复了两遍（site 1 与 site 2）。** 两块从
> `******** Started Site : …` 到 `******** Ended   Site : …` 几乎逐字相同
> （**两块的最后都写着 `PASSED`，两块里的 shmoo 矩阵也一格不差**）。
> **原文没有说明为什么要把两个 site 各印一份。本页照实说。**
> **同一处还有：`******** Ended   Site : 1` 里 `Ended` 与 `Site` 之间是三个空格，
> 而 `******** Started Site : 1` 里 `Started` 与 `Site` 之间是一个空格。**
>
> **⑨ shmoo 输出里混进了一行 test method 执行记录。** 逐字：
> `Executed Testmethod ac_tml.AcTest.Shmoo on Site 1: PASSED`
> ——**它夹在 shmoo 矩阵与 `******** Ended   Site : 1` 之间**，
> **既不是 shmoo 数据、也不带 shmoo 那几种 `----` / `....` 分隔线。**
> **它属于这份输出还是被压平进来的，原文没有交代。本页并列，不判。**
>
> **⑩ 本篇没有 §11.2 ① 那种编码损坏**（本页查过：汉字 0 个、`鈥` 0 处）。

`verified: doc-only`
