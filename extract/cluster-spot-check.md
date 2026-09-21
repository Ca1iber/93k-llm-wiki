# 簇抽样核对表

共 **101** 簇，这里摊开 **15** 个（等距抽样）。

> 第一到第五类全是数字检验。**这一份要人真的看一眼。**

## 先说清楚「同一主题」不是判据

簇是**打包单位**，不是主题单位。合并步骤按体量把相邻的兄弟装在一起，必然跨子主题——这在任何层级都一样（`02.07.04.01.14.x` 和 `.27x` 也是互不相干的函数，只因同属一章就被装进一个簇）。

试过用规则把它们分开：按「章号级不合并」改，簇数从 **101 涨到 1,046**、中位掉到 1,361 token，而且 `99_Unlisted`（248 篇文档号当章节用）会碎成248 个单篇簇。**代价 10 倍，换不到任何东西**（见下）。

**因为页面归属不靠簇决定**：一个对象页由「定义它的那篇文档」所在的簇拥有，而切分是一个划分——每篇文档恰好在一个簇里，所以每个对象页的属主唯一，跨章打包不会让两个簇去写同一页。

## 这一份是给人翻的，不是给人判的

「有没有该在一起的文档被切散」——**这一条已经由第六类穷举判完了**，不需要人看：语料里每个前缀节点都算过体量，读得下的一个都没被拆。

人眼在这里本来也判不了：光看簇内文档标题，看不出某篇的邻居是不是在隔壁簇。而人眼**看得出的**那条（同簇文档是不是同一件事），上面说了，不是判据。

所以下面是给人**浏览**用的——想确认某批文档被分到哪去了，直接翻。
要判「某篇的归属合不合理」，正确的做法是查它的分类号父节点在第六类里是绿的，而不是读这张表。

## 全 101 簇索引

| id | prefix | 篇 | token | 源自 | span2 |
|---|---|---|---|---|---|
| `c0001` | `00` | 1 | 379 | `subtree` | 1 |
| `c0002` | `01` | 121 | 86,831 | `merged` | 9 |
| `c0003` | `01.01` | 134 | 99,704 | `merged` | 1 |
| `c0004` | `02` | 88 | 85,747 | `merged` | 2 |
| `c0005` | `02` | 36 | 40,054 | `merged` | 2 |
| `c0006` | `02` | 137 | 81,358 | `merged` | 2 |
| `c0007` | `02` | 229 | 66,014 | `merged` | 2 |
| `c0008` | `02` | 198 | 96,934 | `merged` | 2 |
| `c0009` | `02` | 145 | 92,858 | `merged` | 7 |
| `c0010` | `02.03` | 56 | 71,005 | `merged` | 1 |
| `c0011` | `02.03` | 137 | 86,174 | `merged` | 1 |
| `c0012` | `02.03` | 32 | 22,457 | `merged` | 1 |
| `c0013` | `02.03.06` | 61 | 72,515 | `merged` | 1 |
| `c0014` | `02.03.06` | 14 | 46,709 | `merged` | 1 |
| `c0015` | `02.03.06.07` | 16 | 95,470 | `subtree` | 1 |
| `c0016` | `02.03.07` | 88 | 63,212 | `subtree` | 1 |
| `c0017` | `02.03.08` | 99 | 98,465 | `merged` | 1 |
| `c0018` | `02.04` | 33 | 81,185 | `merged` | 1 |
| `c0019` | `02.04` | 117 | 99,996 | `merged` | 1 |
| `c0020` | `02.05` | 101 | 95,877 | `merged` | 1 |
| `c0021` | `02.05` | 41 | 82,853 | `merged` | 1 |
| `c0022` | `02.05.05` | 46 | 80,920 | `merged` | 1 |
| `c0023` | `02.05.05.03` | 32 | 40,098 | `merged` | 1 |
| `c0024` | `02.06` | 83 | 78,339 | `merged` | 1 |
| `c0025` | `02.06` | 124 | 97,476 | `merged` | 1 |
| `c0026` | `02.06` | 71 | 77,144 | `merged` | 1 |
| `c0027` | `02.06` | 83 | 89,433 | `merged` | 1 |
| `c0028` | `02.06` | 94 | 76,842 | `merged` | 1 |
| `c0029` | `02.06.02.02` | 88 | 99,783 | `merged` | 1 |
| `c0030` | `02.06.02.02` | 92 | 99,434 | `merged` | 1 |
| `c0031` | `02.06.02.02` | 84 | 98,490 | `merged` | 1 |
| `c0032` | `02.06.02.02` | 87 | 98,817 | `merged` | 1 |
| `c0033` | `02.06.06` | 48 | 60,862 | `merged` | 1 |
| `c0034` | `02.06.07` | 107 | 98,161 | `subtree` | 1 |
| `c0035` | `02.07` | 65 | 69,982 | `merged` | 1 |
| `c0036` | `02.07` | 65 | 99,904 | `merged` | 1 |
| `c0037` | `02.07` | 129 | 96,691 | `merged` | 1 |
| `c0038` | `02.07` | 62 | 61,565 | `merged` | 1 |
| `c0039` | `02.07.03` | 154 | 98,038 | `merged` | 1 |
| `c0040` | `02.07.03` | 21 | 23,336 | `merged` | 1 |
| `c0041` | `02.07.04` | 26 | 33,922 | `merged` | 1 |
| `c0042` | `02.07.04.01` | 62 | 87,613 | `merged` | 1 |
| `c0043` | `02.07.04.01` | 91 | 97,017 | `merged` | 1 |
| `c0044` | `02.07.04.01` | 88 | 96,742 | `merged` | 1 |
| `c0045` | `02.07.04.01` | 64 | 58,546 | `merged` | 1 |
| `c0046` | `02.07.04.01` | 75 | 83,796 | `merged` | 1 |
| `c0047` | `02.07.04.01` | 95 | 95,398 | `merged` | 1 |
| `c0048` | `02.07.04.01` | 159 | 99,950 | `merged` | 1 |
| `c0049` | `02.07.04.01` | 28 | 72,311 | `merged` | 1 |
| `c0050` | `02.07.04.01` | 132 | 95,664 | `merged` | 1 |
| `c0051` | `02.07.04.01` | 128 | 96,686 | `merged` | 1 |
| `c0052` | `02.07.04.01` | 3 | 8,635 | `merged` | 1 |
| `c0053` | `02.07.04.01` | 170 | 99,353 | `merged` | 1 |
| `c0054` | `02.07.04.01.63` | 193 | 99,553 | `merged` | 1 |
| `c0055` | `02.07.13` | 134 | 97,697 | `merged` | 1 |
| `c0056` | `02.07.13` | 180 | 94,584 | `merged` | 1 |
| `c0057` | `02.07.13` | 131 | 77,494 | `merged` | 1 |
| `c0058` | `02.08.04` | 112 | 78,815 | `merged` | 1 |
| `c0059` | `02.08.04` | 93 | 76,036 | `merged` | 1 |
| `c0060` | `02.08.04` | 81 | 76,260 | `merged` | 1 |
| `c0061` | `02.08.04` | 155 | 78,895 | `merged` | 1 |
| `c0062` | `02.08.04` | 153 | 98,161 | `merged` | 1 |
| `c0063` | `02.08.04` | 33 | 19,873 | `merged` | 1 |
| `c0064` | `02.08.04` | 100 | 65,512 | `merged` | 1 |
| `c0065` | `02.08.04.13` | 63 | 70,943 | `merged` | 1 |
| `c0066` | `02.08.04.32` | 100 | 95,520 | `subtree` | 1 |
| `c0067` | `02.08.04.34` | 109 | 94,952 | `merged` | 1 |
| `c0068` | `02.09.01` | 139 | 68,725 | `merged` | 1 |
| `c0069` | `02.09.01` | 132 | 54,419 | `merged` | 1 |
| `c0070` | `02.09.01` | 141 | 86,177 | `merged` | 1 |
| `c0071` | `02.09.01` | 39 | 55,422 | `merged` | 1 |
| `c0072` | `02.09.01.03` | 195 | 63,739 | `merged` | 1 |
| `c0073` | `02.09.01.03.06.01` | 157 | 81,291 | `subtree` | 1 |
| `c0074` | `02.09.01.10` | 129 | 83,393 | `subtree` | 1 |
| `c0075` | `02.09.02` | 89 | 79,557 | `subtree` | 1 |
| `c0076` | `02.10` | 169 | 97,593 | `merged` | 1 |
| `c0077` | `02.10` | 74 | 81,214 | `merged` | 1 |
| `c0078` | `02.11` | 82 | 60,235 | `merged` | 1 |
| `c0079` | `02.11.01` | 43 | 63,410 | `subtree` | 1 |
| `c0080` | `02.11.02` | 81 | 60,146 | `merged` | 1 |
| `c0081` | `02.12.01` | 195 | 47,405 | `subtree` | 1 |
| `c0082` | `02.12.02` | 100 | 53,566 | `merged` | 1 |
| `c0083` | `02.12.02` | 70 | 58,545 | `merged` | 1 |
| `c0084` | `02.12.02.05` | 100 | 99,884 | `merged` | 1 |
| `c0085` | `02.12.03` | 61 | 77,836 | `merged` | 1 |
| `c0086` | `02.12.03` | 54 | 40,746 | `merged` | 1 |
| `c0087` | `02.12.04` | 76 | 68,186 | `subtree` | 1 |
| `c0088` | `02.12.05` | 67 | 37,021 | `subtree` | 1 |
| `c0089` | `02.12.06` | 202 | 92,874 | `merged` | 1 |
| `c0090` | `03` | 113 | 89,793 | `merged` | 6 |
| `c0091` | `03` | 76 | 75,145 | `merged` | 4 |
| `c0092` | `03` | 15 | 52,913 | `merged` | 2 |
| `c0093` | `03.01` | 73 | 56,297 | `subtree` | 1 |
| `c0094` | `03.02` | 95 | 70,621 | `subtree` | 1 |
| `c0095` | `03.13` | 116 | 73,631 | `subtree` | 1 |
| `c0096` | `03.14` | 26 | 99,844 | `merged` | 1 |
| `c0097` | `03.14` | 23 | 95,236 | `merged` | 1 |
| `c0098` | `03.14` | 19 | 94,683 | `merged` | 1 |
| `c0099` | `03.14` | 17 | 93,310 | `merged` | 1 |
| `c0100` | `99` | 204 | 92,885 | `merged` | 204 |
| `c0101` | `99` | 44 | 17,787 | `merged` | 44 |

## 15 簇抽样（等距，看标题用）

### c0001 · `00`

1 篇 / 379 token / 源自 `subtree` / `span2`=1 `span3`=1

- 00_SmarTest_7.10.3_Documentation

### c0007 · `02`

229 篇 / 66,014 token / 源自 `merged` / `span2`=2 `span3`=3

- 02.08.04.34.06.01_Setting_up_the_wavetables
- 02.08.04.34.06.02_Defining_the_equation_sets
- 02.08.04.34.06.03_Defining_the_spec_sets
- 02.08.04.34.06.04.01_Considering_Tri-state_Switching_Accuracy
- 02.08.04.34.06.04_Methodology_for_Generating_Complex_Device_Cycles
- 02.08.04.34.06.05.01_Minimum_period___maximum_frequency_of_the_sequencer
- 02.08.04.34.06.05_Setting_the_period
- 02.08.04.34.06.06.01_Watching_System_Resources
- 02.08.04.34.06.06.02_Checking_Edge_Usage
- 02.08.04.34.06.06.03.01_Dropping_Unused_Edges
- *…另有 219 篇*

### c0013 · `02.03.06`

61 篇 / 72,515 token / 源自 `merged` / `span2`=1 `span3`=1

- 02.03.06.01.01_AV8__MCA__pogo_pin_assignment
- 02.03.06.01.02_MBAV8__MCB__pogo_pin_assignment
- 02.03.06.01.03_MBAV8___MCE__pogo_pin_assignment
- 02.03.06.01.04_6GQS__MCC__pogo_pin_assignment
- 02.03.06.01.05_Wave_Scale_MX_pogo_pin_assignment_and_model_file_configuration
- 02.03.06.01_Pogo_pin_assignment_-_Analog_cards
- 02.03.06.02.01.01_AVI64_pogo_cable_assembly__E8025AVP
- 02.03.06.02.01_AVI64_pogo_pin_assignment
- 02.03.06.02.02.01_E8023PA_pogo_cable_assembly__8_HD_pogo_blocks__Standard
- 02.03.06.02.02.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks
- *…另有 51 篇*

### c0019 · `02.04`

117 篇 / 99,996 token / 源自 `merged` / `span2`=1 `span3`=11

- 02.04.05.01.01_Activating_system_licenses
- 02.04.05.01.02_Activating_licenses_advanced
- 02.04.05.01.03_Find_out_HostID_and_HostName
- 02.04.05.01.04_Editing_.lic_license_files
- 02.04.05.01_The_System_.lic_license_files
- 02.04.05.02.01_Enabling_software_licenses
- 02.04.05.02_The_Software_.lic_license_files
- 02.04.05.03_Configuration_for_digital_cards
- 02.04.05.04_Configuration_for_DPSs
- 02.04.05.05_Configuration_information_in_the_report_window
- *…另有 107 篇*

### c0025 · `02.06`

124 篇 / 97,476 token / 源自 `merged` / `span2`=1 `span3`=2

- 02.06.05.01.01.01_Drive_Levels
- 02.06.05.01.01.02.01_Comparing_output_signals
- 02.06.05.01.01.02_Compare_Levels__Thresholds
- 02.06.05.01.01.03.01_Active_load_termination
- 02.06.05.01.01.03.02_Driver_termination
- 02.06.05.01.01.03_Termination_types
- 02.06.05.01.01_Basic_concepts_of_levels
- 02.06.05.01.02_DPS__Device_Power_Supply__pins
- 02.06.05.01.03_Clamping
- 02.06.05.01.04.01_Elements_of_Equation_Based_Level_Setup
- *…另有 114 篇*

### c0031 · `02.06.02.02`

84 篇 / 98,490 token / 源自 `merged` / `span2`=1 `span3`=1

- 02.06.02.02.253_SWNG__SWNG__-__SWiNG__mV__for_level_dependent_calibration
- 02.06.02.02.254_TCMT__TCMT__-__Test_CoMment_Transfer
- 02.06.02.02.255_TDEX__Test_Data_Extension
- 02.06.02.02.256_TEMP__-__read_TEMPerature
- 02.06.02.02.257_TERM__TERM__-__TERMination_mode
- 02.06.02.02.258_TMUD__Tester_Memory_Utilization_set_Default_values
- 02.06.02.02.259_TMUL___Tester_Memory_Utilization_Log
- 02.06.02.02.260_TOCF__TOCF__-__Timing_Level_Offset_search_ConFiguration
- 02.06.02.02.261_TOCR__TOCR__-__Timing_level_Offset_Configure_Result_pins
- 02.06.02.02.262_TORC_-__Timing_level_Offset_Result_Copy
- *…另有 74 篇*

### c0037 · `02.07`

129 篇 / 96,691 token / 源自 `merged` / `span2`=1 `span3`=5

- 02.07.07.01_Creating_a_customized_shmoo_test_method
- 02.07.07.02.01.01_addParameterType
- 02.07.07.02.01_The_functions_of_the_customized_shmoo_test_method_template
- 02.07.07.02_Customized_shmoo_test_template
- 02.07.07.03_Viewing_customized_results_of_a_customized_shmoo_test_in_the_Shmoo_Tool
- 02.07.07.04_Performing_customized_source-sync_shmoo_tests_with_the_shmoo_tool
- 02.07.07_Shmoo_test_method_customization
- 02.07.08.01_CCF-ISR_mode
- 02.07.08.02_Merging_the_setups
- 02.07.08.03_CCF_test_method_template
- *…另有 119 篇*

### c0043 · `02.07.04.01`

91 篇 / 97,017 token / 源自 `merged` / `span2`=1 `span3`=1

- 02.07.04.01.14.01_CCTaddPAResultId
- 02.07.04.01.14.02_CCTchangeLevelSpec
- 02.07.04.01.14.03_CCTcontinueCurrentTest
- 02.07.04.01.14.04_CCTenableSMC
- 02.07.04.01.14.05_CCTgetAllDCUploadLength
- 02.07.04.01.14.06_CCTgetAllDCUploadStartIdx
- 02.07.04.01.14.07_CCTgetAnalogRFSetName
- 02.07.04.01.14.08_CCTgetContextPins
- 02.07.04.01.14.09_CCTgetCycleOffset
- 02.07.04.01.14.10_CCTgetDCResults
- *…另有 81 篇*

### c0049 · `02.07.04.01`

28 篇 / 72,311 token / 源自 `merged` / `span2`=1 `span3`=1

- 02.07.04.01.267_VEC_EVENTS
- 02.07.04.01.268_VEC_LABEL_EDIT
- 02.07.04.01.269_VECTOR
- 02.07.04.01.270.01_VEC_TRANSFER_PIN_TASK
- 02.07.04.01.270_VEC_TRANSFER_TASK
- 02.07.04.01.271_WAIT_TEST_DONE
- 02.07.04.01.272_WAIT_TIME
- 02.07.04.01.273_Wave
- 02.07.04.01.274_WAVE_LOG
- 02.07.04.01.27_DC_PROFILING_ON
- *…另有 18 篇*

### c0055 · `02.07.13`

134 篇 / 97,697 token / 源自 `merged` / `span2`=1 `span3`=1

- 02.07.13.08.01.01_cont
- 02.07.13.08.01.02_execute
- 02.07.13.08.01.03_id
- 02.07.13.08.01.04_RDI_BEGIN
- 02.07.13.08.01.05_RDI_END
- 02.07.13.08.01.06_RDI_INIT
- 02.07.13.08.01.07_RDI_UNIT_INIT
- 02.07.13.08.01.08_RDI_WAIT_TEST_DONE
- 02.07.13.08.01_General_SmartRDI_functions
- 02.07.13.08.02.01_clearPinStatus
- *…另有 124 篇*

### c0061 · `02.08.04`

155 篇 / 78,895 token / 源自 `merged` / `span2`=1 `span3`=1

- 02.08.04.18.01.01_Pin
- 02.08.04.18.01.02_Pin_group
- 02.08.04.18.01.03_Port
- 02.08.04.18.01.04_Alias_set
- 02.08.04.18.01.05_Utility_purpose
- 02.08.04.18.01_Introduction_of_the_Pin_Configuration_Tool
- 02.08.04.18.02.01_Opening_the_setup_editor
- 02.08.04.18.02.02_Importing_the_pin_configuration_from_a_CSV_file
- 02.08.04.18.02.03_Exporting_the_pin_configuration_to_a_CSV_file
- 02.08.04.18.02.04_Discarding_the_changes_in_the_pin_configuration_tool
- *…另有 145 篇*

### c0067 · `02.08.04.34`

109 篇 / 94,952 token / 源自 `merged` / `span2`=1 `span3`=1

- 02.08.04.34.02.02.01_APRM_-__Activate_PRiMary_sets
- 02.08.04.34.02.02.02_BWDF__BWDF__-__Break_Waveform_DeFinition
- 02.08.04.34.02.02.03_BWDS__BWDS__-__Break_Waveform_Definition_String
- 02.08.04.34.02.02.04_CDCP__-__Cycle_Device_Cycle_Parameter
- 02.08.04.34.02.02.05_CLKR__CLKR__-__CLocK_Resolution
- 02.08.04.34.02.02.06_DCDT__DCDT__-__Device_Cycle_DefaulT
- 02.08.04.34.02.02.07_DCUD_-__Device_Cycle_UnDefine
- 02.08.04.34.02.02.08_DFCR__DFCR__-__DeFine_Clock_Routing
- 02.08.04.34.02.02.09_DPRT__DPRT__-__Default_PRimary_Timing_sets
- 02.08.04.34.02.02.10_DSCP__DSCP__-__Define_System_Control_Parameter
- *…另有 99 篇*

### c0073 · `02.09.01.03.06.01`

157 篇 / 81,291 token / 源自 `subtree` / `span2`=1 `span3`=1

- 02.09.01.03.06.01.01_The_configuration_for_handlers
- 02.09.01.03.06.01.02_Number_of_sites_supported_by_GPIB_handler_driver
- 02.09.01.03.06.01.03_Number_of_sites_supported_by_GPIO_handler_driver
- 02.09.01.03.06.01.04_Conventions_for_GPIB_LAN_communication
- 02.09.01.03.06.01.05.01.01_Valid_combinations_of_plug-ins_and_configuration_files
- 02.09.01.03.06.01.05.01.02_Binning_maps
- 02.09.01.03.06.01.05.01.03_Timing_diagram__Advantest_M-4182
- 02.09.01.03.06.01.05.01_Dual-site_GPIO_configuration
- 02.09.01.03.06.01.05.02.01_General_information_about_the_Advantest_GPIB_handler_driver
- 02.09.01.03.06.01.05.02.02_Default_GPIB_configuration
- *…另有 147 篇*

### c0079 · `02.11.01`

43 篇 / 63,410 token / 源自 `subtree` / `span2`=1 `span3`=1

- 02.11.01.01_Introduction
- 02.11.01.02_Installing_STIL_Reader
- 02.11.01.03.01.01_Signals
- 02.11.01.03.01.02_Timing_and_levels
- 02.11.01.03.01.03_Event_mapping
- 02.11.01.03.01.04_Patterns
- 02.11.01.03.01_How_STIL_elements_are_converted
- 02.11.01.03.02_V93000_break_waveforms
- 02.11.01.03.03_Support_for_SVF__TDL__and_WGL
- 02.11.01.03.04_STIL_Reader_performance
- *…另有 33 篇*

### c0085 · `02.12.03`

61 篇 / 77,836 token / 源自 `merged` / `span2`=1 `span3`=1

- 02.12.03.01.01_Introduction_to_MTL
- 02.12.03.01.02_Syntax_conventions
- 02.12.03.01_Overview_of_MTL
- 02.12.03.02.01_Basic_MTL_workflow
- 02.12.03.02.02_MTL_compiler_syntax
- 02.12.03.02.03_Naming_rules_and_conventions
- 02.12.03.02.04.01.01_MTL_Defines
- 02.12.03.02.04.01.02_Execution_Dialog_window
- 02.12.03.02.04.01.03_Pattern_list_file_syntax
- 02.12.03.02.04.01_MTL_Compiler_Control_dialog
- *…另有 51 篇*
