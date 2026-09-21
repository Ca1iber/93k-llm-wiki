"""语料坏字对照表 —— **从 raw 反解出来，不手写**（`schema.md` §11.2 ①）。

**为什么要有这张表。** 这批文档全是英文的，所以**正文里出现汉字 = 坏字**（1053 / 9398 篇）。
成因是一个固定的错误：文件的字节本来是 UTF-8，却被按 GBK（汉字两字节）读了。
既然是固定映射，就能**反着走回去**：把坏字 `encode('gbk')` 拿回原字节，再 `decode('utf-8')`。

**两处容易做错，本脚本各有一道锁：**

1. **三字节字符会吃掉后面那个 ASCII 字符。** 所以坏字常是「两个汉字 + 紧跟的一个字母」，
   而那个字母**属于坏字的一部分**（`‑b` → `鈥慴`）。只扫汉字的正则会把第三个字节切在外面，
   于是这一类全被误判成「反解不了」。**解法：把紧跟的那个字符一起拿进来解。**
2. **有的字节是真丢了**（`?` 是替换字符，不是原字节），这种**必须留在「反解不了」里**，
   不许猜。**解法：每条都过一遍来回验**——解出来的东西按 UTF-8 编回去、再按 GBK 读回来，
   必须一字不差地等于输入；不等就宁可放弃。

**这张表的用处**（不在本工程内，是给以后的检索层 / MCP 的）：
拿正确的字（`µ`、`±`、`µF`）去 raw 里搜是**搜不到**的，得搜坏掉的那个形态。
两边都查，命中率才回得来。**raw 一个字节不动。**

**只读 raw，不写 raw。** 产出 `extract/encoding-map.csv`。

用法：`python -X utf8 extract/encoding_map.py`
"""

import csv
import re
import collections
import pathlib

RAW = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')
OUT = pathlib.Path(__file__).with_name('encoding-map.csv')

CJK = re.compile(r'[\u4e00-\u9fff]+')


def _roundtrip(blob):
    """`坏字` → 原字符。**回来验不过就返回 None。**

    `blob` 是坏字段本身，或者「坏字段 + 紧跟的那个字符」（三字节字符的情形）。
    """
    try:
        real = blob.encode('gbk').decode('utf-8')
        back = real.encode('utf-8').decode('gbk')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return None
    if CJK.search(real) or back != blob:
        return None
    return real


def scan():
    """扫一遍语料，收：坏字段计数、`(坏字段, 紧跟字符)` 计数、字符总数、含坏字的篇数。"""
    runs = collections.Counter()
    pairs = collections.Counter()
    files_with = total_files = total_chars = 0
    for p in RAW.rglob('*.md'):
        total_files += 1
        text = p.read_text(encoding='utf-8', errors='replace')
        hits = list(CJK.finditer(text))
        if hits:
            files_with += 1
        for m in hits:
            run = m.group(0)
            total_chars += len(run)
            runs[run] += 1
            pairs[(run, text[m.end():m.end() + 1])] += 1
    return runs, pairs, files_with, total_files, total_chars


def lost_hint(run):
    """反解不了的坏字，它**可能**是哪些字符——只给区间，不给答案。

    `鈥` 这种坏字只剩前两个字节（`e2 80`），**第三个字节已经丢了**
    （有的被替换成了 `?`，有的直接没了）。两个字节定不了唯一一个字：
    `e2 80 80`–`e2 80 bf` 整整一个区间的字符，解到前两字节全长一样。
    所以**这里给的是「可能是这类」，不是映射**——不许当映射用。
    """
    try:
        b = run.encode('gbk')
    except UnicodeEncodeError:
        return ''
    if len(b) != 2:
        return ''
    lo = bytes([b[0], b[1], 0x80]).decode('utf-8', errors='replace')
    hi = bytes([b[0], b[1], 0xBF]).decode('utf-8', errors='replace')
    try:
        lo_cp, hi_cp = ord(lo), ord(hi)
    except TypeError:
        return ''
    return f'原字符在 U+{lo_cp:04X}–U+{hi_cp:04X} 之间（第三字节已丢，只能给区间）'


def main():
    runs, pairs, files_with, total_files, total_chars = scan()

    # 先只看坏字段本身；解不出的，再带上紧跟的那个字符试
    by_run = {}
    for (run, nxt), n in pairs.most_common():
        if run in by_run:
            continue
        real = _roundtrip(run)
        how = '坏字段本身'
        if real is None:
            real = _roundtrip(run + nxt)
            how = f'坏字段+紧跟的 {nxt!r}' if real is not None else None
        if real is not None:
            by_run[run] = (real, how)

    rows = [(run, real, how, runs[run]) for run, (real, how) in by_run.items()]
    rows.sort(key=lambda r: -r[3])
    unresolved = [(run, n) for run, n in runs.most_common() if run not in by_run]

    with OUT.open('w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['坏字', '本来是', '怎么解出来的', '处数'])
        for run, real, how, n in rows:
            w.writerow([run, real, how, n])
        for run, n in unresolved:
            w.writerow([run, lost_hint(run), '反解不了——第三字节已丢', n])

    occ = sum(runs.values())
    done = sum(n for _, _, _, n in rows)
    print(f'语料 {total_files} 篇；含坏字 **{files_with} 篇**（{files_with / total_files:.1%}）')
    print(f'坏字 **{occ} 段 / {total_chars} 个字符**'
          f'（一段可能含多个字符——`鈥慴` 是两个字、覆盖原文 `‑b` 两个字符）')
    print(f'可反解 **{len(rows)} 种**（覆盖 {done} 段，{done / occ:.1%}）；'
          f'反解不了 {len(unresolved)} 种（{occ - done} 段）')
    print(f'→ {OUT}')
    print('\n前 22 条：')
    for run, real, how, n in rows[:22]:
        print(f'   {run:6s} ({n:5d} 段)  ->  {real!r}')
    if unresolved:
        print('\n反解不了的（**第三字节真丢了**，只给可能区间，不当映射用）：')
        for run, n in unresolved[:10]:
            print(f'   {run:6s} ({n:5d} 段)  {lost_hint(run)}')


if __name__ == '__main__':
    main()
