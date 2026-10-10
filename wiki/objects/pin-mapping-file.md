---
type: object
title: Pin mapping file
layer: file
stage: pattern
tags: [pin-mapping-file, pmap, mtl, memory-test, pin-configuration, pin-group, pattern-compilation, apg]
related: [pin-configuration-file, device-access-file, apg-pattern-file, pattern, pin, mtp-memory-test, vector-setup-file, pattern-master-file]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06_Pin_mapping_file.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Pin mapping file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,433 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06_Pin_mapping_file.md>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.01_Pin_mapping_file_syntax.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Pin mapping file syntax（整篇，取自子主题）

# Pin mapping file syntax

The syntax of the pin mapping file is similar to that of the `Pin configuration file`（raw: `02.12.03.03.09.01_Pin_configuration_file.md`）, although not identical to it.

Specifically, a pin mapping file looks like this:

```
# declarations
[using pinconfig <pinConfigFile>]
[using port <portName>]
using defaultxmode <defaultXmode>
[using modecontext <modeContext>]
[using interruptCtrl <refreshMode>]
[using protocol "<name>" @(specification = "<hwprtocolID>", revision = "<rev_str>", type = "<stype_str>", port = "<port name>")]
# individual pins
[<mtlPinName>[(<refPinName>)]=<smartestPinName>[@(<pinAtt>=<attValue>;...)]]
[<mtlPinName>(<refPinName>)=<smartestPinName>@(bitseq=copy)]
...
# pin groups
[<mtlPingroupName>=<smartestPingroupName>[@(<pinAtt>=<attValue>;...)]]
[<mtlPingroupName>.<nnn>=<smartestPinName>[@(<pinAtt>=<attValue>;...)]]
...
# buses
[configure bus <busName> (<pinList>)]
...

```

Note While each individual pin or pin group mapping statement is optional, the pin mapping file must map all pins that you want to use, either as individual pins or as members of pin groups.

The order of configuration statements shown above is typical, but not required; you can rearrange the statements as desired. The comments shown are entirely optional and included here only to clarify the file's structure; you can omit them as desired.

Italic text indicates meta-syntax, as described in `Syntax conventions`（raw: `02.12.03.01.02_Syntax_conventions.md`）.

## Keywords and parameters

These are the keywords and their parameters in alphabetical order:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102516.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions
> 表内引用（8 条，供检索）：`x-mode`（raw: `02.12.03.04.02_Transparent_x-modes.md`） · `Device access file`（raw: `02.12.03.03.04_Device_access_file.md`） · `Automatic waveform generation`（raw: `02.12.03.04.03.03_Automatic_waveform_generation.md`） · `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） · `Pin configuration file`（raw: `02.12.03.03.09.01_Pin_configuration_file.md`） · `multiport operations`（raw: `02.12.03.04.14_Multiport_operation.md`） · `Reference pins`（raw: `02.12.03.03.06.03_Reference_pins.md`） · `Buses`（raw: `02.12.03.03.06.02_Buses.md`）

Pin attributes
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102516.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：Attribute | Description
> 表内引用（2 条，供检索）：`Copying vectors`（raw: `02.12.03.03.06.04_Copying_vectors.md`） · `Starting the MTL compiler from the command line`（raw: `02.12.03.02.05_Using_the_MTL_compiler_from_the_command_line.md`）

### Example

```
DM.000=DM
DM=DM_Bus

DQi.007=DQ_i.07
DQi.006=DQ_i.06
DQi.005=DQ_i.05
DQi.004=DQ_i.04
DQi.003=DQ_i.03
DQi.002=DQ_i.02
DQi.001=DQ_i.01
DQi.000=DQ_i.00
DQi=DQi_Bus

DQo.007=DQ_o.07
DQo.006=DQ_o.06
DQo.005=DQ_o.05
DQo.004=DQ_o.04
DQo.003=DQ_o.03
DQo.002=DQ_o.02
DQo.001=DQ_o.01
DQo.000=DQ_o.00
DQo=DQ_Bus

DQSi.001=DQS_i
DQSi.000=DQSn_i
DQSi=DQSi_DiffBus

DQSo.001=DQS_o
DQSo.000=DQSn_o
DQSo=DQS_DiffBus

Bank.002=BA.2
Bank.001=BA.1
Bank.000=BA.0
Bank=Bank_Addr_Bus

Address.012=A.12
Address.011=A.11
Address.010=A.10
Address.009=A.09
Address.008=A.08
Address.007=A.07
Address.006=A.06
Address.005=A.05
Address.004=A.04
Address.003=A.03
Address.002=A.02
Address.001=A.01
Address.000=A.00
Address=Address_Bus

CK=CK
CKn=CKn
CKE=CKE
CSn=CSn
RASn=RASn
CASn=CASn
WEn=WEn

RESETn=RESETn
ODT=ODT
```

<!-- 语法节 end -->

## 是什么

**一句话：`.pmap` 文件是「MTL 侧引脚名」到「SmarTest 侧引脚名」的对照表。** 原文：

> 「The pin mapping file maps pin definitions from the Device access file to pin or pin group specifications from the SmarTest Pin configuration file.」

**但真正决定它分量的是紧接的第二句——它是白名单，不是补充说明**：

> 「The MTL compiler creates test patterns only for SmarTest pins for which APG pin names have been specified in the pin mapping file.」

**同一篇里还有第三句，句式一样**（在「你能指定什么」那节里）：

> 「Per-pin subroutines are generated only for pins which are listed in the pin mapping file.」

**两句都带 `only`，而且是同一件事的两个后果**：**没写进这张文件的引脚，既没有 test pattern，也没有 per-pin subroutine。**
**原文没说漏掉时会不会报错**——**「漏写 = 静默少东西」这个后果是本页从两个 `only` 读出来的，文档没有把它写成警告。**

### 它的两个身份标记

- **扩展名**：原文「The pin mapping file has the .pmap file name extension.」
- **谁引用它**：原文「It is referenced from the APG pattern file with the `:pinMap:` keyword.」——
  **引用方向是「pattern 文件指过来」，不是「它指过去」。**

### 它在文件依赖图里的位置

原文在这两句之间插了一张图（skeleton 里留着那一行）：

```
  ![Miniature scheme of file dependencies with .pmap file highlighted](../../../../raw/102511.png)
```

**本页没有打开这张图**（原图文件名 `102511.png`）。**所以本页对依赖关系的全部认识来自那两句散文：
`Device access file`（引脚定义）引到本文件，本文件再引到 SmarTest `Pin configuration file`（引脚/引脚组规格）。**
**图里画了什么别的东西，本页不知道。**

### 你能在这张文件里指定三样东西

原文：

> 「You can specify in the pin mapping file:」

1. **「APG pin definition assignments for each DUT pin to be tested.」**（配合上面那句 `only` 一起读）
2. **「Transparent x-modes definitions, both global and pin-specific.」**
3. **「The mode context for the Automatic waveform generation.」**

**第三样带一个条件句**：

> 「The mode context is needed only if you are using automatic waveform generation or generating a test label and no mode context is defined in the wavetable.」

**（这句话有歧义，见「出处」⑦。）**

### 它长什么样

**本页「语法 / 参数」节里第一段（`Pin mapping file syntax`，**取自子主题**）给了完整骨架**，分成四段：

| 段 | 语句形状（照抄骨架） | 管什么 |
|---|---|---|
| `# declarations` | `[using pinconfig <pinConfigFile>]` / `[using port <portName>]` / `using defaultxmode <defaultXmode>` / `[using modecontext <modeContext>]` / `[using interruptCtrl <refreshMode>]` / `[using protocol "<name>" @(...)]` | **文件级设置**（方括号是骨架里的可选项标记） |
| `# individual pins` | `[<mtlPinName>[(<refPinName>)]=<smartestPinName>[@(<pinAtt>=<attValue>;...)]` | **单个引脚的映射** |
| `# pin groups` | `[<mtlPingroupName>=<smartestPingroupName>[@(...)]]` / `[<mtlPingroupName>.<nnn>=<smartestPinName>[@(...)]]` | **引脚组的映射**（整组映，或按 `.nnn` 逐位映） |
| `# buses` | `[configure bus <busName> (<pinList>)]` | **总线** |

**三句关于这份骨架的原文话，值得逐字读**：

> 「The syntax of the pin mapping file is similar to that of the Pin configuration file, although not identical to it.」

> 「Note While each individual pin or pin group mapping statement is optional, the pin mapping file must map all pins that you want to use, either as individual pins or as members of pin groups.」

> 「The order of configuration statements shown above is typical, but not required; you can rearrange the statements as desired. The comments shown are entirely optional and included here only to clarify the file's structure; you can omit them as desired.」

**第一句是本页最需要读者警惕的一句**：原文说「像 pin configuration file，但不完全一样」，
**然后全篇没有说差在哪儿**。**所以「能不能照抄 pin configuration file 的写法」这个问题，
本页的语料答不了**（那篇也没读）。

**第二句解释了为什么骨架里每一行都套着方括号**：**每条映射语句本身可选，但「要用的引脚必须都映射到」是硬要求。**

### 8 个引脚属性

**属性写在 `@(...)` 里，用分号分隔**（骨架：`@(<pinAtt>=<attValue>;...)`）。**「语法 / 参数」节里有完整定义，照抄成表**：

| 属性 | 值 | 原文说什么 |
|---|---|---|
| `bitseq` | **只能是 `copy`** | 「This attribute always has the value of `copy`.」——**作用是让编译器把参考引脚的编译结果拷过来，省编译时间** |
| `cycleratio` | `1:1` / `1:2` / `1:4` | 「The ratio of the specified pin's base rate to the standard base rate.」**不给就是 `1:1`** |
| `exps` | **60 到 1,000,000** | 「The expansion size for the pin.」——「Larger expansion sizes decrease the risk of Data Queue Empty errors at the expense of requiring more vector memory.」**设了就覆盖编译器的 `-e` 开关** |
| `interruptCtrl` | `VEC` / `VECTOR` | **不给就用 `using interruptCtrl` 语句的值；连语句也没有，缺省是 `VEC`** |
| `type` | `dcscale` / `digital` | 「If no pin type is specified, the type is assumed to be `digital`.」 |
| `xmode` | x-mode 编号 | **设了就同时覆盖 `using defaultxmode` 语句和 device access file 里的 `:xModeDefinition:`** |
| `system` | `true` / `false` | 「When `system = true`, SmarTest will generate corresponding programs for those pins (system generated). No vector data will be generated for those pins by MTP.」**缺省 `false`** |
| `optional` | `true` / `false` | 「When `optional = true`, even these pins are missed in the pin configuration file, SmarTest will skip these pins and run the relative patterns without warning.」**缺省 `false`** |

**两条关于 cycleratio 的硬规矩，原文写得很硬**：

> 「Pins that are used as reference pins (that is, pins that are specified in parentheses after a pin name, as described in (individual pin), above) must have a pin ratio of 1:1.」

> 「We recommend to always run DC Scale pins at a ratio of 1:4. (This requires setting up a separate port for these pins.)」

**注意第二条是 `We recommend`，第一条是 `must`**——**一个是建议一个是硬约束，原文分得很清，本页照抄不替它拉平。**

### 语法节里的那个例子

**「语法 / 参数」节末尾的 Example 是原文唯一的例子**（DRAM 风格的引脚集：`DM` / `DQi` / `DQo` / `DQSi` / `DQSo` / `Bank` / `Address` / 一批控制脚）。**写法上它只有两种**：

- **逐位映射**：`DQi.007=DQ_i.07` … `DQi.000=DQ_i.00`
- **整组映射到一个 Bus 名**：`DQi=DQi_Bus`、`DM=DM_Bus`、`Address=Address_Bus`

**两种写法在例子里成对出现**，说明「组」既可以逐位展开、也可以整体命名。**但例子里没有的东西也同样重要**：

- **一个 `@(...)` 属性都没有**（`bitseq` / `cycleratio` / `type` … 一个都没出现）
- **一个参考引脚都没有**（`<mtlPinName>(<refPinName>)` 那半截括号形式没出现）
- **一条 `configure bus` 都没有**（用的是 `组名=Bus名` 而不是 `configure bus <busName> (<pinList>)`）

**所以这三样在语料里只有语法定义，没有示例。** 本页不替它们编例子。

## 典型用法

> **原文没有 `## Procedure` 段**，也没有编号步骤。
> **可操作的规则散在定义和关键字说明里**，本节收成七条。**「语法 / 参数」节已经逐字收了骨架、关键字表、
> 属性表和那个例子（10,009 字符），本节不重抄。**

**1. 建文件、起 `.pmap` 名、在 APG pattern file 里用 `:pinMap:` 引用它。** 这三步是文件的存在方式，原文各一句。

**2. 按「要用哪些引脚」写映射。** 骨架四段里，`# declarations` 和 `# buses` 是可选的组织手段，
**真正决定哪些引脚能用的是一行行的 `<mtlPinName>=<smartestPinName>`**——**因为编译只对写进这张文件的引脚出 pattern 和子程序。**

**3. 要让哪一级的参数生效，就用对应的 `using` 语句。** 三条 `using` 语句原文都写了同一句「覆盖」关系：
**`using pinconfig` 覆盖 APG pattern file 的 `:pinConfig:`；`using modecontext` 覆盖 APG pattern file 的 `:modeContext:`；
`using defaultxmode` 覆盖 device access file 的 `:xModeDefinition:`**——**都是「两边都写时，`using` 赢」。**

**4. 要用自动波形生成或生成 test label，就得给 mode context。** 条件句原文见上（**注意那个条件句有歧义**）。

**5. 要用 multiport，`using port` 和 `using pinconfig` 必须一起出现，而且多个 port 不能重叠。** 原文：

> 「This keyword is optional, which is only required in multiport operations. When using "using port", you must specify the pin configuration file (see above).」
> 「You can specify multiple "using port<portName>" in your pin mapping file. However, those specified ports must not overlap with each other.」

**这一条后半段是一脚很深的陷阱，原文自己写出来了**（取自子主题 `Pin mapping file syntax`）：

> 「When the "using port" statement is configured in the pin mapping file, the pins which have been defined in the file but do not belong to any ports will not be compiled with vectors. During the compilation, no warnings or error messages will be issued, but error messages may show up in the Error Log view when the vector files are bing loaded in SmarTest.」

**「不报错、但东西少了、错要到 SmarTest 载入 vector 时才冒出来」**——
**这是本页看到的最容易吃暗亏的一条**（那句里的 `bing` 是原文的错字，见「出处」③）。

**6. DC Scale 引脚建议 `cycleratio=1:4` 并配单独 port；被当参考引脚的必须 `1:1`。** 两条原文见上（一推荐一强制）。

**7. 别再用 `using defaultxmode`。** 原文那条参数说明的最后一句是：

> 「This parameter was supported in earlier versions of MTL and should no longer be used.」

**这句话和本页开头「你能指定三样东西」里的第二样（Transparent x-modes）是矛盾的口气**——
**一边把它列为「你能指定的东西」，一边说「不该再用了」。两处都照抄，本页不判哪边是当前口径。**

## 和谁有关

- [[device-access-file]] — **本文件左侧的源头**：映射的左边（`<mtlPinName>` / `<mtlPingroupName>`）
  「as it is to be used in the Device access file」
- [[pin-configuration-file]] — **本文件右侧的目标**：映射的右边（`<smartestPinName>` /
  `<smartestPingroupName>`）是它里面的引脚或引脚组。
  **原文还说两边的语法「similar … although not identical」**——**差在哪儿没写，本页没有那篇**
- [[apg-pattern-file]] — **唯一一个引用本文件的文件**，用 `:pinMap:` 关键字；
  `using pinconfig` / `using modecontext` 覆盖的就是它里面的两个参数
- [[pin]] / [[pin-configuration-file]] — 引脚本身。**本页只管名字的对应，不管引脚怎么配**
- [[pattern]] / [[pattern-master-file]] / [[vector-setup-file]] — **同属 `stage: pattern` 的文件族**
  （**本页没读它们，不主张具体关系**）
- [[apg-program-file]] — `APG` 另一侧的文件（**未读**）。
  **注意「APG」这个词本页源文档从头用到尾（`APG pin names` / `APG pattern file`），
  但全篇没有展开过一次**
- [[mtp-memory-test]] / [[mtpt]] — **本页源文档在 `Memory Test Plus` 目录下，
  例子是一套 DRAM 引脚**，所以它的语境是存储器测试
- [[dc-scale-uhc4t-card]] / [[dc-scale-xps256-card]] — **`cycleratio` / `type=dcscale` 指向的 DC Scale 那一侧**
  （**未读，不主张关系**）
- `MTL Configuration Files` / `Pin mapping file syntax` / `Buses` / `Reference pins` / `Copying vectors` —
  **本篇的四个子主题和它的父页**，**本页一篇都没读**；
  **其中 `Pin mapping file syntax` 的内容被脚本抽进了本页「语法 / 参数」节**，
  本页引它时逐处标了「取自子主题」
- 原文里其余链接目标，**全部没读**：`Transparent x-modes`、`Automatic waveform generation`、
  `Multiport operation`、`Syntax conventions`、`Starting the MTL compiler from the command line`

## 版本

原文有 `## Functional changes` 段，**只有一条**：

- **Introduced before SmarTest 6.3.2**

> **这一条是哨兵值，不是「6.3.2 新增的」。**
> 它写的是 `before`——意思是「**在本文档集覆盖范围开始之前就已经有了**」（schema §11.2 ②）。
> **照字面读会凭空造出一条「SmarTest 6.3.2 新增了 pin mapping file」的假信息，而且格式齐整。**

**同一篇里还存在两个产品线的版本号**（§11.2 ④）：**源路径上的目录是
`02.12_Memory_Test_Plus_7.10.2`（MTP 7.10.2），而 `## Functional changes` 说的是
`SmarTest 6.3.2`。** 两者不是一个产品线，**本页并列记下，不替它们对齐。**

**原文没有给任何后续变更条目**——**所以「这份文件的语法在 6.3.2 之后改过没有」本页没有依据。**

**唯一一条真正的「版本相关」信息不在这一节里**，而藏在关键字表的 `using defaultxmode` 那格：

> 「This parameter was supported in earlier versions of MTL and should no longer be used.」

**换句话说：这篇文档的「什么过时了」写在参数说明里，不写在 `## Functional changes` 里。**
**只读版本节的人会漏掉它。**

## 出处

`sources:` 一篇：

`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06_Pin_mapping_file.md`
（TDC `67574.htm`，共 104 行）

**本页没做的**：

1. **只读了这一篇（105 行）。**
2. **四个子主题一篇都没读**：`Pin mapping file syntax`、`Buses`、`Reference pins`、`Copying vectors`。
   **其中 `Pin mapping file syntax` 的全文被脚本抽进了本页「语法 / 参数」节**
   （节头的 `（整篇，取自子主题）` 就是标注）。**本页引用它的每一处都写明了来源，
   但没有读那篇文档本身**——**所以本页的「参考引脚」「Bus」「拷贝 vector」三块只有骨架里那几行，
   没有展开。**
3. **那张依赖图没有打开**（`102511.png`）。**本页关于文件依赖关系的全部内容来自散文，不是图。**
4. **没有实测**：本页没有写过 `.pmap` 文件，没有跑过 MTL 编译器，
   没有验证过 `cycleratio` / `exps` / `bitseq` 的实际效果，**也没有验证过「漏写引脚会怎样」**。
   **本页所有结论都是文档事实（`verified: doc-only`）。**
5. **例子之外一个例子都没补**：例子里没有 `@(...)` 属性、没有参考引脚、没有 `configure bus`，
   **本页就没有写这三样的用法示例**——**编一个出来就是造假（§11）。**

> ⚠️ **本篇的语料瑕疵，照实记，一处都没替它改**：
>
> ① **`## Related information` 里两个链接之间没有任何分隔符**：
> `[MTL Configuration Files](<02.12.03.03_MTL_Configuration_Files.md>)[Reference pins](<02.12.03.03.06.03_Reference_pins.md>)`
> ——**两个中括号直接贴在一起，没有空格、没有逗号、没有换行。渲染出来会是
> 「MTL Configuration FilesReference pins」连成一个词。本页照抄，不替它加分隔。**
> ② **`Introduced before SmarTest 6.3.2` 是哨兵值**，见上面「版本」节的说明（§11.2 ②）。
> ③ **「语法 / 参数」节里（**取自子主题**）的三处**：
>   - `when the vector files are bing loaded in SmarTest` —— **`bing` 应为 `being`**。
>   - `(If that statement is not present, the default is VEC.` —— **右括号没闭合**。
>   - **整张 `Keywords and parameters` 表和整张 `Pin attributes` 表被压成了「一个单元格一行」的形态**
>     （每格之间只有一行孤立的 ` |`）。**这一节 10,009 字符里绝大部分是这个。**
>     **不是本页排错，是抽取时表格结构丢了——本页照实说明，不去修（手改会在下次
>     `--refresh-syntax` 时消失）。**
> ④ **关键字表按字母序排，属性表不按**：原文只对关键字表声明了
> 「These are the keywords and their parameters in alphabetical order」；
> **属性表的顺序是 `bitseq` / `cycleratio` / `exps` / `interruptCtrl` / `type` / `xmode` / `system` / `optional`**
> ——**`system` 和 `optional` 挂在 `xmode` 后面。本页照实记，不重排。**
> ⑤ **`using protocol` 只有一句话**：「Currently no cards use protocol-aware transaction.」
> ——**它出现在语法骨架里（`using protocol "<name>" @(specification = …, revision = …, type = …, port = …)`），
> 出现在关键字表里，但「这个关键字到底做什么」一个字都没有。**
> ⑥ **「similar … although not identical」，但差在哪儿全篇没说**：
> `The syntax of the pin mapping file is similar to that of the Pin configuration file, although not identical to it.`
> ——**被比较的那篇（`Pin configuration file`）本页没读，所以这处差别在本页里是空的。**
> ⑦ **mode context 那句的条件有歧义**：
> `The mode context is needed only if you are using automatic waveform generation or generating a test label and no mode context is defined in the wavetable.`
> ——**`and no mode context is defined in the wavetable` 是只接 `or` 的后半句，
> 还是接整个条件？原文没有标点也没有措辞可判。本页不替它断句，两种读法都留。**
> ⑧ **例子与语法骨架的落差**：例子里 `@(...)` 属性、`<refPinName>` 参考引脚、`configure bus`
> **一个都没出现**——**这三样在语料里只有语法定义、没有示例。本页不补。**
> ⑨ **例子里的 `.nnn` 与位序关系只有例子能看出来，没有文字规则**：
> 例子里 `DQi.000=DQ_i.00` … `DQi.007=DQ_i.07`，**后缀看着就是位号**；
> 但原文对 `<nnn>` 只说「A three-digit number specifying an individual pin from a pin group」，
> **没有任何一句说 `.nnn` 与 bit order 的对应关系**
> （**写了位序规则的只有 `configure bus` 那条：「List the pins in their bit order: The most significant bit first and the least significant bit last.」**）。
> **（推断）「后缀 = 位号」是本页从例子里读出来的，不是文档事实。**

`verified: doc-only`
