---
type: object
title: HW_STATE
layer: L2
stage: pin
tags: [hw-state, l2-api, test-method-api, hardware-status, dps, ppmu, vi-source, xps256, kelvin, ganging, offline-mode]
related: [hw-pin-state, on-first-invocation-begin, on-first-invocation-end, for-each-site-begin, for-each-site-end, xps256-status-flags, dc-scale-xps256-card, site-focus-required-before-command, pin, test-method-class, flag]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117_HW_STATE.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# HW_STATE

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,847 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117_HW_STATE.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Query the status outside the ON_FIRST_INVOVATION block

The status is read from the hardware, stored in the HW_STATE object, and finally retrieved from the HW_STATE object for the site in focus outside of the `ON_FIRST_INVOCATION`（raw: `02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md`） block.

```
HW_STATE    hwState;
DOUBLE      forcedVoltage;
DOUBLE      clampCurrent;

ON_FIRST_INVOCATION_BEGIN();
{
    ...
    ...
}
ON_FIRST_INVOCATION_END();

hwState.getStatus ("PMU_pin_1, DPS_pin_1");

forcedVoltage = hwState.pin ("DPS_pin_1").getVoltageForce();
clampCurrent  = hwState.pin ("DPS_pin_1").getCurrentClampSource();

cout << "Current site: " << CURRENT_SITE_NUMBER() << ", pin \"DPS_pin_1\"" << endl;

cout << "\tForced voltage:       " << forcedVoltage << endl;
cout << "\tCurrent clamp source: " << clampCurrent  << endl;
```

### Example 2: Query the status in a FOR_EACH_SITE...WITH_QUERY block

The status is read from the hardware, stored in the HW_STATE object, and finally retrieved from the HW_STATE object for the site in focus within a FOR_EACH_SITE block in the `ON_FIRST_INVOCATION`（raw: `02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md`） block. The `FOR_EACH_SITE_BEGIN_WITH_QUERY`（raw: `02.07.04.01.71_FOR_EACH_SITE_BEGIN_WITH_QUERY.md`） API must be used to set the query focus within the FOR_EACH_SITE block.

```
HW_STATE    hwState;
DOUBLE      forcedVoltage;
DOUBLE      clampCurrent;

ON_FIRST_INVOCATION_BEGIN();
{
    ...
    ...

    FOR_EACH_SITE_BEGIN_WITH_QUERY();
    {
        hwState.getStatus ("PMU_pin_1, DPS_pin_1");

        forcedVoltage = hwState.pin ("PMU_pin_1").getVoltageForce();
        clampCurrent  = hwState.pin ("PMU_pin_1").getCurrentClampSource();

        cout << "Current site: " << CURRENT_SITE_NUMBER() << ", pin \"PMU_pin_1\"" << endl;

        cout << "\tForced voltage:       " << forcedVoltage << endl;
        cout << "\tCurrent clamp source: " << clampCurrent  << endl;
    }
    FOR_EACH_SITE_END();
}
ON_FIRST_INVOCATION_END();
```

<!-- 语法节 end -->

## 是什么

**`HW_STATE` 是「把硬件当前的设置读一份快照存下来」的那个 C++ 类。** 原文第一句：

> 「This class is used to query the correct hardware status in FW. Currently, it can be used for DPS, PPMU and VI-source.」

**两个要点**：① 它在 **FW** 里用；② **目前只覆盖 DPS、PPMU、VI-source 三类**。

**用法永远是两段式**（这一条贯穿本页）：

```
hwState.getStatus ("pin1, pin2");        ← ① 从硬件读一次，存进 HW_STATE 对象
hwState.pin ("pin1").getXxx();           ← ② 从对象里按 pin 取某一项设置
```

**它读的是「一次性快照」，不是实时值**——`pin()` 那一节的原文写死了：

> 「This function returns the hardware settings for the specified pin. These settings are the settings of the hardware at the time you call the getStatus() member function.」

**即：`getStatus()` 之后硬件又变了，对象里的值不会跟着变。**

### 类定义与头文件

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/HwState.h.」

构造函数只有一个：

```
HW_STATE();
```

> 「This constructor creates an object of HW_STATE class. It contains the hardware setting status. You can retrieve the settings with the member functions of HW_PIN_STATE.」

（`HW_PIN_STATE` 后面那个链接已按 §11.1 ② 剥成纯文本；那一篇是 [[hw-pin-state]]。）

### 八个成员函数，分两类

| 成员 | 签名（原文逐字） | 干什么 |
|---|---|---|
| `getStatus()` | `void getStatus(const STRING &pinlist);` | **读快照**：把指定 pin 的硬件状态读进对象 |
| `pin()` | `HW_PIN_STATE& pin(const STRING &pinName);` | **取一项**：返回某 pin 的 `HW_PIN_STATE` 引用 |
| `checkKelvinStatus()` | `bool checkKelvinStatus(...);` | **测 sense 连接**（site in focus） |
| `checkKelvinStatusParallel()` | `bool checkKelvinStatusParallel(...);` | **测 sense 连接**（所有 active site） |
| `checkGangConnection()` | `bool checkGangConnection (...);` | **测 ganging 连接**（**仅 XPS256**） |
| `checkGangConnectionParallel()` | `bool checkGangConnectionParallel (...);` | **测 ganging 连接**（**仅 XPS256**） |
| `readMaxAbsVdropsParallel` | `void readMaxAbsVdropsParallel(const STRING &pinlist, const Boolean reset);` | **读 latch 住的最大压降**（所有 active site，**仅 XPS256**） |
| `getMaxAbsVdrops` | `void getMaxAbsVdrops(const STRING &pin, DOUBLE maxAbsForceDrop, DOUBLE maxAbsReturnDrop);` | **取压降值**（site in focus，**仅 XPS256**） |

**前两个是一组（读快照然后取值），后六个是一组（测连接 / 读压降）。**
`getStatus()` 与 `pin()` 都**没有返回值**或只回一个子对象引用——
**真正的设置项全在 [[hw-pin-state]] 的 getter 里**（**那一篇本页没读**）。

### `getStatus()`：**硬件一变就得重读**

> 「This function queries the status of specified pins for the site in focus. You need to call this method every time the settings of the hardware are changed. The read data are stored in HW_STATE object.」

三件事：① 查的是 **site in focus**；② **硬件设置一变必须重新调一次**；③ 读到的数据存在对象里。

> **第 ② 句是本页最容易踩的坑**：`getStatus()` **不是「调一次用一辈子」**。
> 后端把 DPS 电压改了、或者换了一根 pin 的设置，**旧快照就是过期的**。

**调用位置有硬限制**：

> 「The member function must be called outside of the ON_FIRST_INVOCATION block or within a FOR_EACH_SITE...WITH_QUERY block.」

**只有两处可以调**：`ON_FIRST_INVOCATION` 块**外**，**或** `FOR_EACH_SITE...WITH_QUERY` 块**内**。
（相关页 [[on-first-invocation-begin]] / [[for-each-site-begin]]；**两篇本页都没读**。）

**取值的路径**：

> 「The data read from the hardware and stored in the HW_STATE object can be retrieved per pin and property by the pin() function followed by a member function of the subsidiary HW_PIN_STATE class.」

| | 原文 |
|---|---|
| `pinlist` 参数 | `A comma鈥憇eparated list of the pins to be queried.` |
| 出错 | `If the pinList is empty or an invalid pin is specified, an error message will be thrown out and the query will not be executed.` |
| 返回值 | `There is no return value.` |

### `pin()`：**空名或不在 `getStatus()` 的清单里 → 报错、不回值**

> 「If the pinName is empty or is not in the pinList of getStatus(), an error message will be thrown out and no setting will be returned.」

| | 原文 |
|---|---|
| `pinName` 参数 | `The pin that will be queried.` |
| 返回值 | `A reference to the subsidiary HW_PIN_STATE class.` |

**这一句是 `getStatus()` 与 `pin()` 的连接处**：
**`pin()` 不是独立查询——它只能取 `getStatus()` 已经读过的那批 pin。**
**没在 `pinlist` 里点过名的 pin，`pin()` 取不到。**

### 四个「测连接」的函数：**本页只给到名字与一句说明**

**两个 Kelvin**：

> 「This member function initiates a sense connection test for the site in focus on the defined pins.」

> 「This member function initiates a sense connection test for all active sites on the defined pins.」

**两个 Gang**：

> 「The function is supported only with the DC Scale XPS256 card.」

**四个函数的签名原文都写作 `...`**（`bool checkKelvinStatus(...);` 等），
**具体参数在它们各自的子页里**——原文对四个函数各给一句
`For the syntax and more information refer to …`，指向四个子页（**本页都没读**，见「出处」）。
**返回类型都是 `bool`。**

### 压降那一对：**先 `readMaxAbsVdropsParallel`，后 `getMaxAbsVdrops`**（顺序不能反）

`readMaxAbsVdropsParallel`：

> 「This member function reads the latched maximum absolute voltage drop values from the hardware. The values are read for the given list of pins for all active sites and are stored in the test method cache. As long as the test method is loaded, the stored values in the test method cache are valid and can be retrieved with the getMaxAbsVdrops function.」

> 「The reset parameter defines whether the latched values are then cleared.」

> 「The function should be called in the ON_FIRST_INVOCATION block and is supported only with the DC Scale XPS256 card card.」

`reset` 两档（原文）：`- true (default): Reset after readout.` / `- false: Do not reset after readout.`

`getMaxAbsVdrops`：

> 「This function queries the maximum absolute force and return voltage drop values for the defined pin on the site in focus.」

> 「The readMaxAbsVdropsParallel member function must be called upfront for reading the flags from the hardware into the test method cache.」

> 「The function should be called in a FOR_EACH_SITE...WITH_QUERY block or outside the ON_FIRST_INVOCATION block and is supported only with the DC Scale XPS256 card card.」

**分工与存放位置**：

| 步 | 函数 | 原文要求的调用位置 | 数据在哪 |
|---|---|---|---|
| 1 | `readMaxAbsVdropsParallel(pinlist, reset)` | **`ON_FIRST_INVOCATION` 块里**（`should be called in the ON_FIRST_INVOCATION block`） | **test method cache** |
| 2 | `getMaxAbsVdrops(pin, force, return)` | **`FOR_EACH_SITE...WITH_QUERY` 块里，或 `ON_FIRST_INVOCATION` 块外** | 从 cache 取，按 **site in focus** |

**两处要点**：

> **① 「必须先调 `readMaxAbsVdropsParallel`」是原文用 `must` 写的**
> （`must be called upfront`）——**不是建议**。
> **② 第 1 步的位置被限定在块「里」**（`in the ON_FIRST_INVOCATION block`），
> **和 `getStatus()` 那个「块外或 WITH_QUERY 块内」不是同一套**，**别照抄。**
>
> **③ 第 1 步的数据放在 `test method cache`，不是 `HW_STATE` 对象里**——
> 原文说它 `As long as the test method is loaded … are valid`，
> **即 cache 的生命期是「这个 test method 加载着的时候」。**

两格的单位（原文）：`The maximum absolute force voltage drop in volts (V) for the queried pin and the site in focus.` /
`The maximum absolute return voltage drop in volts (V) for the queried pin and the site in focus.`

### offline 模式：**不能总是给你对的设置**（这一条是警告，不是可选项）

> 「In offline mode, the API cannot always return the correct settings of the hardware. This is especially true when hardware settings depend on pattern鈥慴ased conditional jumps and match loops.」

> 「If SmarTest determines that the state of the hardware cannot be evaluated correctly, "WARNING: ... - reported last DC state ... may not reflect online state." is issued in the ui_report window.」

**两件事**：

1. **offline 下可能给不出对的设置**——**尤其**当设置依赖「pattern-based 的条件跳转与 match loop」时。
   （`pattern鈥慴ased` 是坏字，正字 `pattern-based`，见「出处」⚠️①。）
2. SmarTest **判断不出**当前状态时，会在 **`ui_report` 窗口**打一条
   `WARNING: …`——**原文给的是模板，中间那两处 `...` 是原文自己写的**（§11.1）。

> **所以「offline 下拿到了值」≠「值是对的」。**
> **要盯 `ui_report` 里有没有那条 `WARNING`**——它是这套 API 自己承认「我不确定」的唯一信号。

## 典型用法

**先说范围**：本篇**没有 `## Procedure`、没有 `## Before you begin`、也没有 `## Application`**。
它给的是**两个完整例子**（本页「语法 / 参数」节里逐字收了），**顺序本身就是用法**。

**1. 建对象**：`HW_STATE hwState;`

**2. 读快照**：`hwState.getStatus ("pin1, pin2");`
**位置二选一**：`ON_FIRST_INVOCATION` 块**外**，或 `FOR_EACH_SITE...WITH_QUERY` 块**内**。

**3. 按 pin 取某一项**：`hwState.pin ("pin1").getXxx()`——
`getXxx` 是 [[hw-pin-state]] 的成员函数。**pin 必须是第 2 步点过名的。**

**4. 硬件一变就回到第 2 步重读**（原文：`You need to call this method every time the settings of the hardware are changed.`）。

**5. 要读压降**（仅 XPS256）：先 `readMaxAbsVdropsParallel(pinlist, reset)`，
再 `getMaxAbsVdrops(pin, force, return)`——**顺序不能反**（原文 `must be called upfront`）。

### 两个例子的差别**全在「在哪读」**

| | Example 1 | Example 2 |
|---|---|---|
| 标题（原文逐字） | `Example 1: Query the status outside the ON_FIRST_INVOVATION block` | `Example 2: Query the status in a FOR_EACH_SITE...WITH_QUERY block` |
| `getStatus()` 调在哪 | **`ON_FIRST_INVOCATION` 块结束之后**（块外） | **`FOR_EACH_SITE_BEGIN_WITH_QUERY()` 里面** |
| 读的是哪个 site | **site in focus** | **site in focus**（WITH_QUERY 把查询焦点设进去） |
| 取哪根 pin | `"DPS_pin_1"` | `"PMU_pin_1"` |
| 取哪两项 | `getVoltageForce()` + `getCurrentClampSource()` | 同左 |

原文对 Example 2 的一句关键说明：

> 「The FOR_EACH_SITE_BEGIN_WITH_QUERY API must be used to set the query focus within the FOR_EACH_SITE block.」

> **注意是 `FOR_EACH_SITE_BEGIN_WITH_QUERY()`，不是普通的 `FOR_EACH_SITE_BEGIN()`**——
> **要设「查询焦点」就得用带 `_WITH_QUERY` 的那个**
> （`[[for-each-site-begin]]` 是普通那个的页；`FOR_EACH_SITE_BEGIN_WITH_QUERY`
> **不在 allowlist 里，故本页用反引号写**，§9.1）。

**两个例子里都有的这段**（逐字，两个例子各一遍）：

```
cout << "Current site: " << CURRENT_SITE_NUMBER() << ", pin \"DPS_pin_1\"" << endl;
```

**`CURRENT_SITE_NUMBER()` 在本篇 `sources:` 里没有任何定义**（**语料未写**），
例子只是用它把当前 site 号打出来。
**`getVoltageForce()` / `getCurrentClampSource()` 两个 getter 也不在本篇里定义**——
它们在 [[hw-pin-state]] 里（**那一篇本页没读**）。

## 和谁有关

**先给一句总的关系**：`HW_STATE` 是**父**、[[hw-pin-state]] 是**子**——
**这两页是一对，不能分开读**：本页负责「读一次」，子页负责「读什么」。

- [[hw-pin-state]] — **子容器 / 下游**，这条关系是**原文自己写死的**：
  `This class is a subsidiary data container of the HW_STATE class.`
  取值的动作永远两步：`HW_STATE.getStatus()` 读快照 → `HW_STATE.pin()` 拿子对象 →
  **子对象的某个 getter 取一项**。
  **那一篇本页没读**，所以**「一共能取哪些设置项」本页一个字都没有**。
  另：**子页的 `## Example` 一节没有自己的例子**，它直接指向本页这两个例子
  （原句：`For an example, refer to Example 1: … and Example 2: … in HW_STATE.`）
  ——**这也是本页两个例子同时属于子页的原因。**
- [[on-first-invocation-begin]] / [[on-first-invocation-end]] — **调用位置的硬限制**
  （`getStatus()` 与 `getMaxAbsVdrops()` 都点了这个块；`readMaxAbsVdropsParallel` 要求**在块里**）。
  **两篇本页都没读。**
- [[for-each-site-begin]] / [[for-each-site-end]] — **另一处允许的调用位置**
  （`FOR_EACH_SITE...WITH_QUERY`）。**两篇本页都没读。**
  **注意**：本篇写的名字是 `FOR_EACH_SITE_BEGIN_WITH_QUERY`，
  它和 `[[for-each-site-begin]]` 是不是同一个 API，**本篇没说**（**语料未写**）。
- [[xps256-status-flags]] — **下游**。`readMaxAbsVdropsParallel` 的说明里写着
  `for reading the flags from the hardware into the test method cache`——
  **它读进来的就是「flag」**。
  **那一篇本页没读**，所以**「这些压降 flag 与 XPS256 的 Voltage drop force / return warning
  是不是同一批」本页不判**。
- [[dc-scale-xps256-card]] — **四个函数的卡级前提**：`checkGangConnection()`、
  `checkGangConnectionParallel()`、`readMaxAbsVdropsParallel()`、`getMaxAbsVdrops()`
  都写着 `supported only with the DC Scale XPS256 card`。
  **那一篇本页没读**，所以**「为什么只能用在 XPS256 上」本页没有。**
- [[site-focus-required-before-command]] — **同族的约束**（「用站点焦点的命令要先设焦点」）。
  **这一条是本页加的（推断）**：本篇只说 `for the site in focus`，
  **没有一句提「要先设焦点」**。
- [[pin]] — **`pinlist` / `pinName` 全篇的主角**，也是 frontmatter `stage: pin` 的依据。
- [[test-method-class]] — **本页是 Test Method API（`layer: L2`）里的一员**：
  用法（在 C++ 测试方法里调、有头文件、有构造函数）与它同类。**那一篇本页没读。**
- [[flag]] — `readMaxAbsVdropsParallel` 那句 `reading the flags from the hardware` 里的 flag。
- `CURRENT_SITE_NUMBER()` / `FOR_EACH_SITE_BEGIN_WITH_QUERY` — **两个都在例子里出现、
  本页不链**（**不在 allowlist 里**，§9.1）。

**本页没有引用 `edges.jsonl` 的入边 / 出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，段里有五条**：

| 版本 | 内容（原文逐字） |
|---|---|
| — | `Introduced in SmarTest 6.5.0` |
| **SmarTest 7.4.0** | `New member function HW_STATE.checkKelvinStatus()` |
| **SmarTest 7.4.2** | `New member function checkKelvinStatusParallel()` |
| **SmarTest 7.10.1** | `New member function checkGangConnection(), checkGangConnectionParallel(), getMaxAbsVdrops(), readMaxAbsVdropsParallel()` |
| **SmarTest 7.10.3** | `New syntax for member functions checkKelvinStatus(), checkKelvinStatusParallel(), checkGangConnection() and checkGangConnectionParallel() introduces parameter for defining the maximum resistance.` |

**三条读法**：

- **第一条不是哨兵值**。它写的是 `Introduced in SmarTest 6.5.0`，**不是 `before`**——
  **所以这一条就是「6.5.0 引入了 HW_STATE」**，与 §11.2 ② 那种 `before` 的写法不同。
  → [[smartest-6.5.0]]
- **`getStatus()` 与 `pin()` 没有任何版本条目提到**。
  **（推断）**：它们在 6.5.0 就有——
  依据是第一条说的是「这个类」被引入，而类一开始就得有读快照的手段。
  **原文没有逐函数写，所以这是推断，不是文档事实。**
- **最后一条落在 7.10.3，也就是本 wiki 面向的版本**：
  它给四个「测连接」函数**加了「定义最大电阻」的参数**
  （`New syntax for member functions … introduces parameter for defining the maximum resistance.`）。
  **所以这四个函数在 7.10.3 之前的签名和现在不一样**；
  **到底差在哪一篇里没有**（**语料未写**）——要去那四个子页看。

## 出处

`sources:` 一篇：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117_HW_STATE.md`
  （frontmatter 的 `source_topic` 是 `105633.htm`；**10,758 字节 / 245 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。
  **要留意它只抽到了 `## Examples` 下面那两节**（`### Example 1` / `### Example 2`）——
  **本篇的类定义与八个成员函数都不在段标记里**，所以它们由本页正文补述（§4 的分工：
  段标记能抽的由脚本抽，抽不到的不许猜，**由 LLM 从读过的原文里写**）。
- 本篇的 `## Subtopics` 一节列了**五个子主题**（本页都记在「没读」里）。

**本页没做的**：

- **五个子页一篇都没读**：
  `HW_PIN_STATE`（有页 [[hw-pin-state]]）、`HW_STATE.checkKelvinStatus()`、
  `HW_STATE.checkKelvinStatusParallel()`、`HW_STATE.checkGangConnection()`、
  `HW_STATE.checkGangConnectionParallel()`。
  **所以那四个「测连接」函数要传什么参数、返回的 `bool` 是什么意思、
  7.10.3 新加的「最大电阻」怎么给——本页一个字都没有**
  （原文对这四个函数各只有一句 `For the syntax and more information refer to …`）。
- **`## Related information` 的两条都没读**。原文这一节**只有两条**，
  而且**在 md 里粘成了一行、中间没有分隔符**：
  `HW_PIN_STATE` 与 `HW_STATE.checkKelvinStatus()`（见下面 ⚠️④）。
- **`HW_PIN_STATE` 的成员函数清单本页没读**——
  所以**「一共能取哪些设置项」本页答不了**，去 [[hw-pin-state]]。
- **`ON_FIRST_INVOCATION` / `FOR_EACH_SITE` 那几篇没读**，
  所以**「块内 / 块外」到底怎么界定、`_WITH_QUERY` 与普通版的区别，本页没有。**
- **`DC Scale XPS256 card` 那一篇没读**，**所以「为什么这四个函数只能用在 XPS256 上」本页没有。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**；上游 `105633.htm` 里也 **0 个 `<img>`、0 个图片路径**
  （`src=` 只有 1 处，是那个 `p.css` 样式表）。
  **所以本页没有任何来自图的结论**——**「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上编过、也没跑过 `HW_STATE`**（`verified: doc-only`）。
  **所以「offline 下那条 WARNING 实际多久出现一次」「`getStatus()` 一次读多慢」本页答不了（§11）。**
- **§10 重复投放：本篇在语料里只有一份**（按文件名全树 glob，1 命中）。

### 上游 `.htm` 核对（本页做的一步）

**下面四条去上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\105633.htm`（22,419 字节）核过。
结论：两处坏字是「转换坏的（可救）」，两处是「上游本来就这样（救不回来）」——
分得开，所以下面逐条写明是哪一种。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 坏字：`pattern鈥慴ased`，正字是 `pattern-based`。**
> 原文逐字（**坏字照引**）：
> `This is especially true when hardware settings depend on pattern鈥慴ased conditional jumps and match loops.`
> **上游核对**：`105633.htm` 里写的是 `pattern‑based`——那个字符是 **U+2011（非断行连字符）**，
> **上游是好的**。`鈥` 是 U+2011 的 UTF-8 头两个字节被按 GBK 读的结果，
> **紧跟的 `b` 被并进了第二个坏字**（所以是 `鈥慴` 而不是 `鈥慴ased` 拆成两截——
> 想还原得把 `鈥慴` 整体换成一个短横，只换 `鈥` 会得到残词 `慴ased`）。
> **定性**：**HTML→md 转换坏的（§11.2 ①那一族），上游干净、重做一次转换能救**。
> **但本页照原样引，一处不改**（§11.2 ①：拿修好的字回 raw 里搜是搜不到的）。
>
> **② 同类坏字：`comma鈥憇eparated`，正字是 `comma-separated`（本篇出现 2 次）。**
> 原文逐字（**坏字照引**）：`A comma鈥憇eparated list of the pins to be queried.`
> **上游核对**：`105633.htm` 里是 `comma‑separated`（同样是 U+2011，**上游干净**）
> → **同属转换坏的那一族，可救，本页照原样引。**
> **这一句在本篇里出现两次**（`getStatus()` 与 `readMaxAbsVdropsParallel` 各一次），
> **两次的坏法完全一样**（把那本页正文两处引用与这一处对齐即可）。
>
> **③ 上游就坏的两处（救不回来）：**
>
> - **`ON_FIRST_INVOVATION` 少一个 `C`。** 原文逐字（`### Example 1` 的标题）：
>   `Example 1: Query the status outside the ON_FIRST_INVOVATION block`
>   **上游核对**：`105633.htm` 里 `INVOVATION` 出现 **1 次**、`INVOCATION` 出现 **10 次**
>   → **上游就坏的**（§11.2 ⑥）。
>   **本页的「语法 / 参数」节照抄了这个标题（那一节不许动），本页正文也照抄。**
> - **`supported only with the DC Scale XPS256 card card.` 多一个 `card`。**
>   原文逐字：
>   `The function should be called in the ON_FIRST_INVOCATION block and is supported only with the DC Scale XPS256 card card.`
>   （`readMaxAbsVdropsParallel` 与 `getMaxAbsVdrops` 两处都是 `card card`。）
>   **上游核对**：`105633.htm` 里就是 `DC Scale XPS256 card card.`
>   → **上游就坏的**（英文里这是重复词）。
>   **本页正文引这两句时照原样留着。**
>
> **④ `## Related information` 的两条在 md 里粘成一行——这一处是转换压平的，不是上游错。**
> md 里两个链接直接相接（`](<…>)[`，中间没有分隔符）。
> **上游核对**：`105633.htm` 里它们是**两个独立的 `<div>`**，各自带 `title` 属性
> → **转换压平的**。
>
> **⑤ 坏字合计：本篇 6 个汉字**（`鈥`×3、`慴`×1、`憇`×2），**全部集中在上面①②两处词组里**。
> 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **除这两处外，本篇没有别的汉字**——
> **但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
