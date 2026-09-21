---
type: concept
title: Flags
layer: n/a
stage: testflow
tags: [flag, testflow-tool, testflow-flag, test-suite-flag, site-control-flag, flag-priority, debugging, flow-control, smartest-6.3.2]
related: [testflow-tool, testflow, test-suite, site-control-window, controlling-multiple-sites, flags-page, alphabetical-list-of-flags, data-logging-profiles, flow-control-node, smartest-6.3.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07_Flags.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Flags

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **533 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07_Flags.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.06_Flag_priority.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Flag priority）

- If you set the pass level to 4 and the fail level to 2, then all test suites with test levels 2 and 3 will be set to fail, and all test suites with test levels 4 and above will be set to pass.
- If you set the test level of an individual test suite to 1 and then the Set pass level testflow flag to 1, this test suite will be set to pass each time it is executed. If, however, you activate the individual test suite flag Set fail, the test suite will always be set to fail, irrespective of its own test level or the testflow flags.

<!-- 语法节 end -->

## 是什么

**flag 是 Testflow Tool 里的一类「开关」：用来调试、以及控制一次测试的执行。**
**本篇（定义文档）只有一句定义、一张四类的名单，和一条优先级示例。**
原文的整个定义就是这一句（逐字）：

> 「The Testflow Tool provides four types of flags for debugging and controlling the execution of a test.」

**这一句给出三件事**：

| 格 | 原文 | 要点 |
|---|---|---|
| **谁提供** | `The Testflow Tool` | **提供方是 Testflow Tool**，不是固件、不是 API |
| **几类** | `four types of flags` | **四类**（名单见下） |
| **干什么用** | `for debugging and controlling the execution of a test` | **两个用途：调试 + 控制测试的执行** |

**⚠️ 这一句就是本篇的全部定义。** 它**没有说「一个 flag 是什么」**——
**没有说它是布尔量还是数值、值是 0/1 还是别的、在哪儿设、设了存在哪。**
**本页只能照它写的写，不给它补定义。**

### 四类，名单只有这四行

原文紧跟定义句给了一份清单（**逐字，四条各是一个链接**）：

| # | 类型（**原文的链接文字**） | 子主题文件（**原文的链接目标**） |
|---|---|---|
| 1 | `Testflow flags` | `02.08.04.32.01.02.07.02_Testflow_flags.md` |
| 2 | `Testflow flags for data logging` | `02.08.04.32.01.02.07.03_Testflow_flags_for_data_logging.md` |
| 3 | `Test suite flags` | `02.08.04.32.01.02.07.04_Test_suite_flags.md` |
| 4 | `Site control flags` | `02.08.04.32.01.02.07.05_Site_control_flags.md` |

**四类的名字分两层看**（**这是本页从名字上读出来的，原文没有解释命名**）：

| 作用域 | 类型 | 名字依据 |
|---|---|---|
| **整条 testflow** | 1、2 | 名字以 `Testflow` 开头 |
| **单个 test suite** | 3 | 名字以 `Test suite` 开头 |
| **站点** | 4 | 名字以 `Site control` 开头 |

**（推断）四类是「作用域从小到大」的两端对照**：
**testflow 级、test suite 级、site 级**——
**依据只有这四个名字本身**；**原文没有一句话说它们的作用域是什么，
也没有说它们之间谁覆盖谁**（**唯一沾到「谁盖谁」的是语法节里那条子主题示例，见下**）。

### 定义文档列了六条子主题，比「四类」多两条

原文在正文之前先给 `#### Subtopics`，**六条**（**逐字**）：

- `Alphabetical list of flags`（`02.08.04.32.01.02.07.01_…`）
- `Testflow flags`（`.02_…`）
- `Testflow flags for data logging`（`.03_…`）
- `Test suite flags`（`.04_…`）
- `Site control flags`（`.05_…`）
- `Flag priority`（`.06_…`）

**六条 = 四类 + 两条「不是类型」的页**：

| 多出来的两条 | 它是什么 |
|---|---|
| `Alphabetical list of flags` | **清单**——**逐个 flag 的名字与说明在那一页**（[[alphabetical-list-of-flags]] 已建）；**本页讲「flag 这个概念与分类」，不复制清单** |
| `Flag priority` | **优先级**——**它是「多条规矩」而不是「一种 flag」**；**语法节里那段逐字示例就来自它**（见下） |

**⚠️ 这四类在同一篇里出现了两次**：`#### Subtopics` 里一次（作为子主题），
定义句后面又一次（作为四类名单）。**两次的链接目标完全相同。**
**原文没有说明为什么重复；本页照实记，不替它合并。**

### 优先级：语法节里那两条（**来源是子主题 `Flag priority`**）

**语法节是脚本从子主题抄的**（它自己在段名里标了来源：`Flag priority`），
**那段示例给了 flag 之间「谁盖谁」的两条规矩**。逐字：

> 「If you set the pass level to 4 and the fail level to 2, then all test suites with test levels 2 and 3 will be set to fail, and all test suites with test levels 4 and above will be set to pass.」
> 「If you set the test level of an individual test suite to 1 and then the Set pass level testflow flag to 1, this test suite will be set to pass each time it is executed. If, however, you activate the individual test suite flag Set fail, the test suite will always be set to fail, irrespective of its own test level or the testflow flags.」

**第一条：pass level / fail level 是一条「按 test level 划段」的规矩**。

| 设定 | test level 落在哪 | 结果（**原文**） |
|---|---|---|
| `pass level = 4`、`fail level = 2` | 2 和 3 | `will be set to fail` |
| 同上 | 4 及以上 | `will be set to pass` |

**⚠️ 这一条里有一个缺口**：**pass level 是 4、fail level 是 2，
而 test level 落在「2 以下」（即 0 或 1）时是什么结果，原文没有说。**
**（推断）从「2 和 3 判 fail、4 及以上判 pass」这两段是连续的看，
1 以下大概率也在 fail 那一段**——**但原文没有写，所以这是推断，不是文档事实。**

**第二条：两层之间，**个体压过流程**。** 逐字拆开是两句话：

| 情形 | 结果（**原文**） |
|---|---|
| test level = `1` **且** 打开 testflow flag `Set pass level` = `1` | `this test suite will be set to pass each time it is executed` |
| 在此之上，**激活该 test suite 自己的 flag `Set fail`** | `the test suite will always be set to fail, **irrespective of its own test level or the testflow flags`** |

**`irrespective of its own test level or the testflow flags` 是本页最硬的一句**：
**test suite 自己的 flag 一旦激活，既盖过它自己的 test level、也盖过 testflow flag。**
**即：优先级从低到高是 test level → testflow flag → test suite 自己的 flag。**
（**这条链是本页把两句合起来读的结论；原文这两句是并列的 bullet，
没有一句话说「优先级顺序是……」——所以把它写成链条是本页的推断，
依据是 `irrespective of` 那半句的排他语气。**）

**⚠️ 另一处缺口**：**`Set pass level` / `Set fail` 这两个 flag 名只在语法节那段示例里出现，
本篇正文里没有它们**；**两个名字的大小写就是 `Set pass level` / `Set fail`**，
**而 `Set pass level` 被称作 `testflow flag`、`Set fail` 被称作 `individual test suite flag`**。

### 本篇与「清单」的分工

**本页是概念页：讲 flag 有哪几类、优先级怎么算。**
**逐个 flag 的名字、取值范围、说明，在 [[alphabetical-list-of-flags]] 那一页**——
**原文把它列为第一条子主题**，**而本页没读它**（见 `## 出处`）。
**这不是重复：本页答「flag 是什么、有哪几类」，那一页答「有哪些 flag」。**

## 典型用法

**本篇（定义文档）没有任何 Procedure、没有 Before you begin、没有 Example**——
**它只有：`#### Subtopics`、一句定义、四条类型链接、`## Related information`、
`## Functional changes`。** **所以「怎么用」在本页只能给到下面这个粒度。**

**按原文能落成的动作**（**每一条的依据都是逐字的；顺序是本页排的，不是原文写的**）：

| # | 动作 | 依据（**原文**） |
|---|---|---|
| 1 | **确认要动的是哪一层**：整条 testflow、还是单个 test suite、还是 site | 四类的名字（`Testflow flags` / `Test suite flags` / `Site control flags`） |
| 2 | **找你要的那个 flag 的名字** | 本篇正文**一个 flag 名都没有**（**除了语法节那两条示例里的 `Set pass level` / `Set fail`**）——**去 [[alphabetical-list-of-flags]]** |
| 3 | **要按 test level 批量定 pass/fail** | 语法节第一条：设 pass level 与 fail level，**中间那一段判 fail、上面那一段判 pass** |
| 4 | **要让某个 test suite 无条件通过** | 语法节第二条前半：该 test suite 的 test level 设 `1`，再打开 testflow flag `Set pass level` |
| 5 | **要让某个 test suite 无条件失败** | 语法节第二条后半：**激活该 test suite 自己的 flag `Set fail`**——它盖过 test level 与 testflow flag |
| 6 | **要调试/记录数据** | 第二类 `Testflow flags for data logging`；**原文 `## Related information` 另链了 `Activating event data logging`**（raw：`02.10_Data_Logging/02.10.01.01.04_Activating_event_data_logging.md`） |

**⚠️ 第 6 条那两层关系要说清**：原文把「data logging 的那一类 flag」列为第二类，
**又另链了一篇 `Activating event data logging`**——**两处是两处，原文没有说它们是同一件事；
本页并列，不替它合并。**

**没有的东西**：本篇**没有 `Errors` 段、没有 `Warnings` 段、没有 `Limits` 段、
没有 `## Application` 段**——**所以「flag 设错会怎样」，本页和原文一样答不出。**

## 和谁有关

- [[testflow-tool]] — **提供方，也是唯一的「谁」**。定义句逐字把四类 flag 挂在它名下：
  `The Testflow Tool provides four types of flags …`。
  **本页只有这一句**；**在 Testflow Tool 里 flag 在哪个页签、怎么勾，本篇一个字都没有。**
- [[alphabetical-list-of-flags]] — **清单侧，与本页互补而不是重复**：
  **本页讲分类与优先级，那一页逐个列 flag。** 原文把它列为**第一条子主题**。
  **本页没读那页**——**所以本页全文一个 flag 名都举不出来**（**除了语法节那两条示例里的
  `Set pass level` / `Set fail`**）。
- [[flags-page]] — **GUI 侧的入口，原文 `## Related information` 的第一条链接**
  （`02.08.04.32.03.01.06_Flags_page.md`）。
  **本页没读它**：**所以那一个页面在 GUI 的哪儿、和 Testflow Tool 什么关系，本页不知道。**
- [[testflow]] — **（推断）第 1、2 类 flag 的作用域**。两类名字都以 `Testflow` 开头，
  **而 testflow 这个阶段本身在 [[testflow]] 那一页**；
  **依据只是名字**——**原文没有说这四类的作用域是什么。本页不写流程叙述。**
- [[test-suite]] — **（推断）第 3 类 flag 的作用域，也是本页示例里被盖过的那一层**。
  语法节第二条说的是 `the individual test suite flag Set fail` **盖过** testflow flag；
  **test suite 本身是什么，在那一页。本页没有那页的任何事实。**
- [[site-control-window]] / [[controlling-multiple-sites]] — **（推断）第 4 类
  `Site control flags` 的两个可能去处**：一个是 GUI 窗口页、一个是多站点概念页。
  **依据只是名字里都有 site control**；**原文没有说 site control flag 在哪儿设。
  本页没读那两页。**
- [[data-logging-profiles]] — **（推断）第 2 类 flag 的下游**。
  第 2 类叫 `Testflow flags for data logging`，**而那一页是 data logging profile 的页**；
  **依据只是「都叫 data logging」**——**原文没有把两者接起来。本页没读那页。**
- [[flow-control-node]] — **（推断）测试执行的「控制」这一侧**。
  定义句说 flag 用于 `controlling the execution of a test`；
  **而 testflow 里做流程控制的是 flow control 那一族**——
  **依据只是用途那句话与那一页的名字。本页没有那页的任何事实。**
- [[smartest-6.3.2]] — **版本页，本页 `## 版本` 唯一的落点**（**而本页的版本条目是哨兵值**）。
- 六条子主题（**均未建**，本页一条都没读）：
  `Alphabetical list of flags`（**已有页，见上**） / `Testflow flags` /
  `Testflow flags for data logging` / `Test suite flags` / `Site control flags` / `Flag priority`。
  **这六条是原文自己声明的 `Subtopics`**；**其中五条本页没有内容可写**——
  **四类的正文、flag 的清单、优先级的完整规则，全在那五条里。**
- `Activating event data logging`（**未建**）— 原文 `## Related information` 的第二条链接
  （raw：`02.10_Data_Logging/02.10.01.01.04_Activating_event_data_logging.md`）。**本页没读。**

## 版本

本文档**有** `## Functional changes` 段，**只有一条**（逐字）：

- **Introduced before SmarTest 6.3.2**

**这一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 flag 这套机制本身成立于哪个版本，这份语料里没有。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**。
**本页能确认的只有「6.3.2 之前就有」这一件事**，
**而 7.10.3 上这四类的行为是否与那之前一致，语料里没有依据**
（**注意 §11：这只是「文档这么写」；本页 `verified: doc-only`**）。

**版本段里没有别的条目**——**四类 flag 各自的引入版本、
`Set pass level` / `Set fail` 这两个名字、优先级规则本身，分别是哪个版本进来的，语料里没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07_Flags.md`

**本页没做的：**

- **只读了这一篇（定义文档）。六个子主题一条都没读**——
  `Alphabetical list of flags` / `Testflow flags` / `Testflow flags for data logging` /
  `Test suite flags` / `Site control flags` / `Flag priority`。
  **这是本页最大的空缺**：**四类 flag 各自有哪些 flag、怎么设、默认值是什么，
  以及优先级的完整规则（本页只有语法节里那两条示例），全在那六条里。**
- **本页的 `## 典型用法` 只有六行**——**因为定义文档没有 `## Procedure` /
  `## Before you begin` / `## Example`**，**本页没有别的地方可补**
  （§2.2：concept 页不写流程，流程在 stage 页）。
- **一个 flag 的名字都举不出来**（**除了语法节那两条示例里的 `Set pass level` / `Set fail`**）：
  **定义文档正文里没有列出任何一个 flag**，**清单在 [[alphabetical-list-of-flags]]，本页没读。**
- **`Flags page` 没读**（原文 `## Related information` 第一条）——
  **所以 GUI 上 flag 在哪儿管、和 Testflow Tool 什么关系，本页不知道。**
- **`Activating event data logging` 没读**（第二条）——
  **所以 data logging 那一类 flag 和「激活 event data logging」是不是同一件事，本页不判。**
- **`## 是什么` 第三节那张优先级链（test level → testflow flag → test suite flag）
  是本页把语法节两条示例合起来读的结论**，**原文两条 bullet 是并列的，没有给这条链**。
  **本页已把这一点标成推断；要核只能回子主题 `Flag priority`（本页没读）。**
- **一篇图都没看。** 本篇**没有图片引用**（`![` 0 处，本页核过）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：四类 flag 的「作用域」是本页从名字读出来的，原文一个字都没写；
  本页已把每一处都标成推断。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `#### Subtopics` 的标题层级与同一篇里其它标题不一致。** 逐字：本篇的四个标题是
> `# Flags` / `#### Subtopics` / `## Related information` / `## Functional changes`
> ——**`Subtopics` 用了四级（`####`）**，而它前后的标题是 `#` 与 `##`。
> **同一篇里层级跳了两级。本页照实记，不替它改。**
>
> **② 四类 flag 在同一篇里被列了两次。** 第一次在 `#### Subtopics` 里（六条中的四条），
> 第二次在定义句下面（四条，且**顺序与 Subtopics 里的那四条完全一致**）。
> **两次的链接目标逐字相同**（`.02` / `.03` / `.04` / `.05`）。
> **原文没有说明为什么重复；本页照实记，不替它合并。**
>
> **③ `## Related information` 两条链接粘在一起，中间没有分隔符。** 逐字：
> `Flags page` + `Activating event data logging`
> ——**两对链接首尾相接**（原文里就是 `](<…>)[` 直接相连）。
> **本页在 `## 和谁有关` 里把它们分开写，但引文里的粘法是原文的。**
>
> **④ 定义句没有给 flag 的定义，只给了「几个、谁提供、干什么用」。**
> 逐字就是那一句（`The Testflow Tool provides four types of flags for debugging and
> controlling the execution of a test.`）——**「一个 flag 是什么」本篇没有答案。
> 这不是本页漏读，是原文没写；本页照实说，不替它补。**
>
> **⑤ 优先级那条示例里有一段没有交代的 test level 区间。** 逐字：
> `If you set the pass level to 4 and the fail level to 2, then all test suites with test levels
> 2 and 3 will be set to fail, and all test suites with test levels 4 and above will be set to pass.`
> ——**test level 是 0 或 1 时怎么判，这一句没有覆盖**（**而它上下两段是连续的 2–3 与 4+**）。
> **本页把它标成「缺口」并列，不替它补一条。**
> **另外这一句只交代了 pass level = 4、fail level = 2 这一个组合，
> 两个值之间有没有大小关系要求（例如 pass level 必须大于 fail level），原文没有写。**
>
> **⑥ 两个 flag 名只出现在那两条示例里，正文里没有。** 逐字：`Set pass level`、`Set fail`
> ——**本篇正文（`Subtopics` 与定义句）里一个 flag 名都没有**，
> **所以这两个名字的出处是子主题 `Flag priority` 的示例，不是定义文档。**
>
> **⑦ 本篇标题是复数 `Flags`，而本 wiki 这一页的 slug 是单数 `flag`。**
> 语料标题逐字是 `# Flags`，文件名是 `02.08.04.32.01.02.07_Flags.md`。
> **按标题去搜的人会搜到复数形态，按本 wiki 的 slug 搜是单数**——
> **这是本 wiki 的命名（§5：slug 用本名小写），记录在此以免下一个人以为有一页没建。**
>
> **⑧ 本篇没有 §11.2 ① 那种编码损坏。** 本页查过：**全文没有汉字，也没有 `鈥`**
> （`[一-鿿]` 与 `鈥` 均 0 命中）。

`verified: doc-only`
