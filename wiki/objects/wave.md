---
type: object
title: WAVE, WAVE? - (WAVEform)
layer: L1
stage: timing
tags: [timing, waveform, physical-waveform, wave, l1-command, firmware-command, fixed-timing, equation-based-timing, wavetable]
related: [wfds, wsus, dfgp, waveform-set, wavetable, timing, timing-setup-commands, pclk]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# WAVE, WAVE? - (WAVEform)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **7,863 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### WAVE

```
WAVE {wvf_set}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
WAVE {specset_id|"multiport_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}, ALLOW_EQ
```

### WAVE?

```
WAVE? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {(pinlist)}
```

returns:

```
WAVE {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
```

### Parameters

| wvf_set | Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. | Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. |
|---|---|---|
| specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no` | Derived as follows:<br><br>`100 * equation_set_no + specset_no` |
| wavetable_name | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed by double quotes. | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed by double quotes. |
| multiport_spec | To change or query a multiport specification, enter the name of the specification. | To change or query a multiport specification, enter the name of the specification. |
| wfIndex | Logical waveform index. This index identifies the logical waveform for which a physical waveform is to be created. The values specified for the DD1, DD2, ED1, and ED2 parameters must be in accordance with the format of this logical waveform. | Logical waveform index. This index identifies the logical waveform for which a physical waveform is to be created. The values specified for the DD1, DD2, ED1, and ED2 parameters must be in accordance with the format of this logical waveform. |
| DD1 and DD2 | First and second drive data parameter. These are optional parameters and contain values for both drive data and tri-state. The values you can define are: | First and second drive data parameter. These are optional parameters and contain values for both drive data and tri-state. The values you can define are: |
| DD1 and DD2 | F0N | drive 0 |
| DD1 and DD2 | F1N | drive 1 |
| DD1 and DD2 | FN0 | tri-state off |
| DD1 and DD2 | FNZ | tri-state on |
| DD1 and DD2 | F00 | drive 0, tri-state off |
| DD1 and DD2 | F0Z | drive 0, tri-state on |
| DD1 and DD2 | F10 | drive 1, tri-state off |
| DD1 and DD2 | F1Z | drive 1, tri-state on |
| ED1 and ED2 | First and second receive data parameter. These are optional parameters. The values you can define are: | First and second receive data parameter. These are optional parameters. The values you can define are: |
| ED1 and ED2 | F0 | compare to 0 |
| ED1 and ED2 | F1 | compare to 1 |
| ED1 and ED2 | FI | compare to intermediate |
| ED1 and ED2 | FX | compare to mask |
| ED1 and ED2 | FU | compare to unstable |
| ED1 and ED2 | C | capture digital data |
| ED1 and ED2 | D | do not capture digital data |
| ED1 and ED2 | The values C and D are used for selective digital capture. The following rules apply to these values:<br><br>- A waveform that is used for selective digital capture cannot contain more than one compare action. Therefore, if you specify C or D for one of ED1 or ED2, you cannot specify a value for the other Expected Data parameter.<br>- If you issue more than one instance of the WAVE command for the same logical waveform, the values you specify for the same Expected Data parameter in these different WAVE instances must be homogeneous; that is, either all or none of them must be C or D. You cannot, for instance, set ED1 to C in one of these WAVE instances, and set it to F1 in another. | The values C and D are used for selective digital capture. The following rules apply to these values:<br><br>- A waveform that is used for selective digital capture cannot contain more than one compare action. Therefore, if you specify C or D for one of ED1 or ED2, you cannot specify a value for the other Expected Data parameter.<br>- If you issue more than one instance of the WAVE command for the same logical waveform, the values you specify for the same Expected Data parameter in these different WAVE instances must be homogeneous; that is, either all or none of them must be C or D. You cannot, for instance, set ED1 to C in one of these WAVE instances, and set it to F1 in another. |
| pwfIndex | Physical waveform index. Enter an integer between 0 and 31 (0 and 255 on the Pin Scale Digital systems) for each physical waveform . The index is stored in the vector area and references the physical waveform in the physical waveform table. | Physical waveform index. Enter an integer between 0 and 31 (0 and 255 on the Pin Scale Digital systems) for each physical waveform . The index is stored in the vector area and references the physical waveform in the physical waveform table. |
| pinlist | The name of the pin or pins for which physical waveform states are to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated by commas. | The name of the pin or pins for which physical waveform states are to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated by commas. |
| ALLOW_EQ | This extra parameter allows you to define physical waveforms for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.<br><br>Note also the following:<br><br>- Every runtime change will affect all specifications that use the respective wavetable.<br>- Since the new waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.<br>- The runtime definitions are not checked for consistency. It is up to the user to ensure this. | This extra parameter allows you to define physical waveforms for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.<br><br>Note also the following:<br><br>- Every runtime change will affect all specifications that use the respective wavetable.<br>- Since the new waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.<br>- The runtime definitions are not checked for consistency. It is up to the user to ensure this. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98869.htm`。

### Example

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

This example first defines a logical waveform with the index 2 for waveform set 1. The waveform uses the data parameter D11, the fixed action 0, and the complement C11 of D11. Then two physical waveforms are defined for logical waveform 2, which are referenced by the physical waveform DC/DC power units 4 and 5. Waveform 4 drives to 0 at edge d1, to 0 at d3, and to 1 at d4. Waveform 5 drives to 1 at edge d1, to 0 at d3, and to 0 at d4.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- wvf_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- The logical waveform index is outside the range of 0-31 (for P/C/Ce systems) or 0-255 (Pin Scale systems).
- The physical waveform index is outside the range of 0-31 (0-255 on the Pin Scale Digital Cards).
- You try to define a physical waveform for which no logical waveform exists. Define the waveform first with (`WFDS, WFDS? - (WaveForm Definition String)`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）.
- There is a mismatch of action between the data parameter in the `WFDF`（raw: `02.06.02.02.334_WFDF__WFDF__-__WaveForm_DeFinition.md`） or `WFDS`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`） definition and the corresponding fixed action as specified by WAVE.
- You try to redefine a physical waveform for a waveform. Delete the waveform and any associated physical waveforms first with `WFUD - (WaveForm UnDefine)`（raw: `02.06.02.02.338_WFUD_-__WaveForm_UnDefine.md`）.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid.
- specset_id does not reference a defined wavetable.
- wavetable_name does not reference a defined wavetable.

<!-- 报错节 end -->

## 是什么

**WAVE 干的是「把逻辑波形变成物理波形」这一步。**
逻辑波形（logical waveform）只说「这个 cycle 里做哪些动作、哪些动作由哪个 data 参数决定」，
**真正送进硬件、由 sequencer 执行的是物理波形**——而物理波形就是 WAVE 定义的。原文第一句：

> 「The WAVE command defines a physical waveform in fixed timing by specifying values for the
> data parameters of a logical waveform and assigning a physical waveform index to these values.」

**两个动词说清这件事**：① **给 data 参数填上「驱 0 还是驱 1」这种具体值**；
② **给这套值分配一个物理波形号（`pwfIndex`）**。

### 为什么「没有 data 参数的逻辑波形也至少要写一条 WAVE」

这是最容易跳过、又最不能跳过的一处：

> 「Only physical waveforms are downloaded to the hardware and executed by the sequencer.
> Therefore at least one WAVE command must be issued for every logical waveform, even those
> that do not contain any data parameter.」

**理由链只有两步**：**下到硬件的只有物理波形** → **所以每个逻辑波形都得有物理波形，
哪怕它一个 data 参数都没有**。**原文写的是 `must`。**
跳过它的表现就是「逻辑波形定义了、硬件里没有」——
而 `## Errors` 里恰好有一条对着它（见「典型用法」第 1 条）。

### 逻辑波形 vs 物理波形：谁定什么

| 谁 | 定什么 | 在哪定义 |
|---|---|---|
| **逻辑波形** | 这个 cycle 里**做哪些动作**、每个动作**由固定状态还是 data 参数决定** | `WFDS` / `WFDF`（**前置**） |
| **WAVE（本页）** | **data 参数的具体物理状态** + **物理波形号** | 本命令的参数 |
| **硬件** | **只认物理波形** | — |

> 「The definition of a logical waveform specifies drive and receive actions either by a fixed
> state or by a data parameter. The fixed state actions specify the physical state of the signal
> directly. The physical states for data parameters are supplied by a call of the WAVE command.
> The physical states for drive actions are specified with the WAVE parameters DD1 and DD2, the
> physical states for receive actions with the parameters ED1 and ED2.」

**分工记住了这一句就够了**：**固定动作（fixed state）= 物理状态直接写死，不走 WAVE；
data 参数 = 物理状态留空，等 WAVE 来填。驱动侧的四个空白位是 `DD1` / `DD2`，接收侧是 `ED1` / `ED2`。**

**而「没有 data 参数」的波形要反过来写**：

> 「If the logical waveform contains no data parameters, the WAVE parameters DD1 through ED2
> must be left blank.」

**注意「留空」不是「省略」——四个逗号位还在**，
对照「语法 / 参数」节那行 `WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)`：
**`DD2` / `ED1` / `ED2` 三个位就是两个逗号之间什么都没有。**

### 哪种 data 参数配哪些固定动作（原文两张表）

**这是「填错了会报错」的那类约束**——`## Errors` 里有一条正对它：
`There is a mismatch of action between the data parameter in the WFDF or WFDS definition
and the corresponding fixed action as specified by WAVE.`

| **驱动** data 参数的形式 | 允许配的固定动作 |
|---|---|
| `D11, D22, C11, C22` | `F10, F1Z, F00, F0Z` |
| `D1N, D2N` | `F0N, F1N` |
| `DN1, DN1`（**原文如此，见「出处」⚠️ ②**） | `FN0, FNZ` |

| **接收** data 参数的形式 | 允许配的固定动作 |
|---|---|
| `EE1, EE2` | `F0, F1, FI, FU, FX, C, D` |
| `WE1, WE2` | `F0, F1, FI, FU, FX` |

**两张表读法上最要紧的一处**：**带 `C` / `D` 的行只有 `EE1, EE2` 这一条**——
这正对应下一节那条「选择性 digital capture」的规则。
**表头的原话**分别是
`The following table shows which fixed actions can be assigned to which forms of the drive data parameters.`
与 `The following table shows which fixed actions can be assigned to which forms of the receive data parameters.`

> **这两张表不在本页「语法 / 参数」节的辖区里**（脚本只逐字抽了 `## Parameters` 与 `## Example`），
> 上表是本页照原文重排的散文；**原文里它们是「一格一行、空行隔开」的压平形态**（见「出处」）。
> **要逐字核对请回 raw（第 20 行起）。**

### `DD1` / `DD2` / `ED1` / `ED2` 的取值清单

（逐值见上面「语法 / 参数」节，这里只说**语义**）

| 参数 | 取值个数 | 语义 |
|---|---|---|
| `DD1` `DD2` | **8 个**：`F0N` `F1N` `FN0` `FNZ` `F00` `F0Z` `F10` `F1Z` | 每个是「驱什么 + tri-state 什么」的组合；**没有 `N`（no action）** |
| `ED1` `ED2` | **7 个**：`F0` `F1` `FI` `FX` `FU` `C` `D` | **前 5 个是比较**（0 / 1 / intermediate / mask / unstable），**后 2 个是 capture 开关** |

**驱动侧 8 个值的构成规律**（本页按取值表归纳，**依据就是那张表本身**）：
`F0N` / `F1N` **只有 drive、不碰 tri-state**；`FN0` / `FNZ` **只动 tri-state、不 drive**；
`F00` / `F0Z` / `F10` / `F1Z` **两样都写**。

**原文对这四个参数的定性**：

> 「First and second drive data parameter. These are optional parameters and contain values for
> both drive data and tri-state. The values you can define are:」

> 「First and second receive data parameter. These are optional parameters. The values you can
> define are:」

**两句都写了 `optional`**——所以**不填是合法状态，合法到什么程度取决于逻辑波形**（上一节的留空规则）。

### 选择性 digital capture：两条硬规则

`C` 和 `D` 不是普通的比较值，原文单独给它们两条规则：

> 「The values C and D are used for selective digital capture. The following rules apply to
> these values:」

> - A waveform that is used for selective digital capture cannot contain more than one compare
> action. Therefore, if you specify C or D for one of ED1 or ED2, you cannot specify a value
> for the other Expected Data parameter.

> - If you issue more than one instance of the WAVE command for the same logical waveform, the
> values you specify for the same Expected Data parameter in these different WAVE instances must
> be homogeneous; that is, either all or none of them must be C or D. You cannot, for instance,
> set ED1 to C in one of these WAVE instances, and set it to F1 in another.

**两条规则，一句话各一条**：

| 规则 | 说的是 |
|---|---|
| **① 一个波形只能有一个比较动作** | `ED1` 用了 `C` / `D`，**`ED2` 就不能再给值** |
| **② 同一逻辑波形的多条 WAVE 之间要一致** | 同一个 ED 位上**不能一条写 `C`、另一条写 `F1`**——**要么全是 C/D，要么全不是** |

**第 ② 条是最容易踩的**：它管的不是「一条 WAVE 对不对」，而是**同一个逻辑波形的多条 WAVE
之间自洽不自洽**。而 `## Errors` 里**没有一条专门为它设的报错**
（**推断**：它会落在那条 `mismatch of action` 上，依据是两条都在讲「固定动作与 data 参数不搭」；
**原文没有把这两件事连起来说。**）

### `wfIndex`（逻辑号）与 `pwfIndex`（物理号）是两个不同的号

| 号 | 原文叫它 | 范围 | 干什么用 |
|---|---|---|---|
| `wfIndex` | **Logical waveform index** | **范围只在 `## Errors` 里给**：`0-31`（P/C/Ce）或 `0-255`（Pin Scale） | 指「给哪个逻辑波形建物理波形」 |
| `pwfIndex` | **Physical waveform index** | 参数释义给：`0 and 31`（`0 and 255 on the Pin Scale Digital systems`） | **存进 vector area，指向物理波形表里那一项** |

> 「Logical waveform index. This index identifies the logical waveform for which a physical
> waveform is to be created. The values specified for the DD1, DD2, ED1, and ED2 parameters must
> be in accordance with the format of this logical waveform.」

> 「Physical waveform index. Enter an integer between 0 and 31 (0 and 255 on the Pin Scale
> Digital systems) for each physical waveform . The index is stored in the vector area and
> references the physical waveform in the physical waveform table.」

**分工上最要紧的一点**：**`pwfIndex` 才是后来被向量引用的那个号**——
**vector 里存的不是波形内容，是这个号**（`stored in the vector area`）。
**`wfIndex` 只在这一步用一次**，之后就由物理号代表这条波形了。

**而 `wfIndex` 的范围为什么不写在参数释义里、只写在报错段里**——本篇没说（**语料未写**）。

### equation based timing：`ALLOW_EQ` 这个开关

> 「The command can also be used to create new runtime definitions of physical waveforms in an
> equation based timing.」

**equation based 下要定义物理波形就得加 `ALLOW_EQ`**：

> 「This extra parameter allows you to define physical waveforms for an equation based timing.
> Note that only the runtime settings are affected; the definitions in the wavetable are not
> changed.」

**加了它的代价，原文列了三条**（逐字）：

> - Every runtime change will affect all specifications that use the respective wavetable.

> - Since the new waveform must be evaluated and downloaded for every specification that uses
> the respective wavetable, the change tends to be rather slow.

> - The runtime definitions are not checked for consistency. It is up to the user to ensure this.

| 代价 | 后果 |
|---|---|
| **波及面** | **改了 runtime，同一个 wavetable 的所有 spec 都受影响** |
| **速度** | **每个用到该 wavetable 的 spec 都要重新求值并下载，所以慢** |
| **责任** | **这些 runtime 定义不做一致性检查，你自己保证** |

**「只改 runtime、wavetable 里的定义不动」这组措辞和 [[pclk]] 是同一个机制**——
PCLK 那句写的是 `PCLK will only change the runtime value, not the setup value specified in
the timing set`（见「和谁有关」）。

### `pinlist` 与 `@`

> 「The name of the pin or pins for which physical waveform states are to be defined or read
> back. This parameter can also include groups previously created by DFGP, DFGP? - (DeFine GrouP).
> The symbol @ can be used to specify all configured pins. If more than one pin is to be
> included, the names must be separated by commas.」

**`@` 在这里是「所有已配置的 pin」**——
**对比 [[bwdf]] / [[bwds]] 写的是 `all configured input and IO pins`**，
**同一族命令里 `@` 的展开范围并不一致，本页两处照记、不替它统一。**

## 典型用法

**1. 顺序（原文 `## Prerequisites` 那一句就是硬前提）**：

> 「The logical waveform for which physical waveforms are to be created must have been defined
> with WFDS or WFDF.」

**所以：先用 `WFDS` / `WFDF` 定义逻辑波形 → 再用 WAVE 给物理波形。**
**没有逻辑波形就 WAVE，`## Errors` 里有一条专门对着它**，
**而那条报错顺手给了修法**：原文写的是
`Define the waveform first with ([WFDS, WFDS? - (WaveForm Definition String).`
（**那个左括号没有配套的右括号，见「出处」⚠️ ⑦**）

**2. 想改一条已经存在的物理波形？先删。**

> - You try to redefine a physical waveform for a waveform. Delete the waveform and any
> associated physical waveforms first with WFUD - (WaveForm UnDefine).

**`WFUD` 那一篇本页没读**（见「出处」）——
**所以「删什么、怎么删、会不会连带删掉别的」本页只有这一句。**

**3. 原文示例（`## Example`，逐字）——一条 `WFDS` 加两条 WAVE**：

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

**先逐字读原文的说明**：

> 「This example first defines a logical waveform with the index 2 for waveform set 1. The
> waveform uses the data parameter D11, the fixed action 0, and the complement C11 of D11.
> Then two physical waveforms are defined for logical waveform 2, which are referenced by the
> physical waveform DC/DC power units 4 and 5. Waveform 4 drives to 0 at edge d1, to 0 at d3,
> and to 1 at d4. Waveform 5 drives to 1 at edge d1, to 0 at d3, and to 0 at d4.」

**再把 `WAVE` 那两行的位置对一遍**：

| 位置 | 例中的值 | 是什么 |
|---|---|---|
| 第 1 位 | `1` | `wvf_set`——waveform set 1 |
| 第 2 位 | `2` | `wfIndex`——**给逻辑波形 2 建物理波形** |
| 第 3 位 | `F00` / `F10` | **`DD1`** |
| 第 4-6 位 | `,,,,` | **`DD2` / `ED1` / `ED2` 三个位留空** |
| 第 7 位 | `4` / `5` | **`pwfIndex`**——两个物理波形的号 |
| 第 8 位 | `(pin1,pin2,pin3,pin4)` | `pinlist` |

**第 4-6 位为什么空着**：那条逻辑波形只用了 `D11` 一个 data 参数（`d1:D11`），
**所以驱动侧只需要填 `DD1`**——这和「没有 data 参数时四个位全留空」是同一条规则的连续情形。
**两个物理波形的差别全在第 3 位**（`F00` vs `F10`），
**对应说明里的 `Waveform 4 drives to 0 at edge d1` 与 `Waveform 5 drives to 1 at edge d1`。**

**4. 回读**：

```
WAVE? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {(pinlist)}
```

**注意 `WAVE?` 不带 `wfIndex`**——原文对它的一句是：

> 「The WAVE? query returns the physical waveform definitions for all logical waveforms of the
> specified or implied wavetable / waveform set.」

**一次查询回来的是「这个 wavetable / waveform set 下所有逻辑波形的物理波形定义」，不是某一条。**
`ALL` 可以写在 `wvf_set` 位：`For the query command you can also enter ALL for all waveform sets.`

**5. 四种定位方式都得指到一个真实存在的 wavetable**：`## Errors` 里最后两条说的是
`specset_id does not reference a defined wavetable.` 与
`wavetable_name does not reference a defined wavetable.`

**6. 参数填错时的自查顺序**（本页按「是什么」各节排的，**顺序本身是建议**）：

1. **逻辑波形定义了没有**（`WFDS` / `WFDF`）——没定义会报。
2. **`wfIndex` / `pwfIndex` 在不在范围里**（前者的范围只写在报错段）。
3. **data 参数与固定动作配不配**（那两张表）。
4. **用了 `C` / `D` 的话，两条 capture 规则过了没有**。
5. **要在 equation based 下定义物理波形的，`ALLOW_EQ` 加了没有。**

## 和谁有关

- [[wfds]] — **前置，本篇正文逐字点名的第一条**：
  `must have been defined with WFDS or WFDF`。**分工是「WFDS 写逻辑波形的动作序列 /
  WAVE 填 data 参数的具体值」**。**本页的取材只有 WAVE 这一篇，`WFDS` 的 raw 不在内**——
  **所以「逻辑波形的定义串怎么写」本页一个字没有。**
- [[wsus]] — **`wvf_set` 的上限来源（前置）**。本篇两处点名它：
  `The maximum number is determined by WSUS, WSUS? - (Waveform Sets USed).` 与 `## Errors` 第一条。
- [[waveform-set]] / [[wavetable]] — **WAVE 的作用域（同类）**。`wvf_set` 是 waveform set 号，
  `WAVE?` 回的也是 `all logical waveforms of the specified or implied wavetable / waveform set`。
  **两个概念的正文在各自页里**，本页只保证本篇这么用了这两个词。
- [[dfgp]] — **pinlist 的另一种写法（并列）**：
  `This parameter can also include groups previously created by DFGP, DFGP? - (DeFine GrouP).`
  **DFGP 那一篇本页没读。**
- [[timing]] — **`stage: timing` 的阶段页**。本页是它 L1 表里
  `fixed timing 路线：逐个元素定义 edge / period / waveform` 那一行中的 `waveform` 一环
  （**本页读到的 wiki 页**）。
- [[timing-setup-commands]] — **上游入口**。本篇 `## Application` 全文一句：
  > 「Timing setup, see Timing Setup Commands.」
  **本篇没有说 WAVE 在 timing setup 流程里排第几步**，也没有说它和 [[pclk]] 谁先谁后。
- [[pclk]] — **同族姊妹命令（并列）**。**本篇一次没提 `PCLK`**；
  「同族」的依据是 [[timing]] 阶段页把它们列在同一个 L1 单元里（**本页读到的 wiki 页**）。
  **两篇有一处措辞上的呼应值得记**（两句都是各自文档里的逐字引文）：
  本篇的 `ALLOW_EQ` 说 `only the runtime settings are affected; the definitions in the wavetable
  are not changed`，而 [[pclk]] 说 `PCLK will only change the runtime value, not the setup value
  specified in the timing set`——**同一个「只改 runtime」的机制，两篇各说一遍。**
- [[bwdf]] / [[bwds]] — **同族的另外两条（并列）**。**本篇一次没提它们**；
  它们讲的是 break waveform（只许 drive 动作、不许 data 参数），**与 WAVE 的 `DD` / `ED`
  机制是两套东西**。**两篇的 raw 不在本页取材内**——
  上面那句「`@` 的展开范围不一致」是本页按各自页的「语法 / 参数」节对照出来的，**已标在正文里**。
- `WFDF` / `WFUD`（**均未建，故用反引号，§9.1**）— 本篇点名的另两条同族命令：
  **`WFDF` 也能定义逻辑波形**（`must have been defined with WFDS or WFDF`），
  **`WFUD` 负责删除**（`Delete the waveform and any associated physical waveforms first with
  WFUD - (WaveForm UnDefine).`）。**两篇的 raw 本页都没读。**
- `Specifying the actions`（**未建**）— `## Related information` 一节里的三条链接之一。
  **本页没读**，**所以「动作怎么归类、怎么写」本页没有。**

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 WAVE」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 WAVE」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「物理波形号的范围哪一版从 31 扩到 255」「`ALLOW_EQ` 是哪一版加的」在本篇里查不到**——
**而 `ALLOW_EQ` 讲的是 equation based timing 下的运行时改写，看起来正是会被记进版本段的那类功能，
本篇没有记。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`
  （frontmatter 的 `source_topic` 是 `98869.htm`；**12,059 字节 / 384 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **`## Mode of operation` 里那两张「data 参数 × 固定动作」表不在「语法 / 参数」节的辖区里。**
  脚本只逐字抽了 `## Parameters` 与 `## Example`。**本页那两张表是照原文重排的散文，不是逐字抽取**——
  原文里它们是「一格一行、空行隔开」的压平形态（`|` 与内容分行，中间夹空行），
  连「连续 ≥3 行管道行」都算不上。**要逐字核对请回 raw（第 20 行起）。**
- **`WFDS` / `WFDF` / `WFUD` / `WSUS` / `DFGP` 五篇都没读。** 它们都只是本篇点名的邻居：
  **逻辑波形定义串怎么写（WFDS / WFDF）、怎么删（WFUD）、上限怎么算（WSUS）、
  group 怎么建（DFGP），本页全无。**
- **`Specifying the actions` 没读**——所以「动作分哪些类」本页只有本篇那两句的措辞。
- **`Timing Setup Commands` 那一篇没读。** 本篇 `## Application` 只给了它的标题。
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **「物理波形表长什么样」「`C` / `D` 的 capture 具体抓什么」本页只有文字（§11.4）。**
- **没在机台上跑过 `WAVE` / `WAVE?`**（`verified: doc-only`）。
  **所以「同一个逻辑波形的第二条 WAVE 真会被拒吗」本页答不了（§11）。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的九条——不是漏写。
- **`break waveform` 与本页无关**（那是 [[bwdf]] / [[bwds]] 的对象），
  **本页没有一句讲它——这是取材边界，不是遗漏。**

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`（**本页的出处**） | `98869.htm` | 9,048 | — |
| `02.06_Command_Reference/02.06.06.02.40_WAVE__WAVE__-__WAVEform.md` | `98869_2.htm` | 9,049 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.40_WAVE__WAVE__-__WAVEform.md` | `98869_3.htm` | 9,411 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① `DC/DC power units` 是 §11.2 ⑤ 那一族「整词替换」损坏。**
> 原文 `## Example` 的说明里写的是
> `referenced by the physical waveform DC/DC power units 4 and 5`——
> **`DC/DC power units` 应为 `index`**（那一句讲的是 `pwfIndex`，也就是物理波形号）。
> **判据**：它出现在本该是 index 的位置（`physical waveform ___ 4 and 5`），
> 而**正确的形态 `pwfIndex` 在同一篇的参数表里活着**。
> **代价写清楚：拿 `physical waveform index 4 and 5` 去 raw 里搜是搜不到的，要搜坏掉的形态。**
> **⚠️ 这一处同时出现在本页「语法 / 参数」节里（脚本逐字抽的）——那一节本页一个字没动（§4）。**
> **② `DN1, DN1` 是重复词。** 驱动 data 参数表第三行的原文是 `DN1, DN1`，
> **第二个按同表规律应为 `DN2`**（**推断**，依据是同表的 `D1N, D2N` 与另一张表的
> `EE1, EE2` / `WE1, WE2` 都是「1 配 2」的成对写法；**原文没有一句说明**）。
> **§11.1 明令不许合并重复词，本页照原样引。**
> **③ 同一类硬件三种叫法。** `pwfIndex` 那一栏写 `Pin Scale Digital systems`、
> `## Errors` 第二条写 `Pin Scale systems`、第三条写 `Pin Scale Digital Cards`——
> **三个词指同一类系统，本篇不替它统一。**
> **④ 链接文字不齐。** 同一篇里 `WFDS` / `WFDF` 用短名，
> 而 `WSUS, WSUS? - (Waveform Sets USed)` / `DFGP, DFGP? - (DeFine GrouP)` /
> `WFUD - (WaveForm UnDefine)` 用全名（**`WFUD` 那条连逗号都没有**）；
> `## Related information` 一节更是**三条链接首尾相连、中间没有分隔符**。**本页照原样引。**
> **⑤ 一处排版毛病**：`for each physical waveform .`——**句点前多一个空格**（本页正文引了整句，照抄）。
> **⑥ 一处拼写/语法毛病**：参数释义第一句是 `Waveforms set number.`——**`Waveforms` 多了个 s**
> （同篇别处写的是 `waveform set` / `Waveform Set`）。
> **⑦ 报错段里一个左括号没有闭合**：原文是
> `Define the waveform first with (WFDS, WFDS? - (WaveForm Definition String).`
> ——**这一处在「报错条件」节里，本页一个字没动（§4）。**
> **⑧ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
