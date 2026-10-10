---
type: object
title: PSTE, PSTE? - (Parallel SiTe Enable)
layer: L1
stage: run
tags: [run, multi-site, site, pste, l1-command, firmware-command, mcdignore, site-control]
related: [pals, psfc, site-control-window, controlling-multiple-sites, pin]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# PSTE, PSTE? - (Parallel SiTe Enable)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,148 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSTE

```
PSTE {sites}
```

### PSTE?

```
PSTE? [STR]
```

returns

```
PSTE {sites|"site_string"}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98711.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：sites | The sites parameter is an integer that specifies the number of sites (to be) configured. The maximum is 1024. For more information, refer to Number of s…
> 表内引用（2 条，供检索）：`Number of sites`（raw: `../../01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md#_116532__r_numberOfSites`） · `SmarTest system parameters - default values and limits`（raw: `../../01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md`）

### Example

```
> PSTE 3
```

This example configures three sites (site 1, site 2, and site 3).

```
> PSTE? STR
< PSTE "101"
```

This example says that three sites are configured, but that only two of them (site 1 and site 3) are available for testing. Site 2 uses a channel that is listed in the MCDIgnore file, and therefore cannot be used for testing.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- Not all pins at the site have had their channels assigned by the `PALS`（raw: `02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md`） command.
- All channels are listed in the MCDIgnore file and therefore not available for testing.

<!-- 报错节 end -->

## 是什么

**PSTE 只回答一个问题：这次测试配了几个 site。** 原文第一句：

> 「The PSTE command defines how many sites are to be configured in the pin configuration.
> Note that not all of these sites will be actually available for testing.
> If one of the channels that is used by a site is inactivated in the MCDIgnore file
> (MCDIgnore file in Service Guide Part 1), this site cannot be used for testing.」

**「配几个」和「能用几个」是两件事**——这就是本页全部内容的骨架：

| 概念 | 谁决定 | 命令 |
|---|---|---|
| **配了几个 site** | **PSTE**（`sites` 参数） | 本页 |
| **哪几个 site 真的能测** | **MCDIgnore 文件**（通道被停用的 site 不能测） | 本页只提，不解释 |

**它不改任何 pin / channel 的东西**——它定义的是**数量**，
**而这个数量落在 pin configuration 上**（`how many sites are to be configured **in the pin configuration**`）。

### ⚠️ 最容易错的一处：PSTE 和 Site Control window 的「启用」**不是一回事**

原文专门用了一个 `Note` 说这件事，**这是本页最该先读的一段**：

> 「Do not confuse the effects of the PSTE (Parallel SiTe Enable) command with the enabled state of
> the Site Control window. This state has no counterpart in the firmware.
> The PSTE command determines the number of sites that are displayed in the Site Control window.
> However, only available sites can be set to enabled in this window.」

拆成三句：

| 句 | 原文 | 读法 |
|---|---|---|
| ① | `Do not confuse … with the enabled state of the Site Control window.` | **别把两者当同一个东西** |
| ② | `This state has no counterpart in the firmware.` | **GUI 里那个「启用/停用」状态，固件层没有对应物**——**它不落盘、没有命令可查** |
| ③ | `The PSTE command determines the number of sites that are displayed in the Site Control window. However, only available sites can be set to enabled in this window.` | **PSTE 决定那个窗口里显示几行；但窗口里能勾成 enabled 的只有 available 的 site** |

> **② 那句是全篇最重的一句**：**「Site Control window 里的 enabled 状态在固件里没有对应物」**——
> **意思是这个状态是纯 GUI 的**，**没有命令能读它、也没有命令能写它。**
> **所以「我在窗口里禁用了某个 site」这件事，PSTE? 查不出来、也不会反映出来。**
> （**这是本页的读法**；原文只说了 `has no counterpart in the firmware`，
> **没有展开「那它存在哪里」**——**语料未写**。）

### `PSTE` / `PSTE?` 的分工

| 形式 | 干什么 | 原文 |
|---|---|---|
| `PSTE {sites}` | **设**配置几个 site | `The PSTE command defines how many sites are to be configured in the pin configuration.` |
| `PSTE?` | **只回数量** | `If this parameter is omitted, PSTE? will return the number of sites that are configured in the pin configuration.` |
| `PSTE? STR` | **回 0/1 串**，说明哪几个可用 | `If you specify this optional keyword in the query, PSTE? will return a site string.` |

原文对查询的总说明是：

> 「The PSTE? query simply returns the number of configured sites, or detailed information about which
> of these configured sites is actually available for testing.」

**所以 `PSTE?` 有两种回复形态，靠 `STR` 切换。** 语法行里也写着两种：
`PSTE {sites|"site_string"}`

### `sites`：一个整数，**上限 1024**

> 「The sites parameter is an integer that specifies the number of sites (to be) configured. The maximum is 1024.」

**1024 这个数原文是从别处引的**——它跟着两行引用走：

> 「For more information, refer to Number of sites in SmarTest system parameters - default values and limits.」

**那两篇本页没读**（路径见 `## 和谁有关`），
**所以「为什么是 1024」「是不是所有配置下都是 1024」本页答不上来。**

### `site_string`：**0 和 1 的含义，和它的长度**

> 「A string consisting of "0" and "1". The length of the string corresponds to the number of the
> configured sites. The nth character of this string stands for site n.」

| 字符 | 原文 | 含义 |
|---|---|---|
| `0` | 「\"0\" indicates that the respective site uses a channel that is listed in the MCDIgnore file, and that this site therefore cannot be used for testing.」 | **这个 site 用了一条被 MCDIgnore 停用的通道 → 不能用** |
| `1` | `"1" indicates that the site can be used.` | **能用** |

**两点必须记住：**

- **字符串长度 = 配了几个 site**，**第 n 个字符 = site n（从 1 数）**——
  和 `[[psfc]]` 那一族的 `site_string` 用的是同一套计数法（**但语义不同，见下**）。
- **`0` 在这里表示「不可用」，不是「未选中」。** **这是个反直觉的点**：
  在「勾选」的语境里 0 通常意味着「不选」，**而这里的 0 讲的是硬件层面的不可用。**

**示例把这件事坐实了：**

```text
> PSTE? STR
< PSTE "101"
```

> 「This example says that three sites are configured, but that only two of them (site 1 and site 3)
> are available for testing. Site 2 uses a channel that is listed in the MCDIgnore file,
> and therefore cannot be used for testing.」

**`"101"` = 三个 site，第 2 个不可用。** 长度对得上，数位从 1 起。

### 写 `PSTE` 的示例：**它会连带把 site 号也定了**

```text
> PSTE 3
```

> 「This example configures three sites (site 1, site 2, and site 3).」

**注意「三个 site」被展开成 `site 1, site 2, and site 3`**——
**即 site 号是从 1 起的连续编号**（推断：原文只给了这一个例子，
**它没有说「site 号必须连续」或「一定从 1 开始」**；
**本页把 `site 1` 到 `site 3` 这个现象记下来，不把它升格成规则。**）

### 两条报错条件

> 「An error is generated if:
>
> - Not all pins at the site have had their channels assigned by the PALS command.
> - All channels are listed in the MCDIgnore file and therefore not available for testing.」

| 条件 | 读法 |
|---|---|
| **`PALS` 没分完通道** | 和 `[[psfc]]` 的前置同源——**`PALS` 是这一族共同的入场券** |
| **所有通道都在 MCDIgnore 里** | **一个能用的都没有** → 报错。**注意它说的是 `All`** |

> **第二条的边界原文没有界定**：`All channels` 指的是
> **「全部 site 合起来的全部通道」**还是**「某一个 site 的通道」**，
> **本篇没有写清**（§13.1 第 ⑥′：**「本页没找到界定」与「原文没界定」不是一回事，
> 但本页这一篇里确实只有这一句**）。**本页不替它界定。**

### 一条限制，没有解释

> 「This command does not support pins in HV mode.」

**原文就这一句。** `HV mode` 是什么、为什么不支持、不支持时会怎样——
**本篇一个字都没有。本页也不替它补**（§11：不臆造）。

## 典型用法

**1. 顺序（原文没给 Procedure，这是照语法与前置换的）：**

```text
PSB? / PALS ...        ← 通道分配（PALS 没分完，PSTE 会报错）
PSTE 3                 ← 配 3 个 site
PSTE? STR              ← 回读："101" 之类的串，看哪几个真的能用
```

**2. 两条回读路线怎么选：**

| 想知道 | 发什么 | 得到什么 |
|---|---|---|
| **配了几个** | `PSTE?` | 一个整数 |
| **哪几个能用** | `PSTE? STR` | 一个 0/1 串（**`0` = 不可用**） |

**3. 拿到 `PSTE? STR` 之后该做什么（推断，原文没说）：**
串里为 `0` 的 site 是**因为 MCDIgnore 掉的通道**而不可用
（原文对 `0` 的定义就是这一句）。
**所以「某个 site 明明配了却不出数据」的第一件事是查这个串**——
**这一条是建议，不是原文的流程**。

**4. 不要指望 PSTE 反映 GUI 的勾选状态**：
原文 `This state has no counterpart in the firmware.`
—— **在 Site Control window 里改的启用/停用，`PSTE?` / `PSTE? STR` 都不会告诉你有变化。**

**5. 不要和 setup focus 混**：**PSTE 管「有几个 site」，`[[psfc]]` 管「setup 改动落在哪些 site」。**
**两者是两条独立的轴**——**但两边都有一个叫 `site_string` 的同名参数，
而且 0/1 的含义**不**一定相同。**
**本页只声明本篇对 `site_string` 的定义（见上），
两个命令的 0/1 是否同义，请自己回两篇 raw 各核一遍再混用。**

## 和谁有关

**前置 / 上游：**

- [[pals]] — **前置**。本篇 `## Errors` 的第一条点名它：
  `Not all pins at the site have had their channels assigned by the PALS command.`
  **原文在这里给的是一条链接，链接文本就是 `PALS`**——**这是本页唯一一条有逐字原文的依赖关系。**
- [[pals-before-other-setup]] — **同方向的约束页**。**本页这一篇没有点名它**——
  **这条是照「PALS 是别的东西的前置」这个形状指的**，**不声称那一页讲的就是本页这一条。**
- [[pin-configuration-file]] — **PSTE 写的那个数落在哪儿**：
  `how many sites are to be configured in the pin configuration`。
  **本页这一篇用的是 `pin configuration` 这个说法，没有给文件路径**——
  **指向那页是推断（依据是这一族命令里 `pin configuration` 这个术语的常规所指），本页标明。**
- [[pin]] — **同上的 stage 面**：本页 `stage: run` 而它是 `stage: pin`。
  **PSTE 改的是 pin 那一段的产物，但调用它的时机在 run 前后**（**这是 stage 字段「最近的一段」的用法，§6**）。

**同主题（GUI 那一侧）：**

- [[site-control-window]] — **原文那个 `Note` 整段都在讲它**，
  而 `## Application` 一节全文是 `Site control window.`
  **两者的关系是「命令定义数量 / 窗口显示数量」，而且原文明确说窗口那个 enabled 状态固件里没有。**
- [[controlling-multiple-sites]] — **多 site 测试的主线**。
  **本页这一篇没有点名它**；**关系是照「site」这个主题指的**。

**同族、同名参数、但本页不并列的：**

- [[psfc]] — **同族命令，参数表里有一个同名参数 `site_string`**。
  **本页这一篇一个字都没提 `PSFC`**——**所以 `[[psfc]]` 与 PSTE 的分工、
  以及两边 `site_string` 的 0/1 是不是同义，本页一个字都不写**
  （§5：**不许把别处文档的内容写进本页正文**）。
  **这一条提醒本身就是本页能给的极限：混用两个命令之前，回两篇 raw 各核一遍。**

**本页正文点名、但没有页、故不链的去处（反引号 + raw 路径）：**

- `Number of sites` 与 `SmarTest system parameters - default values and limits`
  （raw: `../../01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md`）——
  **`The maximum is 1024` 那一条的出处**。**本页没读，所以那个 1024 的来历本页没有。**
- `MCDIgnore usage and restrictions`（`## Related information` 全文就这一行）——
  **本页反复出现的那个「不可用 site」的判据的来源**。
  **本页没读它，也不知道它在语料里对应哪一篇**——
  **`## Related information` 一节只有这一行字，没有任何链接可跟。**
  **这是本页最大的缺口**：**「为什么这个 site 不可用」的答案全在那一篇里。**
- **`HV mode`** —— 原文 `This command does not support pins in HV mode.`
  里的那个 `HV mode`。**本篇没有解释它、没有链接**，
  **本页也不知道它在语料里有没有一篇专门讲它的**（**没查**）。

## 版本

**本文档有 `## Functional changes` 段**，**只有一条**，而且**是一条哨兵值**：

- `Introduced before SmarTest 6.3.2`

> **⚠️ 这一条不是「SmarTest 6.3.2 引入了 PSTE」。** 按 §11.2 ②：
> `Introduced before SmarTest 6.3.2` 是语料里的**哨兵写法**，
> 意思是「**在本文档集覆盖范围开始之前就已经有了**」。
> **照字面读会生成一条假信息**——「6.3.2 新增了 PSTE」，**而且格式齐整、看不出假**。
> **正确的读法：`PSTE` 比本文档集能追溯的最早版本还老。**
> **所以本页不写「Introduced in SmarTest 6.3.2」**（§2.7 第 1 条）。
> **顺带记一笔：`[[psfc]]` 那一篇的版本段是同一个哨兵值**——
> **这两个命令很可能同批存在**（**这是推断，依据只是两篇写着同一句哨兵；
> 原文没有说它们同批引入。**）

**除这一条之外，本文档的 `## Functional changes` 段没有别的条目**——
**本篇没有记录 PSTE 在 6.3.2 之后被改过。**
**「没记录」不等于「没改过」**（§13.1 第 ⑥′）：**本页只报「本节只有一行」这个事实。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.md`
（TDC `98711.htm`，73 行）

**本页没做的**：

- **`01.04_SmarTest_system_parameters_-_default_values_and_limits` 没读。**
  **所以 `The maximum is 1024` 这一条本页只能照抄，不知道它和其他系统参数有没有联动。**
- **`MCDIgnore usage and restrictions` 与 `MCDIgnore file in Service Guide Part 1` 都没读。**
  **所以「MCDIgnore 怎么写、写了之后 site 会怎样」本页一个字都没有**，
  **只有本篇给的那句「用了一条被停用通道的 site 不能测」。**
- **`[[pals]]` 那一篇没读。** **「PALS 怎么分通道」本页没有。**
- **`[[psfc]]` 那一篇的内容本页一个字都没写进正文**（见 `## 和谁有关` 里那条说明）。
  **两边的 `site_string` 能不能互推，本页不作断言。**
- **`[[site-control-window]]` 那一页没读。** **「那个窗口长什么样、怎么勾」本页没有**——
  **本页只有本篇那句「它和 PSTE 不是一回事、且固件里没有对应物」。**
- **零张图。** 本篇没有图片引用。
- **没有 `## Procedure` / `## Before you begin` 可读**——本篇只有
  `## Application` / `## Errors` / `## Example` / `## Related information` / `## Functional changes` 五节。
  **所以 `## 典型用法` 里那条序列是本页照语法拼的，不是原文的步骤。**
- **加粗声明**：本页 `## 是什么` 里引的两个示例块
  （`> PSTE 3` 与 `> PSTE? STR` / `< PSTE "101"`）**在「语法 / 参数」节里也有**
  （**脚本抽了 `### Example`**）——**正文重引一次是为了贴着例子讲数位，两处都是原文，不冲突。**
- **没有在任何真实机台上跑过 `PSTE`**（`verified: doc-only`）。
  **「配了 3 个 site 之后真的能测 3 个」这件事本页没有验证过**（§11）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① `Note` 后面缺标点。** 原文第 12 行逐字是：
> `Note Do not confuse the effects of the PSTE (Parallel SiTe Enable) command with the enabled state of the Site Control window.`
> —— **`Note` 与句子之间没有冒号、也没有 `that`**。
> 同族的命令文档在别处写的是 `Note that` / `Note also that`（**那一处的原文不在本页读的这一篇里**），
> **只有这一篇是裸的 `Note` + 句子。本页照实引，不替它补标点。**
> **② 语法块前的引导词缺冒号。** 原文第 28 行写的是 `returns`——
> **而同一族的 `JSDF` 那一篇第 26 行写的是 `returns:`**（**那一处也不在本页读的这一篇里**）。
> **跨篇排版习惯不一致，本页两处都照原样记，不替任何一篇统一。**
> **③ 参数表第一行少一个前导空格。** 原文第 36 行是 `| sites |`，
> **而同表后面几行（第 40 行 `| site_string |`、第 47 行 `| STR |`）都带一个前导空格。**
> **这一点在「语法 / 参数」节里看得出来**（那一节的第一行 `| sites |` 顶格，
> 后面几行都带前导空格）——**本页照实记，不替它对齐。**
> **④ `All channels` 的范围原文没界定**（见 `## 是什么` 里那条）。
> **这是「原文没写清」，不是「本页没找到」**——**本篇 `## Errors` 一节全文只有那两条 bullet。**
> **⑤ 本页在本篇里没有发现坏字（`鈥` / `渭` / `掳` 那一类）。**
> **但这是「本页读到的」，不是「本篇干净」**（§13.1 第 ⑥′）。

`verified: doc-only`
