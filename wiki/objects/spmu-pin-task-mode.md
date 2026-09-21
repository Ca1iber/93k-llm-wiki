---
type: object
title: SPMU_PIN_TASK.mode()
layer: L3
stage: level
tags: [spmu, pin-task, measurement-mode, level, dc-test, badc, pmmu, xps256, ganging]
related: [dc-scale-xps256-card, dps128-dps64-cards, flex-relay, dc-test-programming, xps256-pmu-operating-mode, dc-scale-uhc4t-card, dps-pins-editor, digital-pins-editor, smartest-7.4.0, smartest-7.5.0, smartest-7.10.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# SPMU_PIN_TASK.mode()

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,658 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
SPMU_PIN_TASK& mode(const STRING& mode);
```

Parameter
 | Parameter  | Description |
 | mode  | Default mode is "IFVM".

Refer to the list of available options of the mode parameter below.

 |

Available options of parameter: mode
 | mode  | Description |
 | "IFVM" |

Force current and measure voltage.

This mode is set so that voltage is forced and the required current is defined via symmetrical set current clamp values. Therefore, you must observe the minimum clamp current distance for setting the forced current in the "IFVM" mode.

AVI64 and FVI16 support the real current forcing modes `"CFVM" and "CFIM"`（raw: `02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md#_131275__r_AVI64_FVI16`） in which the minimum clamp distance does not have to be observed.

 |
 | "VFIM"  | Force voltage and measure current. |
 | "VM_HIZ"  | High impedance voltage measurement. |
 | "VM_HIZ_HAC"  | High impedance voltage measure with high accuracy. The voltage range is selected via `SPMU_PIN_TASK.min()`（raw: `02.07.04.01.234.01.23_SPMU_PIN_TASK.min.md`） and `SPMU_PIN_TASK.max()`（raw: `02.07.04.01.234.01.21_SPMU_PIN_TASK.max.md`）. |
 | "IFVM_UNGANGED"  | Force current and measure voltage by temporarily separating ganged channels for this measurement.

The ganged channels are temporarily unganged to the minimum number of channels that is required to force the programmed current. The voltage measurement is always performed on the first channel of the ganged group. Temporarily unganging for voltage measurements will improve the stability of the forced current and therefore improve the stability of the voltage measurement.

 |
 | "VFIM_UNGANGED"  | Force voltage and measure current by temporarily separating ganged channels for this measurement.

See also `Number of channels in unganged mode`（raw: `02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md#_131275__s_Number_of_channels_unganged`） below.

Note that on DPS128/64 and XPS256 you cannot execute a current compare on a ganged group of channels in unganged mode. Already activated comparators are silently disabled in unganged mode. A user notification (Error or warning) is omitted in this case, to avoid any interrupt in the testflow. The previous state of the comparators is automatically restored after the ganged group has been restored.

 |
 | "PPMU_BADC" |

Connects the board ADC (BADC) with the pin PMU (PPMU) for static measurements.

Mapped to "IFVM" for DC Scale cards without a separate board ADC.

 |
 | The following measurement modes are supported only for the `DC Scale XPS256 card`（raw: `../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md`）. |
 | "VFVM"  | Force voltage and measure voltage. |
 | "CFVM" |

Force current directly and measure voltage or current.

Both the lower and the upper clamp must be set by function `SPMU_PIN_TASK.clamp()`（raw: `02.07.04.01.234.01.01_SPMU_PIN_TASK.clamp.md`） if these modes are selected.

 |
 | "CFIM"  | Note If the `SPMU_PIN_TASK.iForce()`（raw: `02.07.04.01.234.01.14_SPMU_PIN_TASK.iForce.md`） or `SPMU_PIN_TASK.vForce()`（raw: `02.07.04.01.234.01.34_SPMU_PIN_TASK.vForce.md`） is used, the corresponding mode("IFVM" or "VFIM") is set automatically.

### Return value

A reference to the `SPMU_PIN_TASK`（raw: `02.07.04.01.234.01_SPMU_PIN_TASK.md`） object.

### Example

In the example below "VM_HIZ" selects the Board ADC for a voltage measurement.

```
SPMU_TASK badc_task;

ON_FIRST_INVOCATION_BEGIN();
 badc_task.pin("pinName").mode("VM_HIZ");
 badc_task.pin("pinName").settling(1 ms).samples(1);
 badc_task.pin("pinName").relay("TERM");
 badc_task.pin("pinName").min(0 V).max(5 V);
 badc_task.preAction("NONE").execMode("PVAL").execute();
ON_FIRST_INVOCATION_END();

cout << badc_task.getValue("pinName") << endl;
```

<!-- 语法节 end -->

## 是什么

**`SPMU_PIN_TASK.mode()` 设 SPMU（pin PMU）的测量模式，并按需把 BADC 或 PPMU 接上。**
原文第一句逐字：

> 「Sets the measurement mode, like fore current measure voltage or force voltage measure current
> and connects the BADC or PPMU if required.」

**签名只有一个字符串参数，返回的是自己**（语法节里逐字）：

```
SPMU_PIN_TASK& mode(const STRING& mode);
```

**`mode` 的默认值是 `"IFVM"`；返回 `SPMU_PIN_TASK` 的引用**——
所以能链式接着调别的成员函数（原文 `## Return value`：`A reference to the SPMU_PIN_TASK object.`）。

### 十个模式，原文分了三档

| 档 | 模式 | 原文给的适用范围 |
|---|---|---|
| 通用 | `"IFVM"` / `"VFIM"` / `"VM_HIZ"` / `"VM_HIZ_HAC"` / `"IFVM_UNGANGED"` / `"VFIM_UNGANGED"` | **没给限制** |
| 板级 ADC | `"PPMU_BADC"` | **没给限制**（无独立 BADC 的 DC Scale 卡上映射到 `"IFVM"`） |
| 仅 XPS256 | `"VFVM"` / `"CFVM"` / `"CFIM"` | 原文写 `supported only for the DC Scale XPS256 card` |

**逐档一句话**：

| mode | 做什么（**原文**） |
|---|---|
| `"IFVM"` | `Force current and measure voltage.` ——**默认值** |
| `"VFIM"` | `Force voltage and measure current.` |
| `"VM_HIZ"` | `High impedance voltage measurement.` |
| `"VM_HIZ_HAC"` | `High impedance voltage measure with high accuracy.` 量程由 `min()` / `max()` 选 |
| `"IFVM_UNGANGED"` | **临时拆开 ganged 通道**来 force current / measure voltage |
| `"VFIM_UNGANGED"` | **临时拆开 ganged 通道**来 force voltage / measure current |
| `"PPMU_BADC"` | 把板级 ADC 接到 pin PMU 上做静态测量 |
| `"VFVM"` | `Force voltage and measure voltage.` |
| `"CFVM"` | `Force current directly and measure voltage or current.` |
| `"CFIM"` | **原文这一格没写它做什么**，只有一个粘上去的 `Note`（见 `## 出处` ④） |

### `"IFVM"` 有个钳位距离约束，AVI64 / FVI16 能绕开

逐字：

> 「This mode is set so that voltage is forced and the required current is defined via symmetrical
> set current clamp values. Therefore, you must observe the minimum clamp current distance for
> setting the forced current in the "IFVM" mode.」

> 「AVI64 and FVI16 support the real current forcing modes "CFVM" and "CFIM" in which the minimum
> clamp distance does not have to be observed.」

**两句合起来读**：名字是「force current」，**实际是 force voltage，要的电流靠一对对称钳位值定出来**，
**所以设的电流必须离钳位值有最小距离**。
**`AVI64` / `FVI16` 上换 `"CFVM"` / `"CFIM"` 就没有这个距离要求。**

### `"VM_HIZ_HAC"` 只选「高阻+高精度」，量程在别处

逐字：`The voltage range is selected via SPMU_PIN_TASK.min() and SPMU_PIN_TASK.max().`
——**量程要去那两个函数里给，本函数不管。**

### `"*_UNGANGED"`：测量期间临时拆开 ganged 组

逐字：

> 「The ganged channels are temporarily unganged to the minimum number of channels that is
> required to force the programmed current. The voltage measurement is always performed on the
> first channel of the ganged group. Temporarily unganging for voltage measurements will improve
> the stability of the forced current and therefore improve the stability of the voltage
> measurement.」

**三件事**：拆到「刚好够 force 这个电流」的最少通道数；
**电压测量一律取 ganged 组的第一个通道**；拆开是为了提高电流稳定性，进而提高电压测量稳定性。

**DPS128/64 与 XPS256 上有一条副作用**，逐字：

> 「Note that on DPS128/64 and XPS256 you cannot execute a current compare on a ganged group of
> channels in unganged mode. Already activated comparators are silently disabled in unganged
> mode. A user notification (Error or warning) is omitted in this case, to avoid any interrupt in
> the testflow. The previous state of the comparators is automatically restored after the ganged
> group has been restored.」

**四件事**：不能做 current compare；已开的比较器**静默**关掉；
**故意不发 Error/warning**（原文写明理由是 `to avoid any interrupt in the testflow`）；
**恢复 ganged 组之后比较器状态自动还原。**

### 拆几个通道：原文给了一条公式（**不在语法节里**）

在 unganged 模式下，`max()` / `min()` / `limits()` 给的 P/F 限值**既定量程、也定拆几个通道**：

- `No. of remaining ganged channels = CEIL [ P/F limit / (ilimitPerChannel ]`
- `ilimitPerChannel = (programmedIlimit / totalNumberOfGangedChannels) - clampError`

**三个输入的含义（原文）**：

| 名字 | 原文 |
|---|---|
| `programmedIlimit` | `Current limit specified in A in SPMU_PIN_TASK.clamp()` |
| `totalNumberOfGangedChannels` | `Original number of ganged channels as defined in the pins editor` |
| `clampError` | `Maximum error, defined in the current clamp specification of the used DPS` |

原文对这条规则的解释逐字：

> 「The current limit per channel is defined by the programmed current limit and the total number
> of ganged channels. For calculating the number of remaining ganged channels, the current limit
> per channel is lowered by the maximum specified error for the selected range. This will ensure
> that the requested current can flow in temporary unganged mode.」

**注意方向**：`clampError` 是**减**掉的，**即算出来的每通道限值比理论值低**——
原文说这么做是为了「保证要的电流在临时拆开时流得动」。

原文的收尾警告逐字：

> 「Note We recommend always, verifying current measurements in temporarily unganged mode
> carefully. Automatic unganging of channels may result in current measurements directly at the
> range boundaries or close to the programmed clamp current.」

**即：自动拆通道可能把测量点推到量程边界或钳位电流附近，所以 unganged 下的电流测量要人工复核。**

### `"PPMU_BADC"`：接板级 ADC，且会撞资源

原文关于这一档共四句，按顺序逐字：

> 「Connects the board ADC (BADC) with the pin PMU (PPMU) for static measurements.」

> 「Mapped to "IFVM" for DC Scale cards without a separate board ADC.」

> 「A resource conflict error will be issued in case multiple pin PMUs are connected to the BADC.」

> 「Note Although Board ADC measurements can be done with this function, it is recommend using the
> FLEX_RELAY class instead.」

**依次是**：接上做什么 → **没有独立 BADC 的 DC Scale 卡上退化成 `"IFVM"`** →
**多个 pin PMU 同时接 BADC 会报 resource conflict error** →
**原文推荐改用 `FLEX_RELAY` 类。**

### 两条「别处也会改这个模式」的说明

- `"CFVM"` / `"CFIM"`：`Both the lower and the upper clamp must be set by function
  SPMU_PIN_TASK.clamp() if these modes are selected.` ——**上下钳位都必须先设。**
- `iForce()` / `vForce()`：`Note If the SPMU_PIN_TASK.iForce() or SPMU_PIN_TASK.vForce() is used,
  the corresponding mode("IFVM" or "VFIM") is set automatically.`
  ——**调这两个函数会顺手把模式改掉**（`iForce()` → `"IFVM"`，`vForce()` → `"VFIM"`），
  **所以它和本函数是两条会互相覆盖的路。**

## 典型用法

**原文只有一个 `## Example`，没有 `## Procedure`、没有 `## Before you begin`。**
例子逐字：

```
SPMU_TASK badc_task;

ON_FIRST_INVOCATION_BEGIN();
 badc_task.pin("pinName").mode("VM_HIZ");
 badc_task.pin("pinName").settling(1 ms).samples(1);
 badc_task.pin("pinName").relay("TERM");
 badc_task.pin("pinName").min(0 V).max(5 V);
 badc_task.preAction("NONE").execMode("PVAL").execute();
ON_FIRST_INVOCATION_END();

cout << badc_task.getValue("pinName") << endl;
```

原文对它的说明只有一句：`In the example below "VM_HIZ" selects the Board ADC for a voltage
measurement.`

**从这个例子能读出四条（都在原文里）**：

| 读出来的 | 依据 |
|---|---|
| **`"VM_HIZ"` 走的是板级 ADC** | 就是上面那句；**本页唯一一个「模式 → 接了哪块 ADC」的实例** |
| **`mode()` 可以链式接别的成员函数** | 例子接着调 `.settling()` / `.samples()` / `.relay()` / `.min()` / `.max()`，最后才 `.execute()` |
| **`"VM_HIZ"` 也要给量程** | 例子里有 `.min(0 V).max(5 V)`——和 `"VM_HIZ_HAC"` 那格说的 `min()` / `max()` 是同一对函数 |
| **做 BADC 测量要包在 `ON_FIRST_INVOCATION` 里** | 例子的结构 |

**能落成动作的还有三条，全是从上文的约束推的**：

- **要 force 电流且用 `"IFVM"`**：先算钳位距离——原文说必须留最小距离；
  **不想管距离就上 AVI64/FVI16 的 `"CFVM"` / `"CFIM"`。**
- **开了 ganged 组又要测**：用 `"*_UNGANGED"` 期间**比较器会被静默关掉**，
  **而且不报错**——所以要靠别的手段确认比较器状态，不能靠「没收到告警」判断它还开着。
- **多个 pin 要同时用 BADC**：会报 resource conflict。
  **原文只说了这个错误会发，没给绕法**——要么串行，要么照它推荐改用 `FLEX_RELAY`。

## 和谁有关

- [[dc-scale-xps256-card]] — **最直接的一个**。`"VFVM"` / `"CFVM"` / `"CFIM"` 那一档的说明句
  **逐字写着 `supported only for the DC Scale XPS256 card`**，
  而且是本页语法节里**唯一**指向别的文档的链接。
  **那卡上讲这三档怎么用，本页只有「哪些卡上能选」这一句。**
- [[dps128-dps64-cards]] — **另一个被点名的硬件**。unganged 那段 `Note` 的第一句
  就是 `on DPS128/64 and XPS256 you cannot execute a current compare …`。
  **本页只有这一句副作用，那种卡本身不在本页。**
- [[flex-relay]] — **原文推荐的替代品**。
  `Note Although Board ADC measurements can be done with this function, it is recommend using the
  FLEX_RELAY class instead.`
  **本页只有「推荐用它」这半句；`FLEX_RELAY` 怎么用、和本函数差在哪，本页没有。**
- [[dc-test-programming]] — **上游，编程入口**。出现在原文 `Related information` 那三个粘连链接里
  （`SPMU_TASK` / `DC Test Programming` / `Measuring current or voltage in PMU operating mode`）。
  **本页是一个成员函数的定义；怎么在 DC 测试程序里组织这些调用、什么时候该在 testflow 的哪一段调，
  在那页。**
- [[xps256-pmu-operating-mode]] — **（推断）同族但不同层的「模式」**。
  本页的 `mode()` 设的是**测量模式**（force/measure 谁），那页从名字看讲的是 **PMU 工作模式**；
  **依据是两边都落在 PMU 上、且本页点名了 XPS256。**
  **本页没有那页的任何事实，两个「模式」是不是同一个概念本页也没验证。**
- [[dc-scale-uhc4t-card]] — **（推断）同族的 DPS 卡**。
  `clampError` 那格写的是 `the current clamp specification of the used DPS`，
  而 AVI64 / FVI16 这两个名字在原文里没有对应的 wiki 页；
  **依据只是「同一批 DC Scale 卡」。本页没有 UHC4T 的任何事实。**
- [[dps-pins-editor]] / [[digital-pins-editor]] — **`totalNumberOfGangedChannels` 的出处**。
  原文写 `Original number of ganged channels as defined in the pins editor` ——
  **只说 `the pins editor`，没指明是哪一个编辑器**；
  本 wiki 里这两个编辑器都在，**本页不替它选，两个都列**（**这是本页唯一没法定下来的关联**）。
- `SPMU_PIN_TASK`（**未建**）— **本页的宿主对象**。返回值的类型就是它，
  语法节里也链到它；**它整体提供哪些成员函数、怎么拿到一个实例，本页没有。**
- `SPMU_TASK`（**未建**）— **例子里的那个类**。例子第一行是 `SPMU_TASK badc_task;`
  **而不是 `SPMU_PIN_TASK`**；**这两个类型什么关系，本页一个字都没有**
  （原文只在 `Related information` 里列了它）。
- `SPMU_PIN_TASK.clamp()` / `.min()` / `.max()` / `.limits()` / `.iForce()` / `.vForce()`
  （**均未建**）— **本页反复点名的六个兄弟函数**：
  `"VM_HIZ_HAC"` 靠 `min()` / `max()` 选量程；`"CFVM"` / `"CFIM"` 靠 `clamp()` 设上下钳位；
  `iForce()` / `vForce()` 会自动改模式；unganged 那条公式要用 `limits()` 给的 P/F 限值。
  **每一个的签名与语义都在本页之外。**
- `Measuring current or voltage in PMU operating mode`（**未建**）—
  原文 `Related information` 里的第三个链接。**PMU 模式的用法在那篇。**
- `AVI64` / `FVI16`（**均未建**）— 两个被点名的硬件：`"IFVM"` 的钳位距离约束
  和版本段里各出现一次。**它们是什么卡、有什么别的模式，本页没有。**

## 版本

原文**有** `## Functional changes` 段，**五条**（逐字）：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.2.3: Support of IFVM_UNGANGED parameter with 7.2.3.1**
- **SmarTest 7.4.0: New measurement modes added for AVI64.**
- **SmarTest 7.5.0: New measurement modes added for FVI16.**
- **SmarTest 7.10.1: New measurement modes added for XPS256.**

**第一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以本页能确定的只有「6.3.2 之前就有这个函数」，具体哪个版本引入的，这份语料里没有。**

**后三条和语法节那张模式表冲突。** 版本说 AVI64（**7.4.0**）与 FVI16（**7.5.0**）
**加过新的测量模式**，而表里 `"CFVM"` / `"CFIM"` 那一档写的是
**`supported only for the DC Scale XPS256 card`**。
**若 CFVM/CFIM 只有 XPS256 支持，AVI64 / FVI16 在 7.4.0 / 7.5.0 加的是什么？**
**本页把三处并列（表里那句、`"IFVM"` 那格里的 AVI64/FVI16 那句、这三条版本条目），
不替它们调和。**

**第二条的 `with 7.2.3.1` 指代不明**：
是「7.2.3 起支持、7.2.3.1 起补全」，还是「随 7.2.3.1 一起支持」——
**原文没说，本页照抄。**

**与 wiki 面向的版本的关系**：本 wiki 的目标版本是 **SmarTest 7.10.3**。
五条里最后一条是 **7.10.1**，**在 7.10.3 之前**——所以**到 7.10.3 为止，本函数没有再变更的条目**。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md`

**本页没做的：**

- **`## 语法 / 参数` 节一个字没改**（§4）。**里面的 `### Syntax` / `### Return value` /
  `### Example` 三节的层级与链接改写都是脚本干的，本页只读不改。**
- **那条 unganged 公式不是从语法节来的。** 它在原文里属于
  `## Number of channels in unganged mode` 段，**落在脚本的抽取区间之外**
  （区间是 `## Syntax` → `## Example` 结束的代码块，见语法节里的 end 标记）。
  **所以本页正文里那条公式是我从原文正文转述的，不是逐字抽的**——
  **要精确到括号、空格和 `CEIL` 的写法，得回原文第 82–86 行。**
- **六个兄弟函数一个都没读**：`clamp()`、`min()`、`max()`、`limits()`、`iForce()`、`vForce()`。
  **这是本页最大的空缺**——**本页到处在说「量程去 min()/max() 拿」「钳位去 clamp() 设」
  「iForce() 会改模式」，但这六个函数各自的签名、单位、默认值、边界行为，本页一个字都没有。**
- **`SPMU_PIN_TASK` 对象本身没读** —— 所以**怎么拿到一个 `SPMU_PIN_TASK`、
  它除了 `mode()` 还有哪些成员、`pin()` 这类选择器怎么用，本页没有。**
- **`SPMU_TASK` 没读** —— 所以**例子里的 `SPMU_TASK` 和本页讲的 `SPMU_PIN_TASK` 什么关系，
  本页答不出**（原文一个字的说明都没有）。
- **`DC Scale XPS256 card` 没读** —— 所以 `"VFVM"` / `"CFVM"` / `"CFIM"` 在卡上怎么用、
  和 `xps256-pmu-operating-mode` 是不是同一套东西，**本页只有「哪些卡支持」这一句。**
- **`DPS128/64` 没读** —— 所以 unganged 下比较器被静默关掉这件事，**在那张卡上怎么绕，本页没有。**
- **`FLEX_RELAY` 没读** —— 原文推荐它替代 `"PPMU_BADC"`，**但推荐的理由原文没写，本页也补不出。**
- **`AVI64` / `FVI16` 的文档没读**（原文只在正文里点名这两个名字，没有链接到独立文档）
  —— 所以「它们在 7.4.0 / 7.5.0 加的是什么模式」这个冲突，**本页无法从别处核对**。
- **`Measuring current or voltage in PMU operating mode` 与 `DC Test Programming` 都没读。**
- **一张图都没有。** 原文没有图片。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：本页 `layer: L3`，所以本页没有去别处找它的层级定位。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 开头第一句有两个错。** 逐字：
> `Sets the measurement mode, like fore current measure voltage or force voltage measure current
> and connects the BADC or PPMU if required.`
> ——**`fore` 是 `force` 的错字**，且 **`force current measure voltage` 中间少了 `and`**
> （对照表里 `"IFVM"` 那格写的是 `Force current and measure voltage.`，可以确认）。
> **本页 `## 是什么` 照原样引，没有替它修。**
>
> **② 模式表的适用范围和正文冲突。** 表里那行写
> `The following measurement modes are supported only for the DC Scale XPS256 card.`，
> 而同一张表上面 `"IFVM"` 那格写
> `AVI64 and FVI16 support the real current forcing modes "CFVM" and "CFIM"`
> ——**同一批模式，一处说「只有 XPS256」，一处说 AVI64/FVI16 也支持。**
> **版本段那三条又分别给 AVI64 / FVI16 / XPS256 记了一笔。**
> **本页三处并列，不判哪个对。**
>
> **③ 公式括号不配对。** 逐字：
> `- No. of remaining ganged channels = CEIL [ P/F limit / (ilimitPerChannel ]`
> ——**`(` 开了没有关**，**`]` 关的是前面的 `[`**。
> **本页照原样引，不替它补右括号。**
>
> **④ `"CFIM"` 那一格没有描述，只有一个粘上去的 `Note`。** 逐字：
> ` | "CFIM"  | Note If the SPMU_PIN_TASK.iForce() or SPMU_PIN_TASK.vForce() is used, the
> corresponding mode("IFVM" or "VFIM") is set automatically.`
> ——**`Note` 与前一格之间没有分隔符，而且 `"CFIM"` 自己干什么原文没写**
> （`"CFVM"` 那格写的是 `Force current directly and measure voltage or current.`，
> 并且用 `if these modes are selected` 指代两档，像是共用一句）。
> **本页在表里照实写「原文这一格没写它做什么」。**
>
> **⑤ `Note` 后面一律没有分隔符。** 全篇四处，逐字开头：
> `Note that on DPS128/64 and XPS256 …`、`Note Although Board ADC measurements …`、
> `Note We recommend always, verifying …`、`Note If the SPMU_PIN_TASK.iForce() …`。
> **本页引文照原样，正文里加了分隔。**
>
> **⑥ `## Related information` 三个链接全粘在一起**，中间没有任何分隔符：
> `SPMU_TASK` + `DC Test Programming` + `Measuring current or voltage in PMU operating mode`。
>
> **⑦ 表里塞了一整句散文当行。** 逐字：
> ` | The following measurement modes are supported only for the DC Scale XPS256 card. |`
> ——**单格成行**，起的是「小标题」的作用，**所以从结构上看不出它是一个分组声明**；
> 这也就是为什么语法节里这一档的模式排在 `"PPMU_BADC"` 后面、中间只隔了这么一行。
>
> **⑧ 语法错误两处**，逐字：
> - `it is recommend using the FLEX_RELAY class instead` ——**应为 `it is recommended to use`
>   或 `recommended using`**；
> - `Note We recommend always, verifying current measurements …` ——**逗号位置不对**
>   （`recommend always, verifying` 应为 `recommend always verifying`）。
>
> **⑨ `with 7.2.3.1` 指代不明**（见 `## 版本`）：`Support of IFVM_UNGANGED parameter with
> 7.2.3.1` ——**这个 `with` 是「随该版本提供」还是「还需 7.2.3.1」，原文没说。**
>
> **⑩ 参数区没有段标记。** 原文里 `Parameter` 和 `Available options of parameter: mode`
> 是两个**裸词行**（不是 `##` / `###` 标题），**所以脚本只能把它们当正文抽进语法节**——
> 语法节里那两行读起来像残句，**这是原文的结构问题，不是脚本的错。**
>
> **⑪ `## Return value` 与 `## Example` 在原文里是 `##` 级**，
> 抽进语法节后成了 `###` 级（本页语法节里就是 `### Return value` / `### Example`）。
> **这是脚本往下一级的正常转换，记在这里只是为了说明层级和原文不一致。**
>
> **⑫ 本篇没有 §11.2 ① 那种 `鈥` 形态的编码损坏**（本页查过 `鈥`，0 处）。

`verified: doc-only`
