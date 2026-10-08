---
type: object
title: JSPR, JSPR? - (Jitter Set PRimary set)
layer: L1
stage: timing
tags: [timing, jitter, jitter-injection, jspr, primary-set, l1-command, firmware-command]
related: [jsdf, jscf, timing, pin]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# JSPR, JSPR? - (Jitter Set PRimary set)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **286 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### JSPR

```
JSPR {"js_set_name"|""}
```

### JSPR?

```
JSPR?
```

returns:

```
JSPR {"js_set_name"|""}
```

### Parameters

| js_set_name | Specifies the name of an existing jitter set. Specify an empty string to inactivate the current primary set and thus to disable jitter injection. |
|---|---|

### Example

```
> JSPR   "js_set1"
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if no jitter set with the specified name exists.

<!-- 报错节 end -->

## 是什么

**JSPR 是 jitter 这一族的「开关」命令——它指定哪个 jitter set 是 primary，而 primary 是真正会被用到的那一个。**

> 「JSPR defines the primary jitter set. Note that
>
> - if a primary jitter set is defined, then it will automatically be used in the test, and
> - the primary jitter set (as defined with JSPR) must be associated with the same context as the other primary sets.」

**这两条 bullet 就是全部机制**，一条不差：

| bullet | 说的是什么 | 本页能补的 |
|---|---|---|
| **第一条** | **有 primary 就自动用**——不需要在 testflow 里再指一次 | **「自动」到什么程度、和 site / pin 什么关系，原文没说**（语料未写） |
| **第二条** | **context 必须和其他 primary set 一致** | **不一致会怎样，原文没说**（语料未写，§10 不替它补） |

> **第二条 bullet 的主语是「primary jitter set」，比较对象是 `the other primary sets`**——
> 这句话意味着**系统里 primary set 不止 jitter 一种**。
> **原文没有展开「还有哪些 primary set」**，本页也不推测。

**三条命令的分工，一句话说清：**

| 命令 | 干什么 | 本页/别页 |
|---|---|---|
| `[[jsdf]]` | 登记一个名字（**不含内容**） | 别页 |
| `[[jscf]]` | 往这个名字里写波形、幅度、`MODE` | 别页 |
| **`JSPR`** | **指定哪一个名字是 primary —— 即「真正生效的那一个」** | **本页** |

**写在 `[[jsdf]]` / `[[jscf]]` 里的东西，只要不是 primary，原文没有说它会被使用。**
（依据是第一条 bullet 的措辞 **`if a primary jitter set is defined, then it will automatically be used`**
——**它把「被使用」这件事挂在 primary 上**。**这是推断：原文没有明写「非 primary 的不生效」**。）

### 关掉抖动的唯一办法：`JSPR ""`

参数表里这一句是全页最有用的一句：

> 「Specifies the name of an existing jitter set. Specify an empty string to inactivate the current
> primary set and thus to disable jitter injection.」

**即：把一个空字符串交给 `JSPR`，就取消了当前 primary，抖动随之关闭。**
**这是本篇给出的唯一一个「关」的动作**——**原文没有别的关闭方式**。

| 想要 | 怎么写 |
|---|---|
| **启用某个 set** | `JSPR "<name>"` —— **名字必须已存在**，否则报错 |
| **关掉抖动** | `JSPR ""` |
| **看现在是哪个** | `JSPR?` |

### 写与查

| 形式 | 原文 |
|---|---|
| `JSPR` | `JSPR defines the primary jitter set.` |
| `JSPR?` | `JSPR? returns the current primary jitter set.` |

**`JSPR?` 不带任何参数**——它的语法行就是光秃秃的 `JSPR?`
（**与 `[[jsdf]]` / `[[jscf]]` 的查询不同，那两个要写名字或 `ALL`**）。

### 语法（**这一节脚本没抽**，见 `## 出处`）

原文的语法块写在 `## JSPR` / `## JSPR?` 两个标题下
（**这两个标题拼写是正确的**），**没有 `Syntax` / `Parameters` 这类段标记，脚本一个字都没收**。原文逐字是：

```text
JSPR {"js_set_name"|""}
JSPR?
```

回复的格式是：

```text
JSPR {"js_set_name"|""}
```

**回复的格式里也留着 `|""`**——**也就是说「当前没有 primary」是可以用空字符串回答的一个合法状态**
（推断，依据是回复格式与写入格式逐字相同，而 `""` 在写入侧的含义是「取消 primary」）。

## 典型用法

**1. 整族的顺序**（**本页只负责最后一环；前两环的出处见 `## 和谁有关`**）：

```text
JSDF "js_set1"                    ← 登记名字
JSCF "js_set1",MODE,CONT,(Pin1)   ← 写内容
JSPR "js_set1"                    ← 指定为 primary（生效）
```

**2. 最小示例（`## Example` 全文就一行）：**

```text
> JSPR   "js_set1"
```

**注意名字两边的三个空格**——**`> JSPR   "js_set1"` 里 `JSPR` 与引号之间是三个空格**，
和 `[[jsdf]]` 那篇的示例（`> JSDF   "js_set1"`）格式一致。
**这是语料自己的排版习惯（对齐用），不是语法要求**（推断：语法行写的是 `JSPR {"js_set_name"|""}`，
**里面有空格但那是有意的可读性间隔**；**原文没有说空格数有语义**）。

**3. 关掉抖动的写法**：`JSPR ""` —— **注意是空字符串，不是省略参数**。
`JSPR?` 的语法里没有参数，**所以「不带名字」不是「取消」，而是「查询」。**
**这两件事在命令形式上必须分开：写 `JSPR` 后面带东西，查 `JSPR?` 后面不带东西。**

**4. 两个会咬人的前提：**

| 前提 | 原文 | 不满足会怎样 |
|---|---|---|
| **名字必须已存在** | `Specifies the name of an existing jitter set.` | `An error is generated if no jitter set with the specified name exists.` |
| **context 要和其他 primary set 一致** | 见上面第二条 bullet | **原文没说会怎样**（语料未写） |

## 和谁有关

**同族命令（`02.06.02.02.14x` 这一段是 jitter set 家族）**：

- [[jsdf]] — **上游**。`JSPR` 要的那个「已存在的 jitter set」就是 `[[jsdf]]` 登记的。
  **本页这一篇没有点名 `JSDF`**（**它只点名了 `JSPR` 自己**）——
  **这条关系是照命令分工写的，不是本页读到的**，故这里用「上游」而不断言语法依赖。
- [[jscf]] — **并列的上游**。`JSPR` 选中的那个 set，**它的内容（波形 / 幅度 / `MODE`）写在 `[[jscf]]` 里**。
  **本页这一篇一个字都没提 `JSCF`**——**所以「先 JSCF 再 JSPR」这个顺序不是本页说的。**
  （**`[[jscf]]` / `[[jsdf]]` 那两篇里也没有这条顺序**，见那两页的 `## 出处`。）
- [[jsud]] / [[jswf]] / [[psfc]] — **本页这一篇一个字都没提它们**，
  **名字是从 allowlist 得知的**，**故本页不写任何关系。**

**同 stage 的页**：

- [[timing]] — 本页 `stage: timing` 的理由：**jitter 注入是加在 timing 的 edge delay 上的配置**
  （**这条证据在 `[[jscf]]` 那一篇里，不在本页**）。
  **本页这一篇里连 `timing` 这个词都没出现**——**本页的 stage 判定据的是命令域（`02.06.02` 命令参考里 jitter 归 timing），
  这是推断，不是本页读到的。**
- [[pin]] — **本页 `stage` 不是 `pin` 的理由**：**`JSPR` 的语法里连 `pinlist` 都没有**
  （**对比 `[[jscf]]` 的四个参数里有 `pinlist`**）——**primary 是全局的一个选择，不分 pin。**

**本页正文点名、但没有页、故不链的东西**：

- **`the other primary sets`** —— 上面第二条 bullet 里那个比较对象。
  **它不是一篇文档，是原文里的一个概念**；**原文没有说它指哪些东西**，
  **本页也不给一个「就是 level / timing 的那些」之类的好听的答案**（§11：不臆造）。

## 版本

**本文档有 `## Functional changes` 段**，一条：

- **Introduced in SmarTest 7.0.1** — **`JSPR` 是 7.0.1 引进的**。
  **没有别的变更条目**——**也就是说 7.0.1 之后 `JSPR` 的语法与参数没有再动过**
  （**这是对本文档这一节的读法**：`## Functional changes` 里只有一条。
  **「没写」和「没动」本页分得清：本节确实只有一行**）。

> **和 `[[jsdf]]` / `[[jscf]]` 对一下**：那两篇各有 2 条和 4 条版本条目
> （**`[[jsdf]]` 在 7.3.0 加了 `mode_context`；`[[jscf]]` 在 7.1.1 / 7.3.0 / 7.3.1 各动过一次**）。
> **`JSPR` 在这一族里是唯一一个从 7.0.1 起一个字没改的命令。**
> —— **这一句的对照依据是那两页的 `## 版本` 节，本页只是并列，不做推断。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.md`
（TDC `117945.htm`，54 行）

**本页没做的**：

- **`[[jsdf]]` / `[[jscf]]` 的文档本页没读。**
  **所以「整族怎么串起来」在本页只有命令分工那一张表**，
  **而那张表里的三行有两行是从别页的页名和参数描写推出来的**——
  **凡是不出自本页这一篇的句子，本页都标了「不在本页」。**
- **`Mode contexts` 那一篇没读**（**本页这一篇甚至没有给出它的 raw 路径**——
  它只写了 `the same context as the other primary sets`，**没有链接**）。
  **后果：第二条 bullet 那条约束本页只能原样转述，既不知道 context 是什么，
  也不知道「哪些 primary set」要一致。**
- **没有 `## Procedure` / `## Before you begin` 可读**——本篇只有
  `## Application` / `## Errors` / `## Example` / `## Functional changes` 四节。
  **所以「典型用法」是照语法、参数表和那一条 bullet 拼的。**
- **零张图。** 本篇没有图片引用。
- **`## Application` 全文只有两个词**（`Jitter test.`）——**本页不为它编内容。**
- **没有在任何真实机台上跑过 `JSPR`**（`verified: doc-only`）。
  **`JSPR ""` 是不是真的把抖动关了、`JSPR?` 在没有 primary 时返回什么，
  本页只能保证「文档这么写」（§11）。**
- **加粗声明**：本页 `## 是什么` 里那两段代码块（`JSPR {...}` / `JSPR?`）
  **是脚本没有收、由本页手抄进来的**——**逐字取自原文，但不在「语法 / 参数」节里**，
  **所以下次 `--refresh-syntax` 不会碰它，第七类也不会替它把关**。**核对请回 raw 第 17–32 行。**

> ⚠️ **本篇的语料瑕疵**：**本页在 `02.06.02.02.149` 这一篇里没有发现坏字、
> 没有发现拼错的标题、没有发现自相矛盾的两句**（`JSPR` / `JSPR?` 两个 H2 标题拼写正确，
> 引号是全角直引号，ASCII 之外只有正文里的普通英文引号）。
> **⚠️ 但这是「本页读到的」，不是「本篇干净」**（§13.1 第 ⑥′：
> **一条检查绿，可能是因为它根本没查到东西**）。
> **本页这一篇只有 62 行、无图、无表格**，**能出瑕疵的面积本身就小**——
> **把「没发现」写成「没有」，正是这一系列教训里反复出现的那一步。**

`verified: doc-only`
