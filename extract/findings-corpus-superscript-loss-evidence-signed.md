# D 类修复证据表 —— 带符号指数被拍平（`10<sup>-9</sup>` → `10-9`）

与 A 类**同一个机制**，只是上标带正负号，A 类的正则（`\d{1,3}`）漏掉了它们。
**只改 markdown，HTML 不动。**判据与流程见 `schema.md` §1.2。

共 **3** 处。

| # | markdown | 源 HTML | 指数 | 改前 | 改后 |
|---|---|---|---|---|---|
| 1 | `02_System_reference/02.06_Command_Reference/02.06.06.01.06.01_Avoiding_rounding_problems_with_the_fract___function.md` | `124790.htm` | `0^-9` | `tly from the fract() definition with expanded precision as 10-9 Hz (nHz). Then the actual use` | `tly from the fract() definition with expanded precision as 10^-9 Hz (nHz). Then the actual use` |
| 2 | `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.02.01.06.01_Avoiding_rounding_problems_with_the_fract___function.md` | `124790_2.htm` | `0^-9` | `tly from the fract() definition with expanded precision as 10-9 Hz (nHz). Then the actual use` | `tly from the fract() definition with expanded precision as 10^-9 Hz (nHz). Then the actual use` |
| 3 | `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.md` | `29809.htm` | `0^-9` | `() member function, the spec variable "Tp" is changed into 10-9 seconds. This is more conveni` | `() member function, the spec variable "Tp" is changed into 10^-9 seconds. This is more conveni` |
