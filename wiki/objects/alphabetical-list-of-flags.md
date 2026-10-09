---
type: object
title: Alphabetical list of flags
layer: L3
stage: testmethod
tags: [flag, testflow, test-suite, data-logging, site-control, results]
related: [flag, flags-page, testflow-file, testflow-properties-view, testflow, bin]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Alphabetical list of flags

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **34,133 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Name in GUI<br><br>Keyword | Area | Description | Default |
|---|---|---|---|
| #1 …#n<br><br>site_control | Site control | These values define the site test sequence if flag `Site Control`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_site_control`） is set to OTHER.<br><br>n = Number of defined sites. |  |
| Allow Parallel<br><br>force_serial | Site control | Determines whether a test suites is executed in parallel or serially. on Test suite is executed in parallel. off Test suite is executed serially. The flag force_serial is inserted in the list of site control parameters if Allow Parallel has been set to off.<br><br>For additional information, see section `Additional information: Allow Parallel (force_serial)`（raw: `02.08.04.32.01.02.07.05_Site_control_flags.md#_100324__s_force_serial`） in `Site control flags`（raw: `02.08.04.32.01.02.07.05_Site_control_flags.md`）. | on |
| buffer_testflow_log<br><br>buffer_testflow_log | Testflow | Controls whether the data log is buffered until the end of the testflow.<br><br>on (1) Enable data log buffering. off (0) Disable data log buffering.<br><br>This is an option for event data logging. The flag allows you to temporarily buffer the data log, then carry all the logged data in the buffer into the event data log stream at the end of the testflow. This way you can minimize the overhead time of the data logging. The details and order of the logged data with this option are the same as of the general event data logging.<br><br>For optimized throughput, set the flag to off. | off (0) |
| Bypass<br><br>bypass | Test suite | The test suite is bypassed. The result is assumed as passed, unless either the `set_fail`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_set_fail`） flag is also activated, or the test suite has a test level which is regarded as a fail level.<br><br>on Bypass the test suite. off Execute the test suite.<br><br>See also testflow flag `set_bypass_level`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_set_bypass_level`）. | off |
| calib_age_monitor<br><br>calib_age_monitor | Data logging | Controls whether the monitor process checks the calibration data age when the application model command `MONITOR_CALL`（raw: `../02.09_Test_Program_Management/02.09.01.02.05.02.40_MONITOR_CALL.md`） is executed. on (1) Enable calibration data age check. off (0) Do not check calibration date age. For optimized throughput, set the flag to off. | on (1) |
| check_testmethod_api<br><br>check_testmethod_api | Testflow | Controls whether undefined pin names cause fatal errors.<br><br>on (1) Checks the pin name parameter. off (0) Pin name parameter is not checked.<br><br>For additional information, see section `Additional information: check_testmethod_api`（raw: `02.08.04.32.01.02.07.02_Testflow_flags.md#_20312__s_check_testmethod_api`） in `Testflow flags`（raw: `02.08.04.32.01.02.07.02_Testflow_flags.md`）.<br><br>Check Test Method API flag should be set to "on" if Standard Test Data Format (STDF) will be used for test result data analysis.<br><br>For optimized throughput, set the flag to off. | off (0) |
| current_monitor<br><br>current_monitor | Data logging | Controls whether the monitor process checks other power supply mode when the application model command `MONITOR_CALL`（raw: `../02.09_Test_Program_Management/02.09.01.02.05.02.40_MONITOR_CALL.md`） is executed. on (1) Enable check of the power supply mode. off (0) Disable check of the power supply mode. For optimized throughput, set the flag to off. | on (1) |
| datalog_formatter<br><br>datalog_formatter | Data logging | Enables or disables the Data Bridge calls in the application model that pipe all logged data (in generic data format) to the a data formatter. on (1) Enable the Data Bridge calls. off (0) Disable the Data Bridge calls. For optimized throughput, set the flag to off. | off (0) |
| datalog_sample_size<br><br>datalog_sample_size | Data logging | Determines the number of devices to be tested before logging data. n Number of devices<br><br>- Minimum: 1<br>- Maximum: 9999<br><br>For example, a data log sample size of 100 results in only the data for each 100th device being logged. Such a feature is useful in statistical process control. The default sample size is 1 (that is, results for every device are logged). | 1 |
| debug_analog<br><br>debug_analog | Testflow | Activates or deactivates support for debugging analog tests. on (1) The test method debugger is launched after the execution. off (0) No analog debug information will be generated.<br><br>If you turn this flag on when developing multisite testing by using an analog module that is shared amongst multiple sites, the system will check the routing inconsistency before a test execution. | off (0) |
| debug_mode<br><br>debug_mode | Testflow | The Debug Mode flag enables debug information collection and provides the controls to select the level of debug information to be displayed in the `Report window`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.md`） during debug execution. For information about debugging, see `Debugging a testflow`（raw: `02.08.04.32.02.04_Debugging_a_testflow.md`）. 0 (Debug off) (0) No debug information is shown. 1 (Display actions) (1) Display actions: All actions performed are displayed in the report window.If logging to the MCDLog file is enabled, every executed testflow is logged to the file, too (see `Using the Trace Function`（raw: `../02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.md`）).<br><br>In online mode, the time required for downloading the patterns is also shown.<br><br>2 (Display results) (2) The results of all the test suites that have been executed are displayed in the report window. 3 (Display execution time) (3) The following information will be displayed in the report window:<br><br>- The total execution time<br>- Detailed information for each test level, including preaction, sublevel, postaction and data log times<br>- The number of devices tested<br>- The execution times for each test suite<br>- The execution time of each test suite to be displayed in the respective test suite node.<br>4 (Display SmarTime) (4) Displays a list of testsuite execution times in the order of execution.<br><br>The following information is displayed in the report window:<br><br>- Execution time of each test suite<br>- Number of devices tested<br>- Average execution time of all executed testflow executions<br>- Total execution time of each test suite<br>- For second execution: Additional columns with second execution times and sum of execution times<br>- For more than two executions: Additional columns with minimum and maximum execution times and the times for the most recent execution. | 0 (Debug off) (0) |
| diag_monitor<br><br>diag_monitor | Data logging | Controls whether the monitor process checks the diagnostics state when the application model command `MONITOR_CALL`（raw: `../02.09_Test_Program_Management/02.09.01.02.05.02.40_MONITOR_CALL.md`） is executed. on (1) Enable check of the diagnostics state. off (0) Disable check of the diagnostics state. For optimized throughput, set the flag to off. | on (1) |
| dsp_file_enable<br><br>dsp_file_enable | n/a | Legacy flag<br><br>Do not use for new device test programs. | n.a. |
| Fail per label<br><br>fail_per_label | Test suite | If the executed label is a burst, then setting this flag configures the overview error map to record one result for every label of the burst. This allows you to identify the failing labels of the burst. The error map is configured to use the LMAP mode (see the `mode`（raw: `../02.06_Command_Reference/02.06.02.02.46_DCRM__DCRM__-__Digital_Compare_Result_Mode.md#_98524__row_mode`） parameter of `DCRM, DCRM? - (Digital Compare Result Mode)`（raw: `../02.06_Command_Reference/02.06.02.02.46_DCRM__DCRM__-__Digital_Compare_Result_Mode.md`）) when this flag is set. This results in 8 to 15 break vectors being added, see illustration in the topic `Pass/Fail per label without break vectors`（raw: `../02.07_Test_Method_Reference/02.07.13.08.09.02_Pass_Fail_per_label_without_break_vectors.md`）. on Record one result for every label of the burst off Disable | off |
| Fail value<br><br>value_on_fail | Test suite | Determine whether the test suite returns the actual fail value. This flag needs the `Output on fail`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_output_on_fail`） test suite flag to be activated. on Enable off Disable | on |
| FFC enable<br><br>ffc_enable | Test suite | Enables or disable logging of the first failing cycles (the first cycles to give an error) for the test suite. on Enables logging of the first failing cycles. off Disable logging of the first failing cycles. | off |
| FFV enable<br><br>ffv_enable | Test suite | A subflag of `ffc_enable`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_ffc_enable`）: Enables or disables logging of the first failing vectors (the first vectors to give an error) for the test suite. on Enables logging of the first failing vectors. off Disable logging of the first failing vectors. | off |
| FRG enable<br><br>frg_enable | Test suite | A subflag of `ffc_enable`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_ffc_enable`）: Enables or disables the fine result granularity. on Enable the fine result granularity. off Disable the fine result granularity.<br><br>If a cycle contains more than one receive strobe the fine result granularity enables you to get result information per receive strobe. If this flag is disabled you only get result information per cycle. There is no information at which strobes of the cycle the failures occurred.<br><br>Note that this flag must not be set for test suites that execute protocol-aware tests. | off |
| global_hold<br><br>global_hold | Testflow | Setting this flag allows you to execute the test suites step by step. The test system goes into a hold state whenever a test suite has been executed. on (1) Execute the test suites step by step. off (0) Do not activate the hold state.<br><br>For additional information, see section `Additional information: global_hold`（raw: `02.08.04.32.01.02.07.02_Testflow_flags.md#_20312__s_global_hold`） in `Testflow flags`（raw: `02.08.04.32.01.02.07.02_Testflow_flags.md`）.<br><br>We recommend using the single step procedure for testflow debugging.<br><br>For optimized throughput, set the flag to off. | off (0) |
| global_overon<br><br>global_overon | Testflow | Setting this flag allows the testflow to continue when stop bins are marked as overon bins. on (1) The Bin Overon flag determines the system behavior. When the Bin Overon is on, the testflow execution continues. When the Bin Overon is off, the testflow execution stops at that bin. off (0) The testflow execution stops when a fail bin is reached. For more information, refer to `Overon flag`（raw: `../02.10_Data_Logging/02.10.03.03.05_Overon_flag.md`）.<br><br>For optimized throughput, set the flag to on. | off (0) |
| graphic_result_display<br><br>graphic_result_displa | Data logging | Controls whether the binning result is displayed graphically after each testflow execution. Depending on your application model , the Wafermap Screen or the Result Display Screen for a package test will be shown as long as the state of the flag is on (default state). on (1) Enable off (0) Disable For optimized throughput, set the flag to off. | on (1) |
| H/L/I/U (multiple execution)<br><br>frg_single_shot | Test suite | A subflag of `frg_enable`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_frg_enable`）: Enables or disables the multishot per-edge detailed result mode (high / low / intermediate / unclear). on Enable (Flag frg_single_shot is deleted) off Disable (Flag frg_single_shot is inserted) | off |
| Hardware DSP disable<br><br>hw_dsp_disable | n/a | Legacy flag<br><br>Do not use for new device test programs. | n.a. |
| hidden_datalog_mode<br><br>hidden_datalog_mode | Data logging | Enables compatible or full hidden data logging mode provided by the `SmartCalc framework`（raw: `../02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.md`）. 0 (off) (0) Turns hidden data logging off. 1 (on - compatibility mode) (1)<br><br>Turns hidden data logging in compatibility mode on.<br><br>In this mode, the limits are used that are defined in the `SMC_SYNCHRONIZE()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.231.43_SMC_SYNCHRONIZE.md`） test suite.<br><br>2 (on - full hidden mode) (2)<br><br>Turns full hidden data logging on, including `LIMIT`（raw: `../02.07_Test_Method_Reference/02.07.04.01.126_LIMIT.md`） support.<br><br>In this mode, the limits are used that are defined by the calling test suite.<br><br>This is the recommended mode.<br><br>Note that activating the hidden mode (value 1 or 2) may cause missing or unexpected data log entries when you interactively execute test suites based on the SMC framework. We therefore recommend that you do not activate hidden data logging in this case.<br><br>When you are using the concurrent test framework, the hidden_datalog flag also determines whether the test events are logged separately for each test suite (if the flag is turned on) or all events are logged together in the final CCExecution test suite (if the flag is turned off). | 0 (off) (0) |
| hold_on_fail<br><br>hold_on_fail | Testflow | If you set this flag, the testflow will be put to a "hold" state every time a test suite fails. A window then lets you select whether to continue or abort the testflow. on (1) Hold if a test suite fails. off (0) Continue if a test suite fails.<br><br>For additional information, see section `Additional information: hold_on_fail`（raw: `02.08.04.32.01.02.07.02_Testflow_flags.md#_20312__s_hold_on_fail`） in `Testflow flags`（raw: `02.08.04.32.01.02.07.02_Testflow_flags.md`）.<br><br>For optimized throughput, set the flag to off. | off (0) |
| Hold<br><br>hold | Test suite | The testflow is paused after the particular test suite has been executed. on Pause after the test suite has been executed. off Continue the testflow.<br><br>For additional information, see section `Additional information: hold and Hold on fail`（raw: `02.08.04.32.01.02.07.04_Test_suite_flags.md#_20262__s_hold_and_hold_on_fail`） in `Test suite flags`（raw: `02.08.04.32.01.02.07.04_Test_suite_flags.md`）. | off |
| Hold on fail<br><br>hold_on_fail | Test suite | The testflow is paused if the test suite fails. on Pause if test suite has failed. off Continue the testflow.<br><br>For additional information, see section `Additional information: hold and Hold on fail`（raw: `02.08.04.32.01.02.07.04_Test_suite_flags.md#_20262__s_hold_and_hold_on_fail`） in `Test suite flags`（raw: `02.08.04.32.01.02.07.04_Test_suite_flags.md`）. | off |
| ink_wafer<br><br>ink_wafer | Data logging | Used to communicate to the wafer prober whether it will ink dies according to the test results. SmarTest does not take any actions depending on the flag value: off (0) Do not ink the die. delay (1) Ink the die later, for example, when the wafer is put back into the cassette. on (2) Ink the die immediately. offline (3) Ink after testing. For optimized throughput, set the flag to off. | off (0) |
| limits_enable<br><br>limits_enable | Testflow | Control whether the pass/fail limits of each test suite are logged (In addition to the pass/fail results). on (1) Enable logging of pass/fail limits. off (0) Disable logging of pass/fail limits.<br><br>If activated, the actual absolute limits during runtime of a test suite containing variables are recorded in the data log, together with information on the primary sets and labels used. This way you can tell what particular level or timing conditions a test suite passed or failed. This is especially useful when using variables and the Equation System to specify setup and pass/fail conditions.<br><br>For optimized throughput, set the flag to off. | off (0) |
| log_cycles_after<br><br>log_cycles_after | Testflow | This parameter determines how many cycles after a failed cycle are logged. n Number of cycles<br><br>- Minimum: 0<br>- Maximum: 9999<br>For optimized throughput, set the value to 0. | 0 |
| log_cycles_before<br><br>log_cycles_before | Testflow | This parameter determines how many cycles before a failed cycle are logged. n Number of cycles<br><br>- Minimum: 0<br>- Maximum: 9999<br>For optimized throughput, set the value to 0. | 0 |
| log_events_enable<br><br>log_events_enable | Data logging | Enables or disables event data logging. on (1) Enable event data logging. off (0) Disable event data logging. For examples, see `Activating event data logging`（raw: `../02.10_Data_Logging/02.10.01.01.04_Activating_event_data_logging.md`） and `Setting up the data log information`（raw: `../02.09_Test_Program_Management/02.09.01.17.08_Setting_up_the_data_log_information.md`）.<br><br>For optimized throughput, set the flag to on. | on (1) |
| Log first<br><br>ffc_on_fail | Test suite | A subflag of `ffv enable`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_ffc_enable`）. n The number of first failing cycles to be logged. | 1 |
| Log Mixed Signal Waveforms<br><br>mx_waves_enable | Test suite | Enables or disables logging of mixed signal waveforms for event data logging. on Enable logging of mixed signal waveforms. off Disable logging of mixed signal waveforms. | off |
| max_reprobes<br><br>max_reprobes | Data logging | Controls how often the tester attempts to re-probe a die if a bin has its reprobe flag set. n The maximum number of re-probes:<br><br>- Minimum: 0<br>- Maximum: 9999<br>For optimized throughput, set the value to 1. | 1 |
| multibin_mode<br><br>multibin_mode | Testflow | Controls the handling of multibin calls. default (0) Default mode suppress_on_set_pass (1) Setting this values ignores calls to `SET_MULTIBIN`（raw: `../02.07_Test_Method_Reference/02.07.04.01.212_SET_MULTIBIN.md`） and the setting of the internal multibin variable in `TESTSET().judgeAndLog`（raw: `../02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.md`） and `SMC_SYNCHRONIZE()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.231.43_SMC_SYNCHRONIZE.md`） calls when the `set_pass`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_set_pass`） test suite flag is set.<br><br>This flag does not affect:<br><br>- The `set_pass_level`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_set_pass_level`） testflow flag<br>- The `RESET_MULTIBIN`（raw: `../02.07_Test_Method_Reference/02.07.04.01.188_RESET_MULTIBIN.md`） command<br>- The `set_fail`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_set_fail`） test suite flag<br>- `SMC_TEST()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.md`） calls (binning happens in the appended SMC_SYNCHRONIZE call) | default (0) |
| Output on fail<br><br>output_on_fail | Test suite | Determine whether the test suite returns an overall fail message. The flag must be set if you want the output (for example, from a user procedure) sent to the data log file. If the flag is disabled, no value or per-pin measurements will be made. on Output on fail enabled. off Output on fail disabled. | on |
| Output on pass<br><br>output_on_pass | Test suite | Determine whether the test suite returns an overall pass message. The flag must be set if you want the output (for example, from a user procedure) sent to the data log file. If the flag is disabled, no value or per-pin measurements will be made. on Output on pass enabled. off Output on pass disabled. | on |
| parallel_mode<br><br>parallel_mode | Testflow | Controls whether test suites for multiple sites are in parallel or serially. on (1) Execute in parallel. off (0) Execute serially. For optimized throughput, set the flag to on.Note If individual test suites within the testflow have been set for serial testing, then these test suites are executed in serial even if the testflow flag is set to parallel. | on (1) |
| Pass value<br><br>value_on_pass | Test suite | Determine whether the test suite returns the actual pass value. This flag needs the `Output on pass`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_output_on_pass`） test suite flag to be activated. on Enable off Disable | on |
| Per pin on fail<br><br>per_pin_on_fail | Test suite | Determine whether the test suite returns a fail message per pin. This flag needs the `Output on fail`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_output_on_fail`） test suite flag to be activated. on Enable off Disable | on |
| Per pin on pass<br><br>per_pin_on_pass | Test suite | Determine whether the test suite returns a pass message per pin. This flag needs the `Output on pass`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_output_on_pass`） test suite flag to be activated. on Enable off Disable | on |
| print_wafermap<br><br>print_wafermap | Data logging | Controls whether a wafer map is printed after the test of the wafer is finished. For this purpose, the $HP83000_ROOT/prod_com/lbin/pr_wafer script is called. on (1) Print the wafer map. off (0) Do not print the wafer map. For optimized throughput, set the flag to off. | off (0) |
| set_bypass_level<br><br>set_bypass_level | Testflow | This parameter lets you bypass test suites according to their test level. 0 No test suites are bypassed. 1 …9999 All test suites for which the `Test Level`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_test_level`） is equal or greater than the set value will be bypassed. -9999 …-1 All test suites for which the `Test Level`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_test_level`） is equal or less than the set value will be bypassed. For optimized throughput, set the flag to 0. | 0 |
| set_fail_level<br><br>set_fail_level | Testflow | This parameter lets you set test suites to fail according to their test level. 0 No test suites are set to fail. 1 …9999 All test suites for which the `Test Level`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_test_level`） is equal or greater than the set value will be set to fail. -9999 …-1 All test suites for which the `Test Level`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_test_level`） is equal or less than the set value will be set to fail. For optimized throughput, set the flag to 0. | 0 |
| set_pass_level<br><br>set_pass_level | Testflow | This parameter lets you set test suites to pass according to their test level. 0 No test suites are set to pass. 1 …9999 All test suites for which the `Test Level`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_test_level`） is equal or greater than the set value will be set to pass. -9999 …-1 All test suites for which the `Test Level`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_test_level`） is equal or less than the set value will be set to pass. | 0 |
| Set fail<br><br>set_fail | Test suite | Force the test suite to fail. on Force the test suite to fail. off Do not change the state of the test suite. | off |
| Set pass<br><br>set_pass | Test suite | Force the test suite to pass. on Force the test suite to pass. off Do not change the state of the test suite. | off |
| Site match mode<br><br>site_match_mode | Testflow | Controls whether site matching is performed. off (0) This state means all sites will be started simultaneously (synchronously). on (1) The on state means all sites will be started successively (with a slight delay). auto(on) (2)<br><br>If the pin configuration does not have the definitions of any shared analog or digital modules, this setting is selected.<br><br>This is same as "on".<br><br>This setting is active when an automatic setting and a `narrow test suite selection`（raw: `02.08.04.32.02.01.11.01_Narrow_selection_and_wide_selection.md`） was chosen.<br><br>auto(off)<br><br>If the pin configuration has the definitions of any shared analog or digital modules, this setting is selected.<br><br>This is same as "off".<br><br>This setting is active when an automatic setting and a `wide test suite selection`（raw: `02.08.04.32.02.01.11.01_Narrow_selection_and_wide_selection.md`） was chosen.<br><br>For optimized throughput, set the flag to off.<br><br>For testing more than 255 sites at the same time, set the flag to off; otherwise, an error message will be generated.<br><br>Note If the site match mode of individual test suites within the testflow has been set by the Site Match test suite flag, then these test suites are executed according to the settings of the test suite flag regardless of the setting of this testflow flag.CAUTION You must turn off site matching when sharing BADCs over sites, to ensure proper pattern-controlled DC value measurements with the BADCs.<br><br>For more information, refer to `Controlling the site match function`（raw: `../02.06_Command_Reference/02.06.03.01.10.04_Controlling_the_site_match_function.md`）, `Controlling Site Synchronization`（raw: `../../03_Use_cases_and_application_papers/03.02_How_to_do_Multi-Site_Testing/03.02.02.06.09_Controlling_Site_Synchronization.md`） and `Multi-Site Synchronization in a multiport Setup`（raw: `../../03_Use_cases_and_application_papers/03.02_How_to_do_Multi-Site_Testing/03.02.02.06.09.01_Multi-Site_Synchronization_in_a_multiport_Setup.md`）. | off (0) |
| Site Control<br><br>site_control | Site control | Controls which sites will be executed in parallel, semi-parallel or serial mode. PARALLEL The test suite is executed in parallel. SERIAL The test suite is executed serially. SEMIPARALLEL The test suite is executed in a semi-parallel manner.<br><br>Parameters `Size and Cycle`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_size_cycle`） are to be defined if the flag is set to SEMIPARALLEL.<br><br>Note We recommend using the test method APIs `FOR_SEMI_PARALLEL_TEST_BEGIN`（raw: `../02.07_Test_Method_Reference/02.07.04.01.73_FOR_SEMI_PARALLEL_TEST_BEGIN.md`） and `FOR_SEMI_PARALLEL_TEST_END`（raw: `../02.07_Test_Method_Reference/02.07.04.01.74_FOR_SEMI_PARALLEL_TEST_END.md`） for semi-parallel or customer-defined sequences. OTHER The test suite is executed serially or semi-parallel in a customer-defined sequence.<br><br>Parameters `#1 ... #n`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_site_sequence`） are to be defined if the flag is set to OTHER.<br><br>Further information is available in `Expanded Site Control window`（raw: `02.08.04.27.02_Expanded_Site_Control_window.md`）, `Testflow Properties view`（raw: `02.08.04.32.03.04_Testflow_Properties_view.md`） and `Controlling Multiple Sites`（raw: `../02.07_Test_Method_Reference/02.07.03.13_Controlling_Multiple_Sites.md`）. | PARALLEL |
| Site Match<br><br>site_match | Site control | Is used for multisite testing using the analog modules that are shared with multiple sites.<br><br>AUTO Enable auto-setting depending on the pin configuration definitions. on All sites will be started successively (with a slight delay). off All sites will be started simultaneously (synchronously). CAUTION You must turn off site matching when sharing BADC(s) over sites, to ensure proper pattern-controlled DC value measurements with the BADC.For more information, refer to testflow flag `site_match_mode`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_site_match_mode`） in this table. | AUTO |
| Size, Cycle<br><br>site_control | Site control | Size and Cycle define the site test sequence if flag `Site Control`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_site_control`） is set to SEMIPARALLEL.<br><br>Refer to `Size & Cycle`（raw: `02.08.04.27.02_Expanded_Site_Control_window.md#_100119__row_Size_Cycle`） and the examples in `Expanded Site Control window`（raw: `02.08.04.27.02_Expanded_Site_Control_window.md`） for information on how to set these parameters.<br><br>Note: Parameter Cycle may be set to unbounded in the `Expanded Site Control window`（raw: `02.08.04.27.02_Expanded_Site_Control_window.md`）. The corresponding value in the `Testflow file`（raw: `02.08.04.32.03.05_Testflow_file.md`） or in the `Test suite properties view`（raw: `02.08.04.32.03.04_Testflow_Properties_view.md#_99279__s_Test_suite_properties_view`） is -1.<br><br>In the `Testflow file`（raw: `02.08.04.32.03.05_Testflow_file.md`）, these values are appended to flag `Site Control`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_site_control`） as parameters. | Not defined |
| sqst_mode<br><br>sqst_mode | Testflow | Controls overriding user-defined break waveforms to debug tests that pass standalone but not in a testflow. on (1) The user defined break waveforms are temporarily overridden and the drivers are set to tri-state mode between all tests in the testflow. off (0) The user defined break waveforms are not overridden.<br><br>You may encounter tests that pass when executed as standalone but may fail when executed within a testflow. A glitch on the drivers may be present between pattern bursts when viewed with an oscilloscope. If you experience this situation, check the sqst_mode testflow flag.<br><br>Set to off in typical applications to avoid side effects with keep alive and test time.<br><br>For optimized throughput, set the flag to off. | off (0) |
| state_display<br><br>state_display | Data logging | Controls whether the tester state (idle, loading, testing, etc.) is displayed in a dedicated state display window. on (1) Display the tester state. off (0) Do not display the tester state. For optimized throughput, set the flag to off. | off (0) |
| stdf_generation<br><br>stdf_generation | n/a | Legacy flag<br><br>Do not use for new device test programs. | n.a. |
| temp_monitor<br><br>temp_monitor | Data logging | Controls whether the monitor process checks tester temperature when the application model command `MONITOR_CALL`（raw: `../02.09_Test_Program_Management/02.09.01.02.05.02.40_MONITOR_CALL.md`） is executed. on (1) Check tester temperature. off (0) Do not check tester temperature. For optimized throughput, set the flag to off. | on (1) |
| test_number_enable<br><br>test_number_enable | Testflow | Controls whether test numbers are logged and verified. off (0) No test numbers from the test suite are used for data logging. on (1) Test numbers from the test suite are logged. on + validity check (2) Test numbers from the test suite are logged.<br><br>In addition, SmarTest checks whether a test executed with any of the judgeAndLog... functions (or through the `TEST()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.241_TEST.md`） or `SMC_TEST()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.md`） APIs) has the test number 0, a missing test number, or a test number that has already been assigned to another test.<br><br>If any of these conditions occur, the test suite is stopped with a fail result.<br><br>For optimized throughput, set the flag to on. | on (1) |
| test_number_inc<br><br>test_number_inc | Testflow | The test number increment between loop iterations. n<br><br>Number of increment:<br><br>- Minimum: 0<br>- Maximum: 9999<br><br>For optimized throughput, set the flag to 1.<br><br>For additional information, see section `Additional information: test_number_inc`（raw: `02.08.04.32.01.02.07.02_Testflow_flags.md#_20312__s_test_number_inc`） in `Testflow flags`（raw: `02.08.04.32.01.02.07.02_Testflow_flags.md`）. | 1 |
| Test Level<br><br>test_level | Test suite | An integer (0 …9999) you can assign to a test suite. In combination with the `pass`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_set_pass_level`）, `fail`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_set_fail_level`）, and `bypass`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_set_bypass_level`） levels you set in the testflow flags window, you can control the results from each of your test suites. n Test level | 0 |
| Test Number<br><br>override_test_number | Test suite | Generated by the software if left empty, or follows the expression set by the user. Is only enabled if the testflow flag `test_number_enable`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_test_number_enable`） is set to on. n Integer test number | n/a |
| tm_crash_as_fatal<br><br>tm_crash_as_fatal | Data logging | This flag controls crashes and unhandled exceptions. off (0) All sites of the current test suite are sent to the `otherwise bin`（raw: `02.08.04.32.01.02.06_Bins.md`） if they have not already been binned. All sites include those to be executed and those already executed by the test suite in which the issue happens. on (1) All sites that have not already been binned are aborted and sent to the `otherwise bin`（raw: `02.08.04.32.01.02.06_Bins.md`）. Lot testing is aborted and needs user interaction to restart production. For optimized throughput, set the flag to off. | on (1) |
| unburst_mode<br><br>unburst_mode | Testflow | Controls how burst labels are treated during testflow execution. off (0) All vector labels in the burst label are executed in one run. on fail (1) If a test suite that runs a burst label fails, it is executed again. If the test suite flag `Fail per label`（raw: `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md#_342556__row_fail_per_label`） is set for a test suite that runs a burst, then only the failing labels are re-executed in the second run. on (2) Like on fail, but for each test suite that runs a burst label and for the first execution. Note Setting this flag to on fail or on increases the test time. Normally in a production test environment, the unburst mode flag is set to off.<br><br>For optimized throughput, set the flag to off. | off (0) |
| use_hw_dsp<br><br>use_hw_dsp | n/a | Legacy flag<br><br>Do not use for new device test programs. | n.a. |
| warn_as_fail<br><br>warn_as_fail | Testflow | Controls whether firmware warnings automatically cause a test to fail. on (1) Any firmware warning will be treated as test fail. off (0) Any firmware warning will not be treated as test fail and the testflow will continue.<br><br>Using the flag allows you to treat a firmware warning as either test fail or as just a warning.<br><br>For optimized throughput, set the flag to off. | on (1) |

<!-- 语法节 end -->

## 是什么

**这一页是 testflow tool 里全部 flag 的字母序总表，共 `64` 行**（本页数的；表头 `Name in GUI` 不算）。
原文第一句交代它的范围：

> 「The testflow tool provides access to a range of flags that control numerous aspects of
> testflow execution.」

**读这张表之前必须先懂一条规矩：每个 flag 有两个名字。** 原文：

> 「The following table lists the flags available in the testflow tool in alphabetical order.
> The first column shows two names for the flags:
>
> - The upper value is the name that is shown in the `Flags page` or in the `Test suite properties view` of the `Testflow Tool`.
> - The lower value is the keyword as it is stored in the `Testflow file`.」

| 位置 | 名字 | 出现在哪 |
|---|---|---|
| **上**（`Name in GUI`） | GUI 名 | `Flags page` / `Test suite properties view` |
| **下**（`Keyword`） | keyword | `Testflow file` |

**取值怎么读**，原文紧跟着给了两条：

> 「Values on and off in the description are for the GUI. These values correspond to 1 and 0 in
> the testflow file or APIs. The same applies to other labels of the GUI drop-down lists: These
> labels are represented as integer values in the testflow file or APIs.
>
> - Integer values in brackets are the values used by the testflow file or APIs.」

**所以描述里的 `on (1)` 要读成「GUI 上写 `on`，文件里存 `1`」**，`off (0)` 同理。
**而且不只是 on/off**：下拉框的其它标签（`PARALLEL` / `SERIAL` / `SEMIPARALLEL` / `OTHER` /
`delay` / `offline` / `AUTO` / `default` …）**在文件与 API 里也都是整数**——
这一条是原文第二句明确说的，只记住 on/off 会漏掉一半。

**flag 的状态存在哪**（原文）：

> 「The state of all flags is stored in the `Testflow file`. SmarTest performs a range check of
> parameters when loading the file.」

**`Area` 列把 64 行分成五类**（行数是本页逐行数的，原文没给过这类数字）：

| `Area` | 行数 | 这一类的例子 |
|---|---|---|
| `Testflow` | 21 | `global_hold`、`parallel_mode`、`test_number_enable` |
| `Test suite` | 20 | `set_pass`、`output_on_fail`、`ffc_enable` |
| `Data logging` | 14 | `log_events_enable`、`datalog_sample_size`、`temp_monitor` |
| `Site control` | 5 | `site_control`、`site_match`、`site_match_mode` |
| `n/a` | 4 | 四个 legacy flag |

**`Area` 为 `n/a` 的那 4 行是 legacy flag**，四行的说明逐字都是同一句：

> 「Legacy flag
>
> Do not use for new device test programs.」

四个是 `dsp_file_enable`、`hw_dsp_disable`、`stdf_generation`、`use_hw_dsp`。
**注意它们没有正式名字**——`Name in GUI` 那一格直接写的是 keyword 本身，
其余 60 行则一律有一个人话名字（如 `Hold on fail` / `hold_on_fail`）。

**按 Area 还能找到三篇子页。** 本篇有 **7 处** `For additional information, see section … in …`，
指向 `Site control flags`（`Site control` 类）、`Testflow flags`（`Testflow` 类）、
`Test suite flags`（`Test suite` 类）三篇。**`Data logging` 与 `n/a` 两类没有对应的子页**
（推断：这是本页从这 7 处链接分布看出来的，原文没有一句话这么归纳）。

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
这是一张**参考表**，「怎么用」只能从每行的描述里读。但有一句口径在整篇里反复出现，
**这是本页最实用的一条经验**：

> 「For optimized throughput, set the flag to off.」

**这句在本篇出现 `29` 次**（本页数的），另有变体
`For optimized throughput, set the value to 0.` / `set the value to 1.` /
`set the flag to 0.` / `set the flag to on.`。
**出现次数本身就是信息：绝大多数 flag 的生产口径是关掉。**

**原文明确点名要「开」的只有这几处**（逐字引）：

| 行 | 原文 |
|---|---|
| `global_overon` | `For optimized throughput, set the flag to on.` |
| `log_events_enable` | `For optimized throughput, set the flag to on.` |
| `parallel_mode` | `For optimized throughput, set the flag to on.` |
| `test_number_enable` | `For optimized throughput, set the flag to on.` |
| `check_testmethod_api` | `Check Test Method API flag should be set to "on" if Standard Test Data Format (STDF) will be used for test result data analysis.` |
| `hidden_datalog_mode` | `This is the recommended mode.`（指取值 `2 (on - full hidden mode) (2)`） |

**几条带前置 / 连带关系的用法**（全部逐字引自对应行）：

- **一个 flag 依赖另一个**（本篇有 4 处 `This flag needs the … to be activated.`）：
  `Fail value` 与 `Per pin on fail` 需要 `Output on fail` 打开；
  `Pass value` 与 `Per pin on pass` 需要 `Output on pass` 打开。
- **父子关系**（本篇有 4 处 `A subflag of …`）：`ffv_enable` 与 `frg_enable` 是 `ffc_enable` 的子 flag；
  `H/L/I/U (multiple execution)` 是 `frg_enable` 的子 flag；`Log first` 那一句**原文写坏了**（见「出处」⑦）。
- **`Bypass` 会往别的参数里塞东西**：原文
  `The flag force_serial is inserted in the list of site control parameters if Allow Parallel has been set to off.`
- **`Test Number` 依赖 `test_number_enable`**：原文
  `Is only enabled if the testflow flag test_number_enable is set to on.`
- **跨对象打架时谁赢**：原文
  `Note If individual test suites within the testflow have been set for serial testing, then these test suites are executed in serial even if the testflow flag is set to parallel.`
- **`site_match_mode` 有一条硬上限**：原文
  `For testing more than 255 sites at the same time, set the flag to off; otherwise, an error message will be generated.`
  以及两句 `CAUTION`：
  `You must turn off site matching when sharing BADCs over sites, to ensure proper pattern-controlled DC value measurements with the BADCs.`
- **`frg_enable` 有一条禁用场景**：原文
  `Note that this flag must not be set for test suites that execute protocol-aware tests.`
- **`sqst_mode` 什么时候关**：原文
  `Set to off in typical applications to avoid side effects with keep alive and test time.`
- **调试时怎么设**：`global_hold` 行原文
  `We recommend using the single step procedure for testflow debugging.`
- **`unburst_mode` 的代价**：原文
  `Note Setting this flag to on fail or on increases the test time. Normally in a production test environment, the unburst mode flag is set to off.`
- **`Size, Cycle` 的 `unbounded` 在文件里怎么存**：原文
  `Note: Parameter Cycle may be set to unbounded in the Expanded Site Control window. The corresponding value in the Testflow file or in the Test suite properties view is -1.`

**本页的「语法 / 参数」节是空的**——脚本没有从定义文档里找到 `Syntax` / `Parameters` / `Example`
这类段标记，所以一个字都没收（骨架里那段说明写的就是这件事）。
**本节及以下的内容全部来自原文正文，不是那个语法节。**

## 和谁有关

- [[flag]] — **本页是它的清单**。本页给的是「有哪些 flag」；那页给的是 flag 这个对象本身。
- [[flags-page]] — **GUI 里显示这些名字的地方**。原文说 `Name in GUI` 那一行的名字
  `is shown in the Flags page`（**那页本页没读**）。
- [[testflow-file]] — **keyword 的落点，也是状态的落点**。原文两句都指向它：
  `the keyword as it is stored in the Testflow file`、
  `The state of all flags is stored in the Testflow file`，
  并且加载时 `SmarTest performs a range check of parameters`（**那页没读**）。
- [[testflow-properties-view]] — **另一个显示 GUI 名的地方**。原文写的是
  `Test suite properties view of the Testflow Tool`；
  **本页把它当成 [[testflow-properties-view]]**（推断：名字相近，但本页没有打开那页核对标题）。
- [[testflow]] — **持有这些 flag 的对象**。原文第一句主语的 `testflow tool` 就是它
  （**那页没读**）。
- [[bin]] — **`Area` 之外的另一个出口**。`tm_crash_as_fatal` 行两处链接指向
  `otherwise bin`（**那页没读**）。
- `Site control flags` / `Testflow flags` / `Test suite flags`（**均未建、均未读**）—
  本篇 7 处 `For additional information, see section … in …` 指向的三篇子页，
  **按 Area 分组的「详解」都在这里**。
- `Expanded Site Control window`（**未建、未读**）— `Size, Cycle` / `Site Control` 两行的详解页
  （**原文说 `Parameter Cycle` 的 unbounded 在那里设**）。
- 表里链接的一批 API / 命令文档（**均未读**）：`TEST()`、`TESTSET().judgeAndLog`、
  `SMC_SYNCHRONIZE()`、`SMC_TEST()`、`SET_MULTIBIN`、`RESET_MULTIBIN`、`MONITOR_CALL`、
  `DCRM`、`FOR_SEMI_PARALLEL_TEST_BEGIN` / `_END`、`SmartCalc framework`、`LIMIT`。
  **本页只记「哪个 flag 提到了谁」，不写那些页里说了什么。**
- [[results]] / [[log]] — **`Data logging` 那 14 行的下游**。
  **本篇没有一句话把它们与本页连成一条链**（推断，仅指归属）。
- [[smartest-7.1.3]] 等版本页 — **本页「版本」一节里的版本号**。
  **那 9 个版本号（6.3.2 / 6.5.3 / 6.5.4 / 7.1.0 / 7.1.2 / 7.1.3 / 7.1.4 / 7.2.0 / 7.4.5）
  对应的版本页本页一个都没读**（见「出处」）。

## 版本

原文 `## Functional changes` 段共 **17 行**（本页数的）：
**第 1 行是哨兵值**，其余 **16 条**是真版本记录。原文逐字：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.3: Removed rf_cal_interp flag`
- `SmarTest 6.5.4: Removed rf_dembedCal_enable flag`
- `SmarTest 7.1.0: Removed OOC_watch flag`
- `SmarTest 7.1.0: Removed OOC_sample_size flag`
- `SmarTest 7.1.0: Removed FFC scan info enable flag`
- `SmarTest 7.1.0: Removed Hardware DSP disable flag`
- `SmarTest 7.1.2: Removed rf_cal_enable flag`
- `SmarTest 7.1.3: Removed optimized_mode flag`
- `SmarTest 7.1.3: Added hidden_datalog_mode flag`
- `SmarTest 7.1.4: Marked use_hw_dsp and dsp_file_enable as legacy flags`
- `SmarTest 7.2.0: Removed report_to_file flag`
- `SmarTest 7.2.0: Removed report_to_printer flag`
- `SmarTest 7.2.0: Removed datalog_to_file flag`
- `SmarTest 7.2.0: Removed datalog_to_printer flag`
- `SmarTest 7.2.0: Removed datalog_to_report_win flag`
- `SmarTest 7.4.5: Marked stdf_generation as legacy flag`

**第一行要按哨兵值读**（§11.2 ②）：它的意思是
「**在本文档集覆盖范围开始之前就已经有了**」，**不是「SmarTest 6.3.2 新增了这张表」**。
照字面读会造出一条假版本事实，而且格式齐整、很难看出来。

**剩下 16 条的形态很不对称：只有 1 条是加法，其余 15 条全是「删除」或「标记废弃」。**
唯一的加法是 `SmarTest 7.1.3: Added hidden_datalog_mode flag`。
**这张版本表本身就是一份「flag 在缩」的历史。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md`
（`342556.htm`，**36,913 字节 / 624 行——本批 12 页里最长的一篇**，整篇读完）。

**本页没做的：**

- **三篇「Additional information」子页一篇都没读**：`Site control flags`、`Testflow flags`、
  `Test suite flags`（本篇 7 处链接指向它们）。
  **所以「某个 flag 背后到底是什么机制」本页一个字都没有**——
  本页只有**表里那一格描述**所说的话。
- **`Flags page`、`Test suite properties view`、`Testflow Tool`、`Testflow file`、
  `Expanded Site Control window`、`Bins` 这些被链接的页，一篇都没读。**
- **表里指向 API / 命令文档的链接一条都没打开**（`TEST()` / `TESTSET()` / `SMC_SYNCHRONIZE()` /
  `SMC_TEST()` / `MONITOR_CALL` / `SET_MULTIBIN` / `RESET_MULTIBIN` / `DCRM` /
  `FOR_SEMI_PARALLEL_TEST_BEGIN` / `SmartCalc framework` / `LIMIT` 等）。
  **所以「这些 flag 改的是哪一层行为」本页写不了。**
- **`Pass/Fail per label without break vectors` 没读**（`Fail per label` 行引的那篇）。
- **定义文档里没有任何图、没有 `## Errors` 段、没有代码块、没有 `## Application` 段。**
- **本页所有数字都是本页数的**：`64` 行、五类 `Area` 的行数（21/20/14/5/4）、
  `29` 次 `For optimized throughput`、`4` 个 legacy flag、`7` 处 `For additional information`、
  `16` 条版本记录。**原文一处这样的数字都没给。**

> ⚠️ **语料瑕疵，照实记下，一处都没替它改**：
> ① **坏字符（§11.2 ①）共 8 处**，全是同一个形态：`鈥?`。
>    逐字是 `| #1 鈥?#n`、`1 鈥?9999`、`-9999 鈥?-1`（后两个在 `set_bypass_level` /
>    `set_fail_level` / `set_pass_level` 三行里各出现一次）、`An integer (0 鈥?9999)`（`Test Level` 行）。
>    按本仓库既有解法反解，`鈥?` 是**两侧带空格的 en dash** —— 即原文应是 `#1 - #n`、`1 - 9999`、
>    `-9999 - -1`、`0 - 9999`。
> ② **keyword 被截断**：`graphic_result_display` 那一行的 keyword 写成了
>    `graphic_result_displa`（**少了尾字符 `y`**），而同一行的 GUI 名是完整的。
>    逐字：` | graphic_result_display` / 空行 / `graphic_result_displa`。
> ③ **同一个 keyword 出现在多行、且 Area 不同**：
>    `hold_on_fail` 出现 **2** 次（一次 `Area` 是 `Testflow`、默认 `off (0)`；
>    一次 `Area` 是 `Test suite`、默认 `off`）；`site_control` 出现 **3** 次
>    （`#1 鈥?#n` 行、`Site Control` 行、`Size, Cycle` 行）。
>    **所以这张表不能按 keyword 建索引，必须按 GUI 名认行。**
> ④ **默认值的写法不统一**：4 个 legacy 行的 `Default` 格写 `n.a.`，
>    而 `Test Number`（`override_test_number`）行的 `Default` 格写 `n/a`。
>    **`n.a.` 与 `n/a` 两种写法都在原文里。**
> ⑤ **一行里正文与它给的链接标题互相打架**：`Fail per label` 行逐字写
>    `This results in 8 to 15 break vectors being added, see illustration in the topic`
>    而它给的链接标题是 `Pass/Fail per label without break vectors`。
>    —— **正文说「会加 break vectors」，链接标题说「without break vectors」。**
> ⑥ **父子的指针指错了**：`Log first` 行（keyword 是 `ffc_on_fail`）逐字写
>    `A subflag of [ffv enable](<…_row_ffc_enable>)`——
>    **文字写的是 `ffv enable`，链接却指向 `ffc_enable` 那一行。**
> ⑦ **列表里有一个空条目**：介绍两个名字的那段列了两个 bullet，
>    第二个 bullet 的内容之后**又跟了一个只有 `-` 的空 bullet**（原文逐字就是一行 `-`）。
> ⑧ **一行的表格塌了**：`test_number_enable` 行的默认值被拆成了三行
>    （` For optimized throughput, set the flag to on. |`、空行、`on (1)`、空行、` |`），
>    **默认值 `on (1)` 因此不在表里、掉到了表格外面。**
> ⑨ **`## Related information` 三条链接首尾相连，中间没有任何分隔符**，逐字是一整行：
>    `[Testflow file](<…>)[Testflow Properties view](<…>)[Expanded Site Control window](<…>)`。
> ⑩ **版本记录与表本身对不上**：版本说
>    `SmarTest 7.1.0: Removed Hardware DSP disable flag`，
>    **可是 `Hardware DSP disable`（`hw_dsp_disable`）仍然作为一行留在表里**（标着 legacy）。
>    而 `SmarTest 7.1.4: Marked use_hw_dsp and dsp_file_enable as legacy flags`
>    **只点了两个**——表里那 4 个 legacy 行里，`hw_dsp_disable` 被记成「已删除」、
>    `stdf_generation` 到 7.4.5 才被标记。**三种说法并存，原文不调和。**
> ⑪ **单复数与标点**：`Allow Parallel` 行逐字 `Determines whether a test suites is executed
>    in parallel or serially.`（`a test suites`）；同行 `on Test suite is executed in parallel.`
>    取值与解释之间**没有标点也没有换行**。**这一形态在整张表里到处都是**
>    （如 `on Enable off Disable`），不是个别行的问题。

`verified: doc-only` —— **本页的 64 个 flag 没有在任何真实机台上设过**
（§11：文档里有 ≠ 这台机器上能用）。
