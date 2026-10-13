---
type: object
title: CTXT, CTXT? - (ConTeXT)
layer: L1
stage: level
tags: [pin, level, timing, mode-context, context, pin-configuration]
related: [pin, conf, constraint-level-mode-context-match, constraint-timing-mode-context-match, pin-config-requires-sequencer-off]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# CTXT, CTXT? - (ConTeXT)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **372 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CTXT

```
CTXT {action},{"name"}
```

### CTXT?

```
CTXT?ALL
```

returns:

```
CTXT {DEFINE},{"name"}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98513.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：action | Specifies the action. Possible values are:

### Example

```
> CTXT? ALL
< CTXT DEFINE,"DEFAULT"
< CTXT DEFINE,"differential"
< CTXT DEFINE,"PdrvNPrcv"
```

<!-- 语法节 end -->

## 是什么

**`CTXT`（ConTeXT）在 pin configuration 里「登记一个模式上下文的名字」。** 它的职责就这一件事，原文第一句说全了：

> The CTXT (ConTeXT) command defines or deletes the name of a mode context.

**mode context 是什么**——紧跟着的第二句是定义，也是全文最关键的一句：

> A mode context sets a type (I, O, or IO) and a mode (std or fast) for every configured pin. Use the CONF command to define these attributes for the individual pins.

**这一句把两条命令的分工划死了：**

| 命令 | 管什么 | 依据 |
|---|---|---|
| **`CTXT`** | **给上下文起名**（新建 / 删除） | 本页第一句 |
| **`CONF`** | **给每一个 pin 定 `type`（I / O / IO）与 `mode`（std / fast）** | 上面第二句的后半句 |

**换句话说，`CTXT` 建出来的是一个「空壳 + 名字」，壳里每个 pin 的取值由 `CONF` 填。**
（推断：文档把「定 type 和 mode」明确派给了 `CONF`，所以这一层不归 `CTXT`；
**文档并没有直接写「`CTXT` 不设置 pin 属性」这句话**。）

### 关键机制：新 context 是 `DEFAULT` 的**副本**

`## Mode of operation` 一节只有两句，但它决定了整套用法：

> When you define a new mode context, it is created as a copy of the actual DEFAULT context. You can change this default configuration with the CONF command.

**三个后果：**

1. **新建不是从零开始**，而是**复制当前的 `DEFAULT`**。
2. **要改它的内容，改用 `CONF`**——文档**第二次**把「改」指向 `CONF`。
3. **改的是副本，`DEFAULT` 本身不动。**（推断：原文用的是 `a copy of`，副本与原件的后续修改互不影响。**文档没有单独说明这一点。**）

> **第 1 条的措辞是 `the actual DEFAULT context`——「当前实际的那个」，不是「出厂的那个」。**
> 若 `DEFAULT` 自己被 `CONF` 改过，新 context 复制的是**改过之后的样子**。
> **这条是本页的推断**，依据是 `actual` 一词；**文档没有正面写这一层。**

### 查询侧

> The CTXT? query returns the context names that are currently defined.

**返回格式**（文档 `## CTXT?` 一节逐字给的）：

```
CTXT {DEFINE},{"name"}
```

**回复里带的动作词是 `DEFINE`**——即使是查询，返回的每行也写 `DEFINE`。
**文档没有解释这一点，本页照原样记下，不替它解释。**

### 三个 action 与一条藏在 `name` 里的批量删除

上面「语法 / 参数」节是脚本逐字抽的，这里只说**它读快了会漏掉的东西**：

| action | 文档原话 |
|---|---|
| `DEFINE` | `Defines a new mode context` |
| `DELETE` | `Deletes a mode context` |
| `ALL` | `Displays all existing mode contexts (only in the query).` |

**批量删除不在 action 表里，藏在 `name` 那一格。** 文档原句：

> The name of the mode context. If the action parameter is set to DELETE, you can also specify ALL to delete all mode contexts.

**即：`DELETE` 的时候 `name` 位可以写 `ALL`，一次删光全部 context。**
**只读 action 表会漏掉这一条**——它是 `name` 格的第二句，不是 `action` 格的取值。

**另外，action 里没有「改」。** 要改 context 的内容**只能用 `CONF`**（两处原文都这么指）。

### 例子说明什么

```
> CTXT? ALL
< CTXT DEFINE,"DEFAULT"
< CTXT DEFINE,"differential"
< CTXT DEFINE,"PdrvNPrcv"
```

**`DEFAULT` 自己也在返回列表里。** 所以 `DEFAULT` **不是「没有 context」那个空状态**，
**它是一个真实存在的、可被查询到的 context**——这和 `## Mode of operation` 里
「新 context 是 `DEFAULT` 的副本」是一致的：**有原件，才有副本。**

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
所以下面这四步是从正文两句 + 语法节拼出来的，**不是文档给的编号流程**（本页标明来源，避免被当成文档事实）。

1. **建**：`CTXT DEFINE,"<name>"` → 得到一份 `DEFAULT` 的副本。
2. **填**：用 `CONF` 逐个 pin 设 `type`（I / O / IO）与 `mode`（std / fast）。
3. **查**：`CTXT? ALL` → 列出现有的全部 context 名。
4. **删**：`CTXT DELETE,"<name>"`；或 `CTXT DELETE,ALL` **一次全删**。

**两条本页文档没有回答的问题，写在这里免得被当成「文档说了」：**

- **`CTXT` 有没有 sequencer 前置条件——语料未写。** `CTXT` 与 `CONF` 都动 pin configuration，
  而 wiki 里 pin configuration 命令族有一条「sequencer 必须 OFF」的前置条件
  （[[pin-config-requires-sequencer-off]] 收的是 `DFPN` / `UDEF` / `CONF` / `PALS` 四篇的原文）。
  **`CTXT` 这一篇里没有写这条**——**语料在本页范围内未写，不等于它不需要**（§11：文档里有 ≠ 机台这样）。
- **`CTXT?` 能不能按名字查单个 context——语料未写。** 文档 `## CTXT?` 一节只给了 `CTXT?ALL` 一种写法，
  `action` 表里 `ALL` 也标着 `(only in the query)`。**别自己发明 `CTXT? "name"` 这种写法。**

## 和谁有关

- [[conf]] — **配对的另一半，最直接的一条边。** 本条文档把两件事分给了两条命令：
  `CTXT` 管名字，pin 的 `type` / `mode` 归 `CONF`；而文档**两次**把「改 context 的内容」指向 `CONF`。
- [[pin]] — **作用对象**。原句 `for every configured pin` 说的是**每一个已配置的 pin**。
- [[constraint-level-mode-context-match]] — **下游消费者（level 侧）**。
  那条规矩是「level setup 必须指派到 pin configuration 里用 `CTXT` 建出来的 context」，
  **本页是它的前置**——context 先在这里存在，level setup 才谈得上指派。
- [[constraint-timing-mode-context-match]] — **下游消费者（timing 侧）**。
  同一个 context 在 timing 侧的另一半要求（equation set 与 base wavetable 必须同 context）。
- [[pin-config-requires-sequencer-off]] — **同族的锁**。上面「典型用法」里那条语料未写的前置条件，
  答案在这页里；**但它收的四篇原文里没有 `CTXT`**，这一点本页已照实写明。
- `GCTX?`（未建）— 查各 setup 组件当前用哪个 context 的查询命令。
  **本页的文档没有提到它**；它出现在上面两页 constraint 页的出处里。
- `Mode_contexts`（raw `02.06.03.01.03.01_Mode_contexts.md`，未建页）— mode context 的总纲。
  **本页没读**（见「出处」）。

## 版本

本文档有 `## Functional changes` 段，**只有一条**：

- `Introduced before SmarTest 6.3.2`

**这条要按哨兵值读**（§11.2 ②）：它的意思是
「**在本文档集覆盖范围开始之前就已经有了**」，**不是「SmarTest 6.3.2 新增了 `CTXT`」**。
**照字面读会造出一条假版本事实，而且格式齐整。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.md`

**本页没做的：**

- **`02.06.03.01.03.01_Mode_contexts.md` 没读。** 那是 mode context 的总纲。
  所以 **「context 必须在 level / timing / pattern 三处分别指定、且三处必须相同」那套完整规矩，
  本页一个字都没有**——本页只有 `CTXT` 这条命令自己那一层（它出现在上面两页 constraint 页的出处里）。
- **`GCTX?` 没读。** 本页的文档也没提它。
- **`CONF` 的文档没读。** 所以「`CONF` 具体怎么给 pin 设 `type` / `mode`」本页一个字都没有，
  只知道**这件事归它管**。
- **`DFPN` / `PALS` / `UDEF` 等 pin configuration 命令族没读。**
  本页正文里那条「sequencer 必须 OFF」**不是来自本页的文档**——本页已写明它的出处是
  [[pin-config-requires-sequencer-off]]。
- **本页的语法节里没有 `CTXT {action},{"name"}` 这两行语法块。**
  脚本的语法节只收 `Parameters` / `Example` 段，**原文 `## CTXT` 与 `## CTXT?` 两个小节里的代码块没有被收进来**。
  本页「是什么」里出现的那两行语法是**从原文正文抄的，不在那个逐字语法节里**。
- **本文档没有 `## Errors` 段、没有 `## Application` 段、没有 `## Procedure` 段、没有任何图。**

> ⚠️ **语料瑕疵，照实记下，一处都没替它改**：
> ① **同一篇里查询的写法有两种。** 语法一节写的是 `CTXT?ALL`（**问号与 `ALL` 之间没有空格**），
> 而 `## Example` 里写的是 `> CTXT? ALL`（**有空格**）。**两种写法都在原文里**，本页不判哪个对。
> ② **`## Parameters` 不是一张表，是被摊平成「一格一行」的管道行**——
> 取值与说明各自成段，段与段之间夹着空行和孤立的 ` |`。本页的语法节就是照这个样子逐字抽的，
> **不是脚本把表拆坏了**；要按参数名读，照名字去搜。

`verified: doc-only`——**本页没有在任何真实机台上跑过 `CTXT`**（§11：文档里有 ≠ 这台机器上能用）。
