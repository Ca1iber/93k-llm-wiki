---
type: object
title: SetupLevelSet0
layer: L2
stage: level
tags: [level, l2, test-method-api, level-set-0, high-z, clamp, active-load, ps1600, ps5000, ps9g]
related: [level, clmp, sprm, sequencer-status, sqst, ps1600, ps5000, level-setup-tool, disconnect, mapping-level, smartest-6.5.3]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.06_SetupLevelSet0.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# SetupLevelSet0

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **250 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.05.04.06_SetupLevelSet0.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/121827.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：Pins[] | string | array of pins Separate pins with semicolon (;). Valid pin types include I, O, or IO digital pin.

<!-- 语法节 end -->

## 是什么

**`SetupLevelSet0` 是一个 test method，改的是 level set 0（high-z state）上的 clamp 与 active load 设置。**
本篇第一句逐字：

> This test method allows you to change the clamp settings and active load settings of level set 0 (high-z state).

**所以它的作用面很窄**：不是给某个 pin 设驱动电平，
而是**给「sequencer 不在 RUN 时那一套高阻态 level set」挂上钳位电压与有源负载**。

### 默认值：两张表

原文给了两张表。**第一张是「不同 channel card 的默认 clamp / active load」**：

| Parameter | PS1600 / PS5000 |
|---|---|
| `Vcl` | -2.00 V |
| `Vch` | 7.00 V |
| Active load | disabled |

**⚠️ 表名说的是 `the different channel cards`（复数），而表里只有一列 `PS1600 / PS5000`**——
**两种卡共用一列**。原文如此，见「出处」⚠️②。

紧跟着一条 Note（在语料里它是缩进在两张表之间的一行）：

> Note Pin Scale 9G cards do not have clamps and active load. If you try to apply clamp levels and active load settings on PS9G, the settings will be ignored.

**这是本页最实用的一条**：**在 PS9G 上调这两个设置不会报错，会被「忽略」**。

**第二张表是「隐式定义的 fixed level set 1 用到的一些系统默认值」**：

| Parameter | Ce-model | P-model | PS1600 / PS5000 |
|---|---|---|---|
| `Vcl` | -2000 mV | -200 mV | -2000 mV |
| `Vch` | 7000 mV | 5200 mV | 7000 mV |
| Active load | disabled | disabled | disabled |

**三点照实说：**

- **第二张表的表名 `Some system default values as used by the implicitly defined "fixed level set 1".`
  是一个没有谓语的句子片段**——原文如此。
- **`Ce-model` 与 `P-model` 是什么，本篇没有解释**（它们与 `PS1600 / PS5000` 并列为三栏，
  而**这三个词各自指什么、有没有对应关系，语料未写**）。
- **第二张表讲的是 fixed level set 1，不是本类管的 level set 0**——
  原文在同一段里顺带把 fixed level set 1 交代了。

### fixed level set 1 那一段：一句话里三件事

> Fixed level set "1" is the SmarTest default level set: whenever the sequencer is put into a/the "BRK"- or "RUN"-state, and the user does not specify any other fixed or equation-based level set as primary, this level set is used as level primary; the currently selected primaries can be checked by executing the SPRM?-firmware command.

| 事 | 原文 |
|---|---|
| 谁是默认 level set | `Fixed level set "1" is the SmarTest default level set` |
| 什么时候用它 | sequencer 进 `BRK` 或 `RUN`，**且用户没指定别的 primary** 时，它当 primary |
| 怎么查当前的 primary | **执行 `SPRM?` 固件命令** |

**`a/the "BRK"- or "RUN"-state` 里那个 `a/the` 是原文的写法**（见「出处」⚠️③）。

### 参数：三块，八个

参数表共 8 行，天然分三块（**表本身在「语法 / 参数」节里，逐字，本页不重抄**）：

| 块 | 参数 | 类型 | 值怎么给 |
|---|---|---|---|
| **pin** | `Pins[]` | `string`（array of pins） | **分号分隔**；**合法 pin 类型只有 `I` / `O` / `IO` digital pin** |
| **clamp** | `ClampVoltage.Mode[]` / `ClampVoltage.Low_V[]` / `ClampVoltage.High_V[]` | `string` | mode 取 `ON`（`Clamp is set to on with low/high voltage.`）/ `OFF`（`Clamp is set to off.`）；low / high 单位 `[V]` |
| **active load** | `ActiveLoad.Mode[]` / `ActiveLoad.CommutationVoltage_V[]` / `ActiveLoad.SourceCurrent_A[]` / `ActiveLoad.SinkCurrent_A[]` | `string` | mode 取 `ON`（`set up active load setting, Vt, Iol and Ioh`）/ `OFF`（`turn off active load`）；Vcom 单位 `[V]`、Ioh / Iol 单位 `[A]` |

**两条贯穿全表的规矩**（原文在每一格后面都重复一遍）：

- **`Pins[]` 那格**：`Separate pins with semicolon (;). Valid pin types include I, O, or IO digital pin.`
- **其余每一格**：`To specify different configuration for different pins, separate the values with semicolon (;).`

**即：这个 test method 的参数是「按 pin 对齐的数组」**——
一个参数上给了几个 pin，另一个参数上就要给几份值。

> **⚠️ 这张参数表在语料里没有表头行。** 表格直接从第一格数据 `Pins[]` 开始，
> **没有一个 `Parameter` / `Type` / `Description` 表头**。
> **上游核过**：`tdc-html/raw/121827.htm` 里那张 `<table class="ly">` 的
> `<colgroup>` 是 `<col><col><col>`（**三列**）、`<caption>` 是空的、**没有 `<thead>`**，
> 紧接着就是 `<tbody>` 里的 `Pins[]`。**所以「表头缺失」是上游就有的，不是转换丢的。**
> **三列各是什么，是本页按列位置读出来的**（参数名 / 类型 / 说明）——**这一步是（推断）**，
> 依据是每一行第三格都以 `array of` 开头（例：`array of pins` / `array of clamp mode`）、
> 第二格全是 `string`。
> **本页不替它补表头。**

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
唯一像「怎么做」的东西是 `## Implementation pseudo code` 那一块（逐字如下）：

```
IF first run OR parameter changed THEN
 FOR all sites in parallel DO
 IF SmarTest version before 6.3.6 THEN
 issue message
 ELSEIF not PinScale system THEN
 issue message
 ELSE
 //process parameter
 split all string-type parameter values
 validate pin types
 validate the integration of dependent parameters
 //set up Level Set 0 configuration
 IF not already disconnected THEN
 disconnect DUT
 ENDIF
 FOR all pins in pinlist DO
 set up clamp for level set 0
 set termination mode for level set 0
 ENDIF
 set first Run true
END-IF
```

**把它摊成表**（**这不是文档给的流程，是本页把伪码读成条件 → 动作**）：

| # | 条件 | 动作 |
|---|---|---|
| 1 | `first run OR parameter changed` | 才往下走（**否则整块不执行**） |
| 2 | 所有 site 并行 | —— |
| 3 | SmarTest 版本**早于 6.3.6** | `issue message` |
| 4 | 否则，**不是 PinScale 系统** | `issue message` |
| 5 | 否则 | 处理参数：拆所有字符串型参数值 → 校验 pin 类型 → 校验依赖参数的整体性 |
| 6 | 尚未 disconnect | **`disconnect DUT`** |
| 7 | 对 pinlist 里每个 pin | 为 level set 0 设 clamp、设 termination mode |
| 8 | —— | `set first Run true` |

**三点必须一起读：**

- **第 3 步的版本门槛是 `6.3.6`，而本篇 `## Functional changes` 说这个 test method
  `Introduced in SmarTest 6.5.3`。两个数不一样。** 本页并列，不替它调和（§10）——见「出处」⚠️①。
- **第 4 步的条件是 `not PinScale system`**，而上面那条 Note 说的是 **Pin Scale 9G**。
  **「不是 PinScale 系统」与「是 PS9G」不是同一句话**，两者关系本篇没有交代。
- **第 7 步写的是 `set termination mode`，而本篇第一句说的是 `clamp settings and active load settings`。**
  **「termination mode」与「active load」在这里是不是同一件事，本篇没有说。**
  （**本页的（推断）**：参数表里 `ActiveLoad.Mode` 那一格自己写着
  `set up active load setting, Vt, Iol and Ioh`，**active load 在 93K 里就是一种端接方式**；
  依据仅此，**本篇没有一句话把两个词等同起来**。）

> ⚠️ **那块伪码的块结构是不闭合的**（原文如此，见「出处」⚠️④）：
> `FOR all sites in parallel DO` **没有对应的收尾**；
> `FOR all pins in pinlist DO` 的收尾写的是 **`ENDIF`**（不是 `END` / `ENDFOR`）；
> 全文只有末尾一个 `END-IF` 收最外层那个 `IF`。
> **照字面读，这是一个块结构不成立的伪码**——本页**照录，不替它补**。
> 同一块里还有一处大小写不一致：第 1 行写 `IF first run OR parameter changed THEN`（小写 `run`），
> 倒数第 2 行写 `set first Run true`（大写 `Run`）。

**「怎么调用这个 test method」本篇一个字都没有**——
没有 `## Procedure`、没有一句 test method 层面的调用说明、也没有第二个例子。
本页能给的只有上面那块伪码。

## 和谁有关

- [[level]] — **stage 页**。本页 `stage: level` 指的是「最近的一段」而不是「归属」（§6）：
  它改的是 level set 0 上的 clamp / active load，落在 Level 这一段里。
  **「Level 这一段整体怎么走、level set 0 还有哪些硬限制」在那一页，本页不写流程**（§2.2）。
  （**本页读了 [[level]] 那一页**：它把本页记成「Test Method，6.5.3 引入，处理 level set 0 场景」。
  那一页的 `sources` 是本页这一篇**加上另外七十多篇**，**那些 raw 本页一篇都没读**。）
- `Controlling high-Z behavior of digital pins while the sequencers are OFF`（**不在 allowlist，故不链**）
  — **本篇 `## Related information` 两条之一**。raw：
  `../02.06_Command_Reference/02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`。
  **本页没读**——所以「high-Z 那套机制整体怎么配、level set 0 为什么存在」本页一个字没有。
- `Pull-down function`（**不在 allowlist，故不链**）— **两条里的另一条**。raw：
  `../02.06_Command_Reference/02.06.05.01.05.06_Pull-down_function.md`。**本页没读。**
  这两条链接在语料里是**挤在同一行、中间没有任何分隔符**的（见「出处」⚠️⑤）。
- [[clmp]] — **同一组量的 L1 侧**。本篇参数里叫 `ClampVoltage.Low_V` / `ClampVoltage.High_V`，
  而默认值表里叫 `Vcl` / `Vch`——**同一个东西的两种名字**。
  **这条对应关系是（推断）**，依据只是 `Vcl` / `Vch` 这两个词在 level 语境里指的都是一对钳位电压；
  **本篇没有点名 [[clmp]]，那一页本页也没读**。
- [[sprm]] — **原文点名的一条固件命令**
  （`the currently selected primaries can be checked by executing the SPRM?-firmware command`）。
  这是本页唯一提到的 L1 命令，**它指路的只是「怎么查 primary」**。
  **[[sprm]] 那一页本页没读**，所以 `SPRM?` 的回复格式、别的用法本页一个字没有。
- [[sequencer-status]] / [[sqst]] — **原文那句里出现了 sequencer 的 `BRK` / `RUN` 两个状态**，
  而**这两个状态怎么设、怎么查不在本篇**。**两页本页都没读**；
  这里只按「sequencer 状态」这件事指路，**不代表本篇与那两页有文档明写的对应**。
- [[ps1600]] / [[ps5000]] — **默认值表那一列的两种卡**。本页只从这一篇里知道
  它们的默认 `Vcl` / `Vch` / active load（第二张表里它们还有第三组值）。
  **两页本页都没读。**
- [[level-setup-tool]] — **（推断）这一设置平时在 GUI 上对应哪一块**。
  **本篇没有出现任何界面名**——所以这条只是按「level 的设置面」指路，**不是文档点名**。
  **那一页本页没读。**
- [[disconnect]] — **伪码里有一步 `disconnect DUT`**。**本条按名字并列**：
  伪码说的是「DUT 被断开」这件事，**是不是 [[disconnect]] 那页讲的那个对象，本页没有依据**
  （**两页的 raw 不同，本页没读那一页**）。
- [[mapping-level]] / [[smartest-6.5.3]] — **跨层对照表**与**版本页**。
  **[[mapping-level]] 本页没读**，本页与它的关系只是「同在 level 这一段」。

## 版本

本文档有 `## Functional changes` 段，**只有一条**：

- **Introduced in SmarTest 6.5.3**

**这是一条正常的 `Introduced in`，不是 §11.2 ② 那个 `Introduced before` 哨兵**——
所以它**可以照字面读**：**6.5.3 之前没有这个 test method**。
本 wiki 面向 7.10.3，**它在**。

**⚠️ 它与伪码里的版本门槛对不上**：`## Implementation pseudo code` 里写的是

> IF SmarTest version before 6.3.6 THEN

**`6.3.6` 与 `6.5.3` 是两个不同的数。** 两种读法都能自圆其说——
① 伪码那句是「比 6.3.6 更早的版本要发消息」，
而本 test method 本身要 6.5.3 才有，**于是那个分支在任何真实版本上都不会走到**；
② 或者其中一个数是文档的笔误。
**本篇没有解释这个差，本页不替它选一个**（§10：两种说法并列，各自附 `sources`）。

**它之后有没有被改过、有没有被废弃——本篇一个字都没有。**
**「没记录」不等于「没改过」**（§13.1 第 ⑥′）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.05.04.06_SetupLevelSet0.md`
（TDC `121827.htm`，97 行 / 4,160 字节）。**整篇读完。**

**本页没做的：**

- **`Controlling high-Z behavior of digital pins while the sequencers are OFF` 与
  `Pull-down function` 两篇没读**——**它们就是本篇 `## Related information` 的两条**。
  所以「level set 0 为什么存在、平时怎么用、pull-down 怎么配」**本页一个字都没有**；
  本页只有「这个 test method 改哪两个设置」。
- **`SPRM?` 那一篇没读**（`02.06.05.02.22_SPRM`）——本页只知道原文那句
  `the currently selected primaries can be checked by executing the SPRM?-firmware command`。
- **`Ce-model` / `P-model` 两栏没有追**——本篇没解释，本页也不去别篇找（§11）。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论**（§11.4：没看图就写「本页没用图」，理由不编）。
- **没有实跑。** 没有在任何机台上调用过这个 test method，
  也没有在 PS9G 上验证过「设置被忽略」那条 Note。`verified: doc-only` 指的就是这件事。
- **本文档没有 `## Procedure` / `## Before you begin` / `## Important points` / `## Example` 段。**
  上面「典型用法」那一节排的是 `## Implementation pseudo code`，
  **不是文档给的编号流程**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改。**
> **全部回上游 `tdc-html/raw/121827.htm`（10,339 字节 / 228 行）核过，结论写在每条后面。**
> ① **版本门槛与引入版本不一致**：伪码里是 `IF SmarTest version before 6.3.6 THEN`，
>   而 `## Functional changes` 是 `- Introduced in SmarTest 6.5.3`。
>   **上游核过**：`121827.htm` 里 `6.3.6` 出现 1 次、`Introduced in SmarTest 6.5.3` 出现 1 次，
>   **不是转换改的，是文档自己不一致。**
> ② **第一张默认值表的表名说 `cards`（复数），表里只有一列 `PS1600 / PS5000`**——
>   原文逐字 `The default clamp voltage levels and active load settings of the different channel cards are:`。
>   另：第二张表的表名 `Some system default values as used by the implicitly defined "fixed level set 1".`
>   **是一个没有谓语的句子片段**。**两条都是上游的措辞**（本页读的就是上游的原句）。
> ③ **`whenever the sequencer is put into a/the "BRK"- or "RUN"-state`**——
>   **`a/the` 两个冠词并排**。**上游核过**：`121827.htm` 里逐字是
>   `a/the "BRK"- or "RUN"-state, and the user does not specify`，**上游如此**。
> ④ **伪码的块结构不闭合**：`FOR all sites in parallel DO` 没有收尾；
>   `FOR all pins in pinlist DO` 收在 `ENDIF` 上；末尾只有一个 `END-IF`。
>   **上游核过**：`121827.htm` 第 216–220 行一带的伪码里就是这几个关键字
>   （`IF not already disconnected THEN` / `disconnect DUT` / `ENDIF`），
>   **`ENDIF` 与 `END-IF` 混用是上游的**。
>   同一块里另有一处大小写：第 1 行 `IF first run OR parameter changed THEN`（小写 `run`）
>   与倒数第 2 行 `set first Run true`（大写 `Run`）。
>   **上游核过**：两个串在 `121827.htm` 里逐字都在。
> ⑤ **`## Related information` 的两条链接挤在同一行、中间没有任何分隔符**（连空格都没有）。
>   **上游核过：这是转换丢的块边界，不是上游就坏的**——`121827.htm` 第 228 行里那两条是
>   两个独立的 `<div>`，每个里面一个 `<a>`。**markdown 把两个块并成了一行**，
>   文本一个字没少，**丢的是块边界**。
> ⑥ **参数表没有表头行**（表格直接从 `Pins[]` 开始）。
>   **上游核过：`121827.htm` 的 `<table class="ly">` 里 `<colgroup>` 是三列、
>   `<caption>` 空、没有 `<thead>`**——**所以「表头缺失」是上游就有的，不是转换丢的。**
> ⑦ **本篇没有坏字。** 用 `[一-鿿]` 实测全文 **0 处非 ASCII 字符**
>   （没有 `鈥` / `渭` / `碌` 那一族）。**这是「本页量过的」，判据是本篇这一个文件**；
>   §11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上调用过 `SetupLevelSet0`**
（§11：文档里有 ≠ 这台机器上能用；尤其 PS9G 那条「设置被忽略」，
**动手前先照实机核对**）。
