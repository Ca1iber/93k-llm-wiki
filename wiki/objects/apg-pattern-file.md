---
type: object
title: APG pattern file
layer: file
stage: pattern
tags: [mtp, apg, mtl, file-format, pattern-compile]
related: [apg-program-file, device-access-file, device-architecture-file, pin-mapping-file, timing-file, waveform-mapping, pattern]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# APG pattern file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,722 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.md>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### APG pattern file syntax（整篇，取自子主题）

# APG pattern file syntax

The syntax of the APG pattern file, in general, follows the conventions of the `MTL compiler syntax`（raw: `02.12.03.02.02_MTL_compiler_syntax.md`）.

Specifically, an APG pattern file looks like this:

```
:apgPattern:
{
[ :version:            <patternVersion>]
[ :defines:
    {
        :format:
        { :name:         :value:        }
        { <macroName><macroValue>   }
...
    } ]
[ :options: <cmdLineOption> ]
    :deviceAccess:       <deviceAccessFile>
    :apgProgram:         <programFileFile>
    :deviceArchitecture: <architectureFile>
[ :dcTest:             <DC_eventFile>:<dcSetName>]
    :pinMap:             <pinMapPath>
    :waveformMap:        <waveformMapFile>|<timingFile>:<wavetableName>
[ :pinConfig:          <pinConfigFile>]
[ :modeContext:        <modeContextName>]
    :nullData:           <nullDataValue>
[ :scramble:           <addressScramblingTableName>]
[ :bitInversion:       <bitInversionTableName>]
[ :bitOrdering:        <bitOrderingTableName>]
[ :crc:                <crcSetting>]
[ :dbi:                <dbiSetting>]
[ :maintenanceOperation: <maintenanceOperationName>]
[ :countedMatchPad:    <matchLoopPaddingName>]
[ :timing:
    {
        :file:           <timingFile>
        :eqns:           <equationSet>
        :tims:           <timingSet>
        :spec:           <specSet>
    } ]
[ :testLabel:          <testLabelName>[ (<ppinLabelList>) ]]
[ :programParam:
    {
        :format:
        { :name:         :value:        }
        { <paramName><paramValue>   }
...
    } ]
}
```

The order of keywords shown above is typical, but not required; you can rearrange the keywords within a set of curly braces as desired.

Italic text indicates meta-syntax, as described in `Syntax conventions`（raw: `02.12.03.01.02_Syntax_conventions.md`）.

## Keywords and parameters

These are the keywords and their parameters in alphabetical order:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102150.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102150.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions

Each of the optional keywords can have a tilde character (~) as a placeholder in the APG pattern file.

## Program parameter keywords

These keywords let you specify parameters for use in the program and device access files (see :programParameter:, above):


## Timing keywords

These keywords let you specify timing settings (see :timing:, above):

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102150.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions
> 表内引用（2 条，供检索）：`Timing file`（raw: `02.12.03.03.09.02_Timing_file.md`） · `Multiport timing conventions`（raw: `02.12.03.04.14.01_Multiport_timing_conventions.md`）

### Example

```
:apgPattern:
{
   :apgProgram:            "refresh_routines.prog"
   :deviceAccess:          "../../device_defs/access_defs/ddr3_64Mx8_x4.dvac"
   :deviceArchitecture:    "../../device_defs/arch_defs/ddr3_64Mx8.dvar"

   :pinMap:                "../../device_defs/pin_maps/ddr3_64Mx8.pmap"
   :waveformMap:           "../../device_defs/waveform_maps/ddr3_x4.wmap:PreDefined"

   :nullData:              0
   :scramble:              ""
   :dataScramble:          ""
   :bitInversion:          ""
   :bitOrdering:           ""

   :maintenanceOperation: "allcore_refresh"

   :programParam:
   {
      :format:
      { :name:         :value: }

# tCK based Device timing parameters
# - based on 1066: tCK period 1.875ns.
# - based on 64Mx8 = 512Mb --> tRFC=90ns

      { tRFC      48 }

   }
}
```

<!-- 语法节 end -->

## 是什么

**APG pattern file 是 MTL 编译器的「主文件」（master file）。** 原文第一句就是全部定义：

> 「The APG pattern file is the "master" file for the compiler. It contains the locations of all the
> other files needed as well as (optionally) program parameters and the mode context.」

**扩展名 `.apg`**（`The pattern file has the .apg file name extension.`）。
**它自己不含测试代码——它是一张「去哪儿找文件」的清单。**

### 它指向什么

**这张表是本页的骨架。** 前五项在语法骨架里**没有加 `[ ]`**（那是「可选」的标记），
后几项加了——**所以必需/可选是照语法骨架读出来的**：

| 指向的东西 | 关键字 | 必需性 |
|---|---|---|
| APG program file | `:apgProgram:` | **必需** |
| Device access file | `:deviceAccess:` | **必需** |
| Device architecture file | `:deviceArchitecture:` | **必需** |
| Pin mapping file | `:pinMap:` | **必需** |
| Waveform mapping 信息 | `:waveformMap:` | **必需** |
| DC event file | `:dcTest:` | 可选，原文：`required only if DC events are to be used` |
| memory device maintenance operation | `:maintenanceOperation:` | 可选 |
| match loop padding setup | `:countedMatchPad:` | 可选 |
| scrambling / null data / CRC / bus inversion 等设置 | `:scramble:` `:nullData:` `:crc:` `:dbi:` 等 | 可选 |
| APG 程序代码里用的 program parameters | `:programParam:` | 可选 |

原文的措辞是「The names and locations of the files **and other information required for compiling
the test pattern**」——**`.apg` 是「谁引用谁」那张图的顶点。**
原文配了一张图（`102175.png`），图注为
`Miniature scheme of file dependencies with .apg file highlighted`——
**这张图本页 2026-09-20 看了**，见下「那张文件依赖小图（④ 图证）」。

### 关键机制：`:waveformMap:` 有两种指法（**最容易读漏的一条**）

原文只用一行把它说完：

> 「Waveform mapping information (`:waveformMap:`), referencing **either** a timing file **or** a
> waveform mapping file which references a timing file in turn」

「语法 / 参数」节（**取自子主题**）把两条路各自说清了：

| 走法 | 填什么 | 原文用词 |
|---|---|---|
| **直接**波形映射 | `<timingFile>:<wavetableName>`（**冒号连接**） | `Direct waveform mapping` |
| **间接**波形映射 | `<waveformMapFile>` | `Indirect waveform mapping` |

**换句话说：同一个关键字，参数里有没有那个冒号，决定走哪条路。**
两条路各自有一篇专文（`Setting_up_direct_waveform_mapping` /
`Setting_up_indirect_waveform_mapping`），**本页都没读**。

### 语法：它跟 MTL 编译器语法走

「语法 / 参数」节里（**放在段名里的来源是子主题 `02.12.03.03.02.01_APG_pattern_file_syntax.md`**）第一句：

> 「The syntax of the APG pattern file, in general, follows the conventions of the `MTL compiler syntax`.」

两条与「怎么写这个文件」直接相关的规则：

- **关键字的先后顺序不是强制的**：
  > 「The order of keywords shown above is typical, but not required; you can rearrange the keywords
  > within a set of curly braces as desired.」
- **可选关键字可以填 `~` 占位**：
  > 「Each of the optional keywords can have a tilde character (~) as a placeholder in the APG pattern file.」

### `:options:` 会覆盖命令行（**反直觉的一条**）

`:options:` 里写的编译选项**压过另外两处**，原文：

> 「If you specify options in the APG pattern file using the :options: keyword, they **override** any
> options that are specified for the compilation of the file using the apgc command as well as any
> option-equivalent settings in the compiler control dialog. That is, if options in two locations
> conflict, the one specified in :options: is used.」

**唯一的例外是 `-D`**：`You can use any command line option except -D.`
——`-D` 归 `:defines:` 管，那张表的值
「can be overwritten from the command line using the -D option of the apgc command or the
`Overwrite an Existing MTL Define` option in the MTL compiler control dialog」。

### 两个关键字已经被判「不该再用」

语法节里这两条**用的是同一句模板**：

| 关键字 | 原话 | 原文让换成什么 |
|---|---|---|
| `:modeContext:` | `This keyword should no longer be used; it is supported only for backwards compatibility.` | Pin mapping file 里的 **`using modecontext`** 语句 |
| `:pinConfig:` | `This keyword should no longer be used; it is supported only for backwards compatibility.` | Pin mapping file 里的 **`using pinconfig`** 语句 |

> **⚠️ 正文和关键字表在这里打架**：正文第一句说 `.apg` 里包含
> 「(optionally) program parameters **and the mode context**」——**把 `:modeContext:` 当正常内容介绍**；
> 而关键字表说它已弃用、只是向后兼容。**两处原文都抄在上面，本页不替它们调和。**

### 那张文件依赖小图（**④ 图证，2026-09-20 补**）

`102175.png`（251×151）。**图上没有图例**，raw 里也没有一句解释它，
所以能读的只有两层：**框上的字**、**哪个框跟哪个框连着**。
**框里的字画在像素里，raw 里 grep 不到**——要核只能自己开
`F:\master-dev\dorm-wsl-sytest\tdc-html\raw\102175.png`。

- **9 个框摆成 3×3**，框里写的是文件扩展名：
  上排 `.tim` / `.dvar` / `.dac`，中排 `.wmap` / `.apg` / `.prog`，下排 `.pin` / `.pmap` / `.dcev`。
  **本图把 `.apg` 那个框涂成橙色**（「高亮」）。
  **同一张图在那族的 9 篇文档里各出现一次、每次换一个框高亮**
  （`.prog` 那篇是 `102176.png`、`.dac` 那篇是 `102312.png`——**这两张本页也开了**，
  框的位置与框里的字完全一样）。
- **`.apg` 那个框的边上数得出 8 处线头**（按像素逐边数的，含并排的两条）：
  上面 3（左上斜、正上、右上斜）、**右面 2（并排两条横线）**、下面 2（正下、右下斜）、左面 1。
  **9 个框里，除它自己以外，它只没连 `.pin`**（`.pin` 全图只有一处线头，接在它右边）。
- **它连到的 7 个框，与本页「和谁有关」列的下游一一对得上**：
  `.prog`（`:apgProgram:`）/ `.dac`（`:deviceAccess:`）/ `.dvar`（`:deviceArchitecture:`）/
  `.pmap`（`:pinMap:`）/ `.tim` 与 `.wmap`（波形映射那两支）**正是本页列出来的六个**；
  多出来的一个是 **`.dcev`（DC event file）**——**它也对得上语法骨架里那条可选的
  `[ :dcTest: <DC_eventFile>:<dcSetName>]`**（推断：两者指同一个文件类型）。

**图没答掉的**：**线型（实线 / 点线）与箭头方向的含义**——**图里没有图例**，
那几篇文档里 grep `dotted line` / `solid line` 是 **0 命中**，**本页不猜**；
**哪条线对应哪个关键字，图上没有任何标注**。
**所以这张图能证的只有一件事**：**这 9 个文件类型是一族，而 `.apg` 在这一族里连得最广**
——这与原文管它叫 `the "master" file` 是一路的（推断）。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` 段**——它是一篇格式说明，不是操作步骤。
从原文能读出来的用法只有两条：

1. **写一个 `.apg`**：照「语法 / 参数」节的骨架填。
   `:apgPattern:` 必须打头（`This keyword is required at the start of the file.`），
   必需关键字给路径，可选的按需给、不要的填 `~`。
2. **编译**：用 `apgc` 命令，或用 MTL compiler control dialog。
   **具体怎么调，原文只留了两个指针**（`apgc command syntax` 与
   `MTL compiler control dialog`），**两篇本页都没读**。

**两条路径规则**：

- **相对路径的基准是「当前目录」**——`:apgProgram:` / `:deviceAccess:` /
  `:deviceArchitecture:` 的说明里都写着 `The path (relative to the active directory)`。
- **`:defines:` 里的宏在别的 MTL 配置文件里也能用，但 SmarTest 配置文件里不行**——
  原文：`Text macros that can be used in the APG pattern file and other MTL configuration files
  (but not SmarTest configuration files).` **这条边界值得记**。

**一个易错点**：`testLabel` 的列表写法。原文给了两个等价写法作例：

- `:testLabel: myLabel(initial,*,PPS(refresh),PARA(active1,active2))`
- `:testLabel: myLabel(initial,*,refresh,PARA(active1),PARA(active2))`

原文紧接着说 **`*` = 当前正在编译的那个 pattern**（`The current pattern`）。

## 和谁有关

- [[apg-program-file]] — **下游**，由 `:apgProgram:` 指到。**测试代码在那一篇**
- [[device-access-file]] — **下游**，由 `:deviceAccess:` 指到
- [[device-architecture-file]] — **下游**，由 `:deviceArchitecture:` 指到；
  **本页好几个关键字填的是它里面定义的表名**（见下）
- [[pin-mapping-file]] — **下游**，由 `:pinMap:` 指到；
  **同时是 `:modeContext:` / `:pinConfig:` 两个弃用关键字的目的地**
- [[timing-file]] — **下游**，直接波形映射那一支
- [[waveform-mapping]] — **下游**，间接波形映射那一支
- **「填的是表名，不是表」的一组关系**：`:scramble:` / `:bitInversion:` / `:bitOrdering:` /
  `:crc:` / `:dbi:` 的参数都是**名字**，原文一律写
  `as it is specified in the Device architecture file`——
  **表本身住在 [[device-architecture-file]] 里**
- `MTL Configuration Files`（**未建**）— 原文 `## Related information` 只指向这一篇，
  **它是这一族文件的共同父页**；**本页没读它**，所以 `.apg` 在整个家族里的位置本页只有原文那一句
- [[pattern]] / [[pattern-master-file]] — **同名不同物，别混淆**：
  本页的 `.apg` 是 **MTP 的** MTL 编译器主文件；93K 侧的 pattern master file 是另一套东西
  （**本页没读那篇，不断言两者关系**）（推断）

## 版本

原文 `## Functional changes` 一共三条：

- **`Introduced before SmarTest 6.3.2`**
- **MTP 2.6.6**：`:countedMatchPadding:` keyword added
- **MTP 3.0.3**：（MTP on SOC 103.0.0）`:countedMatchPadding:` keyword changed to `:countedMatchPad:`

**三点必读：**

1. **第一条是 §11.2② 说的哨兵值**，不是「6.3.2 新增了这个文件」。
   照字面读会生成一条「6.3.2 引入了 `.apg`」的假信息。
2. **三条里只有第一条属 SmarTest，后两条是 MTP 产品线**——
   §11.2④（同一段里混产品线）在本篇就有实例。
3. **「added 又 changed」这一对说明**：`:countedMatchPad:` 这个**短拼法是 MTP 3.0.3 才定下来的**，
   在那之前叫 `:countedMatchPadding:`。**正文用的是短的**。
   **本篇没有一条 SmarTest 7.x 的条目。**

## 出处

`sources:` 一篇：
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.md`
（`68403.htm`，3,197 字节，80 行）——**整篇读完**。

**本页做了什么、没做什么**：

- **「语法 / 参数」节不是从 `sources:` 那篇抽的。** 那篇自己**没有完整语法段**，
  脚本改从子主题 `02.12.03.03.02.01_APG_pattern_file_syntax.md` 抄了 **14,186 字符**（骨架在段名里写明了）。
  **那一篇本页没有读原文**——本节凡引语法节内容，依据是**页内那段逐字拷贝**，不是我对那个 raw 文件的阅读。
  **我读的是另外那一篇 top-level 文档**。
- **被 `.apg` 直接指向的六篇，一篇都没读**：`APG pattern file syntax`（只读了脚本抄进来的那段）、
  `Preprocessor statements`、`Device architecture file`、`Pin mapping file`、
  `Waveform mapping` 相关各篇、`Memory device maintenance operation`。
  **所以「每一项该怎么填」本页只有骨架里那些。**
- **那张图看了（2026-09-20 补）**——**上一版这里写的是「一张图都没看」，
  并由此写下「本页没有任何来自图的结论」；那句话现在是错的，按实际改动如下**：
  `102175.png`（`.apg` 高亮的文件依赖小图）——**9 个框、`.apg` 边上有 8 处线头、连到 7 个框**，
  见上文「那张文件依赖小图（④ 图证）」。**本页另外还开了同族的 `102176.png`（`.prog` 高亮）
  与 `102312.png`（`.dac` 高亮）**，对框的位置与框里的字。
  **图上那些字在 raw 里 grep 不到**，要核只能自己开
  `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\102175.png`。
- **图没答掉的**：**线型与箭头的含义**、**哪个关键字对应哪条线**
  （图里没有图例，raw 里也没有一句说明）。
- **`apgc command syntax` 和 MTL compiler control dialog 两篇没读**——
  **「怎么把 `.apg` 编译出来」本页只有名字，没有一条命令。**
- **`## Example` 那段代码本页没有逐行讲解**；**它和语法子主题里的示例是同一段**（见下 ⚠️⑤）。
- **`MTL Configuration Files`（`## Related information` 唯一指向的那篇）没读。**
- **`MTL compiler syntax`（`Syntax conventions` 两篇）没读**——
  所以 `Italic text indicates meta-syntax` 具体是什么排版约定，本页不知道。

> ⚠️ **本篇的语料瑕疵，照实记、一处没替它改**：
> ① **正文写 `:programParams:`（复数），其余全篇写 `:programParam:`（单数）**。原文：
>    `Optionally, specifications of program parameters used in the APG program code (:programParams:).`
>    而语法骨架和示例里都是 `:programParam:`。**同一篇文档里两种拼法。**
> ② **示例里有一个关键字在关键字表里查不到**：示例写 `:dataScramble: ""`，
>    而语法骨架的关键字清单与「Keywords and parameters」表**都没有 `:dataScramble:`**。
>    **它是不是有效关键字，本篇回答不了。**
> ③ **示例和「怎么关掉」的说明不一致**：`:scramble:` 的说明是
>    `If you do not want to use address scrambling, enter a tilde (~).`，
>    而示例里 `:scramble:` 填的是 `""`（空串）**不是 `~`**；`:bitInversion:` / `:bitOrdering:` 同样填 `""`。
> ④ **正文与关键字表对 `:modeContext:` 的判断相反**（见上「两个关键字已经被判不该再用」）。
> ⑤ **示例在本篇和语法子主题里各出现一次、逐字相同**（骨架「语法 / 参数」节里两段都在）。
>    这是语料结构如此，不是页面重复抄写。
> ⑥ 正文把 `:apgProgram:` 指的文件叫 `programFileFile`（语法骨架里 `<programFileFile>`）——
>    **`File` 写了两遍**。原文如此。

`verified: doc-only`
