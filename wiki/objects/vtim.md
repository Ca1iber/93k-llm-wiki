---
type: object
title: VTIM? - (Verify TIMing)
layer: L1
stage: timing
tags: [timing, edge-timing, period, verify, vtim, l1-command, firmware-command, multi-port, equation-based-timing]
related: [etds, pclk, vclk, vdcg, wsus, tsus, dfgp, timing, timing-setup-commands]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VTIM? - (Verify TIMing)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,479 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VTIM? {waveform_set},{timing_set},{(pinlist)}
```

returns:

```
VTIM {status}
```

### Parameters

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

multi-port_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

timing_set

 |

Specifies the timing sets to be checked. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）.

In a multi-port setup, the check is performed for those pins from pinlist that belong to the same port. If you specify a number, a timing set with this number must be present in every equation set that is associated with a port of the multi-port specification.

 |
 |

pinlist

 |

The name of the pin or pins to be checked. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.

In a multi-port setup, the pins can belong to more than one port. Only those pins are considered that belong to one of the ports of the specification.

 |
 |

status

 |

The system returns:

 |
 |

0

 |

The timing is not the same.

 |
 |

1

 |

The timing is the same.

 |

### Example

The following example illustrates the working of VTIM? in a multi-port setup. The pins S1_1 and DS0_1 belong to the same port, and S1_2 belongs to another one.

```
> ETDS? "spec_port_1_port_2",ALL,,(S1_1,DS0_1,S1_2)
< ETDS "spec_port_1_port_2",1,,"d1:0 d2:30",(S1_1,DS0_1)
< ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(S1_1)
< ETDS "spec_port_1_port_2",2,,"d1:1 d2:12",(DS0_1)
< ETDS "spec_port_1_port_2",1,,"d1:-0.67 d2:1.33 d3:9.3",(S1_2)
```

This call of `ETDS?`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） shows that the edge timings of S1_1 and DS0_1 are the same in timing set 1, but not in timing set 2 of the port to which these pins belong.

```
> PCLK? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< PCLK "spec_port_1_port_2",1,50,(S1_1)
< PCLK "spec_port_1_port_2",2,20,(S1_1)
< PCLK "spec_port_1_port_2",1,50,(DS0_1)
< PCLK "spec_port_1_port_2",2,20,(DS0_1)
< PCLK "spec_port_1_port_2",1,16.667,(S1_2)
```

This call of `PCLK?`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） shows that the periods of S1_1 and DS0_1 are the same in the two timing sets of the port.

```
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 0
```

VTIM? returns 0 because of the different timings for S1_1 and DS0_1 in timing set 2.

```
> ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(DS0_1)
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 1
```

After changing the edge timing of DS0_1 in timing set 2 to the values of S1_1 with a call of `ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`）, VTIM? returns 1 although DS0_1 has a different timing in timing set 1 and in timing set 2, and S1_2, which belongs to another port, has different values altogether.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The specified waveform set number is outside the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- The specified timing set number is outside the range allowed by the `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） command.

<!-- 报错节 end -->

## 是什么

**VTIM? 查的是「同一组 pin 之间，period 与 edge timing 是不是一样」。** 原文第一句：

> 「The VTIM? (Verify TIMing) query checks if the period and edge timing is the same for all the
> specified pins in one or all timing sets of a waveform set or equation set.」

**两个被比的东西**：`period` 与 `edge timing`。
**比的方向是 pin 对 pin**（`for all the specified pins`），**不是 timing set 对 timing set**。

### `1` 的含义比字面窄（**本页最要紧的一段**）

紧接着的一句把这个查询的语义限死了：

> 「When all timing sets are checked, a positive answer indicates that there is no timing set which
> has different edge timings or periods for any two of the specified pins; it does not imply that
> the values are identical for the same pin in different timing sets.」

**拆成两句读**：

| `timing_set` 写 `ALL` 时，回 `1` 代表 | 回 `1` **不**代表 |
|---|---|
| **不存在任何一个 timing set，在其中「任意两个被指定的 pin」的 edge timing 或 period 不同** | **同一个 pin 在不同 timing set 里的值一样** |

**参数表把 `1` 那格写成 `The timing is the same.`**——**这句短话容易读宽**，
**上面那句 `it does not imply` 才是它的边界。**

**`0` / `1` 两个值逐字**：

| 值 | 原文 |
|---|---|
| `0` | `The timing is not the same.` |
| `1` | `The timing is the same.` |

**还有一句交代方向**：

> 「The system responds with a 1 if the timing is the same and a 0 if it is not.」

### multi-port：**跨 port 不比**

> 「In a multi-port setup, the specified pins can belong to more than one port. VTIM? checks for
> every involved port if one or all timing sets associated with the respective port agree for those
> pins that belong to the port. Only pins within one port are compared with each other; it is not
> required for a positive answer that pins belonging to different ports have the same values in
> timing sets with the same number. If the check is positive for all involved ports, VTIM? returns
> 1; otherwise, it returns 0.」

**三条规则一句话**：**同一个 port 里的 pin 互相比；不同 port 的 pin 之间不比；
每个相关 port 都要过，才算 `1`。**

**参数表在 `timing_set` 那一栏又补了一条 multi-port 的硬要求**：

> 「In a multi-port setup, the check is performed for those pins from pinlist that belong to the
> same port. If you specify a number, a timing set with this number must be present in every
> equation set that is associated with a port of the multi-port specification.」

**`pinlist` 那一栏也补一条**：

> 「In a multi-port setup, the pins can belong to more than one port. Only those pins are considered
> that belong to one of the ports of the specification.」

**三段说的同一件事**：**凡是不落在「这个 specification 的某个 port」上的 pin，直接不算。**
**而第一段那句 `it is not required` 是这里唯一一条「放宽」**：**跨 port 不要求相等。**

### 定位、取值与两个上限

| 位 | 参数 | 取值 |
|---|---|---|
| 1 | `waveform_set` | `PRM`（Primary）或整数 1..上限；**上限由 [[wsus]] 定** |
| 1（equation based） | `specset_id` 或 `"multi-port_spec"` | `specset_id` 由 `100 * equation_set_no + specset_no` 算得 |
| 2 | `timing_set` | `PRM`（Primary）、`ALL`，或整数 1..上限；**上限由 [[tsus]] 定** |
| 3 | `pinlist` | pin 名（逗号分隔）、[[dfgp]] 建的 group、或 `@`（所有已配置 pin） |

**两个上限都各有一处点名、各有一条报错**（`## Errors` 的两条，见「报错条件」节）。

**equation based 那一行语法（`VTIM? {specset_id|"multi-port_spec"},{timing_set}, {(pinlist)}`）
不在本页「语法 / 参数」节里**——原因见「出处」⚠️ ①。**它和 fixed timing 那一行的差别只有第一位。**

**`multi-port_spec` 这一栏的写法，本篇和 [[vclk]] 不同**：

> 「To query a multi-port specification, enter the name of the specification.」

**只有这一句，没有 [[vclk]] 那一篇里的「只能是 default port、且没有别的 port 配置」那条限制**
（**两句都是本页的取材；本页不替两篇调和**）。

### 只对 ALL 给了精确语义

**那句 `it does not imply` 的前半句是 `When all timing sets are checked`**——
**所以精确语义只覆盖 `ALL` 那一侧。**
**给一个具体号时，「`1` 的边界在哪」本篇没有再讲一次**（**语料未写**）：
按第一句的措辞只能读到「在这个 set 里，指定的 pin 之间一样」（**推断**，依据是第一句的
`in one or all timing sets`——**原文没有单独为「一个号」这一侧写一句边界说明**）。

## 典型用法

**1. 原文的示例就是一份完整的流程**（`## Example` 一节，四步）。
它演示的**不是怎么调 VTIM?，而是 `1` 那个边界**。原文的场景设定逐字：

> 「The following example illustrates the working of VTIM? in a multi-port setup. The pins S1_1 and
> DS0_1 belong to the same port, and S1_2 belongs to another one.」

**第 1 步：先看两两之间的 edge timing**（逐字）：

```
> ETDS? "spec_port_1_port_2",ALL,,(S1_1,DS0_1,S1_2)
< ETDS "spec_port_1_port_2",1,,"d1:0 d2:30",(S1_1,DS0_1)
< ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(S1_1)
< ETDS "spec_port_1_port_2",2,,"d1:1 d2:12",(DS0_1)
< ETDS "spec_port_1_port_2",1,,"d1:-0.67 d2:1.33 d3:9.3",(S1_2)
```

> 「This call of ETDS? shows that the edge timings of S1_1 and DS0_1 are the same in timing set 1,
> but not in timing set 2 of the port to which these pins belong.」

**第 2 步：再看两两之间的 period**（逐字）：

```
> PCLK? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< PCLK "spec_port_1_port_2",1,50,(S1_1)
< PCLK "spec_port_1_port_2",2,20,(S1_1)
< PCLK "spec_port_1_port_2",1,50,(DS0_1)
< PCLK "spec_port_1_port_2",2,20,(DS0_1)
< PCLK "spec_port_1_port_2",1,16.667,(S1_2)
```

> 「This call of PCLK? shows that the periods of S1_1 and DS0_1 are the same in the two timing sets
> of the port.」

**第 3 步：这时 VTIM? 回 0**（逐字）：

```
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 0
```

> 「VTIM? returns 0 because of the different timings for S1_1 and DS0_1 in timing set 2.」

**第 4 步：把 DS0_1 在 timing set 2 的 edge timing 改成 S1_1 的值，VTIM? 就回 1**（逐字）：

```
> ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(DS0_1)
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 1
```

> 「After changing the edge timing of DS0_1 in timing set 2 to the values of S1_1 with a call of
> ETDS, VTIM? returns 1 although DS0_1 has a different timing in timing set 1 and in timing set 2,
> and S1_2, which belongs to another port, has different values altogether.」

**最后那句 `although` 就是「是什么」里 `it does not imply` 的实例**：
**`1` 到手时，DS0_1 自己跨 set 就不一致**——第 1 步的回复里，
DS0_1 在 timing set 2 是 `d1:1 d2:12`（`< ETDS "spec_port_1_port_2",2,,"d1:1 d2:12",(DS0_1)`），
在 timing set 1 却是 `d1:0 d2:30`；
**S1_2 更是一个值都不沾边**——**而结果是 `1`。**

**2. 从这份示例能读出的用法顺序**（本页按示例的四步归纳，**顺序本身是建议**）：

1. **先确定「哪些 pin 属于同一个 port」**——示例开头那句就是前提（`S1_1` 与 `DS0_1` 同 port，`S1_2` 另一个）。
2. **要分开查，就先看 edge timing（[[etds]]）与 period（[[pclk]]）的明细**，它们给出的是逐值；
   **VTIM? 给的是一个 0/1 的结论**。
3. **VTIM? 只回答「一致不一致」**，**它不会告诉你哪两个 pin 不一致、差在哪**——
   **要定位还得回 [[etds]] / [[pclk]] 的明细**（**这一条是本页的推断**，
   依据是示例里两次 VTIM? 前后都得先用 `ETDS?` / `PCLK?` 看明细；
   **原文没有一句话说「VTIM? 不回细节」**）。
4. **改到两边一致（`ETDS` 写回去）再查一次**——示例的第 4 步就是这么收尾的。

**3. 报错只有两条，都是范围**（见「报错条件」节）：waveform set 越 [[wsus]]、timing set 越 [[tsus]]。
**「timing 不一致」不在这两条里**——**它不是报错，它是这个查询要给你的答案**（**推断**，依据同上）。

**4. 上游入口**：`## Application` 一节全文就一句：

> 「Timing setup, see Timing Setup Commands.」

**本篇没有说 VTIM? 在 timing setup 流程里排第几步。**

## 和谁有关

- [[etds]] — **示例里的主角（前置/搭配）**。示例第 1 步与第 4 步都是 `ETDS?` / `ETDS`，
  **本页两次点名它**：第 1 步的说明以 `This call of ETDS? shows` 开头，
  第 4 步的说明里写着 `with a call of ETDS`。
  **`ETDS` 那一篇本页没读**——**所以「edge timing 怎么写、`d1:` 这些记号什么意思」本页一个字没有。**
- [[pclk]] — **示例里比 period 的那条（前置/搭配）**。示例第 2 步是 `PCLK?`，
  本页点名它一次（说明以 `This call of PCLK? shows` 开头）。**本页没读它**——
  **所以「`PCLK?` 的 `EXACT` / `WANT` 怎么选」本页没有。**
- [[vclk]] — **同族里最近的一条（并列）**。**本篇一次没点名它**；
  「同族」的依据是**两篇同在一章（`02.06.02.02.*`）**、都属 Verify 一族（**两篇都是本页的取材**）。
  **两条查的东西正好互补**：本篇查**现有的** period / edge timing **在 pin 之间一致不一致**；
  [[vclk]] 查**你给出的一个周期会不会触发 auto-correction**。
  **`VCLK?` 要你输入一个 `period`，本篇不要**——**这是两条命令在参数表上最大的差别**（**两篇都是本页的取材**）。
- [[wsus]] — **`waveform_set` 上限的来源（前置）**。本篇两处点名它：
  参数表的 `The maximum number is determined by WSUS, WSUS? - (Waveform Sets USed).` 与 `## Errors` 第一条。
- [[tsus]] — **`timing_set` 上限的来源（前置）**。同样两处点名（参数表 + `## Errors` 第二条）。
- [[dfgp]] — **`pinlist` 的另一种写法（并列）**：
  `This parameter can also include groups previously created by DFGP, DFGP? - (DeFine GrouP).`
- [[timing-setup-commands]] — **上游入口**。本篇 `## Application` 全文一句：
  > 「Timing setup, see Timing Setup Commands.」
- [[vdcg]] — **同族的第三条 Verify 查询（并列）**。**本篇没点名它**；
  同族的依据与 [[vclk]] 那条相同（**三篇都是本页的取材**）。
  **一条能看出三篇分工的差别**：[[vclk]] 与 [[vdcg]] 各带一段 site focus 说明，**本篇没有**（**三篇都是本页的取材**）。
- [[timing]] — **stage 页**。本页 `stage: timing` 的依据是本篇 `## Application` 那句 `Timing setup`，
  以及第一句里的 `the period and edge timing`。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 VTIM」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 VTIM」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「multi-port 下跨 port 不比这条语义是哪一版定的」在本篇里查不到**——
**而它正是这篇文档最要紧的一条规则。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.md`
  （frontmatter 的 `source_topic` 是 `98862.htm`；**5,514 字节 / 170 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **`ETDS` / `PCLK` / `WSUS` / `TSUS` / `DFGP` / `Timing Setup Commands` 六篇都没读。**
  它们都只是本篇点名的邻居：**edge timing 怎么写、period 怎么定、两个上限怎么算、
  group 怎么建、timing setup 的门在哪，本页全无。**
  示例里的 `ETDS?` / `PCLK?` 回复，**本页只按那四行字面读，没有回原文核它们的字段含义。**
- **本篇 `## Equation-based testing` 那一节的语法块不在本页「语法 / 参数」节里**——
  原因见下面 ⚠️ ①。**本页把那一行的差别写在正文里。**
- **本篇没有 site focus 那一段。** 本页读到的 [[vclk]] / [[vdcg]] 两篇各有一段逐字相同的
  site focus 说明（结果只对当前 in focus 的 site 有效），**本篇一句都没有**（**三篇都是本页的取材**）——
  **所以「多 site 下 VTIM? 报的是谁的答案」本篇答不了**（**语料未写**，**而这不是「够不着」**）。
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **这张「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上跑过 `VTIM?`**（`verified: doc-only`）。
  **所以「改完 `ETDS` 之后真会回 1 吗」本页只能保证「文档这么写」（§11）。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的两条——不是漏写。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.md`（**本页的出处**） | `98862.htm` | 5,514 | — |
| `02.06_Command_Reference/02.06.06.02.37_VTIM__-__Verify_TIMing.md` | `98862_2.htm` | 5,515 | **`diff` 报 4 行差异——全部是 frontmatter 的 `source_topic` / `source_html` 两行** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.37_VTIM__-__Verify_TIMing.md` | `98862_3.htm` | 5,769 | **差异只有 frontmatter 与篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它） |

**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有逐字读它们的正文**（§12 不越取材边界）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 一节的语法块没有进本页的「语法 / 参数」节。** 原文里 equation based 的语法另起了一段，
> 段标题逐字是
> ```
> ## Equation-based testing
> ```
> 底下的语法行逐字是
> ```
> VTIM? {specset_id|"multi-port_spec"},{timing_set}, {(pinlist)}
> ```
> **这一节没进本页的语法节**——脚本收的是 `## Syntax` / `## Parameters` / `## Example`
> 这一类段名（§4），`Equation-based testing` 不是其中之一。
> **这不是语料写错，也不是本页漏抄。**
> **② 同一组语法的空格不齐。** fixed timing 那一行是
> `VTIM? {waveform_set},{timing_set},{(pinlist)}`，
> equation based 那一行是
> `VTIM? {specset_id|"multi-port_spec"},{timing_set}, {(pinlist)}`——
> **两处逗号：第一处都不带空格，第二处在 equation based 那一行带空格。**
> **本页照原样引，不替它补齐。**
> —— 顺带记一条**与同族对比出来的**：本页读到的 [[vclk]] 那一篇的 fixed timing 语法行是
> `VCLK? {waveform_set}, {timing_set}, {period}, {(pinlist)}`（**逗号后全带空格**），
> **两篇对同一件事的排版不一样**（**两篇都是本页的取材**）。
> **③ 回复字段混在输入参数表里。** `status` 是回复里的值，却和 `waveform_set` / `timing_set`
> 这些输入参数排在同一张 `Parameters` 表里。**同族三篇都是这个写法**
> （[[vclk]] 的 `autocorrect`、[[vdcg]] 的 `dev_cyc_len` 同理，**三篇都是本页的取材**）——**本页照原样记。**
> **④ 一个 `multi-port_spec`，两种口径。** 本篇那一栏全文是
> `To query a multi-port specification, enter the name of the specification.`；
> 本页读到的 [[vclk]] 那一篇写的是
> `To enter a multi-port specification is only possible if the specification is associated with the default port and if no other ports are configured.`
> ——**一篇给限制，一篇不给**。**本页两篇并列照记，不替它们调和**（**两句都是本页的取材**）。
> **⑤ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
