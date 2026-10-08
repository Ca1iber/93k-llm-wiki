---
type: object
title: XPS256 status flags
layer: L2
stage: level
tags: [level, xps256, status-flags, protection, dps, pmu, test-head-card]
related: [level, xps256-pmu-operating-mode, xps256-programming-dps-operating-mode, dps-task, pin]
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.02_XPS256_status_flags.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# XPS256 status flags

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **8,185 字符逐字取自** `<02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.02_XPS256_status_flags.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getClampDistanceTooLow()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.04_DPS_AUX_TASK.getClampDistanceTooLow.md`） |
 | High voltage or current of surge tracker exceeded  | Trigger: |

### Tables（脚本逐字抽取，第 2 张）

 | Action:  | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
 | High voltage of surge tracker reached  | Trigger: |

### Tables（脚本逐字抽取，第 3 张）

 | Action:  | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
 | High current of surge tracker reached  | Trigger: |

### Tables（脚本逐字抽取，第 4 张）

 | Action:  | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
 | Low voltage or current of surge tracker exceeded  | Trigger: |

### Tables（脚本逐字抽取，第 5 张）

 | Action:  | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
 | Low voltage of surge tracker reached  | Trigger: |

### Tables（脚本逐字抽取，第 6 张）

 | Action:  | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
 | Low current of surge tracker reached  | Trigger: |

### Tables（脚本逐字抽取，第 7 张）

 | Action:  | The hardware settings are not changed. The flag represents the test result of the surge tracker. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.md`） |
 | Measurement range change failed  | Trigger:  | Automatic down‑ranging in DC measurement cannot set the target current measurement range. |
 | Action:  | A warning is shown in the UI report window. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getRangeError()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.07.02_DPS_AUX_TASK.getRangeError.md`） |
 | Range overflow  | Trigger: |

### Tables（脚本逐字抽取，第 8 张）

 | Availability:  | The flag is available per channel. |
 | APIs:  | `DPS_AUX_TASK.getRangeOverflow()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.14_DPS_AUX_TASK.getRangeOverflow.md`） |
 | Voltage drop force warning  | Trigger: |

### Tables（脚本逐字抽取，第 9 张）

 | Availability:  | The flag is available per channel. |
 | APIs:  | `DPS_AUX_TASK.getVoltageDropForceWarn()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.18_DPS_AUX_TASK.getVoltageDropForceWarn.md`） |
 | Voltage drop return warning  | Trigger: |

### Tables（脚本逐字抽取，第 10 张）

 | Flag  | Description |
 | Constant current  | Trigger:  | The channel is in constant current operating mode and forces or clamps the current. |
 | Action:  | The flag is for information only. |
 | Availability:  | The flag is available per channel. |

### Tables（脚本逐字抽取，第 11 张）

 | Constant voltage  | Trigger:  | The channel is in constant voltage operating mode and forces or clamps the voltage. |
 | Action:  | The flag is for information only. |
 | Availability:  | The flag is available per channel. |

### Tables（脚本逐字抽取，第 12 张）

 | Action:  | The related channel or the entire ganging group is disconnected. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getConstantCurrentLimitDisconnect()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.06_DPS_AUX_TASK.getConstantCurrentLimitDisconnect.md`） |
 | DUT board disconnect  | Trigger:  | The channel has received `DUT board disconnect shutdown`（raw: `02.05.05.03.03.06_XPS256_safety_line_and_DUT_board_disconnect.md#_354940__s_DUT_board_disconnect_shutdown`） signal from an appropriately configured trigger source. |
 | Action:  | All XPS256 channels are disconnected. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getDutBoardDisconnect()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.09_DPS_AUX_TASK.getDutBoardDisconnect.md`） |
 | Note:  | See also `XPS256 programming - Safety line and DUT board disconnect`（raw: `02.05.05.03.10.18_XPS256_programming_-_Safety_line_and_DUT_board_disconnect.md`）. |
 | Overpower / Overcurrent / Power budget exceeded  | Trigger: |

### Tables（脚本逐字抽取，第 13 张）

 | Action:  | The related channel is disconnected. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getOvercurrent()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.11_DPS_AUX_TASK.getOvercurrent.md`） |
 | Overtemperature  | Trigger:  | The temperature of the channel hardware is too high. |
 | Action:  | The related channel is disconnected. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getOvertemperature()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.12_DPS_AUX_TASK.getOvertemperature.md`） |
 | Overvoltage  | Trigger: |

### Tables（脚本逐字抽取，第 14 张）

 | Action:  | The channel is disconnected. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getOvervoltage()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.13_DPS_AUX_TASK.getOvervoltage.md`） |
 | Safety line  | Trigger:  | The channel has received `Safety line shutdown`（raw: `02.05.05.03.03.06_XPS256_safety_line_and_DUT_board_disconnect.md#_354940__s_Safety_line_shutdown`） signal from an appropriately configured and assigned trigger source. |
 | Action:  | Only XPS256 channels assigned to the trigger source are disconnected. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getSafetyLine()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.15_DPS_AUX_TASK.getSafetyLine.md`） |
 | Note:  | See also `XPS256 programming - Safety line and DUT board disconnect`（raw: `02.05.05.03.10.18_XPS256_programming_-_Safety_line_and_DUT_board_disconnect.md`）. |
 | Unregulated  | Trigger: |

### Tables（脚本逐字抽取，第 15 张）

 | Action:  | The channel is disconnected. |
 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getUnregulated()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.16_DPS_AUX_TASK.getUnregulated.md`） |
 | Voltage drop force  | Trigger: |

### Tables（脚本逐字抽取，第 16 张）

 | Availability:  | The flag is available per channel. |
 | API:  | `DPS_AUX_TASK.getVoltageDropForce()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.43.06.17_DPS_AUX_TASK.getVoltageDropForce.md`） |
 | Voltage drop return  | Trigger: |

### Tables（脚本逐字抽取，第 17 张）

 | 8  | Lost measurementstoBeChecked  | Set to 1 if not all measurement results were recorded because the test stopped earlier than expected. |
 | 9  | Type mismatch  | Set to 1 if at least one measurement has been executed in a range that does not match the requested measurement type. |
 | 10  | Wrong hardware state  | Set to 1 if the hardware switched into an unexpected state that caused the test to fail (for example, a disconnect for safety reasons). |

### Tables（脚本逐字抽取，第 18 张）

| Bit | Flag | Description |
|---|---|---|
| 0 (LSB) | Current sink limit is reached | Set to 1 if current sink limit is reached (Clamp low) for at least one measurement. |
| 1 | Current source limit | Set to 1 if current source limit is reached (Clamp high) for at least one measurement. |
| 2 | Clamp low was reached | Set to 1 if clamp low was reached during the test for a DC Scale pin where no measurement was executed. |
| 3 | Clamp high was reached | Set to 1 if clamp high was reached during the test for a DC Scale pin where no measurement was executed. |
| 4 | Range underflow | Set to 1 in case of a range underflow has been detected for at least one measurement. |
| 5 | Range overflow | Set to 1 in case of a range underflow or a range overflow has been detected for at least one measurement. |

<!-- 语法节 end -->

## 是什么

> **一句话**：**XPS256 这张卡自己的「仪表盘 + 保险丝」。**
> 卡内建了一套自保护机制和状态指示——**过压、过流、过热、压降过大、DUT 板被拔、
> 探针接触不良**等等，都会亮一个**标志（flag）**；有些标志还会**直接断开通道**。
> **读这一页的问题永远是同一个：「卡断了/报错了，是哪个标志亮了，我该做什么。」**
> `stage: level`——它管的是供电那一段的**保护与状态**。

### 标志分三大类（原文的目录结构）

| 类别 | 里头有什么 | 性质 |
|---|---|---|
| **Status flags and warnings** | surge tracker 的 7 个标志、量程切换失败、量程溢出、压降 warning ×2 | **警告**：告诉你情况不对 |
| **Operating state** | Constant current / Constant voltage | **状态**：现在工作在恒流还是恒压 |
| **Safety and self-protection** | Current limit disconnect、DUT board disconnect、Overpower/Overcurrent/Power budget exceeded、Overtemperature、Overvoltage、Safety line、Unregulated、Voltage drop force/return | **保护**：会**断通道** |

**每个标志原文都给了四个字段**（这是本页最有用的结构，逐条见上面「语法 / 参数」节）：
**`Trigger`（怎么触发）/ `Action`（该怎么办）/ `Availability`（什么条件下这个标志可用）/
`API`（用哪个函数读它）**。
—— **`Action` 那一栏才是出问题时真正要读的**；`API` 那一栏告诉你用哪段代码去读/清。

> **上面「语法 / 参数」节里是 18 张表，不是 1 张**——这不是脚本切错了，是**语料的原样**：
> 原文这张大表在 HTML 转 markdown 时被**拆成了 18 段连续的管道行**，段与段之间夹着散文
> （`Trigger:` 的说明、`Action:` 的说明…）。脚本只认**连续 ≥3 行**的管道表格，
> 所以抓成 18 张。**逐字没丢，只是被分段了**；要按标志读，**照标志名去搜**。
> 实测 `Action:` 出现 16 次、`Availability:` 20 次——**有几个标志的某一栏落在被拆散的
> 散文里，没进表**，那种情况得回 raw 看（`02.05.05.03.10.02`，第 49 行起）。

### 通道被断开之后（原文给了**两套**恢复流程，**别用错**）

**第一件事永远是：先确认断开的原因已经消除。** 之后分两种情况：

| 你当时在哪 | 要做什么 |
|---|---|
| **在 testflow 里**（跑测试时断的） | ①用 `DPS power flags - get...() functions` 那组 API 查标志状态；②**用 SmarTest 把通道 disconnect**（related 错误信息会进 report window，标志会被清掉）；③再 connect |
| **在 hardware view 里手工操作时断的** | **PMU 模式**的针：在 ADC 子面板里做一次 dummy measurement，relay action 设成 **`NT`**；**DPS 模式**的针：点 Eclipse Work Center 工具栏上的 **Disconnect**。之后同样 connect |

> **两套流程不能互换**，因为「怎么清掉标志」的机制不同——testflow 里靠 SmarTest 的
> disconnect，hardware view 里 PMU 靠 dummy 测量 + `NT`、DPS 靠工具栏 Disconnect。
> **这一步做错的表现是：标志一直不清，通道连不回去。**

## 典型用法

**排查路径（照这个顺序走）**：

1. **先分类**：亮的标志属于上表哪一类？是「警告」还是「保护（已断通道）」？
2. **读 `Action`**：上面「语法 / 参数」的表里，每个标志都带 `Action` 栏——**那是文档给的处置**。
3. **用对的 API 读**（原文在 `Status flags and warnings` 一节给了三个入口）：
   `DPS status flags - get...() functions` / `DPS power flags - get...() functions` /
   `DPS_AUX_TASK.getSurgeTrackerStatus()`
   （raw 路径见「语法 / 参数」节里各标志的 `API` 栏）。
4. **通道断了 → 按上面的两套流程之一恢复。**
5. **要看全局状态**：命令 **`TSST?`（TeSt STatus）**——见下。

### `TSST?` 和这些标志不是一回事（**容易混**）

原文（`DC event status` 一节）：`TSST?` 返回的是**上一次执行的测试**在 DC event 上的
**全局**信息，以及**所有已记录测量的累计状态**。三个要点：

- **前提**：必须已经跑过 test point pattern（DC Scale 针）。
- **累计信息在 functional test 开始时被清掉**，之后一直有效到下一次 functional test 开始。
- **`TSST?` 的回复是两段**：一段讲测试结果，一段讲测试状态。

**区别记法**：**本页的标志是「卡现在的状态」，`TSST?` 是「刚才那次测试攒下来的状态」。**
一个是卡在说话，一个是测试在说话。

## 和谁有关

**入边 79 条 / 22 篇**（`inline` 口径）——**这是 XPS256 章里入边最密的页之一**，
因为它同时被三种页引用：**保护相关的专题页、Hardware view 的按钮说明、特定 setup 任务页**。

**被谁当作入口**：

- `XPS256 specific setup tasks`（`02.05.05.03.10.01`）—— **一口气锚了 7 个标志**
  （Current limit disconnect / Overpower / Overtemperature / Overvoltage /
  Voltage drop force / Voltage drop return），**它是「出问题该去哪」的主导航**。
- [[xps256-programming-dps-operating-mode]] —— Hardware view 的 `Check Status Flags` 按钮指向本页。
- [[xps256-pmu-operating-mode]] —— **PMU 模式的 Hardware view 有同一个按钮**，
  所以**本页不是 DPS 专用的**（这一点从页名看不出来，必须写在这儿）。
- `XPS256 force and clamp voltages` / `XPS256 force and clamp currents` —— 讲 clamp 时
  引本页的 **Clamp distance too low**（原文：clamp 距离连续超过 **400 µs** 太小就置位）。
- `XPS256 arbitrary waveform generator (AWG)` —— 讲压摆率时引本页。

**并列（未建页，不链）**：`XPS256 sitemap`（导航）、`XPS256 surge tracker`（surge 机制的专页，
本页有 7 个标志是它的）、`XPS256 operating modes`。

**上游 API 页（未建页）**：`DPS status flags - get...() functions`、
`DPS power flags - get...() functions`、`DPS_AUX_TASK.getSurgeTrackerStatus` —— 
**「怎么用代码读标志」的答案在这三篇里**，本页只给标志的含义与处置。

> 上面每条都来自 `edges.jsonl` 里带原句的边。**本页没有推断。**

## 版本

- **Introduced in SmarTest 7.10.1**（和 [[xps256-pmu-operating-mode]]、
  [[xps256-programming-dps-operating-mode]] 同批引入）
- **SmarTest 7.10.2：新增 `DUT board disconnect` 与 `Safety line` 两个状态标志。**
  —— **这两个标志在 7.10.1 上是没有的**；在 7.10.3 上有。

## ⚠️ 语料里的坏字符

`more than 400 渭s` 里的 **`渭` 应为 `µ`**（微秒）。
同类的还有 [[pogo-pad-and-via-design]] 里的 `碌`——**µ 在这份语料里至少有两种坏法
（`渭` / `碌`）**，看到不认识的汉字夹在数字和单位之间，先怀疑它是 µ。
另见 `鈥慴`/`鈥慸`/`鈥慼`（短横 + 后一个字母被一起吃掉）：
`Standard鈥慸ensity` = *Standard-density*，对照表在 [[pogo-block-compatibility]]。
**语料问题，raw 只读不许改（§1.1）。**

## 出处

- 定义文档：`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.02_XPS256_status_flags.md`
  （TDC `354167.htm`，28,949 字节，398 行）
- **入边 79 条 / 22 篇**（`inline` 口径）——**本页的入边里有大量锚点**
  （`#_354167__r_…` 这种指到「某一个标志」的深层链接），
  这是它入边数高的一大原因：**同一篇文档会为每个标志各留一条链接**。
  **边数高不代表引用它的文档多**（79 条 / 22 篇，比例约 3.6:1）。
- 所属：**Test Head Cards → XPS256**（`02.05.05.03`）
- 本页 `verified: doc-only` —— **没有在任何真实 XPS256 上触发过这些标志**
  （§11：文档里有 ≠ 你这台会这样）。**`Action` 栏照文档抄，动手前先看现场。**
