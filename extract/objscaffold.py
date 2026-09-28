# -*- coding: utf-8 -*-
"""建页骨架 —— 把 `schema.md` §4 的分工落成代码。

§4 的分工是两句话：

- 「对象页的语法 / 参数表骨架 **由脚本从 raw 的 `## Syntax` / `## Parameters` 抽**」（成本 0）
- 「对象页的『和谁有关』部分 **LLM**」（钱花在这里）

所以一页是**两个人写的**：脚本写死的部分（语法表）和我写的部分（转述、关联、判断）。
第一版我打算整页手写，那会立刻撞上两个问题：

1. **手抄参数表 = 重写 = 把「文档事实」降级成「我的转述」**（§11 明令要分开）。
2. 实测 `Sharing configuration file` 的 `## Syntax` 有 **8,268 字符 / 99 行表格**，
   手抄一遍既慢又会抄错，**而抄错一个关键字名，读者照着写就是编译错误**。

本脚本产出的页面里：

- frontmatter：`type` / `layer` / `stage` 来自 `wiki-plan.csv`（人工定，一页一行）
- `## 语法 / 参数`：**逐字**取自定义文档，附出处与字符数
- 其余各节：留 `（待补）`，由 LLM 用 Edit 填

**逐字段里的链接要改写**：raw 里的链接是**语料内部相对路径**（`02.12...md`），
照搬进 wiki 就是一批指不到任何地方的路径。脚本机械地把
`[T](<P>)` 改写成 ``T``（raw: `P`）——**文本和路径都留着，只是不再是链接**。

用：`python objscaffold.py`（读 `extract/wiki-plan.csv`，写 `wiki/<dir>/<slug>.md`）
    `python objscaffold.py --force` 覆盖已存在的页（默认**拒绝覆盖**）
"""
import csv
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import objpack as op

BASE = Path(r'F:\master-dev\understand-anything-wiki')
OUT = BASE / 'extract'
WIKI = BASE / 'wiki'
PLAN = OUT / 'wiki-plan.csv'

# 类型 → 目录（`schema.md` §2）。**`object` 之外的类型不许写进 `objects/`**——
# 类型和目录对不上，§2 那七类就白分了。
DIRS = {'object': 'objects', 'concept': 'concepts', 'constraint': 'constraints',
        'mapping': 'mappings', 'error': 'errors', 'version': 'versions',
        # **`stage` 是补上的**（2026-09-18）：§2 一共七类，这里原先只有六类。
        # 它一直没露出来，是因为**九页 stage 从来没进过 `wiki-plan.csv`**——
        # `plan_sync.py` 把它们回填进去之后，`check_syntax_fresh.py` 立刻
        # 在 `DIRS[r['type']]` 上 `KeyError: 'stage'`。
        # **枚举式的表，漏一项不会报错，只会在第一个新输入进来时炸。**
        'stage': 'stages'}

LINK = re.compile(r'\[([^\]]*)\]\(\s*<?([^)>\s]+)>?\s*\)')

PLACEHOLDER = '（待补）'


def unlink(m):
    """`[T](<P>)` → ``T``（raw: `P`）。

    **两个都留**：文本是给人读的，路径是给人和 agent 回 raw 查的。
    第一版想「同目录的就只留文本」——**那是在猜**：raw 里 `P` 不带目录时表示
    同目录兄弟（`02.12...04_Identifying_sites.md`），不是页内锚点。
    猜错就把路径丢了，而路径是这一节唯一能回查原文的东西。
    """
    t, p = m.group(1), m.group(2)
    return f'`{t.strip() or p}`（raw: `{p}`）'


HEAD = '## 语法 / 参数'

# **语法节的边界靠显式标记，不靠猜。**
#
# 这一天里边界判据换了三次，每次都换出一种新的删法，**记在这里**：
#
# 1. 「下一个 `## `」→ `device-architecture-file` 的语法节里**嵌着十几个 H2**
#    （`_file_syntax` 整篇照收），于是边界落在表格中间，
#    `refresh()` 会把 21,814 字符的表**抄两遍**（没炸只是还没人刷过它）。
# 2. 换成「下一个**页面级**小节」（`PAGE_HEADS`）→ 修好了上一条，
#    但 `cct-multiport-sequencer-synchronizer-api` 的
#    `## 能力` / `## 支持` / `## 同步是怎么做的` / `## 前置条件` / `## 限制` / `## 族`
#    **都不是那五个标准名**，于是**被当成语法节的一部分整段删掉**（实测删掉 6 节）。
#    **这不是猜错，是「我没见过这种页面」。**
# 3. 于是改成显式标记 + **互锁**（见 `refresh()`）：没有标记、
#    又发现要替换的区间里有新块里没有的 `## ` 标题 → **拒绝执行并报错**。
#
# **教训**：脚本对「页面长什么样」的假设，写成判据就会变成删数据的刀。
# 边界这种东西**必须由写它的人留下记号**，不能由读者推断。
MARK_BEGIN = ('<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，'
              '**手改会在下次 `--refresh-syntax` 时消失** -->')
MARK_END = '<!-- 语法节 end -->'

# ── 报错节（2026-09-20 加）──────────────────────────────────────────────
# **为什么加**：语料里 **402 篇**带 `## Errors` 段，写的是「这条命令什么时候会失败」
# （多是 `An error is generated if:` + 一串条件）。那是**命令自身的属性**，属 §2.2 的
# 对象页（不是 §2.4 的约束页、也不是 §2.6 的排错页——**排错页要的是"症状"，
# 而这类段落是"条件"，实测全语料只有 5 个独立来源够格建排错页**）。
# 它**机械可抽**，所以按 §4 **由脚本逐字取，不调 LLM**。
# **没有材料的页不写空节**——空节会读成「这条命令不会失败」。
ERR_HEAD = '## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）'
ERR_BEGIN = ('<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，'
             '**手改会在下次 `--refresh-errors` 时消失** -->')
ERR_END = '<!-- 报错节 end -->'
ERR_MARKS = ('Errors', 'Warnings', 'Limits')
ERR_MIN = 60        # 比这短的段不算材料（实测 <60 字符的多是空壳）


def error_block(rel):
    """`## 报错条件` 这一节的完整文本（含结尾空行）。**没有材料时返回 `''`。**

    与 `syntax_block()` 同规矩：逐字取、内部相对链接改写成 `文本`（raw: `路径`）、
    带自己的 begin/end 标记（好让 `refresh_errors()` 只动这一节）。
    """
    secs = [s for s in op.sections_of(rel)
            if (s.get('h2') or '').strip() in ERR_MARKS
            and s.get('chars', 0) >= ERR_MIN and not s.get('truncated')]
    if not secs:
        return ''
    w = [ERR_HEAD, '', ERR_BEGIN, '',
         f'> 本节**逐字取自** `<{rel}>` 的 {"、".join("`## " + (s.get("h2") or "") + "`" for s in secs)} 段。',
         '> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；',
         '> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。', '']
    for s in secs:
        w += [f'### {s.get("h2")}', '', LINK.sub(unlink, s.get('body') or '').strip(), '']
    w += [ERR_END, '']
    return '\n'.join(w)


def refresh_errors(row):
    """**只动报错节**：有标记就重刷；没标记而有材料就插在语法节之后；都没就跳过。

    插的位置**只认 `MARK_END`**——找不到就**拒绝执行**（不猜位置，同 `refresh()` 的互锁）。
    """
    p = WIKI / DIRS[row['type']] / f"{row['slug']}.md"
    text = p.read_text(encoding='utf-8')
    block = error_block(rels_of(row)[0])
    if ERR_BEGIN in text:
        # **从标题 `ERR_HEAD` 开始替，不是从 `ERR_BEGIN` 开始**（2026-09-20 修）：
        # `block` 里含标题，只替标记之后的部分会把标题**写成两遍**。
        i = text.find(ERR_HEAD)
        if i < 0:
            raise SystemExit(f'❌ {p.name}：有报错节标记却没有标题 `{ERR_HEAD}`——先看页面')
        j = text.index(ERR_END, i) + len(ERR_END)
        e = text.find('\n', j); j = len(text) if e < 0 else e + 1
        if not block:
            raise SystemExit(f'❌ {p.name}：页里有报错节，但 raw 里已取不到材料——先看页面')
        p.write_text(text[:i] + block.rstrip('\n') + '\n' + text[j:], encoding='utf-8')
        return 'refreshed'
    if not block:
        return 'skip'
    k = text.find(MARK_END)
    if k < 0:
        raise SystemExit(f'❌ {p.name}：找不到 `{MARK_END}`，无法定位插入点——不猜位置')
    e = text.find('\n', k) + 1
    p.write_text(text[:e] + '\n' + block + text[e:], encoding='utf-8')
    return 'inserted'

# 页面级小节名（`build()` 写的那五个）。**只在没有标记时当兜底判据用**，
# 且用完要过互锁——见 `refresh()`。
PAGE_HEADS = ('是什么', '典型用法', '和谁有关', '版本', '出处')


def section_end(text, i):
    """语法节（从 `i` 起）的结束位置。

    **优先认 `MARK_END`**；没有标记才退回「下一个页面级小节」，
    退回时调用方（`refresh`）必须再过一次互锁。
    """
    k = text.find(MARK_END, i)
    if k >= 0:
        e = text.find('\n', k)
        return len(text) if e < 0 else e + 1
    best = -1
    for h in PAGE_HEADS:
        k = text.find(f'\n## {h}', i + 1)
        if k >= 0 and (best < 0 or k < best):
            best = k
    return best if best >= 0 else len(text)


def syntax_block(rel):
    """`## 语法 / 参数` 这一节的完整文本（含结尾空行）。

    单独抽成函数，是为了能**只重刷这一节**——见 `refresh()`。
    """
    parts, srcs = op.collect_syntax(rel)
    w = [HEAD, '', MARK_BEGIN, '']
    if not parts:
        w += ['**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`',
              '这类**段标记**，跟着 `Subtopics` 找一层也没有。',
              '**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。', '']
        # **但「没有标记」不等于「没有参数」。** 这两句话混起来就会把读者引错方向：
        # `XPS256 … DPS operating mode` 全篇没有 `## Syntax`，而它整页的实质
        # 就是一张参数清单。第一版这里只写「无」，读起来像「这张卡没什么可配的」。
        # **检查比自称的范围窄**那一课在这里的形态是：**结论比证据强**。
        # 所以补一层「只报告、不收录」的探测，把缺口指出来，让读者回 raw 看原样。
        hints = op.ident_lists((op.CORPUS / rel).read_text(encoding='utf-8', errors='replace'))
        if hints:
            w += [f'> ⚠️ **本文档里有 {len(hints)} 处「未加标记的参数清单」**'
                  '（形状像参数名的一串列表项）。**脚本不收录它们**，但也不许假装它们不存在：', '']
            w += ['> | 上文 | 条数 | 例 |', '> |---|---|---|']
            for h, n, ex in hints:
                w += [f'> | {h or "（无标题）"} | {n} | ' +
                      '、'.join(f'`{e}`' for e in ex) + ' |']
            w += ['', '> **要看这些参数的正规定义，回 raw 读本文档**；'
                  '要参数的含义与取值，查它们链接到的资源页。', '']
        w += [MARK_END, '']
        return '\n'.join(w)

    tot = sum(len(b) for _, b in parts)
    subs = sorted({s for s in srcs if s != rel})
    src_txt = f'`<{rel}>`' + (f' 及其子主题 ' + '、'.join(f'`<{s}>`' for s in subs) if subs else '')
    w += [f'> 本节 **{tot:,} 字符逐字取自** {src_txt}。**不是转述。**',
          '> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是',
          '> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——',
          '> 改写参数表就是把文档事实降级成我的转述（§11）。']
    if subs:
        w += ['> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——',
              '> **来源写在段名里**，别把它当成定义文档自己写的。']
    w += ['> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。', '']
    for name, b in parts:
        w += [f'### {name}', '', LINK.sub(unlink, b), '']
    w += [MARK_END, '']
    return '\n'.join(w)


def refresh(row):
    """**只重刷 `## 语法 / 参数` 一节**，其余一字不动。

    **为什么必须有这个口子**：这一节是脚本的（§4），其余是 LLM 的。
    脚本改了抽取逻辑之后，已经补完散文的页面就卡住了——
    `build()` 默认拒绝覆盖（防手滑），`--force` 会把 LLM 写的散文一起抹掉。
    **两个都不能用**，于是只能手抄一遍新表格——**那就又回到「手抄参数表」，
    正是 §4 要消灭的东西。** 所以补这个只动一节的入口。

    找不到 `## 语法 / 参数` 时**直接报错退出**，不猜位置。

    **没有 `MARK_END` 时过一道互锁**：要替换的区间里如果出现了**新块里没有的
    `## ` 标题**，说明那个标题是页面自己的小节、被我当成了语法节的一部分——
    **拒绝执行**。这条互锁是为 `cct-multiport-sequencer-synchronizer-api`
    那次误删加的：那一页有六个自定义小节夹在语法节和 `## 版本` 之间，
    兜底判据一路跨过去，六节全没了（已从会话记录里恢复）。
    **宁可拒绝，不许猜。**
    """
    p = WIKI / DIRS[row['type']] / f"{row['slug']}.md"
    text = p.read_text(encoding='utf-8')
    i = text.find(HEAD)
    if i < 0:
        raise SystemExit(f'❌ {p.name} 里找不到 `{HEAD}`——不猜位置，先看页面')
    j = section_end(text, i)
    if j >= len(text):
        raise SystemExit(f'❌ {p.name} 的 `{HEAD}` 后面没有页面级小节——结构不对，先看页面')
    block = syntax_block(rels_of(row)[0])
    if MARK_END not in text[i:j]:
        inside = set(re.findall(r'^## .+$', block, re.M))
        strangers = [h for h in re.findall(r'^## .+$', text[i:j], re.M) if h not in inside]
        if strangers:
            raise SystemExit(
                f'❌ {p.name}：语法节里没有 `{MARK_END}` 标记，兜底边界会**吞掉**这些'
                f'非标准小节：{"、".join(strangers)}\n'
                f'   ——拒绝执行。先在这些小节之前补一行 `{MARK_END}`，再重跑。')
    new = text[:i] + block + text[j:]
    if new == text:
        print(f'＝ 无变化：{p.name}')
        return
    # **写之前先存一份快照。** 这一条是拿 `cct-…` 那六个小节换来的：
    # 那次删掉之后能捞回来，**靠的是会话记录里恰好留着全文**——
    # 换个会话、或者被删的是别的页，就没有第二份了。
    # 兜底不能指望运气，所以**由写页面的脚本自己存**，不靠人想起来。
    import snapshot as _snap                     # 同目录，见 extract/snapshot.py
    box = _snap.save(quiet=True)
    # ★ **符号必须是「改后 − 改前」**，`{:+}` 打出来才和左边那个箭头同向。
    #
    # 原来写的是 `len(text) - len(new)`（改前 − 改后），于是**页面变长时它是负数**，
    # 印出来是「`115,885 → 138,305` 字符，`-22,420`」——**箭头说长了 22,420，
    # 数字说少了 22,420**，同一行里自己打自己的脸。
    # 2026-09-24 建页时发现的，当时按 §1.2「不许顺手改旁边」只记进 log，没动；
    # 2026-09-28 单独改。
    delta = len(new) - len(text)
    p.write_text(new, encoding='utf-8')
    print(f'🔄 {p.name}  语法节重刷（整页 {len(text):,} → {len(new):,} 字符，{delta:+,}）')
    print(f'   ↳ 改前已存快照 `{box}`（要撤：`python extract/snapshot.py --restore {box}`）'
          if box else '   ↳ 与最近一份快照逐字节相同，未另存')


def rels_of(row):
    """`rel` 列可以是**分号分隔的多篇**：`主文档;补充1;补充2`。

    **为什么加这个**：一个对象常常由**好几篇文档共同定义**，不是一篇。
    例子：DPS128/DPS64 那张卡由 5 篇定义（总览 / 功能 / 硬件 / 功耗 / pogo 配置），
    它们讲的是**同一个东西**，拆成 5 页就是 5 个半页（§5 不许的重复页）。

    第一版一行只放一篇，于是**那 5 篇里只有 1 篇会被 `sources:` 认领**，
    其余 4 篇永远留在第六类的「未归属」里，**❌ 永远不灭**——
    而真相是它们已经被一页写掉了。**报告会和事实不一致，然后就没人信报告。**

    但 `sources:` 是**页面自己声明的「我定义的是哪几篇」**（第六类按它反查），
    所以这里必须能声明多篇。**第一篇仍是主文档**（语法节从它抽）。
    """
    return [x.strip() for x in (row.get('rel') or '').split(';') if x.strip()]


def build(row):
    rels = rels_of(row)
    rel = rels[0]
    d = op.load_docs().get(rel, {})
    title = ((d.get('frontmatter') or {}).get('title') or row['slug'])
    today = date.today().isoformat()

    w = ['---',
         f"type: {row['type']}",
         f'title: {title}',
         f"layer: {row['layer']}",
         f"stage: {row['stage']}",
         'tags: []',
         'related: []',
         'sources:']
    w += [f'  - {r}' for r in rels]
    w += [f'created: {today}',
         f'updated: {today}',
         'verified: doc-only',
         '---', '',
         f'# {title}', '',
         '<!-- 骨架由 `extract/objscaffold.py` 生成。',
         '     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；',
         '     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->', '']

    w += [syntax_block(rel)]
    # 报错节（2026-09-20）：**有材料才写**——`error_block()` 没材料时返回 `''`，
    # 空节会被读成「这条命令不会失败」。**新页出生就带上，省得每批补跑一次。**
    eb = error_block(rel)
    if eb:
        w += [eb]

    for sec in ['是什么', '典型用法', '和谁有关', '版本', '出处']:
        w += [f'## {sec}', '', PLACEHOLDER, '']
    return '\n'.join(w), title


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    force = '--force' in sys.argv

    rows = [r for r in csv.DictReader(PLAN.open(encoding='utf-8'))
            if r['slug'] and not r['slug'].startswith('#')]
    # 撞名检查：slug 不许撞已存在的页（§5 那条 `PATTERN` → `pattern-object` 的教训）
    have = {p.stem for p in WIKI.rglob('*.md')}
    seen = {}
    for r in rows:
        s = r['slug']
        if s in seen:
            raise SystemExit(f'❌ 两条计划撞同一个 slug：{s}（{seen[s]} / {r["rel"]}）')
        seen[s] = r['rel']
        if r['type'] not in DIRS:
            raise SystemExit(f'❌ 未知 type：{r["type"]}（{s}）')
        # **`skeleton` 是 2026-09-18 加的第三个值**（文件在、正文还是骨架）。
        # 本脚本只认「是不是合法值」——**判据本身在 `plan_sync.is_skeleton()`，
        # 这里不重复实现**：两处各写一份正则，就会有一天不一致。
        # 下面建页的循环只挑 `todo`，所以 `skeleton` 天然被跳过（页面在、不该重建），
        # 正是想要的。
        if r['status'] not in ('todo', 'skeleton', 'done'):
            raise SystemExit(f'❌ 未知 status：{r["status"]}（{s}）')

    # **rel 逐条查存在**：抄错一个字符，页面照建、`sources:` 照写，
    # 而第六类会**照着一个不存在的 rel 认为「这篇有人认领了」**——错误被静默吸收。
    # 逐条查一遍，成本 0。
    _docs = op.load_docs()
    for r in rows:
        for x in rels_of(r):
            if x not in _docs:
                raise SystemExit(f'❌ {r["slug"]} 的 rel 不在语料索引里：{x}')

    # `--refresh-syntax <slug> [<slug>…]`：只重刷语法节，不动散文。
    refresh_slugs = []
    if '--refresh-syntax' in sys.argv:
        k = sys.argv.index('--refresh-syntax')
        refresh_slugs = [s for s in sys.argv[k + 1:] if not s.startswith('--')]
        if not refresh_slugs:
            raise SystemExit('用：python objscaffold.py --refresh-syntax <slug> [<slug>…]')
    if '--refresh-errors' in sys.argv:
        k = sys.argv.index('--refresh-errors')
        rest = sys.argv[k + 1:]
        all_flag = '--all' in rest
        err_slugs = [s for s in rest if not s.startswith('--')]
        if not err_slugs and not all_flag:
            raise SystemExit('用：python objscaffold.py --refresh-errors <slug> [<slug>…]；'
                             '或 --refresh-errors --all 扫全部对象页')
        by = {r['slug']: r for r in rows}
        n = {'inserted': 0, 'refreshed': 0, 'skip': 0}
        targets = ([r for r in rows if r['type'] == 'object'] if all_flag
                   else [by[s] for s in err_slugs if s in by])
        for r in targets:
            n[refresh_errors(r)] += 1
        print(f"✅ 报错节：插入 {n['inserted']}、重刷 {n['refreshed']}、无材料跳过 {n['skip']}")
        return

    if refresh_slugs:
        by = {r['slug']: r for r in rows}
        for s in refresh_slugs:
            if s not in by:
                raise SystemExit(f'❌ wiki-plan.csv 里没有这个 slug：{s}')
            refresh(by[s])
        return

    for r in rows:
        if r['status'] != 'todo':
            continue
        p = WIKI / DIRS[r['type']] / f"{r['slug']}.md"
        if p.exists() and not force:
            print(f'⏭  已存在，跳过：{p.name}（要覆盖加 --force）')
            continue
        if r['slug'] in have:
            raise SystemExit(f'❌ slug 撞上已存在的页：{r["slug"]}——先定限定词（§5）')
        text, title = build(r)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8')
        print(f'✅ {p.relative_to(BASE)}  （{len(text):,} 字符）  {title}')


if __name__ == '__main__':
    main()
