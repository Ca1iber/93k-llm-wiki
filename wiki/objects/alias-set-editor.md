---
type: object
title: Alias Set Editor
layer: gui
stage: pin
tags: [pin, gui, alias-set, pin-alias, package-pin, pin-configuration, search-view, test-program-explorer]
related: [pin-configuration-tool, pin-group-editor, port-editor, utility-purpose-editor, pin-configuration-file, pin, digital-pins-editor, dps-pins-editor, dc-scale-limits-editor, mapping-pin, test-program-explorer, smartest-6.5.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.04_Alias_Set_Editor.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Alias Set Editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Alias Set Editor 是 pin alias set 的编辑器：一个 alias set 里放一组「别名 ↔ 封装针名」的对照。**
原文开门两句逐字：

> 「This editor shows the content of pin alias sets including the package pin names and pin
> aliases. The following figure displays an alias set named Trans_IO.」

第二句逐字给出它能做哪五件事：

> 「With this editor, you can create, edit, copy, paste, and delete pin alias sets. Copying,
> pasting, and deleting the pin alias sets are similar to how you work with pin groups. See below
> for information on creating and editing pin alias sets.」

**五件事里只展开了两件**（create / edit），**copy / paste / delete 三件被推给
「和 pin group 的做法相似」**——**pin group 那边怎么做，本篇没有，本页也没有**（见 `## 出处`）。

### 两列的方向：`Alias` 是别名，`Pin` 是封装针名

编辑时的两列，原文逐字：

> 「  - In the Alias column, enter the alias for this pin.」

> 「  - In the Pin column, enter the package pin name defined in the Pin Setting Editors.」

**方向容易读反，这里要点明：左列 `Alias` 放的是「别名」**（信号名那一侧），
**右列 `Pin` 放的是「封装针名」（package pin name）**——
**即 alias → package pin，不是反过来。**
`Pin` 那一列还有个硬前置：**它的值必须已经在 `Pin Setting Editors` 里定义过**
（`defined in the Pin Setting Editors`）——**所以这个编辑器不能凭空造针**（见 `## 和谁有关`）。

### 一个 alias set 里放什么（图证 · `112400.png`）

原文第一句后面直接跟图。**逐格读出来**：

| 位置 | 图上内容 |
|---|---|
| 窗口标题 | **`*Trans_IO`**（**开头有一个 `*`**，原文没解释；这与 [[dc-scale-limits-editor]] 那篇的窗口标题同形） |
| 表头 | 行号、**`Alias`**、**`Pin`** ——**只有这两列**，与原文那两条 bullet 逐字对得上 |
| 第 1 行 | `CLK` / `CP` |
| 第 2 行 | `write` / `S0` |
| 第 3 行 | `read` / `S1` |

**图上答掉的三件事（正文里都没有）：**

1. **别名可以大小写混排**（`CLK` 大写、`write` / `read` 小写）——**原文没有给命名规则。**
2. **一个 alias set 就是「一张两列的表」**，主键是别名那一列（图上没有重名行）。
3. **名字 `Trans_IO` 只出现在标题栏**，正文那句 `an alias set named Trans_IO` 靠的正是它。

### 一个针的全部别名长什么样（图证 · `112406.png`）

原文 `## Displaying all aliases for one pin` 说：右键点在**那一行的行号**上，选 `Aliases per Pin`，
就会打开 `Search view`；**并且给了每一行的格式**（逐字，原文是代码块）：

```
<alias_set_name>::<alias_name>
```

图 `112406.png` 逐格读出来：

| 位置 | 图上内容 |
|---|---|
| 窗口标题 | **`Search`** |
| 面板标题 | **`Aliases of "CP"`**（**针名带双引号**） |
| 第 1 行 | `FUNC::CLK` |
| 第 2 行 | `USB::USB_CLK` |

**这张图正好把格式用了一遍**，而且**答掉了一件正文没说的事**：

- **一个针的别名可以来自多个 alias set**——`CP` 的别名来自 `FUNC` 与 `USB` **两个** set。
  原文那句 `When there are aliases for a pin in one or more alias sets` 用的正是 `one or more`，
  **图上给的是 `more` 这一种**。
- **注意图 1 与图 2 的 set 名对不上**：图 1 那个 set 叫 `Trans_IO`，
  而图 2 里 `CP` 的两个别名来自 `FUNC` 与 `USB`——**`Trans_IO` 在图 2 里没有出现**。
  **两张图是两次不同的截图，原文没有说明它们之间的关系**（本页照实并列，不替它连）。
- **`Aliases of "CP"` 这个标题原文没有**，只有 `The Search view opens displaying all the
  aliases for this pin.` 一句。

**哪些字算图证，逐个 `grep -F` 核过**：`Trans_IO`（1 次）、`Search`（2 次）**在本篇 raw 里搜得到**；
而 `Aliases of`、`FUNC`、`USB`、`CLK`、`write`、`read`、`CP`、`S0`、`S1` **在本篇 raw 里都是 0 次**
——**所以上两张表里只有后半串算图证**（§11.4 要的就是这条分界）。
`Alias` / `Pin` 这两个列名**在 raw 里搜得到**（各出现于那两条 bullet），**不算图证。**

## 典型用法

**原文有三个过程型 `##` 段**（`## Creating a pin alias set` / `## Editing an alias set` /
`## Displaying all aliases for one pin`），**但没有 `## Procedure`、没有 `## Before you begin`、
没有 `## What to do next`、没有 `## Subtopics`**（本页逐字查过，`Subtopics` 0 次）。

### 建一个 alias set（原文两步）

1. `In the Test Program Explorer view, right-click Alias Sets and choose New.`
   →**`The New Alias window opens.`**
2. `Enter the alias set name in the New Alias text box and click OK.`

**⚠️ 建的过程里没有让你填任何「别名 ↔ 针」的对照**——**对照是在编辑阶段才填的**（下一节）。

### 编辑它（原文逐步）

1. **打开那个 set**：`In the Alias Set Editor, open the alias set you want to edit.`
   ——**新建的那个，`the editable region is empty`。**
2. **填一对**：左列填别名、右列填封装针名（两列原文见上）。
3. **`After you have finished defining the first pair of alias and its related package pin name,
   press the tab key. A new line is created.`** ——**Tab 键换行是原文给的唯一一个键。**
4. **继续**：`Continue to enter the alias for the second package pin names.`
5. **收尾**：`When you finish entering the aliases for your desired pins, apply the data and save
   the pin configuration file.` ——**两步：apply、然后 save pin configuration file。**

### 查一个针的全部别名

1. **`right-click the line number of the pin, and choose Aliases per Pin.`**
   ——**注意右键点的是行号格，不是针名。**
2. `The Search view opens displaying all the aliases for this pin.`
3. **每行按 `<alias_set_name>::<alias_name>` 读**：`::` 前是 set 名、后是别名。

**从原文能落成的动作：**

| 要做的 | 依据 |
|---|---|
| 建一个 set | Test Program Explorer → 右键 `Alias Sets` → `New` → 填名 → `OK` |
| 加一对别名 | `Alias` 列填别名、`Pin` 列填**已在 `Pin Setting Editors` 里定义过**的封装针名 |
| 连续加 | **每填完一对按 Tab**，自动新起一行 |
| 让改动生效 | **apply，然后 save pin configuration file**（原文两句连着说） |
| 查一个针有哪些别名 | 右键**行号** → `Aliases per Pin` |
| copy / paste / delete | **原文只说「和在 pin group 上的做法相似」，具体步骤本篇没有** |

## 和谁有关

- [[pin-configuration-tool]] — **本编辑器是它的一个 element**。那页的元素表里有
  `Alias Sets`，**而且那页记的父文档 `Functional changes` 里有一条
  `SmarTest 6.5.2: The Alias Sets editor is added.`**——**与本页 `## 版本` 那条对得上**
  （**注意那页用的是 `Alias Sets` 这个复数形式，见 `## 出处` ②**）。
  **⚠️ 这一条不是本页 raw 写的**（本页 raw 里 `Pin Configuration` 出现 0 次），
  **出自 wiki 的 [[pin-configuration-tool]] 页；本页没有回那篇原文核。**
- [[pin-group-editor]] — **原文主动点名的一对**：
  `Copying, pasting, and deleting the pin alias sets are similar to how you work with pin groups.`
  ——**copy / paste / delete 三个动作的做法按 pin group 那一套走。**
  **本页只有这句「相似」，pin group 那边具体怎么做本页没有**（那页本页没读）。
- [[port-editor]] / [[utility-purpose-editor]] — **同 `stage: pin` 的同族编辑器**，
  **同为 [[pin-configuration-tool]] 的 element**（归属出自那页，不是本页 raw）。
  **三者的 `## Example` 都是「一张界面截图」**，**本页 raw 与那两篇 raw 互相都没提对方。**
- [[pin-configuration-file]] — **落盘侧，而且是原文点名的一步**：
  `apply the data and save the pin configuration file.` ——
  **本页只给出「要 save 这个文件」这一个动作，文件在哪、什么格式，全在那页。**
- [[pin]] — **`Pin` 那一列填的是 `the package pin name`**，
  而且**必须 `defined in the Pin Setting Editors`**——**即「针」先存在，别名才能挂在它上面。**
  **所以这是上下游：针定义在前，alias set 在后。** 针侧的规矩在那页，本页没读。
- [[mapping-pin]] — **（推断）三侧对照**。本页是 GUI 侧，[[mapping-pin]] 收的是
  「某个对象在 GUI / 文件 / L1 三侧各是谁」。**本页 raw 里没有命令，只有一个文件
  （pin configuration file），所以这条关系本页只有一半依据。**
- [[test-program-explorer]] — **建 set 的入口就在它里面**（`In the Test Program Explorer view,
  right-click Alias Sets and choose New.`）。**本页只有这一个菜单路径，那页怎么用本页没读。**
- `Pin Setting Editors`（**未建**）— **本页的一处上游依赖**：`Pin` 列的值必须在那里定义过。
  **它是什么、在哪、有几个，原文一个字没解释**（见 `## 出处` ⑤）。
- `Search view`（**未建、不在 allowlist，故用反引号**）— **本页第三个过程的落点**
  （`The Search view opens …`）。**它的其它能力、怎么关，本篇没有。**
- `Alias set`（**未建**）— **本页 raw `## Related information` 唯一的链接**
  （`02.08.04.18.01.04_Alias_set.md`）。**它才是讲 alias set 这个概念的那一篇，
  而本页只讲编辑它的 GUI。**
- `New Alias` 窗口 / `New Alias` 文本框（**未建**）— **建 set 那一步的两个名字**，
  **原文对它们只有一句形容量（`The New Alias window opens.`）。**
- `Aliases per Pin`（**未建**）— 右键菜单项。

## 版本

原文 `## Functional changes` **只有一条**，逐字：

- `Introduced in SmarTest 6.5.2`

**这一条不是 §11.2 ② 那个哨兵值**（不是 `Introduced before SmarTest 6.3.2`）——
**本编辑器是 SmarTest 6.5.2 引入的，是一条真版本事实。**

**（推断）6.5.2 这个数与 [[pin-configuration-tool]] 那页记的父文档条目一致**：
那页逐字记着 `SmarTest 6.5.2: The Alias Sets editor is added.`。
**依据是两边同一个版本号 + 同一个功能名；本页没有回那篇原文核，所以这是推断。**

**与 wiki 目标版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（§11），
而这一篇**只有 6.5.2 一条**——**所以 6.5.2 到 7.10.3 之间这个编辑器有没有改过
（列变过、名字变过），语料里没有依据。**

详见 [[smartest-6.5.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.04_Alias_Set_Editor.md`
（`112366.htm`，52 行）——**整篇读完**。

**本页做了什么**：

- **读了本篇两张图**（`112400.png` 编辑器界面、`112406.png` Search view），**逐格读过**。
  图答掉的那几件事写进了「是什么」；**图里读到的字一律没有进 `>` 引文块**——
  引文块的含义是「这段能在 raw 文本里搜到」，**图上的字搜不到**（§11.4）。
- **为了核「本编辑器归谁管、哪个版本引入的」两句，读了 wiki 的
  `wiki/objects/pin-configuration-tool.md`**（**是 wiki 页，不是 raw**）。
  结论只写在「和谁有关」「版本」两处，**每条都标了「不是本页 raw 写的」。**

**本页没做的**：

- **本页 raw 里没有参数表**，也没有 `## Syntax` / `## Parameters` / `## Example` 段
  （本页逐字查过，`example` 0 次、`Subtopics` 0 次）——**所以「语法 / 参数」节是空的**，
  **本页没有任何一格是从脚本抽的逐字表来的**；凡加 `>` 的地方才是逐字原文。
- **`Alias set` 没读** —— **这是本页最大的空缺**：本页只讲「怎么编辑」，
  **「alias set 是什么、为什么要它、别名在哪儿被谁用」整个在那篇。**
- **[[pin-group-editor]] 没读** —— 所以 **copy / paste / delete 三件事的实际做法本页没有**，
  只有原文那句「和 pin group 相似」。
- **`Pin Setting Editors` 没读、原文也没解释** —— 所以
  `the package pin name defined in the Pin Setting Editors` 里的那组编辑器是什么，
  **本页和原文一样不知道**。
- **两张图之间的关系本页没有**：`Trans_IO` 与 `FUNC` / `USB` 是不是同一份配置，
  原文没有一句话，**本页只并列，不替它连**。
- **`Search view` 没读**（本 wiki 也没有它的页）—— 所以那个视图除了列别名还能做什么，
  本页没有。**注意它不是 [[spec-search]]**（那是另一回事，本页没有那页的事实）。
- **`02.06` 的命令原文一篇没读** —— **本页正文没有一条命令事实。**
- **没有实跑。** 没有在机台上开过这个编辑器、没有建过 alias set。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pin.md`。
- **语料里另有一篇同名的 `Alias Set Editor reference`
  （`99_Unlisted_or_Unreferenced/99.0011_Alias_Set_Editor_reference.md`，本页是从语料目录里看到的），
  本页没读它。** 本页 `sources:` 只有上面那一篇，**而 `sources:` 本页不许动**（§6.1）——
  **所以那一篇里的任何内容本页一个字都没有**，它是不是同一对象的另一份说明，本页不知道。

> ⚠️ **本篇的语料瑕疵与对不上的地方，照实记、一处都没替它改**：
>
> **① 图的 alt 文字用了复数，别处一律用单数。** 逐字：`![Alias Sets Editor](<…/112400.png>)`
> ——**alt 是 `Alias Sets Editor`（Sets 复数）**，而本篇的 `title`、`# ` 标题、
> 正文两处说的都是 `Alias Set Editor`（本页逐字数过：`Alias Set Editor` 4 次、
> `Alias Sets Editor` 1 次，**那 1 次就是 alt**）。
> **本页照抄 alt 的复数形式，不替它统一。**
>
> **② 同一个东西在语料里也有复数写法。** [[pin-configuration-tool]] 那页记的父文档条目逐字是
> `SmarTest 6.5.2: The Alias Sets editor is added.`（**也是复数**）。
> **两处复数、其余处单数，原文没有统一。** （**这一条引自 wiki 页，不是本页 raw。**）
>
> **③ `## Creating a pin alias set` 那两条 bullet 被一句散文从中间劈开。** 逐字结构：
> ```
> - In the Test Program Explorer view, right-click Alias Sets and choose New.
>
> The New Alias window opens.
>
> - Enter the alias set name in the New Alias text box and click OK.
> ```
> ——**`The New Alias window opens.` 是夹在两条 bullet 之间的一句独立段落**，
> **它既不是第一条 bullet 的续行，也不是第二条的开头**（markdown 里它会把列表截断）。
> **本页在「典型用法」里把它按语义顺序写回第 1 步的结果，引文里照原样。**
>
> **④ 段标题说「alias set」，窗口说「Alias」。** 段标题逐字是 `## Creating a pin alias set`，
> 而窗口与文本框逐字是 `The New Alias window opens.` 与 `the New Alias text box`
> ——**`New Alias` 后面没有 `Set`**。**本页照实并列，不替它统一。**
>
> **⑤ `Pin Setting Editors` 是个只出现一次的专名。**
> 逐字：`enter the package pin name defined in the Pin Setting Editors.`
> ——**本篇别处再没提过它，也没有链接**（本篇的 `## Related information` 只有一个链接，
> 而且链的是 `Alias set`，**不是它**）。**所以这个上游依赖没有出口，原文也没给。**
>
> **⑥ `Continue to enter the alias for the second package pin names.` 单复数打架。**
> ——**`the second` 是单数、`names` 是复数**；**而且这一句只提了别名那一列，
> 没再提 `Pin` 列**（上一句才有两列）。**本页照抄，不替它改。**
>
> **⑦ 两张图的命名不一致，而且原文没有把它们串起来。**
> 图 1 的 set 叫 `Trans_IO`（正文那句也这么说），**图 2 里 `CP` 的两个别名却来自
> `FUNC` 与 `USB`**——**`Trans_IO` 在图 2 里 0 次**。
> **两张图是两次不同配置的截图，原文一个字没交待其间关系。本页并列，不替它连。**
>
> **⑧ 图 1 的标题栏带一个 `*`。** 逐字读出来是 `*Trans_IO`
> ——**正文对它的全部说明只有 `an alias set named Trans_IO`，`*` 是什么原文没说。**
> **本页不猜**（[[dc-scale-limits-editor]] 那篇的截图标题也带同一个 `*`，
> **那一条引自本 wiki 的另一页，不是本篇 raw。**）
>
> **⑨ `## Related information` 只有一个链接。** 逐字：`[Alias set](<02.08.04.18.01.04_Alias_set.md>)`
> ——**它没跟别的链接粘在一起**（对照 [[dscp]] / [[dc-scale-limits-editor]] / [[port-editor]]
> 三篇同位置的粘连毛病，**本篇没有这个毛病**，但**只有一条链接本身也比同类页少**）。
>
> **⑩ §11.2 ① 那种编码损坏本篇没有。** 本页查过：本篇**只有 ASCII**——
> CJK 字符 0 个、U+00A0 0 个、`鈥` 0 个、`鈭` 0 个。
> （对照：同族的 [[port-editor]] 那篇有一个 `鈭?` 坏字，**本篇一个都没有。**）
> **§11.2 ⑤ 那个整词替换（`DC/DC power units`）本篇 0 命中。**

`verified: doc-only`
