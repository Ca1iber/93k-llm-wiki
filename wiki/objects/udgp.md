---
type: object
title: UDGP - (UnDefine GrouP)
layer: L1
stage: pin
tags: [pin, udgp, pin-group, undefine, pin-configuration, command, l1]
related: [pin, dfgp, dfge, dfpt, udpt, udpr, pin-group-editor, pin-configuration-file, command-reference, pin-config-requires-sequencer-off]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.296_UDGP_-__UnDefine_GrouP.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# UDGP - (UnDefine GrouP)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **387 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.296_UDGP_-__UnDefine_GrouP.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDGP {(group)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98822.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：group | Defines the name of the group of pins to be removed. The symbol @ can be used to dismantle all groups. If more than one group is to be removed, the name…

### Example

```
UDGP (Qout)
```

This command dismantles the group entitled Qout.

<!-- 语法节 end -->

## 是什么

**`UDGP`（UnDefine GrouP）是「拆组」命令。** 原文第一句就是全部定义，**而且一开口就点了两个上游**：

> 「The UDGP (UnDefine GrouP) command dismantles a group that has been previously defined by DFGP or DFGE.」

（原文里 `DFGP` / `DFGE` 是两段 markdown 链接，本页按 §11.1 ② 剥掉链接标记；
raw 逐字是 `[DFGP](<02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md>)` 与 `[DFGE](<02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md>)`。）

**一句话拆开是四件事：**

| 词 | 说的是什么 |
|---|---|
| `dismantles` | **动作是「拆掉」**——不是「清空成员」，也不是「改名」 |
| `a group that has been previously defined` | **只能拆已经存在的组**：先有建，才有得拆 |
| `by DFGP or DFGE` | **拆的对象有两类**：`DFGP` 建的**固定组**、`DFGE` 建的**表达式组** |
| `UnDefine GrouP`（标题里的括注） | **它的全名**，也是它在这一族里的位置 |

**第三件事是本页最该记的**：`DFGP` 与 `DFGE` 建的是两种不同的组，
**而撤销只有 `UDGP` 一条——没有第二条「拆表达式组」的命令**（推断，依据就是本页标题与这第一句都只给了一个名字）。

### 被移除的是「组」，不是「组里的 pin」

参数只有一格，说明逐字是：

> 「Defines the name of the group of pins to be removed.」

**中心词是 `group`**，`of pins` 与 `to be removed` 都挂在它身上——
**所以被拿走的是那个组，不是那些 pin**。**pin 本身还在**：
本篇没有一句话说 pin 会消失，也没有说拆组会动配置（**这一条是推断，依据就是这句的语法**；**本篇没有正面写「pin 不受影响」**）。

### 用法三条，全在 `group` 那一格里

| 要点 | 原文 |
|---|---|
| **参数就是组名** | 「Defines the name of the group of pins to be removed.」 |
| **`@` = 拆掉所有组** | 「The symbol @ can be used to dismantle all groups.」 |
| **多个组名用逗号分隔** | 「If more than one group is to be removed, the names must be separated by a comma.」 |

**`@` 那条要读准**：原文写的是 `all groups`，**没有限定类型**——
按字面，**固定组与表达式组会被一起拆**（推断，依据是这一句与第一句的 `by DFGP or DFGE` 合读）。
**但本篇没有给 `@` 的例子，也没有说 `UDGP (@)` 会不会有二次确认、会不会返回什么**——**这两点语料未写，本页不填。**

### 没有查询形态

**本篇标题是 `UDGP - (UnDefine GrouP)`，`## Syntax` 里也只有一条语法**（逐字见「语法 / 参数」节）：

```
UDGP {(group)}
```

**没有 `UDGP?`。** 对比同族：`DFGP` / `DFGE` 的标题都带 `?`、各有一条查询语法，
**`UDGP` 两头都没有**。**所以「拆完还剩哪些组」在本篇里没有查询路径**
（推断，依据是本篇只有这一条语法；**别的命令能不能查到，本篇没说**）。

### `## Application`：它在体系里的位置

> 「Pin configuration, see Configuration Setup Commands.」

**一句话两件事**：`UDGP` 属于 **Pin configuration**；那一族的目录在
`Configuration Setup Commands`（raw: `02.06.03_Pin_configuration_setup_commands.md`，**不在本 wiki 的 allowlist 里，故本页不写双方括号**）。
**这是本篇唯一一处「它在体系里的位置」**——本篇没有 `## Predependencies`、没有 `## Related information`。

### 本页没有「报错条件」节，这是事实不是漏抽

**本篇没有 `## Errors` 段、也没有 `## Warnings` 段**（raw 的五个 `##` 是
`Syntax` / `Parameters` / `Application` / `Example` / `Functional changes`）。
**所以：「拆一个不存在的组会怎样」本篇一个字没写。**
同族命令在这一点上的做法并不一样——**但那是别篇的规矩，本篇没有**，本页不把它安到 `UDGP` 头上。

### 例子只有这一条

```
UDGP (Qout)
```

> 「This command dismantles the group entitled Qout.」

**三个要点**：① 组名用圆括号包住；② **没有类型参数**——`UDGP` 不像 `DFGP` 那样要 `pin_type`；
③ 原文用的还是 `dismantles`，与第一句同一个词。

> **⚠️ 与一条入边文档的措辞对照（本页并列，不替它们统一）**：
> `02.06.03.01.06_Defining_pin_groups.md` 里写着
> > 「The UDGP command serves to delete both fixed and expression based group definitions.」
>
> ——**它用 `delete`，本篇用 `dismantle`。同一件事，两个词。**
> **那句话还多给了本篇没明说的一点**：`both fixed and expression based group definitions`——
> **它把「两类组」写实了**，与本篇第一句的 `DFGP or DFGE` 对得上。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**，
它是命令参考，不是任务页。**能落成动作的只有三条，全部来自 `## Parameters` 与那一个 `## Example`**：

| 要做的 | 发什么 | 依据（逐字） |
|---|---|---|
| **拆一个组** | `UDGP (Qout)` | 本篇 `## Example` |
| **一次拆几个** | `UDGP (A,B)` | 「If more than one group is to be removed, the names must be separated by a comma.」 |
| **拆掉所有组** | `UDGP (@)` | 「The symbol @ can be used to dismantle all groups.」 |

**唯一能说的先后关系是「先建后拆」**——原文第一句的 `previously defined` 就是这个意思；
**建组的两个入口是本篇点名的 `[[dfgp]]`（固定组）与 `[[dfge]]`（表达式组）**。

**⚠️ `@` 这一条是本页最该小心的一格**：没有例子、没有报错说明、没有「能不能撤」的说法。
**本页照实说：语料未写。**

## 和谁有关

- [[dfgp]] / [[dfge]] —— **上游，也是本篇第一句唯一点名的两篇**。
  `DFGP` 建**固定组**、`DFGE` 建**表达式组**，`UDGP` **把两类一起拆**：三者构成「建 / 建 / 拆」一个闭环。
  **闭环的「建」那一半本页没读**（见「本页没做的」）——**本页只据 `UDGP` 这一篇说它拆什么**。
- [[pin]] —— **本阶段（`stage: pin`）的脊椎页**。依据是本篇 `## Application` 的 `Pin configuration`。
- [[pin-group-editor]] —— **GUI 侧**（pin 组的编辑器）。**本篇没有一个字提 GUI**；
  这一条关系来自 `[[pin]]` / `[[pin-group-editor]]` 那一侧（**本页未读该页**）。
- [[pin-configuration-file]] —— `Pin configuration` 的落点文件。**本篇只写了 `Pin configuration` 这个词，没写任何文件**（**本页未读该页**）。
- [[command-reference]] —— **它的归属**：本篇在 `02.06_Command_Reference` 下。
- [[udpr]] —— **同族的 `UD*` 撤销命令**（它的页标题是 `UDPR - (UnDefine Pin Role)`）。
  **本篇一个字没提过它**——**这一条是「命名同族」的推断**，依据是 `wiki/objects/` 下整排 `UD*` 页
  （`UDEF` / `UDGP` / `UDPR` / `UDPS` / `UDPT` / `UDUP` / `UDUT` / `UDVP`）与 `DF*` 一族相对。
  **本页没有读 [[udpr]]。**
- [[dfpt]] / [[udpt]] —— **`UDGP` 的「port 版本」**。入边 `02.06.03.01.01_Introduction.md`
  把四条命令并列在同一行，逐字（原文四段都是链接，本页剥掉标记）：
  > 「Commands for pin groups and ports: DFGP, UDGP, DFPT, UDPT」
  **这一行是「谁和谁配对」的原始依据**：`DFGP↔UDGP`（组）、`DFPT↔UDPT`（port）。**这两篇本页都没读。**
- [[pin-config-requires-sequencer-off]] —— **一处「答不了」**：那页收的是「哪些 L1 命令要求 sequencer 处于 OFF」这类约束，
  **而 `UDGP` 本篇连 `## Errors` 段都没有**，所以**「`UDGP` 是否受这条约束」本篇无从谈起**（**本页不替它填**）。

## 版本

`## Functional changes` 段有，**只有一条**：

```
- Introduced before SmarTest 6.3.2
```

> ⚠️ **这一条是哨兵值，不是「6.3.2 新增了 `UDGP`」。**
> 按 `schema.md` §11.2 ②，本语料 **2,677 条**可用性行共用 `Introduced before SmarTest 6.3.2` 这种写法，
> 意思是「**在本文档集覆盖范围开始之前就已经有了**」。
> **照字面读会得出「6.3.2 新增了 `UDGP`」这个假结论**——**而它的格式很齐整，正是危险所在。**

**所以：`UDGP` 真实引入的版本，语料未写。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.296_UDGP_-__UnDefine_GrouP.md`
（TDC `98822.htm`，**1161 字节 / 43 行**）。**整篇读完**——它是本页四篇 raw 里最短的一篇，
本页引文全部来自这一篇 + `edges.jsonl` 里带原句的边。

> **它是同一篇的第二次投放。** 同一篇还以
> `02_System_reference/02.06_Command_Reference/02.06.03.02.25_UDGP_-__UnDefine_GrouP.md` 存在
> （`source_topic` 分别是 `98822.htm` 与 `98822_2.htm`，1164 字节）。
> **本页把两份逐字节比过：正文完全相同，唯一差别在 frontmatter 的 `source_topic` / `source_html` 两行**
> （逐行 `diff` 只有那两行，+1 字节就是文件名长了 1 个字符）。
> **所以本页的文档号只写了一个，不是漏列**；**数入度时两条要当一篇看**（§10 的「重复投放」）。

**入边 8 条 / 6 篇**（`inline` + `toc` 口径，**两篇投放合并计**）：
`02.06.03.01.06_Defining_pin_groups`（2 条）、`02.06.02.02_List_of_commands`、
`02.06.03.01.01_Introduction`、`02.06.03_Pin_configuration_setup_commands`、
`02.06.03.02_List_of_configuration_commands`、`02_System_reference/index.md`。
**其中两条带原句**（`Defining_pin_groups` 的 `delete` 那句、`Introduction` 的 `Commands for pin groups and ports` 那句），
本页已逐字引在「是什么」与「和谁有关」里。

**本页没做的**：

- **`DFGP` / `DFGE` 两篇都没读。** 所以「固定组与表达式组在建的时候差在哪、拆的时候有没有差别」
  **本页一个字没有**——本页只知道 **`UDGP` 的文档说它两条都拆**。
- **四条入边文档一篇没读**（`Defining_pin_groups`、`Introduction`、两份 `List_of_commands`、
  `Pin_configuration_setup_commands`）。**本页引它们的话，只引 `edges.jsonl` 里那条带原句的边**，
  **没有回原文核上下文**——**所以那几句话在原文里是不是那一节的结论，本页不知道。**
- **`UD*` 同族七页一篇没读**（`UDEF` / `UDPR` / `UDPS` / `UDPT` / `UDUP` / `UDUT` / `UDVP`），
  只读了它们的**页标题**。
- **`pin-group-editor` / `pin-configuration-file` / `pin` 三页没读**（关系描述来自各自的页标题与本篇的 `## Application`）。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **编码坏字：本篇 0 处**（按 §11.2 ① 的判据 `[一-鿿]` 扫过整篇，**一个汉字都没有**）；
  **整词替换（`DC/DC power units`）本篇 0 命中**。**两条都是实测结果，不是没查。**
- **没有实跑。** 没有在机台上发过 `UDGP`、没有拆过组、没有触发过任何一条报错。`verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[pin]]。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① `## Application` 不在本页「语法 / 参数」节里。** 脚本按段标记抽（§4），
> 那一节收的是 `Syntax` / `Parameters` / `Example` 三段。**不是脚本漏了**——
> 记在这里，是免得读者以为 `Pin configuration, see Configuration Setup Commands.` 被吞了
> （它整节的内容已写进上面的「是什么」）。
>
> **② `Parameters` 与 `Example` 的表格在 raw 里是「一格一行 + 游离 `|`」的形态。**
> `## Parameters` 逐字是：` |` / 空行 / `group` / 空行 / ` |` / 空行 / `Defines the name of the group of pins to be removed. The symbol @ can be used to dismantle all groups. If more than one group is to be removed, the names must be separated by a comma.` / 空行 / ` |`
> ——**这是一个被压平的两列表格**（左格参数名、右格说明），**不是脚本切坏**。
> **说明文字一个字没丢**，但**表头（`Parameter` / `Description` 之类）本篇 raw 里没有**。
>
> **③ 同一篇里的 `@` 裸写，没有反引号。** 逐字：`The symbol @ can be used to dismantle all groups.`
> ——**本页照原样引**（本页的 `group` 参数格也照抄了这个裸 `@`）。**本页没有替它加反引号。**

`verified: doc-only`
