# 取证卡：`edf`

- **状态**：悬空 wikilink 目标（被引 5）
- **引用它的页**：`wiki/concepts/edf-data-organization.md`、`wiki/concepts/edf-data-types.md`、
  `wiki/mappings/mapping-results.md`（2 处）、`wiki/stages/results.md`
- **取证日**：2026-09-21

## raw

**候选 A（章节目录篇 = 最贴 slug 名的那篇）**：
`02_System_reference/02.10_Data_Logging/02.10.01.06_Event_Data_Logging_Format__EDF.md`

- 字节：**602 B**
- 行数：**14**
- **in_src = 3**
- topic = `34647`，单副本

**候选 B / C（同族的两个子篇，in_src 远高于 A）**：

| raw | 字节 | 行 | in_src |
|---|---|---|---|
| `02.10.01.06.01_EDF_data_organization.md` | 3231 B | 55 | **78** |
| `02.10.01.06.02_EDF_data_types.md` | 1136 B | 111 | **72** |

全库标题含 `EDF` 的**只有这三篇**（hubs-dedup 实测）。

## 是什么

**Event Data Logging Format（EDF）**——事件数据日志的格式族名。
⚠️ **候选 A 本篇是一张纯目录页**：正文只有一行标题 + `#### Subtopics` 五条链接，
**没有任何一句定义性文字**。

## 已有页

**无 `edf` 专页。**

- `wiki/concepts/edf-data-organization.md` 认领的是 `EDF_data_organization`（**子篇，不同 raw**）
- `wiki/concepts/edf-data-types.md` 认领的是 `EDF_data_types`（**子篇，不同 raw**）
- `wiki/objects/timestamp-attr-type.md` 的 `sources:` 也命中 `02.10.01.06` 前缀，但认领的是**别的子篇**
- `wiki/stages/results.md` 认领了（`stage`，**不算**）

**同一件事？→ 否。** 已有两页是 EDF 的**子篇**，不是 EDF 本身。

## 建议

- **type = `concept`**
- **layer = `file`**（`wiki/stages/results.md:275` 已标 `[[edf]]` `file`）
- **stage = `results`**

## 依据（逐字）

⚠️ **本篇没有任何定义句可摘。** 全文如下（除 frontmatter）：

> # Event Data Logging Format (EDF)
>
> #### Subtopics
>
> - [EDF data organization](...)
> - [EDF data types](...)
> - [Event types](...)
> - [Creating your own custom events with the DCL library](...)
> - [Attribute types](...)

**唯一的「依据」是标题本身**：`Event Data Logging Format (EDF)`。
如需一句可引的正文，**只能**退到子篇去找，例如候选 B 的开头
（但那句话讲的是**记录怎么排**，不是 EDF 的定义）。

## 风险

1. **⚠️⚠️ 本组七项里最需要注意的一项：这是个「空壳父页」。**
   候选 A **只有 602 B / 14 行，正文 0 句**——它是**章节目录页**，
   语料里**根本没有 EDF 的定义性正文**。
   若按 `concept` 建页，内容只能是「它是一个目录，子页有五个」，
   **等于把 raw 的 `#### Subtopics` 抄一遍**——没有增加任何知识。
   **不要为了消悬空而造一个语料没有的 EDF 定义。**
2. **两个子篇自己已经承认「父」关系是推断。**
   `wiki/concepts/edf-data-organization.md:132`：

   > `[[edf]]`（**未建**）— **父概念**（**同样只是命名与归属相邻，（推断）**）：**本页正文里一次都没有出现 `EDF` 这个词**——它只在标题和文件名里

   `wiki/concepts/edf-data-types.md:118` 写了同样的话。即：**已有页明确标注了这条父关系无原文依据**。
   建 `edf` 页会让这两条推断**看起来像有了落点**，可能掩盖「其实没有依据」这件事。
3. **in_src 口径要分清**（这是本项最容易搞错的地方）：
   slug 名对应的是候选 A（**in_src=3**，全库最低），
   但**同族**候选 B/C 的 in_src 是 **78 / 72**（本组七项里最高）。
   若误按「同族最高 in_src」取 raw，会**认领错篇**——
   那两篇**已经各有主页**（`edf-data-organization.md` / `edf-data-types.md`），
   再认领一次就是**重复建页**。
   **「多副本取 in_src 最高」的规则在这里不适用**：这不是同一篇的多个副本，是**三个不同的 topic**。
4. **两种处置，二选一，不要混：**
   - **改链接**：把 4 处 `[[edf]]` 改指 `[[edf-data-organization]]`（有 78 入度、有正文的那篇）。
     代价：丢掉「父概念」这个层级，且 `mapping-results.md:98` 那句
     「`[[edf]] / [[edl-file]]`」并列表达的「格式 / 落盘文件」对照会变弱。
   - **建索引页**：建一个**诚实标注「原文无定义、本页只做族目录」**的 concept 页。
     代价：多一个低信息量页面，且必须显式写明「依据只有标题」。
   **无论选哪种，都必须先处理第 2 条那两句已被写下的「（推断）」说明。**
5. `Event Formatter`（`02.10.02`）是**建立在本族之上**的工具，
   `wiki/stages/results.md:278` 已把它标为 `gui`。别把 EDF 与 Event Formatter 混为一谈。
