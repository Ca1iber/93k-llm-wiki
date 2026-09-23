# TDC 语料抽取 —— 验证报告

语料：`F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category`
产出：`F:\master-dev\understand-anything-wiki\extract`

设计原则：**每一个抽取结果，都要有一个独立来源的数字可以对账。**
对不上就必须解释；解释不了就是 bug。任何「跳过」都必须出现在报告里。

## 第一类 · 内部一致性（脚本自证）

| 检查 | 判据 | 实测 | 结果 |
|---|---|---|---|
| docs.jsonl 行数 == 实扫文件数 | 9398 | 9398 | ✅ |
| 边总数 == 所有文档出度之和 | 53102 | 53102 | ✅ |
| edges 的 from 全部存在于 docs | 0 | 0 | ✅ |
| 悬空边数（`resolved=false`） | 0 | 0 | ✅ |
| hubs.csv 行数 == docs.jsonl 行数 | 9398 | 9398 | ✅ |
| `in_src` 列求和 == 正文边的去重 (来源,目标) 对数 | 32124 | 32124 | ✅ |
| `in_src` > `in_inline` 的行数（去重来源不可能多于出现次数） | 0 | 0 | ✅ |
| `in_src` 与 `in_inline` 一者为 0、另一者非 0 的行数 | 0 | 0 | ✅ |

**入度表总和** == 边总数：53102（由 `hubs.csv` 的 `in_all` 列求和得到）

**全库 53,102 条边的目标文件全部存在，悬空链接 0 条。** 这不是「差不多」，是语料自带的完整性——HTML→MD 转换把链接目标一并搬了过来，没有断链。

## 第二类 · 与独立测量对账

三条独立路径：**shell（grep/find）** / **朴素 Python 计数** / **extract.py**。
三方互不共享代码。

| 指标 | shell | 朴素 Python | extract.py | 差 | 结论 |
|---|---|---|---|---|---|
| 语料文件数 | 9398 | 9398 | 9398 | 0 | ✅ 完全一致 |
| 总字节（原始文件大小） | 28122233 | 28122233 | 28122233 | 0 | ✅ 完全一致 |
| `](<` 出现次数 | 52578 | 52578 | 51699 | -879 | 见备注 |
| 含 .md 链接的文档数 | 7104 | — | 7103 | -1 | 见备注 |
| 以 `#` 开头的行数 | 43674 | — | 42660 | -1014 | 见备注 |
| 带代码块的文档数 | 4006 | — | 4006 | 0 | ✅ 完全一致 |

差异备注：

- **语料文件数**：必须严格相等
- **总字节（原始文件大小）**：必须严格相等
- **`](<` 出现次数**：两列**不可直接相减**：shell 数「`](<` 这个串出现几次」，extract 数列的是「`RE_ANGLE` match 有几个」。52,578 = 围栏内伪链接 410 + 空目标 `](<>)` 442 + 被 match 覆盖 51,724 + 真残差 2，已完整归因（见下）
- **含 .md 链接的文档数**：两列口径不同：shell 数「文件里有 `](<….md>)` 这个串」，extract 数「文件有 out_degree>0 的边」。shell 7104 − extract 7103 = 1，拆成 仅 shell 有 6 篇 − 仅 extract 有 5 篇，见下
- **以 `#` 开头的行数**：43,674 = 围栏外 ATX **42,660**（= extract 提取的） + 围栏内 `#include` 922 + 围栏外非 ATX 92，见下
- **带代码块的文档数**：口径同：文件里有没有围栏。`grep` 与 extract 都只看有没有，不看是否闭合

### 「含 .md 链接的文档数」差 1 的逐文件归因

**仅 shell 有、extract 无（6 篇）** —— `.md` 链接只出现在**代码围栏内**，`extract.py` 正确地不认（shell 的 `grep` 没有围栏概念）：

- `02_System_reference/02.10_Data_Logging/02.10.01.04.02.22_DRLFailingAddressCountAttr.md`
- `02_System_reference/02.10_Data_Logging/02.10.01.04.02.24_DRLFailingAddressesAttr.md`
- `02_System_reference/02.10_Data_Logging/02.10.01.04.02.51_DRLPinSpecificAddresses.md`
- `02_System_reference/02.10_Data_Logging/02.10.01.04.02.52_DRLPinSpecificCounts.md`
- `02_System_reference/02.10_Data_Logging/02.10.01.04.02.62_DRLResultPinName.md`
- `02_System_reference/02.10_Data_Logging/02.10.01.04.02.86_DRLTestConditionAttr.md`

**仅 extract 有、shell 无（5 篇）** —— 用 **plain 语法** `[x](y.md)`（不带尖括号），shell 的 `\]\(<` 口径天然抓不到：

- `00_Overview/index.md`
- `01_Getting_started/index.md`
- `02_System_reference/index.md`
- `03_Use_cases_and_application_papers/index.md`
- `99_Unlisted_or_Unreferenced/index.md`

**6 − 5 = 1**，与主表中 `7104 − 7103 = 1` 严格吻合。

### 「以 `#` 开头的行数」差 1,014 的三分类归因

`grep '^#'` 只知道「行首是不是 `#`」，**不知道围栏、也不知道 ATX 语法**。
差额必须拆成下面三类，且三类之和 == grep 的总数：

| 类别 | 条数 | 为什么不算标题 |
|---|---|---|
| 围栏外真 ATX 标题 | 42,660 | **算**，等于 extract 的 `heading_count` 合计 |
| 围栏内以 `#` 开头 | 922 | C 代码里的 `#include` / `#define`，在代码块内 |
| 围栏外非 ATX | 92 | 畸形标题：`###`（无文字）、`#01 …`、`#####: …` |
| **合计** | **43,674** | == shell 的 `grep` 结果 |

校验：42,660 + 922 + 92 = 43,674，与主表 shell 列严格吻合。

因此 `grep` 的 43,674 与 extract 的 42,660 差的 1,014 条**全部有归宿，无一条含糊**。

> 📌 **计划里记的旧基线 43,674 在这一项上是可复现的**（不同于 50,073 那种无法复现的数）。
> 它恰好等于「行首是 `#` 的总行数」，因此**独立佐证了 extract 的围栏状态机**：
> 若 extract 少算了围栏外任何一条标题，或把围栏内 922 条 `#include` 误当标题，
> 这个等式立刻不成立。

### `](<` 差额的完整归因（残差逐条披露）

铁律：差异只有三种归宿 —— **脚本 bug / 基线工具不准 / 语料本身如此**。没有第四种。

```
shell `](<` 总数                 52,578
  − 围栏内伪链接                −   410   语料事实：代码块里的示例
  ────────────────────────────────────
  = 围栏外 `](<`                 52,168
      − 空目标 `](<>)`          −   442   语料事实：转换产生的空锚
      − 被 RE_ANGLE 命中区间覆盖 −51,724   51,699 个 match，其中 25 个各覆盖 2 个
      ────────────────────────────────
      = 未被覆盖（真残差）            2
  ────────────────────────────────────
  校验 442 + 51,724 + 2 = 52,168   ✅ 与围栏外总数相等
```

**那 25 个「一个 match 覆盖 2 个 `](<`」是什么：**

形态为 `[![close.png](<x.png>)](<javascript:…>)`。正则的 text 组是贪婪的，
从最外层那个 `[` 起会一路吃到 `…/close.png>` 才回头找 `](<目标>)`，
于是**把内层图片链接的 `](<` 也一并覆盖**。这不是漏抽，是匹配跨度比直觉大。

代价已核实为 **零**：这些 match 的目标是 `javascript:…`，`classify_target` 判为 `external`，**不落边**——
`edges.jsonl` 里 `javascript` 目标 **0 条**。内层 `close.png` 是图片资源，本就不进文档图。

> ⚠️ 反面教材（已修正）：最初用 `行内 ](< 数 − 空目标数 − match 数` 做减法，
> 该式**默认每个 match 只吃一个 `](<`**，于是凭空造出 25 条不存在的「残差」。
> 改为**位置法**（逐个 `](<` 判断是否落在 match 区间内）后残差从 27 降到 2。
> **能对上的算术不等于对的算术。**


**全部 2 条残差（不抽样，一条不漏）：**

| # | 文件:行 | 归类 | 原文 |
|---|---|---|---|
| 1 | `by-category/00_Overview/00_SmarTest_7.10.3_Documentation.md:10` | split | `](<../01_Getting_started/01_Getting_started.md>)` |
| 2 | `by-category/03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.08.10_Verigy_V93000_Direct-Probe__Evolution_of_the_Verigy_V93000_SOC_Tester_in.md:60` | html | `<section class=](<../../../../raw/129497.png>)` |

逐条归因：

- **html（1 条）**：`\t\t<section class=](<../../../../raw/129497.png>)` —— HTML→MD 转换把 `<section class="…">` 的属性值吃掉了，行内根本没有前置 `[`。markdown-it 同样不认为是链接。**语料缺陷，目标也不是 .md。**
- **split（1 条）**：`00_Overview/00_SmarTest_7.10.3_Documentation.md:6,10` ——

  ```
   6| [
   7| 
   8| ## Getting started
   9| 
  10| ](<../01_Getting_started/01_Getting_started.md>)
  ```

  链接文字 `[` 与 `]` 被一个 H2 隔开。CommonMark 规定链接文字不能跨空行，
  **所以 markdown-it 也判它不是链接**——这正是第三类 B−A=0 的原因。
  两套实现独立地得出同一结论，故这是**语料转换缺陷**，不是正则漏抽。
  代价：`01_Getting_started.md` 少一条入边（全库 53,102 条中的 1 条）。
  此处**不做补偿性抽取**——凭空补一条语料没表达的边，会破坏三路一致性。

### 两个正则 → 落边：完整对账

`extract.py` 只把 `classify_target` 判为 `doc` 的链接落成边，其余只计数。
所以「命中数」必然大于「边数」，差额必须**分毫不差**地等于非 doc 目标数：

| 环节 | 数量 |
|---|---|
| `RE_ANGLE` 命中 | 51,699 |
| `RE_PLAIN` 命中 | 9,393 |
| **合计命中** | **61,092** |
| − 非 `doc` 目标 | −7,990 |
| **= 落成的边** | **53,102** |

非 `doc` 目标细分：`asset` 6,471 / `anchor` 1,350 / `external` 140 / `other` 29

**三条交叉校验：**

1. 落成的边 53,102 == `edges.jsonl` 行数 53,102 == `doc` 类目标 53,102 ✅
2. `RE_PLAIN` 命中 9,393 == `toc` 边数 9,393 ✅ → 5 个 `index.md` 的目录链接**全部**是 plain 语法，无一条混用尖括号
3. 于是 `RE_ANGLE` 贡献的 `doc` 边 = 53,102 − 9,393 = 43,709 == `inline` 边数 43,709 ✅

### ⚠️ 旧基线复现性：**失败**

本次会话早期记录的基线是 **50,073 条交叉引用 / 7,076 篇含链接文档**。
这些数字**无法用任何合理的命令复现**。实测候选：

| 命令口径 | 结果 |
|---|---|
| grep '](<[^>]*\.md>)'（严格 .md> 结尾） | 40680 |
| grep -E '\]\(<[^>]*\.md[^>]*\)'（允许锚点） | 44116 |
| grep '](<'（所有尖括号链接） | 52578 |
| grep -c 按行求和 | 41862 |

**结论：旧基线的测量命令没有被记录下来，因此它不是可用的验证锚点。**
本报告一律改用上表中当场可复现的 shell 命令作为基线。
这不是「extract.py 错了」，而是「旧数字不可信」——第五类要求的「逐条解释」在此落地为：
**旧基线作废，改用可复现基线。**

### catalog 差异结案（原计划第八条）

- catalog 数据行：**9393**
- by-category 实扫：**9398**
- 磁盘有 catalog 无：**5** → ['00_Overview/index.md', '01_Getting_started/index.md', '02_System_reference/index.md', '03_Use_cases_and_application_papers/index.md', '99_Unlisted_or_Unreferenced/index.md']
- catalog 有磁盘无：**0**

**9393 + 5 = 9398，算术闭合，无遗漏无悬空。**

## 第三类 · 独立复算（markdown-it-py token 流）

- A（正则，extract.py）：**53102** 条
- B（AST，markdown-it-py）：**53042** 条
- **A 有 B 无**（正则多认）：60 条 / 39 种
- **B 有 A 无**（正则漏认）：0 条 / 0 种

✅ **B−A = 0：正则没有漏掉任何 markdown-it 能解析的链接。**

### A−B 逐条归因（由 markdown-it 块级 token 计算，非手写）

| 所处块类型 | 条数 | 说明 |
|---|---:|---|
| 反引号内联代码段 | 54 | 作者用反引号把链接**引用**起来，渲染后不是链接 |
| 缩进代码块（CommonMark 4 空格规则） | 5 | HTML→MD 转换把列表续行写成了 4 空格缩进；语料里作者的本意仍是交叉引用 |
| HTML 块 | 1 | HTML 残留（如 `<script>`）未闭合，CommonMark 把其后整段当原始 HTML；语料缺陷 |
| **合计** | **60** | 应等于 A−B 总数 60 |

✅ 归因闭合：60 = 60，**每一条都有名字**。

✅ 标记交叉校验：`edges.jsonl` 里 `in_code_span=True` 有 **54** 条，markdown-it 侧算出 **54** 条，**相等**。

其中 1 条落在 HTML 块内，逐条披露：

- `02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md:306` → `02.09.02.03_STPM_control_file.md`（块范围 33–310 行）

**这 6 条边一律保留，未丢弃，也不再另加标记。** 判决属于计划里的第三类归宿
「语料本身如此 → 记录」：目标都是真实存在的 `.md`，作者本意确为交叉引用，
只是 HTML→MD 转换把块结构写坏了（4 空格缩进 / `<script>` 未闭合）。
删掉它们会丢真引用。**它们不参与 `in_code_span` 过滤**——那 54 条是作者在「引用」链接，
这 6 条是作者在「写」链接，性质相反，已逐条点名披露，下游按上面的清单处理即可。

### `in_code_span` 标记的影响面（排序是否因过滤而变）

- 被标记的边 **54** 条，分布在 **9** 篇。
- 入度 Top20 过滤前后：**完全一致**。
- 出度 Top20 过滤前后：**2 处名次交换**，但两篇都仍在 Top20 内（仅换位，未出榜）：
  - 第 18 名 `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.07_Error_handling.md` ↔ `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.03_DPS128____PS64_functionality_and_features.md`
  - 第 19 名 `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.03_DPS128____PS64_functionality_and_features.md` ↔ `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.07_Error_handling.md`
- 单篇占比最高：`02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md`，出度 14 条中被标记 **8 条（57%）**。

**结论**：`hubs.csv` 的排序在 Top20 层面不因过滤而改变，**按入度挑 `object` 页不受影响**；但 GIO API 族单篇出度最多虚高 57%，按**出度**判断「枢纽」时需知情。标记已入 `edges.jsonl`，过滤与否由下游决定。

## 第五类 · 解析失败清单（不许静默丢弃）

共 **71** 条。

| 类型 | 数量 | 说明 |
|---|---|---|
| `no_headings` | 51 | 全文无任何标题。集中在 99_Unlisted 的 Doxygen 残页 |
| `no_h1` | 10 | 有标题但无 H1。title 保持 None，**不 fallback 到文件名** |
| `no_frontmatter` | 5 | 缺 frontmatter。已知 = 5 个分类目录的 index.md |
| `not_in_catalog` | 5 | 不在 catalog-markdown.csv 里。已知 = 5 个 index.md |

**`no_h1`** 样例：

- `00_Overview/00_SmarTest_7.10.3_Documentation.md` ``
- `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md` ``
- `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md` ``
- `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md` ``
- `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.04_Operations_specific_to_RS-232_devices.md` ``

**`no_frontmatter`** 样例：

- `00_Overview/index.md` `文件首行不是 ---`
- `01_Getting_started/index.md` `文件首行不是 ---`
- `02_System_reference/index.md` `文件首行不是 ---`
- `03_Use_cases_and_application_papers/index.md` `文件首行不是 ---`
- `99_Unlisted_or_Unreferenced/index.md` `文件首行不是 ---`

**`not_in_catalog`** 样例：

- `00_Overview/index.md` ``
- `01_Getting_started/index.md` ``
- `02_System_reference/index.md` ``
- `03_Use_cases_and_application_papers/index.md` ``
- `99_Unlisted_or_Unreferenced/index.md` ``

**`no_headings`** 样例：

- `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07_GIO_API_reference.md` ``
- `99_Unlisted_or_Unreferenced/99.0191_SmartProd_API_reference__Class_Index.md` ``
- `99_Unlisted_or_Unreferenced/99.0192_SmartProd_API_reference__Class_Members.md` ``
- `99_Unlisted_or_Unreferenced/99.0193_SmartProd_API_reference__Class_Members_-_Enumerations.md` ``
- `99_Unlisted_or_Unreferenced/99.0194_SmartProd_API_reference__Class_Members_-_Enumerator.md` ``

**判据 1 · 悬空链接比例**：

- `.md` 边总数 **53,102**
- 其中悬空（目标文件不存在）**0** → 比例 **0.0000%**

**判据 2 · 无未知原因条目**：

- 出现的失败类型 ['no_frontmatter', 'no_h1', 'no_headings', 'not_in_catalog']
- 全部落在已知集合内（['dangling_link', 'decode_error', 'fm_parse_failure', 'no_frontmatter', 'no_h1', 'no_headings', 'not_in_catalog', 'unclosed_fence']）✅

以上每一类都对应语料的真实缺陷，不是解析器静默丢弃的证据。

## 第六类 · 幂等性

第一次运行的 sha256：

| 文件 | sha256 |
|---|---|
| `docs.jsonl` | `37ffcd630d7bb7df1ac26282cbf4a92c…` |
| `edges.jsonl` | `4af89376e61faa85d67b8877120b4eca…` |
| `sections.jsonl` | `ab1e993413c79bdc984f49f03d5c6257…` |
| `failures.jsonl` | `7ddf428deecf5d8fe6894f7a1d4de09a…` |
| `hubs.csv` | `e0b6177afee3deb1c0762bae31f02b7f…` |

| 文件 | 两次是否逐字节相同 |
|---|---|
| `docs.jsonl` | ✅ 相同 |
| `edges.jsonl` | ✅ 相同 |
| `sections.jsonl` | ✅ 相同 |
| `failures.jsonl` | ✅ 相同 |
| `hubs.csv` | ✅ 相同 |

✅ **两次运行输出逐字节相同。**
顺序化（`walk()` 排序 + 无并发 + `sort_keys=True`）的目的正在于此——
并发写入会让行序不可复现，这一条就过不了。

## 第七类 · 反向抽样（回归验证）

随机抽 **50** 条边（种子 20260917，可复现），回到原文逐条 grep。

- ✅ 命中：**50**
- ❌ 未命中：**0**

✅ **50 条全部命中：源文件、行号、目标串三者对齐，无错位。**

## 第四类 · 分层抽样人工核对

抽样位 **53** 个 → 去重后 **40** 篇。

> 位子多于篇数是因为同一篇会同时命中多个分层（例如「最大」又「含 Procedure」）。
> 去重只去掉重复渲染，**不减少覆盖面**；不足 40 篇时按 `rel` 等距补齐。

已生成 `spot-check.md`，共 **40** 篇。**这一份机器判不了，只能人看。**

复核记录写在 `..\wiki\log.md`：那里记的是「谁、什么时候、看了哪几篇、看出了什么、每一条怎么处置的」。**不写进本报告**——本报告是脚本生成的，把复核结论写进来会随下一次重跑变成一个没人维护的陈旧断言。

### `first_para` 的退化值（人工核对所见，逐条披露）

- `first_para` 为 `null`：**15** 篇（空文档或只有 frontmatter）
- 非空但**不含任何字母数字**：**7** 篇

| 文档 | `first_para` | 成因 |
|---|---|---|
| `00_Overview/00_SmarTest_7.10.3_Documentation.md` | `[` | HTML→MD 转换把链接文字与目标切到了两行，首行只剩一个 `[` |
| `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.09.01_d2w_parameters.md` | `-` | 空链接残渣 `[](<>)`，或孤立的列表符 |
| `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md` | `[](<>)` | 空链接残渣 `[](<>)`，或孤立的列表符 |
| `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md` | `[](<>)` | 空链接残渣 `[](<>)`，或孤立的列表符 |
| `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.05_Asynchronous_events.md` | `[](<>)` | 空链接残渣 `[](<>)`，或孤立的列表符 |
| `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.06_Session_parameters.md` | `[](<>)` | 空链接残渣 `[](<>)`，或孤立的列表符 |
| `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.08_Formatted_I_O.md` | `[](<>)` | 空链接残渣 `[](<>)`，或孤立的列表符 |

**处置：不改抽取规则，点名披露。** `first_para` 是计划里冻结的「正文第一段」，改规则就得把 9,398 篇重验一遍，而这里只有 7 篇受影响（0.07%），成因就是已披露的转换残渣。**建页时这 7 篇不要用 `first_para` 当摘要**，改用 `frontmatter.title` 或首个 H2。

### 第四类附 · 全库行号回验（穷举，非抽样）

| 断言 | 条数 | 回验不符 | 结论 |
|---|---|---|---|
| 标题行号 + 层级 + 文本 | 42,660 | 0 | ✅ 全部属实 |
| 边的行号 + 目标串 | 53,102 | 0 | ✅ 全部属实 |
| 结构段落的标题行号 | 23,315 | 0 | ✅ 全部属实 |

**穷举结论**：42,660 个标题 + 53,102 条边 + 23,315 个结构段落，每一条「第 N 行」的断言都回到原文核对属实，**无一处错位**。

### 第四类附 · 语境保真（穷举，非抽样）

| 情形 | 条数 | 说明 |
|---|---|---|
| 逐字命中 | 48,704 | ✅ 语境里原样含 `to_raw` |
| 因截断未含 | 4,398 | 语境 300 字符上限；再分两类见下 |
| &nbsp;&nbsp;↳ 刀口切在目标中间 | 1,856 | 目标**前缀**在语境末尾，切点之前逐字忠实 |
| &nbsp;&nbsp;↳ 目标整体在切点之后 | 2,542 | 语境内无目标任何片段，链接在截断点之后 |
| 仅空白不同 | 0 | 目标串自身含空格，被 `\s+ → 单空格` 折叠 |
| **其他** | **0** | ✅ 为 0，无语境被改坏 |

合计 48,704 + 4,398 + 0 + 0 = 53,102 == 边总数 53,102 ✅

截断细分的自洽：1,856 + 2,542 = 4,398 == 因截断未含 4,398 ✅

### 第四类附 · 全库段落正文回验（穷举，非抽样）

- 段落总数 **23,315**（`body` 已按上限截断的 132 条按截断后比对）
- 正文与原文切片**逐字符相同**：**23,315** 条
- 不一致：**0** 条

✅ 23,315 + 0 = 23,315 == 段落总数，**全部逐字符对齐**。

## 交付物字段说明（交接契约）

| 文件 | 行数 | 一行是什么 |
|---|---:|---|
| `docs.jsonl` | 9,398 | 一篇文档（机械索引） |
| `edges.jsonl` | 53,102 | 一条交叉引用（源→目标） |
| `sections.jsonl` | 23,315 | 一个结构段落 |
| `hubs.csv` | 9,398 | 一篇文档的入度/出度排名 |
| `failures.jsonl` | 71 | 一条解析异常（**没有任何东西被静默丢弃**） |

### `edges.jsonl`

| 字段 | 含义 | 易错点 |
|---|---|---|
| `from` | 源文档，相对语料根的 posix 路径 | 等于 `docs.jsonl.rel` |
| `to` | 目标文档，**从源文档出发解析并归一化**后的路径 | 解析失败时为 `null`，要看 `to_raw` |
| `to_raw` | 原文里链接目标**一字不改**的原始串 | 带 `#anchor`、`../`、URL 编码；**别拿它当路径用** |
| `resolved` | `to` 指向的文件是否真实存在 | `false` = 悬空链接 |
| `line` | 链接所在行号（1 起） | 已由第四类附穷举回验 |
| `context` | 链接所在那一行（必要时上并，≤300 字符） | 超 300 会被截断，**截断不等于出错** |
| `link_text` | 方括号里的文字 | 可能是嵌了图片的复合串 |
| `kind` | `toc`（来自 5 个 `index.md` 的目录）或 `inline`（正文里的引用） | **两者语义完全不同，做入度排名时别混** |
| `anchor` | `to_raw` 里 `#` 之后的部分 | 无锚点时为 `null` |
| `in_code_span` | 链接写在反引号里，作者是在**引用**它，渲染后不是链接 | 共 54 条；见第三类「影响面」一节 |

**只有 `to` 指向 `.md` 的链接才建边。** 图片、页内锚点、外部 URL、`.htm/.pdf` 等资源按类型计入 `docs.jsonl.link_kinds`，不进 `edges.jsonl`。

### `sections.jsonl`

| 字段 | 含义 | 易错点 |
|---|---|---|
| `doc` | 所属文档 | |
| `h2` | 段落的标题原文 | 名字取自固定名单；`### Member functions` 这种**低层级结构标题也算一段** |
| `group` | `syntax`/`version`/`related`/`procedure`/`constraint`/`concept`/`error` | 建 `error`/`version`/`constraint` 页时按这个字段筛 |
| `line` | **段落标题所在行**，不是正文起始行 | ⚠️ **正文从 `line + 1` 开始**，别当正文行号用 |
| `chars` | **截断前**的正文长度 | 与 `len(body)` 不等时说明被截断 |
| `truncated` | 正文是否超过 6000 字符上限 | `true` 时 `body` 只有前 6000 字符 |
| `body` | 段落正文，各行用 `\n` 连接、首尾去空白 | 含段落内子标题行；**不含**闭合本段的那个标题行 |

### `docs.jsonl`

| 字段 | 含义 | 易错点 |
|---|---|---|
| `rel` | 相对语料根的 posix 路径，**全库唯一键** | |
| `title` | H1 的文字 | **没有 H1 就是 `null`，不 fallback 到文件名**——fallback 会把「没有标题」伪装成「有标题」 |
| `frontmatter` | 解析出的 YAML；解析不了的行走 `failures.jsonl` | 5 个 `index.md` 为 `null` |
| `headings` | 全部标题 `{level, text, line}` | 42,660 条已逐行回验 |
| `first_para` | 正文第一段，≤300 字符 | 有退化值，见第四类「`first_para` 的退化值」 |
| `struct_sections` / `struct_groups` | 该文档命中的段落名与所属组名单 | 与 `sections.jsonl` 互为索引 |
| `out_degree` / `edge_angle` / `edge_plain` | 出度，以及两种正则各自的命中数 | `edge_angle + edge_plain` 减去非 `doc` 目标 == `out_degree` |
| `link_kinds` | 该文档各类链接目标的计数（`doc`/`asset`/`anchor`/…） | **非 `doc` 的不建边，但计数留着** |
| `is_index` / `in_catalog` | 是否 5 个 `index.md` 之一 / 是否在 catalog-markdown.csv 里 | |
| `bytes` / `chars` / `code_blocks` / `heading_count` | 体积与结构计数 | |

### `hubs.csv`

| 列 | 含义 |
|---|---|
| `path` | 文档路径 |
| `in_all` | 入度（含 `toc` 边） |
| `in_inline` | 入度（**只算 `kind=inline`**）。**这份文件就是按它降序排的** |
| `out` | 出度 |
| `is_index` | 是否目录页。`index.md` 的入度靠 TOC 撑起来，**挑 `object` 页时通常要排除** |

⚠️ **两个入度都只计 `resolved=true` 的边**——悬空链接不入度，否则入度表总和会对不上。本库悬空链接为 **0** 条，所以 `in_all` 合计 53,102 恰好等于边总数 53,102；**一旦语料里出现悬空链接，这两个数就会分叉**，对账时别忘了这条。

两个入度的差就是 TOC 的份量：`toc` 边 9,393 条（占全部边的 17.7%），`inline` 边 43,709 条。**做「谁被引得多」的判断必须用 `in_inline`**——用 `in_all` 的话，凡是在目录里出现过的文档都会被 TOC 灌一遍水。

## 汇总

| 检验 | 结果 |
|---|---|
| 第一类 内部一致性 | ✅ 通过 |
| 第二类 基线对账 | ✅ 通过 |
| 第三类 独立复算 | ✅ 通过 |
| 第五类 失败清单 | ✅ 通过 |
| 第六类 幂等性 | ✅ 通过 |
| 第七类 反向抽样 | ✅ 通过 |
| 第四类 分层抽样 | ⚠️ 见正文 |
| 第四类附 行号回验 | ✅ 通过 |
| 第四类附 语境保真 | ✅ 通过 |
| 第四类附 段落正文 | ✅ 通过 |

**第四类机器判不了。** 自动对账查得出「数字对不上」，查不出「解析对了但语义错了」；
反过来，上面前九行全绿也只说明数字自洽，不说明数据可用。

**放行条件**：`spot-check.md` 的 40 篇逐条看过，且复核发现的每一条差异都
落进计划里那三种归宿之一——**（a）脚本 bug → 修；（b）基线工具不准 → 记录并说明；
（c）语料本身如此 → 记录。没有第四种，「先放着」不算。**
复核记录见 `..\wiki\log.md`；本条不通过前，这批数据视为**未放行**，不得用于建页。
