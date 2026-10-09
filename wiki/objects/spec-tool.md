---
type: object
title: Spec Tool
layer: gui
stage: level
tags: [level, spec, spec-set, spec-variable, scope, gui, level-setup-tool]
related: [level-setup-tool, spec-set, level-file, svlr, level, mapping-level]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Spec Tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,430 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.01_Creating_new_specification_sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.16.01_Global_and_local_spec_values__scope_of_the_spec_variable.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1 (without using variables)（取自子主题 General Editing Features of the Spec Tool › Creating new specification sets）

- In the Level Setup tool, select the menu item Select > Edit Specifications.

Alternatively you can go <93000> <Setup> <Spec Tool>.

If the Select specification window opens:

  !`Select specification`（raw: `../../../../agent-html/131014.png`）  In the window click done.

You access `The Spec Tool window`（raw: `02.08.04.30.01_The_Spec_Tool_window.md`）.

- On the menu, click Change > Create Specification.
- Click the equation set 1 NonSpecs in the Eqn Description area.
- Click create.

The Create level spec set window opens.

- Select "1" in the Unused Numbers area.

The line of the selected number will be highlighted in red.

- In the Description field, enter nospecs.
- Click Create.
- In the Select level equation set window, click done.

In the Levels line, the Spec Tool shows the message "modified, download required".

- Click Download(the Down arrow icon in the Spec Tool).

Since the specification "nospecs" has no values, no further action is required.

This level specset is now ready to use in SmarTest.

- In the Test Program Explorer save the levels file.

### Example 1 (using a variable)（取自子主题 General Editing Features of the Spec Tool › Creating new specification sets）

- From the Level Setup window select Select > Edit Specifications. This opens the Spec Tool.
- In the SpecTool, select Change > Create Specification.
- Select the Equation Set 2 specs.
- Click create.

You now see a window with the heading Create level spec set.

- Select 1.

You are defining a specification that points to spec set 1.

- In the Description field, enter Vcc = 4.5V.
- Click create.
- Click done in the Select level equation set window.

You see the variable names for this spec set in the SpecTool Name column.

- Repeat the procedure for all spec variables accordingly.

After you have defined the specifications:

- Click the Download icon (the down arrow in the SpecTool) and check the Report window for errors.
- In the Test Program Explorer right-click the level file and Save.

### Example（取自子主题 General Editing Features of the Spec Tool › How to set up a multiport timing specification › Global and local spec values  scope of the spec variable）

The following table illustrates an example with five ports and different settings of the scope attribute.

Example for settings of the scope attribute
| Spec | PORT 1 | PORT 2 | PORT 3 | PORT 4 | PORT 5 |
|---|---|---|---|---|---|
| f | local | local | local | global | global |
| ts_Sx_CP | global | global | global | global | global |
| th_CP_Sx | global | global | global | global | global |
| ts_IOx_CP | local | local | local | local | local |
| th_CP_IOx | local | local | local | local | local |
| ts_DSx_CP | local | local | local | global | global |
| th_CP_DSx | local | local | local | global | global |
| tw_CP | global | global | global | global | global |
| tw_MR | global | global | global | global | global |

For example, consider the spec "f" of the table above. It is local for PORT 1, PORT 2 and PORT 3 and global for Port 4 and Port 5.

- If, for example, you change the value of "f" at PORT 2 ("f" is local at this port) the value of "f" at all other ports will not change.
- If, for example, you change the value of "f" at PORT 4 ("f" is global at PORT 4) the change automatically applies to PORT 4 and PORT 5 because "f" is global at PORT 4 and PORT 5.Note In the shmoo tool, the distinction between local and global scope must be expressed in the same way as for the `SVLR`（raw: `../02.06_Command_Reference/02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`） command. If you want to change a spec variable locally, you must add the name of the port for which the change is to be made in the following format:  <spec_variable>@<port_name>

<!-- 语法节 end -->

## 是什么

**Spec Tool 是 SmarTest 里编辑 specification（spec，规格值）的那个窗口。** level setup 里
「spec 变量 / spec set / spec 值」这一族东西的 GUI 侧入口就是它。

定义文档 `02.08.04.30_Spec_Tool.md` 自己只有两句实质内容——**一句导语、一份 `Subtopics` 清单**：

> 「This section explains in more detail how to use the Spec Tool. Its features are highlighted and everyday tasks are explained.」

**注意它说的是「本节」，不是「本文」。** 定义文档**没有一个字的操作正文**，内容全在子主题里。
所以本页以下的机制，**依据是本页「语法 / 参数」节逐字抽来的两段子主题原文**（段名里写着来源：
`02.08.04.30.02.01_Creating_new_specification_sets` 与
`02.08.04.30.02.16.01_Global_and_local_spec_values__scope_of_the_spec_variable`）。

### 两条入口

| 从哪进 | 怎么走 |
|---|---|
| **Level Setup tool** | `Select > Edit Specifications` |
| **93000 主菜单** | `<93000> <Setup> <Spec Tool>` |

原文：「Alternatively you can go <93000> <Setup> <Spec Tool>.」——**第二条是绕开 Level Setup tool 的直路。**

### 它编辑什么

- **spec set**：编号**从 `Unused Numbers` 区里挑**（两条例子里都选 `1`），**选中的行标红**，
  再在 `Description` 字段填说明（例子填 `nospecs` / `Vcc = 4.5V`）。
  **编号是人挑的，不是自动递增的。**
- **spec 变量**：填 `Vcc = 4.5V` 那条的原文说明是「You are defining a specification that points to spec set 1.」；
  做完之后「You see the variable names for this spec set in the SpecTool Name column.」
- **spec 挂在 equation set 上**：新建时先在 `Eqn Description` 区点中一个 equation set
  （例子里是 `1 NonSpecs` 与 `Equation Set 2 specs`），再点 `create`；
  随后打开的窗口标题是 `Create level spec set`。

### 生效链路：`modified, download required` → Download → 保存

| 步骤 | 原文要点 |
|---|---|
| 改完 | Levels 行显示 **`modified, download required`** |
| 送硬件 | 点 Spec Tool 里的 **Download**（原文写作「the Down arrow icon in the Spec Tool」） |
| 查错 | 查 **Report window**（用变量那条例子写的是「check the Report window for errors」） |
| 保存 | **在 Test Program Explorer 里保存 levels 文件**（不在这个窗口里） |
| 空的 spec set | 「Since the specification "nospecs" has no values, no further action is required.」 |

**「空 spec set 无需后续动作」值得记住**：只声明、不给值的 spec set 是合法的——
典型用途就是给某个 equation set 一个 NoSpecs（不要 spec 值）的位。

### 最要紧的机制：spec 变量的 scope（global / local）

「语法 / 参数」节那张 scope 表是本页信息量最大的东西。**它回答的是「同一个 spec 变量
在多个 port 上是不是同一个值」。** 原文给的两条规则：

> 「If, for example, you change the value of "f" at PORT 2 ("f" is local at this port) the value of "f" at all other ports will not change.」

> 「If, for example, you change the value of "f" at PORT 4 ("f" is global at PORT 4) the change automatically applies to PORT 4 and PORT 5 because "f" is global at PORT 4 and PORT 5.」

**一句话**：**`local` = 这个 port 自己一份；`global` = 同属 global 的那几个 port 共用一份。**
表头是 `Spec` 加上五个 port 列（`PORT 1` 到 `PORT 5`），**同一个 spec 变量在不同 port 上可以有不同的 scope**——
`f` 就是：PORT 1–3 是 `local`、PORT 4–5 是 `global`。
（**那张表在「语法 / 参数」节里是逐格一行摊开的**——HTML 的表格被压平了。
**要逐格读请回到上面那一节，本页不重排它**：§4 说参数表由脚本抽、不许 LLM 重写。）

**另一条是跨工具的一致性要求**，原文紧接在表后面：

> 「In the shmoo tool, the distinction between local and global scope must be expressed in the same way as for the SVLR command. If you want to change a spec variable locally, you must add the name of the port for which the change is to be made in the following format:  <spec_variable>@<port_name>」

即：**局部改写的写法是 `<spec_variable>@<port_name>`**，而且 **shmoo tool 里必须与 [[svlr]] 用同一种写法。**
**这是本页唯一一处与其他工具（shmoo）显式对齐的要求。**

### ④ 图证：进 Spec Tool 时那个「选 equation set」对话框

「语法 / 参数」节引了一张图：`131014.png`（**alt 文字是 `Select specification`**）。
**本页打开了这张图**（`F:\master-dev\dorm-wsl-sytest\tdc-html\raw\131014.png`）。图上逐字可见的是：

| 图上可见 | 是什么 |
|---|---|
| 标题栏 `Select level equation set` | **对话框的真名** |
| `Regular Expression Filter` | 一个用正则过滤 equation set 的输入框 |
| `Eqn Description` | 下面那个列表的标题 |
| 列表里一行 `1 NonSpecs`（红色高亮） | 与原文「Click the equation set 1 NonSpecs in the Eqn Description area.」对上 |
| 四个按钮 `create` / `filter` / `help` / `done` | 原文只用到 `create` 与 `done` |

**图解决掉的疑问**：原文先写「If the Select specification window opens:」（图注也是 `Select specification`），
后面又写「In the Select level equation set window, click done.」——
**图给了答案：这两个名字指同一个对话框，它的标题栏读作 `Select level equation set`。**

**图里的字在 raw 里 grep 得到，但那些篇都不是本页的来源**：`Select level equation set`（3 篇）、
`Select specification`（3 篇）、`Eqn Description`（3 篇）、`Regular Expression Filter`（**1 篇**）
——9,398 篇 raw md 里能搜到，**可一篇都不在本页 `sources:` 里**。
**本页照样把它算 ④ 图证：本页的来源是这张图，不是那几篇。**
**要核只能自己再开那张图**（拿图里的字去 raw 里 grep，命中的是别的文档，不是依据）。

**图答不了的**：Spec Tool 主窗口长什么样、有哪些菜单、`filter` / `help` 两个按钮干什么、
spec 值在 level 文件里怎么存——**这张图只是个选择对话框**。
（Spec Tool 窗口的图在 `02.08.04.30.01_The_Spec_Tool_window.md`，**本页没读那篇**。）

## 典型用法

### 用法一：建一个不带值的 spec set（NoSpecs）

原文给了完整步骤。**七步**：

| # | 做什么 | 原文要点 |
|---|---|---|
| 1 | 从 Level Setup tool 进 Spec Tool | `Select > Edit Specifications`；或 `<93000> <Setup> <Spec Tool>` |
| 2 | 若弹出 `Select specification` 窗口，先关掉它 | 「In the window click done.」 |
| 3 | 菜单 `Change > Create Specification` | |
| 4 | 在 `Eqn Description` 区点中一个 equation set | 例子里点 `1 NonSpecs` |
| 5 | 点 `create` | 打开 `Create level spec set` 窗口 |
| 6 | 在 `Unused Numbers` 区选一个号 | 例子里选 `1`，**选中的行标红** |
| 7 | `Description` 填说明 → `Create` → 在下一个窗口 `done` | 例子填 `nospecs` |

收尾：Levels 行出现 `modified, download required` → 点 **Download** →
「Since the specification "nospecs" has no values, no further action is required.」→
「This level specset is now ready to use in SmarTest.」→ **在 Test Program Explorer 里保存 levels 文件**。

### 用法二：建一个带值的 spec set（用变量）

与用法一只差三处：

1. **先选 equation set 2**（`Select the Equation Set 2 specs.`），`Description` 里填的是
   **变量名 = 值**（`Vcc = 4.5V`），这条 spec 指向 spec set 1。
2. `done` 之后「You see the variable names for this spec set in the SpecTool Name column.」
3. **每个 spec 变量都要重复一遍**：「Repeat the procedure for all spec variables accordingly.」

收尾：点 Download 图标 → **查 Report window 有没有错** → 在 Test Program Explorer 里
右键 level 文件 → Save。

### 顺序上的两点（第二点是推断，照实标）

- **两条例子的收尾顺序都是「先 Download，后保存」**——**文档事实**（原文的步骤顺序如此）。
- **「必须先 Download 才能保存」这句明文规矩，本页的 sources 里没有**。
  **本页只知道两条例子的顺序如此，没有找到一句把它写成要求的话** → **（推断）**。

## 和谁有关

每条都说清**是什么关系**：

- [[level-setup-tool]] —— **入口（上游）**。Spec Tool 的第一条进入路径就是它的
  `Select > Edit Specifications`；而 spec set 是挂在 **equation set** 上的，
  equation set 又归 Level Setup tool 管。
- [[spec-set]] —— **它编辑的主要东西**。本页只讲 GUI 侧怎么建；
  「spec set 在文件里长什么样」（`SPECSET` 模块、编号范围）在那一页。
- [[level-file]] —— **产物落点**。本页的 Download 与「在 Test Program Explorer 里保存 levels 文件」
  说的就是这个文件。
- [[svlr]] —— **唯一被原文点名跨过来的东西**。原文：shmoo tool 里区分 local / global scope
  「must be expressed in the same way as for the SVLR command」，局部改写写成
  `<spec_variable>@<port_name>`。**Spec Tool 与运行期的 `SVLR` 必须同一种写法。**
- [[mapping-level]] —— **同阶段的对照表页**。它把「运行时改 spec 值并重算」那一行的 GUI 格
  填成本页的 Download、文件格填 [[level-file]] 的 `SPECS` / `SPECSET` 块、L1 格填 [[svlr]]、
  L2 格填 [[level-spec]]。**本页与它一致**，只有一处措辞差异见「出处」。
- [[level]] —— 本页 `stage: level` 的理由：spec 值是 level setup 的一部分。
- `The Spec Tool window`（raw: `02.08.04.30.01_The_Spec_Tool_window.md`）与
  `General Editing Features of the Spec Tool`（raw: `02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool.md`）
  —— **定义文档自己声明的两个子主题，也就是本页正文真正所在的地方**。
  §9.1 第 4 条说定义文档声明的子主题算「会存在的页」，但它们不在
  `extract/prose-allowlist.txt` 里，**故按规矩用反引号 + raw 路径，不写双方括号**。
  **本页没读这两篇**——所以 Spec Tool 的窗口布局、菜单全貌、
  除 spec 编辑以外的功能，本页一个字都没有。
- `Creating new specification sets` / `Global and local spec values - scope of the spec variable`
  （raw: `02.08.04.30.02.01_Creating_new_specification_sets.md` /
  `02.08.04.30.02.16.01_Global_and_local_spec_values__scope_of_the_spec_variable.md`）
  —— **本页「语法 / 参数」节那两段的来源**。本页只**描述这一节的结构**，
  **没有回去读它们本身**。

## 版本

定义文档 `02.08.04.30_Spec_Tool.md` 的 `## Functional changes` 段只有一条：

- **Introduced before SmarTest 6.3.2**

**⚠️ 这是 §11.2 ② 说的「哨兵值」，不是「6.3.2 新增了 Spec Tool」。** 它的意思是
**在本文档集覆盖范围开始之前就已经有了**（2,677 条可用性行用的是同一个版本号、同一个措辞）。
照字面读会生成一条格式齐整的假信息。参见 [[smartest-6.3.2]]。

**所以本页能说的只有一句**：**Spec Tool 在 7.10.3 上存在，且它的出现早于这套文档集覆盖的版本范围；
它具体哪个版本引入，语料没说。**

**本文档没有第二个条目，本页也没有从别处搬版本来。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.md`
（TDC `17358.htm`，**551 字节 / 18 行**）。

**这一篇的全部内容只有四样**：`## Subtopics` 两项、一句导语、`## Functional changes` 一条、frontmatter。
**本页「语法 / 参数」节那 3,587 字符不是来自它**——那一节的段名里写着来源是两篇子主题
（`.02.01_Creating_new_specification_sets`、`.02.16.01_Global_and_local_spec_values__scope_of_the_spec_variable`）。

**本页没做的**：

- **定义文档声明的两个子主题一篇都没读**：`02.08.04.30.01_The_Spec_Tool_window`（窗口长什么样）、
  `02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool`（它全部的编辑功能）。
  **所以本页只有「建 spec set」这一条线**：窗口布局、菜单全貌、search 测量、
  spec 值在 level 文件里怎么存——**一个字都没有**。
- **「语法 / 参数」节那两段的原文出处（`.02.01` / `.02.16.01`）没有回去读**。
  本页只**描述这一节的结构**（它摊平了、它是逐字抽的、它来自哪两篇），
  **没有引用这两篇之外的任何内容**。
- **没有读任何命令 / L2 文档**，所以 [[svlr]]、[[level-spec]] 那两侧的语法、参数、
  返回值本页一个字没有——**本页只写了原文那句「必须与 SVLR 同一种写法」**。
- **看了一张图**：`131014.png`（`F:\master-dev\dorm-wsl-sytest\tdc-html\raw\131014.png`，
  逐字内容见「是什么」那一节）。**这是本页唯一的图**——定义文档 `02.08.04.30_Spec_Tool.md`
  **自己一张图都没有**（实测 0 处 `raw/` 引用），**所以本页 `sources:` 里没有别的图可看**。
- **没有实跑**：没有开过 Spec Tool，没有建过 spec set，没有 Download 过。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/level.md`。

**与 [[mapping-level]] 的一处措辞差异，本页照实并列、不替它改（§10）**：
`mapping-level` 把「运行时改 spec 值并重算」那一行的 GUI 格写成
「`spec-tool` 的 Download（`File > Download`）」，**而本页读到的两处原文都说是图标、不是菜单路径**——
`Click Download(the Down arrow icon in the Spec Tool).` 与
`Click the Download icon (the down arrow in the SpecTool)`。
**本页判不了哪个对**：`mapping-level` 的 sources 里可能另有写 `File > Download` 的篇，
**本页没读那些篇**。**这是本页能查、但没查的一处，留给下一次。**

**⚠️ 本页读到的语料瑕疵，照原样记下、一处都没替它改（§11.2）**：

- **`Click Download(the Down arrow icon in the Spec Tool).`** —— `Download` 与 `(` 之间**缺一个空格**。
- **一句话里 `Note` 与其前的句子之间缺分隔**。原文（本页只摘出中间这一小段，**两端没有加省略号**）：
  `because "f" is global at PORT 4 and PORT 5.Note In the shmoo tool, the distinction`
  ——`5.` 与 `Note` 直接相连，**`Note` 本该另起一句**。
- **`This level specset is now ready to use in SmarTest.`** —— `specset` 连写；
  同一篇里其他地方写的是 `spec set`。
- **同一个东西三种写法**：`the Down arrow icon in the Spec Tool` / `the down arrow in the SpecTool` /
  `In the SpecTool, select Change > Create Specification.` —— `Spec Tool` 与 `SpecTool` 混用、
  `Down` 与 `down` 混用。
- **语法节里那段子主题段名 `Global and local spec values  scope of the spec variable` 中间丢了分隔符**：
  原始文件名是 `Global_and_local_spec_values__scope_of_the_spec_variable`，
  **双下划线正说明那里原本有一个字符被吃掉了**（本页不改它，照原样写）。
- **一段值得记下的语料组织方式**：那段 scope 原文的父节点写的是
  `How to set up a multiport timing specification`——**即 spec 的 global / local scope 机制
  在语料里的落点是 timing 的一节，不是 level 的一节**。这是语料自己的组织方式，本页照实记下。

**本页检查过、但本页没遇到的瑕疵**：本页 `sources:` 那篇里**一个汉字坏字都没有**
（实测 `[一-鿿]` 0 处，故 §11.2 ① 的 `碌` / `渭` / `卤` / `鈥` 一族在本页不存在）；
**§11.2 ⑤ 的整词替换本页也查过：0 处**（那一族的坏串形如 `DC/DC power units`，
**它是被替换坏的 `Index`，不是一个可用的名字，不许抄进任何代码**），故本页没有坏标识符可记。

`verified: doc-only`
