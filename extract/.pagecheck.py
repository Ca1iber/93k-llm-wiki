# 临时：写页自检。逐页跑，只读不写。
#   ① 正文 [[wikilink]] 全在 allowlist 内（反引号里的不算——那是格式说明）
#   ② frontmatter related: 全在 allowlist 内
#   ③ 无 `（待补）` 残留、骨架注释已删
#   ④ 只动过 tags / related / updated —— 照原骨架比对 frontmatter 其余字段
import re
import pathlib
import sys

AL = {l.strip() for l in open('extract/prose-allowlist.txt', encoding='utf-8') if l.strip()}
# 已经存在的页 stem —— 与 verify_stages.py 第八类同一判据（`have`）
HAVE = {p.stem for p in pathlib.Path('wiki').rglob('*.md')}
KEEP = {'type', 'title', 'layer', 'stage', 'sources', 'created', 'verified'}


def check(path):
    p = pathlib.Path(path)
    t = p.read_text(encoding='utf-8')
    problems = []

    # ① 正文 wikilink：先挖掉 code span，再找 [[…]]（这一遍查「链了清单外的名字」）
    body = re.sub(r'`[^`\n]*`', '', t)
    names = set(re.findall(r'\[\[([^\]|]+)', body))
    bad = sorted(n.strip() for n in names if n.strip() not in AL)
    if bad:
        problems.append('正文 wikilink 越界: %s' % bad)

    # ①b **代码跨度里的 wikilink 也算链接**（verify_stages.py 第八类的口径，故意的）。
    # 所以「解释某条链已经拆掉」的散文里若把旧名字写成双方括号，就会把那条悬空目标原样造回来。
    # 2026-09-18 与 2026-09-21 各踩过一次（`ddic`、`data-logging-profile`）。
    # 只报**会造成悬空**的那些（有页的名字即使写在代码跨度里，第八类也不会记它）；
    # 逐字引别页表格里的 `[[x]]` 单元格是合法的，不该报。
    allspans = set(re.findall(r'\[\[([^\]|]+)', t))
    dangling = sorted(n.strip() for n in (allspans - names) if n.strip() not in HAVE)
    if dangling:
        problems.append('代码跨度里的 wikilink 会造成悬空（第八类照算）: %s' % dangling)

    # ② related:
    m = re.search(r'^related:(.*?)(?=^\w)', t, re.M | re.S)
    rel = []
    if m:
        rel = [x.strip().strip('[]') for x in m.group(1).split(',')]
        rel = [x for x in rel if x]
        badr = sorted(x for x in rel if x not in AL)
        if badr:
            problems.append('related 越界: %s' % badr)

    # ③ 残留
    if '（待补）' in t:
        problems.append('还有 `（待补）` 残留')
    # 注意：语法节/报错节的表头里也含 `objscaffold.py`，不能用它判。
    # 可删的那块以「补完请删掉本注释」结尾。
    if '补完请删掉本注释' in t:
        problems.append('骨架注释未删')
    # ③b **只删了收尾行、留下没闭合的 `<!--`**：它会把后面的 `## 语法 / 参数` 吞进注释里，
    # 渲染出来就没有那个标题了。2026-09-21 在 4 页上真发生过，
    # 是工程自己的第十五类（`plan_sync.is_skeleton()`）抓出来的，本脚本当时抓不到。
    if '骨架由 `extract/objscaffold.py` 生成' in t:
        problems.append('骨架注释只删了一半（`<!--` 未闭合，会吞掉 `## 语法 / 参数`）')

    # ④ frontmatter 未许动的字段：只看字段名在不在，值由脚本块新鲜度检查兜底
    fm = re.match(r'^---\n(.*?)\n---\n', t, re.S)
    keys = set(re.findall(r'^(\w+):', fm.group(1), re.M)) if fm else set()
    missing = KEEP - keys
    if missing:
        problems.append('frontmatter 少了字段: %s' % sorted(missing))
    extra = keys - KEEP - {'tags', 'related', 'updated'}
    if extra:
        problems.append('frontmatter 多了字段: %s' % sorted(extra))

    print('%s  wikilink=%d related=%d' % (p.as_posix(), len(names), len(rel)))
    if problems:
        for x in problems:
            print('   ✗ %s' % x)
    else:
        print('   ✅')
    return not problems


if __name__ == '__main__':
    ok = all(check(a) for a in sys.argv[1:])
    sys.exit(0 if ok else 1)
