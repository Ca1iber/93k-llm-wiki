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
  - **例外一：转换损坏**——上游 `tdc-html/raw/` 的 HTML 明写着原意，
    转换时被拍平 / 粘连 / 丢标签 / 丢内容。判据（三条）、流程（五步）、代价见 `schema.md` **§1.2**。
  - **例外二（2026-09-23 加）：哪一层错就改哪一层**（用户定）。
    **上游 HTML 自己写错时改 HTML**（`<sup>` 把标点或运算符包了进去），
    不再一律只改下游。**但先要判清是哪一层的错**，且**改上游前确认它已入库**——
    重放读的是 `git show HEAD:`。
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
  - **第三批（已改完，2026-09-23）**：**G 类——符号 / 公式上标**，**raw 6 处 + md 18 处**。
    **这一批第一次动了 `tdc-html/raw/`**——因为规矩改了（用户定）：
    「**raw 有问题你就改 raw，markdown 有问题你就改 md**」。
    raw 侧的判据不是「我觉得」，是**同一文件里别处的写法**
    （`98749.htm` 有 12 处写 `2<sup>31</sup>-1`，那 2 处却写 `2<sup>32-1</sup>`）。
    证据表 `extract/findings-corpus-superscript-loss-evidence-symbol.md`、
    清单 `extract/_assign_symbol.json`、脚本 `extract/fix_corpus_superscript_symbol.py`。
  - **第二批（已改完，2026-09-23）**：**D 类 3 处 / 3 篇**——带符号指数被拍平
    （`10<sup>-9</sup>` → `10-9`，与 A 类同一机制，A 类脚本的正则漏了带符号的）。
    证据表 `extract/findings-corpus-superscript-loss-evidence-signed.md`、
    清单 `extract/_assign_signed.json`、脚本 `extract/fix_corpus_superscript_signed.py`。
  - **第四批（2026-09-28，已改完）**：**坏字（GBK 误读）第一批 —— 120 族，5,638 处 / 759 篇**。
    **只改 `agent-markdown/`，`raw/` 一个字节没动**——这一族的上游 `.htm` 是干净的
    （实测 605 篇里 602 篇干净、上游也坏的 0 篇），坏的是转换出来的 md（§1.2：哪一层错就改哪一层）。
    判据：坏字 `encode('gbk')` 拿回原字节、再 `decode('utf-8')` = 原字，**且反向也成立**
    （`µ` → UTF-8 `C2 B5` → GBK 读成 `碌`）。**不用猜**。
    工具 `extract/fix_corpus_mojibake.py`、证据表 `extract/findings-corpus-mojibake-evidence.md`、
    清单 `extract/_assign_mojibake.json`、映射表 `extract/encoding-map.csv`。
    **验**：改完剩 0 处；759 篇新增/删除行数对称（3,638 / 3,638），没有整篇重写、换行未动。
    **第二批（8 族 / 2,268 处）没修**——那些是「第三字节已丢」，只能给区间、**不许猜**；
    试的锚点判据成功率只有 **40%**，不达标。见 `PLAN-未修清单.md` 的 A1。
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
  - **第五批（2026-10-08，已改完）**：**表格被压平 —— 3,642 张表 / 2,399 篇**。
    上游 HTML 是真表格，转 markdown 时**行列结构被拍平**（每格一行、格间夹 ` |` 行、
    行间夹两条）；内容一个字没丢，丢的是「谁挨着谁」。**只改 `agent-markdown/`，
    `raw/` 一个字节没动。**
    判据：压平文本其实就是一张 markdown 表，` |` 分隔符被格内块级换行冲散 ——
    一张 R 行 C 列的表 ` |` token 恰好 **R×(C+1)** 个。按这个切回网格后
    **逐格与上游 `.htm` 核对**（空格/换行/列表标记/反引号/链接图片标记等排版差异已规范化；
    上标标记 `^` 两边都剥，因为那是第一批的账）。**对不上就整张不动。**
    工具 `extract/fix_corpus_tables.py`、证据表 `extract/findings-corpus-tables-evidence.md`
    （3,642 行逐处对照）、清单 `extract/_assign_tables.json`（含 `orig`/`new`/偏移，**供重放**）。
    **验**：`git show HEAD:`（commit `8aa1a8f` 的父）+ 清单偏移**逐字节重放，
    2,399/2,399 篇一字不差**。行数大减是**设计如此**（每格一行 → 每行一格），
    所以 `--numstat` 对称那条**不适用**——重放才是判据（§1.2 第 4 条）。
    **没改的**：上游带 colspan/rowspan 的表 970 张（markdown 表格表达不了合并格）、
    另一来源的 Doxygen 表格 9 篇、格内有代码围栏 30 张、内容近于空 20 张、
    **同一张表在文档里对上 ≥2 处（分不清是重复投放还是撞上）88 张** —— 一律整张不动。
    残留 **1,072 篇 / 39,872 行**孤立竖线（原 3,115 篇 / 91,805 行）。
    **两处注明的改写**（markdown 语法逼出来的，不是改内容）：① 第一行一律成为表头
    （GFM 要求表头分隔行）；② 格内换行写成 `<br>` / `<br><br>`（沿用本工程表格单元格
    的既有写法）。**后者波及 wiki 引文**：`dprt.md` / `tpt-generate-device-dir.md`
    两页原来把单元格内多行合写成一串相邻的 `>` 引文块，第七类按 §11.1 判为「丢字符」，
    **已把两页的引文块分开**（不是改判据）。
  - **顺带修掉 `extract/fix_doc_stats.py` 一个先天 bug**：它把行数写成 `1007 行`
    （无千位逗号），而页面写 `1,007 行` —— **替换成空操作**，`plan()` 报「要改 1 处」、
    页面一个字没动、`check_doc_stats` 那边红着。以前蛰伏，是因为那些数字本来就是对的不需要改。
  - **本次另记一笔，未处置**：语料仓**只跟踪 `agent-markdown/`**（9,401 文件），
    **`raw/`（9,321 个 `.htm` 加图，576 MB）从未入库**。`schema.md` §1.2 的「重放」退路
    靠 `git show HEAD:`，而这一层没有版本历史 —— 它现在只靠文件系统本身不变。
    又：本仓 **`core.autocrlf=true`**（git 存 LF、工作区 CRLF），
    **任何「逐字节重放」都必须先对齐换行**，否则 100% 误报（本次第一跑就是这样）。
  - **第六批（2026-10-08，已改完）**：**带合并格的表被压平 —— 362 张 / 339 篇**。
    第五批遇到上游带 `colspan`/`rowspan` 的表整张跳过（markdown 表格表达不了合并格），
    这批专门处理它们。**判据不变、更强的那一半原封不动**：md 里**每一行的格子数与上游
    HTML 逐行一一对应**（合并格那几行本来就少一格），所以「逐格核对」照旧，对不上整张不动。
    变的只有两处：① 不再要求「每行列数相同」，改按**每行各自的格子数**切
    （`P = Σ(每行格子数) + 行数`）；② 生成时把**展开**写出来 ——
    上游一格跨 N 行/列 → 写成 N 个**相同**的格子。
    工具 `extract/fix_corpus_tables_merged.py`、证据表
    `extract/findings-corpus-tables-merged-evidence.md`（362 行逐处对照）、
    清单 `extract/_assign_tables_merged.json`（含偏移，供重放）。
    **验**：`git show HEAD:` + 清单偏移**逐字节重放，339/339 篇一字不差**。
    **重复格占比平均 23%、上限卡 45%**（超上限的 23 张挂账，不让噪声失控）。
    **跳过**：窗口放不下 147、格子对不上 68、重复>45% 23、格内有围栏 1。
    残留 **750 篇 / 27,836 行**（两批合计：篇 −76%、行 −70%）。
    **★ 本项目第一次让修复器往语料里写自己的话**：每张展开过的表下面加一句
    **固定措辞**的转录说明（只描述做过什么 + 指出真结构在哪，
    **不宣称一条能反推结构的规矩** —— 「相邻相同 = 合并格」实测会**误判 16%**：
    已修的 3,642 张**不含**合并格的表里，594 张本来就有相邻相同的格子）。
    措辞经人确认。**嵌套表（`<td>` 里套 `<table>`）没碰**，理由见
    `extract/PLAN-未修清单.md` 的 **A6**。

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
