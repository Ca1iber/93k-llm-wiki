# 计划：修「表格被压平」（3,115 篇）

> **这份文档是给一个全新的会话看的。** 它自带全部背景 —— 不要假设读者知道之前发生过什么。
> 写于 2026-10-08。**还没有动手**：一个字都没改。

---

## 一、这是什么问题

上游是原厂 HTML 里的**真表格**（`<table><tr><th>/<td>`）。
转换到 markdown 时，表格的**行列结构被拍平了**。

**上游**（第 2 张表，4 行 × 3 列）：

```
| Current Mode | Desired Mode | Password required |
| operating    | supervising  | Supervisor        |
| operating    | engineering  | Engineer          |
| supervising  | engineering  | Engineer          |
```

**md 里实际长这样**（原样，`\r\n` 是真换行）：

```
Current Mode\r\n\r\n |\r\n\r\nDesired Mode\r\n\r\n |\r\n\r\nPassword required\r\n\r\n |\r\n |\r\n\r\noperating\r\n\r\n |\r\n\r\nsupervising\r\n\r\n |\r\n\r\nSupervisor\r\n\r\n |\r\n |\r\n\r\noperating\r\n\r\n |\r\n\r\nengineering\r\n\r\n |\r\n\r\nEngineer\r\n\r\n |\r\n |\r\n\r\nsupervising\r\n\r\n |\r\n\r\nengineering\r\n\r\n |\r\n\r\nEngineer\r\n\r\n
```

**也就是**：每格文字各占一行，格子之间夹一条「只有竖线的行」，行与行之间是**两条**。

**内容一个字没丢，丢的是「谁挨着谁」。** 宽表压平后就**再也看不出哪个默认值属于哪个参数**了 ——
而语言模型猜错的时候不会说「我猜的」。

**为什么要紧**：受影响的是**「读得对不对」**，不是「能不能搜到」（词都在，搜得到）。

---

## 二、三层在哪（**「raw」这个词有歧义，看路径**）

```
F:\master-dev\dorm-wsl-sytest\tdc-html\
    raw\*.htm                      ← 上游 HTML（9,321 个）。**表是好的，一个字节不用动**
    agent-markdown\by-category\    ← markdown 语料（9,398 篇）。★ 病在这里
    agent-markdown\by-category\<分类>\<子类>\*.md
F:\master-dev\understand-anything-wiki\
    wiki\                          ← wiki 页面。**被带进去的，不是源头**
    extract\                       ← 工具、清单、findings 都在这
```

> **别被「raw」绕进去**：`tdc-html\raw\` 里装的是 **HTML**；
> 而 wiki 的 `raw/README.md` 说的「raw 语料」指的是 **markdown**。**同一个词指两层。**
> 本工程内部一律说 **上游（HTML）/ 下游（markdown）**。

**wiki 为什么也有**：wiki 每页有一节 `## 语法 / 参数`，是**脚本从 markdown 逐字抄的**（§4 规定不许 LLM 改）。
所以 markdown 里压平，wiki 页面上就压平。**但 wiki 不用手改** —— 见第六步。

---

## 三、影响面（已量，可直接复算）

```bash
cd F:/master-dev/dorm-wsl-sytest/tdc-html
python -X utf8 - <<'PY'
import pathlib, re
C = pathlib.Path('agent-markdown/by-category')
docs = tot = 0
for p in C.rglob('*.md'):
    t = p.read_bytes().decode('utf-8', 'replace')
    k = sum(1 for l in t.splitlines() if re.fullmatch(r'\s*\|\s*', l))
    if k >= 2:
        docs += 1
        tot += k
print(f'{docs:,} 篇 / {tot:,} 行孤立竖线')
PY
```

实测：**3,115 篇**（占全库 9,398 篇的 **33%**），合计 **91,805 行**孤立竖线。

---

## 四、方法（**关键：这不是「编一张表」，是「解析 + 逐格验」**）

压平后的形状是**规则的**，所以能解析回来：

- **一条**竖线行 = 换列
- **两条**竖线行 = 换行

**流程（每篇）**：

1. 从 md 的 frontmatter 取 `source_topic` → 找到上游 `raw\<topic>.htm`
2. 从上游抽出所有 `<table>`，解析成网格（`<tr>` → 行，`<th>`/`<td>` → 格，去标签取文字）
3. 在 md 里找到对应的压平段，按「单竖线换列 / 双竖线换行」解析回网格
4. **逐格核对**：解析回来的网格 **必须和上游的网格一格不差**（行数、列数、每格文字）
   - **对不上就整张不动** —— 宁可少修，不修错
5. 对上了，才把那段**替换成一张正常的 markdown 表格**

**第一步的原型已经验证过方向是对的**（行、列解析全对，只是原型在竖线行计数上有个 off-by-one，
见「六、坑」）。**不要照抄那个原型，要重写。**

---

## 五、已经定下来的三件事

1. **改 markdown，上游 HTML 一个字节不动。**
   理由：HTML 是唯一能证明「原厂本来怎么写的」的东西，改了就再也证不了。
   本工程的规矩（`schema.md` §1.2，2026-09-23 用户改）是「**哪一层错就改哪一层**」——
   这一族是**转换坏的**，所以改下游。

2. **遇到合并单元格（colspan / rowspan）整张不动。**
   markdown 表格表达不了合并格。拆开还是跳过要有个说法，**倾向跳过**（少修不错修）。

3. **只有当「解析回来的网格 == 上游网格」时才改。**
   这条是整件事的**安全阀**：没有它，就是在**编一张表**，而编表比压平更坏。

---

## 六、★ 坑（这个工程踩过的，**直接继承，别再踩**）

### 6.1 换行：Windows 上 `read_text()` / `write_text()` **会动换行**

- `read_text()` **把 CRLF 转成 LF**（往外抽 CR）
- `write_text()` **把 LF 转成 CRLF**（往里加 CR）
- **语料是 CRLF 的**。用了这两个，会**静默改掉整篇的换行**。

**规矩**：一律 `p.read_bytes().decode('utf-8','replace')` / `p.write_bytes(t.encode('utf-8'))`。
**改完必须验**：`git diff --numstat` 的**新增行数 == 删除行数**（对称 = 每处只动一行，没有整篇重写）。

> **这个坑在本工程已经踩了两次**（09-28 的 `write_text`、10-08 的 `read_text`），两次都是整批文件的换行被改坏。

### 6.2 改完语料**必须重跑下游** —— 跳过会红三类

改了 `agent-markdown\` 之后，**按顺序**跑（少一步，闸门就红）：

```bash
cd F:/master-dev/understand-anything-wiki
python -X utf8 extract/extract.py              # ① 重算 docs/edges/sections（派生物，不入库）
python -X utf8 extract/versions.py             # ② 版本页（它读的是 ① 的产物，不重跑①它读旧缓存）
python -X utf8 extract/check_syntax_fresh.py   # ③ 看哪些页的语法节过期
python -X utf8 extract/objscaffold.py --refresh-syntax <上一步列出的 slug...>
python -X utf8 extract/fix_doc_stats.py --write # ④ 页面里「N 字节」的声明（语料变了，字节数就变）
python -X utf8 extract/verify_stages.py        # ⑤ 闸门：十五类应该全绿，EXIT=0
```

> **这个坑也踩过**：10-08 修完乱码没重跑下游，闸门一次红了**三类**（第十二/十三/十四类），
> 分别对应「页面里的逐字引用」「版本页」「页面里声明的字节数」。

### 6.3 写文件用 Write 工具，**别用 shell heredoc**

在 bash 里用 `python -X utf8 -c "..."` 写含**反引号**的内容时，**反引号会被 shell 当命令执行**，
文本被咬出窟窿。**这个坑本工程踩了至少五次。**
需要写含反引号的文件 → **用 Write 工具**，或先写临时文件再 splice。

### 6.4 工具该有的样子（本工程既有惯例）

- **`guard(path, n, what)` 互锁**：本次结果为 0 条而目标已有内容时 → **拒绝写**（防「空表覆盖好清单」）
- **空跑 / `--apply` 分开**：默认只报数、只出证据表
- **产物三件套**：证据表（逐处对照）、机器可读清单（供重放）、脚本本身 —— **全部入库**
  （`.gitignore` 只排 `docs.jsonl` / `edges.jsonl` / `sections.jsonl` 三个大派生物）
- **不许静默跳过**：任何「跳过」都要计数并打印出来

### 6.5 有界优先

上一版用 `difflib` 做全篇对齐，**思路对但跑不完**（几万字符上是平方级，
某类文档慢 50 倍，而且只在全部跑完才打印 —— 没有进度、没有上限）。
**一条判据再对，跑不完就等于没有。** 这次是**局部解析**，本身就有界，保持这样。

---

## 七、步骤

| # | 做什么 | 判据 / 产出 |
|---|---|---|
| 1 | 写 `extract/fix_corpus_tables.py` | 空跑 / `--apply` 分开 + `guard()` |
| 2 | 抽 **10–15 篇**跑通，**逐格对照上游** | 人工看：解析回来的网格 == 上游网格 |
| 3 | 摸边界情况并定规则 | 格子里有图 / 有链接 / 有换行 / 合并格 → 各自怎么办 |
| 4 | 全量空跑 | 报「能修 N 篇 / 跳过 M 篇（哪一类）」 |
| 5 | `--apply` | 只改判据过的那些 |
| 6 | **下游重算**（见 6.2，五步一步不跳） | 闸门十五类全绿，EXIT=0 |
| 7 | 提交两个仓 + 记账 | 语料仓 + `wiki/log.md` + 更新 `raw/README.md` 台账 |

**验收**：`git diff --numstat` 对称；闸门全绿；抽查几篇渲染出来的表能读。

---

## 八、相关的既有材料（新会话可以读，但不必全读）

| 文件 | 是什么 |
|---|---|
| `extract/PLAN-未修清单.md` | **所有**未修项的账（本计划是它的 A2 附近新增的一条） |
| `extract/fix_corpus_mojibake.py` | 上一批修复器（**照它的骨架写**：guard / 空跑 / 证据表 / 清单） |
| `extract/fix_corpus_mojibake2.py` | 再上一批（词锚定位那版） |
| `wiki/schema.md` §1.2 | 「哪一层错就改哪一层」+ 五步流程 + 三条禁令 |
| `wiki/log.md` 末尾 | 前几批的完整账 |
| `extract/findings-*.md` | 各类缺陷的档案 |

---

## 九、别做的事

- **别动上游 `raw\*.htm`**（它是证据）
- **别手改 wiki 页面的 `## 语法 / 参数` 一节**（脚本管的，`--refresh-syntax` 会冲掉）
- **别在没有逐格校验的情况下改表** —— 那就是编表
- **别一次改一半就停** —— 留下「每张表长得都不一样」比整齐地压平更坏
