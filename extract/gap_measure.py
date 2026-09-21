# -*- coding: utf-8 -*-
"""量 `verbatim_sections` 那次修改的**真实**增量：老逻辑 vs 新逻辑，逐篇对差。

**第一版这个脚本量错了，记在这里当教训。**
它数的是「命中 `SEC_HEADS` 的 H2 底下所有 H3 子段」——**把本身就命中的 H3 也算进去了**
（`### Example 1: SmartRDI, pattern-based programming` 这种，`SEC_EXAMPLE_PREFIX`
本来就认它，老逻辑从来没漏过）。于是报出 **517 篇 / 964,713 字符**，
**是个虚高的数**。

**正确做法是别定义「该收多少」，直接把两版代码跑一遍做差。**
差多少就是多少，没有解释空间。
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, str(Path(__file__).parent))
import objpack as op

H23 = op.re.compile(r'^(#{2,3})\s+(.+?)\s*$')


def old_verbatim_sections(text):
    """修改**之前**的那版（逐字抄自旧的 `objpack.verbatim_sections`）。"""
    lines = text.splitlines()
    i = 0
    if lines and lines[0].strip() == '---':
        i = 1
        while i < len(lines) and lines[i].strip() != '---':
            i += 1
        i += 1
    cur, buf, out = None, [], []
    for ln in lines[i:]:
        m = H23.match(ln)
        if m:
            if cur:
                out.append((cur, '\n'.join(buf).strip()))
            name = m.group(2).strip()
            cur = (name if name.lower() in op.SEC_HEADS or op.SEC_EXAMPLE_PREFIX.match(name)
                   else None)
            buf = []
            continue
        if cur is not None:
            buf.append(ln)
    if cur:
        out.append((cur, '\n'.join(buf).strip()))
    return [(n, b) for n, b in out if b]


def total(secs):
    return sum(len(b) for _, b in secs)


def main():
    docs = op.load_docs()
    n_docs, added, lost, worst = 0, 0, 0, []
    for rel in sorted(docs):
        try:
            body = (op.CORPUS / rel).read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        a, b = total(old_verbatim_sections(body)), total(op.verbatim_sections(body))
        if a != b:
            n_docs += 1
            added += max(0, b - a)
            lost += max(0, a - b)
            worst.append((b - a, rel))
    worst.sort(reverse=True)
    print(f'有变化的文档：{n_docs} 篇 / {len(docs)} 篇')
    print(f'新增字符合计：{added:,}    减少字符合计：{lost:,}')
    print('\n增量最大的 10 篇：')
    for d, rel in worst[:10]:
        print(f'  {d:>+8,}  {rel.split("/")[-1][:64]}')
    print('\n减少的（应当为 0；不为 0 说明新逻辑漏了东西）：')
    for d, rel in [x for x in worst if x[0] < 0][:10]:
        print(f'  {d:>+8,}  {rel}')

    tgt = '02.09.01.14.01_How_to_use_the_test_suite_control_API.md'
    rel = next(r for r in docs if r.endswith(tgt))
    body = (op.CORPUS / rel).read_text(encoding='utf-8', errors='replace')
    print(f'\n本页那一篇：老 {total(old_verbatim_sections(body)):,} → '
          f'新 {total(op.verbatim_sections(body)):,}')
    print('  新收到的段名：', [n for n, _ in op.verbatim_sections(body)])


if __name__ == '__main__':
    main()
