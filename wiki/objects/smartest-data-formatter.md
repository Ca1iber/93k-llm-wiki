---
type: object
title: SmarTest Data Formatter
layer: gui
stage: results
tags: [smartest-data-formatter, stdf, data-logging, results, application-model, gui]
related: [stdf, results, run, testset]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.03_SmarTest_Data_Formatter.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# SmarTest Data Formatter

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **15,468 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.03_SmarTest_Data_Formatter.md>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.03.03.07_Reprobe_data.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.03.09.02_Logging_text_data_in_the_TEST_TXT_field.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.03.11_Force_closing_out_lot_or_wafer_level_in_application_model.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.05_Version_Update_Record__VUR.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.08_Site_Description_Record__SDR.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.12_Pattern_Sequence_Record__PSR.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.27_Generic_Data_Record__GDR.md>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.28_Activity_Trace_Event_Record__ATER.md>`。**不是转述。**
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
| VUR field name | Field description | Value | 93000 data source |
|---|---|---|---|
| UPD_NAM | The version after STDF V4 to which this data log conforms. | Variable-length character string.<br><br>Maximum 255 characters. | The content is taken from the `stdfVersion`（raw: `02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md#_70623__stdfVersion`） parameter. |

VUR in STDF V4/2007.1
| VUR field name | Field description | Value | 93000 data source |
|---|---|---|---|
| UPD_CNT | The number of UPD_NAM fields in this record. | One-byte unsigned integer. |  |
| UPD_NAM | An array of versions after STDF V4 to which this data log conforms. | Array of variable-length character strings.<br><br>Each array element contains a maximum of 255 characters. | The content is based on the `stdfVersion`（raw: `02.10.03.04.03_Configuring_the_contents_of_the_STDF_file.md#_70623__stdfVersion`） parameter. |

### Syntax（取自子主题 Appendix A  STDF Record Types › Site Description Record  SDR）

| SDR field name | Field description | Value | 93000 data source |
|---|---|---|---|
| HEAD_NUM | - Test head number | - One-byte unsigned integer<br>- Value = 1 | - Hard-coded value |
| SITE_GRP`1)`（raw: `#fntarg_1`） | - Site group number<br><br>(station number)<br><br>If there are more than 255 sites, the group number indicates which set of 128 sites is described. | - One-byte unsigned integer<br>- 2 = Default | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>SITE_GRP<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| SITE_CNT | - Number of active sites described in this record | - One-byte unsigned integer | - Calls the DRLNumberOfSites() test method |
| SITE_NUM | - Array of active site numbers in this record.<br><br>For tests with more than 255 sites (which produce multiple SDRs), the numbering restarts with 0 in each individual SDR. | - Array of one-byte unsigned integers | - The values for this are<br><br>0 to N-1 if using 0-based site numbers and 1 to N if using<br><br>1-based site numbers (where N is the number of sites). |
| HAND_TYP | - Handler or prober type | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>HAND_TYP<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| HAND_ID | - Handler or prober ID | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>HAND_ID<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| CARD_TYP | - Probe card type | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>CARD_TYP<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| CARD_ID | - Probe card ID | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>CARD_ID<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| LOAD_TYP | - DUT board type | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>LOAD_TYP<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| LOAD_ID | - DUT board ID | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>LOAD_ID<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| DIB_TYP | - DIB board type | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable2:<br><br>DIB_TYP<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| DIB_ID | - DIB board ID | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>DIB_ID<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| CABL_TYP | - Interface cable type | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>CABL_TYP<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| CABL_ID | - Interface cable ID | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>CABL_ID<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| CONT_TYP | - Handler contactor type | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>CONT_TYP<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| CONT_ID | - Handler contactor ID | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>CONT_ID<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| LASR_TYP | - Laser type | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>LASR_TYP<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| LASR_ID | - Laser ID | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>LASR_ID<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| EXTR_TYP | - Extra equipment type | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>EXTR_TYP<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |
| EXTR_ID | - Extra equipment ID | - Variable length character string<br>- First byte is unsigned count of bytes to follow<br>- Maximum 255 bytes<br>- Length byte = 0 if missing or invalid data | - Application model variable`2)`（raw: `#_69127__fn2`）:<br><br>EXTR_ID<br><br>- Data source can also be a constant value in the configuration file or a system environment variable. |

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

| Data | Code | Alignment Requirement |
|---|---|---|
| "AB" | 10 | A variable-length character string can begin on any byte. This field will contain one data byte, one length byte, and two data bytes, for a total length of 4 bytes. Because this field begins on an even byte, the next field also begins on an even byte. |
| 255 | 1 | A one-byte numeric value can begin on any byte. This field contains two bytes, so the next field also begins on an even byte. |
| 510 | 5 | A two-byte numeric value must begin on an even byte. This GEN_DATA field would begin on an even byte; and, because the first byte is the data code, the actual numeric value would begin on an odd byte. This field must be preceded by a pad byte. |

The byte representation for this example GDR is shown below, and is shown for sample purposes only. The actual data representation differs between CPUs. The byte values are in hexadecimal, with the decimal equivalents given in the byte descriptions.

| Even byte | Odd byte | Description (with decimal values) |
|---|---|---|
| 0c | 00 | Number of bytes following the header (12) |
| 32 | 0a | Record type (50); record subtype (10) |
| 04 | 00 | Number of data fields (4) |
| 0a | 02 | Character string: code (10) and length (2) |
| 41 | 42 | Character string: data bytes ("A" and "B") |
| 01 | ff | One-byte integer: code (1) and data (255 = 0xff) |
| 00 | 05 | Pad byte (0); code (5) for next field |
| fe | 01 | Two-byte signed integer (510 = 0x01fe) |

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

**先说这一页最大的一个事实：这篇定义文档没有正文。**

它 16 行，除了 frontmatter 与标题，**全部内容是 `#### Subtopics` 底下的 7 行清单**——
**一句话都没有写「SmarTest Data Formatter 是什么」**（见 `## 出处` ①）。
**所以本页的实质，只能从它自己列的那 7 个部分里读出来。**

**7 个部分，逐字（这一份清单本身是本文档的全部内容）：**

| # | 部分（**逐字**） | 从名字能读出什么 |
|---|---|---|
| 1 | `Standard Test Data Format (STDF) Overview` | 它的产物是 **STDF** |
| 2 | `Starting and Stopping the Formatter` | **它是一个要起停的常驻东西**（不是一次性函数） |
| 3 | `Formatting V93000 Test Results to STDF` | **它干的事：把 V93000 的测试结果格式化成 STDF** |
| 4 | `STDF Configuration` | 它**可配**（配什么见下面第 4 部分） |
| 5 | `Appendix A: STDF Record Types` | 产物由**一批记录（record）**构成 |
| 6 | `Appendix B: The STDF Reader` | 另有一个**读** STDF 的工具，用来核对内容 |
| 7 | `Appendix C: Example Application Model` | 它跟 **application model** 有关，且有一个可抄的例子 |

**⚠️ 上表右栏第二列是**读出来的结论**，不是原文的句子**——原文只给了这 7 个标题。

### 它到底是什么：从 Appendix C 那两句能定下来的

**7 个部分里只有 Appendix C 有正文**，而它开口就把两件事说死了，逐字：

> 「This application model demonstrates the sample code used for an automatically performed Wafer
> test using the GenericProber driver, and contains a number of application model variables which
> will be recognized by the STDF generation tool.」

> 「These values are included in the STDF data generated by this tool.」

**两句合起来：这是一个「STDF generation tool」；它会**识别 application model 里的变量**，
并把那些值**写进它生成的 STDF 数据**。**

**同一篇的示例代码里还有一条注**（**这里转述，不逐字引**——
那两行在代码块里各带一个 `--` 前缀，逐字引会丢字符）：
**大意是「用户不需要在 App Model 里专门写一句调用来触发 STDF formatter」。**
**即：它是被测试程序自动带起来的，不是显式调用的。**

### 产物里有什么：29 种 STDF 记录类型

**Appendix A 那一篇的 `#### Subtopics` 列了 33 项**，其中 **29 项是记录类型**，
**另外 4 项不是记录**（`Overview`、`Specifying the data source`、`Sequence of STDF records`、
`Application model variables used for STDF generation`）。

**29 种记录，逐字（按清单顺序）：**

| | | | |
|---|---|---|---|
| `FAR` | `ATR` | `VUR` | `MIR` |
| `RDR` | `SDR` | `HBR` | `SBR` |
| `PMR` | `PSR` | `WIR` | `WRR` |
| `WCR` | `PIR` | `STR` | `NMR` |
| `CNR` | `SSR` | `CDR` | `PTR` |
| `MPR` | `FTR` | `PRR` | `TSR` |
| `GDR` | `ATER` | `DTR` | `PCR` |
| `MRR` | | | |

**（表里这些三四个字母的缩写，取自附录那一篇的标题：原文每个标题都是
「全名 + (缩写)」的形态，例如 `File Attributes Record (FAR)`——
**上表把全名省掉了**，33 行的全名见 raw。）**

**⚠️ 上面这张表里**只有 29 行**，而 Appendix A 的清单是 33 项——差的那 4 项就是上面点名的那 4 个非记录项。**
**本页没有把哪一个当作「记录」来数。**

### 每条 STDF 字段都能追回 93000 里的一个源

**这是这一页最有价值的结构**，而且它在本页 `## 语法 / 参数` 节里看得见：
**每一张记录表都有一栏叫 `93000 data source`。**

**以 `VUR`（`Version Update Record`）那份为例**，它的表头逐字是
`VUR field name` / `Field description` / `Value` / `93000 data source`，
而 `93000 data source` 那一格填的是——逐字：

> 「The content is taken from the `stdfVersion` parameter.」

**即：STDF 里的每一格，都能追到 93000 侧的一个参数 / 变量 / API。**
**这一栏不是某一两份记录的特色**：本文档子树里**专门有一篇叫
`Specifying the data source`**（**本页没读**），
而 `Application model variables used for STDF generation` 也是**单独一篇**——
**（推断）说明「哪个字段从哪来」这件事本身，就是这一套文档的一个主题。
依据只是这两个标题的存在，原文没有说它们是干什么的。这是推断。**

### 三个「改输出内容」的机制（在 `## 语法 / 参数` 节里看得见）

#### ① reprobe bin：软 bin 11

**节名是 `Description（取自子主题 … › Reprobe data）`**，逐字：

> 「Software bin 11 is marked as a reprobe bin. If a device is tested and binned into software bin
> 11 (and hardware bin 1), the device will be immediately retested. If the device is retested and
> binned into software bin 10 and hardware bin 0, the SBR and HBR records will show the device
> binned into software bin 10 and hardware bin 0; the initial binning into software bin 11 and
> hardware bin 1 is not reflected in the SBR and HBR records.」

**三条要记住的：**

| # | 内容 |
|---|---|
| 1 | **软 bin `11` 被标为 reprobe bin**（**是 11 这个号，不是「随便哪个」**） |
| 2 | **落进软 bin 11（且硬 bin 1）的器件会被立刻重测** |
| 3 | **重测后落进软 bin 10 / 硬 bin 0 时，`SBR` 与 `HBR` 记录里只有后一次——第一次（11/1）不在记录里** |

**⚠️ 第 3 条最容易读错**：**不是「记录两次」，是「只记最后一次」。**

#### ② 往 `TEST_TXT` 字段里写文本

**节名是 `Syntax（取自子主题 … › Test methods › Logging text data in the TEST TXT field）`。**
**它给三种写法**，逐字：`For a temporary object:` / `For a system-prepared object:` /
`User object (TESTSET obj;)`，各配一段代码：

```
TESTSET().member_func().TEST(parameters);
TestSet.member_func().TEST(parameters);
obj. member_func().TEST(parameters);
```

**⚠️ 第三段的 `obj. member_func()` 里 `obj.` 后面多了一个空格**，见 `## 出处` ②。

**`member_func()` 是一串可选修饰**，原文逐字
`member_func() is one of or a combination of the following member functions:`，
列了 **12 个**：`port()` / `cont()` / `reliability()` /
`testnumber_default()` / `testnumber_none()` / `testnumber()` /
`testname_default()` / `testname()` /
`testtext_none()` / `testtext()` /
`testtype_default()` / `testtype()`。

**三组名字里「`_default` / `_none` / 不带后缀」是三种形态**
（`testnumber_default` / `testnumber_none` / `testnumber` 各一组，`testname` 与 `testtype` 也是）。
**（推断）它们分别对应「取默认值 / 不写这一项 / 显式给值」——
依据只是名字的构词，原文没有解释这三个后缀。这是推断。**

**`TEST(parameters)` 那一项原文没展开**，逐字：
`TEST(parameters): One of the TEST member functions. See the TEST API in the Test Method
Programming Reference.`
**即：这一页把 `TEST` 的语义推给了 `Test Method Programming Reference`（本页没读）。**

#### ③ 关掉 lot / wafer 层的日志：`FORCE_MODEL_LEVEL_LOGGING_COMPLETE`

**节名是 `Example（取自子主题 … › Force closing out lot or wafer level in application model）`。**
**它先讲为什么需要这个调用**，逐字的两句：

> 「To ensure that the log is properly closed before it is copied, FORCE_MODEL_LEVEL_LOGGING_COMPLETE
> is executed just before the copying begins.」

> 「Because logs can be open simultaneously for the lot and the wafer, it is necessary to specify
> which one the data formatter is to close.」

**第 2 句是这一节真正的要点：lot 与 wafer 的日志可以同时开着，所以调用时必须指定关哪一个。**
**代码里指定关 lot**，逐字：`FORCE_MODEL_LEVEL_LOGGING_COMPLETE = CONST_INPUT(LOT);`
**（本页只有 `LOT` 这一个写法，`WAFER` 那个写法本篇没有给。）**

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有一个命令行。**
**7 个部分全是**标题**，一篇正文都没有**（Appendix C 除外）——
**所以「怎么用」本页只能给三样东西：那 7 个部分的顺序、Appendix C 那个可抄的例子、
以及 `## 语法 / 参数` 节里三处带代码的机制。**

### 一、按 7 个部分给出的路径

**这是本文档自己的目录顺序，本页只是把它读成一条路径**：

| 步 | 去哪一篇 | 干什么 |
|---|---|---|
| 0 | `Standard Test Data Format (STDF) Overview` | 先知道 STDF 是什么（**那一篇本页没读**） |
| 1 | `Starting and Stopping the Formatter` | 起 / 停 formatter（**那一篇底下还有
`Starting the formatter` / `Stopping the formatter` / `Generating STDF from the Testflow Editor` /
`Data log flags for STDF` / `Data Formatter errors and warnings` 五项，本页都没读**） |
| 2 | `Formatting V93000 Test Results to STDF` | 怎么把结果变成 STDF（**11 个子主题，本页都没读**） |
| 3 | `STDF Configuration` | 配输出（**4 个子主题，本页都没读**） |
| 4 | `Appendix A: STDF Record Types` | 查某个记录 / 某个字段（**33 项，本页都没读**） |
| 5 | `Appendix B: The STDF Reader` | 反过来**核对**一个 STDF 文件的内容（**2 项，本页都没读**） |
| 6 | `Appendix C: Example Application Model` | 抄一个完整的 application model（**本页读了这一篇**） |

**⚠️ 上表第 4 步那一行是最要紧的**：**「哪个字段是什么」的答案在 Appendix A 的 33 篇里**——
**本页一个字都没有。**

### 二、Appendix C 那个例子：一个 wafer 测试的 application model

**它是一段完整的 application model**（`hp93000,applicmodel,0.1` 开头）。
**原文对它的一句话交代**，逐字：

> 「This application model demonstrates the sample code used for an automatically performed Wafer
> test using the GenericProber driver, and contains a number of application model variables which
> will be recognized by the STDF generation tool.」

**结构（照代码里的层级与注释）**：

| 层 | 里面的关键内容（**逐字**） |
|---|---|
| `START_DIALOG` / `testprogram` | `SCREEN_DIALOG` 里收 `Operator_id`；`ACTIONS` 里 `OPER_NAM` 与 `HOST` 用 `CONST_INPUT` 赋值 |
| `SCREEN_DIALOG` | `* Operator_id = DIALOG_INPUT / REGEXP(string);`——**输入项** |
| `lot` | **一大串 MIR 字段值**（注释逐字 `-- MIR field values`）+ `-- MRR field values` + `-- SDR field values (not all)` |
| `cassette` | `LINE_DIALOG` 收 `cassette_id` |
| `WAFER wafer` | `LINE_DIALOG` 收 `wafer_id`；`ACTIONS` 里给 **WIR / WRR 字段值**（注释逐字 `-- WIR, WRR field values`） |
| `wafer_log` | 注释逐字 `This level is used, to ensure that a wafer log file is written after the DEVICE level is left.` 与 `The wafer_log level is executed exactly once for each wafer.` |
| `DEVICE [({WAFER_ID}),()] die` | `DEVICE_TEST`——**真正跑测试的那一层** |

**三个可抄的具体写法：**

- **MIR 字段值靠 `CONST_INPUT` 一条一条给**，逐字举例：
  `STAT_NUM = CONST_INPUT(25);` / `LOT_ID = CONST_INPUT(5);` /
  `TSTR_TYP = CONST_INPUT(93k SOC Tester);` / `JOB_NAM = CONST_INPUT(Darwin);` /
  `DATE_COD = CONST_INPUT(GET_TEST_INFO(date_time));`——
  **注意 `DATE_COD` 用的是 `GET_TEST_INFO(date_time)`，不是常量。**
- **SDR 只是「给了一部分」**：注释逐字 `-- SDR field values (not all)`。
- **STDF 文件路径由一个变量给**，逐字：
  `STDF_FILE = CONST_INPUT(/tmp/{LOT_ID}.{wafer_id}.stdf);`

**⚠️ 例子里的 `wafer_id` 有四种写法**（`WAFER_ID` / `{WAFER_ID}` / `{wafer_id}` / `{PH_wafer_id}`），
**语料没有解释它们的区别**，见 `## 出处` ③。

### 三、三个可以直接用的机制

**都在 `## 语法 / 参数` 节里**，各自带代码：

| 要做的事 | 用哪个 | 关键约束（**逐字**） |
|---|---|---|
| **让落进某个 bin 的器件自动重测** | reprobe bin = **软 bin 11** | `Software bin 11 is marked as a reprobe bin.` |
| **往 `TEST_TXT` 里写文本** | `TESTSET().member_func().TEST(parameters);` 那一族 | `member_func entries are optional.` |
| **在 lot / wafer 层日志结束前把它关掉** | `FORCE_MODEL_LEVEL_LOGGING_COMPLETE` | `it is necessary to specify which one the data formatter is to close.` |

**第二条里最实用的一个后缀是 `reliability()`**——
**（推断）它应当是给「可靠性测试」那类结果加标记的；依据只是它的名字，
原文的 12 个名字一个都没解释。这是推断。**

## 和谁有关

- [[stdf]] — **本页的产物格式**。7 个部分里第一、三、四、五、六部分全部围着 `STDF` 转
  （`Standard Test Data Format (STDF) Overview` / `Formatting V93000 Test Results to STDF` /
  `STDF Configuration` / `Appendix A: STDF Record Types` / `Appendix B: The STDF Reader`）。
  **那一页本页没读，所以 STDF 这个格式自己是什么，本页没有。**
- [[results]] — 本页 `stage: results` 的理由：**它是结果数据出去的那一端**。
  **⚠️ 本篇没有 `## Application` 这类自我定位段**，这条归属是本 wiki 的既有划分。
- [[run]] — **（推断）它的起停挂在测试跑的那一段上**。
  依据：7 个部分里第 2 个叫 `Starting and Stopping the Formatter`，
  它的子项里有 `Generating STDF from the Testflow Editor`，而 Appendix C 那个例子里
  `DEVICE_TEST` 是真正跑测试的那一层。
  **原文没有把它和 [[run]] 连起来。这是推断。**
- [[testset]] — **（推断）`## 语法 / 参数` 节里那段 `TEST_TXT` 写法的主语**：
  原文的三种写法都以 `TESTSET()` / `TestSet` / `obj`（原文括注 `TESTSET obj;`）开头。
  **依据只是这三个写法的开头词与 wiki 里那一页同名；
  原文没有点过 `TESTSET` 这个页面名。这是推断，那一页本页没读。**
- `Standard Test Data Format (STDF) Overview`（**未建**）— 7 个部分的第 1 个，**本页没读**。
- `Starting and Stopping the Formatter`（**未建**）— 第 2 个，**本页没读**；
  **它的 5 个子项**（`Starting the formatter` / `Stopping the formatter` /
  `Generating STDF from the Testflow Editor` / `Data log flags for STDF` /
  `Data Formatter errors and warnings`）**也一篇没读**——
  **所以「怎么起」「怎么停」「出错怎么办」本页一个字都没有。**
- `Formatting V93000 Test Results to STDF`（**未建**）— 第 3 个，**本页没读**；
  **它的 11 个子主题**（`General data content options for STDF files` /
  `Parametric or functional test types` / `Multiple pass/fail results from a single test` /
  `Pin results` / `Overon flag` / `Test numbers` / `Reprobe data` /
  `The PART_ID field in the PRR` / `Test methods` /
  `Using MAP_SITE to specify alternate site numbers` /
  `Force closing out lot or wafer level in application model`）**一篇没读**——
  **⚠️ 其中 `Reprobe data` / `Test methods` / `Force closing out lot or wafer level in application model`
  三篇，正是本页 `## 语法 / 参数` 节里那三段的来源**（节名里写着）。
  **本页对它们的了解，只到 `## 语法 / 参数` 节里逐字收的那几段为止——那不是整篇。**
- `STDF Configuration`（**未建**）— 第 4 个，**本页没读**；
  **它的 4 个子主题**（`Configuring the STDF file locations` /
  `Creating both detailed and summary output files` / `Configuring the contents of the STDF file` /
  `Example configuration file`）**一篇没读**——
  **所以「怎么配、能配什么」本页只有从名字猜到的两层（文件位置 / 内容），这是推断。**
- `Appendix A: STDF Record Types`（**未建**）— 第 5 个，**本页没读**；
  **它的 33 个条目一篇没读**（其中 29 个是记录类型，清单见 `## 是什么`）。
  **⚠️ 其中 `Version Update Record (VUR)` / `Site Description Record (SDR)` /
  `Pattern Sequence Record (PSR)` / `Generic Data Record (GDR)` /
  `Activity Trace Event Record (ATER)` 五篇，是本页 `## 语法 / 参数` 节里另外五段的来源**——
  **同样，本页只知道那五段，不知道那五篇。**
- `Appendix B: The STDF Reader`（**未建**）— 第 6 个，**本页没读**；
  **它的 2 个子项**（`Checking the contents of an STDF file` / `STDF reader changes`）**都没读**——
  **所以「怎么核对一个 STDF 文件写得对不对」本页没有。**
- `Appendix C: Example Application Model`（**未建**）— 第 7 个，**本页读了这一篇**
  （它是本文档子树里唯一有正文的一篇之一）。
- `application model`（**未建**）— **本页正文里那个「变量来源」的东西**，
  Appendix C 逐字 `a number of application model variables which will be recognized by the STDF
  generation tool`。**它自己是什么、变量有哪些，本篇没有写，本页也没有。**
- `Test Method Programming Reference`（**未建**）— **`TEST(parameters)` 的出口**，
  逐字 `See the TEST API in the Test Method Programming Reference.` **本页没读。**

## 版本

**本文档没有 `## Functional changes` 段。**

**这是事实，不是缺陷**——**本页读的 8 篇（定义文档 + 它自己列的 7 个部分）一篇都没有这一段**
（本页逐篇查过：`Functional changes` 8 篇里 0 次）。

**所以「SmarTest Data Formatter 从哪一版开始有」这件事，本文档给不出答案。**
**本页不拿别处的版本来填这一格。**

> **⚠️ 一处容易混的**：本页 `## 语法 / 参数` 节里有一段的来源叫
> `Force closing out lot or wafer level in application model`，
> **而「版本」这一节讲的是 `## Functional changes`**——
> **两者不是一回事**：前者是一个功能，后者是变更记录清单。
> **本页只报后者：没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.03_SmarTest_Data_Formatter.md`
（TDC 主题号 `130977`；本地 raw md：**836 字节**、**16 行**——
**字节是磁盘上的字节数，行数是换行符个数**）

**⚠️ 本页在 `sources:` 之外多读了一层，特此声明：**

**定义文档是纯 `#### Subtopics` 索引（16 行，零正文），所以本页读了它自己列的那 7 个部分**：

| 读了的 7 篇 | 字节 | 行 |
|---|---|---|
| `02.10.03.01_Standard_Test_Data_Format__STDF__Overview.md` | 377 | 10 |
| `02.10.03.02_Starting_and_Stopping_the_Formatter.md` | 671 | 14 |
| `02.10.03.03_Formatting_V93000_Test_Results_to_STDF.md` | 1,194 | 20 |
| `02.10.03.04_STDF_Configuration.md` | 608 | 13 |
| `02.10.03.05_Appendix_A__STDF_Record_Types.md` | 2,924 | 42 |
| `02.10.03.06_Appendix_B__The_STDF_Reader.md` | 393 | 11 |
| `02.10.03.07_Appendix_C__Example_Application_Model.md` | 5,262 | 122 |

**理由：这 7 篇是定义文档的**全部内容**——不读它们，这一页除了「语料未写」以外写不出任何东西。
**这 7 篇里有 6 篇本身又是索引**（只有 Appendix C 有正文）。
**除此之外没有读第三层。**

**⭐ 本页**没有**读的：`## 语法 / 参数` 节自己声明的那 8 篇**——
它们是定义文档的**孙辈**（比上面那 7 篇深一层）。**8 篇逐条列出**：

- `02.10.03.03.07_Reprobe_data.md`
- `02.10.03.03.09.02_Logging_text_data_in_the_TEST_TXT_field.md`
- `02.10.03.03.11_Force_closing_out_lot_or_wafer_level_in_application_model.md`
- `02.10.03.05.05_Version_Update_Record__VUR.md`
- `02.10.03.05.08_Site_Description_Record__SDR.md`
- `02.10.03.05.12_Pattern_Sequence_Record__PSR.md`
- `02.10.03.05.27_Generic_Data_Record__GDR.md`
- `02.10.03.05.28_Activity_Trace_Event_Record__ATER.md`

**后果说清楚**：**本页 `## 是什么` 里那三个机制（reprobe bin / `TEST_TXT` /
`FORCE_MODEL_LEVEL_LOGGING_COMPLETE`）与那五张记录表，
本页的了解只到 `## 语法 / 参数` 节里逐字收的那几段为止**——
**那几段之外它们还写了什么（上下文、别的选项、别的例子），本页一个字都没有。**

**本页没做的：**

- **整棵子树 73 篇，本页读了 8 篇。** `02.10.03` 下共 **73 篇 md**——
  **即本页覆盖了约 11%。剩下 65 篇一篇没读。**
- **一张图都没看**——**这 8 篇里一个 `![` 都没有**（本页逐篇查过），
  **所以这一页没有任何视觉依据，也不缺。**
- **`## Functional changes` 一次没出现**（8 篇全查过）——
  **所以这一页的 `## 版本` 只有「没有」这一条事实。**
- **29 种记录类型，一种都没查过它们各是什么。** 上面那张表**只有缩写**，
  全名只在 Appendix A 的清单里；**每种记录有哪些字段、什么时候写、写什么，本页没有。**
- **那 5 张记录表（`VUR` / `SDR` / `PSR` / `GDR` / `ATER`）本页是从 `## 语法 / 参数` 节里读的**，
  **不是从它们各自的 raw 读的**——**所以本页不知道那 5 段是不是那 5 篇的全部。**
- **`## 语法 / 参数` 节的段名本身就是一条线索，本页照实记下**：
  它写着「本节 **15,395 字符逐字取自** <定义文档> 及其子主题 <上面那 8 篇>」，
  而 **定义文档自己列的 7 篇并没有出现在这 8 篇里**——
  **即脚本递归了两层，收的是**孙辈**。**（这一段是脚本写的，不是本页写的。）
- **没有交叉验证任何别处的文档**（§11：本页只写读到的这 8 篇里有的）。
  **尤其：[[stdf]] 那一页本页没读**——**本页讲的是「这个 formatter 和它吐出来的记录」，
  不是 STDF 这个格式本身。**
- **`layer: gui` / `stage: results` 不是这 8 篇写的**——**它们都没有 `## Application`
  这类自我定位段**，这个归属是本 wiki 的既有划分。

> ⚠️ **这 8 篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 定义文档没有正文。** 逐字（它的完整正文，标题之后只有这一行块）：
> `#### Subtopics` + 7 行链接。
> ——**同一棵子树里 `Standard Test Data Format (STDF) Overview`（`#### Subtopics` + 1 行）、
> `Starting and Stopping the Formatter`（+ 5 行）也都是这个形态**；
> **只有 `Appendix C` 一篇有散文与代码。**
> **不是本页找不到正文，是本文档确实没有。本页照实记。**
>
> **② `## 语法 / 参数` 节里，一条列表项和紧跟的 `Note` 粘在了一起。** 逐字（`member_func` 那一串的最后一项）：
> `- testtype()Note member_func entries are optional.`
> ——**`testtype()` 后面直接跟 `Note`，没有空格、没有换行、没有标点。**
> **（推断）原文应是一列表项 `testtype()` 加一条独立的 `Note`，
> 转换时 `Note` 被并进了上一行；依据只是这一串里其余 11 项都是干净的。
> 这是推断，原文没写对的是什么。本页引文照原样。**
>
> **③ 同一段代码里，同一个对象有四种写法。** 逐字并列（Appendix C 的代码块）：
> `WAFER_ID = CONST_INPUT({PH_wafer_id});` /
> `{ DEVICE [({WAFER_ID}),()] die:` /
> `STDF_FILE = CONST_INPUT(/tmp/{LOT_ID}.{wafer_id}.stdf);` /
> `* wafer_id = DIALOG_INPUT / REGEXP(string);`
> ——**`WAFER_ID` / `{WAFER_ID}` / `{wafer_id}` / `{PH_wafer_id}` 四种形态同时出现**，
> **而 `LOT_ID` 那一路没有对应的 `PH_` 形态。**
> **语料没有解释这四种的区别（大小写是否承载语义、`PH_` 是什么），本页不猜，也不替它统一。**
>
> **④ `## 语法 / 参数` 节里 `obj.` 后面多一个空格。** 逐字（`TEST_TXT` 那三行代码的第三段）：
> `obj. member_func().TEST(parameters);`
> ——**同节另两段写的是 `TESTSET().member_func()` 与 `TestSet.member_func()`，都没有这个空格。**
> **本页照原样引。**
>
> **⑤ `SDR` 那张表里十六处脚注链接，有一处没链上。** 逐字并列（同一张表里）：
> 十五处写 `` - Application model variable`2)`（raw: `#_69127__fn2`）: ``，
> 而 `DIB_TYP` 那一处写 `- Application model variable2:`
> ——**前者是「正文 + 上标链接 + 冒号」，后者把上标链接整个丢了、`2` 直接粘在 `variable` 后面。**
> **本页照实并列。**
>
> **⑥ 那张大表在语料里被压平成「一格一段」。** 逐字（`VUR` 那一段的一小截；
> **` / ` 是行界，空行也照数**）：
> `UPD_NAM` / （空行） / ` |` / （空行） /
> `The version after STDF V4 to which this data log conforms.` / （空行） / ` |` / （空行） /
> `Variable-length character string.` / （空行） / `Maximum 255 characters.`
> ——**一个字段的四格被拆成十一行，`|` 自己单独占一行。**
> **本页的表格化转述是按字段重排的**；**`## 语法 / 参数` 节里那一份才是原样，要看原样看它。**
>
> **⑦ 压平之后还留下了「整行只有一个 `|`」与「末尾一个空 `| |`」。** 逐字并列：
> ` |`（**整行只有一个空格加一个管道符**——就是上面 ⑥ 里那种行；
> `SDR` 那张表的第一行也是这个形态）与
> `   | One-byte unsigned integer.  | |`（**末尾多一个空 `| |`，前面还有三个空格**）。
> **本页照实并列。**
>
> **⑧ 这 8 篇里没有 §11.2 ① 那种编码损坏**（本页逐篇查过：8 篇里汉字 0 个、`鈥` 0 处）。

`verified: doc-only`
