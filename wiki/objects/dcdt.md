---
type: object
title: DCDT, DCDT? - (Device Cycle DefaulT)
layer: L1
stage: timing
tags: [timing, device-cycle, command, l1, waveform-set, specset, multiport, pattern, wavetable, equation-based]
related: [timing, wsus, clkr, etim, etds, pclk, pattern-tool, timing-setup-commands, waveform-set, wavetable, timing-specification, command-reference, clmp, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DCDT, DCDT? - (Device Cycle DefaulT)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **328 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DCDT

```
DCDT {waveform_set}, {"default_name"}
```

### Example

```
DCDT 1,"HOLD"
```

This example defines the default device cycle name HOLD for Waveform Set 1.

```
DCDT? "fast_ARM",(ARMPort)
DCDT "fast_ARM","Cycle",(ARMPort)
```

This example queries the default device cycle name for the ARMPort port in the multi-port specification fast_ARM.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the WSUS command.
- waveform_set is smaller than one.
- You enter an illegal device cycle name (a reserved name, a name containing illegal characters).
- wavetable_name does not reference a defined wavetable.
- specset_id does not reference a defined wavetable.
- specset_id is invalid because equation_set_no, specset_no or both are invalid.
- multi-port_spec does not reference a defined multi-port specification.

<!-- 报错节 end -->

## 是什么

**`DCDT` 定义的是「默认器件周期名」（default device cycle name）。**
**它的用途只有一个：多模（multi-mode）下要同步两条以上向量流时，用它补测试系统的周期。**

> 「The DCDT (Device Cycle DefaulT) command defines the default device cycle name. The command is used to name a device cycle that will be used to pad out test system cycles in order to synchronize two or more vector streams in multi-mode applications.」

**`pad out test system cycles` 是本命令的全部机制**——
**它不产生新的时序，它给「用来填空的那个周期」起一个名字**，
好让多模下不同的向量流有一个共同的参照。

上电时这个名字是空的，查询在这种情况下返回空串：

> 「At power-up the name is undefined (empty string). The DCDT? query returns the defined default name for the device cycle. If no default name is defined, then "" is returned.」

### 命令一个签名，查询四个（**本页最容易看漏的一处**）

| 形态 | 签名（原文） |
|---|---|
| `DCDT` | `DCDT {waveform_set}, {"default_name"}` |
| `DCDT?`（按 waveform set） | `DCDT? {waveform_set}` |
| `DCDT?`（按 wavetable 名） | `DCDT? {"wavetable_name"}` |
| `DCDT?`（按 specset_id） | `DCDT? {specset_id}` |
| `DCDT?`（按 multi-port 规范） | `DCDT? {"multi-port_spec"}[, (portlist)]` |

**四个返回式**（原文都是 `returns:` 后面接一段）：

| 查询 | 返回（原文逐字） |
|---|---|
| `DCDT? {waveform_set}` | `DCDT {waveform_set},{"default_name"}` |
| `DCDT? {"wavetable_name"}` | `DCDT {"wavetable_name"},{"default_name"}` |
| `DCDT? {specset_id}` | `DCDT {specset_id}, {"default_name"}` |
| `DCDT? {"multi-port_spec"}[, (portlist)]` | `DCDT {"multi-port_spec"},{"default_name"} [, (portlist)]` |

**四行里的逗号不一样**：第一、二行是 `},{"`（**中间无空格**），
第三、四行是 `}, {`（**中间有空格**）。**原文如此，本页照录，没替它统一。**
（前三个查询式还各自被 `or:` / `or, for multiport specifications:` 这类词串起来，
**不是并列的表格，是一条链**——照原文读。）

**这四个查询签名在 raw 里都不在任何「段标记」之下**，所以**一个都没进本页的「语法 / 参数」节**
——原因见 `## 出处` ⚠️①。

### 三个名字只能用在查询上（**本命令最容易踩的一条**）

> 「Note specset_id, multi-port_spec, and wavetable_name can only be used with the DCDT? query. They are not allowed with the DCDT command because overrides are only allowed with the CLKR, ETIM(ETDS for 14 or more edge setups), and PCLK commands.」

**即：`DCDT` 命令只认 waveform set 加一个名字；要按 wavetable / specset / multiport 去问，
只能用 `DCDT?`。** 原文给的**理由是「覆盖只在另外三条命令上允许」**——
那三条是 `CLKR`、`ETIM`、`PCLK`（→ [[clkr]] / [[etim]] / [[pclk]]）。

这句还顺带交代了一件事：**`ETIM` 与 `ETDS` 是同一件事的两种形态**
（原文的括号写法是 `ETIM(ETDS for 14 or more edge setups)`）。

（推断）**这条 Note 与 `## Errors` 后四条连起来看，报错其实是两组**：
前三条（`waveform_set` 超出 `WSUS` 范围、`waveform_set` 小于 1、非法器件周期名）
**命令与查询都可能触发**；后四条（`wavetable_name`、`specset_id` 两条、`multi-port_spec`）
**只可能来自查询**——因为这三个名字按上面这条 Note 不许用在 `DCDT` 上。
**依据就是这两句话的交叉，原文没有一句话这么分过组。**

### 六个参数各自怎么来

| 参数 | 原文要点 |
|---|---|
| `waveform_set` | 「Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`. For the query, you can also enter ALL for all waveform sets.」（那句 `WSUS, WSUS? - (Waveform Sets USed)` 在 raw 里是指向 `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md` 的链接） |
| `specset_id` | 「Derived as follows:」+ `100 * equation_set_no + specset_no` |
| `multi-port_spec` | 「To query a multi-port specification, enter the name of the specification.」 |
| `wavetable_name` | 「The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. The appropriate wavetable is determined by looking at which wavetable is referenced by equation_set_no and specset_no in the Timing Specification File.」 |
| `default_name` | 「Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes.」 |
| `portlist` | 「For multi-port specifications, you can restrict the query to the ports specified here. The ports must be defined in the pin configuration and used in the specified multi-port specification.」 |

**三条要点：**

- **`waveform_set` 的上限由 `WSUS` 决定**（不是本文档自己给的数），**查询时还可以写 `ALL`**。
- **`specset_id` 的算法是 `100 * equation_set_no + specset_no`**——
  **`specset_no` 只占两位**。原文**没有**写 `equation_set_no` 与 `specset_no` 各自的取值范围。
- **两个长度不是一回事**：`wavetable_name` 最长 **40** 个字母数字，`default_name` 最长 **16** 个。
  **读快了会串。**

### 名字的合法性：保留名与非法字符

`default_name` 那一格逐字：

> 「Reserved names are not allowed - these are the character sequences scan, SCAN, c, C and BREAK. Illegal characters are also not allowed - these are #, (, ), ,, ;, ?, @ and *.」

**两条要点：**

- **保留名里包含单个字母 `c` 与 `C`**——**`c` 不能当器件周期名**。
  列出了 `scan` 与 `SCAN` 两种大小写，**但没有 `Scan`**。
- **非法字符那一串里的 `,,` 有歧义**：它到底是「一个逗号这个字符」还是「两个逗号」，
  **字面读不出来**（列表本身就是逗号分隔的）。**本页不判，照原样引**（见 `## 出处` ⚠️④）。

### `## Application` 说的「设在哪、用在哪」

> 「Set in Timing Setup (Timing Setup Commands), used in Pattern Tool.」

**即：设置在 Timing Setup 那一章里，而用在 Pattern Tool 里。**
**这是本篇唯一一句讲位置的话**（`Pattern Tool` 与 `Timing Setup Commands` 原文都没给链接）。

## 典型用法

**先说范围**：这一篇**没有 `## Procedure`，也没有 `## Before you begin`**，
能当过程线索的只有上面那句 `## Application`。

**原文只有两组例子，第二组的读法本身是个坑。**

**1. 定义一个默认名（`DCDT`）**

```
DCDT 1,"HOLD"
```

原文说明：`This example defines the default device cycle name HOLD for Waveform Set 1.`
—— **`1` 是 waveform set 号，`"HOLD"` 是默认器件周期名**（双引号是语法的一部分）。

**2. 按 multi-port 规范查询（`DCDT?`）**

raw 里这一组是**两行连排、只配一句说明**：

```
DCDT? "fast_ARM",(ARMPort)
DCDT "fast_ARM","Cycle",(ARMPort)
```

原文说明：`This example queries the default device cycle name for the ARMPort port in the multi-port specification fast_ARM.`

**这一句说明只讲了「查询」，没讲第二行是什么。两种读法：**

| 读法 | 依据 | 后果 |
|---|---|---|
| **① 第二行是查询的回复**（本页倾向这个） | 它的形状与上面第三个返回式 `DCDT {"multi-port_spec"},{"default_name"} [, (portlist)]` **逐字对得上** | 与前面那条 Note **不冲突** |
| **② 第二行是一条 `DCDT` 命令** | 它写的是 `DCDT` 而不是 `DCDT?` | **与 Note 直接冲突**（`multi-port_spec` 不许用在 `DCDT` 上），**也与 `DCDT {waveform_set}, {"default_name"}` 的签名冲突**（第一个位置本该是整数 waveform set，这里给的是带引号的字符串） |

**本页并列两种读法，不替语料裁定**（见 `## 出处` ⚠️③）。
**编号 ①② 在这里只是这两个读法的序号，不是 §11.4 的证据档号。**

**3. 按本篇能拼出来的顺序**

1. **先定 waveform set 的上限**：上限来自 `WSUS`（**那篇本页没读**）。
2. **发 `DCDT {waveform_set}, {"default_name"}` 写默认名**——名字要
   **≤ 16 个字母数字、双引号包起来**，**不能是保留名**（`scan` / `SCAN` / `c` / `C` / `BREAK`），
   **不能含** `# ( ) , ; ? @ *`。
3. **要核对就查回**：按 waveform set（`DCDT? {waveform_set}`）；上电还没定义时**返回的是空串**。
4. **equation-based 或多模的场合**改用另外三个查询：
   `DCDT? {"wavetable_name"}` / `DCDT? {specset_id}` /
   `DCDT? {"multi-port_spec"}[, (portlist)]`——**这三种只能查、不能写**。

**4. 一个本篇答不了的问题**：`DCDT` / `DCDT?` 是不是也按「setup 焦点」写配置？
**本篇全文 0 处出现 `focus` 这个词**，所以**「要不要先设焦点」本篇一个字都没写**。
**不能因为它是 `02.06.02.02` 那一批命令就假定它要**——依据就是上面那个「0 处」。

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[timing]] | **本页 `stage: timing` 的理由**：`## Application` 说它设在 Timing Setup 那一章 | frontmatter + 本篇 `## Application` |
| [[wsus]] | **上限来源**：`waveform_set` 的最大数由 `WSUS` 定——**原文给了链接** | 本篇参数节 |
| [[clkr]] | **同类命令之一**：原文说 overrides 只在这三条命令上允许 | 本篇那句 Note |
| [[etim]] | 同上；**这句还给出 `ETIM` 与 `ETDS` 的关系**（`ETIM(ETDS for 14 or more edge setups)`） | 本篇那句 Note |
| [[pclk]] | 同上 | 本篇那句 Note |
| [[etds]] | 上面那条 Note 把 `ETDS` 写成 `ETIM` 的括号别名——**它是 `ETIM` 在边沿数 ≥14 时的形态** | 本篇那句 Note |
| [[pattern-tool]] | **使用场所**：`used in Pattern Tool`——**原文这两个词没给链接** | 本篇 `## Application` |
| [[timing-setup-commands]] | **设置场所那一章**：`Set in Timing Setup (Timing Setup Commands)` | 本篇 `## Application` |
| [[waveform-set]] | **第一个参数数的是它**（`DCDT` 命令与 `DCDT?` 查询都以它为主键） | 本篇参数节 |
| [[wavetable]] | **查询入口之一**（`wavetable_name`）；**该查哪个 wavetable 由 Timing Specification File 反查** | 本篇参数节 |
| [[timing-specification]] | `wavetable_name` 那一格说的判定依据是 `Timing Specification File` | 本篇参数节 |
| [[command-reference]] | **所属章**（`02.06_Command_Reference` / `02.06.02.02`） | 路径 |
| [[clmp]] | **同批另建的相邻命令页**（`02.06.02.02.26` 与 `02.06.02.02.41`）；**本篇一个字都没提它**，关系只是并列 | 路径；**本页不声称任何内容上的关系** |
| [[smartest-6.3.2]] | **版本页**：本篇唯一那条 `## Functional changes` 落在它身上 | 本篇 `## Functional changes` |
| `multi-port specification` / `portlist` / `Timing Specification File` / `pin configuration`（**均未建，不链**） | 参数节与 `## Application` 提到的四个东西，**本篇都没给链接** | 本篇参数节 |

**未读**：`WSUS, WSUS? - (Waveform Sets USed)`（`02.06.02.02.342`）、
`Timing Setup Commands`（`02.06.06`）——**所以「上限是多少」「Timing Setup 里在哪个界面设」
本页答不了**。

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，只有一条，逐条转录**：

- `Introduced before SmarTest 6.3.2`

**这一条是哨兵值**（§11.2 ②）：它的意思是
「**在本文档集覆盖范围开始之前就已经有了**」，
**不是「SmarTest 6.3.2 新增了 `DCDT`」**。
**照字面读会生成一条「6.3.2 新增了器件周期默认名」的假信息，而格式齐整、看不出来。**

**所以本页只知道一件事：`DCDT` 早于本文档集覆盖范围。**
**它之后有没有改过，本篇没有记录——「没记录」不等于「没改过」**（§13.1）。

版本页：[[smartest-6.3.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.md`
（TDC `98520.htm`；**3,893 字节 / 161 行**，全文 CRLF，末行带换行。
**本节的行数口径是 `wc -l`（= `splitlines()`），不加 1**，见 §11.5）。**整篇读完。**

**本页没做的**：

- **原文链到的两篇一篇都没读**：`WSUS, WSUS? - (Waveform Sets USed)`（`02.06.02.02.342`）、
  `Timing Setup Commands`（`02.06.06`）。
  **所以「waveform set 的上限是多少」「Timing Setup 里在哪儿设这个默认名」本页一个字都没有。**
- **`CLKR` / `ETIM` / `PCLK` / `Timing Specification File` / `Pattern Tool` /
  `pin configuration` 六处点名都没有链接，也一篇没读**——
  **所以「覆盖（override）是怎么一回事」「多模规范长什么样」本页答不了。**
- **图一张没看——因为这一篇里没有图**（全文 **0 处** `.png` / `.jpg` / `raw/`）。
  **所以本页没有任何来自图的结论**；这与「图够不着」不是一回事（§11.4）。
- **没有 `## Procedure` / `## Before you begin` 可读**，
  所以「典型用法」第 3 点那四步是**本页按参数节与两个例子拼的**，不是文档给的流程。
- **查询的四个签名一个例子都没有**：原文的第二个例子只演示了 multi-port 那一种，
  **`DCDT?` 按 waveform set / wavetable 名 / specset_id 三种查询，本篇没有例子**。
- **没有用 `edges.jsonl`**，故不报入边/出边条数。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **`DCDT?` 的签名没进「语法 / 参数」节，原因是 raw 里那一行底下是空的**：
> 紧挨着的两行是
>
> ```
> ## DCDT?
>
> ## DCDT? {waveform_set}
> ```
>
> ——**第一个 `## DCDT?` 是个空标题**，真正的签名**写在下一个标题行里**
> （所以它成了一个标题，而不是一段语法）。脚本只收 `Syntax` / `Parameters` / `Example`
> 这类段标记下的内容，**抓不到它**。**本页照实记，没替它改标题层级。**
> ② **`wavetable_name` 这个参数名在参数表里被拆成两行**：格子里先写 `wavetable_`、
> 换行再写 `name`——**拿 `wavetable_name` 去搜这一格是搜不到的**
> （`## Errors` 一节里那个 `wavetable_name` 才搜得到）。
> ③ **第二个例子与前面那条 Note 打架**：Note 说
> `They are not allowed with the DCDT command because overrides are only allowed with the CLKR, ETIM(ETDS for 14 or more edge setups), and PCLK commands.`，
> 而例子第二行是 `DCDT "fast_ARM","Cycle",(ARMPort)`。
> **两种读法并列在「典型用法」第 2 点，本页不判**（§10）。
> ④ **保留名与非法字符那一串有两处不齐**：
> `scan, SCAN, c, C and BREAK` —— **`Scan` 没列，`c` 与 `C` 都列了**；
> `#, (, ), ,, ;, ?, @ and *` —— **`,,` 到底是「一个逗号」还是「两个逗号」，字面读不出来。**
> ⑤ **四个返回式的逗号空格不统一**：`DCDT {waveform_set},{"default_name"}` 与
> `DCDT {"wavetable_name"},{"default_name"}` 是 `},{"`；而
> `DCDT {specset_id}, {"default_name"}` 与 `DCDT {"multi-port_spec"},{"default_name"} [, (portlist)]`
> 是 `}, {`。**同一页两种写法，照录。**
> ⑥ **`Note` 后面没有冒号**：`Note specset_id, multi-port_spec, and wavetable_name can only be used with the DCDT? query.`
> ——**原文如此**（引文里没替它补冒号）。
> ⑦ **两个 `specset_no` 的进位方案跨篇不一致**（**对照同批另建的 `02.06.02.02.26` CLMP 篇，
> 那一篇本页也读了**）：本篇的 `specset_id` 是 `100 * equation_set_no + specset_no`
> （**`specset_no` 占两位**），而 CLMP 篇的 `level_set_id` 是
> `100000 * equation_set_no + 1000 * specset_no + level_set_no`（**同一个 `specset_no` 被 ×1000**）。
> **两篇都没解释这个差别；本页并列两处，不替它们调和，也不声称哪个对。**
> ⑧ **本篇没有坏字**：实测 **0 处非 ASCII 字符**（没有 `鈥` / `渭` / `碌` 那一族）。
> **但这是「本页量过的」，判据只是这一个文件**；§11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上发过 `DCDT`，也没有验证过多模下
「填空周期」真的能同步两条向量流**（§11：文档里有 ≠ 这台机器上能用）。
