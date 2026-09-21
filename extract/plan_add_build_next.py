# -*- coding: utf-8 -*-
"""把 `build-next.csv` 那张工作单**转成 `wiki-plan.csv` 的行**。

**为什么要有这个脚本、而不是手敲 71 行。**

`build_next.py` 只回答「哪些 slug 还没建、按什么顺序建」，它**不回答**
`type` / `layer` / `stage`——那三列是**人的判断**（§2 / §6），
`build-next.csv` 里那三格是空的。手工敲 71 行会有一个**看不出来的错法**：
`rel` 抄错一个字符，页面照建、`sources:` 照写，而第六类会照着一个
不存在的 rel 认为「这篇有人认领了」——**错误被静默吸收**。

所以这里把判断写成一个表、由脚本落盘，落盘时逐条对着 `docs.jsonl` 查存在。

---

## 一、这 78 行里有 7 行**不单独建页**

判据是「两行指的是不是同一个东西」。§5 和 §13 都点过：**同一个对象的两个半页，
比一个整页更坏**——读者会停在错的那半张上。

| 候选（不单独建） | 并进 | 为什么 |
|---|---|---|
| `technology-file` | `technology-file-for-a-device` | 同一篇东西的两种叫法；前者连 `rel` 都是空的（连定义文档都没有） |
| `dc-scale-uhc4-uhc4t-card` | `dc-scale-uhc4t-card` | **同一张卡的两个章节**：`02.03`（DUT 板侧，pogo block）和 `02.05`（测试头卡侧）。卡只有一个，两节都进 `sources` |
| `using-the-timing-diagram-tool` | `timing-diagram-tool` | 一个东西的「是什么」和「怎么用」。合成一页，用法进 `## 典型用法` |
| `setting-up-a-shmoo-test-with-the-shmoo-tool` | `shmoo-tool` | 同上 |
| `smartrdi-tmu-test-setup` | `smartrdi` | 同上 |
| `setting-up-dc-scale-pins-with-smartrdi` | `smartrdi` | 同上 |
| `test-number-generator-and-tmlimits` | `structure-of-a-tmlimits-csv-file` | 同一子树的父子：`02.10.01.08.01` 讲生成，`…08.01.01.03.01` 讲产物（CSV）。生成器的产出就是那张表 |

**留下来的 71 行**：B 组 31 − 1 = 30，A 组 47 − 6 = 41。

> ⚠️ **"合并"是一个决定，不是一个事实**。上面每一条都可能被推翻
> （比如以后发现 UHC4 和 UHC4T 真的是两张卡）。所以它**写在这里、不进代码注释**，
> 并且 `build_next.py` 里有一份 `FOLDED` 让工作单不再重复提它们——
> **决定要能被找到、也要能被改**。

## 二、`type` / `layer` / `stage` 怎么定的

- `type`：**是「一个东西」就是 `object`**（命令、文件、工具、卡、API 类）；
  **是「一种做法/一件事」就是 `concept`**（多站点控制、DC 测试编程、板级设计参考）。
- `layer`：这页主要从哪一层描述它。`L1` 固件命令 / `L2` 测试程序 / `L3` 测试方法 API /
  `file` 文件格式 / `gui` 图形工具 / `n/a` 与层次无关（硬件、板级）。
- `stage`：**必须是九页 stage 里的一个**（`level` `pin` `pattern` `project` `results`
  `run` `testflow` `testmethod` `timing`）。跨多个的挑最中心的那个——
  「列了九个」等于「没归位」，而 `stage` 是流程页反向找对象的钥匙。

用：`python -X utf8 extract/plan_add_build_next.py`          # 只看要加什么
    `python -X utf8 extract/plan_add_build_next.py --write`  # 真写进 wiki-plan.csv
"""
import csv
import json
import sys
from pathlib import Path

BASE = Path(r'F:\master-dev\understand-anything-wiki')
OUT = BASE / 'extract'
PLAN = OUT / 'wiki-plan.csv'

# ── 并入别页的 7 行：**不建** ──────────────────────────────────────────
FOLDED = {
    'technology-file': ('technology-file-for-a-device', '同一对象的另一种叫法'),
    'dc-scale-uhc4-uhc4t-card': ('dc-scale-uhc4t-card', '同一张卡的两章（DUT 板侧 / 测试头卡侧）'),
    'using-the-timing-diagram-tool': ('timing-diagram-tool', '「怎么用」并在「是什么」里'),
    'setting-up-a-shmoo-test-with-the-shmoo-tool': ('shmoo-tool', '「怎么用」并在「是什么」里'),
    'smartrdi-tmu-test-setup': ('smartrdi', '「怎么用」并在「是什么」里'),
    'setting-up-dc-scale-pins-with-smartrdi': ('smartrdi', '「怎么用」并在「是什么」里'),
    'test-number-generator-and-tmlimits': ('structure-of-a-tmlimits-csv-file', '父篇讲生成、子篇讲产物'),
}

# ── 71 行：`slug, type, layer, stage, rel, note` ──────────────────────
# A 组的 `rel` 直接抄 `build-next.csv`（那是脚本从语料里查出来的）；
# B 组的 `rel` 是**人查出来的**——`build-next.csv` 里 B 组大多为空，
# 因为「谁被链了」能从 `[[…]]` 数出来，「那篇定义文档在哪」不能。
R = [
    # ================= B 组：被悬空链接指到、但页不存在的靶子（30）=================
    # 固件命令（L1）——`02.06.02.02` 是固件命令字典
    ('ctxt', 'object', 'L1', 'level',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.md', ''),
    ('dfpn', 'object', 'L1', 'pin',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md', ''),
    ('sqst', 'object', 'L1', 'pattern',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.md', ''),
    ('pals', 'object', 'L1', 'pin',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md', ''),
    ('psfc', 'object', 'L1', 'pin',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.md', ''),
    ('conf', 'object', 'L1', 'project',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md', ''),
    ('dscp', 'object', 'L1', 'project',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md', ''),
    ('jscf', 'object', 'L1', 'timing',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md', ''),
    ('jsdf', 'object', 'L1', 'timing',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md', ''),
    ('jspr', 'object', 'L1', 'timing',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.md', ''),
    ('pste', 'object', 'L1', 'run',
     '02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.md', ''),
    # 测试方法 API（L3）
    ('primary-status', 'object', 'L3', 'level',
     '02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.md', ''),
    ('sequencer-status', 'object', 'L3', 'pattern',
     '02_System_reference/02.07_Test_Method_Reference/02.07.04.01.204_SEQUENCER_STATUS_-__Sequencer.md', ''),
    ('tmlimits', 'object', 'L3', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md', ''),
    # 图形工具（gui）
    ('report-window', 'object', 'gui', 'results',
     '01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.md', ''),
    ('timing-diagram-tool', 'object', 'gui', 'pattern',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.md',
     '并入 using-the-timing-diagram-tool'),
    ('error-map-tool', 'object', 'gui', 'results',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.md', ''),
    ('shmoo-tool', 'object', 'gui', 'results',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25_Shmoo_Tool.md',
     '并入 setting-up-a-shmoo-test-with-the-shmoo-tool'),
    ('setup-management-tool', 'object', 'gui', 'project',
     '01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04_Setup_Management_Tool.md', ''),
    ('integrated-result-tool', 'object', 'gui', 'results',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13_Integrated_Result_Tool.md', ''),
    ('digital-pins-editor', 'object', 'gui', 'pin',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md', ''),
    ('stpm', 'object', 'gui', 'project',
     '02_System_reference/02.09_Test_Program_Management/02.09.02_SmarTest_Program_Manager.md', ''),
    # 文件 / 工具 / 概念
    ('model-file', 'object', 'file', 'project',
     '02_System_reference/02.04_Model_File_and_Licensing/02.04.01_The_model_file.md', ''),
    ('testflow-file', 'object', 'file', 'testflow',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.md', ''),
    ('stpm-control-file', 'object', 'file', 'project',
     '02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.md', ''),
    ('spec-set', 'object', 'L2', 'level',
     '02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.09_Spec_sets.md', ''),
    ('ganging', 'concept', 'n/a', 'pin',
     '02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.03_Ganging_utility_blocks.md', ''),
    ('execution-context', 'object', 'L2', 'run',
     '02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md', ''),
    ('sequencer', 'object', 'L1', 'pattern',
     '02_System_reference/02.06_Command_Reference/02.06.07.01.01.03_The_sequencer_program.md', ''),
    ('tpt-generate-device-dir', 'object', 'L2', 'project',
     '02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md', ''),

    # ================= A 组：语料里出现 ≥20 次、九个流程页提过却没链（41）=========
    ('dc-scale-xps256-card', 'object', 'n/a', 'pin',
     '02_System_reference/02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md', ''),
    ('dc-scale-uhc4t-card', 'object', 'n/a', 'pin',
     '02_System_reference/02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.md',
     '并入 dc-scale-uhc4-uhc4t-card（DUT 板侧那章）'),
    ('utility-card', 'object', 'n/a', 'pin',
     '02_System_reference/02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md', ''),
    ('dut-board-design-reference', 'concept', 'n/a', 'project',
     '02_System_reference/02.03_DUT_board_design_reference/02.03_DUT_board_design_reference.md', ''),
    ('utility-power-supplies', 'object', 'n/a', 'project',
     '02_System_reference/02.03_DUT_board_design_reference/02.03.05_Utility_power_supplies.md', ''),
    ('utility-pogo-block-utility-card-v93000-exa-scale-systems', 'object', 'n/a', 'project',
     '02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md', ''),
    ('direct-probe-stiffener', 'concept', 'n/a', 'project',
     '02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md', ''),
    ('layout-information-dut-board', 'concept', 'n/a', 'project',
     '02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.08_Layout_information__DUT_board.md', ''),
    ('technology-file-for-a-device', 'object', 'file', 'project',
     '01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md',
     '并入 technology-file'),
    ('global-section', 'object', 'file', 'project',
     '02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md', ''),
    ('edf-data-organization', 'concept', 'n/a', 'results',
     '02_System_reference/02.10_Data_Logging/02.10.01.06.01_EDF_data_organization.md', ''),
    ('edf-data-types', 'concept', 'n/a', 'results',
     '02_System_reference/02.10_Data_Logging/02.10.01.06.02_EDF_data_types.md', ''),
    ('data-logging-profiles', 'object', 'file', 'results',
     '02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.md', ''),
    ('structure-of-a-tmlimits-csv-file', 'object', 'file', 'testmethod',
     '02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.md',
     '并入 test-number-generator-and-tmlimits'),
    ('alphabetical-list-of-flags', 'object', 'L3', 'testmethod',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md', ''),
    ('special-test-suites', 'object', 'file', 'testflow',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.md', ''),
    ('command-reference', 'concept', 'n/a', 'project',
     '02_System_reference/02.06_Command_Reference/02.06_Command_Reference.md', ''),
    ('timing-setup-commands', 'concept', 'n/a', 'timing',
     '02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.md', ''),
    ('event-base', 'object', 'L3', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01_EVENT_BASE.md', ''),
    ('event-waveform-vfim', 'object', 'L3', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38_EVENT_WAVEFORM_VFIM.md',
     '和已有的 event-waveform-vfvm 是**两套**（63.38 / 63.39）'),
    ('dc-result-accessor', 'object', 'L3', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.04.01.28_DC_RESULT_ACCESSOR.md', ''),
    ('dps-power-flags-get-functions', 'object', 'L3', 'run',
     '02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06_DPS_power_flags_-_get...___functions.md', ''),
    ('spmu-pin-task-mode', 'object', 'L3', 'level',
     '02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.md', ''),
    ('smartcalc-framework', 'object', 'L3', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.md', ''),
    ('smartrdi', 'object', 'L3', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md',
     '并入 smartrdi-tmu-test-setup、setting-up-dc-scale-pins-with-smartrdi'),
    ('smartrdi-vector-and-protocol-programming', 'concept', 'n/a', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.13.24_SmartRDI__Vector_and_protocol_programming.md', ''),
    ('rdi-configure-file', 'object', 'file', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md', ''),
    ('dc-test-programming', 'concept', 'n/a', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.03.02_DC_Test_Programming.md', ''),
    ('controlling-multiple-sites', 'concept', 'n/a', 'run',
     '02_System_reference/02.07_Test_Method_Reference/02.07.03.13_Controlling_Multiple_Sites.md', ''),
    ('how-to-create-a-universal-test-method-class', 'concept', 'n/a', 'testmethod',
     '02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md', ''),
    ('equation-based-level-setup', 'concept', 'n/a', 'level',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02_Equation_based_level_setup.md', ''),
    ('dpspins-resources', 'object', 'L2', 'pin',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md', ''),
    ('protocol-editor', 'object', 'gui', 'pattern',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22_Protocol_editor.md', ''),
    ('test-summary-tab', 'object', 'gui', 'results',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.md', ''),
    ('setting-chart-display-options', 'concept', 'n/a', 'results',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.05_Setting_chart_display_options.md', ''),
    ('raw-data-views', 'object', 'gui', 'results',
     '02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.01_Raw_data_views.md', ''),
    ('mtp-memory-test', 'object', 'L2', 'pattern',
     '02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.md', ''),
    ('apg-pattern-file', 'object', 'file', 'pattern',
     '02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.md', ''),
    ('apg-program-file', 'object', 'file', 'pattern',
     '02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.md', ''),
    ('device-access-file', 'object', 'file', 'pattern',
     '02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04_Device_access_file.md', ''),
    ('pin-mapping-file', 'object', 'file', 'pattern',
     '02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06_Pin_mapping_file.md', ''),
]

COLS = ['slug', 'type', 'layer', 'stage', 'rel', 'status', 'note']


def _q(s):
    s = str(s)
    return f'"{s.replace(chr(34), chr(34) * 2)}"' if any(c in s for c in ',"') else s


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    write = '--write' in sys.argv

    docs = {}
    for line in (OUT / 'docs.jsonl').open(encoding='utf-8'):
        d = json.loads(line)
        docs[d['rel']] = d

    slugs = [r[0] for r in R]
    dup = {s for s in slugs if slugs.count(s) > 1}
    if dup:
        raise SystemExit(f'❌ 表里自己撞了 slug：{dup}')
    bad = [r for r in R if r[4] not in docs]
    if bad:
        for r in bad:
            print(f'❌ rel 不在语料索引里：{r[0]} → {r[4]}')
        raise SystemExit(f'❌ {len(bad)} 行的 rel 查不到——**先查清，不许建**')
    wrong = [r for r in R if r[3] not in
             ('level', 'pin', 'pattern', 'project', 'results', 'run', 'testflow',
              'testmethod', 'timing')]
    if wrong:
        raise SystemExit(f'❌ stage 不是九页之一：{[r[0] for r in wrong]}')

    raw = PLAN.read_bytes()
    nl = '\r\n' if b'\r\n' in raw else '\n'
    lines = [l.rstrip('\r') for l in raw.decode('utf-8').split('\n')]
    header = next(l for l in lines if l.startswith('slug,'))
    i = lines.index(header)
    comments = [l for l in lines[i + 1:] if l.startswith('#')]
    data = [l for l in lines[i + 1:]
            if l.strip() and not l.startswith('#')]
    have = {next(csv.reader([l]))[0] for l in data}

    new = [r for r in R if r[0] not in have]
    skip = [r for r in R if r[0] in have]
    if skip:
        print(f'⏭  已在表里，不重复加：{[r[0] for r in skip]}')

    for r in new:
        d = docs[r[4]]
        t = (d.get('frontmatter') or {}).get('title') or ''
        print(f'  + {r[0]:52s} {r[1]:9s} {r[2]:4s} {r[3]:10s} '
              f'{d["rel"][:56]:56s} | {t[:44]}')

    print(f'\n要加 {len(new)} 行（合并后共 {len(new) + len(have)} 行）；'
          f'另有 {len(FOLDED)} 行决定**不单独建**：')
    for k, (tgt, why) in FOLDED.items():
        print(f'  ⊘ {k:46s} → [[{tgt}]]  （{why}）')

    if not write:
        print('\n（只看，没写。加 --write 才写。）')
        return
    out = [header] + comments
    out += data
    out += [','.join(_q(v) for v in
                     (r[0], r[1], r[2], r[3], r[4], 'todo', r[5])) for r in new]
    PLAN.write_text(nl.join(out).rstrip(nl) + nl, encoding='utf-8', newline='')
    back = PLAN.read_bytes()
    if b'\r\r\n' in back:
        raise SystemExit('❌ 写出 `\\r\\r\\n`——行尾翻译没关掉')
    print(f'✅ 已写入 {PLAN.name}（共 {len(out) - len(comments) - 1} 行数据，'
          f'行尾 {"CRLF" if nl == chr(13) + chr(10) else "LF"}）')
    print('   下一步：python -X utf8 extract/plan_sync.py --write   # 对齐 status')


if __name__ == '__main__':
    main()
