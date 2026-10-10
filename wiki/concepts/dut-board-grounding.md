---
type: concept
title: Grounding
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.09.04_Grounding.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Grounding

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

原文开篇先拆词：**「地」对不同的人指不同的东西**——signal ground、circuit ground、
chassis ground、safety ground、earth ground、reference ground、ground layer、zero volt、
return path……**对 DUT board 设计者，地 =「受控的返回路径」（controlled return path）**；
**grounding = 有系统地把所有地连起来，使所有设计目标都达成。**

**两种根本不同的接地概念：**

- **混合信号接地**：不同地（`DGND`、`AGND`、`UGND` 等）**分开**，
  直到靠近 DUT 处才用电感或磁珠连起来。
- **今天的 SOC 型接地**：**所有地在每个 DUT 正下方连成一个坚固的、类法拉第笼的网格**。

### 目标之间会打架

数字、模拟、DPS、RF 各子系统对地的要求不同，**有些是互相冲突的，必须自己判断哪些适用**。
原文列的设计目标：**降低串扰 / 降低地弹 / 降低 RF 损耗 / 减小压降 / 可接受的感应噪声水平 /
改善 site 间一致性**。

### 设计时要过的四个量

| 考量 | 原文要点 |
|---|---|
| **信号频率** | **数字信号是宽带的** |
| **电流幅度** | 压降与信号电流成正比 |
| **噪声电压阈值** | 电路能承受或产生的噪声水平；**为成本可控，按「可接受的噪声水平」设计** |
| **返回路径** | **低频走电阻最小路径，高频走电感（更一般地说：阻抗）最小路径**——所以要按高/低频要求提供直接的低阻抗/低电阻返回路径 |
| **多条传播路径** | **返回电流按各路径阻抗反比分配**——所以要保证信号路径正下方（或附近）**只有一条**返回路径；**水平层和垂直层都算** |

### 原文推荐的几条做法

- **造类法拉第笼结构**，把信号传播关在里面。
- **用直接、低阻抗的连接接到 DUT board 地。**
- 一个手法：**把电源平面和它的地平面放得靠近 DUT 侧那一层**（而不是像早期设计那样放中心层）——
  **过孔更短，电感更小**。
- 如果**必须保持单点接地**，可以**用容性连接在多个点接到信号地**；**电容引线要短**。

### 限噪的关键步骤（原文列的）

- 选**最适合应用**的卡：一般要求用**最便宜的多针卡**；**低电平、严苛要求的针才用贵的 clean-signal 卡**。
- **在卡的输出端做滤波**，也就是**靠近信号 pogo 针落点**处。
- **在电路处把噪声掐掉**：靠近 DUT 用强滤波。
- **布线**让信号不再捡到额外噪声。
- **把这些手段合起来用**（`Combine all these approaches.`）。

### 避免地环路

原文单列一节，口气最重的一条：**永远避免地环路**——
即避免「电流能走不止一条路」的地回路，高频下则是「信号能沿不止一条路传播」。

> **`Avoid ground loops! Provide one path only!`**

**只要地连接了两个点，电流就该只有一条路，不能有替代路径。**
原文举了个很具体的例子：**即使只是远处的一个返回过孔或返回针，也会造成地环路。**

频率或电平稍有不同，信号在两条（或更多）传播路径上的分配就会变——
**当其中一条路捡到更多感应噪声、或其中一条路的串扰抑制更好时，这个效应尤其麻烦。**

## 典型用法

**1. 什么时候翻这一页**：做 DUT board 设计、或排「噪声大 / site 间不一致 / 地弹」这类问题时。
它是**设计准则**，不是流程步骤。

**2. 与其他页面的分工**：本页讲**板级接地怎么做**；
`UGND` / `DGND` 之间**要不要插隔离电路**这种具体判断在
[[sequencer-controlled-utility-lines]]（串口场景）里有它自己的说法。
**两页不重叠**：一页是通则，一页是那个场景下的要求。

**3. 本页不回答「用哪种地」**——原文明确说**要求会冲突，得你判**。

## 和谁有关

- [[pin]] — DUT board 设计属 pin 阶段；pogo 针落点、返回路径都在那里
- [[pogo-pad-and-via-design]]、[[pogo-block-compatibility]]、[[inter-layer-via-design]] —
  同属 DUT board 设计参考这一族，讲的都是**过孔与 pogo 的物理设计**
- [[utility-line-assignments]] — utility 地针 `UGND` 出现在 utility pogo block 上
- [[sequencer-controlled-utility-lines]] — 那里有「`UGND` ↔ `DGND` 要不要隔离」的具体判断

## 版本

- **Introduced in SmarTest 7.2.0**

## 出处

`sources:` 一篇：
`02_System_reference/02.03_DUT_board_design_reference/02.03.07.09.04_Grounding.md`

**本页没做的**：

- **图一张没看。** 本篇有两张图（`[img]`），本页没有任何来自图的结论。
- **原文 `## Related information` 列的九篇，本页一篇都没读**：
  `Shielding and grounding`、`Importance of ground vias`、
  `DPS layout rules for high frequency designs`、`Utility lines`、
  `Signal return paths`、`RF grounding`、`Electrical design for mixed-signal testing`、
  以及三篇 `SmarTest 7: Grounding of Trigger Signals`（MCE / MCA / MCC 各一篇）。
  本页只在正文提到它们的地方照实写「见某某」，**没有替它们做任何总结**。

> **本页的性质**：它是一份**设计准则的转述**，不是设计规范。
> 原文的口径本身也是「推荐做法 / 要考虑这些」，**没有一条是「必须」**——
> 本页照这个口气写，**没有把「推荐」升格成「必须」**。

`verified: doc-only`
