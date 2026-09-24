---
type: object
title: LotSummaryGenerator
layer: L1
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# LotSummaryGenerator

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,883 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.07_LotSummaryGenerator.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Executing the LotSummaryGenerator in the command line

The following example generates the lot summary for the specified data collection file. The output file is /tmp/LotSummary.out. The log file LotSummrayGenerator.log is generated under the home directory of the current user.

```
/opt/hp93000/soc/formatter/bin/LotSummaryGenerator -d /var/opt/hp93000/soc/tm/93k.iI3eAe/DataColltion.
```

### Using LOT_SUMMNARY_PATH_NAME in the application model

```
...
{ lot:
         SCREEN_DIALOG
             Lot_id  = DIALOG_INPUT    /REGEXP(string);

        ACTIONS
            LOT_SUMMARY_PATH_NAME = CONST_INPUT(/tmp/{Lot_id}.lotSum.gdf);
}
...
```

### Using FORCE_SUMMARY_GENERATION_FOR_LEVEL in the application model

In the following example, the summary is generated at `point #1`. If FORCE_SUMMARY_GENERATION_FOR_LEVEL is not used, the lot summary is generated at `point #2`. Make sure to specify the current level name to FORCE_SUMMARY_GENERATION_FOR_LEVEL and put the variable in the post actions section of the level.

```
...
{ lot:
        ACTIONS
              ...
         {DEVICE device:
                      {
                               DEVICE_TEST
                       }
          }

           ACTIONS
                  FORCE_SUMMARY_GENERATION_FOR_LEVEL = CONST_INPUT(lot);
                   --point #1
                   EXEC_INP_CALL(process_lot_summary_file);
                  ...
}   --point #2
...
```

### Using ENABLE_LOT_SUMMARY_GENERATOR in the application model

In this example, ENABLE_LOT_SUMMARY_GENERATOR is used to enable the LotSummaryGenerator. The LotSummaryGenerator will be started at the beginning of the application model execution.

```
...
{ lot:
      SCREEN_DIALOG
          Lot_id  = DIALOG_INPUT    /REGEXP(string);
      ACTIONS
            ENABLE_LOT_SUMMARY_GENERATOR = CONST_INPUT(1);
}
...
```

### Using LotSummaryGenerator with BLC program

```
//header file
...
using namespace std;
using namespace xoc::hvmapi;
pid_t LSGPid = 0;
...
//Define the function to start the LotSummaryGenerator
void startLotSummaryGenerator()
{
  LSGPid = fork();

  if(LSGPid == 0)
  {
      execl("/opt/hp93000/soc/formatter/bin/LotSummaryGenerator", 0);
  }

}

//Define the function to terminate the LotSummaryGenerator
void terminateLotSummaryGenerator()
{
  int childStatus;

  if(LSGPid > 0)
  {
    sleep(5);
    kill(LSGPid, 9);
    waitpid(LSGPid, &childStatus, 0);
  }
}
...
int main(int argc, char* argv[])
{
  ParamList inputParam, outputParam;
  Status  retVal;

 /**********************
  * Initialize the BLC *
  **********************/
  //check if there are input file provided
  if(argc<=1)
  {
    cout<<"Please sepecify a BLC input file!!!"<<endl;
    cleanup();
    exit(1);
  }

  startLotSummaryGenerator();
  ...
  /***********************
  * Start the lot level *
  ***********************/
  inputParam.clear();
  inputParam["LEVEL_TYPE"] = "CUSTOM_LEVEL";
  inputParam["LEVEL_NAME"] = "lot";
  retVal = syncCommand("StartLevel", inputParam, LOCAL_SESSION_ID);
  processStatus(retVal);

  for(int lotNum=1; lotNum<=1; lotNum++)
  {
    ...
    //Add new variable LOT_SUMMARY_PATH_NAME for LotSummaryGenerator
    inputParam.clear();
    inputParam["VARIABLE_NAME"] = "LOT_SUMMARY_PATH_NAME";
    inputParam["VARIABLE_VALUE"] = string("/tmp/")+lotID+string(".lotSum.gdf");
    retVal = syncCommand("SetApplicationVar", inputParam, LOCAL_SESSION_ID);
    processStatus(retVal);
    ...
    //Add new variable FORCE_SUMMARY_GENERATION_FOR_LEVEL for LotSummaryGenerator
    inputParam.clear();
    inputParam["VARIABLE_NAME"] = "FORCE_SUMMARY_GENERATION_FOR_LEVEL";
    inputParam["VARIABLE_VALUE"] = string("lot");
    retVal = syncCommand("SetApplicationVar", inputParam, LOCAL_SESSION_ID);
    processStatus(retVal);
  } //end of the lot level loop
  terminateLotSummaryGenerator();
  cleanup();
  return 0;
}
```

<!-- 语法节 end -->

## 是什么

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
