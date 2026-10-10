---
type: object
title: Command Set Programming Interface
layer: L3
stage: testflow
tags: [L3, testflow, ci-cpi, flag, system-flag, variable, bin-statistics, message-catalog, data-logging, tpi]
related: [testflow, flag, flags-page, testflow-variable, bin, test-suite, data-logging-profiles, test-suite-control-api, tpi-program-routines, mapping-testflow]
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05_Command_Set_Programming_Interface.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.02.02_Production_Flags.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.02.03_User_Flags.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Command Set Programming Interface

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,344 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05_Command_Set_Programming_Interface.md>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.03_System_Flag.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.07_Application_model_file_string.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.14_Command_Set_Message_File.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.19_Set_the_data_logging_profiles.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.23_Retrieve_the_Testsuite_Name.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.32_Retrieving_bin_statistics.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Miscellaneous › System Flag）

Controlling the sites to be tested in multisite test

```
INT32         MaxSitesEnabled;
int         site,i;
long         status;

/* query current multi-site values */
GetNumberOfSites(&MaxSitesEnabled);

/* ------------------------------------------------------------------
 * Initialization:  disable all sites first (to get a known state)
 * ------------------------------------------------------------------
 */
for(site=1; site<=MaxSitesEnabled;site++)
{
   SetSystemFlagOfSite(CI_SITE_SETUP,site,CI_SITE_NOT_INSERTED);
}

/*--------------------------------------------------------------------------
 * Set the desired Sites to be Tested:  here, the example sets sites 1 & 3
 *--------------------------------------------------------------------------
 */
SetSystemFlagOfSite(CI_SITE_SETUP,1,CI_SITE_INSERTED_TO_TEST);
SetSystemFlagOfSite(CI_SITE_SETUP,3,CI_SITE_INSERTED_TO_TEST);
```

### Example（取自子主题 Miscellaneous › Application model file string）

```
#include <libcicpi> // Required by these two APIs.
...
char new_wafer_id[2];
GetModelfileString("Temperature",new_wafer_id);
char* LB_ID_var="debug_LB";
SetModelfileString("LB_ID", LB_ID_var);
...
```

### Example（取自子主题 Miscellaneous › Command Set Message File）

- Create the messages/string lines in any text file using the format as described by the gencat Linux command:

file myfile.msg

2001 this is message 2001

2002 this is message 2002

- Generate the message file using the command:

/opt/hp93000/soc/prod_env/lbin/install_cs -m myfile.msg

- Messages in the catalog file may now be accessed with the MsgGetMsg routine, for example:

fprintf(stderr, "%s", MsgGetMsg(2001));

generates the string this is message 2001 on the report window.

You might also find it useful to refer to the Linux man pages for catopen, catclose and catget.

### Syntax（取自子主题 Miscellaneous › Set the data logging profiles）

```
void SetSamplingProfiles( const char * on_profile, const char * off_profile) ;
```

This function registers two data logging profiles to be used for sampling.

The system flag datalog_sample_size allows specifying that only one out of N testflow executions is logged into STDF. If on_profile and off_profile are defined by calling this function, the on_profile is activated when a testflow execution is to be logged and the off_profile is activated when a testflow execution is not to be logged.

on_profile and off_profile are profiles in the profiles subdirectory of the device directory.

### Parameters（取自子主题 Miscellaneous › Set the data logging profiles）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/103746.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：on_profile | The profile that is activated when a testflow execution is to be logged.

### Syntax（取自子主题 Miscellaneous › Retrieve the Testsuite Name）

```
long GetTestsuiteName(char *testsuiteName)
```

### Example（取自子主题 Miscellaneous › Retrieve the Testsuite Name）

The following example shows how this function is used:

```
char current_testsuite_name[CI_CPI_MAX_TESTSUITE_LEN];
.
.
.
/* The testsuite name is printed in the report window */
GetTestsuiteName(current_testsuite_name);

fprintf(stdout, "Current testsuite is %s\n", current_testsuite_name);
```

### Example（取自子主题 Miscellaneous › Retrieving bin statistics）

```
CI_CPI_BIN_CURSOR cursor;
  for(cursor = GetBinFirst(); cursor != CI_CPI_INVALID_BIN_CURSOR; cursor = GetBinNext(cursor))
  {
    CI_CPI_BIN_DESCRIPTOR binDescriptor;
    int deviceCount = GetBinStatistics(cursor, &binDescriptor);
    fprintf(stderr, "%d devices were binned to Bin %s\n", deviceCount, binDescriptor.bin_name);
    int site;
    for(site = 0; site < CI_CPI_MAX_SITES; site++)
    {
      fprintf(stderr, "Site %d: %d devices\n", site + 1, binDescriptor.dies_per_site[site]);
    }
  }
```

<!-- 语法节 end -->

## 是什么

**CPI（Command Set Programming Interface）是「测试程序跑的时候，从程序内部去读写 flag 与变量」的那套例程。**
定义文档一共两句，第一句就是全部定位：

> 「The Command Set Programming Interface (CPI) provides a set of routines for accessing SmarTest flags and variables during the execution of a test program, plus a number miscellaneous utilities.」

> 「The CPI also includes TPI (Test Programming Interface) functions.」

⚠️ **第一句里 `a number miscellaneous utilities` 少了一个 `of`**（原文如此，见「出处」①）。
**本页照抄，不替它补。**

**两句合起来是两件事**：**主线是 flag 与变量的访问**（`during the execution of a test program`
——**运行期，不是离线工具**）；**第二条把 TPI 函数也算在 CPI 里**。

### 五个子主题，本篇一篇都没给你内容

| 子主题（原文的 `#### Subtopics`） | 按名字看，答案在哪 |
|---|---|
| Flag Classifications | flag 分几类 |
| Access Routines | 访问例程 |
| Flag Access | 具体怎么访问 flag |
| Miscellaneous | 杂项（本页语法节抽到的六段全在这一支底下） |
| Return Codes | 返回码 |

**本篇正文就是上面那两句，五个子主题的正文一篇没读**（见「出处」）；
**2026-09-20 补进了 `Access Routines` 底下的两篇子文档**（Production Flags / User Flags），
**那五个子主题页本身仍然没读**。
所以**这一页的定位是**：「CPI 是什么、它的 API 落在哪一支底下」——
**另外补录了那两篇子文档给出的 15 个函数签名**（见「flag 读写函数的清单与签名（2026-09-20 补录）」）。
**但参数含义、返回码取值、flag 名清单，本页仍然一个字都没有**——**那两篇也只给签名。**

### 语法节能读出的三件事

本页「语法 / 参数」节 3,320 字节，取自**定义文档 + 六篇子主题**（`System Flag`、
`Application model file string`、`Command Set Message File`、`Set the data logging profiles`、
`Retrieve the Testsuite Name`、`Retrieving bin statistics`，全部挂在 `Miscellaneous` 底下）。

**① 它真是 C 例程，落地形态是符号前缀。** 语法节里出现的符号常量与类型，
前缀是两套：**`CI_`**（`CI_SITE_SETUP`、`CI_SITE_NOT_INSERTED`、`CI_SITE_INSERTED_TO_TEST`）
与 **`CI_CPI_`**（`CI_CPI_MAX_TESTSUITE_LEN`、`CI_CPI_BIN_CURSOR`、`CI_CPI_INVALID_BIN_CURSOR`、
`CI_CPI_BIN_DESCRIPTOR`、`CI_CPI_MAX_SITES`）。**用之前要 `#include <libcicpi>`**：

> 「#include <libcicpi> // Required by these two APIs.」

**② site 的编号有两套约定，同页并存。**
`System Flag` 那段例**从 1 数**：

> 「for(site=1; site<=MaxSitesEnabled;site++)」

而 `Retrieving bin statistics` 那段例**从 0 数、打印时才 +1**：

> 「for(site = 0; site < CI_CPI_MAX_SITES; site++)」

> 「fprintf(stderr, "Site %d: %d devices\n", site + 1, binDescriptor.dies_per_site[site]);」

**两段都是文档原文。本页并列，不替它们调和**——真要写代码时，**这两处得自己确认哪个适用**。

**③ 它管的「变量」是 model file 里的字符串**，不是 testflow 变量：
`GetModelfileString("Temperature",new_wafer_id)` 与 `SetModelfileString("LB_ID", LB_ID_var)`
这一对，配的是 application model file 里的字符串（`Application model file string` 那段）。

### 图证：本页没有任何图

**本页全文（含脚本生成的语法节）引不到一张 `.png`**——定义文档那两句没有图，
语法节里六段子主题例也一张图都没有。
**2026-09-20 补进 `sources:` 的两篇也查过**：两篇 `.md` 与它们各自的上游 `.htm`
（`raw/44868.htm`、`raw/44871.htm`）**都没有任何图引用**——**所以补录之后本页仍然一张图都没有**。
**所以不是「本页的图够不着」，是本页没有图可看**（§11.4：没看图就写「本页没用图」才是真的；
**理由不许编**）。**本页没有任何来自图的结论。**

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**，
所以「怎么用」只能是**那六段例各自证明 CPI 能做的一件事**：

| 要做的事 | 语法节里那段例给了什么 |
|---|---|
| **控制这次测哪些 site** | `GetNumberOfSites(&MaxSitesEnabled)` 先取总数，**再把所有 site 置成 `CI_SITE_NOT_INSERTED`（先得到一个已知状态）**，最后把要测的置成 `CI_SITE_INSERTED_TO_TEST`——例子里设的是 site 1 与 site 3 |
| **读写 model file 里的字符串** | `GetModelfileString("Temperature", new_wafer_id)`、`SetModelfileString("LB_ID", LB_ID_var)`；**注释写明这两条 API 需要 `#include <libcicpi>`** |
| **装一个消息目录，然后按号取消息** | 先按 `gencat` 格式写 `myfile.msg`（`2001 this is message 2001`），再用 `/opt/hp93000/soc/prod_env/lbin/install_cs -m myfile.msg` 生成，之后 `MsgGetMsg(2001)` 取回那句话 |
| **按抽样开关切换 data logging profile** | `SetSamplingProfiles` 两个参数分别是 `on_profile` 与 `off_profile`，一次注册两个 profile；**由系统 flag `datalog_sample_size` 决定某一次 testflow 执行记不记进 STDF**，记则启用 on、不记则启用 off；两个 profile 是 device 目录下 `profiles` 子目录里的文件 |
| **取当前 test suite 名** | `GetTestsuiteName(char *)`，填进调用方给的缓冲区（例子里用的是 `CI_CPI_MAX_TESTSUITE_LEN` 那么长的一个数组） |
| **遍历 bin 统计** | `GetBinFirst()` / `GetBinNext(cursor)` 走一遍，`GetBinStatistics(cursor, &binDescriptor)` 一次取一个 bin 的数量与描述，`binDescriptor.dies_per_site[site]` 是**按 site 分的数** |

**这六段是「入口」，不是「参考」**：**这六段例每一条的完整签名、参数、返回码，本页都没有**
（见「出处」）——**说的是语法节里那六段 Misc 例**；**下一节补录的 15 个 flag 读写函数签名是另一批，不在六段例里**。

## flag 读写函数的清单与签名（2026-09-20 补录）

**这一节是本页第一版缺的那块。** 第一版 `sources:` 里只有那篇 819 字节的父主题桩，
**真正给签名的两篇子文档当时不在 `sources:` 里**，所以第一版一个签名都没写——
**不是没查到，是不许写**。两篇补进 `sources:` 之后，本节照 raw 逐字抄录（见「出处」）。

### Production Flags —— 10 个（`02.09.01.08.05.02.02_Production_Flags.md`）

**raw 原文分 `## get` 与 `## set` 两段，每段五个。下面 10 行照 raw 的行序与写法，未重排、未合并、未删减：**

```
long GetTestsuiteFlag(char *tsname, char *flag, long *value)
long GetTestsuiteFlagOfSite(char *tsname, char *flag, long site, long *value)
long GetTestflowFlag(char *flag, long *value)
long GetSystemFlag(char *flag, long *value)
long GetSystemFlagOfSite(char *flag, long site, long *value)

long SetTestsuiteFlag(char *tsname, char *flag, long value)
long SetTestsuiteFlagOfSite(char *tsname, char *flag, long site, long value)
long SetTestflowFlag(char *flag, long value)
long SetSystemFlag(char *flag, long value)
long SetSystemFlagOfSite(char *flag, long site, long *value)
```

> ⚠️ **数出来是 10 个，顺序就是 raw 的顺序**：get 组 `Testsuite → TestsuiteOfSite → Testflow → System → SystemOfSite`，
> set 组同序，**两组都是五个**。**本页没有重排、没有删减。**
> 这一条特意写出来，是因为本工程在 `wiki/stages/testflow.md` 上**踩过一次「漏一个 + 按主角重排」**：
> 那一页原先只列了 9 个、顺序也被按「本页主角是 testflow」重排过（**2026-09-20 更正过**）。
> **本页与更正后的那一页逐行比对：都是 10 个、顺序相同，两边没有分歧。**

**按作用域读一遍**（下表只是归类，方便看；**raw 里没有这张表，顺序一律以上面代码块为准**）：

| 作用域 | 取 | 置 |
|---|---|---|
| test suite（[[test-suite]]） | `GetTestsuiteFlag` / `GetTestsuiteFlagOfSite` | `SetTestsuiteFlag` / `SetTestsuiteFlagOfSite` |
| testflow（[[testflow]]） | `GetTestflowFlag` | `SetTestflowFlag` |
| system | `GetSystemFlag` / `GetSystemFlagOfSite` | `SetSystemFlag` / `SetSystemFlagOfSite` |

**「`OfSite` = 多 site 时指定 site」是（推断）**，依据是同名函数多出一个 `long site` 参数；
**raw 没有写这两个函数各是干什么的**，两篇都没有参数说明。

**raw 在这 10 个之后还有一句：**

> 「Note that you can use the function GetTestsuiteName described later in this chapter to find out in which testsuite a user procedure was executed.」

**这句里的 `GetTestsuiteName` 就在本页语法节里**（`long GetTestsuiteName(char *testsuiteName)`，
取自 `Retrieve the Testsuite Name` 那一段）——**raw 说它「described later in this chapter」，
本页的两块因此能对上**（文档事实）。

> ⚠️ **语料瑕疵 A（本页补录的两篇里的第 1 处；照实记，本页没替它改）**：`SetSystemFlagOfSite` 的最后一个参数在 raw 里是
> `long *value`（**指针**），而它同组的另外四个 Set 例程都是 `long value`。
> **本页逐字抄成 `long *value`，不判哪个对。**
> **回查上游 `raw/44868.htm`**：里面同样写着 `long SetSystemFlagOfSite(char *flag, long site, long *value)`
> ——**`.htm` 里就是这个**。所以**它不是转换坏的字，是上游 TDC 自己写的不一致**
> （按 §11.2 ⑥ 那张表：**`.htm` 里就是错的 → 救不回来，只能照实记录**）。**（文档事实）**

### User Flags —— 5 个（`02.09.01.08.05.02.03_User_Flags.md`）

**同样分 `## get` / `## set`，get 三个、set 两个。照 raw 逐字、按行序：**

```
long GetUserFlag(char *flag, long *value) // For one site currently in focus.
long GetUserFlagOfSite(char *flag, long site, long *value)
long GetAllTestflowUserFlags( CI_CPI_USER_FLAG_LIST *user_flag_list)

long SetUserFlag(char *flag, long value) // For one site currently in focus.
long SetUserFlagOfSite(char *flag, long site, long *value)
```

**两条行尾注释 `// For one site currently in focus.` 是 raw 自带的，本页连着抄。**
**`GetAllTestflowUserFlags` 的 `(` 后面那个空格也是 raw 的**（原文 `GetAllTestflowUserFlags( CI_CPI_USER_FLAG_LIST *user_flag_list)`），
**没有替它删**。**`CI_CPI_USER_FLAG_LIST` 也是本页第一次见到的 `CI_CPI_` 前缀符号**，
接得上「是什么」①里那两套前缀。

### User Flags 与 Production Flags 是什么关系

**同级兄弟，不是替代**：两篇住在同一个目录 `02_System_reference/02.09_Test_Program_Management/`，
文件名前缀都是 `02.09.01.08.05.02`（`.02` 与 `.03`），**各自独立给出自己的签名，raw 里谁也没引用谁**。

（推断）**这一支就是定义文档列的第二个子主题 `Access Routines`**——依据是 `02.09.01.08.05` 那五条子主题
按列出顺序是 Flag Classifications / Access Routines / Flag Access / Miscellaneous / Return Codes，
编号 `01`–`05` 与之一一对应。**raw 没有明写这个对应，所以这是推断。**

| | Production Flags（`02.09.01.08.05.02.02`） | User Flags（`02.09.01.08.05.02.03`） |
|---|---|---|
| 管哪一批 | **production flag**：test suite / testflow / system 三级 | **user flag**：用户自己那一批 |
| 函数数 | **10**（get 5 + set 5） | **5**（get 3 + set 2） |
| 带 `OfSite` 的 | Testsuite、System | User |
| 多出来的函数 | 无 | `GetAllTestflowUserFlags`——**「一次取回全部 testflow user flag」是按名字的（推断）**，raw 没给它的说明 |
| `## Related information` | **没有这一段** | 有，指向 `02.09.01.08.05.04.04_User_Flag.md` |
| `## Functional changes` | **没有这一段** | 有，两条，见下 |
| 参数含义 / 返回码 / flag 名清单 | **都没有** | **都没有** |

**两篇都只给签名**——**没有参数含义表、没有返回码表、也没有 flag 名的清单**。
所以「这些 flag 具体叫什么、各取什么值」**本页仍然答不了**（见「出处」）。
**flag 名清单的落点应是两篇各自的 `Related information` 指过去的定义页**
（User Flags 篇指的是 `02.09.01.08.05.04.04_User_Flag.md`，**本页没读**；
Production Flags 篇**连这一段都没有**，**该往哪找 raw 没说**）。

**User Flags 篇自己带的版本条目**（raw `## Functional changes` 两条）：

> 「Introduced before SmarTest 6.3.2」

> 「SmarTest 7.1.3: New function GetAllTestflowUserFlags().」

⚠️ **第一条要按 §11.2 ② 读**：`before` 这一族是**哨兵值**，意思是
**「在本文档集覆盖范围开始之前就已经有了」**，**不是「6.3.2 新增了 user flag 例程」**——
全语料 2,677 条可用性行都写同一个版本号、措辞全是 `before`，**照字面读会造出一批格式齐整的假新增记录**。
**第二条是实的**：`GetAllTestflowUserFlags` 是 SmarTest 7.1.3 才加的，
**所以上面那 5 个里它最年轻**（文档事实）。

> ⚠️ **语料瑕疵 B（本页补录的两篇里的第 2 处；照实记，本页没替它改）**：`SetUserFlagOfSite` 的最后一个参数在 raw 里同样是
> `long *value`（**指针**），而同组的 `SetUserFlag` 是 `long value`——**与 Production Flags 篇里
> `SetSystemFlagOfSite` 那处是同型的不一致**。**上游 `raw/44871.htm` 里也写着 `long *value`**，
> **同样不是转换坏的。** **本页两处都照 raw 抄。**

**⚠️ 本节与本页「版本」节的关系**：本页「版本」节说「本文档没有 `## Functional changes` 段」——
**那句话说的是定义文档 `02.09.01.08.05`，仍然成立**；**这里记的是 User Flags 那一篇自己的版本条目**。
（脚本只抽 `Syntax` / `Parameters` / `Example`，`## Functional changes` **进不了语法节**，
所以语法节里看不到它——**这不是缺漏**。）

## 和谁有关

**这是一页定位页**，所以关系比别页更要紧——**它的内容全在别人的页里**。

**入边只有 3 条 / 3 篇**（`inline` 口径，`extract/edges.jsonl`），**全在 `02.09.01.08` 这一章内部**：

- `02.09.01.08_Creating_production_functions_with_command_set_interface`（第 14 行）——**章首页**。
- `02.09.01.08.03.01.03.01_CPI_Functions`（第 8 行）——**这一篇的名字就是「CPI 函数」**，
  ⚠️ **它才是「CPI 有哪些函数」的落点，本页没读**（见「出处」）。
- `02.09.01.08.03.02.05_Additional_Information`（第 12 行）。

> **3 条入边是很低的。** 本页 `layer: L3`、`stage: testflow`，
> 但**本页的定义文档几乎不承载信息**（两句），所以**低入边反映的是「没人需要链这两句」**，
> 不是「它不重要」——**它的重要性在它没写出来的那五个子主题里**。

**出边 5 条**，就是那五个子主题（`Flag Classifications` / `Access Routines` / `Flag Access` /
`Miscellaneous` / `Return Codes`）。

- [[testflow]] — 本页 `stage: testflow`；**CPI 读写的那套 flag，定义与文件侧都在那一阶段**
- [[flag]] / [[flags-page]] — **同一批 flag 的 GUI 侧与概念页**；
  `mapping-testflow` 把 GUI `on`/`off` ↔ 文件与 API 的 `1`/`0` 那一条钉在 `02.08.04.32.01.02.07.01`
  上，**那一格的 API 侧就该由本页补**
- [[testflow-variable]] / [[testflow-file]] — **flag 与变量存在文件哪一段**；
  本页语法节里**没有**任何一句讲文件格式
- [[bin]] — 语法节里 `Retrieving bin statistics` 那段例的对象；**bin 自己另有页**
- [[data-logging-profiles]] — `SetSamplingProfiles` 那一段例的另一半
  （profile 文件在 `profiles` 子目录里这件事**只有那一段写过**）
- [[test-suite-control-api]] — **容易与本页混的一页**：它也读写 test suite flag，但是**外部客户端**
  那一侧；本页是**测试程序内部**那一侧。**两套接口不是同一个**（这一点写在这里，因为从页名看不出来）
- [[tpi-program-routines]] — **TPI 函数**：定义文档第二句说 `The CPI also includes TPI`，
  **但那批函数的具体清单本页没有**，那页是它们的落点
- [[mapping-testflow]] — 同阶段的对照表页；它把本页当作 testflow flag / system flag 两行的 L3 格

> ⚠️ **这一条 2026-09-20 改了说法。** 原文写的是「**flag 读写函数的清单与签名，本页不列**」，
> 并说「**要看签名去那一页**」——**那个理由是「那两篇子文档不在本页 `sources:` 里」**。
> **两篇补进 `sources:` 之后，理由不成立了**：**清单现在就在本页**
> （见「flag 读写函数的清单与签名（2026-09-20 补录）」，**10 个 + 5 个**）。
> **本页与 `wiki/stages/testflow.md` 那一块逐行比对过：都是 10 个、顺序相同，不存在两种说法。**

## 版本

**本文档没有 `## Functional changes` 段。**

**本页语法节里也没有任何版本条目**——脚本只抽 `Syntax` / `Parameters` / `Example` 三种段标记，
`## Functional changes` 不在其中。**所以本页 `## 版本` 是空的，这是事实，不是缺漏。**

## 出处

`sources:` 三篇：

- `02_System_reference/02.09_Test_Program_Management/02.09.01.08.05_Command_Set_Programming_Interface.md`
  （TDC `44860.htm`，18 行 / 819 字节）——**本页最早唯一的来源，正文就是那两句 + 五条子主题**。
- `02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.02.02_Production_Flags.md`
  （TDC `44868.htm`，32 行 / 967 字节）——**2026-09-20 补进 `sources:`**。
- `02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.02.03_User_Flags.md`
  （TDC `44871.htm`，29 行 / 751 字节）——**2026-09-20 补进 `sources:`**。

**⚠️ 本页第一版 `sources:` 只有上面第一篇**（那篇 819 字节的父主题桩，**它自己一个签名都没有**）。
**两篇子文档当时不在 `sources:` 里**，所以**第一版按「只写 `sources:` 里有的」这条规矩，
一个函数签名都没写**——**不是没查到，是不许写**。
**2026-09-20 两篇补进 `sources:` 之后，那 15 个签名才写进
「flag 读写函数的清单与签名（2026-09-20 补录）」一节**（**10 个 + 5 个**）。
**第一版那句「本页不列清单、不列签名」因此作废**——「是什么」与「和谁有关」两节里相应的句子**已一并改掉**，
**没有留着一句已经不成立的旧说法**。

**本节另外沿用的口径**：**两条 `long *value` 的一致性判据（是转换坏还是上游坏）回查了这两篇对应的上游
`.htm`**（`raw/44868.htm`、`raw/44871.htm`）——§11.2 ⑥ 给的判法就是「**去看上游那个 `.htm`**」。

**本页没做的**：

- **五个子主题的正文一篇没读**：`02.09.01.08.05.01_Flag_Classifications.md`、
  `02.09.01.08.05.02_Access_Routines.md`、`02.09.01.08.05.03_Flag_Access.md`、`02.09.01.08.05.04_Miscellaneous.md`、
  `02.09.01.08.05.05_Return_Codes.md`。**2026-09-20 补读的是 `Access Routines` 底下的两篇子文档**
  （Production Flags / User Flags），**`Access Routines` 这一篇本身仍然没读**。
  **「CPI 到底有哪些函数」的完整清单可能还在 `Access Routines` 或
  `02.09.01.08.03.01.03.01_CPI_Functions` 里，本页答不了**——
  **本页现在有的只是那两篇子文档给出的 15 个签名。**
- **⚠️ 那 15 个签名之外，本页仍然一个字都没有。** **参数含义、返回码取值、flag 名清单**
  两篇子文档**也都没给**——Production Flags 篇正文只有 10 行签名 + 一句讲 `GetTestsuiteName` 的 Note；
  User Flags 篇是 5 行签名 + `## Related information` + `## Functional changes`。
  **按 §11「不臆造 API」，本页不替它们补参数表，也不补返回码。**
  **`02.09.01.08.05.04.04_User_Flag.md` 也没读**——那是 User Flags 篇 `## Related information`
  唯一指向的一篇（**user flag 本体的说明页**）；**那篇里有没有 flag 名与取值，本页不知道**。
  Production Flags 篇**连 `## Related information` 都没有**，**它的定义页该往哪找，raw 没说。**
- **图 0 张**（**本页全文引不到 `.png`**，定义文档与语法节都不含图引用）。
  **2026-09-20 补进 `sources:` 的两篇也查过：两篇 `.md` 与各自的上游 `.htm` 里都没有任何图引用**
  （`.png` / `.gif` / `.jpg` / `<img` 逐个查过，全是 0）。
  **不是「图够不着」，是本页没有图**——理由见「是什么」末一节。
- **本页语法节里 `Parameters` 那一段的形态要说清**：它是**逐字**抄的，但原表已被压平——
  每个单元格单独一行，夹着只剩 `|` 的空行。**那是语法节的既定形态（脚本逐字抽，§4），不是本页改的。**
- **`Flag Classifications` / `Return Codes` 两支本页连名字都没展开**——
  所以「flag 分几类、各类叫什么」本页答不了。
- **没有实跑**：没编译过、没链接过 `libcicpi`、没调过 CPI 或 TPI 的函数。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有改 `wiki/stages/testflow.md`。

> ⚠️ **本篇、语法节、以及 2026-09-20 补进 `sources:` 的两篇里，语料瑕疵照实记、一处都没替它改**（§11.2）：
>
> ① **定义文档第一句少一个 `of`**：
> `The Command Set Programming Interface (CPI) provides a set of routines for accessing SmarTest flags and variables during the execution of a test program, plus a number miscellaneous utilities.`
> ——**`a number miscellaneous` 应为 `a number of miscellaneous`**。本页照抄，不补。
>
> ② **语法节里两个 `### Syntax` 段，一个有分号、一个没有。** `Set the data logging profiles`
> 那段写的是 `void SetSamplingProfiles( const char * on_profile, const char * off_profile) ;`
> （**有分号，而且分号前多一个空格**）；`Retrieve the Testsuite Name` 那段写的是
> `long GetTestsuiteName(char *testsuiteName)`（**没有分号**）。
> **两段都是脚本逐字抽的，原文如此。**
>
> ③ **Linux man page 名写错**：`You might also find it useful to refer to the Linux man pages for catopen, catclose and catget.`
> ——**`catget` 疑为 `catgets`**（那一族函数是 `catopen` / `catclose` / `catgets`）。
> **这条是（推断）**，依据是这三个名字在原文里并列出现、而前两个都对得上标准库；
> **本页照抄原文，不替它改。**
>
> ④ **句子以小写字母开头**：`fprintf(stderr, "%s", MsgGetMsg(2001));` 那段代码块之后，
> 正文写的是 `generates the string this is message 2001 on the report window.`
> ——**`generates` 小写**（它读起来像接着代码块的句子）；同一句里 **`on the report window`
> 用的是 `on`**（同篇别处用的是 `in the Report Window`）。
>
> **本页（含脚本生成的语法节）0 处编码坏字**（`碌` / `渭` / `卤` / `惟` / `鈥` 那几族逐个查过），
> **0 处 `DC/DC power units`**（§11.2⑤ 那一族）。
>
> **2026-09-20 补进 `sources:` 的两篇也逐字查过**：**两篇都是纯 ASCII**
> （`file` 报 `ASCII text, with CRLF line terminators`，**0 个非 ASCII 字符**）——
> **所以那两篇里既没有 ① 那一族编码坏字，也没有 `DC/DC power units` 那一族坏标识符**。
> **那两篇的瑕疵不是坏字，是签名自己前后不一致**（`SetSystemFlagOfSite` 与 `SetUserFlagOfSite`
> 的最后一个参数是 `long *value`，而同组其余例程是 `long value`）——**已回查上游 `.htm`，确认上游就是那样**。
> **两处都照 raw 抄、一处没替它改**，见「补录」里的语料瑕疵 A / B。

`verified: doc-only`
