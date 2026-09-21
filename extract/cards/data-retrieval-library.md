# 取证卡：`data-retrieval-library`

- **状态**：悬空 wikilink 目标（被引 5）
- **引用它的页**：`wiki/concepts/edf-data-organization.md`、`wiki/mappings/mapping-results.md`、
  `wiki/stages/results.md`（2 处）、`wiki/objects/signal-analyzer.md`
- **取证日**：2026-09-21

## raw

`02_System_reference/02.10_Data_Logging/02.10.01.04_Data_Retrieval_Library.md`

- 字节：**1811 B**
- 行数：**27**
- **in_src = 7**
- topic = `34714`，单副本

## 是什么

**Data Retrieval Library（DRL）**——一个 **C 函数库 / API**，
提供对 **data log stream**（当前执行的生产测试的全部事件所写入的那条流）的访问。
用它就不必自己写 data log 文件的 parser。
**只在 Linux 上跑**（头文件 `/opt/hp93000/soc/com/include/drl.h`）。

## 已有页

**无** object / concept / constraint 页认领。

- `wiki/stages/results.md` 认领了（`stage`，**不算**）
- `wiki/objects/` 下没有 `data-retrieval-library.md`

## 建议

- **type = `object`**
- **layer = `L2`**（它是 API/函数库；`wiki/stages/results.md:293` 已把它归为 `L2`）
- **stage = `results`**

## 依据（逐字）

> The Data Retrieval Library (DRL) is the application programming interface (API) that provides access to the data log stream where all events of the production test currently being executed are logged

> Using the DRL frees you from the need to write parsers for data log files.

> The header file of the DRL is /opt/hp93000/soc/com/include/drl.h.

## 风险

1. **「runs only on Linux」这条只写在别处。** 本篇 raw（`02.10.01.04`）**没有**这句话；
   它是 `wiki/stages/results.md:303` 转述的另一处声明。建页时若照抄「Linux only」，
   **依据不在本篇**，要么另注出处、要么不写。
   本篇实际写的是头文件路径在 `/opt/hp93000/...`（Linux 路径），**这是间接迹象，不是明文**。
2. **同族易混篇，不要误指**：
   - `02.09.01.03.08.04_Functions_for_Data_Retrieval.md`（in_src=1）——`02.09` 是**程序管理/L3 命令行**侧，另一层的入口
   - `02.10.01.05_Developing_a_data_retrieval_function.md`——**教你写** retrieval function 的 how-to
   - `02.10.01.10.02_DRLDump_as_a_template_for_user-written_data_retrieval_tools.md`——样本工具
   这三篇都不是 DRL 本身。建页时认领的 raw 应锁死 `02.10.01.04`。
3. **注意 `[[drldump]]` 是另一个 slug**（`wiki/stages/results.md:294` 并列引用了两者）：
   DRL 是库，DRLDump 是用它写的样本工具。**建 `data-retrieval-library` 时不要把 DRLDump 的内容收进来。**
4. 本篇 `#### Subtopics` 只列两条：`DRL functions`、`DRL data types`。
   **函数清单不在本篇**，建页若声称「有哪些函数」就超出了本篇依据。
5. in_src=7 属**中等偏低**，未达 §12 常引的「≥20 算高入度」线。
   但 §12 对 `stage` 之外的 object 页判据是「入度**比不少已归属对象还高**」，
   且它有 5 处引用、跨 4 页（含 spine 页 `results`），**建页是合理的**。
