---
type: object
title: CONNECT
layer: L2
stage: testmethod
tags: [connect, disconnect, l2, test-method-api, test-control, relay, dut-power, multi-site, on-first-invocation, pmu]
related: [testmethod, mapping-testmethod, disconnect, dc-test-programming, on-first-invocation-begin, on-first-invocation-end, for-each-site-begin, for-each-site-end, flush, primary-status, level-spec, testflow, run, test-suite]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# CONNECT

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

**`CONNECT()` 是 test method 里把测试机资源接到 DUT 上的那一条 API。** 原文第一句：

> 「The CONNECT API connects the tester resources to the DUT and sets the tester to the "connect" state unless they are already connected.」

**它是幂等的**：

> 「If the test resources are already connected, this API performs no action.」

**它等于主菜单里的 `Connect` 项，做的是下面三件事（原文列死了）**：

> 「This API works the same as Connect item of the main menu, and performs the following sequences:」

> 「Connects the AC relays to the DUT pins」

> 「Powers up the supplies to the DUT」

> 「Sets the sequencer to break/on state.」

（第三句在 raw 里与紧跟着的 `Note` 粘在一起——`state.Note`，见「出处」⚠️①。
**本页引到 `state.` 为止，没有用省略号接句子。**）

**三件事合起来看，`CONNECT()` 管的是「通路 + 上电 + 时序器状态」这三样**——
它**不下发任何设置值**（原文一条都没有）。

**定义位置**原文写明：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/TestControl.h.」

**没有参数、没有返回值**（见「语法 / 参数」节），所以调用只有一种写法：`CONNECT();`。

### 两条 `Note`，是这一页真正要记住的东西

**① 多 site 时位置受限：只能写在 first-invocation 块里，不能写进 each-site 循环块。**

> 「Note For multi-site testing, the CONNECT API must be used in the first-invocation block except the "each site" loop block. The CONNECT API cannot work correctly in the "each site" loop block.」

| 你把它写在哪 | 结果 |
|---|---|
| **first-invocation 块**（[[on-first-invocation-begin]] / [[on-first-invocation-end]]） | 正确 |
| **`each site` 循环块**（[[for-each-site-begin]] / [[for-each-site-end]]） | **原文：`cannot work correctly`** |

**原文没有说会报什么错、也没说为什么**——只说了不工作。**本页不替它补原因。**
（两对作用域块本身**本页没读**，见「出处」。）

**② 别把全局的 `CONNECT()` / `DISCONNECT()` 和单独切 relay 混着用。**

> 「Note Do not mix the global CONNECT()/DISCONNECT() with individual relay switching.」

> 「Manually switching relays (see for example SmartRDI: Digital channel relay control and PPMU_RELAY) will not change the global connect state, and so CONNECT()/DISCONNECT() will see no action to perform.」

> 「The relays which initially have been switched manually, must again be individually and manually switched to change their state.」

**把这三句连起来读，就是「我手动切过 relay，为什么 `CONNECT()` 什么都不做」的答案**：

| 你此前做过什么 | 再调 `CONNECT()` |
|---|---|
| 什么都没动 | 正常连接（原文第一句） |
| **手工切过 relay** | **全局 connect state 没变 → `see no action to perform`**——**它以为已经连好了** |
| 想把手工切过的 relay 改回去 | **必须再手工切**（`must again be individually and manually switched`） |

（**这一格是本页把三句并起来的（推断）**，依据是原文自己写出的因果
`will not change the global connect state, and so CONNECT()/DISCONNECT() will see no action to perform`
与最后那句 `must again be individually and manually switched`——
**三条引文都是原文，那个「表格化的合并」是推断。**）

**这一条的实操含义**：**手工切和全局 connect state 是两套账，互不知道。**
`CONNECT()` 查的是全局那一套，**它不会去读你手工切过的 relay**。
这里的动词是 `see no action to perform`——**不是「拒绝执行」，是「看着没事可做」。**

## 典型用法

原文 `## Example` 是「DC 测量之前先 CONNECT」这个最小场景：

```
CONNECT();
...
...
PMU_IFVM("PIN1,PIN2").iForce(100 uA).settling(5 ms);

PMU_IFVM("PIN1,PIN2").limits("limit1").execute();
...
...
```

> 「To use the PMU_IFVM API, you must set the tester to the CONNECT status. This example connects the tester resources to the DUT with the CONNECT API before DC measurement.」

**那句是「必须」**（`you must set the tester to the CONNECT status`）——
**`PMU_IFVM` 这一类 DC 测量 API 的前置就是它。**
（`PMU_IFVM` 不在 allowlist 里、**未建**，**本页没读它**——Example 里那两行是它的调用，
**它的参数含义本页不知道**。）

**步骤**：原文**没有** `## Procedure`，也**没有** `## Before you begin`。
动作就是**在测量之前调一次 `CONNECT();`**，**多 site 时位置受限**（见上面①）。
Example 里那两串 `...` 是**原文自己写的省略号**（表示中间还有别的代码），
**不是本页加的**（§11.1）。

**与 [[disconnect]] 是一对，但两边的「时机」不在本页的出处里**——
[[dc-test-programming]] 那页写的是：**一般 DC 测试「测试前 `CONNECT`」**，
而**continuity test 要先 `DISCONNECT`**；它把本页与 [[disconnect]] 记成「**前置和收尾**」。
**本页只转述它这一句，没有读它引的 `02.07.03.02`**——**所以「什么时候必须断开」本页答不了。**

## 和谁有关

- [[testmethod]] / [[mapping-testmethod]] — **本页 `stage: testmethod` 的理由**。[[mapping-testmethod]] 主表第 5 行「给 DUT 上电 / 断电」是**唯一**挂本页的那一行，五格是：**GUI `?` / 文件 `—` / L1 `?` / L2 = [[connect]] 与 [[disconnect]] / L3 `?`**。
- **本页没有 L1 对口物，这是语料事实、不是本页没查。** [[mapping-testmethod]] 把那一行的 L1 格填成 `?` 而不是 `—`，理由它自己写了：固件层**确实有东西**（routing / relay 一类命令），**但语料没说 `CONNECT()` 对应哪一条**；它还写明**那四张图里没有一张出现固件命令名**，所以那一格**看完图仍是 `?`**。**本页不替它猜一条命令**（§2.5：不许猜）。
- [[disconnect]]（**未建**）— **本页的对手方**。原文 `Related information` 第一条就是它。**它在 `extract/dangling.csv` 里（12 处引用），属「会存在的页」**，本页按 §9.1 链它。**它的语法、参数、返回值本页一个字没有**——**断开怎么断、断开后怎么恢复，要它自己的页来写。**
  （那 12 处是 **2026-09-20** 的读数；**那张单每次重刷都会变**，**引它要标清是哪一刻**。）
- `Connect`（**未建**，测试方法文档 `02.07.05.04.01`）— 原文指名：`See the test control method Connect for more information about the CONNECT.`。**「CONNECT 的更多信息」在那篇里，本页没读。**
- [[on-first-invocation-begin]] / [[on-first-invocation-end]]（**均未建**）— **多 site 时 `CONNECT()` 该待的地方**（原文写的是 `the first-invocation block`）。**本页的出处文档没有链这两篇**（`Related information` 里是 `FOR_EACH_SITE_*`），**「first-invocation block 就是这两个 API 之间」是本页从 API 名对上的（推断）**。
- [[for-each-site-begin]] / [[for-each-site-end]]（**均未建**）— 原文把这两个作用域块与本页并排列在 `Related information` 里，**原因就是上面那条「不能写进 each site 循环块」**。
- `SmartRDI: Digital channel relay control`（`02.07.13.14`）/ `PPMU_RELAY`（`02.07.04.01.158`）（**均未建**）— **「手工切 relay」的两个例子**，原文点名。**本页没读**——**手工切到底怎么切，本页答不了。**
- [[dc-test-programming]] — **本页在 DC 测试流程里的位置**（上面「典型用法」末段那两条时机就是从它转述的）。
- [[flush]] — **口径与本页一致的那一页**：[[flush]] 在自己的「和谁有关」里写着，它的出处文档讲主时钟时**点名了 `sqst` 与本页**。**本页的出处文档一个字没提 FLUSH**，所以**这条关系是单向的**，本页只记 [[flush]] 那侧说过。
- [[primary-status]] / [[level-spec]] — **不属本页**：改主设置、改 spec 值是它们的事；本页只把**已经设好的东西**接到 DUT 上（**推断**，依据是原文那三件事里没有一件是「下发设置」）。
- [[testflow]] / [[run]] / [[test-suite]] — `CONNECT()` 写在 test method 里、由 testflow 里的 test suite 调用；**原文没有一句链它们**，**本页也不替它写流程**（§2.2：object 页不含流程叙述）。
- **只写反引号、不写链接的名字**：`Connect`（主菜单项与那篇测试方法文档）、`PMU_IFVM`、`SmartRDI: Digital channel relay control`、`PPMU_RELAY`、`each site`、`the "connect" state`、`break/on`——**它们都不在 `extract/prose-allowlist.txt` 里**，按 §9.1 一律反引号。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- `Introduced before SmarTest 6.3.2`

**这是哨兵值，不是「6.3.2 的变更」**（`schema.md` §11.2②）：`Introduced before` 的意思是
「**在本文档集覆盖范围开始之前就已经有了**」——**照字面读会生成一条「6.3.2 新增了 CONNECT」的假信息，而且格式齐整。**

**本篇没有任何其它版本条目**，所以本页那两条 `Note` 都没有版本归属：

| 本页的内容 | 语料给的版本 |
|---|---|
| 那三条连接动作 | **未写**（只有 `Introduced before SmarTest 6.3.2`） |
| 多 site 那条位置限制 | **未写** |
| relay 那条混用禁令 | **未写** |

**即：「多 site 那条限制是哪个版本加的」，语料未写。本页不推测。**

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.md`
  （TDC `28746.htm`，2,298 字节 / 54 行）。
- **本页「语法 / 参数」节的来源就是这一篇自己**（节首没有「取自子主题」后缀），
  节里那 447 字符就是原文的 `## Syntax` + `## Example` 两段。

### 本页读的图：**0 张，因为这一篇一张图都没有**

**实测该篇对 `raw/` 的图片引用 0 处**（`grep -o 'raw/[0-9]*\.\(png\|jpg\)'` 零命中）。
**这不是「图够不着」，是这一篇本来就不带图**——所以本页**没有任何来自图的结论**，
也没有任何一处需要标「④ 图证」。

**另有一件要分清的事**：[[mapping-testmethod]] 已经**为这一行看过四张图**，
结论是「四张图里既没有固件命令名、也没有 L3 的 API 名」，所以那一行的 L1 `?` 没被图填掉。
**本页引它这一句，没有自己去开那四张图**——**那四张图出自别的文档，不属本页的 `sources:`。**

### 本页没做的

- **`## Related information` 的四篇一篇没读**：`DISCONNECT`（`02.07.04.01.41`）、
  `FOR_EACH_SITE_BEGIN`（`.70`）、`FOR_EACH_SITE_END`（`.72`）、
  `Connect`（`02.07.05.04.01`）。**所以「怎么断开、断开后怎么恢复」本页一个字没有**；
  [[disconnect]] 那个 API 的签名、参数、返回值本页也一个字没有。
- **`PMU_IFVM`（`02.07.04.01.151`）没读**——Example 里那两行调用的参数含义本页不知道，
  本页只用到了原文那句「用它之前必须先到 CONNECT 状态」。
- **`SmartRDI: Digital channel relay control`（`02.07.13.14`）、
  `PPMU_RELAY`（`02.07.04.01.158`）没读**——**「手工切 relay」怎么切、切完什么现象，本页答不了**。
  本页对那条 `Note` 的解读**只用了本页读到的三句原文**。
- **`02.07.03.02`（CONNECT / DISCONNECT 的时机）没读**——「典型用法」末段那两条时机是
  **从 [[dc-test-programming]] 转述的**，**不是本页的出处**；**那页还指了别的文档，本页也没有跟过去。**
- **first-invocation / each-site 那四个作用域块一篇没读**——
  **「块怎么写、能不能嵌套」本页一个字没有**，本页只有原文那一句「该放在哪个块里」。
- **没有实跑。** 没有写过 test method、没有调过 `CONNECT()`、没有在机上手动切过 relay，
  也就没有见过那条 `see no action to perform` 真的发生。**`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[testmethod]] 那页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 一处缺空格：`state.Note`。** 原文那一条列表项与紧跟着的 `Note` 粘在同一行：

> 「Sets the sequencer to break/on state.Note For multi-site testing, the CONNECT API must be used in the first-invocation block except the "each site" loop block.」

**`state.` 与 `Note` 之间没有空格。本页正文把那一句截到 `state.` 为止引**——
**截取只发生在引文块尾部**（§11.1），**没有用省略号接句子**。

**② 一处缺冠词：`Connect item`。**

> 「This API works the same as Connect item of the main menu, and performs the following sequences:」

**`Connect item` 前面缺一个 `the`**（读作 `the Connect item` 才通）。
**本页正文引了这一句，一处没动。**

**③ 第二条 `Note` 在 raw 里行首带一个空格**（` Note Do not mix the global ...`）——
**本页引文按 §11.1① 折叠空白，字符一个没动**；那一格在原文里是缩进的 `Note` 块。

**④ 本篇的对错要看大小写**：原文写的是 `the "connect" state`（**小写引号内**），
而 `CONNECT` / `DISCONNECT` 是大写的 API 名——**两者不是同一个东西**，
本页照原样引，**没有把它们统一成一种写法**。

**⑤ 本页这一篇没有编码坏字（§11.2① 那一族）**：用 `[一-鿿]` 实测零命中；
**也没有 §11.2⑤ 那个整词替换**（`DC/DC power units` 实测 0 命中）。
**这不是「没找到」，是查过、结果为零**——**所以本页的 `CONNECT()` / `DISCONNECT()` /
`PMU_IFVM` 这些标识符，都是从正文逐字读到的，不是从图上、也不是从坏字里推的。**

`verified: doc-only`
