# -*- coding: utf-8 -*-
"""未归属对象清单 —— 建 stage 之外 `object` 页的工作单。

**为什么单独一个脚本、还要断言**：

第一版我是在命令行里现算的，用的是**改口径之前**的 `stage-map.csv`，
算出 37 个；紧接着 `verify_stages.py` 改用去重表后报 **34** 个。
两个数都对不上，而它们本该是同一件事。

这类错在本项目里已经出过好几次（口径变了、另一个文件没跟着变）。
规矩是**每个差异都必须有归宿**——那就把归宿写进代码：
本脚本从 `stage-report.md` 里把报告数读出来，和自算的数**必须相等**，
不等就退出。**清单和报告永远是同一个数。**

**2026-09-18 改：这份清单不再靠「记得去跑」。**

它**曾经就是这么坏的**：`object` 页建完之后第六类转绿、报告说 0，
**而 `unowned.csv` 里还留着 26 行**——那 26 个里面每一个都已经有页了。
没人再跑 `unowned.py`，于是**一份全过期的清单躺在那儿，长得像工作单**。
（同一个病，这个仓库已经记过一次，见 `cat8_reachable` 里 `dangling.csv` 那段：
 **一份没人认领的工作单，会一直绿着骗人。**）

处置照 `dangling.csv` 那一份，**但多留一手**：

- `verify_stages.py` 写完报告之后**立刻调用** `refresh()`——
  **这次运行自己写清单**，「忘了跑」这个状态就不存在了。
- `refresh()` 仍是**另一套独立实现**：它从 `hubs-dedup.csv` + `stage-map.csv`
  **自己算**，再和 `stage-report.md` 里的数**必须相等**，不等就抛 `SystemExit`。
  ——**清单由产出报告的那次运行来写，但算它的代码是另一份**。
  两件事都要：前者防过期，后者防「报告算错了、清单跟着一起错」。

用：`python unowned.py`（单独跑也行，先跑 `verify_stages.py`）
    `refresh()`（`verify_stages.py` 内部调用）
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

OUT = Path(r'F:\master-dev\understand-anything-wiki\extract')


def refresh(quiet=False):
    """算未归属 → 与报告对账 → 写 `unowned.csv`。返回 `(个数, 按子树的字典)`。

    **对不上就抛 `SystemExit`，绝不出一份和报告不一致的清单。**
    （宁可不出清单，也不出一份对不上账的清单。）
    """
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    hub = list(csv.DictReader((OUT / 'hubs-dedup.csv').open(encoding='utf-8')))
    # ⚠️ 2026-09-20 改判据：**「归属」= 有页，不是「被提到」。**
    # 原来收 `object_rel` 的全部行——那里面既有已建页、也有只被点名的。
    # 于是「被点名但没页」的对象**不在这张单上**（`WSUS` 入度 93 就是这么漏的）。
    # 现在只认 `strength == 'page'` 那些行（`verify_stages.py` 写已建页时打的标）。
    owned = {r['object_rel'] for r in
             csv.DictReader((OUT / 'stage-map.csv').open(encoding='utf-8'))
             if r.get('strength') == 'page'}
    cand = [r for r in hub if r['rel'] and int(r['in_src']) >= 20]
    un = [r for r in cand if r['rel'] not in owned]

    # **已查明的误报也要在这条路径上生效**，否则「清单 1 ≠ 报告 0」当场断。
    # **定义只留一份**：从 `verify_stages` 借，**不在这里抄一遍**——
    # 抄一遍就会有一天两边不一样，而这两边恰好是被断言要求相等的。
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import verify_stages as _vs
    un, _hit, _dead = _vs.apply_no_page_exceptions(un)
    for _c, _nm, _pg, _why in _hit:
        print(f'⚪ 已查明误报，不计入清单：{_nm} → {_pg}')
    for _c, _nm, _pg, _why in _dead:
        print(f'❌ 例外失效（指名的页不在了）：{_nm} → {_pg}，**如实计回清单**')

    # 与报告对齐。报告是判断落地的地方，这份清单只是它的工作单形态。
    rep = (OUT / 'stage-report.md').read_text(encoding='utf-8')
    # 报告里的原话是 `❌ **一个字都没提，且没有页：33**`（数在粗体**里面**）。
    # 第一版写成 `一个字都没提：(\d+)` —— **数在粗体里**，所以匹配不到，
    # 脚本直接退出而不是算错数。改报告措辞（2026-09-18 加「且没有页」）时它又断了一次，
    # 两次都断得对：**宁可不出清单，也不出一份和报告不一致的清单。**
    m = re.search(r'还没有页的：\s*(\d+)\*\*', rep)
    if not m:
        raise SystemExit('stage-report.md 里找不到「一个字都没提」的数——'
                         '报告格式变了？先跑 verify_stages.py')
    n_rep = int(m.group(1))
    if not quiet:
        print(f'候选(in_src>=20, 去重) {len(cand)}；已归属 {len(cand) - len(un)}；'
              f'未归属 {len(un)}；报告说 {n_rep}')
    if len(un) != n_rep:
        raise SystemExit(
            f'❌ 清单 {len(un)} ≠ 报告 {n_rep}。**先查明再出清单**——'
            '多半是 stage-map.csv 比报告旧，重跑 verify_stages.py。')

    by_tree = defaultdict(list)
    for r in un:
        seg = r['rel'].split('/')
        by_tree['/'.join(seg[:2]) if seg[0].startswith('0') else seg[0]].append(r)

    with (OUT / 'unowned.csv').open('w', encoding='utf-8', newline='') as f:
        # **表头必须落在第 1 行**：`csv.DictReader` 拿第一行当字段名，
        # 注释写在表头**之前**会被当成字段名——`wiki-plan.csv` 栽过这一次。
        wr = csv.writer(f)
        wr.writerow(['subtree', 'in_src', 'title', 'rel'])
        for t in sorted(by_tree, key=lambda t: -max(int(r['in_src']) for r in by_tree[t])):
            for r in sorted(by_tree[t], key=lambda r: -int(r['in_src'])):
                wr.writerow([t, r['in_src'], r['title'], r['rel']])

    return len(un), by_tree


def main():
    n, by_tree = refresh()
    print(f'✅ 与报告一致，{n} 个 -> extract/unowned.csv')
    for t in sorted(by_tree, key=lambda t: -max(int(r['in_src']) for r in by_tree[t])):
        rs = by_tree[t]
        top = max(int(r['in_src']) for r in rs)
        print(f'   {t:56} {len(rs):2} 个，最高 in_src {top}')


if __name__ == '__main__':
    main()
