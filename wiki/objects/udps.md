---
type: object
title: UDPS - (Undefine DPS pin)
layer: L1
stage: pin
tags: [udps, l1, firmware-command, pin, dps, power-supply, undefine, ganging, license-lock]
related: [dfps, udef, ganging, dps-pins-editor, dps-task, dpspins-resources, udpr, udpt, udup, udut, udvp, pin, command-reference, pin-config-locked-during-test]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# UDPS - (Undefine DPS pin)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **459 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDPS {(pinlist)}
```

### Parameters

|

pinlist

 |

Consists of single or multiple pin names or the symbol @ which undefines all DPS pins. If more than one pin is to be removed, the names must be separated with a comma.

 |

### Example

```
UDPS (Vee)
```

This example removes pin Vee from the setup. The software saves the level data associated with the DPS channel. Therefore if you redefine the channel using the same or a different name, the DPS settings are immediately restored.

<!-- 语法节 end -->

## 是什么

**`UDPS`（Undefine DPS pin）把已经定义过的 DPS pin 从当前 setup 里撤掉**，
而且**顺带解掉 ganging（主从）配置**。原文开头两句就是全部机制：

> 「The UDPS (Undefine DPS pin) command removes any specified DPS pins from your current setup,
> that have previously been defined by DFPS, DFPS? - (DeFine Power Supply).
> The gang (master/slave) configuration is also resolved.」

（原文两处 `DFPS, DFPS? - (DeFine Power Supply)` 是链接，本页按 §11.1 ② 剥掉标记。
两句在 raw 里是**同一行**，本页按 §11.1 的「跨段合并不算错、丢字符才算错」断成两行，**一个字没动**。）

**三句话，三个要点：**

| 原文 | 说清的是什么 |
|---|---|
| `removes any specified DPS pins from your current setup` | **动作**：从 setup 里撤掉指定的 DPS pin |
| `that have previously been defined by DFPS, DFPS? - (DeFine Power Supply)` | **只有「`DFPS` 定义过的」才在射程内**——本命令**不是通用的 pin 删除** |
| `The gang (master/slave) configuration is also resolved.` | **副作用**：**ganging 配置一并被解掉** |

**第三句是本页最要紧的一句，也是它和同族其它命令最大的差别。**
`DFPS` 定义 DPS pin 时**同时定下了通道属于哪个 gang（master/slave）**，
所以撤掉 pin 时**那个 gang 关系就没有依附了**——原文用 `is also resolved`（也一并解决掉）。
**「resolved 之后那两个从通道变成什么状态」本篇没写**（**语料未写**），
**只有这一句话**，没有第二句解释。

### 撤掉之后 level 数据**不会丢**——这是本篇第二条独立机制

例子那一句是全篇最有操作价值的话：

> 「This example removes pin Vee from the setup. The software saves the level data associated
> with the DPS channel. Therefore if you redefine the channel using the same or a different name,
> the DPS settings are immediately restored.」

| 时点 | 原文 | 读出来是什么 |
|---|---|---|
| `UDPS (Vee)` 发生时 | `removes pin Vee from the setup` | pin 从 setup 里没了 |
| **同时** | `The software saves the level data associated with the DPS channel.` | **level 数据被存下来**（存在「那条 DPS 通道」上，不是存在名字上） |
| **之后再定义回来时** | `the DPS settings are immediately restored` | **不用重配，直接就回来** |

**两处最容易读错的地方：**

> **① `using the same or a different name`——换名字重新定义，DPS 设置照样回来。**
> **也就是说那份 level 数据挂在 channel 上，不挂在 pin 名上。**
> （这是原文自己写的，不是本页的推断；**但原文没有正面解释这个机制怎么实现的**。）

> **② 「数据保住」不等于「ganging 也保住」。** 原文在参数和例子里只担保了 **level 数据**；
> **而开头那句说的是 gang 配置被 `resolved`（解掉）**。
> **两句合起来的读法是：pin 定义与 gang 关系会丢，level 数据会留。**
> （**推断**，依据是这两句各管一段、而且方向相反。
> **「重新定义回来时 gang 会不会自动恢复」——本篇未写，本页不判。**）

### 参数只有 `pinlist` 一个，而它是**三合一**的写法

> 「Consists of single or multiple pin names or the symbol @ which undefines all DPS pins.
> If more than one pin is to be removed, the names must be separated with a comma.」

| 你写什么 | 效果 |
|---|---|
| **一个 pin 名** | 撤掉那一个（例子里就是 `Vee`） |
| **多个 pin 名**（**必须逗号分隔**） | 撤掉那几个 |
| **`@`** | **`which undefines all DPS pins`——撤掉全部 DPS pin** |

**`@` 的范围要说准**：原文写的是 `all DPS pins`——
**是「全部 DPS pin」，不是「全部 pin」**（对照 [[udef]] 那篇写的是 `all pins`）。
**所以 `UDPS (@)` 不会碰 digital pin、也不会碰 virtual pin。**

**语法的括号 `{}` 与 `()`**：语法行逐字是 `UDPS {(pinlist)}`，例子逐字是 `UDPS (Vee)`——
**圆括号是要照写的字面字符，花括号是占位框**（读法与 [[udef]] 一致：
**本篇的例子、正文里花括号一次都没出现过**）。
**原文没有解释这两种括号的分工**，**所以这一步是推断，不是文档事实。**

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法只有 `## Example` 一条 + `## Parameters` 那张表。**按目的查**：

| 要做的 | 发什么 | 依据 |
|---|---|---|
| **撤掉一个 DPS pin** | `UDPS (Vee)` | `## Example` 逐字 |
| 撤掉多个 DPS pin | `UDPS (p1,p2)`——**逗号分隔** | `If more than one pin is to be removed, the names must be separated with a comma.`——**原文没有给多 pin 的完整例子** |
| **撤掉全部 DPS pin** | `UDPS (@)` | `which undefines all DPS pins`——**原文没有给 `@` 的命令行例子**（把两个事实合起来写是本页的整理，**不是原文的一条示例**） |
| 先看有哪些 DPS pin 可以撤 | **本篇没有查询语法**——见下 | — |
| 撤掉之后再定义回来 | 再发一次 `DFPS`（**同名或不同名都行**），**设置直接回来** | `Therefore if you redefine the channel using the same or a different name, the DPS settings are immediately restored.` |

**顺序上的三条**：

1. **先有、后撤**：本篇第一句就写明撤的是 `previously been defined by DFPS` 的那些 pin——
   **没定义过的 pin 撤什么，本篇没写**（见下「出错时」）。
2. **撤掉之前先想 gang**：如果这条 DPS 通道在某个 gang 里，
   **`UDPS` 会连带把 gang 配置解掉**（`The gang (master/slave) configuration is also resolved.`）。
   **这是本篇唯一一处警告性质的说明，务必先读它再看别的。**
3. **撤了不等于要重配**：level 数据在，重新 `DFPS` 一条同名或不同名的通道就能拿回来。

**「怎么列出已有的 DPS pin」本篇答不了**：本篇**没有 `DFPS?` 那样的查询**，
**也没有指向查询命令的话**（已核：本篇 `?` 只出现在开头的 `DFPS, DFPS?` 这个名字里）。
**要查就去看 [[dfps]] 那一侧**（本页没读它的原文）。

**一条家族级的锁**：[[pin-config-locked-during-test]]。
`UDPS` 所属那一章（`Pin configuration setup commands`）的**章首**写着
`The firmware does not accept any configuration changes while a test is running.`
**这一句不在本篇正文里**（见「出处」）。
**注意别套错另一条**：[[pin-config-requires-sequencer-off]] 那条（「sequencer 非 OFF 不许改」）
**点名的命令是 `DFPN` / `UDEF` / `CONF` / `PALS`，里面没有 `UDPS`**——
**因为本篇根本没有 `## Errors` 段**（见下）。

### 出错时：**本篇没有 `## Errors`，也没有 `## Warnings`**

已核：本篇 md 里 `## Errors` / `## Warnings` **各 0 命中**，上游 `raw/98823.htm` 里也没有这两节。
**所以「撤一个没定义过的 pin 会怎样」本篇答不了**（**语料未写**，本页不推测）。

> **⚠️ 这是本族里一个不均匀的地方，值得单记**：
> 同族的 [[udpr]] / [[udup]] / [[udut]] / [[udvp]] **都有 `## Errors`**，
> 而 `UDPS` 和 [[udpt]] **都没有**。
> **同一批文档里「有没有写报错」并不一致**，所以「这页找不到报错句」
> **不等于「违反这条命令不报错」**——只等于「这一篇没写」。

## 和谁有关

### 这一族的结构：`UDxx` 是 `DFxx` 的撤销面

**这六个页面（[[udpr]] / [[udps]] / [[udpt]] / [[udup]] / [[udut]] / [[udvp]]）是同一族命令的撤销侧。**
族的划分**不是本页猜的**：`02.06.03_Pin_configuration_setup_commands.md` 逐条给了分组，
逐字（已剥链接标记）：

| 分组（逐字） | 命令 |
|---|---|
| `Commands for DPS pins:` | `DFPS`, **`UDPS`** |
| `Commands for DC Scale pins:` | `DFPN`, `UDEF`, `DFPS`, **`UDPS`**, `PSSL` |
| `Commands for pin alias:` | `DFPR`, `UDPR` |
| `Commands for pin groups and ports:` | `DFGP`, `UDGP`, `DFPT`, `UDPT` |
| `Commands for utility lines:` | `DFUT`, `UDUT`, `DFUP`, `UPAS`, `UDUP` |
| — | `UDVP` **不在这个索引里**（实测 0 命中） |

**所以本页的正命令是 [[dfps]]，两页在索引里同处一行**，逐字：

> 「Commands for DPS pins: DFPS, UDPS」

**而且这一对的配对关系在 `UDPS` 自己的原文里就写着**——第一句的
`that have previously been defined by DFPS, DFPS? - (DeFine Power Supply)` 就是它
（本族六页里，**只有本页和 [[udvp]] 把正命令写在自己的正文里**；
[[udpr]] / [[udpt]] / [[udup]] / [[udut]] 那四页的正文里**都没有提过自己的正命令**）。

- [[dfps]] —— **正向命令：那页定义，本页撤掉。** `DFPS` 定 DPS 通道与极性、
  **并且定下 gang 配置**，所以本页撤 pin 时才会连带把 gang 解掉。
  **⚠️ 本页没读 `DFPS` 的 raw**——
  本页对它的了解只有本篇这一句 `previously been defined by DFPS, DFPS? - (DeFine Power Supply)`。
- [[ganging]] —— **本页唯一那句副作用的落点**。**注意用词**：本篇原文写的是
  `The gang (master/slave) configuration`（**`gang`，不是 `ganging`**），
  而 wiki 里那个概念页叫 [[ganging]]。**「`resolved` 之后 master/slave 各变成什么状态」本页没有**。
- [[udef]] —— **同族另一支的撤销命令**（`UnDEFine pin`，撤 digital pin）。
  **两者最值得对照的一点**：`UDEF` 的例子担保的是
  `it assumes its former operating mode and the pin type OFF`，
  而本页担保的是 `the DPS settings are immediately restored`——
  **一个撤完变成 `OFF`，一个撤完设置原样回来，机制不同，别互相套。**
  **`UDEF` 在本篇原文里 0 命中**（实测），**本页没读 `UDEF` 的 raw**。
- [[dps-pins-editor]] / [[dps-task]] / [[dpspins-resources]] —— **DPS 那一侧的相邻页**
  （GUI 编辑器、DPS 任务、资源）。**`UDPS` 在本篇里没有提到它们**；
  这几条关系来自它们各自的对象域，**本页没读它们**。
- [[udpr]] / [[udpt]] / [[udup]] / [[udut]] / [[udvp]] —— **同一族的另外五页**，见上表。
- [[pin]] / [[command-reference]] —— **归属**：本篇在 `02.06_Command_Reference` 下，
  而 `## Application` 指向 `Pin configuration, see Configuration Setup Commands.`。
  （§6：`stage` 填的是**最近的一段**，不是归属。）
- [[pin-config-locked-during-test]] —— **适用于本命令的那条锁**（见「典型用法」）。

### 一个本篇正文里完全没有、但别的文档明确点名的后果：DSL 授权锁

`02.04.05.08.02_Disabling_a_pin_configuration_license_lock.md`（**本篇没在 `sources:` 里，本页另读了它**）
把 `UDPS` 列进**能解除「pin configuration license lock」的命令**里，逐字（放在代码块里，
免得本页的引号把那个 `*` 吃成斜体）：

```
Several firmware commands can disable a device specific license lock, in other words, disable a pin configuration file. These firmware commands are *RST (ReSeT), UDAN (UnDefine ANalog pin), UDEF (UnDEFine pin), UDPS (Undefine DPS pin), UDUP (UnDefine Utility Purpose), and UDUT (UnDefine UTility line).
```

**即：跑一条 `UDPS`，会把 pin 配置文件的 device-specific license 签名作废。**
那一篇接着写（逐字）：

> 「The device-specific-license signature is no longer valid, the pin configuration file is
> unlocked, and the pin configuration related commands are enabled again.」

**「作废签名」既可以是想要的、也可以是事故**——那一篇的标题是
`Disabling a pin configuration license lock`（**讲的是「故意去解锁」这个用法**），**⚠️ 但本页的 `UDPS` 原文一个字都没提这件事**，
**所以「在带锁的配置上随手发一条 `UDPS` 会有什么后果」本篇答不了。**

**这一条对本族里另外两页同样成立**：那份名单里还有 `UDUP` 与 `UDUT`
（见 [[udup]] / [[udut]]）。**`UDPR` / `UDPT` / `UDVP` 不在这份名单里**（本页核过）。

> **本页的 `（推断）` 只有两处**：语法里 `{}` 与 `()` 的分工、「数据留住但 gang 解掉」那句合读。
> 其余每条都能指到本篇原句，或上面那两篇被声明的文档的原行。

## 版本

`## Functional changes` 段有，**只有一条，逐字**：

```
- Introduced before SmarTest 6.3.2
```

**按 §11.2 ②，这不是「6.3.2 的变更记录」，是一个哨兵值。**
全语料那 2,677 条同款写法（`Introduced before …`）的意思是
「**在本文档集覆盖范围开始之前就已经有了**」——
**照字面读会生成一条「6.3.2 新增了 `UDPS`」的假信息，而且格式齐整。**

**所以：`UDPS` 究竟成立于哪个版本，这份语料里没有。**
本页只能记「**至少早于 6.3.2 的覆盖起点**」，**不能记成「6.3.2 引入」。**

**与同族的对照**：`UDPR` 拿到的是**真版本号**（`Introduced in SmarTest 6.5.2`），
`UDVP` 拿到的也是真版本号（`Introduced in SmarTest 7.10.0`），
而**本页与 [[udpt]] / [[udup]] / [[udut]] 拿到的都是哨兵值**。
**这不是本页的缺陷，是三篇文档各自的写法。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**而本篇的版本段一条变更都没有**——**所以「6.3.2 之后 `UDPS` 有没有变过」语料里答不了。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.md`
（TDC `98823.htm`；**md 1,207 字节 / 42 行**，上游 htm 3,060 字节）。**整篇读完——本篇只有 42 行。**

**另外读了三篇 raw 全文 + 一篇 raw 的一句（本页 `sources:` 之外，逐条声明）：**

| 篇 | 为什么读 | 字节 / 行数 |
|---|---|---|
| `02.06.03_Pin_configuration_setup_commands.md`（TDC `10649.htm`） | **本篇 `## Application` 唯一指向的那一篇**；族的分组表与章首 Note 都在这里 | 3,305 B / 41 行 |
| `02.06.03.01.01_Introduction.md`（TDC `10650.htm`） | **同一张分组表在它里面也有一份**（用于判断那是「重复投放」还是「各写一遍」，§10 的判据） | 3,061 B / 37 行 |
| `02.04_Model_File_and_Licensing/02.04.05.08.02_Disabling_a_pin_configuration_license_lock.md`（TDC `114540.htm`） | **它是 `UDPS` 的一条入边**，而且给出一条本篇完全没写的后果（DSL 授权锁） | 3,831 B / 41 行 |
| `02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md`（TDC `98821.htm`）**——只核了「是什么」里那句对照引文，没有通读** | 「本页担保 level 数据留住、`UDEF` 担保 mode 留住」这条对照，**回 raw 核过 `it assumes its former operating mode and the pin type OFF` 那一句** | **1,209 B / 46 行（本页未通读）** |

**还读了三篇 wiki 页（不是 raw）**：`wiki/objects/udef.md`（对照同族担保的差别）、
`wiki/constraints/pin-config-locked-during-test.md`、
`wiki/constraints/pin-config-requires-sequencer-off.md`（核对「哪条锁适用于本命令」）。

**本页没做的**：

- **`DFPS` 的 raw 没读。** 所以「DPS 通道怎么定义、极性怎么写、gang 怎么指派」**本页一个字没有**；
  本页对 `DFPS` 的了解只有本篇那一句链接名。
- **`ganging` 的原文没读。** `resolved` 之后主从两侧各处于什么状态，**本页答不了**。
- **`UDEF` 的 raw 没读**——上面那条对照里的 `UDEF` 引文来自 [[udef]] 那一页本身。
- **`DPS pins editor` / `DPS task` / `DPS pins resources` 没读**——
  它们在 `related` 里是**按对象域相邻**列的，**不是本篇的文档事实**。
- **`Pin Configuration Example` 没读**——索引末尾指向它。
- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4）。
- **没有实跑。** 没在机台上发过 `UDPS`、没解过 gang、没验证过
  「换个名字重新定义是否真能拿回 DPS 设置」，**更没在多 site 或带 DSL 锁的配置上试过**。
  `verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。
- **没有动 `wiki/index.md`**。

> ⚠️ **本篇的语料瑕疵与结构上要注意的地方，本页照实记下、一处都没替它改**（§11.2）。
> **本篇 md 的 CJK 字符数实测为 0**——**没有 §11.2 ① 那一族编码乱码。**
>
> **① `## Parameters` 那张表在 raw 里被压平。** 逐字（本篇 `## Parameters` 起头那一段的原文）：
>
> ```
> ## Parameters
>
>  |
>
> pinlist
>
>  |
> ```
>
> ——**一格一行、中间夹着孤立的 ` | `**（同族的 [[udpr]] / [[udup]] / [[udut]] / [[udvp]] 同一形态）。
> **说明文字一个字没丢**，但**本篇 raw 里没有 `Parameter` / `Description` 之类的表头行**——
> **所以「哪一列是什么」是从位置读出来的，不是原文写的。**
> **⚠️ 上游 `.htm` 里这张表是完整的**：`raw/98823.htm` 里写着
> `<table class="frame-topbot">`，里面是 `<colgroup><col><col></colgroup>`，
> `<tr>` 里两个 `<td>`。
> **所以「压平」是转换侧的产物，不是上游就坏的**（§11.2 ⑥ 的判法：回 `.htm` 核）。
>
> **② 第一句里有一个多余的逗号（逗号拼接）。** 逐字：
> `removes any specified DPS pins from your current setup, that have previously been defined by DFPS, DFPS? - (DeFine Power Supply).`
> ——`your current setup` 后面那个逗号把限定性的 `that` 从句切了出去。
> **上游 `raw/98823.htm` 里这个逗号也在**（转换没动它）。**本页照原样引，不替它删。**
>
> **③ 同一个说法在本族里介词不一致。** 本篇逐字是
> `the names must be separated with a comma.`，
> 而 [[udup]] / [[udut]] 逐字是 `the names must be separated by a comma.`
> ——**同一个句型，一个 `with` 一个 `by`**。**本页各照各的引，不替它统一。**
>
> **④ 本篇原文没有 `## Errors`，也没有 `## Warnings`**（已核，本篇 md 与上游 htm 里各 0 命中）。
> **注意上面「报错条件」那一节在本页是不存在的**——**这不是脚本漏抽，是 raw 里没有这一节**
> （对照 [[udpr]] / [[udup]] / [[udut]] / [[udvp]]：那四页有）。
>
> **⑤ 本篇在语料里有**两份**投放，正文逐行完全相同。**
> 另一份是 `02.06_Command_Reference/02.06.03.02.26_UDPS_-__Undefine_DPS_pin.md`
> （`source_topic: "98823_2.htm"`，**1,208 字节**）。
> **实测 `diff`：两份的差别只有 frontmatter 的第 3、4 行**（`source_topic` / `source_html`），
> 那 1 字节的差就是 `98823` → `98823_2`。**两份上游也各有一个 `.htm`，
> 而且 `cmp` 报 `98823.htm` 与 `98823_2.htm` 完全一致**（都是 3,060 字节）——
> **所以这是上游 TDC 就有的重复投放，不是转换产生的**（§11.2 ⑥ 的判法）。
> **本页的 `sources:` 用的是 `02.06.02.02.298` 那一份**；
> **另一份的内容本页没有另读一遍**（因为实测正文逐行相同）。
>
> **⑥ 那份 DSL 文档里，正文点名的命令比它自己的操作步骤多一个。**
> 那一篇的 CAUTION 点名 `*RST` / `UDAN` / `UDEF` / `UDPS` / `UDUP` / `UDUT` **六个**，
> 而它 `## Procedure` 的列表里**只有五个链接**（`*RST`、`UDEF`、`UDPS`、`UDUP`、`UDUT`——
> **漏了 `UDAN`**），而且列表里还挂着一个**空的列表项**（逐字就是一个光秃秃的 `-`）。
> **这不是本页的引用错误，是那一篇 raw 如此。**

`verified: doc-only`
