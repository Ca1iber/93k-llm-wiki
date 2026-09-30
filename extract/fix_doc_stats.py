# -*- coding: utf-8 -*-
"""按 `check_doc_stats.py` 查出的差，**逐条精确替换**页面里的「N 字节，M 行」。

**为什么用脚本而不是手改。** 十七条改的是同一个东西（同一个抄错的口径），
手改会漏、会顺手改到别处；**脚本改法可复核**（§4：脚本能产出的，不许调 LLM）。

**改什么、不改什么**：

| 情况 | 做法 |
|---|---|
| 字节 = `st_size − 行数`（CR 归一），页面没写这个口径 | **改成 `st_size`**——全库 65 处都用它，这 3 处是例外 |
| 行数 = `wc -l` + 1 / + 2 | **改成 `wc -l`**——这批 9,398 篇**末行都带换行**，`+1` 恒错 |
| 字节 = 剥 frontmatter 后（**页面标注了**） | **不动**——口径写明了就不是错 |
| 字节 = 上游 `.htm` 的大小 | **不动**——量的是另一个文件，本来就该不一样 |

**不许碰生成块**：`objscaffold.py` 生成的语法节 / 报错节夹在 `begin` / `end` 标记之间，
手改会在下次 `--refresh` 时消失。所以命中位置落在标记里就**拒绝改并报错**。

用：`python -X utf8 extract/fix_doc_stats.py`        # 只报要改什么
    `python -X utf8 extract/fix_doc_stats.py --write`
"""
import re
import sys
from pathlib import Path

BASE = Path(r'F:\master-dev\understand-anything-wiki')
sys.path.insert(0, str(BASE / 'extract'))
import check_doc_stats as C  # noqa: E402

GEN = re.compile(r'<!--[^>]*\b(begin|end)\b[^>]*-->')


def in_generated(text, pos):
    """`pos` 是否落在 `objscaffold.py` 的生成块里。**只认 `begin`/`end` 配对**。"""
    depth = 0
    for m in GEN.finditer(text):
        if m.start() > pos:
            break
        depth = depth + 1 if m.group(1) == 'begin' else 0
    return depth > 0


def plan():
    """→ `[(页面, 原文命中, 改后, 理由, 偏移)]`。

    **判据全部向 `check_doc_stats` 借，这里一句都不重写。**
    第一版这里自己抄了一份 `CLAIM` 的分组编号，检查器那边一放宽就当场崩
    （`group(2)` 从「字节」变成「字节或空」）——
    **同一个判据写两遍，就是等着它们不一样**（同 `unowned.py` 那条）。
    """
    rows, _missing, _dup, _cov, _scan = C.scan()
    out = []
    for r in rows:
        b, n, nl = r['b_claim'], r['n_claim'], r['wc']
        var = r['var']
        nb, nn = b, n
        why = []
        if b is not None and b != var['st_size'] and b != var.get('剥掉 frontmatter 后'):
            # ★ **2026-09-30 改**：原来只在 `b == var['st_size − 行数（CR 归一）']`
            # 时才动手，**别的不符一律静默跳过**。
            # 修语料（坏字改短了字符）之后页面有 14 处字节数过期，
            # 而 `plan()` 报「**要改 0 处**」—— 同时 `check_doc_stats` 那边红着 14 条。
            # **两个数打架，看的人只能当没看见。**
            # 现在：**剩下的任何不符，都改成文件实际大小**（`check_doc_stats` 对它们
            # 报的就是「哪个口径都对不上」，改成正字是唯一诚实的处置）。
            nb = var['st_size']
            why.append(f'字节 {b:,}→{nb:,}（改成文件实际大小 st_size）')
        if n is not None and n != nl:
            nn = nl
            why.append(f'行数 {n}→{nn}（wc -l）')
        if why:
            old = r['hit_raw']          # **原样那份**，不是归一过的 `hit`
            new = old
            if nb != b:
                new = new.replace(f'{b:,} 字节', f'{nb:,} 字节')
            if nn != n:
                new = new.replace(f'{n} 行', f'{nn} 行')
            out.append((C.BASE / r['page'], old, new, '；'.join(why), 0))
    return out


def main(write=False):
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    rows = plan()
    print(f'要改 **{len(rows)}** 处。')
    bad = 0
    for page, old, new, why, pos in rows:
        text = page.read_text(encoding='utf-8')
        k = text.count(old)
        rel = page.relative_to(BASE).as_posix()
        if k != 1:
            print(f'  ❌ {rel}：命中原文出现 {k} 次，**不敢改**：`{old}`')
            bad += 1
            continue
        if in_generated(text, text.index(old)):
            print(f'  ❌ {rel}：命中落在 `objscaffold.py` 的生成块里，**拒绝改**：`{old}`')
            bad += 1
            continue
        print(f'  {"✍️ " if write else "→ "}{rel}')
        print(f'      `{old}`  →  `{new}`')
        print(f'      理由：{why}')
        if write:
            page.write_text(text.replace(old, new, 1), encoding='utf-8')
    if bad:
        print(f'\n**{bad} 处没改**——有不能安全替换的，先看它们。')
    elif write:
        print('\n改完。**跑 `check_doc_stats.py` 复核**，别自己声称改好了。')
    return 1 if bad else 0


if __name__ == '__main__':
    raise SystemExit(main(write='--write' in sys.argv))
