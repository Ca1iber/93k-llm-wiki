# -*- coding: utf-8 -*-
"""把悬空 wikilink 的 slug 归一（schema §5 + 「§5 与 §11 的分工」）。

只改 `[[ ]]` 里的目标名，**代码跨度里讲格式的示例不动**——那两句
`` `[[对象页名]]` `` / `` `[[命令对象页]]` `` 是格式说明，不是引用。

映射是**逐条手定的**，不是机械 lower()：
`LotSummaryGenerator` 机械转出来是 `lotsummarygenerator`（不可读），
`02.06.11.02_List_of_test_result_commands` 机械转出来带一串分类号（丑）。
**机械规则适合找候选，不适合定名字。**
"""
import re
from pathlib import Path

WIKI = Path(r'F:\master-dev\understand-anything-wiki\wiki')

RENAME = {
    # 驼峰要拆词，不能只 lower
    'LotSummaryGenerator': 'lot-summary-generator',
    'SmarTest_Data_Formatter': 'smartest-data-formatter',
    # 分类号留在 slug 里没意义，那是路径不是标识符
    '02.06.11.02_List_of_test_result_commands': 'list-of-test-result-commands',
    # 命令 / API 本名小写（§5）；正文里仍写原样大小写（§11）
    'TMLimits': 'tmlimits',
    'EDF': 'edf',
    'STDF': 'stdf',
    'DRLDump': 'drldump',
    'RESULT_CONFIGURATION': 'result-configuration',
    'TESTSET__.testname': 'testset-testname',
    # 下划线 → 连字符
    'Data_Logging_Profile': 'data-logging-profile',
    'Data_logging_profile_API': 'data-logging-profile-api',
    'Data_Retrieval_Library': 'data-retrieval-library',
    'Error_Map': 'error-map',
    'Error_Map_Tool': 'error-map-tool',
    'Event_Formatter': 'event-formatter',
    'Integrated_Result_Tool': 'integrated-result-tool',
    'Report_window': 'report-window',
    'Shmoo_Tool': 'shmoo-tool',
    'Signal_Analyzer': 'signal-analyzer',
    'Timing_Diagram_Tool': 'timing-diagram-tool',
    'EDL_file': 'edl-file',

    # ── 第二批：被反引号藏住的 22 个（修好 `_links()` 之后才现形）────────────
    # 全是 L1/L2 的**本名**，之前 `_strip_code` 把行内代码跨度剥掉，
    # 于是 `` `[[ON_FIRST_INVOCATION_BEGIN]]` `` 这类根本没进检查。
    # §5 自己给了标准变换：`ON_FIRST_INVOCATION_BEGIN` → `on-first-invocation-begin`。
    'ON_FIRST_INVOCATION_BEGIN': 'on-first-invocation-begin',
    'ON_FIRST_INVOCATION_END': 'on-first-invocation-end',
    'FOR_EACH_SITE_BEGIN': 'for-each-site-begin',
    'FOR_EACH_SITE_END': 'for-each-site-end',
    'BEGIN_EXTENSION': 'begin-extension',
    'END_EXTENSION': 'end-extension',
    'FW_TASK': 'fw-task',
    'VEC_EVENTS': 'vec-events',
    'PRIMARY_STATUS': 'primary-status',
    'SEQUENCER_STATUS': 'sequencer-status',
    'PATTERN_CONTROLLER': 'pattern-controller',
    'CONNECT': 'connect',
    'DISCONNECT': 'disconnect',
    'TEST': 'test',
    'TESTSET': 'testset',
    'LIMIT': 'limit',
    'addLimit': 'add-limit',
    'playPattern': 'play-pattern',
    'SpecValue': 'spec-value',
    'SpecVariable': 'spec-variable',
    'PinString': 'pin-string',
    'FileString': 'file-string',
    'OptionList': 'option-list',
    'ContextPins': 'context-pins',
    'Test_Method_Project': 'test-method-project',
    'Test_Method_Class': 'test-method-class',
    'Universal_Test_Method_Library': 'universal-test-method-library',

    # ── 唯一撞名的：`PATTERN` 机械转出来是 `pattern`，而**那是 stage 页**──
    # `PATTERN`（`02.07.04.01.142.01`）是「持有 subpattern 元素的附属容器类」，
    # `pattern` 是流程脊椎的第七段。**同名会被静默指错**——
    # 第八类看到 `pattern` 有页，不报错；读者点进去却是另一个东西。
    # 比「重复页」更坏：重复页看得见，指错看不见。
    # 规矩：**stage 名是保留 slug，对象页撞上时加 `-object`**（写进 schema §5）。
    'PATTERN': 'pattern-object',
}


def strip_code(b):
    b = re.sub(r'```.*?```', ' ', b, flags=re.S)
    return re.sub(r'`[^`\n]*`', ' ', b)


def main():
    # 先确认映射的值本身合 §5
    for old, new in RENAME.items():
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', new), f'{new} 不合 §5'
    # 再确认没有值互相碰撞（碰撞意味着两个对象会被建成一页，那是语义合并，得人定）
    vals = list(RENAME.values())
    assert len(vals) == len(set(vals)), '映射值有重复，需人工确认是否该合并'
    # 再确认改名**不撞已有的页**。这条是冲着 `PATTERN` 来的：
    # 机械转出 `pattern`，而 `pattern` 已经是一页（stage 第七段）。
    # 撞了不会报错——第八类看到有页就算「可达」，读者点进去却是别的东西。
    have = {p.stem for p in WIKI.rglob('*.md')}
    clash = sorted(set(vals) & have)
    assert not clash, f'改名撞上已存在的页，必须先定限定词：{clash}'

    total = 0
    for p in sorted(WIKI.rglob('*.md')):
        txt = p.read_text(encoding='utf-8')
        # 只在 `[[ ]]` 内部替换；用函数式替换，避免动到代码跨度
        def sub(m):
            t = m.group(1)
            return '[[' + RENAME.get(t, t)

        new = re.sub(r'\[\[([^\]|#]+)', sub, txt)
        if new != txt:
            n = sum(1 for m in re.finditer(r'\[\[([^\]|#]+)', txt)
                    if m.group(1) in RENAME)
            p.write_text(new, encoding='utf-8')
            print(f'  {p.relative_to(WIKI)}: {n} 处')
            total += n
    print(f'\n共改 {total} 处，涉及 {len(RENAME)} 个 slug')
    print(f'-> 先 `python verify_stages.py` 复查第八、九类')


if __name__ == '__main__':
    main()
