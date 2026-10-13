---
type: object
title: RDI_Configure file
layer: file
stage: testmethod
tags: [rdi-configure-file, smartrdi, testmethod, keyword-file, rdi, utility-line, technology-file, testflow-variable]
related: [smartrdi, testflow-variable, sequencer-controlled-utility-lines, utility-line-view, vector-setup-file, technology-file, smartcalc, smartrdi-vector-and-protocol-programming]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# RDI_Configure file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,085 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.13.04.01_Example_of_keyword_setups_in_the_RDI_Configure_file.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.04.02_getRdiConfig.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Example of keyword setups in the RDI Configure file）

```
// UTIL setup
UTIL_BLOCK = 12,34,5,6,7,8
UTIL_FRAM = UL_FRAM1,UL_FRAM3,UL_FRAM5,UL_FRAM6,UL_FRAM7,UL_FRAM8
UTIL_SCLK = UL_SCLK,UL_SCLK3,UL_SCLK,UL_SCLK,UL_SCLK,UL_SCLK
UTIL_SINP = UL_SINP,UL_SINP3,UL_SINP,UL_SINP,UL_SINP,UL_SINP
UTIL_SOUT = UL_SOUT,UL_SOUT3,UL_SOUT,UL_SOUT,UL_SOUT,UL_SOUT
UTIL_CTRL_MAX_SPEED = 2e6
UTIL_DYN_MASK_UNSPECIFIED_PIN = FALSE
UTIL_DYN_MASK_INACTIVE_SITE = TRUE
# UTIL_PADDING_RPTV_FLAT

// SmartVec setup
VEC_EDIT_MODE = VTT
DEFAULT_EMAP_LOCATION = TP
DEFAULT_SMV_READ_MODE = EMAP
SMV_DIGCAP_AUTO_BURSTUPLOAD = FALSE
SMV_VEC_MEM_TYPE = SHMEM
USER_NAMED_PATTERN_CONTENT_CHECK = FALSE

// Default pin status
DEFAULT_STATUS_PIN = pinA,pinB
DEFAULT_STATUS_INDEX = 0,1

// Setup name
ANALOG_SET_NAME_MD5 = TRUE
BURST_NAME_MD5 = TRUE

// PPMU setup
PPMU_DEFAULT_RELAY = NO
PPMU_DEFAULT_VALUE_MODE = SA

// Pass or fail per label
PER_LABEL_FUNC_RESULT_MODE = FLBL
PER_LABEL_FUNC_RESULT_NO_BREAK_VEC = TRUE

// ORE setup
ORE_FILE = " "
ENABLE_ORE = FALSE
ORE_TEMPLATE_BY_USER_CODE = TRUE

// Upload
DC_BURST_SITE_UPLOAD = TRUE
DIGCAP_ADAPTIVE_RESULT_SIZE = TRUE
DIGCAP_BURST_SITE_UPLOAD = TRUE

// Debug
REPORT_RESULT_IN_SINGLE_MODE = TRUE
ENABLE_RDI_INFO_LOG_FILE = TRUE

// SMC execution
DISABLE_SMC_EXEC_GLOBAL = TRUE
DISABLE_SMC_EXEC_SHORT_BURST = TRUE

// Production
SETUP_UPTODATE = TRUE

// Alarm handling for DCVI
ALARM_HANDLING_DCVI_ENABLE = TRUE
ALARM_HANDLING_DCVI_SETUP_FILE = "testmethod/RDI_Alarm_setup"

// Others
VEC_MODE_SAMPLING_WAIT = MSET
PURE_GENERATION_MODE = TRUE
ROUTING_SETUP_FILE = "testmethod/routing_tool_states_1.xml"
# ROUTING_SETUP_FILE = ./routing/Routing_Configure.xml
ALLOW_SAME_RESULT_ID_ACROSS_RDI_BLOCK = TRUE
# TMU_TIMEOUT_50ms = FALSE
```

### Syntax（取自子主题 getRdiConfig）

```
string rdi.getRdiConfig(string optionName);
```

Parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/151016.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Return Value（取自子主题 getRdiConfig）

The option value returns.

### Example（取自子主题 getRdiConfig）

```
rdi.getRdiConfig("RF_CAL_DEFAULT");
```

For the option RF_CAL_DEFAULT, one of the three values will return: ON, OFF, and SYSTEM_CAL.

<!-- 语法节 end -->

## 是什么

**一句话：RDI_Configure 文件是 SmartRDI 的「默认设置」文件——一个放在 device 的 `testmethod` 文件夹里、
用关键字写成的纯文本文件，而且整份都是可选的。** 原文：

> 「The RDI_Configure file is used to configure some default settings to be used when programming with SmartRDI. The RDI_Configure file is in folder testmethod of the loaded device. An RDI_Configure.Template file will be generated in the first run, which has all options with comments.」

**这一句里有三条能直接用的东西**：

1. **位置**：device 的 `testmethod` 文件夹。
2. **第一次跑会自动生成 `RDI_Configure.Template`，而且「has all options with comments」**——
   **所以「怎么写」有现成的模板可抄，不必从这篇文档拼。**
3. **它管的是「默认值」**（`default settings`），不是必须项。**原文在最后一格末尾把这句话说死了**：

> 「Note The RDI_Configure file and the settings that can be set in the file are all optional. You can omit any settings in the file or even omit the complete file if no settings are required.」

**「一个字的设置都不写，甚至整个文件不放，程序也照样跑」——这是本篇最重要的一句免责声明。**
（**它的位置很怪，见「出处」⑨。**）

**开头那句还点名了它管的两件事**：

> 「These settings include setting the default pin status and configuring the sequencer鈥慶ontrolled utility.」

**`sequencer鈥慶ontrolled` 是语料的乱码，应为 `sequencer-controlled`**——**这正是 schema §11.2 ①
记的那一类（GBK 解码的 UTF-8），本页照实抄，见「出处」①。**

### 47 个关键字，分 14 组

原文的 `## Definition of keywords in the RDI_Configure file` 是**一张大表**（一句
「The following tables list all of the applicable keywords and their definitions.」），
**按 14 个用途分组**。**照抄成清单**（**关键字名逐字，说明挑有规则的引**）：

| 组 | 关键字 | 值得单独记的 |
|---|---|---|
| **Alarm handling for DCVI** | `ALARM_FAIL_WARNING` / `ALARM_HANDLING_DCVI_ENABLE` / `ALARM_HANDLING_DCVI_SETUP_FILE` | 前两个是布尔，第三个是**报警设置文件的路径** |
| **Default pin status** | `DEFAULT_STATUS_INDEX` / `DEFAULT_STATUS_PIN` | 都是逗号分隔的列表，**两两对应** |
| **For debugging** | `ENABLE_RDI_INFO_LOG_FILE` / `REPORT_RESULT_IN_SINGLE_MODE` | `ENABLE_RDI_INFO_LOG_FILE` 开后在 `device/testmethod` 下生成 `RDI_INFO_LEVEL_x.log` |
| **For production** | `SETUP_UPTODATE` | 决定 setup tool 里**有没有 `*`**（原文连正反两行的写法都给了） |
| **Offline Result Emulation (ORE) setup** | `ENABLE_ORE` / `ORE_FILE` / `ORE_FOLDER` / `ORE_TEMPLATE_BY_USER_CODE` / `ORE_TEMPLATE_DATA_FILE_SIZE_THRESHOLD` | **`ENABLE_ORE` 有三个值**，见下 |
| **Pass or fail per label** | `PER_LABEL_FUNC_RESULT_MODE` / `PER_LABEL_FUNC_RESULT_NO_BREAK_VEC` | 前者只有两个值：`ERMP` 或 `FLBL`（**默认 `ERMP`**）；后者开起来有 **8 cycles 的硬门槛** |
| **PPMU setup** | `PPMU_DEFAULT_RELAY` / `PPMU_DEFAULT_VALUE_MODE` / `FAST_PPMU_LEVEL_TRANSFER` | `SA` 或 `BADC`（**默认 `BADC`**） |
| **Result upload** | `DC_BURST_SITE_UPLOAD` / `DIGCAP_ADAPTIVE_RESULT_SIZE` / `DIGCAP_BURST_SITE_UPLOAD` | 两个 upload 开关都注明了「不支持 hidden upload」 |
| **Routing setup** | `ROUTING_ACK_CHECK` / `ROUTING_SETUP_FILE` | 前者查 PMUX01 卡的 I2C 应答位 |
| **Setup naming** | `ANALOG_SET_NAME_MD5` / `BURST_NAME_MD5` | 都是「在名字尾部追加 MD5」，目的是**重复的 burst 不重新生成** |
| **smartVec setup** | `DEFAULT_EMAP_LOCATION` / `DEFAULT_SMV_READ_MODE` / `SMV_DIGCAP_AUTO_BURSTUPLOAD` / `SMV_VEC_MEM_TYPE` / `USER_NAMED_LABEL_CONTENT_CHECK` / `VEC_EDIT_MODE` / `SMV_IGNORE_COMMENT` | 7 个，**变化最频繁的一组** |
| **SMC execution** | `DISABLE_SMC_EXEC_GLOBAL` / `DISABLE_SMC_EXEC_SHORT_BURST` | 两个都是「禁止」，**默认都为 `FALSE`（= 不禁止）** |
| **Utility line setup** | `UTIL_BLOCK` / `UTIL_CTRL_MAX_SPEED` / `UTIL_DYN_MASK_INACTIVE_SITE` / `UTIL_DYN_MASK_UNSPECIFIED_PIN` / `UTIL_FRAM` / `UTIL_PADDING_RPTV_FLAT` / `UTIL_SCLK` / `UTIL_SINP` / `UTIL_SOUT` | 9 个，**本页最长的一组** |
| **Others** | `ALLOW_SAME_RESULT_ID_ACROSS_RDI_BLOCK` / `INACTIVE_SITE_AUTO_MASK` / `PURE_GENERATION_MODE` / `VEC_MODE_SAMPLING_WAIT` | 四个杂项 |

**注意这 14 组只覆盖 47 个关键字**——**`## Functional changes` 里点名的另外 7 个关键字在这张表里
一个条目都没有**（见「版本」节）。

### 最容易踩的六个关键字

**1. `ENABLE_ORE` 有三个值，不是两个。** 原文：

> 「In online mode, to automatically disable ORE, you can set this keyword as  ENABLE_ORE = TRUE_OFFLINE. With this setting, ORE works only for offline.」

| RDI_Configure option | Offline mode | Online mode |
|---|---|---|
| `ENABLE_ORE = TRUE` | Enable ORE | Enable ORE |
| `ENABLE_ORE = FALSE` | Disable ORE | Disable ORE |
| `ENABLE_ORE = TRUE_OFFLINE` | Enable ORE | Disable ORE |

（**这张表在原文里被压坏了，见「出处」⑦。**）**另外「在线时开着 ORE」不是报错，是给一条提醒**：

> 「If the ORE feature is enabled for online, SmartRDI delivers an error message for reminder.」

**2. `PURE_GENERATION_MODE = TRUE` 会让所有读取函数返回垃圾值。** 原文：

> 「When this option is set to TRUE, SmartRDI generates setups (pattern, burst, dc event, analog set and so on) only and skips pattern execution and results upload.」

> 「Note All `rdi...getXXX()` calls such as `getVector()`, `getReadBit()`, `getWaveform()` return dummy results. The size of result arrays = 0.」

**「省掉第一次跑的 Viasco bind，用来只生成、不执行」是它的用途**——**但代价是那一轮所有 `getXXX()` 都不可信。**

**3. `PER_LABEL_FUNC_RESULT_NO_BREAK_VEC = TRUE` 有 8 cycles 的硬门槛。** 原文：

> 「Note This mode requires a pattern length not less than eight cycles for patterns inside a `RDI_BEGIN()`/`RDI_END()` block, because in BFLM mode, each pattern in the burst must generate eight or more cycles […]. So when this mode is enabled, a specified pattern length less than eight cycles is ignored and all patterns generated by SmartRDI have at least eight cycles. There are exceptions, for example `vecLength()` of the `smartVec()` class, where SmartRDI reports an error for a user setting with insufficient pattern length, rather than ignoring the setting. User labels less than eight cycles cause an error as well.」

**三条不同的后果要分清**：**一般 pattern 长度不够 → 静默抬高到 8 cycles；`smartVec()` 的 `vecLength()` 不够 → 报错；
user label 不够 8 cycles → 也报错。**

**4. `UTIL_BLOCK` 的连号写法是 `-`，不是逗号。** 原文：

> 「Specify the utility block to be controlled by the pattern. Use commas to separate groups; do not use commas to define ganged groups. Use the "-" character to link the ganged block numbers.」

**逗号是「分组」的分隔符，连号要用 `-`**——**这两个符号的用途是相反的，而且原文那三条例子里有一条注释是错的**（见「出处」⑤）。
**另外 `-` 这个写法本身是 7.10.3 才有的**（变更表最后一条），**但 `UTIL_BLOCK` 那一格把它当成唯一的写法讲，没有版本提示。**

**5. 两个 `UTIL_DYN_MASK_*` 的 TRUE/FALSE 不是同一个意思，原文的措辞也不一样。**
**照抄原文的对照**（`UTIL_DYN_MASK_INACTIVE_SITE`）：

> 「FALSE indicates that utility pins at inactive sites will STILL be changed by pattern; TRUE indicates that utility pins at inactive sites will NOT be changed by pattern.」

（`UTIL_DYN_MASK_UNSPECIFIED_PIN`）：

> 「FALSE indicates that unspecified utility pins in the same control pattern will be set to OFF; TRUE indicates that unspecified utility pins in the same control pattern will KEEP their states.」

**一个说的是「改不改」，一个说的是「置 OFF 还是保持」**——**语义一致，措辞两样**，
**而且 `UTIL_DYN_MASK_UNSPECIFIED_PIN` 还带一句兼容性提示**：

> 「To keep the compatibility with old test programs, use FALSE for this keyword.」

**它的默认值是 `TRUE`（2.5.1 改的），而「老程序兼容」要 `FALSE`——这两句是直接冲突的口径，原文并排放着。**

**6. `DEFAULT_EMAP_LOCATION` 的默认值在两个版本里不一样。** 原文：

> 「- TP indicates an error map location in the test processor memory of the channel.」
> 「- RAM indicates that the error map is located in the vector memory of the channel.」
> 「If not specified, the default error map location is RAM, which is the vector memory, because this location provides a higher upload speed.」

**紧跟着一句降级规则和一句版本注**：

> 「In case the vector memory is insufficient for the test, the location switches to TP, which is the test processor memory.」

> 「Note TP is the default value before SmartRDI 2.4.5. RAM is the default value since SmartRDI 2.4.5.」

**（注意这句 `Note` 在原文里是直接粘在 `See also emapLocation().` 后面的，见「出处」⑧的精神。）**

### 路径规则：一篇里三种写法，连「基准目录」都换词

**这是本篇最容易被忽略的一类不一致**——**同一个「文件路径相对谁」的问题，原文对五个地方给了五种说法**：

| 关键字 / 变量 | 原文的路径规矩 |
|---|---|
| `RDI_CONFIGURE_FILE`（testflow 变量） | 「You can put your customized RDI_Configure files to an absolute path or paths.」 |
| `ALARM_HANDLING_DCVI_SETUP_FILE` | 「A file path relative to the root path of the loaded device is to be specified.」**（只说了相对）** |
| `ROUTING_SETUP_FILE` | 「An absolute file path or a file path relative to root path of the loaded device is to be specified.」 |
| `ORE_FILE` | 「absolute path or a relative path. A relative path is based on the current test device's root directory. For example, ./myORE.xml is current_device_folder/myORE.xml.」 |
| `ORE_FOLDER` | 「The path can be an absolute path or a relative path. A relative path is based on the current test device directory.」 |

**基准目录在三格里换了三个词：`the loaded device` / `the current test device` / `device path`。**
**「它们是不是同一个目录」原文没说，本页不替它断。**

### testflow 变量 `RDI_CONFIGURE_FILE`

原文给了它一小节（**导航里也单独列了一节，不属于那 14 组**）：

> 「This testflow variable allows you to select a customized RDI_Configure file for a testflow. Therefore, you can have different setups in different RDI_Configure files for different testflows.」

> 「Use this variable to specify a RDI_Configure file for a testflow each time. You can specify as many RDI_Configure files to testflows as required. You can put your customized RDI_Configure files to an absolute path or paths.」

**它的用途是「多套配置并存」**：一个文件管默认，想给某个 testflow 换一套就用这个变量指过去。
**原文在两处提到它**——`ALARM_HANDLING_DCVI_SETUP_FILE` 那格也用「因为你可以用 `RDI_CONFIGURE_FILE` 给每个 testflow 指一个文件」来解释「为什么不同 testflow 能有不同的报警设置」。

### 配套的两个子主题

本篇有两个子主题，**内容都已经被脚本抽进了本页「语法 / 参数」节**（节里标了「取自子主题」）：

- **`Example of keyword setups in the RDI_Configure file`**——一份完整的示例文件（**本页「语法 / 参数」节最上面那 60 多行**）
- **`getRdiConfig()`**——在代码里读回某个关键字的值：

```
string rdi.getRdiConfig(string optionName);
```

原文的参数说明只有一句「The option name to be queried.」，返回值说明只有一句「The option value returns.」，
**例子里查的是 `RF_CAL_DEFAULT`，可选值是 `ON` / `OFF` / `SYSTEM_CAL`**——
**注意 `RF_CAL_DEFAULT` 这个关键字在正文那 47 个里没有条目。**

## 典型用法

> **原文没有 `## Procedure` 段**，也没有编号步骤。
> **规则散在关键字说明里**，本节收成六条。

**1. 要改默认值，就在 `testmethod` 文件夹里放一个 `RDI_Configure`。**
**不知道怎么起头就先跑一次，抄 `RDI_Configure.Template`**（原文说它「has all options with comments」）——
**这是原文给的唯一一条「怎么开始写」的路径，比这份参考文档本身更适合当起点。**

**2. 只想给某一个 testflow 换设置，用 testflow 变量 `RDI_CONFIGURE_FILE` 指一套别的文件**（可以用绝对路径），
**不必改那份全局的。**

**3. 拿不准的关键字，删掉就是默认值。** 每个布尔的说明里都带一句默认值（**说法有五六种，见「出处」⑩**），
**而整份文件是可省的**——**所以「不写」永远是一个合法选择，不是漏做。**

**4. 代码里要读回设置，用 `rdi.getRdiConfig("<optionName>")`。** 返回值是字符串，**所以拿到 `"TRUE"` 这种文本时要自己判**——
**（推断）依据是它的签名 `string rdi.getRdiConfig(string optionName);` 和例子里 `ON` / `OFF` / `SYSTEM_CAL` 三个字面值；
原文没有展示怎么把结果转成布尔。**

**5. 开某些功能前先确认配套条件。** 原文在两处写了「还要求别的设置」：

- `DC_BURST_SITE_UPLOAD`：「In the Technology File, a setting is required to use this capability:」`"Fast Transfer Buffer" > 128K`
- `PER_LABEL_FUNC_RESULT_NO_BREAK_VEC`：pattern 长度不低于 8 cycles（见上）
- `SMV_DIGCAP_AUTO_BURSTUPLOAD`：「Using burstUpload() for data read by SmartVec in the digital capture mode can significantly decrease test time. By default, all SmartVec's digital capture data on a certain pin in one `RDI_BEGIN()/RDI_END()` block are uploaded as one burst, and the `burstUpload()` function set in the code is ignored.」

**最后这一条是「配置文件盖掉代码」的例子，看代码找不到原因时往这里查。**

**6. 升级时要回头核默认值。** 本篇的 `## Functional changes` 里有 5 条是「默认值改了」，
**其中 4 条集中在 SmartRDI 2.5.0**——**同一份 RDI_Configure 文件在不同版本上跑出来的行为可能不一样，
而文件本身没有任何版本标记。**

## 和谁有关

- [[smartrdi]] — **本文件服务的对象**。原文第一句就是「settings to be used when programming with SmartRDI」
- [[testflow-variable]] — **`RDI_CONFIGURE_FILE` 变量的宿主页**。
  **原文说它「allows you to select a customized RDI_Configure file for a testflow」**，
  **但「这个变量在哪声明、怎么写」本篇没有**（那在 testflow 侧）
- [[sequencer-controlled-utility-lines]] — **`UTIL_*` 那 9 个关键字指向的正是它**
  （**注意原文这里就是乱码**：`the sequencer鈥慶ontrolled utility`）
- [[utility-line-view]] / [[set-utility-lines]] / [[get-utility-lines]] / [[utility-card]] —
  **utility line 的查看 / 设置 / 读取 / 硬件页**（**本页没读它们，不主张具体关系**）
- [[vector-setup-file]] — **同为「给工程设默认值」的文件页**，
  而且 `SMV_VEC_MEM_TYPE` / `VEC_EDIT_MODE` / `SMV_IGNORE_COMMENT` 这几个关键字调的是 vector 那一侧的行为
- [[technology-file]] — **`DC_BURST_SITE_UPLOAD` 要求它里面有 `"Fast Transfer Buffer" > 128K`**；
  `DEFAULT_EMAP_LOCATION` 也点名了它（「the RAM location is related to the "result area" configuration in the technology file of SmarTest」）
- [[smartcalc]] / [[smartcalc-framework]] / [[smc-background-process-locks-config]] —
  **`DISABLE_SMC_EXEC_GLOBAL` / `DISABLE_SMC_EXEC_SHORT_BURST` 管的是 SMC 执行**
- [[smartrdi-vector-and-protocol-programming]] / [[pattern-explorer]] / [[setup-management-tool]] —
  **`VEC_EDIT_MODE` / `SETUP_UPTODATE` 指向的界面那一侧**（**未读**）
- [[rdi-call-requires-begin-end-block]] — **同族约束页**：
  本篇多个关键字都以 `RDI_BEGIN()`/`RDI_END()` 块为界限（**未读，不主张具体关系**）
- [[smartrdi-2.4.5]] / [[smartrdi-2.5.0]] / [[smartrdi-7.10.0]] … — **版本页**，
  见「版本」节的 24 条变更
- 原文里**没读**的链接目标（节选）：`Changing the default pin status with SmartRDI`、
  `SmartRDI: Alarm handling for DCVI`、`Using Offline Result Emulation in SmartRDI`、
  `Pass/Fail per label without break vectors`、`Controlling burst site upload`、
  `SmartRDI: DUT board connections control by Routing Tools`、`Routing Tools editors`、
  `Postfix in burst pattern names`、`Pin Scale 1600 error map size`、
  `Compression factor for overview Error Map`、`Example of keyword setups in the RDI_Configure file`

## 版本

原文有 `## Functional changes` 段，**24 条，全部照抄**：

- **Introduced in SmartRDI 2.1.0**
- SmartRDI 2.2.0: New keywords RF_OPTMIZE_SEQUENCE and RF_STIM_PATH_LOSS_ADJUSTMENT.
- SmartRDI 2.3.0: New keywords PPMU_PURE_VMEAS_2P2_COMPATIBLE_MODE and PMUX_X_CTRL.
- SmartRDI 2.3.1: New keywords PPMU_DEFAULT_VALUE_MODE and PPMU_DEFAULT_RELAY.
- SmartRDI 2.4.0: New keywords SETUP_UPTODATE and VEC_EDIT_MODE.
- SmartRDI 2.4.1: New keywords PER_LABEL_FUNC_RESULT_MODE and SMV_VEC_MEM_TYPE.
- SmartRDI 2.4.3: New keywords ANALOG_SET_NAME_MD5, BURST_NAME_MD5, REPORT_RESULT_IN_SINGLE_MODE, and VEC_MODE_SAMPLING_WAIT.
- SmartRDI 2.4.3: Support the generation of an RDI_Configure.Template file in the testmethod folder in the first run.
- SmartRDI 2.4.4: New keywords ALLOW_SAME_RESULT_ID_ACROSS_RDI_BLOCK, COMBINED_FREQ_LIST, DEFAULT_SMV_READ_MODE, and UTIL_CTRL_MAX_SPEED.
- SmartRDI 2.4.5: During the 1st run, SmartRDI is able to judge whether the burst pattern needs to be regenerated when BURST_NAME_MD5 is set to FALSE.
- SmartRDI 2.4.5: New keywords USER_NAMED_LABEL_CONTENT_CHECK, DEFAULT_EMAP_LOCATION, ENABLE_RDI_INFO_LOG_FILE, DISABLE_SMC_EXEC_GLOBAL, DISABLE_SMC_EXEC_SHORT_BURST, SMV_DIGCAP_AUTO_BURSTUPLOAD, UTIL_DYN_MASK_UNSPECIFIED_PIN, UTIL_DYN_MASK_INACTIVE_SITE, DIGCAP_ADAPTIVE_RESULT_SIZE, and TMU_TIMEOUT_50ms.
- SmartRDI 2.5.0: New keywords DC_BURST_SITE_UPLOAD, DIGCAP_BURST_SITE_UPLOAD, PURE_GENERATION_MODE, PER_LABEL_FUNC_RESULT_NO_BREAK_VEC, ENABLE_ORE, ORE_FILE, and ROUTING_SETUP_FILE.
- SmartRDI 2.5.0: Four keywords have their default values changed: PPMU_DEFAULT_VALUE_MODE (from "SA" to "BADC"), PER_LABEL_FUNC_RESULT_MODE (from "FLBL" to "ERMP"), DEFAULT_SMV_READ_MODE (from "EMAP" to "DIGCAP"), VEC_MODE_SAMPLING_WAIT (from "MSET" to "PATTERN").
- SmartRDI 2.5.1: The default value for UTIL_DYN_MASK_UNSPECIFIED_PIN is changed to "TRUE".
- SmartRDI 7.5.0: New keywords UTIL_PADDING_RPTV_FLAT, PMUX_CTRL_MAX_SPEED, ALARM_HANDLING_DCVI_ENABLE, and ALARM_HANDLING_DCVI_SETUP_FILE.
- SmartRDI 7.5.0: New testflow variable RDI_CONFIGURE_FILE.
- SmartRDI 7.5.1: New keyword ORE_TEMPLATE_BY_USER_CODE.
- SmartRDI 7.5.2: New keywords ALARM_FAIL_WARNING and ORE_FOLDER; new value TRUE_OFFLINE for ENABLE_ORE.
- SmartRDI 7.5.3: New keywords FAST_PPMU_LEVEL_TRANSFER and ROUTING_ACK_CHECK.
- SmartRDI 7.6.0: New keyword SMV_IGNORE_COMMENT.
- SmartRDI 7.10.0: New keyword ORE_TEMPLATE_DATA_FILE_SIZE_THRESHOLD; PPMU_PURE_VMEAS_2P2_COMPATIBLE_MODE is removed; and SMV_DIGCAP_AUTO_BURSTUPLOAD = TRUE by default.
- SmartRDI 7.10.3: New keyword INACTIVE_SITE_AUTO_MASK; "-" character can be used in the UTIL_BLOCK definition.

**五条要点**：

1. **`Introduced in SmartRDI 2.1.0` 是真的版本号，不是哨兵值。** 它写的是 `in`，
   不是 `Introduced before SmarTest 6.3.2` 那种「本文档集覆盖之前就有」的说法（schema §11.2 ②）。
   **而且这份变更表是这份语料里少见的「真·变更日志」：24 条带版本号、带关键字名、
   带 `from "X" to "Y"` 的默认值变化。**
2. **版本号在 2.5.1 之后直接跳到 7.5.0**，中间一条都没有。
   **（推断）这不是漏记，是 SmartRDI 换了版本编号体系**——**依据只有「中间 5 个大版本空白」这个事实本身；
   原文没有任何一句解释这次跳号。本页不替它断。**
3. **变更表里点名的 7 个关键字，正文的 47 个条目里一个都没有**：
   `RF_OPTMIZE_SEQUENCE`、`RF_STIM_PATH_LOSS_ADJUSTMENT`、`PPMU_PURE_VMEAS_2P2_COMPATIBLE_MODE`、
   `PMUX_X_CTRL`、`COMBINED_FREQ_LIST`、`TMU_TIMEOUT_50ms`、`PMUX_CTRL_MAX_SPEED`。
   **其中 `PPMU_PURE_VMEAS_2P2_COMPATIBLE_MODE` 有 7.10.0 的「is removed」条目可解释，
   其余 6 个只有「新增」记录、没有定义。** 详见「出处」⑬。
4. **4 条默认值变更和正文表里的默认值是**对得上的**（本页逐条核过）**：
   `PPMU_DEFAULT_VALUE_MODE` 表里写「If not specified, BADC is used by default.」、
   `PER_LABEL_FUNC_RESULT_MODE` 写「If not specified, ERMP is used by default.」、
   `DEFAULT_SMV_READ_MODE` 写「If not specified, the default read mode is DIGCAP.」、
   `UTIL_DYN_MASK_UNSPECIFIED_PIN` 写「If not specified, the default value is TRUE.」
   ——**四处都反映的是 2.5.0 / 2.5.1 之后的值。**
   **换句话说：正文表描述的是「当前版本」，旧版本的行为只能从变更表倒推。**
5. **7.10.0 那条 `and SMV_DIGCAP_AUTO_BURSTUPLOAD = TRUE by default` 没说它是从什么改过来的**，
   而其余 5 条默认值变更都写了 `(from "X" to "Y")`。**照实记，不替它补。**

**注意这个页面的 `## Functional changes` 就是关键字清单的第二份索引**——
**47 条定义 + 24 条变更合起来才是一份完整的关键字表；只读其中一份都会漏。**

## 出处

`sources:` 一篇：

`02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md`
（TDC `146692.htm`，共 127 行）

**本页没做的**：

1. **只读了这一篇。**
2. **两个子主题没有读**：`Example of keyword setups in the RDI_Configure file` 和 `getRdiConfig()`。
   **它们的正文都被脚本抽进了本页「语法 / 参数」节**（节里标了「取自子主题」），
   **本页引用时写明了来源，但没有读那两篇文档本身**——
   **所以「示例文件里每一行的用意」「`getRdiConfig()` 的完整行为」本页都没有。**
3. **原文里的链接目标一个都没读**（清单见「和谁有关」最后一条）。
   **所以「默认引脚状态怎么设」「alarm handling 是什么」「ORE 怎么用」「路由工具怎么用」这些
   配套话题，本页一个字都没有**——**本篇只讲「哪个关键字填什么」。**
4. **没有实测**：本页没有写过 RDI_Configure 文件，没有跑过 SmartRDI，
   **没有验证过任何一个默认值在机台上的实际行为**，
   **也没有验证过 `-` 连号写法、`TRUE_OFFLINE`、8 cycles 门槛这些规则的后果**。
   **本页所有结论都是文档事实（`verified: doc-only`）。**
5. **原文没有一张图**，本页没有任何来自图的结论。
6. **那 47 个关键字的定义没有整表搬进来**：**原文的表在页面上是「一格里一行」的形态
   （见「出处」⑧），逐字搬进来会等于把整篇文档复制一遍，与 §3 相悖。**
   **本页给的是「14 组 + 47 个名字」的清单 + 挑出来逐字引的规则**；
   **要逐字定义，得回原文那张表。**

> ⚠️ **本篇的语料瑕疵，照实记，一处都没替它改**：
>
> ① **GBK 解码的 UTF-8 乱码（schema §11.2 ① 记的那一类），本篇 7 处**：
> `sequencer鈥慶ontrolled`
> ——**应为 `sequencer-controlled`**（`鈥慶` 是 U+2011 非断字连字符 `‑` 加字符 `c` 被按 GBK 解码后的产物）。
> **7 处的位置**：开头那句 `configuring the sequencer鈥慶ontrolled utility`，
> 以及 `UTIL_DYN_MASK_INACTIVE_SITE`、`UTIL_DYN_MASK_UNSPECIFIED_PIN`、
> `UTIL_FRAM`、`UTIL_SCLK`、`UTIL_SINP`、`UTIL_SOUT` 六格里的
> `for the sequencer鈥慶ontrolled utility lines`。
> **照实记，一处都没改——改了就等于把语料事实改成我的转述（§11）。**
> ② **例子里的关键字名和定义表对不上**：子主题例子的 `// SmartVec setup` 那段写的是
> `USER_NAMED_PATTERN_CONTENT_CHECK = FALSE`，
> **而正文定义表和 2.4.5 的变更条目里，这个关键字叫 `USER_NAMED_LABEL_CONTENT_CHECK`**
> （`PATTERN` vs `LABEL`）。**两者只差一个词，本页照抄两处，不判哪个是现名。**
> ③ **例子里的枚举值不在文档给的值域里**：例子里是 `VEC_EDIT_MODE = VTT`，
> 而正文那一格说「Specify this option to select one of vector edit modes: VECD or VEC_TRANSFER_TASK.」
> ——**`VTT` 三选一里没有。**
> **（推断）`VTT` 像是 `VEC_TRANSFER_TASK` 的缩写，但原文没有给这个缩写，本页不替它认。**
> ④ **`ALARM_FAIL_WARNING` 那一格自己和自己矛盾，还带一个冠词错**：
> 说明的第一句是 `Disable alarm warnings when alarm fails.`，
> 紧接着的正文却是 `If you set ALARM_FAIL_WARNING = TRUE, SmartRDI throws an warning message when the alarm fails, for example, Test Suite:: SuiteName, Burst Label:: BurstName, Alarm Pin ("PinName") failed!.`
> ——**首句说「关掉报警」，正文说 `TRUE` 是「抛出报警」，方向相反**；
> 同句的 `an warning` 应为 `a warning`。**照抄，不替它改。**
> ⑤ **`UTIL_BLOCK` 第一条例子的注释和它的规则、以及和第二条例子的注释都对不上**：
> 原文那一格先立规矩「Use commas to separate groups; do not use commas to define ganged groups.
> Use the "-" character to link the ganged block numbers.」，然后给三条例子：
> `UTIL_BLOCK = 123, 4, 5, 6 // blocks 1, 2, and 3 are ganged`、
> `UTIL_BLOCK = 1-2-3, 4, 5, 6 // blocks 1, 2, and 3 are ganged`、
> `UTIL_BLOCK = 165-166-167, 168, 169, 170 // blocks 165, 166, and 167 are ganged`。
> ——**第一条既不符合自己上面那句规则（它用的是逗号不是 `-`），注释又和第二条逐字相同。**
> **看着像注释被复制到了上一行。本页照抄，不替它改。**
> ⑥ **`DIGCAP_ADAPTIVE_RESULT_SIZE` 的描述句和它的值域对不上**：
> 描述写 `Specify the result size to be retrieved when the number of samples actually captured is less than the expected number.`
> （**「指定结果大小」**），**但它的取值和默认值都是布尔的**（`The default value is FALSE.`），
> 后面两段也是在讲 TRUE / FALSE 的两种行为。**照实记，不替它改。**
> ⑦ **`ENABLE_ORE` 的取值表被压坏，还多出一个空单元格**：表头是
> `| RDI_Configure option  | Offline mode  | Online mode |`，
> 三行数据被拆成了「单元格内容单独成行」的形态（`Enable ORE` 一行、`   | Enable ORE |` 又一行），
> **最后一行是 ` | ENABLE_ORE = TRUE_OFFLINE  | Enable ORE  | Disable ORE  | |`——
> 末尾多一个 `|`，也就是多一个空单元格。** 本页在「是什么」里按语义重排成了三行，
> **但那是我为了让读者看懂而做的排版，不是原文的形态。**
> ⑧ **全篇的表格结构和标题层级都丢了**：
> 正文每张表都是「一格里一行」的形态（` | Keyword  | Description |` 之后每格各占一行，
> 格子之间只有一行孤立的 ` |`）；**14 个分组标题被压成带两个前导空格的行**
> （`  Alarm handling for DCVI`、`  For debugging`、`  Others` 等），
> **和表里关键字名的形态几乎一样**；`## Keyword groups` 那张两列导航表也被 ` |` 行包着。
> **这一篇 465 行里有相当一部分是这个结构开销。本页照实引，不重排。**
> ⑨ **那句最重的免责声明粘在了最后一个关键字的格子里**：
> `…  |     Note The RDI_Configure file and the settings that can be set in the file are all optional.
> You can omit any settings in the file or even omit the complete file if no settings are required.`
> ——**它在 `VEC_MODE_SAMPLING_WAIT` 那一格的末尾，紧接着 `## Related information`。**
> **一条管全篇的话，位置在最后一张表的最后一格里，只扫小标题的人会漏掉。**
> ⑩ **默认值的说法在同一篇里有六种以上**：
> `The default value is X` / `If not specified, X is used by default` /
> `This configuration is set to X by default` / `The default state is X` /
> `X is used by default` / `The default choice is X` / `The default error map location is X`。
> **照实记，本页不统一措辞。**
> ⑪ **两个 `UTIL_DYN_MASK_*` 的 TRUE/FALSE 语义写法不同**（一个讲「改不改」、一个讲「置 OFF / 保持」），
> **而它们在一起用时是同一套掩码机制**（原文两格都写「implemented based on the utility mask capability
> in SmarTest 7.4.2」）。**本页并列照抄，不替它统一。**
> ⑫ **路径规矩一篇里三到五种**，连基准目录都换了词（`the loaded device` / `the current test device` /
> `device path` / `current_device_folder`）。**见「是什么」最后那张表；本页不判它们是不是同一个目录。**
> ⑬ **变更表点名的 7 个关键字在定义表里没有条目**：
> `RF_OPTMIZE_SEQUENCE`、`RF_STIM_PATH_LOSS_ADJUSTMENT`、`PPMU_PURE_VMEAS_2P2_COMPATIBLE_MODE`、
> `PMUX_X_CTRL`、`COMBINED_FREQ_LIST`、`TMU_TIMEOUT_50ms`、`PMUX_CTRL_MAX_SPEED`。
> **其中 `TMU_TIMEOUT_50ms` 在正文里唯一一次出现，是子主题例子里被注释掉的一行
> `# TMU_TIMEOUT_50ms = FALSE`；`PPMU_PURE_VMEAS_2P2_COMPATIBLE_MODE` 有 7.10.0 的
> 「is removed」条目，其余 6 个只有「新增」记录、没有定义。**
> **另外 `RF_OPTMIZE_SEQUENCE` 的 `OPTMIZE` 拼写可疑**——**本页不判它是关键字名就这样还是笔误，
> 因为它在定义表里没有条目可对照。**
> ⑭ **子主题例子里有几点原文没解释**：`ORE_FILE = " "`（一个空格）；
> `# UTIL_PADDING_RPTV_FLAT` 和 `# TMU_TIMEOUT_50ms = FALSE` 两行被注掉；
> **同一个例子里 `//` 和 `#` 两种注释符并用**（`// UTIL setup` 与 `# ROUTING_SETUP_FILE = …`）,
> **两种注释符是否等价、能不能混用，原文一个字都没说。**
> ⑮ **`EMAP` 那句 `Note` 粘在 `See also` 后面**：
> `See also emapLocation().Note TP is the default value before SmartRDI 2.4.5. RAM is the default value since SmartRDI 2.4.5.`
> ——**版本注和上一句的链接之间没有任何分隔。照抄，不替它断开。**

`verified: doc-only`
