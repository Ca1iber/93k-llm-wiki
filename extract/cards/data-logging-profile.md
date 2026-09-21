# 取证卡：`data-logging-profile`

- **状态**：悬空 wikilink 目标（被引 5）
- **引用它的页**：`wiki/objects/ci-cpi.md`、`wiki/objects/data-logging-profiles.md`、
  `wiki/concepts/edf-data-organization.md`、`wiki/mappings/mapping-results.md`、
  `wiki/stages/results.md`（各 1 处）
- **取证日**：2026-09-21

## raw

`02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.md`

- 字节：**3593 B**
- 行数：**66**
- **in_src = 23**
- topic = `98046`，单副本

## 是什么

**一组数据日志规则（`.prf` 文件）**，决定系统内**记录哪些数据**以及**怎么记**。
附带两个默认 profile：`datalog_OFF.prf` / `datalog_ON.prf`。

## 已有页

**有——但建在复数 slug 上。**

`wiki/objects/data-logging-profiles.md` 的 frontmatter `sources:` **认领的就是同一篇 raw**
（`02.10.01.02_Data_Logging_Profiles.md`）。

**同一件事？→ 是。** 两者同源同篇，只是 slug 单复数不同。
本 wiki 里**不存在**两篇不同的 raw 分别讲「一个 profile」与「profile 总览」。

## 建议

- **type = `object`**
- **layer = `file`**
- **stage = `results`**
- **处置：改链接（单数 → 复数），不建重复页。**
  `[[data-logging-profile]]` → `[[data-logging-profiles]]`（5 处）

## 依据（逐字）

> A data logging profile is a set of data logging rules that determine which data is logged within the test system and how.

> Two default data logging profiles are delivered with SmarTest: datalog_OFF.prf / datalog_ON.prf

> With data logging profiles, you can change the flag settings for optimized testflows in production without deleting the optimization.

## 风险

1. **⚠️ 改链接前必须先改 `data-logging-profiles.md` 自己的说明。**
   `wiki/objects/data-logging-profiles.md:149` 现在写着：

   > `[[data-logging-profile]]` — **同一主题的单数页**。本页是总览，它大概是「一个 profile 长什么样」那一层（**本页没有打开那页核对，也没有从本篇文档里读到它**）（推断）。

   即**那一页自己预期有一个单数页存在**。若只把 5 处引用改成复数、不动这一段，
   就会留下一条**自指且错误**的说明（复数页链向自己）。
   **两件事要一起做**，否则改完比不改更乱。
2. **in_src=23 是本组七项里最高的两篇之一**（另一篇是 `context-pins` 的 how-to，也是 23）。
   按 §12「按入度建页」的判据，它**够格建页**——但页**已经存在**（复数形式）。
   所以本项是「**已有页、只需改链接**」，不是「该建页」。
3. **同族的两篇别混**：`02.10.01.02.08_Data_logging_profile_API.md`（`[[data-logging-profile-api]]`）
   是**让 test method 在运行中切 profile 的那套 API**，与 `.prf` 文件本身是两个对象。
   `wiki/stages/results.md:435` 已经把这一层分开写过。
4. 本篇 `## Compatibility with production settings` 提到 profile 放在
   `<device directory>/profiles/` 子目录——这条**只有本篇写过**，
   `wiki/objects/ci-cpi.md:140` 也点明「profile 文件在 `profiles` 子目录里这件事**只有那一段写过**」。
