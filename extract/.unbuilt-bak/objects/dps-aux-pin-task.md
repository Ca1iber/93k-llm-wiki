---
type: object
title: DPS_AUX_PIN_TASK
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01_DPS_AUX_PIN_TASK.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01.02_DPS_AUX_PIN_TASK.checkPowerFlags.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# DPS_AUX_PIN_TASK

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,572 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01_DPS_AUX_PIN_TASK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

This class has no constructor.

List of parameters

There are no parameters.

Return value

There is no return value.

### Example

The example below sets current thresholds, activates the surge tracker, checks the status against the current thresholds, and retrieves the result.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Set the current thresholds to -1 mA/1 mA and switch on surge tracker
    //
    auxTask.pin("dps1")
        .selectISensorSetThresholds(-1 mA, 1 mA)
        .setMode(TM::SURGE_TRACKER);

    auxTask.execute();

    auxTask.pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH);

ON_FIRST_INVOCATION_END();

//
// Get the result of surge tracker
//
TM::SURGE_TRACKER_STATUS surgeTrackerStatus = auxTask.getSurgeTrackerStatus("dps1");

switch (surgeTrackerStatus)
{
    case TM::SURGE_TRACKER_NONE_DETECTED:

        cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_NONE_DETECTED"
             << endl << endl;

        break;

    case TM::SURGE_TRACKER_HIGH_DETECTED:

        cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_HIGH_DETECTED"
             << endl << endl;

        break;

    case TM::SURGE_TRACKER_LOW_DETECTED:

        cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_LOW_DETECTED"
             << endl << endl;

        break;

    case TM::SURGE_TRACKER_BOTH_DETECTED:

        cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_BOTH_DETECTED"
             << endl << endl;

        break;

    default:

        break;
};
```

<!-- 语法节 end -->

## 是什么

`DPS_AUX_PIN_TASK` 是 **[[dps-aux-task]] 的从属数据容器**（subsidiary data container）。

**三条门槛，先记住：**

1. **只能经 `DPS_AUX_TASK.pin()` 拿到**——`You cannot directly construct any objects of this class.`
2. **不要**在 test method 里建它的**静态对象**，**不要**拿它做 test method 的成员变量。
3. 头文件：`/opt/hp93000/soc/prod_com/include/MAPI/DpsAuxPinTask.h`

**它有什么**（七个子主题，即七个成员函数）：

| 成员函数 | 干什么 |
|---|---|
| `checkIcHacError()` | 查 IC/HAC 错误 |
| **`checkPowerFlags()`** | **从硬件读累积的电源状态 flag**（见下） |
| `checkSetRangeError()` | 查设定范围错误 |
| `checkSurgeTracker()` | 查 surge tracker |
| `selectISensorSetThresholds()` | 设电流传感器阈值 |
| `selectVSensorSetThresholds()` | 设电压传感器阈值 |
| `setMode()` | 设模式（例：`TM::SURGE_TRACKER`） |

### 两段式：`check...()` 读硬件，`get...()` 读缓存

这是本页最该记住的一条**分工**，原文分两处讲：

- **`check...()`（在 `DPS_AUX_PIN_TASK` 上）负责把 flag 从硬件读进 test method 缓存。**
- **`get...()`（在 `DPS_AUX_TASK` 上，共 20 个）只负责从缓存里取值。**
  **必须先调 `checkPowerFlags()`**，否则缓存里没有东西可读。

`get...()` 返回枚举 `DPS_POWER_FLAG_STATUS`：**`TM::POWER_FLAG_STATUS_PASS` = 0**
（单 flag 未置位、或多个里一个都没置位）；
**`TM::POWER_FLAG_STATUS_FAIL` = 1**（单 flag 置位、或多个里至少一个置位）。

### 两个必须知道的坑

**坑一：flag 是锁存的，所以要读两次。**

> 硬件里的 flag 是**锁存**的。读状态会返回**锁存值**，并且**只清掉被读的那些 flag**。
> **如果触发条件仍在，flag 会立刻再次置位。因此这个成员函数必须调两次才能读到实际状态。**

**坑二：`PRLT` 的结果会被 `CSAS` / `PSAS` 弄失效。**

`Pass / fail results that are retrieved by command PRLT are invalidated by commands CSAS and PSAS.`
建议：**在相关功能测试之后、`CSAS` / `PSAS` 之前，直接就用 `PRLT`**。
**这条对 API 也一样**：`GET_FUNCTIONAL_RESULT()` **必须在任何 `DPS_AUX_PIN_TASK.check...()` 之前调用**，
否则 `GET_FUNCTIONAL_RESULT()` 的结果就是无效的。

### `checkPowerFlags()` 的参数

`TM::POWER_FLAG flags = TM::ALL_FLAGS` —— 一个**读掩码**。
默认 `TM::ALL_FLAGS` 读全部；也可以只读某一个，可选值有 **17 个**：
`CONST_VOLTAGE`、`CONST_CURRENT`、`UNREGULATED`、`OVER_VOLTAGE`、`OVER_CURRENT`、
`OVER_TEMPERATURE`、`VOL_DROP_FORCE`、`VOL_DROP_RETURN`、`DUTBOARD_DISCON`、`SAFETY_LINE`、
`CONST_CURR_LIMIT_DISCON`、`LOW_HEADROOM`、`CURR_LIMIT_PROTECT_DELE`、`RANGE_OVERFLOW`、
`CLAMP_DISTANCE_TOO_LOW`、`VOL_DROP_FORCE_WARN`、`VOL_DROP_RETURN_WARN`。

**flag 支持的场合**：原文说 `checkPowerFlags()` 读的 flag 由 **DPS operating mode 与
PMU operating mode 下的 DC Scale 卡**支持；而 `get...()` 那一族那一页把范围写成
**DPS operating mode、PMU operating mode 或 Digital I/O operating mode**——
**两处口径不完全一样**（见「出处」）。

## 典型用法

原文 Examples 给的顺序是**「设阈值 → 开 surge tracker → `execute()` → 查 → 取结果」**：

```c
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Set the current thresholds to -1 mA/1 mA and switch on surge tracker
    //
    auxTask.pin("dps1")
        .selectISensorSetThresholds(-1 mA, 1 mA)
        .setMode(TM::SURGE_TRACKER);

    auxTask.execute();

    auxTask.pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH);

ON_FIRST_INVOCATION_END();

//
// Get the result of surge tracker
//
TM::SURGE_TRACKER_STATUS surgeTrackerStatus = auxTask.getSurgeTrackerStatus("dps1");
```

**这段示范了三件事**：

1. **`DPS_AUX_TASK` 自己构造**（`DPS_AUX_TASK auxTask;`），**pin 级的动作链式挂在 `.pin("dps1")` 上**——
   印证了「`DPS_AUX_PIN_TASK` 只能经 `DPS_AUX_TASK.pin()` 拿」。
2. **`setMode()` / `selectISensorSetThresholds()` 只写配置，真正的动作要 `auxTask.execute()`**。
3. **结果不是在 `ON_FIRST_INVOCATION` 块里取的**——块外用 `auxTask.getSurgeTrackerStatus("dps1")` 取。
   这与上面「`check...()` 进缓存、`get...()` 出缓存」的两段式一致。

**要读 power flag 的场合，把 `checkSurgeTracker` 换成 `checkPowerFlags`，其余同形。**

## 和谁有关

- [[dps-aux-task]]（**未建**）— 父类。`DPS_AUX_TASK` 管 **surge tracker 与 TMU（Time Measure Unit）**；
  支持 surge tracker 的卡是 **DPS128/DPS64 和 XPS256**，**TMU 目前没有任何卡支持**
- [[dps128-dps64-cards]] — 本 API 读的就是这张卡的电源 flag
- [[xps256-status-flags]] — 另一张卡的状态 flag，**可对照读**（那张卡是另一族的 flag 命名）
- [[level]] — 本页 `stage: level` 的理由：读的是电源资源的状态
- [[testmethod]] — 本 API 在 test method 里用（`TASK_LIST`、`ON_FIRST_INVOCATION_BEGIN`）

## 版本

- **`checkPowerFlags()` 与 `DPS_AUX_PIN_TASK` 两篇的 `## Functional changes` 本次未逐条读**，
  本页**不填版本号**（见「出处」）

## 出处

`sources:` 两篇：

| 文档 | 讲什么 |
|---|---|
| `…/02.07_Test_Method_Reference/02.07.04.01.43.01_DPS_AUX_PIN_TASK.md` | 类本身、七个成员函数、两条 Note、Example |
| `…/02.07.04.01.43.01.02_DPS_AUX_PIN_TASK.checkPowerFlags.md` | `checkPowerFlags` 的完整语法、17 个 flag 选项、两条 Note |

**本页读了但没写进来的**（它们是**别的页**的料，不是本页）：

- `02.07.04.01.43_DPS_AUX_TASK.md`（父类，总览）
- `02.07.04.01.43.06_DPS_power_flags_-_get...___functions.md`（20 个 `get...()` 的清单与返回值）

**本页没做的**：

- **七个成员函数只详写了 `checkPowerFlags()`**，其余六个**只知道名字**（原文各自有专页）。
- **上面那段代码是原文 Example 1 的「上半段」**，**到 `getSurgeTrackerStatus` 那一行为止，逐字照抄**；
  原文后面接的 `switch (surgeTrackerStatus)` 分支（`SURGE_TRACKER_NONE_DETECTED` /
  `_HIGH_DETECTED` 等）**本页没抄**——**读到这里就断了，别以为这就是完整的例子**。
- **上面那条「flag 支持场合」两处口径不一致**（`checkPowerFlags` 页说两种模式，
  `get...()` 页说三种）。**本页两个口径都照实写了，没有替原文统一**——
  分歧本身是文档事实，**要判断请读这两篇原文**。

`verified: doc-only`
