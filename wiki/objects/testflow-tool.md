---
type: object
title: Testflow Tool
layer: gui
stage: testflow
tags: [testflow, gui, testflow-tool, flow-data-editor, flow-sequence-editor, testflow-file, testflow-master-file, hardware-response-emulator, single-step-debug, report-window]
related: [testflow, flow-sequence-editor, flow-data-editor, testflow-properties-view, testflow-file, testflow-master-file, test-suite, bin, flags-page, flow-control-node, hardware-response-emulator, hardware-response-file, testflow-analyzer-tool, report-window, debug-view, run, mapping-testflow]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32_Testflow_Tool.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Testflow Tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **22,776 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32_Testflow_Tool.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.02_Flow_control_nodes.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.03_Hierarchy_within_a_testflow.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.05_Configuring_the_messages_printed_in_the_Report_Window.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.05_Inserting_a_bin_into_the_testflow.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.14_Identifying_fail_labels_in_a_burst.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.16_Exporting_a_testflow_to_a_CSV_file.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.04_Measuring_the_test_time.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04.01_Single_step_testflow_debugging.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.03_Hardware_response_files.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.05_Variables_page.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Introduction of the Testflow › Testflow components › Flow control nodes）

Expressions which can be used as the condition might be:

- `fail (functional) and (x <=6)`
- `has_run (test1) and not (variable2 > (((13/7)-1)*5))`
- `not (variable1 == variable2) or ((variable3 - 1)<10)`

### Example（取自子主题 Introduction of the Testflow › Testflow components › Bins）

If for some reason your production run should stop unexpectedly, all devices that have not ended up in either a good or bad bin will be assigned to the otherwise bin. This bin is also included in yield calculations, as it can be defined as a good or a bad bin.

### Example（取自子主题 Introduction of the Testflow › Hierarchy within a testflow）

In the testflow shown below, there are three distinct levels. If you select either of the test suite nodes, all nodes in all levels stemming from this node are also selected.

 !`A testflow containing three separate levels`（raw: `../../../../agent-html/110643.png`）

The figure below shows the effect of selecting node test_2_1; the nodes which branches from test_2_1 are also selected. Similarly, you cannot select more than one node from different levels; you can, however, select more than one node within the same level. For example, you could select test_1_2 and test_1_3, but not test_1_2 and test_2_2 or test_3_1.

 !`Effect of clicking on test_2_1`（raw: `../../../../agent-html/110644.png`）

### Examples（取自子主题 Introduction of the Testflow › Configuring the messages printed in the Report Window）

### Printing messages for passed and failed sites in the Report Window

This example shows how you can configure the .testflow.ReportUiOutput.user_def file to print messages in the Report Window for all passed and failed sites after a testflow is executed:

```
<passed>Site: %site -> Bin: %bin -> PASS (Cool)
<failed>Site: %site -> Bin: %bin -> FAIL (Bad)
#<text> This is an example for a commented line (using "#" at the beginning)
```

The messages that are printed in the Report Window are as in the following figure:

!`Printing messages for passed and failed sites in the Report Window`（raw: `../../../../agent-html/345529.png`）

### Printing messages for failed sites only in the Report Window

This example shows how you can configure the .testflow.ReportUiOutput.user_def so that only messages for the failed sites are printed in the Report Window:

```
<failed>Site : %site -> Bin: %bin -> FAIL (Bad)
```

!`Printing messages for failed sites only in the Report Window`（raw: `../../../../agent-html/345530.png`）

### Printing messages in the Report Window for the failed sites after a test suite is executed

This example shows how you can configure your .testflow.ReportUiOutput.user_def file to print a message in the Report Window for the failed sites after a test suite is executed:

```
<failed>TestSuite: %testSuiteName -> Site: %site -> FAIL
```

!`Printing messages in the Report Window for failed sites only after a test suite is executed`（raw: `../../../../agent-html/345531.png`）

### Example（取自子主题 Using the Testflow Tool › Editing a testflow › Inserting a bin into the testflow）

This test method example shows how to define multibins for multisite testing.

```
[..]

bool passed=true;

ON_FIRST_INVOCATION_BEGIN();
    CONNECT();
    FUNCTIONAL_TEST();
ON_FIRST_INVOCATION_END();

if (!TESTSET().cont(true).judgeAndLog_FunctionalTest())
//Functional results are cached for each site by the API
    {SET_MULTIBIN("abc", 12);
    //The devices which fail at the first functional test fall in bin 12.
    passed = false;
    }

[..]

```

```

return;
```

### Example（取自子主题 Using the Testflow Tool › Editing a testflow › Identifying fail labels in a burst）

In this testflow, any failing device from the test suite "Unburst" will end up in bin f1.

 !`Find the failing label in a burst`（raw: `../../../../agent-html/110991.png`）

### Example（取自子主题 Using the Testflow Tool › Editing a testflow › Exporting a testflow to a CSV file）

This is an example of a testflow and the resulting CSV file.

 !`Testflow example`（raw: `../../../../agent-html/110985.png`）

The following is the related CSV file as displayed in a text editor. (For a tabular view, you can also open the file in spreadsheet programs like Excel.)

```
$,Testsuites
>,"Testsuite Name",Type,Name,LibPath,"Tim Eqn","Tim Eqn Desc","Tim Spec",
"Tim Spec Desc","Tim Set","Tim Set Desc","Lev Eqn","Lev Eqn Desc","Lev Spec",
"Lev Spec Desc","Lev Set","Lev Set Desc","Ana Set","Ana Set Desc",
Pattern,Pass/Fail,"Exec Time (ms)","Exec Num","Test Level",Bypass,
"Set pass","Set fail",Hold,"Hold on fail","Output on pass","Output on fail",
"Pass value","Fail value","Per pin on pass","Per pin on fail","Set breakpoint",
"Log MX Waveforms","Fail per label","FFC enable","FFC scan info enable",
"Log first","FFV enable","FRG enable","H/L/I/U (multiple execution)",
"HW DSP disable","Site Match","Allow Parallel","Site Control",Size,Cycle,#1,
"Testsuite Comment"
,continuity,T,continuity,,1,,2,,1,,2,,2,,1,,,,"""gross_func""",,,,0,F,F,F,F,
F,T,T,T,T,T,T,F,F,F,F,F,1,F,F,F,F,UNDEF,T,PARALLEL,,,1,
,gross_func,T,functional,,1,,1,,1,,2,,2,,1,,,,"""gross_func""",,,,0,F,F,F,F,
F,T,T,T,T,T,T,F,F,F,F,F,1,F,F,F,F,UNDEF,T,PARALLEL,,,1,
>,"Testmethod type parameter","Testmethod type value"
,UTMBased,F
$,Parameters
>,"Testsuite Name","Action Name","Name 1","Type 1","Value 1"
,continuity,continuity,continuity,,"@;0;uA; -80;mV; 200;mV; 800;mV; 900;ms;
0;1;Continuity ($P);mV;;1;"
,gross_func,functional,functional,,
$,Tests
>,"Testsuite Name","Test Name","Test Number","Lower Limit","Lower Symbol",
"Upper Symbol","Upper Limit"
,gross_func,[TF]Functional,,,N/A,N/A,
,continuity,[TF]Continuity,,,N/A,N/A,
$,Bins
>,"Software Bin","Software Bin Desc","Hardware Bin","Hardware Bin Desc",
Type,"Bin Color","Bin ReProbe","Bin OverOn"
,1,Pass,,,good,Green,no,yes
,5,"Failed Continuity",,,bad,Red,no,yes
$,Variables
>,Name,Type,"Initial Value","Current Value"
,VIL,DOUBLE,2.4,2.4
,VIH,DOUBLE,2.6,2.6
,i,DOUBLE,0,0.0
$,Flags
>,Flags,"Flag Type",Value
,datalog_formatter,SYSTEM,off
,datalog_sample_size,SYSTEM,1
,graphic_result_display,SYSTEM,on
,state_display,SYSTEM,off
,print_wafermap,SYSTEM,off
,ink_wafer,SYSTEM,off
,max_reprobes,SYSTEM,1
,temp_monitor,SYSTEM,on
,calib_age_monitor,SYSTEM,on
,diag_monitor,SYSTEM,on
,current_monitor,SYSTEM,on
,log_events_enable,SYSTEM,on
,tm_crash_as_fatal,SYSTEM,off
,set_pass_level,TESTFLOW,0
,set_fail_level,TESTFLOW,0
,set_bypass_level,TESTFLOW,0
,hold_on_fail,TESTFLOW,off
,global_hold,TESTFLOW,off
,debug_mode,TESTFLOW,off
,debug_analog,TESTFLOW,off
,parallel_mode,TESTFLOW,on
,site_match_mode,TESTFLOW,auto(on)
,global_overon,TESTFLOW,off
,limits_enable,TESTFLOW,off
,test_number_enable,TESTFLOW,on
,test_number_inc,TESTFLOW,1
,log_cycles_before,TESTFLOW,0
,log_cycles_after,TESTFLOW,0
,unburst_mode,TESTFLOW,off
,sqst_mode,TESTFLOW,off
,warn_as_fail,TESTFLOW,on
,rf_cal_enable,TESTFLOW,on
,rf_cal_interp,TESTFLOW,off
,rf_dembedCal_enable,TESTFLOW,off
,use_hw_dsp,TESTFLOW,off
,buffer_testflow_Log,TESTFLOW,off
,check_testmethod_api,TESTFLOW,off
$,Setups
>,Setup,File
,"Pin Configuration",pins_soc
,Levels,levels
,Timing,timing
,Pattern,all.binl
,"Pin Attributes",
,"Channel Attributes",
,"Analog Control",
,Waveform,
,Routing,
,"Test Table",
$,Information
>,Name,Value
,Description,
,"Device Name",
,"Device Revision",1
,"Test Revision",
$,FlowSequence
>,Index,"Flow Node",Argument
,1,run,gross_func
,1_1,FAIL,
,1_1_1,run,continuity
,1_1_1_1,FAIL,
,1_1_1_1_1,"stop bin",5
,2,"stop bin",1
```

### Example（取自子主题 Using the Testflow Tool › Running a testflow › Measuring the test time）

A simple testflow comprises two test suites, cont and func, in this order. cont performs a continuity test and func a functional test. Both test suites only ask for a global PASS/FAIL result. The testflow is executed three times for two sites, resulting in six devices.

When the testflow is not optimized, the output of the debug mode 3 is shown as below.

 !`Debug 3 Output for unoptimized testflow`（raw: `../../../../agent-html/94560.png`）

Observe the following points in the listing:

- The `# of measure.` column in the `TESTFLOW INFORMATION` specifies the number of testflow repetitions. The number of measurements that is specified on the test suite level in the `seq setup` and `test suite exec.` rows specifies how often the respective test suites are executed. If the testflow is not optimized, this number is the number of testflow repetitions multiplied by the number of sites. The reason for this is that the two sites are processed serially in an unoptimized testflow, so that the test suite must be called twice in every testflow repetition.
- The time spent for executing connect and disconnect sequences is not explicitly specified in an unoptimized testflow. It is included in the test suite execution time. This is in contrast to the output for optimized testflows, as explained below. In both optimized and unoptimized testflows a test suite executes a connect or disconnect sequence only if this is necessary.
- The test suites are ordered as they are defined in the testflow file.
- The total time for running the testflow is greater than the sum of all total test suite times. There are several reasons for this. For example, the testflow can contain nodes which are not test suites, such as Assign Value nodes.

The second figure displays the results after the testflow has been optimized:

 !`Debug mode 3 output for optimized testflow`（raw: `../../../../agent-html/94561.png`）

Observe the following points in this listing:

- An additional line `set connect` is specified for the test suite `func`, but not for `cont`. This shows that a connect or disconnect sequence is executed for `func`, but not for `cont`. In fact, since the tester is in the DISCONNECTED state at the start of a testflow, and the continuity test of the first test suite must be executed in the DISCONNECTED state, it is not necessary to disconnect it again. But the functional test of func must be executed in the CONNECTED state, and therefore a connect sequence must be executed at the start of the second test suite.
- The benefit of downloading the setup data only once can be seen in the `seq setup` line of `cont`. The advantage of executing all sites in parallel can be seen in the `test suite execution` lines of both test suites. The parallel execution of the two sites is also reflected in the number of measurements for the `seq setup` and `test suite execution` rows (three instead of six).

### Examples（取自子主题 Using the Testflow Tool › Debugging a testflow › Single step testflow debugging）

### Preconditions for all examples

- Testflow editor is opened
- Testflow is loaded

### Specification for "Run and Hold"

Starting with Run and Hold testflow execution you can seamlessly continue testflow debugging using the Step Over button.

Preconditions:

- The testflow contains at least two test suites in the same branch. The first test suite is named Testsuite_1, the second Testsuite_2.

Procedure:

- On the testflow editor, select Testsuite_1.
- Right-click the test suite and select Run > Run Testflow and Hold after Here.

Testflow execution starts and pauses after executing the selected test suite.

A WARNING window is displayed.

The Debug view opens, showing the execution node Testflow (Full) with the child entry Ftest (Testsuite_1).

  !`Debug view for testflow execution`（raw: `../../../../agent-html/125021.png`）

The buttons Resume, Terminate, and Step Over are enabled.

- Click Step Over.

Test suite Testsuite_2 is executed and execution is waiting.

A WARNING window is displayed.

The Ftest (Testsuite_1) child entry changes to the Ftest (Testsuite_2).

- Control the process:

  - Click Resume to continue testflow execution with no stops.
  - Click Step Over to execute exact one (next) test suite in testflow.
  - Click Terminate to abort testflow execution.

### Specification for "Run selected"

Starting with Run Testflow (Selection) testflow execution you can perform single step testflow debugging using the Step Over button.

Preconditions:

- Testflow contains at least five test suites in the same branch. Testsuite_1, Testsuite_2, Testsuite_3, , Testsuite_4, and Testsuite_5.

Procedure:

- Select Testsuite_1 and Testsuite_3.
- Right-click Testsuite_1 and select Run > Open Run Dialog.

The Run Configurations windows is displayed.

- Select the default Testflow (Selection) run configuration.

For details on the configuration, see `Running a testflow`（raw: `02.08.04.32.02.03_Running_a_testflow.md`）.

- Select Enable 'single step' execution mode.
- Click Apply.
- Click Run.

The testflow execution starts and pauses after executing Testsuite_1.

The Debug view opens, showing the execution node Testflow (Selection) with the child entry Ftest (Testsuite_1).

The buttons Resume, Terminate, and Step Over are enabled.

- Click Step Over.

Test suite Testsuite_3 is executed and execution is terminated.

The Ftest (Testsuite_1) child entry changes to the Ftest (Testsuite_3).

In all cases the testflow execution terminates before the execution of test suite Testsuite_5.

### Specification for "Run selected (loop)"

Starting with Run Testflow (Selection) testflow execution you can perform single step testflow debugging using the Step Over button, and you can manually control the loop execution.

Precondition:

- Testflow contains at least five test suites in the same branch. Testsuite_1, Testsuite_2, Testsuite_3, , Testsuite_4, and Testsuite_5.

Procedure:

- Select Testsuite_1 and Testsuite_3.
- Right-click Testsuite_1 and select Run > Open Run Dialog.
- Select the default Testflow (Selection) run configuration.
- Select Enable 'single step' execution mode.
- Select Loop and Loop Indefinitely.

For details on loop configuration, see `Loop configuration settings`（raw: `02.08.04.32.02.03.01_Loop_configuration_settings.md`）.

- Click Apply.
- Click Run.

The testflow execution starts and pauses after executing Testsuite_1.

The Debug view opens, showing the execution node Testflow (Selection) with the child entry Ftest (Testsuite_1).

The buttons Resume, Terminate, and Step Over are enabled.

- Click Step Over.

Test suite Testsuite_2 is executed and execution is waiting.

The Ftest (Testsuite_1) child entry changes to the Ftest (Testsuite_3).

- Control the process:

  - Click Resume to continue the looping testflow execution.
  - Click Suspend to pause the execution.
  - Click Step Over to execute exact one (next) test suite in testflow.
  - Click Terminate to abort testflow execution.

### Specification for "Run custom testflow"

Starting with Run Testflow (User Defined) testflow execution you can perform single step testflow debugging using Step Over button, optionally you may control loop execution if loop is enabled (see `Loop configuration settings`（raw: `02.08.04.32.02.03.01_Loop_configuration_settings.md`）).

Precondition:

- Testflow contains at least five test suites in the same branch. Testsuite_1, Testsuite_2, Testsuite_3, , Testsuite_4, and Testsuite_5.

Procedure:

- Select Testsuite_1 and Testsuite_3.
- Right-click Testsuite_1 and select Run > Open Run Dialog.
- Create a new Testflow (User Defined) run configuration.

By default, Whole Flow is enabled and the Single Step Execution configuration area is disabled.

- Select Testsuite(s) or Group(s) and type or select your selection.

For details on the configuration, see `Running a testflow`（raw: `02.08.04.32.02.03_Running_a_testflow.md`）.

The Single Step Execution configuration area is now enabled.

- Select Enable 'single step' execution mode.
- Click Apply.
- Click Run.

The testflow execution starts and pauses after executing Testsuite_1.

The Debug view opens, showing the execution node Testflow (Selection) with the child entry Ftest (Testsuite_1).

The buttons Resume, Terminate, and Step Over are enabled.

- Click Step Over.

Test suite Testsuite_2 is executed and execution is waiting.

The Ftest (Testsuite_1) child entry changes to the Ftest (Testsuite_3).

- Control the process:

  - Click Resume to continue the testflow execution with no stops.
  - Click Step Over to execute exact one (next) test suite in testflow.
  - Click Terminate to abort testflow execution.

In all cases the testflow execution terminates before the execution of test suite Testsuite_5.

### Example（取自子主题 Using the Testflow Tool › Hardware Response Emulator › Using hardware response files for execution）

When the hardware response file is not found for the execution of a test suite with the pass/fail result, the Hardware Response Emulator Pass/Fail Dialog window for the "Import" mode opens.

 !`Emulator dialog for setting pass/fail state for each testsuite`（raw: `../../../../agent-html/21635.png`）

### Example（取自子主题 Using the Testflow Tool › Hardware Response Emulator › Hardware response files）

The hardware response file `TS1;Analog.DGT("a_out").getWaveform(1);1;1` is related to the first execution of the `Analog.DGT("a_out").getWaveform()` API called on site 1 in the method program in the `TS1` test suite. Note that a hardware response file name contains a default input value even if the value was not set in the related API. This is the reason why the file name contains `Waveform(1)` even if "1" is not set for the API.

### Example（取自子主题 Elements of the Testflow Tool › Flow Data Editor › Variables page）

You can use a user flag to branch in a testflow, depending on the current value of the flag. This lets you control the testflow execution during a test program run.

### Syntax（取自子主题 Elements of the Testflow Tool › Testflow file）

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

### Example（取自子主题 Elements of the Testflow Tool › Testflow file）

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

### Example（取自子主题 Elements of the Testflow Tool › Testflow master file）

```
hp93000,testflow_master_file,0.1

testerfile: testflow

information: files/general.tfl
flags: files/general.tfl
bins: files/general.tfl
setup: files/general.tfl
VAR_Default: files/vars.tfl

GROUP group1: files/group1.tfl
VAR myvar1: files/group1.tfl
VAR myvar2: files/group1.tfl

GROUP group2: files/group2.tfl
VAR myvar3: files/group2.tfl
```

<!-- 语法节 end -->

## 是什么

**Testflow Tool 是 SmarTest Work Center 里开发与调试 testflow 的那个工具。** 定义文档的正文只有一句话：

> 「The Testflow Tool is used to develop and debug a testflow.」

**这一句就是那篇文档的全部正文**（18 行 / 562 字节）。它是一篇**父主题页**：底下挂三支子主题，
正文里再没有第二句自己的说明。

### 定义文档一共给了三样东西

| 给了什么 | 内容 |
|---|---|
| 一句定义 | 上面那句 |
| `#### Subtopics` 三条 | Introduction of the Testflow / Using the Testflow Tool / Elements of the Testflow Tool |
| `## Functional changes` 一条 | `Introduced before SmarTest 6.3.2` |

**`## Related information` / `## Procedure` / `## Before you begin` / `## What to do next` 这四段，本篇一段都没有**——
所以本页「典型用法」只能从别的材料里拼（见那一节）。

### 本页「语法 / 参数」那 22,699 字节，不是这个工具的「语法」

语法节自己声明了来源：**定义文档 + 它下游的 14 篇子主题**。
GUI 工具本来没有语法；那 22,699 字节装的是子主题的 `Example` / `Syntax` 段，
**按本篇的文档树分支排下来**：

| 分支 | 语法节里出现的东西 |
|---|---|
| Introduction of the Testflow | flow control 节点的条件表达式三例；otherwise bin；testflow 的三层层级与「选中会连带选中下游」；Report Window 消息配置三例 |
| Using the Testflow Tool | 插 bin 的 `SET_MULTIBIN` testmethod 例；burst 里的 fail label；导出 CSV 的完整例；test time 测量；单步调试的四份 Specification；Hardware Response Emulator |
| Elements of the Testflow Tool | Flow Data Editor 的 Variables page；testflow 文件的 BNF 记号说明与一份完整文件；testflow master file 例 |

**这一格一格是按语法节里已经写着的段名归类的**——每个段的标题本身就是来源
（`### Example（取自子主题 X › Y › Z）`）。**那 14 篇子主题本页一篇都没读**（见「出处」），
所以上表说的是「语法节里有什么」，不是「Testflow Tool 还有什么功能」。

### 从语法节能读出来的六件事

1. **编排**：flow control 节点的条件写成表达式。原文给的例是
   `fail (functional) and (x <=6)`、`has_run (test1) and not (variable2 > (((13/7)-1)*5))`、
   `not (variable1 == variable2) or ((variable3 - 1)<10)`。
2. **定 bin**：`stop_bin`、multibin（testmethod 里 `SET_MULTIBIN("abc", 12)`），以及 **otherwise bin**：

> 「If for some reason your production run should stop unexpectedly, all devices that have not ended up in either a good or bad bin will be assigned to the otherwise bin.」

3. **出报告**：Report Window 的消息由 `.testflow.ReportUiOutput.user_def` 配置，
   语法节给了三份配置例（全部站点 / 只失败站点 / 每个 test suite 一条）。
4. **看时间**：debug mode 3 打印每个 test suite 的耗时（见下「图证」那两张表）。
5. **调试**：单步执行。**前提是先用带单步的 run configuration 启动**
   （Run and Hold / `Testflow (Selection)` / `Testflow (User Defined)` 三种起法），
   之后在 Debug view 里用 `Resume` / `Step Over` / `Terminate`（循环配置下另有 `Suspend`）。
6. **没有硬件也能跑**：Hardware Response Emulator 拿文件把 API 的返回值喂回去。

### 图证：本页引的 11 张图，逐张读过（④ 图证）

本页「语法 / 参数」节引到 **11 张 `.png`，全部读了**。
路径 `../../../../raw/<n>.png` 从 md 往上四层正好是 `tdc-html/`，文件就在 `tdc-html/raw/`——
**有些页曾写「图在语料树之外」，那是错的**（`schema.md` §11.4）。

| 图 | 读到了什么（正文里没有的） | 图里的字在 raw 里 grep 得到吗 |
|---|---|---|
| `110643.png`（三层层级） | 三层分别是：第 1 层 `test_1_1`；第 2 层 `test_1_2` / `test_2_1`；第 3 层 `test_1_3` / `test_2_2` / `test_3_1`。三个 bin 节点写作 `A1` / `A2`（绿）/ `A3`（红）。**正文只说「three distinct levels」，从没给过「哪一层是哪几个节点」** | 节点名搜得到（正文里就有）；**`A1` / `A2` / `A3` 在语料别处有命中（多半是子串），本页不敢说它们只在图里**——但**本篇这一支的正文里没有这三个名字** |
| `110644.png`（点 `test_2_1` 之后） | 「选中会连带选中下游」在图里是**一块灰色背景**：`test_2_1` + `test_2_2` + `test_3_1` + `A2` + `A3` 全在灰底里，`A1` 那条支路留在灰底外 | 灰色高亮这件事，raw 文本里一句话都没有 |
| `110985.png`（testflow 例） | 上下两个窗格。下面是 Flow Sequence Editor（Palette 全小写：`goodbin` / `badbin` / `multi_bin`）；上面是 Flow Data Editor，八个页签 `Test Suites` / `Parameters` / `Tests` / `Bins` / `Variables` / `Flags` / `Setups` / `Information`，表头 `Test Suite Name` / `Timing Eqn` / `Desc` / `Spec/Waveform Set` / `Desc`，两行数据 `gross_func` 与 `continuity` | 页签名与列名搜得到（本页语法节的 CSV 导出例里逐字有 `$,Testsuites` 到 `$,Information`）；**`Spec/Waveform Set` 全语料只有 1 处，且不在本篇这一支** |
| `94560.png` / `94561.png`（debug mode 3 输出） | 行标签逐字：未优化那张是 `total time` / `seq setup` / `testsuite exec. (non opt.)`；已优化那张是 `total time` / `set connect` / `testsuite execution (opt.)` / `seq setup`。列头 `# of measure.` / `sum` / `minimum` / `maximum` / `average` | `set connect` 与 `testsuite execution` 搜得到；**但两张图那两行的完整标签（`testsuite exec. (non opt.)` 与 `testsuite execution (opt.)`）都 0 命中**——正文写的是 `test suite exec.`，**图里那个词没有空格，后面还挂着 `(non opt.)` / `(opt.)`** |
| `125021.png`（Debug view） | 树是 `Testflow (Full) [Testflow (Full)]` → 子项 `FTest`。工具栏上一排按钮里，绿色三角、黄色暂停条、红色方块三个是亮的（形状对 Resume / Suspend / Terminate），其余是灰的；**哪个图标对哪个按钮名，图里没有文字标签，本页不猜** | 正文写的是 `Ftest`（**小写 t**），全语料只 1 处；**图里是大写 `T`**——两处不一致。**方括号那一份 `Testflow (Full) [Testflow (Full)]` 全语料 0 命中**（`Testflow (Full)` 单独搜有 6 篇） |
| `21635.png`（Hardware Response Emulator Pass/Fail Dialog） | 窗口标题 `Hardware Response Emulator` + `Pass/Fail Dialog`；字段标签 `Testsuite; MAPI; call#; site#`；框里的值 `Functional_test;GET_FUNCTIONAL_RESULT();2;1`；两个单选 `Pass` / `Fail`；按钮 `Ok`、复选框 `store HW Response Data`、`Bypass Emulator`、`Emulator Off` | 标签 `Testsuite; MAPI; call#; site#` 与 `Bypass Emulator` **在语料别处有命中**；**`store HW Response Data`、`Emulator Off`、`Functional_test;GET_FUNCTIONAL_RESULT();2;1` 全 0 命中** |
| `345529.png` / `345530.png` / `345531.png`（Report Window） | 窗口标题 `ui_report.ORG.PROD`；底部 `Report Formatter` 的值 `.default.PROD`；`Tester State` = `DISCONNECTED (OFFLINE)`、`Tester Operation` = `NOT monitored (DISABLED)`（都标黄）。`345530` 另有 `USER-DEFINED DISCONNECT SEQUENCE ENABLED!`、`device : vec_transfer`、`DUT_path : /tmp`、`testflow : LimitTable`、`userprocedure : ****`、`Started at:` 与 `Ended at:`。`345531` 里失败的 test suite 名是 `limits`；五个 site 号 `345530` 与 `345531` 都是 **5 / 16 / 23 / 57 / 110** | `Report Formatter`、`PASS (Cool)`、`FAIL (Bad)` 搜得到；**`Tester State`、`Tester Operation`、`vec_transfer`、`LimitTable`、`userprocedure`、`Started at:`、`Ended at:`、`ui_report.ORG.PROD`、`TestSuite: limits` 全 0 命中**（`default.PROD` 有 1 处） |
| `110991.png`（burst 里的 fail label） | 流程里有两个 `PTD`（Print to Datalog）节点，标签是打印 `@lbl PASSED` / `@lbl FAILED` 的字样（图上那个 `\` 是不是原样字符，这个分辨率下本页不判）；红 bin 的名字是 `f1`；**被高亮的那一段里 test suite 写作 `UnBurst`** | 正文写的是 **`Unburst`**（**小写 b**）；**`UnBurst` 全语料 0 命中**——图与正文大小写不一致 |

**十一张里只有一张回答了正文的疑问**：`21635.png` 把硬件响应文件那个四段式键
**拆开写成了字段名**——`Testsuite; MAPI; call#; site#`。
本页语法节里那个例（`TS1;Analog.DGT("a_out").getWaveform(1);1;1`），
正文只说它属于 `TS1` 这个 test suite 里、site 1 上第 1 次调用的那个 API，
**四段各是什么正文没逐个点名，图里逐个点了**。
**其余十张只是把正文已有的东西画出来，或录下某一次具体运行的数值。**

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**，
所以「怎么用」只能用语法节里那四份**单步调试 Specification** 来写
（它们各自带 `Preconditions` 与 `Procedure`）。**四份的差别只在「怎么起」**：

| 起法（原文的 run configuration） | 前提 | 点 `Step Over` 之后 |
|---|---|---|
| 右键 test suite → `Run > Run Testflow and Hold after Here` | 同一分支上至少两个 test suite | 下一个 test suite 执行并等待，弹 WARNING，树里的子项换成它 |
| `Testflow (Selection)` + 勾 `Enable 'single step' execution mode` | 同一分支上至少五个 test suite；先选中 Testsuite_1 与 Testsuite_3 | **Testsuite_3 执行，然后整个执行终止** |
| `Testflow (Selection)` + single step + `Loop` + `Loop Indefinitely` | 同上 | 再执行一个 test suite 并等待；按钮多一个 `Suspend`，可以一轮轮手动走 |
| `Testflow (User Defined)` + 选 Testsuite(s) or Group(s) + single step | 同上 | 同上；**没选 Testsuite(s)/Group(s) 之前，Single Step Execution 那一区是灰的、`Whole Flow` 是开着的** |

**四份都写着同一句收尾**：

> 「In all cases the testflow execution terminates before the execution of test suite Testsuite_5.」

**控制按钮（原文在每份里各重复一遍）**：`Resume` 不停继续、`Step Over` 只走下一个 test suite、
`Terminate` 中止、循环配置下另有 `Suspend`。原文对第一种起法单写了一句：

> 「Starting with Run and Hold testflow execution you can seamlessly continue testflow debugging using the Step Over button.」

**四份合起来只有一句操作要点值得单独记**：**单步只在 step mode 打开的 run configuration 下有效**——
不是随时按一下 `Step Over` 就能走。

## 和谁有关

**入边 22 条 / 16 篇**（`inline` 口径，`extract/edges.jsonl`）。引用它的文档分三类：

- **导航与总表**：`01.01.11.01_93000_menu_and_its_tools`、`02.08.02_93000_menu_and_its_tools`、
  `02.08.03_Tools_grouped_by_function`、`02.08.04_Tools_in_alphabetical_order`——
  **它是「按功能查工具」表里的一个条目**。
- **主线任务页**：`02.08.01.01.04_Task_4__Setting_up_a_Test`、
  `02.08.01.01.05_Task_5__Executing_a_Test_and_Obtaining_the_Results`、
  `01.07.01_Testing_a_basic_digital_device`——**「建测试」这条主线走到 testflow 时指向它**。
- **各处提一句「在 Testflow Tool 里改」的页**：testflow 文件（`02.08.04.32.03.05`，第 125 行）、
  flag 字母表（`02.08.04.32.01.02.07.01`）、MTP 的开发流程页（同一篇 4 处）、`TESTNUMBER`（3 处）。

**入边里有一处特别值得记**：`02.01.02_V93000_Components_and_Compatibility` 引它时，
**链接文本写的是 `flow edit and debug tools`**——那是语料对它的定位：**流程编辑与调试工具**。

**出边只有 3 条**，就是 `#### Subtopics` 那三支。

- [[testflow]] — 本页 `stage: testflow`；那页是本阶段的脊椎，本页是它底下 GUI 工具那一格
- [[flow-sequence-editor]] / [[flow-data-editor]] — Testflow Tool 里的两个编辑器；
  **它们的定义文档与本页平级，不是本页的子页**。本页语法节里两者都出现过，
  但**「Testflow Tool 由哪几个编辑器组成」这句话本篇没写**
- [[testflow-file]] / [[testflow-master-file]] — 本页语法节里那两份格式的落点
- [[test-suite]] / [[bin]] / [[flags-page]] / [[flow-control-node]] — 本页编排的对象
- [[hardware-response-emulator]] / [[hardware-response-file]] — 没有硬件时把流程跑起来的那一套，在语法节里
- [[testflow-analyzer-tool]] / [[testflow-properties-view]] — 同章并列的另外两个 testflow 工具，
  **本页没读它们的文档**
- [[run]] / [[report-window]] / [[debug-view]] — 语法节里那几段讲的正是它们：怎么跑、消息打到哪、
  单步时那棵树长什么样
- [[mapping-testflow]] — 同阶段的对照表页；**它把本页当成 GUI 侧的那一格引用**

## 版本

**本篇的 `## Functional changes` 只有一条**：

- `Introduced before SmarTest 6.3.2`

> ⚠️ **这是一条哨兵值，不是「6.3.2 新增了 Testflow Tool」。**
> 措辞是 `before`——意思是「**在本文档集覆盖范围开始之前就已经有了**」（`schema.md` §11.2②）。
> **照字面读会生成一条假信息**（「6.3.2 新增」）。本页不把它当作 6.3.2 的变更。

**本页语法节里没有任何版本条目**——脚本只抽 `Syntax` / `Parameters` / `Example` 三种段标记，
`## Functional changes` 不在其中。**所以本页 `## 版本` 只有上面那一条。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32_Testflow_Tool.md`
（TDC `91667.htm`，18 行 / 562 字节）——**本页读到的全部正文就是那句定义 + 三条子主题 + 一条版本记录**。

**本页没做的**：

- **三支子主题一篇没读**：`02.08.04.32.01_Introduction_of_the_Testflow.md`、
  `02.08.04.32.02_Using_the_Testflow_Tool.md`、`02.08.04.32.03_Elements_of_the_Testflow_Tool.md`。
  **语法节头里点名的那 14 篇下游子主题同样一篇没读**
  （`01.02.02_Flow_control_nodes`、`01.02.06_Bins`、`01.03_Hierarchy_within_a_testflow`、
  `01.05_Configuring_the_messages_printed_in_the_Report_Window`、
  `02.01.05_Inserting_a_bin_into_the_testflow`、`02.01.14_Identifying_fail_labels_in_a_burst`、
  `02.01.16_Exporting_a_testflow_to_a_CSV_file`、`02.03.04_Measuring_the_test_time`、
  `02.04.01_Single_step_testflow_debugging`、`02.06.02_Using_hardware_response_files_for_execution`、
  `02.06.03_Hardware_response_files`、`03.01.05_Variables_page`、`03.05_Testflow_file`、
  `03.06_Testflow_master_file`）。
  **所以「是什么」里那张分支表是按语法节里已经写着的段名归类的，不是读出来的。**
- **图 11 张全看了**（`110643`、`110644`、`110985`、`110991`、`125021`、`21635`、`345529`、
  `345530`、`345531`、`94560`、`94561`），逐张结论在「是什么」的图证表里。**不是「本页没用图」。**
- **上面图证表里那些「0 命中 / 有命中」，是本页拿那些串去全语料 grep 得到的一次检索结果**，
  **不是本页 `sources:` 里的内容**——写出来只是为了说清「图里的字搜不搜得到」（§11.4 的 ④ 档要求）。
- **「典型用法」是从语法节里那四份 Specification 拼的**——本篇没有 `## Procedure` 可读。
- **没有实跑**：没开过 Testflow Tool、没做过单步、没配过 `.testflow.ReportUiOutput.user_def`、
  没用过 Hardware Response Emulator。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有改 `wiki/stages/testflow.md`。

> ⚠️ **本页读到的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> ① **单步调试那四份 Specification 里有两份自相矛盾。** `Run selected (loop)` 与
> `Run custom testflow` 两份都写着
> `Test suite Testsuite_2 is executed and execution is waiting.`，紧接着下一行却是
> `The Ftest (Testsuite_1) child entry changes to the Ftest (Testsuite_3).`
> ——**执行的是 Testsuite_2，树里换成的却是 Testsuite_3**。而 `Run selected` 那份写的是
> `Test suite Testsuite_3 is executed and execution is terminated.`
> **同一批前提、同一个选中（Testsuite_1 与 Testsuite_3），三处写的不是一件事。本页并列，不替它调和。**
>
> ② **前提句里多一个逗号，出现两次**：
> `Testflow contains at least five test suites in the same branch. Testsuite_1, Testsuite_2, Testsuite_3, , Testsuite_4, and Testsuite_5.`
>
> ③ **`Run custom testflow` 那份，配置名与 Debug view 里的节点名对不上**：它让你建的是
> `Testflow (User Defined)`，紧接着写的却是
> `The Debug view opens, showing the execution node Testflow (Selection) with the child entry Ftest (Testsuite_1).`
>
> ④ **`Ftest`（正文）对 `FTest`（`125021.png` 图里）**——大小写不一致，见图证表。
> **`Ftest` 全语料只出现 1 次，就是这一句。**
>
> ⑤ **`Unburst`（正文）对 `UnBurst`（`110991.png` 图里）**——同上。**`UnBurst` 全语料 0 命中。**
>
> ⑥ **行的名字两套**：正文那一句是
> 「the `seq setup` and `test suite exec.` rows」（原文里两个行名各自带反引号），
> 而 `94560.png` 里的行标签是 `testsuite exec. (non opt.)`、`94561.png` 里是
> `testsuite execution (opt.)`。
>
> ⑦ **「按 testflow 文件里的顺序排列」这句话与两张图对不上。** 正文写的是
> `The test suites are ordered as they are defined in the testflow file.`，
> 而同一段的例子里 testflow 的顺序是 `cont` 在前 `func` 在后
> （`A simple testflow comprises two test suites, cont and func, in this order.`），
> **`94560.png` 与 `94561.png` 打印的都是 `Testsuite func:` 在前、`Testsuite cont:` 在后**。
> **本页并列两说，不替它选一个。**
>
> ⑧ **Report Window 三份配置例里，中间那份的占位符多一个空格**：另两份写
> `<passed>Site: %site -> Bin: %bin -> PASS (Cool)` 与 `<failed>TestSuite: %testSuiteName -> Site: %site -> FAIL`，
> 中间那份写的是 `<failed>Site : %site -> Bin: %bin -> FAIL (Bad)`。
> `345530.png` 里那一行读得出 `Site: 5`，但**冒号前到底有没有空格，这个分辨率下本页判不了**——
> §13.1 第 6 问：**别把图的分辨率当成语料的事实。**
>
> **本页（含脚本生成的语法节）0 处编码坏字**（`碌` / `渭` / `卤` / `惟` / `鈥` 那几族逐个查过），
> **0 处 `DC/DC power units`**（§11.2⑤ 那一族）。

`verified: doc-only`
