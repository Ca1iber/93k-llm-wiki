---
type: object
title: Technology file for a device
layer: file
stage: project
tags: [project, file, technology, device-directory, dscp, memory-limits]
related: [project, device-directory, device-technology-directory, dscp, dtcp, model-file, device-license-file, testflow-analyzer-tool, tpt-generate-device-dir, stpm]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Technology file for a device

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

> **一句话**：**每个 device 目录里的那个隐藏文件 `.technology`。**
> 它定三件事：**technology 源目录**（`cmos` 还是 `ecl`）、**若干 device 专属的系统参数**、
> 以及**若干系统参数的上限**。原文第一句就是全部定位：

> 「The .technology file defines the source directory for technology-related settings, some
> device specific system parameters and some maximum values for certain system parameters.」

**上限那一类参数的真正作用，是「预留多少内存」**——原文第二句就把这件事说破了：

> 「The maximum values for certain system parameters determine the amount of memory reserved
> for the respective data structures.」

**三条必须先记住的性质**（全部逐字来自原文）：

| 性质 | 原文 |
|---|---|
| **绝对最大值不会自动用满** | `The absolute maximum values are not automatically used so that memory usage can reflect the actual requirements of the device.` |
| **固件可能把你的设置改小** | 内存有限，`it is possible that one or more otherwise valid settings are reduced by the firmware in order to remain within the memory limits` |
| **一 device 一份** | `Each device directory contains a .technology file.` |

**第二条是本页最实用的一句**：你写 `testpoints: 100000` 不报错，
**不代表它真按 100000 生效**。原文把「怎么办」指向两篇：
`The Testflow Analyzer Tool` 与 `Optimizing the technology file`（**这两篇本页没读**）。

**归属**：`layer: file` / `stage: project` —— 它属于「建 device、建工程」那一段，
是 device 目录**一建出来就在那儿**的东西，不是你在 testflow 里调用的东西。

### 25 个参数，钥匙是「三列对应关系」

原文 `## Parameters of the .technology file` 先给了表格图例（`The following values are defined:`），
**不读这段图例就会看错那张表**：

| 列 | 原文含义 |
|---|---|
| **Short description** | 参数的一句话说明 |
| **Values** | 支持的值 / 范围，以及默认值 |
| **Change Device wizard** | 对应 **Change Device 向导里哪个字段**（原文指向 `Edit Device page`） |
| **DSCP command** | 对应 `DSCP`（Define System Control Parameter）命令的哪个参数 |
| **Note** | 更细的说明、规则与提示 |

**「`.technology` 参数名 ≠ DSCP 参数名」是这一页最容易踩的一处**——
原文两列并排给出，名字却常常不一样。能对上一个 DSCP 参数的只有下面这几个（其余全是 `n/a`）：

| `.technology` 参数 | DSCP 参数 | 默认 / 上限 |
|---|---|---|
| `device_cycles` | `device_cycles` | 256 / 16 384 |
| `dps_sets` | `dps_set` | 32 / 256 |
| `level_sets` | `level_set` | 32 / 256 |
| `m_sets` | `pmu_set` | 1 024 / 12 800 |
| `pdc_sets` | `devicecycle_set` | 1 / 128 |
| `period_res_precision` | `period_res_prec` | 见下 |
| `timing_sets` | `timing_set` | 256 / 999 |
| `waveform_sets` | `waveform_set` | 32 / 128 |

`period_res_precision` 原文没给固定默认值，给的是**三段条件**：
`.technology` 里没有它就是 **4**；有它就**以文件里的值为默认**；
而**建 device 时会被设成 9（上限）**。

### 哪些参数动的是内存（**这一组要一起看**）

原文明说 `testpoints` 那一条 `has the biggest influence on the memory usage`，
但真正吃内存的是一组参数：

| 参数 | 吃什么内存 | 关键数字 |
|---|---|---|
| `testpoints` | **每个 test point 占几十字节卡上内存** | 默认 10 000，上限 1 048 576 |
| `digital_default_result_area_size` | error map 放在外部（vector）内存时**预留多大的 result area** | 默认 0，上限 134 217 728（**单位是字节**） |
| `m_sets` / `mset_program_memory_preallocation` | PPMU measurement-set 动作的内存；预分配的大小**取决于 `m_sets`** | 默认 1 024，上限 12 800 |
| `fast_transfer_buffer_size` | 改 vector / level spec / PPMU 设置用的缓冲区 | 默认 0；非 0 时必须落在 131 072 … 16 777 216 字节 |
| `himem` + `extended_dram_factor` | 是否启用高内存区；启用后 vector 区占多少 | `himem` 默认 off；`extended_dram_factor` 默认 80（即 80% 给 vector 区） |

`testpoints` 的字节数是 footnote 里的：**XPS256 每点 56 字节，DPS128 和 UHC4T 每点 46 字节**
（原文脚注：`56 bytes on XPS256, 46 bytes on DPS128 and UHC4T.`）。

`digital_default_result_area_size` 原文另给了五条 hint，其中三条最容易踩：

- **每个 digital pin 上都预留**（`but not on DPS pins or DC Scale pins configured for the PMU or DPS operating mode`）；
- **超出预留区就停止记录**，再往后上传会报错；
- **预留区算进 license 上限**；
- 换算：`One byte is one vector.`

### 两个「只在特定机型上才有意义」的开关

| 参数 | 限制（原文） |
|---|---|
| `himem` | `Currently, this parameter only affects PS5000.`；且 `This usage is not supported in memory sharing.` |
| `fast_transfer_buffer_size` | `The VEC_TRANSFER_TASK and LEV_TRANSFER_TASK APIs can be used only with SmartScale test head cards.` |

`fast_transfer_buffer_size` 的取值规则**按 SmarTest 版本分三档**，原文给了三条公式
（`SmarTest 鈮?7.4.3.0` / `SmarTest < 7.4.3.0` / `SmarTest 鈮?7.4.1.0`，坏字见 `## 出处`）：

| 版本档 | 规则 |
|---|---|
| **≥ 7.4.3.0** | `fast_transfer_buffer_size >= blockSize * (number of digital pins specified in VEC_TRANSFER_TASK() * number of configured sites)`；原文另建议**按最少 2000 通道**估，以免以后加 site 出问题 |
| **< 7.4.3.0** | `fast_transfer_buffer_size >= blockSize * (number of configured digital and DPS/DC channels across all sites)` |
| **7.4.1.0 及更早** | 值**必须是 8192 字节的整数倍**（**原文这一个小标题自己就有矛盾**，见 `## 出处` ⑨） |

原文对违反的后果只说了处理办法：
`An error message will be issued if the rule that is defined above is violated. You can then
either increase the block size or split the vector data transfer into smaller blocks.`

### 两条「公式型」约束（**写在 Note 之外，容易漏**）

`device_cycles` 和 `waveform_sets` 两个参数的说明**各自带一条公式，而且是同一条的两半**：

> `Maximum number of device cycles per waveform set or wavetable = (device_cycles - 1) / waveform_sets`

**即：`device_cycles` 调大或 `waveform_sets` 调大，都在压缩「每个 waveform set 能有的 device cycle 数」。**
脚注另补一句限定：`only device cycles that contain physical edge actions need to be considered.`

### `## Application note`：testpoints 的预留规则与它的后果

这一节是本页唯一带 `CAUTION` 的地方，讲 **testpoints 的内存是在什么时候、按什么口径预留的**：

- **在加载 device 的最开始就预留**，用 `DTCP` 与 `*RST` 两条命令（原文点名 `DTCP, DTCP?` 与 `*RST`）；
- **在 model file 里所有可用的 DC Scale 卡上都预留**；
- **按「所有 testpoints 所需的最大内存」预留，不管后面用不用**；
- 预留量取决于 `testpoints` 的值和**卡相关的 testpoint 结构**。

> **CAUTION 原文**：`Ignoring the rules above and defining too much test points may result in
> memory overflow for the subsequently defined and loaded setups or pattern.`

溢出时的表现原文也写了：report window 出现
`ERROR: Specified set size is too large for memory configuration`，
`SmarTest restores the previous setup or the default setup and newly defined settings and
pattern are not available.` —— **注意这是「回滚 + 丢设置」，不只是报个错。**

`testpoints` 上限还有一个**按卡和 `waveform_sets` 联动**的脚注：
`DPS128/DPS64 reserves the memory for maximum 523012 testpoints with waveform_sets set to 128.`
`Some more testpoints are supported with lower settings of waveform_sets.`

## 典型用法

**两条改参数的路径，代价完全不同**（原文 `## Changing the .technolog file` 一节）：

| 你改的参数在哪 | 怎么改 | 生效方式 |
|---|---|---|
| **Change Device 向导里有这个字段** | 菜单 `93000 > Change Device`，在对话框里改 | 存进 `.technology` 文件，**并用 DSCP 等固件命令立刻告诉固件**；`These changes are permanent and apply each time the device is selected thereafter.` |
| **向导里没有这个字段** | **只能直接编辑 `.technology` 文件** | **必须手工补发 DSCP 命令**，否则固件不知道；或者**重新选一次这个 device**（会重发 DSCP） |

> **第二行是这一页最容易做错的一步**：手改文件**不会自动同步到固件**。
> 原文：`In this case, the DSCP command must be issued manually to define the new values to
> the firmware, or the device must be re-selected (which will reissue the DSCP command).`

**文件长什么样**（原文给的完整样例，`## Available parameters` 之前那段代码块，12 行）：

| 样例里的写法 | 说明 |
|---|---|
| 第一行是一个**没有值**的项 | `[/dev_tech/cmos](…)` —— 它选的是 technology 目录，不是键值对 |
| 其余是 `参数: 值` | 例如 `device_cycles: 256`、`waveform_sets: 16`、`tester_model: act` |
| **`licensing_file` 可以是空值** | 样例里就是空的（参数说明：`Parameter value is empty if not used; otherwise the file name is entered.`） |

**一个前置动作**（`/dev_tech/cmos or /dev_tech/ecl` 那条参数说明）：

> 「The specific technology is given in the New device dialog.」

—— **technology 是建 device 时选的**，`.technology` 文件里那一行是结果不是入口。
原文接着说：technology 相关的 level 等数据**存在 device 目录下的子目录里**，
**建 device 时从对应的 `dev_tech` 目录初始化**；默认 level 由选中的 technology 定义，
之后可以按需改（指向 `Default levels file for a device`）。

**排查顺序建议**（**这一条是建议，不是文档要求**）：先看 `## Available parameters` 的清单确认参数名，
再用上面的「参数名 ↔ DSCP 参数名」表确认要发的命令，最后按
`Short description → Values → Change Device wizard → DSCP command → Note` 五列逐列读那一条。
**直接按 DSCP 参数名去文件里搜会搜不到**（`pmu_set` 在文件里写作 `m_sets`）。

## 和谁有关

**上游 / 同族（`.technology` 文件不是孤立的，原文一层层指出去）**

- [[device-directory]] —— **`.technology` 就住在 device 目录里**（原文：`Each device directory contains a .technology file.`）；本页是它的一个成员
- [[device-technology-directory]] —— 参数 `/dev_tech/cmos or /dev_tech/ecl` **指向的那个目录**；
  原文 `## Related information` 也把 `Device Technology Directory` 列在同一组里
- `Device Technology Defaults`（raw: `01.01.07.02.01_Device_Technology_Defaults.md`）—— 同父兄弟页，
  **是否建页本页不知道**
- `Default levels file for a device`（raw: `02.08.04.03.04_Default_levels_file_for_a_device.md`）——
  technology 决定默认 level，那份文件是**改这些默认 level 的地方**

**下游 / 谁读它**

- [[dscp]] —— **本页几乎所有值最终靠 `DSCP` 送到固件**（原文表格的 `DSCP command` 列就是它）
- [[dtcp]] —— testpoints 的内存预留用的是 `DTCP` 与 `*RST`（原文 `Application note` 点名）
- [[model-file]] —— 两处交叉：① `utility_lines_per_pogoblock` 与 model file 的
  `GLOBAL section` 里 `utility_lines` 有交互（原文 `For interactions between the .technology
  file and the model file see utility_lines in the GLOBAL section`）；② testpoints 的内存
  **在 model file 里所有可用的 DC Scale 卡上都预留**
- [[device-license-file]] —— 参数 `licensing_file` 就是它（原文指向 `The device license file`）；
  另有一条更硬的耦合：**result area 的预留 counts against the license limit**
- [[testflow-analyzer-tool]] —— **被固件改小的那些设置，去这里看**（原文把 `The Testflow
  Analyzer Tool` 和 `Optimizing the technology file` 并列为「设置被削减」的出口）
- [[project]] / [[stpm]] / [[tpt-generate-device-dir]] —— 三个都作用在 **device 目录这一层**：
  本页是 device 目录的一件内容物，`tpt_generate_device_dir` 是**建出 device 目录**的那条 STPM 命令。
  **这三条是「同一个目录、不同工具」的关系，不是引用关系**（推断：原文没有一句话把本条和它们并列）

**同一批里的关联**

- [[utility-card]] / `Utility pogo block ...` —— 参数 `utility_lines_per_pogoblock` 的直接后果：
  **16 还是 32** 决定了每个 pogo block 上有多少条 utility line，
  而 Utility Card 提供的是 `256 dynamically controlled utility lines` 分在八个 4-row block 上。
  **本条是推断**——原文没有把这两个数字放在一起对。

> **本页的关系只有一半来自原文**：`## Related information` 那一段列了 10 篇，
> 表里每条对应的原文句子都在上面引了。**标了「推断」的两条不是原文说的**。

**一个名字上的事**：本页承担了候选名 `technology-file`（同一个对象的另一种叫法）。
**本 wiki 不为 `technology-file` 另建页**，所以本页正文用反引号写它。
`stages/level.md` 与 `stages/project.md` 里仍写着旧名的链接（本页未改，那两页不属本批）。

## 版本

本文档有 `## Functional changes` 段，逐条列在下面（**照原文抄，不合并**）：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.1.4**：`Upper limit of PDC_set has been increased`
- **SmarTest 7.1.4.5**：`New parameter: pulldown_in_level_set_0`
- **SmarTest 7.2.0**：`New parameter: utility_lines_per_pogoblock`
- **SmarTest 7.2.1**：`Testflow Analyzer tool provides the numbers of sets`
- **SmarTest 7.2.2**：`New parameter: Result Area Size`
- **SmarTest 7.2.3.9 / 7.3.4.4 / 7.4.1.1**：`New parameter: pulldown_not_configured_pins`
- **SmarTest 7.2.3.9 / 7.3.4.4 / 7.4.1.1 / 7.4.2**：`New parameter: mset_program_memory_preallocation`
- **SmarTest 7.3.2**：`New parameter:fast_transfer_buffer_size`
- **SmarTest 7.4.1**：`New API LEV_TRANSFER_TASK that uses the fast_transfer_buffer_size.`

> **两条读法上的提醒**：
> ① **`Introduced before SmarTest 6.3.2` 是哨兵值**，不是「6.3.2 的变更」——
> 它只表示「在本套文档覆盖范围开始之前就已经有了」（§11.2 ②）。
> ② **`7.3.2` 那一条原文 `New parameter:` 后面没有空格**，照抄原样。

本 wiki 面向 **SmarTest 7.10.3**：上面列到的参数全部都在。

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md`
（TDC `49363.htm`，9,234 字符，441 行）。**本页只读了这一篇。**

**本页没做的**：

- **`## Related information` 里的 10 篇一篇没读**，特别是这四篇，
  **它们各自是「本页某个参数」的展开**，本页只能写到原文一句话的深度：
  - `Editing technology data` 与 `Creating a new device` —— **向导那一侧怎么操作，本页没有**
  - `The model file` —— `utility_lines` 怎么和 `utility_lines_per_pogoblock` 交互，本页不知道
  - `SmarTest system parameters - default values and limits` —— **全局默认值与上限的对照表，本页没有**
- **正文里点名、但本页没读的还有三篇**：
  `Optimizing the technology file`（设置被削减时怎么办）、
  `The Testflow Analyzer Tool`（看「到底给了多少个 set」）、
  `Result areas for error map data`（result area 的用途）。
- **两处 API / 命令只知其名**：`DMAS? MFRE`（查可用内存）与 `DTCP, DTCP?`（预留 testpoints 内存）
  —— **语法、参数、返回值本页一个字都没有**。
- **源文档里没有图**（本篇无插图、也没有内嵌小图，本篇也**没有 `Subtopics`** 那一层要查）。
  **所以本页没有任何来自图的结论。**
- **每条参数只写到原文 Note 里的那一层**：例如 `fast_transfer_buffer_size` 的三条版本公式，
  本页只抄了公式本身，**原文举的那个 128 × 1600 = 204800 的算例没有展开**。
- **`/dev_tech/cmos` 与 `/dev_tech/ecl` 两个目录本身长什么样，本页不知道**——
  原文只说它是一个 `directory structure`。

> ⚠️ **本篇的语料瑕疵，照实记下，一处都没替它改**：
> ① **一节的标题掉了字母**：`## Changing the .technolog file` ——
> **`technolog` 应为 `technology`**（本页正文引这一节时用的是「原文 `## Changing the .technolog file` 一节」的写法，未改字）。
> ② **`≥` 的编码损坏**：`For SmarTest 鈮?7.4.3.0:` 与 `For SmarTest 鈮?7.4.1.0:` ——
> `鈮?` 是 `≥` 按 GBK 读出来的坏字（与 §11.2 ① 同源，但形态是**单坏字 + 一个 `?`**，
> 不是常见的 `鈥` 两字组合）。**同一段里的 `For SmarTest < 7.4.3.0:` 用的却是正常的 `<`**，
> 所以这一处只能靠上下文读。
> ③ **链接锚点和参数名对不上**：`## Available parameters` 里
> `enforce_smart_scale_dc_sync_compatibility` 的链接是
> `01.01.07.02.01.02_Technology_file_for_a_device.md#_49363__enforce_ps5000_dc_sync_compatibility`
> —— **锚点里写的是 `ps5000`，参数名里写的是 `smart_scale`**；同表其余各项的锚点形状都是
> `#_49363__row_<参数名>`。**原文没说哪个是对的，本页不判。**
> ④ **一处缺词**：`The value of the fast_transfer_buffer_size must greater than the largest used
> VTT (transfer) size multiplied by the number of configured (DPS and digital) channels.`
> —— **`must` 后面缺 `be`**。
> ⑤ **子标题被吞进正文行**：`## Application note` 的第一行是
> `  Memory reserved for testpoints  Some rules must be observed when defining high numbers of testpoints:`
> —— 子标题 `Memory reserved for testpoints` 和正文挤在同一行，靠**两个空格**分隔。
> ⑥ **同一栏位两种名字**：`himem` 用 `Notes:`、`init_vectors_with_value` 里一处 `Note` 一处 `Notes`；
> 而 `pulldown_not_configured_pins` 的栏位名是 `New device default value:`，
> **别的参数同一位置叫 `Values:`**。
> ⑦ **脚注块被吞进 `## Functional changes` 段尾**（§11.2 ③ 的同一现象）：
> 三个脚注定义 `[1)](<>) …` / `[2)](<>) …` / `[3)](<>) …` 紧跟在最后一条 bullet 后面，
> 内容分别是「只算含物理边沿动作的 device cycle」「XPS256 56 字节 / DPS128 与 UHC4T 46 字节」
> 「DPS128/DPS64 523012 个 testpoint 的上限」。
> ⑧ **「语法 / 参数」节里有 8 张表缺参数名那一行**（第 6/7/8/9/10/13/15/17 张）——
> 原因是 raw 里参数名（如 `enforce_smart_scale_dc_sync_compatibility`）是**独立的非管道行**，
> 脚本只收连续管道行。**逐字没丢，但要按参数名去 raw 里搜，别在表里搜。**
> ⑨ **一处自相矛盾**：小标题写的是 `For SmarTest 鈮?7.4.1.0:`（即 `≥ 7.4.1.0`），
> 紧跟着的正文却写 `must be a multiple of 8192 bytes for SmarTest 7.4.1.0 and older versions.`
> —— **`≥ 7.4.1.0` 与 `and older versions` 方向相反**。
> 本页正文因此不引这个小标题，只写「7.4.1.0 及更早」并在此记明冲突（§10：两种说法并列，不替它选）。
> ⑩ **`fast_transfer_buffer_size` 的取值说明插在 `Short description:` 与 `Values:` 之间**，
> 位置在管道行之外，所以「语法 / 参数」节那张表里只剩 `Values:` 的那一行。

`verified: doc-only` —— **只在 TDC 文档里确认存在**，未在任何真实机台上改过 `.technology` 文件。
