---
type: object
title: Device access file
layer: file
stage: pattern
tags: [mtp, apg, mtl, file-format, device-access, pattern-compile]
related: [apg-pattern-file, apg-program-file, device-architecture-file, pin-mapping-file, pin-configuration-file, pattern]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04_Device_access_file.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Device access file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **12,889 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04_Device_access_file.md>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.01_Device_access_file_syntax.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Device access file syntax（整篇，取自子主题）

# Device access file syntax

The syntax of the device access file follows the conventions of the `MTL compiler syntax`（raw: `02.12.03.02.02_MTL_compiler_syntax.md`）.

Specifically, a device access file looks like this:

```
:deviceAccess:
{
[ :version:      <deviceAccessVersion>]
    :deviceParam:  {<deviceParamName>...}
    :groups:
    {
        :format:
        { :name:        :size:    }
        { <pinDefName><pinsNum> }
        { ......       }
    }
[ :subGroups:
    {
        :format:
        { :baseGroup:  :context:      :name:          :bits:     }
        { <groupName><contextName><subgroupName><numBits>  }
        { ............        }
    } ]
[ :constants:
    {
        :format:
        {  :name:           :bits:     :value:         }
        {  <constantName><numBits><int-hexValue>  }
        {  .........             }
    } ]
[ :muxModeDefinition:
    {
        :format:
        {  :pin:        :muxMode:  }
        {  <pin-name>   2 | 4     }
        {  ......        }
    } ]
  :apgAccess:
  {
    :name: <accessName>
    :interface: {  <interfaceParam>... }
    :table:
    {
        :format:
        { [ :instruction: ] :pin:    :states:    :data:  :operation:  :comment:  }
        { [<instrExpr>]<pinId>  {<i0><i1>} <data><op><comment>  }
        { [...]...............       }
    }
...
  }
 :countedMatchPad:
  {
    :name: <paddingName>
    :table:
    {
        :format:
        { :subroutine:       [ :port: ]  }
        { <paddingRoutine>[<port>]  }
        { ...[...]  }
    }
...
  }
}
```

Note The :devCyc: and :stateParam: keywords from older versions of MTL were used for specifying non-transparent x-modes. They are still supported but should not be used any more for new programs; support for them may be removed from a future version of MTL. See the `Non-transparent x-modes`（raw: `02.12.03.05.03_Non-transparent_x-modes.md`） appendix for more information.

The order of keywords shown above is typical, but not required; you can rearrange the keywords within a set of curly braces as desired.

Italic text indicates meta-syntax, as described in `Syntax conventions`（raw: `02.12.03.01.02_Syntax_conventions.md`）.

## Keywords and parameters

These are the keywords and their parameters in alphabetical order:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102365.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions
> 表内引用（4 条，供检索）：`APG program`（raw: `02.12.03.03.03_APG_program_file.md`） · `Device architecture file`（raw: `02.12.03.03.05_Device_architecture_file.md`） · `Pin configuration file`（raw: `02.12.03.03.09.01_Pin_configuration_file.md`） · `Pin mapping file syntax`（raw: `02.12.03.03.06.01_Pin_mapping_file_syntax.md`）

## APG access keywords

These keywords let you specify device accesses for use in the program file (see :apgAccess:, above):

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102365.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102365.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions
> 表内引用（4 条，供检索）：`APG program file`（raw: `02.12.03.03.03_APG_program_file.md`） · `macros`（raw: `02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md`） · `control instructions`（raw: `02.12.03.03.04.03_Control_instructions_in_device_accesses.md`） · `Naming rules and conventions`（raw: `02.12.03.02.03_Naming_rules_and_conventions.md`）

The :table: element contains these keywords:

 |

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102365.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。

Keyword

 |

Parameters and descriptions

 |
 |

:comment:

 |

An optional comment explaining the row.

The comment can be any text.

 |
 |

:data:

 |

A value or expression that determines which of the two values in the :state: column (the left or the right one) is sent to the pins.

:data: may contain:

- A fixed hexadecimal or decimal value. Hexadecimal numbers must be prefixed with `0x` to distinguish them from decimal numbers.
- An expression using predefined operators and parameters whose values are set by the APG program code. (For example, `xAddr(rowAddress)`, `data(0,xAddr)`, `data(0,xAddr,yAddr,zAddr)`.)

Each row of the table:

- Takes the value given in the :data: column or, if it is an expression, evaluates it.
- Maps the resulting bit (`0` or `1`) to the states given in the :states: column, a 0 indicating the left state and a 1, the right.

If the :pin: column contains a pin group, the first bit of the expression result is used to determine the state character for the first pin, the second bit for the second pin, and so on. If there are more bits in the result than there are pins in the group, the excess bits are discarded. For illustration, see Pin groups and the :data: column in the Examples section, below.

For an overview of the operators that you can use in the :data: column, see the description of operators for the APG program file in `Operators`（raw: `02.12.03.03.03.01.01_Operators.md`） and the description of data macros in `Macros in device accesses`（raw: `02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md`）.

Note that the :data: column is ignored in device accesses when the :operation: column comprises the crc macro and CRC is enabled.

 |
 |

:instruction:

 |

The :instruction: column can contain optional control instructions that affect the execution of the statements in the other columns.

For an overview of the statements supported in the :instruction: column, see `Control instructions in device accesses`（raw: `02.12.03.03.04.03_Control_instructions_in_device_accesses.md`）.

 |
 |

:operation:

 |

The :operation: column contains specifications of `Cyclic redundancy checks`（raw: `02.12.03.04.09_Cyclic_redundancy_checks.md`） and `dynamic bus inversions`（raw: `02.12.03.04.10_Dynamic_bus_inversion.md`） to apply.

To apply multiple operations, specify them in the desired order and separate them with commas.

This column is optional; if neither cyclic redundancy checks nor dynamic bus inversion is required for an access, it can be omitted.

 |
 |

:pin:

 |

The pins or pin groups involved in the device access.

The pins or pin groups are listed one per row; they must be specified in the `Pin mapping file`（raw: `02.12.03.03.06_Pin_mapping_file.md`）.

 |
 |

:states:

 |

The single state character from the wavetable. In this column, each row must contain two single state characters surrounded by {}. The two state characters are separated with space. For example, `{0 1}`. When the expression in the :data: column is evaluated to 0, the left of the two characters will be transferred to a pin. When the expression is evaluated to 1, the right one will be transferred to a pin.

You can also use the {} characters to reference the interface parameters of this APG access and transfer different state characters to the pins with the same APG access at different call times. Those interface parameters must have the following attributes:

- Data type must be string.
- String to be transferred with a parameter must be one character. For example, "0".
- Independent of any loop variable in this APG access-called program.

For example,

```
:apgAccess:
  {
    :name:  Write
    :interface: {zero one}
    :table:
    {
       :format:
       { :pin:           :states:           :data:     }
       { DQ              {zero one}          0         }
       { ""              {zero one}          1         }
    }
  }
 
main()
{
  Write("0", "1");
  //Be careful, do not code like Write(0, 1), or Write("01"), both of which are wrong.
}
```

 |

## Constants keywords

These keywords let you specify constants for use in device access (see :constants:, in the topmost table above):

 |

Keyword

 |

Parameters and descriptions

 |
 |

:bits:

 |

The width of the constant in bits.

For example, a constant may be 8 bits wide or 64 bits wide.

 |
 |

:name:

 |

The name of the constant.

The name can be any text that follows the `naming conventions`（raw: `02.12.03.02.03_Naming_rules_and_conventions.md`）.

 |
 |

:value:

 |

Specifies the value of the constant.

You can enter hexadecimal or decimal values. Hexadecimal numbers must be prefixed with `0x` to distinguish them from decimal numbers. (For values greater than 64 bits, there are `special considerations`（raw: `02.12.03.04.15_Expressions_with_more_than_64_bits.md`）.)

A constant's value can also be defined as an expression using any of these operators: `+ - * / << >> & | ~`

Comparison operators are not permitted in these expressions.

 |

## Counted match padding keywords

Note Counted match padding is available only in MTP on SOC.

These keywords let you define padding setups that are referenced in the APG pattern file (see :countedMatchPad:, above).

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102365.htm`
> 中**第 5 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions
> 表内引用（1 条，供检索）：`Naming rules and conventions`（raw: `02.12.03.02.03_Naming_rules_and_conventions.md`）

The :table: element contains these keywords:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102365.htm`
> 中**第 6 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions
> 表内引用（2 条，供检索）：`APG program file`（raw: `02.12.03.03.03_APG_program_file.md`） · `pin mapping file`（raw: `02.12.03.03.06.01_Pin_mapping_file_syntax.md`）

## Groups keywords

These keywords let you define groups of pins (see :groups:, in the topmost table above):

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102365.htm`
> 中**第 7 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions
> 表内引用（1 条，供检索）：`Pin mapping file`（raw: `02.12.03.03.06_Pin_mapping_file.md`）

We recommend that you no longer use groups and instead use buses. See `Buses`（raw: `02.12.03.03.06.02_Buses.md`） for more information.

## Subgroup keywords

These keywords let you specify subgroup, that is, subsets of groups that you can address together (see :subGroups:, in the topmost table above):

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/102365.htm`
> 中**第 8 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：Keyword | Parameters and descriptions
> 表内引用（1 条，供检索）：`naming conventions`（raw: `02.12.03.02.03_Naming_rules_and_conventions.md`）

We recommend that you no longer use subgroups and instead use buses. See `Buses`（raw: `02.12.03.03.06.02_Buses.md`） for more information.

## Example

### Pin groups and the :data: column

Lets assume these settings for a device access (with `PinGroup` being a properly defined group of four pins):

```
{ :pin:     :states:  :data: }
{ PinGroup  { 0 1 }   0x5    }
{ ~         { 0 1 }   0x5    }
{ ~         { 0 1 }   0x5    }
{ ~         { 0 1 }   0x5    }
```

The pins of PinGroup are then set like this:

- PinGroup.000 is set to 0.
- PinGroup.001 is set to 1.
- PinGroup.002 is set to 0.
- PinGroup.003 is set to 1.

### Example

```
:deviceAccess:
{
  :version: 1.0
  :deviceParam:
  {  xBits  yBits  dBits  }
  :groups:
  {
    :format:
    {  :name:     :size:  }
    {  x_address  10      }
    {  y_address  8       }
    {  data       16      }
  }

  :apgAccess:
  {
    :name: write_access
    :interface:
    {  xAddr  yAddr  dataw  }
    :table:
    {
      :format:
      {  :pin:      :states:  :data:                     }
      {  CS_        {0 1}     0                          }
      {  OE_        {0 1}     1                          }
      {  WE_        {0 1}     0                          }
      {  BHE_       {0 1}     0                          }
      {  BLE_       {0 1}     0                          }
      {  x_address  (0 1}     xaddr(xAddr,yAddr)         }
      {  y_address  {0 1}     yaddr(xAddr,yAddr)         }
      {  data       {L H}     data(dataw,xAddr,yAddr)    }
    }
  }

  :apgAccess:
  {
    :name:  read_access
    :interface:
    {  xAddr    yAddr    dataw  }
    :table:
    {
      :format:
      {  :pin:      :states:  :data:                     }
      {  CS_        {0 1}     0                          }
      {  OE_        {0 1}     0                          }
      {  WE_        {0 1}     1                          }
      {  BHE_       {0 1}     0                          }
      {  BLE_       {0 1}     0                          }
      {  x_address  {0 1}     xaddr(xAddr,yAddr)         }
      {  y_address  {0 1}     yaddr(xAddr,yAddr)         }
      {  data       {L H}     data(dataw,xAddr,yAddr)    }
    }
  }

  :apgAccess:
  {
    :name: "NMT_Rx6"
    :interface: { ... }
    :table:
    {
      :format:
      { :pin:    :states:  :data:   :operation:            }
      { Rx6.000  {0 1}      0       ~                      }
      { ~        {0 1}      0       crc(NMT_Rx6_crc,6)[0]  }
      { ~        {0 1}      0       crc(NMT_Rx6_crc,5)[0]  }
    }
  }
}
```

<!-- 语法节 end -->

## 是什么

**device access file 是「把逻辑调用翻译成具体波形」的那一层。** 原文第一句：

> 「The device access file describes which **bitstreams need to be sent to device pins** to execute
> specific operations on the device, **translating logical calls to concrete waveforms**. The device
> access defined in the device access file are called from the APG program file.」

**扩展名 `.dvac`**（`The device access file has the .dvac file name extension.`）。
**由 [[apg-pattern-file]] 用 `:deviceAccess:` 关键字指过来**（`relative to the active directory`）。

**原文还给了它第二个职责**——这一句容易被第一句盖过去：

> 「In addition, device access files also **declare parameters from the device architecture files**
> that are to be used in device access specifications and **define constants**, also to be used in
> device access specifications.」

**所以 `.dvac` 干三件事：① 声明要用的设备参数（`:deviceParam:`）；
② 定义常量（`:constants:`）；③ 定义访问（`:apgAccess:`）。**

### 三层的分工（一句话记住）

| 层 | 在哪 | 写什么 |
|---|---|---|
| **逻辑层** | [[apg-program-file]] | C 子集代码，写 `WriteBackground(bank, DW1, …)` 这种**按名的调用** |
| **翻译层** | **本页** | `.dvac`：每个调用**哪根针、什么状态、什么数据** |
| **物理层** | [[device-architecture-file]] / [[pin-configuration-file]] / [[pin-mapping-file]] | 器件参数、针组、针名映射 |

（**这张表的分工是推断**：依据是原文「translating logical calls to concrete waveforms」这一句，
以及 `.dvac` 关键字表里 `:deviceParam:` 说参数必须
`specified in the Device architecture file`、`:pin:` 说针
`must be specified in the Pin mapping file`。**原文没有把三层并排画出来**。）

### `.dvac` 的骨架（见「语法 / 参数」节）

```
:deviceAccess:
{
[ :version: ]
    :deviceParam:  { ... }        ← 从 device architecture file 引参数
    :groups:       { ... }        ← 定义针组
[ :subGroups:      { ... } ]
[ :constants:      { ... } ]
[ :muxModeDefinition: { ... } ]
  :apgAccess:      { ... }        ← 一次访问；可重复多次
 :countedMatchPad: { ... }        ← 可重复；仅 MTP on SOC
}
```

**必需/可选照语法骨架的 `[ ]` 读**：`:deviceParam:` / `:groups:` / `:apgAccess:`
**没有** `[ ]`，其余有。

### 一次 `:apgAccess:` 里有什么

这是本页最有用的结构。`:table:` 的**每一行**描述**一次**「哪些针、什么状态、什么数据」：

| 列 | 干什么 | 关键约束（原文） |
|---|---|---|
| `:pin:` | 涉及哪些针或针组 | **必须已在 Pin mapping file 里定义**，否则再去 pin configuration file 找，**再找不到就报错** |
| `:states:` | **两个**状态字符，用 `{}` 括、空格分隔（如 `{0 1}`） | **`:data:` 算出 0 → 送左边那个；算出 1 → 送右边那个** |
| `:data:` | 决定送左右哪一个 | 可以是定值，也可以是**表达式**（`xAddr(rowAddress)` 这种） |
| `:operation:` | 要施加的 CRC / 动态总线反转 | 多个操作**按想要的顺序、逗号分隔**；不需要就整列省略 |
| `:instruction:` | 影响同表其余列执行的控制指令 | 可选 |
| `:comment:` | 注释 | 可选，`can be any text` |

**三条容易踩的细节：**

1. **`:data:` 的结果是「按位摊到针组上的」**。原文：
   > 「If the `:pin:` column contains a pin group, **the first bit of the expression result** is used
   > to determine the state character for the first pin, **the second bit for the second pin**, and
   > so on. If there are more bits in the result than there are pins in the group,
   > **the excess bits are discarded**.」
   原文在 `## Example` 里给了整段例子：四根针的组 `PinGroup`、`:data:` 填 `0x5`，
   结果的映射是 `PinGroup.000 → 0` / `.001 → 1` / `.002 → 0` / `.003 → 1`
   —— **位 0（最低位）配第 0 根针**。
2. **`:states:` 可以是接口参数**（而不只是字面字符）。要用的话接口参数必须满足三条
   （原文逐条）：`Data type must be string.` / `String to be transferred with a parameter must be
   one character.` / `Independent of any loop variable in this APG access-called program.`
   原文还配了一段 `:name: Write` 的例子，并在例子后直接写了警告：
   > 「//Be careful, do not code like Write(0, 1), or Write("01"), both of which are wrong.」
3. **`:data:` 会在一种情况下被完全忽略**：
   > 「Note that the `:data:` column is **ignored** in device accesses when the `:operation:` column
   > comprises the crc macro and CRC is enabled.」

### 两个关键字已被判「不该再用」

| 关键字 | 原文措辞 | 原文让换成什么 |
|---|---|---|
| `:devCyc:` / `:stateParam:` | `They are still supported but should not be used any more for new programs; support for them may be removed from a future version of MTL.` | **Non-transparent x-modes** 那篇附录（**本页没读**） |
| `:groups:` / `:subGroups:` | `We recommend that you use them and stop using groups.` | **pin mapping file 里的 buses**（`Buses`，**本页没读**） |

> **`:groups:` / `:subGroups:` 那两条原文说的是同一件事**，措辞也几乎一样：
> 「The buses that you can configure in the pin mapping file **fulfill the same purpose as groups and
> subgroups and are easier to use.**」——**所以这两块是「旧写法」，新写法在
> [[pin-mapping-file]] 里。但本篇没说 buses 怎么写。**

### `:countedMatchPad:` 有产品线门槛

语法节的按语直说：

> 「Note Counted match padding is available **only in MTP on SOC**.」

**这是一条硬范围限制**，不是「版本新旧」问题。
它的 `:table:` 只有两列（`:subroutine:` + 可选的 `:port:`），三条约束值得记：

- **不给 `:port:` 时，填充例程对所有 port 生效——这时 `:subroutine:` 列只能写一个。**
- **一个 port 只接受一个填充例程**（`One port accepts only one padding routine.`）。
- `:port:` 的值必须是 pin mapping file 里 `using port` 指定的那些 port 之一。

### 那张文件依赖小图（**④ 图证，2026-09-20 补**）

本篇开头那张图是 `102312.png`（251×151，**alt 文字里写的是 `.dac`**）。
**图上没有图例**，raw 里也没有一句解释它，所以能读的只有两层：**框上的字**、
**哪个框跟哪个框连着**。**框里的字画在像素里，raw 里 grep 不到**——
要核只能自己开 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\102312.png`。

- **9 个框摆成 3×3**，框里写的是文件扩展名：
  上排 `.tim` / `.dvar` / `.dac`，中排 `.wmap` / `.apg` / `.prog`，下排 `.pin` / `.pmap` / `.dcev`。
  **本图把 `.dac` 那个框涂成橙色**（也就是「高亮」）。
- **同一张图在那一族的 9 篇文档里各出现一次，每次换一个框高亮**——
  本页抽查了 **4 张**：`102175`（高亮 `.apg`）、`102312`（本图，高亮 `.dac`）、
  `102413`（高亮 `.dvar`）、`102581`（高亮 `.tim`）。
- **这 4 张里，那个框都写 `.dac`，没有一张写 `.dvac`**（处置见下 ⚠️①）。
- 框与框之间有连线，**线型有两种（实线 / 点线）**，
  且**同一处能看到方向相反的箭头**（例如 `.apg` 与 `.prog` 之间是并排两条、各指一头）。

**这张图解决掉的只有一件事**：⚠️① 里那处分歧（**正文一种拼法、图注里另一种拼法**）——
**图注没有抄错：图上那个框确实写着 `.dac`**（按 10 倍放大逐字看的）。
**它没解决的是「到底该是 `.dvac` 还是 `.dac`」**：
**正文与图各说各的，本页照旧不判**（图里也没有一个字说明谁对）。
**线型和箭头的含义**同理——**图里没有图例，raw 那几篇里 grep `dotted line` / `solid line`
也是 0 命中，本页不猜。**

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` 段。** 从原文能读出来的顺序：

1. **先在别处把地基打好**——`.dvac` 里的东西都是**引用别处的名字**：
   - `:deviceParam:` 的参数 → 必须在 [[device-architecture-file]] 里定义
   - `:groups:` 的针 → 必须在 [[pin-mapping-file]] 里定义（否则去 pin configuration file 找）
   - `:pin:` 的针/针组 → 必须在 [[pin-mapping-file]] 里定义
   - `:constants:` 的名字 → 遵循 `Naming rules and conventions`（**那篇没读**）
2. **写 `.dvac`**：`:deviceAccess:` 打头（`This keyword is required at the start of the file.`），
   然后 `:deviceParam:` → `:groups:` → 任意多个 `:apgAccess:`。
   **关键字顺序不强制**：`The order of keywords shown above is typical, but not required; you can
   rearrange the keywords within a set of curly braces as desired.`
3. **在 `.prog` 里按 `:name:` 调用**它（`:name:` 的说明：
   `The name of the device access by which it is called from the APG program code.`）。
4. **用 `.apg` 把这一整套编译起来**（`:deviceAccess:` 关键字）。

**原文给的 `:constants:` 是一条建议，不是要求**：
`This section is optional, but it is good practice to store important and often-used parameters in
these constants for easier maintenance.`

**`:constants:` 的值只许用这几个运算符**：`+ - * / << >> & | ~`，
且 `Comparison operators are not permitted in these expressions.`
**`:value:` 支持十六进制与十进制**（`Hexadecimal numbers must be prefixed with 0x`）。

## 和谁有关

- [[apg-pattern-file]] — **上游**。`:deviceAccess:` 从那里指过来；
  **`.dvac` 的路径写在那儿**
- [[apg-program-file]] — **调用方**。原文：
  `The device access defined in the device access file are called from the APG program file.`
  ——**`.prog` 里的 `WriteBackground(...)` 一类调用，落地就是这里的 `:apgAccess:`**（推断，
  依据是 `.prog` 示例的调用名与 `.dvac` 示例的 `:name: write_access` / `read_access` 同族）
- [[device-architecture-file]] — **参数来源**。`:deviceParam:` 的参数必须在那儿定义；
  原文：`All parameters imported via this keyword can be used like constants in device accesses.`
  **另外**：`:crc:` / `:dbi:` / `:scramble:` / `:bitInversion:` / `:bitOrdering:` 在
  [[apg-pattern-file]] 里填的**也都是这一篇里的表名**
- [[pin-mapping-file]] — **针名来源**，也是 `:groups:` / `:subGroups:` 的**官方替代品**
  （pin mapping file 里的 buses）。`:port:` 的取值范围也由它（`using port`）决定
- [[pin-configuration-file]] — **兜底来源**。`:groups:` 的针若不在 pin mapping file 里，
  原文说 `pins with these name must be specified in the SmarTest pin configuration file`
- [[pin]] — **概念上的下游**：`.dvac` 里的每一行最终落到具体的针上；
  **但原文没有把这两者连起来说**，本条是关系提示（推断）
- [[mtp-memory-test]] — **产品线边界**：`:countedMatchPad:` **只在 MTP on SOC 上有**
- **未建的几篇**（都在「语法 / 参数」节里被点名，**本页都没读**）：
  `Macros and functions in device accesses` / `Control instructions in device accesses`
  （**这两篇是 `:data:` 与 `:instruction:` 两列的全部依据**）、
  `Cyclic redundancy checks` / `Dynamic bus inversion`（`:operation:` 两列的依据）、
  `Buses` / `Non-transparent x-modes` / `Naming rules and conventions` /
  `Expressions with more than 64 bits` / `MTL compiler syntax` / `Syntax conventions`
- `MTL Configuration Files`（**未建**）— 原文 `## Related information` 只指向这一篇

## 版本

原文 `## Functional changes` 只有一条：

- **`Introduced before SmarTest 6.3.2`**

**就这一条，没有别的。**

> ⚠️ **§11.2②：这是哨兵值，不是「6.3.2 新增」。**
> 意思是「在本文档集覆盖范围开始之前就已经有了」。
> **照字面读会得到一条假信息。**
>
> **对照（来自同批另一篇，不是本篇的结论）**：[[apg-pattern-file]] 有三条
> （含 MTP 2.6.6 / 3.0.3 的 `:countedMatchPad:` 关键字更名），**本篇一条都没有**——
> **所以本篇不能用来判断 `.dvac` 的格式有没有变过。**（推断）

**另有一条「会失效」的预告**（不是版本条目，但同样是时间维度的事实）：
`:devCyc:` / `:stateParam:` 原文写着
`support for them may be removed from a future version of MTL`——
**这是「可能移除」，不是「已移除」**，原文没有给版本号。

## 出处

`sources:` 一篇：
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04_Device_access_file.md`
（`67571.htm`，3,476 字节，101 行）——**整篇读完**。

**本页做了什么、没做什么**：

- **「语法 / 参数」节不是 `sources:` 那篇抽的。** 那篇自己**没有完整语法段**，
  脚本改从子主题 `02.12.03.03.04.01_Device_access_file_syntax.md` 抄了 **17,358 字符**（骨架段名里写明了）。
  **那一篇本页没有读原文**——本节凡引语法节内容，依据是**页内那段逐字拷贝**。
- **`.dvac` 语法子主题下还有两篇，一篇都没读**：
  `Macros and functions in device accesses`、`Control instructions in device accesses`。
  **`:data:` 里能用哪些宏/函数、`:instruction:` 能写哪些控制指令，本页一条都没有。**
- **CRC 与动态总线反转两篇没读**（`Cyclic redundancy checks` / `Dynamic bus inversion`）——
  **`:operation:` 列是本页唯一「知道有这么一列但讲不出内容」的地方。**
- **`Buses` 没读**——**所以「该用什么代替 `:groups:` / `:subGroups:`」本页只有名字。**
- **`Non-transparent x-modes` 没读**——`:devCyc:` / `:stateParam:` 到底干什么的，本页不知道。
- **那张图看了（2026-09-20 补）**——**上一版这里写的是「一张图都没看」，
  并由此写下「本页没有任何来自图的结论」；那句话现在是错的，按实际改动如下**：
  `102312.png`（文件依赖小图）——**9 个框、`.dac` 那个框高亮、框里写的是 `.dac`**，
  见上文「那张文件依赖小图（④ 图证）」。**同一族另外三张（`102175` / `102413` / `102581`）
  也开了、逐字对过。** **图上那些字在 raw 里 grep 不到**，要核只能自己开
  `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\102312.png`。
- **图没答掉的**：`.dvac` 与 `.dac` 到底哪个对（图与正文各说各的）；
  **线型与箭头的含义**（图里没有图例，raw 里也没有说明）。
- **`## Example` 那段 `.dvac` 完整例子没有逐行讲解**，
  也**没有运行过**；`crc(NMT_Rx6_crc,6)[0]` 这种写法**本页只照抄了字面**。
- **`Naming rules and conventions` / `Expressions with more than 64 bits` /
  `MTL compiler syntax` / `Syntax conventions` 四篇没读**——
  **命名限制、超 64 位表达式、`<meta-syntax>` 的斜体约定，本页都只有名字。**
- **`MTL Configuration Files`（`## Related information` 唯一指向）没读。**

> ⚠️ **本篇的语料瑕疵，照实记、一处没替它改**：
> ① **扩展名两处不一致**：正文写
>    `The device access file has the .dvac file name extension.`，
>    而**同一篇配图的图注写的是 `.dac`**：
>    `![Miniature scheme of file dependencies with .dac file highlighted](<../../../../raw/102312.png>)`。
>    **正文一处拼法、图注一处拼法，两处不一致**——**这张图本页 2026-09-20 看了**
>    （结论在下面「那张文件依赖小图（④ 图证）」里）；**但哪个对，图和正文都答不了，
>    本页照旧不判。**
> ② **示例代码里一个花括号写成了圆括号**，**两处示例都一样**：
>    `{  x_address  (0 1}     xaddr(xAddr,yAddr)         }`
>    —— **`(0 1}` 应以 `{` 开头**（其余各行都是 `{0 1}`）。
>    这句在本篇 `## Example` 和语法节的 `## Example` 里**各出现一次**，**同一个错抄了两遍**。
> ③ **主语与谓语数不一致**：正文第一段
>    `The device access defined in the device access file **are** called from the APG program file.`
>    —— 主语 `access` 是单数、谓语是 `are`（**按上下文应是 `accesses`**）。
> ④ **单复数不一致**：同一段里写 `parameters from the device architecture **files**`（复数），
>    而关键字表里一律写 `the Device architecture **file**`（单数）。**指同一个文件。**
> ⑤ **关键字名大小写不一致**：`:subGroups:` **中间是大写 `G`**，而它的父关键字是 `:groups:`（小写）。
>    原文两个拼法都用，**本页照抄**。

`verified: doc-only`
