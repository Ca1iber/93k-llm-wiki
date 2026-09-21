---
type: object
title: Assign Value node
layer: gui
stage: testflow
tags: [assign-value-node, testflow-node, testflow, variable-assignment, wizard, gui-node]
related: [testflow, testflow-variable, svlr, flow-control-node, group-node, print-node, smartest-6.3.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.03_Assign_Value_node.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Assign Value node

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Assign Value node 是 testflow 里的一个节点：在 testflow 的某个点上，把一个值赋给一个变量。**
本篇正文**只有这一句**，逐字：

> 「Use this node when you wish to assign a certain value to a variable at a point in your testflow.」

**这一句里有五个要素**，本页把能确定与不能确定的分开列：

| 要素 | 原文写法 | 本页能确定的 |
|---|---|---|
| 用途 | `assign a certain value to a variable` | **赋值：值 → 变量** |
| 位置 | `at a point in your testflow` | **它挂在 testflow 的某个点上**，不是独立运行的东西 |
| 何时用 | `Use this node when you wish to` ＋ 后半句 | **条件句**：想在这种情况下用它——**原文没有说「必须」用它** |
| 值 | `a certain value` | **只说「某个值」**；**值从哪来、什么形式，原文没说** |
| 变量 | `a variable` | **只说「一个变量」**；**变量属于谁、什么类型，原文没说** |

**⚠️ 这一篇的全部正文就是这一句。** 整篇 417 字符（含 frontmatter 与一条版本条目），
**二级标题只有一个 `## Functional changes`**。**所以本页后面的一切，都是这一句、一个图片文件名、
一条版本条目推出来的；推不出来的地方一律写「语料未写」。**

### 界面：唯一的线索是图名，正文一个字都没提界面

**正文没有提向导、没有提窗口、没有提字段。** 唯一的界面线索是图片的 alt 文本，逐字：

`  ![New Assign Value Node Wizard window](<../../../../raw/110635.png>)`

——**图名说它是一个 `Wizard window`（向导窗口），名字是 `New Assign Value Node Wizard`。**

**（推断）这个节点是通过一个向导加进 testflow 的**——
**依据只是这个图片名里的 `Wizard` 一词与 `New` 一词**；
**正文没有一个字提「向导」或「新建」这个动作。图本身本页没看**（见 `## 出处`）。

**还要分清两件事**：本篇标题是 **`Assign Value node`**（节点），
图名是 **`New Assign Value Node Wizard`**（**新建它的向导**）——
**一个是节点、一个是加节点用的向导，原文没有一句话把两者连起来。**

### 语料未写的六件事

**这一篇里查不到下面任何一项**（**每一项都是本页查过全篇之后的结论，不是本页没找**）：

| 问题 | 状态 |
|---|---|
| 是哪个域的变量？ | **语料未写**——原文只写 `a variable`（是不是 testflow 变量、还是别处的变量，没说） |
| 值能是什么？ | **语料未写**——只写 `a certain value`（常量？表达式？别的节点的输出？都没说） |
| 一个节点能赋几个值？ | **语料未写** |
| 什么时候执行？ | **语料未写**——只写 `at a point in your testflow`，**「点」怎么定义没说** |
| 加进去之前有什么前置？ | **语料未写**——本篇没有 `## Before you begin`，也没有 `## Procedure` |
| 会报什么错？ | **语料未写**——本篇没有 `## Errors` / `## Warnings`，也没有 `## Application` |

**本篇也没有 `Subtopics`、没有 `## Related information`**——
**所以本节点的父页、兄弟节点、相关文档，本篇一个名字都没给。**

### 一条只能靠读法得到的判断

**原文那句的主句是 `Use this node when you wish to`，不是 `This node assigns`。**
**（推断）这是「什么时候该用它」的写法，不是「它做什么」的定义句**——
**依据是 `Use` ＋ `when you wish to` 这个句式本身**；
**所以本页标题里那句「把一个值赋给一个变量」是这句话的转述，
原文真正的主句是 `use this node`。本页不做更强的断言。**

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## Example`。**
**全篇唯一带「用法」性质的信息就是那句以 `Use this node when you wish to` 开头的条件句，
不是步骤。** 所以本节**给不出步骤**，只有一条条件：

| 什么时候用（原文条件） | 结果 | 原文给的步骤 |
|---|---|---|
| 你想 **在 testflow 的某个点上**把一个值赋给一个变量 | 在那个点上用这个节点 | **原文没给**（`## Procedure` 不存在） |

**能落成的两条，两条都带「未写」：**

- **位置**：`at a point in your testflow`。
  **（推断）节点的插入位置就是赋值发生的位置**——**依据只是 `at a point` 这个介词短语**；
  **节点的位置与 testflow 的执行顺序是什么关系，原文没说。**
- **入口**：**（推断）`New Assign Value Node Wizard`**——
  依据是图片 alt 里的图名（见上），**正文没提向导**。

**本页明确给不出的一条**：**怎么把它加进 testflow、加进去之后在编辑里长什么样、怎么改它**——
**语料未写。** 本篇能回答的只有「它在什么场合下用」。

## 和谁有关

- [[testflow]] — **原文唯一的定位词**：赋值发生在 `at a point in your testflow`
  ——**本节点是 testflow 的一部分，不是独立工具**。
  **本页只有这一句；testflow 是什么、怎么跑，在那一页，本页没读。**
- [[testflow-variable]] — **（推断）赋值的宾语**。本篇只写 `a variable`，
  **没有写 `testflow variable`**；**（推断）它指的很可能就是 testflow 的变量**——
  **依据只是「赋值发生在 testflow 的某个点上」与那个页名**。
  **本页没有那一页的任何事实。**
- [[svlr]] — **（推断）同一个赋值的「命令侧」，但这条不是本篇 raw 里的话**。
  **依据是本次补页的工作单（`extract/.batch/8.txt`）写着「`svlr` 在 testflow 侧挂的就是这个节点」**
  ——**本页查过：本篇 raw 里 `svlr` 出现 0 次。**
  **所以「命令侧 ↔ testflow 侧」这个配对在本页是推断 + 工作单的说法，不是文档事实**；
  **`svlr` 自己做什么在那一页，本页没读、也没有去核实。**
- [[flow-control-node]] / [[group-node]] / [[print-node]] — **（推断）名字同族**
  （都以 `node` 结尾），**本篇 raw 一个字都没提它们**，
  **依据只是页名。本页不判它们与本节点同不同层、是不是同一批。**
- [[smartest-6.3.2]] — **版本页**，本页 `## 版本` 唯一的落点。
- `New Assign Value Node Wizard`（**未建**）— **图片名里的那个向导**；
  **正文没提它，所以它是不是一个独立的界面/工具，本页判不了**（见 `## 出处` ②）。

## 版本

原文 `## Functional changes` **只有一条**，逐字：

- Introduced before SmarTest 6.3.2

**这是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以这个节点成立于哪个版本，这一篇里没有。**

**版本段里没有别的条目**，而**本篇正文也只有一句**——
**所以这个节点在 6.3.2 之后有没有改过，语料里没有依据。**

**与 wiki 目标版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**而这一篇一个字都没有提 7.x**——**所以本页只能确认「6.3.2 之前就有」，
不能确认它在 7.10.3 上的样子。**

详见 [[smartest-6.3.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.03_Assign_Value_node.md`

**本页没做的：**

- **可读的只有一篇文章，而它只有一句正文。** 本篇 417 字符（含 frontmatter 与
  `## Functional changes`）——**本页的全部文档事实就是：一句正文、一个图片 alt、
  一条版本条目。** **所以本页反复写「语料未写」，不是本页偷懒，
  是这一篇的规模就只有这么大。**
- **唯一的图没看**（`raw/110635.png`，图名 `New Assign Value Node Wizard window`）。
  **§11.4 说 raw 里的图可读、且该读**——**而这一篇关于界面的全部信息就在这一张图里**：
  **本页只知道它叫「向导窗口」，不知道向导里有几个字段、字段叫什么、有没有默认值。**
  **这是本页最大的空缺。**
- **[[svlr]] 没读** —— 工作单提示的那个「命令侧 ↔ testflow 侧」配对（见 `## 和谁有关`）
  **本页没有去那一篇核实**，**所以那条在本页只是推断 + 工作单的说法。**
- **没有读父页，也没有读任何兄弟节点文档。** 本篇 raw 里**没有 `Subtopics`、
  没有 `## Related information`**——**本页因此也没有去别处找它的父页与兄弟节点**：
  **这个节点在 testflow 的组件里排第几、和别的节点是什么关系，本页一个字都没有。**
- **没有打开过 testflow 编辑器，也没有实机验证。** `verified: doc-only`——
  **向导长什么样、赋值在实机上怎么生效，本页只有文档依据。**
- **没有交叉验证任何别处的文档**（§11）。**本页唯一一处引自本篇以外的依据是工作单
  （`extract/.batch/8.txt`），已在正文明确标明那不是本篇 raw 里的话。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 正文与图名的信息量不对称：正文没提「向导」，图名里却有两个正文没有的词。**
> 正文逐字：`Use this node when you wish to assign a certain value to a variable at a point in your testflow.`
> 图名逐字：`![New Assign Value Node Wizard window](<../../../../raw/110635.png>)`
> ——**正文一个字都没有 `Wizard`、没有 `New`、没有 `window`。**
> **本页照实并列两处，不替正文补「用向导新建」这句话。**
>
> **② 本篇的二级标题只有一个。** 全篇结构是：一句正文 → 一张图 → `## Functional changes`。
> **没有 `## Subtopics`、没有 `## Related information`、没有 `## Procedure`、
> 没有 `## Before you begin`、没有 `## Application`、没有 `## Errors` / `## Warnings`。**
> **这一条不是缺点，是事实**——**它决定了本页能写的东西的上限**。
>
> **③ 图片那一行行首有两个空格。** 逐字（**注意开头两个空格**）：
> `  ![New Assign Value Node Wizard window](<../../../../raw/110635.png>)`
> ——**行首缩进两个空格，在 markdown 里像是某个列表项的续行**，
> **而它前面是空行、后面是空行，本篇没有任何列表。** **本页引文照原样。**
>
> **④ `node` 三处都是小写，前后一致。** 逐字三处：
> `title: "Assign Value node"` / `# Assign Value node` /
> 文件名 `02.08.04.32.01.02.03_Assign_Value_node.md`
> ——**三处都写小写 `node`，没有一处写成 `Node`。**
> **本页照录，不替它统一大小写，也不据此改本页的 `title`。**
>
> **⑤ 正文用 `certain` 而不是 `specified` / `given` 一类的词。** 逐字：
> `assign a certain value to a variable` ——**「某一个值」的措辞是原文的**；
> **本页不替它解释这个 `certain` 是「随便哪个」还是「特定的那个」。**
>
> **⑥ 本篇没有 §11.2 ① 那种编码损坏。** **本页通读过这一篇，`[一-鿿]` 字符 0 处。**

`verified: doc-only`
