---
type: object
title: Maintenance operations
layer: n/a
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Maintenance operations

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,533 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Structure example

This example assumes a maintenance operation period taken from the data sheet of a memory device with a maintenance operation period of 300 ns. The test system cycle period is 100 ns. This causes a maintenance operation subroutine to be called on test system cycles 3, 6, ... as shown in the example below.

 !`Maintenance operation example with test system cycle of 100ns`（raw: `../../../../raw/75962.png`）

If the test system cycle period is reduced to 50 ns and the maintenance operation period remains 300 ns long, the maintenance operation subroutine is called on test system cycle number 6 as shown in the example below.

 !`Maintenance operation example with test system cycle of 50ns`（raw: `../../../../raw/75963.png`） Note The maintenance operation period numbers in the above examples differ from the numbers for common memory devices. They are used just to explain the maintenance operation concept.

### Code example

```
main ()
{
  // write device
  for (rowAddr=0 ; rowAddr<rowMax; rowAddr+=1)
  {
    // no maintenance operation allowed during full device write
    is {}
    for (colAddr=0 ; colAddr<colMax ; colAddr+=1)
    {
       write (rowAddr, colAddr, data);
    }
  }

  // read device
  for (rowAddr=0 ; rowAddr<rowMax; rowAddr+=1)
  {
     // no maintenance operation allowed during burst read
     // maintenance operation can occur in between bursts
     for (colAddr=0 ; colAddr<colMax ; colAddr+=burstLength)
     {
       is {}
       read_burst (rowAddr, colAddr, data);
     }
  }
}
```

<!-- 语法节 end -->

## 是什么

原文的定义：

> 「**Maintenance operations are procedures that need to be performed regularly during the testing
> of a device, most commonly refreshes.**」

对存储器件来说就是**刷新**。它由两样东西拼成：

- **一串 vector**（由器件访问和其他指令编译而来）——要执行的动作本身；
- **一个 interval**——多久执行一次。

**关键在最后半句**：MTP 拿着这两样信息**自己排期**，
`avoiding any need for you to insert them manually into your test patterns.`
**你不用手工往 pattern 里插刷新**——这正是这套机制存在的理由。

因为刷新**只能落在测试的特定位置上**（见下面的 `is{}` / `nis{}`），
原文说 MTP 另配了**一批特征**来控制「刷新能出现在哪、不能出现在哪」，
以及**影响它的自动排期**。

### 周期（maintenance operation period）

**两次执行之间想要的间隔**。写在 **Timing file** 里：

| 关键字 | 用于 |
|---|---|
| **`maintop_time_a`** | **单次**刷新 |
| **`static_maintop_time_x`**（`x` 任意字母） | **多次**刷新 |

**边界**：**最长 9.2 秒**（原文：`2^28 times the test system period`）；
**最短 16 倍 test system period**。

> ⚠️ **上面这两个数本页没有替它换算。** 原文把「9.2 秒」和「228 × test system period」
> 并列写在同一句里，**但本页不知道这里的「test system period」指哪个周期**，
> 所以**不去反推它**。**要用这个上限，请回原文确认这个 period 的定义。**

### 两种操作类型

| | 单次刷新 | 多次刷新 |
|---|---|---|
| 一次 pattern 执行里 | **只刷一次** | **刷不止一次** |
| 支持它的 timer mode | **static 和 dynamic 都支持** | **只有 static 支持** |
| multiport | 单次 static 刷新**单端口和多端口都支持** | 多次 static 刷新**同样两者都支持** |
| 附加限制 | — | 可以**从一次刷新切到另一次刷新**，但**任一时刻只允许一次刷新在跑** |

### 什么时候真的刷：靠波形类型触发

**触发判据是波形类型，不是时间到了就刷**：

> 「If the **refresh counter reaches zero**, the refresh is executed at the
> **next interruptible waveform** in the pattern stream.
> (**Interruptible waveforms have an index below `0x80`.**)」

**这里有个硬前提**：需要**复制过的 wavetable**（replicated wavetables）——
**每个波形在里面出现两次，一次是正常（可打断）形态，一次是不可打断形态**。
（怎么做见 `Wavetables for maintenance operations`，**本页没读那篇**。）

**vector 模式**下你要显式指定哪些地方可以打断：
在 **pin mapping file** 的 `using interruptCtrl` 语句里写 **`VEC`**，
或把 **`interrupCtrl`** pin 属性设成 `VEC`。

> ⚠️ **上面这一句里，同一个属性出现了两种拼法**：`interruptCtrl` 与 `interrupCtrl`
> （**差一个 `t`**），**而且就在相邻的两个短语里**。**本页两个都照抄了，没有替它统一。**

### `is{}` 与 `nis{}`：哪些地方可以打断

- **`is{}`**：程序**总体不可打断**，**只有被 `is{}` 标出的位置可以**。
  **花括号里必须是空的**（`is{} must be empty between the curly braces.`）。
- **`nis{}`**：程序**任何位置都可以打断**，**除了花括号里的那些语句之间**。

**两条硬约束：**

1. **一个程序里只能有 `is{}` 或 `nis{}` 之一，不能两个都有。**
2. **sequencer 模式的引脚，程序里只能出现 `is{}`。**

### timer mode：static 与 dynamic

| | **static（静态）** | **dynamic（动态）** |
|---|---|---|
| 在哪 | **编译进 pattern** | 由**硬件计数器**执行，SmarTest 在运行时施加 |
| 落在哪 | 原文说好处是**可在 tester cycle 之间**可用 | **只能在 tester cycle 边界上** |
| 改设置 | **每次改周期/间隔都要重新编译** | **不用重新编译** |
| 支持的类型 | 单次 + **多次** | **只有单次** |
| 端口 | 单端口 + 多端口 | （原文未列） |
| 怎么声明 | Device architecture file 里 `:timerMode:` 写 `static`；时序信息用 `:timing:` 加进 APG pattern file | — |

**两条独立的禁令，别混在一起：**

- **static 刷新不能和 accumulated interval mode 一起用。**
- **dynamic 模式不支持 DC Scale 卡 DPS128/64。** ← 这一条是**卡级**的限制，
  和 [[dps128-dps64-cards]] 那张卡直接相关。

### interval mode：compensated 与 accumulated

两种模式**差别在「从哪儿起算」**：

| | **compensated（补偿）** | **accumulated（累积）** |
|---|---|---|
| 起算点 | **memory pattern 的开头**，往后加维护周期 | **上一次维护操作实际发生的时刻** |
| 300 ns 周期下的例子 | 落在 300 / 600 / 900 ns…… | 第一次仍排 300 ns；若 300 ns 处有不可打断序列、实际 380 ns 才开始，**下一次从 680 ns 算起**（380 + 300） |

- **`accumulated` + static 刷新需要 `HSM3G` 或 `HSM6800` 卡。**（又一条卡级前提。）
- 写在 **device architecture file** 的 **`:intervalMode:`** 关键字里。

### PMU 型 DC event 会打断 pattern

> 「The **PMU type of DC events** causes the execution of the pattern to be interrupted.
> These interruptions can take **up to 1.3 ms**, which **may exceed the maximum refresh
> interval for the DUT**.」

**原文的建议是**：用了 PMU 型 DC event，**写 pattern 时要把这个效应算进去**。
（这和上面的 `## Functional changes` 里 `MTP 3.0.1: PMU type DC events may prevent timely
refreshes` 是同一条。）

## 典型用法

**1. 一篇文档，四个环节**：**周期**（Timing file）→ **类型**（单次/多次）→
**能不能打断**（`is{}` / `nis{}`）→ **排期方式**（timer mode × interval mode）。
四个环节各有自己落脚的**文件**，见下面「和谁有关」。

**2. 挑配置时的次序建议**（本页给的读法，不是原文的清单）：
先定 **static 还是 dynamic**（这一步就砍掉了「多次刷新」或砍掉了 DPS128/64）；
再定 **compensated 还是 accumulated**（选 accumulated + static 就要 HSM3G/HSM6800）；
最后才是周期数字。

**3. 两个例子**（原文 `## Examples` 给了，**上面语法节里是脚本逐字抽的，本页不重复**）：

- **Structure example**：周期 300 ns、测试系统周期 100 ns 时，维护子程序在**第 3、6……个
  cycle** 被调用；把系统周期缩到 50 ns 而周期仍是 300 ns，子程序改在**第 6 个 cycle** 调用。
  **原文特意声明这两个数只用于解释概念、和常见存储器件的数字不同。**
- **Code example**：一段 `main()`，用 `is {}` 把**整块 device write** 和
  **每次 burst read** 标成不可打断，注释写明 `maintenance operation can occur in between bursts`。
  **本页没有重复它**——要看去上面语法节或 raw。

**4. 什么时候**：写存储器 pattern、或查「刷新为什么没按时发生」时。

## 和谁有关

- [[dps128-dps64-cards]] — **dynamic 模式不支持这张卡**（原文点名 `DPS128/64`）
- [[pattern]] — 本页 `stage: pattern` 的理由：刷新的载体是 pattern，排期也是排进 pattern
- [[timing]] — `maintop_time_a` / `static_maintop_time_x` 写在 **Timing file** 里
- [[pin]] — `VEC` 写在 **pin mapping file** 的 `using interruptCtrl` 语句里；
  这是引脚属性，属 pin 阶段
- [[device-architecture-file ]] — `:timerMode:` 与 `:intervalMode:` 写在这里
- [[apg-pattern-file ]] — `:timing:` 加在这里
- [[waveform-mapping]]（**未建**）— 原文 `Related information` 里**只列了这一篇**；
  波形与 index `0x80` 的关系在那边
- [[mtp-shared-test-commands]]、[[mtpt]] — 同批建的另两页 MTP 页
- [[error]]（**未建**）— 刷新没按时发生属于哪一类，本页不判

## 版本

**⚠️ 这一节同样是 MTP 版本号，不是 SmarTest 版本号**（和 [[mtp-shared-test-commands]] 同一个坑）。

- **`Introduced before SmarTest 6.3.2`**（原文就写了「before」，**没给准确版本**）
- `MTP 3.0.1`：**dynamic refresh 新增 sequencer 模式**
- `MTP 3.0.1`：**PMU 型 DC event 可能使刷新不及时**
- `MTP 3.0.1`：维护操作**可以在程序控制下启用/禁用**
- `MTP 3.0.3`（MTP on SOC 103.0.0）：**sequencer 模式在 MTP on HSM 和 MTP on SOC 上都可用了**
- `MTP 3.1.6`（MTP on SOC 103.3.0）三条：**多次 static 刷新两边都可用**；
  **static 刷新支持 multiport**；**新增关键字 `static_maintop_time_x`**

## 出处

`sources:` 一篇：
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md`

> **本页 `stage:` 与 `extract/wiki-plan.csv` 里写的不一致**：plan 里是 `testmethod`，
> 本页改成了 **`pattern`**。理由是**文档自己的落脚点**：
> 它的 `Related information` 只列 `Waveform mapping`；
> 它的四个子主题分别讲 APG program file、wavetables、Timing file；
> 它的 `## Functional changes` 一多半在讲 pattern 侧的 keyword。
> **plan 里那个值是本 wiki 生成骨架时的默认，不是文档事实**——这里改成事实那一侧，
> 记在 `wiki/log.md`。

**本页没做的**：

- **四个子主题一篇都没读**：
  `Setting up a maintenance operation`、
  `Enabling and disabling maintenance operations in APG program file`、
  `Wavetables for maintenance operations`、
  `Reusable maintenance operations`。
  **所以「怎么一步步配」本页没有**——本页只有概念和约束。
- **两张图一张没看**（`75884.png` 的维护周期示意、`75962.png` / `75963.png` 的两个例子图）。
  本页对 Structure example 的描述**只来自原文的文字**，**没有任何来自图的结论**。
- **`Related information` 只列的一篇 `Waveform mapping`，本页没读。**
- **七篇被正文链接的文档本页没读**：`Timing file`、`Pin mapping file syntax`、
  `Other control structures`（`is{}` / `nis{}` 的细则在那里）、`Device architecture file`
  及其 `…syntax`、`APG pattern file`、`Wavetables for maintenance operations`。
- **`HSM3G` / `HSM6800` 两张卡是什么，本页一个字都没有**（原文只给了型号名）。
- **语料里有一处错拼**：`Static mode supports:` 那一条下面写的是
  **`Both singel-port and multiport operations.`**（**`single` 拼成了 `singel`**）。
  **这一处在正文里，语法节没有收它**（上面那一节只收了 `## Examples`），
  所以**本页正文统一写成 `单端口`，那个错拼没有出现在本页任何地方**——
  **要引用就回 raw 引原文。**

`verified: doc-only`
