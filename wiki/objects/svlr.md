---
type: object
title: SVLR, SVLR? - (Spec VaLues at Runtime)
layer: L1
stage: level
tags: [svlr, l1, firmware-command, level, timing, spec-value, spec-variable, spec-set, runtime, multi-port, spst, psfc, debug]
related: [level, timing, mapping-level, mapping-timing, level-spec, timing-spec, spec-tool, spec-set, spec-value, spec-variable, primary-status, spst, psfc, aprm, flush, assign-value-node, flow-sequence-editor, test-program-explorer, level-file]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# SVLR, SVLR? - (Spec VaLues at Runtime)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,221 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

| spec_type | Which specification type to use. Use: | Which specification type to use. Use: |
|---|---|---|
| spec_type | LEV | to specify levels, or |
| spec_type | TIM | to specify timing. |
| equation_set_no | Equation set number. An integer in the range 1 to 99.<br><br>Use PRM to specify the primary equation set, or, in a multi-port setup, the primary specification as defined with SPRM. In this case, the specset_no parameter is ignored.<br><br>In the query, use ALL to display all equation sets.<br><br>This parameter must be omitted if a multi-port specification is specified for the thirdparameter. | Equation set number. An integer in the range 1 to 99.<br><br>Use PRM to specify the primary equation set, or, in a multi-port setup, the primary specification as defined with SPRM. In this case, the specset_no parameter is ignored.<br><br>In the query, use ALL to display all equation sets.<br><br>This parameter must be omitted if a multi-port specification is specified for the thirdparameter. |
| specset_no | Specset number. An integer in the range of 1 to 99. In the query, use ALL to select all defined specsets.<br><br>If specset_no is not set, and equation_set_no is set to ALL or a number, only the spec names in the specified equation sets, but no values are returned. | Specset number. An integer in the range of 1 to 99. In the query, use ALL to select all defined specsets.<br><br>If specset_no is not set, and equation_set_no is set to ALL or a number, only the spec names in the specified equation sets, but no values are returned. |
| multi-port_spec | In a multi-port setup, enter the name of a specification instead of a spec set number. In this case, the secondparameter must be left empty. | In a multi-port setup, enter the name of a specification instead of a spec set number. In this case, the secondparameter must be left empty. |
| spec_name | The name of a base (spec) variable. In a multi-port setup, the same variable name can occur among the spec variables of more than one port within the same specification. In this case, you can qualify the variable name by a port name in the following format<br><br><spec_name>@<port_name>,<br><br>if you want to modify the variable on that port only.<br><br>Note, however, that the scope of the variable will be set to local for the port in question after such a modification (even if it is set to global in the setup), until the setup is downloaded again.<br><br>Note also that in a multi-port setup, you cannot change the value of a variable globally (that is, without specifying a port) unless at least one of the variable instances has its scope set to global in the setup. For basic information on the local and global scope of spec variables in a multi-port setup see `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）. | The name of a base (spec) variable. In a multi-port setup, the same variable name can occur among the spec variables of more than one port within the same specification. In this case, you can qualify the variable name by a port name in the following format<br><br><spec_name>@<port_name>,<br><br>if you want to modify the variable on that port only.<br><br>Note, however, that the scope of the variable will be set to local for the port in question after such a modification (even if it is set to global in the setup), until the setup is downloaded again.<br><br>Note also that in a multi-port setup, you cannot change the value of a variable globally (that is, without specifying a port) unless at least one of the variable instances has its scope set to global in the setup. For basic information on the local and global scope of spec variables in a multi-port setup see `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）. |
| spec_or_equ_name | The name of a base (spec) or derived (equation) variable. An equation variable cannot be specified in the command or in a query which uses the extra parameter. | The name of a base (spec) or derived (equation) variable. An equation variable cannot be specified in the command or in a query which uses the extra parameter. |
| ALL | Requires that the actual values of both base and derived variables are returned. | Requires that the actual values of both base and derived variables are returned. |
| EQUA | Requires that the actual values of only the derived (equation) variables are returned. | Requires that the actual values of only the derived (equation) variables are returned. |
| MAX | Requires that the maximum values of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the maximum value of the specified spec variable. | Requires that the maximum values of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the maximum value of the specified spec variable. |
| MIN | Requires that the maximum of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the minimum value of the specified spec variable. | Requires that the maximum of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the minimum value of the specified spec variable. |
| SPEC | Requires that the actual values of only the base (spec) variables are returned. | Requires that the actual values of only the base (spec) variables are returned. |
| UNIT | Requires that the units of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the unit of the specified spec variable. | Requires that the units of all the base (spec) variables are returned.<br><br>This keyword can also be specified as an extra parameter in combination with the spec_name parameter to retrieve only the unit of the specified spec variable. |
| value | Float with 5 possible decimal places. | Float with 5 possible decimal places. |
| pinlist | By this extra parameter, you can modify the runtime definitions for an individual pin. Note that you cannot retrieve the pin specific values with SVLR?.<br><br>Note You can use the pinlist parameter to modify the value of a spec variable of an individual pin, temporarily. If you make a new modification on a different spec variable, only the last modification is kept while the previous spec variable is reset to the setup value defined in the spec file. To make a permanent modification on a spec variable, specify all pins (that is, @) as the pinlist. Otherwise, to change the value of a spec variable of an individual pin permanently, you have to use a specset for each pin and modify the spec variable in that specset. | By this extra parameter, you can modify the runtime definitions for an individual pin. Note that you cannot retrieve the pin specific values with SVLR?.<br><br>Note You can use the pinlist parameter to modify the value of a spec variable of an individual pin, temporarily. If you make a new modification on a different spec variable, only the last modification is kept while the previous spec variable is reset to the setup value defined in the spec file. To make a permanent modification on a spec variable, specify all pins (that is, @) as the pinlist. Otherwise, to change the value of a spec variable of an individual pin permanently, you have to use a specset for each pin and modify the spec variable in that specset. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98764_2.htm`。

### Example 1

The following example queries the values of the spec variable f in a setup where both single-port and multi-port specifications occur:

```
> SVLR? TIM,ALL,ALL,"f"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",35
< SVLR TIM,,"spec_p_1_p_2","f@p_2",33
< SVLR TIM,1,1,"f",37
```

### Example 2

The next example queries in which equation sets the spec variable f occurs:

```
> SVLR? TIM,ALL,,"f"
< SVLR TIM,1,,"f",
< SVLR TIM,2,,"f",
```

### Example 3

For this example assume that the primary timing is a multi-port specification which contains the two ports p_1 and p_2, and that p_1 and p_2 share the spec variable f in this specification. Assume further that f has been set to scope global for the port p_1. Now query the current value of f for p_1, change it globally, and query it again:

```
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",33
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",43
```

Since f is global for p_1, its value has been modified. Now change the value a second time, but this time locally, and then try to change it globally again:

```
> SVLR TIM,PRM,,"f@p_1",53
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",53
```

The second global command has no effect because f has only local scope after issuing the local command.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The spec does not exist.
- The change to the spec's value results in violations of range, limit, etc.

<!-- 报错节 end -->

## 是什么

**`SVLR` 是运行期改 spec 变量值的那条固件命令；`SVLR?` 是它的查询形式。**
原文第一句把四件事一次说完：

> 「The SVLR command sets a base (spec) variable to the supplied value and recalculates the timing or levels.」

> 「The value must be within the minimum and maximum range specified in the given spec set.」

> 「The new values are activated at the start of the next functional test.」

> 「Note that SVLR does not change the setup value of the spec variable. The previous modifications are reset to the setup values when you make a new one.」

**四句合成一张表**——这是本页最要紧的一条：

| 问题 | 答案 |
|---|---|
| 改的是什么 | 一个 **base (spec) variable** 的**运行期值** |
| 改完会怎样 | **重算 timing 或 levels**（`and recalculates the timing or levels`） |
| 取值有什么限制 | **必须在给定 spec set 的最小/最大范围之内** |
| 什么时候生效 | **下一次 functional test 开始时**（`at the start of the next functional test`）——**不是立刻** |
| 改的是不是 setup 文件里的值 | **不是**（`does not change the setup value`） |
| 连着改第二次会怎样 | **上一次的修改被复位回 setup 值**（`The previous modifications are reset to the setup values when you make a new one.`） |

**最后一行是最大的坑**：`SVLR` **不是累积的**。
参数表里那条 `pinlist` 的 `Note` 把同一件事说得更死：

> 「If you make a new modification on a different spec variable, only the last modification is kept while the previous spec variable is reset to the setup value defined in the spec file.」

| 你连着做的动作 | 结果 |
|---|---|
| 改完 `a`，再改 `a` | 后一次生效 |
| 改完 `a`，再改 **`b`** | **只有 `b` 留着；`a` 被复位回 spec 文件里的 setup 值** |

**所以 `SVLR` 一次只维持一个临时改动**——`LEVEL_SPEC` 那侧靠 C++ 缓存能做到 `restore()`，
**固件这一侧没有那份缓存**（**推断**，依据是两篇共用那段 CAUTION，见下）。

### `SVLR?` 查的是两种东西

> 「The SVLR? query either returns the current runtime values of one or more base or derived (spec or equation) variables, or the associations between variables and equation sets.」

**「值」与「隶属关系」是两种回答**——`Example 1` 回值，`Example 2` 回隶属关系（见「典型用法」）。

**一条查询能力上的边界**：

> 「Note that you cannot retrieve the pin specific values with SVLR?.」

**即：能用 `pinlist` 写 per-pin 的值，但读不回来。**

### `SVLR` 不改 Test Program Explorer，改的是一个状态位

> 「Note The SVLR command does not set the Test Program Explorer out of date, but it sets the status bit 10 of the affected spec set. The status bits can be queried with the SPST? query.」

**这句话给了两件事**：① **`SVLR` 改过的 spec set 会被标记出来**（**bit 10**）；
② **查它要换一条查询**——`SPST?`（[[spst]]，**未建**）。
**所以「`SVLR` 改过没有」这个问题，`SVLR?` 自己回答不了**（它回的是值，不是改过没改过）。

### 它作用在「有 setup focus 的那个 site」上

> 「With this command you configure setups of those sites that have the setup focus: For more information, see also: PSFC, PSFC?」

> 「With this command you can retrieve site specific information (only one site can be in focus at a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**前置是 [[psfc]]（Parallel Setup FoCus）**——**setup focus 不在你想要的那个 site 上，这条命令就作用在别的 site 上。**

### 单口 / 多口：三套写法，`PRM` 与 `,,` 是两个关键字

原文把写法按「specification 是单口还是多口」分成三组（**这三组是原文自己的小标题**：
`## For single-port specifications` / `## For multiport specifications` / `## For both types of specifications`）。
写法本身**没有进「语法 / 参数」节**（脚本按段标记收，本篇命中的 H2 是 `## Parameters`
与 `## Examples`，上面那三组写法的小标题不命中，**一个字符都没收进去**）——
**要照抄写法得回 raw 看那三节**。这里只说三条读法：

**① `,,` 不是笔误——多口写法里 `equation_set_no` 那一格必须是空的。**
参数表：`This parameter must be omitted if a multi-port specification is specified for the thirdparameter.`
（**`thirdparameter` 缺空格，原文如此**，见「出处」⚠️②。）

**② `PRM` 管两种情况。** 参数表：`Use PRM to specify the primary equation set, or, in a multi-port setup, the primary specification as defined with SPRM. In this case, the specset_no parameter is ignored.`
——**用了 `PRM` 就不要再给 specset 号**（`is ignored`）。

**③ `ALL` 出现在哪一格，意思不一样。**

| `ALL` 出现在 | 意思 |
|---|---|
| `equation_set_no` 那一格 | **所有 equation set**（`use ALL to display all equation sets`） |
| `specset_no` 那一格 | **所有已定义的 specset**（`use ALL to select all defined specsets`） |

**而且 `specset_no` 空着时，只回名字不回值**：
`If specset_no is not set, and equation_set_no is set to ALL or a number, only the spec names in the specified equation sets, but no values are returned.`
——**这正是 `Example 2` 回出来一行空值的原因**（见下）。

### 三个额外关键字、以及一条自相矛盾（⚠️）

`MAX` / `MIN` / `UNIT` 都是「额外参数」，可以单独用，也可以**跟着一个 `spec_name` 用**
（参数表：`This keyword can also be specified as an extra parameter in combination with the spec_name parameter`）。

**但 `MIN` 那一格的说明自相矛盾**（照实记，本页不替它改）：

> 「Requires that the maximum of all the base (spec) variables are returned.」

**这一格是 `MIN`，正文里写的却是 `maximum`**；紧接着的第二句才写
`retrieve only the minimum value of the specified spec variable.`——
**同一格里一个 maximum、一个 minimum。**（`MAX` 那一格写的是 `maximum`，是对的。）

### `## Application` 一节只有一行

> 「The assign value node in the testflow.」

（**后面紧跟着的 `Note` 是粘在一起的**：`The assign value node in the testflow.Note Each site in a multisite environment can set its own value.`
——见「出处」⚠️④。）
**即：这条命令在 testflow 侧挂的是 assign value 节点**（[[assign-value-node]]，**未建**），
**多 site 时每个 site 可以给自己的值**。

### `## Errors`：两种情况下报错

> 「An error is generated if:」

> 「- The spec does not exist.」

> 「- The change to the spec's value results in violations of range, limit, etc.」

**第二条与开头那句「value 必须在范围之内」是同一件事的两面**——
**范围检查不是「静默截断」，是报错。**

## 典型用法

原文三个 Example **各演示一种回答形态**。逐字在「语法 / 参数」节里，这里只写读法：

**Example 1：同一套 setup 里，单口与多口并存时 `f` 有几个实例。**
`SVLR? TIM,ALL,ALL,"f"` 回了三行——两行多口（`"spec_p_1_p_2"` 的 `f@p_1`、`f@p_2`），
一行单口（`TIM,1,1,"f",37`）。
**所以「同名变量在多口与单口里是两个不同的实例」，同一个查询会把它们全报出来。**

**Example 2：`f` 出现在哪些 equation set 里。**

> 「The next example queries in which equation sets the spec variable f occurs:」

回出来的是 `SVLR TIM,1,,"f",` 与 `SVLR TIM,2,,"f",`——**值那一格是空的**。
**这正是上面「`specset_no` 空着就只回名字」那条规则的实例。**
**这条查询回答的是「在哪」，不是「是多少」**——**要值就得给 `specset_no` 那一格。**

**Example 3：local / global scope 的三步因果链**（**本页最实用的一条**）。
原文先给的假设：

> 「Assume further that f has been set to scope global for the port p_1.」

然后三步：

| 第几步 | 命令 | 结果 |
|---|---|---|
| 1 | `SVLR? TIM,PRM,,"f@p_1"` | **33**（查出来是 33） |
| 2 | `SVLR TIM,PRM,,"f",43`（**不带 port**，全局改） | 再查 `f@p_1` → **43** |
| 3 | `SVLR TIM,PRM,,"f@p_1",53`（**带 port**，局部改），再 `SVLR TIM,PRM,,"f",43`（全局改） | 再查 `f@p_1` → **还是 53** |

原文对第 2 步的解释：

> 「Since f is global for p_1, its value has been modified.」

对第 3 步的解释：

> 「The second global command has no effect because f has only local scope after issuing the local command.」

**因果链**（原文在参数表里把规则写全了）：

| 规则 | 原文 |
|---|---|
| 带 port 改过之后，那个 port 上的 scope **变成 local** | `the scope of the variable will be set to local for the port in question after such a modification (even if it is set to global in the setup), until the setup is downloaded again` |
| 不带 port 改（全局改）**要先有至少一个实例是 global** | `you cannot change the value of a variable globally (that is, without specifying a port) unless at least one of the variable instances has its scope set to global in the setup` |
| **怎么恢复** | `until the setup is downloaded again`——**重新下载 setup** |

**所以「我全局改了，怎么没生效」的答案就是**：**之前有人带 port 改过一次，那个 port 的 scope 被降成 local 了。**
参数表还为这条规则专指了一篇（`Global and local scope of base variables`，**本页没读**）。

**本篇没有 `## Procedure`，也没有 `## Before you begin`**——
原文的结构是「单口 / 多口 / 两者适用」三组写法 + `## Parameters` + `## Application` + `## Errors` + `## Examples`。

**和 [[level-spec]] 是同源文本**：两篇的 CAUTION 段落**逐字相同**，
而且**互相指对方**——本页那段说的是「非调试目的别混用 API 与固件命令」，
[[level-spec]] 那篇的 `Note` 说的是「调试时可以停了 application model、从 `hpt` 敲 `SVLR`」。
**一条命令的两条路，分工在原文里就是这么写的。**

## 和谁有关

- [[level]] / [[timing]] / [[mapping-level]] / [[mapping-timing]] — **本页 `stage: level`，但它同时管 timing**（`spec_type` 取 `LEV` 或 `TIM`）。
  **所以它被两页对照表都引到**：[[mapping-level]] 主表第 124 行「运行时改 spec 值并重算」的 **L1 格就是本页**（同一行 L2 格是 [[level-spec]]、GUI 格是 [[spec-tool]] 的 Download、文件格是 [[level-file]] 的 `SPECS` / `SPECSET` 块）。
  **建本页之前**（2026-09-20 写这页时）`extract/dangling.csv` 里本页被 **8 处引用**
  （`level`、`mapping-level`、`mapping-timing`、`spec-tool`、`timing` 等）——**本页是两个阶段页共同的那个口。**
  ⚠️ **那个数是「建页之前」的**：**本页一建成，它就从那张单上消失了**。
  **引用外部工作单的数字都会这样过期**——写的时候要标清是哪一刻的数。
- [[level-spec]] — **同一件事的 L2 路**。两篇共用同一段 CAUTION（**逐字相同**），**分工是「C++ 里改」与「`hpt` 里改」**，而且**原文把固件这条标成 `For debug purpose only`**。**那页本页没读**（本页只在两条 CAUTION 里认识它）。
- [[timing-spec ]] — **timing 侧的 L2 同款 API**，位置与 [[level-spec]] 对称。**本页的 `TIM` 分支与它是一对**（**推断**，依据只有那句并列的 CAUTION 与 `spec_type` 的两个取值）。
- [[spec-tool]] / [[spec-set]] / [[spec-value]] / [[spec-variable]]（**后两个未建**）— **别混**：`spec-tool` 是 GUI 上编 spec set 的工具、`spec-set` 是「一组值」那个容器；**本页不是它们中的任何一个**——本页是「**运行期改一个已经存在的 spec 变量**」的那条命令。
  另有一处反向的关系：[[spec-tool]] 那页记着，**shmoo tool 里区分 local / global 必须与 `SVLR` 用同一种写法**（`<spec_variable>@<port_name>`）——**那一条写在那页的出处文档里，本页的出处文档没有说**。
- [[primary-status]] — 原文用 `PRM` 表示 primary equation set 或 primary specification，**primary 是 `SPRM` 定义的**。**`PRM` / `SPRM` 两篇本页都没读**，本页只有参数表里那两句话。
- [[spst ]] — **查本页改过没有的入口**：`it sets the status bit 10 of the affected spec set. The status bits can be queried with the SPST? query.`
- [[psfc]]（**已建**）— **本页的前置**：原文说这条命令配置的是「有 setup focus 的那些 site」，并要求参见 `PSFC, PSFC?`。**那页本页没读**，本页只有这一句。
- [[assign-value-node ]] — `## Application` 一节**只有它**（`The assign value node in the testflow.`）——**本页在 testflow 侧挂的就是那个节点**。[[mapping-testflow]] 主表第 112 行「运行期改 level / timing spec 值」把 **GUI 格给 [[flow-sequence-editor]] 的两个向导（`assign level value` / `assign timing value`）、L1 格给 `SVLR`**——那一页引的原文是 `02.08.04.32.02.01.12.05`，**本页没读那一篇**。
- [[test-program-explorer]]（**已建**）— **原文明确说本页不会把它置成 out of date**（只置状态位）——**这是本页与「改了 setup 就要存盘」那条习惯的分界**。**那页本页没读。**
- [[aprm]] / [[flush]] — **不属本页**：改完 spec 值之后「怎么让它到硬件」是它们的事（**推断**，依据是 [[flush]] 那页写的「改 spec 值只到固件层、不到硬件」；**本页的出处文档一个字没提 FLUSH**）。
- `Global and local scope of base variables`（`02.06.06.01.05.03.01`，**未建**）— 原文为 scope 规则专指的那一篇。**本页没读**——**所以 scope 的完整规则本页没有**，本页只有 `Example 3` 那段演示与参数表里的两句。
- **只写反引号、不写链接的名字**：`SVLR` / `SVLR?`（页名里带了，但正文里的命令自身按 §9.1 走反引号写法）、`hpt`、`LEV` / `TIM` / `PRM` / `ALL` / `EQUA` / `MAX` / `MIN` / `SPEC` / `UNIT`、`SPST?`、`PSFC`、`spec_name@port_name`、`<spec_name>@<port_name>`——**它们都不在 `extract/prose-allowlist.txt` 里**，按 §9.1 一律反引号。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- `Introduced before SmarTest 6.3.2`

**这是哨兵值，不是「6.3.2 的变更」**（`schema.md` §11.2②）：`Introduced before` 的意思是
「**在本文档集覆盖范围开始之前就已经有了**」——**照字面读会生成一条「6.3.2 新增了 SVLR」，那是错的。**

**本篇没有任何其它版本条目**，所以这些都没有版本归属（**语料未写**，本页不推测）：

| 本页的内容 | 语料给的版本 |
|---|---|
| `pinlist` 那个额外参数 | **未写** |
| 多口那一套写法（`multi-port_spec` / `@port_name`） | **未写** |
| 那句 `For debug purpose only` 的调试路径 | **未写** |
| `ALL` / `EQUA` / `MAX` / `MIN` / `SPEC` / `UNIT` 这些额外关键字 | **未写** |

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`
  （TDC `98764_2.htm`，13,695 字节 / 310 行）。
- **本页「语法 / 参数」节的来源就是这一篇自己**（节首没有「取自子主题」后缀），
  节里那 5,330 字符就是原文的 `## Parameters` 表与三个 `### Example`。

### ⚠️ 这一条命令在语料里有四份投放，本页只读了其中一份

实测按 `source_topic` 查，同一篇 `SVLR` 有四个落点：

| `source_topic` | 文件 | 本页 |
|---|---|---|
| `98764.htm` | `02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md` | **只 diff 过正文，没有当出处读** |
| **`98764_2.htm`** | **`02.06.05.02.24_...`（本页的出处）** | **整篇读过** |
| `98764_3.htm` | `02.06.06.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md` | **没读** |
| （内嵌） | `02.08.04.34.02.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`（Timing Setup Tool 的子主题） | **没读**；`wiki/objects/timing-setup-tool.md` 收的是那一份 |

**本页把前两份逐字 `diff` 过：正文完全相同，只有 frontmatter 的 `source_topic` / `source_html`
两行不同**（9,835 字节 vs 9,834 字节，差的正是那两个字符串）。
另两份**没有比对过**——**所以「四份是不是都逐字相同」本页不知道。**

**一处值得记的投放关系**：本页的出处文档（`.24`）在它那句调试 `Note` 里，
把读者指向的是**另一份投放**（`[SVLR](<02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>)`），
**不是它自己**；[[level-spec]] 那篇指的还是同一个 `.252`。
**raw 逐字如此，本页不改**——**这属于「重复投放」在链接上的表现**（见 `schema.md` §10 的重复投放）。

### 本页读的图：**0 张，因为这一篇一张图都没有**

**实测该篇对 `raw/` 的图片引用 0 处**（`grep -o 'raw/[0-9]*\.\(png\|jpg\)'` 零命中）。
**这不是「图够不着」，是这一篇本来就不带图**——所以本页**没有任何来自图的结论**，
也没有任何一处需要标「④ 图证」。**`SVLR` / `SVLR?` / `SPST?` / `PRM` 这些标识符
全部是从正文逐字读到的。**

### 本页没做的

- **同一命令的另外三份投放没读**（只 diff 了其中一份的正文，见上）。**另外三份里有没有多出来的段落，本页不知道。**
- **`02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md` 没读**——
  原文为 scope 规则专指的那一篇。**所以 scope 的完整规则本页没有**；
  本页只有 `Example 3` 那段三步演示与参数表里的两句。
- **`PSFC, PSFC?`（`02.06.02.02.191`）没读**——**setup focus 是本页的前置**，
  而本页只有原文那一句「配置的是有 setup focus 的 site」。**「focus 怎么设、一次能有几个」本页答不了。**
- **`SPST?` 没读**——**bit 10 怎么查、那个 spec set 的其他 bit 是什么，本页一个字没有。**
- **`PRM` / `SPRM` 两篇没读**——`PRM` 在多口里等于 `SPRM` 定义的 primary specification，
  **这条本页只从参数表的原文里转述**。
- **`LEVEL_SPEC` / `TIMING_SPEC` 两篇没读**——本页读到的那段 CAUTION
  **是从本页的出处文档里读到的**，**不是从它们那两篇**；
  「固件层没有缓存」这个因果**是本页的推断**，依据是那段 CAUTION 自己的措辞。
- **`02.06_Command_Reference` 里别篇对 `SVLR` 的引用没查**（例如 `timing-setup-tool` 那页收的内嵌副本），
  **所以本页不知道语料里还有谁在讲这条命令。**
- **没有实跑。** 没有在 `hpt` 上敲过 `SVLR`、没有查过 `SPST?` 的 bit 10、
  没有在多口 setup 上验证过那条 scope 规则。**`verified: doc-only` 指的就是这件事**——
  **`Example 1`–`3` 的回显是原文给的，不是本页跑出来的。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[level]] / [[timing]] 那两页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① `MIN` 那一格自相矛盾。** 参数表里 `MAX` 写的是

> 「Requires that the maximum values of all the base (spec) variables are returned.」

而 `MIN` 写的是

> 「Requires that the maximum of all the base (spec) variables are returned.」

**`MIN` 的正文里也是 `maximum`**，紧接着的第二句却写
`retrieve only the minimum value of the specified spec variable.`
**同一格里一个 maximum 一个 minimum。本页在正文里并列两处，没有替它选一个。**

**② 两处缺空格：`secondparameter` / `thirdparameter`。**

> 「This parameter must be omitted if a multi-port specification is specified for the thirdparameter.」

> 「In this case, the secondparameter must be left empty.」

**`thirdparameter` 与 `secondparameter` 都是一个词写成的。本页照原样引，没有在中间加空格。**

**③ 一处缺空格：`itself.Note`。** 那段 CAUTION 与紧跟的 `Note` 粘在一起
（`...corresponding setup file itself.Note For debug purpose only:`）。
**[[level-spec]] 的出处文档在同一处有一个空格**（`itself. Note`）——两篇是同源文本，
**两篇那段 CAUTION 的文字只有这一处不同**（不是两次笔误，是两次投放之间掉了那个空格；
另有一处不同是 raw 链接的相对路径写法——那是 md 所处的目录深度造成的，
不是文字差别，见「出处」那一节）。
**本页引到 `itself.` 为止，没有用省略号接句子。**

**④ `## Application` 一节里两个 `Note` 粘在一起**：

> 「The assign value node in the testflow.Note Each site in a multisite environment can set its own value.」

**`testflow.` 与 `Note` 之间没有空格**；**后一个 `Note` 与前一句之间也没有任何分隔**——
**本页照原样引。**

**⑤ 多口 `SVLR?` 的第二行缺空格。** 原文那一行是
`SVLR?{spec_type},, {"multi-port_spec"}, {ALL|EQUA|MAX|MIN|SPEC|UNIT}`——
**`SVLR?` 与 `{spec_type}` 之间没有空格**，而它上一行（查询 `spec_or_equ_name` 的那条）写的是 `SVLR? {spec_type}`。
**同一节的相邻两行，一行有空格一行没有。本页照原样转录，不补空格。**

**⑥ 一处大小写不统一**：原文标题写 `Spec VaLues at Runtime`（**`L` 大写**），
而正文那句写的是 `The SVLR command ...`（命令名本身全大写）。
**这是语料的标题命名法（每个词里挑一个字母大写），不是错**——**本页记下它，免得下一个人以为是错字。**

**⑦ 本页这一篇没有编码坏字（§11.2① 那一族）**：用 `[一-鿿]` 实测零命中；
**也没有 §11.2⑤ 那个整词替换**（`DC/DC power units` 实测 0 命中）。
**这不是「没找到」，是查过、结果为零**——**所以本页的 `SVLR` / `SVLR?` / `SPST?` / `PSFC`
这些标识符，都是从正文逐字读到的，不是从图上、也不是从坏字里推的。**

`verified: doc-only`
