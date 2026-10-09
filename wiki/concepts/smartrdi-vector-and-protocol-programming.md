---
type: concept
title: SmartRDI: Vector and protocol programming
layer: n/a
stage: testmethod
tags: [smartrdi, pattern, vector, protocol, api, error-map]
related: [smartrdi, pattern, pattern-object, pattern-master-file, vector-setup-file, waveform-mapping, match-loops, event-waveform-vfim, event-waveform-vfvm, smartrdi-2.3.0]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24_SmartRDI__Vector_and_protocol_programming.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# SmartRDI: Vector and protocol programming

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **50,888 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.13.24_SmartRDI__Vector_and_protocol_programming.md>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.02_bitLength.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.04_burstUpload.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.05_comment.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.06_copyLabel.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.07_defaultBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.08_defaultVec.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.09_download.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.10_emapLocation.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.11_enPassFail.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.12_expectBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.13_expectData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.14_failCount.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.15_failCyc.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.16_failNode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.17_FFC.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.18_fillBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.19_fillVec.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.20_insertJmpe.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.21_insertSub.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.22_label.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.23_labelName.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.24_multiFFC.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.25_passNode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.26_pMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.27_pModeStrobe.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.28_readBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.29_readData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.30_rdi.smartVec__.readMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.31_repeat.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.32_repeatSub.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.33_rdi.smartVec__.vecEditMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.34_vecLength.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.35_writeBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.36_writeData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.37_writeDataBurst.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.38_writeParData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.39_writeParDataBurst.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.40_writePat.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.41_writeVec.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.42_xMode.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.43_getFailCount.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.44_getFailCyc.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.45_getFFC.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.46_rdi.id__.getMultiFFC.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.47_getReadBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.48_getReadData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.01.01_instruction.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.02.01_matchBit.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.02.02_matchCycle.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.02.03_matchData.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.03_Retrieving_match_loop_results.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 bitLength）

```
bitLength(int length);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

length

 |

The length of the bit stream.

   | Note If the pattern contents exceed the length defined by the bitLength() parameter, the length of the generated pattern refers to the actual contents' length.

### Example（取自子主题 bitLength）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").defaultBit(0).bitLength(10).execute();
RDI_END();
```

### Syntax（取自子主题 burstLabel）

```
burstLabel(const string &labelName);
burstLabel(const string &labelName,TA::MD5_OPTION);
```

List of parameters
| Parameter | Description |
|---|---|
| labelName | The specified name of the big label.<br><br>The label name can be as long as 128 characters at maximum. |
| TA::MD5_OPTION | The option which defines to use an MD5 postfix string or not in the label name. |

List of available options of parameter: <TA::MD5_OPTION>
| Option | Description |
|---|---|
| TA::MD5_ON | With an MD5 postfix string in the label name. This is the default value.<br><br>With MD5_ON, the maximum length of a valid "targetLabelName" in the generated pattern name is 74. |
| TA::MD5_OFF | Withou an MD5 postfix string in the label name.<br><br>With MD5_OFF, the maximum length of a valid "targetLabelName" in the generated pattern name is 111. |

### Example 1（取自子主题 burstLabel）

```
...
RDI_BEGIN();
  rdi.smartVec().burstLabel("burstlabel").begin();
    rdi.smartVec().pin("DATA1").writeVec("01",2).execute();
    rdi.smartVec().pin("DATA3").fillBit(1,8,4).execute();
    rdi.smartVec().pin("DATA7").writeData(0x54,8,4).execute();
  rdi.smartVec().burstLabel().end();
RDI_END();

// Allow repeat() and wait() in burstLabel() in SmartRDI 2.3.1
RDI_BEGIN();
  rdi.smartVec().burstLabel("burstlabel").begin();
    rdi.smartVec().pin("DATA1").writeVec("01",2).repeat(2).execute();
    rdi.wait(1 ms);
    rdi.smartVec().pin("DATA3").fillBit(1,8,4).repeat(3).execute();
    rdi.wait(1 ms);
    rdi.smartVec().pin("DATA7").writeData(0x54,8,4).repeat(4).execute();
  rdi.smartVec().burstLabel().end();
RDI_END();

// Allow to get the Pass-Fail result with burstLabel() in SmartRDI 2.3.1
RDI_BEGIN();
  rdi.smartVec("pf_result").burstLabel("burstlabel").enPassFail().begin();
    rdi.wait(1 ms);
    rdi.smartVec().pin("DATA3"). writeData(0x54,8,4)
                  .pin("DATA4"). expectData(0x54,8,4)
                  .repeat(3).execute();
    rdi.wait(1 ms);
rdi.smartVec().pin("DATA5"). writeData(0x55,8,24)
                  .pin("DATA6"). expectData(0x55,8,24)
                  .repeat(3).execute();
    rdi.smartVec().burstLabel().end();
RDI_END();
...
int passfail_result=rdi.id("pf_result").getPassFail();
```

Note The resulting "big pattern" is automatically reusable. If the content is changed, the postfix of the pattern name will be changed and a new pattern will be created. If the content is not changed, SmartRDI will reuse the existing pattern. An md5 postfix string will be added to the created label.

### Example 2（取自子主题 burstLabel）

```
burstLabel("abc")              // The default is with an MD5 postfix
burstLabel("abc",TA::MD5_ON)   // With an MD5 postfix
burstLabel("abc",TA::MD5_OFF)  // Without an MD5 postfix
```

Note In case that the MD5 postfix option is OFF, make sure that if the content is different, the label name must be different.

### Example 3（取自子主题 burstLabel）

```
RDI_BEGIN();
  ...
  rdi.smartVec("pf").burstLabel("abc").enPassFail().begin();
    rdi.smartVec()...
    ...
  rdi.smartVec().burstLabel().end();
  ...
RDI_END();

Rdi.id("pf").getPassFail();
```

### Example 4（取自子主题 burstLabel）

Since SmartRDI 2.4.4, the combination of run-time accesses for the VTT mode within a `burstLabel().begin()`/`burstLabel().end()` block is supported.

```
rdi.smartVec().vecEditMode(TA::VTT);
rdi.runTimeVal("rtData",rtData);

RDI_BEGIN();
  rdi.smartVec().burstLabel("abc").begin();
  for(int k=0;k<64;k++)  // 64 vector segments to edit in run time
  {
    rdi.smartVec().pin("DATA1").writeData("rtData",16,0).vecLength(160).execute();
  }
  rdi.smartVec().burstLabel().end();
RDI_END();
```

There should be no instructions like MACT, RPTV, JSUB inside the burst label.

### Example 5（取自子主题 burstLabel）

Before SmartRDI 2.4.5, the `rdi.smartVec().burstLabel().begin()/rdi.smartVec().burstLabel().end()` block can only be used for a single port.

SmartRDI 2.4.5 supports the combination of multiple parallel `execute()` commands for specified ports by `rdi.port().smartVec().burstLabel()`. It also supports the combined usage with `portSync()`. See example below.

 !`burstLabel()_for_ports_with_portSync()`（raw: `../../../../agent-html/153089.png`）

### Syntax（取自子主题 burstUpload）

```
burstUpload();
```

### Example（取自子主题 burstUpload）

```
// you can get a combined result of all readBit()/readData() inside burstUpload.begin()/end() from only one id.
ON_FIRST_INVOCATION_BEGIN();

rdi.smartVec().readMode(TA::EMAP);  // TA::DIGCAP

RDI_BEGIN();
rdi.smartVec("id").burstUpload().begin();
rdi.smartVec(id1).pin("DATA2").readBit(2,2).execute();
rdi.smartVec(id2).pin("DATA2").readBit(4,4).execute();
rdi.smartVec(id3).pin("DATA4").readData(8,8).execute();
rdi.smartVec(id4).pin("DATA4").readData(8,12).execute();
rdi.smartVec().burstUpload().end();
RDI_END();

ON_FIRST_INVOCATION_END();

ARRAY_I bitResult=rdi.id("id").getReadBit("DATA2");
ARRAY_LL dataResult=rdi.id("id").getReadData("DATA4");
```

### Syntax（取自子主题 comment）

```
comment(const string &comment, int vecNum);
```

List of parameters
| Parameter | Description |
|---|---|
| comment | The content to be added. |
| vecNum | The position of the vector. |

See `SMV_IGNORE_COMMENT`（raw: `02.07.13.04_RDI_Configure_file.md#_146692__row_SMV_IGNORE_COMMENT`）, which can be used in the `RDI_Configure file`（raw: `02.07.13.04_RDI_Configure_file.md`） to globally disable comment output in pattern generation.

### Examples（取自子主题 comment）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeData(0x54,8).comment("MSB",0).comment("LSB",8).execute();
RDI_END();
```

   Note Adding comments significantly increases the time for pattern generation (first-run). To reduce the first-run time, you can remove the comment commands from your code after the pattern generation and debugging have been finished.

### Syntax（取自子主题 copyLabel）

```
label("Label").copyLabel(boolVar);
```

List of parameters
| Parameter | Description |
|---|---|
| boolVar | Specifies whether to edit an existing pattern, or create a copy from an existing pattern and edit the copied pattern. |

List of available options of parameter: bool
| Option | Description |
|---|---|
| true | Make a copy of an existing pattern and edit the copied pattern.<br><br>This is the default value. |
| false | Edit an existing pattern. |

Return value

There is no return value.

### Example（取自子主题 copyLabel）

```
RDI_BEGIN();
...
 rdi.smartVec().label("label4").copyLabel(false).pin("D3").writeData(0x55,8,0).execute();
...
RDI_END();
```

### Syntax（取自子主题 defaultBit）

```
defaultBit(int bit);
defaultBit(string bit);
```

List of parameters
| Parameter | Description |
|---|---|
| bit | The bit or string you want to write into the pattern. |

### Example（取自子主题 defaultBit）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").bitLength(20).defaultBit(0).execute();
RDI_END();
```

Supporting a string

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").bitLength(20).defaultBit("L").execute();
RDI_END();
```

### Syntax（取自子主题 defaultVec）

```
defaultVec(int index);
defaultVec(string dvc);
```

List of parameters
| Parameter | Description |
|---|---|
| index | The physical index you want to write to the pattern . |
| dvc | The device cycle you want to write to the pattern. |

### Example（取自子主题 defaultVec）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").defaultVec(0).vecLength(10).execute();   // index
rdi.smartVec().pin("DATA3").defaultVec("1").vecLength(10).execute(); // device cycle
RDI_END();
```

### Syntax（取自子主题 download）

```
download();
```

 A statement example that download() works together with write...() and expect...() commands:

```
rdi.smartVec().pin(pName).write...("rtData",...).download();
```

```
rdi.smartVec().pin(pName).expect...("rtData",...).download();
```

### Examples（取自子主题 download）

### download() code structure

```
ARRAY_LL rtData = ...
rdi.runTimeVal("rtD", rtData);

//Download value into the existing pattern label "abc"
rdi.smartVec().label("abc").copyLabel(false).pin("D1").writeData("rtD",8).download();

//Create a new label "cde" based on code and download runtime data in it.
rdi.smartVec().pin("D2").defaultBit(1).writeData("rtD",8,10).labelName("cde").download();

```

### Hidden vector download

```
ARRAY_LL rtData= ...
rdi.runTimeVal("rtData", rtData);

RDI_BEGIN();
...
RDI_END(TA::NON_BLOCKING);

rdi.smartVec().pin(pinA).writeData("rtData",8).labelName("abc").download();
...
RDI_WAIT_TEST_DONE();
```

### Using copyLabel(false) and download() together

```
RDI_BEGIN();
  rdi.func("id1").label("label1").execute(); // measurement
  rdi.digCap().pin(A).samples(5).execute();  // measurement
RDI_END(TA::NON_BLOCKING);

rdi.smartVec().label("abc").copyLabel(false).pin("pinA").writeData("rtD",8).download();
// HVD to the existing pattern "abc" without creating a new pattern.

RDI_WAIT_TEST_DONE();
```

### NON_BLOCKING starts at the second run

```
RDI_BEGIN()
  rdi.dc().pin("dig").vForce(1).iMeas().execute();
RDI_END(TA::NON_BLOCKING)

rdi.smartVec() label("abc").copyLabel(false).pin("pinA").writeData("rtD",8).download();

RDI_WAIT_TEST_DONE();
```

### Syntax（取自子主题 emapLocation）

```
emapLocation(TA::EMAP_LOCATION loc);
```

List of parameters
| Parameter | Description |
|---|---|
| TA::EMAP_LOCATION loc | The location where error maps are stored. |

List of available options of parameter: <TA::EMAP_LOCATION loc>
| Option | Description |
|---|---|
| TA::TP | The location is the test processor on the card. The default value. |
| TA::RAM | The location is the unused vector memory on the tester. |

### Example（取自子主题 emapLocation）

```
rdi.emapLocation(TA::RAM);
rdi.smartVec().readMode(TA::EMAP)

RDI_BEGIN();
  rdi.smartVec().pin("A").readBit(10000).execute();
RDI_END();
```

### Syntax（取自子主题 enPassFail）

```
enPassFail(bool val = true)
```

### Example（取自子主题 enPassFail）

```
RDI_BEGIN();
  rdi.smartVec("a").label("label1").pin("A")....enPassFail(true).execute();
  rdi.smartVec("b").label("label2").pin("B")....enPassFail().execute();
RDI_END();

rdi.id("a").getPassFail();
rdi.id("b").getPassFail();
```

### Syntax（取自子主题 expectBit）

```
expectBit(ARRAY_I bitStream,int startBit=0);
expectBit(string rtv, int startBit=0); // For runtime setup
```

Relationship of bit to DVC:

- X1 mode: bit 0 to DVC "L", 1 to "H", and 2 to "X".
- Xn mode: 0101 to "LHLH" and 0112 to "LHHX".
  SmartRDI always deals with 0, 1, and 2 for DVC "L", "H", and "X".

List of parameters
| Parameter | Description |
|---|---|
| bitStream | The expected bit stream you need to get from the captured pin. |
| startBit | The starting position of the bits to be compared. If the startBit parameter is not specified, the default value is 0. |
| rtv | The value to be used at runtime. |

### Example（取自子主题 expectBit）

```
ARRAY_I bitStream(4);
bitStream[0]=1;
bitStream[1]=0;
bitStream[2]=1;
bitStream[3]=1;

ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();
  rdi.smartVec(1).pin("DATA7").expectBit(bitStream,2).execute();
RDI_END();

ON_FIRST_INVOCATION_END();

int pf_result=rdi.id(1).getPassFail();
```

### Syntax（取自子主题 expectData）

```
expectData(long long data, int bitLength, int startBit=0);
expectData(string rtv, int bitLength, int startBit=0);
```

List of parameters
| Parameter | Description |
|---|---|
| data | The expected data you want to get from the captured pin. |
| bitLength | The length of the bits (data will be automatically converted into bits) to be written. |
| startBit | The starting position of the bits to be compared. If the startBit parameter missing, the default value is 0. |
| rtv | The value to be used at runtime. |

### Example 1（取自子主题 expectData）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA3").expectData(0x54,8,2).execute();
RDI_END();
```

### Example 2（取自子主题 expectData）

This example demonstrates how to use `expectData()` at runtime.

```
ARRAY_I outputSite = ...
rdi.runTimeVal("rtValue", outputSite);
RDI_BEGIN();
  ...
  rdi.smartVec("a").pin("pinA").expectData("rtValue",8).execute();
  ...
RDI_END();

int result = rdi.id("a").getPassFail();
```

### Syntax（取自子主题 failCount）

```
failCount(int startCyc,int cycRange);
failCount(int startCyc);
failCount();
```

List of parameters
| Parameter | Description |
|---|---|
| startCyc | Start cycle. |
| cycRange | Cycle range. |

Return value

There is no return value.

  Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports xMode directly.
- The xMode parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when xMode is set to be greater than 1.
- For one pin, xMode must remain the same in different labels in burst; otherwise the results might be wrong.

### Syntax（取自子主题 failCyc）

```
failCyc(int startCyc,int cycRange);
failCyc(int startCyc);
failCyc();
```

List of parameters
| Parameter | Description |
|---|---|
| startCyc | Start cycle. |
| cycRange | Cycle range. |

Return value

There is no return value.

  Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports xMode directly.
- The xMode parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when xMode is set to be greater than 1.
- For one pin, xMode must remain the same in different labels in burst; otherwise the results might be wrong.

### Syntax（取自子主题 failNode）

```
failNode();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 failNode）

```
RDI_BEGIN();
...
  rdi.smartVec...
	.insertJmpe(2).failNode().pin("DATA1").writeData(0xf,8,0)...execute();
...
RDI_END();
```

### Syntax（取自子主题 FFC）

```
FFC(int startCyc);
FFC();
```

List of parameters
| Parameter | Description |
|---|---|
| startCyc | The number of the first cycle in a cycle range in which fails are counted.<br><br>An integer. Cycle counting starts from zero.<br><br>This is an optional parameter. If it is omitted, the cycle range starts with the first cycle. |

Return value

There is no return value.

  Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports xMode directly.
- The xMode parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when xMode is set to be greater than 1.
- For one pin, xMode must remain the same in different labels in burst; otherwise the results might be wrong.

### Syntax（取自子主题 fillBit）

```
fillBit(int bit,int bitLength,int startBit);
fillBit(const string bit,int bitLength,int startBit);
```

List of parameters
| Parameter | Description |
|---|---|
| bit | The bit or string that you want to write to the pattern. |
| bitlength | The length of the bits to be filled. |
| startBit | The starting position of the bit to be written. If you do not specify a starting position, the default value is 0. |

### Example（取自子主题 fillBit）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").fillBit(1,4,2).execute(); // index
RDI_END();
```

Supporting a string

```
RDI_BEGIN()
  rdi.smartVec().pin("A").defaultBit(0).fillBit("p",4,1)
                         .xMode(2).bitLength(6)
                         .execute();
RDI_BEGIN();
```

You must define device cycles in the corresponding wavetable.

### Syntax（取自子主题 fillVec）

```
fillVec(int index,int vecLength,int startVec);
fillVec(string dvc,int vecLength,int startVec);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

index

 |

The physical index you want to write to the pattern .

 |
 |

dvc

 |

The device cycle you want to write to the pattern.

 |
 |

vecLength

 |

The length of the vector to be filled.

 |
 |

startVec

 |

The starting position of the vector to be written. If the startVec parameter missing, the default value is 0.

   | Note You must define the device cycles' names in the corresponding wavetables.

### Example（取自子主题 fillVec）

```
RDI_BEGIN()
rdi.smartVec().pin("DATA1").fillVec(3,1).execute();       // physical index= 3
rdi.smartVec().pin("DATA3").fillVec("0101",4).execute();  // device cycle
RDI_END();
```

### Syntax（取自子主题 insertJmpe）

```
insertJmpe(int vecLine, int level);
```

List of parameters
| Parameter | Description |
|---|---|
| vecLine | Number of the vector line where you want to insert the subroutine. |
| level | Subroutine level. This refers to the target level at which you want to insert a new subroutine.<br><br>The default value is 1, which means the first level subroutine and actually refers to the main pattern. To insert a subroutine into another subroutine, you should specify a level larger than 1. |

Return value

There is no return value.

### Example 1（取自子主题 insertJmpe）

```
RDI_BEGIN();
  rdi.smartVec(). pin("DATA1").writeData(0x1,8,0)// the content in main pattern
     .insertJmpe(2).passNode().pin("DATA1").writeData(0x0,8,0) // the content of pass branch label of JMPE in main pattern
                   .failNode().pin("DATA1").writeData(0xf,8,0).execute(); // the content of fail branch label by JMPE in main pattern
RDI_END();
```

This code example inserts two subroutines into the pattern at vector 2: one subroutine for pass node and the other for fail node. See the figure below.

 !`insertJmpe`（raw: `../../../../agent-html/152409.png`）

### Example 2（取自子主题 insertJmpe）

You can use `insertJmpe()` inside `insertSub()`（raw: `02.07.13.24.21_insertSub.md`）. Below is an example.

```
RDI_BEGIN();
...
  rdi.smartVec().pin()...pin()...
                      .insertSub(3).repeatSub()...
                      .insertJmpe(5,2).passNode()...
                                      .failNode()...
                      .execute();
...
RDI_END();
```

### Example 3（取自子主题 insertJmpe）

You can also use `insertSub()`（raw: `02.07.13.24.21_insertSub.md`） inside `insertJmpe()`. Below is an example.

```
RDI_BEGIN();
...
  rdi.smartVec().pin()...pin()...
                       .insertJmpe(3)
                            .passNode()...
                               .insertSub(5,2).repeatSub()...
                            .failNode()...
                      .execute();
...
RDI_END();
```

### Example 4（取自子主题 insertJmpe）

You can insert JSUB and JMPE in the same vector line of a label. The JSUB instruction is invoked before the JMPE instruction in this case. Below is an example.

```
RDI_BEGIN();
    rdi.smartVec("id5").pin("DATA1").writeData(0x1,8,0)
        .insertSub(2).pin("DATA1").writeData(0x1,8,0)
        .insertSub(2).pin("DATA1").writeData(0x2,8,0)
        .insertJmpe(2).passNode().pin("DATA1").writeData(0x3,8,0)
                  .failNode().pin("DATA1").writeData(0x4,8,0)
        .execute();
RDI_END();
```

### Syntax（取自子主题 insertSub）

```
insertSub(int vecLine);
insertSub(int vecLine, int level);
```

List of parameters
| Parameter | Description |
|---|---|
| vecLine | Number of the vector line where you want to insert the subroutine. |
| level | Subroutine level. This refers to the target level at which you want to insert a new subroutine.<br><br>The default value is 1, which means the first level subroutine and actually refers to the main pattern. To insert a subroutine into another subroutine, you should specify a level larger than 1. |

Return value

There is no return value.

### Example 1（取自子主题 insertSub）

```
RDI_BEGIN();
    rdi.smartVec("id2").pin("DATA1").writeData(0x1,8,0);    // the content of the main pattern
        .insertSub(3).pin("DATA1").writeData(0x3,8,0);    // the content of sublabel A which is inserted in the main pattern
        .insertSub(6).pin("DATA1").writeData(0x6,8,0);    // the content of sublabel B, which is inserted in the main pattern
        .insertSub(9,2).pin("DATA1").writeData(0x9,8,2).execute();    // the content of sublabel C which is inserted in sublabel B
RDI_END();
```

In the example above, subroutines A and B are inserted into the main pattern at vector lines 3 and 6. subroutine C is inserted into a level 2 subroutine at vector line 9. Because the insertion is always made in the closest label when multiple subroutines exist at the target insertion level, subrountine C is inserted into subroutine B which is closer than A. The created pattern structure is as follows.

 !`2016-11-09_16-28-25`（raw: `../../../../agent-html/152255.png`）

### Example 2（取自子主题 insertSub）

Below is an example of using `label()`（raw: `02.07.13.24.22_label.md`）, for example `label("abc")`, within `insertSub()`:

```
RDI_BEGIN();
...
rdi.smartVec().pin()...pin()... // the content in the main pattern
           .insertSub(10).label("abc")    // label "abc" is inserted in the main pattern with JSUB
              .insertSub(5 ).label("abc").pin()...pin()... // sublabel A (copied and edited from "abc") is inserted in the main pattern with JSUB
...
RDI_END();
```

In this example,

- If there are no `pin()...pin()...` settings after `label()`, the label "abc" will be directly called by JSUB.
- If there are `pin()...pin()...` settings after `label()`, the label "abc" will be copied and edited, then called by JSUB.
- If the label "abc" is not a subroutine, SmartRDI will clone it to a subroutine, then call it by JSUB and give a warning.

### Example 3（取自子主题 insertSub）

Below is an example when `insertSub()` is put in to `label()`（raw: `02.07.13.24.22_label.md`）, for example `label("abc")`:

```
RDI_BEGIN();
    rdi.smartVec().label("abc").pin()...pin()...  // the content in the main pattern
          .insertSub(5).pin()...pin()... // the content in sublabel A, which is inserted in the main pattern
RDI_END();
```

In this example,

- If `copyLabel()`（raw: `02.07.13.12.01.01.04_copyLabel.md`） is set to true, the JSUB will be inserted into the copy of label "abc"; if `copyLabel()`（raw: `02.07.13.12.01.01.04_copyLabel.md`） is set to false, the JSUB will be inserted directly into label "abc".
- Following the general rule, omitting the `copyLabel()`（raw: `02.07.13.12.01.01.04_copyLabel.md`） command by default makes a copy of the label "abc" and inserts the modification. The copied label name will hold the content of the actions. It ensures the right content in the right pattern.

### Example 4（取自子主题 insertSub）

`insertSub(`) can be used inside a `burstLabel().begin()`/`burstLabel().end()` block, as long as it is not inserted into a user label. Below is an example.

```
RDI_BEGIN();
    rdi.smartVec().burstLabel("smv").begin();
    rdi.smartVec().pin("DATA1").readData(2,0)
        .insertSub(3).repeatSub(5).pin("DATA1").writeData(0x86,8,3).execute();
    rdi.smartVec()
        .insertSub(10).pin("DATA1").writeData(0x86,8,3).execute();
    rdi.smartVec().burstLabel().end();
RDI_END();
```

### Syntax（取自子主题 label）

```
label(const string& sLabelName);
```

List of parameters
| Parameter | Description |
|---|---|
| sLabelName | The label to be executed / pattern on which measurement is performed. |

Return value

There is no return value.

### Example（取自子主题 label）

```
RDI_BEGIN();
...
  rdi.smartVec().label("label4").pin("D3").writeData(0x55,8,0).execute();
...
RDI_END();
```

### Syntax（取自子主题 labelName）

```
labelName(const string &name);
labelName(const string &name, TA::MD5_OPTION);
```

List of parameters
| Parameter | Description |
|---|---|
| name | User specified name for the label. |
| TA::MD5_OPTION | The option which defines to use an MD5 postfix string or not. |

List of available options of parameter: <TA::MD5_OPTION>
| Option | Description |
|---|---|
| TA::MD5_ON | With an MD5 postfix string in the label name.<br><br>With MD5_ON, the maximum length of a valid "targetLabelName" in the generated pattern name is 74. |
| TA::MD5_OFF | Without an MD5 postfix string in the label name. This is the default value.<br><br>With MD5_OFF, the maximum length of a valid "targetLabelName" in the generated pattern name is 111. |

### Example（取自子主题 labelName）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3").writeData(0x54,8,2).readData(8,20).labelName("label_name").execute();
RDI_END();
```

Note If a label with the same name exists, the pattern will not be re-generated. So make sure that the label name will change if the content changes.

### Syntax（取自子主题 multiFFC）

```
multiFFC(int startCycle, int FailNumber);
```

List of parameters
| Parameter | Description |
|---|---|
| startCycle | The number of the first cycle to start the action. |
| FailNumber | The number of failing cycles within a pattern to acquire. |

Use the following functions to collect the result:

- getMultiFFC(string resultPin)
- getMultiFFC():Use this command if only one result pin exists.
   Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports `xMode`（raw: `02.07.13.24.42_xMode.md`） directly.
- The `xMode`（raw: `02.07.13.24.42_xMode.md`） parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when `xMode`（raw: `02.07.13.24.42_xMode.md`） is set to be greater than 1.
- For one pin, `xMode`（raw: `02.07.13.24.42_xMode.md`） must remain the same in different labels in burst; otherwise the results might be wrong.

### Example（取自子主题 multiFFC）

```
RDI_BEGIN();
   rdi.emap("mffc").label("abc")
                   .pin("inA")
                   .multiFFC(0,100)
                   .execute();
   /* For smartVec():
   rdi.smartVec("mffc").label("abc")
                       .pin("inA")
                      .multiFFC(0,100)
                     .execute();
   */

RDI_END();

rdi.id("mffc").getMultiFFC();
```

### Syntax（取自子主题 passNode）

```
passNode();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 passNode）

```
RDI_BEGIN();
...
    rdi.smartVec...
    .insertJmpe(2).passNode().pin("DATA1").writeData(0x0,8,0)...execute();
...
RDI_END();
```

### Syntax（取自子主题 pMode）

```
pMode(int Pmode);
```

List of parameters
| Parameter | Description |
|---|---|
| Pmode | The number of tester cycles per device cycle. |

### Example（取自子主题 pMode）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").fillBit(1,4,2).pMode(2).execute();
  rdi.smartVec().pin("DATA3").readBit(4,2).pMode(2).execute();
  rdi.smartVec().pin("DATA5").writeData(0x54,8,4).pMode(4).execute();
  rdi.smartVec().pin("DATA7").readData(8,4).pMode(4).execute();
RDI_END();
```

### Syntax（取自子主题 pModeStrobe）

```
pModeStrobe(int strobePos);
```

List of parameters
| Parameter | Description |
|---|---|
| strobePos | The strobe position within pMode cycles. |

### Example（取自子主题 pModeStrobe）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA7").readData(8,4).pMode(4).pModeStrobe(3).execute();
RDI_END();
```

The following code illustrates the operation of pModeStrobe.

```
rdi.smartVec().pin("A").expectBit(arr).pMode(4).pModeStrobe(2).execute();
```

expect bit : 001-> LLH

vec: XLXXXHXXXHXX

### Syntax（取自子主题 readBit）

```
readBit(int bitLength,int startBit);
```

List of parameters
| Parameter | Description |
|---|---|
| bitLength | The length of the bits to be read |
| startBit | The starting position of the bits to be read. If the "startBit" parameter missing, the default value is 0. |

### Example（取自子主题 readBit）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").readBit(4,2).execute();
RDI_END();
```

### Syntax（取自子主题 readData）

```
readData(int bitLength,int startBit);
```

List of parameters
| Parameter | Description |
|---|---|
| bitLength | The length of the bits (data will be automatically converted into bits) to be read. |
| startBit | The starting position of the bits to be read. If the startBit parameter missing, the default value is 0. |

### Example（取自子主题 readData）

```
RDI_BEGIN();
  rdi.smartVec("result").pin("DATA1").readData(4,2).execute();
RDI_END();
...
ARRAY_LL data_result = rdi.id("result").getReadData("DATA1");
```

### Syntax（取自子主题 rdi.smartVec  .readMode）

```
readMode(TA::MEAS_TYPE mode);
```

List of parameters
| Parameter | Description |
|---|---|
| mode | The read mode. |

List of available options of parameter: <mode>
 |

Option

 |

Description

 |
 |

TA::EMAP

 |

The error map as the read mode.

In this mode, for each pin, the ERROR_MAP_TEST API is used to get all failed positions. A post processing is done afterward.

 |
 |

TA::DIGCAP

 |

The digital capture as the read mode.

In this mode, a dummy pattern with a digital capture variable is created. It cannot be mixed with the digCap() class inside a burstUpload-begin()/end() block.

   | Note The option TA::EMAP cannot be used together with a match loop in label.

### Example（取自子主题 rdi.smartVec  .readMode）

```
rdi.smartVec().readMode(TA::EMAP);

RDI_BEGIN();
  ...
  rdi.smartVec().pin("A").read...().execute();
  ...
RDI_END();
```

### Syntax（取自子主题 repeat）

```
repeat(int rptNum);
repeat(int rptNum, int vecSize, int startVec); // relevant only for the Vector class
```

List of parameters
| Parameter | Description |
|---|---|
| rptNum | The loop / repeat number. |
| vecSize | Only Vector class: Vector size. Used together with startVec to define the sector for repetition. |
| startVec | Only Vector class: Start vector. Used together with vecSize to define the sector for repetition. |

### Example 1（取自子主题 repeat）

```
// Have some content repeats in pattern, for example, clock signal
RDI_BEGIN();
rdi.port("clk").smartVec().pin("CLK").writePat("0,1,1").repeat(1000).execute();
RDI_END();
// readBit()/readData() with a huge number
RDI_BEGIN();
rdi.smartVec().pin("dout").readBit(10000).execute(); // original
RDI_END();
RDI_BEGIN();
rdi.smartVec().pin("dout").readBit(1).repeat(10000).execute();
RDI_END();
```

### Example 2（取自子主题 repeat）

```
RDI_BEGIN();
  rdi.smartVec()...repeat(5,10,2).repeat(4,5,20).execute();
  // add RPTV to 2 different segments of the pattern
RDI_END();
```

### Syntax（取自子主题 repeatSub）

```
repeatSub(int repeatNum);
```

List of parameters
| Parameter | Description |
|---|---|
| repeatNum | number of repeated subroutine calls. |

Return value

There is no return value.

### Example（取自子主题 repeatSub）

```
RDI_BEGIN();
    rdi.smartVec(). pin("DATA1").writeData(0x1,8,0)    // the content in the main pattern
       .insertSub(5).repeatSub(5).pin("DATA1").writeData(0x3,8,0).execute(); //  the content in sublabel 1, RPTJ 5, which is inserted in the main pattern
RDI_END();
```

With the above code, you add the target subroutine at the vector 5 for five times, as the figure below shows.

 !`repeatSub`（raw: `../../../../agent-html/152408.png`）

### Syntax（取自子主题 rdi.smartVec  .vecEditMode）

```
rdi.smartVec().vecEditMode(TA::Mode);
```

List of parameters
| Parameter | Description |
|---|---|
| TA::Mode | The mode to be used for one piece of pattern. |

List of available options of parameter: <TA::Mode>
| Option | Description |
|---|---|
| TA::VECD | The VECD firmware command mode, which calls the VECD FW command for vector editing. |
| TA::VTT | The VEC_TRANSFER_TASK API mode. |

### Example 1（取自子主题 rdi.smartVec  .vecEditMode）

To change the edit mode across `RDI_BEGIN()`/`RDI_END()` blocks:

```
rdi.smartVec().vecEditMode(TA::VECD);
RDI_BEGIN();
   ...
   rdi.smartVec() ... execute(); // Runtime editing
   ...
RDI_END();

rdi.smartVec().vecEditMode(TA::VTT);
RDI_BEGIN();
   ...
   rdi.smartVec() ... execute(); // Runtime editing
   ...
RDI_END();
```

### Example 2（取自子主题 rdi.smartVec  .vecEditMode）

To change edit mode inside the `RDI_BEGIN()`/`RDI_END()` block:

```
RDI_BEGIN();
    rdi.smartVec().vecEditMode(TA::VECD);
    rdi.smartVec()...;// run-time edit
    rdi.smartVec().vecEditMode(TA::VTT);
    rdi.smartVec()...;// run-time edit
RDI_END();
```

### Example 3（取自子主题 rdi.smartVec  .vecEditMode）

Use only the VTT mode for editing vectors when `copyLabel()`（raw: `02.07.13.24.06_copyLabel.md`） is used for the label.

```
rdi.smartVec().vecEditMode(TA::VTT);

RDI_BEGIN();
  rdi.smartVec().label("sLabel").copyLabel(false).pin(A)
                                .writeData("rt",8,0).execute();
  rdi.smartVec().label("sLabel").copyLabel(false).pin(A)
                                .writeData("rt",8,8).execute(); // a different position
RDI_END();
```

### Syntax（取自子主题 vecLength）

```
vecLength(int length);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

length

 |

The length of the pattern.

   | Note If the pattern contents exceed the length defined by the vecLength() parameter, the length of the generated pattern refers to the value of the vecLength() parameter. The overhang will be cut off.

### Example（取自子主题 vecLength）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").defaultVec(0).vecLength(10).execute();
RDI_END();
```

### Syntax（取自子主题 writeBit）

```
writeBit(ARRAY_I bitStream,int startBit);
writeBit(const string &sData, int startBit);  // application for runtime
writeBit(vector<ARRAY_I> perSiteBitStream, int startBit);
```

For pattern generation with bit streams per site, the sizes of all elements in ARRAY_I must be the same. The value for a site can be different from the value for another site. The values for all sites cannot be changed at runtime.

For more information about bits versus DVCs, see `Relationship between bits and device cycles`（raw: `02.07.13.24.01_Relationship_between_bits_and_device_cycles.md`）.

List of parameters
| Parameter | Description |
|---|---|
| bitStream | The bit stream to be written to the pattern. |
| sData | The sData of the parameter that can be changed at runtime. |
| startBit | The bit position in pattern, starting from which the specified bit stream or sData to be written on.<br><br>If the startBit parameter is not specified, the default value is 0. |
| perSiteBitStream | The bit stream per site. |

### Examples（取自子主题 writeBit）

```
...
ARRAY_I bitStream(4);
bitStream[0]=1;
bitStream[1]=0;
bitStream[2]=1;
bitStream[3]=1;

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeBit(bitStream,4).execute();
  rdi.smartVec().pin("DATA1").writeBit(bitStream).execute(); // The value of the "startBit" is 0.
RDI_END();
```

  Application for runtime

```
...
// This data type for writeBit() runtime
vector<ARRAY_I> runtime_vec_ARRAY_I;
//Initialize the array with required data
rdi.runTimeVal("string_runtime_vec_ARRAY_I", runtime_vec_ARRAY_I);

// This data type for writeBit() runtime
ARRAY_I runtime_ARRAY_I;
//Initialize the array with required data
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeBit("string_runtime_vec_ARRAY_I",2).execute();
  rdi.smartVec().pin("DATA3").writeBit("string_runtime_ARRAY_I",4).execute();
RDI_END();
```

   Pattern generation with per-site data

```
...
vector<ARRAY_I> perSiteBitStream_1,perSiteBitStream_2;
ARRAY_I dataBit(8);
dataBit[0] = 1;
...
RDI_BEGIN();
  rdi.smartVec().pin("DATA3").writeBit(perSiteBitStream_1,0).writeData(0x55,8,20).execute();
  ...
RDI_END();
ARRAY_I bitStream(20),bitStream_2(20);
...
perSiteBitStream_1.push_back(bitStream);
perSiteBitStream_2.push_back(bitStream_2);
...
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeBit(perSiteStream_1,0).defaultBit(0)
                .pin("DATA2").readData(4,0).execute();
    ...
RDI_END();
```

### Syntax（取自子主题 writeData）

```
writeData(long long data,int bitLength,int startBit);
writeData(const string &sData, int bitLength, int startBit); // application for runtime
writeData(ARRAY_LL perSiteData, int bitLength, int startBit); // values for all sites must be different each other and cannot be changed at runtime
```

List of parameters
| Parameter | Description |
|---|---|
| data | The data block you want to write to the pattern. |
| bitLength | The length of the bits (data will be automatically converted into bits) to be written. |
| sData | The sData of the parameter that can be changed at runtime. |
| startBit | The starting position of the bits to be written. If the startBit parameter is not specified, the default value is 0. |
| perSiteData | The array of data. |

### Example（取自子主题 writeData）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeData(0x54,8,4).execute();
rdi.smartVec().pin("DATA3").writeData(0x54,8).execute();  // the value of the "startBit" is 0.
RDI_END();

// application for runtime
static int runtime=0;
ARRAY_I runtime_ARRAY_I;     // this data type for writeData() runtime is supported
ARRAY_LL runtime_ARRAY_LL;   // this data type for writeData() runtime is supported
int runtime_int;// this data type for writeData() run-time is supported
long long runtime_longlong;  // this data type for writeData() runtime is supported
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);
rdi.runTimeVal("string_runtime_ARRAY_LL", runtime_ARRAY_LL);
rdi.runTimeVal("string_runtime_int", runtime_int);
rdi.runTimeVal("string_runtime_longlong", runtime_longlong);

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeData("string_runtime_ARRAY_I",8,2).execute();
  rdi.smartVec().pin("DATA3").writeData("string_runtime_ARRAY_LL",8,4).execute();
  rdi.smartVec().pin("DATA5").writeData("string_runtime_int",4,2).execute();
  rdi.smartVec().pin("DATA7").writeData("string_runtime_longlong",64,4).execute();
RDI_END();

// Pattern generation with different data per site.
ARRAY_LL Data(4);  // four sites are used
Data[0]=1;
Data[1]=2;
Data[2]=3;
Data[3]=4;

RDI_BEGIN();
  rdi.smartVec().pin("DATA2").writeData(Data,4).execute();
RDI_END();
```

### Syntax（取自子主题 writeDataBurst）

```
writeDataBurst(ARRAY_I data, ARRAY_I bitLength, ARRAY_I startBit);
writeDataBurst(ARRAY_I data, int bitLength, int bitDistance, int startBit);
writeDataBurst(ARRAY_I data, int bitLength); // startBit =0,bitDistance=bitLength
writeDataBurst(ARRAY_LL data, ARRAY_I bitLength, ARRAY_I startBit);
writeDataBurst(ARRAY_LL data, int bitLength, int bitDistance, int startBit);
writeDataBurst(ARRAY_LL data, int bitLength); // startBit =0,bitDistance=bitLength
```

List of parameters
| Parameter | Description |
|---|---|
| data | The array of data you want to write to the pattern. |
| bitLength | The length of the bits (data will be automatically converted into bits) to be written. |
| bitDistance | The bit distance between one data and the next data. |
| startBit | The starting position of the bits to be written. If the startBit parameter missing, the default value is 0. |

### Example（取自子主题 writeDataBurst）

```
ARRAY_I array_data_1(4); // data array
array_data_1[0]=0x1;
array_data_1[1]=0x23;
array_data_1[2]=0x456;
array_data_1[3]=0x7890;
ARRAY_I bitLength(4);   // bitLength array
bitLengt[0]=4;
bitLengt[1]=8;
bitLengt[2]=12;
bitLengt[3]=16;
ARRAY_I startBit(4);   // startBit array
startBit[0]=0;
startBit[1]=4;
startBit[2]=12;
startBit[3]=24;
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeDataBurst(array_data_1,bitLength,startBit).execute();
RDI_END();
ARRAY_I array_data_2(4);
array_data_2[0]=0x12;
array_data_2[1]=0x34;
array_data_2[2]=0x56;
array_data_2[3]=0x78;
RDI_BEGIN();
rdi.smartVec().pin("DATA3").writeDataBurst(array_data_2,8,4).execute(); // the default value of "startBit" is 0
rdi.smartVec().pin("DATA5").writeDataBurst(array_data_2,8).execute();   // startBit=0,bitDistance=bitLength
RDI_END();
```

### Syntax（取自子主题 writeParData）

```
writeParData(long long Data, int startBit);
writeParData(const string &sData, int startBit); // application for runtime
writeParData(ARRAY_LL perSiteData, int startBit);
```

For pattern generation with different data per site, values for all sites must be different each other and cannot be changed at runtime.

List of parameters
| Parameter | Description |
|---|---|
| data | The array of data you want to write to the pattern. |
| sData | The sData of the parameter that can be changed at run-time. |
| startBit | The starting position of the bits to be written. If the startBit parameter is not specified, the default value is 0. |
| perSiteData | The array of data. |

### Example（取自子主题 writeParData）

```
// 11(Dec) = 1011(Bin), "1011" will be assigned into the four pins successively,
// DATA1=1,DATA3=0,DATA5=1,DATA7=1
// 6(Dec) = 110(Bin), "110" will be assigned into the three pins successively,
// DATA9=1,DATA11=1,DATA13=0
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParData(11,4).execute();
rdi.smartVec().pin("DATA9,DATA11,DATA13").writeParData(6,4).execute();
RDI_END();

//application for runtime
static int runtime=0;
ARRAY_I runtime_ARRAY_I(4);//parallel data array, this data type for writeParData() run-time is supported
ARRAY_LL runtime_ARRAY_LL(4);//parallel data array, this data type for writeParData() run-time is supported
int runtime_int;//this data type for writeParData() run-time is supported
long long runtime_longlong;//this data type for writeParData() run-time is supported
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);
rdi.runTimeVal("string_runtime_ARRAY_LL", runtime_ARRAY_LL);
rdi.runTimeVal("string_runtime_int", runtime_int);
rdi.runTimeVal("string_runtime_longlong", runtime_longlong);
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParData("string_runtime_ARRAY_I",2).execute();
rdi.smartVec().pin("DATA9,DATA11,DATA13,DATA15").writeParData("string_runtime_ARRAY_LL",4).execute();
rdi.smartVec().pin("DATA17,DATA19,DATA21,DATA23").writeParData("string_runtime_int",6).execute();
rdi.smartVec().pin("DATA25,DATA27,DATA29,DATA31").writeParData("string_runtime_longlong",8).execute();
RDI_END();

// Pattern generation with different data per site.
ARRAY_LL perSiteData(4);  // four sites are used
...
RDI_BEGIN();
  rdi.smartVec().pin("GP").writeParData(perSiteData).execute();
RDI_END();

```

### Syntax（取自子主题 writeParDataBurst）

```
writeParDataBurst(ARRAY_I data, int bitDistance, int startBit);
writeParDataBurst(ARRAY_I data); // bitDistance=1, startBit=0
writeParDataBurst(ARRAY_LL data, int bitDistance, int startBit);
writeParDataBurst(ARRAY_LL data);// bitDistance=1, startBit=0
```

List of parameters
| Parameter | Description |
|---|---|
| data | The array of data you want to write to the pattern. |
| bitDistance | The bit distance between one data and the next data. |
| startBit | The starting position of the bits to be written. If the startBit parameter missing, the default value is 0. |

### Example（取自子主题 writeParDataBurst）

```
ARRAY_I I_ParDataBurst(4); // parallel data array
I_ParDataBurst[0]=0x01;
I_ParDataBurst[1]=0x05;
I_ParDataBurst[2]=0x09;
I_ParDataBurst[3]=0x0B;
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(I_ParDataBurst,2,4).execute();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(I_ParDataBurst).execute();
RDI_END();
ARRAY_LL LL_ParDataBurst(4); // parallel data array
LL_ParDataBurst[0]=0x01;
LL_ParDataBurst[1]=0x05;
LL_ParDataBurst[2]=0x09;
LL_ParDataBurst[3]=0x0B;
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(LL_ParDataBurst,2,4).execute();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(LL_ParDataBurst).execute();
RDI_END();
```

### Syntax（取自子主题 writePat）

```
writePat(const string &dvc,int startVec);
```

List of parameters
| Parameter | Description |
|---|---|
| dvc | The device cycle you want to write into the pattern. |
| startVec | The starting position of the vector to be written. If the startVec parameter missing, the default value is 0. |

### Example（取自子主题 writePat）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writePat("0,1,Z,Z,H",1).execute();
RDI_END();
```

### Syntax（取自子主题 writeVec）

```
writeVec(vector<string> dvcList, int startVec);
writeVec(ARRAY_I indexList, int startVec);
writeVec(const string &sData, int startVec); // application for runtime
writeVec(vector<ARRAY_I> perSiteIndex, int startVec);
writeVec(vector<vector<string>> perSiteDvc, int startVec);
```

For pattern generation with per-site data, the sizes of all elements in ARRAY_I or vector<string> must be the same. The value for a site can be different from the value for another site. The values for all sites cannot be changed at runtime.

List of parameters
| Parameter | Description |
|---|---|
| dvcList | The device cycle list you want to write to the pattern. |
| indexList | The physical index list you want to write to the pattern. |
| sData | The sData of the parameter that can be changed at runtime. |
| startVec | The starting position of the vector to be written. If the startVec parameter is not specified, the default value is 0. |
| perSiteIndex | The index list per site. |
| perSiteDvc | The device cycle list per site. |

### Examples（取自子主题 writeVec）

```
vector<string> dvcList;
dvcList.push_back("1"); // device cycle
dvcList.push_back("0");

ARRAY_I indexList(3);
indexList[0]=0;         // physical index
indexList[1]=1;
indexList[2]=2;
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeVec(dvcList,1).execute();   // dvcList
  rdi.smartVec().pin("DATA3").writeVec(indexList,4).execute(); // indexList
RDI_END();
```

  Application for runtime

```
vector<ARRAY_I> runtime_vec_ARRAY_I;  // this data type for writeData() runtime is supported
rdi.runTimeVal("string_runtime_vec_ARRAY_I", runtime_vec_ARRAY_I);

// This data type for writeData() run-time is supported
ARRAY_I runtime_ARRAY_I;
//Initialize the array with required data
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeVec("string_runtime_vec_ARRAY_I",2).execute();
  rdi.smartVec().pin("DATA3").writeVec("string_runtime_ARRAY_I",4).execute();
RDI_END();
```

   Pattern generation with per-site data

```
// The sizes of ARRAY_I index1, index2, index3, and index4 must be the same:
ARRAY_I index1(8), index2(8), index3(8), index4(8);
vector<ARRAY_I> perSiteIndex;
perSiteIndex.push_back(index1);
...
RDI_BEGIN();
  rdi.smartVec().pin("A").writeVec(perSiteIndex,2).execute();
RDI_END();
```

```
...
vector<string> vec_s;
vec_s.push_back("0");
vec_s.push_back("1");
vec_s.push_back("0");
vec_s.push_back("1");

vector<string> vec_s1;
vec_s1.push_back("1");
vec_s1.push_back("0");
vec_s1.push_back("1");
vec_s1.push_back("0");

vector<vector<string> > vec_vec_s;
vec_vec_s.push_back(vec_s);
vec_vec_s.push_back(vec_s1);
vec_vec_s.push_back(vec_s);
vec_vec_s.push_back(vec_s1);

RDI_BEGIN();
  rdi.smartVec().pin("DATA1").writeVec(vec_vec_s).execute();
RDI_END();
```

### Syntax（取自子主题 xMode）

```
xMode(int Xmode);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

Xmode

 |

The number of device cycles in each tester cycle.

   |   Note

- The fail count and fail position are about "compare edge" (not tester cycle). So they supports xMode directly.
- The xMode parameter for a pin must be correct, otherwise the result for the pin will not be correct.
- The parameter specified in the function, such as startCyc and cycRange, is about user cycles (edge), not tester cycles. This setting is critical when xMode is set to be greater than 1.
- For one pin, the xMode must remain the same in different labels in burst; otherwise the results might be wrong.
 Note For correctly retrieving the results of error map data:

- For a specified pin, in one RDI_BEGIN/RDI_END block, its xMode number must remain the same value, no matter it is for a SmartRDI command or in the user pattern.
- In the wavetable, the length of the device cycle name must align with the xMode() value. For example, if you set xMode to xMode(2), the dvc must correspondingly have two letters, such as "LL", "00", "11", "LL". Even the dvc of the physical index f, which normal value is "." with SmartRDI, must be ".." for xMode(2). Otherwise SmarTest cannot recognize the correct xMode value from pattern.

### Example（取自子主题 xMode）

```
RDI_BEGIN();
  rdi.smartVec().pin("DATA1").fillBit(1,4,2).xMode(2).execute();
  rdi.smartVec().pin("DATA3").readBit(4,2).xMode(2).execute();
  rdi.smartVec().pin("DATA5").writeData(0x54,8,4).xMode(4).execute();
  rdi.smartVec().pin("DATA7").readData(8,4).xMode(4).execute();
RDI_END();
```

Data from `readBit()`（raw: `02.07.13.24.28_readBit.md`）, `readData()`（raw: `02.07.13.24.29_readData.md`）, `expectBit()`（raw: `02.07.13.24.12_expectBit.md`）, or `expectData()`（raw: `02.07.13.24.13_expectData.md`） can cross over device cycles.

```
RDI_BEGIN();
  rdi.smartVec().pin("A").expectData(0,4,1).defaultBit(0)
                         .xMode(2).bitLength(8)
                         .execute();
RDI_END();
```

The result vector:

 !`xMode crossover borders`（raw: `../../../../agent-html/151539.png`）

Supporting a string from `fillBit()`（raw: `02.07.13.24.18_fillBit.md`） and `defaultBit()`（raw: `02.07.13.24.07_defaultBit.md`）.

```
RDI_BEGIN();
  rdi.smartVec().pin("A").defaultBit(0).fillBit("p",4,1)
                         .xMode(2).bitLength(6)
                         .execute();
RDI_END();
```

The result vector:

 !`string_support by fillbit and defaultBit`（raw: `../../../../agent-html/151540.png`） Note You must define device cycle names in the corresponding wavetable.

### Syntax（取自子主题 getFailCount）

```
int getFailCount(string pin);
```

List of parameters
| Parameter | Description |
|---|---|
| pin | Specifies a pin for which to get the fail count. |

### Return value（取自子主题 getFailCount）

The return value is an integer indicating the number of errors.

### Example（取自子主题 getFailCount）

```
ON_FIRST_INVOCATION_BEGIN();

  RDI_BEGIN();
    rdi.smartVec("a").pin("pA").writePat("0,1,1,H,H,H,L").failCount().execute();
  RDI_END();

ON_FIRST_INVOCATION_END();

int fcount=rdi.id("a").getFailCount("pA");
```

### Syntax（取自子主题 getFailCyc）

```
ARRAY_LL getFailCyc(string pin);
```

List of parameters
| Parameter | Description |
|---|---|
| pin | Specifies a pin for which to get all failing cycles' positions. |

### Return value（取自子主题 getFailCyc）

The return value is an ARRAY_LL indicating all failing cycles' positions.

### Syntax（取自子主题 getFFC）

```
int getFFC(string pin);
```

List of parameters
| Parameter | Description |
|---|---|
| pin | Specifies a pin for which to get the first failing cycle. |

### Return value（取自子主题 getFFC）

The return value is an integer indicating the first failing cycle.

### Syntax（取自子主题 rdi.id  .getMultiFFC）

```
ARRAY_LL getMultiFFC(string pin);
ARRAY_LL getMultiFFC(); // if only one result pin exists.
```

List of parameters
| Parameter | Description |
|---|---|
| pin | The pin for which to retrieve the number of failing cycles. |

### Example（取自子主题 rdi.id  .getMultiFFC）

```
RDI_BEGIN();
   rdi.emap("mffc").label("abc")
                   .pin("inA")
                   .multiFFC(0,100)
                   .execute();
RDI_END();

rdi.id("mffc").getMultiFFC();
```

### Syntax（取自子主题 getReadBit）

```
ARRAY_I getReadBit(const string &pin);
```

List of parameters
 |

Parameter

 |

Description

 |
 |

pin

 |

The pin to query.

   | Note If the pin parameter is missing, the default pin will be used.

### Example（取自子主题 getReadBit）

```
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
rdi.smartVec("result").pin("DATA1").readBit(4,2).execute();
RDI_END();
ON_FIRST_INVOCATION_END();
ARRAY_I bit_result = rdi.id("result").getReadBit("DATA1");
```

### Syntax（取自子主题 getReadData）

```
ARRAY_LL  getReadData(const string &pin);
```

List of parameters
| Parameter | Description |
|---|---|
| pin | The pin to query. |

### Example（取自子主题 getReadData）

```
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
   rdi.smartVec("result").pin("DATA1").readData(4,2).execute();
RDI_END();
ON_FIRST_INVOCATION_END();
ARRAY_LL data_result = rdi.id("result").getReadData("DATA1");
```

### Syntax（取自子主题 Match loop support › Inserting MACT and MRPT in a smartVec label › instruction）

```
instruction(string instruct, int vecPos);
```

List of parameters
| Parameter | Description |
|---|---|
| instruct | An MACT X, MACT X CONTINUE, or MRPT X instruction to be inserted.<br><br>"X" presents an integer number for the loop repetitions. |
| vecPos | The starting vector position from which MACT or MRPT to be inserted. |

### Example（取自子主题 Match loop support › Inserting MACT and MRPT in a smartVec label › instruction）

```
rdi.smartVec().pin("DATA1")
    .writePat("X,X,H,L,H,L",8)
    .defaultVec("X")
    .vecLength(20)
    .instruction("MACT 6",8)
    .instruction("MRPT 6",14)
    .execute();
```

With a CONTINUE option for the MACT instruction, the sequencer program continues even if the match loop has failed:

```
rdi.smartVec().pin("DATA1")
    .writePat("X,X,H,L,H,L",8)
    .instruction("MACT 6 CONTINUE",8)
    .instruction("MRPT 6",14)
    .execute();
```

### Syntax（取自子主题 Match loop support › Creating a match loop pattern from logical data › matchBit）

```
matchBit(ARRAY_I bitStream,int startBit,int maxLoopNum)
```

List of parameters
| Parameter | Description |
|---|---|
| bitStream | The bit stream to be written to the vector. |
| startBit | The starting position of the vector to be included in the match loop. |
| maxLoopNum | The maximum number of loops to be executed. |

### Syntax（取自子主题 Match loop support › Creating a match loop pattern from logical data › matchCycle）

```
matchCycle(int cycle);
```

List of parameters
| Parameter | Description |
|---|---|
| cycle | The number of waiting cycles between matches. |

### Example（取自子主题 Match loop support › Creating a match loop pattern from logical data › matchCycle）

```
rdi.smartVec().pin("DATA1").defaultBit(0).matchData(0x36,8,10,6).matchCycle(8).execute();
```

### Syntax（取自子主题 Match loop support › Creating a match loop pattern from logical data › matchData）

```
matchData(long long data,int bitLength,int startBit,int maxLoopNum)
matchData(long long data,int bitLength,int startBit,int maxLoopNum,TA::MATCH_CONT)
```

List of parameters
| Parameter | Description |
|---|---|
| bitLength | The number of vectors to be included in the match loop. |
| startBit | The starting position of the bit to be written in the match loop. |
| maxLoopNum | The maximum number of the loops to be executed. |
| TA::MATCH_CONT | An option parameter which presents CONTINUE for the MACT instruction. |

### Examples（取自子主题 Match loop support › Creating a match loop pattern from logical data › matchData）

### defaultBit

```
rdi.smartVec().pin("DATA1").defaultBit(0).matchData(0x36,8,10,6).matchCycle(8).execute();
```

### matchData

```
rdi.smartVec().pin("DATA1").matchData(0x36,8,10,6,TA::MATCH_CONT).matchCycle(8).execute();
```

### Example（取自子主题 Match loop support › Retrieving match loop results）

```
RDI_BEGIN();
 rdi.smartVec("abc").pin("pinA").defaultBit(0)
             .matchData(0x36,8,10).matchCycle(10)
             .readMatchCount("pinA")
             .readMatchPassFail("pinA").execute();
RDI_END();
 int pf = rdi.id("abc").getMatchPassFail();
 int cnt= rdi.id("abc").getMatchCount();
```

<!-- 语法节 end -->

## 是什么

**本页是 SmartRDI 里那个「生成 vector 和 pattern」的类的总览页。**

原文两句话定范围：

> 「The SmartRDI **Vector class** supports the **generation of vector and patterns with simple
> commands**. It provides an easy way to **read digital outputs of a device**.」

**两个方向都管**：**写 pattern 出去** + **把 device 的数字输出读回来**。

### 七条能力清单（原文逐条列的就是这七条）

原文 `The typical vector and pattern operations you can perform using the smart vector class are
listed below`：

| # | 能力 | 原文 |
|---|---|---|
| 1 | **三种数据输入方式** | `3 different data input options for the pattern creation (**data block, bit stream, vector stream**)` |
| 2 | **自动处理 x mode 和 1/x mode** | `Automatic handling of the x mode and 1/x mode` |
| 3 | **结构化 burst 数据的 pattern** | `Creation of patterns with **structured burst data**` |
| 4 | **多 port 的并行数据 burst** | `Creation of patterns with a **parallel data burst for multiple ports**` |
| 5 | **大 pattern**（一串建 pattern 的命令拼出来） | `Creation of **big patterns** for a series of pattern creation commands` |
| 6 | **取数据有两种方式，为的是省测试时间** | `Data retrieval is handled in different ways for test time optimization (**digital capture and error map**)` |
| 7 | **多次取数时把 upload 次数压到最少** | `The number of upload actions is **minimized** in case of multiple data retrievals` |

**读这张表要抓的两件事：**

> **① 第 1 条是「三选一」，不是三个都要用。**
> `data block` / `bit stream` / `vector stream` ——**它们是同一件事的三条路径**，
> 原文没有说什么时候用哪条。
>
> **② 第 6 和第 7 条是一组，讲的是「读回来」那一侧。**
> **取数据有两种机制**（digital capture / error map），
> **而第 7 条是针对「要读很多次」做的优化**——两次 upload 会浪费时间。

### 三个「层」——本页对结构唯一的说明

> 「The vector generation class provides APIs and commands for different **"layers"**:
> **Vector layer, stream layer and data block layer**.」

**原文只列了这三个名字，没有解释任何一层是干什么的。**

但这一句和上面第 1 条对得上：

| 层 | 和第 1 条的关系（**（推断）**） |
|---|---|
| **data block layer** | 对应第 1 条的 `data block` |
| **stream layer** | 对应第 1 条的 `bit stream` / `vector stream` |
| **Vector layer** | 最高层，本页的类就叫 `Vector class` |

> **（推断）的依据**：三层名字里的两个（`data block` / `vector`）和「三种输入方式」
> 里的两个**同名**。**原文没有把这层对应关系写出来**，
> **本页不把它当成事实**——只知道两层命名重合。

### 语法节里的东西：**这一页的正文全在脚本那一节里**

本页 `## 语法 / 参数` 一节有 **3000 行上下**，因为主文档的 `Subtopics` 有 **49 篇**，
脚本把它们的 `Syntax` / `Example` 逐字抄了进来——`bitLength()`、`burstLabel()`、
`burstUpload()`、`comment()`、`copyLabel()`、`defaultBit()`、`download()`、
`emapLocation()` 等等。

**所以这一页的读法是反的**：
**散文这一节只有「定位」，真正的用法在脚本那一节**——而且那一节**逐字来自 49 篇本页没读的子主题**。

## 典型用法

**原文这篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**，
也没有任何步骤。**本页按原文能支撑的内容列三条：**

**1. 选输入方式**（原文只给了名字，没给选择标准）：

| 方式 | 本页对它的了解 |
|---|---|
| **data block** | **只知道名字**（对应 `data block layer`） |
| **bit stream** | **只知道名字** |
| **vector stream** | **只知道名字** |

**2. 取数据**（两种机制）：

| 机制 | 本页对它的了解 |
|---|---|
| **digital capture** | **只知道名字** |
| **error map** | **只知道名字**（allowlist 里另有 `error-map` 页） |

> **原文对这两种机制的唯一说明是「for test time optimization」**——
> **即它们是性能上的两条路，不是能力上的两条路**（**（推断）**：
> 依据是原文那句话把两者并列在 `test time optimization` 之下）。

**3. 要读很多次的时候**：原文第 7 条明说
`The number of upload actions is minimized in case of multiple data retrievals`
——**即「多次取数」是被专门优化过的场景**，**但怎么优化、API 叫什么，原文没写**。

**4. 有一个特例**：`Subtopics` 里第 49 篇是
`Match loop support`（**本页未读**）——**它是 49 篇里唯一不是方法名的一篇**，
说明 match loop 和这些方法是**并列的一块支持**，不是其中一个方法。
**（推断）**依据是它在清单里的位置和命名方式。

## 和谁有关

- [[smartrdi]] — 本页的上层入口；**本页是它下面「vector 与 protocol 编程」这一支**
- [[pattern]] / [[pattern-object]] / [[pattern-master-file]] — **本页生成的 pattern 落在这些页描述的体系里**；
  **本页讲的是「用 API 建 pattern」，不是 pattern 文件格式**
- [[vector-setup-file]] — vector 的文件侧；**本页是 API 侧，两者原文没说关系**
- [[waveform-mapping]] — 波形映射；**SmartRDI 发的 vector 最终要落到波形上**，
  **但本页没提这件事**
- [[match-loops]] — **`Subtopics` 第 49 篇就是 `Match loop support`**，
  说明 wiki 里已有一页讲 match loop；**本页没读它，也没读子主题那篇**
- [[event-waveform-vfim]] / [[event-waveform-vfvm]] — 另两种波形事件；
  **和本页同属「往 device 发东西」这一侧，但本页没提它们**
- [[smartrdi-2.3.0]] — **本页 `Functional changes` 里唯一那条对应的版本页**
- `Relationship between bits and device cycles` / `bitLength()` / `burstLabel()` /
  `burstUpload()` / `comment()` / `copyLabel()` / `defaultBit()` / `defaultVec()` /
  `download()` / `emapLocation()` / `enPassFail()` / `expectBit()` / `expectData()` /
  `failCount()` / `failCyc()` / `failNode()` / `FFC()` / `fillBit()` / `fillVec()` /
  `insertJmpe()` / `insertSub()` / `label()` / `labelName()` / `multiFFC()` / `passNode()` /
  `pMode()` / `pModeStrobe()` / `readBit()` / `readData()` / `rdi.smartVec().readMode()` /
  `repeat()` / `repeatSub()` / `rdi.smartVec().vecEditMode()` / `vecLength()` / `writeBit()` /
  `writeData()` / `writeDataBurst()` / `writeParData()` / `writeParDataBurst()` /
  `writePat()` / `writeVec()` / `xMode()` / `getFailCount()` / `getFailCyc()` / `getFFC()` /
  `rdi.id().getMultiFFC()` / `getReadBit()` / `getReadData()` / `Match loop support`
  （**均未建**）— **本页 `Subtopics` 的 49 篇，本页一篇没读**；
  **本页语法节里那 3000 行就是它们被脚本抽出来的片段**

## 版本

- **Introduced in SmartRDI 2.3.0**

> **注意这条不是 SmarTest 版本，是 SmartRDI 版本**——本页是这一批页里少数
> 版本号走 SmartRDI 自己序列的（对照 [[smartrdi-2.3.0]] 那一页）。
> **原文 `## Functional changes` 只有这一条，没有后续版本条目。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.13.24_SmartRDI__Vector_and_protocol_programming.md`

**本页没做的**：

- **`Subtopics` 的 49 篇一篇没读**——**这是本页最大的缺口，而且缺口是本页正文的几十倍。**
  本页主文档只有 7 条能力清单 + 一句「三个层」，**而 49 个方法的签名、参数、例子
  全在那 49 篇里**。所以本页**只有定位，没有任何一个方法的用法**。
- **`## 语法 / 参数` 一节里的 3000 行，本页一条都没有验证过。**
  它们由脚本从 49 篇子主题逐字抄出，**本页没读那些子主题**，
  所以无法判断：**同一方法的多次出现是否重复、`Example` 的上下文有没有缺、
  子主题之间的先后顺序有没有含义**。
- **「Vector layer / stream layer / data block layer」到底是哪一层调用哪一层，原文没写，本页也不知道。**
- **`x mode` 和 `1/x mode` 是什么，原文没解释**——只说了「自动处理」。
- **「structured burst data」的结构是什么样的，原文没写。**
- **图零张**（原文这篇没有图）。
- **原文没有 `## Procedure` / `## Before you begin` / `## What to do next` /
  `## Related information`**——四个都没有。**所以「典型用法」一节里
  除了「有三条路可选」之外没有内容可写。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`Subtopics` 的 49 篇里，最后一个不是方法名**——
> 前 48 篇都是 `xxx()` 形式的方法名，第 49 篇是 `Match loop support`（一句话）。
> **它混在同一张清单里，没有任何标记说它不一样。**
> ② **`rdi.smartVec().readMode()` 和 `rdi.smartVec().vecEditMode()`
> 两个子主题的标题里带点号**，写成了
> `02.07.13.24.30_rdi.smartVec__.readMode.md`（**点号被替换成下划线**），
> 和其余 47 篇的命名规则不同。
> ③ **`FFC()` 和 `multiFFC()` / `getFFC()` / `rdi.id().getMultiFFC()` 是三组不同的名字**，
> 而正文七条能力里**没有一条提到 FFC**——**它们只在 `Subtopics` 里出现。**
> ④ **原文第一句 `The SmartRDI Vector class` 用的是 `Vector` 大写**，
> 而七条清单那一句用的是 `the smart vector class`（**小写 `smart vector`**）
> ——**同一个类在同一页里两种写法。**

`verified: doc-only`
