#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""跟随改名修路径：`tdc-html/raw/` → `tdc-html/agent-html/`。

用法：无参空跑 / `--apply` / `--verify-only`

## 为什么

2026-10-09 用户把 `tdc-html/raw/` 改名成 `tdc-html/agent-html/`。
md 里有两处**写死了旧路径**，改完就指不到了：

1. **资源链接** `](<../../../../raw/100053.png>)` —— **6,459 处 / 2,583 篇**。
   目标文件在（`agent-html/` 里有 5,193 个 png），**是路径失效，不是内容丢失**。
2. **转录说明**里的 `tdc-html/raw/<topic>.htm` —— **500 篇**（第六、七批写下的那句）。

## 只改这两种形态，**不做全局替换**

`raw` 在语料里还出现在别处（`raw 层`、`raw 语料`、散文里的路径），
**全局把 `raw/` 换成 `agent-html/` 会咬坏它们**。所以只认两个精确形态：
`](<.../raw/文件>)` 与 `` `tdc-html/raw/文件.htm` ``，且**只换目录名、保留其余部分**。

## 判据

- 替换**不改变**链接里的其它任何字符（前导 `../` 的层数原样保留）
- 替换后**每篇的命中数不变**（不是删，是改）
- 行尾不变（本仓 CRLF）
- **重放**：把同一套确定性替换施加到 `git show HEAD:` 的基线上，必须与工作区**逐字节相同**
  （偏移不用记 —— 替换是确定性的、且不增删行，所以不需要清单里的偏移）
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, r'F:\master-dev\understand-anything-wiki\extract')
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import fix_corpus_tables as F

WIKI = F.WIKI
CORPUS = F.CORPUS
MD = F.MD
EVID = WIKI / 'extract' / 'findings-corpus-html-paths-evidence.md'
ASSIGN = WIKI / 'extract' / '_assign_html_paths.json'

APPLY = '--apply' in sys.argv

# ① 资源链接：](<../../../../raw/xxx.png>)  →  只换目录名，前导 ../ 层数不动
LINK = re.compile(r'\]\(<((?:\.\./)+)raw/([^>]+)>\)')
# ② 转录说明里的路径（第六、七批那句）
NOTE = re.compile(r'(`tdc-html/)raw/([A-Za-z0-9_.\-]+\.htm`)')


def rewrite(t):
    """确定性替换。返回 (新文本, 链接处数, 说明处数)。"""
    t2, n1 = LINK.subn(lambda m: f'](<{m.group(1)}agent-html/{m.group(2)}>)', t)
    t2, n2 = NOTE.subn(lambda m: f'{m.group(1)}agent-html/{m.group(2)}', t2)
    return t2, n1, n2


def main():
    if '--verify-only' in sys.argv:
        return verify_only()

    rows = []
    for p in sorted(MD.rglob('*.md')):
        t = p.read_bytes().decode('utf-8', 'replace')
        if '/raw/' not in t and 'tdc-html/raw/' not in t:
            continue
        t2, n1, n2 = rewrite(t)
        if t2 == t:
            continue
        assert t2.count('/agent-html/') - t.count('/agent-html/') == n1 + n2
        assert t2.count('\n') == t.count('\n'), p.name
        rows.append((p, n1, n2, t.count('\n') == t.count('\r\n')))

    n1 = sum(r[1] for r in rows)
    n2 = sum(r[2] for r in rows)
    print(f'要改 **{len(rows):,}** 篇：资源链接 {n1:,} 处、转录说明 {n2:,} 处')

    if not F.guard(EVID, len(rows), '证据表') or not F.guard(ASSIGN, len(rows), '清单'):
        print('   （什么都没写，语料也没动。）')
        sys.exit(2)

    with EVID.open('w', encoding='utf-8', newline='\n') as fh:
        fh.write('# 语料路径修复证据表 —— `tdc-html/raw/` → `tdc-html/agent-html/`\n\n')
        fh.write('2026-10-09 用户把语料里的 `raw/` 目录改名成 `agent-html/`。\n'
                 'md 里两处写死了旧路径，改完就指不到 —— **目标文件都在，是路径失效。**\n\n')
        fh.write('只认两个精确形态（**不做全局替换**，`raw` 在散文里还有别的意思）：\n'
                 '`](<.../raw/文件>)` 与 `` `tdc-html/raw/文件.htm` ``，**只换目录名**。\n\n')
        fh.write(f'共 **{len(rows):,}** 篇；资源链接 **{n1:,}** 处、转录说明 **{n2:,}** 处。\n\n')
        fh.write('| # | markdown | 资源链接 | 转录说明 |\n|---|---|---|---|\n')
        for i, (p, a, b, _) in enumerate(rows, 1):
            fh.write(f'| {i} | `{p.relative_to(MD).as_posix()}` | {a} | {b} |\n')
    print(f'证据表 → {EVID}')

    _m = [dict(md=p.relative_to(MD).as_posix(), links=a, notes=b,
               sha1_before=hashlib.sha1(p.read_bytes()).hexdigest()) for p, a, b, _ in rows]
    ASSIGN.write_text(json.dumps(_m, ensure_ascii=False, indent=0), encoding='utf-8')
    print(f'机器可读清单 → {ASSIGN}（{len(_m):,} 条）')

    if not APPLY:
        print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
        return

    for p, a, b, crlf in rows:
        t = p.read_bytes().decode('utf-8', 'replace')
        t2, m1, m2 = rewrite(t)
        assert (m1, m2) == (a, b), f'{p.name}: 命中数与空跑不一致'
        if crlf:
            assert t2.count('\n') == t2.count('\r\n'), f'{p.name}: 混入了裸 LF'
        p.write_bytes(t2.encode('utf-8'))
    print(f'\n[已改] {len(rows):,} 篇')

    bad = verify_only(quiet=True)
    if bad:
        print(f'⛔ 重放失败 {len(bad)} 篇，前 5：')
        for rel in bad[:5]:
            print('   ', rel)
        sys.exit(3)
    print(f'✅ 逐字节重放：{len(rows):,}/{len(rows):,} 篇一致')


def verify_only(quiet=False):
    """重放：把同一套替换施加到 `git show HEAD:` 的基线上，与工作区逐字节比。"""
    bad = []
    for p in sorted(MD.rglob('*.md')):
        t = p.read_bytes().decode('utf-8', 'replace')
        if '/raw/' not in t and 'tdc-html/raw/' not in t:
            continue
        if rewrite(t)[0] != t:
            continue                                   # 工作区里还有没改的 → 不在本批
        rel = p.relative_to(CORPUS).as_posix()
        r = subprocess.run(['git', '-C', str(CORPUS), 'show', f'HEAD:{rel}'],
                           capture_output=True)
        if r.returncode != 0:
            bad.append(rel)
            continue
        base = r.stdout.decode('utf-8', 'replace')
        cur = p.read_bytes().decode('utf-8', 'replace')
        if '\r\n' in cur and '\r\n' not in base:
            base = base.replace('\n', '\r\n')
        if rewrite(base)[0] != cur:
            bad.append(rel)
    if not quiet:
        print(f'✅ 逐字节重放：对 `git show HEAD:` 施加同一套替换，与工作区比对 —— '
              f'失败 {len(bad)} 篇')
    return bad


if __name__ == '__main__':
    main()
