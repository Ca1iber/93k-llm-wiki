---
type: object
title: JSDF, JSDF? - (Jitter Set DeFinition)
layer: L1
stage: timing
tags: [timing, jitter, jitter-set, jsdf, l1-command, firmware-command, mode-context]
related: [jscf, jspr, timing, pin]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# JSDF, JSDF? - (Jitter Set DeFinition)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **428 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117922.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：js_set_name | In the command, this is the name of a new jitter set. In the query, it is a name of an existing jitter set. If you omit this parameter in the quer…

### Example

```
> JSDF   "js_set1"
> JSDF   "js_set2"
> JSDF   "js_set3"

> JSDF?
< JSDF   "js_set1"
< JSDF   "js_set2"
< JSDF   "js_set3"

```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if a jitter set with the specified name already exists.

<!-- 报错节 end -->

## 是什么

**JSDF 是 jitter set 的「上户口」命令——它只干一件事：给一个抖动配置起个名字。**

> 「JSDF creates a jitter set by defining a unique name for it.」

**注意它不管内容。** 抖动长什么样（波形、幅度、周期、什么时候抖）
全部是 `[[jscf]]` 的活；**JSDF 只把这个名字登记进硬件，好让后面的命令有个东西可指。**
`## Application` 一节全文就两个词：`Jitter test.`

### 三条硬性事实（**都在第一段里，一条都不长**）

| 事实 | 原文 |
|---|---|
| **硬件里最多存 128 个 jitter set** | `Up to 128 jitter sets can be stored in the hardware.` |
| **超了是 FIFO 替换，不是报错** | 「If you exceed this number by selecting a jitter set that is not yet stored in the hardware, the new set will replace the set that was downloaded first.」 |
| **重名是错误** | `An error is generated if a jitter set with the specified name already exists.` |

> **第二条值得读两遍**：它是**静默的**——不报错、不警告，
> **最早下载进去的那个 set 被顶掉**。
> **「定义 128 个以上」这件事本身不会失败，失败的是后来某次测试用的那个 set 已经不在硬件里了。**
>
> **措辞上有一处跳跃，本页照实记**：这一句的主语动作写的是 `selecting`（选择），
> 而这一段上一句写的是 `creates`（创建）——
> **「定义」和「选择」在原文里被当成同一件事在这里混用**。
> **本页不替它统一措辞，也不据此推断硬件的行为**（见 `## 出处` 的 ⚠️）。

### 与 mode context 绑定（**7.3.0 之后**）

> 「A jitter set can be associated with a user defined mode context」

`mode_context` 是语法里的第二个参数（**可选**），原文对它的说明是：

> 「The mode context with which the jitter set is associated. If this parameter is omitted, the DEFAULT context is assumed.」

**也就是说：不写 `mode_context` 就是 `DEFAULT` 上下文。**
`Mode contexts` 是什么、怎么用，**本页没读那篇，一个字都不写**（raw 路径见 `## 和谁有关`）。

**还有一条跨命令的一致性要求**，原文就写在 mode context 的下一句：

> 「The primary jitter set (as defined with JSPR) must be associated with the same context as the other primary sets.」

**这条约束的主语是「primary jitter set」，动作是 `must be associated with the same context`，
比较对象是 `the other primary sets`**——**但原文没有说违反它会怎样**（语料未写）。

### 写与查的分工

| 形式 | 干什么 | 原文 |
|---|---|---|
| `JSDF` | 新建一个 jitter set 的名字 | `In the command, this is the name of a new jitter set.` |
| `JSDF?` | 查名字 | 「JSDF? returns the names of the specified or all defined jitter sets.」 |

**`JSDF?` 的两种查法，原文给了两处说法，措辞不一样：**

| 写法 | 参数表里的原文 |
|---|---|
| **省掉名字** | `If you omit this parameter in the query, JSDF? will return the names of all user defined jitter sets.` |
| **写 `ALL`** | `With this parameter, the query returns all existing jitter sets.` |

> **一处「本页不替它调和」的地方**：一处的宾语是 **`all user defined jitter sets`**，
> 另一处是 **`all existing jitter sets`**。**两句话是不是同一件事，原文没说**（§10 第 3 步）。
> **本页把两种写法并列，不选一个当正确答案。**

### 语法（**这一节脚本没抽**，见 `## 出处`）

原文的语法块写在 `## JDSF` / `## JDSF?` 两个标题下（**标题里的拼写有错，见 `## 出处` ⚠️**），
**没有 `Syntax` / `Parameters` 这类段标记，所以脚本一个字都没收**。原文逐字是：

```text
JSDF {"js_set_name"} [, "mode_context"]
JSDF? ["js_set_name"|ALL]
```

回复的格式是：

```text
JSDF {"js_set_name"} [, "mode_context"]
```

**`mode_context` 两头都带方括号，说明它在写入和回复里都是可选的**——
**回复里带不带它，本页不知道**（原文只给了这一行格式，没给带 context 的回复示例）。

## 典型用法

**1. 顺序：先定义、后配置、再设 primary。** 三段各有各的命令，**本页只负责第一段**：

| 步 | 命令 | 干什么 |
|---|---|---|
| ① | **`JSDF "<name>"`** | 登记名字（**本页**） |
| ② | `[[jscf]] "<name>",<property>,<value>,(<pin>)` | 写波形、幅度、周期、`MODE`（**本页没读**） |
| ③ | `[[jspr]] "<name>"` | 把它设成 primary（**本页没读**） |

**②③ 的顺序不是本页说的**——`[[jscf]]` 的文档要求 set 必须先存在，
而 `[[jspr]]` 在**本页**的 mode context 那句里被点名（`as defined with JSPR`）。
**除此之外本页不声称任何顺序（§2.2：流程不写在对象页里）。**

**2. 原文的示例（`## Example`）——三写一查：**

```text
> JSDF   "js_set1"
> JSDF   "js_set2"
> JSDF   "js_set3"

> JSDF?
< JSDF   "js_set1"
< JSDF   "js_set2"
< JSDF   "js_set3"
```

**注意这个例子的回复里没有 `mode_context`**——三行回复全是 `JSDF "<name>"`。
**这与「省略就是 DEFAULT」一致，但原文没有把这一点说出来**（推断，依据是上面那条 `If this parameter is omitted, the DEFAULT context is assumed.` 加上这个例子的实际形状）。
**本页标明这是推断，不是文档事实。**

**3. 一条会咬人的前提**：**同名再定义一次就是错误**，不是覆盖。
`An error is generated if a jitter set with the specified name already exists.`
—— **所以「重新定义一遍」这条路走不通**；**要改配置走 `[[jscf]]`，要换名字得换个新名字**
（后半句是推断：原文只说重名报错，**没说怎么删除或改名**——**语料未写**）。

**4. 128 个的边界怎么用**：**能存 128 个，但没有「删除」命令的记载**（本页这一篇里没有）。
**所以超过 128 以后的替换顺序（`the set that was downloaded first`）是唯一被文档描述的淘汰机制。**
**「怎么主动腾位置」本页答不上来（语料未写）。**

## 和谁有关

**同族命令（`02.06.02.02.14x` 这一段是 jitter set 家族）**：

- [[jscf]] — **下游**。`[[jscf]]` 的文档逐字要求 `The specified jitter set must have been defined with JSDF.`，
  **所以 JSDF 是它的前置**。（**这句话出自 `jscf` 那一篇，本页只是转述它**——
  **本页自己那一篇里没有这句。**）
- [[jspr]] — **下游**。而且**本页正文亲自点名了它**两次：
  `The primary jitter set (as defined with JSPR) must be associated with the same context as the other primary sets.`
  **这是本页唯一一处跨命令的关系，且是文档事实。**
- [[jsud]] / [[jswf]] — **同族，本页没读它们的文档**。
  **这两个名字是从 allowlist 得知存在的，不是从本篇读到的**，
  **故本页不写它们和 JSDF 的分工。**
- [[psfc]] — **不是 jitter 家族**，但 `[[jscf]]` 的正文点名了它。
  **它管 site 的 setup focus**；**本页这一篇一个字都没提它**，所以本页不写它们的关系。

**同 stage / 同主题的页**：

- [[timing]] — 本页 `stage: timing` 的理由：**jitter 是加在 timing 的 edge delay 上的**
  （这句话的证据在 `[[jscf]]` 那一篇里：`offsets from the edge delays specified in the currently active timing set`）。
  **本页那一篇没有提 timing。**
- [[pin]] — **本页 `stage` 不是 `pin` 的理由**：**jitter 按 pin 生效**（`[[jscf]]` 的 `pinlist`），
  但**本页这一篇里连 `pin` 这个词都没出现**。

**本页正文点名、但没有页、故不链的去处（反引号 + raw 路径）**：

- `Mode contexts`（raw: `02.06.03.01.03.01_Mode_contexts.md`）——
  `mode_context` 那一句把它指为「看这里」。**本页没读它，
  所以「mode context 是什么、怎么建、跟别的东西怎么共存」本页一个字都没有。**
  **这是本页最大的缺口**：**7.3.0 之后 jitter set 的第二个参数全靠这一篇解释。**

## 版本

**本文档有 `## Functional changes` 段**，两条：

- **Introduced in SmarTest 7.0.1** — **JSDF 是 7.0.1 引进的**。
  **和 `[[jscf]]` / `[[jspr]]` 同为 7.0.1**（后两条出自各自那一篇，**本页只是并列，不做推断**）。
- **SmarTest 7.3.0**：`The jitter set can now be associated with a user defined mode context.`
  —— **推断**：**`mode_context` 这个参数是 7.3.0 才有的**（依据是 `can now be` 这个措辞）。
  **所以 7.3.0 之前 `JSDF` 只有一个参数**——
  **但原文没有给 7.3.0 之前的语法行，这一条是从措辞推的，本页标明是推断。**

> **和 `[[jscf]]` 对一下**：`[[jscf]]` 的版本段里也有 `SmarTest 7.3.0: The MODULATION_SETS property was added.`
> **同一个版本号、两个命令各动一处**——**这不是冲突，是两篇各记各的。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md`
（TDC `117922.htm`，63 行）

**本页没做的**：

- **`Mode contexts` 那一篇（`02.06.03.01.03.01`）没读。**
  后果：**`mode_context` 参数本页只能给到「省了就是 DEFAULT」这一句**，
  **它是什么、有哪些、和 `[[jscf]]` 有没有关系，本页一个字都没有。**
- **`[[jscf]]` / `[[jspr]]` 的文档本页没读**（虽然本页正文引了它们各一句，
  但**引的是本页这一篇里写的**，不是去读那两篇拿的）。
  **所以「定义完之后怎么配、怎么设 primary」本页没有。**
- **没有 `## Procedure` / `## Before you begin` 可读**——本篇只有
  `## Application` / `## Errors` / `## Example` / `## Functional changes` 四节，
  **所以本页的「典型用法」是照语法与示例拼的，不是照原文的步骤抄的。**
- **零张图。** 本篇没有图片引用。
- **「怎么删除 / 改名一个 jitter set」本页答不上来**：
  **本篇没有这个记载**（不是没找到——**这一篇里确实没有**；
  **但「别的篇里有没有」本页没查**，§13.1 第 ⑥′）。
- **128 这个数在真机上是不是 128**，本页不知道（`verified: doc-only`）。
- **加粗声明**：本页 `## 是什么` 里那段语法块（`JSDF {...}` / `JSDF? [...]`）
  **是脚本没有收、由本页手抄进来的**——**它逐字取自原文，但不在「语法 / 参数」节里**，
  所以**下次 `--refresh-syntax` 不会碰它，第七类也不会替它把关**。**要逐字核对请回 raw 第 16–30 行。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 两个小标题把命令名拼错了——`S` 和 `D` 换了位。** 原文第 14 行与第 20 行逐字是：
> `## JDSF` 和 `## JDSF?`
> —— **正确写法是 `JSDF` / `JSDF?`**（正文每一处、参数表、示例回复里写的都是 `JSDF`）。
> **这一处坏在两个 H2 标题里，而脚本抽语法时正好不看标题**，
> **所以它没进 wiki 的「语法 / 参数」节，只活在本页这一段记录里。**
> **代价：拿 `## JDSF` 去搜 raw 能搜到，拿 `## JSDF` 搜不到标题行。**
> **② 正文在 `creates` 与 `selecting` 之间跳了一次**（128 上限那两句）——
> **本页照抄不替它改**，见 `## 是什么` 里那条。
> **③ 本页在本篇里没有发现坏字（`鈥` / `渭` 那一类）。**
> **但这是「本页读到的」，不是「本篇没有」**（§13.1 第 ⑥′）。

`verified: doc-only`
