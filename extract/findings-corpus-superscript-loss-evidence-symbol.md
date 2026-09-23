# G 类修复证据表 —— 符号 / 公式上标（**按层处置**）

规矩（2026-09-23 用户定）：**哪一层错就改哪一层。**

- **raw 自己写错**：6 处 —— `<sup>` 把标点/运算符包了进去
- **markdown 丢上标**：18 处 / 15 篇 —— raw 是对的

## 一、raw 侧（改 `tdc-html/raw/`）

| # | 文件 | 改前 | 改后 | 凭什么说它错 |
|---|---|---|---|---|
| 1 | `98749.htm` | `2<sup>32-1</sup>` | `2<sup>32</sup>-1` | 同文件另有 12 处写 `2<sup>31</sup>-1`（`-1` 在上标外）——此处 `-1` 被包进去了 |
| 2 | `98749.htm` | `2<sup>16-1</sup>` | `2<sup>16</sup>-1` | 同上 |
| 3 | `98749_2.htm` | `2<sup>32-1</sup>` | `2<sup>32</sup>-1` | 同上（重投件） |
| 4 | `98749_2.htm` | `2<sup>16-1</sup>` | `2<sup>16</sup>-1` | 同上 |
| 5 | `125001.htm` | `(2<sup>n).</sup>` | `(2<sup>n</sup>).` | `)` `.` 被包进上标，渲染成 2 的「n).」次方 |
| 6 | `125003.htm` | `(2<sup>n).</sup>` | `(2<sup>n</sup>).` | 同上（重投件） |

## 二、markdown 侧（只改 `agent-markdown/`）

| # | markdown | 源 HTML | 改前 | 改后 |
|---|---|---|---|---|
| 1 | `02_System_reference/02.06_Command_Reference/02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md` | `100076.htm` | `2n` | `2^n` |
| 2 | `02_System_reference/02.06_Command_Reference/02.06.17.01_Overview_of_pseudo_random_bit_sequences.md` | `118592.htm` | `2j` | `2^j` |
| 3 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.02.21_Accurate_Incoherent_Signal_Measurement_with_RTSPU.md` | `120456.htm` | `ejwt` | `e^jwt` |
| 4 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.06.08_X-Mode_Pattern_Synchronization_to_Free_Running_Bit_Streams.md` | `123993.htm` | `2n` | `2^n` |
| 5 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.24_DC_PROFILING_DEFINE.md` | `125001.htm` | `2n` | `2^n` |
| 6 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.27_DC_PROFILING_ON.md` | `125003.htm` | `2n` | `2^n` |
| 7 | `03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.04.07_A_Novel_Dynamic_Method_to_Generate_PRBS_Pattern.md` | `129462.htm` | `2X` | `2^X` |
| 8 | `02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md` | `149558.htm` | `2n` | `2^n` |
| 9 | `02_System_reference/02.07_Test_Method_Reference/02.07.03.04.04_FS_Gain___LSB_Gain.md` | `26088.htm` | `2n` | `2^n` |
| 10 | `02_System_reference/02.07_Test_Method_Reference/02.07.13.01.10_SmartRDI_7.4.4.md` | `344019.htm` | `2n` | `2^n` |
| 11 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.03_The_X-Mode_Control_File___.cmb.md` | `37494.htm` | `nm` | `n^m` |
| 12 | `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.02.03_The_X-Mode_Control_File___.cmb.md` | `37494.htm` | `nm` | `n^m` |
| 13 | `02_System_reference/02.06_Command_Reference/02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md` | `98518.htm` | `2n` | `2^n` |
| 14 | `02_System_reference/02.06_Command_Reference/02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md` | `98530.htm` | `2n` | `2^n` |
| 15 | `02_System_reference/02.06_Command_Reference/02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `98749.htm` | `232` | `2^32` |
| 16 | `02_System_reference/02.06_Command_Reference/02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `98749.htm` | `216` | `2^16` |
| 17 | `02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `98749_2.htm` | `232` | `2^32` |
| 18 | `02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md` | `98749_2.htm` | `216` | `2^16` |

## 三、具名排除（**一个字没动**，附理由）

- `118592.htm` 的 `xj` / `xj-1`：该篇把 `<sup>` 当**下标**用（`c1*x1`、`x3`、`x0`），展平是对的
- `46266.htm` 的 `yx`：「y^x 序列」还是「y_x 序列」判不出 → **留给人**
- `344019.htm` 的 `2n-1`：raw 写 `2<sup>n-1</sup>` = 2^(n-1)，**raw 是对的**；写成 `2^n-1` 会读错，得写 `2^(n-1)` —— **这个写法要人定**
- `69125.htm` `<sup>1)</sup>`（套在 `<a href="#fn1">` 里，是脚注）、`151881.htm` `<sup>TM</sup>`（商标）、`120830.htm` `<sup>[a]</sup>`（引用标记）
- 序数后缀 `3<sup>rd</sup>` → `3rd`（99 处）：**本来就该这么写**
- 脚注标记（1,235 处）：**忠实转换，不是损坏**
