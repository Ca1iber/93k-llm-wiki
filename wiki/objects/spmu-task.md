---
type: object
title: SPMU_TASK
layer: L2
stage: testmethod
tags: [testmethod, dc-test, spmu, pmu, badc, dc-scale, task-handle, legacy-name, parallel-measurement]
related: [dc-test-programming, offline-result-emulation, spmu-pin-task, spmu-pin-task-mode, dps-task]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# SPMU_TASK

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **798 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
SPMU_TASK();
```

Creates an object to define different conditions for DC measurements and to execute them concurrently.

Note Do not create static objects of the class in the test method and do not create test method member variables from this class. List of parameters There are no parameters. Return value The constructor has no return value.

### Example

```
//DC Current Measurement
SPMU_TASK spmuTask;

ON_FIRST_INVOCATION_BEGIN();

 spmuTask.pin("pmu1").mode("VFIM").vForce(2000 mV).clamp(200000 uA, 200000 uA).min(-200000 uA)
 .max(200000 uA).vForceRange(6500 mV).iForceRange(1000000 uA).compare("I").samples(100).settling(1 ms)
 .relay("NT").execMode("SER");

 spmuTask.preAction("NPRM").execMode(TM::PVAL).execute();

ON_FIRST_INVOCATION_END();
double measuredValue = spmuTask.getValue("pmu1");
```

<!-- 语法节 end -->

## 是什么

**`SPMU_TASK` 是 DC 测量的「任务句柄」**：一个对象代表一批**并行**跑的 DC 测量，
测量条件按 pin 一条条挂上去，最后统一执行、统一取结果。本篇第一句给的是它的**两条硬件路径**：

> 「Defines and executes parallel DC measurements with the DC Scale card in PMU mode or the BADC
> of digital cards.」

**即：DC Scale 卡的 PMU 模式，或数字卡上的板级 ADC（BADC）。**

### ⚠️ 名字是遗留名，7.10 上不再支持 System PMU

这是本篇最值钱的一句，逐字：

> 「The name SPMU_TASK is a legacy name. SmarTest 7.10 does not support the High Precision PMU
> (System PMU).」

**别把 `SPMU` 读成「System PMU 还在」**：本 wiki 面向 **SmarTest 7.10.3**，
而这一篇明说 **7.10 不支持 High Precision PMU（System PMU）**。类名留着，
**实际走的是上面那两条路径**。
**语料只给了这一句否定式**——「那 7.10 上 `SPMU_TASK` 具体驱动哪块硬件」它**没有正面说明**，
本页不补。

### 它是「执行者」，per-pin 的条件在另一个类里

本篇把二者的分工写成了一句：

> 「If used with SPMU_PIN_TASK the relays settings required for a measurement can be altered.」

**这一句只说「一起用时能改 relay 设置」**。`pin()` 返回什么类型、per-pin 条件容器怎么构造，
**本篇一个字没写**——那一半在 `SPMU_PIN_TASK` 那一篇里
（raw: `02.07.04.01.234.01_SPMU_PIN_TASK.md`），**本页没读它**。

### 和 `TASK_LIST` 的关系，也只有一句

> 「In conjunction with TASK_LIST multiple DC measurements can be defined to be executed in a
> sequence.」

**「把多个 DC 测量排成顺序执行」这件事靠 `TASK_LIST`**，不靠本类。
`TASK_LIST` 的接口不在本页 sources 里（raw: `02.07.04.01.240_TASK_LIST.md`）。

### 构造：无参数、无返回值，且不能当静态对象 / 成员变量

> 「Creates an object to define different conditions for DC measurements and to execute them
> concurrently.」

> 「Do not create static objects of the class in the test method and do not create test method
> member variables from this class. List of parameters There are no parameters. Return value
> The constructor has no return value.」

**三条硬事实**：① 不能在 test method 里建**静态**对象；② 不能建类**成员变量**；
③ 构造函数**无参数、无返回值**。
最后那句里其实塞了三节（`List of parameters` / `Return value` 都没有段标记，是裸词行）——
**这是原文的结构，不是本页的转写**（见 `## 出处` ③）。

### 头文件

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/SpmuTask.h.」

### 九个 `Subtopics`，八个是本类的成员

本篇的 `Subtopics` 一节逐条列了 **9 条**：8 个 `SPMU_TASK.*` 成员 + `SPMU_PIN_TASK` 本身。

| 成员（`Subtopics` 逐个列出） | 在本篇里出现过的地方 |
|---|---|
| `pin()` | 例子里 `spmuTask.pin("pmu1")`；**签名与返回值本篇没写** |
| `execMode()` | 例子出现**两次**，两种写法：`execMode("SER")` 与 `execMode(TM::PVAL)` |
| `preAction()` | `spmuTask.preAction("NPRM")` |
| `execute()` | `spmuTask.preAction("NPRM").execMode(TM::PVAL).execute();` |
| `getValue()` | `double measuredValue = spmuTask.getValue("pmu1");` |
| `setup()` | **只在清单里出现过**，本篇正文一句说明都没有 |
| `getPassFail()` | **只在清单里出现过** |
| `getFunctionalResult()` | **只在清单里出现过** |

**每个成员的参数、返回值、报错条件，都在它们各自的专页里**（`Subtopics` 给的就是那 8 个链接）；
**本页一篇没读**。

## 典型用法

**本篇只有一个 `## Example`，没有 `## Procedure`、没有 `## Before you begin`。**
例子（逐字在语法节里）的**骨架**是六步：

| 步 | 代码 | 要点 |
|---|---|---|
| 1 | `SPMU_TASK spmuTask;` | 对象建在 **`ON_FIRST_INVOCATION` 块外** |
| 2 | `ON_FIRST_INVOCATION_BEGIN();` | 配置与执行都包在块里 |
| 3 | `spmuTask.pin("pmu1").mode("VFIM").vForce(2000 mV)…` | **一条链配完一个 pin**，链上有 12 个成员（`clamp` / `min` / `max` / `vForceRange` / `iForceRange` / `compare` / `samples` / `settling` / `relay` / `execMode`） |
| 4 | `spmuTask.preAction("NPRM").execMode(TM::PVAL).execute();` | **执行另起一条语句**，也带 `execMode()` |
| 5 | `ON_FIRST_INVOCATION_END();` | |
| 6 | `double measuredValue = spmuTask.getValue("pmu1");` | **取结果在块外** |

**从这一个例子能读出五条：**

| 读出来的 | 依据 |
|---|---|
| 配置阶段**全是链式调用**，一条语句配完一个 pin | 例子第 3 步就是一整条语句 |
| `execMode()` **有字符串与枚举两种写法** | 同一例子里 `execMode("SER")` 与 `execMode(TM::PVAL)` 并存 |
| 「配置」与「执行」是**两步** | 先 `execMode("SER")`（配），再 `preAction("NPRM")…execute()`（跑） |
| **取结果在 `ON_FIRST_INVOCATION_END()` 之后** | 例子最后两行的顺序 |
| 例子注释自称 `//DC Current Measurement`，模式参数写的是 `"VFIM"` | **本篇没有解释 `"VFIM"` 是什么意思**（选项清单在 `SPMU_PIN_TASK.mode()` 那一篇里，本页没读） |

**例子里出现了五处字符串取值（`"VFIM"` / `"SER"` / `"NPRM"` / `"NT"` / `compare("I")` 的 `"I"`），
本篇一处都没有解释它们。** 这是覆盖范围的边界，不是本页的省略。

## 和谁有关

- `SPMU_PIN_TASK`（raw: `02.07.04.01.234.01_SPMU_PIN_TASK.md`）— **per-pin 条件容器，本类 `pin()` 的对象**。
  两篇文档编号相邻（`.234` / `.234.01`），`Subtopics` 里它排在第一位。
  **本篇只给了「一起用时能改 relay 设置」半句**（引文在 `## 是什么`）；
  **它的构造方式、38 个成员、两个例子都在那一篇里。本页没读那一篇。**
- `TASK_LIST`（raw: `02.07.04.01.240_TASK_LIST.md`）— **顺序执行的组合器**。
  本篇只给了「`In conjunction with TASK_LIST …`」那一句。**本页没读它。**
- `DPS_TASK`（raw: `02.07.04.01.50_DPS_TASK.md`）— **（推断）同族的另一个任务句柄**。
  依据：wiki 里它与本页同层同阶段，且**成员清单的形状相同**
  （都是 `pin()` + `execute()` + `getValue()` / `getPassFail()` / `getFunctionalResult()`）。
  **本篇一句话都没有提到它**；**本页没有它的任何事实**。
- [[dc-test-programming]] / [[offline-result-emulation]] — **原文 `## Related information` 的两个链接**
  （这两个名字**粘在同一行、中间没有分隔符**）。
  前者是 DC 测试编程入口，后者是离线结果仿真。**本页没读这两篇**，
  所以「本页与离线仿真怎么配合」本页答不出。
- [[spmu-pin-task-mode]] — **（推断）例子里第一个成员 `mode()` 的专页**。
  依据：例子的链以 `mode("VFIM")` 开头，而 wiki 里有 `SPMU_PIN_TASK.mode()` 一页。
  **本篇没有链接到它，本页也没有它的事实。**
- 8 个成员页（`SPMU_TASK.execMode()` / `.execute()` / `.getFunctionalResult()` / `.getPassFail()` /
  `.getValue()` / `.pin()` / `.preAction()` / `.setup()`；raw 路径见本篇 `Subtopics`）—
  **本页一篇没读**，所以上面那张表只有「名字」和「例子里怎么调」两列。
- **上面这些名字里，`SPMU_TASK` / `SPMU_PIN_TASK` / `TASK_LIST` / `spmu-task` / `spmu-pin-task` / `dps-task`
  都不在 `extract/prose-allowlist.txt` 里**，所以本页**只能写成反引号 + raw 路径，不能写成 `[[ ]]`**（§9.1）。
  **这是清单的现状，不是本页的选择**——同样的处理见 `wiki/mappings/mapping-testmethod.md` 的 ⑩。

## 版本

**本篇有 `## Functional changes` 段，只有一条：**

> 「- Introduced before SmarTest 6.3.2」

**这一条是 §11.2 ② 的哨兵值，不是「6.3.2 新增了 `SPMU_TASK`」。**
它的意思是「**早于本文档集覆盖范围开始之前就已经有了**」。
所以本页能确定的只有「6.3.2 之前就存在」，**具体哪个版本引入的，这份语料里没有**。

**本篇没有第二条版本记录。** 从 6.3.2 到本 wiki 面向的 **7.10.3**，
这一篇**没有记过 `SPMU_TASK` 的任何变更**——**这是「本篇没记」，不是「没发生过」**。

## 出处

`sources:` **一篇**：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md`
（TDC `55670.htm`，2,477 字节，64 行——**本批五篇里最短的一篇**）。
**整篇读完**（65 行全读）。

**本页没做的：**

- **`## 语法 / 参数` 节一个字没改**（§4）。里面 `### Syntax` / `### Example` 两段的层级、
  以及语料内部链接改写成 `` `文本`（raw: `路径`） ``——**都是 `extract/objscaffold.py` 干的，本页只读不改。**
- **九个 `Subtopics` 目标一篇没读**（8 个成员页 + `SPMU_PIN_TASK`）。
  **所以 `pin()` 的签名、`execMode()` 的取值表、`getValue()` 返回什么单位，本页一个字都没有**——
  本页只有「名字在清单里」和「例子怎么调」。
- **`TASK_LIST` 没读**，所以「多个 DC 测量怎么串起来顺序执行」只有原文那半句。
- **`DC Test Programming` / `Offline Result Emulation` 两篇没读**，那两条链接只证明
  「本篇认为读者该去看它们」，**不证明它们讲了什么**。
- **没有读任何别的 02.07 文档来补本页与 `SPMU_PIN_TASK` / `DPS_TASK` 的关系**（§11）。
  本页**没有断言 `pin()` 返回什么、也没有断言两个类是不是同一个族的**。
- **一张图都没有。** 本篇 raw 里 `![` / `.png` / `.jpg` **命中 0**（我数过），
  **上游 `raw/55670.htm` 里 `<img>` 也是 0 个**。**所以本页没有任何来自图的结论**——
  **这不是「图够不着」，是这一篇没有图**（§11.4 ①）。
- **没有实跑**：没有建过 `SPMU_TASK` 对象，没有在机台上跑过这个例子。`verified: doc-only` 指的就是这件事。

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改：**

> **① `the relays settings`——名词复数当了定语。** 逐字：
> `If used with SPMU_PIN_TASK the relays settings required for a measurement can be altered.`
> ——读作 `the relay settings` 才通。**本页正文照原样引。**

> **② `## Related information` 的两个链接粘在一起**，中间没有任何分隔符：
> `DC Test Programming` 紧跟 `Offline Result Emulation`。
> 同一批语料里 `SPMU_PIN_TASK.mode()` 那一篇有**完全相同**的毛病（那里是三个链接），
> **是这批文档的通病，不是本页的错。**

> **③ 两节被压进一行。** 逐字：
> `List of parameters There are no parameters. Return value The constructor has no return value.`
> ——`List of parameters` / `Return value` **都没有段标记**（不是 `##` / `###`，是裸词行），
> **所以脚本只能把它们当正文收进语法节**。**这是原文的结构问题，不是脚本的错。**

> **④ `Note` 后面一律没有分隔符**，本篇两处逐字开头：
> `Note Do not create static objects of the class …`、`Note The name SPMU_TASK is a legacy name.`

> **⑤ 本篇没有 §11.2 ① 那种编码坏字，也没有 §11.2 ⑤ 那种整词替换。** 两条都实测过：
> 汉字 `[一-鿿]` **0 行命中**；`DC/DC power units`（`Index` 被替换出来的那串）**0 命中**。

> **⑥ 例子里五个字符串取值一个都没解释**（`"VFIM"` / `"SER"` / `"NPRM"` / `"NT"` / `"I"`）。
> 这不算错字，但**是这一篇最主要的空白**——照它抄代码必须去翻成员页。

`verified: doc-only`
