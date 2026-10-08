# 语料坏字修复（第二批）证据表 —— 第三字节已丢的 8 族

**md 推不回来**（第三字节被 `?` 顶掉），正字取自**上游 `.htm`**。
判据三条叠加：① 词锚（字母数字词，天然干净）② 锚全篇唯一命中 ③ 候选落在坏字字节定死的区间里。
**只改下游 md，上游 HTML 一个字节不动。**

共 **1,482** 处。

| # | markdown | 坏字 | 正字 | 上下文 |
|---|---|---|---|---|
| 1 | `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md` | `鈮?` | `≥` | `1072 ... 16777216 bytes.    Note  -  For SmarTest 鈮?7.4.3.0:  fast_tra` |
| 2 | `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md` | `鈮?` | `≤` | `1072 ... 16777216 bytes.    Note  -  For SmarTest 鈮?7.4.3.0:  fast_tra` |
| 3 | `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.04_Utility_Line_view.md` | `鈥?` | `…` | `numbers of the utility lines, using the range [01 鈥?nbsp;32] from righ` |
| 4 | `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.04_Utility_Line_view.md` | `鈥?` | `…` | `numbers of the utility lines, using the range [01 鈥?nbsp;32] from righ` |
| 5 | `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.05_Using_the_Utility_Line_View.md` | `鈥?` | `…` | `numbers of the utility lines, using the range [01 鈥?nbsp;32] from righ` |
| 6 | `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.05_Using_the_Utility_Line_View.md` | `鈥?` | `…` | `numbers of the utility lines, using the range [01 鈥?nbsp;32] from righ` |
| 7 | `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.01_SmarTest_Prerequisites.md` | `鈮?` | `≥` | `ating systems only. Note Installation of SmarTest 鈮?.5 and SmarTest 8 ` |
| 8 | `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.01_SmarTest_Prerequisites.md` | `鈮?` | `≥` | `ating systems only. Note Installation of SmarTest 鈮?.5 and SmarTest 8 ` |
| 9 | `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.01_SmarTest_Prerequisites.md` | `鈮?` | `≥` | `ating systems only. Note Installation of SmarTest 鈮?.5 and SmarTest 8 ` |
| 10 | `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.01_SmarTest_Prerequisites.md` | `鈮?` | `≥` | `ating systems only. Note Installation of SmarTest 鈮?.5 and SmarTest 8 ` |
| 11 | `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.02_Using_the_Advantest_Software_Center.md` | `鈮?` | `≥` | `tion operating system is Red Hat Enterprise Linux 鈮?7.2.x or the requi` |
| 12 | `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.03_Downloading_and_installing_the_SmartInstall_add-on.md` | `鈮?` | `≥` | `tion operating system is Red Hat Enterprise Linux 鈮?7.2.x or the requi` |
| 13 | `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.01.04_Downloading_and_installing_SmarTest_software.md` | `鈮?` | `≥` | `tion operating system is Red Hat Enterprise Linux 鈮?7.2.x or the requi` |
| 14 | `02_System_reference/02.02_Specifications/02.02.01.07_Environmental.md` | `鈩?` | `℃` | ` to 86 °F) \|  \|  Maximum rate of change   \|   ± 2 鈩?h (3.6 鈩?h)   \|  \|` |
| 15 | `02_System_reference/02.02_Specifications/02.02.01.07_Environmental.md` | `鈩?` | `℉` | ` to 86 °F) \|  \|  Maximum rate of change   \|   ± 2 鈩?h (3.6 鈩?h)   \|  \|` |
| 16 | `02_System_reference/02.02_Specifications/02.02.04.01.01_PS1600_overview.md` | `鈩?` | `™` | `dard pattern space (32k per pin)   \|  \|  SmartLoop鈩?/p> \|  Active, ret` |
| 17 | `02_System_reference/02.02_Specifications/02.02.04.01.01_PS1600_overview.md` | `鈮?` | `≤` | `hangeable   \|  Speed  \|  Maximum I/O data rate at 鈮?1.8 V (pattern, PR` |
| 18 | `02_System_reference/02.02_Specifications/02.02.04.01.01_PS1600_overview.md` | `鈩?` | `™` | `dard pattern space (32k per pin)   \|  \|  SmartLoop鈩?/p> \|  Active, ret` |
| 19 | `02_System_reference/02.02_Specifications/02.02.04.01.01_PS1600_overview.md` | `鈮?` | `≤` | `hangeable   \|  Speed  \|  Maximum I/O data rate at 鈮?1.8 V (pattern, PR` |
| 20 | `02_System_reference/02.02_Specifications/02.02.04.01.01_PS1600_overview.md` | `鈩?` | `™` | `dard pattern space (32k per pin)   \|  \|  SmartLoop鈩?/p> \|  Active, ret` |
| 21 | `02_System_reference/02.02_Specifications/02.02.04.01.01_PS1600_overview.md` | `鈮?` | `≤` | `hangeable   \|  Speed  \|  Maximum I/O data rate at 鈮?1.8 V (pattern, PR` |
| 22 | `02_System_reference/02.02_Specifications/02.02.04.01.01_PS1600_overview.md` | `鈮?` | `≤` | `hangeable   \|  Speed  \|  Maximum I/O data rate at 鈮?1.8 V (pattern, PR` |
| 23 | `02_System_reference/02.02_Specifications/02.02.04.01.06.01_PS1600_Voltage_force_and_measure.md` | `鈮?` | `≤` | `nge  within range 1 (± 40 mA)  within range 2..5 (鈮?± 1 mA)   \|  Volta` |
| 24 | `02_System_reference/02.02_Specifications/02.02.04.01.06.01_PS1600_Voltage_force_and_measure.md` | `鈮?` | `≥` | `nge  within range 1 (± 40 mA)  within range 2..5 (鈮?± 1 mA)   \|  Volta` |
| 25 | `02_System_reference/02.02_Specifications/02.02.04.01.06.01_PS1600_Voltage_force_and_measure.md` | `鈮?` | `≤` | `nge  within range 1 (± 40 mA)  within range 2..5 (鈮?± 1 mA)   \|  Volta` |
| 26 | `02_System_reference/02.02_Specifications/02.02.04.01.06.02_PS1600_Current_force_and_measure.md` | `鈮?` | `≤` | `  Range 1 force current up to ±56 mA for voltages 鈮?3.3 V. Range 1 for` |
| 27 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `™` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 28 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `Ω` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 29 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `™` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 30 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 31 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 32 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 33 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `Ω` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 34 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 35 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 36 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 37 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 38 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 39 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 40 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `K` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 41 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 42 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 43 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 44 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 45 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 46 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 47 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 48 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 49 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 50 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 51 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 52 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 53 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 54 | `02_System_reference/02.02_Specifications/02.02.04.03.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 55 | `02_System_reference/02.02_Specifications/02.02.04.03.02_Pin_Scale_5000_vector_memory.md` | `鈥?` | `…` | `  \|  1,792 M   \|  \|  X5鈥8-mode   \|  5 Gbps   \|  5鈥?   \|  1 drive + 1 ` |
| 56 | `02_System_reference/02.02_Specifications/02.02.04.03.02_Pin_Scale_5000_vector_memory.md` | `鈥?` | `…` | `  \|  1,792 M   \|  \|  X5鈥8-mode   \|  5 Gbps   \|  5鈥?   \|  1 drive + 1 ` |
| 57 | `02_System_reference/02.02_Specifications/02.02.04.03.03_Pin_Scale_5000_timing.md` | `鈩?` | `Ω` | `the following figures:  - Vswing = 500 mV into 50 鈩?at a single connec` |
| 58 | `02_System_reference/02.02_Specifications/02.02.04.03.03_Pin_Scale_5000_timing.md` | `鈩?` | `Ω` | `the following figures:  - Vswing = 500 mV into 50 鈩?at a single connec` |
| 59 | `02_System_reference/02.02_Specifications/02.02.04.03.03_Pin_Scale_5000_timing.md` | `鈥?` | `…` | `sight E5052B, phase noise integration range 1 kHz 鈥? 40 MHz[2)](<>) Me` |
| 60 | `02_System_reference/02.02_Specifications/02.02.04.03.03_Pin_Scale_5000_timing.md` | `鈥?` | `…` | `sight E5052B, phase noise integration range 1 kHz 鈥? 40 MHz[2)](<>) Me` |
| 61 | `02_System_reference/02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md` | `鈩?` | `Ω` | `ition: half the noted voltage, terminated into 50 鈩?   \|  \|  Maximum t` |
| 62 | `02_System_reference/02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md` | `鈮?` | `≤` | `into open   \|  \|  High level (vih) range at \|VGS\| 鈮?100 mV   \|  Fast m` |
| 63 | `02_System_reference/02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md` | `鈮?` | `≤` | `into open   \|  \|  High level (vih) range at \|VGS\| 鈮?100 mV   \|  Fast m` |
| 64 | `02_System_reference/02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md` | `鈩?` | `Ω` | `ition: half the noted voltage, terminated into 50 鈩?   \|  \|  Maximum t` |
| 65 | `02_System_reference/02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md` | `鈩?` | `Ω` | `ition: half the noted voltage, terminated into 50 鈩?   \|  \|  Maximum t` |
| 66 | `02_System_reference/02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md` | `鈩?` | `Ω` | `ition: half the noted voltage, terminated into 50 鈩?   \|  \|  Maximum t` |
| 67 | `02_System_reference/02.02_Specifications/02.02.04.03.05_Pin_Scale_5000_receiver.md` | `鈮?` | `≤` | `) \|  \| Input voltage and threshold range at \|VGS\| 鈮?100 mV  \| -1.5 V t` |
| 68 | `02_System_reference/02.02_Specifications/02.02.04.03.05_Pin_Scale_5000_receiver.md` | `鈩?` | `Ω` | `gle-ended impedance  \| -1.5 V 鈮?VSE 鈮?3.0 V  \| 50 鈩?± 3 鈩?/td> \|  \| VS` |
| 69 | `02_System_reference/02.02_Specifications/02.02.04.03.05_Pin_Scale_5000_receiver.md` | `鈮?` | `≤` | `) \|  \| Input voltage and threshold range at \|VGS\| 鈮?100 mV  \| -1.5 V t` |
| 70 | `02_System_reference/02.02_Specifications/02.02.04.03.05_Pin_Scale_5000_receiver.md` | `鈩?` | `Ω` | `gle-ended impedance  \| -1.5 V 鈮?VSE 鈮?3.0 V  \| 50 鈩?± 3 鈩?/td> \|  \| VS` |
| 71 | `02_System_reference/02.02_Specifications/02.02.04.03.09_Pin_Scale_5000_parametric_measurement_unit.md` | `鈩?` | `Ω` | ` current. R is the maximum wiring resistance of 1 鈩?   \| Voltage force` |
| 72 | `02_System_reference/02.02_Specifications/02.02.04.03.09_Pin_Scale_5000_parametric_measurement_unit.md` | `鈮?` | `≤` | `asure \|  \| Voltage force / measure range at \|VGS\| 鈮? 100 mV  \| I 鈮?25 ` |
| 73 | `02_System_reference/02.02_Specifications/02.02.04.03.09_Pin_Scale_5000_parametric_measurement_unit.md` | `鈮?` | `≤` | `asure \|  \| Voltage force / measure range at \|VGS\| 鈮? 100 mV  \| I 鈮?25 ` |
| 74 | `02_System_reference/02.02_Specifications/02.02.04.03.11_Pin_Scale_5000_high_voltage_protection.md` | `鈮?` | `≤` | `+10 V ... +80 V \|  \| Overvoltage reaction time  \| 鈮?15 ns \|  \| Overcur` |
| 75 | `02_System_reference/02.02_Specifications/02.02.04.03.11_Pin_Scale_5000_high_voltage_protection.md` | `鈮?` | `≥` | `+10 V ... +80 V \|  \| Overvoltage reaction time  \| 鈮?15 ns \|  \| Overcur` |
| 76 | `02_System_reference/02.02_Specifications/02.02.04.03.11_Pin_Scale_5000_high_voltage_protection.md` | `鈮?` | `≤` | `+10 V ... +80 V \|  \| Overvoltage reaction time  \| 鈮?15 ns \|  \| Overcur` |
| 77 | `02_System_reference/02.02_Specifications/02.02.04.03.14_Pin_Scale_5000_terms.md` | `鈮?` | `≥` | `ly connected to the DUT, enable to compensate for 鈮?97% (or 鈮?94% for ` |
| 78 | `02_System_reference/02.02_Specifications/02.02.04.03.14_Pin_Scale_5000_terms.md` | `鈮?` | `≥` | `ly connected to the DUT, enable to compensate for 鈮?97% (or 鈮?94% for ` |
| 79 | `02_System_reference/02.02_Specifications/02.02.04.03_PS5000_specifications.md` | `鈩?` | `™` | `digital card to execute digital tests on EXA Scale鈩?test systems.  ![O` |
| 80 | `02_System_reference/02.02_Specifications/02.02.04.03_PS5000_specifications.md` | `鈩?` | `™` | `digital card to execute digital tests on EXA Scale鈩?test systems.  ![O` |
| 81 | `02_System_reference/02.02_Specifications/02.02.04.03_PS5000_specifications.md` | `鈩?` | `™` | `digital card to execute digital tests on EXA Scale鈩?test systems.  ![O` |
| 82 | `02_System_reference/02.02_Specifications/02.02.04.03_PS5000_specifications.md` | `鈩?` | `™` | `digital card to execute digital tests on EXA Scale鈩?test systems.  ![O` |
| 83 | `02_System_reference/02.02_Specifications/02.02.05.01_DC_Scale_DPS128_Device_Power_Supply__E8023CS_E8023CSH__-_high_current_sp.md` | `鈮?` | `≤` | `age drop in the Force path beyond the pogo pin of 鈮?nbsp;0.1 V.   ![DP` |
| 84 | `02_System_reference/02.02_Specifications/02.02.05.02_DC_Scale_UHC4T_Device_Power_Supply__E8024UH.md` | `鈮?` | `≤` | `in these limits for each channel of a board:    - 鈮?0.6 V : 鈮?40 A   -` |
| 85 | `02_System_reference/02.02_Specifications/02.02.05.02_DC_Scale_UHC4T_Device_Power_Supply__E8024UH.md` | `鈮?` | `≤` | `in these limits for each channel of a board:    - 鈮?0.6 V : 鈮?40 A   -` |
| 86 | `02_System_reference/02.02_Specifications/02.02.05.02_DC_Scale_UHC4T_Device_Power_Supply__E8024UH.md` | `鈮?` | `≤` | `in these limits for each channel of a board:    - 鈮?0.6 V : 鈮?40 A   -` |
| 87 | `02_System_reference/02.02_Specifications/02.02.05.03.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 88 | `02_System_reference/02.02_Specifications/02.02.05.03.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 89 | `02_System_reference/02.02_Specifications/02.02.05.03.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 90 | `02_System_reference/02.02_Specifications/02.02.05.03.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 91 | `02_System_reference/02.02_Specifications/02.02.05.03.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 92 | `02_System_reference/02.02_Specifications/02.02.05.03.02_XPS256_voltage_specifications.md` | `鈥?` | `…` | `0735__fn_Measurement_conditions>) \|  \|   \| -0.5 V 鈥?nbsp;+1.5 V  \| 10 ` |
| 93 | `02_System_reference/02.02_Specifications/02.02.05.03.02_XPS256_voltage_specifications.md` | `鈥?` | `…` | `0735__fn_Measurement_conditions>) \|  \|   \| -0.5 V 鈥?nbsp;+1.5 V  \| 10 ` |
| 94 | `02_System_reference/02.02_Specifications/02.02.05.03.02_XPS256_voltage_specifications.md` | `鈥?` | `…` | `0735__fn_Measurement_conditions>) \|  \|   \| -0.5 V 鈥?nbsp;+1.5 V  \| 10 ` |
| 95 | `02_System_reference/02.02_Specifications/02.02.05.03.02_XPS256_voltage_specifications.md` | `鈥?` | `…` | `0735__fn_Measurement_conditions>) \|  \|   \| -0.5 V 鈥?nbsp;+1.5 V  \| 10 ` |
| 96 | `02_System_reference/02.02_Specifications/02.02.05.03.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 97 | `02_System_reference/02.02_Specifications/02.02.05.03.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 98 | `02_System_reference/02.02_Specifications/02.02.05.03.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 99 | `02_System_reference/02.02_Specifications/02.02.05.03.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 100 | `02_System_reference/02.02_Specifications/02.02.05.03.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 101 | `02_System_reference/02.02_Specifications/02.02.05.03.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 102 | `02_System_reference/02.02_Specifications/02.02.05.03.04_XPS256_voltage_and_current_capability_specifications.md` | `鈮?` | `≤` | `op in the force path beyond the pogo pin of total 鈮?0.5V.  ## Maximum ` |
| 103 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 104 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 105 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 106 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 107 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 108 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 109 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 110 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 111 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 112 | `02_System_reference/02.02_Specifications/02.02.05.03.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 113 | `02_System_reference/02.02_Specifications/02.02.05.03.08_XPS256_pogo_block_specifications.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 114 | `02_System_reference/02.02_Specifications/02.02.05.03.08_XPS256_pogo_block_specifications.md` | `鈼?` | `●` | `C  \| GND  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 115 | `02_System_reference/02.02_Specifications/02.02.05.03.08_XPS256_pogo_block_specifications.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 116 | `02_System_reference/02.02_Specifications/02.02.05.03.08_XPS256_pogo_block_specifications.md` | `鈼?` | `●` | `C  \| GND  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 117 | `02_System_reference/02.03_DUT_board_design_reference/02.03.01.01_Release_information.md` | `锛?` | `：` | `Package updated to Revision F  - System dimensions锛?Test head movement` |
| 118 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 119 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 120 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 121 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 122 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 123 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 124 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 125 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 126 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 127 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 128 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 129 | `02_System_reference/02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md` | `鈥?` | `…` | `erface.  The pogo block number in round brackets (鈥? are alternate pog` |
| 130 | `02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md` | `鈥?` | `…` | ` all  \| all  \| +3.3 V \|  \| CTH  \| active  \| URW00 鈥?nbsp;URW15  \| 3 an` |
| 131 | `02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md` | `鈥?` | `…` | ` all  \| all  \| +3.3 V \|  \| CTH  \| active  \| URW00 鈥?nbsp;URW15  \| 3 an` |
| 132 | `02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md` | `鈥?` | `…` | ` all  \| all  \| +3.3 V \|  \| CTH  \| active  \| URW00 鈥?nbsp;URW15  \| 3 an` |
| 133 | `02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md` | `鈥?` | `…` | ` all  \| all  \| +3.3 V \|  \| CTH  \| active  \| URW00 鈥?nbsp;URW15  \| 3 an` |
| 134 | `02_System_reference/02.03_DUT_board_design_reference/02.03.04.05_Sequencer-controlled_utility_lines.md` | `鈥?` | `…` | `ight utility pogo blocks. The pogo pins are URW00 鈥?nbsp;URW15 on 2‑ro` |
| 135 | `02_System_reference/02.03_DUT_board_design_reference/02.03.04.05_Sequencer-controlled_utility_lines.md` | `鈥?` | `…` | `ight utility pogo blocks. The pogo pins are URW00 鈥?nbsp;URW15 on 2‑ro` |
| 136 | `02_System_reference/02.03_DUT_board_design_reference/02.03.04_Utility_lines.md` | `鈥?` | `…` | `an be accessed via the utility pogo blocks UTIL 1 鈥?nbsp;UTIL 8 of the` |
| 137 | `02_System_reference/02.03_DUT_board_design_reference/02.03.04_Utility_lines.md` | `鈥?` | `…` | `an be accessed via the utility pogo blocks UTIL 1 鈥?nbsp;UTIL 8 of the` |
| 138 | `02_System_reference/02.03_DUT_board_design_reference/02.03.05.06.02_External_utility_power_supply_-_Configuration_and_DUT_board_design.md` | `鈥?` | `…` | `alue should be in the range of approximately 1 μF 鈥?22μF depending on ` |
| 139 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.01_AVI64_pogo_pin_assignment.md` | `鈼?` | `●` | `_N  \| SAFETY_P \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 140 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.01_AVI64_pogo_pin_assignment.md` | `鈼?` | `●` | `_N  \| SAFETY_P \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 141 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.01_AVI64_pogo_pin_assignment.md` | `鈥?` | `…` | ` the pogo pin descriptions:  - Pin: # = Channel 1 鈥?nbsp;16 - The DNC ` |
| 142 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.01_E8023PA_pogo_cable_assembly__8_HD_pogo_blocks__Standard.md` | `鈥?` | `…` | `the same pogo pin assignment.   \|   \|   \| Block A 鈥?H \|  \| Pin  \| a  \|` |
| 143 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.01_E8023PA_pogo_cable_assembly__8_HD_pogo_blocks__Standard.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \|    \|  ` |
| 144 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.01_E8023PA_pogo_cable_assembly__8_HD_pogo_blocks__Standard.md` | `鈥?` | `…` | `the same pogo pin assignment.   \|   \|   \| Block A 鈥?H \|  \| Pin  \| a  \|` |
| 145 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks.md` | `鈼?` | `●` | ` GND  \|   \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 146 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks.md` | `鈥?` | `…` | `es on the pogo pin descriptions:  - # = Channel 1 鈥?nbsp;16 -  DC/DC p` |
| 147 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.03_E8023PC_pogo_cable_assembly__4_HD_pogo_blocks__DPS128-HC_only.md` | `鈥?` | `…` | `same pogo pin assignment.   \|   \|   \|   \| Block A 鈥?D \|  \|   \| Pin  \| ` |
| 148 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.03_E8023PC_pogo_cable_assembly__4_HD_pogo_blocks__DPS128-HC_only.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \|  \|  Th` |
| 149 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.03_E8023PC_pogo_cable_assembly__4_HD_pogo_blocks__DPS128-HC_only.md` | `鈥?` | `…` | `same pogo pin assignment.   \|   \|   \|   \| Block A 鈥?D \|  \|   \| Pin  \| ` |
| 150 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.04_E8023PD_pogo_cable_assembly__2_HD_pogo_blocks__DPS64_only.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \|  \|  Th` |
| 151 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.04_E8023PD_pogo_cable_assembly__2_HD_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16.   \|  For ` |
| 152 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.05_E8023PE_pogo_cable_assembly__8_MS-DPS_style_pogo_blocks__DPS128-HC_only.md` | `鈼?` | `●` | `5+PS16)  \| P4 (P13+P14) \|  \|   \| Orientation mark 鈼?/strong>  \|  \|  Th` |
| 153 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.05_E8023PE_pogo_cable_assembly__8_MS-DPS_style_pogo_blocks__DPS128-HC_only.md` | `鈥?` | `…` | `n the DPS128-HC side  "#" is the channel number 1 鈥?nbsp;16 for DPS128` |
| 154 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.05_E8023PE_pogo_cable_assembly__8_MS-DPS_style_pogo_blocks__DPS128-HC_only.md` | `鈥?` | `…` | `n the DPS128-HC side  "#" is the channel number 1 鈥?nbsp;16 for DPS128` |
| 155 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.06_E8023PF_pogo_cable_assembly__2_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈼?` | `●` | `4  (P9+P10+  P11+P12)   \|  \|   \| Orientation mark 鈼?/strong>  \|   \|  T` |
| 156 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.06_E8023PF_pogo_cable_assembly__2_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16 for DPS64 ` |
| 157 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.06_E8023PF_pogo_cable_assembly__2_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16 for DPS64 ` |
| 158 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.07_E8023PG_pogo_cable_assembly__4_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16 for DPS64 ` |
| 159 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.07_E8023PG_pogo_cable_assembly__4_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16 for DPS64 ` |
| 160 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.08_E8023PH_pogo_cable_assembly__4_HD_pogo_blocks__DPS64_standard.md` | `鈼?` | `●` | ` \| NC  \| NC  \| NC  \| NC \|  \|   \| Orientation mark 鈼?/strong>  \|   \|  T` |
| 161 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.08_E8023PH_pogo_cable_assembly__4_HD_pogo_blocks__DPS64_standard.md` | `鈥?` | `…` | `rovide landing pads.  "#" is the channel number 1 鈥?nbsp;16.   \|  For ` |
| 162 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.09_E8023PK_pogo_cable_assembly__4_VHD_pogo_blocks__DPS128.md` | `鈼?` | `●` | ` GND  \|   \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 163 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02.09_E8023PK_pogo_cable_assembly__4_VHD_pogo_blocks__DPS128.md` | `鈥?` | `…` | `es on the pogo pin descriptions:  - # = Channel 1 鈥?nbsp;16 -  DC/DC p` |
| 164 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 165 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 166 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 167 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 168 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 169 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 170 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 171 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 172 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 173 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.02_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 174 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.04_FVI16_pogo_pin_assignment.md` | `鈼?` | `●` | `  \| SAFETY1_5V \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 175 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.04_FVI16_pogo_pin_assignment.md` | `鈼?` | `●` | `  \| SAFETY1_5V \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 176 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.04_FVI16_pogo_pin_assignment.md` | `鈥?` | `…` | ` Control line of the safety circuit for channel 1 鈥?nbsp;8  \|   \| Conn` |
| 177 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.04_FVI16_pogo_pin_assignment.md` | `鈥?` | `…` | ` Control line of the safety circuit for channel 1 鈥?nbsp;8  \|   \| Conn` |
| 178 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.04_FVI16_pogo_pin_assignment.md` | `鈥?` | `…` | ` Control line of the safety circuit for channel 1 鈥?nbsp;8  \|   \| Conn` |
| 179 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.05_PVI8_pogo_pin_assignment.md` | `鈼?` | `●` | `SAFETY_GND  \| SAFETY_5V \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 180 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.05_PVI8_pogo_pin_assignment.md` | `鈼?` | `●` | `SAFETY_GND  \| SAFETY_5V \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 181 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.05_PVI8_pogo_pin_assignment.md` | `鈥?` | `…` | ` the pogo pin descriptions:  - Pin: # = Channel 1 鈥?nbsp;8 - The Hardw` |
| 182 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 183 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md` | `鈼?` | `●` | `C  \| GND  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 184 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 185 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md` | `鈼?` | `●` | `C  \| GND  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 186 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 187 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 188 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.02.07_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 189 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 190 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 191 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 192 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 193 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 194 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 195 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 196 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 197 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 198 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 199 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 200 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 201 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.03_PS1600_pogo_pin_assignment.md` | `鈩?` | `™` | `13 - D15  \|   \| D14 - D16  \|    \|    The SmartLoop鈩? loopback scheme (` |
| 202 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 203 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈼?` | `●` | `GND  \| DGNDS‑A \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 204 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 205 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈼?` | `●` | `GND  \| DGNDS‑A \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 206 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈼?` | `●` | `GND  \| DGNDS‑A \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 207 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 208 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 209 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 210 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 211 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 212 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 213 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 214 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 215 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 216 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 217 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.05_PS5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 218 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.06_PS9G_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md` | `鈩?` | `™` | ` general use in all applications. - [The SmartLoop鈩?loopback scheme](<` |
| 219 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.06_PS9G_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md` | `鈩?` | `™` | ` general use in all applications. - [The SmartLoop鈩?loopback scheme](<` |
| 220 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.11_Link_Scale_USB3_pogo_pin_assignment.md` | `鈥?` | `…` | ` High-density (HD) pogo block   \|  \|   \| Block AB 鈥?GH: 4 x 16 channel` |
| 221 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.11_Link_Scale_USB3_pogo_pin_assignment.md` | `鈼?` | `●` | `6  \| GND  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 222 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.01_PMUX01_Power_MUX_pogo_pin_assignment.md` | `鈼?` | `●` | `  \|   \| a  \| b  \| c  \| d \|  \| Orientation mark  \| 鈼?/strong>  \|   \|   ` |
| 223 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.05.02_MUX_cards_filling_rules.md` | `鈩?` | `™` | ` frame. The supported MUX cards for a Direct-Probe鈩?configuration are ` |
| 224 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 225 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 226 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 227 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 228 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 229 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 230 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 231 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 232 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 233 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `‑` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 234 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 235 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 236 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 237 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 238 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 239 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 240 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 241 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 242 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 243 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 244 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 245 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 246 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 247 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 248 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 249 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01.01_WSMM_Card_Cage_RFIM18___RFIM6_channel_transformation.md` | `鈥?` | `…` | `8 / RFIM-18 bracket assembly (E8027BRA)   The RFIM鈥?/8 / RFIM鈥?8 brack` |
| 250 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01_WSMM_Card_Cage_DUT_Interface.md` | `鈥?` | `‑` | `e with the internal RF‑related routing of two RFIM鈥?8 modules and two ` |
| 251 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.01_WSMM_Card_Cage_DUT_Interface.md` | `鈥?` | `‑` | `e with the internal RF‑related routing of two RFIM鈥?8 modules and two ` |
| 252 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.02.02.02_WSMM_Family_Board_E8027FAA_pogo_pin_mapping.md` | `鈥?` | `…` | ` build from the WSMM pogo block and the signal 01 鈥?16. For pogo block` |
| 253 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.07.04_Wave_Scale_RF_pogo_pin_assignment__10_MHz_clock.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \|    \| \|` |
| 254 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.md` | `鈥?` | `…` | `ility line with read/write capabilities:  - URW00 鈥?nbsp;URW31    \| Fo` |
| 255 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.md` | `鈥?` | `…` | `ility line with read/write capabilities:  - URW00 鈥?nbsp;URW31    \| Fo` |
| 256 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.md` | `鈥?` | `…` | `ility line with read/write capabilities:  - URW00 鈥?nbsp;URW31    \| Fo` |
| 257 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md` | `鈥?` | `…` | `0 EXA Scale systems, the legacy pogo blocks DPS 1 鈥?nbsp;DPS 8 are use` |
| 258 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md` | `鈥?` | `…` | `0 EXA Scale systems, the legacy pogo blocks DPS 1 鈥?nbsp;DPS 8 are use` |
| 259 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md` | `鈥?` | `…` | `0 EXA Scale systems, the legacy pogo blocks DPS 1 鈥?nbsp;DPS 8 are use` |
| 260 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md` | `鈥?` | `…` | `0 EXA Scale systems, the legacy pogo blocks DPS 1 鈥?nbsp;DPS 8 are use` |
| 261 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.03_Utility_pogo_block_-_LTH_large_DUT_interface.md` | `鈥?` | `…` | `-row](<../../../../raw/153013.png>) \|   \| Block 1 鈥?nbsp;8 \|  \|   \| c ` |
| 262 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.03_Utility_pogo_block_-_LTH_large_DUT_interface.md` | `鈥?` | `…` | `-row](<../../../../raw/153013.png>) \|   \| Block 1 鈥?nbsp;8 \|  \|   \| c ` |
| 263 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.03_Utility_pogo_block_-_LTH_large_DUT_interface.md` | `鈥?` | `…` | `-row](<../../../../raw/153013.png>) \|   \| Block 1 鈥?nbsp;8 \|  \|   \| c ` |
| 264 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.03_Utility_pogo_block_-_LTH_large_DUT_interface.md` | `鈥?` | `…` | `-row](<../../../../raw/153013.png>) \|   \| Block 1 鈥?nbsp;8 \|  \|   \| c ` |
| 265 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.04_Utility_pogo_block_-_STH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 266 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.04_Utility_pogo_block_-_STH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 267 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.04_Utility_pogo_block_-_STH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 268 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.04_Utility_pogo_block_-_STH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 269 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.05_Utility_pogo_block_-_CTH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 270 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.05_Utility_pogo_block_-_CTH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 271 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.05_Utility_pogo_block_-_CTH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 272 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.05_Utility_pogo_block_-_CTH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 273 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.06_Utility_pogo_block_-_ATH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 274 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.06_Utility_pogo_block_-_ATH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 275 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.06_Utility_pogo_block_-_ATH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 276 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.06_Utility_pogo_block_-_ATH_DUT_Scale_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 277 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.07_Utility_pogo_block_-_STH_small_DUT_interface.md` | `鈥?` | `…` | `ility line with read/write capabilities:  - URW00 鈥?nbsp;URW15   \| For` |
| 278 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.07_Utility_pogo_block_-_STH_small_DUT_interface.md` | `鈥?` | `…` | `ility line with read/write capabilities:  - URW00 鈥?nbsp;URW15   \| For` |
| 279 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.07_Utility_pogo_block_-_STH_small_DUT_interface.md` | `鈥?` | `…` | `ility line with read/write capabilities:  - URW00 鈥?nbsp;URW15   \| For` |
| 280 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.08_Utility_pogo_block_-_CTH_small_DUT_interface.md` | `鈥?` | `…` | `ility line with read/write capabilities:  - URW00 鈥?nbsp;URW15   \| For` |
| 281 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.08_Utility_pogo_block_-_CTH_small_DUT_interface.md` | `鈥?` | `…` | `ility line with read/write capabilities:  - URW00 鈥?nbsp;URW15   \| For` |
| 282 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.08_Utility_pogo_block_-_CTH_small_DUT_interface.md` | `鈥?` | `…` | `ility line with read/write capabilities:  - URW00 鈥?nbsp;URW15   \| For` |
| 283 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.09_Utility_pogo_block_-_ATH_small_DUT_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 284 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.09_Utility_pogo_block_-_ATH_small_DUT_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 285 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.09_Utility_pogo_block_-_ATH_small_DUT_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 286 | `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.09_Utility_pogo_block_-_ATH_small_DUT_interface.md` | `鈥?` | `…` | `th read/write capabilities:  - 2-row block: URW00 鈥?nbsp;URW15 - 4-row` |
| 287 | `02_System_reference/02.03_DUT_board_design_reference/02.03.07.04.04_Maintaining_signal_quality_in_mixed-signal_testing.md` | `鈩?` | `Ω` | `f a via is unavoidable, make sure to specify a 50 鈩?equivalent via to ` |
| 288 | `02_System_reference/02.03_DUT_board_design_reference/02.03.07.04.07_Grounding_concept_for_power_applications.md` | `鈮?` | `≥` | ` to the analog ground "AGND".  A 10 Ω resistor of 鈮?1 W connects the "` |
| 289 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.01.04_AVI64_channel_group_and_differential_compare_assignment.md` | `鈥?` | `…` | ` Pogo block   \|  Channels   \|  \|  1   \|  A   \|  1 鈥?nbsp;8   \|  \|  2  ` |
| 290 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.04.03_FVI16_safety_pogo_pins.md` | `鈥?` | `…` | `TY1_5V and SAFETY1_GND are assigned to channels 1 鈥?nbsp;8 while SAFET` |
| 291 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.04.03_FVI16_safety_pogo_pins.md` | `鈥?` | `…` | `TY1_5V and SAFETY1_GND are assigned to channels 1 鈥?nbsp;8 while SAFET` |
| 292 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.04.04_FVI16_ganged_wiring.md` | `鈥?` | `…` | `s are equally distributed to two channel groups 1 鈥?nbsp;8 and 9 鈥?nbs` |
| 293 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.04.04_FVI16_ganged_wiring.md` | `鈥?` | `…` | `s are equally distributed to two channel groups 1 鈥?nbsp;8 and 9 鈥?nbs` |
| 294 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.01_UHC4___UHC4T_recommendations_for_use.md` | `鈥?` | `…` | `against open loop.  We recommend also, adding 4.7 鈥?10 nF bypass capac` |
| 295 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.01_UHC4___UHC4T_recommendations_for_use.md` | `鈥?` | `…` | `against open loop.  We recommend also, adding 4.7 鈥?10 nF bypass capac` |
| 296 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.01_UHC4___UHC4T_recommendations_for_use.md` | `鈥?` | `…` | `against open loop.  We recommend also, adding 4.7 鈥?10 nF bypass capac` |
| 297 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.04.02_Real_capacitors.md` | `鈥?` | `’` | `  Both, ESL and ESR, are considered as ‘parasitics鈥?most of the time. ` |
| 298 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.05.03.04.01_Recipe_for_1_Volt__40_Amp_step_application.md` | `鈩?` | `Ω` | ` ripple.  Steps 1 to 3 provide  - max ESR = 1.25 m鈩?nbsp;(Milli-Ohm), ` |
| 299 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.05.03.04.02_Recipe_for_2_Volt__20_Amp_step_application.md` | `鈩?` | `Ω` | `e ripple.  Steps 1 to 3 provide  - max ESR = 2.5 m鈩?nbsp;(Milli-Ohm), ` |
| 300 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06.05.04.01_Power_planes_stack-up.md` | `鈥?` | `’` | ` an issue with high current. A good ‘rule of thumb鈥? is to have a widt` |
| 301 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.01_XPS256_pogo_pins.md` | `鈥?` | `…` | `voltage range  \| \|  \| XPS256 (EK751HC): \|  -0.5 V 鈥?nbsp;+1.5 V in 1.5` |
| 302 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.01_XPS256_pogo_pins.md` | `鈥?` | `…` | `voltage range  \| \|  \| XPS256 (EK751HC): \|  -0.5 V 鈥?nbsp;+1.5 V in 1.5` |
| 303 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.01_XPS256_pogo_pins.md` | `鈥?` | `…` | `voltage range  \| \|  \| XPS256 (EK751HC): \|  -0.5 V 鈥?nbsp;+1.5 V in 1.5` |
| 304 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.01_XPS256_pogo_pins.md` | `鈥?` | `…` | `voltage range  \| \|  \| XPS256 (EK751HC): \|  -0.5 V 鈥?nbsp;+1.5 V in 1.5` |
| 305 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `→` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 306 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `→` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 307 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `→` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 308 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `→` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 309 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `→` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 310 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `→` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 311 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `→` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 312 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `→` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 313 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `←` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 314 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈫?` | `←` | `andard.md>)  \| DPS128  \| 8  \| none  \| Standard  \| 鈫?/td>  \| Direct  \| ` |
| 315 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈥?` | `…` | `to XPS256   The XPS256 card can replace the DPS128鈥? DPS64 card. Some ` |
| 316 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈥?` | `…` | `to XPS256   The XPS256 card can replace the DPS128鈥? DPS64 card. Some ` |
| 317 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈥?` | `…` | `to XPS256   The XPS256 card can replace the DPS128鈥? DPS64 card. Some ` |
| 318 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈥?` | `…` | `to XPS256   The XPS256 card can replace the DPS128鈥? DPS64 card. Some ` |
| 319 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07.06_DPS128_and_UHC4_migration_to_XPS256.md` | `鈮?` | `≤` | `fnsrc_1>) Total voltage drop on force/ground path 鈮? 0.2.V. ` |
| 320 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07_DC_Scale_XPS256_card.md` | `鈥?` | `…` | `Min/max external voltage at force input  \| -4.5 V 鈥?nbsp;+7.5 V \|  \| M` |
| 321 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07_DC_Scale_XPS256_card.md` | `鈥?` | `…` | `Min/max external voltage at force input  \| -4.5 V 鈥?nbsp;+7.5 V \|  \| M` |
| 322 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07_DC_Scale_XPS256_card.md` | `鈥?` | `…` | `Min/max external voltage at force input  \| -4.5 V 鈥?nbsp;+7.5 V \|  \| M` |
| 323 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07_DC_Scale_XPS256_card.md` | `鈥?` | `…` | `Min/max external voltage at force input  \| -4.5 V 鈥?nbsp;+7.5 V \|  \| M` |
| 324 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.07_DC_Scale_XPS256_card.md` | `鈥?` | `…` | `Min/max external voltage at force input  \| -4.5 V 鈥?nbsp;+7.5 V \|  \| M` |
| 325 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.01.04_PS5000_ground_sensing.md` | `鈥?` | `…` | `lock>):    - "DGNDS‑A" is assigned to channels A1 鈥?nbsp;A16.  - [HD p` |
| 326 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.01.04_PS5000_ground_sensing.md` | `鈥?` | `…` | `lock>):    - "DGNDS‑A" is assigned to channels A1 鈥?nbsp;A16.  - [HD p` |
| 327 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.01.04_PS5000_ground_sensing.md` | `鈥?` | `…` | `lock>):    - "DGNDS‑A" is assigned to channels A1 鈥?nbsp;A16.  - [HD p` |
| 328 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.01.04_PS5000_ground_sensing.md` | `鈥?` | `…` | `lock>):    - "DGNDS‑A" is assigned to channels A1 鈥?nbsp;A16.  - [HD p` |
| 329 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.01.04_PS5000_ground_sensing.md` | `鈥?` | `…` | `lock>):    - "DGNDS‑A" is assigned to channels A1 鈥?nbsp;A16.  - [HD p` |
| 330 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.01.04_PS5000_ground_sensing.md` | `鈥?` | `…` | `lock>):    - "DGNDS‑A" is assigned to channels A1 鈥?nbsp;A16.  - [HD p` |
| 331 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.03.03_Link_Scale_USB3_card.md` | `鈥?` | `…` | `is 12 inches.   - The width of traces should be 6 鈥?nbsp;8 mils.   - O` |
| 332 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.04.04_MUX_cards_design_data.md` | `鈩?` | `™` | `ip>) and [N2605-96570 (PCB layout for Direct-Probe鈩?](<../../../../raw` |
| 333 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.05.03.04.05_Twinning_family_board_design_for_Direct-Probe.md` | `鈩?` | `™` | `d design for Direct-Probe  Due to the Direct-Probe鈩?mechanical require` |
| 334 | `02_System_reference/02.03_DUT_board_design_reference/02.03.08.05.03.05.03_Twinning_DUT_board_design_for_Direct-Probe.md` | `鈩?` | `™` | `-Probe  Twinning DUT board design for Direct-Probe鈩?wafer probing appl` |
| 335 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.01_Direct-Probe_probe_card_specifications.md` | `鈩?` | `™` | ` gives general specifications for the Direct-Probe鈩?interface valid fo` |
| 336 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02.01_Direct-Probe_PSRF_tower_connection_specifications.md` | `鈩?` | `™` | `interface N2392A is not compatible to Direct-Probe鈩?  For general Dire` |
| 337 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02.01_Direct-Probe_PSRF_tower_connection_specifications.md` | `鈩?` | `™` | `interface N2392A is not compatible to Direct-Probe鈩?  For general Dire` |
| 338 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02.02_RF_interface_port_assignment_for_Direct-Probe.md` | `鈩?` | `™` | `ng scheme and port assignment for the Direct-Probe鈩?RF interface solut` |
| 339 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02.03_Direct-Probe_RF_Interconnect_Board.md` | `鈩?` | `™` | `ect_docking_test.md>)  The purpose of Direct Probe鈩?Interconnect Board` |
| 340 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02.03_Direct-Probe_RF_Interconnect_Board.md` | `鈩?` | `™` | `ect_docking_test.md>)  The purpose of Direct Probe鈩?Interconnect Board` |
| 341 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02.03_Direct-Probe_RF_Interconnect_Board.md` | `鈩?` | `™` | `ect_docking_test.md>)  The purpose of Direct Probe鈩?Interconnect Board` |
| 342 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02.03_Direct-Probe_RF_Interconnect_Board.md` | `鈩?` | `™` | `ect_docking_test.md>)  The purpose of Direct Probe鈩?Interconnect Board` |
| 343 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02_Direct-Probe_PSRF_probe_card_specifications.md` | `鈩?` | `™` | `interface N2392A is not compatible to Direct-Probe鈩?  - RF interface N` |
| 344 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02_Direct-Probe_PSRF_probe_card_specifications.md` | `鈩?` | `™` | `interface N2392A is not compatible to Direct-Probe鈩?  - RF interface N` |
| 345 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02_Direct-Probe_PSRF_probe_card_specifications.md` | `鈩?` | `™` | `interface N2392A is not compatible to Direct-Probe鈩?  - RF interface N` |
| 346 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.03.01_Direct-Probe_products_from_vendors.md` | `鈩?` | `™` | `g products aligned with the Advantest Direct-Probe鈩?specifications.  #` |
| 347 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.03.01_Direct-Probe_products_from_vendors.md` | `鈩?` | `™` | `g products aligned with the Advantest Direct-Probe鈩?specifications.  #` |
| 348 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.03.01_Direct-Probe_products_from_vendors.md` | `鈩?` | `™` | `g products aligned with the Advantest Direct-Probe鈩?specifications.  #` |
| 349 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.03.01_Direct-Probe_products_from_vendors.md` | `鈩?` | `™` | `g products aligned with the Advantest Direct-Probe鈩?specifications.  #` |
| 350 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.03.05.01_Step_1__Check_stiffener_specification.md` | `鈮?` | `≤` | `within 315 x 214 mm zone.   Note A parallelism of 鈮?0.03 mm is require` |
| 351 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.03.05.01_Step_1__Check_stiffener_specification.md` | `鈮?` | `≤` | `within 315 x 214 mm zone.   Note A parallelism of 鈮?0.03 mm is require` |
| 352 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.03.05.03_Step_3__Backer_height_measurement.md` | `鈮?` | `≥` | `the thickness gauge. the height required is to be 鈮?0.00 mm.    ![Dire` |
| 353 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.03_Direct-Probe_design_specifications.md` | `鈩?` | `™` | `on using design examples on Advantest Direct-Probe鈩?  For a more gener` |
| 354 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.01_Bridge_Beam_Direct_Probe_for_Digital_and_Mixed_Signal__E8016BBD.md` | `鈩?` | `™` | `tness at very high probe counts.    ![Direct-Probe鈩?Bridge Beam E8016B` |
| 355 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.01_Bridge_Beam_Direct_Probe_for_Digital_and_Mixed_Signal__E8016BBD.md` | `鈩?` | `™` | `tness at very high probe counts.    ![Direct-Probe鈩?Bridge Beam E8016B` |
| 356 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.01_Bridge_Beam_Direct_Probe_for_Digital_and_Mixed_Signal__E8016BBD.md` | `鈩?` | `™` | `tness at very high probe counts.    ![Direct-Probe鈩?Bridge Beam E8016B` |
| 357 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md` | `鈩?` | `™` | `) supports the connection to the PSRF Direct-Probe鈩?tower of the teste` |
| 358 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md` | `鈩?` | `™` | `) supports the connection to the PSRF Direct-Probe鈩?tower of the teste` |
| 359 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md` | `鈩?` | `™` | `) supports the connection to the PSRF Direct-Probe鈩?tower of the teste` |
| 360 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md` | `鈩?` | `™` | `) supports the connection to the PSRF Direct-Probe鈩?tower of the teste` |
| 361 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md` | `鈩?` | `™` | `) supports the connection to the PSRF Direct-Probe鈩?tower of the teste` |
| 362 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md` | `鈩?` | `™` | `) supports the connection to the PSRF Direct-Probe鈩?tower of the teste` |
| 363 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md` | `鈩?` | `™` | `) supports the connection to the PSRF Direct-Probe鈩?tower of the teste` |
| 364 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md` | `鈩?` | `™` | `) supports the connection to the PSRF Direct-Probe鈩?tower of the teste` |
| 365 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.02_Bridge_Beam_Direct_Probe_for_PSRF__E8016BBRF.md` | `鈩?` | `™` | `) supports the connection to the PSRF Direct-Probe鈩?tower of the teste` |
| 366 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.03_Bridge_Beam_Direct_Probe_for_WSRF_and_PMUX__E8016BBWS.md` | `鈩?` | `™` | `dules can access the DUT board or the Direct-Probe鈩?probe card.    The` |
| 367 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.03_Bridge_Beam_Direct_Probe_for_WSRF_and_PMUX__E8016BBWS.md` | `鈥?` | `…` | `in the inner four slots (Pogo block positions 901 鈥?nbsp;904 and 909 鈥` |
| 368 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.03_Bridge_Beam_Direct_Probe_for_WSRF_and_PMUX__E8016BBWS.md` | `鈥?` | `…` | `in the inner four slots (Pogo block positions 901 鈥?nbsp;904 and 909 鈥` |
| 369 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.03_Bridge_Beam_Direct_Probe_for_WSRF_and_PMUX__E8016BBWS.md` | `鈩?` | `™` | `dules can access the DUT board or the Direct-Probe鈩?probe card.    The` |
| 370 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.03_Bridge_Beam_Direct_Probe_for_WSRF_and_PMUX__E8016BBWS.md` | `鈩?` | `™` | `dules can access the DUT board or the Direct-Probe鈩?probe card.    The` |
| 371 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.04_Bridge_Beam_Direct_Probe_for_special_WSRF__PMUX_and_WSMM__E8016BBMM.md` | `鈩?` | `™` | `dules can access the DUT board or the Direct-Probe鈩?probe card. Compar` |
| 372 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.04_Bridge_Beam_Direct_Probe_for_special_WSRF__PMUX_and_WSMM__E8016BBMM.md` | `鈩?` | `™` | `dules can access the DUT board or the Direct-Probe鈩?probe card. Compar` |
| 373 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04.04_Bridge_Beam_Direct_Probe_for_special_WSRF__PMUX_and_WSMM__E8016BBMM.md` | `鈩?` | `™` | `dules can access the DUT board or the Direct-Probe鈩?probe card. Compar` |
| 374 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04_Direct-Probe_bridge_beams.md` | `鈩?` | `™` | ` three different bridge beams for the Direct-Probe鈩?technology. The th` |
| 375 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04_Direct-Probe_bridge_beams.md` | `鈩?` | `™` | ` three different bridge beams for the Direct-Probe鈩?technology. The th` |
| 376 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.04_Direct-Probe_bridge_beams.md` | `鈩?` | `™` | ` three different bridge beams for the Direct-Probe鈩?technology. The th` |
| 377 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.05.03.01_Test_head_alignment_for_probing_with_the_Wave_Scale_Millimeter_solution.md` | `鈮?` | `≤` | `he WSMM solution, the test head planarity must be 鈮? 0.1° in reference` |
| 378 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.05.03.01_Test_head_alignment_for_probing_with_the_Wave_Scale_Millimeter_solution.md` | `鈮?` | `≤` | `he WSMM solution, the test head planarity must be 鈮? 0.1° in reference` |
| 379 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.05.03.01_Test_head_alignment_for_probing_with_the_Wave_Scale_Millimeter_solution.md` | `鈮?` | `≤` | `he WSMM solution, the test head planarity must be 鈮? 0.1° in reference` |
| 380 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.07.01_Hiding_the_wafer_prober_chuck.md` | `鈩?` | `™` | ` proceed with the installation of the Direct Probe鈩?Bridge Beam hardwa` |
| 381 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.07.03.01_Bridge_beam_installation_on_Accretech_UF3000_EX_-_Phase_1.md` | `鈩?` | `™` | `o persons are required to install the Direct Probe鈩?Bridge Beam hardwa` |
| 382 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.07.03.03_Bridge_beam_installation_on_Accretech_UF3000_EX_-_Phase_2.md` | `鈩?` | `™` | `o persons are required to install the Direct Probe鈩?Bridge Beam hardwa` |
| 383 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.07.03.04.01_Verification_Phase_2_-_Stage_1.md` | `鈥?` | `”` | `g area with the "high" stiffener, remove the “high鈥?stiffener from the` |
| 384 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.07.04_Loading_a_DUT_board_on_the_Accretech_UF3000_EX_wafer_prober.md` | `鈩?` | `™` | `UT board, you must have installed the Direct Probe鈩?Bridge Beam on the` |
| 385 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.07_Interfacing_the_test_system_to_Accretech_UF3000_EX_wafer_prober.md` | `鈩?` | `™` | ` special piece of hardware called the Direct Probe鈩?Bridge Beam - inst` |
| 386 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.07_Interfacing_the_test_system_to_Accretech_UF3000_EX_wafer_prober.md` | `鈩?` | `™` | ` special piece of hardware called the Direct Probe鈩?Bridge Beam - inst` |
| 387 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08.01_Protecting_the_chuck_on_the_wafer_prober.md` | `鈩?` | `™` | ` proceed with the installation of the Direct Probe鈩?Bridge Beam hardwa` |
| 388 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08.02_Installing_Direct-Probe_bridge_beam_on_TEL_Precio_wafer_prober.md` | `鈩?` | `™` | `o persons are required to install the Direct Probe鈩?Bridge Beam hardwa` |
| 389 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08_Interfacing_the_test_system_to_TEL_Precio_wafer_prober.md` | `鈩?` | `™` | ` special piece of hardware called the Direct Probe鈩?Bridge Beam. This ` |
| 390 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.08_Interfacing_the_test_system_to_TEL_Precio_wafer_prober.md` | `鈩?` | `™` | ` special piece of hardware called the Direct Probe鈩?Bridge Beam. This ` |
| 391 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11.01_Direct-Probe_interface.md` | `鈩?` | `™` | `1.09_Semics_OPUS3_compatibility.md>)  Direct-Probe鈩?technology is a co` |
| 392 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11_Wafer_prober_interfaces.md` | `鈩?` | `™` | `e test head and the wafer prober.  ## Direct-Probe鈩?wafer prober inter` |
| 393 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11_Wafer_prober_interfaces.md` | `鈩?` | `™` | `e test head and the wafer prober.  ## Direct-Probe鈩?wafer prober inter` |
| 394 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11_Wafer_prober_interfaces.md` | `鈩?` | `™` | `e test head and the wafer prober.  ## Direct-Probe鈩?wafer prober inter` |
| 395 | `02_System_reference/02.03_DUT_board_design_reference/02.03.11_Wafer_prober_interfaces.md` | `鈩?` | `™` | `e test head and the wafer prober.  ## Direct-Probe鈩?wafer prober inter` |
| 396 | `02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.01_Direct-Probe_probe_card_layout_information.md` | `鈩?` | `™` | `ayout information  Below you find the Direct-Probe鈩?card layout relate` |
| 397 | `02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md` | `鈩?` | `™` | `t-Probe stiffener  Below you find the Direct-Probe鈩?stiffener related ` |
| 398 | `02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.11_MUX_cards_design_data.md` | `鈩?` | `™` | `ip>) and [N2605-96570 (PCB layout for Direct-Probe鈩?](<../../../../raw` |
| 399 | `02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.23_Wave_Scale_RF_PCB_layout_and_stiffener_info_for_Direct-Probe.md` | `鈩?` | `™` | `ip>) and [N2605-96570 (PCB layout for Direct-Probe鈩?](<../../../../raw` |
| 400 | `02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.24_Wave_Scale_RF_PCB_layout_and_stiffener_info_for_final_test.md` | `鈩?` | `™` | `ip>) and [N2605-96570 (PCB layout for Direct-Probe鈩?](<../../../../raw` |
| 401 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.01.02_CARD_CONFIGURATION_section.md` | `鈥?` | `…` | `can also be the one digit DPS pogo block number 1 鈥? 8.   - Valid pogo` |
| 402 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.01_Model_file_reference__tester.model.md` | `鈩?` | `™` | `ple, the PS5000 card can only be used in EXA Scale鈩?test systems. PS16` |
| 403 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.01_Model_file_reference__tester.model.md` | `鈩?` | `™` | `ple, the PS5000 card can only be used in EXA Scale鈩?test systems. PS16` |
| 404 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md` | `鈮?` | `≥` | `e settings from the model file.  RHEL 7 (SmarTest 鈮?7.5):  - Port 1: `` |
| 405 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md` | `鈮?` | `≥` | `e settings from the model file.  RHEL 7 (SmarTest 鈮?7.5):  - Port 1: `` |
| 406 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 407 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 408 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 409 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 410 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 411 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.03_IOCHANNEL_section.md` | `鈩?` | `™` | `rds.  The "PHY test bundle" combines the SmartLoop鈩?external loopback ` |
| 412 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.08.01.04_Entitlements.md` | `鈥?` | `–` | `ists of entitlements.  - My assigned entitlements 鈥?Displays a list of` |
| 413 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.08.01.04_Entitlements.md` | `鈥?` | `–` | `ists of entitlements.  - My assigned entitlements 鈥?Displays a list of` |
| 414 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.08.01.05_Renewing_your_licenses.md` | `鈥?` | `–` | `tivated licenses are available, the Renew license 鈥?server overview pa` |
| 415 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.08.01.05_Renewing_your_licenses.md` | `鈥?` | `–` | `tivated licenses are available, the Renew license 鈥?server overview pa` |
| 416 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.10.03_Adding_entitlement_IDs_and_organization_to_a_user_account.md` | `鈥?` | `…` | `age is displayed.  -  Click Entitlement not listed鈥?/span>  The Assign` |
| 417 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.13.03.02_Advantest_FlexNet_Embedded_license_server_tools.md` | `鈥?` | `…` | `ion  \| /usr/local/bin/ \|  \| Options  \| Log level 1鈥?  Logfile <show sp` |
| 418 | `02_System_reference/02.04_Model_File_and_Licensing/02.04.13_FlexNet_Embedded_licensing.md` | `鈮?` | `≥` | `dded licensing can be used with SmarTest versions 鈮?8.1.  - FNE archit` |
| 419 | `02_System_reference/02.05_Test_Head_Cards/02.05.01.04_Pogo_mapping.md` | `鈥?` | `…` | `ID used for pogo mapping \|  \| CX  \| 1  \| 1  \| 101 鈥?109 \|  \| SX  \| 1, ` |
| 420 | `02_System_reference/02.05_Test_Head_Cards/02.05.01.04_Pogo_mapping.md` | `鈥?` | `…` | `ID used for pogo mapping \|  \| CX  \| 1  \| 1  \| 101 鈥?109 \|  \| SX  \| 1, ` |
| 421 | `02_System_reference/02.05_Test_Head_Cards/02.05.01.04_Pogo_mapping.md` | `鈥?` | `…` | `ID used for pogo mapping \|  \| CX  \| 1  \| 1  \| 101 鈥?109 \|  \| SX  \| 1, ` |
| 422 | `02_System_reference/02.05_Test_Head_Cards/02.05.01.04_Pogo_mapping.md` | `鈥?` | `…` | `ID used for pogo mapping \|  \| CX  \| 1  \| 1  \| 101 鈥?109 \|  \| SX  \| 1, ` |
| 423 | `02_System_reference/02.05_Test_Head_Cards/02.05.01.04_Pogo_mapping.md` | `鈥?` | `…` | `ID used for pogo mapping \|  \| CX  \| 1  \| 1  \| 101 鈥?109 \|  \| SX  \| 1, ` |
| 424 | `02_System_reference/02.05_Test_Head_Cards/02.05.01.04_Pogo_mapping.md` | `鈥?` | `…` | `ID used for pogo mapping \|  \| CX  \| 1  \| 1  \| 101 鈥?109 \|  \| SX  \| 1, ` |
| 425 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.01_PS1600_overview.md` | `鈩?` | `™` | `dard pattern space (32k per pin)   \|  \|  SmartLoop鈩?/p> \|  Active, ret` |
| 426 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.01_PS1600_overview.md` | `鈮?` | `≤` | `hangeable   \|  Speed  \|  Maximum I/O data rate at 鈮?1.8 V (pattern, PR` |
| 427 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.01_PS1600_overview.md` | `鈩?` | `™` | `dard pattern space (32k per pin)   \|  \|  SmartLoop鈩?/p> \|  Active, ret` |
| 428 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.01_PS1600_overview.md` | `鈮?` | `≤` | `hangeable   \|  Speed  \|  Maximum I/O data rate at 鈮?1.8 V (pattern, PR` |
| 429 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.01_PS1600_overview.md` | `鈩?` | `™` | `dard pattern space (32k per pin)   \|  \|  SmartLoop鈩?/p> \|  Active, ret` |
| 430 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.01_PS1600_overview.md` | `鈮?` | `≤` | `hangeable   \|  Speed  \|  Maximum I/O data rate at 鈮?1.8 V (pattern, PR` |
| 431 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.01_PS1600_overview.md` | `鈮?` | `≤` | `hangeable   \|  Speed  \|  Maximum I/O data rate at 鈮?1.8 V (pattern, PR` |
| 432 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.06.01_PS1600_Voltage_force_and_measure.md` | `鈮?` | `≤` | `nge  within range 1 (± 40 mA)  within range 2..5 (鈮?± 1 mA)   \|  Volta` |
| 433 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.06.01_PS1600_Voltage_force_and_measure.md` | `鈮?` | `≥` | `nge  within range 1 (± 40 mA)  within range 2..5 (鈮?± 1 mA)   \|  Volta` |
| 434 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.06.01_PS1600_Voltage_force_and_measure.md` | `鈮?` | `≤` | `nge  within range 1 (± 40 mA)  within range 2..5 (鈮?± 1 mA)   \|  Volta` |
| 435 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.02.06.02_PS1600_Current_force_and_measure.md` | `鈮?` | `≤` | `  Range 1 force current up to ±56 mA for voltages 鈮?3.3 V. Range 1 for` |
| 436 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03.06_PS1600_SmartLoop__loopback_testing.md` | `鈩?` | `™` | `rn, or hardware based PRBS sequences.  - SmartLoop鈩?(external loop bac` |
| 437 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03.06_PS1600_SmartLoop__loopback_testing.md` | `鈩?` | `™` | `rn, or hardware based PRBS sequences.  - SmartLoop鈩?(external loop bac` |
| 438 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03_PS1600_functionality_and_features.md` | `鈩?` | `™` | `easurement of values. - A loopback mode (SmartLoop鈩? is also supported` |
| 439 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03_PS1600_functionality_and_features.md` | `鈩?` | `™` | `easurement of values. - A loopback mode (SmartLoop鈩? is also supported` |
| 440 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.04.01_Identifying_Pin_Scale_vs._Smart_Scale_test_systems.md` | `鈼?` | `○` | `  \| Pin Scale  \| Smart Scale \|  \| PS1600, PSSL  \| 鈼?/td>  \| 鈼?/td> \|  ` |
| 441 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.04.01_Identifying_Pin_Scale_vs._Smart_Scale_test_systems.md` | `鈼?` | `●` | `  \| Pin Scale  \| Smart Scale \|  \| PS1600, PSSL  \| 鈼?/td>  \| 鈼?/td> \|  ` |
| 442 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.04.01_Identifying_Pin_Scale_vs._Smart_Scale_test_systems.md` | `鈼?` | `○` | `  \| Pin Scale  \| Smart Scale \|  \| PS1600, PSSL  \| 鈼?/td>  \| 鈼?/td> \|  ` |
| 443 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.04.01_Identifying_Pin_Scale_vs._Smart_Scale_test_systems.md` | `鈼?` | `○` | `  \| Pin Scale  \| Smart Scale \|  \| PS1600, PSSL  \| 鈼?/td>  \| 鈼?/td> \|  ` |
| 444 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.04.01_Identifying_Pin_Scale_vs._Smart_Scale_test_systems.md` | `鈼?` | `●` | `  \| Pin Scale  \| Smart Scale \|  \| PS1600, PSSL  \| 鈼?/td>  \| 鈼?/td> \|  ` |
| 445 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.04.01_Identifying_Pin_Scale_vs._Smart_Scale_test_systems.md` | `鈼?` | `○` | `  \| Pin Scale  \| Smart Scale \|  \| PS1600, PSSL  \| 鈼?/td>  \| 鈼?/td> \|  ` |
| 446 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.04.01_Identifying_Pin_Scale_vs._Smart_Scale_test_systems.md` | `鈼?` | `●` | `  \| Pin Scale  \| Smart Scale \|  \| PS1600, PSSL  \| 鈼?/td>  \| 鈼?/td> \|  ` |
| 447 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.04.01_Identifying_Pin_Scale_vs._Smart_Scale_test_systems.md` | `鈼?` | `●` | `  \| Pin Scale  \| Smart Scale \|  \| PS1600, PSSL  \| 鈼?/td>  \| 鈼?/td> \|  ` |
| 448 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 449 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 450 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 451 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 452 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 453 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 454 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 455 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 456 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 457 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 458 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 459 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 460 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.06_PS1600_pogo_pin_assignment.md` | `鈩?` | `™` | `13 - D15  \|   \| D14 - D16  \|    \|    The SmartLoop鈩? loopback scheme  ` |
| 461 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.01.01_PS1600_DC_offset.md` | `鈮?` | `≠` | ` this mate pull-down resistor. That is, a voltage 鈮?DUTGND is present ` |
| 462 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.01.01_PS1600_DC_offset.md` | `鈮?` | `≠` | ` this mate pull-down resistor. That is, a voltage 鈮?DUTGND is present ` |
| 463 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.01.01_PS1600_DC_offset.md` | `鈮?` | `≠` | ` this mate pull-down resistor. That is, a voltage 鈮?DUTGND is present ` |
| 464 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.01.01_PS1600_DC_offset.md` | `鈮?` | `≠` | ` this mate pull-down resistor. That is, a voltage 鈮?DUTGND is present ` |
| 465 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.01_Pull-down_function.md` | `鈩?` | `Ω` | `rcuitry of a PS1600 card offers an internal 14.3 k鈩?pull-down resistor` |
| 466 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.02_PS1600_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... H are mapped to pogo block positions "101" 鈥?nbsp;"108". The co` |
| 467 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.02_PS1600_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... H are mapped to pogo block positions "101" 鈥?nbsp;"108". The co` |
| 468 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.02_PS1600_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... H are mapped to pogo block positions "101" 鈥?nbsp;"108". The co` |
| 469 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.02_PS1600_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... H are mapped to pogo block positions "101" 鈥?nbsp;"108". The co` |
| 470 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.02_PS1600_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... H are mapped to pogo block positions "101" 鈥?nbsp;"108". The co` |
| 471 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.07.02_PS1600_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... H are mapped to pogo block positions "101" 鈥?nbsp;"108". The co` |
| 472 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.01_Pin_Scale_5000_sitemap.md` | `鈩?` | `™` | `emap  The Pin Scale 5000 (PS5000) is the EXA Scale鈩?generation digital` |
| 473 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `™` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 474 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `Ω` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 475 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `™` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 476 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 477 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 478 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 479 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `Ω` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 480 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 481 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 482 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 483 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 484 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 485 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈮?` | `≤` | `e (pattern, PRBS, SmartLoop鈩?   \|  > 4.0 Gbps but 鈮?5.0 Gbps at 鈮?1.0 ` |
| 486 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `K` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 487 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 488 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 489 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 490 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 491 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 492 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 493 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 494 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 495 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 496 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 497 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 498 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℃` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 499 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 500 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.01_Pin_Scale_5000_basic_parameters.md` | `鈩?` | `℉` | `rn space (64 KiByte per channel)   \|  \|  SmartLoop鈩?/p> \|  Active, re-` |
| 501 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.02_Pin_Scale_5000_vector_memory.md` | `鈥?` | `…` | `  \|  1,792 M   \|  \|  X5鈥8-mode   \|  5 Gbps   \|  5鈥?   \|  1 drive + 1 ` |
| 502 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.02_Pin_Scale_5000_vector_memory.md` | `鈥?` | `…` | `  \|  1,792 M   \|  \|  X5鈥8-mode   \|  5 Gbps   \|  5鈥?   \|  1 drive + 1 ` |
| 503 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.03_Pin_Scale_5000_timing.md` | `鈩?` | `Ω` | `the following figures:  - Vswing = 500 mV into 50 鈩?at a single connec` |
| 504 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.03_Pin_Scale_5000_timing.md` | `鈩?` | `Ω` | `the following figures:  - Vswing = 500 mV into 50 鈩?at a single connec` |
| 505 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.03_Pin_Scale_5000_timing.md` | `鈥?` | `…` | `sight E5052B, phase noise integration range 1 kHz 鈥? 40 MHz[2)](<>) Me` |
| 506 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.03_Pin_Scale_5000_timing.md` | `鈥?` | `…` | `sight E5052B, phase noise integration range 1 kHz 鈥? 40 MHz[2)](<>) Me` |
| 507 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.04_Pin_Scale_5000_driver.md` | `鈩?` | `Ω` | `ition: half the noted voltage, terminated into 50 鈩?   \|  \|  Maximum t` |
| 508 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.04_Pin_Scale_5000_driver.md` | `鈮?` | `≤` | `into open   \|  \|  High level (vih) range at \|VGS\| 鈮?100 mV   \|  Fast m` |
| 509 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.04_Pin_Scale_5000_driver.md` | `鈮?` | `≤` | `into open   \|  \|  High level (vih) range at \|VGS\| 鈮?100 mV   \|  Fast m` |
| 510 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.04_Pin_Scale_5000_driver.md` | `鈩?` | `Ω` | `ition: half the noted voltage, terminated into 50 鈩?   \|  \|  Maximum t` |
| 511 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.04_Pin_Scale_5000_driver.md` | `鈩?` | `Ω` | `ition: half the noted voltage, terminated into 50 鈩?   \|  \|  Maximum t` |
| 512 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.04_Pin_Scale_5000_driver.md` | `鈩?` | `Ω` | `ition: half the noted voltage, terminated into 50 鈩?   \|  \|  Maximum t` |
| 513 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.05_Pin_Scale_5000_receiver.md` | `鈮?` | `≤` | `) \|  \| Input voltage and threshold range at \|VGS\| 鈮?100 mV  \| -1.5 V t` |
| 514 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.05_Pin_Scale_5000_receiver.md` | `鈩?` | `Ω` | `gle-ended impedance  \| -1.5 V 鈮?VSE 鈮?3.0 V  \| 50 鈩?± 3 鈩?/td> \|  \| VS` |
| 515 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.05_Pin_Scale_5000_receiver.md` | `鈮?` | `≤` | `) \|  \| Input voltage and threshold range at \|VGS\| 鈮?100 mV  \| -1.5 V t` |
| 516 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.05_Pin_Scale_5000_receiver.md` | `鈩?` | `Ω` | `gle-ended impedance  \| -1.5 V 鈮?VSE 鈮?3.0 V  \| 50 鈩?± 3 鈩?/td> \|  \| VS` |
| 517 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.09_Pin_Scale_5000_parametric_measurement_unit.md` | `鈩?` | `Ω` | ` current. R is the maximum wiring resistance of 1 鈩?   \| Voltage force` |
| 518 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.09_Pin_Scale_5000_parametric_measurement_unit.md` | `鈮?` | `≤` | `asure \|  \| Voltage force / measure range at \|VGS\| 鈮? 100 mV  \| I 鈮?25 ` |
| 519 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.09_Pin_Scale_5000_parametric_measurement_unit.md` | `鈮?` | `≤` | `asure \|  \| Voltage force / measure range at \|VGS\| 鈮? 100 mV  \| I 鈮?25 ` |
| 520 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.11_Pin_Scale_5000_high_voltage_protection.md` | `鈮?` | `≤` | `+10 V ... +80 V \|  \| Overvoltage reaction time  \| 鈮?15 ns \|  \| Overcur` |
| 521 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.11_Pin_Scale_5000_high_voltage_protection.md` | `鈮?` | `≥` | `+10 V ... +80 V \|  \| Overvoltage reaction time  \| 鈮?15 ns \|  \| Overcur` |
| 522 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.11_Pin_Scale_5000_high_voltage_protection.md` | `鈮?` | `≤` | `+10 V ... +80 V \|  \| Overvoltage reaction time  \| 鈮?15 ns \|  \| Overcur` |
| 523 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.14_Pin_Scale_5000_terms.md` | `鈮?` | `≥` | `ly connected to the DUT, enable to compensate for 鈮?97% (or 鈮?94% for ` |
| 524 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02.14_Pin_Scale_5000_terms.md` | `鈮?` | `≥` | `ly connected to the DUT, enable to compensate for 鈮?97% (or 鈮?94% for ` |
| 525 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02_PS5000_specifications.md` | `鈩?` | `™` | `digital card to execute digital tests on EXA Scale鈩?test systems.  ![O` |
| 526 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02_PS5000_specifications.md` | `鈩?` | `™` | `digital card to execute digital tests on EXA Scale鈩?test systems.  ![O` |
| 527 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02_PS5000_specifications.md` | `鈩?` | `™` | `digital card to execute digital tests on EXA Scale鈩?test systems.  ![O` |
| 528 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.02_PS5000_specifications.md` | `鈩?` | `™` | `digital card to execute digital tests on EXA Scale鈩?test systems.  ![O` |
| 529 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 530 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈼?` | `●` | `GND  \| DGNDS‑A \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 531 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 532 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈼?` | `●` | `GND  \| DGNDS‑A \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 533 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈼?` | `●` | `GND  \| DGNDS‑A \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 534 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 535 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 536 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 537 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 538 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 539 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 540 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 541 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 542 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 543 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 544 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.06_Pin_Scale_5000_pogo_pin_assignment.md` | `鈥?` | `…` | `HD pogo block but can access only the channels A1 鈥?nbsp;A16 on rows b` |
| 545 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.01_Pull-down_function.md` | `鈩?` | `Ω` | `rcuitry of a PS1600 card offers an internal 14.3 k鈩?pull-down resistor` |
| 546 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.03.01_Pin_Scale_5000_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... P are mapped to pogo block positions "101" 鈥?nbsp;"116". The co` |
| 547 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.03.01_Pin_Scale_5000_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... P are mapped to pogo block positions "101" 鈥?nbsp;"116". The co` |
| 548 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.03.01_Pin_Scale_5000_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... P are mapped to pogo block positions "101" 鈥?nbsp;"116". The co` |
| 549 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.03.01_Pin_Scale_5000_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... P are mapped to pogo block positions "101" 鈥?nbsp;"116". The co` |
| 550 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.03.01_Pin_Scale_5000_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... P are mapped to pogo block positions "101" 鈥?nbsp;"116". The co` |
| 551 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.03.01_Pin_Scale_5000_card_configuration_in_the_model_file.md` | `鈥?` | `…` | ` A ... P are mapped to pogo block positions "101" 鈥?nbsp;"116". The co` |
| 552 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02_Pin_Scale_5000_card.md` | `鈩?` | `™` | `000 (PS5000) is the digital base card of EXA Scale鈩? It can be used in` |
| 553 | `02_System_reference/02.05_Test_Head_Cards/02.05.04.02_Pin_Scale_5000_card.md` | `鈩?` | `™` | `000 (PS5000) is the digital base card of EXA Scale鈩? It can be used in` |
| 554 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.02.01_DC_Scale_DPS128_Device_Power_Supply__E8023CS_E8023CSH__-_high_current_sp.md` | `鈮?` | `≤` | `age drop in the Force path beyond the pogo pin of 鈮?nbsp;0.1 V.   ![DP` |
| 555 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128____PS64_power_budget.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 power budge` |
| 556 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128____PS64_power_budget.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 power budge` |
| 557 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128____PS64_power_budget.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 power budge` |
| 558 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128____PS64_power_budget.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 power budge` |
| 559 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128____PS64_power_budget.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 power budge` |
| 560 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128____PS64_power_budget.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 power budge` |
| 561 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128____PS64_power_budget.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 power budge` |
| 562 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128____PS64_power_budget.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 power budge` |
| 563 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.01_E8023PA_pogo_cable_assembly__8_HD_pogo_blocks__Standard.md` | `鈥?` | `…` | `the same pogo pin assignment.   \|   \|   \| Block A 鈥?H \|  \| Pin  \| a  \|` |
| 564 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.01_E8023PA_pogo_cable_assembly__8_HD_pogo_blocks__Standard.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \|    \|  ` |
| 565 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.01_E8023PA_pogo_cable_assembly__8_HD_pogo_blocks__Standard.md` | `鈥?` | `…` | `the same pogo pin assignment.   \|   \|   \| Block A 鈥?H \|  \| Pin  \| a  \|` |
| 566 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks.md` | `鈼?` | `●` | ` GND  \|   \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 567 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.02_E8023PB_pogo_cable_assembly__2_VHD_pogo_blocks.md` | `鈥?` | `…` | `es on the pogo pin descriptions:  - # = Channel 1 鈥?nbsp;16 -  DC/DC p` |
| 568 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.03_E8023PC_pogo_cable_assembly__4_HD_pogo_blocks__DPS128-HC_only.md` | `鈥?` | `…` | `same pogo pin assignment.   \|   \|   \|   \| Block A 鈥?D \|  \|   \| Pin  \| ` |
| 569 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.03_E8023PC_pogo_cable_assembly__4_HD_pogo_blocks__DPS128-HC_only.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \|  \|  Th` |
| 570 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.03_E8023PC_pogo_cable_assembly__4_HD_pogo_blocks__DPS128-HC_only.md` | `鈥?` | `…` | `same pogo pin assignment.   \|   \|   \|   \| Block A 鈥?D \|  \|   \| Pin  \| ` |
| 571 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.04_E8023PD_pogo_cable_assembly__2_HD_pogo_blocks__DPS64_only.md` | `鈼?` | `●` | `NC  \| NC  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \|  \|  Th` |
| 572 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.04_E8023PD_pogo_cable_assembly__2_HD_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16.   \|  For ` |
| 573 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.05_E8023PE_pogo_cable_assembly__8_MS-DPS_style_pogo_blocks__DPS128-HC_only.md` | `鈼?` | `●` | `5+PS16)  \| P4 (P13+P14) \|  \|   \| Orientation mark 鈼?/strong>  \|  \|  Th` |
| 574 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.05_E8023PE_pogo_cable_assembly__8_MS-DPS_style_pogo_blocks__DPS128-HC_only.md` | `鈥?` | `…` | `n the DPS128-HC side  "#" is the channel number 1 鈥?nbsp;16 for DPS128` |
| 575 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.05_E8023PE_pogo_cable_assembly__8_MS-DPS_style_pogo_blocks__DPS128-HC_only.md` | `鈥?` | `…` | `n the DPS128-HC side  "#" is the channel number 1 鈥?nbsp;16 for DPS128` |
| 576 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.06_E8023PF_pogo_cable_assembly__2_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈼?` | `●` | `4  (P9+P10+  P11+P12)   \|  \|   \| Orientation mark 鈼?/strong>  \|   \|  T` |
| 577 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.06_E8023PF_pogo_cable_assembly__2_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16 for DPS64 ` |
| 578 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.06_E8023PF_pogo_cable_assembly__2_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16 for DPS64 ` |
| 579 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.07_E8023PG_pogo_cable_assembly__4_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16 for DPS64 ` |
| 580 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.07_E8023PG_pogo_cable_assembly__4_MS-DPS_style_pogo_blocks__DPS64_only.md` | `鈥?` | `…` | `ls on the DPS64 side  "#" is the channel number 1 鈥?nbsp;16 for DPS64 ` |
| 581 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.08_E8023PH_pogo_cable_assembly__4_HD_pogo_blocks__DPS64_standard.md` | `鈼?` | `●` | ` \| NC  \| NC  \| NC  \| NC \|  \|   \| Orientation mark 鈼?/strong>  \|   \|  T` |
| 582 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.08_E8023PH_pogo_cable_assembly__4_HD_pogo_blocks__DPS64_standard.md` | `鈥?` | `…` | `rovide landing pads.  "#" is the channel number 1 鈥?nbsp;16.   \|  For ` |
| 583 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.09_E8023PK_pogo_cable_assembly__4_VHD_pogo_blocks__DPS128.md` | `鈼?` | `●` | ` GND  \|   \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 584 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08.09_E8023PK_pogo_cable_assembly__4_VHD_pogo_blocks__DPS128.md` | `鈥?` | `…` | `es on the pogo pin descriptions:  - # = Channel 1 鈥?nbsp;16 -  DC/DC p` |
| 585 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 586 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 587 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 588 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 589 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 590 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 591 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 592 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.08_DPS128____PS64_pogo_cable_assemblies_and_pogo_pin_assignments.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 pogo cable ` |
| 593 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 594 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 595 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 596 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 597 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.md` | `鈥?` | `…` | `.5.4.4, 8.3.4.2, and higher.    - For channels A1 鈥?nbsp;A16[1)](<#_14` |
| 598 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09_DPS128____PS64_specific_setup_tasks.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 specific se` |
| 599 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09_DPS128____PS64_specific_setup_tasks.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 specific se` |
| 600 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09_DPS128____PS64_specific_setup_tasks.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 specific se` |
| 601 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09_DPS128____PS64_specific_setup_tasks.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 specific se` |
| 602 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09_DPS128____PS64_specific_setup_tasks.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 specific se` |
| 603 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09_DPS128____PS64_specific_setup_tasks.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 specific se` |
| 604 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09_DPS128____PS64_specific_setup_tasks.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 specific se` |
| 605 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09_DPS128____PS64_specific_setup_tasks.md` | `鈥?` | `…` | `--- title: "DPS128鈥? DPS64 specific se` |
| 606 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.02_UHC4T_specifications.md` | `鈮?` | `≤` | `in these limits for each channel of a board:    - 鈮?0.6 V : 鈮?40 A   -` |
| 607 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.02_UHC4T_specifications.md` | `鈮?` | `≤` | `in these limits for each channel of a board:    - 鈮?0.6 V : 鈮?40 A   -` |
| 608 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.02_UHC4T_specifications.md` | `鈮?` | `≤` | `in these limits for each channel of a board:    - 鈮?0.6 V : 鈮?40 A   -` |
| 609 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.06_UHC4___UHC4T_recommendations_for_use.md` | `鈥?` | `…` | `against open loop.  We recommend also, adding 4.7 鈥?10 nF bypass capac` |
| 610 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.06_UHC4___UHC4T_recommendations_for_use.md` | `鈥?` | `…` | `against open loop.  We recommend also, adding 4.7 鈥?10 nF bypass capac` |
| 611 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.06_UHC4___UHC4T_recommendations_for_use.md` | `鈥?` | `…` | `against open loop.  We recommend also, adding 4.7 鈥?10 nF bypass capac` |
| 612 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 613 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 614 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 615 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 616 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.01_XPS256_overview.md` | `鈥?` | `…` | `imum source current per channel \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 617 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.02_XPS256_voltage_specifications.md` | `鈥?` | `…` | `0735__fn_Measurement_conditions>) \|  \|   \| -0.5 V 鈥?nbsp;+1.5 V  \| 10 ` |
| 618 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.02_XPS256_voltage_specifications.md` | `鈥?` | `…` | `0735__fn_Measurement_conditions>) \|  \|   \| -0.5 V 鈥?nbsp;+1.5 V  \| 10 ` |
| 619 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.02_XPS256_voltage_specifications.md` | `鈥?` | `…` | `0735__fn_Measurement_conditions>) \|  \|   \| -0.5 V 鈥?nbsp;+1.5 V  \| 10 ` |
| 620 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.02_XPS256_voltage_specifications.md` | `鈥?` | `…` | `0735__fn_Measurement_conditions>) \|  \|   \| -0.5 V 鈥?nbsp;+1.5 V  \| 10 ` |
| 621 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 622 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 623 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 624 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 625 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 626 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.03_XPS256_current_specifications.md` | `鈥?` | `…` | `50736__fn_Measurement_conditions>) \|  \|   \| 10 mA 鈥?nbsp;1.0 A  \| 10 µ` |
| 627 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.04_XPS256_voltage_and_current_capability_specifications.md` | `鈮?` | `≤` | `op in the force path beyond the pogo pin of total 鈮?0.5V.  ## Maximum ` |
| 628 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 629 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 630 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 631 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 632 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 633 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 634 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 635 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 636 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 637 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.07_XPS256_other_performance_characteristics.md` | `鈥?` | `…` | `<#fntarg_6>)  \| Range  \| Resolution \|  \|   \| 0 µs 鈥?127 µs  \| 1 µs \|  ` |
| 638 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.08_XPS256_pogo_block_specifications.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 639 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.08_XPS256_pogo_block_specifications.md` | `鈼?` | `●` | `C  \| GND  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 640 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.08_XPS256_pogo_block_specifications.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 641 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02.01.08_XPS256_pogo_block_specifications.md` | `鈼?` | `●` | `C  \| GND  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 642 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02_XPS256_specifications.md` | `鈥?` | `…` | ` 256 channels  \| Source current \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 643 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.02_XPS256_specifications.md` | `鈥?` | `…` | ` 256 channels  \| Source current \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 644 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.03_XPS256_functionality_and_features.md` | `鈥?` | `…` | ` 256 channels  \| Source current \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 645 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.03_XPS256_functionality_and_features.md` | `鈥?` | `…` | ` 256 channels  \| Source current \|  1.0 A @ -2.5 V 鈥?nbsp;+3.0 V  0.6 A` |
| 646 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.04_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 647 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.04_XPS256_pogo_pin_assignment.md` | `鈼?` | `●` | `C  \| GND  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 648 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.04_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 649 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.04_XPS256_pogo_pin_assignment.md` | `鈼?` | `●` | `C  \| GND  \| NC \|  \|   \| \|  \|   \| Orientation mark 鈼?/strong>  \| \|   \| ` |
| 650 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.04_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 651 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.04_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 652 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.04_XPS256_pogo_pin_assignment.md` | `鈥?` | `…` | `  High-density (HD) pogo block   \|  \|   \| Block A 鈥?P: 16 x 16 channel` |
| 653 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.06.01_XPS256_force_and_clamp_voltages.md` | `鈥?` | `…` | `disconnected)  \| \|  \| XPS256 (EK751HC):  \| -4.5 V 鈥?nbsp;+7.5 V \|  The` |
| 654 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.09_XPS256_load_step_response.md` | `鈥?` | `…` | `with capacitors on the DUT board  \| standard  \| 1 鈥?n  \| 10 kHz \|  \| f` |
| 655 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.09_XPS256_load_step_response.md` | `鈥?` | `…` | `with capacitors on the DUT board  \| standard  \| 1 鈥?n  \| 10 kHz \|  \| f` |
| 656 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 657 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 658 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 659 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 660 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 661 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≤` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 662 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 663 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≤` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 664 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≤` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 665 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01.01_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≤` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 666 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 667 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 668 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 669 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 670 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 671 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 672 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 673 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 674 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 675 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 676 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 677 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 678 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 679 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.01_XPS256_specific_setup_tasks.md` | `鈥?` | `…` | `pability license covers 32 channels: 1 ... 32, 33 鈥?nbsp;64, 鈥?nbsp;, ` |
| 680 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.05_XPS256_programming_-_Default_values.md` | `鈮?` | `≥` | `54611__r_max_Vdrop>) parameters is set to a value 鈮?nbsp;0.5 V.  See a` |
| 681 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.20_XPS256_programming_-_DPS128_and_UHC4_migration_to_XPS256.md` | `鈥?` | `…` | `ation to XPS256  The XPS256 can replace the DPS128鈥? DPS64 and UHC4鈥? ` |
| 682 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.20_XPS256_programming_-_DPS128_and_UHC4_migration_to_XPS256.md` | `鈥?` | `…` | `ation to XPS256  The XPS256 can replace the DPS128鈥? DPS64 and UHC4鈥? ` |
| 683 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.20_XPS256_programming_-_DPS128_and_UHC4_migration_to_XPS256.md` | `鈥?` | `…` | `ation to XPS256  The XPS256 can replace the DPS128鈥? DPS64 and UHC4鈥? ` |
| 684 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.20_XPS256_programming_-_DPS128_and_UHC4_migration_to_XPS256.md` | `鈥?` | `…` | `ation to XPS256  The XPS256 can replace the DPS128鈥? DPS64 and UHC4鈥? ` |
| 685 | `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.20_XPS256_programming_-_DPS128_and_UHC4_migration_to_XPS256.md` | `鈮?` | `≤` | `fnsrc_1>) Total voltage drop on force/ground path 鈮? 0.2.V. ` |
| 686 | `02_System_reference/02.05_Test_Head_Cards/02.05.08.01.02_External_utility_power_supply_-_Configuration_and_DUT_board_design.md` | `鈥?` | `…` | `alue should be in the range of approximately 1 μF 鈥?22μF depending on ` |
| 687 | `02_System_reference/02.06_Command_Reference/02.06.02.02.103_EMAP__-__Error_MAP.md` | `鈮?` | `≤` | `padded to two bytes, even if results_per_cycle is 鈮?4.   \|  \|   \|  PAC` |
| 688 | `02_System_reference/02.06_Command_Reference/02.06.02.02.111_ERCE__-__Expected_and_Received_Cycle_data_of_Events.md` | `鈮?` | `≤` | `he N digit defines the number of the digits ni (1 鈮?i 鈮?N) that specif` |
| 689 | `02_System_reference/02.06_Command_Reference/02.06.02.02.111_ERCE__-__Expected_and_Received_Cycle_data_of_Events.md` | `鈮?` | `≤` | `he N digit defines the number of the digits ni (1 鈮?i 鈮?N) that specif` |
| 690 | `02_System_reference/02.06_Command_Reference/02.06.02.02.115_ERRE__-__Expected_and_Received_Results_of_Events.md` | `鈮?` | `≤` | `he N digit defines the number of the digits ni (1 鈮? i 鈮?N) that speci` |
| 691 | `02_System_reference/02.06_Command_Reference/02.06.02.02.115_ERRE__-__Expected_and_Received_Results_of_Events.md` | `鈮?` | `≤` | `he N digit defines the number of the digits ni (1 鈮? i 鈮?N) that speci` |
| 692 | `02_System_reference/02.06_Command_Reference/02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 693 | `02_System_reference/02.06_Command_Reference/02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 694 | `02_System_reference/02.06_Command_Reference/02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 695 | `02_System_reference/02.06_Command_Reference/02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 696 | `02_System_reference/02.06_Command_Reference/02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 697 | `02_System_reference/02.06_Command_Reference/02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 698 | `02_System_reference/02.06_Command_Reference/02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 699 | `02_System_reference/02.06_Command_Reference/02.06.02.02.152_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 700 | `02_System_reference/02.06_Command_Reference/02.06.02.02.152_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 701 | `02_System_reference/02.06_Command_Reference/02.06.02.02.152_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 702 | `02_System_reference/02.06_Command_Reference/02.06.02.02.152_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 703 | `02_System_reference/02.06_Command_Reference/02.06.02.02.152_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 704 | `02_System_reference/02.06_Command_Reference/02.06.02.02.152_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 705 | `02_System_reference/02.06_Command_Reference/02.06.02.02.153_LBRT__-__LoopBack_RouTing.md` | `鈩?` | `™` | `he specified pins could be configured as SmartLoop鈩?pins, and with whi` |
| 706 | `02_System_reference/02.06_Command_Reference/02.06.02.02.153_LBRT__-__LoopBack_RouTing.md` | `鈩?` | `™` | `he specified pins could be configured as SmartLoop鈩?pins, and with whi` |
| 707 | `02_System_reference/02.06_Command_Reference/02.06.02.02.153_LBRT__-__LoopBack_RouTing.md` | `鈩?` | `™` | `he specified pins could be configured as SmartLoop鈩?pins, and with whi` |
| 708 | `02_System_reference/02.06_Command_Reference/02.06.02.02.177_PDMM__-__PDps_Miscellaneous_Measurement.md` | `鈥?` | `…` | `d.  The valid range of the integer parameter is 1 鈥?128.  The default ` |
| 709 | `02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md` | `鈮?` | `≤` | `voltage   \|  Lowest allowed voltage in V. Must be 鈮?0.   \|  \|  max_vol` |
| 710 | `02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md` | `鈮?` | `≥` | `voltage   \|  Lowest allowed voltage in V. Must be 鈮?0.   \|  \|  max_vol` |
| 711 | `02_System_reference/02.06_Command_Reference/02.06.02.02.235_SQLA__SQLA__-__SeQuencer_Label_Attribute.md` | `鈩?` | `™` | `the_memory_type.md>).  HSER = memory for SmartLoop鈩? initialization pa` |
| 712 | `02_System_reference/02.06_Command_Reference/02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `鈩?` | `™` | `\| \|  LPBK   \|  This instruction starts a SmartLoop鈩?test. param_1 and ` |
| 713 | `02_System_reference/02.06_Command_Reference/02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `鈩?` | `™` | `\| \|  LPBK   \|  This instruction starts a SmartLoop鈩?test. param_1 and ` |
| 714 | `02_System_reference/02.06_Command_Reference/02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `鈩?` | `™` | `\| \|  LPBK   \|  This instruction starts a SmartLoop鈩?test. param_1 and ` |
| 715 | `02_System_reference/02.06_Command_Reference/02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `鈩?` | `™` | `\| \|  LPBK   \|  This instruction starts a SmartLoop鈩?test. param_1 and ` |
| 716 | `02_System_reference/02.06_Command_Reference/02.06.02.02.260_TOCF__TOCF__-__Timing_Level_Offset_search_ConFiguration.md` | `鈮?` | `≤` | `tance between the last two binary search steps is 鈮?resolution.  Units` |
| 717 | `02_System_reference/02.06_Command_Reference/02.06.02.02.286_TTCF__TTCF__-__Transition_Test_ConFiguration.md` | `鈮?` | `≤` | `).  The default is 0. The specified value must be 鈮?256.   \|  \|  DEVIA` |
| 718 | `02_System_reference/02.06_Command_Reference/02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md` | `鈮?` | `≥` | `des.md#_106910__r_return_drop>) is set to a value 鈮?nbsp;0.5 V.  \|  Th` |
| 719 | `02_System_reference/02.06_Command_Reference/02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md` | `鈥?` | `…` | `racteristics.md>).  The programmable range is 0.0 鈥?nbsp;1.0 V for the` |
| 720 | `02_System_reference/02.06_Command_Reference/02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md` | `鈮?` | `≥` | `8518__r_voltageDrop>) parameter is set to a value 鈮?nbsp;0.5 V.  See a` |
| 721 | `02_System_reference/02.06_Command_Reference/02.06.02.02.46_DCRM__DCRM__-__Digital_Compare_Result_Mode.md` | `鈥?` | `…` | `ed into one result. Note that with this option, 8 鈥?nbsp;15 break cycl` |
| 722 | `02_System_reference/02.06_Command_Reference/02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md` | `鈥?` | `…` | `racteristics.md>).  The programmable range is 0.0 鈥?nbsp;1.0 V for the` |
| 723 | `02_System_reference/02.06_Command_Reference/02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md` | `鈮?` | `≥` | `8530__r_voltageDrop>) parameter is set to a value 鈮?nbsp;0.5 V.  See a` |
| 724 | `02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md` | `鈥?` | `‑` | `it (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.  The ` |
| 725 | `02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md` | `鈥?` | `‑` | `it (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.  The ` |
| 726 | `02_System_reference/02.06_Command_Reference/02.06.02.02.86_DPSR__DPSR__-__Define_Parallel_SeaRch.md` | `鈥?` | `…` | `tional test runs in milliseconds.  Valid range: 0 鈥?2^31 - 2  Default ` |
| 727 | `02_System_reference/02.06_Command_Reference/02.06.03.01.05_Defining_a_utility_line.md` | `鈥?` | `…` | `numbers of the utility lines, using the range [01 鈥?nbsp;32] from righ` |
| 728 | `02_System_reference/02.06_Command_Reference/02.06.03.01.05_Defining_a_utility_line.md` | `鈥?` | `…` | `numbers of the utility lines, using the range [01 鈥?nbsp;32] from righ` |
| 729 | `02_System_reference/02.06_Command_Reference/02.06.03.02.11_DFUP__DFUP__-__DeFine_Utility_Purpose.md` | `鈥?` | `‑` | `it (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.  The ` |
| 730 | `02_System_reference/02.06_Command_Reference/02.06.03.02.12_DFUT__DFUT__-__DeFine_UTility_line.md` | `鈥?` | `‑` | `it (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.  The ` |
| 731 | `02_System_reference/02.06_Command_Reference/02.06.03.02.21_PSSL__PSSL___Power_Supply_Safety_Limits.md` | `鈮?` | `≤` | `voltage   \|  Lowest allowed voltage in V. Must be 鈮?0.   \|  \|  max_vol` |
| 732 | `02_System_reference/02.06_Command_Reference/02.06.03.02.21_PSSL__PSSL___Power_Supply_Safety_Limits.md` | `鈮?` | `≥` | `voltage   \|  Lowest allowed voltage in V. Must be 鈮?0.   \|  \|  max_vol` |
| 733 | `02_System_reference/02.06_Command_Reference/02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md` | `鈩?` | `Ω` | `t 0 as well to [control the engagement of the 14 k鈩?pull-down resistor` |
| 734 | `02_System_reference/02.06_Command_Reference/02.06.05.01.05.06_Pull-down_function.md` | `鈩?` | `Ω` | `rcuitry of a PS1600 card offers an internal 14.3 k鈩?pull-down resistor` |
| 735 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 736 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 737 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 738 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 739 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 740 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 741 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈮?` | `≤` | `t of a LOOP_I statement is  LOOP_I [Xi],  where 1 鈮?i 鈮?8.  If no x-mo` |
| 742 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈮?` | `≤` | `t of a LOOP_I statement is  LOOP_I [Xi],  where 1 鈮?i 鈮?8.  If no x-mo` |
| 743 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 744 | `02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 745 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≤` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 746 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≤` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 747 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≥` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 748 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≤` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 749 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≤` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 750 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≥` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 751 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.03_Period_resolution__clock_resolution__and_master_clock_period.md` | `鈮?` | `≤` | `solution/p,  where p is an integer such that 1.76 鈮? clock_resolution ` |
| 752 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.03_Period_resolution__clock_resolution__and_master_clock_period.md` | `鈮?` | `≤` | `solution/p,  where p is an integer such that 1.76 鈮? clock_resolution ` |
| 753 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.04_Period_resolution_for_a_multi-port_setup__Smart_Scale.md` | `鈮?` | `≤` | `lock resolution of the respective system, that is 鈮?3.52 ns on a PS160` |
| 754 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.01_Defining_the_edge_delays_for_Pin_Scale_standard_pins.md` | `鈮?` | `≤` | `lay of a drive pin is  d<n>=<expression>  where 1 鈮?n 鈮?8 and expressi` |
| 755 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.01_Defining_the_edge_delays_for_Pin_Scale_standard_pins.md` | `鈮?` | `≤` | `lay of a drive pin is  d<n>=<expression>  where 1 鈮?n 鈮?8 and expressi` |
| 756 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.01_Defining_the_edge_delays_for_Pin_Scale_standard_pins.md` | `鈮?` | `≤` | `lay of a drive pin is  d<n>=<expression>  where 1 鈮?n 鈮?8 and expressi` |
| 757 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.01_Defining_the_edge_delays_for_Pin_Scale_standard_pins.md` | `鈮?` | `≤` | `lay of a drive pin is  d<n>=<expression>  where 1 鈮?n 鈮?8 and expressi` |
| 758 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.01_Defining_edge_delays_and_period_length_for_a_protocol_engine_test.md` | `鈮?` | `≤` | `lock resolution on the Pin Scale 9G cards is 0.88 鈮?clock_resolution <` |
| 759 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.01_Defining_edge_delays_and_period_length_for_a_protocol_engine_test.md` | `鈮?` | `≤` | `lock resolution on the Pin Scale 9G cards is 0.88 鈮?clock_resolution <` |
| 760 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.03_Defining_edge_delays_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `Loop test  The edges for a pattern‑based SmartLoop鈩?test are distribut` |
| 761 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.03_Defining_edge_delays_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `Loop test  The edges for a pattern‑based SmartLoop鈩?test are distribut` |
| 762 | `02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.03_Defining_edge_delays_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `Loop test  The edges for a pattern‑based SmartLoop鈩?test are distribut` |
| 763 | `02_System_reference/02.06_Command_Reference/02.06.07.01.04.02_Memory_pooling_within_channel_groups.md` | `鈩?` | `™` | `the group channels that are licensed for SmartLoop鈩?  Note that the po` |
| 764 | `02_System_reference/02.06_Command_Reference/02.06.07.01.04.02_Memory_pooling_within_channel_groups.md` | `鈩?` | `™` | `the group channels that are licensed for SmartLoop鈩?  Note that the po` |
| 765 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 766 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 767 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 768 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 769 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 770 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 771 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 772 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 773 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 774 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 775 | `02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.md` | `鈩?` | `™` | `a PRBS (Pseudo Random Bit Sequence) or a SmartLoop鈩?test (for backgrou` |
| 776 | `02_System_reference/02.06_Command_Reference/02.06.07.02.26_SQLA__SQLA__-__SeQuencer_Label_Attribute.md` | `鈩?` | `™` | `the_memory_type.md>).  HSER = memory for SmartLoop鈩? initialization pa` |
| 777 | `02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `鈩?` | `™` | `\| \|  LPBK   \|  This instruction starts a SmartLoop鈩?test. param_1 and ` |
| 778 | `02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `鈩?` | `™` | `\| \|  LPBK   \|  This instruction starts a SmartLoop鈩?test. param_1 and ` |
| 779 | `02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `鈩?` | `™` | `\| \|  LPBK   \|  This instruction starts a SmartLoop鈩?test. param_1 and ` |
| 780 | `02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `鈩?` | `™` | `\| \|  LPBK   \|  This instruction starts a SmartLoop鈩?test. param_1 and ` |
| 781 | `02_System_reference/02.06_Command_Reference/02.06.09.02.02_DPSR__DPSR__-__Define_Parallel_SeaRch.md` | `鈥?` | `…` | `tional test runs in milliseconds.  Valid range: 0 鈥?2^31 - 2  Default ` |
| 782 | `02_System_reference/02.06_Command_Reference/02.06.09.02.17_TOCF__TOCF__-__Timing_Level_Offset_search_ConFiguration.md` | `鈮?` | `≤` | `tance between the last two binary search steps is 鈮?resolution.  Units` |
| 783 | `02_System_reference/02.06_Command_Reference/02.06.10.02.09_PDMM__-__PDps_Miscellaneous_Measurement.md` | `鈥?` | `…` | `d.  The valid range of the integer parameter is 1 鈥?128.  The default ` |
| 784 | `02_System_reference/02.06_Command_Reference/02.06.10.02.16_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md` | `鈮?` | `≥` | `des.md#_106910__r_return_drop>) is set to a value 鈮?nbsp;0.5 V.  \|  Th` |
| 785 | `02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.02.07_Compression_factor_for_overview_Error_Map.md` | `鈥?` | `…` | `is not the case with BFLM.   Note In LMAP mode, 8 鈥?nbsp;15 break vect` |
| 786 | `02_System_reference/02.06_Command_Reference/02.06.11.02.10_DCRM__DCRM__-__Digital_Compare_Result_Mode.md` | `鈥?` | `…` | `ed into one result. Note that with this option, 8 鈥?nbsp;15 break cycl` |
| 787 | `02_System_reference/02.06_Command_Reference/02.06.11.02.18_EMAP__-__Error_MAP.md` | `鈮?` | `≤` | `padded to two bytes, even if results_per_cycle is 鈮?4.   \|  \|   \|  PAC` |
| 788 | `02_System_reference/02.06_Command_Reference/02.06.11.02.23_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 789 | `02_System_reference/02.06_Command_Reference/02.06.11.02.23_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 790 | `02_System_reference/02.06_Command_Reference/02.06.11.02.23_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 791 | `02_System_reference/02.06_Command_Reference/02.06.11.02.23_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 792 | `02_System_reference/02.06_Command_Reference/02.06.11.02.23_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 793 | `02_System_reference/02.06_Command_Reference/02.06.11.02.23_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 794 | `02_System_reference/02.06_Command_Reference/02.06.11.02.23_FFCI__-__First_Failed_Cycle_Information.md` | `鈥?` | `…` | `efined by the first eight address bytes `0000000` 鈥? `00000011`.     -` |
| 795 | `02_System_reference/02.06_Command_Reference/02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md` | `鈥?` | `…` | `answer is to be interpreted as follows:  - Byte 1 鈥?8: Address of the ` |
| 796 | `02_System_reference/02.06_Command_Reference/02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md` | `鈥?` | `…` | `answer is to be interpreted as follows:  - Byte 1 鈥?8: Address of the ` |
| 797 | `02_System_reference/02.06_Command_Reference/02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md` | `鈥?` | `…` | `answer is to be interpreted as follows:  - Byte 1 鈥?8: Address of the ` |
| 798 | `02_System_reference/02.06_Command_Reference/02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md` | `鈥?` | `…` | `answer is to be interpreted as follows:  - Byte 1 鈥?8: Address of the ` |
| 799 | `02_System_reference/02.06_Command_Reference/02.06.12.02.01_DFUP__DFUP__-__DeFine_Utility_Purpose.md` | `鈥?` | `‑` | `it (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.  The ` |
| 800 | `02_System_reference/02.06_Command_Reference/02.06.12.02.02_DFUT__DFUT__-__DeFine_UTility_line.md` | `鈥?` | `‑` | `it (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.  The ` |
| 801 | `02_System_reference/02.06_Command_Reference/02.06.13.01.02_Starting_a_TMU_measurement.md` | `鈩?` | `™` | `mbining a TMU measurement with a PRBS or SmartLoop鈩?test  It is possib` |
| 802 | `02_System_reference/02.06_Command_Reference/02.06.13.01.02_Starting_a_TMU_measurement.md` | `鈩?` | `™` | `mbining a TMU measurement with a PRBS or SmartLoop鈩?test  It is possib` |
| 803 | `02_System_reference/02.06_Command_Reference/02.06.13.01.02_Starting_a_TMU_measurement.md` | `鈩?` | `™` | `mbining a TMU measurement with a PRBS or SmartLoop鈩?test  It is possib` |
| 804 | `02_System_reference/02.06_Command_Reference/02.06.15.01.02.02_Skipping_idle_tokens.md` | `鈮?` | `≤` | `purpose with TTCF (IDLE_TOKEN_i property, where 1 鈮?i 鈮? 6). The numbe` |
| 805 | `02_System_reference/02.06_Command_Reference/02.06.15.01.02.02_Skipping_idle_tokens.md` | `鈮?` | `≤` | `purpose with TTCF (IDLE_TOKEN_i property, where 1 鈮?i 鈮? 6). The numbe` |
| 806 | `02_System_reference/02.06_Command_Reference/02.06.15.02.01_Combining_transition_tracking_with_a_PRBS_or_pattern__ased_SmartLoop_tes.md` | `鈩?` | `™` | ` to combine a PRBS test or pattern‑based SmartLoop鈩?test (see [Command` |
| 807 | `02_System_reference/02.06_Command_Reference/02.06.15.02.01_Combining_transition_tracking_with_a_PRBS_or_pattern__ased_SmartLoop_tes.md` | `鈩?` | `™` | ` to combine a PRBS test or pattern‑based SmartLoop鈩?test (see [Command` |
| 808 | `02_System_reference/02.06_Command_Reference/02.06.15.02.01_Combining_transition_tracking_with_a_PRBS_or_pattern__ased_SmartLoop_tes.md` | `鈩?` | `™` | ` to combine a PRBS test or pattern‑based SmartLoop鈩?test (see [Command` |
| 809 | `02_System_reference/02.06_Command_Reference/02.06.15.03.03_TTCF__TTCF__-__Transition_Test_ConFiguration.md` | `鈮?` | `≤` | `).  The default is 0. The specified value must be 鈮?256.   \|  \|  DEVIA` |
| 810 | `02_System_reference/02.06_Command_Reference/02.06.17.02_Generating_and_checking_pseudo_random_bit_sequences.md` | `鈩?` | `™` | `).  The PRBS per pin is activated by the SmartLoop鈩?license (loopback ` |
| 811 | `02_System_reference/02.06_Command_Reference/02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md` | `鈩?` | `™` | `for pattern‑based SmartLoop testing  The SmartLoop鈩?license also enabl` |
| 812 | `02_System_reference/02.06_Command_Reference/02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md` | `鈩?` | `™` | `for pattern‑based SmartLoop testing  The SmartLoop鈩?license also enabl` |
| 813 | `02_System_reference/02.06_Command_Reference/02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md` | `鈩?` | `™` | `for pattern‑based SmartLoop testing  The SmartLoop鈩?license also enabl` |
| 814 | `02_System_reference/02.06_Command_Reference/02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md` | `鈩?` | `™` | `for pattern‑based SmartLoop testing  The SmartLoop鈩?license also enabl` |
| 815 | `02_System_reference/02.06_Command_Reference/02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md` | `鈩?` | `™` | `for pattern‑based SmartLoop testing  The SmartLoop鈩?license also enabl` |
| 816 | `02_System_reference/02.06_Command_Reference/02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `or_pattern__ased_SmartLoop_testing.md>)  SmartLoop鈩?tests are a specia` |
| 817 | `02_System_reference/02.06_Command_Reference/02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `or_pattern__ased_SmartLoop_testing.md>)  SmartLoop鈩?tests are a specia` |
| 818 | `02_System_reference/02.06_Command_Reference/02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `or_pattern__ased_SmartLoop_testing.md>)  SmartLoop鈩?tests are a specia` |
| 819 | `02_System_reference/02.06_Command_Reference/02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `or_pattern__ased_SmartLoop_testing.md>)  SmartLoop鈩?tests are a specia` |
| 820 | `02_System_reference/02.06_Command_Reference/02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `or_pattern__ased_SmartLoop_testing.md>)  SmartLoop鈩?tests are a specia` |
| 821 | `02_System_reference/02.06_Command_Reference/02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `or_pattern__ased_SmartLoop_testing.md>)  SmartLoop鈩?tests are a specia` |
| 822 | `02_System_reference/02.06_Command_Reference/02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `or_pattern__ased_SmartLoop_testing.md>)  SmartLoop鈩?tests are a specia` |
| 823 | `02_System_reference/02.06_Command_Reference/02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `or_pattern__ased_SmartLoop_testing.md>)  SmartLoop鈩?tests are a specia` |
| 824 | `02_System_reference/02.06_Command_Reference/02.06.17.05.01_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 825 | `02_System_reference/02.06_Command_Reference/02.06.17.05.01_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 826 | `02_System_reference/02.06_Command_Reference/02.06.17.05.01_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 827 | `02_System_reference/02.06_Command_Reference/02.06.17.05.01_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 828 | `02_System_reference/02.06_Command_Reference/02.06.17.05.01_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 829 | `02_System_reference/02.06_Command_Reference/02.06.17.05.01_LBMD__-__LoopBack_MoDe.md` | `鈩?` | `™` | `pBack MoDe)  The LBMD? query returns the SmartLoop鈩?configuration of o` |
| 830 | `02_System_reference/02.06_Command_Reference/02.06.17.05.02_LBRT__-__LoopBack_RouTing.md` | `鈩?` | `™` | `he specified pins could be configured as SmartLoop鈩?pins, and with whi` |
| 831 | `02_System_reference/02.06_Command_Reference/02.06.17.05.02_LBRT__-__LoopBack_RouTing.md` | `鈩?` | `™` | `he specified pins could be configured as SmartLoop鈩?pins, and with whi` |
| 832 | `02_System_reference/02.06_Command_Reference/02.06.17.05.02_LBRT__-__LoopBack_RouTing.md` | `鈩?` | `™` | `he specified pins could be configured as SmartLoop鈩?pins, and with whi` |
| 833 | `02_System_reference/02.07_Test_Method_Reference/02.07.02.03.03_How_to_call_the_functions_in_one_test_method_library_from_another_test_m.md` | `鈥?` | `’` | `bout this task  The default linker option `-rpath=鈥?$ORIGIN鈥?/code> is` |
| 834 | `02_System_reference/02.07_Test_Method_Reference/02.07.03.03.02.03_Changing_and_obtaining_conditions_for_digital_capture_test.md` | `鈥?` | `…` | `ction_#> for ... \|  \| ... changing a condition  \| 鈥?obtaining a condit` |
| 835 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.108_GET_UTILITY_LINES_STATUS.md` | `鈥?` | `…` | `pogo block numbers:  - 0 (All utility blocks) - 1 鈥?nbsp;8 (1st [Utili` |
| 836 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.02_HW_STATE.checkKelvinStatus.md` | `鈥?` | `…` | `d.  The valid range of the integer parameter is 1 鈥?128.  The default ` |
| 837 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.03_HW_STATE.checkKelvinStatusParallel.md` | `鈥?` | `…` | `d.  The valid range of the integer parameter is 1 鈥?128.  The default ` |
| 838 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.04_HW_STATE.checkGangConnection.md` | `鈥?` | `…` | `d.  The valid range of the integer parameter is 1 鈥?128.  The default ` |
| 839 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.05_HW_STATE.checkGangConnectionParallel.md` | `鈥?` | `…` | `d.  The valid range of the integer parameter is 1 鈥?128.  The default ` |
| 840 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.128_LOOPBACK_OPERATION_TASK.md` | `鈩?` | `™` | `b` executes the direct or direct retimed SmartLoop鈩?based loopback tes` |
| 841 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.12_CALC_COHERENCY.md` | `鈮?` | `≥` | `\|  \|  I   \|  `M`   \|  Number of signal periods  M 鈮?1   \|  \|  I   \|  `` |
| 842 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.12_CALC_COHERENCY.md` | `鈮?` | `≥` | `\|  \|  I   \|  `M`   \|  Number of signal periods  M 鈮?1   \|  \|  I   \|  `` |
| 843 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.190.01.03_RESULT_AREA_CONFIG_PINS.setResultRetentionEnabled.md` | `鈥?` | `’` | `d using this member function and specifying ‘false鈥?as the parameter v` |
| 844 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.190.01.07_RESULT_AREA_CONFIG_PINS.isResultRetentionEnabled.md` | `鈥?` | `’` | `d using this member function and specifying ‘false鈥?as the parameter v` |
| 845 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.199.01_SEARCH_FUNC_PIN_TASK.md` | `鈥?` | `…` | ` functional test runs in seconds.  Valid range: 0 鈥?(2^31 - 2) ms  Def` |
| 846 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27_SMC_PIN_ERROR_MAP.md` | `鈥?` | `…` | `ped to result 1. - Recording mode X2:    - Edge 1 鈥?4 are mapped to re` |
| 847 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27_SMC_PIN_ERROR_MAP.md` | `鈥?` | `…` | `ped to result 1. - Recording mode X2:    - Edge 1 鈥?4 are mapped to re` |
| 848 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.09_SPMU_PIN_TASK.forceDropMax.md` | `鈥?` | `…` | `racteristics.md>).  The programmable range is 0.0 鈥?nbsp;1.0 V for the` |
| 849 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.md` | `鈮?` | `≤` | `ned as working with some bypass capacitor network 鈮?nbsp;10 nF.    - T` |
| 850 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.md` | `鈮?` | `≥` | `ned as working with some bypass capacitor network 鈮?nbsp;10 nF.    - T` |
| 851 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.25_SPMU_PIN_TASK.openLoopProtection.md` | `鈮?` | `≥` | `PMU_PIN_TASK.returnDropMax.md>) is set to a value 鈮?nbsp;0.5 V.  See a` |
| 852 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.29_SPMU_PIN_TASK.returnDropMax.md` | `鈥?` | `…` | `racteristics.md>).  The programmable range is 0.0 鈥?nbsp;1.0 V for the` |
| 853 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.257.01_TRANSITION_TEST_PINS.md` | `鈮?` | `≤` | `e default value is 0. The specified value must be 鈮?256.   \|  ### devi` |
| 854 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.257.01_TRANSITION_TEST_PINS.md` | `鈮?` | `≤` | `e default value is 0. The specified value must be 鈮?256.   \|  ### devi` |
| 855 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.257.01_TRANSITION_TEST_PINS.md` | `鈮?` | `≤` | `e default value is 0. The specified value must be 鈮?256.   \|  ### devi` |
| 856 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.265.02_UTILITY_SEQ_MODE.pogoBlock.md` | `鈥?` | `…` | `pogo block numbers:  - 0 (All utility blocks) - 1 鈥?nbsp;8 (1st [Utili` |
| 857 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.266.02_UTILITY_SEQ_STATIC_MASK.pogoBlock.md` | `鈥?` | `…` | `pogo block numbers:  - 0 (All utility blocks) - 1 鈥?nbsp;8 (1st [Utili` |
| 858 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.270_VEC_TRANSFER_TASK.md` | `鈮?` | `≥` | `y_file_for_a_device.md>).   Note  -  For SmarTest 鈮?7.4.3.0:  fast_tra` |
| 859 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.270_VEC_TRANSFER_TASK.md` | `鈮?` | `≤` | `y_file_for_a_device.md>).   Note  -  For SmarTest 鈮?7.4.3.0:  fast_tra` |
| 860 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.273_Wave.md` | `鈮?` | `≠` | `e above figure, t × periods = Dt × size.  periods 鈮?1.  In relation to` |
| 861 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.273_Wave.md` | `鈮?` | `≤` | `e above figure, t × periods = Dt × size.  periods 鈮?1.  In relation to` |
| 862 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.273_Wave.md` | `鈮?` | `≤` | `e above figure, t × periods = Dt × size.  periods 鈮?1.  In relation to` |
| 863 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.273_Wave.md` | `鈮?` | `≤` | `e above figure, t × periods = Dt × size.  periods 鈮?1.  In relation to` |
| 864 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.273_Wave.md` | `鈮?` | `≤` | `e above figure, t × periods = Dt × size.  periods 鈮?1.  In relation to` |
| 865 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.273_Wave.md` | `鈮?` | `≤` | `e above figure, t × periods = Dt × size.  periods 鈮?1.  In relation to` |
| 866 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.52_DRAM_ADDRESS_MAPPER.md` | `鈮?` | `≤` | ` binary format).  Note that not all row addresses 鈮?8191 may be valid.` |
| 867 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.01_DSP_ABS_MINMAX.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 868 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.01_DSP_ABS_MINMAX.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 869 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.01_DSP_ABS_MINMAX.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 870 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.02_DSP_ABS_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 871 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.02_DSP_ABS_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 872 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.02_DSP_ABS_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 873 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.02_DSP_ABS_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 874 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.03_DSP_ADC_HISTOGRAM.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152 (il` |
| 875 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.03_DSP_ADC_HISTOGRAM.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152 (il` |
| 876 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.03_DSP_ADC_HISTOGRAM.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152 (il` |
| 877 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.03_DSP_ADC_HISTOGRAM.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152 (il` |
| 878 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.03_DSP_ADC_HISTOGRAM.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152 (il` |
| 879 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.03_DSP_ADC_HISTOGRAM.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152 (il` |
| 880 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.03_DSP_ADC_HISTOGRAM.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152 (il` |
| 881 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.06_DSP_ADD_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 882 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.06_DSP_ADD_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 883 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.06_DSP_ADD_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 884 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.06_DSP_ADD_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 885 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.07_DSP_ADD_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 886 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.07_DSP_ADD_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 887 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.07_DSP_ADD_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 888 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.07_DSP_ADD_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 889 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.07_DSP_ADD_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 890 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.08_DSP_A_DECODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 891 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.08_DSP_A_DECODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 892 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.08_DSP_A_DECODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 893 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.09_DSP_A_ENCODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 894 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.09_DSP_A_ENCODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 895 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.09_DSP_A_ENCODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 896 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.101_DSP_SUB_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 897 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.101_DSP_SUB_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 898 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.101_DSP_SUB_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 899 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.101_DSP_SUB_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 900 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.102_DSP_SUB_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 901 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.102_DSP_SUB_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 902 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.102_DSP_SUB_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 903 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.102_DSP_SUB_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 904 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.102_DSP_SUB_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 905 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.103_DSP_SUM.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?size 鈮?2097152   \|` |
| 906 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.103_DSP_SUM.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?size 鈮?2097152   \|` |
| 907 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.103_DSP_SUM.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?size 鈮?2097152   \|` |
| 908 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.103_DSP_SUM.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?size 鈮?2097152   \|` |
| 909 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.104_DSP_TAN_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 910 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.104_DSP_TAN_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 911 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.104_DSP_TAN_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 912 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.104_DSP_TAN_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 913 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.105_DSP_THD.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  Then, for `1`鈮? j 鈮?size/2 - 1, C` |
| 914 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.105_DSP_THD.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  Then, for `1`鈮? j 鈮?size/2 - 1, C` |
| 915 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.105_DSP_THD.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  Then, for `1`鈮? j 鈮?size/2 - 1, C` |
| 916 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.105_DSP_THD.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  Then, for `1`鈮? j 鈮?size/2 - 1, C` |
| 917 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.105_DSP_THD.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  Then, for `1`鈮? j 鈮?size/2 - 1, C` |
| 918 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.105_DSP_THD.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  Then, for `1`鈮? j 鈮?size/2 - 1, C` |
| 919 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.105_DSP_THD.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  Then, for `1`鈮? j 鈮?size/2 - 1, C` |
| 920 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.106_DSP_TH_QUANTIZE.md` | `鈮?` | `≥` | `9271.png>)  The number of result elements must be 鈮? size + 1.  This A` |
| 921 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.106_DSP_TH_QUANTIZE.md` | `鈮?` | `≤` | `9271.png>)  The number of result elements must be 鈮? size + 1.  This A` |
| 922 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.106_DSP_TH_QUANTIZE.md` | `鈮?` | `≤` | `9271.png>)  The number of result elements must be 鈮? size + 1.  This A` |
| 923 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.106_DSP_TH_QUANTIZE.md` | `鈮?` | `≤` | `9271.png>)  The number of result elements must be 鈮? size + 1.  This A` |
| 924 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.106_DSP_TH_QUANTIZE.md` | `鈮?` | `≤` | `9271.png>)  The number of result elements must be 鈮? size + 1.  This A` |
| 925 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.107_DSP_TRANS_MAT.md` | `鈮?` | `≤` | `I   \|  row   \|  Row dimension of source matrix  1 鈮?row   \|  \|  I   \| ` |
| 926 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.107_DSP_TRANS_MAT.md` | `鈮?` | `≤` | `I   \|  row   \|  Row dimension of source matrix  1 鈮?row   \|  \|  I   \| ` |
| 927 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.107_DSP_TRANS_MAT.md` | `鈮?` | `≤` | `I   \|  row   \|  Row dimension of source matrix  1 鈮?row   \|  \|  I   \| ` |
| 928 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.107_DSP_TRANS_MAT.md` | `鈮?` | `≤` | `I   \|  row   \|  Row dimension of source matrix  1 鈮?row   \|  \|  I   \| ` |
| 929 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.108_DSP_UNIT_MAT.md` | `鈮?` | `≠` | `j]  = 1, when i = j or result [i][j]  = 0, when i 鈮?j ```  This API is` |
| 930 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.108_DSP_UNIT_MAT.md` | `鈮?` | `≤` | `j]  = 1, when i = j or result [i][j]  = 0, when i 鈮?j ```  This API is` |
| 931 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.108_DSP_UNIT_MAT.md` | `鈮?` | `≤` | `j]  = 1, when i = j or result [i][j]  = 0, when i 鈮?j ```  This API is` |
| 932 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.109_DSP_XOR_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 933 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.109_DSP_XOR_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 934 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.109_DSP_XOR_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 935 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.109_DSP_XOR_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 936 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.10_DSP_AND_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 937 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.10_DSP_AND_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 938 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.10_DSP_AND_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 939 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.10_DSP_AND_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 940 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.110_DSP_XOR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 941 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.110_DSP_XOR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 942 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.110_DSP_XOR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 943 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.110_DSP_XOR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 944 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.110_DSP_XOR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 945 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.11_DSP_AND_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 946 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.11_DSP_AND_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 947 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.11_DSP_AND_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 948 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.11_DSP_AND_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 949 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.11_DSP_AND_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 950 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.12_DSP_AREA.md` | `鈮?` | `≤` | `art   \|  Subscript at which the process starts  0 鈮?start 鈮?2097152 - ` |
| 951 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.12_DSP_AREA.md` | `鈮?` | `≤` | `art   \|  Subscript at which the process starts  0 鈮?start 鈮?2097152 - ` |
| 952 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.12_DSP_AREA.md` | `鈮?` | `≤` | `art   \|  Subscript at which the process starts  0 鈮?start 鈮?2097152 - ` |
| 953 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.12_DSP_AREA.md` | `鈮?` | `≤` | `art   \|  Subscript at which the process starts  0 鈮?start 鈮?2097152 - ` |
| 954 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.12_DSP_AREA.md` | `鈮?` | `≤` | `art   \|  Subscript at which the process starts  0 鈮?start 鈮?2097152 - ` |
| 955 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.12_DSP_AREA.md` | `鈮?` | `≤` | `art   \|  Subscript at which the process starts  0 鈮?start 鈮?2097152 - ` |
| 956 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.12_DSP_AREA.md` | `鈮?` | `≥` | `art   \|  Subscript at which the process starts  0 鈮?start 鈮?2097152 - ` |
| 957 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.13_DSP_ASSIGN_FILTER.md` | `鈮?` | `≤` | `\|  Number of elements to be returned to result  4 鈮?size 鈮?2097152  si` |
| 958 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.13_DSP_ASSIGN_FILTER.md` | `鈮?` | `≤` | `\|  Number of elements to be returned to result  4 鈮?size 鈮?2097152  si` |
| 959 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.13_DSP_ASSIGN_FILTER.md` | `鈮?` | `≤` | `\|  Number of elements to be returned to result  4 鈮?size 鈮?2097152  si` |
| 960 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.14_DSP_BLOCK_FFT.md` | `鈮?` | `≤` | ``   \|  Computed results  block_num × fft_size / 2 鈮?(size of result ar` |
| 961 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.14_DSP_BLOCK_FFT.md` | `鈮?` | `≤` | ``   \|  Computed results  block_num × fft_size / 2 鈮?(size of result ar` |
| 962 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.14_DSP_BLOCK_FFT.md` | `鈮?` | `≤` | ``   \|  Computed results  block_num × fft_size / 2 鈮?(size of result ar` |
| 963 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.14_DSP_BLOCK_FFT.md` | `鈮?` | `≤` | ``   \|  Computed results  block_num × fft_size / 2 鈮?(size of result ar` |
| 964 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.14_DSP_BLOCK_FFT.md` | `鈮?` | `≤` | ``   \|  Computed results  block_num × fft_size / 2 鈮?(size of result ar` |
| 965 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 966 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 967 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 968 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 969 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 970 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 971 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 972 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 973 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 974 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 975 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 976 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 977 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 978 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 979 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 980 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 981 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 982 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 983 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 984 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 985 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.15_DSP_COMBINE_BIT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 986 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.16_DSP_COMPRESS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size × slot 鈮?2097` |
| 987 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.16_DSP_COMPRESS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size × slot 鈮?2097` |
| 988 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.16_DSP_COMPRESS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size × slot 鈮?2097` |
| 989 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.16_DSP_COMPRESS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size × slot 鈮?2097` |
| 990 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.16_DSP_COMPRESS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size × slot 鈮?2097` |
| 991 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.16_DSP_COMPRESS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size × slot 鈮?2097` |
| 992 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.16_DSP_COMPRESS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size × slot 鈮?2097` |
| 993 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.17_DSP_CONCAT.md` | `鈮?` | `≤` | `\|  Computed result array  (src1_size + src2_size) 鈮?result_size < 2097` |
| 994 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.17_DSP_CONCAT.md` | `鈮?` | `≤` | `\|  Computed result array  (src1_size + src2_size) 鈮?result_size < 2097` |
| 995 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.17_DSP_CONCAT.md` | `鈮?` | `≤` | `\|  Computed result array  (src1_size + src2_size) 鈮?result_size < 2097` |
| 996 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.17_DSP_CONCAT.md` | `鈮?` | `≤` | `\|  Computed result array  (src1_size + src2_size) 鈮?result_size < 2097` |
| 997 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.18_DSP_CONV_D_x.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 998 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.18_DSP_CONV_D_x.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 999 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.18_DSP_CONV_D_x.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1000 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.18_DSP_CONV_D_x.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1001 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.19_DSP_CONV_I_x.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1002 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.19_DSP_CONV_I_x.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1003 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.19_DSP_CONV_I_x.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1004 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.19_DSP_CONV_I_x.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1005 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.20_DSP_CONVOL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1006 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.20_DSP_CONVOL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1007 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.20_DSP_CONVOL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1008 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.20_DSP_CONVOL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1009 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.20_DSP_CONVOL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1010 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.21_DSP_CORREL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1011 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.21_DSP_CORREL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1012 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.21_DSP_CORREL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1013 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.21_DSP_CORREL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1014 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.21_DSP_CORREL.md` | `鈮?` | `≤` | `mber of elements in src1 array to be processed  1 鈮?size1 鈮?2097152  s` |
| 1015 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.22_DSP_COS_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1016 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.22_DSP_COS_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1017 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.22_DSP_COS_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1018 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.22_DSP_COS_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1019 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1020 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1021 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1022 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1023 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1024 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1025 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1026 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1027 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1028 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1029 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1030 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1031 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1032 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1033 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1034 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1035 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1036 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.23_DSP_DFT.md` | `鈮?` | `≤` | `a](<../../../../raw/30628.png>)  where   `g(k): 0`鈮?k 鈮?N - 1   G(n): ` |
| 1037 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1038 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1039 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1040 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1041 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1042 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1043 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1044 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1045 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1046 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.24_DSP_DGDP.md` | `鈮?` | `≤` | ` Subscript at which the first block is started  1 鈮?start_point 鈮?size` |
| 1047 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.25_DSP_DIFF.md` | `鈮?` | `≤` | `y   \|  \|  O   \|  result   \|  Difference  size - 1 鈮?size of result   \|` |
| 1048 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.25_DSP_DIFF.md` | `鈮?` | `≤` | `y   \|  \|  O   \|  result   \|  Difference  size - 1 鈮?size of result   \|` |
| 1049 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.25_DSP_DIFF.md` | `鈮?` | `≤` | `y   \|  \|  O   \|  result   \|  Difference  size - 1 鈮?size of result   \|` |
| 1050 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.25_DSP_DIFF.md` | `鈮?` | `≤` | `y   \|  \|  O   \|  result   \|  Difference  size - 1 鈮?size of result   \|` |
| 1051 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.27_DSP_DIV_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1052 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.27_DSP_DIV_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1053 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.27_DSP_DIV_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1054 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.27_DSP_DIV_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1055 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.28_DSP_DIV_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1056 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.28_DSP_DIV_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1057 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.28_DSP_DIV_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1058 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.28_DSP_DIV_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1059 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.28_DSP_DIV_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1060 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.29_DSP_EDGE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1061 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.29_DSP_EDGE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1062 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.29_DSP_EDGE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1063 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.29_DSP_EDGE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1064 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.29_DSP_EDGE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1065 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.29_DSP_EDGE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1066 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.30_DSP_EXP10_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1067 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.30_DSP_EXP10_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1068 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.30_DSP_EXP10_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1069 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.30_DSP_EXP10_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1070 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.31_DSP_EXPAND.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152   \|` |
| 1071 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.31_DSP_EXPAND.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152   \|` |
| 1072 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.31_DSP_EXPAND.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152   \|` |
| 1073 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.32_DSP_EXP_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1074 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.32_DSP_EXP_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1075 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.32_DSP_EXP_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1076 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.32_DSP_EXP_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1077 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.33_DSP_EXTRACT.md` | `鈮?` | `≤` | `  Start point of source array  s_start + size - 1 鈮?size of source arr` |
| 1078 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.33_DSP_EXTRACT.md` | `鈮?` | `≤` | `  Start point of source array  s_start + size - 1 鈮?size of source arr` |
| 1079 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.33_DSP_EXTRACT.md` | `鈮?` | `≤` | `  Start point of source array  s_start + size - 1 鈮?size of source arr` |
| 1080 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.33_DSP_EXTRACT.md` | `鈮?` | `≤` | `  Start point of source array  s_start + size - 1 鈮?size of source arr` |
| 1081 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1082 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1083 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1084 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1085 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1086 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1087 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1088 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1089 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1090 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1091 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1092 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.34_DSP_FFT.md` | `鈮?` | `≤` | ``size`   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  Si` |
| 1093 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.35_DSP_FILL_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1094 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.35_DSP_FILL_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1095 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.35_DSP_FILL_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1096 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1097 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1098 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1099 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1100 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1101 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1102 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1103 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1104 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1105 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.36_DSP_FIR_FILTER1.md` | `鈮?` | `≤` | ` magnitude response of the FIR filter in dB.  256 鈮?size 鈮?524288  The` |
| 1106 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1107 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1108 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1109 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1110 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1111 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1112 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1113 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1114 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1115 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1116 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1117 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1118 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1119 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1120 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.37_DSP_HISTOGRAM.md` | `鈮?` | `≤` | `----   1st element : SE < MIN   2nd element : MIN 鈮?SE < MIN + BW   . ` |
| 1121 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.38_DSP_IFFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  si` |
| 1122 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.38_DSP_IFFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  si` |
| 1123 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.38_DSP_IFFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  si` |
| 1124 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.38_DSP_IFFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  si` |
| 1125 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.38_DSP_IFFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  si` |
| 1126 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.38_DSP_IFFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  si` |
| 1127 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.38_DSP_IFFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  8 鈮?size 鈮?2097152  si` |
| 1128 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.39_DSP_IFFT_POLAR.md` | `鈮?` | `≤` | `n which to store real part data  (size of result) 鈮?2 × (size of ampli` |
| 1129 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.39_DSP_IFFT_POLAR.md` | `鈮?` | `≤` | `n which to store real part data  (size of result) 鈮?2 × (size of ampli` |
| 1130 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.43_DSP_LINEAR.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1131 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.43_DSP_LINEAR.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1132 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.43_DSP_LINEAR.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1133 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.43_DSP_LINEAR.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1134 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.43_DSP_LINEAR.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1135 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.44_DSP_LOG10_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1136 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.44_DSP_LOG10_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1137 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.44_DSP_LOG10_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1138 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.44_DSP_LOG10_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1139 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.45_DSP_LOG_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1140 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.45_DSP_LOG_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1141 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.45_DSP_LOG_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1142 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.45_DSP_LOG_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1143 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.46_DSP_MEAN.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1144 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.46_DSP_MEAN.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1145 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.46_DSP_MEAN.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1146 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.47_DSP_MINMAX.md` | `鈮?` | `≤` | ````   \|  ``` Number of elements to be processed 2 鈮?em>size鈮?2097152 s` |
| 1147 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.47_DSP_MINMAX.md` | `鈮?` | `≤` | ````   \|  ``` Number of elements to be processed 2 鈮?em>size鈮?2097152 s` |
| 1148 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.48_DSP_MEDIAN.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?`size`鈮?2097152   ` |
| 1149 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.48_DSP_MEDIAN.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?`size`鈮?2097152   ` |
| 1150 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.48_DSP_MEDIAN.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?`size`鈮?2097152   ` |
| 1151 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.48_DSP_MEDIAN.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?`size`鈮?2097152   ` |
| 1152 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.49_DSP_MOVAVG.md` | `鈮?` | `≤` | ` ![formula](<../../../../raw/30642.png>)  where 0 鈮?i 鈮?size - length.` |
| 1153 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.49_DSP_MOVAVG.md` | `鈮?` | `≤` | ` ![formula](<../../../../raw/30642.png>)  where 0 鈮?i 鈮?size - length.` |
| 1154 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.49_DSP_MOVAVG.md` | `鈮?` | `≤` | ` ![formula](<../../../../raw/30642.png>)  where 0 鈮?i 鈮?size - length.` |
| 1155 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.49_DSP_MOVAVG.md` | `鈮?` | `≤` | ` ![formula](<../../../../raw/30642.png>)  where 0 鈮?i 鈮?size - length.` |
| 1156 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.49_DSP_MOVAVG.md` | `鈮?` | `≤` | ` ![formula](<../../../../raw/30642.png>)  where 0 鈮?i 鈮?size - length.` |
| 1157 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.49_DSP_MOVAVG.md` | `鈮?` | `≤` | ` ![formula](<../../../../raw/30642.png>)  where 0 鈮?i 鈮?size - length.` |
| 1158 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.49_DSP_MOVAVG.md` | `鈮?` | `≤` | ` ![formula](<../../../../raw/30642.png>)  where 0 鈮?i 鈮?size - length.` |
| 1159 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.49_DSP_MOVAVG.md` | `鈮?` | `≤` | ` ![formula](<../../../../raw/30642.png>)  where 0 鈮?i 鈮?size - length.` |
| 1160 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.51_DSP_MU_DECODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1161 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.51_DSP_MU_DECODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1162 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.51_DSP_MU_DECODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1163 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.52_DSP_MU_ENCODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1164 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.52_DSP_MU_ENCODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1165 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.52_DSP_MU_ENCODE.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1166 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.53_DSP_MUL_MAT.md` | `鈮?` | `≤` | ` row   \|  Row dimension of multiplicand matrix  1 鈮?row   \|  \|  I   \| ` |
| 1167 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.53_DSP_MUL_MAT.md` | `鈮?` | `≤` | ` row   \|  Row dimension of multiplicand matrix  1 鈮?row   \|  \|  I   \| ` |
| 1168 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.53_DSP_MUL_MAT.md` | `鈮?` | `≤` | ` row   \|  Row dimension of multiplicand matrix  1 鈮?row   \|  \|  I   \| ` |
| 1169 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.53_DSP_MUL_MAT.md` | `鈮?` | `≤` | ` row   \|  Row dimension of multiplicand matrix  1 鈮?row   \|  \|  I   \| ` |
| 1170 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.53_DSP_MUL_MAT.md` | `鈮?` | `≤` | ` row   \|  Row dimension of multiplicand matrix  1 鈮?row   \|  \|  I   \| ` |
| 1171 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.53_DSP_MUL_MAT.md` | `鈮?` | `≤` | ` row   \|  Row dimension of multiplicand matrix  1 鈮?row   \|  \|  I   \| ` |
| 1172 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.54_DSP_MUL_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1173 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.54_DSP_MUL_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1174 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.54_DSP_MUL_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1175 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.54_DSP_MUL_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1176 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.55_DSP_MUL_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1177 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.55_DSP_MUL_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1178 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.55_DSP_MUL_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1179 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.55_DSP_MUL_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1180 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.55_DSP_MUL_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1181 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.56_DSP_OR_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1182 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.56_DSP_OR_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1183 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.56_DSP_OR_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1184 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.56_DSP_OR_SCL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1185 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.57_DSP_OR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1186 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.57_DSP_OR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1187 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.57_DSP_OR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1188 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.57_DSP_OR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1189 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.57_DSP_OR_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1190 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.58_DSP_PARA_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1191 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.58_DSP_PARA_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1192 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.58_DSP_PARA_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1193 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.58_DSP_PARA_SERI.md` | `鈭?` | `∞` | `d  1 鈮?size 鈮?2097152  size 鈮?(size of src)  size 鈭?slot 鈮?(size of re` |
| 1194 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.58_DSP_PARA_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1195 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.58_DSP_PARA_SERI.md` | `鈮?` | `≥` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1196 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.58_DSP_PARA_SERI.md` | `鈮?` | `≥` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1197 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.59_DSP_POL_RECT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1198 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.59_DSP_POL_RECT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1199 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.59_DSP_POL_RECT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1200 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.59_DSP_POL_RECT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1201 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.59_DSP_POL_RECT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1202 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.60_DSP_POWER_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1203 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.60_DSP_POWER_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1204 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.60_DSP_POWER_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1205 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.60_DSP_POWER_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1206 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.61_DSP_RECT_POL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1207 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.61_DSP_RECT_POL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1208 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.61_DSP_RECT_POL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1209 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.61_DSP_RECT_POL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1210 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.61_DSP_RECT_POL.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1211 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.62_DSP_REG1.md` | `鈮?` | `≤` | `  \|  Start point of regression in source array  0 鈮?start   \|  \|  I   ` |
| 1212 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.62_DSP_REG1.md` | `鈮?` | `≤` | `  \|  Start point of regression in source array  0 鈮?start   \|  \|  I   ` |
| 1213 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.62_DSP_REG1.md` | `鈮?` | `≤` | `  \|  Start point of regression in source array  0 鈮?start   \|  \|  I   ` |
| 1214 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.62_DSP_REG1.md` | `鈮?` | `≤` | `  \|  Start point of regression in source array  0 鈮?start   \|  \|  I   ` |
| 1215 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.63_DSP_REG2.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1216 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.63_DSP_REG2.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1217 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.63_DSP_REG2.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1218 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.63_DSP_REG2.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1219 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1220 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1221 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1222 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1223 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1224 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1225 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1226 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1227 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1228 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1229 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1230 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1231 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1232 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.65_DSP_RESPONSE.md` | `鈮?` | `≤` | `./../raw/30649.png>)  where   \|  input[k]:   \|  0 鈮?k 鈮?N - 1   \|  \|  ` |
| 1233 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.85_DSP_RMS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1234 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.85_DSP_RMS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1235 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.85_DSP_RMS.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  2 鈮?size 鈮?2097152  si` |
| 1236 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.86_DSP_SEARCH_PARA.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?(size of sr` |
| 1237 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.86_DSP_SEARCH_PARA.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?(size of sr` |
| 1238 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.86_DSP_SEARCH_PARA.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?(size of sr` |
| 1239 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.86_DSP_SEARCH_PARA.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?(size of sr` |
| 1240 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.86_DSP_SEARCH_PARA.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?(size of sr` |
| 1241 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.86_DSP_SEARCH_PARA.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?(size of sr` |
| 1242 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.86_DSP_SEARCH_PARA.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?(size of sr` |
| 1243 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.86_DSP_SEARCH_PARA.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?(size of sr` |
| 1244 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.87_DSP_SEARCH_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1245 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.87_DSP_SEARCH_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1246 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.87_DSP_SEARCH_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1247 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.87_DSP_SEARCH_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1248 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.87_DSP_SEARCH_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1249 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.87_DSP_SEARCH_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1250 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.87_DSP_SEARCH_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1251 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.87_DSP_SEARCH_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1252 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.87_DSP_SEARCH_SERI.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1253 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.88_DSP_SERI_PARA.md` | `鈮?` | `≤` | `O   \|  result   \|  Result array  (size of result) 鈮? size/slot   \|  \| ` |
| 1254 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.88_DSP_SERI_PARA.md` | `鈮?` | `≤` | `O   \|  result   \|  Result array  (size of result) 鈮? size/slot   \|  \| ` |
| 1255 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.88_DSP_SERI_PARA.md` | `鈮?` | `≤` | `O   \|  result   \|  Result array  (size of result) 鈮? size/slot   \|  \| ` |
| 1256 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.88_DSP_SERI_PARA.md` | `鈮?` | `≥` | `O   \|  result   \|  Result array  (size of result) 鈮? size/slot   \|  \| ` |
| 1257 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.88_DSP_SERI_PARA.md` | `鈮?` | `≤` | `O   \|  result   \|  Result array  (size of result) 鈮? size/slot   \|  \| ` |
| 1258 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.88_DSP_SERI_PARA.md` | `鈮?` | `≤` | `O   \|  result   \|  Result array  (size of result) 鈮? size/slot   \|  \| ` |
| 1259 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.89_DSP_SETTLING.md` | `鈮?` | `≤` | `esult will be in the following range:  0 < result 鈮?1.0  If all the sr` |
| 1260 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.89_DSP_SETTLING.md` | `鈮?` | `≤` | `esult will be in the following range:  0 < result 鈮?1.0  If all the sr` |
| 1261 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.89_DSP_SETTLING.md` | `鈮?` | `≤` | `esult will be in the following range:  0 < result 鈮?1.0  If all the sr` |
| 1262 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.89_DSP_SETTLING.md` | `鈮?` | `≤` | `esult will be in the following range:  0 < result 鈮?1.0  If all the sr` |
| 1263 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.89_DSP_SETTLING.md` | `鈮?` | `≤` | `esult will be in the following range:  0 < result 鈮?1.0  If all the sr` |
| 1264 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1265 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1266 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1267 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1268 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1269 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1270 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1271 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1272 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1273 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1274 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.90_DSP_SFDR.md` | `鈮?` | `≤` | `s number must be a power of two: 8, 16, 32, ... 8 鈮?size 鈮?2097152 siz` |
| 1275 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.91_DSP_SHIFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152   \|` |
| 1276 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.91_DSP_SHIFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152   \|` |
| 1277 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.91_DSP_SHIFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152   \|` |
| 1278 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.91_DSP_SHIFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152   \|` |
| 1279 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.91_DSP_SHIFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152   \|` |
| 1280 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.91_DSP_SHIFT.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152   \|` |
| 1281 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.92_DSP_SHUFFLE.md` | `鈮?` | `≠` | `above figure, t × rel_freq = Dt × size.  rel_freq 鈮?1.  size and rel_f` |
| 1282 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.92_DSP_SHUFFLE.md` | `鈮?` | `≤` | `above figure, t × rel_freq = Dt × size.  rel_freq 鈮?1.  size and rel_f` |
| 1283 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.92_DSP_SHUFFLE.md` | `鈮?` | `≤` | `above figure, t × rel_freq = Dt × size.  rel_freq 鈮?1.  size and rel_f` |
| 1284 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.92_DSP_SHUFFLE.md` | `鈮?` | `≤` | `above figure, t × rel_freq = Dt × size.  rel_freq 鈮?1.  size and rel_f` |
| 1285 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.93_DSP_SINFIT.md` | `鈮?` | `≤` | `result   \|  Elements of the ideal sine wave  size 鈮?size of result   \|` |
| 1286 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.93_DSP_SINFIT.md` | `鈮?` | `≤` | `result   \|  Elements of the ideal sine wave  size 鈮?size of result   \|` |
| 1287 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.93_DSP_SINFIT.md` | `鈮?` | `≤` | `result   \|  Elements of the ideal sine wave  size 鈮?size of result   \|` |
| 1288 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.93_DSP_SINFIT.md` | `鈮?` | `≤` | `result   \|  Elements of the ideal sine wave  size 鈮?size of result   \|` |
| 1289 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.94_DSP_SIN_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1290 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.94_DSP_SIN_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1291 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.94_DSP_SIN_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1292 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.94_DSP_SIN_VEC.md` | `鈮?` | `≤` | `  size   \|  Number of elements to be processed  1 鈮?size 鈮?2097152  si` |
| 1293 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.95_DSP_SND.md` | `鈮?` | `≤` | `` DSP_FFT( src, c, size, RECT); ```  Then, for `1`鈮?j 鈮?size/2 - 1, CO` |
| 1294 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.95_DSP_SND.md` | `鈮?` | `≤` | `` DSP_FFT( src, c, size, RECT); ```  Then, for `1`鈮?j 鈮?size/2 - 1, CO` |
| 1295 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.95_DSP_SND.md` | `鈮?` | `≤` | `` DSP_FFT( src, c, size, RECT); ```  Then, for `1`鈮?j 鈮?size/2 - 1, CO` |
| 1296 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.95_DSP_SND.md` | `鈮?` | `≤` | `` DSP_FFT( src, c, size, RECT); ```  Then, for `1`鈮?j 鈮?size/2 - 1, CO` |
| 1297 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.95_DSP_SND.md` | `鈮?` | `≤` | `` DSP_FFT( src, c, size, RECT); ```  Then, for `1`鈮?j 鈮?size/2 - 1, CO` |
| 1298 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.95_DSP_SND.md` | `鈮?` | `≤` | `` DSP_FFT( src, c, size, RECT); ```  Then, for `1`鈮?j 鈮?size/2 - 1, CO` |
| 1299 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.95_DSP_SND.md` | `鈮?` | `≤` | `` DSP_FFT( src, c, size, RECT); ```  Then, for `1`鈮?j 鈮?size/2 - 1, CO` |
| 1300 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.95_DSP_SND.md` | `鈮?` | `≤` | `` DSP_FFT( src, c, size, RECT); ```  Then, for `1`鈮?j 鈮?size/2 - 1, CO` |
| 1301 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.95_DSP_SND.md` | `鈮?` | `≤` | `` DSP_FFT( src, c, size, RECT); ```  Then, for `1`鈮?j 鈮?size/2 - 1, CO` |
| 1302 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.96_DSP_SNR.md` | `鈮?` | `≤` | ` DSP_FFT( src, c, size, RECT); ```  Then, for `1 `鈮?j 鈮?size/2 - 1, CO` |
| 1303 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.96_DSP_SNR.md` | `鈮?` | `≤` | ` DSP_FFT( src, c, size, RECT); ```  Then, for `1 `鈮?j 鈮?size/2 - 1, CO` |
| 1304 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.96_DSP_SNR.md` | `鈮?` | `≤` | ` DSP_FFT( src, c, size, RECT); ```  Then, for `1 `鈮?j 鈮?size/2 - 1, CO` |
| 1305 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.96_DSP_SNR.md` | `鈮?` | `≤` | ` DSP_FFT( src, c, size, RECT); ```  Then, for `1 `鈮?j 鈮?size/2 - 1, CO` |
| 1306 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.96_DSP_SNR.md` | `鈮?` | `≤` | ` DSP_FFT( src, c, size, RECT); ```  Then, for `1 `鈮?j 鈮?size/2 - 1, CO` |
| 1307 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.96_DSP_SNR.md` | `鈮?` | `≤` | ` DSP_FFT( src, c, size, RECT); ```  Then, for `1 `鈮?j 鈮?size/2 - 1, CO` |
| 1308 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.96_DSP_SNR.md` | `鈮?` | `≤` | ` DSP_FFT( src, c, size, RECT); ```  Then, for `1 `鈮?j 鈮?size/2 - 1, CO` |
| 1309 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.96_DSP_SNR.md` | `鈮?` | `≤` | ` DSP_FFT( src, c, size, RECT); ```  Then, for `1 `鈮?j 鈮?size/2 - 1, CO` |
| 1310 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.98_DSP_SORT.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?size 鈮?2097152   \|` |
| 1311 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.98_DSP_SORT.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?size 鈮?2097152   \|` |
| 1312 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.98_DSP_SORT.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?size 鈮?2097152   \|` |
| 1313 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.98_DSP_SORT.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?size 鈮?2097152   \|` |
| 1314 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.98_DSP_SORT.md` | `鈮?` | `≤` | `n/Range   \|  \|  I   \|  `src`   \|  Source array  1 鈮?size 鈮?2097152   \|` |
| 1315 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.99_DSP_SPECTRUM.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  then, for `0`鈮?j 鈮?size/2 - 1, ea` |
| 1316 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.99_DSP_SPECTRUM.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  then, for `0`鈮?j 鈮?size/2 - 1, ea` |
| 1317 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.99_DSP_SPECTRUM.md` | `鈮?` | `≠` | ``` DSP_FFT(src, c, size, RECT); ```  then, for `0`鈮?j 鈮?size/2 - 1, ea` |
| 1318 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.99_DSP_SPECTRUM.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  then, for `0`鈮?j 鈮?size/2 - 1, ea` |
| 1319 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.99_DSP_SPECTRUM.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  then, for `0`鈮?j 鈮?size/2 - 1, ea` |
| 1320 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.99_DSP_SPECTRUM.md` | `鈮?` | `≤` | ``` DSP_FFT(src, c, size, RECT); ```  then, for `0`鈮?j 鈮?size/2 - 1, ea` |
| 1321 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.53.99_DSP_SPECTRUM.md` | `鈮?` | `≠` | ``` DSP_FFT(src, c, size, RECT); ```  then, for `0`鈮?j 鈮?size/2 - 1, ea` |
| 1322 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1323 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1324 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1325 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1326 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1327 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≤` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1328 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≥` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1329 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≤` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1330 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≤` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1331 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01.02_Timing_of_DC_events_-_XPS256.md` | `鈮?` | `≤` | `r slow cycle times make sure 0.5 µs * n comprises 鈮?nbsp;8 cycles.   \|` |
| 1332 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.03_Encoding_Decoding_Table_for_A-Law__-Law.md` | `鈮?` | `≤` | `ing Table for A-Law  \|  Input of DSP_A_ENCODE  P1 鈮?x < P2   \|  Output` |
| 1333 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.03_Encoding_Decoding_Table_for_A-Law__-Law.md` | `鈮?` | `≤` | `ing Table for A-Law  \|  Input of DSP_A_ENCODE  P1 鈮?x < P2   \|  Output` |
| 1334 | `02_System_reference/02.07_Test_Method_Reference/02.07.05.02.09_OutputDC.md` | `鈮?` | `≤` | ` executed. A pass is returned if:  measured value 鈮?maxPassLow  To tes` |
| 1335 | `02_System_reference/02.07_Test_Method_Reference/02.07.05.02.09_OutputDC.md` | `鈮?` | `≤` | ` executed. A pass is returned if:  measured value 鈮?maxPassLow  To tes` |
| 1336 | `02_System_reference/02.07_Test_Method_Reference/02.07.05.02.09_OutputDC.md` | `鈮?` | `≥` | ` executed. A pass is returned if:  measured value 鈮?maxPassLow  To tes` |
| 1337 | `02_System_reference/02.07_Test_Method_Reference/02.07.05.03.07_OutputDC.md` | `鈮?` | `≤` | ` executed. A pass is returned if:  measured value 鈮?maxPassLow  To tes` |
| 1338 | `02_System_reference/02.07_Test_Method_Reference/02.07.05.03.07_OutputDC.md` | `鈮?` | `≤` | ` executed. A pass is returned if:  measured value 鈮?maxPassLow  To tes` |
| 1339 | `02_System_reference/02.07_Test_Method_Reference/02.07.05.03.07_OutputDC.md` | `鈮?` | `≥` | ` executed. A pass is returned if:  measured value 鈮?maxPassLow  To tes` |
| 1340 | `02_System_reference/02.07_Test_Method_Reference/02.07.10.02.01.02_SmartCalc_common_thread_example.md` | `鈥?` | `…` | `2 are processed while run() is invoked for site 1 鈥?5. The remaining s` |
| 1341 | `02_System_reference/02.07_Test_Method_Reference/02.07.11.01.09.08.01_Using_pin_role_groups_for_parallel_protocols.md` | `鈮?` | `≥` | `ciated with bits protocol_width * n + i for all n 鈮?0 such that protoc` |
| 1342 | `02_System_reference/02.07_Test_Method_Reference/02.07.11.01.09.08.01_Using_pin_role_groups_for_parallel_protocols.md` | `鈮?` | `≤` | `ciated with bits protocol_width * n + i for all n 鈮?0 such that protoc` |
| 1343 | `02_System_reference/02.07_Test_Method_Reference/02.07.11.01.11.05.02_Parameter_reconstruction.md` | `鈥?` | `‘` | `rovided, the Pattern Debug Tool display will show 鈥?' for the paramete` |
| 1344 | `02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.09_The__rfm__element.md` | `鈥?` | `…` | ` \|  \|  ARRAY_D getAclr();   \|  <rfm aclr ="1.2,1.3鈥?" />   \|  \|  ARRAY` |
| 1345 | `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.26_loadCap.md` | `鈮?` | `≤` | `ned as working with some bypass capacitor network 鈮?nbsp;10 nF.    - T` |
| 1346 | `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.26_loadCap.md` | `鈮?` | `≥` | `ned as working with some bypass capacitor network 鈮?nbsp;10 nF.    - T` |
| 1347 | `02_System_reference/02.07_Test_Method_Reference/02.07.13.15.01.03_Routing_Tools_-_Utility_Lines_Config_editor.md` | `鈥?` | `…` | ` Scale systems with the last two digits set to 01 鈥?nbsp;32 for utilit` |
| 1348 | `02_System_reference/02.07_Test_Method_Reference/02.07.13.15.01.03_Routing_Tools_-_Utility_Lines_Config_editor.md` | `鈥?` | `…` | ` Scale systems with the last two digits set to 01 鈥?nbsp;32 for utilit` |
| 1349 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.03_Technology_file_for_a_device.md` | `鈮?` | `≥` | `1072 ... 16777216 bytes.    Note  -  For SmarTest 鈮?7.4.3.0:  fast_tra` |
| 1350 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.03_Technology_file_for_a_device.md` | `鈮?` | `≤` | `1072 ... 16777216 bytes.    Note  -  For SmarTest 鈮?7.4.3.0:  fast_tra` |
| 1351 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md` | `鈥?` | `…` | `racteristics.md>).  The programmable range is 0.0 鈥?nbsp;1.0 V for the` |
| 1352 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md` | `鈥?` | `…` | `racteristics.md>).  The programmable range is 0.0 鈥?nbsp;1.0 V for the` |
| 1353 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md` | `鈮?` | `≥` | `6887__max_voltage_drop_return>) is set to a value 鈮?nbsp;0.5 V.    \| T` |
| 1354 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.02.02.01_Estimate_the_time_shift_between_two_swings.md` | `鈮?` | `≈` | `ng>)   with swing1 = 3V, swing2 = 1V and slewrate 鈮?340ps/V.   Note Th` |
| 1355 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.03_Technology_file_for_a_device.md` | `鈮?` | `≥` | `1072 ... 16777216 bytes.    Note  -  For SmarTest 鈮?7.4.3.0:  fast_tra` |
| 1356 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.03_Technology_file_for_a_device.md` | `鈮?` | `≤` | `1072 ... 16777216 bytes.    Note  -  For SmarTest 鈮?7.4.3.0:  fast_tra` |
| 1357 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.04.03_STATEMAP_section_of_the_wavetable.md` | `鈮?` | `≤` | `er - x1/N-mode: N hex numbers, comma separated, N 鈮?1024  When definin` |
| 1358 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.05_Virtual_sequencer_instructions_for_protocol_patterns.md` | `鈮?` | `≥` | `mber n of tester cycles so that n * tester_period 鈮? specified_time  T` |
| 1359 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.md` | `鈥?` | `…` | `d the following characters are not allowed:  # ; (鈥? ) ? @ ,  Other Sm` |
| 1360 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.md` | `鈥?` | `…` | `d the following characters are not allowed:  # ; (鈥? ) ? @ ,  Other Sm` |
| 1361 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.md` | `鈥?` | `…` | `d the following characters are not allowed:  # ; (鈥? ) ? @ ,  Other Sm` |
| 1362 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` | `鈥?` | `…` | `yword    \| Area  \| Description  \| Default \|  \| #1 鈥?#n  site_control  ` |
| 1363 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` | `鈥?` | `…` | `yword    \| Area  \| Description  \| Default \|  \| #1 鈥?#n  site_control  ` |
| 1364 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` | `鈥?` | `…` | `yword    \| Area  \| Description  \| Default \|  \| #1 鈥?#n  site_control  ` |
| 1365 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` | `鈥?` | `…` | `yword    \| Area  \| Description  \| Default \|  \| #1 鈥?#n  site_control  ` |
| 1366 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` | `鈥?` | `…` | `yword    \| Area  \| Description  \| Default \|  \| #1 鈥?#n  site_control  ` |
| 1367 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` | `鈥?` | `…` | `yword    \| Area  \| Description  \| Default \|  \| #1 鈥?#n  site_control  ` |
| 1368 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` | `鈥?` | `…` | `yword    \| Area  \| Description  \| Default \|  \| #1 鈥?#n  site_control  ` |
| 1369 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md` | `鈥?` | `…` | `yword    \| Area  \| Description  \| Default \|  \| #1 鈥?#n  site_control  ` |
| 1370 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 1371 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 1372 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 1373 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 1374 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 1375 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 1376 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈮?` | `≤` | `t of a LOOP_I statement is  LOOP_I [Xi],  where 1 鈮?i 鈮?8.  If no x-mo` |
| 1377 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈮?` | `≤` | `t of a LOOP_I statement is  LOOP_I [Xi],  where 1 鈮?i 鈮?8.  If no x-mo` |
| 1378 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 1379 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.03.02.03_Defining_the_wavetable_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | ` test  The wavetable for a pattern‑based SmartLoop鈩? test is generated` |
| 1380 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≤` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 1381 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≤` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 1382 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≥` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 1383 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≤` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 1384 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≤` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 1385 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md` | `鈮?` | `≥` | ` p of timing set 1 as the largest number r with L 鈮?r 鈮?U which satisf` |
| 1386 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.01.02.03_Period_resolution__clock_resolution__and_master_clock_period.md` | `鈮?` | `≤` | `solution/p,  where p is an integer such that 1.76 鈮? clock_resolution ` |
| 1387 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.01.02.03_Period_resolution__clock_resolution__and_master_clock_period.md` | `鈮?` | `≤` | `solution/p,  where p is an integer such that 1.76 鈮? clock_resolution ` |
| 1388 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.01.02.04_Period_resolution_for_a_multi-port_setup__Smart_Scale.md` | `鈮?` | `≤` | `lock resolution of the respective system, that is 鈮?3.52 ns on a PS160` |
| 1389 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.01_Defining_the_edge_delays_for_Pin_Scale_standard_pins.md` | `鈮?` | `≤` | `lay of a drive pin is  d<n>=<expression>  where 1 鈮?n 鈮?8 and expressi` |
| 1390 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.01_Defining_the_edge_delays_for_Pin_Scale_standard_pins.md` | `鈮?` | `≤` | `lay of a drive pin is  d<n>=<expression>  where 1 鈮?n 鈮?8 and expressi` |
| 1391 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.01_Defining_the_edge_delays_for_Pin_Scale_standard_pins.md` | `鈮?` | `≤` | `lay of a drive pin is  d<n>=<expression>  where 1 鈮?n 鈮?8 and expressi` |
| 1392 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.01_Defining_the_edge_delays_for_Pin_Scale_standard_pins.md` | `鈮?` | `≤` | `lay of a drive pin is  d<n>=<expression>  where 1 鈮?n 鈮?8 and expressi` |
| 1393 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.03.01_Defining_edge_delays_and_period_length_for_a_protocol_engine_test.md` | `鈮?` | `≤` | `lock resolution on the Pin Scale 9G cards is 0.88 鈮?clock_resolution <` |
| 1394 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.03.01_Defining_edge_delays_and_period_length_for_a_protocol_engine_test.md` | `鈮?` | `≤` | `lock resolution on the Pin Scale 9G cards is 0.88 鈮?clock_resolution <` |
| 1395 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.03.03_Defining_edge_delays_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `Loop test  The edges for a pattern‑based SmartLoop鈩?test are distribut` |
| 1396 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.03.03_Defining_edge_delays_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `Loop test  The edges for a pattern‑based SmartLoop鈩?test are distribut` |
| 1397 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.04.02.03.03_Defining_edge_delays_for_a_pattern__ased_SmartLoop_test.md` | `鈩?` | `™` | `Loop test  The edges for a pattern‑based SmartLoop鈩?test are distribut` |
| 1398 | `02_System_reference/02.09_Test_Program_Management/02.09.01.02.05.02.05_BrdTemp_check.md` | `鈩?` | `℃` | `op_rule.  The lines below show that limits of ± 2 鈩?(3.6 鈩? have been ` |
| 1399 | `02_System_reference/02.09_Test_Program_Management/02.09.01.02.05.02.05_BrdTemp_check.md` | `鈩?` | `℉` | `op_rule.  The lines below show that limits of ± 2 鈩?(3.6 鈩? have been ` |
| 1400 | `02_System_reference/02.10_Data_Logging/02.10.01.06.05.29_PassRangeAttrType.md` | `鈮?` | `≤` | `ional operator for the minimum value.  Example: 0 鈮?X < 7: 鈮?is the re` |
| 1401 | `02_System_reference/02.10_Data_Logging/02.10.01.06.05.29_PassRangeAttrType.md` | `鈮?` | `≤` | `ional operator for the minimum value.  Example: 0 鈮?X < 7: 鈮?is the re` |
| 1402 | `02_System_reference/02.10_Data_Logging/02.10.03.05.28_Activity_Trace_Event_Record__ATER.md` | `鈥?` | `​` | `tion that was specified with the setTestCaseSource鈥?) method. \|  \| HEA` |
| 1403 | `02_System_reference/02.10_Data_Logging/02.10.03.05.28_Activity_Trace_Event_Record__ATER.md` | `鈥?` | `​` | `tion that was specified with the setTestCaseSource鈥?) method. \|  \| HEA` |
| 1404 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.01.01.01_The_Input_Columns.md` | `鈮?` | `≥` | `e different ASCII periods as follows:    - If gcd 鈮?minimaltest system` |
| 1405 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.01.01.01_The_Input_Columns.md` | `鈮?` | `≤` | `e different ASCII periods as follows:    - If gcd 鈮?minimaltest system` |
| 1406 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.02.01.03_Defining_the_Clock_for_Fast_Differential_Receive_Pins__ssb_on_off.md` | `鈮?` | `≤` | ` for the two shots (this is also done for x-modes 鈮?10). - It determin` |
| 1407 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.03.01_The_Structure_of_the_X-Mode_Control_File.md` | `鈥?` | `‘` | `on the mapping operator see [The Mapping Operator 鈥?>'](<02.11.02.02.0` |
| 1408 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.03.01_The_Structure_of_the_X-Mode_Control_File.md` | `鈥?` | `‘` | `on the mapping operator see [The Mapping Operator 鈥?>'](<02.11.02.02.0` |
| 1409 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.03.07_Controlling_the_Waveforms_for_Differential_Pins.md` | `鈥?` | `‘` | ` mapping operator. If the normal mapping operator 鈥?>' is used, or no ` |
| 1410 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.03.07_Controlling_the_Waveforms_for_Differential_Pins.md` | `鈥?` | `‘` | ` mapping operator. If the normal mapping operator 鈥?>' is used, or no ` |
| 1411 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.06.01.04_Generating_the_Wavetable_and_Timing_Map_File.md` | `鈥?` | `‘` | ` file. This is achieved by defining the character 鈥?' as a wildcard fo` |
| 1412 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.03.02.02.02_The_ASCII_Vector_Row.md` | `鈮?` | `≥` | `right. If the length of the binary number is m (m 鈮? n), then the left` |
| 1413 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.03.02.03_Translating_ASCII_Vectors_with_Differential_Pins.md` | `鈥?` | `‘` | ` (see [Evaluation by Signal (the Mapping Operator 鈥?>')](<02.11.02.02.` |
| 1414 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.03.03.03.03_Defining_the_Scan_Instances.md` | `鈥?` | `‘` | `pins are ignored, but some character (for example 鈥?strong>-') must be` |
| 1415 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.03.03.07.02_Synchronizing_Scan_and_Parallel_Ports_with_Different_X-Mode_Factors.md` | `鈮?` | `≥` | ` such that n is directly divisible by xP*xS and n 鈮?TL. Call this corr` |
| 1416 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.03.04.01_Structure_of_a_Timing_Map_File_Block.md` | `鈥?` | `‘` | `_Keeping_the_Clock_Alive.md>)). In this case, the 鈥?strong>*' characte` |
| 1417 | `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.11_SharedLeakageParallel_test_method.md` | `鈥?` | `‘` | `onnects all power supplies. The power supply‘s DPS鈥?are left configure` |
| 1418 | `02_System_reference/02.16_ACS_TE-Cloud/02.16.03.08_Transmitting_files_between_Linux_machines_with_command_line.md` | `锛?` | `：` | `_file_name transmit_file_name login_name@public_IP锛?var class="varname` |
| 1419 | `02_System_reference/02.16_ACS_TE-Cloud/02.16.04.05_Transmitting_files_to_the_tester.md` | `锛?` | `：` | `_file_name transmit_file_name login_name@tester_IP锛?var class="varname` |
| 1420 | `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.04_Tools_to_analyze_the_situation.md` | `鈥?` | `‘` | `ill be called automatically.  - Get the result in 鈥?Device/report/' or` |
| 1421 | `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md` | `鈮?` | `≥` | `end the single-port flat pattern n times, where n 鈮?1 (default 1). The` |
| 1422 | `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md` | `鈮?` | `≥` | `end the single-port flat pattern n times, where n 鈮?1 (default 1). The` |
| 1423 | `03_Use_cases_and_application_papers/03.08_How_to_set_up_a_multiport_EPRC_match_loop/03.08_How_to_set_up_a_multiport_EPRC_match_loop.md` | `鈥?` | `…` | `ng>) - [Putting the two important points together 鈥?/a> - [What if the` |
| 1424 | `03_Use_cases_and_application_papers/03.08_How_to_set_up_a_multiport_EPRC_match_loop/03.08_How_to_set_up_a_multiport_EPRC_match_loop.md` | `鈥?` | `…` | `ng>) - [Putting the two important points together 鈥?/a> - [What if the` |
| 1425 | `03_Use_cases_and_application_papers/03.08_How_to_set_up_a_multiport_EPRC_match_loop/03.08_How_to_set_up_a_multiport_EPRC_match_loop.md` | `鈥?` | `…` | `ng>) - [Putting the two important points together 鈥?/a> - [What if the` |
| 1426 | `03_Use_cases_and_application_papers/03.08_How_to_set_up_a_multiport_EPRC_match_loop/03.08_How_to_set_up_a_multiport_EPRC_match_loop.md` | `鈥?` | `…` | `ng>) - [Putting the two important points together 鈥?/a> - [What if the` |
| 1427 | `03_Use_cases_and_application_papers/03.08_How_to_set_up_a_multiport_EPRC_match_loop/03.08_How_to_set_up_a_multiport_EPRC_match_loop.md` | `鈥?` | `…` | `ng>) - [Putting the two important points together 鈥?/a> - [What if the` |
| 1428 | `03_Use_cases_and_application_papers/03.08_How_to_set_up_a_multiport_EPRC_match_loop/03.08_How_to_set_up_a_multiport_EPRC_match_loop.md` | `鈥?` | `…` | `ng>) - [Putting the two important points together 鈥?/a> - [What if the` |
| 1429 | `03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md` | `鈥?` | `…` | `ight utility pogo blocks. The pogo pins are URW00 鈥?nbsp;URW15 on 2‑ro` |
| 1430 | `03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md` | `鈥?` | `…` | `ight utility pogo blocks. The pogo pins are URW00 鈥?nbsp;URW15 on 2‑ro` |
| 1431 | `03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.01.01_TP360_3.7.0.md` | `锛?` | `？` | `d parameters and test suite flags in testflow view锛?/td> \|  \| Test Pro` |
| 1432 | `03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.17_CSV_rule_file_for_checking_voltage_current_risks.md` | `鈥?` | `–` | `urrent programmed to pins with [Smart correlation 鈥?Release Checker](<` |
| 1433 | `03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.07.18_CSV_rule_file_for_flow_execution.md` | `鈥?` | `–` | `onditional flow execution with [Smart correlation 鈥?Release Checker](<` |
| 1434 | `03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.10.01_Generating_failure_mode_error_analyzer_reports.md` | `锛?` | `，` | ` closed.  -  If you want to customize the analysis锛?such as the wait t` |
| 1435 | `03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04.10.02_Preference_of_Failure_Mode_Error_Analyzer.md` | `銆?` | `。` | `rd. You can set the interval for the board cooling銆?/li> - Pause runni` |
| 1436 | `03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04_Using_TP360.md` | `鈥?` | `–` | `setups in your test program. - [Smart Correlation 鈥?Release Data Colle` |
| 1437 | `03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13.04_Using_TP360.md` | `鈥?` | `–` | `setups in your test program. - [Smart Correlation 鈥?Release Data Colle` |
| 1438 | `03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13_Test_Program_360_Cookbook.md` | `鈥?` | `–` | `setups in your test program. - [Smart Correlation 鈥?Release Data Colle` |
| 1439 | `03_Use_cases_and_application_papers/03.13_Test_Program_360_Cookbook/03.13_Test_Program_360_Cookbook.md` | `鈥?` | `–` | `setups in your test program. - [Smart Correlation 鈥?Release Data Colle` |
| 1440 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.06.08_X-Mode_Pattern_Synchronization_to_Free_Running_Bit_Streams.md` | `鈮?` | `≥` | ` does not support word alignment   \|  \|  bit time 鈮?minimum cycle time` |
| 1441 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.06.08_X-Mode_Pattern_Synchronization_to_Free_Running_Bit_Streams.md` | `鈮?` | `≥` | ` does not support word alignment   \|  \|  bit time 鈮?minimum cycle time` |
| 1442 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.06.11_ATE_solutions_to_3D-IC_test_challenges__The_readiness_of_Advantest_s_V93.md` | `鈥?` | `–` | `challenges.  ## Test Program Software Maintenance 鈥?SmarTest Program M` |
| 1443 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.06.11_ATE_solutions_to_3D-IC_test_challenges__The_readiness_of_Advantest_s_V93.md` | `鈥?` | `–` | `challenges.  ## Test Program Software Maintenance 鈥?SmarTest Program M` |
| 1444 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.06.11_ATE_solutions_to_3D-IC_test_challenges__The_readiness_of_Advantest_s_V93.md` | `鈥?` | `–` | `challenges.  ## Test Program Software Maintenance 鈥?SmarTest Program M` |
| 1445 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.08_Choosing_the_Dielectric_Material_for_a_V93000_DUT_Loadboard.md` | `鈮?` | `≤` | `  0.0014   \|  2   \|  \|  FASTRISE 27   \|  2.7   \|  鈮?.0020   \|  鈮?.0020` |
| 1446 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1447 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1448 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1449 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1450 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1451 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1452 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1453 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1454 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1455 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1456 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1457 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1458 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1459 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1460 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1461 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1462 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1463 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1464 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1465 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1466 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1467 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1468 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1469 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1470 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1471 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1472 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1473 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1474 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1475 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1476 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1477 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1478 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1479 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1480 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1481 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
| 1482 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md` | `鈩?` | `™` | `xisted in package test[2]. The V93000 Direct-Probe鈩?solution substanti` |
