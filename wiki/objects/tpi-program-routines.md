---
type: object
title: TPI Program Routines
layer: L3
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09_TPI_Program_Routines.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# TPI Program Routines

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **35,631 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.01.09_TPI_Program_Routines.md>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.01.09.01_ChangeDevice.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.03_ExecMonitor.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.04_GetConnectState.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.05_GetActiveSites.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.06_GetAvailableSites.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.07_GetDevPath.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.08_GetEnabledSites.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.09_GetEQVariableFromCache.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.10_GetEQVariableValue.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.11_GetFileState.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.12_GetLoadedTestflowName.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.13_GetNumberOfSites.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.14_GetSiteInFocus.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.15_GetSiteState.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.16_GetTechPath.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.17_GetTestflowRevisionInfo.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.18_GetTmpPath.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.19_HpInit.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.20_HpTerm.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.21_HpFwTask.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.22_InsertEQVariableInCache.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.23_MonitorStatus.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.24_ReportMessage.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.25_RestoreSiteState.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.26_SetActiveSites.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.27_SetEnabledSites.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.28_SetErrorMapMode.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.29_SetSiteInFocus.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 ChangeDevice）

```
VOID ChangeDevice(
    CHAR    *device_path,
    CHAR    *device_name,
    INT32     force_change,
    INT32    *return_state);
```

Parameters
| Parameter | Description |
|---|---|
| device_path | path to device to change to (max. length: DM_MAX_DEVICE) |
| device_name | name of device to change to (max. length: DM_MAX_FILE) |
| force_change | 0 - change only if paths of actual and new device are different |
| force_change | 1 - change even if paths of actual and new device are identical |
| return_state | 0 if an error occurred |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/26580.htm`。

### Example（取自子主题 ChangeDevice）

```
#include <stdio.h>
/* List the custom header files. */
#include "tpi_c.h"
#include "ci_types.h"
#include "libcicpi.h"
int main(int argc, char* argv[])
{
     char szSysCmd[256], szDevPath[256];
     long lReturnValue, lDeviceState;
     int iExitStatus;

     #ifndef OS_LINUX
       _main();
     #endif

     HpInit();   /* attach to SmarTest process */

     /* Program Arguments:
        argv[0]=="run_supervisor"
        argv[1]=="device path"
        argv[2]=="device name"
        argv[3]=="program name"
    */

     ChangeDevice(argv[1],argv[2],FALSE,&lDeviceState);      /* Change device */

     if (lDeviceState == 1) {        /* Check for an error. */
     {
            sprintf(szDevPath,"%s/%s",argv[1],argv[2]);       /* init path */

            /* Load test program */
            DataManager(dm_testprog,dm_load,szDevPath,argv[3],0,&lDeviceState);

                   if (lDeviceState >= -1) {     /* Check for an error. */
                  lReturnValue = ExecTestProgram();     /* Execute test program. */
                  if (lReturnValue == 0) {      /* Set exit status */
                        iExitStatus = CI_CALL_PASS;

                  } else {
                       iExitStatus = CI_CALL_ERROR;
                  }

          } else {
                 iExitStatus = CI_CALL_ERROR;    /* Error, cannot run data mngr */
          }

     } else {
          iExitStatus = CI_CALL_ERROR;    /* Error, cannot change device. */
     }
     HpTerm();
     exit(iExitStatus);

}

```

### Syntax（取自子主题 DataManager）

```
VOID DataManager(
 enum dm_fid  Fid,
 enum dm_opc  Opc,
 const CHAR *Device,
 const CHAR *Fname,
 DM_FLAGS  Flags,
 INT32 *State);
```

### Parameters（取自子主题 DataManager）

### Fid (File ID)

This parameter determines the type of file to operate on.

Values for Parameter Fid
| Value | Description |
|---|---|
| dm_applicat | application data file |
| dm_applicmodel | application model file |
| dm_attrib | pin attribute setup |
| dm_bitmap | memory test - bitmap |
| dm_catr | channel attributes |
| dm_config | pin configuration setup |
| dm_dataform | data bridge command set |
| dm_emap | error map |
| dm_fam | memory test - fail memory |
| dm_hplib | prober and handler command set |
| dm_level | level setup |
| dm_procdata | execution input command set |
| dm_report | report |
| dm_set | data set |
| dm_shmoo | shmoo |
| dm_state | state list |
| dm_scan_res | scan test - results |
| dm_tdiag | timing diagram |
| dm_testflow | testflow file |
| dm_testprog | test program |
| dm_timing | timing setup |
| dm_userproc | user procedure command set |
| dm_vector | vector setup<br><br>Note Use dm_vector also to save a pattern master file.<br><br>See also the note for dm_pattern_master_file. |
| dm_wafertyp | wafer description file |
| dm_mx_analog | analog setup file |
| dm_mx_waveform | waveform file |
| dm_mx_routing | routing setup file |
| dm_pattern_master_file | pattern master file<br><br>Note Use dm_pattern_master_file only to save the updated patterns in in a new pattern master file. Using dm_pattern_master_file SmarTest does not save unchanged patterns.<br><br>To save data in existing files use dm_vector instead. |
| dm_profile | data logging profile file |
| dm_testtable | `test table`（raw: `../02.10_Data_Logging/02.10.01.08.03_Working_with_test_tables.md`） file |

### Opc (Operation)

This parameter determines the operation to be performed.

Values for Parameter Opc
| Entry | Operation |
|---|---|
| dm_load | replace current setup by file |
| dm_merge | merge a file (add additional pins) |
| dm_append | append a file (add additional vectors) |
| dm_save | save current setup to file |
| dm_print | print file |
| dm_copy_in | copy file from another device directory |
| dm_delete | delete file |
| dm_utd | return up to date status for the file specified by Fid |
| dm_optimize | create an optimized testflow |
| dm_del_optimize | delete a optimized testflow |
| dm_optimize_utd | return up to date state of the optimized testflow |
| dm_replace (obsolete) | nothing happens. |
| dm_pload | load pattern master file |
| dm_plinit | initialize pattern master file |
| Dm_blload | load one label which should be in the current loaded pattern master file |
| Dm_pldump | dump the contents of the pattern master file to a file |
| Dm_ustate | query the firmware to get the label states and then updating the pattern master file with the returned states. |
| Dm_unload | unload a library (user procedure, hplib, dataform, etc) in application model |
| Dm_labsave | save the label to a file |

### Device

Specifies the device path. The maximum length of this string is defined by DM_MAX_DEVICE.

Note The tpi_c.h header file provides the external linkage that no manual linkage via `extern "C"` is necessary. If your code uses the `extern` function, make sure that it is conform to the current signature.

Use an absolute path (as in interactive environment) or a path relative to the directory from where you will start the test flow program. Trailing slash "/" is allowed. The current device is denoted with an empty string.

For some operations, this parameter has no meaning and is ignored.

### Fname (File Name)

Specifies the name of the file. The maximum length of this string is defined by DM_MAX_FILE. Only real names are permitted (no wildcards).

Note The tpi_c.h header file provides the external linkage that no manual linkage via `extern "C"` is necessary. If your code uses the `extern` function, make sure that it is conform to the current signature.

### Flags

Specifies modifications to normal operation. A value of zero denotes normal (unmodified) operation. Flags can be bitwise OR'ed to combine several modifications.

Values for Parameter Flags
| Entry | Modification |
|---|---|
| DM_OWRT | Allows the Test Program Explorer process to overwrite an existing setup file. If the flag is not set and the save fails, the routine returns an error code to the test flow program and displays an error message in the report window. |
| DM_FORCE | Defeats the optimizing operations of the Test Program Explorer process and always downloads a setup file. |
| DM_SILENT | Defeats error messages to the report window; the Test Program Explorer process still returns an error code to the test flow program. |

### State (return state)

State reports the execution return state and can have the following values:

Values for Parameter State
| Value | Description |
|---|---|
| 1 | up-to-date for operation dm_utd |
| 0 | not up-to-date for operation dm_utd;<br><br>ok for other operations |
| < -1 | not ok (please refer to `Appendix A: Listing of Error Messages`（raw: `02.09.01.08.07.03_Appendix_A__Listing_of_Error_Messages.md`）) |

### Example（取自子主题 DataManager）

This example loads inputted test program for the device `szDevPath`.

```
DataManager(dm_testprog,dm_load,szDevPath,argv[3],0,&lDeviceState);
```

### Syntax（取自子主题 ExecMonitor）

```
VOID ExecMonitor(
 UINT16  FuncType,
 CHAR *Parameter,
 INT32 *ExecReturn);
```

### Parameters（取自子主题 ExecMonitor）

Parameters for ExecMonitor
| Parameter | Value | Description |
|---|---|---|
| FuncType | TM_CONTROL_MONITOR | Lets you program the Monitor. |
|  | TM_RESET_MONITOR_<br><br>STATUS | Lets you reset the test system Operation state displayed in the report window. After reset the state is updated with the actual Monitor state. |
|  | TM_UNLOCK_TESTER | Lets you unlock the test system. Executes Connect and Disconnect after you have locked the test system. |
| Parameter |  | A string containing the information necessary to execute the required Monitor function. |
|  | Monitor type | Specifies Monitor function (see the table below). |
|  | Monitor settings | Settings you can make when programming the Monitor (see the table below). |
| ExecReturn |  | Monitor function execution state. |
|  | TM_SUCCEED | Monitor function successfully executed. |
|  | TM_BAD_FUNC_TYPE | Incorrect function type entered. |
|  | TM_BAD_PARAM_S_<br><br>SYNTAX | Incorrect parameter string syntax used. |
|  | TM_PARAM_S_TOO_<br><br>LONG | Parameter string is too long. |
|  | TM_POLL_TIME_OUT_OF_RANGE | Entered Poll Time is out of the allowed range. |
|  | TM_SOFT_ALARM_OUT_OF_RANGE | Entered Soft Alarm is out of the allowed range. |

Monitor Type Parameters
| Parameter | Function |
|---|---|
| CalAge | Age of current calibration |
| BoardTempr | IO Board temperature |
| Diagnostic | Diagnostic finished |
| DpsCurrent | DPS forced current |

Monitor Settings Parameters
 |

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/26604.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：32 行 × 3 列，含 rowspan。

Parameter

 |

Function

 |

Values

 |
 |

<poll enable>

 |

"enable"/"disable"

 |

enable or disable the monitor

 |
 |

<poll time value>

 |

enter string to set Monitor poll time

(values depend on <poll time unit>)

 |

3.0 ... 60.0 [seconds]

 |
 |

1.0 ... 60.0 [minutes]

 |
 |

1.0 ... 24.0 [hours]

 |
 |

1.0 ... 7.0 [days]

 |
 |

1.0 ... 4.0 [weeks]

 |
 |

1.0 ... 12.0 [months]

 |
 |

1.0 [year]

 |
 |

<poll time unit>

 |

set unit of Monitor poll time

 |

"second(s)"

 |
 |

"minute(s)"

 |
 |

"hour(s)"

 |
 |

"day(s)"

 |
 |

"week(s)"

 |
 |

"month(s)"

 |
 |

"year(s)"

 |
 |

<high soft alarm value>

 |

set limit for "CalAge"

 |

time since last cal; range is 0.0 ... 7884000.0 seconds (1/4 year)

 |
 |

set limit for "BoardTempr"

 |

positive temp. delta in range 0.0 ... (2.5 - max cal. temp. delta/2) [C]

 |
 |

set limit for "DpsCurrent"

 |

% value of programmed current limits of all DPSs in range 0.0 ... 1.0

 |
 |

<low soft alarm value>

 |

set limit for "BoardTempr"

 |

negative temp. delta in range

(-2.5 + max cal. temp. delta/2) ... 0.0 [C]

 |
 |

<soft alarm unit>

 |

set unit of soft alarm limit for "CalAge"

 |

"second(s)"

 |
 |

"minute(s)"

 |
 |

"hour(s)"

 |
 |

"day(s)"

 |
 |

"week(s)"

 |
 |

"month(s)"

 |
 |

"year(s)"

 |
 |

set unit of soft alarm limit for "BoardTempr"

 |

"C" (celsius)

 |
 |

"K" (kelvin)

 |
 |

"F" (fahrnheit)

 |
 |

set unit of soft alarm limit for "DpsCurrent"

 |

"A" (Ampere)

 |
 |

<lock tester enable>

 |

set "lock_enable" / "lock_disable" (used for DPS Current only)

 |

"lock_enable" or " lock_disable"

 |

### Example（取自子主题 ExecMonitor）

```
INT32 ExecReturn;

ExecMonitor(TM_RESET_STATUS,"",&ExecReturn);
ExecMonitor(TM_CONTROL_MONITOR,"CalAge;enable;\
           1;day(s);4.0;month(s)", &ExecReturn);
ExecMonitor(TM_CONTROL_MONITOR,"BoardTempr;enable;\
 2.0;-2.0;C",&ExecReturn);
ExecMonitor(TM_CONTROL_MONITOR,"DpsCurrent; \
            enable;10.0;second(s);0.8;A;\
            lock_enable",&ExecReturn);
```

### Syntax（取自子主题 GetConnectState）

```
VOID GetConnectState(
    INT32    *is_connected);
```

### Parameters（取自子主题 GetConnectState）

The output parameter is_connected is set to

- FALSE if the device is actually disconnected
- TRUE if the device is actually connected

### Example（取自子主题 GetConnectState）

```
INT32 isConnected;
GetNumberOfSites(&isConnected);
```

### Syntax（取自子主题 GetActiveSites）

```
VOID GetActiveSites(MS_SITE_SET active_set);
```

### Parameters（取自子主题 GetActiveSites）

|

Parameter

 |

Description

 |
 |

active_set

 |

A character array containing whether each site is activated or not. It is in the type of `MS_SITE_SET`.

- If active_set[i] is not 0, site i is activated.
- If active_set[i] is 0, site i is deactivated.

MS_SITE_SET is a character array with the length `MS_MAX_SITES+1`. It is used to access the status of all configured sites. Its element contains the status of the corresponding site.

If you define the variable siteSet of type MS_SITE_SET, siteSet[i] will be used to contain the status of site i.

The data type is defined as below:

`typedef char MS_SITE_SET[MS_MAX_SITES+1];`

MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher versions:

- For 64-bit system: 1024
- For 32-bit system: 128

MS_MAX_SITES is defined as follows for older versions of SmarTest:

- For 64-bit system: 256
- For 32-bit system: 128

   | Note Note that 0 is not a valid site number.

### Example（取自子主题 GetActiveSites）

```
MS_SITE_SET active_sites;
GetActiveSites(active_sites);
```

### Syntax（取自子主题 GetAvailableSites）

`void GetAvailableSites(MS_SITE_SET available_set);`

### Parameters（取自子主题 GetAvailableSites）

|

Parameter

 |

Description

 |
 |

available_set

 |

A character array containing whether each site is available or not. It is in the type of `MS_SITE_SET`.

- If available_set[i] is not 0, site i is available.
- If available_set[i] is 0, site i is not available.

MS_SITE_SET is a character array with the length `MS_MAX_SITES+1`. It is used to access the status of all configured sites. Its element contains the status of the corresponding site.

If you define the variable siteSet of type MS_SITE_SET, siteSet[i] will be used to contain the status of site i.

The data type is defined as below:

`typedef char MS_SITE_SET[MS_MAX_SITES+1];`

MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher versions:

- For 64-bit system: 1024
- For 32-bit system: 128

MS_MAX_SITES is defined as follows for older versions of SmarTest:

- For 64-bit system: 256
- For 32-bit system: 128

   | Note Site counting starts from 1 and 0 is not a valid site number.

### Example（取自子主题 GetAvailableSites）

```
MS_SITE_SET available_sites;
GetAvailableSites(available_sites);
```

### Syntax（取自子主题 GetDevPath）

```
VOID GetDevPath(
    CHAR    *dev_path_p);
```

### Parameters（取自子主题 GetDevPath）

On return the character array dev_path contains the actual device path. The array should be defined of length DM_MAX_DEVICE.

### Example（取自子主题 GetDevPath）

```
char device_path[DM_MAX_DEVICE];
GetDevPath(device_path);
strcat (device_path, "/report/pll.csv");
cout << "path is " << device_path << endl;
```

### Syntax（取自子主题 GetEnabledSites）

```
VOID GetEnabledSites(MS_SITE_SET enabled_set);
```

### Parameters（取自子主题 GetEnabledSites）

|

Parameter

 |

Description

 |
 |

enabled_set

 |

A character array containing whether each site is enabled or not. It is in the type of `MS_SITE_SET`.

- If enabled_set[i] is 1, site i is enabled.
- If enabled_set[i] is 0, site i is disabled.

MS_SITE_SET is a character array with the length `MS_MAX_SITES+1`. It is used to access the status of all configured sites. Its element contains the status of the corresponding site.

If you define the variable siteSet of type MS_SITE_SET, siteSet[i] will be used to contain the status of site i.

The data type is defined as below:

`typedef char MS_SITE_SET[MS_MAX_SITES+1];`

MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher versions:

- For 64-bit system: 1024
- For 32-bit system: 128

MS_MAX_SITES is defined as follows for older versions of SmarTest:

- For 64-bit system: 256
- For 32-bit system: 128

   | Note Note that site counting starts from 1 and 0 is not a valid site number.

### Example（取自子主题 GetEnabledSites）

```
MS_SITE_SET enabled_sites;

GetEnabledSites(enabled_sites);
```

### Syntax（取自子主题 GetEQVariableFromCache）

```
VOID GetEQVariableFromCache(
    INT32      equation_system,
    INT32      equation_set,
    INT32      spec_set,
    INT32      site_number,
    CHAR     *variable_name,
    FLOAT64     *value,
    INT32     *return_state);
```

### Parameters（取自子主题 GetEQVariableFromCache）

Parameters of GetEQVariableFromCache
| Parameter | Description | Range |
|---|---|---|
| equation_system | type of equation system | TIMING_EQ_SYSTEM or LEVEL_EQ_SYSTEM |
| equation_set | equation set number | 1 ... 99 |
| spec_set | spec set number | 1 ... 99 |
| site_number | number of appropriate site | 1 ... MS_MAX_SITES |
| variable_name | name of equation variable | null-terminated string |
| value | on return: actual value of variable |  |
| return_state | execution return state | 0 if successful |

### Example（取自子主题 GetEQVariableFromCache）

```
FLOAT64 variable_value;
INT32 re_state;
GetEQVariableFromCache(TIMING_EQ_SYSTEM,2,1,2,"var1",&variable_value,&re_state);
```

### Syntax（取自子主题 GetEQVariableValue）

```
VOID GetEQVariableValue(
    INT32      equation_system,
    INT32      equation_set,
    INT32      spec_set,
    INT32      site_number,
    CHAR     *variable_name,
    FLOAT64     *value,
    INT32     *return_state);
```

### Parameters（取自子主题 GetEQVariableValue）

Parameters of GetEQVariableValue
| Parameter | Description | Range |
|---|---|---|
| equation_system | type of equation system | TIMING_EQ_SYSTEM or LEVEL_EQ_SYSTEM |
| equation_set | equation set number | 1 ... 99 |
| spec_set | spec set number | 1 ... 99 |
| site_number | number of appropriate site | 1 ... MS_MAX_SITES |
| variable_name | name of equation variable | null-terminated string |
| value | on return: actual value of variable |  |
| return_state | execution return state | 0 if successful |

### Example（取自子主题 GetEQVariableValue）

```
FLOAT64 variable_value;
INT32 re_state;
GetEQVariableValue(TIMING_EQ_SYSTEM,2,1,2,"var1",&variable_value,&re_state);
```

### Syntax（取自子主题 GetFileState）

```
VOID GetFileState(
    enum dm_fid      fid;
    struct dm_file_state     *file_state;
    INT32     *ret_state;);
```

### Example（取自子主题 GetFileState）

```
#include "/opt/hp93000/soc/pws/lib/tpi_c.h"
virtual void run()
{
...
ON_FIRST_INVOCATION_BEGIN();

{
struct dm_file_state file_state;
int ret_state;
GetFileState(dm_testflow, &file_state, &ret_state);
cout<< "My Test Flow file name is " << file_state.name << endl;
GetFileState(dm_config, &file_state, &ret_state);
cout<< "My Pin Config file name is " << file_state.name << endl;
GetFileState(dm_pattern_master_file, &file_state, &ret_state);
cout<< "My Pattern Master File name is " << file_state.name << endl;
GetFileState(dm_testtable, &file_state, &ret_state);
cout<< "My Test Table File name is " << file_state.name << endl;
}

ON_FIRST_INVOCATION_END();
...
return;
} //virtual void run()
```

### Syntax（取自子主题 GetLoadedTestflowName）

```
const CHAR *GetLoadedTestflowName();
```

### Return value（取自子主题 GetLoadedTestflowName）

The maximum length of the returned testflow name is defined by DM_MAX_FILE. The returned pointer cannot be freed.

### Example（取自子主题 GetLoadedTestflowName）

```
CHAR *testflowName = NULL;
testflowName = GetLoadedTestflowName();
cout << "Loaded testflow is" << testflowName << endl;
```

### Syntax（取自子主题 GetNumberOfSites）

```
VOID GetNumberOfSites(
    INT32     *number_of_sites);
```

### Parameters（取自子主题 GetNumberOfSites）

On return, number_of_sites specifies the number sites currently configured.

### Example（取自子主题 GetNumberOfSites）

```
INT32 MaxSitesEnabled;
GetNumberOfSites(&MaxSitesEnabled);
```

### Syntax（取自子主题 GetSiteInFocus）

```
VOID GetSiteInFocus(
    INT32     *site_in_focus);
```

### Parameters（取自子主题 GetSiteInFocus）

Note Another focus exists besides the query focus: the setup focus.

On return, site_in_focus specifies the number of the site that currently has the query focus.

### Example（取自子主题 GetSiteInFocus）

```
INT32 focus_site;
GetSiteInFocus(&focus_site);
```

### Syntax（取自子主题 GetSiteState）

```
VOID GetSiteState (
    MS_SITE_STATE *site_state);
```

### Parameters（取自子主题 GetSiteState）

site_state points to a structure of type MS_SITE_STATE containing information on the number of sites and on the sites currently enabled, active, and in focus.

### Example（取自子主题 GetSiteState）

```
MS_SITE_STATE site_state;
GetSiteState(&site_state);
```

### Syntax（取自子主题 GetTechPath）

```
VOID GetTechPath (
    CHAR     *tech_path);
```

### Parameters（取自子主题 GetTechPath）

On return the character array tech_path contains the actual technology path. The array should be defined of length DM_MAX_DEVICE.

### Example（取自子主题 GetTechPath）

```
CHAR tech_path[DM_MAX_DEVICE];
GetTechPath(tech_path);
cout << "path is " << tech_path << endl;
```

### Syntax（取自子主题 GetTestflowRevisionInfo）

```
int GetTestflowRevisionInfo(const CHAR *testflow, TESTFLOW_REVISION_INFO *revision_info);
```

Parameters
| Parameter | Description |
|---|---|
| testflow | A non-null string which indicates the full path of the testflow file. |
| revision_info | A pointer to the TESTFLOW_REVISION_INFO structure which holds the following information:<br><br>CHAR description[TESTFLOW_REVISION_LEN]: The value of the description attribute defined in the testflow.<br><br>CHAR device_name[TESTFLOW_REVISION_LEN]: The value of the device_name attribute defined in the testflow.<br><br>CHAR device_revision[TESTFLOW_REVISION_LEN]: The value of the device_revision attribute defined in the testflow.<br><br>CHAR test_revision[TESTFLOW_REVISION_LEN]: The value of the test_revision attribute defined in the testflow. |

### Return value（取自子主题 GetTestflowRevisionInfo）

If the function is executed successfully, it returns 0. Otherwise, it returns -1.

### Example（取自子主题 GetTestflowRevisionInfo）

```
TESTFLOW_REVISION_INFO testflowInfo;
int retValue = 0;
retValue = GetTestflowRevisionInfo("/home/device_demo/testflow/demo.tf", &testflowInfo);
```

### Syntax（取自子主题 GetTmpPath）

```
VOID GetTmpPath(CHAR *tmp_path_p);
```

### Parameters（取自子主题 GetTmpPath）

It returns the character array containing the actual temporary path. The array should be defined of length SA_TMP_PATH_LENGTH (defined in the header file /opt/hp93000/soc/com/include/sa_prc.h).

### Example（取自子主题 GetTmpPath）

```
char tmp_path[SA_TMP_PATH_LENGTH];
GetTmpPath(tmp_path);
cout << "path is " << tmp_path << endl;
```

### Syntax（取自子主题 HpInit）

```
VOID HpInit()
```

### Parameters（取自子主题 HpInit）

None

### Example（取自子主题 HpInit）

```
#include <stdio.h>
/* List the custom header files. */
#include "tpi_c.h"
#include "ci_types.h"
#include "libcicpi.h"
int main(int argc, char* argv[])
{
     char szSysCmd[256], szDevPath[256];
     long lReturnValue, lDeviceState;
     int iExitStatus;

     #ifndef OS_LINUX
       _main();
     #endif

     HpInit();   /* attach to SmarTest process */

     /* Program Arguments:
        argv[0]=="run_supervisor"
        argv[1]=="device path"
        argv[2]=="device name"
        argv[3]=="program name"
    */

     ChangeDevice(argv[1],argv[2],FALSE,&lDeviceState);      /* Change device */

     if (lDeviceState == 1) {        /* Check for an error. */
     {
            sprintf(szDevPath,"%s/%s",argv[1],argv[2]);       /* init path */

            /* Load test program */
            DataManager(dm_testprog,dm_load,szDevPath,argv[3],0,&lDeviceState);

                   if (lDeviceState >= -1) {     /* Check for an error. */
                  lReturnValue = ExecTestProgram();     /* Execute test program. */
                  if (lReturnValue == 0) {      /* Set exit status */
                        iExitStatus = CI_CALL_PASS;

                  } else {
                       iExitStatus = CI_CALL_ERROR;
                  }

          } else {
                 iExitStatus = CI_CALL_ERROR;    /* Error, cannot run data mngr */
          }

     } else {
          iExitStatus = CI_CALL_ERROR;    /* Error, cannot change device. */
     }
     HpTerm();
     exit(iExitStatus);

}

```

### Syntax（取自子主题 HpTerm）

```
VOID HpTerm()
```

### Parameters（取自子主题 HpTerm）

None

### Example（取自子主题 HpTerm）

```
#include <stdio.h>
/* List the custom header files. */
#include "tpi_c.h"
#include "ci_types.h"
#include "libcicpi.h"
int main(int argc, char* argv[])
{
     char szSysCmd[256], szDevPath[256];
     long lReturnValue, lDeviceState;
     int iExitStatus;

     #ifndef OS_LINUX
       _main();
     #endif

     HpInit();   /* attach to SmarTest process */

     /* Program Arguments:
        argv[0]=="run_supervisor"
        argv[1]=="device path"
        argv[2]=="device name"
        argv[3]=="program name"
    */

     ChangeDevice(argv[1],argv[2],FALSE,&lDeviceState);      /* Change device */

     if (lDeviceState == 1) {        /* Check for an error. */
     {
            sprintf(szDevPath,"%s/%s",argv[1],argv[2]);       /* init path */

            /* Load test program */
            DataManager(dm_testprog,dm_load,szDevPath,argv[3],0,&lDeviceState);

                   if (lDeviceState >= -1) {     /* Check for an error. */
                  lReturnValue = ExecTestProgram();     /* Execute test program. */
                  if (lReturnValue == 0) {      /* Set exit status */
                        iExitStatus = CI_CALL_PASS;

                  } else {
                       iExitStatus = CI_CALL_ERROR;
                  }

          } else {
                 iExitStatus = CI_CALL_ERROR;    /* Error, cannot run data mngr */
          }

     } else {
          iExitStatus = CI_CALL_ERROR;    /* Error, cannot change device. */
     }
     HpTerm();
     exit(iExitStatus);

}

```

### Syntax（取自子主题 HpFwTask）

```
VOID HpFwTask(
    CHAR    *task_str,
    INT32    *task_len,
    CHAR    *answ_str,
    INT32    *answ_len,
    INT32    *ret_state);
```

### Parameters（取自子主题 HpFwTask）

Parameters for HpFwTask
| Parameter | Value |
|---|---|
| task_str | Command string with one or more commands, each limited by a newline (\n) or by a semicolon. It is an input parameter. |
| task_len | Length of the command string. It is an input parameter. |
| answ_str | Answer string. This is an output parameter. |
| answ_len | As an input parameter: the dimensioned size of the answer string. As an output parameter: the length of the answer string. |
| ret_state | Status (see `Appendix A: Listing of Error Messages`（raw: `02.09.01.08.07.03_Appendix_A__Listing_of_Error_Messages.md`）). This is an output parameter. |

In order to optimize data transfer times, the size of the answer string should be determined in relation to the amount of data to be passed.

Note The SmarTest software allows you to execute firmware commands directly from a terminal. The utility that does this is called hpt and is described in the `Command Reference`（raw: `../02.06_Command_Reference/02.06_Command_Reference.md`）. To use hpt the SmarTest software environment must be running.

### Example（取自子主题 HpFwTask）

The following listing shows an example of how to build the command string for HpFwTask and how to retrieve results from the answer string.

```
#define FW_TASK_BUF_LEN   1000
#define FW_ANSW_BUF_LEN   1000

 CHAR     TaskBuffer[FW_TASK_BUF_LEN + 1];
 CHAR     *Task;
 INT32    TaskLength;
 CHAR     AnswerBuffer[FW_ANSW_BUF_LEN + 1];
 INT32    AnswerLength;
 INT32    ReturnState;
 double   MeasurementValue;

   /* create and execute the fw-string for */
   /* pmu setup and measurement            */
   Task  = TaskBuffer;
   Task += sprintf(Task,"DFCM %d,%f,%f,%f,%f,%f,%f,%s,(%s);",1,  /* DC set number */
           800.0,        /* force voltage [mA] */
           200000.0,     /* clamp current in [uA] */
           0, 200000.0,  /* PASS/ FAIL treshold */
           800.0,        /* precharge voltage */
           1.0,          /* setling time in [ms] */
           "NTERM",      /* termination mode */
           "CP");        /* pin to measure */
    Task += sprintf(Task, "PTST? %d,%s,%s\n",
           1,      /* DC set number */
           "NONE", /* pre action: NO */
           "CVAL"); /* mode: value with Rs comp. */

  TaskLength   = Task - TaskBuffer;
  AnswerLength = FW_ANSW_BUF_LEN;
  HpFwTask(TaskBuffer, &TaskLength, AnswerBuffer, &AnswerLength, &ReturnState);
  AnswerBuffer[AnswerLength] = EOS;  /* truncation of AnswerBuffer string */

   if(ReturnState==0) {
    /* extract the pmu valid code and the measured current */
    /* example answer: PTST 1,3,9697.204,(CP) */
    /* PTST returns the measured current in 'uA' */
     sscanf(AnswerBuffer, "PTST 1,%d,%lf,", &ValidCode,
     &MeasurementValue);

    /* the measured value is now accessible in    */
    /* 'MeasurementValue' for further processing */
    } else {
      /**** HpFwTask ERROR ****/
   }
```

### Syntax（取自子主题 InsertEQVariableInCache）

```
VOID InsertEQVariableInCache(
    INT32      equation_system;
    INT32      equation_set;
    INT32      spec_set;
    CHAR     *variable_name;
    INT32     *return_state)
```

### Parameters（取自子主题 InsertEQVariableInCache）

Parameters of InsertEQVariableInCache
| Parameter | Description | Range |
|---|---|---|
| equation_system | type of equation system | TIMING_EQ_SYSTEM or LEVEL_EQ_SYSTEM |
| equation_set | equation set number | 1 ... 99 |
| spec_set | spec set number | 1 ... 99 |
| variable_name | name of equation variable | null-terminated string |
| return_state | execution return state | 0 if successful |

### Example（取自子主题 InsertEQVariableInCache）

```
INT32 re_state;
InsertEQVariableInCache(TIMING_EQ_SYSTEM, 1, 1, "tim_var",&re_state);
```

### Syntax（取自子主题 MonitorStatus）

```
VOID MonitorStatus(
    UINT16    *TstrOpState_p,
    UINT16    *StatusReg_p);
```

### Parameters（取自子主题 MonitorStatus）

Values for Parameter TstrOpState_p
| Parameter | Value | Description |
|---|---|---|
| TstrOpState_p | TM_GREEN_STATE | test system operation is "In Spec"; at least one monitor function is "In Spec" while the others are not being monitored (DISABLED). |
| TstrOpState_p | TM_YELLOW_STATE | test system operation is "In Spec" (WARNING); at least one monitor function is "In Spec" (WARNING) while the others are not being monitored (DISABLED). |
| TstrOpState_p | TM_RED_STATE | test system operation is "Out of Spec" (ALARM); at least one monitor function is "Out of Spec" (ALARM) while the others are "In Spec", "In Spec" (WARNING), or not being monitored (DISABLED). |
| TstrOpState_p | TM_DISABLED_STATE | test system operation is not monitored. All monitor functions are DISABLED. |
| TstrOpState_p | TM_OFFLINE_STATE | test system operation is not monitored, system software was started in OFFLINE mode. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/26690.htm`。

Values for Parameter StatusReg_p
| Parameter | Description | Value |
|---|---|---|
| StatusReg_p |  |  |
| bits 0, 1: | Age of Calibration | 00 = test system Oper. In Spec |
| bits 0, 1: | Age of Calibration | 01 = test system Oper. In Spec (WARNING) |
| bits 0, 1: | Age of Calibration | 10 = test system Oper. Out of Spec (ALARM) |
| bits 0, 1: | Age of Calibration | 11 = test system Oper. Not Monitored |
| bits 0, 1: | Age of Calibration |  |
| bits 2, 3: | Timing and Level Accuracy | 00 = test system Oper. In Spec |
| bits 2, 3: | Timing and Level Accuracy | 01 = test system Oper. In Spec (WARNING) |
| bits 2, 3: | Timing and Level Accuracy | 10 = test system Oper. Out of Spec (ALARM) |
| bits 2, 3: | Timing and Level Accuracy | 11 = test system Oper. Not Monitored |
| bits 2, 3: | Timing and Level Accuracy |  |
| bits 4, 5: | Diagnostic Done | 00 = test system Oper. In Spec |
| bits 4, 5: | Diagnostic Done | 01 = test system Oper. In Spec (WARNING) |
| bits 4, 5: | Diagnostic Done | 10 = test system Oper. Out of Spec (ALARM) |
| bits 4, 5: | Diagnostic Done | 11 = test system Oper. Not Monitored |
| bits 6, 7: | unused |  |
| bits 8, 9: | DPS Force Current | 00 = test system Oper. In Spec |
| bits 8, 9: | DPS Force Current | 01 = test system Oper. In Spec (WARNING) |
| bits 8, 9: | DPS Force Current | 10 = test system Oper. Out of Spec (ALARM) |
| bits 8, 9: | DPS Force Current | 11 = test system Oper. Not Monitored |
| bits 10 ... 15: | unused |  |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/26690.htm`。

### Example（取自子主题 MonitorStatus）

```
UINT16 TstrOpState, StatusReg;

MonitorStatus(&TstrOpState, &StatusReg);
```

### Syntax（取自子主题 ReportMessage）

```
VOID ReportMessage (
    INT32      type,
    CHAR     *message);
```

### Parameters（取自子主题 ReportMessage）

Parameters of ReportMessage
| Parameter | Description | Range |
|---|---|---|
| type | type of message to be printed | UI_MESSAGE, UI_WARNING, UI_ERROR, UI_FATAL |
| message | message to be printed | null-terminated string |

The actual display depends on the type of message:

- Messages are printed as they come.
- For warnings the message text is preceded with Warning: .
- For errors the message text is preceded with Error: .
- For fatals the message text is preceded with:

Fatal ['<file_name>' # '<line_number>']:

and followed by:

System errno: '<system error text>'.

After a fatal message a core is created and the software is shut down.

### Example（取自子主题 ReportMessage）

This code shows an example for how to use ReportMessage to display a fatal error message.

The executable is named my_prog. It tries to open the file not_there that does not exist. Therefore the external variable errno is set to ENONET (no such file or directory).

fdes = open("not_there",O_RDONLY);

ReportMessage(UI_FATAL, "This is a Fatal");

The following message will be printed in the report window:

Fatal [my_prog tpi_sa.c #1143]:

This is a Fatal

System errno: No such file or directory

After this message the SmarTest software will shut down.

### Syntax（取自子主题 RestoreSiteState）

```
VOID RestoreSiteState(
MS_SITE_STATE     *site_state,
INT32     *return_state);
```

### Parameters（取自子主题 RestoreSiteState）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/26705.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。

Parameters for RestoreSiteState
 |

Parameter

 |

Description

 |
 |

site_state

 |

Points to a structure of type MS_SITE_STATE containing information on the number of sites and on the sites currently enabled, active, and in focus. This structure usually is filled by a call to `GetSiteState`（raw: `02.09.01.09.15_GetSiteState.md`）.

 |
 |

return_state

 |

Status is set to 0 if execution was ok. Otherwise the site state could not be restored because the number of sites before and after restoring did not match.

   | Note To change site states use `SetActiveSites`（raw: `02.09.01.09.26_SetActiveSites.md`）, `SetEnabledSites`（raw: `02.09.01.09.27_SetEnabledSites.md`） and `SetSiteInFocus`（raw: `02.09.01.09.29_SetSiteInFocus.md`）.

### Example（取自子主题 RestoreSiteState）

```
MS_SITE_STATE site_state;
INT32 re_state;
GetSiteState(&site_state);
...
RestoreSiteState(&site_state, &re_state);
```

### Syntax（取自子主题 SetActiveSites）

```
VOID SetActiveSites(MS_SITE_SET active_set,
                    INT32      *return_state);
```

### Parameters（取自子主题 SetActiveSites）

|

Parameter

 |

Description

 |
 |

active_set

 |

A character array containing whether each site is activated or not. It is in the type of `MS_SITE_SET`.

- If active_set[i] is not 0, site i is activated.
- If active_set[i] is 0, site i is deactivated.

MS_SITE_SET is a character array with the length `MS_MAX_SITES+1`. It is used to access the status of all configured sites. Its element contains the status of the corresponding site.

If you define the variable siteSet of type MS_SITE_SET, siteSet[i] will be used to contain the status of site i.

The data type is defined as below:

`typedef char MS_SITE_SET[MS_MAX_SITES+1];`

MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher versions:

  - For 64-bit system: 1024
  - For 32-bit system: 128

MS_MAX_SITES is defined as follows for older versions of SmarTest:

  - For 64-bit system: 256
  - For 32-bit system: 128

 |
 |

return_state

 |

Status is set to 0 if execution was ok. Otherwise an error occurred.

   | Note You should not activate more sites than are currently configured. Site counting starts from 1 and 0 is not a valid site number.

### Example（取自子主题 SetActiveSites）

```
INT32       re_state;
MS_SITE_SET active_sites;

active_sites[1] = 1;
active_sites[2] = 0;
active_sites[3] = 1;
active_sites[4] = 0;

SetActiveSites(active_sites,&re_state);
```

### Syntax（取自子主题 SetEnabledSites）

```
VOID SetEnabledSites(MS_SITE_SET enabled_set;
                     INT32       *return_state;
```

### Parameters（取自子主题 SetEnabledSites）

|

Parameter

 |

Description

 |
 |

enabled_set

 |

A character array containing whether each site is enabled or not. It is in the type of `MS_SITE_SET`.

- If enabled_set[i] is not 0, site i is enabled.
- If enabled_set[i] is 0, site i is disabled.

MS_SITE_SET is a character array with the length `MS_MAX_SITES+1`. It is used to access the status of all configured sites. Its element contains the status of the corresponding site.

If you define the variable siteSet of type MS_SITE_SET, siteSet[i] will be used to contain the status of site i.

The data type is defined as below:

`typedef char MS_SITE_SET[MS_MAX_SITES+1];`

MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher versions:

  - For 64-bit system: 1024
  - For 32-bit system: 128

MS_MAX_SITES is defined as follows for older versions of SmarTest:

  - For 64-bit system: 256
  - For 32-bit system: 128

 |
 |

return_state

 |

Status is set to 0 if execution was ok. Otherwise an error occurred

   | Note You should not enable more sites than are currently configured. Site counting starts from 1 and 0 is not a valid site number.

### Example（取自子主题 SetEnabledSites）

```
include"/opt/hp93000/soc/pws/lib/tpi_c.h"
...
...
...

INT32       re_state;
MS_SITE_SET enabled_sites;

enabled_sites[1] = 1;
enabled_sites[2] = 0;
enabled_sites[3] = 1;
enabled_sites[4] = 0;

SetEnabledSites(enabled_sites,&re_state);
```

### Syntax（取自子主题 SetErrorMapMode）

```
VOID SetErrorMapMode(
    INT32     mode);
```

### Parameters（取自子主题 SetErrorMapMode）

The mode variable supports two values:

- ERROR_MAP_FAILURE_ORIENTED to set the error map to failure oriented mode (only failed cycles are logged in the error map).
- ERROR_MAP_CYCLE_ORIENTED to set the error map to cycle oriented mode (all cycles are logged in the error map).

### Example（取自子主题 SetErrorMapMode）

```
SetErrorMapMode(ERROR_MAP_FAILURE_ORIENTED);
```

### Syntax（取自子主题 SetSiteInFocus）

```
VOID SetSiteInFocus(
    INT32      site_in_focus,
    INT32     *return_state);
```

### Parameters（取自子主题 SetSiteInFocus）

Parameters for SetSiteInFocus
| Parameter | Description |
|---|---|
| site_in_focus | Specifies the number of the site to be focused. |
| return_state | Status is set to 0 if execution was ok. Otherwise an error occurred. |

### Example（取自子主题 SetSiteInFocus）

```
INT32 re_state;
SetSiteInFocus(2, &re_state);
```

<!-- 语法节 end -->

## 是什么

> **一句话**：**外部客户端程序里能直接调的那批 C 例程**。原文自述
> *"reference information on all C routines available for writing test flow programs"*。
> 全章 **31 篇** = **29 个例程 + 1 篇附录 + 本页的定义文档**。
>
> **「test flow programs」这个词组是原文的说法，但它指的是「你写的那个客户端程序」
> ——不是「testflow 里的东西」（那是 L2 的地盘）。**判据见「出处」：原文自己的例子是
> `main()` + `HpInit(); /* attach to SmarTest process */` + `argv[0]=="run_supervisor"`。
> **同一章用词宽松，实证在例子里。**

**它是「平铺的函数集合」，不是「对象模型」。** 与 [[test-suite-control-api]] 的用法正相反：
那边要先 `initializeSession()` 再拿到一个 `TestsuiteProxy` 句柄、方法挂在句柄上；
这边是**直接调函数**——`HpInit()`、`GetSiteInFocus()`、`DataManager()`、`MonitorStatus()`。

**必须先 include 头文件**（附录原文）：

> The definitions of all symbolic constants, function declarations and structures that you are
> likely to need for your SmarTest test flow programs are contained in the include file
> `/opt/hp93000/soc/pws/lib/tpi_c.h`.

```c
#include "/opt/hp93000/soc/pws/lib/tpi_c.h"
```

**常量不够用没有第二出口**：原文说 *"If you require extra constants that have not been defined
in this include file, you have to define them yourself in the 'defines' area of your program."*
——**自己定义**，文档不提供别的头文件。

### 文档自己按功能分了 10 组（**这 10 组是照抄的，不是我的归纳**）

下表分组名与成员**逐条照抄定义文档的 overview 段**。例程名写成反引号而**不是链接**——
**本 wiki 一个例程都没单独建页**（理由见「和谁有关」）。
它们的**签名、参数、返回值、示例**都在本页上面的 `## 语法 / 参数` 里：
**29 个例程的 `## Syntax` 已逐字抽进来**，出处写在每个小节的标题里。

| 功能组（原文） | 例程 |
|---|---|
| Initializing and Terminating the Test Flow | `HpInit`、`HpTerm` |
| Managing Data Files | `DataManager` |
| Setting the Error Map Mode | `SetErrorMapMode` |
| Accessing Equation Variables | `InsertEQVariableInCache`、`GetEQVariableFromCache`、`GetEQVariableValue` |
| Executing Firmware Commands | `HpFwTask` |
| Printing Messages to the report window | `ReportMessage` |
| Changing the Device | `ChangeDevice`、`GetDevPath`、`GetTechPath`、`GetFileState` |
| Determining the Connect State | `GetConnectState` |
| Controlling Multiple Sites | `GetNumberOfSites`、`GetSiteInFocus`、`SetSiteInFocus`、`GetEnabledSites`、`GetAvailableSites`、`SetEnabledSites`、`GetActiveSites`、`SetActiveSites`、`GetSiteState`、`RestoreSiteState` |
| Checking Test System Status with the Monitor | `MonitorStatus`、`ExecMonitor` |

> ⚠️ **这 10 组没收全 29 个例程，差 3 个**（`Subtopics` 里声明了、但 overview 一个组都没收）：
> **`GetLoadedTestflowName`、`GetTestflowRevisionInfo`、`GetTmpPath`**。
> **这是文档自己的缺口，不是我漏抄**——三者的名字都不像属于任何一组
> （前两个是 testflow 名与版本查询，第三个是临时目录），原文没给它们归类。
> 本页**不给它们编组**：分类是判断，原文没做，我不替它做。

### 数据文件这一支要单独看一眼

`DataManager` 的文件标识（`dm_config`、`dm_level`、`dm_timing`、`dm_vector`、`dm_testflow`、
`dm_emap`…）**几乎一一对应九个 stage 各自的产物文件**——
这是 `02.09.01.09` 与九个 stage 之间最实在的一条接线，也是 [[project]] 页
「程序侧的产物文件接口」那一节的依据。

## 典型用法

**用法分两步：先 include（见上），再在外部客户端程序里直接调。**

### 本页**有**一份完整可运行的程序（就在上面语法节里）

原文在 **3 个例程**的 `## Example` 里**重复给了同一份完整程序**
（`ChangeDevice`、`HpInit`、`HpTerm` 三篇各一份，逐字相同），
**已随语法节逐字抽进本页**（语法节里搜 `int main` 有 3 处，是同一份）。

> **这段要改口**：本页初稿写的是「本页不提供完整可跑的例子」——**那句是假的**，
> 是我没读语法节就下的断言。**先量再说**，这条又栽一次。

它是**外部客户端程序**的骨架，**与 [[test-suite-control-api]] 的三个例子同形**。
**完整那段 `main()` 在上面语法节的 `### Example（取自子主题 ChangeDevice）` 里，逐字取自原文**（§4）——
**这里不再抄第二遍。**

> **为什么删掉了原来那第二份。** 本页初稿在这里放过一份「精简版」，
> 转录时把原文 `/* Program Arguments:` 底下三行 `argv[1]` / `argv[2]` / `argv[3]`
> **并成了两行**，又漏了 `/* Program Arguments:` 那一行——
> **同一段原文在一个页里存两份，就一定有一份会漂。** 第七类复核（引用块逐字回查语料）把它照了出来。
> **要看例子去语法节看那一份；这一节只讲它说明了什么。**

调用次序是：`HpInit()` 挂上 SmarTest 进程 → `ChangeDevice()` 换设备 →
`sprintf()` 拼出 `device path / device name` → `DataManager()` 装载 test program →
`ExecTestProgram()` 执行 → `HpTerm()` 收尾。

**三点，读者照着这段走之前要知道：**

1. **它是 `main()`，跑在外部进程里**（`argv[0]=="run_supervisor"` 写在原文注释里）——
   **不是**塞进 test method 的片段。这就是本节开头「在外部客户端程序里调」的实证。
2. **它是 CPI + TPI 混用**：`#include "ci_types.h"` / `"libcicpi.h"` 是 CPI 的，
   `ExecTestProgram()`、`CI_CALL_PASS` 也来自 CPI。**本页只管 TPI 那半。**
   （CPI 属于哪一层、在哪章，**本次未查，本页不判**。）
3. **原文那段的 `if (lDeviceState == 1) {` 后面多一个 `{`**，按字面抄是编译不过的。
   **这是原文自带的**，不是本页转录错——语法节是逐字抽的，我一个字没动（§4）。

**其余例程各带一个几行的调用片段**（如 `SetSiteInFocus(2, &re_state);`），也都在语法节里。

**按用途找函数的顺序**：先看上表定位功能组，再去上面语法节找同名小节。

**「改设备」那一组值得留意**：`ChangeDevice` / `GetDevPath` / `GetTechPath` / `GetFileState`
四个是**成组**用的（改、查路径、查文件状态），
[[project]] 页把这一组记为 L3 里**唯一直接对口「建 device」**的接口。

## 和谁有关

**入边先分清两个口径，混起来会得出相反的结论：**

| 口径 | 数 | 说明 |
|---|---|---|
| **本 wiki 内的引用** | **12 处 / 9 个 stage 页** | level×2、testmethod×2、timing×2，pattern/pin/project/results/run/testflow 各 1 |
| **语料内指向根文档的边** | **1 条 inline**（+1 条 `toc`，来自章节目录 `index.md`） | 来自父章 `02.09.01_Managing_Test_Programs_with_SmarTest` |
| **语料内指向本章任意一篇的边** | **123 条 / 14 篇** | 指向例程，不指向根文档 |

**所以「建这一页的理由」既不是入度、也不是 `Subtopics`，是第三种：九页已经伸手要它了。**
根文档在语料里几乎没人直接引用（1 条），**但本 wiki 的九个 stage 页一共引了它 12 处**——
**那 12 处全都指向一个当时还不存在的页**。**是 wiki 自己要它，不是语料在要它。**
**「wiki 内入度」和「语料内入度」是两个不同的指标**，这一页是两者背离最明显的例子。

**九个 stage 页把它当什么用**：都放在各自的 `## L3 — 外部控制` 一节里，
与 [[test-suite-control-api]] 并列（见 [[level]]：*「横切入口见
[[test-suite-control-api]]；产物文件接口见 [[tpi-program-routines]]（**同层、同样由外部客户端
进程调用**，见该页「出处」）」*）。[[pin]] 页还单独记了 `DataManager` 的文件标识那一支。

> **那 11 处措辞改过一次。** 九页原写「**程序侧**对产物文件的操作见 [[tpi-program-routines]]」，
> 与「横切入口」对举——**读起来像「TPI 在 testflow 程序里用」**。**我自己就是被这个词带偏的**，
> 才把 `layer: L3` 记成「推断，存疑」（见「出处」）。2026-09-18 复核后九页统一改口。
> **两页真正的区别是「产物文件 vs 执行控制」，不是「内部 vs 外部」。**

**本页与 [[test-suite-control-api]] 并列**，是 L3 的两个横切入口，**读者要同时看两页**。

> ⚠️ **本页初稿在这里写过一句「二者不能同时用」，那是编的，已删。**
> 原文只说 [[test-suite-control-api]] 不能与 **HVM API / BLC API** 被同一 client 进程并行使用——
> **一个字都没提 TPI**。而且这条**看起来很像真的**（两个都是外部客户端程序），
> 所以特别危险：**「文档没说」不等于「可以」，更不等于「不可以」**，只等于**本页不许写**（§11）。

**不链的**：29 个例程（`02.09.01.09.01`–`.29`）**一个都没建页**，也不在任何一份可建页清单里
（不在 `dangling.csv`、不在 `unowned.csv`），按 §9.1 只能写成反引号。
**它们的正文已经在上面语法节里逐字抽进来了**，不需要再建页——
建出来会是一批只有签名、没有上下文的空页。

**上行**：[[run]]（`stage` 字段填它，含义是「最近」，不是「归属」，见下）、[[testflow]]。

## 版本

- **Introduced before SmarTest 6.3.2**（即本 wiki 面向的 7.10.3 **包含全部**这些例程）
- **SmarTest 7.1.0**：`ExecTfFile`、`ExecTfParam` **obsolete**
- **SmarTest 7.2.0**：**移除了 shmoo plot 的三个 TPI**（`OpenShmoo`、`CloseShmoo`、
  `writeShmoo`），**改用 `SHMOO.drawPlot()` API**

> **这三条要连起来读**：7.1.0 说「过时」、7.2.0 说「移除」，
> 而**这五个名字在 7.10.3 的 29 个例程里一个都找不到**（`Subtopics` 里没有）——
> 文档自己做到了「移除的就不列」。
> **所以读老代码时看到 `OpenShmoo()`，那不是本页漏抄，是它在 7.2.0 被删了。**
> （`SHMOO.drawPlot()` 属于哪一层，本页不判——它不在本章，**本次未查**。）

## 出处

- 定义文档：`02_System_reference/02.09_Test_Program_Management/02.09.01.09_TPI_Program_Routines.md`
  （TDC `26578.htm`）
- 全章 **31 篇**（`02.09.01.09` + `.01`–`.30`）；语法节逐字取自其中 **29 篇**
  （`29,953` 字符；`.30` 附录是 include 说明，被引在「是什么」里而不是当语法抽）
- **wiki 内引用 12 处 / 9 页**；**语料内根文档入边 1 条 inline**（见「和谁有关」的表）
- `layer: L3` **是文档事实**（2026-09-18 复核后定；此前本页记作「推断，存疑」）。
  **原先的存疑是「文档没明说调用者是 testflow 程序还是外部程序」——答案是外部程序**，
  三篇文档各自独立说到，且互相印证：

  | 出处 | 原文 |
  |---|---|
  | `02.09.01.15.01.02_Custom_shell_in_supervisor_mode` | 用 `-S` 起 supervisor mode，然后 *"make use the SmarTest **TPI and CPI** libraries. This is the recommended way if you want to implement a custom production test shell"*；外壳会 *"start another program (**run_supervisor**) that will do the actual work of calling the SmarTest API functions"* |
  | `02.09.01.15.04.01_TPI_functions` | `HpInit()` *"must be called first by **the test shell**, but after SmarTest is up and running in **supervisor mode**"*；`HpTerm()` *"at the end of your program (for example, **run_supervisor**)"* |
  | `02.09.01.09.19_HpInit`（本篇自己的例子） | `int main()` → `HpInit(); /* attach to SmarTest process */`，注释写明 `argv[0]=="run_supervisor"`，随后 `DataManager(dm_testprog, dm_load, …)` + `ExecTestProgram()` + `HpTerm(); exit()` |

  **判据是那篇例子**：它是一个**独立可执行程序**（有 `main`、有 `argv`、有 `exit`），
  `HpInit` 的注释直说 *attach to SmarTest process*——**从外部进程 attach 上去**，
  这正是「外部控制」的定义。`HpInit` 分配的是 **IPC** 资源（进程间通信），进程间三个字本身就排除了同进程内调用。

  原先记的两条旁证仍然成立、方向一致：①`DataManager` 原文说该编程接口是
  *"a **mirror image** of the Test Program Explorer interface"*，是**图形界面的程序化镜像**；
  ②`HpFwTask` 原文 *"will not automatically handle site focus **as test method APIs do**"*——
  文档自己把它和 L2 对立起来。

  >⚠️ **一处曾把我带偏的措辞，记在这儿**：`tpi_c.h` 附录说这些定义是给
  > *"your SmarTest **test flow programs**"* / *"your **testflow source file**"* 用的。
  > 「test flow program」很容易读成「testflow 里的东西」＝L2 甚至 L1。
  > **但那指的是「你写的那个客户端程序」**——`HpInit` 里那段 `main()`＋`argv[0]=="run_supervisor"`
  > 就是这种程序长什么样的实证。**同一章里用词宽松，实证在例子里。**

  > **由此得一条 schema 层面的更正**：`schema.md` §3 把 L3 枚举成
  > Test suite control API（51）+ HVM API（16）= **67 篇**，**漏了 TPI 的 31 篇**。
  > 已改正（67 → 98），并另记 `02.09.01.15`（15 篇）为 TPI/CPI 的**用法章**。
- **`layer: L3` 与 [[test-suite-control-api]] 是同一层、同一调用场景**——
  两者都在**外部客户端进程**里调，启动方式都是 **`run -S`**：

  | | 原文怎么写 | 原文怎么叫它 |
  |---|---|---|
  | 本篇 | *"after SmarTest is up and running in **supervisor mode**"* | supervisor mode |
  | tsca | *"To activate the **run shell**, execute the following command: `run -S`"* | run shell |

  **是同一个开关（`-S`），但两篇文档给它两个名字**——本页照录两边措辞，**不替文档归并**。
  两页的骨架也一一对应：`HpInit()` ↔ `initializeSession()`、`HpTerm()` ↔ `detachSession()`，
  且 **`SetSiteInFocus` / `SetActiveSites` 两个名字在两张 API 里都有**（同名不同族）。
- `stage: run` 填的是**「最近的一段」，不是「归属」**（§6）。§6 给的判据是
  **「读者该去哪一段里找它的用法」**，按这个判据填 [[run]]：
  ①`HpInit` 那段例子本身就是 **attach → 装/执行测试程序 → detach** 的执行期动作；
  ②[[run]] 页里有 `### 3b. TPI 例程` 一整节，**是全 wiki 唯一给出完整能力清单的地方**——
  读者的实际去处就是它。
  **另一个说得通的答案是 [[testflow]]**（原文说这些例程是 *"for writing test flow programs"*，
  且 `DataManager` 管的是测试程序/产物文件的装载）。**这条也一并写下来**，
  免得下次有人重新判一遍还判得不一样（§3「归属判定」那条规矩）。
  **本页横跨执行期与装载期，`stage` 字段只能填一个，承载不了这个事实。**
- 本页 `verified: doc-only`。**参数表在语料里已被 HTML→markdown 转换拆散**
  （实测本页语法节里有 **427 处**孤立 `|` 行，如 `Parameter` / ` |` / `Value` / ` |` …），
  **内容不缺、形状缺**。**本页原样保留，不回填成表格**——回填要猜列数与行界，
  猜就是编（§4）。要整齐的表格，**回看 raw 里那几篇**。
