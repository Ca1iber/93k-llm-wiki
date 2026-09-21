---
type: object
title: FLUSH
layer: L2
stage: run
tags: [flush, flsh, l2, test-method-api, setup-flush, spec-value, routing-status, debugging, firmware-buffer]
related: [run, mapping-run, flsh, aprm, primary-status, timing-spec, level-spec, spec-tool, spec-search, sequencer-status, connect, sqst]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# FLUSH

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,085 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void FLUSH();
void FLUSH(const TM::FLUSH_POST_ACTION action);
void FLUSH(bool force);
void FLUSH(TM::FLUSH_POST_ACTION action, bool force);
void FLUSH(TM::FLUSH_SECTION_TYPE flush_section);
void FLUSH(bool force, TM::FLUSH_SECTION_TYPE flush_section);
void FLUSH(TM::FLUSH_POST_ACTION action, bool force, TM::FLUSH_SECTION_TYPE flush_section);
```

Parameters
 | action |

This parameter controls how the setup data will be downloaded to the hardware.

You can leave it empty or use TM::APRM.

When using the TM:APRM option, the command `APRM`（raw: `../02.06_Command_Reference/02.06.02.02.03_APRM_-__Activate_PRiMary_sets.md`） with mode set to CNL will be issued following the normal FLUSH() actions.

 |
 | force |

When to execute the firmware command `FLSH`（raw: `../02.06_Command_Reference/02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`） and `WSDN`（raw: `../02.06_Command_Reference/02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md`）. It can be:

-

true: always executes the firmware command `FLSH`（raw: `../02.06_Command_Reference/02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`） and `WSDN`（raw: `../02.06_Command_Reference/02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md`） (default)

-

false: only executes the firmware command `FLSH`（raw: `../02.06_Command_Reference/02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`） and `WSDN`（raw: `../02.06_Command_Reference/02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md`） when necessary.

 |
 | flush_section  | This parameter allows you to set which types of APIs to flush.You can use the following options:

- TM::FLUSH_PRIMARY`1)`（raw: `#fntarg_1`）,
- TM::FLUSH_UTIL`2)`（raw: `#fntarg_2`）,
- TM::FLUSH_ALL,
 or a combination hereof. |

This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/MapiFuncs.h.

### Example

### TM::FLUSH_PRIMARY / UTIL

```
Routing.util("UTI1").on();
Primary.getLevelSpec().change("S_VCC", 4.45);
FLUSH(TM::FLUSH_PRIMARY | TM::FLUSH_UTIL);
```

  Alternatively:

```
TM::FLUSH_SECTION_TYPE flushType;
flushType = TM::FLUSH_UTIL | TM::FLUSH_PRIMARY;

Routing.util("UTI1").on();
Primary.getLevelSpec().change("S_VCC", 4.45);
FLUSH(flushType);
```

<!-- 语法节 end -->

## 是什么

**`FLUSH()` 是 test method 里那条「把缓冲区里的设置真正刷下去」的 API。**
它**不产生任何新设置**，只负责**把你已经改过的东西推下去**——推多远，看改的是哪一类东西。
`layer: L2` / `stage: run`。

**先把最容易混的一条说清：`FLUSH` 不是 `FLSH`。**
`FLUSH` 是 test method 的 C++ API（本页，`02.07.04.01.69`）；
`FLSH` 是固件层的命令（`02.06.02.02.124`，[[flsh]]，**未建**）。
**两者是两层上的两个东西**，本页的 `force` 参数决定要不要执行 `FLSH`——
**「FLUSH 会调 FLSH」这句话只对一半，另一半是「不一定每次都调」。**
（[[mapping-run]] 把这两条分列在主表的同一行里：**L1 格写 `[[flsh]]`、L2 格写 `[[flush]]`**——
本页与那个口径一致。）

### 它推的是**两段**，而且两段的目的地不同（本页最要紧的一条）

原文 `## Introduction` 用两句话把两段分开写。第一段：

> 「This API reflects the changes specified by the following APIs to the setup data or hardware:」

第二段：

> 「And also, this reflects the changes specified by the following APIs to the MCD (firmware level), but does not reflect them to the hardware:」

两段各带一张清单，并起来就是这张表：

| 你改的是 | `FLUSH()` 把它送到哪 | 依据 |
|---|---|---|
| `ROUTING_STATUS` | **setup data 或硬件**（原文 `to the setup data or hardware`） | 第一段 |
| `PRIMARY_STATUS`、`TIMING_SPEC` / `LEVEL_SPEC` / `SPECIFICATION` | **只到 MCD（固件层）**——**原文明说 `but does not reflect them to the hardware`** | 第二段 |

**这条差别是「我改了 spec 值、也 FLUSH 了，怎么硬件还没变」的答案**：
改 spec 值之后 `FLUSH()`，**值到了固件层，但没到硬件**。要到硬件，得等下一节那批 API 之一被执行。

### 大多数情况下你**不用**自己调它（原文明说）

> 「The operation of the FLUSH API is contained in the behavior of the EXECUTE_TEST, START_TEST, DIGITAL_CAPTURE_TEST, and NB_DIGITAL_CAPTURE_START APIs. Therefore, in most cases, you do not need to call this API. Mainly, this API is used for debugging your test method program.」

**四个 API 的行为里已经含了 FLUSH**，所以 `FLUSH()` 的定位是**调试工具**，不是搭流程的积木。

### 「到硬件」这件事发生在哪些 API 上——**清单分两类**

> 「The changes specified by the PRIMARY_STATUS, TIMING_SPEC, LEVEL_SPEC, and SPECIFICATION are actually reflected to the hardware when any of the following APIs is executed. For more information, see PRIMARY_STATUS - (Primary).」

清单 11 条，**原文的写法本身就是两类**：

| 类 | 原文条目 | 读出来 |
|---|---|---|
| **自己就含 FLUSH** | `EXECUTE_TEST` / `START_TEST` / `DIGITAL_CAPTURE_TEST` / `NB_DIGITAL_CAPTURE_START` / `FUNCTIONAL_TEST` | 调它就行，FLUSH 是它的一部分 |
| **要你先 FLUSH** | `FLUSH then SPEC_SEARCH (execute() member function)`、`FLUSH then SEQUENCER_STATUS (run() member function)`、`FLUSH then PMU_IFVM (execute() member function)`、`FLUSH then PMU_VFIM (execute() member function)`、`FLUSH then TASK_LIST (execute() member function)`、`FLUSH then DPS_VFIM (execute() member function)` | **两步，顺序不能反** |

**第二类的写法逐字就是 `FLUSH then X`**——**「先 FLUSH、再 X」要你自己按顺序做**，
六个 API 各配一个 `member function` 括号注（`execute()` 或 `run()`）。

**这条「两类」的读法是本页把上面两段并起来得出的（推断），依据是清单里那六个条目字面上的 `FLUSH then` 与前一段那句 `The operation of the FLUSH API is contained in the behavior of`。**

### 三个参数各管什么

| 参数 | 取值 | 含义 |
|---|---|---|
| `action` | 留空 / `TM::APRM` | **控制 setup data 怎么下载到硬件**。传 `TM::APRM` 时，**在正常 FLUSH 动作之后会再发一条 `APRM`（模式 `CNL`）** |
| `force` | `true`（**默认**）/ `false` | **要不要执行 `FLSH` 与 `WSDN` 这两条固件命令**：`true` 总是执行；`false` **只在必要时**执行 |
| `flush_section` | `TM::FLUSH_PRIMARY` / `TM::FLUSH_UTIL` / `TM::FLUSH_ALL`，或它们的组合 | **刷哪几类 API**（逐项见下） |

**`flush_section` 的两项原文用脚注列了清单**（脚注在原文里被折算进 `## Functional changes`，见「出处」⑤）：

| 取值 | 刷掉的是 |
|---|---|
| `TM::FLUSH_PRIMARY` | `Primary Sets` / `Timing Spec` / `Specification Level` / `Spec Sequencer` / `Definition changes` |
| `TM::FLUSH_UTIL` | `Utility Purpose control` / `Utility line control` |

**`force` 那一条是「为什么有时快有时慢」的答案**：`false` 时那两条固件命令**只在必要时才发**。
参数表里还写明了这个 API 的定义位置：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/MapiFuncs.h.」

### 三条应用注意（`## Application note` 里最实用的三段）

**① 要刷 utility line，sequencer 与所有 analog module 都得先停。**

> 「In order for the FLUSH API (or an API that internally executes the FLUSH API) to reflect the changes that are specified by ROUTING_STATUS to utility lines, the sequencers must be halted.」

> 「(No FLUSH is required for the trigger() / abort() / getXXXX() / isRunning() member functions in ROUTING_STATUS.)」

> 「The following are the corresponding member functions, for which all analog modules (AWGs/DGTs/Samplers) must be halted when the FLUSH API is executed.」

下面逐字是那四个成员函数：

> 「- Routing.primary(), Routing.pin(), Routing.util(), Routing.uti_purpose()」

拆成「条件 → 结果」：

| 情况 | 要不要先停 |
|---|---|
| 要刷的是 `ROUTING_STATUS` 里的 **utility line** | **sequencer 必须先停** |
| 调的是 `Routing.primary()` / `Routing.pin()` / `Routing.util()` / `Routing.uti_purpose()` | **所有 analog module（AWG / DGT / Sampler）都必须停** |
| 调的是 `trigger()` / `abort()` / `getXXXX()` / `isRunning()` | **原文：`No FLUSH is required`** |

**最后那一行是豁免清单**——**这四个成员函数不用 FLUSH**，是本页最容易被漏掉的一条。

**② 改 spec 值时的调用次数，看的是「改的是不是同一个变量」。**

> 「When using the `FLUSH(TM::APRM)` option, if your application is changing the same spec variable, it must be called after each change command.」

> 「However, If your application is changing different spec variables, the `FLUSH(TM::APRM)` only needs to be called once at the last line.」

| 你在改 | `FLUSH(TM::APRM)` 要调几次 |
|---|---|
| **同一个** spec 变量 | **每一条 change 命令之后都要调** |
| **不同的** spec 变量 | **只在最后一行调一次** |

（上面第二句里 **`However, If`** 的 `If` 是大写——**原文如此**，见「出处」③。）

**③ `FLUSH()` 必须和它要刷的东西在同一个作用域里——调晚了会报错。**

> 「Note FLUSH() should be called before elements which should be "flushed" get out of scope. For example, if the elements to be flushed are declared inside an "if{}" block, then FLUSH() must also be declared within the same block. Otherwise, placing the FLUSH() outside the block will cause a FLUSH() error to occur.」

**这不是「早点调更好」，是「调晚了会出错」**——原文的措辞是 `will cause a FLUSH() error to occur`。

### 一条副作用：`FTCG` 的 keep alive 端口 + `FLUSH(TM::APRM)` 会**强制关时钟**

> 「Note If keep alive ports are set via the FTCG command and FLUSH(TM::APRM) (Command FLSH) is executed, the following message will be issued in case of updating the clock:」

消息逐字如下（原文放在代码块里、第二行带缩进，**本页按 `schema.md` §11.1① 把空白折叠成一行**）：

> 「FTCG ON was specified for at least one port which cannot be retained unchanged now. The command "Flush" forces a clock off, resulting in a stop of all channels.」

**后果写在消息里：`forces a clock off, resulting in a stop of all channels`——所有通道停止。**
这正好对上版本记录里 7.1.4 那一条（**主时钟关掉时 analog module 的硬件访问不到，会报错并显示在 report window 里**）。
原文为这件事另指了两篇（`Suppressing Reactivation of Primary Sets with FTCG` 与本页在讲 master clock 时点的
[[sqst]] / [[connect]]）——**那三篇本页都没读**。

### 一条边界：这条 API 与「落盘」无关

`FLUSH()` 刷的是**缓冲区里的运行期状态**，**不是文件**。原文没有任何一句提到文件或保存——
**「改完怎么存下来」不在本页**。（[[mapping-run]] 的「文件」列在第 7 行是 `—`，
理由它自己给了：`02.06.02.02.124` 明说被缓冲的是 MCD 里的状态，不是文件。）

## 典型用法

原文 `## Example` 给的就是一个最小可用序列，**两步：先改、再 FLUSH**：

```
Routing.util("UTI1").on();
Primary.getLevelSpec().change("S_VCC", 4.45);
FLUSH(TM::FLUSH_PRIMARY | TM::FLUSH_UTIL);
```

它后面还有**同一件事的另一种写法**（把组合先存进一个变量）：

```
TM::FLUSH_SECTION_TYPE flushType;
flushType = TM::FLUSH_UTIL | TM::FLUSH_PRIMARY;

Routing.util("UTI1").on();
Primary.getLevelSpec().change("S_VCC", 4.45);
FLUSH(flushType);
```

**两段合起来说明两件事**：① 顺序是「改设置 → FLUSH」，FLUSH 在最后；
② **`flush_section` 是一个位组合（`|`）**，两种写法等价。

| 想干什么 | 怎么做 | 依据 |
|---|---|---|
| 改了 utility line，要它生效 | 停 sequencer → 改 → `FLUSH()`（刷 `FLUSH_UTIL`） | `## Application note` |
| 改了 primary set / timing spec / level spec | 改 → `FLUSH()`（刷 `FLUSH_PRIMARY`）——**但它只到固件层** | `## Introduction` 第二段 |
| 想让它**真的到硬件** | 再执行上面那 11 个 API 之一（含 FLUSH 的那四个，或 `FLUSH then X` 的两步） | 那条 11 项清单 |
| 调试时改了 spec 值，想立刻看到 | `FLUSH()`；**也可以直接用 Spec Tool 改** | `## Application note`（`During debugging, you can also change the spec values with the Spec Tool.`） |
| 在 `if {}` 里改的东西 | **`FLUSH()` 也必须写在同一个块里** | 那条 `Note` |

**三条顺序上的提醒（推断，依据都是本页引过的原文）：**

- **`Routing.util()` / `Routing.pin()` / `Routing.primary()` / `Routing.uti_purpose()` 之前，先把 sequencer 和所有 analog module 停掉**——不停就 FLUSH 是 `## Application note` 明写的反例。
- **`force` 默认是 `true`**：不改它，每次 `FLUSH()` 都会发 `FLSH` + `WSDN`。
  要省这两条固件命令得**显式传 `false`**，而且 `false` 的语义是「必要时才发」，
  **不是「永远不发」**。
- **`FLUSH(TM::APRM)` 是唯一会触发 `APRM`（模式 `CNL`）的那个选项**——
  **`FTCG` 的 keep alive 端口 + 它 = 强制关时钟**（上面那条副作用）。

## 和谁有关

- [[run]] / [[mapping-run]] — **本页的 stage 页与同阶段对照表页。**
  [[mapping-run]] 主表第 7 行「把缓冲的设置真正刷到硬件（调试用）」**L1 格是 [[flsh]]、L2 格就是本页**
  ——**同一行里两条东西分列两格**，本页与它口径一致；它还把那一行的「文件」格判成 `—`。
- [[flsh ]] — **L1 那条固件命令，与本页只差一个字母，是另一件东西。**
  本页 `force` 参数决定要不要执行它；名字出现在 `extract/dangling.csv` 里
  （3 处引用：`mapping-run` / `mapping-testmethod` / `run`）——**那页迟早要建**，
  **本页不替它写内容**（它的参数、返回值本页一个字没有）。
- [[aprm]] — `TM::APRM` 对应的固件命令。原文说传 `TM::APRM` 时会在正常 FLUSH 动作之后发一条
  `APRM`（模式 `CNL`）。**那页本页没读。**
- [[primary-status]] — 原文点名 `PRIMARY_STATUS` 的改动「靠 FLUSH 反映到固件层」，
  并把 `PRIMARY_STATUS - (Primary)` 那篇指为细节所在。**那篇本页没读。**
- [[timing-spec]] / [[level-spec]] — **用它们的成员函数改 spec 值时，改动是在 FLUSH 被调用的那一刻反映到 spec 数据上的**；要到硬件还得等那批 API。**两页本页都没读。**
- [[spec-tool]] — **调试期改 spec 值的另一个入口**，原文与 FLUSH 并列提了一次。
  **那页本页没读。**
- [[spec-search]] / [[sequencer-status]] — 六个 `FLUSH then X` 里的两个
  （原文写作 `SPEC_SEARCH` / `SEQUENCER_STATUS`）。**两页本页都没读**，
  所以**「先 FLUSH 再调它」为什么必须分两步，本页答不了。**
- [[sqst]] / [[connect]] — 原文讲「激活 master clock」时指了这两篇；**它们与那条「强制关时钟」的副作用是同一个话题**。**两页本页都没读。**
- **只写反引号、不写链接的那些名字**：`WSDN`、`FTCG`、`FUNCTIONAL_TEST`、`NB_DIGITAL_CAPTURE_START`、
  `PMU_IFVM`、`PMU_VFIM`、`TASK_LIST`、`DPS_VFIM`、`ROUTING_STATUS`、`LEVEL_SPEC`、`SPECIFICATION`
  ——**它们都不在 `extract/prose-allowlist.txt` 里**，所以按 §9.1 一律反引号 + raw 路径。

## 版本

本文档**有** `## Functional changes` 段，4 条，逐条照录：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.3: Support of MBAV8+`
- `SmarTest 7.1.4: HW of analog modules cannot be accessed when the master clock is switched off. An error is issued and the message is displayed in the report window.`
- `SmarTest 7.6.1: Added parameter flush_section`

**第一条是哨兵值，不是「6.3.2 的变更」。** 按 `schema.md` §11.2②，
`Introduced before` 这一整类说法的意思是「**在本文档集覆盖范围开始之前就已经有了**」——
**照字面读会读成「6.3.2 新增了 FLUSH」，那是错的。**

**后三条各钉住本页一块内容：**

| 版本 | 原文条目 | 落在本页哪一处 |
|---|---|---|
| **7.6.1** | `Added parameter flush_section` | **第三个参数的来历**——所以上面那张 `TM::FLUSH_PRIMARY` / `FLUSH_UTIL` 表**在 7.6.1 之前不存在**；语法节里前五个重载**都不带 `flush_section`** |
| **7.1.4** | `HW of analog modules cannot be accessed when the master clock is switched off. An error is issued and the message is displayed in the report window.` | **那条「`FTCG` + `FLUSH(TM::APRM)` 强制关时钟」的副作用**——两处讲的是同一件事的两面 |
| 7.1.3 | `Support of MBAV8+` | **本页正文里没有任何一处能接住它**——`MBAV8+` 在本篇只出现这一次，本页不知道它是什么（**语料未写**） |

**同批条目也收在 `wiki/versions/` 的 [[smartest-7.1.3]] / [[smartest-7.1.4]] / [[smartest-7.6.1]] 三页里**
——**那三页不是本页建的**，这里只指路。

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.md`
  （TDC `29338.htm`，7,420 字节 / 154 行）。
- **本篇没有重复投放**：全语料按 `source_topic` 查 `29338.htm`，**只有这一个文件**。
- **本页「语法 / 参数」节的来源就是这一篇自己**（节首没写「取自子主题」后缀），
  节里那 2,085 字符包括 7 个重载的 `Syntax` 块、`Parameters` 表、以及那个 `## Example` 的两个代码块。

### 本页读的图：**0 张，因为这一篇一张图都没有**

**实测该篇对 `raw/` 的图片引用 0 处**（`grep -o 'raw/[0-9]*\.\(png\|jpg\)'` 零命中）。
**这不是「图够不着」，是这一篇本来就不带图**——所以本页**没有任何来自图的结论**，
也没有任何一处需要标「④ 图证」。

### 本页没做的

- **`## Related information` 指的那一篇没读**：`Working with FLUSH()`
  （`03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.04.01`）
  ——**「怎么用 FLUSH 省测试时间」这个正面用法，本页一个字没有**。
- **原文点到名的命令 / API 页一篇没读**：`FLSH`（`02.06.02.02.124`）、`WSDN`（`.341`）、
  `APRM`（`02.06.02.02.03`）、`FTCG`（`.125`）、`PRIMARY_STATUS`（`02.07.04.01.167`）、
  `SPEC_SEARCH`、`SEQUENCER_STATUS`、`PMU_IFVM`、`PMU_VFIM`、`TASK_LIST`、`DPS_VFIM`、
  [[sqst]]、[[connect]]。**它们的参数、返回值、错误行为本页一个字没有**——
  本页只有「FLUSH 与它们的关系」这一层。
- **`Suppressing Reactivation of Primary Sets with FTCG`（`03.03.04.04.01`）没读**——
  所以**「怎么避免那条强制关时钟」本页答不了**。
- **`MBAV8+` 是什么没查**（它在本篇只出现一次，在版本记录里）。
- **没有实跑。** 没有写过调用 `FLUSH()` 的 test method、没有在机台上刷过任何设置、
  没有触发过那条 `FTCG` 消息。**`verified: doc-only` 指的就是这件事**——
  「这台机器上 `force=false` 到底什么时候才发 `FLSH`」本页一句都不能保证。
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[run]] 那页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 一处少一个冒号：`TM:APRM`（第 88 行）。**

> 「When using the TM:APRM option, the command APRM with mode set to CNL will be issued following the normal FLUSH() actions.」

**`TM:APRM` 应为 `TM::APRM`**——同一篇第 86 行写的是 `You can leave it empty or use TM::APRM.`，
**冒号是两个**。**引文里原样保留**；本页正文的参数表里那一格是**转述**（写的是 `TM::APRM`，没引这一句），
所以那处坏拼写只活在这条瑕疵记录里。

**② 一处句号后缺空格：`to flush.You`（第 104 行）。**

> 「This parameter allows you to set which types of APIs to flush.You can use the following options:」

**`flush.` 与 `You` 之间没有空格。** 本页正文没有引用这一句。

**③ 一处句中的大写：`However, If`（第 65 行）。**

> 「However, If your application is changing different spec variables, the `FLUSH(TM::APRM)` only needs to be called once at the last line.」

**逗号之后的 `If` 不应大写。原文如此，引文里原样保留**（本页正文引了这一句）。

**④ 一处缺标点：`Note FLUSH()`（第 67 行）。**

> 「Note FLUSH() should be called before elements which should be "flushed" get out of scope.」

**`Note` 后面既没有冒号也没有句号，直接接 `FLUSH()`。**
（`pattern-explorer` 那篇里有同型的粘连 `edit bursts.Note`，**两处不是同一个文件，是同一类毛病**。）

**⑤ `## Functional changes` 段吞掉了文末的脚注块（第 144–155 行）。**
这正是 `schema.md` §11.2③ 记的那一类（全语料 171 篇）：原文的脚注定义 `[1]` / `[2]`
连同它们的两串清单挂在文件最后，而这一节按模板顺序正好是最后一个 `## ` 段，于是被算了进来。
**具体到本页**：本页「语法 / 参数」节里 `flush_section` 那一行写着
`TM::FLUSH_PRIMARY`1)`（raw: `#fntarg_1`）与 `TM::FLUSH_UTIL`2)`（raw: `#fntarg_2`）——
**这两个上标标记指向的脚注正文，就在这个被吞掉的块里**（本页已在上面把两串清单抄成表）。
语料结构如此，**不是脚本 bug**（`versions.py` 遇脚注定义行即截断）。

**⑥ 本页这一篇没有编码坏字（§11.2① 那一族）。** 用 `[一-鿿]` 实测零命中
——对照 §11.2① 的全语料 1,053 / 9,398 篇含坏字，**本篇属于没有的那一批**。
**这不是「没找到」，是查过、结果为零。**

**⑦ 本篇没有 §11.2⑤ 那个整词替换（`DC/DC power units`）**，实测 0 命中。
**但本篇里确实有一族 `TM::` 前缀的标识符**（`TM::FLUSH_POST_ACTION` / `TM::FLUSH_SECTION_TYPE` /
`TM::FLUSH_PRIMARY` / `TM::FLUSH_UTIL` / `TM::FLUSH_ALL` / `TM::APRM`）——
**它们是标识符，抄进代码块前照抄即可；本条只在提醒：这一类前缀密集的地方最容易看漏 ① 那种少一个冒号的错。**

`verified: doc-only`
