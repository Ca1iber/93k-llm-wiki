# -*- coding: utf-8 -*-
"""**新检查**：已建页的 `## 语法 / 参数` 与抽取器**当前**输出是否一致。

**为什么需要它。** §4 把一页劈成两半：语法节是脚本的，散文是 LLM 的。
脚本改了抽取逻辑之后，**没有一条检查会告诉你哪些页面的语法节过期了**——
`objscaffold.py --refresh-syntax` 得**先知道**要刷哪几个 slug。
2026-09-18 修 `verbatim_sections` 那个 bug 时，我是**手工挑了两个 slug**去刷的；
**手工挑就会漏**，而漏掉的页面看上去完全正常。

**判据**：把页面里 `## 语法 / 参数` 到下一个 `## ` 之间的文本，
和 `objscaffold.syntax_block(rel)` 逐字比。不一致就是过期。

**这是「检查比它自称的范围窄」的第四面镜子**：前三面查的是页面之间、
页面与语料之间，这一面查的是**页面与产出它的脚本之间**。

---

**2026-09-18 补的第二面：这一条自己也在「比自称的范围窄」。**

`plan_sync.py` 把 29 行 stage/constraint/error 回填进 `wiki-plan.csv` 之后，
本脚本**对那 29 页一个字都查不了**——它们没有 `## 语法 / 参数` 节，
`page_section()` 返回 `None`，于是**连比较都不发生**。

原来的写法是 `fresh if cur is not None and cur == want else stale`：
**`cur is None` 掉进 `stale` 是碰巧**——因为那时表里只有 30 页、全都有语法节。
29 页新输入一进来，它们会**全部报成「过期」**（页面 0 字符 vs 抽取器 N 字符），
而真相是：**这 29 页按设计就没有这一节**（§4：脚本出骨架的是对象页）。

> 这就是 §13.1 第 ⑥′ 问：「这条检查绿，是因为查过了没问题，
> 还是因为它根本没查到东西？」
> **反方向同样致命**：一条检查**红**，也可能只是它把「不适用」当成了「不合格」。

所以判据改成**两边都封死**：

| 页面的 `type` | 页面里必须 | 为什么 |
|---|---|---|
| `object` / `concept`（脚本出骨架的，见 `SCAFFOLDED`） | **必须有** `<!-- 语法节 begin -->` 标记 | 没标记 = 这一节被删了/改了名/被手写顶掉了，**而旧写法会静默跳过它** |
| 其余（`constraint` / `error` / `stage` / `mapping`） | 不要求 | 这些页是纯散文页，本来就没有脚本写的一节 |

**判据挂在标记上，不挂在类型上**——标记是「这一节归脚本管」的**声明**，
脚本只核验自己的声明：**带标记的页一律逐字比**（哪怕它的 type 不在上表里），
**不带标记的脚手架页一律红**。两个方向都看得见，才叫封死。
"""
import csv
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, str(Path(__file__).parent))
import objscaffold as os_
import subindex

HEAD = os_.HEAD

# **脚本出骨架的类型**（`objscaffold.build()` 的输出）。
# 实测 2026-09-18：30 页 object+concept **全部** 有 头/起/止 三个标记齐全，
# 29 页 constraint+error+stage **全部** 一个都没有——**没有中间态**。
# 这个整洁本身就是证据：分工是按类型走的，不是零散的。
SCAFFOLDED = ('object', 'concept')

# 由 `main()` 填。**调用方读这个，不许自己数、更不许写死。**
#
# ⚠️ 2026-09-18 从 `[一致, 过期, 未建页]` 改成 dict：加第四项时才发现
# 调用方写的是 `n_fresh, _, n_missing = csf.LAST_COUNTS`——
# **位置解包**，多一项就 `ValueError`，少一项就悄悄错位。
# 位置解包和硬编码数字是同一个病（结论的形状被写死在读的人那里）。
#
# **装的是清单本身、不是计数。** 第一版装计数，于是报告里只能印出数字，
# 要印「是哪几页」就得**再存一份平行的清单**——两份东西必然有一天不同步。
# 现在 `len()` 由读的人自己算，**数字和名单不可能对不上**。
LAST = {'fresh': [], 'stale': [], 'missing': [], 'unmarked': [], 'prose': []}


def page_section(p):
    """**边界用 `objscaffold.section_end`**，不许写 `find('\\n## ')`。

    第一版这里就是 `find('\\n## ')`，于是 `device-architecture-file` 被误报成
    「页面 3,527 vs 抽取器 24,820」——**那一页的语法节里嵌着十几个 `## `**
    （`_file_syntax` 整篇照收）。**检查器犯的错和它要查的东西是同一种**：
    范围比自称的窄。抽成同一个函数，两边就再也不会各判各的。
    """
    t = p.read_text(encoding='utf-8')
    i = t.find(HEAD)
    if i < 0:
        return None
    return t[i:os_.section_end(t, i)]


def page_error_section(p):
    """页面里报错节那一整块（**含节标题**，含 begin/end 标记）。没有则返回 None。

    **从 `ERR_HEAD` 起，不是从 `ERR_BEGIN` 起**（2026-09-20 修）：
    `error_block()` 返回的串是「标题 + 标记 + 正文」，这里若从标记起，
    就**少一段**——于是 10 页全被误报成「过期」，差的正好是标题那 53 个字符。
    **检查器和它要查的东西各判各的**——这个病在本文件里已经出现过一次
    （见 `page_section()` 的注释），这是第二次。
    """
    t = p.read_text(encoding='utf-8')
    i = t.find(os_.ERR_HEAD)
    if i < 0:
        return None
    j = t.find(os_.ERR_END, i)
    if j < 0:
        return None
    return t[i:j + len(os_.ERR_END)]


def main(strict=False):
    """**`rel` 列可能是分号分隔的多篇，这里必须取第一篇。**

    第一版写的是 `os_.syntax_block(r['rel'])`，把整串
    `主文档;补充1;补充2` 当成一个路径——于是 `dps128-dps64-cards`（5 篇）
    直接 `FileNotFoundError:` 崩掉，**第十二类整个跑不出来**。
    而 `objscaffold.build()` 用的是 `rels_of(row)[0]`（第一篇是主文档，
    语法节从它抽）——**两边口径不一致，检查判的东西和生成的东西不是一个东西**。
    这和 `page_section` 那条注释是同一个病：**检查器和它要查的对象各判各的。**
    """
    rows = [r for r in csv.DictReader(l for l in os_.PLAN.open(encoding='utf-8')
                                      if not l.startswith('#')) if r['slug']]
    fresh, stale, missing = [], [], []
    err_stale, err_unmarked = [], []
    unmarked, prose = [], []          # 见文件头那张表
    skipped_sub = []                  # §7 的子索引：不是骨架页，本类不管它
    for r in rows:
        if r['slug'] in subindex.STEMS:
            # **子索引不是 `objscaffold.py` 出的骨架**，没有也不该有语法节。
            # 它登记在 `extract/subindex.py`（**具名，不按 `index-` 前缀**——
            # 按模式豁免等于让「新加一个子索引」自动获得豁免，那是个洞）。
            # **跳过了必须报出来**，否则「没查」和「查了没问题」长得一样。
            skipped_sub.append(r['slug'])
            continue
        p = os_.WIKI / os_.DIRS[r['type']] / f"{r['slug']}.md"
        if not p.exists():
            missing.append(r['slug'])
            continue
        txt = p.read_text(encoding='utf-8')
        # **先按标记分流，再考虑类型**（顺序不能反：标记是页面自己的声明，
        # 类型只是「本该有声明」的名单）。
        if os_.MARK_BEGIN not in txt:
            if r['type'] in SCAFFOLDED:
                # 细分两种：标记没了但 `## 语法 / 参数` 标题还在 → 有人手写顶掉了
                # 脚本那一节；标题也没了 → 整节被删或改了名。**修法不同，所以分开报。**
                unmarked.append((r['slug'], r['type'],
                                 '标题还在' if HEAD in txt else '标题也没了'))
            else:
                prose.append(r['slug'])
            continue
        cur = page_section(p)
        want = os_.syntax_block(os_.rels_of(r)[0]).rstrip('\n')
        (fresh if cur is not None and cur.rstrip('\n') == want else stale).append(
            (r['slug'], len(cur or ''), len(want)))
        # ── 报错节（2026-09-20 加）：同一条规矩，同一个理由 ──
        # **没有这一比，报错节就是下一个静默过期**：脚本改了抽取、页面没跟上，
        # 而「报错节非空」照样绿——正是 §11.3③ 那个病的形状。
        ecur = page_error_section(p)
        ewant = os_.error_block(os_.rels_of(r)[0]).rstrip('\n')
        if ecur is not None:
            if ecur.rstrip('\n') != ewant:
                err_stale.append((r['slug'], len(ecur), len(ewant)))
        elif ewant:
            err_unmarked.append(r['slug'])
    # **数字由本函数给出，调用方不许自己写死。**
    # `verify_stages.py` 第十二类那行原来硬编码「12 个已建页」，
    # 建到 28 页时它就成了一句假话——**报告里最危险的不是红，是过期的绿。**
    LAST.update({'fresh': fresh, 'stale': stale, 'missing': missing,
                 'unmarked': unmarked, 'prose': prose, 'skipped_sub': skipped_sub,
                 'err_stale': err_stale, 'err_unmarked': err_unmarked})
    print(f'已建页 {len(fresh) + len(stale) + len(unmarked) + len(prose)} 个：'
          f'一致 {len(fresh)}，**过期 {len(stale)}**，'
          f'**该有语法节却没有 {len(unmarked)}**，'
          f'纯散文页（按设计不参与比较）{len(prose)}'
          f'{"：" + "、".join(prose[:6]) + "…" if prose else ""}')
    for s, a, b in stale:
        print(f'  ❌ {s}  页面 {a:,} 字符 vs 抽取器 {b:,} 字符（{b - a:+,}）')
    # **跳过要报出来**：不报的话，「本类没查它」和「本类查了没问题」长得一样。
    _skip = (f'；**跳过 {len(skipped_sub)} 个已登记的子索引**'
             f'（{"、".join(skipped_sub)}，它们不是骨架页）' if skipped_sub else '')
    print(f'报错节：过期 {len(err_stale)}，该有却没有 {len(err_unmarked)}{_skip}')
    for s, a, b in err_stale:
        print(f'  ❌ [报错节] {s}  页面 {a:,} vs 抽取器 {b:,}')
    for s in err_unmarked:
        print(f'  ❌ [报错节] {s}  raw 有 Errors 材料，页面里没有报错节')
    for s, t, what in unmarked:
        print(f'  ❌ {s}  type={t}，**没有 `语法节 begin` 标记**（{what}）'
              f'——旧写法会静默跳过它')
    if missing:
        print(f'  未建页（wiki-plan.csv 里有、文件不在）：{len(missing)}')
    if (stale or unmarked or err_stale or err_unmarked) and strict:
        raise SystemExit('❌ 语法节过期或该有标记而没有，跑：'
                         'python objscaffold.py --refresh-syntax '
                         + ' '.join(s for s, _, _ in stale + unmarked))
    return stale


if __name__ == '__main__':
    main(strict='--strict' in sys.argv)
