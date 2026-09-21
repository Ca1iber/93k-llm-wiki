"""把 `wiki-plan.csv` 和 `wiki/` 的实际状态对齐（**只做机械的两件事**）。

**为什么要有它。** `wiki-plan.csv` 的表头自己写着
「**这份文件是「建什么」的唯一记录**，不是散在对话里」——
而 2026-09-18 实测：**它两处都不真**。

| 实测 | 数 |
|---|---|
| 行里写 `todo`、**页面其实早就建好了** | **20** |
| 页面在六个类型目录里、**表里根本没有这一行** | **29** |

（第二条里包括九个 **stage 页**——它们**从来没进过这张表**，
因为表的 9 行注释被当成了 9 行空数据。）

所以「唯一记录」这半句是假的。本脚本把两件事**机械修掉**：

1. **`status` 跟着文件走**：页面在 → `done`；不在 → `todo`。
   这是**纯机械**的（文件在不在不需要判断），所以归脚本，不归 LLM（§4）。
2. **缺的行从页面自己的 frontmatter 回填**：
   `type` / `layer` / `stage` 抄页面的 frontmatter，`rel` 抄 `sources` 的第一条。
   **⚠️ 方向是反的，必须写明白**：正常流程是「先定计划 → 脚本出骨架 → 人写正文」，
   回填是「页面先建了 → 回头补计划行」。**回填的行 `note` 列会标出来。**

> **回填会不会让「建页没登记」这个错永远抓不到？** 不会——它抓的是**下一次**：
> 新页建了却没跑本脚本、也没进表，第十四类**戊**照样红。
> **回填只处理既成事实，不改判据。**

用：`python -X utf8 extract/plan_sync.py`            # 只看，不写
    `python -X utf8 extract/plan_sync.py --write`    # 真写
**它不碰任何 `wiki/**/*.md`**，只重写 `wiki-plan.csv`。
"""
import csv
import re
import sys
from pathlib import Path

BASE = Path(r'F:\master-dev\understand-anything-wiki')
OUT = BASE / 'extract'
WIKI = BASE / 'wiki'
PLAN = OUT / 'wiki-plan.csv'

# 计划表管这六个目录。`versions/` 不进表——那 143 页由 `versions.py` 整批生成，
# **它没有「一页一行的人工判断」可记**（§4：脚本产出的不登记进人工计划）。
DIRS = ['stages', 'objects', 'concepts', 'constraints', 'errors', 'mappings']

COLS = ['slug', 'type', 'layer', 'stage', 'rel', 'status', 'note']
HEAD_COMMENTS = [
    '# 建页计划 —— 一行一页。**这份文件是「建什么」的唯一记录**，不是散在对话里。',
    '# type/layer/stage 是人的判断（§2 / §6），slug 按 §5 定；rel 指定义该对象的那篇 raw。',
    '# objscaffold.py 读它出骨架；verify_stages.py 第六类按页面的 sources 反查归属。',
    '# 来源：extract/unowned.csv（= stage-report.md 第六类未归属清单，脚本断言两边同数）',
    '#',
    '# 2026-09-18 实测：本表曾与 wiki/ 实际差 20 行 status + 29 行缺失——**「唯一记录」当时是假的**。',
    '# 现在 status 由 extract/plan_sync.py 与文件对齐，第十四类丁/戊 两条检查看着它。',
    '# `note` 列：`回填` = 页面先建、计划行是事后从页面 frontmatter 抄的（方向是反的）。',
    '#',
    '# ── 2026-09-18 第二次修：`status` 从两个值改成三个。**原因是它当时在说假话。**',
    '# 原判据是「文件在不在」，于是 `objscaffold.py` 刚出完骨架、正文一个字没写的页',
    '# **也记成 `done`**——71 页里有 68 页当时是这个状态。**「done」这个词的意思是写完了，',
    '# 而它当时的意思是「文件在」**：本仓库记了多次的「说明与行为不符」，又一次。',
    '#   `todo`     = 文件不在（还没建）',
    '#   `skeleton` = 文件在，但正文还是骨架（`（待补）` 或骨架注释还在）',
    '#   `done`     = 文件在，且正文写过',
    '# 判据只有一处实现：`plan_sync.is_skeleton()`；第十五类看着它。',
]


def read_plan():
    """读计划表，**注释行原样留着**（它们是表头的一部分，不是数据）。

    **表头必须是第一行**（实测：`objscaffold.py` 和 `verify_stages.py` 都是
    `csv.DictReader(PLAN.open())` 直接读，第一行当字段名）。
    第一版把注释排在表头前面——**那样两个读者都会在 `r['slug']` 上 KeyError**。
    所以这里返回的四样东西里带一个 `nl`：**行尾也照原样写回去**（本文件是 CRLF，
    统一成 LF 会让整个文件变成一次无意义的 diff）。
    """
    raw = PLAN.read_bytes()
    nl = '\r\n' if b'\r\n' in raw else '\n'
    # **按 `\n` 切、再把每行末尾的 `\r` 剥掉**，不要按 `\r\n` 切：
    # 第一版按 `\r\n` 切，而 `write_text` 默认会把 `\n` **再翻译一次**成 `os.linesep`，
    # 于是写出去的是 `\r\r\n`；下一轮按 `\r\n` 切就把那个多余的 `\r` 留在行尾，
    # **再写一次还是 `\r\r\n`**——自己喂自己，永远修不回来。
    # 剥干净再拼，行尾就只有一种写法。
    lines = [l.rstrip('\r') for l in raw.decode('utf-8').split('\n')]
    header = next(ln for ln in lines if ln.startswith('slug,'))
    comments = [ln for ln in lines if ln.startswith('#')]
    data = [ln for ln in lines if ln.strip() and not ln.startswith('#')
            and ln is not header and not ln.startswith('slug,')]
    rows = list(csv.DictReader([header] + data))
    return header, comments, rows, nl


def fm_of(p):
    """只取 frontmatter 里那几行的值。**不引 yaml 库**（本工程 stdlib only）。

    **⚠️ 不能用 `split('---', 2)[1]` 取 frontmatter**（第一版就是这么写的）：
    `results.md` 的 `sources:` 列表里有一行**注释 `# --- 结果命令（L1 依据） ---`**，
    里面带 `---`，于是 split 在那里就断了，**那个页面的 20 条 sources 全丢**，
    回填出来的 `rel` 是空的。**分隔符出现在数据里，是最普通的一种塌方。**
    改成：**只认「整行等于 `---`」的那一行当结尾**。
    """
    txt = p.read_text(encoding='utf-8')
    lines = txt.split('\n')
    if lines[0].strip() != '---':
        return {}
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == '---'), None)
    if end is None:
        return {}
    block = '\n'.join(lines[1:end])
    out, key = {}, None
    for ln in block.split('\n'):
        if ln.startswith('sources:'):
            key = 'sources'
            out[key] = []
            continue
        if key == 'sources' and ln.strip().startswith('- '):
            out[key].append(ln.strip()[2:].strip())
            continue
        if ':' in ln and not ln.startswith(' '):
            k, v = ln.split(':', 1)
            out[k.strip()] = v.strip()
            key = k.strip()
    return out


# 「这页的正文还是骨架」的**唯一判据**。放在这里、别处 import 它——
# 三个地方要用同一个答案（本文件的 status、`verify_stages.py` 第十四类丁、
# 第十五类），**三处各写一份正则 = 三份会各自漂的判据**。
#
# 两个 marker 都要认，因为它们**是同一个状态的两处痕迹**，而实测两者会不同时消失：
#   - `（待补）`：`objscaffold.py` 填的占位符，人在写某一节时容易只删掉自己那节的；
#   - 骨架注释：PROSE-SPEC 要求补完删掉。它和占位符**都在头尾**，
#     但一个 agent 可能删了注释、只填了三节就断线——**只要还有一个，这页就没写完**。
#
# **半角括号也算**：`objscaffold.py` 现在写的是全角，但中文输入法下打半角是常事，
# 而「半角漏认」的后果是**一页明明没写完却判 ok**——正是这条检查要防的那个方向。
RE_TODO = re.compile(r'[（(]\s*待补\s*[)）]')
SKEL_COMMENT = '<!-- 骨架由'


def is_skeleton(p):
    """文件在、正文还是骨架 → `True`。**判据只有这一处。**

    **不看 frontmatter、不看语法节**：这两块正是脚本写的，
    **agent 断线时它们一定齐全**——拿它们当判据，等于问「脚本跑过没有」，
    而脚本一定跑过。**要问的是「散文有没有到」，所以只读正文。**
    """
    t = p.read_text(encoding='utf-8')
    return bool(RE_TODO.search(t)) or SKEL_COMMENT in t


def status_of(p):
    """`Path | None` → 三个 status 之一。**这是「status 该怎么写」的唯一实现。**"""
    if p is None:
        return 'todo'
    return 'skeleton' if is_skeleton(p) else 'done'


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    write = '--write' in sys.argv

    header, comments, rows, nl = read_plan()
    pages = {p.stem: p for d in DIRS for p in (WIKI / d).glob('*.md')}
    have = {r['slug'] for r in rows}

    n_done, n_todo, n_skel, backfill = 0, 0, 0, []
    n_rel_fix = 0
    for r in rows:
        want = status_of(pages.get(r['slug']))
        if r.get('status') != want:
            if want == 'done':
                n_done += 1
            elif want == 'skeleton':
                n_skel += 1
            else:
                n_todo += 1
            r['status'] = want
        r.setdefault('note', '')
        # 回填行如果 `rel` 是空的（正是 `fm_of` 那个 `---` bug 造成的），
        # **补上**：空着不是「不确定」，是「连同一条都没读出来」——
        # 而 `rel` 是 `objscaffold` 抽语法节的输入，空着就会在后面某处 IndexError。
        if not (r.get('rel') or '').strip() and r['slug'] in pages:
            srcs = fm_of(pages[r['slug']]).get('sources') or []
            if srcs:
                r['rel'] = srcs[0]
                n_rel_fix += 1

    for slug in sorted(set(pages) - have):
        fm = fm_of(pages[slug])
        srcs = fm.get('sources') or []
        backfill.append({
            'slug': slug,
            'type': fm.get('type', ''),
            'layer': fm.get('layer', ''),
            'stage': fm.get('stage', ''),
            'rel': srcs[0] if srcs else '',
            'status': status_of(pages[slug]),
            'note': f'回填（页面先建；sources 共 {len(srcs)} 条，此处只记第一条）',
        })

    # **表头第一行，注释紧随其后，数据最后**——和原文件同一个布局（见 read_plan）。
    out = [','.join(COLS)] + comments
    for r in rows + backfill:
        out.append(','.join(_q(r.get(c, '')) for c in COLS))
    text = nl.join(out).rstrip(nl) + nl

    print(f'计划表原有：{len(rows)} 行')
    print(f'  status 改成 done 的：{n_done}')
    print(f'  status 改成 skeleton 的：{n_skel}')
    print(f'  status 改成 todo 的：{n_todo}')
    print(f'  补上空的 rel：{n_rel_fix}')
    print(f'  从页面回填的新行：{len(backfill)}'
          f'{"（" + "、".join(b["slug"] for b in backfill[:6]) + " …）" if backfill else ""}')
    if write:
        # **`newline=''` 是必须的**：默认值会把 `\n` 翻译成 `os.linesep`，
        # 而我们自己已经把行尾拼好了（见 read_plan）。不关掉就是 `\r\r\n`。
        PLAN.write_text(text, encoding='utf-8', newline='')
        # **写完自己再读一遍**：这个脚本刚刚在行尾上栽过一次
        # （`\r\r\n`，而且是自喂自的、修不回来的那种）。行尾这种事**看不出来**，
        # 所以不许靠「我这次改对了」——断言它。
        back = PLAN.read_bytes()
        stray = [i for i, l in enumerate(back.split(b'\n')) if l.endswith(b'\r')
                 and not l.endswith(b'\r\r')]  # 正常行：…内容 + \r，然后 \n
        double = back.count(b'\r\r\n')
        if double:
            raise SystemExit(f'❌ 写完发现 {double} 处 `\\r\\r\\n`——行尾翻译没关掉')
        print(f'✅ 已写入 {PLAN.name}（{len(rows) + len(backfill)} 行，'
              f'行尾 {"CRLF" if nl == chr(13) + chr(10) else "LF"}，无重复 CR）')
    else:
        print('（只看，没写。加 --write 才写。）')


def _q(s):
    """含逗号/引号的字段要引起来。`rel` 列是多篇 raw 用分号连的，正文里没有逗号；
    但 `note` 列有——**不引就会被 csv 拆成两列**。"""
    s = str(s)
    return f'"{s.replace(chr(34), chr(34) * 2)}"' if any(c in s for c in ',"') else s


if __name__ == '__main__':
    main()
