---
type: object
title: DFGP, DFGP? - (DeFine GrouP)
layer: L1
stage: pin
tags: [pin, dfgp, pin-group, pin-configuration, command, dps]
related: [pin, mapping-pin, dfge, dfpn, dfps, dfpt, conf, udgp, pin-configuration-file, pin-group-editor, pin-config-requires-sequencer-off]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# DFGP, DFGP? - (DeFine GrouP)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,713 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFGP

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### DFGP?

```
DFGP? {(pin_group)}
```

returns:

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### Parameters

| pin_type | Defines the type of pins in the group. This can be: | Defines the type of pins in the group. This can be: |
|---|---|---|
| pin_type | I | Identifies a group of device input pins. |
| pin_type | O | Identifies a group of device output pins. |
| pin_type | DC | Identifies a group of DC type pins. |
| pin_type | X | Identifies a group that may contain pins of any type. |
| pinlist | The names of the pins to be included in the group. All pin names must be separated with a comma. | The names of the pins to be included in the group. All pin names must be separated with a comma. |
| pin_group | The name assigned to the pin group. You can use the same name for groups of different type.<br><br>The symbol @ can be used with the DFGP? query to list all groups previously defined using the DFGP command. If you query a non-existent group, the system returns nothing.<br><br>Maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest. | The name assigned to the pin group. You can use the same name for groups of different type.<br><br>The symbol @ can be used with the DFGP? query to list all groups previously defined using the DFGP command. If you query a non-existent group, the system returns nothing.<br><br>Maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/98546.htm`。

### Example

```
DFGP O,(Q0,Q1,Q2,Q3),(outputs)
```

This example defines a group called outputs which contains pins Q0, Q1, Q2 and Q3.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md>` 的 `## Errors`、`## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

-  More than 2400 groups are defined.
-  The intended group name is already being used for a pin.
-  The intended group name is already being used for a DPS pin.
-  There are too many pins in the group (max. number of pins in all groups is 1843200).

### Warnings

A warning is generated if:

-  A pin cannot be part of the specified group and is therefore ignored.
-  A group cannot be part of the specified group and is therefore ignored.

<!-- 报错节 end -->

## 是什么

**`DFGP`（DeFine GrouP）定义一个「固定 pin 组」。** 原文前两句就是全部定义与用途：

> 「The DFGP (DeFine GrouP) command defines a fixed group of digital pins. Pin groups can be used as though they were individual pins. The DFGP? query returns a list of the pins and pin types in the named group.」

三件事**挤在两句话里**，拆开是：

| 句 | 说的是什么 |
|---|---|
| `defines a fixed group of digital pins` | **动作**：定义；**对象**：数字 pin 的固定组 |
| `Pin groups can be used as though they were individual pins` | **为什么要定义它**：定义完之后，**组可以当单个 pin 用** |
| `The DFGP? query returns a list of the pins and pin types in the named group` | **查询**：`DFGP?` 按组名返回**成员 pin 与 pin 类型** |

**第二条是本页的价值所在**：`DFGP` 不是一个「整理名单」的命令，**它造出来的东西在后续命令里能顶一个 pin 名用**——原文用的是 `as though they were`（**就像它们是**）。**哪些命令能用组名，本篇没有列**，所以本页也不举例。

### 最该记的一条机制：同名复用是**追加**，不是替换

> 「Reusing a group name causes the pins in the new group definition to be appended to the pins in the original definition.」

**这一句决定了 `DFGP` 的用法与陷阱**：拿同一个组名再发一次 `DFGP`，**旧成员不会消失，新成员会接在后面**——**所以同名组只会变大，不会变小**（推断，依据就是 `appended to` 这一句）。**要把组改小、或者清空，本篇一个字没写**（**本页不替它填**）。

### 语法两条：定义与查询分在两个小节

本篇**没有 `## Syntax` 段标记**，而是把两条语法**分成两个 `## ` 小节**写：

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

```
DFGP? {(pin_group)}
```

而查询**返回的形态就是定义那一行的形态**：

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

**所以 `DFGP?` 的返回串看着能照着再发一遍**（推断，依据是返回串与本篇 `## Example` 里那条定义**逐字同形**；**本篇没有说这句话，本页把它标成推断**）。

### `pin_type` 四个取值

| 值 | 原文 |
|---|---|
| `I` | 「Identifies a group of device input pins.」 |
| `O` | 「Identifies a group of device output pins.」 |
| `DC` | 「Identifies a group of DC type pins.」 |
| `X` | 「Identifies a group that may contain pins of any type.」 |

**四个值里只有 `X` 是「什么都收」**。原句是：

> 「Defines the type of pins in the group. This can be:」

（四个取值本身是**表格里的格子**，逐字见本页「语法 / 参数」节。）

### `pin_group` 的四条硬规矩

| 规矩 | 原文 |
|---|---|
| **同名可以跨类型复用** | 「You can use the same name for groups of different type.」 |
| **`@` 列举所有已定义的组** | 「The symbol @ can be used with the DFGP? query to list all groups previously defined using the DFGP command.」 |
| **查不存在的组返回空** | 「If you query a non-existent group, the system returns nothing.」 |
| **组名长度** | 「Maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.」 |

**「同名可以跨类型复用」要和上面那条「追加」一起读才不矛盾**：`You can use the same name for groups of different type` 说的是 **I 组和 O 组可以重名**（类型不同就不算同一个组）；**它不是说同一类型下的重名是替换**——同一类型的重名按上面那条**追加**。

### `## Application`：它属于哪一块

> 「Pin Configuration, see Configuration Setup Commands.」

**`DFGP` 是 Pin Configuration 一族里的命令**（后一句就是那个链接名）。**这是本篇唯一一处「它在体系里的位置」**——本篇没有 `## Predependencies`、没有 `## Related information`。

### `## Errors` / `## Warnings` 的读法

**四条报错没有一条是语法错**，全是「数量」与「重名」（逐字见本页「报错条件」节）：

| 触发 | 原文 |
|---|---|
| 组数超限 | 「More than 2400 groups are defined.」 |
| **组名与 pin 名撞车** | 「The intended group name is already being used for a pin.」 |
| **组名与 DPS pin 名撞车** | 「The intended group name is already being used for a DPS pin.」 |
| pin 数超限 | 「There are too many pins in the group (max. number of pins in all groups is 1843200).」 |

**四条里两条是重名**：`DFGP` 的组名**不能与 pin 名或 DPS pin 名相同**。**注意最后一条的措辞**：句子的主语是 `too many pins in the group`，而括号里的判据是 `in all groups`——**按原文，这是「所有组加起来的 pin 总数」而不是「单个组」**。**本页按原文措辞照记，不改。**

**两条 `Warnings` 都是「静默丢东西」**：pin 或组**进不了指定的组，就被忽略**：

> 「A warning is generated if:」

- 「A pin cannot be part of the specified group and is therefore ignored.」
- 「A group cannot be part of the specified group and is therefore ignored.」

**也就是说：`DFGP` 不保证你写进去的 pin 都真的进了组**——**它给 warning，然后继续**（推断，依据是这两条的措辞 `is therefore ignored`）。**哪些 pin / 组会被忽略，本篇没写**（**本页不替它列**）。

> **一处「没有」也要记**：同族命令里，`DFPN` / `UDEF` / `CONF` / `PALS` 的文档都带「**sequencer 不在 OFF 状态就报错**」这一类条目（见 [[pin-config-requires-sequencer-off]]，它的清单里正是这四条），**而 `DFGP` 本篇的 `## Errors` / `## Warnings` 两段里没有 `sequencer` 这个词**（本页实测 0 命中）。**本页照实说：本篇没有这条约束**——**这不等于「`DFGP` 随时可用」**，只是本篇没写。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`**——它是一篇命令参考，不是任务页。**能写出来的用法只有三件，全部来自本篇的 `## Example` 与 `## Parameters`。**

### 1. 定义一个组（本篇唯一的例子，逐字）

```
DFGP O,(Q0,Q1,Q2,Q3),(outputs)
```

> 「This example defines a group called outputs which contains pins Q0, Q1, Q2 and Q3.」

**照参数表读这一行**：`O` 是 `pin_type`（输出 pin 组），`(Q0,Q1,Q2,Q3)` 是 `pinlist`，`(outputs)` 是 `pin_group`。**三段用逗号分隔，后两段各自带括号、第一段不带**。**语法串 `DFGP {pin_type}, {(pinlist)}, {(pin_group)}` 里的花括号是「这里填东西」，不是要打进去的字符**（推断，依据是例子里的实际写法）。

### 2. 查回来

**本篇只给了查询的语法，没有给查询的例子**：

```
DFGP? {(pin_group)}
```

- 查某个组 → 返回该组的 `pin_type` / 成员 pin / 组名。
- 查**全部已定义的组** → 用 `@`（原文：`The symbol @ can be used with the DFGP? query to list all groups previously defined using the DFGP command.`）。
- 查**一个不存在的组** → **什么都不返回**（原文：`If you query a non-existent group, the system returns nothing.`）。
  **这一条要注意**：`returns nothing` **不是报错**——**按本篇 `## Errors` 那四条，查不存在的组不在报错清单里**（推断，依据是两处措辞的对照）。

### 3. 加成员：再发一次同名 `DFGP`

**这是本篇唯一给出的「改」的路径**，而且是**追加**：

> 「Reusing a group name causes the pins in the new group definition to be appended to the pins in the original definition.」

**所以「给一个已有组补 pin」就是重发一条同名 `DFGP`。** **反过来（把某个 pin 从组里去掉）本篇没有路径**（**语料未写**）。

### 一个组名、可能有两个类型

**`DFGP?` 的返回里带 `pin_type`**（`The DFGP? query returns a list of the pins and pin types in the named group.`）——**所以「这个组是什么类型」不用猜，查一下就有**。而组名本身不携带类型：原文 `You can use the same name for groups of different type.` **所以同一个名字下面可能同时存在 I 组和 O 组**——**查的时候要按类型读返回**（推断，依据是这两句的合读；**本篇没有给重名的查询例子**）。

## 和谁有关

- [[mapping-pin]] — **同段的对照页，`DFGP` 在它表里的那一行是钉住的。** 它的表里「固定 pin 组 / 表达式型 pin 组」那一行的 **L1 格是 `[[dfgp]] / [[dfge]]` 两条并列**、文件格是 [[pin-configuration-file]]、GUI 格是 [[pin-group-editor]]。**与 `DFGP` 自己的文档对得上**：本篇 `## Application` 写的 `Pin Configuration` 与那两格一致。**本页没有发现那一页把 `DFGP` 读错**（**`DFGE` 那一半本页没核**，见「本页没做的」）。
- [[dfge]] — **另一条命令**（表达式型 pin 组）。**`DFGP` 自己的文档从头到尾没有提过 `DFGE`**（本页实测 0 命中）——两者的并列关系只出现在 [[mapping-pin]] 的表与 [[pin]] 的「涉及对象」节里，**本篇一个字都没有**。**本页不把 `DFGE` 的内容写进来。**
- [[pin]] — **本阶段（`stage: pin`）的脊椎页。** 它在「Pin group 与 port」一节里把 `[[dfgp]]` / `[[dfge]]` 与 `[[dfpt]]` / `[[udgp]]` 并列，**并在「常见错误」里记了一条与本页 `## Errors` 直接对应的**（组名与 pin 名冲突）。**注意另一条**：那一页还记了「把不匹配类型的 pin 加进组，固件不报错」——**本页 `## Warnings` 只说「进不了组就被忽略」，没有说类型不匹配会不会报错**，**那一节的判据不在本篇，本页不引用它的结论**。
- [[pin-configuration-file]] — **`DFGP` 的落点。** 本篇 `## Application` 说它属于 Pin Configuration；**那条「GUI ↔ 文件 ↔ 固件命令逐条对应」的声明在 [[mapping-pin]] 里，不在本篇。**
- [[pin-group-editor]] — **GUI 侧**（[[mapping-pin]] 表里的那一格）。**本篇没有提任何 GUI。**
- [[dfpn]] / [[dfps]] — **同族的定义型命令，也是本页两条报错的另一半**：`DFGP` 报「组名已被某个 pin 用掉」「已被某个 DPS pin 用掉」——**pin 名由 [[dfpn]] 定义、DPS pin 名由 [[dfps]] 定义**。**这两条 Errors 的存在本身说明三者的命名空间是共享的**（推断，依据是这两条的措辞）。**本页没有读这两篇。**
- [[conf]] / [[dfpt]] / [[udgp]] — 同族命令（`CONF` 设 pin 类型与工作模式、`DFPT` 定义 port、`UDGP` 撤销组）。**三者都不在本篇里出现**；[[pin]] 的「涉及对象」节把它们与 `[[dfgp]]` 并列。
- [[pin-config-requires-sequencer-off]] — **该约束页的清单里没有 `DFGP`**（它收的是 `DFPN` / `UDEF` / `CONF` / `PALS` 四条），与本页「`## Errors` 段里没有 sequencer」这一处**互相对得上**。**本页据此把「没有」记成事实，而不是记成缺失。**
- `sqst` — **只在反面出现**：它是「sequencer 状态」的查询命令，与本篇无关。**本页列它，是为了说清「本篇不牵扯它」**——`DFGP` 的文档里没有 `SQST`（0 命中）。
- `ganging` — **本页不连线。** 本篇 `## Errors` 里出现过一次 `DPS pin`，但**本篇没有一个字讲 ganging**，**本页不据一个词面去接那一页。**

## 版本

`## Functional changes` 段有，**只有一条**：

> 「Introduced before SmarTest 6.3.2」

⚠️ **这一条是哨兵值，不是「6.3.2 新增了 `DFGP`」。** 按 `schema.md` §11.2 ②，`Introduced before SmarTest 6.3.2` 是本语料 2,677 条可用性行共用的写法，意思是「**在本文档集覆盖范围开始之前就已经有了**」。**照字面读会得出「6.3.2 新增了 `DFGP`」这个假结论，而它的格式很齐整。**

**所以：`DFGP` 真实引入的版本，语料未写**——**本页不知道它早到什么时候。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`
（TDC `98546.htm`，3,275 字节，76 行）。**整篇读完**，本页引文全部来自这一篇。

> **它是同一篇的第二次投放。** 同一篇还以 `02.06.03.02.05_DFGP__DFGP__-__DeFine_GrouP.md`
> 存在（`source_topic` 分别是 `98546.htm` 与 `98546_2.htm`）。**本页把两份逐字节比过**：
> **正文完全相同，唯一差别在 frontmatter 的 `source_topic` / `source_html` 两行**（§10 的「重复投放」）。
> **所以本页的文档号只写了一个，不是漏列**；数入度时两条要当一篇看。

**本页没做的**：

- **对照页只核了 `DFGP` 那一行。** [[mapping-pin]] 是整篇读过的（它是本页的「同族页」对齐材料），但**本页只用它核对 `DFGP` 的对应关系**，**没有核它 `DFGE` 那一半，也没有核它 pin 组那一行的 L2 / L3 格**。
- **`DFGE`（`02.06.02.02.59`）没读。** 所以「固定组与表达式组有什么差别」**本页一个字没有**——本页只知道 `DFGP` 的文档里**没有提过 `DFGE`**。
- **`UDGP` / `DFPN` / `DFPS` / `DFPT` / `CONF` / `CTXT` 的命令页一篇没读。** 它们的名字只从 [[pin]] 与 [[mapping-pin]] 的对应关系里来，**职责一句话也没有回到原文复核**。
- **`pin-group-editor` 那篇 GUI 文档没读。** 所以「GUI 上怎么建一个固定组、组名在界面哪个字段」**本页没有**。
- **三篇 pin group 的 GUI 文档没读**：`02.08.04.18.02.08_Working_with_pin_groups`、`02.08.04.18.03.02.01_Rules_for_defining_groups`、`02.08.04.18.03.02.02_Incompatible_pin_groups`（它们出现在 [[pin]] 的 `sources:` 里）。**「哪些 pin / 组会被忽略」「组与 timing / level / vector setup 的兼容性」「组数上限到底是多少」全在那三篇**，而本页的 `## Warnings` 只有「被忽略」这一句。
- **图：本篇文档没有内嵌图片**，所以**本页没有 ④ 图证**。
  判据可核：本篇 md 里 `png` / `jpg` / `![` **0 命中**，
  其上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\98546.htm` 里 `<img` 与 `.png` **也 0 命中**。
  **不是「图够不着」，是这篇文档不带图**——**所以 [[mapping-pin]] 那种「从 pin 编辑器截图读出参数顺序」的办法，在这一篇上无从施展**。
- **编码坏字：本篇 0 处**（按 `schema.md` §11.2 ①的判据，用 `[\u4e00-\u9fff]` 扫过整篇，**一个汉字都没有**）。**整词替换（`DC/DC power units`）本篇 0 命中**——**两条都没有，这是实测结果，不是没查。**
- **没有实跑。** 没有在机台上发过 `DFGP`、没有建过组、没有触发过那四条 Errors 或两条 Warnings 里的任何一条。`verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[pin]]。

> ⚠️ **本篇的语料瑕疵，照实记下、一处都没替它改**（§11.2）：
>
> **① `## Application` 的提示句多一个 `of`。** 逐字是：
> `Note The maximum of number of characters for the pin group name is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.`
> ——**`The maximum of number of characters` 应为 `The maximum number of characters`**。
> **同一篇的 Parameters 表里写的是对的那一版**：`Maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.`
> **一处限值、两种写法，本页并列，不替它改。**
>
> **这一处在上游 `.htm` 里就是坏的**：`98546.htm` 里逐字是 `The maximum of number of`，
> 且它包在一个 `<div class="note">` 里。**按 `schema.md` §11.2 那张表的判据，这属于「上游就坏的」，
> 不是转换造成的**——**所以将来重做一次转换也救不回来。**
>
> **② `Note` 标签被压平进正文（同一句）。** `98546.htm` 里它是一个独立的提示块
> （`<div class="note">` 里带一个 `Note` 标签），**md 里标签与句子粘成了一行**——
> 于是看起来像 `## Application` 底下有一句以 `Note` 开头的怪句子。**这是转换造成的，本页照实记。**
>
> **③ 同一句话在本篇里出现两次。** `Maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.` 在 **`pin_group` 参数格**里一次，在 **`## Application` 的提示里**再一次（就是上面那句）。
> **`## Application` 整节除了一句 `Pin Configuration, see Configuration Setup Commands.` 就只剩这条重复的限值。**
>
> **④ `## Errors` / `## Warnings` 的列表项，`-` 之后有两个空格。** 逐字是 `-  More than 2400 groups are defined.`
> （`-` 之后**两个空格**，不是排版差异而是 raw 里就有）。**脚本把它逐字抽进本页「报错条件」节时也照抄了这两个空格**，本页照实记。
>
> **⑤ `## Application` 在脚本的「语法 / 参数」节里没有出现。** 本页「语法 / 参数」节收的是 `Parameters` 与 `Example` 两节（脚本按段标记抽，§4）。**这不是脚本漏了**——**记在这里，是免得读者以为 `## Application` 那一段被吞了。**（它整节的内容已写进上面的「是什么」。）

`verified: doc-only`
