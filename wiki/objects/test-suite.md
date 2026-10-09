---
type: object
title: Test suites
layer: n/a
stage: testflow
tags: [testflow, test-suite, run-and-branch, special-test-suite, floating-test-suite, multibin-smartdisconnect, multibin, bin]
related: [testflow, test-suites-page, special-test-suites, testflow-file, flow-sequence-editor, flow-data-editor, bin, test-suite-control-api, testmethod, run, testflow-tool, mapping-testflow]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01_Test_suites.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Test suites

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **737 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01_Test_suites.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.04_Multibin_SmartDisconnect_test_suite.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Multibin SmartDisconnect test suite）

### Properties of a Multibin SmartDisconnect test suite

The Multibin SmartDisconnect test suite is a combination of a `multibin node`（raw: `../../03_Use_cases_and_application_papers/03.02_How_to_do_Multi-Site_Testing/03.02.02.06.07_Use_of_multibins.md`） and a test suite and therefore offers properties that are typical for a test suite:

 !`Multibin SmartDisconnect test suite properties`（raw: `../../../../raw/353652.png`）  Note You must choose the `wide selection`（raw: `02.08.04.32.02.01.11.01_Narrow_selection_and_wide_selection.md`） for the node in order to inspect or change the properties of the Multibin SmartDisconnect test suite. For the narrow selection, inspecting and changing the properties is possible only for the Run and Branch node.

<!-- 语法节 end -->

## 是什么

**test suite 是 testflow 里那个「可以被执行的最小单元」的名字。** 定义文档给的是一句集合定义：

> 「This is the collective name given to individual, independent, executable device tests (a functional test, for example). The test suite contains the various timing and level sets and equations and the set of test suite flags.」

**两件事要分开读**：**它是一个集合名**（functional test 这类「独立的、可执行的器件测试」都叫 test suite），
**不是一个具体对象**；而**一个 test suite 里装着四样东西**——
timing sets、level sets、equations、**和一组 test suite flags**。

### 四类 test suite（原文的四条，一条一句）

| 类型 | 原文那一句 |
|---|---|
| **"Run" / "Run and Branch"** | `"Run" test suites offer only one path, while "Run and Branch" test suites offer branching depending on the test result.` |
| **Special test suites** | `Special test suites are executed at a particular point in time, which can be either dependent or independent of the testflow.` |
| **Multibin SmartDisconnect test suite** | `The Multibin SmartDisconnect test suite is a combination of a multibin node and a user defined test suite.` |
| **Floating test suite** | `The floating test suite is not connected to the testflow sequence and can be used for debugging.` |

**四类各有一篇专页**（`## Related information` 之外，正文里也重复链了一遍，见「和谁有关」）。
**本篇每一类只给一句**，所以这一页的定位是**分诊台**：
「**我要的东西属于哪一类**」，答案在这儿；「**这一类具体怎么用**」，答案在专页。

### 图证：Multibin SmartDisconnect 的属性清单只在图里（④ 图证）

**本页 `sources:` 那一篇没有图。** 但本页「语法 / 参数」节里有一张
`353652.png`（Multibin SmartDisconnect test suite properties），
是随子主题的 Example 段一起抄进来的——**本页读了它**。
路径 `../../../../raw/<n>.png` 从 md 往上四层正好是 `tdc-html/`，文件在 `tdc-html/raw/`——
**有些页曾写「图在语料树之外」，那是错的**（`schema.md` §11.4）。

**它把「properties that are typical for a test suite」这句话坐实了**——
`语法 / 参数` 里那句只说「有 typical 属性」，**属性叫什么名字，一个字没写**，图里全在：

| 图 `353652.png` 读到的 | |
|---|---|
| **右窗格的表头** | 两列 `Property` / `Value`；面板标题 `Multibin Disconnect`，值 `Disconnect_1`；上方另有 `type filter text` 输入框，页签 `Properties 23` / `Outline 8` / `Site Select` |
| **属性逐条** | `Comment` = `...`；`Primaries` 展开后 `Timing` = `1, 1, 1`、`Level` = `1, 1, 1`、`Analog` 空；`Pattern` = `Test_1_pattern`；`Context` = `DEFAULT`；`Test Type` = `Multibin_SD`；`Test Method` = `TML.Disconnect_Setup_1`；另有 `Parameters`、`Flags`、`Site Control` 三个可展开项；`BackgroundColor` = `Yellow` |
| **左窗格** | `Start` → `Test_1`（分支节点，P/F）→ P 下来 `Test_2` → `Test_3` → `Disconnect_all` → 绿色 good bin；`Test_1` 的 F 支路接一个**黄底高亮的 bin 节点**；`Test_1` / `Test_2` / `Test_3` **各挂一个 `SD` bin 图标（三个重叠的红圆）**，底色分别是黄 / 青 / 橙 |

**图里的字，哪些搜得到、哪些搜不到**（本页拿它们去全语料 grep 过——
**这是本页为「图里的字搜不搜得到」做的一次检索，不是本页 `sources:` 里的内容**）：

- **0 命中**：`Multibin_SD`、`Disconnect_1`、`TML.Disconnect_Setup_1`、`Properties 23`、`Outline 8`。
- **有命中，但不在本页这一支**：`Test_1_pattern`（1 篇，是 `03.05` 的一篇用例）；
  `Multibin Disconnect`（1 篇，是 `02.08.04.32.01.02.01.04.01`）；
  `Disconnect_all`（1 篇，同上那篇）；
  `BackgroundColor`（2 篇）、`Primaries`（13 篇）**都搜得到**，但那是**别的页面的截图**里的同一批列名。
- **`SD` 这个 bin 标签太短，搜得到的东西全是子串命中**，本页不拿它当证据。

**结论**：这张图**给的是「属性叫什么」**，不包括取值以外的规范——
**哪些属性必填、哪些组合非法，本页答不了**（图是某一次具体配置的截图，不是格式规范）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**，
所以「怎么用」这一节只能是**选型**——原文四条描述本身就是判据：

| 你的情况 | 用哪一类 |
|---|---|
| 一个测试跑完就完，没有分支 | **"Run"** test suite（`offer only one path`） |
| 要**按测试结果**分岔（过 / 不过各走一路） | **"Run and Branch"** test suite |
| 要在某个**特定时刻**执行，跟不跟 testflow 走都行 | **Special test suites** |
| 要在**fail 分支**上按多 site 分别断开（multibin + 断开序列） | **Multibin SmartDisconnect test suite** |
| 还在**调试**，先别挂在流程里 | **Floating test suite** |

**两条从原文那一句里能直接读出的限制**：

- **Multibin SmartDisconnect 是「multibin 节点 + 一个用户定义的 test suite」的组合**
  ——**它不是另一个 test suite 类型，是一个组合体**；
- **Floating test suite 不连在流程上**（`is not connected to the testflow sequence`），
  **所以它是调试用的旁路，不是正式路径。**

**本篇没有「下一步」段**：连 `## What to do next` 都没有，
四个专页是靠 `#### Subtopics` 与正文里重复的那两批链接给出的（见「和谁有关」）。

## 和谁有关

**出边 8 条，但只指向 4 个目标**——**同一批四条链接在文档里出现了两次**：
一次在 `#### Subtopics`（第 10–13 行），一次在正文「There are several types of test suites:」底下
（第 19 / 23 / 27 / 31 行）。**两处的顺序还不一样**（Subtopics 把 Floating 排第三、
Multibin SmartDisconnect 排第四；正文里两个对调了）——**照实记，见「出处」②**。

**入边 9 条 / 8 篇**（`inline` 口径，`extract/edges.jsonl`）：

- `02.08.04.32.01.02_Testflow_components`（**2 处**）——**它是「testflow 由什么组成」那一节里的一项**，
  这是本页最正式的上游。
- `02.08.04.32.02.01.11_Working_with_nodes`、`02.08.04.32.02.01.12.01_Defining_variables`
  ——讲节点与变量时把它当参照。
- `02.12.02.05.04_Creating_a_testflow_in_SmarTest`（MTP 那一章）——**在别的产品线里也这么叫**。
- `99_Unlisted_or_Unreferenced` 四篇：`Adding_a_test_suite_in_the_testflow`、
  `Types_of_testflow_variables`、`Inserting_a_floating_test_suite_in_the_testflow_sequence`、
  `Searching_for_a_variable`。

- [[testflow]] — 本页 `stage: testflow`；**test suite 是 testflow 的组成单元，本页是它的定义页**
- [[test-suites-page]] — **定义在哪**：Testflow Tool / Flow Data Editor 里那两处
  （**本页没读那一篇**，所以「那一页长什么样」本页不知道）
- [[special-test-suites]] — **同类且是下游**：本页给 Special test suites 一句话，那页展开
- [[testflow-file]] — **它存到哪**：`test_flow` / `test_suites` 两个 section
  （**本页没读那一篇**，那是从同阶段页 [[mapping-testflow]] 的对照表里知道的）
- [[flow-sequence-editor]] / [[flow-data-editor]] — **在哪编**：图形侧与数据侧的两个编辑器
- [[bin]] / [[testmethod]] / [[run]] — test suite 边上直接相关的东西
- [[test-suite-control-api]] — **从外部读/写 test suite flag 的那套接口**
  （`mapping-testflow` 把它记成 test suite flag 那一行的 L3 落点）
- [[testflow-tool]] — **父级 GUI 工具**；本页的定义文档挂在它的 `Introduction of the Testflow` 支下
- [[mapping-testflow]] — 同阶段的对照表页；它把本页当作「test suite flag 的 GUI / 文件两侧」的落点

**同名的**：`Floating test suite`（未建）、`"Run" and "Run and Branch" test suites`（未建）、
`Multibin SmartDisconnect test suite`（未建）——**本页四条链接的三个目标都还没有页**，
所以那三条**本页不链**（§9.1：链一个清单外的名字 = 造一个永远不会建的悬空目标）。

## 版本

本篇 `## Functional changes` 两条：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.6.1: Added Multibin SmartDisconnect test suite.`

> ⚠️ **第一条是哨兵值**（`schema.md` §11.2②）：措辞是 `before`，意思是「**在本文档集覆盖范围
> 开始之前就已经有了**」，**不是「6.3.2 新增了 test suite 这个概念」**。
>
> **第二条是真新增**，而且**和本页的语法节对得上**：语法节里那段 Multibin SmartDisconnect 的
> 属性例（含图 `353652.png`）**就是 7.6.1 才有的东西**——所以**在 7.6.1 之前的版本上，
> 那一支子主题与那张图不该存在**。**这条对应关系是（推断）**：依据是本篇自己的版本记录
> 与那篇子主题的存在，**本页没有 7.6.1 之前的语料可对照。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01_Test_suites.md`
（TDC `20227.htm`，38 行 / 1,802 字节）。

**本页没做的**：

- **四支子主题一篇没读**：`02.08.04.32.01.02.01.01_Run__and__Run_and_Branch__test_suites.md`、
  `02.08.04.32.01.02.01.02_Special_test_suites.md`、`02.08.04.32.01.02.01.03_Floating_test_suite.md`、
  `02.08.04.32.01.02.01.04_Multibin_SmartDisconnect_test_suite.md`。
  **这是本页最大的缺口**：本篇每一类只给一句话，**「每一类到底怎么用」全在这四篇里**，
  所以本页**只有分诊，没有做法**。
- **「test suite 里那四样东西」本页只点到名字**：timing sets、level sets、equations、
  test suite flags 各是什么、怎么配，**本页一个字没有**（那四样各有专页）。
- **图 1 张看了**（`353652.png`，随语法节的子主题例一起进来的），结论在「是什么」里。
  **本页 `sources:` 那一篇本身没有图**，所以「本页的图」只有这一张。
  **不是「本页没用图」。**
- **上面那些「0 命中 / 有命中」，是本页拿那些串去全语料 grep 得到的检索结果**，
  **不是本页 `sources:` 里的内容**——写出来只为说清「图里的字搜不搜得到」（§11.4 的 ④ 档要求）。
  其中被点到名字的 `02.08.04.32.01.02.01.04.01_Inserting_a_Multibin_SmartDisconnect_test_suite.md`
  与 `03.05.02.04_DC_event_example__Setup_per_site.md` 两篇，**本页也没读**。
- **`layer: n/a`（frontmatter 里就是 `n/a`，来自 `extract/wiki-plan.csv`）**：
  **「test suite 属于哪一层」本页不判**——本篇没写，本页也没有第二条依据。
- **没有实跑**：没建过 test suite、没插过 Multibin SmartDisconnect、没跑过 floating test suite。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有改 `wiki/stages/testflow.md`。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> ① **Multibin SmartDisconnect 的定义，本篇与那篇子主题措辞不同。** 本篇写的是
> `The Multibin SmartDisconnect test suite is a combination of a multibin node and a user defined test suite.`
> （**带 `user defined`**），而本页语法节里那段子主题原文是
> `The Multibin SmartDisconnect test suite is a combination of a multibin node and a test suite and therefore offers properties that are typical for a test suite:`
> （**没有 `user defined`**）。**同一支文档树里两种说法，本页并列，不替它选一个。**
>
> ② **四条子主题链接在文档里出现两次，而且顺序不同。** `#### Subtopics` 的顺序是
> Run and Branch → Special → **Floating** → **Multibin SmartDisconnect**；
> 正文「There are several types of test suites:」底下的顺序是
> Run and Branch → Special → **Multibin SmartDisconnect** → **Floating**。
> `extract/edges.jsonl` 里同一批目标各有两条边（第 10–13 行与第 19 / 23 / 27 / 31 行），
> **正是这件事的机器证据**。
>
> ③ **排版瑕疵**：正文里 `There are several types of test suites:` 这一行
> **在 raw 里前面有两个空格的行首缩进**（它上面还空了一行）——
> 本页没有原样引用这一行，故不受影响。
>
> ④ **图 `353652.png` 里 test suite 的显示名与正文用词不同**：图里 `Test Type` 的值是
> `Multibin_SD`，而正文一律写 `Multibin SmartDisconnect`。**`Multibin_SD` 全语料 0 命中**
> ——**那个缩写只在图里**，本页照实记，不把它当成文档用词。
>
> **本页（含脚本生成的语法节）0 处编码坏字**（`碌` / `渭` / `卤` / `惟` / `鈥` 那几族逐个查过），
> **0 处 `DC/DC power units`**（§11.2⑤ 那一族）。

`verified: doc-only`
