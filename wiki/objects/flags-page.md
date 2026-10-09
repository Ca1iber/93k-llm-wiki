---
type: object
title: Flags page
layer: gui
stage: run
tags: [gui, run, flags, system-flags, testflow-flags, operation-control-window, screenshot]
related: [testflow, testflow-file, mapping-run, run, xps256-status-flags]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Flags page

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Flags page 是 SmarTest 里设 system flag 与 testflow flag 的那个界面。** 定义文档的正文一共只有 3 句散文，第一句就是它的全部身份：

> On this page, you can set the system flags and testflow flags.

**本文档正文没有一个字描述界面长什么样、有哪些 flag、值怎么给。** 本页下面写得出东西，全靠**文档自己带的那张插图**——**出处逐条标明**，请按「正文文字 / 图上的字」两路读。

### 界面的骨架：一个 `Flags` tab（**读自插图 `110705.png`，不是正文**）

| 图上看到的 | 值 |
|---|---|
| 窗口标题 | `adc_dac_x2.tfl`（**一个 `.tfl` 文件名**） |
| 表格列 | 行号 / `Flags` / `Flag Type` / `Value` |
| 底部 tab 条 | `Test Suites`、`Parameters`、`Tests`、`Bins`、`Variables`、`Flags`、`Setups`、`Information` |

**所以「Flags page」不是独立窗口，是一份 testflow 文件窗口里的一个 tab**（**推断**）：依据是①窗口标题是 `.tfl`（testflow file）文件名，② `Flags` 只是底部八个 tab 之一，③ 同一条 tab 里的 `Variables` 那一项，[[mapping-run]] 把它的归属写成 [[testflow]] 段（那页的原话是把 Variables page 与 testflow-variable 一起划给 testflow 段）。**正文没说它在哪个窗口里**——这条推论只建立在图上。

### 图里那张表：10 行，两个 flag 族并排（**逐字读自插图**）

**这是本页唯一的实质内容。** `Flag Type` 那一列恰好只有两个取值——`SYSTEM` 与 `TESTFLOW`——**与正文那句 `system flags and testflow flags` 一一对应**（**推断**：正文没有把两个族和列的取值对起来，图里这一列是唯一把两者并排的证据）。

| # | `Flags` | `Flag Type` | `Value` |
|---|---|---|---|
| 14 | `calib_age_monitor` | `SYSTEM` | `on` |
| 15 | `diag_monitor` | `SYSTEM` | `on` |
| 16 | `current_monitor` | `SYSTEM` | `on` |
| 17 | `log_events_enable` | `SYSTEM` | `on` |
| 18 | `stdf_generation` | `SYSTEM` | `on` |
| 19 | `tm_crash_as_fatal` | `SYSTEM` | `off` |
| 20 | `set_pass_level` | `TESTFLOW` | `0` |
| 21 | `set_fail_level` | `TESTFLOW` | `0` |
| 22 | `set_bypass_level` | `TESTFLOW` | `0` |
| 23 | `hold_on_fail` | `TESTFLOW` | `off` |

**三条读数限制，先写在前面，免得被当成结论**：

- **这不是全部 flag。** 图里是**第 14–23 行**，右侧滚动条说明列表更长——**前 13 行不在图里**，第 24 行以后也不在。**「flag 一共有几个」本页答不了。**
- **`Value` 一列两种写法混着用**：`SYSTEM` 那 6 行是 `on` / `off`，`TESTFLOW` 那 4 行是 `0` / `0` / `0` / `off`。**为什么不同（布尔 vs 数值？）——语料未写，本页不猜。**
- **这些字是从 PNG 上读的，不是正文文字**，所以本页**没有把它们放进 `>` 引文块**——引文块等于声称「能在 raw 文本里搜到」，而**图上的字在 raw 文本里搜不到**（§11.1）。**要复核就自己打开 `110705.png` 看**（路径见「出处」）。

### 一条运行期硬约束：**能「access」不等于能「改」**（正文 Note）

Note 的两句是一对，第一句给入口，第二句把入口砍掉一半：

> You can also access the system flags and testflow flags through the Operation Control window (via Production Settings), when running SmarTest in engineering mode (see Activating event data logging).

（末句的 `(see [Activating event data logging](<../02.10_Data_Logging/02.10.01.01.04_Activating_event_data_logging.md>))` 按 §11.1 ② 剥掉了链接标记，只留链接文字。）

> To actually make changes to the flags, all windows must be set to Testflow settings mode (not to Production settings mode) from the Operation Control window.

**条件 → 结果**：

| 入口 / 模式 | 结果 |
|---|---|
| Operation Control window → **Production Settings**（**仅 engineering mode 下**有这条路） | **能 access 这两个 flag 族**——但**不是「能改」** |
| 从 Operation Control window 把**所有窗口**设成 **Testflow settings mode** | **才能实际改 flag**（`To actually make changes`） |

**第二条写的是 `all windows`，不是「那个窗口」。** 原文还把 `(not to Production settings mode)` 用括号插在句子中间——**读这句话时那个否定是句子的主干，不是补充**。

**本页不知道的**（别指望从这里推）：flag 改完落在哪里、什么时候生效、谁读它——**语料未写**。

## 典型用法

**本文档没有 `## Procedure`，也没有 `## Before you begin`。** 全文给出的「怎么用」只有上面那条模式约束，所以本节只能到这个粒度：

1. **前置：先把模式切对。** 从 **Operation Control window** 把**所有窗口**设成 **Testflow settings mode**——否则不是「改不了」，是原文那句 `To actually make changes to the flags` 根本不成立。**这是本文档给出的唯一前置条件。**
2. **在 `Flags` tab 里改**：图上是 `Flags` / `Flag Type` / `Value` 三列（读自插图）。

**语料未写的**（这些本页一个字都没有，**别当成漏写**）：

| 问题 | 状态 |
|---|---|
| 怎么新建 / 删除一个 flag | 语料未写 |
| `Value` 怎么输入、取值范围、`0` 是什么意思 | 语料未写 |
| 改完什么时候生效（立刻 / 下次起测 / 要 flush） | 语料未写 |
| 这些 flag 在 testflow 程序里怎么读、哪条 API / 哪个命令 | 语料未写——**`Related information` 指向的三篇讲这个，本页一篇没读** |
| 图里第 13 行以上是什么 | 语料未写（不在图里） |
| Operation Control window 那条路具体怎么走 | 语料未写——原文只说「可以 access」，把细节推给 `Activating event data logging` |

## 和谁有关

**先把分层说清**——**这一条是 [[mapping-run]] 已下的裁定，不是本页源文档里的话**：**flag 在哪一级定义属 [[testflow]] 段的事，run 段只讲运行时怎么用。** 本页 `stage: run`、`layer: gui`，**是 run 段那一侧的 GUI 入口**；[[mapping-run]] 的对照表里 flags 那两行（testflow flag / test suite flag）的 GUI 一格填的就是本页。**本页不复述那张表的结论，也不把它的 L1 / L2 / L3 格子搬过来。**

- [[testflow]] — **定义侧**。flag 是什么、分几族、由谁定义——归属那一页，不归本页。
- [[testflow-file]] — **据 [[mapping-run]]**，flag 落到 testflow 文件里（那页「文件」列）。**图里有一条线索与它一致**：窗口标题是 `adc_dac_x2.tfl`（**推断**：`.tfl` 即 testflow file，所以这个 `Flags` tab 长在 testflow 文件窗口里——**正文没写这件事**）。
- [[run]] — 同 `stage` 的脊椎页；run 段的主链在那边，本页只是链上的一格。
- [[mapping-run]] — **本页的跨层对照（GUI ↔ 文件 ↔ L1/L2/L3）在那一页**；「在哪一级定义 flag」由它与 [[testflow]] 回答，**不由本页回答**。
- [[xps256-status-flags]] — **⚠️ 同名不同物，别混**：那是 **XPS256 卡的硬件状态标志**（`layer: L2` / `stage: level`），讲的是过压、过流、过热这类**卡在说话**的标志；**本页是 SmarTest 的配置开关**（`gui` / `run`）。**两者唯一的「关系」就是共用一个词。**（依据：两页的 `layer` / `stage` 与页名；**两页没有共同的源文档**。）

**源文档 `Related information` 指的三篇（本页一篇都没读）**：

| 文档 | 状态与看名字能猜到什么 |
|---|---|
| `Testflow flags`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.02_Testflow_flags.md`） | **未建页**。原文把它排在本页 Related information 第一位——**「flag 是什么」的正文很可能在它那里** |
| `Testflow flags for data logging`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.03_Testflow_flags_for_data_logging.md`） | **未建页**。名字上看是 flag 在 **data logging** 里的用法 |
| `Activating event data logging`（`02_System_reference/02.10_Data_Logging/02.10.01.01.04_Activating_event_data_logging.md`） | **未建页**。**正文 Note 里的那个 `(see Activating event data logging)` 就指向它**——即「走 Operation Control window 那条路」的细节在它那里 |

**三条链的目标文件在本机都存在**（按路径核过文件在不在，**没有打开来读**）。

## 版本

**本文档有 `## Functional changes` 段，全段一条**：

> - Introduced before SmarTest 6.3.2

**这条不能照字面读。** 它是 §11.2 ② 记的**哨兵值**：2,677 条可用性行共用这一句，措辞全是 `before`，意思是「**在本文档集覆盖范围开始之前就已经有了**」——**不是「6.3.2 新增了 Flags page」**。照字面读会得到一条格式齐整的假信息（「Flags page 引入于 6.3.2」）。

**所以**：

- **「Flags page 从哪个版本开始有」——语料未写。** 只能说到：**`SmarTest 6.3.2` 之前就已经有了**。
- **flag 本身的版本沿革（有哪些、行为怎么变）——语料未写**：本段里没有别的条目。
- **本页不把这条链到 `smartest-6.3.2` 那一页**（**建议，不是文档要求**）：链了会给那个版本页添一条不属于它的入边，而这句按定义**不描述任何版本变更**。

## 出处

**`sources:` 一篇**：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.md`（TDC `99273.htm`；**1,085 字节 / 19 行**——**本 wiki 里最薄的源文档之一**）。

**本页有两个证据面，分开记**：

1. **正文文字**：3 句散文（1 句定义 + Note 的 2 句）+ `## Related information` 的 3 条链 + `## Functional changes` 的 1 行。
   **本页的 `>` 引文块一共 4 处，全部逐字取自正文**（3 处在上文，1 处在「版本」）。
2. **插图 `110705.png`：看了。** 路径 `../../../../raw/110705.png` **在本机解析得开**，落在 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\110705.png`（9,489 字节，510 × 365；该目录共 15,025 个文件）。
   **⚠️ 这一点与 [[mapping-run]] 的一句表述不符**——那一页写「本页涉及的 GUI 文档里图片路径都向上爬四层（`../../../../raw/`），**在语料树之外**，所以本页没有任何来自图的结论」。**它对那一页的文档是否成立，本页没有复核；但本页的图就在语料树里，而且看得清。**（顺手核了另一篇的 `137362.png`，也在同一个目录里。）**如果这条对别的 GUI 文档也成立，那「图不可用」这个前提要重估——这条留给主会话，不作为本页的结论。**
   **图上读到的东西（10 行的表、窗口标题、tab 条）在上文逐处标明了出处，且一律没进引文块。**

**本页没做的**：

- **`Related information` 的三篇一篇没读**：`Testflow flags`、`Testflow flags for data logging`、`Activating event data logging`。**所以「flag 有哪些、怎么在 data logging 里用、Operation Control window 那条路怎么走」本页一个字都没有**——**这三件事的正文在那三篇里。**
- **没有 `## Procedure` / `## Before you begin` / `## Syntax` / `## Parameters` / `## Example` 任何一段**（脚本对过了：**没有段标记**），**所以「语法 / 参数」节是空的。**
  **空 ≠ 没有参数，两件事一起成立**：① 脚本在没有段标记时**一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）；② **这篇文档确实没有参数表**（正文只有 3 句话）。**要找 flag 的参数与取值，本页给不了，得去上面那三篇。**
- **除这一张插图，别的图没看**——本页只有这一张图。
- **没有实跑**。没开过 SmarTest、没进过 Operation Control window、没在机台上改过任何 flag。**`verified: doc-only` 说的就是这件事。**
- **没动 `wiki/index.md`**，也**没把本页挂进 [[run]]**。后者是**待办**：run 那页目前不知道本页存在。

### ⚠️ 语料瑕疵（照实记，一处都没替它改；§11.2）

- **① 这一篇没有坏字。** 用 §11.2 ① 的判据（`[一-鿿]`，即「英文文档里出现任何汉字都是坏字」）扫过全文：**0 处**。**本页照实记「无」**——语料整体 11.2% 的文档含坏字（`碌` = µ、`渭` = μ、`卤` = ±、`鈥慴` = `‑b` 这一类），**这一篇不在其中**，所以本页正文里没有需要说明的坏字。
- **② 插图与 Note 被挤在同一行。** raw 第 10 行的开头逐字是
  `  ![Flags page](<../../../../raw/110705.png>) Note You can also access the system flags and testflow flags`
  ——**`Note` 那个词紧贴在图片后面**（HTML 里的 Note 框与插图在转 markdown 时并成了一段），这一行还以**两个空格**开头。**所以本页引那两句时从 `You can also` 起**：`Note` 确实在原文里，只是连着图，本页没有把它抄进引文块。
- **③ `## Related information` 的三条链接首尾相连、中间没有任何分隔符。** raw 第 14 行逐字是
  `[Testflow flags for data logging](<02.08.04.32.01.02.07.03_Testflow_flags_for_data_logging.md>)[Testflow flags](<02.08.04.32.01.02.07.02_Testflow_flags.md>)[Activating event data logging](<../02.10_Data_Logging/02.10.01.01.04_Activating_event_data_logging.md>)`
  ——**渲染出来三条链接的文字会直接拼成一串**（`for data logging` 后面紧跟着下一段链接文字 `Testflow flags`）。原文很可能是列表项，转 markdown 时丢了分隔。**本页正文把三条分开写**（见「和谁有关」的表）。
- **④ 版本那一行是哨兵值，不是瑕疵本身**：`- Introduced before SmarTest 6.3.2` 属 §11.2 ② 记过的全局现象，本页正是那 2,677 条之一，**在这里点名**，处置见「版本」节。

`verified: doc-only`
