# raw/ — 证据层

**这里没有文件，这是故意的。**

raw 语料有 9,398 篇 / 26.8 MB，复制一份进 wiki 目录是浪费。

## 位置

```
F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category
```

## 结构

```
by-category/
  00_Overview                       2 篇
  01_Getting_started              256 篇
  02_System_reference           8,317 篇   ← 88%
  03_Use_cases_and_papers         574 篇
  99_Unlisted                     249 篇
```

层级编码在**文件名前缀**里，不在目录里。例：

```
02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md
                    └─ 子类 ──────┘ └─ 四级前缀 ─┘
```

全库约 110 个四级簇。`catalog-markdown.csv`（9,394 行）是现成的全量目录。

## 铁律

- **只读。** 任何情况下不许修改这里的文件。
  - **唯一例外：A 类「转换损坏」**——上游 `tdc-html/raw/` 的 HTML 明写着原意，
    转换时被拍平 / 粘连 / 丢标签。判据（三条）、流程（五步）、代价见 `schema.md` **§1.2**。
  - **每次都要先向人摆证据、经人批准，且只改被批准的那几处。**
  - **B 类（文档内容本身有误）一个字都不许动**——只能在 wiki 层标注。
    **区别在于**：A 类改完 raw 说的还是原厂那句话；B 类改完就成了你的话，且再也分不出来。
- 引用时用**相对路径**（相对 `by-category/`），写进 wiki 页面的 `sources:` 字段。
- wiki 里每一句断言都要能追回这里的某个文件。追不回去的，就是编的。
- **改过的每一处都要有 log 记录。**
  - **第一批（已改完，2026-09-22）**：**151 处 / 60 篇**——数字上标被拍平（`2^48`→`248`）。
    证据表 `extract/findings-corpus-superscript-loss-evidence.md`（151 行逐处对照）、
    清单 `extract/_assign.json`、脚本 `extract/fix_corpus_superscript.py`、
    完整账 `extract/findings-corpus-superscript-loss.md`、log 见 `wiki/log.md`。
    **`tdc-html/raw/` 的 HTML 一个字没动。**
  - **验法**：拿 `git show HEAD:` + 记录的偏移**重放**，60/60 篇逐字节一致；
    CRLF 计数改前改后相同；带上下文锚复检 **151 → 0**。
  - **这两个产物必须进版本库——2026-09-23 已进。** 2026-09-22 它们被**清空过一次**——
    `fix_corpus_superscript.py` 的写盘在 `--apply` 判断**之前**，改完语料再空跑，
    151 处全报「未定位」，**一份空表盖掉了好清单**；两份都是未追踪文件，**git 救不回**。
    靠「HTML 没动」重算才补回（并与残留清单逐条对上）。
    现已加互锁 **`guard()`：空结果不许覆盖非空清单**。
    **教训**：同一次事故里，被追踪的 `findings-corpus-superscript-loss.md` 毫发无损，
    **没进版本库的两份没了**——「数据要能重算」**不能拿来代替留版本**，
    重算得出来的前提，恰恰是别的东西没被动过。

## 已知的语料特征

| 特征 | 数量 | 说明 |
|---|---|---|
| 含交叉引用 | 7,076 篇（75%） | 全库约 50,073 条链接 |
| 带代码块 | 4,006 篇 | 语法/示例 |
| 带 `Functional changes` | 6,107 篇 | 版本引入信息 |
| 带 `Procedure` | 491 篇 | 程序性文档 |
| 带 `Before you begin` | 459 篇 | 前置条件 |
| 带 `Dependency`/`Predependencies` | 103 篇 | 显式依赖 |
| 带 `Errors` | 425 篇 | 报错 |

原始链接语法是 `](<相对路径.md>)`——**注意尖括号**，解析时别漏。

例（`DFPN` 页第 10 行）：

```
Note that before you can use the DFPN command the sequencer state must be OFF
(see the [SQST](<02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.md>) command).
```
