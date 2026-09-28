---
type: object
title: VWFS? - (Verify WaveForm Sets)
layer: L1
stage: timing
tags: [timing, vwfs, l1-command, firmware-command, verify, waveform-set, compatibility]
related: [vwfg, wsus, waveform-set, wfds, wave, dfgp, timing, timing-setup-commands, test-program-explorer]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VWFS? - (Verify WaveForm Sets)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,094 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VWFS? {waveform_set_1},{waveform_set_2},{(pinlist)}
```

returns:

```
VWFS {status}, {(pinlist)}
```

### Parameters

|

waveform_set_x

 |

Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

pinlist

 |

The name of the pin or pins for which you wish to check waveform set compatibility. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.

 |
 |

status

 |

The system returns:

 |
 |

 |

0

 |

The waveform sets are not compatible.

 |
 |

 |

1

 |

The waveform sets are compatible.

 |

### Example

```
VWFS? 1,2,(DATA)
```

This example checks whether waveform sets 1 and 2 are the same for the pins in the group DATA. If they are the same the following string is returned:

```
VWFS 1,(DATA)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.

<!-- 报错节 end -->

## 是什么

**`VWFS?` 是 timing setup 里的另一条校验查询：问「两个 waveform set 对指定 pin 是不是兼容」，
答 `1`（兼容）或 `0`（不兼容）。** 原文第一句：

> 「The VWFS? (Verify WaveForm Sets) query checks whether two specified waveform sets are compatible
> for the specified pins. The system responds with 1 if the pins are compatible, and with 0 if they
> are not compatible.」

**「两个」是这条命令的身份**：`two specified waveform sets` 是它的输入，
而比较的落点是 `for the specified pins`——**先给两个 set，再问「这一组 pin 上它们一样吗」**。

> ⚠️ **开篇句自己有个小别扭**：前半句的主语是 `two specified waveform sets`，
> 而判据句的主语换成了 `the pins`（`if the pins are compatible`）。
> **本篇没有解释这两者怎么切换**——**本页照原样引，不替它统一**（见「出处」⚠️ ①）。

### 它比什么：一份判据清单，**而且和 [[vwfg]] 那份不一样**

> 「The items that must be identical when checking for the compatibility of waveform sets are the
> device cycle name and waveform sequence, and the waveforms and data parameters as specified by the
> commands WFDF, WFDF? - (WaveForm DeFinition) and WAVE, WAVE? - (WAVEform).」

拆成三段：

| # | 要求相同的东西 | 原文 |
|---|---|---|
| 1 | **device cycle 名** | `the device cycle name` |
| 2 | **波形序** | `and waveform sequence` |
| 3 | **波形与数据参数**（由 `WFDF` 与 `WAVE` 规定） | `and the waveforms and data parameters`（哪两条命令规定，见上引整句） |

**第 3 段是本页与 [[vwfg]] 分岔的地方**：`VWFG?` 的同一位置列的是**三条**命令
（`WFDF`, `WAVE`, `BWDF`），而 `VWFS?` 只列了**两条**（`WFDF`, `WAVE`）。
**两篇都是「哪些东西算进 waveform 定义」的答案，两个答案不一样，而两篇都没有解释这个差**——
**本页把两处并列记下，不替它们裁定**（见「出处」⚠️ ②）。

### 它也不改任何东西

> 「The VWFS? query has no influence on the number of defined waveform sets.」

**与 [[vwfg]] 那一句逐字相同**（只差命令名）。**两篇都只声明了这一件事**，
别的状态碰不碰，**语料未写**。

### 语法与参数：两个输入，而且**没有 device cycle 过滤器**

```
VWFS? {waveform_set_1},{waveform_set_2},{(pinlist)}
```

returns:

```
VWFS {status}, {(pinlist)}
```

两个要点：

| 要点 | 说明 |
|---|---|
| **输入是两个编号** | `waveform_set_1` / `waveform_set_2`——**没有 `wavetable_name` / `specset_id` 形式**，即 **equation based 那一侧的两种写法在本篇不存在**（对照 [[vwfg]]） |
| **回复带回 pinlist** | `VWFS {status}, {(pinlist)}`——回复里**把 pin 组名回显一次**（示例里回来的是 `(DATA)`） |

**两个编号的取值**（参数表逐字）：

> 「Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform
> sets. The maximum number is determined by WSUS, WSUS? - (Waveform Sets USed).」

**注意这里没有 `PRM`**——[[vwfg]] 的同一个位置写的是
`Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of
allowed waveform sets.`，
**而本篇只给整数区间**。两篇的取值集不一致，本页照记。

`pinlist` 逐字（与 [[vwfg]] 那句只差最前面的一个从句）：

> 「The name of the pin or pins for which you wish to check waveform set compatibility. This
> parameter can also include groups previously created by DFGP, DFGP? - (DeFine GrouP). If more than
> one pin is to be included, the names must be separated with a comma. The symbol @ can be used to
> check all configured pins.」

`status` 的取值（参数表里那两块嵌套格逐字）：

| 值 | 意思 |
|---|---|
| `0` | `The waveform sets are not compatible.` |
| `1` | `The waveform sets are compatible.` |

**`0` 是正常回复，不是报错。** 真正会报错的只有一种情形：编号越 [[wsus]] 的上限。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`。** 能给定位的只有
`## Application`（一行）与 `## Example`（一个示例）。

**1. 原文的定位**（`## Application` 全文，逐字）：

> 「Timing setup, see Timing Setup Commands and Test Program Explorer.」

**两个去处**：`Timing Setup Commands`（有链接 → [[timing-setup-commands]]）与
`Test Program Explorer`（**这一处没有链接** → [[test-program-explorer]]）。
**本篇说这件事有两个入口，但没说两边各做什么。**

**2. 唯一一个示例**（`## Example`，逐字）：

```
VWFS? 1,2,(DATA)
```

**原文对它的说明**：

> 「This example checks whether waveform sets 1 and 2 are the same for the pins in the group DATA. If
> they are the same the following string is returned:」

```
VWFS 1,(DATA)
```

**三点值得注意**：

| 观察 | 说明 |
|---|---|
| **请求行没有 `>` 前缀** | 与 [[vwfg]] 的示例不同，本篇的示例**没有区分进出的符号**，就是一行命令加一行回复 |
| **回复把 pinlist 回显了** | `(DATA)` 回来了——与语法里的 `VWFS {status}, {(pinlist)}` 对得上 |
| **只示范了「兼容」那一支** | 原文写的是 `If they are the same the following string is returned`——**不兼容（`0`）时回复长什么样，本篇没给**（**语料未写**） |

**3. 什么时候问它、什么时候问 [[vwfg]]**：

| 你的问题 | 用哪一条 |
|---|---|
| **同一组 pin 上，两个 waveform set 能不能互换** | **`VWFS?`**（两个编号 + 一组 pin） |
| **同一个 waveform set 里，一组 pin 的定义是不是一样** | **`VWFG?`**（一个 set + 一组 pin + 可选 device cycle） |
| **是哪几个 pin 不兼容** | **本篇答不了**——回复只有 `{status}` 与 pin 组名，**没有逐 pin 的输出**（**语料未写**） |

**4. 出错**：只有一条（编号越 [[wsus]] 上限），见上面「报错条件」节。

## 和谁有关

- [[vwfg]] — **姊妹查询，方向互补（同类）**。两篇共用一句
  `The VWFS? query has no influence on the number of defined waveform sets.`（[[vwfg]] 同句只差命令名），
  `pinlist` 那一段也几乎逐字相同（只差最前面的一个从句）。
  **但四处不一样，都在上面逐条记了**：比较对象（两个 set vs 一组 pin）、
  输入形式（只有编号 vs 三种写法）、判据清单（`WFDF`+`WAVE` vs `WFDF`+`WAVE`+`BWDF`）、
  编号取值集（无 `PRM` vs 有 `PRM`）。
- [[wsus]] — **上限来源（前置）**：参数表与报错都指着它，两处原文分别是
  `The maximum number is determined by WSUS, WSUS? - (Waveform Sets USed).` 与
  `An error is generated if waveform_set is greater than the range allowed by the WSUS command.`
- [[waveform-set]] — **作用域（同类）**：`{waveform_set_x}` 指的就是它。
  **「一个 waveform set 里装什么」的正文在那一页，本页没有。**
- [[wfds]] / [[wave]] — **判据的来源（上游）**：本篇说兼容与否看的是这两条命令规定的
  `the waveforms and data parameters`。**这两篇的 raw 本页没读**（见「出处」）。
- [[dfgp]] — **`pinlist` 可以带组（上游）**：`groups previously created by DFGP`。
- [[timing]] — **`stage: timing` 的阶段页**；它的「验证」表里有 `VWFS?` 一行：
  `两个 waveform set 是否兼容（返回 0/1）`（**本页读到的 wiki 页**，不是本篇 raw）。
- [[timing-setup-commands]] / [[test-program-explorer]] — **`## Application` 指的两个入口**
  （见「典型用法」）。
- [[command-reference]] — **命令索引页**：`VWFS?` 属 `02.06_Command_Reference` 一族。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 VWFS?」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 VWFS?」。**

**版本段里没有的东西**（照实记，不替它补）：**没有第二条**。
所以「`VWFS?` 与 [[vwfg]] 是不是同一版进来的」「`@` 是哪一版加的」**在本篇里查不到**。

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.md`
  （frontmatter 的 `source_topic` 是 `98864.htm`；**2,466 字节 / 100 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。
- **上游 `.htm` 核过**：`raw/98864.htm`（**6,881 字节**）。核的是下面 ⚠️ ④ 那一条。

**本页没做的**：

- **`WFDF` / `WAVE` / `WSUS` / `DFGP` 四篇的 raw 一篇没读。**
  **所以「兼容判据具体比哪些参数、上限怎么改、组怎么建」本页一个字没有。**
- **`Timing Setup Commands` 与 `Test Program Explorer` 两篇没读**——
  `## Application` 只给了这两个名字（后者连链接都没有）。
- **equation based 那一侧一篇没读。** 本页**没有** [[vwfg]] 那种
  `specset_id` / `wavetable_name` 形式，**所以那一侧（wavetable、timing specification）本页一个字没有。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**；上游 `raw/98864.htm` 里 `<img` 也是 **0 次**。
  **所以本页没有任何来自图的结论，这张「没有图」是查过的事实（§11.4）。**
- **没在任何 93K 机台上跑过 `VWFS?`**（`verified: doc-only`）。
  **所以「不兼容时回复长什么样」「是哪几个 pin 不兼容」本页答不了。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的唯一一条——不是漏写。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.md`（**本页的出处**） | `98864.htm` | 2,466 | — |
| `02.06_Command_Reference/02.06.06.02.39_VWFS__-__Verify_WaveForm_Sets.md` | `98864_2.htm` | 2,467 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.39_VWFS__-__Verify_WaveForm_Sets.md` | `98864_3.htm` | 2,640 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，差的字节就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 开篇句的判据从 set 滑到 pin。** 逐字是
> `The VWFS? (Verify WaveForm Sets) query checks whether two specified waveform sets are compatible
> for the specified pins. The system responds with 1 if the pins are compatible, and with 0 if they
> are not compatible.`
> ——**前半句问的是「两个 set 兼不兼容」，后半句答的却是「pins 兼不兼容」。
> 本篇没有交代这两者怎么过渡**（本页「是什么」引了整句，照原样）。
> **② 与 [[vwfg]] 的判据清单不一致**：本篇那句只列 `WFDF` 与 `WAVE`，
> 而 [[vwfg]] 的同一位置多列一条 `BWDF`。**两篇都没解释这个差，本页不替它们裁定**
> （对照依据是 [[vwfg]] 页的「语法 / 参数」节；**那一篇的 raw 不在本页的 `sources:` 里**）。
> **③ 参数名在两处不同形**：`## Parameters` 写 `waveform_set_x`，
> 而 `## Errors` 写的是 `waveform_set is greater than the range allowed by the WSUS command.`
> ——**同一篇里同一个参数两个名字**（[[bwds]] 那一页记过同一种毛病）。
> **④ `## Application` 里两个去处只有一个有链接。** 逐字是
> `Timing setup, see Timing Setup Commands and Test Program Explorer.`
> ——**`Timing Setup Commands` 在 md 里是链接，`Test Program Explorer` 是纯文本。**
> **核过上游 `raw/98864.htm`：那里同样只有前一个带 `<a href>`，后一个是裸文本**——
> **所以这处不齐是上游文档自带的，不是转换丢的**（§11.2 ⑥ 的判法）。
> **⑤ `status` 那张参数表是嵌套表。** 值 `0` 与 `1` 各自占一行、**每行第一格是空的**
> （压平后就是「空首格 + 值格 + 释义格」），语法节里能看出这个形状。
> **原文如此，不是脚本抽错。**
> **⑥ 坏字：本篇 0 个。** 按 §11.2 ① 的判据（英文文档里出现任何汉字都是坏字）逐字查过，
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
