---
type: object
title: DC Scale DPS128/DPS64 cards
layer: n/a
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01_DC_Scale_DPS128_DPS64_cards.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01.03_DPS128____PS64_functionality_and_features.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01.04_DPS128____PS64_hardware_overview.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128____PS64_power_budget.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# DC Scale DPS128/DPS64 cards

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **160 字符逐字取自** `<02_System_reference/02.05_Test_Head_Cards/02.05.05.01_DC_Scale_DPS128_DPS64_cards.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| DPS128‑HC | E8023CS | 128 HC channels | 1.0 A | -2.5 V ... +7.0 V |
|---|---|---|---|---|
| DPS64‑HC | E8023CSH | 64 HC channels | 1.0 A | -2.5 V ... +7.0 V |

<!-- 语法节 end -->

## 是什么

`DPS128` 与 `DPS64` 是 **DC Scale 电源卡**家族里的两块卡，**可插任意 I/O channel card slot**。

每路通道能：在设定电压下 source / sink 电流、测量供出的电压与电流、
给 DUT board 上的外部电路供电、在 test suite 里为某个测试编程、
在 site 之间共享（channel sharing）、ganging 起来加大供出电流、
做连通性检查、查器件电源的状态。

**两个变体**（原文表格，逐格照抄）：

| 变体 | 订货号 | 通道 | 电流 | 电压 |
|---|---|---|---|---|
| `DPS128-HC` | E8023CS | 128 HC channels | 1.0 A | -2.5 V ... +7.0 V |
| `DPS64-HC` | E8023CSH | 64 HC channels | 1.0 A | -2.5 V ... +7.0 V |

> ⚠️ **语料里这两行写的是 `DPS128鈥慔C`。这是编码损坏，不是我转录错。**
> 逆推回原始字节是 `DPS128` + **U+2011（不换行连字符）** + `HC`。
> 同批损坏还有 `pull鈥憉p`（= `pull-up`）、`low鈥憇ide`（= `low-side`）、
> `1 鈥?nbsp;16`（= `1` `–` `16`）。
> **本页写成普通的 `-`。回 raw 搜 `DPS128-HC` 是搜不到的，要搜 `DPS128鈥慔C`。**
> （文档标题那处损坏更重——`DPS128鈥?鈥奃PS64` 里有一个字节已经丢了，
> **原文到底写的是哪个字符无法还原，本页不猜**，正文一律直接写 `DPS128` 和 `DPS64`。）

**两种工作模式**：`DPS+`（DPS operating mode）与 `SIG`（PMU operating mode）。
前者当标准 DPS 用，在 testflow 执行期间给器件供电；后者当标准 PMU 用，
临时给单个或一组 test suite 供电。**一个通道只能配成其中一种，不能同时两种。**
原文写明 **DPS operating mode 是 PMU operating mode 的超集**，多出来的能力是：
只有 DPS 模式下这两块卡才能**参与 connect / disconnect 序列**、才能**参与 set activation**。

**硬件尺寸的对应关系**：DPS128/DPS64 **每个 logical board 对应一个 channel module**。
HC 模块顺序是 A、B、C、D，HV 模块是 H、G、F、E（见 [[logical-boards]]）。

**功耗预算**：整卡原始电压供应最大 **426 W**，**均分给两个 power domain**，
每域 **213 W**，由 64（DPS128）或 32（DPS64）个通道的输出级共享。
SmarTest 限制总功耗，**超了报错**。

原文特意强调一句，读功耗数字时最容易漏：**这个预算是「输出级上」的，不是「DUT 上」的**——
算单通道总功耗时还要加上输出级的内部损耗、内部测流电阻上的损耗、内部走线与 pogo cable 的损耗。
文档因此建议用 **DC Scale DPS128 Power Calculator** 来算总功耗和预算占用率。

**电压范围限制**：用到 1 A 电流的通道必须设电压范围。
**小于 2.25 V 的范围一律映射到 2.25 V**；2.25 V 到 7 V 之间有 256 档，约 18 mV/档。

**pogo cabling 要在 model file 里配对**：各种 pogo cable assembly 让 DPS128/DPS64
的 DUT board 与 DPS32、MS-DPS 兼容，**每种 assembly 都要在 [[model-file]] 里写对应的
`POGOCABLING` 条目**（原文的 `E8023PA` / `E8023PB` 对照表见「出处」列的那篇）。

## 典型用法

**1. 它落在 [[level]] 阶段。** 这是一张电源卡，执行的是 level setup 要的那些电压/电流。
本页 `stage: level` 由此而来。（**推断**：原文没有一句「本卡属于 level 阶段」；
这是按「它在流程里被谁驱动」定的，判据见 `schema.md` §6。）

**2. 按 power domain 分配通道**，否则会撞功耗限制。原文给了
power domain ↔ channel module ↔ pogo block ↔ 通道号 的完整映射表
（例：domain 1 含 module A/B 与 E/F；`DPS64` 上 module E–H 是 `n/a`）。

**3. 高电流通道相应压低电压范围**，以减小消耗的功率。

**4. ganging 的物理并联做在 DUT board 上**，软件侧用 **Pin configuration tool** 建 gang。
可以 gang **任意多路相邻通道**。

**5. 在 Hardware view 里做 profiling。** `Profile` 字段能在 pattern 执行期间测量并显示
电流/电压波形；`Surge Tracker`、`ADC` 也是交互字段。底层序列还会在 `Sample Code view` 里
**生成对应的 test method 示例代码**，可以直接拷进 test method 程序。

**6. channel sharing 省通道**：同一路 DC Scale 通道可以在多个 site 之间共享，
用来省 DPS 通道、也给 DUT board 上的外部电路供电。

## 和谁有关

- [[level]] — 本卡是 level setup 的电源执行者；本页的 `stage` 字段来源
- [[logical-boards]] — 一个 channel module 一个 logical board；通道地址与 virtual pogo block 的概念在那里
- [[pin]] — pogo 块与引脚分配；ganging 的软件侧入口是 Pin configuration tool
- [[dps-aux-pin-task]] — L2 侧读这张卡电源状态 flag 的那一族
- [[xps256-programming-dps-operating-mode]]、[[xps256-pmu-operating-mode]] — 同属「电源卡 × 两种工作模式」这一族，**可对照读**
- [[model-file ]] — pogo cabling 的 `POGOCABLING` 条目写在这里

## 版本

- **Introduced in SmarTest 7.2.1**
- **7.2.2**：支持 `DPS128-HC/HV` 与 `DPS128-HV`
- **7.3.2**：DPS128/DPS64 hardware views 增加 `Load Capacitance` 字段

## 出处

`raw` 里定义这张卡的**五篇**（`sources:` 列了全部五条）：

| 文档 | 讲什么 |
|---|---|
| `02_System_reference/02.05_Test_Head_Cards/02.05.05.01_DC_Scale_DPS128_DPS64_cards.md` | 总览 + 变体表 |
| `…/02.05.05.01.03_DPS128____PS64_functionality_and_features.md` | 功能全集 + 两种工作模式 + ganging + channel sharing |
| `…/02.05.05.01.04_DPS128____PS64_hardware_overview.md` | 模块顺序 + Hardware view |
| `…/02.05.05.01.05_DPS128____PS64_power_budget.md` | 426 W / 两个 domain / 电压范围映射 |
| `…/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.md` | pogo cable assembly ↔ model file 条目 |

**本页没做的**（读者别当本页说过）：

- **规格数字没取。** 每卡最大 source/sink 电流等在 `02.05.05.01.02_DPS128____PS64_specifications.md`，
  **本次未读**，所以本页只写原文这几篇里出现的数字。
- **功耗计算器没读**（`02.05.05.01.05.01_DC_Scale_DPS128_Power_Calculator.md`）。
  本页只能转述「文档建议用它」，**不能替它算**。
- 本页的表格是**逐格照抄**的，但表格在语料里是**断行的**（每格一行、行间空行），
  本页还原成标准 markdown 表——**格子内容逐字，排版是我重排的**。

`verified: doc-only`
