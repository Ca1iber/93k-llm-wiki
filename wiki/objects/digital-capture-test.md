---
type: object
title: DIGITAL_CAPTURE_TEST
layer: L2
stage: testmethod
tags: [testmethod, l2, test-method-api, digital-capture, sequencer, execution-context, result-area, run, flush]
related: [run, execution-context, execution-context-requires-firmware-definition, flush, pattern, pattern-editor, mapping-pattern, testmethod, sequencer, primary-status, smartest-6.3.2, smartest-6.5.0]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.35_DIGITAL_CAPTURE_TEST.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# DIGITAL_CAPTURE_TEST

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,759 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.35_DIGITAL_CAPTURE_TEST.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void DIGITAL_CAPTURE_TEST();
void DIGITAL_CAPTURE_TEST(const TM::WAIT_ACTION& wait_action);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout, const TM::WAIT_ACTION& wait_action);
void DIGITAL_CAPTURE_TEST(const STRING & resultAreaId);
void DIGITAL_CAPTURE_TEST(const STRING & resultAreaId, const STRING& context);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout,
                          const STRING & resultAreaId);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout,
                          const STRING & resultAreaId, const STRING& context);
void DIGITAL_CAPTURE_TEST(const TM::WAIT_ACTION& wait_action,
                          const STRING & resultAreaId);
void DIGITAL_CAPTURE_TEST(const TM::WAIT_ACTION& wait_action,
                          const STRING & resultAreaId, const STRING& context);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout, const TM::WAIT_ACTION& wait_action,
                          const STRING & resultAreaId);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout, const TM::WAIT_ACTION& wait_action,
                          const STRING & resultAreaId, const STRING& context);
```

Parameters
 |

I/O

 |

Parameter

 |

Description/Range

 |
 |

I

 |

timeout

 |

Timeout time of the measurement (test).

Unit: s

If you omit this parameter, the default timeout is 360000 s.

 |
 |

I

 |

wait_action

 |

This parameter allows you to select which sequencer's completion the API waits for, from the following hardware categories that are represented by the constant variables. It is also valid for combination of them by using "|" (use bitwise OR to select multiple ones). For example, if you make this API waited until AWGs and digitizers/samplers complete the current sequencer programs, specify TM::WAIT_AWG|TM::WAIT_DGT to this parameter.

- TM::WAIT_ALL:

waits until all used digital channels, AWGs, digitizers/samplers, and TIAs complete their tasks.

- TM::WAIT_DIGITAL (default):

waits until all used digital channels complete the current sequencer program.

- TM::WAIT_AWG:

waits until all used AWGs complete the current sequencer programs.

- TM::WAIT_DGT:

waits until all used digitizers and samplers complete the current sequencer programs.

- TM::WAIT_TIA:

waits until all used TIAs complete the current measurements.

 |
 |

I

 |

resultAreaId

 |

The name of a result retention area for background processing. See `RESULT_AREA_CONFIG`（raw: `02.07.04.01.190_RESULT_AREA_CONFIG_SET.md`） API.

For sequencer context executions without using a result area use an empty string for the resultAreaId, and specify both this and the context parameter. See also example below.

 |
 |

I

 |

context

 |

Name of an execution context. The ports of the context must be included in the current start label (which must be a multiport burst). For more information on execution contexts see `Using execution contexts`（raw: `../02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） .

The context must have been defined on the firmware level (with the SQEC command), or as a SEQUENCER_CONTEXT_ITEM object. In the latter case this object must have been included in a SEQUENCER_CONTEXT object, and must also have been activated on the firmware level with the apply() function of this SEQUENCER_CONTEXT object. If the context has been defined as a SEQUENCER_CONTEXT_ITEM object, you must use the name specified for its name parameter.

 |

### Example

### Sequencer context execution without result area

```
string defaultResultAreaId = "";
string contextName = "JTAG_PORT_context"
DIGITAL_CAPTURE_TEST(defaultResultAreaId, contextName);
```

Using an empty string for the resultAreaId, and specify both this and the context parameter allows sequencer context executions without using a result area.

The DIGITAL_CAPTURE_TEST API starts the test.

<!-- 语法节 end -->

## 是什么

**`DIGITAL_CAPTURE_TEST` 是「带 digital capturing 的测试」唯一合法的执行入口。**

> The DIGITAL_CAPTURE_TEST API executes a test which contains digital capturing.

> This API starts the digital sequencer and waits for its completion.

**它是阻塞式的**：起定序器，**等它跑完**才返回。头文件是
`/opt/hp93000/soc/prod_com/include/MAPI/Execute.h`——**注意入口在 `Execute.h` 里，
和 `EXECUTE_TEST` / `START_TEST` 是一族**，这正是下面那条规则存在的原因。

### 一条「只能用它、也只能用它」的规则

原文把两个方向都写死了，**这是一个双向的硬边界，不是建议**：

| 测试里有没有 digital capturing | 用 `EXECUTE_TEST` / `START_TEST` | 用 `DIGITAL_CAPTURE_TEST` |
|---|---|---|
| **有** | **跑不了**（`the test cannot be done`） | **正确入口** |
| **没有** | 正常 | **必然 FAIL**（`the execution always results in FAIL`） |

> If you attempt to execute a test containing digital capturing with the EXECUTE_TEST or START_TEST API, the test cannot be done. On the other hand, if you attempt to execute a test in which digital capturing is not used with the DIGITAL_CAPTURE_TEST API, the execution always results in FAIL.

**所以这个 API 不是「EXECUTE_TEST 的超集」**：它**按测试内容分工**，
用错了**两边都报错**——一边是跑不了，一边是**永远 FAIL**。

### 它在起测前会自己刷一遍 setup（调 `FLUSH`）

> Before starting test execution, the DIGITAL_CAPTURE_TEST API executes the FLUSH API internally to reflect the changes specified by the following APIs to the hardware of setup data:

七个来源（原文的 bullet，**照抄名字**）：`ANALOG`、`ANALOG_STATUS`、`PRIMARY_STATUS`、
`TIMING_SPEC` / `LEVEL_SPEC` / `SPECIFICATION`、`ROUTING_STATUS`。
**这条的直接后果：用这个 API 起测，你不需要自己先调 `[[flush]]`**——
**它已经调过了**（`FLUSH` 那篇的原文在 `02.07.04.01.69`，**本页没读**）。

**但有一条例外条件，只对模拟模块成立**：

> In order for the DIGITAL_CAPTURE_TEST API (or an API that internally executes the FLUSH API) to reflect the changes that are specified by ROUTING_STATUS/ANALOG_STATUS to an analog module hardware, the sequencers in all analog modules must be halted.

**即：内部 `FLUSH` 能替你推 `ROUTING_STATUS` / `ANALOG_STATUS` 到模拟模块，
前提是那些模块上的定序器已经停住。** 这一条是**条件**，不是「总是成立」。

### 它**不等**谁：三类硬件的等待边界

| 不等的对象 | 文档给的补救 | 原文关键句（逐字） |
|---|---|---|
| **AWG 的输出** | 若 AWG 用了无限循环（`LOOPI` / `RPTI`），**用 `ABORT_TEST` 停** | `This API does not wait until the AWG finishes the output.` |
| **Digitizer / Sampler 与 TIA 的测量** | **在这之后再调 `WAIT_TEST_DONE`** | `This API does not wait until the Digitizers/Samplers and TIAs finish the measurement.` |
| **数字定序器** | **它等**（这就是它的本职） | `This API starts the digital sequencer and waits for its completion.` |

**注意 `wait_action` 参数与这张表的关系**：`TM::WAIT_DGT` / `TM::WAIT_TIA` 那几个常量
**是给「等哪些定序器完成」用的**（脚本在上面逐字抄了这五个取值和各自的等待范围，
**本页不重抄**）；而上面那张表说的是**这个 API 出厂不等 AWG / DGT / TIA 的收尾**——
**两件事是两回事**：一个管「等谁跑完程序」，一个管「收尾谁去等」。
`TM::WAIT_DIGITAL` 是**默认值**。

### 两个「附加参数」把它接进了另外两块机制

**① `resultAreaId` —— 接后台结果暂存区。**
给定名字时指向一个结果保留区（原文点名 `RESULT_AREA_CONFIG` API，`02.07.04.01.190`，**本页没读**）。
**空字符串 + `context` 一起给，就表示「不用结果区」**：

> Using an empty string for the resultAreaId, and specify both this and the context parameter allows sequencer context executions without using a result area.

**② `context` —— 接 execution context。**
两条硬条件同时成立才能用：端口必须属于当前 start label（**而且那个 start label 必须是
multiport burst**），并且**上下文必须先在固件级定义过**：

> The context must have been defined on the firmware level (with the SQEC command), or as a SEQUENCER_CONTEXT_ITEM object.

**这一条和本 wiki 的约束页 [[execution-context-requires-firmware-definition]] 是同一件事的两面**
（那页从「不许随用随起名字」那一侧写，本页从「这个 API 收 `context` 参数」这一侧写）。
**`SQEC` / `SEQUENCER_CONTEXT` / `SEQUENCER_CONTEXT_ITEM` 三篇原文本页没读。**

### 两个数

- **`timeout` 省略时默认 `360000 s`**（原文：`If you omit this parameter, the default timeout is 360000 s.`）
  ——**约 100 小时（本页算的），实践上等于「不等超时」**。
- **`wait_action` 可以按位或组合**：`specify TM::WAIT_AWG|TM::WAIT_DGT to this parameter`。

### 一个必须分清的同族：`NB_` 那两个

> The NB_DIGITAL_CAPTURE_START API waits until the digital sequencer has completed before returning, while the NB_DIGITAL_CAPTURE_START(); and NB_DIGITAL_CAPTURE_END(timeout); do not.

**这一句本身是坏的**（见「出处」⚠️①）：它**把 `NB_DIGITAL_CAPTURE_START` 同时说成
「等」和「不等」。**照它现在的字面读，无法确定谁等谁不等**——
**本页不替它裁定**，只记下这里有一条**阻塞/非阻塞之分**。

## 典型用法

**把这一页当「起测入口的选择题」用**：

1. **先看测试内容**：这次要跑的功能测试里**有没有 digital capturing**？
   有 → **必须** `DIGITAL_CAPTURE_TEST`；没有 → **必须** `EXECUTE_TEST` / `START_TEST`。
2. **要并行（不阻塞）** → 走 `NB_DIGITAL_CAPTURE_START` / `NB_DIGITAL_CAPTURE_END` 那一对
   （**阻塞语义那一句是坏的，见上**）。
3. **起测后还要等 DGT / Sampler / TIA 收尾** → 在它后面补一个 `WAIT_TEST_DONE`。
4. **AWG 用了无限循环** → 用 `ABORT_TEST` 停。
5. **要在 execution context 上跑、又不想开结果区** → `resultAreaId` 传空字符串、`context` 给上下文名。

**本篇唯一的例子就是第 5 步**（`### Sequencer context execution without result area`，
代码已由脚本逐字抄在「语法 / 参数」节里，**本页不重抄**）。它的形状是两行：

```
string defaultResultAreaId = "";
string contextName = "JTAG_PORT_context"
DIGITAL_CAPTURE_TEST(defaultResultAreaId, contextName);
```

**两件要留意的事**：① `contextName` 那一行**行尾没有分号**（见「出处」⚠️③）；
② 原文在这段后面只补了两句——一句解释「空 resultAreaId + context = 不用结果区」，
一句是 `The DIGITAL_CAPTURE_TEST API starts the test.`，**没有别的用法说明**。

**它在 pattern 那一段的位置（与 [[mapping-pattern]] 对齐）**：那张三层对照表的
「digital capture pattern」一行里，**GUI 侧是 [[pattern-editor]]**（Digital Capture setup）、
**L2 侧写的就是本页**（`DIGITAL_CAPTURE_TEST` 与 `VECTOR`，`02.07.04.01.35` / `.269`）；
**那一行的 L1 格是 `?`、L3 格是 `—`**——**即：抓取这件事在 GUI 与 L2 之间有桥，
在固件命令层与外部接口层都没有桥**。本页**只负责 L2 那一格**。

## 和谁有关

**执行入口那一族（同层、互斥）**：

- [[run]] — `stage: run` 的那条**执行与调试**主轴。本页是它的一个**专用入口**：
  同样是「起测」，但**只受理带 digital capturing 的测试**。两边的分工由上面那条
  「只能用它、也只能用它」的规则划死。
- [[flush]] — **文档事实**：本 API **内部会调 `FLUSH`**，所以用本页起测时不必自己先刷
  （`02.07.04.01.69_FLUSH.md` 原文**本页没读**，只读了本篇点名它的那两句）。

**它接进来的两块机制**：

- [[execution-context]] — `context` 参数指向的执行上下文（**该页在 `stage: run`**）。
- [[execution-context-requires-firmware-definition]] — 上一条的**前置约束页**：
  上下文必须先在固件级定义过。**本页那一句（`with the SQEC command`）就是这条约束的文档依据之一。**
- [[primary-status]] — **文档事实**：内部 `FLUSH` 的七个来源里就有 `PRIMARY_STATUS`；
  而 `context` 那条又要求「端口属于当前 start label」，**start label 是 [[primary-status]] 管的**。
  **「start label 由谁指定」这一层本页没有展开**（本篇没写）。

**pattern 那一侧**：

- [[pattern-editor]] / [[mapping-pattern]] — 见「典型用法」最后一段。
  本页**只管 L2 那一格**；GUI 侧怎么建 Digital Capture setup、L1 侧为什么是 `?`，
  **在 [[mapping-pattern]] 与 [[pattern-editor]] 里**，本页不复述。
- [[pattern]] — **本页没读那一页**；关系只到「这是一个 pattern 里的抓取动作」这个粒度，
  **本篇没有点名它**。

**同名但不同的东西（别混）**：

- `SMC_DIGITAL_CAPTURE_TEST`（`02.07.04.01.231.08`，**本页没读**）——**SMC 那一族的包装**，
  **不是本页这个 API**。**两者的差别本篇一个字没写**，本页不推。
- `NB_DIGITAL_CAPTURE_START` / `NB_DIGITAL_CAPTURE_END` / `WAIT_TEST_DONE` / `ABORT_TEST` /
  `EXECUTE_TEST` / `START_TEST`——**这几条都不在 `extract/prose-allowlist.txt` 里，故一律反引号**。

**放进测试方法的那一侧**：[[testmethod]]——本类的 `layer: L2` 说的就是这件事。

## 版本

**本文档有 `## Functional changes` 段，两条**：

- **Introduced before SmarTest 6.3.2** —— **这是 §11.2 ② 那个哨兵值**，
  意思是「**在本文档集覆盖范围开始之前就已经有了**」。
  **照字面读会得出「6.3.2 新增」这条假信息**，**本页照原样记、不加解释性日期。**
- **SmarTest 6.5.0: New parameter resultAreaId.** —— **这一条是正常的版本事实**：
  **`resultAreaId` 是 6.5.0 才有的参数**。
  **本 wiki 面向 SmarTest 7.10.3，所以这个参数在目标版本上是有的**；
  **反过来说，6.5.0 之前的程序里不该出现它**。

**两条合起来读，本篇的版本信息就是这一件事**：API 本身早于 6.3.2，**`resultAreaId` 是 6.5.0 加的**。
**`context` 参数是哪一版加的，本篇没有条目——本页不知道。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.35_DIGITAL_CAPTURE_TEST.md`
（TDC `28758.htm`，174 行 / 6,349 字节）。**整篇读完**。

**本页没做的**：

- **`FLUSH`（`02.07.04.01.69`）原文没读。** 本页只能说「它被内部调用了」；
  **`FLUSH` 到底推什么、推不到哪里，本页一个字没有**（`[[flush]]` 那页是另一批建的）。
- **`RESULT_AREA_CONFIG`（`02.07.04.01.190`）原文没读**，所以结果保留区的机制本页没有。
- **`Using execution contexts`（`02.06.07.01.08.05.03.02.03`）原文没读**——
  正文把「execution context 是什么」推给了它，**那一段本页没有**。
- **`SEQUENCER_CONTEXT` / `SEQUENCER_CONTEXT_ITEM` / `SQEC` 的原文没读**，
  所以「怎么先在固件级定义一个 context」本页答不了。
- **`NB_DIGITAL_CAPTURE_START`（`.135`）/ `NB_DIGITAL_CAPTURE_END`（`.134`）原文没读**，
  所以那一句自相矛盾的话**本页只能记下、不能裁定**。
- **`WAIT_TEST_DONE`、`ABORT_TEST`、`EXECUTE_TEST`、`START_TEST`、`VECTOR`（`.269`）原文没读**，
  全部只在本篇的链接里出现过。
- **一张图都没看——因为这一篇里没有图。** 实测：本篇全文 **0 处** `raw/`、
  **0 处** `.png` / `.jpg`。**所以本页没有任何来自图的结论**；
  **这不是「图够不着」，是这一篇里根本没有图**（§11.4）。
- **没有实跑。** 没有在任何机台上跑过这个 API、没有建过 execution context、
  没有触发过「用错入口必 FAIL」那条规则。`verified: doc-only` 指的就是这件事。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 「`NB_` 那一句」自相矛盾，逐字是**：
> `The NB_DIGITAL_CAPTURE_START API waits until the digital sequencer has completed before returning, while the NB_DIGITAL_CAPTURE_START(); and NB_DIGITAL_CAPTURE_END(timeout); do not.`
> —— **同一个 `NB_DIGITAL_CAPTURE_START` 前半句说「等」、后半句说「不等」**。
> **本页照录，不裁定哪个是笔误。**
> **② 例子里少一个分号**：`string contextName = "JTAG_PORT_context"` **行尾没有 `;`**
> （同段上一行的 `string defaultResultAreaId = "";` 是有的）。**本页照录。**
> **③ 参数说明里有一处结构读不通，逐字是**：
> `For example, if you make this API waited until AWGs and digitizers/samplers complete the current sequencer programs, specify TM::WAIT_AWG|TM::WAIT_DGT to this parameter.`
> —— **`make this API waited until …` 这个结构不成立**（本页**只引不改**）。
> **④ 本页未发现编码坏字，未发现 `DC/DC power units`。** 实测本篇 **0 处非 ASCII 字符**、
> **0 处** `DC/DC power units`。**但这是「本页量过的」，不是「语料干净」**（§13.1 第 ⑥′）。

`verified: doc-only`
