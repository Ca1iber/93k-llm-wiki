# 建页资料包 04 — 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.md

## 0. 元信息

- 标题（frontmatter）：Device architecture file
- H1：Device architecture file
- 字节：3992；出度：5；入边：50
- frontmatter：`{"source_html": "02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.htm", "source_topic": "68405.htm", "title": "Device architecture file"}`
- 标题结构：Device architecture file / Subtopics / Example / Related information / Functional changes

## 1. 定义文档全文（raw，禁止修改）

```markdown
---
title: "Device architecture file"
source_topic: "68405.htm"
source_html: "02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.htm"
---
# Device architecture file

#### Subtopics

- [Device architecture file syntax](<02.12.03.03.05.01_Device_architecture_file_syntax.md>)

The device architecture file describes the physical characteristics of the DUT, in particular the mapping of logical to physical addresses.

  ![Miniature scheme of file dependencies with .dvar file highlighted](<../../../../raw/102413.png>)

The device architecture file has the .dvar file name extension. It is referenced from the [APG pattern file](<02.12.03.03.02_APG_pattern_file.md>) with the :deviceArchitecture: keyword.

The device architecture files contains the scrambling, bit inversion, and bit ordering settings.

You also define certain device parameters (the x, y, and z dimensions of the memory and the data size) and have the option of defining custom parameters. All parameters are available in the APG program file.

You can also specify a maintenance operation (refresh). This is discussed in more detail in [Maintenance operations](<02.12.03.04.12_Maintenance_operations.md>).

The syntax for these settings is described in [Device architecture file syntax](<02.12.03.03.05.01_Device_architecture_file_syntax.md>).

## Example

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

## Related information

[MTL Configuration Files](<02.12.03.03_MTL_Configuration_Files.md>)

## Functional changes

- Introduced before SmarTest 6.3.2
```

## 2. 语法 / 参数段落（脚本逐字抽取，§4 —— 进页面时照抄，不重写）

### 〔Example〕

```text
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
```

## 3. 入边 32 篇（谁引它、引它的原句 —— 「和谁有关」的唯一来源）

### ← APG pattern file syntax
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md`（引 8 次）

- L99：<bitInversionTableName>: The name of the bit inversion table to be used, as it is specified in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).
- L112：<bitOrderingTableName>: The name of the bit ordering table to be used, as it is specified in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).
- L125：<crcSetting>: A named CRC setting from the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) that is to be used whenever the [crc macro](<02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md>) is called.
- L138：<dbiSetting>: A named dynamic bus inversion setting from the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) that is to be used whenever the [dbi macro](<02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md>) is called.

### ← Setting up data scrambling
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.08.01_Setting_up_data_scrambling.md`（引 3 次）

- L16：Make sure that the correct [device access](<02.12.03.03.04_Device_access_file.md>) and [device architecture files](<02.12.03.03.05_Device_architecture_file.md>) are specified in the [APG pattern file](<02.12.03.03.02_APG_pattern_file.md>).
- L22：If you want to use bit inversion, add a bit inversion table to the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) using the :bitInversion: keyword.
- L28：If you want to use bit ordering, add a bit ordering table to the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) using the :bitOrdering: keyword.

### ← Enabling and disabling maintenance operations in APG program file
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.02_Enabling_and_disabling_maintenance_operations_in_APG_program_file.md`（引 3 次）

- L85：In the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>):
- L145：In the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>):
- L239：[Maintenance operations](<02.12.03.04.12_Maintenance_operations.md>)[APG program file](<02.12.03.03.03_APG_program_file.md>)[Macros and functions in program files](<02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md>)[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)

### ← Creating the device architecture
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.06_Creating_the_device_architecture.md`（引 2 次）

- L8：Create the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) in the <device directory>/mts/device_defs/arch_defs/ directory.
- L12：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)

### ← MTL Configuration Files
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03_MTL_Configuration_Files.md`（引 2 次）

- L14：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)
- L28：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)

### ← Setting up address scrambling
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.07.01_Setting_up_address_scrambling.md`（引 2 次）

- L16：Make sure that the correct [device access](<02.12.03.03.04_Device_access_file.md>) and [device architecture files](<02.12.03.03.05_Device_architecture_file.md>) are specified in the [APG pattern file](<02.12.03.03.02_APG_pattern_file.md>).
- L20：Add an address scrambling table to the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) using the :scramble: keyword.

### ← Data scrambling
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.08_Data_scrambling.md`（引 2 次）

- L36：This is a sample bit inversion table from the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>):
- L59：This is a sample bit ordering table from the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>):

### ← Cyclic redundancy checks
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.09_Cyclic_redundancy_checks.md`（引 2 次）

- L16：CRC settings are defined in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>). There is a switch in the [APG pattern file](<02.12.03.03.02_APG_pattern_file.md>) to choose a setting or disable CRC.
- L22：[APG pattern file](<02.12.03.03.02_APG_pattern_file.md>)[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)[Device access file](<02.12.03.03.04_Device_access_file.md>)[Macros and functions in device accesses](<02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md>)

### ← Setting up dynamic bus inversion
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.10.01_Setting_up_dynamic_bus_inversion.md`（引 2 次）

- L20：Define the DBI settings in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).
- L57：In the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>):

### ← Features for the editor of MTP-EWC
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md`（引 2 次）

- L31：A device parameter which has been defined by the :deviceParam: keyword in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).
- L44：A device parameter: Opens the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) that the device parameter is defined in on a new MTP editor and jumps to where the parameter locates in this file.

### ← Device directory structure
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.03.05.02_Device_directory_structure.md`（引 1 次）

- L76：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)

### ← Creating an MTL pattern
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.04_Creating_an_MTL_pattern.md`（引 1 次）

- L10：Create the [Device access file](<02.12.03.03.04_Device_access_file.md>) (.dvac) and the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) (.dvar) according to the data sheet.

### ← Creating a pattern file
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.07_Creating_a_pattern_file.md`（引 1 次）

- L22：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) (:deviceArchitecture:)

### ← Basic MTL workflow
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.01_Basic_MTL_workflow.md`（引 1 次）

- L36：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)

### ← apgc command syntax
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md`（引 1 次）

- L170：Using the -m switch requires either a program file without a main() function that contains just the maintenance operation, or a program file containing both the main() function and the maintenance operation at the top level. In the latter case, the name of the maintenance operation must match the na

### ← Overview of configuration files
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.01_Overview_of_configuration_files.md`（引 1 次）

- L32：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) (.dvar)

### ← Preprocessor statements
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.02_Preprocessor_statements.md`（引 1 次）

- L15：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)

### ← APG pattern file
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.md`（引 1 次）

- L25：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) (:deviceArchitecture:)

### ← APG program file
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.md`（引 1 次）

- L20：The program file must contain one main() function and can contain any number of subroutines that are called by name from main(). It can also contain device parameters from the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).

### ← Device access file syntax
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.01_Device_access_file_syntax.md`（引 1 次）

- L135：The parameter must be specified in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>). All parameters imported via this keyword can be used like constants in device accesses.

### ← Macros and functions in device accesses
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md`（引 1 次）

- L73：Note that all parameters are masked with the respective device parameter from the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>), that is, dBits, xBits, yBits, and zBits. For example, when xBits is 8 and the value provided as the unscrambled x address is 258, masking would

### ← Device architecture file syntax
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md`（引 1 次）

- L953：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)

### ← Address scrambling
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.07_Address_scrambling.md`（引 1 次）

- L18：The address scrambling structure of the previous example can be described with the expressions in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>) below.

### ← Setting up cyclic redundancy checks
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.09.01_Setting_up_cyclic_redundancy_checks.md`（引 1 次）

- L20：Define the CRC settings in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).

### ← Dynamic bus inversion
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.10_Dynamic_bus_inversion.md`（引 1 次）

- L18：[APG pattern file](<02.12.03.03.02_APG_pattern_file.md>)[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)[Device access file](<02.12.03.03.04_Device_access_file.md>)[Macros and functions in device accesses](<02.12.03.03.04.02_Macros_and_functions_in_device_accesses.md>)

### ← Setting up a maintenance operation
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.01_Setting_up_a_maintenance_operation.md`（引 1 次）

- L20：Specify the maintenance operation in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>):

### ← Maintenance operations
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md`（引 1 次）

- L72：Static maintenance operation are specified by declaring the :timerMode: to be static in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>). The information on the timing to be used has to be added to the [APG pattern file](<02.12.03.03.02_APG_pattern_file.md>) using the :ti

### ← MTL compiler directories and file name extensions
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.05.01_MTL_compiler_directories_and_file_name_extensions.md`（引 1 次）

- L122：[Device architecture file](<02.12.03.03.05_Device_architecture_file.md>)

### ← Syntax highlight in the MTP editor
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.01_Syntax_highlight_in_the_MTP_editor.md`（引 1 次）

- L96：Device parameters defined in the :deviceParam: block in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).

### ← Content assistant in the MTP editor
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.02_Content_assistant_in_the_MTP_editor.md`（引 1 次）

- L27：Content AssistFilter > Device Parameter: Selecting it will list all device parameters defined in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).

### ← Error annotations in the MTP editor
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.03_Error_annotations_in_the_MTP_editor.md`（引 1 次）

- L20：Device parameter check: Checks whether the used device parameter has been redefined in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).

### ← Automatic Map Converter operating principles
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.01_Automatic_Map_Converter_operating_principles.md`（引 1 次）

- L26：If this is not the case, a transformation has to be applied to the addresses first to make them linear. This transformation has to be specified through the scrambling expression in the [Device architecture file](<02.12.03.03.05_Device_architecture_file.md>).

## 4. 出边 4 个（它引谁）

- [[APG pattern file]] → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.md`（APG pattern file）
- [[Device architecture file syntax]] → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md`（Device architecture file syntax）
- [[MTL Configuration Files]] → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03_MTL_Configuration_Files.md`（MTL Configuration Files）
- [[Maintenance operations]] → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md`（Maintenance operations）

## 5. 结构段落（Procedure / Dependency / Errors …）

### 〔related Subtopics〕（L8，1129 字符）

- [Device architecture file syntax](<02.12.03.03.05.01_Device_architecture_file_syntax.md>)

The device architecture file describes the physical characteristics of the DUT, in particular the mapping of logical to physical addresses.

  ![Miniature scheme of file dependencies with .dvar file highlighted](<../../../../raw/102413.png>)

The device architecture file has the .dvar file name extension. It is referenced from the [APG pattern file](<02.12.03.03.02_APG_pattern_file.md>) with the :deviceArchitecture: keyword.

The device architecture files contains the scrambling, bit inversion, and bit ordering settings.

You also define certain device parameters (the x, y, and z dimensions of the memory and the data size) and have the option of defining custom parameters. All parameters are available in the APG program file.

You can also specify a maintenance operation (refresh). This is discussed in more detail in [Maintenance operations](<02.12.03.04.12_Maintenance_operations.md>).

The syntax for these settings is described in [Device architecture file syntax](<02.12.03.03.05.01_Device_architecture_file_syntax.md>).

### 〔syntax Example〕（L26，2338 字符）

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
    :maintenanceOp

### 〔related Related information〕（L131，67 字符）

[MTL Configuration Files](<02.12.03.03_MTL_Configuration_Files.md>)

### 〔version Functional changes〕（L135，34 字符）

- Introduced before SmarTest 6.3.2
