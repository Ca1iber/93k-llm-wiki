---
type: object
title: DFPR, DFPR? - (DeFine Pin Role)
layer: L1
stage: pin
tags: [pin, dfpr, pin-alias, alias-set, pin-configuration, command, query, l1]
related: [pin, udpr, alias-set-editor, pin-configuration-file, dfpn, dfgp, command-reference, smartest-6.5.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# DFPR, DFPR? - (DeFine Pin Role)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,326 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFPR

```
DFPR "alias_set_name","pin_alias", (package_pin_name)
```

### DFPR

```
DFPR?DEF|ALL, (alias_set_name::pin_alias|alias_set_name|@)
```

returns:

```
DFPR "alias_set_name", "pin_alias", (package_pin_name)
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112436.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：alias_set_name | The alias set name. If you assign a pair of pin alias and package pin name to a nonexistent alias set, an alias set is created named with this …

### Examples

### Generic case

The pin configuration file includes three pins: `CP`, `S0`, and `S1`. There are two alias sets, `FUNC` and `TRANS.`

FUNC

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112436.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Alias | Pin

TRANS

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112436.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：Alias | Pin

The following examples are the operations of these sets.

### Example 1

```
DFPR? DEF,(@)
```

returns

```
DFPR "FUNC","CLK",(CP)
DFPR "TRANS","Read",(S0)
DFPR "TRANS","Write",(S1)
```

This example returns the names of all defined alias sets together with their defined pin aliases. This query will not return the pins without aliases.

### Example 2

```
DFPR? ALL,(FUNC,TRANS)
```

returns

```
DFPR "FUNC","CLK",(CP)
DFPR "FUNC", "S0",(S0)
DFPR "FUNC", "S1",(S1)
DFPR "TRANS","CP",(CP)
DFPR "TRANS","Read",(S0)
DFPR "TRANS","Write",(S1)
```

This example returns the pin aliases for all pins in the alias sets `FUNC` and `TRANS`. For the pins without aliases, the package pin names are returned.

### Example 3

```
DFPR? DEF,(TRANS)
```

returns

```
DFPR "TRANS","Read",(S0)
DFPR "TRANS","Write",(S1)
```

This example returns the defined pin aliases in the alias set `TRANS`. This query will not return the pins without aliases.

### Example 4

```
DFPR? DEF,(FUNC::CLK)
```

returns

```
DFPR "FUNC","CLK",(CP)
```

This example returns the package pin name `CP` which is related to the pin alias `CLK` in the alias set `FUNC`.

### Example 5

```
DFPR "TRANS","CLK",(CP)
```

This example adds the package pin `CP` and its alias `CLK` to the alias set `TRANS`. Now the alias set `TRANS` is as the following.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112436.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：Alias | Pin

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the package pin name has not been defined.

<!-- 报错节 end -->

## 是什么

**`DFPR`（DeFine Pin Role）管的是「pin alias（pin 别名）」。** 原文前三句就把定义、查询、**前置条件**讲完了：

> 「The DFPR command defines the pin alias sets and the relation between pin alias and package pin names.
> The DFPR? query returns a list of the package pin names and their pin alias. Before you use the DFPR
> command, the package pin name must have been defined in the Pin Setting Editors.」

（原文里 `DFPR` / `DFPR?` 带反引号，本页引文按 §11.1 ③ 去掉反引号；三个句子在 raw 里是**同一行**，
本页按 §11.1 的「跨段合并不算错、丢字符才算错」分成了三行，**一个字没动**。）

**三句话三个要点**：

| 句 | 说的是什么 |
|---|---|
| `defines the pin alias sets and the relation between pin alias and package pin names` | **建两样东西**：alias set（别名集）**和**「别名 ↔ package pin 名」的对应 |
| `The DFPR? query returns a list of the package pin names and their pin alias` | **查询返回成对的东西**：package pin 名 + 它的别名 |
| `Before you use the DFPR command, the package pin name must have been defined in the Pin Setting Editors`（这一句是从原文那一行里切出来的**一段连续文字**） | **前置条件**：pin 本身得先在 GUI 里存在 |

**第二句是本页的价值所在**：这不是「给 pin 起个外号」那么简单——
**它建的是一张映射表，而这张表有名字（alias set）**。
**第三句是最容易撞的一条**：`Before you use` 是硬前提，**撞它的报错就是本页「报错条件」节里那唯一一句**。

### 一条定义 = 一个三元组

`DFPR` 的语法（逐字见「语法 / 参数」节）是三段：

```
DFPR "alias_set_name","pin_alias", (package_pin_name)
```

| 段 | 参数名 | 原文对它的说明 |
|---|---|---|
| 1 | `alias_set_name` | 「The alias set name.」 |
| 2 | `pin_alias` | 「The pin alias.」 |
| 3 | `package_pin_name` | 「The package pin name.」 |

**三段里只有第一段带「会自动创建」的语义**：

> 「If you assign a pair of pin alias and package pin name to a nonexistent alias set, an alias set is created named with this parameter.」

**即：alias set 不用先建。** 写一个不存在的集合名，**它就被建出来**——
**这是本页最实用的一条**，Example 5 就是它的实例。
（**反过来说**：本篇**没有**「先声明一个空集合」的写法，也**没有**「删除一个集合」的写法——**后者在本篇里一个字没有**。）

**「一个 alias 能不能同时属于两个集合」本篇没有明写**，但 Example 5 的结果表把它示范出来了：
同一个 `CLK→CP` 在 `FUNC` 里有一份，写进 `TRANS` 之后 `TRANS` 里也有一份，**`FUNC` 那边没有变化**
（**推断，依据是 Example 5 的说明句 + 它给的那张结果表**）。

### `DFPR?` 的三个「查什么」

查询语法的括号里写了三种形态（逐字）：

```
DFPR?DEF|ALL, (alias_set_name::pin_alias|alias_set_name|@)
```

| 形态 | 查的是 | 例子 |
|---|---|---|
| `alias_set_name::pin_alias` | **一个别名**（集合与别名用 `::` 连） | Example 4 |
| `alias_set_name` | **一个 alias set** | Example 2 / 3 |
| `@` | **全部已定义的 alias set** | Example 1 |

> 「In the query, you can define multiple alias sets or use the symbol @ to list all the defined pin alias sets.」

**注意 `multiple alias sets` 说的是「查询里可以写多个集合名」**（Example 2 就是两个）——
**它说的不是定义时能一次写多个**（见「典型用法」最后一段）。

### `DEF` 与 `ALL` 只差一件事

| 取值 | 原文 | 没有别名的 pin 怎么办 |
|---|---|---|
| `ALL` | 「If you select ALL in the query, for the pins without aliases, the package pin names are returned.」 | **用 package pin 名顶上**（输出里看起来像「有别名」） |
| `DEF` | 「If DEF is chosen in the query, only the defined pin aliases are returned.」 | **不返回** |

**⚠️ 这一格最容易读错**：`ALL` **不是**「返回所有东西」，**它是「把没有别名的 pin 也用本名报出来」**。
返回串里 `DFPR "FUNC", "S0",(S0)` 这种「别名和 pin 名一模一样」的行，**就是 `ALL` 补出来的**
（推断，依据是 `ALL` 那句说明与 Example 2 的输出逐行对照）。

### 五个例子：一张表读完

原文 `## Examples` 给了五条，**四条查、一条写**。前提逐字：

> 「The pin configuration file includes three pins: CP, S0, and S1.」

（原句里三个 pin 名带反引号，本页按 §11.1 ③ 去掉。）

| # | 命令（逐字） | 做的是 | 返回几行 |
|---|---|---|---|
| 1 | `DFPR? DEF,(@)` | 全部集合、**只列定义过的别名** | 3 |
| 2 | `DFPR? ALL,(FUNC,TRANS)` | 两个集合、**没有别名的 pin 用本名顶上** | 6 |
| 3 | `DFPR? DEF,(TRANS)` | 一个集合、只列定义过的别名 | 2 |
| 4 | `DFPR? DEF,(FUNC::CLK)` | **一个别名 → 反查它的 package pin** | 1 |
| 5 | `DFPR "TRANS","CLK",(CP)` | **写**：往 `TRANS` 里加一条 | （不返回，改的是状态） |

**Example 2 是唯一能看出 `ALL` 效果的一条**：`FUNC` 里只定义过 `CLK→CP` 一条，
**而返回了 3 行**——`S0` / `S1` 是用它们自己的名字顶上的。

> **（推断）`ALL` 会把「这个集合涉及到的每一个 pin」都列一行**，
> 即 **行数 = 集合数 × pin 数**（本例 2 × 3 = 6）。依据是 Example 2 的说明句
> 「This example returns the pin aliases for all pins in the alias sets FUNC and TRANS.」
> 与那 6 行输出。**本篇没有把这条写成规矩**，所以本页只当推断用。

**Example 5 是唯一一条写操作，也是「自动建集合」的实例**：

> 「This example adds the package pin CP and its alias CLK to the alias set TRANS.」（原文三个名字带反引号，已按 §11.1 ③ 去掉）

### `## Errors`：只有一条，而且它是一句前置条件

（逐字见本页「报错条件」节。）

> 「An error is generated if the package pin name has not been defined.」

**这一条正好是开头那句 `Before you use` 的报错面。**
**注意它的主语是 `the package pin name`，不是 `alias_set_name`**：

| 情况 | 会不会报错 |
|---|---|
| `package_pin_name` 没定义过 | **报错**（这一条就是） |
| `alias_set_name` 不存在 | **不报错**——它**会被创建**（Parameters 那一格明写） |
| `pin_alias` 不存在 | **不报错**——别名正是你要建的东西 |

**后两行是推断**，依据是「唯一的报错只点了 package pin 名」+「不存在的集合会被创建」两句合读；
**本篇没有正面写「查一个不存在的集合会怎样」**。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法全部来自 `## Examples` 那五条与 `## Parameters` 那张表。**按目的查**：

| 要做的 | 发什么 | 依据 |
|---|---|---|
| **建一个别名集，并加进第一条别名** | `DFPR "TRANS","CLK",(CP)` | Example 5 逐字 |
| 往已有集合再加一对 | 同上 | 「If you assign a pair of pin alias and package pin name to a nonexistent alias set, an alias set is created named with this parameter.」（**存在则直接用——这一半本篇没写**） |
| **列出全部集合里定义过的别名** | `DFPR? DEF,(@)` | Example 1 |
| 列出某几个集合里的**所有 pin**（没别名的用本名顶） | `DFPR? ALL,(FUNC,TRANS)` | Example 2 |
| 列出某集合里**定义过的**别名 | `DFPR? DEF,(TRANS)` | Example 3 |
| **反查**：某个别名是哪个 package pin | `DFPR? DEF,(FUNC::CLK)` | Example 4 |

**顺序上的两个前提**：

1. **先有 package pin，后有别名**——原文第三句 + 那唯一一条 Error。
2. **查之前得先写过**。`DEF` 类查询「will not return the pins without aliases」，
   **所以一个集合刚建好、一条别名都还没定义时，对这个集合发 `DFPR? DEF,(集合名)` 的返回应该是空的**
   （推断，依据是 Example 1/3 的说明句；**本篇没有「空集合返回什么」的例子，本页不替它编**）。

**一次写多对 / 一次写多个集合：语料未写。** 本篇只给了**单条**写法（Example 5 一条命令一对），
`## Parameters` 里那个 `multiple` 说的是**查询**（`In the query, you can define multiple alias sets or use the symbol @ to list all the defined pin alias sets.`）。

## 和谁有关

- [[udpr]] —— **反向命令**（页标题 `UDPR - (UnDefine Pin Role)`）。**本篇一个字没提过它**——
  两者的并列只出现在入边里，逐字（原文两段都是链接，本页按 §11.1 ② 剥掉）：
  > 「Commands for pin alias: DFPR, UDPR」
  这条在 `02.06.03.01.01_Introduction.md` 与 `02.06.03_Pin_configuration_setup_commands.md` 里**各有一条**。
  **本页没有读 [[udpr]]。**
- [[alias-set-editor]] —— **GUI 侧**，也是最可能的入边来源之一：有一条入边来自
  `02_08_Setup_and_Result_Tools/02.08.04.18.01.04_Alias_set.md`（那篇的标题就是 `Alias set`），
  它的链接行逐字（同样剥掉标记）：
  > 「DFPR, DFPR? - (DeFine Pin Role)UDPR - (UnDefine Pin Role)Creating a new format」
  ——**三段链接粘在一行、中间一个分隔符都没有**（这是 raw 的毛病，见「出处」⚠️ ⑦）。
  **本页没读那一篇**，所以 GUI 上长什么样本页没有。
- [[pin]] —— **本阶段（`stage: pin`）的脊椎页**。
- [[pin-configuration-file]] —— **`package_pin_name` 的来处**。**注意别顺口接错**：
  本篇写的是 **`Pin Setting Editors`（一个 GUI）**，**不是配置文件**——
  **本页不把两者等同**（**本页未读该页**）。
- [[dfpn]] / [[dfgp]] —— **同族的定义型命令**（`DFPN` 的页标题是 `DFPN, DFPN? - (DeFine Pin Name)`，
  `DFGP` 是 `DeFine GrouP`）。**本篇没有提过它们**（实测 `DFPN` / `DFGP` 0 命中）——
  **「package pin 名由 `DFPN` 定义」这一句是推断**，依据是本篇的前置条件（pin 名必须先定义）+ 那两个页标题。
  **本页没有读这两篇。**
- [[command-reference]] —— **它的归属**：本篇在 `02.06_Command_Reference` 下。
- [[smartest-6.5.2]] —— **版本落点**，见下。

## 版本

`## Functional changes` 段有，**只有一条**：

```
- Introduced in SmarTest 6.5.2
```

**这一条不是哨兵值**：措辞是 `Introduced in`（**不是 `before`**），
所以按字面读就是「**6.5.2 引入**」——与 §11.2 ② 那种 `Introduced before SmarTest 6.3.2` 的写法**不是一回事**
（对照 `[[udgp]]` 那一页：它拿到的是哨兵值，本页拿到的是真版本号）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md`
（TDC `112436.htm`，**3,762 字节 / 252 行**）。**整篇读完**——本页引文全部来自这一篇 + `edges.jsonl` 里带原句的边。

**入边 5 条 / 5 篇**（`inline` + `toc` 口径）：
`02.06.02.02_List_of_commands`、`02.06.03.01.01_Introduction`、`02.06.03_Pin_configuration_setup_commands`、
`02.08.04.18.01.04_Alias_set`、`02_System_reference/index.md`。
**五条全是整篇引用，一条锚点都没有**（`anchor` 字段全为 `null`）。

**本页没做的**：

- **`UDPR` 没读。** 所以「怎么撤掉一个别名 / 撤掉一个 alias set」**本页一个字没有**。
- **`Alias_set.md`（`02.08.04.18.01.04`）没读。** 所以「GUI 上 alias set 长什么样、怎么建」**本页没有**。
- **`Pin Setting Editors` 那篇 GUI 文档没读**——而本篇的**前置条件与唯一一条 Error 都挂在它身上**。
  **它叫什么、在哪一节、怎么定义 pin 名，本页一概不知道。**
- **`DFPN` / `DFGP` 没读**（见「和谁有关」那一节）。
- **四条入边文档一篇没读**：本页引它们的话，**只引 `edges.jsonl` 里那条带原句的边**，
  **没有回原文核上下文**。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **编码坏字：本篇 0 处**（`[一-鿿]` 扫过整篇，**一个汉字都没有**）；
  **整词替换（`DC/DC power units`）本篇 0 命中**。**两条都是实测结果，不是没查。**
- **没有实跑。** 没有在机台上发过 `DFPR` / `DFPR?`、没有建过 alias set、没有触发过那条 Error。
  `verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[pin]]。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① 句号被包进了代码跨度。** 那一句逐字（放在代码块里，免得本页的引号把它再切碎一次）：
>
> ```
> The pin configuration file includes three pins: `CP`, `S0`, and `S1`. There are two alias sets, `FUNC` and `TRANS.`
> ```
>
> ——**`TRANS` 后面那个句号在反引号里面**，于是句号成了「代码」的一部分；
> **同一句里的 `CP` / `S0` / `S1` / `FUNC` 都没有这个问题**。**本页照原样记，不替它把句号挪出来。**
>
> **② 同一篇里有两个同名 `##` 小节。** 原文的 `## DFPR` 出现**两次**（先讲定义语法、再讲查询语法），
> **骨架里因此是两个 `### DFPR`**——**不是脚本切重了，是 raw 里就这两个同名标题**
> （一个 13 行的定义式、一个 19 行的查询式）。
>
> **③ 语法模板与例子里的空格不一致。** 模板逐字是
> `DFPR?DEF|ALL, (alias_set_name::pin_alias|alias_set_name|@)`（**`?` 后没有空格**），
> 而五条例子全是 `DFPR? DEF,(@)`、`DFPR? ALL,(FUNC,TRANS)` 这种形态（**`?` 后有空格**）。
> 定义模板逐字是 `DFPR "alias_set_name","pin_alias", (package_pin_name)`，
> 而 `returns:` 底下那一行逐字是 `DFPR "alias_set_name", "pin_alias", (package_pin_name)`
> ——**同一个命令，同一个冒号后，两种空格。**
>
> **④ Example 2 的输出里空格同样不一致。** 逐字四行：
> `DFPR "FUNC","CLK",(CP)` / `DFPR "FUNC", "S0",(S0)` / `DFPR "FUNC", "S1",(S1)` / `DFPR "TRANS","CP",(CP)`
> ——**有的第一个逗号后有空格，有的没有**（同一段输出里混着两种）。
>
> **⑤ `Parameters` 表在 raw 里被压平。** `alias_set_name` / `pin_alias` / `package_pin_name` / `DEF|ALL`
> 四格的说明都散成「一格一行 + 游离 `|`」，`pin_alias` 与 `package_pin_name` 前面**还各多一对空的 ` |`**。
> **说明文字一个字没丢**，但**表头（`Parameter` / `Description` 之类）本篇 raw 里没有**。
>
> **⑥ `## Application` 与 `## Errors` 都不在本页「语法 / 参数」节里。** 脚本按段标记抽（§4），
> 那一节收的是**两个 `## DFPR` + `Parameters` + `Examples`**。
> `## Application` 整节只有一句 `Configuration setup. See Configuration Setup Commands.`
> （已写进上面的「是什么」），`## Errors` 那一句在「报错条件」节里。
>
> **⑦ 入边那篇 `Alias_set.md` 的链接行没有任何分隔符。** 逐字：
> `[DFPR, DFPR? - (DeFine Pin Role)](<../02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md>)[UDPR - (UnDefine Pin Role)](<../02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.md>)[Creating a new format](<02.08.04.33.01.07_Creating_a_new_format.md>)`
> ——**三段链接首尾相接**（本页在「和谁有关」里引的那一句就是它剥掉标记后的样子）。
> **这不是本页的引用错误，是 raw 如此**；而本页**没读那一篇**，**所以它原文是不是一节列表，本页不知道。**

`verified: doc-only`
