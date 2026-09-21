# 临时工具：清掉「页已经建好、正文却还写着（**未建**）」的那类过期标记。
# 见 `extract/findings-stale-unbuilt-marks.md`。
#
# **只删判据能证伪的那些**，理由必须写死在代码里，不许临场放宽：
#   ① 形状为 `（**未建**）` / `（未建）`，且**紧跟在某个 `[[x]]` 之后**（括号起点 == 链接终点）
#      → 它只可能管那一个链接。**那个链接有页 ⇒ 括号是假的 ⇒ 删掉括号。**
#   ② 形状为 `（**均未建**）` / `（**均未建**）`变体，管的是**同一行它前面所有链接**
#      → **全部都有页**才删。有一个没有 ⇒ 标记仍然成立 ⇒ 不动。
#   ③ 其余一切形状（带解释的「与本页同批建」「但允许清单里有」…）
#      **一律不动**，交给人改措辞——删掉会连信息一起丢。
#
# 用法：
#   python -X utf8 extract/fix_unbuilt_marks.py          # 试跑，只打印
#   python -X utf8 extract/fix_unbuilt_marks.py --write  # 落盘
import pathlib
import re
import sys

WIKI = pathlib.Path('wiki')
BAK = pathlib.Path('extract/.unbuilt-bak')
HAVE = {p.stem for p in WIKI.rglob('*.md')}

# ⚠️ **2026-09-21 修**：这里原来写的是 `\]\($`——**半角括号**，而原文用的是**全角 `（`**。
# 于是「括号紧跟某一条链接」那一支**一条都没匹配上**，只走了「均未建」那一支，
# 试跑因此印出「只改了 12 处」，而真数远大于此。
# **这正是本项目反复记的那个形状：一个字的差，让一条判据静默地永远为空。**
RE_LINK_END = re.compile(r'\[\[([^\]|]+)\]\]$')            # 括号紧跟在上一条链接之后
RE_ALL_LINKS = re.compile(r'\[\[([^\]|]+)\]\]')


def quoted_spans(ln):
    """这一行里所有「引文跨度」。**跨度内的字一律不许动。**

    为什么必须挡：`objects/device-directory.md:147` 写的是
    「依据：该页自己写着 `[[device-directory]]（未建）— 产物`」——
    那是**引用另一页的原话**，删掉括号就**把引文改了**，而第七类正是查引文逐字。
    同理 `:251` 那条整行是 `>` 引用块，讲的就是「那句话是它写的时候的状态」，
    删了等于把这条说明自己抹掉。

    三类跨度：`>` 引用块整行、反引号跨度、`「」`/`『』`。
    """
    spans = []
    if ln.lstrip().startswith('>'):
        return [(0, len(ln))]
    # 反引号：成对切；奇数的落单，按「到行尾」算（宁可多跳过）
    tick = [m.start() for m in re.finditer(r'`', ln)]
    for a, b in zip(tick[0::2], tick[1::2]):
        spans.append((a, b))
    if len(tick) % 2:
        spans.append((tick[-1], len(ln)))
    for op, cl in (('「', '」'), ('『', '』')):
        pos = 0
        while True:
            a = ln.find(op, pos)
            if a < 0:
                break
            b = ln.find(cl, a)
            spans.append((a, b if b >= 0 else len(ln)))
            pos = (b if b >= 0 else len(ln)) + 1
    return spans


def fix_line(ln, out):
    """返回改过的行。`out` 收 (说明, 原名) 供打印。"""
    spans = quoted_spans(ln)
    # ③ 只认判据写死的两种括号，别的一律不动
    for m in reversed(list(re.finditer(r'（(?:未建|\*\*未建\*\*|\*\*均未建\*\*)）', ln))):
        if any(a <= m.start() < b for a, b in spans):
            out.append(('跳过：在引文里', ln[m.start():m.end()]))
            continue
        paren = m.group(0)
        head = ln[:m.start()]
        both = '均' in paren
        if both:
            names = [x.group(1).strip() for x in RE_ALL_LINKS.finditer(head)]
        else:
            names = []
            mm = RE_LINK_END.search(head)
            if mm:
                names = [mm.group(1).strip()]
        if not names:
            continue
        if not all(n in HAVE for n in names):
            continue
        out.append(('删括号', '%s → %s' % (paren, ' / '.join(names))))
        ln = head + ln[m.end():]
    return ln


def main(write):
    changed, skips, leftover = [], [], []
    for p in sorted(WIKI.rglob('*.md')):
        t = p.read_text(encoding='utf-8')
        out = []
        lines = t.split('\n')
        newl = []
        for i, ln in enumerate(lines):
            o = []                      # **按行记账**——上一版把「已改的行」也算进「留给人改」，
            newl.append(fix_line(ln, o))  # 于是那 156 是个假数（同 §13.1 那个形状）
            out += o
            if not o and '未建' in ln and any(
                    x.group(1).strip() in HAVE for x in RE_ALL_LINKS.finditer(ln)):
                leftover.append((p, i + 1, ln.strip()[:110]))
        new = '\n'.join(newl)
        sk = [x for x in out if x[0].startswith('跳过')]
        hits = [x for x in out if not x[0].startswith('跳过')]
        # ⚠️ **跳过要单独报，挂在文件上、不挂在「改没改」上**：
        # 上一版只有「改了东西」的文件才印，于是「整行都在引文里、一处没改」
        # 的文件**看不见**——而「跳过」和「根本没看」在报告里长得一模一样。
        if sk:
            skips.append((p, sk))
        if hits and new != t:
            changed.append((p, len(hits), hits))
            if write:
                bak = BAK / p.relative_to(WIKI)
                bak.parent.mkdir(parents=True, exist_ok=True)
                bak.write_text(t, encoding='utf-8', newline='')   # 原样备份，可逐字节回退
                p.write_text(new, encoding='utf-8', newline='')
    print('改了 %d 个文件（%d 处）：' % (len(changed), sum(c[1] for c in changed)))
    for p, n, out in changed:
        print('  %s  ×%d' % (p.relative_to(WIKI).as_posix(), n))
        for kind, desc in out:
            print('      - %s: %s' % (kind, desc))
    print('\n跳过（在引文里，一个字不动）%d 个文件 %d 处：'
          % (len(skips), sum(len(s) for _, s in skips)))
    for p, sk in skips:
        print('  %s  ×%d' % (p.relative_to(WIKI).as_posix(), len(sk)))
    print('\n留给人改措辞的（形状不明确/删了会丢信息）：%d 处' % len(leftover))
    if not write:
        print('\n（试跑，未落盘。加 --write 落盘。）')


if __name__ == '__main__':
    main('--write' in sys.argv)
