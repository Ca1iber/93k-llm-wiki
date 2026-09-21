# 建页资料包 06 — 02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md

## 0. 元信息

- 标题（frontmatter）：XPS256 programming - PMU operating mode
- H1：XPS256 programming - PMU operating mode
- 字节：19208；出度：58；入边：57
- frontmatter：`{"source_html": "02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.htm", "source_topic": "354253.htm", "title": "XPS256 programming - PMU operating mode"}`
- 标题结构：XPS256 programming - PMU operating mode / Pin definition / Hardware view / SmartRDI overview / API overview / Relay switching in PMU operating mode / Supported measurement modes / Application note / Examples / Examples / Example 1: SmartRDI, pattern鈥慴ased programming / Example 2: SmartRDI, code鈥慴ased programming / Example 3: Test method API SPMU_TASK / Related information / Functional changes

## 1. 定义文档全文（raw，禁止修改）

```markdown
---
title: "XPS256 programming - PMU operating mode"
source_topic: "354253.htm"
source_html: "02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.htm"
---
# XPS256 programming - PMU operating mode

In PMU operating mode, a pin is used like a standard PMU to temporarily supply power during the execution of a single test suite or a group of test suites.

  The following sections are available in this topic:

 |

- [Pin definition](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Pin_definition>)
- [Hardware view](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Hardware_view>)
- [SmartRDI overview](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_SmartRDI_overview>)
- [API overview](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_API_overview>)
- [Relay switching in PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Relay_switching>)
- [Supported measurement modes](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Supported_measure_modes>)
 |

- [Application note](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Application_notes>)
- [Examples](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_examples_overview>)

  - [Example 1: SmartRDI, pattern鈥慴ased programming](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_pattern-based>)
  - [Example 2: SmartRDI, code鈥慴ased programming](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_code-based>)
  - [Example 3: Test method API SPMU_TASK](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_TM_API_based>)

 |

## Pin definition

An XPS256 pin is configured to operate in PMU operating mode if it is defined as dc type pin using the [Digital Pins editor](<../02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md>). The Type parameter is to be set to dc and the Mode parameter is to be set to SIG.

See also [Digital Pins editor](<../02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md>).

## Hardware view

[Hardware view](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md>) of XPS256 in PMU operating mode:

   ![HW view of XPS256 in PMU operating mode](<../../../../raw/354251.png>)   Buttons of the Hardware view:

 |

- Quick

Performs a single measurement using the settings defined by the Measure dialog and displays the measured value in one of the fields below.

- MeasureAllows setting the basic parameters and performs single or looped measurements. Supported measurements are

  - Voltage measurement and current measurement
  - Voltage drop measurement on the force line or the return line.

- [Check Status Flags](<02.05.05.03.10.02_XPS256_status_flags.md>)

Reads and clears the latched status flags.

 |

- [Profiling](<02.05.05.03.03.05_XPS256_profiling.md>)

Starts profiling of the voltage or current and displays the sampled waveform.

- [Force Sense Check](<02.05.05.03.10.12_XPS256_programming_-_Kelvin_test___sense_connection_test.md>)

Performs a sense connection test.

- [Surge Tracker](<02.05.05.03.10.17_XPS256_programming_-_Surge_tracker.md>)

Reads and clears the latched status of the surge tracker.

- [Max Voltage Drop](<02.05.05.03.10.19_XPS256_programming_-_Voltage_drop_measurement.md>)

Reads the latched maximum voltage drop for the force line and for the return line and resets the two values.

- [Check Gang Connection](<02.05.05.03.10.10_XPS256_programming_-_Ganging.md#_354657__s_Checking_the_gang_connections>)

Performs a connection check for all channels of ganging groups.

   |  In the Measure dialog you cannot only set the standard parameters, but also change the regulation and safety parameters for the measurement:

 |   ![XPS256 HW view PMU Measure dialog](<../../../../raw/355135.png>)    | See also [Default values](<02.05.05.03.10.05_XPS256_programming_-_Default_values.md>), [Load step response](<02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md>), and [Voltage drop measurement](<02.05.05.03.10.19_XPS256_programming_-_Voltage_drop_measurement.md>). |

## SmartRDI overview

The complete functionality to set up an XPS256 channel in the PMU operating mode is covered by the dc() API of SmartRDI. Both the code鈥慴ased mode and the pattern鈥慴ased mode are supported. For more information refer to [Setting up DC Scale pins with SmartRDI](<../02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) and the related member functions of the API.

## API overview

The complete functionality to set up an XPS256 channel in the PMU operating mode and to perform voltage and current measurements are covered by APIs [SPMU_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md>) and [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>).

Pattern鈥慴ased setups and measurements are supported by [DC events](<../02.07_Test_Method_Reference/02.07.04.01.63_EVENT_...__DC_events_API_reference.md#_345840__s_Event_classes_and_data_types>). For the maximum pattern frequency, refer also to [Minimum period / maximum frequency of the sequencer](<../02.08_Setup_and_Result_Tools/02.08.04.34.06.05.01_Minimum_period___maximum_frequency_of_the_sequencer.md>).

## Relay switching in PMU operating mode

The [relay()](<../02.07_Test_Method_Reference/02.07.04.01.234.01.28_SPMU_PIN_TASK.relay.md>) member function of the SPMU_PIN_TASK class selects the termination mode that specifies the relay control pattern of the target pins.

DC-Scale cards support the following relay switching modes:

- NO
- NT

The termination modes NTMBB, NTBBM, and TERM are not supported by DC-Scale cards.

The tables below show the effect of relay switching with and without [preCharge](<../02.07_Test_Method_Reference/02.07.04.01.234.01.26_SPMU_PIN_TASK.preCharge.md>).

 Note In [SPMU_TASK.execMode()](<../02.07_Test_Method_Reference/02.07.04.01.234.02_SPMU_TASK.execMode.md>), you can use the TM::FORCE_ON and TM::FORCE_OFF options to connect or disconnect a PMU pin, but not in combination with [SPMU_PIN_TASK.mode()](<../02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md>) set to "..._UNGANGED".

Actions based on relay settings in PMU operating mode without precharge
 | [SPMU_TASK.execMode()](<../02.07_Test_Method_Reference/02.07.04.01.234.02_SPMU_TASK.execMode.md>)  | FORCE_ON  | GPF | PPF | PVAL  | FORCE_OFF |
 | [SPMU_PIN_TASK.relay()](<../02.07_Test_Method_Reference/02.07.04.01.234.01.28_SPMU_PIN_TASK.relay.md>)  | NO  | NT  | NO  | NT  | NO  | NT |
 | Setup PMU  | Yes  | Yes  | Yes  | Yes  | Yes  | Yes |
 | Close relay  | leave unchanged  | Yes  | leave unchanged  | Yes  | leave unchanged  | leave unchanged |
 | Do measure  | No  | No  | Yes  | Yes  | No  | No |
 | Open relay  | leave unchanged  | leave unchanged  | leave unchanged  | Yes  | leave unchanged  | Yes |

Actions based on relay settings in PMU operating mode with precharge
 | [SPMU_TASK.execMode()](<../02.07_Test_Method_Reference/02.07.04.01.234.02_SPMU_TASK.execMode.md>)  | FORCE_ON  | GPF | PPF | PVAL  | FORCE_OFF |
 | [SPMU_PIN_TASK.relay()](<../02.07_Test_Method_Reference/02.07.04.01.234.01.28_SPMU_PIN_TASK.relay.md>)  | NO  | NT  | NO  | NT  | NO  | NT |
 | Precharge PMU  | No  | Yes  | No  | Yes  | No  | No |
 | Close relay  | leave unchanged  | Yes  | leave unchanged  | Yes  | leave unchanged  | leave unchanged |
 | Setup PMU  | Yes  | Yes  | Yes  | Yes  | Yes  | Yes |
 | Do measure  | No  | No  | Yes  | Yes  | No  | No |
 | Open relay  | leave unchanged  | leave unchanged  | leave unchanged  | Yes  | leave unchanged  | Yes |

## Supported measurement modes

Supported measurement modes of the [SPMU_PIN_TASK.mode()](<../02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md>) API:

 | Parameter mode  | Description  | Note |
 | "VFVM"  | Force voltage and measure voltage.  |   | Basic voltage or current forcing modes of the PMU with programmable current or voltage clamp.

Note: Unlike other DC scale cards, XPS256 pins feature a real current force mode with programmable voltage clamps.

 |
 | "VFIM"  | Force current and measure voltage.  | |
 | "VFIM_UNGANGED"  | Force voltage and measure current by temporarily separating ganged channels for this measurement.  | |
 | "CFVM"  | Force current directly and measure voltage.  | |
 | "CFIM"  | Force current directly and measure current.  | |
 | "IFVM"  | Force current and measure voltage.  |   | Legacy mode for compatibility with other DC scale cards: Currents are forced using the clamp current functionality. The clamp current is programmed to the required force value, and the voltage must be set to a value that forces the pin into the clamping situation. |
 | "IFVM_UNGANGED"  | Force current and measure voltage by temporarily separating ganged channels for this measurement.

Voltage measurements in unganged mode means that the number of forcing channels of a ganging group is minimized temporarily to improve the stability of the forced current and the voltage measurement.

  | |
 | "VM_HIZ"  | High impedance voltage measurement.  |   | The PMU is set to a high-impedance mode. Only voltage measurements are supported. |

## Application note

 DC events in reused pattern For a minimized test time we recommend, not to reuse pattern with DC events that are to be applied for different XPS256 ranges. The recommendation applies to pattern that are manually created using the related test method APIs but not to the automatically created [SmartRDI](<../02.07_Test_Method_Reference/02.07.13_SmartRDI.md>) pattern.

The XPS256 channels feature several force ranges. The pattern data of related DC events must be reloaded in case the containing pattern is reused for another range. This may significantly increase the test time.

The recommendation applies to all DC events that change the force- or clamp value or range or the measurement range.

## Examples

### Examples

The following examples demonstrate how to set up an XPS256 pin for a standard current measurement.

The three examples are set up in a three-step sequence of connecting the pin and applying the basic setup, measuring the requested parameter, and disconnecting in a separate task. This sequence is suitable for XPS256-specific tests, since very often more than one setup has to be applied and more than one measurement has to be carried out before the pin is disconnected again.

 These examples are available in the following sections:

- [Example 1: SmartRDI, pattern鈥慴ased programming](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_pattern-based>)

Pattern鈥慴ased programming using SmartRDI is the recommended solution that requires the least amount of code and on the other hand delivers the most stable result in terms of timing.

- [Example 2: SmartRDI, code鈥慴ased programming](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_code-based>)

Code鈥慴ased programming using SmartRDI needs some more code and must follow the structure of the wrapped test method APIs.

- [Example 3: Test method API SPMU_TASK](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_TM_API_based>)

This example is based on the test method APIs and is strongly tied to the structure of the underlying commands.

The code of the three examples generates the same measurement sequence for the programmed pin. If you use the [Trace Function](<../02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.md>) to compare the code鈥慴ased SmartRDI example and the example based on the test method APIs, you will get the same output in the MCDLog file.

### Example 1: SmartRDI, pattern鈥慴ased programming

The example uses a code鈥慴ased [RDI command](<../02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md#_142604__dle_RDI_command>) to setup and connect the XPS256 pin. The following [RDI block](<../02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md#_142604__dle_RDI_block>) performs a pattern鈥慴ased measurement. The last RDI command disconnects the XPS256 pin in code鈥慴ased mode.

Since the RDI block uses a specialized [DC event](<../02.07_Test_Method_Reference/02.07.04.01.63_EVENT_...__DC_events_API_reference.md>) to perform the measurement, only the measurement related parameters must be defined. In contrast, for code鈥慴ased programming with SmartRDI or programming with test method APIs, all parameters must be specified also for the measurement.

```
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
    rdi.dc().pin("XPS256_PMU_1")
            .vForce         ( 5.0 V)          .vForceRange(7.0 V).preCharge(0.0 V)
            .iClamp         (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .execute        ();

    RDI_BEGIN();
    {
        rdi.dc("iMeasXPS256").pin("XPS256_PMU_1")
                .iMeas      ()
                .average    (16)
                .measWait   (2.5 ms)
                .execute    ();
    }
    RDI_END();

    rdi.dc().pin("XPS256_PMU_1").disconnect().execute();
}
ON_FIRST_INVOCATION_END();

double resultIMeasXPS256;

resultIMeasXPS256 = rdi.id("iMeasXPS256").getValue("XPS256_PMU_1");
```

### Example 2: SmartRDI, code鈥慴ased programming

The first [RDI command](<../02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md#_142604__dle_RDI_command>) connects and sets the XPS256 pin: DC Scale pins in PMU operating mode are automatically connected if [iForce()](<../02.07_Test_Method_Reference/02.07.13.12.02.16_iForce.md>) or [vForce()](<../02.07_Test_Method_Reference/02.07.13.12.02.41_vForce.md>) are used within the RDI command. For more information, see also [Setting up DC Scale pins with SmartRDI](<../02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>).

The second RDI command contains a measurement iMeas(). The programmed pin remains connected after the measurement.

The third RDI command contains no measurement but the disconnect() function: Output relays are controlled again and the pin is disconnected.

In this example, SmartRDI is mainly a wrapper for the test method API [SPMU_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md>). The structure is therefore tied to the SPMU_TASK and to the corresponding low level commands as mentioned in [Example 3: Test method API SPMU_TASK](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_TM_API_based>) below.

```
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
    rdi.dc().pin("XPS256_PMU_1")
            .vForce         ( 0.0 V)          .vForceRange(7.0 V).preCharge(0.0 V)
            .iClamp         (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .execute        ();

    rdi.dc("iMeasXPS256").pin("XPS256_PMU_1")
            .vForce         ( 5.0 V)          .vForceRange(7.0 V)
            .iClamp         (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .iMeas          ()
            .average        (16)
            .measWait       (2.5 ms)
            .execute        ();

    rdi.dc().pin("XPS256_PMU_1").disconnect().execute();
}
ON_FIRST_INVOCATION_END();

double resultIMeasXPS256;

resultIMeasXPS256 = rdi.id("iMeasXPS256").getValue("XPS256_PMU_1");
```

### Example 3: Test method API SPMU_TASK

XPS256 measurements, created by the test method API [SPMU_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md>) are based on the low-level commands [DCCH](<../02.06_Command_Reference/02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md>) and [DCVH](<../02.06_Command_Reference/02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md>) in combination with [DCEX](<../02.06_Command_Reference/02.06.02.02.43_DCEX_-__DC_set_EXecute.md>). These commands define complete measurement sequences including connecting and disconnecting the programmed pins.

 The tasks spmuTask_connect as well as spmuTask_measure of the example must therefore define the same mode() and connectState() and ensure that the same ranges are used, although the first task is used only to connect and activate the pin while the second task is used only for the measuring:

- spmuTask_connect: The combination of `relay("NT")` and `execMode(TM::FORCE_ON)` of the connect task enables switching of the output relays and activation of the pin. A measurement is not supported by this task.
- spmuTask_measure: Relay control is set to "NO" to inhibit actions of the output relays. The pin remains therefore connected after the task has been performed. `execMode(TM::PVAL)` causes that the requested value is measured and returned as per pin value and pass/fail results.
- spmuTask_disconnect: The combination of `relay("NT")` and `execMode(TM::FORCE_OFF)` causes that the pin is disconnected. Although no more measurements are performed, some parameters such as `min()` and `max()` must be defined for a valid setup.

```
SPMU_TASK spmuTask_connect;
SPMU_TASK spmuTask_measure;
SPMU_TASK spmuTask_disconnect;

ON_FIRST_INVOCATION_BEGIN();
{
    spmuTask_connect.pin("XPS256_PMU_1")
            .mode           ("VFIM")
            .vForce         ( 0.0 V)          .vForceRange(7.0 V).preCharge(0.0 V)
            .clamp          (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .min            (-5.0 mA)
            .max            (50.0 mA)
            .relay          ("NT");

    spmuTask_measure.pin("XPS256_PMU_1")
            .mode           ("VFIM")
            .vForce         ( 5.0 V)          .vForceRange(7.0 V)
            .clamp          (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
            .min            (-5.0 mA)
            .max            (50.0 mA)
            .relay          ("NO")
            .settling       (2.5 ms)
            .samples        (16);

    spmuTask_disconnect.pin("XPS256_PMU_1")
            .vForce         ( 0.0 V)
            .min            ( 0.0 mA)
            .max            (10.0 uA)
            .relay          ("NT");

    spmuTask_connect   .execMode(TM::FORCE_ON) .execute();
    spmuTask_measure   .execMode(TM::PVAL)     .execute();
    spmuTask_disconnect.execMode(TM::FORCE_OFF).execute();
}
ON_FIRST_INVOCATION_END();

double resultIMeasXPS256;

resultIMeasXPS256 = spmuTask_measure.getValue("XPS256_PMU_1");
```

## Related information

[XPS256 programming - DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md>)[XPS256 operating modes](<02.05.05.03.05_XPS256_operating_modes.md>)[Setting up DC Scale pins with SmartRDI](<../02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>)

## Functional changes

- Introduced in SmarTest 7.10.1
```

## 2. 语法 / 参数段落（脚本逐字抽取，§4 —— 进页面时照抄，不重写）

### 〔Examples〕

```text
The following examples demonstrate how to set up an XPS256 pin for a standard current measurement.

The three examples are set up in a three-step sequence of connecting the pin and applying the basic setup, measuring the requested parameter, and disconnecting in a separate task. This sequence is suitable for XPS256-specific tests, since very often more than one setup has to be applied and more than one measurement has to be carried out before the pin is disconnected again.

 These examples are available in the following sections:

- [Example 1: SmartRDI, pattern鈥慴ased programming](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_pattern-based>)

Pattern鈥慴ased programming using SmartRDI is the recommended solution that requires the least amount of code and on the other hand delivers the most stable result in terms of timing.

- [Example 2: SmartRDI, code鈥慴ased programming](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_code-based>)

Code鈥慴ased programming using SmartRDI needs some more code and must follow the structure of the wrapped test method APIs.

- [Example 3: Test method API SPMU_TASK](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_TM_API_based>)

This example is based on the test method APIs and is strongly tied to the structure of the underlying commands.

The code of the three examples generates the same measurement sequence for the programmed pin. If you use the [Trace Function](<../02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.md>) to compare the code鈥慴ased SmartRDI example and the example based on the test method APIs, you will get the same output in the MCDLog file.
```

## 3. 入边 29 篇（谁引它、引它的原句 —— 「和谁有关」的唯一来源）

### ← XPS256 programming - PMU operating mode
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md`（引 15 次）

- L14：[Pin definition](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Pin_definition>)
- L15：[Hardware view](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Hardware_view>)
- L16：[SmartRDI overview](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_SmartRDI_overview>)
- L17：[API overview](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_API_overview>)

### ← XPS256 in PMU operating mode
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.05.02_XPS256_in_PMU_operating_mode.md`（引 5 次）

- L18：The static and dynamic behavior is defined by a combination of the connection state, the measurement mode, and the execution mode as described below. For more information refer to the [XPS256 programming - PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).
- L24：See also section [Hardware view](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Hardware_view>) in [XPS256 programming - PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).
- L24：See also section [Hardware view](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Hardware_view>) in [XPS256 programming - PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).
- L51：The measurement mode defines the force mode and the measurement mode of the channel when it is configured for the PMU operating mode. For more information and a list of all supported measurement modes, refer to [XPS256 programming - PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_ope

### ← XPS256 programming - Measure currents
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.13_XPS256_programming_-_Measure_currents.md`（引 5 次）

- L61：In [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>), automatic down鈥憆anging is supported only for [pattern鈥慴ased](<../02.07_Test_Method_Reference/02.07.01.01.02_Code-based_and_pattern-based_programming.md#_355202__s_Pattern-based_programming>) programming using th
- L97：Setting the current measurement range for automatic down鈥憆anging in [DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md>) is supported for the code鈥慴ased mode and for the pattern鈥慴ased mode. Setting the current measurement range for automatic down鈥憆anging in [PMU opera
- L101：The complete functionality to set up an XPS256 pin to measure currents is covered by APIs [SPMU_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md>) and [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>) for an XPS256 pin in [PMU operating mode](<02
- L153：| Setting the current measurement range for automatic down鈥憆anging in [DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md>) is supported for the [code鈥慴ased](<../02.07_Test_Method_Reference/02.07.01.01.02_Code-based_and_pattern-based_programming.md#_355202__s_Code-base

### ← XPS256 programming - Ganging
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.10_XPS256_programming_-_Ganging.md`（引 3 次）

- L71：Ganging groups for [XPS256 channels in PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>) are defined in the Digital Pins editor. You can specify the range of channels to be ganged by "-" (hyphen) or each channel separated by "," (comma). For more information refer t
- L77：APIs [SPMU_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md>) and [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>) for an [XPS256 pin in PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>) or by the
- L118：The gang connection test is supported by the [Hardware view](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md>) for the XPS256 pins in [DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md#_354249__s_Hardware_view>) or in [PMU operatin

### ← XPS256 programming - Measure voltages
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.14_XPS256_programming_-_Measure_voltages.md`（引 2 次）

- L77：The complete functionality to set up an XPS256 pin to measure voltages is covered by APIs [SPMU_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md>) and [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>) for an XPS256 pin in [PMU operating mode](<02
- L149：Voltage measurements are supported by the [Hardware view](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md>) for the XPS256 pins in [DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md#_354249__s_Hardware_view>) or in [PMU operating m

### ← XPS256 programming - Open loop protection
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.16_XPS256_programming_-_Open_loop_protection.md`（引 2 次）

- L44：Setup in [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>):
- L48：The status can also be changed in the Hardware view for the [DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md>) and for the [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).

### ← XPS256 programming - Voltage drop measurement
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.19_XPS256_programming_-_Voltage_drop_measurement.md`（引 2 次）

- L49：Measure dialog of the [Hardware view](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Hardware_view>) in [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).
- L49：Measure dialog of the [Hardware view](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__s_Hardware_view>) in [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).

### ← XPS256 programming overview
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10_XPS256_programming_overview.md`（引 2 次）

- L24：[XPS256 programming - PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>)
- L37：[DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md>) - [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>)

### ← XPS256 sitemap
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.01_XPS256_sitemap.md`（引 1 次）

- L33：[DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md>) - [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>)

### ← XPS256 profiling
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.03.05_XPS256_profiling.md`（引 1 次）

- L23：or in the [Hardware view](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md>) for the XPS256 pins in [DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md#_354249__s_Hardware_view>) or in [PMU operating mode](<02.05.05.03.10.15_XPS256_p

### ← XPS256 measure currents
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.07.02_XPS256_measure_currents.md`（引 1 次）

- L69：In [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>), automatic down鈥憆anging is supported only for [pattern鈥慴ased](<../02.07_Test_Method_Reference/02.07.01.01.02_Code-based_and_pattern-based_programming.md#_355202__s_Pattern-based_programming>) programming using th

### ← XPS256 programming - AWG
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.03_XPS256_programming_-_AWG.md`（引 1 次）

- L40：The basic setup of the AWG must be programmed by standard APIs for an XPS256 pin in [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>) or by the [Equation based level setup](<../02.08_Setup_and_Result_Tools/02.08.04.14.02_Equation_based_level_setup.md>) or API [DPS_

### ← XPS256 programming - DGT
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.06_XPS256_programming_-_DGT.md`（引 1 次）

- L58：The basic setup of the DGT must be programmed by standard APIs for an XPS256 pin in [PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>) or by the [Equation based level setup](<../02.08_Setup_and_Result_Tools/02.08.04.14.02_Equation_based_level_setup.md>) or API [DPS_

### ← XPS256 programming - DPS operating mode
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md`（引 1 次）

- L182：[XPS256 programming - PMU operating mode](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>)[XPS256 operating modes](<02.05.05.03.05_XPS256_operating_modes.md>)[DPS Pins editor](<../02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.md>)[DPSPINS](<../02.08_Setup_and_Resul

### ← XPS256 programming - Force and clamp currents
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.08_XPS256_programming_-_Force_and_clamp_currents.md`（引 1 次）

- L107：The complete functionality to set up an XPS256 pin to force or clamp currents is covered by APIs [SPMU_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md>) and [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>) for an XPS256 pin in [PMU operating mo

### ← XPS256 programming - Force and clamp voltages
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.09_XPS256_programming_-_Force_and_clamp_voltages.md`（引 1 次）

- L115：The complete functionality to set up an XPS256 pin to force or clamp voltages is covered by APIs [SPMU_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md>) and [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>) for an XPS256 pin in [PMU operating mo

### ← XPS256 programming - Kelvin test / sense connection test
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.12_XPS256_programming_-_Kelvin_test___sense_connection_test.md`（引 1 次）

- L64：The Kelvin test / sense connection test is supported by the [Hardware view](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md>) for the XPS256 pins in [DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md#_354249__s_Hardware_view>) or i

### ← XPS256 programming - Surge tracker
`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.17_XPS256_programming_-_Surge_tracker.md`（引 1 次）

- L65：The Kelvin test / sense connection test is supported by the [Hardware view](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md>) for the XPS256 pins in [DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md#_354249__s_Hardware_view>) or i

### ← SPMU_PIN_TASK.highAccuracy()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.11_SPMU_PIN_TASK.highAccuracy.md`（引 1 次）

- L10：Only the [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) in the [PMU operating mode](<../02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>) is supported:

### ← SPMU_PIN_TASK.iMeasureRange()
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.16_SPMU_PIN_TASK.iMeasureRange.md`（引 1 次）

- L64：For [code鈥慴ased](<02.07.01.01.02_Code-based_and_pattern-based_programming.md#_355202__s_Code-based_programming>) programming, the [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) does not support automatic down鈥憆anging in [PMU operating mode](<../02.05_Test_Head

### ← SmartRDI 7.10.1
`02_System_reference/02.07_Test_Method_Reference/02.07.13.01.03_SmartRDI_7.10.1.md`（引 1 次）

- L22：In SmartRDI 7.10.1, these member functions only support [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) in the [PMU operating mode](<../02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).

### ← forceDropWarn()
`02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.09_forceDropWarn.md`（引 1 次）

- L12：This function only supports [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) in the [PMU operating mode](<../02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).

### ← hiAccuracy()
`02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.10_hiAccuracy.md`（引 1 次）

- L10：Only the [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) in the [PMU operating mode](<../02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>) is supported:

### ← iClampTimeToAlarm()
`02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.13_iClampTimeToAlarm.md`（引 1 次）

- L12：This function only supports [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) in the [PMU operating mode](<../02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).

### ← iClampTimeToDisconnect()
`02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.14_iClampTimeToDisconnect.md`（引 1 次）

- L12：This function only supports [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) in the [PMU operating mode](<../02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).

### ← iMeasRange()
`02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.19_iMeasRange.md`（引 1 次）

- L37：For [code鈥慴ased](<02.07.01.01.02_Code-based_and_pattern-based_programming.md#_355202__s_Code-based_programming>) programming, the [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) does not support automatic down鈥憆anging in [PMU operating mode](<../02.05_Test_Head

### ← loadStepMode()
`02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.27_loadStepMode.md`（引 1 次）

- L12：This function supports only [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) in the [PMU operating mode](<../02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).

### ← pulldown()
`02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.33_pulldown.md`（引 1 次）

- L12：This function supports only [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) in the [PMU operating mode](<../02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).

### ← returnDropWarn()
`02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.37_returnDropWarn.md`（引 1 次）

- L12：This function only supports [DC Scale XPS256 card](<../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md>) in the [PMU operating mode](<../02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md>).

## 4. 出边 30 个（它引谁）

- [[Hardware view]] → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md`（Hardware view）
- [[Profiling]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.03.05_XPS256_profiling.md`（XPS256 profiling）
- [[XPS256 operating modes]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.05_XPS256_operating_modes.md`（XPS256 operating modes）
- [[Check Status Flags]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.02_XPS256_status_flags.md`（XPS256 status flags）
- [[Default values]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.05_XPS256_programming_-_Default_values.md`（XPS256 programming - Default values）
- [[XPS256 programming - DPS operating mode]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md`（XPS256 programming - DPS operating mode）
- [[Check Gang Connection]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.10_XPS256_programming_-_Ganging.md`（XPS256 programming - Ganging）
- [[Load step response]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md`（XPS256 programming - Load step response）
- [[Force Sense Check]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.12_XPS256_programming_-_Kelvin_test___sense_connection_test.md`（XPS256 programming - Kelvin test / sense connection test）
- [[Pin definition]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md`（XPS256 programming - PMU operating mode）
- [[Surge Tracker]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.17_XPS256_programming_-_Surge_tracker.md`（XPS256 programming - Surge tracker）
- [[Max Voltage Drop]] → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.19_XPS256_programming_-_Voltage_drop_measurement.md`（XPS256 programming - Voltage drop measurement）
- [[Trace Function]] → `02_System_reference/02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.md`（Using the Trace Function）
- [[DCCH]] → `02_System_reference/02.06_Command_Reference/02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md`（DCCH - (DC Current measurement High precision pmu)）
- [[DCEX]] → `02_System_reference/02.06_Command_Reference/02.06.02.02.43_DCEX_-__DC_set_EXecute.md`（DCEX - (DC set EXecute)）
- [[DCVH]] → `02_System_reference/02.06_Command_Reference/02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md`（DCVH - (DC Voltage measurement High precision pmu)）
- [[SPMU_PIN_TASK.mode()]] → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md`（SPMU_PIN_TASK.mode()）
- [[preCharge]] → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.26_SPMU_PIN_TASK.preCharge.md`（SPMU_PIN_TASK.preCharge()）
- [[relay()]] → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.28_SPMU_PIN_TASK.relay.md`（SPMU_PIN_TASK.relay()）
- [[SPMU_PIN_TASK]] → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md`（SPMU_PIN_TASK）
- [[SPMU_TASK.execMode()]] → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.02_SPMU_TASK.execMode.md`（SPMU_TASK.execMode()）
- [[SPMU_TASK]] → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md`（SPMU_TASK）
- [[DC events]] → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63_EVENT_...__DC_events_API_reference.md`（EVENT_... (DC events API reference)）
- [[RDI command]] → `02_System_reference/02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md`（Code structure with SmartRDI）
- [[iForce()]] → `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.16_iForce.md`（iForce()）
- [[vForce()]] → `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.41_vForce.md`（vForce()）
- [[Setting up DC Scale pins with SmartRDI]] → `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md`（Setting up DC Scale pins with SmartRDI）
- [[SmartRDI]] → `02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md`（SmartRDI）
- [[Digital Pins editor]] → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md`（Digital Pins editor）
- [[Minimum period / maximum frequency of the sequencer]] → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.05.01_Minimum_period___maximum_frequency_of_the_sequencer.md`（Minimum period / maximum frequency of the sequencer）

## 5. 结构段落（Procedure / Dependency / Errors …）

### 〔syntax Examples〕（L158，1710 字符）

The following examples demonstrate how to set up an XPS256 pin for a standard current measurement.

The three examples are set up in a three-step sequence of connecting the pin and applying the basic setup, measuring the requested parameter, and disconnecting in a separate task. This sequence is suitable for XPS256-specific tests, since very often more than one setup has to be applied and more than one measurement has to be carried out before the pin is disconnected again.

 These examples are available in the following sections:

- [Example 1: SmartRDI, pattern鈥慴ased programming](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_pattern-based>)

Pattern鈥慴ased programming using SmartRDI is the recommended solution that requires the least amount of code and on the other hand delivers the most stable result in terms of timing.

- [Example 2: SmartRDI, code鈥慴ased programming](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_SRDI_code-based>)

Code鈥慴ased programming using SmartRDI needs some more code and must follow the structure of the wrapped test method APIs.

- [Example 3: Test method API SPMU_TASK](<02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.md#_354253__e_TM_API_based>)

This example is based on the test method APIs and is strongly tied to the structure of the underlying commands.

The code of the three examples generates the same measurement sequence for the programmed pin. If you use the [Trace Function](<../02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.md>) to compare the code鈥慴ased SmartRDI example and the example based on the test method APIs, you will get the same output in the MCDLog file.

### 〔related Related information〕（L304，304 字符）

[XPS256 programming - DPS operating mode](<02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.md>)[XPS256 operating modes](<02.05.05.03.05_XPS256_operating_modes.md>)[Setting up DC Scale pins with SmartRDI](<../02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>)

### 〔version Functional changes〕（L308，31 字符）

- Introduced in SmarTest 7.10.1
