---
type: constraint
title: 同步或环回的一组 pin，必须分配在同一个测试处理器上
layer: L1
stage: pin
tags: [constraint, dut-board, pogo, fast-sync, loopback, test-processor, channel-group]
related: [[pin]], [[cross-card-ganging-requires-ddic]], [[pogo-block-compatibility]], [[logical-boards]]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.01_AVI64_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.04_FVI16_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.05_PVI8_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.06_PS9G_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03.06_PS1600_SmartLoop__loopback_testing.md
  - 02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md
  - 02_System_reference/02.06_Command_Reference/02.06.09.01.02_Using_embedded_timing_and_level_search_on_a_Smart_Scale_system.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 同步或环回的一组 pin，必须分配在同一个测试处理器上

## 约束是什么

有两类场景要求**多条 pin 当作一个整体来用**：

- **快同步（Fast Sync / Fast Match）**——几条 DUT pin 的边沿要一起动；
- **环回（loopback，PS1600 的 SmartLoop）**——一条 pin 发、另一条 pin 收。

**这两类场景都有一条同样的分配要求**：这些 pin **不能随便摊在机台各处**，
必须落在**同一个测试处理器（test processor, TP）**上。

> - Pin assignment for Fast Sync / Fast Match: For fast local synchronization, the synchronized DUT pins must be assigned to the same group of channels respectively to the same test processor.

> Loopback pins must belong to the same test processor (TP).

> - The SmartLoop loopback scheme: Loopback pins must belong to the same test processor.

**这是 §2.4 的 D3（一致匹配）**——约束的不是某一条 pin 的取值，
而是**多条 pin 之间的分配关系**：它们必须"在同一个 TP 里"。

## 在什么条件下成立

**这是「DUT 板怎么布线 / 怎么分配通道」的约束，不是测试程序里的写法约束。**
它决定的是**硬件设计阶段**的事：你在画 pogo 电缆、分配通道时就要满足它，
写测试程序时已经改不了了。

**分两档，管的范围不一样**：

| 场景 | 要求 | 文档怎么写的 |
|---|---|---|
| **快同步** | 同一个 **channel group**，且同一个 **test processor** | 两项都要求（`the same group of channels respectively to the same test processor`） |
| **环回** | 同一个 **test processor** | 只要求 TP |

> **⚠️ 快同步那句的 `respectively` 是原文自己的写法**，读起来别扭
> （字面像"分别地"）。**本页照抄，不替它解释**——
> 我**不确定**它说的是"两个条件各自成立"还是别的意思。
> 能确定的只有一件：**这句同时点了 `group of channels` 和 `test processor` 两样东西。**

**`test processor` 和 `channel group` 不是一回事**：
快同步两项都要，环回只要 TP。
**本页不推断两者的包含关系**（TP 是不是由若干 channel group 组成，文档在
这几句里没说）——**§2.1：没找到就不写。**

### 覆盖范围

| 键 | 命中 | 独立文档 |
|---|---|---|
| `P-fastSync` | 15 处 / 15 行 / 15 文件 | **12 篇** |
| `P-loopback-TP` | 7 处 / 7 行 / 4 文件 | **3 篇** |

**12 篇快同步文档横跨七种卡**：AVI64、DPS128/PS64、FVI16、PVI8、XPS256、PS1600、PS9G
（`02.03.06.02.*` 与 `02.03.06.03.*` 两个子系列）。
**本次抽读了其中 4 篇，那一句逐字相同**——**同一段模板在卡之间复制**，不是各卡独立写的（§10）。

**「倍」值得记一笔**：环回只有 **3 篇**，但它才是这条约束**最具体**的用例
（`SmartLoop` 是真实存在的环回方案）；快同步 12 篇虽多，**是模板复制来的**。
**按 §10 的口径，多不等于强。**

## 违反了会怎样

> **⚠️ 本次未找到任何描述报错形态的原文。**

这批文档是**板级设计参考**，通篇讲"怎么分配"，
**没有一句写"分错了会怎样"**。本页不猜。

**这条与测试程序里的约束有个实际差别**：
程序里的错，跑起来会报错或被拒；
**板子布错了，是硬件层面的错**——同一个 TP 的约束在**物理上就不成立**了，
**改测试程序也救不回来**。**这是推断，不是文档事实，标出来。**

## 与之相邻、但**不是同一条**的三条规矩（**都不属于本页**）

这一族最容易出错的地方是：**它们共用 `belong to the same test processor` 这个谓语，
但主语和条件都不一样。** 本页把它们逐个列出来、并说明为什么**不合**进来。

### 一、Smart Scale 嵌入式搜索的 setup / result pin

> Setup and result pins are independent of each other, but must belong to the same test processor.

- **主语不同**：这里说的是**同一条搜索的 setup pin 与 result pin**，
  不是"一组要一起动的 pin"。
- **条件不同**：它成立的条件是**用嵌入式 timing/level 搜索**，
  不是"板子上有快同步或环回"。
- **出处不同**：这句话在**命令参考**（`02.06.09.01.02`）里，不在板级设计文档里。

**所以它不建在本页。** 数字：**2 处 / 1 篇**（`P-setupresult-TP`），
**只有 1 篇，不足以单独建页**——记在这里，等它凑够证据再建。

### 二、XPS256 的内存池化

> This must be taken into account when assigning the channels if, for example, very large amounts of sample data are expected for individual channels.

（上文是「XPS256 卡支持按 **8 通道一组**、在**同一 test processor 内**做内存池化」。）

- **它管的是内存，不是同步**——约束的对象是**采样数据的存放**，
  不是"几条 pin 要一起动"。
- 那句 `must be taken into account when assigning the channels` 是**提醒**，
  **语气是"要考虑到"，不是"必须满足"**——**形状上是建议，不是约束**。

数字：**3 处 / 2 篇**（`P-pooling`）。**不建页，归宿是 [[logical-boards]] 那一类对象页。**

### 三、`P-sameTP` 这个键本身是个错误

> **⚠️ 这一条是记给我自己看的，也是这一页最值钱的部分。**
>
> 上面三条规矩，原先在 `extract/rule_evidence.py` 里**只有一个键 `P-sameTP`**，
> 数出来是「**10 处 / 4 篇**」。**那个数把三条不同的规矩加在了一起。**
>
> 拆开后：环回 7 处 / 3 篇 + setup-result 2 处 / 1 篇 + 内存池化 1 处 = **10 处**，
> **正好等于旧数**——所以我拆得对，旧键确实是三合一。
>
> **判据把三件事算成一个数，是判据的错，不是语料的错。**
> 而**这个错数会一路绿着走进页面**：十三类检验里**没有哪一类在核
> 「这个计数背后是不是同一件事」**。

## 与 [[pin]] / [[cross-card-ganging-requires-ddic]] / [[pogo-block-compatibility]] 的关系

- [[pin]] 讲 pin 本身；本页讲**一组 pin 的相对位置要求**。
- [[cross-card-ganging-requires-ddic]] 讲**跨卡 ganging 之前要用 DDIC 使能连接**——
  那是"怎么把分开的连起来"，本页是"**本来就必须在一起**"。两者相邻但不同。
- [[pogo-block-compatibility]] 讲 pogo 块的密度与网格；
  **本页这条约束它一个字都没提**（建页前查过），所以不存在重复。

## 出处

| raw | 里面的原句 |
|---|---|
| `02.03.06.02.01_AVI64_pogo_pin_assignment.md` | 快同步句 |
| `02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | 快同步句 |
| `02.03.06.02.04_FVI16_pogo_pin_assignment.md` | 快同步句 |
| `02.03.06.02.05_PVI8_pogo_pin_assignment.md` | 快同步句 |
| `02.03.06.02.07_XPS256_pogo_pin_assignment.md` | 快同步句 + 内存池化句 |
| `02.03.06.03.03_PS1600_pogo_pin_assignment.md` | 快同步句 + 环回两句 |
| `02.03.06.03.06_PS9G_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md` | 环回句 |
| `02.05.04.01.03.06_PS1600_SmartLoop__loopback_testing.md` | 环回句 |
| `02.05.04.01.06_PS1600_pogo_pin_assignment.md` | 环回句 |
| `02.06.09.01.02_Using_embedded_timing_and_level_search_on_a_Smart_Scale_system.md` | **setup/result 句（不属于本页）** |

> **⚠️ 引文避开了 `02.03.06.03.06_PS9G…md` 第 74 行。**
> 那一行含 **GBK mojibake**（`SmartLoop鈩?`，§11.2 ① 记的已知瑕疵）——
> **引它会把坏字符抄进 wiki**。本页引了该篇第 78 行的干净版本
> （`02.03.06.03.06` 与 `02.03.06.03.03` 两句措辞相同，后者无坏字符）。
> **这不是"改引文"，是"换一条出处引"**——本页**不修语料**（§10）。

文档事实，`verified: doc-only`。

## 这条约束怎么被发现的

**这一族先是被"分层"卡住的**，卡对了地方。

上一批把它记成"证据够了但没建，因为横跨两层"。
这一批查清楚：**9 个 stage 页里没有"板级设计"这一档**
（`level / pattern / pin / project / results / run / testflow / testmethod / timing`），
而第一类检验的正是「**九页**与十节齐备」——**加第 10 个 stage 是改 schema，不是建页。**

**解法是先例**：`constraints/cross-card-ganging-requires-ddic.md` 也是板级/通道类约束，
它用的是 `stage: pin`、`layer: L1`。**照先例办，不动 stage 分类。**
既有的 `concepts/pogo-block-compatibility.md` 也标的是 `stage: pin`——
**房里的规矩本来就是这么定的。**

> **所以"分层问题"这一档的答案不是"新建一层"，是"先看房里已有的先例怎么放的"。**
