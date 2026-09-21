---
type: object
title: PRIMARY_STATUS - (Primary)
layer: L2
stage: level
tags: [primary, timing-set, level-set, dps-set, start-label, timing-spec, level-spec, flush, mcd, multiport]
related: [timing, level, timing-spec, level-spec, spec-set, flush, ctim, execution-context, sequencer]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# PRIMARY_STATUS - (Primary)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **474 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Change the primary timing set

```
Primary.timing(3);

FUNCTIONAL_TEST();
```

The timing member function specifies timing set 3 as the primary timing set to be defined, and FUNCTIONAL_TEST reflects it to the hardware then executes a functional test.

### Retrieve the primary DPS set

```
INT dps_setNum;
...
dps_setNum = Primary.getDps();
```

The getDps member function returns the DPS set number that is currently defined as the primary into the variable dps_setNum.

<!-- 语法节 end -->

## 是什么

**`PRIMARY_STATUS` 是「数字 primary 的定义容器」这个 API。** 原文第一句就是全部机制：

> 「The PRIMARY_STATUS API accesses the data container holding the current definitions of
> digital primaries (timing-related primaries, level-related primaries, and start label).
> These definitions can be changed using the member functions.」

**「digital primaries」是一张清单，不是一个数**。按原文成员函数的划分，它至少含六样：

| 原话 | 管的是什么 |
|---|---|
| `timing()` | **the timing-related primaries (except the waveform set)** |
| `waveform()` | **waveform set**（被 `timing()` 明确排除，单独一个函数） |
| `level()` | **the level-related primaries (except DPS set)**（同上，DPS 被排除） |
| `dps()` | **DPS set** |
| `label()` | **the (digital) sequencer start label name** |
| `getTimingSpec()` / `getLevelSpec()` | **方程式的 primary**（equation + spec set 号 + spec 值） |

**排除关系是原文写死的**：`timing` 与 `level` 的说明都带一个 `except`，
**所以「primary timing」不含 waveform、「primary level」不含 DPS**——**这是四个独立的 primary**。

### 这个对象不许你造，只能用系统给的那一个

> 「There is no constructor available for this class.」

> 「To use the PRIMARY_STATUS API, you must always use the system-prepared class object
> Primary which represents the current definitions of the digital primaries or represents the
> digital primaries to be defined. You cannot create any object of this API.」

**所以语法永远是 `Primary.xxx()`，没有 `PRIMARY_STATUS obj;` 这种写法。**
定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/PrimaryStat.h`。

**`Primary` 有两种时态**（上面那句 `or` 的两半）：**表示「当前已定义的定义」，
或表示「将要被定义的定义」**——**改了不等於生效，这就是下一页「三层生效」的来由。**

### 下层还有三个容器：TIMING_SPEC / LEVEL_SPEC / SPECIFICATION

> 「This API can also be used to call the subsidiary data containers: The TIMING_SPEC and
> LEVEL_SPEC. API's class objects. Call these objects to change the definitions of the primary
> timing equation/spec sets and primary level equation/spec sets, and to change the definitions
> of the spec values. For multi-port testing, another subsidiary data container, the
> SPECIFICATION API's class object is available.」

**「spec 值」不在 `PRIMARY_STATUS` 里改，要穿过一层到下层容器去改**——
第三个使用形态就是干这个的（`Primary.member_f.s_member_f;`）。
原文对 `s_member_f` 的定义是：**`A member function of the subsidiary data container.
Only one member function is available.`**——**每层只有一个函数可用，不是随便挑。**

### 最关键的一件事：改完之后，什么时候才生效

**原文自己把「生效」拆成了两个动作：写进 MCD（及 UI）与激活到硬件。**
**这两件事由不同的 API 触发。**

**① 激活到硬件**——原文给了完整清单：

> 「The changes of the definitions specified by this API are actually reflected to the hardware
> when any of the following APIs is executed.」

| 直接激活（不需要 FLUSH） | **要先 `FLUSH` 再调** |
|---|---|
| `EXECUTE_TEST` | `FLUSH` → `SPEC_SEARCH.execute()` |
| `START_TEST` | `FLUSH` → `SEQUENCER_STATUS.run()` |
| `DIGITAL_CAPTURE_TEST` | `FLUSH` → `PMU_IFVM.execute()` |
| `NB_DIGITAL_CAPTURE_START` | `FLUSH` → `PMU_VFIM.execute()` |
| `FUNCTIONAL_TEST` | `FLUSH` → `TASK_LIST.execute()` |
| — | `FLUSH` → `DPS_VFIM.execute()` |

**② 反映到 MCD / 界面**（原文：这是**可选项**）：

> 「The changes of the definitions specified by this API can be also reflected to the MCD when
> the FLUSH API is executed. This is an option to reflect the changes on the user interface such
> as the Test Program Explorer and the Spec Tool.」

**即：`FLUSH` 管的是「让 MCD 和界面看到」，上面那五个 API 管的是「让硬件照做」。**
**`FLUSH` 顺带也能激活**（所以左表右栏写「要先 `FLUSH` 再调」而不是「不能激活」）。

### 三条硬条件，**漏一条就白改**

| 条件 | 原文要点 |
|---|---|
| **测 analog 时 `FUNCTIONAL_TEST` 不够** | `However, FUNCTIONAL_TEST does nothing for the analog set and routing set (execute FLUSH before FUNCTIONAL_TEST if you execute a functional test that involves an analog module).` |
| **DC 测试前必须先 `FLUSH`** | `If you need to generate vectors in a DC test API (PMU_VFIM, PMU_IFVM, or DPS_VFIM) after you specify the change of digital primaries using the PRIMARY_STATUS API, execute the FLUSH API beforehand to reflect the changes.` |
| **`NPRM` 会**抑制**激活** | 脚注 3：`Activating timing/level-related primaries is suppressed if you specify NPRM in the PreAction member function in PMU_VFIM, PMU_IFVM, DPS_VFIM, or SPMU_TASK (except SEQUENCER_STATUS / SPEC_SEARCH/TASK_LIST / DPS_TASK). For SPMU_TASK, NPRM is the default setting.` |

> **第三条最容易踩**：**`SPMU_TASK` 的 `NPRM` 是默认设置**——
> **也就是说用 `SPMU_TASK` 时「改了 primary 但没生效」是默认行为，不是故障。**

### **读回来的不是「现在跑的那个」**（`CTIM` / `CLEV` 陷阱）

> 「For retrieving the definitions, the current activated definitions are returned. Note that
> even if the timing set (or level set) is changed from the primary one to another one by the
> CTIM (or CLEV) sequencer instruction during the vector generation of the start label, the
> CTIM (or CLEV) sequencer instruction does not change the definition of primary timing set
> (or primary level set).」

`getTiming()` 的说明里又把同一件事说了一遍：

> 「(Note that the CTIM sequencer instruction changes the timing set, but does not change the
> definition of the primary).」

**`getLevel()` 那条也一样**（`note` 小写，见「出处」的 ⚠️）：
> 「(note that the CLEV sequencer instruction changes the level set, but does not change the
> definition of the primary).」

**记法：`CTIM` / `CLEV` 换的是「正在用哪个 set」，`Primary` 记的是「哪个 set 被定义成 primary」。**
**两件事。** 所以 **`Primary.getTiming()` 回答不了「现在在跑第几号 timing set」这个问题**——
**要问现在跑哪个，得问 sequencer 侧（见 [[sequencer-status]]），不是问 `Primary`。**

### 改一次、什么时候被**清掉**

> 「When one of the following member functions is executed, the changes of the primary timing
> set number and spec values that are specified in the PRIMARY_STATUS, TIMING_SPEC, and
> SPECIFICATION APIs are cleared if the FLUSH API has not been executed for them yet.」

被点名的三个函数：

```
timing(const TIMING_SPEC& specset)
waveform(INT wfset)
timing(const SPECIFICATION& specif)
```

**即：改了 spec 相关的东西却没 `FLUSH`，又被上面三个函数之一碰过 → 那次改动**没了**，且不报错。**

### 20 个成员函数，按用途分五组

**基类 17 个 + 多端口额外 6 个。**原文列在 "Member functions" 标题下（**该标题在语料里掉了层级，见「出处」**）。

| 用途 | 函数 | 要点 |
|---|---|---|
| **改 primary** | `timing()` `waveform()` `level()` `dps()` `label()` | **`tset` / `wfset` / `lset` / `dpsset` 传 `0` → 定义不变**；`timing()` 有 **4 个重载，靠参数类型分派**（`Which primary you specify is determined by the data type of the specified parameter.`）；**方程式模式下也用这几个号参数**（`Even if the setup is equation-based, use this parameter…`） |
| **读号** | `getTiming()` `getLevel()` `getDps()` `getWaveform()` `getLabel()` | 各有前提：`getWaveform` 要求 **a waveform set … must currently be defined as the primary**；`getDps` 要求 **a DPS set of the level setup**；`getLabel` 返回的是 **the currently activated (digital) sequencer start label**，多端口下可以是 **the multi-port burst label** |
| **读下层容器** | `getTimingSpec()` `getLevelSpec()` `getSpecification()` | **`getSpecification()` 只用于多端口**；三者都要求对应的 spec set **当前就是 primary** |
| **per-site 四个** | `assignLabelToCurrentSite()` `getAssignedLabelForCurrentSite()` `assignPinToCurrentSite()` `getAssignedPinForCurrentSite()` | **只能在 `FOR_EACH_SITE` 块内用**（`assignPinToCurrentSite` 例外，见下）；**要求 test suite 的 parallel enable 标志已设** |
| **端口判定** | `isTimingPortBased()` `isLabelPortBased()` | 两者原文都写 **`For multi-port testing (however, executable even for non-multi-port)`**；返回 `TRUE` 的含义见下 |

**`assignPinToCurrentSite()` 是组里唯一有两种模式的**（原文说得最细）：

| 在哪调 | 传什么 | 效果 |
|---|---|---|
| **`FOR_EACH_SITE` 块内** | **一个 pin 名**（该 pin 在当前 site 上与别的 site 共用一个 channel） | **让当前 site 的 start label 在这个 channel 上执行** |
| **块外** | **必须传空** | **撤销之前所有「共 channel 的 pin ↔ site」关联** |

**端口判定的返回含义**（两条容易混，并列）：

| 函数 | `TRUE` 表示 |
|---|---|
| `isTimingPortBased()` | **「当前 timing setup 是 port-based」**——即 **any specification of the timing setup is currently defined as the primary** |
| `isLabelPortBased()` | **「当前 vector setup 是 port-based」**——即 **any multi-port burst label is currently activated as the start label** |

> **原文给 `isTimingPortBased()` 的用途是「确认 specification 是不是 primary」**：
> 「You can confirm whether a specification is defined as the primary or not by using the
> isTimingPortBased member function.」

**`getModeContextName()`**：返回当前 active `mode context` 的名字，
参数是**一个已定义 string 变量的引用**，**原文说 `The member function returns always true.`**。

### 多端口的两条禁令 + 两种「rare usage」

**禁令**：**specification 已是 primary 时，`getTimingSpec()` 与 `getWaveform()` 不能执行**
（原文：`which are not for specification`）。

**两种少见切换**（原文自己标 `Rare usage`）——**要在同一个 test suite 内换 primary 的「种类」，
必须先用一个函数把种类改过去**：

| 从 → 到 | 先执行 |
|---|---|
| **specification → 非多端口的 TIMING_SPEC / waveform set** | `timing(const TIMING_SPEC& specset)` 或 `waveform(INT wfset)` |
| **非多端口的 TIMING_SPEC / waveform set → specification** | `timing(const SPECIFICATION& specif)` |

### 一条**跨层的**警告：别把 firmware 命令和 test method API 混着用

这段原文很硬，**它管的不只是本 API，而是「L1 命令 vs L2 API」这条界**：

> 「Do not mix the usage of the firmware command with the test method API to query or change
> the hardware status. The test method API uses an internal cache which is not known and not
> accessible to the firmware command. The hardware status change made with the firmware command
> is not recorded in the cache and the subsequent hardware status querying with the test method
> API may return an incorrect result. To query the hardware status with the test method API, you
> need to change the hardware status with the test method API. To query the hardware status with
> the firmware command, you need to change the hardware status with the firmware command.」

**一句话：test method API 走内部 cache，firmware 命令不认这个 cache。
「谁改的谁去读」——用 A 改就必须用 A 读，混用会读到错的。**

### 三种使用形态（原文 "Syntax for common tasks" 的表）

| 要干什么 | 写法 | 原文对占位符的说明 |
|---|---|---|
| **改 primary 定义** | `Primary.memberFunction();` | `Member functions of the PRIMARY_STATUS API.` |
| **读一个号**（timing/waveform/level/DPS set 号或 start label） | `return_value = Primary.memberFunction;` | **`For retrieving data, only one member function is available.`**（**注意第二个形态没有括号**） |
| **读/改方程式与 spec 值** | `return_value = Primary.member_f.s_member_f;` | `member_f` = **`getTimingSpec` 或 `getLevelSpec`**；`s_member_f` = **下层容器的某个函数，`Only one member function is available.`**；多端口用 `getSpecification` |

## 典型用法

**1. 改一个号，然后让它生效**（原文 "Change the primary timing set" 例，逐字）：

```
Primary.timing(3);

FUNCTIONAL_TEST();
```

> 「The timing member function specifies timing set 3 as the primary timing set to be defined,
> and FUNCTIONAL_TEST reflects it to the hardware then executes a functional test.」

**2. 读一个号**（原文 "Retrieve the primary DPS set" 例，逐字）：

```
INT dps_setNum;
...
dps_setNum = Primary.getDps();
```

> 「The getDps member function returns the DPS set number that is currently defined as the
> primary into the variable dps_setNum.」

**3. 改 primary 的完整顺序**（把上面几节拼起来，**每一步都有依据**）：

| 步 | 做什么 | 依据 |
|---|---|---|
| ① | **用 `Primary.timing()` / `.level()` / `.dps()` / `.waveform()` / `.label()` 选号** | 传 `0` 表示「不改」 |
| ② | **要改 spec 值 → 穿过 `getTimingSpec()` / `getLevelSpec()` 到下层容器改** | `Primary.member_f.s_member_f;` |
| ③ | **决定怎么生效**：用五个直接 API / 用 `FLUSH` / DC 测试前必须 `FLUSH` | 见上面「三层生效」的两张表 |
| ④ | **测 analog 或 routing → 一定补 `FLUSH`** | `FUNCTIONAL_TEST does nothing for the analog set and routing set` |
| ⑤ | **用 `SPMU_TASK` → 检查 `PreAction` 里的 `NPRM`** | 默认就是 `NPRM`，会**抑制激活** |

**4. per-site start label 的顺序**：**必须开 test suite 的 parallel enable 标志** →
**进 `FOR_EACH_SITE` 块** → **`assignLabelToCurrentSite(label)`** →
**要读回来用 `getAssignedLabelForCurrentSite()`**。
**块内、parallel enable 未设，这两条任一不满足都用不了。**
原文把「怎么分 site 跑不同 pattern」指到了另一篇（`How to execute separate patterns per site`，**本页没读**）。

**5. 一个使用上的判断**：**要「现在在跑哪个 set」→ 不要问 `Primary`**（`CTIM`/`CLEV` 不改 primary 定义），
**去 sequencer 侧问**（[[sequencer-status]] / [[sqst]]）。

## 和谁有关

**上游（本 API 的下层容器，改 spec 值必须经过它们）**：

- [[timing-spec ]] — `getTimingSpec()` 返回的就是它的 class object；
  **primary timing 的 equation/spec set 号与 spec 值存在这里**
- [[level-spec ]] — 同上，level 侧
- `SPECIFICATION`（**未建**，**且不在 allowlist 里**）— **多端口专用**的第三个下层容器；
  原文：`another subsidiary data container, the SPECIFICATION API's class object is available`

**下游 / 生效链（改了 primary 要靠它们才落地）**：

- [[flush ]] — **`FLUSH` 是本页的枢纽**：它把改动反映到 MCD 与 UI
  （[[test-program-explorer]]/ `Spec Tool`（**未建**）），
  **也是 DC 测试前的前置**。**没有 `FLUSH`，spec 改动还会被三个函数清掉**
- [[sequencer-status]] — 原文列在「`FLUSH` 之后才激活」的左表里
  （`FLUSH then SEQUENCER_STATUS.run()`）；**它也是「现在在跑哪个 set」的答案所在**
- [[spec-set]] — 同属 `stage: level`、同属 spec set 这条线；**本页讲 primary 是哪一套，它讲套本身**

**陷阱 / 反例（最容易读错的一条）**：

- [[ctim]] — **`CTIM` 换 timing set 但不改 primary 的定义**；
  `CLEV`（**不在 allowlist**）是它在 level 侧的对应物。**这两条是本页「读回来的是什么」那节的根**

**同层 / 同阶段**：

- [[execution-context]] — 同批建页；**本页的 `getModeContextName()` 读的 mode context
  与执行上下文是同一层的话题**，但**该页讲什么本页没读，不作断言**
- [[sequencer]] — start label 那一半的上游：**`label()` 指定的 start label 是 sequencer 的入口**
- [[timing]] / [[level]] — 阶段页；**本页是这两个阶段里「primary 是哪一套」的那一环**

**`FOR_EACH_SITE` 那四个函数牵出的**：

- [[for-each-site-begin]] / [[for-each-site-end ]] — **per-site 四函数的活动范围**
- [[label-edit-requires-tstl-selection]] — **同类约束页**：都在讲「某个 per-site / label 操作有前置条件」。
  **本页的前置条件是 parallel enable 标志 + `FOR_EACH_SITE` 块**

**被本页点名的其它 API（均未建，不链）**：
`FUNCTIONAL_TEST` / `START_TEST` / `EXECUTE_TEST` / `DIGITAL_CAPTURE_TEST` /
`NB_DIGITAL_CAPTURE_START` / `PMU_VFIM` / `PMU_IFVM` / `DPS_VFIM` / `TASK_LIST` /
`SPMU_TASK` / `DPS_TASK` / `SPEC_SEARCH` / `ANALOG_STATUS` / `ROUTING_STATUS`。
**它们每一个的语义本页都不知道，本页只知道「它们会触发 primary 的 define / activate」。**

> **本页的「和谁有关」全部来自这一篇原文里点到的名字。** 原文没有给本页的入边/出边统计，
> **本页也不替它算。**

## 版本

本文档有 `## Functional changes` 段，**全部内容两条**：

- **`Introduced before SmarTest 6.3.2`**
- **`SmarTest 7.5.3: New member function getModeContextName().`**

> **上面第一条**不是**「6.3.2 新增了 `PRIMARY_STATUS`」。**
> 按 §11.2 ② 的约定，`Introduced before SmarTest 6.3.2` 是个**哨兵值**，
> 措辞里的 `before` 意思是「**在本文档集覆盖范围开始之前就已经有了**」。
> **照字面读会得到一条格式齐整但错的信息，本页照实两边都写出来。**
>
> **所以本页能确定的版本事实只有一条：`getModeContextName()` 是 SmarTest 7.5.3 加的。**
> **`PRIMARY_STATUS` 本身何时引入，本文档没说。**
> （`7.5.3` 同时是 [[smartest-7.5.3]] 那一版的覆盖范围，**该页本页没读**。）

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.md`
（raw 的 `source_topic: "29640.htm"`）。

**本页没做的**：

- **所有被本页点名的其它 API 一篇都没读**：`FLUSH` / `TIMING_SPEC` / `LEVEL_SPEC` /
  `SPECIFICATION` / `CTIM` / `CLEV` / `FUNCTIONAL_TEST` / `START_TEST` / `EXECUTE_TEST` /
  `DIGITAL_CAPTURE_TEST` / `NB_DIGITAL_CAPTURE_START` / `PMU_VFIM` / `PMU_IFVM` / `DPS_VFIM` /
  `TASK_LIST` / `SPMU_TASK` / `DPS_TASK` / `SEQUENCER_STATUS` / `SPEC_SEARCH` /
  `ANALOG_STATUS` / `ROUTING_STATUS`。**它们的语法、参数、返回值本页一个字都没有**——
  **本页只有「它们会让 primary 生效 / 不生效」这一件事。**
- **`How to execute separate patterns per site` 没读**（原文在 `assignLabelToCurrentSite` 与
  `assignPinToCurrentSite` 下各指了一次）。**所以「per-site start label 具体怎么落地、
  与 pin 映射怎么配合」本页没有。**
- **`Mode contexts` 那篇没读**（`getModeContextName` 指过去）。**mode context 是什么、有几个，本页不知道。**
- **「语法 / 参数」节里只有两个 `Examples`，没有语法表。** 原因是语料的节标题掉了层级
  （见下 ⚠️ ④），抽取器认不出 `Syntax` 段标记。
  **本页正文里的「三种使用形态」表是我从原文散文里读出来重排的，
  它的原始位置在 raw 的 ` Syntax for common tasks` 那一节**——
  **想看原文那张表，得回 raw，别只看本页。**
- **原文那张「When Primaries and Spec Values are Defined as New Settings (in MCD) and
  Activated in Hardware」大表，本页只用了能确定还原的前 3 行**（Testsuite dialog 上的
  timing/level primaries、start label、analog set）。**后 4 行（`PRIMARY_STATUS` 的
  timing/level primaries、start label、spec 值，以及 `ANALOG_STATUS`/`ROUTING_STATUS` 的
  analog/routing set）的单元格在语料里缺格**（见下 ⚠️ ①），**本页不替它拼。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 那张「define / activate」大表被拆成了「一列一行」，且部分行缺格。**
> raw 里长这样（逐字）：
> `When Primaries and Spec Values are Defined as New Settings (in MCD) and Activated in Hardware`
> 下一行是 ` | |`，再往下每个单元格各占一行。**前三行能拼回 4 列，后四行拼不出来**——
> 例：`Timing/Level-related primaries specified by PRIMARY_STATUS` 之后只有
> `   |   | |`、`Define`、`Activate if defined by FLUSH[3)](<#_29640__fn3>)` 三段，
> **其余列在语料里就没有。** **本页把它记成缺陷，不还原。**
>
> **② 脚注定义被 `## Functional changes` 段吞了**——这正是 §11.2 ③ 写的那件事，
> 本篇是 171 篇之一。raw 里 `## Functional changes` 的两条之后紧跟着
> `[1)](<#fnsrc_1>) The testflow automatically does the above in each testsuite…` 起头的四条脚注。
> **本页引 `NPRM` 那条时引的是脚注 3 的正文，它在这个位置。**
>
> **③ 一个小节标题被粘进了上一段末尾。** `isTimingPortBased()` 那条 Note 的最后一句是
> `To query the hardware status with the firmware command, you need to change the hardware
> status with the firmware command. isLabelPortBased()`——**`isLabelPortBased()` 是下一个
> 函数的标题，被并进了 Note 段落**，后面紧跟的才是它的代码块。
> **本页正文里那条 Note 与 `isLabelPortBased()` 是分开写的，但语料里是粘的。**
>
> **④ 节标题掉层级：`## Class definition` 之后的标题全部只有两个前导空格**，
> 如 `  Constructor`、`  Member functions`、`  timing()`、`  getTiming()`，
> 连 ` Syntax for common tasks` 也是。**这就是「语法 / 参数」节只抽到 `Examples` 的原因**
> （抽取器认的是段标记，不认两个空格的伪标题）。**本页不改语料，只记这一笔。**
>
> **⑤ 同一件事两种大小写。** `getTiming()` 下是 `(Note that the CTIM sequencer instruction…`，
> 而 `getLevel()` 下是 `(note that the CLEV sequencer instruction…`——
> **同一个 `Note`，一处大写一处小写**。本页两处都按原文引了。
>
> **⑥ 正文里直接留着脚注锚点。** 例：`and Activated in Hardware` 那行后面的
> `[1)](<#fntarg_1>)`、`[2)](<#fntarg_2>)`、`[3)](<#_29640__fn3>)`——
> **是 raw 里的锚点残留，不是本页加的。**
>
> **⑦ 第三个使用形态里的占位符是下划线形式** `Primary.member_f.s_member_f;`，
> 而它上面那张表又用 `memberFunction`（驼峰）——**两处命名风格不一致**，本页照引。
>
> **⑧ `Primary` 这个词在原文里既指「系统给的 class object」，又出现在
> 标题 `PRIMARY_STATUS - (Primary)` 里**；文件名是
> `02.07.04.01.167_PRIMARY_STATUS_-__Primary.md`（`- (` 变成了 `-__`）。
> **本页按 raw 文件名写路径。**

`verified: doc-only`
