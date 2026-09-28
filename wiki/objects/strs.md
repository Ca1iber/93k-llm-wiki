---
type: object
title: STRS? - (Spec TRansition Search)
layer: L1
stage: timing
tags: [strs, l1-command, firmware-command, query-command, spec-search, spec-variable, transition-search, equation-based, multi-port, pin-scale]
related: [spec-search, spec-set, spec-variable, spec-value, execution-context, dfgp, shmoo-tool, test, timing, level, pin]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# STRS? - (Spec TRansition Search)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,714 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
STRS? ["exec_context",] [start], [stop], {mode}, [(pinlist)], {spec_type}, {"spec_name[@port[@UNCHANGED]]"}, [stepwidth], {resolution}
```

returns:

```
STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]
```

### Parameters

|

exec_context

 |

An execution context. For more information on execution contexts see `Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） .

 |
 |

start

 |

Double float with up to 5 digits after the decimal point defining the value of spec_name at the start of the search. The maximum valid range is -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values defined with the spec. If the parameter is omitted, the minimum value as defined in the spec set will be used.

The start value can be greater than the stop value. In this case the search will be in the negative direction.

 |
 |

stop

 |

Double float with up to 5 digits after the decimal point defining the value of spec_name where you want the search to end. The maximum valid range is -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values defined with the spec. If the parameter is omitted, the maximum value as defined in the spec set will be used.

The stop value can be smaller than the start value. In this case the search will be in the negative direction.

 |
 |

mode

 |

Search mode. Use:

L to specify a linear search,

LB to specify linear/binary search,

B to specify a binary search.

 |
 |

pinlist

 |

The name of the pin or pins for which the value of the spec variable is to be modified. This parameter may also include groups previously created by the `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） command. If more than one pin is to be included, the names must be separated with a comma.

The @ character indicates all pins. This is the default.

 |
 |

spec_type

 |

Which specification type to use. Use :

LEV to specify levels, or

TIM to specify timing.

 |
 |

spec_name

 |

A string of up to 64 alphanumeric characters (upper or lower case) enclosed in double quotes.

If you use the option @port`[`@UNCHANGED`]`, (see the port parameter), you must include this extension in the double quotes, too.

 |
 |

port

 |

In a multi-port setup, you can add a port name to the spec variable. This will have the effect that the value of the variable will be modified only for pins belonging to this port. This holds even if the variable has global scope for this port in the timing specification.

If you specify the spec variable without a port in a multi-port setup, its value will only be modified for a pin whose port has the spec variable set to global scope.

For more information on the scope of a variable see `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）.

Note that if a port that is specified with the name of the variable it is this port on which the value of the variable will be modified. The setup pins have no influence on this.

On a Pin Scale system, the specification of a port will have an additional effect:

If spec_name is used in the definition of the port period, this port will be temporarily used as the primary port. For more information see `Modifying the period for a search or shmoo in a multi-port setup`（raw: `02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）.

This switch can be suppressed by adding @UNCHANGED to the port name.

 |
 |

stepwidth

 |

The search step width in the unit specified with the corresponding spec. This is optional if mode is B.

 |
 |

resolution

 |

The smallest step size to be used in the search. Especially useful in a binary search of a range of floating point numbers, where the number of values between start and stop is infinite. The unit must be the same as defined with the spec.

 |
 |

res_spec

 |

LT (less than)

LE (less than or equal to)

EQ (equal to)

GE (greater than or equal to)

GT (greater than).

 |
 |

pass_meas_value

 |

A double float defining the passed measured value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647.

This parameter contains the last (in a PASS/FAIL transition) or the first (in a FAIL/PASS transition) value where the test passed.

 |
 |

fail_meas_value

 |

A double float defining the failed measured value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647.

This parameter contains the first (in a PASS/FAIL transition) or the last (in a FAIL/PASS transition) value where the test failed.

 |

### Example

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the primary sets used are not equation-based.

<!-- 报错节 end -->

## 是什么

**`STRS?` 是「让一个 functional test 反复跑、每跑一次改一点 spec 变量的值，去找 PASS↔FAIL 翻转点」的那条查询命令。**
原文第一段把机制一次说完：

> 「The STRS? query repeats a functional test in a loop. With each test execution, the value of a (timing or level) spec variable is systematically modified within a specified interval for all those pins that are specified in the query and depend on the spec variable in question in their (timing or level) setup. The goal of the search is to identify that value of the variable where the test result changes from PASS to FAIL or from FAIL to PASS.」

拆成四件事：

| # | 机制 | 原文 |
|---|---|---|
| ① | **反复跑一个 functional test**（循环） | `repeats a functional test in a loop` |
| ② | **每次执行，在指定区间内系统地改一个 spec 变量的值** | `the value of a (timing or level) spec variable is systematically modified within a specified interval` |
| ③ | **只改「在 query 里点了名、而且它自己的 setup 里用到这个变量」的 pin** | `for all those pins that are specified in the query and depend on the spec variable in question in their (timing or level) setup` |
| ④ | **目标是那个翻转点** | `identify that value of the variable where the test result changes from PASS to FAIL or from FAIL to PASS` |

**第 ③ 条是最容易漏读的一句**：**pin 必须在自己的 timing / level setup 里用到这个变量，才会被改。**
**没用到的 pin 会怎样，原文没说**（**语料未写**）。

### 找到 / 没找到，回的东西**不一样**（这一段最容易读错）

> 「If such a transition is found within the search interval, STRS? returns the last value where the test result is still the same as for the start value, and the first value where it has changed. If it does not change, then only one value is returned, namely the stop value.」

| 情况 | 回几个值 | 是哪几个 |
|---|---|---|
| **区间内有翻转** | **两个** | ①**最后一个结果仍与起始值相同**的值；②**第一个结果变了**的值 |
| **区间内没翻转** | **一个** | **`stop` 那个值** |

> **「没翻转 → 回 `stop`」是个陷阱**：**回了值不等于找到了边界。**
> 只回一个值时，你看不出「是搜到头了」还是「压根没翻」。

### 起止值的默认值来自 spec set，而且**填全了会更快**

> 「The default values for start and stop are the minimum and maximum values that are defined for the spec variable in the primary spec set. Defining such maximum and minimum values speeds up the search.」

**两件事**：① 不写 `start` / `stop` → 用 **primary spec set 里为这个变量定义的 min / max**；
② **在 spec set 里把 max / min 定义好，能让搜索变快**（这是原文自己给的一条性能提示）。

> **一处口径要记**：这句说的是 **spec set** 里定义的 min / max；
> 而 Parameters 一节讲 `start` 的取值范围时写的是
> `this may be limited by the maximum and minimum values defined with the spec`——**用的是 `spec`**。
> **两个词在本篇里都出现，本页照记，不替它统一**（§11.5）。

### 三种搜索模式

| `mode` | 原文 |
|---|---|
| `L` | `L to specify a linear search,` |
| `LB` | `LB to specify linear/binary search,` |
| `B` | `B to specify a binary search.` |

两格的配套条件：

- **`stepwidth`**：`The search step width in the unit specified with the corresponding spec. This is optional if mode is B.`
  —— **`B` 模式下 `stepwidth` 可以省**。
- **`resolution`**：`The smallest step size to be used in the search. Especially useful in a binary search of a range of floating point numbers, where the number of values between start and stop is infinite. The unit must be the same as defined with the spec.`
  —— **它是「最小步长」**，原文明说它**在浮点区间上做二分搜索时特别有用**
  （理由是「start 与 stop 之间的值的个数是无限的」）。

### 返回式：`res_spec` 五个取值 + 两个测量值

```
STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]
```

`res_spec` 是**五个关系符之一**：`LT (less than)` / `LE (less than or equal to)` /
`EQ (equal to)` / `GE (greater than or equal to)` / `GT (greater than).`

两个测量值的定义**互为镜像，而且都跟着翻转方向变**：

| 参数 | PASS/FAIL 翻转时 | FAIL/PASS 翻转时 |
|---|---|---|
| `pass_meas_value` | **最后一个**通过的值 | **第一个**通过的值 |
| `fail_meas_value` | **第一个**失败的值 | **最后一个**失败的值 |

逐字：

> 「This parameter contains the last (in a PASS/FAIL transition) or the first (in a FAIL/PASS transition) value where the test passed.」

> 「This parameter contains the first (in a PASS/FAIL transition) or the last (in a FAIL/PASS transition) value where the test failed.」

> **`res_spec` 与这两个测量值之间是什么关系，原文没有解释**——
> 它只列了五个关系符的名字，**没有一句说 `GE` 这种结果意味着什么**（**语料未写**）。

### 硬前提：primary sets 必须是 equation-based

报错条件那一节**只有一条**：

> 「An error is generated if the primary sets used are not equation-based.」

**这一条也解释了上面「默认范围从 spec set 来」为什么成立**——
按 equation-based 的读法，spec 的 min / max 才是一个已知的区间。

### `pinlist`：三种写法，`@` 是默认

> 「The name of the pin or pins for which the value of the spec variable is to be modified. This parameter may also include groups previously created by the DFGP command. If more than one pin is to be included, the names must be separated with a comma.」

> 「The @ character indicates all pins. This is the default.」

| 写法 | 含义 |
|---|---|
| `(pin1,pin2)` | **点名**（逗号分隔） |
| `(group)` | **`DFGP` 建的组** |
| `@` | **所有 pin**，**这是默认** |

### `spec_name` 与它的引号规则

> 「A string of up to 64 alphanumeric characters (upper or lower case) enclosed in double quotes.」

**两条格式要求**：**名字最长 64 个字母数字（大小写都行）、必须加双引号**；
**如果还带 `@port` / `@UNCHANGED`，那一段也要写在双引号里面**
（语法式里就是 `{"spec_name[@port[@UNCHANGED]]"}`）。
> 那一句里出现的反引号是**上游的 `<code>` 标记**被转成了反引号，**不是本页写错**——见「出处」⚠️①。

### `port` 那一格：多口 setup 里最绕的一段

原文在这一格写了**四层**意思：

| # | 原文 | 意思 |
|---|---|---|
| 1 | `In a multi-port setup, you can add a port name to the spec variable. This will have the effect that the value of the variable will be modified only for pins belonging to this port. This holds even if the variable has global scope for this port in the timing specification.` | **带 port = 只改属于这个 port 的 pin**；**即使该变量在这个 port 上是 global scope 也一样** |
| 2 | `If you specify the spec variable without a port in a multi-port setup, its value will only be modified for a pin whose port has the spec variable set to global scope.` | **不带 port = 只改「那个 port 上该变量是 global scope」的 pin** |
| 3 | `Note that if a port that is specified with the name of the variable it is this port on which the value of the variable will be modified. The setup pins have no influence on this.` | **认的是变量名里写的那个 port，setup pin 说了不算** |
| 4 | `On a Pin Scale system, the specification of a port will have an additional effect:` … `If spec_name is used in the definition of the port period, this port will be temporarily used as the primary port.` … `This switch can be suppressed by adding @UNCHANGED to the port name.` | **Pin Scale 上还有副作用**：临时改 primary port，用 `@UNCHANGED` 抑制 |

**第 1 条与第 2 条互为反面**，合起来是一条完整判据：
**带 port → 只改该 port 的 pin；不带 port → 只改 global scope 的那些。**

**第 3 条的后半句 `The setup pins have no influence on this.` 是这一格最容易读漏的一句。**

### Pin Scale 上的副作用：临时改 primary port，**搜完会复位**

原文专门为这件事起了一节：

> 「The STRS? query can temporarily change the primary port; see the description of the port parameter. If it does it resets the primary port after the search is complete.」

三件事：① **会临时改**；② **触发条件是 `spec_name` 用在了 port period 的定义里**（见上表第 4 条）；
③ **搜索结束会把它复位**。**要它别改，就在 port 名后加 `@UNCHANGED`。**
详细说明原文指向 `Modifying the period for a search or shmoo in a multi-port setup`（**本页没读**）。

## 典型用法

**先说范围**：本篇**没有 `## Procedure`、没有 `## Before you begin`**。
`## Application` 一节**全文只有一句**：

> 「Spec search testflow.」

**就这么一句**——所以「`STRS?` 在流程里排第几步」本篇没写（**语料未写**）。
`[[spec-search]]` 是同一件事的 **API 侧**页（`SPEC_SEARCH`，L2），**本页没读它**。

**1. 先确认前提**：**primary sets 必须是 equation-based**（报错条件只有这一条）。

**2. 选变量与 pin**：

| 格 | 写什么 |
|---|---|
| `spec_type` | `LEV`（levels）或 `TIM`（timing） |
| `spec_name` | 双引号里的变量名，**最长 64 个字母数字**；带 port 扩展就一起写进引号 |
| `pinlist` | 点名 / `DFGP` 组 / `@`（默认）。**只有 setup 里用到这个变量的 pin 才会被改** |

**3. 给区间**：不写 `start` / `stop` → 用 **primary spec set 的 min / max**；**写了更快**。
另外，**`start` 可以大于 `stop`**：

> 「The start value can be greater than the stop value. In this case the search will be in the negative direction.」

（`stop` 那一格有对称的一句：`The stop value can be smaller than the start value. In this case the search will be in the negative direction.`）

**4. 选 `mode`**（`L` / `LB` / `B`）+ `stepwidth`（`B` 可省）+ `resolution`（最小步长，浮点区间做二分时给）。

**5. 按语法式写**（原样照抄，见本页「语法 / 参数」节）：

```
STRS? ["exec_context",] [start], [stop], {mode}, [(pinlist)], {spec_type}, {"spec_name[@port[@UNCHANGED]]"}, [stepwidth], {resolution}
```

**6. 原文的示例（`## Example`，逐字）**：

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

**把这两行按位置对一遍**（这是本页唯一一个逐字示例）：

| 位置 | 发出的值 | 是什么 |
|---|---|---|
| 1 | **（空）** | `exec_context` 省略 |
| 2 | `0.5` | `start` |
| 3 | `2.0` | `stop` |
| 4 | `LB` | `mode` = linear/binary |
| 5 | **（空）** | `pinlist` 省略 → **默认 `@`（所有 pin）** |
| 6 | `LEV` | `spec_type` = levels |
| 7 | `"aclk_vo_swing"` | `spec_name` |
| 8 | `0.1` | `stepwidth` |
| 9 | `0.1` | `resolution` |

回复按 `{res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]` 对：

| 位置 | 回的值 | 是什么 |
|---|---|---|
| 1 | `GE` | `res_spec` |
| 2 | `2` | `pass_meas_value` |
| 3 | **（空）** | `fail_meas_value` |
| 4 | **（空）** | `pinlist` |

> **（推断）这一例是「区间内没翻转」的那一种。**
> 依据：**回复只给了一个测量值**（`fail_meas_value` 空），
> 而原文说 `If it does not change, then only one value is returned, namely the stop value.`；
> 这里的 `2` 正对着请求里的 `stop` = `2.0`。
> **推断到此为止**：`res_spec = GE` 与这个结论是什么关系，**原文没解释**。
> **另记一处形态差**：请的是 `2.0`，回的是 `2`——**两个写法都是原文示例自带的，本页两个都照抄，不替它归一。**

**7. 报错只有一条**：`primary sets used are not equation-based`。
**所以「pin 名写错会怎样」「变量名不存在会怎样」，本篇没有**（**语料未写**）。

## 和谁有关

- [[spec-search]] — **同一件事的 API 侧**（`SPEC_SEARCH`，L2）。
  本篇 `## Application` 那句 `Spec search testflow.` 说的是同一族。
  **那一篇本页没读**，所以它有哪些入口、覆盖不覆盖 `STRS?` 的三种 mode，本页不知道。
- [[spec-variable]] / [[spec-set]] / [[spec-value]] — **被搜的变量 / 范围来源 / 值**三篇。
  本篇通篇在讲 spec variable 与 primary spec set，
  **但它一条都没链它们**（`Related information` 里链的全是 shmoo 侧）。
  **三篇本页都没读。**
- [[execution-context]] — **第一个参数 `exec_context` 的落点**。
  原文对这一格只写了一句：`An execution context. For more information on execution contexts see Using execution contexts.`
  **那一篇本页没读。**
- [[dfgp]] — **`pinlist` 的第二种写法**：`groups previously created by the DFGP command`。
  **那一篇本页没读。**
- [[test]] — **被反复执行的那个 functional test**（本篇第一句的 `repeats a functional test in a loop`）。
- [[timing]] / [[level]] — **`spec_type` 的两个取值 `TIM` / `LEV` 各落在哪个 stage**；
  也是 frontmatter `stage: timing` 的依据。**两篇本页都没读。**
- [[pin]] — **`pinlist` / `@` / 「pin 的 setup 里有没有用到这个变量」三处都指着它**。
- [[shmoo-tool]] — **同族的「扫值」一类**：本篇 `Related information` 列的三条里，
  两条是 shmoo 命令（`SHSP` / `SHVL`），一条是 search **和** shmoo 共用的多口说明。
  **但本页没有链那三个名字**——**它们都不在 allowlist 里**（§9.1）。
  `[[shmoo-tool]]` 是 GUI 侧的页，**本篇没有提它**——**这一条关系是本页加的（推断），不是本篇写的。**

**本篇点到名字、本页没读的还有两篇**：

- `Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）——
  有页 [[execution-context]]，本页在参数那一处按本篇的写法引它。
- `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）——
  `port` 那一格把「不带 port 时只改 global scope 的 pin」这条规则指向它。**这一篇没有页**（不在 allowlist 里）。

**本页没有引用 `edges.jsonl` 的入边 / 出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，段里有两条**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.0: Setting the primary port`

> **第一条是 §11.2 ② 说的哨兵值**：措辞是 `before`，意思是
> 「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 STRS?」。**

**第二条与正文对得上**：正文有一整节 `Temporarily changing the primary port on a Pin Scale system`，
版本段说的正是 **7.1.0 加了「Setting the primary port」**。
**两条并列照记**——**本页不替它们判定「7.1.0 之前这条命令在 multi-port 上是什么行为」**
（**版本段没有说**）。

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.md`
  （frontmatter 的 `source_topic` 是 `98762.htm`；**7,164 字节 / 221 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节都是脚本从这一篇抽的（**本页一个字没动**）。
- 本篇的节序（照 raw 的 `## ` 标题）：正文三段 → `Temporarily changing the primary port on a Pin Scale system`
  → `Syntax` → `Parameters` → `Application` → `Errors` → `Example` → `Related information` → `Functional changes`。

**本页没做的**：

- **`Related information` 里的三条一条都没读**：
  `SHSP, SHSP? - (SHmoo SPecs)`（raw: `02.06.02.02.221_SHSP__SHSP__-__SHmoo_SPecs.md`）、
  `SHVL, SHVL? - (SHmoo spec VaLues)`（raw: `02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md`）、
  `Modifying the period for a search or shmoo in a multi-port setup (Pin Scale)`
  （raw: `02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）。
  所以**「`@UNCHANGED` 到底改什么」「shmoo 的 spec 与 search 的 spec 是什么关系」
  本页一个字都没有**——正文两次把读者推向第三条，**而那条本页没读**。
- **正文点到、本页没读的还有两篇**：`Using execution contexts`、
  `Global and local scope of base variables`（raw 路径见「和谁有关」末段）。
  **所以「global scope 具体指什么」本页没有。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**；上游 `98762.htm` 里也 **0 个 `<img>`、0 个图片路径**
  （`src=` 只有 1 处，是那个 `p.css` 样式表）。
  **所以本页没有任何来自图的结论**——**「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上跑过 `STRS?`**（`verified: doc-only`）。
  **所以「一次搜索实际跑多久」「`LB` 与 `B` 谁快」本页答不了（§11）。**
- **§10 重复投放：本篇在语料里只有一份**（按文件名全树 glob，1 命中）——
  **不存在 ETIM 那种三份投放的情况。**
- **跨页核对：[[spec-search]]（`SPEC_SEARCH`）的 raw 不在本页的 `sources:` 里**，
  **本页没读它**。本页对它的全部说法只有一句：它是同一件事的 API 侧——
  **这一句来自本篇 `## Application` 那句 `Spec search testflow.`，不是从那一篇读来的。**

### 上游 `.htm` 核对（本页做的一步）

**下面四条去上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\98762.htm`（15,890 字节）核过。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `spec_name` 那一格里的反引号来自上游的 `<code>` 标记——不是丢字，但读起来像内容。**
> md 里那一句逐字是：
> `If you use the option @port`[`@UNCHANGED`]`, (see the port parameter), you must include this extension in the double quotes, too.`
> **上游核对**：`98762.htm` 里，那两个方括号**各自被包在一个 `<code>` 元素里**
> （`@`、`port`、`@UNCHANGED` 三处则包在 `keyword` 的 `span` 里）
> —— **上游把可选方括号标成了代码**，转成 md 就成了反引号。
> **所以这不是转换丢字，是「上游这么标的」**；
> **但它让这一格读起来像「反引号本身是语法的一部分」。**
> **它落在本页的「语法 / 参数」节里，那一节一个字都不许动（§4），故照原样留着。**
>
> **② `Use :` 与 `Use:` 在同一篇里并存。** 逐字两处：
> `Which specification type to use. Use :`
> （`Use` 与 `:` 之间**有一个空格**）与
> `Search mode. Use:`
> （**没有空格**）。
> **上游核对**：`98762.htm` 里 `Use :` 出现 1 次、`Use:` 出现 1 次
> → **上游就坏的**（§11.2 ⑥）。
>
> **③ `Related information` 的三条在 md 里粘成了一行。** md 里那三个链接之间
> **没有任何分隔符**——`](<…>)[` 直接相接。
> **上游核对**：`98762.htm` 里它们**是三个独立的 `<div>`**（各自带 `title` 属性）
> → **是转换把它们压平的**，不是上游的错。
> **本页正文分条引它们时，三个标题都按 `Related information` 的原样写，没有改写。**
>
> **④ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）
> 逐字查过：**本篇一个汉字都没有**——
> **但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
