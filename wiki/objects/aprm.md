---
type: object
title: APRM - (Activate PRiMary sets)
layer: L1
stage: level
tags: [aprm, l1, firmware-command, level, primary-set, frontend, sprm, sqst]
related: [sprm, sqst, level, mapping-level, primary-status, command-reference, dc-test-programming, spec-value, spec-variable, conf, xps256-status-flags]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# APRM - (Activate PRiMary sets)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **459 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
APRM {mode}
```

### Parameters

| mode | Selects the activation mode: | Selects the activation mode: |
|---|---|---|
| mode | FRC | Forced activation. Primary sets are always activated. |
| mode | CNL | Conditional activation, depends on previous activation performed by APRM or by any of the commands in the second list above. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98485_2.htm`。

### Example

```
APRM CNL
```

<!-- 语法节 end -->

## 是什么

**`APRM` 是「把 primary set 激活到硬件」的那条 L1 固件命令。** 原文第一句就是全部机制：

> 「The APRM command activates primary sets in the hardware which were made known to the firmware
> by the SPRM (Set PRiMary sets).」

**这一句把「登记」和「激活」分成两条命令**：让固件知道那组 primary 的是 `SPRM`，
把它推到硬件的是 `APRM`。**`made known to the firmware` 说的是「已经登记过」**——
所以 `APRM` 自己不去找 primary，它只是把**固件已经知道的那一组**送进硬件。

**标题里的 `PRiMary` 不是本页打错的**——原文的标题就写作 `APRM - (Activate PRiMary sets)`，
命令名本身是 `APRM` 四个大写字母（§11：命令大小写敏感，原样保留）。

### 四条命令「自己就会做这件事」（**这一节不在上面的语法节里**）

**`## Mode of operation` 那一节没有被脚本收进「语法 / 参数」**（语法节只有 `Syntax` / `Parameters` / `Example` 三节），
**它是本页从 raw 逐字抄的**：

> 「The following commands do not require a prior execution of APRM, since they themselves perform
> this function:」

| 命令 | 原文注解 |
|---|---|
| `FTST?` | `- (Functional TeST)` |
| `RCLS?` | `- (ReCeive Level Sensitivity)` |
| **`SQST` RUN** | `- (SeQuencer STate)` |
| `PSST` | `- (Power Supply STatus)` |

**这张表是本页最值钱的一条**：这四条**跑起来就顺带完成了激活**，
所以「忘了先发 `APRM`」在这四条上不会出问题。

**两个细节要照实说**：

- **`SQST` 那一行原文连写成 `SQST RUN`**——**只有 `RUN` 这个形态在表上**，
  原文没有说 `SQST` 的其他参数形态算不算（**推断**：不算，因为表里点名的是 `SQST RUN` 而不是 `SQST`；
  **原文没有这句话**）。
- **`FTST?` 与 `RCLS?` 带问号、`PSST` 不带**——**原文的写法如此，本页照抄**。
  **`SQST` 那一行是唯一一个带参数的**。

### 两个 mode 的差别

**两条正文都在上面的「语法 / 参数」节里**（那一节的 `## Parameters` 表）。它们的语义差别一句话：

| mode | 原文 | 读法 |
|---|---|---|
| `FRC` | `Forced activation. Primary sets are always activated.` | **无条件激活**——不看上次做过什么 |
| `CNL` | `Conditional activation, depends on previous activation performed by APRM or by any of the commands in the second list above.` | **有条件激活**——看上一步有没有激活过 |

**⚠️ `CNL` 那句里的 `the second list above` 指的那张表不在本文档里。**
本文档正文里只有**一张**清单（上面那四条）。**本页并列记下，不替它补一张表**（见「出处」⚠️①）。

### 适用范围

同一节的 `## Application` 也**不在语法节里**，原文只有一行：

> 「AC tests and DC Measurement Commands.」

**即：原文把这个命令的适用范围写成两样**——AC 测试，以及 `DC Measurement Commands`
（`02.06.10` 那一章，**本页没读**）。

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`**——
定义文档只有 43 行，`## Example` 一节只有一行。**能读出的顺序只有三条**：

| # | 做什么 | 依据 |
|---|---|---|
| 1 | **先让固件知道 primary set**（`SPRM`） | 原文第一句的 `made known to the firmware by the SPRM` |
| 2 | **再激活，并选一个 mode** | `## Example` 逐字是 `APRM CNL` |
| 3 | **或者不做第 2 步**——四条命令自带这个功能 | `## Mode of operation` 那张清单 |

**第 2 步的 mode 怎么选**：原文只给了那两句定义（见上表），**没有给「什么场合用哪个」的判据**，
也没有说选错了会怎样。**（推断）**：`CNL` 是「只有在之前激活过的情况下才激活」，
所以它的用途当是「避免重复激活」；**依据只有 `depends on previous activation` 这半句，
原文没有举任何例子。**

**一条 wiki 内部的用法**（**不在本页 `sources:` 里**，本页没读那张表引的文档）：
[[mapping-level]] 主表「把 primary 激活到硬件（frontend）」那一行把这件事分到五格，
其中 **GUI 格写的是「Firmware view 里敲 `APRM`」、L1 格写的是 [[sprm]] 与本页**
——**即：那张表把本页当成「手动敲命令」这条路的落点**。
同一页另引一篇 Spec Tool 的文档说明**改完 spec 值不会自动刷新 frontend**，
出路是 `or invoke the FW command APRM in the Firmware view tab.`
——**那一篇不在本页 sources 里，本页只转述 [[mapping-level]] 的结论，没有自己去读它。**

## 和谁有关

- [[sprm]]（**未建**；raw: `02.06.02.02.228_SPRM__SPRM__-__Set_PRiMary_sets.md`）— **本页唯一的前置命令**。
  原文点名：要给硬件激活的那组 primary，就是它「made known to the firmware」的。
  **那篇本页没读**，所以它的参数与时机本页一个字没有。
- [[sqst]] — **「自带 APRM」四条里的一条**（原文写作 `SQST RUN`）。
  [[sqst]] 那页讲的是「控制一组 sequencer 的状态」，**它的 `RUN` 这个参数正是原文点名的那个形态**。
- `PSST`（**未建**；raw: `02.06.02.02.198_PSST__PSST__-__Power_Supply_STatus.md`）—
  同清单上的一条。
- `FTST?`（**未建**；raw: `02.06.02.02.127_FTST__-__Functional_TeST.md`）、
  `RCLS?`（**未建**；raw: `02.06.02.02.203_RCLS__-__ReCeive_Level_Sensitivity.md`）—
  同清单上的另外两条。**四个名字都只在这张表上出现过，本页没有一篇它们自己的文档。**
- [[mapping-level]] / [[level]] — **本页 `stage: level` 的理由**：那张对照表把本页放在
  「把 primary 激活到硬件（frontend）」那一行，与 [[sprm]] 同格。
- [[primary-status]] — **L2 侧的对应物**：`PRIMARY_STATUS` 是 digital primary 的**定义容器**，
  改的是容器里的定义；本页做的是把这些定义**推到硬件**。
  **那页本页没读**，「推到硬件」这层关系是**按 [[mapping-level]] 的行位**说的（**推断**）。
- `DC Measurement Commands`（**未建**；raw: `02.06.10_DC_Measurement_Commands.md`）—
  原文 `## Application` 点名的另一半适用范围。
- [[dc-test-programming]] / [[command-reference]] — **主题上最近的 wiki 页**：
  前者讲 DC 测试这一类怎么组织，后者是 `02.06` 整章（L1 固件命令字典）的入口。
  **原文没有链到这两页中的任何一页**，这里的两条关系是**按章与主题**说的（**推断**）。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- **`Introduced before SmarTest 6.3.2`**

> **这一条是 §11.2② 的哨兵值，不是「6.3.2 新增了 APRM」。**
> 它写的是 `before`——意思是「**在本文档集覆盖范围开始之前就已经有了**」。
> **照字面读会凭空造出一条「SmarTest 6.3.2 新增了 `APRM`」的假信息，而且格式齐整。**
> **对照着看**：同一批建的 [[spec-value]] 与 [[spec-variable]] 两篇写的是 `Introduced in`
> 加一个真版本号——**那才是真版本号**。**两个句式只差一个词（`in` / `before`），读法完全相反。**

**原文没有给任何后续变更条目**——所以「`APRM` 的 mode、适用范围在 6.3.2 之后改过没有」
本页没有依据。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.md`
（TDC `98485_2.htm`，1,705 字节 / 43 行）——**整篇读完**。

**「语法 / 参数」节收了 `## Syntax` / `## Parameters` / `## Example` 三节**（278 字符）。
**`## Mode of operation`（481 字符）、`## Application`（93 字符）与开头那段导语都不在里面**——
**所以本页正文里那张四条命令的清单、以及适用范围那半句，是本页从 raw 逐字抄的，
不是我从语法节复制的，也不构成「改语法节」。**

**⚠️ 这一篇在语料里有四次投放，本页的 `sources:` 只列了其中一个。**
按 §10 的第 0 步查过（**比对方法与披露见「本页没做的」第二条**）：

| raw 路径 | `source_topic` | 正文 |
|---|---|---|
| `02.06.02.02.03_APRM_-__Activate_PRiMary_sets.md` | `98485.htm` | 与下面一份**逐字节相同** |
| `02.06.05.02.01_APRM_-__Activate_PRiMary_sets.md`（**本页出处**） | `98485_2.htm` | —— |
| `02.06.06.02.01_APRM_-__Activate_PRiMary_sets.md` | `98485_3.htm` | 与上面一份**逐字节相同** |
| `02.08.04.34.02.02.01_APRM_-__Activate_PRiMary_sets.md` | `98485_4.htm` | **不同**——差异**只在内部链接的相对路径**（多一层 `../02.06_Command_Reference/`） |

**按 §10，这是「同一篇页被投放了四次」，不是四篇文档**——
**引用本页时不要把它们当成四条独立来源**；这一条对 [[mapping-level]] 那张表尤其要紧
（它按 `edges.jsonl` 数链接，同一篇的每一份投放都是一条独立的边源）。

**本页没做的**：

- **只读了这一篇的正文。**
- **一处例外，要明确交代**：为做 §10 的**第 0 步（先查是不是同一篇被投放了两次）**，
  本页比对过另外三条路径（见上面那张表）
  ——**只比对了字节数、首 5 行 frontmatter 与「去掉 frontmatter 后的正文 diff」，
  没有读它们的正文当依据。** 结果：三条里两条与本篇**正文逐字节相同**，
  第三条（`02.08.04.34.02.02.01`）**只差内部链接的相对路径**。
- **`SPRM` 那篇没读**——**「先登记、再激活」这条链的前半段本页只有原文那一句话的依据**：
  参数是什么、什么时候必须发、`APRM` 之前还有没有别的步骤，本页都没有。
- **「自带 APRM」那四条一篇没读**（`FTST?` / `RCLS?` / `SQST` / `PSST`）——
  **本页只知道它们在这张表上**，**不知道它们各在哪一步、哪个参数形态下做这件事**。
  （[[sqst]] 那页是别的批次建的，**本页没有拿它的正文当依据**。）
- **`DC Measurement Commands`（`02.06.10`）没读**——`## Application` 那半句的落点本页没有。
- **`02.06.05.02` 那一族的父级文档没读**——见下 ⚠️①，那句 `the second list above` 的「第一张表」
  应当在别处，**本页没有去找它在哪儿**。
- **`02.06.05.02_List_of_level_setup_commands`（`02.06.05.02`）没读**——
  **所以「`APRM` 在那一族命令里的位置」本页没有。**
- **图：0 张，因为这一篇一张图都没有。** 实测该篇对 `raw/` 的图片引用 **0 处**
  （`grep -o 'raw/[0-9]*\.\(png\|jpg\)'` 零命中），**上游 `raw/98485_2.htm`（4,789 字节）里也没有一个 `<img>`**
  ——**这不是「图够不着」，是这一篇本来就不带图**。
  所以本页**没有任何来自图的结论**，也没有一处需要标「④ 图证」。
- **语料瑕疵查过、结果为零**：本篇用 `[一-鿿]` 实测 **0 命中**（不是 §11.2① 那一族坏字），
  `DC/DC power units`（§11.2⑤ 那个整词替换）实测 **0 命中**。
  **这不是「没找」，是查过。**
- **没有实跑**：没有在 Firmware view 里敲过 `APRM`、没有验过 `CNL` 在什么情况下真的不激活、
  也没有验过 `SQST RUN` 是不是真的会自动激活。
  **`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按本批分工，避免抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[level]] / [[command-reference]] 两页。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**：
>
> ① **`CNL` 那句里的 `the second list above` 在本文档里找不到落点。** 原文：
>    `Conditional activation, depends on previous activation performed by APRM or by any of the commands in the second list above.`
>    **本文档正文里只有一张清单**（`## Mode of operation` 那四条），**没有「第一张」**。
>    **（推断）**：这句话是从更大的上下文里带过来的（本篇属 `02.06.05.02` 那一族 level setup 命令页，
>    「第一张」应当是那一族命令的清单）；**依据只有「本文档只列了一张表」这一个事实，
>    原文没有解释，本页不替它补一张。**
>
> ② **`## Parameters` 那张表在 raw 里是三行「前面带一个空格」的表格行**：
>    每行以空格 + `|` 开头，**而且整张表没有 delimiter 行**——
>    **所以它在 md 里不是一个合法表格**。**这是 raw 的表格被拆散**，
>    同 [[conf]] 记的 `DC` 那一行、[[xps256-status-flags]] 记的那种现象。
>    **那一节在「语法 / 参数」里逐字保留着，本页一个字没动。**
>
> ③ **标题里的 `PRiMary` 是原文的写法**（`APRM - (Activate PRiMary sets)`），
>    不是本页的大小写错误；**本页照原样保留**（§11：命令大小写敏感）。
>
> ④ **同一篇文档在语料里有四次投放，本页 frontmatter 只列了一个。**
>    四条路径、四个 `source_topic`（`98485.htm` / `_2` / `_3` / `_4`）与正文比对结果见「出处」那张表。
>    **按 §10，这是一篇页的四个投放，不是四篇文档**——**引用本页时不要把它们当成四条独立来源**
>    （尤其别拿 `edges.jsonl` 里同一篇的几个投放去凑「有多少文档链到了 APRM」）。

`verified: doc-only`
