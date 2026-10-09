---
type: object
title: PSAS? - (Power Supply Accumulated Status)
layer: L1
stage: results
tags: [dps, status, flags, query, accumulated, results, dc-test, power-supply]
related: [results, mapping-results, xps256-status-flags, dps-aux-pin-task, dps-power-flags-get-functions, get-functional-result, dpspins-resources, dps128-dps64-cards]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# PSAS? - (Power Supply Accumulated Status)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,617 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PSAS? [msMode ,] {mask}, {(pinlist)}
```

returns

```
PSAS {status}, {(pinlist)}
```

Parameters
 | msMode  | The extra parameter controls how the return value is created.

The value of the parameter can be PQFC:

- PQFC specified: The current query focus is respected and allows status query per site without affecting status bits of other sites.
- PQFC not specified: The command reads (and clears) status bits of all enabled and active sites at a glance, ignoring the actual query focus.
The parameter applies only to use of parameter mask as integer value. |
 | mask  | Integer bit mask or ALL.

-

Integer bit mask: Integer value is used to mask out individual status bits. Each bit of mask is logically AND-ed with the corresponding bit of the DPS status. If one of the resulting bits is set, then F (Fail) is returned, otherwise P (Pass).

It is used to check for an error condition. All bit positions of the status flags that should be checked, must be set to 1 in mask. If one of the selected status bits is set, then PSAS? returns F.

- ALL: Hex value (hexadecimal representation of all status bits) is returned.
For setting the integer bit mask or interpreting a returned hex value, refer to the `status`（raw: `02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.md#_98691__r_status`） parameter below. |
 | pinlist  | Comma separated list of DPS128/64 or XPS256 pins. The @ character can be used to read the status for all DPS pins. |
 | status  | If parameter mask is ALL, you need to translate the hex value (hexadecimal representation of the status bits) to its binary form as follows:

 | Bit 0 (LSB):  | Constant voltage |
 | Bit 1:  | Constant current |
 | Bit 2:  | Unregulated |
 | Bit 3:  | Overvoltage |
 | Bit 4:  | Overpower / Overcurrent / Power budget exceeded |
 | Bit 5:  | Overtemperature |
 | Bit 6:  | Voltage drop force |
 | Bit 7:  | Voltage drop return |
 | Bit 8:  | DUT board disconnect  | For the special mapping of bit 9 and 8 on UHC4 and UHC4T, refer to table `DPS flag description`（raw: `02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.md#_98691__s_DPS_flag_description`） below. |
 | Bit 9:  | Safety line |
 | Bit 10:  | Current limit disconnect |
 | Bit 11:  | Low headroom |
 | Bit 12:  | Current limiter protection detected |
 | Bit 13:  | Range overflow |
 | Bit 14 (MSB):  | Clamp distance too low |
 | Bit 15:  | Voltage drop force warning |
 | Bit 16:  | Voltage drop return warning  |  If parameter mask is specified as an integer bit-mask:

- Pass: P
- Fail: F

Refer to table `DPS flag implementation`（raw: `02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.md#_98691__s_DPS_flag_implementation_710`） below for information regarding the card specific implementation of the bits or flags.

 |

### Description

For the following examples (1 to 4), the assumed binary value of the status of the UHC4 pin Vcc is 10000110 (Voltage drop return, Unregulated, Constant Current).

### Example 1

To get all flags:

```
PSAS? ALL,(Vcc)
```

returns

```
PSAS #86,(Vcc)
```

### Example 2

To check if Unregulated (bit 2) is set:

```
PSAS? 4,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 3

To check if Constant Current (bit 1) or Overpower (bit 4) is set:

```
PSAS? 18,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 4

To check if Voltage Drop Force (bit 6) or DUT Board Disconnect (bit 8) is set:

```
PSAS? 320,(Vcc)
```

returns

```
PSAS P,(Vcc)
```

### Example 5

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 2,(Vee)
```

This example for device pin Vee shows the DPS is working in constant current mode.

### Example 6

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 64,(Vee)
```

This example for device pin Vee shows the DPS has hit the voltage drop force threshold.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if a communication error with the DPS occurs.

The status bits 4 to 11 result in a disconnect of the pin. To reconnect you must execute a disconnect-connect sequence.

<!-- 报错节 end -->

## 是什么

**一句话：`PSAS?` 是 DPS 的状态累积查询——它一次做三件事：读标志、清标志、给一个结果。** 原文第一句：

> 「The PSAS? (Power Supply Accumulated Status) query reads and clears the internal status flags of the Device Power Supplies (DPS) in DPS operating mode, in PMU operating mode, or in Digital I/O operating mode.」

**`reads and clears` 是这一页最该记的三个字**：它不是纯读——**读这一下就把标志清掉了**。紧随其后的一句把「什么时候清」也说了：

> 「All DPS status flags are cleared at connect and disconnect if the trigger condition is no longer true.」

### 只有查询形态，没有设置形态

本篇给的两行语法里，**命令那一行带 `?`、返回那一行不带**：

```
PSAS? [msMode ,] {mask}, {(pinlist)}
```

```
PSAS {status}, {(pinlist)}
```

**本页实测：全篇没有一条不带 `?` 的 `PSAS` 调用例子，也没有任何一句说 `PSAS` 能设什么**——`## Examples` 那六个例子全是查询。**所以「`PSAS` 的设置形态」在本篇里不存在**（不是本页没找到，是这篇文档只讲查询）。

### `Accumulated` 是什么意思

> 「The query returns either a hex value or a pass/fail result. The hex value must be translated into binary form to interpret the status.」

> 「The result will show any bits that have been set on tests performed since the previous execution of the command, or since the last connect or disconnect sequence was executed.」

**第二句就是 `Accumulated`（累积）的定义**：返回的不是「此刻的标志」，而是**自上次执行本命令、或自上次 connect / disconnect 以来，被置起来过的位**。**所以同一个标志连着读两次，结果可能不同**（推断，依据就是 `reads and clears` 与这句 `since the previous execution`）。

### 三个参数：`msMode` / `mask` / `pinlist`

| 参数 | 原文 |
|---|---|
| `msMode`（可省） | 「The extra parameter controls how the return value is created.」 |
| `mask` | 「Integer bit mask or ALL.」 |
| `pinlist` | 「Comma separated list of DPS128/64 or XPS256 pins. The @ character can be used to read the status for all DPS pins.」 |

**`mask` 决定「返回什么形状」**，这是最容易用错的一处：

| `mask` 写成 | 返回 | 判据（原文） |
|---|---|---|
| **整数 bit mask** | `P` 或 `F` | 「Each bit of mask is logically AND-ed with the corresponding bit of the DPS status. If one of the resulting bits is set, then F (Fail) is returned, otherwise P (Pass).」 |
| **`ALL`** | 十六进制 | 「Hex value (hexadecimal representation of all status bits) is returned.」 |

**整数 mask 怎么写，原文也给了**：

> 「It is used to check for an error condition. All bit positions of the status flags that should be checked, must be set to 1 in mask. If one of the selected status bits is set, then PSAS? returns F.」

即：**想查哪几位就把哪几位置 1**；**只要被查的位里有一个是 1，整条命令就返回 `F`**——它是「中了没有」的汇总，**不是逐位回答**。

### `msMode` 只有一个取值，而且只在整数 mask 时才有意义

> 「The value of the parameter can be PQFC:」

| 写不写 `PQFC` | 原文 |
|---|---|
| **写** | 「PQFC specified: The current query focus is respected and allows status query per site without affecting status bits of other sites.」 |
| **不写** | 「PQFC not specified: The command reads (and clears) status bits of all enabled and active sites at a glance, ignoring the actual query focus.」 |

**这一对是整页最反直觉的一条**：**默认（不写 `PQFC`）反而是「忽略 query focus、把所有 enabled and active 的 site 的标志一起读掉」**；写了 `PQFC` 才只碰 focus site。

> 「The parameter applies only to use of parameter mask as integer value.」

**所以 `msMode` 配 `ALL` 无效**——这句话把它锁死在整数 mask 上。**本页实测：全篇 `PQFC` 只出现 3 次，全在这一节（`can be PQFC` / `PQFC specified` / `PQFC not specified`）。**

**这一条要和另一句分开读**：

> 「With this command you can retrieve site specific information (only one site can be in focus at a time).」

**那句说的是「结果怎么显示」**——它后面紧跟着的原文是 `For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools.`——**不是「命令只能读一个 site」**；命令的取数范围恰恰由 `msMode` 决定。（推断，依据是这两句的合读。）

### 位号 ↔ 标志名（17 位）

`mask=ALL` 时返回的十六进制**必须自己翻成二进制再对表**。表逐字见本页「语法 / 参数」节，这里按位号抄一遍：

| 位 | 标志 |
|---|---|
| 0 (LSB) | Constant voltage |
| 1 | Constant current |
| 2 | Unregulated |
| 3 | Overvoltage |
| 4 | Overpower / Overcurrent / Power budget exceeded |
| 5 | Overtemperature |
| 6 | Voltage drop force |
| 7 | Voltage drop return |
| 8 | DUT board disconnect |
| 9 | Safety line |
| 10 | Current limit disconnect |
| 11 | Low headroom |
| 12 | Current limiter protection detected |
| 13 | Range overflow |
| 14 | Clamp distance too low |
| 15 | Voltage drop force warning |
| 16 | Voltage drop return warning |

**原文在 bit 14 上写着 `(MSB)`**——**它下面还有 Bit 15 与 Bit 16**（见「出处」⚠️ ①）。

**每个标志一句话的解释在 `## DPS flag description` 一节里**（本页「语法 / 参数」节不收那一节）。原文对那整节的总述是：

> 「The functionality of the flags is largely the same for the various DPS cards.」

**然后它只挂了一条链接**：

> 「For a card-specific detailed description of the flags refer to」

（那节里这个列表只有一项：`XPS256 status flags`——**四种卡只给了 XPS256 一篇**。）

**而且四种卡不是每个标志都实现**：

> 「The implementation of the flags differs for the various DPS cards, that is, various cards do not support every flag.」

逐格见本页「语法 / 参数」节的 `DPS flag implementation` 表（`+` 支持 / `-` 不支持）。

### 什么时候被清：两条规则，还有一处原文自己没对齐

> 「All DPS status flags are reset to 0 at connect (PSST ON) and disconnect (PSST OFF), but the effect of a PSAS? is different for the "Constant Voltage" flag. It is 1 when all other flags are 0.」

> 「Note that a reset to 0 is only effective if the condition for the flag is no longer true. The flag is not reset, if the condition is still true at the time of the connect / disconnect or PSAS? query.」

**合起来是**：connect / disconnect 清标志，**但「清」只管条件已经不成立的那些位**——**条件还成立就不清**。**Constant Voltage 这一位特殊：别的位全 0 时它是 1。**

⚠️ **这里有一处原文自己没对齐**：开头的 `Note` 把「为什么 `PSAS?` 的效果不同」归给**卡的不同**，而 `## DPS flag reset` 那一节归给**`Constant Voltage` 这一个标志**。**两处并列，本页不替它调和**（见「出处」⚠️ ④）。

### `## Errors` 里两句不是同一类话

（这一节由脚本逐字抽进本页「报错条件」节，本页一个字没动。）**但它里面只有第一句是报错条件**：

> 「An error is generated if a communication error with the DPS occurs.」

> 「The status bits 4 to 11 result in a disconnect of the pin. To reconnect you must execute a disconnect-connect sequence.」

**第二句是「后果 + 恢复动作」**——**它是这一页最要紧的一句操作信息**：**位 4 到 11 里任意一个置起来，pin 会被断开；要连回来必须走一次 disconnect-connect**。**注意它是「断开」，不是「报错」。**

### 一条会咬人的顺序约束：`PSAS?` 会让 `PRLT` 的结果失效

原文用一整块 `Note` 讲这件事，并给了 API 侧的对应：

> 「Pass/fail results that are retrieved by command PRLT are invalidated by commands CSAS and PSAS.」

> 「We recommend therefore using the command PRLT directly after the related functional test and before command CSAS or PSAS are performed.」

> 「This behavior applies not only to the commands but also to the related APIs: Function GET_FUNCTIONAL_RESULT() must be performed before any of the DPS_AUX_PIN_TASK.check...() functions is called or the results of GET_FUNCTIONAL_RESULT() are invalid.」

**所以顺序是**：functional test → `PRLT` / `GET_FUNCTIONAL_RESULT()` → **之后才** `CSAS` / `PSAS?` / `DPS_AUX_PIN_TASK.check...()`。**反过来（先 `PSAS?` 再 `PRLT`），拿到的 pass/fail 是失效的。**

### `## Application`：它属于哪一块

> 「DC Tests, see DC Measurement Commands.」

**`PSAS?` 是 DC Measurement Commands 一族里的命令**（后一句就是那个链接名）。**这是本篇唯一一处「它在体系里的位置」**——本篇没有 `## Predependencies`，`## Related information` 也只有四条名字。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`**——它是一篇命令参考。**能写出来的用法全部来自 `## Examples` 那六段**（逐字在本页「语法 / 参数」节）。

### 六个例子逐条

例子 1–4 共用一个假定状态：

> 「For the following examples (1 to 4), the assumed binary value of the status of the UHC4 pin Vcc is 10000110 (Voltage drop return, Unregulated, Constant Current).」

| 例 | 命令 | 返回 | 原文写的意图 |
|---|---|---|---|
| 1 | `PSAS? ALL,(Vcc)` | `PSAS #86,(Vcc)` | 「To get all flags:」 |
| 2 | `PSAS? 4,(Vcc)` | `PSAS F,(Vcc)` | 「To check if Unregulated (bit 2) is set:」 |
| 3 | `PSAS? 18,(Vcc)` | `PSAS F,(Vcc)` | 「To check if Constant Current (bit 1) or Overpower (bit 4) is set:」 |
| 4 | `PSAS? 320,(Vcc)` | `PSAS P,(Vcc)` | 「To check if Voltage Drop Force (bit 6) or DUT Board Disconnect (bit 8) is set:」 |
| 5 | `PSAS? ALL,(Vee)` | `PSAS 2,(Vee)` | 「This example for device pin Vee shows the DPS is working in constant current mode.」 |
| 6 | `PSAS? ALL,(Vee)` | `PSAS 64,(Vee)` | 「This example for device pin Vee shows the DPS has hit the voltage drop force threshold.」 |

**三件事从这张表里直接读出来**：

- **返回的形状跟着 `mask` 走**：例 1 / 5 / 6 用 `ALL` → 回来的是十六进制；例 2 / 3 / 4 用整数 → 回来的是 `P` / `F`。
- **整数 mask 是「把要查的位加起来」**：例 3 查 bit 1 与 bit 4 → `18`；例 4 查 bit 6 与 bit 8 → `320`。**原文只写「查哪两位」，那个数怎么算出来的它没解释**——**这一步是本页补的（推断）**，依据是参数表里 bit ↔ 权重的定义（2¹+2⁴=18、2⁶+2⁸=320）。
- **十六进制回来要自己翻位**：例 5 的 `2` 是 bit 1（Constant current），与原文那句结论一致；例 6 的 `64` 按十进制读是 bit 6（Voltage drop force），与原文那句 `voltage drop force threshold` 一致——**但按十六进制读就不是只有 bit 6**（见「出处」⚠️ ⑧）。**例 1 的 `#86` 与 `### Description` 里那个 `10000110` 完全对得上**（bit 1 + bit 2 + bit 7），**这一条是本页核过的。**

### 按顺序走一遍

1. **先想清楚要「中了没有」还是要「哪些位」**：要 `P`/`F` 就用整数 mask，要全部位就用 `ALL`。
2. **整数 mask 的算法**：把要查的位按权重加起来（例 3 / 4 的 `18` 与 `320`）。
3. **只在整数 mask 时才考虑 `msMode`**：**要给单个 site 留清、不碰别的 site，就写 `PQFC`**（[[pqfc]]）。
4. **要读所有 DPS pin 就写 `@`**（原文：`The @ character can be used to read the status for all DPS pins.`）。**六个例子里一条都没用 `@`。**
5. **拿到十六进制回来自己翻位**（用上面的位号表）——**原文不给翻译工具，也不给第二张对照表。**
6. **顺序别错**：在 functional test 之后、`PRLT` / `GET_FUNCTIONAL_RESULT()` 之前**别调它**。
7. **看到 `F` 别只看结果**：位 4 到 11 会让 pin 断开，**要连回来得走一次 disconnect-connect**。

## 和谁有关

- [[results]] — **本页 `stage: results` 的归属阶段页**。**本页没有把它挂进去**，**而且实测 `stages/results.md` 里 `PSAS` 0 命中**——**那一页目前不知道本页存在。**
- [[mapping-results]] — **results 段的五层对照表**（同族页，本页读过它）。**本页核过它的主表：13 行里没有一行讲 DPS 状态**，L1 列收的是 `EMAP?` / `ERMP?` / `CYRM` / `FFCI?` 那一族，**没有 `PSAS?`**。**所以本页不往那张表里加行**——那是另一件活。
- [[xps256-status-flags]] — **本页 `## DPS flag description` 里唯一那条链接的目标**。两页讲的是**同一批标志的两个面**：本页给「位号 ↔ 标志名 + 命令」，那一页给每个标志的触发 / 处置 / 可用性 / API。**本页只读了它在 wiki 上的页（作为同族页对齐），没有读它的 raw 源文档。**
- [[dps-aux-pin-task]] — 原文的 `DPS_AUX_PIN_TASK.check...()`：它出现在那条顺序约束里，原文把 `GET_FUNCTIONAL_RESULT()` 排在它前面。**本页没读那一篇**，所以「`check...()` 一族具体有哪些函数」本页没有。
- [[dps-power-flags-get-functions]] — `## Related information` 里的 `DPS power flags - get...() functions`。**只由这条链接建立关系，本页没读那篇。**
- `get-functional-result`（raw: `02.07.04.01.88_GET_FUNCTIONAL_RESULT.md`）— **顺序约束的另一半**：`GET_FUNCTIONAL_RESULT()` 必须在 `DPS_AUX_PIN_TASK.check...()` 之前执行，否则它自己的结果失效。**本页没读那一篇**，所以「结果失效之后怎么办」本页没有。
  **注意：它在 wiki 上已有页（`objects/get-functional-result.md`），但这个名字不在 `extract/prose-allowlist.txt` 里**——按 §9.1 本页用反引号写它，没有链。
- [[dpspins-resources]] — 原文三处把标志的解释指回它：bit 6（`max_voltage_drop_force`）、bit 7（`max_voltage_drop_return`）——两处都带 `For UHC4T channels in DPS operating mode`——与 bit 10（`ms_const_curr_disconnect`）。**本页没读那篇**，所以那几个**用户定义**的门限怎么设、默认多少，本页没有。
- [[dps128-dps64-cards]] — **`pinlist` 与实现表里都点名的两张卡**（原文把 `DPS128` 与 `DPS64` 写在同一个表头格里）。**本页没读那一篇。**
- [[xps256-pmu-operating-mode]] / [[xps256-programming-dps-operating-mode]] — **只在反面出现**：本页第一句列了三种 operating mode（`in DPS operating mode, in PMU operating mode, or in Digital I/O operating mode`），**而本篇没有一条链接指向它们（0 命中）**。**这条并列是按名字接的（推断）**，本页不主张内容关系。
- `sqst` / `sequencer-status` — **本页不连线**：`sequencer` 与 `SQST` 本篇各 0 命中，**`## Errors` / `## Warnings` 里也没有「sequencer 不在 OFF 就报错」那一条**。**本页照实说：本篇没有这条约束**——**这不等于「随时可用」，只是本篇没写。**
- `ganging` — **本页不连线**：`ganging` 本篇 0 命中。
- [[pqfc]] — **`msMode` 的唯一取值**：原文的 `The value of the parameter can be PQFC`。**它在原文里只是一个取值，不是一条命令**——**本页不主张那一页的内容。**
- `PSST` / `CSAS` / `PRLT` / `DC Measurement Commands` / `DPS flag description` / `DPS flag implementation` / `DPS flag reset` / `Testflow Editor` — **原文里的名字，allowlist 里没有**（raw 路径见本页「语法 / 参数」节）。

## 版本

`## Functional changes` 段有，**8 条，全部照抄**：

> 「Introduced before SmarTest 6.3.2」

> 「SmarTest 7.3.1: The command supports now pins in SIG (PMU) mode.」

> 「SmarTest 7.3.1: New bit "Low Headroom" added.」

> 「SmarTest 7.3.2: DC Scale UHC4T card added.」

> 「SmarTest 7.3.3: New extra parameter "msMode".」

> 「SmarTest 7.4.0: DC Scale AVI64 card and support for the Digital I/O operating mode of DPS added.」

> 「SmarTest 7.4.0: New flags Range overflow (Bit 13) and Clamp distance too low (Bit 14).」

> 「SmarTest 7.5.0: DC Scale FVI16 card added.」

**第一条是哨兵值，不是「6.3.2 新增了 `PSAS?`」**（schema §11.2 ②）：`before` 的意思是「在本文档集覆盖范围开始之前就已经有了」——**格式很齐整，照字面读会得出假结论。所以 `PSAS?` 真实引入的版本，语料未写。**

**三条值得单独说**：

1. **`7.3.3: New extra parameter "msMode"`** 与上面 `msMode` 那一节对得上。**7.3.3 之前的程序里没有 `PQFC` 这个写法。**
2. **`7.3.1: New bit "Low Headroom" added` 与实现表对不上**：`Low headroom` 在位表里是 **Bit 11**，而实现表里 DPS128/DPS64、UHC4T、XPS256 **三列全是 `-`**。**两处并列，本页不替它调和**（见「出处」⚠️ ⑥）。
3. **Bit 15 / Bit 16 两条 warning 没有任何版本条目**——`Voltage drop force warning` 与 `Voltage drop return warning` 在 `## Functional changes` 里 **0 命中**。**它们什么时候加的，语料未写。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.md`
（TDC `98691_2.htm`，15,937 字节，257 行）。**整篇读完**，本页引文全部来自这一篇。

> **它是同一篇的第二次投放。** 同一篇还以 `02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.md`
> 存在（`source_topic` 分别是 `98691_2.htm` 与 `98691.htm`）。**本页把两份逐字节比过**：
> **正文完全相同，唯一差别在 frontmatter 的 `source_topic` / `source_html` 两行**（§10 的「重复投放」），
> 而且**两处投放挂在两个不同的章下**（`02.06.10` 与 `02.06.02`）。
> **所以本页的文档号只写了一个，不是漏列**；数入度时两条要当一篇看。

> **另有一条值得单独记**：本篇正文里的内部链接（`status` 参数、`DPS flag description`、
> `DPS flag implementation`、`DPS flag reset`）**目标全写成 `02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.md`**
> ——**也就是说：这一份在链自己那一份的另一处投放。** 本页照实记。

**本页没做的**：

- **`PSST`（`02.06.02.02.198`）没读。** 原文 12 处点名它（`PSST ON` / `PSST OFF`），**而「connect / disconnect 到底做了什么」本页一个字没有**——本页只知道「它俩会清标志」。
- **`CSAS`（`02.06.02.02.33`）与 `PRLT`（`02.06.02.02.183`）没读。** 「`PRLT` 的结果怎么被作废」本页只有原文那一句。
- **`GET_FUNCTIONAL_RESULT()`（`02.07.04.01.88`）与 `DPS_AUX_PIN_TASK` 一族（`02.07.04.01.43.01`）没读。** 所以「代码里怎么写这条顺序、什么时候读结果」本页没有。
- **`DPSPINS resources`（`02.08.04.14.02.03.07.01`）没读。** 所以 `max_voltage_drop_force` / `max_voltage_drop_return` / `ms_const_curr_disconnect` 三个门限怎么设、默认多少，**本页一概没有**。
- **`XPS256 status flags` 那一篇的 raw 没读。** 本页只读了它在 wiki 上的页（作为同族页对齐），**所以「XPS256 侧每个标志的 Trigger / Action / Availability」本页没有照抄。**
- **`DPS128/DPS64` 卡那一篇没读**，`DC Measurement Commands` 那一章页也没读。
- **`## DPS flag description` / `## DPS flag implementation` / `## DPS flag reset` 三节没有逐格展开。** 它们在本页「语法 / 参数」节里是**逐字在的**（脚本按段标记抽的），但本页正文只做到「位号 ↔ 标志名」那一层；**三种卡的逐格差异、每个标志的适用条件，本页没有另写一遍。**
- **图：本篇文档没有内嵌图片**，所以**本页没有 ④ 图证**。
  判据可核：本篇 md 里 `png` / `jpg` / `![` **0 命中**，
  其上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\98691_2.htm`（40,484 字节）里 `<img` 与 `.png` **也 0 命中**。
  **不是「图够不着」，是这篇文档不带图**——所以「位号在测试机上怎么显示」这类问题，本页无从用图回答。
- **没有实跑。** 没有在机台上发过 `PSAS?`、没有触发过任何一位标志、没有走过 disconnect-connect 恢复。`verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`**（实测 `index.md` 里 `psas` 0 命中），也没有把本页挂进 [[results]]。
- **`## 报错条件` 节是脚本抽的**，本页一个字没动——**包括那个「一句报错 + 一句后果」的混编**（见上面「是什么」）。

> ⚠️ **本篇的语料瑕疵，照实记下、一处都没替它改**（§11.2）。
> **下面引文里的内部链接标记按 §11.1 ② 剥成纯文本**（例：raw 里 `PSST ON` 那几个字外面包着一个尖括号链接目标，引文里引成 `(PSST ON)`）。
>
> **① `Bit 14 (MSB)` 下面还有 Bit 15 与 Bit 16。** 逐字是
> `| Bit 14 (MSB):  | Clamp distance too low |`，紧随其后的是
> `| Bit 15:  | Voltage drop force warning |` 与 `| Bit 16:  | Voltage drop return warning  |`。
> **同一篇的 `## Functional changes` 写的是** `New flags Range overflow (Bit 13) and Clamp distance too low (Bit 14).`
> ——**没有 `(MSB)`**。（**推断**）`(MSB)` 是这张表还停在 bit 14 时留下的尾巴，**依据是位 15 / 16 在版本段里一条记录都没有**。**本页并列，不替它改。**
>
> **② 「特殊映射」适用的卡，两处写法不同。** `## DPS flag description` 与 Bit 8 那一格都写
> `on UHC4 and UHC4T` / `This special mapping of the bit applies only to UHC4 and UHC4T.`，
> 而文末脚注写 `Due to the hardware structure of UHC4T, flag "Safety line" is actually mapped to flag "DUT board disconnect" and flag "Safety line" will never be set. This special mapping of the bit applies only to UHC4T.`
> ——**一处收 UHC4，一处只收 UHC4T。本页照实并列。**
>
> **③ 开头说「见下面的 table」，而那一节没有表。** 逐字是
> `but the effect of a PSAS? query differs depending on the DPS card. For details see the DPS flag reset table below.`
> ——**`## DPS flag reset` 那一节里是两段散文，一张表都没有。**
>
> **④ 「为什么效果不同」两处归因不同。** 开头归给**卡**（`differs depending on the DPS card`），
> `## DPS flag reset` 归给**一个标志**（`the effect of a PSAS? is different for the "Constant Voltage" flag`）。**本页两处并列。**
>
> **⑤ `Example 4` 里标志名首字母大写，参数表里是小写。** 逐字是
> `To check if Voltage Drop Force (bit 6) or DUT Board Disconnect (bit 8) is set:`，
> 而位表里是 `Voltage drop force` / `DUT board disconnect`。**同一篇两种写法（`## Examples` 里其余各条都用小写）。**
>
> **⑥ `Low headroom`（Bit 11）三列全是 `-`，版本段却说它是 7.3.1 新增的，`## Errors` 又把它算进「会断 pin」的范围里。** 逐字三处：
> `| 11  | Low headroom  |   | -  | -  | - |`、`SmarTest 7.3.1: New bit "Low Headroom" added.`、`The status bits 4 to 11 result in a disconnect of the pin.`
> ——**三处并列，本页不替它调和。**
>
> **⑦ `pinlist` 那句没有 UHC4。** 逐字是 `Comma separated list of DPS128/64 or XPS256 pins.`，
> 而例子 1–4 用的正是 `the UHC4 pin Vcc`（`### Description` 逐字），`## DPS flag description` 与实现表也都收 UHC4T。**那一句只列了两族卡。**
>
> **⑧ 例 5 / 例 6 的返回没有 `#` 前缀，例 1 有。** 例 1 是 `PSAS #86,(Vcc)`，例 5 / 6 是
> `PSAS 2,(Vee)` 与 `PSAS 64,(Vee)`。**而 `mask` 那节说返回的是** `Hex value (hexadecimal representation of all status bits)`：
> 按十进制读，`64` = bit 6，与结论 `the DPS has hit the voltage drop force threshold.` 一致；
> 按十六进制读，`64` = 0x64 = 位 2、5、6 三位，**不只是位 6**。
> **本页把两种读法并列，不替它选哪一个是十六进制。**
>
> **⑨ `mask` 参数节里有一个空的项目符号。** 逐字是单独一行 `-`（夹在 `Integer bit mask or ALL.` 与 `Integer bit mask: Integer value is used to mask out individual status bits.` 之间）。**本页不补内容。**
>
> **⑩ 两处 `Note` 标签，一处压平、一处独立。** 压平的那处逐字以
> ` Note All DPS status flags are reset to 0 at connect` 开头（`Note` 与句子**粘成一行**，前面只有一个空格）；
> 下面另一处是**独立一行** ` Note`。**同一篇两种形态。**
>
> **⑪ `Bit 8` 那一格吞进了下一句，`Bit 16` 那一格也吞了。** 逐字分别是
> `| Bit 8:  | DUT board disconnect  | For the special mapping of bit 9 and 8 on UHC4 and UHC4T, refer to table DPS flag description below. |`
> （**注意位号写作 `bit 9 and 8`，倒序**）与
> `| Bit 16:  | Voltage drop return warning  |  If parameter mask is specified as an integer bit-mask:`
> ——**后一格的后面还跟着 `- Pass: P` 与 `- Fail: F` 两条，被算进了 Bit 16 的格子里。**
>
> **⑫ `DPS flag implementation` 的表头被拆成三行。** 逐字是
> `| Bit  | Flag  |   | DPS128` / `DPS64` / `  | UHC4T  | XPS256 |`
> ——**`DPS128` 与 `DPS64` 共用一列**，中间夹着空行，**所以这张表有几列从标题上看不出来。**
>
> **⑬ 脚注定义块挂在 `## Functional changes` 的末尾，而且脚注 2 的链接目标是空的。** 逐字是
> `[1)](<#fnsrc_1>) This applies not for DC Scale cards in Digital I/O operating mode.[2)](<>)`
> ——**它紧接在最后一条版本条目 `- SmarTest 7.5.0: DC Scale FVI16 card added.` 之后，中间没有空行**（§11.2 ③ 那一族）；**`[2)](<>)` 是一个空目标。**
>
> **⑭ `## Related information` 的四条链接首尾相接，没有分隔符。** 那四条链接的文本依次是
> `CSAS? - (Channel Slot Accumulated Status)`、`DPS_AUX_PIN_TASK.checkPowerFlags()`、
> `DPS power flags - get...() functions`、`XPS256 status flags`
> ——**四条粘成一行，相邻两条之间连一个空格都没有。**
> **注意第三条里的 `...` 是文件名本身带的**，不是省略。
>
> **⑮ 编码坏字：本篇 0 处**（按 §11.2 ① 的判据用 `[\u4e00-\u9fff]` 扫过整篇，**一个汉字都没有**）；
> **整词替换（`DC/DC power units`）本篇 0 命中**——**两条都是实测结果，不是没查。**

`verified: doc-only`
