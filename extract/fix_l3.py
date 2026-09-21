# -*- coding: utf-8 -*-
"""按 L3 审计结论改写九页的 ## L3 小节。

只用**已回原文逐条核实过**的分类号与签名。每处改写都在页内留下「上一版写了什么、为什么错」，
因为错的断言比缺的断言更危险：缺的会被发现，错的会被当证据用。

替换策略：按 `## L3` 到下一个顶级 `## ` 之间的整段替换。
"""
import re
from pathlib import Path

STAGES = Path(r'F:\master-dev\understand-anything-wiki\wiki\stages')

CROSS = """**L3 入口是横切的，能力面按阶段分族。** 文档事实：`TestsuiteProxy`
（`02.09.01.14.02.01`）的 33 个编号成员里，session / execute / `isPass` / `isExecuted` /
name / siteMatch 那几个是**横切面**，其余**天然按阶段分组**——这不是巧合，是文档自己的组织方式。
横切入口见 [[test-suite-control-api]]；程序侧对产物文件的操作见 [[tpi-program-routines]]。"""

NEW = {}

# ─────────────────────────── level ───────────────────────────
NEW['level'] = """## L3 — 外部控制

""" + CROSS + """

### 本阶段专属读写口

文档事实（`02.09.01.14.02.01`）：level 一族是 `.05` `getLevelEquation()` /
`.06` `getLevelSet()` / `.07` `getLevelSpec()` / `.04` `getAnalogSet()` /
`.24` `setAnalogSet()` / `.25` `setEquationBasedLevel()`。

其中 `.25`（`02.09.01.14.02.01.25_TestsuiteProxy.setEquationBasedLevel`）：

```
bool setEquationBasedLevel(const std::string& levelEquation,
                           const std::string& levelSpec,
                           const std::string& levelSet);
```

> This function sets the equation based level information to the test suite.

三个参数依次是 level equation / level spec / level set，与 `.05` / `.07` / `.06` 三个
getter 一一对应。调用方式见 `02.09.01.14.01_How_to_use_the_test_suite_control_API`：
建外部 C++ 客户端，include `testsuitecontrol_api.hpp`、`using namespace testsuitecontrol;`，
编译 `-I/opt/hp93000/soc/prod_com/include/ -m32`、链接 `-ltestsuitecontrol_api`，
经 `/opt/hp93000/soc/system/bin/run -x <program>` 启动。该族 `Introduced in SmarTest 6.5.2`，
7.10.3 可用。

程序侧的产物文件接口（[[tpi-program-routines]]，`02.09.01.09` 全章 31 篇）：`DataManager`
（`02.09.01.09.02`）的文件标识 `dm_level` 就是 **level setup 文件**，配 `dm_load` /
`dm_save` / `dm_merge` / `dm_copy_in` / `dm_delete` 五个操作；`GetEQVariableValue`
（`02.09.01.09.10`）读 equation 变量值。

> **改判记录。** 本页上一版 L3 写的是「文档未覆盖」，并断言 Test suite control API
> 「它控制的是 test suite 的执行，**不提供任何 level 值接口**」。**那一句是错的**——
> `setEquationBasedLevel()` 就是 level 值接口，`getLevelEquation/Set/Spec` 就是读口。
> 该断言已删。错的断言比缺的断言更危险：缺的会被发现，错的会被当成「查过了，没有」。

### 两个同形陷阱 —— 名字里有 level，但不是本阶段的 level

写在这里是因为它们极容易被拿去错误地「补」本页：

- **HVM `GetLevelProfile`**（`02.09.01.10.03.02.02.26`）：文档事实是「returns all the variable
  names and values contained in the specified level」。但这里的 level 是 **application model
  的层级结构**，与 `IssueEDLEvent()` / `IssueHVMExecutionEvent()` 同族——`02.09.01.11.03.02`
  明写「maintain the application model file **level structure** in the BLC」。**不是电压 level。**
- **BLC `Level_control_API`**（`02.09.01.11.03.02`）的 `StartLevel()` / `LoopLevel()` /
  `CompleteLevel()`：同上，是产线层级（lot / wafer / die）的维护接口。

**不许拿 L1 命令或 L2 API 冒充 L3。**
"""

# ─────────────────────────── timing ───────────────────────────
NEW['timing'] = """## L3 — 外部控制

""" + CROSS + """

### 本阶段专属读写口

文档事实（`02.09.01.14.02.01`）：timing 一族是 `.18` `getTimingEquation()` /
`.19` `getTimingSet()` / `.20` `getTimingSpec()` / `.22` `isMultiportTiming()` /
`.26` `setEquationBasedTiming()` / `.27` `setMultiportTiming()`。

其中 `.26`（`02.09.01.14.02.01.26_TestsuiteProxy.setEquationBasedTiming`）：

```
bool setEquationBasedTiming(const std::string& timingEquation,
                            const std::string& timingSpec,
                            const std::string& timingSet);
```

> This function sets the equation based timing for the test suite.

三参数依次是 timing equation / timing spec / timing set，与 `.18` / `.20` / `.19` 三个
getter 对应。`.22` / `.27` 是 multiport timing 的查询与设置——**与 [[pattern]] 的
multi-port burst 是同一件事的外部化**，见 [[run]] 的 `Using_execution_contexts`。

调用方式见 `02.09.01.14.01`：外部 C++ 客户端，链接 `-ltestsuitecontrol_api`，经
`run -x` 启动。该族 `Introduced in SmarTest 6.5.2`，7.10.3 可用。

程序侧的产物文件接口（[[tpi-program-routines]]，`02.09.01.09` 全章 31 篇）：`DataManager`
（`02.09.01.09.02`）中 `dm_timing` = timing setup 文件、`dm_tdiag` = timing diagram 文件、
`dm_mx_waveform` = multiport waveform，各配 `dm_load` / `dm_save` / `dm_merge` /
`dm_copy_in` / `dm_delete`。

> **改判记录。** 本页上一版 L3 写「文档未覆盖」，并断言「Test suite control API / HVM
> 在本次读到的语料里**没有覆盖 timing setup 的条目**」。**那一句是错的**——`.26` 就是
> timing 值接口。已删。

### 同形陷阱

- **HVM 侧的 timing**：`02.09.01.10`（HVM API）本阶段未见 timing 值接口；HVM 面向的是
  测试执行与会话控制。

**不许拿 L1 命令冒充 L3。**
"""

# ─────────────────────────── testmethod ───────────────────────────
NEW['testmethod'] = """## L3 — 外部控制

""" + CROSS + """

**本页是九页里 L3 专属面最厚的一页。** 文档事实（`02.09.01.14.02.01`）：test method 一族
有九个成员，占 `TestsuiteProxy` 编号成员的近三分之一——

| 分类号 | 成员 | 作用 |
|---|---|---|
| `.01` | `attachTestmethod()` | 把 test method 挂到 test suite |
| `.13` | `getTestmethodName()` | 取 test method 名 |
| `.14` | `getTestmethodParameterNames()` | 取参数名 |
| `.15` | `getTestmethodParameterValue()` | 读参数值 |
| `.32` | `setTestmethodParameterValues()` | 写参数值 |
| `.11` | `getTestmethodDefaultLimitNames()` | 取 default limits 名 |
| `.16` | `getTestmethodUserDefinedLimitNames()` | 取 user-defined limits 名 |
| `.12` | `getTestmethodLimitValue()` | 读 limit 值 |
| `.31` | `setTestmethodLimits()` | 写 limit 值 |

`attachTestmethod` 的签名与用例（`02.09.01.14.02.01.01`、`02.09.01.14.01`）：

```
bool attachTestmethod(const std::string& name);
// ts.attachTestmethod("ac_tml.AC_TEST.FunctionalTest");
```

即 **test instance 的指定可以不点 GUI，由外部程序完成**；参数与 limit 也可外部读写。
调用方式见 `02.09.01.14.01`：外部 C++ 客户端，链接 `-ltestsuitecontrol_api`，
经 `run -x` 启动；该族 `Introduced in SmarTest 6.5.2`，7.10.3 可用。

程序侧的产物文件接口（[[tpi-program-routines]]）：`DataManager`（`02.09.01.09.02`）的
`dm_testprog` / `dm_testflow` / `dm_testtable`，配 `dm_copy_in` 等操作；`GetEQVariableValue`
（`.10`）读 equation 变量。

> **改判记录。** 本页上一版 L3 写：「除此之外，本阶段语料中没有其它外部控制接口（无 HVM
> 实际用法、无远程/脚本化接口文档）」，然后落到「文档未覆盖」。**那一句是错的**——
> Test suite control API 里 test method 是最完整的一族。已删。
>
> 上一版唯一找对的是 `02.07.01` 那句「这些 API 不在 test method 编程里用」——**它说的是
> 「不在 test method **内部**编程时调用」，不是「与 test method 无关」**。前者是调用位置，
> 后者是主题；上一版把这两个读混了。这族接口的对象**正是** test method。

"""

# ─────────────────────────── results ───────────────────────────
NEW['results'] = """## L3 — 外部控制

""" + CROSS + """

**本阶段有专属 L3，而且直接对口。** 文档事实：

### 1. 结果数据的实时读取 —— Data Retrieval Library

`02.09.01.16.02_How_to_capture_the_test_result_in_real_time`（章：`02.09.01.16`
Critical tasks in production environment）明写事件数据日志（EDL）就是为**从生产环境取出测试结果**
而提供的，并给出用 data retrieval library 实时抓取结果的流程；`02.09.01.16.04`
是用 **BLC API 控制 event data logging**。同章下还有
`02.09.01.16.02.05_Example_of_yield_monitor`、
`02.09.01.16.02.06_Example_of_analyzing_the_Iddq_measurement_results` —— 这两个例子
**就是本阶段在做的事**（良率监控、Iddq 结果分析），只是从外部程序侧做。

### 2. Error Map 的记录粒度由外部程序决定

`02.09.01.09.28_SetErrorMapMode`：

```
VOID SetErrorMapMode(INT32 mode);
```

> This routine lets you determine the mode in which the results are recorded for the result
> displays (for example, the Error Map) when executing a test.

- `ERROR_MAP_FAILURE_ORIENTED` — only failed cycles are logged
- `ERROR_MAP_CYCLE_ORIENTED` — all cycles are logged

即 **Error Map 是记 failed cycles 还是全部 cycles，可以在执行前由外部程序设定**。

### 3. 判定与执行状态的查询

`TestsuiteProxy.isPass()`（`.23`）与 `isExecuted()`（`.21`）——外部程序可查某 site 的
pass/fail 与是否执行过。

### 4. 事件流

HVM API 的 `GetLastEvent`（`02.09.01.10.03.02.02.25`）与 EDL 事件（如 die 完成事件）
构成结果数据的推送面。

### 5. 产物文件

`DataManager`（`02.09.01.09.02`）中与结果相关的文件标识：`dm_emap`（error map）、
`dm_fam`（fail map）、`dm_report`、`dm_scan_res`、`dm_dataform`，配 `dm_load` / `dm_save` /
`dm_merge` / `dm_copy_in` / `dm_delete`。

> **改判记录。** 本页上一版 L3 写「文档未覆盖」，理由是「`02.09_Test_Program_Management`
> 下的 HVM API / Test suite control API **文档未把它们与结果数据的读取关联起来**」。
> **那一句是错的**——`02.09.01.16.02` 的标题就是 "How to capture the test result in real
> time"，就在同一章 `02.09.01` 里。上一版没翻到 `02.09.01.16` 这一节就下了结论。已改。

### SmartShell 仍然不可用

`02.15_SmartShell` 的 Functional changes 明写 `Introduced in SmarTest 8.2.5`，
本 wiki 面向 7.10.3，该章仅 1 篇且正文全是 PDF 外链。**不拿它当可用的 L3 结果接口。**
"""

# ─────────────────────────── pattern（只换尾句 + 补 DataManager）─────────
PATTERN_OLD = """**本阶段其余 L3 能力：**

文档未覆盖"""

PATTERN_NEW = """**本阶段其余 L3 能力：**

文档事实（`02.09.01.14.02.01`）：pattern / sequencer 一族只有 label 两个成员
（`.09` get / `.29` set），上面已列全；除此之外 `TestsuiteProxy` 里与本阶段相关的是
`.22` `isMultiportTiming()` / `.27` `setMultiportTiming()`（multiport timing，归 [[timing]]）。

程序侧的产物文件接口（[[tpi-program-routines]]，`02.09.01.09` 全章 31 篇）：`DataManager`
（`02.09.01.09.02`）中 `dm_vector` = 向量/pattern 文件，文档在其说明里明写这个文件标识
**also to save a pattern master file**；另有 `dm_pattern_master_file`、`dm_plinit` /
`dm_pload`（pattern load）、`dm_bitmap`、`dm_del_optimize` / `dm_optimize_utd` /
`dm_optimize`（pattern 优化相关），各配 `dm_load` / `dm_save` / `dm_merge` /
`dm_copy_in` / `dm_delete`。

横切入口（session / execute / `isPass`）见 [[test-suite-control-api]]——
`executeActiveSites()` / `isPass()` 与 [[run]]、[[results]] 共用，本页不复述。"""

# ─────────────────────────── pin（补 L3 + 修假断言）─────────
PIN_OLD = """- **pin 配置本身的 L3 接口：文档未覆盖。**"""

PIN_NEW = """- **pin 配置本身的 L3 接口：有，两处。**
  - **`DataManager`（[[tpi-program-routines]]，`02.09.01.09.02`）**：文件标识里
    `dm_config` = pin configuration setup 文件、`dm_attrib` = pin attribute setup、
    `dm_catr` = channel attributes，配 `dm_load` / `dm_save` / `dm_merge` /
    `dm_copy_in` / `dm_delete` 五个操作。文档自述该接口是
    「the mirror image of the interactive interface」——**即 Pin Configuration GUI 的程序化镜像**。
  - **`HpFwTask`（`02.09.01.09.21`）**：文档事实是「allows direct access from a C program to
    the system hardware **at firmware level**」——即从 C 程序直接下发 pin 固件命令。
    注意同篇的注意事项：**它不像 test method API 那样自动处理 site focus**；
    不先下发 site focus 命令时，setup 类命令取默认 focus（通常所有 site），
    而查询类命令只返回默认 focus site 的结果，**于是各 site 的结果看起来一模一样**。

  调用方式见 `02.09.01.09` 章（TPI Program Routines）：从程序侧链接 TPI 例程，
  与 `02.09.01.14` 的 C++ 外部客户端是两条不同的通道。

> **改判记录。** 本页上一版把上面这条写成「文档未覆盖」，并另写了一句
> 「**tpi 调用的具体签名在本语料里没有**（指向另一本手册），不臆造」。
> **那一句是错的**：`02.09.01.09` 全章 31 篇就是 TPI（Test Program Interface）例程的签名，
> 例如 `02.09.01.09.14_GetSiteInFocus` 就有完整签名
> `VOID GetSiteInFocus(INT32 *site_in_focus);` 和用例；
> `02.06.10.01.07.01_Example` 也明写 SetSiteInFocus 属 "TPI (Test Program Interface)"。
> 正确说法是：**PACT / PQFC 的 CAUTION 指向的那本《Test Flow Programming in C》手册
> 不在本语料**，但**同样的 TPI 例程在本语料的 `02.09.01.09` 章里有签名**。已改。

**横切入口**（session / execute / `isPass`）见 [[test-suite-control-api]]——它不由本阶段独占，
本页不复述。"""

# ─────────────────────────── project / run / testflow（追加）─────────
PROJECT_ANCHOR = """推断：这三个接口属于 [[run]] / [[results]] 阶段的候选 L3，而不是本阶段；本阶段的 L3 就是 STPM + smartest_mfh + switch_version。"""

PROJECT_NEW = PROJECT_ANCHOR + """

### 补：程序侧的产物文件接口（[[tpi-program-routines]]）

文档事实（`02.09.01.09.02_DataManager`）：`DataManager` 提供从程序内访问 SmarTest Test
Program Explorer 的接口，「the mirror image of the interactive interface」。与本阶段相关的
文件标识是 `dm_testprog`（test program 文件）与 `dm_testflow`（testflow 文件），
配 `dm_copy_in` / `dm_load` / `dm_save` / `dm_merge` / `dm_delete`。
`DataManager` 的 Opc 参数取值即 `dm_load` / `dm_save` / `dm_merge` / `dm_copy_in` / `dm_delete`。

这与本页上面第 1 条的 STPM 是**两条不同的通道**：STPM 是命令行工具（生成/管理 device 目录），
`DataManager` 是从程序内操作产物文件。

### 层归属（**推断**，留待复核）

`02.09.01.09` 章自述 TPI 例程是「available for writing test flow programs」，
而本 wiki 的 L3 定义是「外部控制」。把它记在 L3 的理由：①它自述是 GUI 的**程序化镜像**，
操作的是整个测试程序的产物文件集，不是执行期 test method 内的 API；②`HpFwTask` 明写
「will not automatically handle site focus **as test method APIs do**」——**文档自己把它和
L2 的 test method API 对立起来**。**存疑**：文档未明说调用者是 testflow 程序还是外部程序。"""

RUN_ANCHOR = """**推断**：`setSiteInFocus` / `setActiveSites` 与 `[[site-control-window]]` 是同一件事的外部化——L3 可以在不点 GUI 的情况下切 focus site 与 active sites。"""

RUN_NEW = RUN_ANCHOR + """

### 2b. 同族的横切成员

`TestsuiteProxy` 里与本阶段直接相关的还有 `.21` `isExecuted()` 与 `.23` `isPass()`——
执行状态与判定查询，与 [[results]] 共用，见 [[test-suite-control-api]]。

### 3b. TPI 例程（[[tpi-program-routines]]，`02.09.01.09` 全章 31 篇）

文档事实：本阶段在此章可用的有 `ExecMonitor`（`.03`）、`GetSiteInFocus` / `GetActiveSites` /
`GetEnabledSites` / `GetSiteState` / `GetNumberOfSites`（`.14` / `.05` / `.08` / `.15` / `.13`）、
`GetLoadedTestflowName`（`.12`）、`GetConnectState`（`.04`）、`GetTechPath` / `GetDevPath`
（`.16` / `.07`）、`HpFwTask`（`.21`，固件级直接访问）等。

**注意 site focus 陷阱**（`02.09.01.09.21` 文档事实）：经 `HpFwTask` 下发的命令
**不像 test method API 那样自动处理 site focus**。不先下发 site focus 命令时，setup 类命令
取默认 focus，查询类命令只返回默认 focus site 的结果，**各 site 结果看起来一样**。
本阶段恰好是「看各 site 执行状态」的阶段，这个陷阱直接相关。"""

TESTFLOW_ANCHOR = """**建议：** 本阶段的 testflow 组装走 Testflow Tool（人）或直接改 testflow 文件 / `smartest_mfh`（自动化），不要指望 HVM 或 SmartShell。"""

TESTFLOW_NEW = """**补：Test suite control API 的 flag 读写**（`02.09.01.14.02.01.17` / `.33`）

文档事实：`getTestsuiteFlag()` / `setTestsuiteFlag()` 是 test suite 级 flag 的外部读写口。
与上面 CI_CPI 的 `GetTestsuiteFlag` / `SetTestsuiteFlag`（`02.09.01.08.05.02.02`）
**是两套不同的接口**，都作用于 test suite flag：CI_CPI 从 testflow 程序内访问，
TestsuiteProxy 从外部客户端访问。不要把它们当成同一个。

**补：程序侧的产物文件接口**（[[tpi-program-routines]]）

`DataManager`（`02.09.01.09.02`）的 `dm_testflow` = testflow 文件，配 `dm_copy_in` 等操作；
STPM control file 的 `mtp_device_testflow` 也指向 testflow 文件——**三套通道都指向同一个
`.tf` 产物**，见本页「产物」小节。

""" + TESTFLOW_ANCHOR


def replace_l3(page: str, new_text: str) -> bool:
    p = STAGES / f'{page}.md'
    s = p.read_text(encoding='utf-8')
    m = re.search(r'^## L3 .*?(?=^## )', s, re.S | re.M)
    if not m:
        print(f'  !! {page}: 找不到 ## L3 小节')
        return False
    s2 = s[:m.start()] + new_text.rstrip() + '\n\n' + s[m.end():]
    p.write_text(s2, encoding='utf-8')
    print(f'  ok {page}: L3 {len(m.group(0))} -> {len(new_text)} 字节')
    return True


def replace_str(page: str, old: str, new: str) -> bool:
    p = STAGES / f'{page}.md'
    s = p.read_text(encoding='utf-8')
    if old not in s:
        print(f'  !! {page}: 锚点没找到')
        return False
    if s.count(old) != 1:
        print(f'  !! {page}: 锚点出现 {s.count(old)} 次，不唯一')
        return False
    p.write_text(s.replace(old, new), encoding='utf-8')
    print(f'  ok {page}: 局部替换')
    return True


if __name__ == '__main__':
    print('整段改写 L3：')
    for k in ('level', 'timing', 'testmethod', 'results'):
        replace_l3(k, NEW[k])
    print('局部替换：')
    replace_str('pattern', PATTERN_OLD, PATTERN_NEW)
    replace_str('pin', PIN_OLD, PIN_NEW)
    replace_str('project', PROJECT_ANCHOR, PROJECT_NEW)
    replace_str('run', RUN_ANCHOR, RUN_NEW)
    replace_str('testflow', TESTFLOW_ANCHOR, TESTFLOW_NEW)
