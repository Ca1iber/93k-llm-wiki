---
type: object
title: Structure of an equation based level setup
layer: file
stage: level
tags: [level, level-file, equation-based, fixed-level, module-structure, spec-set, dps, file-format]
related: [level, equation-based-level-setup, level-master-file, level-equation-file, level-setup-tool, spec-tool, spec-set, dpspins-resources, mapping-level]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02_Structure_of_an_equation_based_level_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05_Data_Organization_of_Fixed_Levels.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Structure of an equation based level setup

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **417 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.01.04.02_Structure_of_an_equation_based_level_setup.md>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.03_Specs_module.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.06.01_Pin_exclusion.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Specs module）

```
SPECS
  vcc_level   [V]  # Base vcc voltage
  vcc_offset   [V]  # Offset to add to vcc_level
```

### Syntax（取自子主题 Level sets › Pin exclusion）

```
PINS <pin list> [-( <exclude pin list> )] [# comment]
```

Note You must type a blank between the left parenthesis and <exclude pin list> and a blank between <exclude pin list> and the right parenthesis.

### Example（取自子主题 Level sets › Pin exclusion）

```
LEVELSET 1 "normal"
PINS I_PINS -( i1+@diff ) # remove pair
vil=0
vih=4.3

PINS i1+@diff
vil=0
vih=3.3
```

<!-- 语法节 end -->

## 是什么

**本页是「一个 equation based level setup 由哪几块组成」的定义页。它不给写法。**

原文第一句就是本页的全部骨架：

> To enter the equation based level setup information you follow a modular approach when setting up a level equation set.

**这句里有两个词要说清**：`modular approach`（模块化）和 `level equation set`。
**本页只给了「模块化」这三个字，没给怎么模块化。**

### 一个 level equation set 由五块必需模块 + 一块 `plus` 组成

原文紧接着列清单，先导句逐字引：

> The required modules of a level equation set are:

**随后逐条列了五项，再用 `plus` 另加一项。下表按原文顺序转录——
六项名字之外的那一列是转述，不是引文**：

| 序 | 原文里的名字 | 本页知道什么 |
|---|---|---|
| 1 | `Equation set number` | **只有名字** |
| 2 | `Specs module` | 只有名字；**本页语法节里那个 `SPECS` 例子取自它的子主题** |
| 3 | `Equations module` | **只有名字** |
| 4 | `DPS module` | **只有名字** |
| 5 | `Level sets module` | 只有名字；**本页语法节里 `PINS` / `LEVELSET` 两个例子取自它的子主题** |
| + | `Spec Sets (defined in Spec Tool)` | 只有名字；**原文自己注明它定义在 Spec Tool 里**，不在这个文件里 |

**两块容易读错的地方：**

**① `plus` 后面那一条算不算「必需」，原文没写。**
它把 Spec Sets 放在「required modules」这段叙述里，用的连接词却是 `plus`。
**本页不判它是必需还是可选**（§10：并列记录，不替语料调和）。

**② 「模块名」和「关键字名」的对齐，本页读到的两篇原文一句都没写。**
（**上一版这里写的是「语料里一句都没有」——那是一条本页证不出来的全称否定，已收窄**：
本页只读了两篇，**没读那九篇子主题**，所以**「子主题里有没有写明这个对齐」本页不答**。）

**（推断 + ④ 图证）** `Specs module` 对应 `SPECS`、`Equations module` 对应 `EQUATIONS`、
`DPS module` 对应 `DPSPINS`、`Level sets module` 对应 `LEVELSET` 与 `PINS`。**两路依据：**

- **本页自己的语法节**里出现的三样东西——`SPECS` 块的例子、
  `PINS <pin list> [-( <exclude pin list> )] [# comment]` 的语法、`LEVELSET 1 "normal"` 的例子——
  段名分别写着「取自子主题 `Specs module`」和「取自子主题 `Level sets › Pin exclusion`」，
  **而正文的必需模块清单里正好有同名的两块**。
  **换句话说是「两边名字对得上」，不是「文档说它们是一回事」。**
- **`56944.png`（④ 图证）**：那个容器里竖排的四个方框，框上的字正是
  `SPECS` / `EQUATIONS` / `DPSPINS` / `LEVELSET`。**强度与上一条不同**——
  **图是并排摆放，它没有用一个字解释这个对应**；
  但**上一版写着「在本页语法节里没有对应物」的 `Equations module` 与 `DPS module`，在图中是有的**
  （上一版因此说「对它们一个字都不推」，**这一句被图改掉了**）。

（[[mapping-level]] 的对照表按 `SPECS` / `LEVELSET` / `DPSPINS` 分块——
**那是那一页的证据，本页不搬、不替它背书。**）

### 原文的「结构」在那张图上——**这张图本页读了**（④ 图证）

原文最后一句：

> The figure below illustrates the structure of an equation based level setup.

**结构本身在 `56944.png` 里**（alt 文字 `Level Setup Process`，23,961 字节）。
raw 第 34 行就是它：`  ![Level Setup Process](<../../../../raw/56944.png>)`。
**本页读了这张图**——路径解析到 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\56944.png`，
**就在语料树里**（§11.4：md 往上四层正好是 `tdc-html/`）。

**图上读到的东西逐条列在下面（④ 图证）。它们一律不进 `>` 引文块**——
`>` 的含义是「这段能在 raw 文本里搜到」，**而图上这些字在 raw 文本里一个都搜不到**（核对见本节末）。

| 图上看到的 | 内容 |
|---|---|
| 左半边标题 | `Level Equation Editor` |
| 左半边顶上那一叠方框 | `LEVEL EQN SET n`（后）、一个被压住只露出上沿的同名方框、`LEVEL EQN SET 1`（前） |
| `LEVEL EQN SET 1` 容器里的竖排方框（自上而下） | `SPECS`、`EQUATIONS`、`DPSPINS`、`LEVELSET 1`、`…`、`LEVELSET k` |
| `SPECS` 框里 | `<spec 1>`、`<spec 2>`、`…`、`<spec k>`；框右侧一行斜体注 `Spec declaration` |
| 右半边标题 | `Level Spec Tool` |
| 右半边副题 | `Spec Sets defined for LEVEL EQN SET 1` |
| 右半边的方框 | `LEVEL SPEC SET 11`、`LEVEL SPEC SET 12`、`…`、`LEVEL SPEC SET 1n` |
| 每个 `LEVEL SPEC SET` 旁括号里的值 | `11`：`4.5V / 0.5V / … / 5V`；`12`：`4.5V / 0.2V / … / 5.5V`；`1n`：`2.5V / 2.0V / … / 4.5V`（形状都是 `<spec i> = <值>`） |
| 两个半边之间 | 一个绿椭圆写着 `Select a Spec Set`，**箭头从 `SPECS` 指到 `LEVEL SPEC SET 12`** |
| 右半边底部斜体 | `A spec set assigns values to the specs declared in the LEVEL EQN SET` |

**「这五块怎么拼、谁包着谁、嵌套关系是什么」——图答了，答法是这四条（④ 图证）：**

1. **`LEVEL EQN SET` 是最外层的容器**，而它自己可以有好几份（图上那一叠方框）。
2. **正文那几块模块是容器里竖排的方框，彼此平级、不互相嵌套**——
   **图上没有任何一块画在另一块里面**；`LEVELSET 1` … `LEVELSET k` 是**同一层上的多份并列**。
3. **`Spec Sets` 不在这个容器里，在另一个工具里**（右半边 `Level Spec Tool`），
   而且**按 EQN SET 归属**（副题写着 `defined for LEVEL EQN SET 1`）——
   **一个 EQN SET 对多个 spec set**（`11` 一直到 `1n`）。
4. **两块之间的接口是「选一个 spec set」**（那个绿椭圆），
   底部那句斜体给出了这个接口的语义：**`SPECS` 那一块只声明、不给值，值由 spec set 赋。**

**图上与正文对不上的一处，照实记**：正文把 `Equation set number` 列为一个必需模块，
**而图上它不是容器里的一个方框**——图上只有整叠容器上的 `LEVEL EQN SET n` 这种标识。
**「编号是容器的标识而不是内部模块」是本页对图的读法，图自己没有一个字解释**（§11：这一句算推断那一侧）。

**「模块名 ↔ 关键字名」这张图也摆出来了**：容器里那四个方框上的字正是
`SPECS` / `EQUATIONS` / `DPSPINS` / `LEVELSET`，与正文清单的
`Specs module` / `Equations module` / `DPS module` / `Level sets module` 对得上
（**是并排摆放，不是一句话**；与上面 ② 那条合起来看）。

**这张图上的字，哪些搜得到、哪些搜不到（本页逐串核过）**：

| 串 | raw 文本里 |
|---|---|
| `LEVEL EQN SET`、`LEVEL SPEC SET`、`Select a Spec Set`、`Spec Sets defined for`、`Spec declaration`、`A spec set assigns values` | **0 命中——只存在于图里** |
| `Level Equation Editor`、`Level Spec Tool`、`DPSPINS`、`SPECS`、`EQUATIONS`、`LEVELSET` | **搜得到**（它们是语料里的工具名与关键字写法）——**搜不到的是这张图把它们摆成的那个结构** |

**一个搜索陷阱，顺手记一笔**：拿 `LEVELSET k` 去 grep **会有命中**，
但命中它的那一行写的是 `LEVELSET keyword`（**grep 出来的位置在 `Level sets` 那篇子主题里，
本页没有读那一篇**），**命中的不是图上那个方框标签**。
**「搜到了」和「搜到的是同一件东西」是两回事。**

### 两条路线：本页的定义文档只管其中一条

`sources:` 的第二篇是 **fixed level setup 的定义页**。它的两句原文：

> For a fixed level setup, you use firmware commands to specify the level values as constants within every level set.

> The fixed level setup commands specify the required driver amplifier and receiver comparator voltage levels, set termination modes, load currents, or the clamp voltage. They also define the device power supply (DPS) voltage levels. You can set the levels for individual pins or for groups of pins previously defined by the DFGP command.

**逐点拆开**：

| 原文给的 | 内容 |
|---|---|
| fixed 怎么写 | **用固件命令**把 level 值写成**常量**，写在**每一个 level set 里面** |
| 这些命令管哪些东西 | ① 驱动放大器电平 ② 接收比较器电平 ③ 端接方式（`termination modes`）④ 负载电流（`load currents`）⑤ clamp 电压 |
| 还管什么 | **DPS 的电压 level**（`device power supply (DPS) voltage levels`） |
| 作用范围 | **单个 pin，或 `DFGP` 命令预先定义好的 pin 组** |

**这就是「两条路线」的第二处独立证据**（第一处在 [[mapping-level]]）：
**fixed = 文件里一行一条固件命令**，而 **equation based = 模块化的一整份 level equation set**。

**但要说清本页这两篇是「一边给全、一边给一半」**：

- **fixed 那一半给得很实**（它的两句话本页逐字引在上面，见上表五行）。
- **equation based 那一半只给了模块清单**——**第一篇一个字都没说它的 level 值是什么形态**
  （常量还是表达式？是不是命令序列？本页不知道）。
  **「整块搬运 / 是 `EQSP` 的参数」那句话的依据不在这两篇里**，
  在 `02.08.04.14.02_Equation_based_level_setup`（见 [[equation-based-level-setup]]），**本页不搬。**

**「两条互斥」这个说法，本页的依据只有一条（推断）**：第二篇的 `Note` 要读者**改走 equation based**
（原文那半句是 `We recommend using the Equation based level setup for all releases of SmarTest 7.2 or higher versions.`，见「典型用法」），
**这条建议的措辞默认了「二选一」**。**两篇里没有任何一句写「两者互斥」**——**本页据此与 [[mapping-level]] 保持一致，不写反。**

### 语法节的正确读法：**非空 ≠ 有完整参数**

本页 `## 语法 / 参数` 一节**不是空的**，里面有 `SPECS` 的例子、
`PINS <pin list> [-( <exclude pin list> )] [# comment]` 的语法、和 `LEVELSET 1 "normal"` 的例子。
**但三个段名全都带着「取自子主题」**：

| 语法节里的段 | 取自哪篇子主题 |
|---|---|
| `### Example`（`SPECS` 那段） | `Specs module` |
| `### Syntax`（`PINS` 那段） | `Level sets › Pin exclusion` |
| `### Example`（`LEVELSET` 那段） | `Level sets › Pin exclusion` |

**为什么脚本要走这一层**：**定义文档自己没有 `Syntax` / `Parameters` / `Example` 段**——
它的正文只有两句 + 一张图（见上）。**两件事要分开说**：

- **语法节非空，不等于「这就是 equation based level setup 的完整语法」。**
  它只覆盖 **9 篇子主题里的 2 篇**；`Equation set number and description`、
  `Mode context in level setup`、`Equations module`、`DPS module`、
  `IO PINS resources`、`Supported level resources`、`Spec sets` **七篇一篇都没进来**。
- **定义文档没有语法段，也不等于「这东西没有语法/没有参数」。**
  **语法全在 9 篇子主题里，脚本只抽到了 2 篇。**
- **那七篇是不是没有语法段，本页不知道**——**本页一篇子主题都没读**（见「出处」）。

**（推断）要找 equation based level setup 的完整语法，得回 raw 读那 9 篇子主题，本页不是那个地方。**
依据是本页语法节的段名分布。

## 典型用法

**两篇原文都没有 `## Procedure` / `## Before you begin` / `## What to do next` / `## Related information`。**
所以本节没有「步骤」可抄——**原文给的只有「按模块走」这一条**。

### 原文给的用法：一个顺序，没有细节

> To enter the equation based level setup information you follow a modular approach when setting up a level equation set.

**把这句话展开成做法，只有下面这张表；右列是本页实际知道的量**：

| 序 | 做什么 | 本页知道什么 |
|---|---|---|
| 1 | 定 equation set 的编号与描述 | **只有子主题名** |
| 2 | 写 Specs module | 知道它是必需模块之一 |
| 3 | 写 Equations module | 知道它是必需模块之一 |
| 4 | 写 DPS module | 知道它是必需模块之一 |
| 5 | 写 Level sets module | 知道它是必需模块之一 |
| + | 引 Spec Sets（在 Spec Tool 里定义） | **原文说它在 Spec Tool 里，不在这个文件里** |

**表中每一步的具体写法，本页一个字都给不出**——它们全在九篇子主题里，**本页一篇没读**。

### 一条文档给的迁移建议（**不是本页的建议**）

第二篇用一条 `Note` 把读者推向本页这条路：

> Note The support for fixed level setups is discontinued with SmarTest version 7.4.1T. We recommend using the Equation based level setup for all releases of SmarTest 7.2 or higher versions.

**拆成两条，都是文档事实**：

| 事实 | 内容 |
|---|---|
| **停用** | fixed level setup 的支持**自 SmarTest 7.4.1T 起 discontinued** |
| **建议** | **7.2 及以上所有版本都改用 equation based level setup**（原文是 `We recommend`——**这是文档给的建议，不是本页的**） |

**这句话在原文里挂着一个真链接**（`[Equation based level setup](<../02.08_Setup_and_Result_Tools/02.08.04.14.02_Equation_based_level_setup.md>)`）——
**即：fixed 路的定义文档自己链到了 equation based 的文档。** 见「和谁有关」。

### 阅读顺序（**推断**）

**原文没给子主题的阅读顺序**（`Subtopics` 只是一张列表，正文也没说先读哪篇）。
**本页按「必需模块」的次序推它**：`Equation set number and description` → `Specs module` →
`Equations module` → `DPS module` → `Level sets`，再接 `IO PINS resources` /
`Supported level resources` / `Spec sets` 三篇补充。
**`Mode context in level setup` 本页不知该放哪**——它不在正文的必需模块清单里。
**依据**：正文那句 `The required modules of a level equation set are:` 后面列出的次序。
**这是本页的推断，不是文档给的顺序。** **（④ 图证，只支持到「次序」这一步）**：
`56944.png` 里那四块在容器内的**竖排次序**正是 `SPECS` → `EQUATIONS` → `DPSPINS` → `LEVELSET`，
**与正文清单的次序一致**——**但图上没有说这是「阅读顺序」**，所以这一步仍然只是推断。

### 一条实机前必须知道的事

**第二篇那套固件命令，原文自己说它自 SmarTest 7.4.1T 起 discontinued，
并建议 7.2 以上一律改用 equation based。**
**本页不替它下「新程序不许用 / 旧程序还能不能跑」的结论**——
原文只写了 `discontinued` 和 `We recommend`，**这两条各自覆盖什么范围、
已经存在的 fixed level setup 会不会失效，原文一个字没写**（**语料未写**）。

## 和谁有关

### 上游 —— 本页挂在哪一章下

- [[command-reference]] — 本页的定义文档在 **Command Reference** 章（`02.06`）下。
  **这有点反直觉**：讲「一个文件的结构」的页，落在**命令**章里。
- **本页的定义文档是 `Data Organization of Equation Based Levels` 的子主题**——
  `extract/edges.jsonl` 里那条入边的 `link_text` 就是本页标题（`Structure of an equation based level setup`）。
- **它的对称篇就是本页的第二个 `source`**：`Data Organization of Fixed Levels`。
  **两条路线在语料的目录上成对出现**（`Data Organization of Equation Based Levels` ↔ `Data Organization of Fixed Levels`），
  **而本页这篇 `Structure of an equation based level setup` 是前者的子主题**。
  **这是与 [[mapping-level]] 那条「两条互斥路线」结论吻合的一处结构证据**（本页据此与它保持一致）。

### 替代关系 —— 同一件事的另一条路（**方向别读反**）

- `02.06.05.01.05_Data_Organization_of_Fixed_Levels`（本页第二个 `source`）**在正文里链到**
  `02.08.04.14.02_Equation_based_level_setup`（即 [[equation-based-level-setup]] 的源文档），
  理由是 **fixed 已停用、建议改用 equation based**。
  **边的方向是「fixed → equation based」**：**是 fixed 那一侧把读者推过来，不是反过来。**

### 同层 / 相邻

- [[level]] — 本页 `stage: level` 的理由：**它是 level 这一段的文件侧**。
  （**填的是「最近的一段」，不是「归属」**，§6。）
- [[level-file]] — **本页自己**。本页讲的是它「由哪几块组成」。
- [[equation-based-level-setup]] — **同一件事的定位页（concept）**。两页分工：
  **它讲「为什么 / 是什么做法」，本页讲「由哪几块组成」**。
  两页还有一个共同点：**各自的定义文档都没有语法段**，语法节都是脚本从子主题抽的。
- [[level-master-file]]（**未建**）/ [[level-equation-file]]（**未建**）——**文件层的同族**。
  **本页的模块清单和它们是什么关系，原文没写**，本页不知道。
- [[level-setup-tool]]（**未建**）—— GUI 侧的入口。**本页这两篇一个字没提工具。**
- [[spec-set]] — 原文那句 `Spec Sets (defined in Spec Tool)` 的落点。
- [[spec-tool]]（**未建**）—— **原文点名的唯一一个工具**：Spec Sets 定义在它里面。
- [[dpspins-resources]] — 必需模块里 `DPS module` 的资源清单落在那一页
  （**这条关系是 [[mapping-level]] 的证据表连的，本页没有独立依据**）。
- [[mapping-level]] — 同阶段的对照表页。**它的主表把 equation based 路线写成「整块搬运」、
  把 fixed 写成「命令序列」。本页两篇支持的是后半句**（fixed = 命令序列，逐字有依据），
  **前半句本页没有依据**——**本页不照抄、也不替它背书。**

### 本页没链的

- 本页定义文档的九篇子主题——`Equation set number and description` / `Mode context in level setup` /
  `Specs module` / `Equations module` / `DPS module` / `Level sets` /
  `IO PINS resources` / `Supported level resources` / `Spec sets` ——
  **全部未建，且本页一篇没读**，故只写反引号名（§9.1）。
- `DFGP` —— fixed 那一篇点名了它（`previously defined by the DFGP command`），
  **但原文没有给它链接**；本页不替语料补链，也不展开它。
- 那张图 `56944.png` —— **不是页**；**本页读了它**，结论在「是什么」那节的 ④ 图证里。

## 版本

**本文档没有 `## Functional changes` 段。**（**两篇都没有**——这是事实，不是缺陷：
两篇正文都只有两三段散文 + 一节 `Subtopics`，没有任何版本条目。）

**但第二篇的正文里有一条版本事实**——**它不是版本段里的条目，是散文句里的一截**：

| 版本 | 事实 |
|---|---|
| **SmarTest 7.4.1T** | **fixed level setup 的支持自这个版本起 discontinued** |
| **SmarTest 7.2 及以上** | **文档建议全部改用 equation based level setup** |

逐字引：

> Note The support for fixed level setups is discontinued with SmarTest version 7.4.1T. We recommend using the Equation based level setup for all releases of SmarTest 7.2 or higher versions.

**本页的定义文档（第一篇）没有任何版本信息**——它全文不提版本号。

**⚠️ 一处版本号写法不一致（照实记，不改）**：同一句里两个版本号写法不同——
`7.4.1T` **带 `T`**，`7.2` **不带**。
**本页不判哪个是笔误、也不改**（§11.2 ④ 记的正是「同一版本号跨产品线撞车」这一类问题）。

## 出处

`sources:` 两篇，**两篇都整篇读完**：

| # | 文件 | 规模 |
|---|---|---|
| 1 | `02_System_reference/02.06_Command_Reference/02.06.05.01.04.02_Structure_of_an_equation_based_level_setup.md` | 1,361 字节（TDC `56943.htm`） |
| 2 | `02_System_reference/02.06_Command_Reference/02.06.05.01.05_Data_Organization_of_Fixed_Levels.md` | 1,696 字节（TDC `56936.htm`） |

**本页没做的**：

- **九篇子主题一篇没读。** 所以 `Equation set number` / `Specs module` / `Equations module` /
  `DPS module` / `Level sets` / `IO PINS resources` / `Supported level resources` /
  `Spec sets` / `Mode context in level setup` 的**具体写法，本页一个字都没有**。
  **本页语法节里那三个片段是脚本从其中 2 篇抽的，本页没有复核过它们是否完整、有没有上下文缺失。**
- **`Specs module` 与 `Level sets › Pin exclusion` 两篇子主题没读**——
  **本页语法节的全部内容来自它们**，**本页无法复核**。
- **原文只有一张图，本页读了它。** `56944.png`，alt 文字 `Level Setup Process`，23,961 字节。
  raw 里它的路径是 `../../../../raw/56944.png`，**解析到
  `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\56944.png`——就在语料树里，取得到**（§11.4）。
  **上一版这三行写的是「爬到语料树之外 / 本页取不到 / 所以本页没有任何来自图的结论」，
  那句话是错的**：md 在 `tdc-html/agent-markdown/by-category/…` 下，**往上四层正好是 `tdc-html/`**，
  图就在 `tdc-html/raw/` 里，**而且读得出来**。
  **这一节因此按改判重写过**：结构结论现在全部来自这张图，逐条标在「是什么」那节的 ④ 图证里。
- **改判记录（上一版写了什么、为什么错）**：上一版说「本页没有任何来自图的结论」——
  **前提假、结论跟着假**。**现在这段话不成立了**：
  本页**读了**那张图，**「五块怎么拼」已经答了**；仍未答的只有**图与正文都没写的事**
  （例如各模块的具体写法——那在九篇子主题里，本页没读）。
- **没有实跑。** 没有生成过 level equation set、没有在 Level Setup Tool 里开过 equation based 的 level setup、
  没有在机台上验过任何一条。**也没有查过 SmarTest 7.10.3 上 fixed 路线到底还能不能用。**
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`、没有动 `extract/wiki-plan.csv`、没有跑 `verify_stages.py`、没有动别的页。**

**用了别页 / 别的数据的地方（都不作为本页的事实来源）**：

- [[mapping-level]] —— 只用来**对齐「两条互斥路线」的说法**，
  **本页没有从它搬任何事实**；凡本页没有依据的（equation based 侧的「整块搬运」），
  本页**标明「本页没有依据」**，不照抄。
- [[equation-based-level-setup]] —— 只用来**指路**（同一件事的定位页），**本页没有引它一个字**。
- `extract/edges.jsonl`（**元数据查询，不是读原文**）—— 本页用它确认了三件事：
  ① 第一篇的入边来自 `02.06.05.01.04_Data_Organization_of_Equation_Based_Levels`（`link_text` 即本页标题）；
  ② 第一篇的出边**全部**是它的九篇子主题；
  ③ 第二篇的出边是七篇子主题 **+ 一条指向 `02.08.04.14.02_Equation_based_level_setup` 的链接**（即 `Note` 里那条）。
- `extract/docs.jsonl`（**只查元数据字段，不读正文**）—— 用来确认「同名两篇」，见下 ⑤。

### ⚠️ 语料瑕疵（照实记下、一处都不替它改）

**① 本页这两篇一个坏字都没有——这是实测结果，不是没查。**
实测：两篇全文**没有任何非 ASCII 字符**。
`extract/encoding-map.csv` 里那一族（`碌` = µ、`渭` = μ、`卤` = ±、`鈥慴` = `‑b` 等）
**在本页一处都不出现**。**所以本页没有「坏字」可记。**

**② 正文的「必需模块」清单和 `Subtopics` 清单对不上（个数差）。**
正文说的是**五块必需 + 一块 `plus`**，`Subtopics` 列了**九篇**。
多出来的是（**本页转述，不是引文**）`Mode context in level setup`、`IO PINS resources`、
`Supported level resources` 三篇——**正文一个字都没提它们**。
**原文没说这三篇算不算「必需」，本页不判。**

**③ 同一件东西两种写法。** 正文写 `Level sets module`，`Subtopics` 写 `Level sets`——
**一个带 `module` 后缀、一个不带**。同类还有正文的 `Specs module`（`module`）
对上 `Spec Sets`（`Sets` 无 `module` 且大写 `S`）。
**原文如此，本页不改、不顺。**

**④ 一条 `Note` 标签与正文黏在一起。** 第二篇里那条停用声明在 raw 里以
` Note The support for fixed level setups is discontinued with SmarTest version 7.4.1T.` 开头——
**`Note` 这个词直接黏在句子开头**，它前面只有一个空格。本页引用时按 §11.1 ① 折叠了空白，**保留了 `Note` 本身**。
**（推断）「`Note` 不是正文的一部分、是转换时被并进来的标签」**——
依据是同类文档里 `Note` 一律是独立标签。**原文就是黏的，本页不替它切开。**

**⑤ 语料里有两篇同名的 `Structure of an equation based level setup`，不是同一篇的两个投放。**
一篇是本页的第一个 `source`（`02_System_reference/02.06_Command_Reference/` 下的那一篇，TDC `56943.htm`，1,361 字节），
另一篇在 `02_System_reference/02.08_Setup_and_Result_Tools/` 下（TDC `16878.htm`，2,643 字节）。
**判据**：`extract/docs.jsonl` 里两篇的 `source_topic` 不同（`56943.htm` / `16878.htm`），
而 §10 的「同源」判据要求 `source_topic` 去掉后缀后相同——
**所以这不是重复投放，是两篇不同的文档**（这一点与 [[mapping-level]]「对不上的地方」② 那批同源投放不是一回事）。
**为什么必须记**：[[mapping-level]] 的 `sources:` 里列的是 **`02.08` 那一份**，
**和本页的 `02.06` 那一份不是同一篇**；**「哪一份算这个标题的正本」，语料没有唯一答案。**
**本页只依据自己 `sources:` 里的 `02.06` 那一份，没有读 `02.08` 那一份的正文**，也不替它表态。

`verified: doc-only`
