---
type: object
title: Utility Pins editor
layer: gui
stage: pin
tags: [pin, gui, utility-line, utility-card, pogo-block, tester-channel, safety-line]
related: [pin, pin-configuration-tool, pin-configuration-file, utility-purpose-editor, utility-line-view, utility-card, utility-pogo-block-utility-card-v93000-exa-scale-systems, flex-relay, get-utility-lines, set-utility-lines, dps-pins-editor, digital-pins-editor, mapping-pin, dfut]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Utility Pins editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Utility Pins editor 是给 utility pogo pin 分配名字的 GUI。** 原文第一句就是全部机制：

> 「Utility pin names are assigned to utility pogo pins in the Utility Pins editor.」

**注意这句划的范围**：它只承诺「**分名字**」。
utility line 的**运行期状态**（谁开、谁关、什么时候开）不在这里——
原文把那条线分别挂在 `t[ms]` 与 `Name` 两格里外链出去（routing set / test method / 固件命令 `UTST`）。

**本文档没有 `## Syntax` / `## Parameters` / `## Example` 段标记**——
所以本页的「语法 / 参数」节是空的（脚本一个字都不收：没有段标记时「哪一段是参数表」是猜，而猜就是编）。
**下面这张表是我从 raw 的散文里转述的**，凡加 `>` 的才是逐字原文。
原文对表本身的说明是：

> 「The following table describes the parameters in the Utility Pins editor:」

### 五个列

| 列 | 原文要点 |
|---|---|
| **`Name`** | 描述性名字，**最多 16 个字母数字字符**；空格与 `# ; (鈥? ) ? @ ,` 不允许。别的窗口引用这个 pin 时显示的就是它 |
| **`Mode`** | 这行的**工作模式**：`w`（write-only）/ `r`（read-only）/ `rw`（read-write）；**可选 Utility Card 的 line 还能填四个安全关键字**（见下） |
| **`t[ms]`** | **可选**。utility line 状态改变到下一个动作之间的等待时间；**只在 `w` / `rw` 模式下有效**，默认 `0 ms` |
| **`Comment`** | 可选描述 |
| **`Tester Channel`** | **utility pogo block + 该 block 的 utility line**：前三位是 block，后两位是 line 号 |

`Name` 那一句原文：

> 「The pin name can have up to 16 alphanumeric characters. Spaces and the following characters are not allowed:」

> 「Other SmarTest windows will always display the pin name when they refer to this pin.」

### `Mode`：三个读写模式 + 四个安全关键字

> 「The parameter defines the operating mode of the utility line using the following specifiers:」

> - 「w: write-only」
> - 「r: read-only」
> - 「rw: read-write」

**`w` / `r` / `rw` 怎么选，原文给了判据**：

> 「For a write-only utility line, specify the w mode.」

> 「For a read-write utility line, you can select one of three:」

> - 「If you want to use it as write-only, specify the w mode.」
> - 「If you want to use it as read-only, specify the r mode.」
> - 「If you want to use both functions in your tests, specify the rw mode.」

**另外四个取值只对可选 Utility Card 的 line 有效**（原文那句有个限定语 `of the optional Utility Card`）：

> 「Utility lines of the optional Utility Card can also be configured as safety lines or as global shutdown line for hardware鈥慶ontrolled shutdown of XPS256 pins:」

> - 「triggerIfHigh: Safety line」
> - 「triggerIfLow: Safety line」
> - 「triggerSiteIfHigh: Global shutdown line」
> - 「triggerSiteIfLow: Global shutdown line」

（⚠️ `hardware鈥慶ontrolled` 里的 `鈥慶` 是坏字（`= ‑c`），应为 `hardware‑controlled`——见「出处」③。）
原文把这两类用途的说明**外链**给 `XPS256 safety line and DUT board disconnect`（**本页没读**）。

### `t[ms]`：什么时候用得上

> 「The optional parameter specifies a wait time from when the utility line state is changed until the next action is executed, such as the settling time of the controlled user-relay.」

> 「The wait time defined here is used in the following cases:」

> - 「When the utility line is controlled using a routing set.」
> - 「When the utility line is controlled from your test method programs.」
> - 「When the utility line is controlled using the UTST firmware command.」

**多条一起控制时是并行切换，等待时间取最长的那个**：

> 「When multiple utility lines are controlled at a time, they are switched in parallel and the longest settling time of all the utility lines is used.」

> 「This setting is valid only when the utility lines are used in the w or rw mode. The default value of the settling time is 0 ms.」

**原文还给了一条绕开它的办法**：

> 「You can also set a wait time in the routing set using a different procedure, instead of this parameter.」

### `Tester Channel`：那五位数怎么读，**以及那个差 1 的坑**

> 「The parameter specifies the utility pogo block and the utility line of the pogo block.」

> 「The first three digits define the utility pogo block of V93000 EXA Scale systems.」

> 「The last two digits specify the utility line number. Valid utility line numbers are 01 鈥?nbsp;32 for the 4-row utility block.」

**然后是这一节最该记住的一句**——「界面上的号」和「命令里的号」**差 1**：

> 「Note that the utility line number ( 01 鈥?nbsp;32) is different from the number (00 鈥?nbsp;31) used in the UTST firmware command and as pin designator of the utility pogo blocks.」

| 在哪 | line 号范围 |
|---|---|
| **本编辑器界面（也就是这篇文档）** | `01` 到 `32` |
| **`UTST` 命令、以及 utility pogo block 的 pin designator** | `00` 到 `31` |

（上面那三处的 `鈥?` 是坏字，`nbsp;` 前面那个 `&` 也已经丢了——**照原样引，没替它修**，见「出处」①。）

**黄底 = 这条 line 被复用**：

> 「The background color will change to yellow for re-used utility lines: The screen shot above shows this feature for the utility pin "VS". "VS" is assigned to the a single utility pogo pin "16601" for all four sites.」

⚠️ `assigned to the a single` 里 `the a` 重复，**原文如此**（见「出处」④）。

**「怎么用」那一步在 `Name` 那一格里**（本页唯一一处）：

> 「You can access the utility pins with the test method library (GetUtilityLines and SetUtilityLines), test method API or your own test method.」

（原文里 `GetUtilityLines` 与 `SetUtilityLines` 是两条**语料内部链接**，指向
`02.07.05.04.05` / `02.07.05.04.07`；上面按 §11.1 ② 剥掉链接标记后引，**名字仍是逐字的**。
**那两篇本页没读。**）

### 界面长什么样（④ 图证 · `354720.png`）

原文在参数表前挂了一张界面图——**它的 alt 文字自己写着版本**：
`Utility pins editor SmarTest 7.10.x`（`354720.png`，642 × 276）。**逐格读过，第 8、9 行还放大核过**：

- 窗口上一个 tab `Utility Pins`；表头是行号、`Name`、`Mode`、`t[ms]`、`Comment`、`Tester Channel`——
  **与正文那张表的五个列名逐个对得上**。
- **`Tester Channel` 那一格被拆成四个子列：`Site 1` `Site 2` `Site 3` `Site 4`**。
  正文只在 `VS` 那一句里说过 `for all four sites`，**表头这个「一列一个 site」的结构正文一个字没写**。
- 九行逐格读出来是：

| # | `Name` | `Mode` | `t[ms]` | `Comment` | `Site 1` | `Site 2` | `Site 3` | `Site 4` |
|---|---|---|---|---|---|---|---|---|
| 1 | `OUT1 TO LOAD` | `w` | `0.0` | 空 | `16505` | `16506` | `16507` | `16508` |
| 2 | `OUT2 TO LOAD` | `w` | `0.0` | 空 | `16615` | `16616` | `16620` | `16611` |
| 3 | **`VS`** | `w` | `0.0` | 空 | **`16601`** | **`16601`** | **`16601`** | **`16601`** |
| 4 | `GND TO IN` | `rw` | `0.0` | 空 | `16701` | `16702` | `16703` | `16704` |
| 5 | `VS TO C 100NF` | `r` | `0.0` | 空 | `16605` | `16606` | `16607` | `16608` |
| 6 | `VS TO LOAD` | `w` | `0.0` | 空 | `16706` | `16707` | `16708` | `16709` |
| 7 | `VS TO 100R` | `w` | `0.0` | 空 | `16801` | `16802` | `16803` | `16804` |
| 8 | `SAFETY LINE` | `triggerIfHigh` | **灰块** | 空 | `16510` | `16511` | `16512` | `16513` |
| 9 | `GLOBAL SHUTDOWN` | `triggerSiteIfHigh` | **灰块** | 空 | **`16514`** | **`16514`** | **`16514`** | **`16514`** |

（第 3 行与第 9 行的**通道格子是黄底**——见下。）

**图上读到的字里，哪些算图证，逐个 `grep -F` 核过**：
`Site 1` / `Site 2` / `Site 3` / `Site 4` / `OUT1 TO LOAD` / `OUT2 TO LOAD` /
`VS TO C 100NF` / `VS TO LOAD` / `VS TO 100R` / `SAFETY LINE` / `GLOBAL SHUTDOWN` /
`16505` / `16514` / `0.0` / `100NF` **在本篇 raw 里都是 0 次**；
而 **`VS` / `16601` / `triggerIfHigh` / `triggerSiteIfHigh` 是搜得到的**——
**所以这四个不算图证**，只有上面那串算（§11.4 要的就是这条分界：
**拿图里的字回 raw 数一遍，能搜到的不算图证**）。

**图答掉的三件事：**

1. **黄底有两行，不是一行。** 正文只点名了 `VS`（`The screen shot above shows this feature for the utility pin "VS".`）；
   图上 **`GLOBAL SHUTDOWN` 那一行四个 site 的 `16514` 也是黄底**。
   而且两行的黄**只铺在 `Tester Channel` 那几格上，不是整行**。**这一条正文没写。**
2. **`t[ms]` 对两个安全关键字是灰块（不可用）。** 这与正文那句
   `This setting is valid only when the utility lines are used in the w or rw mode.` 一致；
   **但「灰块」这个形态只在图上**。另外图上其余七行的 `t[ms]` **全是 `0.0`**，与「默认 `0 ms`」一致。
3. **五位数真的按「前三位 block + 后两位 line」切。** 图上的 block 号是
   `165` / `166` / `167` / `168` 四个，line 号从 `01` 到 `20`——
   与正文那条规则对得上；而 **`VS` 那行四个 site 都是 `16601`（block `166`、line `01`），
   正是正文举的那个例子**（正文说它是 `a single utility pogo pin "16601" for all four sites`）。

**一条（推断）**：图上 `SAFETY LINE` 用 `triggerIfHigh`，四个 site 分到**四个不同的 pin**
（`16510` 到 `16513`）；`GLOBAL SHUTDOWN` 用 `triggerSiteIfHigh`，四个 site **共用同一个 pin**（`16514`）。
**两个关键字的差别（一个 per-site、一个全局）在图上看得见**——
依据是这两个关键字自己的名字里就有 `Site`，而正文把它们分别叫 `Safety line` 与 `Global shutdown line`；
**但正文没有把「per-site 对全局」写成一句话，所以这一条是推断。**

**图答不了的，照实说**：`triggerIfLow` 与 `triggerSiteIfLow` **图上一行都没有**（这份配置只用了一对 High）；
`Comment` 列九行全空；block 号的**合法值域**图不给（只有 `165` 到 `168` 四个实例）；
**图是一次具体配置的截图，不是格式规范**——「哪些列必填、`Mode` 能不能中途改」图答不了。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## Example` 段**，
唯一的 `## Related information` 是一张链接清单（那六条本页一条没读）。
下面这条链是**从五个列的说明里拼的**（推断），**顺序即原文列序**：

1. **挑一个 utility pogo block 和它的一条 line**，写进 `Tester Channel`：
   **前三位 block、后两位 line**（④ 图证：图上 `16601` = block `166` 的 line `01`）。
2. **填 `Name`**：≤16 个字母数字字符，避开 `# ; (鈥? ) ? @ ,` 与空格。
3. **填 `Mode`**：`w` / `r` / `rw`；**要把这条 line 当安全线或全局 shutdown 线，
   就填四个关键字之一**——**前提是它属于可选 Utility Card**（原文的限定语）。
4. **需要就填 `t[ms]`**：**只在 `w` / `rw` 下有效**（④ 图证：两个安全关键字的 `t[ms]` 格是灰的）；
   默认 `0 ms`；**也可以不填这里，改在 routing set 里设**（原文给了这条替代路径）。
5. **`Comment` 可选**（图上九行全空）。

**然后三条「用」的路**（原文在 `t[ms]` 与 `Name` 两处分别点名）：

| 谁在控制它 | 原文 |
|---|---|
| **routing set** | `the utility line is controlled using a routing set` |
| **你的 test method 程序** | `the utility line is controlled from your test method programs`；库函数是 `GetUtilityLines` / `SetUtilityLines` |
| **固件命令** | `the utility line is controlled using the UTST firmware command` |

**两条硬约束，装进脑子再动手：**

- **`t[ms]` 只在 `w` / `rw` 下有效**——`r`（只读）那条路线上它没有意义。
- **界面上的 line 号 `01` 到 `32` ≠ `UTST` / pin designator 的 `00` 到 `31`。**
  写 `UTST` 时**照 `00` 到 `31` 那套写**——原文的措辞是 `Note that the utility line number ( 01 鈥?nbsp;32) is different from the number (00 鈥?nbsp;31) used in the UTST firmware command and as pin designator of the utility pogo blocks.`，
  **这是个会静默配错线的坑**（推断：原文只说「不同」，**没有给换算例子、也没说为什么差 1**）。

**一条并行规则**：多条 utility line 同时被控制时**并行切换**，
`t[ms]` 取**所有被控 line 里最长的那个**——所以**一条慢线会把整组的等待时间拖长**（推断，依据是原文
`the longest settling time of all the utility lines is used.`）。

## 和谁有关

- [[utility-purpose-editor]] — **把若干 utility line 组成一个 purpose 并给标准状态**的下一个编辑器。
  **本篇 raw 里没有它**（`purpose` 一词在整篇里出现 0 次）——这条关系来自 [[mapping-pin]] 的对照表，
  **本页没有回那篇原文核**。
- [[utility-line-view]] — **utility line 的运行期视图**（原文 `## Related information` 指向
  `01_Getting_started` 那一族的 `01.01.07.05.04`）。**本页没读**——
  所以「配好之后在界面上怎么看它的状态」，本页没有。
- [[utility-card]] — **四个安全关键字只对它的 line 有效**（原文的限定语 `of the optional Utility Card`）。
  **没读**——所以「哪些 block 的哪些 line 算 Utility Card 的」，本页不知道。
- [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] — 原文两处指向
  `utility pogo blocks`（`02.03.06.08`）。**那个 `00` 到 `31` 的 pin designator 的解释在那边，
  本页没读**——所以那个差 1 的坑**本页只说了「差 1」，没说为什么**。
- [[get-utility-lines]] / [[set-utility-lines]] — 原文在 `Name` 那一格点名的两个 test method 库函数
  （`02.07.05.04.05` / `02.07.05.04.07`）。**没读**——**参数、返回值、怎么调，本页一个字没有。**
- [[flex-relay]] — 原文 `## Related information` 里的一条（`FLEX_RELAY`，`02.07.04.01.68`）。
  **`t[ms]` 那句里的 `the controlled user-relay` 多半就是它**（推断，仅指关系）——**没读**。
- [[dut-board-design-reference]] — 原文指向那一族里的 `DUT interface layout`（utility block 的位置）
  与 `Utility lines`。**没读。**
- [[mapping-pin]] — 那张对照表把本编辑器排在**「utility line 的符号名与方向」**那一行：
  GUI 侧是本页、文件侧是 [[pin-configuration-file]]、L1 侧是 [[dfut]]。
  **`DFUT` 这个词在本页 raw 里出现 0 次**——**本页既不背书也不否认那条对应。**
  同一张表还有一行「utility line 的**运行期**状态」，GUI 格写的是 `?`——
  **本页确实没有那一格**：本页管的是 `Mode` 与 `t[ms]` 这类**配置**，
  **开与关是运行期的事**（见「是什么」第一段）。
- [[pin-configuration-file]] — 落盘侧（关系来自 [[mapping-pin]]，**本页没读那篇**）。
- [[dps-pins-editor]] / [[digital-pins-editor]] — 同 `stage: pin` 的同族 GUI 编辑器。
- `UTST`（**在本 wiki 里没有页，也不在 allowlist**）— 原文三处点名它。
  **本页用反引号写它，不链**（§9.1：链一个不会被建的名字 = 造一个悬空目标）。
- `XPS256 safety line and DUT board disconnect`（`02.05.05.03.03.06`）——
  `Mode` 那格里外链出去的那篇，**没读**；所以**四个安全关键字到底怎么触发 XPS256 断电，本页没有。**

## 版本

原文 `## Functional changes` **五条**，条目逐字：

- `Introduced in SmarTest 6.5.0`
- **SmarTest 7.1.3**：`Changed the parameter "Operation Mode" to "Mode".`
- **SmarTest 7.1.3**：`Changed the parameter "Delay [ms]" to "t[ms]".`
- **SmarTest 7.10.1**：`Three-digit utility pogo block designator on V93000 EXA Scale systems.`
- **SmarTest 7.10.2**：`New keywords for the Mode parameter to configure shutdown of XPS256 pins using utility lines.`

**五条必读：**

1. **第一条不是哨兵值**（不是 `Introduced before SmarTest 6.3.2`）——
   **这个编辑器是 SmarTest 6.5.0 引入的**，是一条真版本事实。
2. **7.1.3 一口气改了 `Mode` 与 `t[ms]` 两个列名**（`Operation Mode` → `Mode`、
   `Delay [ms]` → `t[ms]`）。同族的 [[dps-pins-editor]] 在**同一个版本号**上改了它那篇的三处列名
   （`Polarity` → `Pol`、`Load Capacitor [uF]/V-Ramp [us]` → `C[uF]`、`Instrument` → `HW`）——
   **两篇改的都是列名，但两篇文档互相没有引用**，所以「同一批改动」是**按版本号并列**，
   不是语料说的（推断）。
3. **7.10.1 那条正是正文「前三位」那句的前提**：正文写
   `The first three digits define the utility pogo block of V93000 EXA Scale systems.`，
   而版本记录说三位 block 号是 **7.10.1** 才有的——**所以那个读法不适用于 7.10.1 之前**（推断）。
   这也解释了图上 block 号为什么是 `165` 这种三位数。
4. **7.10.2 那条与正文完全对得上**：`Mode` 格里那四个关键字
   （`triggerIfHigh` / `triggerIfLow` / `triggerSiteIfHigh` / `triggerSiteIfLow`）
   的用途正是 `shutdown of XPS256 pins`。**这是本篇版本记录与正文自洽的一条。**
5. **版本记录里没有一条讲界面号与命令号那个差 1**（除 7.10.1 那条讲 block 位数之外）——
   **所以「界面 `01` 到 `32` / `UTST` `00` 到 `31`」这个差是什么时候来的，本篇没写。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.md`
（`105637.htm`，104 行）——**整篇读完**。

**本页做了什么**：

- **读了本页唯一那张图** `354720.png`（alt 文字 `Utility pins editor SmarTest 7.10.x`，642 × 276），
  **逐格读过，第 8、9 行放大到 2 倍核过**。
  **图片路径 `../../../../raw/x.png` 往上四层正好是 `tdc-html/`，图就在那儿**（`schema.md` §11.4）。
  图答掉的东西写进了「是什么」（黄底两行、`t[ms]` 灰块、九行逐格取值、五个列名与四个 site 子列）。
- **图里读到的字一律没有进 `>` 引文块**——引文块的含义是「这段能在 raw 文本里搜到」，
  **图上的字搜不到**（§11.4）。逐个 `grep -F` 核过：`Site 1` 到 `Site 4`、
  `OUT1 TO LOAD`、`OUT2 TO LOAD`、`VS TO C 100NF`、`VS TO LOAD`、`VS TO 100R`、
  `SAFETY LINE`、`GLOBAL SHUTDOWN`、`16505`、`16514`、`0.0`、`100NF`
  **在本篇 raw 里都是 0 次**；`VS` / `16601` / `triggerIfHigh` / `triggerSiteIfHigh`
  **是搜得到的，所以那四个不算图证**。

**本页没做的**：

- **「语法 / 参数」节是空的**（文档没有 `Syntax` / `Parameters` / `Example` 段标记）——
  **所以本页「五个列」那张表是我从散文里转述的，不是逐字**；凡加 `>` 的地方才是逐字原文。
- **`## Related information` 那六条链接一条都没读**（`Utility lines`、
  `Pogo pin assignment - Utility pogo blocks`、`UTST`、`FLEX_RELAY`、`Utility Line view`、
  `DUT interface layout`）；`Mode` 那格里的 `XPS256 safety line and DUT board disconnect`
  与 `Utility Card`、`Name` 那格里的 `GetUtilityLines` / `SetUtilityLines` **也都没读**。
- **`UTST` 的命令原文没读**——**所以那个 `00` 到 `31` 的编号为什么和界面差 1，本页没有答案。**
- **没有实跑。** 没有开过这个编辑器、没有写过 utility line 配置、没有在机台上发过 `UTST`。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pin.md`。

> ⚠️ **本篇的语料瑕疵，照实记、一处没替它改**：
> ① **一个 `&nbsp;` 的 `&` 丢了，前面那个字还是坏字**——三处同一形态：
>    `01 鈥?nbsp;32`（两处）与 `00 鈥?nbsp;31`（一处）。
>    `鈥?` 是三字节字符丢了一个字节（落 **U+2000 到 U+203F** 区间，`–` / `‑` 都可能，**反解不了**，§11.2①）；
>    `nbsp;` 则说明原来的 `&nbsp;` 实体只剩后半截。**照原样引，没替它修**——
>    §11.2① 明令：**引文里必须原样留着坏字，不许用省略号替掉它。**
> ② **禁用字符清单那一行整片坏掉**：逐字是
>    `# ; (鈥? ) ? @ ,`
>    ——而**同族的 [[dps-pins-editor]] 与 [[digital-pins-editor]] 那两篇同一行渲染成 `# ; ( ' ' ) ? @ ,`**。
>    **同一份清单在这三篇里有两种坏法**（推断：原意应是双引号和单引号两个字符，即 `" '`）。
>    **本页照抄，不替它改。**
> ③ **`hardware鈥慶ontrolled`** —— `鈥慶` = `‑c`（§11.2①），所以是 **`hardware‑controlled`**。
>    **⚠️ 拿 `controlled` 去 raw 里搜是搜不到的，要搜 `鈥慶ontrolled`。**
> ④ **一句话里 `a` 出现两次**：逐字是
>    `"VS" is assigned to the a single utility pogo pin "16601" for all four sites.`
>    ——`the a` 重复，**原文如此**。
> ⑤ **`## Related information` 那一节把六条链接挤成了一行**：
>    第一条以 `)` 收尾，**下一条紧接着以 `[` 开头，中间连一个空格都没有**，
>    六条一路排到行末。**原文如此。**

**⑥（这一条是 ④ 图证，所以故意不放进上面的 `>` 块——引文块的含义是「这段能在 raw 文本里搜到」，而图上的字搜不到）**
**正文举的黄底例子只有一个，图上有两行。**
正文逐字写的是 `The screen shot above shows this feature for the utility pin "VS".`——
**只点名 `VS`**；而 `354720.png` 上**第 3 行 `VS` 与第 9 行 `GLOBAL SHUTDOWN` 的通道格子都是黄底**
（`GLOBAL SHUTDOWN` 那行的值是 `16514`，四个 site 相同）。
**原文没有解释第二行为什么是黄的**；本页两处并列，**不替它判定哪一处更全**。

`verified: doc-only`
