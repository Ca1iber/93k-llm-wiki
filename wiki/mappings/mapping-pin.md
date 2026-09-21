---
type: mapping
title: Pin 配置的三层对照
layer: n/a
stage: pin
tags: [mapping, pin, gui, firmware-command, test-method-api, setup, pin-configuration-file]
related: [pin, dfpn, dfps, conf, ctxt, dfgp, dfge, dfpt, dfpr, dfut, dfup, pssl, vpin, pste, pals, psfc, pqfc, pact, stme, upas, pin-configuration-file, pin-configuration-master-file, pin-configuration-tool, digital-pins-editor, dps-pins-editor, utility-pins-editor, utility-purpose-editor, pin-group-editor, port-editor, alias-set-editor, dc-scale-limits-editor, setup-management-tool, flex-relay]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01.04_Alias_set.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.01_Virtual_pins.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08.01_Creating_a_pin_group.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.11_Setting_DC_Scale_voltage_and_current_limits.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md
  # ⚠️ 2026-09-20 补：本页「7.1.3 改名」那段**逐条引自这一篇的 `## Functional changes`**，
  # 而原先只列了它的两个子主题——**引的那一篇不在 `sources:` 里**（与 `stpm-merge-rules-file` 同一个洞）。
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.02_Load_capacitance_connected_to_the_DC_Scale_DPS128_DPS64.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.03_Load_capacitance_connected_to_the_DC_Scale_XPS256.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.06_Virtual_Pins_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.06_DC_Scale_Limits_editor.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.10_Protocol_assignments.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.10.01_Assigning_pin_roles_and_protocols.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Pin 配置的三层对照

## 这张表在说什么

Pin 这一段的配置，语料里**同时存在三套说法**：Pin Configuration 工具里的表格（GUI）、
`<device_dir>/configuration` 下的 pin 配置文件（file）、以及一组固件命令（L1）。
**这三套是不是同一个东西的三种写法——语料自己回答了，而且是明说的。**

`02.08.04.18.04_Pin_configuration_file.md` 第一段：

> 「The Pin Configuration tool stores the data in the pin configuration file located in the directory:」

> 「The file contains a set of firmware commands corresponding exactly to the parameters specified within the Pin Configuration tool.」

**`corresponding exactly to` 是本页的地基。** 它说的是：**GUI 上填的每一个参数，
在文件里都有一条对应的固件命令**——不是「有关」，是「逐条对应」。
所以本页不是我在替语料做归纳，**是语料自己声明了这个对应关系，本页把它按「目的」排成一张表**。

同一个文件里给了落点：

> 「<device_dir>/configuration」

而 `02.08.04.18.05_Pin_configuration_master_file.md` 补了拆分情形：

> 「A pin configuration can be organized as one single file, or different parts of the pin configuration can be stored in separate files. In the latter case, the respective pin configuration files can be merged through a master file which contains references to the individual files.」

（第三句里 `Setup Management Tool` 在原文里是**语料内部链接**，指向
`01_Getting_started/…/01.01.07.02.02.04_Setup_Management_Tool.md`；**本页把链接名放在引号外**，
引号里保留逐字原文。**这句话的后半截有一个语料错字**，见「对不上的地方」④。）

**「三层」这个词在本页要放宽理解**：§2.5 的格式给了五列（GUI / 文件 / L1 / L2 / L3），
而 pin 这一段**只有前三层被语料钉住**，**L2 只在少数几个点上出现，L3 一格都没有**——
这不是我没找到，是**pin 的定义动作本来就不发生在 L3**。下面「对不上的地方」逐条说明。

## 对照表

**读法**：一格填了名字 = 有证据（证据是什么见下一节）；`?` = 语料没说，**本页不猜**；
`—` = 这一层不存在这个对应物（不是「没找到」）。

| 目的 | GUI | 文件 | L1 命令 | L2 API | L3 接口 |
|---|---|---|---|---|---|
| 给数字 channel 分配 pin 名与 pin 号 | [[digital-pins-editor]] | [[pin-configuration-file]] | [[dfpn]] | — | — |
| 把 DPS channel 绑到器件 pin，并给极性 | [[dps-pins-editor]] | [[pin-configuration-file]] | [[dfps]] | — | — |
| 设 pin 类型与工作模式 | [[digital-pins-editor]] | [[pin-configuration-file]] | [[conf]] | — | — |
| mode context 的定义与切换 | [[digital-pins-editor]]（右上 `CONTEXT` 下拉） | [[pin-configuration-file]] | [[ctxt]] | — | — |
| 固定 pin 组 / 表达式型 pin 组 | [[pin-group-editor]] | [[pin-configuration-file]] | [[dfgp]] / [[dfge]] | — | — |
| port（可独立跑 timing 的 pin 组） | [[port-editor]] | [[pin-configuration-file]] | [[dfpt]] | — | — |
| pin alias | [[alias-set-editor]] | [[pin-configuration-master-file]]（拆文件时） | [[dfpr]] | — | — |
| utility line 的符号名与方向 | [[utility-pins-editor]] | [[pin-configuration-file]] | [[dfut]] | — | — |
| utility purpose（一组 utility line + 标准状态） | [[utility-purpose-editor]] | [[pin-configuration-file]] | [[dfup]] | — | — |
| DPS128/DPS64 与 XPS256 的负载电容 | DPS Pins 表的 `C[uF]` 列（**7.1.3 之前叫 `Load Capacitor [uF]/V-Ramp [us]`**） | [[pin-configuration-file]] | `PSLC` | `SPMU_PIN_TASK.loadCap` | — |
| DC Scale 的电压/电流**限值** | [[dc-scale-limits-editor]] | [[pin-configuration-file]] | `?` | `EVENT_ICVM.limits` / `.limitHigh` / `.limitLow`、`EVENT_ICIM.limits` / `.limitHigh` / `.limitLow` | — |
| 虚拟 pin（不接 pogo，只用于记结果） | `Virtual Pins editor` | [[pin-configuration-file]] | [[vpin]] | `SMC_TEST()`、`TESTSET::judgeAndLog_ParametricTest` / `_ScanTest` | — |
| protocol / pin role 分配 | [[protocol-editor]] | [[pin-configuration-file]] | `?` | `Pin_role` / `Protocol` / `Transaction`（`02.07.11.01.09`） | — |
| utility line 的**运行期**状态 | `?` | — | `UTST` | `SetUtilityLines()` / `GetUtilityLines()`、[[flex-relay]] | — |
| 声明 site 数、逐 site 分配 channel | `?` | [[pin-configuration-file]] | [[pste]] / [[pals]] | — | — |
| setup focus / query focus / site 激活 | `?` | — | [[psfc]] / [[pqfc]] / [[pact]] | — | — |
| site match function | `?` | — | [[stme]] | — | — |
| 逐 site 的 utility purpose 标准状态 | [[utility-purpose-editor]] | [[pin-configuration-file]] | [[upas]] | — | — |

**表里没有的**：`RDIV`、`DDSL`、`DFAN` **三条命令出现在 pin 配置文件的例子里**
（`02.08.04.18.04` 的 `## Example` 代码块，逐字），但**pin 那页的「涉及对象」没收它们**，
本页也不替它收——**它们的 GUI 侧是什么，语料没写**。

## 证据：哪几格是钉死的，哪几格只是「那边链过来了」

**证据分四档，本页不把它们混成一种。**

**① 语料明说对应（最硬）** —— 就是上面那句 `corresponding exactly to`。
它覆盖的是**「Pin Configuration 工具 ↔ pin 配置文件 ↔ 固件命令」这条整链**，
所以主表里 GUI / 文件 / L1 三列**凡是属于 Pin Configuration 工具族的，都由这一句背书**。
但它**不逐条说「哪个编辑器对应哪一条命令」**——那一层对应是本页按各编辑器的职责排的（**推断**），
依据是各编辑器文档自己的表格列（`Name/No/Type/Mode/…` 对 `DFPN`/`CONF` 的参数集）。

**② 文档之间有链接（次硬，逐条可查）** —— 这些是语料里**实际存在的跨层链接**，
取自 `extract/edges.jsonl`（`02.08` → `02.06`/`02.07`，共 42 条落在 pin 这一段）：

| 源文档（GUI 侧） | 链到 | 条数 |
|---|---|---|
| `02.08.04.18.01.04_Alias_set.md` | `DFPR`、`UDPR`、`Defining pin groups`、`Defining ports` | 4 |
| `02.08.04.18.02.08.01_Creating_a_pin_group.md` | `Defining pin groups` | 1 |
| `02.08.04.18.02.07.01_Virtual_pins.md` | `SMC_TEST()`、`TESTSET::judgeAndLog_ParametricTest`、`_ScanTest` | 3 |
| `02.08.04.18.03.01.06_Virtual_Pins_editor.md` | 同上三条 | 3 |
| `02.08.04.18.03.01.02_Digital_Pins_editor.md` | `Mode contexts` | 1 |
| `02.08.04.18.03.01.03.02_Load_capacitance_…DPS128_DPS64.md` | `PSLC`、`SPMU_PIN_TASK.loadCap` | 2 |
| `02.08.04.18.03.01.03.03_Load_capacitance_…XPS256.md` | 同上两条 | 2 |
| `02.08.04.18.03.01.04_Utility_Pins_editor.md` | `UTST`、`FLEX_RELAY`、`GetUtilityLines`、`SetUtilityLines` | 4 |
| `02.08.04.18.03.06_DC_Scale_Limits_editor.md` | `EVENT_ICVM` 与 `EVENT_ICIM` 的 `limits`/`limitHigh`/`limitLow` | 6 |
| `02.08.04.18.03.10_Protocol_assignments.md` | `Pin_role`、`Protocol`、`Transaction` | 3 |
| `02.08.04.18.03.10.01_Assigning_pin_roles_and_protocols.md` | 同上三条 | 3 |

**链接证的强度要说清**：一条链接**只证明「那篇文档认为读者该去看这一篇」**，
**不证明两个东西等价**——可能是「见也」，也可能是「区别在这里」，也可能是「前提」。
本页只在主表的**同一行**里用它们，**不跨行搬**。

**③ 只有命令侧、没有 GUI 侧的证据** —— 主表里 L1 列填了命令、而 GUI 列是 `?` 的那些行
（`PSTE`/`PALS`/`PSFC`/`PQFC`/`PACT`/`STME`/`UPAS`、`UTST`）。
它们的命令事实来自 `wiki/stages/pin.md` 与各命令页，**但语料里没有一篇 GUI 文档链到它们**，
所以 **GUI 那一格是 `?`，不是 `—`**——`?` 的意思是「本页没找到证据」，不是「不存在」。

**④ 图证（2026-09-20 加，本页用到了）** —— 从 raw 自带的截图里读出来的。
本页的三处**参数顺序**（`DFPN` / `DFPS` / `DFAN`）就是这一档，见「对不上的地方」⑥。
**它比①②③都硬**（图是文档自带的，不是我的推断），**但它不可检索**——
**理由和写法见 `schema.md` §11.4**；要点是：**必须写清是哪张图，并说明图里的字 grep 不到。**

> **这一档是被一个假说法挡了很久才补上的。** 本页原先写着「图片路径在语料树之外，
> 所以本页没有任何来自图的结论」——**路径是对的、图是读得出来的**（§11.4）。
> **一个不成立的理由，会把一整档证据永久关在门外。**

## 对不上的地方

**① L3 整列是 `—`，这是结论不是缺口。** §6 把 `L3` 定义成「调用者是**外部进程**」
（TPI / HVM / test suite control）。pin 定义是 **setup 期的动作**，发生在
SmarTest 自己的 setup 流程里，**外部进程插不进来**——所以这一列不是「没找到」，是**不存在**。

**② L2 整列几乎全空，这是 pin 这一段的结构事实。** pin 是**定义**动作，
而 L2 是**在 test method 里调用**的动作。定义好了以后，test method 侧用的是另一批东西
（`CONF` 生效后的 pin 状态、DC Scale 的 limits、virtual pin 的记结果）。
主表里 L2 有值的四行，**恰好全是「定义完之后在测试里要用」的那些点**——
负载电容、DC Scale 限值、虚拟 pin、protocol——**这个分布本身就是一条信息**。

**③ `PSSL` 那一格是 `?`，因为**「DC Scale Limits editor ↔ `PSSL`」**这个对应语料没说。**
`PSSL` 自己的文档（`02.06.02.02.…PSSL…`）说它是给 DPS power pin 与 DC signal(PMU) pin
设安全限值，而 `DC_Scale_Limits_editor` 那篇**只链到 L2 的 `EVENT_ICVM`/`EVENT_ICIM`**，
**一条 L1 链接都没有**。两者看起来像同一件事，但**看起来像不算证据**——§2.5 的规矩是「不许猜」。

**④ `02.08.04.18.05` 有一处语料错字，本页照实记下、没替它改**：

> 「The Setup Management Tool uses the master file to assemble the in configuration files.」

**`the in configuration files` 应为 `the pin configuration files`。**
本页把它原样留在引文里（**引文不许替语料修字**，§11.2）。

**⑤ `RDIV` / `DDSL` / `DFAN` 三条命令无处安放**（见上「表里没有的」）：
它们**确实在 pin 配置文件的例子里**，但**pin 那页没把它们收进「涉及对象」，
也没有任何 GUI 文档提到它们**。本页**不把它们塞进表里凑数**。

**⑥ 图能读，这一页读了——原先这里写的「图在语料树之外」是错的。**（**2026-09-20 更正**）
`02.08.04.18.04` 的 `## Example` 里有三张图（`21671.png` 数字、`105641.png` DPS、`105640.png` 模拟），
原文说它们「show the pin setting and the contents of the related pin configuration file」。
**图片路径 `../../../../raw/` 往上四层正好是 `tdc-html/`——文件就在那儿**
（`tdc-html/raw/` 里 5,193 张 png）。**三张都读了**，它们把**参数顺序**钉死了：

| 图（GUI 的列） | 文件里那一行（同篇 `## Example`） | 得出的参数顺序 |
|---|---|---|
| Digital Pins：`Name`=`IAQ_D8`、`NO`=`108`、`Tester Channel`=`10208` | `DFPN 10208,"108",(IAQ_D8)` | **`DFPN <Tester Channel>,"<NO>",(<Name>)`** |
| DPS Pins：`Name`=`VCC1`、`Polarity`=`POS`、`Tester Channel`=`DPS11` | `DFPS 11,POS,(VCC1)` | **`DFPS <Tester Channel 里的数字>,<Polarity>,(<Name>)`**（`DPS` 前缀**不进文件**） |
| Analog Pins：`Name`=`input_a_1`、`NO`=`232`、`Type`=`i`、`Instrument`=`MCB` | `DFAN "MCB231,1,i","232",(input_a_1)` | **`DFAN "<Instrument><n>,<序号>,<Type>","<NO>",(<Name>)`** |

> ⚠️ **2026-09-20 重要更正：这三张图是 7.1.3 之前的界面截图，上表里的列名是旧名。**
> `02.08.04.18.03.01.03_DPS_Pins_editor` 的 `## Functional changes` 明写三条 7.1.3 的改名：
> **`Polarity` → `Pol`**、**`Load Capacitor [uF]/V-Ramp [us]` → `C[uF]`**、**`Instrument` → `HW`**。
> **本 wiki 面向 7.10.3，所以上表 DPS 那一行的列名要按 `Pol` / `C[uF]` 读**；
> **`Pol` 也只是取值 `POS` 的旧写法，正文的 `Pol` 列定义表列名同样改过。**
> **参数顺序的结论不受影响**（三段形状新旧两版都成立：新版 `354609.png` 上 `Name`=`PWR`、
> `Pol`=`POS`、`Tester Channel`=`22510`，同一条 `DFPS <数>,POS,(<Name>)` 照样对得上），
> **但「列名」这一半必须按当前版本写。**

> ⚠️ **2026-09-20 补第二条更正：`Ser.R[ohm]` 在 7.1.3 是「被删掉」，不是「改了名」。**
> 上面那三条改名引自 **`DPS_Pins_editor`** 一篇；**7.1.3 对 pin 编辑器的改动不止那三条**——
> **`Digital_Pins_editor`**（`02.08.04.18.03.01.02`）的 `## Functional changes` 里还有一条：
> `SmarTest 7.1.3: Removed the parameter Ser.R[ohm].`
> **实测全语料 4 处命中**（另有 `02.08.04.18.02.07.03_Defining_a_context` /
> `…02.07.04_Defining_additional_test_sites` / `03.05.01.02_Configuring_the_pins_for_a_dynamic_DC_test`，
> 措辞都是 `Removed the parameter Ser.R[ohm] from Digital Pins editor.`）。
> **为什么这一条要单独写、而不是并进上面那张改名表**：
> **「改名」和「删除」在对表里的处置是相反的**——
> 改名 → **表里继续写这一行，只换列名**（`Polarity`→`Pol`）；
> 删除 → **这一行要标「7.1.3 起不存在」**，因为它**没有新名字可换**。
> 把删除混进改名表，读的人会以为去找个新名就行。**本页这张表里原来没有这一行，所以上面那张表不受影响**；
> 记在这里，是为了**别让「7.1.3 的改动 = 三条改名」这个印象留在页面上**。

> ⚠️ **2026-09-20 补第三条：旧图上的 `MSDPS` / `DPS11` 在当前文档里找不到对应，本页照实说。**
> 两个串都是**从旧截图（`105641.png` 那张 DPS Pins）的 `Tester Channel` 列里读到的**，
> 而**在当前版本的 DPS Pins editor 文档里找不到它们**：
>
> | 串 | 全语料命中 | 命中的是什么 | 与当前 DPS Pins editor 的关系 |
> |---|---|---|---|
> | `MSDPS` | **1** | `02.09.01.16.03_How_to_collect_the_hardware_and_software_configuration_with_HVM_API` 里的 `HW Type: MSDPS` | **是硬件型号串**，不是列取值——**本页不把它接成列** |
> | `DPS11` | **3** | 全在 `02.08.01.03.03.02_Pins_and_port_for_Digital_Source_Memory`（**Digital Source Memory** 那一侧） | **不是 DPS Pins editor 的写法** |
>
> 而当前 `02.08.04.18.03.01.03_DPS_Pins_editor` 对 `Tester Channel` 列**只有一句**
> 「Specify a DPS channel.」，**没有给任何取值形状**；新版截图（`354609.png`）上这一列是**纯数字**（`22510`）。
> **所以：`DPS11` 那种「字母前缀 + 序号」是旧界面的写法，7.1.3 之后的列里没有它的位置。**
> **本页不为这两个串猜一个映射**——**图上读到的字在 raw 里 grep 不到，这一档（④ 图证）
> 本来就不能靠检索复核**，所以照实记「找不到对应」比编一个对应更可信。

**图还印证了表里已经写着的一行**：DPS 图上 `Load Capacitor [uF]` 那列（值 `0.1`）
**没有出现在 `DFPS` 行里**。
**⚠️ 2026-09-20 收窄**：本页原先直接写「它是**另一条命令**（`PSLC`）」——**图只能证明 `0.1` 不在 `DFPS` 行里**，
「那条命令就是 `PSLC`」**是（推断）**（依据是本页表里 `PSLC` 那一行的 ② 档链接）。
**图证与链接证是两档，本页原先把它们写成了一档。**

**图证答不了的两件事，照实说：**

- 模拟那张图的 `Tester Channel` 分成 **`Pogo`**（`23116` / `23114`）与 **`Pad`**（`S2`）两格。
  **⚠️ 2026-09-20 更正**：本页原先写「`Pogo` 那两个数在 `DFAN` 行里找不到」——**那是错的**。
  `23116` / `23114` 是 **pogo block `231` + 块内通道 `16` / `14`**，
  而 **`231` 就在 `DFAN` 行的 `MCB231` 里**——**所以 pogo block 是能从行里回收的**，
  **只有块内那两位和 `Pad`（`S2`）不在**。（把 `231` 读成 pogo block 是**推断**：
  依据是图上两行的 pogo 值共享 `231`、两行 `DFAN` 都写 `MCB231`，
  且 `02.08.04.18.03.01.02` 说 pogo block 的范围是 `201…232`、含 `231`。）
  **这条错是 `pin-configuration-file` 那页的 agent 查出来的**——它核对本页三条公式时发现的。
- **图是「某一次具体配置」的截图，不是格式规范。** 「哪些列必填、哪些组合非法」**图答不了**
  ——那是文本的事，而文本在这一点上也没写全。
- **多 site 的时候 `DFPS` 那行怎么写，本页的公式覆盖不到**（**2026-09-20 补记**）。
  本页的 `DFPS <一个数字>,...` 是从**单 site** 的旧截图（`105641.png`，只有一个 `Site1` 子列）得出的；
  而 `dps-pins-editor` 那页的新截图（`354609.png`）显示 **`Tester Channel` 按 site 拆成 `Site 1`/`Site 2` 两列，
  同一根针两 site 的值可以不同**（`PWR` 那行是 `22510` / `22511`）。
  **所以多 site 时 `DFPS` 行怎么写，本页没有依据**——
  **要去 `02.08.04.18.04` 的多 site 例子里核**（本页没核）。**这条是 `dps-pins-editor` 那页的 agent 报上来的。**

**证据分档因此多一档**（`schema.md` §11.4）：**④ 图证**——**比①②③都硬**（图是文档自带的，
不是我的推断），**但它不可检索**：**拿图里读到的字去 raw 里 grep 是 grep 不到的**，
要核只能自己再去开那张图。**这两件事必须分开说，才是诚实的。**

## 出处

`sources:` 十四篇，**全部是 `02.08.04.18` 这一族的 GUI/文件文档**（见 frontmatter）。
引文只来自其中**两篇**（`02.08.04.18.04` 与 `02.08.04.18.05`），**那两篇是整篇读完的**；
其余十二篇**只读了它们互相之间的链接**（`edges.jsonl`），**没有读正文**。

**本页没做的**：

- **一条 L2 API 文档都没读。** 主表 L2 列里那些名字（`EVENT_ICVM.limits`、
  `SPMU_PIN_TASK.loadCap`、`SMC_TEST()`…）**是从链接里取的**，
  **它们自己的参数、返回值、用法，本页一个字没有**。
- **`02.06` 的命令页一篇没读。** 主表 L1 列的命令名与一句话职责，转自
  `wiki/stages/pin.md` 的「涉及对象」节（那页建页时读的），**本页没有回到命令原文复核**。
- **`02.07.11.01.09` 那一族（`Pin_role`/`Protocol`/`Transaction`）只见到链接。**
  **它们和 `DFPR`（DeFine Pin Role）是不是同一个「role」，本页没查、也没敢合并**——
  `DFPR` 在 `pin.md` 里被记成「定义 pin alias」，而 `02.07.11.01.09.08` 叫 `Pin_role`，
  **两个词面相同、位置不同（02.06 vs 02.07.11），本页按「同名不同物」处理，L1 格留 `?`。**
  这一条**值得后续单独查一次**。
- **没有实跑。** 没有在机台上开过任何编辑器、没有生成过 pin 配置文件、
  没有用 `extract/wiki-plan.csv` 之外的任何数据校对过本表。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pin.md`。
  后者是**待办**：pin 那页目前不知道本页存在。

**本页 `layer: n/a` 的理由**：§6 要求 mapping 页必填 `layer`，而本页**本身不属于任何一层接口**
（它是对照表，不是接口）——`n/a` 是这个六值枚举里为这种情况准备的值。

`verified: doc-only`
