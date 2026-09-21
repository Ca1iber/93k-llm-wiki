# ⚠️⚠️ **别拿这个脚本的输出当判据。**
# 2026-09-21：它对全库报「949 条引文对不上」。抽三条回 raw 逐条核过——
#   ① 一条**在 raw 里真的有**（是它自己的归一化不如第七类的 `_norm` 全）；
#   ② 一条是**页面自己写的中文摘要**（`>` 块不一定是引文）；
#   ③ 一条是**页面记录自己初版错译**的引文（它故意不在 raw 里）。
# **949 条里没有一条是页面的错。** 引文这一项的判据是 `verify_stages.py` 的第七类
# （它会跳过语法节、按 8 词窗算覆盖率、只对自称「逐字」的段落判错），那个是 ✅。
# 留着它只为**可复现**——记在 `wiki/log.md` 与 `findings-stale-unbuilt-marks.md` 里。
# 临时：验证 wiki 页里的「逐字引文」真的能在它 sources 指的 raw 里找到。
# 判据：把页面里的引文候选抽出来，做三处归一化后去 raw 里找子串：
#   ① 剥掉引用块标记 `> `（否则断行的引文会夹进一个 `> `）
#   ② 语法节的链接改写 `（raw: 路径）` 去掉；markdown 链接 [文本](路径) 只留文本
#   ③ 去掉 `**` 与反引号，空白折叠
# raw 那侧做同样的 ②③，保证两边可比。
# **只读，不写任何文件。**
import pathlib
import re
import sys

CORPUS = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')
WIKI = pathlib.Path('wiki')
CJK = re.compile(r'[\u4e00-\u9fff]')
# \u5f15\u6587\u4e24\u7aef\u53ef\u80fd\u662f\u672c\u9875\u81ea\u5df1\u7684\u6807\u70b9\uff0c\u4e0d\u662f\u539f\u6587\u7684\u4e00\u90e8\u5206
EDGE_JUNK = ' \t\uff08\uff09()\u300c\u300d\u300e\u300f\u3001\uff0c\u3002\uff1b\uff1a:;,.\u2026\u2014\u2013-"\'\u2019\u2018\u201c\u201d'


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def unlink(s):
    s = re.sub(r'（raw:\s*`[^`]*`）', '', s)          # 语法节的链接改写
    s = re.sub(r'\[([^\]]*)\]\(<?[^)]*>?\)', r'\1', s)  # [文本](路径) -> 文本
    s = s.replace('\\|', '|')                            # 语法节把表格里的 | 转义成 \|
    return s.replace('**', '').replace('`', '')


def load_raw(rel):
    p = CORPUS / rel
    if not p.exists():
        return None
    return norm(unlink(p.read_text(encoding='utf-8', errors='replace')))


def sources_of(text):
    m = re.search(r'^sources:(.*?)(?=^\w)', text, re.M | re.S)
    if not m:
        return []
    return [s.replace('\\', '/') for s in re.findall(r'[\w\-./]+\.md', m.group(1))]


SCRIPT_BLOCK = re.compile(
    r'<!-- (?:语法节|报错节) begin.*?<!-- (?:语法节|报错节) end -->', re.S)


def candidates(text):
    """引文候选：① 正文里的 「…」；② 反引号里成句的英文。

    先切掉两个**脚本生成块**（语法节 / 报错节）：那两块的原文来自 raw（含子主题），
    不是本页作者写的，且 `check_syntax_fresh.py` 已独立证明它们没被手改。
    本检查器只管**手写的散文**。
    """
    text = SCRIPT_BLOCK.sub('\n', text)
    out = []
    # 剥掉引用块标记，让断行的引文连起来
    flat = re.sub(r'^[ \t]*>[ \t]?', '', text, flags=re.M)
    # ① 「…」：本工程「逐字」的正式标记。非贪婪——否则一个 「 会吞到最后一个 」。
    for m in re.finditer(r'「([^」]{25,}?)」', flat, re.S):
        out.append(m.group(1))
    # ② 反引号里成句的英文（⚠️ 段里逐字引语料瑕疵时用的写法）。
    #    只取「含空格、≥40 字符、无中文」的，避免把命令名、路径、字段名当引文。
    #    必须按奇偶切分：正则 `` `([^`]+)` `` 会从**上一个反引号的收尾**跨到
    #    **下一个反引号的开头**，把两个 code span 之间的行文当成引文抓出来。
    for line in text.split('\n'):
        for s in line.split('`')[1::2]:
            if len(s) >= 40 and ' ' in s and not CJK.search(s):
                out.append(s)
    return out


def main():
    only = set(sys.argv[1:]) or None
    bad_total = 0
    checked = 0
    for p in sorted(WIKI.rglob('*.md')):
        if only and p.stem not in only:
            continue
        text = p.read_text(encoding='utf-8', errors='replace')
        if not text.startswith('---'):
            continue
        rels = sources_of(text)
        raws = [r for r in (load_raw(x) for x in rels) if r]
        if not raws:
            if rels:
                print('⚠️  %s: sources 找不到 raw %s' % (p.as_posix(), rels))
            continue
        checked += 1
        miss = []
        for q in candidates(text):
            # 引文两端常粘着本页自己的标点（全角括号、句号、省略号…），剥掉再比
            c = norm(unlink(q)).strip(EDGE_JUNK)
            if len(c) < 40:
                continue
            if not any(c in r for r in raws):
                miss.append(c)
        if miss:
            bad_total += len(miss)
            print('=' * 90)
            print('%s  (%d 段对不上)' % (p.as_posix(), len(miss)))
            for m in miss[:8]:
                print('   ✗ %s' % m[:160])
    print()
    print('查了 %d 页，对不上的引文段 %d 条。' % (checked, bad_total))


if __name__ == '__main__':
    main()
