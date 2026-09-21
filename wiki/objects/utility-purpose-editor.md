---
type: object
title: Utility Purpose Editor
layer: gui
stage: pin
tags: [pin, gui, utility-purpose, utility-line, settling-time, multi-site, site-state, pin-configuration]
related: [utility-pins-editor, utility-line-view, utility-lines, utility-line-assignments, utility-card, utility-pogo-block-utility-card-v93000-exa-scale-systems, pin-configuration-tool, pin-configuration-file, port-editor, alias-set-editor, digital-pins-editor, dps-pins-editor, dc-scale-limits-editor, smartest-6.3.2, smartest-7.1.3, smartest-7.2.0, smartest-7.10.1]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.05_Utility_Purpose_Editor.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Utility Purpose Editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Utility Purpose Editor 是「给一个 utility purpose 挑 utility line」的编辑器。**
原文开门一句就是全部机制：

> 「In this editor, you select utility lines for a utility purpose.」

**注意这句划的范围**：它只承诺「**挑 line**」。
**purpose 是什么、为什么要把几条 line 归成一个 purpose、运行期谁去用它，本篇一个字没写**——
本篇只有这一句、一段名的规矩、一段记号的说明、两段区域说明、一个时间框、两句 `Note`（见 `## 出处`）。

### 四个部件（原文逐段，加图证）

| 部件 | 原文（逐字，凡加 `>` 的见下） | 图上（`354759.png`） |
|---|---|---|
| **编辑器标题** | `The editor title is the name of the utility purpose.` | 标题栏就是 **`UP1`** |
| **`Utility Lines` 区** | 可选 line 的列表；**加进来的那一条前面有一个记号** | 左栏，一列 `Channel`，行 `16501` 起逐行往下排 |
| **`Utility Members` 区** | `shows the selected utility lines with the setting states of each site: 1, 0, or X (Do not care).` | 右栏，`Channel` + `State`（**下面拆成 `Site 1`–`Site 4` 四个子列**） |
| **`Settling Time` 文本框** | `shows wait time after the write action of the utility purpose` | 左下角一行：`Settling Time` + `0.000` + `[ms]` |

### 名字的规矩：≤16 个字母数字，且有一串禁用字符

原文逐字：

> 「The editor title is the name of the utility purpose. It can have up to 16 alphanumeric
> characters. It must not contain spaces, or any of the following characters:」

**跟着的就是那一串禁用字符**，原文逐字（**注意行首那个空格**）：

```
 # ; ('' ) ? @ ,
```

**三条要点**：

- **上限是 16 个字母数字字符**——**与 [[utility-pins-editor]] 那篇给 pin 名的上限是同一个数**
  （那页逐字写 `The pin name can have up to 16 alphanumeric characters.`，
  **那一条引自本 wiki 的另一页，不是本篇 raw**）。
- **查的是「不能含空格」+ 一串具名禁用字符**——**具体是什么字符，原文明写的就是上面那一行**
  （⚠️ **那一行的形态有问题，见 `## 出处` ②**）。
- **本篇没说撞名会怎样**（名字与该编辑器里已有的 purpose 重了、或与别处的东西重了）——
  **这一条链是断的。**

### `Utility Members` 区里的「site 状态」

原文逐字（**这一句同时是这一节唯一的定义**）：

> 「The Utility Members area shows the selected utility lines with the setting states of each site:
> 1, 0, or X (Do not care).」

**三个取值**：`1` / `0` / **`X (Do not care)`** ——**`X` 是「不管」**，这是原文给的唯一解释。

⚠️ **图上出现的是四个 site、只有 `0` 和 `1`，没有 `X`**（见下「图证」）；
**而且图上有跨 site 不一致的值，与 `Settling Time` 那段末句打架**（见 `## 出处` ⑤）。

### `Settling Time`：范围 + 一条多 site 硬约束

原文逐字三句：

> 「The Settling Time text box shows wait time after the write action of the utility purpose, such
> as the settling time of the user relays controlled by the defined utility purpose. The range is
> 0 ... 2147483.646. ms. For multi-site testing, you must set the same value for all sites.」

**三件事：**

| # | 内容 | 原文 |
|---|---|---|
| 1 | **它是什么**：utility purpose **write 动作之后的等待时间** | `wait time after the write action of the utility purpose` |
| 2 | **典型用途**：被这个 purpose 控制的**用户继电器**的稳定时间 | `such as the settling time of the user relays controlled by the defined utility purpose` |
| 3 | **范围**：`0 ... 2147483.646. ms` | `The range is 0 ... 2147483.646. ms.` |

**外加一条硬约束**：`For multi-site testing, you must set the same value for all sites.`
——**多 site 测试时，所有 site 必须用同一个值。**

**（推断）所以 `Settling Time` 是「一个 purpose 一个值」，不是「一个 site 一个值」**——
**依据是那句 `you must set the same value for all sites`**；
**原文没有说这个框长得像不像「按 site 分开填」，也没有说填了不一样会怎样。**

**单位**：原文写 `ms`，图上写 `[ms]`（**方括号是图上才有的**）。

### 两句 `Note`（原文**粘在同一行里**）

原文第 24 行逐字（**两个 `Note` 之间没有分隔符**）：

> 「Note Even if a certain utility line was already defined individually, a utility purpose can
> consist of the utility line.Note You can define the same utility line for different utility
> purposes by overlapping.」

**两句各说一件事：**

| # | 原文 | 意思 |
|---|---|---|
| 1 | `Even if a certain utility line was already defined individually, a utility purpose can consist of the utility line.` | **一条 line 已经被单独定义过，也不妨碍把它放进 purpose** ——**不互斥** |
| 2 | `You can define the same utility line for different utility purposes by overlapping.` | **同一条 line 可以同时属于多个 purpose**（`by overlapping`）——**是多对多** |

**这两句合起来把「归属」讲清了**：**line 与 purpose 之间不是独占关系，两个方向都可以复用。**
⚠️ **但两个 `Note` 被粘成了一行（`utility line.Note You can`），见 `## 出处` ③。**

### 界面长什么样（图证 · `354759.png`）

原文 `## Example` 一节没有单独标题，**图直接夹在正文里**：
`The following figure displays the configuration settings of utility purpose UP1. UP1 has three
members: 16501, 16502, and 16508.` ——**逐格读出来**：

| 位置 | 图上内容 |
|---|---|
| 窗口标题 | **`UP1`**（**这一张的标题栏没有 `*`**） |
| 左栏表头 | **`Utility Lines`**，一列 **`Channel`**（前面是行号列） |
| 左栏第 1–30 行 | `16501`、`16502`、`16503`、…、`16530`（**逐个连续递增**，滚动条显示还有更多） |
| 左栏记号 | **只有第 1、2、8 行的行号格里有一个勾选形状的记号**——对应的 Channel 正是 **`16501` / `16502` / `16508`**，**与正文那句 `UP1 has three members` 逐个对得上** |
| 左栏四个按钮（上到下） | `Add >` / `Add All >>` / `< Remove` / `<< Remove All` |
| 右栏表头 | **`Utility Members`**：行号、**`Channel`**、**`State`**（**`State` 是一个跨列的表头，底下一行是 `Site 1` / `Site 2` / `Site 3` / `Site 4` 四个子列**） |
| 右栏第 1 行 | `16501` / `0` / `1` / `0` / `1` |
| 右栏第 2 行 | `16502` / `0` / `0` / `0` / `0` |
| 右栏第 3 行 | `16508` / `1` / `1` / `1` / `1` |
| 左下角 | `Settling Time` + 文本框 **`0.000`** + 单位标签 **`[ms]`** |

**图上答掉的四件事（正文里都没有）：**

1. **两个区域的两栏搬移式界面**，四个按钮（`Add >` 单个加、`Add All >>` 全加、
   `< Remove` 单个移回、`<< Remove All` 全移回）。**正文对这四个按钮一个字都没写。**
2. **`State` 是按 site 拆列的**，图上是 **4 个 site**。
   **正文只说 `the setting states of each site`，没有说「按 site 拆成并排的子列」。**
3. **一个 purpose 里选了几条 line 就显示几行**（图上是 3 行 = 正文那三个成员）。
4. **左栏列到 `16530` 还没到底**——**所以可选 line 是一个很长的连续清单**；
   **那个编号是什么段、范围到哪，正文一个字没写**（见 `## 出处`）。

**哪些字算图证，逐个 `grep -F` 核过**：`UP1`（1 次）、`16501`（1 次）、`16502`（1 次）、
`16508`（1 次）、`Utility Lines`（1 次）、`Utility Members`（2 次）、`Settling Time`（1 次）、
`Do not care`（1 次）**在本篇 raw 里都搜得到，所以不算图证**；
而 **`Channel`（0 次）、`Site`（0 次）、`State`（0 次）、
`Add >`（0 次）、`Add All`（0 次）、`Remove`（0 次）、`0.000`（0 次）、`[ms]`（0 次）、
`16503`（0 次）、`16530`（0 次）**——**才**算图证（§11.4 要的就是这条分界）。

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`、
没有 `## Subtopics`**（本页逐字查过，`Subtopics` 0 次）；**也没有 `## Example` 段标题**
（图是夹在正文里的）。**所以下面这条是从「四个部件的说明 + 图上的按钮」拼的（推断）**：

1. **给 purpose 起名**（= 编辑器标题）：≤16 个字母数字字符，**不含空格与那串禁用字符**。
2. **在左栏 `Utility Lines` 里挑 line**，用 `Add >` 搬进右栏 `Utility Members`
   （或 `Add All >>` 全搬）。
3. **搬错了**：`< Remove` 单个移回，`<< Remove All` 全移回。
   ——**第 2、3 步的按钮名出自图，正文没写。**
4. **在右栏给每个 site 填 state**：`1` / `0` / `X (Do not care)`。
5. **填 `Settling Time`**：范围 `0 ... 2147483.646. ms`；
   **多 site 时所有 site 用同一个值**。
6. **收尾**：**本篇没有说要不要 apply / save**——**这是本页与
   [[alias-set-editor]]（明写 `apply the data and save the pin configuration file`）
   和 [[port-editor]] 的一处差别**（见 `## 出处`）。

**从原文和图能落成的动作：**

| 要做的 | 依据 |
|---|---|
| 把一条 line 加进 purpose | 图上左栏 → 右栏的搬移；**正文只说「已经加进来的会有一个记号」** |
| 一次加完 | `Add All >>`（**图证**） |
| 撤销 | `< Remove` / `<< Remove All`（**图证**） |
| 一个 site 单独不管 | state 填 `X`（`X (Do not care)`，原文） |
| 多 site 一致 | `For multi-site testing, you must set the same value for all sites.` |
| 让 relay 有时间稳定 | 用 `Settling Time`——原文给的就是这个例子 |
| 一条 line 给两个 purpose | **可以**：`You can define the same utility line for different utility purposes by overlapping.` |
| 一条 line 已单独定义过还想归进 purpose | **可以**：第一句 `Note` |

## 和谁有关

- [[utility-pins-editor]] — **⚠️ 这是本页要划清的一条界线：两个编辑器不是同一个东西。**
  **本篇 raw 里 `Utility Pins` 出现 0 次**，两篇互不引用。
  按两篇各自的原文，分工是：
  - **[[utility-pins-editor]]**：`Utility pin names are assigned to utility pogo pins` ——
    **给 utility pogo pin 分名字**，五列 `Name` / `Mode` / `t[ms]` / `Comment` / `Tester Channel`。
  - **本页**：`you select utility lines for a utility purpose` ——
    **把 utility line 归成 purpose**，界面上是 `Utility Lines` / `Utility Members` / `Settling Time`。
  **（两条引文里，本页的出自本页 raw；另一条出自 wiki 的 [[utility-pins-editor]] 页，
  本页没有回那篇 raw 核。）**
  **两页的 `related` 互指，是 wiki 的既有写法，不是任何一篇 raw 写的。**
- [[utility-line-view]] / [[utility-lines]] / [[utility-line-assignments]] —
  **（推断）utility line 的「对象侧」**：本页是「把 line 归成 purpose」的 GUI，
  那三页从名字看是 line 本身的清单 / 视图 / 分配。**本篇 raw 一个都没提**，
  **所以这三条关系本页没有依据。**
- [[utility-card]] / [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] —
  **（推断）硬件侧**。本页 `## 版本` 最后一条逐字提到
  `Three-digit utility pogo block designator on V93000 EXA Scale systems.`
  ——**`utility pogo block` 这个词出现在本篇里，但本篇没有解释它是什么、在哪配。**
  那两页从名字看是它的对象页与卡页，**本页都没读。**
- [[pin-configuration-tool]] — **本编辑器是它的一个 element**。
  那页的元素表里有 utility purpose 编辑器，**而且那页记的父文档 `Functional changes`
  里有一条 `SmarTest 7.1.3: Move utility purpose editor to Pin Settings.`**
  ——**这一条在本篇 raw 的 `## 版本` 里没有**（本篇 7.1.3 的两条是另两件事，见 `## 版本`）。
  **⚠️ 这一条不是本页 raw 写的**（本页 raw 里 `Pin Configuration` 出现 0 次），
  **出自 wiki 的 [[pin-configuration-tool]] 页；本页没有回那篇原文核。**
- [[pin-configuration-file]] — **（推断）落盘侧**。本页是 GUI，
  **而本篇 raw 里没提任何文件**——**注意这不是小差别**：
  同族的 [[alias-set-editor]] 那篇明写 `save the pin configuration file`，
  **本篇连「要不要保存」都没说。** **依据只是「同族的另一篇有这一步」；
  本页没有那篇 raw 的原文核。**
- [[port-editor]] / [[alias-set-editor]] / [[digital-pins-editor]] / [[dps-pins-editor]] /
  [[dc-scale-limits-editor]] — **同 `stage: pin` 的同族 GUI 编辑器**。
  **本页与它们的关系只在「同族」这一层**，**本篇 raw 一个都没提。**
  形态上有一个共同点：**本页与 [[port-editor]] 的界面是同一个两栏搬移式**
  （左「还没选的」→ 右「已选的」，四个按钮位置都一样）——
  **这是本页从两张图上读出来的对比，两篇 raw 都没有写。**
- [[mapping-pin]] — **（推断）三侧对照**。本页是 GUI 侧，[[mapping-pin]] 收的是
  「某个对象在 GUI / 文件 / L1 三侧各是谁」。**本篇 raw 里没有命令、没有文件，
  所以这条关系本页没有依据。**
- `Utility purpose`（**未建**）— **本页 raw `## Related information` 的第一个链接**
  （`02.08.04.18.01.05_Utility_purpose.md`）。**它才是讲 purpose 这个概念的那一篇，
  而本页只讲编辑它的 GUI。**
- `Working with utility purposes`（**未建**）— 第二个链接
  （`02.08.04.18.02.10_Working_with_utility_purposes.md`），**从名字看是操作过程那一篇。**
- `Utility Purpose view`（**未建、且不在 allowlist，故用反引号**）—
  第三个链接（`../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.06_Utility_Purpose_view.md`），
  **也是 `## 版本` 第 4 条那句 `SmarTest 7.2.0: Utility Purpose view introduced` 的所指。**
- `Pin Settings`（**未建**）— **（推断）本编辑器 7.1.3 之后被搬去的地方**，
  **依据只是 [[pin-configuration-tool]] 那页记的那条 `Move utility purpose editor to Pin Settings.`；
  本页 raw 里 `Pin Settings` 出现 0 次。**

## 版本

原文 `## Functional changes` **五条**，条目逐字：

- `Introduced before SmarTest 6.3.2`
- **SmarTest 7.1.3**：`The site information is moved to the Utility Members area.`
- **SmarTest 7.1.3**：`The state buttons are removed.`
- **SmarTest 7.2.0**：`Utility Purpose view introduced`
- **SmarTest 7.10.1**：`Three-digit utility pogo block designator on V93000 EXA Scale systems.`

**第一条是 §11.2 ② 那个哨兵值**（`Introduced before SmarTest 6.3.2` =
「早于语料覆盖范围」），**不是「6.3.2 新增」**——
**所以这个编辑器本身成立于哪个版本，这份语料里没有。**

**后四条是四条真事实，三条要读：**

1. **7.1.3 有两条，都是「减法 / 搬移」**：**site 信息搬进 `Utility Members` 区**、
   **state 按钮被拿掉**。**这两条正好解释了现在的界面为什么是这个形状**——
   图上 `State` 是**并排的子列**（不是按钮），而且它在 **`Utility Members` 区里**
   （左上 `Utility Lines` 区没有 site 概念）。
   **（推断）所以图上这张快照是 7.1.3 之后的**——**依据是那两条改动与图上形态吻合**
   （并排子列 = 搬进该区；没有按钮 = 按钮已拿掉）；**原文没有说这张图是哪个版本截的。**
   ⚠️ **但那张图与 `Settling Time` 末句的矛盾还在**（见 `## 出处` ⑤），
   **本页不拿版本去解释那个矛盾。**
2. **7.2.0 那条讲的是另一个东西**：`Utility Purpose view introduced`
   ——**它说的是一个 **view**，不是本编辑器**，而 `Related information` 里也链了这个 view。
   **本页没有那个 view 的页，所以那是什么本页不知道。**
3. **7.10.1 那条把编号改成三位**：`Three-digit utility pogo block designator on V93000 EXA
   Scale systems.` ——**（推断）这与图上那个五位 Channel 编号（`16501`）的读法有关**
   （前几位是 block、后两位是 line），**依据只是这句里的 `utility pogo block designator`
   与图上 `Channel` 那一列的名字对得上**；**本篇没有解释 `Channel` 编号怎么读，
   所以这是推断，不是原文明写的。**

**（推断）7.1.3 还有一条不在本篇的 `Functional changes` 里**：
[[pin-configuration-tool]] 那页记的父文档条目逐字是
`SmarTest 7.1.3: Move utility purpose editor to Pin Settings.`
——**这一条讲的是「这个编辑器被搬到哪儿」，本篇一个字没有。**
**依据是两边同一个版本号；本页没有回那篇原文核，所以这是推断。**

**与 wiki 目标版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（§11），
而这一篇**最后一条是 7.10.1**——**所以 7.10.1 到 7.10.3 之间有没有再改，语料里没有依据。**

详见 [[smartest-6.3.2]] / [[smartest-7.1.3]] / [[smartest-7.2.0]] / [[smartest-7.10.1]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.05_Utility_Purpose_Editor.md`
（`17603.htm`，36 行）——**整篇读完**。

**本页做了什么**：

- **读了本页唯一那张图** `354759.png`（夹在正文里的那张配置截图），**逐格读过**。
  图答掉的四件事写进了「是什么」；**图里读到的字一律没有进 `>` 引文块**——
  引文块的含义是「这段能在 raw 文本里搜到」，**图上的字搜不到**（§11.4）。
- **为了核「本编辑器归谁管、7.1.3 那条在哪」两句，读了 wiki 的
  `wiki/objects/pin-configuration-tool.md`；为了核「它和 utility-pins-editor 的界线」，
  读了 wiki 的 `wiki/objects/utility-pins-editor.md`**（**两篇都是 wiki 页，不是 raw**）。
  结论只写在「和谁有关」「版本」两处，**每条都标了「不是本页 raw 写的」。**

**本页没做的**：

- **本页 raw 里没有参数表**，也没有 `## Syntax` / `## Parameters` / `## Example` 段
  （本页逐字查过）——**所以「语法 / 参数」节是空的**；
  **本页没有一格是从脚本抽的逐字表来的**，凡加 `>` 的地方才是逐字原文。
- **`Utility purpose` 没读** —— **这是本页最大的空缺**：本页只讲「怎么往 purpose 里挑 line」，
  **「purpose 是什么、为什么要把几条 line 归成一个 purpose」整个在那篇。**
- **`Working with utility purposes` 没读** —— 所以
  **「改完要不要 apply / save」本页没有答案**（本篇正文一个字没提）。
- **`Utility Purpose view` 没读**（本 wiki 也没有它的页）——
  `## 版本` 第 4 条与 `Related information` 第三条都指向它，**那是什么本页不知道。**
- **`16501` 这类编号怎么读，本篇没写** —— 图上左栏一直排到 `16530` 以上，
  **本页只报「是一串连续递增的号」，不报它的构成、也不报范围。**
- **`X (Do not care)` 在界面上怎么填，本篇没写** —— 图上三个成员一个 `X` 都没有，
  **所以本页连「它是打一个字母还是选一个项」都不知道。**
- **四个按钮、`Site 1`–`Site 4` 这四个子列名，都是图证**，正文没有；
  **而图上那几个 site 到底是几个 site、和实际测试 site 数什么关系，本篇没有。**
- **`02.06` 的命令原文一篇没读** —— **本页正文没有一条命令事实。**
- **没有实跑。** 没有在机台上开过这个编辑器、没有给 relay 量过 settling time。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pin.md`。

> ⚠️ **本篇的语料瑕疵与对不上的地方，照实记、一处都没替它改**：
>
> **① 一个坏字，形态 `鈭?`**（第 18 行），**与 [[port-editor]] 那篇是同一个形态**。
> 逐字：`In the Utility Lines area, the "鈭? symbol preceding with the utility line means that this utility line has been added to the current utility purpose.`
> ——**`鈭` 属 `extract/encoding-map.csv` 里「原字符在 U+2200–U+223F 之间、
> 第三字节已丢、反解不了」那一类**，**与可反解的 `鈥`（U+9225）那一族不是一族。**
> **本页引文照抄 `鈭?`，没有替它改成 `√`**——搜的时候要搜坏掉的那个形态（§11.2 ①）。
> **本页数过：本篇带非 ASCII 字节的行只有这一行（第 18 行）。**
> **⚠️ 同一处与 [[port-editor]] 那篇有一处用词差别**：那篇写的是 `character`，
> **本篇写的是 `symbol`**；**两句其余部分逐字相同**（`the "鈭? _ preceding with the pin/utilty line`）。
> **原文没有统一，本页照实并列。**
>
> **② 禁用字符清单那一行是坏的。** 原文逐字（**注意行首那个空格**）：
> ```
>  # ; ('' ) ? @ ,
> ```
> ——**`('' )` 这一段读不通**：两个单引号紧贴、后面跟一个空格，再一个右括号。
> 按上下文（这一行是「不允许的字符」）**原意应是双引号和单引号**（即 `" '`），
> **语料把它渲染成了 `('' )`**。
> **同一份清单在语料里已经见到两种坏法**：[[dps-pins-editor]] 那页记的它那篇是
> `# ; ( ' ' ) ? @ ,`（**引号两侧都有空格**），
> [[utility-pins-editor]] 那页记的它那篇是 `# ; (鈥? ) ? @ ,`（**用了 `鈥` 那个坏字**）——
> **这一条来自本 wiki 的那两页，不是本篇 raw。**
> **本页照抄 `('' )`，一个字符都不替它改。**
>
> **③ 两句 `Note` 被粘成一行，中间没有分隔符。** 逐字（**注意 `line.Note` 那个位置**）：
> `Note Even if a certain utility line was already defined individually, a utility purpose can consist of the utility line.Note You can define the same utility line for different utility purposes by overlapping.`
> ——**第二个 `Note` 紧跟在第一个 Note 的句号后面，两者之间的分隔符就是一个 `.`**。
> **本页照抄，不替它断行、不替它加分隔符。**
> （**`Note` 后面同样没有冒号或破折号**——这与 [[dscp]] / [[uptd]] 两篇的 `Note` 是同类毛病。）
>
> **④ `Settling Time` 的范围写法多了一个句号。** 逐字：
> `The range is 0 ... 2147483.646. ms.`
> ——**`2147483.646` 后面又跟了一个 `.`，然后才是 ` ms.`**，
> **所以这一句里有三个句点连着出现（`646. ms.`）**。
> **上界是 `2147483.646`（毫秒）还是别的，原文这个写法本身没有排除歧义；
> 本页照抄，不替它删那个点。**
> **⚠️ 另外 `0 ... 2147483.646` 这个上界与 float 的精度有关**（`2147483647` 是 32 位有符号整数的上界，
> 把它按毫秒、小数点后三位读就是这个数）——**这是我的推断，原文一个字没解释。**
>
> **⑤ 图上的多 site 取值与正文那句硬约束打架。** 正文逐字：
> `For multi-site testing, you must set the same value for all sites.`
> **而图 `354759.png` 右栏第 1 行 `16501` 逐格读出来是 `0` / `1` / `0` / `1`**
> ——**四个 site 的值不一样，而且是交替的**（第 2 行 `16502` 是 `0 0 0 0`、
> 第 3 行 `16508` 是 `1 1 1 1`，这两行是一致的）。
> **图与它自己这篇文档的正文，在「多 site 能不能填不一样」这件事上对不上。**
> **原文没有解释**，也没说那张图是哪个版本截的；
> **本页两处并列，不替它判定哪一处是对的。**
>
> **⑥ `Settling Time` 的单位在正文与图上写法不同。** 正文写 `ms`，
> 图上的单位标签是 `[ms]`（**方括号只有图上有**）。**本页照实并列。**
>
> **⑦ `## Related information` 三个链接全部粘在一起。** 逐字（开头）：
> `[Utility purpose](<…>)[Working with utility purposes](<…>)[Utility Purpose view](<…>)`
> ——**一个挨一个，没有空格、没有逗号、没有换行**
> （与 [[dscp]] / [[dc-scale-limits-editor]] / [[port-editor]] 同位置的毛病同类）。
>
> **⑧ 本篇没有 `## Example` 段标题，图是夹在正文里的。** 原文的图直接跟在
> `The following figure displays the configuration settings of utility purpose UP1. UP1 has three
> members: 16501, 16502, and 16508.` 这两句后面，
> **它上面最近的段标记是 `# Utility Purpose Editor`（一级标题）**——
> **所以本页的「语法 / 参数」节收不到任何段**（脚本的判据是段标记）。
> **图里的内容（按钮、`Site` 子列、`Channel` 列名）因此只留在本页的散文里。**
>
> **⑨ 本篇没有 `## Application` 段**（[[dscp]] / [[uptd]] 两篇都有）——
> **所以本页 `layer: gui` / `stage: pin` 这两个归属是照 wiki 的既有划分填的，
> 不是本篇文档写出来的。**
>
> **⑩ §11.2 ① 那一族（`鈥`）本篇没有；§11.2 ⑤ 那个整词替换（`DC/DC power units`）本篇 0 命中**
> （本页逐字查过）——**本篇的坏字只有 ① 那一处，禁用清单那一行是 ② 那种坏法。**

`verified: doc-only`
