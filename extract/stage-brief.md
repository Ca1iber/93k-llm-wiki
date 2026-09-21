# 建 stage 页 · 共用简报

你负责**一个** stage 页。这份简报是九个页共用的规矩，逐条照做。

## 1. 背景（一句话）

`F:\master-dev\understand-anything-wiki\` 是一个 llm_wiki，三层：`raw/`（9,398 篇
SmarTest 7.10.3 文档，**只读**）、`wiki/`（要生成的产物）、`schema.md`（维护者说明书）。

**stage 页是 wiki 的脊椎**：它回答「这一步该干什么、前置是什么、下一步是什么」。
raw 语料**按产品功能**组织（命令参考、API 参考、文件格式），**没有任何一篇讲完整流程**——
这一层是语料里不存在、必须由你合成的。所以你是**唯一允许写"流程"的地方**。

## 2. 语料在哪

```
F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category\<分类目录>\<分类号>_<名字>.md
```

**铁律：raw 里的任何文件都不许改。你只读，只写自己那一个输出文件。**

## 3. 工具（用这些，不要自己 grep 整个语料）

```bash
cd F:/master-dev/understand-anything-wiki/extract
python show.py 02.06.05 01.07.01.03        # 按分类号打原文
python show.py --head 02.06.05             # 只打前 800 字符
python show.py --grep 关键词                # 按标题/文件名找分类号
```

- `docs.jsonl` — 9,398 篇的机械索引（`rel` / `title` / `headings` / `first_para` /
  `struct_sections` / `bytes`）。**先在这里定位，再读原文。**
- `edges.jsonl` — 53,102 条交叉引用边，带**语境句子**和行号。想找「谁引用了 X」用它。
- `hubs.csv` — 按 `in_src`（被多少篇不同文档引用）排的枢纽榜。
- `sections.jsonl` — 抽出的 `Procedure` / `Before you begin` / `Dependency` / `Errors`
  等结构段落正文。

## 4. 硬规矩（违反即作废）

1. **不许凭印象写。** 你写的每一条 L1/L2/L3 条目、每个产物、每条验证方法，
   都必须来自你**真的读过**的文档，并写进 frontmatter 的 `sources:`。
2. **区分三种东西**，页内措辞必须体现：
   - **文档事实** — 文档里明写着。直述。
   - **推断** — 你从多处推出的。必须写「推断：」。
   - **建议** — 你的意见。必须写「建议：」。
   不许把推断或建议写成文档事实。这是这个项目最容易犯的错。
3. **没有材料就写「文档未覆盖」**，四个字，单独一行。**不许编，不许凑。**
   十个小节一个都不许省——这是 schema 的硬规定，空着也是信息。
4. **不许据 TDC 文档推断某个实际 93K 机台已实现的能力。** 全部页面的
   `verified` 一律 `doc-only`。
5. 中文正文，但**文件名必须 ASCII**。

## 5. 输出模板（照抄小节名，不许改、不许省）

```markdown
---
type: stage
title: <人类可读标题>
tags: []
related: []
sources: []              # raw 相对路径，至少一条。你实际读过哪些就写哪些
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# <stage 中文名>

> <一句话：这一步在整条流程里解决什么问题>

## 目的
## 前置条件
## 涉及对象
## L1 — Firmware / Setup Command
## L2 — Test Method API
## L3 — 外部控制
## 产物
## 验证
## 常见错误
## 下一步
```

写进 `wiki/stages/<stage>.md`（`<stage>` = `project` / `pin` / `level` / `timing` /
`pattern` / `testmethod` / `testflow` / `run` / `results`）。

## 6. 各小节怎么写

- **目的** — 这段流程解决什么问题。从走查/概念页的 `About this task` 抄实义。
- **前置条件** — 做这一步之前必须完成什么。优先找 **`Before you begin` /
  `Dependency` / `Predependencies`** 段落（`sections.jsonl` 里有）。
  逐条注明出处。引用别的 stage 用 `[[pipeline]]` 形式的 wikilink。
- **涉及对象** — 本阶段用到的命令 / API / 文件 / 工具。**每条写三样**：
  `[[对象页名]]` + 层级（L1/L2/L3/file/gui） + 一句它在本阶段干什么。
  对象页多数**还没建**，这没关系——wikilink 就是待建清单。
- **L1 / L2 / L3** — 三层的具体条目。
  - L1 = firmware / setup 命令（如 `DFPN`、`PSFC`）。**给最小可用示例**（从文档里抄，别自己编）。
  - L2 = C++ Test Method API（`02.07_Test_Method_Reference` 那一大章）。
  - L3 = 外部控制：SmartShell / Test suite control API / HVM。语料里这块很薄，
    **薄就写「文档未覆盖」，不许拿 L1 的东西冒充 L3。**

    > **已知陷阱：SmartShell 在本版本不存在。** 全库唯一一篇 SmartShell 总述
    > `02_System_reference/02.15_SmartShell/02.15_SmartShell.md` 的 Functional changes
    > 明写 **`Introduced in SmarTest 8.2.5`**，而本 wiki 面向 **7.10.3**。
    > 那一章总共只有 1 篇，正文全是 PDF 外链。**不许拿它当可用的 L3 接口填小节**，
    > 要么写「文档未覆盖」，要么在 L3 里显式记录「此接口在 7.10.3 不存在」。
    > （`schema.md` §2.1 把 SmartShell 列为 L3 的三样之一，这一条 schema 自身写错了，
    > 已另记。）
- **产物** — 这一步产出哪些文件、放在哪个目录、什么格式。device directory 结构见
  `01.07.01.01.01_Device_directory_structure`。
- **验证** — 怎么确认这一步做对了。优先找文档里的 `Results` / `What to do next` /
  `Verifying ...` 段，以及 GUI 上该看到什么、校验/查询命令。**不许自己发明验证方法。**
- **常见错误** — 典型症状 + 排查入口。语料有专门的错误章（如 `02.06.03_Errors`）
  和 `Errors` 段（`sections.jsonl`）。没有就写「文档未覆盖」。
- **下一步** — 链到下一个 stage：`[[next-stage]]`，一句说明为什么是它。

## 7. 回报（你返回给我的正文，**不超过 25 行**）

```
## <stage>
写入了 wiki/stages/<stage>.md
读了 N 篇，sources 列了 M 条
未覆盖的小节：<列出，没有就写"无">
存疑/需要我定的：<最多 3 条，没有就写"无">
```

**不要把页面正文贴回来。** 页面在盘上，我会自己读。
