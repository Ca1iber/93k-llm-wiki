---
type: object
title: Special test suites
layer: file
stage: testflow
tags: [testflow, test-suite, flow-data-editor, bin, disconnect, exception-handling]
related: [testflow, test-suite, flow-data-editor, flow-sequence-editor, test-suites-page, bin, disconnect]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Special test suites

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**special test suite 是「不在 testflow 图上、而在特定时刻被触发」的测试套件。** 原文第一句：

> 「Special test suites are executed at a particular point in time, which can be either dependent or independent of the testflow. For example, downloading an initial set of values to the test system, or defining what will be executed if you abort the testflow.」

**「a particular point in time」是它和普通 test suite 的全部分界。** 普通 test suite
被 testflow 的顺序流到才执行；**special test suite 由「系统进入某个状态」或「流程走到某个节点」触发**，
**和 testflow 的执行顺序可以有关、也可以无关**——原文用 `either dependent or independent` 明确留了两头。

原文给的两个例子正好各占一头：**下载初始值**（和流程有关）、**定义 abort 时执行什么**（和流程无关）。

### 它不出现在 Flow Sequence Editor 里

> 「Special test suites do not appear as nodes in the Flow Sequence Editor, but in the Flow Data Editor, they are displayed at the end of the Test Suites page when sorting by default.」

| 在哪个视图 | 看不看得见 |
|---|---|
| `Flow Sequence Editor` | **不作为节点出现**（`do not appear as nodes`） |
| `Flow Data Editor` → `Test Suites page` | **默认排序时显示在末尾** |

**「图上没有、列表里有」是它最容易被漏掉的原因**——**只照着 Flow Sequence Editor 找，一个都找不到。**

### 一条硬禁令：不许抛异常

原文把它写成一个 `Note`：

> 「Do not throw any exceptions from inside special test suites, as the handling is not compatible with the testflow executor.」

**这是本篇唯一的「不许」，理由是「处理方式与 testflow executor 不兼容」。**
原文**只说不能抛，没说抛了会怎样**——**本页不替它补**。

### 八种（**原文说的是七种**）

原文这一句和它后面的列表对不上：

> 「There are seven types of special test suites.」

**紧接着列出来的有八个。**（**本页照实记，不替它改**，见 `## 出处` ⚠️①。）

| 套件 | 什么时候执行 | 原文的补充 |
|---|---|---|
| `Init` | **`Download` 之后、testflow 首次运行之前** | **可选**；给系统做初始设定：testflow 变量、外部设备初始状态（原文举例：支持 prober 的 docking）等 |
| `bin_disconnect` | **器件落进某个 bin 时** | **legacy**，新设备原文推荐换掉（见下） |
| `Abort` | 系统进入 **abort** 状态 | **不重置硬件** |
| `Reset` | 系统进入 **reset** 状态 | **重置硬件**，所以要接着跑必须重新 download 原始设置 |
| `Pause` | 系统进入 **pause** 状态 | 在 application model 的 pause section **之前**执行 |
| `multi_bin_decision` | **一个或多个 site 走到 testflow 里的 multi_bin 节点时** | 用 `SET_MULTIBIN` API 决定用哪个 bin |
| `Exit` | 系统进入 **exit** 状态 | **只在 testflow 是从 testprogram 里启动时才有意义**；在 testprogram 终止**之前**执行 |
| `Download` | **testflow 加载之后** | 用来加载 `Setups page` 上选中的 pin configuration setup，或其他 setup 文件 |

**八个里有四个（`Abort` / `Reset` / `Pause` / `Exit`）是同一族**：都由「系统进入某个状态」触发。
它们的触发来源，原文各写了一句几乎一样的话——**但措辞有三处不同，值得单列：**

| 套件 | 触发状态的三种来源（原文） | 异常处理那一档的原文措辞 |
|---|---|---|
| `Abort` | `chosen in the Operation Control Window (in any mode)`, `or programmed`, `or occurs in cases of exception handling (test system, library or program errors)` | `occurs in cases of …` |
| `Reset` | 同上，**但没有 `(in any mode)`** | **`occurs in some cases of …`** |
| `Pause` | 同上，**但没有 `(in any mode)`** | **`occurs in most cases of …`** |
| `Exit` | 同上，**但没有 `(in any mode)`** | `occurs in cases of …` |

> **三点必须点出来，且不许替原文统一**：
> ① **只有 `Abort` 写了 `(in any mode)`**——其余三个没有这四个字；
> ② **`some` 只出现在 `Reset`、`most` 只出现在 `Pause`**——`Abort` / `Exit` 都是不带限定的 `cases of`；
> ③ **原文没有解释这个差别意味着什么**（是频率不同？是每个套件各自成立的条件不同？）。
> **本页不判、也不合并这三种写法。**

### `Abort` 与 `Reset` 的差别只有一条：硬件重不重置

这两个最容易混，原文各写了一句，**正好互为反面**：

| | `Abort` | `Reset` |
|---|---|---|
| unload test program | **是** | **是** |
| 断开测试系统 | **是** | **是**，且进入 `an initialized (disconnected) state` |
| **重置硬件** | **不** —— `It does not, however, reset the test system hardware.` | **是** —— `The test system hardware is reset` |
| 接着要跑怎么办 | 原文没写 | **必须把原始设置重新 download** |

> 「The reset state unloads the test program and puts the test system in an initialized (disconnected) state. The test system hardware is reset, so you must ensure you download the original settings again if you wish to restart.」

**所以「重启」这件事上，「卸载并断开」两个都做到了，差的只有硬件那一下**——
**而恰恰是那一下决定了你要不要重新 download。**

### `bin_disconnect` 的两条分支，以及原文唯一一条「改用别的」

**只有用了 `DISCONNECT` API，才有下面这个分岔**：

> 「If you use the DISCONNECT API in this test suite, then
> - if you defined a disconnect sequence in the device, the disconnect sequence will be executed;
> - if no disconnect sequence is defined, the standard disconnect sequence will be executed.」

| 条件 | 结果 |
|---|---|
| 设备里**定义了** disconnect sequence | **执行你定义的那个** |
| **没定义** | **执行标准的那个** |

**然后原文主动劝退**：

> 「bin_disconnect is a legacy method of disconnecting failing devices. For new devices, we recommend using the Multibin SmartDisconnect test suite that is a combination of a multibin node and a user defined test suite.」

**这是本篇唯一一处「推荐用别的」。** 注意它的形态：**替代品不是另一个 special test suite，
而是「一个 multibin 节点 + 一个用户自定义 test suite」的组合**——
**也就是说，新的做法不在本页这张八种表里。**

### 执行顺序：原文写了两遍

testflow 的启动序列，原文在 `Init` 和 `Download` 两处各给了一遍（**两遍八步逐字相同，只是形式不同**）：

| 步 | 动作 |
|---|---|
| 1 | test program 被加载 |
| 2 | testflow 被加载 |
| 3 | pin configuration 被加载 |
| 4 | **`Download` 套件执行** |
| 5 | **`Init` 套件执行** |
| 6 | **testflow 的第一次 run 开始** |
| 7 | **所有尚未加载的 setup 文件被 download** |
| 8 | 第一个 test suite 执行 |

**两处值得停一下：**

> **① 第 6 步在第 7 步前面**——「testflow 的第一次 run 开始」**先于**「其余 setup 文件下载」。
> 也就是说**第 7 步发生在 `Init` 和 `Download` 之外**，`Download` 套件管不到它。
> **原文就这个顺序，本页不判它是否反直觉。**

> **② `Init` 与 `Download` 的先后是写死的**：`Download`（第 4 步）**总在** `Init`（第 5 步）之前。
> 原文在 `Init` 那一条里用一句话把这个关系重复了一遍：
> `The Init test suite is executed after the Download test suite and before the testflow execution starts.`

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`。** 所以**「怎么建一个 special test suite」
本篇给不出来**——**本页只能给「什么时候用哪一个」。**

**1. 怎么挑**（按「你要在什么时刻做事」对号）：

| 你要做的事 | 用哪个 |
|---|---|
| testflow 开跑之前设变量、让外部设备就位（prober docking 等） | **`Init`**（**原文标为可选**：`An optional test suite`） |
| testflow 加载后补下载 setup 文件 / pin configuration | **`Download`** |
| abort / reset / pause / exit 时收尾 | 对应的四个之一 |
| 器件落 bin 时断开（**legacy**） | **`bin_disconnect`**（**新设备原文建议换成 multibin 节点 + 自定义 test suite**） |
| 在 multi_bin 节点决定 bin | **`multi_bin_decision`**（配 `SET_MULTIBIN`） |

**2. 找它们的地方**：`Flow Data Editor` → `Test Suites page`，**默认排序时在末尾**。
**不要在 `Flow Sequence Editor` 里找**，它们不上图。

**3. 写的时候必须守的一条**：**套件里不许抛异常**（理由见上）。

**4. 原文的 `## Related information` 列了五篇**：`Multibin SmartDisconnect test suite`、
`Defining connect/disconnect sequences`、`Aborting a Production Run`、`Resetting a Production Run`、
`Aborting a Testflow`——**本页一篇都没读**（见 `## 出处`）。

## 和谁有关

- [[testflow]]（**已建**）— **多数套件是在 testflow 的某个时刻被触发的**；
  但原文第一句就强调**有的与 testflow 无关**，**所以不能把这一页当成 testflow 的子页看**
- [[test-suite ]] — **同类、但分界清楚**：普通套件在图上按顺序执行，**special 套件不上图**
- [[flow-sequence-editor ]] — **它们在这里看不见**（`do not appear as nodes`）
- [[flow-data-editor ]] — **它们在这里被看到**
- [[test-suites-page ]] — 具体显示位置（**默认排序时在末尾**）
- [[bin ]] — 两处相关：`bin_disconnect` **按 bin 触发**；`multi_bin_decision` **决定 bin**
- [[disconnect ]] — `bin_disconnect` 只有在套件里用了 `DISCONNECT` API 时，才走「自定义 / 标准」那两条分支
- `Multibin SmartDisconnect test suite`（**未建，且不在本 wiki 的建页清单里**）—
  原文**推荐新设备用它替代 `bin_disconnect`**；**本页没读它那篇**，所以它怎么组合出来的本页不知道
- `Operation Control Window`（**未建**）— `Abort` / `Reset` / `Pause` / `Exit` 四个状态的**人工触发入口**
- `Flow Sequence Editor` / `Flow Data Editor` / `Test Suites page`（**均未建**）—
  它们长什么样本页不知道，**本页只有「这个套件在哪个视图里出得来」这一条**

## 版本

原文**有** `## Functional changes`，四条：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 6.3.2**：`Special test suites are now displayed in the Tabular Testflow Editor.`
- **SmarTest 6.5.0**：`New special test suite bin_disconnect.`
- **SmarTest 6.5.2**：`New special test suite multi_bin_decision.`

**① 第一条是哨兵值，不是「6.3.2 引入」。** 本 wiki 里 `Introduced before SmarTest 6.3.2`
的写法意思是「**在本文档集覆盖范围开始之前就已经有了**」（schema §11.2 ②）——
**照字面读会读成「6.3.2 新增了 special test suite 这个机制」，那是假的。**

**② 6.3.2 那条新增的是「显示」，不是套件本身**：
`are now displayed in the Tabular Testflow Editor`——**机制早就有，这一版只是让它出现在 Tabular 编辑器里。**

**③ 两条既有的，正文里也点了名**（`bin_disconnect` / `multi_bin_decision`），
**且 `bin_disconnect` 在正文里已经被打成 legacy**——**同一条特性在「版本」里是新增、在「正文」里是劝退，
原文两处都留着。**

**④ 剩下六种套件是哪个版本进来的，原文一个字没写**——
**版本记录里只有这两条「New special test suite」**，
所以**「八种从哪一版开始齐」这个问题，本篇答不了。**

> **顺带一提，版本记录也治不了正文那个数**：正文说 `seven types`、列了八个，
> **版本记录里能数出名字的只有两种**——**两处加起来仍然数不清到底是七还是八**（见 `## 出处` ⚠️①）。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.md`

**本页没做的**：

- **`## Related information` 那五篇一篇没读**：`Multibin SmartDisconnect test suite`、
  `Defining connect/disconnect sequences`、`Aborting a Production Run`、`Resetting a Production Run`、
  `Aborting a Testflow`。**所以「怎么让系统进入 abort / reset 状态」本页只有那一句 `chosen in the
  Operation Control Window … or programmed`，没有操作步骤。**
- **`Flow Data Editor` / `Test Suites page` / `Flow Sequence Editor` 三篇没读**——
  **special test suite 在页面上长什么样、能不能编辑、怎么新建或删除，本页一个字都没有。**
- **`DISCONNECT` 和 `SET_MULTIBIN` 两个 API 那两篇没读**——
  **怎么在套件里调它们、调完什么效果**，本页只有原文转述的那一两句。
- **`Operation Control Window` 那篇没读。**
- **源文档里没有图**（那一篇正文里没有任何插图，也**没有 `Subtopics`** 那一层要查）。
  **所以本页没有任何来自图的结论。**
- **没有 `## Procedure` / `## Before you begin`**，**本页也没有实跑过任何一个套件**——
  `verified: doc-only` 指的就是这件事。
- **`Init` 之外那七个套件的「可选/必填」属性，原文没说**，本页也没敢推。

> ⚠️ **本篇的语料瑕疵四处，本页照实记下、一处都没替它改**：
>
> ① **数目自相矛盾（最实的一处）**：原文写
> `There are seven types of special test suites.`
> **紧接着列出来的条目有八个**——`Init`、`bin_disconnect`、`Abort`、`Reset`、`Pause`、
> `multi_bin_decision`、`Exit`、`Download`。**本页按实际列出的八个写**，
> 并把这句话原样留在这里。**原文没有一处解释多出来的是哪一个。**
>
> ② **`Note` 块和它前面那段粘在一起**：`…when sorting by default.Note Do not throw any exceptions…`
> ——**`default.` 与 `Note` 之间没有空格、也没有换行**，所以这句禁令在原文里是**接在上一段末尾**的。
>
> ③ **同一个启动序列写了两遍，形式不同**：`Init` 那条用 `-` 列表，
> `Download` 那条用 `1.` – `8.` 编号。**本页核对过两遍的八步文字逐字相同**，
> **只是列表符与编号的区别**——**不是内容矛盾，但确实是同一份内容被抄了两遍。**
>
> ④ **两条自指链接**：`Init` 那一条的链接指向**本篇自己**，
> `Download` 那一条指向**本篇自己的一个锚点**（`#_20281__r_Download`）。
> **原文如此，本页不判它是不是笔误。**

`verified: doc-only`
