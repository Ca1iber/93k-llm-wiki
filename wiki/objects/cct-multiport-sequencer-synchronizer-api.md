---
type: object
title: CCT Multiport Sequencer Synchronizer API
layer: L2
stage: pattern
tags: [pattern, timing, multiport, cct, L2]
related: [pattern, timing, testflow, multiport-burst-editor, sequencer-status, play-pattern]
sources:
  - 03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# CCT Multiport Sequencer Synchronizer API

> **一句话**（原文）：*"The CCT Multi-port Sequencer Synchronizer API is an API set that is used
> to program digital multi-port bursts and handle synchronization across ports."*

入度 **43**。它是一整套 API 的**总入口页**——43 篇 L2 API 参考页在页尾指向它，
**反向说明了这一族里有哪些 API**（见下「族」一节）。

`stage: pattern` 记的是**它服务于哪一段**：主体是组装/同步**多端口 burst**（pattern 域）。
但它的前置条件横跨三段，见「前置条件」。

## 是什么

- **一整套 API**（不是单个函数），用来：编程 **digital multi-port burst**；在多个端口之间
  **保持同步**。
- 原文对同步的定义：端口间 vector/cycle 长度或执行时间不同时，**在下一个 label 开始之前**
  把各端口对齐。可以对齐的有：不同端口的 **flat pattern**；**PA transaction 序列**与普通
  pattern。
- 引用文档里的原文说明：这是一个 **CCT（Concurrent Test）** 场景下的 API 集，
  必须在 **Concurrent Test Framework** 环境里用。

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,538 字符逐字取自** `<03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>` 及其子主题 `<03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Using the CCT Multi-Port Sequencer Synchronizer API）

Example code for checking the transaction port against the multi-port burst:

```
CCTMultiportSync Sync;
Sync.registerSyncPort(Lshift::getInstance(tsName));
Lshift::getINstance(tsName).write(0x18, 0x22);
Lshift::getINstance(tsName).write(0x18, 0x86);
Lshift::getINstance(tsName).read(0x18, "readID1");
Lshift::getINstance(tsName).readExpect(0x18, 0xFE);
Lshift::getINstance(tsName).getReadValue("readID1") //get the read value marked as "readID1"
```

### Example（取自子主题 Using the CCT Multi-Port Sequencer Synchronizer API）

Code example for adding a sequencer鈥慶ontrolled DC to an assigned port:

```
CCTMultiportSync Sync;
DCDynamicPort::getInstance().setPort("pPPMUDC");
Sync.registerSyncPort(DCDynamicPort::getInstance());
DCDynamicPort::getInstance().PPMU_Relay("DC_Pin1", "PPMU_ON", 20 ns);
DCDynamicPort::getInstance().PPMU_Setting_VForce("DC_Pin1", vin V, 10 mA, -12 uA, 12 mA, 10 ns);
DCDynamicPort::getInstance().PPMU_Relay(MeasPin, "PPMU_ON", 20 us);
DCDynamicPort::getInstance().PPMU_Setting_IForce(MeasPin, "CLAMP_ON", 0 uA, 100 uA, -1 uA, 1 uA, 0.002 ms);
DCDynamicPort::getInstance().PPMU_VClamp(MeasPin, "CLAMP_ON", 0, 4 V, 0.1 us);
DCDynamicPort::getInstance().PPMU_Meas(MeasPin, "VMUM", "PVAL", 2, 10 ns);
```

### Example（取自子主题 Using the CCT Multi-Port Sequencer Synchronizer API）

Code example for adding a dynamic DC test to an assigned ports:

```
CCTMultiportSync Sync;
DCDynamicPort::getInstance().setPort("pDPS128");
Sync.registerSyncPort(DCDynamicPort::getInstance());
DCDynamicPort::getInstance().DPS_MeasVoltageRange(mDpsPins, 3.0);
DCDynamicPort::getInstance().DPS_Force("DPS128_2"), vin, 50 mA);
DCDynamicPort::getInstance().DPS_MeasVoltage(mDpsPins, 2);
```

<!-- 语法节 end -->

## 能力（Key features，逐字归类）

**同步类**

- 自动维持跨端口同步：对齐 vector/cycle 长度或执行时间不同的端口
  （flat pattern 之间；PA transaction 序列与普通 pattern 之间）
- 在 pattern 里**插入 sequencer 控制的 DC 测试**（必须指定同步点，才能和别的端口对齐）
- 在 pattern 里**插入 DC Dynamic 测试**并与其他端口的 pattern 保持同步
- 按 analog sequencer group / analog sequence program，在指定端口生成 trigger pattern
  或 PA transaction 序列，再与其他端口同步
- 支持在**不同 digital capture 端口**上做多个 digital capture（`DigitalCapturePort`）

**读写类**

- 用预定义协议对 DUT 做 write to / read to / read from（可用 protocol-aware 方法），
  **不同 site 可以给不同的值**

**组装与工程性**

- 把 digital capture pattern 插进 multiport burst，并**自动生成对应的 `VECTOR_VARIABLE`**
- 为协议活动提供**统一的 wrapper API**（走 PA）
- 工程模式与生产模式之间**平滑切换**
- **可视化** multiport 组装
- 在多端口 burst 的某个端口上创建并插入 flat label；在 multiport burst 的 HIF 端口上
  生成并附加 protocol-type label

## 支持的硬件与授权

- 普通 digital pattern：**所有 smart scale 数字卡**都能用
- **API 本身不需要专门 license**；但要在 multiport burst 里附加 *protocol type labels*，
  **需要 protocol-aware license**

## 同步是怎么做的（原文机制，照述）

1. 先用 API 建 flat pattern
2. 给 burst 的某个端口加 **flat label**，或附加 **protocol type label**
3. 每个端口 label 的**长度/执行时间被记录下来**，算出端口间的执行时间差
4. 需要同步时，对**执行时间短的那个端口**追加「rep Idle 向量」（普通端口）或 **`IDLE` 命令**
   （transaction 端口），使各端口 sequencer **同时结束**
5. 同步之后，各端口的下一个 vector **同时开始**

- **端口必须先 register**。API 通过查询每个 label 的 cycles 和 period 来跟踪已注册端口的
  执行时间。
- **同步是用户发起的**（原文 *"The synchronization activity is user-initiated"*）。
- **计算式**（原文）：设端口 i 的执行时间为 `T@Port<i>`，最大值为 `Tmax`，
  则 API 给 `T@Port<i> < Tmax` 的端口追加：
  - **Dummy cycles**（普通 pattern），或
  - **`IDLE` 命令**（PA 端口），时长 `deltaT@Port<i> = Tmax - T@Port<i>`
- 也可以**自己指定同步点** `Tsync`：给 `T@Port<i> < Tsync` 的端口追加同样的东西，
  时长 `Tsync - T@Port<i>`。同步点之后，新加 label 的已注册端口**同时开始下一个 vector**。

**multi-port burst 的组装不要求它当时已存在**：burst 可以先被分配，同步端口和 single-port
label **之后再加**。（原文 *"It is not necessary that the multi-port burst exists when it is
assigned."*）

## 前置条件（文档事实 —— 这是硬约束，`Prerequisites` 段原文）

> Before you can use the CCT Multi-port Sequencer Synchronizer API, make sure that the
> following conditions are met:

1. **Digital pattern must be multi-port based** —— 数字 pattern 必须是多端口结构 → [[pattern]]
2. **Timing set must be multi-port based** —— timing set 必须是多端口结构 → [[timing]]
3. **Must be used in Concurrent Test Framework environment** —— 必须在并发测试框架环境下
   → [[testflow]] / [[run]]

三条缺一不可。第 3 条是**环境级**要求，写测试程序之前就得满足，不是调用时能补的。

## 限制（`Limitations` 段原文，全部是「不支持」）

- 数字 pattern 里含 **CTIM / CLEV** 的端口**不支持**
- **D2S 不支持**
- **BADC 不支持**

## 族：哪些 API 属于这一套

下面是「页尾反向指回本页」的 L2 API 参考页（`02.07.04.01.*`）——
**这张表的来源是链接结构，不是任何一句原文**（那 43 篇的引用形式全是页尾的相关链接，
**没有一句解释关系的散文**）。名单照抄，不做归类推断：

`CCTMultiportSync()` / `.start()` / `.sync()` / `.flush()`；
`registerSyncPort()`；`registerCCTestMethod()`；`release()` - CCTMultiPortSync；
`SynchronizedPort& setPort()` / `setIdentifier()`；
`PatternPort& getInstance()` / `releaseInstance()` - PatternPort API；
`DCDynamicPort& getInstance()` / `releaseInstance()` - DCDynamicPort API；
`DigitalCapturePort& getInstance()` / `setDefaultPattern()` / `setDefaultPattern() - Repeat` /
`releaseInstance()` - DigitalCapturePort API；
`AnalogSeqGroup()`；`attachPA()`；`Capture()`；`Trigger()`；`playPattern()`；
`dumpMPBGraph()`；`setAWG()`；`setDGT()`；`setMeasDef()`；`setStimDef()`；`setWaveTable()`；
`setWaitTemplatePatternName()`；
`PPMU_Meas()` / `PPMU_IClamp()` / `PPMU_VClamp()` / `PPMU_Relay()` /
`PPMU_Setting_IForce()` / `PPMU_Setting_VForce()`；
`DPS_Force()` / `DPS_MeasCurrent()` / `DPS_MeasVoltage()` / `DPS_MeasCurrentRange()` /
`DPS_MeasVoltageRange()`

> 这 40 多条**不建页、也不链接**（`schema.md` §12：只为高入度对象建页）。
> 名字留在这里是为了让人能照着去 raw 里搜。已建 / 已排队的相关页是
> [[multiport-burst-editor]]、[[sequencer-status]]、[[play-pattern]]。

**Limitations 与族的交叉点**：族里同时有 PPMU / DPS 的强制与测量 API，而限制里写了
D2S、BADC 不支持——**哪些组合能一起用，本页不推断**，需要时读各自的成员页。

## 版本

- **Introduced in SmarTest 7.3.2**（`Functional changes` 段，仅此一条）

本 wiki 面向 **7.10.3**，该 API 集在。

## 出处

- 定义文档：`03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md`
  （TDC `148142.htm`，5,717 字节）
- 入边 43 篇：`extract/pack/02-cct-multiport-sequencer-synchronizer-api.md`
- ⚠️ **语法节的来历要更正**（2026-09-18）。本页初版这一节写的是
  **「这一页没有……定义文档里没有 `Syntax` / `Parameters` 段落，所以不写语法」**——
  **那是从「抽取器抽不到」推出来的，不是从文档读出来的。**
  抽取器当时会把 `## Examples` 底下的 `### 子段` 整段丢掉；修好之后本节收到
  **子主题 `Using the CCT Multi-Port Sequencer Synchronizer API` 里的三段代码**
  （寄存器读校验 / 给已分配端口加 DC / 加 dynamic DC 测试）。
  **注意：这三段仍是「用法示例」，不是签名表**——签名在成员页上，本页的定性没变。
- ⚠️ **那三段代码里有两处语料本身的毛病，照录不改**：
  ① `sequencer鈥慶ontrolled` 是**编码损坏**（`鈥慶` 是 `–c` 的乱码形态，
  同族还有 `鈥慴`/`鈥慸`/`鈥慼`），原文此处应为 *sequencer–controlled*；
  ② `DCDynamicPort::getInstance().DPS_Force("DPS128_2"), vin, 50 mA);` **括号位置不对**
  （`DPS_Force(...)` 后多一个 `)`，逗号落在括号外），照字面抄**编译不过**。
  另有 `getINstance` 大小写不一致（同段里 `getInstance` / `getINstance` 混用）。
  **这三处都是原文自带的**，不是本页转录错——**照录，不替文档改**（§11）。
- 本页 `verified: doc-only` —— 只在 TDC 文档里确认存在，未在任何真实机台上调用过。
  **「文档里有」≠「这台机器上能用」**（§11）。
