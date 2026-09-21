# -*- coding: utf-8 -*-
"""第十三类 · 版本页：**页面 == 脚本产出**，且**每条条目逐字回得到 raw**。

**为什么要有这一类**（2026-09-18，建完 142 个版本页的当天）：

版本页的页首自己声明了两件事：

1. 「**本页由 `extract/versions.py` 机械汇编，没有一句是模型写的**」
2. 「**条目原样转录**」

**这两句话此前一条检查都没有。** 第七类（引文逐字）只抠 `>` 引用块和代码块，
**而版本页的条目是普通列表项**——它们连第七类的门都进不去
（`_extract_quotes` 明确只收不含 CJK 的块，中文块是「页面自己的话」）。

于是出现了一个很别扭的局面：**本 wiki 里唯一一处「成规模声称逐字」的地方，
正好落在唯一一类检查之外。** 这是同一个病的第九次，形态和前面几次一样——
**检查比它自称的范围窄，而窄掉的那块是绿的。**

所以这一类查两件独立的事：

- **甲：页面 ↔ 脚本。** 拿 `versions.render()` 的当前输出和磁盘上的文件逐字比。
  不等就是**有人手改过**，或者**脚本改了但没重跑**。这条管「机械汇编」那句声明。
- **乙：条目 ↔ raw。** 把页面上每一条条目的文本**回 9,398 篇原文里找完全子串**
  （**不经过 `sections.jsonl`**，直接读 raw——否则抽取器错了，这一条跟着一起错，
  等于没查）。这条管「原样转录」那句声明。

**甲乙必须都有**：只有甲，脚本自己抽错了照样一路绿；只有乙，页面被手改过也看不出来。

用：`python check_version_fresh.py`（打印；返回对不上的条数，0 = 干净）
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
BASE = Path(r'F:\master-dev\understand-anything-wiki')
OUT = BASE / 'extract'
WIKI = BASE / 'wiki'
CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')

import versions as V          # 同目录；渲染逻辑**只有一份**，不在这里重写

# 页面上条目的形态：`- [标题](<rel>) —— 原文`
RE_ITEM = re.compile(r'^- \[.*?\]\(<(?P<rel>[^>]+)>\) —— (?P<text>.*)$')


def norm(s):
    """折叠空白。**只做这一件**——多做的每一点规范化，都是替被检对象打掩护。"""
    return re.sub(r'\s+', ' ', s).strip()


def raw_section(rel, cache):
    """raw 里那篇的 `## Functional changes` 段落原文（**截到脚注块**）。

    返回 `None` 表示该篇读不到或没有这一节——**那不是通过，是要报出来的**。
    """
    if rel in cache:
        return cache[rel]
    p = CORPUS / rel
    got = None
    if p.exists():
        lines = p.read_text(encoding='utf-8', errors='replace').splitlines()
        buf, on = [], False
        for ln in lines:
            if ln.startswith('## '):
                if on:                      # 下一个 H2，本段结束
                    break
                on = ln.strip().lower() == '## functional changes'
                continue
            if on:
                if V.FN_DEF.match(ln.strip()):   # 坑二：脚注块不算本节内容
                    break
                buf.append(ln)
        if on:
            got = '\n'.join(buf)
    cache[rel] = got
    return got


def main(quiet=False):
    facts, _, _ = V.load_facts()
    ttl = V.titles()
    VDIR = V.VDIR

    # ── 甲：页面 ↔ 脚本 ──
    grp = {}
    for r in facts:
        grp.setdefault((r['prod'], r['ver']), []).append(r)
    n_page = n_stale = 0
    stale_names = []
    for (prod, ver), items in grp.items():
        p = VDIR / f'{V.SLUG_OF[prod]}-{ver}.md'
        if not p.exists():
            stale_names.append((p.name, '页面不存在'))
            continue
        n_page += 1
        base = [r for r in items if r['kind'] == 'base']
        rest = [r for r in items if r['kind'] != 'base']
        _, want = V.render(prod, ver, rest, base, ttl)
        if p.read_text(encoding='utf-8') != want:
            n_stale += 1
            stale_names.append((p.name, '与脚本当前产出不一致'))

    # ── 甲之二：**目录页** ↔ 脚本 ──
    #
    # 目录页原来**一条检查都没有**：它不参与甲（甲按 `grp` 走 142 个 `(产品线, 版本)`，
    # 目录页不是其中之一），也不参与乙（乙按条目行匹配，目录页只有表格行）。
    # 于是它是**整批产出里唯一一处「机器写的、没人对」的正文**——
    # 而它恰恰是「这个功能哪一版才有」的入口页。
    #
    # 它也没有 `sources:`（机器汇编的清单，没有对应的 raw 文档），所以**格式检查也管不到它**：
    # §6 那条「`sources` 至少一条」对它是空的。**豁免必须配一条替换判据**，
    # 否则豁免就等于「没人管」。替换判据就是这一条：**与 `render_index()` 逐字节一致**。
    idx_p = VDIR / V.IDX_NAME
    idx_ok = idx_p.exists() and idx_p.read_text(encoding='utf-8') == V.render_index(facts)
    if not idx_ok:
        stale_names.append((V.IDX_NAME, '目录页与脚本当前产出不一致' if idx_p.exists()
                            else '目录页不存在'))
        n_stale += 1

    # ── 乙：条目 ↔ raw ──
    cache = {}
    n_item = n_bad = n_nodoc = 0
    bad = []
    for p in sorted(VDIR.glob('*.md')):
        body = p.read_text(encoding='utf-8')
        # frontmatter 不算正文——里面没有条目
        if body.startswith('---'):
            k = body.find('\n---', 3)
            if k > 0:
                body = body[k + 4:]
        for ln in body.splitlines():
            m = RE_ITEM.match(ln)
            if not m:
                continue
            n_item += 1
            rel, text = m.group('rel'), norm(m.group('text'))
            sec = raw_section(rel, cache)
            if sec is None:
                n_nodoc += 1
                if len(bad) < 20:
                    bad.append((p.name, rel, '**raw 里找不到 `## Functional changes` 段落**'))
                continue
            if text not in norm(sec):
                n_bad += 1
                if len(bad) < 20:
                    bad.append((p.name, rel, text[:100]))

    lines = [f'{n} — {why}' for n, why in stale_names]
    lines += [f'{a} ← {b}｜{c}' for a, b, c in bad]
    info = {'n_page': n_page, 'n_stale': n_stale, 'n_item': n_item,
            'n_bad': n_bad, 'n_nodoc': n_nodoc, 'lines': lines}
    total = n_stale + n_bad + n_nodoc
    if not quiet:
        print(f'甲·页面 ↔ 脚本：{n_page} 个版本页 + 目录页，'
              f'**与脚本产出不一致的 {n_stale} 个**')
        for n, why in stale_names[:10]:
            print(f'    ❌ {n} — {why}')
        print(f'乙·条目 ↔ raw：{n_item:,} 条条目，**逐字对不上的 {n_bad} 条**，'
              f'**出处段落读不到的 {n_nodoc} 条**')
        for a, b, c in bad:
            print(f'    ❌ {a}  ←  {b}\n         {c}')
        if not total:
            print(f'✅ {n_page} 个版本页**没有一个字偏离脚本产出**，'
                  f'**{n_item:,} 条条目全部逐字回得到 raw**。')
            print('   ——这只证明「转录忠实」，**不证明「分对了组」**：'
                  '把某条记到错的版本上，这一条一样是绿的。')
    return total, info


if __name__ == '__main__':
    sys.exit(1 if main()[0] else 0)
