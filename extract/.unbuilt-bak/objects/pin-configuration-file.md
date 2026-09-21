---
type: object
title: Pin configuration file
layer: file
stage: pin
tags: [pin-configuration-file, pin, file, firmware-command, setup, master-file, mtl, memory-test, pin-mapping]
related: [pin, pin-configuration-tool, pin-configuration-master-file, setup-management-tool, pin-mapping-file, mapping-pin, device-directory, dfpn, dfps, dfpt, dfpr, pste, conf, digital-pins-editor, dps-pins-editor, utility-pins-editor, pin-group-editor, port-editor, alias-set-editor, multiport-burst-editor, mtp-memory-test, mtpt, smartest-6.3.2, smartest-6.5.2, smartest-7.10.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.09.01_Pin_configuration_file.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Pin configuration file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,664 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

- The figures below show the pin setting and the contents of the related pin configuration file. !`A mixed-signal pin configuration example - digital pins`（raw: `../../../../raw/21671.png`）   !`A mixed-signal pin configuration example - DPS pins`（raw: `../../../../raw/105641.png`）   !`A mixed-signal pin configuration example - analog pins`（raw: `../../../../raw/105640.png`）

```
hp93000,config,0.1
DFPN 10208,"108",(IAQ_D8)
DFPN 10207,"107",(IAQ_D7)
DFPN 10206,"106",(IAQ_D6)
DFPN 10205,"105",(IAQ_D5)
DFPN 10204,"104",(IAQ_D4)
DFPN 10203,"103",(IAQ_D3)
DFPN 10202,"102",(IAQ_D2)
DFPN 10201,"101",(IAQ_D1)
DFPN 10403,"",(WDA_TRIG)
DFPN 10401,"",(WDB_TRIG)
DFPS 11,POS,(VCC1)
DFPS 12,POS,(VEE)
DFPS 14,POS,(DRC_IN_TERM)
DFAN "MCB231,1,i","232",(input_a_1)
DFAN "MCB231,2,i","234",(input_a_2)
PSTE 1
CONF OFF,F160,(IAQ_D8,IAQ_D7,IAQ_D6,IAQ_D5,IAQ_D4,IAQ_D3,IAQ_D2,IAQ_D1,
    WDA_TRIG,WDB_TRIG)
RDIV 0,(IAQ_D8,IAQ_D7,IAQ_D6,IAQ_D5,IAQ_D4,IAQ_D3,IAQ_D2,IAQ_D1,
    WDA_TRIG,WDB_TRIG)
DDSL 0,(VCC1)
DDSL 0,(VEE)
DDSL 0,(DRC_IN_TERM)
PSLC 0.1,(VCC1,VEE,DRC_IN_TERM)
NOOP "6.1.0",,,
```

- The following lines shows a multi-port pin configuration file. The firmware command DFPT is used to define ports.

```
hp93000,config,0.1
DFPN 10102,"12",(CP_1)
DFPN 10302,"12",(CP_2)
...
DFPT (CP_1,DS7_1,DS0_1,I/O7_1,I/O6_1,I/O5_1,I/O4_1,I/O3_1,I/O2_1,
    I/O1_1,IO0_1,Q7_1,Q0_1,S1_1,S0_1,_MR_1), (port_1)
DFPT (CP_2,DS7_2,DS0_2,I/O7_2,I/O6_2,I/O5_2,I/O4_2,I/O3_2,I/O2_2,
    I/O1_2,I/O0_2,Q7_2,Q0_2,S1_2,S0_2,_MR_2), (port_2)
...
```

Note You can use a text editor instead of the Pin Configuration Tool to create or edit a pin configuration file in the form of a set of firmware commands.

<!-- 语法节 end -->

## 是什么

**一句话：pin configuration file 是 Pin Configuration 工具把界面上填的东西落盘成的那个文件，内容是「一族固件命令」，一条命令对着界面上一个参数。** 地点和内容原文各一句：

> 「The Pin Configuration tool stores the data in the pin configuration file located in the directory:」

> 「<device_dir>/configuration」

> 「The file contains a set of firmware commands corresponding exactly to the parameters specified within the Pin Configuration tool.」

**第三句里的 `corresponding exactly to` 是本页的地基**：不是「有关」，是**逐条对应**——界面上填的每一个参数，文件里都有一条对应的固件命令。**但它只钉住「Pin Configuration 工具 ↔ 本文件 ↔ 固件命令」这一整条链**，**没有逐条说「哪个编辑器对应哪条命令」**——那个更细的粒度语料没写（本页也不推）。

### 三张图把这条「逐条对应」并排摆了出来（④ 图证）

`02.08.04.18.04` 的 `## Example` 一开头就是三张图，原文一句话说它们是干什么的：

> 「The figures below show the pin setting and the contents of the related pin configuration file.」

**「the pin setting」和「the contents of the related pin configuration file」并排**——三张图正是 **GUI 表格与文件内容的对照**。（读法见 `schema.md` §11.4：图片路径 `../../../../raw/x.png` 往上四层就是 `tdc-html/`，**文件就在那儿，`Read` 直接打得开**。）**三张逐张打开核对过**：

| 图（GUI 上那一行） | 同篇例子里那一行（文件） | 由此定下来的参数顺序 |
|---|---|---|
| `21671.png`（`Digital Pins`）：`Name`=`IAQ_D8`、`NO`=`108`、`Tester Channel`=`10208` | `DFPN 10208,"108",(IAQ_D8)` | **`DFPN <Tester Channel>,"<NO>",(<Name>)`** |
| `105641.png`（`DPS Pins`）：`Name`=`VCC1`、`Polarity`=`POS`、`Tester Channel`=`DPS11` | `DFPS 11,POS,(VCC1)` | **`DFPS <Tester Channel 里的数字>,<Polarity>,(<Name>)`**（`DPS` 前缀**不进文件**） |
| `105640.png`（`Analog Pins`）：`Name`=`input_a_1`、`NO`=`232`、`Type`=`i`、`Instrument`=`MCB`、`Tester Channel` 的 `Pogo` 格=`23116` | `DFAN "MCB231,1,i","232",(input_a_1)` | **`DFAN "<Instrument><pogo block>,<序号>,<Type>","<NO>",(<Name>)`** |

**这三行是本页「逐条对应」唯一的实物证据**：原文只声明了这条链，**一条命令的参数顺序都没写**；顺序是这三张图钉住的。**（同一条结论 [[mapping-pin]] 那页也记了；本页不引它的文字，是自己把三张图重核了一遍。）**

**图里读出来、raw 文本里 grep 不到的字**（grep 不到才叫图证）：`PS3600`、`MSDPS`、`23116`、`23114`、`Ser.R[Ohm]`、`Pogo`、`Pad`——**这些字符串在 `02.08.04.18.04` 这篇里一次都不出现**。（`10208` / `IAQ_D8` / `MCB231` 这些**是**搜得到的，它们在例子的代码块里；**图给的不是这些字，是它们的对齐方式**。）

**图还多给了一条文本没写的关系**——**（推断）`DFAN` 第一格里 `MCB` 后面那个数就是 pogo block 号**。依据两条：① 模拟那张图两行的 `Pogo` 值是 `23116` / `23114`，**前三位都是 `231`**，而 `DFAN` 两行第一格都写 `MCB231`；② **同篇系统参考的另一篇**（`02.08.04.18.03.01.02_Digital_Pins_editor.md`，**不是本篇**）说五位数 channel-ID 是 `aaabb`、`aaa` 就是 pogo block，而它给的范围 `201 ... 232` 里正含 `231`。**但块内那两位（`16` / `14`）和 `Pad` 格（`S2`）在 `DFAN` 行里都没有**——**语料没说这两处落在哪条命令里，本页不替它接。**

**图同时说明「文件里没有的东西」**：数字那张图上有 `Instrument`（`PS3600`）、`Mode`（`std`）、`Ser.R[Ohm]`（`0.0`）三列，DPS 那张上有 `Instrument`（`MSDPS`）与 `Load Capacitor [uF]`（`0.1`），**这些值都不在各自对应的 `DFPN` / `DFPS` 行里**。（**（推断）** DPS 那个 `0.1` 可能落在同篇例子的 `PSLC 0.1,(VCC1,VEE,DRC_IN_TERM)` 上——依据只是两处都写着 `0.1`；**语料没有一句话把这两者连起来，所以这只是推断。**）

### 页名撞车：语料里有两个「Pin configuration file」

`sources:` 三篇里，**两篇的标题一模一样，说的却不是同一件事**：

| 出处 | 它给的身份标记 | 它说这个文件干什么 |
|---|---|---|
| `02.08.04.18.04`（系统参考 → Setup and Result Tools） | 落点 **`<device_dir>/configuration`**；**没写扩展名** | 含一族固件命令，与 Pin Configuration 工具里的参数**逐条对应** |
| `02.12.03.03.09.01`（Memory Test Plus 7.10.2） | **有 `.pin` 扩展名**（`The pin configuration file has the .pin file name extension.`）；**没写落在哪个目录** | 「A pin configuration file specifies which pins are available on the DUT.」 |
| `02.08.04.18.05`（系统参考） | 讲的是**它的 master file**（拆成多份时的入口） | 见下「一份还是几份」 |

**两者是不是同一个文件——本页三篇里没有一句话回答。** 拿得出来的只有两条间接线索：

- MTP 那篇说这个文件是 `generated within SmarTest when the pins of the device are defined`，并且链到 `Setting the DUT Pin Configuration`（→ `02.08.04.18_Pin_configuration_tool.md`）——**指的是系统参考那篇说的同一个工具**。
- 系统参考那篇给了**目录**（`<device_dir>/configuration`）、MTP 那篇给了**扩展名**（`.pin`）——**两者不冲突，因为谁都没写「完整的文件名是什么」**。

**（推断）这两篇讲的很可能是同一件东西在两个产品线文档里的两次描述**，依据就是上面两条线索。**原文没有一处把两条身份合起来说过，也没有任何一篇提到另一篇，所以这只是推断。**

**（建议）拿到这个文件先确认你在读哪一篇的说法**：系统参考那篇讲的是**它怎么被生成**（GUI 工具落盘，或用文本编辑器手写），MTP 那篇讲的是**它被谁引用、什么时候必须引用**。两篇互补，**但混着当一份规格读，就等于替语料做了它没做的合并。**

### 「语法 / 参数」节里是什么（脚本抽的，本节只导读）

`02.08.04.18.04` **没有 `Syntax` / `Parameters` 段**，它只有 `## Example` 和 `## Functional changes` 两个 `##` 段。脚本按段标记收的是 **`## Example` 整段**（1,664 字符）——**所以这一页的语法节不空**，里面是三张图的行 + 两段代码 + 一条 Note。

**第一段代码就是一份真实的 pin configuration file**（一个混合信号器件：数字、DPS、模拟三类 pin 都在同一份文件里）。按行拆开看（**表里的代码行按 §11.1 ① 把原文的换行与行首缩进折叠成了一个空格，字一个没动**）：

| 行 | 例子里原样的一行 | 这一行上有什么 |
|---|---|---|
| 头行 | `hp93000,config,0.1` | 文件第一行 |
| `DFPN` | `DFPN 10208,"108",(IAQ_D8)` | **数字 pin**：channel 号 + pin 号 + pin 名 |
| `DFPN`（pin 号为空） | `DFPN 10403,"",(WDA_TRIG)` | **第二格可以是空串**——同一份文件里两种写法并存 |
| `DFPS` | `DFPS 11,POS,(VCC1)` | **DPS pin**：channel 号 + 极性（`POS`）+ pin 名 |
| `DFAN` | `DFAN "MCB231,1,i","232",(input_a_1)` | **模拟 pin**：**第一格是带逗号的引号串**（板卡、一个序号、方向——**这一格的读法见上一节 ④ 图证**），第二格是 pin 号 |
| `PSTE` | `PSTE 1` | site 数 |
| `CONF` / `RDIV` | `CONF OFF,F160,(IAQ_D8,IAQ_D7,IAQ_D6,IAQ_D5,IAQ_D4,IAQ_D3,IAQ_D2,IAQ_D1, WDA_TRIG,WDB_TRIG)` / `RDIV 0,(IAQ_D8,IAQ_D7,IAQ_D6,IAQ_D5,IAQ_D4,IAQ_D3,IAQ_D2,IAQ_D1, WDA_TRIG,WDB_TRIG)` | **模式（`OFF`）+ 一个 pin 列表**；`RDIV` 用的是**同一批 pin 名**，第一格是 `0` |
| `DDSL` / `PSLC` | `DDSL 0,(VCC1)` / `DDSL 0,(VEE)` / `DDSL 0,(DRC_IN_TERM)` / `PSLC 0.1,(VCC1,VEE,DRC_IN_TERM)` | 也带 pin 列表，**对象是 DPS / 模拟那几个** |
| `NOOP` | `NOOP "6.1.0",,,` | 收尾，**带一个版本串** |

**这张表只说明「例子里哪一行长什么样」，不是参数说明。** `DFAN` / `RDIV` / `DDSL` / `PSLC` / `NOOP` **在本页三篇里一个字的定义都没有**；`DFPN` / `DFPS` / `DFPT` / `DFPR` / `PSTE` / `CONF` 在本 wiki 里另有页，**但那几页本页也没读**（见「和谁有关」）。**所以「`CONF OFF,F160` 的 `F160` 是什么」这类问题，本页答不了。**

**第二段代码是「多 port」的形态**，原文一句带过：

> 「The following lines shows a multi-port pin configuration file. The firmware command DFPT is used to define ports.」

**`DFPT` 那一行的形状是「一串 pin 名，再跟一个 port 名」，两段各包一层括号**（**原文的换行已折叠成空格**）：`DFPT (CP_1,DS7_1,DS0_1,I/O7_1,I/O6_1,I/O5_1,I/O4_1,I/O3_1,I/O2_1, I/O1_1,IO0_1,Q7_1,Q0_1,S1_1,S0_1,_MR_1), (port_1)`。**注意这段代码原文自己就用 `...` 截断了**（`DFPN 10302,"12",(CP_2)` 之后有一行就是 `...`）——**本页照抄，不替它补全。**

**Example 的最后一条是 Note，它说的是「谁可以写这个文件」**：

> 「Note You can use a text editor instead of the Pin Configuration Tool to create or edit a pin configuration file in the form of a set of firmware commands.」

**这条 Note 把本文件的定位说全了：它是文本，格式就是固件命令，GUI 工具只是一个生成器。**（**（推断）**反过来读：只要命令写对，不经过 GUI 也能有合法的文件——**依据就是这条 Note 的字面**；原文没有把「手写的和工具生成的同等有效」写成一句。）

### 一份还是几份：master file

（本节来自 `02.08.04.18.05`。**master file 自己的格式细节归 [[pin-configuration-master-file]] 那一页**，本节只说它和 pin configuration file 的关系。）

> 「A pin configuration can be organized as one single file, or different parts of the pin configuration can be stored in separate files. In the latter case, the respective pin configuration files can be merged through a master file which contains references to the individual files.」

> 「The Setup Management Tool uses the master file to assemble the in configuration files.」

（**第二句里 `the in configuration files` 是语料错字，应为 `the pin configuration files`；本页照原样引，不改**，见「出处」①。）

拆开之后，**每一份都有自己的角色名**：

> 「One of the individual pin configuration files is the "package file", which contains the specification for the complete package. The other files are referred to as "alias files". The pin names in the alias files are taken as pin aliases in the assembled file.」

**为什么要拆，原文只给了一条理由**：

> 「Splitting the pin configuration into multiple individual files allows multiple users to work on the configuration in parallel.」

**拆开有代价：装配时 Setup Management Tool 要过四道校验**（原文：`The Setup Management Tool verifies that the following conditions are true for all files:`）。**这是本页最该记住的一张表——违反任意一条，装配直接中止。**

| # | 条件（逐字原文） | 说的是什么 |
|---|---|---|
| 1 | 「The numbers of sites specified in different files are same.」 | **各文件声明的 site 数必须相同** |
| 2 | 「All the channels in the alias files occur in the package file.」 | **alias 文件里用到的 channel 必须在 package 文件里出现过** |
| 3 | 「The contexts specified in different files are not same, except for the "DEFAULT" context.」 | **各文件的 context 不许重名，`DEFAULT` 除外** |
| 4 | 「The channel must be defined as I/O in the package file to allow both I and O directions for the different alias pins. If the channel is defined to be either only I or only O, then all aliases must have the same specification. None of the aliases must have the opposite direction or I/O.」 | **方向自由度由 package 文件决定**：package 里写成 I/O，alias 才能各取 I 或 O；package 里定死成只有 I 或只有 O，**则所有 alias 必须同规格，且不许出现反向或 I/O** |

> 「If any of the rules is violated, the assembly process is aborted and an error message is generated.」

**装配的产物长什么样，同一篇的例子里有。** package 文件的 pin 名原样保留，**每个 alias 文件贡献若干条 `DFPR`**，把「alias 集合名 + alias pin 名」绑到 package 文件的 pin 名上：

```
DFPR "TRANSIO","Data2",(Data_in_2)
DFPR "USB","Data5",(Data_in_5)
```

**（推断）`DFPR` 是「装配」这个动作留在产物里的痕迹**——依据是**它只出现在标题写明 assembled 的那段例子里**，三个输入（`package.cfg` / `transio_file.cfg` / `usb_file.cfg`）里一条都没有。**原文没有解释 `DFPR`，本页不替它解释。**

### `.pin` 那一边：它怎么被引用

（本节全部来自 `02.12.03.03.09.01`，**语境是 MTP**；**最后一段讲它自带的依赖图，其中另引了一句 `02.12.03.03.01`，那里标明了「不是本篇的句子」**。）

> 「The pin configuration file has the .pin file name extension. It is optionally referenced from the Pin mapping file with the using pinconfig keyword. The reference is needed when a port is specified, usually for multiport operations or Automatic waveform generation.」

**`using pinconfig` 是它在 MTP 那条链上的唯一入口**，而且是**引用方指过来**——文件自己不知道谁在用它。**显式引用不是必须的，只有用到 port 时才需要**（`The reference is needed when a port is specified`）。

**紧接着原文又说了一句口气相反的话**：

> 「Note The pin mapping file always implicitly references the pin configuration file that is currently chosen in SmarTest because, in that file, DUT pin names are assigned to the SmarTest pin names as defined in the pin configuration file.」

**「optionally referenced」（显式引用可选）和「always implicitly references」（隐含引用总有）在同一段里并排。** 严格读可以并存（显式那层可选、隐含那层总有），**但原文没有这样说明**——**本页把两处并列照抄，不替它们调和**（见「出处」④）。

**谁生成它，这一篇也说了**：

> 「Pin configuration files are generated within SmarTest when the pins of the device are defined (see Setting the DUT Pin Configuration for more information).」

**这句和系统参考那篇的 `The Pin Configuration tool stores the data in the pin configuration file located in the directory:` 是同一件事的两种说法**（一个说生成时机，一个说生成者）——**本页并列，不合并。**

**`.pin` 在文件依赖图里排在哪儿——这一篇的图上有（④ 图证）。** `02.12.03.03.09.01` 第一段就挂了那张图（`102576.png`，alt 文字是 `Miniature scheme of file dependencies with .pin file highlighted`）。**图是九个文件格组成的一张依赖图**，按图上位置逐个读出来是：`.tim`（左上）、`.dvar`（中上）、`.dac`（右上）、`.wmap`（左中）、`.apg`（正中）、`.prog`（右中）、`.pin`（左下）、`.pmap`（中下）、`.dcev`（右下）。**九格里只有 `.pin` 那一格被填成橙色**（其余八格淡紫底）——这就是 alt 里 `highlighted` 的意思；**`.pin` 从左列再往下、以及它上方，图上都是空白，没有任何箭头**。**整张图只有一条箭头落在 `.pin` 身上：从 `.pmap` 指过来，而且画的是虚线。** 这与正文那句 `It is optionally referenced from the Pin mapping file with the using pinconfig keyword.` 说的是**同一条边**。**`.pin` 自己没有向外的箭头。**

**这张图本页答不了的部分，照实说**：

- **图没有图例。** 虚线 / 实线各是什么意思，图上没写；**本篇正文对这张图也一个字都没解释**（它只写了 `Miniature scheme`）。**所以「哪条边代表什么关系」本页答不了。**
- **图上另有三四条虚线斜箭头穿过 `.dvar` / `.apg` / `.prog` / `.dcev` 那一簇。** 原图只有 **251 × 151 像素**；放大到 8–14 倍之后，**`.pmap` → `.pin` 这一条能读死，那一簇的方向读不实**——**本页不在读不实的地方硬认**。
- **一个「图与正文写得不一样」的字**：图右上角那一格写的是 **`.dac`**，而语料正文（`02.12.03.03.01`，**不是本篇**）把那个文件叫 **`.dvac`**（那张图自己的 alt 文字也写 `.dac`）。**本页照图记，不替二者统一。**

（**推断**）**虚线标的看起来是「这条边的一端是可选文件」**：本页读出来的三条虚线，端点分别落在 `.wmap` / `.dcev` / `.pin` 上，而 `02.12.03.03.01` 明说这三个文件是 `Optional`（**那句不是本篇的句子**）。**图没有图例，所以这层只是推断，不是文档事实。**

## 典型用法

**本页三篇都没有 `## Procedure`、没有 `## Before you begin`。**（`02.08.04.18.05` 有一个 `## Format of entries`，那是格式定义，不是步骤。）**可操作的规则收成下面四条路径。**

### 一、建成一份（不拆）

1. **用 Pin Configuration 工具填** → 数据落到 `<device_dir>/configuration`（原文：`The Pin Configuration tool stores the data in the pin configuration file located in the directory:`）。
2. **或者用文本编辑器手写**——**格式就是一族固件命令**（那条 Note，见「是什么」）。

**两条路的产物是同一个格式**（推断，依据是 Note 只说「可以用文本编辑器代替工具」，没有说格式不同）。

### 二、拆成几份 + master file

**master file 的行序是固定的**，原文分三段说：

| 位置 | 行 | 依据（逐字原文） |
|---|---|---|
| 第 1 行 | `hp93000,config_master_file,0.1` | 「A pin configuration master file always begins with a header row that must have this content:」 |
| 第 2 行 | `testerfile: <tester_file_name>` | 「The second line specifies the tester file which is to be divided. It has the format:」+「It specifies the tester setup file which is to be split.」 |
| 其后 | `Package: <package_file_name.cfg>`，再是若干行 `alias_set_name_X: <alias_file_name_X.cfg>` | 「The entry format for the parts is as follows:」 |

**三条配套规则**（逐字原文）：

> 「The paths for the subfiles can be relative or absolute. The reference directory for relative paths is the directory of the master file.」

> 「You can insert comments anywhere in the file. They are identified by the hash (#) character at the start of a line.」

> 「The Package keyword refers to the package file. The pin names specified in this file are all used in the assembled file.」

**`Package:` 一条就够，alias 行可以有多条**——原文写 `The subsequent lines in the master file specify that the alias set named with "alias_set_name_X" is generated with the information extracted from the file "alias_file_name_X.cfg".`（**（推断）**「package 唯一、alias 多行」是**从原文 `Package` 用单数、alias 用 `_1` 到 `_X` 的下标读出来的**，原文没有明说这个数量关系。）

### 三、装配（这一步不是人做的）

**装配由 [[setup-management-tool]] 执行**（原文两句：master file `contains references to the individual files`、`The Setup Management Tool uses the master file to assemble the in configuration files.`）。**过不了那四条校验就中止并报错**（四条见「是什么」）。**本页三篇没有给命令行入口，也没有给报错长什么样。**

### 四、MTP 侧：先决定要不要在 pin mapping file 里引用它

- **不用 port**：可以不写引用——**隐含引用总是存在**。
- **要用 port**（`multiport operations` 或 `Automatic waveform generation`）：**必须在 [[pin-mapping-file]] 里用 `using pinconfig` 显式写**（原文：`The reference is needed when a port is specified`）。

**（推断）这两条合起来才是完整规则**，依据是同一段里那两句相反口气的话（显式 + 隐含）；**原文没有把「什么时候必须写」写成一条判据。**

## 和谁有关

**同一件事的另一侧（GUI / 生成侧）：**

- [[pin-configuration-tool]]（**未建**）— **本文件的生成者**。原文 `The Pin Configuration tool stores the data in the pin configuration file`。**但它不是唯一的路**：那条 Note 说可以用文本编辑器代替它。
- [[digital-pins-editor]] / [[dps-pins-editor]] / [[utility-pins-editor]] / [[pin-group-editor]] / [[port-editor]] / [[alias-set-editor]]（**`alias-set-editor` 未建**）— **同 `stage: pin` 的 GUI 侧编辑器族**。**本页三篇一篇都没点名它们**——这条关系是**推断**，依据是 [[pin]] 那页把这些编辑器列为本阶段 GUI 侧（**依据来自别页，不是本页的 sources**）。**所以「哪条命令出自哪个编辑器」本页不主张。**

**拆文件时的另一半：**

- [[pin-configuration-master-file]]（**未建**）— **拆成多份时的那份入口文件**，原文叫它 `a master file which contains references to the individual files`。**它的行格式、`testerfile:` 的语义、`package.cfg` / `transio_file.cfg` / `usb_file.cfg` 三个示例，全部在 `02.08.04.18.05` 里**——本页只讲「它和 pin configuration file 是什么关系」，**格式细节归那一页。**
- [[setup-management-tool]] — **唯一执行装配、也是四道校验执行者的角色**（原文：`The Setup Management Tool uses the master file to assemble the in configuration files.` / `The Setup Management Tool verifies that the following conditions are true for all files:`）。**反过来，那一页自述 master file 机制并不在它自己那篇的正文里**（**这句转自 [[setup-management-tool]] 那页，不是本页 sources 的内容**）——**两页是同一条机制的上下两端，谁都不完整。**

**文件链上的位置（MTP 侧）：**

- [[pin-mapping-file]] — **本文件在 MTP 链上的引用方**（原文：`It is optionally referenced from the Pin mapping file with the using pinconfig keyword.`）。**那一页自述两边的语法相近但不完全相同**（**这句话是转述 [[pin-mapping-file]] 那页的内容，不是本页 sources 的原文**）——**差在哪儿，两篇都没写。**
- `Multiport operation` / `Automatic waveform generation`（**均未建、未读**，raw: `02.12.03.04.14_Multiport_operation.md` / `02.12.03.04.03.03_Automatic_waveform_generation.md`）— **「用 port 就必须显式引用本文件」的两个场合**（原文：`usually for multiport operations or Automatic waveform generation`）。
- [[mtp-memory-test]] / [[mtpt]] — 第三篇 source 在 `02.12_Memory_Test_Plus_7.10.2` 下，**本文件在 MTP 里的用法是它讲的**。
- `SmarTest files` / `MTL Configuration Files`（**均未建、未读**，raw: `02.12.03.03.09_SmarTest_files.md` / `02.12.03.03_MTL_Configuration_Files.md`）— 原文 `## Related information` 那三个同级入口里的两个（**第三个是上面那条 `Pin configuration tool`**；**三个链接之间没有分隔符**，见「出处」③）。
- [[device-directory]] — 本文件的落点 `<device_dir>/configuration` 属于它那套目录结构。**本页没读那篇**，所以 `configuration` 在那套结构里是第几层、里面还有哪些文件，**本页不知道**。

**文件里逐行出现的固件命令（本页只有「它出现在哪一行」的证据）：**

- [[dfpn]] / [[dfps]] / [[dfpt]] / [[dfpr]] / [[pste]] / [[conf]] — **例子里逐行出现的命令**（**`DFPS` / `DFPT` / `DFPR` 未建，但它们在 allowlist 里，所以照链**）。**它们各自的参数定义在命令自己的文档里，本页三篇一个字都没有**；**本 wiki 里有页的只有 [[dfpn]] / [[pste]] / [[conf]]，而这三页本页也没读。**
- `DFAN` / `RDIV` / `DDSL` / `PSLC` / `NOOP` — **同样在例子里逐行出现，但语料里没有参数说明，本 wiki 也没有对应页名**——**本页用反引号写名字，不链**（§9.1：清单外的名字不造悬空目标）。
- [[pin]] — 本页 `stage: pin` 的落点页。
- [[smartest-6.3.2]] / [[smartest-6.5.2]] / [[smartest-7.10.2]] — 见下节。

## 版本

**三篇都有 `## Functional changes` 段，各一条，其中两条是同一个哨兵值**：

| 出处 | 条目（逐字） |
|---|---|
| `02.08.04.18.04` | `- Introduced before SmarTest 6.3.2` |
| `02.08.04.18.05` | `- Introduced in SmarTest 6.5.2` |
| `02.12.03.03.09.01` | `- Introduced before SmarTest 6.3.2` |

> **两条 `Introduced before SmarTest 6.3.2` 是哨兵值，不是「6.3.2 新增的」。** 措辞是 `before`，意思是「**在本文档集覆盖范围开始之前就已经有了**」（§11.2 ②）。**照字面读会凭空造出一条「SmarTest 6.3.2 新增了 pin configuration file」的假信息，而且格式齐整。**

**唯一一条真正的版本信息是中间那条：master file（把 pin 配置拆成 package + alias 再装配的机制）是 SmarTest 6.5.2 引进的。**

**（推断）**把两条并起来能读出一层意思：**pin configuration file 本身在 6.3.2 之前就有，而「拆成多份 + master file 装配」是 6.5.2 才加的**——依据就是一条写 `before`、一条写确定版本号。**原文没有把两者放在一起说过，所以这层意思是推断，不是文档事实。**

**产品线不一致（§11.2 ④）**：第三篇挂在 `02.12_Memory_Test_Plus_7.10.2` 目录下（MTP 7.10.2），而它的 `## Functional changes` 说的是 `SmarTest 6.3.2`。**两者不是一个产品线，本页并列记下，不替它们对齐。**

## 出处

`sources:` 三篇，**三篇都整篇读完**（前缀 `02_System_reference/`）：

| 路径 | 规模 | `## Functional changes` |
|---|---|---|
| `02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.md` | 65 行 / 2,258 字节 | `Introduced before SmarTest 6.3.2` |
| `02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.md` | 140 行 / 4,847 字节 | `Introduced in SmarTest 6.5.2` |
| `02.12_Memory_Test_Plus_7.10.2/02.12.03.03.09.01_Pin_configuration_file.md` | 24 行 / 1,578 字节 | `Introduced before SmarTest 6.3.2` |

**本页做了什么（2026-09-20 更新，原「四张图一张没看」那条是错的，已删）**：

- **四张图都看了，逐张打开过。** `02.08.04.18.04` 的三张（`21671.png` 数字 pin、`105641.png` DPS pin、`105640.png` 模拟 pin）+ `02.12.03.03.09.01` 的依赖图（`102576.png`）。**路径 `../../../../raw/x.png` 往上四层正好是 `tdc-html/`，图就在那儿**（`schema.md` §11.4）——**本页原先写的「在语料树之外」是个不成立的理由，删掉。**
- **图答掉的两件事写进了正文**：① 「GUI 的哪一列对应文件的哪一行」——三张图与同篇例子并排，**把 `DFPN` / `DFPS` / `DFAN` 三条命令的参数顺序钉死了**（见「是什么」的 ④ 图证表）；② `.pin` 在文件依赖图里的位置（左下、唯一被高亮的一格、只有一条从 `.pmap` 来的虚线箭头，见「`.pin` 那一边」）。
- **图里读到的字一律没有进 `>` 引文块。** 引文块的含义是「这段能在 raw 文本里搜到」；**图上的字搜不到**，所以它们只出现在正文和表格里。逐个核过：`PS3600` / `MSDPS` / `23116` / `23114` / `Ser.R[Ohm]` / `Pogo` / `Pad` 在 `02.08.04.18.04` 里**都是 0 次**（`Ser.R` 那一处 raw 写的是小写 `Ser.R[ohm]`，在**另一篇**的版本行里）。
- **图答不了的，照实写了，没有硬填**：依赖图**没有图例**（虚线/实线的含义图上没写、本篇正文也没解释）、**斜箭头那一簇在 251 × 151 像素上读不实**、`DFAN` 行里**没有** pogo 的块内两位与 `Pad` 格、`Load Capacitor [uF]`（`0.1`）与 `PSLC` 的关系**只是推断**。
- **为核图，本页另外开了两篇不是 `sources` 的文档**：`02.12.03.03.01_Overview_of_configuration_files.md`（整篇读完，用来核依赖图的节点是哪些文件、以及哪个标着 `Optional`）与 `02.08.04.18.03.01.02_Digital_Pins_editor.md`（整篇读完 + 它的界面图 `355141.png`，用来试核瑕疵⑧）。**两处都只取单点事实，没有并入正文；用到的都在正文里标了「不是本篇的句子」或「不是本篇的图」。**
- **语法 / 参数节一个字没改，但比对过一次。** 折叠空白、排除脚本改写的三处图片标记之后，raw `## Example` 段的词**全部**能在语法节里找到（158 个词里对不上的 6 个 token，全是三张图的重写形态）。**这一节是脚本产物，本页只做了上述比对，没有回写任何内容。**
- **三篇里的语料内部链接目标，一篇都没读**：`Setting the DUT Pin Configuration`（→ `02.08.04.18_Pin_configuration_tool.md`）、`Pin mapping file`（→ `02.12.03.03.06`）、`Multiport operation`、`Automatic waveform generation`、`SmarTest files`、`MTL Configuration Files`、`Setup Management Tool`（→ `01.01.07.02.02.04`）。**所以「`using pinconfig` 具体怎么写」本页没有**（**「在依赖图里和谁相邻」现在有了，但那只来自图，不是来自这些目标文档**）。
- **`02.08.04.18.05` 没有子主题、全篇只有一条对外链接**（就是正文里那个 `Setup Management Tool`）——**所以 master file 这一块没有更细的下游可看，本页（和 [[pin-configuration-master-file]]）就是它的最细一层。**
- **本页正文的事实来自上面三篇 + 它们自带的四张图。** 别的 wiki 页（[[mapping-pin]] / [[pin-mapping-file]] / [[setup-management-tool]] / [[pin]] / [[pste]] / [[psfc]] / [[digital-pins-editor]] / [[conf]]）**只用来交叉「关系」那一层**，凡用到都在「和谁有关」里注明了出处，**没有把它们的结论搬进正文**；**④ 图证那几条是本页自己重核的，不是从 [[mapping-pin]] 搬的**（那页也记了同一组结论，两处独立）。
- **没有实跑**：没在机台上生成过 pin configuration file，没手写过固件命令，**没用 Setup Management Tool 装配过 master file，也没有故意违反那四条校验去看 `an error message is generated` 是什么样子**。**全部是文档事实 + 图证（`verified: doc-only`）。**
- **例子之外一个例子都没补。** `DFAN` / `RDIV` / `DDSL` / `PSLC` / `NOOP` 在语料里**只有「出现过」，没有参数定义，本页不替它们编。**

> ⚠️ **本页三篇的语料瑕疵，照实记，一处都没替它改**：

> ① **`02.08.04.18.05` 有错字**：

> 「The Setup Management Tool uses the master file to assemble the in configuration files.」

> ——**`the in configuration files` 应为 `the pin configuration files`**。本页在「是什么」里照原样引。

> ② **同一篇里，同一个 alias 文件有两个名字，而且代码跨度里混进了一个逗号**：正文写 `` `TRANSIO.cfg` `` 与 `` `USB.cfg,` ``（**逗号在反引号里面**），而它自己的小节标题是 `### transio_file.cfg` / `### usb_file.cfg`，master file 例子里写的是 `TRANSIO:transio_file.cfg` / `USB:usb_file.cfg`。**`TRANSIO.cfg` 和 `transio_file.cfg` 谁是对的，原文没说**——本页两处都照抄，不替它统一。

> ③ **`02.12.03.03.09.01` 的 `## Related information` 里三个链接之间没有任何分隔符**：`[SmarTest files](<02.12.03.03.09_SmarTest_files.md>)[MTL Configuration Files](<02.12.03.03_MTL_Configuration_Files.md>)[Pin configuration tool](<../02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.md>)` ——**渲染出来是三个名字连成一句**。本页照抄，不替它加分隔。

> ④ **`02.12.03.03.09.01` 同一段里两句口气相反**（原句见「是什么」）：一句 `It is optionally referenced from the Pin mapping file with the using pinconfig keyword.`，一句 `The pin mapping file always implicitly references the pin configuration file that is currently chosen in SmarTest because, in that file, DUT pin names are assigned to the SmarTest pin names as defined in the pin configuration file.`。**「可选」与「总是隐含」并排**——**严格读可以并存，但原文没有说明**；本页并列照抄，不替它调和。

> ⑤ **`02.08.04.18.05` 的示例与它自己声明的格式在空格上不一致**：声明的是 `testerfile: <tester_file_name>` 与 `Package: <package_file_name.cfg>`（**冒号后有空格**），例子里写的是 `testerfile:demo.cfg` 与 `Package:package.cfg`（**冒号后没有空格**）。**原文没说空格可省**——本页照抄两处，不判哪一处是笔误。

> ⑥ **`02.08.04.18.04` 有一处主谓不一致**：`The following lines shows a multi-port pin configuration file.` ——**`shows` 应为 `show`**。本页照原样引。

> ⑦ **`02.12.03.03.09.01` 里同一个目标挂了两个不同的链接文本**：`Pin configuration tool` 与 `Setting the DUT Pin Configuration` **指向同一个文件**（`../02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.md`）。**是不是同一个东西，原文没说**；本页按「同一目标的两种叫法」记，不合并。

> ⑧ **`02.08.04.18.04` 的两条 `DFPT` 例子里，同一类 pin 名少了一个斜杠**：port_1 那一行写的是 `I/O1_1,IO0_1,Q7_1`，port_2 那一行写的是 `I/O1_2,I/O0_2,Q7_2`——**`IO0_1` 比 `I/O0_2` 少一个 `/`**。两行结构完全相同，所以这是**不一致**；**原文没说哪个是笔误，本页照抄，不替它补斜杠**（语法节里那两行也是原样）。

> ⑧ 的**补记（2026-09-20）**：为核这一条，本页打开了另一篇（`02.08.04.18.03.01.02_Digital_Pins_editor.md`）里的界面图 `355141.png`——**（推断）图上那 15 行的 pin 名与这两条 `DFPT` 例子里的名字逐个对得上**（只多一个 `IO0`），而图上 `I/O7` … `I/O1` **七个都带斜杠**（放大到 5 倍逐个核过）。**但那张图只列到第 15 行，`IO0` 那一行不在画面里——所以这一条图核不了**：`IO0_1` 该不该带斜杠，**图答不了，本页照旧不替语料补。**（这张图本身的事另记在 [[digital-pins-editor]] 那页。）

> **另外记一条「不是瑕疵」的事实**：**本页三篇一个坏字都没有。** 按 §11.2 的判据（`[一-鿿]`）全篇扫过，**三篇共 229 行里 0 行含非 ASCII 字符**——`碌` / `渭` / `卤` / `鈥慴` 那一族在本页**不存在**。**所以本页的引文可以照字面直接拿去 raw 里搜。**（**图上的字不在此列**——它们本来就不在 raw 文本里，见「出处」。）

`verified: doc-only`
