---
type: constraint
title: 编辑 label 前必须先用 TSTL 把它选为编辑态
layer: L1
stage: pattern
tags: [constraint, pattern, vector-memory, sequencer, firmware]
related: [[pattern]], [[sequencer]], [[sequencer-status]]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.01.02_Creating_a_label_with_edit_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.02_APDV_-__APpenD_Vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.32_CPYV_-__CopY_Vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.55_DELI_-__DELete_Instruction.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.56_DELV_-__DELete_Vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.30_CNGV_-__CoNnect_Generate_Vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.168_NODV__-__Number_Of_Displayable_Vectors.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.130_GETA__-__GET_vector_memory_Address_information.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.322_VDCN_-__Vector_Device_Cycle_Name.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.323_VDCP__VDCP___Vector_Device_Cycle_Parameter.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 编辑 label 前必须先用 TSTL 把它选为编辑态

## 约束是什么

**要对一个 label 里的向量或 sequencer 指令做增删改，必须先用 `TSTL` 把那个 label
「选为编辑态」。** 没有选中的 label，这些命令无处可落。

文档在**总的操作说明**里把这条规矩写成了前置条件（`Creating a label with edit commands`
的 Procedure 段）：

> - For the further steps, you must activate the new label for editing with the TSTL command if you want to apply any edit command:

**这不是某一两条命令的特例**，而是**该族命令共有的前置条件**。命令页各自在自己的
`## Predependencies` 段里复述了一遍，措辞有出入：

> - The APDV command can only be issued after a label has been selected for editing with the TSTL command.

> CPYV can only be issued after the label to which the sequencer construct belongs has been activated for editing with the TSTL command.

> The DELI command can only be issued after the label to which the sequencer instructions belong has been selected for editing with the TSTL command.

**⚠️ 注意措辞不统一**：上面前两句一个说 `selected`、一个说 `activated`，
**说的是同一件事**。语料里两种说法混用（命令页段落里两种都有，报错句里两种也都有）。
**按其中任何一种去 grep，都只能捞到一半**——本页把两种都算进来了。

## 在什么条件下成立

**文档事实**：规矩横跨 **12 篇命令文档**（在语料里投放成 **24 个文件**，
每篇在两个分类树 `02.06.02.02_*` 与 `02.06.07.02_*` 下各一份，§11.2 ④）。

这 12 篇**不是整齐的**——把「规矩段」和「报错段」分别数出来，两边并不重合：

| | 篇数 | 命令 |
|---|---|---|
| 两边都写 | **10** | APDV、CNGV、CPYV、DELI、DELV、INGV、INSI、NODV、SPGV、VPAR |
| **只写规矩、不写报错** | **1** | `GETA` |
| **只写报错、不写规矩段** | **2** | `VDCN`、`VDCP` |

> **这张差集是本页最该记住的东西。** 它说明：
> **只读 `## Predependencies` 段会漏掉 VDCN / VDCP；只读 `## Errors` 段会漏掉 GETA。**
> 两段都是「文档写了的」，**但没有任何一段是完整的**。
> 发现途径就是这里：先用规矩段捞一遍、再用报错段捞一遍，**两个集合做差**，
> 差出来的三篇才是「只读一段就会漏」的那部分。

数字口径：规矩段 22 处 / 22 文件 / **11 篇**；报错段 24 处 / 24 文件 / **12 篇**。
两者都来自 `extract/rule_evidence.py`（键 `B-predep` / `B-error`），可重跑。

**范围**：文档把它表述成「any edit command」，**没有给出命令清单**。
上表 12 篇是**从语料里数出来的下界**，不是文档声明的全集。

## 违反了会怎样

**报错，而且报错文本是逐字的。** 落到 `## Errors` 段里的形态有两种措辞：

> - No label has been activated for editing.

> - No label has been selected for editing.

也有的篇目把它写成（`NODV`）：

> An error is generated if no label has been activated for editing.

**这属于「命令被拒」而不是「静默做错」**——与
[[pin-config-locked-during-test]] 那条「文档未写报错形态」形成对照。
**同是前置条件类约束，报错形态写不写、语料里并不一致。**

## 与 [[pattern]] / [[sequencer]] 的关系

- **编辑态是 label 的属性**，而 label 属于 sequencer 构造、落在向量内存里。
  这条约束管的是**「改哪一块」**，不是「能不能改」——能不能改另见
  [[pin-config-requires-sequencer-off]]（那条管 sequencer 的开关状态）。
- **选为编辑态不等于执行**。`TSTL` 只把 label 摆到「可编辑」的位置，
  真正改动的是随后那条命令。

文档给的完整最小序列（`Creating a label with edit commands`，已省略散文）：

```
APTS "test_2",MAIN,"table1"
TSTL "test_2",(@)
INGV 11,12
```

三步的顺序就是本页这条约束的实例：**先建 label（`APTS`），再选为编辑态（`TSTL`），
然后才轮到编辑命令（`INGV`）。**

> **⚠️ 推断，标出来**：`APTS` 建 label 之后**为什么还非要 `TSTL` 一次**，
> 文档没解释。上例中 `APTS` 与 `TSTL` 作用在同一个 label 上，
> 看起来「刚建好、应该是编辑态」，但文档仍要求显式选一次。
> **本页只陈述这个事实，不解释机制。**

## 一处相邻但不属于本页的限制

`APTS` 自身有个类型限制，**和本页的编辑态是两件事**，别合并：

> Note that you can use APTS only for labels of types MAIN and SVEC. For the other label types, you must proceed as described in steps 1 and 2 of Creating a label with low level commands.

**这条是「用哪个命令建 label」，本页是「建完怎么编辑」。**

## 出处

| raw | 里面的原句 |
|---|---|
| `02.06.07.01.07.01.02_Creating_a_label_with_edit_commands.md` | 总规矩句 + `APTS` 类型限制 + 上面那段序列 |
| `02.06.02.02.02_APDV_-__APpenD_Vectors.md` | Predependencies 句、Errors 句 |
| `02.06.02.02.32_CPYV_-__CopY_Vectors.md` | 措辞为 `activated` 的 Predependencies 句 |
| `02.06.02.02.55_DELI_-__DELete_Instruction.md` | 措辞为 `selected` 的 Predependencies 句、Errors 句 |
| `02.06.02.02.56_DELV_-__DELete_Vectors.md` | 措辞为 `activated` 的 Predependencies 句 |
| `02.06.02.02.30_CNGV_-__CoNnect_Generate_Vectors.md` | 同 APDV 措辞 |
| `02.06.02.02.168_NODV__-__Number_Of_Displayable_Vectors.md` | Errors 段单独成句的写法 |
| `02.06.02.02.130_GETA__-__GET_vector_memory_Address_information.md` | **有规矩、无报错**的那篇 |
| `02.06.02.02.322_VDCN_-__Vector_Device_Cycle_Name.md` | **有报错、无规矩段** |
| `02.06.02.02.323_VDCP__VDCP___Vector_Device_Cycle_Parameter.md` | **有报错、无规矩段** |

`sources:` 里只列了 `02.06.02.02_*` 这 10 个路径；
**另外 12 个文件是这些篇目在 `02.06.07.02_*` 下的重复投放**（同一篇文档，不是另一篇），
按 §10 的判据不构成第二个来源，故不重复登记。

文档事实，`verified: doc-only`。

## 这条约束怎么被发现的

**走的是 `sections.jsonl` 的 `## Predependencies` / `## Errors` 段**，
而不是全文 grep——第 ① 次用全文 grep 试过，`Error.*label` 这类模式
**把 `111032.png` 这样的图片文件名也当成了命中**，109 处里绝大多数是噪声。

> **可复用的做法**：命令族的前置条件写在 `## Predependencies`，
> 违反后果写在 `## Errors`，**两段都抽了**（`sections.jsonl` 的 `hdr` 字段）。
> 但本页证明了**两段都不完整**——必须**两边都查、再做差**。
> 这个教训与 §2.4 记的「前置词旁证」同源：
> **任何单一判据都只覆盖一部分，页面里写的「N 篇」必须说清是哪个判据数的。**
