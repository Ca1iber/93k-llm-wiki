# 建页资料包 02 — 03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md

## 0. 元信息

- 标题（frontmatter）：CCT Multiport Sequencer Synchronizer API
- H1：CCT Multiport Sequencer Synchronizer API
- 字节：5717；出度：4；入边：43
- frontmatter：`{"source_html": "03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.htm", "source_topic": "148142.htm", "title": "CCT Multiport Sequencer Synchronizer API"}`
- 标题结构：CCT Multiport Sequencer Synchronizer API / Subtopics / Key features / Supported hardware / Synchronization across ports in a multi-port burst / Prerequisites / Limitations / Related information / Functional changes

## 1. 定义文档全文（raw，禁止修改）

```markdown
---
title: "CCT Multiport Sequencer Synchronizer API"
source_topic: "148142.htm"
source_html: "03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.htm"
---
# CCT Multiport Sequencer Synchronizer API

#### Subtopics

- [Using the CCT Multi-Port Sequencer Synchronizer API](<03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md>)
- [CCT multi-port user interface APIs](<03.03.05.09.02_CCT_multi-port_user_interface_APIs.md>)

The CCT Multi-port Sequencer Synchronizer API is an API set that is used to program digital multi-port bursts and handle synchronization across ports.

## Key features

The key features of the API set include:

- Automatically maintain synchronization across ports by synchronizing ports with different vector/cycle lengths or execution time before the start of the next label. You can synchronize:

  - Flat patterns at different ports
  - PA transaction sequences and normal patterns

- Execute the following read/write actions on a DUT using a predefined protocol (You can use the protocol-aware method):

  - Write to
  - read to
  - read from

You can specify different values for different sites.

- Insert sequencer鈥慶ontrolled DC tests into the pattern (You must assign a synchronization point to align with other ports).
- Insert DC Dynamic tests into the pattern and maintain synchronization with the patterns of other ports.
- Generate a trigger pattern or a sequence of PA transactions according to an analog sequencer group or an analog sequence program at a predefined port, and then synchronize it with patterns at other ports.
- Insert a digital capture pattern into the multiport burst pattern, and automatically generate the VECTOR_VARIABLE for the digital capture pattern.
- Provides unified wrapper APIs for protocol activities, using PA.
- Provides smooth switching between engineering modes and production modes.
- Visualizes the multiport assembly.
- Create and insert a flat label to a port of multi-port burst, and generate and attach a protocol-type label at the HIF port of a multi-port burst.
- Supports multiple digital captures on different digital capture ports (DigitalCapturePort).

## Supported hardware

For normal digital pattern, the API can be used with all smart scale digital cards.

The API does not require a dedicated license. However, if you want to attach "protocol type labels" in the multiport burst, a protocol-aware license is required.

## Synchronization across ports in a multi-port burst

To synchronize across ports in a multi-port burst, you must first use APIs to create the flat pattern. Next, you add flat labels to a port of a multi-port burst, or attach protocol type labels to a multi-port burst. The length or execution time of each port鈥檚 labels is recorded and then the execution time differences between ports is calculated.

If synchronization is required, a label of "repeating" idle vectors (for normal ports) or IDLE command (for transaction port) can be added to those ports with short execution time, ensuring the sequencer of each port ends at the same time.

After the synchronization, the next vector of each port starts simultaneously.

The following diagram illustrates two synchronization points:

 ![SynchronizingPorts](<../../../../raw/148151.png>)

A multi-port burst is assigned so that the single-port patterns, and protocol-type labels can be added to any port of the burst. It is not necessary that the multi-port burst exists when it is assigned. The synchronized port and the single-port labels can be added later.

The ports that need to be synchronized must be be registered. The CCT Multi-port Sequencer Synchronizer API can trace the execution time of labels at each registered port by querying the cycles and period of each label.

The synchronization activity is user-initiated:

You might require synchronization across all registered ports or partial ports. If the execution time of each port is T@Port<i>, and the maximum execution time is Tmax.

The CCT Multi-port Sequencer Synchronizer API appends one of the following labels to those ports that exhibit an execution time T@Port<i> of less than Tmax:

- Dummy cycles (for normal patterns).
- An IDLE command (for PA ports) which exhibit an execution time of (deltaT@Port<i> = Tmax-T@Port<i>).

User can assign a synchronization point to any port with the specified time point Tsync.

The CCT Multi-port Sequencer Synchronizer API appends one of the following labels to the assigned ports that exhibit an execution time T@Port<i> of less than Tsync.

- Dummy cycles (for normal patterns).
- An IDLE command (for PA ports) which exhibit an execution time of (deltT@Port<i> = Tsync-T@Port<i>).

After the synchronization point, the labels newly added to the registered ports start the next vector of each port simultaneously.

## Prerequisites

Before you can use the CCT Multi-port Sequencer Synchronizer API, make sure that the following conditions are met:

- Digital pattern must be multi-port based
- Timing set must be multi-port based
- Must be used in Concurrent Test Framework environment

## Limitations

- Ports containing CTIM/CLEV in the digital pattern are not supported.
- D2S is not supported
- BADC is not supported

## Related information

[Using the CCT Multi-Port Sequencer Synchronizer API](<03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md>)[CCT multi-port user interface APIs](<03.03.05.09.02_CCT_multi-port_user_interface_APIs.md>)

## Functional changes

- Introduced in SmarTest 7.3.2
```

## 2. 语法 / 参数段落（脚本逐字抽取，§4 —— 进页面时照抄，不重写）

*（这篇没有 `Syntax`/`Parameters` 这类段落——那就没有语法可抄，页面不许自己编一个）*

## 3. 入边 43 篇（谁引它、引它的原句 —— 「和谁有关」的唯一来源）

### ← AnalogSeqGroup()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.04_AnalogSeqGroup.md`（引 1 次）

- L35：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← attachPA()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.06_attachPA.md`（引 1 次）

- L47：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← Capture()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.13_Capture.md`（引 1 次）

- L126：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← CCTMultiportSync.flush()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.25.01_CCTMultiportSync.flush.md`（引 1 次）

- L47：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← CCTMultiportSync.start()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.25.02_CCTMultiportSync.start.md`（引 1 次）

- L46：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← CCTMultiportSync.sync()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.25.03_CCTMultiportSync.sync.md`（引 1 次）

- L46：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← CCTMultiportSync()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.25_CCTMultiportSync.md`（引 1 次）

- L46：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← PatternPort& getInstance()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.143_PatternPort__getInstance.md`（引 1 次）

- L45：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← playPattern()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.149_playPattern.md`（引 1 次）

- L45：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← PPMU_IClamp()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.155_PPMU_IClamp.md`（引 1 次）

- L84：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← PPMU_Meas()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.156_PPMU_Meas.md`（引 1 次）

- L81：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← PPMU_Relay()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.159_PPMU_Relay.md`（引 1 次）

- L63：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← PPMU_Setting_IForce()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.161_PPMU_Setting_IForce.md`（引 1 次）

- L90：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← PPMU_Setting_VForce()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.162_PPMU_Setting_VForce.md`（引 1 次）

- L90：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← PPMU_VClamp()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.163_PPMU_VClamp.md`（引 1 次）

- L81：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← registerCCTestMethod()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.179_registerCCTestMethod.md`（引 1 次）

- L75：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← registerSyncPort()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.180_registerSyncPort.md`（引 1 次）

- L57：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← release() - CCTMultiPortSync
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.182_release___-_CCTMultiPortSync.md`（引 1 次）

- L59：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← releaseInstance() - DCDynamicPort API
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.183_releaseInstance___-_DCDynamicPort_API.md`（引 1 次）

- L37：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← releaseInstance() - DigitalCapturePort API
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.184_releaseInstance___-_DigitalCapturePort_API.md`（引 1 次）

- L52：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← releaseInstance() - PatternPort API
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.185_releaseInstance___-_PatternPort_API.md`（引 1 次）

- L38：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← setAWG()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.206_setAWG.md`（引 1 次）

- L45：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← setDGT()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.208_setDGT.md`（引 1 次）

- L45：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← setMeasDef()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.211_setMeasDef.md`（引 1 次）

- L45：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← setStimDef()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.214_setStimDef.md`（引 1 次）

- L45：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← setWaitTemplatePatternName()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.223_setWaitTemplatePatternName.md`（引 1 次）

- L55：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← setWaveTable()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.224_setWaveTable.md`（引 1 次）

- L66：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← SynchronizedPort& setIdentifier()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.237_SynchronizedPort__setIdentifier.md`（引 1 次）

- L110：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← SynchronizedPort& setPort()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.238_SynchronizedPort__setPort.md`（引 1 次）

- L108：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← DCDynamicPort& getInstance()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.23_DCDynamicPort__getInstance.md`（引 1 次）

- L33：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← Trigger()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.259_Trigger.md`（引 1 次）

- L64：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← DigitalCapturePort& getInstance()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.32_DigitalCapturePort__getInstance.md`（引 1 次）

- L99：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← DigitalCapturePort& setDefaultPattern()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.33_DigitalCapturePort__setDefaultPattern.md`（引 1 次）

- L108：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← DigitalCapturePort& setDefaultPattern() - Repeat
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.34_DigitalCapturePort__setDefaultPattern___-_Repeat.md`（引 1 次）

- L117：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← DPS_Force()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.44_DPS_Force.md`（引 1 次）

- L57：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← DPS_MeasCurrent()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.45_DPS_MeasCurrent.md`（引 1 次）

- L65：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← DPS_MeasCurrentRange()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.46_DPS_MeasCurrentRange.md`（引 1 次）

- L49：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← DPS_MeasVoltage()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.47_DPS_MeasVoltage.md`（引 1 次）

- L66：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← DPS_MeasVoltageRange()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.48_DPS_MeasVoltageRange.md`（引 1 次）

- L48：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← dumpMPBGraph()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.54_dumpMPBGraph.md`（引 1 次）

- L46：[CCT Multiport Sequencer Synchronizer API](<../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

### ← Using the CCT Multi-Port Sequencer Synchronizer API
`03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md`（引 1 次）

- L154：[CCT Multiport Sequencer Synchronizer API](<03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)[CCT multi-port user interface APIs](<03.03.05.09.02_CCT_multi-port_user_interface_APIs.md>)

### ← CCT multi-port user interface APIs
`03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.02_CCT_multi-port_user_interface_APIs.md`（引 1 次）

- L342：[CCT Multiport Sequencer Synchronizer API](<03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)[Using the CCT Multi-Port Sequencer Synchronizer API](<03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md>)

### ← Concurrent Tests (CCT)
`03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05_Concurrent_Tests__CCT.md`（引 1 次）

- L18：[CCT Multiport Sequencer Synchronizer API](<03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md>)

## 4. 出边 2 个（它引谁）

- [[Using the CCT Multi-Port Sequencer Synchronizer API]] → `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md`（Using the CCT Multi-Port Sequencer Synchronizer API）
- [[CCT multi-port user interface APIs]] → `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.02_CCT_multi-port_user_interface_APIs.md`（CCT multi-port user interface APIs）

## 5. 结构段落（Procedure / Dependency / Errors …）

### 〔related Subtopics〕（L8，375 字符）

- [Using the CCT Multi-Port Sequencer Synchronizer API](<03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md>)
- [CCT multi-port user interface APIs](<03.03.05.09.02_CCT_multi-port_user_interface_APIs.md>)

The CCT Multi-port Sequencer Synchronizer API is an API set that is used to program digital multi-port bursts and handle synchronization across ports.

### 〔constraint Prerequisites〕（L82，252 字符）

Before you can use the CCT Multi-port Sequencer Synchronizer API, make sure that the following conditions are met:

- Digital pattern must be multi-port based
- Timing set must be multi-port based
- Must be used in Concurrent Test Framework environment

### 〔related Related information〕（L96，218 字符）

[Using the CCT Multi-Port Sequencer Synchronizer API](<03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md>)[CCT multi-port user interface APIs](<03.03.05.09.02_CCT_multi-port_user_interface_APIs.md>)

### 〔version Functional changes〕（L100，30 字符）

- Introduced in SmarTest 7.3.2
