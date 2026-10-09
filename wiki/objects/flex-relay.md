---
type: object
title: FLEX_RELAY
layer: L2
stage: pin
tags: [testmethod, api, flex-relay, relay, utility-line, utility-purpose, multi-site, task-list, data-container]
related: [pin, pin-group-editor, pin-configuration-tool, utility-pins-editor, utility-purpose-editor, utility-line-view, utility-lines, task-list, flush, on-first-invocation-begin, on-first-invocation-end, for-each-site-begin, for-each-site-end, controlling-multiple-sites, sequencer-controlled-utility-lines, set-utility-lines, get-utility-lines, spmu-pin-task, spmu-pin-task-mode, digital-pins-editor, dps-pins-editor, pin-utility, smartest-6.3.2, smartest-6.5.2, smartest-7.10.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68_FLEX_RELAY.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# FLEX_RELAY

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,406 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68_FLEX_RELAY.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Single site testing

```
//
// Construct TASK_LIST class object "tasklist1"
// and FLEX_RELAY class object "frelay".
//
TASK_LIST tasklist1;
FLEX_RELAY frelay;

//
// Set "PIN1" to Hi-Z by setting the AC, DC, PPMU relays to off.
//
frelay.pin("PIN1").set("IDLE","X");

// Use utility purposes "group1" and "group2":
//
// - "group1" definition: 16501:ON, 16502:ON, 16503:OFF.
// - "group2" definition: 16503:ON, 16504:OFF, 16505:ON.
//
// "16503" is included in both the groups. The setting of
// "16503" in "group1" is overwritten by the setting in "group2".
// Thus, "16503" is set to ON by the following statement.
//
frelay.util_purpose("group1,group2").set();

//
// Modify the previous utility line settings:
//
// Change 16501 to OFF.
// Change 16504 and 16506 to ON.
//
frelay.util("UTL101").off();
frelay.util("UTL104, UTL106").on();

//
// Add "frelay" of FLEX_RELAY to the task list.
//
tasklist1.add(frelay);

//
// Execute the tasklist1, that is, "frelay" task.
//
tasklist1.execute();
```

In the last statement, `frelay.execute()` is called from the `TASK_LIST`（raw: `02.07.04.01.240_TASK_LIST.md`） class object tasklist1 internally, and the task frelay is executed. All the relay settings are download to the hardware after checking whether the settings are validated or not. If an error is found, this statement does nothing except displaying the error message.

You can also execute the frelay task by executing the `frelay.execute()` statement.

### Multi-site testing

```
STRING utilgrp = "UTL1, UTL2, UTL3, UTL4, UTL5";

//
// "UTL1" to "UTL5" are the following utility lines
//
// For Site1: 16501, 16502, 16503, 16504, 16505
// For Site2: 16506, 16507, 16508, 16509, 16510
//
STRING setting_1 = "1,1,1,0,0";
STRING setting_2 = "0,1,1,0,1";

FLEX_RELAY frelay;

ON_FIRST_INVOCATION_BEGIN();

    //
    // common setting in all sites;
    //
    frelay.pin("PIN1").set("IDLE");

    //
    // site-specific settings
    //
    FOR_EACH_SITE_BEGIN();

        INT site = CURRENT_SITE_NUMBER();

        if(site == 1)
        {
            frelay.util(utilgrp).set(setting_1);
        }
        else if(site == 2)
        {
            frelay.util(utilgrp).set(setting_2);
        }

    FOR_EACH_SITE_END();

    //
    // Download the relay settings to the hardware
    //
    frelay.execute();

    //
    // Execute a test here
    //
    ...
    ...

ON_FIRST_INVOCATION_END();
```

<!-- 语法节 end -->

## 是什么

**`FLEX_RELAY` 是 L2 的一个「任务容器」：你把继电器的设置往里面塞，执行时一次性下载到硬件。**
原文两句逐字：

> 「The FLEX_RELAY class is a data container holding the contents of the task for setting up relay
> connections. You can control the relays for the digital channel pins and the user relays that are
> controlled by the utility lines.」

**两个词要抓住：**

- **`data container`** ——**它先是「装设置的地方」，不是一个动作**。
  **不调 `execute()`，里面填的东西不会下去**（见下「执行那一侧」）。
- **两类继电器**：**数字 channel 的继电器** 与 **utility line 驱动的用户继电器**。

### 四条特性（原文自己列的）

原文 `This API has the following features.` 加四条 bullet：

| # | 原文（要点） | 意思 |
|---|---|---|
| 1 | `Controls various types of relays with unified programming interface:` | **统一的编程接口**（下面挂了两条子 bullet） |
| 1a | `Relays in digital channels (relays on channel boards and clock boards).` | **channel board 与 clock board 上的继电器**；原文给的例子是 `you can set digital pins to Hi-Z by disconnecting the relays` |
| 1b | `User relays (controlled by the utility lines).` | **用户继电器** |
| 2 | `Supports multi-site testing` | **支持多 site** |
| 3 | `Enables you to activate utility line settings by executing the task. You can activate them without using the FLUSH API, which activates various parameters specified with other APIs at a time.` | **执行这个 task 就生效，不需要 [[flush]]** |
| 4 | （见下，与 `Routing.util()` 并存的那一条） | **与旧路并存** |

**第 3 条是它最要紧的一句**：**它是「不经过 [[flush]]」的一条路**——
**所以 `FLEX_RELAY` 与 `FLUSH` 是两条并行的「让设置生效」的机制**（见「和谁有关」）。

### 第 4 条：与 `Routing.util()` / `Routing.util_purpose()` 并存

原文逐字（**这是全文最长的一条 bullet**）：

> 「In a test method program, you can use both of the FLEX_RELAY API and the
> Routing.util()/Routing.util_purpose() API whose settings are activated by the FLUSH API. However,
> controlling the utility lines by using either one in each test method program would be a good
> practice: for example, control the utility lines with FLEX_RELAY in digital/DC tests, and control
> them with Routing.util()/Routing.util_purpose() in mixed signal tests where the routing sets and
> analog module relay settings and so on are activated by the FLUSH API.」

**即：两个都能用，但原文给了一条「建议」**（`would be a good practice`）：
**一个 test method program 里只用其中一条**——

| 场景 | 原文建议用 |
|---|---|
| digital / DC 测试 | **`FLEX_RELAY`** |
| mixed signal 测试（那一侧本来就要 FLUSH 来激活 routing set 与模拟模块继电器） | **`Routing.util()` / `Routing.util_purpose()`** |

**⚠️ 这一条是原文里唯一的「建议」性语句**（不是硬规矩：前半句明说 `you can use both`）。

### 四个子容器

原文逐字：`This class has four subsidiary data containers, which are for digital pins, utility
lines, and utility purposes, respectively.` ——**四个，各有一篇 `Subtopics`：**

| 子容器 | 原文（它装什么） | 由哪个成员函数拿到 |
|---|---|---|
| `FLEX_PIN_RELAY` | `Holds the relay settings for the specified digital channels.` | `pin()` |
| `FLEX_UTILITY_RELAY` | `Holds the utility line (user relay) settings specified with the utility line names.` | `util()` |
| `FLEX_UTILITY_PURPOSE_RELAY` | `Holds the utility line (user relay) settings specified with the utility purposes.` | `util_purpose()` |
| `FLEX_UTILITY_CHANNEL_RES` | `Holds the settings of utility line channel resources.` | `util_channelRes()` |

**后三个装的是同一类东西（utility line / 用户继电器），差别只在「用什么去指它」**：
**line 名 / purpose 名 / channel resource 名。**

原文接着逐字说明它们的归属：

> 「These four class objects are stored in the FLEX_RELAY class object. When the task is executed,
> the settings defined with these four subsidiary containers are downloaded to the hardware.」

**这两句合起来就是整个机制**：**设置先存进四个子容器（在内存里），`execute()` 时才下去。**

### `execute()`：校验、下载、等待

原文 `execute()` 一节逐字：

> 「This member function executes the task defined with FLEX_RELAY.」

> 「This member function checks whether the settings in the task are validated or not. If any error
> message is generated, this member function performs no action, that is, any setting is not
> downloaded to the hardware.」

**⚠️「全有或全无」**：**有一条错，整个 task 一个设置都不下载**
（`performs no action` / `any setting is not downloaded`）。

**执行顺序**原文给了三条 bullet，逐字：

> 「- Download the settings of relays related to digital pins to the hardware if defined.
> - Download the settings of utility lines specified with util_purpose()/util() to the hardware if defined.
> - Wait for the specified time.」

| 步 | 做什么 | 注意 |
|---|---|---|
| 1 | 下载**数字 pin** 的继电器设置 | `if defined` ——**没定义就跳过** |
| 2 | 下载 `util_purpose()` / `util()` 指定的 utility line 设置 | 同上；**注意 `util_channelRes()` 不在这一步里**（见 `## 出处` ⑤） |
| 3 | **等 `wait()` 指定的时间** | **即 `wait()` 是在下载之后生效** |

### 六个成员函数

原文 `Class definition` 一节列了六个（**同一文件内的锚点链接**），
`## Member functions` 一节逐个展开。**本页按原文转述**
（**这些签名与参数表都没进「语法 / 参数」节**，见 `## 出处`）：

| # | 函数 | 签名（原文） | 返回 |
|---|---|---|---|
| 1 | `pin()` | `FLEX_PIN_RELAY& pin(const STRING& pinlist);` | 引用，指向 `FLEX_PIN_RELAY` 对象 |
| 2 | `util()` | `FLEX_UTILITY_RELAY& util(const STRING& utilitylist);` | 引用，指向 `FLEX_UTILITY_RELAY` 对象 |
| 3 | `util_channelRes()` | `FLEX_UTILITY_CHANNEL_RES& util_channelRes (const STRING& channellist);` | 引用，指向 `FLEX_UTILITY_CHANNEL_RES` 对象 |
| 4 | `util_purpose()` | `FLEX_UTILITY_PURPOSE_RELAY& util_purpose(const STRING&utility_purposes);` | 引用，指向 `FLEX_UTILITY_PURPOSE_RELAY` 对象 |
| 5 | `wait()` | `void wait (const DOUBLE& time);` | 无 |
| 6 | `execute()` | `void execute();` | 无 |

**前四个是同一种形状：给一串名字，拿回一个子容器的引用，再在那个子容器上做设置**
（原文的 `Using the class` 一节把它写成一个模板，见「典型用法」）。
**后两个是动作：`wait()` 与 `execute()`。**

**构造函数**原文逐字：

> 「  Constructor」

```
FLEX_RELAY();
```

> 「This constructor creates an object of the FLEX_RELAY class.」

**（对照 [[pin-utility]]：那一篇明写「没有公开构造函数、必须用系统准备好的对象」；
本页明写有一个无参构造函数。）**

**头文件路径**（原文逐字）：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/FlexRelay.h.」
> ——**注意 `hp93000` 是四个 0**（**同日读的 [[pin-utility]] 那篇写的是同一个目录、
> 同一个写法**；**这一条引自另一篇 raw，不是本篇**）。

### 四个「取子容器」函数的参数，逐个说清

| 函数 | 参数名 | 原文对它的说明 |
|---|---|---|
| `pin()` | `pinlist` | `A target pin name or pin group name of the digital channel pins. You can specify multiple pins and pin groups by separating with a comma.` + **`"@" specifies all the defined digital channel pins, including the digital pins that are used as the trigger source of the analog modules.`** + **`All pins must be configured as i, o, io, or dc pin in the Pin Configuration window.`** |
| `util()` | `utilitylist` | `A utility line name or a list of utility line names separated with a comma. You can use the name defined in the Utility Pins editor.` |
| `util_channelRes()` | `channellist` | `A utility line channel resource or a list of utility line channel resources separated with commas. It can be "@", that means all the utility line resources.` |
| `util_purpose()` | `utility_purposes` | `A utility purpose name or a list of utility purpose names separated with a comma. You can use the names defined in the Utility Purpose Editor.` |

**四条共有的两点：**
**① 都是「一个名字或一串逗号分隔的名字」；② 其中两条支持 `"@"` 通配**
（`pin()` 的是「所有已定义的数字 channel pin」，`util_channelRes()` 的是「所有 utility line 资源」）。
**⚠️ `util()` 与 `util_purpose()` 的说明里都没有 `"@"`**——**能不能用通配，那两条原文没说。**

**`pin()` 那条第三句是一条硬约束**：`All pins must be configured as i, o, io, or dc pin in the
Pin Configuration window.` ——**四个类型（`i` / `o` / `io` / `dc`）**，
**这与 [[digital-pins-editor]] 那类编辑器里的 `Type` 列是同族的东西**（**本页只到这一句**）。

### `wait()`：单位是秒

原文逐字：

> 「This member function defines a wait time after controlling all relays in the task when the task
> is executed.」

参数说明逐字：

> 「Wait time for the task in seconds (s).」

> 「Specify a positive value or zero.」

**三件事：**
- **时机是「控制完 task 里所有继电器之后」**（与 `execute()` 第 3 步一致）。
- **单位是 `seconds (s)`** ——**注意不是毫秒**。
- **取值只能是「正数或零」**——**负值会怎样，原文没说。**

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段**，
**用法靠 `## Class definition` 的 `Using the class` 模板 + `## Examples` 的两段代码**。

### 四条「先取子容器、再做设置」的模板（原文 `Using the class` 逐字）

原文把四个函数写成同一个形状——**`object.xxx("名字").member_func;`**：

| 要设置的 | 原文模板 | `member_func` 是谁的 |
|---|---|---|
| 数字 channel 的继电器 | `object.pin("pinlist").member_func;` | `FLEX_PIN_RELAY` 类 |
| utility line（按 **line 名**） | `object.util("utilitylist").member_func;` | `FLEX_UTILITY_RELAY` 类 |
| utility line（按 **purpose 名**） | `object.util_purpose("uti_purposelist").member_func;` | `FLEX_UTILITY_PURPOSE_RELAY` 类 |
| utility line（按 **channel resource**） | `object.util_channelRes("channel_list").member_func;` | `FLEX_UTILITY_CHANNEL_RES` 类 |

**另两条**：`object.wait(time);`（设等待时间）与 `object.execute();`（执行 task）。

**建对象**原文逐字：`FLEX_RELAY object;`。

### 单 site：一整条链（原文 `### Single site testing`）

| 步 | 代码（原文逐字，注释保留） | 在做什么 |
|---|---|---|
| 1 | `TASK_LIST tasklist1;` `FLEX_RELAY frelay;` | **建两个对象**：一个 task list、一个 flex relay |
| 2 | `frelay.pin("PIN1").set("IDLE","X");` | 注释逐字：`Set "PIN1" to Hi-Z by setting the AC, DC, PPMU relays to off.` ——**把一根针设成 Hi-Z** |
| 3 | `frelay.util_purpose("group1,group2").set();` | **按 purpose 名设 utility line**（**重叠语义见下**） |
| 4 | `frelay.util("UTL101").off();` / `frelay.util("UTL104, UTL106").on();` | **按 line 名改上一步的结果** |
| 5 | `tasklist1.add(frelay);` | **把这个 task 挂进 [[task-list]]** |
| 6 | `tasklist1.execute();` | 执行 |

**第 3 步那段注释是本页最有用的一段语义**，逐字：

> 「// - "group1" definition: 16501:ON, 16502:ON, 16503:OFF.
> // - "group2" definition: 16503:ON, 16504:OFF, 16505:ON.
> //
> // "16503" is included in both the groups. The setting of
> // "16503" in "group1" is overwritten by the setting in "group2".
> // Thus, "16503" is set to ON by the following statement.」

**行首那两个斜杠是原文代码块里的注释符**——本页上一版把它们去掉了，
那样写出来的东西**不是原文的子串**，却仍写着「逐字」。**现在照原文连注释符一起抄。**
（**这篇的 `## Example` 是 `// …` 注释与 C++ 代码混排的**，注释符是它的一部分。）

**即：同一个 line 被两个 purpose 都圈进去时，后面那个 purpose 的设置覆盖前面那个**
——**这正好是 [[utility-purpose-editor]] 那篇 `Note` 说的 `by overlapping`
在实际执行时的行为**（**那篇只说「可以重叠」，没有说重叠时谁赢；谁赢在本篇的注释里**）。

**第 6 步的语义**原文紧接着逐字解释：

> 「In the last statement, `frelay.execute()` is called from the `TASK_LIST` class object tasklist1
> internally, and the task frelay is executed. All the relay settings are download to the hardware
> after checking whether the settings are validated or not. If an error is found, this statement
> does nothing except displaying the error message.」

> 「You can also execute the frelay task by executing the `frelay.execute()` statement.」

**两条路**：**挂进 [[task-list]] 让 task list 执行，或者自己调 `frelay.execute()`。**

### 多 site：`ON_FIRST_INVOCATION_BEGIN` + `FOR_EACH_SITE_BEGIN`（原文 `### Multi-site testing`）

| 步 | 代码（原文逐字） | 在做什么 |
|---|---|---|
| 1 | `STRING utilgrp = "UTL1, UTL2, UTL3, UTL4, UTL5";` | **一组 utility line 名**（注释说明 `UTL1`–`UTL5` 在两个 site 上各对应哪五条 line：Site1 是 `16501`–`16505`、Site2 是 `16506`–`16510`） |
| 2 | `STRING setting_1 = "1,1,1,0,0";` `STRING setting_2 = "0,1,1,0,1";` | **两串按位置对应那五条 line 的设置值** |
| 3 | `ON_FIRST_INVOCATION_BEGIN();` | 进「只跑一次」的段（[[on-first-invocation-begin]]） |
| 4 | `frelay.pin("PIN1").set("IDLE");` | **所有 site 共用的设置**（注释逐字：`common setting in all sites;`） |
| 5 | `FOR_EACH_SITE_BEGIN();` … `INT site = CURRENT_SITE_NUMBER();` … `if(site == 1) { frelay.util(utilgrp).set(setting_1); } else if(site == 2) { … set(setting_2); }` … `FOR_EACH_SITE_END();` | **按 site 分别设值**（[[for-each-site-begin]]） |
| 6 | `frelay.execute();` | **把设置下载到硬件**（注释逐字：`Download the relay settings to the hardware`） |
| 7 | `...` `...` | 原文在这儿放了两行省略号表示「在这里跑测试」 |
| 8 | `ON_FIRST_INVOCATION_END();` | 出段 |

**多 site 的要点**：**`execute()` 在 site 循环之外**——
**设置是逐 site 攒的，下载只做一次**。
**这与单 site 那段里「先设后 execute」是同一条规则的两种写法。**

**从原文能落成的动作：**

| 要做的 | 依据 |
|---|---|
| 把数字针设成 Hi-Z | `frelay.pin("PIN1").set("IDLE","X");`（**注释说这等于把 AC / DC / PPMU 继电器都关掉**） |
| 对一批针 / pin group 设 | `pin()` 的 `pinlist` 支持逗号分隔的多个名字，**也支持 `"@"`** |
| 按 line 名设用户继电器 | `frelay.util("UTL104, UTL106").on();` / `.off()` |
| 按 purpose 名设 | `frelay.util_purpose("group1,group2").set();` |
| 按 channel resource 设 | `util_channelRes("channel_list")`（**这条只在模板里出现，两个例子都没用它**） |
| 让继电器动作后等一会儿 | `object.wait(time);` ——**单位秒、只能正数或零** |
| 让设置生效 | **`execute()`，或把 task 挂进 [[task-list]] 再执行它** |
| 一条错都不许有 | `execute()` 是「全有或全无」 |
| 不想用 [[flush]] | **用这条**（原文特性第 3 条） |

**⚠️ 两处例子与原文都没解释的写法差别**（见 `## 出处` ③）：
**① `set()` 在单 site 例子里给了两个参数（`set("IDLE","X")`），在多 site 里只给了一个（`set("IDLE")`）。**
**② `set()` 在 `util_purpose(...)` 后面是无参的（`.set()`），在 `util(...)` 后面带一串值（`.set(setting_1)`）。**
**`set()` 是子容器的成员函数**（在 `FLEX_PIN_RELAY` / `FLEX_UTILITY_RELAY` 那几篇里），
**本页没读那四篇**——**所以这两种调用形态各是什么意思，本页没有依据。**

## 和谁有关

- [[flush]] — **原文主动对照的那一个 API**：`You can activate them without using the FLUSH API,
  which activates various parameters specified with other APIs at a time.`
  **即 `FLEX_RELAY` 是「不经过 FLUSH」的另一条让 utility line 设置生效的路。**
  **本页只有这一句；FLUSH 自己怎么激活、激活哪些，在那页。**
- [[task-list]] — **两条执行路之一，也是原文的例子用的那条**：
  `tasklist1.add(frelay);` 然后 `tasklist1.execute();`。
  **原文说 `tasklist1.execute()` 会在内部调 `frelay.execute()`。**
  **task list 的其余规矩在那页。**
- [[utility-pins-editor]] — **`util()` 那一格的参数出处，原文直接点名**：
  `You can use the name defined in the Utility Pins editor.`
  **所以 line 名先要在那个编辑器里定义出来，本页才能用它们。**
- [[utility-purpose-editor]] — **`util_purpose()` 那一格的参数出处，原文直接点名**：
  `You can use the names defined in the Utility Purpose Editor.`
  **而且两页有一条对得上的语义**：那篇的 `Note` 说 `You can define the same utility line for
  different utility purposes by overlapping.`，**而本页的单 site 例子把「重叠时谁覆盖谁」
  用注释写清了**（后面的 purpose 赢）。**两篇 raw 互相都没有引用对方**
  （**那篇没有提 `FLEX_RELAY`，本篇没有提 `Utility Purpose Editor` 的 `Note`**）——
  **这条呼应关系是本页并读两篇 raw 得出的，不是任何一篇写的。**
- [[pin]] / [[pin-group-editor]] / [[pin-configuration-tool]] — **`pin()` 那一格的三个外部依赖**：
  参数是 `A target pin name or pin group name`，硬约束是
  `All pins must be configured as i, o, io, or dc pin in the Pin Configuration window.`。
  **三个对象的规矩在那三页，本页只有这一句。**
- [[utility-line-view]] / [[utility-lines]] / [[utility-line-assignments]] —
  **（推断）utility line 的「对象侧」**：本页的 `util()` 按 line 名设值，
  那三页从名字看是 line 的视图 / 清单 / 分配。**本篇 raw 一个都没提，
  所以这三条关系本页没有依据。**
- [[set-utility-lines]] / [[get-utility-lines]] / [[sequencer-controlled-utility-lines]] —
  **（推断）utility line 的另几条控制路径**。本页是 L2 的 test method API；
  那三页从页名看与「设置 / 读取 / 由 sequencer 控制 utility line」有关。
  **同样是按名字相邻列出，本篇 raw 没有它们，本页没有依据。**
- [[spmu-pin-task-mode]] — **⚠️ 本页是那一页的「另一半」。**
  [[spmu-pin-task-mode]] 那页记着：**它那一篇 raw 在讲某个错误时推荐
  `it is recommend using the FLEX_RELAY class instead`**，
  并且那页明写「**本页只有「推荐用它」这半句；`FLEX_RELAY` 怎么用、和本函数差在哪，本页没有**」。
  **那一半就是本页。**
  **⚠️ 但反过来不成立**：**本篇 raw 里 `SPMU_PIN_TASK_MODE` 0 次、
  也没有推荐谁来替代谁**——**所以「替代」这层关系只在那一篇里，本页一个字都没有。**
  （**这一条的原文引自 wiki 的 [[spmu-pin-task-mode]] 页，不是本篇 raw。**）
- [[spmu-pin-task]] / [[pin-utility]] / [[digital-pins-editor]] / [[dps-pins-editor]] —
  **（推断）同族的 pin 侧 L2 对象 / GUI**，**依据只是它们同在
  `02.07.04` 那一支或同在 `stage: pin`**。**本篇 raw 里这四个名字一个都没有**，
  **本页没有读那几页，所以这是推断。**
- [[controlling-multiple-sites]] / [[on-first-invocation-begin]] / [[on-first-invocation-end]] /
  [[for-each-site-begin]] / [[for-each-site-end]] — **多 site 那段例子里的五个构件**。
  **本页只有「它们出现在这段代码里、分别包住哪几步」这一个事实；
  每个标记自己的语义在那五页。**
- `FLEX_PIN_RELAY` / `FLEX_UTILITY_RELAY` / `FLEX_UTILITY_PURPOSE_RELAY` /
  `FLEX_UTILITY_CHANNEL_RES`（**四个，均未建**）— **本页的四个子容器**，
  也是原文 `#### Subtopics` 列的四篇（**本页一篇都没读**）。
  **`set()` / `on()` / `off()` 这些真正改设置的成员函数都在那四篇里。**
- `Routing.util()` / `Routing.util_purpose()`（**未建、不在 allowlist，故用反引号**）—
  **原文特性第 4 条里与 `FLEX_RELAY` 并列的那条旧路**（**由 FLUSH 激活**）。
  **它属于哪个类、怎么用，本篇没有。**
- `Pin Configuration window`（**未建**）— **`pin()` 那条硬约束点名的窗口**。
  **它与 [[pin-configuration-tool]] 是不是同一个东西，本页没有依据。**

## 版本

原文 `## Functional changes` **三条**，条目逐字：

- `Introduced before SmarTest 6.3.2`
- **SmarTest 6.5.2**：`New member function util_channelRes().`
- **SmarTest 7.10.1**：`Three-digit utility pogo block designator on V93000 EXA Scale systems.`

**三条读法：**

1. **第一条是 §11.2 ② 那个哨兵值**（`Introduced before SmarTest 6.3.2` =
   「早于语料覆盖范围」），**不是「6.3.2 新增」**——
   **所以 `FLEX_RELAY` 本身成立于哪个版本，这份语料里没有。**
2. **六个成员函数里只有一个有版本条目**：`util_channelRes()` 是 **SmarTest 6.5.2** 加的
   ——**这与它「不在 `execute()` 那三步里的任何一个」可能是同一件事的两面**
   （**推断**：它是后来加的，所以**依据只是这个版本号与那三步的措辞**；
   **原文没有把这两件事联系起来**）。
   **另外五个函数（含 `pin()` / `util()` / `util_purpose()` / `wait()` / `execute()`）
   什么时候有的，本篇没说。**
3. **7.10.1 那一条讲的是 utility pogo block 编号改成三位。**
   **（推断）它与本页的 `util_channelRes()` / utility line 编号有关**——
   **依据是同一句在语料里也出现在 [[utility-purpose-editor]] 那篇的版本段里**
   （**那是我读的另一篇 raw，逐字也是 `SmarTest 7.10.1: Three-digit utility pogo block
   designator on V93000 EXA Scale systems.`**），**而那一篇讲的是 utility purpose 的编辑器**；
   **本篇没有解释这条改动对 `FLEX_RELAY` 的参数写法有没有影响，所以这是推断。**

详见 [[smartest-6.3.2]] / [[smartest-6.5.2]] / [[smartest-7.10.1]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68_FLEX_RELAY.md`
（`74892.htm`，338 行）——**整篇读完**。

**本页做了什么**：

- **整篇读完**。
- **没有看任何图**（**没有图可看**：本篇 raw 里图片引用 0 处，两个例子都是代码块）。
- **为了核「本页与 spmu-pin-task-mode 的替代关系」这一句，读了 wiki 的
  `wiki/objects/spmu-pin-task-mode.md`**（**是 wiki 页，不是 raw**）——
  **只用来看那一页把本页写成了什么关系**。结论写在「和谁有关」里，
  **并标明「那一条原文引自那一页，不是本篇 raw」。**
  **本页正文没有引用它的任何技术事实。**

**本页没做的**：

- **四个子容器一篇都没读**（`FLEX_PIN_RELAY` / `FLEX_UTILITY_RELAY` /
  `FLEX_UTILITY_PURPOSE_RELAY` / `FLEX_UTILITY_CHANNEL_RES`，即原文 `#### Subtopics` 那四篇）——
  **这是本页最大的空缺**：**`set()` / `on()` / `off()` 这些真正改设置的成员函数全在那四篇里。**
  **所以「`set("IDLE","X")` 那两个参数各是什么」「`setting_1 = "1,1,1,0,0"` 那串值的
  每一位怎么对到 line 上」——本页只有例子的字面，没有语义依据。**
- **六个成员函数的签名与参数表都没进「语法 / 参数」节。** 脚本抽到的段只有
  `### Examples`（2,406 字符，**含 `### Single site testing` 与 `### Multi-site testing` 两个子节**）——
  **`#### Subtopics`、`## Class definition`、`## Member functions` 三节的正文一句都没进**。
  **所以本页正文里那六行函数表、四个参数说明、`execute()` 的三步，全都是本页从原文转述的，
  不是逐字**；**凡加 `>` 的地方才是逐字原文。**
- **`FlexRelay.h` 头文件没读**（它是一个系统路径，不在语料里）——
  **所以 `FLEX_PIN_RELAY` 等四个类的完整接口、`set()` 的重载形态，本页一个都没有。**
- **一行代码都没有编译、没有实跑。** `verified: doc-only` 指的就是这件事。
- **`Routing.util()` / `Routing.util_purpose()` 没读** —— 所以原文那条「建议」
  在实际差别上是怎么来的，本页不知道（**只知道建议本身**）。
- **`TASK_LIST` 与 `FLUSH` 两篇都没读** —— **所以两条执行路、两条生效路的内部机制，
  本页只有原文那句对照。**
- **没有动 `wiki/index.md`**，也没有改 `wiki/stages/pin.md`
  （**那一页把本页写成 `L2`、一句话是「运行期统一控制数字 channel 继电器与
  utility line 驱动的用户继电器」——这一句与本篇第一句意思一致，
  但那是 wiki 页的写法，不是本页写的**）。

> ⚠️ **本篇的语料瑕疵与对不上的地方，照实记、一处都没替它改**：
>
> **① `util_purpose()` 的说明句被复制粘贴成了 `util()` 的那一句。** 逐字并列：
> - `util()`：`returns the reference to the FLEX_UTILITY_RELAY class object that represents the setup data for relays associated with the specified` **`utility lines`**`.`
> - `util_purpose()`：`returns the reference to the FLEX_UTILITY_PURPOSE_RELAY class object that represents the setup data for relays associated with the specified` **`utility lines`**`.`
> ——**第二句说的是 `util_purpose()`，却写成 `associated with the specified utility lines`**；
> **按它自己的参数说明（`A utility purpose name or a list of utility purpose names`），
> 这里应当是 `utility purposes`。** **原文如此，本页照抄，不替它改。**
>
> **② 「四个」后面只列了三样。** 逐字：
> ```
> This class has four subsidiary data containers, which are for digital pins, utility lines, and utility purposes, respectively.
> ```
> ——**`four subsidiary data containers`，但 `which are for` 后面只有三项**
> （`digital pins`、`utility lines`、`utility purposes`）**，而且句尾还用了 `respectively`。**
> **第四样（utility line channel resources）是在下面那一串 bullet 里才出现的**，
> **不在这一句里。** **本页照抄，不替它补第四项、也不替它改成 `three`。**
>
> **②b 同一篇的模板里有个变量名少一个字母。** 逐字：
> ```
> object.util_purpose("uti_purposelist").member_func;
> ```
> ——**`uti_purposelist`**（**少一个 `l`**，其余三处模板里对应位置的写法是
> `"pinlist"` / `"utilitylist"` / `"channel_list"`）。
> **它是占位符，不是 API 名，所以不会有编译错误**——**但同一篇里另外三个都拼得整齐。**
> **本页照抄，不替它补那个 `l`。**
>
> **③ 两个例子对同一个 `set()` 用了两种参数形态，原文都没解释。** 逐字并列：
> `frelay.pin("PIN1").set("IDLE","X");`（**单 site，两个参数**）
> 与 `frelay.pin("PIN1").set("IDLE");`（**多 site，一个参数**）；
> 以及 `frelay.util_purpose("group1,group2").set();`（**无参**）
> 与 `frelay.util(utilgrp).set(setting_1);`（**带一串值**）。
> ——**`set()` 属于子容器，本页没读那四篇，所以四种形态各是什么意思本页不知道。
> 本页并列，不替它判定哪个是笔误。**
>
> **④ 单 site 例子里的注释用「编号」指 utility line，代码里用「名字」，两者的对应原文没说。**
> 逐字：注释写 `Change 16501 to OFF.` 与 `Change 16504 and 16506 to ON.`，
> **而紧跟着的代码是** `frelay.util("UTL101").off();` 与 `frelay.util("UTL104, UTL106").on();`。
> ——**注释用 `16501` / `16504` / `16506`，代码用 `UTL101` / `UTL104` / `UTL106`。**
> **（推断）命名规律是 `UTL1nn` ↔ `165nn`**（**依据是两处例子里的对应：
> 本页多 site 那段的注释把 `UTL1`–`UTL5` 对到 Site1 的 `16501`–`16505`，
> 而单 site 这段把 `UTL101`/`UTL104`/`UTL106` 对到 `16501`/`16504`/`16506`**）——
> **但原文没有给出这条规律，所以这是推断，不是文档事实。**
>
> **⑤ `execute()` 的执行顺序里没有 `util_channelRes()`。** 三步逐字是
> `Download the settings of relays related to digital pins…` /
> `Download the settings of utility lines specified with util_purpose()/util()…` / `Wait for the specified time.`
> ——**第二步只点了 `util_purpose()` 与 `util()`，第四个取子容器的函数没有出现在任何一步里。**
> **那它设的东西什么时候下去，原文没说。本页照实指出，不替它补。**
> （**可对照的是 `## 版本`：`util_channelRes()` 正是唯一有版本条目的那个函数，
> 而且是 6.5.2 才加的——这个「对得上」是推断，原文没说。**）
>
> **⑥ `## Class definition` 一节的结构和 `## Member functions` 一节的标题全是残的。**
> 逐字（**注意它们挤在同一行里**）：
> ```
>   List of parameters The constructor has no parameters. Return value The constructor has no return value.     Member functions
> ```
> ——**`List of parameters`、`Return value`、`Member functions` 三个「小标题」被塞进同一行**，
> 后面紧跟着那串成员函数 bullet。
> **同一节里 `  Constructor` 是一行裸词开头**（行首两个空格，没有冒号、不是标题）。
> **而 `## Member functions` 一节里每个函数的「小标题」也是同类**，逐字（例）：
> ```
>    |   Return value A reference to the [FLEX_PIN_RELAY](<…>) class object.   util()
> ```
> ——**下一个函数名 `util()` 被粘在前一个函数的 `Return value` 那句话末尾**，
> **中间只有三个空格，没有换行、没有标题标记**。
> **`util_channelRes()` / `util_purpose()` / `wait()` / `execute()` 四处都是这个形态。**
> **本页照实说，不替它断行、不替它补标题。**
>
> **⑦ 参数表也是同一族残破形态。** 逐字（`pin()` 那一份的开头）：
> ```
>  | Parameter  | Description |
>  | pinlist |
> ```
> ——**两行合起来的表头 + 一个孤立的参数名行**，
> **而说明文字落在表外**（与 [[dscp]] / [[uptd]] / [[dc-scale-limits-editor]] /
> [[pin-utility]] 几篇的表格残破同形）。**本页照实说，不替它补竖线。**
>
> **⑧ `#### Subtopics` 用的是四级标题**（`####`），而它是紧跟 `# FLEX_RELAY` 的第一节——
> **标题层级比正文里别的节还深**（`## Class definition` / `## Member functions` 都是二级）。
> **同一篇里层级是乱的。本页照实说。**
>
> **⑨ 单 site 例子的注释里有拼写与语法毛病，逐字记、一处没改：**
> `All the relay settings are download to the hardware after checking whether the settings are
> validated or not.`
> ——**`are download` 应为 `are downloaded`**。
> （**同一篇 `## Examples` 上面那句说明里也有同一个毛病**，两处逐字相同。）
>
> **⑩ 多 site 例子里有两行裸省略号。** 逐字：
> ```
>     //
>     // Execute a test here
>     //
>     ...
>     ...
> ```
> ——**两个 `...` 是原文自己写的**（**不是本页的截取标记**，见 §11.1 那一条：
> **省略号出现在引文里的唯一合法场合就是原文自己写着它**）。
> **本页在两个例子的表里照原样记成 `...` `...`，不替它展开。**
>
> **⑪ §11.2 ① 那种编码损坏本篇没有。** 本页查过：**本篇只有 ASCII**——
> CJK 字符 0 个、U+00A0 0 个、`鈥` 0 个、`鈭` 0 个。
> **§11.2 ⑤ 那个整词替换（`DC/DC power units`）本篇 0 命中。**
> （**本页有 `V93000` 与 `hp93000` 两个串——那是设备名与路径，不是坏字。**）

`verified: doc-only`
