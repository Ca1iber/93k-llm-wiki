---
type: object
title: EQSP, EQSP? - (EQuation SPecification transfer)
layer: L1
stage: timing
tags: [L1, timing, level, equation-based, firmware-command, binary-transfer, download-upload, test-program-explorer, equation-set, wavetable, spec-set]
related: [eqfs, timing, level, mapping-timing, mapping-level, timing-file, level-file, wavetable-file, timing-equation-set, spec-set, test-program-explorer, timing-setup-commands, command-reference, equation-based-level-setup, spec-tool, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# EQSP, EQSP? - (EQuation SPecification transfer)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **710 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### EQSP

```
EQSP {spec_type}, {part}, {#spec(data)}
```

### EQSP?

```
EQSP?{spec_type}, {part}
```

returns:

```
EQSP {spec_type}, {part}, {#spec(data)}
```

if these are not empty, for backward compatibility.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98593_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：spec_type | The mandatory parameter defines which specification type to use. Use: LEV to specify levels TIM to specify timing

### Example

The following example queries the current wavetables:

```
> EQSP? TIM,WVT
< EQSP TIM,WVT,#9000000127WAVETBL table1  # derived from waveform set 1

  PINS Pin1 Pin2
  WFDS 0  "d1:D11"
  1    0   .   .   .
  2    1   .   .   .
  BWDS ""

  @
```

<!-- 语法节 end -->

## 是什么

**`EQSP` 是一条 L1 固件命令，而且是成对的两条：`EQSP` 把一整块 equation based 数据下载进固件，`EQSP?` 把固件里「当前」的那一块问回来。**
原文头两句就是这两个方向的完整定义：

> 「The EQSP command downloads an equation based collection of setup data (for example, wavetables or equation sets) in binary format to firmware.」

> 「The EQSP? query returns, in binary format, an equation based collection of the current setup data from firmware.」

| 命令 | 方向 | 原文里的词 |
|---|---|---|
| **`EQSP`** | **setup file → firmware**（下） | 原文里两段：`downloads an equation based collection of setup data` / `in binary format to firmware` |
| **`EQSP?`** | **firmware → 问的人**（上） | 原文：`returns, in binary format, an equation based collection of the current setup data from firmware` |

**三条要读准的：**

1. **搬的是「一个集合」，不是「一项设置」** —— `an equation based collection of setup data`。
   原文自己举的两个例子是 wavetable 与 equation set（`for example, wavetables or equation sets`）。
2. **传输格式是二进制**（`in binary format`）——**两个方向各写了这一句**。
   这决定了第 3 个参数长什么样（见下 `#spec(data)`）。
3. **`EQSP?` 问的是 `current setup data`**——**是固件里现在的那一份，不是「文件里存的那一份」**。
   这两者是不是一回事，**本篇没说**（见「出处」的「本页没做的」）。

### 命令语法：**原文写在 `## EQSP` / `## EQSP?` 两个标题下，不在本页上方那一节里**

> ⚠️ **本页的「语法 / 参数」节只收到 `## Example` 一节（244 字符）。** 这**不是**脚本漏抽：
> **本定义文档没有 `## Syntax` / `## Parameters` 这类段标记**（实测：全文 `Syntax` 出现 **0** 次、
> `Errors` **0** 次、`Warnings` **0** 次；`Parameters` 只出现 **1** 次，而且是**一行没有 `##` 的裸标题**）。
> 两行语法挂在 `## EQSP` 与 `## EQSP?` 两个标题下——按 §4，**没有段标记时「哪一段是语法」是猜，
> 脚本不猜**。**本页一个字都没往那一节里加**；下面这几行是**本页在正文里逐字引出的**，
> 出处是同一篇原文——**不是本页补写的语法。**

原文给了三行。前两行是两个方向的形式：

```
EQSP {spec_type}, {part}, {#spec(data)}
```

```
EQSP?{spec_type}, {part}
```

第三行是 `EQSP?` 的返回形式。原文在那之前写着 `returns:`，
返回行的字面与 `EQSP` 的形式**逐字相同**，而且带一个条件：

> 「if these are not empty, for backward compatibility.」

**`EQSP?` 那个形式里 `?` 与 `{spec_type}` 之间没有空格**，`EQSP` 那个形式里有——
**原文如此，本页照原样引**（见「出处」瑕疵②）。

### 三个参数位

| 位置 | 参数 | 原文（逐字） |
|---|---|---|
| 1 | `spec_type` | `The mandatory parameter defines which specification type to use.` |
| 2 | `part` | `The mandatory parameter defines which part of the specification type to use.` |
| 3 | `#spec(data)` | `An equation based set of data (for example wavetables) in binary format.` |

**前两位都写着 `mandatory`**（原文两句各一次：`The mandatory parameter defines which specification type to use.`
与 `The mandatory parameter defines which part of the specification type to use.`；
**实测 `mandatory` 全文出现两次**，在第 39 行与第 52 行）——**即 `EQSP` 没有「只写命令名」的用法。**

**第 1 位的两个取值，就是「本页跨两级」的依据**：

> 「- LEV to specify levels」

> 「- TIM to specify timing」

**第 2 位原文给了三个取值**：

> 「- EQN to specify equations」

> 「- SPS to specify specs」

> 「- WVT to specify a wavetable」

**但这三个取值后面紧跟一句限制，而那一句里的清单与上面的取值表对不上**——
原文逐字是：

> 「part can only be set to WVT, EQN, or CLK if spec_type is set to TIM.」

**`CLK` 全文只出现这一次**（取值表里没有它），**`SPS` 在这句限制里没有出现**（实测：`CLK` 1 次、
`SPS` 1 次、`EQN` 2 次、`WVT` 4 次）。**两条清单一多一少，本篇没说哪个是现行版——本页不替它判**
（详见「出处」瑕疵①）。

### `#spec(data)`：四条格式说明（这部分原文写得比别处细）

> 「This parameter enables you to define the length of the data (in bytes) and the data itself to be transferred. It has the following format:」

`It has the following format:` 之后是四条列表，逐字如下：

> 「- A # to mark the start of the data block.」

> 「- One digit indicating how many digits make up the data length specifier.」

> 「- A number of digits indicating the length (in bytes) of the data to follow.」

> 「- A number of characters which make up the specified equation based testing file. This stream of characters must be terminated with a @ character.」

**合起来就是一个自描述的块**：`#` + **一位**「长度说明符有几位」+ 那么多位的长度 + 数据本身 + `@` 收尾。

**（推断，依据是上面四条本身 + 本页上方「语法 / 参数」节里那个例子）**：
例子里的 `#9000000127` 按这四条解是「`#` 开头，第一位 `9` 表示长度说明符占 9 位，
后 9 位 `000000127`」→ **127 字节**。
**但这个 127 与例子里实际打印出来的那段数据对不上——见「出处」瑕疵③，本页不判。**

### `## Application`：调用者是谁，以及**「LEV 那一半」在这里被摆明**

> 「- The EQSP command is used in the level and timing setup files.」

> 「- The EQSP? query is used by the test program explorer to generate and save setup files.」

| 谁 | 调哪个 | 原文 |
|---|---|---|
| **level 与 timing 的 setup file** | **`EQSP`** | `used in the level and timing setup files` |
| **test program explorer** | **`EQSP?`** | `used by the test program explorer to generate and save setup files` |

**第一句是本页最要紧的一条**：`EQSP` **同时**用在 level 与 timing 两种 setup file 里，
与第 1 位参数的 `LEV` / `TIM` 两个取值对得上。
**所以 `stage: timing` 填的只是「最近的一段」（§6）**——
**`LEV` 那一半同样在它身上，读者不要以为它只管 timing**（见「和谁有关」的 [[level]]）。

**第二句给出一个具名的 GUI 调用者**：[[test-program-explorer]]。

### 一条必须显式记的「别混」：`EQ` 开头的命令不是同一件事

**命令参考章（`02.06_Command_Reference`）里 `EQ` 开头的命令页有三条，其中一条的 `EQ` 根本不是 `EQuation`**：

| 命令 | 名字展开 | 干什么 |
|---|---|---|
| `EQFS` | `EQuation FileS command transfer` | 编辑器工具用的 **load / save**，两端是**临时文件** |
| **`EQSP`**（本页） | `EQuation SPecification transfer` | **setup file ↔ 固件**之间的整块搬运（本页「是什么」） |
| `EQFC` | `EQualization and Filter Configuration` | **与 equation 无关**：配的是 equalization 与低通滤波器参数 |

**第三行是本页唯一想让人记住的**：`EQFC` 的名字里也有 `EQ`，
**但它是 `EQualization`，不是 `EQuation`——它不搬任何 equation based 数据。**

**（这一节的取材边界，实测）** **全语料里「`EQ` + 字母」形式的命令名一共四个**：
`EQFC`（2 份投放）、`EQFS`（4 份）、`EQSP`（4 份）、`EQNSET`（1 份）。
**第四个 `EQNSET` 不在这条对照里**：它是 level equation set 的**段头**，
文档在 `02.08_Setup_and_Result_Tools/02.08.04.14.02.03.01` 下，**不是命令参考章的命令页**。
**本页只取命令参考章里的三条**——**「`EQ` 开头一共几条命令」这句话本页不写**，因为没有全称依据。

**（来源声明）** 上表**第二行**（本页那一行）的字面来自本页 `sources:` 那一篇
（原文的 H1 就是 `EQSP, EQSP? - (EQuation SPecification transfer)`）；
**第一行（`EQFS`）与第三行（`EQFC`）的内容来自本页另外打开的两篇文档
（`02.06.05.02.09` / `02.06.05.02.08`），它们不在本页 `sources:` 里**——
原因与处置见「出处」的「对外核对」一节，
**那一节列了本页从这两篇取到的每一处逐字片段（五处，全是短标识符 / 短语）。**

### 本页答不住的几件事（本篇没写，本页不猜）

- **「当前 setup data」（固件里）与「setup file 里那一份」的关系**——本篇只写了 `current` 这个词。
- **那个二进制块的具体编码**——四条格式说明只说了一个自描述的块怎么开头、怎么收尾，
  **没说数据部分是按什么规则排的**。
- **`EQSP` 什么时候被发出去**（编辑器 / setup file 是在哪个动作上发它）——本篇没写。
- **失败会怎样**——**本篇没有 `## Errors` / `## Warnings` 段**（这是事实，不是本页漏读；实测两个词各 0 次）。
  所以本页**没有**「报错条件」那一节。**同族的 `EQFS` 那一篇有 `## Errors`**——**同一族、两篇不等**（见「出处」瑕疵⑥）。
- **`LEV` 下第 2 位能取什么**——限制句只说了 `TIM` 那一侧，**`LEV` 那一侧本篇没写全**（瑕疵①）。

## 典型用法

### 原文只给了一个例子，而且它是 `EQSP?` 那一半

`## Example` 段的引导句逐字是：

> 「The following example queries the current wavetables:」

**那段会话全文已经在「语法 / 参数」节里（脚本整段收进去了），本页不重复抄一遍。**
读它要盯三处：

1. **它用 `EQSP?`，不是 `EQSP`**——即它是**往上问**的那一半（`queries`）。
2. **参数是 `TIM,WVT`**——第 1 位 `TIM`、第 2 位 `WVT`，**两个值都在取值表里**。
3. **回答行的形状**：`< EQSP TIM,WVT,#9000000127WAVETBL table1`
   ——**和 `EQSP?` 的返回形式 `EQSP {spec_type}, {part}, {#spec(data)}` 对得上**，
   而且 `#9000000127` **后面直接接数据**（`WAVETBL table1`）、**中间没有空格**，
   与 `#spec(data)` 第 4 条的「一串字符」一致；块尾就是那一行单独的 `@`。

**这一段只演示了「问」。** **本篇没有给 `EQSP`（下载）方向的例子**——
所以「一条 `EQSP` 写出来长什么样」，**本页只能从 `#spec(data)` 的格式说明里推**（下表）。

### 其余组合：**原文没给例子，下表是本页按取值表排的（推断）**

**表里只有第 1 行是原文的例子**，其余各行是**按第 1 位（`LEV` / `TIM`）与第 2 位（`EQN` / `SPS` / `WVT`）
两张取值表拼出来的**。**原文没有给它们的例子，本页不声称它们都试过。**

| 目的 | 命令（**除第一行外均为（推断）**） | 依据 |
|---|---|---|
| **读回当前 timing 的 wavetable** | `EQSP? TIM,WVT` ← **原文的例子** | 本篇 `## Example` |
| 读回当前 timing 的 equation set | `EQSP? TIM,EQN` | 第 2 位取值表 `- EQN to specify equations` |
| 读回当前 timing 的 spec | `EQSP? TIM,SPS` | 第 2 位取值表 `- SPS to specify specs` |
| 写下去（下载）以上三种 | 把 `?` 去掉，末位换成 `#<长度位><长度><数据>@` 的块 | `EQSP` / `EQSP?` 两行形式 + `#spec(data)` 四条 |
| **level 侧**（`LEV` 那一半） | **只有第 1 位能确定是 `LEV`**；第 2 位取什么，本篇没写全 | `- LEV to specify levels` + `## Application` 说它用在 level setup file 里；**见上面那句「留白」与瑕疵①** |

**表里刻意没写 `LEV,WVT` 这一格。** 理由要说准：**本篇的限制句只管 `TIM` 那一侧**
（`part can only be set to WVT, EQN, or CLK if spec_type is set to TIM.`）——
**它没有说 `LEV,WVT` 合法，也没有说不合法**。**这格是本篇的空白，不是本页的结论。**

### 这个第 3 位参数，人是敲不出来的

`#spec(data)` 的定义就是一个**自描述的二进制块**（`#` → 长度说明符 → 数据 → `@`）。
**（推断，依据是 `## Application` 那两句 + 那四条格式说明）**：**这一位不是一个「值」，是一段数据**——
所以真实场景里它由**产生这段数据的工具**（编辑器 / setup file 的写出方）拼出来，
**不是工程师在控制台上手敲的**。**本篇没有直接说这句话**，本页只把它标成推断。

### 顺序 / 前提

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next` 段**——
**（这是事实：实测这几个词各 0 次，不是本页漏读）。** 所以本篇给得出来的只有两条：

- **`EQSP` 的落点是 setup file**（`## Application` 第 1 句）——
  所以它**跟着 setup 的下载 / 保存走**，不是一条随手敲的查询命令；
- **`EQSP?` 的调用者是 test program explorer**，用途是 `generate and save setup files`
  （`## Application` 第 2 句）——**即「问」这一半是为「生成并保存 setup file」服务的**。
  **至于它问回来之后怎么写进文件，本篇没写。**

## 和谁有关

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[test-program-explorer]] | **原文逐字点名的调用者**（`## Application` 第 2 行就是它）。**本页与它是「被调用 ↔ 调用」，不是同类** | 本篇 `## Application`（**文档事实**） |
| [[eqfs]] | **同族的另一条命令，也是最容易和本页混的那一条**。**分工**：`EQFS` 搬的两端是**编辑器与临时文件**，`EQSP` 搬的两端是**setup file 与固件** | [[eqfs]] 那一页 + 本页 `## Application`（**读过的 wiki 页 / 文档事实**） |
| [[timing]] | **stage 页**。本页 `stage: timing` 填的是「**最近的一段**」（§6）——**`EQSP` 的 `## Application` 明说它横跨 level 与 timing 两侧**，填 `timing` 只是取最近的那一段 | frontmatter 约定 + 本篇 `## Application` |
| [[level]] | **同上，level 那一侧**。第 1 位参数的 `LEV`、以及 `## Application` 里的 `level and timing setup files` 都指向它。**本页特意把它写出来，免得读者以为 `EQSP` 只管 timing** | 本篇参数表 + `## Application`（**文档事实**） |
| [[timing-file]] | **`EQSP` 出现的地方之一**：`## Application` 说它用在 timing setup file 里。**这个文件内部长什么样，本页没读** | 本篇 `## Application`（**文档事实**，仅限「它出现在这种文件里」） |
| [[level-file]] | **同上，level 侧的那一种** | 本篇 `## Application`（**文档事实**） |
| [[wavetable-file]] | **原文举的两个例子之一**（原文：`for example, wavetables or equation sets`）。第 2 位的 `WVT` 指向的就是它 | 本篇首两句 + 参数表（**文档事实**） |
| [[timing-equation-set]] | **原文举的另一个例子**（同一句里：`for example, wavetables or equation sets`）。第 2 位的 `EQN` 指向的就是它 | 本篇首两句 + 参数表（**文档事实**） |
| [[spec-set]] | **第 2 位的 `SPS` 那一格**（`- SPS to specify specs`）。**（推断）**：`SPS` 与「一组 spec 值」是不是同一件事，**本篇没有出现 `SPECSET` / `SPECS` 这两个词**（各 0 次）；这条关系是**本页按 [[mapping-timing]] 把三块记成 EQN / SPS / WVT 的那一行排的** | 本篇参数表 + [[mapping-timing]]（**文档事实 / 读过的 wiki 页**） |
| [[mapping-timing]] | **对照表页（已建）**。它把 `EQSP` 排在「把三块数据下载 / 上传（EQN / SPS / WVT）」那一行的 L1 列；**它引的 timing setup file 例子文件里逐字有三条 `EQSP`**（`TIM,EQN` / `TIM,SPS` / `TIM,WVT`）——**那个例子文件本页没读，那三条只能记成「那页说的」** | 那页的主表与「出处」节（**本页读过的 wiki 页**） |
| [[mapping-level]] | **level 侧那张对照表**。**本页没读它**——它出现在 `dangling.csv` 的 `eqsp` 引用者名单里（见「出处」） | `extract/dangling.csv`（**计数产物，不是文档事实**） |
| [[timing-setup-commands]] | **`EQSP` 在 timing setup 命令的清单里**。依据是 `extract/edges.jsonl` 里 `02.06.06.02_List_of_timing_setup_commands.md` 有一条边指到 `EQSP` 的一份投放 | `extract/edges.jsonl`（**计数产物**） |
| [[equation-based-level-setup]] | **`LEV` 那一半的上游概念**（level 侧的 equation based 配置）。**本页没读那页**，所以「equation based level 配置长什么样」本页给不出来 | 本页未读（**取材边界**） |
| [[command-reference]] | **本页定义文档所在的章**（`02.06_Command_Reference`）。这一章**不逐篇建页**（§12.1），本页是这一章里被单独建页的少数之一 | §12.1 + 本页 `sources:` 的路径（**项目约定**） |
| [[spec-tool]] | **注意：它不是 `EQSP` 的调用者**。它是同族 `EQFS` 的调用者（`EQFS` 那一篇的 `## Application` 里逐字有 `The Spec tool`）。**列在这里是为了让「`EQ` 这一族谁调谁」一眼看得全** | `EQFS` 那一篇（**不在本页 `sources:`**，见「出处」的「对外核对」） |
| [[smartest-6.3.2]] | **版本哨兵值**指向的版本页（见下节） | 本篇 `## Functional changes`（**文档事实**） |

**两条本页答不住、只能记下来的**：

- **`EQSP` 与 `EQFS` 在「save 一个 setup」这条链上谁先谁后**——**两篇都没有写这条链。**
  `EQFS` 那一篇的 `temporary files` 与 `EQSP` 这一篇的 `setup files` 是两处不同的词，
  **它们之间隔着什么，本页给不出**（见「出处」的「本页没做的」）。
- **`EQSP?` 问回来的数据与 `EQFS` save 出去的数据是不是同一块**——**两篇都没说。**

## 版本

本节照 `## Functional changes` 段写。**那一段只有一条**：

> 「- Introduced before SmarTest 6.3.2」

**这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 `EQSP`」。**
措辞是 `before`（不是 `in`），意思是「**在本套文档覆盖范围开始之前就已经有了**」。
（`wiki/schema.md` §11.2 ② 记着：全语料 **2,677** 条可用性行写的是同一个版本号，措辞全是 `before`。）
**所以只能说：7.10.3 上有 `EQSP`，而且它比 6.3.2 更老。**

**版本段里没有的东西**：**没有一条 `SmarTest X.Y.Z:` 形式的变更记录**。
所以「`if these are not empty, for backward compatibility.` 这句是哪个版本为了兼容加的」
「`CLK` 那一档是哪个版本进的」**在本篇里查不到**。

**横向对照（这两条也是本页读到的，来源见「出处」的「对外核对」）**：
同族的 `EQFS` 那一篇的 `## Functional changes` **写的是同一条**
（`- Introduced before SmarTest 6.3.2`）；
而 `EQFC` 那一篇写的是 **`- Introduced in SmarTest 7.0.1`**——
**但 `EQFC` 不是同族**（它的 `EQ` 是 `EQualization`，见「是什么」的「别混」表），
**所以这一条只是摆在一起给你看，本页不据此推断任何事。**

## 出处

`sources:` 1 篇：`02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.md`（TDC `98593_2.htm`，1,660 字节，61 行）。**整篇读完。**

### 数是怎么量的（§11.5 的口径）

| 数 | 值 | 怎么量的 |
|---|---|---|
| 字节 | **2,314** | `len(path.read_bytes())`（即 `st_size`）。**不是** `len(read_text())` |
| 行数 | **103** | `wc -l`（**不 +1**；本语料末行都带换行） |
| 换行 | **103 个全 CRLF、裸 CR 0 个** | 所以 `len(read_text())` 会给出 **2,211**（**恰好少 103 = 行数**）——**本页不拿 2,211 当字节数** |
| 代码块 | **4** | `docs.jsonl` 的 `code_blocks`（= 全文 24 个反引号，8 条围栏线） |
| 标题 | **6**（1 个 H1 + 5 个 H2） | `docs.jsonl` 的 `heading_count`；抽取器认作「结构段」的只有 `Application` / `Example` / `Functional changes` 三个 |
| 出边 | **0** | `docs.jsonl` 的 `out_degree: 0`、`link_kinds: {}`——**本篇正文里一个链接都没有** |

**「语法 / 参数」节那 244 字符**是本页核过的：抽取器在这一篇上只收到 **1 段**（`## Example`，
`chars: 244`），**`## Syntax` / `## Parameters` 两段都不存在**（`Syntax` / `Errors` / `Warnings` 各 0 次）。

### 这一篇在语料里有 4 份投放——本页核过

| 路径（相对 `by-category/`） | `source_topic` | `st_size` |
|---|---|---|
| `02_System_reference/02.06_Command_Reference/02.06.02.02.109_EQSP__EQSP__-__EQuation_SPecification_transfer.md` | `98593.htm` | 2,313 |
| **`02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.md`（本页 source）** | **`98593_2.htm`** | **2,314** |
| `02_System_reference/02.06_Command_Reference/02.06.06.02.14_EQSP__EQSP__-__EQuation_SPecification_transfer.md` | `98593_3.htm` | 2,314 |
| `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.14_EQSP__EQSP__-__EQuation_SPecification_transfer.md` | `98593_4.htm` | 2,325 |

**四份的正文逐字节相同**：剥掉 frontmatter 之后**都是 2,091 字节**，
`sha256` 同为 `690258c0264de3eb871079c7b7fc2869e35cd0f6cbe3742fe89f1177906bb852`。
**差别只在 frontmatter 的 `source_topic` 与 `source_html` 两行**（实测 `st_size` 依次
2,313 / 2,314 / 2,314 / 2,325；`title` 四份逐字相同）。
判据是 §10 第 0 条：`source_topic` 去掉 `_N` 后缀后相同 → 同一篇 TDC 页。

> **所以：`EQSP` 这一篇被投放了 4 次，不是 4 处独立证据。**
> **本页只把 `02.06.05.02.10` 当来源**，其余三份**只做了去重核对（哈希），没有当成证据读**。
> **注意这与 [[eqfs]] 那一页的措辞有一点不同**（那页写的是「四份剥掉 frontmatter 之后逐字节相同，
> 都是 1,493 字节」）——**本页这一篇的四份也是同样的关系，但本页报的是自己量出来的字节数**：
> **剥掉 frontmatter 后 2,091 字节**（不是 2,314，2,314 是含 frontmatter 的 `st_size`）。

### 边是怎么数的（这一节给的是可复核的数，来源 `extract/edges.jsonl`）

- **`EQSP` 的 4 份投放一共被 19 条边指着，来自 10 篇不同的文档。**
- **本页 `sources:` 那一份只有 2 条入边**：`02.06.05.02_List_of_level_setup_commands.md`
  与 `02_System_reference/index.md` 各 1 条。
- **这一篇的出边 = 0 条**（见上表）——**所以本页没有任何来自「它链了谁」的结论。**
- `hubs.csv` 记：`02.06.02.02.109` 那一份 `in_all=13` / `in_src=12` / `in_inline=6`；
  **本页这一份 `in_all=2` / `in_src=1` / `in_inline=1`。**
  **同一篇文档在不同章的投放，入度差这么多**——**`in_src` 不能按投放份数直接比**（§10「重复投放」第 1 条）。
- `dangling.csv`（**建本页之前**那一版）里有一行是 `eqsp`：`refs` 列写 **10**，
  `stages` 列列了 **7 个**引用它的页（`eqfs` / `level` / `mapping-level` / `mapping-timing` /
  `timing` / `timing-file` / `wavetable-file`）。
  **⚠️ 这个数会随建页变**：本页一建成，`eqsp` 就不再是「不存在的目标」了（§9.1 专门警告过这一点）。
  **本页引它只当「谁在等这一页」的线索，不当文档事实。**

### 对外核对：`EQ` 开头的这三条命令（**这两篇不在 `sources:` 里，说明如下**）

**本页的 `sources:` 只有 1 篇**——它由 `extract/wiki-plan.csv` 的 `rel` 列决定
（那一行 `rel` 只有一个路径），而按补页规格第 2 条 **`sources:` 不许手改**，**本页没改它**。

为了让「`EQ` 开头的这三条各干什么」不留空白，本页另外打开了两篇同章文档，
**只做一件事：核对三条命令的分工**：

| 打开的是 | 读了多少 | 本页从它那里拿到了什么 |
|---|---|---|
| `02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md`（TDC `98592_2.htm`，1,177 字节，44 行） | 整篇 | 只核了「它是 load/save、两端是临时文件、调用者是编辑器工具与 Spec tool」 |
| `02_System_reference/02.06_Command_Reference/02.06.05.02.08_EQFC__EQFC__-__EQualization_and_Filter_Configuration.md`（TDC `112905_2.htm`，4,664 字节，99 行） | 整篇 | 只核了「它的 `EQ` 是 `EQualization`，与 equation 无关」 |

**处置与 `mapping-timing.md` 的「出处」节同一套**：那页也用过一篇「只 `grep` 看过一行、
因此没进 `sources:`」的文档，处置是**记下来，不冒充来源**。
**本页的处置说得更细：这两篇一共只贡献了五处逐字片段，全部是短标识符 / 短语，没有一句成段的引文**：

| 逐字片段 | 从哪一篇 | 用在本页哪里 |
|---|---|---|
| `EQuation FileS command transfer`、`temporary files`、`The Spec tool` | `02.06.05.02.09`（`EQFS`） | 「是什么」的「别混」表、「和谁有关」的 [[spec-tool]] 那一行 |
| `EQualization and Filter Configuration`、`- Introduced in SmarTest 7.0.1` | `02.06.05.02.08`（`EQFC`） | 「是什么」的「别混」表、「版本」的横向对照 |

**这五处的出处都在正文里当场标了**（不是只在「出处」节补一句）。
**其余关于这两篇的话都是转述，不是引文。**

### 本页没做的

- **没有实跑。** 没在机台上敲过 `EQSP` / `EQSP?`，没有下载或上传过任何 equation based 数据块，
  **没有验证过那段二进制到底怎么编码**。`verified: doc-only` 指的就是这件事。
- **`## Example` 里的输出没有复现过。** 本页只核了它的**形状**（`#9000000127` 能解出 127 字节），
  **没有判 127 与实测 147 字节谁对**（瑕疵③）。
- **`EQFS` / `EQFC` 两篇只用来核分工**（见上），**两篇的正文内容没有进本页**（只有上表那五处逐字片段）。
- **`02.06.05.02` 这一章的其他兄弟命令一条没读**——所以本页不知道 `EQSP` 在这一章里还跟谁并列。
- **`02.06.05.01.04.*` 那一族（equation based level setup）全文没读**——
  本页只知道 [[equation-based-level-setup]] 那一页存在，**level 侧的细节本页给不出**。
- **`mapping-level` 没读**——所以「level 侧那张对照表怎么排 `EQSP`」本页不知道。
- **`Test Program Explorer` 那一篇没读**——所以「它调 `EQSP?` 去 `generate and save setup files`
  的具体动作是什么」本页只有原文那一句。
- **`timing setup file` 的例子文件没读**（`02.08.04.34.04.04`）——那里面逐字有三条 `EQSP`
  （`TIM,EQN` / `TIM,SPS` / `TIM,WVT`），**本页是从 [[mapping-timing]] 读到的，不是自己读的原文**。
- **四份投放只做了哈希核对**——`02.08.04.34.02.*` 那一棵**是整章镜像**（`wiki/schema.md` §10 与
  [[mapping-timing]] 都记着这件事），**但本页没有读它们的上下文**，
  所以「这一篇在别的章里跟谁并列」本页不知道。
- **图**：本篇对 `raw/` 的引用 **0 处**（`.png` / `.jpg` / `.gif` / `![` / `<img` / `raw/`
  六种写法**全部 0 命中**）——**所以本页没有任何来自图的结论**。
- **没有动 `wiki/index.md`**，也没有动任何别的页。

### ⚠️ 本篇的六处瑕疵，本页照实记下、一处都没替它改

> ① **`part` 的两张清单对不上。** 取值表是三个（`EQN` / `SPS` / `WVT`），
> 紧跟的限制句里是另外三个（`WVT` / `EQN` / `CLK`）——
> **`CLK` 全文只出现 1 次（就是这一句），取值表里没有它；`SPS` 全文只出现 1 次（在取值表里），
> 限制句里没有它。** 而且这一句**只说了 `TIM` 那一侧**：
> **`LEV` 下第 2 位能取什么，本篇没有一句写全**——而 `## Application` 又明说它用在 level setup file 里。
> **两条清单不是一对多、也不是大小写问题，就是不重合。本页不替它判哪边是现行版。**

> ② **两行语法的空格不一致**：`EQSP?{spec_type}, {part}` 里 `?` 与 `{spec_type}` **之间没有空格**，
> 而 `EQSP {spec_type}, {part}, {#spec(data)}` 里有。**原文如此**（它在原文的
> `## EQSP?` 标题下，**本页一个字没动**）。

> ③ **例子里声明的长度与打印出来的数据对不上**：`#9000000127` 按 `#spec(data)` 的四条
> 解出来是 **127 字节**；而例子那段数据（从 `WAVETBL` 到 `@`）本页量出来是
> **147 字节 / 138 字符**（含 9 个 CRLF）。**两者不等。**
> 本页**不判是哪一边的问题**——只能记下：要么这个例子是示意性的、不是真实抓取，
> 要么那个长度字段指的不是这段字符数。**本篇没有一句解释。**

> ④ **本篇没有 `## Syntax` / `## Parameters` 段标记，参数表挂在一行裸的 `Parameters` 下**
> （`Parameters` 全文出现 1 次，且不带 `##`）。**这不是本页的缺陷，是本篇的结构**——
> 后果写在「语法 / 参数」节里（脚本只收到 `## Example` 那 244 字符）。
> **同族的 `EQFS`（`02.06.05.02.09`）两样都有**：`## Syntax` + `## Parameters` + `## Errors`。
> **同一个家族、同一种内容，章节标记不一样**——**本页照实记，不改脚本、也不往那一节补字。**

> ⑤ **参数表是 HTML 表格压平出来的管道行**（许多行只有一个孤立的 ` |`，中间夹空行）。
> **这是语料的结构，不是脚本切错**（[[xps256-status-flags]] 的「语法 / 参数」节记过同一种形态）。

> ⑥ **本篇没有 `## Errors`、没有 `## Warnings`**（实测两个词各 0 次）。
> 这一条要单独说，因为它**读起来像「`EQSP` 不会失败」**——**不是**。
> 本页只能说「**本篇没写失败条件**」；同族的 `EQFS` 那一篇**有** `## Errors`，
> 里面是**两条**条件、都是「文件不存在」。**本页没有「报错条件」那一节，
> 就是因为脚本按「材料为空」处理了**（实测 `error_block()` 返回空串）。

`verified: doc-only`
