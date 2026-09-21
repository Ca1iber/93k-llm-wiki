"""第十四、十五类 + 退出码总闸的**反向测试**。

规矩来自本工程自己：**一条检查写完，必须证明它抓得住它声称要抓的东西。**
做法：把 `wiki/` 和 `extract/` 各拷一份到临时目录，只改那一份，
把 `V.WIKI` / `V.OUTDIR` 指过去。**绝不动真的 `wiki/index.md`。**

**这份脚本留着，不是一次性的**：`$?` 那条总闸、以及第十四/十五类的每一条判据，
下次谁改 `verify_stages.py` 时靠它证明「还抓得住」。
**跑法**：`python -X utf8 extract/_negtest_checks.py`，全绿就行（末尾会自己收摊）。

> **⚠️ 2026-09-18 改名**：原叫 `_negtest_cat14.py`。加第十五类的用例时改名，
> 因为**文件名会变成假话**——里面装着两个类的用例，名字只说一个。
> 这正是本仓库反复记的那个病（说明与实际不符），而且是最容易发生的一种：
> **加用例的人不会想到要改文件名。** 现在的名字按「它测什么」起，不按类号起，
> **以后加类不用再改名**。`schema.md` 里那处引用同步改了。
"""

import re
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, r'F:\master-dev\understand-anything-wiki\extract')
import verify_stages as V
import objscaffold as OS_

REAL_W = Path(r'F:\master-dev\understand-anything-wiki\wiki')
REAL_O = Path(r'F:\master-dev\understand-anything-wiki\extract')

tmp = Path(tempfile.mkdtemp(prefix='negtest-'))
shutil.copytree(REAL_W, tmp / 'wiki')
shutil.copytree(REAL_O, tmp / 'extract')
ORIG = (tmp / 'wiki' / 'index.md').read_text(encoding='utf-8')
V.WIKI = tmp / 'wiki'
# **丁/戊 读的是 `OUTDIR / wiki-plan.csv`，也得指到临时那份去**——
# 不指的话那两条量的是真表、其余量的是临时表，**一个测试里两套数据源**，
# 绿了也不知道绿的是哪一份。指针要跟着被测对象一起搬。
V.OUTDIR = tmp / 'extract'

print(f'临时目录：{tmp}\n')


def realign():
    """把临时 `index.md` 的 `<!-- index-token -->` 标记刷成实测值。

    **为什么每次注入之后都要跑一遍（2026-09-18 加）。**
    本文件的注入**改的是 `index.md` 的正文**，而己 的判据是
    「页面自己写的 token 数 == 实测」——于是**任何一次改字都会让己变红**，
    而它红的原因**和这一条测试要测的东西毫无关系**。

    这个坑一直是有的（`丙 · 措辞改了` 那一例单独调了 `CIB.main(write=True)`
    来躲它），只是**当时注入的字符数恰好是 token 中性的**，所以没人发现。
    2026-09-18 改了注入点（`对象 22` → `79`）之后它露出来了：
    甲 的第二例报的是「己 差 -1」，**一条测试因为另一个类变红而挂**。

    **修法不是给那一例打补丁**（下一例照样会踩），而是**把它变成 `run_case` 的默认动作**：
    注入 → 对齐标记 → 再跑。**唯一要显式关掉它的是「己」自己那一例**，
    它注入的就是标记，对齐了就等于把注入抹掉。
    """
    import io
    import contextlib
    import check_index_budget as CIB

    class Quiet(io.StringIO):
        """吃掉 `check_index_budget` 的打印，但**必须长得像 stdout**。

        **不能直接用 `(io.StringIO())`**：那个模块开头有一句
        `sys.stdout.reconfigure(encoding='utf-8')`，而 `StringIO` **没有
        `reconfigure`**——第一次这么写就 `AttributeError` 挂在这里。
        **把输出重定向到一个「不太像 stdout 的假 stdout」是个常见陷阱**：
        被测代码只要碰一下 `sys.stdout` 的别的属性就炸。
        """
        def reconfigure(self, **kw):
            pass

    with contextlib.redirect_stdout(Quiet()):
        for _ in range(3):      # 标记自己的字符数也算在内，换位数时两次才收敛
            CIB.main(path=tmp / 'wiki' / 'index.md', write=True)


def run_case(name, text, want, fix_marker=True):
    """写进临时 index.md，单跑第十四类，看结果里有没有 `want`。"""
    (tmp / 'wiki' / 'index.md').write_text(text, encoding='utf-8')
    if fix_marker:
        realign()
    V.R.clear()
    ok = V.cat14_index_claims()
    out = '\n'.join(V.R)
    hit = want in out
    print(f'{"✅" if (hit and not ok) else "❌ 测试本身没通过"}  {name}：'
          f'返回 ok={ok}，报告里{"" if hit else "**没有**"}出现「{want}」')
    return hit and not ok


def sub(text, a, b):
    assert a in text, f'注入点没找到：{a}'
    return text.replace(a, b, 1)


# ---- **注入点不许写死**（2026-09-20 补）----
#
# 原先这里写的是 `sub(ORIG, '<!-- index-count: 对象 = 79 -->', …)`——
# 而对象的页数**已经涨到 143**，于是**负测试第 2 个用例就崩**，
# **后面 丁/戊/第十二到十五类 的用例一条都不跑**。
# 而这份脚本存在的全部理由就是「**证明绿不是假的**」——
# **它自己静默地废掉了大半，比没有它更坏**（§13.1 第九次就是「注入了一个不在文件里的串」，
# 那是第一次；这次是同一个病的第二次，只是换成「注入了一个过期的数」）。
#
# 所以注入一律**从被测文件里现读现算**，不抄常量。
CN = dict(zip('一二三四五六七八九十', range(1, 11)))


def find_marker(text, name):
    """→ `(匹配对象, 那个数)`。**找不到就断言失败**（不静默跳过）。"""
    m = re.search(rf'<!--\s*index-count:\s*{re.escape(name)}\s*=\s*(\d+)\s*-->', text)
    assert m, f'`{name}` 的 index-count 标记没找到——**判据改了，负测试要跟着改**'
    return m, int(m.group(1))


def bump_marker(text, name, delta=7):
    """把标记里的数改错 → `(新正文, 原数, 写进去的数)`。"""
    m, n = find_marker(text, name)
    return (text[:m.start()] + f'<!-- index-count: {name} = {n + delta} -->'
            + text[m.end():], n, n + delta)


def drop_marker(text, name):
    m, _ = find_marker(text, name)
    return text[:m.start()] + text[m.end():]


def bump_gap(text, delta=1):
    """`## 已知缺口（五条）` → 换成另一个数 → `(新正文, 原数, 新数)`。

    **也现读**：这条标题的措辞已经被改过一次（第十二次附记），
    所以正则里 `条` 前面的空格写成可选。
    """
    m = re.search(r'## 已知缺口（([一二三四五六七八九十]+) ?条）', text)
    assert m, '`## 已知缺口（N 条）` 没找到——**措辞改了，负测试要跟着改**'
    old = CN[m.group(1)]
    new = old + delta
    cn = {v: k for k, v in CN.items()}[new]
    return text[:m.start()] + f'## 已知缺口（{cn}条）' + text[m.end():], old, new


# ---- 甲 · 漏列：新建一页却不登记（**就是本次真正踩到的那个坑**）----
# 第一版测试是「删一行 `[[pogocabling-section]]`」——**没红，但那是测试写错了**：
# 那一节里 `pogocabling-section` 被链了两次（351 行的条目 + 361 行的说明），
# 删一行它还在。**这说明「数出现次数」比「数链接行」更容易骗过检查。**
shutil.copy(tmp / 'wiki' / 'objects' / 'pogocabling-section.md',
            tmp / 'wiki' / 'objects' / 'zzz-新建但没登记.md')
run_case('甲 · 目录里有一页、节里没列',
         ORIG, '`zzz-新建但没登记`')
(tmp / 'wiki' / 'objects' / 'zzz-新建但没登记.md').unlink()

# ---- 甲 · 列了但不存在（指到一个没有的页）----
run_case('甲 · 节里列了一个不存在的页',
         sub(ORIG, '[[pogocabling-section]] `file/pin`',
             '[[zzz-nope]] `file/pin`'),
         '❌ `zzz-nope`')

# ---- 乙：把标记的数改错 ----
_inj, _old, _new = bump_marker(ORIG, '对象')
run_case('乙 · 标记写的数和实际不符', _inj, f'`对象` | {_new} | {_old} | ❌')

# ---- 乙 · 把标记删掉 ----
run_case('乙 · 整节没有标记', drop_marker(ORIG, '排错'), '`排错` | ❌ **没有标记**')

# ---- 丙：散文里的数改错 ----
_inj, _old, _new = bump_gap(ORIG)
run_case(f'丙 · 已知缺口写「{_new} 条」而实际 {_old} 条',
         _inj, f'已知缺口（N 条） | `{_new}` | `{_old}` | ❌')

# ---- 丙：措辞改了 → 只 ℹ️，不判错（**这条测的是「不许静默」**）----
# 判据：**结果必须是绿的，但报告里必须印出「没找到」。**
# 绿 + 不印 = 这条声明死了而没人知道，那才是要防的。
(tmp / 'wiki' / 'index.md').write_text(
    sub(ORIG, '## 阶段（脊椎，9）', '## 阶段（脊椎 9 页）'), encoding='utf-8')
# ⚠️ **改了 `index.md` 的正文，就要把 `<!-- index-token -->` 标记重新对齐**
# （己 的判据是「页面自己写的数 == 实测」）。**这不是测试的技巧，是真实工作流**：
# 任何一次改 `index.md`，之后都要跑一次 `check_index_budget.py --write`。
# 不重对齐的话，这条测试会因为**己**变红而挂，而它要测的是**丙**。
import check_index_budget as CIB
for _ in range(3):                       # 标记自己的字符数也算，换位数时两次才收敛
    CIB.main(path=tmp / 'wiki' / 'index.md', write=True)
V.R.clear()
ok = V.cat14_index_claims()
out = '\n'.join(V.R)
miss_line = [l for l in out.split('\n') if '这句没找到' in l]
print(f'{"✅" if (ok and miss_line) else "❌ 测试本身没通过"}  '
      f'丙 · 措辞改了就匹配不上：ok={ok}（**要绿**），'
      f'{len(miss_line)} 行「没找到」（**要 ≥1**）')
print(f'     {miss_line[0] if miss_line else "（一行都没有——措辞改了却什么都没说）"}')

# ---- 丁 · `status` 和文件在不在对不上 ----
# **注入的是「真表曾经的样子」**：2026-09-18 实测有 20 行是这个状态。
# 从临时表里挑第一行 `done` 改成 `todo`（那一页文件是真的在）。
PLAN = tmp / 'extract' / 'wiki-plan.csv'
PLAN_ORIG = PLAN.read_bytes()
raw = PLAN_ORIG.decode('utf-8')
lines = raw.split('\n')
k = next(i for i, l in enumerate(lines) if l and not l.startswith('#')
         and not l.startswith('slug,') and ',done' in l)
lines[k] = lines[k].replace(',done', ',todo', 1)
PLAN.write_text('\n'.join(lines), encoding='utf-8', newline='')
run_case('丁 · 页面在、表里却写 todo',
         ORIG, f'❌ **1 行不符**：{lines[k].split(",")[0]}')
PLAN.write_bytes(PLAN_ORIG)

# ---- 戊 · 页面建了、计划表里没有这一行 ----
shutil.copy(tmp / 'wiki' / 'objects' / 'pogocabling-section.md',
            tmp / 'wiki' / 'objects' / 'zzz-戊测试.md')
run_case('戊 · 目录里有页、表里没登记',
         ORIG, '❌ **1 页没有登记行**：`zzz-戊测试`')
(tmp / 'wiki' / 'objects' / 'zzz-戊测试.md').unlink()

# ---- 第十二类 · **该有语法节标记的页面，标记被删掉了** ----
# 这一条是本次新判据的反向测试。旧写法下**这个注入是不会红的**：
# `page_section()` 返回 `None`，代码把 `None` 当成「不一致」……不，
# 旧写法里 `object` 页删掉整节之后 `cur is None` → 落进 `stale`，
# **看起来是红了，但红的原因是错的**（报「页面 0 字符 vs 抽取器 N 字符」，
# 而真相是「这一节没了」）。更要命的是**只删标记、留下正文**那种改法：
# 旧写法 `cur` 是 `None`（找不到 `## 语法 / 参数` 时）才红——
# 只要标题还在，它就照常比较，**根本发现不了标记没了**。
# **新判据直接盯标记**，两种改法都落在「该有标记而没有」上。
OS_.WIKI = tmp / 'wiki'                    # check_syntax_fresh 走的是 objscaffold 的常量
OS_.PLAN = PLAN
_obj = tmp / 'wiki' / 'objects' / 'pogocabling-section.md'
_obj_orig = _obj.read_text(encoding='utf-8')
_obj.write_text(_obj_orig.replace(OS_.MARK_BEGIN, '', 1), encoding='utf-8')
V.R.clear()
ok12 = V.cat12_syntax_fresh()
out12 = '\n'.join(V.R)
hit12 = '没有 `<!-- 语法节 begin -->` 标记' in out12 and '`pogocabling-section`' in out12
print(f'{"✅" if (hit12 and not ok12) else "❌ 测试本身没通过"}  '
      f'第十二类 · 脚手架页的语法节标记被删：ok={ok12}，'
      f'报告里{"" if hit12 else "**没有**"}点出这一页')
# **反方向也要证**：29 页纯散文页**不许**被算成「该有标记而没有」。
# 数字从 `check_syntax_fresh.LAST` 里读——**不许在这里写死 29 和 1 之外的期望**，
# 但也**不许反过来**：`unmarked` 期望 1 是因为我们只删了一页的标记。
import check_syntax_fresh as CSF
L = CSF.LAST
# ⚠️ **`L` 是 `CSF.LAST` 这个 dict 本身，不是它的副本。** 基线那一跑会把它**就地覆盖**，
# 所以**先把注入那一跑的三个数取出来**，再跑基线——否则读到的是基线那份，
# 而那句「要 1」会永远是 0。（第一版就是这么错的，**当场被这一行报出来**。）
_n_inject, _un_inject, _fresh_inject = len(L['prose']), len(L['unmarked']), len(L['fresh'])
# **基线现量，不写死。** 原先是 `== 29`，而纯散文页**已经从 29 涨到 38**
# （建页就会涨）——于是这一条**每次都报「测试本身没通过」**，
# 而**它旁边那行注释正好写着「不许在这里写死 29」**：说明和代码不符，又是那个病。
#
# 真正要证的不变式是**注入前后 `prose` 不变、`unmarked` 恰好 +1**（我们只删了一页的标记）。
# 所以基线**从真的那份仓库量一次**——这是独立来源，而且不会过期。
_bak_w, _bak_o = V.WIKI, OS_.WIKI
V.WIKI = OS_.WIKI = REAL_W
CSF.main()
_base = len(CSF.LAST['prose'])
V.WIKI, OS_.WIKI = _bak_w, _bak_o
ok12b = (_n_inject == _base and _un_inject == 1)
print(f'{"✅" if ok12b else "❌ 测试本身没通过"}  '
      f'第十二类 · 纯散文页按设计不参与比较：'
      f'prose={_n_inject}（真仓库基线 {_base}，**注入不该动它**）、'
      f'unmarked={_un_inject}（要 1）、逐字比了 {_fresh_inject} 页')
_obj.write_text(_obj_orig, encoding='utf-8')

# ---- 己 · `index.md` 的 token 标记和实测对不上 ----
# **把标记改成一个明显错的数**。这一条查的是「页面自己写的数」，
# 所以注入点必须是标记本身——**改正文没用**，正文里那个数不在判据里（见 §7 的说明）。
_mark = re.search(r'<!--\s*index-token:.*?-->', ORIG)
assert _mark, 'index.md 里没有 index-token 标记——己 的注入点没了'
# **断言里不写实测的那个数**：标记改短了，实测值就跟着变几个 token
# （标记自己的字符也算在内）。判据是「**两份数不一样**」这个事实，不是某个具体数字——
# 把数字写进测试，就等于让测试跟着实现一起漂。
run_case('己 · token 标记写的数和实测不符',
         sub(ORIG, _mark.group(0), '<!-- index-token: cl100k_base=100 o200k_base=100 -->'),
         '和实测不符', fix_marker=False)   # ← **这一例注入的就是标记，对齐等于抹掉注入**

# ---- 第十五类 · 骨架占位符 ----
#
# **这一条的反向测试和别的不一样，得先说清为什么。**
# 其余各类的判据是「某一页符不符合」，注入一处坏 → 类红。
# 第十五类现在**本来就红**（第四批还有若干页骨架没写，数字天天在动），
# 所以「修好一页 → 类转绿」
# 这条路**今天走不通**。于是分两段证：
#   ① **类级别的红**：把占位符塞回一页已写完的页 → 报告里必须点出这一页；
#   ② **判据级别的双向**：`plan_sync.is_skeleton()` 对「有占位符」「有骨架注释」
#      「两个都清掉」三种状态各给什么答案。**判据只有一处实现，
#      所以证它等于证了类、也证了第十四类丁。**
import plan_sync as PS
# **注入点要挑一页确实写完了的。** 第一版挑的是 `pogocabling-section`，
# 而它正文里**还留着一个行内的 `（待补）`**（骨架没清干净）——断言当场挂在它身上。
# **那不是测试的毛病，是它替我们抓到了一页真没写完的页**（第十五类现在就把它列着）。
# 挑定稿的 exemplar 当注入点，别挑「我以为写完了」的。
_done_page = tmp / 'wiki' / 'objects' / 'analysis-views.md'
_done_orig = _done_page.read_text(encoding='utf-8')
assert not PS.is_skeleton(_done_page), \
    'analysis-views 现在被当成骨架了——下面 ① 的注入点不成立'
assert '（待补）' not in _done_orig
assert '\n## 是什么\n' in _done_orig, '注入点 `## 是什么` 不在这一页里'

# ①-A：塞一个占位符回正文
_done_page.write_text(
    _done_orig.replace('\n## 是什么\n\n', '\n## 是什么\n\n（待补）\n', 1),
    encoding='utf-8')
V.R.clear()
ok15 = V.cat15_skeleton()
out15 = '\n'.join(V.R)
hit_a = '`objects/analysis-views`' in out15 and '`（待补）` × 1' in out15
print(f'{"✅" if (hit_a and not ok15) else "❌ 测试本身没通过"}  '
      f'第十五类 · 占位符塞回一页已写完的页：ok={ok15}（要 False），'
      f'报告里{"" if hit_a else "**没有**"}点出这一页、也没数对个数')

# ①-B：**只删注释、只填正文，是不够的**——骨架注释仍在也要红。
# 这一条测的是「两个 marker 都要认」：只认一个的话，agent 填完正文忘了删注释
# （或反过来）就会被判 ok，**而那正好是本类要防的那个中间状态**。
_done_page.write_text(
    _done_orig.replace('\n## 是什么\n', '\n## 是什么\n\n（待补）\n', 1)
    + '\n<!-- 骨架由 `extract/objscaffold.py` 生成。 -->\n', encoding='utf-8')
V.R.clear()
ok15b = V.cat15_skeleton()
out15b = '\n'.join(V.R)
hit_b = '骨架注释还在' in out15b
print(f'{"✅" if (hit_b and not ok15b) else "❌ 测试本身没通过"}  '
      f'第十五类 · 占位符＋骨架注释同时在：报告里{"" if hit_b else "**没有**"}'
      f'说「骨架注释还在」')

# ②判据双向。三种状态各一个文件，**看 `is_skeleton` 说什么**。
_probe = tmp / 'wiki' / 'objects' / 'zzz-判据探针.md'
cases = [
    ('只有占位符', '正文\n\n（待补）\n', True),
    ('只有骨架注释', '正文\n\n<!-- 骨架由 x -->\n', True),
    ('半角括号的占位符', '正文\n\n(待补)\n', True),
    ('两个都清掉', '正文，真的写过了。\n', False),
    ('「待补」出现在别处（不是占位符）', '库里写的是「待补充材料」四个字。\n', False),
]
for name, text, want in cases:
    _probe.write_text(text, encoding='utf-8')
    got = PS.is_skeleton(_probe)
    print(f'{"✅" if got == want else "❌"}  第十五类 · 判据探针「{name}」：'
          f'is_skeleton={got}（要 {want}）')
_probe.unlink()

# ③**反方向：不许误红。** 恢复原状后，**这一页**必须从骨架名单里消失。
#
# **这里不许断言 `ok15c is True`**：类级结果还要看**其余 63 页**
# （它们今天真的还是骨架）。断言整体绿等于**让测试依赖「活儿干完了没有」**——
# 那样这批页一写完，这个测试就从「测判据」变成「什么都没测」，
# 而**它自己不会告诉你这件事**。所以只断言与本次注入有关的那一页。
_done_page.write_text(_done_orig, encoding='utf-8')
V.R.clear()
ok15c = V.cat15_skeleton()
out15c = '\n'.join(V.R)
clean = '`objects/analysis-views`' not in out15c
thin_marked = '最薄的十节' in out15c
all_clean = '页的正文都写过了' in out15c
print(f'{"✅" if (clean and thin_marked) else "❌ 测试本身没通过"}  '
      f'第十五类 · 恢复原状后这一页从名单里消失：'
      f'{"" if clean else "**还在名单里**"}；'
      f'薄节{"" if thin_marked else "**没有**"}被列出来（**列而不判红**）')
print(f'     （类级 ok={ok15c}，{"全部写完，类绿" if all_clean else "仍有骨架页，类红"}'
      f'——**这个数跟着进度走，所以上面不断言它**）')

# ---- 总闸：第十四类红了，`main()` 到底退不退非零 ----
(tmp / 'wiki' / 'index.md').write_text(
    bump_marker(ORIG, '对象')[0],
    encoding='utf-8')
V.R.clear()
try:
    V.main()
except SystemExit as e:
    print(f'\n✅ 总闸：`main()` 抛了 SystemExit —— {e}')
    print('   （这就是本次补的东西：**在此之前它是 `return None`，进程退 0**。）')
else:
    print('\n❌ 测试本身没通过：第十四类红了，`main()` 却正常返回、进程会退 0。')

shutil.rmtree(tmp, ignore_errors=True)
