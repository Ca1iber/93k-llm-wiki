# -*- coding: utf-8 -*-
"""给 `wiki/` 做一个**能回滚的快照**。

**为什么写它（2026-09-18，拿一次真实事故换的）**：

这一天 `objscaffold.refresh()` 的边界判据写错，**把
`cct-multiport-sequencer-synchronizer-api` 的六个小节整段删掉**，
页面 5,609 → 3,958 字符。**能捞回来纯属运气**——
我在同一会话里 Edit 过那一页，transcript 里留着完整原文
（`.toolUseResult.originalFile`，两处独立捕获逐字节相同）。

**换句话说：这次靠的是「我恰好读过那个文件」。**
如果被删的是一小时前建的页、或者这一批建完就换了会话，
**那些散文没有第二份副本，也就没有了。**

`wiki/` 那时不是 git 仓库（**2026-09-21 起是了**），`F:\\master-dev` 也不是。所以：

- **不做增量、不做历史压缩**——那是 git 的活，这里只做**能回滚的快照**；
- 一次运行 = 一个带时间戳的目录 + `manifest.csv`（每页字节数与 `sha256`）；
- **内容与上一份快照完全相同时不写新目录**（否则每次跑都堆一份，等于没有）；
- 恢复是**一条命令**：`python snapshot.py --restore <目录名>`，
  它会**先**把当前 `wiki/` 存成 `pre-restore-<时间>`，再覆盖——**回滚本身也可回滚**。

用：`python snapshot.py`（存快照）
    `python snapshot.py --list`（列出所有快照与规模）
    `python snapshot.py --restore <名字>`（回滚；先自动存现场）
"""
import csv
import hashlib
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
BASE = Path(r'F:\master-dev\understand-anything-wiki')
WIKI = BASE / 'wiki'
SNAPS = BASE / 'snapshots'

# **`wiki/` 之外、同样是人手写的东西。**
#
# 为什么加这一条（2026-09-18）：快照原本只收 `WIKI.rglob('*.md')`，
# 而 `schema.md` **在仓库根、不在 `wiki/` 里**——也就是说
# **这份 wiki 里唯一一份「规则书」从来没被快照过**。
# 那时**本目录不是 git 仓库**（2026-09-21 才建），所以它此前**一个字节的兜底都没有**；
# 而它恰恰是「丢了最贵」的那一个：wiki 的每一页都要按它判对错。
#
# 用 `@root/` 命名空间而不是相对路径（`../schema.md`）——**恢复时要能算回绝对位置**，
# 而 `..` 在不同 `cwd` 下算出来的东西不一样。**边界必须由写它的人钉死。**
#
# **2026-09-18 补**：`purpose.md` 也是人手写在根上的，同一类，**也从来没被兜底过**。
ROOT_FILES = ['schema.md', 'purpose.md']

# **`extract/` 下的脚本也收**：那时本目录无版本控制，**改坏了脚本一样捞不回来**。
# 这条从建快照那天起就挂在 log「仍待决」里，今天补上——因为本批一次改了三个脚本
# （`versions.py` / `verify_stages.py` / `check_version_fresh.py`），
# **而它们一个字节的兜底都没有。**
#
# **只收 `.py`，不收同目录的产出**（`*.jsonl` / `*.csv` / `*-report.md`）：
# 那些是**再生得出来的**，而且体积大（`verify_stages.py` 一个 78 KB）；
# 更要紧的是——**「用旧快照的产出配新快照的页面」只会制造不一致**。
# **代码要能回滚，数据要能重算。**
SCRIPT_GLOB = 'extract/*.py'
NS = '@root/'


def _rel_of(p):
    """仓库内文件 → 清单里的 `rel`。**只认这两个位置，别的路径直接报错。**

    **分隔符统一成 `/`**：Windows 的 `relative_to` 给的是 `objects\\mtpt.md`，
    而 `_path_of` 是按 `/` 切前缀的——两边不一致时**恢复会把文件放到一个叫
    `objects\\mtpt.md` 的怪名字下**，而清单上看着完全正常。
    """
    try:
        return str(p.relative_to(WIKI)).replace('\\', '/')
    except ValueError:
        pass
    if p.parent == BASE and p.name in ROOT_FILES:
        return NS + p.name
    if p.parent == BASE / 'extract' and p.suffix == '.py':
        return NS + f'extract/{p.name}'
    raise SystemExit(f'❌ 不在快照范围内：{p}')


def _path_of(rel):
    """清单里的 `rel` → 仓库内绝对路径。`_rel_of` 的逆。"""
    return BASE / rel[len(NS):] if rel.startswith(NS) else WIKI / rel


def _covered():
    """**快照该收哪些文件**——`collect()` 和「范围自检」共用同一份。

    **两边口径必须同源**：`collect()` 收了什么，自检就得检查什么。
    （本项目在 `_other_pages()` 上栽过一次：两处口径不同却共用一个函数，
     于是两个检查只能有一个数。）
    """
    out = list(WIKI.rglob('*.md'))
    out += [BASE / n for n in ROOT_FILES]
    out += list(BASE.glob(SCRIPT_GLOB))
    return sorted(out)


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def collect():
    """`{相对路径: (字节数, sha256)}`，按路径排序——**排序保证指纹可比**。"""
    out = {}
    for p in _covered():
        if p.exists():
            out[_rel_of(p)] = (p.stat().st_size, digest(p))
    return out


def fingerprint(files):
    h = hashlib.sha256()
    for rel, (n, d) in sorted(files.items()):
        h.update(f'{rel}\t{n}\t{d}\n'.encode())
    return h.hexdigest()[:12]


def last_manifest():
    if not SNAPS.exists():
        return None
    for d in sorted([x for x in SNAPS.iterdir() if x.is_dir()], reverse=True):
        m = d / 'manifest.csv'
        if m.exists():
            return d
    return None


def save(quiet=False):
    """存一份快照，返回新目录名；与上一份逐字节相同时返回 `None`。

    `quiet=True` 时只返回名字不打印——给 `objscaffold.refresh()` 这类
    **写页面的脚本**用的：**它们写之前先自己存一份**，
    免得再出现「删掉了才发现没兜底」。见下方 `__main__`。
    """
    files = collect()
    fp = fingerprint(files)
    prev = last_manifest()
    if prev:
        with (prev / 'manifest.csv').open(encoding='utf-8', newline='') as f:
            rows = list(csv.DictReader(l for l in f if not l.startswith('#')))
        old = {r['rel']: (int(r['bytes']), r['sha256']) for r in rows}
        if old == files:
            if not quiet:
                print(f'＝ 与上一份快照逐字节相同（`{prev.name}`，指纹 {fp}）——**不写新目录**')
            return None
    name = 'wiki-' + datetime.now().strftime('%Y-%m-%d-%H%M%S')
    d = SNAPS / name
    d.mkdir(parents=True, exist_ok=True)
    with (d / 'manifest.csv').open('w', encoding='utf-8', newline='') as f:
        f.write('# 快照清单。**由 extract/snapshot.py 写，不许手改。**\n')
        f.write(f'# 指纹 sha256[:12] = {fp}\n')
        wr = csv.writer(f)
        wr.writerow(['rel', 'bytes', 'sha256'])
        for rel, (n, sg) in sorted(files.items()):
            wr.writerow([rel, n, sg])
    for rel in files:
        dst = d / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(_path_of(rel), dst)
    tot = sum(n for n, _ in files.values())
    if quiet:
        return name
    print(f'✅ 快照 `{name}`：{len(files)} 个文件 / {tot:,} 字节，指纹 **{fp}**')
    if prev:
        with (prev / 'manifest.csv').open(encoding='utf-8', newline='') as f:
            old = {r['rel']: r['sha256']
                   for r in csv.DictReader(l for l in f if not l.startswith('#'))}
        ch = [r for r in files if old.get(r) != files[r][1]]
        # ⚠️ **这一行只报「改过的」，不报「删掉的」**（2026-09-21 发现）：
        # 删文件时**文件总数会变**（上一行印的那个数），但这一行的清单里**看不见它**——
        # 于是「比上一份哪些没了」在报告里**没有出口**。
        # **没修它，只记下**：改这个回滚工具本身要单独一轮，而它现在能用。
        # 要看删了什么，比两份快照的文件清单（本项目 §13.1 那个形状的第 N 次）。
        print(f'   相对上一份（`{prev.name}`）改动 {len(ch)} 个：'
              + '、'.join(ch[:6]) + ('…' if len(ch) > 6 else ''))
    return name


def restore(name):
    src = SNAPS / name
    if not src.is_dir():
        raise SystemExit(f'❌ 没有这个快照：{name}（用 --list 看有哪些）')
    live = collect()
    print(f'恢复前先把现场存成 pre-restore：{len(live)} 个文件')
    name_now = 'pre-restore-' + datetime.now().strftime('%Y-%m-%d-%H%M%S')
    d = SNAPS / name_now
    d.mkdir(parents=True, exist_ok=True)
    for rel in live:
        dst = d / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(_path_of(rel), dst)
    # **按清单恢复，不按 `rglob('*.md')`。**
    #
    # 这里原来是 `for p in sorted(src.rglob('*.md'))`——**只认 `.md`**。
    # 于是任何非 `.md` 的文件都会**存进快照、却永远恢复不出来**：
    # 清单上列着、目录里躺着、`--restore` 当它不存在。**一个只存不还的快照，
    # 比没有快照更坏**——它会让人以为有兜底。
    # 今天之前快照里恰好全是 `.md`，所以这个洞**是潜伏的**；
    # 2026-09-18 把 `extract/*.py` 纳进来，**它就立刻是活的**。
    # 清单是快照自己写的，**恢复就该读它自己那份账**。
    with (src / 'manifest.csv').open(encoding='utf-8') as f:
        kept = {r['rel'] for r in csv.DictReader(l for l in f if not l.startswith('#'))}
    n = 0
    for rel in sorted(kept):
        p = src / rel
        if not p.exists():
            raise SystemExit(f'❌ 清单里有、快照里没有：`{rel}`——**这份快照坏了**')
        dst = _path_of(rel)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst)
        n += 1
    extra = sorted(set(live) - kept)
    print(f'✅ 已从 `{name}` 恢复 {n} 个文件。现场存于 `{name_now}`——'
          f'**回滚本身也可回滚。**')
    if extra:
        print(f'⚠️ 快照之后新建、本次**没删**的 {len(extra)} 个：'
              + '、'.join(extra[:8]) + ('…' if len(extra) > 8 else ''))
        print('   ——要一起回退请手工删（**脚本不替你决定删文件**）。')


def listing():
    if not SNAPS.exists():
        print('还没有任何快照。')
        return
    for d in sorted([x for x in SNAPS.iterdir() if x.is_dir()]):
        m = d / 'manifest.csv'
        if not m.exists():
            print(f'  {d.name}  （无清单）')
            continue
        with m.open(encoding='utf-8') as f:
            head = [l for l in f if l.startswith('#')]
            rows = list(csv.DictReader(l for l in m.open(encoding='utf-8')
                                       if not l.startswith('#')))
        fp = next((l.split('=')[-1].strip() for l in head if '指纹' in l), '?')
        print(f'  {d.name}  {len(rows)} 个文件 / '
              f'{sum(int(r["bytes"]) for r in rows):,} 字节  指纹 {fp}')


if __name__ == '__main__':
    if '--list' in sys.argv:
        listing()
    elif '--restore' in sys.argv:
        k = sys.argv.index('--restore')
        if k + 1 >= len(sys.argv):
            raise SystemExit('用：python snapshot.py --restore <快照目录名>')
        restore(sys.argv[k + 1])
    else:
        save()
