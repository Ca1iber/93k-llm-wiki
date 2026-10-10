---
type: concept
title: Equation based level setup
layer: n/a
stage: level
tags: [level, equation, setup, file-format, dps]
related: [level, level-file, level-master-file, equation-based-level-setup, level-equation-file, level-set-selector, level-setup-tool, level-spec, timing-equation-set, dpspins-resources]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02_Equation_based_level_setup.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Equation based level setup

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,098 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02_Equation_based_level_setup.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.02.01_Syntax_of_expression.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.05_Pin_alias_set__PIN_ALIAS_SET.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05.01_Master_file_format_for_level_setup.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Elements of Equation Based Level Setup › Syntax of expression）

shsp32

-10.00

ref+sp12*(shmsp5/sp5)

shsp18sp19>shsp32+ct3?shsp18sp19:shsp32+ct3

### Syntax（取自子主题 Structure of an equation based level setup › Pin alias set  PIN ALIAS SET）

!`PIN_ALIAS_SET`（raw: `../../../../raw/112434.png`）

 |

Pin alias set name

 |

The default pin alias set.

The pin alias defined in this alias set is used as the default in the equation set.

   | Note You can use pin aliases from sets other than the default pin alias set, by adding the set name in front of the pin alias: <pin_alias_set_name>::<pin_alias>`.` If you use a package pin name, add `"::"` before it: `::<`package_pin_name`>`.

### Examples（取自子主题 Structure of an equation based level setup › Pin alias set  PIN ALIAS SET）

### Alias set: alias_set_1

In this example, the involved pins are: `clock`, `io_pin`, and `mode`.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112433.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：Alias | Pin

### Alias set: alias_set_2

In this example, the involved pins are: `clock`, `io_pin`, and `mode`.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112433.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：Alias | Pin

The following is the timing equation set using the pin aliases.

```
EQNSET tim_eqn_set1
PIN_ALIAS_SET alias_set_1
TIMINGSET 1
PINS  ::clock  io_pin_1  alias_set_2::mode_2
...
```

In this example, the keyword PIN_ALIAS_SET specifies `alias_set_1` as the default alias set.

- To use a pin alias from the default alias set, specify the alias pin name without any prefix (for example, `io_pin_1`).
- To use a pin alias from an alias set which is not the default set, explicitly specify the alias set name (for example, `alias_set_2::mode_2`).
- To use a package pin name, add the prefix "::" (for example, `::clock`).

### Example 1: Copy/paste example with all resource keywords（取自子主题 Structure of an equation based level setup › DPSPINS）

```
EQNSET 1 "Example equation set 1"

DPSPINS Example_DPS_pin

    vout                        =  5.0      # [V]       Forced output voltage
    ilimit                      = 20.0      # [mA]      Source and sink current limit
    ilimit_source               = 20.0      # [mA]      Source current limit (DC Scale pins)
    ilimit_sink                 = 10.0      # [mA]      Sink   current limit (DC Scale pins)

    t_ms                        = 5.0       # [ms]      Connect setup time

    vout_rise_t_ms_per_volt     = 0.1       # [ms/V]    Inverse slew rate for the rising edge
    vout_rise_t_ms_per_volt_c2c = 0.2       # [ms/V]    Inverse "connect-to-connect" slew rate
    vout_fall_t_ms_per_volt     = 0.1       # [ms/V]    Inverse slew rate for the falling edge
    vout_fall_t_ms_per_volt_c2c = 0.2       # [ms/V]    Inverse "connect-to-connect" slew rate
    vout_rise_settling_t_ms     = 0.5       # [ms]      Settling time for the rising edge
    vout_rise_settling_t_ms_c2c = 0.9       # [ms]      "connect-to-connect" settling time
    vout_fall_settling_t_ms     = 0.5       # [ms]      Settling time for the falling edge
    vout_fall_settling_t_ms_c2c = 0.9       # [ms]      "connect-to-connect" settling time

    offcurr                     = act_min   #           act | min | open | act_min | act_open
                                            #           Defines current to apply in disconnected state

    vout_frc_rng                =  8.0      # [V]       Force voltage range
    iout_clamp_rng              = 50.0      # [mA]      Clamp current range

    disable_const_curr_check                #           Switch off constant current check
    ms_const_curr_disconnect    = 10.0      # [ms]      Delay for constant current flag (UHC4T + XPS256)

    connect_state               = ungang    #           norm (see note below) | himp | ungang |
                                            #           hdig (UHC4T) | hdig (UHC4T)

    ms_fast_preload             = 8.0       # [ms]      Full current (40A) for the specified time (UHC4T)
    max_voltage_drop_force      = 3.0       # [V]       Upper FS drop limit (UHC4T + XPS256)
    max_voltage_drop_return     = 3.0       # [V]       Lower FS drop limit (UHC4T + XPS256)
    protect                                 #           Current limiter (UHC4T)
    voltage_filter_frequency    = 2000.0    # [Hz]      Force voltage or clamp voltage filter (XPS256))
    current_filter_frequency    = 2000.0    # [Hz]      Force current or clamp current filter (XPS256))

    #
    # Parameters supported only by XPS256
    #
    capacitance                 = 100       # [uF]      Specifies the load capacitance on the DUT board.
    load_step_mode              = std       #           std, fast
    open_loop_protection        = diode     #           diode, none
    pulldown                    = on        #           on, off
    voltage_slew_rate           = 50        # [mV/us]
    warn_voltage_drop_force     = 0.3       # [V]
    warn_voltage_drop_return    = 0.2       # [V]

LEVELSET 1 "Example level set 1"            # Dummy for this example: At least one level set needs to be specified
```

The copy/paste example above shows all available keywords for the DPS pin resources and the DPS modulation set. The example is not valid for all types of DPS and must be adapted to the really used DPS.

The default value norm of DPS pin resource connect_state can be selected for the conn state column in the `DPS Setup window`（raw: `02.08.04.14.03.02_How_to_read_the_DPS_Setup_window.md`） of the Level setup tool and can be programmed by the related command `PSLR`（raw: `../02.06_Command_Reference/02.06.02.02.194_PSLR__PSLR__-__Power_Supply_Level_Ranges.md`） but cannot be programmed explicitly in the level setup equations. The parameter connect_state must be omitted to define the default value norm in the level setup equations.

### Example（取自子主题 Level setup master file › Master file format for level setup）

### Level master file

```
hp93000,level_master_file,0.1

# this is a comment
testerfile: demo.lev

EQNSET 1 [PIN_ALIAS_SET usb_set]: files/eqnset01.lev
EQNSET 2 : files/eqnset02.lev
EQNSET 3 : files/eqnset_34.lev
EQNSET 4 : files/eqnset_34.lev
TESTDATA : files/testdata.lev
DEFINES : files/defines.lev
GENERAL: GENERAL.lev
```

In the assembled level setup file `demo.lev`, the alias set `usb_set` is used in the equation set 1. When `demo.lev` is splitted, the alias set `usb_set` is removed from the generated sub-file `eqnset01.lev` and package pin names are used.

<!-- 语法节 end -->

## 是什么

**这一页讲的是「level setup 可以写成等式」这件事的定位，不是它的写法。**

**原文全文只有三段话**（这篇主文档本身不到 1.4 KB），本页照实按这三段展开。

### 一、level setup 的目标是什么

> 「The goal of a level setup is to **assign values to the level resources** like **drive levels,
> compare levels, load currents, power supply voltage**.」

**这四样就是 level setup 管的全部对象。** 本页的定位是「怎么赋值」，
**这四样各自的含义不在本页**（那是 [[level]] 的活）。

### 二、equation based 是什么：把「值」换成「表达式」

> 「Equation based level setup allows you to define **dependencies between different parameters in a
> general form** and provides **more flexibility**. With this setup, **the levels are determined by
> expressions that are built up from variables (and constants) by arithmetic and logical
> operators**.」

拆成两条：

| 特征 | 原文依据 |
|---|---|
| **可以在参数之间定义依赖** | `define dependencies between different parameters in a general form` |
| **值由表达式算出**，表达式由**变量、常量 + 算术/逻辑运算符**构成 | `built up from variables (and constants) by arithmetic and logical operators` |

**「参数之间有依赖」是这一页存在的理由**——不是「写法更短」，
是「一个 level 可以从别的 level 算出来」。

### 三、和固定值写法的机制差别：下载的粒度

> 「In equation based level setup, **the setup elements are part of larger data blocks which are
> downloaded to the test system as a whole**.」

**这一句是机制层面唯一的信息**：equation based 的 setup 元素**不是一个一个下发的**，
**是一整块一起下发的**。

> **（推断）** 这个「整块下发」的说法和 [[timing-setup-commands]] 那页里
> 「With **fixed** timing, each setup element is defined by **calling a firmware command**.
> With **equation based** timing, the setup elements are part of **larger data blocks that are
> downloaded to the tester as a whole**」是**同一句话的两个版本**（一个说 level，一个说 timing）。
> **依据**：两篇的措辞几乎一致，且都在讲「equation based 对上 firmware command」这组对立。
> **本页把这两处并列，但不下结论说 level 和 timing 共用同一套机制**——
> **本页没读 timing 那篇之外的任何依据。**

### 语法节里有东西——但那是脚本从子主题抽的

本页 `## 语法 / 参数` 一节**不是空的**：里面有 `Pin alias set` 的语法与两个例子、
`DPSPINS` 的 copy/paste 例子、以及 level setup master file 的开头。
**这些全部标着「取自子主题」**——**主文档自己没有语法段**，
所以脚本从 `Subtopics` 里那五篇抄的。

**这带来一个读法上的提醒**：语法节里的内容**不是本页的结论**，
是**五篇本页没读的子主题的逐字片段**。
**要看正规定义，回 raw 读那五篇。**

## 典型用法

**原文这篇没有任何操作内容**——没有 `## Procedure`、没有 `## Before you begin`、
没有 `## What to do next`、没有例子。**所以本节只能写「原文里有什么」。**

**原文能支撑的唯一一条「怎么用」，是它把这件事拆成了五步**（`Subtopics` 的五个标题，
本页按顺序列，**但不展开——本页一篇都没读**）：

| 顺序 | 子主题 | 本页对它的了解 |
|---|---|---|
| 1 | `The advantage of using level setup file to store all the level sets` | **只知道标题** |
| 2 | `Elements of Equation Based Level Setup` | **只知道标题** |
| 3 | `Structure of an equation based level setup` | **只知道标题**（语法节里有它的片段） |
| 4 | `Equation based level setup example` | **只知道标题** |
| 5 | `Level setup master file` | **只知道标题**（语法节里有它的开头） |

**从这五个标题能读出来的只有一件事**：
**这条路是「用一个 level setup file 存所有 level set」**，
**而且这个文件的组织方式由 master file 定**。
**具体怎么写，本页一个字都给不出。**

**（推断）** 「equation based」在本语料里是一个**跨阶段的做法**：level 有 equation based，
timing 也有（[[timing-setup-commands]] 明写 `The standard timing setup of SmarTest is equation
based.`）。**依据**：两篇文档用了同一组措辞。
**但 level 这一篇没说「这是标准做法还是可选做法」**——**timing 那篇说了，level 这篇没说。**

## 和谁有关

- [[level]] — 本页 `stage: level` 的理由：**它是 level 的赋值侧**
- [[level-file]] / [[level-master-file]] — **`Subtopics` 第 5 篇讲的就是 master file**；
  本页的语法节里已经有它的开头，**但格式细节在本页没有**
- [[level-equation-file]] — wiki 里另一页名字带 `equation` 的 level 页；
  **和本页是不是同一件东西，本页不知道**（本页没读它，也没读原文里对应的篇）
- [[timing-equation-set]] — **timing 侧的对应物**；和本页是同一族做法的两个阶段
- [[level-spec]] — level specification；**本页的表达式最终落成什么，本页没说**
- [[level-set-selector]] / [[level-setup-tool]] — level 的 GUI 侧；
  **本页讲的是文件/表达式这一侧，和它们的关系原文没提**
- [[dpspins-resources]] — **本页语法节里 `DPSPINS` 那个例子来自子主题**，
  而 `DPSPINS` 的另一处落点在这一页
- [[equation-based-level-setup]] — 本页自己
- `The advantage of using level setup file to store all the level sets` /
  `Elements of Equation Based Level Setup` / `Structure of an equation based level setup` /
  `Equation based level setup example` / `Level setup master file`（**均未建**）—
  **本页 `Subtopics` 的五篇，本页一篇没读**；语法节里的内容就是它们被脚本抽出来的片段

## 版本

**本文档没有 `## Functional changes` 段。**

（这是一条事实，不是缺陷：原文主文档只有三段正文，没有任何版本条目，
**也没有 `## Related information` 段**。）

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02_Equation_based_level_setup.md`

**本页没做的**：

- **`Subtopics` 的五篇一篇没读**——**这是本页最大的缺口，而且缺口比本页的正文还大。**
  本页主文档只有三段话，**而「equation based level setup 到底怎么写」
  全在那五篇里**。所以本页能给的**只有定位，没有做法**。
- **`## 语法 / 参数` 一节里的内容本页一条都没有验证过**：
  `Pin alias set` 的语法、两个 alias set 例子、`DPSPINS` 的 copy/paste 例子、
  level master file 的开头——**它们都是脚本从子主题逐字抄的**，
  **本页没有读那些子主题，所以无法判断它们是否是完整格式、有没有上下文缺失。**
- **图零张**（原文这篇没有图）。
- **原文没有 `## Procedure` / `## Before you begin` / `## What to do next` /
  `## Related information`**，所以「典型用法」一节里
  **除「有五步」之外没有内容可写**。
- **「drive levels / compare levels / load currents / power supply voltage」四样
  各是什么，本页没读、没展开。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **主文档标题是 `Equation based level setup`，而子主题标题用的是
> `Equation Based Level Setup`**（`Elements of Equation Based Level Setup` 里三个词都大写）
> ——**同一页里两种大小写。**
> ② **`Subtopics` 列出五篇，但主文档正文里一篇都没有链接**——
> 三段话里没有任何指向那五篇的引用，**链接只存在于 `Subtopics` 那一节**。
> ③ **这一篇是本页所见的扫描里少见的「没有 `## Functional changes` 也没有
> `## Related information`」的主文档**——两个通常都有的段都没有。

`verified: doc-only`
