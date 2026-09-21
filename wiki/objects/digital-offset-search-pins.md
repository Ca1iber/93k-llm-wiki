---
type: object
title: DIGITAL_OFFSET_SEARCH_PINS
layer: L2
stage: pattern
tags: [pattern, l2, test-method-api, offset-search, timing-offset, level-offset, pin, subordinate-container]
related: [pin, timing, level, dps-aux-pin-task, testmethod, pattern, smartest-7.2.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01_DIGITAL_OFFSET_SEARCH_PINS.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# DIGITAL_OFFSET_SEARCH_PINS

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **117 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01_DIGITAL_OFFSET_SEARCH_PINS.md>`。**不是转述。**
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

<!-- 语法节 end -->

## 是什么

**`DIGITAL_OFFSET_SEARCH_PINS` 是一个「没构造函数、只能从别人手里拿」的条件容器。**
它装的是**一批 pin 的 timing / level 偏移搜索条件**：

> Holds the timing/level offset search conditions for the pins specified with DIGITAL_OFFSET_SEARCH_TASK.pin().

**它的身份由两句定死**（原文相邻的两句）：

> It is a subclass of DIGITAL_OFFSET_SEARCH_TASK. You cannot directly create an object for it. An instance of this class is returned by DIGITAL_OFFSET_SEARCH_TASK.pin().

**这两句合起来是一条**：**它没有自己的入口**。`new` 不出来，只能**经父类的 `pin()` 方法拿**
——也就是说，**「哪几个 pin 要搜偏移」这件事由父类决定，本类只管那些 pin 的搜索条件**。
上面「语法 / 参数」节里那三句（`This class has no constructor.` /
`There are no parameters.` / `There is no return value.`）说的就是这件事的语法面：
**类页本身不列参数**——**参数和返回值都在它那 31 个成员函数的各自页里**。

头文件是 `/opt/hp93000/soc/prod_com/include/MAPI/DigitalOffsetSearchPins.h`。

### 本篇给出的全部信息量 = 那份 32 条的子主题清单

**这一篇没有 `## Example`、没有 `## Important points`、没有一段正文解释这些条件怎么用。**
除去上面那四句（两处定义、一句头文件、`## Functional changes` 一行），
**整篇就只剩子主题清单**。所以**这份清单就是本页能给的极限**：

**本页按名字把它们分成四组**——**依据只是名字本身，不是文档的分类**
（**原文只把它们按字母序列出来，没有分组**）：

| 组 | 成员（照清单逐字） | 名字在说什么（**本页按名字的读法**） |
|---|---|---|
| **配置** | `setConfiguration()` / `getConfiguration()` / `setExecutionContext()` / `getExecutionContext()` / `searchType()` / `stepWidth()` / `numSteps()` / `resolution()` / `resolutionHistogramSearch()` / `minPassCount()` / `minStableErrorCount()` / `errorCountLimit()` / `enableFastStop()` / `restoreFlag()` / `resourceType()` / `transitionDetection()` | 搜索怎么搜：步长、步数、分辨率、判定门槛、快速停止、是否还原 |
| **执行** | `setup()` / `start()` / `search()` / `execute()` / `remove()` | 把条件装上去、起搜、执行、撤掉 |
| **取结果** | `getOffset()` / `getStatus()` / `getLatestLBTransitionOffset()` / `getLatestRBTransitionOffset()` / `uploadOffset()` / `uploadResult()` / `uploadLatestTransition()` / `DigitalOffsetResultCopy()` / `DigitalOffsetResultReset()` / `TransitionOffsetFound()` | 偏移量、状态、最新左右边界跳变、上传、结果拷贝/复位 |
| **数据类型** | `DigitalOffsetSearchConfigDataType` | 配置用的数据类型（**它不是成员函数**，是同一份清单里的一个类型页） |

**这 31 个名字的含义，本页一个字都没有。** 每一个都有自己的子主题页
（`02.07.04.01.36.01.01` … `.32`），**那些页本页一篇没读**（见「出处」）。
**能确定的只有一件事：这个类能表达的条件面就是这 31 个名字**。

### 本篇答不了的东西（照实说，不填）

| 你可能会问 | 本篇的答复 |
|---|---|
| 偏移的**单位**是什么（时间？电压？步长怎么算） | **语料未写** |
| 条件的**取值范围 / 默认值** | **语料未写**（类页一个参数都不列） |
| `search()` 与 `execute()` 有什么区别 | **语料未写**（本页不猜） |
| 搜出来的偏移**存在哪、怎么落盘** | **语料未写**（只从名字看得见 `upload*` 一族） |
| 「timing / level」两个词各自指什么 | **语料未写**——定义句只写了 `timing/level offset search conditions` 这一个词组 |

**另外，`stage: pattern` 是骨架按 §6 填的「最近的一段」，不是「归属」。**
本篇正文**一次都没出现 pattern 这个词**（唯一的 `pin` 出现在 `…TASK.pin()` 里）。
§6 要求页面把这件事写明，所以写在这里。

## 典型用法

**本页给不出用法，这是本页最需要说清的一件事。**

- 本篇**没有** `## Procedure`、**没有** `## Before you begin`、**没有** `## Example`、
  **没有** `## Important points`——**一篇定义文档能省的全省了**。
- **用法在它那 31 个子主题页里**（`setup()` / `search()` / `start()` / `execute()` /
  `setConfiguration()` …），**那些页本页一篇没读**。

**能说的只有调用形状，而且是从两句话推出来的**：

1. **入口**：父类 `DIGITAL_OFFSET_SEARCH_TASK` 的 `pin(...)` 返回本类实例
   （`An instance of this class is returned by DIGITAL_OFFSET_SEARCH_TASK.pin().`）。
2. **之后的动作只能落在本类的成员函数上**——因为**没有别的入口**：不能 `new`、类页没有构造。
   （**这一步是推断**，依据就是上面那两句；**链式写法是不是文档推荐的写法，本篇未写。**）

**所以这一页的正确用法是当字典用**：拿到一个 pin 上的偏移搜索条件对象，
**要查某个 `....` 成员函数干什么，去它自己的子主题页**——
本页只保证「名字是这些、父类是那个、7.2.1 才有」。

## 和谁有关

**上游（唯一的上游）**：

- `DIGITAL_OFFSET_SEARCH_TASK`（**不在清单里，故不链**）— **父类，也是唯一入口**。
  本类**从它派生**、**由它的 `pin()` 返回**。文档的 `## Related information` 一节
  **整节只有它一条**——**这是本篇唯一给出的「和谁有关」**。
- `DIGITAL_OFFSET_SEARCH_TASK.pin()`（子主题，未读）— 拿实例的那一手。

**同类（形状一样，不是同一个对象）**：

- [[dps-aux-pin-task]]（**本页没读那一页**）— 本 wiki 里另一个「`xxx_TASK.pin()` 返回的
  从属数据容器、不许自己造」的对象。**形状的判据来自本页的定义句**（`You cannot directly
  create an object for it.`），**那一页本页没有依据说它也一样**，只按行名指路。

**名字对得上、关系没有依据的两条（本页不声称关系）**：

- [[pin]]（stage 页）— 本类的条件**按 pin 组织**（定义句里的 `for the pins`）。
  **本篇没有点名这一页**；「pin 怎么配置」与「pin 上怎么搜偏移」是不是前后关系，**本页没有依据**。
- [[timing]] / [[level]]（stage 页）— 本类的定义句里就有 `timing/level offset search`
  这两个词。**但本篇没有点名这两页**，**本页不据此声称它属于 timing 段或 level 段**。

**同族的其他对象**：本篇的 `## Related information` 一节**只有父类一条**，
**没有列出任何兄弟类**——所以「这一类里还有哪些别的对象」，**本篇未写**，
**本页不补**（§11：不臆造 API）。

**放进测试方法的那一侧**：本类的 `layer: L2`（骨架标）说明它**在 test method 里被调用**，
那一段是 [[testmethod]]。**这是（推断）**，依据是 `layer: L2` 这个字段本身——
**本篇正文没有一句提到 test method 或 test program**。

## 版本

**本文档有 `## Functional changes` 段，只有一条**：

- **Introduced in SmarTest 7.2.1**

**这是一条正常的 `Introduced in`，不是 §11.2 ② 那个 `Introduced before` 哨兵**——
所以它**可以照字面读**：**7.2.1 之前没有这个类**。本篇没有别的版本条目，
**也没有记录它从 7.2.1 之后被改过**——**「没记录」不等于「没改过」**（§13.1 第 ⑥′）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01_DIGITAL_OFFSET_SEARCH_PINS.md`
（TDC `140966.htm`，67 行 / 4,832 字节）。**整篇读完**——**这页之所以短，是因为它本来就短**。

**本页没做的**：

- **31 个子主题页一篇都没读**（`02.07.04.01.36.01.01` … `.32`）。
  **这是本页最大的缺口，而且是结构性的**：本页**只有名字清单**，
  每一个名字的**参数、返回值、默认值、单位**——**一个字都没有**。
- **父类 `DIGITAL_OFFSET_SEARCH_TASK`（`02.07.04.01.36`）没读**，
  所以 `pin()` 的签名、这个搜索整体怎么起、有哪些兄弟类——**本页不知道**。
- **`## Related information` 一节只有父类一条**，所以「同族还有哪些对象」本页没有依据可写。
- **一张图都没看——因为这一篇里没有图。** 实测：本篇全文 **0 处** `raw/`、
  **0 处** `.png` / `.jpg`。**所以本页没有任何来自图的结论**；
  **这不是「图够不着」，是这一篇里根本没有图**（§11.4）。
- **没有实跑。** 没有在任何机台上做过一次偏移搜索。`verified: doc-only` 指的就是这件事。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 子主题清单的排序有三处例外。** 那张清单**其余部分按字母序**，但
> `DIGITAL_OFFSET_SEARCH_PINS.DigitalOffsetResultCopy()` 与
> `DIGITAL_OFFSET_SEARCH_PINS.DigitalOffsetResultReset()` **插在 `numSteps()` 与 `remove()` 之间**，
> 而 `DigitalOffsetSearchConfigDataType` **排在整张清单的最后**。
> **两处都不合字母序**，本页**照录原始顺序、不替它重排**。
> **② 本篇没有坏字。** 实测**全文 0 处非 ASCII 字符**（没有 `渭` / `碌` / `鈥` 那一族）。
> **但这是「本页量过的」，判据是本篇这一个文件**；§11.2 ① 那族在别的篇里大量存在。
> **③ 本页未发现 `DC/DC power units`（§11.2 ⑤ 那族整词替换）。** 实测本篇 0 命中。

`verified: doc-only`
