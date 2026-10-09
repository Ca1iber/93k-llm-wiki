---
type: object
title: Port Editor
layer: gui
stage: pin
tags: [pin, gui, port, pin-group, pin-configuration, naming-rule, fixed-group]
related: [pin-configuration-tool, pin-group-editor, pin, pin-configuration-file, pin-configuration-master-file, level-setup-tool, alias-set-editor, utility-purpose-editor, digital-pins-editor, dps-pins-editor, dc-scale-limits-editor, mapping-pin, smartest-6.3.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.03_Port_Editor.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Port Editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **243 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.03_Port_Editor.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The following picture shows a port Port_IO consisting of eight pins.

In the Available Pin List, the "鈭? character preceding with the pin name means that this pin has been added to Port_IO.

 !`Port Example`（raw: `../../../../agent-html/97848.png`）

<!-- 语法节 end -->

## 是什么

**Port Editor 是「给一个 port 挑成员」的编辑器。** 原文开门一句逐字：

> 「In this editor, you can select port members for a port.」

**port 是什么、为什么要它，本篇一个字没写**——本篇只有这一句、三条规则、一个例子。
**所以「它是什么」只能从三条规则反过来读**（推断，依据逐条标明）。

### 三条 port 定义规则

原文 `There are some rules for defining ports:` 加三条 bullet，逐字：

> 「- A port must not have the same name as a pin or pin group.」

> 「- Port definitions correspond to fixed group definitions. Expression-based port definitions are
> not supported.」

> 「- Ports are automatically pin groups. That is, ports in a setup can be used as an ordinary pin
> group. For example:」

**三条各管一件事：**

| # | 规则（原文要点） | 管什么 |
|---|---|---|
| 1 | port **不许**与 pin 或 pin group **重名** | **命名空间**：port / pin / pin group 共用一套名字 |
| 2 | port 定义**对应「固定组」定义**；**不支持**表达式型 port 定义 | **两类组里只许用第一类** |
| 3 | port **自动就是** pin group，可以**当普通 pin group 用** | **它不是新种类，是 pin group 的一个来源** |

**第 3 条底下还挂着两条 `for example`**（原文里是**缩进的子 bullet**）：

> 「  - In the level setup, the port names may be included in all lists from which you can select
> pin groups.」

> 「  - In the pin configuration, you can use ports (as pin groups) in expression based pin group
> definitions.」

**这两条合起来是一处值得注意的对照**：**规则 2 说「port 自己的定义不许用表达式」，
而第 3 条的第二个例子说「port 可以被拿去用在表达式型 pin group 的定义里」。**
——**约束在定义那一侧，不在使用那一侧。原文没有把这两句放在一起说。**

**（推断）所以 port 的定位是「固定组的另一个名字」。**
**依据是三条并列**：规则 2（`correspond to fixed group definitions`）+
规则 3 前半（`automatically pin groups`）+ 那两条 `for example`（进 level setup 的 pin group 列表、
进表达式型组定义）。**原文没有一句直接这么定义它，所以这是推断。**

### 界面长什么样（图证 · `97848.png`）

原文 `## Example` **只有一句加一张图**，正文对图的全部交待就是那一句
（`The following picture shows a port Port_IO consisting of eight pins.`）。
**逐格读出来**：

| 位置 | 图上内容 |
|---|---|
| 窗口标题 | **`Port_IO`** ——**port 的名字直接做窗口标题** |
| 左栏表头 | **`Available Pin List`**，两列：`Pin Name` / `Type` |
| 左栏四个按钮（上到下） | `Add >` / `Add All >>` / `< Remove` / `<< Remove All` |
| 右栏表头 | **`Port Members`**，同样两列：`Pin Name` / `Type` |
| 左栏第 1–8 行 | `CP`/`i`、`DS7`/`i`、`DS0`/`i`、`S1`/`i`、`S0`/`i`、`_MR`/`i`、`Q7`/`o`、`Q0`/`o` |
| 左栏第 9–12 行 | **行号格里各有一个勾选形状的记号**，针名依次是 `I/O7`/`io`、`I/O6`/`io`、`I/O5`/`io`、`I/O4`/`io` |
| 右栏第 1–8 行 | `I/O7`/`io`、`I/O6`/`io`、`I/O5`/`io`、`I/O4`/`io`、`I/O3`/`io`、`I/O2`/`io`、`I/O1`/`io`、`I/O0`/`io` |

**图上答掉了四件事（正文里一个字都没有）：**

1. **那个记号长什么样**：是一个**勾选形状**的标记，**位置在行号格里、即针名的前一格**——
   与原文那句 `preceding with the pin name`（在针名**之前**）对得上。
   **但「那个字的码位是什么」图答不了**：图只给字形，不给编码。
2. **界面是两栏搬移式**：左 `Available Pin List` → 右 `Port Members`，**四个按钮**
   （`Add >` 单个加、`Add All >>` 全加、`< Remove` 单个移回、`<< Remove All` 全移回）。
   **原文对这四个按钮一个字都没写。**
3. **`Type` 那一列是有值的**：图上出现 `i` / `o` / `io` 三种。
   **这一列原文一次都没提**——所以三种值什么意思，**本篇没有**（见 `## 出处`）。
4. **八根针的构成**：`I/O7` 到 `I/O0` **连续八个**——与例子那句 `consisting of eight pins` 对得上；
   左栏能看见的四个勾选记号，就是右栏八根里的前四个（左栏可滚动，另外四个在视图外）。

**哪些字算图证，逐个 `grep -F` 核过**：`Port_IO`（2 次）、`Available Pin List`（1 次）、
`eight pins`（1 次）**在本篇 raw 里搜得到，所以不算图证**；
而 `Port Members`、`Add >`、`Add All`、`Remove`、`Pin Name`、`Type`、`CP`、`DS7`、`DS0`、
`_MR`、`Q7`、`Q0`、`I/O7`、`I/O0` **在本篇 raw 里都是 0 次**——
**所以上表里只有后半串算图证**（§11.4 要的就是这条分界）。

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`、
没有 `## Subtopics`**（本页逐字查过，`Subtopics` 0 次）；`## Example` 只有一句加一张图，
**不是步骤**。**所以下面这条是从「图上四个按钮 + 三条规则」拼的（推断），不是文档给的步骤**：

1. **给 port 起名**——**不许与已有 pin 或 pin group 撞**（规则 1）。
2. **在左栏 `Available Pin List` 里挑针**，用 `Add >` 搬进右栏 `Port Members`
   （或 `Add All >>` 全搬）。
3. **搬错了**：`< Remove` 单个移回，`<< Remove All` 全移回。
4. **定义方式只能用固定组那一套**：`Expression-based port definitions are not supported.`（规则 2）。
5. **用**：这个 port 从此就是一个普通 pin group——**可以进 level setup 的 pin group 列表，
   也可以进表达式型 pin group 的定义里**（规则 3 的两条 `for example`）。

| 要做的 | 依据 |
|---|---|
| 挑成员 | 图上左栏 → 右栏的搬移，四个按钮 |
| 一次搬完 | `Add All >>` |
| 撤销 | `< Remove` / `<< Remove All` |
| 确认定义方式 | 规则 2：**表达式型不支持** |
| 确认能用在哪儿 | 规则 3 的两条 `for example` |

**要提醒的一条**：**规则 1 是三条里唯一带否定词的硬约束**，
而**原文没说撞名了会怎样**（报错？还是 GUI 里根本不让建）——**这一条链是断的。**

## 和谁有关

- [[pin-configuration-tool]] — **本编辑器是它的一个 element，而且那页已经写过一节**
  （标题 `### Port 不是 pin group 的别名，但行为上是`）。那页把本篇的三条规则逐字引了，
  并写出结论逐字：**「这一条把 [[port-editor]] 与 [[pin-group-editor]] 连起来了」**
  ——**指的是规则 3（`Ports are automatically pin groups.`）。**
  **⚠️ 这一条不是本页 raw 写的**（本页 raw 里 `Pin Configuration` 出现 0 次），
  **出自 wiki 的 [[pin-configuration-tool]] 页；本页没有回那篇原文核。**
- [[pin-group-editor]] — **关系就是规则 3**：**port 就是 pin group**，
  **所以 port 能出现的地方 pin group 也能出现**。**⚠️ 两篇 raw 互相都没提对方**
  （本页 raw 里没有 `pin group editor`）——**这层关系由 [[pin-configuration-tool]] 那页点出，
  本页没有回那两篇核。** 另：**两篇的 `## Example` 里用的是同一个坏字**
  （本篇 `the "鈭? character`，[[pin-group-editor]] 那篇两处也是 `鈭?`）——
  **同属一支的坏字，见 `## 出处` ①。**
- [[pin]] — **规则 1 把 port / pin / pin group 放进同一个命名空间**
  （`A port must not have the same name as a pin or pin group.`）。
  **所以这条规则同时是 pin 那一侧的约束**；**pin 自己的命名规矩在那页，本页没读。**
- [[level-setup-tool]] — **规则 3 的第一个 `for example` 点名 `the level setup`**：
  `the port names may be included in all lists from which you can select pin groups.`
  **本页只有这一句；level setup 里怎么用，本页没有。**
- [[pin-configuration-file]] / [[pin-configuration-master-file]] — **（推断）落盘侧**。
  本页是 GUI，**而本篇 raw 里没提任何文件**。
  **依据只是 [[pin-configuration-tool]] 那页把 pin 配置的文件侧分给了这两页；
  本页没有回那两篇核，也没有它们的任何事实。**
- [[mapping-pin]] — **（推断）三侧对照**。本页是 GUI 侧，[[mapping-pin]] 收的是
  「某个对象在 GUI / 文件 / L1 三侧各是谁」。**本篇 raw 里没有命令、没有文件，
  所以这条关系本页没有依据。**
- [[alias-set-editor]] / [[utility-purpose-editor]] / [[digital-pins-editor]] / [[dps-pins-editor]] /
  [[utility-pins-editor]] / [[dc-scale-limits-editor]] — **同 `stage: pin` 的同族 GUI 编辑器**,
  **同为 [[pin-configuration-tool]] 的 element**（**归属出自那页，不是本页 raw**）。
  **本页与它们的关系只在「同族」这一层**，本页 raw 一个都没提。
- `Port`（**未建、不在 allowlist，故用反引号**）— **本页 raw `## Related information`
  的第一个链接**（`02.08.04.18.01.03_Port.md`）。
  **它才是讲 port 这个概念的那一篇，而本页只讲编辑它的 GUI。**
- `Working with ports`（**未建**）— `## Related information` 的第二个链接
  （`02.08.04.18.02.09_Working_with_ports.md`），**从名字看是操作过程那一篇。**
- `Type` 列那三个值（`i` / `o` / `io`，**未建**）— **图上才有、原文没有，本页不给解释。**

## 版本

原文 `## Functional changes` **只有一条**，逐字：

- `Introduced before SmarTest 6.3.2`

**这一条是 §11.2 ② 那个哨兵值。** 它的意思是**「早于语料覆盖范围」**，
**不是「6.3.2 新增」**——**所以 Port Editor 本身成立于哪个版本，这份语料里没有。**

**与 wiki 目标版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（§11），
而这一篇**连一条 7.x 的条目都没有**——**所以本页只能确认「6.3.2 之前就有」；
7.10.3 时的界面与本页图 `97848.png` 是否一致，语料里没有依据。**

详见 [[smartest-6.3.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.03_Port_Editor.md`
（`97782.htm`，33 行）——**整篇读完**。

**本页做了什么**：

- **读了本页唯一那张图** `97848.png`（`## Example` 一节的全部内容），**逐格读过**。
  图答掉的四件事写进了「是什么」；**图里读到的字一律没有进 `>` 引文块**——
  引文块的含义是「这段能在 raw 文本里搜到」，**图上的字搜不到**（§11.4）。
- **为了核 port ↔ pin group 的关系，读了 wiki 的 `wiki/objects/pin-configuration-tool.md`**
  （**是 wiki 页，不是 raw**）。结论只写在「和谁有关」「版本」两处，
  **逐条标了「不是本页 raw 写的」。**
- **为了认那个坏字的族属，读了 `extract/encoding-map.csv`**（**既不是 raw 也不是 wiki 页**）。

**本页没做的**：

- **本页 raw 里没有参数表**（一个 `## Syntax` / `## Parameters` 都没有）。
  脚本只收了 `## Example` 一节（236 字符）——**所以「三条规则」那张表是我从散文里转述的，
  凡加 `>` 的地方才是逐字原文。**
- **`Port` 没读** —— **这是本页最大的空缺**：本页只讲「怎么往 port 里挑成员」，
  **「port 是什么、为什么要它」整个在那篇。**
- **`Working with ports` 没读** —— 所以完整的操作顺序（哪一步先、有没有前置）本页没有，
  **上面那条是我从图上的按钮拼的。**
- **[[pin-group-editor]] / [[pin-configuration-tool]] 两篇 raw 都没读** ——
  所以「port 与 pin group 到底差在哪」，本页只有本页 raw 里那三条规则。
- **四个按钮的行为原文没写，`Type` 那一列原文没写** —— 本页只能报图上的字形。
- **`02.06` 的命令原文一篇没读** —— **本页正文没有一条命令事实。**
- **没有实跑。** 没有在机台上开过这个编辑器、没有建过 port。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pin.md`。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**：
>
> **① 一个坏字，形态 `鈭?`**（第 23 行，`## Example` 一节）。逐字：
> `In the Available Pin List, the "鈭? character preceding with the pin name means that this pin has been added to Port_IO.`
> ——`extract/encoding-map.csv` 把它记成
> 「**原字符在 U+2200–U+223F 之间（第三字节已丢，只能给区间）**」，
> **属「反解不了」那一类**。**注意它和 `鈥`（U+9225）不是一族**：
> `鈥` 那一族有确定映射、可反解，**`鈭` 这个只能给区间**——**两族不许并成一类。**
> **本页引文照抄 `鈭?`，没有替它改成 `√`**——搜的时候要搜坏掉的那个形态（§11.2 ①）。
> **本页数过：本篇带非 ASCII 字节的行只有这一行。**
>
> **② `## Related information` 两个链接粘在一起**，逐字：
> `[Port](<02.08.04.18.01.03_Port.md>)[Working with ports](<02.08.04.18.02.09_Working_with_ports.md>)`
> ——**两个链接之间没有任何分隔符**（与 [[dscp]]、[[dc-scale-limits-editor]] 同位置的毛病同类）。
>
> **③ 第三条规则是「一条 bullet 套两条 bullet」，句末用冒号。** 逐字：
> `- Ports are automatically pin groups. That is, ports in a setup can be used as an ordinary pin group. For example:`
> ——**它自己是一条 bullet，`For example:` 底下那两条在原文里是缩进的子 bullet。**
> **本页引文保留原文的缩进。**
>
> **④ `## Example` 里那张图，正文给它的话只有一句。** alt 文字是 `Port Example`，
> 正文全部交待就是 `The following picture shows a port Port_IO consisting of eight pins.`
> ——**四个按钮、`Type` 列、两个表头名（`Available Pin List` / `Port Members`）的差别，
> 正文一个字都没有。**
>
> **⑤ 正文写 `preceding with the pin name`，不是 `preceding the pin name`。**
> 逐字核过：本篇 `preceding with` 出现 1 次。
> **本页照抄，不替它改成 `preceding the`。**
>
> **⑥ 图与正文唯一对得上的地方是「记号的位置」。** 正文说它在 `the pin name` **之前**，
> 图上记号确实在针名的前一格；**但正文把它叫 `character`（一个字符），
> 而图上是一个勾选字形**——**那个字的码位是什么，正文没说、图也不给，本页不猜。**
> （同族的 [[pin-group-editor]] 那页在同一位置也记了同一个坏字，
> **那一页只写到「√ 形状」、同样没有定码位**。）
>
> **⑦ §11.2 ① 那一族（`鈥`）本篇没有；§11.2 ⑤ 那个整词替换（`DC/DC power units`）本篇 0 命中**
> （本页逐字查过）——**本篇的坏字只有 ① 那一处。**
>
> **⑧ 本篇没有 `## Application` 段**（[[dscp]] / [[uptd]] 两篇都有）——
> **所以本页 `layer: gui` / `stage: pin` 这两个归属是照 wiki 的既有划分填的，
> 不是本篇文档写出来的。**

`verified: doc-only`
