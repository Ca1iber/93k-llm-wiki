---
type: object
title: Concepts of vector setup
layer: file
stage: pattern
tags: [pattern, file-format, vector-setup-file, pattern-master-file, binl, label]
related: [pattern, pattern-master-file, test-program-explorer, device-directory, command-reference, mapping-pattern]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01_Concepts_of_vector_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Concepts of vector setup

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **13,666 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.07.01_Concepts_of_vector_setup.md>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.07.01.01.01_The_label_definition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.01.02_The_vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.02_Label_definition__sequencer_program__and_sequencer_area.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.03_Sequencer_areas_and_vector_areas.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.04_Addressing_the_vector_areas.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.07.03.01_Inserting_a_sequencer_instruction.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.07.03.02_Deleting_a_sequencer_instruction.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.07.04_Executing_a_label.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.01_Vector_generating_instructions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.02_Address_instructions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.03.01_Changing_the_timing_set__CTIM.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.01_Endless_loops.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.02_Counted_loops.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.02_SVEC_subroutines.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.09.01_Data_transfer_from_the_vector_area_to_the_data_queue.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.10.01_Synchronization_within_sequencing_groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.10.02_De-coupling_ports_by_separate_sequencing_groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.10.03_Phase_synchronization_across_sequencing_groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.10.04_Defining_sequencing_groups.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 The structure of labels › The label definition）

The following instances of the SQLB command define the labels which provide the standard example for the explanation of the vector setup:

```
SQLB "test_1",MAIN,4,8,"table1"
SQLB "test_2",MAIN,9,12,"table1"
```

Both labels are associated with the default port, that is, they can be executed independently (with FTST?); both are of type MAIN, and both have table1 as their base wavetable.

### Example（取自子主题 The structure of labels › The vectors）

The following figure shows the left upper corner of the index array for the label test_1 of the standard example:

 !`Array of physical waveform DC/DC power units`（raw: `../../../../raw/10526.png`）

The vector numbers in the first column count the parallel vectors. They are logical vector numbers (for details see `Addressing the vector areas`（raw: `02.06.07.01.04_Addressing_the_vector_areas.md`）).

### Example（取自子主题 Label definition  sequencer program  and sequencer area）

The following figure shows the label definitions of the standard example and the corresponding sections of the sequencer area for the default port @:

 !`Label Definitions and Sequencer Area`（raw: `../../../../raw/120222.png`）

Since the default port contains all configured pins, the sequencer area on the right side of this figure is stored in the memory of all pins.

### Example（取自子主题 Sequencer areas and vector areas）

The following figure illustrates the case where one pin belongs to more than one port:

 !`Vector areas for pin belonging to two ports`（raw: `../../../../raw/114615.png`）

Observe the following points in this figure:

- port1 comprises the pins Pin1 and Pin2, while port2 only contains Pin2.
- The arrows indicate which vector area segments belong to which labels. Pin2 has two vector areas, one for the labels of port1 and one for the labels of port2.
- The numbers above the arrow heads are the start addresses of the vector area segments for the respective label (as defined by STVA).
- The association of the vector generating instructions to vector area sub-segments is exemplified by Pin1 and Test 1.

### Example（取自子主题 Addressing the vector areas）

The following figure displays the relations between the sequencer program and the vector areas of the standard example, and also illustrates the various concepts introduced to describe the structure of these areas:

 !`Vector areas`（raw: `../../../../raw/120207.png`）

The left side of the figure shows a section of the sequencer area for the default port @. It contains the sequencer programs for two labels (command line 4 through 8 and line 9 through 12). The right side displays the associated segments of the vector areas for the pins IN1 and OUT1.

Notice the following points in the figure:

- An instance of the sequencer area for @ is contained in the memory of both pin IN1 and pin OUT1.
- Each of the rows on the right side represents one memory word.
- Every cell of a row represents 8 bits. Every active vector contains one physical waveform index (which is displayed in hexadecimal notation).
- The padding (inactive) vectors are left blank in the figure.
- The numbers to the left of the memory words specify the absolute start addresses of the words within the vector areas.
- The numbers above the memory words are the logical vector numbers.
- The first label contains two sequencer constructs:

  - The first construct consists of the RPTV instruction and the single words starting at address 408 in the vector areas of both pins. Only the first 7 data cells of this block contain waveform DC/DC power units.
  - The second construct consists of the GENV instruction and the two words starting at addresses 416 and 424. The last 7 cells of the second word contain no user data.

The second label contains one sequencer construct (framed by a dotted line), which comprises two words.

### Syntax（取自子主题 The pattern master file）

The syntax of the pattern master file is as follows:

hp93000,pattern_master_file,0.1

[path:

 [<relative_or_absolute_path_1 >]]

files:

 <file_name_1_1>

 <file_name_1_2>

 ...

 <file_name_1_m>

[[path:

 [<relative_or_absolute_path_2>]]

files:

 <file_name_2_1>

 <file_name_2_2>

 ...

 <file_name_2_n>

...]

The default for the path is the vectorssubdirectory of the current device. But if you specify a path, note that the reference directory for relative paths is the waste subdirectory of the device. Therefore, if your pattern files are in the subdirectory sample of the vectors directory, you must specify the relative path to this directory as ./vectors/sample.

You can add comments to a pattern master file after "-- " (2 times the minus sign followed by a space) at the beginning of a line.

### Example（取自子主题 The pattern master file）

Both the usage of relative paths and the insertion of comments are illustrated by the following example file:

```

hp93000,pattern_master_file,0.1

-- The following file must reside in <device>/vectors:
files:
   sample1.binl

-- The following path points to <device>/vectors/pmfl_test:
path: ../vectors/pmfl_test

files:
  sample2.binl.gz
  sample3.binl.gz
```

### Example (general case)（取自子主题 Editing and executing labels at firmware level › Inserting and Deleting Sequencer Instructions › Inserting a sequencer instruction）

For example, you can insert a CTIM instruction (see `Changing the Timing Set`（raw: `02.06.07.01.08.03.01_Changing_the_timing_set__CTIM.md`）) between command lines 6 and 7 in the figure in `Addressing the vector areas`（raw: `02.06.07.01.04_Addressing_the_vector_areas.md`） as follows:

- `TSTL "test_1",`
- INSI 7,1
- SQPG 7,CTIM,2,,,(@)

### Example (vector generating instructions)（取自子主题 Editing and executing labels at firmware level › Inserting and Deleting Sequencer Instructions › Inserting a sequencer instruction）

The insertion of a GENV instruction and of an RPTV instruction are slightly different.

### Example (general case)（取自子主题 Editing and executing labels at firmware level › Inserting and Deleting Sequencer Instructions › Deleting a sequencer instruction）

For example, you can remove the CTIM instruction which was introduced in the general case example of `Inserting a sequencer instruction`（raw: `02.06.07.01.07.03.01_Inserting_a_sequencer_instruction.md`） from the first label of the standard example as follows:

- TSTL "test_1",
- DELI 7,1

### Example (vector generating instructions)（取自子主题 Editing and executing labels at firmware level › Inserting and Deleting Sequencer Instructions › Deleting a sequencer instruction）

If you want to remove again the initial GENV instruction that was added to the program of `test_1` in the figure of `Inserting a sequencer instruction`（raw: `02.06.07.01.07.03.01_Inserting_a_sequencer_instruction.md`）, proceed as follows:

- TSTL "test_1",
- DELV 6,10
- DELI 6,1

### Example（取自子主题 Editing and executing labels at firmware level › Executing a label）

In order to execute the label `test_2` of the standard example with the timing defined in the `Timing Setup Commands`（raw: `02.06.06_Timing_Setup_Commands.md`） chapter, proceed as follows:

- SQSL "test_2"
- SPRM 101,1,101002,101003
- FTST?

### Example（取自子主题 Using sequencer instructions › Vector generating instructions）

Two examples of vector generating instructions are:

```
SQPG 7,GENV,9,,,(@)
```

This GENV instruction generates 9 vectors.

```
SQPG 6,RPTV,6,5,,(@)
```

This RPTV instruction generates 6 vectors 5 times in a row.

### Example（取自子主题 Using sequencer instructions › Address instructions）

If the vector setup contains only patterns for the default port, the reply of an SQPG? query looks as follows:

```
> SQPG? "test",(@)
< SQPG 5,STVA,112,,,(@)
< SQPG 6,STSA,,,,(@)
< SQPG 7,GENV,9,,,(@)
< SQPG 8,STOP,,,,(@)
```

The STVA address is returned as param_1. However, after you have added a pattern for a user defined port to the setup, it will be returned as param_2:

```
> SQPG? "test",(@)
< SQPG 5,STVA,,112,,(@)
< SQPG 6,STSA,,,,(@)
< SQPG 7,GENV,9,,,(@)
< SQPG 8,STOP,,,,(@)
```

### Example（取自子主题 Using sequencer instructions › Instructions for changing the setup › Changing the timing set  CTIM）

The example:

```
SQPG 0,STVA,0,,(@)
 ....
SQPG 4,CTIM,2,,(@)
SQPG 5,GENV,400,,(@)
SQPG 6,CTIM,1,,(@)
SQPG 7,GENV,200,,(@)
SQPG 8,STOP,,,(@)
```

changes the timing to set 2 at the start of the test before the device is initialized. At the end of vector 400 the timing is changed to set 1.

For binning tests, the CTIM instruction allows you to change to the primary timing set as shown in the following listing:

```
SQPG 0,STVA,0,,(@)
SQPG 1,STSA,,,(@)
 ....
SQPG 4,CTIM,2,,(@)
SQPG 5,GENV,400,,(@)
SQPG 6,CTIM,PRM,,(@)
SQPG 7,GENV,200,,(@)
SQPG 8,STOP,,,(@)
```

Each time you execute a functional test with this test sequence, the timing is changed to the primary timing set. If you use the `SPRM`（raw: `02.06.02.02.228_SPRM__SPRM__-__Set_PRiMary_sets.md`） command to change the primary set for each test run, you can repeat the test and vary the parameters without changing your setup.

### Example（取自子主题 Using sequencer instructions › Loops › Endless loops）

### Endless loop

```
SQPG 7,LBGN,,,,(@)
SQPG 8,GENV,7,,,(@)
SQPG 9,LEND,,,,(@)
```

The sequence repeats the `GENV`（raw: `02.06.07.01.07.03.01_Inserting_a_sequencer_instruction.md`） instruction in command line 8.

### Examples（取自子主题 Using sequencer instructions › Loops › Counted loops）

### Counted loop

```
SQPG 7,LBGN,50,,,(@)
SQPG 8,GENV,7,,,(@)
SQPG 9,LEND,,,,(@)
```

The sequence repeats the `GENV`（raw: `02.06.07.01.07.03.01_Inserting_a_sequencer_instruction.md`） instruction 50 times.

### Repeated subroutine

```
SQPG 0,STVA,408,,,(@)
SQPG 1,STSA,,,,(@)
SQPG 2,GENV,6,,,(@)
SQPG 3,RPTJ,10,,,(@)
SQPG 3,JSUB,,"sub",,(@)
SQPG 4,STOP,,,,(@)
```

In this example, the call of the subroutine `sub` is repeated ten times.

### Nested counted loop

```
SQPG 0,STVA,408,,,(@)
SQPG 1,STSA,,,,(@)
SQPG 3,LBGN,5,,,(@)
SQPG 4,GENV,7,,,(@)
SQPG 5,LBGN,9,,,(@)
SQPG 6,GENV,3,,,(@)
SQPG 7,LEND,,,,(@)
SQPG 8,LEND,,,,(@)
SQPG 9,STOP,,,,(@)
```

The outer loop is repeated five times and the inner loop nine times.

### Nested counted loop and subroutine

```
SQPG 0,STVA,408,,,(@)
SQPG 1,STSA,,,,(@)
SQPG 3,LBGN,5,,,(@)
SQPG 4,GENV,7,,,(@)
SQPG 5,LBGN,9,,,(@)
SQPG 6,JSUB,,"sub1",,(@)
SQPG 7,LEND,,,,(@)
SQPG 8,LEND,,,,(@)
SQPG 9,STOP,,,,(@)
```

### Nested repeated subroutine

```
SQPG 0,STVA,408,,,(@)
SQPG 1,STSA,,,,(@)
SQPG 3,LBGN,5,,,(@)
SQPG 4,GENV,7,,,(@)
SQPG 5,RPTJ,9,,,(@)
SQPG 6,JSUB,,"sub1",,(@)
SQPG 7,LEND,,,,(@)
SQPG 8,STOP,,,,(@)
```

### Example（取自子主题 Using sequencer instructions › Main programs and subroutines › SVEC subroutines）

The following listing shows a SVEC subroutine that is called from two MAIN labels:

```
SQPG 0,STVA,408,,,(@)
SQPG 1,STSA,,,,(@)
SQPG 2,GENV,6,,,(@)
SQPG 3,JSUB,,"sub",,(@)
SQPG 4,STOP,,,,(@)
SQPG 5,STVA,416,,,(@)
SQPG 6,STSA,,,,(@)
SQPG 7,GENV,4,,,(@)
SQPG 8,JSUB,,"sub",,(@)
SQPG 9,STOP,,,,(@)
SQPG 10,STVA,424,,,(@)
SQPG 11,GENV,400,,,(@)
SQPG 12,RSUB,,,,(@)
```

The definitions of the three labels are as follows:

```
SQLB "test1",MAIN,0,4,"table1"
SQLB "test2",MAIN,5,9,"table1"
SQLB "sub",SVEC,10,12,"table1"
```

### Example 1（取自子主题 Using sequencer instructions › Instructions for PRBS and SmartLoop tests）

The following is the sequencer program of a PRBS test.

```
> SQPG? "prbs_test",(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,BRKV,200,0,,(@)
< SQPG 3,LBGN,100,,,(@)
< SQPG 4,TMUA,,,,(@)
< SQPG 5,PRBS,2147483647,4095,,(@)
< SQPG 6,LEND,,,,(@)
< SQPG 7,STOP,,,,(@)
```

This example combines a PRBS test with a TMU per pin measurement. Note that the TMUA instruction is included in a loop. Note also that the first parameter of PRBS is set to its maximum value 231 - 1, and that the number of cycles is increased above this maximum by multiplication with the second parameter, which is also set to its maximum value 212 - 1.

### Example 2（取自子主题 Using sequencer instructions › Instructions for PRBS and SmartLoop tests）

```
> SQPG? "loopback_tmu",(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,LPBK,1000,1,,(@)
< SQPG 3,TMUA,,,,(@)
< SQPG 4,LPBK,500,1,,(@)
< SQPG 5,STOP,,,,(@)
```

This example combines a SmartLoop鈩?test with a TMU per pin measurement.

### Example（取自子主题 Managing the data queue › Data transfer from the vector area to the data queue）

The following figure illustrates the transfer process for one pin:

 !`Transferring waveform DC/DC power units into the data queue`（raw: `../../../../raw/120209.png`）

Note the following points in the figure:

- The example slightly deviates from the vector setup standard example.
- The flattened vector instances, not the stored vectors, must be a multiple of 8. The label has 16 active vectors, but is flattened to 22 instances. Therefore two break vector instances are required.

### Example（取自子主题 Synchronizing vectors in a multi-port setup › Synchronization within sequencing groups）

The following figure illustrates the algorithm by a sequencing group consisting of two ports:

 !`Synchronization After CTIM Within One Sequencing Group`（raw: `../../../../raw/104692.png`）

The variables j, k, m, n, are integers.

Observe that the synchronization is based on the simultaneous change to the new period within the CTOF sequence which is triggered by a CTIM instruction. Therefore, the user vectors can only be synchronized exactly at the start of a functional test if a timing set is activated before the first user vector. By default, this condition is satisfied for any sequencing group that contains more than one port (even if the primary sets are the same as before). But if this activation is suppressed with the FTCG firmware command (option ON), exact synchronization is not possible.

The following figure shows a "macroscopic" view of a multi-port burst for three ports that belong to the same sequencing group:

 !`Execution of CTIM commands within a sequencing group`（raw: `../../../../raw/104678.png`）

Observe that the user vectors start synchronously not only at the start of the testsuite, but also after the CTIM instruction that occurs in the sequencer programs of all three ports.

### Example（取自子主题 Synchronizing vectors in a multi-port setup › De-coupling ports by separate sequencing groups）

The following figure shows two testsuites for three ports belonging to two sequencing groups:

 !`Port Patterns in Different Sequencing Groups`（raw: `../../../../raw/54320.png`）

Observe the following points in the figure:

- The start of the user vectors in Sequencing Group 1 and Sequencing Group 2 is not simultaneous.
- In contrast to Port A, the two ports of sequencing group 2 contain an additional CTIM instruction in the first testsuite.
- Port A in Sequencing Group 1 waits for Port B and Port C in Sequencing Group 2 to finish their user vectors before the second testsuite starts.

### Example（取自子主题 Synchronizing vectors in a multi-port setup › Phase synchronization across sequencing groups）

The following figure shows phase synchronization after the internal CTIM at test start for the two ports of the figure in `Synchronization within sequencing groups`（raw: `02.06.07.01.10.01_Synchronization_within_sequencing_groups.md`）, which are now supposed to belong to different sequencing groups and to have the PHASE flag set:

 !`Phase Synchronization After Internal CTIM at Test Start`（raw: `../../../../raw/104693.png`）

j, k, m, n, x, y are integers.

Since the start of the user vectors of port A is delayed by a multiple of pB, and k 脳 pA + FA + m 脳 8 脳 pA is also a multiple of pB by

k 脳 pA + FA + m 脳 8 脳 pA = k 脳 pB + n 脳 8 脳 pB,

the first user vector of port A in the figure above is still synchronous with some user vector of port B.

### Example（取自子主题 Synchronizing vectors in a multi-port setup › Defining sequencing groups）

For sequencing group definitions within a multi-port specification, see the example in `Multi-port timing specifications`（raw: `02.06.06.01.05.03_Multiport_timing_specifications.md`）. The same grouping could be defined in the vector setup with the SQLB command as follows:

```
> SQLB "MP_B",MPBU,28,31,"gr1",(port1)
> SQLB "MP_B",MPBU,28,29,"gr2",(port2)
> SQLB "MP_B",MPBU,31,32,"gr2",(port3)
```

<!-- 语法节 end -->

## 是什么

**`vector-setup-file` 是「装 label（pattern）与向量数据的那个文件」。** 它在本 wiki 里是 `layer: file`、
`stage: pattern`——**`stage` 填的是「最近的一段」，不是归属**（§6）：**读者该去 pattern 那一段里找它的用法，
但这不等于它只被那一段用。**

**两篇 raw 里，直接命名这个对象的只有一句**（`02.06.07.01.05`，全文 84 行）：

> 「Vector data can be organized in two ways. You can either keep all the labels (patterns) in one big vector setup file, or you can store every pattern in a separate file and specify the subset of them that you want to work with in a pattern master file.」

**这一句就是本页的全部地基**：vector setup 文件有**两种形态**——「一个大文件装全部 label」与「一个 pattern 一个文件」；
后一种要配一个 `[[pattern-master-file]]` 来指定用哪些。**两种形态的区别只有下面这五条，全部出自同一篇。**

| 维度 | 一个大 vector setup 文件 | 一个 pattern 一个文件 + pattern master file |
|---|---|---|
| 装什么 | 全部 label（pattern）+ 向量数据 | 每个 pattern 一个文件；master file 只装**文件名与所在目录路径** |
| 能放哪 | **必须**在 `<device>/vectors` | pattern 文件**可以在文件系统里的任何地方** |
| 加载哪些 | 全部 | **只加载当前真正需要的那部分** |
| 保存 | **语料未写** | 改过 pattern 再存 master file，**只存改过的那些** |
| 代价 | **语料未写** | master file 引用的 pattern 很多时，**向量下载时间可能很长** |

**「代价」那一格原文给了补救办法，而且它顺手说明了两种形态可以互转**：

> 「A possible disadvantage of using a pattern master file is that the download time for the vectors can be rather long if the number of patterns referenced in the master file is very large.」

> 「In this case you can convert the vector setup into a big vector file by loading it and then saving it under another name in the Test Program Explorer.」

**注意这句话只给了转换方向（多文件 → 一个大文件）和动作（load + save as）、地点（Test Program Explorer），
却没有给那个「big vector file」的名字或扩展名**（**语料未写**，见下面第二小节）。

### pattern master file 的四条硬规矩

这四条都在 `02.06.07.01.05` 里明说，**是本页能给出的最硬的一组规则**：

1. **它装什么**：

> 「The pattern master file contains the names of the pattern files and also the directory path where they are located.」

2. **怎么建、放哪里**：

> 「The pattern master file must be created manually (or with the ASCII interface). The file itself must be located in the vectorssubdirectory of the current device.」

3. **注释怎么写**：

> 「You can add comments to a pattern master file after "-- " (2 times the minus sign followed by a space) at the beginning of a line.」

4. **格式骨架**：首行固定为 `hp93000,pattern_master_file,0.1`，之后 `path:` + `files:` 成对出现；
   `path:` 可省，整块可重复（原文用**双层方括号**表示「这一整块可选、且可以再来一遍」）。
   **逐字全文在上一节，本页不重抄。**

### `.binl` / `.binl.gz`：证据只到「例子里的文件名」这一级

**本 wiki 的 [[pattern]] 阶段页把本页记成 file 层、扩展名 `.binl` / `.binl.gz` 的载体。照 raw 核一遍，这个说法要收窄：**

- **有的**：`02.06.07.01.05` 的 `## Example` 里，pattern master file 的 `files:` 段下列出的文件名是
  `sample1.binl`、`sample2.binl.gz`、`sample3.binl.gz`（这段在同一篇的 Example 里，本页「语法 / 参数」节也抽了它）。
  **也就是说：被 master file 引用的那些 pattern 文件，在例子里长这样。**
- **没有的**：**两篇 raw 里没有一句说 pattern 文件的扩展名是 `.binl`**——正文只把它叫 `the pattern files`，
  语法段只把它叫 `<file_name_1_1>`。**两篇 raw 也没有说 `.gz` 是压缩**（那是本页的读法，不是文档的话）。
- **完全没有的**：**那个「一个大的 vector setup 文件」自己的扩展名。** 原文只说可以在 Test Program Explorer 里
  load + save as 得到 `a big vector file`，**没给名字**。

**所以本页的立场是：`.binl` / `.binl.gz` 是「master file 例子里列出的 pattern 文件名」这一级的证据，
不是「本页这个文件（大 vector setup 文件）的扩展名」的证据。** 这一条不是抠字眼——
**两种形态的文件名不同、位置规则也不同（见上表），把它们混成一种会直接读错「文件该放哪」。**

### ④ 图证：图钉死了什么、钉不死什么

**④ 图证 = 从 raw 自带的图里读出来的**（`schema.md` §11.4 / §2.5 第四档）。**它比①②③都硬**
（图是文档自带的，不是本页的推断），**但它有一个别档都没有的毛病：不可检索**——
**图里的字拿回 raw 文本里 grep 是 0 命中**（本节下面每一条都举了例子），要核只能自己再去开那张图。
**本页读了 12 张**：语法节引到的 9 张，**加上语法节源文档里引到、语法节却没抄进来的两张**
（`120208.png`、`10557.png`），**再加 `96892.png`**——它出自 `02.06.07.01.01`，
而它的两个子篇 `.01.01.01` / `.01.01.02` 都在语法节源列表里。
**下面四条，每条都写清是哪张图。**

**（一）「vector area 的内存字怎么排」——图钉死了；本页原先说这一条「只由文字推」，那句话作废。**
`120207.png`（出自语法节源文档 `02.06.07.01.04_Addressing_the_vector_areas.md` 的 `## Example`）
左边是 default port `@` 的 sequencer area 片段（`SQPG 4,STVA,408,,,(@)` 一路到 `SQPG 12,STOP,,,(@)`），
右边是 `Pin IN1` 与 `Pin OUT1` 两个 vector area。**图里直接看得见的（④ 图证，都 grep 不到）：**

- **一行 = 一个 memory word，一行 8 格**；行**左侧**的数字是绝对地址（图里是 `408` / `416` / `424` / `432` / `440`），
  行**上方**的数字是 logical vector number（图里是 `0`–`7`、`8`–`15`）。
- 格子分两色，图底下那个 **`Memory word` 放大块**给了图例：黄格 = `Active vectors (waveform indices)`，
  蓝格 = `Padding vectors`。**本页语法节那段文字说的「padding 留白」「绝对地址在左」「logical vector number 在上」，
  在图上就是这三种画法。**
- 格里的值是 `1 3 4 5 7 5 9`、`b a a b a a b a`、`5 6 5 8`——**`a` / `b` 只有按十六进制读才是数**，
  所以图**独立支持了语法节那句「displayed in hexadecimal notation」**（那句话本身也是 raw 文本，可 grep）。
- `120209.png` 里有一块**同款 `Memory word` 放大块**（出自 `02.06.07.01.09.01`），画法一致。

**（二）图把术语钉死了：那个东西图上叫 `waveform indices`，不叫别的话。**（**这一条直接收掉 ⚠️⑤**）
**五张**图在讲同一件事时写的是 `waveform indices`：`10526.png` 的表头 `Vector number` / `Waveform indices for pins`；
`96892.png` 右侧的括号标注 `Waveform indices`；`120207.png` 与 `120209.png` 的图例
`Active vectors (waveform indices)`；`120222.png` 的注释
`Base wavetable for translating waveform indices into device cycles (state characters) and vice versa`。
**`waveform indices` 这个复数形式在 raw 文本里 0 篇命中**——**图上的字就是搜不到**，
这就是④这一档要单独标出来的理由。**具体推论见 ⚠️⑤。**

**（三）本页的主题——两种文件形态——图一张都没画。这一条比上面两条更该说清。**
本页讲的是「一个大 vector setup 文件」与「一个 pattern 一个文件 + pattern master file」。
**这 12 张图里没有任何一张画文件、文件名、扩展名、目录树或路径**：它们画的**全是内存里的东西**
（sequencer area、vector area、sequencer construct、data queue、多端口时序、CTOF 序列）。
**pattern master file 自己的那一篇（`02.06.07.01.05`）一张图都没有。** 所以：

- 「大 vector 文件叫什么名字」「`.gz` 是不是压缩」「`waste` 目录真不真」「`./vectors/sample` 与
  `../vectors/pmfl_test` 哪个对」——**图一张都答不了**。**这四条仍是文本的事**：
  前两条在「是什么」里标着「语料未写」，后两条见 ⚠️①②。
- 「`vectors` 在设备目录结构里的位置」——**图里没有设备目录树**，也答不了。
- **这一节不是「图把本页补全了」**：图只补上了**内存侧**；**本页的主题（文件侧）仍然一个字都没被图证过。**

**（四）图还顺手露了一处文本与图对不上。** 见 ⚠️⑥。

### 这一页的边界：定义文档本身是空的

**本页的 raw 定义文档 `02.06.07.01_Concepts_of_vector_setup.md` 全文只有 19 行（1,160 字节）：
一个标题、一个 `#### Subtopics` 标题、10 条子主题链接——正文一个字都没有。**

**所以「Concepts of vector setup」不是一篇讲概念的文章，是一个入口节点**：它的内容就是那 10 篇子主题
（label 的结构、sequencer program 与 sequencer area、vector area 与它的寻址、pattern master file、固件命令总览、
在固件层编辑与执行 label、sequencer 指令、data queue、多端口 setup 里的向量同步）。

**后果两条，用之前必须知道：**

- **上一节「语法 / 参数」的 13,666 字符，每一段都带「取自子主题」后缀，没有一段来自定义文档自己**——
  脚本在节首自己声明了这件事。**本页的语法节不是空的**（它有 21 篇子主题可抽）；
  对照另一类页：**定义文档和它的子主题都没有 `Syntax` / `Parameters` / `Example` 段标记时，脚本一个字都不收**——
  **那是脚本的正确行为，不是「这个对象没有参数」**。本页属于「有内容」的那一类。
- **本页（wiki）只写 `sources:` 那两篇里有的。** 那 10 篇子主题的正文**建页时一篇没读**
  （**2026-09-20 为核图读了其中 2 篇**，见「出处」），
  所以**「label 是什么、sequencer area 怎么排、`STVA` / `SQPG` 的参数什么含义」在本页正文里一个字都没有**
  ——**上面「④ 图证」补的是「vector area 的内存字怎么排」，不是这三件**；
  语法节里那些例子是脚本抄的，不是本页说的（见「出处」）。

## 典型用法

**先记一条事实：这篇文档没有 `## Procedure`，也没有 `## Before you begin`**——`02.06.07.01.05` 只有
`## Syntax` / `## Example` / `## Functional changes` 三节。**所以下面这几步的先后顺序是本页按原文散句排的，
不是原文给的流程**（原文没有流程）。

**1. 先选形态**，判据原文只给了一条，而且是**位置**：

| 你要的 | 选哪种 | 依据（原文） |
|---|---|---|
| pattern 放在**文件系统任意位置** | pattern master file | 大 vector setup 文件**必须**在 `<device>/vectors`；用 master file 就不受这条约束 |
| 只做当前项目要用的那部分 | pattern master file | 只加载需要的那些 |
| 改过几个 pattern 后想快点存 | pattern master file | 只存改过的那些 |
| 引用的 pattern 太多、**下载太慢** | 转成一个**大 vector 文件** | load + save as，在 Test Program Explorer 里做 |

**2. 建 master file：手工写**（或走 ASCII 接口）。原文的措辞是 `must be created manually`——
**两篇 raw 里没有出现任何「用工具生成 master file」的说法**（这就是这两篇能说的全部）。

**3. 文件本身放进 `<device>/vectors`**（原文：`The file itself must be located in the vectorssubdirectory of the current device.`）。

**4. 写内容**：首行 `hp93000,pattern_master_file,0.1` → `path:`（可省）+ `files:`（一行一个文件名）→
需要分组的再写一组 `path:` + `files:`。**注释写在行首 `-- `（两个减号 + 一个空格）之后。**

**5. 相对路径的参考目录——原文这里自己矛盾，两句都照录，本页不替它调和**：

> 「The default for the path is the vectorssubdirectory of the current device. But if you specify a path, note that the reference directory for relative paths is the waste subdirectory of the device. Therefore, if your pattern files are in the subdirectory sample of the vectors directory, you must specify the relative path to this directory as ./vectors/sample.」

**按这句话，`<device>/vectors/sample` 要写成 `./vectors/sample`。但同一篇的 `## Example` 里写的是另一回事**：

> 「path: ../vectors/pmfl_test」

**而它上面的注释说这条路径指向 `<device>/vectors/pmfl_test`。** 两个写法只能有一个对：
`./vectors/sample` 要求参考目录是 `<device>`，`../vectors/pmfl_test` 要求参考目录是 `<device>/waste`。
**原文两句并列，本页不选哪个是真**（详见「出处」的 ⚠️ ②）。**动手时以你机器上实际能解析的结果为准。**（建议）

**6. 之后每次改完 pattern 存 master file**：**只有改过的 pattern 会被写**（这是原文给的两条好处之一）。

## 和谁有关

- [[pattern]] — **本页 `stage: pattern` 的那个阶段页**。关系是**上位**：本页是那一段的产物文件之一。
  **本页被那页记成 `vector-setup-file`（file，`.binl` / `.binl.gz`）**——那个说法要收窄，见「是什么」最后一节。
- [[pattern-master-file]] — **同一篇 raw（`02.06.07.01.05`）里的另一半，是本页的「配套文件」，不是同类**：
  本页装 **label 与向量数据**，master file 只装 **pattern 文件的名字与路径**。
  **一个是大文件（可含全部 label），一个是索引**；选了「一个 pattern 一个文件」这条路，两者才同时存在。
  注意 **本页「语法 / 参数」节里也有一块 PMF 的 Syntax / Example**——`.05` 是定义文档的子主题，
  脚本按子树抽；**PMF 的正文归那一页，本页不重复**。
- [[test-program-explorer]] — **两篇 raw 里唯一被点名的 GUI**：把多文件 setup 转成一个大 vector 文件的
  load + save as 在这里做。**这也是本页唯一一条 GUI 关系。**
- `pattern-explorer` / `pattern-editor` — **两篇 raw 里一次都没出现**，所以**本页不写它们和本页的关系**：
  **不是漏了，是没有出处**。（§9.1：没有证据的关系不写链接——那两个名字在本页只以反引号出现。）
- [[device-directory]] — **目录前提（上游）**：`<device>/vectors`。**两种文件都必须落在这里**：
  大 vector setup 文件由 `You can store the patterns anywhere in your file system (…)` 那句的括号里说明，
  master file 由 `The file itself must be located in the vectorssubdirectory of the current device.` 说明。
  **那一页本页没读**——`vectors` 在设备目录结构里的位置，本页不知道。
- [[command-reference]] — **出处归属**：本页的 raw 定义文档就在 `02.06 Command Reference` 这一章下
  （raw 路径即证据）。**那一页本页没读。**
- [[mapping-pattern]] — **同阶段的对照表页**，把本页列入 pattern 那一段的「文件」层载体。
  **它的表里没有把 `.binl` 写在本页头上**；`.binl` 那句在 [[pattern]] 里（见「是什么」最后一节）。

**还有一层关系要点名否掉**：本页**不是** `label` / `sequencer program` 的定义页——那两个东西的正文在
`02.06.07.01.01` 与 `02.06.07.01.02` 里，**本页没读**，它们只是**在语法节里顺带被脚本抽进来过**。
**别把本页当 label 的入门页用。**

## 版本

**`02.06.07.01.05` 有 `## Functional changes` 段，全文只有一条**：

> 「- Introduced before SmarTest 6.3.2」

**这一条不是「6.3.2 新增」。** §11.2 ② 把这种写法定成**哨兵值**：`before` 的意思是
「**在这批文档集覆盖范围开始之前就已经有了**」。**照字面读会读出「SmarTest 6.3.2 引入了 vector setup」这条假信息**，
而且格式齐整、很容易抄进别处。**本页照录、不换算。**

**`02.06.07.01_Concepts_of_vector_setup.md` 没有 `## Functional changes` 段**（全文只有标题 + `#### Subtopics`）。
**这是事实，不是缺陷**：它自己没有内容，也就没有自己的变更记录——**要查 vector setup 的版本沿革，得去那 10 篇子主题里查，本页查不到。**

## 出处

`sources:` 两篇，**都整篇读完**：

| raw（前缀 `F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category\`） | TDC | 规模 |
|---|---|---|
| `02_System_reference/02.06_Command_Reference/02.06.07.01_Concepts_of_vector_setup.md` | `104700.htm` | 1,160 字节 / 19 行 |
| `02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md` | `58905.htm` | 2,837 字节 / 84 行 |

**「语法 / 参数」这一节不是本页写的。** 脚本抽了 **13,666 字符**，来源是**定义文档 + 21 篇子主题**；
**那 21 篇里，建页时只读了 `02.06.07.01.05`（它是 `sources:` 之一），另外 20 篇一篇没读**；
**2026-09-20 为核图另读了 4 篇的正文**（`02.06.07.01.01`、`02.06.07.01.01.02`、`02.06.07.01.04`、
`02.06.07.01.10.03`）**和其余带图篇的「图那一行」**——详见下面「本页没做的」第二条。
因为定义文档自己没有完整语法段，**语法节里每一段都带「取自子主题」后缀**——
**这不是缺内容，是脚本按 §4 认段标记抽的结果**；脚本在节首也说明了**段内的语料内部相对链接被改写成 `文本`（raw: `路径`）**，
所以段名里 `Label definition  sequencer program  and sequencer area` 那种**双空格是脚本改写留下的，不是语料的字**。
**「空 ≠ 没有参数」也要说一句**：本页的语法节非空；**脚本只在「定义文档与子主题都没有 `Syntax` / `Parameters` / `Example`
段标记」时才一个字都不收**——那同样是脚本的正确行为，不能读成「这个对象没有参数」。

**本页没做的**：

- **10 篇直接子主题（`02.06.07.01.01` 到 `02.06.07.01.10`）建页时一篇没读；为核图另读了其中 2 篇**
  （`02.06.07.01.01_The_structure_of_labels`、`02.06.07.01.04_Addressing_the_vector_areas`）——
  **剩下 8 篇一篇没读**（label 定义/sequencer program/sequencer area、sequencer area 与 vector area、
  固件命令总览、在固件层编辑与执行 label、sequencer 指令的用法、data queue、多端口 setup 下的向量同步）。
  **「vector setup 的概念」的正文在那 10 篇里，本页只碰到其中 2 篇的边。**
- **语法节其余子主题的原文：只读了 4 篇的正文，其余只读了「图那一行」**（2026-09-20 补）。
  读全的是 `02.06.07.01.01`、`02.06.07.01.01.02_The_vectors`、`02.06.07.01.04`、`02.06.07.01.10.03`；
  其余带图的子主题（`02.06.07.01.02`、`.03`、`.07.03.01`、`.08.03.01`、`.09.01`、`.10.01`、`.10.02` 等）
  **只读了它 `![…](<../../../../raw/…>)` 那一行**，为的是确认每张图归哪一篇。
  **所以语法节里的英文句子，绝大部分仍然是脚本抄的、本页没有回原文核过**——
  ⚠️③④ 记的仍是这种「只在本页上看见」的东西；**⚠️⑤ 是例外，它现在有两条新证据（同篇自证 + ④ 图证）。**
- **图：这 9 张一张没看，是建页时的事实；但原句给的那个理由是错的，已删（2026-09-20 更正）。**
  语法节里引到的 9 张是 `raw/10526.png`、`raw/120222.png`、`raw/114615.png`、`raw/120207.png`、
  `raw/120209.png`、`raw/104692.png`、`raw/104678.png`、`raw/54320.png`、`raw/104693.png`。
  **上一版在这里写着「路径向上爬四层（`../../../../raw/`）、在语料树之外」，并由此写下「本页没有任何来自图的结论」。**
  **那句话是错的**（它是一句可算的路径断言，而算出来的结果正相反）：md 在 `tdc-html/agent-markdown/by-category/<分类>/x.md`，
  **往上四层正好是 `tdc-html/`**，所以 `../../../../raw/x.png` 解析到 `tdc-html/raw/x.png`——
  **路径是对的、文件就在那儿**（`schema.md` §11.4 更正）。**真正的原因只有一个：建这页时没去开那些图。**
  **现在读了 12 张**：上面 9 张，加语法节源文档里引到、语法节没抄进来的 **`120208.png`**
  （`02.06.07.01.07.03.01` 的 `## Example`，而语法节那段 `Deleting a sequencer instruction` 的英文
  **正指着「the figure of Inserting a sequencer instruction」说话**）与 **`10557.png`**（`02.06.07.01.08.03.01`），
  加 **`96892.png`**（`02.06.07.01.01`，它的两个子篇都在语法节源列表里）。
  **图证写在「是什么」的「④ 图证」一节**：**图补的是内存侧**（vector area 的内存字怎么排、那个东西图上叫 `waveform indices`），
  **本页的主题——两种文件形态——12 张图一张都没画**。**「一个 vector setup 文件长什么样」仍然只由文字推。**
- **没有实跑**：没有在任何机台上建过 vector setup 文件或 pattern master file，没有用 Test Program Explorer 做过
  load + save as，也没有验证过 `./vectors/sample` 与 `../vectors/pmfl_test` 到底哪个能被解析。
  **那一条在「典型用法」里只能并列摆着，就是因为没有实测。** `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**（本页还没进索引；按分工归主会话），也**没动别的页**。
- **`SQLB` / `SQPG` / `STVA` 这些命令的原文一篇没核**：它们在本页只出现在语法节（子主题的 Example）里，
  **本页没有去 `02.06.07.02.*` 的命令页复核**。

> **⚠️ 语料瑕疵，照实记下、一处都没替它改（§11.2）。**

**① 同一篇里 `vectors` 子目录有两种写法（有空格 1 次，没空格 2 次）。** 上文写有空格的那种：

> 「You can store the patterns anywhere in your file system (whereas the big vector setup file must be located in the vectors subdirectory of your current device).」

下文写没空格的那种，两次，其中一次是：

> 「The pattern master file must be created manually (or with the ASCII interface). The file itself must be located in the vectorssubdirectory of the current device.」

**② `waste` 子目录：原文自己的两句话不互容。** 两句都逐字引在「典型用法」第 5 步，这里只说结论：
- 「参考目录是设备的 `waste` 子目录」+「`<device>/vectors/sample` 要写成 `./vectors/sample`」——
  **这两句只有参考目录是 `<device>` 时才同时成立**（`./vectors/sample` 相对 `<device>` 才是 `<device>/vectors/sample`）；
- 而 `## Example` 的 `path: ../vectors/pmfl_test` 要落到 `<device>/vectors/pmfl_test`（它上面的注释这么写的），
  **只有参考目录是 `<device>/waste` 时才成立**。
- **`waste` 是纯 ASCII 词，不属于 §11.2 那两类编码坏字**（那两类吃的是非 ASCII 字符，ASCII 词不受影响），
  **所以不能当坏字处理、也不能当坏字搜**；**它是不是一个真实存在的目录名，两篇 raw 都没说**（语料未写）。
  **本页照录、不判、不调和**（§10 第 2/3 步）。

**③ 编码坏字，都在语法节里。**（建页时没直读那些子主题，坏字是看本页语法节本身记下的；
**2026-09-20 补**：`脳` 那一篇 `02.06.07.01.10.03` 为核图读过了，**raw 里原样就是 9 处 `脳`**；
`鈩?` 仍在 `02.06.07.01.08.06` 的 raw 里、**那一篇本页没读**。）引文里原样留着坏字：
- `k 脳 pA + FA + m 脳 8 脳 pA`（`### Example（取自子主题 Synchronizing vectors in a multi-port setup › Phase synchronization across sequencing groups）` 里，
  两行公式共 **9 处** `脳`）——**`脳` 应为 `×`**（乘号；`extract/encoding-map.csv`：`脳` → `×`）。
- `SmartLoop鈩?test`（`### Example 2（取自子主题 Using sequencer instructions › Instructions for PRBS and SmartLoop tests）` 里）——
  **`鈩?` 是坏字**：对照表把 `鈩` 归进「**第三字节已丢、只能给区间**」那一类（原字符在 **U+2100–U+213F** 之间），
  **不能唯一反解**；上下文里读作 **™** 才通（**推断**：`SmartLoop™`）。
- **代价照写**：拿修好的 `×` / `™` 去 raw 里搜**搜不到**，要搜坏掉的形态（§11.2）。

**④ 上标丢失（推断）。** 语法节 `### Example 1（取自子主题 Using sequencer instructions › Instructions for PRBS and SmartLoop tests）` 里那句写的是
`the first parameter of PRBS is set to its maximum value 231 - 1`、`the second parameter, which is also set to its maximum value 212 - 1`。
**这两个数只能是 2³¹ − 1 与 2¹² − 1**——依据是**同一段程序自己写着** `SQPG 5,PRBS,2147483647,4095`
（2147483647 = 2³¹ − 1，4095 = 2¹² − 1）。**HTML 转 markdown 时 `<sup>` 丢了**（推断）。
**本页照原样引，没替它补上标。**

**⑤ `waveform DC/DC power units`——原先写「本页不判」，现在收了：它不是原文如此，也不是 §11.2 那两族编码坏字。**
语法节里有 **3 处** `waveform DC/DC power units`（两处在图的 alt 文字里：
`Array of physical waveform DC/DC power units`、`Transferring waveform DC/DC power units into the data queue`；
一处在正文里：`Only the first 7 data cells of this block contain waveform DC/DC power units.`），
**三处的上下文讲的都是 vector area 与 data queue，与 DC/DC 电源无关**——这一句不变。
**两条新证据（2026-09-20 补）：**

- **同篇自证（文档事实，可 grep）**：那处正文出自语法节源文档 `02.06.07.01.04`，
  **而同一篇在别处把同一个东西叫 `physical waveform index`**——
  `divided into 8 data units of 8 bits. Every data unit can hold one physical waveform index`
  和 `Every active vector contains one physical waveform index`。
  **同一篇、同一个东西、两个叫法**，所以两个里至少有一个不是原文。
- **④ 图证**：这批文档自带的图**一律把它叫 `waveform indices`**——
  `10526.png` 的表头 `Waveform indices for pins`、`96892.png` 的括号 `Waveform indices`、
  `120207.png` 与 `120209.png` 的图例 `Active vectors (waveform indices)`、
  `120222.png` 的注释 `Base wavetable for translating waveform indices into device cycles (state characters) and vice versa`。
  **图上的字 grep 不到**：本页为核这一条在语料里另搜过，
  **`waveform indices` 这个复数形式 0 篇命中，`waveform index` 这个单数形式 67 篇命中**
  ——**活的叫法是 `index`，不是 `DC/DC power units`。**

**推断（推断链写在这里）**：`DC/DC power units` 是语料侧的一次**替换**，被换掉的词在 `index` 这一族里
——依据是**同一篇里 `index` 的形态活着，而 `DC/DC power units` 出现在 `index` 该在的位置**，
且**图一律用 `indices`**。**它纯 ASCII，所以按本页 ⚠️② 同一套理由，它不可能是 §11.2 的两族编码坏字**
（那两族吃的都是非 ASCII 字符）。**引文照原样留着它，一处不替它改**（§10 / §11.2）。
**具体在图上的样子见「是什么」的「④ 图证」（二）。**

**⑥ 图与文本一处对不上：相位同步那条等式里的 `k` 和 `j`（④ 图证）。**（2026-09-20 补）
语法节里那条等式逐字是 `k 脳 pA + FA + m 脳 8 脳 pA = k 脳 pB + n 脳 8 脳 pB`（出自 `02.06.07.01.10.03`）。
**同一篇正文上方就是那张图 `104693.png`**，图把两个端口的项分开标：
port A 的两段括号是 `= j * pA`（CTOF break vectors）与 `= m * 8 * pA`（synchronization break vectors），
中间夹一个 `F_A`；port B 是 `= k * pB` 与 `= n * 8 * pB`。
**也就是：图上 port A 的首项是 `j * pA`，文本里写成了 `k * pA`。**
同一族的那张 `104692.png` 也写 `= j * pA`。而正文刚写完 `j, k, m, n, x, y are integers.`——
**`j` 是声明过的变量**，等式右边的 `k 脳 pB` 又与图一致。
**推断**：文本里那个 `k` 是原文自己的笔误，`j` 才对（`FA` 在图上写作 `F_A`，`脳` 的问题见 ⚠️③）。
**这一处只有图看得出来**——**图上的字 grep 不到**。**本页照录语法节原文，一处不替它改**（§10）。

`verified: doc-only`
