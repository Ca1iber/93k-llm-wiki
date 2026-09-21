---
type: object
title: Pattern Explorer
layer: gui
stage: pattern
tags: [pattern, pattern-explorer, gui, pattern-master-file, multiport-burst, port-burst]
related: [pattern-tool, pattern-editor, multiport-burst-editor, pattern-master-file, pattern, mapping-pattern]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Pattern Explorer

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,555 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.06_Cloning_a_pattern.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.07_Moving_or_copying_pattern_files.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.08_Deleting_pattern_files.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.14.01_Moving_vectors_to_another_memory_type.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Cloning a pattern）

The following examples explain the transformation to NOP instructions in more detail.

- For the instruction `SSRC dsm_data_pattern`, if the port of the pattern `dsm_data_pattern` is also the port of the target pattern, the `SSRC` instruction is cloned to the target pattern without change.
- For the instruction `JSUB sub_pattern`, as the port of the pattern `sub_pattern` is not the same as that of the source pattern, in the target pattern, the `JSUB` instruction is replaced by an `NOP` instruction and a warning message is displayed on the console tab.

If an instruction is replaced by `NOP` in the target pattern (for example, the `JSUB sub_pattern` instruction), you must modify the instruction manually:

- Create a new subroutine pattern `sub_pattern_clone` by cloning the `sub_pattern` pattern with the port of the target pattern.
- Replace `NOP` with the `JSUB` instruction using the new pattern: `JSUB sub_pattern_clone.`

### Example（取自子主题 Moving or copying pattern files）

Update of pattern master file when moving `pattern 4` from the `patterns_a` folder to the `patterns_b ` folder`:`

 |

Before

 |

After

 |
 |

```
hp93000,pattern_master_file,0.1
 
path:
  ../data/patterns_a
 
files:
  pattern1
  pattern2
  pattern3
  pattern4
 
path:
  ../data/patterns_b
 
files:
  pattern5
  pattern6
```

 |

```
hp93000,pattern_master_file,0.1
 
path:
  ../data/patterns_a
 
files:
  pattern1
  pattern2
  pattern3
 
path:
  ../data/patterns_b
 
files:
  pattern4
  pattern5
  pattern6
```

 |

### Example（取自子主题 Deleting pattern files）

"Cannot delete ..." error message:

 !`Error: Cannot delete because referenced ...`（raw: `../../../../raw/129371.png`）

Confirmation dialog:

 !`Confirm Delete dialog`（raw: `../../../../raw/129372.png`）

### Usage（取自子主题 Editing properties in the Pattern Explorer › Moving vectors to another memory type）

The general format of the call is:

conv_vector -target <option><source_file><target_file>

<option> will usually be

- SM for conversion to SM or
- VM for conversion to VM

Rules:

- If you use port names in your vector file you must also specify a pin configuration file with the option -p.

You may specify a pin configuration file in any case.

- conv_vector does not accept a pattern master file.
- When the source file came from a single-density (SD) V93000 system, you must use the -sdvectors option.

For more details, type conv_vector without any parameters:

```
Tool to convert the vector file to the specified target format
conv_vector Revision: 5.4.33 (26-May-2017)
conv_vector [options] source-file [dest-file]
Converts the vector file <source-file> to the specified target format
and writes it to <dest-file> or stdout if no <dest-file> is specified.
-target <str>   The conversion target; one of MCU, C200...P1000, F330,
                SM(Sequencer Memory), VM(Vector Memory), UMM (Unified Memory Mode), SHMEM(Shared Memory)
-quiet          Warnings and messages are suppressed
-log <str>      All messages are written to a log file
-compress       The resulting vector file is compressed
-novectors      No vector data is emitted
-noscan         Scan vectors and labels containing scan calls are removed
-nomemtest      Memory tests are removed
-toascii <str>  Print waveform DC/DC power units of specified label and pin
-reorder        Puts SQPG's directly after defining label
-escan2 <str>   Pins in external scan memory with 2 bit/vector
-escan4 <str>   Pins in external scan memory with 4 bit/vector
-p <str>        Pin Configuration File
-keep           The resulting vector file will not be removed in case of error during conversion
-sdvectors      Source vector file originates from a V93000 Single Density (SD) test system.

```

### Example（取自子主题 Editing properties in the Pattern Explorer › Moving vectors to another memory type）

conv_vector -target SM -p pins_soc pattern_vm pattern_sm

<!-- 语法节 end -->

## 是什么

**Pattern Explorer 是「这套 setup 里有哪些 pattern」的那张总表，也是进入各种 pattern 编辑器的入口。**
它住在 SmarTest Work Center 里（原文说那条状态行在 `the bottom of the work center`），
`layer: gui` / `stage: pattern`——管的是 pattern 这一段**看得见、点得动的那一层**。

原文对自己能力的清单只有一句引导语：

> 「With the Pattern Explorer you can:」

| 原文条目 | 做什么 |
|---|---|
| `explore the patterns contained in the loaded setup,` | 看**载入的** setup 里有哪些 pattern |
| `create new patterns, port bursts, and multiport bursts,` | 建 pattern / port burst / multiport burst |
| `delete patterns,` | 删 pattern |
| `load and save selected patterns (see note below),` | 载入与保存选中的 pattern（**有前提**，见下） |
| `start pattern editors and multiport burst editors,` | 启动 Pattern Editor 与 Multiport Burst Editor |
| `edit bursts.` | 编辑 burst |

### 一条硬前提：load/save 看的是「怎么载入的」，不是「选中了什么」

> 「Loading and saving selected patterns requires that they were loaded via a pattern master file. This feature is not available for standard pattern setup files.」

**这是本页最有用的一句**，它把上面第四条能力劈成两半：

| 这批 pattern 是怎么载入的 | `load and save selected patterns` |
|---|---|
| 经 **pattern master file** 载入 | 可用 |
| 标准 **pattern setup file** 载入 | **原文：`This feature is not available`** |

所以「为什么这个功能点不动」的答案**在载入方式上，不在选中项上**。
原文没写不可用时界面上是变灰、隐藏还是报错——它只写了 `not available`。

### 工具栏上还有一条同样的界：只有 pmfl 才亮的四个图标

> 「The icons below are active for pattern master files (*.pmfl) only.」

**同一个门槛在工具栏上又出现一次**（扩展名原文写 `*.pmfl`）。
这说明 pattern master file 在本页不是「另一种存法」而已，而是**一类功能的开关**：
它同时决定 load/save 能不能用、以及工具栏上那四个图标活不活。

### 两区结构：主区是「有什么」，细节区是「选中的长什么样」

> 「The Pattern Explorer consists of two areas: the main area and the details area. The main area lists all patterns of the loaded setup file.」

> 「The content of the details area is context sensitive and depends on the selection in the main area. When there is nothing to display, it shows an instruction message.」

**细节区的内容跟着主区的选中走**，而且**没有固定内容**：没东西可显示时它给一句提示语。
**细节区到底显示哪些字段，这一篇没有列**——本页能说的到此为止。
那一块在子主题 `16.01.14_Editing_properties_in_the_Pattern_Explorer` 一线，**本页没读**。

原文另有一句 `The figure below shows a pattern master file in the folder-oriented view mode.`
——说明**「文件夹 / 文件视图」是一种显示模式**（对应下面工具栏的 `Show Folder in Hierarchy`）。
**那张图本页没看**，所以这个视图长什么样、和 pattern 视图差在哪，本页不知道。

### 状态行：两处原文措辞不同，一起照录

> 「The status line at the bottom shows the selected item, the row number and the total number of rows.」

> 「The status line at the bottom of the work center shows the selected item, the row number of the selected cell, and the total number of rows. For example, for a top most cell (below the filter cell) the row number indicator could show 1 / 200, that is row 1 of 200 rows in total. For a filter cell the status line would show Filter / 200.」

**其一**：`the row number`（开头那处）对 `the row number of the selected cell`（`## Status line` 那处）；
`at the bottom` 对 `at the bottom of the work center`。**两处并列记下，本页不替它统一。**

**其二**：后一句多给了三件事，都是能直接用的：

| 原文 | 读出来的 |
|---|---|
| `1 / 200` + `row 1 of 200 rows in total` | 那个数字是**「第几行 / 共几行」**，不是行 ID |
| `below the filter cell` | **最上面那一格是过滤单元格**，数据从它的下一行开始 |
| `Filter / 200` | 选中过滤单元格时，行号那一格显示的是 `Filter` |

**过滤怎么用**在子主题 `16.01.13_Sorting_and_filtering_the_pattern_table` 里，**本页没读**。

### 工具栏图标：五个通用的 + 四个 pmfl 专属的

`## Icons` 一节一共给了 9 个工具栏图标。前五个任何 setup 都能用：

| 图标 | 做什么 | 原文要点 |
|---|---|---|
| `Link with Editor` | 让选中与**活动编辑器**联动 | 选中后换编辑器，选择**自动**更新到正在编辑的资源 |
| `Show Executed Pattern` | 高亮**最后执行过的**那个 pattern | — |
| `Go to Row (Ctrl + L)` | 跳到指定行 | **快捷键 `Ctrl + L`** |
| `Pin Details Area` | **锁住细节区** | 主区选中变了，细节区**也不换内容**；原文说编辑 burst 时有用 |
| `View Menu` | 布局与首选项 | 三个子菜单，见下 |

后四个只在 pattern master file 下才活（就是上面那句 `*.pmfl` 划的界）：

| 图标 | 做什么 |
|---|---|
| `Show Folder in Hierarchy` | 在**文件夹 / 文件视图**与 **pattern 视图**之间来回切 |
| `Show Multiport Burst in Hierarchy` | 开关 multiport burst 层次的显示 |
| `Expand All` | 展开整棵层次 |
| `Collapse All` | 折叠整棵层次 |

三句原文逐字引在这里（第一句讲视图模式，后两句是本页下面要拿来对比的两个开关）：

> 「Show Folder in Hierarchy: Toggles between folder/file-oriented view mode and pattern-oriented view mode.」

> 「Link with Editor: Toggles whether the Pattern Explorer selection is linked to the active editor. When this option is selected, changing the active editor will automatically update the Pattern Explorer selection to the resource being edited.」

> 「Pin Details Area: Locks the details area, when the selection in the main area is changed. Useful when editing bursts.」

**(推断) 容易看混的一处：这两个开关的「联动」联的是不同的两头。**
`Link with Editor` 让 **Pattern Explorer 的选中跟着活动编辑器走**；
`Pin Details Area` 让 **细节区不跟着主区的选中走**——一个让显示动，一个让显示不动。
**依据是两句原文的主语**：前者联的是 `the active editor` 与 `the Pattern Explorer selection`，
后者冻的是 `the details area` 与 `the selection in the main area`。
**原文没有把两者放在一起讲**，这条对应关系是本页排的。

`View Menu` 的三个子菜单：

| 子菜单 | 项 | 效果 |
|---|---|---|
| Layout | `Vertical View Orientation` | 细节区在主区**下面** |
| | `Horizontal View Orientation` | 细节区在主区**右边** |
| | `Automatic View Orientation` | 按 Pattern Explorer 的**高宽比**自动排 |
| | `Pattern Main Area Only` | **只显示主区** |
| Show in Hierarchy | `Folder` | 显示文件夹 / 文件层次（原文：同 `Show Folder in Hierarchy`） |
| | `Multiport Burst` | 显示 multiport burst 层次（原文：同 `Show Multiport Burst in Hierarchy`） |
| Preferences | — | 打开 preferences 对话框——**Pattern Explorer 与 Pattern Editor 共用** |

最后那一格是本页与 Pattern Editor 之间最硬的一条关系（原文逐字）：

> 「Opens the preferences dialog for the Pattern Explorer and the Pattern Editor.」

### 主区图标：一眼看状态

主区里 12 个图标，把原文的说明逐条摊开就是这张表——**这是本页最实用的一张**：

| 图标（原文 alt 文字） | 原文说明 |
|---|---|
| `Folder` | `A folder.` |
| `Modified folder` | `A modified folder.` |
| `Pattern` | `A pattern.` |
| `Selected pattern (not loaded)` | `An initialized, but not loaded pattern (icon, pattern name, etc. are grayed out.)` |
| `Modified pattern` | `A modified pattern.` |
| `Pattern with results` | `The current primary pattern.` |
| `Multiport burst` | `A port burst (type = PortBurst).` |
| `Modified port burst` | `A modified port burst.` |
| `Port burst with results` | `The current primary port burst.` |
| `Show Multiport Burst in Hierarchy` | `A multiport burst (type = MPBurst).` |
| `Modified multiport burst` | `A modified multiport burst.` |
| `Multiport burst with result` | `The current primary multiport burst.` |

**(推断) 这 12 行其实是一张 3 × 3 的表**：pattern、port burst、multiport burst **每一类都配三种状态**
——**普通**（原文是 `A folder.` / `A pattern.` 这一族）、**改过**（原文在名词前加 `modified`）、
**当前 primary**（原文作 `The current primary` 再接名词）；
文件夹另占两行（普通 / 改过）。
**依据**：12 行说明文字的措辞本身——`modified` 与 `current primary` 两组词各自出现三次。
**原文没有把这条规律写出来**，它是本页从措辞里读出来的。

**原文自己给的两个类型名值得单独记**：port burst 那行写 `A port burst (type = PortBurst).`，
multiport burst 那行写 `A multiport burst (type = MPBurst).`——
**主区的行知道自己是什么类型**，而**这一篇里出现的类型名只有这两个**。

**一条边界**：`The current primary pattern.` 只说明**图标能显示哪个是 primary**。
**这一篇里没有任何「设置 / 切换 primary」的动作**，所以本页不据这一句说 GUI 能改 primary
（口径与同阶段的 [[mapping-pattern]] 一致）。

**另一行值得单独看**：`An initialized, but not loaded pattern (icon, pattern name, etc. are grayed out.)`
——**「已初始化」和「已载入」在这里是两个状态**（推断：否则不会出现「初始化了但没载入」这一行；
依据就是这行说明文字本身）。**这两个动作在哪做，本篇没写。**

## 典型用法

**这一篇是参考页，不是步骤页**：它没有 `## Procedure`，也没有 `## Before you begin`。
下面能拼出来的操作**全部来自 `## Icons` 一节的图标说明**——所以每一条都只到「按哪个图标」为止，
**「先做什么再做什么」的完整流程在这一篇里没有，本页也不替它编**。

| 想干什么 | 按什么 | 依据 |
|---|---|---|
| 看另一个 pattern 的细节 | 在主区**选中它**——细节区自动跟着变 | 文档事实（两区结构那两句） |
| 换选中时**不让**细节区跟着变 | `Pin Details Area` | 文档事实 |
| 跳到第 N 行 | `Go to Row`（`Ctrl + L`） | 文档事实 |
| 让选中跟着活动编辑器走 | 打开 `Link with Editor` | 文档事实 |
| 找最后跑过的那个 pattern | `Show Executed Pattern` | 文档事实 |
| 换布局（细节区在下 / 在右 / 只留主区，或让它按高宽比自己排） | `View Menu` → `Layout` | 文档事实 |
| 在文件夹视图与 pattern 视图之间切 | `Show Folder in Hierarchy`（**仅 pmfl**） | 文档事实 |
| 看 / 收 multiport burst 层次 | `Show Multiport Burst in Hierarchy`（**仅 pmfl**） | 文档事实 |
| 整棵层次一把展开 / 收起 | `Expand All` / `Collapse All`（**仅 pmfl**） | 文档事实 |
| 改这一页与 Pattern Editor 的首选项 | `View Menu` → `Preferences` | 文档事实 |

**上面那张表最右边一列全是「文档事实」，因为每一行都是原文对那个图标的一句说明。**

**能力清单里那六条（建 / 删 / 载入 / 保存 / 启动编辑器 / 编辑 burst）只说「能做」，没说按哪里。**
它们的操作步骤在 15 篇子主题里，**本页一篇没读**——这是本页与「怎么用」之间最大的缺口。

**一条顺序上的提醒（推断）**：因为 load/save 与那四个工具栏图标都挂在 `*.pmfl` 上，
**开工前先确认手里这套 setup 是经 pattern master file 载入的**——它决定后面一半操作可不可用。
**依据**：上面两条 `*.pmfl` 门槛（load/save 的那条 note 与工具栏那句）。
**原文没有把「先确认载入方式」写成一条建议**，这一步是本页排的顺序。

## 和谁有关

- [[pattern-tool ]] —— **父页**。本页是 `02.08.04.16_Pattern_Tools.md` 下的子主题之一，
  那一篇链到本页（`extract/edges.jsonl`）。**那一篇本页没读**，父子关系来自本页的 `Subtopics` 清单与这条入边。
- [[pattern-editor ]] —— **同章兄弟，且与本页共用设置**。原文 `## Related information` 第一个就是它；
  更硬的证据是 `View Menu → Preferences` 那一句里写着
  `for the Pattern Explorer and the Pattern Editor`。
  **分工**：本页答「有哪些 pattern」，它答「pattern 里面长什么样」——
  **`Instruction` 列、sequencer instruction、GUI 与 L1 的指令名差异全在它那边**；
  本页的源文档里**一个指令名都没有**。
- [[multiport-burst-editor ]] —— **本页是它的入口之一**：能力清单里有
  `start pattern editors and multiport burst editors`；本页 7.1.3 那条版本记录也是为 multiport burst 加的。
- [[pattern-master-file]] —— **前置关系，不是并列**。它不只是「pattern 的另一种存法」：
  `*.pmfl` 决定本页的 load/save 能不能用、以及工具栏那四个图标活不活。
- [[pattern]] —— 本页的 `stage` 页。**pattern 定义侧**（label 是什么、有哪些类型）在那边，不在本页。
- [[mapping-pattern]] —— **同阶段的对照表页，本页是它 GUI 列的一个来源**。
  三层（GUI / 文件 / L1）怎么对、**GUI 与 L1 的指令名哪里不同**，**一律记在那一页**
  （包括 `LOOP`/`LOOPEND`/`RETURN` 对 `LBGN`/`LEND`/`RSUB`、`GENV` 在 GUI 侧隐式那几条）；
  本页不重复、也不改它的口径。**本页的源文档对这套三层对照一个字都没写。**
- **子主题 15 篇**（本页 `Subtopics` 全列）：本页「语法 / 参数」节里有其中 **4 篇**的片段
  （`16.01.06_Cloning_a_pattern`、`16.01.07_Moving_or_copying_pattern_files`、
  `16.01.08_Deleting_pattern_files`、`16.01.14.01_Moving_vectors_to_another_memory_type`）——
  **是脚本抄的，不是本页写的**；**这 15 篇本页一篇都没读**（见「出处」）。
- **从别的阶段链过来的**（`edges.jsonl` 入边 19 条 / 18 篇，「链到本页」这一条事实取自它）：
  `Using the Trace Function`（raw: `02_System_reference/02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.md`）、
  `Principles of operation of the Integrated Result Tool`（raw: `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.01_Principles_of_operation_of_the_Integrated_Result_Tool.md`）、
  `FFC Pareto chart view`（raw: `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.04.06_FFC_Pareto_chart_view.md`）、
  `Function of the base wavetable`（raw: `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05.01_Function_of_the_base_wavetable.md`）、
  `Setting up the pattern and the vectors`（raw: `03_Use_cases_and_application_papers/03.07_How_to_set_up_Digital_Capture/03.07.01.03_Setting_up_the_pattern_and_the_vectors.md`）
  ——**这 18 篇本页一篇都没读**，只知道它们链到本页，**不知道它们说了什么**。
- **不在 `extract/prose-allowlist.txt` 里、本页只用反引号写的两篇**：
  `Pattern Explorer preference page`（raw: `01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.13_Pattern_Explorer_preference_page.md`）
  ——本页只有一条事实指向它（`View Menu → Preferences` 打开的是它），**内容没读**；
  `Function of the base wavetable`（raw 见上）——它链到本页，本页没回读。

## 版本

本文档**有** `## Functional changes` 段，5 条，逐条照录：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.3: Additional view modes and load/save functionality for pattern master files.`
- `SmarTest 6.5.3: Additional columns: State and Location.`
- `SmarTest 6.5.3: Additional icons to indicate the pattern state.`
- `SmarTest 7.1.3: Additional icons and functions to support multiport bursts.`

**第一条是哨兵值，不是「6.3.2 的变更」。** 按 `schema.md` §11.2②，`Introduced before`
这一整类说法的意思是「**在本文档集覆盖范围开始之前就已经有了**」——
**照字面读会读成「6.3.2 新增了 Pattern Explorer」，那是错的。**

剩下四条里有三条集中在 **6.5.3**，内容全指向 pattern master file：

| 版本 | 加了什么 | 落在本页哪个位置 |
|---|---|---|
| 6.5.3 | `Additional view modes and load/save functionality for pattern master files.` | 工具栏的 `Show Folder in Hierarchy`（视图模式）+ 那条 load/save 门槛 |
| 6.5.3 | `Additional columns: State and Location.` | **本页正文里没有这两列的任何说明**——版本记录说加了，正文没介绍，**语料未写** |
| 6.5.3 | `Additional icons to indicate the pattern state.` | 主区那 12 个图标（尤其 `modified` 与 `current primary` 两族） |
| 7.1.3 | `Additional icons and functions to support multiport bursts.` | multiport burst 那三个主区图标 + 工具栏 `Show Multiport Burst in Hierarchy` |

**这是一条前后一致的线**：本页最「活」的那半边（pmfl 门槛 + 状态图标）不是原生的，
是 **6.5.3** 才长出来的；multiport burst 那半边则是 **7.1.3**。

同批条目也收在 [[smartest-6.5.3]] 与 [[smartest-7.1.3]] 两页里（`wiki/versions/`）——
**那两页不是本页建的**，这里只指路。

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.md`
  （TDC `99156.htm`，7,300 字符 / 201 行）。

### 本页「语法 / 参数」节的来源（**那一节不是本页写的，也不来自定义文档**）

- **定义文档里没有语法段**：它的 `##` 段只有 `## Icons`、`## Status line`、`## Related information`、
  `## Functional changes`——没有 `Syntax` / `Parameters` / `Example` 这类**段标记**。
  **Pattern Explorer 是 GUI 工具，这一篇本来就没有命令行语法可抽。**
  §4 的规矩是脚本只收带段标记的内容：**没有段标记就不收，这是脚本的正确行为**，
  和「这一节是空的」是两件事。**这一页这里正好是相反的情形**——
  脚本从定义文档一个字都没收到，**转而收了子主题**。
- 那一节的 **3,555 字符全部来自四个子主题**：
  `16.01.06_Cloning_a_pattern`、`16.01.07_Moving_or_copying_pattern_files`、
  `16.01.08_Deleting_pattern_files`、`16.01.14.01_Moving_vectors_to_another_memory_type`
  ——**来源写在段名里**（脚本在节首自己声明了这件事）。
- **这四篇子主题本页一篇都没读。** 所以那一节里的 `conv_vector` 参数表、
  pattern master file 移动前后的对照、那句 `Cannot delete ...` 报错（**省略号是原文自己带的**）、
  克隆 pattern 时 `JSUB` 被换成 `NOP` 这些内容，
  **本页正文一句都没有展开，也不该由本页负责**——它们属于那四篇子主题自己的页。

### 本页没做的

- **15 篇子主题一篇没读**（含被脚本收进「语法 / 参数」的那 4 篇）。因此
  **建 pattern、克隆、移动 / 复制、删除、检查引用、合并 / 拆分、导入 / 导出、
  排序与过滤、编辑 properties、pattern master file 那一族全部没展开**——
  「六条能力按哪里」的答案就在这些篇里。
- **24 处图片引用一张没看**（1 张正文主图 + 21 个图标 + `View Menu` 里 2 处重复引用，
  其中 `119794.png` 与 `128874.png` 各被引用不止一次）。
  **本页没有任何来自图的结论**：图标长什么样、细节区里有哪些字段、`Filter` 单元格怎么用，
  **本页一个都不知道，只有名字**。`raw/` 目录在本仓库里是空的
  （`raw/README.md`：**「这里没有文件，这是故意的」**），图片路径在本机不存在。
- **`## Related information` 指的两篇没读**：`Pattern Editor`（`02.08.04.16.02`，[[pattern-editor]]）
  与 `Pattern Explorer preference page`（`01.01.14.13`）。
- **18 篇「链到本页」的文档没读**（入边取自 `extract/edges.jsonl`，19 条 / 18 篇，`inline` 口径）。
- **没有实跑**：没有在 Work Center 里开过 Pattern Explorer、没有载入过任何 setup 或 pattern master file、
  没有建过 pattern。**「这些图标在真机上会怎样、哪些功能真会变灰」本页一句都不能保证**——
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有改别的页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 本页这一篇没有编码坏字。** 用 `[一-鿿]` 实测零命中，也没有 `鈥` 开头那一族与 `聽`。
对照 §11.2① 的全语料 1,053 / 9,398 篇含坏字，**本篇属于没有的那一批**——
所以本页引文里没有任何需要说明的坏字。**这不是「没找到」，是查过、结果为零。**

**② `edit bursts.` 与 `Note` 之间少了空白（也没有换行），两句粘成一行**（第 33 行）。原文照录：

> 「- edit bursts.Note Loading and saving selected patterns requires that they were loaded via a pattern master file. This feature is not available for standard pattern setup files.」

**`bursts.` 之后直接跟 `Note`，中间没有空格。本页没替它补。**
所以上面能力清单表里最后一项写成 `edit bursts.` 时，读者要知道它在本篇里后面还粘着一个 `Note`
（「载入与保存」那条 note 就藏在这个粘连处——**它不是独立的一段**）。

**③ 主区那个 port burst 图标的 alt 文字与它的说明不是一回事**（第 155–157 行）：

- 图片引用写作 `![Multiport burst](<../../../../raw/120065.png>)`
- 紧跟着的说明是 `A port burst (type = PortBurst).`

**alt 写的是 Multiport，说明写的是 port burst。原文如此，本页照录，不判哪个是笔误。**

**④ 同一个图片路径在本篇被引用三次，承担两个不同的含义。**
`../../../../raw/128874.png` 既当工具栏的 `Show Multiport Burst in Hierarchy` 用（第 102 行），
又当主区里那一行 multiport burst 的图标用（第 170 行）——**而后者的 alt 文字直接抄了前者的名字**。
**原文没说这两处共用一个图标是不是有意的**，本页只记事实、不作解释。

**⑤ 相邻两行的同一处写法不一致：一处有空格，一处没有**（第 85、86 行，`Show in Hierarchy` 那两项）：

- `- Folder: Displays the folder/file hierarchy of the patterns (same as ![Directory/file-oriented view mode](<../../../../raw/119794.png>) Show Folder in Hierarchy).`
- `- Multiport Burst: Displays the multiport burst hierarchy (same as ![Show Multiport Burst in Hierarchy](<../../../../raw/128874.png>)Show Multiport Burst in Hierarchy).`

**第一行 `>) ` 后面有空格，第二行 `>)` 后面直接接 `Show`。** 原文如此，两行一并照录。

**⑥ `## Related information` 的两条链接之间没有任何分隔符**（第 192 行）：

`[Pattern Editor](<02.08.04.16.02_Pattern_Editor.md>)[Pattern Explorer preference page](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.13_Pattern_Explorer_preference_page.md>)`

**两个链接挨着，中间没有空格、逗号或换行**，渲染出来会贴成一段。

**⑦ 同一件事两处措辞不同（不是错，是不一致）。** 开头那处写 `the row number`，
`## Status line` 那处写 `the row number of the selected cell`；`at the bottom` 对
`at the bottom of the work center`。**两处并列照录，本页不替它统一**（两段原文都引在「是什么」里）。

`verified: doc-only`
