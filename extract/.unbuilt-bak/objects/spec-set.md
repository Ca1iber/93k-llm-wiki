---
type: object
title: Spec sets
layer: L2
stage: level
tags: [level, spec-set, specset, level-file, spec-variable, spec-tool]
related: [level, level-file, spec-tool, spec-variable, equation-based-level-setup]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.09_Spec_sets.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Spec sets

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**一句话：spec set 是「给 spec 变量赋的一组值」。** 原文第一句就是全部机制：

> 「Spec sets assign values to the spec variables declared in the SPECS module.」

**所以一条 spec set 不是「一个值」，是一整套值**——它一次性给某个 spec 模块里声明的
**所有** spec 变量填上值。**这也是为什么原文说的是「选一个 spec set」而不是「选一个 spec 值」。**

### 它在 level file 里长什么样

原文给了模块头的形状和一个逐字例子：

> 「The module header starts with the keyword SPECSET followed by the spec set number, an integer in the range 1 to 99, and a descriptive name, the spec set description.」

```
SPECSET 1 "example specification"
```

| 位置 | 是什么 | 约束 |
|---|---|---|
| `SPECSET` | **模块头的关键字** | 固定 |
| `1` | **spec set 编号** | 原文：`an integer in the range 1 to 99`——**1 到 99** |
| `"example specification"` | **spec set 描述**（描述性的名字） | 原文：`a descriptive name, the spec set description` |

**编号上限 99 是本页唯一的硬数字。** 原文没有说「一份 level file 能放多少个 spec set」，
也没有说编号要不要连续——**只给了 1 到 99 这个范围。**

### 一个 spec 模块可以有多个 spec set，测试里选一个

原文两句话把「多套值并存、用时挑一套」这件事说完：

> 「You can setup different spec sets for a particular spec module. When you set up a test you select the spec set you want to use.」

**两条信息**：
- **一个 spec 模块下面可以挂多套**（`different spec sets for a particular spec module`）；
- **选择发生在「set up 一个 test」的时候**（`When you set up a test you select …`）——
  **不是**在跑测试的时候，也不是在 level file 里。
  **「怎么选」的具体操作原文没写**（它只说了「select」这个动作）。

### 换 spec set 就能换 level 设置（这是它的用途）

原文最后一节之外的收尾句：

> 「Changing the spec set from one test to the other allows you to execute tests with different level settings.」

**这就是它的存在意义**：**同一个测试程序，换一个 spec set，跑出来的 level 设置就不同。**
**（推断）因此它常被用来做「同一套测试、不同规格档」的切换**——
依据只有这一句话里的 `different level settings`；**原文没有举任何例子。**

### 它在方程编辑器里看不见

这条是原文专门用一整段说的，**是使用上最容易踩的一脚**：

> 「Spec sets are not displayed in the equation editor. To see the module you would have to open the level file in an ASCII editor (for example, vi).」

**两件事**：
- **方程编辑器里看不到 spec set**（`not displayed in the equation editor`）——
  **所以别在方程编辑器里找它，找不到不是出错。**
- **要看它的原文，只能拿 ASCII 编辑器打开 level file**（原文举的例子是 `vi`）。
  **（推断）也就是说 spec set 的物理落点是 level file**——
  依据是这句 `open the level file`；**原文没有另起一句直说「spec set 存在 level file 里」。**

## 典型用法

> **原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段**
> ——定义文档只有 25 行，**没有一套编号步骤可抄。**
> 下面三条都是从「怎么创建 / 怎么选 / 怎么看」这三处散文里抽的。

**1. 要创建或改值，用 Spec Tool。** 原文：

> 「To create a spec set and to specify or modify the values, use the [Spec Tool](<../02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.md>).」

**注意原文把「创建」和「指定 / 修改值」都归给同一个工具**（`create … and … specify or modify the values`）。
**Spec Tool 怎么用，本篇没写**——那句话只给了工具名和它所在的路径
（`02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool`）。

**2. 要选哪一套，在 set up test 的时候选。**
原文只有 `When you set up a test you select the spec set you want to use.` 这一句，
**「在哪个界面、点哪里」本页没有**。

**3. 要直接看或手改，用 ASCII 编辑器打开 level file。**
原文举的例子是 `vi`。**这是原文唯一给出的「绕过工具」的路径**，
但它说的是 `To see the module`（**看**）——
**原文没有说能不能用编辑器直接改、改完会不会被工具覆盖。**

**4. 顺序上的前提（（推断））**：spec 变量必须先被**声明**（`spec variables declared in the SPECS module`），
spec set 才有东西可赋值。**依据是原文第一句的 `declared` 这个过去分词**；
**原文没有把这条写成一句要求。**

## 和谁有关

- [[level-file]] — **spec set 的落点**。原文：要看它得 `open the level file in an ASCII editor`。
  **两页的关系是「内容 ↔ 宿主文件」**
- [[spec-tool]]（**未建**）— **创建与改值的唯一指定工具**，原文点名的那一个
- [[spec-variable]]（**未建**）— **spec set 赋值给谁**：原文第一句的
  `the spec variables declared in the SPECS module`。**「spec 变量怎么声明」两页都没有**
- [[level]] — 本页 `stage: level` 的归属阶段页：**spec set 管的是供电那一段的规格值**
- [[equation-based-level-setup]] — **同为 level 阶段里「值从哪来」的一页**；
  **注意原文专门说了 spec set 在方程编辑器里看不见**，**这正是两页的接缝所在**
- [[level-master-file]] / [[level-setup-tool]] — 同属 level 文件族的兄弟；**本页不主张具体关系**
- `SPECS module` / `Spec Tool`（**未建**）— `Spec Tool` 那句里的原始链接目标
  （raw: `02.08.04.30_Spec_Tool.md`）

## 版本

原文有 `## Functional changes` 段，**只有一条**：

- **Introduced before SmarTest 6.3.2**

> **这一条是哨兵值，不是「6.3.2 新增的」。**
> 它写的是 `before`——意思是「**在本文档集覆盖范围开始之前就已经有了**」（schema §11.2 ②）。
> **照字面读会凭空造出一条「SmarTest 6.3.2 新增了 spec sets」的假信息，而且格式齐整。**

**原文没有给任何后续变更条目**——所以「spec set 的编号范围、语法、
可见性在 6.3.2 之后改过没有」本页没有依据。

## 出处

`sources:` 一篇：

`02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.09_Spec_sets.md`
（TDC `56957.htm`，共 24 行）

**本页没做的**：

- **只读了这一篇。** 本页正文里每一个事实都出自这 25 行。
- **`Spec Tool` 那篇没读**（原文里面那句 `To create a spec set … use the Spec Tool` 指向的
  `02.08.04.30_Spec_Tool.md`）。**所以「怎么创建 / 怎么改值」的全部操作细节本页没有**——
  **本页只知道该用哪个工具，不知道怎么用。**
- **`spec variables` / `SPECS module` 没有专页，也没读任何相关文档**——
  **「spec 变量怎么声明、有哪些类型」本页一个字都没有。**
- **`level file` 那篇没读**——**本页知道 spec set 在它里面，但不知道它的结构、
  不知道 spec set 段落排在哪儿。**
- **原文没有 `#### Subtopics` 段**，本页即没有兄弟文档可顺；
  **本页「语法 / 参数」节因此是空的**（脚本只对加标记的段落动手，
  而这篇既没有 `Syntax` / `Parameters` / `Example` 段标记，也没有 `Subtopics` 可跟）。
  **这不是本页的缺陷，是本脚本的判据如此（§4）。**
- **没有实测**：本页没有打开过任何 level file 验证 `SPECSET` 的实际写法，
  **`SPECSET 1 "example specification"` 那行是照原文抄的示例。**
- **原文没有一张图**，本页没有任何来自图的结论。

> ⚠️ **本篇的语料瑕疵，照实记，一处都没替它改**：
>
> ① **`setup` 被当动词用**（应为 `set up`）：
> `You can setup different spec sets for a particular spec module.`
> ——**同一篇的下一句就写对了**：`When you set up a test you select …`。
> **同一段里两种写法并存，本页并列记下，不替它统一。**
> ② **`from one test to the other` 措辞可疑**（常见写法是 `from one test to another`）：
> `Changing the spec set from one test to the other allows you to execute tests with different level settings.`
> **本页照抄，不判对错**——它可能是笔误，也可能是原文的固定说法，**原文没有第二处可对照。**
> ③ **同一篇里模块有两个名字**：先写 `declared in the SPECS module`，
> 紧接着写 `The module header starts with the keyword SPECSET`。
> **`SPECS`（模块名）与 `SPECSET`（模块头关键字）是不是同一个东西，原文没说，本页不判。**
> ④ **`Introduced before SmarTest 6.3.2` 是哨兵值**，见上面「版本」节的说明（§11.2 ②）。

`verified: doc-only`
