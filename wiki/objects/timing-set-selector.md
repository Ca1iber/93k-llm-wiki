---
type: object
title: TimingSetSelector
layer: L2
stage: timing
tags: [timing, l2, test-method-api, timing-set, digital-offset-search, waveform-set, equation-based-timing, multiport]
related: [timing, level-set-selector, digital-offset-search-pins, waveform-set, timing-specification, primary-status, mapping-timing, multiport-burst-editor, smartest-7.2.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# TimingSetSelector

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,562 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The default constructor `TimingSetSelector()` is equal to `TimingSetSelector(DIGITAL_OFFSET_SEARCH::PRM, DIGITAL_OFFSET_SEARCH::PRM). R` efers to the primary timing set.

The available constructors are:

```
TimingSetSelector();
TimingSetSelector (const TimingSetSelector& rhs);
TimingSetSelector (const TimingSetSelector* rhs);
TimingSetSelector (const STRING& multiportspec, INT timingset);
TimingSetSelector (INT waveformORspecId, INT timingset);
TimingSetSelector (DIGITAL_OFFSET_SEARCH::PRM_ALL waveformOrSpec,
                   INT timingset);
TimingSetSelector (const STRING& multiportspec,
                   DIGITAL_OFFSET_SEARCH::PRM_ALL timingset);
TimingSetSelector (INT waveformOrSpecId,
                   DIGITAL_OFFSET_SEARCH::PRM_ALL timingset);
TimingSetSelector (DIGITAL_OFFSET_SEARCH::PRM_ALL waveformOrSpec,
                   DIGITAL_OFFSET_SEARCH::PRM_ALL timingset);
TimingSetSelector(const TimingSetSelector & rhs, INT timingSet);
TimingSetSelector(const STRING& waveformOrSpec, const STRING& timingSet);
TimingSetSelector(const STRING& timingSelector);
```

Parameters
 |

Parameter

 |

Description

 |
 |

rhs

 |

The name of an existing TimingSetSelector object.

 |
 |

multiportspec

 |

The name of a multi-port specification, in a multi-port setup.

 |
 |

waveformORspecId (INT)

 |

In fixed timing setup, it is the waveform set number.

In equation based timing setup, it is a timing specification ID calculated as follows:

`100*equation_set_no + specset_no`

 |
 |

waveformOrSpec (`DIGITAL_OFFSET_SEARCH::PRM_ALL`)

 |

It can be:

- DIGITAL_OFFSET_SEARCH::PRM: Selects the primary specification
- DIGITAL_OFFSET_SEARCH::ALL: Selects all waveform sets in the fixed timing set.

Note that this option is only supported for waveform sets, not for specification ID's.

 |
 |

timingset

(`INT`)

 |

The timing set number to select.

 |
 |

timingset

(`DIGITAL_OFFSET_SEARCH::PRM_ALL`)

 |

It can be:

- DIGITAL_OFFSET_SEARCH::PRM: Selects the current primary timing set.
- DIGITAL_OFFSET_SEARCH::ALL: Selects all timing sets in a timing set group.
 |

Return value

There is no return value.

### Example

```
DIGITAL_OFFSET_SEARCH_TASK dos;
STRING strpins1("pcie_tx1n");
DIGITAL_OFFSET_SEARCH::TimingSetSelector dest("multi_port", DIGITAL_OFFSET_SEARCH::ALL);

  dos.pin(strpins1).resourceType(DIGITAL_OFFSET_SEARCH::RECEIVE).searchType(DIGITAL_OFFSET_SEARCH::EYE)
     .start(15).numSteps(120).stepWidth(15)
     .restoreFlag(DIGITAL_OFFSET_SEARCH::NO);
  dos.execute();
  dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::ALL_EDGES);
```

<!-- 语法节 end -->

## 是什么

**`TimingSetSelector` 是一个「指哪儿」的对象——它指的是一个 timing set，或者一批 timing set。**
本篇的第一句就是全部：

> This class refers to a single timing set or all fixed timing sets.

**它是干什么用的，本篇第二句也说了**：

> It is used with DIGITAL_OFFSET_SEARCH_TASK and DIGITAL_OFFSET_SEARCH_PINS.

**即：它不是自己干活的类**——它**只被那两个搜索类用**（那两个的文档**本页没读**，见「出处」）。
它**没有返回值**（语法节末那一格：`There is no return value.`），
**本篇也没有列出任何成员函数**——**类页上只有 11 个构造函数**。
所以它的身份是**一个「目的地」对象**：你把它造出来，交给搜索任务，
让搜索的结果落到它指的那些 timing set 上（下面「典型用法」里例子的最后一行就是这个用法）。

头文件：`/opt/hp93000/soc/prod_com/include/MAPI/DigitalOffsetSearchTypes.h`。
**本篇没有出现 `test method` 这个词**；`layer: L2` 的依据是**这个头文件路径**
（`soc/prod_com/include/MAPI/`，MAPI 是 Test Method API 那一族）——
**这一步是（推断），依据只是路径本身，不是本篇的正文。**

### 两个参数：第一个选「哪一套」，第二个选「这里面哪些」

原文对这两个参数有一段总述（**这是读懂本类唯一的钥匙**）：

> Two parameters are required:

> - The first one selects a waveform set (fixed timing) or a timing specification (equation based timing) or a multi-port specification.
> - The second parameter selects one or all timing sets from this waveform set or specification.

**把它摊成一张表：**

| 位置 | 能吃哪几种东西 | 对应的重载（见「语法 / 参数」节） |
|---|---|---|
| **第 1 个** | **① waveform set**（**fixed timing** 那一侧）<br>**② timing specification**（**equation based timing** 那一侧）<br>**③ multi-port specification** | `INT waveformORspecId` / `DIGITAL_OFFSET_SEARCH::PRM_ALL waveformOrSpec`（①②）；<br>`const STRING& multiportspec`（③） |
| **第 2 个** | **一个 timing set** 或 **全部 timing set** | `INT timingset` / `DIGITAL_OFFSET_SEARCH::PRM_ALL timingset` |

**这样一个类就把两套 timing 体系（fixed / equation based）都罩住了**——
**第一参数写「套」的名字或号，第二参数写「里面哪个」**。

### ⚠️ 同一个 `PRM` / `ALL`，在两个位置上意思不同

**这是本页最容易用错的地方。** `DIGITAL_OFFSET_SEARCH::PRM` 与 `::ALL`
**在第一个参数位和第二个参数位上各有一套定义**，原文把它们**分两格**写：

| 位置 | 取值 | 原文（逐字） |
|---|---|---|
| **第 1 个** | `PRM` | `DIGITAL_OFFSET_SEARCH::PRM: Selects the primary specification` |
| **第 1 个** | `ALL` | `DIGITAL_OFFSET_SEARCH::ALL: Selects all waveform sets in the fixed timing set.` |
| **第 2 个** | `PRM` | `DIGITAL_OFFSET_SEARCH::PRM: Selects the current primary timing set.` |
| **第 2 个** | `ALL` | `DIGITAL_OFFSET_SEARCH::ALL: Selects all timing sets in a timing set group.` |

**两个词、四个意思**：

- 位置 1 上的 `PRM` 指 **primary specification**，位置 2 上的 `PRM` 指 **primary timing set**；
- 位置 1 上的 `ALL` 指**这个 fixed timing set 里的全部 waveform set**，
  位置 2 上的 `ALL` 指**一个 timing set group 里的全部 timing set**。

**并且第 1 个位置上的 `PRM_ALL` 有个明确的限用条件**：

> Note that this option is only supported for waveform sets, not for specification ID's.

**即：第一个参数位上的 `PRM` / `ALL` 这套写法只对 waveform set 有效，对 specification ID 无效。**
原文把这句话放在**参数表里第 1 个位置的那一格**——
**所以「equation based 那一侧不能用 `PRM_ALL` 写法、只能给 ID」，是文档明写的。**

**默认构造函数是被定义成 `(PRM, PRM)` 的**（语法节第一句，逐字）：

> The default constructor `TimingSetSelector()` is equal to `TimingSetSelector(DIGITAL_OFFSET_SEARCH::PRM, DIGITAL_OFFSET_SEARCH::PRM). R` efers to the primary timing set.

**这句话在原文里被拆坏了**——`R` 与 `efers` 分家，见「出处」⚠️①。
**照参数表两格拼起来读**：`(PRM, PRM)` = **primary specification** + **current primary timing set**，
**也就是「不写参数时，指的就是当前那套 primary」。**

### equation based 那一侧：timing specification 的 ID 是算出来的

第一个参数在两个重载里叫 `waveformORspecId` / `waveformOrSpecId`（`INT`）。
**它在两套 timing 体系里分别是不同的东西**：

> In fixed timing setup, it is the waveform set number.

> In equation based timing setup, it is a timing specification ID calculated as follows: `100*equation_set_no + specset_no`

**公式是 `100 × equation_set_no + specset_no`**——**两位十进制拼法**：
**equation set 号占百位以上，specset 号占十位与个位**。
（**所以 `specset_no` 在公式里只有两位的容量**——这是（推断），依据是 `× 100`
这个系数与 `+ specset_no` 的形式；**原文没有写 `specset_no` 的取值范围**。）

### multi-port 那一侧：端口不由本类决定

> In the case of a multi-port specification, the ports which the selector refers to are determined by the pin list of the DIGITAL_OFFSET_SEARCH_TASK object.

**这是一条结构上的信息**：走 multi-port 时，第一个参数只是一个**名字**
（`const STRING& multiportspec`），**而「落到哪几个 port」不在本类里——
它由 `DIGITAL_OFFSET_SEARCH_TASK` 那个对象的 pin 列表决定**。
**本页没有那个类的事实**（那一篇没读）；**本篇也只写了这一句，没有展开。**

### 参数表与构造函数表对不齐的一处

11 个构造函数里，**有三个的第 1 个参数是 `STRING`**（见「语法 / 参数」节的构造函数清单）：
`const STRING& multiportspec`、`const STRING& waveformOrSpec, const STRING& timingSet`、
`const STRING& timingSelector`。

**但参数表只解释了 `multiportspec` 一个**（`The name of a multi-port specification, in a multi-port setup.`）。
**另外两处 `STRING` 参数——「一个字符串形式的 waveform set / timing set 名怎么写」——本篇没有对应行。**
**本页不补**（§11：文档没写就写「语料未写」）。

**参数表里另一处与签名不对的地方**：`rhs` 那格写的是
`The name of an existing TimingSetSelector object.`，
而两个取它的重载签名是 `const TimingSetSelector& rhs` 与 `const TimingSetSelector* rhs`——
**一个引用 / 一个指针，不是「名字」**。**原文如此**，见「出处」⚠️④。

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
**能当用法读的只有 `## Example` 段那一块代码**——它一共三件事，**顺序是明的**：

```
DIGITAL_OFFSET_SEARCH_TASK dos;
STRING strpins1("pcie_tx1n");
DIGITAL_OFFSET_SEARCH::TimingSetSelector dest("multi_port", DIGITAL_OFFSET_SEARCH::ALL);

  dos.pin(strpins1).resourceType(DIGITAL_OFFSET_SEARCH::RECEIVE).searchType(DIGITAL_OFFSET_SEARCH::EYE)
     .start(15).numSteps(120).stepWidth(15)
     .restoreFlag(DIGITAL_OFFSET_SEARCH::NO);
  dos.execute();
  dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::ALL_EDGES);
```

| # | 做什么 | 谁在做 | 文档依据 |
|---|---|---|---|
| 1 | **造一个 selector，指明目的地** | `TimingSetSelector dest("multi_port", DIGITAL_OFFSET_SEARCH::ALL);` | `## Example` |
| 2 | **配置并执行搜索** | `dos.pin(...).resourceType(...).searchType(...).start(15).numSteps(120).stepWidth(15).restoreFlag(...)`，再 `dos.execute()` | `## Example`（**这些方法都属于 `DIGITAL_OFFSET_SEARCH_TASK`，本篇没有它们的定义**） |
| 3 | **把结果上传到 selector 指的地方** | `dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::ALL_EDGES);` | `## Example` |

**第 3 步是本类在例子里的落点，也是本页唯一能确证的用法**：
**selector 是 `uploadResult()` 的第一个实参，也就是「结果往哪儿放」。**

**几点照实说明：**

- **`uploadResult` 的第二个实参 `ALL_EDGES` 在本篇的语法节与参数表里都没有**——
  它属于 `DIGITAL_OFFSET_SEARCH_TASK`（**那一篇本页没读**），
  **所以「结果类型还能取哪些值」本页答不出来。**
- **例子里 multi-port specification 的名字写的是 `"multi_port"`**（小写、带下划线），
  而参数表的说明是 `The name of a multi-port specification, in a multi-port setup.`——
  **原文没有写命名规则**，本页不据此声称任何大小写约定。
- **例子的多端口设置在哪、pin 列表怎么给**，**本篇一个字都没有**；
  只有那句「端口由 `DIGITAL_OFFSET_SEARCH_TASK` 的 pin 列表决定」。
- **`## Example` 段之外，本篇没有任何 `Note` / `Important points` / 使用建议。**
  所以「什么时候该用 `ALL` 而不是 `PRM`」「选错了会怎样」**语料未写**。

**与它配对的那个类，本篇只在 `## Related information` 里点了一个名字**（见下）。

## 和谁有关

- [[timing]] — **stage 页，也是本页 `stage: timing` 的理由**。本类选的是 timing set；
  **「Timing 这一段整体怎么走」在那一页，本页不写流程**（§2.2）。
- [[digital-offset-search-pins]] — **文档点名的使用者之一**（`It is used with DIGITAL_OFFSET_SEARCH_TASK and DIGITAL_OFFSET_SEARCH_PINS.`）。
  那一页讲的是**搜索条件**（`pin()` 返回的条件容器），**本页讲的是结果落到哪**。
  **两页的 raw 互不相同，本页没读它**——所以那条「被它用」的话**本页只能照抄，不能展开**。
- `DIGITAL_OFFSET_SEARCH_TASK`（**不在 allowlist，故不链**）— **本类的宿主，也是唯一入口**。
  原文两处点它：multi-port 的端口由**它的 pin 列表**决定；例子里所有搜索动作都调**它的方法**。
  raw：`02.07.04.01.36_DIGITAL_OFFSET_SEARCH_TASK.md`。**本页没读**——
  所以 **`uploadResult()` 的完整签名、`ALL_EDGES` 之外的取值、`pin()` 怎么给**，本页都没有。
- [[level-set-selector]] — **文档点名的唯一一条 `Related information`**。
  本篇 `## Related information` 一节**整节只有它一条**。
  **两个类是「同一个形状的另一半」**：它指的是 level set，本类指的是 timing set
  （**这一步是（推断）**，依据两条：① 两个类名同形，都以 `…SetSelector` 结尾；
  ② [[level-set-selector]] 那一页的语法节里，它的参数类型写的也是
  `DIGITAL_OFFSET_SEARCH::PRM_ALL`——**同一个命名空间**。
  **本页没有读它那一篇的 raw**，所以它的构造与 ID 公式**本页一个字都没有**）。
- [[waveform-set]] — **第 1 个参数在 fixed timing 那一侧指的东西**。
  原文写的是 `a waveform set (fixed timing)`。
  **⚠️ 两处口径不一致**：[[waveform-set]] 那一页把本页记成
  「**GUI 侧的「选 timing set」入口**（那页未建）」——
  **而本页是 `layer: L2` 的 C++ 类**（头文件在 `/opt/hp93000/soc/prod_com/include/MAPI/` 下）。
  **本页只记这件事，不去改那一页**（那一页的 raw 本页没读，**谁改谁要带证据**）。
- [[timing-specification]] / [[timing-spec]] — **第 1 个参数在 equation based 那一侧指的东西**
  （原文：`a timing specification (equation based timing)`）。
  **本篇没有点名这两页**，也没有给出 timing specification 是什么；
  「equation based 那一侧的容器怎么组织」在两页里，**本页没读它们**。
  **[[timing-spec]] 那一页也做了同样的保留——它写「`TimingSetSelector` 本篇没读」，
  两边都标了取材边界，谁也没声称关系。**
- [[primary-status]] — **`PRM` 那两个字面值的语义落点**。
  本类两处 `PRM` 读的都是「primary specification / primary timing set」，
  而「当前 primary 是哪个」这件事在 [[primary-status]] 那一族里。
  **本篇没点名那一页**；这条关系来自 [[timing]] 的 stage 页（**它把本页与
  `Primary.getTimingSpec()` 并列成「从 test method 里拿当前 primary 的 timing spec」**）。
- [[multiport-burst-editor]] — **（推断）名字里有 multiport 的同族页**。
  **本篇没有点名它**；第 1 个参数确实能吃 multi-port specification，
  但**「multi-port setup 长什么样、在哪配」本篇一个字都没写**。**按页名并列，不代表同物。**
- [[mapping-timing]] — **跨层对照表**。本页在那张主表里占**两行**：
  「选定 primary set（哪个 testsuite 用哪套 timing）」那一行的 L2 列，
  以及它与 [[primary-status]] 的 `timing()` 并列出现的那一格。
- [[timing-setup-commands]] — **另一页也把本页列成「timing 的 GUI 侧」**（与 [[waveform-set]] 同一处口径），
  **而本条是 L2 的 API**。**两页的记载口径一致地不对**——
  本页照实记下，**依 §1.1 与 §11，本页不去改它们的散文**（它们的 raw 本页没读）。
- [[timing-setup-tool]]（GUI 侧那个工具）— **原文一个字都没提**
  （本篇全文**没有出现任何界面名与工具名**），**所以本类与 GUI 的关系本页没有依据**。
- [[smartest-7.2.1]] — **版本页**：本篇 `## Functional changes` 唯一的落点。
- `LevelSetSelector` 之外的同族类（`DIGITAL_OFFSET_SEARCH::PRM_ALL` 那一族的数据类型）——
  原文只给了枚举的两个取值与 `PRM_ALL` 这个类型名，**同族还有哪些、定义在哪，本篇未写**。

## 版本

本文档有 `## Functional changes` 段，**只有一条**：

- **Introduced in SmarTest 7.2.1**

**这是一条正常的 `Introduced in`，不是 §11.2 ② 那个 `Introduced before` 哨兵**——
所以它**可以照字面读**：**7.2.1 之前没有这个类**。

**这条与 [[digital-offset-search-pins]] 是同一条**（那一页的 `## Functional changes` 也只有
`Introduced in SmarTest 7.2.1` 一句）——**两个类是同批引入的**。
**本篇没有别的版本条目**，所以：

- **`TimingSetSelector` 之后有没有被改过——`## Functional changes` 里没有记录。**
  **「没记录」不等于「没改过」**（§13.1 第 ⑥′）。
- **它有没有在更晚的版本上被废弃——本篇一个字都没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.md`
（TDC `141248.htm`，150 行 / 3,882 字节）。**整篇读完。**

**本页没做的：**

- **`DIGITAL_OFFSET_SEARCH_TASK`（`02.07.04.01.36`）没读**——**这是本页最大的缺口。**
  本类是**被它用的**：例子里每一个动作（`pin()` / `resourceType()` / `searchType()` /
  `start()` / `numSteps()` / `stepWidth()` / `restoreFlag()` / `execute()` / `uploadResult()`）
  **都是它的方法**。所以：
  **`uploadResult()` 的签名、第二个实参除了 `ALL_EDGES` 还能取什么、**
  **`pin()` 的 pin 列表怎么给、multi-port 的 port 是怎么从 pin 列表算出来的**——
  **本页一个字都没有。**
- **`DIGITAL_OFFSET_SEARCH_PINS`（`02.07.04.01.36.01`）没读**
  （wiki 上的 [[digital-offset-search-pins]] 页另建，**它的 raw 本页也没读**）。
  所以「两个类怎么配合」本页只有原文那一句 `It is used with DIGITAL_OFFSET_SEARCH_TASK and DIGITAL_OFFSET_SEARCH_PINS.`。
- **`LevelSetSelector`（`02.07.04.01.123`）没读**——**本篇 `## Related information` 整节只有它一条**，
  而**它是什么、怎么构造、ID 怎么算，本页一个字都没有**
  （[[level-set-selector]] 那一页本 wiki 已建，但**它的 raw 本页没读**）。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** 没有在任何机台上做过一次 offset search，也没有验证过
  `(PRM, PRM)` 是不是真的落到当前 primary、`ALL` 在两个位置上的实际效果。
  `verified: doc-only` 指的就是这件事。
- **本文档没有 `## Procedure` / `## Before you begin` 段**——
  上面「典型用法」那三步是**本页按 `## Example` 那一块代码排出来的**，
  **不是文档给的编号流程**；**例子的三行本身是原文逐字。**
- **本文档没有 `## Important points` 段、没有一条 `Note`（正文里的除外）。**
  所以「选错了会怎样」「`ALL` 的性能代价」这类问题**语料未写**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **第一句里的代码跨度被拆坏了**——`Refers` 被切成 `R` + `efers`，
> 而**反引号关在了 `R` 之后**。原文逐字是：
> The default constructor `TimingSetSelector()` is equal to `TimingSetSelector(DIGITAL_OFFSET_SEARCH::PRM, DIGITAL_OFFSET_SEARCH::PRM). R` efers to the primary timing set.
> **所以照原文渲染出来，`R` 与 `efers` 之间会多出一个空格**（读到的是「R efers」而不是「Refers」）。
> **本页在「是什么」里照原样引出，一个字没改。**
> ② **同一个参数名在本篇里有三种拼法**：
> `waveformORspecId`（构造函数清单第 5 行、参数表里那一格）、
> `waveformOrSpecId`（构造函数清单第 8 行）、
> `waveformOrSpec`（`PRM_ALL` 那一族重载与参数表另一格）。
> **`OR` 与 `Or` 不一致，`Id` 时有时无**——原文如此，**本页照录，不替它统一**。
> ③ **`specification ID's` 用了撇号**（参数表那句
> `Note that this option is only supported for waveform sets, not for specification ID's.`）——
> **复数不写撇号**。引文照原样。
> ④ **`rhs` 那一格与签名不符**：参数表写 `The name of an existing TimingSetSelector object.`，
> 而签名是 `const TimingSetSelector& rhs` / `const TimingSetSelector* rhs`——
> **取的是引用或指针，不是「名字」**。原文如此，**本页照录**。
> ⑤ **三个 `STRING` 参数的重载里，参数表只解释了 `multiportspec` 一个**
> （`const STRING& timingSelector` 与 `const STRING& waveformOrSpec, const STRING& timingSet`
> 的 `STRING` 参数在参数表里没有对应行）。**这是「表不全」，不是本页漏抄**——
> **本页按「语料未写」处理，不猜那两个字符串写什么。**
> ⑥ **`Return value` 那一格写的是 `There is no return value.`**，
> 而**本篇只列了 11 个构造函数、没有列任何成员函数**——
> **「谁没有返回值」原文没有指明**（构造函数本来就没有返回值，
> **但这一步是本页的推断，不是原文的话**）。
> ⑦ **本篇没有坏字。** 实测全文 **0 处非 ASCII 字符**（没有 `鈥` / `渭` / `碌` 那一族）。
> **但这是「本页量过的」，判据是本篇这一个文件**；§11.2 ① 那族在别的篇里大量存在。
> ⑧ **两处 wiki 页与本篇的口径不一致**（**不是 raw 的错，是本 wiki 自己的错**，
> 记在这里免得下一个人拿它去「补」错）：
> [[waveform-set]] 把本页记成「**GUI 侧的「选 timing set」入口**（那页未建）」，
> [[timing-setup-commands]] 把本页记成「timing 的 **GUI 侧**」——
> **而本页是 `layer: L2` 的 C++ 类**（头文件在 `/opt/hp93000/soc/prod_com/include/MAPI/` 下、无一句提到界面）。
> **本页只记这件事，不去改那两页**：它们的 raw 本页没读，
> **依 §1.1/§13.1，改判要带证据，不能凭本页一句话就回头改别人的散文。**

`verified: doc-only`——**本页没有在任何真实机台上做过一次 offset search**
（§11：文档里有 ≠ 这台机器上能用；尤其 `PRM` / `ALL` 在两个位置上的四种含义，
**动手前先照实机核对**）。
