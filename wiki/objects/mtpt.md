---
type: object
title: MTPT (STPM MCM mapping tables)
layer: file
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.03.04_MTPT__STPM_MCM_mapping_tables.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# MTPT (STPM MCM mapping tables)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **18,352 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.03.04_MTPT__STPM_MCM_mapping_tables.md>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.03.04.01_STP_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.02_Pin_mapping_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.03_Group_mapping_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.04_Test_mapping_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.05_Test_suite_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.06_Bin_mapping_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.07_Test_number_mapping_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.08_Testflow_variable_mapping_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.09_Special_tests_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.10_Shared_pins_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.11_Test_flag_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.12_Off_DC_levels_table.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.14_MTPT_configuration_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 STP table）

Each row in the STP table describes one test program. The table contains these columns:

- STP: The name of the test program
- Test Flow Path: The file path of the STP's testflow file
- Prefix: The prefix that STPM MCM will use for renaming elements from this STP. This value can be omitted if no prefix is desired for elements from an STP.

Note that whether STPM MCM actually applies these prefixes to pins from the STP depends on the value in the Apply Prefix On Pin Config column (see below). Whether the prefixes are used for other imported elements is controlled by the global setting apply_prefix_on_specs_and_equations (described in `STPM MCM parameter settings`（raw: `02.09.03.03.01_STPM_MCM_parameter_settings.md`）).

- Bin Offset: The number that STPM MCM adds to bin numbers from this STP when merging it into the MTP
- Test Number Offset: The number that STPM MCM adds to test numbers from this STP when merging it into the MTP
- Tim EQNSET Offset: The number that STPM MCM adds to timing equation set numbers from this STP when merging it into the MTP
- Lev EQNSET Offset: The number that STPM MCM adds to level equation set numbers from this STP when merging it into the MTP
- Test Mode: (Optional) The test mode from the test table that is to be used or this STP. This value can be left empty if no mode is desired for a test.
- Apply Prefix On Pin Config: Whether the prefixes from the Prefix column are used for this pin:

  - 0: The prefix is not applied to the names of pin configuration objects from this STP
  - 1: The prefix is applied to the names of pin configuration objects from this STP

Pin configuration objects include names of pins, pin groups, power supplies, port, and utility lines.

- Keep Unused Data: Whether all timing, level, and pattern data from this STP is copied to the MTP or just the data that is actually used by the MTP:

  - 0: Only timing, level, and pattern data that is used is copied to the MTP
  - 1: All timing, level, and pattern data in the STP is copied to the MTP

- Notes: This column allows both you and STPM MCM to add remarks about the test program. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

### Syntax（取自子主题 Pin mapping table）

Each row in the pin mapping table describes the mapping of a specific STP pin or utility line. The table contains these columns:

- STP:<STP name>: Beginning at the left of the table, there is one column for each STP, with the STP name as the column title. The columns list the pin names from the STPs.
- MTP Pin[@shared port]: The name of the pin in the MTP. If the pin belongs to a shared port in the MTP, the port name is appended with a @ character, for example, "A_CLK@MTP_SHARED".

The default name STPM MCM enters in this column is the STP pin name with the prefix defined in the `STP table`（raw: `02.09.03.04.01_STP_table.md`）. (If the "apply prefix on pin config" setting is 0, STPM MCM enters just the STP pin name without the prefix.)

If an STP pin is not connected to any MTP pin, this is indicated by __NC__.

- MTP Pin Attribute: Digital pins can be defined as triggers in this column; analogs pins can be assigned triggers.

A digital pin is defined as a trigger by entering a statement in the form `TRIG_DEF:`<trigger_id>, <input_pin> in this column:

  - <trigger_id> must be C1, C2, C3, or C4. Each of these IDs can be used only once per MCM.
  - <input_pin> specifies which pin is used as the trigger. It can be either COM1 (to specify the CT2 pin) or COM2 (to specify the CT1 pin).

An analog pin is triggered by a digital pin by including a statement of the form `TRIG:`<pin name> in this column. <pin name> is the name of a pin (as it appears in the MTP Pin[@shared port] column) that you have declared as a trigger pin as described above.

- Site <n>: There is one column for each site that has been defined in the generate_template command. These columns list the channel number that the pin has for the site in question in the MTP. This information is not automatically generated by STPM MCM and must be filled in by you.
- Notes: This column allows both you and STPM MCM to add remarks about the pin. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

### Syntax（取自子主题 Group mapping table）

Each row in the group mapping table describes the mapping of a specific STP entity (port, pin group, or utility purpose). The table contains these columns:

- STP:<STP name>: Beginning at the left of the table, there is one column for each STP, with the STP name as the column title. The columns list the entity names from the STPs.
- MTP Group: The name of the entity in the MTP.

The default name STPM MCM enters in this column is the STP name with the prefix defined in the `STP table`（raw: `02.09.03.04.01_STP_table.md`）. (If the "apply prefix on pin config" setting is 0, STPM MCM enters just the STP pin name without the prefix.)

If an STP entity is not connected to any MTP entity, this is indicated by __NC__.

- Notes: This column allows both you and STPM MCM to add remarks about the port, pin group, or utility purpose. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

STPM MCM initially fills this column with the name of the STP from which an entity is imported and the firmware command that is triggered by the mapping (DFGP for pin groups, DFPT for ports, or DFUP for utility purposes).

### Syntax（取自子主题 Test mapping table）

Each row in the test mapping table describes the mapping of a specific STP test suite or test group. In certain cases (see the CCT mode described below), multiple test suites can be described in one row.

The table contains these columns:

- STP:<STP name>: Beginning at the left of the table, there is one column for each STP, with the STP name as the column title. The columns list the test suite or test group names from the STPs.
- Mode: The integration mode for the test suite or test group in the STP:

  - TG: Test group integration mode - the test group from the STP is integrated into the MTP, with all of its contained test suites and test groups and internal structure (branches etc.) intact. This mode applies only to test groups.
  - TS: Test suite integration mode. The test suite is integrated into the MTP without any surrounding testflow structures. This mode applies only to test suites.
  - CCT: Concurrent test integration mode - all test suites in this row are merged into the same MTP test group, which conforms to the concurrent test framework, and will be executed concurrently.

This mode applies only to test suites and requires test suites to be listed in at least two <STP name> columns in this row.

  - CCT_FG: This mode is similar to the CCT mode. However, instead of creating a multi_bin node in the fail branch of the test suite, it creates a test group named "<test object name>_FG" in this branch. You can insert objects into this group by specifying it as a parent group.

For example, if a test suite has the name "CCT1" in the MTP Test Object column (see below) and has the integration mode CCT_FG, you can enter "CCT1_FG" in the MTP Parent Group column (see below) of any other object to include it in the fail branch of CCT1.

  - NOP: This object is not integrated into the MTP.

You can use this mode to temporarily exclude objects that you may want to include again later (and therefore do not want to delete from the table), for example during debugging.

- MTP Parent Group: The test group in the MTP into which this test suite or test group is put. This entry is ignored if a matching test object already exists in the MTP. (See MTP Test Object, below, for details.)

If there is no entry in this column, the test group or test suite is integrated at the end of the testflow in the MTP.

- MTP Test Object: The name of the test suite or test group in the MTP that is replaced by the object from the STP.

If an object with this name already exists in the MTP, the object from the STP replaces it. If no object with this name exists in the MTP, the object from the STP is copied to the location specified by the entry in the MTP Parent Group column and renamed, if necessary.

- Notes: This column allows both you and STPM MCM to add remarks. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

### Syntax（取自子主题 Test suite table）

Each row in the test suite table describes one test suite. The table contains these columns:

- STP: The name of the STP (source test program) from which the test suite is imported
- STP TestSuite: The name of the test suite in the STP
- MTP TestSuite: The name of the test suite in the MTP
- Test Flags: The name of the test flag set that is applied to the test suite in the MTP.

This name must match the entry for the desired flag set in the FlagSet Id column of the `Test flag table`（raw: `02.09.03.04.11_Test_flag_table.md`）.

If the Test Flags column contains the value __DEFAULT__, no test flag set is specified for the test suite and it uses the default test flags for the MTP.

- UTM Id: The ID of the UTM that will be executed by this test suite
- Limits: Test limits specified for the test suite

Each limit entry has the format <limit name> `=`<lower value> <= x <= <upper limit>. You can omit either the lower or the upper limit (for example `functional = x <= 4)`. You can also use < in place of <=.

If you want to specify more than one limit, you must put each one in a new line (separated by CR characters) and put a semicolon (;) after each limit except the last one.

- Parameters: The parameters that are passed to the test method when the test suite is executed

Each parameter entry has the format <parameter name> `=`<parameter value>.

If you want to specify more than one parameter, you must put each one in a new line (separated by CR characters) and put a semicolon (;) after each parameter except the last one.

- Notes: This column allows both you and STPM MCM to add remarks about the test suite. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

STPM MCM initially fills this column with the information on where it has replaced pin, group, or port names, as well as any warnings.

### Syntax（取自子主题 Bin mapping table）

Each row in the bin mapping table describes the mapping of a specific STP bin. The table contains these columns:

- STP: The name of the STP from which the bin is imported
- STP SBin: The software bin number of the bin in the STP
- SBin: The software bin number of the bin in the MTP
- SBin Label: The software bin label of the bin in the MTP
- HBin: The hardware bin number of the bin in the MTP
- HBin Label: The hardware bin label of the bin in the MTP
- Type: The type of the bin in the MTP. The value in this column can be good or bad.
- Color: The color of the bin in the MTP
- Reprobe: Whether the Reprobe flag is set for this bin in the MTP. The value in this column can be 0 (Reprobe off) or 1 (Reprobe on).
- Overon: Whether the Overon flag is set for this bin in the MTP. The value in this column can be 0 (Overon off) or 1 (Overon on).
- Notes: This column allows both you and STPM MCM to add remarks about the bn. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

STPM MCM initially fills this column with the source of the bin. It also notes any conflicting definitions it finds and indicates bins that are default bins.

If any conflicts are noted, they are prefixed with the coordinates of the conflicting cell (in standard Excel notation). For example, "[D6]" indicates that the value in row 6, column D conflicts with an earlier entry in the same column.

### Syntax（取自子主题 Test number mapping table）

Each row in the test suite table describes one test number. The table contains these columns:

- STP: The name of the STP (source test program) from which the test number is imported
- STP Test Number: The test number as it is used in the STP
- MTP Test Number: The test number in the MTP to which the STP test number is mapped
- Notes: This column allows both you and STPM MCM to add remarks about the test number. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

STPM MCM initially fills this column with the information on the source of the number and any detected conflicts.

### Syntax（取自子主题 Testflow variable mapping table）

Each row in the testflow variable mapping table describes the mapping of a specific variable or flag. The table contains these columns:

- STP: The name of the STP from which the variable is imported

For system testflow flags, this column contains SYSTEM_FLAGS.

- STP Var: The name of the variable or flag in the STP

For system testflow flags, this column is empty.

- MTP Var: The name of the MTP variable or flag to which the STP variable or flag is mapped
- Type: The data type of the MTP variable or flag
- Value: The value to which the MTP variable or flag is set

For system flags, the value may initially be empty if a flag was defined in none of the STPs or had different settings in different STPs. You must fill in any empty cells in this column; otherwise, STPM will generate an error when creating the MTP.

- Notes: This column allows both you and STPM MCM to add remarks about the variable or flag. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

STPM MCM notes here any conflicts and other issues detected.

### Syntax（取自子主题 Special tests table）

Each row in the special tests table describes the handling of one type of special test suite. The table contains these columns:

- Type: The kind of `special test suite`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.md`） that the column describes
- Master STP: The name of the STP from which this kind of test suite is imported.

For example, when the entry for "download" in this column is "MyTP4", every time the download special test suite is needed in the MTP, the version from the MyTP4 STP is used.

An entry of __NONE__ in this column indicates that none of the specified STPs contain a special test of this type.

- Notes: This column allows both you and STPM MCM to add remarks. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

### Syntax（取自子主题 Shared pins table）

Each row in the shared pins table describes the handling of one set of shared pins. The table contains these columns:

- CCT Group Name: The name of an MTP test group that contains concurrent tests

The name must appear in the MTP Parent Group column in the `Test mapping table`（raw: `02.09.03.04.04_Test_mapping_table.md`） and the mode specified for the group must be CCT.

- Shared DPS Pin/Port: The name of the shared pin or digital port

If a shared port is noted here, it must be listed in the MTP Pin[@shared port] column of the `Pin mapping table`（raw: `02.09.03.04.02_Pin_mapping_table.md`）.

- Master STP: The name of the STP from which the timings and levels for this shared pin or port are imported.
- Notes: This column allows both you and STPM MCM to add remarks about the shared pin. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

### Syntax（取自子主题 Test flag table）

Each row in the test flag table describes a test flag set. The table contains these columns:

- FlagSet Id: The name of the flag set

This name can be used to reference the flag set from the `Test suite table`（raw: `02.09.03.04.05_Test_suite_table.md`）.

- (individual flags): Each column corresponds to one flag. It can contain 1 to indicate that the flag is on, or 0 to indicate that it is off.
- Notes: This column allows both you and STPM MCM to add remarks about the flag set. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

In all columns describing flag settings, 0 indicates that the flag is off and 1 indicates that it is on.

### Syntax（取自子主题 Off DC levels table）

Each row in the levels table describes the levels for one DC pin. The table contains these columns:

- MTP Pin: The name of the DC pin in the MTP for which you are setting the levels. The pin names in this column must match the names in the `Pin mapping table`（raw: `02.09.03.04.02_Pin_mapping_table.md`）.

The __DEFAULT__ entry is already predefined; it applies to all pins of inactive STPs for which there is no explicit entry in this table. (That is, all pins whose name does not appear in the MTP Pin column.)

- vout: The DC power supply voltage in V
- ilimit: The connect current limit in mA
- offcurr: The off current state of the pin

Supported states are:

  - min: Minimum current for high impedance
  - act: Actual current for low impedance
  - open: High impedance and open output relay

See `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`） for more information on these states.

- vih: The Vih voltage in V
- vil: The Vil voltage in V
- voh: The Voh voltage in V
- vol: The Vol voltage in V
- Notes: This column allows both you and STPM MCM to add remarks about the level. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

### Syntax（取自子主题 MTPT configuration file）

The internal structure of the MTPT configuration file is private and subject to change without notice.

<!-- 语法节 end -->

## 是什么

**MTPT 不是程序，是一组 CSV 文件。**

> 「An MTPT contains a number of CSV tables that specify **various aspects of how STPs
> (source test programs) are combined into an MTP (master test program)**.」

一句话概括它的角色：**多个 STP 拼成一个 MTP 时，谁对应谁、各自的设置是什么，全写在这些 CSV 里。**

> ⚠️ **先把缩写钉住，这里有个陷阱。**
> 本页的 **MTP = `master test program`**（主测试程序）。
> 本 wiki 另一批页（[[mtp-shared-test-commands]]、[[mtp-maintenance-operations]]
> 里那些 `MTP 3.1.5` 之类的版本号）里的
> **MTP = `Memory Test Plus`**（一个独立产品，`02.12_Memory_Test_Plus_7.10.2`）。
> **同一个三字母缩写，在这份语料里是两个完全不同的东西。**
> 判据很简单：**看版本号**——`SmarTest 7.x` 这边是 master test program；
> **`MTP 3.x`** 那边是 Memory Test Plus。

### 十四张表，原文自己分了三组

| 组 | 原文的说法 | 表 |
|---|---|---|
| **① 描述用了哪些 STP** | `describes the STPs used in creating the MTP` | **STP table** |
| **② 映射：STP 的对象 ↔ MTP 的对象** | `describe which objects from the STPs correspond to which objects from the MTP` | Pin / Group / Test / Bin / Test number / Testflow variable **mapping table**（**6 张**） |
| **③ MTP 里各对象的设置与参数** | `describe settings and parameters for the objects in the MTP` | Test suite / Special tests / Shared pins / Test flag / Off DC levels table（**5 张**） |

**1 + 6 + 5 = 12。** 另外两张不走上面三组，原文单列：

> 「Two additional tables, the **MTPT configuration file** and the **STP test information table**,
> are intended for **internal bookkeeping** and **future expansion**, respectively,
> and **should not be edited**.」

**这两张一个字都别改**——一句 `should not be edited` 管着它们。
其中 **MTPT configuration file** 的语法节里原文又补了一句更重的话：

> `The internal structure of the MTPT configuration file is private and subject to change
> without notice.`

**12 + 2 = 14 张表**，与原文 `#### Subtopics` 的 15 条差一条——
**差的那条是 `OpenOffice spreadsheet for editing the CSV files`，是编辑工具，不是表。**

### 怎么改：推荐用表格软件，不是文本编辑器

> 「While the tables listed above **tables** can be edited with **text editors**, we
> **recommend** using the **OpenOffice spreadsheet** that is also part of the MTPT
> for editing the CSV files.」

**注意口气是 `recommend`，不是 `must`**——原文承认文本编辑器能改。
**本页照原文的强度写，没有把它升格成禁止。**

> ⚠️ **引文里那个重复的 `tables`（`the tables listed above tables`）是原文就有的，不是本页打重了。**
> 它属于第七类检查抓出来的：本页初版**漏抄了第二个 `tables`**，
> 却仍把这一段标成逐字——**那等于把转述冒充成引文。**
> **处置：补回原文形态，并在这里记下这处语料瑕疵**——
> 按本 wiki 的分工，**语料本身的毛病归「记录」，不归「修」**（raw 一个字节都不动）。
> **这一篇共 55 行，本页逐行看过，只有这一处重复词**（核对方法见「出处」）。

## 典型用法

**1. 什么时候翻这一页**：要**把多个 STP 合成一个 MTP**、或要知道**某个 CSV 是干什么的**时。
它是**索引页**——每张表的字段在本页上面的语法节里（脚本从各子主题逐字抽的），
**本页散文部分讲的是「有哪些表、怎么分组、哪张不能动」**。

**2. 想动 MTPT 时的次序**（本页给的读法）：
先分清楚**你要改的那张表属于三组里的哪一组**——
**改「映射」和改「设置」是两回事**；然后确认**它不是那两张禁改的表之一**。

**3. 一条硬边界**：**MTPT configuration file 的内部结构是私有的、可能不通知就变**
（原文那句 `private and subject to change without notice`）。
**解析它、依赖它的字段，等于依赖一个明确声明过会变的东西。**

**4. 15 个子主题本页一篇都没读**——每张表的字段含义**只在上面语法节里**
（那是脚本抽的子主题语法段）。**要判断某张表某个字段怎么填，请回 raw 读那一篇。**

## 和谁有关

- [[preprocessing-and-postprocessing-scripts]] — 同属
  `02.09_Test_Program_Management`，同批建页；STPM 是造 MTP 的那套工具
- [[gpib-lan-communication-conventions]] — 同上，同一章
- [[mtp-shared-test-commands]]、[[mtp-maintenance-operations]] — **⚠️ 见上**
  「MTP 这个缩写有两个意思」——**那两页的 MTP 不是本页的 MTP**
- [[stpm-control-file ]] — STPM 侧的控制文件；本页是它的产物之一
- [[project]]、`layer: file` — 本页 `stage: project` / `layer: file` 的理由：
  它是**一堆配置文件**，不落在九个工艺阶段上，也不是某段代码

## 版本

- **Introduced in SmarTest 7.1.4**

## 出处

`sources:` 一篇：
`02_System_reference/02.09_Test_Program_Management/02.09.03.04_MTPT__STPM_MCM_mapping_tables.md`

**本页没做的**：

- **15 个子主题一篇都没读**。所以：
  **每张表有哪些列、每列什么含义、必填还是可选，本页一个字都没有**——
  那些内容**以「取自子主题」的形式进了上面的语法节**（脚本抽的），
  **本页散文部分没有对它们做任何总结**。
- **`OpenOffice spreadsheet` 那篇没读**（编辑工具的用法）。
- **`Related information`：本篇没有这一节。** 全文 **28 条链接，去重后只有 15 个目标**，
  **和 `#### Subtopics` 那 15 条完全同一批**（每张表被链两次：目录一次、正文分组里一次），
  **没有一条指向外面**。**它是个「表目录」，位置决定它是叶子。**
- **`MCM` 是什么，原文从头到尾没有展开。** 标题写的是 `STPM MCM mapping tables`，
  正文只说 STP 和 MTP。**本页不猜 MCM 的全称。**
- **`STP` / `MTP` 这两个词本身本页只用了原文的括注**
  （`STPs (source test programs)` / `MTP (master test program)`），
  **没有替它们补别的解释**。

> ⚠️ **语料瑕疵两处，本页照实记下、没有替它改**（raw 一个字节都不动）：
>
> ① **第 51 行有一处重复词**：`While the tables listed above tables can be edited…`
> —— `tables` 连着写了两次。**本页上面那段引文照抄了这个重复**（见「怎么改」那节末尾）。
> ② **第 32 行主谓不一致**：`Several mapping table describe which objects…`
> —— `several` 后面应是复数，`table` **缺一个 `s`**，而动词 `describe` **用的却是复数形态**。
> **同一句里两处对不上，本页也没替它统一。**
>
> **核对方法**：这一篇只有 **55 行**，本页**逐行读过**，
> 重复词与主谓不一致**各只有上面这一处**。
> 正文里凡是引用原文的地方，引文形态**一律照原文**。

`verified: doc-only`
