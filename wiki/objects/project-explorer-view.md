---
type: object
title: Project Explorer view
layer: gui
stage: project
tags: [gui, project, project-explorer, device-directory, workspace, test-method-project, eclipse, navigator]
related: [setup-perspective, project, device-directory, workspace, test-method-project, test-method-class, testmethod, test-program-explorer]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02_Project_Explorer_view.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Project Explorer view

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **595 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02_Project_Explorer_view.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Icon | Function |
|---|---|
| !`Navigator view - collapse button`（raw: `../../../../raw/91709.png`） | Collapses all file trees. |
| !`Navigator view - link with editor button`（raw: `../../../../raw/91710.png`） | Toggles whether the Project Explorer view selection is linked to the active editor. When this option is selected, changing the active editor will automatically update the Project Explorer view selection to the resource being edited. |
| !`Navigator view - menu button`（raw: `../../../../raw/91711.png`） | Provides menu items for sorting and filtering files, creating and selecting working sets. |

<!-- 语法节 end -->

## 是什么

**Project Explorer view 是 `Setup perspective` 里的一个 view，它把 device 目录层次化地画出来。**
原文两句：

> 「The Project Explorer view is part of the [Setup perspective](…01.01.07.02_Setup_perspective.md)
> and provides a hierarchical view of the device directories.」
>
> 「In the Project Explorer view you add (import) or remove devices to your workspace
> and activate the device you are currently working on.」

**所以它是 device 的「工作区管理入口」：import 进来、remove 出去、把某一个 activate 成
「我现在做的这一颗」。** 这三件事**在这一篇里都只出现一次、各一句话，原文没给步骤**。

### 读这一页最重要的一件事：同一节里两段在讲两个不同的东西

**这是本篇最容易读错的地方，原文没有提醒。**

| 段落 | 讲的是 | 关键字 |
|---|---|---|
| **开头两句** | **device**（device 目录 / device 的 import、remove、activate） | `device directories`、`add (import) or remove devices`、`activate the device` |
| **紧接着的 `In this view you can:` 列表** | **test method project 与 class 源文件** | `test method projects`、`class source file`、`shared library` |

**两段之间没有任何过渡句。** 前一段的宾语是 device，后一段的宾语全是 test method 程序代码。
**「这个 view 到底管 device 还是管 test method 代码」——原文等于把两个答案并排放在了一起，本页不替它调和**（推断部分见「出处」）。

### `In this view you can:`——原文给的六件事

| # | 原文 |
|---|---|
| 1 | `Navigate to the elements of test method projects` |
| 2 | `Open and edit a class source file in the editor view` |
| 3 | `Create new projects and class source files` |
| 4 | `Manage existing projects, class source files, and methods (cut, paste, delete, move or rename)` |
| 5 | **`Build the test method shared library by compiling your sources`** |
| 6 | `Import and remove external test method projects to/from the explorer` |

**第 5 项值得单看一眼：编译（build 共享库）是从这个 view 发起的。**
**它是一个「浏览 + 编辑 + 编译 + 增删」的复合入口**，不是只读的树。

**第 6 项里的 import / remove 宾语是 `test method projects`**，
和第 1 条开头的「import / remove **devices**」**用的是一对词、宾语不同**——
这正是上面那个「同一节讲两件事」的又一处痕迹。

### 右键菜单

> 「Right-click any file in the Project Explorer view to open a shortcut menu that allows you to
> perform operations such as copying, moving, creating new files, or comparing files with each other.」

**原文列的是「例如」**（`such as`），**不是完整清单**——所以菜单里还有什么，本页不知道。

### 工具栏上的三个图标

原文这张表在语料里**被压平了**（见「出处」⚠️ ①），下面按「图标 ⇄ 功能」成对复原：

| 图标（alt 文本） | 功能 |
|---|---|
| `Navigator view - collapse button` | `Collapses all file trees.` |
| `Navigator view - link with editor button` | **切换「view 的选中是否跟随活动编辑器」**。勾上以后，**换编辑器会自动把 Project Explorer 的选中移到正在编辑的那个资源上** |
| `Navigator view - menu button` | 给出排序、过滤文件的菜单项，以及创建与选择 working sets |

> **⚠️ 三个 alt 文本里都还写着旧名字 `Navigator view`**，
> 而这一篇的版本段说 `SmarTest 6.5.3: The Navigator view is renamed as Project Explorer view.`
> ——**这是「改名了但图没重做」留下的痕迹**（文档事实：alt 文本逐字如此）。
> **拿 `Navigator view` 去搜图是搜得到的**，这一点对找资料有用。

**三个图标都只有 alt 文本描述，本页没看图**，所以**它们长什么样本页不知道**。

## 典型用法

**这一篇没有操作节。** 原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## Results`。

**能照做的只有两条，而且都在别的页里**：

| 想干的事 | 本篇给什么 |
|---|---|
| import device / remove device / activate device | **只说了这个 view 能办**（一句话），**步骤推给了子主题 `Working with Project Explorer view`（本页没读）** |
| 搞清楚 device 目录本身长什么样 | **不给**，推给 `Device Directories` 子主题（**没读**） |
| 右键菜单具体有哪些项 | **只给「例如」三条半**（copy / move / 新建文件 / 互相比对） |
| 工具栏三个按钮 | 上面那张表就是全部 |

**关于 `link with editor` 那一个按钮，有一条实用判断**：
**它管的是「选中跟不跟着编辑器走」**，原文写得很具体——
`changing the active editor will automatically update the Project Explorer view selection to the
resource being edited`。**换句话说，它是一个「同步开关」，不是过滤开关。**

**另一个子主题 `SmarTest lock mechanism` 名字看起来很重要**（文件被锁住时怎么办），
**但本篇一个字没讲**，本页也没读那一篇。

## 和谁有关

- [[setup-perspective]] — **父页**。原文第一句就说这个 view `is part of the Setup perspective`，
  并且链接指向它。**它在父页里排第几、父页还装了哪些 view，本页不写**——
  那是父页 source（`01.01.07.02`）的事，**本页没有以它为据**。
- [[project]] — 本页 `stage: project` 的理由：它管的是 device 与 test method project 的组织。
- [[device-directory]] — **本页画的就是它**（`hierarchical view of the device directories`）。
  本页只有「是一棵树」这一句；**目录里有哪些子目录、每个子目录放什么，在 [[device-directory]] 那一页**。
- [[workspace]] — 原文说 import / remove 的落点是 **`your workspace`**；**workspace 本身是什么，本篇没讲**。
- [[test-method-project]]、[[test-method-class]]、[[testmethod]] — `In this view you can:` 那六条
  管的**全是 test method 侧的 project / class / shared library**；
  **这三个页讲的是那些对象本身，本页讲的是从这个 view 怎么够到它们**。
  原文里没有出现 `test method project` 这个页名对应的专页链接，**本页只按原文的用词写**。
- [[test-program-explorer]] — **本篇一个字都没提到它。** 本页把它列在这里只是为了标出
  **「同类的另一个 Explorer」**这个位置；**两者分工谁是上游，本页不下结论**。
- **清单外、本页不链（用反引号写名字）**：`Working Sets`、`SmarTest lock mechanism`、
  `Device Directories`、`Working with Project Explorer view`、`Problems View`
  —— 前四个是本篇的四个子主题，**都不在 `prose-allowlist.txt` 里**。

## 版本

原文 `## Functional changes` 段两条：

| 条目 | 读法 |
|---|---|
| `Introduced before SmarTest 6.3.2` | **哨兵值，不是「6.3.2 的变更」**——意思是「**在本文档集覆盖范围开始之前就已经有了**」（§11.2 ②）。**照字面读会生成一条「6.3.2 新增了 Project Explorer view」的假信息。** |
| `SmarTest 6.5.3: The Navigator view is renamed as Project Explorer view.` | **6.5.3 之前它叫 `Navigator view`。** 这是本篇唯一一条真实变更，**而且它和正文的图对不上**——图里的 alt 文本还是旧名字（见上） |

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02_Project_Explorer_view.md`（TDC `91566.htm`）

**本页没做的**：

- **四个子主题一篇没读**：`01.01.08.02.01_Working_with_Project_Explorer_view`、
  `01.01.08.02.02_Working_Sets`、`01.01.08.02.03_Device_Directories`、
  `01.01.08.02.04_SmarTest_lock_mechanism`。
  **所以 import / remove / activate device 的具体步骤、working sets 是什么、
  device 目录的结构、锁机制，本页一个字都没有。** 本页只有原文那两句。
- **`Related information` 的两篇没读**：`Perspectives`（父篇）、`Views`。
- **一张图没看**：`raw/91705.png`（`Project Explorer view`）、以及工具栏那三个图标的图
  （`91709.png` / `91710.png` / `91711.png`）。**本页没有任何来自图的结论**——
  三个图标长什么样、树长什么样，都不知道。
- **父页 [[setup-perspective]] 的 source（`01.01.07.02_Setup_perspective.md`）没有作为本页依据**——
  本页说「它是 Setup perspective 的一部分」，依据是**本篇自己那一句**。
  所以**「父页里还装了哪些 view、本页排第几」本页一个字都没写**。
- **左边「两段讲两个东西」那一节，本页只并置、不判定**：
  原文没有一句话说明这两段的关系，**本页没有推断出「device 与 test method 是两棵不同的树」
  这样的结论**——那需要读子主题 `Device Directories`，本页没读。
- **本页没在真机上打开过这个 view**（`verified: doc-only`）。

> ⚠️ **本篇的三处语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **工具栏那张表被压平成「管道行 + 空行」**，表头两格各自成了独立段落。逐字是
> ` |` / `Icon` / ` |` / `Function` / ` |`，**每个单元格之间都夹着空行**。
> 本页上面那张三行表是**按「图标 → 功能」的相邻关系复原**的，**不是原文的排版**。
> ② **图标的 alt 文本用的是改名前的旧名**：`Navigator view - collapse button`、
> `Navigator view - link with editor button`、`Navigator view - menu button`。
> ③ **`## Related information` 里两个链接中间没有任何分隔符**（逐字引）：
> `[Perspectives](<01.01.07_Perspectives.md>)[Views](<01.01.08_Views.md>)`

`verified: doc-only`
