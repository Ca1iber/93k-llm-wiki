---
type: object
title: Test Suites page
layer: gui
stage: testflow
tags: [testflow, gui, flow-data-editor, test-suite, test-suite-flag, annotation, consistency-check]
related: [testflow, testflow-tool, flow-data-editor, flow-sequence-editor, test-suite, special-test-suites, testflow-properties-view, alphabetical-list-of-flags, test-suite-control-api, site-control-window]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.01_Test_Suites_page.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Test Suites page

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,398 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.01_Test_Suites_page.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Wide green border | Passed test suite. |
|---|---|
| Wide red border | Failed test suite. |
| Narrow green border | Test suite which has been set to pass. |
| Narrow red border | Test suite which has been set to fail. |
| Narrow yellow border | Test suite which has been set to bypass. |

### Tables（脚本逐字抽取，第 2 张）

| !`1t`（raw: `../../../../agent-html/110947.png`） / !`Hide primary setup columns`（raw: `../../../../agent-html/110950.png`） | Show or hide the test setup columns |
|---|---|
| !`Primary setup columns`（raw: `../../../../agent-html/110946.png`） / !`2p`（raw: `../../../../agent-html/110951.png`） | Show or hide the primary setup columns |
| !`Show result columns`（raw: `../../../../agent-html/110948.png`） / !`2p`（raw: `../../../../agent-html/110952.png`） | Show or hide the result columns |
| !`Show testsuite flag columns`（raw: `../../../../agent-html/110949.png`） / !`Hide testsuite flag columns`（raw: `../../../../agent-html/110953.png`） | Show or hide the test suite flag columns |
| !`Show all columns icon`（raw: `../../../../agent-html/110688.png`） | Show all columns |
| !`Validate setups icon`（raw: `../../../../agent-html/111383.png`） | Validate setups<br><br>Clicking this button highlights any invalid testflow setup (where setup files have not been loaded or the selected setting does not exist in the setup files) the equation or set number in yellow and displays the annotation. You can hover over the annotation to see the detailed information. |

<!-- 语法节 end -->

## 是什么

**Test Suites page 是 Flow Data Editor 里那张「一行一个 test suite」的表。** 第一句就把职责讲全了：

> 「On the Test Suites page, you can add or delete special test suites and floating test suites. You can also edit the settings of every test suite on this page.」

**它的第二个卖点是批量改**（原文自己把它单列成一句）：

> 「The Test Suites page makes it easy to do batch setups.」

批量的两条路，原文各一句：

> 「You can copy the content of one cell and then paste it into several cells.」

> 「You can copy the content of a range of cells to a text editor, edit the content in this text editor, and paste the modified content back into the Test Suites page.」

**即：这张表认剪贴板，也认「导出到文本编辑器改完再粘回来」。**

### 页上三种 test suite，用背景色区分

> 「Three types of test suites are shown on this page:」

| 种类 | 怎么认 |
|---|---|
| `"Run"` 与 `"Run and Branch"` test suite | **原文没给颜色** |
| **Special test suite** | **青色背景**（`cyan background`） |
| **Floating test suite** | **灰色背景**（`gray background`） |

**`Floating test suite` 是什么，本文档一句都没解释**——它只给了一个灰底作识别特征，
并把它链到 `Floating test suite`（**未建，本页没读**）。

### 列分五组

> 「The Test Suites page displays test suite settings in the columns described below.」

| 列组 | 装什么 | 本页的图证 |
|---|---|---|
| **Test Setup columns** | 这个 test suite 跑什么测试 | ④ `125597.png` / `125588.png`（`Ty...` 0 命中） |
| **Primary Settings columns** | timing / level / analog setup / pattern | **不算 ④** `110689.png`（`Timing` / `Eqn` / `Desc` / `Spec/Waveform Set` 四个串**都搜得到**） |
| **Result columns** | 跑完之后的执行信息 | ④ `111670.png`（`#1 Pass/Fail` 等 0 命中） |
| **Test suite flags columns** | 控制输出的那些 flag | **不算 ④** `110690.png`（11 个列名**都搜得到**） |
| **Test suite Comment column** | 注释 | ④ `111670.png`（`Test Suite Comment` 0 命中） |

（**「④」= §11.4 的图证档**——判据只有一条：**图里的那个串在 raw 里 grep 不到（0 篇）**；
**搜得到的图不占 ④ 档**，本页逐张的判据写在「出处」那张表里，图与正文对不上的几处写在「出处」的 ⚠️ 里。）

### Test Setup columns：`Type` 只能是 `M`

> 「In these columns, you can define the test executed by this test suite. The Type column specifies which kind of test the test suite executes. It can only be M for test method.」

**本页语料只点名了 `Type` 一列**。**图证 ④**：`125597.png` 与 `125588.png` 两张截图里，
这块的表头是一个跨列的 `Test Setup` 组名，下面两列是 **`Ty...`（被箭头挡住后半，值全是 `M`）** 与 **`Name`**
——**`Name` 这一列名在本文档正文里一个字都没有**。

### Primary Settings columns：正文只说了一句话，图给了三个子列名

> 「These columns include the timing, level, analog setup, and pattern settings.」

**正文到此为止**——它**没有列这四个子组各自有哪些列**。
**这张图不算 ④**（按 §11.4 的判据实测：`Timing` 733 篇 / `Eqn` 29 篇 / `Desc` 2,010 篇 /
`Spec/Waveform Set` 1 篇，**四个串全搜得到，没有一个是 0 命中**）。
`110689.png` 的 alt 正是 `Primary Settings columns on the Testsuites page`，
图上这一块的组名是 **`Timing`**，它跨住三个子列：**`Eqn`** / **`Desc`** / **`Spec/Waveform Set`**。
**这三个列名本文档正文里一个都没有**——**但「本文档正文里没有」不等于「raw 里搜不到」**，
按 §11.4 只能算「图补了正文没列的名字」，不占 ④ 档。
（图上这一屏只露出 timing 这一组；另三个子组 `level` / `analog` / `pattern` 不在这一屏里。）

### Result columns：五档边框颜色，加两条多 site 规则

> 「In these columns, you can check the execution information after running the test suite or the whole testflow. On the Result columns of the Test Suites page, the borders of the executed test suites change colors.」

**边框颜色是这一页最实用的一张表**（原表五行，逐字）：

| 边框 | 含义 |
|---|---|
| **宽绿**（`Wide green border`） | 通过的 test suite（`Passed test suite.`） |
| **宽红**（`Wide red border`） | 失败的 test suite（`Failed test suite.`） |
| **窄绿**（`Narrow green border`） | **被置成 pass** 的 test suite（`Test suite which has been set to pass.`） |
| **窄红**（`Narrow red border`） | **被置成 fail** 的 test suite（`Test suite which has been set to fail.`） |
| **窄黄**（`Narrow yellow border`） | **被置成 bypass** 的 test suite（`Test suite which has been set to bypass.`） |

**「宽 = 真结果，窄 = 人手设的」——这条区分是这张表的全部要点。**

> 「If you change the testflow after current execution, the borders of all test suites become dashed lines.」

**多 site 两条规则**：

> 「For multisite testing, if the Test Suites page is set to show the results of all sites, the test suite borders of all sites are green only when all sites are pass. If one site fails, the test suites for all sites appear with red borders.」

> 「If the Test Suites page is set to show the result of the site in focus only, the test suite border changes color according to the result of the site in focus. Passed test suites appear with green borders and failed test suites appear with red borders without considering the results of the sites not in focus.」

**即：显示全部 site 时「一个 site 失败 = 全列红」；只显示 focus site 时只按 focus site 上色。**
另外还有一个开关：

> 「For multisite testing, if you activate Show All Sites in the Preferences window, the results for all sites are displayed.」

（**原文没有说 `Show All Sites` 与上面第一种模式是不是同一件事**——两处本页并列，不替它合并。）

**三个数据列**（原文表）：

> 「The table below explains the meaning of each column.」

| 列 | 含义 |
|---|---|
| `Pass/Fail` | 测试结果 |
| `Exec Time (ms)` | 每个 test suite 的总执行时间；**多 site 时显示所有器件的平均** |
| `Exec Num` | 每个 test suite 的执行次数——**优化与非优化 testflow 下含义不同** |

`Exec Num` 的两义原文说得很清楚：

> 「For non-optimized testflows, this number is the number of testsuite repetitions multiplied by the number of sites.」

> 「For optimized testflows, this number is the number of testsuite repetitions as multiple sites are tested in parallel.」

**图证 ④**：`111670.png`（alt 逐字 `Result columns on the Testsuites page`，
在 raw 里挂在 `Exec Num` 那一行的末尾）
把这一块的组名 `Result` 与四个列名逐字摆出来：**`#1 Pass/Fail`** / **`#2 Pass/Fail`** /
**`Exec Time (ms)`** / **`Exec Num`**，而 **`Test Suite Comment`** 是这一屏最右边那一列。
**`#1 Pass/Fail` / `#2 Pass/Fail` / `Test Suite Comment` 三个串在全部 9,398 篇 raw 里 0 命中**
——正文那张表只写了一个 `Pass/Fail`，**没有写这两个带 site 号的形式**。

### Test suite flags columns：一条容易踩的操作前提

> 「These columns display the test suite flags which control the output of the test suite.」

**紧接着的那条 `Note` 是本页最值得记的一句**（原文行首有一个空格）：

> 「Note You can also access the test suite flags through the Operation Control window (via Production Settings), when running SmarTest in engineering mode. To actually make changes to the flags, all windows must there be set to Testflow settings mode (not to Production settings mode) from the Operation Control window.」

**读法：engineering 模式下 flag 能从 Operation Control 窗口（走 Production Settings）够到；
但要真改，所有窗口都得是 `Testflow settings mode`，不能停在 `Production settings mode`。**
**「改不动」的第一嫌疑人就是这一条。**

**这张图不算 ④**（实测 11 个列名在 raw 里**全部搜得到**：`Test Suite Name` 10 篇、`Test Level` 4 篇、
`Bypass` 42 篇、`Set pass` 5 篇、`Set fail` 6 篇、`Hold` 75 篇、`Hold on fail` 3 篇、
`Output on pass` 13 篇、`Output on fail` 14 篇、`Pass value` 15 篇、`Fail value` 15 篇，
**没有一个是 0 命中**；`02.08.04.32.02.01.16` 的 CSV 导出例里，`Test Level` → `Fail value` 这**十个**
还按同一顺序连着排（那一篇的首列写作 `Testsuite Name`，不是 `Test Suite Name`））。
那 11 个名字**在本篇正文里确实没有**，**但「本篇没有」不等于「raw 里搜不到」**——所以不占 ④ 档。
`110690.png`（alt 逐字 `Testsuite flag columns on the Testsuites page`）
把这一组的 **11 个列名**逐字摆出来——
`Test Suite Name` / **`Test Level`** / **`Bypass`** / **`Set pass`** / **`Set fail`** / **`Hold`** /
**`Hold on fail`** / **`Output on pass`** / **`Output on fail`** / **`Pass value`** / **`Fail value`**。
**正文一个字都没列这些列名**，只说「display the test suite flags」——**但列名本身在语料别处是有的**。

### Test suite Comment column

> 「You can add comments for each test suite.」

（**图证 ④** 见上：`111670.png` 最右一列的列名逐字就是 `Test Suite Comment`。）

### Annotation：四根条、六类元素

> 「For the following six kinds of elements, annotations are displayed on the Test Suites page:」

原文列了这些元素（**原文的层次是列表，本页照它的层次排，没有合并行**）：

- Bookmarked test suite
- Executed test suite
  - Failed
  - Passed
- Failed test suite
- Invalid parameter
- Linked test suites
- Passed test suite

**六个「类」是：Bookmarked / Executed / Failed / Passed / Invalid parameter / Linked test suites。**
（`Executed` 下面的 `Failed` / `Passed` 是它的两个子状态。）

**两条交互一句到位**：

> 「Clicking on the annotation locates the relevant element. Hovering the mouse over an annotation displays the relevant information in a tooltip.」

> 「You can change the way the annotation is displayed in the Table Annotations preference page.」

**四根条**：

> 「The annotations are organized in four annotation bars:」

> 「In the local annotation bars, the annotations are aligned with the visible columns and rows. The overview rulers provide overviews for all columns or rows of the table.」

四根条的名字是 **`Top local annotation bar`** / **`Left local annotation bar`** /
**`Right overview ruler`** / **`Bottom overview ruler`**：
**前两根是 local（对齐可见的行列），后两根是 ruler（给全表做概览）。**

原文还给了「怎么找最后一个跑过的 test suite」这个例子：

> 「The annotations help you easily navigate the relevant test element. For example, to locate the last executed test suite, click the last annotation in the right overview ruler, if you have set the Table Annotations preference page to show the table annotations_ of Executed type in the Overview Rulers.」

（`annotations_` 后面那个下划线是原文自带的，见「出处」⚠️ ②。）

**图证 ④**：`111693.png`（alt 逐字 `Annotation bars in the Test Suites page`）是**四根条的标注图**——
图上四个标注框逐字是 `Top local annotation bar` / `Left local annotation bar` /
`Right overview ruler` / `Bottom overview ruler`，**每个框指在哪条边上可以一眼看出**
（正文只列这四个名字，方位是名字自己带的；图把「名字对哪条边」坐实了）。
图上另有正文没有的东西：标签页名 **`tf_advance`**、五行 test suite 名
**`Inp_Volt_Sens`** / **`Input_Leakage`** / **`OutputDC`** / **`Prop_Delay`** / **`continuity`**，
以及一个**悬停出来的 tooltip**，逐字是 **`Invalid Timing Set`** 加一行 `- Prop_Delay`。
**`tf_advance` / `Inp_Volt_Sens` / `Prop_Delay` / `Invalid Timing Set` 四个串在全部 raw 里 0 命中。**
**这张图的价值在于它把正文那句「hover 会出 tooltip」变成了「tooltip 长这样」**——
而且那一行 `Prop_Delay` 的 `Eqn` 格是**黄底**，正对上 `Validate setups` 那句的 `the equation or set number in yellow`。

**Next / Previous Annotation 按钮**：

> 「By clicking the Next Annotation button or Previous Annotation button on the main toolbar, you can navigate the test suites on the Test Suites page. If you want to specify the search scope, click the arrow next to the button and select the types of test suites you are interested in from the pop-up list.」

**这张图不算 ④**（`Invalid` / `Failed` / `Passed` / `Executed` **四个词单个都搜得到**）：
`111912.png` 把这两个按钮圈了红圈，并**展开**了那个下拉——下拉里是**四个带复选框的项**：
**`Invalid`** / **`Failed`** / **`Passed`** / **`Executed`**（`Passed` 被勾上）。
**这一条与正文对不上**：正文的注解种类是**六类**（多了 `Bookmarked` 与 `Linked`），
下拉里只有**四项**。**本页照实并列，不替语料选一个**（见「出处」⚠️ ①）。

### Show and Hide 按钮，加一个 `Validate setups`

> 「When you activate the Test Suites page on the Flow Data Editor, the following buttons appear on the main icon bar of the SmarTest Work Center.」

> 「These buttons control only the visible columns. You can choose which columns are visible in the Test Suites preference page.」

| 按钮 | 作用 |
|---|---|
| Show / hide **test setup** columns | 开关 Test Setup 那组列 |
| Show / hide **primary setup** columns | 开关 Primary Settings 那组列 |
| Show / hide **result** columns | 开关 Result 那组列 |
| Show / hide **test suite flag** columns | 开关 flag 那组列 |
| **Show all columns** | 一次全开 |
| **Validate setups** | **检查器（不是显示开关，见下）** |

**`Validate setups` 不是显示开关，是检查器**——原文那段单独说它：

> 「Clicking this button highlights any invalid testflow setup (where setup files have not been loaded or the selected setting does not exist in the setup files) the equation or set number in yellow and displays the annotation. You can hover over the annotation to see the detailed information.」

**两个「坏」的判据是原文给的**：**setup 文件没加载**，或**选的那个设置在 setup 文件里不存在**。
表现是 **equation 或 set 号变黄** + **出一根 annotation**。

**图证 ④**：`113770.png`（alt 逐字 `Buttons controlling which columns are displayed in the Flow Data Editor`）
把这一排按钮**圈了红圈**，
**圈住的是第二排工具栏最右端的六个按钮**。**正文只说「on the main icon bar」，没有说在哪一段**
——「在第二排最右端」这一条只在图上。
（这张图上另外几个字——`File`/`Edit`/`Navigate`/`Search`/`Project`/`Run`/`93000`/`Window`/`Help`
与窗口标题里的 `/home/demo/workspace`——**都能在 raw 里搜到**，
所以**这一张按 §11.4 的判据只有「红圈的位置」是图证，其余不算**。）

### 一致性检查：两个按钮、两套适配流程

> 「When you open any page of the Flow Data Editor, the following buttons appear on the main icon bar on the left of the Show and Hide buttons (see above).」

两个按钮是 `Check Inconsistency` 与 `Check All Inconsistencies`，而**检查本身是自动跑的**：

> 「SmarTest automatically checks the consistency of the test suites with the current testflow.」

**不一致时给两个信号**：

> 「If a test suite is inconsistent, SmarTest:」

> 「Shows the test setup entries on the test suite page with a yellow background (SmarTest default configuration)」

> 「Grays out the test suite's properties on the property view」

**两个信号要分清**：**表格里黄底 = 这一行不一致**；**properties view 变灰 = 那里改不动**。

> 「Using the buttons, you can adapt a single inconsistent or multiple inconsistent test suites to your testflow.」

| 情形 | 步骤 | 结果 |
|---|---|---|
| **单个** | ①选中那个 test suite ②点 `Check Inconsistency` | 背景变回默认色（白）；properties view 可以编辑 |
| **一个或多个** | ①点 `Check All Inconsistencies` ②选择窗口打开，**默认全选** ③**清掉你不想适配的** ④点 `OK` | 同上 |

选择窗口里装的是什么，原文一句：

> 「The selection window opens showing all inconsistent test methods that can be adapted.」

> 「By default all inconsistent test suites are preselected.」

**图证 ④**：`125588.png`（alt `Check Inconsistency of single test suite`）把**两个红箭头**画在图上，
分别标 `Select a test suite`（指向第 1 行）与 `Click Check Inconsistency`（指向工具栏上那两个蓝勾）
——**正文只说「在 Show and Hide 按钮左边的图标栏上」，图把「哪两个图标」钉死了**。
`125583.png`（就是原文 `The selection window opens...` 后面那张图）给出那个选择窗口的**实际字面**：
标题两行是 **`Adapt testflow to parameter changes in test method library.`** 与
**`Please select test suite(s) of which parameter changes will be all adapted.`**，
下面是一棵带复选框的测试方法树（`ac_tml.AcTest.FunctionalTest` / `tmu_tml.TmuTest.RiseFallTime` /
`tmu_tml.TmuTest.Frequency` …），底部 `OK` / `Cancel`。
**那两行标题在全部 raw 里 0 命中**——正文只有 `The selection window opens showing all inconsistent
test methods that can be adapted.` 这一句，**窗口自己怎么措辞在文本里查不到**。
（alt 与图里的字不一致，见「出处」⚠️ ③。）

## 典型用法

**本文档没有 `## Procedure` 段、没有 `## Before you begin`**——但页上的动作都是**按钮级**的，
所以这一节按「你要干什么 → 点哪里」来排。

**1. 加 / 删 test suite。** 这张表上能加能删的是 **special** 与 **floating** 两种，
普通的 `"Run"` / `"Run and Branch"` 由 Flow Sequence Editor 编排（**本页没读那一篇**）。

**2. 批量改设置。** 两条路：同一种改法要套多个格 → **复制一格、粘到多格**；
改动有多处且要细看 → **复制一片区域到文本编辑器、改完粘回来**。

**3. 跑完看结果。** 看 **边框颜色**：**宽 = 真结果，窄 = 人手置的**；
`Pass/Fail` / `Exec Time (ms)` / `Exec Num` 三列看数值。
**跑完又改了 testflow → 边框全变虚线，说明这一屏的结果已经过期。**

**4. 多 site 怎么看。** 全部 site 一起看 → 一荣俱荣、一损俱损；
只看 focus site → 只按 focus site 上色。

**5. 设置「没生效」的排查顺序**（本页语料给的两个入口）：
先看 **flag 列**那一节那条 `Note`（所有窗口必须处在 `Testflow settings mode`）；
再看 `Validate setups` 按钮——**黄字的就是 setup 文件没加载或设置不存在的那一处**。

**6. 换了测试方法库之后行变黄了。** 这是**一致性检查**：
①单个改 → 选中 + `Check Inconsistency`；
②批量改 → `Check All Inconsistencies` → 在窗口里清掉不想改的 → `OK`。
**改完的判据是两条：背景回到白色、properties view 能编辑。**

**7. 表太长找不到出问题的行。** 用 `Next Annotation` / `Previous Annotation` 跳；
要缩小范围就点旁边那个箭头，在弹出列表里勾类型。

**8. 列太多 / 太少。** 用那六个显示开关按钮；**改了忘了，去 Test Suites preference page 看**
（**那一篇本页没读**）。

## 和谁有关

- [[testflow]] —— 本页 `stage: testflow`。
- [[flow-data-editor]] —— **直接宿主**：原文两处说「activate the Test Suites page on the Flow Data Editor」
  / 「open any page of the Flow Data Editor」——**本页是它的一个 page，不是一个独立窗口**。
- [[flow-sequence-editor]] —— **同级的另一个编辑面**（流程顺序那一半）。
  本页的语料**没有提它**；这条关系是**按 testflow 章的结构排的（推断）**，
  依据是原文反复出现的「Flow Data Editor 的某一个 page」这个说法。
- [[testflow-tool]] —— **上层窗口**。**本文档没有提它**：本页语料自己只说到 `property view`
  （原文那句 `Grays out the test suite's properties on the property view`，**没说那是哪个窗口的**）。
  这条关系是**按 testflow 章的结构排的（推断）**。
- [[test-suite]] —— **一行就是一个 test suite**；`Test Suite Name` 是这一页的第一列。
- [[special-test-suites]] —— **本页能加能删的那一类**：原文 `special test suites` 是链接到它那一篇的。
  **那一篇本页没读**，所以「七/八种」那些细节不在本页。
- [[testflow-properties-view]] —— **一致性检查的第二个信号落点**：原文 `Grays out the test suite's
  properties on the property view`。**`property view` 是否就是它，原文没说**——**本页不判**。
- [[alphabetical-list-of-flags]] —— **flag 列的语言表**：这一页的 flag 列显示的是 flag 名，
  取值与关键字的对照在那一篇（**那一篇本页没读**）。
- [[test-suite-control-api]] —— **同一批 flag 的 L3 读写口**。
  **本文档一个字都没提 API**（通篇 0 命中），这条关系是**按 wiki 结构排的（推断）**。
- [[site-control-window]] —— 原文 `## Related information` 里那一条叫
  `Expanded Site Control window`（**「Expanded」这一篇未建**）。
  **它与本页已有的 [[site-control-window]] 是不是同一件事，本页不判。**
- `Test Suites preference page`、`Table Annotations preference page`（**均未建**）——
  两处「你可以去那里改」的落点：**列可见性**与**注解显示方式**。**两篇本页都没读。**
- `Editing a test suite in the Flow Data Editor`、`Test suite flags`（**均未建**）——
  原文 `## Related information` 的另两条。**都没读。**

## 版本

本文档有 `## Functional changes` 段，六条：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.2: Test suite names can be changed.`
- `SmarTest 6.5.2: Test suite Comment column is added.`
- `SmarTest 6.5.2: Show all columns button is added.`
- `SmarTest 6.5.4: Adapt test suite(s) buttons added`
- `SmarTest 7.0.1: Cloned test suite renamed to linked test suite`

**第一条是哨兵值，不是「6.3.2 的变更」**（§11.2②）：`before` 的意思是
「在本文档集覆盖范围开始之前就已经有了」。

**三条和正文对得上的，本页逐条给出对应（前两条是文档事实、第三条是推断）：**

| 版本条目 | 正文里的对应物 |
|---|---|
| `Test suite Comment column is added`（6.5.2） | 就是那一节 `## Test suite Comment column`（**本篇正文自己写着**） |
| `Show all columns button is added`（6.5.2） | 就是按钮表里那一行 `Show all columns`（**本篇正文自己列着**） |
| `Cloned test suite renamed to linked test suite`（7.0.1） | 注解元素表里的 **`Linked test suites`**——**（推断）**：这是本页语料里唯一带 `Linked` 的东西，**但原文没有一句话把两者连起来**，所以标推断 |

**另有一条推断，本页标出来但不当结论用**：`Adapt test suite(s) buttons added`（6.5.4）
与 `Check Inconsistency` / `Check All Inconsistencies` 那两个按钮措辞对得上，
**但 6.5.4 的条目写的是 `Adapt test suite(s)`，正文里那两个按钮叫 `Check ...`**——
**名字不一样，所以本页只说「措辞相近」，不认作同一条。**

## 出处

`sources:` 一篇，**整篇读完**：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.01_Test_Suites_page.md`
（TDC `99272.htm`，**全文 10,253 字节**）。**没有读 `sources` 之外的任何文档。**

**看了 21 张图，全看了。** 本篇对 `raw/` 下 `.png` 的引用共 **23 处 / 21 张互不重复**
（被引了两次的是 `125585.png` 与 `125534.png` **两张一致性检查按钮图**——
它们各在「图标 + 名字」那一行出现一次、又在「Adapt a single / one or more」的步骤里出现一次；
**那四对显示/隐藏按钮图（`110946`–`110953`）八张各被引了一次**）。

**逐张按 §11.4 的判据分档**（判据是「**图里的字在 raw 里 grep 得到吗**」；
本页的 grep 是全语料 9,398 篇 `.md` 实测）：

| 图 | 读到了什么 | 图里的字 grep 得到吗 |
|---|---|---|
| `111670.png` | `Result` 组 + `#1 Pass/Fail` / `#2 Pass/Fail` / `Exec Time (ms)` / `Exec Num` / `Test Suite Comment` | **`#1 Pass/Fail`、`#2 Pass/Fail`、`Test Suite Comment` 三串 0 命中** ——**是严格的 ④** |
| `111693.png` | 四根条的四个框名 + 标签页 `tf_advance` + 五行 test suite 名 + tooltip `Invalid Timing Set` | **`tf_advance` / `Inp_Volt_Sens` / `Prop_Delay` / `Invalid Timing Set` 四串 0 命中**——**是严格的 ④** |
| `125583.png` | 选择窗口的标题两行 | **那两行 0 命中**——**是严格的 ④** |
| `125597.png` | `Test Setup` 组名 + `Ty...` + `Name` + 灰掉的 properties 面板 | `Debug-testflow` **0 命中**；`Name` / `Type` / 面板上的标签是常用词——**部分 ④** |
| `125588.png` | 两个红箭头标注 | `Click Check Inconsistency` **0 命中**；`Select a test suite` 另有 1 篇——**部分 ④** |
| `110689.png` | `Timing` 组头 + 三个子列名 `Eqn` / `Desc` / `Spec/Waveform Set` | 三个列名**都搜得到**（`Spec/Waveform Set` 在 1 篇里，**那一篇不是本篇**）——**所以它「补了正文没列的名字」，但不是严格 ④** |
| `110690.png` | flag 组的 11 个列名 | **11 个名字全部搜得到**（在 `Test_suite_flags` 等篇里）——**同样不是严格 ④** |
| `111912.png` | 搜索范围下拉的四项 | **四个词单个都搜得到**——**不是 ④**，是「图与正文的对照」（见「出处」⚠️ ①） |
| `113770.png` | 红圈圈住第二排工具栏最右端的六个按钮 | **图上没有搜不到的字**（菜单名与窗口标题都搜得到）——**这一张的 ④ 成分是「红圈的位置」，不是字** |
| `110946`–`110953` 八张 | 显示 / 隐藏按钮的图标本身 | **图上没有可读的字**——**没有文字结论** |
| `110688.png` | `Show all columns` 的图标 | 同上 |
| `125585.png` / `125534.png` | 单个 / 双个蓝勾（那两个一致性按钮的图标） | 同上 |
| `111383.png` | `Validate setups` 的图标（很小、很模糊） | 同上 |

**本页没做的：**

- **`## Related information` 的三条一篇没读**（`Editing a test suite in the Flow Data Editor`、
  `Test suite flags`、`Expanded Site Control window`）。
- **正文链出去的几篇也没读**：`"Run" and "Run and Branch" test suites`、`Special test suites`、
  `Floating test suite`、`Table Annotations preference page`、`Test Suites preference page`、
  `Cloning nodes`（`Linked test suites` 那个锚点的宿主）。
  **所以本页没有：这三种 test suite 各自的细节、两张 preference page 里到底能设什么。**
- **没有实跑。** 没有开过 Flow Data Editor、没有点过那两个一致性按钮、没有 hover 过 annotation。
  `verified: doc-only` 指的就是这件事。
- **写这页时没有动 `wiki/index.md`、也没有把本页挂进 `wiki/stages/testflow.md`**；**`index.md` 已由本批收尾挂入**。（**2026-09-20 更正**：原文写「那是待办」——**收尾动作把它变成了假话**。stage 页那侧**仍未挂**，那才是真待办。）

**⚠️ 本页照实记下、一处都没替语料改的瑕疵：**

**① 注解种类：正文六类，图里的下拉四项。** 正文写 `For the following six kinds of elements`，
列了 **Bookmarked / Executed / Failed / Passed / Invalid parameter / Linked test suites** 六类；
而 `111912.png` 里那个搜索范围下拉只有 **`Invalid` / `Failed` / `Passed` / `Executed`** 四项
（没有 `Bookmarked`，也没有 `Linked`）。**两处本页并列，不替语料选一个。**

**② 一处多余的下划线。** 正文写 `to show the table annotations_ of Executed type`——
`annotations` 后面多一个 `_`。**引文里照原样留着。**

**③ 图与 alt 对不上两处，照实记。**
`125583.png` 的 alt 是 `Adjust testflow to parameter changes in test method library`，
而**图上的字是 `Adapt testflow to parameter changes in test method library`**（`Adjust` / `Adapt` 一字之差）；
同图的第二行 `Please select test suite(s) of which parameter changes will be all adapted.`
**语法也是原文如此**（`will be all adapted`）。
另一处：`125588.png` 的 alt 是 `Check Inconsistency of single test suite`，图上的标注框写的是
`Click Check Inconsistency` 与 `Select a test suite`——**三处措辞三种。**

**④ 按钮表的 alt 串与说明不一致，另有三个无意义的 alt。**
原文那一对一对的按钮图，alt 是
`1t` / `Hide primary setup columns` / `Primary setup columns` / `2p`（`2p` 出现两次）。
其中 **`1t` 与 `2p` 是无意义串**；**`Hide primary setup columns` 落在说明为
`Show or hide the test setup columns` 的那一行上**（说的是 primary，描述说的是 test）。
**本页一处都没替它改。**

**⑤ 一句语序坏掉的句子。** 正文写 `all windows must there be set to Testflow settings mode`——`there` 的位置不对（正常语序应是 `must be set to`）。**这句本页在上面那个 `Note` 的引文里逐字留着。**

**⑥ 另一句语法不完整的句子。** `Validate setups` 那段里，括号插在 `highlights any invalid testflow setup` 与 `the equation or set number in yellow` 之间，**两个成分直接相撞、中间缺一个动词**。**本页在正文里照原样引了那一整句，没有替它补词。**

**⑦ 两节的指代词撞车。** `## Test Setup columns` 一节写 `In these columns, you can define the test executed by this test suite.`，紧接着的 `## Primary Settings columns` 一节又写 `These columns include the timing, level, analog setup, and pattern settings.`——**两个 `these columns` 指的不是同一组列**（前者是 Test Setup，后者是 Primary Settings）。**这是原文的写法，本页没有替它改指代。**

**⑧ 编码坏字：零处。** 实测这一篇的 CJK 字符数是 **0**（§11.2① 那一族在这篇里一处都没有）；
**`DC/DC power units` 那一族（§11.2⑤）也是 0 处**（本篇没有代码块，也没有 C++ 标识符）。

`verified: doc-only`
