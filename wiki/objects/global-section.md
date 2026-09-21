---
type: object
title: GLOBAL section
layer: file
stage: project
tags: [global, model-file, project-config, system-definition, license, utility-lines, testhead, timing-bundle]
related: [model-file, technology-file-for-a-device, pogocabling-section, device-license-file, mtp-memory-test, gpib-lan-communication-conventions, error-model-file-rejected-at-startup, error-flexlm-license-codes, sequencer-controlled-utility-lines, utility-line-assignments, smartest-7.2.0, smartest-7.4.3]
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# GLOBAL section

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **179 字符逐字取自** `<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

```
...
GLOBAL
    testhead = TH_8CC
    dut_interface = SOC
    device_maintenance = ON
    timing_bundle = w256-d8-r8
    diag_subsystem_interface = /dev/usb/ttyUSB0
    ...
```

<!-- 语法节 end -->

## 是什么

**`GLOBAL` 是 model file 的一个 section：在这里声明「用的是什么系统」和「系统范围内有哪些特性」。**
原文第一句逐字：

> 「In the GLOBAL section of the model file you define what kind of system is used and what
> features are available system-wide.」

**紧接着一句 `The following definitions are available:`，然后是一张 17 个名字的索引表，
再往下是这 17 个名字各自的参数说明段。** 结构就这三块（后面是 Example / Related information /
Functional changes）。

**两个「范围」要分清，这是本页最要紧的一条**：

| 范围 | 定义 | 性质 |
|---|---|---|
| **什么系统** | `testhead` / `dut_interface` / `utility_lines` / `timing_bundle` | **硬件声明**——系统有多少卡笼、接什么 DUT 板、有多少 utility 线、每通道多少波形 |
| **哪些特性系统范围内可用** | `apg_speed` / `device_maintenance` / `memorytest` / `protocol_aware` / `rapid_source_synch` / `s&s_value_package` / `triage` / `xpressdata` / `memory_pooling` / `PS1600MemoryCompatibility` / `vectorCache` | **多数是开关**，其中一部分**受 license 控制** |
| **接口/连接** | `diag_subsystem_interface` / `hpib_interface` | **外部设备怎么接** |

（**这个三分法是本页做的**，原文只给一张平铺的名字表。）

**「受 license 控制」这件事原文在索引表里就点了名**，逐字：

> 「Note The following features, for example, are licensed. Thus they could be overwritten by the
> device license file: `apg_speed, device_maintenance, memorytest, timing_bundle, xpressdata`」

**五个是举例（`for example`），不是全部。** 逐条说明里另外写明要 license 的还有
`triage`、`xpressdata`、`memorytest`、`apg_speed`、`s&s_value_package`（后者的条件是
**有生效的服务合同**）、`device_maintenance`（**FLEXlm license**）；
而 `rapid_source_synch` 原文明确写 **`RSS requires no license.`**。

### 17 个定义：取值、默认、一句话要点

**表里「取值」一列是原文的取值行；`|` 表示「或」**（原文那几处就是这么写的）。

| 定义 | 原文取值行 | 默认 | 要点 |
|---|---|---|---|
| `apg_speed` | `apg_speed = 400Mbps | 800Mbps | 1800Mbps`（**SOC 系统**） | **`0 Mbps`** | MTP memory pattern 的最高执行速率 |
| `device_maintenance` | `device_maintenance = ON` | **不写就关**，**且不发警告、不报错** | 器件维护 / refresh |
| `diag_subsystem_interface` | `diag_subsystem_interface = <device>` | 无 | RS-232 低级诊断的串口设备 |
| `dut_interface` | `dut_interface = SOC | HSM | SOC_8GROUP | SOC_4GROUP` | 无 | DUT 接口型号 |
| `hpib_interface` | `hpib_interface = vxi11/<LAN-GPIB gateway>/192.168.0.100/gpib0` | 无 | NIST 可溯源校准用的 GPIB 接口 |
| `memory_pooling` | `memory_pooling = OFF` | **默认开** | 把多个 pin 的 license 合到一个 pin 上用 |
| `memorytest` | `memorytest = ON` | 不写就关 | 存储测试软件的 pattern 生成功能 |
| `protocol_aware` | `protocol_aware = ON` | **原文没说** | 事务型协议测试要用 |
| `PS1600MemoryCompatibility` | `PS1600MemoryCompatibility = OFF | ON` | **默认开** | **关掉 PS1600 内存兼容模式** |
| `rapid_source_synch` | `rapid_source_synch = <number_of_sites>` | **`0`** | RSS，硬件里攒结果并行处理 |
| `s&s_value_package` | `s&s_value_package = ON` | **原文没说** | 开 correction data converter |
| `testhead` | `testhead = TH_8CC | TH_4CC | TH_2CC| TH_1CC` | 无 | 测试头大小与卡笼数 |
| `timing_bundle` | `timing_bundle = w32-d8-r6 | w256-d8-r8` | 无 | 全通道捆绑的波形/驱动沿/接收沿数 |
| `triage` | `triage = ON`；或 `triage = BCA | END_POINT_LOG | HOLD_TIME_FAULT | SPEED_SCAN` | 不写就关 | Yield Learning Solution 的算法 |
| `utility_lines` | `utility_lines = (64 | 128 | 256)...` `[, type = (static | sequencer_controlled) ]...` `[, pogo_size = (16 | 32)]` | **不写就 16 条** | 见下节，**本页最长的一条** |
| `vectorCache` | `vectorCache = OFF # default ON` | **默认开** | 测试处理器的向量缓存 |
| `xpressdata` | `xpressdata = ON` | **默认关**，**不写就用不了** | Xpress Data Mode |

**几条单说的：**

**`apg_speed`** —— 除了「最高速率」还管两件事：许可**作用于整个测试系统**，
而且**pattern 的实际执行速率取两个许可里的低值**。逐字：

> 「The APG speed license applies to the entire test system. The execution speed of a pattern is
> the lower value of the APG speed license and the applicable channel speed license (see IOCHANNEL
> section).」

> 「An APG speed license is required to download MTP memory test patterns.」

**即：要下载 MTP 存储测试 pattern，必须这个许可；而且它是「通道速率许可之外再加」的**
（`This license is required in addition to the channel speed license.`）。

**`device_maintenance`** —— 为什么需要它，原文给了一段机理：

> 「Memory device cells leak charge over time and must be refreshed in a specified time (16-32 ms
> typical). For a refresh, the cell state is read into a buffer and then written back.」

**`diag_subsystem_interface`** —— 有一个 `CAUTION` 是优先级问题，逐字：

> 「CAUTION If you also specify the export variable DI_RS-232 , it takes precedence over the
> settings from the model file.」

**即：环境变量压过 model file。** 取值随 OS 与 SmarTest 版本分两档：

| 场景 | 端口 → 取值 |
|---|---|
| **RHEL 7（`SmarTest ≥ 7.5`）** | Port 1 → `/dev/ttyUSB0`；Port 2 → `/dev/ttyUSB1`；**经 Com1 直连** → `/dev/ttyS0` |
| **2 口 / 4 口 RS-232 MOXA 卡（`SmarTest ≥ 7.3`）** | Port 1 → `/dev/ttyMUE0`；Port 2 → `/dev/ttyMUE1`；Port 3（仅 4 口卡）→ `/dev/ttyMUE2`；Port 4（仅 4 口卡）→ `/dev/ttyMUE3` |

**`dut_interface`** —— 四个值，原文只解释了三个：`SOC`（Pin Scale 系统标准）、
`SOC_8GROUP`（接大 DUT 板）、`SOC_4GROUP`（接小 DUT 板）。
**`HSM` 出现在合法值里，但这一节没给它任何说明**（见 `## 出处` ⑤）。

**`memorytest`** —— 已废弃，逐字：

> 「Note: DO NOT use this parameter for SmarTest versions 7.0.1 and later. It has been obsoleted
> since 7.0.1.」

**`rapid_source_synch`** —— 名字是「同步」，说明第一句却是**站点数**：
`Specifies the number of enabled sites, the default is 0.`；第二句才讲功能：

> 「Rapid Source Synch (RSS) serves to enhance the performance of source synchronous testing by
> accumulating result data in the hardware, and processing the results in parallel.」

**`testhead`** —— 四个值对应四档，逐字：`TH_8CC`（大测试头，8 卡笼）、`TH_4CC`（小，4）、
`TH_2CC`（紧凑，2）、`TH_1CC`（1 卡笼）。

**`timing_bundle`** —— 原文先定性 `A "system" resource.`，再给约束：

> 「Channels running at a speed of 1800 Mbps, 2700 Mbps or 3200 Mbps must be configured with 256
> waveforms, 8 drive edges and 8 receive edges (`timing_bundle = w256-d8-r8`), or 32 waveforms, 8
> drive edges and 6 receive edges (`timing_bundle = w32-d8-r6`).」

| 取值 | 波形数 | 驱动沿 | 接收沿 |
|---|---|---|---|
| `w32-d8-r6` | `32` | `8` | `6` |
| `w256-d8-r8` | `256` | `8` | `8` |

**即：高速通道（1800 / 2700 / 3200 Mbps）只能在这两档里选，没有第三档。**
**每通道的等价资源在 IOCHANNEL section 的 `tim` 里。**

**`vectorCache`** —— 默认是开的，而且原文加了一句「必须保持开」：

> 「The vector cache must remain enabled for all currently allowed cases.」

**即：这个开关虽然有 `OFF`，但原文说当前所有允许的用法下都得开着。**

**`xpressdata`** —— 与 `vectorCache` 的默认方向**相反**：

> 「The Xpress Data Mode is disabled by default. If not specified, you cannot use the mode. To
> operate Smart Scale cards you must enable the Xpress Data Mode. It requires a license.」

**`PS1600MemoryCompatibility`** —— 名字是「兼容」，动作是「关」：

> 「Disables the PS1600 memory compatibility mode.」

> 「The mode is enabled by default.」

**这两句在原文里不相邻**——中间隔着取值行 `PS1600MemoryCompatibility = OFF | ON`。
**本页把它拆成两段引，是因为在 markdown 里两个相邻的 `>` 行会渲染成同一个引用段**，
看上去像一句连续的原文，**而原文里它们并不是**（§11.1）。

**即：写 `OFF` 才是关掉兼容模式；不动它时兼容模式是开的。**

### `utility_lines`：本页最长的一条，四条规则

**这是 17 个定义里唯一一个能挡住系统启动的**（后文有三处 `SmarTest does not start` / 起不来的说法）。
原文一共给了四条规则。

**规则一：两个文件都要写，系统会校验。** 逐字：

> 「For online use the utility lines are defined in the .technology file (device viewpoint) as well
> as in the `model` file (system viewpoint). Dependent on the detected wiring board the definitions
> are validated and a warning is given if there is a mismatch.」

**两个视角**：`.technology` 是**器件视角**，`model` 是**系统视角**；
**检出接线板之后两边校验，不一致给 warning。**

**规则二：`256` 才能开满每块 32 条；不写就 16 条；乱写会起不来。** 逐字：

> 「A `utility_lines = 256` entry in the model file is required to enable all 32 utility lines per
> pogo block. If no `utility_lines` entry is made at all the system defaults to 16 utility lines.
> Entering 32 lines makes sense only if 4-row utility line pogo blocks are installed. If this is
> not observed SmarTest does not start.」

**三个数对齐**：`256` = **8 块 × 每块 32 条**；
**`32` 条只在装了 4 行 utility pogo block 时才有意义，违反则 SmarTest 起不来。**

**规则三：test head × `dut_interface` 决定合法的 `utility_lines` / `type` / `pogo_size` 组合。**

| Test head | `dut_interface` | `utility_lines` | `type` | `pogo_size` |
|---|---|---|---|---|
| `ATH`（`TH_1CC`） | `SOC_4GROUP` | `64` | `sequencer_controlled` | `16` |
| `ATH`（`TH_1CC`） | `SOC_8GROUP` | `128` 或 `256` | `sequencer_controlled` | `16` 或 `32` |
| `CTH`（`TH_2CC`） | `SOC_4GROUP` | `64` | **`static`** | `16` |
| `CTH`（`TH_2CC`） | `SOC_8GROUP` | `128` 或 `256` | `sequencer_controlled` | `16` 或 `32` |
| `STH`（`TH_4CC`） | `SOC_4GROUP` | `64` | **`static`** | `16` |
| `STH`（`TH_4CC`） | `SOC_8GROUP` | `128` 或 `256` | `sequencer_controlled` | `16` 或 `32` |
| `LTH`（`TH_8CC`） | `SOC_8GROUP` | `128` 或 `256` | `sequencer_controlled` | `16` 或 `32` |

**读出来的三条（都是这张表里的）**：
**`64` 条那一档只能是 `static`（在 `CTH` / `STH` 上）或 `sequencer_controlled`（在 `ATH` 上）**；
**`128` / `256` 那一档一律是 `sequencer_controlled`**；
**`LTH`（`TH_8CC`）只能配 `SOC_8GROUP`——大测试头没有 `SOC_4GROUP` 那一行。**

> ⚠️ **原文那几格是用 `|` 隔开写的（`128 | 256`、`16 | 32`），
> 本页为了排进表格改写成「或」**；**数值与顺序一个没动**。

**规则四：两个文件都不写时的兜底行为。** 原文写了两遍，一遍说小测试头、一遍说大测试头，
**两遍内容一样**（见 `## 出处` ⑥）：

> 「No `utility_lines` entry in the model file nor in the .technology file causes the following
> system behavior on the small test head:
> - If `dut_interface = SOC_8GROUP`, the system provides 128 utility lines, not
>   sequencer-controllable」

> 「Note No `utility_lines` entry in the model file nor in the .technology file causes the following
> system behavior on the large test head:
> If `dut_interface = SOC_8GROUP`, the system provides 128 utility lines, not
> sequencer-controllable..」

**即：都不写时，`SOC_8GROUP` 给 128 条，而且不可被 sequencer 控制。**

## 典型用法

**原文有一个 `## Example`，没有 `## Procedure`、没有 `## Before you begin`。**
**那个 Example 已经在语法节里逐字了**，内容是 5 行（`testhead` / `dut_interface` /
`device_maintenance` / `timing_bundle` / `diag_subsystem_interface` 各一行），
本页不重复抄一遍。

**从这个例子加上那些说明，能落成动作的有这些：**

| 要做的 | 怎么做 / 依据 |
|---|---|
| **先声明系统是什么** | `testhead` 与 `dut_interface` 是**其它定义的前提**——`utility_lines` 的合法组合就是按这两个查的 |
| **要用 utility 线** | **两个文件都要写**（`model` 系统视角 + `.technology` 器件视角），否则按**规则四**兜底：`SOC_8GROUP` 下 128 条且不可 sequencer 控制 |
| **要每块 32 条 utility 线** | 必须写 `utility_lines = 256`，**且确认装的是 4 行 utility pogo block**，否则 **SmarTest 起不来** |
| **要高速通道** | `timing_bundle` 只能 `w32-d8-r6` 或 `w256-d8-r8`；**实际速率还要看 `apg_speed` 与通道速率许可里的低值** |
| **要用串口诊断** | `diag_subsystem_interface` 按 OS 与 SmarTest 版本选端口；**如果同时设了 `DI_RS-232` 环境变量，它会压过 model file** |
| **开了特性但没生效** | 先看是不是 license 问题——索引表那条 `Note` 点了 5 个受许可控制的定义，**而且明确说它们 `could be overwritten by the device license file`** |
| **要改 `memorytest`** | **别改**：7.0.1 起已废弃 |
| **要开 Xpress Data Mode** | 必须显式写 `xpressdata = ON`（默认是关的，不写就用不了）；**要操作 Smart Scale 卡就必须开** |

**注意例子本身有一处对不上**（见 `## 出处` ⑦）：
例子里同时写了 `testhead = TH_8CC` 和 `dut_interface = SOC`，
**而 `utility_lines` 那张组合表里 `LTH`（`TH_8CC`）只有 `SOC_8GROUP` 那一行**；
**例子里也没有 `utility_lines` 这一行**，照**规则四**就只能拿默认。
**本页照原样引，不替例子补行、也不替它改值。**

## 和谁有关

- [[model-file]] — **上游，本页是它的一个 section**。原文第一句就是
  `In the GLOBAL section of the model file you define …`。
  **model file 整体有哪些 section、GLOBAL 在里面的位置，在那页。**
- [[technology-file-for-a-device]] — **utility 线的另一个视角**。
  `utility_lines` 规则一逐字写着两个文件都要写、系统会校验；
  **`.technology` 是「器件视角」，本页是「系统视角」——一个定义查两处，不一致只给 warning。**
- [[sequencer-controlled-utility-lines]] — **`type = sequencer_controlled` 的落点**。
  这个名字在本页出现三次（取值行、组合表、兜底规则里的 `not sequencer-controllable`），
  而且原文 `Related information` 直接链到
  `Serial interface for sequencer-controlled utility lines`。
  **本页只有「能不能被 sequencer 控制」这个开关，线怎么被控在那页。**
- [[utility-line-assignments]] / [[utility-line-view]] — **utility 线的软件侧**。
  本页 `utility_lines` 只说**有几条、什么类型、pogo 多大**；
  **哪条线派什么用、软件里怎么看，在那两页。**
- [[pogocabling-section]] — **同级的另一个 section**。
  它出现在两处：`Related information` 和版本条目 `SmarTest 6.5.0: New definition: POGOCABLING`。
  **注意：它是版本段里被记了一笔、但本页正文一个字都没写的定义。**
- [[device-license-file]] — **会覆盖本页定义的那个文件**。
  索引表那条 `Note` 逐字说受许可控制的功能 `could be overwritten by the device license file`。
  **本页只有「会被它覆盖」这一句，覆盖规则在那页。**
- [[mtp-memory-test]] — **`apg_speed` 与 `memorytest` 的下游**。
  `apg_speed` 管的是 `MTP memory patterns` 的执行速率，**且是下载它们的必要条件**；
  `memorytest` 管的是「存储测试软件的 pattern 生成功能」。
  **两个定义都指到 MTP 存储测试那边去，那页讲 MTP 怎么用。**
- [[gpib-lan-communication-conventions]] — **（推断）`hpib_interface` 的下游**。
  本页只说这个定义给 NIST 可溯源校准指定 GPIB 接口、取值是 `vxi11/<网关>/IP/gpib0`；
  **依据是「都是 LAN-to-GPIB 这条路」。本页没有那页的任何事实。**
- [[error-model-file-rejected-at-startup]] — **（推断）本页几条硬约束的后果页**。
  `utility_lines` 那两句 `If this is not observed SmarTest does not start.` 与
  `The vector cache must remain enabled for all currently allowed cases.`
  都是「写错就起不来」这一类的；**依据是页名指的正是「model file 在启动时被拒」。
  本页只有这两句后果，那个报错的细节在那页。**
- [[error-flexlm-license-codes]] — **（推断）license 侧的报错页**。
  `device_maintenance requires a FLEXlm license` 是本页唯一一处点名 FLEXlm 的地方；
  **依据只是「FLEXlm」这个词。本页没有那页的任何事实。**
- `IOCHANNEL section`（**未建**）— **`timing_bundle` 的每通道等价物**。
  原文两处链到它：`apg_speed` 的「通道速率许可」和 `timing_bundle` 的
  `For the equivalent per-channel resource see tim in the IOCHANNEL section`。
  **本页是系统级的捆绑数，通道级在那页。**
- `POGOCABLING section`（**未建**，但允许清单里有 [[pogocabling-section]]）— 见上。
- `Maintenance operations`（**未建**）— `device_maintenance` 的细节页。
- `Exploiting hardware resources for performance enhancement`（**未建**）—
  `rapid_source_synch` 的细节页。
- `Serial interface for sequencer-controlled utility lines`（**未建**）—
  `utility_lines` 的 `sequencer_controlled` 类型对应的细节页。
- `PPU` / `mux_boards` / `ppu_device`（**均未建/不在清单**）—
  只在版本段里出现（`SmarTest 7.0.1: Removed option: ppu_device`、
  `SmarTest 7.3.4: New definition: mux_boards`），**本页正文没有它们。**

## 版本

原文**有** `## Functional changes` 段，**17 条**（逐字）：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 6.5.0: New definition: POGOCABLING**
- **SmarTest 6.5.2: New definition: triage**
- **SmarTest 6.5.3: E7032B (L488) LAN to GPIB gateway introduced**
- **SmarTest 6.5.3: SW Online Value Package license added, which is needed by cal data converter**
- **SmarTest 6.5.3: RSS no longer requires license**
- **SmarTest 7.0.1: For HSM: No license required for multiport**
- **SmarTest 7.0.1: Removed option: ppu_device**
- **SmarTest 7.0.1: For HSM: Xpress Transfer Mode supported**
- **SmarTest 7.1.0: New parameters: memory_pooling, protocol_aware**
- **SmarTest 7.1.0: No license or entry required for multisite**
- **SmarTest 7.1.0: For MTP on SOC: additional 4600/8000 Mbps speed steps with release 7.1.3.2**
- **SmarTest 7.2.0: New definition: utility_lines**
- **SmarTest 7.3.4: New definition: mux_boards**
- **SmarTest 7.4.3: diag_subsystem_interface definition**
- **SmarTest 7.4.4: New optional parameter diag_behavior of definition mux_boards**
- **SmarTest 7.5.3: Term "calibration data converter" replaced**

**三条要点：**

**第一，第一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 说的是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 GLOBAL section 本身成立于哪个版本，这份语料没有。**

**第二，版本段比本页正文宽。** 17 条里有 3 条讲的是
**本页正文一个字都没写的定义**：
`POGOCABLING`（6.5.0）、`mux_boards`（7.3.4）与其可选参数 `diag_behavior`（7.4.4）；
还有一条讲**被删掉的** `ppu_device`（7.0.1）。
**即：这一段记的是「GLOBAL 这一族」的变更，不只是本页那 17 个定义。**
**本页不把它们当本页的定义讲。**

**第三，两条自身就不自洽的条目：**

| 条目 | 问题 |
|---|---|
| `SmarTest 7.1.0: For MTP on SOC: additional 4600/8000 Mbps speed steps with release 7.1.3.2` | **挂在 7.1.0 下面，正文却说 `with release 7.1.3.2`** —— **同一条里两个版本号** |
| `SmarTest 6.5.3: E7032B (L488) LAN to GPIB gateway introduced` | **正文 `hpib_interface` 那格写的是 `E7032A LAN to GPIB gateway: e5810a (E5810A)`** —— **版本段说 E7032B，正文说 E7032A**（见 `## 出处` ③） |

**另外两条与正文的对应关系值得记：**
`SmarTest 7.4.3: diag_subsystem_interface definition` 说明**这个定义是 7.4.3 才加的**，
而正文那两档取值（`≥7.5` 与 `≥7.3`）说的是**不同 OS 下的端口名**——
**两者不冲突，但正文没有一句话说这个定义本身从 7.4.3 起才有**。
`SmarTest 7.5.3: Term "calibration data converter" replaced` 与
`s&s_value_package` 那格的 `Enables the correction data converter` 对应——
**即 7.5.3 起这个词从 `calibration data converter` 改成了 `correction data converter`
（6.5.3 那条里还写着旧的 `cal data converter`）。**

**与 wiki 面向版本的关系**：本 wiki 目标是 **SmarTest 7.10.3**，**最后一条是 7.5.3**，
**在 7.10.3 之前**——**所以 7.5.3 到 7.10.3 之间 GLOBAL section 没有变更条目。**

## 出处

`sources:` 一篇：
`02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md`

**本页没做的：**

- **那 17 段的原文段落本页是转述 + 择要引的，不是全抄。**
  尤其是 `device_maintenance`、`rapid_source_synch`、`triage`、`s&s_value_package` 四段，
  本页只留了最要紧的一两句，**它们的完整措辞（含 license 的具体条件与联系途径）
  得回原文看。**
- **`## 语法 / 参数` 节一个字没改**（§4）。**里面那个 `### Example` 也是脚本逐字抽的**，
  所以本页 `## 典型用法` 里没有重复抄它。
- **五个下游文档一个都没读**：`IOCHANNEL section`、`POGOCABLING section`、
  `The device license file`、`Maintenance operations`、
  `Exploiting hardware resources for performance enhancement`、
  `Serial interface for sequencer-controlled utility lines`（**六个**）。
  **这是本页最大的空缺**——**`utility_lines` 的时序/接线细节、license 覆盖规则、
  refresh 怎么做、RSS 怎么用、sequencer 怎么控线，本页一个字都没有。**
- **`.technology` file 没读**（[[technology-file-for-a-device]] 那页也没读）——
  所以**「器件视角」那一半是什么样、两个文件怎么写才不冲突，本页只有一句 `a warning is given
  if there is a mismatch`。**
- **`model file` 整体结构没读** —— 所以 **GLOBAL 在 model file 里排第几、前面后面是什么 section、
  别的 section 有哪些定义，本页没有。**
- **`MTP`（存储测试）那一族的文档没读** —— 所以 `apg_speed` 说的
  `MTP memory patterns` 和 `memorytest` 说的「存储测试软件的 pattern 生成功能」
  **具体是哪套软件、怎么用，本页不知道。**
- **`Smart Scale` 卡与 `Pin Scale` 的文档没读** —— 所以 `xpressdata` 那句
  `To operate Smart Scale cards you must enable the Xpress Data Mode` 的**理由本页没有。**
- **`PS1600` 的文档没读** —— 所以 `PS1600MemoryCompatibility` 到底在兼容什么、**为什么要能关掉，
  本页只有「关掉它就是写 OFF」这一句。**
- **`HSM` 的文档没读** —— 所以 `dut_interface` 的 `HSM` 这个值是什么，
  **本页和原文一样都不知道**（见下 ⑤）。
- **一张图都没有。** 原文没有图片。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：本页 `layer: file`、`stage: project`，所以本页没有去别处找它的层级定位。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 编码损坏：`鈮?` 形态 2 处。** 逐字：
> `RHEL 7 (SmarTest 鈮?7.5):` 与 `2-port and 4-port RS-232 MOXA cards (SmarTest 鈮?7.3):`
> ——**`鈮?` 是 `≥`**（§11.2 ① 那一类，只是前缀不是 `鈥`）。
> **代价照 §11.2 ① 写清楚：拿修好的 `SmarTest ≥ 7.5` 去 raw 里搜是搜不到的。**
> **本页正文里写的是修好的 `≥`，引文里照原样。**
> **本篇没有 `鈥` 形态的损坏**（查过 `鈥`，0 处）。
>
> **② 索引表里有一个名字和正文对不上。** 索引里写 `memory_compatibility`，
> **正文里那一段的标题是 `PS1600MemoryCompatibility`**，取值行也是
> `PS1600MemoryCompatibility = OFF | ON`。
> **同一个定义，索引与正文用了两个名字。本页正文用 `PS1600MemoryCompatibility`，
> 并在表里保留索引那个名字的存在这件事——没有替它们统一。**
>
> **③ GPIB 网关的型号在正文与版本段里不一致。** 正文逐字：
> `E7032A LAN to GPIB gateway: e5810a (E5810A)`；
> 版本段逐字：`SmarTest 6.5.3: E7032B (L488) LAN to GPIB gateway introduced`。
> **一个说 E7032A、一个说 E7032B。本页并列两处，不判哪个对。**
>
> **④ `dut_interface` 的取值里有没解释的值。** 取值行是
> `dut_interface = SOC | HSM | SOC_8GROUP | SOC_4GROUP`，**而正文只解释了 `SOC` /
> `SOC_8GROUP` / `SOC_4GROUP` 三个**——**`HSM` 一个字的说明都没有。**
> （`HSM` 在后面反而出现在**版本段**里三次：`For HSM: No license required for multiport`、
> `For HSM: Xpress Transfer Mode supported`。）
> **本页在正文里照实写「`HSM` 没给说明」。**
>
> **⑤ `testhead` 的取值行少一个空格。** 逐字：
> `testhead = TH_8CC | TH_4CC | TH_2CC| TH_1CC`
> ——**`TH_2CC|` 之间没有空格**，前两处都有。**本页引文照原样。**
>
> **⑥ `utility_lines` 的兜底规则写了两遍，第二遍是 `Note` 且多一个句号。**
> 第一遍在小测试头上、用 bullet 起头：
> `- If dut_interface = SOC_8GROUP, the system provides 128 utility lines, not
> sequencer-controllable`；
> 第二遍在大测试头上、**内容一样但以 `Note` 起头、丢了 bullet、且以 `..` 结尾**：
> `…not sequencer-controllable..`
> ——**同一个结论对应两个测试头，两遍的措辞几乎相同。**
> **本页并列两处，不替它们合并。**
>
> **⑦ 原文那个 Example 与本页正文的约束对不上。** 例子逐字（在语法节里）：
> `testhead = TH_8CC` 配 `dut_interface = SOC`；
> 而 `utility_lines` 那张组合表里 **`LTH`（`TH_8CC`）只有 `SOC_8GROUP` 一行**。
> **例子里也没有任何 `utility_lines` 行。**
> **本页照原样，不替例子补行、不替它改值。**
>
> **⑧ Example 里的串口设备名和正文的例子不同。** 例子写
> `diag_subsystem_interface = /dev/usb/ttyUSB0`，
> **而正文 RHEL 7 那一档写的是 `diag_subsystem_interface = /dev/ttyUSB0`**
> ——**多了一段 `/usb/`。本页并列两处，不判哪个对。**
>
> **⑨ 索引表那条 `Note` 被放进了表格单元里。** 逐字（它就是那一行的第三格）：
> `|   |   |   |  Note The following features, for example, are licensed. Thus they could be
> overwritten by the device license file: …`
> ——**那张索引表是 3 列 6 行，这条 `Note` 占掉了第 6 行的第三格**，
> **和 `vectorCache` / `xpressdata` 排在同一个位置的邻居格里**
> （这也解释了为什么 17 个定义占满了 18 个格）。
> **本页把它当独立的一段讲。**
>
> **⑩ `Note` 与 `CAUTION` 后面一律没有分隔符**，逐字开头：
> `Note The following features, for example, are licensed.`、
> `CAUTION If you also specify the export variable DI_RS-232 , it takes precedence …`、
> `Note: DO NOT use this parameter for SmarTest versions 7.0.1 and later.`、
> 以及 ⑥ 里那条 `Note No utility_lines entry …`。
> **本页引文照原样，正文里加了分隔。**
>
> **⑪ 标点异常两处**：`DI_RS-232 ,` 里的**逗号前面多一个空格**；
> 以及 ⑥ 那条末尾的 `..`（两个句号）。
>
> **⑫ `## Related information` 五个链接全粘在一起**，中间没有任何分隔符：
> `The device license file` + `IOCHANNEL section` + `POGOCABLING section` +
> `Technology file for a device` + `Serial interface for sequencer-controlled utility lines`。
> **注意第三个和第五个的名字与它们在别处的标题不完全一样**
> （正文里是 `POGOCABLING section`，版本段里是 `New definition: POGOCABLING`）。
>
> **⑬ 版本段里有一条自身带两个版本号的条目**（见 `## 版本` 第三点）：
> `SmarTest 7.1.0: For MTP on SOC: additional 4600/8000 Mbps speed steps with release 7.1.3.2`。
> **本页照抄，不判它该归 7.1.0 还是 7.1.3.2。**
>
> **⑭ `PS1600MemoryCompatibility` 那一格多出一个空单元。** 它前面那行是单独的 ` | `，
> 而别的定义（如 `protocol_aware`）前面也是 ` | `——
> **即每个定义前后各有一格空单元，表结构本身是碎的两列表**，
> **`rapid_source_synch` 那一格前面更连着两个空单元。**
> **这是原文表格结构的问题，不是脚本的错。**

`verified: doc-only`
