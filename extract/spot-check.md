# 分层抽样核对表

共 **40** 篇（抽样位 53 个，去重后）。左列原文，右列抽取结果，逐条对齐。

> 自动对账查不出「解析对了但语义错了」。**这一份要人真的看一遍。**

## 看的时候按这几条规则对

**边的 `语境` 抽取规则**（写死在计划里，不许临场发挥，核对的就是它）：

1. 取链接所在那一行
2. 剥掉行首列表符（`-` `*` `1.`）与 markdown 强调符，**但链接目标 `](<...>)` 原样保留**
3. 若结果 < 20 字符，向上并入前一行（最多并 3 行）
4. 截断到 300 字符

`语境` 显示的是**完整存值**（≤300 字符）。`to_raw` 一字不改地出现在语境里，就是对的。

**标题**：`L{n}` 是 1 起的行号，回到左边原文数到第 n 行应当正是那个标题。

**段落**：`L{n}` 是**段落标题所在行**，正文从 n+1 行开始；`chars` 是截断前的长度（上限 6000）。

**故意不建边的东西**：图片（`.png` 等）、页内锚点、外部 URL、`javascript:`、以及 `[](<>)` 空链接。看到它们没出现在边里，是对的。

---

## `00_Overview/00_SmarTest_7.10.3_Documentation.md`

*抽样理由：00_Overview 首篇；无任何结构段落；解析异常 no_h1*

- 字节 1325 / 标题 1 / 出度 8 / 代码块 0
- frontmatter：`{"source_html": "00_Overview/00_SmarTest_7.10.3_Documentation.htm", "source_topic": "9561.htm", "title": "SmarTest 7.10.3 Documentation"}`
- title：`None`
- 结构段落：（无）
- ⚠️ 解析异常：[{'detail': '', 'doc': '00_Overview/00_SmarTest_7.10.3_Documentation.md', 'kind': 'no_h1'}]

### 原文开头

```
---
title: "SmarTest 7.10.3 Documentation"
source_topic: "9561.htm"
source_html: "00_Overview/00_SmarTest_7.10.3_Documentation.htm"
---
[

## Getting started

](<../01_Getting_started/01_Getting_started.md>)

[SmarTest Work Center](<../01_Getting_started/01.01_SmarTest_Work_Center/01.01_SmarTest_Work_Center.md>)

[SmarTest workstation administration](<../01_Getting_started/01.02_SmarTest_workstation_administration/01.02_SmarTest_workstation_administration.md>)

[Using SmarTest](<../01_Getting_started/01.03_Using_SmarTest/01.03_Using_SmarTest.md>)

[SmarTest system parameters - default values and limits](<../01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md>)

[SmarTest character and number limits](<../01_Getting_started/01.05_SmarTest_character_and_number_limits/01.05_SmarTest_character_and_number_limits.md>)

[Test methods](<../01_Getting_started/01.06_Test_methods/01.06_Test_methods.md>)

[Testing a Basic Digital Device](<../01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07_Testing_a_Basic_Digital_Device.md>)

[Migrating test programs to SmarTest 7.10](<../01_Getting_started/01.08_Migrating_test_programs_to_SmarTest_7.10/01.08_Migrating_test_programs_to_SmarTest_7.10.md>)

```

### 抽取的标题

- L8 `## Getting started`

### 抽取的边（8 条，显示前 10）

- L12 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01_SmarTest_Work_Center.md`
  - 语境：[SmarTest Work Center](<../01_Getting_started/01.01_SmarTest_Work_Center/01.01_SmarTest_Work_Center.md>)
- L14 → `01_Getting_started/01.02_SmarTest_workstation_administration/01.02_SmarTest_workstation_administration.md`
  - 语境：[SmarTest workstation administration](<../01_Getting_started/01.02_SmarTest_workstation_administration/01.02_SmarTest_workstation_administration.md>)
- L16 → `01_Getting_started/01.03_Using_SmarTest/01.03_Using_SmarTest.md`
  - 语境：[Using SmarTest](<../01_Getting_started/01.03_Using_SmarTest/01.03_Using_SmarTest.md>)
- L18 → `01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md`
  - 语境：[SmarTest system parameters - default values and limits](<../01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md>)
- L20 → `01_Getting_started/01.05_SmarTest_character_and_number_limits/01.05_SmarTest_character_and_number_limits.md`
  - 语境：[SmarTest character and number limits](<../01_Getting_started/01.05_SmarTest_character_and_number_limits/01.05_SmarTest_character_and_number_limits.md>)
- L22 → `01_Getting_started/01.06_Test_methods/01.06_Test_methods.md`
  - 语境：[Test methods](<../01_Getting_started/01.06_Test_methods/01.06_Test_methods.md>)
- L24 → `01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07_Testing_a_Basic_Digital_Device.md`
  - 语境：[Testing a Basic Digital Device](<../01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07_Testing_a_Basic_Digital_Device.md>)
- L26 → `01_Getting_started/01.08_Migrating_test_programs_to_SmarTest_7.10/01.08_Migrating_test_programs_to_SmarTest_7.10.md`
  - 语境：[Migrating test programs to SmarTest 7.10](<../01_Getting_started/01.08_Migrating_test_programs_to_SmarTest_7.10/01.08_Migrating_test_programs_to_SmarTest_7.10.md>)

---

## `00_Overview/index.md`

*抽样理由：00_Overview 中位；00_Overview 末篇；体积最小 105B；无任何结构段落；解析异常 no_frontmatter*

- 字节 105 / 标题 1 / 出度 1 / 代码块 0
- frontmatter：`null`
- title：`00_Overview`
- 结构段落：（无）
- ⚠️ 解析异常：[{'detail': '文件首行不是 ---', 'doc': '00_Overview/index.md', 'kind': 'no_frontmatter'}, {'detail': '', 'doc': '00_Overview/index.md', 'kind': 'not_in_catalog'}]

### 原文开头

```
# 00_Overview

- [SmarTest 7.10.3 Documentation](00_SmarTest_7.10.3_Documentation.md)
  - `9561.htm`

```

### 抽取的标题

- L1 `# 00_Overview`

### 抽取的边（1 条，显示前 10）

- L3 → `00_Overview/00_SmarTest_7.10.3_Documentation.md`
  - 语境：[SmarTest 7.10.3 Documentation](00_SmarTest_7.10.3_Documentation.md)

---

## `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.01_Starting_SmarTest_with_supervisor_mode.md`

*抽样理由：01_Getting_started 首篇；出度 0*

- 字节 1093 / 标题 1 / 出度 0 / 代码块 0
- frontmatter：`{"source_html": "01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.01_Starting_SmarTest_with_supervisor_mode.htm", "source_topic": "43518.htm", "title": "Starting SmarTest with supervisor mode"}`
- title：`Starting SmarTest with supervisor mode`
- 结构段落：（无）

### 原文开头

```
---
title: "Starting SmarTest with supervisor mode"
source_topic: "43518.htm"
source_html: "01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.01_Starting_SmarTest_with_supervisor_mode.htm"
---
# Starting SmarTest with supervisor mode

With supervisor status you have the possibility of both creating and allocating workorders, and executing them. Moreover you can run calibration and diagnostics tools using the Supervising Pop-up window (see the figure below). But you have no access to the test program development functions of SmarTest.

To start SmarTest with supervisor mode open a terminal and type:

HPSmarTest -S or,

HPSmarTest -So if you are running the software offline (that is, the tester is not connected).

The screen shown below appears.

  ![Operation Control Window with Supervisor Status](<../../../../raw/349459.png>)

In order to change the user mode of SmarTest, click the button supervising in the Operation control window (figure above), and chose the new desired mode.

In order to exit SmarTest, click Quit in the Operation control window.

```

### 抽取的标题

- L6 `# Starting SmarTest with supervisor mode`

### 抽取的边（0 条，显示前 10）


---

## `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.02_Starting_SmarTest_with_operator_mode.md`

*抽样理由：补齐（全库等距，非随机）*

- 字节 1335 / 标题 2 / 出度 2 / 代码块 0
- frontmatter：`{"source_html": "01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.02_Starting_SmarTest_with_operator_mode.htm", "source_topic": "43520.htm", "title": "Starting SmarTest with operator mode"}`
- title：`Starting SmarTest with operator mode`
- 结构段落：['Related information']

### 原文开头

```
---
title: "Starting SmarTest with operator mode"
source_topic: "43520.htm"
source_html: "01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.02_Starting_SmarTest_with_operator_mode.htm"
---
# Starting SmarTest with operator mode

With operator status you focus on the execution of workorders, which have previously been set up. But you have no access to the test program development functions of SmarTest.

To start SmarTest with operator mode open a terminal and type:

HPSmarTest -O or,

HPSmarTest -Oo if you are running the software offline (that is, the tester is not connected).

The screens shown below appear.

  ![Operation Control (Operator Status) and Workorder Select Screens](<../../../../raw/349461.png>)

In order to change the user mode of SmarTest, click the button operating in the Operation control window (figure above), and chose the new desired mode.

In order to exit SmarTest completely, click Quit in the Workorder select window.

## Related information

[Setting up Workorder Directories](<../01.02_SmarTest_workstation_administration/01.02.02.02.03_Setting_up_Workorder_Directories.md>)[Executing a workorder from the operation control panel](<../../02_System_reference/02.09_Test_Program_Management/02.09.01.05.05.01_Executing_a_workorder_from_the_operation_control_panel.md>)

```

### 抽取的标题

- L6 `# Starting SmarTest with operator mode`
- L24 `## Related information`

### 抽取的边（2 条，显示前 10）

- L26 → `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.02.03_Setting_up_Workorder_Directories.md`
  - 语境：[Setting up Workorder Directories](<../01.02_SmarTest_workstation_administration/01.02.02.02.03_Setting_up_Workorder_Directories.md>)[Executing a workorder from the operation control panel](<../../02_System_reference/02.09_Test_Program_Management/02.09.01.05.05.01_Executing_a_workorder_from_the_oper
- L26 → `02_System_reference/02.09_Test_Program_Management/02.09.01.05.05.01_Executing_a_workorder_from_the_operation_control_panel.md`
  - 语境：[Setting up Workorder Directories](<../01.02_SmarTest_workstation_administration/01.02.02.02.03_Setting_up_Workorder_Directories.md>)[Executing a workorder from the operation control panel](<../../02_System_reference/02.09_Test_Program_Management/02.09.01.05.05.01_Executing_a_workorder_from_the_oper

### 抽取的段落

- `Related information`（related，L24，324 字符）
  - 开头：'[Setting up Workorder Directories](<../01.02_SmarTest_workstation_administration/01.02.02.02.03_Setting_up_Workorder_Dir'

---

## `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.04_Changing_the_User_Mode.md`

*抽样理由：含 Functional changes*

- 字节 2246 / 标题 3 / 出度 3 / 代码块 0
- frontmatter：`{"source_html": "01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.04_Changing_the_User_Mode.htm", "source_topic": "43524.htm", "title": "Changing the User Mode"}`
- title：`Changing the User Mode`
- 结构段落：['Functional changes', 'Subtopics']

### 原文开头

```
---
title: "Changing the User Mode"
source_topic: "43524.htm"
source_html: "01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.04_Changing_the_User_Mode.htm"
---
# Changing the User Mode

#### Subtopics

- [Changing the SmarTest Mode Passwords](<01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md>)

The top button in each of the Operation Control screens indicates your current user mode. Clicking this button reveals a new shortcut menu that allows you to change the user mode (provided you know the password, if relevant).

 Note Changing the user mode will extend or reduce your possibilities within the SmarTest environment. But, this will not affect the file permissions, that you have acquired when logging on to the system. This means, your individual rights to read/write certain files remain unchanged.

To change the user mode, proceed as follows:

- In the Operation Control Window, click the user mode button.
- The screen shown below appears. ![The User Mode Pop-up Window](<../../../../raw/46352.png>)
- Click the appropriate user-mode keyword or associated diamond. Note Before you use the operate console mode you have to install the operator console. For detailed information, see [The Operator Console for Controlling Workorders](<../../02_System_reference/02.09_Test_Program_Management/02.09.01.05.06_The_Operator_Console_for_Controlling_Workorders.md>).

If a password is required, an entry-box appears prompting you for the correct password. See [Changing the SmarTest Mode Passwords](<01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md>) for details on setting and changing user mode passwords.

- Key in the password-if required-and press return.

You are only prompted for a password when you are going to a higher user level; for example operator to supervisor, or supervisor to engineer. Changing from Operator Console to Operator status requires no password.

The Operation Control Window appears in its new mode providing the appropriate options.
```

### 抽取的标题

- L6 `# Changing the User Mode`
- L8 `#### Subtopics`
- L32 `## Functional changes`

### 抽取的边（3 条，显示前 10）

- L10 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md`
  - 语境：[Changing the SmarTest Mode Passwords](<01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md>)
- L20 → `02_System_reference/02.09_Test_Program_Management/02.09.01.05.06_The_Operator_Console_for_Controlling_Workorders.md`
  - 语境：Click the appropriate user-mode keyword or associated diamond. Note Before you use the operate console mode you have to install the operator console. For detailed information, see [The Operator Console for Controlling Workorders](<../../02_System_reference/02.09_Test_Program_Management/02.09.01.05.0
- L22 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md`
  - 语境：If a password is required, an entry-box appears prompting you for the correct password. See [Changing the SmarTest Mode Passwords](<01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md>) for details on setting and changing user mode passwords.

### 抽取的段落

- `Subtopics`（related，L8，1893 字符）
  - 开头：'- [Changing the SmarTest Mode Passwords](<01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md>)\n\nThe top button in ea'
- `Functional changes`（version，L32，84 字符）
  - 开头：'- Introduced before SmarTest 6.3.2\n- SmarTest 6.5.3: Introduced new operator console'

---

## `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01_Starting_SmarTest.md`

*抽样理由：含 Functional changes；含 Before you begin*

- 字节 9537 / 标题 8 / 出度 20 / 代码块 0
- frontmatter：`{"source_html": "01_Getting_started/01.01_SmarTest_Work_Center/01.01.01_Starting_SmarTest.htm", "source_topic": "107991.htm", "title": "Starting SmarTest"}`
- title：`Starting SmarTest`
- 结构段落：['About this task', 'Before you begin', 'Functional changes', 'Related information', 'Subtopics']

### 原文开头

```
---
title: "Starting SmarTest"
source_topic: "107991.htm"
source_html: "01_Getting_started/01.01_SmarTest_Work_Center/01.01.01_Starting_SmarTest.htm"
---
# Starting SmarTest

#### Subtopics

- [Starting SmarTest with supervisor mode](<01.01.01.01_Starting_SmarTest_with_supervisor_mode.md>)
- [Starting SmarTest with operator mode](<01.01.01.02_Starting_SmarTest_with_operator_mode.md>)
- [Starting SmarTest with engineer mode](<01.01.01.03_Starting_SmarTest_with_engineer_mode.md>)
- [Changing the User Mode](<01.01.01.04_Changing_the_User_Mode.md>)

## About this task

 Note This topic is applicable to SmarTest 7 only. This topic covers both how to start SmarTest from the command line in a terminal window, and from the task bar of the Linux system:

- [Starting SmarTest from the task bar](<01.01.01_Starting_SmarTest.md#_107991__task_bar>)
- [Starting SmarTest from the terminal](<01.01.01_Starting_SmarTest.md#_107991__terminal>)

You can start the software in several ways, depending on what status you want to have. For details on each of these modes, refer to [ Starting SmarTest with supervisor mode](<01.01.01.01_Starting_SmarTest_with_supervisor_mode.md>), [ Starting SmarTest with operator mode](<01.01.01.02_Starting_SmarTest_with_operator_mode.md>) and [Starting SmarTest with engineer mode](<01.01.01.03_Starting_SmarTest_with_engineer_mode.md>).

 Note Do not start SmarTest as root user.

The root user has access to all commands and files on the system controller adding the risk that changes are made to files that should not be changed.

## Before you begin
```

### 抽取的标题

- L6 `# Starting SmarTest`
- L8 `#### Subtopics`
- L15 `## About this task`
- L28 `## Before you begin`
- L41 `## Starting SmarTest from the task bar`
- L152 `## Starting SmarTest from the terminal`
- L426 `## Related information`
- L430 `## Functional changes`

### 抽取的边（20 条，显示前 10）

- L10 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.01_Starting_SmarTest_with_supervisor_mode.md`
  - 语境：[Starting SmarTest with supervisor mode](<01.01.01.01_Starting_SmarTest_with_supervisor_mode.md>)
- L11 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.02_Starting_SmarTest_with_operator_mode.md`
  - 语境：[Starting SmarTest with operator mode](<01.01.01.02_Starting_SmarTest_with_operator_mode.md>)
- L12 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.03_Starting_SmarTest_with_engineer_mode.md`
  - 语境：[Starting SmarTest with engineer mode](<01.01.01.03_Starting_SmarTest_with_engineer_mode.md>)
- L13 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.04_Changing_the_User_Mode.md`
  - 语境：[Changing the User Mode](<01.01.01.04_Changing_the_User_Mode.md>)
- L19 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01_Starting_SmarTest.md`
  - 语境：[Starting SmarTest from the task bar](<01.01.01_Starting_SmarTest.md#_107991__task_bar>)
- L20 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01_Starting_SmarTest.md`
  - 语境：[Starting SmarTest from the terminal](<01.01.01_Starting_SmarTest.md#_107991__terminal>)
- L22 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.01_Starting_SmarTest_with_supervisor_mode.md`
  - 语境：You can start the software in several ways, depending on what status you want to have. For details on each of these modes, refer to [ Starting SmarTest with supervisor mode](<01.01.01.01_Starting_SmarTest_with_supervisor_mode.md>), [ Starting SmarTest with operator mode](<01.01.01.02_Starting_SmarTe
- L22 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.02_Starting_SmarTest_with_operator_mode.md`
  - 语境：You can start the software in several ways, depending on what status you want to have. For details on each of these modes, refer to [ Starting SmarTest with supervisor mode](<01.01.01.01_Starting_SmarTest_with_supervisor_mode.md>), [ Starting SmarTest with operator mode](<01.01.01.02_Starting_SmarTe
- L22 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.03_Starting_SmarTest_with_engineer_mode.md`
  - 语境：You can start the software in several ways, depending on what status you want to have. For details on each of these modes, refer to [ Starting SmarTest with supervisor mode](<01.01.01.01_Starting_SmarTest_with_supervisor_mode.md>), [ Starting SmarTest with operator mode](<01.01.01.02_Starting_SmarTe
- L36 → `02_System_reference/02.04_Model_File_and_Licensing/02.04_Model_File_and_Licensing.md`
  - 语境：[Model File and Licensing](<../../02_System_reference/02.04_Model_File_and_Licensing/02.04_Model_File_and_Licensing.md>)

### 抽取的段落

- `Subtopics`（related，L8，359 字符）
  - 开头：'- [Starting SmarTest with supervisor mode](<01.01.01.01_Starting_SmarTest_with_supervisor_mode.md>)\n- [Starting SmarTest'
- `About this task`（procedure，L15，986 字符）
  - 开头：'Note This topic is applicable to SmarTest 7 only. This topic covers both how to start SmarTest from the command line in '
- `Before you begin`（constraint，L28，975 字符）
  - 开头：'The model file is used to store the test head hardware configuration. It specifies the installed test head cards, their '
- `Related information`（related，L426，207 字符）
  - 开头：'Switch Version tool[Switching between TML versions](<../01.02_SmarTest_workstation_administration/01.02.02.03.02.01_Swit'
- `Functional changes`（version，L430，173 字符）
  - 开头：'- Introduced before SmarTest 6.3.2\n- SmarTest 7.1.4: Renamed .device_inuse_soc file\n[1)](<>) Yes, if Engineer Password i'

---

## `01_Getting_started/01.01_SmarTest_Work_Center/01.01.02_Shutting_down_SmarTest.md`

*抽样理由：含 Procedure*

- 字节 1191 / 标题 3 / 出度 0 / 代码块 0
- frontmatter：`{"source_html": "01_Getting_started/01.01_SmarTest_Work_Center/01.01.02_Shutting_down_SmarTest.htm", "source_topic": "16264.htm", "title": "Shutting down SmarTest"}`
- title：`Shutting down SmarTest`
- 结构段落：['Functional changes', 'Procedure']

### 原文开头

```
---
title: "Shutting down SmarTest"
source_topic: "16264.htm"
source_html: "01_Getting_started/01.01_SmarTest_Work_Center/01.01.02_Shutting_down_SmarTest.htm"
---
# Shutting down SmarTest

This topic explains how to shut down SmarTest in engineering mode.

## Procedure

-  To shut down the SmarTest Work Center, from the menu click File > Exit.

A confirmation window opens.

   ![Exit Confirm](<../../../../raw/108788.png>)
-  To confirm the exit click OK.

  - If all data are saved, SmarTest shuts down.
  - If you changed any setup data, the system displays the Exit dialog. The Exit dialog lists any processes which may still be running, and any setup and resource files, which you did not save yet. ![SmarTest shutdown dialog](<../../../../raw/109592.png>)

-  If you want to save any of the changed setup data, click Cancel.
-  To continue the exit, click OK. In this case any changes to the listed files will be lost.

If SmarTest hangs up, on the main menu (Red Hat button on the task bar), click Red Hat button and select Advantest > kill SmarTest.

## Functional changes

```

### 抽取的标题

- L6 `# Shutting down SmarTest`
- L10 `## Procedure`
- L27 `## Functional changes`

### 抽取的边（0 条，显示前 10）


### 抽取的段落

- `Procedure`（procedure，L10，788 字符）
  - 开头：'-  To shut down the SmarTest Work Center, from the menu click File > Exit.\n\nA confirmation window opens.\n\n   ![Exit Conf'
- `Functional changes`（version，L27，76 字符）
  - 开头：'- Introduced before SmarTest 6.3.2\n- SmarTest 6.5.0: Enhanced exit sequence.'

---

## `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.01_Opening_a_perspective.md`

*抽样理由：含 Procedure；含 What to do next*

- 字节 1982 / 标题 6 / 出度 13 / 代码块 0
- frontmatter：`{"source_html": "01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.01_Opening_a_perspective.htm", "source_topic": "108352.htm", "title": "Opening a perspective"}`
- title：`Opening a perspective`
- 结构段落：['About this task', 'Functional changes', 'Procedure', 'Related information', 'What to do next']

### 原文开头

```
---
title: "Opening a perspective"
source_topic: "108352.htm"
source_html: "01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.01_Opening_a_perspective.htm"
---
# Opening a perspective

This topic describes how change the perspective. For details on perspectives, see [Perspectives](<01.01.07_Perspectives.md>).

## About this task

The following are predefined perspectives:

- [Setup](<01.01.07.02_Setup_perspective.md>)
- [C/C++](<01.01.07.03_C_C___perspective.md>)
- [Hardware](<01.01.07.05_Hardware_Perspective.md>)
- [Debug](<01.01.07.04_Debug_perspective.md>)

In addition to the predefined perspectives, you can define your own perspectives, see [Saving and resetting a perspective](<01.01.07.01.05_Saving_and_resetting_a_perspective.md>).

When you start SmarTest for the first time, the [93000 Setup perspective](<01.01.07.02_Setup_perspective.md>) will be opened by default.

## Procedure

-  Click the Open Perspective button ![Open Perspective button](<../../../../raw/123065.png>) or click Window > Open Perspective.

  -  On the shown menu, select the perspective you want to open.

```

### 抽取的标题

- L6 `# Opening a perspective`
- L10 `## About this task`
- L23 `## Procedure`
- L31 `## What to do next`
- L36 `## Related information`
- L40 `## Functional changes`

### 抽取的边（13 条，显示前 10）

- L8 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07_Perspectives.md`
  - 语境：This topic describes how change the perspective. For details on perspectives, see [Perspectives](<01.01.07_Perspectives.md>).
- L14 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.md`
  - 语境：[Setup](<01.01.07.02_Setup_perspective.md>)
- L15 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.03_C_C___perspective.md`
  - 语境：[C/C++](<01.01.07.03_C_C___perspective.md>)
- L16 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05_Hardware_Perspective.md`
  - 语境：[Hardware](<01.01.07.05_Hardware_Perspective.md>)
- L17 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.04_Debug_perspective.md`
  - 语境：[Debug](<01.01.07.04_Debug_perspective.md>)
- L19 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.05_Saving_and_resetting_a_perspective.md`
  - 语境：In addition to the predefined perspectives, you can define your own perspectives, see [Saving and resetting a perspective](<01.01.07.01.05_Saving_and_resetting_a_perspective.md>).
- L21 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.md`
  - 语境：When you start SmarTest for the first time, the [93000 Setup perspective](<01.01.07.02_Setup_perspective.md>) will be opened by default.
- L33 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.02_Arranging_views.md`
  - 语境：Adapt the perspective to your needs, see [Arranging views](<01.01.07.01.02_Arranging_views.md>), [Customizing toolbars and menus](<01.01.07.01.04_Customizing_toolbars_and_menus.md>), and [Saving and resetting a perspective](<01.01.07.01.05_Saving_and_resetting_a_perspective.md>).
- L33 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.04_Customizing_toolbars_and_menus.md`
  - 语境：Adapt the perspective to your needs, see [Arranging views](<01.01.07.01.02_Arranging_views.md>), [Customizing toolbars and menus](<01.01.07.01.04_Customizing_toolbars_and_menus.md>), and [Saving and resetting a perspective](<01.01.07.01.05_Saving_and_resetting_a_perspective.md>).
- L33 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.05_Saving_and_resetting_a_perspective.md`
  - 语境：Adapt the perspective to your needs, see [Arranging views](<01.01.07.01.02_Arranging_views.md>), [Customizing toolbars and menus](<01.01.07.01.04_Customizing_toolbars_and_menus.md>), and [Saving and resetting a perspective](<01.01.07.01.05_Saving_and_resetting_a_perspective.md>).

### 抽取的段落

- `About this task`（procedure，L10，552 字符）
  - 开头：'The following are predefined perspectives:\n\n- [Setup](<01.01.07.02_Setup_perspective.md>)\n- [C/C++](<01.01.07.03_C_C___p'
- `Procedure`（procedure，L23，295 字符）
  - 开头：'-  Click the Open Perspective button ![Open Perspective button](<../../../../raw/123065.png>) or click Window > Open Per'
- `What to do next`（procedure，L31，587 字符）
  - 开头：'- Adapt the perspective to your needs, see [Arranging views](<01.01.07.01.02_Arranging_views.md>), [Customizing toolbars'
- `Related information`（related，L36，42 字符）
  - 开头：'[Perspectives](<01.01.07_Perspectives.md>)'
- `Functional changes`（version，L40，34 字符）
  - 开头：'- Introduced before SmarTest 6.3.2'

---

## `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.04_Customizing_toolbars_and_menus.md`

*抽样理由：含 Before you begin*

- 字节 2025 / 标题 5 / 出度 5 / 代码块 0
- frontmatter：`{"source_html": "01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.04_Customizing_toolbars_and_menus.htm", "source_topic": "112889.htm", "title": "Customizing toolbars and menus"}`
- title：`Customizing toolbars and menus`
- 结构段落：['Before you begin', 'Functional changes', 'Procedure', 'Related information']

### 原文开头

```
---
title: "Customizing toolbars and menus"
source_topic: "112889.htm"
source_html: "01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.04_Customizing_toolbars_and_menus.htm"
---
# Customizing toolbars and menus

This topic describes how to configure the toolbar buttons and menu items of a perspective.

## Before you begin

Open the perspective which you want to configure.

## Procedure

-  On the menu, click Window > Customize Perspective.

The Customize Perspective window opens.

  ![Perspective_Customize perspective - Setup](<../../../../raw/130410.png>)

The window contains the following tabs:

  - Tool Bar Visibility: Showing and hiding toolbar buttons
  - Menu Visibility: Showing and hiding menu items
  - Command Groups Availability: Adding and removing command groups to and from the current perspective.
  - Shortcuts: Showing and hiding the shortcuts buttons which will be added as cascade items to the chosen submenus.Note On the Shortcuts tab, you cannot configure keyboard shortcuts. For keyboard shortcuts, see [Useful keyboard shortcuts](<01.01.16_Useful_keyboard_shortcuts__key_bindings.md>).

```

### 抽取的标题

- L6 `# Customizing toolbars and menus`
- L10 `## Before you begin`
- L14 `## Procedure`
- L38 `## Related information`
- L42 `## Functional changes`

### 抽取的边（5 条，显示前 10）

- L27 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.16_Useful_keyboard_shortcuts__key_bindings.md`
  - 语境：Shortcuts: Showing and hiding the shortcuts buttons which will be added as cascade items to the chosen submenus.Note On the Shortcuts tab, you cannot configure keyboard shortcuts. For keyboard shortcuts, see [Useful keyboard shortcuts](<01.01.16_Useful_keyboard_shortcuts__key_bindings.md>).
- L40 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01_Working_with_a_perspective.md`
  - 语境：[Working with a perspective](<01.01.07.01_Working_with_a_perspective.md>)[Arranging views](<01.01.07.01.02_Arranging_views.md>)[Opening a view and adding it to the perspective](<01.01.07.01.03_Opening_a_view_and_adding_it_to_the_perspective.md>)[Saving and resetting a perspective](<01.01.07.01.05_Sa
- L40 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.02_Arranging_views.md`
  - 语境：[Working with a perspective](<01.01.07.01_Working_with_a_perspective.md>)[Arranging views](<01.01.07.01.02_Arranging_views.md>)[Opening a view and adding it to the perspective](<01.01.07.01.03_Opening_a_view_and_adding_it_to_the_perspective.md>)[Saving and resetting a perspective](<01.01.07.01.05_Sa
- L40 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.03_Opening_a_view_and_adding_it_to_the_perspective.md`
  - 语境：[Working with a perspective](<01.01.07.01_Working_with_a_perspective.md>)[Arranging views](<01.01.07.01.02_Arranging_views.md>)[Opening a view and adding it to the perspective](<01.01.07.01.03_Opening_a_view_and_adding_it_to_the_perspective.md>)[Saving and resetting a perspective](<01.01.07.01.05_Sa
- L40 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.01.05_Saving_and_resetting_a_perspective.md`
  - 语境：[Working with a perspective](<01.01.07.01_Working_with_a_perspective.md>)[Arranging views](<01.01.07.01.02_Arranging_views.md>)[Opening a view and adding it to the perspective](<01.01.07.01.03_Opening_a_view_and_adding_it_to_the_perspective.md>)[Saving and resetting a perspective](<01.01.07.01.05_Sa

### 抽取的段落

- `Before you begin`（constraint，L10，49 字符）
  - 开头：'Open the perspective which you want to configure.'
- `Procedure`（procedure，L14，1160 字符）
  - 开头：'-  On the menu, click Window > Customize Perspective.\n\nThe Customize Perspective window opens.\n\n  ![Perspective_Customiz'
- `Related information`（related，L38，337 字符）
  - 开头：'[Working with a perspective](<01.01.07.01_Working_with_a_perspective.md>)[Arranging views](<01.01.07.01.02_Arranging_vie'
- `Functional changes`（version，L42，34 字符）
  - 开头：'- Introduced before SmarTest 6.3.2'

---

## `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.04_Renaming_a_single_setup_component.md`

*抽样理由：含 What to do next*

- 字节 1241 / 标题 5 / 出度 0 / 代码块 0
- frontmatter：`{"source_html": "01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.04_Renaming_a_single_setup_component.htm", "source_topic": "96417.htm", "title": "Renaming a single setup component"}`
- title：`Renaming a single setup component`
- 结构段落：['About this task', 'Procedure', 'What to do next']

### 原文开头

```
---
title: "Renaming a single setup component"
source_topic: "96417.htm"
source_html: "01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.04_Renaming_a_single_setup_component.htm"
---
# Renaming a single setup component

## About this task

Do not change file names directly in the file system, while SmarTest is running. If you rename a test component file in a Linux shell, SmarTest cannot recognize the file and will issue an error.

Instead, use the file handling functionality provided by the Test Program Explorer:

## Procedure

-  In the Test Program Explorer highlight the item (file) the name of which you want to change, for example the testflow.
-  Right-click and select Save As... .
-  The Enter or select new file name window is displayed. Type the new file name in the Selection: field. Note Do not use the button Rename File.
-  Click OK. The renamed item is shown in the Test Program Explorer.
-  Delete the original file using the Device Navigator or a Linux shell.

## Results

SmarTest creates a new setup file containing the content of the original component.

## What to do next

You can now open the renamed setup component by double-clicking it in the Test Program Explorer.
```

### 抽取的标题

- L6 `# Renaming a single setup component`
- L8 `## About this task`
- L14 `## Procedure`
- L22 `## Results`
- L26 `## What to do next`

### 抽取的边（0 条，显示前 10）


### 抽取的段落

- `About this task`（procedure，L8，279 字符）
  - 开头：'Do not change file names directly in the file system, while SmarTest is running. If you rename a test component file in '
- `Procedure`（procedure，L14，448 字符）
  - 开头：'-  In the Test Program Explorer highlight the item (file) the name of which you want to change, for example the testflow'
- `What to do next`（procedure，L26，96 字符）
  - 开头：'You can now open the renamed setup component by double-clicking it in the Test Program Explorer.'

---

## `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11_Menu_bar.md`

*抽样理由：01_Getting_started 中位*

- 字节 1444 / 标题 4 / 出度 8 / 代码块 0
- frontmatter：`{"source_html": "01_Getting_started/01.01_SmarTest_Work_Center/01.01.11_Menu_bar.htm", "source_topic": "350785.htm", "title": "Menu bar"}`
- title：`Menu bar`
- 结构段落：['Functional changes', 'Subtopics']

### 原文开头

```
---
title: "Menu bar"
source_topic: "350785.htm"
source_html: "01_Getting_started/01.01_SmarTest_Work_Center/01.01.11_Menu_bar.htm"
---
# Menu bar

#### Subtopics

- [93000 menu and its tools](<01.01.11.01_93000_menu_and_its_tools.md>)
- [Project menu](<01.01.11.02_Project_menu.md>)
- [Run menu](<01.01.11.03_Run_menu.md>)
- [Window menu](<01.01.11.04_Window_menu.md>)

The Menu Bar along the top of the main window includes a series of pull-down menus.

## SmarTest Eclipse Workcenter main menu bar

   ![SmarTest Eclipse Workcenter main menu](<../../../../raw/350806.png>)     File Controls for opening, closing and saving files, importing and exporting projects, saving data, switching workspaces, accessing properties, and printing.  Edit Controls for finding and modifying data. Navigate Controls for navigating annotations, trees, files, and repositories. Search Controls for search tools. [Project menu](<01.01.11.02_Project_menu.md>) Controls for opening, cleaning and building projects. [93000 menu and its tools](<01.01.11.01_93000_menu_and_its_tools.md>) Controls for accessing the SmarTest tools [Run menu](<01.01.11.03_Run_menu.md>) Controls for running and debugging your test programs, testflows, and test methods. [Window menu](<01.01.11.04_Window_menu.md>) Controls for navigation and managing views and perspectives. Help Online help information.

## Functional changes

- Introduced in SmarTest 7.5.4

```

### 抽取的标题

- L6 `# Menu bar`
- L8 `#### Subtopics`
- L17 `## SmarTest Eclipse Workcenter main menu bar`
- L21 `## Functional changes`

### 抽取的边（8 条，显示前 10）

- L10 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.01_93000_menu_and_its_tools.md`
  - 语境：[93000 menu and its tools](<01.01.11.01_93000_menu_and_its_tools.md>)
- L11 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.02_Project_menu.md`
  - 语境：[Project menu](<01.01.11.02_Project_menu.md>)
- L12 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.03_Run_menu.md`
  - 语境：[Run menu](<01.01.11.03_Run_menu.md>)
- L13 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.04_Window_menu.md`
  - 语境：[Window menu](<01.01.11.04_Window_menu.md>)
- L19 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.02_Project_menu.md`
  - 语境：![SmarTest Eclipse Workcenter main menu](<../../../../raw/350806.png>) File Controls for opening, closing and saving files, importing and exporting projects, saving data, switching workspaces, accessing properties, and printing. Edit Controls for finding and modifying data. Navigate Controls for nav
- L19 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.01_93000_menu_and_its_tools.md`
  - 语境：![SmarTest Eclipse Workcenter main menu](<../../../../raw/350806.png>) File Controls for opening, closing and saving files, importing and exporting projects, saving data, switching workspaces, accessing properties, and printing. Edit Controls for finding and modifying data. Navigate Controls for nav
- L19 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.03_Run_menu.md`
  - 语境：![SmarTest Eclipse Workcenter main menu](<../../../../raw/350806.png>) File Controls for opening, closing and saving files, importing and exporting projects, saving data, switching workspaces, accessing properties, and printing. Edit Controls for finding and modifying data. Navigate Controls for nav
- L19 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.04_Window_menu.md`
  - 语境：![SmarTest Eclipse Workcenter main menu](<../../../../raw/350806.png>) File Controls for opening, closing and saving files, importing and exporting projects, saving data, switching workspaces, accessing properties, and printing. Edit Controls for finding and modifying data. Navigate Controls for nav

### 抽取的段落

- `Subtopics`（related，L8，290 字符）
  - 开头：'- [93000 menu and its tools](<01.01.11.01_93000_menu_and_its_tools.md>)\n- [Project menu](<01.01.11.02_Project_menu.md>)\n'
- `Functional changes`（version，L21，30 字符）
  - 开头：'- Introduced in SmarTest 7.5.4'

---

## `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.03.02.01_Switching_between_TML_versions.md`

*抽样理由：含 Errors*

- 字节 2878 / 标题 8 / 出度 3 / 代码块 3
- frontmatter：`{"source_html": "01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.03.02.01_Switching_between_TML_versions.htm", "source_topic": "151655.htm", "title": "Switching between TML versions"}`
- title：`Switching between TML versions`
- 结构段落：['Errors', 'Example', 'Functional changes', 'Parameters', 'Prerequisites', 'Related information', 'Syntax']

### 原文开头

```
---
title: "Switching between TML versions"
source_topic: "151655.htm"
source_html: "01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.03.02.01_Switching_between_TML_versions.htm"
---
# Switching between TML versions

The switch version tool allows you to switch between different versions of test method libraries (TML) installed on your system controller.

TML is named as tml_x.y.z_r.s.t, where x.y.z is the SmarTest version number, r.s.t is the TML version number. This means this TML version r.s.t is for SmarTest x.y.z. For example, tml_6.5.4_2.1.0 means TML 2.1.0 for SmarTest 6.5.4. You can only use it for SmarTest 6.5.4. For MTP, see [Switching to a different MTP version](<../../02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.01_Switching_to_a_different_MTP_version_on_SmarTest.md>).

To select a SmarTest version or a version of SmarTest together with a TML version, you can either run switch_version with the dedicated versions as options, or run it without any options to show a list of the installed versions, see [Switching between TML versions](<01.02.02.03.02.01_Switching_between_TML_versions.md>).

## Prerequisites

 Note This topic is applicable to SmarTest 7 only.

- Make sure your SmarTest installation is version 6.5.4 or later, but excluding SmarTest 8.x.
- Several versions of SmarTest or MTP are installed
- The software is not running

## Syntax

```
/opt/hp93000/soc_common/bin/switch_version <valid software version> [-tml <valid tml_version>]
```

## Parameters
```

### 抽取的标题

- L6 `# Switching between TML versions`
- L14 `## Prerequisites`
- L22 `## Syntax`
- L28 `## Parameters`
- L59 `## Errors`
- L93 `## Example`
- L101 `## Related information`
- L105 `## Functional changes`

### 抽取的边（3 条，显示前 10）

- L10 → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.01_Switching_to_a_different_MTP_version_on_SmarTest.md`
  - 语境：TML is named as tml_x.y.z_r.s.t, where x.y.z is the SmarTest version number, r.s.t is the TML version number. This means this TML version r.s.t is for SmarTest x.y.z. For example, tml_6.5.4_2.1.0 means TML 2.1.0 for SmarTest 6.5.4. You can only use it for SmarTest 6.5.4. For MTP, see [Switching to a
- L12 → `01_Getting_started/01.02_SmarTest_workstation_administration/01.02.02.03.02.01_Switching_between_TML_versions.md`
  - 语境：To select a SmarTest version or a version of SmarTest together with a TML version, you can either run switch_version with the dedicated versions as options, or run it without any options to show a list of the installed versions, see [Switching between TML versions](<01.02.02.03.02.01_Switching_betwe
- L103 → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.01_Switching_to_a_different_MTP_version_on_SmarTest.md`
  - 语境：[Switching to a different MTP version on SmarTest](<../../02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.01_Switching_to_a_different_MTP_version_on_SmarTest.md>)

### 抽取的段落

- `Prerequisites`（constraint，L14，226 字符）
  - 开头：'Note This topic is applicable to SmarTest 7 only.\n\n- Make sure your SmarTest installation is version 6.5.4 or later, but'
- `Syntax`（syntax，L22，102 字符）
  - 开头：'```\n/opt/hp93000/soc_common/bin/switch_version <valid software version> [-tml <valid tml_version>]\n```'
- `Parameters`（syntax，L28，238 字符）
  - 开头：'|\n\nvalid software version\n\n |\n\n- SmarTest release:\n\nsoc64_<release number>\n\n- MTP release:\n\nmts-<release number> or\n\nmts'
- `Errors`（error，L59，523 字符）
  - 开头：'If switch_version detects any shared memory, semaphores, or message queues left over by other users and they contain 0x9'
- `Example`（syntax，L93，138 字符）
  - 开头：'To switch to SmarTest release 7.2.0 and a compatible test method library, type:\n\n```\nswitch_version soc64_7.2.0 -tml tml'
- `Related information`（related，L101，173 字符）
  - 开头：'[Switching to a different MTP version on SmarTest](<../../02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.01_'

---

## `01_Getting_started/index.md`

*抽样理由：01_Getting_started 末篇；解析异常 no_frontmatter*

- 字节 33512 / 标题 1 / 出度 255 / 代码块 0
- frontmatter：`null`
- title：`01_Getting_started`
- 结构段落：（无）
- ⚠️ 解析异常：[{'detail': '文件首行不是 ---', 'doc': '01_Getting_started/index.md', 'kind': 'no_frontmatter'}, {'detail': '', 'doc': '01_Getting_started/index.md', 'kind': 'not_in_catalog'}]

### 原文开头

```
# 01_Getting_started

- [Starting SmarTest with supervisor mode](01.01_SmarTest_Work_Center/01.01.01.01_Starting_SmarTest_with_supervisor_mode.md)
  - `43518.htm`
- [Starting SmarTest with operator mode](01.01_SmarTest_Work_Center/01.01.01.02_Starting_SmarTest_with_operator_mode.md)
  - `43520.htm`
- [Starting SmarTest with engineer mode](01.01_SmarTest_Work_Center/01.01.01.03_Starting_SmarTest_with_engineer_mode.md)
  - `43523.htm`
- [Changing the SmarTest Mode Passwords](01.01_SmarTest_Work_Center/01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md)
  - `43571.htm`
- [Changing the User Mode](01.01_SmarTest_Work_Center/01.01.01.04_Changing_the_User_Mode.md)
  - `43524.htm`
- [Starting SmarTest](01.01_SmarTest_Work_Center/01.01.01_Starting_SmarTest.md)
  - `107991.htm`
- [Shutting down SmarTest](01.01_SmarTest_Work_Center/01.01.02_Shutting_down_SmarTest.md)
  - `16264.htm`
- [SmarTest in Eclipse 4](01.01_SmarTest_Work_Center/01.01.03_SmarTest_in_Eclipse_4.md)
  - `351407.htm`
- [Creating and opening a workspace](01.01_SmarTest_Work_Center/01.01.04.01_Creating_and_opening_a_workspace.md)
  - `130442.htm`
- [Warnings and error messages when starting SmarTest](01.01_SmarTest_Work_Center/01.01.04.02_Warnings_and_error_messages_when_starting_SmarTest.md)
  - `130443.htm`
- [SmarTest workspaces](01.01_SmarTest_Work_Center/01.01.04_SmarTest_workspaces.md)
  - `91571.htm`
- [SmarTest project configuration](01.01_SmarTest_Work_Center/01.01.05_SmarTest_project_configuration.md)
  - `132841.htm`
- [About projects, file system, and references](01.01_SmarTest_Work_Center/01.01.06_About_projects__file_system__and_references.md)
  - `130434.htm`
```

### 抽取的标题

- L1 `# 01_Getting_started`

### 抽取的边（255 条，显示前 10）

- L3 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.01_Starting_SmarTest_with_supervisor_mode.md`
  - 语境：[Starting SmarTest with supervisor mode](01.01_SmarTest_Work_Center/01.01.01.01_Starting_SmarTest_with_supervisor_mode.md)
- L5 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.02_Starting_SmarTest_with_operator_mode.md`
  - 语境：[Starting SmarTest with operator mode](01.01_SmarTest_Work_Center/01.01.01.02_Starting_SmarTest_with_operator_mode.md)
- L7 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.03_Starting_SmarTest_with_engineer_mode.md`
  - 语境：[Starting SmarTest with engineer mode](01.01_SmarTest_Work_Center/01.01.01.03_Starting_SmarTest_with_engineer_mode.md)
- L9 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md`
  - 语境：[Changing the SmarTest Mode Passwords](01.01_SmarTest_Work_Center/01.01.01.04.01_Changing_the_SmarTest_Mode_Passwords.md)
- L11 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01.04_Changing_the_User_Mode.md`
  - 语境：[Changing the User Mode](01.01_SmarTest_Work_Center/01.01.01.04_Changing_the_User_Mode.md)
- L13 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.01_Starting_SmarTest.md`
  - 语境：[Starting SmarTest](01.01_SmarTest_Work_Center/01.01.01_Starting_SmarTest.md)
- L15 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.02_Shutting_down_SmarTest.md`
  - 语境：[Shutting down SmarTest](01.01_SmarTest_Work_Center/01.01.02_Shutting_down_SmarTest.md)
- L17 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.03_SmarTest_in_Eclipse_4.md`
  - 语境：[SmarTest in Eclipse 4](01.01_SmarTest_Work_Center/01.01.03_SmarTest_in_Eclipse_4.md)
- L19 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.04.01_Creating_and_opening_a_workspace.md`
  - 语境：[Creating and opening a workspace](01.01_SmarTest_Work_Center/01.01.04.01_Creating_and_opening_a_workspace.md)
- L21 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.04.02_Warnings_and_error_messages_when_starting_SmarTest.md`
  - 语境：[Warnings and error messages when starting SmarTest](01.01_SmarTest_Work_Center/01.01.04.02_Warnings_and_error_messages_when_starting_SmarTest.md)

---

## `02_System_reference/02.01_Release_Information/02.01.01_SmarTest_Release_Concept.md`

*抽样理由：02_System_reference 首篇*

- 字节 3216 / 标题 7 / 出度 0 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.01_Release_Information/02.01.01_SmarTest_Release_Concept.htm", "source_topic": "250854.htm", "title": "SmarTest Release Concept"}`
- title：`SmarTest Release Concept`
- 结构段落：（无）

### 原文开头

```
---
title: "SmarTest Release Concept"
source_topic: "250854.htm"
source_html: "02_System_reference/02.01_Release_Information/02.01.01_SmarTest_Release_Concept.htm"
---
# SmarTest Release Concept

SmarTest has different types of releases, each of which has its own life cycle. The release types follow an overall cycle that is divided into four phases.

SmarTest releases follow a general cycle of rapidly adding features in a technology phase, providing a stable release, fixing bugs and polishing features for that stable release, and discontinuing that release.

## 1. Technology phase

During the Technology Phase multiple so-called technology releases are delivered. Technology releases primarily deliver new functionality. They also include enhancements and defect fixes.

Patches to technology releases are provided to fix blockers, critical defects, and serious defects. New functionality or enhancements are not included in patches. Patches are cumulative, that is, later patches include bug fixes from earlier patches for the same release.

## 2. Enterprise phase (typically 1 year)

The enterprise phase begins when all planned new functionality is fully integrated into the particular release stream and when defined quality measures are met. The release is named "enterprise release". Enterprise releases are recommended for all new customer test program developments and for deployment in device production.

No new functionality or enhancements is added once a release is in the enterprise phase.

Patches to enterprise releases include fixes for blockers, critical defects, and serious customer-reported defects. They are cumulative, that is, later patches include bug fixes from earlier patches for the same release.

## 3. Maintenance phase (typically 1 year)

The maintenance phase follows the enterprise phase. The release is named "enterprise release (in maintenance phase)". We recommend that you do not use a release to develop new applications once it has reached ts maintenance phase.
```

### 抽取的标题

- L6 `# SmarTest Release Concept`
- L12 `## 1. Technology phase`
- L18 `## 2. Enterprise phase (typically 1 year)`
- L26 `## 3. Maintenance phase (typically 1 year)`
- L32 `## 4. Discontinuance phase`
- L36 `## Overview of phases`
- L44 `## Release name examples`

### 抽取的边（0 条，显示前 10）


---

## `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.05_XPS256_programming_-_Default_values.md`

*抽样理由：补齐（全库等距，非随机）*

- 字节 11089 / 标题 5 / 出度 74 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.05_XPS256_programming_-_Default_values.htm", "source_topic": "354611.htm", "title": "XPS256 programming - Default values"}`
- title：`XPS256 programming - Default values`
- 结构段落：['Functional changes', 'Related information']

### 原文开头

```
---
title: "XPS256 programming - Default values"
source_topic: "354611.htm"
source_html: "02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.05_XPS256_programming_-_Default_values.htm"
---
# XPS256 programming - Default values

For XPS256, global default values for parameters relating to the dynamic behavior and the protection of the hardware can be defined in the pin configuration for a test program. These default values override the system鈥慸efined default values and can in turn be overridden by setting these parameters by DPSPINS resource parameters or TM APIs.

The global default values for parameters relating to the dynamic behavior can be defined in the DC Scale Regulation editor. The protection and safety related parameters can be defined in the [DC Scale Safety editor](<02.05.05.03.10.05_XPS256_programming_-_Default_values.md#_354611__s_DC_Scale_Safety_editor>).

## DC Scale Regulation editor

 The [DC Scale Regulation editor](<../02.08_Setup_and_Result_Tools/02.08.04.18.03.07_DC_Scale_Regulation_editor.md>) is used to set global defaults for regulation parameters.

 ![DC Scale Regulation editor](<../../../../raw/354626.png>)

 Available settings and APIs that override the settings of the editor:

 | Column  | [DPSPINS resources](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md>)  | [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>)  | [SmartRDI rdi.dc()](<../02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) |
 | [Voltage filter[Hz]](<02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md#_352356__li_Voltage_bandwidth_filter_table>)  | [voltage_filter_frequency](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__voltage_filter_frequency>)  | [vFilter()](<../02.07_Test_Method_Reference/02.07.04.01.234.01.33_SPMU_PIN_TASK.vFilter.md>)  | [vFilter()](<../02.07_Test_Method_Reference/02.07.13.12.02.40_vFilter.md>) |
 | [Voltage slew[mV/us]](<02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md#_352356__li_Voltage_slew_rate_table>)  | [voltage_slew_rate](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__voltage_slew_rate>)  | [vSlewRate()](<../02.07_Test_Method_Reference/02.07.04.01.234.01.38_SPMU_PIN_TASK.vSlewRate.md>)  | [vSlewRate()](<../02.07_Test_Method_Reference/02.07.13.12.02.48_vSlewRate.md>) |
 | [Current filter[Hz]](<02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md#_352356__li_Current_bandwidth_filter_table>)  | [current_filter_frequency](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__current_filter_frequency>)  | [iFilter()](<../02.07_Test_Method_Reference/02.07.04.01.234.01.13_SPMU_PIN_TASK.iFilter.md>) |

[iFilter()](<../02.07_Test_Method_Reference/02.07.13.12.02.15_iFilter.md>)

[iClampFilter()](<../02.07_Test_Method_Reference/02.07.13.12.02.12_iClampFilter.md>)

```

### 抽取的标题

- L6 `# XPS256 programming - Default values`
- L12 `## DC Scale Regulation editor`
- L36 `## DC Scale Safety editor`
- L93 `## Related information`
- L97 `## Functional changes`

### 抽取的边（74 条，显示前 10）

- L10 → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.05_XPS256_programming_-_Default_values.md`
  - 语境：The global default values for parameters relating to the dynamic behavior can be defined in the DC Scale Regulation editor. The protection and safety related parameters can be defined in the [DC Scale Safety editor](<02.05.05.03.10.05_XPS256_programming_-_Default_values.md#_354611__s_DC_Scale_Safety
- L14 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.07_DC_Scale_Regulation_editor.md`
  - 语境：The [DC Scale Regulation editor](<../02.08_Setup_and_Result_Tools/02.08.04.18.03.07_DC_Scale_Regulation_editor.md>) is used to set global defaults for regulation parameters.
- L20 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`
  - 语境：| Column | [DPSPINS resources](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md>) | [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>) | [SmartRDI rdi.dc()](<../02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_Sm
- L20 → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md`
  - 语境：| Column | [DPSPINS resources](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md>) | [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>) | [SmartRDI rdi.dc()](<../02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_Sm
- L20 → `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md`
  - 语境：| Column | [DPSPINS resources](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md>) | [SPMU_PIN_TASK](<../02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.md>) | [SmartRDI rdi.dc()](<../02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_Sm
- L21 → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md`
  - 语境：| [Voltage filter[Hz]](<02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md#_352356__li_Voltage_bandwidth_filter_table>) | [voltage_filter_frequency](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__voltage_filter_frequency>) | [vFilter()](<../02.07_Test
- L21 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`
  - 语境：| [Voltage filter[Hz]](<02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md#_352356__li_Voltage_bandwidth_filter_table>) | [voltage_filter_frequency](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__voltage_filter_frequency>) | [vFilter()](<../02.07_Test
- L21 → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.33_SPMU_PIN_TASK.vFilter.md`
  - 语境：| [Voltage filter[Hz]](<02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md#_352356__li_Voltage_bandwidth_filter_table>) | [voltage_filter_frequency](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__voltage_filter_frequency>) | [vFilter()](<../02.07_Test
- L21 → `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.40_vFilter.md`
  - 语境：| [Voltage filter[Hz]](<02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md#_352356__li_Voltage_bandwidth_filter_table>) | [voltage_filter_frequency](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__voltage_filter_frequency>) | [vFilter()](<../02.07_Test
- L22 → `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md`
  - 语境：| [Voltage slew[mV/us]](<02.05.05.03.10.11_XPS256_programming_-_Load_step_response.md#_352356__li_Voltage_slew_rate_table>) | [voltage_slew_rate](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md#_16887__voltage_slew_rate>) | [vSlewRate()](<../02.07_Test_Method_Reference/

### 抽取的段落

- `Related information`（related，L93，214 字符）
  - 开头：'[DC Scale Regulation editor](<../02.08_Setup_and_Result_Tools/02.08.04.18.03.07_DC_Scale_Regulation_editor.md>)[DC Scale'
- `Functional changes`（version，L97，189 字符）
  - 开头：'- Introduced in SmarTest 7.10.1\n- SmarTest 7.10.2: Shutdown of XPS256 pins via utility lines: New "Safetyln Pin" column.'

---

## `02_System_reference/02.06_Command_Reference/02.06.02.02.02_APDV_-__APpenD_Vectors.md`

*抽样理由：含 Predependencies；含 Errors*

- 字节 3034 / 标题 11 / 出度 4 / 代码块 2
- frontmatter：`{"source_html": "02_System_reference/02.06_Command_Reference/02.06.02.02.02_APDV_-__APpenD_Vectors.htm", "source_topic": "98313.htm", "title": "APDV - (APpenD Vectors)"}`
- title：`APDV - (APpenD Vectors)`
- 结构段落：['Application', 'Errors', 'Example', 'Functional changes', 'Mode of operation', 'Parameters', 'Postdependencies', 'Predependencies', 'Related information', 'Syntax']

### 原文开头

```
---
title: "APDV - (APpenD Vectors)"
source_topic: "98313.htm"
source_html: "02_System_reference/02.06_Command_Reference/02.06.02.02.02_APDV_-__APpenD_Vectors.htm"
---
# APDV - (APpenD Vectors)

The APDV (APpenD Vectors) command appends vectors at the end of a sequencer construct.

## Predependencies

- The instruction of the construct must be GENV, RPTV, or MRPT.
- The APDV command can only be issued after a label has been selected for editing with the [TSTL](<02.06.02.02.281_TSTL__TSTL__-__TeST_Label.md>) command.

## Mode of operation

If the additional active vectors can be accommodated by the inactive vectors within the vector area segment of the label, the total length of this segment need not be increased. In this case, APDV just updates the length of the construct and moves comments so that they are aligned to the correct vectors. If the length of the segment increases, the command also expands the vector areas of the pins and updates the STVA instructions of the labels that use later segments of the vector area.

## Postdependencies

To generate useful data for the sequencer construct, you must overwrite the appended vectors with appropriate physical waveform DC/DC power units. You can do this with the command [VDCP, VDCP? (Vector Device Cycle Parameter)](<02.06.02.02.323_VDCP__VDCP___Vector_Device_Cycle_Parameter.md>).

## Syntax

```
APDV {cmd_No}, {vect_length}
```

```

### 抽取的标题

- L6 `# APDV - (APpenD Vectors)`
- L10 `## Predependencies`
- L15 `## Mode of operation`
- L19 `## Postdependencies`
- L23 `## Syntax`
- L29 `## Parameters`
- L50 `## Application`
- L54 `## Errors`
- L65 `## Example`
- L88 `## Related information`
- L92 `## Functional changes`

### 抽取的边（4 条，显示前 10）

- L13 → `02_System_reference/02.06_Command_Reference/02.06.02.02.281_TSTL__TSTL__-__TeST_Label.md`
  - 语境：The APDV command can only be issued after a label has been selected for editing with the [TSTL](<02.06.02.02.281_TSTL__TSTL__-__TeST_Label.md>) command.
- L21 → `02_System_reference/02.06_Command_Reference/02.06.02.02.323_VDCP__VDCP___Vector_Device_Cycle_Parameter.md`
  - 语境：To generate useful data for the sequencer construct, you must overwrite the appended vectors with appropriate physical waveform DC/DC power units. You can do this with the command [VDCP, VDCP? (Vector Device Cycle Parameter)](<02.06.02.02.323_VDCP__VDCP___Vector_Device_Cycle_Parameter.md>).
- L60 → `02_System_reference/02.06_Command_Reference/02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md`
  - 语境：The specified command number refers to a sequencer instruction other than GENV, RPTV, or MRPT, see the command [SQPG, SQPG? - (SeQuencer ProGramming)](<02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md>).
- L90 → `02_System_reference/02.06_Command_Reference/02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md`
  - 语境：[SQPG, SQPG? - (SeQuencer ProGramming)](<02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md>)

### 抽取的段落

- `Predependencies`（constraint，L10，218 字符）
  - 开头：'- The instruction of the construct must be GENV, RPTV, or MRPT.\n- The APDV command can only be issued after a label has '
- `Mode of operation`（concept，L15，491 字符）
  - 开头：'If the additional active vectors can be accommodated by the inactive vectors within the vector area segment of the label'
- `Postdependencies`（constraint，L19，291 字符）
  - 开头：'To generate useful data for the sequencer construct, you must overwrite the appended vectors with appropriate physical w'
- `Syntax`（syntax，L23，36 字符）
  - 开头：'```\nAPDV {cmd_No}, {vect_length}\n```'
- `Parameters`（syntax，L29，332 字符）
  - 开头：'|\n\ncmd_No\n\n |\n\nA number that identifies the command within the sequencer area of the port to which the label belongs. En'
- `Application`（concept，L50，29 字符）
  - 开头：'Edit command in Pattern Tool.'

---

## `02_System_reference/02.06_Command_Reference/02.06.02.02.08_BCMT__BCMT__-__Binary_CoMmenT.md`

*抽样理由：含 Predependencies*

- 字节 4310 / 标题 8 / 出度 2 / 代码块 4
- frontmatter：`{"source_html": "02_System_reference/02.06_Command_Reference/02.06.02.02.08_BCMT__BCMT__-__Binary_CoMmenT.htm", "source_topic": "98488.htm", "title": "BCMT, BCMT? - (Binary CoMmenT)"}`
- title：`BCMT, BCMT? - (Binary CoMmenT)`
- 结构段落：['Application', 'Errors', 'Example', 'Functional changes', 'Predependencies']

### 原文开头

```
---
title: "BCMT, BCMT? - (Binary CoMmenT)"
source_topic: "98488.htm"
source_html: "02_System_reference/02.06_Command_Reference/02.06.02.02.08_BCMT__BCMT__-__Binary_CoMmenT.htm"
---
# BCMT, BCMT? - (Binary CoMmenT)

The BCMT (Binary CoMmenT) command downloads comments in binary format for a specified vector range. The BCMT? query reads the comments of the specified port.

## Predependencies

Note that BCMT can only be issued in the LOAD or APP operation modes, not in the default EDIT operation mode. The operation mode is set with the [SAOF](<02.06.02.02.216_SAOF__SAOF__-__Set_Alternating_Operation_Features.md>) command.

## BCMT

```
BCMT {vect_addr}, {vect_length}[, HIMEN][, (port)], {#spec(data)}
```

## BCMT?

```
BCMT? [(portlist)]
```

returns:

```
```

### 抽取的标题

- L6 `# BCMT, BCMT? - (Binary CoMmenT)`
- L10 `## Predependencies`
- L14 `## BCMT`
- L20 `## BCMT?`
- L93 `## Application`
- L97 `## Errors`
- L108 `## Example`
- L118 `## Functional changes`

### 抽取的边（2 条，显示前 10）

- L12 → `02_System_reference/02.06_Command_Reference/02.06.02.02.216_SAOF__SAOF__-__Set_Alternating_Operation_Features.md`
  - 语境：Note that BCMT can only be issued in the LOAD or APP operation modes, not in the default EDIT operation mode. The operation mode is set with the [SAOF](<02.06.02.02.216_SAOF__SAOF__-__Set_Alternating_Operation_Features.md>) command.
- L55 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md`
  - 语境：If this parameter is specified, the data format of #spec(data) will be treated as 64-bit. If the HIMEM parameter is omitted, the data format will be treated as 32-bit. If you want to set any comments to over 2GB vector address, you should also use the himem:on parameter in the [.technology file](<..

### 抽取的段落

- `Predependencies`（constraint，L10，232 字符）
  - 开头：'Note that BCMT can only be issued in the LOAD or APP operation modes, not in the default EDIT operation mode. The operat'
- `Application`（concept，L93，34 字符）
  - 开头：'Download comments in Pattern Tool.'
- `Errors`（error，L97，412 字符）
  - 开头：'An error is generated if:\n\n- The specified address exceeds the maximum vector address allowed by the system.\n- You speci'
- `Example`（syntax，L108，424 字符）
  - 开头：'```\n> BCMT?\n< BCMT 0,49,#9000000078&!This is the first vector\n  of test_2&0This is the first vector of test_3\n```\n\nThis '
- `Functional changes`（version，L118，101 字符）
  - 开头：'- Introduced before SmarTest 6.3.2\n- SmarTest 6.5.3: Maximum comment length increased from 40 to 250.'

---

## `02_System_reference/02.06_Command_Reference/02.06.13.02.03_TSER__-__TMU_Set_ERror.md`

*抽样理由：体积中位 1686B*

- 字节 1686 / 标题 6 / 出度 1 / 代码块 3
- frontmatter：`{"source_html": "02_System_reference/02.06_Command_Reference/02.06.13.02.03_TSER__-__TMU_Set_ERror.htm", "source_topic": "126327_2.htm", "title": "TSER? - (TMU Set ERror)"}`
- title：`TSER? - (TMU Set ERror)`
- 结构段落：['Application', 'Example', 'Functional changes', 'Parameters', 'Syntax']

### 原文开头

```
---
title: "TSER? - (TMU Set ERror)"
source_topic: "126327_2.htm"
source_html: "02_System_reference/02.06_Command_Reference/02.06.13.02.03_TSER__-__TMU_Set_ERror.htm"
---
# TSER? - (TMU Set ERror)

The TSER? query returns possible errors that have occurred during the last TMU measurement.

With this command you can retrieve site specific information (only one site can be in focus at a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools. Also, any firmware queries report setup and results for the site currently in focus only.

## Syntax

```
TSER? {(pinlist)}
```

returns:

```
TSER {VDL_OVERRUN|ARM_OVERRUN|OUT_OF_MEMORY|GLITCH_OVERRUN|NOT_FINISHED}, {(pinlist)}
```

## Parameters

 |

VDL_OVERRUN
```

### 抽取的标题

- L6 `# TSER? - (TMU Set ERror)`
- L12 `## Syntax`
- L24 `## Parameters`
- L81 `## Application`
- L85 `## Example`
- L92 `## Functional changes`

### 抽取的边（1 条，显示前 10）

- L59 → `02_System_reference/02.06_Command_Reference/02.06.13.01.05_Dealing_with_very_high_data_rates.md`
  - 语境：An event that should appear in the prescaler output occurs before the positive pulse representing the previous such event is terminated. See [Dealing with very high frequencies](<02.06.13.01.05_Dealing_with_very_high_data_rates.md>).

### 抽取的段落

- `Syntax`（syntax，L12，130 字符）
  - 开头：'```\nTSER? {(pinlist)}\n```\n\nreturns:\n\n```\nTSER {VDL_OVERRUN|ARM_OVERRUN|OUT_OF_MEMORY|GLITCH_OVERRUN|NOT_FINISHED}, {(pin'
- `Parameters`（syntax，L24，689 字符）
  - 开头：'|\n\nVDL_OVERRUN\n\n |\n\nThe sample rate of the TMU is exceeded.\n\n |\n |\n\nARM_OVERRUN\n\n |\n\nThe TMU is re-armed before all the '
- `Application`（concept，L81，25 字符）
  - 开头：'TMU per pin measurements.'
- `Example`（syntax，L85，48 字符）
  - 开头：'```\n> TSER? (Pin1)\n< TSER ARM_OVERRUN,(Pin1)\n```'
- `Functional changes`（version，L92，30 字符）
  - 开头：'- Introduced in SmarTest 7.1.0'

---

## `02_System_reference/02.07_Test_Method_Reference/02.07.02.13.02_OptionList.md`

*抽样理由：出度中位 2*

- 字节 1825 / 标题 4 / 出度 2 / 代码块 1
- frontmatter：`{"source_html": "02_System_reference/02.07_Test_Method_Reference/02.07.02.13.02_OptionList.htm", "source_topic": "146206.htm", "title": "OptionList"}`
- title：`OptionList`
- 结构段落：['Example', 'Functional changes', 'Related information']

### 原文开头

```
---
title: "OptionList"
source_topic: "146206.htm"
source_html: "02_System_reference/02.07_Test_Method_Reference/02.07.02.13.02_OptionList.htm"
---
# OptionList

This parameter type provides the functionality to enter multiple options as the value of a parameter in this type.

It defines a vector containing string elements. Vector is a standard C++ container. A OptionList variable can be processed with all the member functions of a vector. With these member functions you can query the capacity, access the elements and modify the elements of the vectors. You can find all the member functions of the vector here http://www.cplusplus.com/reference/stl/vector/.

To enter multiple options as the value for the test method parameter in this type, key in the options in the test suite Properties view and separate the options only with a comma.

 ![OptionList usage](<../../../../raw/146207.png>)

## Example

```
class TryOptionList: public testmethod::TestMethod {
protected:
  vector< std::string >  mOpt1;
protected:
  virtual void initialize()
  {
    addParameter("opt1",
                 "OptionList",
                 &mOpt1,
                 testmethod::TM_PARAMETER_INPUT)
```

### 抽取的标题

- L6 `# OptionList`
- L16 `## Example`
- L47 `## Related information`
- L51 `## Functional changes`

### 抽取的边（2 条，显示前 10）

- L49 → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.03_addParameter.md`
  - 语境：[addParameter](<02.07.04.01.03_addParameter.md>)[How to create a universal test method class](<02.07.02.02.02_How_to_create_a_universal_test_method_class.md>)
- L49 → `02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md`
  - 语境：[addParameter](<02.07.04.01.03_addParameter.md>)[How to create a universal test method class](<02.07.02.02.02_How_to_create_a_universal_test_method_class.md>)

### 抽取的段落

- `Example`（syntax，L16，621 字符）
  - 开头：'```\nclass TryOptionList: public testmethod::TestMethod {\nprotected:\n  vector< std::string >  mOpt1;\nprotected:\n  virtual'
- `Related information`（related，L47，158 字符）
  - 开头：'[addParameter](<02.07.04.01.03_addParameter.md>)[How to create a universal test method class](<02.07.02.02.02_How_to_cre'
- `Functional changes`（version，L51，30 字符）
  - 开头：'- Introduced in SmarTest 7.2.0'

---

## `02_System_reference/02.07_Test_Method_Reference/02.07.03.04.04_FS_Gain___LSB_Gain.md`

*抽样理由：补齐（全库等距，非随机）*

- 字节 1258 / 标题 1 / 出度 0 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.07_Test_Method_Reference/02.07.03.04.04_FS_Gain___LSB_Gain.htm", "source_topic": "26088.htm", "title": "FS Gain / LSB Gain"}`
- title：`FS Gain / LSB Gain`
- 结构段落：（无）

### 原文开头

```
---
title: "FS Gain / LSB Gain"
source_topic: "26088.htm"
source_html: "02_System_reference/02.07_Test_Method_Reference/02.07.03.04.04_FS_Gain___LSB_Gain.htm"
---
# FS Gain / LSB Gain

To calculate FS Gain and LSB Gain the following formulas are used:

 |

Unit

 |

FS_GAIN

 |

LSB_GAIN

 |
 |

mV

 |

```

### 抽取的标题

- L6 `# FS Gain / LSB Gain`

### 抽取的边（0 条，显示前 10）


---

## `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.22.08_EVENT_VCVM.getOutOfRangeCheck.md`

*抽样理由：补齐（全库等距，非随机）*

- 字节 1233 / 标题 5 / 出度 4 / 代码块 1
- frontmatter：`{"source_html": "02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.22.08_EVENT_VCVM.getOutOfRangeCheck.htm", "source_topic": "150313.htm", "title": "EVENT_VCVM.getOutOfRangeCheck()"}`
- title：`EVENT_VCVM.getOutOfRangeCheck()`
- 结构段落：['Example', 'Functional changes', 'Related information', 'Syntax']

### 原文开头

```
---
title: "EVENT_VCVM.getOutOfRangeCheck()"
source_topic: "150313.htm"
source_html: "02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.22.08_EVENT_VCVM.getOutOfRangeCheck.htm"
---
# EVENT_VCVM.getOutOfRangeCheck()

Reads the state of the out-of-range check that has been defined by [EVENT_VCVM.outOfRangeCheck()](<02.07.04.01.63.22.07_EVENT_VCVM.outOfRangeCheck.md>).

The state is read from the corresponding [EVENT_VCVM](<02.07.04.01.63.22_EVENT_VCVM.md>) object and returned as a bool value.

This member function is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/Events.h.

## Syntax

```
void getOutOfRangeCheck(bool & failOnOutOfRange) const;
```

Parameter
 | Parameter  | Description |
 | failOnOutOfRange |

The programmed value true or false of the out-of-range check.

- true: The out-of-range check is enabled
- false: The out-of-range check is disabled
 |
```

### 抽取的标题

- L6 `# EVENT_VCVM.getOutOfRangeCheck()`
- L14 `## Syntax`
- L34 `## Example`
- L38 `## Related information`
- L42 `## Functional changes`

### 抽取的边（4 条，显示前 10）

- L8 → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.22.07_EVENT_VCVM.outOfRangeCheck.md`
  - 语境：Reads the state of the out-of-range check that has been defined by [EVENT_VCVM.outOfRangeCheck()](<02.07.04.01.63.22.07_EVENT_VCVM.outOfRangeCheck.md>).
- L10 → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.22_EVENT_VCVM.md`
  - 语境：The state is read from the corresponding [EVENT_VCVM](<02.07.04.01.63.22_EVENT_VCVM.md>) object and returned as a bool value.
- L36 → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.22_EVENT_VCVM.md`
  - 语境：For an example see [EVENT_VCVM](<02.07.04.01.63.22_EVENT_VCVM.md>).
- L40 → `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.22.07_EVENT_VCVM.outOfRangeCheck.md`
  - 语境：[EVENT_VCVM.outOfRangeCheck()](<02.07.04.01.63.22.07_EVENT_VCVM.outOfRangeCheck.md>)

### 抽取的段落

- `Syntax`（syntax，L14，320 字符）
  - 开头：'```\nvoid getOutOfRangeCheck(bool & failOnOutOfRange) const;\n```\n\nParameter\n | Parameter  | Description |\n | failOnOutOfR'
- `Example`（syntax，L34，67 字符）
  - 开头：'For an example see [EVENT_VCVM](<02.07.04.01.63.22_EVENT_VCVM.md>).'
- `Related information`（related，L38，84 字符）
  - 开头：'[EVENT_VCVM.outOfRangeCheck()](<02.07.04.01.63.22.07_EVENT_VCVM.outOfRangeCheck.md>)'
- `Functional changes`（version，L42，30 字符）
  - 开头：'- Introduced in SmarTest 7.4.0'

---

## `02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.03_resolution.md`

*抽样理由：02_System_reference 中位*

- 字节 1234 / 标题 4 / 出度 1 / 代码块 2
- frontmatter：`{"source_html": "02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.03_resolution.htm", "source_topic": "149534.htm", "title": "resolution()"}`
- title：`resolution()`
- 结构段落：['Example', 'Functional changes', 'Syntax']

### 原文开头

```
---
title: "resolution()"
source_topic: "149534.htm"
source_html: "02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.03_resolution.htm"
---
# resolution()

This function specifies a value that represents the resolution between steps in cogo searches. For a binary search, it equals the value of the width between the two final steps; for a linear search, it equals a step width. See [Sequencer-controlled searching with cogo](<02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md>) for more information about `resolution()` and `step()`.

## Syntax

```
resolution(double dRes)
```

List of parameters
 |

Parameter

 |

Description

 |
 |

dRes
```

### 抽取的标题

- L6 `# resolution()`
- L10 `## Syntax`
- L38 `## Example`
- L52 `## Functional changes`

### 抽取的边（1 条，显示前 10）

- L8 → `02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md`
  - 语境：This function specifies a value that represents the resolution between steps in cogo searches. For a binary search, it equals the value of the width between the two final steps; for a linear search, it equals a step width. See [Sequencer-controlled searching with cogo](<02.07.13.19.02_Sequencer-cont

### 抽取的段落

- `Syntax`（syntax，L10，200 字符）
  - 开头：'```\nresolution(double dRes)\n```\n\nList of parameters\n |\n\nParameter\n\n |\n\nDescription\n\n |\n |\n\ndRes\n\n |\n\nFor a binary search'
- `Example`（syntax，L38，341 字符）
  - 开头：'```\nRDI_BEGIN();\n\n  rdi.cogo("bin_vf_r").search(TA::BINARY).pathPin("DATA9").start(0).stop(3).init(1.5).resolution(0.375'
- `Functional changes`（version，L52，30 字符）
  - 开头：'- Introduced in SmartRDI 2.4.0'

---

## `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.01_Sorting_tables.md`

*抽样理由：补齐（全库等距，非随机）*

- 字节 3552 / 标题 10 / 出度 11 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.01_Sorting_tables.htm", "source_topic": "137055.htm", "title": "Sorting tables"}`
- title：`Sorting tables`
- 结构段落：['About this task', 'Before you begin', 'Examples', 'Functional changes', 'Procedure', 'Related information']

### 原文开头

```
---
title: "Sorting tables"
source_topic: "137055.htm"
source_html: "02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.01_Sorting_tables.htm"
---
# Sorting tables

Tables in the [Data navigation views](<02.08.04.13.03.02_Data_navigation_views.md>) and [Detail data views](<02.08.04.13.03.03_Detail_data_views.md>) can be sorted by clicking a column title.

## About this task

Sort a table to find rows with entries of a particular size in a column or to see all entries together that have similar values in a column (for example, all test with the same name).

Sorting a data navigation view has no effect on the [Analysis views](<02.08.04.13.03.04_Analysis_views.md>).

## Before you begin

- Open the [data navigation view](<02.08.04.13.03.02_Data_navigation_views.md>) or [detail data view](<02.08.04.13.03.03_Detail_data_views.md>) that you want to sort.
- In a data navigation view, open that tab that you want to sort.

## Procedure

- In the table that you want to sort, click the title of the column by which you want to sort.

For example, to sort a test summary tab by the number of failed devices, click the F# column title.

The table is sorted by this column in ascending order; that is, the rows with the smallest values in this column appear at the top of the table. The sorting order is indicated by a triangle ![Data log summary view_Ascending triangle](<../../../../raw/136425.png>) in the column title.

```

### 抽取的标题

- L6 `# Sorting tables`
- L10 `## About this task`
- L16 `## Before you begin`
- L21 `## Procedure`
- L39 `## Results`
- L43 `## Examples`
- L45 `### Sorting by one column`
- L51 `### Sorting by multiple columns`
- L59 `## Related information`
- L63 `## Functional changes`

### 抽取的边（11 条，显示前 10）

- L8 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.md`
  - 语境：Tables in the [Data navigation views](<02.08.04.13.03.02_Data_navigation_views.md>) and [Detail data views](<02.08.04.13.03.03_Detail_data_views.md>) can be sorted by clicking a column title.
- L8 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03_Detail_data_views.md`
  - 语境：Tables in the [Data navigation views](<02.08.04.13.03.02_Data_navigation_views.md>) and [Detail data views](<02.08.04.13.03.03_Detail_data_views.md>) can be sorted by clicking a column title.
- L14 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.04_Analysis_views.md`
  - 语境：Sorting a data navigation view has no effect on the [Analysis views](<02.08.04.13.03.04_Analysis_views.md>).
- L18 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.md`
  - 语境：Open the [data navigation view](<02.08.04.13.03.02_Data_navigation_views.md>) or [detail data view](<02.08.04.13.03.03_Detail_data_views.md>) that you want to sort.
- L18 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03_Detail_data_views.md`
  - 语境：Open the [data navigation view](<02.08.04.13.03.02_Data_navigation_views.md>) or [detail data view](<02.08.04.13.03.03_Detail_data_views.md>) that you want to sort.
- L37 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.04.07_Protocol_Monitor_view.md`
  - 语境：For the [Protocol Monitor view](<02.08.04.13.03.04.07_Protocol_Monitor_view.md>) only: If you want to sort by additional columns, repeat steps 1 through 3 for these columns.
- L61 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.02_Filtering_test_result_data.md`
  - 语境：[Filtering test result data](<02.08.04.13.02.03.02_Filtering_test_result_data.md>)[Highlighting specific data](<02.08.04.13.02.03.03_Highlighting_specific_data.md>)[Selecting similar data](<02.08.04.13.02.03.04_Selecting_similar_data.md>)[Separating summary results by wafer, site, or pin](<02.08.04.
- L61 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.03_Highlighting_specific_data.md`
  - 语境：[Filtering test result data](<02.08.04.13.02.03.02_Filtering_test_result_data.md>)[Highlighting specific data](<02.08.04.13.02.03.03_Highlighting_specific_data.md>)[Selecting similar data](<02.08.04.13.02.03.04_Selecting_similar_data.md>)[Separating summary results by wafer, site, or pin](<02.08.04.
- L61 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.04_Selecting_similar_data.md`
  - 语境：[Filtering test result data](<02.08.04.13.02.03.02_Filtering_test_result_data.md>)[Highlighting specific data](<02.08.04.13.02.03.03_Highlighting_specific_data.md>)[Selecting similar data](<02.08.04.13.02.03.04_Selecting_similar_data.md>)[Separating summary results by wafer, site, or pin](<02.08.04.
- L61 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.05_Separating_summary_results_by_wafer__site__or_pin.md`
  - 语境：[Filtering test result data](<02.08.04.13.02.03.02_Filtering_test_result_data.md>)[Highlighting specific data](<02.08.04.13.02.03.03_Highlighting_specific_data.md>)[Selecting similar data](<02.08.04.13.02.03.04_Selecting_similar_data.md>)[Separating summary results by wafer, site, or pin](<02.08.04.

### 抽取的段落

- `About this task`（procedure，L10，293 字符）
  - 开头：'Sort a table to find rows with entries of a particular size in a column or to see all entries together that have similar'
- `Before you begin`（constraint，L16，232 字符）
  - 开头：'- Open the [data navigation view](<02.08.04.13.03.02_Data_navigation_views.md>) or [detail data view](<02.08.04.13.03.03'
- `Procedure`（procedure，L21，1099 字符）
  - 开头：'- In the table that you want to sort, click the title of the column by which you want to sort.\n\nFor example, to sort a t'
- `Examples`（syntax，L43，638 字符）
  - 开头：'### Sorting by one column\n\nClicking the title of the Max column twice sorts the table in descending order by that column'
- `Related information`（related，L59，435 字符）
  - 开头：'[Filtering test result data](<02.08.04.13.02.03.02_Filtering_test_result_data.md>)[Highlighting specific data](<02.08.04'
- `Functional changes`（version，L63，137 字符）
  - 开头：'- Introduced in SmarTest 7.2.0\n- SmarTest 7.2.1: Added sorting of detail data views.\n- SmarTest 7.3.2: Added sorting by '

---

## `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.35.01.05_Resizing_the_Wafer_Map_Geometry.md`

*抽样理由：体积下四分位 1002B*

- 字节 1002 / 标题 2 / 出度 0 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.35.01.05_Resizing_the_Wafer_Map_Geometry.htm", "source_topic": "43074.htm", "title": "Resizing the Wafer Map Geometry"}`
- title：`Resizing the Wafer Map Geometry`
- 结构段落：['Procedure']

### 原文开头

```
---
title: "Resizing the Wafer Map Geometry"
source_topic: "43074.htm"
source_html: "02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.35.01.05_Resizing_the_Wafer_Map_Geometry.htm"
---
# Resizing the Wafer Map Geometry

You can resize the wafer map editor in the following two ways.

## Procedure

-  To double the size of the wafer map geometory, click Display > Double Size in the Wafer Description Editor.
-  To manually define the size of the wafer map geometory,

  -  click the X in the upper left of the wafer map editor and select Advanced > Special Window Settings. The Edit Window-Specific Settings-Kwin dialog pops up.  ![Wafer Description Editor](<../../../../raw/137565.png>)
  -  In the Geometory tab, check the box before size, select Force from the list and then enter the size you want to have. The scaled values you enter should have roughly the same aspect ratio with the default value.   ![edit window-specific settings - kwin](<../../../../raw/137566.png>)

```

### 抽取的标题

- L6 `# Resizing the Wafer Map Geometry`
- L10 `## Procedure`

### 抽取的边（0 条，显示前 10）


### 抽取的段落

- `Procedure`（procedure，L10，679 字符）
  - 开头：'-  To double the size of the wafer map geometory, click Display > Double Size in the Wafer Description Editor.\n-  To man'

---

## `02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.01.01_Parameters_for_log_file_generation.md`

*抽样理由：补齐（全库等距，非随机）*

- 字节 461 / 标题 1 / 出度 0 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.01.01_Parameters_for_log_file_generation.htm", "source_topic": "69262.htm", "title": "Parameters for log file generation"}`
- title：`Parameters for log file generation`
- 结构段落：（无）

### 原文开头

```
---
title: "Parameters for log file generation"
source_topic: "69262.htm"
source_html: "02_System_reference/02.09_Test_Program_Management/02.09.01.03.04.01.01.01_Parameters_for_log_file_generation.htm"
---
# Parameters for log file generation

You can change the following parameters to increase the debug level and read the generated error messages:

- debug_level
- driver_error_log
- driver_message_log
- log_files_to_keep
- trace_driver_calls

```

### 抽取的标题

- L6 `# Parameters for log file generation`

### 抽取的边（0 条，显示前 10）


---

## `02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.01_FLEXLM_LICENSE_REQUEST_STARTED.md`

*抽样理由：含 Dependency*

- 字节 1332 / 标题 4 / 出度 2 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.01_FLEXLM_LICENSE_REQUEST_STARTED.htm", "source_topic": "119315.htm", "title": "FLEXLM_LICENSE_REQUEST_STARTED"}`
- title：`FLEXLM_LICENSE_REQUEST_STARTED`
- 结构段落：['Dependency', 'Functional changes', 'Related information']

### 原文开头

```
---
title: "FLEXLM_LICENSE_REQUEST_STARTED"
source_topic: "119315.htm"
source_html: "02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.01_FLEXLM_LICENSE_REQUEST_STARTED.htm"
---
# FLEXLM_LICENSE_REQUEST_STARTED

This asynchronous event indicates the start of the FlexLM licenses request. It is received after the `DEVICE_CHANGE_COMPLETED` event.

## Dependency

Changing device is performed.

Parameter
 |

I/O

 |

Parameter

 |

Description

 |
 |
```

### 抽取的标题

- L6 `# FLEXLM_LICENSE_REQUEST_STARTED`
- L10 `## Dependency`
- L91 `## Related information`
- L95 `## Functional changes`

### 抽取的边（2 条，显示前 10）

- L93 → `02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.03_GetFlexLMLicenseState.md`
  - 语境：[GetFlexLMLicenseState](<02.09.01.10.03.02.01.03_GetFlexLMLicenseState.md>)[FLEXLM_LICENSE_REQUEST_COMPLETED](<02.09.01.10.03.02.01.02_FLEXLM_LICENSE_REQUEST_COMPLETED.md>)
- L93 → `02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.02_FLEXLM_LICENSE_REQUEST_COMPLETED.md`
  - 语境：[GetFlexLMLicenseState](<02.09.01.10.03.02.01.03_GetFlexLMLicenseState.md>)[FLEXLM_LICENSE_REQUEST_COMPLETED](<02.09.01.10.03.02.01.02_FLEXLM_LICENSE_REQUEST_COMPLETED.md>)

### 抽取的段落

- `Dependency`（constraint，L10，598 字符）
  - 开头：'Changing device is performed.\n\nParameter\n |\n\nI/O\n\n |\n\nParameter\n\n |\n\nDescription\n\n |\n |\n\nO\n\n |\n\nSESSION_ID\n\n |\n\nthe ID o'
- `Related information`（related，L91，172 字符）
  - 开头：'[GetFlexLMLicenseState](<02.09.01.10.03.02.01.03_GetFlexLMLicenseState.md>)[FLEXLM_LICENSE_REQUEST_COMPLETED](<02.09.01.'
- `Functional changes`（version，L95，30 字符）
  - 开头：'- Introduced in SmarTest 6.5.3'

---

## `02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.02_FLEXLM_LICENSE_REQUEST_COMPLETED.md`

*抽样理由：含 Dependency*

- 字节 2136 / 标题 4 / 出度 2 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.02_FLEXLM_LICENSE_REQUEST_COMPLETED.htm", "source_topic": "119316.htm", "title": "FLEXLM_LICENSE_REQUEST_COMPLETED"}`
- title：`FLEXLM_LICENSE_REQUEST_COMPLETED`
- 结构段落：['Dependency', 'Functional changes', 'Related information']

### 原文开头

```
---
title: "FLEXLM_LICENSE_REQUEST_COMPLETED"
source_topic: "119316.htm"
source_html: "02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.02_FLEXLM_LICENSE_REQUEST_COMPLETED.htm"
---
# FLEXLM_LICENSE_REQUEST_COMPLETED

This asynchronous event indicates that the FlexLM license request is completed. This event is received after the FLEXLM_LICENSE_REQUEST_STARTED event.

The HVM client can get the requested, acquired and missing license information with this event passively. It can get these information with the GetFlexLMLincseState() API actively.

## Dependency

Changing device is performed.

Parameter
 |

I/O

 |

Parameter

 |

Description

```

### 抽取的标题

- L6 `# FLEXLM_LICENSE_REQUEST_COMPLETED`
- L12 `## Dependency`
- L129 `## Related information`
- L133 `## Functional changes`

### 抽取的边（2 条，显示前 10）

- L131 → `02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.03_GetFlexLMLicenseState.md`
  - 语境：[GetFlexLMLicenseState](<02.09.01.10.03.02.01.03_GetFlexLMLicenseState.md>)[FLEXLM_LICENSE_REQUEST_STARTED](<02.09.01.10.03.02.01.01_FLEXLM_LICENSE_REQUEST_STARTED.md>)
- L131 → `02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.01.01_FLEXLM_LICENSE_REQUEST_STARTED.md`
  - 语境：[GetFlexLMLicenseState](<02.09.01.10.03.02.01.03_GetFlexLMLicenseState.md>)[FLEXLM_LICENSE_REQUEST_STARTED](<02.09.01.10.03.02.01.01_FLEXLM_LICENSE_REQUEST_STARTED.md>)

### 抽取的段落

- `Dependency`（constraint，L12，1163 字符）
  - 开头：'Changing device is performed.\n\nParameter\n |\n\nI/O\n\n |\n\nParameter\n\n |\n\nDescription\n\n |\n |\n\nO\n\n |\n\nSESSION_ID\n\n |\n\nThe ID o'
- `Related information`（related，L129，168 字符）
  - 开头：'[GetFlexLMLicenseState](<02.09.01.10.03.02.01.03_GetFlexLMLicenseState.md>)[FLEXLM_LICENSE_REQUEST_STARTED](<02.09.01.10'
- `Functional changes`（version，L133，30 字符）
  - 开头：'- Introduced in SmarTest 6.5.3'

---

## `02_System_reference/02.10_Data_Logging/02.10.01.04.02.98_DRLTestSuiteNameAttr.md`

*抽样理由：补齐（全库等距，非随机）*

- 字节 389 / 标题 2 / 出度 0 / 代码块 1
- frontmatter：`{"source_html": "02_System_reference/02.10_Data_Logging/02.10.01.04.02.98_DRLTestSuiteNameAttr.htm", "source_topic": "34848.htm", "title": "DRLTestSuiteNameAttr"}`
- title：`DRLTestSuiteNameAttr`
- 结构段落：['Functional changes']

### 原文开头

```
---
title: "DRLTestSuiteNameAttr"
source_topic: "34848.htm"
source_html: "02_System_reference/02.10_Data_Logging/02.10.01.04.02.98_DRLTestSuiteNameAttr.htm"
---
# DRLTestSuiteNameAttr

A variable of this type holds the name of a test suite as a NULL terminated string.

```
typedef char *DRLTestSuiteNameAttr;
```

## Functional changes

- Introduced before SmarTest 6.3.2

```

### 抽取的标题

- L6 `# DRLTestSuiteNameAttr`
- L14 `## Functional changes`

### 抽取的边（0 条，显示前 10）


### 抽取的段落

- `Functional changes`（version，L14，34 字符）
  - 开头：'- Introduced before SmarTest 6.3.2'

---

## `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.13_Running_MTP_testflows_with_MTP-EWC.md`

*抽样理由：体积上四分位 3211B*

- 字节 3211 / 标题 7 / 出度 8 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.13_Running_MTP_testflows_with_MTP-EWC.htm", "source_topic": "140721.htm", "title": "Running MTP testflows with MTP-EWC"}`
- title：`Running MTP testflows with MTP-EWC`
- 结构段落：['About this task', 'Before you begin', 'Functional changes', 'Procedure', 'Related information']

### 原文开头

```
---
title: "Running MTP testflows with MTP-EWC"
source_topic: "140721.htm"
source_html: "02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.13_Running_MTP_testflows_with_MTP-EWC.htm"
---
# Running MTP testflows with MTP-EWC

To run MTP testflows with the [MTP-EWC](<02.12.04.02_MTP-EWC.md>) (SmarTest Work Center), open the Testflow (MTP) page to set up run configurations and run.

## About this task

Note Do not use the Run Testflow or Run Selected commands to run MTP tests, because the system will not load vector files, pattern master files and modified timing files for the execution, and will not provide an automatic build for the MTP .apg files.Note To learn the other features on MTP-EWC, see [MTP-EWC](<02.12.04.02_MTP-EWC.md>).

## Before you begin

Make sure:

- MTP software is installed.
- An MTP testflow is loaded and open.

## Procedure

-  From the menu bar of SmarTest, select Run > Run Configurations....

The Run Configuration window opens.

-  In this window, from the left navigation panel, expand Testflow (MTP) and select a configuration, for example, Testflow (MTP) (the default configuration).

```

### 抽取的标题

- L6 `# Running MTP testflows with MTP-EWC`
- L10 `## About this task`
- L14 `## Before you begin`
- L21 `## Procedure`
- L55 `## Results`
- L59 `## Related information`
- L63 `## Functional changes`

### 抽取的边（8 条，显示前 10）

- L8 → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02_MTP-EWC.md`
  - 语境：To run MTP testflows with the [MTP-EWC](<02.12.04.02_MTP-EWC.md>) (SmarTest Work Center), open the Testflow (MTP) page to set up run configurations and run.
- L12 → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02_MTP-EWC.md`
  - 语境：Note Do not use the Run Testflow or Run Selected commands to run MTP tests, because the system will not load vector files, pattern master files and modified timing files for the execution, and will not provide an automatic build for the MTP .apg files.Note To learn the other features on MTP-EWC, see
- L39 → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.12.02_The_MTP_build_configuration_pages.md`
  - 语境：You can select any available [build configuration](<02.12.02.05.12.02_The_MTP_build_configuration_pages.md>) for the automatic build. The default configuration is the active build configuration.
- L47 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md`
  - 语境：Here, you can select a testflow and set the execution scope for the testflow. For details, see "To run a user-defined testflow" in [Running a testflow](<../02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md>).
- L51 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.05_Adding_user_defined_testflows_to_the_Run_menu.md`
  - 语境：Here, you can add your run configurations to the Run menu. For details, see [Adding user defined testflows to the Run menu](<../02.08_Setup_and_Result_Tools/02.08.04.32.02.03.05_Adding_user_defined_testflows_to_the_Run_menu.md>).
- L61 → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.12_Building_MTP_files_with_MTP-EWC.md`
  - 语境：[Building MTP files with MTP-EWC](<02.12.02.05.12_Building_MTP_files_with_MTP-EWC.md>)[MTP-EWC](<02.12.04.02_MTP-EWC.md>)[Running a testflow](<../02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md>)
- L61 → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02_MTP-EWC.md`
  - 语境：[Building MTP files with MTP-EWC](<02.12.02.05.12_Building_MTP_files_with_MTP-EWC.md>)[MTP-EWC](<02.12.04.02_MTP-EWC.md>)[Running a testflow](<../02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md>)
- L61 → `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md`
  - 语境：[Building MTP files with MTP-EWC](<02.12.02.05.12_Building_MTP_files_with_MTP-EWC.md>)[MTP-EWC](<02.12.04.02_MTP-EWC.md>)[Running a testflow](<../02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.md>)

### 抽取的段落

- `About this task`（procedure，L10，337 字符）
  - 开头：'Note Do not use the Run Testflow or Run Selected commands to run MTP tests, because the system will not load vector file'
- `Before you begin`（constraint，L14，78 字符）
  - 开头：'Make sure:\n\n- MTP software is installed.\n- An MTP testflow is loaded and open.'
- `Procedure`（procedure，L21，1716 字符）
  - 开头：'-  From the menu bar of SmarTest, select Run > Run Configurations....\n\nThe Run Configuration window opens.\n\n-  In this w'
- `Related information`（related，L59，216 字符）
  - 开头：'[Building MTP files with MTP-EWC](<02.12.02.05.12_Building_MTP_files_with_MTP-EWC.md>)[MTP-EWC](<02.12.04.02_MTP-EWC.md>'
- `Functional changes`（version，L63，199 字符）
  - 开头：'- Introduced in MTP 3.1.1\n- MTP 3.2.1: Changes the name for the MTP testflow run configuration from "MTP Launch" to "Tes'

---

## `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.04.06.03.04_Parameters_for_the_DataTraining_test_method.md`

*抽样理由：补齐（全库等距，非随机）*

- 字节 3202 / 标题 3 / 出度 1 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.04.06.03.04_Parameters_for_the_DataTraining_test_method.htm", "source_topic": "99475_2.htm", "title": "Parameters for the DataTraining test method"}`
- title：`Parameters for the DataTraining test method`
- 结构段落：['Functional changes', 'Related information']

### 原文开头

```
---
title: "Parameters for the DataTraining test method"
source_topic: "99475_2.htm"
source_html: "02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.04.06.03.04_Parameters_for_the_DataTraining_test_method.htm"
---
# Parameters for the DataTraining test method

These tables describe all parameters for the DataTraining testmethod.

DataTraining test method parameters
 |

Name

 |

Comment

 |
 |

TrainingAlgorithm

 |

SpecTraining or EmbeddedTraining

SpecTraining performs the search for the on the test controller workstation as a parallel spec search.
```

### 抽取的标题

- L6 `# Parameters for the DataTraining test method`
- L144 `## Related information`
- L148 `## Functional changes`

### 抽取的边（1 条，显示前 10）

- L146 → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.03.01_Data_training_concept.md`
  - 语境：[Data training concept](<02.12.02.05.06.06.03.01_Data_training_concept.md>)

### 抽取的段落

- `Related information`（related，L144，75 字符）
  - 开头：'[Data training concept](<02.12.02.05.06.06.03.01_Data_training_concept.md>)'
- `Functional changes`（version，L148，79 字符）
  - 开头：'- Introduced before SmarTest 6.3.2\n- MTP 3.0.1: New parameter TrainingAlgorithm'

---

## `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md`

*抽样理由：解析异常 no_h1*

- 字节 5595 / 标题 2 / 出度 14 / 代码块 4
- frontmatter：`{"source_html": "02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.html", "source_topic": "group__openclose.html", "title": "Opening and closing connections"}`
- title：`None`
- 结构段落：（无）
- ⚠️ 解析异常：[{'detail': '', 'doc': '02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md', 'kind': 'no_h1'}]

### 原文开头

```
---
title: "Opening and closing connections"
source_topic: "group__openclose.html"
source_html: "02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.html"
---
|Reference 254242   ![mag_sel.png](<../../../../raw/254242-search/mag_sel.png>)   [![close.png](<../../../../raw/254242-search/close.png>)](<javascript:searchBox.CloseResultsWindow()>)             Opening and closing connections

| [](<>) Functions |
| IDID  | [gio_open](<02.13.07.01_Opening_and_closing_connections.md#gaddc8671fd089529c77794f0d38603fca>) (const char *pName)Open an interface or device. |
| IDID  | [gio_get_interface](<02.13.07.01_Opening_and_closing_connections.md#ga267c08ba41cc3d2f3662b27683687615>) (IDID id)Return an interface ID referring to the interface associated with the given device ID. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_close](<02.13.07.01_Opening_and_closing_connections.md#gaa2ca178dbd1f7b8435e3c1c6e34f1605>) (IDID id)Close an interface or device. |
| const char *  | [gio_get_name](<02.13.07.01_Opening_and_closing_connections.md#ga71dcdd2c63203488d9f9413a75a98c71>) (IDID id)Return the name of an interface or device (for diagnostic purposes).  |  [](<>)

## Detailed Description

## Function Documentation

 [](<>)

 | [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>) gio_close   | (  | IDID   | id | )  | |

Close an interface or device.

This function shuts down a connection opened by `[gio_open()](<02.13.07.01_Opening_and_closing_connections.md#gaddc8671fd089529c77794f0d38603fca>)`; after it returns, the `IDID` passed to it must no longer be used.

 ReturnsGIO_ERROR  Return values

| GIO_ERR_NO_ERROR | Operation successfully completed. |
```

### 抽取的标题

- L14 `## Detailed Description`
- L16 `## Function Documentation`

### 抽取的边（14 条，显示前 10）

- L9 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md`
  - 语境：| IDID | [gio_open](<02.13.07.01_Opening_and_closing_connections.md#gaddc8671fd089529c77794f0d38603fca>) (const char pName)Open an interface or device. |
- L10 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md`
  - 语境：| IDID | [gio_get_interface](<02.13.07.01_Opening_and_closing_connections.md#ga267c08ba41cc3d2f3662b27683687615>) (IDID id)Return an interface ID referring to the interface associated with the given device ID. |
- L11 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.07_Error_handling.md`
  - 语境：| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>) | [gio_close](<02.13.07.01_Opening_and_closing_connections.md#gaa2ca178dbd1f7b8435e3c1c6e34f1605>) (IDID id)Close an interface or device. |
- L11 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md`
  - 语境：| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>) | [gio_close](<02.13.07.01_Opening_and_closing_connections.md#gaa2ca178dbd1f7b8435e3c1c6e34f1605>) (IDID id)Close an interface or device. |
- L12 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md`
  - 语境：| const char | [gio_get_name](<02.13.07.01_Opening_and_closing_connections.md#ga71dcdd2c63203488d9f9413a75a98c71>) (IDID id)Return the name of an interface or device (for diagnostic purposes). | [](<>)
- L20 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.07_Error_handling.md`
  - 语境：| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>) gio_close | ( | IDID | id | ) | |
- L24 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md` `[代码跨度]`
  - 语境：This function shuts down a connection opened by [gio_open()](<02.13.07.01_Opening_and_closing_connections.md#gaddc8671fd089529c77794f0d38603fca>); after it returns, the IDID passed to it must no longer be used.
- L37 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md` `[代码跨度]`
  - 语境：Some of the functions in the GIO layer do not work given an IDID which refers to a device session. Instead of always opening separate interface and device sessions, a client application can use [gio_get_interface()](<02.13.07.01_Opening_and_closing_connections.md#ga267c08ba41cc3d2f3662b27683687615>)
- L39 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md` `[代码跨度]`
  - 语境：Attention[gio_get_interface()](<02.13.07.01_Opening_and_closing_connections.md#ga267c08ba41cc3d2f3662b27683687615>) can return identical IDIDs when called for different devices connected to the same interface. Client applications should not call [gio_close()](<02.13.07.01_Opening_and_closing_connect
- L39 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.01_Opening_and_closing_connections.md` `[代码跨度]`
  - 语境：Attention[gio_get_interface()](<02.13.07.01_Opening_and_closing_connections.md#ga267c08ba41cc3d2f3662b27683687615>) can return identical IDIDs when called for different devices connected to the same interface. Client applications should not call [gio_close()](<02.13.07.01_Opening_and_closing_connect

---

## `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md`

*抽样理由：解析异常 no_h1*

- 字节 13436 / 标题 3 / 出度 51 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.html", "source_topic": "group__misc.html", "title": "Operations applicable to diverse interface or device types"}`
- title：`None`
- 结构段落：（无）
- ⚠️ 解析异常：[{'detail': '', 'doc': '02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md', 'kind': 'no_h1'}]

### 原文开头

```
---
title: "Operations applicable to diverse interface or device types"
source_topic: "group__misc.html"
source_html: "02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.html"
---
|Reference 254242   ![mag_sel.png](<../../../../raw/254242-search/mag_sel.png>)   [![close.png](<../../../../raw/254242-search/close.png>)](<javascript:searchBox.CloseResultsWindow()>)             Operations applicable to diverse interface or device types

| [](<>) Enumerations |
| enum  | [GIO_REASON](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga8b9bd2c914b4a1ff993930771eb7a772>) { [GIO_REASON_REQCNT](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gga8b9bd2c914b4a1ff993930771eb7a772ac9a1942570c2d6653a6f4cc408d8c6dc>) = 1 << 0, [GIO_REASON_CHR](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gga8b9bd2c914b4a1ff993930771eb7a772aba1bcc5a063435d9bbf01f251acc55fb>) = 1 << 1, [GIO_REASON_END](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gga8b9bd2c914b4a1ff993930771eb7a772a4887af887198a9cccc6d21b334306ea5>) = 1 << 2 }
|   | Reasons for returning from a read request. [More...](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga8b9bd2c914b4a1ff993930771eb7a772>)
 | |

| [](<>) Functions |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_clear](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga3ffa3bd02beca7fc651b3eeb0f82d86c>) (IDID id)Clear an interface or device. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_write](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga91862461d833db0642f79f0410c33468>) (IDID id, const void *pBuffer, size_t len, bool_t end, size_t *pActual)Write data. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_read](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gac927c44b656660a6150cd7564b98f13c>) (IDID id, void *pBuffer, size_t len, int *pReasons, size_t *pActual)Read data. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_read_status_byte](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga02d19585c20ed08fc4071d0e9b1b78e4>) (IDID id, uint8_t *pStb)Read status byte. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_set_status_byte](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga0568b46d55d49fca982038493e9d9c19>) (IDID id, uint8_t stb)Set status byte. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_trigger](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gaa160b98845cb8eed252651b9a2407823>) (IDID id)Trigger device(s). |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_local](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gac3440bc0888fd578f7acbe148e4aa847>) (IDID id)Switch device to local operation. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_remote](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gaad13df2866d8e8536c16ea80f3d89cc8>) (IDID id)Switch device to remote operation. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_lock](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga281f1e0664bd2ea69456e1f38bc93b61>) (IDID id)Lock an interface or device. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_unlock](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gaec1fd6f26e13a0c20d1311c6f8a1811f>) (IDID id)Unlock an interface or device.  |  [](<>)

## Detailed Description

## Enumeration Type Documentation

```

### 抽取的标题

- L25 `## Detailed Description`
- L27 `## Enumeration Type Documentation`
- L54 `## Function Documentation`

### 抽取的边（51 条，显示前 10）

- L9 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md`
  - 语境：| enum | [GIO_REASON](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga8b9bd2c914b4a1ff993930771eb7a772>) { [GIO_REASON_REQCNT](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gga8b9bd2c914b4a1ff993930771eb7a772ac9a1942570c2d6653a6f4cc408d8c6dc>
- L9 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md`
  - 语境：| enum | [GIO_REASON](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga8b9bd2c914b4a1ff993930771eb7a772>) { [GIO_REASON_REQCNT](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gga8b9bd2c914b4a1ff993930771eb7a772ac9a1942570c2d6653a6f4cc408d8c6dc>
- L9 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md`
  - 语境：| enum | [GIO_REASON](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga8b9bd2c914b4a1ff993930771eb7a772>) { [GIO_REASON_REQCNT](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gga8b9bd2c914b4a1ff993930771eb7a772ac9a1942570c2d6653a6f4cc408d8c6dc>
- L9 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md`
  - 语境：| enum | [GIO_REASON](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga8b9bd2c914b4a1ff993930771eb7a772>) { [GIO_REASON_REQCNT](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gga8b9bd2c914b4a1ff993930771eb7a772ac9a1942570c2d6653a6f4cc408d8c6dc>
- L10 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md`
  - 语境：| | Reasons for returning from a read request. [More...](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga8b9bd2c914b4a1ff993930771eb7a772>)
- L14 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.07_Error_handling.md`
  - 语境：| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>) | [gio_clear](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga3ffa3bd02beca7fc651b3eeb0f82d86c>) (IDID id)Clear an interface or device. |
- L14 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md`
  - 语境：| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>) | [gio_clear](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga3ffa3bd02beca7fc651b3eeb0f82d86c>) (IDID id)Clear an interface or device. |
- L15 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.07_Error_handling.md`
  - 语境：| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>) | [gio_write](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga91862461d833db0642f79f0410c33468>) (IDID id, const void pBuffer, size_t len, bool_t end, size_t pActual)Write data. |
- L15 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md`
  - 语境：| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>) | [gio_write](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#ga91862461d833db0642f79f0410c33468>) (IDID id, const void pBuffer, size_t len, bool_t end, size_t pActual)Write data. |
- L16 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.07_Error_handling.md`
  - 语境：| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>) | [gio_read](<02.13.07.02_Operations_applicable_to_diverse_interface_or_device_types.md#gac927c44b656660a6150cd7564b98f13c>) (IDID id, void pBuffer, size_t len, int pReasons, size_t pActual)Read data. |

---

## `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`

*抽样理由：解析异常 no_h1*

- 字节 8888 / 标题 3 / 出度 34 / 代码块 0
- frontmatter：`{"source_html": "02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.html", "source_topic": "group__gpib.html", "title": "Operations specific to GPIB devices"}`
- title：`None`
- 结构段落：（无）
- ⚠️ 解析异常：[{'detail': '', 'doc': '02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md', 'kind': 'no_h1'}]

### 原文开头

```
---
title: "Operations specific to GPIB devices"
source_topic: "group__gpib.html"
source_html: "02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.html"
---
|Reference 254242   ![mag_sel.png](<../../../../raw/254242-search/mag_sel.png>)   [![close.png](<../../../../raw/254242-search/close.png>)](<javascript:searchBox.CloseResultsWindow()>)             Operations specific to GPIB devices

| [](<>) Enumerations |
| enum  | [GIO_GPIB_STATUS_REQUEST](<02.13.07.03_Operations_specific_to_GPIB_devices.md#ga5e55a5bea329978d932f4c7f7aae1325>) {
 [GIO_GPIB_STATUS_REMOTE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a5ce041586fc1cdfb5f7639ac925f57b0>) = 1, [GIO_GPIB_STATUS_SRQ](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a87370c026139cd974dd275a8bf842eeb>) = 2, [GIO_GPIB_STATUS_NDAC](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a7d0cc84b85da7c18c346d454935ed501>) = 3, [GIO_GPIB_STATUS_SYSTEM_CONTROLLER](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325adbb3b015a1275a31f1dffab3ebee40c2>) = 4,
 [GIO_GPIB_STATUS_CONTROLLER_IN_CHARGE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a023d85bc49e3b7e6b8f85247fab04bff>) = 5, [GIO_GPIB_STATUS_TALKER](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a4cac4ae666cfd776f766e3da5a794bd3>) = 6, [GIO_GPIB_STATUS_LISTENER](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325ac20ec61e014c0f40933eedaf4efcf1f1>) = 7, [GIO_GPIB_STATUS_BUS_ADDRESS](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a2455447c6fbe1683299efb90cdf30eac>) = 8
 }
|   | Parameters for GPIB Bus Status command. [More...](<02.13.07.03_Operations_specific_to_GPIB_devices.md#ga5e55a5bea329978d932f4c7f7aae1325>)
 | |

| [](<>) Functions |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_gpib_send_IFC](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gac412964b605b33bd1b60acaa8c6bae91>) (IDID id)Send an IFC (interface clear) on a GPIB interface. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_gpib_send_cmd](<02.13.07.03_Operations_specific_to_GPIB_devices.md#ga0305551b69eaeb5f96237491f449f199>) (IDID id, const void *pCommand, size_t len)Send a GPIB command. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_gpib_bus_status](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gad90039c7bf09a556c936e770cd6e12d2>) (IDID id, [GIO_GPIB_STATUS_REQUEST](<02.13.07.03_Operations_specific_to_GPIB_devices.md#ga5e55a5bea329978d932f4c7f7aae1325>) request, uint8_t *pResult)Inquire GPIB bus status. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_gpib_ATN_control](<02.13.07.03_Operations_specific_to_GPIB_devices.md#ga2981963d87898fcdfa57e65355046ef0>) (IDID id, bool_t enable)Control the ATN (attention) line on a GPIB interface. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_gpib_REN_control](<02.13.07.03_Operations_specific_to_GPIB_devices.md#ga3ef158829aa1b094e22c2842961ff4d0>) (IDID id, bool_t enable)Control the REN (remote enable) line on a GPIB interface. |
| [GIO_ERROR](<02.13.07.07_Error_handling.md#ga307753a7be5d06f3eaf383ca94efd15a>)  | [gio_gpib_local_lockout](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gae86193ba113ea0decd5b4f12ed8470f4>) (IDID id)Place all devices on a GPIB interface into local lockout mode.  |  [](<>)

## Detailed Description

## Enumeration Type Documentation

 [](<>)
```

### 抽取的标题

- L24 `## Detailed Description`
- L26 `## Enumeration Type Documentation`
- L78 `## Function Documentation`

### 抽取的边（34 条，显示前 10）

- L9 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：| enum | [GIO_GPIB_STATUS_REQUEST](<02.13.07.03_Operations_specific_to_GPIB_devices.md#ga5e55a5bea329978d932f4c7f7aae1325>) {
- L10 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：[GIO_GPIB_STATUS_REMOTE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a5ce041586fc1cdfb5f7639ac925f57b0>) = 1, [GIO_GPIB_STATUS_SRQ](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a87370c026139cd974dd275a8bf842eeb>) = 
- L10 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：[GIO_GPIB_STATUS_REMOTE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a5ce041586fc1cdfb5f7639ac925f57b0>) = 1, [GIO_GPIB_STATUS_SRQ](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a87370c026139cd974dd275a8bf842eeb>) = 
- L10 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：[GIO_GPIB_STATUS_REMOTE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a5ce041586fc1cdfb5f7639ac925f57b0>) = 1, [GIO_GPIB_STATUS_SRQ](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a87370c026139cd974dd275a8bf842eeb>) = 
- L10 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：[GIO_GPIB_STATUS_REMOTE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a5ce041586fc1cdfb5f7639ac925f57b0>) = 1, [GIO_GPIB_STATUS_SRQ](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a87370c026139cd974dd275a8bf842eeb>) = 
- L11 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：[GIO_GPIB_STATUS_CONTROLLER_IN_CHARGE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a023d85bc49e3b7e6b8f85247fab04bff>) = 5, [GIO_GPIB_STATUS_TALKER](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a4cac4ae666cfd776f766
- L11 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：[GIO_GPIB_STATUS_CONTROLLER_IN_CHARGE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a023d85bc49e3b7e6b8f85247fab04bff>) = 5, [GIO_GPIB_STATUS_TALKER](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a4cac4ae666cfd776f766
- L11 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：[GIO_GPIB_STATUS_CONTROLLER_IN_CHARGE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a023d85bc49e3b7e6b8f85247fab04bff>) = 5, [GIO_GPIB_STATUS_TALKER](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a4cac4ae666cfd776f766
- L11 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：[GIO_GPIB_STATUS_CONTROLLER_IN_CHARGE](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a023d85bc49e3b7e6b8f85247fab04bff>) = 5, [GIO_GPIB_STATUS_TALKER](<02.13.07.03_Operations_specific_to_GPIB_devices.md#gga5e55a5bea329978d932f4c7f7aae1325a4cac4ae666cfd776f766
- L13 → `02_System_reference/02.13_Generic_Input_Output__GIO__API/02.13.07.03_Operations_specific_to_GPIB_devices.md`
  - 语境：| | Parameters for GPIB Bus Status command. [More...](<02.13.07.03_Operations_specific_to_GPIB_devices.md#ga5e55a5bea329978d932f4c7f7aae1325>)

---

## `02_System_reference/index.md`

*抽样理由：02_System_reference 末篇；体积最大 1082500B；出度最高 8316*

- 字节 1082500 / 标题 1 / 出度 8316 / 代码块 0
- frontmatter：`null`
- title：`02_System_reference`
- 结构段落：（无）
- ⚠️ 解析异常：[{'detail': '文件首行不是 ---', 'doc': '02_System_reference/index.md', 'kind': 'no_frontmatter'}, {'detail': '', 'doc': '02_System_reference/index.md', 'kind': 'not_in_catalog'}]

### 原文开头

```
# 02_System_reference

- [SmarTest Release Concept](02.01_Release_Information/02.01.01_SmarTest_Release_Concept.md)
  - `250854.htm`
- [V93000 Components and Compatibility](02.01_Release_Information/02.01.02_V93000_Components_and_Compatibility.md)
  - `103226.htm`
- [TDC feedback and support](02.01_Release_Information/02.01.03_TDC_feedback_and_support.md)
  - `104296.htm`
- [Release Notes](02.01_Release_Information/02.01.04_Release_Notes.md)
  - `smartest64_7.10.3.0_ReleaseNotes.html`
- [Workstation Platform Description RHEL 7.4](02.01_Release_Information/02.01.05_Workstation_Platform_Description_RHEL_7.4.md)
  - `Workstation_Platform_Description_RHEL7.4.html`
- [Release Information](02.01_Release_Information/02.01_Release_Information.md)
  - `101490.htm`
- [Test heads](02.02_Specifications/02.02.01.01_Test_heads.md)
  - `347653.htm`
- [System slots](02.02_Specifications/02.02.01.02_System_slots.md)
  - `347655.htm`
- [Smart Scale device power supplies](02.02_Specifications/02.02.01.03_Smart_Scale_device_power_supplies.md)
  - `347656.htm`
- [Parametric measurements](02.02_Specifications/02.02.01.04_Parametric_measurements.md)
  - `347657.htm`
- [Internal utility resources](02.02_Specifications/02.02.01.05.01_Internal_utility_resources.md)
  - `347659.htm`
- [Utility Card (EK051 and EK051A)](02.02_Specifications/02.02.01.05.02_Utility_Card__EK051_and_EK051A.md)
  - `347661.htm`
- [Utility resources](02.02_Specifications/02.02.01.05_Utility_resources.md)
  - `347658.htm`
```

### 抽取的标题

- L1 `# 02_System_reference`

### 抽取的边（8316 条，显示前 10）

- L3 → `02_System_reference/02.01_Release_Information/02.01.01_SmarTest_Release_Concept.md`
  - 语境：[SmarTest Release Concept](02.01_Release_Information/02.01.01_SmarTest_Release_Concept.md)
- L5 → `02_System_reference/02.01_Release_Information/02.01.02_V93000_Components_and_Compatibility.md`
  - 语境：[V93000 Components and Compatibility](02.01_Release_Information/02.01.02_V93000_Components_and_Compatibility.md)
- L7 → `02_System_reference/02.01_Release_Information/02.01.03_TDC_feedback_and_support.md`
  - 语境：[TDC feedback and support](02.01_Release_Information/02.01.03_TDC_feedback_and_support.md)
- L9 → `02_System_reference/02.01_Release_Information/02.01.04_Release_Notes.md`
  - 语境：[Release Notes](02.01_Release_Information/02.01.04_Release_Notes.md)
- L11 → `02_System_reference/02.01_Release_Information/02.01.05_Workstation_Platform_Description_RHEL_7.4.md`
  - 语境：[Workstation Platform Description RHEL 7.4](02.01_Release_Information/02.01.05_Workstation_Platform_Description_RHEL_7.4.md)
- L13 → `02_System_reference/02.01_Release_Information/02.01_Release_Information.md`
  - 语境：[Release Information](02.01_Release_Information/02.01_Release_Information.md)
- L15 → `02_System_reference/02.02_Specifications/02.02.01.01_Test_heads.md`
  - 语境：[Test heads](02.02_Specifications/02.02.01.01_Test_heads.md)
- L17 → `02_System_reference/02.02_Specifications/02.02.01.02_System_slots.md`
  - 语境：[System slots](02.02_Specifications/02.02.01.02_System_slots.md)
- L19 → `02_System_reference/02.02_Specifications/02.02.01.03_Smart_Scale_device_power_supplies.md`
  - 语境：[Smart Scale device power supplies](02.02_Specifications/02.02.01.03_Smart_Scale_device_power_supplies.md)
- L21 → `02_System_reference/02.02_Specifications/02.02.01.04_Parametric_measurements.md`
  - 语境：[Parametric measurements](02.02_Specifications/02.02.01.04_Parametric_measurements.md)

---

## `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.01_Target_audience.md`

*抽样理由：03_Use_cases_and_application_papers 首篇*

- 字节 529 / 标题 1 / 出度 0 / 代码块 0
- frontmatter：`{"source_html": "03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.01_Target_audience.htm", "source_topic": "118191.htm", "title": "Target audience"}`
- title：`Target audience`
- 结构段落：（无）

### 原文开头

```
---
title: "Target audience"
source_topic: "118191.htm"
source_html: "03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.01_Target_audience.htm"
---
# Target audience

The V93000 Performance Cookbook is targeted to help SmarTest Users to increase the throughput of their test programs. It begins with some generic considerations related to throughput performances. Further you will become familiar with all aspects and rules to follow when designing testflows for performance.

```

### 抽取的标题

- L6 `# Target audience`

### 抽取的边（0 条，显示前 10）


---

## `03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01.07_Utility_line_capabilities_in_relation_to_the_system_hardware.md`

*抽样理由：03_Use_cases_and_application_papers 中位*

- 字节 5307 / 标题 7 / 出度 7 / 代码块 0
- frontmatter：`{"source_html": "03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01.07_Utility_line_capabilities_in_relation_to_the_system_hardware.htm", "source_topic": "149630.htm", "title": "Utility line capabilities in relation to the system hardware"}`
- title：`Utility line capabilities in relation to the system hardware`
- 结构段落：['Functional changes', 'Related information']

### 原文开头

```
---
title: "Utility line capabilities in relation to the system hardware"
source_topic: "149630.htm"
source_html: "03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01.07_Utility_line_capabilities_in_relation_to_the_system_hardware.htm"
---
# Utility line capabilities in relation to the system hardware

The capability of the utility lines depends on the test head type, the DUT interface and the type and version of the installed wiring board.

   Note This section applies to V93000 Pin Scale and Smart Scale systems.

## DUT interface

Two types of DUT interfaces are available for the test systems:

- DUT Scale interface or large DUT interfaceThe number of utility lines on a test system, fitted with a DUT Scale interface or large DUT interface, depends on the type of the utility pogo blocks:

  - 2-row utility pogo blocks: 128 utility lines
  - 4-row utility pogo blocks: 256 utility lines and additionally access to the optional [External utility power supply (V93000 systems)](<../../02_System_reference/02.03_DUT_board_design_reference/02.03.05.06_External_utility_power_supply__V93000_systems.md>)

- Small DUT interface

Test systems fitted with the small DUT interface (ATH, CTH and STH) provide 64 utility lines. The combination ATH/small DUT interface supports sequencer control of utility lines.

Details of DUT interface related layouts and utility lines are provided in [Utility line assignments](<../../02_System_reference/02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.md>) and [Utility line characteristics](<../../02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md>).

## Dynamic (sequencer鈥慶ontrolled) and static utility lines

```

### 抽取的标题

- L6 `# Utility line capabilities in relation to the system hardware`
- L12 `## DUT interface`
- L27 `## Dynamic (sequencer鈥慶ontrolled) and static utility lines`
- L39 `## Utility line capabilities in relation to the hardware configuration`
- L60 `## Information on the installed Wiring board type`
- L68 `## Related information`
- L72 `## Functional changes`

### 抽取的边（7 条，显示前 10）

- L19 → `02_System_reference/02.03_DUT_board_design_reference/02.03.05.06_External_utility_power_supply__V93000_systems.md`
  - 语境：4-row utility pogo blocks: 256 utility lines and additionally access to the optional [External utility power supply (V93000 systems)](<../../02_System_reference/02.03_DUT_board_design_reference/02.03.05.06_External_utility_power_supply__V93000_systems.md>)
- L25 → `02_System_reference/02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.md`
  - 语境：Details of DUT interface related layouts and utility lines are provided in [Utility line assignments](<../../02_System_reference/02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.md>) and [Utility line characteristics](<../../02_System_reference/02.03_DUT_board_design_reference/0
- L25 → `02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md`
  - 语境：Details of DUT interface related layouts and utility lines are provided in [Utility line assignments](<../../02_System_reference/02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.md>) and [Utility line characteristics](<../../02_System_reference/02.03_DUT_board_design_reference/0
- L31 → `03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md`
  - 语境：Dynamic (sequencer鈥慶ontrolled) utility lines can be controlled by the pattern sequencer. They are made available by an active Wiring board. For more information, refer to [Sequencer-controlled utility lines](<03.09.01_Sequencer-controlled_utility_lines.md>).
- L37 → `03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01.06_SmarTest_7_dependencies_between_static_and_dynamic_access.md`
  - 语境：For more information refer to [SmarTest 7 dependencies between static and dynamic access](<03.09.01.06_SmarTest_7_dependencies_between_static_and_dynamic_access.md>).
- L70 → `03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md`
  - 语境：[Sequencer-controlled utility lines](<03.09.01_Sequencer-controlled_utility_lines.md>)[External utility power supply (V93000 systems)](<../../02_System_reference/02.03_DUT_board_design_reference/02.03.05.06_External_utility_power_supply__V93000_systems.md>)EDC dump tool (Smart Scale Service guide)HL
- L70 → `02_System_reference/02.03_DUT_board_design_reference/02.03.05.06_External_utility_power_supply__V93000_systems.md`
  - 语境：[Sequencer-controlled utility lines](<03.09.01_Sequencer-controlled_utility_lines.md>)[External utility power supply (V93000 systems)](<../../02_System_reference/02.03_DUT_board_design_reference/02.03.05.06_External_utility_power_supply__V93000_systems.md>)EDC dump tool (Smart Scale Service guide)HL

### 抽取的段落

- `Related information`（related，L68，336 字符）
  - 开头：'[Sequencer-controlled utility lines](<03.09.01_Sequencer-controlled_utility_lines.md>)[External utility power supply (V9'
- `Functional changes`（version，L72，30 字符）
  - 开头：'- Introduced in SmarTest 7.2.0'

---

## `03_Use_cases_and_application_papers/index.md`

*抽样理由：03_Use_cases_and_application_papers 末篇*

- 字节 88005 / 标题 1 / 出度 573 / 代码块 0
- frontmatter：`null`
- title：`03_Use_cases_and_application_papers`
- 结构段落：（无）
- ⚠️ 解析异常：[{'detail': '文件首行不是 ---', 'doc': '03_Use_cases_and_application_papers/index.md', 'kind': 'no_frontmatter'}, {'detail': '', 'doc': '03_Use_cases_and_application_papers/index.md', 'kind': 'not_in_catalog'}]

### 原文开头

```
# 03_Use_cases_and_application_papers

- [Target audience](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.01_Target_audience.md)
  - `118191.htm`
- [Situation analysis ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.01_Situation_analysis.md)
  - `122115.htm`
- [Tester model and Configuration ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.02_Tester_model_and_Configuration.md)
  - `122743.htm`
- [Application focus ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.03_Application_focus.md)
  - `122744.htm`
- [Tools to analyze the situation](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.04_Tools_to_analyze_the_situation.md)
  - `122745.htm`
- [Defining target ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.05_Defining_target.md)
  - `122746.htm`
- [Generic Recommendations](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.06_Generic_Recommendations.md)
  - `123073.htm`
- [TP Performance Potential](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02_TP_Performance_Potential.md)
  - `121991.htm`
- [Multisite Programming Techniques ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.01.01_Multisite_Programming_Techniques.md)
  - `122749.htm`
- [Usage of Parallel Hardware (PPMU) ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.01.02_Usage_of_Parallel_Hardware__PPMU.md)
  - `122750.htm`
- [Semi-parallel best practices ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.01.03_Semi-parallel_best_practices.md)
  - `122751.htm`
- [Code Clean-up ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.01.04_Code_Clean-up.md)
  - `122752.htm`
- [Generic Test Program Setup ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.01_Generic_Test_Program_Setup.md)
  - `122747.htm`
```

### 抽取的标题

- L1 `# 03_Use_cases_and_application_papers`

### 抽取的边（573 条，显示前 10）

- L3 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.01_Target_audience.md`
  - 语境：[Target audience](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.01_Target_audience.md)
- L5 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.01_Situation_analysis.md`
  - 语境：[Situation analysis ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.01_Situation_analysis.md)
- L7 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.02_Tester_model_and_Configuration.md`
  - 语境：[Tester model and Configuration ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.02_Tester_model_and_Configuration.md)
- L9 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.03_Application_focus.md`
  - 语境：[Application focus ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.03_Application_focus.md)
- L11 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.04_Tools_to_analyze_the_situation.md`
  - 语境：[Tools to analyze the situation](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.04_Tools_to_analyze_the_situation.md)
- L13 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.05_Defining_target.md`
  - 语境：[Defining target ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.05_Defining_target.md)
- L15 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.06_Generic_Recommendations.md`
  - 语境：[Generic Recommendations](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.06_Generic_Recommendations.md)
- L17 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02_TP_Performance_Potential.md`
  - 语境：[TP Performance Potential](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02_TP_Performance_Potential.md)
- L19 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.01.01_Multisite_Programming_Techniques.md`
  - 语境：[Multisite Programming Techniques ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.01.01_Multisite_Programming_Techniques.md)
- L21 → `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.01.02_Usage_of_Parallel_Hardware__PPMU.md`
  - 语境：[Usage of Parallel Hardware (PPMU) ](03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.03.01.02_Usage_of_Parallel_Hardware__PPMU.md)

---

## `99_Unlisted_or_Unreferenced/99.0001_Test_Numbering_preferences.md`

*抽样理由：99_Unlisted_or_Unreferenced 首篇*

- 字节 1391 / 标题 2 / 出度 2 / 代码块 0
- frontmatter：`{"source_html": "99_Unlisted_or_Unreferenced/99.0001_Test_Numbering_preferences.htm", "source_topic": "118478.htm", "title": "Test Numbering preferences"}`
- title：`Test Numbering preferences`
- 结构段落：['Related information']

### 原文开头

```
---
title: "Test Numbering preferences"
source_topic: "118478.htm"
source_html: "99_Unlisted_or_Unreferenced/99.0001_Test_Numbering_preferences.htm"
---
# Test Numbering preferences

First test number: The number that is assigned to the first numbered test.

Increment size: The number that is added to the current test number to calculate the next test number.

Overwrite existing test numbers during generation:

- Check to assign new test numbers to all selected tests.
- Uncheck to assigned new numbers only to tests that have no number.

Use global testflow loop settings: Check to increase the test number for each test loop iteration at the testflow level. After each test loop iteration, the test number is increased by the specified amount.

Testflow loop increment: The number that is added after each test loop iteration.

Use global test method loop settings: Similar to Use global testflow loop settings (above), but for loops within test methods.

Test method loop increment: The number that is added after each test loop iteration.

## Related information

[Test Numbering preferences page](<../01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.24_Test_Numbering_preferences_page.md>)[Generating test numbers from the SmarTest GUI](<../02_System_reference/02.10_Data_Logging/02.10.01.08.01.01_Generating_test_numbers_from_the_SmarTest_GUI.md>)

```

### 抽取的标题

- L6 `# Test Numbering preferences`
- L25 `## Related information`

### 抽取的边（2 条，显示前 10）

- L27 → `01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.24_Test_Numbering_preferences_page.md`
  - 语境：[Test Numbering preferences page](<../01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.24_Test_Numbering_preferences_page.md>)[Generating test numbers from the SmarTest GUI](<../02_System_reference/02.10_Data_Logging/02.10.01.08.01.01_Generating_test_numbers_from_the_SmarTest_GUI.md>)
- L27 → `02_System_reference/02.10_Data_Logging/02.10.01.08.01.01_Generating_test_numbers_from_the_SmarTest_GUI.md`
  - 语境：[Test Numbering preferences page](<../01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.24_Test_Numbering_preferences_page.md>)[Generating test numbers from the SmarTest GUI](<../02_System_reference/02.10_Data_Logging/02.10.01.08.01.01_Generating_test_numbers_from_the_SmarTest_GUI.md>)

### 抽取的段落

- `Related information`（related，L25，291 字符）
  - 开头：'[Test Numbering preferences page](<../01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.24_Test_Numbering_preferenc'

---

## `99_Unlisted_or_Unreferenced/99.0125_Define_Site_Number_reference.md`

*抽样理由：99_Unlisted_or_Unreferenced 中位*

- 字节 419 / 标题 2 / 出度 1 / 代码块 0
- frontmatter：`{"source_html": "99_Unlisted_or_Unreferenced/99.0125_Define_Site_Number_reference.htm", "source_topic": "119770.htm", "title": "Define Site Number reference"}`
- title：`Define Site Number reference`
- 结构段落：['Related information']

### 原文开头

```
---
title: "Define Site Number reference"
source_topic: "119770.htm"
source_html: "99_Unlisted_or_Unreferenced/99.0125_Define_Site_Number_reference.htm"
---
# Define Site Number reference

Select number of sites: Select the number of sites that you wish to test. You can enter numbers from 1 to 256.

## Related information

[Setting the number of test sites](<99.0021_Setting_the_number_of_test_sites.md>)

```

### 抽取的标题

- L6 `# Define Site Number reference`
- L10 `## Related information`

### 抽取的边（1 条，显示前 10）

- L12 → `99_Unlisted_or_Unreferenced/99.0021_Setting_the_number_of_test_sites.md`
  - 语境：[Setting the number of test sites](<99.0021_Setting_the_number_of_test_sites.md>)

### 抽取的段落

- `Related information`（related，L10，81 字符）
  - 开头：'[Setting the number of test sites](<99.0021_Setting_the_number_of_test_sites.md>)'

---

## `99_Unlisted_or_Unreferenced/index.md`

*抽样理由：99_Unlisted_or_Unreferenced 末篇*

- 字节 21953 / 标题 1 / 出度 248 / 代码块 0
- frontmatter：`null`
- title：`99_Unlisted_or_Unreferenced`
- 结构段落：（无）
- ⚠️ 解析异常：[{'detail': '文件首行不是 ---', 'doc': '99_Unlisted_or_Unreferenced/index.md', 'kind': 'no_frontmatter'}, {'detail': '', 'doc': '99_Unlisted_or_Unreferenced/index.md', 'kind': 'not_in_catalog'}]

### 原文开头

```
# 99_Unlisted_or_Unreferenced

- [Test Numbering preferences](99.0001_Test_Numbering_preferences.md)
  - `118478.htm`
- [Core](99.0002_Core.md)
  - `119016.htm`
- [Using the firmware view](99.0003_Using_the_firmware_view.md)
  - `119017.htm`
- [CTM_UTM](99.0004_CTM_UTM.md)
  - `119029.htm`
- [CSH Topics](99.0005_CSH_Topics.md)
  - `119165.htm`
- [Pin Configuration](99.0006_Pin_Configuration.md)
  - `119166.htm`
- [Export 93000 Setup reference](99.0007_Export_93000_Setup_reference.md)
  - `119167.htm`
- [Import 93000 Setup reference](99.0008_Import_93000_Setup_reference.md)
  - `119168.htm`
- [New Pin Attributes reference](99.0009_New_Pin_Attributes_reference.md)
  - `119169.htm`
- [New Pin Configuration reference](99.0010_New_Pin_Configuration_reference.md)
  - `119170.htm`
- [Alias Set Editor reference](99.0011_Alias_Set_Editor_reference.md)
  - `119171.htm`
- [Analog pin editor reference](99.0012_Analog_pin_editor_reference.md)
  - `119172.htm`
- [Core allocation editor reference](99.0013_Core_allocation_editor_reference.md)
  - `119173.htm`
```

### 抽取的标题

- L1 `# 99_Unlisted_or_Unreferenced`

### 抽取的边（248 条，显示前 10）

- L3 → `99_Unlisted_or_Unreferenced/99.0001_Test_Numbering_preferences.md`
  - 语境：[Test Numbering preferences](99.0001_Test_Numbering_preferences.md)
- L5 → `99_Unlisted_or_Unreferenced/99.0002_Core.md`
  - 语境：[Core](99.0002_Core.md)
- L7 → `99_Unlisted_or_Unreferenced/99.0003_Using_the_firmware_view.md`
  - 语境：[Using the firmware view](99.0003_Using_the_firmware_view.md)
- L9 → `99_Unlisted_or_Unreferenced/99.0004_CTM_UTM.md`
  - 语境：[CTM_UTM](99.0004_CTM_UTM.md)
- L11 → `99_Unlisted_or_Unreferenced/99.0005_CSH_Topics.md`
  - 语境：[CSH Topics](99.0005_CSH_Topics.md)
- L13 → `99_Unlisted_or_Unreferenced/99.0006_Pin_Configuration.md`
  - 语境：[Pin Configuration](99.0006_Pin_Configuration.md)
- L15 → `99_Unlisted_or_Unreferenced/99.0007_Export_93000_Setup_reference.md`
  - 语境：[Export 93000 Setup reference](99.0007_Export_93000_Setup_reference.md)
- L17 → `99_Unlisted_or_Unreferenced/99.0008_Import_93000_Setup_reference.md`
  - 语境：[Import 93000 Setup reference](99.0008_Import_93000_Setup_reference.md)
- L19 → `99_Unlisted_or_Unreferenced/99.0009_New_Pin_Attributes_reference.md`
  - 语境：[New Pin Attributes reference](99.0009_New_Pin_Attributes_reference.md)
- L21 → `99_Unlisted_or_Unreferenced/99.0010_New_Pin_Configuration_reference.md`
  - 语境：[New Pin Configuration reference](99.0010_New_Pin_Configuration_reference.md)
