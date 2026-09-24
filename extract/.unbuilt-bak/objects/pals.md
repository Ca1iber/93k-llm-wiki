---
type: object
title: PALS, PALS? - (Pin ALlocation for multiple Sites)
layer: L1
stage: pin
tags: [pals, pin-allocation, site, channel, dc-scale, master-slave, ganging, dfpn, setup-order, pin-configuration]
related: [dfpn, conf, pals-before-other-setup, ganging, cross-card-ganging-requires-ddic, dc-scale-uhc4t-card, dfut, pin-configuration-tool, smartest-7.1.3, smartest-7.5.0]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# PALS, PALS? - (Pin ALlocation for multiple Sites)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,199 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PALS

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

### PALS?

```
PALS? {site}, {(pinlist)}
```

returns:

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

### Parameters

|

site

 |

The site parameter is an integer that defines the number of the site where the channels are to be defined.

The integer must be greater than 1 (channels for site 1 are defined by the command `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）.

When specified as part of the PALS? query, you can use the parameter ALL to read the channel allocation for all sites or the parameter PEND to read the pending channel allocation.

 |
 |

channel_1

 |

This parameter specifies the test system channel used in the specified site for the pin.

For a digital or DC Scale channel, specify it with the test system channel number, which is five digits.

See `DFPN, DFPN? - (DeFine Pin Name)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） for the channel number.

For utility lines, see `DFUT, DFUT? - (DeFine UTility line)`（raw: `02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md`） for the channel number.

 |
 |

DC_scale_channels_list

 |

You can define a Master/Slave configuration for DC Scale channels by specifying a list of DC Scale channels, separated by commas and enclosed by parentheses. The first channel is the master.

For UHC4 / UHC4T the channels must be physically adjacent on the same board, or be the last (the 4th) channel of a board and the first of another UHC4 / UHC4T board. You cannot gang UHC4 and UHC4T boards. Before ganging between boards can be used, the connection must be enabled by `DDIC`（raw: `02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md`）.

 |
 |

channel_2

 |

The optional parameter is currently not used.

 |
 |

pin

 |

This defines the name of the pin.

 |
 |

pinlist

 |

The names of the pins to be allocated to the pin.

The query returns the name of the pin allocated to each channel. The symbol @ can be used with the PALS? command to list all pins previously defined by the PALS command. If a list of more than one pin is required, the pin names must be separated with a comma. If you query a non-existent pinlist, the system returns nothing.

 |

### Examples

```
PALS 2,10201,,(Clock)
PALS 2,10202,,(D0)
```

The above example allocates the Clock pin for site 2 to channel 10201 and allocates pin D0 for site 2 to channel 10202.

```
PALS 2,(10101, 10102),,(dc1)
```

This example defines a master/slave configuration for DC Scale channels. The first channel is the master.

```
DDIC CONN, (104GO, 105GI)
DDIC CONN, (105GO, 107GI)
PALS 2,(10403, 10404, 10501, 10502, 10503, 10504, 10701, 10702),,(dc1)
```

This example defines a master/slave configuration for DC Scale UHC4 channels across boards. The first channel is the master.

```
DFAN "MCE231,2,i","",(av8_bbrx_b+)
DFAN "MCE231,6,i","",(av8_bbrx_b-)
PALS 2,"MCE231,1,i",,(av8_bbrx_b+)
PALS 3,"MCE231,3,i",,(av8_bbrx_b+)
PALS 4,"MCE231,4,i",,(av8_bbrx_b+)
PALS 2,"MCE231,5,i",,(av8_bbrx_b-)
PALS 3,"MCE231,7,i",,(av8_bbrx_b-)
PALS 4,"MCE231,8,i",,(av8_bbrx_b-)
```

This example defines a pair of differential pins av8_bbrx_b+ and av8_bbrx_b- using the MCE card in 4 sites.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The specified channel number is not valid;
- The specified channel is not installed;
- The specified pin name is already used as a group name;
- The sequencer is in RUN or BREAK mode.

<!-- 报错节 end -->

## 是什么

**`PALS` 是「给 site 1 **以外**的 site 分配通道号」的命令。**

> 「The PALS command defines the channel numbers for pins on sites other than site 1.」

> 「Channels for site 1 are defined with DFPN.」

**这条分工是本页的第一块基石**：

| site | 用哪条命令分配通道 |
|---|---|
| **site 1** | **`DFPN`**（`DFPN, DFPN? - (DeFine Pin Name)`） |
| **site 2 及以上** | **`PALS`** |

**所以「多 site 的引脚分配」是**两条命令**合起来干的一件事，
本页只管其中除 site 1 之外的部分。**参数表里 `site` 那一格把这条又写了一次：
**`The integer must be greater than 1`**。

### 第二块基石：**`PALS` 有执行**顺序**上的硬要求**

> 「Note that PALS must be used before any other setup command (including CONF).」

**这句是本页最要紧的一句**——**`PALS` 必须在**任何**其它 setup 命令之前**，
**原文还特意把 `CONF` 点名放进括号里强调。**
**含义是：引脚到通道的分配决定了后面一切 setup 的落脚点，所以它得先定。**
（**推断**：括号里那句「包括 CONF」是原文给的**唯一**例证，
**「为什么必须最先」原文没说**——本页这句解释是本页的推断。）

### 两个语法行

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

```
PALS? {site}, {(pinlist)}
```

returns：

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

**⚠️ 括号的用法在这一行里**不统一**，读语法行时要小心**（**本页的观察，原文没有解释**）：

| 位置 | 括号 | 例子里的实际形态 |
|---|---|---|
| `site` | `{}` | **总是要给**（四段示例都给） |
| `channel_1` 或 `(DC_scale_channels_list)` | `{}` **包住一个竖线二选一** | **要么给一个五位数，要么给一对圆括号包的通道表** |
| `channel_2` | **`[]`（可选）** | **四段示例里全是空的**——写成两个连续的逗号 |
| `pin` | **`{(pin)}`** | **给的是圆括号包的引脚名** |

**`{}` 同时用在「必给」和「引脚」两处，而 `[channel_2]` 用 `[]` 表示可选**——
**同一套记号里 `{}` 和 `[]` 的分工**只在 `channel_2` 那一处**看得出来。
**`(pin)` 与 `pinlist` 都是圆括号包的**——**含义是「可以是一串」，不是「可选」。**

### 六个参数（**原文参数表全文，一格不漏**）

原文的参数表是一张被拆成「一格一行」的大表（见「出处」⚠️①）。**六个参数：**

| 参数 | 原文（逐字要点） |
|---|---|
| **`site`** | **`The site parameter is an integer that defines the number of the site where the channels are to be defined.`** + **`The integer must be greater than 1`** + **查询侧的 `ALL` / `PEND`（见下）** |
| **`channel_1`** | **`This parameter specifies the test system channel used in the specified site for the pin.`** + **`For a digital or DC Scale channel, specify it with the test system channel number, which is five digits.`** + 两个指路：**`DFPN`**（通道号怎么查）与 **`DFUT`**（utility line 怎么查） |
| **`DC_scale_channels_list`** | **Master/Slave 配置**——**一串 DC Scale 通道，逗号分隔、圆括号包住，第一个是 master**；**UHC4 / UHC4T 的相邻性规则与跨板条件（见下）** |
| **`channel_2`** | **`The optional parameter is currently not used.`** |
| **`pin`** | **`This defines the name of the pin.`** |
| **`pinlist`** | **`The names of the pins to be allocated to the pin.`** + 查询语义 + **`@`** + 逗号分隔 + 查不到就什么都不回（见下） |

**`channel_2` 那一条要照字面读**：**它存在、它是可选的、但它**现在不用**。**
**四段示例里它全是空的**（`PALS 2,10201,,(Clock)` 里那两个连续逗号就是它）。

### `DC_scale_channels_list`：**master/slave 与跨板 ganging**

原文对这一个参数说得最多，**因为它是本命令里唯一涉及硬件拓扑的地方**：

> 「You can define a Master/Slave configuration for DC Scale channels by specifying a list of
> DC Scale channels, separated by commas and enclosed by parentheses. **The first channel is the
> master.**」

> 「For UHC4 / UHC4T the channels must be physically adjacent on the same board, or be the last
> (the 4th) channel of a board and the first of another UHC4 / UHC4T board. **You cannot gang
> UHC4 and UHC4T boards.** Before ganging between boards can be used, the connection must be
> enabled by DDIC.」

**拆成四条硬条件**：

| # | 条件 |
|---|---|
| **1** | **第一个通道是 master** |
| **2** | **UHC4 / UHC4T 的通道必须在同一块板上**物理相邻**；或者**一块板的第 4 个通道 + 另一块 UHC4/UHC4T 板的第 1 个通道 |
| **3** | **UHC4 与 UHC4T 的板**不能混着 gang** |
| **4** | **跨板 ganging 之前，连接必须先由 `DDIC` 使能** |

> **第 3 条是本页唯一一条「明令禁止」**（原文 `You cannot gang …`）——
> **注意它禁的是「UHC4 板和 UHC4T 板互相 gang」，不是「UHC4T 不能用」。**

### 查询侧：两个特殊值 + `@`

**`site` 参数在查询里有两个特殊值**（原文写在 `site` 那一格）：

> 「When specified as part of the PALS? query, you can use the parameter ALL to read the channel
> allocation for all sites or the parameter PEND to read the pending channel allocation.」

| 特殊值 | 读什么 |
|---|---|
| **`ALL`** | **所有 site 的通道分配** |
| **`PEND`** | **pending 的通道分配**（**pending 是什么意思，本文档没写——语料未写**） |

**`pinlist` 有四条查询规则**（原文一整格）：

| 规则 | 原文 |
|---|---|
| **返回什么** | **`The query returns the name of the pin allocated to each channel.`** |
| **`@` 的用法** | **`The symbol @ can be used with the PALS? command to list all pins previously defined by the PALS command.`** |
| **多个引脚** | **`If a list of more than one pin is required, the pin names must be separated with a comma.`** |
| **查不到时** | **`If you query a non-existent pinlist, the system returns nothing.`**——**不报错，什么都不回** |

> **最后一条是一个排错陷阱**：**查询「不存在的 pinlist」不会报错，只会没有输出**。
> **所以「命令敲下去静悄悄」未必是命令没执行，也可能是你查的名字不存在。**
> （**推断**：这是对原文 `returns nothing` 的字面含义的说明，**原文没有把它标成注意事项**。）

### 四条报错条件

原文 `## Errors` 一节：

> 「An error is generated if：
> - The specified channel number is not valid;
> - The specified channel is not installed;
> - The specified pin name is already used as a group name;
> - The sequencer is in RUN or BREAK mode.」

| # | 条件 | 类型 |
|---|---|---|
| 1 | **通道号无效** | 值错 |
| 2 | **通道未安装** | 硬件不在 |
| 3 | **引脚名已经被用作组名** | 命名冲突（**组名是哪来的，本文档没写**） |
| 4 | **sequencer 处于 `RUN` 或 `BREAK` 模式** | **时序前置**——**在跑的时候不能改分配** |

> **第 4 条与「`PALS` 必须最先执行」是同一条要求的两个面**：
> **配置阶段做，别在跑的时候做。**

### `## Application`：引脚配置

> 「Pin Configuration, see Configuration Setup Commands.」

**即本命令归在「引脚配置」这一类下**——**那一篇本页没读。**

## 典型用法

**原文四段示例，一段一个场景。逐段照抄并读。**

**1. 最基本的：把一个 pin 分给某个 site 的某个通道**（逐字）：

```
PALS 2,10201,,(Clock)
PALS 2,10202,,(D0)
```

> 「The above example allocates the Clock pin for site 2 to channel 10201 and allocates pin D0
> for site 2 to channel 10202.」

**读法**：**`2` = site 2；`10201` = 五位数通道号；空的那个 = `channel_2`；`(Clock)` = 引脚名。**
**两行是同一个 site 的两个引脚**——**`PALS` 一次只分一个（或一 list）pin。**

**2. 单板上的 DC Scale master/slave**（逐字）：

```
PALS 2,(10101, 10102),,(dc1)
```

> 「This example defines a master/slave configuration for DC Scale channels. The first channel
> is the master.」

**读法**：**通道位换成了一对圆括号包的列表 `(10101, 10102)`**，
**`10101` 是 master**（`The first channel is the master.`）。

**3. 跨板的 DC Scale ganging**（逐字，**注意它多了一段 `DDIC`**）：

```
DDIC CONN, (104GO, 105GI)
DDIC CONN, (105GO, 107GI)
PALS 2,(10403, 10404, 10501, 10502, 10503, 10504, 10701, 10702),,(dc1)
```

> 「This example defines a master/slave configuration for DC Scale UHC4 channels across boards.
> The first channel is the master.」

**读法**：**先用两条 `DDIC CONN` 把跨板连接使能**（对应上面第 4 条硬条件），
**再把跨三块板的 8 个通道写成一个列表交给 `PALS`。**
**顺序是硬的：`DDIC` 在前，`PALS` 在后。**
**列表里的 `10403, 10404` / `10501…10504` / `10701, 10702` 三组正好对应三块板**
（**推断**：依据是三条 `DDIC CONN` 与列表里三段通道号的数目对应，**原文没有分点说明**）。

**4. 用 MCE 卡在 4 个 site 上做一对差分引脚**（逐字）：

```
DFAN "MCE231,2,i","",(av8_bbrx_b+)
DFAN "MCE231,6,i","",(av8_bbrx_b-)
PALS 2,"MCE231,1,i",,(av8_bbrx_b+)
PALS 3,"MCE231,3,i",,(av8_bbrx_b+)
PALS 4,"MCE231,4,i",,(av8_bbrx_b+)
PALS 2,"MCE231,5,i",,(av8_bbrx_b-)
PALS 3,"MCE231,7,i",,(av8_bbrx_b-)
PALS 4,"MCE231,8,i",,(av8_bbrx_b-)
```

> 「This example defines a pair of differential pins av8_bbrx_b+ and av8_bbrx_b- using the MCE
> card in 4 sites.」

**读法**：**先两条 `DFAN` 建两个差分引脚**（`av8_bbrx_b+` / `av8_bbrx_b-`），
**再用六条 `PALS` 把它们的六个通道分到 site 2 / 3 / 4 上**
（**site 1 的那两个通道由 `DFAN` 那两条管**——**推断**：
依据是本页「site 1 用 `DFPN`」的分工，**而这里出现的是 `DFAN`，另有一条命令；
原文没有解释 `DFAN` 与 `DFPN` 的关系**）。
**`channel_1` 在这里写成了带引号的串 `"MCE231,1,i"`，不是一个五位数**（见「出处」⚠️③）。

**由四段示例拼出的使用顺序（本页的建议顺序，依据见括号）：**

**① 确认 site**（≥ 2，site 1 走 `DFPN`）→
**② 拿到通道号**（数字或 DC Scale 用 `DFPN`/`DFUT` 查，MCE 这类用 `DFAN` 建）→
**③ DC Scale 要 ganging 就先 `DDIC CONN` 使能跨板连接** →
**④ `PALS {site},{通道},,({pin})`** →
**⑤ 要查就 `PALS? {site},({pinlist})`，全查用 `PALS? ALL,...`。**
**并且**整个 ①–④ 必须在任何其它 setup 命令之前做**（`including CONF`）。

> **⚠️ 上面这五步是本页把原文四段示例与那几条规则拼起来的**——
> **原文给的是四个孤立示例，没有给过顺序说明**（只有「`PALS` 必须最先」那一条是明说的）。
> **`DFAN` 与 `DFPN` 的分工、`DFAN` 的参数，本文档没写——语料未写。**

## 和谁有关

**上游（本页的通道号从哪儿来 / 本页的前置命令）**：

- [[dfpn]] — **site 1 的引脚通道由它定义**，**本页只管 site ≥ 2**。
  原文两处指过去：`Channels for site 1 are defined with DFPN.` 与
  `See DFPN, DFPN? - (DeFine Pin Name) for the channel number.`
  **即：同一次引脚配置里，`DFPN` 与 `PALS` 是一对，按 site 分工。**
- `DFUT, DFUT? - (DeFine UTility line)`（[[dfut]]，**未建**）——
  **utility line 的通道号查它**（`For utility lines, see DFUT … for the channel number.`）。
  **即 `PALS` 也能给 utility line 分配通道。**
- `DDIC`（**未建，且不在 allowlist 里**）—— **跨板 ganging 的使能命令**，
  原文示例 3 里用了它的 `CONN` 形式。
  **约束页 [[cross-card-ganging-requires-ddic]] 说的正是这件事**（见下）。
- `DFAN`（**未建，不在 allowlist**）—— **原文示例 4 里用它建差分引脚**；
  **它和本页的关系原文没有说明。**

**执行顺序上的约束（本页最硬的一条关系）**：

- [[pals-before-other-setup]] — **本页的核心规则「`PALS` must be used before any other setup
  command (including CONF)」的约束页。**
  **那页本页没读**；**本页只转述了原文这一句。**
- [[conf]] — **原文点名的那条 setup 命令**：
  `before any other setup command (including CONF)`。
  **即 `PALS` 必须排在 `CONF` **之前**。**（**那页本页没读**）

**同域（引脚 / 通道配置这一片）**：

- [[pin-mapping-file]]/ [[pin-configuration-file]]/
  [[pin-configuration-tool]]/ [[digital-pins-editor ]] ——
  **`PALS` 的 `## Application` 写的是 `Pin Configuration`**，
  **这些是「引脚配置」这一片的其余部分。**
  **本页与它们的**具体**分工，本页没读那几篇，不作断言。**
- [[sharing-configuration]] / [[sharing-configuration-file]]（**均未建**）——
  **多 site 共用资源这一片**；**本页做的是「按 site 分配通道」，
  与「哪些资源在 site 间共享」相邻但不同**（**推断**：依据是本页 `site` 参数的语义，
  **原文没有提到 sharing**）。

**硬件侧（本页的规则针对的卡）**：

- [[dc-scale-uhc4t-card ]] — **`DC_scale_channels_list` 那段的相邻性规则
  与「不能混 gang」禁令，针对的就是 UHC4 / UHC4T。**（**那页本页没读**）
- [[ganging ]] — **master/slave 配置这件事的总页**；
  **本页给的是「怎么在 `PALS` 里写出来」，ganging 本身是什么在那一边。**
- [[cross-card-ganging-requires-ddic]] — **与原文那句
  `Before ganging between boards can be used, the connection must be enabled by DDIC.` 直接对应**
  （**关系是**推断**：本页没有读那个约束页，只从名字与原文这句话判断它们讲的是同一件事**）。

**别处**：

- `Configuration Setup Commands`（**未建**）— **`## Application` 指向的上一级分类。**
- `DUT interface layout`（**未建**）— **`## Related information` 里**唯一**的一条**；
  它属于 [[dut-board-design-reference]]那一章。
  **原文只给了链接，没有任何说明它和本页什么关系。**
- [[smartest-7.1.3]] / [[smartest-7.5.0]] — **本页版本记录里的两版**（见「版本」）。

> **本页的「和谁有关」全部来自这一篇原文里点到的名字。**

## 版本

本文档有 `## Functional changes` 段，**全部内容三条**：

- **`Introduced before SmarTest 6.3.2`**
- **`SmarTest 7.1.3: Support of MBAV8+`**
- **`SmarTest 7.5.0: New extra parameter channel_3 for stacked FVI16 channels.`**

> **第一条 `Introduced before SmarTest 6.3.2` 是哨兵值，不是「6.3.2 的变更」。**
> 按 §11.2 ②，`before` 的意思是「**在本文档集覆盖范围开始之前就已经有了**」——
> 照字面读会造出一条格式齐整的假信息。**本页不把它读成版本变更。**
>
> **后两条是真版本记录**（措辞是 `SmarTest 7.1.3:` / `SmarTest 7.5.0:`）。
>
> **⚠️ 第三条与本文档自己的语法 / 参数两节**对不上**，这是本篇最大的一处内部不一致**：
> **`SmarTest 7.5.0` 说新增了参数 `channel_3`（给 stacked FVI16 通道用），
> 而同一个文档的语法行与参数表里**都没有 `channel_3`**——
> 语法行只有 `[channel_2]`，参数表里 `channel_2` 写的是
> `The optional parameter is currently not used.`**
> **本页照实两处都写，不替它调和、也不替它补 `channel_3` 的语法。**
>
> **对照页**：[[smartest-7.1.3]] / [[smartest-7.5.0]] / [[smartest-6.3.2]]（**均未建**）——
> **三版的覆盖范围本页都没读。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md`
（raw 的 `source_topic: "98680.htm"`）。

**本页没做的**：

- **`DFPN`（[[dfpn]]）没读**——**而 site 1 那一半、以及「通道号怎么查」都在它那儿。**
  **本页对它的了解只有原文那两句指路。**
- **`DFUT`（utility line）没读**——**utility line 怎么分配、通道号长什么样，本页没有。**
- **`DDIC` 没读**——**跨板 ganging 的 `CONN` 语法、`GO` / `GI` 是什么，本页不知道**
  （**示例 3 里的 `104GO` / `105GI` 本页只照抄，没解释**）。
- **`DFAN` 没读**——**示例 4 全靠它建差分引脚，而它一个字都没在本页解释。**
- **`CONF`（[[conf]]）没读**——**`PALS` 要排在它前面的那条规则，本页只有原文一句转述。**
- **`Configuration Setup Commands` / `DUT interface layout` 没读**——
  **`## Application` 与 `## Related information` 各指一篇，两篇本页都没读。**
- **`stacked FVI16`、`MBAV8+` 本页没有任何依据**——
  **这两个词只出现在 `## Functional changes` 里，本文档正文没解释过它们是什么。**
- **`pending channel allocation`（`PEND`）是什么意思，本文档没写——语料未写。**
- **`PALS` 一次能不能给多个 site 分配？** 本文档的语法行只有**一个** `{site}`，
  **但示例 4 里同一个 pin 在 site 2/3/4 上要写三条 `PALS`**。
  **即：本文档的形状是「一次一个 site」**（**推断**：依据是语法行与示例 4 的写法一致）。
- **「引脚名已经被用作组名」里的**组名**是哪来的，本文档没写。**
- **没有任何图。** 本篇没有图片引用。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `## Parameters` 是一张被拆成「一格一行」的大表。** 逐字：
> `|` /（空行）/ `site` /（空行）/ ` |` /（空行）/ `The site parameter is an integer that
> defines the number of the site where the channels are to be defined.` /（空行）/…
> ——**每个单元格各占一行、格与格之间夹空行**。脚本只认连续 ≥3 行的管道行，
> **所以「语法 / 参数」节里这张表是散着的**。与 [[xps256-status-flags]] 那 18 张表、
> 以及 [[sqst]] 的参数表是同一类成因（HTML 表格转 markdown 被拆散）。
> **逐字没丢，只是形状变了。**
>
> **② 语法行的括号记号不统一。** 逐字：
> `PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}`
> ——**`site` 用 `{}`、`channel_1` 用 `{}`、`channel_2` 用 `[]`、`pin` 写成 `{(pin)}`**。
> **`{}` 同时出现在「必给」与「圆括号列表」两个位置**，**原文没有给记号说明。**
>
> **③ 通道号的写法在本文档里不止一种，而参数表只写了一种。**
> 参数表 `channel_1` 那格说 **`which is five digits`**，
> 而示例 4 里 `channel_1` 的位置上写的是**带引号的 `"MCE231,1,i"`**——
> **不是五位数。** 另外示例 3 里 `DDIC CONN` 那两行用的是**带字母的 `104GO` / `105GI`**
> （**那是 `DDIC` 的参数，不是 `PALS` 的**，本页把它一并列出只因为它在同一段示例里）。
> **原文没有解释这些写法之间的关系。本页照引，不判。**
>
> **④ `## Errors` 那条的状态名大写且与别处可能不同形。** 逐字：
> `The sequencer is in RUN or BREAK mode.`——**原文写的是 `BREAK`**。
> **本页照引这一句，不改它的拼法。**
> （**本页不在正文里把 `BREAK` 与其它文档里的状态名作比较**——
> **§5：本页只写这一篇里有的。**）
>
> **⑤ 一处圆括号没有闭合。** 逐字（`site` 那一格）：
> `The integer must be greater than 1 (channels for site 1 are defined by the command` +
> `DFPN` 的链接 + `.`——**左圆括号开了，右圆括号在原文里没有**。
> **本页在「是什么」里只引了它的前半句 `The integer must be greater than 1`（一个完整的子串），
> 没有补那个括号，也没有把整句当作逐字引文。**
>
> **⑥ `## Related information` 只有一条链接、没有任何文字说明。**
> 逐字：`[DUT interface layout](<../02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md>)`
> ——**全节就这一行**，**原文没说它和本页是什么关系。**
>
> **⑦ 示例 4 里出现了 `DFAN`，而正文与参数表里一次都没提过它、也没给链接。**
> **即：一段示例用了一条本文档从未定义过的命令。** 本页在「典型用法」里标出了这一点。

`verified: doc-only`
