---
type: object
title: Device architecture file
layer: file
stage: pattern
tags: [pattern, mtl, file-format, apg, dvar]
related: [pattern, maintenance-operations, sharing-configuration-file]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Device architecture file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **24,152 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.md>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Device architecture file syntax（整篇，取自子主题）

# Device architecture file syntax

The syntax of the device architecture file follows the conventions of the `MTL compiler syntax`（raw: `02.12.03.02.02_MTL_compiler_syntax.md`）.

Specifically, a device architecture file looks like this:

```
:deviceArchitecture:
{
[ :version: <deviceArchitectureVersion>]
[ :scramble:
    {
        :name: <scramblingTableName>
        :table:
        {
            :format:
            {:bit:            :expression:       }
            {<scrambledBits><scramblingExpr>   }
            {......                }
        }
    } ]
...
[ :bitInversion:
    {
        :name: <bitInversionTableName>
        :table:
        {
            :format:
            {:bit:               :expression:         }
            {<bitInversionBits><bitInversionExpr>  }
            {......                 }
        }
    } ]
...
[ :bitOrdering:
    {
        :name: <bitOrderingTableName>
        :table:
        {
            :format:
            {:bit:              :expression:         }
            {<bitOrderingBits><bitOrderingExpr>  }
            {......                  }
        }
    } ]
...
[ :operationOrder: { <operationList> } ]
[ :crc:
    {
        :name: <crcName>
        :bitSequence:
        {
            :name: <bitSequenceName>
            :table:
            {
                :format:
                { :pinList:       :sequence:          }
                { <pinName> ...<sequenceOrder>     }
...
            }
        }
...
        :bitExpression:
        {
            :name: <bitExpressionName>
            :table:
            {
                :format:
                { :bit:         :expression:     }
                { <bitNumber><bitExpression> }
...
            }
        }
...
        :configuration:
        {
            :name: <crcConfigurationName>
            :bitSequence: <bitSequenceName>
            :bitExpression: <bitExpressionName>
        }
...
    } ]
...
[ :dbi:
    {
        :name: <dbiName>
        :configuration:
        {
            :name: <dbiConfigurationName>
            :condition: <condition>
            :table:
            {
                :format:
                { :bus:           :flag:          }
                { <pinName> ...<flagPinName>   }
...
            }
        }
...
    } ]
...
[ :maintenanceOperation:
    {
        :name: <maintenanceOperationTableName>
        :table:
        {
           :format:
           {:operation:		:subroutine:		[:timerMode:]		[:intervalMode:] }
           {<operationName>	<subroutineName>	[<timerMode>]	[<intervalMode>] }
        }
    } ]
...
[ :deviceParam:
    {
        :format:
        {  :name:            :value:       }
        {  <paramName><paramValue>  }
        {  ......           }
    } ]
}
```

The order of keywords shown above is typical, but not required; you can rearrange the keywords within a set of curly braces as desired.

Italic text indicates meta-syntax, as described in `Syntax conventions`（raw: `02.12.03.01.02_Syntax_conventions.md`）.

## Keywords and parameters

These are the keywords and their parameters in alphabetical order:

 |

Keyword

 |

Parameters and descriptions

 |
 |

:bitInversion:

 |

Specifies bit inversion tables, that is, tables that tell MTL for which bits to invert logical 0 and 1 under which conditions.

This keyword is optional; it is required only if bit inversion is to be used. You need to specify bit inversion to use data scrambling.

There can be any number of :bitInversion: statements in a device architecture file. You reference the desired one from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） using the :bitInversion: keyword.

See the "Bit inversion keywords" table below for details.

 |
 |

:bitOrdering:

 |

Specifies bit ordering tables, that is, tables that specify ways of reordering bits.

This keyword is optional; it is required only if bit reordering is to be used. You need to specify bit ordering to use data scrambling.

There can be any number of :bitOrdering: statements in a device architecture file.You reference the desired one from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） using the :bitOrdering: keyword.

See the "Bit ordering keywords" table below for details.

 |
 |

:crc:

 |

Specifies a named cyclic redundancy check (CRC) setting.

This keyword is optional; it is required only if you want to use CRC.

There can be any number of :crc: statements in a device architecture file. You reference the desired one from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） using the :crc: keyword.

See the "CRC keywords" table below for details.

 |
 |

:dbi:

 |

Specifies a named dynamic bus inversion (DBI) setting.

This keyword is optional; it is required only if you want to use DBI.

There can be any number of :dbi: statements in a device architecture file. You reference the desired one from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） using the :dbi: keyword.

See the "DBI keywords" table below for details.

 |
 |

:deviceArchitecture:

 |

This keyword is required at the start of the file.

 |
 |

:deviceParam:

 |

Specifies values for device parameters, that is, the number of x, y, and (optionally) z bits and the number of data bits. You can also define custom device parameters.

See the "Device parameter keywords" table below for details.

 |
 |

:maintenanceOperation:

 |

Specifies maintenance operation (refreshes).

This keyword is optional; it is required only if a device maintenance operation is to be used.

There can be any number of :maintenanceOperation: statements in a device architecture file. You reference the desired one from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） using the :maintenanceOperation: keyword.

See the "Maintenance operation keywords" table below for details.

 |
 |

:operationOrder:

 |

Specifies whether dynamic bus inversion or cyclic redundancy checks should be performed first:

- To perform the DBI first, specify `{ dbi crc }`.
- To perform the CRC first, specify `{ crc dbi }`.
 |
 |

:scramble:

 |

Specifies tables for recalculating addresses.

This keyword is optional; it is required only if address scrambling is to be used.

There can be any number of :scramble: statements in a device architecture file. You reference the desired one from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） using the :scramble: keyword.

See the "Scrambling keywords" table below for details.

 |
 |

:version:

 |

<deviceArchitectureVersion>: Any string describing the version of the device architecture file.

This keyword is optional.

 |

## Bit inversion keywords

These keywords let you specify bit inversion tables for referencing from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） (see :bitInversion:, above):

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<bitInversionTableName>: The name by which the table can be referenced.

 |
 |

:table:

 |

The bit inversion specification.

See the following table for details.

 |

The :table: element contains these keywords:

 |

Keyword

 |

Parameters and descriptions

 |
 |

:bit:

 |

<bitInversionBits>: The bits that MTL is to invert.

Bit specifications can contain ranges as well as lists of pins.

For example: `[0..8,10,12]` which indicates pins 0 through 8, pin 10, and pin 12. The order of the bits is significant, that is `[0,1,2,3]` is a different subgroup from `[3,2,1,0]`.

If a range lists the higher number first, the order of most and least significant bits is reversed: Specifying bits `[15..0]` is an easy way of making bit 0 the least significant bit.

 |
 |

:expression:

 |

<bitInversionExpr>: An expression that controls whether the specified bits are inverted or not.

MTL calculates the value of the expression and uses the specified order only if the expression evaluates to logical 1.

Expressions can contain the `AND`, `OR`, `NOT`, and `XOR` logical operators.

 |

## Bit ordering keywords

These keywords let you specify bit ordering tables for referencing from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） (see :bitOrdering:, above):

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<bitOrderingTableName>: The name by which the table can be referenced.

 |
 |

:table:

 |

The bit ordering specification.

See the following table for details.

 |

The :table: element contains these keywords:

 |

Keyword

 |

Parameters and descriptions

 |
 |

:bit:

 |

<bitOrderingBits>: The order in which MTL is to arrange the bits.

Bit specifications can contain ranges as well as lists of pins.

For example: `[0..8,10,12]` which indicates pins 0 through 8, pin 10, and pin 12. The order of the bits is significant, that is `[0,1,2,3]` is a different subgroup from `[3,2,1,0]`.

If a range lists the higher number first, the order of most and least significant bits is reversed: Specifying bits `[15..0]` is an easy way of making bit 0 the least significant bit.

 |
 |

:expression:

 |

<bitOrderingExpr>: An expression that controls whether the reordering is used or not.

MTL calculates the value of the expression and inverts the specified bits only if the expression evaluates to logical 1. There must always be paris of expressions (and accompanying entries in the :bits: column) that must be the logical inversions of each other (that is, one expression in the pair must evaluate to 1 exactly when the other evaluates to 0).

Expressions can contain the `AND`, `OR`, `NOT`, and `XOR` logical operators.

 |

## CRC keywords

These keywords let you specify CRC settings for referencing from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） (see :crc:, above):

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<crcName>: The name by which the CRC setting can be referenced.

 |
 |

:bitExpression:

 |

A specification to calculate the CRC bits.

There can be any number of :bitExpression: blocks in a :crc: block. See the Bit expression keywords section below for details.

 |
 |

:bitSequence:

 |

A specification of bits from which a CRC expression is to be calculated.

There can be any number of :bitSequence: blocks in a :crc: block. See the Bit sequence keywords section below for details.

 |
 |

:configuration:

 |

A named combination of a bit expression and a bit sequence.

There can be any number of :configuration: blocks in a :crc: block. See the Configuration keywords section below for details.

 |

## Bit expression keywords

The :bitExpression: element contains these keywords, either directly or within the subordinate :table: block:

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<bitExpressionName>: The name by which this bit expression can be referenced in a :configuration: block.

 |
 |

:bit:

 |

<bitNumber>: The number of the bit in the CRC word.

 |
 |

:expression:

 |

<bitExpression>: An expression that calculates the CRC bit.

The expression can access the bits of the bit sequence (the source data for calculating the CRC) using the e pseudo-variable. For example, to access bit 1 of the bit sequence, use `e[1]`.

If the result of the expression has more bits than there are pins in the pin list of the pin expression used (see below), only its least significant bits are assigned to the result bits.

 |

## Bit sequence keywords

The :bitSequence: element contains these keywords, either directly or within the subordinate :table: block:

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<bitSequenceName>: The name by which this bit sequence can be referenced in a :configuration: block.

 |
 |

:pinList:

 |

<pinName>: The name of a pin the edges of which are used to calculate the CRC.

There can be multiple pins in each :pinList: row. Each row must contain the same number of pins.

If rows contain multiple pins, the edges of each of these pins are handled in the same way when connecting a bit expression (see above). Each column of pins in the pin list result in one bit in the result of applying the crc macro. For example, if each row of the pin list contains four pins, the crc macro result has four bits.

 |
 |

:sequence:

 |

<sequenceOrder>: The bits of the expression e to which the edges of the device access on the pin are assigned.

Edges are assigned in order to the listed bits, that is, the first edge is assigned to the first listed bit, the second edge to the second bit, and so on.

Not all edges of an access need to be assigned to bits, but there must be an edge for every listed bit. In other words, a device access must contain at least as many edges as bits are listed.

 |

## Configuration keywords

The :configuration: element contains these keywords:

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<crcConfigurationName>: The name by which this CRC configuration can be referenced in a crc() macro.

See `Macros and functions in device accesses`（raw: `02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md`） for more information on the crc() macro.

 |
 |

:bitExpression:

 |

<bitExpressionName>: The name of the bit expression that is to be used in this named CRC configuration.

The bit expression must be defined in the same :crc: block that contains this :configuration: block.

 |
 |

:bitSequence:

 |

<bitSequenceName>: The name of the bit sequence that is to be used in this named CRC configuration.

The bit sequence must be defined in the same :crc: block that contains this :configuration: block.

 |

## DBI keywords

These keywords let you specify DBI settings for referencing from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） (see :dbi:, above):

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<dbiName>: The name by which the DBI setting can be referenced.

 |
 |

:configuration:

 |

A a combination of a condition for when to invert bits and a list of pins on which to invert the bits.

There can be any number of :configuration: blocks in a :dbi: block. See the Configuration keywords section below for details.

 |

## Configuration keywords

The :configuration: element contains these keywords, either directly or within the subordinate :table: block:

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<dbiConfigurationName>: The name by which this bit expression can be referenced in the :operation: column of a device access in a `Device access file`（raw: `02.12.03.03.04_Device_access_file.md`）.

 |
 |

:condition:

 |

<condition>: A specification of a condition under which the bus inversion is to be applied.

The condition must be a statement that evaluates to true or to false. If it evaluates to true, bus inversion is applied; if it does not, no bus inversion is applied.

The expression can use the e pseudo-variable that refers to all pins specified in the :bus: column (see below). You can access:

- Individual pins with expressions like `e[3]`
- Ranges of pins with expressions like `e[3..6]`
- All pins of the bus with `e[]`

You may want to use the bitCount function, which is described in `Macros and functions in device accesses`（raw: `02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md`）.

 |
 |

:bus:

 |

<pinName>: A list of the pins that belong to the bus which is to be inverted.

There can be multiple rows, with each row linking a subset of the bus pins to a particular flag pin (see below). The bus to be inverted is the union of all rows.

Note that a device access that employs dynamic bus inversion (that is, that uses the `dbi` macro in the :operation: column) must use all pins of the bus, if it accesses the bus. It must not address only some pins of the bus.

 |
 |

:flag:

 |

<flagPinName>: A name of a flag pin outside of the bus itself. This pin is inverted whenever the section of the bus specified in the same row is inverted.

The flag pin must be a single pin.

A flag pin is only inverted when the associated section of the bus is inverted, which requires all pins in that section to be included in the :pin: column of the row of the device access in which the dbi macro is called.

 |

## Device parameter keywords

These keywords let you specify parameters describing important architectural characteristics of the DUT (see :deviceParam:, above):

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<paramName>: The name of the device parameter you want to define:

- `xBits` to provide the number of x address bits
- `yBits` to provide the number of y address bits
- `zBits` to provide the number of z address bits
- `dBits` to provide the number of data bits.

Please note that these four words are built-in keywords words that you must use in this definition.

The `zBits` parameter is optional. You can use it if your device has several memory banks or the DUT is a memory SIMM.

You can also define additional parameters depending on your test. For example, in tests with burst mode, you can define a parameter burst length to enter the number of vectors in a burst. These additional parameters can be used in the `APG program file`（raw: `02.12.03.03.03_APG_program_file.md`） and `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`）.

You can use all operators (except assignment and increment operators) in defining device parameters. You cannot use program parameters in the definition of device parameters.

 |
 |

:value:

 |

<paramName>: The value that the parameter has for this device.

Hexadecimal values must be prefixed with `0x`.

 |

## Maintenance operation keywords

These keywords let you specify maintenance (refresh) operations for referencing from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） (see :maintenanceOperation:, above):

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<maintenanceOperationTableName>: The name by which the table can be referenced.

 |
 |

:table:

 |

The maintenance operation specification. In this table:

- A row specifies a refresh's configuration.
- If the operation is a single refresh operation, this table contains only one row.
- If the operation is a multiple refreshes operation, this table contains multiple rows.

See the following table for details.

 |

The :table: element contains these keywords:

 |

Keyword

 |

Parameters and descriptions

 |
 |

:intervalMode:

 |

<intervalMode>: `compensated` or `accumulated`.

If the interval mode is `compensated`, delays in executing a refresh operation caused by non-interruptible sequences are deducted from the next refresh interval. In effect, a refresh interval begins when the previous refresh should have happened (irrespective of when it actually happened).

If the interval mode is `accumulated`, a refresh interval always begins with the previous refresh. Any delays to one refresh cause all following refreshes to be pushed back by a similar amount.

If the :intervalMode: keyword is not used, the compensated mode is applied.

See `Maintenance operations`（raw: `02.12.03.04.12_Maintenance_operations.md`） for more information on interval modes.

 |
 |

:operation:

 |

<operationName>: The name of the maintenance operation configuration to be executed. The allowed keywords:

- maintop_time_a for single refresh operations.
- static_maintop_time_x (x can be any given letter) for multiple refreshes operations.

Each refresh is assigned with a static_maintop_time_x (x can be any given letter) keyword, where x must be different from the other refreshes'.

Note that these keywords must be identical with the keywords for the refresh-period names in the `Timing file`（raw: `02.12.03.03.09.02_Timing_file.md`）.

See `Enabling and disabling maintenance operations`（raw: `02.12.03.04.12.02_Enabling_and_disabling_maintenance_operations_in_APG_program_file.md`） for more information on controlling refreshes from a program.

 |
 |

:subroutine:

 |

<subroutineName>: The name of the subroutine from the `APG program file`（raw: `02.12.03.03.03_APG_program_file.md`） that is to executed as the maintenance operation.

 |
 |

:timerMode:

 |

<timerMode>: `dynamic` or `static`.

If the timer mode is `dynamic`, the refresh interval for device maintenance is specified in the SmarTest timing equation system. Refreshes are initiated by SmarTest and can occur only on tester cycle boundaries.

If the timer mode is `static`, device maintenance is predefined and inserted into the pattern during compilation. Refreshes can occur between tester cycle boundaries. A reference to the timing equation has to be added to the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`）. See `Maintenance operations`（raw: `02.12.03.04.12_Maintenance_operations.md`） for more information.

If the :timerMode: keyword is not used, the dynamic mode is applied.

The static timer mode is not compatible with multiport operation.

 |

## Scrambling keywords

These keywords let you specify maintenance (refresh) operations for referencing from the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`） (see :scramble:, above):

 |

Keyword

 |

Parameters and descriptions

 |
 |

:name:

 |

<scramblingTableName>: The name by which the table can be referenced.

 |
 |

:table:

 |

The scrambling specification.

See the following table for details.

 |

The :table: element contains these keywords:

 |

Keyword

 |

Parameters and descriptions

 |
 |

:bit:

 |

<scrambledBits>: A bit in the scrambled address (that is, the physical address).

To specify the bits, use the formats xan, yan, and zan, where n is the specific bit in the respective dimension. For example: xa0, xa1, ya0, za5.

 |
 |

:expression:

 |

<scramblingExpr>: A logical expression to calculate the value of the specified bit.

To calculate the expression, you can use the logical address bits x0, x1, y0, z0, etc. You can also use the `AND`, `OR`, `NOT`, and `XOR` logical operators.

 |

### Example

This is an example of a device architecture file for an DRAM device. It contains address scrambling, bit inversion, cyclic redundancy checks, and device parameter definitions.

```
  :deviceArchitecture:
  {
    :version:  1.0
    :scramble:
    {
      :name:  "address scrambling"
      :table:
      {
        :format:
        {  :bit:  :expression:  }
        {  xa0    "not x0"      }
      }
    }
    :bitInversion:
    {
      :name:  "bit inversion"
      :table:
      {
        :format:
        {  :bit:    :expression:  }
        {  d[0..7]  x0            }
      }
    }
    :bitOrdering:
    {
      :name:  "bit ordering"
      :table:
      {
        :format:
        {  :bit:     :expression:  }
        {  d[15..0]  "not x1"      }
        {  d[0..15]  x1            }
      }
    }
    :crc:
    {
      :name: "my_crc"
      :bitExpression:
      {
        :name: "my_crc_expression"
        :table:
        {
          :format:
          { :bit: :expression: }
          { "0" "e[0]^e[8]" }
          { "1" "e[1]^e[9]" }
          { "2" "e[2]" }
          { "3" "e[3]" }
          { "4" "e[4]" }
          { "5" "e[5]" }
          { "6" "e[6]" }
          { "7" "e[7]" }
        }
      }
      :bitSequence:
      {
        :name: "my_crc_bitOrder"
        :table:
        {
          :format:
          { :pinList: :sequence: }
          { DQ.000,DQ.008,DQ.016,DQ.024 [0..1] }
          { DQ.001,DQ.009,DQ.017,DQ.025 [2..3] }
          { DQ.002,DQ.010,DQ.018,DQ.026 [4..5] }
          { DQ.003,DQ.011,DQ.019,DQ.027 [6..7] }
          { DQ.004,DQ.012,DQ.020,DQ.028 [8..9] }
          { DQ.005,DQ.013,DQ.021,DQ.029 [10..11] }
          { DQ.006,DQ.014,DQ.022,DQ.030 [12..13] }
          { DQ.007,DQ.015,DQ.023,DQ.031 [14..15] }
          { dbii.000,dbii.001,dbii.002,dbii.003 [16..17] }
        }
      }
      :configuration:
      {
        :name: "crcConfig1"
        :bitSequence: "my_crc_bitOrder"
        :bitExpression: "my_crc_expression"
      }
    }
    :maintenanceOperation:
    {
      :name: BurstRefresh
      :table:
      {
        :format:
        {  :operation:  :subroutine:  }
        {  maintop_a    refreshBurst  }
      }
    }
    :deviceParam:
    {
      :format:
      {  :name:  :value:  }
      {  xBits   10       }
      {  yBits   8        }
      {  dBits   16       }
    }
  }
```

<!-- 语法节 end -->

## 是什么

- **`.dvar` 文件**。原文：*"The device architecture file describes the physical characteristics
  of the DUT, in particular the mapping of logical to physical addresses."*
- **被谁引用**：APG pattern file，用 `:deviceArchitecture:` 关键字（原文）。
- **装什么**：`scrambling`（地址加扰）、`bit inversion`、`bit ordering` 三种设置；
  以及 **device parameters** —— x / y / z 三个存储维度和数据宽度，**还可以自定义参数**
  （原文 *"have the option of defining custom parameters"*）。
  **所有参数在 APG program file 里都可用**。
- **还可以声明维护操作**（refresh），见 [[mtp-maintenance-operations]]。
- **放哪**：（`Creating the device architecture` 原文）
  `<device directory>/mts/device_defs/arch_defs/`。
- **属于哪一段**：`stage: pattern` —— 它是 **APG 侧的配置文件**，
  被 pattern 引用、给 pattern 用 → [[pattern]]。它本身不是 pattern，是 pattern 的**前提**。

> **本页的「语法 / 参数」是两篇合成的。**
> 这份文件的语法**不在定义文档里**，在子主题 `Device architecture file syntax` 里
> （原文：*"The syntax for these settings is described in …"*）。
> 子主题**通篇就是关键字表**（961 行），所以脚本把它**整篇**收进这一节，
> 再在后面接上定义文档自己的 `Example`。**「取自子主题」写在段名里，别搞混来源。**
>
> 对照 [[sharing-configuration-file]]：那份文件的 `## Syntax` 是**内联**的，
> 9,403 字符全在定义文档自己身上，没有子主题。
> **同是 MTL 配置文件，来源结构不同——这正是为什么语法节要逐段标来源。**
>
> 这个「跟子主题」的能力是 2026-09-18 才补进 `extract/objpack.py` 的：
> 在此之前本页的语法节**是空的**（只有一份 Example），
> 而 `Device architecture file` 这一族**共 10 篇** MTL 配置文件都是这个结构。
> 修好后用 `python objscaffold.py --refresh-syntax device-architecture-file`
> 只重刷了这一节，**散文一字未动**。

## 典型用法

**什么时候写它**（`Creating an MTL pattern` 原文，第 2 步）：

> "Create the Device access file (.dvac) and the Device architecture file (.dvar) according to
> the data sheet."

—— **照着数据手册写**，不是照着模板写。地址映射、位序这些都来自器件的 datasheet。

**分项怎么加**（全部来自入边原文）：

| 想做什么 | 加什么 | 出处 |
|---|---|---|
| 地址加扰 | 用 `:scramble:` 关键字加一张地址加扰表 | Setting up address scrambling |
| 位反转 | 用 `:bitInversion:` 加一张位反转表 | Setting up data scrambling |
| 位排序 | 用 `:bitOrdering:` 加一张位排序表 | Setting up data scrambling |
| CRC | 在本文件定义 CRC 设置；在 APG pattern file 里**有开关**选一个设置或禁用 | Cyclic redundancy checks |
| DBI（动态总线反转） | 在本文件定义 DBI 设置 | Setting up dynamic bus inversion |
| 维护操作 | 用 `:maintenanceOperation:` 指定 | Setting up a maintenance operation |
| **静态**维护操作 | 在本文件里声明 `:timerMode: static`；**时序信息要写进 APG pattern file** | Maintenance operations |

**一个前置动作**（两条入边都写了同一句）：动手加表之前，
*"Make sure that the correct device access and device architecture files are specified in the
APG pattern file."* —— **先在 APG pattern file 里把两份文件挂对**，否则后面加的表根本不生效。

**表名从哪被取用**（`APG pattern file syntax` 原文，四个参数都指向本文件）：

- `<bitInversionTableName>` — 位反转表名
- `<bitOrderingTableName>` — 位排序表名
- `<crcSetting>` — 具名 CRC 设置，`crc` 宏每次调用时使用
- `<dbiSetting>` — 具名 DBI 设置，`dbi` 宏每次调用时使用

**注意这四个是「名字」而不是「内容」**：本文件是**定义表**的地方，
APG pattern file 是**选哪张表**的地方。改错了地方会很难查。

## 和谁有关

**上游：谁引它**

- `APG_pattern_file` —— 用 `:deviceArchitecture:` 挂上本文件；表名也从这里选
- `Device_access_file` —— 与 .dvar 并列创建（`.dvac` + `.dvar`），同一个数据手册出来

**下游：它的内容流到哪**

- **APG program file** —— 本文件里定义的参数在程序文件里**可用**（原文：
  *"It can also contain device parameters from the Device architecture file."*）
- **Device access file syntax** —— 原文：*"The parameter must be specified in the Device
  architecture file. All parameters imported via this keyword can be used like constants in
  device accesses."*
- **Macros and functions in device accesses** —— 参数**会被对应的 device parameter 掩码**
  （`dBits` / `xBits` / `yBits` / `zBits`）（原文；文中的具体算例见 raw）。
  **这条最容易被忽略**：地址数值不是原样进去的，先被位宽截断。

**工具：谁会打开它**

- **MTP editor** —— device parameter 可跳转（原文：*"Opens the Device architecture file that
  the device parameter is defined in on a new MTP editor and jumps to where the parameter
  locates in this file."*）；Content Assist 的 `Device Parameter` 过滤器列出本文件定义的全部参数；
  Error annotations 里有 `Device parameter check`（查参数是否被重定义）；
  Syntax highlight 也认 `:deviceParam:` 块
- **Automatic Map Converter** —— 地址不线性时，*"a transformation has to be applied to the
  addresses first to make them linear. This transformation has to be specified through the
  scrambling expression in the Device architecture file."* —— **加扰表达式是给工具用的，不只是给机台用的。**

**同族**：`MTL_Configuration_Files`（本文件是 MTL 配置文件族的一员）、
[[mtp-maintenance-operations]]、`Device_architecture_file_syntax`。
这三个都**不入 backlog**（入度不够），所以不链，名字留在这里是为了能照着去 raw 里搜。

> 以上每条都来自 `edges.jsonl` 里带原句的边。**本页没有推断。**

## 版本

**两篇各有一份 `Functional changes`，合起来才是完整的** —— 这是个容易漏的坑：

定义文档（`Device architecture file`）：

- **Introduced before SmarTest 6.3.2**

子主题（`Device architecture file syntax`）—— **按关键字分的引入版本**：

- **Introduced before SmarTest 6.3.2**
- **MTP 2.4.0**：加入 `:crc:` 关键字及其从属关键字
- **MTP 2.4.0**：加入 `:dbi:` 关键字及其从属关键字
- **MTP 2.4.0**：加入 `:operationOrder:` 关键字

> ⚠️ **只看定义文档那一份，会以为「早于 6.3.2 就没别的了」**，
> 于是漏掉 `:crc:` / `:dbi:` / `:operationOrder:` 三个关键字是 **MTP 2.4.0** 才加的。
> **「这机器上能不能用某个关键字」的答案在子主题里，不在定义文档里。**

本 wiki 面向 **7.10.3**，上述关键字均在。
**「before 6.3.2」意味着没有确切的引入版本**——文档本身就只说「早于」。

## 出处

- 定义文档：`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.md`
  （TDC `68405.htm`，3,992 字节）
- **语法子主题**：`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md`
  （23,466 字节，961 行）
- **入边 50 条 / 32 篇文档**：`extract/pack/04-device-architecture-file.md`
  （50 是边数，32 是**去重后的文档数**——`APG pattern file syntax` 一篇就引了 8 次。
  口径同 `hubs-dedup.csv`：**只算 `inline` 边**。）
- 所属：**Memory Test Plus**（`02.12`），不是通用 93K 功能
- 本页 `verified: doc-only` —— 只在 TDC 文档里确认存在，未在真实机台上写过这份文件。
