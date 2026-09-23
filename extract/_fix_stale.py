#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""订正三处**已经说过时的话**。

最要紧的一处：`schema.md` §1.2 是**规则书**，里面「改哪一层」还写着旧规矩。
我在 log 里写了「规矩改了」，**却没改规则书**——下一个人（或我）读 §1.2 会照错的做。
"""
import pathlib

W = pathlib.Path('F:/master-dev/understand-anything-wiki')


def patch(rel, subs, label):
    p = W / rel
    b = p.read_bytes()
    crlf = b.count(b'\r\n') > b.count(b'\n') - b.count(b'\r\n')
    NL = '\r\n' if crlf else '\n'
    n0 = (b.count(b'\r\n'), b.count(b'\n') - b.count(b'\r\n'))
    for i, (old, new) in enumerate(subs, 1):
        o, n = old.replace('\n', NL).encode('utf-8'), new.replace('\n', NL).encode('utf-8')
        c = b.count(o)
        assert c == 1, f'{rel} 第 {i} 处命中 {c} 次'
        b = b.replace(o, n, 1)
    p.write_bytes(b)
    n1 = (b.count(b'\r\n'), b.count(b'\n') - b.count(b'\r\n'))
    assert n1[1] == n0[1], f'{rel} 裸 LF 变了 {n0[1]}→{n1[1]}'
    print(f'✓ {label:<22} {n1[0]} CRLF / {n1[1]} 裸LF   {p.stat().st_size:,} 字节')


# ── 1. schema.md §1.2：**规则书**（CRLF）────────────────────────
patch('schema.md', [(
    '**改哪一层：只改 `agent-markdown/`。`tdc-html/raw/` 一个字不许动。**\n'
    '**理由**：HTML 是 A 类**唯一的对证上游**。改掉它，以后**再也证不了任何一处**——\n'
    '包括已经改过的那 151 处。',
    '**改哪一层：哪一层错就改哪一层。**（**2026-09-23 用户改**，此前写的是'
    '「只改 `agent-markdown/`，`tdc-html/raw/` 一个字不许动」）\n'
    '\n'
    '> **为什么原来那条可以让位。** 原来的理由是「HTML 是唯一的对证上游，改掉就再也证不了」。\n'
    '> **现在两层都在 git 里**——`git log` / `git show HEAD:` 接管了「不许动」想干的事：\n'
    '> 上游被改过也**查得出来、回得去**。\n'
    '>\n'
    '> **但有两条不能松：**\n'
    '> 1. **先判是哪一层的错**，不要默认改下游。判据取**上游自己**——\n'
    '>    同一文件里别处的写法（`98749.htm` 有 12 处写 `2<sup>31</sup>-1`，\n'
    '>    那 2 处却写 `2<sup>32-1</sup>`），或文内自证（`10-9 Hz (nHz)` 里的 `nHz`\n'
    '>    就证明了那是 10⁻⁹）。\n'
    '> 2. **改上游之前，先确认它已入库**——重放读的是 `git show HEAD:`，不是工作区。\n'
    '>    **上游没进 git 就改它，「重放」这条退路同时断掉。**',
)], 'schema.md §1.2')

# ── 2. raw/README.md 铁律（LF）─────────────────────────────────
patch('raw/README.md', [(
    '- **只读。** 任何情况下不许修改这里的文件。\n'
    '  - **唯一例外：A 类「转换损坏」**——上游 `tdc-html/raw/` 的 HTML 明写着原意，\n'
    '    转换时被拍平 / 粘连 / 丢标签。判据（三条）、流程（五步）、代价见 `schema.md` **§1.2**。',
    '- **只读。** 任何情况下不许修改这里的文件。\n'
    '  - **例外一：转换损坏**——上游 `tdc-html/raw/` 的 HTML 明写着原意，\n'
    '    转换时被拍平 / 粘连 / 丢标签 / 丢内容。判据（三条）、流程（五步）、代价见 `schema.md` **§1.2**。\n'
    '  - **例外二（2026-09-23 加）：哪一层错就改哪一层**（用户定）。\n'
    '    **上游 HTML 自己写错时改 HTML**（`<sup>` 把标点或运算符包了进去），\n'
    '    不再一律只改下游。**但先要判清是哪一层的错**，且**改上游前确认它已入库**——\n'
    '    重放读的是 `git show HEAD:`。',
)], 'raw/README.md 铁律')

# ── 3. findings 两处过时话（LF）────────────────────────────────
patch('extract/findings-corpus-superscript-loss.md', [(
    '语料 **151 处 / 60 篇**、wiki **91 处 / 5 页**，逐字节验过。处置与账目见 **§八** 与 **§十**。',
    '语料 **151 处 / 60 篇**；wiki 侧**散文 2 处**手工改 + **4 页**由 `--refresh-syntax`\n'
    '**脚本重刷**，逐字节验过。处置与账目见 **§八** 与 **§十**。\n'
    '（此处曾写「wiki 91 处 / 5 页」——**那是判据找到的候选数，不是改动数**：'
    '91 里 88 处落在脚本管的两节里。见 §十·错二。）',
), (
    '- **改哪一层**：只改 `agent-markdown/`。**`tdc-html/raw/` 的 HTML 一个字不许动**——\n'
    '  它是 A 类唯一的对证上游，改掉就再也证不了任何一处。',
    '- **改哪一层**：只改 `agent-markdown/`。**`tdc-html/raw/` 的 HTML 一个字不许动**——\n'
    '  它是 A 类唯一的对证上游，改掉就再也证不了任何一处。\n'
    '  （**这是 A 批当时的规矩。2026-09-23 已改成「哪一层错就改哪一层」，见 `schema.md` §1.2。**）',
)], 'findings 两处')
