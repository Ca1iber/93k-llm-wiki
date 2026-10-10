---
type: object
title: addLimit
layer: L2
stage: testmethod
tags: [testmethod, l2, test-method-api, limit, testname, limits-tab, properties-view]
related: [testmethod, limit, tmlimits, testname-requires-matching-limits, test-method-class, test-method-project, mapping-testmethod, test-suite]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.02_addLimit.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# addLimit

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **337 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.02_addLimit.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
TestMethodLimitProxy& addLimit(const std::string& testName)
```

Parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99952.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I/O | Parameter | Description

### Example

Refer to the example in `Test method concept`（raw: `02.07.02.01_Universal_test_method_concept.md`）.

<!-- 语法节 end -->

## 是什么

**`addLimit` 是一条「只登记名字、不管值」的接口。** 本篇两句话就说完了它的全部机制：

> This API adds a limit to the test method. The default values ('NA') will be added to the limit. You need to add the limit values in the tabular testflow editor (See Limits tab) or Properties view.

拆开看，这里有一件**分工**：

| 谁 | 干什么 | 原文 |
|---|---|---|
| **本 API** | **把一条 limit 加进 test method**，此时值是默认的 | `This API adds a limit to the test method. The default values ('NA') will be added to the limit.` |
| **谁填真值** | **不是在代码里填**——要到 **tabular testflow editor 的 `Limits` 页**，或者 **Properties view** | `You need to add the limit values in the tabular testflow editor (See Limits tab) or Properties view.` |

**这是本页最要紧的一条**：`addLimit` **不负责限值**，它只负责**让这个 test method 里存在这么一条 limit**。
**值在 testflow 那一侧填**——所以**代码侧与 testflow 侧两边必须对上**（对不上的后果不在本篇，见「和谁有关」）。

### 签名与参数

```
TestMethodLimitProxy& addLimit(const std::string& testName)
```

| 项 | 原文 | 本页能说的 |
|---|---|---|
| **返回类型** | `TestMethodLimitProxy&` | **返回一个 `TestMethodLimitProxy` 的引用**——**不是 `void`**。**这个 proxy 上有什么成员函数、拿到它能干什么，本篇一个字都没写**（`TestMethodLimitProxy` 自己那一页也不在本篇的 `sources` 里）。 |
| **参数个数** | 参数表只有一行 | **只有一个入参**（`I/O` 列写 `I`），**没有出参**。 |
| **`testName`** | `A test name for the test method.` | **参数名与说明都只说「这是 test method 的一个 test name」**——**它和别处哪个名字是一回事，本篇没写**（见「和谁有关」）。 |
| **头文件** | `/opt/hp93000/soc/testmethod/include/testmethod.hpp` | **原文只给了路径**；编译怎么配置、要不要 include 别的头，**语料未写**。 |

### 默认值是 `'NA'`——这一句有三个说不清的地方

`The default values ('NA') will be added to the limit.` 这一句**照实读完，还剩三处没交代**：

| 没交代的 | 原文的样子 |
|---|---|
| **是几个值** | 写的是复数 `values`，括号里却只有一个 `'NA'` |
| **`'NA'` 是什么** | 是**字面字符串** `NA`，还是「不可用 / 未定」的标记？**原文没有解释** |
| **默认值会不会被判** | **本篇没有一个字讲判定**——「`NA` 的 limit 参不参与 pass/fail」**语料未写** |

**这三条本页都不填。** 依 §11：**文档没写就写「语料未写」，不许推测填空。**
（唯一能确定的是：**不填值也能先 `addLimit` 一条出来**——这是 `default values will be added` 的直接含义。）

### 本篇只有 48 行：它是一篇「入口 + 指路」的页

本篇没有 `## Application` 段、没有 `## Procedure` 段、没有 `## Before you begin` 段、
没有 `## Important points` 段。**连 `## Example` 段里也没有例子**，只有一句指路
（见「典型用法」）。所以：

**本页能给的极限就是上面那些。** 「limit 在代码里怎么用」「判定怎么写」
**不在本篇**——`## Example` 段把读者推给了另一篇（`Test method concept`），本页没读那篇。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、`## Example` 段也没有代码。**
能排出的只有两步，**而且第一步的「在哪儿调」本页给不出来**：

1. **调 `addLimit(testName)`**，把一条 limit 加进 test method。此时它的值是默认的 `'NA'`。
2. **到 testflow 侧填真值**：**tabular testflow editor 的 `Limits` 页**，或者 **Properties view**。

**⚠️ 第 1 步这一步在本篇里是「不知道在哪个函数里调」的。**
坊间常见的说法是「在 `initialize()` 里 `addLimit("limit");`」——
**那个写法不是本篇的**：**本篇 raw 里 `initialize` 这个词出现 0 次**。
出处是 [[mapping-testmethod]] 与 [[testmethod]] 两个 wiki 页（它们引的是 `01.06.02.03` 那一篇，
**本页没读**）。**本页把它标成「wiki 页的记载」，不当成本篇的文档事实。**

**`## Example` 段给的原文只有一句**：

> Refer to the example in Test method concept.

**所以「用法长什么样」本篇的答案是：去 `Test method concept` 那一篇看。**
（raw：`02.07.02.01_Universal_test_method_concept.md`，**本页没读**。）

**要读的例子和要填值的两处，本篇都只给了指针：**

| 本篇指的路 | 原文里的名字 | raw |
|---|---|---|
| 例子 | `Test method concept` | `02.07.02.01_Universal_test_method_concept.md` |
| 填值的第 1 处 | `Limits tab` | `02.08.04.32.03.01.03_Tests_page.md` |
| 填值的第 2 处 | `Properties view` | `02.08.04.32.03.04_Testflow_Properties_view.md` |

**三篇本页一篇都没读。**

## 和谁有关

- [[testmethod]] — **stage 页，也是本页 `stage: testmethod` 的理由**。`addLimit` 是 test method 里的一个调用；
  **「test method 这一步整体怎么走」在那一页，本页不写流程**（§2.2）。
  （那一页把本页记成「在 `initialize()` 里给 test method class 注册 limit 名」——
  **`initialize()` 这个说法出自它，不是本页的 raw**，见「典型用法」。）
- [[limit]] — **名字最近的另一个 L2 页**。[[limit]] 讲的是 `LIMIT` **对象**
  （承载 low/high limit 与比较运算符，作 `TEST()` 的 limit 参数）；
  **本篇 raw 里 `LIMIT` 这个类名出现 0 次**，**本页没有依据说两者是同一个东西、或者有什么先后关系**。
  **按页名相邻列出，不代表同物。**
- [[tmlimits]] — **另一条「用外部表控 limits」的路**（TMLimits / CSV）。
  **本篇一个字都没提它**；「API 登记的名字 ↔ TMLimits 表里的名字」这条关系**本页没有依据**。
- [[testname-requires-matching-limits]] — **名字必须对上那条规矩的汇总页**。
  两页的关系是**互补**：那页管「名字必须与 test suite 上的 limit 同名」，
  本页管「名字怎么登记进来」。
  **注意那一页的证据不是本篇**：它的 7 篇 `sources` 全在 `02.07.05.03_*` 参数测试例程子树下，
  **本篇不在其中**。那页里确实点到过 `addLimit(const std::string& testName)`，
  但**是把它当成「看起来像参数名、其实是规矩」的反面例子引的**——
  **那条引用说明的是它扫到了这个签名，不是它读了本篇。**
- [[test-suite]] — **limit 值真正挂上去的地方**。原文把「填值」推给 testflow 工具那一侧，
  而约束页把 limit 说成是**挂在 test suite 上、按 test name 对**的。
  **这条「挂在哪」本页没有依据**（原文只说 `in the tabular testflow editor (See Limits tab) or Properties view`），
  **本页不据此声称它挂在 [[test-suite]] 上**。
- [[test-method-class]] / [[test-method-project]] — **（推断）本页调用的宿主**。
  原文说的是 `adds a limit to the test method`，而「test method」在本 wiki 里对应
  [[test-method-class]] 那一侧（class 的模板与参数由它讲）。
  **依据只是 `the test method` 这个措辞与那两个页名**；**本篇没有出现 class 工程、C++ perspective 之类的词。**
- [[mapping-testmethod]] — **跨层对照表**，本页在那张主表里占一格：
  「在 `initialize()` 里注册 limit **名**」那一行的 L2 列就是 [[add-limit]]。
  **那一格里的 `addLimit("limit");` 与 `initialize()` 都不是本篇的字**——
  **本页只是被它列为 L2 侧的代表。**
- `TestMethodLimitProxy` — **本页的返回类型**。**本篇只给了它的名字，一个成员函数都没给**；
  它自己的文档页**本页没读、也不在本篇的 `sources` 里**（**不在 allowlist，故不链**）。
- `Test method concept`（未建） / `Limits tab` / `Properties view` — **本篇指出的三条路**，
  **本页一篇都没读**（raw 路径见上面那张表）。
- **本篇没有 `## Related information` 段**，也没有 `## Functional changes` 段——
  **所以上面这些关系里，没有一条是「文档点名」的**：它们全部来自 wiki 页的记载、或者本页标明的推断。

## 版本

**本文档没有 `## Functional changes` 段。**（这是事实，不是缺陷——§2.2。
**48 行里确实没有这一节**，实测本篇 grep `Functional changes` 命中 0。）

**所以关于 `addLimit` 的版本信息，本篇一个字都没有。**
**「它哪个版本引入的」本页答不出来**，也不去别的文档里找（§11：不臆造 API，
**更不许拿别篇的版本行安到这一篇上**）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.02_addLimit.md`
（TDC `99952.htm`，25 行 / 953 字节）。**整篇读完**——**这页之所以短，是因为它本来就短**。

**本页没做的：**

- **`Test method concept` 没读**（`02.07.02.01_Universal_test_method_concept.md`）——
  **这是本篇 `## Example` 段唯一的指路**。所以「`addLimit` 的完整例子长什么样、
  它在哪个函数里被调、返回值怎么用」**本页一个字都没有**。
- **`Limits tab` 与 `Properties view` 两篇没读**
  （raw 分别是 `02.08.04.32.03.01.03_Tests_page.md`、`02.08.04.32.03.04_Testflow_Properties_view.md`）——
  **「值到底怎么填、填进去之后存在哪、长什么样」本页没有。**
- **`TestMethodLimitProxy` 那一页没读**（本篇连它的 raw 路径都没给）。
  所以**那 278 字符的语法节里唯一一个没说清的返回类型，本页补不了**。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** 没有在任何机台上写过一行调 `addLimit` 的 test method，
  也没有验证过「不填值时判定会怎样」。`verified: doc-only` 指的就是这件事。
- **`02.07.05.03_*` 那一族参数测试例程没读**——**那条「名必须同名」的约束本页不写**，
  它有自己的页（见「和谁有关」）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`## Example` 段里没有例子。** 整段只有一句 `Refer to the example in Test method concept.`——
> **一个代码块都没有**。语法节里那个 `### Example` 标题下面就是这句话，
> **不是脚本抽漏了，是原文如此**。
> ② **参数表的表头把 `Parameter` 写了两遍。** 摊平后的原文逐字是
> `Parameter` ／ `I/O` ／ `Parameter` ／ `Description`——
> **第一列与第三列的标题同名**。这是语料把原表摊平成一串单元格之后的样子，
> **本页照录，不替它改**（同一形态在别篇也有）。
> ③ **`The default values ('NA') will be added to the limit.`**——
> **复数 `values` 配单数 `'NA'`**，而且 `'NA'` 是用**单引号**包的。
> **本页照原样引出，不替它补解释**（下面「是什么」里把三处没交代的地方逐条列了，
> **列出来是为了说明「本篇没写」，不是替它圆**）。
> ④ **链接文本与目标文件名不一致**：链接文本写的是 `Limits tab`，
> 指向的文件却是 `02.08.04.32.03.01.03_Tests_page.md`（`Tests page`）。
> **「`Limits` 页签」很可能就是 `Tests page` 上的一个页签，所以它未必是错**——
> **本页没读那篇，不判**（§10：不自行选一个当正确答案）。
> ⑤ **本篇没有坏字。** 实测全文 **0 处非 ASCII 字符**（没有 `鈥` / `渭` / `碌` 那一族）。
> **但这是「本页量过的」，判据是本篇这一个文件**；§11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上写过或跑过 `addLimit`**
（§11：文档里有 ≠ 这台机器上能用；尤其「不填值时的默认 `'NA'` 行为」，
**文档没写清，动手前先照实机核对**）。
