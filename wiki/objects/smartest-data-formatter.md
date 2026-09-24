---
type: object
title: SmarTest Data Formatter
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.03_SmarTest_Data_Formatter.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# SmarTest Data Formatter

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **15,395 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.03_SmarTest_Data_Formatter.md>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.03.03.07_Reprobe_data.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.03.09.02_Logging_text_data_in_the_TEST_TXT_field.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.03.11_Force_closing_out_lot_or_wafer_level_in_application_model.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.05_Version_Update_Record__VUR.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.08_Site_Description_Record__SDR.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.12_Pattern_Sequence_Record__PSR.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.27_Generic_Data_Record__GDR.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.28_Activity_Trace_Event_Record__ATER.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Description（取自子主题 Formatting V93000 Test Results to STDF › Reprobe data）

Software bin 11 is marked as a reprobe bin. If a device is tested and binned into software bin 11 (and hardware bin 1), the device will be immediately retested. If the device is retested and binned into software bin 10 and hardware bin 0, the SBR and HBR records will show the device binned into software bin 10 and hardware bin 0; the initial binning into software bin 11 and hardware bin 1 is not reflected in the SBR and HBR records.

### Syntax（取自子主题 Formatting V93000 Test Results to STDF › Test methods › Logging text data in the TEST TXT field）

For a temporary object:

```
TESTSET().member_func().TEST(parameters);
```

For a system-prepared object:

```
TestSet.member_func().TEST(parameters);
```

User object (TESTSET obj;)

```
obj. member_func().TEST(parameters);
```

`member_func()` is one of or a combination of the following member functions:

- port()
- cont()
- reliability()
- testnumber_default()
- testnumber_none()
- testnumber()
- testname_default()
- testname()
- testtext_none()
- testtext()
- testtype_default()
- testtype()Note member_func entries are optional.

`TEST(parameters)`: One of the TEST member functions. See the TEST API in the Test Method Programming Reference.

### Example（取自子主题 Formatting V93000 Test Results to STDF › Force closing out lot or wafer level in application model）

The following example illustrates a common use of FORCE_MODEL_LEVEL_LOGGING_COMPLETE. It performs tests on all devices belonging to a lot and at the end copies the finished log into a quality database. (The details of the test are unimportant here and have been left out; the log is copied by using EXEC_INP_CALL to call an external function that is assumed to perform this task.)

To ensure that the log is properly closed before it is copied, FORCE_MODEL_LEVEL_LOGGING_COMPLETE is executed just before the copying begins. Because logs can be open simultaneously for the lot and the wafer, it is necessary to specify which one the data formatter is to close.

```
{ lot:
    ...
  { DEVICE device:
    ...
    { DEVICE_TEST }
    ...
  }
  ...
  ACTIONS
    FORCE_MODEL_LEVEL_LOGGING_COMPLETE = CONST_INPUT(LOT);
    EXEC_INP_CALL(push_stdf_to_database);
}
```

### Syntax（取自子主题 Appendix A  STDF Record Types › Version Update Record  VUR）

VUR in STDF V4/2007
 |

VUR field name

 |

Field description

 |

Value

 |

93000 data source

 |
 |

UPD_NAM

 |

The version after STDF V4 to which this data log conforms.

 |

Variable-length character string.

Maximum 255 characters.

 |

The content is taken from the `stdfVersion`（raw: `02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md#_70623__stdfVersion`） parameter.

 |

VUR in STDF V4/2007.1
 |

VUR field name

 |

Field description

 |

Value

 |

93000 data source

 |
 |

UPD_CNT

 |

The number of UPD_NAM fields in this record.

   | One-byte unsigned integer.  | |
 |

UPD_NAM

   | An array of versions after STDF V4 to which this data log conforms. |

Array of variable-length character strings.

Each array element contains a maximum of 255 characters.

 |

The content is based on the `stdfVersion`（raw: `02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md#_70623__stdfVersion`） parameter.

 |

### Syntax（取自子主题 Appendix A  STDF Record Types › Site Description Record  SDR）

|

SDR field name

 |

Field description

 |

Value

 |

93000 data source

 |
 |

HEAD_NUM

 |

- Test head number
 |

- One-byte unsigned integer
- Value = 1
 |

- Hard-coded value
 |
 |

SITE_GRP`1)`（raw: `#fntarg_1`）

 |

- Site group number

(station number)

If there are more than 255 sites, the group number indicates which set of 128 sites is described.

 |

- One-byte unsigned integer
- 2 = Default
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

SITE_GRP

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

SITE_CNT

 |

- Number of active sites described in this record
 |

- One-byte unsigned integer
 |

- Calls the DRLNumberOfSites() test method
 |
 |

SITE_NUM

 |

- Array of active site numbers in this record.

For tests with more than 255 sites (which produce multiple SDRs), the numbering restarts with 0 in each individual SDR.

 |

- Array of one-byte unsigned integers
 |

- The values for this are

0 to N-1 if using 0-based site numbers and 1 to N if using

1-based site numbers (where N is the number of sites).

 |
 |

HAND_TYP

 |

- Handler or prober type
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

HAND_TYP

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

HAND_ID

 |

- Handler or prober ID
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

HAND_ID

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

CARD_TYP

 |

- Probe card type
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

CARD_TYP

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

CARD_ID

 |

- Probe card ID
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

CARD_ID

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

LOAD_TYP

 |

- DUT board type
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

LOAD_TYP

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

LOAD_ID

 |

- DUT board ID
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

LOAD_ID

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

DIB_TYP

 |

- DIB board type
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable2:

DIB_TYP

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

DIB_ID

 |

- DIB board ID
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

DIB_ID

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

CABL_TYP

 |

- Interface cable type
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

CABL_TYP

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

CABL_ID

 |

- Interface cable ID
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

CABL_ID

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

CONT_TYP

 |

- Handler contactor type
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

CONT_TYP

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

CONT_ID

 |

- Handler contactor ID
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

CONT_ID

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

LASR_TYP

 |

- Laser type
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

LASR_TYP

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

LASR_ID

 |

- Laser ID
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

LASR_ID

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

EXTR_TYP

 |

- Extra equipment type
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

EXTR_TYP

- Data source can also be a constant value in the configuration file or a system environment variable.
 |
 |

EXTR_ID

 |

- Extra equipment ID
 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

- Application model variable`2)`（raw: `#_69127__fn2`）:

EXTR_ID

- Data source can also be a constant value in the configuration file or a system environment variable.
 |

### Syntax（取自子主题 Appendix A  STDF Record Types › Pattern Sequence Record  PSR）

|

PSR field name

 |

Field description

 |

Value

 |

93000 data source

 |
 |

CONT_FLAG

 |

Flag for the existence of PSR continuation records

 |

- Variable-length bit-encoded field
- If the value is 1, there is a PSR continuation record after the current record.

If the value is 0, this PSR is the last record.

 |

 |
 |

PSR_INDX

 |

Index of the PSR record (used by STR records)

 |

- Two-byte unsigned integer
- 0 = missing or invalid data
 |

 |
 |

PSR_NAM

 |

The symbolic name of the test suite to which the PSR belongs

 |

- Variable length character string
- First byte is unsigned count of bytes to follow
- Maximum 255 bytes
- Length byte = 0 if missing or invalid data
 |

 |
 |

OPT_FLG

 |

Flags that indicate the presence of optional fields and conventions for certain indexes.

 |

Variable-length bit-encoded field

 |

 |
 |

 |

 |

Bit 0:

- If 0, the PAT_LBL field is present.
- If 1, the PAT_LBL field is missing.
 |

 |
 |

 |

 |

Bit 1:

- If 0, the FILE_UID field is present.
- If 1, the FILE_UID field is missing.
 |

 |
 |

 |

 |

Bit 2:

- If 0, the ATPG_DESC field is present.
- If 1, the ATPG_DESC field is missing.
 |

 |
 |

 |

 |

Bit 3:

- If 0, the SRC_ID field is present.
- If 1, the SRC_ID field is missing.
 |

 |
 |

 |

 |

Bit 4: The first cycle number (0 or 1)

 |

 |
 |

 |

 |

Bit 5: The first pattern number (0 or 1)

 |

 |
 |

 |

 |

Bit 6: The starting value of the bit position

 |

 |
 |

TOTP_CNT

 |

The total number of patterns that comprise the scan test over all PSRs. This must be the same value in all PSRs for the test (initial record and continuation records).

 |

- Two-byte unsigned integer
- Index between 1 and 32767
 |

 |
 |

LOCP_CNT

 |

Count of pattern file information sets in this record

 |

- Two-byte unsigned integer
- Index between 1 and 32767
 |

 |
 |

PAT_BGN

 |

Array of cycle numbers at which the patterns begin. The number of the first cycle (0 or 1) is determined by bit 4 of OPT_FLG.

 |

- Array with the dimension LOCP_CNT
- Each value is an eight-byte unsigned integer
 |

 |
 |

PAT_END

 |

Array of cycle numbers at which the patterns stop

 |

- Array with the dimension LOCP_CNT
- Each value is an eight-byte unsigned integer
 |

 |
 |

PAT_FILE

 |

Array of pattern file names

 |

- Array with the dimension LOCP_CNT
- Variable length character string:

- First byte is unsigned count of bytes to follow

- Maximum 255 bytes

- Length byte = 0 if missing or invalid data

 |

 |
 |

PAT_LBL

 |

Optional array of symbolic pattern names

 |

- Array with the dimension LOCP_CNT
- Variable length character string:

- First byte is unsigned count of bytes to follow

- Maximum 255 bytes

- Length byte = 0 if missing or invalid data

 |

 |
 |

FILE_UID

 |

Optional array of file identifier codes

 |

- Array with the dimension LOCP_CNT
- Variable length character string:

- First byte is unsigned count of bytes to follow

- Maximum 255 bytes

- Length byte = 0 if missing or invalid data

 |

 |
 |

ATPG_DESC

 |

Optional array of ATPG information

 |

- Array with the dimension LOCP_CNT
- Variable length character string:

- First byte is unsigned count of bytes to follow

- Maximum 255 bytes

- Length byte = 0 if missing or invalid data

 |

 |
 |

SRC_ID

 |

Optional array of PatternInSrcFileIDs

 |

- Array with the dimension LOCP_CNT
- Variable length character string:

- First byte is unsigned count of bytes to follow

- Maximum 255 bytes

- Length byte = 0 if missing or invalid data

 |

 |

### Example（取自子主题 Appendix A  STDF Record Types › Generic Data Record  GDR）

The following table describes a sample GDR that contains three data fields of different data types. We are assuming that numeric data of more than one byte must begin on an even boundary. Pad bytes are used to meet the requirements.

 |

Data

 |

Code

 |

Alignment Requirement

 |
 |

"AB"

 |

10

 |

A variable-length character string can begin on any byte. This field will contain one data byte, one length byte, and two data bytes, for a total length of 4 bytes. Because this field begins on an even byte, the next field also begins on an even byte.

 |
 |

255

 |

1

 |

A one-byte numeric value can begin on any byte. This field contains two bytes, so the next field also begins on an even byte.

 |
 |

510

 |

5

 |

A two-byte numeric value must begin on an even byte. This GEN_DATA field would begin on an even byte; and, because the first byte is the data code, the actual numeric value would begin on an odd byte. This field must be preceded by a pad byte.

 |

The byte representation for this example GDR is shown below, and is shown for sample purposes only. The actual data representation differs between CPUs. The byte values are in hexadecimal, with the decimal equivalents given in the byte descriptions.

 |

Even byte

 |

Odd byte

 |

Description (with decimal values)

 |
 |

0c

 |

00

 |

Number of bytes following the header (12)

 |
 |

32

 |

0a

 |

Record type (50); record subtype (10)

 |
 |

04

 |

00

 |

Number of data fields (4)

 |
 |

0a

 |

02

 |

Character string: code (10) and length (2)

 |
 |

41

 |

42

 |

Character string: data bytes ("A" and "B")

 |
 |

01

 |

ff

 |

One-byte integer: code (1) and data (255 = 0xff)

 |
 |

00

 |

05

 |

Pad byte (0); code (5) for next field

 |
 |

fe

 |

01

 |

Two-byte signed integer (510 = 0x01fe)

 |

### Example（取自子主题 Appendix A  STDF Record Types › Activity Trace Event Record  ATER）

```
GDR Record
  REC_CUSTM:       ACTIVITY_TRACE_LOG
  EVT_SRC:         Demo2
  HEAD_NUM:        0x0
  SITE_NUM:        0x1
  ACTIVITY:        *********
[PERSPEC 1010] 240 18 0 1
[USER 2020] *********
00000000000000000000004294927948  : ####2#

shmoo_size: 1
[PERSPEC 6708282] 223 0 -39348 1145128001 1145128001
```

<!-- 语法节 end -->

## 是什么

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
