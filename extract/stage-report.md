# 页面格式与出处对账报告

对象：**`wiki/` 下各类型页面**（范围与跳过项由**每一类自己的开头**写明）。依据：`schema.md` §2 / §5 / §6 / §9 / §11。

> **本文件覆盖十五类检查**，其中 `stages/*.md` 只是**第一类**的对象。标题里原先写的「九页」是本文件出生时的范围，早就不是了。
> **退出码是有意义的**：参与总闸的那几类里只要有一类红，进程就非 0 退出（第八、十类标着「— 记录」，不参与）。**这条 2026-09-18 才补上**——在此之前退出码**永远是 0**，而它看起来像「表是绿的」。

## 第一类 · 九页齐不齐、十节齐不齐


| stage | 字节 | 小节数 | 缺 | 声明「文档未覆盖」的小节 |
|---|---|---|---|---|
| `project` | 30,990 | 10 | 0 | 3 |
| `pin` | 23,994 | 10 | 0 | 2 |
| `level` | 27,871 | 10 | 0 | 1 |
| `timing` | 22,743 | 10 | 0 | 1 |
| `pattern` | 16,527 | 10 | 0 | 0 |
| `testmethod` | 27,400 | 10 | 0 | 1 |
| `testflow` | 22,439 | 10 | 0 | 2 |
| `run` | 41,338 | 10 | 0 | 1 |
| `results` | 32,606 | 10 | 0 | 3 |

## 第二类 · frontmatter 必填字段

| stage | type | title | tags | related | sources | created | updated | verified |
|---|---|---|---|---|---|---|---|---|
| `project` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `pin` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `level` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `timing` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `pattern` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `testmethod` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `testflow` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `run` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `results` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

`type` 必须 `stage`、`verified` 必须 `doc-only`（是否上机验证过只有人能改，见 `schema.md` §6）。

### 第二类续 · `stages/` 以外各页（`objects/` `concepts/` …）

| 页 | type | title | tags | related | sources | created | updated | verified |
|---|---|---|---|---|---|---|---|---|
| `concepts/command-reference.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/context-pins.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/controlling-multiple-sites.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/dc-test-programming.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/direct-probe-stiffener.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/dut-board-design-reference.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/dut-board-grounding.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/dut-interface-layout.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/edf-data-organization.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/edf-data-types.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/edf.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/equation-based-level-setup.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/flag.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/ganging.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/gpib-lan-communication-conventions.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/how-to-create-a-universal-test-method-class.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/hv-protection.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/inter-layer-via-design.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/layout-information-dut-board.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/logical-boards.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/offline-result-emulation.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/pogo-block-compatibility.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/pogo-pad-and-via-design.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/sequencer-controlled-utility-lines.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/setting-chart-display-options.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/setting-up-a-shmoo-test-with-the-shmoo-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/setting-up-dc-scale-pins-with-smartrdi.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/smartrdi-tmu-test-setup.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/smartrdi-vector-and-protocol-programming.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/test-number-generator-and-tmlimits.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/timing-setup-commands.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/utility-lines.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `concepts/waveform-set.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/constraint-level-mode-context-match.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/constraint-timing-mode-context-match.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/cross-card-ganging-requires-ddic.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/execution-context-requires-firmware-definition.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/label-edit-requires-tstl-selection.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/pals-before-other-setup.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/pin-config-locked-during-test.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/pin-config-requires-sequencer-off.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/rdi-call-requires-begin-end-block.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/referenced-set-requires-prior-definition.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/site-focus-required-before-command.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/smc-background-process-locks-config.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/synchronized-pins-require-same-test-processor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `constraints/testname-requires-matching-limits.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `errors/error-data-queue-empty.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `errors/error-flexlm-license-codes.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `errors/error-model-file-rejected-at-startup.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `errors/error-result-server-transmission-timeout.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `errors/error-utility-power-supply-not-enabled.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `errors/error-workspace-in-use.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-level.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-pattern.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-pin.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-project.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-results.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-run.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-testflow.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-testmethod.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-timing.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/add-limit.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/alias-set-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/alphabetical-list-of-flags.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/analysis-views.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/apg-pattern-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/apg-program-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/aprm.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/assign-value-node.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/begin-extension.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/bin.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/built-in-functions.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/bwdf.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/bwds.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/cct-change-level-spec.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/cct-multiport-sequencer-synchronizer-api.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/change-device-wizard.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/chin.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/ci-cpi.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/clkr.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/clmp.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/conf.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/connect.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/ctxt.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/data-logging-profile-api.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/data-logging-profiles.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/data-navigation-views.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/data-retrieval-library.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dc-result-accessor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dc-scale-limits-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dc-scale-uhc4t-card.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dc-scale-xps256-card.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dcdt.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/debug-perspective.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/debug-view.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/device-access-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/device-architecture-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/device-directory.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/device-license-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/device-summary-tab.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/device-technology-directory.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dfge.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dfgp.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dfpc.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dfpn.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dfpr.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dfps.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dfpt.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dfup.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dfut.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/digital-capture-test.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/digital-offset-search-pins.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/digital-pins-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/disconnect.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dprl.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dprt.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-aux-pin-task.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-aux-task.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-pins-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-power-flags-get-functions.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-task.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dps128-dps64-cards.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dpspins-resources.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/drlv.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dscp.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dsus.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/dtcp.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/edl-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/edsp.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/end-extension.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/eqfs.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/eqsp.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/error-map-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/error-map.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/etds.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/etim.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/event-base.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/event-formatter.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/event-value-double.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/event-value-int.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/event-waveform-vfim.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/event-waveform-vfvm.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/execution-context.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/file-string.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/flags-page.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/flex-relay.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/flow-data-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/flow-sequence-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/flsh.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/flush.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/for-each-site-begin.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/for-each-site-end.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/fw-task.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/gctx.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/get-functional-result.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/get-utility-lines.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/global-section.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/ground-sense-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/group-node.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/hardware-bin-summary-tab.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/hardware-response-emulator.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/hardware-view.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/hidden-upload.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/hw-pin-state.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/hw-state.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/hwty.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/index-objects.md` | ✅ | ✅ | ✅ | — 豁免 | — 豁免 | ✅ | ✅ | ✅ |
| `objects/integrated-result-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/jrst.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/jscf.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/jsdf.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/jspr.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/jsud.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/jswf.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/level-equation-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/level-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/level-master-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/level-set-selector.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/level-setup-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/level-spec.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/limit.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/lot-summary-generator.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/lsus.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/lsux.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/match-loops.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/model-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/mscf.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/msdf.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/mtp-maintenance-operations.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/mtp-memory-test.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/mtp-shared-test-commands.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/mtpt.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/multiport-burst-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/new-device-wizard.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/on-first-invocation-begin.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/on-first-invocation-end.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/option-list.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pact.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pals.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-controller.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-explorer.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-master-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-object.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pclk.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pdiv.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pfnd.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-configuration-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-configuration-master-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-configuration-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-group-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-mapping-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-property-monitor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-string.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-utility.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/play-pattern.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pogocabling-section.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/port-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pqfc.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/preprocessing-and-postprocessing-scripts.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/primary-status.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/prlt.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/project-explorer-view.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/protocol-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/psas.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/psfc.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pslv.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pssl.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pssr.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/pste.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/raw-data-views.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/rclv.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/rdi-configure-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/report-window.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/result-configuration.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/rset.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/run-dialog.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/sequencer-status.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/sequencer.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/set-utility-lines.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/setup-level-set-0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/setup-management-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/setup-perspective.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/shared-continuity-test.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/sharing-configuration-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/sharing-configuration.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/shmoo-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/signal-analyzer.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/site-control-window.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/sldo.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/smartcalc-framework.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/smartcalc.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/smartest-data-formatter.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/smartrdi.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/smartshell.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/smc-synchronize.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/smc-test.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/software-bin-summary-tab.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-search.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-set.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-value.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-variable.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/special-test-suites.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/spmu-pin-task-mode.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/spmu-pin-task.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/spmu-task.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/sprm.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/spst.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/sqst.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/stdf.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/stme.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/stpm-control-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/stpm-merge-rules-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/stpm.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/strs.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/structure-of-a-tmlimits-csv-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/svlr.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/table-filter.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/task-list.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/technology-file-for-a-device.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/term.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/test-method-class.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/test-program-explorer.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/test-suite-control-api.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/test-suite.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/test-suites-page.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/test-summary-tab.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/test.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-analyzer-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-master-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-properties-view.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-variable.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/testset-testname.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/testset.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/timestamp-attr-type.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-diagram-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-equation-set.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-master-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-set-selector.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-setup-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-spec.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-specification.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/tmlimits.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/tp360.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/tpi-program-routines.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/tpt-generate-device-dir.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/tpt-import-from-device.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/tsus.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/tsux.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/udef.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/udgp.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/udpr.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/udps.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/udpt.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/udup.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/udut.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/udvp.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/universal-test-method-library.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/upas.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/uptd.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-card.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-line-assignments.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-line-view.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-pins-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-pogo-block-utility-card-v93000-exa-scale-systems.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-power-supplies.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-purpose-editor.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/vclk.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/vdcg.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/vec-events.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/vector-setup-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/vpin.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/vtim.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/vwfg.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/vwfs.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/wafer-summary-tab.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/wave.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/waveform-mapping.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/waveform-view.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/wavetable-file.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/wavetable.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/wfds.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/wsus.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/xps256-pmu-operating-mode.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/xps256-programming-dps-operating-mode.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `objects/xps256-status-flags.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/index-versions.md` | ✅ | ✅ | ✅ | — 豁免 | — 豁免 | ✅ | ✅ | ✅ |
| `versions/mtp-2.4.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-2.4.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-2.6.5.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-2.6.6.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.0.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.0.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.0.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.1.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.1.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.1.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.1.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.1.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.1.5.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.1.6.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.1.7.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.2.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.2.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.2.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.3.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.3.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.3.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.3.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.4.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.4.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-3.4.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-7.5.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-7.5.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/mtp-7.6.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-2.4.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-2.5.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-6.3.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-6.3.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-6.3.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-6.3.5.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-6.5.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-6.5.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-6.5.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-6.5.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-6.5.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.0.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.0.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.0.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.0.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.1.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.1.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.1.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.1.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.1.4.5.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.1.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.10.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.10.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.10.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.10.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.2.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.2.1.5.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.2.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.2.2.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.2.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.2.3.9.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.2.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.3.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.3.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.3.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.3.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.3.4.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.3.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.4.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.4.1.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.4.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.4.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.4.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.4.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.4.5.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.5.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.5.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.5.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.5.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.5.4.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.5.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.50.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.6.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.6.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-7.6.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.0.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.0.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.0.7.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.0.8.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.1.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.1.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.1.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.1.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.1.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.2.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.2.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.2.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.2.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.2.5.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.3.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.3.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.3.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.3.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.3.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.3.5.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.4.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.4.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.4.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.4.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.4.4.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.4.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartest-8.5.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartprod-0.1.0-14.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartprod-0.1.0-17.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.1.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.2.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.3.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.3.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.3.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.4.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.4.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.4.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.4.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.4.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.4.5.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.5.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-2.5.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.10.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.10.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.10.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.4.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.5.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.5.1.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.5.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.5.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.5.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/smartrdi-7.6.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/tp360-3.10.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/tp360-3.10.3.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/tp360-3.10.4.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/tp360-3.8.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/tp360-3.9.0.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/tp360-7.2.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `versions/tp360-7.3.2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
    - ℹ️ `objects/index-objects.md`：`sources` / `related` **豁免**（§7 子索引）。**逐批手写**（钩子直接写在条目里；`index_rebuild.py` 的 `OBJ_HOOK` 只是2026-09-18 那一次迁移的输入，**那份脚本已跑完、不要重跑**）——**没有渲染器，所以做不到逐字节对账**；替换判据 = **第十四类甲：子索引列出的页 ↔ 目录里的页互为子集**
    - ℹ️ `versions/index-versions.md`：`sources` / `related` **豁免**（§7 子索引）。由 `extract/versions.py` 的 `render_index()` 生成；替换判据 = **与它的产出逐字节一致**（第十三类甲之二）

| 页 | `type` | 目录对不对 | `layer` | `stage` |
|---|---|---|---|---|
| `concepts/command-reference.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/context-pins.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/controlling-multiple-sites.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/dc-test-programming.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/direct-probe-stiffener.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/dut-board-design-reference.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/dut-board-grounding.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/dut-interface-layout.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/edf-data-organization.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/edf-data-types.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/edf.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/equation-based-level-setup.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/flag.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/ganging.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/gpib-lan-communication-conventions.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/how-to-create-a-universal-test-method-class.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/hv-protection.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/inter-layer-via-design.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/layout-information-dut-board.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/logical-boards.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/offline-result-emulation.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/pogo-block-compatibility.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/pogo-pad-and-via-design.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/sequencer-controlled-utility-lines.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/setting-chart-display-options.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/setting-up-a-shmoo-test-with-the-shmoo-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/setting-up-dc-scale-pins-with-smartrdi.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/smartrdi-tmu-test-setup.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/smartrdi-vector-and-protocol-programming.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/test-number-generator-and-tmlimits.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/timing-setup-commands.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/utility-lines.md` | ✅ | ✅ | ✅ | ✅ |
| `concepts/waveform-set.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/constraint-level-mode-context-match.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/constraint-timing-mode-context-match.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/cross-card-ganging-requires-ddic.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/execution-context-requires-firmware-definition.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/label-edit-requires-tstl-selection.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/pals-before-other-setup.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/pin-config-locked-during-test.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/pin-config-requires-sequencer-off.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/rdi-call-requires-begin-end-block.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/referenced-set-requires-prior-definition.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/site-focus-required-before-command.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/smc-background-process-locks-config.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/synchronized-pins-require-same-test-processor.md` | ✅ | ✅ | ✅ | ✅ |
| `constraints/testname-requires-matching-limits.md` | ✅ | ✅ | ✅ | ✅ |
| `errors/error-data-queue-empty.md` | ✅ | ✅ | — 未带 | — 未带 |
| `errors/error-flexlm-license-codes.md` | ✅ | ✅ | — 未带 | — 未带 |
| `errors/error-model-file-rejected-at-startup.md` | ✅ | ✅ | — 未带 | — 未带 |
| `errors/error-result-server-transmission-timeout.md` | ✅ | ✅ | — 未带 | — 未带 |
| `errors/error-utility-power-supply-not-enabled.md` | ✅ | ✅ | — 未带 | — 未带 |
| `errors/error-workspace-in-use.md` | ✅ | ✅ | — 未带 | — 未带 |
| `mappings/mapping-level.md` | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-pattern.md` | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-pin.md` | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-project.md` | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-results.md` | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-run.md` | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-testflow.md` | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-testmethod.md` | ✅ | ✅ | ✅ | ✅ |
| `mappings/mapping-timing.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/add-limit.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/alias-set-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/alphabetical-list-of-flags.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/analysis-views.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/apg-pattern-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/apg-program-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/aprm.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/assign-value-node.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/begin-extension.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/bin.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/built-in-functions.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/bwdf.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/bwds.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/cct-change-level-spec.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/cct-multiport-sequencer-synchronizer-api.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/change-device-wizard.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/chin.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/ci-cpi.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/clkr.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/clmp.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/conf.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/connect.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/ctxt.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/data-logging-profile-api.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/data-logging-profiles.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/data-navigation-views.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/data-retrieval-library.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dc-result-accessor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dc-scale-limits-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dc-scale-uhc4t-card.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dc-scale-xps256-card.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dcdt.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/debug-perspective.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/debug-view.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/device-access-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/device-architecture-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/device-directory.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/device-license-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/device-summary-tab.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/device-technology-directory.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dfge.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dfgp.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dfpc.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dfpn.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dfpr.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dfps.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dfpt.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dfup.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dfut.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/digital-capture-test.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/digital-offset-search-pins.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/digital-pins-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/disconnect.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dprl.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dprt.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-aux-pin-task.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-aux-task.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-pins-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-power-flags-get-functions.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dps-task.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dps128-dps64-cards.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dpspins-resources.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/drlv.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dscp.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dsus.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/dtcp.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/edl-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/edsp.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/end-extension.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/eqfs.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/eqsp.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/error-map-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/error-map.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/etds.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/etim.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/event-base.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/event-formatter.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/event-value-double.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/event-value-int.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/event-waveform-vfim.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/event-waveform-vfvm.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/execution-context.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/file-string.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/flags-page.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/flex-relay.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/flow-data-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/flow-sequence-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/flsh.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/flush.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/for-each-site-begin.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/for-each-site-end.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/fw-task.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/gctx.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/get-functional-result.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/get-utility-lines.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/global-section.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/ground-sense-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/group-node.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/hardware-bin-summary-tab.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/hardware-response-emulator.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/hardware-view.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/hidden-upload.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/hw-pin-state.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/hw-state.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/hwty.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/index-objects.md` | ✅ | ✅ | ✅ | — 豁免 |
| `objects/integrated-result-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/jrst.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/jscf.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/jsdf.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/jspr.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/jsud.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/jswf.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/level-equation-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/level-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/level-master-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/level-set-selector.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/level-setup-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/level-spec.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/limit.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/lot-summary-generator.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/lsus.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/lsux.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/match-loops.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/model-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/mscf.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/msdf.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/mtp-maintenance-operations.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/mtp-memory-test.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/mtp-shared-test-commands.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/mtpt.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/multiport-burst-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/new-device-wizard.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/on-first-invocation-begin.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/on-first-invocation-end.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/option-list.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pact.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pals.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-controller.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-explorer.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-master-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-object.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pattern-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pclk.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pdiv.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pfnd.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-configuration-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-configuration-master-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-configuration-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-group-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-mapping-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-property-monitor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-string.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pin-utility.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/play-pattern.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pogocabling-section.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/port-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pqfc.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/preprocessing-and-postprocessing-scripts.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/primary-status.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/prlt.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/project-explorer-view.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/protocol-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/psas.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/psfc.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pslv.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pssl.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pssr.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/pste.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/raw-data-views.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/rclv.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/rdi-configure-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/report-window.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/result-configuration.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/rset.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/run-dialog.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/sequencer-status.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/sequencer.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/set-utility-lines.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/setup-level-set-0.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/setup-management-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/setup-perspective.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/shared-continuity-test.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/sharing-configuration-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/sharing-configuration.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/shmoo-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/signal-analyzer.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/site-control-window.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/sldo.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/smartcalc-framework.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/smartcalc.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/smartest-data-formatter.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/smartrdi.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/smartshell.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/smc-synchronize.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/smc-test.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/software-bin-summary-tab.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-search.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-set.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-value.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/spec-variable.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/special-test-suites.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/spmu-pin-task-mode.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/spmu-pin-task.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/spmu-task.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/sprm.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/spst.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/sqst.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/stdf.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/stme.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/stpm-control-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/stpm-merge-rules-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/stpm.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/strs.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/structure-of-a-tmlimits-csv-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/svlr.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/table-filter.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/task-list.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/technology-file-for-a-device.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/term.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/test-method-class.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/test-program-explorer.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/test-suite-control-api.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/test-suite.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/test-suites-page.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/test-summary-tab.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/test.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-analyzer-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-master-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-properties-view.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/testflow-variable.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/testset-testname.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/testset.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/timestamp-attr-type.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-diagram-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-equation-set.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-master-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-set-selector.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-setup-tool.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-spec.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/timing-specification.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/tmlimits.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/tp360.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/tpi-program-routines.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/tpt-generate-device-dir.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/tpt-import-from-device.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/tsus.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/tsux.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/udef.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/udgp.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/udpr.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/udps.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/udpt.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/udup.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/udut.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/udvp.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/universal-test-method-library.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/upas.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/uptd.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-card.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-line-assignments.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-line-view.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-pins-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-pogo-block-utility-card-v93000-exa-scale-systems.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-power-supplies.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/utility-purpose-editor.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/vclk.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/vdcg.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/vec-events.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/vector-setup-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/vpin.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/vtim.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/vwfg.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/vwfs.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/wafer-summary-tab.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/wave.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/waveform-mapping.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/waveform-view.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/wavetable-file.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/wavetable.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/wfds.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/wsus.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/xps256-pmu-operating-mode.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/xps256-programming-dps-operating-mode.md` | ✅ | ✅ | ✅ | ✅ |
| `objects/xps256-status-flags.md` | ✅ | ✅ | ✅ | ✅ |
| `versions/index-versions.md` | ✅ | ✅ | — 未带 | — 豁免 |
| `versions/mtp-2.4.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-2.4.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-2.6.5.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-2.6.6.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.0.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.0.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.0.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.1.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.1.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.1.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.1.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.1.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.1.5.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.1.6.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.1.7.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.2.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.2.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.2.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.3.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.3.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.3.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.3.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.4.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.4.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-3.4.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-7.5.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-7.5.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/mtp-7.6.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-2.4.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-2.5.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-6.3.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-6.3.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-6.3.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-6.3.5.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-6.5.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-6.5.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-6.5.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-6.5.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-6.5.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.0.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.0.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.0.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.0.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.1.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.1.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.1.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.1.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.1.4.5.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.1.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.10.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.10.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.10.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.10.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.2.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.2.1.5.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.2.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.2.2.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.2.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.2.3.9.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.2.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.3.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.3.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.3.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.3.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.3.4.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.3.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.4.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.4.1.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.4.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.4.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.4.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.4.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.4.5.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.5.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.5.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.5.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.5.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.5.4.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.5.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.50.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.6.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.6.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-7.6.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.0.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.0.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.0.7.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.0.8.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.1.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.1.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.1.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.1.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.1.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.2.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.2.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.2.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.2.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.2.5.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.3.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.3.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.3.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.3.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.3.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.3.5.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.4.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.4.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.4.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.4.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.4.4.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.4.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartest-8.5.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartprod-0.1.0-14.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartprod-0.1.0-17.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.1.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.2.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.3.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.3.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.3.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.4.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.4.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.4.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.4.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.4.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.4.5.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.5.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-2.5.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.10.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.10.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.10.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.4.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.5.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.5.1.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.5.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.5.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.5.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/smartrdi-7.6.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/tp360-3.10.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/tp360-3.10.3.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/tp360-3.10.4.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/tp360-3.8.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/tp360-3.9.0.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/tp360-7.2.2.md` | ✅ | ✅ | — 未带 | — 未带 |
| `versions/tp360-7.3.2.md` | ✅ | ✅ | — 未带 | — 未带 |

`layer` 合法值：`L1` / `L2` / `L3` / `file` / `gui` / `n/a`（§2 那六层）。
`stage` 合法值：九段之一。**`layer`/`stage` 对 `object`/`constraint`/`mapping` 是必填**，其余类型带了就得合法。

> **`stage` 该填什么，建了这一批才有个真问题**：§12 允许为**不属于任何一段流程**的对象建页（判据是入度），可 §6 又要求 `stage` 必填。
> 处置：**填「最近的一段」，并在页内写明这是「最近」不是「归属」**。
> 理由：这个字段的用处是「读者该去哪一段里找它的用法」，填最近的一段对这个用处是对的；
> 而把「归属」写成字段会把**没人要它**的东西伪装成某一环的正式成员。

## 第三类 · `sources:` 可追溯（**抓幻觉**）

每条来源路径逐个查语料。**不存在的路径 = 编的**，一个都不许放过。

- ✅ `project` — 64 条来源
- ✅ `pin` — 112 条来源
- ✅ `level` — 100 条来源
- ✅ `timing` — 72 条来源
- ✅ `pattern` — 102 条来源
- ✅ `testmethod` — 38 条来源
- ✅ `testflow` — 71 条来源
- ✅ `run` — 64 条来源
- ✅ `results` — 54 条来源

阶段页合计 677 条来源路径。

### 第三类续 · `stages/` 以外 495 页

- ✅ `concepts/command-reference.md` — 1 条来源
- ✅ `concepts/context-pins.md` — 1 条来源
- ✅ `concepts/controlling-multiple-sites.md` — 1 条来源
- ✅ `concepts/dc-test-programming.md` — 1 条来源
- ✅ `concepts/direct-probe-stiffener.md` — 1 条来源
- ✅ `concepts/dut-board-design-reference.md` — 1 条来源
- ✅ `concepts/dut-board-grounding.md` — 1 条来源
- ✅ `concepts/dut-interface-layout.md` — 1 条来源
- ✅ `concepts/edf-data-organization.md` — 1 条来源
- ✅ `concepts/edf-data-types.md` — 1 条来源
- ✅ `concepts/edf.md` — 1 条来源
- ✅ `concepts/equation-based-level-setup.md` — 1 条来源
- ✅ `concepts/flag.md` — 1 条来源
- ✅ `concepts/ganging.md` — 1 条来源
- ✅ `concepts/gpib-lan-communication-conventions.md` — 1 条来源
- ✅ `concepts/how-to-create-a-universal-test-method-class.md` — 1 条来源
- ✅ `concepts/hv-protection.md` — 11 条来源
- ✅ `concepts/inter-layer-via-design.md` — 1 条来源
- ✅ `concepts/layout-information-dut-board.md` — 1 条来源
- ✅ `concepts/logical-boards.md` — 1 条来源
- ✅ `concepts/offline-result-emulation.md` — 1 条来源
- ✅ `concepts/pogo-block-compatibility.md` — 1 条来源
- ✅ `concepts/pogo-pad-and-via-design.md` — 1 条来源
- ✅ `concepts/sequencer-controlled-utility-lines.md` — 1 条来源
- ✅ `concepts/setting-chart-display-options.md` — 1 条来源
- ✅ `concepts/setting-up-a-shmoo-test-with-the-shmoo-tool.md` — 1 条来源
- ✅ `concepts/setting-up-dc-scale-pins-with-smartrdi.md` — 1 条来源
- ✅ `concepts/smartrdi-tmu-test-setup.md` — 1 条来源
- ✅ `concepts/smartrdi-vector-and-protocol-programming.md` — 1 条来源
- ✅ `concepts/test-number-generator-and-tmlimits.md` — 1 条来源
- ✅ `concepts/timing-setup-commands.md` — 1 条来源
- ✅ `concepts/utility-lines.md` — 1 条来源
- ✅ `concepts/waveform-set.md` — 1 条来源
- ✅ `constraints/constraint-level-mode-context-match.md` — 3 条来源
- ✅ `constraints/constraint-timing-mode-context-match.md` — 2 条来源
- ✅ `constraints/cross-card-ganging-requires-ddic.md` — 4 条来源
- ✅ `constraints/execution-context-requires-firmware-definition.md` — 8 条来源
- ✅ `constraints/label-edit-requires-tstl-selection.md` — 10 条来源
- ✅ `constraints/pals-before-other-setup.md` — 1 条来源
- ✅ `constraints/pin-config-locked-during-test.md` — 2 条来源
- ✅ `constraints/pin-config-requires-sequencer-off.md` — 5 条来源
- ✅ `constraints/rdi-call-requires-begin-end-block.md` — 6 条来源
- ✅ `constraints/referenced-set-requires-prior-definition.md` — 9 条来源
- ✅ `constraints/site-focus-required-before-command.md` — 2 条来源
- ✅ `constraints/smc-background-process-locks-config.md` — 5 条来源
- ✅ `constraints/synchronized-pins-require-same-test-processor.md` — 10 条来源
- ✅ `constraints/testname-requires-matching-limits.md` — 7 条来源
- ✅ `errors/error-data-queue-empty.md` — 1 条来源
- ✅ `errors/error-flexlm-license-codes.md` — 3 条来源
- ✅ `errors/error-model-file-rejected-at-startup.md` — 6 条来源
- ✅ `errors/error-result-server-transmission-timeout.md` — 1 条来源
- ✅ `errors/error-utility-power-supply-not-enabled.md` — 1 条来源
- ✅ `errors/error-workspace-in-use.md` — 1 条来源
- ✅ `mappings/mapping-level.md` — 46 条来源
- ✅ `mappings/mapping-pattern.md` — 40 条来源
- ✅ `mappings/mapping-pin.md` — 7 条来源
- ✅ `mappings/mapping-project.md` — 32 条来源
- ✅ `mappings/mapping-results.md` — 24 条来源
- ✅ `mappings/mapping-run.md` — 36 条来源
- ✅ `mappings/mapping-testflow.md` — 42 条来源
- ✅ `mappings/mapping-testmethod.md` — 31 条来源
- ✅ `mappings/mapping-timing.md` — 68 条来源
- ✅ `objects/add-limit.md` — 1 条来源
- ✅ `objects/alias-set-editor.md` — 1 条来源
- ✅ `objects/alphabetical-list-of-flags.md` — 1 条来源
- ✅ `objects/analysis-views.md` — 1 条来源
- ✅ `objects/apg-pattern-file.md` — 1 条来源
- ✅ `objects/apg-program-file.md` — 1 条来源
- ✅ `objects/aprm.md` — 1 条来源
- ✅ `objects/assign-value-node.md` — 1 条来源
- ✅ `objects/begin-extension.md` — 1 条来源
- ✅ `objects/bin.md` — 1 条来源
- ✅ `objects/built-in-functions.md` — 1 条来源
- ✅ `objects/bwdf.md` — 1 条来源
- ✅ `objects/bwds.md` — 1 条来源
- ✅ `objects/cct-change-level-spec.md` — 1 条来源
- ✅ `objects/cct-multiport-sequencer-synchronizer-api.md` — 1 条来源
- ✅ `objects/change-device-wizard.md` — 1 条来源
- ✅ `objects/chin.md` — 1 条来源
- ✅ `objects/ci-cpi.md` — 3 条来源
- ✅ `objects/clkr.md` — 1 条来源
- ✅ `objects/clmp.md` — 1 条来源
- ✅ `objects/conf.md` — 1 条来源
- ✅ `objects/connect.md` — 1 条来源
- ✅ `objects/ctxt.md` — 1 条来源
- ✅ `objects/data-logging-profile-api.md` — 1 条来源
- ✅ `objects/data-logging-profiles.md` — 1 条来源
- ✅ `objects/data-navigation-views.md` — 1 条来源
- ✅ `objects/data-retrieval-library.md` — 1 条来源
- ✅ `objects/dc-result-accessor.md` — 1 条来源
- ✅ `objects/dc-scale-limits-editor.md` — 1 条来源
- ✅ `objects/dc-scale-uhc4t-card.md` — 1 条来源
- ✅ `objects/dc-scale-xps256-card.md` — 1 条来源
- ✅ `objects/dcdt.md` — 1 条来源
- ✅ `objects/debug-perspective.md` — 1 条来源
- ✅ `objects/debug-view.md` — 1 条来源
- ✅ `objects/device-access-file.md` — 1 条来源
- ✅ `objects/device-architecture-file.md` — 1 条来源
- ✅ `objects/device-directory.md` — 1 条来源
- ✅ `objects/device-license-file.md` — 1 条来源
- ✅ `objects/device-summary-tab.md` — 1 条来源
- ✅ `objects/device-technology-directory.md` — 1 条来源
- ✅ `objects/dfge.md` — 1 条来源
- ✅ `objects/dfgp.md` — 1 条来源
- ✅ `objects/dfpc.md` — 1 条来源
- ✅ `objects/dfpn.md` — 1 条来源
- ✅ `objects/dfpr.md` — 1 条来源
- ✅ `objects/dfps.md` — 1 条来源
- ✅ `objects/dfpt.md` — 1 条来源
- ✅ `objects/dfup.md` — 1 条来源
- ✅ `objects/dfut.md` — 1 条来源
- ✅ `objects/digital-capture-test.md` — 1 条来源
- ✅ `objects/digital-offset-search-pins.md` — 1 条来源
- ✅ `objects/digital-pins-editor.md` — 1 条来源
- ✅ `objects/disconnect.md` — 1 条来源
- ✅ `objects/dprl.md` — 1 条来源
- ✅ `objects/dprt.md` — 1 条来源
- ✅ `objects/dps-aux-pin-task.md` — 2 条来源
- ✅ `objects/dps-aux-task.md` — 1 条来源
- ✅ `objects/dps-pins-editor.md` — 1 条来源
- ✅ `objects/dps-power-flags-get-functions.md` — 1 条来源
- ✅ `objects/dps-task.md` — 1 条来源
- ✅ `objects/dps128-dps64-cards.md` — 5 条来源
- ✅ `objects/dpspins-resources.md` — 1 条来源
- ✅ `objects/drlv.md` — 1 条来源
- ✅ `objects/dscp.md` — 1 条来源
- ✅ `objects/dsus.md` — 1 条来源
- ✅ `objects/dtcp.md` — 1 条来源
- ✅ `objects/edl-file.md` — 1 条来源
- ✅ `objects/edsp.md` — 1 条来源
- ✅ `objects/end-extension.md` — 1 条来源
- ✅ `objects/eqfs.md` — 1 条来源
- ✅ `objects/eqsp.md` — 1 条来源
- ✅ `objects/error-map-tool.md` — 1 条来源
- ✅ `objects/error-map.md` — 1 条来源
- ✅ `objects/etds.md` — 1 条来源
- ✅ `objects/etim.md` — 1 条来源
- ✅ `objects/event-base.md` — 1 条来源
- ✅ `objects/event-formatter.md` — 1 条来源
- ✅ `objects/event-value-double.md` — 1 条来源
- ✅ `objects/event-value-int.md` — 1 条来源
- ✅ `objects/event-waveform-vfim.md` — 1 条来源
- ✅ `objects/event-waveform-vfvm.md` — 1 条来源
- ✅ `objects/execution-context.md` — 1 条来源
- ✅ `objects/file-string.md` — 1 条来源
- ✅ `objects/flags-page.md` — 1 条来源
- ✅ `objects/flex-relay.md` — 1 条来源
- ✅ `objects/flow-data-editor.md` — 1 条来源
- ✅ `objects/flow-sequence-editor.md` — 1 条来源
- ✅ `objects/flsh.md` — 1 条来源
- ✅ `objects/flush.md` — 1 条来源
- ✅ `objects/for-each-site-begin.md` — 1 条来源
- ✅ `objects/for-each-site-end.md` — 1 条来源
- ✅ `objects/fw-task.md` — 1 条来源
- ✅ `objects/gctx.md` — 1 条来源
- ✅ `objects/get-functional-result.md` — 1 条来源
- ✅ `objects/get-utility-lines.md` — 1 条来源
- ✅ `objects/global-section.md` — 1 条来源
- ✅ `objects/ground-sense-editor.md` — 1 条来源
- ✅ `objects/group-node.md` — 1 条来源
- ✅ `objects/hardware-bin-summary-tab.md` — 1 条来源
- ✅ `objects/hardware-response-emulator.md` — 1 条来源
- ✅ `objects/hardware-view.md` — 1 条来源
- ✅ `objects/hidden-upload.md` — 1 条来源
- ✅ `objects/hw-pin-state.md` — 1 条来源
- ✅ `objects/hw-state.md` — 1 条来源
- ✅ `objects/hwty.md` — 1 条来源
- ✅ `objects/index-objects.md` — 0 条来源
- ✅ `objects/integrated-result-tool.md` — 1 条来源
- ✅ `objects/jrst.md` — 1 条来源
- ✅ `objects/jscf.md` — 1 条来源
- ✅ `objects/jsdf.md` — 1 条来源
- ✅ `objects/jspr.md` — 1 条来源
- ✅ `objects/jsud.md` — 1 条来源
- ✅ `objects/jswf.md` — 1 条来源
- ✅ `objects/level-equation-file.md` — 1 条来源
- ✅ `objects/level-file.md` — 2 条来源
- ✅ `objects/level-master-file.md` — 2 条来源
- ✅ `objects/level-set-selector.md` — 1 条来源
- ✅ `objects/level-setup-tool.md` — 1 条来源
- ✅ `objects/level-spec.md` — 1 条来源
- ✅ `objects/limit.md` — 1 条来源
- ✅ `objects/lot-summary-generator.md` — 1 条来源
- ✅ `objects/lsus.md` — 1 条来源
- ✅ `objects/lsux.md` — 1 条来源
- ✅ `objects/match-loops.md` — 1 条来源
- ✅ `objects/model-file.md` — 1 条来源
- ✅ `objects/mscf.md` — 1 条来源
- ✅ `objects/msdf.md` — 1 条来源
- ✅ `objects/mtp-maintenance-operations.md` — 1 条来源
- ✅ `objects/mtp-memory-test.md` — 1 条来源
- ✅ `objects/mtp-shared-test-commands.md` — 3 条来源
- ✅ `objects/mtpt.md` — 1 条来源
- ✅ `objects/multiport-burst-editor.md` — 1 条来源
- ✅ `objects/new-device-wizard.md` — 1 条来源
- ✅ `objects/on-first-invocation-begin.md` — 1 条来源
- ✅ `objects/on-first-invocation-end.md` — 1 条来源
- ✅ `objects/option-list.md` — 1 条来源
- ✅ `objects/pact.md` — 1 条来源
- ✅ `objects/pals.md` — 1 条来源
- ✅ `objects/pattern-controller.md` — 1 条来源
- ✅ `objects/pattern-editor.md` — 1 条来源
- ✅ `objects/pattern-explorer.md` — 1 条来源
- ✅ `objects/pattern-master-file.md` — 1 条来源
- ✅ `objects/pattern-object.md` — 1 条来源
- ✅ `objects/pattern-tool.md` — 1 条来源
- ✅ `objects/pclk.md` — 1 条来源
- ✅ `objects/pdiv.md` — 1 条来源
- ✅ `objects/pfnd.md` — 1 条来源
- ✅ `objects/pin-configuration-file.md` — 2 条来源
- ✅ `objects/pin-configuration-master-file.md` — 1 条来源
- ✅ `objects/pin-configuration-tool.md` — 2 条来源
- ✅ `objects/pin-group-editor.md` — 3 条来源
- ✅ `objects/pin-mapping-file.md` — 1 条来源
- ✅ `objects/pin-property-monitor.md` — 1 条来源
- ✅ `objects/pin-string.md` — 1 条来源
- ✅ `objects/pin-utility.md` — 1 条来源
- ✅ `objects/play-pattern.md` — 1 条来源
- ✅ `objects/pogocabling-section.md` — 3 条来源
- ✅ `objects/port-editor.md` — 1 条来源
- ✅ `objects/pqfc.md` — 1 条来源
- ✅ `objects/preprocessing-and-postprocessing-scripts.md` — 1 条来源
- ✅ `objects/primary-status.md` — 1 条来源
- ✅ `objects/prlt.md` — 1 条来源
- ✅ `objects/project-explorer-view.md` — 1 条来源
- ✅ `objects/protocol-editor.md` — 1 条来源
- ✅ `objects/psas.md` — 1 条来源
- ✅ `objects/psfc.md` — 1 条来源
- ✅ `objects/pslv.md` — 1 条来源
- ✅ `objects/pssl.md` — 1 条来源
- ✅ `objects/pssr.md` — 1 条来源
- ✅ `objects/pste.md` — 1 条来源
- ✅ `objects/raw-data-views.md` — 1 条来源
- ✅ `objects/rclv.md` — 1 条来源
- ✅ `objects/rdi-configure-file.md` — 1 条来源
- ✅ `objects/report-window.md` — 1 条来源
- ✅ `objects/result-configuration.md` — 1 条来源
- ✅ `objects/rset.md` — 1 条来源
- ✅ `objects/run-dialog.md` — 1 条来源
- ✅ `objects/sequencer-status.md` — 1 条来源
- ✅ `objects/sequencer.md` — 1 条来源
- ✅ `objects/set-utility-lines.md` — 1 条来源
- ✅ `objects/setup-level-set-0.md` — 1 条来源
- ✅ `objects/setup-management-tool.md` — 1 条来源
- ✅ `objects/setup-perspective.md` — 1 条来源
- ✅ `objects/shared-continuity-test.md` — 1 条来源
- ✅ `objects/sharing-configuration-file.md` — 1 条来源
- ✅ `objects/sharing-configuration.md` — 2 条来源
- ✅ `objects/shmoo-tool.md` — 1 条来源
- ✅ `objects/signal-analyzer.md` — 1 条来源
- ✅ `objects/site-control-window.md` — 1 条来源
- ✅ `objects/sldo.md` — 1 条来源
- ✅ `objects/smartcalc-framework.md` — 1 条来源
- ✅ `objects/smartcalc.md` — 1 条来源
- ✅ `objects/smartest-data-formatter.md` — 1 条来源
- ✅ `objects/smartrdi.md` — 1 条来源
- ✅ `objects/smartshell.md` — 1 条来源
- ✅ `objects/smc-synchronize.md` — 1 条来源
- ✅ `objects/smc-test.md` — 1 条来源
- ✅ `objects/software-bin-summary-tab.md` — 1 条来源
- ✅ `objects/spec-search.md` — 1 条来源
- ✅ `objects/spec-set.md` — 1 条来源
- ✅ `objects/spec-tool.md` — 1 条来源
- ✅ `objects/spec-value.md` — 1 条来源
- ✅ `objects/spec-variable.md` — 1 条来源
- ✅ `objects/special-test-suites.md` — 1 条来源
- ✅ `objects/spmu-pin-task-mode.md` — 1 条来源
- ✅ `objects/spmu-pin-task.md` — 1 条来源
- ✅ `objects/spmu-task.md` — 1 条来源
- ✅ `objects/sprm.md` — 1 条来源
- ✅ `objects/spst.md` — 1 条来源
- ✅ `objects/sqst.md` — 1 条来源
- ✅ `objects/stdf.md` — 1 条来源
- ✅ `objects/stme.md` — 1 条来源
- ✅ `objects/stpm-control-file.md` — 1 条来源
- ✅ `objects/stpm-merge-rules-file.md` — 1 条来源
- ✅ `objects/stpm.md` — 1 条来源
- ✅ `objects/strs.md` — 1 条来源
- ✅ `objects/structure-of-a-tmlimits-csv-file.md` — 1 条来源
- ✅ `objects/svlr.md` — 1 条来源
- ✅ `objects/table-filter.md` — 1 条来源
- ✅ `objects/task-list.md` — 1 条来源
- ✅ `objects/technology-file-for-a-device.md` — 1 条来源
- ✅ `objects/term.md` — 1 条来源
- ✅ `objects/test-method-class.md` — 1 条来源
- ✅ `objects/test-program-explorer.md` — 1 条来源
- ✅ `objects/test-suite-control-api.md` — 1 条来源
- ✅ `objects/test-suite.md` — 1 条来源
- ✅ `objects/test-suites-page.md` — 1 条来源
- ✅ `objects/test-summary-tab.md` — 1 条来源
- ✅ `objects/test.md` — 1 条来源
- ✅ `objects/testflow-analyzer-tool.md` — 1 条来源
- ✅ `objects/testflow-file.md` — 1 条来源
- ✅ `objects/testflow-master-file.md` — 1 条来源
- ✅ `objects/testflow-properties-view.md` — 1 条来源
- ✅ `objects/testflow-tool.md` — 1 条来源
- ✅ `objects/testflow-variable.md` — 1 条来源
- ✅ `objects/testset-testname.md` — 1 条来源
- ✅ `objects/testset.md` — 1 条来源
- ✅ `objects/timestamp-attr-type.md` — 1 条来源
- ✅ `objects/timing-diagram-tool.md` — 1 条来源
- ✅ `objects/timing-equation-set.md` — 1 条来源
- ✅ `objects/timing-file.md` — 2 条来源
- ✅ `objects/timing-master-file.md` — 1 条来源
- ✅ `objects/timing-set-selector.md` — 1 条来源
- ✅ `objects/timing-setup-tool.md` — 1 条来源
- ✅ `objects/timing-spec.md` — 1 条来源
- ✅ `objects/timing-specification.md` — 1 条来源
- ✅ `objects/tmlimits.md` — 1 条来源
- ✅ `objects/tp360.md` — 1 条来源
- ✅ `objects/tpi-program-routines.md` — 1 条来源
- ✅ `objects/tpt-generate-device-dir.md` — 1 条来源
- ✅ `objects/tpt-import-from-device.md` — 1 条来源
- ✅ `objects/tsus.md` — 1 条来源
- ✅ `objects/tsux.md` — 1 条来源
- ✅ `objects/udef.md` — 1 条来源
- ✅ `objects/udgp.md` — 1 条来源
- ✅ `objects/udpr.md` — 1 条来源
- ✅ `objects/udps.md` — 1 条来源
- ✅ `objects/udpt.md` — 1 条来源
- ✅ `objects/udup.md` — 1 条来源
- ✅ `objects/udut.md` — 1 条来源
- ✅ `objects/udvp.md` — 1 条来源
- ✅ `objects/universal-test-method-library.md` — 1 条来源
- ✅ `objects/upas.md` — 1 条来源
- ✅ `objects/uptd.md` — 1 条来源
- ✅ `objects/utility-card.md` — 1 条来源
- ✅ `objects/utility-line-assignments.md` — 4 条来源
- ✅ `objects/utility-line-view.md` — 1 条来源
- ✅ `objects/utility-pins-editor.md` — 1 条来源
- ✅ `objects/utility-pogo-block-utility-card-v93000-exa-scale-systems.md` — 1 条来源
- ✅ `objects/utility-power-supplies.md` — 1 条来源
- ✅ `objects/utility-purpose-editor.md` — 1 条来源
- ✅ `objects/vclk.md` — 1 条来源
- ✅ `objects/vdcg.md` — 1 条来源
- ✅ `objects/vec-events.md` — 1 条来源
- ✅ `objects/vector-setup-file.md` — 2 条来源
- ✅ `objects/vpin.md` — 1 条来源
- ✅ `objects/vtim.md` — 1 条来源
- ✅ `objects/vwfg.md` — 1 条来源
- ✅ `objects/vwfs.md` — 1 条来源
- ✅ `objects/wafer-summary-tab.md` — 1 条来源
- ✅ `objects/wave.md` — 1 条来源
- ✅ `objects/waveform-mapping.md` — 1 条来源
- ✅ `objects/waveform-view.md` — 1 条来源
- ✅ `objects/wavetable-file.md` — 1 条来源
- ✅ `objects/wavetable.md` — 1 条来源
- ✅ `objects/wfds.md` — 1 条来源
- ✅ `objects/wsus.md` — 1 条来源
- ✅ `objects/xps256-pmu-operating-mode.md` — 1 条来源
- ✅ `objects/xps256-programming-dps-operating-mode.md` — 1 条来源
- ✅ `objects/xps256-status-flags.md` — 1 条来源
- ✅ `versions/index-versions.md` — 0 条来源
- ✅ `versions/mtp-2.4.0.md` — 17 条来源
- ✅ `versions/mtp-2.4.2.md` — 6 条来源
- ✅ `versions/mtp-2.6.5.md` — 21 条来源
- ✅ `versions/mtp-2.6.6.md` — 9 条来源
- ✅ `versions/mtp-3.0.1.md` — 30 条来源
- ✅ `versions/mtp-3.0.3.md` — 30 条来源
- ✅ `versions/mtp-3.0.4.md` — 4 条来源
- ✅ `versions/mtp-3.1.0.md` — 2 条来源
- ✅ `versions/mtp-3.1.1.md` — 8 条来源
- ✅ `versions/mtp-3.1.2.md` — 1 条来源
- ✅ `versions/mtp-3.1.3.md` — 30 条来源
- ✅ `versions/mtp-3.1.4.md` — 24 条来源
- ✅ `versions/mtp-3.1.5.md` — 30 条来源
- ✅ `versions/mtp-3.1.6.md` — 19 条来源
- ✅ `versions/mtp-3.1.7.md` — 3 条来源
- ✅ `versions/mtp-3.2.0.md` — 4 条来源
- ✅ `versions/mtp-3.2.1.md` — 30 条来源
- ✅ `versions/mtp-3.2.2.md` — 30 条来源
- ✅ `versions/mtp-3.3.0.md` — 1 条来源
- ✅ `versions/mtp-3.3.1.md` — 16 条来源
- ✅ `versions/mtp-3.3.2.md` — 30 条来源
- ✅ `versions/mtp-3.3.3.md` — 5 条来源
- ✅ `versions/mtp-3.4.0.md` — 3 条来源
- ✅ `versions/mtp-3.4.1.md` — 3 条来源
- ✅ `versions/mtp-3.4.2.md` — 3 条来源
- ✅ `versions/mtp-7.5.0.md` — 1 条来源
- ✅ `versions/mtp-7.5.2.md` — 1 条来源
- ✅ `versions/mtp-7.6.0.md` — 1 条来源
- ✅ `versions/smartest-2.4.0.md` — 1 条来源
- ✅ `versions/smartest-2.5.0.md` — 1 条来源
- ✅ `versions/smartest-6.3.2.md` — 30 条来源
- ✅ `versions/smartest-6.3.3.md` — 5 条来源
- ✅ `versions/smartest-6.3.4.md` — 3 条来源
- ✅ `versions/smartest-6.3.5.3.md` — 6 条来源
- ✅ `versions/smartest-6.5.0.md` — 30 条来源
- ✅ `versions/smartest-6.5.1.md` — 12 条来源
- ✅ `versions/smartest-6.5.2.md` — 30 条来源
- ✅ `versions/smartest-6.5.3.md` — 30 条来源
- ✅ `versions/smartest-6.5.4.md` — 30 条来源
- ✅ `versions/smartest-7.0.0.md` — 1 条来源
- ✅ `versions/smartest-7.0.1.md` — 30 条来源
- ✅ `versions/smartest-7.0.3.md` — 30 条来源
- ✅ `versions/smartest-7.0.4.md` — 30 条来源
- ✅ `versions/smartest-7.1.0.md` — 30 条来源
- ✅ `versions/smartest-7.1.1.md` — 30 条来源
- ✅ `versions/smartest-7.1.2.md` — 30 条来源
- ✅ `versions/smartest-7.1.3.md` — 30 条来源
- ✅ `versions/smartest-7.1.4.5.md` — 3 条来源
- ✅ `versions/smartest-7.1.4.md` — 30 条来源
- ✅ `versions/smartest-7.10.0.md` — 30 条来源
- ✅ `versions/smartest-7.10.1.md` — 30 条来源
- ✅ `versions/smartest-7.10.2.md` — 30 条来源
- ✅ `versions/smartest-7.10.3.md` — 30 条来源
- ✅ `versions/smartest-7.2.0.md` — 30 条来源
- ✅ `versions/smartest-7.2.1.5.md` — 2 条来源
- ✅ `versions/smartest-7.2.1.md` — 30 条来源
- ✅ `versions/smartest-7.2.2.1.md` — 2 条来源
- ✅ `versions/smartest-7.2.2.md` — 30 条来源
- ✅ `versions/smartest-7.2.3.9.md` — 3 条来源
- ✅ `versions/smartest-7.2.3.md` — 30 条来源
- ✅ `versions/smartest-7.3.0.md` — 16 条来源
- ✅ `versions/smartest-7.3.1.md` — 30 条来源
- ✅ `versions/smartest-7.3.2.md` — 30 条来源
- ✅ `versions/smartest-7.3.3.md` — 30 条来源
- ✅ `versions/smartest-7.3.4.4.md` — 3 条来源
- ✅ `versions/smartest-7.3.4.md` — 21 条来源
- ✅ `versions/smartest-7.4.0.md` — 30 条来源
- ✅ `versions/smartest-7.4.1.1.md` — 3 条来源
- ✅ `versions/smartest-7.4.1.md` — 30 条来源
- ✅ `versions/smartest-7.4.2.md` — 30 条来源
- ✅ `versions/smartest-7.4.3.md` — 30 条来源
- ✅ `versions/smartest-7.4.4.md` — 30 条来源
- ✅ `versions/smartest-7.4.5.md` — 16 条来源
- ✅ `versions/smartest-7.5.0.md` — 30 条来源
- ✅ `versions/smartest-7.5.1.md` — 30 条来源
- ✅ `versions/smartest-7.5.2.md` — 30 条来源
- ✅ `versions/smartest-7.5.3.md` — 30 条来源
- ✅ `versions/smartest-7.5.4.1.md` — 2 条来源
- ✅ `versions/smartest-7.5.4.md` — 28 条来源
- ✅ `versions/smartest-7.50.md` — 1 条来源
- ✅ `versions/smartest-7.6.0.md` — 30 条来源
- ✅ `versions/smartest-7.6.1.md` — 30 条来源
- ✅ `versions/smartest-7.6.2.md` — 30 条来源
- ✅ `versions/smartest-8.0.0.md` — 4 条来源
- ✅ `versions/smartest-8.0.2.md` — 1 条来源
- ✅ `versions/smartest-8.0.7.md` — 1 条来源
- ✅ `versions/smartest-8.0.8.md` — 4 条来源
- ✅ `versions/smartest-8.1.0.md` — 13 条来源
- ✅ `versions/smartest-8.1.1.md` — 1 条来源
- ✅ `versions/smartest-8.1.2.md` — 14 条来源
- ✅ `versions/smartest-8.1.3.md` — 2 条来源
- ✅ `versions/smartest-8.1.4.md` — 14 条来源
- ✅ `versions/smartest-8.2.0.md` — 21 条来源
- ✅ `versions/smartest-8.2.1.md` — 6 条来源
- ✅ `versions/smartest-8.2.2.md` — 1 条来源
- ✅ `versions/smartest-8.2.3.md` — 2 条来源
- ✅ `versions/smartest-8.2.5.md` — 24 条来源
- ✅ `versions/smartest-8.3.0.md` — 11 条来源
- ✅ `versions/smartest-8.3.1.md` — 1 条来源
- ✅ `versions/smartest-8.3.2.md` — 8 条来源
- ✅ `versions/smartest-8.3.3.md` — 9 条来源
- ✅ `versions/smartest-8.3.4.md` — 30 条来源
- ✅ `versions/smartest-8.3.5.md` — 2 条来源
- ✅ `versions/smartest-8.4.0.md` — 18 条来源
- ✅ `versions/smartest-8.4.1.md` — 4 条来源
- ✅ `versions/smartest-8.4.2.md` — 8 条来源
- ✅ `versions/smartest-8.4.3.md` — 30 条来源
- ✅ `versions/smartest-8.4.4.1.md` — 1 条来源
- ✅ `versions/smartest-8.4.4.md` — 13 条来源
- ✅ `versions/smartest-8.5.0.md` — 4 条来源
- ✅ `versions/smartprod-0.1.0-14.md` — 2 条来源
- ✅ `versions/smartprod-0.1.0-17.md` — 1 条来源
- ✅ `versions/smartrdi-2.1.0.md` — 30 条来源
- ✅ `versions/smartrdi-2.2.0.md` — 21 条来源
- ✅ `versions/smartrdi-2.3.0.md` — 30 条来源
- ✅ `versions/smartrdi-2.3.1.md` — 18 条来源
- ✅ `versions/smartrdi-2.3.2.md` — 1 条来源
- ✅ `versions/smartrdi-2.4.0.md` — 30 条来源
- ✅ `versions/smartrdi-2.4.1.md` — 17 条来源
- ✅ `versions/smartrdi-2.4.2.md` — 30 条来源
- ✅ `versions/smartrdi-2.4.3.md` — 29 条来源
- ✅ `versions/smartrdi-2.4.4.md` — 30 条来源
- ✅ `versions/smartrdi-2.4.5.md` — 23 条来源
- ✅ `versions/smartrdi-2.5.0.md` — 30 条来源
- ✅ `versions/smartrdi-2.5.1.md` — 7 条来源
- ✅ `versions/smartrdi-7.10.0.md` — 15 条来源
- ✅ `versions/smartrdi-7.10.1.md` — 9 条来源
- ✅ `versions/smartrdi-7.10.3.md` — 15 条来源
- ✅ `versions/smartrdi-7.4.4.md` — 2 条来源
- ✅ `versions/smartrdi-7.5.0.md` — 30 条来源
- ✅ `versions/smartrdi-7.5.1.md` — 16 条来源
- ✅ `versions/smartrdi-7.5.2.md` — 21 条来源
- ✅ `versions/smartrdi-7.5.3.md` — 15 条来源
- ✅ `versions/smartrdi-7.5.4.md` — 1 条来源
- ✅ `versions/smartrdi-7.6.0.md` — 30 条来源
- ✅ `versions/tp360-3.10.0.md` — 2 条来源
- ✅ `versions/tp360-3.10.3.md` — 2 条来源
- ✅ `versions/tp360-3.10.4.md` — 4 条来源
- ✅ `versions/tp360-3.8.0.md` — 3 条来源
- ✅ `versions/tp360-3.9.0.md` — 1 条来源
- ✅ `versions/tp360-7.2.2.md` — 1 条来源
- ✅ `versions/tp360-7.3.2.md` — 1 条来源

其余页合计 3053 条来源路径（阶段页合计 677 条）。

## 第四类 · 正文引用的分类号是否存在于语料

- ✅ `project` — 引用 43 个分类号，全部存在
- ✅ `pin` — 引用 59 个分类号，全部存在
- ✅ `level` — 引用 66 个分类号，全部存在
- ✅ `timing` — 引用 49 个分类号，全部存在
- ✅ `pattern` — 引用 60 个分类号，全部存在
- ✅ `testmethod` — 引用 46 个分类号，全部存在
- ✅ `testflow` — 引用 59 个分类号，全部存在
- ✅ `run` — 引用 48 个分类号，全部存在
- ✅ `results` — 引用 66 个分类号，全部存在

> 分类号只取前两级/三级也能命中（如 `01.07`），所以这一类比第三类松；
> 它是补第三类的漏网，不是替代。

## 第五类 · 「下一步」链

- ✅ `project` → `[[pin]]`
- ✅ `pin` → `[[level]]`
- ✅ `level` → `[[timing]]`
- ✅ `timing` → `[[pattern]]`
- ✅ `pattern` → `[[testmethod]]`
- ✅ `testmethod` → `[[testflow]]`
- ✅ `testflow` → `[[run]]`
- ✅ `run` → `[[results]]`
- ℹ️ `results`（末段）指向 ['run'] — 末段允许指向收尾页，只要不是硬造第十段

## 第六类 · object 候选的 stage 归属覆盖

`in_src >= 20` 的 object 候选（排除 index）：**125** 个。

- ✅ **已建页**（`wiki/` 下任意类型目录，由 frontmatter `sources` 认领）：**124**
- ✅ **成链**（wikilink 或反引号点名，九页里）：**0**
- ⚠️ **只在散文里提过，没成链**：**1**
- ✅ **一个字都没提的：0**（**这一档空着才是对的**）
- ⚪ **已查明误报**（不计入 ❌）：`DC Scale UHC4 / UHC4T card` 这一篇由 `wiki/objects/dc-scale-uhc4t-card.md` 认领——同一对象在 `02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.md` 另有一篇，页以那一篇为 `sources:`。
- ✅ **`in_src >= 20` 还没有页的：0**（**这一档空着才是对的**）

已建页（这些从「未归属」里出列了）：

| in_src | 对象 | 页 |
|---|---|---|
| 95 | DUT board design reference | `wiki/concepts/dut-board-design-reference.md` |
| 95 | DC Scale XPS256 card | `wiki/objects/dc-scale-xps256-card.md` |
| 78 | EDF data organization | `wiki/concepts/edf-data-organization.md` |
| 72 | EDF data types | `wiki/concepts/edf-data-types.md` |
| 70 | TESTSET | `wiki/objects/testset.md` |
| 67 | EVENT_VALUE_DOUBLE | `wiki/objects/event-value-double.md` |
| 65 | ON_FIRST_INVOCATION_BEGIN | `wiki/constraints/execution-context-requires-firmware-definition.md` |
| 63 | PSFC, PSFC? - (Parallel Setup FoCus) | `wiki/objects/psfc.md` |
| 62 | Alphabetical list of flags | `wiki/mappings/mapping-testflow.md` |
| 56 | SmartRDI | `wiki/objects/smartrdi.md` |
| 55 | RDI_Configure file | `wiki/objects/rdi-configure-file.md` |
| 54 | SPMU_PIN_TASK | `wiki/objects/spmu-pin-task.md` |
| 51 | DUT interface layout | `wiki/concepts/dut-interface-layout.md` |
| 49 | APG pattern file | `wiki/objects/apg-pattern-file.md` |
| 46 | Structure of a TMLimits CSV file | `wiki/mappings/mapping-testmethod.md` |
| 46 | SMC_ARM() | `wiki/constraints/smc-background-process-locks-config.md` |
| 46 | DPSPINS resources | `wiki/mappings/mapping-level.md` |
| 45 | Data navigation views | `wiki/objects/data-navigation-views.md` |
| 45 | Utility Card | `wiki/objects/utility-card.md` |
| 43 | CCT Multiport Sequencer Synchronizer API | `wiki/objects/cct-multiport-sequencer-synchronizer-api.md` |
| 43 | Technology file for a device | `wiki/mappings/mapping-project.md` |
| 42 | MTP_MEMORY_TEST | `wiki/objects/mtp-memory-test.md` |
| 39 | Utility pogo block - Utility Card (V93000 EX | `wiki/objects/utility-pogo-block-utility-card-v93000-exa-scale-systems.md` |
| 39 | APG program file | `wiki/objects/apg-program-file.md` |
| 39 | Sharing configuration file | `wiki/objects/sharing-configuration-file.md` |
| 38 | EVENT_BASE | `wiki/objects/event-base.md` |
| 38 | SmartCalc framework | `wiki/objects/smartcalc.md` |
| 38 | Utility lines | `wiki/concepts/utility-lines.md` |
| 38 | GET_FUNCTIONAL_RESULT() | `wiki/objects/get-functional-result.md` |
| 37 | SmartRDI: Vector and protocol programming | `wiki/concepts/smartrdi-vector-and-protocol-programming.md` |
| 37 | Equation based level setup | `wiki/mappings/mapping-level.md` |
| 36 | Using execution contexts | `wiki/mappings/mapping-run.md` |
| 36 | TEST | `wiki/objects/test.md` |
| 36 | SPMU_TASK | `wiki/objects/spmu-task.md` |
| 35 | DPS_TASK | `wiki/objects/dps-task.md` |
| 35 | WSUS, WSUS? - (Waveform Sets USed) | `wiki/mappings/mapping-timing.md` |
| 34 | EVENT_VALUE_INT | `wiki/objects/event-value-int.md` |
| 34 | FOR_EACH_SITE_BEGIN | `wiki/constraints/execution-context-requires-firmware-definition.md` |
| 33 | STPM control file | `wiki/objects/stpm-control-file.md` |
| 33 | STPM merge rules file | `wiki/objects/stpm-merge-rules-file.md` |
| 33 | Device access file | `wiki/objects/device-access-file.md` |
| 32 | Device architecture file | `wiki/objects/device-architecture-file.md` |
| 32 | Pogo pad and via design | `wiki/concepts/pogo-pad-and-via-design.md` |
| 30 | LIMIT | `wiki/objects/limit.md` |
| 30 | TASK_LIST | `wiki/objects/task-list.md` |
| 30 | DC Test Programming | `wiki/concepts/dc-test-programming.md` |
| 30 | Pin mapping file | `wiki/objects/pin-mapping-file.md` |
| 30 | PATTERN_CONTROLLER | `wiki/objects/pattern-controller.md` |
| 29 | ON_FIRST_INVOCATION_END | `wiki/constraints/execution-context-requires-firmware-definition.md` |
| 29 | XPS256 programming - PMU operating mode | `wiki/objects/xps256-pmu-operating-mode.md` |
| 29 | DSCP, DSCP? - (Define System Control Paramet | `wiki/mappings/mapping-project.md` |
| 29 | Pattern Editor | `wiki/mappings/mapping-pattern.md` |
| 27 | SMC_TEST() | `wiki/objects/smc-test.md` |
| 27 | Setting up a shmoo test with the Shmoo Tool | `wiki/concepts/setting-up-a-shmoo-test-with-the-shmoo-tool.md` |
| 27 | Test summary tab | `wiki/mappings/mapping-results.md` |
| 27 | DC Scale DPS128/DPS64 cards | `wiki/objects/dps128-dps64-cards.md` |
| 27 | DPS128 and DPS64 pogo cabling and model file | `wiki/objects/dps128-dps64-cards.md` |
| 27 | Pogo pin assignment - Utility pogo blocks | `wiki/objects/utility-line-assignments.md` |
| 27 | Pin configuration tool | `wiki/objects/pin-configuration-tool.md` |
| 27 | Utility line assignments | `wiki/objects/utility-line-assignments.md` |
| 26 | TMLimits | `wiki/constraints/smc-background-process-locks-config.md` |
| 26 | EVENT_WAVEFORM_VFVM | `wiki/objects/event-waveform-vfvm.md` |
| 26 | Sequencer-controlled utility lines | `wiki/concepts/sequencer-controlled-utility-lines.md` |
| 26 | SHARING_CONFIGURATION | `wiki/objects/sharing-configuration.md` |
| 26 | DPS128… DPS64 functionality and features | `wiki/objects/dps128-dps64-cards.md` |
| 26 | DIGITAL_OFFSET_SEARCH_PINS | `wiki/objects/digital-offset-search-pins.md` |
| 26 | DPS power flags - get...() functions | `wiki/objects/dps-power-flags-get-functions.md` |
| 26 | Conventions for GPIB/LAN communication | `wiki/concepts/gpib-lan-communication-conventions.md` |
| 26 | SQPG, SQPG? - (SeQuencer ProGramming) | `wiki/mappings/mapping-pattern.md` |
| 25 | Timing Setup Commands | `wiki/mappings/mapping-timing.md` |
| 25 | Pin configuration setup commands | `wiki/constraints/pin-config-locked-during-test.md` |
| 25 | Setting chart display options | `wiki/concepts/setting-chart-display-options.md` |
| 25 | Timing Diagram Tool | `wiki/mappings/mapping-timing.md` |
| 25 | DPS_AUX_PIN_TASK.checkPowerFlags() | `wiki/objects/dps-aux-pin-task.md` |
| 25 | Special test suites | `wiki/mappings/mapping-testflow.md` |
| 25 | Controlling Multiple Sites | `wiki/concepts/controlling-multiple-sites.md` |
| 25 | Maintenance operations | `wiki/objects/mtp-maintenance-operations.md` |
| 24 | SMC_SYNCHRONIZE() | `wiki/objects/smc-synchronize.md` |
| 24 | Preprocessing and postprocessing scripts | `wiki/objects/preprocessing-and-postprocessing-scripts.md` |
| 24 | Pogo block compatibility | `wiki/concepts/pogo-block-compatibility.md` |
| 24 | Signal Analyzer | `wiki/objects/signal-analyzer.md` |
| 23 | Test Number Generator and TMLimits | `wiki/concepts/test-number-generator-and-tmlimits.md` |
| 23 | Direct-Probe stiffener | `wiki/concepts/direct-probe-stiffener.md` |
| 23 | DPS_AUX_PIN_TASK | `wiki/objects/dps-aux-pin-task.md` |
| 23 | FLUSH | `wiki/mappings/mapping-testmethod.md` |
| 23 | Utility power supplies | `wiki/objects/utility-power-supplies.md` |
| 23 | Concepts of logical boards | `wiki/concepts/logical-boards.md` |
| 23 | Data Logging Profiles | `wiki/objects/data-logging-profiles.md` |
| 23 | DFGP, DFGP? - (DeFine GrouP) | `wiki/objects/dfgp.md` |
| 23 | How to create a universal test method class | `wiki/mappings/mapping-testmethod.md` |
| 23 | Flow Sequence Editor | `wiki/objects/flow-sequence-editor.md` |
| 22 | DC Scale UHC4T card | `wiki/objects/dc-scale-uhc4t-card.md` |
| 22 | SHARED_CONTINUITY_TEST | `wiki/objects/shared-continuity-test.md` |
| 22 | SHARED_LEAKAGE_PARALLEL_TEST | `wiki/objects/mtp-shared-test-commands.md` |
| 22 | SPMU_PIN_TASK.mode() | `wiki/objects/spmu-pin-task-mode.md` |
| 22 | Using the Timing Diagram Tool | `wiki/mappings/mapping-timing.md` |
| 22 | DPS128… DPS64 hardware overview | `wiki/objects/dps128-dps64-cards.md` |
| 22 | Setting up DC Scale pins with SmartRDI | `wiki/concepts/setting-up-dc-scale-pins-with-smartrdi.md` |
| 22 | Opening TP360 | `wiki/objects/tp360.md` |
| 22 | DPS128… DPS64 power budget | `wiki/objects/dps128-dps64-cards.md` |
| 22 | TimeStampAttrType | `wiki/objects/timestamp-attr-type.md` |
| 22 | GLOBAL section | `wiki/objects/global-section.md` |
| 22 | DFPN, DFPN? - (DeFine Pin Name) | `wiki/constraints/pin-config-requires-sequencer-off.md` |
| 22 | DC_RESULT_ACCESSOR | `wiki/objects/dc-result-accessor.md` |
| 21 | Command Reference | `wiki/concepts/command-reference.md` |
| 21 | EVENT_WAVEFORM_VFIM | `wiki/objects/event-waveform-vfim.md` |
| 21 | Protocol editor | `wiki/objects/protocol-editor.md` |
| 21 | Hidden upload | `wiki/mappings/mapping-project.md` |
| 21 | Layout information: DUT board | `wiki/concepts/layout-information-dut-board.md` |
| 21 | SmartRDI: TMU test setup | `wiki/concepts/smartrdi-tmu-test-setup.md` |
| 21 | FOR_EACH_SITE_END | `wiki/objects/for-each-site-end.md` |
| 21 | Internal utility power supply (V93000 system | `wiki/objects/utility-line-assignments.md` |
| 21 | XPS256 status flags | `wiki/objects/xps256-status-flags.md` |
| 21 | DFPS, DFPS? - (DeFine Power Supply) | `wiki/constraints/cross-card-ganging-requires-ddic.md` |
| 21 | PSAS? - (Power Supply Accumulated Status) | `wiki/objects/psas.md` |
| 20 | Digital Pins editor | `wiki/mappings/mapping-pin.md` |
| 20 | Grounding | `wiki/concepts/dut-board-grounding.md` |
| 20 | Raw data views | `wiki/mappings/mapping-results.md` |
| 20 | Displaying test results in analysis views | `wiki/objects/analysis-views.md` |
| 20 | MTPT (STPM MCM mapping tables) | `wiki/objects/mtpt.md` |
| 20 | Utility line characteristics | `wiki/objects/utility-line-assignments.md` |
| 20 | DIGITAL_CAPTURE_TEST | `wiki/objects/digital-capture-test.md` |
| 20 | XPS256 programming - DPS operating mode | `wiki/objects/xps256-programming-dps-operating-mode.md` |
| 20 | Testflow Properties view | `wiki/mappings/mapping-testmethod.md` |

「只在散文里提过」不算漏，但**对象页建起来之后没有入链**——这页读起来会像没有这个对象。值得补成 `[[...]]`。

| in_src | 对象 | 出现在 |
|---|---|---|
| 22 | DC Scale UHC4 / UHC4T card | pin |

映射表写入 `extract/stage-map.csv`（1 条候选 + 124 条已建页；多归属的会多行；已建页的属主写成 `page:<类型目录>/<slug>`）。

## 第七类 · 引文是否逐字（**抓编引文**）

> **范围：`wiki/` 下**除 `log.md` / `index.md` 和 §7 的子索引（`index-*.md`）**外的全部页面**——本次跳过 **4 个元文件**，逐个列在下面（本类曾只走九页，见下）。判据是「引用块能在 **9,398 篇 md + 本篇 sources 指向的上游 .htm** 里找到完全子串」，不是「读起来像」。

> 跳过的：`index.md`、`log.md`、`objects/index-objects.md`、`versions/index-versions.md`。**这是全部**——排除必须报出来，不许静默缩小范围。

- ✅ `concepts/command-reference.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/context-pins.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `concepts/controlling-multiple-sites.md` — 引用块/代码块 7 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 67%｜`This optimization enables parallel execution of setup and test … Then, post-test…`
    - 🟠 **疑似自加结构 2 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `execution of setup and test … Then, post-test`
        - `test … Then, post-test processing (getting result, computation,`
- ✅ `concepts/dc-test-programming.md` — 引用块/代码块 6 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 67%｜`If you need (a) auto-ranging in DPS current measurements or (b) need to suppress…`
    - 🟠 **疑似自加结构 2 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `you use the DPS_TASK and DPS_PIN_TASK APIs… (Auto-ranging`
        - `and DPS_PIN_TASK APIs… (Auto-ranging and preAction "NPRM" are`
- ✅ `concepts/direct-probe-stiffener.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/dut-board-design-reference.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/dut-board-grounding.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/dut-interface-layout.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；32 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `concepts/edf-data-organization.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/edf-data-types.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/edf.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/equation-based-level-setup.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/flag.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；1 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `concepts/ganging.md` — 引用块/代码块 7 处；对不上的 2 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 56%｜`A serial interface for sequencer-controlled utility lines can handle the data st…`
    - ⚠️ 未称逐字，覆盖率 67%｜`You determine the word width yourself by fitting either 2-row or 4-row utility p…`
- ✅ `concepts/gpib-lan-communication-conventions.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/how-to-create-a-universal-test-method-class.md` — 引用块/代码块 2 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**；1 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - ⚠️ 未称逐字，覆盖率 67%｜`It must start with an upper case character. Otherwise an error message is displa…`
- ✅ `concepts/hv-protection.md` — 引用块/代码块 21 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/inter-layer-via-design.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/layout-information-dut-board.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/logical-boards.md` — 引用块/代码块 3 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 60%｜`If a pogo block provides pogo pins for more than 16 channels (= 1 logical board)…`
- ✅ `concepts/offline-result-emulation.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/pogo-block-compatibility.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/pogo-pad-and-via-design.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/sequencer-controlled-utility-lines.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/setting-chart-display-options.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/setting-up-a-shmoo-test-with-the-shmoo-tool.md` — 引用块/代码块 29 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/setting-up-dc-scale-pins-with-smartrdi.md` — 引用块/代码块 18 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/smartrdi-tmu-test-setup.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/smartrdi-vector-and-protocol-programming.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/test-number-generator-and-tmlimits.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/timing-setup-commands.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/utility-lines.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `concepts/waveform-set.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `constraints/constraint-level-mode-context-match.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/constraint-timing-mode-context-match.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/cross-card-ganging-requires-ddic.md` — 引用块/代码块 20 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；50 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `constraints/execution-context-requires-firmware-definition.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；30 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `constraints/label-edit-requires-tstl-selection.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/pals-before-other-setup.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/pin-config-locked-during-test.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/pin-config-requires-sequencer-off.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/rdi-call-requires-begin-end-block.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/referenced-set-requires-prior-definition.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/site-focus-required-before-command.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/smc-background-process-locks-config.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/synchronized-pins-require-same-test-processor.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `constraints/testname-requires-matching-limits.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `errors/error-data-queue-empty.md` — 引用块/代码块 11 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `errors/error-flexlm-license-codes.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `errors/error-model-file-rejected-at-startup.md` — 引用块/代码块 33 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `errors/error-result-server-transmission-timeout.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `errors/error-utility-power-supply-not-enabled.md` — 引用块/代码块 14 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `errors/error-workspace-in-use.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；9 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `mappings/mapping-level.md` — 引用块/代码块 21 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；11 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `mappings/mapping-pattern.md` — 引用块/代码块 14 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `mappings/mapping-pin.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `mappings/mapping-project.md` — 引用块/代码块 15 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - ⚠️ 未称逐字，覆盖率 50%｜`Note The VEC_TRANSFER_TASK and LEV_TRANSFER_TASK APIs can be used only with Smar…`
- ✅ `mappings/mapping-results.md` — 引用块/代码块 12 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；4 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `mappings/mapping-run.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；3 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `mappings/mapping-testflow.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `mappings/mapping-testmethod.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；13 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `mappings/mapping-timing.md` — 引用块/代码块 22 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；55 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/add-limit.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/alias-set-editor.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/alphabetical-list-of-flags.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；3 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/analysis-views.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/apg-pattern-file.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；14 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/apg-program-file.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/aprm.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/assign-value-node.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/begin-extension.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/bin.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；23 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/built-in-functions.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/bwdf.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；9 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/bwds.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；26 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/cct-change-level-spec.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/cct-multiport-sequencer-synchronizer-api.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/change-device-wizard.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/chin.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/ci-cpi.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/clkr.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；13 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/clmp.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；35 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/conf.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；9 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/connect.md` — 引用块/代码块 12 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/ctxt.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/data-logging-profile-api.md` — 引用块/代码块 25 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/data-logging-profiles.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
    - 🟠 **疑似自加结构 1 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `debug profile to enable more detailed logging. …`
- ✅ `objects/data-navigation-views.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/data-retrieval-library.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dc-result-accessor.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；10 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dc-scale-limits-editor.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dc-scale-uhc4t-card.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dc-scale-xps256-card.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dcdt.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；8 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/debug-perspective.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/debug-view.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/device-access-file.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；22 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/device-architecture-file.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/device-directory.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/device-license-file.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/device-summary-tab.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/device-technology-directory.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dfge.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；8 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dfgp.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dfpc.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；8 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dfpn.md` — 引用块/代码块 20 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；111 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dfpr.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dfps.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dfpt.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dfup.md` — 引用块/代码块 12 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；32 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dfut.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；20 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/digital-capture-test.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；4 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/digital-offset-search-pins.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/digital-pins-editor.md` — 引用块/代码块 5 处；对不上的 2 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 67%｜`The editor consists mainly of the tabular pin configuration area. The CONTEXT dr…`
    - ⚠️ 未称逐字，覆盖率 72%｜`The software uniquely identifies each channel in the system using a five-digit c…`
    - 🟠 **疑似自加结构 2 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `a virtual pogo block number. - bb: The`
        - `number. - bb: The channel number (range 01`
- ✅ `objects/disconnect.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dprl.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dprt.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；26 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dps-aux-pin-task.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dps-aux-task.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dps-pins-editor.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；15 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dps-power-flags-get-functions.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dps-task.md` — 引用块/代码块 11 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；18 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dps128-dps64-cards.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dpspins-resources.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/drlv.md` — 引用块/代码块 10 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**；12 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - ⚠️ 未称逐字，覆盖率 79%｜`The DRLV command defines the low and the high voltage levels for the driver ampl…`
    - 🟠 **疑似自加结构 2 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `previously defined by the DFGP, DFGP? - (DeFine`
        - `DFGP, DFGP? - (DeFine GrouP) command. These levels`
- ✅ `objects/dscp.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；36 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/dsus.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/dtcp.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/edl-file.md` — 引用块/代码块 16 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/edsp.md` — 引用块/代码块 12 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；39 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/end-extension.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/eqfs.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；8 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/eqsp.md` — 引用块/代码块 12 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；24 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/error-map-tool.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/error-map.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/etds.md` — 引用块/代码块 28 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；112 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/etim.md` — 引用块/代码块 16 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；8 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/event-base.md` — 引用块/代码块 6 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 50%｜`The following event types are provided by specialized event classes：`
- ✅ `objects/event-formatter.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/event-value-double.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/event-value-int.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；3 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/event-waveform-vfim.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/event-waveform-vfvm.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/execution-context.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/file-string.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/flags-page.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/flex-relay.md` — 引用块/代码块 11 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；4 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/flow-data-editor.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/flow-sequence-editor.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/flsh.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/flush.md` — 引用块/代码块 20 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；9 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/for-each-site-begin.md` — 引用块/代码块 16 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/for-each-site-end.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/fw-task.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/gctx.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；18 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/get-functional-result.md` — 引用块/代码块 23 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；25 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/get-utility-lines.md` — 引用块/代码块 8 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - ⚠️ 未称逐字，覆盖率 75%｜`GetUtilityLines: Gets the status of the utility lines SetUtilityLines: Sets the …`
- ✅ `objects/global-section.md` — 引用块/代码块 16 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；98 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/ground-sense-editor.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；8 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/group-node.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/hardware-bin-summary-tab.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/hardware-response-emulator.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/hardware-view.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/hidden-upload.md` — 引用块/代码块 3 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 50%｜`Note Hidden uploads, controlled and started by SMC_ARM()， must be finished befor…`
- ✅ `objects/hw-pin-state.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/hw-state.md` — 引用块/代码块 20 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；40 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/hwty.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/integrated-result-tool.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/jrst.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；1 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/jscf.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；13 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/jsdf.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/jspr.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/jsud.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/jswf.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/level-equation-file.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/level-file.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/level-master-file.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/level-set-selector.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/level-setup-tool.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/level-spec.md` — 引用块/代码块 17 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**；另有 1 处**忽略空白后才对上**（排版差异，不判错）；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - ⚠️ 未称逐字，覆盖率 0%｜`| specset | Spec set number. | Member functions`
- ✅ `objects/limit.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；19 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/lot-summary-generator.md` — 引用块/代码块 17 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/lsus.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/lsux.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/match-loops.md` — 引用块/代码块 14 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/model-file.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/mscf.md` — 引用块/代码块 12 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；52 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/msdf.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/mtp-maintenance-operations.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/mtp-memory-test.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；4 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/mtp-shared-test-commands.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/mtpt.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/multiport-burst-editor.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；1 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/new-device-wizard.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/on-first-invocation-begin.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/on-first-invocation-end.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/option-list.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pact.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；15 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pals.md` — 引用块/代码块 17 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；28 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - 🟠 **疑似自加结构 2 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `An error is generated if： - The specified`
        - `if： - The specified channel number is not`
- ✅ `objects/pattern-controller.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；9 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pattern-editor.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；16 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pattern-explorer.md` — 引用块/代码块 11 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；22 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pattern-master-file.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/pattern-object.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pattern-tool.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/pclk.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；46 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pdiv.md` — 引用块/代码块 11 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；13 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pfnd.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；4 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pin-configuration-file.md` — 引用块/代码块 18 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/pin-configuration-master-file.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/pin-configuration-tool.md` — 引用块/代码块 30 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pin-group-editor.md` — 引用块/代码块 17 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/pin-mapping-file.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；46 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pin-property-monitor.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/pin-string.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pin-utility.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/play-pattern.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/pogocabling-section.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/port-editor.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/pqfc.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/preprocessing-and-postprocessing-scripts.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/primary-status.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；8 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/prlt.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/project-explorer-view.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/protocol-editor.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/psas.md` — 引用块/代码块 25 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/psfc.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；29 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pslv.md` — 引用块/代码块 16 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；39 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pssl.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pssr.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；16 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/pste.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；8 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/raw-data-views.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/rclv.md` — 引用块/代码块 11 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；22 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - 🟠 **疑似自加结构 2 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `previously defined by the DFGP, DFGP? - (DeFine`
        - `DFGP, DFGP? - (DeFine GrouP) command. The threshold`
- ✅ `objects/rdi-configure-file.md` — 引用块/代码块 17 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；92 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - 🟠 **疑似自加结构 2 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `generate eight or more cycles […]. So when`
        - `cycles […]. So when this mode is enabled,`
- ✅ `objects/report-window.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/result-configuration.md` — 引用块/代码块 17 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；32 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/rset.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/run-dialog.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/sequencer-status.md` — 引用块/代码块 19 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；11 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/sequencer.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/set-utility-lines.md` — 引用块/代码块 12 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**；40 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - ⚠️ 未称逐字，覆盖率 75%｜`GetUtilityLines: Gets the status of the utility lines SetUtilityLines: Sets the …`
- ✅ `objects/setup-level-set-0.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/setup-management-tool.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/setup-perspective.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/shared-continuity-test.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/sharing-configuration-file.md` — 引用块/代码块 1 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - ⚠️ 未称逐字，覆盖率 40%｜`"This parameter is ignored for DPS-shared load boards for which there is a utili…`
- ✅ `objects/sharing-configuration.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/shmoo-tool.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/signal-analyzer.md` — 引用块/代码块 14 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/site-control-window.md` — 引用块/代码块 6 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 0%｜`The site in focus is automatically switched depending on the current situation i…`
- ✅ `objects/sldo.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；20 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/smartcalc-framework.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/smartcalc.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/smartest-data-formatter.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；1 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/smartrdi.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/smartshell.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/smc-synchronize.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；22 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/smc-test.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；3 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/software-bin-summary-tab.md` — 引用块/代码块 11 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；3 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/spec-search.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/spec-set.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/spec-tool.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/spec-value.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/spec-variable.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/special-test-suites.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；23 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/spmu-pin-task-mode.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；33 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/spmu-pin-task.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/spmu-task.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/sprm.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；9 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/spst.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；28 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/sqst.md` — 引用块/代码块 11 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；27 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/stdf.md` — 引用块/代码块 11 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/stme.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；20 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/stpm-control-file.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/stpm-merge-rules-file.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/stpm.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/strs.md` — 引用块/代码块 14 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；30 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/structure-of-a-tmlimits-csv-file.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/svlr.md` — 引用块/代码块 21 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；24 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/table-filter.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/task-list.md` — 引用块/代码块 12 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；4 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/technology-file-for-a-device.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/term.md` — 引用块/代码块 18 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；62 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/test-method-class.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/test-program-explorer.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/test-suite-control-api.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/test-suite.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/test-suites-page.md` — 引用块/代码块 37 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；12 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/test-summary-tab.md` — 引用块/代码块 4 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 71%｜`Refresh: Updates the system data log stream display with the latest logged data …`
- ✅ `objects/test.md` — 引用块/代码块 38 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；36 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/testflow-analyzer-tool.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/testflow-file.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/testflow-master-file.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/testflow-properties-view.md` — 引用块/代码块 17 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**
    - ⚠️ 未称逐字，覆盖率 0%｜`!Universal test method parameter display and modification Note If a parameter va…`
    - 🟠 **疑似自加结构 1 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `!Universal test method parameter display and modification Note If a parameter value is …`
- ✅ `objects/testflow-tool.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/testflow-variable.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/testset-testname.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；19 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/testset.md` — 引用块/代码块 18 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/timestamp-attr-type.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/timing-diagram-tool.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/timing-equation-set.md` — 引用块/代码块 25 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/timing-file.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/timing-master-file.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/timing-set-selector.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；5 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/timing-setup-tool.md` — 引用块/代码块 43 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/timing-spec.md` — 引用块/代码块 19 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/timing-specification.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/tmlimits.md` — 引用块/代码块 32 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；43 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - 🟠 **疑似自加结构 1 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `getLimitRef(), getLimitObj() / load() (without parameters!). - The`
- ✅ `objects/tp360.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；另有 1 处**忽略空白后才对上**（排版差异，不判错）
- ✅ `objects/tpi-program-routines.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/tpt-generate-device-dir.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；9 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/tpt-import-from-device.md` — 引用块/代码块 10 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**；51 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - ⚠️ 未称逐字，覆盖率 60%｜`<pre_proc> is a script that is executed before this command. <post_proc> is a sc…`
- ✅ `objects/tsus.md` — 引用块/代码块 12 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/tsux.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；23 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/udef.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/udgp.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/udpr.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/udps.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/udpt.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/udup.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/udut.md` — 引用块/代码块 10 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；2 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/udvp.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/universal-test-method-library.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/upas.md` — 引用块/代码块 15 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；22 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/uptd.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；9 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/utility-card.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/utility-line-assignments.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/utility-line-view.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/utility-pins-editor.md` — 引用块/代码块 20 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；73 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/utility-pogo-block-utility-card-v93000-exa-scale-systems.md` — 引用块/代码块 5 处；对不上的 1 处，其中**页面自称「逐字」的 0 处**；16 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - ⚠️ 未称逐字，覆盖率 50%｜`CAUTION The 4-row utility block uses the row sequence c-a-b-d for compatibility …`
- ✅ `objects/utility-power-supplies.md` — 引用块/代码块 6 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；10 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/utility-purpose-editor.md` — 引用块/代码块 5 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/vclk.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；14 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/vdcg.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/vec-events.md` — 引用块/代码块 16 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/vector-setup-file.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/vpin.md` — 引用块/代码块 3 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/vtim.md` — 引用块/代码块 18 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；20 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/vwfg.md` — 引用块/代码块 13 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；24 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/vwfs.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；13 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/wafer-summary-tab.md` — 引用块/代码块 20 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/wave.md` — 引用块/代码块 24 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；93 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/waveform-mapping.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/waveform-view.md` — 引用块/代码块 16 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；32 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/wavetable-file.md` — 引用块/代码块 7 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；3 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/wavetable.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/wfds.md` — 引用块/代码块 19 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；70 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/wsus.md` — 引用块/代码块 9 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；12 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/xps256-pmu-operating-mode.md` — 引用块/代码块 2 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；4 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `objects/xps256-programming-dps-operating-mode.md` — 引用块/代码块 1 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `objects/xps256-status-flags.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `stages/level.md` — 引用块/代码块 17 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `stages/pattern.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `stages/pin.md` — 引用块/代码块 14 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；1 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `stages/project.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `stages/results.md` — 引用块/代码块 4 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `stages/run.md` — 引用块/代码块 58 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；另有 2 处**忽略空白后才对上**（排版差异，不判错）；62 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - 🟠 **疑似自加结构 2 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `system/testflow/testsuite flags. - Execute the test. Obtain the`
        - `flag settings. - Execute all tests. Obtain the`
- ✅ `stages/testflow.md` — 引用块/代码块 8 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `stages/testmethod.md` — 引用块/代码块 16 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；7 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
- ✅ `stages/timing.md` — 引用块/代码块 20 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**；6 处在**上游 raw/** 里对上（表格已换成指针，见 `_up_blob`）
    - 🟠 **疑似自加结构 1 处**（引文单元以 `- ` 开头 / 中间有 ` - ` / 含 `…` 或 `...`，**且对不上原文**）。**筛查项，不判错**——滑窗跨过两个真列表项的接缝时也会命中，要人看。
        - `CONF, CONF? - (CONFiguration). The maximum number of`
- ✅ `versions/mtp-2.4.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-2.4.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-2.6.5.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-2.6.6.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.0.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.0.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.0.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.1.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.1.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.1.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.1.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.1.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.1.5.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.1.6.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.1.7.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.2.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.2.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.2.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.3.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.3.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.3.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.3.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.4.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.4.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-3.4.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-7.5.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-7.5.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/mtp-7.6.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-2.4.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-2.5.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-6.3.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-6.3.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-6.3.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-6.3.5.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-6.5.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-6.5.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-6.5.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-6.5.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-6.5.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.0.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.0.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.0.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.0.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.1.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.1.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.1.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.1.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.1.4.5.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.1.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.10.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.10.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.10.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.10.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.2.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.2.1.5.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.2.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.2.2.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.2.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.2.3.9.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.2.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.3.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.3.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.3.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.3.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.3.4.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.3.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.4.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.4.1.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.4.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.4.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.4.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.4.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.4.5.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.5.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.5.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.5.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.5.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.5.4.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.5.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.50.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.6.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.6.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-7.6.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.0.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.0.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.0.7.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.0.8.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.1.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.1.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.1.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.1.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.1.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.2.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.2.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.2.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.2.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.2.5.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.3.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.3.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.3.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.3.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.3.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.3.5.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.4.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.4.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.4.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.4.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.4.4.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.4.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartest-8.5.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartprod-0.1.0-14.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartprod-0.1.0-17.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.1.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.2.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.3.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.3.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.3.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.4.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.4.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.4.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.4.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.4.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.4.5.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.5.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-2.5.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.10.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.10.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.10.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.4.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.5.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.5.1.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.5.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.5.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.5.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/smartrdi-7.6.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/tp360-3.10.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/tp360-3.10.3.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/tp360-3.10.4.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/tp360-3.8.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/tp360-3.9.0.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/tp360-7.2.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**
- ✅ `versions/tp360-7.3.2.md` — 引用块/代码块 0 处；对不上的 0 处，其中**页面自称「逐字」的 0 处**

> **判据分两档，因为这两件事严重程度差一个数量级：**
>
> - **自称「逐字」却没对上 = 硬错误。** 要么改回原文，要么把「逐字」二字删掉。
> - **没自称逐字 = 转述，对不上是正常的。** 只提示，不判错。
>
> **另一档，与上面两档都不同：疑似自加结构 —— 本次共 20 处。**
> **本类主动排除：`<!-- 语法节 begin -->`…`<!-- 语法节 end -->` 之间那一段，本次涉及 322 页、共 2283871 字符。**
> 那一段由 `objscaffold.py` 写（§4），段内语料链接被机械改写成 ``文本``（raw: `路径`），**按设计就不是逐字的**——不排除它，本类会稳定地报一条自己造成的「对不上」。
> **它没有被放过，是被更硬的口径接管了**：第十二类查的是「页面与脚本当前产出**逐字节一致**」。两个检查管同一段时，弱的那条只产生噪声。
> 形状判据三条：引文单元**以 `- ` 开头**、**中间含 ` - `**、或**含 `…` / `...`**，**且对不上原文**。
> 页面自加的列表符和页面自加的 `—` 在规范化后都是 `- `，三条同时覆盖两种。
> **这一档不看「有没有自称逐字」**——§11.1 的闭合清单是**引文本身**的规矩：在引文块里，`…`、列表符 `- `、单元格分隔都算原文的一部分。**排版差异可以放过，加进结构不行。**
> **它会误报，误报有名字**：滑窗跨过两个**真**列表项的接缝时也命中。**所以它是筛查项、不判错**——价值在于**把这一类从「排版差异」里拎出来**。
> 单列这一档的原因写在 `check()` 的 docstring 里：**同一个形状 2026-09-18 一天内出现两次，两次都被读成「排版差异」。**

> **判法分两种，因为块有两种：**
>
> - **代码块逐行验。** 页面会把多篇文档的行**拼成一个示例块**（`pin` 页那个 DFPN 会话块自注「逐字取自 A 与 B 与 C」）——
>   那句话的意思是**每一行**取自其中某篇，不是整块连续。整块比对必然冤枉它。
> - **散文引用用滑窗验**（8 词窗、步长 4）。散文会被换行、省略号、并句打断，
>   滑窗能把「接缝丢一两窗」和「成片丢窗」分开。

> ⚠️ **这条容忍 2026-09-18 收紧了。** 原文这里写的是「表格被改写成一行、多行被并成一句，只丢窗不丢片——**它们不是编，是格式改写**」。**那句话是错的**：
> 它并没有骗过机器（这几处一样被报成失配），**它是骗过了我**——被报出来之后，我**照着这句话把它们归类成「排版差异」而不是缺陷**，于是留在待办里。
>
> 复核那几处「格式改写」时发现，其中三处**真的少了字符**，不是只换了排版：
> `02.07.04.01.69_FLUSH` 的两个列表被拍平成行内代码（少抄了每行的 `- `）；
> `02.06.05_Level_Setup_Commands` 的六项列表被拍平，并加上**原文没有的粗体**；
> `01.01.08.06_Debug_View` 表格的两列被用**页面自加的 `—`** 连成句（原文里没有这个破折号）。
>
> **判据现在写死：`…`、列表符 `- `、单元格分隔，都算原文的一部分。**
> 引文里出现 `…`，等于承认中间有字没抄——**那就不是引文，是转述：要么补全，要么把引号去掉。**
> 分界是：**跨段合并不算错**（字还是连续的），**丢字符才算错**。
>
> **这条也是「检查比它自称的范围窄」那类错的第六次**——前五次见 §13。这次窄在**判据自己写的容忍度**上：本类叫「引文逐字」，却预先声明「格式改写放行」。

## 第八类 · 链接目标可达（**抓断链；排除项是名字白名单两项，行内代码跨度里的 wikilink 照样算**）

- 内容页共 **505** 页，引用 **521** 个目标，其中 **16** 个找不到对应页。
- 口径指纹：内容页 505 个文件、白名单 2 项、空目标跳过、`log.md` 不计入，`sha256[:12] = 019e95ec1acb`。

> **这不是页面的缺陷，是建页 backlog。** 它列的是**脊椎已经要求**的页——
> 比按 `in_src` 排的「125 个高入度对象」更有用：那些只是"语料里常出现"，
> 这些是"流程页已经伸手去要了"。

| 悬空目标 | 被引 | 引用它的 stage |
|---|---|---|
| `ps1600` | 14 | chin, drlv, jsud, jswf, logical-boards, pin-utility, rclv, setup-level-set-0, smartrdi, smartrdi-tmu-test-setup, term |
| `ps5000` | 11 | chin, drlv, ground-sense-editor, logical-boards, match-loops, rclv, setup-level-set-0, smartrdi, term |
| `flow-control-node` | 9 | assign-value-node, built-in-functions, flag, flow-sequence-editor, group-node, mapping-testflow, testflow, testflow-tool |
| `test-method-project` | 8 | add-limit, how-to-create-a-universal-test-method-class, mapping-testmethod, pin-string, project-explorer-view, smartcalc-framework, testmethod, universal-test-method-library |
| `hardware-response-file` | 6 | flow-sequence-editor, hardware-response-emulator, mapping-run, run, testflow-tool |
| `drldump` | 4 | edl-file, mapping-results, results |
| `technology-file` | 4 | level, project, rdi-configure-file |
| `print-node` | 3 | assign-value-node, mapping-testflow, testflow |
| `switch-version-command-line-tool` | 3 | mapping-project, project |
| `workspace` | 3 | new-device-wizard, project, project-explorer-view |
| `ctim` | 2 | primary-status, timing |
| `list-of-test-result-commands` | 2 | mapping-results, results |
| `org-file` | 2 | mapping-project, project |
| `shared-leakage-parallel-test` | 2 | shared-continuity-test, sharing-configuration-file |
| `gio-library-api` | 1 | project |
| `initialize` | 1 | testmethod |

> 九页之间的互链见第五类；本类只看**指向未建页**的链接。

## 第九类 · 命名合规（**schema §5**）

- **乙 · 文件名本身**：**506 个文件**逐个验过，**0 个不合 §5**。
- **丙 · stem 唯一**：506 个文件占 **506 个 stem**，**0 个撞名**。
- **甲 · 链接目标**：内容页引用 **7544** 处，其中 **0 个目标不合 §5**。
- ⚠️ **语法节整段不参与链接检查**：**322 页**有脚本写的语法节，已整段切掉（`add-limit`、`alias-set-editor`、`alphabetical-list-of-flags`、`analysis-views`、`apg-pattern-file`、`apg-program-file`、`aprm`、`assign-value-node`…）。
  **理由**：那一段是 §4 规定**脚本写、LLM 一个字不许改**的逐字原文，它由**第十二类**用更硬的口径管（页面 ↔ 脚本逐字节一致）。实测 `concepts/command-reference.md` 的语法节里抄着 pattern master file 的格式，而**那个格式自己就用 `[[path: …]]`**——不切，甲就会报一个名叫 `path:` 的「下划线分隔」违规，**而那是假红**。

- ✅ 甲无违规。
## 第十类 · 语料重复投放

- 物理文档 **9,398** 篇 → 唯一 TDC 页 **8,786** 个（无 `source_topic` 的 5 篇是各章 `index.md`）。
- 重复投放：**504** 个页，涉及 1,111 篇，**冗余 607 篇**。

**为什么这件事必须记下来：**

1. `hubs.csv` 的 `in_src` 会被灌水——同一篇页存在 5 份，就有 5 份引用各记一次。
   实测 `WSUS` 121 → **62**、`PSFC` 119 → 约六成。**index.md 的建页优先级表按旧数排的。**
2. 页面 `sources:` 里同篇列两个路径，会让「677 条来源」这种计数虚高。
3. 「两篇文档都说 X」可能只是**一篇被投了两次**——§10 的冲突判定必须先做这一步。

| source_topic | 份数 | 投放位置 |
|---|---|---|
| `98606` | 5 | 02.06.02.02.125_FTCG__FTCG__-__Functional_Test_ConfiGure.md<br>02.06.05.02.11_FTCG__FTCG__-__Functional_Test_ConfiGure.md<br>02.06.06.02.19_FTCG__FTCG__-__Functional_Test_ConfiGure.md<br>02.08.04.34.02.02.19_FTCG__FTCG__-__Functional_Test_ConfiGure.md<br>03.03.04.04.02_FTCG__FTCG__-__Functional_Test_ConfiGure.md |
| `98723` | 5 | 02.06.02.02.210_RSET_-__ReSET.md<br>02.06.05.02.19_RSET_-__ReSET.md<br>02.06.06.02.23_RSET_-__ReSET.md<br>02.06.07.02.22_RSET_-__ReSET.md<br>02.08.04.34.02.02.23_RSET_-__ReSET.md |
| `98578` | 5 | 02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md<br>02.06.03.02.13_DSCP__DSCP__-__Define_System_Control_Parameter.md<br>02.06.04.02.01_DSCP__DSCP__-__Define_System_Control_Parameter.md<br>02.06.06.02.10_DSCP__DSCP__-__Define_System_Control_Parameter.md<br>02.08.04.34.02.02.10_DSCP__DSCP__-__Define_System_Control_Parameter.md |
| `98485` | 4 | 02.06.02.02.03_APRM_-__Activate_PRiMary_sets.md<br>02.06.05.02.01_APRM_-__Activate_PRiMary_sets.md<br>02.06.06.02.01_APRM_-__Activate_PRiMary_sets.md<br>02.08.04.34.02.02.01_APRM_-__Activate_PRiMary_sets.md |
| `98585` | 4 | 02.06.02.02.100_EDDC__-__EDge_in_Device_Cycle.md<br>02.06.06.02.11_EDDC__-__EDge_in_Device_Cycle.md<br>02.06.09.02.04_EDDC__-__EDge_in_Device_Cycle.md<br>02.08.04.34.02.02.11_EDDC__-__EDge_in_Device_Cycle.md |

> **§10 冲突判定的前置步骤：先查是不是同篇重复投放，再谈版本、再谈并列。**

## 第十一类 · 层断言的一致性（**跨页**）

- 覆盖 157 个对象、211 行。
- ✅ 没有对象在两页里被标成**不同的层**。
- ℹ️ 3 个对象只是**措辞不同、层相同**：
    - `spec-value`：level=L2 / testmethod=L2 参数类型
    - `spec-variable`：level=L2 / testmethod=L2 参数类型
    - `tmlimits`：testmethod=L2 + file / results=L2/file

### 第十一类续 · 对象页 `layer:` vs 舞台页表格

| 对象页 | 对象 | 页里 `layer:` | stage 表格里写的 | 一致 |
|---|---|---|---|---|
| `concepts/context-pins.md` | How to create a universal test method cl | `L2` | testmethod=L2 参数类型 | ✅ |
| `concepts/edf.md` | Event Data Logging Format (EDF) | `file` | results=file | ✅ |
| `concepts/flag.md` | Flags | `n/a` | testflow=n/a | ✅ |
| `concepts/offline-result-emulation.md` | Offline Result Emulation | `n/a` | run=n/a | ✅ |
| `concepts/waveform-set.md` | Waveform and timing sets | `n/a` | timing=n/a | ✅ |
| `objects/add-limit.md` | addLimit | `L2` | testmethod=L2 | ✅ |
| `objects/aprm.md` | APRM - (Activate PRiMary sets) | `L1` | level=L1 / timing=L1 | ✅ |
| `objects/assign-value-node.md` | Assign Value node | `gui` | testflow=gui | ✅ |
| `objects/begin-extension.md` | BEGIN_EXTENSION | `L2` | testmethod=L2（L1 通道） | ✅ |
| `objects/bin.md` | Bins | `n/a` | testflow=n/a | ✅ |
| `objects/built-in-functions.md` | Built-in functions | `gui` | testflow=gui | ✅ |
| `objects/bwdf.md` | BWDF, BWDF? - (Break Waveform DeFinition | `L1` | timing=L1 | ✅ |
| `objects/bwds.md` | BWDS, BWDS? - (Break Waveform Definition | `L1` | timing=L1 | ✅ |
| `objects/cct-change-level-spec.md` | CCTchangeLevelSpec | `L2` | level=L2 | ✅ |
| `objects/change-device-wizard.md` | Change Device wizard | `gui` | project=gui | ✅ |
| `objects/ci-cpi.md` | Command Set Programming Interface | `L3` | testflow=L3 | ✅ |
| `objects/clkr.md` | CLKR, CLKR? - (CLocK Resolution) | `L1` | timing=L1 | ✅ |
| `objects/clmp.md` | CLMP, CLMP? - (CLaMP level) | `L1` | level=L1 | ✅ |
| `objects/connect.md` | CONNECT | `L2` | testmethod=L2 | ✅ |
| `objects/data-logging-profiles.md` | Data Logging Profiles | `file` | results=file | ✅ |
| `objects/data-retrieval-library.md` | Data Retrieval Library | `L2` | results=L2 | ✅ |
| `objects/dcdt.md` | DCDT, DCDT? - (Device Cycle DefaulT) | `L1` | timing=L1 | ✅ |
| `objects/debug-perspective.md` | Debug perspective | `gui` | run=gui | ✅ |
| `objects/debug-view.md` | Debug View | `gui` | run=gui | ✅ |
| `objects/device-directory.md` | Device directory structure | `file` | project=file | ✅ |
| `objects/device-license-file.md` | The device license file | `file` | project=file | ✅ |
| `objects/device-technology-directory.md` | Device Technology Directory | `file` | project=file | ✅ |
| `objects/disconnect.md` | DISCONNECT | `L2` | testmethod=L2 | ✅ |
| `objects/dprl.md` | DPRL, DPRL? - (Default PRimary Level set | `L1` | level=L1 | ✅ |
| `objects/dprt.md` | DPRT, DPRT? - (Default PRimary Timing se | `L1` | timing=L1 | ✅ |
| `objects/drlv.md` | DRLV, DRLV? - (DRive LeVel) | `L1` | level=L1 | ✅ |
| `objects/dscp.md` | DSCP, DSCP? - (Define System Control Par | `L1` | project=L1 / level=L1 | ✅ |
| `objects/dsus.md` | DSUS, DSUS? - (Dps Sets USed) | `L1` | level=L1 | ✅ |
| `objects/dtcp.md` | DTCP, DTCP? - (Define Technology Control | `L1` | project=L1 | ✅ |
| `objects/edl-file.md` | The V93000 Data Logging Architecture | `file` | results=file | ✅ |
| `objects/edsp.md` | EDSP, EDSP? - (EDge SPecification) | `L1` | timing=L1 | ✅ |
| `objects/end-extension.md` | END_EXTENSION | `L2` | testmethod=L2（L1 通道） | ✅ |
| `objects/eqfs.md` | EQFS - (EQuation FileS command transfer) | `L1` | level=L1 / timing=L1 | ✅ |
| `objects/eqsp.md` | EQSP, EQSP? - (EQuation SPecification tr | `L1` | level=L1 / timing=L1 | ✅ |
| `objects/error-map-tool.md` | Error Map Tool | `gui` | run=gui / results=gui | ✅ |
| `objects/error-map.md` | Error Map | `file` | results=file | ✅ |
| `objects/etds.md` | ETDS, ETDS? - (Edge Timing Definition St | `L1` | timing=L1 | ✅ |
| `objects/etim.md` | ETIM, ETIM? - (Edge TIMing) | `L1` | timing=L1 | ✅ |
| `objects/event-formatter.md` | Event Formatter | `gui` | results=gui | ✅ |
| `objects/execution-context.md` | Using execution contexts | `L2` | run=L2 | ✅ |
| `objects/file-string.md` | How to create a universal test method cl | `L2` | testmethod=L2 参数类型 | ✅ |
| `objects/flags-page.md` | Flags page | `gui` | run=gui | ✅ |
| `objects/flow-data-editor.md` | Flow Data Editor | `gui` | testflow=gui | ✅ |
| `objects/flow-sequence-editor.md` | Flow Sequence Editor | `gui` | testflow=gui / run=gui | ✅ |
| `objects/for-each-site-begin.md` | FOR_EACH_SITE_BEGIN | `L2` | testmethod=L2 | ✅ |
| `objects/for-each-site-end.md` | FOR_EACH_SITE_END | `L2` | testmethod=L2 | ✅ |
| `objects/fw-task.md` | FW_TASK | `L2` | testmethod=L2（L1 通道） | ✅ |
| `objects/group-node.md` | Group node | `gui` | testflow=gui | ✅ |
| `objects/hardware-response-emulator.md` | Hardware Response Emulator | `gui` | run=gui | ✅ |
| `objects/hardware-view.md` | Hardware view | `gui` | run=gui | ✅ |
| `objects/integrated-result-tool.md` | Integrated Result Tool | `gui` | results=gui | ✅ |
| `objects/level-equation-file.md` | Level equation file | `file` | level=file | ✅ |
| `objects/level-file.md` | Structure of an equation based level set | `file` | level=file | ✅ |
| `objects/level-master-file.md` | Level setup master file | `file` | level=file | ✅ |
| `objects/level-set-selector.md` | LevelSetSelector | `L2` | level=L2 | ✅ |
| `objects/level-setup-tool.md` | Level setup tool | `gui` | level=gui | ✅ |
| `objects/level-spec.md` | LEVEL_SPEC | `L2` | level=L2 | ✅ |
| `objects/limit.md` | LIMIT | `L2` | testmethod=L2 | ✅ |
| `objects/lot-summary-generator.md` | LotSummaryGenerator | `L1` | results=L1 | ✅ |
| `objects/lsus.md` | LSUS, LSUS? - (Level Sets USed) | `L1` | level=L1 | ✅ |
| `objects/lsux.md` | LSUX, LSUX? - (Level Sets Used eXtended) | `L1` | level=L1 | ✅ |
| `objects/model-file.md` | The model file | `file` | project=file | ✅ |
| `objects/new-device-wizard.md` | New Device wizard | `gui` | project=gui | ✅ |
| `objects/on-first-invocation-begin.md` | ON_FIRST_INVOCATION_BEGIN | `L2` | testmethod=L2 | ✅ |
| `objects/on-first-invocation-end.md` | ON_FIRST_INVOCATION_END | `L2` | testmethod=L2 | ✅ |
| `objects/option-list.md` | How to create a universal test method cl | `L2` | testmethod=L2 参数类型 | ✅ |
| `objects/pattern-tool.md` | Pattern Tools | `gui` | run=gui | ✅ |
| `objects/pclk.md` | PCLK, PCLK? - (Pin CLocK) | `L1` | timing=L1 | ✅ |
| `objects/pdiv.md` | PDIV? - (Period DIVider) | `L1` | timing=L1 | ✅ |
| `objects/pin-string.md` | How to create a universal test method cl | `L2` | testmethod=L2 参数类型 | ✅ |
| `objects/primary-status.md` | PRIMARY_STATUS - (Primary) | `L2` | level=L2 / timing=L2 | ✅ |
| `objects/project-explorer-view.md` | Project Explorer view | `gui` | project=gui | ✅ |
| `objects/pslv.md` | PSLV, PSLV? - (Power Supply LeVel) | `L1` | level=L1 | ✅ |
| `objects/pssr.md` | PSSR, PSSR? -(Power Supply Slew Rate) | `L1` | level=L1 | ✅ |
| `objects/rclv.md` | RCLV, RCLV? - (ReCeive LeVel) | `L1` | level=L1 | ✅ |
| `objects/report-window.md` | Report window | `gui` | run=gui / results=gui | ✅ |
| `objects/rset.md` | RSET - (ReSET) | `L1` | level=L1 | ✅ |
| `objects/run-dialog.md` | Running a testflow | `gui` | run=gui | ✅ |
| `objects/setup-level-set-0.md` | SetupLevelSet0 | `L2` | level=L2 | ✅ |
| `objects/setup-management-tool.md` | Setup Management Tool | `gui` | project=gui / testflow=gui | ✅ |
| `objects/setup-perspective.md` | Setup perspective | `gui` | project=gui | ✅ |
| `objects/shmoo-tool.md` | Shmoo Tool | `gui` | results=gui | ✅ |
| `objects/signal-analyzer.md` | Signal Analyzer | `gui` | results=gui | ✅ |
| `objects/site-control-window.md` | Site Control Window | `gui` | run=gui | ✅ |
| `objects/sldo.md` | SLDO - (Switch Level and Dps Order) | `L1` | level=L1 | ✅ |
| `objects/smartest-data-formatter.md` | SmarTest Data Formatter | `gui` | results=gui/file | ✅ |
| `objects/spec-search.md` | SPEC_SEARCH | `L2` | timing=L2 | ✅ |
| `objects/spec-set.md` | Spec sets | `L2` | level=L2 | ✅ |
| `objects/spec-tool.md` | Spec Tool | `gui` | level=gui / timing=gui | ✅ |
| `objects/spec-value.md` | SpecValue | `L2` | level=L2 / testmethod=L2 参数类型 | ✅ |
| `objects/spec-variable.md` | SpecVariable | `L2` | level=L2 / testmethod=L2 参数类型 | ✅ |
| `objects/sprm.md` | SPRM, SPRM? - (Set PRiMary sets) | `L1` | level=L1 / timing=L1 | ✅ |
| `objects/spst.md` | SPST? - (SPecset STatus) | `L1` | level=L1 / timing=L1 | ✅ |
| `objects/sqst.md` | SQST, SQST? - (SeQuencer STate) | `L1` | level=L1 | ✅ |
| `objects/stdf.md` | Starting the formatter | `file` | results=file | ✅ |
| `objects/stpm-control-file.md` | STPM control file | `file` | project=file | ✅ |
| `objects/stpm-merge-rules-file.md` | STPM merge rules file | `file` | project=file | ✅ |
| `objects/stpm.md` | SmarTest Program Manager | `L3` | project=L3 / testflow=L3 | ✅ |
| `objects/strs.md` | STRS? - (Spec TRansition Search) | `L1` | timing=L1 | ✅ |
| `objects/svlr.md` | SVLR, SVLR? - (Spec VaLues at Runtime) | `L1` | level=L1 / timing=L1 | ✅ |
| `objects/term.md` | TERM, TERM? - (TERMination mode) | `L1` | level=L1 | ✅ |
| `objects/test-method-class.md` | 2. Create a Test Method Class | `gui` | testmethod=gui | ✅ |
| `objects/test-program-explorer.md` | Test Program Explorer | `gui` | project=gui | ✅ |
| `objects/test-suite.md` | Test suites | `n/a` | testflow=n/a | ✅ |
| `objects/test-suites-page.md` | Test Suites page | `gui` | run=gui | ✅ |
| `objects/test.md` | TEST | `L2` | testmethod=L2 | ✅ |
| `objects/testflow-analyzer-tool.md` | The Testflow Analyzer Tool (TAT) | `L3` | project=L3 | ✅ |
| `objects/testflow-file.md` | Testflow file | `file` | testflow=file / run=file | ✅ |
| `objects/testflow-master-file.md` | Testflow master file | `file` | testflow=file | ✅ |
| `objects/testflow-properties-view.md` | Testflow Properties view | `gui` | testflow=gui | ✅ |
| `objects/testflow-tool.md` | Testflow Tool | `gui` | testflow=gui / run=gui | ✅ |
| `objects/testflow-variable.md` | Testflow variable mapping table | `file` | testflow=file | ✅ |
| `objects/testset.md` | TESTSET | `L2` | testmethod=L2 | ✅ |
| `objects/timing-diagram-tool.md` | Timing Diagram Tool | `gui` | timing=gui / run=gui / results=gui | ✅ |
| `objects/timing-equation-set.md` | Timing equation set reference | `file` | timing=file | ✅ |
| `objects/timing-file.md` | Data organization of equation based timi | `file` | timing=file | ✅ |
| `objects/timing-master-file.md` | Timing setup master file | `file` | timing=file | ✅ |
| `objects/timing-set-selector.md` | TimingSetSelector | `L2` | timing=L2 | ✅ |
| `objects/timing-setup-tool.md` | Timing Setup Tool | `gui` | timing=gui | ✅ |
| `objects/timing-spec.md` | TIMING_SPEC | `L2` | timing=L2 | ✅ |
| `objects/timing-specification.md` | Defining the timing specification | `file` | timing=file | ✅ |
| `objects/tmlimits.md` | TMLimits | `L2` | testmethod=L2 + file / results=L2/file | ✅ |
| `objects/tpt-generate-device-dir.md` | tpt_generate_device_dir | `L3` | project=L3 | ✅ |
| `objects/tpt-import-from-device.md` | tpt_import_from_device | `L3` | project=L3 | ✅ |
| `objects/tsus.md` | TSUS, TSUS? - (Timing Sets USed) | `L1` | timing=L1 | ✅ |
| `objects/tsux.md` | TSUX, TSUX? - (Timing Sets Used eXtended | `L1` | timing=L1 | ✅ |
| `objects/universal-test-method-library.md` | Developing a universal test method libra | `file` | testmethod=file | ✅ |
| `objects/uptd.md` | UPTD, UPTD? - (UP To Date) | `L1` | level=L1 / timing=L1 | ✅ |
| `objects/utility-line-view.md` | Utility Line view | `gui` | run=gui | ✅ |
| `objects/vclk.md` | VCLK? - (Verify CLocK) | `L1` | timing=L1 | ✅ |
| `objects/vdcg.md` | VDCG? - (Verify Device Cycle for Group) | `L1` | timing=L1 | ✅ |
| `objects/vtim.md` | VTIM? - (Verify TIMing) | `L1` | timing=L1 | ✅ |
| `objects/vwfg.md` | VWFG? - (Verify WaveForms in Groups) | `L1` | timing=L1 | ✅ |
| `objects/vwfs.md` | VWFS? - (Verify WaveForm Sets) | `L1` | timing=L1 | ✅ |
| `objects/wave.md` | WAVE, WAVE? - (WAVEform) | `L1` | timing=L1 | ✅ |
| `objects/waveform-view.md` | Waveform View | `gui` | timing=gui | ✅ |
| `objects/wavetable-file.md` | Wavetable file | `file` | timing=file | ✅ |
| `objects/wavetable.md` | wavetable | `n/a` | timing=n/a | ✅ |
| `objects/wfds.md` | WFDS, WFDS? - (WaveForm Definition Strin | `L1` | timing=L1 | ✅ |
| `objects/wsus.md` | WSUS, WSUS? - (Waveform Sets USed) | `L1` | timing=L1 | ✅ |

- ℹ️ 201 页的层**没有第二处可以对照**（表格里没有它）——这不是错，是「**这层只有页自己说了算，机器无从复核**」：
    - `concepts/command-reference.md` — `layer: n/a`
    - `concepts/controlling-multiple-sites.md` — `layer: n/a`
    - `concepts/dc-test-programming.md` — `layer: n/a`
    - `concepts/direct-probe-stiffener.md` — `layer: n/a`
    - `concepts/dut-board-design-reference.md` — `layer: n/a`
    - `concepts/dut-board-grounding.md` — `layer: n/a`
    - `concepts/dut-interface-layout.md` — `layer: n/a`
    - `concepts/edf-data-organization.md` — `layer: n/a`
    - `concepts/edf-data-types.md` — `layer: n/a`
    - `concepts/equation-based-level-setup.md` — `layer: n/a`
    - `concepts/ganging.md` — `layer: n/a`
    - `concepts/gpib-lan-communication-conventions.md` — `layer: L3`
    - `concepts/how-to-create-a-universal-test-method-class.md` — `layer: n/a`
    - `concepts/hv-protection.md` — `layer: n/a`
    - `concepts/inter-layer-via-design.md` — `layer: n/a`
    - `concepts/layout-information-dut-board.md` — `layer: n/a`
    - `concepts/logical-boards.md` — `layer: n/a`
    - `concepts/pogo-block-compatibility.md` — `layer: n/a`
    - `concepts/pogo-pad-and-via-design.md` — `layer: n/a`
    - `concepts/sequencer-controlled-utility-lines.md` — `layer: n/a`
    - `concepts/setting-chart-display-options.md` — `layer: n/a`
    - `concepts/setting-up-a-shmoo-test-with-the-shmoo-tool.md` — `layer: n/a`
    - `concepts/setting-up-dc-scale-pins-with-smartrdi.md` — `layer: n/a`
    - `concepts/smartrdi-tmu-test-setup.md` — `layer: n/a`
    - `concepts/smartrdi-vector-and-protocol-programming.md` — `layer: n/a`
    - `concepts/test-number-generator-and-tmlimits.md` — `layer: n/a`
    - `concepts/timing-setup-commands.md` — `layer: n/a`
    - `concepts/utility-lines.md` — `layer: n/a`
    - `constraints/constraint-level-mode-context-match.md` — `layer: L1`
    - `constraints/constraint-timing-mode-context-match.md` — `layer: L1`
    - `constraints/cross-card-ganging-requires-ddic.md` — `layer: L1`
    - `constraints/execution-context-requires-firmware-definition.md` — `layer: L1`
    - `constraints/label-edit-requires-tstl-selection.md` — `layer: L1`
    - `constraints/pals-before-other-setup.md` — `layer: L1`
    - `constraints/pin-config-locked-during-test.md` — `layer: L1`
    - `constraints/pin-config-requires-sequencer-off.md` — `layer: L1`
    - `constraints/rdi-call-requires-begin-end-block.md` — `layer: L1`
    - `constraints/referenced-set-requires-prior-definition.md` — `layer: L1`
    - `constraints/site-focus-required-before-command.md` — `layer: L1`
    - `constraints/smc-background-process-locks-config.md` — `layer: L1`
    - `constraints/synchronized-pins-require-same-test-processor.md` — `layer: L1`
    - `constraints/testname-requires-matching-limits.md` — `layer: L1`
    - `mappings/mapping-level.md` — `layer: n/a`
    - `mappings/mapping-pattern.md` — `layer: n/a`
    - `mappings/mapping-pin.md` — `layer: n/a`
    - `mappings/mapping-project.md` — `layer: n/a`
    - `mappings/mapping-results.md` — `layer: n/a`
    - `mappings/mapping-run.md` — `layer: n/a`
    - `mappings/mapping-testflow.md` — `layer: n/a`
    - `mappings/mapping-testmethod.md` — `layer: n/a`
    - `mappings/mapping-timing.md` — `layer: n/a`
    - `objects/alias-set-editor.md` — `layer: gui`
    - `objects/alphabetical-list-of-flags.md` — `layer: L3`
    - `objects/analysis-views.md` — `layer: gui`
    - `objects/apg-pattern-file.md` — `layer: file`
    - `objects/apg-program-file.md` — `layer: file`
    - `objects/cct-multiport-sequencer-synchronizer-api.md` — `layer: L2`
    - `objects/chin.md` — `layer: L1`
    - `objects/conf.md` — `layer: L1`
    - `objects/ctxt.md` — `layer: L1`
    - `objects/data-logging-profile-api.md` — `layer: n/a`
    - `objects/data-navigation-views.md` — `layer: gui`
    - `objects/dc-result-accessor.md` — `layer: L3`
    - `objects/dc-scale-limits-editor.md` — `layer: gui`
    - `objects/dc-scale-uhc4t-card.md` — `layer: n/a`
    - `objects/dc-scale-xps256-card.md` — `layer: n/a`
    - `objects/device-access-file.md` — `layer: file`
    - `objects/device-architecture-file.md` — `layer: file`
    - `objects/device-summary-tab.md` — `layer: gui`
    - `objects/dfge.md` — `layer: L1`
    - `objects/dfgp.md` — `layer: L1`
    - `objects/dfpc.md` — `layer: L1`
    - `objects/dfpn.md` — `layer: L1`
    - `objects/dfpr.md` — `layer: L1`
    - `objects/dfps.md` — `layer: L1`
    - `objects/dfpt.md` — `layer: L1`
    - `objects/dfup.md` — `layer: L1`
    - `objects/dfut.md` — `layer: L1`
    - `objects/digital-capture-test.md` — `layer: L2`
    - `objects/digital-offset-search-pins.md` — `layer: L2`
    - `objects/digital-pins-editor.md` — `layer: gui`
    - `objects/dps-aux-pin-task.md` — `layer: L2`
    - `objects/dps-aux-task.md` — `layer: L2`
    - `objects/dps-pins-editor.md` — `layer: gui`
    - `objects/dps-power-flags-get-functions.md` — `layer: L3`
    - `objects/dps-task.md` — `layer: L2`
    - `objects/dps128-dps64-cards.md` — `layer: n/a`
    - `objects/dpspins-resources.md` — `layer: L2`
    - `objects/event-base.md` — `layer: L3`
    - `objects/event-value-double.md` — `layer: L2`
    - `objects/event-value-int.md` — `layer: L2`
    - `objects/event-waveform-vfim.md` — `layer: L3`
    - `objects/event-waveform-vfvm.md` — `layer: L2`
    - `objects/flex-relay.md` — `layer: L2`
    - `objects/flsh.md` — `layer: L1`
    - `objects/flush.md` — `layer: L2`
    - `objects/gctx.md` — `layer: L1`
    - `objects/get-functional-result.md` — `layer: L2`
    - `objects/get-utility-lines.md` — `layer: L2`
    - `objects/global-section.md` — `layer: file`
    - `objects/ground-sense-editor.md` — `layer: gui`
    - `objects/hardware-bin-summary-tab.md` — `layer: gui`
    - `objects/hidden-upload.md` — `layer: L2`
    - `objects/hw-pin-state.md` — `layer: L2`
    - `objects/hw-state.md` — `layer: L2`
    - `objects/hwty.md` — `layer: L1`
    - `objects/index-objects.md` — `layer: n/a`
    - `objects/jrst.md` — `layer: L1`
    - `objects/jscf.md` — `layer: L1`
    - `objects/jsdf.md` — `layer: L1`
    - `objects/jspr.md` — `layer: L1`
    - `objects/jsud.md` — `layer: L1`
    - `objects/jswf.md` — `layer: L1`
    - `objects/match-loops.md` — `layer: L1`
    - `objects/mscf.md` — `layer: L1`
    - `objects/msdf.md` — `layer: L1`
    - `objects/mtp-maintenance-operations.md` — `layer: n/a`
    - `objects/mtp-memory-test.md` — `layer: L2`
    - `objects/mtp-shared-test-commands.md` — `layer: L2`
    - `objects/mtpt.md` — `layer: file`
    - `objects/multiport-burst-editor.md` — `layer: gui`
    - `objects/pact.md` — `layer: L1`
    - `objects/pals.md` — `layer: L1`
    - `objects/pattern-controller.md` — `layer: L2`
    - `objects/pattern-editor.md` — `layer: gui`
    - `objects/pattern-explorer.md` — `layer: gui`
    - `objects/pattern-master-file.md` — `layer: file`
    - `objects/pattern-object.md` — `layer: L2`
    - `objects/pfnd.md` — `layer: L1`
    - `objects/pin-configuration-file.md` — `layer: file`
    - `objects/pin-configuration-master-file.md` — `layer: file`
    - `objects/pin-configuration-tool.md` — `layer: gui`
    - `objects/pin-group-editor.md` — `layer: gui`
    - `objects/pin-mapping-file.md` — `layer: file`
    - `objects/pin-property-monitor.md` — `layer: L2`
    - `objects/pin-utility.md` — `layer: L2`
    - `objects/play-pattern.md` — `layer: L2`
    - `objects/pogocabling-section.md` — `layer: file`
    - `objects/port-editor.md` — `layer: gui`
    - `objects/pqfc.md` — `layer: L1`
    - `objects/preprocessing-and-postprocessing-scripts.md` — `layer: file`
    - `objects/prlt.md` — `layer: L1`
    - `objects/protocol-editor.md` — `layer: gui`
    - `objects/psas.md` — `layer: L1`
    - `objects/psfc.md` — `layer: L1`
    - `objects/pssl.md` — `layer: L1`
    - `objects/pste.md` — `layer: L1`
    - `objects/raw-data-views.md` — `layer: gui`
    - `objects/rdi-configure-file.md` — `layer: file`
    - `objects/result-configuration.md` — `layer: L2`
    - `objects/sequencer-status.md` — `layer: L3`
    - `objects/sequencer.md` — `layer: L1`
    - `objects/set-utility-lines.md` — `layer: L2`
    - `objects/shared-continuity-test.md` — `layer: n/a`
    - `objects/sharing-configuration-file.md` — `layer: file`
    - `objects/sharing-configuration.md` — `layer: n/a`
    - `objects/smartcalc-framework.md` — `layer: L2`
    - `objects/smartcalc.md` — `layer: L2`
    - `objects/smartrdi.md` — `layer: L2`
    - `objects/smartshell.md` — `layer: n/a`
    - `objects/smc-synchronize.md` — `layer: L2`
    - `objects/smc-test.md` — `layer: L2`
    - `objects/software-bin-summary-tab.md` — `layer: gui`
    - `objects/special-test-suites.md` — `layer: file`
    - `objects/spmu-pin-task-mode.md` — `layer: L3`
    - `objects/spmu-pin-task.md` — `layer: L2`
    - `objects/spmu-task.md` — `layer: L2`
    - `objects/stme.md` — `layer: L1`
    - `objects/structure-of-a-tmlimits-csv-file.md` — `layer: file`
    - `objects/table-filter.md` — `layer: gui`
    - `objects/task-list.md` — `layer: L2`
    - `objects/technology-file-for-a-device.md` — `layer: file`
    - `objects/test-suite-control-api.md` — `layer: L3`
    - `objects/test-summary-tab.md` — `layer: gui`
    - `objects/testset-testname.md` — `layer: L2`
    - `objects/timestamp-attr-type.md` — `layer: file`
    - `objects/tp360.md` — `layer: gui`
    - `objects/tpi-program-routines.md` — `layer: L3`
    - `objects/udef.md` — `layer: L1`
    - `objects/udgp.md` — `layer: L1`
    - `objects/udpr.md` — `layer: L1`
    - `objects/udps.md` — `layer: L1`
    - `objects/udpt.md` — `layer: L1`
    - `objects/udup.md` — `layer: L1`
    - `objects/udut.md` — `layer: L1`
    - `objects/udvp.md` — `layer: L1`
    - `objects/upas.md` — `layer: L1`
    - `objects/utility-card.md` — `layer: n/a`
    - `objects/utility-line-assignments.md` — `layer: n/a`
    - `objects/utility-pins-editor.md` — `layer: gui`
    - `objects/utility-pogo-block-utility-card-v93000-exa-scale-systems.md` — `layer: n/a`
    - `objects/utility-power-supplies.md` — `layer: n/a`
    - `objects/utility-purpose-editor.md` — `layer: gui`
    - `objects/vec-events.md` — `layer: L2`
    - `objects/vector-setup-file.md` — `layer: file`
    - `objects/vpin.md` — `layer: L1`
    - `objects/wafer-summary-tab.md` — `layer: gui`
    - `objects/waveform-mapping.md` — `layer: n/a`
    - `objects/xps256-pmu-operating-mode.md` — `layer: L2`
    - `objects/xps256-programming-dps-operating-mode.md` — `layer: L2`
    - `objects/xps256-status-flags.md` — `layer: L2`

## 第十二类 · 语法节与抽取器当前产出一致（**页面 ↔ 脚本**）

✅ **322 个已建页的 `## 语法 / 参数` 与 `objscaffold.py` 现在的产出逐字一致。**

> **这一条查了哪些、没查哪些，都写出来**（§13.1 第 ⑥′ 问）：逐字比了 **322** 页；**38** 页是纯散文页（`constraint` / `error` / `stage`），按设计没有脚本写的一节，**不参与比较**；
> 判据是**两个方向都封死**的：`object` / `concept` 页**必须**带`<!-- 语法节 begin -->` 标记（没有就是红——旧写法会**静默跳过**它，那正是本文件头说的「检查比自称的范围窄」），带标记的页**一律逐字比**。

> **判据是逐字相等**，不是「看起来差不多」——这一节是脚本写的，它和脚本的输出**必须**是同一个东西。
> 边界靠页面里的 `<!-- 语法节 begin/end -->` 标记认。**没有标记时 `refresh()` 会过一道互锁**：要替换的区间里如果有「非标准小节」，它**拒绝执行**而不是猜边界——这条互锁是拿一次真实误删换来的（`cct-multiport-sequencer-synchronizer-api` 被删掉 6 节，已从会话记录恢复）。
> **底下的教训比这条检查值钱**：脚本对「页面长什么样」的假设，写成判据就会变成删数据的刀。**边界必须由写它的人留记号，不能由读者推断。**

## 第十三类 · 版本页与抽取器一致、且条目逐字回得到 raw（**页面 ↔ 脚本 ↔ raw**）

✅ **142 个版本页没有一个字偏离 `versions.py` 的当前产出**；**7,711 条条目全部逐字回得到 raw 的 `## Functional changes` 段落**。

> **这只证明「转录忠实」，不证明「分对了组」。**把某一条记到错的版本号底下，这一条一样是绿的——而**分组判据（`- SmarTest X: …` 的 `X`）就在原文里写着，机器只认字面**。真要查分组，得人拿几条回原文看。

## 第十四类 · 手写文件的自我声明是不是真的（`index.md` / `wiki-plan.csv` / token 预算）

### 甲 · 每一页都在它那一节里被列出了吗

| 节 | 目录 | 目录里有 | 节里列了 | 漏列 | 列了但不存在 | 列了别的类 |
|---|---|---|---|---|---|---|
| `阶段` | `stages/` | 9 | 9 | ✅ 无 | ✅ 无 | — |
| `概念` | `concepts/` | 33 | 35 | ✅ 无 | ✅ 无 | `cross-card-ganging-requires-ddic`, `utility-line-assignments` |
| `约束` | `constraints/` | 14 | 14 | ✅ 无 | ✅ 无 | — |
| `映射` | `mappings/` | 9 | 9 | ✅ 无 | ✅ 无 | — |
| `对象` | `objects/` | 289 | 298 | ✅ 无 | ✅ 无 | `dut-interface-layout`, `hv-protection`, `inter-layer-via-design`, `pogo-block-compatibility`, `setting-up-a-shmoo-test-with-the-shmoo-tool`, `setting-up-dc-scale-pins-with-smartrdi`, `smartrdi-tmu-test-setup`, `test-number-generator-and-tmlimits`, `utility-lines` |
| `排错` | `errors/` | 6 | 6 | ✅ 无 | ✅ 无 | — |

> **本类不查 `版本` 节**：它不逐页列出——`index.md` 只带一行指针 `[[index-versions]]`，那 143 个文件由**第十三类**管（与 `versions.render()` 逐字节一致 + 条目逐字回 raw）。**被接管的范围要报出来，不然它和「没人管」长得一样。**

> **「列了但不存在」与第八类重叠**，这里是**按节**再看一遍：第八类只知道「有个 `[[ ]]` 指不到东西」，不知道**它写在哪个节里**——而「写在对象节里却指到别处」和「写在正文里指到一个还没建的页」是两件事。

### 乙 · `<!-- index-count: … -->` 标记的数对不对

| 声明 | 标记写的 | 实际 | 结果 |
|---|---|---|---|
| `阶段` | 9 | 9 | ✅ |
| `概念` | 33 | 33 | ✅ |
| `约束` | 14 | 14 | ✅ |
| `映射` | 9 | 9 | ✅ |
| `对象` | 289 | 289 | ✅ |
| `排错` | 6 | 6 | ✅ |
| `已知缺口` | 5 | 5 | ✅ |

### 丙 · 散文里逐条登记的数字声明

| 声明 | 写的 | 实际 | 结果 |
|---|---|---|---|
| 已知缺口（N 条） | `5` | `5` | ✅ |
| 阶段（脊椎，N） | `9` | `9` | ✅ |
| （脊椎 N / 概念 N / 约束 N / 对象 N / 排错 N / 映射 N） | `(9, 33, 14, 289, 6, 9)` | `(9, 33, 14, 289, 6, 9)` | ✅ |

> **登记了 3 条散文声明，本次找到 3 条、全部找到。****「没找到」不判错**（散文会被改写），**但必须印出来**——否则改一次措辞，这条声明就**静默地不再被检查**，而报告照样全绿。
> 没登记进表的散文数字**本类一概不管**：`index.md` 里还有很多「N 页」「N 个」的说法，**它们没有检查**。这一条只覆盖登记在 `IDX_PROSE_CLAIMS` 里的那些。

### 丁 / 戊 · `wiki-plan.csv`（「建什么」的唯一记录）和实际对不对

| 检查 | 判据 | 结果 |
|---|---|---|
| **丁** · `status` 和实际进度一致 | 表里每一行 | ✅ 一致 |
| **戊** · 六个类型目录里每一页都在表里 | 目录 ↔ 表，双向 | ✅ 都有 |
| （反向，**不判错**）表里有、页面还没有 | = 待建 | ℹ️ 0 行 |

> **为什么 戊 不算多此一举**：`index.md` 的甲抓「建好了没登记进目录」，戊 抓「建好了没登记进**计划**」——**是两份不同的账**。上一批真正踩到的坑（`pogocabling-section` / `hv-protection`）**两份账同时漏**，而当时两条检查都不存在。
> **`plan_sync.py` 会回填缺的行**（从页面 frontmatter 抄 type/layer/stage）——**回填不削弱 戊**：它抓的是**下一次**：新页建了却没跑同步、也没进表，照样红。

### 己 · `index.md` 装得下一个 context window 吗（§7 硬约束 < 25,000 token）

| 编码器 | 实测 | 页面自己写的 | 对 25,000 |
|---|---|---|---|
| `cl100k_base` | 9,060 | 9060 | +15,940 |
| `o200k_base` | 7,690 | 7690 | +17,310 |

**取大的那个当上界：`cl100k_base` = 9,060，余 15,940。**

> **这是代理，不是本体**：`tiktoken` 是 OpenAI 的编码器，读这份文件的是 Claude，
> **两家的切分不同**。所以它的用法是「**能证伪『超了』，不能证明『离得远』**」——**那正是这条检查要的**（它只判超没超）。
> **为什么取两个编码器里大的**：宁可虚报，不许漏报。
> **量不出来时计入红**（不是「跳过」）：本机 `tiktoken` 是现装的，换台机器就没有——**那时这条会红，而它应该红**，
> 因为「不知道」和「没超」不是一回事。

**修法**：`python -X utf8 extract/check_index_budget.py --write` 会把页面里的
`<!-- index-token: … -->` 刷成实测值（**换位数时要跑两次才收敛**，
因为标记自己的字符也算在里面）。**超了才拆子索引**——
§7 明令「别把『拆了更整齐』当成『拆』的理由」。

### 庚 · 页面里的「N 字节，M 行」对得上 raw 吗

- 页里「N 字节…」形态 **405** 条；**认到 TDC 号、真被比过** **246** 条；**够不着、没比的 159 条**。
- 比过的里面带行数的 **96** 条。
- 字节：✅ 对得上文件实际大小的 **187**；**口径不同但页面写明了**的 **0**（不算错）；**值错的 0**。
- 行数：错 **0 / 96**（真值取 `wc -l`）。

> **为什么这一条要单独有一节。** 它和「引文逐字」是同一类东西：**可机械复核的断言**。
> 2026-09-20 那批页里出过 **6 处「两篇互为出边」全错**，教训写成了「**能核而不核的，迟早是假的**」——
> 字节和行数和边数一样**就在那儿、一数就知道**，而它此前**一处检查都没有**。
> **两条已知限界**（不藏着）：① 只认「附近有 TDC 号」的写法，**159 条够不着**（文档写成纯路径的认不出）；
> ② 它**不改**页面——改法是 `python -X utf8 extract/fix_doc_stats.py --write`。

## 第十五类 · 散文有没有真的写（**骨架占位符**）

✅ **502 页的正文都写过了**（没有 `（待补）`，也没有残留的骨架注释）。

> **最薄的十节**（只列，不判——理由见本类开头）：
>
> | 字符 | 页 | 节 |
> |---|---|---|
> | 15 | `objects/stpm` | `##############################` |
> | 15 | `objects/stpm-control-file` | `##############################` |
> | 34 | `concepts/dut-board-grounding` | `版本` |
> | 34 | `objects/mtpt` | `版本` |
> | 34 | `objects/preprocessing-and-postprocessing-scripts` | `版本` |
> | 34 | `objects/tp360` | `版本` |
> | 67 | `objects/timestamp-attr-type` | `版本` |
> | 71 | `objects/cct-multiport-sequencer-synchronizer-api` | `限制（`Limitations` 段原文，全部是「不支持」）` |
> | 74 | `objects/dfge` | `版本` |
> | 74 | `objects/dtcp` | `版本` |

> **为什么这一条不能只看文件在不在**：`wiki-plan.csv` 的 `status` 曾经只有 `todo` / `done` 两个值，判据是「文件在不在」——**于是 68 页骨架也记成 `done`**。现在它是三个值（`todo` / `skeleton` / `done`），判据和本类**同一处实现**（`plan_sync.is_skeleton()`），第十四类丁 也调它。

## 汇总

| 检验 | 结果 |
|---|---|
| 第一类 九页与十节齐备 | ✅ 通过 |
| 第二类 frontmatter 必填 | ✅ 通过 |
| 第三类 sources 可追溯 | ✅ 通过 |
| 第四类 分类号存在 | ✅ 通过 |
| 第五类 下一步链 | ✅ 通过 |
| 第六类 候选归属覆盖 | ✅ 通过 |
| 第七类 引文逐字 | ✅ 通过 |
| 第八类 链接目标可达 | — 记录 |
| 第九类 命名合规 | ✅ 通过 |
| 第十类 重复投放 | — 记录 |
| 第十一类 层断言一致性 | ✅ 通过 |
| 第十二类 语法节新鲜度 | ✅ 通过 |
| 第十三类 版本页新鲜度 | ✅ 通过 |
| 第十四类 自我声明 | ✅ 通过 |
| 第十五类 散文已写（无骨架占位符） | ✅ 通过 |

**第六类的 ❌ 是怎么灭的（2026-09-18）**：建了 **352 个 `stage` 之外的页**，由各页 frontmatter 的 `sources:` 把候选逐个认领。
（另有 **143 个文件在 `wiki/versions/`**——142 个版本页 + 一个目录页。它们的 `sources:` 意思是「这篇文档里有一条这个版本的变更记录」，**不是「本页讲的是它」**，所以**不参与第六类**，见 `MECH_TYPES`。）
**这一条不用再盯了**——但注意它**只证明「每个高入度候选都有归宿」，不证明「当归宿的那页写得对」**。

**十五类全绿只证明：格式齐、引的文档真的存在、引的句子真的在原文里、候选没漏、链接不悬空、命名统一、同一对象没被两页标成不同层、脚本写的那一节和脚本的产出是同一个东西、版本页的条目逐字回得到 raw、`index.md` 每节列出的页和目录里的文件互相都对得上、**每一页的散文都真的写过了（不是 `（待补）` 骨架）**。**
**不证明内容对。**「文档事实 / 推断 / 建议」分得对不对、**层判得对不对**、边界（testflow vs run、run vs results）守得对不对——
这些机器判不了，**必须人读**。读之前别把 stage 页当可信输入。

> **注意区分**：第十一类只判「两页说法一不一致」，**不判「哪层对」**。
> 「对象属于哪层」试过用文档章节推，4 条全是误报——章节结构里没有这个信息。
> 所以「层判得对」仍在「必须人读」那一栏里。

> 第八、九、十类报的多是**建页 backlog 与结构事实**，不是页面错误：
> 第八类的悬空目标是「脊椎已经伸手去要的页」；
> 第九类是「同一对象被写成多个 slug」——建页前不收掉就会建出重复页（§13 那条）；
> 第十类是语料自身的重复投放，影响一切计数。

