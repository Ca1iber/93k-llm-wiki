---
type: object
title: DISCONNECT
layer: L2
stage: testmethod
tags: [disconnect, connect, l2, test-method-api, test-control, relay, global-connect-state, shared-source-doc]
related: [testmethod, mapping-testmethod, mapping-testflow, connect, dc-test-programming, special-test-suites, dps-power-flags-get-functions, dpspins-resources, utility-power-supplies]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# DISCONNECT

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **447 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
CONNECT();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example

```
CONNECT();
...
...
PMU_IFVM("PIN1,PIN2").iForce(100 uA).settling(5 ms);

PMU_IFVM("PIN1,PIN2").limits("limit1").execute();
...
...
```

To use the `PMU_IFVM`（raw: `02.07.04.01.151_PMU_IFVM.md`） API, you must set the tester to the CONNECT status. This example connects the tester resources to the DUT with the CONNECT API before DC measurement.

<!-- 语法节 end -->

## 是什么

**`DISCONNECT()` 是 test method 里与 `CONNECT()` 成对的那条断连 API。** 但有一件事要先说清：
**本页 `sources:` 只有一篇文档，而那一篇是 CONNECT 的文档**——它**同时讲 CONNECT 与 DISCONNECT**。
**所以：连接那一半（三件动作、多 site 位置限制、`## Example`、头文件）在 [[connect]] 里，两页共用同一篇文档。**

**这一篇里直接写到 `DISCONNECT()` 的只有一条 `Note`，三句。** 全文逐字：

> 「Note Do not mix the global CONNECT()/DISCONNECT() with individual relay switching.」

> 「Manually switching relays (see for example SmartRDI: Digital channel relay control and PPMU_RELAY) will not change the global connect state, and so CONNECT()/DISCONNECT() will see no action to perform.」

> 「The relays which initially have been switched manually, must again be individually and manually switched to change their state.」

**关键在原文的写法本身：`CONNECT()/DISCONNECT()`。** 两个 API 用的是**同一个** `global connect state`
——所以「手工切过 relay 之后 `DISCONNECT()` 什么都不做」与 `CONNECT()` 那一边是**同一个原因**，不是两件事。

**它的机制（本页从这三句读出来的）**：

| 你此前做过什么 | 再调 `DISCONNECT()` | 依据 |
|---|---|---|
| 什么都没手工切过 | 正常断开 | **（推断）**：那三句讲的是「手工切过才失效」，反过来说没切过就正常 |
| **手工切过 relay** | **全局 connect state 没变 → `see no action to perform`**——它以为没自己什么事 | 原文第二句 |
| 想把手工切过的 relay 改回去 | **必须再手工切**（`must again be individually and manually switched`） | 原文第三句 |

**这张表是本页把三句并起来的（推断）**，依据是原文自己写出的因果
（`will not change the global connect state, and so … will see no action to perform`）
与最后那句 `must again be individually and manually switched`——
**三条引文都是原文，「表格化的合并」是推断。**

**这一条的实操含义**：**手工切和全局 connect state 是两套账，互不知道。**
`DISCONNECT()` 查的是全局那一套，**它不会去读你手工切过的 relay**；
动词是 `see no action to perform`——**不是「拒绝执行」，是「看着没事可做」。**

### 它的边界（**语料未写**）

| 问题 | 本页的出处文档 |
|---|---|
| 断开时会做什么动作（断电？断 AC relay？sequencer 变成什么态？） | **一个字没写** |
| 有没有参数、有没有返回值 | **一个字没写**（`There are no parameters.` / `There is no return value.` 那两句是 **CONNECT** 的） |
| 定义在哪个头文件 | **一个字没写**（`TestControl.h` 那一句是 **CONNECT** 的） |
| 什么时候该断开 | **一个字没写** |

**本页不把 CONNECT 那一半的答案搬到 DISCONNECT 上。**

### ⚠️ 本页「语法 / 参数」节里是 `CONNECT();`，不是 `DISCONNECT()`

那一节是脚本按 `sources:` 逐字抽的（§4：**这一节不许手改**），而本页唯一那一篇就是 **CONNECT 的文档**——
**所以本页的语法节与 [[connect]] 那页逐字相同（447 字符），内容是 `CONNECT();` 的 `## Syntax` 与 `## Example`。**
**`DISCONNECT()` 自己的语法、参数、返回值，本页一个字都没有**——它们在语料里是**另一篇**：
`02.07.04.01.41_DISCONNECT.md`（2,499 字节，**本页没读**，见「出处」）。
**本页没有把它改写成 `DISCONNECT()` 的样子，也没有假装它讲的是 DISCONNECT。**

## 典型用法

**语料未写。** 本页的出处文档**没有** DISCONNECT 的 `## Example`、**也没有** `## Procedure` 与 `## Before you begin`——
它唯一的 `## Example` 是 `CONNECT();` 那一段（**那是 CONNECT 那一半，已在上面「语法 / 参数」节里逐字**）。
**动作顺序、调用时机、断开后怎么恢复：本页答不了。**

**本页能给的只有一条操作禁令**（来源就是上面那条 `Note`）：

| 别做的事 | 为什么（原文的因果） |
|---|---|
| **把全局的 `DISCONNECT()` 和单独切 relay 混着用** | 手工切**不改变全局 connect state**，`DISCONNECT()` **看不到该做的事**（`see no action to perform`） |
| **指望 `DISCONNECT()` 把手工切过的 relay 复位** | 原文要求**再手工切回去**（`must again be individually and manually switched`） |

**想找「什么时候必须断开」**：本页的出处文档里没有；[[connect]] 那页记了它从 [[dc-test-programming]]
转述的两条时机——**本页没有独立读 [[dc-test-programming]]**，所以**本页只指路、不复述它的结论**。

## 和谁有关

- [[connect]] — **对手方，而且与本页共用同一篇文档**（`02.07.04.01.18_CONNECT.md`）。那一篇的首段、三件连接动作、多 site 位置限制、`## Example` 全在 [[connect]] 那页；**本页只写 DISCONNECT 那一半**。`extract/wiki-plan.csv` 里 `connect` 与 `disconnect` 两个 slug 的 `rel` **都是这一篇**——**这不是巧合，是那一篇同时讲两者**。
- **语料里 DISCONNECT 自己的那一篇（`02.07.04.01.41`）没有页**：`extract/wiki-plan.csv` 里查不到以它为 `rel` 的行，**本页的 slug 也不指向它**。**本页没读它**——「断开怎么做」全都不在本页。
- [[mapping-testmethod]] — 主表第 5 行「给 DUT 上电 / 断电」的 **L2 格写的就是 [[connect]] 与 [[disconnect]] 两页**。它把那一行的 **L1 格判成 `?`（不是 `—`）**，理由它自己给了：固件层**确实有东西**（routing / relay 一类命令），**但语料没说 `CONNECT()` 对应哪一条**；它还写明**那四张图里没有一张出现固件命令名**，所以那一格**看完图仍是 `?`**。**本页不替它猜一条命令**（§2.5：不许猜）。
- [[mapping-testflow]] — 主表第 13 行 `bin_disconnect` special test suite 的 **L2 格写的是 `DISCONNECT`**。**那句话是那一页从 `02.08` 侧的链接与散文里取的**（它自己声明了这一点），**本页没读 `Special_test_suites` 那篇**——所以「`bin_disconnect` 到底调不调 `DISCONNECT()`」**本页答不了**。
- [[dc-test-programming]] / [[special-test-suites]] / [[dps-power-flags-get-functions]] / [[dpspins-resources]] / [[utility-power-supplies]] — 这几页在 `extract/dangling.csv`（**2026-09-20 的读数**）里写着 `disconnect` 这个名字（该页记录本名字 **12 处引用、跨 8 个 stage**）。**本页没有读它们**，所以「它们各自在什么语境下提本页」**本页一个字没有**。（那张单每次重刷都会变，引它要标清是哪一刻。）
- **入边（`extract/edges.jsonl`，2026-09-17 的快照）**：链到那篇 raw DISCONNECT（`02.07.04.01.41`）的边 **18 条 / 13 篇**，**全部 `resolved`**（17 条 `inline` + 1 条 `toc`），**0 条落在代码跨度里**。其中有两篇是成章的：
  - `03.04_How_to_do_disconnect/03.04.01.01_Comparing_the_disconnect_methods`（2 条）与 `03.04.01.02_Standard_disconnect_sequence`（1 条）——**一整章讲「怎么做 disconnect」，正是本页缺的那一块**；
  - `02.07.04.01.42_DISCONNECT_EX`（2 条）、`02.08.04.32.01.02.01.02_Special_test_suites`（1 条）、`02.07.03.02_DC_Test_Programming`（1 条）、`02.07.04.01.231.07_SMC_CLEANUP`（1 条）、`02.12.06.10_MTP_CONTINUITY_TASK` 与它的 `.execute`（3 + 2 条）、`02.05.05.02.03.01_UHC4T_power_modes`（1 条）、`02.06.07.01.08.04.03.03.01_How_to_use_Fast_Sync`（1 条）。
  **这些文档本页一篇没读**，只用了计数与文件名。
- **只写反引号、不写链接的名字**：`SmartRDI: Digital channel relay control`（`02.07.13.14`）、`PPMU_RELAY`（`02.07.04.01.158`）、`DISCONNECT_EX`（`02.07.04.01.42`）、`global connect state`、`the "connect" state`、`each site` ——前两个是原文点名的两个「手工切 relay」的例子，**都不在 `extract/prose-allowlist.txt` 里**，按 §9.1 一律反引号；**本页没读那两篇**。

## 版本

本页的出处文档**有** `## Functional changes` 段，**只有一条**：

- `Introduced before SmarTest 6.3.2`

**但它是这一篇（CONNECT）的**：**本页的出处文档没有一条版本记录提到 `DISCONNECT()`**。

- 那一条是**哨兵值，不是「6.3.2 的变更」**（`schema.md` §11.2②）：`Introduced before` 的意思是「**在本文档集覆盖范围开始之前就已经有了**」——**照字面读会读成「6.3.2 新增了 CONNECT」，那是错的**。
- **DISCONNECT 是哪个版本引入的：语料未写**（本页不推测）。
- 对照页：[[smartest-6.3.2]]（**版本页，不是本页建的**）。

**本页那三句引文（那条 `Note`）也没有版本归属**：语料未写它是哪个版本进来的。

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.md`
  （TDC `28746.htm`，2,298 字节 / 54 行）。**这一篇与 [[connect]] 是同一篇。**
- **本页「语法 / 参数」节逐字取自这一篇**（447 字符，节首没有「取自子主题」后缀），
  节里是 **`CONNECT();`** 的 `## Syntax` 与 `## Example`。**这一节不许手改**（§4 / `PROSE-SPEC.md`），
  **所以它与 [[connect]] 那页的语法节逐字相同**——**它是 CONNECT 那一半**，
  **本页没有改写它、也没有假装它是 `DISCONNECT()` 的**（这句话在上面「是什么」里再强调过一次）。

### 本页读的图：**0 张，因为这一篇一张图都没有**

**实测该篇对 `raw/` 的图片引用 0 处**（`grep -c '!\['` 零命中）。
**这不是「图够不着」，是这一篇本来就不带图**——所以本页**没有任何来自图的结论**，
也没有任何一处需要标「④ 图证」。**本条与 [[connect]] 那页一致**（它读的也是这一篇）。

### 本页没做的

- **`02.07.04.01.41_DISCONNECT.md` 没读——这是本页最大的缺口。**「断开时做什么、
  有没有参数与返回值、定义在哪个头文件、错误行为」**本页一个字没有**；
  本页对 DISCONNECT 的**全部**陈述都只来自 CONNECT 那一篇里点名 `DISCONNECT()` 的那三句。
- **`## Related information` 里另外三篇没读**：`FOR_EACH_SITE_BEGIN`（`.70`）、
  `FOR_EACH_SITE_END`（`.72`）、`Connect`（`02.07.05.04.01`）。**[[connect]] 那页同样没读它们。**
- **入边那 13 篇一篇没读**（`DISCONNECT_EX`、`03.04_How_to_do_disconnect` 那一章的两篇、
  `Special_test_suites`、`DC_Test_Programming`、`SMC_CLEANUP`、`UHC4T_power_modes`、
  `MTP_CONTINUITY_TASK` 两篇、`How_to_use_Fast_Sync`、`APIs_in_alphabetical_order`、`index.md`）
  ——**本页只做了边检索（`extract/edges.jsonl`）与字符串检索，没有读正文**。
- **`dc-test-programming` 那两条时机没读**：[[connect]] 那页转述过它，
  **本页只指路、不复述**（§5：本页正文只写本页读过的那几篇）。
- **没有实跑。** 没有写过调 `DISCONNECT()` 的 test method、没有在机上手工切过 relay、
  没有见过那条 `see no action to perform` 真的发生。**`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[testmethod]] 那页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改；**本页与 [[connect]] 读的是同一篇，所以这几处那页也有**）

**① 一处缺空格：`state.Note`。** 原文那条列表项与紧跟着的 `Note` 粘在同一行：

> 「Sets the sequencer to break/on state.Note For multi-site testing, the CONNECT API must be used in the first-invocation block except the "each site" loop block.」

**`state.` 与 `Note` 之间没有空格。** 本页正文没有引这一句（它是 CONNECT 那一半的内容），**照实记在这里**。

**② 一处缺冠词：`Connect item`。**

> 「This API works the same as Connect item of the main menu, and performs the following sequences:」

**`Connect item` 前面缺一个 `the`**（读作 `the Connect item` 才通）。**本页照实记，一处没动。**

**③ 第二条 `Note` 在 raw 里行首带一个空格**（` Note Do not mix the global …`）——
**本页上面对那三句的引文按 §11.1① 折叠空白，字符一个没动**；那一格在原文里是缩进的 `Note` 块。

**④ 本篇的对错要看大小写**：原文写的是 `the "connect" state`（**小写、引号内**），
而 `CONNECT` / `DISCONNECT` 是大写的 API 名——**两者不是同一个东西**，
本页照原样引，**没有把它们统一成一种写法**。

**⑤ 本页这一篇没有编码坏字（§11.2① 那一族）**：用 `[一-鿿]` 实测零命中；
**也没有 §11.2⑤ 那个整词替换**（`DC/DC power units` 实测 0 命中）。
**这不是「没找到」，是查过、结果为零**——**所以本页正文里那些标识符（`CONNECT()` / `DISCONNECT()` /
`SmartRDI: Digital channel relay control` / `PPMU_RELAY`）都是从正文逐字读到的**，不是从坏字里、也不是从图上推的。

`verified: doc-only`
