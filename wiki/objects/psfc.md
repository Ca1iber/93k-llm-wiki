---
type: object
title: PSFC, PSFC? - (Parallel Setup FoCus)
layer: L1
stage: pin
tags: [pin, site, setup-focus, psfc, l1-command, firmware-command, multi-site, mcdignore]
related: [pals, site-control-window, controlling-multiple-sites, timing, level, pattern, pin]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# PSFC, PSFC? - (Parallel Setup FoCus)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,488 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSFC

```
PSFC {site|"site_string"|ALL}
```

### PSFC?

```

PSFC? [STR]
```

returns

```
PSFC {"site_string"|ALL}
```

### Parameters

|

site

 |

A single integer representing the site number.

 |
 |

site_string

 |

A string of characters ("0" or "1"). The length of the string corresponds to the number of the configured sites. The nth character of this string stands for site n.

-

1 means that the site is (to be) addressed by any subsequent commands that take the setup focus into account.

-

0 means that the site is not (to be) addressed by any subsequent commands.

If some of the sites that are required to get the setup focus are not available (because they use a channel that is inactivated in the MCDIgnore file) the setup status of these sites will not be changed.

 |
 |

ALL

 |

In the command, this means that all sites that are available for testing (that is, do not use a channel that is inactivated in the MCDIgnore file) are to be addressed by subsequent (setup focus aware) commands.

ALL is returned in the query reply, if the query is issued without the STR parameter, and if all available sites have the setup focus.

 |
 |

STR

 |

forces the query to return a site string even if all available sites have the setup focus. This can be used to check if some sites are not available.

 |

### Example

```
PSFC "11111110"
```

In this example, 8 sites are defined. The PSFC command unsets the setup focus for the last site. The setup data of this site will not be changed by any subsequent command execution.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if not all pins at the site have had their channels assigned by the PALS command.

<!-- 报错节 end -->

## 是什么

**PSFC 是「setup 改动只作用到一部分 site」的开关。** 原文第一句：

> 「The PSFC command serves to restrict certain changes of setup data to a proper subset of the available sites.
> It does this by setting or unsetting the setup focus for individual sites.
> By default, all sites have the setup focus.」

**记住这一句就懂了：** 它**不改任何 setup 数据**，它只决定**后续那些「认 setup focus 的命令」会改到哪些 site。**
**默认是所有 site 都有 focus** —— **也就是说：你不调用 PSFC 的时候，setup 命令改的是全部 site。**

> **⚠️ 这是本页最要紧的一句话（推断，依据在下面两条原文）**：
> `[[jscf]]` 那一篇写着 `With this command you configure setups of those sites that have the setup focus`，
> 而本篇写着 `By default, all sites have the setup focus.`。
> **两条合起来：在一次都没调用过 PSFC 的工程里，`[[jscf]]` 这类命令改的是全部 site。**
> **本页把这条标成推断**——**因为「哪些命令认 focus」那张名单是原文给的（见下），
> 而 `[[jscf]]` 在不在这张名单上，本页这一篇没有列它。**

### 最关键的一张表：**谁认 focus，谁不认**

原文用一个 `Note that` 点名了这件事，**这是本页最有工程价值的一段**：

> 「Note that some setup commands do not take the setup focus into account.
> These commands will always change the setup data of all sites, regardless of any restrictions configured with PSFC.
> Commands that comply with the setup focus are the timing and level setup commands;
> in contrast, most vector setup commands disregard it (but not VECD and VECC).」

| 命令族 | 认不认 focus | 原文依据 |
|---|---|---|
| **timing setup 命令** | **认** | `Commands that comply with the setup focus are the timing and level setup commands` |
| **level setup 命令** | **认** | 同上 |
| **大多数 vector setup 命令** | **不认** | `most vector setup commands disregard it` |
| **`VECD` / `VECC`** | **认**（**是两个例外**） | 括号里的 `(but not VECD and VECC)` |

> **这句话的读法值得说清**：`(but not VECD and VECC)` 挂在 `most vector setup commands disregard it` 后面，
> **所以「不认」的是 `most`（大多数），`VECD` / `VECC` 是那两个不在此列的**——
> **语法上 `but not X` 是「X 不算在刚说的那类里」。**
> **推断：`VECD` / `VECC` 认 focus。**（**原文没有正面写「VECD 认 focus」**，
> **它是从 `but not` 这个结构读出来的。**）
> **其余「哪些 vector 命令不认」原文没有逐条列** —— **它只说 `most`。**

**两族命令的名字含义（本页不展开）**：timing 一族见 `[[timing]]`，level 一族见 `[[level]]`，
`VECD` / `VECC` 是 vector 下载命令（**本页只从本篇读到这两个名字，没有它们的页，故不链**）。

### ⚠️ 原文的 CAUTION：**直接用 PSFC 有出事的风险**

这一段在原文里是 `CAUTION` 开头的，**不是普通的 note**：

> 「Using PSFC directly may have the effect that the site control window does not show the correct
> information about which sites are active and which are not. This may lead to sites, thought to be
> inactive, being updated by site control FW commands with undesirable results or even damage.
> To avoid this, the site control should normally be performed via the site control window
> (see Using the site control) or test method APIs.」

**拆开就是三句：**

| 句 | 含义 |
|---|---|
| ① | **直接调 PSFC，Site control window 的显示可能就和实际对不上了** |
| ② | **后果可能很重**：`thought to be inactive` 的 site **被 site control FW 命令改了**，`or even damage` |
| ③ | **原文的建议**：**site control 的正常做法是走 Site control window 或 test method API**，不是直接发 PSFC |

> **注意 ③ 的措辞是 `should normally be performed`** —— **是「正常应该」，不是「禁止」。**
> **原文没有说「不许用 PSFC」**；**它说的是走 GUI / API 更安全。**
> **本页照抄这个分寸，不把它升格成禁令。**

### 不是所有 site 都能拿到 focus：MCDIgnore

> 「Note also that not all sites that are configured in the pin configuration are necessarily
> available for testing. If a site uses a channel that is inactivated in the MCDIgnore file
> (see MCDIgnore file in Service_Guide Part 1), this site cannot be used for testing.」

**所以「pin configuration 里配了 8 个 site」不等于「8 个 site 都能测」。**
参数表里那条同样的限制又写了一次：

> 「If some of the sites that are required to get the setup focus are not available (because they use a
> channel that is inactivated in the MCDIgnore file) the setup status of these sites will not be changed.」

**即：要不到 focus 的 site，PSFC 不会报错，只是「不动它」。**

### `site_string` 怎么数位：**第 n 个字符 = site n**

这是本页最容易读错的一处，原文写得很短：

> 「A string of characters ("0" or "1"). The length of the string corresponds to the number of the
> configured sites. The nth character of this string stands for site n.」

| 字符 | 原文 |
|---|---|
| `1` | `1 means that the site is (to be) addressed by any subsequent commands that take the setup focus into account.` |
| `0` | `0 means that the site is not (to be) addressed by any subsequent commands.` |

**数位从 1 起**，而且**和 `[[pin]]` 里的 site 号是同一套编号**（推断：
`The nth character of this string stands for site n` 加上例子——见下）。

**示例（`## Example`）把这件事坐实了：**

```text
PSFC "11111110"
```

> 「In this example, 8 sites are defined. The PSFC command unsets the setup focus for the last site.
> The setup data of this site will not be changed by any subsequent command execution.」

**8 个字符、最后一个是 `0` → 是第 8 个 site 被取消 focus。**
**所以字符串长度 = 配了几个 site，顺序就是 site 号顺序，不是从 0 数。**

### 三种写法：`site` / `site_string` / `ALL`

| 写法 | 原文 | 特点 |
|---|---|---|
| **`site`** | `A single integer representing the site number.` | **一次只动一个 site** |
| **`site_string`** | （见上） | **一次动一排**，长度必须对上配的 site 数 |
| **`ALL`** | 「In the command, this means that all sites that are available for testing (that is, do not use a channel that is inactivated in the MCDIgnore file) are to be addressed by subsequent (setup focus aware) commands.」 | **把所有「可用」的 site 都设上 focus** |

> **`ALL` 的定义里有个细节**：它说的是 **`all sites that are available for testing`**，
> 而 `available` 又被括注成 `that is, do not use a channel that is inactivated in the MCDIgnore file`。
> **也就是说 `PSFC ALL` 不是「site 0..N 全部」，是「能测的那些」**——
> **MCDIgnore 里关掉的 site 不会被它设上 focus。**

### 查询：`PSFC?` 和 `STR`

| 写法 | 得到什么 |
|---|---|
| `PSFC?` | **当前有 setup focus 的 site**（`The PSFC? query returns the sites that have currently the setup focus.`） |
| `PSFC? STR` | **强制返回字符串形式，即使所有可用 site 都有 focus** |

原文对 `STR` 的说明是：

> 「forces the query to return a site string even if all available sites have the setup focus.
> This can be used to check if some sites are not available.」

**`STR` 的真正用途是「探测不可用的 site」**——因为不带 `STR` 时，
如果所有可用 site 都有 focus，回复就是那个简写的 `ALL`：

> 「ALL is returned in the query reply, if the query is issued without the STR parameter,
> and if all available sites have the setup focus.」

| 你看到 | 说明 |
|---|---|
| 回复 `ALL` | **所有「可用」site 都有 focus**——**但「可用」是几个、有没有 MCDIgnore 掉的，这里看不出来** |
| 回复一个 0/1 串 | 逐 site 的真实状态——**带上 `STR` 就能总是拿到这个** |

### 一条前置：`PALS` 必须先把通道分完

> `An error is generated if not all pins at the site have had their channels assigned by the PALS command.`

**即：`[[pals]]` 没把该 site 上所有 pin 的通道分完，`PSFC` 就报错。**
**原文只给了这一条错误**（本页这一篇的 `## Errors` 一节全文就这一句）。

## 典型用法

**1. 最小序列（原文没给 Procedure，这是照语法与示例拼的）：**

```text
PALS ...              ← 先给所有 pin 分通道（不满足则 PSFC 报错）
PSFC "11111110"       ← 关掉第 8 个 site 的 focus
<改 timing / level 的 setup 命令>   ← 这些改不到第 8 个 site
PSFC?                 ← 回读：现在谁的 focus 还开着
PSFC ALL              ← 收工：把所有可用 site 的 focus 打开，别留给下一个人
```

**最后一步 `PSFC ALL` 是建议，不是原文要求**（原文没有写「用完要收尾」）——
**但原文说了 `By default, all sites have the setup focus.`，
所以「回到默认」就是 `PSFC ALL`**（推断，依据就是这一句）。

**2. 三种典型场景：**

| 想干什么 | 怎么写 | 依据 |
|---|---|---|
| **只改一个 site 的 level** | `PSFC <site 号>`，然后发 level 命令 | `site` 参数 + level 命令认 focus |
| **跳过某几个 site** | `PSFC "<0/1 串>"` | 示例的用法 |
| **临时只想改一批** | 同上——**没有「批量取反」这种写法**，只能逐位写 | 参数表里只有 `site` / `site_string` / `ALL` 三种 |

**3. 什么时候**不要**用 PSFC：**

- **原文的 CAUTION 说得很直接**：**site control 的正常做法是走 Site control window 或 test method API**。
  **直接发 PSFC 会让 GUI 的显示与实际不一致，进而可能导致误操作甚至损坏。**
- **而且它对「不认 focus 的命令」完全无效**——**大多数 vector setup 命令照改全部 site。**
  **这一条最容易误判**：以为设了 focus 就万无一失，**结果 vector 那边的改动照样铺到所有 site。**
  **要改 vector 的东西，PSFC 帮不上忙**（推断，依据是 `most vector setup commands disregard it`）。

**4. 回读的正确姿势**：

- **只想知道「是不是全都有 focus」** → `PSFC?`（可能回 `ALL`）。
- **想确认有没有 site 被 MCDIgnore 掉了** → **`PSFC? STR`**，
  **因为不带 `STR` 时 `ALL` 会把这件事盖住。**

## 和谁有关

**上游 / 前置：**

- [[pals]] — **前置**。本篇 `## Errors` 逐字写着：
  `An error is generated if not all pins at the site have had their channels assigned by the PALS command.`
  **这是本页唯一一条有逐字原文的依赖关系。**
- [[pals-before-other-setup]] — **同方向的约束页**（**本页的 `PALS` 前置是它的一个实例**）。
  **本页这一篇没有点名那一页**——**这条是照「PALS 是别的东西的前置」这个形状指的**，
  **不声称那一页讲的就是本页这一条。**
- [[pin-configuration-file]] / [[pin-configuration-tool]] — **`available` 这件事的第一道门**：
  `not all sites that are configured in the pin configuration are necessarily available for testing`。
  **本页这一篇只写到「pin configuration 里配了」这一层，没往上游走。**

**下游（谁会受 PSFC 影响）：**

- [[timing]] — **认 focus 的两族之一**（`the timing and level setup commands`）。
  **本页 `stage: pin` 而它是 `stage: timing`**——**PSFC 改的是 timing 那一段的**作用范围**，
  不是 timing 本身。**
- [[level]] — **另一族**，同上。
- [[pattern]] — **恰好相反的一侧**：`most vector setup commands disregard it`。
  **本页 `stage` 不是 `pattern` 的理由就在这里**——**pattern / vector 那一段基本不吃 PSFC。**

**同主题（GUI 那一侧）：**

- [[site-control-window]] — **原文 CAUTION 和 `## Application` 都指着它**
  （`## Application` 全文是 `Site control window.`）。
  **原文的建议是「走那个窗口，别直接发 PSFC」**——**两者的关系是「正常路径 vs 手工后门」。**
- [[controlling-multiple-sites]] — **多 site 测试的主线**。
  **本页这一篇没有点名它**；**关系是照「site control」这个主题指的**。
- [[alias-set-editor]] / [[digital-pins-editor]] / [[dps-pins-editor]] / [[pin-group-editor]] /
  [[utility-pins-editor]] — **GUI 侧的编辑器**，**本页这一篇一个字都没提它们**。
  **列在这里只是因为它们同属 `pin` 这一段的 GUI 面，本页不声称任何具体关系。**

**本页正文点名、但没有页、故不链的东西（反引号 + raw 路径）：**

- `VECD`（raw: `02.06.02.02.325_VECD__VECD__-__VECtor_Download.md`）
  与 `VECC`（raw: `02.06.02.02.324_VECC__VECC__-__VECtor_download_Compressed.md`）——
  **原文点名它们是 vector 命令里认 focus 的两个例外**。
  **本页没读它们，所以「它们为什么例外」本页没有。**
- `Using the site control`
  （raw: `../../03_Use_cases_and_application_papers/03.02_How_to_do_Multi-Site_Testing/03.02.02.04_Using_the_site_control.md`）——
  **原文 CAUTION 指的「正确做法」那一篇**。**本页没读，所以「GUI 里怎么做 site control」本页没有。**
  **这是本页最大的缺口**：**原文的结论是「别直接发 PSFC」，而它指向的那篇本页一个字没读。**
- `MCDIgnore file in Service_Guide Part 1` 与 `MCDIgnore usage and restrictions`（`## Related information`）——
  **MCDIgnore 是本页反复出现的那个「不可用 site」的判据**。
  **本页没读它，也不知道 Service_Guide 在语料里对应哪一篇**——
  **`## Related information` 一节只有这一行字，没有任何链接可跟。**

## 版本

**本文档有 `## Functional changes` 段**，**只有一条**，而且**是一条哨兵值**：

- `Introduced before SmarTest 6.3.2`

> **⚠️ 这一条不是「SmarTest 6.3.2 引入了 PSFC」。** 按 §11.2 ②：
> `Introduced before SmarTest 6.3.2` 是语料里的**哨兵写法**，
> 意思是「**在本文档集覆盖范围开始之前就已经有了**」。
> **照字面读会生成一条假信息**——「6.3.2 新增了 PSFC」，**而且格式齐整、看不出假**。
> **正确的读法：`PSFC` 比本文档集能追溯的最早版本还老。**
>
> **所以本页不写「Introduced in SmarTest 6.3.2」**（§2.7 第 1 条明令这一条不许当成 6.3.2 的变更）。
> **`[[smartest-6.3.2]]` 那一页上也不会把它当成一条新功能**（**本页没读那一页，只照 §11.2 ② 说规矩**）。

**除这一条之外，本文档的 `## Functional changes` 段没有别的条目** ——
**也就是说本篇没有记录 PSFC 在 6.3.2 之后被改过。**
**「没记录」不等于「没改过」**（§13.1 第 ⑥′）——**本页只报「本节只有一行」这个事实。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.md`
（TDC `98698.htm`，113 行）

**本页没做的**：

- **原文 CAUTION 指向的 `Using the site control` 没读**
  （`03_Use_cases_and_application_papers/03.02_How_to_do_Multi-Site_Testing/03.02.02.04`）。
  **后果：原文说「正常应该走 GUI 或 test method API」，但 GUI 里那一步怎么做、
  test method API 是哪个函数，本页一个字都没有。**
- **`MCDIgnore` 相关的一篇都没读**（`MCDIgnore usage and restrictions`、
  `MCDIgnore file in Service_Guide Part 1`）。
  **所以「MCDIgnore 怎么写、写了之后 site 会怎样」本页没有**，
  **只有本篇给的那句「用了被停用通道的 site 不能测」。**
- **`VECD` / `VECC` 两篇没读**。**那两个「例外」的实际行为本页只能照本篇那句话读。**
- **`[[pals]]` 那一篇没读**。**所以「PALS 怎么分通道」本页没有**——
  **本页只有本篇 `## Errors` 里那一句前置。**
- **`[[timing]]` / `[[level]]` / `[[pattern]]` 三页的正文没读**。
  **本篇只说「timing 和 level 认 focus、most vector 不认」，
  至于具体是哪些命令、怎么发，本页一个字都没有。**
- **零张图。** 本篇没有图片引用。
- **没有 `## Procedure` / `## Before you begin` 可读**——本篇只有
  `## Application` / `## Errors` / `## Example` / `## Related information` / `## Functional changes` 五节。
  **所以 `## 典型用法` 里那条序列是本页照语法拼的，不是原文的步骤。**
- **加粗声明**：本页 `## 是什么` 里引的 `PSFC "11111110"` 那一块在「语法 / 参数」节里也有
  （**脚本抽了 `### Example`**）——**本页在正文里重引一次是为了贴着示例讲数位，
  两处都是原文，不冲突。**
- **没有在任何真实机台上跑过 `PSFC`**（`verified: doc-only`）。
  **「直接发 PSFC 会让 GUI 显示不一致」这件事本页没有复现过**——
  **它是原文的 CAUTION，不是本页的实测（§11：文档里有 ≠ 这台机器上会这样）。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① `PSFC?` 的语法块里，第一行是空的。** 原文第 26–29 行逐字是
> 一个开着的代码围栏、**跟着一个空行**、然后才是 `PSFC? [STR]`、然后闭合围栏。
> **即这一段的语法行前面多了一个空行**（对比同篇 `## PSFC` 那一段，围栏后直接就是 `PSFC {site|"site_string"|ALL}`）。
> **不影响语义，但脚本抽这一节时会把它当一个空行**——**本页照实记，不替它删。**
> **② 同族的措辞不一致（跨篇）：** 本篇第 31 行写的是 `returns`（**没有冒号**），
> 而 `[[jsdf]]` 那一篇写的是 `returns:`。**这是语料在不同篇里的排版习惯差异，
> 本篇本页不动它**（**这一条是拿两篇对出来的，本页只声明本篇的写法**）。
> **③ 本页在本篇里没有发现坏字（`鈥` / `渭` / `掳` 那一类）。**
> **但这是「本页读到的」，不是「本篇干净」**（§13.1 第 ⑥′）。

`verified: doc-only`
