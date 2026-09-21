---
type: concept
title: Waveform and timing sets
layer: n/a
stage: timing
tags: [timing, waveform-set, timing-set, device-cycle, wavetable, timing-setup-tool, concept]
related: [timing, wavetable, timing-setup-commands, timing-specification, timing-equation-set, timing-set-selector, timing-file, timing-master-file, timing-setup-tool, mapping-timing, mapping-project, command-reference, dscp, wsus, tsus, jswf, smartest-6.3.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.03_Waveform_and_timing_sets.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Waveform and timing sets

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**waveform set 是「存在系统内存里的一个逻辑实体」，它是一个容器——不是一条命令、不是一个文件、不是一段语法。**
原文就是这么定的，一个字没绕：

> 「A waveform set is a logical entity stored in system memory that holds:」

**「logic entity stored in system memory」这五个词是本页的定盘星**：它是**运行期在内存里的东西**，
所以它**没有语法、没有文件格式、没有参数表**——**本页的「语法 / 参数」节为空，这不是缺内容**。

### 它装什么：一半是全体 pin 共享的，一半是每个 pin 各自的

原文紧接着用一个两级的清单把它的内容列全了（**逐字结构如下**）：

| 层级 | 原文的项 | 意思 |
|---|---|---|
| **`For all pins together`** | `System clock period` | **系统时钟周期**——全体 pin 共用 |
| | `Default device cycle name` | **默认 device cycle 名**——全体 pin 共用 |
| **`Per pin`** | `Device cycle definitions in a device cycle table` | **device cycle 定义**，装在**一张 device cycle 表**里 |
| | `Physical waveform definitions in a physical waveform table` | **物理波形定义**，装在**一张 physical waveform 表**里 |
| | `One or more timing sets` | **一个或多个 timing set** |

**这张表就是「waveform set 是什么」的全部答案。** 三个要点：

1. **它是两层结构**：上层两个字段是**全体 pin 一起**的，下面三项是**逐 pin**的——
   **同一个 waveform set 里，每个 pin 各有一套 device cycle / 波形 / timing set。**
2. **device cycle 与波形都放在「表」里**（`device cycle table` / `physical waveform table`），
   **不是直接列在 waveform set 底下**。
3. **timing set 是 waveform set 的一个成员，且可以是多个**（`One or more timing sets`）。

> ⚠️ **`physical waveform table` 那一项，语料自己的链接指向的是 `Wavetables`**
> （`[physical waveform table](<02.08.04.16.04.05_Wavetables.md>)`）。
> **也就是说：本篇管它叫 physical waveform table，而链过去的那一篇叫 Wavetables。**
> **本页照原样两处并列**——**这两个名字是不是同一个东西，本篇没有写**。
> （注意：[[wavetable]] 那一页的出处是**另一篇** raw：`02.08.04.34.04.03.03.07_wavetable.md`，
> **和本篇链的 `02.08.04.16.04.05` 不是同一篇**——**`02.08.04.16.04.05` 本页没读**。）

### timing set 在它里面：`forms a part of` —— **包含关系，不是并列关系**

**这是本页最要紧的一条，也是这个词最容易读错的地方。** 原文：

> 「A timing set forms a part of a waveform set and stores:」

**并且交代了「为什么要有 timing set」**：

> 「To define a waveform, you need to provide (among other things) the timing information for the
> waveform. This is where timing sets come in.」

**timing set 自己装两样东西**（原文）：

| timing set 装什么 | 原文 |
|---|---|
| **测试系统周期** | `The test system period` |
| **各已配置 pin 的边沿放置延迟** | `Edge placement delays for the configured pins` |

**所以层级是：waveform set（容器）⊃ timing set（容器的一部分）⊃ 周期 + 各 pin 的边沿延迟。**
**「一个 waveform set 里可以有多个 timing set」和「每个 timing set 一套边沿延迟」合起来，
就是这个容器的用法**：换 timing set = 换一套边沿延迟（**这是本页的读法（推断）**，
依据是上面那两条原文——`One or more timing sets` + `Edge placement delays for the configured pins`；
**本篇没有举任何例子，也没有写「怎么切换」**）。

### 作用范围：`channel` 或 `group of channels`

> 「For each channel or a group of channels you can define a number of waveform and timing sets
> to run your tests with.」

**两个口径要一起读出来**：**「为每个通道 / 每组通道」**、**「可以定义若干套」**。
**注意 `you can define a number of` 这句里的数是「若干」，不是「一个」**——
**本篇没有写上限是多少**（上限在别的篇里，见「典型用法」那一节的 ⚠️ 表）。

### ⚠️ 一条词面警告：**这不是 02.06 那条 `JSWF` 命令**

**本页的 slug 是 `waveform-set`，而语料里另有一条以 `JSWF` 为缩写的命令**
（`02.06.16.02.06_JSWF__-__Jitter_Set_WaveForm`，见 [[jswf]]）。
**两者的全称里都有 `WaveForm`，但没有任何关系**：

| | 本页（waveform set） | `JSWF` |
|---|---|---|
| 它是什么 | **内存里的逻辑容器**（本篇第一句） | **一条抖动注入命令**（属 02.06.16 抖动族） |
| 出处 | `02.08.04.34.03`（**本页的 `sources:`**） | `02.06.16.02.06`（**本页没读**） |
| 本篇有没有提到它 | **一个字都没有** | — |

**本篇 raw 里出现的 `waveform` 全部在 `waveform set` / `physical waveform` 这两个语境里**，
**没有一处是指那条命令**。**词面匹配会把这两件事指到一起，本页把它点明。**

### 本篇的两个子主题（**语料自己声明的下一层，本页没读**）

原文的 `#### Subtopics` 列了两篇，**这两篇是本篇的正式下钻方向**：

- `Relationship between waveform sets and timing sets`（raw: `02.08.04.34.03.01_...`）
- `Implications when running tests`（raw: `02.08.04.34.03.02_...`）

**从篇名就能看出它们正好是本页最想要的两块**——「两者的关系」与「跑测试时的后果」——
**而它们本页都没读**（所以「timing set 在运行期怎么切换、切换有什么代价」本页答不了，见「出处」）。

## 典型用法

**先说清楚：本篇没有 Procedure、没有 Before you begin、没有 Example、没有图。**
它整篇是「一句定义 + 一个内容清单 + 一段 timing set 的说明 + 六个链接 + 一行版本」。
**所以这一节给不出「照这个顺序敲这几条命令」**——那在本 wiki 的 timing 那一族里是别的页的事。

**本篇能确定的三件事（都是文档事实）：**

1. **可以定义「若干套」**，作用范围是**每个通道或每组通道**（`For each channel or a group of channels`）。
2. **每个 pin 各有一套** device cycle / 物理波形 / timing set（`Per pin`）。
3. **timing set 是 waveform set 的一部分**，一套里可以有多个，**每个装周期 + 各 pin 边沿延迟**。

**本篇答不了、本 wiki 别处答的**（**下面这些命令名在本篇 raw 里一个都没出现**，
它们来自 [[timing-setup-commands]] 那一页——**那是本页读过的 wiki 页，不是本页的 raw**）：

| 想知道什么 | 那条命令（二手，来自 [[timing-setup-commands]]） |
|---|---|
| **上限是多少** | `DSCP` 的 `waveform_set` / `timing_set` 参数定**上限**；`WSUS` 定「用了几个 waveform set」、`TSUS` 定「用了几个 timing set」 |
| **哪一套是 primary** | `DPRT`（Default PRimary Timing sets）、`SPRM`（Set PRiMary sets） |
| **谁按 waveform set 号操作** | `BWDF` / `ETDS` / `EUDS` / `PCLK` / `DCUD` / `CLKR` 等都带 **waveform set 号**这一位参数 |
| **怎么查有哪些** | `SDSC? TIM,WSET`（waveform sets，非 equation based）/ `SDSC? TIM,TSET`（timing sets，非 equation based） |

**其中一条与本篇互为印证，值得单独记**（**二手**，逐字来自 [[timing-setup-commands]] 的 `DSCP` 条目）：

> 「The number of timing sets must be equal to or greater than the number of waveform sets,
> as there must be at least one timing set per waveform set.」

**「每个 waveform set 至少一个 timing set」——这正是本篇 `One or more timing sets`
那句话在配置侧的后果**（**推断**：两篇说的是同一件事，依据是两句话的主语与关系完全对应；
**本篇没有写过任何上限/下限规则**）。

> ⚠️ **上面这张表的每一行都不是本页的 raw 读出来的。** 本页的 raw 只讲「容器里装什么」，
> **一条命令名都没有**。**列在这里是因为读者一定会接着问「那怎么配」**——
> 但**本页不对这些命令的参数、顺序、报错声称任何事**。

## 和谁有关

**每行都标明这条关系的证据是哪来的**——**本页的 raw 极短，很多关系是别的页给的**。

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[wavetable]] | **被包含项之一（物理波形的所在）**。本篇的内容清单里那一项叫 `Physical waveform table`，**语料把它链到 `Wavetables`**——两边的名字不一样，**本篇没说它们是不是同一个东西** | 本篇内容清单 + 那句链接（**文档事实**）；对比 [[wavetable]] 那页的出处是**另一篇 raw**（**本页没读**） |
| [[timing-setup-commands]] | **L1 命令侧的入口（下游）**。上限（`DSCP`/`WSUS`/`TSUS`）、primary（`DPRT`/`SPRM`）、按号操作的命令都在那一页的语法节里 | [[timing-setup-commands]]（**本页读过的 wiki 页**）——**本篇 raw 里没有一条命令名** |
| [[timing-specification]] | **别一套体系里的对应物（易混）**。timing specification 是 **equation based** 那一侧的合成物；**本页讲的是非 equation based 那一侧的容器**。**「近」在哪：两个名字里都有 timing；「不同」在哪：本篇 raw 里 `timing specification` 这个词一次都没出现** | 本页没读那篇（**取材边界**） |
| [[timing-equation-set]] | **同上，equation based 一侧的另一个件**。**本篇没有出现它** | 本页没读（**取材边界**） |
| [[timing-set-selector]] | **GUI 侧的「选 timing set」入口**（那页未建）。**本篇写的是「一个 waveform set 里可以有多个 timing set」，但没有写「在哪选」** | 本页没读（**取材边界**） |
| [[timing-file]] / [[timing-master-file]] | **落盘的一侧**。本篇讲的是**内存里的实体**，**它和文件的关系本篇一个字没写** | 本页没读那两篇（**取材边界**） |
| [[timing-setup-tool]] / `Waveform Editor`（未建） | **GUI 编辑入口**。本篇的 `## Related information` 点了 `Timing Setup Tool` 与 `Waveform Editor` 两条链接 | 本篇 `## Related information`（**文档事实：链接存在**）——**两篇都没读** |
| [[mapping-project]] | **上限那一格在这里**。那张映射表的「定 waveform set 上限」一行把 GUI 的 `Waveform sets`、文件的 `waveform_sets`、L1 的 `DSCP` 的 `waveform_set` 排在一起 | [[mapping-project]]（**本页读过的 wiki 页**）——**本页没读那一篇的 raw** |
| [[mapping-timing]] | **timing 侧的跨层对照表**（已建）。**本页没读它**，但它和本页同属 timing 段 | 本页没读（**取材边界**） |
| [[command-reference]] | **字母序命令索引页**。`WSUS` / `TSUS` / `DSCP` 这些名字在那里出现过 | [[command-reference]]（**本页读过的 wiki 页**） |
| `Relationship between waveform sets and timing sets`（**未建，语料自己声明的子主题**） | **本篇的正式下钻**：讲两者关系。**本页没读** | 本篇 `#### Subtopics`（**文档事实：篇名与链接**） |
| `Implications when running tests`（**未建，同上**） | **本篇的另一个正式下钻**：讲跑测试时的后果。**本页没读** | 本篇 `#### Subtopics`（**文档事实**） |
| [[jswf]] | **词面撞车、实质无关**：那条 02.06 的抖动命令全称里也有 `WaveForm`。**本篇一个字没提它** | 本页没读那篇（**取材边界**）；见「是什么」那节的警告 |
| [[timing]] | **stage 页**。本页 `stage: timing` 填的是「最近的一段」不是「归属」（§6），**而且本页的 `layer: n/a` 是对的**——它不是 L1/L2/L3 里的任何一层，**它是内存里的数据实体**。（**⚠️ [[timing]] 的「涉及对象」表里原先把本页写成 `file/concept`，`extract/stage-report.md` 的第十一类因此报过这一处 ❌。2026-09-21 已查明：`concept` 是页面类型、不是层——schema §6 的层值是 `L1|L2|L3|file|gui|n/a`，那一格已改成 `n/a`。`layer` 按 PROSE-SPEC 第 2 条本页不许动，所以改的是对面那张表。**） | frontmatter 约定 + [[timing]] 的表格（**本页读过的 wiki 页**）+ `extract/stage-report.md` 第十一类 |

**一条要显式记下来的**：**本页的 `related` 里最硬的关系其实只有 `wavetable` 一条**
（本篇唯一给出名字的内容项），**其余全是「该去哪找」**——
**本页的 raw 一共 1,869 字节，它没有能力承担更多关系**。

## 版本

本文档**有** `## Functional changes` 段，段里**只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 waveform set」。**
> 措辞是 `before`，意思是「在本套文档集覆盖范围开始之前就已经有了」。
> **所以只能说：7.10.3 上有，且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 waveform set」。**

**版本段里没有的东西**（照实记，不替它补）：**没有第二条**。
所以「`Per pin` 那三项里哪一项是哪个版本加的」「timing set 的个数上限哪一版改过」
**在本篇里查不到**——要去 [[smartest-6.3.2]] 之后的各版本页，或去别的文档。

## 出处

`sources:` **一篇**：

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.03_Waveform_and_timing_sets.md`
  （frontmatter 的 `source_topic` 是 `17791_2.htm`，**1,869 字节 / 37 行，整篇读完**——
  按 §11.5 口径：字节是 `st_size`，行数是 `wc -l`）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。
  **它这一节是空的**，理由脚本自己写在节里：**本篇没有 `Syntax` / `Parameters` / `Example` 这类段标记**，
  「跟着 `Subtopics` 找一层也没有」。
  > **⚠️ 这后半句本页无法复核**：脚本说它跟着 `#### Subtopics` 往下找了一层——
  > **那两篇子主题本页没读**（见下）。**本页照原样留着脚本这句话，不动它，也不替它背书。**
  > **这不是对脚本的质疑，是本页的取材边界。**

**⚠️ 一处 §10 的「重复投放」，本页查了**：本篇的 `source_topic` 是 **`17791_2.htm`**（带 `_2` 后缀），
**带这个后缀就说明同一篇 TDC 页被投放了两份**。实测确实有另一份：

| | 路径 | `source_topic` | 字节 |
|---|---|---|---|
| **本页的出处** | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.03_Waveform_and_timing_sets.md` | `17791_2.htm` | **1,869** |
| **同页的另一份** | `01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04_Waveform_and_timing_sets.md` | `17791.htm` | **2,282** |

**两份的字节数不一样**（差 **413 字节**），**所以它们不是同一份拷贝那么简单**——
**差在哪，本页没看**（本页只核了另一份的 frontmatter 与大小，**没有读它的内容**，按 §12 不越取材边界）。
**记这一条的用处**：按 §10，遇到「两篇文档说法不同」时**先做这一步**——
**本页的结论全部只来自 `17791_2.htm` 这一份。**

**本页没做的**：

- **两个 `Subtopics` 一篇没读**：`Relationship_between_waveform_sets_and_timing_sets` 与
  `Implications_when_running_tests`。**所以「waveform set 与 timing set 的关系细节」
  与「跑测试时的后果」本页一个字没有**——**恰恰是本篇标题承诺、又推到子主题去的那两块。**
  （**注意**：这两个篇名**在 `extract/prose-allowlist.txt` 里没有**，所以本页用反引号写它们，
  **没有做成链接**——按 §9.1，链一个清单外的名字就是造一个永远不会填的悬空目标。）
- **`## Related information` 那六条一篇没读**：`Editing Device Cycles and Waveforms`、
  `Selecting a Waveform for Editing`、`Waveform Editor`、`Equation based timing setup`、
  `Timing Setup Tool`、`Using the Timing Setup Tool`。
  **所以「GUI 上怎么编 device cycle / 波形」本页一个字没有**——只有链接的名字。
- **`02.08.04.16.04.05_Wavetables` 没读**（本篇链过去的那个 `physical waveform table`）。
  所以**本篇那个名字与 [[wavetable]] 那页讲的到底是不是同一个东西，本页答不了。**
- **02.06 的命令一篇没读**：`DSCP` / `WSUS` / `TSUS` / `DPRT` / `SPRM` / `BWDF` 等
  **本页只在 [[timing-setup-commands]] 那张**（wiki 页，**二手**）**里见过名字**，
  **没读它们的 raw**，**所以参数细节、顺序、报错本页一概没有**。
- **`JSWF` 那一篇没读**——本页只在「是什么」里点明**它和本页不是同一个东西**，
  **不对它声称任何别的事**。
- **图**：**本篇对 `raw/` 的引用 0 处**——实测 `.png` / `.jpg` / `.gif` / `!\[` / `<img` / `raw/`
  六种写法在本篇里**全部 0 命中**。**所以本页没有任何来自图的结论，这张「没有图」是查过的事实，
  不是「够不着」。**
- **没有实跑。** 没在机台上定义过 waveform set、没切过 timing set、没看过内存里的它长什么样。
  `verified: doc-only` 指的就是这件事。
- **本篇没有 `## Errors` / `## Warnings` 段**，所以本页**没有「报错条件」节**——
  这不是漏写（**本页的骨架里本来就没有那一节**），是语料没有。

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **`## Related information` 那六条链接挤在一行里、中间没有任何分隔**。
> 原文逐字（一行就是全部六条）：
>
> `[Editing Device Cycles and Waveforms](<02.08.04.34.06.07_Editing_Device_Cycles_and_Waveforms.md>)[Selecting a Waveform for Editing](<02.08.04.34.06.07.04_Selecting_a_Waveform_for_Editing.md>)[Waveform Editor](<02.08.04.26.02.05.05.01.01_Waveform_Editor.md>)[Equation based timing setup](<../../01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.01_Equation_based_timing_setup.md>)[Timing Setup Tool](<02.08.04.34_Timing_Setup_Tool.md>)[Using the Timing Setup Tool](<02.08.04.34.06_Using_the_Timing_Setup_Tool.md>)`
>
> **`](<` 紧接 `[`，六个条目之间没有逗号、没有换行、没有列表符**——
> 这是 HTML→md 压平时把列表压成了连续文本。**本页照原样引这一整行，没有替它断句。**

> ② **措辞在 `waveform` 与 `waveform set` 之间滑动。** 那两句话逐字是：
>
> `To define a waveform, you need to provide (among other things) the timing information for the waveform.`
>
> `This is where timing sets come in. A timing set forms a part of a waveform set and stores:`
>
> **前半句的主语是 `waveform`（单个波形），后半句讲的是 `a waveform set`（容器）的一部分。**
> **本篇没有说清这两者怎么过渡**——**本页不替它把 `waveform` 改成 `waveform set`**，
> **两处照原样并列**（「是什么」那节引的就是原句）。

> ③ **同一篇里两个范围口径**：开头一句写 `For each channel or a group of channels`，
> 而紧接着的清单标题写 **`Per pin`**。
> **`channel` 与 `pin` 在这里是不是同一个东西，本篇没有说**——
> （**推断**）是同一个：依据是两句相邻、且没有任何过渡说明；**但这是推断，不是原文。**

> ④ **清单的两项层级用词不齐**：`- For all pins together:` 与 `- Per pin:`
> ——**前者的 `together` 是副词、后者 `Per pin` 是介词短语**，
> 两个标题的语法结构不一样（**不是错，是原文的行文**，照原样记）。

`verified: doc-only`
