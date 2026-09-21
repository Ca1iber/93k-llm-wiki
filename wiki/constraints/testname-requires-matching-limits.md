---
type: constraint
title: 自定的 testName 必须在 test suite 里有同名 limits
layer: L1
stage: testmethod
tags: [constraint, testmethod, limits, parametric-test, testname]
related: [[testmethod]], [[results]], [[spec-set]]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.03.01_Continuity.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.03.02_DpsConnectivity.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.03.04_GeneralPMU.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.03.05_Leakage.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.03.06_OperatingCurrent.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.03.07_OutputDC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.03.08_ProductionIddq.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 自定的 testName 必须在 test suite 里有同名 limits

## 约束是什么

参数测试例程（continuity、leakage、Iddq 这一类）让你**自己给测量起名字**，
名字通过 `testName` 参数传进去。**起了名字就得配上同名的 limit**：

> If you define new test names in the parameter testName, you need to add limits to the test suite with the same test name.

**这是 §2.4 的 D3（一致匹配）**——
两处的 `test name` **必须字面相同**：一处是测试程序里的参数值，
一处是 test suite 上挂的 limit 条目的名字。

## 在什么条件下成立

**触发条件是 `If you define new test names`**——文档把它写成了**条件句**，
不是无条件要求。**这一句的边界很要紧**：

- **只要你新起了名字**，这条就成立；
- 文档**没有说**「不起新名字时怎么办」（那大概是用例程自己的默认名，
  但**这是推断，文档在这一句里没写**）。

**这条规矩只覆盖「配套」这一件事**，不涉及 limit 的数值——
数值怎么定、放哪一张 suite，**是另一件事，本页不管**。

## 违反了会怎样

> **⚠️ 本次未找到任何描述报错形态的原文。**

这 7 篇文档都只写了「you need to add limits …」，
**没有一句写「不加会怎样」**。本页不猜。

**⚠️ 但这一条有个很具体的可疑形态，标出来是推断**：
文档把 limit 说成是挂在 **test suite** 上的、按 **test name** 去对。
名字对不上时，**测量本身可能照样跑完、照样有数**——
出问题的是**判定那一步**（limit 找不到 → 不判 / 判不了）。
**这是推断，我没有在语料里找到依据，写在这里只是为了让人知道「该往哪儿看」。**

> **它和本页其他条目不同**：[[label-edit-requires-tstl-selection]] 那类文档写了逐字报错句，
> 本页这一类没写。**「文档没写」不等于「不会报错」**（§2.1）。

## 数字口径

**7 处 / 7 行 / 7 文件 / 7 篇独立文档**——**没有重复投放，一一对应**。
数字出自 `extract/rule_evidence.py`（键 `L-testname`），可重跑。

**7 篇全部落在 `02.07.05.03_*` 参数测试例程子树下**：
Continuity、DpsConnectivity、GeneralPMU、Leakage、OperatingCurrent、OutputDC、ProductionIddq。

> **这 7 篇是同一段模板**（同一句话，逐字相同），
> **不是 7 处各自独立的表述**——理由与
> [[smc-background-process-locks-config]] 里那条 TMLimits CAUTION 同源（§10）：
> **多篇 ≠ 多次独立印证。**
>
> **但这与前面几页有一处不同，值得记**：这里连 `source_topic` 都是
> **不同文档**（7 个不同的例程页），说明这句话是**从一篇例程页复制到其余六篇的**。
> **复制传播本身就是文档事实**——它说明这条要求在 Advantest 的文档体系里
> 被当成**每个例程都要交代一遍**的事，**不是某一页的偶然措辞**。

## 与 [[testmethod]] / [[results]] 的关系

- [[testmethod]] 讲测试方法类怎么写；本页管**它里面自定名字和外部 limit 的对应**。
- [[results]] 讲结果怎么组织；本页管**结果能不能被判**——
  limit 是按 test name 找的，**名字断了，判定链就断了**。

## 出处

| raw | 里面的原句 |
|---|---|
| `02.07.05.03.01_Continuity.md` | 原句（在 `## Limits` 段下） |
| `02.07.05.03.02_DpsConnectivity.md` | 同一句 |
| `02.07.05.03.04_GeneralPMU.md` | 同一句 |
| `02.07.05.03.05_Leakage.md` | 同一句 |
| `02.07.05.03.06_OperatingCurrent.md` | 同一句 |
| `02.07.05.03.07_OutputDC.md` | 同一句 |
| `02.07.05.03.08_ProductionIddq.md` | 同一句 |

**原句后面跟着两个指向操作步骤的链接**（"Adding a limit in the Properties view" /
"Adding a limit on the Tests page"）——**说明「怎么加」不是本页的事，是那两页的事**。
本页只记「必须同名」这一条。

文档事实，`verified: doc-only`。

## 这条约束怎么被发现的

**这一族的族名先前是对的，但我的 grep 差点把它判死。**

我先按 `testName[^.]{0,60}limit|limit[^.]{0,60}testName` 扫，得到 **108 处**，
**印出来的前 7 条全是 API 签名**——`limits(const STRING& testname)`、
`addLimit(const std::string& testName)`——**看起来完全是「这只是个参数名，不是规矩」**。

真正那句话在 **第 100 条开外**（`02.07.05.*` 排在 `02.07.04.*` 之后）。
**我只看前 7 条就会把它判死。**

> **本批第二次踩同一个坑**（第一次是 `execution-context`）：
> **打印上限是一个不声不响的过滤器。**
> 两次都是**回原文按行号核**才纠正的，两次都不是靠那个 grep 纠正的。
>
> **可复用的做法**：宽正则只用来**定位文件**，
> **判断「这条规矩存不存在」必须打开原文看那一段**——
> 因为「命中很多但都是噪声」和「命中很少因为没有」**在打印结果上长得一样**。
