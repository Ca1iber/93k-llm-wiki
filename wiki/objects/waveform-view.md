---
type: object
title: Waveform View
layer: gui
stage: timing
tags: [waveform-view, gui, smatest-work-center, debugging, array-variables, signal-analyzer]
related: [signal-analyzer, debug-view, debug-perspective, timing]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.12_Waveform_View.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Waveform View

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Waveform View 是 SmarTest Work Center 里的一个调试期查看器：把「你在调试器里高亮的一个
数组变量」画成图。** 原文第一句：

> 「This view graphically shows the contents of an array selected in the Editor view on debugging.」

**触发方式（第二句逐字）**：

> 「If you highlight an array variable with the mouse during debugging, you can graphically view the
> captured waveform or calculated results. The following array variable types are supported.」

**两个要点**：**它是 `on debugging` 才有的**（调试期），
**对象是 `an array selected in the Editor view`**（`Editor view` 那一侧本页没读，见「出处」）。
**它 6.5.2 以前叫 Quick Viewer**——版本段明写了这次改名（见「版本」），
而**篇内还留着一处旧名**（见「出处」⚠️ ③）。

### 支持哪些变量类型（11 条，逐字）

原文用一个清单列全了：

> 「int[ ], unsigned int[ ], short[ ], long[ ], unsigned short[ ], and unsigned long[ ]」

> 「double[ ] and long double [ ]」

> 「float[ ]」

> 「ARRAY_D」

> 「ARRAY_I」

> 「ARRAY_F」

> 「ARRAY_COMPLEX」

> 「Wave<INT>, Wave<DOUBLE>, Wave<FLOAT> and Wave<COMPLEX>」

> 「the element of the array of ARRAY_D, ARRAY_I, ARRAY_F, ARRAY_COMPLEX」

> 「std::vector<int>, std::vector<double>」

> 「the element of std::vector<ARRAY_D>, std::vector<ARRAY_I>, std::vector<ARRAY_F>, std::vector<ARRAY_COMPLEX>」

按家族归一下（**归类是本页做的，原文是平铺的 11 条**）：

| 家族 | 支持的东西 |
|---|---|
| **C++ 内建标量数组** | `int[ ]`, `unsigned int[ ]`, `short[ ]`, `long[ ]`, `unsigned short[ ]`, `unsigned long[ ]`, `double[ ]`, `long double [ ]`, `float[ ]` |
| **`ARRAY_*` 类型** | `ARRAY_D`, `ARRAY_I`, `ARRAY_F`, `ARRAY_COMPLEX` |
| **`Wave<>` 模板** | `Wave<INT>`, `Wave<DOUBLE>`, `Wave<FLOAT>`, `Wave<COMPLEX>` |
| **`std::vector`** | `std::vector<int>`, `std::vector<double>` |
| **「元素」两种** | `ARRAY_*` 数组的元素；`std::vector<ARRAY_*>` 的元素（**7.2.1 加，见「版本」**） |

### 标题栏：变量名 + 类型

> 「On the headline, the variable name and data type are shown.」

**这句有图证**：`raw/141206.png` 的标题栏读出来是 **`ARRAY_COMPLEX cData`**——
**变量名 `cData` + 类型 `ARRAY_COMPLEX`**（**图证**，见「出处」）；
**这张图搜不到，只能自己开图看**（§11.4）。

### 数组怎么变成图：三条规则

> 「The array data is handled as follows:」

> 「X-axis: DC/DC power units of the array elements」

> 「Y-axis: Values of the array elements」

> 「The graph is automatically scaled based on the maximum value of the array elements.」

| 轴 | 原文 | 怎么读 |
|---|---|---|
| **X 轴** | `X-axis: DC/DC power units of the array elements` | **⚠️ 这一句是坏串**：`DC/DC power units` 应为 **`Index`**（§11.2 ⑤ 那一族）。**上游 `.htm` 里就是坏的**，本页照原样引，见「出处」⚠️ ① |
| **Y 轴** | `Y-axis: Values of the array elements` | 数组元素的值 |
| **缩放** | `The graph is automatically scaled based on the maximum value of the array elements.` | **自动**，以数组元素的最大值为准——**没有手设范围的入口**（原文只写了这一句） |

**所以图的语义是「下标 → 值」**（**推断**：依据是 Y 轴那句 `Values of the array elements`
与 X 轴那句的平行结构、以及「每个点一行」的 Paste 数据格式；
**本篇没有一句直接写「X 轴是下标」**——它写的是那个坏串）。

### 和 Signal Analyzer 的分工

> 「You can open the Signal Analyzer tool from here if you need to inspect more details or apply
> calculation algorithm for signal analysis.」

**分工一句话**：**Waveform View 是「看一眼」的，Signal Analyzer 是「细看 / 算」的**
（→ [[signal-analyzer]]）。**这句话是原文给的**，而两个工具各自的能力边界本篇没写。

### Toolbar：五条

**这一段原文档是一张表（Icon / Command / Description）**，
而语料压平后**每个格子各占一行**（所以它在这份 md 里已不是一张连续表格）。
**注意「语法 / 参数」节为空不是因为这张表**——脚本自己的理由是
本篇没有 `Syntax` / `Parameters` / `Example` 这类**段标记**，那是另一条判据。
下表是本页按三个列名重组的结果（**重组是本页做的**），**每格文字逐字**：

| Command | Description（逐字） | Icon |
|---|---|---|
| **`Clear Waveform`** | `Clear the displayed waveform data with the headline in this view.` | `raw/107074.png`——**alt 还写着旧名 `icon - Clear Quick Viewer`**（见「出处」⚠️ ③） |
| **`Show Waveform on Signal Analyzer`** | `Launch up the Signal Analyzer tool, and the waveform is shown in the tool to analysis the waveform.` | `raw/107075.png`（alt `icon - Run Signal Analyzer`） |
| **`Menu`** | `Click the triangle icon to open a menu of items specific to this view. You can select a menu item from a shortcut menu. In this view you can choose Save Trace As or Save Graph As.` | `raw/64022.png`（alt `icon - menu`） |
| **`Minimize`** | `Minimizes this view.` | **原文这一格是空的**（见下） |
| **`Maximize`** | `Maximizes this view.` | `raw/107035.png`（alt `Maximize button`） |

> **`Minimize` 那一行的图标格在原文里就是空的**——`raw/107073.htm` 里那一格写的是
> `&nbsp;`，**不是转换丢了一张图**（§11.2 ⑥ 的判法：去看上游 `.htm`）。
> **另外四个小图标本页都打开了**（三个 99–679 字节、`107035.png` 389 字节）：
> **图太小，除形状外读不出任何字**（**图证**，见「出处」）。

### `Menu` 底下的两条命令

> 「In this view you can choose Save Trace As or Save Graph As.」

**原文接下来用两个子项展开**：

**① `Save Trace as...`**（逐字）：

> 「Save the displayed waveform into an ASCII file. This file format is the same as Save Trace As...
> of the Signal Analyzer tool. The ASCII file can be opened in waveform view for later usage. (See
> Displaying the ASCII waveform file in the waveform view.)」

**两条附注**（都在原文里）：

> 「If more than one waveform is displayed (i.e. an ARRAY_COMPLEX) the user first has to select which
> one of the traces should be saved. To do that, a dialog with a selection list containing all traces
> is presented before the usual file dialog [see screenshot below].」

**这一条有图证**——`raw/141206.png` 里那个对话框标题是 `Select Target Trace`，
`Trace to save:` 下拉里是 **`Real`** 与 **`Img`**，而图例把两条曲线标成
**黄色 `Real` / 青色 `Img`**（**图证**，见「出处」；**其中截图的版本不确定**，见 ⚠️ ⑤）。
**注意原文那句里的方括号旁白 `[see screenshot below]` 是原文自带的**，不是本页加的。

**② `Save Graph As...`**（逐字，**注意这句原文末尾没有句号**）：

> 「Save Graph As... Save the displayed graph into a XML file containing the waveform and metadata
> as the heading, legend etc. This file format is the same as the graph file of the Signal Analyzer」

**两条命令的产物格式是这一节最有用的信息**：

| 命令 | 产物 | 归属 |
|---|---|---|
| `Save Trace as...` | **ASCII 文件** | **与 Signal Analyzer 的 `Save Trace As...` 同格式**；可再被 waveform view 打开 |
| `Save Graph As...` | **XML 文件**（含 waveform + metadata：heading、legend 等） | **与 Signal Analyzer 的 graph file 同格式** |

### Shortcut menu：只有一条 `Paste`

> 「Reads the waveform data from clipboard and displays the data in the waveform view. The copied
> data must be non-encrypted data of ASCII waveform file. Every point of the waveform must be in one
> line in the copied data. The data can be copied from Eclipse editors, terminal window and any other
> Linux editors. An example of the waveform data is shown as below:」

**三条硬条件**：**未加密的 ASCII waveform 文件内容**、**每个点一行**、来源是
**编辑器 / 终端 / 任何 Linux 编辑器**（即剪贴板里的纯文本就行）。

**「每个点一行」是什么意思，原文给了一张图**：`raw/123291.png` 里是一个叫
**`Cosine.ascii`** 的编辑器页签，能读出的行形如
**`10.609488844871521`**（第一行）到 **`110.21152202785015106`**（最后一行）——
**共 11 行，逐行递增的前导数字是点号**
——**图证**，**这张图搜不到**（§11.4），**且截图的版本不明**（见「出处」⚠️ ⑤）。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有编号步骤。**
能从原文拼出来的路径只有三条，全是围绕「数据怎么进出这个视图」的。

**1. 主路径（调试期看图）**——把原文前两句拼起来：

**调试中 → 在 `Editor view` 里用鼠标高亮一个数组变量 → 这个视图把抓到的波形或算出的结果画出来。**

**2. 三种数据流**（这是本页最实用的一张表，全部来自原文）：

| 想做什么 | 走哪条 | 格式要求（原文） |
|---|---|---|
| **看图** | 高亮数组变量 | 变量类型必须在上面的 11 条清单里 |
| **导出留档 / 给别人** | `Menu` → `Save Trace as...` 或 `Save Graph As...` | Trace → **ASCII**；Graph → **XML**（含 heading / legend 等 metadata） |
| **把外面的数据拿进来** | 右键 → `Paste` | **未加密的 ASCII waveform 数据，每个点一行**；来源随便（Eclipse 编辑器 / 终端 / 任何 Linux 编辑器） |

**3. 要看细节 / 要算，就换工具**：

> 「You can open the Signal Analyzer tool from here if you need to inspect more details or apply
> calculation algorithm for signal analysis.」

**入口就是 Toolbar 的 `Show Waveform on Signal Analyzer`**，且**当前这张波形会一起带过去**
（原文：`the waveform is shown in the tool to analysis the waveform.`）。→ [[signal-analyzer]]

**4. 多波形（`ARRAY_COMPLEX`）导出前要先选一条**：
`Save Trace as...` 会**先弹一个选 trace 的对话框，再弹常规文件对话框**
（原文 `a dialog with a selection list containing all traces is presented before the usual file
dialog`）。**图证**：`raw/141206.png` 里就是那个 `Select Target Trace` 对话框。
**而 `Save Graph As...` 有没有同样的「先选 trace」步骤，本篇没写**（**语料未写**）。

**5. 清屏**：Toolbar 的 `Clear Waveform`——按原文，它清的是
`the displayed waveform data with the headline in this view`。

**6. 输入回来的数据长什么样**：见上面 `Cosine.ascii` 那张图证。
**注意原文只给了「长的样子」，没有给文件格式规范**——
所以「一行的两个数之间到底怎么分隔」**本篇答不了**（见「出处」，我在那里把从图上读到的
形状写清楚了，但**那是图证不是文本**）。

## 和谁有关

- [[signal-analyzer]] — **下游工具（本视图的一个出口）**：原文写了
  `You can open the Signal Analyzer tool from here`，而且**两种导出格式都声明与它同格式**
  （`This file format is the same as Save Trace As... of the Signal Analyzer tool.` /
  `This file format is the same as the graph file of the Signal Analyzer`）。
  **「Signal Analyzer 自己能干什么」本篇一个字没写**，见那一页。
- [[debug-view]] / [[debug-perspective]] — **同属调试期（同类，本页自己判的）**：
  本视图的触发前提是 `on debugging`，而 `Editor view` 那一侧**本页没读**
  （`Editor view` 不在 `extract/prose-allowlist.txt` 里，所以本页用反引号写它，没做成链接）。
  **这两个页面与本页是「同一次调试里的不同窗口」——但本篇没有点名它们中的任何一个**（**推断**：
  依据只有 `on debugging` 这个前提，不是文档里的一句对应关系）。
- [[timing]] — **`stage: timing` 的阶段页，但这条归属本页要打个问号。**
  [[timing]] 的 GUI 表里有
  `[[waveform-view]] / wavetable editor | gui | 看/改物理波形表` 一行（**本页读到的 wiki 页**）；
  **而本篇 raw 的第一句说的是「画一个数组变量」**——它**没有任何一句**提到 wavetable、
  device cycle、timing；**`## Functional changes` 七条也全是变量类型与界面改名**。
  **所以「看/改物理波形表」那一格，本篇不支持**；那一格讲的是 **wavetable editor**
  （一个本 wiki 还没有页的工具）。**本页把这个不齐照记下来，不去改 [[timing]] 那一页**（§10）。
- `Editor view`（**未建，且不在 allowlist**）— **数据的来源**：
  原文的 `an array selected in the Editor view on debugging` 说的是它。
  **它长什么样、怎么选数组，本页没有。**
- `Save Trace As...` / `Displaying the ASCII waveform file in the waveform view`（**均未建**）—
  **原文点了名但没给链接的两件事**：前者是 Signal Analyzer 的同名菜单项，
  后者是「把 ASCII 文件再显示回来的做法」——**原文用了圆括号旁白
  `(See Displaying the ASCII waveform file in the waveform view.)`，那一篇本页没读。**

## 版本

**本文档有 `## Functional changes` 段，七条**（逐条照抄）：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.2: Quick Viewer view is renamed to Waveform view.`
- `SmarTest 7.0.3: Support the display of variable type ARRAY_F, Wave<INT>, Wave<DOUBLE> and Wave<FLOAT>.`
- `SmarTest 7.0.3: New shortcut menu Paste.`
- `SmarTest 7.2.1: Added new waveform type ARRAY_COMPLEX.`
- `SmarTest 7.2.1: Support the display of the element of the array of ARRAY_D, ARRAY_I, ARRAY_F, ARRAY_COMPLEX`
- `SmarTest 7.2.1: Support the display of the element of std::vector<ARRAY_D>, std::vector<ARRAY_I>, std::vector<ARRAY_F>, std::vector<ARRAY_COMPLEX>`

| 版本 | 这一版加了什么 |
|---|---|
| **（6.3.2 之前）** | 已有本视图 |
| **6.5.2** | **改名**：Quick Viewer → Waveform view |
| **7.0.3** | **加类型** `ARRAY_F` / `Wave<INT>` / `Wave<DOUBLE>` / `Wave<FLOAT>`；**加 `Paste`** 这条右键命令 |
| **7.2.1** | **加类型 `ARRAY_COMPLEX`**；**加两类「元素」**（`ARRAY_*` 数组的元素、`std::vector<ARRAY_*>` 的元素） |

**三点读法**：

1. **第一条是 §11.2 ② 说的哨兵值**：`Introduced before SmarTest 6.3.2` 的意思是
   「**在本套文档集覆盖范围开始之前就已经有了**」，
   **不许读成「6.3.2 引入了 Waveform view」** → [[smartest-6.3.2]]。
2. **6.5.2 那条解释了一个篇内矛盾**：正文里还留着旧名 `Quick Viewer`
   （`raw/107074.png` 的 alt 是 `icon - Clear Quick Viewer`），**版本段说明这是改名前的残留**
   （见「出处」⚠️ ③）。→ [[smartest-6.5.2]]
3. **7.0.3 与 7.2.1 各两条/三条，与正文那张类型清单对得上**：
   清单里的 `Wave<>` 与 `ARRAY_F` 是 7.0.3 的，`ARRAY_COMPLEX` 与两类「元素」是 7.2.1 的。
   **6.5.2 到 7.0.3 之间（6.5.3 / 6.5.4 / 7.0.0 / 7.0.1 / 7.0.2）没有条目**——
   **这是版本段的空白，不是本页漏抄**。→ [[smartest-7.0.3]] / [[smartest-7.2.1]]

**版本段里没有的东西**（照实记，不替它补）：
**没有**任何一条讲 `Save Trace as...` / `Save Graph As...` 是哪一版加的，
**也没有**一条讲 `Minimize` / `Maximize` / `Clear Waveform` / `Show Waveform on Signal Analyzer`
的图标或名字改过。**所以上面那五个图标的当前形态，本篇无法定版。**

## 出处

`sources:` 一篇：

- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.12_Waveform_View.md`
  （frontmatter 的 `source_topic` 是 `107073.htm`；**3,070 字节 / 124 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节是脚本从这一篇抽的，**它这一节是空的**——
  本篇没有 `Syntax` / `Parameters` / `Example` 这类**段标记**，所以脚本一个字都不收。
  **本页一个字没动这一节**；**本篇也确实没有 `## Errors` / `## Warnings` 段，
  所以本页没有「报错条件」节**——不是漏写（骨架里本来就没有那一节）。
- **本篇 `stage: timing`（骨架给的）与 raw 的关系，本页写了判断**：
  见「和谁有关」里 [[timing]] 那一条，**那是本页的观察，不是本篇的话**。

### 图：**6 张全看了**（§11.4）

**本篇对 `raw/` 有 6 处引用，本页逐张开图读完**——
**其中 2 张有实质内容，4 张是图标（最大 679 字节，除形状外读不出字）**：

| 图 | 字节 | 看出来的东西 |
|---|---|---|
| `raw/141206.png` | 18,678 | **图证**：标题栏 `ARRAY_COMPLEX cData`；Y 轴 0–5、X 轴 0–100；一个 `Select Target Trace` 对话框（`Trace to save:` 下拉里是 `Real` / `Img`）；图例黄 = `Real`、青 = `Img` |
| `raw/123291.png` | 12,652 | **图证**：编辑器页签 `Cosine.ascii`，11 行数据，能读出的行如 `10.609488844871521`（第 10 行）、`110.21152202785015106`（第 11 行） |
| `raw/107075.png` | 679 | 图标，红色波形 + 箭头形状；**太小，读不出字** |
| `raw/107035.png` | 389 | 图标，一个窗口（蓝色标题条 + 浅色体）；**读不出字** |
| `raw/107074.png` | 169 | 图标，一张纸 + 黄色笔的形状；**读不出字** |
| `raw/64022.png` | 99 | 图标，一个深色三角/箭头；**读不出字** |

**⚠️ 图证的两条规矩（§11.4），本页照做**：

- **图里的字搜不到。** 拿 `ARRAY_COMPLEX cData`、`Select Target Trace`、`Cosine.ascii`
  去 raw 里 grep 是 **grep 不到的**——它们**只存在于 `.png` 的像素里**。
  本页凡是从图里读出来的，上文都标了「**图证**」。
- **图没有版本标注。** `raw/141206.png` 与 `raw/123291.png` **都没有 SmarTest 版本号**，
  而**本篇的版本段里也没有一条讲这两个界面改过版**——
  **所以这两张图的版本不明**（**不是「旧」，是「不知道」**）。
  本页从它们读出的结论**只用了结构性的部分**（有哪几条 trace、对话框长什么样、
  数据是「一行一个点」的形状），**没有把它们上面的任何名字当成 7.10.3 的当前名字**。

**图题注核过，没有错位、没有重复**（这一类 GUI 页的常见毛病，本页专门核了）：

| 题注 | 落在哪张图前面 | 对不对 |
|---|---|---|
| `The following picture illustrates the case of a COMPLEX_ARRAY waveform. In this case you need to select which trace will be saved.` | `raw/141206.png` | **对**——图里正是那个选 trace 的对话框 |
| `An example of the waveform data is shown as below:` | `raw/123291.png` | **对**——图里正是那份 `Cosine.ascii` 数据 |

### §10 同题的另一份：`99_Unlisted_or_Unreferenced/99.0072_Waveform_View.md`

**本页查重时发现语料里另有一篇同名的 `Waveform View`**：
`99_Unlisted_or_Unreferenced/99.0072_Waveform_View.md`，`source_topic` 是 **`119275.htm`**，
**356 字节 / 9 行**，**正文只有 `#### Subtopics` 加三条链接**
（`Waveform view`、`Displaying array variables`、`Displaying DC waveforms`）。
**它不是本页的出处，本页也没读它的三个子主题**——
**所以它讲的是不是同一个视图，本页答不了**（**它和本篇不同源：本篇是 `107073.htm`**）。
**记这一条的用处**：按 §10，遇到「两篇同名文档」时先把两份都摆出来，
**本页的结论全部只来自 `107073.htm` 这一份。**

**本页没做的**：

- **`Editor view` 那一侧没读。** 原文说数组是「在 `Editor view` 里选的」，
  **但 `Editor view` 是什么、怎么选、调试怎么起，本页一个字没有。**
- **Signal Analyzer 那一篇没读**（它是本页点名的下游工具，也是两种导出格式的对照物）。
  **所以「ASCII 文件导过去之后能干什么、XML graph file 长什么样」本页没有。**
- **`Save Trace As...`（Signal Analyzer 的同名菜单项）没读。**
- **`Displaying the ASCII waveform file in the waveform view` 没读**——
  原文用圆括号旁白指了它，**所以「导出的 ASCII 怎么再显示回来」本页没有。**
- **`ARRAY_D` / `ARRAY_I` / `ARRAY_F` / `ARRAY_COMPLEX` / `Wave<>` 这些类型自己的页没读**
  （本 wiki 有 `ARRAY_*` 的族吗：**本页没查**）。
  **所以「每种类型各长什么样、它们的 API 是什么」本页没有。**
- **`std::vector` 两种、以及两类「元素」的支持细节**：原文只是列进清单，
  **没有一句讲它们的轴怎么算、元素图怎么画。**
- **没在任何 93K 机台上开过这个视图**（`verified: doc-only`）。
  **所以「Paste 进来的数据到底怎么解析（分隔符是什么）」「X 轴那个坏串（`Index`）在实际界面上写什么」
  本页答不了。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① `X-axis: DC/DC power units of the array elements` —— `DC/DC power units` 是坏串。**
> 按 §11.2 ⑤ 那一族（整词替换，`Index` → `DC/DC power units`），这句应为
> **`X-axis: Index of the array elements`**：判据有两条——
> **①** 它是数组图的 X 轴，而下一句 Y 轴写的是 `Values of the array elements`，
> **两句是平行结构**，X 轴只可能是下标；**②** 同族实例 `dqIndex` → `dqDC/DC power units` 的替换词就是 `Index`。
> **核过上游 `raw/107073.htm`（8,140 字节）：那一行在 `.htm` 里就是
> `X-axis: DC/DC power units of the array elements`**——
> **所以它是⑤那一族（上游就坏的、救不回来），不是①那一族（转换坏的、重做转换能救）**（§11.2 ⑥ 的判法）。
> **本页照原样引这一句，一个字节没改；代价是拿 `Index of the array elements` 去 raw 里搜搜不到。**
> **② 同一个类型名在篇内出现三种写法**：正文写 **`COMPLEX_ARRAY`**
> （`The following picture illustrates the case of a COMPLEX_ARRAY waveform.`）、
> **图的 alt 写 `Complex_Array`**、**而支持清单里写的是 `ARRAY_COMPLEX`**；
> 更硬的一条：**`raw/141206.png` 的标题栏读出来是 `ARRAY_COMPLEX cData`**（**图证**）。
> **所以正字是 `ARRAY_COMPLEX`，另两处是篇内不一致——原文如此，本页三处都照原样引。**
> **③ 旧名 `Quick Viewer` 留在图标 alt 里**：`raw/107074.png` 的 alt 逐字是
> `icon - Clear Quick Viewer`，**而同一行的 Command 列写的是 `Clear Waveform`**。
> **核过上游 `raw/107073.htm`：alt 在 `.htm` 里就是 `icon - Clear Quick Viewer`**——
> **上游自带，不是转换丢的**。**版本段说 6.5.2 已把 Quick Viewer 改名为 Waveform view**，
> **所以这是改名时漏掉的一处 alt。本页不改它。**
> **④ 错的英文照原样引**：`Show Waveform on Signal Analyzer` 那一格写的是
> `Launch up the Signal Analyzer tool, and the waveform is shown in the tool to analysis the waveform.`
> ——**`to analysis the waveform` 应为 `to analyze the waveform`**；
> 另有一处大小写/标点不齐：同一段里先写 `Save Trace As` / `Save Graph As.`，
> 后一个子项写 `Save Graph As...`，**同一篇里三种写法**。
> **两处都照抄，不改。**
> **⑤ 两处 `Save Graph As...` 那一格的原文末尾没有句号**
> （原文那一句的结尾逐字是 `This file format is the same as the graph file of the Signal Analyzer`），
> **本页引它时也没加句号**（§11.1：不许补标点）。
> **⑥ 原文里有一处方括号旁白混在正文中**：`presented before the usual file dialog [see screenshot below].`
> ——**`[see screenshot below]` 是文档自己写给读者的旁白，本页照原样引。**
> **⑦ 坏字：本篇 0 个。** 按 §11.2 ① 的判据（英文文档里出现任何汉字都是坏字）逐字查过，
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。
> **⚠️ 注意 `①` 那条坏串不是这一类**：`DC/DC power units` **全是正常英文**，
> 按「有没有汉字」查是查不出来的——**这正是 §11.2 ⑤ 说它比 ① 危险的地方。**

`verified: doc-only`
