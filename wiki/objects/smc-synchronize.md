---
type: object
title: SMC_SYNCHRONIZE()
layer: L2
stage: testmethod
tags: [testmethod, l2, test-method-api, smartcalc, smc, thread-synchronization, timeout, datalog, binning, multisite, hidden-datalog]
related: [smartcalc, smartcalc-framework, hidden-upload, smc-background-process-locks-config, testmethod, test-method-class, for-each-site-begin, for-each-site-end, on-first-invocation-begin, on-first-invocation-end, mapping-results, smartest-6.5.3, smartest-7.1.3, smartest-7.2.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.43_SMC_SYNCHRONIZE.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# SMC_SYNCHRONIZE()

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,284 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.43_SMC_SYNCHRONIZE.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
Boolean SMC_SYNCHRONIZE(DOUBLE timeout = 0);
Boolean SMC_SYNCHRONIZE(DOUBLE timeout, Boolean forceErrorExitOnFail);
Boolean SMC_SYNCHRONIZE(INT *noOfSMCExecutedTests, DOUBLE timeout = 0);
Boolean SMC_SYNCHRONIZE(INT *noOfSMCExecutedTests, DOUBLE timeout, Boolean forceErrorExitOnFail);
```

This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/SMART_CALC2.h.

  Parameters

 | Parameter  | Description/Range |
 | timeout |

The time in seconds after which a thread should be canceled and SMC_SYNCHRONIZE() should not wait for its completion.

Resolution: 1 碌s

The accuracy of this parameter is influenced by the overhead time of the operating system.

The default value is 0.0 seconds which means that no timeout is set.

 |
 | noOfSMCExecutedTests  | References a pointer to store the number of `SMC_TEST()`（raw: `02.07.04.01.231.45_SMC_TEST.md`） statements which have been executed during this synchronize operation per site. Note

When using the class SMC_ARM_FOR_SITES() or SMC_ARM_OTHER_TS_FOR_SITES(), SMC_SYNCHRONIZE() does not not return a test count. As a result, noOfSMCExecutedTests is not incremented and does not count the number of calls to SMC_TEST().

 |
 | forceErrorExitOnFail |

Enables a forced exit on an error. If set to

-

true - it causes an exception in case a calculation routine had to be aborted.

-

false - it causes SMC_SYCHRONIZE() to return false in case a calculation routine had to be aborted.

   |  Return value

Returns false in case threads had to be terminated or an invocation error occurred, else true is returned.

If the noOfSMCExecutedTests parameter is used, the number of `SMC_TEST()`（raw: `02.07.04.01.231.45_SMC_TEST.md`） statements which have been executed during this synchronize operation per site will be stored in the integer variable referenced by the pointer.

### Example

Waits for all calculations to be finished within 100 ms. After the timeout of 100 ms all other still running calculation threads will be terminated!

```
SMC_SYNCHRONIZE(100 ms);
```

Waits for all calculations to be finished within 10 ms. After the timeout of 10 ms all other still running calculation threads will be terminated! In case a calculation had to terminated, SMC_SYNCRONIZE() throws an exception.

```
SMC_SYNCHRONIZE(10 ms, true);
```

<!-- 语法节 end -->

## 是什么

**`SMC_SYNCHRONIZE()` 是 SmartCalc（`SMC`）里「等线程、然后结算」的那一个函数。**
它自己不做测量、不做判断——它管的是**顺序**：先把后台线程等完，再让排队的东西落地。

原文第一段就是全部机制（三句连读）：

> 「Waits for the end of the execution of all threads which have been started using SMC_ARM(). After all threads have finished their upload and calculation task the queued SMC_TEST() statements will be executed to perform the data logging and binning.」

**这一句拆成三步，每一步都会影响你怎么写程序**：

| 步 | 原文的措辞 | 含义 |
|---|---|---|
| ① 等谁 | `all threads which have been started using SMC_ARM()` | **等的是 `SMC_ARM()` 起的那些线程**——不是「等测试跑完」，是「等线程结束」 |
| ② 等到什么程度 | `After all threads have finished their upload and calculation task` | 线程要**做完两件事**：`upload` 与 `calculation` |
| ③ 等完之后发生什么 | `the queued SMC_TEST() statements will be executed to perform the data logging and binning` | **`data logging` 与 `binning` 都发生在这一步** |

**第 ③ 步是本页最值钱的一句**：「`SMC_TEST()` 当场不写日志」的答案就在这儿——
**它排的那个队，是在 `SMC_SYNCHRONIZE()` 这一行被消费掉的**，
而且**是同一条语句同时把 `data logging` 与 `binning` 做掉**。
（`SMC_TEST()` 那一篇本页没读，见「出处」；本页只说得出本篇点名它的那两处。）

### 它必须 per site 调，而且必须在 `ON_FIRST_INVOCATION` 块外面

> 「SMC_SYNCRONIZE() has to be called per site and thus outside of an ON_FIRST_INVOCATION block.」

**这一句里有一个 `thus`，它把两个要求绑成了一条因果**：

| 要求 | 原因（原文的 `thus` 给的） |
|---|---|
| **per site 调**（每个 site 各调一次） | 它结算的是「本 site 的那批线程」 |
| **在 `ON_FIRST_INVOCATION` 块之外** | 因为那个块是「整个程序只跑一次」的——**放进去就做不到 per site** |

**`SMC_SYNCRONIZE()` 少了一个 `H`**（正确拼法是 `SMC_SYNCHRONIZE`）——
**本页照录，不替它改**（§11.2）。同一篇里还有第二种错拼 `SMC_SYCHRONIZE`（见「出处」⚠️②）。

### 一条例外：用了 hidden data logging，binning 就不在它这儿

> 「If Hidden data logging is used, binning is not handled in SMC_SYNCHRONIZE(), but in your SMC_backgroundProcessing() method. For details on binning rules, see Use of bins with multisite tests and Use of multibins.」

**条件 → 结果**：

| 情形 | binning 发生在哪 |
|---|---|
| 普通用法 | **在 `SMC_SYNCHRONIZE()` 里**（第 ③ 步那半句 `and binning`） |
| **用了 Hidden data logging** | **不在 `SMC_SYNCHRONIZE()`，而在你的 `SMC_backgroundProcessing()` 方法里** |

**所以「`SMC_SYNCHRONIZE()` = 分 bin 的地方」这句话是有条件的**，
**条件就是「没用 hidden data logging」**。原文把这条例外放在正文第二段（不是脚注、不是 Note）——
**它是一条会改你程序结构的位置信息**，不是细节。

### 四个参数：脚本已逐字抄在上面，这里只写「机制与后果」

**`timeout`（默认 `0.0` = 不设超时）**

> 「The time in seconds after which a thread should be canceled and SMC_SYNCHRONIZE() should not wait for its completion.」

> 「The default value is 0.0 seconds which means that no timeout is set.」

**注意这里的动作是 `canceled`**——超时之后**线程是被取消的**，不是「等不到就算了」。
参数表另外给了分辨率与误差来源：

> 「Resolution: 1 碌s」

> 「The accuracy of this parameter is influenced by the overhead time of the operating system.」

**`碌` 是坏字。** `extract/encoding-map.csv` 第 2 行写着 `碌,µ`——**它是 `µ`**，
所以这句读作「分辨率 1 µs」。**本页照录坏字，不替它改**（§11.2 ①）。

> ⚠️ **单位上有一处对不上，本页照实记**：参数表说 `The time in seconds`，
> 而 `## Example` 里两个示例传的是 `100 ms` / `10 ms`（见「典型用法」）。
> **`ms` 在这个 API 里是什么（常量？宏？单位后缀？），语料未写**——**本页不猜。**
> **这一条会直接决定你写 `100` 还是 `100 ms`，所以它是本页最该被读到的一处。**

**`noOfSMCExecutedTests`（一个指针）**

> 「References a pointer to store the number of SMC_TEST() statements which have been executed during this synchronize operation per site.」

**它带的限制比它的功能重要**：

> 「When using the class SMC_ARM_FOR_SITES() or SMC_ARM_OTHER_TS_FOR_SITES(), SMC_SYNCHRONIZE() does not not return a test count. As a result, noOfSMCExecutedTests is not incremented and does not count the number of calls to SMC_TEST().」

| 条件 | 结果 |
|---|---|
| 用 `SMC_ARM()` 起线程 | `noOfSMCExecutedTests` 记 **per site 已执行的 `SMC_TEST()` 条数** |
| **用 `SMC_ARM_FOR_SITES()` 或 `SMC_ARM_OTHER_TS_FOR_SITES()`** | **本 API 不返回 test count**；该指针**不被递增**，**也不数 `SMC_TEST()` 的调用次数** |

**`does not not return` 是重复词**（原文如此，**本页照录**，见「出处」⚠️③）。

**`forceErrorExitOnFail`（两条取值）**

> 「true - it causes an exception in case a calculation routine had to be aborted.」

> 「false - it causes SMC_SYCHRONIZE() to return false in case a calculation routine had to be aborted.」

**条件 → 结果**：

| 取值 | 计算过程被中止时的行为 |
|---|---|
| `true` | **抛异常** |
| `false` | **返回 `false`** |

**这里又出现了第二种错拼 `SMC_SYCHRONIZE`（少一个 `N`）**——**本页照录**（⚠️②）。

**`forceErrorExitOnFail` 没有默认值**：四条签名里它总是显式写出的参数。
**所以 `SMC_SYNCHRONIZE(100 ms)` 这一形在出错时走哪条路，语料未写。**
（**推断**：`### Syntax` 底下那段 Return value 写的是
`Returns false in case threads had to be terminated or an invocation error occurred, else true is returned.`
——读者容易据此认为默认就是「返回 false」，**但那是那一节对返回值的措辞，不是对默认值的声明**。
本页把它标成推断，不当文档事实用。）

**返回值（这一段与参数表分开放，别漏读）**

> 「Returns false in case threads had to be terminated or an invocation error occurred, else true is returned.」

**两种 `false`**：**线程被终止**，或**发生 invocation error**。其余情况返回 `true`。

> 「If the noOfSMCExecutedTests parameter is used, the number of SMC_TEST() statements which have been executed during this synchronize operation per site will be stored in the integer variable referenced by the pointer.」

## 典型用法

**本页给得出的是「位置」与「顺序」，给不出「一个完整例子」**——
原文没有 `## Procedure`、没有 `## Before you begin`，
`## Example` 一节只有两段各三行的说明加一行代码。

**位置与顺序（三条硬要求）**：

| # | 要求 | 依据 |
|---|---|---|
| 1 | **`SMC_ARM()` 起线程 → `SMC_SYNCHRONIZE()` 等它们**（顺序不能反） | 第一段 `threads which have been started using SMC_ARM()` |
| 2 | **per site 调** | 第二段 `has to be called per site` |
| 3 | **放在 `ON_FIRST_INVOCATION` 块外面** | 第二段的 `thus` 推出来的结论 |

**第 3 条反过来读也成立**：**把 `SMC_SYNCHRONIZE()` 放进 `ON_FIRST_INVOCATION_END()` 之前，
就等于让它「只跑一次」——而原文说它必须 per site。**

**一条时序上的推论（本页的推断，依据就是第一段）**：
`SMC_ARM()` 起的线程做完 `upload` 与 `calculation` 之后，排队的 `SMC_TEST()` 才被执行。
**所以 `SMC_SYNCHRONIZE()` 返回之前，`SMC_TEST()` 的结果还没有进 data log。**
**任何「读回上一条 `SMC_TEST()` 的结果」的写法都必须排在它后面。**

**原文的两个示例（逐字）**：

> 「Waits for all calculations to be finished within 100 ms. After the timeout of 100 ms all other still running calculation threads will be terminated!」

```
SMC_SYNCHRONIZE(100 ms);
```

> 「Waits for all calculations to be finished within 10 ms. After the timeout of 10 ms all other still running calculation threads will be terminated! In case a calculation had to terminated, SMC_SYNCRONIZE() throws an exception.」

```
SMC_SYNCHRONIZE(10 ms, true);
```

**两条示例的差别只有一个**：第二条多传了 `true`（= `forceErrorExitOnFail`），
所以**「计算被中止」这件事在第一条里体现为返回值，在第二条里体现为异常**。

**第二条说明里有两处语料瑕疵，本页照录**：
`had to terminated`（**缺 `be`**，⚠️④）与 `SMC_SYNCRONIZE()`（**少一个 `H`**，⚠️①）。

**本页答不了的一条，原文自己指了路**：

> 「To properly synchronize a test flow with the "thread per site" or the "common thread" implementation and also a mixture of both, refer to Synchronize a test flow with any use model in SmartCalc recommendations.」

**「thread per site」「common thread」「两者混用」三种 use model 各自怎么摆同步点**——
**本页一个字都没有**，因为那一段在 `SmartCalc recommendations`（`02.07.10.05`）里，**本页没读**。

**另一个空白**：`SMC_ARM()` 与 `SMC_SYNCHRONIZE()` 之间能放什么、能不能放两条
`SMC_SYNCHRONIZE()`、能不能干脆不调——**语料未写（在本篇里）**，本页不推。

## 和谁有关

**同一族的页（本页是 API 参考层，不是框架层）**：

- [[smartcalc-framework]]（**本页读过它，但一句都不搬**）— **SmartCalc 的框架/导读层**：讲「为什么要有 SMC」。
  **它自己的「语法 / 参数」节里就有 `SMC_SYNCHRONIZE()` 的示例代码**（脚本从子主题抽来的），
  而**那一页正文明确声明自己不解释这些名字**（它把这件事写在它的「出处」里）。
  **分工：那一页讲「为什么」，本页讲「什么时候结算」。**
- [[smartcalc]]（**未建**，slug 在清单里）— **`SMC_...` 那一族的 API 参考侧**。
  本页是 `.231.43`，**是那一族里的一条**；**本篇没有点名它**，
  **这一条关系是按编号前缀指的，不是文档说的**。
- [[smc-background-process-locks-config]]（**本页没读**）— SMC 后台进程的**配置锁**约束页。
  **本篇一个字都没提「锁」或「配置」**——本页只由 `SMC` 这个前缀与它相邻。

**本篇点名的 API 与页（全部是「文档事实」级的关系）**：

- `SMC_ARM()`（raw: `02.07.04.01.231.01_SMC_ARM.md`）— **上游**：**本页等的就是它起的线程**。
  **不在 allowlist，写名字**。**本页没读它**——所以「武装一次还是多次」「它有没有参数」
  「线程的生命期」本页一个字没有。
- `SMC_TEST()`（raw: `02.07.04.01.231.45_SMC_TEST.md`）— **下游**：
  `the queued SMC_TEST() statements` 在这里被执行，`data logging` 与 `binning` 都发生在这时候。
  **`smc-test` 不在 allowlist**（实测 `grep -x` 查过 `extract/prose-allowlist.txt`），所以按反引号 + raw 路径写。
  **本页没读那篇。**
- `SMC_SYNCHRONIZE_WITHOUT_BINNING()`（raw: `02.07.04.01.231.44_SMC_SYNCHRONIZE_WITHOUT_BINNING.md`）
  — **同族的兄弟**，`## Related information` 自己给的。
  **从名字看是「只同步、不分 bin」**，而本页正文刚说过「binning 在这里发生」——
  **两者的差是不是就在这一处，本页没有依据**（那篇没读）。**只指路，不断言。**
- [[on-first-invocation-begin]] — **本页点名它，而且是禁令的方向**：
  **本 API 必须在它开的块外面调**。`## Related information` 也列了它。
- `Four-step SmartCalc implementation`（raw: `02.07.10.04.03_Four-step_SmartCalc_implementation.md`）
  — `## Related information` 之一；**它也是 `SMC_backgroundProcessing()` 那个锚点所在的文档**。
  **本页没读**，所以「那个后台方法怎么写」本页没有。
- `SMC_ARM_FOR_SITES()` / `SMC_ARM_OTHER_TS_FOR_SITES()` — **本篇只在 `noOfSMCExecutedTests`
  那一格点了名**，说的是「用它们时本 API 不返回 test count」。
  **它们自己的语义、参数、与 `SMC_ARM()` 的区别，本页一个字没有**（没读，连 raw 路径都不知道）。
- [[hidden-upload]]（**本页没读**）— SMC 家族里「把上传藏起来」的那一页。
  **本页出现的词是 `Hidden data logging`**（raw: `02.07.10.04.09_Hidden_data_logging.md`），
  **不是 `Hidden upload`**——**两者是不是同一件事，本页没有依据**，所以只指路、不断言。

**这一页在 results 那段的位置**：

- [[mapping-results]]（**本页读过它**）— Results 段的五层对照表。
  **那张表 13 行 78 格里没有 `SMC_SYNCHRONIZE()` 这一格**：它的
  「把结果落成人读的报告与机器读的 STDF」一行，L2 列写的是
  `TESTSET` / `TESTSET::judgeAndLog_ScanTest` / `TEST` / `PUT_DATALOG`。
  **也就是说 results 的 L2 那一条路是「当场判、当场落」**，
  而 **`SMC_SYNCHRONIZE()` 是另一条路：先等线程，再一起落**。
  **那页自己也声明了「`02.07` 的 L2 页一篇没读」**——**本页就是它没读的那一族里的一个**。

**放进测试方法的那一段**：[[testmethod]]（本页 `stage: testmethod` 的理由）。

## 版本

**本文档有 `## Functional changes` 段，四条，全部照录**：

- `Introduced in SmarTest 6.5.3`
- `SmarTest 6.5.3: Patch 1 - New noOfSMCExecutedTests parameter.`
- `SmarTest 7.1.3: New data logging function hidden data logging`
- `SmarTest 7.2.1: Patch 1 - New forceErrorExitOnFail parameter.`

**四条与正文哪一处对得上**：

| 条 | 说的是 | 对得上正文哪一处 |
|---|---|---|
| 1 | **6.5.3 引进本 API** | **不是 §11.2 ② 的哨兵**——它写的是 `Introduced in`，不是 `Introduced before` |
| 2 | **6.5.3 Patch 1 加了 `noOfSMCExecutedTests`** | **签名里那两条带 `INT *noOfSMCExecutedTests` 的重载** |
| 3 | **7.1.3 引入 hidden data logging** | **正文第二段那条例外**（binning 改到后台方法里做） |
| 4 | **7.2.1 Patch 1 加了 `forceErrorExitOnFail`** | **签名里那两条带它的重载**，以及参数表里它的两条取值说明 |

**四条里两条带 `Patch`、两条不带**——**原文的写法如此，本页照录，不替它统一。**

**第 3 条给本页补了一层时间信息（推断）**：
「hidden data logging 改变了 binning 的位置」这件事是 **7.1.3 起的**——
**7.1.3 之前，`SMC_SYNCHRONIZE()` 没有这条例外。**
依据是原文把这句记成一条 `New data logging function hidden data logging`，
而正文的例外句自己没有写版本号——**两者是不是同一条，本页只能推到这一步，不往下断言。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.43_SMC_SYNCHRONIZE.md`
（TDC `120088.htm`，87 行 / 4,600 字节）。**整篇读完**——这篇短，
正文 + 语法 + 参数表 + 两个示例 + `## Related information` 就是它的全部。

**本页另外读过的两份 wiki 文件（不是 raw，读了只为指路，一句不搬）**：
`wiki/objects/smartcalc-framework.md`、`wiki/mappings/mapping-results.md`。

**本页没做的**：

- **`SMC_ARM()`（`.231.01`）原文没读。** 本页所有关于「谁起的线程」的依据，
  就是本篇第一段那一句 `started using SMC_ARM()`——
  **它的参数、能不能多次调用、线程的生命期，本页一个字没有。**
- **`SMC_TEST()`（`.231.45`）原文没读。** 所以本页凡讲「排队」「落盘」「binning」，
  依据都只是本篇点名它的那两处（第一段的 `the queued SMC_TEST() statements` 与参数表那一格）。
- **`SMC_SYNCHRONIZE_WITHOUT_BINNING()`（`.231.44`）原文没读。**
  **「WITHOUT_BINNING」到底少做什么，本页没有依据。**
- **`SMC_ARM_FOR_SITES()` / `SMC_ARM_OTHER_TS_FOR_SITES()` 的文档没读**
  （本页连它们的 raw 路径都不知道）。所以「为什么用它们就不返回 test count」本页没有。
- **`Hidden data logging`（`02.07.10.04.09`）、`Four-step SmartCalc implementation`（`02.07.10.04.03`）、
  `SmartCalc recommendations`（`02.07.10.05`）、`SmartCalc "Thread per site" and "Common thread"`
  （`02.07.10.02.01`）原文一篇没读。**
  所以「hidden data logging 的完整流程」「三种 use model 各自怎么摆同步点」
  「一个完整的 test method 怎么写」**本页一个字都没有**——原文把这三件事全推给了它们。
- **两篇 bin 规则的 use case 没读**（`Use of bins with multisite tests`、`Use of multibins`，
  原文在第二段里点名）——**`binning rules` 的具体内容本页不展开**。
- **一张图都没看——因为这一篇里没有图。** 实测：本篇全文 **0 处** `raw/`、
  **0 处** `.png` / `.jpg`。**所以本页没有任何来自图的结论**；
  **这不是「图够不着」，是这一篇里根本没有图**（§11.4）。
- **没有实跑。** 没有在任何机台上跑过 `SMC_SYNCHRONIZE()`、没有触发过一次超时、
  没有造过一次「计算被中止」。`verified: doc-only` 指的就是这件事。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① `SMC_SYNCRONIZE` 少一个 `H`，2 处**——正文第 12 行
> `SMC_SYNCRONIZE() has to be called per site and thus outside of an ON_FIRST_INVOCATION block.`
> 与示例第 2 段 `In case a calculation had to terminated, SMC_SYNCRONIZE() throws an exception.`
> —— **正确拼法是 `SMC_SYNCHRONIZE`**。
> **② 同一篇里还有第三种错拼 `SMC_SYCHRONIZE`（少一个 `N`），1 处**：
> `false - it causes SMC_SYCHRONIZE() to return false in case a calculation routine had to be aborted.`
> —— **同一篇文档里，这个 API 名有「拼对 / 少 H / 少 N」三种形态。**
> **本页照录，不替语料选一个。**
> **③ 重复词 1 处**：`SMC_SYNCHRONIZE() does not not return a test count.`
> —— **`not not` 重复了**（应为 `does not return`）。
> **④ 缺字 1 处**：`In case a calculation had to terminated`
> —— **`had to terminated` 缺 `be`**（应为 `had to be terminated`）。
> **⑤ 坏字 1 处**（本页量过：本篇含 `[一-鿿]` 的行 **1 行** / 全文 **87 行**）：
> `Resolution: 1 碌s` —— **`碌` 应为 `µ`**（`extract/encoding-map.csv` 第 2 行：`碌,µ`）。
> **本页正文照录这个坏字**，并在旁边注了正字。
> **⑥ 单位对不上**：参数表写 `The time in seconds`，两个示例写 `100 ms` / `10 ms`。
> **两个都照录，本页不裁定**（见「是什么」那一处 ⚠️）。
> **⑦ 本篇未发现 `DC/DC power units`**（实测 0 命中）。
> **但这是「本页量过的」，不是「语料干净」**（§13.1 第 ⑥′）。

`verified: doc-only`
