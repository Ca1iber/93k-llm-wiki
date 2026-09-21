---
type: object
title: DFGE, DFGE? - (DeFine Group by Expressions)
layer: L1
stage: pin
tags: [dfge, firmware-command, pin-group, expression-based-group, group-expression, pin-configuration, l1-command]
related: [dfgp, pin, mapping-pin, pin-group-editor, pin-configuration-file, conf, dfpn, dfps, dfpt, udgp]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# DFGE, DFGE? - (DeFine Group by Expressions)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,817 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

|

group_type

 |

Defines the type of pins in the group. This can be:

 |
 |

I

 |

Identifies a group of device input pins.

 |
 |

O

 |

Identifies a group of device output pins.

 |
 |

IO

 |

Identifies a group of bidirectional pins.

 |
 |

DC

 |

Identifies a group of DC type pins.

 |
 |

group_expression

 |

The expression that describes the pins to be included in the group. The expression must be built up from pin or pin group names which serve as arguments for the following operators:

 |
 |

 |

+

 |

returns the union of its arguments, that is, all pins that are contained in one of its arguments.

 |
 |

 |

*

 |

returns the intersection of its arguments, that is, all pins that are contained in both of its arguments.

 |
 |

 |

-

 |

returns the difference of its arguments, that is, all pins that are contained in the first argument, but not in the second.

 |
 |

 |

You can also use parentheses to force a certain processing order.

 |
 |

pin_group

 |

The name assigned to the pin group. You can use the same name for groups of different type.

The symbol @ can be used with the DFGE? query to list all groups previously defined using the DFGP and DFGE command. If you query a non-existent group, the system returns nothing.

 |

### Example

```
> DFGP? (SCAN)
< DFGP X,(SI1,SI2,SO1,SO2),(SCAN)
> DFGP? (OUT)
< DFGP O,(O1,SO1,SO2),(OUT)
> DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGE? (SCAN_OUT)
< DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGP? (SCAN_OUT)
< DFGP O,(SO1,SO2),(SCAN_OUT)
```

This example defines a group called SCAN_OUT which contains the pins that occur both in pin groups OUT and SCAN. Note that you must use the DFGP? query to display the pins of SCAN_OUT. DFGE? returns the group definition.

The same result would be obtained with the definition

```
> DFGE O,"OUT - O1",(SCAN_OUT)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md>` 的 `## Errors`、`## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

-  More than 2400 groups are defined.
-  Another group_type than I, O, IO, or DC is used.
-  There are too many pins in the group (max. number of pins in all groups is 1843200).
-  The group definition is recursive.
-  The group expression is empty.
-  The group expression contains errors.
-  The intended group name is already being used for a pin.
-  The group name is already used by a digital pin, an analog group or non-group analog pin.

### Warnings

A warning is generated if:

- The group name is already used by a digital core group or expression-based group (in which case the old definition will be overwritten).
- The group expression contains undefined pins or groups.
- The evaluation of the group expression results in an empty group.

<!-- 报错节 end -->

## 是什么

**`DFGE` 定义「表达式型 pin 组」**——组的成员不是逐个列出来的 pin 名，
而是一个**由 `+` / `*` / `-` 和括号写成的表达式**，运行时按表达式算出成员。

> 「The DFGE (DeFine Group Expressions) command defines an expression based group.
> Pin groups can be used as though they were individual pins.
> The DFGE? query returns the group type and group expression of the named group.」

**「pin 组可以当作单个 pin 来用」**是本篇给的全部用途说明——
**原文没有再说它具体用在哪些工具、哪些命令里。**

### 组的成员不是存下来的，是算出来的

这一点由原文的例子点明：定义一个组之后，
**`DFGE?` 只还给你「组类型 + 表达式」，不还给你成员表**；
要看成员，得换成 `DFGP?` 去问：

> 「Note that you must use the DFGP? query to display the pins of SCAN_OUT.
> DFGE? returns the group definition.」

**所以 `DFGE` 的组是「规则」，`DFGP` 的组是「名单」**——
**两者共用同一个命名空间**（见 `## 典型用法` ③）。

### 组类型只有四个值

| `group_type` | 原文的说明 |
|---|---|
| `I` | `Identifies a group of device input pins.` |
| `O` | `Identifies a group of device output pins.` |
| `IO` | `Identifies a group of bidirectional pins.` |
| `DC` | `Identifies a group of DC type pins.` |

**用这四个以外的值会报错**（`## Errors` 第 2 条）。
**但原文 `## Example` 里出现了一个 `X`**——见下 ⚠️ ⑩。

## 典型用法

**① 定义：`DFGE {group_type}, {"group_expression"}, {(pin_group)}`。**
**表达式要带引号**（`"SCAN * OUT"`），**组名要带括号**（`(SCAN_OUT)`）。

**② 查询：`DFGE? {(pin_group)}`**，返回**组类型 + 表达式**。
**`@` 可以列出所有已定义的组**：

> 「The symbol @ can be used with the DFGE? query to list all groups previously defined
> using the DFGP and DFGE command. If you query a non-existent group, the system returns nothing.」

**注意 `@` 列的是 `DFGP` 与 `DFGE` 两条命令定义的组**——**是两者的并集，不只 `DFGE` 自己的。**

**③ 三个运算符的语义**（原文逐句）：

| 运算符 | 含义 |
|---|---|
| `+` | `returns the union of its arguments, that is, all pins that are contained in one of its arguments.` |
| `*` | `returns the intersection of its arguments, that is, all pins that are contained in both of its arguments.` |
| `-` | `returns the difference of its arguments, that is, all pins that are contained in the first argument, but not in the second.` |

**括号可以强制运算顺序**（`You can also use parentheses to force a certain processing order.`）。

**④ 组名可以与 pin 名冲突吗——要看冲突对象是什么。** 这是本篇最需要对着两条列表一起读的地方：

- **组名已被一个 pin 用掉 → 报错**（`## Errors` 第 7、8 条）；
- **组名已被另一个「digital core group」或「expression-based group」用掉 → 只是警告，
  且旧定义会被覆盖**（`## Warnings` 第 1 条：`in which case the old definition will be overwritten`）。

**同一个命令、同一种「名字被占了」，命运有两种**——
**取决于占住它的东西是 pin 还是另一类组。本篇没有把这条对照做成一张表**（见 ⚠️ ⑥）。

**⑤ 原文的完整例子**（定义 `SCAN_OUT` = `SCAN` 与 `OUT` 的交集）：

```
> DFGP? (SCAN)
< DFGP X,(SI1,SI2,SO1,SO2),(SCAN)
> DFGP? (OUT)
< DFGP O,(O1,SO1,SO2),(OUT)
> DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGE? (SCAN_OUT)
< DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGP? (SCAN_OUT)
< DFGP O,(SO1,SO2),(SCAN_OUT)
```

**同一批成员还可以换个写法得到**——原文给了第二种定义：

```
> DFGE O,"OUT - O1",(SCAN_OUT)
```

**⑥ 两个上限**（`## Errors`）：**组数最多 2400**，**所有组里的 pin 总数最多 1843200**。
**原文没说这两个数怎么换算**（1843200 / 2400 = 每组 768，**这个除法是本页算的，不是原文写的**）。

## 和谁有关

- [[dfgp]]（**已建**）— **姊妹命令**：`DFGP` 定义固定 pin 组（逐 pin 列名单），
  `DFGE` 定义表达式型组（给规则）。**两者的关系在本篇里只以「查询要换用 `DFGP?`」
  和 `@` 并列的形式出现**，原文没有一句把它们对照起来。
  **那一页本页没读**；**它自己那篇文档从头到尾没有提过 `DFGE`**——
  这一点是 [[dfgp]] 页实测并写下的（**引自那一页**）。
- [[pin]]（**已建**）— **本阶段的脊椎页**，它在「Pin group 与 port」一节把
  [[dfgp]] / [[dfge]] 与 [[dfpt]] / [[udgp]] 并列。**那一页本页没读。**
- [[mapping-pin]]（**已建**）— **把 `DFGP` / `DFGE` 并成一行的那张表**（这一条引自 [[dfgp]] 页的转述；**那页本页没读**）。
- [[pin-group-editor]] / [[pin-configuration-file]] — **同一件事的 GUI 侧与文件侧**。
  **本篇没有提任何 GUI、也没有提任何文件名**；这两条并列同样来自 mapping 表的转述。
- [[conf]] / [[dfpn]] / [[dfps]] / [[dfpt]] / [[udgp]] — **同族命令**（设 pin 类型与工作模式 /
  定义 pin 名 / 定义 DPS pin / 定义 port / 撤销组）。
  **五个名字本篇一个都没有出现**，这里列的是同族位置，**不是本篇写的分工。**
- `Configuration Setup Commands`（**未建**）— **原文 `## Application` 的点名对象**
  （`Pin Configuration, see Configuration Setup Commands.`）。
  **它是章节名，不在 allowlist，用反引号。**

## 版本

**一条：`Introduced before SmarTest 6.3.2`。**

**没有精确引入版本，也没有任何改动、废弃或重命名条目。**

## 出处

本页只读了 `sources:` 那一篇（`02.06.02.02.59`）。
**本篇结构完整**：`## DTCP` 式的小节命名、`## Parameters`、`## Application`、
`## Errors`（8 条）、`## Warnings`（3 条）、`## Example`、`## Functional changes` 都在。
**`## 典型用法` ③⑤ 的表格与代码块是把原文的三段列表和两个代码块照原样搬过来的**，
没有改写语义。

**本页没有做的事：**

① 没有读 [[dfgp]] 的 raw——**「`DFGP` 那篇不提 `DFGE`」这一条是转引 [[dfgp]] 页的实测结论，本页没有自己核过**；
② 没有读 [[pin]] / [[mapping-pin]] / [[pin-group-editor]] / [[pin-configuration-file]] 中任何一页；
③ **没有读 `Configuration Setup Commands` 那一章**——所以
`DFGE` 在 pin 配置流程里的位置、以及它和 `CONF` 的先后关系，本页没有；
④ **没有验证 `@` 列出的并集里，`DFGP` 与 `DFGE` 两边的组在答复里怎么区分**；
⑤ **没有验证那个 `X`**（见 ⚠️ ⑩）到底是漏写的类型、还是 `DFGP?` 的另一种返回形态。

**引用规模**：`extract/hubs-dedup.csv` 记本篇被 **5 篇**文档引用（`in_src=5`）。

### ⚠️ 语料瑕疵（逐字，本页不代改）

> ① **标题与正文的定义展开不一致。** 标题（以及文件名）是
> `DFGE, DFGE? - (DeFine Group by Expressions)`，
> 而正文第一句写 `The DFGE (DeFine Group Expressions) command`——**少了 `by`。**
> ② **`## Parameters` 整张表散架**：**没有表头行**，`|` 各自单独占一行，
> 四层嵌套（`group_type` 的四个取值、`group_expression` 的三个运算符）都靠连续空行分隔，
> **运算符那三行左边还有空单元格**。
> ③ **`DFGE?` 的返回模板与实际返回不一致。** 模板写
> `DFGE {group_type}, {("group_expression")}, {(pin_group)}`——
> **`group_expression` 外面多一层圆括号**；
> 而 `## Example` 里的真实返回是 `DFGE O,"SCAN * OUT",(SCAN_OUT)`，**没有那一层。**
> ④ **没有 `## Syntax` 段**：语法放在 `## DFGE` 与 `## DFGE?` 两个并列的二级标题底下。
> **脚本的段名表只认 `Syntax` / `Parameters` / `Example`**，所以本页「语法 / 参数」节里
> **只有参数表、没有那两行语法**（见 `extract/findings-scaffold-syntax.md`）。
> **§4 规定该节不许手改，故本页把语法写在上面 `## 典型用法` ①② 里。**
> ⑤ **`## Errors` 第 7 条与第 8 条是同一件事的两半。** 第 7 条
> `The intended group name is already being used for a pin.`；
> 第 8 条 `The group name is already used by a digital pin, an analog group or non-group analog pin.`——
> **第 8 条被第 7 条包含**，且第 8 条多了「analog」这个第 7 条没提的范围。
> ⑥ **「名字被占」的两种命运没有做成对照表**（见 `## 典型用法` ④）：
> 「被 pin 占」在 `## Errors`、「被另一类组占」在 `## Warnings`，**两节隔了十几行。**
> ⑦ **`@` 的说明放在 `DFGE` 的页上，却讲的是 `DFGP` 与 `DFGE` 两条命令的并集。**
> ⑧ **`If you query a non-existent group, the system returns nothing.`**——
> **`returns nothing` 没有定义**：是空串、还是根本不应答、还是别的，原文没说。
> ⑨ **`## Application` 是一句指路**（`Pin Configuration, see Configuration Setup Commands.`），
> **没有动词句，也没有说 `DFGE` 落在流程的哪一步。**
> ⑩ **例子里出现了参数表没写的组类型 `X`**：`## Example` 第一行返回
> `DFGP X,(SI1,SI2,SO1,SO2),(SCAN)`，而 `## Parameters` 说 `group_type` 只能是
> `I` / `O` / `IO` / `DC`，`## Errors` 第 2 条还说用别的值会报错。
> **`X` 与这两处都对不上，原文没有解释它。**
> ⑪ **两个上限（2400 组 / 1843200 pin）之间没有给出换算关系**，
> 也没说这两个数是不是 `DFGP` 与 `DFGE` 共享的。
> ⑫ **没有 `## Related information` 一节**：与同族命令的关系全靠正文里那几处链接承载。
> ⑬ **`## Example` 先用 `DFGP?` 查两个组，但没有交代这两个组是哪来的**——
> 例子的前两行 `DFGP? (SCAN)` / `DFGP? (OUT)` 读起来像先决条件，**原文没说是。**
