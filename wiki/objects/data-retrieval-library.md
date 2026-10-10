---
type: object
title: Data Retrieval Library
layer: L2
stage: results
tags: [drl, data-retrieval-library, c-api, data-log-stream, event-records, drl-data-types, offline-analysis, results]
related: [event-formatter, edl-file, edf, error-map, smartest-6.3.2]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.04_Data_Retrieval_Library.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Data Retrieval Library

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **19,733 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.04_Data_Retrieval_Library.md>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.01.04.01.01_DRLEventAvailable.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.02_DRLEventGetAttribute.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.03_DRLEventGetFirstAttributeByType.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.04_DRLEventGetNextAttributeByType.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.05_DRLEventGetNoOfAttributes.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.06_DRLEventGetType.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.07_DRLFreeEvent.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.08_DRLGetEventMask.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.09_DRLGetNextUnmaskedEvent.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.10_DRLKeepEvent.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.11_DRLNumberOfPinGroups.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.12_DRLNumberOfPins.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.13_DRLNumberOfSites.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.14_DRLPinGroupIndexToName.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.15_DRLPinGroupIndexToPins.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.16_DRLPinGroupNameToIndex.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.17_DRLPinIndexToChannel.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.18_DRLPinIndexToName.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.19_DRLPinIndexToNumber.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.20_DRLSave.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.21_DRLSetEventMask.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.22_DRLStart.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.23_DRLStop.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.24_DRLTruncate.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.03_DRLAttributeRec.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.05_DRLBankSpecificCounts.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.08_DRLBitFailMapDescAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.15_DRLErrorMapAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.16_DRLErrorOverviewAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.17_DRLEventMask.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.22_DRLFailingAddressCountAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.23_DRLFailingAdresses.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.24_DRLFailingAddressesAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.29_DRLLabelDescriptorAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.30_DRLLabelListAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.42_DRLPatternLabelAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.51_DRLPinSpecificAddresses.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.52_DRLPinSpecificCounts.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.53_DRLPinType.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.60_DRLRARepairResult.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.61_DRLRARepairResultsAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.62_DRLResultPinName.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.63_DRLScanInstanceDescriptorAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.64_DRLScanInstanceListAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.65_DRLShmooAxisData.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.72_DRLShmooHXInstrumentType.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.73_DRLShmooHXResourceType.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.75_DRLShmooSpecVariableType.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.77_DRLShmooTestCellAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.78_DRLShmooTestCellData.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.79_DRLShmooTestInfoAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.80_DRLShmooUserDefinedParamType.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.83_DRLSiteSetAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.86_DRLTestConditionAttr.md>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.87_DRLTestCondition.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Return Value（取自子主题 DRL functions › DRLEventAvailable）

For the data log stream, non-zero is returned if a new event record is ready to be read. This allows you to treat the result value as true if a new record is ready and false if it is not.

For a data log file, non-zero is always returned.

Note that EOF is handled by the `DRLGetNextUnmaskedEvent`（raw: `02.10.01.04.01.09_DRLGetNextUnmaskedEvent.md`） function.

### Return Value（取自子主题 DRL functions › DRLEventGetAttribute）

The return value is zero if the function was successful; otherwise the error code ERR_NO_ATTR (see `Error Codes`（raw: `02.10.01.04.02.108_Error_Codes.md`）) is returned if the event has no attribute record as specified by which.

### Example（取自子主题 DRL functions › DRLEventGetAttribute）

```
void example (void)
{
   DRLEventRec event;
   DRLAttributeRec attribute;
   int i, no_of_attributes;
    if (DRLGetNextUnmaskedEvent(&event));
      { /* error handler*/ break;
      }
   no_of_attributes = DRLEventGetNoOfAttributes(&event);
   for (i=0; i < no_of_attributes, i++)
   {
       DRLEventGetAttribute(&event, i, &attribute);
       /* attribute is now filled with data of the
          attribute record number i of event and can be
          processed  */
    }
}
```

### Return Value（取自子主题 DRL functions › DRLEventGetFirstAttributeByType）

The return value is zero if the function was successful; otherwise the error code ERR_NO_ATTR (see `Error Codes`（raw: `02.10.01.04.02.108_Error_Codes.md`）) is returned if the event has no attribute record as specified by type.

### Example（取自子主题 DRL functions › DRLEventGetFirstAttributeByType）

```
void example (void)
{
    DRLEventRec event;
    DRLAttributeRec attribute;
    if (DRLGetNextUnmaskedEvent(&event))
        { /* error handler*/
            break;
        }
    if (DRLEventGetFirstAttributeByType(&event, DeviceIdAttrType,
                                        &attribute) == 0)
        {
            printf("Device processed: %s\n",
                    attribute.data.device_id_attr.device_id);
        }
    else
        {
            printf("No DeviceIdAttr found !!!\n");
        }
}
```

### Return Value（取自子主题 DRL functions › DRLEventGetNextAttributeByType）

The return value is zero if the function was successful; otherwise the error code ERR_NO_ATTR (see `Error Codes`（raw: `02.10.01.04.02.108_Error_Codes.md`）) is returned if the event has no more attribute records as specified by type.

### Example（取自子主题 DRL functions › DRLEventGetNextAttributeByType）

```
void example (void)
{
    DRLEventRec event;
    DRLAttributeRec attribute;
    int error_code;
    if (DRLGetNextUnmaskedEvent(&event))
        { /* error handler*/
            break;
        }
    error_code = DRLEventGetFirstAttributeByType(&event,
                                         DeviceIdAttrType, &attribute);
    while (error_code == 0)
        {
            printf("Device processed: %s\n",
                    attribute.data.device_id_attr.device_id);
            error_code = DRLEventGetNextAttributeByType(&event,
                                        DeviceIdAttrType, &attribute);
        }
}
```

### Return Value（取自子主题 DRL functions › DRLEventGetNoOfAttributes）

The function returns the number of attribute records coming with event or a negative number indicating an error.

### Return Value（取自子主题 DRL functions › DRLEventGetType）

The event type of event.

### Example（取自子主题 DRL functions › DRLEventGetType）

```
void example (void)
{
   /* event has been initialized before by a call of DRLGetNextUnmaskedEvent */

   DRLEventType event_type;
   event_type = DRLEventGetType (&event)
   switch (event_type)
       { case ProgramStartEventType:
         /* analysis of the attribute records coming
             with an event of the type ProgramStartEventType
         */
              break;
         case TestFlowStartEventType:
          /* analysis of the attribute records coming with
             an event of the typeTestFlowStartEventType */
              break;
         /*
              .
              .
              .
              .
         */
       };
}
```

### Return Value（取自子主题 DRL functions › DRLFreeEvent）

None.

### Return Value（取自子主题 DRL functions › DRLGetEventMask）

The function returns a pointer to the active event mask of the data log stream or file event, or NULL in case of an error.

### Return Value（取自子主题 DRL functions › DRLGetNextUnmaskedEvent）

The return value is zero if the function was successful. Otherwise one of the following error codes is returned (see `Error Codes`（raw: `02.10.01.04.02.108_Error_Codes.md`）):

- ERR_NO_EVENT: Either no event record was available or the events related to all available event records were masked by the current event mask.
- ERR_EOF: The end of the data log stream or data log file was encountered before the event record had been read completely.

### Example（取自子主题 DRL functions › DRLGetNextUnmaskedEvent）

```
void example (void)
{
   DRLEventRec event;
     if (DRLGetNextUnmaskedEvent (&stream,&event))
   {
      /*  error handler  */
   }
/*   if DRLGetNextUnmaskedEvent was successful, the
event is now filled with valid data and &event can be
used for calls of functions which expect an argument of
the type DRLEventRec* (for example, DRLEventGet... functions)
*/
}
```

### Return Value（取自子主题 DRL functions › DRLKeepEvent）

None.

### Example（取自子主题 DRL functions › DRLKeepEvent）

```
/* keeps the data of 100 event records that are read
   from the data log stream */

DRLEventRec event_rec[100];
int last = 0;
while (last < 100)
 { DRLGetnextUnmaskedEvent (&my_stream, &event_rec[last]);
   DRLKeepEvent(&my_stream, &event_rec[last]);
   last++;
  };

/* after the event records have been processed, the
   allocated memory must be freed again */

while (last > 0)
 { /* process the event record event_rec[last] */
   DRLFreeEvent(&event_rec[--last]);
  };
```

### Return Value（取自子主题 DRL functions › DRLNumberOfPinGroups）

The function returns the number of pin groups in the current pin configuration.

### Return Value（取自子主题 DRL functions › DRLNumberOfPins）

The function returns the number of pins in the current pin configuration.

### Return Value（取自子主题 DRL functions › DRLNumberOfSites）

The function returns the number of sites in the current pin configuration.

### Return Value（取自子主题 DRL functions › DRLPinGroupIndexToName）

The function returns the name of the pin group with the index index.

In the case of an invalid index, the function returns NULL.

### Return Value（取自子主题 DRL functions › DRLPinGroupIndexToPins）

The function returns a pointer to an array of pin names (see `DRLPinName`（raw: `02.10.01.04.02.46_DRLPinName.md`）). The variable number_of_pins holds the number of pin names in that array, that is, the number of pins in the group with the index index.

If the provided index is invalid, the function returns NULL, and number_of_pins is 0.

### Return Value（取自子主题 DRL functions › DRLPinGroupNameToIndex）

The function returns the value 1, if the index of the pin group with the name name could be determined, and the variable index then holds the index.

Otherwise, the function returns 0, and index holds the value DRLNumberOfPinGroups. (See `DRLNumberOfPinGroups`（raw: `02.10.01.04.01.11_DRLNumberOfPinGroups.md`）).

### Return Value（取自子主题 DRL functions › DRLPinIndexToChannel）

The function returns the channel number of the pin with the index pin_index and the site site. The function returns 0, if pin_index belongs to an analog pin, or if pin_index is invalid.

### Return Value（取自子主题 DRL functions › DRLPinIndexToName）

The function returns the name of the pin with the index pin_index and capabilities holds the information on the type of that pin. In the case of an error the function returns NULL and type is undefined.

### Return Value（取自子主题 DRL functions › DRLPinIndexToNumber）

The function returns the number of the pin with the index pin_index. In case of an error, for example, if pin_index is invalid, the function returns NULL.

### Return Value（取自子主题 DRL functions › DRLSave）

The return value is zero if the function was successful or one of the following error codes (see `Error Codes`（raw: `02.10.01.04.02.108_Error_Codes.md`）) is returned in case of an error:

- ERR_ACCESS: the path specified in path could not be accessed
- ERR_TRUNC: the data log stream could not be truncated

### Return Value（取自子主题 DRL functions › DRLSetEventMask）

The return value is zero if the function was successful or non-zero if the event mask specified in mask is invalid.

### Example（取自子主题 DRL functions › DRLSetEventMask）

```
void example (void)
{
   DRLEventMask mask;
   /* set the values for mask as shown in the example in
    "DRLEventMask" on page 137*/
   if (DRLSetEventMask(&mask,&stream))
   {
      /*  error handler  */
   }
/* the active event mask is now set to that specified in mask */
}
```

### Return Value（取自子主题 DRL functions › DRLStart）

The return value is zero if the function was successful; otherwise the error code ERR_ACCESS (see `Error Codes`（raw: `02.10.01.04.02.108_Error_Codes.md`）) is returned if the file specified in path could not be accessed.

### Example（取自子主题 DRL functions › DRLStart）

```
void example (void)
{
 DRLDataStream stream;
 if (DRLStart (NULL,(DRL_SYNC_COUNTER | DRL_RESET_MASK,
    &stream))
    {
       /* error handler  */
     };
/* starts a data retrieval operating on the data log stream and checks */
/* only for new event records. The active event mask is reset.*/
}
```

### Return Value（取自子主题 DRL functions › DRLStop）

None.

### Return Value（取自子主题 DRL functions › DRLTruncate）

The return value is zero if the function was successful. If the data log stream could not be truncated, the error code ERR_TRUNC is returned.

### Example（取自子主题 DRL data types › DRLAttributeRec）

```
void example (void)
{
   /* event has been initialized before by a call of DRLGetNextUnmaskedEvent */

   DRLAttributeRec attribute;
   int i;
   i=1;
   DRLEventGetAttribute (&event,i,&attribute);
   /* gets the first (i=1) attribute record of event */

   switch (attribute.type)
       { case TestSuiteNameAttrType:
        /* processing attribute.data.test_suite_name_attr
       */
              break;
         case SiteSetAttrType:
       /* processing attribute.data.site_set_attr
       */
              break;
         /*
              ...

         */
       };
}
```

### Syntax（取自子主题 DRL data types › DRLBankSpecificCounts）

The struct contains these members:

- bank_id: The identifier for the bank.
- failing_address_count: The number of failed addresses for the bank.
- failing_address_limit:
- DRLFailureCode: The code for the overall result for the bank. (See the table below for details.)

```
typedef struct _DRLBankSpecificCounts {
  unsigned int         bank_id;
  unsigned long long   failing_address_count;
  unsigned long long   failing_address_limit;
  enum DRLFailureCode  result;
} DRLBankSpecificCounts;
```

Failure code values
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/123465.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：Value | Description

### Syntax（取自子主题 DRL data types › DRLBitFailMapDescAttr）

The description is contained in the label description.

```
typedef struct _DRLBitFailMapDescAttr {
  const char* description;
} *DRLBitFailMapDescAttr;
```

### Syntax（取自子主题 DRL data types › DRLErrorMapAttr）

```
typedef struct _DRLErrorMapAttr {
  DRLPinName pin;
  const char* description;
  int mode;
  unsigned failure_count;
  struct {
    long long cycle_number;
    int instance_id;
    unsigned offset;
    char state_character;
    char received;
  } cycle[1];
} *DRLErrorMapAttr;
```

### Syntax（取自子主题 DRL data types › DRLErrorOverviewAttr）

```
typedef struct _DRLErrorOverviewAttr {
  const char* description;
  long long cycle_count;
  long long failure_count;
} *DRLErrorOverviewAttr;
```

### Example（取自子主题 DRL data types › DRLEventMask）

```
void example (void)
{
  DRLEventMask event_mask = {NumberOfEventTypes,0};
  /* initialization */

  event_mask.event_mask[TestSuiteStartEventType] = 1;
  event_mask.event_mask[TestSuiteEndEventType] = 1;
  event_mask.event_mask[BinReachedEventType] = 1;
  event_mask.event_mask[AssignmentEventType] = 1;
  /* masking of events which are specified by the
     event type*/

  DRLSetEventMask(&event_mask);
 /* sets the active event mask as specified in event_mask */
}
```

### Syntax（取自子主题 DRL data types › DRLFailingAddressCountAttr）

The struct contains these members:

- global_count: The number of failed addresses.
- failing_access_count: The sum of failed accesses to these addresses.
- result_pin_count: The number of pins with failed accesses.
- bank_count: The number of banks with failed accesses.
- bank_specific_counts: The failed address counts for the individual banks, one per bank with failures.
- pin_specific_counts: The failed address counts for the individual pins, one per pins with failures.

```
typedef struct _DRLFailingAddressCountAttr {
  unsigned long long       global_count; /* number of failing addresses */
  unsigned long long       failing_access_count; /* number of failing accesses */
  unsigned int             result_pin_count; /* d dimension */
  unsigned int             bank_count; /* z_address_count */
  `DRLBankSpecificCounts`（raw: `02.10.01.04.02.05_DRLBankSpecificCounts.md`）*   bank_specific_counts; /* size is bank_count */
  `DRLPinSpecificCounts`（raw: `02.10.01.04.02.52_DRLPinSpecificCounts.md`）*    pin_specific_counts; /* size is result_pin_count */
} *DRLFailingAddressCountAttr;
```

### Syntax（取自子主题 DRL data types › DRLFailingAdresses）

The struct contains these members:

- x_address: The x-coordinate of the failing address.
- y_address: The y-coordinate of the failing address.
- z_address: The z-coordinate of the failing address.
- expected_data: The data that the test expected to find at the address - 0 or 1. If the expected data was not recorded, this member contains the value 3.

```
typedef struct _DRLFailingAddresses {
  unsigned long long x_address;
  unsigned long long y_address;
  unsigned long long z_address;
  unsigned short     expected_data; /* 0 or 1 */
} DRLFailingAddresses;
```

### Syntax（取自子主题 DRL data types › DRLFailingAddressesAttr）

The struct contains these members:

- failing_address_count: The number of failed addresses.
- failing_access_count: The sum of failed accesses to these addresses.
- result_pin_count: The number of pins with failed accesses.
- x_address_count: The number of different x-addresses with failed accesses.
- y_address_count: The number of different y-addresses with failed accesses.
- z_address_count: The number of different z-addresses with failed accesses.
- pin_specific_addresses: The failed addresses for the individual pins, one set per pin with failures.

```
typedef struct _DRLFailingAddressesAttr {
  unsigned long long       failing_address_count; /* number of failing addresses */
  unsigned long long       failing_access_count; /* number of failing accesses */
  unsigned int             result_pin_count; /* d dimension */
  unsigned int             x_address_count;
  unsigned int             y_address_count;
  unsigned int             z_address_count;
  `DRLPinSpecificAddresses`（raw: `02.10.01.04.02.51_DRLPinSpecificAddresses.md`）* pin_specific_addresses; /* size is result_pin_count*/
} *DRLFailingAddressesAttr;
```

### Syntax（取自子主题 DRL data types › DRLLabelDescriptorAttr）

```
typedef struct _DRLLabelDescriptor {
  int id;
  const char* name;
} *DRLLabelDescriptor;
```

### Syntax（取自子主题 DRL data types › DRLLabelListAttr）

```
typedef struct _DRLLabelListAttr {
  int label_count;
  struct _DRLLabelDescriptor label[1];
} *DRLLabelListAttr;
```

### Syntax（取自子主题 DRL data types › DRLPatternLabelAttr）

The pattern label is contained in the label member.

```
typedef struct _DRLPatternLabelAttr {
  const char* label;
} *DRLPatternLabelAttr;
```

### Syntax（取自子主题 DRL data types › DRLPinSpecificAddresses）

The struct contains these members:

- result_pin_name: The name of the pin for which the failed addresses are listed.
- logged_failing_address_count: The number of failed addresses being listed.
- DRLFailingAdresses: The failed address for the pin.

```
typedef struct _DRLPinSpecificAddresses {
  `DRLResultPinName`（raw: `02.10.01.04.02.62_DRLResultPinName.md`）     result_pin_name;
  unsigned long long   logged_failing_address_count;
  `DRLFailingAddresses`（raw: `02.10.01.04.02.23_DRLFailingAdresses.md`）* logged_failing_addresses;
                       /* size is logged_failing_address_count */
} DRLPinSpecificAddresses;
```

### Syntax（取自子主题 DRL data types › DRLPinSpecificCounts）

The struct contains these members:

- result_pin_name: The name of the pin.
- failing_address_count: The number of failed addresses for the pin.
- failing_address_limit:
- DRLFailureCode: The code for the overall result for the pin. (See the table below for details.)

```
typedef struct _DRLPinSpecificCounts {
  `DRLResultPinName`（raw: `02.10.01.04.02.62_DRLResultPinName.md`）  result_pin_name;
  unsigned long long   failing_address_count;
  unsigned long long   failing_address_limit;
  enum DRLFailureCode  result;
} DRLPinSpecificCounts;
```

Failure code values
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/123466.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：Value | Description

### Example（取自子主题 DRL data types › DRLPinType）

```
void example (void)
{
  DRLPinType *type;
  DRLPinIndex index=1;
if (DRLPinIndexToName(index,type) = NULL)
    {
       /* error handler  */
    };
/* type now holds the information on the pin type. */
if (type->input)  {/* pin 1 is an input pin*/};
if (type->output) {/* pin 1 is an output pin*/};
if (type->dps)    {/* pin 1 is a DPS pin*/};
if (type->dc)     {/* pin 1 is a DC pin*/};
if (type->analog) {/* pin 1 is an analog pin*/};
if (type->virt)   {/* pin 1 is a virtual pin*/};
}
```

### Syntax（取自子主题 DRL data types › DRLRARepairResult）

The struct contains these members:

- element: The identifier of the row or column in the segment.
- segment: The identifier of the segment to which the element belongs.
- spare: The spare resource used to repair the element.

```
typedef struct _DRLRARepairResult {
  unsigned int element;
  unsigned int segment;
  unsigned int spare;
} *DRLRARepairResult;
```

### Syntax（取自子主题 DRL data types › DRLRARepairResultsAttr）

The struct contains these members:

- repairable: Whether the tested device is repairable:

  - DRLFailureCode_Fail: The device is not repairable. The other members show what has been repaired.
  - DRLFailureCode_Pass: The device is repairable. The other members show the repair solution.

- dieX: The x dimension of the die.
- dieY: The y dimension of the die.
- spare_column_count: The number of spare columns used for repairs.
- spare_row_count: The number of spare rows used for repairs.
- column_results: A list of the columns used for repairs. This is a value of type `DRLRARepairResult`（raw: `02.10.01.04.02.60_DRLRARepairResult.md`）; the size is spare_column_count.
- row_results: A list of the rows used for repairs. This is a value of type `DRLRARepairResult`（raw: `02.10.01.04.02.60_DRLRARepairResult.md`）; the size is spare_row_count.

```
typedef struct _DRLRARepairResults {
  enum DRLFailureCode repairable;
  unsigned long long dieX;
  unsigned long long dieY;
  unsigned int spare_column_count;
  unsigned int spare_row_count;
  DRLRARepairResult* column_results;
  DRLRARepairResult* row_results;
} *DRLRARepairResults;
```

### Syntax（取自子主题 DRL data types › DRLResultPinName）

The struct contains these members:

- bit_pos: The position of the pin's bit in the d dimension.
- pin_name: The name of the pin being reported.

```
typedef struct _DRLResultPinName {
  unsigned int         bit_pos;
  `DRLPinName`（raw: `02.10.01.04.02.46_DRLPinName.md`）           pin_name;
} DRLResultPinName;
```

### Syntax（取自子主题 DRL data types › DRLScanInstanceDescriptorAttr）

```
typedef struct _DRLScanInstanceDescriptor {
  int id;
  const char *name;
  int label_id;
  const char* label;
  long long start_cycle;
  long long end_cycle;
} *DRLScanInstanceDescriptor;
```

### Syntax（取自子主题 DRL data types › DRLScanInstanceListAttr）

```
typedef struct _DRLScanInstanceListAttr {
  int instance_count;
  struct _DRLScanInstanceDescriptor instance[1];
} *DRLScanInstanceListAttr;
```

### Syntax（取自子主题 DRL data types › DRLShmooAxisData）

```
typedef struct _DRLShmooAxisData
{
  double start;
  double stop;
  unsigned int totalSteps;
  unsigned int linearSteps;
  const char* primaryValue;
  const char* scale;
  const char* otherDescription;
  DRLShmooParametersType parameterType;
  union
   {
     DRLShmooSpecVariableType spec;
     DRLShmooHXInstrumentType HXInstrument;
     DRLShmooHXResourceType HXResource;
     DRLShmooUserDefinedParamType userDefinedParam;
   } parameter;
} *DRLShmooAxisData;
```

### Syntax（取自子主题 DRL data types › DRLShmooHXInstrumentType）

```
typedef struct _DRLShmooHXInstrumentType
{
  const char* instrumentPin;
  const char* property;
  const char* unit;
} *DRLShmooHXInstrumentType;
```

### Syntax（取自子主题 DRL data types › DRLShmooHXResourceType）

```
typedef struct _DRLShmooHXResourceType
{
  const char* resourceName;
  const char* property;
  const char* unit;
} *DRLShmooHXResourceType;
```

### Syntax（取自子主题 DRL data types › DRLShmooSpecVariableType）

```
typedef struct _DRLShmooSpecVariableType
{
  const char* spec;
  const char* setupPins;
} *DRLShmooSpecVariableType ;
```

### Syntax（取自子主题 DRL data types › DRLShmooTestCellAttr）

```
typedef struct _DRLShmooTestCellAttr
{
  unsigned int numberOfPin;
  unsigned int numberOfTestMode;
  const char* pinNames;
  const char* testModes;

  unsigned int numberOfCell;
  DRLShmooTestCellData* cellData;
}*DRLShmooTestCellAttr;
```

### Syntax（取自子主题 DRL data types › DRLShmooTestCellData）

```
typedef struct _DRLShmooTestCellData
{
  unsigned int coordinates[MAX_NUM_AXIS];
  unsigned int numberOfValues;
  double* cellValue;
} *DRLShmooTestCellData;
```

### Syntax（取自子主题 DRL data types › DRLShmooTestInfoAttr）

```
typedef struct _DRLShmooTestInfoAttr
{
  const char* title;
  const char* testMode;
  const char* resultPins;
  const char* otherDescription;
  double resultResolution;
  int numberOfAxis;
  DRLShmooAxisData* axisData;
} *DRLShmooTestInfoAttr;
```

### Syntax（取自子主题 DRL data types › DRLShmooUserDefinedParamType）

```
typedef struct _DRLShmooUserDefinedParamType
{
  const char* paramName;
  const char* type;
}*DRLShmooUserDefinedParamType;
```

### Example（取自子主题 DRL data types › DRLSiteSetAttr）

```
/* lists all site Ids of a site set */
void example (DRLSiteSetAttr ss_attribute)
/* contents of ss_attribute are passed by the caller
    of example */
{
  int i
  for (i=0; i<ss_attribute->size;i++)
  {
    printf(ss_attribute->site[i]);
  };
}
```

### Syntax（取自子主题 DRL data types › DRLTestConditionAttr）

```
typedef struct _DRLTestConditionAttr {
  unsigned short conditionCount;
  `DRLTestCondition`（raw: `02.10.01.04.02.87_DRLTestCondition.md`） testCondition[];
} *DRLTestConditionAttr;
```

To write this attribute:

```
DCLAttribute DCLMakeTestConditionAttr ( DCLTestCondition* testCondition, unsigned short testCondCnt )
```

To read this attribute:

```
static int TestConditionAttrConv(DRLDataStream* stream, unsigned char* p, DCLAttributeRecLength length, DRLAttributeRec* attr)
```

### Syntax（取自子主题 DRL data types › DRLTestCondition）

```
typedef struct _DRLTestCondition {
char* key;
char* value;
} *DRLTestCondition;
```

<!-- 语法节 end -->

## 是什么

**定义句逐字（本篇第 1 段第 1 句）：**

> 「The Data Retrieval Library (DRL) is the application programming interface (API) that provides
> access to the data log stream where all events of the production test currently being executed
> are logged (see Event Data Logging Concepts). The DRL also provides access to the data held in
> the individual event records. When you write your own data logging tools, the DRL lets you make
> full use of all capabilities of event data logging.」

**三句，各给一层：**

| # | 原句（**逐字**） | 说的什么 |
|---|---|---|
| 1 | `the application programming interface (API) that provides access to the data log stream` | **它是一个 API，提供对 `data log stream` 的访问** |
| 2 | `the data log stream where all events of the production test currently being executed are logged` | **那个 stream 里装的是「**当前正在执行的那次生产测试**的所有事件」** |
| 3 | `The DRL also provides access to the data held in the individual event records.` | **除了流，它还给「单条 event record 里的数据」的访问** |
| 4 | `When you write your own data logging tools, the DRL lets you make full use of all capabilities of event data logging.` | **它是给「自己写 data logging 工具」的人用的** |

**要注意第 2 句里 `currently being executed` 这个限定**——
**流装的是「正在跑的那一次」的事件**；
**要看已经跑完的，本篇另给了出口（见下「离线：把流存成文件」）。**

**（推断）它是一套 C 接口。** 依据有两条，都在本页上：
① **本篇正文给的三个头文件都是 `.h`**（见下「三个头文件」）；
② **本页 `## 语法 / 参数` 节里全是 C 的东西**——
`void example (void)` 形式的函数、`typedef struct _DRLBankSpecificCounts { … }` 形式的
结构体、`unsigned long long` / `const char*` 这样的 C 类型。
**⚠️ 但本篇正文一个字都没写「C」**（`C` 这个字母在本篇正文里不出现），
**所以这一条是本页的推断，不是文档事实。**

**frontmatter 的 `layer: L2` 与这句 `the application programming interface (API)` 相符**
（**对应关系是本 wiki 的划分，不是本篇写的**）。

### 它免掉什么：写 parser

**本篇第 2 段全文只有一句**，逐字：

> 「Using the DRL frees you from the need to write parsers for data log files.」

**这是本篇给的最直接的「为什么用它」**——
**不用它的代价就是自己写一个 data log file 的 parser。**

### 它的函数能做什么（**三个动作**）

**本篇第 3 段，逐字：**

> 「The functions of the DRL enable you to read event records from the data log stream, to extract
> data from these records, and to store the extracted data in variables of appropriate data types.
> These data types, which are also provided by the DRL, are designed to hold all the different data
> from the various attributes. Thus, you can use them for any further direct processing of logged
> data you require.」

**三个动作是一条链**，**而且第三个动作要用的「变量类型」也是 DRL 给的**：

| 动作 | 原文（**逐字**） |
|---|---|
| 1 读 | `read event records from the data log stream` |
| 2 取 | `extract data from these records` |
| 3 存 | `store the extracted data in variables of appropriate data types` |

**第 3 步的类型从哪来**：`These data types, which are also provided by the DRL`——
**即 DRL 自带一套 data type，专门用来装 `the various attributes` 里的各种数据。**
**这也解释了本页 `## 语法 / 参数` 节为什么长这样：它由两组子主题拼成——
24 个 `DRL functions`（动作）与 31 个 `DRL data types`（容器）。**

### 离线：把流存成文件，然后**用同一套办法**读

**本篇第 4 段全文只有一句**，逐字：

> 「For offline analysis of logged data, you can save the data log stream to a file and later
> access this file in the same way as the data log stream itself.」

**「流」与「文件」在 DRL 这一层是**同一种输入**——`in the same way as the data log stream itself`。**

**这一点在 `## 语法 / 参数` 节里能找到对应的写法。**
节里第一个函数 `DRLEventAvailable` 的 Return Value 逐字分了两段：

> 「For the data log stream, non-zero is returned if a new event record is ready to be read. This
> allows you to treat the result value as true if a new record is ready and false if it is not.」
> 「For a data log file, non-zero is always returned.」

**即：同一个函数对两种输入给的返回值不同——流会说「还没好」（0），文件永远说「好了」（非 0）。**
**（推断）这正是「流是活的、文件是死的」这件事在 API 上的表现**——
**依据是这两段并排的写法本身；本篇正文没有把这层关系说出来，所以这是推断。**

### 谁建在它上面：Event Formatter

**本篇第 5 段全文只有一句**，逐字：

> 「The Event Formatter (see Using the Event Formatter) is built on top of the DRL.」

**这是本篇给出的唯一一条「谁用它」——[[event-formatter]] 建在 DRL 之上。**
**⚠️ 括号里的链接文本与它指的文件名不是一回事**（见 `## 出处` ②）。

### 三个头文件

**本篇第 6 段（最后一段）全文，逐字：**

> 「The header file of the DRL is /opt/hp93000/soc/com/include/drl.h. The same directory contains
> the header files dcl.h and dcl_drl.h that also are related to the data retrieval library.」

| 文件（**逐字**） | 位置（**逐字**） |
|---|---|
| `drl.h` | `/opt/hp93000/soc/com/include/drl.h`——**原文说这是「DRL 的头文件」** |
| `dcl.h` | **同一个目录**（`The same directory`） |
| `dcl_drl.h` | **同一个目录** |

**后两个原文只说 `that also are related to the data retrieval library`**——
**「也和 data retrieval library 有关」，但没说它们是干什么的、谁的头文件。**
**`dcl` 这三个字母在本篇正文里没有展开**（**（推断）它与 DCL / Data Collection Library 相关，
但本篇正文没有写这个展开，所以这是推断**）。

### 本篇的结构与规模

**本篇正文只有 6 段、1,784 个字符**（本页数过），
**而 `## 语法 / 参数` 节取自 55 个子主题**（**24 个 DRL functions + 31 个 DRL data types**，
本页按节首那行列出的路径数过）——
**这 55 篇本页一篇都没有读**（见 `## 出处`）。
**`#### Subtopics` 底下只有两条链接**（`DRL functions`、`DRL data types`），
**它们是那 55 篇的两个总入口。**

**`#### Subtopics` 是 H4，直接挂在 H1 下面**——
**H2 与 H3 在本篇里不存在**（**与本批 [[edf]] / [[error-map]] / [[event-formatter]]
三页记的同一个形态；那一条本页引自那三页，不是本篇 raw**）。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有一个命令行、没有一个配置项。**
**本篇的「用法」全在 `## 语法 / 参数` 节的那两族内容里**
（**24 个函数的用法 + 31 个数据类型的结构**），
**而本节只从里面取骨架，不给逐个函数的用法表**（见 `## 出处` ①）。

**从本篇正文能落成的只有下面这几条：**

| 要做的 | 依据（**原文**） |
|---|---|
| **自己写一个读 data log 的工具** | 用它。`When you write your own data logging tools, the DRL lets you make full use of all capabilities of event data logging.` |
| **省掉自己写 parser** | `Using the DRL frees you from the need to write parsers for data log files.` |
| **读正在跑的那次生产测试** | 直接读 `the data log stream`（**注意 `currently being executed` 这个限定**） |
| **做离线分析** | `save the data log stream to a file and later access this file in the same way as the data log stream itself` |
| **拿到事件里的数据** | 三步：`read event records` → `extract data from these records` → `store the extracted data in variables of appropriate data types` |
| **写测试程序时引头文件** | `/opt/hp93000/soc/com/include/drl.h`；**同目录另有 `dcl.h` 与 `dcl_drl.h`** |
| **想找参考实现** | **原文指向 [[event-formatter]]**：`is built on top of the DRL`——**本篇没有说哪里能看到它的源码** |
| **想搞清楚「事件」这个概念** | **原文把出口指向 `Event Data Logging Concepts`**（`see Event Data Logging Concepts`）——**本页没读** |

**一处本页要提醒的**：**本篇正文里没有一句话讲调用顺序**
（先 `DRLStart` 还是先 `DRLSetEventMask`、读完之后要不要 `DRLFreeEvent`）。
**这些顺序只能从 `## 语法 / 参数` 节里那些 example 反推**，
**而那些 example 之间本身就互相矛盾**（**索引基数 0 与 1 两处不一致，见 `## 出处` ⑥**）。
**本页不据它们排出顺序。**

## 和谁有关

- [[event-formatter]] — **原文点名的唯一一个「建在 DRL 上」的东西**，上下游关系明确。
  逐字：`The Event Formatter (see Using the Event Formatter) is built on top of the DRL.`
  **即：DRL 在下、Event Formatter 在上**；
  **本页只有这一句，Event Formatter 自己怎么用本页没有（那一页本页没读）。**
- [[edl-file]] — **（推断）那个「文件」可能就是指它**。
  依据：本篇说 `you can save the data log stream to a file`，
  而 wiki 另有一页讲 results 侧的 data log 文件（[[edl-file]]）；
  **但本篇用的词是 `a file`，既没写 `EDL`、也没写 `EDF`、更没写 `DataCollection`**
  （**本页查过：本篇 `EDL` 0 次、`EDF` 0 次、`DataCollection` 0 次、
  `STDF` 0 次**）——**所以本页没有依据把这两个「文件」并成一个。这是推断。**
- [[edf]] — **（推断）名字与主题同族**。
  依据只是：本篇讲的是读 event data log 的流与记录，而 wiki 另有一页叫
  `Event Data Logging Format (EDF)`；
  **本篇一个字都没提 `EDF`，那一页本页也没读**——
  **按页名相邻列出，不代表同物。**
- [[error-map]] — **（推断）语法节里的两个结构名指向它**。
  依据：**本页 `## 语法 / 参数` 节里有 `DRLErrorMapAttr` 与 `DRLErrorOverviewAttr`
  两个结构**（本页查过：各出现 4 次），
  而 [[error-map]] 那页讲的正是 detailed 与 overview 两种 error map；
  **两个名字的对应关系本篇一个字都没说，那一页本页也没读**——
  **这是推断，而且本页不据此写任何机制。**
- [[smartest-6.3.2]] — **版本页**。本页 `## 版本` 唯一那一条的落点。
- `Event Data Logging Concepts`（**未建、不在 allowlist，故用反引号**）—
  **原文唯一的「概念」出口**：`see Event Data Logging Concepts`，
  链到 `02.10.01.01_Event_Data_Logging_Concepts.md`。**本页没读**——
  **所以「事件」「属性」「流」这些词的定义本页一个都没有。**
- `Using the Event Formatter`（**未建**）— **原文给 [[event-formatter]] 用的链接文本**，
  而它链到的文件是 `02.10.02_Event_Formatter.md`（**见 `## 出处` ②**）。
- `DRL functions` / `DRL data types`（**两个，均未建**）— **`#### Subtopics` 的两条**，
  也是 `## 语法 / 参数` 节那 55 个子主题的两个总入口
  （`02.10.01.04.01` 与 `02.10.01.04.02`）。
- `Error Codes`（**未建**）— **语法节里被引用 6 次的那个出口**
  （每一处都写成 `see Error Codes`），链到 `02.10.01.04.02.108_Error_Codes.md`。
  **本页没读，所以那些 `ERR_*` 的完整清单与含义本页没有**
  （**本页只见到语法节里露出来的几个：`ERR_NO_ATTR`、`ERR_NO_EVENT`、`ERR_EOF`、
  `ERR_ACCESS`、`ERR_TRUNC`**）。
- `DCL`（**未建**）— **三项点名的东西**：头文件 `dcl.h` / `dcl_drl.h`，
  以及语法节里出现的 `DCLAttribute` / `DCLMakeTestConditionAttr` / `DCLTestCondition` /
  `DCLAttributeRecLength`（**本页查过：`DCL` 在本页出现 4 次，全在语法节里**）。
  **本篇正文没有展开 `DCL` 这三个字母，也没有说它和 DRL 是什么分工。**
- `drl.h` / `dcl.h` / `dcl_drl.h`（**三个头文件，均未建**）— 见上「三个头文件」。
  **本页没有读过其中任何一个文件的内容。**
- `data log stream`（**未建**）— **本页这个库读的那个东西**
  （`the data log stream where all events of the production test currently being executed are
  logged`）。**本篇没有说它是文件、是内存、还是进程间的通道**——
  **只知道它可以被 `save … to a file`。**
- `DRLEventRec` / `DRLAttributeRec` / `DRLEventMask` / `DRLDataStream` / `DRLFailureCode`
  （**均未建**）— **语法节里反复出现的那几个核心类型**，
  **本页只在语法节里见过它们的用法，本篇正文一个都没提。**

## 版本

**本文档有 `## Functional changes` 段，只有一条**，逐字：

- **Introduced before SmarTest 6.3.2**

**这一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 DRL 本身成立于哪个版本，这份语料里没有。**

**本篇没有任何别的版本信息**：**正文 6 段、`SmarTest 6.3.2` 是里面唯一出现过的版本号。**

**与 wiki 目标版本（SmarTest 7.10.3）的关系**：
**本篇连一条 7.x 的条目都没有**——
**所以「DRL 在 7.10.3 上还是不是这个接口、`drl.h` 还在不在那个路径」
本篇给不出任何依据。**
**（推断）本篇正文那 55 个子主题的规模说明它是一个长期存在的大接口**——
**依据只是子主题数量本身；原文没有一句话说它稳定或长期支持。这是推断。**

详见 [[smartest-6.3.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.01.04_Data_Retrieval_Library.md`

**本页没做的：**

- **`## 语法 / 参数` 节取自的 55 个子主题（24 个 DRL functions + 31 个 DRL data types）
  一篇都没读。** **这是本页最大的空缺**：
  **每一个函数的签名、参数、返回值语义，每一个数据类型的字段含义，全在那 55 篇里**，
  **本页只按语法节里逐字摆出来的内容转述骨架，没有回任何一篇核过。**
  **所以本页给不出「哪个函数怎么调、按什么顺序调」。**
- **`Event Data Logging Concepts` 没读** —— **而它是本篇正文唯一的「概念」出口**
  （`see Event Data Logging Concepts`）。
  **所以「事件」「属性」「event stream」这些词在本篇里的定义，本页没有。**
- **`Error Codes` 没读** —— **而语法节里 6 处 `see Error Codes`**。
  **所以本页只能列出语法节里亲眼见到的五个 `ERR_*` 名字，给不出完整清单与含义。**
- **`drl.h` / `dcl.h` / `dcl_drl.h` 三个头文件都没打开** ——
  **所以函数原型、宏、枚举的权威定义本页一个都没有**
  （**本页只有语法节里从子主题抄来的那些**）。
- **[[event-formatter]] 没读** —— **所以「built on top of the DRL」在实现上意味着什么、
  它调了哪些 DRL 函数，本页一个字都没有。**
- **`data log stream` 是什么形态，本篇没写、本页也没有** ——
  **本页只知道它可以被 `save … to a file`，且它装的是「正在执行的那次生产测试」的事件。**
- **调用顺序本页没写**（见 `## 典型用法`），**因为语法节里的 example 互相矛盾**，
  **本页不据它们排序。**
- **一张图都没有。** 原文没有图片（本页查过：0 处图片语法）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：[[event-formatter]] / [[edl-file]] / [[error-map]] 都没读**——
  **本页与它们的关系全部取自本篇这一篇的正文（与本节里逐字摆着的语法节），
  没有从对面回校过。**
- **`layer: L2` / `stage: results` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分
  （**（推断）`L2` 与 `the application programming interface (API)` 相符，
  但这是本页的观察，不是原文说的**）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 正文 6 段、1,784 个字符，而它的语法节取自 55 个子主题。**
> ——**一个库的主页自己只有 6 句话，全部实质内容都在子主题里。
> 本页照实说，不替它扩写。**
>
> **② 链接文本与它指的文件名不是一回事。** 逐字：
> `The Event Formatter (see [Using the Event Formatter](<02.10.02_Event_Formatter.md>)) is built on
> top of the DRL.`
> ——**链接文本是 `Using the Event Formatter`（「使用 Event Formatter」），
> 而链到的文件是 `02.10.02_Event_Formatter.md`（那一篇的标题是 `Event Formatter`）。**
> **即：显示名比目标文档多了一个动作词，指的还是同一篇。本页照实并列，不替它改。**
>
> **③ `#### Subtopics` 是 H4，直接挂在 H1 下面。** 本篇的非 H1 标题只有这一个，
> 层级是 H4——**H2 与 H3 在本篇里不存在**。
> （**与本批 [[edf]] / [[error-map]] / [[event-formatter]] 三页记的同一形态；
> 那一条本页引自那三页，不是本篇 raw。**）
>
> **④ 空格不是放在 `## Syntax` / `## Return Value` 段里的标题上，而是挤在段名之后。**
> 逐字：
> `### Return Value（取自子主题 DRL functions › DRLEventAvailable）`
> ——**「取自子主题 …」这一串是脚本加在段名后面的括注**，
> **本篇原文那一节可能就叫 `Return Value`。这一条是「页面的语法节」自己的形态，
> 不是本篇正文的形态，本页照实记。**
>
> **⑤ 语法节里有两个函数名少一个字母。** 逐字（同一页内并列）：
> `DRLGetNextUnmaskedEvent`（正确形态，出现在多处）与
> `DRLGetnextUnmaskedEvent`（**`next` 的 `n` 小写了**，出现在 `DRLKeepEvent` 的 example 里）。
> ——**一个函数两种拼法，同页并存。本页照实并列，不替它统一。**
>
> **⑥ 语法节里的 example 把索引基数写成了两种（0 与 1）。** 逐字并列：
> `for (i=0; i < no_of_attributes, i++)`（`DRLEventGetAttribute` 的 example）
> 与 `i=1;` 加注 `/* gets the first (i=1) attribute record of event */`
> （`DRLAttributeRec` 的 example）。
> ——**一处从 0 开始数、一处说「第一个是 1」。
> 哪一个对，本篇正文没有说，本页也不据它排调用顺序。**
>
> **⑦ 语法节里有几处 C 代码本身是错的，本页逐字记，一处都没替它改**
> （**这些 example 全部来自子主题，见节首 ⚠️**）：
>
> - `for (i=0; i < no_of_attributes, i++)` —— **条件与自增之间是逗号，不是分号**
> - `if (DRLGetNextUnmaskedEvent(&event));` —— **`if` 后面多一个分号，
>   于是下面那个「error handler」块与这个 `if` 没有从属关系**
> - `if (DRLPinIndexToName(index,type) = NULL)` —— **赋值 `=`，不是判断 `==`**
> - `event_type = DRLEventGetType (&event)` —— **行末没有分号**
> - `DRLSetEventMask(&event_mask);`（**一个参数**）与 `DRLSetEventMask(&mask,&stream)`
>   （**两个参数**）—— **同一个函数两种实参个数**
> - `printf(ss_attribute->site[i]);` —— **把非格式串直接当格式串用**
> - `int i`（`DRLSiteSetAttr` 的 example 里）—— **行末没有分号**
>
> **本页把这些照原样列出，不修、不补，也不假装没看见**——
> **照抄这些 example 的人会撞上它们。**
>
> **⑧ 两个数据类型的文件名字母数与结构体名不一致。** 逐字：
> 文件名 `<02.10.01.04.02.23_DRLFailingAdresses.md>`（**`Adresses`，一个 `d`**），
> 而同一节里的结构体是 `typedef struct _DRLFailingAddresses`（**`Addresses`，两个 `d`**）。
> ——**同一节里两处拼法不同；而紧邻的下一个子主题
> `<02.10.01.04.02.24_DRLFailingAddressesAttr.md>` 又拼成两个 `d`。**
> **本页照实并列，不替它改文件名。**
>
> **⑨ 同一个枚举被用在一个读起来相反的位置上。** 逐字（`DRLRARepairResultsAttr` 一节）：
> `repairable: Whether the tested device is repairable:` 下面两条是
> `- DRLFailureCode_Fail: The device is not repairable. The other members show what has been
> repaired.` 与 `- DRLFailureCode_Pass: The device is repairable. …`；
> **而 `DRLBankSpecificCounts` 一节那张表里 `0 = DRLFailureCode_Pass` 的意思是 `passed`。**
> ——**即 `Pass` 在「可修复」这个位置上代表「能修」。**
> **原文两处都写了，本页并列，不替它解释，也不改。**
>
> **⑩ 本篇没有 §11.2 ① 那种编码损坏**（本页查过：本篇正文汉字 0 个、`鈥` 0 处）。
>
> **⑪ 语法节里「省略」有三种写法，各在一处，互不相同。** 逐字并列：
>
> - **四个独立成行的 `.`**：`DRLEventGetType` 的 example 里，
>   `/*` 之后是四行各一个 `.`，再一行 `*/`；
> - **一个 `...`**：`DRLAttributeRec` 的 example 里，`/*` 之后是一行 `...`，再一行 `*/`；
> - **名字尾部的 `...`**：`DRLGetNextUnmaskedEvent` 的 example 注释里写
>   `DRLEventGet... functions`——**用省略号截断了一串函数名**。
>
> **三个都是原文自己写的省略，不是本页加进去的**
> （**本页查过：本节里 `鈥`/`…`（U+2026）0 处，`...` 2 处，加上那四个独立成行的 `.`**）。
> **本页照实记，不替它统一。**（§11.1：省略号只许出现在原文自己就有的地方。）

`verified: doc-only`
