# -*- coding: utf-8 -*-
"""给已建页的语法节**补上 begin / end 标记**。

为什么要补：`refresh()` 的边界判据换过三次，第三次才定成「认标记」。
已经建好的页面里没有标记，**下次刷新就会退回兜底判据**——
而兜底判据正是删掉 `cct` 六节的那把刀。**补标记就是拆这把刀。**

**判据是自证的，不靠猜**：把「页面现有的语法节」和「抽取器现在的产出」
（都去掉标记行后）比字符串——

- 在候选边界 `c1`（下一个任意 `## `）、`c2`（下一个页面级小节）里，
  **哪个让两边相等，哪个就是真边界**；
- **两个都不等就跳过并报出来**，不动那一页。

`device-architecture-file` 这种「语法节里嵌着十几个 H2」的页面，
`c1` 会落在表格中间因而对不上，只有 `c2` 对得上——**自证在这里就是必需的**，
不是保险。
"""
import csv
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, str(Path(__file__).parent))
import objscaffold as os_

MARKS = (os_.MARK_BEGIN, os_.MARK_END)


def norm(s):
    """去掉标记行、把连续空行压成一行、去掉首尾空白。

    **为什么要压空行**：`syntax_block` 里标记是 `[HEAD, '', MARK_BEGIN, '', …]`——
    抽掉标记行后会**多出一个空行**，于是「有标记的块」和「没标记的页面」
    逐行比永远差一行。第一版就栽在这儿：**12 页全部自证失败**，
    看上去像「没有一页边界对得上」，实际是**比较器自己偏了一行**。
    """
    keep = [ln for ln in s.splitlines() if ln.strip() not in MARKS]
    out = []
    for ln in keep:
        if not ln.strip() and out and not out[-1].strip():
            continue
        out.append(ln)
    return '\n'.join(out).strip()


def main(apply=False):
    rows = [r for r in csv.DictReader(l for l in os_.PLAN.open(encoding='utf-8')
                                      if not l.startswith('#')) if r['slug']]
    done = skipped = already = 0
    for r in rows:
        p = os_.WIKI / os_.DIRS[r['type']] / f"{r['slug']}.md"
        if not p.exists():
            continue
        text = p.read_text(encoding='utf-8')
        i = text.find(os_.HEAD)
        if i < 0:
            print(f'⏭  {r["slug"]}：没有 `{os_.HEAD}`（非脚本建页）')
            continue
        if os_.MARK_END in text[i:os_.section_end(text, i)]:
            already += 1
            continue
        block = os_.syntax_block(r['rel'])
        cands = []
        k = text.find('\n## ', i + 1)
        if k > 0:
            cands.append(('下一个任意 H2', k + 1))
        cands.append(('下一个页面级小节', os_.section_end(text, i)))
        hit = sorted([(c, n) for n, c in cands if norm(text[i:c]) == norm(block)])
        if not hit:
            skipped += 1
            print(f'❌ {r["slug"]}：没有候选边界自证成功——{cands}。**不动这一页。**')
            continue
        # 两个候选常常是**同一条边界**（一个指 `\n`、一个指 `## `，差 1 个字符），
        # 都会自证成功。**取小的那个**：它让下一节前面保留一个空行。
        # 第一版要求「恰好 1 个自证」→ 10 页被判成「边界有歧义」，实际是**判据太严**。
        c, name = hit[0]
        new = text[:i] + block + ('' if text[c:].startswith('\n') else '\n') + text[c:]
        status = '✅' if apply else '·'
        print(f'{status} {r["slug"]}：边界＝{name}，'
              f'{len(text):,} → {len(new):,} 字符（+{len(new) - len(text)}，标记行）')
        if apply:
            p.write_text(new, encoding='utf-8')
        done += 1
    print(f'\n补标记 {done} 页，已有标记 {already} 页，跳过 {skipped} 页'
          + ('' if apply else '  ——**这是预演，没有写盘**（加 --apply 才写）'))


if __name__ == '__main__':
    main(apply='--apply' in sys.argv)
