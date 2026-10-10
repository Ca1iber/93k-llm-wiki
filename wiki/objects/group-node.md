---
type: object
title: Group node
layer: gui
stage: testflow
tags: [testflow, gui, group-node, grouping, group-bypass, readability]
related: [testflow, testflow-file, test-suite, flow-control-node, assign-value-node, mapping-testflow, testflow-properties-view, tpt-import-from-device, smartest-6.3.2, smartest-7.1.3, smartest-7.2.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.05_Group_node.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Group node

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Group node（组节点）是 testflow 里的一个「折叠容器」——把同一层级里连续若干节点收成一组，
目的是让长 testflow 好读。** 本篇的全部机制就在这一句里：

> You can put several consecutive nodes within the same testflow level together into one group. This way, you can display an apparently long testflow in a more easily readable form.

**这一句里两个限定词是「能收谁」的全部约束**：

| 限定 | 原文 | 含义 |
|---|---|---|
| **同一个 testflow 层级** | `within the same testflow level` | **不许跨层收** |
| **连续** | `several consecutive nodes` | **不许挑着收**——中间夹着的要么一起进、要么不进 |

**收组的目的是「显示」，不是「执行」。** 原文给的理由是
`This way, you can display an apparently long testflow in a more easily readable form.`
——`display` / `more easily readable`。**本篇没有一句说 group 会改变执行顺序或判定**；
**唯一会动执行的属性是下面那个 `Group Bypass`。**

### 两种造法（第二种是 7.2.2 才有的）

> You can either create a group node out of several consecutive nodes, or you can create an empty group and add new nodes, test suites or floating test suites later.

| 造法 | 做法 | 版本落点 |
|---|---|---|
| **① 就地收编** | 选若干**连续**节点 → 收成一组 | `Introduced before SmarTest 6.3.2`（**哨兵值**，见「版本」） |
| **② 先建空组** | **先建一个空 group**，之后往里加 `new nodes` / `test suites` / `floating test suites` | **`SmarTest 7.2.2: Add an empty group node`** |

**第 ② 条的版本落点是本篇自己给的**：`## Functional changes` 里 7.2.2 那一条写的就是
`Add an empty group node`，而正文里「可以建空组、以后再加」那句正好对应它。
**两条并排看：空 group 是 7.2.2 引入的**（本页把两处对齐，不替语料调和措辞）。

### 三个属性，只有一个会改变执行

原文：`On the Properties view you determine the following values:`——**三个值**：

| 属性 | 原文那一格（逐字） | 说明 |
|---|---|---|
| **Group Name** | `256` ／ `Names with more than 19 characters abbreviated. The name is displayed in the group graphic with the first and last 9 characters separated by three dots (...).` | **只在图上显示用**，见下面「名字长了怎么显示」 |
| **Group Comment** | `(More than 2056 characters allowed)` | 注释；**原文没说它出现在哪、给谁看** |
| **Group Bypass** | `If selected SmarTest skips the group and its elements when running a testflow.` | **唯一一个动执行的属性**：勾上 → **整个组连同组内元素在运行时被跳过** |

**`Group Bypass` 那一格还带一条兼容性警告**（同一格内，逐字）：

> Note that if Group Bypass is selected the testflow (file) is not backward compatible with SmarTest versions before 7.1.3.

**即：勾了它，这个 testflow 文件在 7.1.3 以前的 SmarTest 上读不了。**
这条与 `## Functional changes` 里 `SmarTest 7.1.3: Flag Group Bypass introduced` 对上——
**这个属性本身是 7.1.3 才引入的**，所以更早的版本既没有它、也读不了带它的文件。

### 名字长了怎么显示

> Names with more than 19 characters abbreviated. The name is displayed in the group graphic with the first and last 9 characters separated by three dots (...).

**规则是「前 9 个字符 + 三个点 + 后 9 个字符」，中间被省掉。**
**注意作用范围**：原文写的是 `The name is displayed in the group graphic with the first and last 9 characters separated by three dots (...)`——
**被缩略的是「图上的显示」，不是名字本身。**

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
本篇能给的操作信息只有三样：**两种造法**（上面）、**三个属性**（上面）、
**`## Related information` 的两条链接**（见「和谁有关」）。

**按本篇字面能排出来的顺序只有一条——「收谁」在「设属性」之前：**

1. **在同一个层级里选连续节点**（原文的限定：`several consecutive nodes` `within the same testflow level`），
   **或者先建一个空组**（7.2.2 起），之后再往里加节点 / test suite / floating test suite。
2. **在 Properties view 上设 `Group Name` / `Group Comment` / `Group Bypass`**
   （原文 `On the Properties view you determine the following values:`）。
   **三个里只有 `Group Bypass` 会改变运行行为**；另两个只影响显示与记录。
3. **勾了 `Group Bypass` 就要接受那条兼容性代价**：文件在 SmarTest 7.1.3 之前读不了。

**「怎么把节点拖进组里」「空组是哪个菜单/哪个按钮建出来的」「组在流程图上长什么样」——语料未写。**
本篇**没有任何图**，所以这些动作在界面上是什么样，**本页一个字都写不出来**。

## 和谁有关

- [[testflow]] — **stage 页，也是本页 `stage: testflow` 的理由**。group node 是 testflow 组装期的一个结构件；
  **「Testflow 这一步怎么走」在那一页，本页不写流程**（§2.2 的分工）。
- [[testflow-file]] — **落盘的那一侧**。[[mapping-testflow]] 把本页排在
  「`testflow-file` 的 `test_flow` section（含 `{}` 与 `<compound_label>`）」那一格——
  **那是 [[mapping-testflow]] 的记载，不是本页的**：**本篇 raw 里一个文件名、一个 section 名都没有**。
- [[test-suite]] — **能往空组里加的三样东西之一**。原文列的是 `new nodes`、
  `test suites`、`floating test suites`。**test suite 本身那一层在 [[test-suite]] 页**，
  本页只有「它可以被放进组里」这一条，**没有它是什么的任何说明**。
- [[flow-control-node]] / [[assign-value-node]] — **同族的节点页（名字都以 `node` 结尾）**。
  **本篇 raw 一个字都没提它们**；[[assign-value-node]] 自己就把这条关系标成「**（推断）名字同族**」，
  并写明「**本页不判它们与本节点同不同层、是不是同一批**」。**本页沿用那个口径，不新声称任何关系。**
- [[tpt-import-from-device]] — **它从参数名（`include_groups` / `empty_groups`）反推本页是「group 的宿主页」**，
  而且那一页自己明写「**本页没读它**」，依据只是页名。**本页不回认这条**：
  本篇没有这两组参数的任何信息，也说不清 group 在文件里怎么被选中。
- [[testflow-master-file]] — 那页写 `all top level objects must be groups`，并把本页记成
  「能拆出去的最小顶层单位」。**那是它的文档事实，不是本篇的**——
  **本篇只讲「同一层级里连续节点收成一组」，没有一句说 group 是顶层单位。**
- [[mapping-testflow]] — **跨层对照表**。本页在那张主表里占一行（GUI 侧 [[group-node]]、
  文件侧 `test_flow` section、L1 `—`、L2 `—`、L3 `?`）。
- [[testflow-properties-view]] — **原文那句 `On the Properties view you determine the following values:`
  指的场所**。**注意原文只写 `Properties view`，没有写全名**；
  「它是不是 [[testflow-properties-view]] 那一页」**是（推断）**，
  依据是 group node 就是 testflow 里的节点、而那三个属性是节点属性。**本页没有去核那一页。**
- [[testflow-tool]] — **（推断）操作它的 GUI 入口**。**本篇 raw 里没有出现任何工具名**——
  连 `Testflow Tool` 这个字符串都没有。**所以这条关系本页没有依据**，只按同 stage 并列。
- `Hierarchy within a testflow` / `Grouping nodes` — **本篇 `## Related information` 段的全部两条链接**
  （raw：`02.08.04.32.01.03_Hierarchy_within_a_testflow.md`、
  `02.08.04.32.02.01.11.07_Grouping_nodes.md`）。**两篇本页都没读**；
  **它们是本页的父页还是专题页，本页不知道。**
- [[smartest-6.3.2]] / [[smartest-7.1.3]] / [[smartest-7.2.2]] — **版本页**：
  本篇 `## Functional changes` 的三条分别落在它们身上（见「版本」）。

## 版本

本文档有 `## Functional changes` 段，**三条，逐条转录**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.3: Flag Group Bypass introduced`
- `SmarTest 7.2.2: Add an empty group node`

**三条都要留意：**

- **第一条是哨兵值**（§11.2 ②）：`Introduced before SmarTest 6.3.2` 的意思是
  「**在本文档集覆盖范围开始之前就已经有了**」，**不是「SmarTest 6.3.2 新增了 group node」**。
  **照字面读会生成一条「6.3.2 新增了分组能力」的假信息，而格式齐整、看不出来。**
- **后两条与正文逐条对得上**（本页把两处并列，不替语料调和）：
  - `7.1.3` 那条对应正文里 **`Group Bypass` 属性**，以及同格那句
    「勾了它，文件在 7.1.3 以前不兼容」的警告；
  - `7.2.2` 那条对应正文第一段的 **「先建一个空 group，以后再加节点 / test suite / floating test suite」**。
- **三条合起来给出一条时间线**：**「就地收编连续节点」这一条早于本文档集覆盖范围**，
  `Group Bypass` 是 **7.1.3** 加的，空 group 是 **7.2.2** 加的。

**本篇没有记录 `Group Bypass` 或空 group 之后被改过**——
**「没记录」不等于「没改过」**（§13.1 第 ⑥′）。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.05_Group_node.md`
（TDC `20234.htm`，29 行 / 1,506 字节）。**整篇读完**——**这页之所以短，是因为它本来就短**。

**本页没做的：**

- **`Hierarchy within a testflow` 与 `Grouping nodes` 两篇没读**（本篇 `## Related information` 的全部两条）。
  所以**group 在 testflow 的层级结构里到底处在哪一层、除了收组还有哪些分组做法，本页一个字都没有**。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论**：「组的图形长什么样」「`Group Bypass` 是哪个勾选框」
  **本页只知道名字**。这与「图够不着」不是一回事（§11.4）。
- **Properties view 那一篇没读**（原文把它链在 `02.08.04.32.03.04_Testflow_Properties_view.md`），
  所以**这三个属性在界面上排在哪儿、有没有第四个、界面上叫什么**，本页不知道。
- **`testflow-file` 的格式没读**——**一个 group 在文件里落成什么，本页没有依据**。
  （[[mapping-testflow]] 那一格的说法**出自那一页**，本页不引它当自己的事实。）
- **没有实跑。** 没有在任何机台上建过组、也没有勾过 `Group Bypass` 去验证
  「跳过整组」与「7.1.3 以前读不了」这两句。`verified: doc-only` 指的就是这件事。
- **本文档没有 `## Procedure` / `## Before you begin` / `## Example` / `## Parameters` / `## Application` 段**——
  所以「怎么建组、怎么往空组里加节点」这类操作步骤**本篇根本没有**，
  「典型用法」那一节是**本页按正文的限定词拼的，不是文档给的流程**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`Group Name` 那一格的第二列只有一个光秃秃的 `256`**，没有单位、没有说明词
> （该格三列连起来是：属性名 `Group Name`、第二列 `256`、
> 第三列 `Names with more than 19 characters abbreviated. The name is displayed in the group graphic with the first and last 9 characters separated by three dots (...).`）。
> **本页不判定那个 `256` 就是「最长 256 字符」**——虽然把它和 `Group Comment` 那格的
> `(More than 2056 characters allowed)` 并排看很像一个长度上限
> （**这一步是推断**，依据只是这两个数出现在同一列）。
> ② **`Group Comment` 那格写的是 `(More than 2056 characters allowed)`**——
> **`More than` 字面是「多于」**，与同格的括号形式、以及 `Group Name` 那格的裸数字 `256` 放在一起，
> **读不出这一条到底是上限还是下限**。原文如此，**本页照录，不替它解释**。
> ③ **`Group Name` 的显示规则里有一处算不平的地方**：门槛写的是
> `Names with more than 19 characters abbreviated.`，而缩略形态写的是
> `the first and last 9 characters separated by three dots (...).`——
> **9 + 3 + 9 = 21 个字符，比触发缩略的那个 19 还长。**
> 两句话都在原文同一格里，**本页并列录出，不替它调和（§10）**。
> ④ **本篇没有坏字。** 实测全文 **0 处非 ASCII 字符**（没有 `鈥` / `渭` / `碌` 那一族）。
> **但这是「本页量过的」，判据是本篇这一个文件**；§11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上建过 group node，也没有勾过 `Group Bypass`**
（§11：文档里有 ≠ 这台机器上能用；尤其「跳过整组」与那条向后兼容限制，**动手前先照实机核对**）。
