---
type: constraint
title: SMC 后台进程运行中不许改动它读的配置与参数
layer: L1
stage: run
tags: [constraint, smartcalc, background-process, thread-safety, hidden-upload]
related: [[testmethod]], [[hidden-upload]], [[run]], [[results]]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.01_SMC_ARM.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10.02.02_Thread_safety.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10.05_SmartCalc_recommendations.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10.04.09_Hidden_data_logging.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SMC 后台进程运行中不许改动它读的配置与参数

## 约束是什么

**SMC 后台进程（background process）跑起来之后，它读的那些东西就不许再动了。**
文档点名点了三类：**test method class 的成员变量**、**TMLimits 表**、**Mode context**。

> Member variables of the test method class that are used in a background process must not be changed while the background process is running.

> CAUTION You must not change or reload a TMLimits table while an SMC background process is armed or running. Violating this rule may result in invalid data or the crash of the test method.

> Hidden uploads, controlled and started by SMC_ARM() must be finished before a Mode context is changed.

## 在什么条件下成立

**条件是「后台进程 armed 或 running」，不是「测试在跑」。**
这两个条件**不一样**，别和 [[pin-config-locked-during-test]] 合并——
那条管的是「测试运行中」，这条管的是「后台线程活着」。
**后台进程的生命周期比 `run()` 长**（见 §「违反了会怎样」里那句原文），
所以存在「`run()` 已经返回、后台还在跑」的窗口，**那个窗口里同样不许动**。

**范围有三类，文档给的是并列的三种说法**：

| 不许动的东西 | 原文限定语 |
|---|---|
| 类的成员变量 | `must not be changed while the background process is running` |
| TMLimits 表 | `must not change or reload`（**改和重新加载都算**） |
| Mode context | `must be finished before a Mode context is changed` |

> **⚠️ 「armed or running」是本条最容易被漏掉的半句。**
> 已 `SMC_ARM()` 但还没真跑起来的状态**也算**。
> 按「running」去理解、在 armed 之后就去改 TMLimits，**文档说这是违规的**。

**文档还给了一条替代做法**（不是禁令，是出路）：

> If you read and write commonly accessible variables in a multi-thread environment you need to guard them with a mutual exclusion (mutex).

**用 mutex 保护，而不是「约定不去写」。**

## 违反了会怎样

**文档逐字写了后果，而且是本 wiki 里语气最重的一类。**
注意后果**不是「报错」，是「数据错了」或「崩了」**：

> CAUTION Parallel access to member variables of a test method class through the run() function and a background process may result in invalid data or in a crash of the test method and is therefore not allowed.

> Using non-thread-safe APIs in a background process can result in loss off data, invalid data, or a crash of the test method.

> **原文如此：`loss off data`（`of` 写成了 `off`）。**
> §11.1：引文照抄，**错拼不改**，在旁边记一笔就够了——
> **修的是「记录」，不是「引文」。**

**⚠️ 这一条与本 wiki 其他约束的关键差别**：
别的约束违反后**固件拦你**（报错、命令被拒）；
**这一条固件不拦**——它只是**产出错的数据**。
`invalid data` 会流进 results，**在测试跑完、甚至分析完之前都不会有任何提示。**

**为什么要写这句话进 wiki**：它是「静默做错」类约束的实例，
与 [[label-edit-requires-tstl-selection]]（报错类）形成对照——
**两类约束在使用者眼里长得一模一样（都是一条禁令），代价却完全不同。**

## 「3 篇文档都说」这件事，比看上去弱

上面第二条 TMLimits CAUTION，在语料里出现在 **3 篇不同文档**里，
**逐字完全相同**（`02.07.04.01.250_TMLimits`、`02.07.10.04.09_Hidden_data_logging`、
`02.07.10.05_SmartCalc_recommendations`，`sources` 已列）。

> **⚠️ 但这不是「三次独立印证」。** 三篇是同一句话的**再投放**，
> 不是三个人各自得出的结论。§10 要求判 `source_topic` 是否相同——
> 这三篇的 `source_topic` 不同（是不同文档），**但它们复用的是同一段文字**。
> **数字上「3 篇」，证据强度上要按「1 句话」算。**

数字口径：含后果描述的句子 **19 处**，但只落在 **10 行**、**8 篇独立文档** 上。
**处数与行数不相等，是因为语料把两条 CAUTION 塞进了同一行**
（`SMC_ARM.md` 第 21 行里既有成员变量那条、也有 parallel access 那条）。
**报「处」还是报「行」，页面必须说清是哪个**（§13.1 ②）。
数字出自 `extract/rule_evidence.py`（键 `E-caution` / `E-must-not`），可重跑。

## 与 [[hidden-upload]] / [[testmethod]] / [[run]] 的关系

这句把两条线索接上了：

> Hidden uploads, controlled and started by SMC_ARM() must be finished before a Mode context is changed.

- [[hidden-upload]] 讲**什么是隐藏上传**；本页讲**它没结束之前不许换 Mode context**。
- [[testmethod]] 讲**测试方法类怎么写**；本页管**它跑起来之后成员变量的可写窗口**。
- `SMC_ARM()` 在 [[run]] 里调用，但**它的生命期跨出 `run()`**——
  文档原句提醒了这件事（`as the background process will last longer than the run() function
  where it has been armed`）。

## 出处

| raw | 里面的原句 |
|---|---|
| `02.07.04.01.231.01_SMC_ARM.md` | 成员变量句、parallel access CAUTION、hidden upload / Mode context 句、生命期长于 `run()` 的说明 |
| `02.07.04.01.250_TMLimits.md` | TMLimits CAUTION |
| `02.07.10.04.09_Hidden_data_logging.md` | 同一句 TMLimits CAUTION |
| `02.07.10.05_SmartCalc_recommendations.md` | mutex 替代做法、同一句 parallel access CAUTION、同一句 TMLimits CAUTION |
| `02.07.10.02.02_Thread_safety.md` | `loss off data` 那句 |

**这四篇文档都在 `02.07.10` 与 `02.07.04.01.231*` 子树下**，属 SmartCalc 一组。
注意 `SMC_ARM_FOR_SITES` / `SMC_ARM_OTHER_TS` / `SMC_ARM_OTHER_TS_FOR_SITES`
三个变体各自也带一份同样的段落（本次未逐句比对是否逐字相同，
**⚠️ 只说「带同样的段落」，不说「逐字相同」**）。

文档事实，`verified: doc-only`。

## 这条约束怎么被发现的

**`constraints.py` 的候选表把它顶上来了**——这是少数几个
「机械判据真正抓到的真约束」。原因是它的**后果句高度模板化**
（`invalid data or ... crash of the test method` 反复出现），
所以在「同一句规矩在多少篇文档里复现」这个判据下分数很高。

> **反过来看这件事**：同一个判据**抓到了这条**，却**漏掉了**
> [[pin-config-locked-during-test]]（只写在 2 篇的章首 Note 里）。
> **判据的偏向正好在「模板化的后果句」上**——
> 警告写得越标准，越容易被抓到；**而最危险的规矩往往写在最不标准的位置。**
> 这是那条候选表为什么只能当「取材清单」的实例（§2.4）。
