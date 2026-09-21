---
type: object
title: The sequencer program
layer: L1
stage: pattern
tags: [sequencer, sqpg, pattern, label, vector, cycle, instruction, port, parallel-vector]
related: [sequencer-status, sqst, pattern, timing, level, vector-setup-file]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01.03_The_sequencer_program.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# The sequencer program

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**sequencer program 是「一个 label 里的向量生成脚本」。** 原文第一句就给了它的能力清单：

> 「Sequencer programs are coded in a simple language that provides
> - instructions for sending waveforms to the DUT
> - instructions for changing the timing or level setup during the test
> - control structures that allow to repeat a sequence of instructions and to call a subroutine.」

**三件事：送波形、测试中途改 timing/level setup、重复与调用子程序。**
**它是一个语言，不是一张表**——所以有指令、有命令号、有控制结构。

**⚠️ 「改 timing 或 level setup」的具体指令是哪几条，本文档没有点名——语料未写。**
本页只写本文档真写出来的那五条指令（见下）。

**每一个 label 一个 program，一行一条指令，指令用 `SQPG` 命令建。**
（原文：`Every line of the program contains an instruction for the sequencers.
The instructions are created with the SQPG command.`）

### 原文用来讲解的整段程序（**逐字**）

原文说它 `belongs to label test_1 of the standard example`：

```
SQPG 4,STVA,408,,,(@)
SQPG 5,STSA,,,,(@)
SQPG 6,RPTV,7,5,,(@)
SQPG 7,GENV,9,,,(@)
SQPG 8,STOP,,,,(@)
```

> **这段程序是本页唯一的代码，但它**没有**进「语法 / 参数」节**——
> 因为它落在散文里，上面没有 `Syntax` / `Example` 这类**段标记**。
> **想看它在原位置的样子，得回 raw。**（见「出处」）

### `SQPG` 一行的六个字段

| 位置 | 原文怎么说 |
|---|---|
| **第 1 个** | **`The first parameter of SQPG specifies the command number of the instruction.`** |
| **第 2–4 个** | `The next three parameters define the instruction and its input information.` |
| **第 5 个** | **`The fifth parameter is not used.`** |
| **第 6 个（最后一个）** | **`The last parameter specifies the port to which the label belongs.`** |

**第 1 个字段的命令号是本页最容易读错的一处**：

> 「The command numbers count the instructions of one port (the default port in the example) across
> all sequencer programs (see Label definition, sequencer program, and sequencer area). The first
> line of the sample program has command number 4 because this is not the first program of the port.
> Note that the first and last command number are those specified in the SQLB definition of the label
> (see The label definition).」

**即：命令号是「按 port 跨所有 program 累积」的，不是「本 program 里的第几行」。**
**所以上面这段程序从 `4` 开始**（它不是该 port 的第一个 program），
**而它是第几号，是 `SQLB` 定义 label 时指定的。**

> **这解释了一个初学者常撞的现象**：**一个新建的 label 里第一行写 `SQPG 1,...` 还是
> `SQPG 4,...`，取决于这个 port 上前面已经有多少条指令**——**不是随便写的**。

**最后一个字段的 port**：例子里的 `(@)` 原文解释为
`The sample program belongs to the default port @, which contains all configured pins.`

### 五条指令，各自是什么意思

| 指令 | 原文要点 |
|---|---|
| **`STVA`** | **`points to the location of the physical waveform DC/DC power units for the label test_1`**；**`The sequencer program of every label that generates parallel vectors must start with an STVA instruction.`** |
| **`STSA`** | **`is only present for historical reasons.`**——**没有任何功能，白写的** |
| **`RPTV`** | **`generates 7 vectors and repeats this action 5 times`** |
| **`GENV`** | **`generates 9 vectors`** |
| **`STOP`** | **`marks the end of the program.`** |

**两条硬结论：**

1. **凡是生成 parallel vector 的 label，程序必须以 `STVA` 开头。**（原文 `must start with`）
2. **`STSA` 是历史遗留**——**见到它不用研究它，它不干活。**

### 指令的 **length** 是「从几行 index 生出来」

> 「The number of index rows from which these vectors are generated is called the length of the
> instruction. Thus, the RPTV instruction has length 7, and the GENV instruction has length 9.」

**`length` = 参与生成这批向量的 index 行数。** 这是原文唯一给出的 length 定义。

### **vector 和 cycle 不是一回事**（本页第二个最容易混的地方）

`RPTV` 会把同一批向量重复送多次，于是原文说：

> 「Therefore, a distinction must be made between vectors and cycles.
> A vector is a sequence of waveforms whose DC/DC power units are stored as a row in the index array.
> A cycle is one of possibly many applications of the same vector to the DUT.」

| 概念 | 定义（原文） | 数出来的结果 |
|---|---|---|
| **vector** | **`a sequence of waveforms whose DC/DC power units are stored as a row in the index array`** | **由 index array 的行决定**——**RPTV 这条只对应 7 行** |
| **cycle** | **`one of possibly many applications of the same vector to the DUT`** | **同一批向量每送一次就是一个 cycle** |

**例子给了数**：

> 「Thus the first vector of the example label will be applied 5 times to the DUT with the cycle
> numbers 0, 7, 14, 21, 28 (cycles are counted per label starting from 0).」

**读法：第一个 vector 被用了 5 次，对应 5 个 cycle 号 `0` / `7` / `14` / `21` / `28`。**
**每一步跳 `7`——正好是 `RPTV` 的 length 7**（推断：原文只并列了「length 7」与「步长 7」这两个数，
**没有说因果关系**；但两个数一致）。
**另外：`cycles are counted per label starting from 0`——cycle 号是**按 label** 从 0 数的。**

> **一句话记法：`vector` 是「长什么样」，`cycle` 是「第几次送出去」。**
> **所以 `RPTV` 那一条程序里，vector 只有 7 个，cycle 有 35 个**
> （推断：7 个 vector × 重复 5 次 = 35；**原文没有把 35 这个数写出来，
> 它只写了第一个 vector 的 5 个 cycle 号**）。

## 典型用法

**1. 读一个 label 的 sequencer program 的顺序**（本文档给出的结构，按原文的讲解顺序）：

**看 `SQLB` 定义的起始/结束命令号** → **按命令号逐行看 `SQPG`** →
**第一行必须是 `STVA`**（生成 parallel vector 的 label）→
**中间的生成指令看它的 length 与重复次数** → **末行 `STOP`**。

**2. 写一条生成指令时要定的三件事**（从 `RPTV` 那一行读出来的）：

| 定什么 | 在哪个字段 | 例（`SQPG 6,RPTV,7,5,,(@)`） |
|---|---|---|
| **命令号** | 第 1 个 | `6` |
| **指令** | 第 2 个 | `RPTV` |
| **生成几行 / 重复几次** | 第 3–4 个 | `7` 行、重复 `5` 次 |
| **第 5 个** | — | **留空（`The fifth parameter is not used.`）** |
| **哪个 port** | 最后一个 | `(@)` |

**3. 要判断「这一段究竟送了几次」**：**先把 vector 数与 cycle 数分开**——
**`RPTV` 的 length 是 vector 数，重复次数才是 cycle 的倍数。** 依据是上面 vector/cycle 那两段。

**4. 见到 `STSA` 不要改动它**：**原文说它 `only present for historical reasons`**——
**它既不是错也不是功能，删它不在本文档的授权范围内。**

**5. 本文档没给的**：**怎么改 timing / level setup、怎么写子程序调用**——
原文只在开头的能力清单里提了这两件事，**后面用来说明的那段例子里没有它们，也没给指令名。
语料未写。**

## 和谁有关

**同一件事的两个时间尺度（本页是「静态的那份」）**：

- [[sequencer-status]] — **它是「运行时怎么控制」的那一半**：`run()` / `stopCycle()` /
  `abort()` / 各状态。
  **本页是「程序里写了什么」，它是「跑起来之后停在哪、还在不在跑」。**
  **两页都由 pattern 这一阶段管**（本页 `stage: pattern`，那页也是 `stage: pattern`）。
  **注意口径差别**：那页讲的是 L3 test method API，本页是 L1 的 `SQPG` 命令——
  **两层办的是同一件事的两面。**

**firmware 侧的邻居（同为 `stage: pattern` 的 L1 命令）**：

- [[sqst]] — `SQST` 是 sequencer 的 **state** 命令。
  **本页的 `SQPG` 是「写程序」，`SQST` 是「问状态 / 控制运行」**——
  **两者都在 L1 的命令层，本页只立这一组对照，`SQST` 的具体语义本页没读。**

**上游 / 归属**：

- [[pattern]] — **阶段页**。sequencer program **属于某个 label**，
  而 label 属于 pattern；**本页是 pattern 阶段里「向量怎么生成」的那一环**。
- [[timing]] / [[level]] — 原文说这个语言能 `change the timing or level setup during the test`。
  **即：本页的程序可以在这两个阶段的设置中途改它们**——
  **但改的是哪几条指令、怎么改，本文档没写（语料未写），所以这两条关系只到「能力清单」这一层。**

**下游（本页只碰了一下）**：

- [[vector-setup-file]] — **向量数据本身的那一侧**。原文说 vector 是
  `a sequence of waveforms whose DC/DC power units are stored as a row in the index array`，
  **`index array` 是什么、怎么建，本页没有**（**那页本页也没读，这一条只作指向，不是断言**）。

**本文档点名、但本页没读的（均未建，不链）**：

- `Label definition, sequencer program, and sequencer area`（`02.06.07.01.02`）——
  **命令号「跨所有 sequencer program 累积」那条规则的出处**
- `The label definition`（`02.06.07.01.01.01`）——**`SQLB` 与命令号上下界在那儿**
- `Sequencer program and vector areas`（`02.06.07.01.03`）——**`STVA` 的详细解释在那儿**
  （**注意：链接文字与文件名不一致，见「出处」的 ⚠️**）
- `SQPG` / `SQLB` **两条命令自己的页**（**不在 allowlist 里，所以只用反引号**）——
  **本页讲的是「这两个命令产生的程序长什么样」，不是它们的参数表。**

## 版本

本文档有 `## Functional changes` 段，**全部内容一条**：

- **`Introduced before SmarTest 6.3.2`**

> **这一条是哨兵值，不是「6.3.2 的变更」。**
> 按 §11.2 ②，`Introduced before SmarTest 6.3.2` 的意思是
> 「**在本文档集覆盖范围开始之前就已经有了**」——全语料 2,677 条可用性行都是这个写法，
> **照字面读会得到「6.3.2 一口气新增了 2,677 个功能」这种格式齐整的假信息。**
>
> **所以本页的版本结论就一句话：本文档**没有**记录 sequencer program 的任何一次变更。**
> **本页不写任何 SmarTest 版本号。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.07.01.01.03_The_sequencer_program.md`
（raw 的 `source_topic: "96571.htm"`）。

**本页没做的**：

- **「语法 / 参数」节是空的，而原文里其实有一段代码。** 原因是**这篇文档没有任何段标记**：
  没有 `## Syntax`、没有 `## Parameters`、没有 `## Example`（参数讲在 `## Parameters of SQPG` 下，
  代码块直接跟在散文里）。**脚本按 §4 的规矩「没有段标记就不收录」，所以一个字都没收。**
  **本页正文把那段程序和 `SQPG` 的字段拆解写出来了，但那是我从散文里读出来重排的，
  不是脚本抽的。**
- **本文档点名的三篇一篇都没读**：`Label definition, sequencer program, and sequencer area`、
  `The label definition`、`Sequencer program and vector areas`。
  **所以：`SQLB` 的语法、命令号上下界怎么定、`STVA` 指向的到底是什么、`index array` 怎么建，
  本页一个字都没有**——**本页只转述了原文在讲到这几处时顺带写下的那几句。**
- **`SQPG` 与 `SQLB` 两条命令自己的参考页没读。**
  **这两个名字不在 allowlist 里，所以本页只用反引号写它们，没有链。**
- **「改 timing 或 level setup」的指令、「调用子程序」的控制结构，本文档一个都没给名字。**
  原文只在开头的能力清单里说有这两类东西，**后面再没提**。
  **本页照实写「语料未写」，不推测它们是哪些指令。**
- **没有任何图。** 本篇没有图片引用。
- **`the standard example` 是什么，本文档没有定义**（原文只用了这个说法，没说它在哪）。
  **本页不猜。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 原文用 `line N` 指代「命令号 N」，同一篇里又用 `the first line` 指「第一行」。**
> 逐字：
> `The STSA instruction in line 5 is only present for historical reasons.`
> `Finally, the STOP instruction in line 8 marks the end of the program.`
> —— **`STSA` 在示例程序的第**二**行、命令号 `5`；`STOP` 在第**五**行、命令号 `8`。
> 而同一篇前面写的是 `The first line of the sample program has command number 4`（用 `line` 指行）。
> 即：`line 5` / `line 8` 里的 `line` 指的是**命令号**，不是行号，**而同篇的 `first line` 指的是行**。
> **一处「line」两个意思，本页照实记，不替它统一。**
>
> **② 一处链接的文字与目标文件名不一致。** 逐字：
> `in more detail in [Sequencer program and vector areas](<02.06.07.01.03_Sequencer_areas_and_vector_areas.md>)`
> —— **链接文字是 `Sequencer program and vector areas`，
> 文件名却是 `..._Sequencer_areas_and_vector_areas.md`（少了 `program`）**。
> **本文档正文后面又用 `Sequencer areas and vector areas` 这个说法指同一篇，
> 即同一篇在同文档里有两种叫法。**
>
> **③ 「waveform DC/DC power units」这个说法本文档没定义。** 逐字：
> `The first line of the sample program contains the STVA instruction that points to the location
> of the physical waveform DC/DC power units for the label test_1.`
> 和 `A vector is a sequence of waveforms whose DC/DC power units are stored as a row in the index array.`
> —— **`waveform DC/DC power units` 是什么，本文档没解释**，本页也不解释。
>
> **④ 语法节的空节说明是脚本写的**，它说「跟着 `Subtopics` 找一层也没有」——
> **本篇 raw 里没有 `Subtopics` 段**，所以那句是本节的通用措辞，**不是本篇的事实**。
> **本页照实说明这一点，不改那一节。**

`verified: doc-only`
