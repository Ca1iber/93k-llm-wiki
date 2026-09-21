"""合并两张工作单 → `extract/build-next.csv`（**下一批建什么**）。

**为什么要有这个脚本。** 欠着的页有两个来源，两份清单各说各的、从没合过：

| 来源 | 是什么 | 谁产的 | 规模 |
|---|---|---|---|
| **A · `stage-map.csv` 的 `prose` 行** | 语料里出现 ≥20 次、九页的正文**提过它却没链它**、也没有页 | 第六类 | 47 个对象（in_src≥20） |
| **B · `dangling.csv` 的 `refs≥3` 行** | **已建页伸手要、但页还没有** | 第八类 | 31 个目标 |

两张单子**问的不是同一个问题**（A 问「语料反复讲它」，B 问「页面缺了它就断」），
所以**合起来才是「下一批建什么」**。合的时候按 §5 的 slug 归一——
**A 给的是人写的标题、B 给的是 slug，不归一就会把同一个对象算成两个。**

**这个脚本只做机械部分**（§4）：合并、去重、排除已建、排序、印数。
**`类型/layer` 两列留空**——那是人的判断（§2 / §6），脚本不许替它猜；
`stage` 和 `rel` 从 `stage-map.csv` 带过来（那里已经是判过的）。

用：`python -X utf8 extract/build_next.py`
**它不改任何页面**，只写 `build-next.csv` 和一份 `build-next.md`（给人看的）。
"""
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

OUT = Path(r'F:\master-dev\understand-anything-wiki\extract')
WIKI = Path(r'F:\master-dev\understand-anything-wiki\wiki')

# 建页门槛。**两个都要能调**，不然「还欠多少」这个问题没法重新问。
A_MIN_IN_SRC = 20      # A 单：语料里出现次数
B_MIN_REFS = 3         # B 单：被已建页引用的次数（长尾是 1 次，不建）


def slugify(title):
    """人写的标题 → §5 的 slug。**这是机械近似，不是判据**。

    §5 说 slug 用「命令/API 的本名」或「描述性名词短语」——
    「本名」这件事脚本认不出来（`XPS256` 该留数字、`get...()` 该丢掉括号）。
    所以这里只做**能确定的那几步**：小写、非字母数字换连字符、去首尾、压重复。
    **凡是它产出的 slug 和已建页撞名，就在表里标出来给人看**，不自动加限定词。
    """
    s = title.strip().lower()
    s = s.replace('&', ' and ')
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return re.sub(r'-{2,}', '-', s).strip('-')


def read_csv(p):
    with p.open(encoding='utf-8') as f:
        return [r for r in csv.reader(f)
                if r and r[0] and not r[0].startswith('#')]


def load_docs():
    """读 `docs.jsonl`，给每篇算两个可用于查 slug 的键。

    **为什么不猜**：B 单只给了 slug（`dfpn`、`report-window`），
    **没给「哪篇 raw 定义它」**——而 `rel` 是 `objscaffold.py` 抽语法节的输入，猜错就是错页。
    所以这里只做**字符串匹配**，并把「匹配到 0 篇」「匹配到一堆」的都**留空交给人**：
    **留空看得见，猜错看不见。**
    """
    docs = []
    for line in (OUT / 'docs.jsonl').open(encoding='utf-8'):
        d = json.loads(line)
        fm = d.get('frontmatter') or {}
        title = (fm.get('title') or '').strip()
        # 命令参考的标题形如 `PSFC, PSFC? - (Parallel Setup FoCus)`——
        # **逗号前那一段就是命令本名**，这是 `02.06` 自己的排版习惯。
        lead = re.split(r'[,(\-–]', title)[0].strip() if title else ''
        fn = d['rel'].rsplit('/', 1)[-1]
        fn = re.sub(r'^[\d.]+_', '', fn[:-3])          # 去掉 `02.06.02.02.191_` 和 `.md`
        docs.append({'rel': d['rel'], 'title': title,
                     'lead_slug': slugify(lead),
                     'fn_slug': slugify(fn),
                     'cmd_ref': '/02.06_Command_Reference/' in d['rel']})
    return docs


def resolve_rel(slug, docs):
    """slug → 定义它的 raw。**命中就返回，含糊就返回空。**

    **同一个命令在语料里有多份**（`CTXT` 三份、`DSCP` 五份、`PALS` 三份），
    实测过：**大小差 1–2 字节、md5 各不相同**——不是同一份文件被抄了两遍，
    是**同一篇内容在不同章节下重复投放**（§10 说的那个现象，
    只是发生在 `02.06` 内部，不是 `source_topic` 层面）。
    **哪一份算「定义」有唯一答案：`02.06.02.02`。**
    那一层是**固件命令字典**（367 篇，`02.06.02.01` 就叫
    `Syntax_of_the_firmware_commands`），其余是各章「本章用到的命令」的转载。
    其余依次是 `02.06.03.02`（56 篇）、`02.06.06.02`、`02.06.10.02`、`03.xx` 用例章。
    """
    hits = [d for d in docs if d['lead_slug'] == slug or d['fn_slug'] == slug]
    if not hits:
        pre = [d for d in docs if d['fn_slug'].startswith(slug + '-')]
        return ('', len(pre)) if len(pre) != 1 else (pre[0]['rel'], 1)
    canon = [h for h in hits if '/02.06_Command_Reference/02.06.02.02.' in h['rel']]
    if len(canon) == 1:
        return canon[0]['rel'], len(hits)
    if len(hits) == 1:
        return hits[0]['rel'], 1
    return '', len(hits)


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    built = {p.stem for p in WIKI.rglob('*.md')}
    plan = read_csv(OUT / 'wiki-plan.csv')
    plan_slugs = {r[0] for r in plan[1:]}

    # ---- A 单：散文里反复出现、却既没链也没页 ----
    a_rows = [r for r in csv.DictReader(
        (OUT / 'stage-map.csv').open(encoding='utf-8')) if r['strength'] == 'prose']
    a = defaultdict(lambda: {'in_src': 0, 'stages': set(), 'rel': '', 'title': ''})
    for r in a_rows:
        k = slugify(r['object_title'])
        e = a[k]
        e['title'] = r['object_title']
        e['in_src'] = max(e['in_src'], int(r['in_src']))
        e['stages'].add(r['stage'])
        # 多行同 slug 时，rel 取**出现次数最高那一行**的（下面排序后覆盖）
        if not e['rel'] or int(r['in_src']) >= e['in_src']:
            e['rel'] = r['object_rel']

    # ---- B 单：悬空目标 ----
    b = {}
    for r in read_csv(OUT / 'dangling.csv')[1:]:
        if len(r) < 2 or not r[1].isdigit():
            continue
        if int(r[1]) >= B_MIN_REFS:
            b[r[0]] = {'refs': int(r[1]), 'stages': set(r[2].split('/')) if len(r) > 2 else set()}

    merged = {}
    for k, e in a.items():
        if e['in_src'] >= A_MIN_IN_SRC:
            merged[k] = {'slug': k, 'title': e['title'], 'in_src': e['in_src'],
                         'refs': b.get(k, {}).get('refs', 0),
                         'stages': sorted(e['stages'] | b.get(k, {}).get('stages', set())),
                         'rel': e['rel'], 'src': 'A' + ('+B' if k in b else '')}
    for k, e in b.items():
        if k not in merged:
            merged[k] = {'slug': k, 'title': '', 'in_src': 0, 'refs': e['refs'],
                         'stages': sorted(e['stages']), 'rel': '', 'src': 'B'}

    # ---- B 单的 `rel`：**机械查，查不到就留空**（见 resolve_rel 的说明）----
    docs = load_docs()
    n_rel, unresolved = 0, []
    for k, e in merged.items():
        if e['rel']:
            continue
        rel, n_hit = resolve_rel(k, docs)
        if rel:
            e['rel'], n_rel = rel, n_rel + 1
        else:
            unresolved.append((k, n_hit))

    # ---- 排除已建 / 已在计划里 ----
    rows, skipped = [], []
    for k, e in merged.items():
        if k in built:
            skipped.append((k, '已建页'))
        elif k in plan_slugs:
            skipped.append((k, '已在 wiki-plan.csv'))
        else:
            rows.append(e)

    # 排序：**先按「流程页缺了它就断」（refs），再按语料热度（in_src）**。
    # 这是刻意的：A 单只说「文档反复讲」，B 单说「已建页伸手要它」——
    # **后者是断链，前者只是没链**，断链更急。
    rows.sort(key=lambda e: (-e['refs'], -e['in_src'], e['slug']))

    with (OUT / 'build-next.csv').open('w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['slug', 'type', 'layer', 'stage', 'rel', 'in_src', 'refs',
                     '来源', '候选名（人写的标题，供核对 slug）'])
        for e in rows:
            wr.writerow([e['slug'], '', '', '/'.join(e['stages']), e['rel'],
                         e['in_src'], e['refs'], e['src'], e['title']])

    both = [e for e in rows if e['src'] == 'A+B']
    print(f'A 单（语料 in_src≥{A_MIN_IN_SRC} 的 prose 行）去重后：'
          f'{len({k for k, e in a.items() if e["in_src"] >= A_MIN_IN_SRC})} 个')
    print(f'B 单（悬空目标 refs≥{B_MIN_REFS}）去重后：{len(b)} 个')
    print(f'**两张单子的交集：{len(both)} 个**'
          f'{"（" + "、".join(e["slug"] for e in both[:8]) + "…）" if both else ""}')
    print(f'排除：已建页 {sum(1 for _, w in skipped if w == "已建页")} 个、'
          f'已在计划里 {sum(1 for _, w in skipped if w != "已建页")} 个')
    print(f'✅ 下一批待建：**{len(rows)} 个** → extract/build-next.csv')
    print(f'   其中 B 单来的（断链，最急）：{sum(1 for e in rows if "B" in e["src"])} 个')
    print(f'   只在 A 单的（语料反复讲，没链也没页）：{sum(1 for e in rows if e["src"] == "A")} 个')
    print(f'   `rel` 机械查到的：{n_rel} 个；**留空待定的：{len(unresolved)} 个**'
          f'{"（" + "、".join(f"{k}×{n}" for k, n in unresolved[:10]) + "）" if unresolved else ""}')
    print('   （留空 = 脚本没查准，**不许它猜**；这些行要人打开语料定 `rel` 再建）')
    print()
    print('前 20（refs 优先）：')
    for e in rows[:20]:
        print(f'  {e["slug"]:<44} refs={e["refs"]:<3} in_src={e["in_src"]:<3} [{e["src"]}] '
              f'{"、".join(e["stages"])[:30]}')


if __name__ == '__main__':
    main()
