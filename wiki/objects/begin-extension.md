---
type: object
title: BEGIN_EXTENSION
layer: L2
stage: testmethod
tags: [testmethod, l2, test-method-api, extension-block, fw-task, firmware-command, mcd, multisite, site-focus, flush, caching]
related: [testmethod, end-extension, fw-task, flush, on-first-invocation-begin, controlling-multiple-sites, site-focus-required-before-command, mapping-testmethod, command-reference, primary-status, add-limit, smartest-6.3.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# BEGIN_EXTENSION

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,273 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void BEGIN_EXTENSION();
void BEGIN_EXTENSION(STRING& sites);
void BEGIN_EXTENSION(ARRAY_I& sites);
```

Parameter
 |

I/O

 |

Parameter

 |

Description / Range

 |
 |

I

 |

sites

 |

This parameter sets the setup focus sites for the statements in the extension block.

To make the extension block effective for sites 1 to 3 in four sites,

STRING: "1110".

ARRAY_I: sites[0]=1, sites[1]=2, and sites[2]=3.

 |

### Example 1: BEGIN_EXTENSION and END_EXTENSION declare the extension block

```
STRING dfcm("DFCM 1,4000,50,-1.00,1.00,4000,5,I,0,PPNP,(CP)\n");
STRING ptstq("PTST? 1,NONE,NONE,PVAL\n");

BEGIN_EXTENSION();

    FW_TASK(dfcm);

    STRING answer;

    FW_TASK(ptstq, answer);
    ...
    ...

END_EXTENSION();
```

### Example 2: Extension block for all enabled sites

```
STRING enabled_sites;

GET_ENABLED_SITES(enabled_sites);

BEGIN_EXTENSION(enabled_sites);

    //
    // Your FW_TASK code
    //
    ...
    ...

END_EXTENSION();
```

The GET_ENABLED_SITES API retrieves the information of the current enabled sites and stores it to the variable enabled_sites. BEGIN_EXTENSION and END_EXTENSION declare the extension block for multi-site testing. In this example, the extension block is effective for the current enabled sites. BEGIN_EXTENSION sets the current enabled sites to the setup focus sites. Therefore, the statements will be performed for the current enabled sites only.

<!-- 语法节 end -->

## 是什么

**`BEGIN_EXTENSION` 是「扩展块」的开括号。** 原文第一句就是它存在的理由：

> This API declares the beginning of the block where you can access the system hardware or MCD at the firmware level.

**两个词要抠准**：`at the firmware level`（**说出去的是固件层的东西，不是 GUI 动作**）与 `block`
（**它自己不干活——它只划一块地**）。这块地在原文里有名字：

> BEGIN_EXTENSION and END_EXTENSION should be used as a pair. The area enclosed by BEGIN_EXTENSION and END_EXTENSION is called "extension block".

**头文件**（原文给了绝对路径）：

> This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/Extension.h.

**`END_EXTENSION` 与它同一个头文件**——`END_EXTENSION` 那一篇写的是同一个路径
（本页读了那一篇，见 [[end-extension]]）。**两个 API 住一个头，是「配对」这件事的物理形态。**

> **⚠️ `MCD` 是什么，本篇没有展开。** 全篇 2 次 `MCD`，都是 `the system hardware or MCD`
> 这个连写；**它和 `system hardware` 是什么关系，语料未写。** 本页不替它补。

### 三个重载 = 两种用途

| 重载（逐字见「语法 / 参数」节） | 干什么 | 本页能说的 |
|---|---|---|
| `void BEGIN_EXTENSION();` | 不带参数 | **原文没有单独讲它**；两个 Example 里 Example 1 用的是它 |
| `void BEGIN_EXTENSION(STRING& sites);` | 指定 setup focus sites | 参数说明见下 |
| `void BEGIN_EXTENSION(ARRAY_I& sites);` | 同上，另一种写法 | 同上 |

**`sites` 是入参**（参数表 `I/O` 列写着 `I`），**不是出参**。原文对它的定义只有一句：

> This parameter sets the setup focus sites for the statements in the extension block.

**同一个「四 site 里只要 1 到 3 号」在这个参数上有两种写法**（原文逐字）：

> To make the extension block effective for sites 1 to 3 in four sites,
> STRING: "1110".
> ARRAY_I: sites[0]=1, sites[1]=2, and sites[2]=3.

**注意 `ARRAY_I` 那种写法是 0 基的**：`sites[0]` 里放的是第 1 个 site 号。

> **（推断）`STRING` 那种写法是从 site 1 起逐位映射的。**
> 依据是上面这一个例子（四 site、要 1–3 号 → `"1110"`，左起四位、左边三个是 1）。
> **原文没有写位序、没有写串长不够时怎么办、也没有写 site 数多于串长时怎么办——
> 这三件事都「语料未写」。** 照着这个例子写代码之前必须先实机核一次。

### 五条 `## Important points`——这一页真正的内容全在这五条里

原文用五条把「这块地是什么、能放什么、进块前要做什么、多 site 怎么用」写完了。
**逐条读，不要跳**（引文分块照抄，一条一段）：

**① 配对 + 命名：**

> BEGIN_EXTENSION and END_EXTENSION should be used as a pair. The area enclosed by BEGIN_EXTENSION and END_EXTENSION is called "extension block".

**② 块里能放什么——这一条给了「能」与「不能」两半：**

> You can describe the FW_TASK functions within the extension block. One or more FW_TASKs can be applied to this block. Beside the FW_TASK function, you can also describe the function you originally created. You should not describe the other test method APIs in the extension block.

**拆成表**：

| 想放进块里的东西 | 原文怎么说 |
|---|---|
| `FW_TASK` | **可以，且条数不限**（`One or more FW_TASKs can be applied to this block.`） |
| **你自己写的函数** | **可以**（`you can also describe the function you originally created`） |
| **别的 test method API** | **不要**（`You should not describe the other test method APIs in the extension block.`） |

**③ 数据 setup 的冲突——这一条是全篇唯一的机制说明：**

> For data setup, a conflict might occur between the test method API outside the extension block and firmware commands within the extension block. To avoid such a conflict, you should consider the following actions:

**原文给的两个动作**（各为一小条）：

> The caching mechanism of the test method is temporarily turned off between the "extension block" explicitly declared by BEGIN_EXTENSION and END_EXTENSION. This is implicitly done by the system.

> You should execute the FLUSH API before entering the extension block. The setup data relating to the API such as ANALOG, ANALOG_STATUS, PRIMARY_STATUS, and ROUTING_STATUS will be stored in the caching mechanism. The FLUSH API downloads the setup data to the system hardware or the MCD.

**这两条读成一句话就是**：**块内是固件层、块外是 test method 层，两边的 setup 会打架；
系统在块内自动关掉 caching（`implicitly done by the system`），而你要做的是「进块之前先 `FLUSH`」。**

**④ 多 site：`sites` 参数怎么起作用、以及可以嵌套：**

> For multi-site testing, you can specify optional parameter sites to set the setup focus sites for the statements in the extension block. Therefore, the statements will be performed for the specified sites only.

> In this case, you can make nested extension blocks.

**⑤ 出块时 site focus 会还原；嵌套错了会怎样：**

> END_EXTENSION just after BEGIN_EXTENSION reverts the setup focus sites to the same settings as before entering the extension block.

> This allows you to do complicated and flexible site management correctly. If the extension block is not nested correctly, the nest information will be initialized at the end of the test suite execution automatically. Also, a warning message appears in the report window.

**⑤ 的后果是这一页里唯一一条「做错了会怎样」**：**嵌套不正确 → 到 test suite 执行结束时
nest 信息被自动初始化 + report window 里出现 warning**。**注意「warning」不是「error」**，
原文用的词是 `a warning message`，**而且没有说执行结果会不会因此错**——那一步语料未写。

> **⚠️ 第 ⑤ 条里那句以 `END_EXTENSION just after BEGIN_EXTENSION` 开头的话，讲的是另一个 API 的行为，
> 却写在本页的 `## Important points` 里**（原文没有为它单起一条）。**本页照原样引，并把它同时记进
> [[end-extension]]**——那一篇自己（35 行）**一个字都没提这个还原行为**，见「出处」⚠️③。

### 条件 → 结果（把五条摊平）

| 条件 | 结果 | 原文依据 |
|---|---|---|
| 只写 `BEGIN_EXTENSION` 不写 `END_EXTENSION` | **原文只写了 `should be used as a pair`**——**没说会怎样** | 第 ① 条 |
| 块里放固件命令 | 用 `FW_TASK`，一条或多条都行 | 第 ② 条 |
| 块里放自己写的函数 | 允许 | 第 ② 条 |
| 块里放别的 test method API | `You should not describe the other test method APIs in the extension block.`——**没说会怎样** | 第 ② 条 |
| 要在块里做 setup | **进块前先执行 `FLUSH`** | 第 ③ 条 |
| 多 site 只想对部分 site 生效 | 用带 `sites` 的那个重载 | 第 ④ 条 |
| 块里再开块 | 允许（`you can make nested extension blocks`） | 第 ④ 条 |
| 嵌套不正确 | nest 信息在 test suite 执行结束时被自动初始化；report window 出现 warning | 第 ⑤ 条 |

**这张表里「没说会怎样」的两格要照实留着**：原文对这两件事只有措辞（`should`），**没有给后果**。
§11：**全称结论的举证责任在写的人**——本页不替它补一个后果。

## 典型用法

**两个 Example 都已经在上面「语法 / 参数」节里逐字，本页不重抄。**
**本文档没有 `## Procedure` 段、没有 `## Before you begin` 段**——
能当用法读的只有那两个 Example 和上表，**没有文档给的编号流程**。

| # | Example 1（单 site 基线） | Example 2（多 site，对全部 enabled site） |
|---|---|---|
| 1 | 把要下的固件命令写成 `STRING`（`dfcm` / `ptstq`） | `STRING enabled_sites;` 然后 `GET_ENABLED_SITES(enabled_sites);` |
| 2 | `BEGIN_EXTENSION();`（**不带参数**） | `BEGIN_EXTENSION(enabled_sites);`（**带 `sites` 参数**） |
| 3 | 块里 `FW_TASK(dfcm);`，再 `STRING answer; FW_TASK(ptstq, answer);` | 块里写自己的 `FW_TASK` 代码 |
| 4 | `END_EXTENSION();` | `END_EXTENSION();` |

**Example 2 末尾那一段说明是独立事实**（它解释了「为什么这样写就能对全部 enabled site 生效」）：

> The GET_ENABLED_SITES API retrieves the information of the current enabled sites and stores it to the variable enabled_sites. BEGIN_EXTENSION and END_EXTENSION declare the extension block for multi-site testing. In this example, the extension block is effective for the current enabled sites. BEGIN_EXTENSION sets the current enabled sites to the setup focus sites. Therefore, the statements will be performed for the current enabled sites only.

**一句话**：`GET_ENABLED_SITES` 取回「当前 enabled 的 site」，把它当 `sites` 传进去，
**`BEGIN_EXTENSION` 就把这批 site 设成 setup focus sites**——于是块里的语句只对它们生效。

**三点照实说明：**

- **`GET_ENABLED_SITES` 的签名、返回的集合是什么形态、`STRING` 还是别的**——
  **本页一个字都没有**（那一篇没读，见「出处」）。
- **`FW_TASK` 有几种重载、`answer` 接回来的是什么**——**本页没有**（[[fw-task]] 那一篇没读）。
- **Example 1 用的是不带参数的重载**；**多 site 场景该用哪个重载，本篇没说**——
  那条要求（first-invocation 块里 `FW_TASK` 必须裹在**带 site 参数**的这一对里）写在
  `ON_FIRST_INVOCATION_BEGIN` 那一篇里，记在 [[on-first-invocation-begin]] 那页（**本页没读那篇 raw**）。

## 和谁有关

- [[end-extension]] — **配对的后半，也是本篇 `## Related information` 的第一个**。
  原文：`BEGIN_EXTENSION and END_EXTENSION should be used as a pair.`
  **本页读了它那一篇**（`02.07.04.01.59`，35 行）：它把全部机制都推回本页，
  所以**「出块时 site focus 还原」「嵌套错了会怎样」这两条只在本页有**——反过来，
  本页的引文也不替它补它没有的话。
- [[fw-task]] — **第 ② 条点名要放进块里的东西，也是 `## Related information` 的第二篇。**
  那一页记着它自己的头文件也是同一个 `/opt/hp93000/soc/prod_com/include/MAPI/Extension.h`，并引了它那一篇的一句
  `BEGIN_EXTENSION and END_EXTENSION APIs are always used together with the FW_TASK function.`
  ——**那句是从 `FW_TASK` 那一侧说的（讲的是「它与这两个 API 合用」），
  本页的 `should be used as a pair` 讲的是「这两个 API 彼此配对」；两句不是同一件事，
  本页不把它们对齐，也不做加强。**（本页没有读 `FW_TASK` 那一篇的 raw。）
- [[flush]] — **第 ③ 条要求的那个动作**（`You should execute the FLUSH API before entering the extension block.`）。
  **本页没有读 `FLUSH` 那一篇**，所以「`FLUSH` 怎么调、有没有参数、下什么」本页一个字都没有。
  顺带一条**按页名容易走错的**：本 wiki 另有一页 [[flsh]]（L1 的固件命令 `FLSH - FLuSH buffered commands`），
  **它与本页说的 `FLUSH` API 不是同一篇 raw**（`02.06.02.02.124` vs `02.07.04.01.69`）；
  **本篇没有出现 `FLSH` 这个词**，所以本页不为它做任何断言。
- [[testmethod]] — **stage 页，也是本页 `stage: testmethod` 的理由。** 它那一页的
  「L1 — Firmware / Setup Command」一节把本页与 [[fw-task]] 并列，并抄了 `02.07.03.10` 的一段
  示例和「caching 被临时关闭」「进块前先 `FLUSH`」两条——**那两条的出处标的是 `02.07.03.10`**，
  与本页 `## Important points` 第 ③ 条是同一内容；**两篇文档都写了它**，可以互相印证，
  但**本页的引文一律取自本页的 raw**。
- [[on-first-invocation-begin]] — **多 site 场景里那条硬要求的落点**：那一页记着它那一篇写着
  `FW_TASK` 要裹在**带 site 参数**的 `BEGIN_EXTENSION` / `END_EXTENSION` 里，
  并且 `you should not describe it enclosed by the BEGIN_EXTENSION API with no parameter`。
  **那条要求不在本篇里**——本页只记「它来自哪一页」。（本页没读那篇 raw，引的是那一页的转引。）
- [[controlling-multiple-sites]] / [[site-focus-required-before-command]] — **site focus 主题的邻近页**。
  本页的 `sites` 参数改的就是 setup focus sites，所以读本页时要连着那一族一起看；
  **两页的 raw 本页都没读**——**按主题并列，不代表同物。**
- [[primary-status]] — 第 ③ 条在列「setup 数据存在 caching 里」时点了 `PRIMARY_STATUS` 这个名字
  （同一句里还有 `ANALOG` / `ANALOG_STATUS` / `ROUTING_STATUS`，**那三个没有页**）。
  **本篇只把它们列在一个从句里，没有说其中任何一个的行为**——所以本页与 [[primary-status]]
  的关系**只有「被同一句话点到名」这一层**。
- [[command-reference]] — **固件命令的本体在 `02.06`**（Example 1 里的 `DFCM` / `PTST?` 属于它那一域）。
  **本页没有读 `02.06`**，所以**那两串参数的含义本页一个字都没有**；
  照抄示例当会用，正是 §11 防的那件事。
- [[mapping-testmethod]] — **跨层对照表**：它把本页填在「在 test method 里执行固件命令」那一行的
  L2 格，与 [[fw-task]] 并列，并引了一句
  `You can execute firmware command to control your hardware directly by using the FW_TASK, BEGIN_EXTENSION and END_EXTENSION APIs.`
  ——**那一句不在本篇的 raw 里**（它出自 `02.07.03.10`），**本页只登记它被填在哪里**。
- [[add-limit]] — **非同族，只在语料形态上同病**：它那一篇的参数表表头也把 `Parameter` 写了两遍
  （见「出处」⚠️①）。**本篇的 `## Related information` 里没有它，两页没有文档上的关系。**
- `GET_ENABLED_SITES()`（**未建**，也不在 allowlist，故不链）— Example 2 用的那个 API，
  raw：`02.07.04.01.86_GET_ENABLED_SITES.md`。**本页没读它。**
- [[smartest-6.3.2]] — **版本页**：本篇 `## Functional changes` 那一条的落点（是哨兵，见「版本」）。

## 版本

本文档有 `## Functional changes` 段，**只有一条**：

- `Introduced before SmarTest 6.3.2`

**这是 §11.2 ② 那个哨兵值，不是「6.3.2 引入了它」**：措辞是 `before` 不是 `in`，
意思是「**在本文档集覆盖范围开始之前就已经有了**」。所以：

- **本页答不出「哪一版才有 `BEGIN_EXTENSION`」。** 照字面读会得到一条假信息
  （「6.3.2 新增了它」），而且格式齐整——那正是要防的。**本页不提供这个答案。**
- 版本页 [[smartest-6.3.2]] 对这个哨兵的处理是**单列一节讲那 2,677 条的做法、不逐条铺开**；
  本页这一条**不在它正文列出的 33 条里**（落在「⚠️ 另一批」那一节）。
- **本篇没有别的版本行**，所以**「它后来改过没有」本页答不出**——
  「`## Functional changes` 里没记录」不等于「没改过」。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.md`
（TDC `28740.htm`，119 行 / 3,911 字节）。**整篇读完。**

**本页没做的：**

- **`## Related information` 三篇里只读了一篇。** 读了 `END_EXTENSION`（`02.07.04.01.59`，
  35 行——它是本页的另一半，见 [[end-extension]]）；**`FW_TASK`（`02.07.04.01.77`）与
  `GET_ENABLED_SITES()`（`02.07.04.01.86`）都没读**——所以
  「`FW_TASK` 的三种重载怎么选、`answer` 是什么类型」「`GET_ENABLED_SITES` 返回什么形态的 site 集合」
  **本页一个字都没有**。
- **`FLUSH`（`02.07.04.01.69`）没读——这是本页最大的缺口。** 第 ③ 条明确要求「进块前先执行 `FLUSH`」，
  而「它怎么调、有没有参数、和 L1 的 `FLSH` 是什么关系」全在那一篇里。
- **`02.07.03.10_Executing_Firmware_Commands.md` 没读**（[[testmethod]] stage 页那一节引的就是它）。
  所以「多 site 下 first-invocation 块里该怎么写」这条要求，本页只有 [[on-first-invocation-begin]]
  那一页的转引。
- **Example 1 里那两条固件命令（`DFCM` / `PTST?`）的参数含义没查。** 它们的定义在
  `02.06_Command_Reference` 那一域，**本页没读**。**本页不解释那两串里的任何一个数**。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** 没在任何机台上写过一段扩展块，也没有验证过 `"1110"` 的位序、
  `FLUSH` 的实际效果、以及嵌套错乱时那条 warning 长什么样。`verified: doc-only` 指的就是这件事。
- **本文档没有 `## Procedure` / `## Before you begin` / `## Application note` 段。**
  上面「典型用法」里那两张表是**本页按 `## Important points` 与两个 Example 排出来的**，
  不是文档给的编号流程；**两个 Example 的代码本身是原文逐字（已在「语法 / 参数」节里）。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **参数表的表头把 `Parameter` 写了两遍。** 摊平后的原文逐字是
> `Parameter` ／ `I/O` ／ `Parameter` ／ `Description / Range`——**第一列与第三列同名**。
> 这是语料把原表摊平成一串单元格的样子，**本页照录，不替它改**
> （同一形态在 [[add-limit]] 那一篇里也有，见那一页的 ⚠️②）。
> ② **参数表只有一行（`sites`），而 `Syntax` 段列了三个重载。** 不带参数的那个重载在参数表里
> **没有对应行**——**这不是漏抄，是原文如此**（它本来就没有参数）；`STRING&` 与 `ARRAY_I&`
> 两个重载共用 `sites` 那一格。
> ③ **第 ④ 条里混进了一句讲 `END_EXTENSION` 的话**：
> `END_EXTENSION just after BEGIN_EXTENSION reverts the setup focus sites to the same settings as before entering the extension block.`
> ——**它讲的是本页之外那个 API 的行为，却写在本页的 `## Important points` 里**，
> 原文没有为它另起一条。**本页照原样引，并把它同时记进 [[end-extension]]**
> （那一篇自己一个字都没提这个还原行为）。
> ④ **同一段 `DFCM` 示例在两篇文档里不一样**（**不是本篇内部矛盾，是跨文档差异**）：
> 本篇 Example 1 写的是 `-1.00` 与 `I,0,PPNP`，而 [[testmethod]] 那一页转引的 `02.07.03.10` 版本
> 写的是 `-1.0` 与 `NGNG`；`PTST?` 那一条也不同（本篇是 `1,NONE,NONE,PVAL`，那一版是 `1,NONE,CVAL`）。
> **本页没有读 `02.07.03.10`**，所以**只登记「两处对不上」，不判谁对，也不动本页的引文**。
> ⑤ **`sites` 的 `STRING` 写法只有一个例子**（`"1110"`），**位序与位数规则原文没写**——
> 见「是什么」里那条（推断）。这是**语料没写**，不是错；但**照它写代码前必须实机确认**。
> ⑥ **`MCD` 没有展开**（全篇 2 次都是 `the system hardware or MCD` 这个连写），
> 第 ③ 条点名的 `ANALOG` / `ANALOG_STATUS` / `ROUTING_STATUS` 三个 API 也一样——
> **本篇只给了名字，没给行为**。
> ⑦ **本篇没有坏字。** 实测全文 **0 处非 ASCII 字符**（没有 `鈥` / `渭` / `碌` 那一族）。
> **但这是「本页量过的」**，判据是本篇这一个文件；§11.2 ① 那族在别的篇里大量存在。
> ⑧ **`## Related information` 那一行的三个链接之间没有任何分隔符**，在 raw 里是连着的一串：`[END_EXTENSION](<02.07.04.01.59_END_EXTENSION.md>)[FW_TASK](<02.07.04.01.77_FW_TASK.md>)[GET_ENABLED_SITES()](<02.07.04.01.86_GET_ENABLED_SITES.md>)`——**三个名字挤成一串，一个空格都没有**。同一形态 [[end-extension]] 与 [[fw-task]] 两页都记过。

`verified: doc-only`——**本页没有在任何真实机台上写过一段扩展块**
（§11：文档里有 ≠ 这台机器上能用；尤其 `"1110"` 的位序与「嵌套错乱时会发生什么」，
**文档没写清，动手前先照实机核对**）。
