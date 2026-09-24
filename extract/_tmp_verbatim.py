"""查 wiki 页里引的原文（`>` 行）在语料里**逐字**找得到——一次性的，只认 `PAGES` 里那 4 页。

**不是检验。** 页和语料一改，`PAGES` 就过期，跑出来的 `MISS` 也就不再是缺陷——
所以它没进 `verify_stages.py`。名字里的 `tmp` 是实话：这是当时就地写的核对工具。
"""
import re
import os

RAW = r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category'
PAGES = {
    'timing-spec': ('wiki/objects/timing-spec.md',
                    '02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.md'),
    'wavetable-file': ('wiki/objects/wavetable-file.md',
                       '02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.03_Wavetable_file.md'),
    'dfps': ('wiki/objects/dfps.md',
             '02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md'),
    'eqfs': ('wiki/objects/eqfs.md',
             '02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md'),
}

LINK = re.compile(r'\[([^\]]*)\]\(<[^>]*>\)')


def norm(s):
    s = LINK.sub(r'\1', s)
    s = s.replace('**', '').replace('`', '')
    for ch in '「」『』':
        s = s.replace(ch, '')
    s = re.sub(r'[\u2014\u2013\u2212]', '-', s)
    s = re.sub(r'[\u201c\u201d]', '"', s)
    s = re.sub(r'[\u2018\u2019]', "'", s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


CJK = re.compile(r'[\u4e00-\u9fff]')

for name, (page, raws) in PAGES.items():
    raw = norm(open(os.path.join(RAW, raws), encoding='utf-8').read())
    text = open(page, encoding='utf-8').read()
    print('====', name, '-- pure-ASCII ">" lines (these are the checked ones)')
    for i, l in enumerate(text.split('\n')):
        if not l.startswith('>'):
            continue
        if CJK.search(l):
            continue
        body = l.lstrip('>').strip()
        n = norm(body)
        if not n:
            continue
        # treat inline code spans individually too
        spans = re.findall(r'`([^`\n]+)`', body)
        okline = (n in raw) or (spans and all(norm(s) in raw for s in spans))
        print('  L%-4d %s  %s' % (i + 1, 'OK ' if okline else 'MISS', n[:150]))
