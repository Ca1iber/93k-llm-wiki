---
type: object
title: Testflow file
layer: file
stage: testflow
tags: [testflow, file-format, bnf, test-suite, binning, flags, text-file]
related: [testflow, testflow-tool, test-suite, flag, testmethod, bin]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Testflow file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,121 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The following syntax listing conforms to the Backus-Naur Format (BNF). Additional symbols used in the syntax description are as follows:

 |

 |

 |

Indicate that a choice is available; read as or.

 |
 |

:=

 |

Read as comprises.

 |
 |

<x>

 |

A single construct, <x>.

 |
 |

[<x>]

 |

An optional construct <x>: " " or <x>.

 |
 |

(<x> | <y>)

 |

An alternative construct <x> or <y>.

 |
 |

[<x>] ...

 |

A sequence of one or more optional <x>: " " or <x> or <x> <x> etc.

 |
 |

<x> ...

 |

A sequence of one or more <x>: <x> or <x> <x> etc.

 |
 |

[ ... ]

 |

A sequence of one or more of the previous line - optional.

 |
 |

"<x>"

 |

A sequence of (3) predefined characters: "<" and "x" and ">".

 |
 |

[0-9A-F]

 |

A single character from the range 0123456789ABCDEF. Note that this differs from optionality grammar which always has a construct <> within it's braces, or is the [ ... ] specifier.

 |
 |

<x> ::= "x"

 |

The construct evaluates to the character "x".

 |
 |

--

 |

Denote a comment.

 |

### Example

```
hp93000,testflow,0.1
language_revision = 1;

information

device_name = "74145";

device_revision = "1";

test_revision = "1";

description = "The 74145 is a BCD-to-Decimal Converter";

end
-----------------------------------------------------------------
declarations

end
-----------------------------------------------------------------
implicit_declarations

end
-----------------------------------------------------------------
flags

datalog_formatter = 0;
datalog_sample_size = 1;
graphic_result_displa = 1;
state_display = 0;
print_wafermap = 0;
ink_wafer = 0;
max_reprobes = 1;
temp_monitor = 1;
calib_age_monitor = 1;
diag_monitor = 1;
current_monitor = 1;
log_events_enable = 1;
set_pass_level = 0;
set_fail_level = 0;
set_bypass_level = 0;
hold_on_fail = 0;
global_hold = 0;
debug_mode = 0;
debug_analog = 0;
parallel_mode = 1;
site_match_mode = 2;
global_overon = 0;
limits_enable = 0;
test_number_enable = 1;
test_number_inc = 1;
log_cycles_before = 0;
log_cycles_after = 0;
unburst_mode = 0;
sqst_mode = 0;
warn_as_fail = 1;
use_hw_dsp = 0;
dsp_file_enable = 0;
buffer_testflow_log = 0;
check_testmethod_api = 0;
stdf_generation = 1;
tm_crash_as_fatal = 1;
hidden_datalog_mode = 0;
multibin_mode = 0;
end
-----------------------------------------------------------------
testmethodparameters
tm_1:
  "testName" = "Functional";
  "output" = "ReportUI";
tm_2:
  "pinlist" = "@";
  "testCurrent" = "-80[uA]";
  "settlingTime" = "4[ms]";
  "measurementMode" = "PPMUpar";
  "polarity" = "BPOL";
  "prechargeToZeroVol" = "ON";
  "testName" = "passVolt_mV";
  "output" = "ReportUI";
tm_3:
  "pinlist" = "io_in";
  "measure" = "BOTH";
  "measureMode" = "PPMUpar";
  "relaySwitchMode" = "DEFAULT(BBM)";
  "forceVoltageLow" = "0[mV]";
  "forceVoltageHigh" = "4500[mV]";
  "spmuClampCurrentLow" = "0[uA]";
  "spmuClampCurrentHigh" = "0[uA]";
  "ppmuPreCharge" = "ON";
  "prechargeVoltageLow" = "0[mV]";
  "prechargeVoltageHigh" = "0[mV]";
  "settlingTimeLow" = "2[ms]";
  "settlingTimeHigh" = "2[ms]";
  "preFunction" = "ALL";
  "controlTestNumOfFunctional" = "NO";
  "stopCycVecLow" = "0";
  "stopCycVecHigh" = "0";
  "testName" = "(passCurrentLow_uA,passCurrentHigh_uA)";
  "output" = "ReportUI";
end
-----------------------------------------------------------------
testmethodlimits
tm_1:
  "Functional" = "":"NA":"":"NA":"":"":"";
tm_2:
  "passVolt_mV" = "200":"GE":"800":"LE":"":"":"0";
tm_3:
  "passCurrentLow_uA" = "-100":"GE":"100":"LE":"":"":"0";
  "passCurrentHigh_uA" = "-100":"GE":"100":"LE":"":"":"0";
end
-----------------------------------------------------------------
testmethods
tm_1:
  testmethod_class = "ac_tml.AcTest.FunctionalTest";
tm_2:
  testmethod_class = "dc_tml.DcTest.Continuity";
tm_3:
  testmethod_class = "dc_tml.DcTest.Leakage";
end
-----------------------------------------------------------------
test_suites
Continuity:
  override = 1;
 override_tim_equ_set = 1;
 override_lev_equ_set = 2;
 override_tim_spec_set = 1;
 override_lev_spec_set = 2;
 override_timset = 1;
 override_levset = 1;
 override_seqlbl = "gross_func";
 override_testf = tm_2;
local_flags  = output_on_pass, output_on_fail, value_on_pass, value_on_fail, per_pin_on_pass, per_pin_on_fail;
 site_match = 0;
 site_control = "parallel:";
Leakage:
  override = 1;
 override_tim_equ_set = 1;
 override_lev_equ_set = 2;
 override_tim_spec_set = 1;
 override_lev_spec_set = 1;
 override_timset = 1;
 override_levset = 1;
 override_seqlbl = "gross_func_leak";
 override_testf = tm_3;
local_flags  = output_on_pass, output_on_fail, value_on_pass, value_on_fail, per_pin_on_pass, per_pin_on_fail;
 site_match = 0;
 site_control = "parallel:";
gross_func:
  override = 1;
 override_tim_equ_set = 1;
 override_lev_equ_set = 2;
 override_tim_spec_set = 1;
 override_lev_spec_set = 2;
 override_timset = 1;
 override_levset = 1;
 override_seqlbl = "gross_func";
 override_testf = tm_1;
local_flags  = output_on_pass, output_on_fail, value_on_pass, value_on_fail, per_pin_on_pass, per_pin_on_fail;
 site_match = 0;
 site_control = "parallel:";
end
-----------------------------------------------------------------
test_flow

 run_and_branch(Continuity)
 then
 {
 }
 else
 {
    stop_bin "2", "Failed Continuity", , bad, noreprobe, red, 2, over_on;
 }
 run_and_branch(gross_func)
 then
 {
 }
 else
 {
    stop_bin "4", "Failed functional", , bad, noreprobe, red, 4, over_on;
 }
 run_and_branch(Leakage)
 then
 {
 }
 else
 {
    stop_bin "6", "Failed Leakage", , bad, noreprobe, red, 6, over_on;
 }
 stop_bin "1", "Pass", , good, noreprobe, green, 1, over_on;
end
-----------------------------------------------------------------
binning
otherwise bin = "db", "", , bad, noreprobe, red, , not_over_on;
end
-----------------------------------------------------------------
context

context_config_file = "pins_74ACT299_Incorruptus_CSDPS";
context_levels_file = "levels";
context_timing_file = "timing";
context_vector_file = "all.binl";
context_channel_attrib_file = "ChannelAttribute.soc";
end
-----------------------------------------------------------------
hardware_bin_descriptions
end

```

<!-- 语法节 end -->

## 是什么

**一句话：testflow file 是 testflow 工具的数据落盘处。** 原文第一句就是全部机制：

> 「The testflow tool stores the data in the testflow file located in the directory `<device_dir>/testflow`」

**三个立刻要记住的性质：**

| 性质 | 原文依据 |
|---|---|
| **一台设备一份** | 路径写死在 `<device_dir>/testflow` 下 |
| **它是纯文本** | `Since the testflow file is a text file, you can change parameters directly using a text editor.` |
| **但原文要你别直接改** | `However, we recommend changing the settings only by the [Testflow Tool](<02.08.04.32_Testflow_Tool.md>) of the SmarTest Work Center.` |

**所以本页的正确读法是：先知道它长什么样，才知道 Testflow Tool 点一下改的是文件里的哪一条。**

### 结构：全是 `关键字 … end` 包起来的段

BNF 的 `<section>` 一给出**全部 17 个段名**。把它们按「里面装什么」列出来，就是这份文件的目录：

| 段 | 里面装什么（据 BNF 的段定义） |
|---|---|
| `information` | `description` / `device_name` / `device_revision` / `test_revision` 四个字符串 |
| `declarations` | `@<var_name> = <expression>` 或 `@<var_name> = <string>` |
| `flags` | `<flag_name> = <flag_value>;` 或 `user <user_flag_name> = <flag_value>;` |
| `tests` | `<test_label>:` + 可选 `user_procedure = "<user parameters>";` |
| `testfunctions` | 标识符 + `testfunction_description` + `testfunction_parameters` |
| `datasets` | `<dataset_label>:` + 可选 `file = "<dataset_file>";` |
| `test_suites` | `<test_suite_entry>`（见下） |
| `initialize` / `download` / `abort` / `pause` / `reset` / `exit` | **六个段共用同一个定义 `<test_suite_entry>`** |
| `test_flow` | 一条 `<statement>` 序列 |
| `binning` | `otherwise bin = …`（见下） |
| `context` | 12 个 `context_*` 键（见下） |
| `hardware_bin_descriptions` | `<integer> = <string>;` |

文件头部另有一行可选的 `<lang_rev>`：`language_revision = <revision_number>;`。

> **「六个事件段共用 `<test_suite_entry>`」是本页最值得记的结构事实。**
> `initialize` / `download` / `abort` / `pause` / `reset` / `exit` 在 BNF 里各占一行，
> 但**六行右值逐字相同**，都是 `<test_suite_entry>`——
> **也就是说：这六段能写的东西，和 `test_suites` 里一条 suite 能写的东西是同一套。**

### 载入时会做参数范围检查，不合格就**整份不载**

这是原文 `## Range check of parameters` 一节的全部内容，也是**唯一一处讲「文件写坏了会怎样」**：

> 「If an invalid parameter is found, loading of the testflow will be aborted and an error message similar to the following will be displayed in the ui_report window:」

报错模板长这样（`...` 是**原文自带的**占位，不是本页省略）：

```
".../TestFlow", line ##, near ";": error: [;] Flag ... must be between ... and ...
ERROR: cannot parse shm setting from testflow '.../TestFlow'
```

**两行各管一件事**：第一行给**行号 + 就近的记号 + 哪个 flag 越界**；
第二行说**整份 testflow 解析失败**。
**「aborted / cannot parse」是最重的后果——不是跳过那一条参数，是整个 testflow 起不来。**
出问题时的第一现场因此很明确：**`ui_report` 窗口**。

**（推断）这条检查发生在「载入」时、不是「保存」时**——依据是原文用的词是
`loading of the testflow will be aborted`，全文没有一句把检查挂在保存或编辑上。
**所以：拿文本编辑器改完，照样要过这一关。**

### `*` 在语法里用了四次，而符号表没定义它

BNF 前面那张符号表（就是上面「语法 / 参数」节的第一张表）逐条定义了
`|` / `:=` / `<x>` / `[<x>]` / `(<x> | <y>)` / `[<x>] ...` / `<x> ...` / `[ ... ]` /
`"<x>"` / `[0-9A-F]` / `<x> ::= "x"` / `--`。

**表里没有 `*`。** 而语法正文里 `*` 出现在四处：
`<declaration>` 的 `* <test_suite>.ffc_on_fail`、
`<test_suite_entry>` 的 `* ffc_on_fail = <ffc_count>;` 与 `* override_wvfset = <expression>;`、
`<expression>` 操作数的 `* wsus()`。
**原文一处都没解释 `*` 是什么意思，本页不替它猜。**

### `--` 是注释，所以示例里那些横线是注释行

符号表最后一行：

> 「`--` / Denote a comment.」

示例文件里每个段之间都有一行 **65 个连字符**（`-----…----`）。
**（推断）那行是注释行**——依据就是上面这条：`--` 起头即注释，一整行连字符符合这个形状。
**原文没有对那行横线说过一个字。**

### `test_suite` 那一段：一条 entry 能写的键

`<test_suite_entry>` 的键（按 BNF 原样归类）：

| 类别 | 键 |
|---|---|
| **关联** | `datasets = <dataset_label>;` / `tests = <test_label>;` |
| **覆盖开关** | `override = <boolean>;` |
| **六个 `override_*`** | `override_dpsset` / `override_levset` / `override_seqlbl` / `override_timset` / `override_wvfset` / `override_testf` |
| **site 相关** | `site_match = {0 \| 1};` / `site_control = "<site_control_info>";` |
| **别的** | `test_level = <test_level>;` / `local_flags = <ts_flag> [, ...];` / `ffc_on_fail = <ffc_count>;` |

`<site_control_info>` 的形状是 `<sequence_type>: [<sequence_info>]`，
其中 `<sequence_type>` 是 `{serial|parallel|semiparallel|other}` 四选一，
**而 `<sequence_info>` 的写法随类型变**（BNF 自己括注了这两条）：

| `<sequence_type>` | `<sequence_info>` 怎么写 |
|---|---|
| `serial` / `parallel` | **省略**（BNF：`<sequence_info> is omitted if <sequence_type> = serial or parallel`） |
| `semiparallel` | `<size>:<cycle>:` |
| `other` | `<sequence_order>`（一串以 `:` 分隔的整数） |

`<ts_flag>` 是 11 个值的枚举：`bypass` / `set_pass` / `set_fail` / `hold` / `hold_on_fail` /
`output_on_pass` / `output_on_fail` / `value_on_pass` / `value_on_fail` /
`per_pin_on_pass` / `per_pin_on_fail`。

### `test_flow` 那一段：能写的语句

`<statement>` 一共这几种（BNF 原样）：

```text
<assignment>
run(<test_suite>)
run_and_branch(<test_suite>) then <statement> [else <statement>]
print(<print_expression>)
print_dl(<print_expression>)
if <expression> then <statement> [else <statement>]
while <expression> do <statement>
for <assignment>;<expression>;<assignment>; do <statement>
repeat <statement>; until <expression>
'{' <statement> [;<statement>]... '}'
    [[<compound_state>], [<compound_label>], [<compound_description>]]
stop_bin(<major_bin>, <minor_bin>, , <good_flag>, <reprobe_flag>, <color>, <physical_bin>[, <over_on_flag>]);
```

**这个文件里能拿来做判断的东西全在 `<expression>` 的操作数里**——BNF 给了 5 个问句函数
`pass()` / `fail()` / `tf_result()` / `has_run()` / `has_not_run()`，
以及 5 个状态函数 `wsus()` / `tsus()` / `lsus()` / `dsus()` / `bsus()`；
运算符是 `+ - * / > >= < <= == != ( ) and or not`。

`<color>` 两头都能写：

| 写法 | 值 |
|---|---|
| 整数 | `0` 黑 / `1` 白 / `2` 红 / `3` 黄 / `4` 绿 / `5` 青 / `6` 蓝 / `7` 品红 |
| 小写颜色名 | 原文：`or the name of the color in lower case.` |

**`stop_bin` 与 `binning` 段的 `otherwise bin`，参数表形状是同一套**
（`<major_bin>` `<minor_bin>` `, ,` `<good_flag>` `<reprobe_flag>` `<color>` `<physical_bin>`
再可选 `<over_on_flag>`）——BNF 里这两行逐字对应，**中间的连续两个逗号是语法的一部分**，
不是笔误：原文两条脚注都专门解释了它（见「出处」）。

### `context` 那一段：testflow 与其它 setup 文件的接缝

`<setup_section>` 给了 12 个键（原文顺序）：
`context_analog_control_file` / `context_attrib_file` / `context_channel_attrib_file` /
`context_config_file`（**在 BNF 里出现了两次**，第 1 个和第 5 个）/ `context_levels_file` /
`context_mixsgl_file` / `context_protocols` / `context_routing_file` / `context_testtable_file` /
`context_timing_file` / `context_vector_file` / `context_waveform_file`。

示例里用到的 5 个值与它们的取值：

| 键 | 示例里的值 |
|---|---|
| `context_config_file` | `"pins_74ACT299_Incorruptus_CSDPS"` |
| `context_levels_file` | `"levels"` |
| `context_timing_file` | `"timing"` |
| `context_vector_file` | `"all.binl"` |
| `context_channel_attrib_file` | `"ChannelAttribute.soc"` |

**（推断）这一段的角色是「这份 testflow 挂靠哪些 setup 文件」，依据有三**：
① 键名都是 `*_file`；② 取值是文件名（`"levels"` / `"timing"`）；
③ `context_config_file` 的值以 `pins_` 开头。
**原文只给了键名和一处示例取值，没有一句解释这些键各指什么文件、谁去读它们。**

### 示例文件的骨架（`## Example` 那一段）

原文给了一份完整的 74145（BCD-to-Decimal Converter）testflow。它实际写的段序是：

`information` → `declarations` → `implicit_declarations` → `flags` →
`testmethodparameters` → `testmethodlimits` → `testmethods` → `test_suites` →
`test_flow` → `binning` → `context` → `hardware_bin_descriptions`

> **⚠️ 其中四个段不在 BNF 的 `<section>` 列表里**：
> `implicit_declarations` / `testmethodparameters` / `testmethodlimits` / `testmethods`。
> **文档自己前后不一致，本页照实并列，不判谁对。**

其余可数的：`flags` 段写了 **38 个 flag**；`context` 段 5 个键；
文件头是 `hp93000,testflow,0.1` 加 `language_revision = 1;`；
`test_flow` 段是三次 `run_and_branch` + 各自 `else` 里一个 `stop_bin`，最后落 `stop_bin "1", "Pass"`。

## 典型用法

> **原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段。**
> 所以本页**没有一套可以照抄的步骤**——下面三条都是从「改这份文件」和「文件坏了」两处散文里抽的。

**1. 要改 setting，走 Testflow Tool。**
原文只给了一句「推荐」，**没有给步骤**：

> 「we recommend changing the settings only by the Testflow Tool of the SmarTest Work Center.」

**「改哪一条对应点哪个按钮」的答案在 `Testflow Tool` 那篇里，本页没读。**
直接拿文本编辑器改**原文承认可行**（`you can change parameters directly using a text editor`），
但**改完载入时照样过范围检查那一关**（见上「（推断）」）。

**2. 文件骨架照 `## Example` 抄。** 三段式：头部 `language_revision` + `关键字 … end` 的段 +
段与段之间那行 65 连字符的注释行。**要写 `initialize` / `download` / `abort` / `pause` /
`reset` / `exit` 这六段时，键照 `test_suites` 里一条 suite 写**（它们共用 `<test_suite_entry>`）。

**3. 载入失败先看 `ui_report` 窗口。** 报错的两行分别给
**行号 + 越界的 flag** 和 **`cannot parse` 的结论**。**注意它不会告诉你是哪一段的哪个键语义错了**——
它只给行号和 flag 名。

**4. 下一步（原文 `## Related information` 指的四篇）**：
`Test Methodologies` / `Elements of the Testflow Tool` / `Testflow components` / `Flags`
——**四篇本页都没读**。其中 `Flags` 那一篇是**唯一能解释那 38 个 flag 各自含义的地方**。

## 和谁有关

- [[testflow]] — 本页 `stage: testflow` 的归属：**本页是那个阶段的落盘产物**
- [[testflow-tool]] — **写这份文件的工具**，原文全文只点名了这一个工具，
  并把「改 setting」的正规路径指向它
- [[test-suite]]（**未建**）— `test_suites` 段定义的实体；
  **六个事件段与它共用同一份 BNF 定义**，所以这条关系比看上去近
- [[flag]] / [[flags-page]]（**均未建**）— `flags` 段的 38 个 flag 的含义侧；
  **本页只有 flag 的名字和取值，没有一个是干什么的**
- [[testmethod]] — 示例里的 `testmethods` / `testmethodparameters` / `testmethodlimits`
  三个段；**注意这三段不在 BNF 的 `<section>` 里**（见上）
- [[bin]] — `binning` 段的 `otherwise bin` 与 `test_flow` 里的 `stop_bin`
- [[timing-file]] / [[level-file]] / [[pin-configuration-file]]（**前两个未建**）—
  **（推断）`context` 段那几个键指的就是这些文件**，依据见上；**原文没明说**
- [[testflow-variable]]（**未建**）— `declarations` 段写的 `@<var_name>` 是不是它就是它，
  **原文没说，本页不判**
- [[command-reference]] — 同属「文件 / 命令」这一族的对照页
- [[smartest-6.3.2]] / [[smartest-7.1.0]] / [[smartest-7.2.0]] / [[smartest-7.2.2]] / [[smartest-7.3.2]] —
  本页「版本」节里那五条的中枢
- `Elements of the Testflow Tool` / `Testflow components` / `Test Methodologies`（**均未建**）—
  原文 `## Related information` 里的另外三篇

## 版本

原文有 `## Functional changes` 段。逐条：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.1.0**：`Testflow optimization function removed`
- **SmarTest 7.2.0（六条，全是「删」）**：移除 `report_to_file` flag、
  `report_to_printer` flag、`datalog_to_file` flag、`datalog_to_printer` flag、
  `datalog_to_report_win` flag——原文五条 flag 各占一行，外加 `Testflow optimization function removed`
  不在这一组里（它归 7.1.0）
- **SmarTest 7.2.2**：`Removed ooc_rule, OOC_watch, and OOC_sample_size related syntaxes`
- **SmarTest 7.3.2（十二条，全是「增」）**：新增 12 个 setup context——
  `context_analog_control_file` / `context_attrib_file` / `context_channel_attrib_file` /
  `context_config_file` / `context_levels_file` / `context_mixsgl_file` / `context_protocols` /
  `context_routing_file` / `context_testtable_file` / `context_timing_file` /
  `context_vector_file` / `context_waveform_file`

**两处对得上正文的地方**：

| 版本条目 | 正文里的对应 |
|---|---|
| 7.2.0 删掉 5 个 flag | **示例的 `flags` 段里确实没有这 5 个**——示例是这一节之后的状态 |
| 7.3.2 新增 12 个 context | **`<setup_section>` 正好列了这 12 个键**（其中 `context_config_file` 被列了两遍） |

> **`Introduced before SmarTest 6.3.2` 不要读成「6.3.2 新增的」。**
> 它是哨兵值——意思是「**在本文档集覆盖范围开始之前就已经有了**」（schema §11.2 ②）。
> **照字面读会凭空造出一条「6.3.2 新增了 testflow file」的假信息，而且格式齐整。**

## 出处

`sources:` 一篇：

`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.md`
（TDC `43086.htm`，源 markdown 670 行）

**本页没做的**：

- **只读了这一篇。** `## Related information` 指的四篇
  （`Test Methodologies` / `Elements of the Testflow Tool` / `Testflow components` / `Flags`）
  **一篇都没读**——所以**那 38 个 flag 的含义、`context_*` 各键的定义、
  Testflow Tool 的操作步骤，本页一个字都没有**。
- **没有 `## Procedure` / `## Before you begin` / `## What to do next` 段可读**，
  所以「怎么新建 / 打开 / 保存一份 testflow」本页没有。
- **一篇文档一张图都没有**，本页**没有任何来自图的结论**（本篇也没有图）。
- **没有实测**：本页**没有在任何真实 testflow 上验证过范围检查的报错格式**，
  那一节照文档抄。
- **`<section>` 与示例对不上的那四个段**，本页**只并列、不解释**——
  解释它们需要 `testmethod` 那几篇，那些本页没读。
- **BNF 里 `*` 的含义、那行 65 连字符是不是注释**，本页**都只标了「原文没说」**。

> ⚠️ **本篇的语料瑕疵，照实记，一处都没替它改**：
>
> ① **`pogitive` 应为 `positive`**：
> `<sequence_order_element> := an integer number (where, 0 = undefined, or a pogitive integer = test order)`。
> ② **`unbouded` 应为 `unbounded`**：
> `or -1 for "unbouded"`。
> ③ **`it's` 应为 `its`**：
> `Note that this differs from optionality grammar which always has a construct <> within it's braces`。
> ④ **同一个 flag 在语法节与示例里拼法不同**：
> BNF 写 `graphic_result_displ`，示例写 `graphic_result_displa`。
> ⑤ **同一个 flag 一处带下划线一处不带**：
> BNF 的 `<system_flag>` 写 `ink wafer`，示例写 `ink_wafer`。
> ⑥ **`<tflow_flag>` 那一串全部写成带空格的短语**：
> `set pass level | set fail level | bypass level | hold on fail | global_hold |
> debug mode | site_match_mode`——
> **而示例里是 `set_pass_level` / `set_fail_level` / `set_bypass_level` / `hold_on_fail` /
> `debug_mode` / `site_match_mode`**（六个都有下划线）。
> ⑦ **`context_config_file` 在 `<setup_section>` 里列了两次**（第 1 行和第 5 行）。
> ⑧ **脚注标记漏进了语法正文**：`stop_bin[1)](<#fntarg_1>)` 与 `otherwise bin[2)](<#fntarg_2>)`——
> **`[1)](<#fntarg_1>)` 是引用标记，不是语法的一部分。**
> ⑨ **示例里有四个段不在 BNF 的 `<section>` 列表里**：
> `implicit_declarations` / `testmethodparameters` / `testmethodlimits` / `testmethods`。
> ⑩ **首句末尾缺句号**：`…located in the directory <device_dir>/testflow`（无 `.`）。
> ⑪ **`## Functional changes` 段吞掉了文末脚注**（schema §11.2 ③ 那一类）：
> 那两条解释「逗号之间为什么要留空」的脚注定义
> （`For compatibility reasons to older versions, SmarTest saves stop_bin with a blank in between commas`）
> **现在挂在 `## Functional changes` 段末尾，和版本变更混在一起**。
> ⑫ **`Introduced before SmarTest 6.3.2` 是哨兵值**，见上面「版本」节的说明（§11.2 ②）。
> ⑬ **BNF 符号表没有定义 `*`，而语法正文用了四次**（见上「是什么」节）。

`verified: doc-only`
