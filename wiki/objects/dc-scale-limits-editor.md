---
type: object
title: DC Scale Limits editor
layer: gui
stage: pin
tags: [pin, gui, dc-scale, limit, safety, pin-configuration, dps, error-message]
related: [pin-configuration-tool, dps-pins-editor, utility-pins-editor, digital-pins-editor, dc-scale-uhc4t-card, dc-scale-xps256-card, dpspins-resources, mapping-pin, pin, add-limit, limit, smartest-7.2.1]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.06_DC_Scale_Limits_editor.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# DC Scale Limits editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**DC Scale Limits editor 是给 DC Scale 卡配「电压 / 电流安全限值」的 GUI。** 原文开门两句逐字：

> 「DC Scale Limits is a safety feature. If the voltage or current is too high or too low, an error
> message is triggered.」

> 「Any limit settings done here apply for DC Scale cards only.」

**它是一个 safety feature**：超限就触发错误信息。**而且只对 DC Scale 卡生效**——
第二句把作用范围写死了（`for DC Scale cards only`）。

**编辑器由五个 cell 组成**（原文引子逐字：`The DC Scale Limits editor consists of the following cells:`）：

| cell | 原文（逐字） |
|---|---|
| `Name` | `A descriptive name for the DUT pin.` |
| `Max Volt[V]` | `The upper voltage limit` |
| `Min Volt[V]` | `The lower voltage limit` |
| `Max Source[A]` | `The upper current limit.` |
| `Min Source[A]` | `The lower current limit.` |

**五格里有一个不是限值**：`Name` 是「DUT 针的描述性名字」——**所以这个编辑器的行是按 DUT 针
组织的，不是按 tester channel**（推断：**依据就是这一句里的 `for the DUT pin`**；
原文没有说这个名字与哪个编辑器共用）。

**四格限值的形状是「两个量 × 上下限」**：电压 `[V]`、电流 `[A]`，**单位写在列名的方括号里**。
**原文没有给任何一格的取值范围、默认值或步长。**

⚠️ **电流那一对的列名在正文和图上是两个不同的词**（正文 `Min Source[A]` / 图 `Max Sink[A]`），
见 `## 出处` ②。

### 限值查哪儿

原文在表后只有一句出口：

> 「For the appropriate limits see the specifications for DC Scale Device Power Supplies.」

**即：这个编辑器不告诉你「限值该填多少」。** 判据在 DC Scale 器件的电源规格里，
**那一篇本页没读**（见 `## 出处`）。

### 界面长什么样（图证 · `142047.png`）

原文 `## Example` 一节**只有一张图**（`../../../../raw/142047.png`，
alt 文字就是 `DC Scale Limits editor`）。**整张读过**，逐格读出来是：

- 窗口标题是 **`*DC Scale Limits`**——**开头有一个 `*`**，原文没解释它是什么。
- 表头从左到右：行号、`Name`、`Max Volt[V]`、`Min Volt[V]`、`Max Source[A]`、
  **`Max Sink[A]`**（**与正文最后一个列名不同，见 `## 出处` ②**）。
- 两行数据逐格是：
  `DPSGang` / `3` / `-1` / `OFF` / `OFF`；
  `DPSSingle` / `OFF` / `OFF` / `0.400` / `-0.1`。

**图上答掉的三件事（正文里一个字都没有）：**

1. **限值可以填 `OFF`**，而且**第 1 行是电压两格有数、电流两格全 `OFF`，第 2 行正好相反**
   ——**所以 `OFF` 不是「无效」，而是一种可用的取值**（推断：**依据是两行各自只填了成对的
   另外两格，形态是「这一类不管」**）。
2. **电压可以填负数**（`-1`），**电流也可以**（`-0.1`）。
3. **`Name` 栏里放的是 `DPSGang` / `DPSSingle` 这种针名**，**两个针各占一行**。

**哪些字算图证，逐个 `grep -F` 核过**：`*DC Scale Limits`、`Max Sink[A]`、`DPSGang`、
`DPSSingle`、`OFF`、`0.400`、`-0.1` **在本篇 raw 里都是 0 次**；
而 `Name` / `Max Volt[V]` / `Min Volt[V]` / `Max Source[A]` / `DC Scale Limits` 本身
**是搜得到的**——**所以列名不算图证，只有上面那串算**（§11.4 要的就是这条分界）。

**图答不了的，照实说**：`OFF` 到底是什么意思、**「什么时候该只填一半」有没有规矩**、
标题那个 `*` 是什么、这张图是哪个版本截的——**图上和正文里都没有**。

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`**；
`## Example` 只有一张截图、**一句说明文字都没有**。
**所以下面的顺序是从「列序 + 图」拼的（推断），不是文档给的步骤**：

1. **在 `Name` 里写 DUT 针名**（原文：`A descriptive name for the DUT pin.`）。
2. **填 `Max Volt[V]` / `Min Volt[V]`**：上限 / 下限电压。
3. **填 `Max Source[A]` / `Min Source[A]`**：上限 / 下限电流。
4. **值从哪来**：`For the appropriate limits see the specifications for DC Scale Device Power
   Supplies.` ——**那一篇本页没读，所以「该填多少」本页一个数都没有。**
5. **填错了会怎样**：原文只说 `an error message is triggered`——
   **信息文本是什么、在哪显示、是 warning 还是 error，原文没写**（见 `## 出处` ⑧）。

**从原文和图能落成的动作：**

| 要做的 | 依据 |
|---|---|
| **只让电压受限** | 图第 1 行：电压两格填数、电流两格 `OFF` |
| **只让电流受限** | 图第 2 行：反过来 |
| **查「合适的限值」** | 原文那一句指向 `DC Scale Device Power Supplies` 的规格 |
| **确认改动的作用范围** | `Any limit settings done here apply for DC Scale cards only.` |

## 和谁有关

- [[pin-configuration-tool]] — **本编辑器是它的一个 element**。
  [[pin-configuration-tool]] 那页把 `DC Scale Limits` 列在它的元素表里，定义逐字是
  `Define voltage and current limits for DC Scale cards.`；**那页记的父文档 `Functional changes`
  里还有一条 `SmarTest 7.2.1: DC Scale Limits added.`**——**与本页 `## 版本` 那一条对得上。**
  **⚠️ 这一条不是本页 raw 写的**（本页 raw 里 `Pin Configuration` 出现 0 次），
  **出自 wiki 的 [[pin-configuration-tool]] 页；本页没有回那篇原文核。**
- [[dps-pins-editor]] / [[utility-pins-editor]] / [[digital-pins-editor]] — **同 `stage: pin`
  的同族 GUI 编辑器**。分工的形状一致：**那几页管「针」（名字、极性、通道），本页管「限值」。**
  **⚠️ 两边的 raw 互相都没提对方**（本页 raw 里 `DPS Pins` 出现 0 次）——
  **所以这是「同一 stage 并列」的关系，不是任何一篇文档写出来的。**
- [[dc-scale-uhc4t-card]] / [[dc-scale-xps256-card]] — **（推断）卡侧**。
  本页 raw 只说限值 `apply for DC Scale cards only`，**而它给出的出口是
  `DC Scale Device Power Supplies and VI Cards`（未建）**。
  **那两页是 wiki 里名字带 DC Scale 卡的页，本页没读，不知道它们收不收规格。**
  **本页正文没有一条卡的事实。**
- [[dpspins-resources]] — **本页 raw 的 `## Related information` 直接链了它**
  （原文那一串里的 `DPSPINS resources`）。**它为什么在那里、和限值什么关系，原文一个字
  没解释；本页没读那篇。**
- [[mapping-pin]] — **（推断）GUI↔文件的对照**。本页是 GUI 侧的限值页，
  [[mapping-pin]] 收的是「某个对象在 GUI / 文件 / L1 三侧各是谁」。
  **本页 raw 里没有提任何文件或命令，所以这条关系本页没有依据**；
  [[dps-pins-editor]] 那页记过同族的一行，**而那一页也没读它的原文**。
- [[pin]] — `Name` 那一格指的是 `the DUT pin`，**所以本页是「给一个 pin 属性」的地方**；
  **pin 本身是什么、有哪些属性，在不在这页，本页没读。**
- [[add-limit]] / [[limit]] — **（推断）名字近、所指未必同物**。
  **本页 raw 里这两个名字出现 0 次**；本页讲的是 DC Scale 的**硬件安全限值**（超限触发出错），
  那两页从名字看是测试结果的限值。**本页没有依据判断是不是同一批东西——
  按页名相邻列出，不代表同物。**
- `DC Scale cards`（**未建**）— 本页 raw `## Related information` 的第一个链接，
  **也是作用范围那句话（`for DC Scale cards only`）的所指。**
- `DC Scale Device Power Supplies and VI Cards`（**未建**）— **本页唯一的「限值该填多少」的出口。**
- `EVENT_ICVM.limits()` / `EVENT_ICVM.limitHigh()` / `EVENT_ICVM.limitLow()` /
  `EVENT_ICIM.limits()` / `EVENT_ICIM.limitHigh()` / `EVENT_ICIM.limitLow()`
  （**六个，均未建、均不在 allowlist，故用反引号**）——**本页 raw `## Related information`
  里六个连着的链接。**从名字看是 test method 侧读写限值的入口**
  （推断，**依据只是方法名里的 `limits` / `limitHigh` / `limitLow`**）；
  **它们与本编辑器填的是不是同一份限值，原文没说，本页不知道。**
- `DC Scale Extensions editor` / `DC Scale Regulation editor`（**均未建**）——
  **（推断）同族的另两个 DC Scale 编辑器**，**依据只是 [[pin-configuration-tool]] 那页的
  元素表里与本编辑器并列**；**本页 raw 里没有它们。**

## 版本

原文 `## Functional changes` **只有一条**，逐字：

- `Introduced in SmarTest 7.2.1`

**这一条不是 §11.2 ② 那个哨兵值**（不是 `Introduced before SmarTest 6.3.2`）——
**本编辑器是 SmarTest 7.2.1 引入的，是一条真版本事实。**

**（推断）7.2.1 这个数与 [[pin-configuration-tool]] 那页记的父文档条目一致**：
那页逐字记着 `SmarTest 7.2.1: DC Scale Limits added.`。
**依据是两边同一个版本号 + 同一个功能名；本页没有回那篇原文核，所以这是推断。**

**与 wiki 目标版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（§11），
而这一篇**只有 7.2.1 一条**——**所以 7.2.1 到 7.10.3 之间这个编辑器有没有改过
（加过列、改过名），语料里没有依据。**

详见 [[smartest-7.2.1]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.06_DC_Scale_Limits_editor.md`
（`142046.htm`，72 行）——**整篇读完**。

**本页做了什么**：

- **读了本页唯一那张图** `142047.png`（`## Example` 一节的全部内容），**逐格读过**。
  **图答掉的三件事写进了「是什么」；图里读到的字一律没有进 `>` 引文块**——
  引文块的含义是「这段能在 raw 文本里搜到」，**图上的字搜不到**（§11.4）。
- **为了核「本编辑器归谁管」这一句，读了 wiki 的 `wiki/objects/pin-configuration-tool.md`**
  （**是 wiki 页，不是 raw**）。结论只写在「和谁有关」与「版本」两处，
  **每条都标了「不是本页 raw 写的」。**

**本页没做的**：

- **本页 raw 里没有 `## Syntax` / `## Parameters` 一类的段标记**（唯一一个 `## ` 段
  是 `## Example`，而它下面只有一张图）——**所以「语法 / 参数」节是空的；
  上面五个 cell 那张表是我从散文里转述的，不是逐字**；凡加 `>` 的地方才是逐字原文。
- **`DC Scale Device Power Supplies and VI Cards` 没读** —— **这是本页最大的空缺**：
  原文把「限值该填多少」整个推给它，**而本页一个数、一个范围、一个单位换算都没有。**
- **`DC Scale cards` 没读** —— 所以 `for DC Scale cards only` 那句里的范围
  **具体含哪几张卡，本页不知道。**
- **[[dpspins-resources]] 没读** —— `## Related information` 链了它，**两者什么关系本页不明。**
- **六个 `EVENT_ICVM` / `EVENT_ICIM` 方法一篇没读** —— **只能给名字，不能给它们做什么。**
- **`02.06` 的命令原文一篇没读**，[[add-limit]] / [[limit]] 两页也没读——
  **本页正文没有一条命令事实。**
- **没有实跑。** 没有在机台上开过这个编辑器、没有故意超限触发过那条 error message。
  `verified: doc-only` 指的就是这件事。
- **`## Example` 那张图是「一次具体配置的截图，不是格式规范」** —— 哪格必填、
  `OFF` 的语义、`*` 的含义，图上都没有。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pin.md`。

> ⚠️ **本篇的语料瑕疵与对不上的地方，照实记、一处没替它改**：
>
> **① 正文那张表残破，与 [[dscp]] / [[uptd]] 两篇同形。** 它**没有表头**，
> 而且每一格前后都夹着孤立的 `|` 行。逐字（开头两格）：
> ```
>  |
>
> Name
>
>  |
> ```
> ——**列名与说明各占一行、被空行和裸 `|` 隔开**，markdown 里渲染出来不成表格。
> **本页照实说，不替它补竖线、不替它加表头。**
>
> **② 正文最后一个列名与图上列头不是同一个词。** 正文逐字写
> `Min Source[A]`（说明是 `The lower current limit.`），
> **而图 `142047.png` 上那一列的列头是 `Max Sink[A]`**——
> **`Max Sink` 在本篇 raw 里出现 0 次**（逐字核过）。**两处并列，本页不判哪个是当前列名。**
>
> **③ 电流那一对列名的构词与电压那一对不同。** 电压是 `Max Volt` / `Min Volt`（上限 / 下限），
> 电流是 `Max Source` / `Min Source`——**而说明文字两对都写成 `upper` / `lower`**
> （`The upper current limit.` / `The lower current limit.`）。
> **`Source` 不是 `upper` 的同义词**（source / sink 说电流方向，max / min 说大小）；
> **图上那一列叫 `Sink` 正好说明这一点**。**原文没说这个命名是有意的还是笔误，
> 本页照实并列。**
>
> **④ `## Related information` 八个链接全部粘在一起，中间没有任何分隔符。** 逐字（开头）：
> `[DC Scale cards](<…>)[DC Scale Device Power Supplies and VI Cards](<…>)[DPSPINS resources](<…>)[EVENT_ICVM.limits()](<…>)`
> ——**一个挨一个，没有空格、没有逗号、没有换行**（与 [[dscp]] 那篇同位置的毛病同类）。
> **本页按名字逐个拆开列，不替它补分隔符。**
>
> **⑤ `## Example` 一节的内容只有一张图，一个字的说明都没有。** 同族的 [[dps-pins-editor]]
> 那篇的 `## Example` 至少有一句 `See DC Scale pin (DPS mode) setup`；
> **本篇连这一句都没有**——**图下面直接就是 `## Related information`。**
>
> **⑥ 「安全特性」这个说法只在第一句出现一次，之后全文再没提。** 逐字：
> `DC Scale Limits is a safety feature.` ——**它说的是 `DC Scale Limits`（不带 editor），
> 而紧接着的第二段说的是 `The DC Scale Limits editor`。**
> **同一篇里两个名字指同一个东西，原文没有统一。**
>
> **⑦ `error message` 的性质没说。** 逐字只有 `an error message is triggered`——
> **是不是真的 error（会不会中止测试）、还是只是 warning、文本长什么样、在哪儿显示，
> 原文一个字都没有。** 对一个自称 safety feature 的编辑器，**「触发了会怎样」这条链是断的。**
>
> **⑧ §11.2 ① 那种编码损坏本篇没有。** 本页查过：**CJK 字符 0 个、U+00A0 0 个、
> `鈥` 一族 0 个**，全文只有 ASCII。
>
> **⑨ 工具链与本篇 raw 对不上的一处（这一条不是语料的错，是骨架的）。**
> 本页 `## 语法 / 参数` 节的脚本说明逐字写
> `定义文档里没有 Syntax / Parameters / Example 这类段标记`，
> **而本篇 raw 第 62 行就是一个真实的段标记 `## Example`。**
> **两者为什么对不上，本页没有查**（可能是脚本对「只有图、没有文本」的段做了截断，
> 也可能它认的段标记集合与本文不同）。**照 §11.1 的分工，本页不替任何一侧改，
> 只把这一处并列在这里。本节本页一个字都没动。**

`verified: doc-only`
