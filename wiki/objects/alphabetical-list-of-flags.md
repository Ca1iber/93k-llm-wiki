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

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

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
（`342556.htm`，**37,008 字节 / 624 行——本批 12 页里最长的一篇**，整篇读完）。

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
