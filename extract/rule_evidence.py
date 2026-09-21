"""给「我要建页的那条规矩」数证据：**处数 / 文件数 / 独立文档数 / 出处**。

## 为什么要有这个脚本

`constraints/` 的每一页都要写「这条规矩在语料里出现 N 处、横跨 M 篇」。
**这个数是文档事实，不是印象**——它必须是某条命令能重跑出来的。
§13.1 常设问题②：「我印的这个数是谁算的？」**答不上来的数不许写进页面。**

所以这里把每条规矩写成一条**具名正则**，页面里引用的是 `RULES` 的键，
跑一次就能复现页面上的每一个计数。

## ⚠️ 计数器的三个坑，这里都避开了

1. **`docs` 不是独立文档数。** 语料把同一篇文档投放在多个分类树下
   （§11.2 ④ / 第十类），所以「28 个文件」可能只是「16 篇文档」。
   真正要报的是 `n_doc`——**去掉分类号前缀后的标题**，副本共享它。
   （`title_of` 与 `constraint_dispose.py` 同一个函数，**不是照抄**：它从这里导入。）
2. **句子不是行。** 语料里一行常塞好几个句子（见 `SMC_ARM.md` 第 21 行，
   一行装了两条 CAUTION）。**按行数报会把两处报成一处**，所以这里报的是**正则命中次数**，
   并同时报**命中行数**，两个数不一样时页面必须挑一个说清是哪个。
3. **大小写。** 全部 `re.I`——语料同一句话有 `TSTL`/`tstl` 两种写法。
   代价是可能多认，所以每种规则都把**命中原文**打印出来供人核。

用法：

    python -X utf8 rule_evidence.py            # 全部规则
    python -X utf8 rule_evidence.py B          # 只跑键以 B 开头的规则

只读 raw，不写任何文件——**它产的是「给人看的证据」，不是「给脚本吃的索引」**。
"""
import collections
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')

sys.path.insert(0, str(HERE))
from constraint_dispose import title_of   # 与 ③ 的处置脚本**同一个**身份函数

# 每条规矩 = 一个具名正则。**键就是页面里引用的名字。**
RULES = {
    # B 族：编辑 label 前必须用 TSTL 选为编辑态。
    # 两种措辞都收：「activate … for editing」（命令页 Predependencies 的多数措辞）、
    # 「select … for editing」（APDV/CNGV/DELI 的措辞、以及 CPYV/DELI 的报错句）。
    # **两种措辞是同一件事**——只收一种会漏掉一半证据，这在页面里要写明。
    'B-predep': re.compile(
        r'can\s+only\s+be\s+issued\s+after\s+(?:a\s+label|the\s+label)[^.]{0,80}?'
        r'(?:activated|selected)\s+for\s+editing', re.I),
    'B-general': re.compile(
        r'you\s+must\s+activate\s+the\s+new\s+label\s+for\s+editing\s+with\s+the\s+TSTL\s+command',
        re.I),
    'B-error': re.compile(r'No\s+label\s+has\s+been\s+(?:activated|selected)\s+for\s+editing\.', re.I),

    # H 族：引用型集合必须先定义。报错形态是「集合不存在」。
    'H-error': re.compile(
        r'(?:the\s+)?(?:spec\s+value|search|jitter|transition\s+test)\s+set'
        r'[^.]{0,40}?(?:does\s+not\s+exist|with\s+the\s+specified\s+name\s+exists)', re.I),
    'H-predep': re.compile(r'must\s+have\s+been\s+defined\s+with', re.I),

    # E 族：SMC 后台进程运行中，配置/参数不许动。
    'E-caution': re.compile(
        r'(?:may\s+result\s+in\s+invalid\s+data|invalid\s+data\s+or\s+(?:in\s+)?a\s+crash'
        r'|crash\s+of\s+the\s+test\s+method)', re.I),
    'E-must-not': re.compile(
        r'must\s+not\s+be\s+changed\s+while\s+the\s+background\s+process\s+is\s+running'
        r'|must\s+not\s+change\s+or\s+reload\s+a\s+TMLimits\s+table'
        r'|must\s+be\s+finished\s+before\s+a\s+Mode\s+context\s+is\s+changed', re.I),

    # 站点焦点族：用站点焦点的命令，执行前必须先设焦点。
    'S-general': re.compile(
        r'you\s+have\s+to\s+set\s+the\s+site\s+focus\s+before\s+you\s+can\s+execute\s+the\s+command',
        re.I),
    'S-setupfocus': re.compile(r'configure\s+setups\s+of\s+those\s+sites\s+that\s+have\s+the\s+setup\s+focus', re.I),
    # 站点焦点的**后果**：不设焦点时走默认焦点。文档把默认值写出来了。
    'S-hpfw': re.compile(
        r'without\s+site\s+focus\s+setup\s+command\s+will\s+not\s+automatically\s+get'
        r'|take\s+the\s+default\s+setup\s+focus|take\s+the\s+result\s+of\s+default\s+site\s+in\s+focus',
        re.I),

    # ④ 执行上下文：必须先在固件级定义过。**分支写法**，两条路都要收。
    'C-execctx-fw': re.compile(r'must\s+have\s+been\s+defined\s+on\s+the\s+firmware\s+level', re.I),
    'C-execctx-name': re.compile(r'must\s+use\s+the\s+name\s+specified\s+for\s+its\s+name\s+parameter', re.I),
    'C-execctx-port': re.compile(r'ports\s+of\s+the\s+context\s+must\s+be\s+included\s+in\s+the\s+current\s+start\s+label', re.I),
    # 配对使用。**和上面三条不是同一条规矩**——这条管「成对」，不管「定义」。
    'C-pair': re.compile(r'must\s+be\s+used\s+as\s+a\s+pair', re.I),

    # ⑤ testName 与 limits 必须同名。D3。
    'L-testname': re.compile(r'add\s+limits\s+to\s+the\s+test\s+suite\s+with\s+the\s+same\s+test\s+name', re.I),

    # ⑥ RDI：**两条不同的规矩**，别合并。
    'R-rdi-inside': re.compile(r'It\s+must\s+be\s+used\s+inside\s+a\s+RDI_BEGIN\(\)/RDI_END\(\)\s+block', re.I),
    'R-rdi-same': re.compile(r'must\s+be\s+the\s+same\s+within\s+one\s+RDI_BEGIN\(\)', re.I),

    # ③ 同测试处理器：**⚠️ 这个键原本叫 `P-sameTP`，它把两条不同的规矩混成了一个数。**
    # 一条讲 **DUT 板上的环回 pin**，一条讲 **Smart Scale 嵌入式搜索的 setup/result pin**——
    # 两个主语、两个条件、两个出处，只是共用 `belong to the same test processor` 这个谓语。
    # **判据把两件事算成一个数，是判据的错，不是语料的错。** 拆开分别数。
    'P-loopback-TP': re.compile(
        r'Loopback\s+pins\s+must\s+belong\s+to\s+the\s+same\s+test\s+processor', re.I),
    'P-setupresult-TP': re.compile(
        r'Setup\s+and\s+result\s+pins\s+are\s+independent\s+of\s+each\s+other,\s+but\s+must\s+belong'
        r'\s+to\s+the\s+same\s+test\s+processor', re.I),
    'P-pooling': re.compile(r'support\s+memory\s+pooling\s+in\s+groups\s+of\s+eight\s+channels', re.I),
    'P-fastSync': re.compile(r'synchronized\s+DUT\s+pins\s+must\s+be\s+assigned\s+to\s+the\s+same', re.I),
}


def hunt(rx):
    """→ (命中次数, 命中行数, 文件数, 独立文档数, 出处 Counter)"""
    hits = lines = 0
    files, docs, where = set(), set(), collections.Counter()
    for p in sorted(CORPUS.rglob('*.md')):
        rel = p.relative_to(CORPUS).as_posix()
        t = p.read_text(encoding='utf-8', errors='replace')
        n = len(rx.findall(t))
        if not n:
            continue
        hits += n
        lines += sum(1 for l in t.splitlines() if rx.search(l))
        files.add(rel)
        docs.add(title_of(rel))
        where[rel] = n
    return hits, lines, files, docs, where


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    picks = sys.argv[1:] or list(RULES)
    for key in picks:
        # **印的必须是真正匹配到的那个键，不是我传进去的那个。**
        # 前缀匹配一次就只中一条：传 `R-rdi` 会静默选中 `R-rdi-inside`，
        # 而下面的标题原本照抄我传的 `R-rdi`——**数是对的，标签是错的**。
        # 这正是常设问题②要抓的形状，所以命中后把真名印出来，不匹配时点名。
        matched = [k for k in RULES if k == key or k.startswith(key)]
        if not matched:
            print(f'!! 没有这个规则键：{key}（有：{", ".join(RULES)}）')
            continue
        if len(matched) > 1:
            print(f'!! `{key}` 是前缀，命中 {len(matched)} 条：{", ".join(matched)}——'
                  f'请给全名。**本次不跑，免得数错了还对不上账。**')
            continue
        name = matched[0]
        hits, lines, files, docs, where = hunt(RULES[name])
        print(f'\n===== {name}  命中 {hits} 次 / {lines} 行 / {len(files)} 文件 / '
              f'**{len(docs)} 篇独立文档**')
        for rel, n in where.most_common(6):
            print(f'    {n:4}  {rel}')
        if len(where) > 6:
            print(f'    …（还有 {len(where)-6} 个文件，最多的 6 个印在上面）')


if __name__ == '__main__':
    main()
