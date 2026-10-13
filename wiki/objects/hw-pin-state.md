---
type: object
title: HW_PIN_STATE
layer: L2
stage: pin
tags: [hw-pin-state, l2-api, test-method-api, hardware-status, pin-state, dps, sig, avi64, xps256, comparator, clamp, kelvin]
related: [hw-state, xps256-status-flags, xps256-pmu-operating-mode, dc-scale-xps256-card, on-first-invocation-begin, for-each-site-begin, pin, flag, test-method-class]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.01_HW_PIN_STATE.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# HW_PIN_STATE

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **351 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.01_HW_PIN_STATE.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

For an example, refer to

- `Example 1: Query the status outside the ON_FIRST_INVOVATION block`（raw: `02.07.04.01.117_HW_STATE.md#_105633__ex_Example_ON_FIRST_INVOCATION`） and
- `Example 2: Query the status in a FOR_EACH_SITE...WITH_QUERY block`（raw: `02.07.04.01.117_HW_STATE.md#_105633__ex_Example_FOR_EACH_SITE`）
in `HW_STATE`（raw: `02.07.04.01.117_HW_STATE.md`）.

<!-- 语法节 end -->

## 是什么

**`HW_PIN_STATE` 是 `HW_STATE` 的「子容器」——按 pin 存一份硬件设置，一个 getter 取一项。**

> 「This class is a subsidiary data container of the HW_STATE class.」

**它与 [[hw-state]] 的分工是原文写死的**（**这两页是一对，别分开读**）：

| 谁 | 管什么 | 依据 |
|---|---|---|
| [[hw-state]] | **从硬件读一次**，存进对象 | `You need to call this method every time the settings of the hardware are changed.` |
| **本页** | **按 pin、按项把值取出来** | `This class is a subsidiary data container of the HW_STATE class.` |

**你不能 new 它，也没有构造函数**：

> 「This class has no constructor.」

> 「You can access this class object via the pin() member function of the HW_STATE class by specifying the pin name. You cannot directly construct any objects of this class.」

（两句里的 markdown 链接标记已按 §11.1 ② 剥成纯文本。）

### 头文件与唯一的访问路径

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/HwPinState.h.」

`hwState.pin ("DPS_pin_1").getVoltageForce()` —— **`pin()` 是唯一入口**，没有第二条路。

### 一条贯穿全页的前置条件：**先 `getStatus()`**

> 「For all of the member functions, listed above, the HW_STATE member function getStatus() member function must be called upfront to retrieve the data from the hardware.」

**这句话是对「上面列出的所有成员函数」说的**——**下面那 40 个 getter 一个都不例外。**
**所以本页每个 getter 都隐含同一句**：**先 `HW_STATE::getStatus(pinlist)`，再 `pin(pinName).getXxx()`。**

> 原文这一句里 **`member function` 连着出现两次**（`the HW_STATE member function getStatus() member function`），
> `Member functions` 那个小标题后面也**少一个冒号**——**上游如此**，见「出处」⚠️。

### 40 个成员函数：**原文自己按返回类型分成三组**

| 组 | 个数 | 成员（原文的函数名） |
|---|---|---|
| **返回 `DOUBLE`** | **31** | 见下 |
| **返回 `INT`** | **2** | `getActiveChannels()` / `getStackLevel()` |
| **返回 `STRING`** | **7** | `getCompSelector()` / `getConnectState()` / `getLoadStepMode()` / `getOpenLoopProtection()` / `getPulldownState()` / `getReferencePin()` / `getVoltageClampState()` |

**共 40 个**（数法见「出处」）。原文在类定义那一节给了三张导航表，
又在三个 `## ` 小节里逐个展开——**两处的个数一致**（31 / 2 / 7）。

### 31 个 `DOUBLE`：按「量什么」分三堆

| 堆 | 成员 | 单位（原文写了才写） |
|---|---|---|
| **force / clamp 的电压与电流** | `getVoltageForce()` `getVoltageForceMax()` `getVoltageForceMin()` `getVoltageClampLow()` `getVoltageClampHigh()` `getVoltageClampMax()` `getVoltageClampMin()` `getCurrentForce()` `getCurrentForceMax()` `getCurrentForceMin()` `getCurrentClampSource()` `getCurrentClampSink()` `getCurrentClampMax()` `getCurrentClampMin()` | **都不写单位**（原文只有 `It returns the real value of the hardware.`） |
| **速率 / 滤波 / 电容 / 时间** | `getVoltageSlew()` `getCurrentSlew()` `getLoadcap()` `getMeasFilter()` `getVoltageForceFilter()` `getCurrentClampFilter()` `getCompHoldOff()` | `mV / 碌s`、`A / s`、`碌F`、`Hz`、`Hz`、**`ns`** |
| **余量 / 预算 / 压降阈值** | `getCompHysteresis()` `getDCPower()` `getPulseEnergy()` `getComplianceValue()` `getVoltageDropMaxForce()` `getVoltageDropMaxReturn()` `getVoltageDropWarnForce()` `getVoltageDropWarnReturn()` `getConstCurrTimeToAlarm()` `getConstCurrTimeToDisconnect()` | `%`、`mW`、`mJ`，其余不写单位 |

**三堆合计 14 + 7 + 10 = 31。**
**`碌` 是坏字（正字 `µ`）**，见「出处」⚠️。

### `NaN` 是「这一项对这根 pin 不适用」的统一答复

原文里 **`NaN (Not a Number)` 出现 29 次**，句式几乎一致：

> 「If this setting of the hardware is not applicable, NaN (Not a Number) is returned.」

**所以「拿到 `NaN`」不是出错，是「这一项与这根 pin 不搭」。**
**29 次里有 6 次是带例子的长句，句法上少一个左括号**，逐字：

> 「If this setting of the hardware is not applicable for example, filter value is set to "OFF" or the hardware does not support the filter), NaN (Not a Number) is returned.」

**6 处**分别是：`getCurrentClampFilter()`、`getCurrentSlew()`、`getDCPower()`、
`getPulseEnergy()`、`getVoltageForceFilter()`、`getVoltageSlew()`。

> ⚠️ **两个 `INT` 函数也照抄了这句话。** `getActiveChannels()` 与 `getStackLevel()` 的原文都写
> `If this setting of the hardware is not applicable, NaN (Not a Number) is returned.`，
> **而它们的返回类型是 `INT`**——**`INT` 里没有 `NaN`。**
> **这是原文自相矛盾的一处，本页照记，不替它改**（见「出处」⚠️）。

### XPS256 独有的 **7 项**：原文用两句固定话划界

`The function is supported only with DC Scale XPS256 card.`（2 处）与
`The function is supported only for the DC Scale XPS256 card.`（5 处）：

| 成员 | 原文用的句式 |
|---|---|
| `getConstCurrTimeToAlarm()` | `The function is supported only with DC Scale XPS256 card.` |
| `getConstCurrTimeToDisconnect()` | `The function is supported only with DC Scale XPS256 card.` |
| `getVoltageDropWarnForce()` | `The function is supported only for the DC Scale XPS256 card.` |
| `getVoltageDropWarnReturn()` | `The function is supported only for the DC Scale XPS256 card.` |
| `getLoadStepMode()` | `The function is supported only for the DC Scale XPS256 card.` |
| `getPulldownState()` | `The function is supported only for the DC Scale XPS256 card.` |
| `getOpenLoopProtection()` | `The function is supported only for the DC Scale XPS256 card.` |

**「只有 7 项」是本页数出来的**（原文没有一句 `These 7 functions …` 的总起句）——
**判据是上面那两句固定话在正文里各出现几次。**

### 7 个 `STRING` getter：**只有两个给了表，其余五个只给一行取值**

| getter | 取值（原文逐字） |
|---|---|
| `getCompSelector()` | **带一张三列表**：`"na"` / `"LS"` / `"LS_DIFFVM"` / `"HS"` / `"HS_TERM"` / `"HS_DIFFERENTIAL"` |
| `getConnectState()` | **带一张三列表**：`"FAST"` / `"NORMAL"` / `"PULSE"` |
| `getLoadStepMode()` | `Possible return values are "STD" or "FAST".` |
| `getOpenLoopProtection()` | `Possible return values are "DIODE" or "NONE".` |
| `getPulldownState()` | `Possible return values are "ON" or "OFF".` |
| `getReferencePin()` | **不是枚举**：`The function returns "GND" if the reference pin is not defined or is defined as TM::REF_GND for measure modes that support a reference pin.` |
| `getVoltageClampState()` | **两个值**：`This function queries the clamp status. It returns "ON" or "OFF".` |

**`getCompSelector()` 那张表**（**`Supported pin types` 那一列把大多数取值限定到 `SIG (AVI64 only)`**）：

| Returned value | Meaning | Supported pin types |
|---|---|---|
| `"na"` | 比较器不适用或未定义 | `DPS, SIG` |
| `"LS"` | 高分辨率电压 / 电流比较器。**AVI64 通道在 PMU operating mode 下的默认比较器。** | `SIG (AVI64 only)` |
| `"LS_DIFFVM"` | 差分电压表的高分辨率电压比较器 | `SIG (AVI64 only)` |
| `"HS"` | 高速数字电压比较器 | `SIG (AVI64 only)` |
| `"HS_TERM"` | 端接的高速数字电压比较器。**输入经 `50 O` 端接到地。** | `SIG (AVI64 only)` |
| `"HS_DIFFERENTIAL"` | 差分高速数字电压比较器 | `SIG (AVI64 only)` |

> **`50 O` 里的 `O` 是字母 `O`，不是 `Ω`。** 逐字：
> `Input signal is terminated to ground via 50 O.`
> **上游核对**：`105632.htm` 里就是 `50 O.` → **上游就坏的**（§11.2 ⑥），**本页照原样写**。
> （**`Ω` 在这套语料里另有坏法**——§11.2 ① 记的那个 `惟`；**本篇这里是干净的 ASCII `O`**，
> 属于「看起来完全正常、其实不对」的那一类，**只能靠上下文认出来**。）

**`getConnectState()` 那张表**（**md 里第一行数据前面多出一个空单元格**——见「出处」⚠️）：

| Returned value | Meaning | Supported pin types |
|---|---|---|
| `"FAST"` | 快速 VI 模式 | `SIG` |
| `"NORMAL"` | DPS 应用的默认模式 | `DPS, SIG` |
| `"PULSE"` | 大电流模式 | `DPS, SIG` |

> ⚠️ **`getConnectState()` 的取值清单与版本段对不上。**
> 表里**只有三个取值**；而 `## Functional changes` 里给这个函数**另外列了 6 个新取值**：
> `"SENSE_ONLY"` `"SAFE_CONNECT"`（7.4.0）、`"KELVIN_REVERSE"` `"FORCE_ONLY"`（7.4.1）、
> `"HIGH_VOLTAGE"`（7.5.0）、`"FS_OVERRIDE"`（7.5.1）——**那 6 个值在取值表里一个都没有。**
> **原文如此，本页两处并列照记，不替它补表、也不替它判定谁过时。**

**另外 38 个 getter 都没有「支持哪些 pin」这一列**：
它们的说法只有 `If this setting of the hardware is not applicable, NaN (Not a Number) is returned.`
（`STRING` 那组里除 `getConnectState()` 外的四个写的是 `If this setting of the hardware is not applicable, "na" is returned.`）

> **`getConnectState()` 是唯一没有 `"na"` 那一句的 `STRING` getter**——
> 它既没有 `"na"` 兜底，表里也没有 `SENSE_ONLY` 那 6 个值。**两处缺口叠在一起。**

### 两处「函数名 / 签名 / 说明」的错位（**都是上游就坏的**）

| 位置 | 原文逐字 | 问题 |
|---|---|---|
| `getCurrentForceMax()` 那一节的**签名** | `DOUBLE getVoltageForceMax() const;` | **节标题是 `getCurrentForceMax`，签名却是 `getVoltageForceMax`** |
| `getVoltageForceMax()` 那一节的**说明** | `This function queries the maximum force current of the specified pin.` | **函数名是 voltage，说明写的是 force current** |

**再加一条**：`getCurrentForceMax()` 那一节的**说明文字与 `getVoltageForceMax()` 的完全一样**
（两句都是 `This function queries the maximum force current of the specified pin. It returns the real value of the hardware.`
/ `If the maximum force current of the hardware is not applicable, NaN (Not a Number) is returned.`）
—— 那一节**疑似整段复制自 `getVoltageForceMax()`**。
**三处（名字 / 签名 / 说明）该信哪一个，原文没说**，本页照记不判。

## 典型用法

**先说范围**：本篇**没有 `## Procedure`、没有 `## Before you begin`、没有 `## Application`，
也没有 `## Errors` 段**。

**而且本篇的 `## Example` 一节没有自己的例子**，它把读者送到 [[hw-state]] 去：

> For an example, refer to
>
> - Example 1: Query the status outside the ON_FIRST_INVOVATION block and
> - Example 2: Query the status in a FOR_EACH_SITE...WITH_QUERY block
> in HW_STATE.

> **上面这一块是逐字引的**（只剥了 markdown 链接标记，§11.1 ②）——
> 所以那三个 `- ` 列表符与行末的 `and` / `in HW_STATE.` 都按原样留着。
> **注意它照抄了 `ON_FIRST_INVOVATION` 这个少一个 `C` 的拼写**（见「出处」⚠️）；
> **`FOR_EACH_SITE...WITH_QUERY` 里那三个点也是原文自带的**（§11.1）。

**所以用法一律照 [[hw-state]] 的流程走，只是取值这一步落到本页的 getter 上**：

**1. 先把快照读进来**：`hwState.getStatus ("pin1, pin2");`
位置二选一：`ON_FIRST_INVOCATION` 块**外**，或 `FOR_EACH_SITE...WITH_QUERY` 块**内**。
（**这两句是 [[hw-state]] 写的**；本页只说 `getStatus()` **必须**先调过。）

**2. 按 pin 拿子对象**：`hwState.pin ("DPS_pin_1")` —— **pin 必须是第 1 步点过名的**
（[[hw-state]]：`If the pinName is empty or is not in the pinList of getStatus(), an error message will be thrown out and no setting will be returned.`）。

**3. 调一个 getter**：`getVoltageForce()` / `getCurrentClampSource()` / …… 40 选 1。

**4. 换一项就换一个 getter，不用重新 `getStatus()`。**
**（推断）**：依据是 [[hw-state]] 那句
`The data read from the hardware and stored in the HW_STATE object can be retrieved per pin and property by the pin() function …`
——**「per pin and property」说的是同一份快照里按 pin、按项取。**
**本篇没有这一句**，所以这是推断。

**5. 拿到 `NaN`（`DOUBLE` / `INT`）或 `"na"`（部分 `STRING`）→ 这一项对这根 pin 不适用**，
**不是错误**。

**6. 要读压降**（仅 XPS256）：**先 `HW_STATE::readMaxAbsVdropsParallel()`，再 `getMaxAbsVdrops()`**
——**顺序不能反**（[[hw-state]] 原文 `must be called upfront`）。

## 和谁有关

- [[hw-state]] — **父类（前置）**，**这一对是本页最重要的关系**。三处都在原文里：
  ① 第一句：`This class is a subsidiary data container of the HW_STATE class.`
  ② **访问入口只有它的 `pin()`**：`You can access this class object via the pin() member function of the HW_STATE class by specifying the pin name. You cannot directly construct any objects of this class.`
  ③ **例子里用的两个 getter（`getVoltageForce()` / `getCurrentClampSource()`）就是本页的。**
  **本页原文只写「必须先调 `getStatus()`」；「值是调用那一刻的快照」那一句在 [[hw-state]] 里**——
  **本篇没有这句。**
- [[xps256-status-flags]] — **下游，而且是本页最实的一条跨页关系**：
  `getVoltageDropWarnForce()` 与 `getVoltageDropWarnReturn()` 的原文**直接点了那两个 flag 的名字**——
  前者 `This function queries the force drop voltage threshold (above which the "Voltage drop force warning" status flag is set), of the specified pin.`，
  后者 `… (above which the "Voltage drop return warning" status flag is set) …`。
  **`"Voltage drop force warning"` 与 `"Voltage drop return warning"` 正是 [[xps256-status-flags]] 里的两个标志**
  （那一页给了它们的 `Trigger` / `Action` / `Availability` / `API`）。
  **那一篇本页没读**，所以**「阈值到了会怎样、怎么清」本页没有。**
- [[xps256-pmu-operating-mode]] — **一处取值说到了它**：`getCompSelector()` 表里 `"LS"` 那一格写着
  `This is the default comparator for an AVI64 channel in the PMU operating mode.`
  **那一篇本页没读。**
- [[dc-scale-xps256-card]] — **7 个 XPS256 独有 getter 的卡级前提**。
  **那一篇本页没读**，所以**「为什么这 7 项只能用在 XPS256 上」本页没有。**
- [[on-first-invocation-begin]] / [[for-each-site-begin]] — **`getStatus()` 的两个允许位置**
  （**那两句在 [[hw-state]] 里，不在本页**）。**两篇本页都没读。**
- [[pin]] — **`pin()` 的参数、`getReferencePin()` 的参考针**，
  也是 frontmatter `stage: pin` 的依据。
- [[flag]] — 本页两处 `status flag` 指的是它。
- [[test-method-class]] — 本页是 Test Method API（`layer: L2`）里的一员：
  有头文件、靠别的对象访问、成员函数按返回类型分组。
- `HW_STATE.getStatus()` / `HW_STATE.pin()` / `FOR_EACH_SITE_BEGIN_WITH_QUERY` /
  `CURRENT_SITE_NUMBER()` / `TM::REF_GND` — **五个名字本篇都提到了，本页都不链**
  （**不在 allowlist 里**，§9.1）。

**本页没有引用 `edges.jsonl` 的入边 / 出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，段里有 14 条**：

| 版本 | 内容（原文逐字） |
|---|---|
| — | `Introduced in SmarTest 6.5.0` |
| **SmarTest 7.3.1** | `New member functions getVoltageForceFilter(), getCurrentClampFilter().` |
| **SmarTest 7.3.1** | `New member function getConnectState().` |
| **SmarTest 7.4.0** | `New return values "SENSE_ONLY" and "SAFE_CONNECT" of member function getConnectState()` |
| **SmarTest 7.4.0** | `New member functions getVoltageSlew(), getCurrentSlew(), getLoadcap()` |
| **SmarTest 7.4.0** | `New member functions getReferencePin(), getCompHysteresis()` |
| **SmarTest 7.4.0** | `New member functions getMeasFilter(), getCompSelector()` |
| **SmarTest 7.4.1** | `New return values "KELVIN_REVERSE" and "FORCE_ONLY" of member function getConnectState()` |
| **SmarTest 7.5.0** | `New member functions getVoltageDropMaxForce(), getVoltageDropMaxReturn(), getComplianceValue(), getActiveChannels(), getStackLevel()` |
| **SmarTest 7.5.0** | `New return value "HIGH_VOLTAGE" of member function getConnectState()` |
| **SmarTest 7.5.1** | `New member functions getCompHoldOff(), getDCPower(), getPulseEnergy()` |
| **SmarTest 7.5.1** | `New return value "FS_OVERRIDE" of member function getConnectState()` |
| **SmarTest 7.10.1** | `New member functions getConstCurrToAlarm(), getConstCurrToDisco(), getVoltageDropWarnForce(), getVoltageDropWarnReturn(), getLoadStepMode(), getPulldownState()` |
| **SmarTest 7.10.3** | `New member function getOpenLoopProtection()` |

**四条读法**：

- **第一条不是哨兵值**：写的是 `Introduced in SmarTest 6.5.0`（**不是 `before`**），
  **所以这一条就是「6.5.0 引入了 HW_PIN_STATE」**，与 [[hw-state]] 同批引入
  （那一篇的第一条也是 `Introduced in SmarTest 6.5.0`）。→ [[smartest-6.5.0]]
- **有一条里的两个函数名是缩写、与正文对不上**：7.10.1 那条写的是
  `getConstCurrToAlarm(), getConstCurrToDisco()`，
  **而正文里这两个函数叫 `getConstCurrTimeToAlarm()` 与 `getConstCurrTimeToDisconnect()`**。
  **版本段的名字更短，正文的名字更长，原文两处都这样**——见「出处」⚠️，**本页照记不判**。
- **5 条与 `getConnectState()` 有关**（1 条引入 + 4 条加返回值），
  而那 4 条加的 **6 个取值在取值表里一个都没有**（见「是什么」）。
- **7.10.3 是本 wiki 面向的版本**：那一条只加了 `getOpenLoopProtection()` 一个函数。

**版本段里没有的东西（照实记）**：
**`checkKelvinStatus()` 那一族不在这里**——它们是 [[hw-state]] 的成员，记在那一篇的版本段里。
**本页 14 条里没有任何一条提到 `getStatus()` / `pin()`**，因为它们不是本类的成员。

## 出处

`sources:` 一篇：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.01_HW_PIN_STATE.md`
  （frontmatter 的 `source_topic` 是 `105632.htm`；**20,104 字节 / 523 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径。**这是本批四篇里最长的一篇。**）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。
  **要留意它只抽到了 `## Example` 一节**——**本篇的类定义与 40 个成员函数都不在段标记里**，
  所以它们由本页正文补述（§4 的分工：段标记能抽的脚本抽，抽不到的**从读过的原文里写**，
  不许猜）。
- **「40 个」的数法**（§11.5 口径）：按三个 `## Member functions returning …` 小节里的
  成员函数小节标题逐个点（`^  getXxx()`），得 **31 / 2 / 7**；
  再用三张签名行核对（`DOUBLE … const;` / `INT … (void) const;` / `STRING … const;`）。
  **`getStatus` 不算本类成员**——它出现在正文那句 `Note` 的句子里，是 [[hw-state]] 的函数。

**本页没做的**：

- **原文点到的 `HW_STATE` 那一篇，本页按「同一对」读了它的两个例子**——
  但**本页只读了自己这一篇的 raw**；上面凡是标了「[[hw-state]] 写的」的句子，
  **都是从那一篇的原句转引，不是本页的推断**。
- **四个子页一篇都没读**：`HW_STATE.checkKelvinStatus()` /
  `HW_STATE.checkKelvinStatusParallel()` / `HW_STATE.checkGangConnection()` /
  `HW_STATE.checkGangConnectionParallel()`。
  **本篇只在 `## Subtopics` 与 `Related information` 里点到 `HW_STATE.checkKelvinStatus()` 一处**，
  **所以那四个函数本页一个字都没有。**
- **`Related information` 一节本篇根本没有**（原文的节序是 `## Example` → `## Functional changes`）——
  **不是本页没读，是原文没有这一节。**
  类定义那一段里的 `## Subtopics` 倒是列了五个子主题，**五个本页都没读。**
- **`## Errors` / `## Warnings` 两节本篇都没有**，
  所以**「pin 名写错、函数不支持这台机器时会怎样」本页答不了**（原文只在 `getStatus()` / `pin()`
  那两处借 [[hw-state]] 说了「会抛 error message」）。
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**；上游 `105632.htm` 里也 **0 个 `<img>`、0 个图片路径**
  （`src=` 只有 1 处，是那个 `p.css` 样式表）。
  **所以本页没有任何来自图的结论**——**「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上编过、也没跑过 `HW_PIN_STATE`**（`verified: doc-only`）。
  **所以「哪些项在真机上真会回值、哪些项常年 `NaN`」本页答不了（§11）。**
- **§10 重复投放：本篇在语料里只有一份**（按文件名全树 glob，1 命中）——
  **不存在 ETIM 那种三份投放的情况。**

### 上游 `.htm` 核对（本页做的一步）

**下面五条去上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\105632.htm`（37,008 字节）核过。
结论：坏字两处是「转换坏的（可救）」，其余是「上游本来就这样（救不回来）」——逐条分开了。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 坏字 `碌`：`碌F`（微法）与 `mV / 碌s`（毫伏每微秒），正字是 `µF` 与 `µs`。**
> 原文逐字（**坏字照引**）：
> `This function queries the specified load capacitance of the specified pin. It returns the real value of the hardware. The unit of the returned value is 碌F (Microfarad).`
> 与 `The unit of the returned value is mV / 碌s (Millivolt per microsecond).`
> **上游核对**：`105632.htm` 里写的是 `µF` 与 `mV / µs`，**µ 是好的**
> → **HTML→md 转换坏的（§11.2 ①那一族），可救**；
> **但本页照原样引，一处不改**（§11.2 ①：拿修好的字回 raw 里搜是搜不到的）。
> **本篇的汉字一共只有这 2 个**（`碌`×2），**都在这一处。**
>
> **② `50 O` ——不是坏字，是「看着正常、其实不对」。** 原文逐字：
> `Input signal is terminated to ground via 50 O.`
> **上游核对**：`105632.htm` 里就是 `50 O.` → **上游就坏的**（§11.2 ⑥）。
> **`Ω` 在这套语料里另有坏法**（§11.2 ① 记的 `惟`），**而这里是一个干净的 ASCII `O`**——
> **编码检测抓不到它，只能靠上下文认出「这里应该是 Ω」。**
> **本页照原样写 `50 O`，没有改成 `Ω`。**
>
> **③ `getCurrentForceMax()` 的签名是 `getVoltageForceMax()`。** 原文逐字（那一节的两行）：
> `getCurrentForceMax()` 与
> `DOUBLE getVoltageForceMax() const;`
> **上游核对**：`105632.htm` 里那一段的标题是 `getCurrentForceMax()`、
> **紧跟的 `<pre>` 里就是 `DOUBLE getVoltageForceMax() const;`** → **上游就坏的**（§11.2 ⑥）。
> **同一处还有第三个问题**：那一节的说明文字与 `getVoltageForceMax()` 那一节**逐字相同**，
> 而 `getVoltageForceMax()` 的说明写的是 `This function queries the maximum force current of the specified pin.`
> —— **函数名是 voltage、说明是 force current**。**上游核对**：`105632.htm` 里两节都是这句话
> → **上游就坏的。**
>
> **④ `getActiveChannels()` / `getStackLevel()` 的「`NaN`」与它们的返回类型矛盾。**
> 原文逐字（两个函数各一遍）：
> `If this setting of the hardware is not applicable, NaN (Not a Number) is returned.`
> 而两条签名是 `INT getActiveChannels(void) const;` 与 `INT getStackLevel(void) const;`
> ——**`INT` 里没有 `NaN`。**
> **上游核对**：`105632.htm` 里这两句就是照抄来的 → **上游就坏的**（§11.2 ⑥）。
>
> **⑤ 两处「结构被压平 / 上游缺字」：**
>
> - **`getConnectState()` 取值表头一行多一个空单元格。** md 逐字：
>   ` | Returned value  | Meaning  | Supported pin types |` 下一行就是
>   ` |   | "FAST"  | The fast VI mode.  | SIG |`——**数据行有 4 格，表头只有 3 格。**
>   **上游核对**：`105632.htm` 里那一行是 `Returned value || Meaning || Supported pin types || || || "FAST" || …`
>   → **上游就坏的表结构**（§11.2 ⑥），不是脚本切错。
> - **`  Member functions  Member functions returning DOUBLE:` 后面少一个冒号、
>   而且 `member function` 在一句话里重复。** 原文逐字：
>   `For all of the member functions, listed above, the HW_STATE member function getStatus() member function must be called upfront to retrieve the data from the hardware.`
>   **上游核对**：`105632.htm` 里就是 `the HW_STATE member function getStatus() member function must be called`，
>   小标题也是 `Member functions  Member functions returning DOUBLE:`
>   → **上游就坏的。**
> - **`getConstCurrToAlarm()` / `getConstCurrToDisco()` 是版本段里的缩写名。**
>   原文逐字（7.10.1 那一条）：
>   `SmarTest 7.10.1: New member functions getConstCurrToAlarm(), getConstCurrToDisco(), getVoltageDropWarnForce(), getVoltageDropWarnReturn(), getLoadStepMode(), getPulldownState()`
>   而正文的正式名是 `getConstCurrTimeToAlarm()` / `getConstCurrTimeToDisconnect()`。
>   **上游核对**：`105632.htm` 的 `Functional changes` 里就是 `getConstCurrToAlarm(), getConstCurrToDisco()`
>   → **上游就坏的**（§11.2 ⑥）。**本页照原样引这两个短名，没替它改成长名。**
>
> **⑥ 坏字合计：本篇 2 个汉字**（`碌`×2），**都在 ⚠️① 那一处**。
> 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **除这一处外，本篇没有别的汉字**——
> **但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
