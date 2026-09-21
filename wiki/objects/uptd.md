---
type: object
title: UPTD, UPTD? - (UP To Date)
layer: L1
stage: level
tags: [uptd, firmware-command, up-to-date-flag, device-file-sync, status-query, hardware-vs-file]
related: [dscp, conf, dfpn, pclk, pslv, drlv, rclv, pin-configuration-tool, equation-based-level-setup, test-program-explorer, smartest-7.2.0]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# UPTD, UPTD? - (UP To Date)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **196 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

```
UPTD? CONF
```

This example requests if the pin configuration data has been changed since the file was last loaded or saved. If the data has not changed, the response is:

```
UPTD CONF,1
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if you specify a flag other than 0 or 1.

<!-- 报错节 end -->

## 是什么

**`UPTD` 管的是「硬件里的数据，和当前 device 文件还对得上吗」。** 原文两句逐字：

> 「The UPTD (UP To Date) command allows you to declare a given setup, result or command set as
> up to date or out of date.」

> 「The UPTD? query allows you to read if the data in hardware has been changed since the current
> device file was last saved or loaded. A 1 or a 0 is returned. At power-on or after use of the
> *RST or DSCP commands, all the flags are set to 0.」

**分工是「写」与「读」两件事**：`UPTD` **声明**（把某一类数据标成 up to date 或 out of date），
`UPTD?` **读回**（返回 `1` 或 `0`）。

**读的到底是什么**：`the data in hardware has been changed since the current device file was last
saved or loaded` —— **硬件里的数据，自从当前 device 文件上次保存或加载以来有没有变过。**

**两个起点会把所有 flag 清零**：**power-on**，以及**用过 `*RST` 或 `DSCP` 之后**。

### `flag` 只有两个值

原文 `## flag` 一节逐字：

> - 1: The specified device file is identical to the data currently used in hardware.
> - 0: The specified device file differs from the data currently used in hardware.

**`1` = 文件与硬件一致；`0` = 不一致。**

### `status` 是 27 个选项，每个盯一类数据

**27 格里，`ALL` 加 26 个具名项**（**这 27 个是本页从原文 `## Parameters` 转述的，
不是语法节抽的**——见 `## 出处` ①）：

| # | `status` | 盯的数据（**原文**） | 谁把它设成 0 |
|---|---|---|---|
| 1 | `ALL` | `The status of all options` | `PADS`（for 14 edge setups）、`DFPN`、`CONF`（**原文这一格措辞有问题，见 `## 出处` ⑤**） |
| 2 | `ANA` | analog control data | — |
| 3 | `APPL` | production test application data file | — |
| 4 | `ATR` | edge attributes setup | `PCLK`、`DFPN`、`CONF` |
| 5 | `CAL` | calibration data | — |
| 6 | `CNFG` | production test configuration | — |
| 7 | `CONF` | pin configuration setup | **`Pin configuration setup commands` 整章** |
| 8 | `DFRM` | Data Bridge Command Set | **← 见下「四个 Command Set」** |
| 9 | `DPS` | power supply setup | `equation based level setup`、`PSLV`、`Pin configuration setup commands` |
| 10 | `DSET` | data set | — |
| 11 | `EDA` | CAE link files | — |
| 12 | `ERMP` | Error Map files | — |
| 13 | `FLOW` | production testflow file | — |
| 14 | `LEV` | level setup | `equation based level setup`、`Pin configuration setup commands`、`Level Setup Commands` 整章 |
| 15 | `PDL` | path delay data | `SATR`、`FXDL`、`DFPN`、`CONF` |
| 16 | `PRBH` | Prober/Handler Command Set | **← 见下「四个 Command Set」** |
| 17 | `PRCS` | Execution Input Command Set | **← 见下「四个 Command Set」** |
| 18 | `PROG` | production test program file | — |
| 19 | `REP` | report window data | — |
| 20 | `ROUT` | routing setup | — |
| 21 | `SLST` | state list files | — |
| 22 | `TIM` | timing setup | `CONF`、`DFPN`、`Timing Setup Commands` 整章 |
| 23 | `TMDG` | timing diagram files | — |
| 24 | `USRP` | User Procedure Command Set | **← 见下「四个 Command Set」** |
| 25 | `VEC` | vector and sequencer setup | `DFPN`、`CONF`、`Vector Setup Commands` 整章 |
| 26 | `WAFR` | wafer description file | — |
| 27 | `WAVE` | waveform definition data | — |

**这张表里有一处不是同一句话套出来的**，**本页单独拎出来**：

**四个 Command Set（`DFRM` / `PRBH` / `PRCS` / `USRP`）的 flag 语义与其余 23 个相反。**
其余 23 个一律是「数据变了 → `0`，保存或加载后回 `1`」；
**这四个反过来**：**名字被改 → `0`**，**进程成功加载并运行 → `1`**。
逐字（`DFRM` 那格，另外三格同构）：

> 「The status of the Data Bridge Command Set is returned. When the Command Set name is changed,
> the flag is set to 0. When the Command Set process is successfully loaded and running, the flag
> is set to 1.」

**即：这四个盯的不是「文件与硬件一致」，而是「那个进程有没有在跑」。**
**同一张表里混了两种判据，原文没有把这四个单独分节。**

**另外 8 格（`ALL` / `ATR` / `CONF` / `DPS` / `LEV` / `PDL` / `TIM` / `VEC`）
点名了会触发它们的命令或整章命令**，**其余 15 格（`ANA` / `APPL` / `CAL` / `CNFG` / `DSET` /
`EDA` / `ERMP` / `FLOW` / `PROG` / `REP` / `ROUT` / `SLST` / `TMDG` / `WAFR` / `WAVE`）
只描述了「哪类数据」，没有说谁会让它变。**
**这是本页能从原文落下的唯一一处分类，原文没给这个分法命名。**

### 一条 `Note`：`DPS` 与 `LEV` 是同步的

原文那一行**以 `   | ` 开头**（表格残留，见 `## 出处` ③），逐字：

> 「Note The status of the DPS and LEV parameters is kept synchronized when modified via the pin
> configuration tool or by equation based level setup. Only the commands PSLV (Power Supply LeVel),
> DRLV (DRive LeVel), or RCLV, RCLV? - (ReCeive LeVel) allow to unsychronize their status.」

**两条**：

- **走 [[pin-configuration-tool]] 或 [[equation-based-level-setup]] 改 → `DPS` 与 `LEV` 保持同步。**
- **只有 [[pslv]] / [[drlv]] / [[rclv]] 三条命令**能让两者的状态不同步
  （**原文的 `unsychronize` 少一个 `n`，见 `## 出处` ②**）。

**表里 `DPS` / `LEV` 两格列的触发命令是同一套**（都含 `equation based level setup` 与
`Pin configuration setup commands`）——**与这句 `Note` 是一致的**。

### `Application`

原文 `## Application` 只有一句两个词：`Test Program Explorer.`
——**（推断）本命令属于 Test Program Explorer 那一侧的使用场景**；
**依据只是这一句，原文没有解释它为什么归在那儿。**

### `Errors`

原文 `## Errors` 只有一句（**已在报错节里逐字**）：
`An error is generated if you specify a flag other than 0 or 1.`
——**只管 `flag` 的取值范围，不管 `status`**。
**给一个不存在的 `status`（比如 `UPTD? XXXX`）会怎样，原文没说。**

## 典型用法

**原文有 `## Example`（已在语法节里逐字），没有 `## Procedure`、没有 `## Before you begin`。**
例子是两段代码块，逐字：

```
UPTD? CONF
```

> 「This example requests if the pin configuration data has been changed since the file was last
> loaded or saved. If the data has not changed, the response is:」

```
UPTD CONF,1
```

**注意回的是什么**：问的是 `UPTD? CONF`（一个参数），**回的是 `UPTD CONF,1`**——
**把 `status` 和 `flag` 一起带回，且命令名后面**没有**问号**（与 [[dscp]] 那页 `DSCP?` 的行为一致）。

**两条语法只在参数个数上不同**（原文 `## UPTD` / `## UPTD?` 两节的代码块，**不在语法节里**）：

| 动作 | 语法（原文） | 参数个数 |
|---|---|---|
| 声明 | `UPTD {status}, {flag}` | **两个** |
| 查询 | `UPTD? {status}` | **一个** |
| 查询返回 | `UPTD {status}, {flag}` | **两个** |

**从原文能落成的动作：**

| 要做的 | 依据 |
|---|---|
| **问某一类数据变没变** | `UPTD? {status}`，`status` 取上表 27 个之一 |
| **一次问全部** | `status` 用 `ALL` |
| **把某类数据标成「与硬件一致」** | `UPTD {status}, 1` |
| **把某类数据标成「与硬件不一致」** | `UPTD {status}, 0` |
| **想重新开始** | power-on，或用 `*RST` / [[dscp]]——**所有 flag 归 `0`** |
| **要避免 flag 被误触** | 避开上表「谁把它设成 0」那列的八格命令（`CONF` / `DFPN` 出现次数最多，各五次） |
| **想只改 DPS 而不动 LEV（或反之）** | 用 [[pslv]] / [[drlv]] / [[rclv]] 之一——**其余路径都会让两者同步**（见上 `Note`） |
| **提交 `flag` 之前** | 只有 `0` 和 `1` 合法，别的报错（见上 `Errors`） |

**一处本页要提醒的**：`UPTD` 是**写**、`UPTD?` 是**读**，
**但 `## flag` 一节的措辞是 `Sets or returns the up-to-date status`**，
**把两个动作放在了一个参数上**——**原文没有说明「声明」这个动作到底改了哪一侧**
（改硬件？改文件？还是只改这个 flag 本身）。
**本页不做推断，`## 出处` ⑦ 记下这个空缺。**

## 和谁有关

- [[dscp]] — **原文点名的两个「把所有 flag 归 0」的起点之一**：
  `At power-on or after use of the *RST or DSCP commands, all the flags are set to 0.`
  **本页只有这一句；[[dscp]] 那页记的是「每调一次就删掉 Sequencer Memory 里原有数据」。
  两页说的是同一个动作的两个后果，但两篇原文都没有互相引用。**
- [[conf]] — **触面最广的一条**：`ALL` / `ATR` / `PDL` / `TIM` / `VEC` **五格**都点了它。
  **本页只有它在哪几格出现，`CONF` 自己改什么在那一页。**
- [[dfpn]] — 同上，**也是五格**（`ALL` / `ATR` / `PDL` / `TIM` / `VEC`）。
- [[pclk]] — 只在 `ATR` 那一格出现。
- [[pslv]] / [[drlv]] / [[rclv]] — **原文点名「只有这三条」能让 `DPS` 与 `LEV` 的状态不同步**。
  **本页只有「这三条是例外」这一个事实，它们各自做什么在那三页。**
- [[pin-configuration-tool]] / [[equation-based-level-setup]] — **两条保持 `DPS`/`LEV`
  同步的路径**。**本页只有「走这条路会同步」，那两处各自怎么改值在本页没有。**
- [[timing-setup-commands]] — `TIM` 那一格点名的整章命令。
- [[test-program-explorer]] — **原文 `## Application` 唯一的一句**。
  **本页只有这个归属，那页怎么用本页没读。**
- [[alphabetical-list-of-flags]] — **（推断）名字近、所指未必同物**。
  本页的 `flag` 是 0/1 两值状态位；**那个清单页收的是哪一类 flag，
  原文两篇都没有互相引用，本页没有依据判断是不是同一批。** **按页名相邻列出，不代表同物。**
- `PADS`（**未建**）— `ALL` 那格点它。**注意那一格的括注本身是坏的**
  （`PADS` 后面没有空格就直接接了 `for 14 edge setups`），**见 `## 出处` ⑤**。
  **不在 allowlist，用反引号。**
- `SATR` / `FXDL`（**未建**）— `PDL` 那格点名的两条命令。
- `*RST`（**未建**）— **另一个清零起点**，原文与 [[dscp]] 并列。
- `PATR`（**未建，且原文没解释**）— `ALL` 那格里出现一次，
  **和 `PADS` 并列在同一句里，原文没说它是什么**（见 `## 出处` ⑤）。
- `Pin configuration setup commands` / `Level Setup Commands` / `Vector Setup Commands`
  （**三章，均未建**）— **`CONF` / `LEV` / `DPS` 与 `TIM` / `VEC` 那几格点名的整章**。
- `Data Bridge Command Set` / `Prober/Handler Command Set` / `Execution Input Command Set` /
  `User Procedure Command Set`（**四个，均未建**）— **flag 语义相反的那四格的所指**。
  **原文没有说明 Command Set 是什么、怎么 load。**
- `CAE link files` / `data set` / `state list files` / `report window data`
  （**均未建**）— 那 15 个「只描述数据、不说谁改它」的格子里的一部分。

## 版本

`## Functional changes` **四条，逐字**：

- Introduced before SmarTest 6.3.2
- SmarTest 7.0.3: BIT and FAM are no longer supported
- SmarTest 7.0.3: TSTF are no longer supported due to the obsoletion of standard test functions.
- SmarTest 7.2.0: Removed the SHMO parameter

**第一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 `UPTD` 本身成立于哪个版本，这份语料里没有。**

**后三条清一色是「减法」**：7.0.3 去掉 `BIT`、`FAM`、`TSTF`，7.2.0 去掉 `SHMO`。

**（推断）这四个名字当年属于 `status` 选项或 `flag` 一侧的参数**——
**依据只是：本篇 `## Parameters` 的 27 个选项里一个都没有它们**，
**原文既没说它们属于哪一侧，也没说去掉之后用什么替代。这是推断，不是原文明写的。**

**（推断）语料里的 `status` 表已经是「去掉之后」的状态**——
同上，依据只是表里没有它们；**原文没有一句话把版本段和参数表对上。**

**与 wiki 目标版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
而这一篇**最后一条是 7.2.0**，之后八个小版本没有任何条目——
**所以 `UPTD` 在 7.2.0 到 7.10.3 之间有没有再变，语料里没有依据。**

**版本段里没有 `UPTD?` 的条目**，**尽管查询与声明是同一篇文档的两节**。

详见 [[smartest-6.3.2]] / [[smartest-7.0.3]] / [[smartest-7.2.0]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.md`

**本页没做的：**

- **27 个 `status` 选项的说明文字，是本页从原文 `## Parameters` 转述的，不是语法节抽的。**
  语法节里**只有 `### Example` 一节**（脚本抽到的段就这一个），
  **原文的 `## UPTD` / `## UPTD?` 两个代码块、`## Parameters` 整张表、`## Application`
  都没进语法节**（`## Errors` 进了报错节）。
  **所以上表里 `盯的数据` 那一列是转述——要精确到原文措辞，得回原文第 32–288 行。**
- **`## UPTD` / `## UPTD?` 两条语法行也是本页从原文正文转述的**（同上）。
- **`PADS` / `SATR` / `FXDL` / `PATR` / `*RST` 都没读**（前四个原文也没解释），
  **所以「谁把它设成 0」那几格里的命令各自做什么，本页一个字都没有。**
- **[[pin-configuration-tool]] / [[equation-based-level-setup]] 没读** ——
  **所以 `DPS` 与 `LEV`「同步」在实现上意味着什么、不同步之后会怎样，本页没有。**
- **四个 Command Set（`DFRM` / `PRBH` / `PRCS` / `USRP`）没读，原文也没解释它是什么** ——
  **所以那四格「load 并运行」这个动作怎么做、谁发起，本页不知道。**
  **本页只能指出这四个的判据与其余 23 格不同。**
- **`Test Program Explorer` 没读** —— `## Application` 只有一个名字，
  **本命令在它那里怎么用，本页没有。**
- **「声明」这个动作改了哪一侧，本页没有** —— 原文 `## flag` 写
  `Sets or returns the up-to-date status`，**把读和写放在同一个参数上，
  没有说明设置 flag 会不会动到硬件或文件本身**（见 `## 出处` ⑦）。
- **给一个不存在的 `status` 会怎样，本页不知道** —— `## Errors` 只管 `flag` 的取值。
- **一张图都没有。** 原文没有图片。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：本页 `layer: L1`、`stage: level`，这个归属是本页照 wiki 的既有划分填的，
  不是本篇文档写出来的**——**原文 `## Application` 只说 `Test Program Explorer.`**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 语法节只抽到 `### Example`。** 原文的 `## UPTD` / `## UPTD?` / `## Parameters` /
> `## flag` / `## Application` 五节**都没进语法节**。
> **所以本页正文里那 27 格的说明、两条语法行，全部是转述，不是逐字。**
> **这一条是本页最大的出处限制。**
>
> **② `unsychronize` 是原文的拼写。** 逐字：
> `allow to unsychronize their status.`
> ——**少一个 `n`**（应为 `unsynchronize`）。**同一句里 `synchronized` 又拼对了。**
> **本页引文照原样。**
>
> **③ `Note` 那一行以 `   | ` 开头，是表格残留。** 逐字（**注意开头的三个空格与竖线**）：
> `   | Note The status of the DPS and LEV parameters is kept synchronized …`
> ——**`Note` 被塞进了一行残破的表格单元里，`Note` 后面也没有分隔符。**
> **本页引文照原样，正文里当普通段落写。**
> **（与 [[dscp]] 那篇同位置对照：[[dscp]] 页记的是那里的 `Note` 行首多一个空格。
> 那一条本页引自 wiki 的 [[dscp]] 页、不是本篇 raw，两篇 raw 本页没有互校。）**
>
> **④ 版本段提到的四个名字，在参数表里一个都没有。** `BIT` / `FAM` / `TSTF` / `SHMO`
> 只在 `## Functional changes` 出现；**`## Parameters` 的 27 个 `status` 选项里没有它们。**
> **原文没说它们当年属于 `status` 还是 `flag`，也没说取代者是谁。本页并列两处，不替它编。**
>
> **⑤ `ALL` 那一格的括注是坏的。** 逐字节录（**这一条是本页唯一保留原始 markdown 链接的引文**——
> 因为坏掉的正是链接和括号这一段，改写成 `文本（raw: 路径）` 会把要指出的瑕疵抹掉）：
> `Use of the PATR ([PADS](<02.06.02.02.172_PADS__PADS__-__Pin_Attributes_Definition_String.md>)for 14 edge setups), [DFPN (DeFine Pin Name)](<02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md>), or [CONF (CONFiguration)](<02.06.02.02.31_CONF__CONF__-__CONFiguration.md>) commands sets the flag to 0 until the setup is saved or loaded.`
> ——**`PATR` 在本篇别处一次都没出现，原文也没解释它是什么**；
> **而 `for 14 edge setups` 紧贴在 `[PADS](…)` 的收尾 `)` 后面、中间没有空格**，
> **所以这句读起来是 `(PADSfor 14 edge setups)`——`PATR` 后面那个 `(` 没有对应的 `)`**。
> **同一句里并列了三个命令名，只有中间那个的括注是完整的。**
> **本页照实说，不替它补 `)`、也不替 `PATR` 编身份。**
>
> **⑥ `## Application` 只有两个词，没有动词。** 逐字：`Test Program Explorer.`
> ——**本篇的 `Application` 短到不足以独立成句。**
> **（[[dscp]] 页也记了同位置的短句，那一条本页引自 wiki 页、不是本篇 raw。）**
>
> **⑦ 「声明」这个动作的作用面，原文没说。** `## flag` 一节逐字：
> `Sets or returns the up-to-date status:` ——
> **`Sets` 与 `returns` 共用一个参数说明，而 `## UPTD`（写）与 `## UPTD?`（读）是两节。
> 设置 `flag` 会不会改变硬件、会不会改变 device 文件、还是只改这个状态位本身，
> 原文一个字都没有。本页不推断。**
>
> **⑧ 27 个 `status` 选项里，15 个没有「谁会改它」的信息。**
> 原文那 15 格的说明是**同一个句式、只换主语**——以 `analog control data` 那格为例，逐字：
> `The status of the analog control data is returned. When analog control data has changed the flag is set to 0 until the changed data is saved or loaded.` ——
> **把主语换成任何一类数据都成立，等于没给操作入口。本页照实列成 `—`。**
>
> **⑨ 全文没有 `## Related information` 一节。** （[[dscp]] 那篇有，且那一节里两个链接
> 还是粘在一起的。）**本篇一个站外/站内链接清单都没有**——
> **命令之间的全部关系都散在 `Parameters` 表格的说明文字里。**
>
> **⑩ 本篇没有 §11.2 ① 那种 `鈥` 形态的编码损坏**（本页查过，0 处）。

`verified: doc-only`
