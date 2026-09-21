---
type: object
title: Utility line assignments
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05.05_Internal_utility_power_supply__V93000_systems.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Utility line assignments

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**utility line（实用线）** 是 V93000 基础设施暴露到 DUT 接口上的一批通用信号线。
它们**全部可读可写**，被路由到 DUT 接口上的 **utility pogo block**。

**一个 utility pogo block 装 16 根线（编号 00–15）或 32 根线（00–31）。**
选哪种块，取决于 DUT 接口的大小：

| DUT 接口 | 块型 | pogo 针数 | DUT 接口上的总线数 |
|---|---|---|---|
| 所有 small DUT interfaces | 16 线 / 2 排 | 34 | **64** |
| DUT Scale / large，2 排 | 16 线 / 2 排 | 68 | **128** |
| DUT Scale / large，4 排 | 32 线 / 4 排 | 68 | **256** |

**用满 256 根线要求 4 排块 + SmarTest 7.2（或更高）。**

4 排块的**额外 pogo 针不只是多出来的线**，还带来 **External utility power supply**
（V93000 systems）的供电线——**外部 utility 电源只能从 4 排 utility pogo block 上取**。

**内部 utility 电源**走的是另一个针：**utility pogo block 的 `UP5V` 针**。
具体有几个电源、每个电源喂几个块，随 test head 类型与 DUT 接口类型变
（原文表：A-test head / Compact / Small / Large 各自几路、每路覆盖 1、2、4 或 8 个块）。
输出电压也不是固定值——**同一路电源的输出电压取决于供电卡笼里 slot 一、二里插的是什么卡**
（原文给的两档是 `4.85 V +1%, -5%` 与 `4.85 V +1%, -20%`，条件不同）。

**线的电气特性**由三件事决定：**线数**、**控制方式**、**输出/输入电路的电气特性**。
其中一处最容易踩的是**内部上拉电阻**：

- **EXA Scale 系统**：未激活的线（low-side 开关断开）**一律上拉到 +3.3 V**。
- **Pin Scale / Smart Scale 系统**：上拉配置**取决于 test head 类型与 wiring board 类型**
  （原文表按 ATH / CTH 等逐行列；例：ATH + 任意板 → 全部线 + 任意块，上拉到 `+3.3 V`）。

**utility pogo block 提供的不只是 utility line**，还有 utility 电源和 V93000 基础设施的
其他资源。**哪些块可用、怎么配，取决于系统类型 + test head 类型 + DUT 接口类型三者。**

> **EXA Scale 的基础配置**：每卡笼 **32 根静态控制的 utility line + 一个 +5 V utility 电源**。

## 典型用法

**1. 本页是「线在哪、有几根、上拉到哪」的查询面**，落在 [[pin]] 阶段。
它与 [[pin]] 页的 [[pin-configuration-file]] / pogo 块分配是同一条链路的两端：
**pin 页管信号通道，本页管基础设施通道**。

**2. 数的口径要对齐。** 问「这台机器有几根 utility line」时，
必须同时给出 **DUT 接口类型**与**块型**——64 / 128 / 256 三个答案都可能是对的。

**3. 要外部 utility 电源就必须上 4 排块。** 这条是硬约束：
外部电源的线**只出现在 4 排块的额外针上**。

**4. 想让 utility line 与 pattern 同步，本页不够。**
静态访问（本页描述的默认形态）**不能**与 pattern 同步；
要同步得走 **dynamic access**，见 [[sequencer-controlled-utility-lines]]。

## 和谁有关

- [[pin]] — 同属 pin 阶段；pogo 块与引脚分配的另一半
- [[sequencer-controlled-utility-lines]] — utility line 的**动态访问**：由 pattern sequencer 控制
- [[logical-boards]] — pogo 块地址与 virtual pogo block 的概念；**一个物理块超过 16 通道就要多一个地址**
- [[sharing-configuration-file]] — 那份文件里有 `utility-line-assignments` 相关字段（该页 `related` 已列本页）
- [[dps128-dps64-cards]] — 同类「卡 ↔ pogo 块 ↔ DUT 接口」的对应关系，可对照读

## 版本

- 4 排 utility 块（256 线）要求 **SmarTest 7.2 或更高**
- 本篇四份文档中，`Utility line assignments` 与 `Utility line characteristics` 的
  `## Functional changes` **本次未读到引入版本**——**本页不填**，要版本号请回 raw 查
- EXA Scale 的 utility line 行为与 V93000（Pin Scale / Smart Scale）**不同源**，
  原文用的是两篇并列的文档（`Utility lines (V93000 EXA Scale systems)` / `(V93000 systems)`）

## 出处

`sources:` 里四篇：

| 文档 | 讲什么 |
|---|---|
| `…/02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.md` | 线数、块型、64/128/256 的由来、外部电源只在 4 排块上 |
| `…/02.03.04.02_Utility_line_characteristics.md` | 电气特性、上拉电阻规则、TH × DUT IF 兼容性 |
| `…/02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.md` | 各 TH / DUT IF 下的 utility pogo block 配置；EXA 基础配置 |
| `…/02.03.05.05_Internal_utility_power_supply__V93000_systems.md` | 内部 utility 电源：`UP5V`、路数、输出电压两档 |

**本页没做的**：

- **每个 TH / DUT IF 组合的完整配置表没抄。** `02.03.06.08` 底下挂着九个子主题
  （Basic configuration / Utility Card / LTH / STH / CTH / ATH × DUT Scale × small），
  本页只写了**共同的规则**。
- **上拉电阻表只举了一行**（ATH）。**其余行未抄**——要用请回 `02.03.04.02` 看原表。
- **内部电源那张表只说了形状，没抄数字**（几个电源、覆盖几个块、四种 test head 的差异）。
- **`Grounding` 不在本页**，它是单独一页：[[dut-board-grounding]]。

`verified: doc-only`
