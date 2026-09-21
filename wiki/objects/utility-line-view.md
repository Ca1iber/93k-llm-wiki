---
type: object
title: Utility Line view
layer: gui
stage: run
tags: [utility-line, hardware-perspective, utility-pogo-block, utility-card, gui-view, debug, run]
related: [utility-lines, utility-line-assignments, utility-pogo-block-utility-card-v93000-exa-scale-systems, dut-interface-layout, utility-card, utility-pins-editor, hardware-view]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.04_Utility_Line_view.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Utility Line view

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**`Utility Line view` 是 Hardware Perspective 里的一个视图：查 utility line 的读 / 写状态，
并设它的写状态——用在调试 test setup 的时候。** 原文逐字：

> 「The Utility Line View is part of the Hardware Perspective and provides an interface for querying
> utility line read and write states and setting utility line write states when you are debugging
> your test setup.」

**拆成四件事**：

| 原文的说法 | 是什么 |
|---|---|
| `is part of the Hardware Perspective` | **它不是一个独立窗口，是 Hardware Perspective 的一部分** |
| `querying utility line read and write states` | **查**：读状态与写状态都能查 |
| `setting utility line write states` | **写**：能设**写**状态（**原文没说能设读状态**） |
| `when you are debugging your test setup` | **时机**：调 test setup 时用 |

**utility line 是干什么的**，原文紧接着一句：

> 「Utility lines are provided on the V93000 test head to control external devices such as relays
> and indicators or to read from external devices.」

**即：test head 上用来控外部设备（继电器、指示灯）或从外部设备读的线。**
**这句在原文里是直接链到 utility lines 那一篇的**（见 `## 和谁有关`）。

### 它最要紧的一条能力：能碰「没在 pin configuration 里定义的那些」

原文逐字（**含括号里那句条件**）：

> 「The Utility Line view enables you to monitor or control all utility lines, including those that
> are not defined in the pin configuration. (Defining utility line names or utility purposes in the
> pin configuration is required when you control the write states of the utility lines using the
> routing sets created in the Routing Setup Tool.)」

**两句拆开看：**

- **前一句**：范围是 `all utility lines` —— **包括没在 pin configuration 里定义的**。
  **所以这个视图比 pin configuration 宽**。
- **后一句是一条条件**：**用 Routing Setup Tool 建的 routing set 去控写状态时**，
  **才要求**在 pin configuration 里定义 utility line 名或 utility purpose。
  **原文只写了 `required when` 这一种情形**——**不用 routing set 的那条路径是否也有这个前提，原文没说。**

### 界面：左列是 utility pogo block

原文逐字：

> 「The left column of the Utility Line view represents the utility pogo blocks. For the first eight
> utility pogo blocks, the displayed identifier is a combination of the legacy "UTI#" and the new
> three digit pogo block number. The screen shot above also shows eight more pogo blocks of a second
> optional Utility Card.」

**图证**（下同：**图里读到的字在 raw 文本里搜不到**，见 `## 出处`）。
`raw/354721.png` 的 alt 是 `Utility Line View SmarTest 7.10.x`，图里是：

| 图里看到的 | 与原文对照 |
|---|---|
| 视图以标签页形式出现，标签名 `Utility Line`（旁边还有一个 `Sample Code` 标签） | 原文没提标签页 |
| 左列列表头是 `Block`，往下 16 行 | 原文说「左列是 utility pogo block」 |
| 前八行标识从 `UTI1/165` 递增到 `UTI8/172`（共 8 行） | **对得上**「`legacy "UTI#"` + 三位 pogo block 号」的组合 |
| 后八行标识是裸的三位数，从 `265` 到 `272`（共 8 行） | **对得上**「eight more pogo blocks of a second **optional** Utility Card」 |
| 第一行横排 32 个列号，从 `32` 一路递减到 `01`，`01`–`09` 带前导零 | **对得上**「the range [01 鈥?nbsp;32] **from right to left**」（**原文这处是坏字**，见 `## 出处` ⚠️①） |
| **所有格子里的值都是 `0`** | **原文没有解释 0 / 1 各代表什么** |

**后八行 = 第二块可选 Utility Card 这个等式是（推断）**——
**依据只是原文把「eight more pogo blocks」和「a second optional Utility Card」写在同一句里，
再对上图里正好多八行**；**原文没有写「后八行就是它」这样一句。**

### 编号的两套体系（原文的 `Note`）

**原文 `Note` 那行行首有两个空格**（逐字，**注意开头那两个空格**）：

> 「  Note In the header row of the Utility Line view, SmarTest shows the channel numbers of the
> utility lines, using the range [01 鈥?nbsp;32] from right to left. The utility line itself are
> numbered with an offset of -1 in the range [00 鈥?nbsp;31] that corresponds to the scheme "URW##"
> of the "Utility pogo pin layouts" in the "DUT Board Design Guidelines". For detailed description
> about utility pogo blocks, see Utility line assignments.」

**两条编号，差 1**：

| | 原文 | 区间 | 方向 | 对应什么 |
|---|---|---|---|---|
| **表头显示的是 channel number** | `SmarTest shows the channel numbers of the utility lines` | `[01 – 32]` | `from right to left` | —— |
| **utility line 自己的编号** | `numbered with an offset of -1` | `[00 – 31]` | —— | `DUT Board Design Guidelines` 里 `Utility pogo pin layouts` 的 `URW##` 方案 |

**图证与这条相符**：表头最右是 `01`，所以「编号从右往左走」是对的。

**两处区间里的 `鈥?nbsp;` 是坏字**——本页原样引，**不猜它是哪个字符**（见 `## 出处` ⚠️①）。

### 三个图标

原文逐字：`There are three icons at the top of the Utility Line view.` 底下三条 bullet：

| # | 原文 bullet（逐字） | 作用 |
|---|---|---|
| 1 | `Clicking the Setup Preferences icon opens a preference window with the same settings of the Utility Line preference page.` | 开一个 preference window，**设置项与 `Utility Line preference page` 相同** |
| 2 | `Clicking the Refresh icon performs a manual refresh of the Utility Line View.` | **手动**刷新一次（原文用 `manual`，**所以刷新不是只有自动的**） |
| 3 | `The center icon is used for applying write changes to all utility blocks.` | 把写改动应用到**所有** utility block |

**图证**（`raw/70662.jpg`，alt 是 `Utility Line View icons`）：
**三个图标从左到右是 `Refresh` → `Apply write changes to all` → `Setup preferences`**
（这三个词是**图里的标注**，不是可搜的文本）。

**两件事因此可以定下来：**

- **原文三条 bullet 的顺序与界面上的左右顺序不一致**：bullet 把 Setup Preferences 排在第一条，
  而界面上它在最右。
- **原文第三条 bullet 只写「the center icon」、不给名字**，前两条却给了名字。
  图证把这一格补上了：**中间那个 = `Apply write changes to all`**，与原文那句「应用到所有 block」相符。
- **图里这三个图标右边还有两个方形图标，一个标注都没有**——**本页不猜它们是什么。**

### 这个视图里，原文没写的东西

原文**没有**写：格子里的 `0` / `1` 是什么电平、能不能逐格点击切换、
read state 与 write state 在界面上怎么区分、要不要先选 site、刷新是自动的还是只有手动的。
**这些一律是「语料未写」。**（图里所有格子都是 `0`，**图证也答不了 0 / 1 的含义**。）

**也没有**：`## Procedure`、`## Before you begin`、`## Syntax`、任何一条命令或 API 的名字。
**这一篇是纯 GUI 描述**（这也是它的语法节为空的原因，见页首那一节）。

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`。**
**能从原文落成步骤的只有三步**——下面每一格都附依据：

| 步骤 | 依据（原文） |
|---|---|
| **1. 在 Hardware Perspective 里打开 Utility Line view** | `The Utility Line View is part of the Hardware Perspective` ——**原文没写具体怎么打开** |
| **2. 查**：看 utility line 的读 / 写状态 | `querying utility line read and write states` |
| **3. 要拿最新状态就手动刷一次**：点左边那个刷新图标 | `Clicking the Refresh icon performs a manual refresh of the Utility Line View.` |
| **4. 改**：改完写状态后，点中间那个图标把改动应用到所有 utility block | `The center icon is used for applying write changes to all utility blocks.` |

**改之前要确认的一件事（原文只有这一条前提）**：
**如果你是用 Routing Setup Tool 建的 routing set 去控写状态，那 pin configuration 里必须先有
utility line 名或 utility purpose。** 依据就是上面那句 `required when` 的括号句。
**别的控制路径要不要这个前提，原文没说——所以这一步本页只敢挂在「用 routing set」这个条件底下。**

**三条（推断），各自的依据都只是原文那一句：**

- **第 1 步的入口**：原文只说 `is part of the Hardware Perspective`，
  **没说菜单项、没说要不要先选 pin**——**本页不知道路径，只敢写「在 Hardware Perspective 里」。**
- **第 4 步的作用范围**：`applying write changes to **all** utility blocks` 读起来是**一次对所有 block 生效**；
  **依据只是那个 `all`。****它会不会把没改过的 block 的当前值一起覆盖，原文没写。**
- **第 2 步要不要先选 site**：原文整篇没有一个 `site` 字，
  **而 utility line 是 test head 级的（原文说在 test head 上）**——
  **所以「不需要选 site」是（推断），依据是原文把它写在 test head 一级、且全文不提 site；
  原文没有正面写这一句。**

## 和谁有关

- `Hardware Perspective`（**未建**，raw: `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05_Hardware_Perspective.md`）
  — **上游，本页是它的一部分**。原文逐字 `The Utility Line View is part of the Hardware Perspective`，
  并在这句里直接链到它。**这一篇的父视图页不在 allowlist 里，所以只能写反引号 + raw 路径。本页没读它。**
- [[utility-lines]] — **同一个对象的定义页（概念层）**。原文那句
  `Utility lines are provided on the V93000 test head to control external devices such as relays and indicators or to read from external devices.`
  在原文里是直接链到 utility lines 那一篇的。**本页只有「它在 test head 上、用来控外部设备或读」这一句；
  utility line 本身的定义与电气特性在那页。** **两页不同层**：本页是**运行期视图**（`stage: run`），
  那页是**概念**（`stage: pin`）——**这正是本页与它分开建页的理由。**
- [[utility-line-assignments]] — **细节那一侧**。原文 `Note` 以
  `For detailed description about utility pogo blocks, see Utility line assignments.` 收尾，
  **把 pogo block 的细节整体推给了它**。**本页只有「左列是 utility pogo block」与「前八个带 `UTI#` 前缀」两条表面事实；
  block 怎么分配、`URW##` 怎么对，在那页。**
- [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] — **原文同段推荐的去处**。原文
  `For more information, refer to DUT interface layout and to section Utility pogo block mapping in Utility pogo block - Utility Card (V93000 EXA Scale systems).`
  ——**它指的是那篇里的 `Utility pogo block mapping` 这一节**（原文那一处带节锚点）。
- [[dut-interface-layout]] — **与上一条并列的推荐去处**（同一句里的另一个目标）。
  **本页对这两页只有「原文点了它们」这一条信息，它们的内容一篇都没读。**
- [[utility-card]] — **那块「第二块可选卡」的页**。原文说图里 `also shows eight more pogo blocks of a second optional Utility Card`；
  **图证里那八个裸三位数（`265`–`272`）就是本页判断的那八行**（**是（推断），见 `## 是什么`**）。
  **本页只有「有这么一块可选卡、它多出八个 block」这两句，卡本身在那页。**
- [[utility-pins-editor]] — **（推断）pin configuration 那一侧的编辑器**。
  依据：原文的括号句要求在 pin configuration 里定义 utility line 名或 utility purpose，
  而这一页从名字看就是定义这些东西的编辑器；**依据只是这一句 + 页名。本页没有那页的任何事实。**
- [[hardware-view]] — **（推断）同族的兄弟视图**。依据两条：
  本页 raw 是 `01.01.07.05.04`、Hardware view 是 `01.01.07.05.03`，**同挂在 `01.01.07.05`（Hardware Perspective）底下**；
  而 [[hardware-view]] 自己的原文里也写着它是 `in the Hardware perspective`。
  **⚠️ 本页读的这一篇里一个字都没提 Hardware view——所以这是推断，不是文档事实。本页没读 [[hardware-view]]。**
- `Utility Line preference page`（**未建**，raw: `01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.31_Utility_Line_preference_page.md`）
  — **图标 1 指向它**。原文说 preference window 的 `the same settings of the Utility Line preference page`，
  **即两条路进的是同一组设置**。**本页只有「设置项相同」这一句；有哪些设置项，在那篇。**
- `Utility Purpose view`（**未建**，raw: `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.06_Utility_Purpose_view.md`）
  — **原文 `Related information` 五个目标之一**。
  **⚠️ 同形陷阱：它不是 `utility-purpose-editor`。** 后者的 raw 是
  `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.05_Utility_Purpose_Editor.md`
  （**Editor**），而本篇链的是 **View**（`01.01.07.05.06`）——
  **两个不同的对象、两个不同的路径，本页不把两者当同一个东西，也不给 `utility-purpose-editor` 建链。**
- `Routing Setup Tool`（**未建**）— **原文括号句里那个「用 routing set 控写状态」的工具**。
  **原文只有这一个名字，没说它在哪、怎么建 routing set。**
- `DUT Board Design Guidelines`（**未建**）— **`URW##` 编号方案的出处**（原文
  `the scheme "URW##" of the "Utility pogo pin layouts" in the "DUT Board Design Guidelines"`）。
  **本页不知道它是什么、在哪里、和 TDC 语料是什么关系。**
- `get-utility-lines` / `set-utility-lines`（**名字在 allowlist 里，但本页不链**）——
  **本页服务的是「查 / 设 utility line 状态」这件事，而这一篇从头到尾没有出现过一条命令或 API 的名字**，
  所以本页**没有任何依据**说这两个对象和这个视图是什么关系。**它们各自是什么，本页不知道。**

## 版本

本文档**有** `## Functional changes` 段，**四条**（逐字）：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.3: In the Utility Line View, the utility lines are shown with bit numbers 01 to 16.`
- `SmarTest 7.2.0: Utility Purpose view introduced`
- `SmarTest 7.10.1: Three-digit utility pogo block designator on EXA Scale systems.`

**四条各自的要点：**

1. **第一条是 §11.2 ② 那个哨兵值。** `Introduced before SmarTest 6.3.2` 的意思是
   **「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
   **所以这个视图成立于哪个版本，这份语料里没有。**
2. **6.5.3 那条与正文的数字对不上**（⚠️ 见 `## 出处` ④）：
   它说 utility line `are shown with bit numbers 01 to 16`，
   而正文说表头区间是 `[01 鈥?nbsp;32]`、截图 alt 写 `SmarTest 7.10.x`、图里也是 **32 列**。
   **两种说法并列存在，本页不选一个。**
3. **7.2.0 是 `Utility Purpose view introduced`** —— 与正文 `Related information` 里那个
   `Utility Purpose view` 名字对得上。**版本段只说它被引入，正文里没有它的任何用法。**
4. **7.10.1 解释了正文里「three digit pogo block number」是哪来的** ——
   图证里 `UTI1/165` 那三位数就是它。**EXA Scale 系统**这一限定也只在版本条目里出现，
   **正文没有把三位数标识与 EXA Scale 挂在同一句里。**

**与 wiki 面向版本的关系**：本 wiki 目标是 **SmarTest 7.10.3**，而这一篇最后一条是 **7.10.1**——
**7.10.2 / 7.10.3 有没有再动它，这一篇里没有任何条目。**

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.04_Utility_Line_view.md`

**本页没做的：**

- **本页读了这一篇的两张图**（§11.4 允许、也要求读）：`raw/354721.png`（视图截图）与 `raw/70662.jpg`（三个图标）。
  **图里读到的字在 raw 的文本里搜不到**——拿 `UTI1/165`、`Apply write changes to all`、
  `Setup preferences` 去这一篇 grep，**一处也没有**。所以凡是来自图的，本页都标了「图证」，
  **读者要核只能自己再开那两张图。**
- **父页 `Hardware Perspective` 没读** —— 所以这个视图在 perspective 里怎么打开、
  和别的视图怎么排布、有没有 `## Subtopics` 把它列进去，**本页答不了**。
- **原文点名的七篇都没读**（`Utility lines` / `Utility line assignments` / `DUT interface layout` /
  `Utility Card` / `Utility pogo block - Utility Card (V93000 EXA Scale systems)` /
  `Utility Purpose view` / `Utility Line preference page`）——
  **本页只在「原文点了它们」这个层面上写它们。** 尤其是：
  **utility line 是什么、pogo block 怎么分配、preference 里有哪些设置项、
  `Utility Purpose view` 长什么样，本页一个字都没有。**
- **`DUT Board Design Guidelines` / `Routing Setup Tool` 没读（原文也没说它们在哪）** ——
  所以 `URW##` 方案的内容、routing set 怎么建、它在哪个 GUI 里，**本页都不知道。**
- **没有任何 L1 / L2 / L3 材料** —— **这一篇全文没有出现过一条命令、一个 API、一个文件名。**
  所以本页**不能**回答「这个视图在自动化里怎么复现」——**「和谁有关」最后一条把这件事写明了。**
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其本页 `stage: run` 填的是「最近的一段」（§6），不是「归属」**——
  **这一篇没有一句话说它属于哪一段流程**，`run` 是按「调试 test setup 时用」这个时机填的。
- **两张图之外的图一张都没看**，原文也没有别的图。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 两处坏字（§11.2 ① 那一族）。** `Note` 里两处区间逐字是
> `[01 鈥?nbsp;32]` 与 `[00 鈥?nbsp;31]`。
> **`鈥` 是三字节 UTF-8 字符的头两个字节被按 GBK 读出来的结果**，第三个字节已经丢了（这里是 `?`），
> 所以按 §11.2 ① **只许报区间、不许当映射用**——它落在 **U+2000–U+203F**
> （破折号 / 引号那一带，`–` / `—` / `‘` / `’` / `“` / `”` 都在里面），**本页不猜它是哪一个。**
> 另外 `nbsp;` 前面的 `&` 也没了（那是 HTML 实体没被转换，**所以这里连 `&nbsp;` 都不是完整的**）。
> **本页引文里原样留着坏字**（见 `## 是什么` 里那条 `Note` 引文）。
> **代价照 §11.2 ① 写明白**：拿修好的 `–` 去这一篇里搜是搜不到的，**要搜坏掉的那个形态。**
>
> **② `Note` 行首有两个空格，`Note` 后面也没有分隔符。** 逐字（**注意开头的两个空格**）：
> `  Note In the header row of the Utility Line view, SmarTest shows the channel numbers of the`
> ——**这是原文就有的**（在 markdown 里两个行首空格会让这一行变成缩进块或段落续行，看渲染器）。
> **本页引文照原样留了那两个空格。**
>
> **③ 同一行里主谓不一致。** 逐字：`The utility line itself are numbered with an offset of -1`
> ——**`line itself` 配 `are`**。**本页照原样引，不替它改成 `lines themselves`。**
>
> **④ 6.5.3 那条版本条目与正文的数字对不上，而且对不上得不止一处。** 条目逐字：
> `SmarTest 6.5.3: In the Utility Line View, the utility lines are shown with bit numbers 01 to 16.`
> 而正文写表头区间是 `[01 鈥?nbsp;32]`、图的 alt 写的是 `Utility Line View SmarTest 7.10.x`、图里是 32 列。
> **两种解释都说得通，原文一条也没排除**：
> **(a) 6.5.3 时确实是 `01 to 16`，后来扩到 32**（版本条目只记变更当时的形态，这在语料里是常态）；
> **(b) 条目里的 `16` 指的不是表头宽度**（比如某种 bit 编号方式，而正文说的是 channel number）。
> **本页把两处并列，不判哪个对，也不替任何一处改数。**
>
> **⑤ 三条 bullet 的顺序与界面上的左右顺序不一致，而且第三个图标没有名字。** bullet 顺序是
> Setup Preferences → Refresh → `The center icon`，而图证（`70662.jpg`）的左右顺序是
> `Refresh` → `Apply write changes to all` → `Setup preferences`。
> **第三条 bullet 只写 `The center icon`，前两条却给了名字**（`Setup Preferences icon` / `Refresh icon`）——
> **同一组三个图标，命名法不统一。** **本页把两处并列，不替它重排 bullet、也不替第三个图标起名。**
>
> **⑥ `the same settings of` 不是规范英文**（按上下文该是 `the same settings as`）。逐字：
> `Clicking the Setup Preferences icon opens a preference window with the same settings of the Utility Line preference page.`
> ——**本页照原样引，不替它改介词。**
>
> **⑦ `Related information` 五个链接粘成一行，中间没有任何分隔符。** 逐字（**注意五个名字之间一个字都没有**）：
> `Utility lines`＋`Utility Line preference page`＋`Utility Purpose view`＋`Utility Pins editor`＋`DUT interface layout`。
> ——**本页照实说，不替它加分号、逗号或换行。**
>
> **⑧ 图里的标注与正文的名字大小写不一致。** 正文 bullet 写 `Setup Preferences`（**两个词都大写**），
> 图里标的是 `Setup preferences`（**只有第一个词大写**）。
> **这两个写法都不是本页改的**；**而且图里那个字形搜不到**（见上 §11.4 的四档）。
> **本页并列，不替它统一。**
>
> **⑨ 两张图都只有 alt、没有题注，而图二里有 alt 装不下的字。** 两张图的 alt 分别是
> `Utility Line View SmarTest 7.10.x` 与 `Utility Line View icons`；
> **而 `Refresh` / `Apply write changes to all` / `Setup preferences` 这三个标签只存在于图的像素里**——
> **alt 里没有、正文里也没有。** 原文也没有给两张图编号（正文用的是 `The following screen shot` 与
> `The screen shot above` 这种指代）。**本页照实说，不替它补题注或编号。**

`verified: doc-only`
