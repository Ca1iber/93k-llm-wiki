---
type: object
title: EVENT_WAVEFORM_VFIM
layer: L3
stage: testmethod
tags: [event, waveform, vfim, force-measure, combined, analog-waveform, event-base, constructor, implicit-id]
related: [event-base, event-waveform-vfvm, smartest-6.5.2, smartest-7.4.0]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38_EVENT_WAVEFORM_VFIM.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# EVENT_WAVEFORM_VFIM

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **965 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38_EVENT_WAVEFORM_VFIM.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
class EVENT_WAVEFORM_VFIM : public EVENT_BASE

    EVENT_WAVEFORM_VFIM(const STRING & id);
    EVENT_WAVEFORM_VFIM(      INT      id);
    EVENT_WAVEFORM_VFIM();
```

This constructs an object of the EVENT_WAVEFORM_VFIM class. The class derives from the `EVENT_BASE`（raw: `02.07.04.01.63.01_EVENT_BASE.md`） class.

When using the EVENT_WAVEFORM_VFIM() constructor, the event ID is implicitly derived from the name of the assigned ANALOG_WAVEFORM. The event ID will look like: WAV_waveformName

Parameter
 | Parameter  | Description |
 | id |

Identifier of the event.

The identifier may be defined as integer value or as string.

 |

### Example

- Describes the waveform of a voltage ramp:

```
ANALOG_WAVEFORM rampUp("rampUp");

rampUp.definition(TM::RAMP)
      .direction(TM::POS)
      .samples(4)
      .min(0.1).max(1.6);
```

- Defines a force voltage ramp waveform:

```
EVENT_WAVEFORM_VF rampUpEvent;
rampUpEvent.vForce(rampUp);
rampUpEvent.sampleVectorDistance(64);
```

<!-- 语法节 end -->

## 是什么

**`EVENT_WAVEFORM_VFIM` = `Voltage Force / Current Measure Waveform`**——
**「加电压、同时测电流」的波形事件类。**

> 「Specialized force/measure waveform classes are EVENT_WAVEFORM_VFIM (Voltage Force / Current
> Measure Waveform) and EVENT_WAVEFORM_VFVM (Voltage Force / Voltage Measure Waveform).」

**它和它的兄弟属于「合体」那一族**：

> 「Combined force/measure waveform classes provide functionality to define events, which
> generate waveforms, and measure at the same point in time when the samples are applied to
> the frontend.」

**这一句定义了整族的能力，三个要点：**

| 要点 | 原文 |
|---|---|
| **既定义 event、又生成波形** | `define events, which generate waveforms` |
| **还测量** | `and measure` |
| **测的时机是「采样加到前端的同一时刻」** | **`at the same point in time when the samples are applied to the frontend`** |

> **第三点是这一类存在的理由**：**「加」与「测」不是先后两步，是同一时刻**——
> **所以它是「combined」而不是「先 force 再 measure」。**

**定义在头文件** `/opt/hp93000/soc/prod_com/include/MAPI/Events.h`。

### 名字怎么读：`VFIM` 是三个词拼的

原文把 `VFIM` 和 `VFVM` 两个缩写展开了：

| 类 | 原文展开 | 拆开读 |
|---|---|---|
| **`EVENT_WAVEFORM_VFIM`** | **`Voltage Force / Current Measure Waveform`** | **`VF`** = Voltage Force、**`IM`** = Current Measure |
| **`EVENT_WAVEFORM_VFVM`** | **`Voltage Force / Voltage Measure Waveform`** | **`VF`** = Voltage Force、**`VM`** = Voltage Measure |

**两者只差 `I` 与 `V`——即「测的是电流还是电压」。**
**`Related information` 里还有两个同类**：`EVENT_WAVEFORM_VF`（应该只加不测）与
`EVENT_WAVEFORM_IM`——**但那两个名字原文没有展开，本页也不展开**（**推断**：
本页只从命名形状看出它们属于同一族，**原文没说**）。

### 三个构造函数，**其中一个会替你造 `id`**

原文 `## Syntax` 里的类声明（**逐字**）：

```
class EVENT_WAVEFORM_VFIM : public EVENT_BASE

    EVENT_WAVEFORM_VFIM(const STRING & id);
    EVENT_WAVEFORM_VFIM(      INT      id);
    EVENT_WAVEFORM_VFIM();
```

> 「This constructs an object of the EVENT_WAVEFORM_VFIM class. The class derives from the
> EVENT_BASE class.」

**第三行那个无参构造函数有一条特殊规则，本页最要紧的一条**：

> 「When using the EVENT_WAVEFORM_VFIM() constructor, the event ID is implicitly derived from the
> name of the assigned ANALOG_WAVEFORM. The event ID will look like: **WAV_waveformName**」

**即：不传 `id` 也能建——`id` 会由**被赋给它的 `ANALOG_WAVEFORM` 的名字**自动生成，
形状是 `WAV_` 前缀 + 波形名。**

**`id` 参数的原文说明**（那条参数表的文字部分）：

> 「Identifier of the event. The identifier may be defined as integer value or as string.」

**两种给法：整数或字符串**——**与基类 [[event-base]] 的 `id` 规则一致**
（**推断**：依据是两篇的参数说明措辞相同；**本页没有读基类那篇的源码**）。

### `## Subtopics` 里的第 14 个成员函数（**本页只拿到名字**）

原文把本类的成员函数**全部拆成了子页**，一共 **14 篇**：

| # | 子页（原文） | 从名字看是 |
|---|---|---|
| 1 | `EVENT_WAVEFORM_VFIM.vForce()` | 设「加什么电压」 |
| 2 | `EVENT_WAVEFORM_VFIM.getVForce()` | 读回来 |
| 3 | `EVENT_WAVEFORM_VFIM.sampleVectorDistance()` | 设采样点间隔 |
| 4 | `EVENT_WAVEFORM_VFIM.getSampleVectorDistance()` | 读回来 |
| 5 | `EVENT_WAVEFORM_VFIM.getSamples()` | **只读**（**没有对应的 setter**） |
| 6 | `EVENT_WAVEFORM_VFIM.averages()` | 设平均次数 |
| 7 | `EVENT_WAVEFORM_VFIM.getAverages()` | 读回来 |
| 8 | `EVENT_WAVEFORM_VFIM.clampChecks()` | 设钳位检查 |
| 9 | `EVENT_WAVEFORM_VFIM.getClampChecks()` | 读回来 |
| 10 | `EVENT_WAVEFORM_VFIM.iClampChecks()` | **电流**侧的钳位检查（**推断**：`i` 前缀） |
| 11 | `EVENT_WAVEFORM_VFIM.getIClampChecks()` | 读回来 |
| 12 | `EVENT_WAVEFORM_VFIM.outOfRangeCheck()` | 超量程检查 |
| 13 | `EVENT_WAVEFORM_VFIM.getOutOfRangeCheck()` | 读回来 |
| 14 | `EVENT_WAVEFORM_VFIM.getRepeatCount()` | **只读**（**没有对应的 setter**） |

**这张表有三条可以直接看出来的规律**（**推断**：本节全部结论来自「14 个名字」，
**不是那 14 篇的内容**）：

1. **成对出现**：13 个 setter 配 getter 的模式里，**只有 `getSamples()` 与 `getRepeatCount()`
   是孤儿**——**没有对应的 `samples()` / `repeatCount()`**。**这两项大概率是别处算出来的或别处设的。**
2. **`clampChecks` / `iClampChecks` 分成两组**：**电压侧与电流侧**——
   **和 `VFIM` 这个类「加电压、测电流」的双重身份对得上**。
3. **本页没有拿到任何一个成员函数的签名、参数或语义**——
   **它们全在那 14 篇子页里**（见「出处」）。

### 本页能确定的**唯一**一条版本事实

`clampChecks()` 与 `getClampChecks()` 是 **SmarTest 7.4.0** 加的（见「版本」）——
**即上面第 8、9 两项在那之前不存在。**

## 典型用法

**⚠️ 本文档的 `## Example` 只有两段代码，没有过程、没有 `Before you begin`。**
**两段代码里只有第二段属于本类**（**第一段是 `ANALOG_WAVEFORM`，见下**），
**而且第二段用的类名不是本页的类**（见「出处」的 ⚠️ ①）。**本页照实引，照实说明。**

**第一步：先把波形定义出来**（原文第一段，逐字）——原文的说明是
`Describes the waveform of a voltage ramp:`

```
ANALOG_WAVEFORM rampUp("rampUp");

rampUp.definition(TM::RAMP)
      .direction(TM::POS)
      .samples(4)
      .min(0.1).max(1.6);
```

**读法**：**造一个名为 `rampUp` 的模拟波形** → **定义成 `TM::RAMP`（斜坡）** →
**方向 `TM::POS`（正）** → **4 个采样点** → **幅度从 `0.1` 到 `1.6`**。
**链式写法，五次调用串在一句里。**

**第二步：把波形挂到事件上，并设采样点间隔**（原文第二段，逐字）——原文的说明是
`Defines a force voltage ramp waveform:`

```
EVENT_WAVEFORM_VF rampUpEvent;
rampUpEvent.vForce(rampUp);
rampUpEvent.sampleVectorDistance(64);
```

**读法**：**建一个事件** → **`vForce(rampUp)` 把上一步的波形赋给它** →
**`sampleVectorDistance(64)` 设采样点间隔为 64**。

> **⚠️ 第二段声明的类型是 `EVENT_WAVEFORM_VF`，不是本页的 `EVENT_WAVEFORM_VFIM`**——
> **原文如此，本页不替它改**（见「出处」⚠️①）。
> **所以这两段代码能不能直接用在 `VFIM` 上，本文档没说。**

**由这两段能拼出的顺序**（**推断**，依据是两段的先后与无参构造函数的隐式 `id` 规则）：

**① 定义 `ANALOG_WAVEFORM`（给名字）** → **② 无参构造事件对象** →
**③ `vForce(波形)` 把波形赋进去** → **④ 到这一步事件才有 `id`**（形状 `WAV_waveformName`）→
**⑤ 再设采样点间隔等其它参数**。

**为什么第 ③ 步必须在 `id` 之前**：原文说隐式 `id` 来自 **`the assigned ANALOG_WAVEFORM`**
（**被赋给的**那个），而示例里「赋值」这个动作就是 `vForce(rampUp)`——
**即：无参构造之后、`vForce()` 之前，这个事件的 `id` 还没定。**
（**这是本页的推断**：原文只说 `assigned`，**没有说赋值靠的是 `vForce()`**；
**两处的对应关系是本页从示例读出来的**。）

**本文档**没有**说的（语料未写）**：`sampleVectorDistance(64)` 的 `64` 是什么单位、
`averages()` / `clampChecks()` 怎么用、超量程检查怎么设、
**以及**测到的电流值从哪读**（本类的 14 个成员函数里**没有** `getValue()` 一类的名字）。

## 和谁有关

**父类（本页声明里直接写着）**：

- [[event-base]] — **`class EVENT_WAVEFORM_VFIM : public EVENT_BASE`**，
  原文正文也再说了一遍：`The class derives from the EVENT_BASE class.`
  **基类提供通用 event 接口（`id` / `getId` / `getEventType` / `toXml`），本类提供波形与测量的那部分。**
  **那页本页没读**（**本页关于基类的一切都只有这一篇里那两句转述**）。

**兄弟类（同一族里的另一个，**只差测什么**）**：

- [[event-waveform-vfvm]] — 原文并列的另一半：
  **`EVENT_WAVEFORM_VFVM (Voltage Force / Voltage Measure Waveform)`**。
  **两者都是 `Voltage Force`，区别只在 `Measure` 的是 `Current` 还是 `Voltage`。**
  **那页本页没读。**

**`Related information` 一节点名的六个（**原文只列名字，没有任何一句说明**）**：

| 原文名字 | 在 allowlist 里？ | 本页怎么处理 |
|---|---|---|
| `EVENT_BASE` | **在**（[[event-base]]） | 上面已链 |
| `EVENT_WAVEFORM_VFVM` | **在**（[[event-waveform-vfvm]]） | 上面已链 |
| `EVENT_WAVEFORM_VF` | **不在** | **只写反引号**；**示例里用的就是它** |
| `EVENT_WAVEFORM_IM` | **不在** | **只写反引号** |
| `EVENT_VALUE_INT` | **不在** | **只写反引号** |
| `ANALOG_WAVEFORM` | **不在** | **只写反引号**；**示例第一步用的就是它** |

> **原文对它的六个 `Related information` 一个字的说明都没给**——
> **所以「这六个和本类各是什么关系」本页不知道**，只知道它们被列在一起。
> **本页唯一敢说的**：`ANALOG_WAVEFORM` 出现在示例第一步，
> **所以「先有波形、再有事件」这个顺序是原文示例给的**（**推断**：
> 原文没有用一句话说过这个顺序）。

**被本页点名、本页没读的（均未建，不链）**：
**`EVENT_WAVEFORM_VFIM` 的 14 个成员函数子页**、
`EVENT_WAVEFORM_VF`、`EVENT_WAVEFORM_IM`、`EVENT_VALUE_INT`、`ANALOG_WAVEFORM`。
**前 14 篇是本页真正的「内容所在」**——**本页只有它们的名字。**

> **本页的「和谁有关」全部来自这一篇原文里点到的名字。本页没有从别处文档引任何东西。**

## 版本

本文档有 `## Functional changes` 段，**全部内容两条**：

- **`Introduced in SmarTest 6.5.2`**
- **`SmarTest 7.4.0: New member functions clampChecks() and getClampChecks().`**

> **两条用的都是 `in`，不是 `before`**——按 §11.2 ②，哨兵值的措辞一定是
> `Introduced before …`。**所以这两条都是**真版本记录**：**
> **本类 6.5.2 引入；`clampChecks()` 与 `getClampChecks()` 是 7.4.0 加的。**
>
> **可推出的结论**（**推断**，依据是「7.4.0 才加」+ 上面那张 14 个成员函数的表）：
> **钳位检查这一对函数在 7.4.0 之前不存在**，
> **但 `iClampChecks()` 与 `getIClampChecks()`（电流侧那一对）**不在**这条变更记录里**——
> **它们是不是同一批加的，本文档没说，本页不推断。**
>
> **对照页**：[[smartest-6.5.2]] / [[smartest-7.4.0]]（**均未建**）——
> **这两版的覆盖范围本页都没读。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38_EVENT_WAVEFORM_VFIM.md`
（raw 的 `source_topic: "116927.htm"`）。

**本页没做的**：

- **14 篇成员函数子页一篇都没读**：`vForce()` / `getVForce()` / `sampleVectorDistance()` /
  `getSampleVectorDistance()` / `getSamples()` / `averages()` / `getAverages()` /
  `clampChecks()` / `getClampChecks()` / `iClampChecks()` / `getIClampChecks()` /
  `outOfRangeCheck()` / `getOutOfRangeCheck()` / `getRepeatCount()`。
  **所以：这 14 个函数各自怎么用、参数是什么、单位是什么，本页一个字都没有。**
  **「是什么」里那张表的三条规律是本页从那 14 个**名字**推出来的，不是从它们的内容读出来的。**
- **`Related information` 六篇一篇都没读**：`EVENT_BASE` / `EVENT_VALUE_INT` /
  `EVENT_WAVEFORM_VF` / `EVENT_WAVEFORM_IM` / `EVENT_WAVEFORM_VFVM` / `ANALOG_WAVEFORM`。
  **⚠️ 注意 [[event-base]] 也在其中**——**本页对基类的描述只来自本篇里那两句转述，
  没有从基类那篇读过任何内容。**
- **`ANALOG_WAVEFORM` 没读**——**所以 `TM::RAMP` / `TM::POS` 之外还有哪些取值、
  `samples(4)` 是几个点、`.min(0.1).max(1.6)` 带不带单位，本页都没有。**
  示例第一步那四行**本页只做了逐字转述与字面直读，没有从它的定义文档取任何依据。**
- **`EVENT_WAVEFORM_VF` 没读**——**而示例第二步用的正是它**（见下 ⚠️ ①）。
  **所以「这段示例到底能不能用在 `VFIM` 上」本页答不了。**
- **本文档没有 `## Procedure`、没有 `Before you begin`、没有 `What to do next`。**
  所以「典型用法」一节的顺序**是本页从两段示例与构造函数的隐式 `id` 规则拼出来的，不是原文给的步骤**——
  本页在那一节已标出哪些是推断。
- **没有任何图。** 本篇没有图片引用。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 示例里用的类名不是本页的类。** `## Example` 第二段的说明是
> `Defines a force voltage ramp waveform:`，代码是
> `EVENT_WAVEFORM_VF rampUpEvent;` / `rampUpEvent.vForce(rampUp);` /
> `rampUpEvent.sampleVectorDistance(64);`——
> **声明的是 `EVENT_WAVEFORM_VF`，而本页讲的是 `EVENT_WAVEFORM_VFIM`。**
> **两个名字在本篇里都出现过**（`EVENT_WAVEFORM_VF` 在 `Related information` 里），
> **所以不是笔误就是这一段是从 `VF` 那篇搬过来的**——**原文没说，本页不判。**
> **本页照实引了这段，并在「典型用法」里标出这一点。**
>
> **② `Related information` 的六个链接**粘在一起**，中间没有任何分隔。** 逐字：
> `[EVENT_BASE](<02.07.04.01.63.01_EVENT_BASE.md>)[EVENT_VALUE_INT](<02.07.04.01.63.19_EVENT_VALUE_INT.md>)[EVENT_WAVEFORM_VF](<02.07.04.01.63.37_EVENT_WAVEFORM_VF.md>)[EVENT_WAVEFORM_IM](<02.07.04.01.63.33_EVENT_WAVEFORM_IM.md>)[EVENT_WAVEFORM_VFVM](<02.07.04.01.63.39_EVENT_WAVEFORM_VFVM.md>)[ANALOG_WAVEFORM](<02.07.04.01.05_ANALOG_WAVEFORM.md>)`
> ——**六个链接一个挨一个，没有空格、没有顿号、没有换行**。
> **本页在「和谁有关」里把它们拆成了表，那是本页的整理，不是原文的形状。**
>
> **③ `Parameter` 那张表丢了数据格。** 逐字：
> `Parameter` / ` | Parameter  | Description |` / ` | id |` /（空行）/
> `Identifier of the event.` /（空行）/ `The identifier may be defined as integer value or as string.` /（空行）/ ` |`
> ——**表头是 `Parameter` 与 `Description` 两列，但 `id` 那一行的 `Description` 格没进表**，
> **两句说明落在表外面。** 这与 [[xps256-status-flags]] 那 18 张表是同一类成因
> （HTML 表格转 markdown 时被拆散）。**本页正文把那两句照原样引了。**
>
> **④ `#### Subtopics` 出现在任何 `##` 之前，且层级是 H4。** 与 [[event-base]] 同一形状——
> **这两篇都是「文件从一个 H4 开始」**。**同一族里至少两篇这样，不是孤例。**
>
> **⑤ 本页的类声明代码块里，三个构造函数的缩进不一致。** 逐字：
> `EVENT_WAVEFORM_VFIM(const STRING & id);`（**4 个空格缩进，无对齐空格**），
> 而 `EVENT_WAVEFORM_VFIM(      INT      id);`（**`INT` 两侧各塞了 6 个空格**）——
> **与 [[event-base]] 里同样的对齐做法，也同样地没对齐好**（`STRING` 那行本来就不需要补空格）。
> **本页照引。**
>
> **⑥ 语法节的 `### Syntax` 下**只有类声明**，没有那 14 个成员函数的签名。**
> **原因是它们被拆成了独立的子页（在 `#### Subtopics` 里），不在本篇正文里**——
> **所以「本类有哪些函数」这件事，只看「语法 / 参数」节是看不全的**。
> **本页在「是什么」里补了那 14 个名字，但**签名一个都没有**。**

`verified: doc-only`
