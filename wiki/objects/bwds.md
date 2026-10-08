---
type: object
title: BWDS, BWDS? - (Break Waveform Definition String)
layer: L1
stage: timing
tags: [timing, break-waveform, bwds, l1-command, firmware-command, fixed-timing, definition-string]
related: [bwdf, wfds, wsus, waveform-set, pclk, wave, timing, timing-setup-commands]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# BWDS, BWDS? - (Break Waveform Definition String)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,081 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### BWDS

```
BWDS {wvf_set}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

### BWDS?

```
BWDS? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {(pinlist)}
```

returns:

```
BWDS {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

Parameters
| wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. Enter PRM for the Primary waveform set. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|
| wavetable_name | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. wavetable_name can only be specified in the query. |
| specset_id | Derived as follows:<br><br>100 * equation_set_no + specset_no<br><br>specset_id can only be specified in the query. |
| multi-port_spec | To query a multi-port specification, enter the name of the specification. |
| break_waveform_index | Enter DEF for the default break waveform or an integer in the range 0 to 3. This parameter is optional in release 2.0 and can only be used to select the default break waveform (DEF). |
| mode | NOT USED. |
| definition_string | The definition string consists of a sequence of items each of which associates a drive action with a drive edge.<br><br>Receive edge are always denoted by rn.<br><br>All edges which are not explicitly specified are set to N. In the query only those edges that are used are printed.<br><br>For details of the syntax see `WFDS, WFDS? - (WaveForm Definition String)`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）. |
| pinlist | The name of the pin or pins for which break waveform definitions are to be made or read back. The symbol @ can be used to specify all configured input and IO pins. If more than one pin is to be included, the names must be separated with a comma. |

### Example

```
> BWDS? 1,,,(@)
< BWDS 1,,,"",(io)
< BWDS 1,,,"d1:F00 d5:F10",(clk)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

- waveform_set is greater than the range allowed by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.
- There is a mismatch between the edge actions and edge order in the specified waveform.
- A tri-state action is defined or implicitly required on edge 2 or 5 (only for P/C/Ce systems).

<!-- 报错节 end -->

## 是什么

**BWDS 定义 break waveform 的动作，和 [[bwdf]] 干的是同一件事——
区别在于它用「定义串」写，而不是六个固定的边沿位。** 原文第一句：

> 「The BWDS (Break Waveform Definition String) command defines the actions for the break
> waveform of the specified waveform set. The BWDS? query returns the definitions for the
> current break waveform of the specied pins.」

**第二句里的 `specied` 是原文的错字，应为 `specified`**——
**本页照原样引，见「出处」⚠️ ①。**

### 它和 BWDF 的分工：一条按边沿数划的界

原文有一句自述，而 [[bwdf]] 那一篇有一句方向相反的话，两句说的是同一件事：

| 谁说 | 原句 |
|---|---|
| **BWDS（本篇）** | `This command replaces the command BWDF, BWDF?` |
| **BWDF（那一篇）** | `is replaced by BWDS, BWDS? from release 2.1 onwards when 14-edge setups are used. The command will be disabled for pin and waveform sets containing more than 6 edges.` |

**（第二句出自 [[bwdf]] 那一篇，不在本页的 `sources:` 里，本页按「读到的另一篇」对照引，
见「出处」。）**

**这里最该记住的是「两条边界对不齐」**：本篇说 `14 or more edges`，
BWDF 说 `more than 6 edges` 就禁用——**7 到 13 个 edge 的 setup 归谁管，两篇都没写**（**语料未写**）。

### 与 BWDF 相比：三条性质一样，一条不一样

> 「Only drive actions are allowed. The break waveform must not contain data dependent actions.
> Edge delays that are incompatible with the defined actions will be auto-corrected to fit.
> The BWDS command can only be used for fixed timing.」

| 性质 | 本篇的写法 | [[bwdf]] 的写法 |
|---|---|---|
| **只许 drive 动作** | `Only drive actions are allowed.` | 同一句 |
| **不许 data dependent 动作** | `The break waveform must not contain data dependent actions.` | 同一句 |
| **延迟不相容时自动改正** | `Edge delays that are incompatible with the defined actions will be auto-corrected to fit.` | `Edges with delays that are incompatible with the defined actions will be auto-corrected to fit.` |
| **能不能用于 equation based** | **写了：`can only be used for fixed timing`** | **没写** |

**多出来的是最后那一整句**，而且紧接着还有一句反向的补充：

> 「The query can also be used for equation based timing.」

**两句合起来是一条很实用的规则**（**这是本篇比 [[bwdf]] 明确的地方**）：

| 用哪一个 | fixed timing | equation based timing |
|---|---|---|
| **`BWDS`（写）** | **可以** | **不可以** |
| **`BWDS?`（读）** | **可以** | **可以** |

**「为什么写不行、读行」本篇没有解释**（**语料未写**）。

### 定义串怎么写——本体在 WFDS，本篇只给规则

`definition_string` 那一栏逐字：

> 「The definition string consists of a sequence of items each of which associates a drive action
> with a drive edge.」

> 「Receive edge are always denoted by rn.」

> 「All edges which are not explicitly specified are set to N. In the query only those edges
> that are used are printed.」

> 「For details of the syntax see WFDS, WFDS? - (WaveForm Definition String).」

**四句话拼出四条规则**：

| 规则 | 原文 |
|---|---|
| **一项 = 一个 drive 动作 + 一个 drive 边沿** | `a sequence of items each of which associates a drive action with a drive edge` |
| **receive 边沿一律写 `rn`** | `Receive edge are always denoted by rn.` |
| **没写到的边沿 = `N`** | `All edges which are not explicitly specified are set to N.` |
| **回读只印用到的边沿** | `In the query only those edges that are used are printed.` |

**四条里有两条是「默认值」，而且方向相反**：
**写的时候「不写 = `N`」**；**读的时候「只印用到的」**。
**合起来就是一句最实用的话：写完再读回来，回复比你以为的短是正常的。**

**而「动作有哪些取值」「`d1` / `r1` 这种边沿名怎么定」本篇一句不写**——
它把这件事整段推给 `WFDS`（`For details of the syntax see WFDS, WFDS? - (WaveForm Definition String).`）。
**`WFDS` 那一篇本页没读**（见「出处」），**所以定义串的完整语法本页没有。**

**「`rn` 里的 `n` 是什么」本篇也没写**：它只说 receive 边沿**一律**用 `rn` 表示，
**没有说 `n` 是边沿号还是占位符**（**语料未写**；
**推断**——对照示例里的 `d1` / `d5` 与 [[bwdf]] 的「第 4 / 第 5 个边沿」，
`n` 最可能就是边沿序号，**但本篇一个例子都没有，本页不把它写成事实**）。

### `BWDS` 与 `BWDF` 还有一个结构上的差别：边沿位的数量

| | 怎么写动作 | 边沿数从哪来 |
|---|---|---|
| **[[bwdf]]** | **`a1` 到 `a6` 六个位，一位一个动作** | **写死在语法里（6）** |
| **BWDS（本页）** | **一串 `边沿:动作` 项** | **由定义串自己给** |

**这就是「14-edge setup 必须换 BWDS」的机制性原因**——
**六个位装不下 14 条边沿，而定义串没有位数的上限。**
（**推断**：本条只把两篇的语法并排看；**两篇都没有一句说「BWDS 是为了突破 6 位限制」，
但 [[bwdf]] 的 `Note` 段同时写了 `14-edge setups` 与 `more than 6 edges` 两个数。**）

### `break_waveform_index`：一句自相矛盾的释义

逐字：

> 「Enter DEF for the default break waveform or an integer in the range 0 to 3. This parameter
> is optional in release 2.0 and can only be used to select the default break waveform (DEF).」

**前一句说「可以给 0 到 3 的整数」，后一句说「只**能**用来选默认的 `DEF`」——
两句能不能同时成立，本篇没有解释。本页两处照引、不替它裁定**（见「出处」⚠️ ②）。

**另外两点照实记**：

- **`This parameter is optional in release 2.0`**——**本篇讲的是 `release 2.0` 的状态**，
  **而 7.10.3 上它是不是还可选，本篇没说。**
- **`DEF` 之外的 `0` 到 `3` 分别指什么**——本篇没写（**语料未写**）。

### `mode` 这个参数是空的

`mode` 那一栏的原文只有两个词：

> 「NOT USED.」

**而语法里 `[mode]` 还占着一个可选位**（`BWDS {wvf_set}, [break_waveform_index], [mode],
{definition_string}, {(pinlist)}`）——**位子还在，只是没用。**
**为什么留一个没用的参数、以后会不会启用，本篇没说**（**语料未写**）。

### 定位的四条路：写与读不一样，而且本篇明说了限制

`BWDS?` 的第一位可以写四种：`{wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}`；
`BWDS`（写）只写 `{wvf_set}`。**参数释义把「只在查询里可用」这件事明写在两条上**：

> 「wavetable_name can only be specified in the query.」

> 「specset_id can only be specified in the query.」

**这是本篇比 [[bwdf]] 清楚的地方**——**BWDF 那两个参数项里没有这两句限制**
（**那一条对照依据的是 [[bwdf]] 页的「语法 / 参数」节，见「和谁有关」**）。

**`wvf_set` 给了三个取值**，逐字：

> 「Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. Enter PRM for
> the Primary waveform set. The maximum number is determined by the command WSUS, WSUS? -
> (Waveform Sets USed).」

| 取值 | 意思 |
|---|---|
| 数字 | `range 1 to maximum` |
| **`PRM`** | **Primary waveform set** |
| `ALL` | **all waveform sets** |

**三条并列给出，不分写读**——
**而 [[bwdf]] 那篇同一位置的取值集里没有 `PRM`**（**两篇不一致，本页不替它补**）。
**另外 `ALL` 用在「写」命令上是什么语义，本篇没说**（**语料未写**）。

## 典型用法

**1. 先判两件事**：

| 判什么 | 结论 |
|---|---|
| **边沿数** | **≥ 14 个 edge → 用本条**；**≤ 6 个 → [[bwdf]] 也能用**；**7 到 13 个 → 语料未写** |
| **timing 类型** | **要写定义就只能是 fixed timing**；**只是回读的话 equation based 也行** |

**2. 写**：`BWDS {wvf_set}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}`
——**中间两个可选位可以留空**（示例里就留了），**定义串必须用双引号包起来**。

**3. 原文示例（`## Example`，逐字）——全篇唯一一个示例，而且是一条查询**：

```
> BWDS? 1,,,(@)
< BWDS 1,,,"",(io)
< BWDS 1,,,"d1:F00 d5:F10",(clk)
```

**读这个例子有四点值得注意**：

| 观察 | 说明 |
|---|---|
| **`> ` 与 `< ` 两个前缀** | `>` 是发出去的、`< ` 是回复——**本篇用符号区分进出** |
| **回复是两行** | **一个 pin 组一行**（`(io)` 一行、`(clk)` 一行） |
| **`@` 回来的是「组」，不是 pin** | 请求写 `(@)`，回来的 pinlist 是 `(io)` 与 `(clk)` 两个**组名** |
| **`""` 也是有效回复** | `(io)` 那组回的是**空定义串**——**按「不写 = `N`」的规则，这一组的边沿全是默认值** |

**第三点与 `pinlist` 的释义对得上**：

> 「The symbol @ can be used to specify all configured input and IO pins.」

**注意是 `input and IO pins`，不是所有 pin**——
**[[bwdf]] 写的是同一个短语，而 [[wave]] 写的是 `all configured pins`**
（**三篇不一致，本页照记**）。

**4. 回读要预期「短回复」**：`All edges which are not explicitly specified are set to N.
In the query only those edges that are used are printed.`
——**所以 `BWDS?` 回来的定义串比你以为的短是正常的**，
**而且回复的行数取决于 pin 组的数量（一组一行），不是一条命令一行。**

**5. 出错的三条**（`## Errors` 里全部三条）：

- `waveform_set` 越 [[wsus]] 的范围；
- **edge 动作与 edge 顺序不搭**：`There is a mismatch between the edge actions and edge order
  in the specified waveform.`
- **第 2 或第 5 个边沿上出现（或隐含需要）tri-state 动作**——
  **这一条在本篇带了限定 `(only for P/C/Ce systems)`，而 [[bwdf]] 的同一条没有这个限定。**

**6. `BWDS?` 一个写命令的例子都没有。**
`## Example` 只示范了查询——**「怎么写一条完整的 `BWDS`」本篇**没有**示范过**（**语料未写**）。

## 和谁有关

- [[bwdf]] — **被替代的那条（前身）**。本篇正文逐字点名：
  `This command replaces the command BWDF, BWDF?`。
  **分工按边沿数划**（`14 or more edges` vs `more than 6 edges`，中间那段两篇都没写，见「是什么」）。
  **本页的取材只有 BWDS 这一篇**——上面从 [[bwdf]] 引的那些对照句
  **出自那一页的 raw，不在本页的 `sources:` 里**，按「读到的另一篇」标注。
- [[wfds]] — **定义串语法的出处（前置）**。本篇把整件事推给它：
  `For details of the syntax see WFDS, WFDS? - (WaveForm Definition String).`
  **`WFDS` 的 raw 不在本页取材内**——
  **所以「动作怎么写、边沿名怎么定」本页一个字没有。**
- [[wsus]] — **`wvf_set` 的上限来源（前置）**：
  `The maximum number is determined by the command WSUS, WSUS? - (Waveform Sets USed).`
  **`## Errors` 第一条也指着它。**
- [[waveform-set]] — **本页的作用域（同类）**：break waveform 是按 waveform set 定义的
  （正文 `of the specified waveform set`），`wvf_set` 指的就是它，
  **`PRM` 指的也是「第一号 waveform set」**。**「waveform set 装什么」的正文在那一页，本页没有。**
- [[pclk]] / [[wave]] — **同族姊妹命令（并列）**。**本篇一次没提它们**；
  「同族」的依据是 [[timing]] 阶段页把它们列在同一个 L1 单元里
  `fixed timing 路线：逐个元素定义 edge / period / waveform`（**本页读到的 wiki 页**）。
  **`WAVE` 那一边（`DD` / `ED` / data 参数）与 break waveform 是两套东西。**
- [[timing]] — **`stage: timing` 的阶段页**（同上）；
  **而本页 `stage: timing` 另有一条正文依据**：`The BWDS command can only be used for fixed timing.`
- [[timing-setup-commands]] — **上游入口**。本篇 `## Application` 全文一句：
  > 「Timing setup, see Timing Setup Commands.」
  **本篇没有说 BWDS 在 timing setup 流程里排第几步。**

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 BWDS」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 BWDS」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「它是从哪一版起替代 BWDF 的」在本篇里查不到**——
**正文写的是「本命令替代 BWDF」，没有给版本号；
版本号那一侧（`from release 2.1 onwards`）写在 [[bwdf]] 那一篇里。
两篇合起来才有一条完整的时间线，而两篇用的编号体系不同（`release 2.x` 与 `SmarTest 6.3.2`）。**

**另记一句**：**参数释义里还有一个更老的编号 `release 2.0`**
（`This parameter is optional in release 2.0`）——**本篇一篇里就有两个 `release 2.x` 的引用，
而它们与 `SmarTest 7.10.3` 的对应关系，本篇一个字没写。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md`
  （frontmatter 的 `source_topic` 是 `98498.htm`；**3,769 字节 / 140 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。
- **本页「语法 / 参数」节里 `Parameters` 是一个裸行**——**原文那一行就没有 `##`**
  （别篇写的是 `## Parameters`）。**所以脚本没起 `### Parameters` 小标题、
  也没把那张参数表当表格抽。这是语料的段标记缺失，不是脚本抽错。**

**本页没做的**：

- **`WFDS` 的 raw 没读。** 本篇把定义串语法整段推给它——
  **所以「一项怎么写、动作有哪些、边沿名怎么编号」本页一个字没有。**
- **`BWDF` 的 raw 不在本页的 `sources:` 里。** 本页为对照引了它一篇里的两处
  （`is replaced by BWDS, BWDS? from release 2.1 onwards when 14-edge setups are used. The
  command will be disabled for pin and waveform sets containing more than 6 edges.`
  与它的参数表里没有「只在查询里可用」的限制、它的 `## Errors` 那条报错没有
  `(only for P/C/Ce systems)` 这个限定）——**这三处都标成了「读到的另一篇」，
  不作为本页的文档事实来源。**
- **`WSUS` / `WAVE` / `PCLK` 三篇都没读。** 上面「`@` 展开范围」「`PRM` 有没有」两处对照，
  **依据是各自页的「语法 / 参数」节，不是本页的 raw。**
- **`Timing Setup Commands` 那一篇没读。** 本篇 `## Application` 只给了它的标题。
- **真正的 break waveform 语义没有第二处来源。** 本篇与 [[bwdf]] 是语料里唯一两篇讲它的，
  **而两篇都不定义它**——**「break 是什么意思、什么测试会用到、第 2 与第 5 个边沿为什么特殊」
  本页答不了（语料未写）。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **「一条 break waveform 长什么样」本页只有文字（§11.4）。**
- **没在机台上跑过 `BWDS` / `BWDS?`**（`verified: doc-only`）。
  **所以「`""` 那条空定义串在机台上到底意味着什么」本页答不了（§11）**——
  本页只说「按本篇那条 `set to N` 的规则，它应当全是默认值」。
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的三条——不是漏写。
- **`## Example` 只有一个（查询）。** 所以「怎么写一条 `BWDS`」本页没有示例可依。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md`（**本页的出处**） | `98498.htm` | 3,858 | — |
| `02.06_Command_Reference/02.06.06.02.03_BWDS__BWDS__-__Break_Waveform_Definition_String.md` | `98498_2.htm` | 3,860 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.03_BWDS__BWDS__-__Break_Waveform_Definition_String.md` | `98498_3.htm` | 4,060 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 错字 `specied`。** 第一段第二句原文是
> `The BWDS? query returns the definitions for the current break waveform of the specied pins.`
> ——**`specied` 应为 `specified`**。**本页正文引了整句，按错字照抄。**
> **代价写清楚：拿 `specified pins` 去 raw 里搜是搜不到的，要搜 `specied`。**
> **② `break_waveform_index` 的释义自相矛盾。** 前一句给 `an integer in the range 0 to 3`，
> 后一句说 `can only be used to select the default break waveform (DEF)`——
> **两句都在本篇里，谁对谁错本篇没说。本页两处并列照引，不替它裁定。**
> **③ `mode` 写着 `NOT USED.`，但语法里 `[mode]` 这个可选位还在。**
> **这是原文的留白，本页照记。**
> **④ 一句语法错误照实引**：`Receive edge are always denoted by rn.`
> ——**`Receive edge` 单数配 `are`**（本页正文引了整句，照抄）。
> **⑤ `Parameters` 那一节没有 `##` 段标记**（见上）。
> **同一份文档里 `BWDS` / `BWDS?` / `Parameters` 三个标题只有前两个带 `##`**——
> **这是压平后的段结构，本页照记，不替它补 `##`。**
> **⑥ 参数名两处不同**：语法与参数释义写 `wvf_set`，而报错段第一条写的是
> `waveform_set is greater than the range allowed by the command WSUS, WSUS? - (Waveform Sets USed).`
> ——**同一篇里同一个参数两个名字。**
> **（[[bwdf]] 那一篇有同样的一处，两篇是同一种毛病——本页不替它们统一。）**
> **⑦ 链接被拆成三段，其中一段的链接文字就是 `, `（逗号加空格）。**
> 原文那句是三个首尾相连的 markdown 链接、目标都是同一篇 BWDF，
> **三段链接文字依次是 `BWDF`、`, `、`BWDF?`**；
> **而且第三段之后紧跟着 `for`，中间连空格都没有**——
> **所以「读成文字」之后是 `BWDF, BWDF?for setups with 14 or more edges.`**
> **本页引这一句时只引到 `BWDF, BWDF?` 为止**（**截取只许发生在引文的头尾，§11.1**），
> **后半句用散文说明，不把那个缺空格的地方当成原文引文。**
> **⑧ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
