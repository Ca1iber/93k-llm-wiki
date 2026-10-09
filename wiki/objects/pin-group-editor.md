---
type: object
title: Pin group editor
layer: gui
stage: pin
tags: [pin, gui, pin-configuration, pin-group, fixed-group, expression-based-group, group-arithmetic, dfgp]
related: [pin, pin-configuration-tool, pin-configuration-file, mapping-pin, dfgp, dfpn, dfps, conf, digital-pins-editor, dps-pins-editor, utility-pins-editor, command-reference]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02_Pin_group_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.01_Rules_for_defining_groups.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.02_Incompatible_pin_groups.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Pin group editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **70 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02_Pin_group_editor.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| D | Digital fixed groups |
|---|---|
| E | Expression-based groups |

<!-- 语法节 end -->

## 是什么

**Pin group editor 是「挑组成员」的 GUI。** 原文开门两句就把它的范围和骨干一次说清：

> 「In this editor, you can select group members for a group.」

> 「There are two types of groups which differ in the way they are set up:」

后一句底下就列着那两条：`Fixed groups` 与 `Expression-based groups`。
**这个二分是本页的骨干**——下面每一节都挂在它上面，
连两张图都正好各拍一边（见「界面」）。

### 第一类：Fixed groups

> 「These are basic groups which only consist of digital pins and pin aliases as group members.」

成员只有两种：**digital pin** 与 **pin alias**。没有别的组，也没有集合运算。

### 第二类：Expression-based groups

> 「These are groups which consist of digital pins, pin aliases, and/or other groups (digital fixed or expression-based) and support group arithmetic. Expression-based groups are defined by so-called group expressions, like, for example,」

紧接着是原文给的表达式例子（代码块，逐字）：

```
(group1 + pin1 + pin4 + group3) * group2
```

> 「The evaluation of the group expression results in the actual pins contained in the group.」

**「成员里可以有别的组」加「要求值」这两条，就是它与固定组的全部实质差别**：
表达式里写的是组名，**组里最终装的是求值之后那些 pin**。

支持的运算，原文逐字（`A, B, C and D` 是组、`a, b and c` 是 pin）：

> 「The following group operations are supported (A, B, C and D are groups, a, b and c are pins)」

- `UNION (+)`: `A = (a + b + a) => A= {a,b}`
- `DIFFERENCE (-)`: `B = A - a => B = {b}`
- `INTERSECTION (*)`: `C = A * B => C = {b}`
- `Nested expressions`: `D = ((A - b) + (C + c)) => D = {a, b, c}`

⚠️ 第一条里 `A=` 与 `{a,b}` 之间**没有空格**（同一条前面的 `A = (a + b + a)` 两侧却有）——
**原文如此，本页照抄**。

### `Component Type`：一个下拉决定「谁是活的」

> 「The Component Type list determines the type (I, O , IO and DC) of active pins in the group.」

⚠️ **引文里 `O` 与逗号之间那个空格是原文如此**（`(I, O , IO and DC)`）——
同一篇别处写的是 `(I, O and IO)`，**没有多这个空格**。**本页照抄，不替它改。**

四种取值各自的行为（原文是一张两列表，md 压平后仍能看出格界；
**本表是从原文那些句子转述的，不是逐字**，逐字的引文只给下面两组，其余同型换词）：

| `Component Type` | 进 `Group Members` 的 | 作为**非活跃**成员进去的 |
|---|---|---|
| `I` | 求值后表达式的**全部 input 与 IO pin** | output 与 DC pin，作为非活跃的 **input** pin |
| `O` | 全部 output 与 IO pin | input 与 DC pin，作为非活跃的 **output** pin |
| `IO` | 全部 input、output 与 IO pin | DC pin，作为非活跃的 **IO** pin |
| `DC` | 全部 DC pin | input、output 与 IO pin，作为非活跃的 **DC** pin |

逐字原文（以 `I` 那一格为例，两句话都在同一格里）：

> 「All input and IO pins of the evaluated expression are inserted into the Group Members area.」

> 「Output and DC pins are inserted as inactive input pins.」

（`O` / `IO` / `DC` 三格是同型句子换词——`All output and IO pins of the evaluated expression are inserted into the Group Members area.` 这一型；
**本页不替它们逐条铺开，也不拿它们当引文**。）

**为什么会有「非活跃成员」这种设计，原文用一条 `Note` 交代**（这一句在 raw 里是表格的一格，
行首带 `   | `，本页引的是格内容）：

> 「Note Pins that are not of the component type selected for a group A are included as inactive members, because they have to be in the group A to be activated, if another group B uses group A in its definition, and the component type of group B is different of that of group A.」

### 两个列表，名字不一样

原文对两个列表分别说了话，**名字是不同的**：

- 固定组那一边：`Available Pin List`（正文与 `97841.png` 的表头一致）；
- 表达式型那一边：`In the Available Group/Pin List:`。

**这个差别正好对应两类组**——固定组只列 pin，表达式型组要连组一起列。
**这一条不是图证**：两个名字在本篇 raw 里各出现 1 次，正文自己就把它们分给了两节
（`Available Pin List` 在第 24 行的 Fixed groups 一节，`Available Group/Pin List:` 在第 96 行），
**两张图的表头只是与正文对得上**（见「界面」）。

### 那个记号：原文这里是坏字

> 「In the Available Pin List, the "鈭? character preceding with the pin name means that this pin has been added to mode.」

> 「- The "鈭? character marks the pin added to the group.」

**`鈭?` 是坏字，本篇两处都是它。** 口径：**129 行里带非 ASCII 字节的只有这两行，各 3 字节**
（逐行数过）——**本篇的坏字就这两处**，没有第三种形态。
**本页照抄，不替它改**（§11.2 ①）。它本来是什么，见「出处」的语料瑕疵那一段。

**图答得了一半**（**④ 图证**）：`97841.png` 上第 4、5 行（`S1`、`S0`）
的**行号与 `Pin Name` 之间**确实有一个 **√ 形状**的记号，别的行那一格是空的；
`97842.png` 上第 10–12 行（`CP`、`DS7`、`DS0`）同样有。
**但「那个字的码位是什么」图答不了**——图只给字形，不给编码。

### `Type` 列：两类组各有代号

> 「- The Type column identifies the type of each pin (I, O and IO) and each group (D and E).」

原文给了两个组的代号：

- `D` — `Digital fixed groups`
- `E` — `Expression-based groups`

⚠️ **图与正文在大小写上对不上**（**观察，不是矛盾判定**）：正文这一句写的是大写 `(I, O and IO)`，
而两张图里 **pin 的类型显示的是小写** `i` / `o` / `io`，组的 `D` / `E` 才是大写。
**原文没有解释这件事，本页两处并列。**

### 非活跃成员：`Group Members` 里的 `*`

> 「In the Group Members area, the "*" character in the Type column marks the inactive members, whose types are different with the one shown in the Component Type list.」

**注意 `*` 标的是「非活跃」，不是「不属于这个组」**——按上面那条 `Note`，
它们**必须留在组里**，别的组拿这个组去定义时才能激活它们。

### 界面：两张图（**④ 图证**）

原文挂了两张图，路径都是 `../../../../raw/x.png`——**往上四层正好是 `tdc-html/`**（§11.4）：

| 图 | alt 文字（**可搜**） | 文件 | 尺寸 | 字节 |
|---|---|---|---|---|
| 固定组 | `The atomar group example`（`atomar` 原文如此） | `97841.png` | 733 × 383 | 8,551 |
| 表达式型组 | `The expression based group example` | `97842.png` | 679 × 448 | 12,295 |

**这两张图是本页唯一能证明「界面长什么样」的东西。** 读出来的是 **④ 图证**——
**图里的字去 raw 里 grep 是 grep 不到的**，要核只能自己再开那张图（§11.4）。

**`97841.png`（固定组）逐格读出的**：

- 窗口上**一个 tab，标题 `mode`**（后面一个 `×`）。
- 左表表头 **`Available Pin List`**；列是：行号 / 一个**没有表头的空列** / `Pin Name` / `Type`。
- 左表 12 行逐格：`CP` `i`、`DS7` `i`、`DS0` `i`、`S1` `i`、`S0` `i`、`_MR` `i`、
  `Q7` `o`、`Q0` `o`、`I/O7` `i`、`I/O7` `o`、`I/O6` `i`、`I/O6` `o`。
  **注意 `I/O7`、`I/O6` 各出现两次**（一次 `i`、一次 `o`）——**同名两行，图不解释**。
- **`S1`（第 4 行）、`S0`（第 5 行）那两格里有 √ 记号**，其余行空。
- 中间四个按钮：`Add >`、`Add All >>`、`< Remove`、`<< Remove All`。
- 右表 **`Group Members`**，列是：行号 / `Pin Name` / `Type`；**两行：`S1` `i`、`S0` `i`**。
- 最右两个按钮 **`^ Up` / `v Down`**。
- **这张图上没有** `Component Type` 下拉、没有 `Group Expression` 栏、没有 `Category` 列
  ——**这三样只在 `97842.png` 上出现**（**结构性观察**，不是命名性结论）。

**`97842.png`（表达式型组）逐格读出的**：

- tab 标题 **`all_in`**。
- 左表表头 **`Available Group/Pin List`**；列是：行号 / 空列 / `Pin Name` / `Type` / **`Category`**。
- 左表 12 行逐格（名 / `Type` / `Category`）：
  `io_in` `D` `Group`、`io_out` `D` `Group`、`mode` `D` `Group`、`ser_in` `D` `Group`、
  `ser_out` `D` `Group`、`ctrl` `E` `Group`、`all_out` `E` `Group`、`io_pins` `E` `Group`、
  `PORT_IO` `P` `Port`、`CP` `i` `Pin`、`DS7` `i` `Pin`、`DS0` `i` `Pin`。
  后三行（`CP` / `DS7` / `DS0`）**有 √ 记号**。
- 中间 **`Operator`** 框里三个按钮：**`+ Union`**、**`- Difference`**、**`* Intersection`**。
- 再下面 **`Component Type`** 标签 + 一个下拉，**当前显示 `IO`**。
- 右表 **`Group Members`**，列是：行号 / `Pin Name` / `Type`；12 行逐格：
  `_MR` `i`、`I/O5` `io`、`I/O0` `io`、`I/O1` `io`、`I/O4` `io`、`I/O7` `io`、`I/O3` `io`、
  `DS7` `i`、`CP` `i`、`S0` `i`、`I/O6` `io`、`I/O2` `io`。
- 底部一栏 **`Group Expression`**，输入框里是 **`ctrl + ser_in + io_in`**，右边一个按钮 **`Evaluate`**。

**哪些字算图证，逐个数过**（判据同 §11.4：**拿图里的字回 raw 数一遍，能搜到的就不算图证**）：

- **本篇 raw 里 0 次的**（→ **算图证**）：`CP`、`DS7`、`DS0`、`_MR`、`Q7`、`Q0`、
  `I/O7`、`I/O6`、`S0`、`Pin Name`、`Category`、`Port`、`Operator`、`Union`、`Difference`、
  `Intersection`、`Evaluate`、`Group Expression`、`Add`、`Add All`、`Remove All`、`Up`、`Down`、
  `io_out`、`ser_out`、`all_out`、`io_pins`、`PORT_IO`。
- **能搜到的**（→ **不算图证**，只是与正文互相印证）：`Available Pin List`（1 次）、
  `Available Group/Pin List`（1 次）、`Group Members`（5 次）、`Component Type`（2 次）、
  `mode`（2 次）、`S1`（1 次）、`S2`（1 次）、`all_in`（1 次）、`io_in`（1 次）、
  `ser_in`（1 次）、`ctrl`（1 次）。

**图答不了的，照实说**：两张图都是**一次具体配置的截图，不是格式规范**——
「哪些列必填、哪些组合非法」图上没有（那不是图能答的，见「典型用法」两篇子主题）；
`*` 非活跃成员那几个字**图上一个都没出现**（`97842.png` 的 `Component Type` 选的是 `IO`，
成员 `Type` 列只有 `i` 与 `io`，**没有 `*`**）——
**所以「`*` 长什么样」本页没有图证，只有上面那句原文**；
正文说组成员可以是 pin alias（`SmarTest 6.5.3` 起），**而图上 `Category` 列只出现
`Group` / `Port` / `Pin` 三种，没有一条 alias 行**——
**图答不了 alias 在那一列里显示成什么，也不能据图说 alias 不存在。**

## 典型用法

**先说清楚：原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段**，
唯一像例子的地方就是那两张图和它们各配的一句话。
**所以下面这条链是从上面那些定义句里拼的（推断），顺序即原文的叙述顺序**：

1. **决定这个组是哪一类**——`Fixed groups` 还是 `Expression-based groups`（原文的二分）。
   固定组**只装 pin 与 pin alias**；**要装别的组、要做集合运算，就必须走表达式型**。
2. **挑成员**（原文第一句：`you can select group members for a group.`）。
   `97841.png` 上那条路是：左表选中 → `Add >`（或 `Add All >>`）→ 进 `Group Members`；
   已进组的 pin 在左表那一格会**带上 √ 记号**；`< Remove` / `<< Remove All` 往回退；
   **`^ Up` / `v Down` 调成员的先后次序**（**这两个按钮的作用原文一个字没写**——
   本页只从名字与位置说它俩是排序，**这是推断**）。
3. **表达式型还要写表达式、选 `Component Type`、按 `Evaluate`**。
   `97842.png` 上 `Group Expression` 里是 `ctrl + ser_in + io_in`，
   `Component Type` 选 `IO`，右边按钮是 `Evaluate`——
   **原文解释了 `Component Type` 会怎么改写成员（上面那张表），但「什么时候要按 `Evaluate`」
   原文没说**（**这是图上的东西，文字里没有对应句**）。
4. **落盘**：这个编辑器的结果进 pin 配置文件——**这一步的依据不在本篇**，
   来自 [[mapping-pin]] 的对照表（见「和谁有关」）。

**两条硬约束**，来自子主题 `Rules for defining groups`（`17576.htm`），逐字：

> 「The maximum number of the fixed groups is 2400. The maximum number of pins in all groups is 1,228,800. If pins in a new group definition exceed this number, an error message is printed to the report window and the exceeding pins are not included in the group.」

> 「- A new group cannot have a name already used by another digital pin or digital group.」

**第一条注意两件事**：**只给了 `fixed groups` 的上限（2400），表达式型组的上限这篇没写**；
超限时**不是拒绝整个组，而是「超出的那些 pin 不进组」**，并且往 report window 打一条错误信息。
**第二条把命名空间说死了**：组名与 digital pin 名**共用一个空间**。

**哪些组合不合法**，来自子主题 `Incompatible pin groups`（`17580.htm`），逐字：

> 「Although the Pin Group Editor does not restrict your choice of pins when you create a group, certain combinations of pins can cause problems when you display the group in other setup windows.」

> 「With each setup window, the group compatibility is checked before any group operation is allowed. Groups with incompatible pins are not displayed in some setup windows, and are shown in half-tone in the respective define format dialog box.」

**这一段有两层**：**建组时编辑器不拦你**，**到别的 setup 窗口去用的时候才检查**；
不兼容的组**在某些窗口不显示、在对应的 define format 对话框里显示成半调（half-tone）**。

三条具体条件，按原文的三个小标题（**标题里的 `stup` 是原文如此**）：

- **`## Timing stup`**：`The following conditions cause a group's pins to be incompatible:` →
  `mixed input and output pins` / `pins with different operating modes`。
- **`## Level stup`**：`A group cannot contain mixed output and bidirectional (io) pins`
- **`## Vector stup`**：`You can only enter all i, all o, or all io pins in the parameter column.`

⚠️ **三个小标题都写成 `stup`，而正文别处的词是 `setup`**——**原文如此，本页照抄**
（这条只是记下来，**本页不替它判定是不是漏了 `e`**）。
另外 **`Vector stup` 那一条讲的是 `parameter column`**，**那是不是 pin group editor 里的列，
这篇没有说**——**本页不主张它属于哪个界面**。

## 和谁有关

- [[mapping-pin]] — **同段的对照页，本页在它表里的那一行是钉住的**：
  它的表里「固定 pin 组 / 表达式型 pin 组」那一行的 **GUI 格就是本页**、
  文件格是 [[pin-configuration-file]]、**L1 格是 `DFGP` / `DFGE` 两条并列**。
  **⚠️ 那一格的两条命令，本篇一处都没出现**（见下一条），
  所以**这条对应关系本页不背书**——依据只在 [[mapping-pin]] 上。
- [[dfgp]] — **固定组在 L1 侧的命令**。**但 `DFGP` 这个词在本篇 raw 里出现 0 次**
  （4 个数过：`DFGP` / `DFGE` / `UDGP` / `DFPT` **都是 0**）。
  **所以「哪个编辑器对应哪条命令」本页没有任何依据**——
  [[dfgp]] 那页自己也记着「本篇没有提任何 GUI」。
- **`DFGE`（表达式型组）、`UDGP`（撤销组）、`DFPT`（定义 port）三条本 wiki 没有建页**，
  **所以本页不链它们**。它们的并列关系只出现在 [[mapping-pin]] 的表格与 [[pin]] 的
  「涉及对象」节里——**那两页读过它们的原文，本页没有**。
  三者的名字在本页一律按普通文本写，不做链接。
  它们真正讲什么，见 [[pin]]（`DFGE` 的示例代码在那页）与 [[command-reference]]（`02.06` 章入口）。
- [[pin-configuration-file]] — **同一份配置的落盘侧**（GUI ↔ 文件）。
  **这两句不是本页 raw 的句子**，来自 [[mapping-pin]] 的对照表；**本页没有回那篇原文核**。
- [[pin-configuration-tool]] — **本编辑器是它 `Pin Settings` 下的一个编辑器（`Groups`）**。
  依据来自 [[pin-configuration-tool]]，**本篇一个字没提这个工具**。
  它那一页另记了一条与 port 有关的规则（`Ports are automatically pin groups.`），
  **本页不重复**——那是 [[pin-configuration-tool]] 读 `02.08.04.18.03.03`（Port Editor）得来的。
- [[pin]] — **`stage: pin` 的理由。这是「最近的一段」，不是归属**（§6）。
  那页把本页列为本阶段的 GUI 侧编辑器之一。
- [[digital-pins-editor]] / [[dps-pins-editor]] / [[utility-pins-editor]] — **同 `stage: pin`、
  同 `layer: gui` 的编辑器族**，写法可以互相对照。
  **分工看起来是互补的**：那几页是「配针」的表，
  **本页没有表，本页是「把已有的针（和组）挑成组」**（推断，依据是原文第一句
  `you can select group members for a group.` 与两张图的界面）。
  **本页读的是它们的 wiki 页，没有读它们各自的 raw**；
  其中 [[utility-pins-editor]] 那一页**本页连 wiki 页也没读**，**它的列不在这里替它说。**
- [[conf]] / [[dfpn]] / [[dfps]] — 同族命令（`CONF` 设 pin 类型与工作模式、`DFPN` 定义 pin 名、
  `DFPS` 定义 DPS pin 名——**这三句定位取自 [[mapping-pin]] 的表，不是本页 raw**）。
  **`DFPN`、`DFPS` 在本篇 raw 里都是 0 次**；
  **但它们与本页的关系是硬的，只是硬在子主题上**：
  `Rules for defining groups` 说组名不能与 **digital pin** 重名——
  **digital pin 名正是 [[dfpn]] 定义的**（推断，依据是这条规则的措辞 + [[dfpn]] 那页的定位）。
  **本页没有读 [[dfpn]] / [[dfps]] / [[conf]] 的原文。**
- [[command-reference]] — **`02.06` 章入口**。本页涉及的那四条命令
  （`DFGP` / `DFGE` / `UDGP` / `DFPT`）的原文都在那一章
  （依据是 [[dfgp]] 那页的 `sources` 路径与 [[pin]] 的 `sources` 清单），
  **但本页一篇都没读**——这里只作为「去哪儿找」的指针。
- **原文 `## Related information` 只有一条链接**，逐字：`[Pin group](<02.08.04.18.01.02_Pin_group.md>)`
  ——**那是「pin group」这个概念本身，本 wiki 没有这一页**（`pin-group` 未建），
  **所以本页不链接它**。按 §2.5，这条只是**证据档 ②「文档之间有链接」**：
  它**只证明那篇文档认为读者该去看那一篇，不证明等价**。

## 版本

本页三篇 raw 的 `## Functional changes` **各只有一条或两条**，全部逐字：

- 本篇（`97914.htm`）**两条**：
  - `Introduced before SmarTest 6.3.2`
  - `SmarTest 6.5.3: When a pin group is created, the pin alias can be added as a group member.`
- `Rules for defining groups`（`17576.htm`）**一条**：`Introduced before SmarTest 6.3.2`
- `Incompatible pin groups`（`17580.htm`）**一条**：`Introduced before SmarTest 6.3.2`

**三条必读：**

1. **`Introduced before SmarTest 6.3.2` 是哨兵值，不是「6.3.2 的变更」**（§11.2 ②）——
   它的意思是「**在本文档集覆盖范围开始之前就已经有了**」。
   **照字面读会得出「6.3.2 新增了这个编辑器」这个假结论，而它格式齐整。**
   **所以本编辑器真实引入的版本，语料未写。**
2. **本篇的第二条是一条真版本事实**（自带版本号、措辞是 `SmarTest 6.5.3:`）：
   **6.5.3 起，pin alias 可以当组成员**。
   注意它**与正文的措辞对得上**：正文说固定组「由 digital pins **and pin aliases** 组成」、
   表达式型组「由 digital pins, **pin aliases**, and/or other groups 组成」——
   **两处都把 pin alias 写进了成员种类，那正是 6.5.3 之后的状态**。
3. **本篇 `## Functional changes` 里没有一条改名 / 改界面的记录**——
   没有 `Changed ... to ...` 这种句子，只有那一条 `6.5.3` 的功能增补。

**⚠️ 因此，从图上读到的名字，本页一个都不能当「现名」**（§11.4）：
`mode`、`all_in`、`io_in`、`io_out`、`ser_in`、`ser_out`、`ctrl`、`all_out`、`io_pins`、
`PORT_IO`、`CP`、`DS7`、`DS0`、`_MR`、`Q7`、`Q0`、`I/O0`–`I/O7`、`S0`、`S1`，
以及 `Available Group/Pin List` / `Category` / `Operator` / `Union` / `Difference` /
`Intersection` / `Evaluate` / `Group Expression` 这些界面名——
**在 `## Functional changes` 里查不到任何一条比图更新的改名记录，**
**所以：这张图的版本不明。** 本页按图上写的样子记，**但不声称那就是 7.10.3 的现名**。
**不受这条影响的是结构性的东西**（两张图各是哪一类组的界面、有哪些面板与按钮、
哪个列表带 `Category` 列）——**那类结论与版本无关**。

## 出处

`sources:` **3 篇**：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02_Pin_group_editor.md`
（TDC `97914.htm`，**3,563 字节，114 行**）、
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.01_Rules_for_defining_groups.md`
（TDC `17576.htm`，**698 字节，15 行**）、
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.02_Incompatible_pin_groups.md`
（TDC `17580.htm`，**1,050 字节，29 行**）。
**三篇都整篇读完。** 口径：字节 = `len(path.read_bytes())`，行 = `wc -l`（§11.5）；
三篇都是 CRLF。

**这一段单说图**（§11.4）。本页读了**那两张图，两张都读了**：

- `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\97841.png`（`The atomar group example`，
  733 × 383，8,551 字节）与 `...\raw\97842.png`（`The expression based group example`，
  679 × 448，12,295 字节）。原文里的路径是 `../../../../raw/97841.png` 这种，
  **往上四层正好是 `tdc-html/`**，所以它们就在 `tdc-html/raw/` 下。
- **从图里读到的**（④ 图证，**不可检索**）：两张图的 tab 标题（`mode` / `all_in`）、
  两张图左表的**全部 12 行逐格取值**、右表 `Group Members` 的全部逐格取值、
  四个搬移按钮与 `^ Up` / `v Down`、`Operator` 那三个按钮、
  `Group Expression` 里的 `ctrl + ser_in + io_in` 与 `Evaluate` 按钮、
  `Component Type` 当前值是 `IO`、`Category` 列的存在与它的三个取值
  （`Group` / `Port` / `Pin`）、`S1`/`S0`/`CP`/`DS7`/`DS0` 那几格里的 **√ 记号**。
  **这些字去 raw 里 grep 是 grep 不到的**——上面「界面」一节列出了逐个数过的结果
  （28 个串 0 次、11 个串能搜到）。**要核只能自己再开那两张图。**
- **图答不了的**（照实列）：哪些列必填、哪些组合非法（那是子主题两篇的文字，不是图）；
  `*` 非活跃成员在 `Type` 列里长什么样（**图上 0 个 `*`**）；
  pin alias 在 `Category` 列里显示成什么（**图上只有 `Group` / `Port` / `Pin`，没有 alias 行**）；
  那个 √ 记号的**码位**（图只给字形）；**这两张图的版本**（图上没有版本标注）。

**本页没做的**：

- **一张图都没少读**——原文只有这两处图引用，两处都读了。
  **也没多读别的图**（本页没有为核别的话去开第三张图）。
- **为了两件事，另外开了上游的 `.htm`**：`tdc-html/raw/97914.htm`（**7,232 字节，95 行**）。
  **它不是本页的 `sources`**（不是 `by-category/` 下的 md，格式上也列不进 `sources`），
  只用来判两件事，结论都写在下面「语料瑕疵」里：
  ① 那处坏字**本来是哪个字**；② `S1 and S2` 到底是**转换坏的还是上游就坏的**（§11.2 ⑥）。
- **`02.06` 的命令原文一篇没读**。`DFGP` / `DFGE` / `UDGP` / `DFPT` **只在本页出现名字**，
  **语法、参数、错误，本页一个字没有**。
- **子主题两篇之外的文档（raw）一篇没读**：`02.08.04.18.03.02` 的兄弟页
  （`...03.01_Pin_setting_editors` 那一族、`...03.03_Port_Editor`、`...03.04_Alias_Set_Editor`）
  和原文 `## Related information` 指向的 `02.08.04.18.01.02_Pin_group`，**都没读**。
  **所以「这个编辑器与 port / alias set 的关系」，本页只有从别页转来的话，没有本页自己的依据。**
  （**读过的 wiki 页不算 raw**：本页读过 [[mapping-pin]] / [[digital-pins-editor]] /
  [[dps-pins-editor]] / [[dfgp]] / [[pin-configuration-tool]] / [[pin]] 等页，
  **但没有读它们各自 `sources` 里的 raw**。）
- **本页没有一条命令事实、没有一条 API 事实。**
- **没有在机台上开过这个编辑器、没有生成过 pin 配置文件。**
  `verified: doc-only` 指的就是这件事。
- **没有实跑、没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pin.md`。
- **「典型用法」那条链是拼的，不是原文的过程**——原文没有过程段（见那一节开头的说明）。

> ⚠️ **本篇的语料瑕疵与对不上的地方，照实记、一处没替它改**：
> ① **两处坏字，同一个形态 `鈭?`**（第 24 行与第 98 行）。
>    `extract/encoding-map.csv` 把 `鈭` 归在**「反解不了——第三字节已丢」**那一类，
>    只给得出区间 **`U+2200–U+223F`**。
>    **但这一处能定死**：上游 `raw/97914.htm`（本篇 `source_topic` 的那个号）
>    该处的字节是 **`E2 88 9A` = U+221A `√`**（十六进制核过），
>    **图上那一格也正是一个 √ 形状的记号**。
>    **本页引文照抄 `鈭?`，没有替它改成 `√`**——搜的时候要搜坏掉的那个形态（§11.2 ①）。
> ② **正文说固定组「has two members: S1 and S2」，图上是 `S1` 与 `S0`。**
>    原文逐字是 `has two members: S1 and S2.`，而 `97841.png` 的 `Group Members`
>    第 1、2 行是 `S1` / `S0`，左表里**有 `S0`、根本没有 `S2`**
>    （**放大核过**：那个字形是闭口的 `0`，不是 `2`）。
>    **这一处不是转换坏的**——上游 `raw/97914.htm` 里也是 `S1 and S2`（纯 ASCII，没有坏字）。
>    **两处并列，本页不替它判定哪一处是对的**（§11.2 ⑥）。
> ③ **`O` 与逗号之间多一个空格**（`(I, O , IO and DC)`），而同篇别处是 `(I, O and IO)`。
>    **照抄。**
> ④ **`UNION` 那一条里 `A=` 后没有空格**（`=> A= {a,b}`），同一条前面却是 `A = (a + b + a)`。
>    **照抄。**
> ⑤ **子主题 `Incompatible pin groups` 的三个小标题都写成 `stup`**（`Timing stup` /
>    `Level stup` / `Vector stup`），而这个词在别处是 `setup`。**照抄，不替它补 `e`。**
> ⑥ **图上 `I/O7`、`I/O6` 各出现两次**（一次 `i`、一次 `o`），
>    **原文没有解释同名两行是什么**。**本页不猜。**
> ⑦ **图与正文的 `Type` 大小写对不上**：正文 `(I, O and IO)` 大写，图上 pin 是小写 `i`/`o`/`io`。
>    **两处并列。**
> ⑧ **`Vector stup` 说的 `parameter column` 属于哪个界面，两篇子主题都没说。**
>    **本页不主张它在本编辑器里。**

`verified: doc-only`
