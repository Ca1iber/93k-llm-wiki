---
type: object
title: LotSummaryGenerator
layer: L1
stage: results
tags: [lot-summary-generator, l1, results, data-logging, gdf, edl, application-model, blc, command-line-tool, summary]
related: [results, edl-file, run, testflow, smartest-7.10.3]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# LotSummaryGenerator

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,883 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Executing the LotSummaryGenerator in the command line

The following example generates the lot summary for the specified data collection file. The output file is /tmp/LotSummary.out. The log file LotSummrayGenerator.log is generated under the home directory of the current user.

```
/opt/hp93000/soc/formatter/bin/LotSummaryGenerator -d /var/opt/hp93000/soc/tm/93k.iI3eAe/DataColltion.
```

### Using LOT_SUMMNARY_PATH_NAME in the application model

```
...
{ lot:
         SCREEN_DIALOG
             Lot_id  = DIALOG_INPUT    /REGEXP(string);

        ACTIONS
            LOT_SUMMARY_PATH_NAME = CONST_INPUT(/tmp/{Lot_id}.lotSum.gdf);
}
...
```

### Using FORCE_SUMMARY_GENERATION_FOR_LEVEL in the application model

In the following example, the summary is generated at `point #1`. If FORCE_SUMMARY_GENERATION_FOR_LEVEL is not used, the lot summary is generated at `point #2`. Make sure to specify the current level name to FORCE_SUMMARY_GENERATION_FOR_LEVEL and put the variable in the post actions section of the level.

```
...
{ lot:
        ACTIONS
              ...
         {DEVICE device:
                      {
                               DEVICE_TEST
                       }
          }

           ACTIONS
                  FORCE_SUMMARY_GENERATION_FOR_LEVEL = CONST_INPUT(lot);
                   --point #1
                   EXEC_INP_CALL(process_lot_summary_file);
                  ...
}   --point #2
...
```

### Using ENABLE_LOT_SUMMARY_GENERATOR in the application model

In this example, ENABLE_LOT_SUMMARY_GENERATOR is used to enable the LotSummaryGenerator. The LotSummaryGenerator will be started at the beginning of the application model execution.

```
...
{ lot:
      SCREEN_DIALOG
          Lot_id  = DIALOG_INPUT    /REGEXP(string);
      ACTIONS
            ENABLE_LOT_SUMMARY_GENERATOR = CONST_INPUT(1);
}
...
```

### Using LotSummaryGenerator with BLC program

```
//header file
...
using namespace std;
using namespace xoc::hvmapi;
pid_t LSGPid = 0;
...
//Define the function to start the LotSummaryGenerator
void startLotSummaryGenerator()
{
  LSGPid = fork();

  if(LSGPid == 0)
  {
      execl("/opt/hp93000/soc/formatter/bin/LotSummaryGenerator", 0);
  }

}

//Define the function to terminate the LotSummaryGenerator
void terminateLotSummaryGenerator()
{
  int childStatus;

  if(LSGPid > 0)
  {
    sleep(5);
    kill(LSGPid, 9);
    waitpid(LSGPid, &childStatus, 0);
  }
}
...
int main(int argc, char* argv[])
{
  ParamList inputParam, outputParam;
  Status  retVal;

 /**********************
  * Initialize the BLC *
  **********************/
  //check if there are input file provided
  if(argc<=1)
  {
    cout<<"Please sepecify a BLC input file!!!"<<endl;
    cleanup();
    exit(1);
  }

  startLotSummaryGenerator();
  ...
  /***********************
  * Start the lot level *
  ***********************/
  inputParam.clear();
  inputParam["LEVEL_TYPE"] = "CUSTOM_LEVEL";
  inputParam["LEVEL_NAME"] = "lot";
  retVal = syncCommand("StartLevel", inputParam, LOCAL_SESSION_ID);
  processStatus(retVal);

  for(int lotNum=1; lotNum<=1; lotNum++)
  {
    ...
    //Add new variable LOT_SUMMARY_PATH_NAME for LotSummaryGenerator
    inputParam.clear();
    inputParam["VARIABLE_NAME"] = "LOT_SUMMARY_PATH_NAME";
    inputParam["VARIABLE_VALUE"] = string("/tmp/")+lotID+string(".lotSum.gdf");
    retVal = syncCommand("SetApplicationVar", inputParam, LOCAL_SESSION_ID);
    processStatus(retVal);
    ...
    //Add new variable FORCE_SUMMARY_GENERATION_FOR_LEVEL for LotSummaryGenerator
    inputParam.clear();
    inputParam["VARIABLE_NAME"] = "FORCE_SUMMARY_GENERATION_FOR_LEVEL";
    inputParam["VARIABLE_VALUE"] = string("lot");
    retVal = syncCommand("SetApplicationVar", inputParam, LOCAL_SESSION_ID);
    processStatus(retVal);
  } //end of the lot level loop
  terminateLotSummaryGenerator();
  cleanup();
  return 0;
}
```

<!-- 语法节 end -->

## 是什么

**LotSummaryGenerator 是 SmarTest 自带的一个命令行工具，把测试结果汇总成 GDF 格式的 lot summary 文件。**
原文第一句把「产物 / 两种输入 / 所在目录」一口气讲完：

> 「This tool is provided to generate the test summary in GDF format from data collection file or
> real-time event data stream. It is located in the directory /opt/hp93000/soc/formatter/bin.」

| 要素 | 值 |
|---|---|
| **产物** | **GDF 格式的 summary 文件** |
| **输入①** | **离线 data collection file（EDL 文件）**——从命令行给 |
| **输入②** | **real-time event data stream**——不给文件时，自己去挂当前 SmarTest 会话 |
| **位置** | `/opt/hp93000/soc/formatter/bin` |
| **形态** | **命令行工具**（不是 GUI 工具、不是 test method API） |

**产物被两个名字指称，本页并列、不替它统一**：第一句写的是 `test summary`，
而讲实时模式的那句写的是 `generate the lot summary file in real time`。
工具自己的名字里是 `Lot`。**两条口径（`test summary` / `lot summary`）原文各写各的**（§11.5）。

### 两种输入模式

| 模式 | 怎么触发 | 原文 |
|---|---|---|
| **离线（EDL 文件）** | 命令行给 `-d` | `Provide an offline data collection file (EDL file) as input when executing LotSummaryGenerator from the command line.` |
| **实时（event stream）** | **不给** `-d` | `If you do not provide the data collection file when executing the LotSummaryGenerator, it will try to attach to the current SmarTest session and generate the lot summary file in real time.` |

离线模式产出多少份，原文也写了：

> 「LotSummaryGenerator will then retrieve data from the file and generate the lot summary for
> all the test program and testflow executions recorded in the file.」

**即：一个 EDL 文件里记了多少次 test program / testflow 执行，就出多少份汇总**——
不是「一个文件一份」。

**实时模式有两个前置条件，缺一个都不出数据**（原文逐字）：

> 「If there's no SmarTest running, error messages will be printed and the LotSummaryGenerator exits.
> Make sure the system flag log_events_enable is set to on. Otherwise, no summary data will be generated.」

| 条件 | 不满足时会怎样 |
|---|---|
| **有 SmarTest 在跑** | 没有 → **打印错误信息并退出**（原文是 `exits`，**不是等待、不是重试**） |
| **系统标志 `log_events_enable` = on** | 不是 on → `no summary data will be generated`（**一条都不产生**） |

> ⚠️ **`log_events_enable` 这个名字只在上面那一句里出现过一次**，
> **原文没有说它在哪设、怎么查、默认值是什么**——**语料未写**。

**命令行的生命周期是绑在会话上的**：

> 「You can also execute LotSummaryGenerator from the command line as below.
> The running of this tool will stop automatically when the current SmarTest session is terminated.」

**即：命令行起来的那个进程，当前 SmarTest 会话一结束就自己停**——
不用（也不能）靠 `-l` 那个日志文件去等它。

### 三个应用变量——**其中两个管「文件在哪」，一个管「要不要跑」**

| 变量 | 作用 | 原文 |
|---|---|---|
| `LOT_SUMMARY_PATH_NAME`（**raw 里多数处拼作 `LOT_SUMMNARY_PATH_NAME`**，见「出处」⚠️ ①） | 给**每个 level** 单独指定一份 summary 文件的路径与名字 | `LOT_SUMMNARY_PATH_NAME is used to specify the path and name of a separate summary file for each level in the application model file or BLC program.` |
| `FORCE_SUMMARY_GENERATION_FOR_LEVEL` | 让汇总**在 level loop 结束之前**就生成 | `FORCE_SUMMARY_GENERATION_FOR_LEVEL is used to generate the summary file before the level loop is completed in application model and BLC program.` |
| `ENABLE_LOT_SUMMARY_GENERATOR` | 控制工具**是否启用** | 见下 |

**`ENABLE_LOT_SUMMARY_GENERATOR` 的判据是「变量在不在」，不是「值是多少」**——原文逐字：

> 「ENABLE_LOT_SUMMARY_GENERATOR controls whether the LotSummaryGenerator is enabled.
> If this variable exists in the application model file, the LotSummaryGenerator will be started
> at the beginning of the application model execution. It will be shut down after the application
> model is finished.」

**注意 `exists` 这个词**：原文给的条件是「**变量存在**」，
而例子给的是 `ENABLE_LOT_SUMMARY_GENERATOR = CONST_INPUT(1);`（值 `1`）。
**「值写成 0 会不会等于关」——语料未写**，本页不判。

**两个方向的分工是原文明确划的：**

| 你用什么跑 | 谁负责起停工具 | 谁负责设那两个变量 |
|---|---|---|
| **application model 文件** | **`ENABLE_LOT_SUMMARY_GENERATOR` 存在**就自动起，application model 结束就停 | 写在 application model 里 |
| **BLC program（BLC client）** | **自己在 BLC 里起、自己停** | 用 `SetApplicationVar` API 设 |

逐字（后一半）：

> 「If you use BLC client instead of application model file, you need to start and terminate
> the LotSummaryGenerator in the BLC client. You can define the variable LOT_SUMMNARY_PATH_NAME and
> FORCE_SUMMARY_GENERATION_FOR_LEVEL with SetApplicationVar API.」

**BLC 那条路上原文只点名了那两个「文件路径」变量**——
`ENABLE_LOT_SUMMARY_GENERATOR` 在 BLC 段落里**一次都没出现**（那一段的措辞是「自己起停」，
本来也不需要它）。

### 六个命令行选项

原文的语法行（变量名带方括号，**逐字如此**）：

> 「./LotSummaryGenerator [-d DataCollection] [-l logfile] [-o outputfile] [-v] [-m] [-h]」

> 「All the parameters are optional.」

| 选项 | 逐字说明的要点 |
|---|---|
| `-d DataCollection` | **离线 EDL 文件**的路径与名。**不给就转实时模式**（见上）；**挂上了就收实时事件并出 GDF**；没 SmarTest 就跑不出来 |
| `-l logFile` | 日志文件的路径与名。**不给**时 `the log file LotSummaryGenerator.log will be generated in the home directory of the current user.` |
| `-o outputfile` | 输出的 lot summary 文件。**不给**时 `If not specified, /tmp/LotSummary.output is used by default.`；**文件已存在则追加**（见下） |
| `-v` | 让 `LOT_SUMMARY_PATH_NAME` **失效**——只在「**只想把离线文件转成 `-o` 指定的那一个输出**」时用 |
| `-m` | **关掉**追加时打的那行 test program 分隔符 |
| `-h` | 打印用法 + 每个参数的说明 |

**`-d` 的完整原文**（它把两种模式的切换讲得最全）：

> 「Specify the path and name of the offline EDL data collection file. If not specified,
> LotSummaryGenerator will try to attach to the current SmarTest session. If successfully attached,
> it will receive real-time events from SmarTest and generate the lot summary in GDF format.
> If no SmarTest is running, LotSummaryGenerator will send out error messages and exit.」

**`-v` 和 `-o` 是一对，`-m` 和「追加」是一对**——这两组关系是本页最容易读错的地方：

- **`-v` 只在「离线 + `-o`」这个组合里有意义**（原文：`This is used when you only want to
  generate the summary from offline data collection file to the output file specified by -o.`）。
  **它是把 `LOT_SUMMARY_PATH_NAME` 关掉**，不是把输出关掉。
- **`-o` 指定的文件已经存在时是追加，不是覆盖**：

> 「If the specified file is already existing, the lot summary will be appended to this file.
> Otherwise, a new file will be created. When appending the lot summary to the existing file,
> the following line will be printed in the file as the separator.」

追加时插进文件的那一行**逐字**是：

```
========Start Of New TestProgram "testprogram_name" at yyyymmdd hhmmss========
```

> 「where "testprogram_name" is the name of the test program/testflow and "yyyymmdd hhmmss"
> is the time stamp when the test program/testflow is started.」

**`-m` 就是把这行关掉**（`Disables the printing of the test program separator above in the
output summary file.`）——**注意它只关「这一行」，不关「追加」**。

### 本页语法节里为什么只有 `## Examples`

**本篇没有 `## Syntax` / `## Parameters` 两个段标记。** 命令行语法写在正文散文里
（就是上面那句 `./LotSummaryGenerator [-d DataCollection] …`），
**六个选项也是散文段落（`-d` / `-l` / `-o` / `-v` / `-m` / `-h`），不是表格**。
所以脚本按段标记去抽时**只抽到了 `## Examples`**——
上面「语法 / 参数」节里那 5 个子节是**本篇 Examples 的全部五个例子**，一个没漏。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法全部来自 `## Examples` 五个例子、六个选项的散文说明、以及正文前三段。
**先决定「用哪条路」，再谈参数**：

```
要历史数据 ──→ 命令行 + -d <EDL 文件>        → 一次性出汇总
要实时数据 ──→ 命令行不给 -d（挂当前会话）   → 需要 log_events_enable = on
要挂进流程 ──→ application model             → 靠 ENABLE_LOT_SUMMARY_GENERATOR 起停
要挂进流程 ──→ BLC program                   → 自己 fork / kill + SetApplicationVar
```

**① 命令行跑离线文件**（`## Examples` 第一个例子，逐字）：

> 「The following example generates the lot summary for the specified data collection file.
> The output file is /tmp/LotSummary.out. The log file LotSummrayGenerator.log is generated
> under the home directory of the current user.」

```
/opt/hp93000/soc/formatter/bin/LotSummaryGenerator -d /var/opt/hp93000/soc/tm/93k.iI3eAe/DataColltion.
```

**这个例子里的 `-d` 值有两个毛病**（`DataColltion` 少个 `e`、末尾多个 `.`），
**以及它自称的输出文件名和 `-o` 的默认值不一致**——三条都在「出处」⚠️ 里逐字记着。

**② 给每个 level 单独一个文件**（`LOT_SUMMARY_PATH_NAME`）：

```
LOT_SUMMARY_PATH_NAME = CONST_INPUT(/tmp/{Lot_id}.lotSum.gdf);
```

**`{Lot_id}` 来自上面几行的 `SCREEN_DIALOG` / `DIALOG_INPUT`**——
原文的用法是**先弹个对话框问 `Lot_id`，再拿它拼文件名**。

**③ 让汇总提前落盘**（`FORCE_SUMMARY_GENERATION_FOR_LEVEL`）——
**这是本页最实用的一条，因为「什么时候写文件」决定了你什么时候能读到它**：

> 「In the following example, the summary is generated at `point #1`. If
> FORCE_SUMMARY_GENERATION_FOR_LEVEL is not used, the lot summary is generated at `point #2`.
> Make sure to specify the current level name to FORCE_SUMMARY_GENERATION_FOR_LEVEL and
> put the variable in the post actions section of the level.」

**两条硬要求，原文都写在这一句里**（不在别处）：

| 要求 | 原文 |
|---|---|
| 值必须是**当前 level 的名字** | `Make sure to specify the current level name to FORCE_SUMMARY_GENERATION_FOR_LEVEL` |
| 变量必须放在**该 level 的 post actions 段** | `put the variable in the post actions section of the level` |

例子里的写法是 `FORCE_SUMMARY_GENERATION_FOR_LEVEL = CONST_INPUT(lot);`——
**值 `lot` 就是那个 level 的名字**，与「当前 level 名」那条对得上。

**④ 让 application model 自己起停**：

```
ENABLE_LOT_SUMMARY_GENERATOR = CONST_INPUT(1);
```

> 「In this example, ENABLE_LOT_SUMMARY_GENERATOR is used to enable the LotSummaryGenerator.
> The LotSummaryGenerator will be started at the beginning of the application model execution.」

**⑤ BLC 那条路要自己 fork / kill**——第五个例子是一段完整 C++：`startLotSummaryGenerator()`
里 `fork()` + `execl("/opt/hp93000/soc/formatter/bin/LotSummaryGenerator", 0)`，
`terminateLotSummaryGenerator()` 里 `sleep(5)` → `kill(LSGPid, 9)` → `waitpid(...)`；
两个变量用 `syncCommand("SetApplicationVar", inputParam, LOCAL_SESSION_ID)` 设。
**注意 `kill(..., 9)` 是 SIGKILL、而且停之前先 `sleep(5)`**——
**原文没有解释这 5 秒等的是什么**（**语料未写**；**不建议照抄这个常量**，
见「和谁有关」的 `verified` 那段）。

**常见组合与顺序**（从上表推出来的，**不是原文另列的流程**）：

| 你要什么 | 怎么组合 |
|---|---|
| 把一个 EDL 文件转成一份汇总 | `-d <file>` `-o <out>`（**不给 `-v`**，除非你确定 `LOT_SUMMARY_PATH_NAME` 会捣乱） |
| 只要一份干净的文件、不要 test program 那行头 | 再加 `-m` |
| 跑实时、结果直接进你的路径 | 不给 `-d`，先确认 `log_events_enable` 是 on |
| 每个 level 一个文件 | 走 application model / BLC，用 `LOT_SUMMARY_PATH_NAME` |
| 想在 level 结束**之前**就读到汇总 | 加 `FORCE_SUMMARY_GENERATION_FOR_LEVEL`（放 post actions） |

**出错时**：**本篇没有 `## Errors` / `## Warnings` 段**（已核，两个段名 0 命中），
**所以本页没有「报错条件」节**——这不是漏，是原文没有。
原文给的「出错」只有散文里的两处：**没有 SmarTest 在跑**时 `error messages will be printed`
（`-d` 那格用的是 `will send out error messages and exit`），
以及**`log_events_enable` 不是 on** 时 `no summary data will be generated`。
**两处原文都没给错误信息原文**。

## 和谁有关

- [[results]] —— **本页 `stage: results` 的理由**：它是结果数据的**汇总侧**；
  和 [[analysis-views]]（结果数据的**展示侧**）是同一批结果的两种去向。
- [[edl-file]] —— **两个输入之一就是它**。原文把离线输入明写成 `EDL file`
  （`Provide an offline data collection file (EDL file)` / `the offline EDL data collection file`）。
  **`EDL` 这个格式长什么样，本页一个字没有**（那篇没读，见「出处」）。
- [[run]] / [[testflow]] —— **上游**：产物覆盖的是**每一次 test program / testflow 执行**
  （原文：`generate the lot summary for all the test program and testflow executions recorded in the file.`）。
  **「哪次执行算一次」的判据在那边，不在本篇。**
- [[smartest-7.10.3]] —— 本 wiki 面向的版本；**本篇的版本段停在 7.1.3**（见「版本」④）。
- `application model` / `BLC program` / `BLC client`（**均未建、且不在 allowlist 里**）——
  **本页有一半用法挂在它们身上**（`ENABLE_LOT_SUMMARY_GENERATOR` 只对前者有效，
  `SetApplicationVar` 只对后者提到）。**那两份文档本页没读**，
  **所以「application model 怎么写、BLC client 是什么」本页答不了。**
- `SetApplicationVar`（**未建、不在 allowlist 里**）—— BLC 那条路上设变量的 API，
  原文只点名了一次，**没有签名、没有参数表**。
- `GDF`（**未建**）—— 产物格式，**原文只给了名字**（`in GDF format`），
  **GDF 是什么、怎么读，本篇一个字没写**。同理 `test summary` 这个说法也没有格式说明。
- `log_events_enable`（**未建、不在 allowlist 里**）—— **实时模式的开关**，
  原文只在讲实时模式那一句里提了一次（见「是什么」）。
- `SQST` / `TSST` 那一类命令、`Utility`、**与 `DFPN` 那种「定义」命令**—— **本篇一个字没提**
  （已核：`SQST` / `TSST` / `DFPN` 在本篇 0 命中）。**本页不写它们。**

> **本页没有推断。** 上面每条都来自本篇原文里的一句话；**凡是本页自己算出来的
> （如「一个文件出多份汇总」），都在正文里当句写明依据。**

## 版本

本文档**有** `## Functional changes` 段，**11 条，逐字**：

| 条目 | 和正文对得上吗 |
|---|---|
| `Introduced in SmarTest 7.1.0` | 成立版本**明写**了（**不是 §11.2 ② 的哨兵值**） |
| `SmarTest 7.1.1: Support the option -w waferIDVariable` | **该选项现在不在语法行里**，见下① |
| `SmarTest 7.1.1: Add FF/TF/TT to the output file` | **正文一个字没提 FF/TF/TT**，见下② |
| `SmarTest 7.1.1: Start LotSummaryGenerator automatically when executing test program/testflow` | 与 7.1.3 那条**是两种说法**，见下③ |
| `SmarTest 7.1.2: New application variable LOT_SUMMNARY_PATH_NAME and FORCE_SUMMARY_GENERATION_FOR_LEVEL` | **对得上**（正文有这两个变量）。**拼写见「出处」⚠️ ①** |
| `SmarTest 7.1.2: Support generating lot summary for incomplete data collection file` | **正文一个字没提「不完整文件」** |
| `SmarTest 7.1.2: Support using with BLC program` | **对得上**（正文有整节 BLC 用法） |
| `SmarTest 7.1.2: Remove the option -w waferIDVariable` | **对得上**：语法行里确实没有 `-w` |
| `SmarTest 7.1.3: New option -v` | **对得上**（`-v` 在语法行与选项表里） |
| `SmarTest 7.1.3: New option -m` | **对得上**（同上） |
| `SmarTest 7.1.3: New application variable ENABLE_LOT_SUMMARY_GENERATOR.` | **对得上**（正文有它） |

**① `-w` 只活了两个版本。** `SmarTest 7.1.1` 加、`SmarTest 7.1.2` 删，
**所以它在 7.10.3 上不存在，也不该在语法行里**——**语法行与版本记录自洽**。

**② `FF/TF/TT` 和「不完整文件」两条，正文里一个字都没有。**
**所以「输出文件里哪几列是 FF/TF/TT、拿不完整的 EDL 文件会发生什么」，本页答不了。**

**③ 「自动起」的两种说法，本页并列、不替它调和。**
版本记录把 `Start LotSummaryGenerator automatically when executing test program/testflow`
记在 **7.1.1**；而正文说自动起停的**条件**是 `ENABLE_LOT_SUMMARY_GENERATOR`
**存在**于 application model 文件里，那个变量记在 **7.1.3**。
**两者措辞不同（`executing test program/testflow` vs `the beginning of the application model
execution`），原文没说这是同一件事，本页不判。**

**④ 与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
而这一篇的版本段**停在 7.1.3**——**7.1.3 之后这个工具有没有变，语料里没有。**
**所以本页写的全部是 7.1.3 时点的说法**，不能直接当成 7.10.3 的行为
（§11：文档里有 ≠ 这台机器上能用）。

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md`
（TDC `127877.htm`；**md 8,743 字节 / 225 行**，上游 htm 11,544 字节）。**整篇读完。**

**本页没做的**：

- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4：没看图就写「本页没用图」，不编理由）。
- **`EDL` / `GDF` 两份格式文档没读**——**所以「EDL 文件长什么样、GDF 怎么解析」本页一个字没有**；
  本页只有「输入是 EDL、输出是 GDF」这两个名字。
- **`log_events_enable` 那个系统标志的文档没读**——**在哪设、默认值、怎么查，本页没有。**
- **`SetApplicationVar` 的 API 文档没读**——BLC 那条路上的设变量方式本页只有名字。
- **`application model` 与 `BLC program` 的文档没读**——
  **两个概念本身是什么、语法怎么写，本页没有**；本页只有本篇顺带给出的那几行示例。
- **`## Errors` / `## Warnings` 两个段本篇都没有**（已核，0 命中），
  **所以本页没有「报错条件」节**——这是原文的结构，不是本页漏做。
- **没有实跑。** 没有在机台上发过这条命令、没跑过 EDL 文件、没起过 BLC、
  没触发过「没有 SmarTest 在跑」那条错误。`verified: doc-only` 说的就是这件事（§11）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**（§11.2）。
> **下面六条全部核过上游 `raw/127877.htm`——六条在 htm 里就是这样。**
> **所以这一族是 §11.2 ⑥ 那一类（上游就坏的），不是 §11.2 ① 的转换坏字**
> **（本篇 md 的 CJK 字符数实测为 0，没有那一族乱码）。**
>
> **① 同一个变量名在一篇里拼成两种样子。** 这是本篇最贵的一处——
> **拼错的那种出现在解释性散文和版本记录里，拼对的那种出现在代码与选项说明里。**
> 逐字（左列是**完整原文片段**，不是截断）：
>
> | 拼法 | 出现处（逐字） | 次数 |
> |---|---|---|
> | **`LOT_SUMMNARY_PATH_NAME`**（`SUMMNARY`，多一个 `N`） | `The application variable LOT_SUMMNARY_PATH_NAME, FORCE_SUMMARY_GENERATION_FOR_LEVEL and  ENABLE_LOT_SUMMARY_GENERATOR are defined for LotSummaryGenerator.` / `LOT_SUMMNARY_PATH_NAME is used to specify the path and name of a separate summary file for each level` / `define the variable LOT_SUMMNARY_PATH_NAME and  FORCE_SUMMARY_GENERATION_FOR_LEVEL with SetApplicationVar API.` / 子节标题 `### Using LOT_SUMMNARY_PATH_NAME in the application model` / 版本条 `SmarTest 7.1.2: New application variable LOT_SUMMNARY_PATH_NAME and FORCE_SUMMARY_GENERATION_FOR_LEVEL` | **5** |
> | **`LOT_SUMMARY_PATH_NAME`**（正确拼法） | `Disables the effect of the application variable LOT_SUMMARY_PATH_NAME.`（`-v` 的说明）/ `LOT_SUMMARY_PATH_NAME = CONST_INPUT(/tmp/{Lot_id}.lotSum.gdf);` / `inputParam["VARIABLE_NAME"] = "LOT_SUMMARY_PATH_NAME";` | **4** |
>
> **本页不替它判哪个是「真」标识符**——§11.2 明令只许照实记。
> **但要提醒一句**：**可执行的那两处（`-v` 的说明、BLC 例子里的字符串）用的是正确拼法**，
> 而**拼错的那五处都是散文**。**这是一个观察，不是结论**（§11.4：观察不许占档号）。
> **拿拼错的那个名字去 raw 里搜是搜得到的**（它就在散文里），
> **但拿它去 `SetApplicationVar` 里用会不会生效，本篇没有写。**
>
> **② `Ofline`。** 逐字：`- Ofline data collection file`
> ——**应为 `Offline`**（下一行散文里就写着 `Provide an offline data collection file`，小写且拼对）。
>
> **③ `DataColltion`，且末尾多一个 `.`。** 逐字（命令行的 `-d` 值）：
> `/opt/hp93000/soc/formatter/bin/LotSummaryGenerator -d /var/opt/hp93000/soc/tm/93k.iI3eAe/DataColltion.`
> ——**`DataColltion` 应为 `DataCollection`**（少一个 `e`）；**末尾那个 `.` 后面什么都没有**，
> 而这一句原文是 `The following example generates the lot summary for the specified data
> collection file.`（一个完整的例子、不是省略号）。
> **路径里还有个 `iI3eAe`**（大小写混排），**原文没有说明它是什么**——本页照抄。
>
> **④ 日志文件名也拼错一次，而且同一篇里另有一处拼对。** 逐字两处：
> `The log file LotSummrayGenerator.log is generated under the home directory of the current user.`
> （例子说明，**`LotSummray`**）对
> `If not specified, the log file LotSummaryGenerator.log will be generated in the home directory of the current user.`
> （`-l` 的说明，**拼对**）。**两处说的是同一个文件。**
>
> **⑤ 例子自称的输出文件名与 `-o` 的默认值不是同一个名字。** 逐字两处：
> `The output file is /tmp/LotSummary.out.`（例子说明）对
> `If not specified, /tmp/LotSummary.output is used by default.`（`-o` 的说明）。
> **`LotSummary.out` vs `LotSummary.output`**，而**那个例子里根本没有 `-o`**
> ——**所以按 `-o` 的规则它该落到 `/tmp/LotSummary.output`，与例子自称的名字对不上。**
> **本页并列两处，不替它判哪个对。**
>
> **⑥ `sepecify`。** 逐字（BLC 例子里的那一行）：
> `cout<<"Please sepecify a BLC input file!!!"<<endl;`
> ——**应为 `specify`**。**这是别人的示例代码，本页不修。**
>
> **另外两条结构上的事，不是错、但值得记**：
> `## Parameters` 那一节在本篇里**不是表格**（六个选项是散文段落，`-d` / `-l` / `-o` / `-v` / `-m` / `-h`），
> **所以「语法 / 参数」节只收到 `## Examples`**——这是抽取规则的作用，不是脚本漏抽。
> 以及本篇**没有 `## Errors` / `## Warnings` 段**，所以骨架里没有「报错条件」节。

`verified: doc-only`
