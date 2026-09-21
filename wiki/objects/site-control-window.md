---
type: object
title: Site Control Window
layer: gui
stage: run
tags: [site-control, site-state, enable, active, focus, multi-site, semi-parallel, run, debug, bad-bin]
related: [run, mapping-run, controlling-multiple-sites, site-focus-required-before-command, pqfc, test-suite, testflow-tool, results, run-dialog, alphabetical-list-of-flags]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Site Control Window

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,475 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.01_The_states_of_the_sites.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.02_Expanded_Site_Control_window.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 The states of the sites）

The menu items of the Site Control window Action > Enable all and activate all only affect those sites which are available. The figure below shows an example, where the sites 2, 3, 6, 7, 9, 10, 13 and 14 are not available.

 !`Site Control window including the unavailable sites`（raw: `../../../../raw/42587.png`）

The following figure shows the indication behavior of the check boxes in the Site Control window during a semi-parallel test.

 !`Check Boxes in Site Control Window`（raw: `../../../../raw/47565.png`）

### Example（取自子主题 Expanded Site Control window）

For example, to test sites 1 and 2 in parallel and then sites 3 and 4 in parallel for four-site semi-parallel testing, you can set up the test sequence by specifying Size = 2 and Cycle = Unbounded. Each parallel test in the semi-parallel test will be executed from the group including site 1 in numerical order.

If test sites are added afterward, additional sites will be tested according to the Size and Cycle settings. Therefore, you do not have to set up this again.

The figure below shows three examples of the site test sequence settings including the above typical example.

 !`Size and Cycle Parameters`（raw: `../../../../raw/47559.png`）

You can also enter the order numbers directly into the Site Test Sequence field. Hence, you can set up a free site test sequence. In this case, if test sites are added afterward, additional sites will be tested in parallel after tests of the existing sites are completed.

The Parallel and Serial buttons can be used to change the site test sequence from Semi-Parallel or free sequence to the Parallel or Serial sequence.

Note If you turn the `Allow Parallel`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_allow_parallel`） flag off, all sites will be tested serially. However, the sequence might be different from the sequence specified by clicking the Serial button. For example, if you click the Semi-Parallel button and run the test suite in the following sequence as sites 1 and 3 (in parallel), and site 2 and site 4 (in parallel), then after you turn off the Allow Parallel flag, the site test sequence is site 1, site 3, site 2, and site 4. However, for the serial test (the Allow Parallel flag is turned on and the Serial button is pressed), the site test sequence is site 1, site 2, site 3, and site 4.

TIP: You can also set up the site test sequence for all test suites in the Site Control window. If you want to set it up for many test suites once, it is better to use the Site Control window.

<!-- 语法节 end -->

## 是什么

**Site Control window 是「每个 site 现在处在什么状态」那张控制面板**——
多 site testflow 调试时，用它挑哪些 site 跑、看哪个 site 被 focus。
`layer: gui` / `stage: run`：它管的是**运行那一段里「site 这一维」**。
打开路径原文逐字是 `93000 > System > Site Control`（SmarTest Work Center 菜单）。

原文把它存在的理由写成一句：

> 「To debug a multi-site testflow, you need to identify passing and failing sites and view the results of individual site in the result tools.」

**这一句里有两个动作，方向不同**：① **认出**哪些 site 过、哪些不过；② **在结果工具里看单个 site 的结果**。
**而窗口自己干的是另外两件事**：

> 「You do this with the Site Control window (the SmarTest Work Center menu 93000 > System > Site Control), which allows you」

> 「- to set the state of each site .」

> 「- to stimulate the behavior of the site setups, which is usually done by the prober/handler library.」

| 原文条目 | 读出来的 |
|---|---|
| `to set the state of each site .` | **设每个 site 的状态**——这一项是窗口自己的功能 |
| `to stimulate the behavior of the site setups, which is usually done by the prober/handler library.` | **模拟 site setup 的行为**——注意这半句说的是**通常由 prober/handler 库来驱动**，不是窗口自己算出来的 |

**第二条是本页最容易被读错的一格**：原文把它写成窗口的一项能力，
**但同一句里又说明了这件事平常是谁在做**——**prober / handler 库**。
「不给真实 prober 时窗口可以代它一下」这层意思**原文没有明写**，本页不替它补。

### 它长什么样：小版是「site 号 × 状态名」的复选框矩阵（图证）

> 「The screenshot above shows the small version of the Site Control window. For the expanded view, refer to Expanded Site Control window.」

**原文把窗口分成「小版」与「expanded 版」两种形态，而 expanded 版的长相不在本页**（在子主题 `27.02` 里，
**本页没读**，`refer to` 那一条就是它）。

小版的样子，图 `21624.png` 上逐字是：

- 标题栏 `Site Control`；菜单栏三项：`Action` / `Doc` / `Edit`；
- 中间是一张**矩阵**：**列头是 site 号**（`1` `2` `3` `4`），**行头是三个状态名**——
  `enable` / `active` / `focus`；
- 每一格是一个复选框（绿色实心 = 勾上）；
- **`focus` 那一行只有一格勾着，而那一格外面另画了一个黑框**——**当前 focus 的 site 在图上是有记号的**。

**列数 = site 数**（图证）：小版那张是 **4** 列；同一族的 `42587.png` 是 **16** 列；
下面那张 `47565.png` 里并排的五张小窗各是 **4** 列。**没有一张图里出现「固定列数」的痕迹。**

**grep 不到的字**：`enable active focus` 三连（0 命中）、`Site#`（0 命中）——
**三个状态名单独都能在别处搜到，但「它们排成这张表的行头」只有图上看得见。**

### 三个状态名里，`focus` 是唯一在图上被解释的那个（图证）

`47565.png` 里有一个提示框，逐字是：

> 「The site in focus is automatically switched depending on the current situation in the test. You can also set a focus site.」

**这句话答掉了本页最大的一个疑问：`focus` 是谁在动。** 两件事：
**① 它会跟着测试的当前情况自动切；② 你也可以自己设一个。**
（`enable` 与 `active` 各自的定义，本页**没有**——那两个在子主题 `27.01` 里，**本页没读**。）

### `Size` 与 `Cycle`：semi-parallel 怎么排（图证）

本页「语法 / 参数」节里引自子主题 `27.02` 的那段给了 `Size` / `Cycle` 的用法，
而图 `47559.png` 把三个取值摆成三个面板，**每个面板下面直接写出它排出来的测试顺序**：

| 面板 | `Size` | `Cycle` | 图上 site 列里的组号 | 图上写出的测试顺序 |
|---|---|---|---|---|
| 1 | `2` | `unbounded` | `1 1 2 2`（site `#1`–`#4`） | `1. Parallel Test on Site 1 & 2` / `2. Parallel Test on Site 3 & 4`；右栏追加的四 site 是 `3 3 4 4`，序列续 `3. Parallel Test on Site 5 & 6` / `4. Parallel Test on Site 7 & 8` |
| 2 | `2` | `4` | `1 1 2 2` | `1. Parallel Test on Site 1 & 2 & 5 & 6` / `2. Parallel Test on Site 3 & 4 & 7 & 8`（右栏 site `#5`–`#8` 也是 `1 1 2 2`） |
| 3 | `1` | `2` | `1 2 1 2` | `1. Parallel Test on Site 1 & 3 & 5 & 7` / `2. Parallel Test on Site 2 & 4 & 6 & 8` |

**从这张图读出来的两条（推断，依据是三个面板里 `Size` / `Cycle` 的取值与组号序列的对应）：**

- **`Size` = 一组并行几个 site；`Cycle` = 组号每多少格回到 1。**
  `Cycle = unbounded` 时组号一直往上加（第 1 面板追加后变成 `3 3 4 4`）；
  `Cycle = 4` 时组号在第 5 格回到 1，**于是 site 5 / 6 与 site 1 / 2 落进同一组、一起并行**
  （第 2 面板那句 `Site 1 & 2 & 5 & 6` 就是结果）。
- **等价的算法是「并行组的个数 = `Cycle` ÷ `Size`」**：4÷2=2、2÷1=2，两组；
  `unbounded` 的那一档不封顶，**site 一多就多开一组**。
  原文（本页语法节引的那段）只说 `Size = 2 and Cycle = Unbounded` 这个典型例子的效果，
  **没有把这条换算写出来**——**它是本页从图上算的**。

**grep 不到的字**：`Parallel Test on Site`（0 命中）——**图上那三组编号序列行，语料里一处都没有**。
（`Size` / `Cycle` / `unbounded` / `Site Test Sequence` 这些**词**能搜到，在 `27.02` 的正文里
——**所以这张图的图证价值在「取值 → 组号序列」这一层，不在那些词本身**。）

### 一张图看完整条 semi-parallel 的机制（图证）

`47565.png` 不是窗口截图，是一张**过程示意图**，把「一轮半并行测试里 site 状态怎么变」画了五格：

- 上半是两个灰框 `Testsuite "1"` 与 `Testsuite "2"`；中间一条标 `P` 的箭头带 `Site 1/2/3`，
  一条标 `F` 的箭头带 `Site 4`、指向一个粉色的 `Bad Bin` 框；
- 中间是 `Site 1` ~ `Site 4` 四行，每行五个时间步的 DUT 板图标；
- 右下角图例三条：`Connected and active` / `Connected and masked` / `Disconnected`
  ——**`masked` 与 `Disconnected` 是两个不同状态**，这一点**正文里没有**；
- 底下并排五张小号的 Site Control 窗（各 `1 2 3 4`，含 `enable` / `active` / `focus` 三行），
  跟着时间步变——**第 1 面板里那个提示框指的就是这五张小窗在动这件事**
  （提示框逐字是 `The site in focus is automatically switched depending on the current situation in the test.`）。

**grep 不到的字**：`Connected and active`（0 命中）、`Connected and masked`（0 命中）、
`The site in focus is automatically switched`（0 命中）。
（`Bad Bin`、`Disconnected` 两个串**能搜到**，**但搜到的是别处的正文，不是这张图**。）

### 一条 `Action` 菜单的行为（本页语法节引的那段）

本页「语法 / 参数」节里引自 `27.01` 的那段写了 `Action` 菜单里两项的一个限制：
`Action > Enable all` 与 `activate all` **只作用于 available 的 site**，
并且给了一个例子（`the sites 2, 3, 6, 7, 9, 10, 13 and 14 are not available`）。
**「哪些 site 算 available、为什么不可用」在 `27.01` 里，本页没读**——
本页只知道**这两个菜单项不是对每个 site 都生效**。

## 典型用法

**本页的源文档只有 24 行、1,201 字节**：它**没有 `## Procedure`，也没有 `## Before you begin`**，
连一句「先点哪里再点哪里」都没有。所以下面这张表**只能到「在哪一栏做什么」**，
**「怎么一步步点」本页给不出，也不替它编**。

| 想干什么 | 在哪 | 依据 |
|---|---|---|
| 打开这个窗口 | SmarTest Work Center 菜单 `93000 > System > Site Control` | 文档事实 |
| 让某些 site 跑、其余不跑 | `enable` 那一行（**一次设一个 site 的状态**） | 文档事实（`to set the state of each site`）+ 图证（行头 `enable`） |
| 看哪些 site 正在参与 | `active` 那一行 | 图证（行头）+ 图 `47565.png` 里的 `masked` / `Disconnected` 两状态 |
| 换 focus site | `focus` 那一行；**它也会自己切** | 图证（`You can also set a focus site.` 与 `is automatically switched`） |
| 给一批 site 一次性 enable / activate | `Action` 菜单 → `Enable all` / `activate all`（**只对 available 的 site 生效**） | 本页语法节引的 `27.01` 那段 |
| 设 site 测试顺序（semi-parallel 的 `Size` / `Cycle`） | **小版窗口里没有**——在 expanded 版 / test suite 那一侧 | 本页语法节引的 `27.02` 那段（**TIP 说：「想一次给很多 test suite 设」，用 Site Control window 更好**） |

**两条顺序上的提醒（推断）：**

- **先 enable，再谈跑不跑。** 图 `21624.png` 里三行的次序就是 `enable` → `active` → `focus`
  ——**先可用、再参与、再聚焦**。**原文没有把这三次序说成流程**，这一条是**本页按图上的行序排的**。
- **`Allow Parallel` 那个 flag 会覆盖你在这里设的顺序。** 本页语法节引的 `27.02` 那段有一段
  `Note` 专门讲这件事（关掉 `Allow Parallel` 之后，实际顺序可能与按 `Serial` 按钮得到的顺序不同，
  原文给了一个 `site 1, 3, 2, 4` 对 `site 1, 2, 3, 4` 的例子）。
  **那条 flag 自己的页本页没读**——它列在 `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags` 里，
  那是 [[alphabetical-list-of-flags]] 的地盘。

## 和谁有关

- [[run]] / [[mapping-run]] — **本页的 stage 页与同阶段对照表页。**
  [[mapping-run]] 主表第 8 行「选 site / 改 focus site」的四格是
  **GUI `[[site-control-window]]` / 文件 `?` / L1 `PQFC` / L2 [[controlling-multiple-sites]]**，
  L3 那格是它的（推断）`setSiteInFocus()` / `setActiveSites()`。
  **本页只负责那一行的 GUI 格**——`PQFC` 怎么用、L2 那篇说什么，**本页一个字没有**。
- [[controlling-multiple-sites]] — **同一个动作的 L2 侧**（原文 `Controlling Multiple Sites`，`02.07.03.13`）。
  **那条链接是 [[mapping-run]] 记的**（它引 `27.03`）：**`27.03` 本页没读**，所以本页不据它填任何格子。
- [[pqfc]] — **L1 侧的「选 site / 改 query focus」命令**。**同样是 [[mapping-run]] 记的**，
  本页没读它的命令页，**参数与返回值本页没有**。
- [[site-focus-required-before-command]]（**已建的 constraint 页**）— **本页是那条约束的 GUI 面**：
  约束说「某些动作前必须先确定 focus site」，而**本页的 `focus` 那一行就是设 focus 的地方**。
  **那条约束的原文依据在它自己页里，本页不重复。**
- [[test-suite]] / [[testflow-tool]] — **site 测试顺序其实有两个设置场所**，
  本页语法节引的那段 `TIP` 明说：
  「想一次给很多 test suite 设，用 Site Control window 更好」——
  **也就是说另一个场所（test suite 那一侧）是更细粒度的入口**。
  **那一侧的工具页本页没读。**
- [[results]] — 原文第一句的后半截是「**在结果工具里看单个 site 的结果**」
  ——**所以本页与 results 段是「选 site」与「看这个 site 的结果」的分工**。
- [[run-dialog ]] — [[mapping-run]] 从 `119959.png` 读到 Run dialog 的 `Main` 页里有一项
  `Site in Focus (for selection of test suites only)`。**那是 Run dialog 那一头，本页没读**；
  **两个入口是不是同一件事，本页不判。**
- [[alphabetical-list-of-flags]] — 本页语法节引的那段 `Note` 里的 `Allow Parallel` flag 列在它那儿。
  **那页不是本页建的**，这里只指路。

## 版本

**本文档没有 `## Functional changes` 段。**

这是**事实，不是缺陷**：源文档一共 24 行，`##` 段只有 `#### Subtopics` 与 `## Site Control Window`
（正文本身没有二级节），**结尾停在 `refer to Expanded Site Control window` 那两句上**。

**所以这一页答不了版本问题**：

- **Site Control window 是哪个版本有的、后来加过什么**——**本篇没写**；
- **「小版 / expanded 版」是哪个版本分成两种形态的**——**本篇没写**；
- 它的**四篇子主题**（`27.01` / `27.02` / `27.03` / `27.04`）**本页一篇没读**，
  **所以「那四篇里有没有版本段」本页也不知道。**

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.md`
  （TDC `100118.htm`，**1,201 字节 / 24 行**——是本批对象页 sources 里最短的一篇）。
- **本篇没有重复投放**：全语料按 `source_topic` 查 `100118.htm`，**只有这一个文件**。

### 本页「语法 / 参数」节的来源（**那一节不是定义文档写的**）

- **定义文档里没有语法段标记**（没有 `Syntax` / `Parameters` / `Example` / `Procedure`）。
- 那一节的 **2,475 字符全部来自两个子主题**（来源写在段名里，脚本在节首自己声明了）：
  `02.08.04.27.01_The_states_of_the_sites`、`02.08.04.27.02_Expanded_Site_Control_window`。
- **那两篇子主题本页一篇都没读。** 所以本页正文里凡用到它们的内容，
  **都只用到「它们已经出现在本页语法 / 参数节里的那两小段 + 它们自带的图」**，
  **没有展开**——那两篇里的 `## Procedure`、`Before you begin`、以及别的段落本页都不知道。

### 本页读的图（4 张）

- **sources 那篇引的图 1 张，本页读了 1 张**：`21624.png`（小版窗口）。
- **另读了 3 张本页「语法 / 参数」节里出现的图**：`42587.png`、`47565.png`、`47559.png`
  （各自出自哪个子主题见上面各节）。
- **没读的 2 张**：`47564.png`（出自 `27.02`）与 `47454.png`（出自 `27.03`）。
  **那两篇子主题文档本身也没读**——**四篇子主题引的图一共 6 张（去重后），本页看了 4 张。**
- **4 张都整张看完**，图上读到的字**逐条回 9,398 篇 raw md 里查过 grep 命中**——
  本页凡写「grep 不到」的都是实测 0 命中。

### 本页没做的

- **四篇子主题一篇没读**：`27.01_The_states_of_the_sites`、`27.02_Expanded_Site_Control_window`、
  `27.03_Changing_the_site_in_focus`、`27.04_Selecting_the_sites_to_run_your_test`。
  因此下面四件事**本页一个字没有**：**`enable` / `active` / `focus` 三个状态各自的定义**、
  **expanded 版窗口长什么样**、**怎么改 focus site**、**怎么选要跑的 site 的完整步骤**。
- **`Changing the site in focus` 那篇明链的三篇没读**：`Controlling Multiple Sites`（L2）、
  `Site dependent firmware commands`、`Defining the query focus`（L1）——
  **那三条链接是 [[mapping-run]] 记的，本页只转述「有这三条链」，没有回原文复核。**
- **没有实跑。** 没有在机台上开过 Site Control window、没有 enable / disable 过任何 site、
  没有跑过 semi-parallel 测试。**`verified: doc-only` 指的就是这件事**——
  「这台机器上哪些 site 算 available、按 `Enable all` 会怎样」本页一句都不能保证。
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[run]] 那页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 句号前面多一个空格（第 19 行）。** 原文逐字是：

> 「- to set the state of each site .」

**`site` 与 `.` 之间有一个空格。** 这条能力清单**只有两行**，**另一行没有这个毛病**。
**引文里原样保留**（本页正文引了这一句）。

**② 一处数不一致：`the results of individual site`（第 15 行）。**

> 「To debug a multi-site testflow, you need to identify passing and failing sites and view the results of individual site in the result tools.」

**`individual site` 前面没有冠词、后面没有复数**（同一句前半截用的是 `sites`）。
**原文如此，本页照录不判**——它指的是「单个 site」还是「各个 site」，**本页不替它定。**

**③ 本页这一篇没有编码坏字（§11.2① 那一族）。** 用 `[一-鿿]` 实测零命中
——对照 §11.2① 的全语料 1,053 / 9,398 篇含坏字，**本篇属于没有的那一批**。
**这不是「没找到」，是查过、结果为零。**

**④ 本篇没有 §11.2⑤ 那个整词替换（`DC/DC power units`）**，实测 0 命中。

**⑤ 一条不是瑕疵、但必须说明的结构事实**：本页的源文档**只有 24 行**，
**它的「内容」几乎全在四篇子主题里**（本页语法节那 2,475 字符就是从其中两篇抄来的）。
所以本页**正文比同批其它对象页短**——**这是语料的分工如此，不是本页漏写**。

`verified: doc-only`
