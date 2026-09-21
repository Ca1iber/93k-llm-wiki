---
type: object
title: Data Logging Profiles
layer: file
stage: results
tags: [data-logging, profile, log, flag, sampling, testflow]
related: [data-logging-profile-api, flag, flags-page, device-directory, testflow]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Data Logging Profiles

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **983 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

You can create two different data logging profiles:

- A standard profile that logs only the pass/fail results of all tests.
- A debug profile that logs certain details such as pin value results, first failing cycles and so on.

If you notice a drop in yield during a production run, just activate the debug profile to enable more detailed logging. The system will then log the results needed to understand the reasons for the yield drop.

There is no need to toggle all relevant flags per hand or to modify the testflow file: The flags are automatically set through the activation of the profile with just a single mouse click.

You can even program the testflow's test methods to monitor yield drops. If the number of failing tests exceeds a certain threshold, a simple function call from within a test method activates the debug profile mentioned above, to change the flag configuration on-the-fly. This way, the debug profile is activated automatically without user intervention.

<!-- 语法节 end -->

## 是什么

**data logging profile（数据记录配置）是一组「记什么、怎么记」的规则。** 原文的定义句：

> 「A data logging profile is a set of data logging rules that determine which data is logged
> within the test system and how.」

**它不是一份日志，是一份「日志的开关组合」。** 原文紧接着两句把它的价值说完了：

> 「Data logging profiles provide a very easy and powerful way to control data logging and store
> setups for easy re-use.
>
> With data logging profiles, you can change the flag settings for optimized testflows in
> production without deleting the optimization.」

**第二句是这一页的题眼**：生产用的 testflow 为了跑得快，把一堆 flag 关掉了；
**profile 让你在需要的时候把这套 flag 组合换掉，而不用把那份优化过的 testflow 改坏。**

**原文给了三条好处**（`## The advantages of using profiles`，逐字）：

| 好处 | 原文 |
|---|---|
| Ease of use | `Data logging profiles allow one-click data logging (on/off).` |
| Flexibility | `Data logging profiles allow predefining data logging configurations that can be switched as needed in production.` |
| Efficiency | `Data logging profiles allow efficient fixed and adaptive sampling.` |

**注意第三条里的两个词 `fixed` 与 `adaptive`**——那是两种采样方式，
本篇只在这里点了名，**详解在子页 `Data logging profiles and sampling`**（**那个子页本页没读**）。

### 出厂就带两个 profile

`## Default data logging profiles` 一节，原文：

> 「Two default data logging profiles are delivered with SmarTest:
>
> - datalog_OFF.prf
> - datalog_ON.prf」

| 文件 | 装载后（原文） |
|---|---|
| `datalog_OFF.prf` | `no data is logged during test program execution and no information is written to a log file` |
| `datalog_ON.prf` | `data is logged per pin, with value results for all tests` |

**两个都是可以改的**：原文 `You can customize both default profiles according to your requirements.`
（**改完还能不能还原——子页 `Restoring the default data logging profiles` 管这件事，本页没读**。）

**注意 `OFF` / `ON` 是全大写**，而且这句里一个带冠词一个不带：
`If the datalog_OFF.prf profile is loaded…` 对 `If datalog_ON.prf is loaded…`。
**文件名照大写写，别写成 `datalog_off.prf`。**

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段，没有任何命令或 API 调用。**
本篇是一页**总览**——「怎么用」的答案在它 `#### Subtopics` 列的 8 个子页里。

**本篇自己给出的用法只有两条场景 + 一条兼容做法：**

**① 生产掉良率时切 profile**（原文，这就是本页语法节里那段）：

> 「You can create two different data logging profiles:
>
> - A standard profile that logs only the pass/fail results of all tests.
> - A debug profile that logs certain details such as pin value results, first failing cycles and so on.
>
> If you notice a drop in yield during a production run, just activate the debug profile to enable
> more detailed logging. …」

**切换的代价是「一次鼠标点击」**，原文：

> 「There is no need to toggle all relevant flags per hand or to modify the testflow file: The flags
> are automatically set through the activation of the profile with just a single mouse click.」

**这句话点明了 profile 与 flag 的关系：profile 做的事就是替你设 flag**
（flag 的清单在 [[flag]] / [[alphabetical-list-of-flags]] 那边；**那两页本篇没提，是本页自己的联想**）（推断）。

**② 让 test method 自己切**（原文）：

> 「You can even program the testflow's test methods to monitor yield drops. If the number of
> failing tests exceeds a certain threshold, a simple function call from within a test method
> activates the debug profile mentioned above, to change the flag configuration on-the-fly. This
> way, the debug profile is activated automatically without user intervention.」

**`a simple function call` 具体是哪个函数——本篇没写**（推断：那是子页
`Data logging profile API` 的内容，**本页没读那一篇**）。

**③ 把老的生产设置当 profile 用**（`## Compatibility with production settings`，原文两步）：

> - 「Copy the production settings files to the directory `<device directory>/profiles/`.」
> - 「Load the production settings files as read-only data logging profiles as described in
>   `Loading a data logging profile`.」

**注意 `read-only` 这个限定**：这样装载进来的 profile **是只读的**。
原文在这一句里同时给出了目录形态：**`<device directory>/profiles/`**。

**本页没给的（都在子页里）**：加载 / 卸载 / 与 testflow 关联 / 还原默认 / Profile Editor 界面 /
采样 / API。**8 个子页一篇都没读**（见「出处」）。

## 和谁有关

- **关于「单数的 `data-logging-profile`」——本页上一版在这里写错过，记在这里。**
  上一版把单数名当成「同一主题的另一页」（还带一个（推断））；
  **实测是错的**：`extract/wiki-plan.csv` 里**只有复数这一行**，
  `extract/prose-allowlist.txt` 里单数、复数两个名字都有，
  而**单数名既没有页、也不在建页计划里**——**它永远不会被建**。
  **原先指单数名（`data-logging-profile`）的几处已改指本页**（见「出处」）。
  **这里故意不写成双方括号**：本库第八类把代码跨度里的 wikilink 也算作链接，
  写上就等于把这个刚从悬空清单里去掉的名字原样加回去。
  （**注意与下一行的 `data-logging-profile-api` 区分**：那个是另一件东西，有一篇自己的文档。）
- [[data-logging-profile-api]] — **让 test method 在运行中切 profile 的那套 API**。
  依据是本篇 `#### Subtopics` 里的 `Data logging profile API` 这一条子页名
  （**那页本页没读**）。
- [[flag]] / [[flags-page]] — **profile 实际改的东西**。原文说
  `The flags are automatically set through the activation of the profile`
  与 `to change the flag configuration on-the-fly`。
  **本篇没有一句话把这些 flag 与 [[alphabetical-list-of-flags]] 那张表连起来**——
  **那条边是本页接的，不是文档给的**（推断）。
- [[device-directory]] — **`profiles/` 挂在它下面**。原文给了路径形态
  `<device directory>/profiles/`（**那页本页没读**）。
- [[testflow]] — **profile 要关联到的对象**。本篇 `#### Subtopics` 里有一条
  `Associating a data logging profile with a testflow`；正文也提到
  `to modify the testflow file`（**那两处本页都没读**）。
- [[log]] — **最终产物**。原文 `no information is written to a log file`、
  `the results needed to understand the reasons for the yield drop`。
- `Flags and data logging profiles` / `Loading a data logging profile` /
  `Unloading a data logging profile` / `Associating a data logging profile with a testflow` /
  `Restoring the default data logging profiles` / `Profile Editor` /
  `Data logging profiles and sampling` / `Data logging profile API`
  （**8 篇子页，均未建、均未读**）——**本篇的全部操作细节都在这 8 篇里，本页一篇都没有。**
- [[results]] — **doc 的 `stage` 是 `results`**，
  但**本篇正文没有一句话把它与 profile 连起来**（推断，仅指归属）。

## 版本

原文 `## Functional changes` 段**只有一行**：

- `Introduced before SmarTest 6.3.2`

**这一行要按哨兵值读**（§11.2 ②）：它的意思是
「**在本文档集覆盖范围开始之前就已经有了**」，
**不是「SmarTest 6.3.2 引入了 data logging profile」**。
照字面读会造出一条假版本事实，而且格式齐整、看不出是哨兵。

**本篇没有任何一条真版本记录。** 所以：

- **两个默认 profile（`datalog_OFF.prf` / `datalog_ON.prf`）是哪个版本开始随 SmarTest 出厂的——语料未写。**
- **`profiles/` 目录、Profile Editor、API 的引入版本——语料未写。**

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.md`
（`98046.htm`，**3,593 字节 / 67 行**）——**整篇读完**。

**本页没做的：**

- **8 个子页一篇都没读**（见「和谁有关」最后一条）。
  **所以本页只回答了「profile 是什么、为什么要有它」，
  「怎么加载、怎么卸载、怎么关联、怎么还原、编辑器长什么样、API 怎么调」一个字都没有。**
- **本篇文档里没有 `## Procedure` 段、没有 `## Errors` 段、没有 `## Application` 段、没有任何图、
  没有任何代码块、没有一条 API 签名。**
- **「语法 / 参数」节里的内容不是语法。** 脚本收的是原文的 `## Example` 段（**983 字符**），
  那一段是**散文**（讲两种 profile 的用法），里面**没有一个参数、没有一行代码**。
  —— **不是脚本把语法收坏了，是这篇文档根本没有语法段。**
  本页照原样保留语法节（§4：语法节不许改），并在此说明它是什么。
- **`datalog_ON.prf` 的默认采样率、日志格式、文件落点——本篇没写。**
- **`SmarTest` 之外的产品线（MTP / SmartRDI / TP360 / SmartProd）有没有同名机制——语料未写。**

> ⚠️ **语料瑕疵，照实记下，一处都没替它改**：
> ① **`#### Subtopics` 是 4 级标题，却是本篇最顶层的结构段**——
>    它出现在 `## The advantages of using profiles` 这些 2 级标题**之前**，
>    级别却比它们深。**全语料同此形态**（[[apg-pattern-file]]、[[device-access-file]]、
>    [[dc-scale-uhc4t-card]] 也是 `#### Subtopics`），**不是本篇独有**（推断）。
> ② **`datalog_OFF.prf` / `datalog_ON.prf` 的冠词不一致**，逐字：
>    `If the datalog_OFF.prf profile is loaded…` 与 `If datalog_ON.prf is loaded, data is logged
>    per pin` —— 一个带 `the`，一个不带。**同段相邻两句。**
> ③ **「一次点击」这个说法与「用 API 自动切」并列出现，中间没有任何限定**：
>    `with just a single mouse click` 讲的是人在 GUI 上切，
>    下一段就讲 `without user intervention` 的程序化切换。
>    **原文没有一句话说明这两条路是不是同一个机制。**
> ④ **`## Compatibility with production settings` 只说了「复制到 `profiles/` 就能当只读 profile 用」，
>    没有说「生产设置文件」与「profile 文件」是不是同一种格式**——
>    而它给的第二步是「像加载 profile 那样加载它」。**这一点原文没说清。**
> ⑤ **标题层级跳跃**：`## The advantages…` / `## Default…` / `## Example` /
>    `## Compatibility…` / `## Functional changes` 全是 2 级，
>    中间没有任何 3 级标题，而正文里却用加粗小标题式的分段（如 `Two default data logging
>    profiles are delivered with SmarTest:`）。**原文没有任何 `###`。**

`verified: doc-only` —— **本页没有在任何真实系统上加载过 profile**（§11：文档里有 ≠ 这台机器上能用）。
