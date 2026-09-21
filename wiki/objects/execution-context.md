---
type: object
title: Using execution contexts
layer: L2
stage: run
tags: [execution-context, multiport, parallel, port-subset, sqec, sqst-run, dc-scale, restrictions]
related: [sqst, sequencer, primary-status, sequencer-status, dc-scale-xps256-card, protocol-editor, smartest-7.2.0]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Using execution contexts

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,709 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

For a test method example, see the description of `SEQUENCER_CONTEXT`（raw: `../02.07_Test_Method_Reference/02.07.04.01.201_SEQUENCER_CONTEXT.md`）.

The following firmware example first displays the current start label, then shows its definition and that of another multi-port burst, then defines two execution contexts each of which is related to one of the two multi-port bursts, and finally executes these two contexts, changing the start label after starting the first context:

```
> SQSL?
< SQSL "mu_burst1"
> SQLB? "mu_burst1",MPBU,(@@)
< SQLB "mu_burst1",MPBU,6,7,,(PA)
< SQLB "mu_burst1",MPBU,6,7,,(PB)
< SQLB "mu_burst1",MPBU,10,11,,(PC)
< SQLB "mu_burst1",MPBU,4,5,,(PD)
> SQLB? "mu_burst2",MPBU,(@@)
< SQLB "mu_burst2",MPBU,3,4,,(PX)
< SQLB "mu_burst2",MPBU,8,9,,(PY)
> SQEC "c1",(PA,PD)
> SQEC "c2",(PY)
> SQST RUN,"c1"
> SQSL "mu_burst2"
> SQST RUN,"c2"
```

If `c1` has not yet been finished when `c2` is started, `c1` and `c2` will now run in parallel, provided that the ports `PA`, `PD`, and `PY` are disjunct, and at least one of the two contexts contains only Smart Scale channels.

Note also the following points in this example:

- The primary timing has not been changed between the start of `c1` and `c2`. If it had, then most probably the master clock period would have been recalculated, and this would have stopped `c1`.
- The first context is started with SQST RUN, not FTST?. This is required for parallel execution; using FTST? would block the firmware interface until execution of `c1` is finished and FTST? has returned its global PASS/FAIL result.
- If both contexts contain DC Scale channels, `c2` will not be started, and an error message will be issued. `c1` will continue to run.

<!-- 语法节 end -->

## 是什么

**execution context（执行上下文）= 一个名字 + 一份端口清单。**原文第一句是全部定义：

> 「Execution contexts allow you to run subsets of one or even more than one multiport burst
> independently and in parallel. Such an execution context consists of a port list that is
> associated with a name. In order to activate it, you must specify the name when you start
> the test. Generally, the ports of the context must be a subset of the ports in the current
> start label.」

**四个要素，缺一个都不成立**：

| 要素 | 原文 |
|---|---|
| **它是什么** | **a port list that is associated with a name** |
| **干什么用** | **run subsets of one or even more than one multiport burst independently and in parallel** |
| **怎么激活** | **指定它的名字**（`you must specify the name when you start the test`） |
| **前提** | **它的端口一般是当前 start label 端口的子集** |

> **「一个或多个多端口 burst 的子集」这句话是本页最要紧的一点**：
> **context 切的是**端口**，不是时隙**——**它把「哪些 port 参与」从 start label 里摘出来，
> 于是同一个 label 下可以有几拨端口各跑各的。**

### 它和「不完整多端口 burst」的分工（原文专门比了一次）

原文给了另一条路，并说清了该用哪个：

> 「Another option to execute only a proper subset of the ports in a multiport setup is to define
> an incomplete multiport burst (see Incomplete multi-port setups). Execution contexts, however,
> are more flexible, because you do not have to create a new multi-port burst for every port
> subset. But their main advantage is that they allow you to execute different sequencer tasks
> in parallel, which is not possible with an incomplete multi-port burst.」

| 做法 | 灵活性 | 能不能**并行跑不同的 sequencer task** |
|---|---|---|
| **不完整多端口 burst** | **每个端口子集都要建一个新的 burst** | **不能** |
| **execution context** | **不用为每个子集建 burst** | **能**——原文：`their main advantage` |

**而且两者不互斥**（原文 Note）：

> 「Incomplete multi-port bursts and execution contexts do not exclude each other. You can also
> define and run an execution context for a port subset of an incomplete multi-port burst.」

### 并行的场景长什么样（原文的叙述版）

> 「Thus you can, for example, first select a multi-port burst `mu_burst1` as the start label and
> start an execution context `c1` with a subset of the ports in `mu_burst1`, then change the start
> label to the multi-burst `mu_burst2` and start an execution context `c2` referring to `mu_burst2`.
> If `c1` is still running when `c2` is started (and all boundary conditions are satisfied), both
> contexts will then run in parallel.」

**关键在中间那一步：**先起 `c1`，**不等它跑完就换 start label，再起 `c2`**——
**两个 context 跑的是**不同 label** 的端口子集，同时跑。**

> **这条路径的存在意味着：start label 是「可以中途换的」**，
> 而先起的那个 context **不受影响**——**只要不碰下面那五条限制。**

### 五条限制（原文 `## Restrictions` 一节，**这一节是本页的实操核心**）

> 「The usage of execution contexts is subject to several restrictions. This holds in particular
> for systems that are not pure Smart Scale systems, but contain also DC Scale channels.」

**顺序照原文，一条不改：**

| # | 条件 → 结果 |
|---|---|
| **1** | **端口必须是当前 start label 的子集** → 否则**不能跑**（`An execution context can only be run if all its ports are included in the current start label.`） |
| **2** | **两个 context 有共用的 channel** → **不能并行**；报错、**B 不启动**、**A 继续跑** |
| **3** | **先起的那个是用 `SQST RUN`（或 `START_TEST()`）起的** → **才能并行**；**用 `FTST()`（或 `FUNCTIONAL_TEST()` / `EXECUTE_TEST()`）起 → 第二个要等第一个返回 global PASS/FAIL 之后才启动** |
| **4** | **两个 context 之间有 primary timing 变更且触发 master clock 重算** → **重算会停掉所有 user defined sequencer task**，**所以要避开** |
| **5** | **两个 context 都含 DC Scale channel 的 port** → **不能并行**；报错、**B 不启动**、**A 继续跑** |

**三条补注（原文分别写在条目下面）：**

**① 定 1 的例外是协议端口**（原文紧接着 1 写）：

> 「Note that protocol ports are an exception to this. Protocol ports are not allowed to occur in
> the start label. This also holds if the protocol port is contained in a context.」

**即：协议端口**不允许**出现在 start label 里——**哪怕它只是出现在 context 里也不行**。
**协议端口走另一条路**（原文指向 `Independent protocol test`）。

**② 2 与 5 的失败方式完全一样**（原文各写了一遍，措辞几乎相同）：

> 「If an execution context A is running and you try to start another execution context B that
> shares a channel with A, an error message to this effect will be issued, and B will not be
> started. A will continue to run.」

> 「If an execution context A that contains a DC Scale channel is running, and you try to start
> another context B for which this also holds, then an error message to this effect will be
> issued, and B will not be started. A will continue to run.」

**记法：限制 2 和 5 都**不打断**已经在跑的那个。报错的是新的，停的是新的，老的继续跑。**

**③ 定 3 的理由在示例的注释里给了**（见「典型用法」最后一条）：
**用 `FTST?` 会阻塞固件接口**。

### 6 条相关命令 + 3 个相关 API

原文 `## Related firmware commands` 一节（**逐条都是原文**）：

| 命令 | 干什么 |
|---|---|
| **`SQEC`** | **`An execution context is defined with the SQEC command`** |
| **`SQRC`** | **`Execution contexts are deleted with the SQRC command.`** |
| **`FTST?`** / **`SQST RUN`** | **启动靠「把名字加在跑测试的那个命令/查询上」**——`started by adding its name to the command/query that executes the test (for example FTST? or SQST RUN)` |
| **`SQLC?`** | **`retrieves this information per port`**——问**上一次**起了哪些 context |
| **`SQSC?`** | **`returns it over all ports`**——同一件事，**跨全部端口问** |

> **注意 `SQLC?` / `SQSC?` 问的是「最后启动的那些 context」**（原文：
> `There are two queries that inform about the execution contexts that were started last.`）——
> **不是当前正在跑的**。这两个问题在原文里是不同的词，本页照原文写。

**Test Method API 侧三个**（原文 `## Related Test Method APIs` 一节）：

| API | 原文 |
|---|---|
| **`SEQUENCER_CONTEXT`** | 三个里唯一给了示例的一篇（`For a test method example, see the description of SEQUENCER_CONTEXT.`） |
| **`SEQUENCER_CONTEXT_ITEM`** | —（原文只列名） |
| **`INDEPENDENT_TEST`** | **带注解 `(Protocol Aware)`** |

## 典型用法

**原文那段固件示例是本页的全部操作依据**，它一次性演示了「定义 → 起 → 换 label → 再起」。
逐步拆开（**命令行是原文，括号里是它在干什么**）：

```
> SQSL?
< SQSL "mu_burst1"                      ← 问当前 start label，是 mu_burst1
> SQLB? "mu_burst1",MPBU,(@@)
< SQLB "mu_burst1",MPBU,6,7,,(PA)       ← mu_burst1 定义在 PA/PB/PC/PD 四个 port 上
< SQLB "mu_burst1",MPBU,6,7,,(PB)
< SQLB "mu_burst1",MPBU,10,11,,(PC)
< SQLB "mu_burst1",MPBU,4,5,,(PD)
> SQLB? "mu_burst2",MPBU,(@@)
< SQLB "mu_burst2",MPBU,3,4,,(PX)       ← mu_burst2 定义在 PX/PY 上
< SQLB "mu_burst2",MPBU,8,9,,(PY)
> SQEC "c1",(PA,PD)                     ← 定义 context c1 = {PA, PD}（mu_burst1 的子集）
> SQEC "c2",(PY)                        ← 定义 context c2 = {PY}（mu_burst2 的子集）
> SQST RUN,"c1"                         ← 起 c1（用 SQST RUN，不用 FTST?）
> SQSL "mu_burst2"                      ← c1 还没跑完就换 start label
> SQST RUN,"c2"                         ← 再起 c2
```

**并行的成立条件，原文一句话给全**：

> 「If `c1` has not yet been finished when `c2` is started, `c1` and `c2` will now run in parallel,
> provided that the ports `PA`, `PD`, and `PY` are disjunct, and at least one of the two contexts
> contains only Smart Scale channels.」

**三件事同时成立才并行**：① `c1` 还没跑完；② **`PA` / `PD` / `PY` 互不相交**（对应限制 2）；
③ **两个 context 里至少有一个只含 Smart Scale 通道**（对应限制 5 的反面）。

**原文在这段示例后另给了三个注意点**（**这是本页最值钱的三条经验**）：

| # | 原文 | 读法 |
|---|---|---|
| **1** | `The primary timing has not been changed between the start of c1 and c2. If it had, then most probably the master clock period would have been recalculated, and this would have stopped c1.` | **示例里两次 `SQST RUN` 之间**没碰 primary timing**——**碰了大概率会重算 master clock，把 `c1` 停掉**（限制 4 的实例） |
| **2** | `The first context is started with SQST RUN, not FTST?. This is required for parallel execution; using FTST? would block the firmware interface until execution of c1 is finished and FTST? has returned its global PASS/FAIL result.` | **第一个 context 必须用 `SQST RUN` 起**——**`FTST?` 会把固件接口**堵住**直到它返回**（限制 3 的理由） |
| **3** | `If both contexts contain DC Scale channels, c2 will not be started, and an error message will be issued. c1 will continue to run.` | **两个都含 DC Scale 通道 → `c2` 起不来，报错，`c1` 不受影响**（限制 5 的实例） |

**所以最小可用套路（由上面拼出）**：

**① 建多端口 burst**（或用一个不完整的）→ **② `SQEC` 定义 context，端口取子集** →
**③ 用 `SQST RUN,"名字"` 起（**不要用 `FTST?`**）** →
**④ 不等它完，换 start label，再 `SQST RUN` 起第二个** →
**⑤ 期间**不要动 primary timing**（会触发 master clock 重算）**→
**⑥ 用完 `SQRC` 删掉 context**。

**要排查「为什么没并行」时的检查顺序**：**端口是不是相交**（限制 2）→
**是不是都用 `SQST RUN` 起的**（限制 3）→ **是不是都含 DC Scale 通道**（限制 5）→
**端口是不是当前 start label 的子集**（限制 1）→ **中间有没有改 primary timing**（限制 4）。

## 和谁有关

**上游 / 被切的那个东西**：

- [[primary-status]] — 示例注释第 1 条说的 `The primary timing has not been changed` 与
  限制 4 的 `changes of the primary timing involving such a recalculation`，
  **指的就是那套 primary timing 定义**。
  **本页的用法里，改 primary timing 是一个**要避开的动作**——因为它会重算 master clock，
  而重算会停掉所有 user defined sequencer task。**
- [[sequencer]] — **context 切出来的端口子集，跑的正是各自的 sequencer program**。
  **本页是运行侧「谁跟谁一起跑」，那页是程序侧「跑的是什么」。**

**firmware 侧的命令（本页的启动方式就是它）**：

- [[sqst]] — **`SQST RUN` 是本页并行执行的**必要条件**（限制 3）**，
  也是示例里起 `c1` / `c2` 的那条命令。
  **`SQST` 这一篇本页没读**——**它的 `RUN` 参数细节本页只有原文这几句转述。**

**同一条线上的另一页（**本页没读**，只作指向，不作断言）**：

- [[sequencer-status]] — 同为 sequencer 运行控制这一条线（`stage: run` 与它同域）。
  **本页没读它，所以两页之间**具体**什么关系本页不判。**
- [[cct-multiport-sequencer-synchronizer-api]]（**在 allowlist 里**）—— 多端口同步这一侧。
  **本页两次碰到「端口 / 同步」的边（限制 2 的 channel、限制 4 的 master clock），
  但同步本身怎么做的，本页一个字都没有。**
- [[smartest-7.2.0]] — **本页的引入版本**（见「版本」）。

**被限制 5 点名的那张卡 / 那类通道**：

- [[dc-scale-xps256-card]] / [[dc-scale-uhc4t-card]] — **限制 5 与示例注意点 3 说的
  `DC Scale channel` 就是这类卡提供的通道**。
  **原文对它的要求只有一条：两个 context 不能都含它。**
  **这两张卡本页都没读。**

**协议端口那条例外牵出的**：

- [[protocol-editor]] — 原文说 **`Protocol ports are not allowed to occur in the start label`**，
  并把这个例外指向 `Independent protocol test`（**那篇本页没读**）。
  **协议侧本身是什么样，本页没有；本页只有「它被排除在外」这一条。**

**被本页点名、本页没读的（均未建，不链）**：
`Incomplete multi-port setups`、`Independent protocol test`、`SEQUENCER_CONTEXT`、
`SEQUENCER_CONTEXT_ITEM`、`INDEPENDENT_TEST`、`START_TEST()`、`FUNCTIONAL_TEST()`、
`EXECUTE_TEST()`、`SQEC` / `SQRC` / `SQSL` / `SQLB` / `SQLC?` / `SQSC?` / `MPBU` / `FTST?`。

> **本页的「和谁有关」全部来自这一篇原文里点到的名字。**

## 版本

本文档有 `## Functional changes` 段，**全部内容一条**：

- **`Introduced in SmarTest 7.2.0`**

> **这一条和本 wiki 里常见的那个哨兵值**不同形**——
> 写成的是 `Introduced in`，**不是** `Introduced before`。**
> 按 §11.2 ② 的描述，哨兵值的措辞一定是 `before`（意思是「本文档集覆盖之前就有了」）。
> **所以 `Introduced in SmarTest 7.2.0` 是一条**真正的**版本记录：
> **execution context 是 SmarTest 7.2.0 引入的。**
>
> **对照页**：[[smartest-7.2.0]]（**未建**）—— 该版覆盖范围本页没读。
>
> **⚠️ 一个本页**不判**的问题**：本页的示例用到了 `SQEC` / `SQST RUN` / `SQLC?` / `SQSC?`
> 四条命令，而 `## Functional changes` 只记了 `7.2.0` 这一条，**没有单独记某条命令是后来加的**。
> **所以「这四条命令是不是 7.2.0 一起进来的」本文档没说，本页不推断。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`
（raw 的 `source_topic: "135848.htm"`）。

**本页没做的**：

- **全部相关命令与 API 一篇都没读**：`SQEC` / `SQRC` / `SQST RUN` / `FTST?` / `SQSL` /
  `SQLB` / `SQLC?` / `SQSC?` / `MPBU` / `SEQUENCER_CONTEXT` / `SEQUENCER_CONTEXT_ITEM` /
  `INDEPENDENT_TEST`。
  **所以：这些命令的完整参数表、`MPBU` 是什么样的 burst、`SEQUENCER_CONTEXT` 的 test method
  写法，本页一个字都没有**——**本页只有原文在讲 context 时顺带写下的那几句。**
  **`SEQUENCER_CONTEXT` 那篇里有一个 test method 示例（原文两次指过去），本页也没看。**
- **`Incomplete multi-port setups` 没读**——**所以「不完整多端口 burst」具体怎么建、
  它和 context 在硬件上差在哪里，本页只有原文那句对比性的转述。**
- **`Independent protocol test` 没读**——**协议端口为什么不能出现在 start label 里，
  本页不知道，只知道这条禁令存在。**
- **`SQST`（[[sqst]]）没读**——**`SQST RUN` 的 `RUN` 之外还有哪些参数、`SQST` 有哪些状态，
  本页没有。**
- **`SEQUENCER_STATUS`（[[sequencer-status]]）没读**——**所以「context 与 sequencer 运行状态
  怎么互相影响」本页不判**（本页只有限制 4 这一条：master clock 重算会停掉
  `all user defined sequencer tasks`）。
- **`Smart Scale` / `DC Scale` 两类通道本身本页没读任何页**——
  **原文的限制 5 与示例注意点 3 都靠这个区分，而这个区分的机制本页没有。**
- **`master clock period` 怎么算、什么时候会重算，本文档没写。**
  原文只说 `most probably the master clock period would have been recalculated`——
  **连原文自己用的都是 `most probably`。本页照实保留这个不确定度，不写成确定因果。**
- **没有任何图。** 本篇没有图片引用。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 限制 3 里多一个介词。** 逐字：
> `Two execution contexts can run in parallel only if the context that is started first is
> executed in with SQST RUN (or the test method API START_TEST()).`
> —— **`is executed in with` 应为 `is executed with`。**
>
> **② 同一条命令在一篇里两种写法。** 限制 3 用的是 `FTST()`（带括号），
> `## Related firmware commands` 与示例注释用的是 `FTST?`（带问号）。逐字对照：
> `If it is started with FTST() (or one of the test method APIs FUNCTIONAL_TEST() or EXECUTE_TEST())`
> / `(for example FTST? or SQST RUN)` / `This is required for parallel execution; using FTST? would …`
> —— **`FTST()` 与 `FTST?` 指同一条命令，本页照原样各引各的。**
>
> **③ `multiport` 与 `multi-port` 两种拼法混用，且出现过第三种拼法。** 逐字：
> 第一段 `run subsets of one or even more than one multiport burst independently`（**无连字符**），
> 同一段稍后 `you do not have to create a new multi-port burst for every port subset`（**有连字符**）；
> 再往后 `then change the start label to the multi-burst mu_burst2`——
> **`multi-burst` 是第三种写法，按上下文应为 `multi-port burst`。**
>
> **④ 一处 `Note` 标记粘在正文上，没有分隔。** 逐字：
> ` Note Incomplete multi-port bursts and execution contexts do not exclude each other.`
> —— 行首一个空格 + `Note` 直接接 `Incomplete`。**同一个毛病在 [[sequencer-status]] 那篇里
> 也有（`Note In an AC test, …`），是这份语料的一个通例，不是孤例。**
>
> **⑤ 语法节里那两条「`<` 开头的行」是命令的回复**，原文用 `> ` 表示发命令、
> `< ` 表示返回。**本页在「典型用法」里引这段时，把 `←` 起的注解**加在了行尾**——
> **这些注解是本页写的，原文没有**；命令行本身逐字未改。
>
> **⑥ 语法节的 `### Example` 标题下第一句是 `For a test method example, see the description of
> SEQUENCER_CONTEXT`**，而这一节的正文其实是**固件**示例——
> **即这一节叫 `Example`，但里面**既有**指向 test method 的索引，又有固件示例**。
> 抽取器把这个标题下的全部内容收了进来，**所以「语法 / 参数」节里同时有两种东西。**
> **本页不改那一节，只在此说明。**

`verified: doc-only`
