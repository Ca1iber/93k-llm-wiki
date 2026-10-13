---
type: concept
title: Command Reference
layer: n/a
stage: project
tags: [command, firmware, api, smartrdi, site, reference]
related: [smartrdi, testmethod, pin, site-focus-required-before-command, timing-setup-commands, results, run, flag, alphabetical-list-of-flags, utility-line-assignments, dc-test-programming]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06_Command_Reference.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Command Reference

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **638,878 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06_Command_Reference.md>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.01.02_Firmware_view.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.02_APDV_-__APpenD_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.03_APRM_-__Activate_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.04_APTS_-__APpend_TeSt.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.05_ASWE__ASWE__-__Auto_SWing_Enable.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.06_ASWM__ASWM__-__Auto_SWing_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.07_BCMD__BCMD__-_Binding_CoMmanD.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.08_BCMT__BCMT__-__Binary_CoMmenT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.09_BDID__BDID__-__BoarD_ID.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.100_EDDC__-__EDge_in_Device_Cycle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.101_EDGE__-__EDGE_errors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.103_EMAP__-__Error_MAP.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.104_EMBS__Error_Map_Block_Size.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.105_ENSP__ENSP__-__ENable_Sampling_Profile.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.106_EPRC__-__Error_Propagation_Repetition_Count.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.107_EQFC__EQFC__-__EQualization_and_Filter_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.108_EQFS_-__EQuation_FileS_command_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.109_EQSP__EQSP__-__EQuation_SPecification_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.10_BLUP_-__BLock_UP_to_date.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.110_ERCC__-__ERror_in_Cycle_range_Count.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.111_ERCE__-__Expected_and_Received_Cycle_data_of_Events.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.112_ERCT__-__ERror_CounT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.113_ERCY__-__ERror_CYcle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.114_ERMP__-__ERror_MaP.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.115_ERRE__-__Expected_and_Received_Results_of_Events.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.116_ESGB__ESGB__-__Edge_Search_GloBal.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.119_EUDS__-__Edge_Usage_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.11_BSVE_-__Bulk_Set_Value_Evaluation.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.120_EVCK__-__EVent_ClocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.121_EXSR_-__EXecute_SeaRch.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.123_FLBL__-__Failing_LaBeLs.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.125_FTCG__FTCG__-__Functional_Test_ConfiGure.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.126_FTSM__FTSM__-__Functional_Test_Set_Mask.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.127_FTST__-__Functional_TeST.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.128_FXDL__FXDL__-__FiXture_DeLay.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.129_GCTX__-__Get_ConTeXt.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.12_BSVR__BSVR___Bulk_Set_Value_at_Runtime.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.130_GETA__-__GET_vector_memory_Address_information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.131_GETC__-__GET_Cycles.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.132_GETL__-__GET_Label.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.133_GETN__-__GEt_Testdata_Name.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.134_GETS__-__GET_Sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.135_GETV__-__GET_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.136_GETX__-__GET_eXtended_vector_information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.137_GNOS__-__GetNumberofOccupiedSets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.138_HREX__-__High_Resolution_EXecution.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.139_HRIT__HRIT__-__High_Resolution_Interval_of_Time.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.140_HROL__HROL__-__High_Resolution_Option_and_Level.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.141_HWTY__-__HardWare_TYpe.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.142_I2CA__I2CA__-__I2CA_bus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.143_INGV_-__INsert_Generate_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.144_INSI_-__INsert_Instructions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.145_INST__-__INSTrument_query.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.146_JRST_-__Jitter_modulator_ReseT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.150_JSUD_-__Jitter_Set_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.151_JSWF__-__Jitter_Set_WaveForm.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.152_LBMD__-__LoopBack_MoDe.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.153_LBRT__-__LoopBack_RouTing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.154_LBUD__LBUD__-__LaBel_User_Data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.157_LTDE__LTDE__-__Load_Test_Data_Entity.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.158_MCNT__-__Match_loop_CouNT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.159_MEAR__retrieve_MEAsurement_Results.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.15_CDCP__-__Cycle_Device_Cycle_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.160_MEAS_-__execute_a_MEASurement_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.161_MERL__MERL__-__Message_ERror_Limits.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.165_MVCU_-__Modify_Vector_variable_Configuration_Usage.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.166_MVVA_-__Modify_Vector_VAriable.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.167_NIFE__NIFE__-__Number_of_Independent_Fast_Error.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.168_NODV__-__Number_Of_Displayable_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.169_NOOP__NOOP__-__NO_OPeration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.16_CFCF__CFCF__-__Clock_Forwarding_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.170_OUTS__-__OUTput_Search.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.172_PADS__PADS__-__Pin_Attributes_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.174_PASS__-__PASS_or_fail_result.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.176_PDIV__-__Period_DIVider.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.177_PDMM__-__PDps_Miscellaneous_Measurement.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.178_PFND__-__Pin_FiND.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.179_PMUR___retrieve_PPMU_result.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.17_CFDF__CFDF__-__Clock_Forwarding_Set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.180_PQFC__PQFC__-__Parallel_Query_FoCus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.181_PRCF__PRCF__-__Pseudo_Random_bit_sequence_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.182_PRDF__PRDF__-__PRBS_set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.184_PRMD__-__PRBS_MoDe.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.185_PRPR__PRPR__-__PRBS_PRimary_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.187_PRUD_-__PRBS_set_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.189_PSEE_-__Power_Supply_External_trigger_measurement_Execute.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.18_CFPR__CFPR__-__Clock_Forwarding_PRimary_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.190_PSER__-__Power_Supply_External_trigger_measurement_Read_results.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.192_PSIE_-__Power_Supply_Internal_trigger_Execute.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.193_PSLC__PSLC__-__Power_Supply_Load_Capacitance.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.194_PSLR__PSLR__-__Power_Supply_Level_Ranges.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.198_PSST__PSST__-__Power_Supply_STatus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.19_CFUD_-__Clock_Forwarding_set_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.200_PTDE__PTDE__-__Path_for_Test_Data_Entities.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.201_PTDS__PTDS__-__Pin_attributes_Tweaking_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.202_RCLK__-__Reference_CLocK_source.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.203_RCLS__-__ReCeive_Level_Sensitivity.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.205_RDGC_-__Reset_DiGital_Capture.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.206_RLYC__RLYC__-__ReLaY_Control.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.207_RRDF_-__Result_Retention_area_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.208_RRSC_-__Result_Retention_area_Select_for_Capture.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.209_RRUD_-__Result_Retention_area_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.20_CHER__-__CHeck_ERrors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.211_RSSR__-__Retrieve_Spec_Search_Results.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.212_RRSU___Result_Retention_area_Select_for_Upload.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.213_RVCU_-__Remove_Vector_variable_Configuration_Usage.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.214_RVVA_-__Remove_Vector_VAriable.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.215_RVVC_-__Remove_Vector_Variable_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.216_SAOF__SAOF__-__Set_Alternating_Operation_Features.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.217_SATR__SATR__-__System_ATtRibutes.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.218_SCLK__-__System_CLocK_query.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.219_SDGC__SDGC__-__Setup_DiGital_Capture.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.21_CHFA__-__CHannel_FAil_flag.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.220_SDSC__-__Set_number_DeSCriptions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.221_SHSP__SHSP__-__SHmoo_SPecs.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.223_SLDO_-__Switch_Level_and_Dps_Order.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.224_SPCP__-__SPeCification_Port_list.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.225_SPEC__-__SPECification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.226_SPGV_-__SPlit_Generate_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.227_SPOP__SPOP__Set_Performance_Optimization_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.228_SPRM__SPRM__-__Set_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.229_SPST__-__SPecset_STatus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.230_SQBV__SQBV__-__SeQuencer_Break_Vector_insertion.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.231_SQEC__SQEC__-__SeQuencer_Execution_Context.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.232_SQGB__SQGB__-__SeQuencer_GloBal.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.233_SQIB__SQIB__-__SeQuencer_Interrupt_Behavior.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.234_SQIT__-__SeQuencer_InterRupt.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.235_SQLA__SQLA__-__SeQuencer_Label_Attribute.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.236_SQLB__SQLB__-__SeQuencer_LaBel_definition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.238_SQRC_-__SeQuencer_Remove_execution_Context.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.239_SQRP__SQRP__-__SeQuencer_Reference_Port.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.23_CHRS__CHRS__-__CHeck_Routing_Set_globally.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.240_SQSL__SQSL__-__SeQuencer_Start_Label.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.242_SQTO__SQTO__-__SeQuencer_TimeOut.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.243_SREC__SREC__-__Set_RECeiver_mask.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.244_SRPR__SRPR__-__Set_Routing_PRimary.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.245_SSAC__SSAC__-__Source_Synchronous_testing__Add_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.246_SSCT__SSCT__-__Source_Synchronous_data__Combine_and_Transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.247_SSRC_-__Source_Synchronous_testing__Remove_Configurations.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.248_SSTR__-__Source_Synchronous_Testing__Result_query.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.249_STDE_-__Save_Test_Data_Entity.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.254_TCMT__TCMT__-__Test_CoMment_Transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.255_TDEX__Test_Data_Extension.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.256_TEMP__-__read_TEMPerature.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.258_TMUD__Tester_Memory_Utilization_set_Default_values.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.259_TMUL___Tester_Memory_Utilization_Log.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.25_CLKC.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.260_TOCF__TOCF__-__Timing_Level_Offset_search_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.261_TOCR__TOCR__-__Timing_level_Offset_Configure_Result_pins.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.262_TORC_-__Timing_level_Offset_Result_Copy.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.263_TORN__-__Timing_level_Offset_search_RuN.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.264_TORR__Timing_level_Offset_Reset_Result.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.265_TORS__-__Timing_level_Offset_ReSult.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.266_TORT__-__Timing_Level_Offset_search_Result_Transitions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.267_TOUD_-__Timing_Offset_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.268_TPSE__TPSE__-__Test_Point_SEquence.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.269_TPSP__TPSP__-__TestPoint_SuPpression.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.270_TSCF__TSCF__-__TMU_Set_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.271_TSDF__TSDF__-__TMU_Set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.272_TSER__-__TMU_Set_ERror.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.273_TSHA__-__Timing_Setup_Has_Arming.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.274_TSRH__-__TMU_Set_Result_Handle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.275_TSMD__-__TMU_Set_Measurement_Done.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.276_TSPR__TSPR__-__TMU_Set_PRimary_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.277_TSRC__-__Time_Stamping_Results_Computed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.278_TSRS__-__TMU_Set_ReSults.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.279_TSRW__-__TMU_Set_RaW_results.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.27_CMNT__CMNT__-__CoMmeNT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.280_TSST__-__TeSt_STatus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.281_TSTL__TSTL__-__TeST_Label.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.282_TSUD_-__TMU_Set_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.284_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.285_TSVD__-__TimStamper_ValiD.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.286_TTCF__TTCF__-__Transition_Test_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.287_TTDB__-__Transition_Test_DeBug_information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.288_TTDF__TTDF__-__Transition_Test_set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.289_TTMD__-__Transition_Test_MoDe_query.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.28_CMVC_-__Clear_and_MoVe_Comments.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.290_TTPR__TTPR__-__Transition_Test_PRimary_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.291_TTRS__-__Time_TRansition_Search.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.292_TTST__-__Transition_Test_STatus_information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.293_TTUD_-__Transition_Test_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.294_TTVD__-__Transition_Test_ValiDate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.296_UDGP_-__UnDefine_GrouP.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.299_UDPT_-__UnDefine_PorT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.29_CNCT_-_CoNneCT_disCoNneCT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.300_UDRS_-__UnDefine_Routing_Set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.305_UPST__UPST__-__Utility_Purpose_STate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.306_UPTD__UPTD__-__UP_To_Date.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.307_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.308_UTDE_-__Unload_Test_Data_Entity.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.309_UTIN__-__UTility_line_INputs.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.30_CNGV_-__CoNnect_Generate_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.310_UTIX__-__UTility_line_Inputs_eXtended.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.311_UTOT__UTOT__-__UTility_line_OuTputs.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.312_UTSC__UTSC__-__UTility_line_Serial_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.313_UTST__UTST__-__UTility_line_STate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.314_UTTI__UTTI__-__UTility_line_settling_TIme.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.315_VALC__-__VALid_Cycle_range.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.316_VALD__-__VALid_Data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.317_VALR__-__VALid_Range.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.318_VCAT__VCAT__-__VeCtor_ATtachment.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.320_VCYC__-__Valid_CYCle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.321_VDCG__-__Verify_Device_Cycle_for_Group.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.322_VDCN_-__Vector_Device_Cycle_Name.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.323_VDCP__VDCP___Vector_Device_Cycle_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.324_VECC__VECC__-__VECtor_download_Compressed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.325_VECD__VECD__-__VECtor_Download.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.326_VNEC__-__Valid_Number_of_Executed_Cycles.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.327_VPAR__-__Vectors_in_PARallel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.328_VRCS__-__Valid_ReConStruction.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.32_CPYV_-__CopY_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.332_WAIT_-__WAIT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.334_WFDF__WFDF__-__WaveForm_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.336_WFEX__-__WaveForm_EXpected_data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.337_WFRE__-__WaveForm_REceived_data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.338_WFUD_-__WaveForm_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.339_WRST_-__Waveform_ReSeT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.33_CSAS__-__Channel_Slot_Accumulated_Status.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.340_WSDM__WSDM__-__Waveform_Set_Display_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.343_IDN__-__IDeNtify.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.344_OPT__-__hardware_OPTions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.345_RST_-__ReSeT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.34_CTST__-__Continuity_TeST.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.36_CYCI__-__get_CYCle_Information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.37_CYRM__CYRM__-__CYcle_Resolution_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.38_CYRP__-__CYcle_Resolution_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.39_CYRS__-__CYcle_Resolution_State.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.42_DCEL__DCEL__-__Digital_Compare_Exception_List.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.43_DCEX_-__DC_set_EXecute.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.44_DCGM__DCGM__-__Digital_Compare_Global_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.45_DCRE__-__DC_set_REsult.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.46_DCRM__DCRM__-__Digital_Compare_Result_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.47_DCRP__DCRP__-__Digital_Compare_Result_Positioning.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.48_DCRS__-__Digital_Compare_Result_Size.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.49_DCRT__DCRT__-__Digital_Compare_Result_Target.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.50_DCST__-__DC_SeT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.51_DCUD_-__Device_Cycle_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.55_DELI_-__DELete_Instruction.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.56_DELV_-__DELete_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.57_DFCR__DFCR__-__DeFine_Clock_Routing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.58_DFCT_-__DeFine_Continuity_Test.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.61_DFLV__DFLV__-__DeFaultLeVel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.62_DFPC__DFPC__-__DeFine_Pin_Comment.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.66_DFPT__DFPT__-__DeFine_PorT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.67_DFSP__DFSP__-__DeFine_Sampling_Profile.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.71_DGCM__-__DiGital_Capture_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.72_DGCS__DGCC___DiGital_Capture_aSynchronous.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.73_DGCT__-__DiGital_Capture_Test.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.74_DIAG_-__DIAGnostics.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.75_DIDT__DIDT__-__upload_DIgital_DaTa.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.76_DLPP_-__DeLete_Per_Pin_Subroutine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.77_DLSO__Driver_Level_Switch_Off.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.78_DLTS_-__DeLete_TeSt.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.79_DMAS__DMAS__-__Define_Memory_Area_Size.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.80_DPPC_-__Define_Per_Pin_subroutine_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.81_DPPS__DPPS__-__Define_Per_Pin_Subroutine_label.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.82_DPRL__DPRL__-__Default_PRimary_Level_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.83_DPRT__DPRT__-__Default_PRimary_Timing_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.84_DPSA__DPSA__-__Define_per_Pin_Subroutine_Address.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.85_DPSE__DPSE__-__Define_Power_Supply_External_trigger_measurement.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.86_DPSR__DPSR__-__Define_Parallel_SeaRch.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.87_DQUE__-__show_Data_QUEue_low_level.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.88_DRLS__-__DRive_Level_Sensitivity.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.92_DSVS__DSVS__-__Define_Spec_Value_Set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.93_DTCP__DTCP__-__Define_Technology_Control_Parameters.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.94_DVVA__DVVA__-__Define_Vector_VAriable.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.95_DVVC__DVVC__-__Define_Vector_Variable_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.96_DVCU__DVCU__-__Define_Vector_variable_Configuration_Usage.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.97_EAEX__-__Edge_Action_EXpected_data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.98_EARD__-__Edge_Action_Result_Data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.99_EARE__-__Edge_Action_REceived_data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.01.06_Defining_pin_groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.01.07_Defining_ports.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.01_CHIN__-__CHannel_INformation.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.02_CONF__CONF__-__CONFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.03_CTXT__CTXT__-__ConTeXT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.04_DFGE__DFGE__-__DeFine_Group_by_Expressions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.05_DFGP__DFGP__-__DeFine_GrouP.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.06_DFLV__DFLV__-__DeFaultLeVel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.07_DFPC__DFPC__-__DeFine_Pin_Comment.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.08_DFPN__DFPN__-__DeFine_Pin_Name.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.09_DFPS__DFPS__-__DeFine_Power_Supply.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.10_DFPT__DFPT__-__DeFine_PorT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.11_DFUP__DFUP__-__DeFine_Utility_Purpose.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.12_DFUT__DFUT__-__DeFine_UTility_line.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.13_DSCP__DSCP__-__Define_System_Control_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.14_GCTX__-__Get_ConTeXt.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.15_HWTY__-__HardWare_TYpe.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.16_PACT__PACT__-__Parallel_ACTivities_control.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.17_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.18_PFND__-__Pin_FiND.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.20_PRLT__-__request_Parallel_ResuLTs.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.21_PSSL__PSSL___Power_Supply_Safety_Limits.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.22_PSTE__PSTE__-__Parallel_SiTe_Enable.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.23_STME__STME__-__SiTe_Match_Enable.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.24_UDEF_-__UnDEFine_pin.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.25_UDGP_-__UnDefine_GrouP.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.26_UDPS_-__Undefine_DPS_pin.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.27_UDUP_-__UnDefine_Utility_Purpose.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.28_UDUT_-__UnDefine_UTility_line.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.29_UDVP_-__UnDefine_Virtual_Pin.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.30_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.31_UPST__UPST__-__Utility_Purpose_STate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.32_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.33_UTST__UTST__-__UTility_line_STate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.34_UTTI__UTTI__-__UTility_line_settling_TIme.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.36_IDN__-__IDeNtify.md>`、`<02_System_reference/02.06_Command_Reference/02.06.03.02.37_OPT__-__hardware_OPTions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.04.02.01_DSCP__DSCP__-__Define_System_Control_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.04.02.02_SRPR__SRPR__-__Set_Routing_PRimary.md>`、`<02_System_reference/02.06_Command_Reference/02.06.04.02.03_UDRS_-__UnDefine_Routing_Set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.02_CLMP__CLMP__-__CLaMP_level.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.03_DFSP__DFSP__-__DeFine_Sampling_Profile.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.04_DPRL__DPRL__-__Default_PRimary_Level_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.05_DRLV__DRLV__-__DRive_LeVel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.06_DSUS__DSUS__-__Dps_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.07_ENSP__ENSP__-__ENable_Sampling_Profile.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.08_EQFC__EQFC__-__EQualization_and_Filter_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.11_FTCG__FTCG__-__Functional_Test_ConfiGure.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.12_LSUS__LSUS__-__Level_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.13_LSUX__LSUX__-__Level_Sets_Used_eXtended.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.14_MERL__MERL__-__Message_ERror_Limits.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.15_PSLV__PSLV__-__Power_Supply_LeVel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.16_PSSR__PSSR__-_Power_Supply_Slew_Rate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.17_RCLS__-__ReCeive_Level_Sensitivity.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.18_RCLV__RCLV__-__ReCeive_LeVel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.19_RSET_-__ReSET.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.20_SDSC__-__Set_number_DeSCriptions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.21_SLDO_-__Switch_Level_and_Dps_Order.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.23_SPST__-__SPecset_STatus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.25_TERM__TERM__-__TERMination_mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.27_WAIT_-__WAIT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.05.02.28_RST_-__ReSeT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.01_APRM_-__Activate_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.02_BWDF__BWDF__-__Break_Waveform_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.03_BWDS__BWDS__-__Break_Waveform_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.04_CDCP__-__Cycle_Device_Cycle_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.05_CLKR__CLKR__-__CLocK_Resolution.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.06_DCDT__DCDT__-__Device_Cycle_DefaulT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.07_DCUD_-__Device_Cycle_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.08_DFCR__DFCR__-__DeFine_Clock_Routing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.09_DPRT__DPRT__-__Default_PRimary_Timing_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.10_DSCP__DSCP__-__Define_System_Control_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.11_EDDC__-__EDge_in_Device_Cycle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.12_EDSP__EDSP__-__EDge_SPecification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.13_EQFS_-__EQuation_FileS_command_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.14_EQSP__EQSP__-__EQuation_SPecification_transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.15_ETDS__ETDS__-__Edge_Timing_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.16_ETIM__ETIM__-__Edge_TIMing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.17_EUDS__-__Edge_Usage_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.18_EVCK__-__EVent_ClocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.19_FTCG__FTCG__-__Functional_Test_ConfiGure.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.20_PCLK__PCLK__-__Pin_CLocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.21_PDIV__-__Period_DIVider.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.22_RCLK__-__Reference_CLocK_source.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.23_RSET_-__ReSET.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.24_SCLK__-__System_CLocK_query.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.25_SDSC__-__Set_number_DeSCriptions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.26_SPCP__-__SPeCification_Port_list.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.27_SPEC__-__SPECification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.28_SPRM__SPRM__-__Set_PRiMary_sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.29_SPST__-__SPecset_STatus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.30_STRS__-__Spec_TRansition_Search.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.32_TSUS__TSUS__-__Timing_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.33_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.34_UPTD__UPTD__-__UP_To_Date.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.35_VCLK__-__Verify_CLocK.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.36_VDCG__-__Verify_Device_Cycle_for_Group.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.37_VTIM__-__Verify_TIMing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.38_VWFG__-__Verify_WaveForms_in_Groups.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.39_VWFS__-__Verify_WaveForm_Sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.40_WAVE__WAVE__-__WAVEform.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.41_WFDF__WFDF__-__WaveForm_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.42_WFDS__WFDS__-__WaveForm_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.43_WFUD_-__WaveForm_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.44_WRST_-__Waveform_ReSeT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.45_WSDM__WSDM__-__Waveform_Set_Display_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.06.02.46_WSUS__WSUS__-__Waveform_Sets_USed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.02_Label_definition__sequencer_program__and_sequencer_area.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.03_Sequencer_areas_and_vector_areas.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.04_Addressing_the_vector_areas.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.01_APDV_-__APpenD_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.02_APTS_-__APpend_TeSt.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.03_BCMT__BCMT__-__Binary_CoMmenT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.04_BLUP_-__BLock_UP_to_date.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.05_CMNT__CMNT__-__CoMmeNT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.06_CMVC_-__Clear_and_MoVe_Comments.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.07_CNGV_-__CoNnect_Generate_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.08_CPYV_-__CopY_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.09_DELI_-__DELete_Instruction.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.10_DELV_-__DELete_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.11_DLPP_-__DeLete_Per_Pin_Subroutine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.12_DLTS_-__DeLete_TeSt.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.13_DMAS__DMAS__-__Define_Memory_Area_Size.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.14_DPPC_-__Define_Per_Pin_subroutine_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.15_DPPS__DPPS__-__Define_Per_Pin_Subroutine_label.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.16_DPSA__DPSA__-__Define_per_Pin_Subroutine_Address.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.17_FTSM__FTSM__-__Functional_Test_Set_Mask.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.18_GETA__-__GET_vector_memory_Address_information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.19_INGV_-__INsert_Generate_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.20_INSI_-__INsert_Instructions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.21_NODV__-__Number_Of_Displayable_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.22_RSET_-__ReSET.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.23_SAOF__SAOF__-__Set_Alternating_Operation_Features.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.24_SPGV_-__SPlit_Generate_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.25_SQGB__SQGB__-__SeQuencer_GloBal.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.26_SQLA__SQLA__-__SeQuencer_Label_Attribute.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.27_SQLB__SQLB__-__SeQuencer_LaBel_definition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.29_SQSL__SQSL__-__SeQuencer_Start_Label.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.30_SQST__SQST__-__SeQuencer_STate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.31_SQTO__SQTO__-__SeQuencer_TimeOut.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.32_SREC__SREC__-__Set_RECeiver_mask.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.33_TCMT__TCMT__-__Test_CoMment_Transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.34_TSTL__TSTL__-__TeST_Label.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.35_VDCG__-__Verify_Device_Cycle_for_Group.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.36_VDCN_-__Vector_Device_Cycle_Name.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.37_VDCP__VDCP___Vector_Device_Cycle_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.38_VECC__VECC__-__VECtor_download_Compressed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.39_VECD__VECD__-__VECtor_Download.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.02.40_VPAR__-__Vectors_in_PARallel.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.01.02_Using_embedded_timing_and_level_search_on_a_Smart_Scale_system.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.01_CYRM__CYRM__-__CYcle_Resolution_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.02_DPSR__DPSR__-__Define_Parallel_SeaRch.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.03_DRLS__-__DRive_Level_Sensitivity.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.04_EDDC__-__EDge_in_Device_Cycle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.05_EDSP__EDSP__-__EDge_SPecification.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.06_ESGB__ESGB__-__Edge_Search_GloBal.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.07_EXSR_-__EXecute_SeaRch.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.08_FTSM__FTSM__-__Functional_Test_Set_Mask.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.09_FTST__-__Functional_TeST.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.10_RCLS__-__ReCeive_Level_Sensitivity.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.11_RSSR__-__Retrieve_Spec_Search_Results.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.12_SHSP__SHSP__-__SHmoo_SPecs.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.13_SHVL__SHVL__-__SHmoo_spec_VaLues.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.14_SQGB__SQGB__-__SeQuencer_GloBal.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.15_SREC__SREC__-__Set_RECeiver_mask.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.16_STRS__-__Spec_TRansition_Search.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.17_TOCF__TOCF__-__Timing_Level_Offset_search_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.18_TOCR__TOCR__-__Timing_level_Offset_Configure_Result_pins.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.19_TORC_-__Timing_level_Offset_Result_Copy.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.20_TORN__-__Timing_level_Offset_search_RuN.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.21_TORR__Timing_level_Offset_Reset_Result.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.22_TORS__-__Timing_level_Offset_ReSult.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.23_TORT__-__Timing_Level_Offset_search_Result_Transitions.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.24_TOUD_-__Timing_Offset_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.09.02.25_TTRS__-__Time_TRansition_Search.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.01.05_DC_measurements_using_a_PPMU_and_a_DC_Scale_DPS.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.01_CSAS__-__Channel_Slot_Accumulated_Status.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.02_CTXT__CTXT__-__ConTeXT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.03_DDIC__DDIC__-__Define_DUT_Interface_Connection.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.04_DFCT_-__DeFine_Continuity_Test.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.05_DPSE__DPSE__-__Define_Power_Supply_External_trigger_measurement.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.06_GNOS__-__GetNumberofOccupiedSets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.07_MEAS_-__execute_a_MEASurement_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.08_MSET__MSET__-__definition_of_Measurement_SET.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.09_PDMM__-__PDps_Miscellaneous_Measurement.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.10_PMUR___retrieve_PPMU_result.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.12_PSEE_-__Power_Supply_External_trigger_measurement_Execute.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.13_PSER__-__Power_Supply_External_trigger_measurement_Read_results.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.14_PSIE_-__Power_Supply_Internal_trigger_Execute.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.15_PSST__PSST__-__Power_Supply_STatus.md>`、`<02_System_reference/02.06_Command_Reference/02.06.10.02.16_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.01_CDCP__-__Cycle_Device_Cycle_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.02_CHER__-__CHeck_ERrors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.03_CHFA__-__CHannel_FAil_flag.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.04_CYCI__-__get_CYCle_Information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.05_CYRM__CYRM__-__CYcle_Resolution_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.06_CYRP__-__CYcle_Resolution_Parameter.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.07_CYRS__-__CYcle_Resolution_State.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.08_DCEL__DCEL__-__Digital_Compare_Exception_List.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.09_DCGM__DCGM__-__Digital_Compare_Global_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.10_DCRM__DCRM__-__Digital_Compare_Result_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.11_DCRP__DCRP__-__Digital_Compare_Result_Positioning.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.12_DCRS__-__Digital_Compare_Result_Size.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.13_DCRT__DCRT__-__Digital_Compare_Result_Target.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.14_EAEX__-__Edge_Action_EXpected_data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.15_EARD__-__Edge_Action_Result_Data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.16_EARE__-__Edge_Action_REceived_data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.17_EDGE__-__EDGE_errors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.18_EMAP__-__Error_MAP.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.19_ERCC__-__ERror_in_Cycle_range_Count.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.20_ERCT__-__ERror_CounT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.21_ERCY__-__ERror_CYcle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.22_ERMP__-__ERror_MaP.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.23_FFCI__-__First_Failed_Cycle_Information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.25_FTST__-__Functional_TeST.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.26_GETC__-__GET_Cycles.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.27_GETS__-__GET_Sets.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.28_GETV__-__GET_Vectors.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.29_GETX__-__GET_eXtended_vector_information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.30_PASS__-__PASS_or_fail_result.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.31_SQGB__SQGB__-__SeQuencer_GloBal.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.32_SQIB__SQIB__-__SeQuencer_Interrupt_Behavior.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.33_VALD__-__VALid_Data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.34_VALR__-__VALid_Range.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.35_VCYC__-__Valid_CYCle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.36_VNEC__-__Valid_Number_of_Executed_Cycles.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.37_VRCS__-__Valid_ReConStruction.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.38_WFEX__-__WaveForm_EXpected_data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.11.02.39_WFRE__-__WaveForm_REceived_data.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.01_Accessing_Utility_Lines.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.01_DFUP__DFUP__-__DeFine_Utility_Purpose.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.02_DFUT__DFUT__-__DeFine_UTility_line.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.03_UDUP_-__UnDefine_Utility_Purpose.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.04_UDUT_-__UnDefine_UTility_line.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.05_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.06_UPOW__UPOW__-__Utility_POWer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.07_UPST__UPST__-__Utility_Purpose_STate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.08_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.09_UTIN__-__UTility_line_INputs.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.10_UTIX__-__UTility_line_Inputs_eXtended.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.11_UTOT__UTOT__-__UTility_line_OuTputs.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.12_UTSC__UTSC__-__UTility_line_Serial_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.13_UTST__UTST__-__UTility_line_STate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.12.02.14_UTTI__UTTI__-__UTility_line_settling_TIme.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.01.01_TMU_per_Pin_overview.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.01.03_Storing_the_results_of_more_than_one_TMU_measurement.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.01_TSCF__TSCF__-__TMU_Set_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.02_TSDF__TSDF__-__TMU_Set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.03_TSER__-__TMU_Set_ERror.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.04_TSHA__-__Timing_Setup_Has_Arming.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.05_TSMD__-__TMU_Set_Measurement_Done.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.06_TSRH__-__TMU_Set_Result_Handle.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.07_TSPR__TSPR__-__TMU_Set_PRimary_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.08_TSRC__-__Time_Stamping_Results_Computed.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.09_TSRS__-__TMU_Set_ReSults.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.10_TSRW__-__TMU_Set_RaW_results.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.11_TSUD_-__TMU_Set_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.13.02.12_TSVD__-__TimStamper_ValiD.md>`、`<02_System_reference/02.06_Command_Reference/02.06.14.01.01_Principles_of_source_synchronous_testing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.14.02.01_SSAC__SSAC__-__Source_Synchronous_testing__Add_Configuration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.14.02.02_SSCT__SSCT__-__Source_Synchronous_data__Combine_and_Transfer.md>`、`<02_System_reference/02.06_Command_Reference/02.06.14.02.03_SSRC_-__Source_Synchronous_testing__Remove_Configurations.md>`、`<02_System_reference/02.06_Command_Reference/02.06.14.02.04_SSTR__-__Source_Synchronous_Testing__Result_query.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.01.01_Drift_and_transition_tracking.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.01_CFCF__CFCF__-__Clock_Forwarding_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.02_CFDF__CFDF__-__Clock_Forwarding_Set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.03_TTCF__TTCF__-__Transition_Test_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.04_TTDB__-__Transition_Test_DeBug_information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.05_TTDF__TTDF__-__Transition_Test_set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.06_TTMD__-__Transition_Test_MoDe_query.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.07_TTPR__TTPR__-__Transition_Test_PRimary_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.08_TTST__-__Transition_Test_STatus_information.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.09_TTUD_-__Transition_Test_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.15.03.10_TTVD__-__Transition_Test_ValiDate.md>`、`<02_System_reference/02.06_Command_Reference/02.06.16.01_Principles_of_jitter_injection.md>`、`<02_System_reference/02.06_Command_Reference/02.06.16.02.01_JRST_-__Jitter_modulator_ReseT.md>`、`<02_System_reference/02.06_Command_Reference/02.06.16.02.02_JSCF__JSCF__-__Jitter_Set_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.16.02.03_JSDF__JSDF__-__Jitter_Set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.16.02.04_JSPR__JSPR__-__Jitter_Set_PRimary_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.16.02.05_JSUD_-__Jitter_Set_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.16.02.06_JSWF__-__Jitter_Set_WaveForm.md>`、`<02_System_reference/02.06_Command_Reference/02.06.16.02.07_MSCF__MSCF__-__Modulation_Set_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.16.02.08_MSDF__MSDF__-__Modulation_Set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.17.01_Overview_of_pseudo_random_bit_sequences.md>`、`<02_System_reference/02.06_Command_Reference/02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.17.05.01_LBMD__-__LoopBack_MoDe.md>`、`<02_System_reference/02.06_Command_Reference/02.06.17.05.02_LBRT__-__LoopBack_RouTing.md>`、`<02_System_reference/02.06_Command_Reference/02.06.17.05.03_PRCF__PRCF__-__Pseudo_Random_bit_sequence_ConFiguration.md>`、`<02_System_reference/02.06_Command_Reference/02.06.17.05.04_PRDF__PRDF__-__PRBS_set_DeFinition.md>`、`<02_System_reference/02.06_Command_Reference/02.06.17.05.05_PRMD__-__PRBS_MoDe.md>`、`<02_System_reference/02.06_Command_Reference/02.06.17.05.06_PRPR__PRPR__-__PRBS_PRimary_set.md>`、`<02_System_reference/02.06_Command_Reference/02.06.17.05.07_PRUD_-__PRBS_set_UnDefine.md>`、`<02_System_reference/02.06_Command_Reference/02.06.18.02.01_ASWE__ASWE__-__Auto_SWing_Enable.md>`、`<02_System_reference/02.06_Command_Reference/02.06.18.02.02_ASWM__ASWM__-__Auto_SWing_Mode.md>`、`<02_System_reference/02.06_Command_Reference/02.06.18.02.03_FXDL__FXDL__-__FiXture_DeLay.md>`、`<02_System_reference/02.06_Command_Reference/02.06.18.02.04_PADS__PADS__-__Pin_Attributes_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.18.02.05_PTDS__PTDS__-__Pin_attributes_Tweaking_Definition_String.md>`、`<02_System_reference/02.06_Command_Reference/02.06.18.02.06_SATR__SATR__-__System_ATtRibutes.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Introduction to firmware commands › Firmware view）

As the following example shows, the `VECD?` query returns vector data from the sequencer memory in the range between 0 and 8, for the S0_1 pin.

Add the $ prefix to the query command to retrieve the binary data in a readable format.

 !`Executing the firmware command in the Firmware view`（raw: `../../../../raw/111040.png`）

### Syntax（取自子主题 Commands in alphabetical order › List of commands › APDV -  APpenD Vectors）

```
APDV {cmd_No}, {vect_length}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › APDV -  APpenD Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98313.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | A number that identifies the command within the sequencer area of the port to which the label belongs. Enter the command number of a GENV or RPTV instr…

### Example（取自子主题 Commands in alphabetical order › List of commands › APDV -  APpenD Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,520,,,(@)
< ...
> TSTL "test_1",(@)
> APDV 2,25
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,34,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,544,,,(@)
< ...
```

This example appends 25 vectors to the end of the sequencer construct with the command number 2. Note the change of the start address in command line 4.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › APRM -  Activate PRiMary sets）

```
APRM {mode}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › APRM -  Activate PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98485.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：mode | Selects the activation mode:

### Example（取自子主题 Commands in alphabetical order › List of commands › APRM -  Activate PRiMary sets）

```
APRM CNL
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › APTS -  APpend TeSt）

```
APTS {"label"}, {type}, {base_wf_set|"wavetable"|specset_id|"multiport_spec"} [,(port)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › APTS -  APpend TeSt）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98316.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：label | Defines the name of the new label. Enter an alphanumeric string in double quotes containing 1 to 128 characters.
> 表内引用（3 条，供检索）：`SQPG, SQPG? - (SeQuencer ProGramming)`（raw: `02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md`） · `DVCU, DVCU? - (Define Vector variable Configuration Usage)`（raw: `02.06.02.02.96_DVCU__DVCU__-__Define_Vector_variable_Configuration_Usage.md`） · `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › APTS -  APpend TeSt）

```
> APTS "test_2",MAIN,"gross_func_wtb"
> SQLB? ALL,ALL,(@)
< SQLB "test_1",MAIN,0,3,"gross_func_wtb"
< SQLB "test_2",MAIN,4,6,"gross_func_wtb"
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,12,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,520,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
```

This example appends a label to the sequencer area of the default port @. The label has the name `test_2`, is of type MAIN and is configured with the base wavetable `gross_func_wtb`. The following two queries display the result of the call. The STVA instruction of the new label points to the actual end of the vector areas.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › APTS -  APpend TeSt）

```
APTS "NEW",MAIN,"spec_port_1_port_2",(port_1)
```

This example appends the label `NEW` to the sequencer area of port `port_1`. The base wavetable is identified uniquely by specifying the multi-port specification `spec_port_1_port_2` and the port `port_1`, which belongs to `spec_port_1_port_2`.

### ASWE（取自子主题 Commands in alphabetical order › List of commands › ASWE  ASWE  -  Auto SWing Enable）

```
ASWE {waveform_set|specset_id}, {enable_status}
```

### ASWE?（取自子主题 Commands in alphabetical order › List of commands › ASWE  ASWE  -  Auto SWing Enable）

```
ASWE? {waveform_set|specset_id}
```

returns:

```
ASWE {waveform_set|specset_id}, {enable_status}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › ASWE  ASWE  -  Auto SWing Enable）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98486.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：waveform_set | Specifies the number of a waveform set for non-equation based testing. Enter PRM for the Primary Waveform Set, ALL for all waveform sets, or an i…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › ASWE  ASWE  -  Auto SWing Enable）

```
ASWE 1,ON
```

This example enables the automatic swing adjustment for waveform set 1.

### ASWM（取自子主题 Commands in alphabetical order › List of commands › ASWM  ASWM  -  Auto SWing Mode）

```
ASWM {command}, {mode}
```

### ASWM?（取自子主题 Commands in alphabetical order › List of commands › ASWM  ASWM  -  Auto SWing Mode）

```
ASWM?
```

returns:

```
ASWM {command}, {mode}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › ASWM  ASWM  -  Auto SWing Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98487.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：command | This parameter is used to set the specified mode:

### Example（取自子主题 Commands in alphabetical order › List of commands › ASWM  ASWM  -  Auto SWing Mode）

```
ASWM SET,AUTO
```

This example sets the swing adjustment mode AUTO.

### BCMD（取自子主题 Commands in alphabetical order › List of commands › BCMD  BCMD  - Binding CoMmanD）

```
BCMD "InstanceName",{Set | Reset | Action},"parameter", "value"
```

### BCMD?（取自子主题 Commands in alphabetical order › List of commands › BCMD  BCMD  - Binding CoMmanD）

```
BCMD? "InstanceName","parameter"
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › BCMD  BCMD  - Binding CoMmanD）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/10738.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：InstanceName | User-defined unique name to identify what type of binding instance is being controlled. It is a string without a ".".

### BCMT（取自子主题 Commands in alphabetical order › List of commands › BCMT  BCMT  -  Binary CoMmenT）

```
BCMT {vect_addr}, {vect_length}[, HIMEN][, (port)], {#spec(data)}
```

### BCMT?（取自子主题 Commands in alphabetical order › List of commands › BCMT  BCMT  -  Binary CoMmenT）

```
BCMT? [(portlist)]
```

returns:

```
BCMT {vect_addr}, {vect_length}[, HIMEN][, (port)], {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98488.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：vect_addr | The first vector of the segment for which comments are to be transferred. This number counts the active vectors of the port (as specified for the po…

### Example（取自子主题 Commands in alphabetical order › List of commands › BCMT  BCMT  -  Binary CoMmenT）

```
> BCMT?
< BCMT 0,49,#9000000078&!This is the first vector
  of test_2&0This is the first vector of test_3
```

This call of BCMT? displays the comments of the default port. The `&` character (with the decimal ASCII value 38) indicates the (identical) length of the two comments. The first comment is at vector 33 (decimal ASCII value of the ! character), the second at vector 48 (decimal ASCII value of the 0 character).

### BDID（取自子主题 Commands in alphabetical order › List of commands › BDID  BDID  -  BoarD ID）

```
BDID {-1|0|2|3}, {"string"}
```

### BDID?（取自子主题 Commands in alphabetical order › List of commands › BDID  BDID  -  BoarD ID）

```
BDID? {-1|0|2|3|ALL}
```

returns:

```
BDID {0|2|3}, {"string"}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98489.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：address | Specifies how the value of the string parameter is to be processed. Possible values are:

### BLUP（取自子主题 Commands in alphabetical order › List of commands › BLUP -  BLock UP to date）

```
BLUP {"name"}, {type}, {state},
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › BLUP -  BLock UP to date）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98490.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：name | The name of a label.

### Example（取自子主题 Commands in alphabetical order › List of commands › BLUP -  BLock UP to date）

```
BLUP "test",LBL,UPDT,
```

This example sets the state of label `test` to up to date.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › BSVE -  Bulk Set Value Evaluation）

```
BSVE {spec_value_set_no}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › BSVE -  Bulk Set Value Evaluation）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118973.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：spec_value_set_no | Number of a spec value set.

### Example（取自子主题 Commands in alphabetical order › List of commands › BSVE -  Bulk Set Value Evaluation）

```
> BSVE 11
```

### BSVR（取自子主题 Commands in alphabetical order › List of commands › BSVR  BSVR   Bulk Set Value at Runtime）

```
BSVR {spec_value_set_no}, {"spec_name"|"spec_name@port_name"}, {value}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › BSVR  BSVR   Bulk Set Value at Runtime）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118969.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：spec_value_set_no | Number of a spec value set. The set must have been defined with DSVS.
> 表内引用（1 条，供检索）：`Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › BSVR  BSVR   Bulk Set Value at Runtime）

```
> DSVS 11, "per", TIM,1,1
> BSVR 11,"per1",30
> BSVR 11,"per2",60
> BSVR? 11
< BSVR 11,"per1",30
< BSVR 11,"per2",60
```

### BWDF（取自子主题 Commands in alphabetical order › List of commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### BWDF?（取自子主题 Commands in alphabetical order › List of commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF? {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {(pinlist)}
```

returns:

```
BWDF {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › BWDF  BWDF  -  Break Waveform DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98497.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number …
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

This example defines a pulse for waveform set 1, and for pins D0 to D3, driving to 1 at edge action 4 and to 0 at edge action 5. The tri-state formatter is not used.

### BWDS（取自子主题 Commands in alphabetical order › List of commands › BWDS  BWDS  -  Break Waveform Definition String）

```
BWDS {wvf_set}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

### BWDS?（取自子主题 Commands in alphabetical order › List of commands › BWDS  BWDS  -  Break Waveform Definition String）

```
BWDS? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {(pinlist)}
```

returns:

```
BWDS {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98498.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. Enter PRM for the Primary waveform set. The maximum number is determined by…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `WFDS, WFDS? - (WaveForm Definition String)`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › BWDS  BWDS  -  Break Waveform Definition String）

```
> BWDS? 1,,,(@)
< BWDS 1,,,"",(io)
< BWDS 1,,,"d1:F00 d5:F10",(clk)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CDCP  -  Cycle Device Cycle Parameter）

```
CDCP? {start_cycle}, {no_of_cycles}, {strt_disp}, {disp_length}, {(pinlist)}
```

returns:

```
CDCP {cycle}, {dev_cyc_name}, {dev_cyc_len}, {DD1}, {DD2}, {ED1}, {ED2}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CDCP  -  Cycle Device Cycle Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98499.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle to be analyzed. The range of values for this parameter depends on the analysis mode: In the Start …

### Example（取自子主题 Commands in alphabetical order › List of commands › CDCP  -  Cycle Device Cycle Parameter）

```
> CDCP? 0,8,0,8,(S0_1)
< CDCP 0,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 1,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 2,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 3,"MYDC",2,F00,N,N,N,(S0_1)
< CDCP 5,"MYDC",2,F10,N,N,N,(S0_1)
< CDCP 7,"DNRZ",1,F10,N,N,N,(S0_1)
> CDCP? 2,6,4,2,(S0_1)
< CDCP 5,"MYDC",2,F10,N,N,N,(S0_1)
< CDCP 7,"DNRZ",1,F10,N,N,N,(S0_1)
```

In the second call of CDCP? (the first call just serves to display the underlying situation) the range of interest starts at vector 6. Note that the reply starts with vector 5, and that the first occurrence of MYDC, which lies between vector 2 and vector 6, is not displayed.

### CFCF（取自子主题 Commands in alphabetical order › List of commands › CFCF  CFCF  -  Clock Forwarding ConFiguration）

```
CFCF {"cf_name"}, {(source_pin)}, {(sink_pins)} [, speed]
```

### CFCF?（取自子主题 Commands in alphabetical order › List of commands › CFCF  CFCF  -  Clock Forwarding ConFiguration）

```
CFCF? {"cf_name"}, {(pinlist)}
```

returns:

```
CFCF {"cf_name"}, {(source_pin)}, {(sink_pins)} [, speed]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CFCF  CFCF  -  Clock Forwarding ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117851.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：cf_name | Specifies the name of a clock forwarding set that must have been defined with CFDF.
> 表内引用（1 条，供检索）：`Implementation details of clock forwarding`（raw: `02.06.15.01.01.05.01_Implementation_details_of_clock_forwarding.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › CFCF  CFCF  -  Clock Forwarding ConFiguration）

```
> CFCF? "cf_set1",(@)
< CFCF "cf_set1",(Pin1),(Pin3, Pin2)
< CFCF "cf_set1",(Pin4),(Pin5)
> CFCF "cf_set1",(Pin1),(Pin6, Pin3)
> CFCF "cf_set1",(Pin7),(Pin4)
> CFCF? "cf_set1",(@)
> CFCF "cf_set1",(Pin1),(Pin6, Pin3)
> CFCF "cf_set1",(Pin7),(Pin4)
```

### CFDF（取自子主题 Commands in alphabetical order › List of commands › CFDF  CFDF  -  Clock Forwarding Set DeFinition）

```
CFDF {"cf_set_name"} [, "mode_context"]
```

### CFDF?（取自子主题 Commands in alphabetical order › List of commands › CFDF  CFDF  -  Clock Forwarding Set DeFinition）

```
CFDF? ["cf_set_name"]
```

returns:

```
CFDF {"cf_set_name"} [, "mode_context"]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CFDF  CFDF  -  Clock Forwarding Set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117850.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cf_set_name | In the command, this is the name of a new clock forwarding set. In the query, it is a name of an existing clock forwarding set. If you omit this p…

### Example（取自子主题 Commands in alphabetical order › List of commands › CFDF  CFDF  -  Clock Forwarding Set DeFinition）

```
> CFDF   "cf_set1"
> CFDF   "cf_set2"
> CFDF   "cf_set3"

> CFDF?
< CFDF   "cf_set1"
< CFDF   "cf_set2"
< CFDF   "cf_set3"
```

### CFPR（取自子主题 Commands in alphabetical order › List of commands › CFPR  CFPR  -  Clock Forwarding PRimary set）

```
CFPR {"cf_set_name"}
```

### CFPR?（取自子主题 Commands in alphabetical order › List of commands › CFPR  CFPR  -  Clock Forwarding PRimary set）

```
CFPR?
```

returns:

```
CFPR {"cf_set_name"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CFPR  CFPR  -  Clock Forwarding PRimary set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117943.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：cf_set_name | Specifies the name of an existing clock forwarding set. Specify an empty string to inactivate the current primary set and thus to disable clock fo…

### Example（取自子主题 Commands in alphabetical order › List of commands › CFPR  CFPR  -  Clock Forwarding PRimary set）

```
> CFPR   "cf_set1"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CFUD -  Clock Forwarding set UnDefine）

```
CFUD {"cf_set_name"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CFUD -  Clock Forwarding set UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117926.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cf_set_name | Specifies the name of an existing clock forwarding set.

### Example（取自子主题 Commands in alphabetical order › List of commands › CFUD -  Clock Forwarding set UnDefine）

```
> CFUD   "cf_set1"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CHER  -  CHeck ERrors）

```
CHER? [MUX,] {(pinlist)}
```

returns:

```
CHER {res_flag}, [MUX,] {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CHER  -  CHeck ERrors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98500.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：MUX | If this flag is set, and one of the specified (Pin Scale) pins is multiplexed to an HXA pin, then the result returned for this Pin Scale pin will be combi…

### Example（取自子主题 Commands in alphabetical order › List of commands › CHER  -  CHeck ERrors）

After a functional test has been performed, sending CHER? returns the result for each pin in pinlist.

```
CHER? (@)
```

returns:

```
CHER F,(Q0,Q1)
CHER P,(Q2)
CHER F,(Q3)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CHFA  -  CHannel FAil flag）

```
CHFA? [MUX,] {(pinlist)}
```

returns:

```
CHFA {res_flag}, [MUX,] {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CHFA  -  CHannel FAil flag）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98501.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：MUX | If this flag is set, and one of the specified (Pin Scale) pins is multiplexed to an HXA pin, then the combined result from all Pin Scale pins multiplexed …

### Example（取自子主题 Commands in alphabetical order › List of commands › CHFA  -  CHannel FAil flag）

```
CHFA? (D1)
```

returns:

```
CHFA F, (D1)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CHIN  -  CHannel INformation）

```
CHIN? {channel_nr|ALL}
```

returns:

CHIN {channel_nr}, {channel_type}, [phys_location], {board_no}, [clk_board], [chan_info_1], [chan_info_2]

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CHIN  -  CHannel INformation）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98502.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：24 行 × 3 列。
> 首行（上游原文）：channel_nr | The number that identifies the channel. Specify ALL if you want information about all channels. For a digital channel, specify it with the test sys…
> 表内引用（3 条，供检索）：`DFPN, DFPN? - (DeFine Pin Name) for the number)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） · `DFPS, DFPS? - (DeFine Power Supply)`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） · `*OPT? - (hardware OPTions)`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md`）

### Examples（取自子主题 Commands in alphabetical order › List of commands › CHIN  -  CHannel INformation）

```
CHIN? 10901
```

returns:

```
CHIN 10901,PSIO,120601,109,21,512,0
```

```
CHIN? ALL
```

  Return (for example):

```
CHIN 10101,PYIO,110301,101,11,3551,0
CHIN 10102,PYIO,110302,101,11,3551,0

CHIN 21701,DPS128HC,-1,217,31,191,0
CHIN 21702,DPS128HC,-1,217,31,191,0

```

### CHRS（取自子主题 Commands in alphabetical order › List of commands › CHRS  CHRS  -  CHeck Routing Set globally）

```
CHRS {ON|OFF}
```

### CHRS?（取自子主题 Commands in alphabetical order › List of commands › CHRS  CHRS  -  CHeck Routing Set globally）

```
CHRS?
```

returns:

```
CHRS {ON|OFF}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CHRS  CHRS  -  CHeck Routing Set globally）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98503.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：OFF | SmarTest tries to fulfill an inconsistent request as well as possible. This is the default.

### CLKR（取自子主题 Commands in alphabetical order › List of commands › CLKR  CLKR  -  CLocK Resolution）

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res}
```

### CLKR?（取自子主题 Commands in alphabetical order › List of commands › CLKR  CLKR  -  CLocK Resolution）

```
CLKR?[type,] {waveform_set|specset_id|"multi-port_spec"}
```

returns:

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res|clock_res}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CLKR  CLKR  -  CLocK Resolution）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98504.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `Automatic calculation of period resolution for single-port setups`（raw: `02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › CLKR  CLKR  -  CLocK Resolution）

```
> CLKR 1,,10
> CLKR? 1
< CLKR 1,1000,10

```

This example sets and queries the period resolution (10 ns) for waveform set 1. Ignore the returned value of the ref_period parameter.

```
> CLKR? "spec_port_1_port_2"
< CLKR "spec_port_1_port_2",50,5.555555556
```

This example queries the period resolution for the multi-port specification `spec_port_1_port_2`.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CLKC）

```
CLKC? <specset | specificationName>, (portName)
```

returns:

```
CLKC <spscset | specificationName>, mater_clock_ns, edge_clock_ns, (portName)
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/152895.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：specset | The required specification set.

### CLMP（取自子主题 Commands in alphabetical order › List of commands › CLMP  CLMP  -  CLaMP level）

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### CLMP?（取自子主题 Commands in alphabetical order › List of commands › CLMP  CLMP  -  CLaMP level）

```
CLMP? {level_set|level_set_id}, {(pinlist)}
```

returns:

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CLMP  CLMP  -  CLaMP level）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98505.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：level_set | The identification number of the level set in which you want the levels to be included. The number must not exceed the maximum number of level sets …

### Example（取自子主题 Commands in alphabetical order › List of commands › CLMP  CLMP  -  CLaMP level）

```
CLMP 1,ON,-10,5100,(Q0,Q1,Q2,Q3)
```

This example sets the clamp levels for level set 1 for pins Q0, Q1, Q2 and Q3. The low clamp level is set to -10 mV, and the high clamp level is set to 5100 mV.

### CMNT（取自子主题 Commands in alphabetical order › List of commands › CMNT  CMNT  -  CoMmeNT）

```
CMNT {act_vect_of_port}, {"text"}[, (port)]
```

### CMNT?（取自子主题 Commands in alphabetical order › List of commands › CMNT  CMNT  -  CoMmeNT）

```
CMNT? {act_vect_of_port}, [vect_length][, (port)]
```

returns:

```
CMNT {act_vect_of_port}, {"text"}[, (port)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CMNT  CMNT  -  CoMmeNT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98506.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：act_vect_of_port | Specifies the active vector of the referenced port at which the comment is to be inserted, or, in the query, the first vector of which the co…

### Example（取自子主题 Commands in alphabetical order › List of commands › CMNT  CMNT  -  CoMmeNT）

Display the sequencer area of the default port:

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
< SQPG 5,STVA,528,,,(@)
< SQPG 6,STSA,,,,(@)
< SQPG 7,GENV,12,,,(@)
< SQPG 8,STOP,,,,(@)
```

Add the comment "Start of test_2" to the active vector 15 of the default port @, that is, to the first active vector of the second label:

```
> CMNT 15,"Start of test_2"
```

Activate test_2 for editing and display the comments for its vectors with the label specific TCMT? query:

```
> TSTL "test_2",(@)
> TCMT? 0,11
< TCMT 0,"Start of test_2"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CMVC -  Clear and MoVe Comments）

CMVC {src_vec_No}, {dst_vec_No}, {vect_length}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CMVC -  Clear and MoVe Comments）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98507.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：src_vec_No | The logical vector number that determines the start of the source range.

### Example（取自子主题 Commands in alphabetical order › List of commands › CMVC -  Clear and MoVe Comments）

```
> CMNT? 0,6
< CMNT 0,"0"
< CMNT 1,"1"
< CMNT 2,"2"
< CMNT 3,"3"
< CMNT 4,"4"
< CMNT 5,"5"
> TSTL "test_1",(@)
> CMVC 0,4,2
> CMNT? 0,6
< CMNT 4,"0"
< CMNT 5,"1"
```

This example moves comments in the vector range 0 to 1 to the range 4 to 5. The previous comments for vectors 4 and 5 are overwritten, the comments for vector 2 and 3 are cleared.

### CNCT（取自子主题 Commands in alphabetical order › List of commands › CNCT - CoNneCT disCoNneCT）

```
CNCT {mode}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CNCT - CoNneCT disCoNneCT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99085.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：mode | OFF: Disconnects all pins in the specified modules. CNCT? always returns OFF as mode.

CNCT disconnects the pins immediately.

The following rules apply if the CNCT command is used in conjunction with PPS cards:

- CNCT disconnects all 16 output pins in the PPS module, even in multisite testing.
- CNCT does not change the output voltage of the PPS core when disconnecting the pins.

### Example（取自子主题 Commands in alphabetical order › List of commands › CNCT - CoNneCT disCoNneCT）

To set all defined PPS pins to 0 V and disconnect all output pins of the PPS modules:

```
FORC 0,(@)
CNCT OFF,(@)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CNGV -  CoNnect Generate Vectors）

```
CNGV {(cmd_No)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CNGV -  CoNnect Generate Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98508.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number which references the first of the two consecutive GENV sequencer constructs.

### Example（取自子主题 Commands in alphabetical order › List of commands › CNGV -  CoNnect Generate Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,GENV,8,,,(@)
< SQPG 4,STOP,,,,(@)
> TSTL "test_1",(@)
> CNGV 2
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,17,,,(@)
< SQPG 3,STOP,,,,(@)
```

### CONF（取自子主题 Commands in alphabetical order › List of commands › CONF  CONF  -  CONFiguration）

```
CONF ["context",]{pin_type},[pin_oper_mode],{(pinlist)}


```

### CONF?（取自子主题 Commands in alphabetical order › List of commands › CONF  CONF  -  CONFiguration）

```
CONF? ["context"|ALL,] {(pinlist)}
```

returns:

```
CONF ["context",]{pin_type},{pin_oper_mode},{(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CONF  CONF  -  CONFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98510.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 6 列，含嵌套表。
> 首行（上游原文）：context | This extra parameter specifies a mode context. If it is omitted, the default mode context DEFAULT is set or read. If DEFAULT is the only context defin…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98510.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：I | Configures a drive pin.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98510.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：DCSIGNAL | In the query this indicates that the pin is associated with a DC Scale channel and has been configured in PMU mode with DFPN.

### Example 1（取自子主题 Commands in alphabetical order › List of commands › CONF  CONF  -  CONFiguration）

```
> CONF IO,F160,(D0,D1)
```

This example configures pins `D0` and `D1` as bidirectional pins operating in Standard Mode for the default mode context.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › CONF  CONF  -  CONFiguration）

```
> CONF? (sdd,vdd)
< CONF DC,DCSIGNAL,(sdd)
< CONF DC,POWER,(vdd)
```

This example queries the DC Scale channels `sdd` and `vdd`, which were set with `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） to PMU mode (`DCSIGNAL`) and with `DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） to DPS mode (`POWER`), respectively.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CPYV -  CopY Vectors）

```
CPYV {src_vec_No}, {dst_vec_No}, {vect_length}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98511.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：src_vec_No | The logical vector number that determines the start of the source range.

### Example（取自子主题 Commands in alphabetical order › List of commands › CPYV -  CopY Vectors）

```
> SQPG? all,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
> $VECD? PARA,SM,504,24,(S0_1)
< VECD PARA,SM,504,24,(S0_1),
  0000 0001  0000 0001  0000 0001  0000 0001  0000 0001  0000 0011  0000 0001  0000 0001
  0000 0001  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000
  0000 0000  0000 0000  0000 0000  0000 0001  0000 0011  0000 0001  0000 0000  0000 0000
```

The first three active vectors of the RPTV instruction (with the logical vector numbers 9 to 11) are set to 0 for pin S0_1. Now activate the label for editing and copy vectors 12 to 14 to position 9 for S0_1:

```
> TSTL "test_1",(@)
> CPYV 12,9,3,(S0_1)
```

Display the result:

```
> $VECD? PARA,SM,504,24,(S0_1)
< VECD PARA,SM,504,24,(S0_1),
  0000 0001  0000 0001  0000 0001  0000 0001  0000 0001  0000 0011  0000 0001  0000 0001
  0000 0001  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000
  0000 0001  0000 0011  0000 0001  0000 0001  0000 0011  0000 0001  0000 0000  0000 0000
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CSAS  -  Channel Slot Accumulated Status）

```
CSAS? [msMode,] {mask}, {(pinlist)}
```

returns:

```
CSAS {status}, {(pinlist)}

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/144688.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CSAS  -  Channel Slot Accumulated Status）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/144688.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 4 列，含嵌套表。
> 首行（上游原文）：msMode | The extra parameter controls how the return value is created.The value of the parameter can be PQFC: PQFC specified: The current query focus is respect…


 | msMode  | The extra parameter controls how the return value is created.

The value of the parameter can be PQFC:

- PQFC specified: The current query focus is respected and allows status query per site without affecting status bits of other sites.
- PQFC not specified: The command reads (and clears) status bits of all enabled and active sites at a glance, ignoring the actual query focus.
The parameter applies only to use of parameter mask as integer value. |
 |

mask

   | Integer bit mask or ALL.

-

Integer bit mask: Integer value is used to mask out individual status bits. Each bit of mask is logically AND-ed with the corresponding bit of the DPS status. If one of the resulting bits is set, then F (Fail) is returned, otherwise P (Pass).

It is used to check for an error condition. All bit positions of the status flags that should be checked, must be set to 1 in mask. If one of the selected status bits is set, then CSAS? returns F.

- ALL: Hex value (hexadecimal representation of all status bits) is returned.
For setting the integer bit mask or interpreting a returned hex value, refer to the `status`（raw: `02.06.02.02.33_CSAS__-__Channel_Slot_Accumulated_Status.md#_144688__r_status`） parameter below. |
 |

pinlist

 |

Comma separated list of DPS128/64 or XPS256 pins. The @ character can be used to read the status for all DPS pins.

 |
 |

status

   | If mask is ALL, you need to translate the hex value (hexadecimal representation of the status bits) to its binary form as follows:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/144688.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：Bit 0: | High voltage or current of surge tracker exceeded

If mask is specified as an integer bit-mask:

- Pass: P
- Fail: F
 |

### Example 1:（取自子主题 Commands in alphabetical order › List of commands › CSAS  -  Channel Slot Accumulated Status）

```
CSAS? 3,(VCC)
```

returns either

```
CSAS P,(VCC)
```

or

```
CSAS F,(VCC)
```

The example uses the integer bitmask and checks whether a spike on the `VCC` pin exceeded the low or high limit.

- P = Pass

No spike occurred since the last CSAS? query.

- F = Fail

Either the low or high limit or both were exceeded.

### Example 2:（取自子主题 Commands in alphabetical order › List of commands › CSAS  -  Channel Slot Accumulated Status）

```
CSAS? ALL,(Vaux)
```

returns

```
CSAS #H10,(Vaux)
```

The example uses the ALL specifier and checks for an error condition on the `Vaux` pin.

- Bit 3 = 0

No "Measurement range change failed" error. All set current measurement range requests were successful.

- Bit 4 = 1

The "Clamp current correction failed". A high-accuracy clamp current correction for a DCVH setup with execution mode SER_HAC or PAR_HAC was not successful.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CTST  -  Continuity TeST）

```
CTST? {mode}
```

returns:

```
CTST {result},{(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CTST  -  Continuity TeST）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98512.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：mode | The mode is:

### Example（取自子主题 Commands in alphabetical order › List of commands › CTST  -  Continuity TeST）

```
DFCT
10.000,1700.000,200.000,700.000,SPOL,(p1,p2,p3,p4)
CTST? GPF
```

This example uses the command to set up the parameters needed to execute a continuity test on pins p1 to p4. The parameters are as follows:

- Force current = 10 mA
- Commutation voltage = 1.7 V
- Voltage minimum pass value = 200 mV
- Voltage maximum pass value = 700 mV
- Single polarity measurement selected.

It then executes the test with the CTST command using the global pass/fail mode.

### CTXT（取自子主题 Commands in alphabetical order › List of commands › CTXT  CTXT  -  ConTeXT）

```
CTXT {action},{"name"}
```

### CTXT?（取自子主题 Commands in alphabetical order › List of commands › CTXT  CTXT  -  ConTeXT）

```
CTXT?ALL
```

returns:

```
CTXT {DEFINE},{"name"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CTXT  CTXT  -  ConTeXT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98513.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：action | Specifies the action. Possible values are:

### Example（取自子主题 Commands in alphabetical order › List of commands › CTXT  CTXT  -  ConTeXT）

```
> CTXT? ALL
< CTXT DEFINE,"DEFAULT"
< CTXT DEFINE,"differential"
< CTXT DEFINE,"PdrvNPrcv"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CYCI  -  get CYCle Information）

CYCI? {start_cycle}, {no_of_cycles}, {resolution_mode} [,MUX] [,(port)]

returns:

CYCI {cycle}, [res_mode] [, (port)], {vector_number}, [label], [type], [seq_status], [comment], [no_of_waveforms] [,MUX], {#spec(data)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CYCI  -  get CYCle Information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99098.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：73 行 × 8 列。
> 首行（上游原文）：start_cycle | The start cycle is an integer that defines the first cycle to be reported. The start cycle is in the range 0 to 248 when the sequencer runs in the…

### Example（取自子主题 Commands in alphabetical order › List of commands › CYCI  -  get CYCle Information）

CYCI? 20,2,CYCL

returns:

CYCI 20,11,"TEST1",SVEC,RPTV,"comment",1,

#9000000046

 dvc_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x04\x99

 dvc_02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x0F\x0F\x00

CYCI 21,12,"TEST1",SVEC,GENV,,1,

#9000000046

 dvc_03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x04\x05\x0F\x6C

 dvc_04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x04\x0F\x0F\x0D

This example returns result information (on the cycle level) for 2 cycles and 2 output pins of the label `TEST1`, which is of type SVEC. The first cycle was generated by a RPTV instruction from logical vector 11 and has an associated comment, the second cycle was generated by a GENV instruction for logical vector 12.

The binary data reports the device cycle names, which in this example are different for each pin and cycle. The waveform offsets are zero. The reported drive/expected/received data are:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99098.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：dvc_01: | DD1 = F00, DD2 = F10, ED1 = FX, ED2 = F0 error: high received on edge 3 (param E2)

### CYRM（取自子主题 Commands in alphabetical order › List of commands › CYRM  CYRM  -  CYcle Resolution Mode）

```
CYRM {resolution_mode}, [error_limit], {(pinlist)}
```

### CYRM?（取自子主题 Commands in alphabetical order › List of commands › CYRM  CYRM  -  CYcle Resolution Mode）

```
CYRM? {(pinlist)}
```

returns:

```
CYRM {resolution_mode},[error_limit], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CYRM  CYRM  -  CYcle Resolution Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98515.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：resolution_mode | Defines the resolution mode. This can be:
> 表内引用（1 条，供检索）：`Retrieving edge information by repeating the test`（raw: `02.06.11.01.02.02.01_Retrieving_edge_information_by_repeating_the_test.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › CYRM  CYRM  -  CYcle Resolution Mode）

```
CYRM CYCL,,(@)
CYRM CYCL,,(MatchLoopPin)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CYRP  -  CYcle Resolution Parameter）

```
CYRP [recovery],[shots]
CYRP?
```

returns:

```
CYRP {recovery},{shots}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CYRP  -  CYcle Resolution Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98516.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：recovery | Specifies whether the test is repeated with all receive edges enabled after the last fine granularity shot. This serves to reset the hardware registe…

### Example（取自子主题 Commands in alphabetical order › List of commands › CYRP  -  CYcle Resolution Parameter）

```
CYRP NRCR,ONE
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › CYRS  -  CYcle Resolution State）

```
CYRS? {(pinlist)}
CYRS {result_state}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › CYRS  -  CYcle Resolution State）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98517.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：result_state | Specifies the result state of the selected pins. Possible values are:

### Example（取自子主题 Commands in alphabetical order › List of commands › CYRS  -  CYcle Resolution State）

```
CYRS? (Out1,Out2)
CYRS CYCL,(Out1,Out2)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DCCH -  DC Current measurement High precision pmu）

```
DCCH {`setNr`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_setNr`）}, `[prechargeVoltage`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_prechargeVoltage`）], `[forceMode`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_forceMode`）,] `[forceValue`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_forceValue`）], `[clampValue`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_clampValue`）], `[voltageDrop`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_voltageDrop`）,]
            `[lowThreshold`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_lowThreshold`）], `[highThreshold`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_highThreshold`）], `[forceRange`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_forceRange`）,] `[compareMode`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_compareMode`）], `[settlingTime`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_settlingTime`）],
            `[clampRange`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_clampRange`）,] `[relayAction`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_relayAction`）], `[measureCurrentRange`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_measureCurrentRange`）,] `[executionMode`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_executionMode`）],
            `[connectState`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_connectState`）,] `[samples`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_samples`）,] {(`pinlist`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_pinList`）)} `, ([refPinList`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md#_98518__r_refPinList`）)]



> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 10 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。







> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I | The force value is to be specified as current in µA (Microampere).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I | The clamp value is to be specified as output clamp voltage in mV (Millivolt). This is the default mode.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 5 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：Property | Value type | Description
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 6 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：Property | Value type | Description
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 7 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I | The force current range is to be specified in µA (Microampere).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 8 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：Value | Mode | Description
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 9 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I | The clamp voltage range is to be specified in mV (Millivolt).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 11 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：SER | Serial measurement (all pins of a site are measured sequentially)
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：50 行 × 35 列，含嵌套表。
> 首行（上游原文）：setNr | The DC set identification number, starting with 1.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98518.htm`
> 中**第 12 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：Property | Value | Description

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DCCH -  DC Current measurement High precision pmu）

Precondition:

```
DCCH 1,,1000,6000,-4170,-3830,I,0,NO,SER,(pin1,pin2,pin3)
```

Execution:

```
DCEX 1, MEAS_VAL
```

Result:

```
DCRE? 1, VAL
DCRE P, -4103.3, (pin1)
DCRE F, 200.1, (pin2)
DCRE P, -3908.4, (pin3)
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DCCH -  DC Current measurement High precision pmu）

Precondition:

```
DCCH 1,,I,100000,"lowLimit:-1000 highLimit:10000",0,100000,I,0,NT,PAR,"HC_AWG:ON",(pin1, pin2),(refPin1,refPin2)
```

Execution:

```
DCEX 1, FORCE_ON
```

### Example 3（取自子主题 Commands in alphabetical order › List of commands › DCCH -  DC Current measurement High precision pmu）

Precondition:

```
DCCH 1,,V,10000,"lowLimit:-100000 highLimit:200000",0,100000,I,0,NT,PAR,(pin1, pin2)
```

Execution:

```
DCEX 1, FORCE_ON
```

### DCDT（取自子主题 Commands in alphabetical order › List of commands › DCDT  DCDT  -  Device Cycle DefaulT）

```
DCDT {waveform_set}, {"default_name"}
```

### Example（取自子主题 Commands in alphabetical order › List of commands › DCDT  DCDT  -  Device Cycle DefaulT）

```
DCDT 1,"HOLD"
```

This example defines the default device cycle name HOLD for Waveform Set 1.

```
DCDT? "fast_ARM",(ARMPort)
DCDT "fast_ARM","Cycle",(ARMPort)
```

This example queries the default device cycle name for the ARMPort port in the multi-port specification fast_ARM.

### DCEL（取自子主题 Commands in alphabetical order › List of commands › DCEL  DCEL  -  Digital Compare Exception List）

```
DCEL {DCRT}, {TP}, {action}, {(pinlist)}
```

### DCEL?（取自子主题 Commands in alphabetical order › List of commands › DCEL  DCEL  -  Digital Compare Exception List）

```
DCEL? {DCRT}, {parameter}, {(pinlist)}
```

returns:

```
DCEL? {DCRT}, {parameter}, {action}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DCEL  DCEL  -  Digital Compare Exception List）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/128210.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：DCRT | The command for which an exception list is to be created. Currently, DCRT is the only allowed command.

### Example（取自子主题 Commands in alphabetical order › List of commands › DCEL  DCEL  -  Digital Compare Exception List）

```
> DCRT RAM,(portA)
> DFPT? (portA)
< DFPT (p1,p2,p3),(portA)
> DCEL DCRT,TP,(p2)
> DCEL? DCRT,TP,(portA)
< DCEL DCRT,TP,SET,(p2)
> DCEL DCRT,TP,(p1,p3)
> DCEL? DCRT,TP,(portA)
< DCEL DCRT,TP,SET,(p1,p2,p3)
> DCRT? (portA)
< DCRT RAM,(portA)
```

Note that you can add further pins to the exception list, and that the settings of DCRT are not changed even if all three pins of `portA` are in the exception list.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DCEX -  DC set EXecute）

```
DCEX {setNr}, [mode]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DCEX -  DC set EXecute）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98521.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：setNr | The DC Set Identification number, starting with 1.
> 表内引用（2 条，供检索）：`DCCH`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md`） · `DCVH`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › DCEX -  DC set EXecute）

Precondition:

```
DCVH 1,,20000,200,-100,100,I,25,NTBBM,PAR,(pin1,pin2,pin3)
```

Execution:

```
DCEX 1, MEAS_VAL
```

Result:

```
DCRE? 1,
DCRE P, 10.3, (pin1)
DCRE F, 200.1, (pin2)
DCRE P, 20.4, (pin3)
```

### DCGM（取自子主题 Commands in alphabetical order › List of commands › DCGM  DCGM  -  Digital Compare Global Mode）

```
DCGM {acqu_mode},{emap_pos_int},{ovem_pos_int}
```

### DCGM?（取自子主题 Commands in alphabetical order › List of commands › DCGM  DCGM  -  Digital Compare Global Mode）

```
DCGM? [answer_type] [,"exec_context"]
```

returns:

```
DCGM {acqu_mode},{emap_pos_int},{ovem_pos_int}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DCGM  DCGM  -  Digital Compare Global Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98522.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 4 列。
> 首行（上游原文）：acqu_mode | Specifies the recording mode for the detailed Error Map. Possible values are:

### Example（取自子主题 Commands in alphabetical order › List of commands › DCGM  DCGM  -  Digital Compare Global Mode）

```
DCGM FAIL,STRT,NONE
```

This example sets the error map into acquire failure mode and specifies that the error map position is to be interpreted as a start value for the detailed error map, and to be ignored for the overview error map.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DCRE  -  DC set REsult）

```
DCRE? setNr,[resultMode]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98523.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 6 列，含嵌套表。
> 首行（上游原文）：setNr | The DC set identification number, starting with 1.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98523.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：GPF | A single result, which includes the pass/fail result of the pins, specified in the DC set. A pass is only returned if all pins passed the test.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98523.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 6 列，含嵌套表。
> 首行（上游原文）：setNr | The DC set identification number, starting with 1.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98523.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：P | Pass

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DCRE  -  DC set REsult）

Preconditions:

```
DCVH 1,,20000,200,-100,100,I,25,NTBBM,PAR,(pin1, pin2, pin3)
DCEX 1, MEAS_VAL
```

Result:

```
DCRE? 1, VAL
DCRE 1,P, 10.3, (pin1)
DCRE 1,F, 200.1, (pin2)
DCRE 1,P, 20.4, (pin3)
```

Result:

```
DCRE? 1, GPF
DCRE 1,F,, ()
```

Result:

```
DCRE? 1, PPF
DCRE 1,P,, (pin1,pin3)
DCRE 1,F,, (pin2)
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DCRE  -  DC set REsult）

Preconditions:

```
DCVH 1,,20000,200,-100,100,I,25,NTBBM,PAR,(pin1, pin2, pin3)
DCEX 1, MEAS_VAL
```

Result:

```
DCRE? 1,
DCRE 1,P, 10.3, (pin1)
DCRE 1,F, 200.1, (pin2)
DCRE 1,P, 20.4, (pin3)
```

Result:

```
DCRE? 1, GPF
DCRE 1,F,, ()
```

Result:

```
DCRE? 1, PPF
DCRE 1,P,, (pin1,pin3)
DCRE 1,F,, (pin2)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DCRM  DCRM  -  Digital Compare Result Mode）

DCRM

```
DCRM {map},{mode},[bits],["sub_cycles",] {(port_list)}
```

 DCRM?

```
DCRM? [answer_type,] {map},{(port_list)}
```

returns:

```
DCRM {map},{mode},[bits],[sub_cycles,] {(port)}


```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DCRM  DCRM  -  Digital Compare Result Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98524.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 5 列。
> 首行（上游原文）：Received


> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98524.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：FCM | A fixed number of cycles is combined into one result. The number can be defined by a second call of DCRM, where the number is specified as the mode parame…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98524.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：22 行 × 10 列，含嵌套表。
> 首行（上游原文）：map | Specifies which error map will be configured. Possible values are:

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DCRM  DCRM  -  Digital Compare Result Mode）

```
DCRM EMAP,4,PF,"c1:1,3 c2:5,7 c3:2,4 c4:6,8",(P1,P2)
```

This example configures the detailed Error Map of port `P1` and `P2` to record 1 bit results for 4 sub-cycles, each of which combines two different edges.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DCRM  DCRM  -  Digital Compare Result Mode）

```
DCRM EMAP,1,PFC,(P1,P2)
```

This example configures the Error Map to record one global detailed two bit result combining all edges of a cycle at every test execution.

### Example 3（取自子主题 Commands in alphabetical order › List of commands › DCRM  DCRM  -  Digital Compare Result Mode）

```
DCRM OVEM,6000,,(@)
```

This example defines that 6000 cycles will be compressed into one Overview Error Map bit when the next test will be executed.

### DCRP（取自子主题 Commands in alphabetical order › List of commands › DCRP  DCRP  -  Digital Compare Result Positioning）

```
DCRP {error_map_pos},{(ref_port)}
```

### DCRP?（取自子主题 Commands in alphabetical order › List of commands › DCRP  DCRP  -  Digital Compare Result Positioning）

```
DCRP? [answer_type,]{(port_list)}
```

returns:

```
DCRP {error_map_pos},{(port)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DCRP  DCRP  -  Digital Compare Result Positioning）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98525.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：error_map_pos | Specifies the start or stop position for Error Map recording. The interpretation of the value is determined by DCGM independently for both error…

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DCRP  DCRP  -  Digital Compare Result Positioning）

```
> PCLK? "mu_burst",1,(@@)
< PCLK "mu_burst",1,20,(P1)
< PCLK "mu_burst",1,10,(P2)
> DCGM ALL,STRT,NONE
> DCRP 20,(P2)
> DCRP? (@@)
< DCRP 10,(P1)
< DCRP 20,(P2)
```

This example illustrates the calculation of the cycle numbers for the ports that are not used as the reference port. For interpretation mode STRT, recording will start for the reference port `P2` with cycle 16 (largest multiple of 8 smaller than 20). Since the period length for `P1` is twice the period length of `P2`, recording for `P1` will start with cycle 8 (largest multiple of 8 smaller than 10).

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DCRP  DCRP  -  Digital Compare Result Positioning）

```
> SQGB STSQ,14,(P2)
> DCGM ALL,HALT,NONE
> DCRP 20,(P2)
> DCRP? (@@)
< DCRP 7,(P1)
< DCRP 14,(P2)
> SQGB STRD,
> DCRP? (@@)
< DCRP 10,(P1)
< DCRP 20,(P2)
```

This example shows that a definition of the Error Map position with DCRP is ignored when the sequencer mode is STSQ, but that it can subsequently be activated. Note that the DCGM command only serves to make the initial ineffectiveness of the definition visible. It is not possible to execute a functional test with these settings when the sequencer mode is STSQ.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DCRS  -  Digital Compare Result Size）

```
DCRS? [answer_type,] {map},[mode],[bits],{(port_list)}
```

returns:

```
DCRS {map},{x-mode},{bits},{no_of_cycles},{(port)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98526.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 4 列。
> 首行（上游原文）：answer_type | This parameter specifies whether the current configuration or the configuration of the last executed test is to be returned. Possible values are:

### Example（取自子主题 Commands in alphabetical order › List of commands › DCRS  -  Digital Compare Result Size）

```
> DCGM ALL,HALT,NONE
> DCRT TP,(P1)
> DCRM EMAP,8,PF,(P1)
> CYRM CYCL,,(P1)
> DCRS? EMAP,,,(P1)
< DCRS EMAP,8,PF,2048,(P1)
> DCRP 3360,(P1)
> FTST?
> EMAP? PPIN,1312,2048,EDGE,8,PF,ALL,BYTE,(P1)
```

This example shows how to get hold of the first cycles of your area of interest under the following conditions:

- The area of interest is greater than the capacity of the error map.
- The acquire mode is set to ALL with DCGM, so that the first recorded cycles will be overwritten when the error map is full before the end of the test.

The solution is to interpret the error map position defined with DCRP as a stop value (by setting the second parameter of DCGM to HALT), and to calculate the last cycle to be recorded as:

```
first_cycle_of_interest + capacity_of_the_Error_Map
```

In the example, the first addend is 1312. The second addend is determined with the DCRS? query.

### DCRT（取自子主题 Commands in alphabetical order › List of commands › DCRT  DCRT  -  Digital Compare Result Target）

```
DCRT {target},{(port_list)}
```

### DCRT?（取自子主题 Commands in alphabetical order › List of commands › DCRT  DCRT  -  Digital Compare Result Target）

```
DCRT? [answer_type,] {(port_list)}
```

returns:

```
DCRT {target},{(port)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DCRT  DCRT  -  Digital Compare Result Target）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98527.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 4 列。
> 首行（上游原文）：target | Specifies the target area for the error map. Possible values are:

### Examples（取自子主题 Commands in alphabetical order › List of commands › DCRT  DCRT  -  Digital Compare Result Target）

### Querying the location of the error map for all ports and setting it for specific ones (multi-port label)

This example queries the location of the error map for all ports. Then, it sets the location of the error map in the test processor for port `P2`, and in RDRAM for `P1`:

```
DCRT? (@@) // Note: this is equivalent to specifying DCRT? CONF,(@@)
DCRT RAM,(P1) // Set location of error map for port P1 in RDRAM
DCRT TP,(P2) // Set location of error map for port P2 in Test Processor
```

### Querying and setting the location of the result map for the default port (non multi-port label)

To query or set the location of the error map for the default port, you need to specify @ as the port_list of the DCRT? and DCRT commands, respectively:

```
DCRT? (@) // Query location of error map for the default port
DCRT TP,(@) // Set location of error map for the default port to Test Processor
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DCST  -  DC SeT）

```
DCST? {setNr}
DCST? ALL
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DCST  -  DC SeT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98528.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：setNr | The DC set identification number, starting with 1.

The query returns the DC set definition with the syntax as described for `DCCH`（raw: `02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.md`） and `DCVH`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md`）.

### Example 1: Read a specific setup（取自子主题 Commands in alphabetical order › List of commands › DCST  -  DC SeT）

Precondition

```
DCVH 1,,20000,200,-100,100,I,25,NTBBM,PAR,(pin1, pin3)
DCCH 1,,4000,200,-100,100,I,25,NTBBM,PAR,(pin2)
DCVH 3,,20000,200,-100,100,I,25,NTBBM,PAR,(pin4)
DCCH 2,,7000,3000,100,2000,I,25,NTBBM,PAR,(pin5)
```

  Execution

```
Task>  DCST? 1
DCVH 1,,20000,200,-100,100,I,25,NTBBM,PAR,(pin1,pin3)
DCCH 1,,4000,200,-100,100,I,25,NTBBM,PAR,(pin2)
```

  The example works in offline mode for five PS1600 pins.

### Example 2: Read all setups（取自子主题 Commands in alphabetical order › List of commands › DCST  -  DC SeT）

Precondition

```
DCVH 1,,20000,200,-100,100,I,25,NTBBM,PAR,(pin1, pin3)
DCCH 1,,4000,200,-100,100,I,25,NTBBM,PAR,(pin2)
DCVH 3,,20000,200,-100,100,I,25,NTBBM,PAR,(pin4)
DCCH 2,,7000,3000,100,2000,I,25,NTBBM,PAR,(pin5)
```

  Execution

```
Task>  DCST? ALL
DCVH 1,,20000,200,-100,100,I,25,NTBBM,PAR,(pin1,pin3)
DCCH 1,,4000,200,-100,100,I,25,NTBBM,PAR,(pin2)
DCCH 2,,7000,3000,100,2000,I,25,NTBBM,PAR,(pin5)
DCVH 3,,20000,200,-100,100,I,25,NTBBM,PAR,(pin4)
```

All defined DC sets are returned. The sort order is defined by the DC set identification number. The example works in offline mode for five PS1600 pins.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DCUD -  Device Cycle UnDefine）

```
DCUD {waveform_set},{"dev_cyc_name"},{(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DCUD -  Device Cycle UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98529.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › DCUD -  Device Cycle UnDefine）

```
DCUD 1,"WRITE"
```

This example deletes the device cycle `WRITE` for waveform set 1 from the device cycle table.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DCVH -  DC Voltage measurement High precision pmu）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I | Specifies the force current mode. Parameter forceValue is to be defined in µA (Microampere). This is the default force mode.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I | The force value is to be specified as current in µA (Microampere).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I | The clamp value is to be specified as output clamp voltage in mV (Millivolt). This is the default mode.


```
DCVH {`setNr`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_setNr`）}, `[prechargeVoltage`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_prechargeVoltage`）], `[forceMode`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_forceMode`）,] `[forceValue`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_forceValue`）], `[clampValue`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_clampValue`）], `[voltageDrop`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_voltageDrop`）,]
            `lowThreshold`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_lowThreshold`）], `[highThreshold`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_highThreshold`）], `[forceRange`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_forceRange`）,] `[compareMode`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_compareMode`）], `[settlingTime`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_settlingTime`）],
            `[clampRange`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_clampRange`）,] `[relayAction`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_relayAction`）], `[measureVoltageRange`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_measureVoltageRange`）,] `[executionMode`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_executionMode`）],
            `[connectState`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_connectState`）,] `[samples`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_samples`）,] {(`pinList`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_pinList`）)} `, ([refPinList`（raw: `02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.md#_98530__r_refPinList`）)]



> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 10 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。




> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 5 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列，含 rowspan。
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：55 行 × 35 列，含嵌套表。
> 首行（上游原文）：setNr | The DC set identification number, starting with 1.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 6 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：Property | Value type | Description
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 7 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I | The force current range is to be specified in µA (Microampere).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 8 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：Value | Mode | Description
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 9 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：I | The clamp voltage range is to be specified in mV (Millivolt).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 11 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：SER | Serial measurement (all pins of a site are measured sequentially).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98530.htm`
> 中**第 12 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：Property | Value | Description

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DCVH -  DC Voltage measurement High precision pmu）

Precondition:

```
DCVH 1,,1,1000,4820,5180,i,0,no,ser,(pin1, pin2, pin3)
```

Execution:

```
DCEX 1, MEAS_VAL
```

Result:

```
DCRE? 1, VAL
DCRE P, 4903.3, (pin1)
DCRE F, 200.1, (pin2)
DCRE P, 5108.4, (pin3)
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DCVH -  DC Voltage measurement High precision pmu）

Precondition:

```
DCVH 2,,,,100,200,i,0,TERM,HIZ,(pin1)
```

Execution:

```
DCEX 2, MEAS_VAL
```

Result:

```
DCRE? 2, VAL
DCRE F, 4903.3, (pin1)
```

### Example 3（取自子主题 Commands in alphabetical order › List of commands › DCVH -  DC Voltage measurement High precision pmu）

Precondition:

```
DCVH 1,,I,200000,"lowLimit:-1000 highLimit:5000",-500,4700,I,0,NT,PAR,"DIFF_VM:ON",(pin1, pin2),(refPin1,refPin2)
```

Execution:

```
DCEX 1, FORCE_ON
```

### Example 4（取自子主题 Commands in alphabetical order › List of commands › DCVH -  DC Voltage measurement High precision pmu）

Precondition:

```
DCVH 1,,V,10000,"lowLimit:-100000 highLimit:200000",-500,9000,I,0,NT,PAR,(pin1, pin2)
```

Execution:

```
DCEX 1, FORCE_ON
```

### DDIC（取自子主题 Commands in alphabetical order › List of commands › DDIC  DDIC  -  Define DUT Interface Connection）

```
DDIC ["connectionSet",] {"circuitry_type"}, {(cp1,cp2)}
```

### DDIC?（取自子主题 Commands in alphabetical order › List of commands › DDIC  DDIC  -  Define DUT Interface Connection）

```
DDIC? {"circuitry_type"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DDIC  DDIC  -  Define DUT Interface Connection）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106906.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 4 列。
> 首行（上游原文）：connectionSet | This parameter is currently not used. This extra string parameter adds the ability to define several pins containing the same DC Scale channel i…

### Example 1: Ganging（取自子主题 Commands in alphabetical order › List of commands › DDIC  DDIC  -  Define DUT Interface Connection）

```
DDIC CONN, (207GO,209GI)
DDIC? ALL
```

returns

```
DDIC CONN, (207GO,209GI)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DELI -  DELete Instruction）

```
DELI {cmd_No}, {count}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DELI -  DELete Instruction）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98536.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number which references the first sequencer instruction to be deleted.

### Example（取自子主题 Commands in alphabetical order › List of commands › DELI -  DELete Instruction）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,27,,,(@)
< SQPG 3,RPTV,7,5,,(@)
< SQPG 4,STOP,,,,(@)
< SQPG 5,STVA,544,,,(@)
< ...
> DELI 2,1
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,7,5,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,544,,,(@)
< ...
```

This example deletes the sequencer instruction with command number 2 from the sequencer area of the default port @. Note that since the vectors of the instruction are not deleted, the start address of the following label (STVA instruction at command number 4) does not change.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DELV -  DELete Vectors）

```
DELV {cmd_No}, {vect_length}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DELV -  DELete Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98537.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number which references the sequencer construct where vectors are to be deleted. The instruction of the construct must be GENV (GENerate Ve…

### Example（取自子主题 Commands in alphabetical order › List of commands › DELV -  DELete Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,34,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,544,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
> TSTL "test_1",(@)
> DELV 2,25
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,520,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
```

This example deletes 25 vectors from the end of the sequencer construct referenced by command number 2. Three memory words become inactive in the process and are deleted. The start address of the following label (command line 4) is adjusted.

### DFCR（取自子主题 Commands in alphabetical order › List of commands › DFCR  DFCR  -  DeFine Clock Routing）

```
DFCR {source_group},{dest_group}
```

### DFCR?（取自子主题 Commands in alphabetical order › List of commands › DFCR  DFCR  -  DeFine Clock Routing）

```
DFCR?
```

returns (for every group except G4):

```
DFCR {source_group},{dest_group}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFCR  DFCR  -  DeFine Clock Routing）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98541.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：source_group | specifies the hardware group whose local clock is to be routed to dest_group. The format is Gx, where x is the group number.

### Example（取自子主题 Commands in alphabetical order › List of commands › DFCR  DFCR  -  DeFine Clock Routing）

```
> DFCR?
<
> DFCR G1,G8
> DFCR?
< DFCR G4,G3
< DFCR G4,G1
< DFCR G4,G5
< DFCR G1,G6
< DFCR G1,G2
< DFCR G1,G8
< DFCR G1,G7
```

This example changes the default routing (DFCR? gives an empty reply). Note that the inherited clocks of G6 and of all successors of G6 are also changed.

### DFCT（取自子主题 Commands in alphabetical order › List of commands › DFCT -  DeFine Continuity Test）

```
DFCT {force_current}, {commutation_voltage}, {pass_volt_min}, {pass_volt_max}, {polarity}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFCT -  DeFine Continuity Test）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98542.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：force_current | The force_current parameter specifies the current (in [micro ]A) that the active load sources or sinks. The range is 0 to 35 mA for the Pin Scal…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98542.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：pass_volt_min | This parameter specifies (in mV) the minimum pass value of the test. It defines the low level threshold for the comparator during the measuremen…

This parameter specifies (in mV) the maximum pass value of the test. It defines the high level threshold for the comparator during the measurement.

   | Note If pass_volt_min > pass_volt_max, the two parameters are swapped around internally.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98542.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：polarity | The polarity is as follows:

### Example（取自子主题 Commands in alphabetical order › List of commands › DFCT -  DeFine Continuity Test）

```
DFCT 10000,1700,200,700,SPOL,(p1,p2,p3,p4)
CTST? GPF
```

This example sets up the parameters needed to execute a continuity test on pins `p1` to `p4`. The parameters are as follows:

-  Force current = 10 mA
-  Commutation voltage = 1.7 V
-  Voltage minimum pass value = 200 mV
-  Voltage maximum pass value = 700 mV
-  Single polarity measurement selected

The example also includes the CTST? (Continuity TeST) query used to execute the test.

### DFGE（取自子主题 Commands in alphabetical order › List of commands › DFGE  DFGE  -  DeFine Group by Expressions）

```
DFGE {group_type}, {"group_expression"}, {(pin_group)}
```

### DFGE?（取自子主题 Commands in alphabetical order › List of commands › DFGE  DFGE  -  DeFine Group by Expressions）

```
DFGE? {(pin_group)}
```

returns:

```
DFGE {group_type}, {("group_expression")}, {(pin_group)}
```

for expression-based groups, and

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

for digital fixed groups.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFGE  DFGE  -  DeFine Group by Expressions）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98544.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 4 列。
> 首行（上游原文）：group_type | Defines the type of pins in the group. This can be:

### Example（取自子主题 Commands in alphabetical order › List of commands › DFGE  DFGE  -  DeFine Group by Expressions）

```
> DFGP? (SCAN)
< DFGP X,(SI1,SI2,SO1,SO2),(SCAN)
> DFGP? (OUT)
< DFGP O,(O1,SO1,SO2),(OUT)
> DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGE? (SCAN_OUT)
< DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGP? (SCAN_OUT)
< DFGP O,(SO1,SO2),(SCAN_OUT)
```

This example defines a group called SCAN_OUT which contains the pins that occur both in pin groups OUT and SCAN. Note that you must use the DFGP? query to display the pins of SCAN_OUT. DFGE? returns the group definition.

The same result would be obtained with the definition

```
> DFGE O,"OUT - O1",(SCAN_OUT)
```

### DFGP（取自子主题 Commands in alphabetical order › List of commands › DFGP  DFGP  -  DeFine GrouP）

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### DFGP?（取自子主题 Commands in alphabetical order › List of commands › DFGP  DFGP  -  DeFine GrouP）

```
DFGP? {(pin_group)}
```

returns:

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFGP  DFGP  -  DeFine GrouP）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98546.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：pin_type | Defines the type of pins in the group. This can be:

### Example（取自子主题 Commands in alphabetical order › List of commands › DFGP  DFGP  -  DeFine GrouP）

```
DFGP O,(Q0,Q1,Q2,Q3),(outputs)
```

This example defines a group called outputs which contains pins Q0, Q1, Q2 and Q3.

### DFLV（取自子主题 Commands in alphabetical order › List of commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV [resourceSpecifier,] [mode,] {value}
```

### DFLV?（取自子主题 Commands in alphabetical order › List of commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV? [resourceSpecifier] [, mode]
```

returns

```
DFLV VIL,STD,value
DFLV VIH,STD,value
DFLV VIHH,STD,value
DFLV VOL,STD,value
DFLV VOH,STD,value
DFLV VOL_DIFF,STD,value
DFLV VOH_DIFF,STD,value
DFLV VT,STD,value
DFLV VCOM,STD,value
DFLV REC_OFFSET,STD,value
DFLV REC_SWING,STD,value
```

if neither parameter resourceSpecifier nor parameter mode have been specified.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFLV  DFLV  -  DeFaultLeVel）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/349982.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 4 列，含嵌套表。
> 首行（上游原文）：resourceSpecifier | The extra parameter specifies the resource to be set or queried. The following resources are supported: Resource specifier | Description
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/349982.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：Resource specifier | Description

### Example 1: Resource and mode specified（取自子主题 Commands in alphabetical order › List of commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV VIL,STD,100

```

This example sets the default value for the VIL resource in STD mode to 100 mV. Other default values are not modified.

### Example 2: Resource specified, mode omitted（取自子主题 Commands in alphabetical order › List of commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV VIL,100
DFLV VIH,200
```

This example sets the default value for the VIL resource to 100 mV, and VIH to 200 mV. As no operating mode is specified, the values are applied only for the STD mode.

### Example 3: Reset single resource（取自子主题 Commands in alphabetical order › List of commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV VIL, RESET
```

Sets the default value for the VIL resources to the technology defined default value for all operating modes. This overwrites potential user-defined values by the initial system value.

### Example 4: Reset all default values to the technology defined values and query all values（取自子主题 Commands in alphabetical order › List of commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV RESET
DFLV? ALL, ALL
```

returns

```
DFLV VIL,STD,2250
DFLV VIH,STD,2500
DFLV VIHH,STD,0
DFLV VOL,STD,2250
DFLV VOH,STD,2500
DFLV VOL_DIFF,STD,0
DFLV VOH_DIFF,STD,0
DFLV VT,STD,2500
DFLV VCOM,STD,2500
DFLV REC_OFFSET,STD,1200
DFLV REC_SWING,STD,3200
```

for the cmos technology.

### DFPC（取自子主题 Commands in alphabetical order › List of commands › DFPC  DFPC  -  DeFine Pin Comment）

```
DFPC {(pin)}, {"comment"}
```

### DFPC?（取自子主题 Commands in alphabetical order › List of commands › DFPC  DFPC  -  DeFine Pin Comment）

```
DFPC? {(pinlist)}
```

returns:

```
DFPC {(pin)}, {"comment"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFPC  DFPC  -  DeFine Pin Comment）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131109.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：pin | In the command, this is the pin to which a comment is to be added. In the query reply, it is the pin whose comment is returned.

### Example（取自子主题 Commands in alphabetical order › List of commands › DFPC  DFPC  -  DeFine Pin Comment）

```
> DFPC (pin1), "This is a comment to pin1"
> DFPC? (pin1,pin2)
< DFPC (pin1), "This is a comment to pin1"
```

Since no comment has been defined for pin `pin2`, it is ignored in the reply.

### DFPN（取自子主题 Commands in alphabetical order › List of commands › DFPN  DFPN  -  DeFine Pin Name）

```
DFPN ["connectionSet",] {channelNo_1|(list_of_DC_scale_channels)}, ["pinNo"], {(pinName)}
```

### DFPN?（取自子主题 Commands in alphabetical order › List of commands › DFPN  DFPN  -  DeFine Pin Name）

```
DFPN? {(pinlist)}
```

returns:

```
DFPN {channelNo_1|(list_of_DC_scale_channels)}, ["pinNo"], {(pinName)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFPN  DFPN  -  DeFine Pin Name）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98550.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：connectionSet | This parameter is currently not used. This extra string parameter adds the ability to define several pins containing the same DC Scale channel i…
> 表内引用（2 条，供检索）：`DDIC`（raw: `02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md`） · `Pogo pin assignment - Utility pogo blocks`（raw: `../02.03_DUT_board_design_reference/02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DFPN  DFPN  -  DeFine Pin Name）

```
> DFPN 10101,"1",(Clock)
> DFPN 10102,"2",(D0)
> DFPN? (@)
< DFPN 10101,"1",(Clock)
< DFPN 10102,"2",(CD0)
```

The above example allocates the `Clock` pin to channel 10101 and allocates pin `D0` to channel 10102, and then queries these definitions. The device pin numbers allocated are 1 and 2 respectively.

```
DFPN (11901, 11902),,(vee)
```

This example defines ganging for DC Scale channels in PMU mode.

### DFPR（取自子主题 Commands in alphabetical order › List of commands › DFPR  DFPR  -  DeFine Pin Role）

```
DFPR "alias_set_name","pin_alias", (package_pin_name)
```

### DFPR（取自子主题 Commands in alphabetical order › List of commands › DFPR  DFPR  -  DeFine Pin Role）

```
DFPR?DEF|ALL, (alias_set_name::pin_alias|alias_set_name|@)
```

returns:

```
DFPR "alias_set_name", "pin_alias", (package_pin_name)
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFPR  DFPR  -  DeFine Pin Role）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112436.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：alias_set_name | The alias set name. If you assign a pair of pin alias and package pin name to a nonexistent alias set, an alias set is created named with this …

### Examples（取自子主题 Commands in alphabetical order › List of commands › DFPR  DFPR  -  DeFine Pin Role）

### Generic case

The pin configuration file includes three pins: `CP`, `S0`, and `S1`. There are two alias sets, `FUNC` and `TRANS.`

FUNC

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112436.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Alias | Pin

TRANS

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112436.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：Alias | Pin

The following examples are the operations of these sets.

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DFPR  DFPR  -  DeFine Pin Role）

```
DFPR? DEF,(@)
```

returns

```
DFPR "FUNC","CLK",(CP)
DFPR "TRANS","Read",(S0)
DFPR "TRANS","Write",(S1)
```

This example returns the names of all defined alias sets together with their defined pin aliases. This query will not return the pins without aliases.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DFPR  DFPR  -  DeFine Pin Role）

```
DFPR? ALL,(FUNC,TRANS)
```

returns

```
DFPR "FUNC","CLK",(CP)
DFPR "FUNC", "S0",(S0)
DFPR "FUNC", "S1",(S1)
DFPR "TRANS","CP",(CP)
DFPR "TRANS","Read",(S0)
DFPR "TRANS","Write",(S1)
```

This example returns the pin aliases for all pins in the alias sets `FUNC` and `TRANS`. For the pins without aliases, the package pin names are returned.

### Example 3（取自子主题 Commands in alphabetical order › List of commands › DFPR  DFPR  -  DeFine Pin Role）

```
DFPR? DEF,(TRANS)
```

returns

```
DFPR "TRANS","Read",(S0)
DFPR "TRANS","Write",(S1)
```

This example returns the defined pin aliases in the alias set `TRANS`. This query will not return the pins without aliases.

### Example 4（取自子主题 Commands in alphabetical order › List of commands › DFPR  DFPR  -  DeFine Pin Role）

```
DFPR? DEF,(FUNC::CLK)
```

returns

```
DFPR "FUNC","CLK",(CP)
```

This example returns the package pin name `CP` which is related to the pin alias `CLK` in the alias set `FUNC`.

### Example 5（取自子主题 Commands in alphabetical order › List of commands › DFPR  DFPR  -  DeFine Pin Role）

```
DFPR "TRANS","CLK",(CP)
```

This example adds the package pin `CP` and its alias `CLK` to the alias set `TRANS`. Now the alias set `TRANS` is as the following.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112436.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：Alias | Pin

### DFPS（取自子主题 Commands in alphabetical order › List of commands › DFPS  DFPS  -  DeFine Power Supply）

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

### DFPS?（取自子主题 Commands in alphabetical order › List of commands › DFPS  DFPS  -  DeFine Power Supply）

```
DFPS? {(pinlist)}
```

returns:

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFPS  DFPS  -  DeFine Power Supply）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98551.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：dps_channel | The test system channel number of the DPS channel to be configured. The channel is to be defined as follows: For external device power supplies, t…

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DFPS  DFPS  -  DeFine Power Supply）

```
DFPS 11,POS,(Vee)
```

This example connects device pin Vee to channel 1 of DPS board 1. The DPS output polarity is positive.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DFPS  DFPS  -  DeFine Power Supply）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98551.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 1 列。
> 首行（上游原文）：DFPS (10101, 10102),POS,(vee)

Both lines define the same master/slave configuration for DC Scale channels in DPS mode. They just use different notations. Note the five digit channel numbers.

### Example 3（取自子主题 Commands in alphabetical order › List of commands › DFPS  DFPS  -  DeFine Power Supply）

```
DDIC CONN, (104GO, 105GI)
DFPS (10403, 10404, 10501, 10502),POS,(vee)
```

This example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across two boards.

### Example 4（取自子主题 Commands in alphabetical order › List of commands › DFPS  DFPS  -  DeFine Power Supply）

```
DDIC CONN, (104GO, 105GI, 105GO, 106GI)
DFPS (10403, 10404, 10502, 10503, 10504, 10601),POS,(vee)
```

This example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across three boards.

### Example 5（取自子主题 Commands in alphabetical order › List of commands › DFPS  DFPS  -  DeFine Power Supply）

```
DDIC CONN,(230GO, 227GI)
DFPS (23004, 22701),POS,(VDDCI)
```

This example specifies the ganging of channels across two DC Scale UHC4 cards.

### DFPT?（取自子主题 Commands in alphabetical order › List of commands › DFPT  DFPT  -  DeFine PorT）

```
DFPT? {(portlist)}
```

returns:

```
DFPT {(pinlist)}, {(port)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFPT  DFPT  -  DeFine PorT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98552.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：pinlist | Pin name or names. If more than one pin is required, the names must be separated with a comma. The @ character can be used to refer to all configured …

### Example（取自子主题 Commands in alphabetical order › List of commands › DFPT  DFPT  -  DeFine PorT）

```
DFPT? (port_1, port_2)
```

returns:

```
DFPT (CP_1,DS7_1,DS0_1,I/O7_1,...,I/O0_1,Q7_1,
Q0_1,S1_1,S0_1,_MR_1),(port_1)
DFPT (CP_2,DS7_2,DS0_2,I/O7_2,...,I/O0_2,Q7_2,
Q0_2,S1_2,S0_2,_MR_2),(port_2)
```

### DFSP（取自子主题 Commands in alphabetical order › List of commands › DFSP  DFSP  -  DeFine Sampling Profile）

```
DFSP [meas_resource,] {measure_type}, {measure_range}, {sampling_rate}, [average_factor], [keep_range,] {(pinlist)}
```

### DFSP?（取自子主题 Commands in alphabetical order › List of commands › DFSP  DFSP  -  DeFine Sampling Profile）

```
DFSP? {(pinlist)}
```

returns

```
DFSP [meas_resource,] {measure_type}, {measure_range},{sampling_rate}, [average_factor], [keep_range,] {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFSP  DFSP  -  DeFine Sampling Profile）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124994.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：meas_resource | The measurement resource. It can be: PMU - The default value

### Example 1: Current measurements（取自子主题 Commands in alphabetical order › List of commands › DFSP  DFSP  -  DeFine Sampling Profile）

```
DFSP CURR,0.5,2048,2,(@)
```

or

```
DFSP CURR,40,2048,,KEEP,(dps1)
```

### Example 2: Voltage measurements（取自子主题 Commands in alphabetical order › List of commands › DFSP  DFSP  -  DeFine Sampling Profile）

```
DFSP VOLT,2,50,8,(dps1)
```

or

```
DFSP VOLT,2,50,,(@)
```

### DFTD（取自子主题 Commands in alphabetical order › List of commands › DFTD  DFTD   DeFine Test Data）

```
DFTD {"`testdata_name`（raw: `02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md#_100076__r_testdata_name`）"}, {`edit_mode`（raw: `02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md#_100076__r_edit_mode`）}, {(`pinlist`（raw: `02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md#_100076__r_pinlist`）)}, {`#spec(data)`（raw: `02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.md#_100076__r_spec`）}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFTD  DFTD   DeFine Test Data）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 5 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 7 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment



> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 3 列。
> 首行（上游原文）：ALL | Returns all test data collections (only in the query).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：REPLACE | Replaces all existing td elements with the new definitions.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：ALL | returns all elements of all categories.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：66 行 × 63 列，含嵌套表。
> 首行（上游原文）：testdata_name | A mandatory name that identifies a collection of test data elements (td). If the collection contains DC sets, the name is freely definable. Note…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 6 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 8 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 9 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 10 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 11 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 12 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 13 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 14 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 15 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 16 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100076.htm`
> 中**第 17 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 4 列。
> 首行（上游原文）：Attribute | Type | Value | Comment

Comma separated list of values for the waveform in Volt or Ampere.

Note that number of list items must have the same value on all pins of the specified pattern for which DC waveforms are defined.

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DFTD  DFTD   DeFine Test Data）

```
# For pin vdd, define dc test data:
DFTD "DCTasks",REPLACE,(vdd),#3237<?xml version="1.0"?>
<testdata>
 <td id="0" type="dcset">
 <setMeasureRange type="voltage" minValue="0" maxValue="3"/>
 </td>
 <td id="1" type="dcset">
 <measure type="current" failOnLowClamp="true" failOnHighClamp="true"/>
 </td>
</testdata>
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DFTD  DFTD   DeFine Test Data）

```
DFTD "DCTasks",REPLACE,(vdd),#3233<?xml version="1.0"?>
<testdata>
 <td id="maxVoltage" type="dcset">
 <setForceValue type="voltage" value="LEV:maxVoltage"/>
 </td>
 <td id="derivedVoltage" type="dcset">
 <setForceValue type="voltage" value="LEV:derivedVoltage"/>
</td>
</testdata>
```

This example shows how base and derived variables can be referenced within a test event. A test in which this setForceValue element is executed must be run with a primary level equation set where these variables are declared, for example:

```
EQNSET 1 "level1"
 SPECS
 maxVoltage [V]
 EQUATIONS
 derivedVoltage = maxVoltage/2
 ...
```

### Example 3（取自子主题 Commands in alphabetical order › List of commands › DFTD  DFTD   DeFine Test Data）

The following example shows a test data collection of DC waveforms, and how an element of this collection is referenced in a SVEC pattern:

```
DFTD "dcSubLabel",INSERT,(pmuPort),#9000000352<?xml version="1.0"?>
<testdata>
<td id="force1V" type="dcWaveform">
<setForceWaveform type="voltage" vectorDistance = "16" iRange="0.01" values="0,0.5,1"/>
</td>
<td id="force0V" type="dcWaveform">
<setForceWaveform type="voltage" vectorDistance = "16" iRange="0.01"
values="1,0.75,0.5,0.25,0"/>
</td>
</testdata>

SQLB "dcSubLabel",SVEC,0,2,"functional_MP",(pmuPort)
...
SQPG 0,STVA,,0,SM,(pmuPort)
SQPG 1,XACT,,"force1V",SM,(pmuPort) # execute ramp to force 1V
SQPG 2,RSUB,,,,(pmuPort)
```

The subpattern named `dcSubLabel` executes the first of the two DC waveforms that are contained in the test data collection of the same name.

### DFUP（取自子主题 Commands in alphabetical order › List of commands › DFUP  DFUP  -  DeFine Utility Purpose）

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### DFUP?（取自子主题 Commands in alphabetical order › List of commands › DFUP  DFUP  -  DeFine Utility Purpose）

```
DFUP? {(purpose_name)}
```

returns

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFUP  DFUP  -  DeFine Utility Purpose）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98559.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ch_No_list | Utility line channel numbers to be defined as the members of a utility purpose and specified with five digits. The channels must be separated with …

### Example（取自子主题 Commands in alphabetical order › List of commands › DFUP  DFUP  -  DeFine Utility Purpose）

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

This example defines a utility purpose AWG_CNCT and activates its standard settings.

The members and the setting values are as follows:

```
Member:      16501  16502  16503  16504
---------------------------------------
Setting:     0      1      1      0
```

### DFUT（取自子主题 Commands in alphabetical order › List of commands › DFUT  DFUT  -  DeFine UTility line）

```
DFUT {ch_No}, {type}, {(util_name)}
```

### DFUT?（取自子主题 Commands in alphabetical order › List of commands › DFUT  DFUT  -  DeFine UTility line）

```
DFUT? {(util_name)}
```

returns

```
DFUT {ch_No}, {type}, {(util_name)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DFUT  DFUT  -  DeFine UTility line）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98560.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ch_No | Channel number of the utility line specified with five or three digits. In the five‑digit format, the first three digits specify the utility pogo block.…

### Example（取自子主题 Commands in alphabetical order › List of commands › DFUT  DFUT  -  DeFine UTility line）

```
DFUT 16504,w,(filter)
```

This example assigns the name `filter` and operating mode w to utility line 4 of the first utility pogo block.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DGCM  -  DiGital Capture Mode）

```
DGCM? {"vector_label"}
```

returns:

```
DGCM {"vector_label"},{capt_mode}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DGCM  -  DiGital Capture Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99055.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：vector_label | Vector main label. Must be enclosed in double quotes

### Example（取自子主题 Commands in alphabetical order › List of commands › DGCM  -  DiGital Capture Mode）

```
> DGCM? "my_vec_lab"
< DGCM "my_vec_lab", SEQ
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DGCS  DGCC   DiGital Capture aSynchronous）

```
DGCS
SQST RUN
DGCC?
```

returns:

```
DGCC {result_flag}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/136579.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：result_flag | The result returned by DGCC?. P (for Pass) is returned if received and expected data match. F (for Fail) is returned if received and expected data…
> 表内引用（1 条，供检索）：`Combining selective digital capture with a functional test`（raw: `02.06.06.01.03.01.03_Combining_selective_digital_capture_with_a_functional_test.md`）

### Examples（取自子主题 Commands in alphabetical order › List of commands › DGCS  DGCC   DiGital Capture aSynchronous）

### Generic example

```
> DGCS
> SQST RUN
> DGCC?
< DGCC F
```

### Application

This command performs hardware activation and clean-up on pins configured for digital capture.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DGCT  -  DiGital Capture Test）

```
DGCT? ["exec_context"]
```

returns:

```
DGCT {result_flag}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DGCT  -  DiGital Capture Test）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99056.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts .
> 表内引用（1 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › DGCT  -  DiGital Capture Test）

```
> DGCT?
< DGCT F
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DIAG -  DIAGnostics）

```
DIAG {option}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DIAG -  DIAGnostics）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98562.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：option | Specifies the desired option:

### Example（取自子主题 Commands in alphabetical order › List of commands › DIAG -  DIAGnostics）

```
DIAG 44
```

This example stops to display the error and warning messages to the report window.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DIDT  DIDT  -  upload DIgital DaTa）

```
DIDT {"var_name"}, [code_format], [code_input_mode], [byte_order], [code_width], [offset], [nr_vectors], [comment], {data}
DIDT? {"var_name"}, ["area-id",][code_format], [code_input_mode], [byte_order], [code_width], [offset], [nr_vectors]
```

returns:

```
DIDT {"var_name"}, [code_format], [code_input_mode], [byte_order], [code_width], [offset], [nr_vectors], [comment], {data}
```

To return only parameters and comments:

```
DIDT?ALL,,,,,0,0
```

Returns all vector variable parameters.

```
DIDT? "var_name",,,,,0,0
```

Returns only the parameters of the specific vector variable var_name:

```
DIDT {"var_name"}, [code_format], [code_input_mode], [byte_order], [code_width], [offset], [nr_vectors], ["comment"], #9000000000
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99057.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：var_name | This is a unique name string for the vector variable that defines the filtering conditions.
> 表内引用（3 条，供检索）：`Code Format Tables`（raw: `../02.07_Test_Method_Reference/02.07.04.04_Code_Format_Tables.md`） · `inputMode()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.269_VECTOR.md#_29830__dle_inputMode`） · `getInputMode()`（raw: `../02.07_Test_Method_Reference/02.07.04.01.269_VECTOR.md#_29830__dle_getInputMode`）

### Example 1 - Digital capture（取自子主题 Commands in alphabetical order › List of commands › DIDT  DIDT  -  upload DIgital DaTa）

```
> DVVA? ALL
< DVVA "par_var",DIGCAPT,"MYTEST",PARA,,,,0,3,1,1,2,2,(PAR3,PAR2,PAR1)
> DIDT? "par_var",,,,,,
< DIDT "par_var",BIN,NORM,BIG_ENDIAN,3,0,6,,#9000000024,,,,,,
```

or, alternatively:

```
> $DIDT? "par_var",,,,,,2
< DIDT "par_var",BIN,NORM,BIG_ENDIAN,3,0,2,,
       0000  0000  0000 0000  0000 0000  0000  0110
       0000  0000  0000 0000  0000 0000  0000  0101
```

In the preceding call of $DIDT? it was assumed that the output format of the DUT is BIN. Accordingly, no conversion was performed. If the output format is GRAY, call and reply will look like this:

```
> $DIDT? "par_var",GRAY,,,,,2
< DIDT "par_var",GRAY,NORM,BIG_ENDIAN,3,0,2,,
       0000 0000 0000 0000 0000 0000 0000 0100
       0000 0000 0000 0000 0000 0000 0000 0110
```

### Example 2 - Digital Source Memory（取自子主题 Commands in alphabetical order › List of commands › DIDT  DIDT  -  upload DIgital DaTa）

```
> DIDT? ALL,,,,,0,0
```

returns:

```
DIDT "LEFT",BCD,NORM,BIG_ENDIAN,16,0,10,"download comment LEFT",#9000000000
DIDT "L1",BIN,NORM,BIG_ENDIAN,32,0,0,"download sin wave",#9000000000
DIDT "L11",BIN,NORM,BIG_ENDIAN,32,0,0,"", #9000000000
DIDT "L2",BIN,NORM,BIG_ENDIAN,32,0,0,"",#9000000000
DIDT "LF",BIN,NORM,BIG_ENDIAN,16,0,20,"download comment Flat",#9000000000
```

Note To query the comments or download parameters of DIDT, you must specify that offset and nr_vectors be 0. Omitting nr_vectors means that you upload the number of frames defined in the vector variable configuration usage, using all the other default download parameters.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DLPP -  DeLete Per Pin Subroutine）

```
DLPP {label}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DLPP -  DeLete Per Pin Subroutine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98563.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：label | Specifies the name of the per-pin subroutine to be deleted.

### Example（取自子主题 Commands in alphabetical order › List of commands › DLPP -  DeLete Per Pin Subroutine）

```
DLPP "summer"
```

This command deletes the per-pin subroutine referenced by the label "summer".

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DLSO  Driver Level Switch Off）

```
DLSO{(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DLSO  Driver Level Switch Off）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98564.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pinlist | Pin or pins for which the channels are to be set to high impedance as defined by level set 0. You can specify @ for all pins, and @NONSHARED@ for the …

### Example（取自子主题 Commands in alphabetical order › List of commands › DLSO  Driver Level Switch Off）

DLSO can be used in a customized disconnect sequence (disconnect.user_def in the testfunc directory) as follows:

```
DLSO(@)
RLYC IDLE,OFF,(@)
...
PSST OFF
```

Executing this file instead of the standard disconnect sequence has the advantage that only the sequencers of the sites that are in setup focus are switched off. DLSO also ensures that this is done without hot switching. The standard sequence uses the SQST OFF command, which switches all sequencers off, not only those in setup focus.

 Note The goal is to ensure that the AC relay is not open while there is current flowing through it nor close the AC relay when there is a difference in potential across the two AC relay terminals. That is, we want to minimize the di/dt when we open or close the AC relay or PPMU relay. The clamps only help to limit the voltage excursion transient from L*di/dt. So it's best if di/dt is zero or near zero so clamps are not needed. This is the theory behind how to eliminate hot switching damage to both the DUT as well as the tester's pin electronics. We need the device connect and disconnect sequences to minimize di/dt during the switching of any relay or FET between the tester pin electronics and the DUT due to the long inductive cable between the pin electronics and DUT. This applies to all cards.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DLTS -  DeLete TeSt）

```
DLTS {"label"}[, (port)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DLTS -  DeLete TeSt）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98565.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：label | Specifies the label to be deleted.

### Example（取自子主题 Commands in alphabetical order › List of commands › DLTS -  DeLete TeSt）

```
DLTS "MPBU_port_1_port_2",(port_1)
```

This example deletes the label referenced by `MPBU_port_1_port_2` from the port `port_1`.

### DMAS（取自子主题 Commands in alphabetical order › List of commands › DMAS  DMAS  -  Define Memory Area Size）

```
DMAS SQPG, [memory], {size}, {(port)}
```

### DMAS?（取自子主题 Commands in alphabetical order › List of commands › DMAS  DMAS  -  Define Memory Area Size）

Area type PARA:

```
DMAS? PARA, [memory], PER_PORT, {(port_list)}
```

returns:

```
DMAS PARA, {memory}, {size}, {(port)}
```

Area type SQPG:

```
DMAS? SQPG, [SM], [PER_PORT,] {(port_list)}
```

returns:

```
DMAS SQPG, SM, {size}, {(port)}
```

Area type PPSQ:

```
DMAS? PPSQ, [SM], [PER_PORT,] {(@)}
```

returns:

```
DMAS PPSQ, SM, {size}, {(@)}
```

Area type RSLT, querying ports:

```
DMAS? RSLT, [SM], [PER_PORT,] {(port_list)}
```

returns:

```
DMAS RSLT, SM, {size}, {port}
```

Area type RSLT, querying pins:

```
DMAS? RSLT, [SM], {PER_PIN}, {(pin_list)}
```

returns:

```
DMAS RSLT, SM, {size}, {pin}
```

Area type SAVE:

```
DMAS? SAVE, ALL, [PER_PORT,] {(port_list)}
```

returns:

```
DMAS SAVE, {memory}, {size}, {(port)}
```

Area type ALL:

```
DMAS? ALL, [memory], [PER_PORT,] {(port_list)}
```

returns:

```
DMAS {area}, {memory}, {size}, {(port)}
```

Area type MFRE, querying ports:

```
DMAS? MFRE, [SM|SMEXT], [PER_PORT,] {(port_list)}
```

returns:

```
DMAS MFRE, {SM|SMEXT}, {size}, {port}
```

Area type MFRE, querying pins:

```
DMAS? MFRE, [SM|SMEXT], {PER_PIN}, {(pin_list)}
```

returns:

```
DMAS MFRE, {SM|SMEXT}, {size}, {pin}
```

Area type MFRE, querying channels:

```
DMAS? MFRE, [SM|SMEXT], {PER_CHANNEL}, {(channel_list)}
```

returns:

```
DMAS MFRE, {SM|SMEXT}, {size_1}, {size_2}, {size_3}, {(channel)}
```

Area type MFRP, querying channels:

```
DMAS? MFRP, [SM|SMEXT], {PER_CHANNEL}, {(port_list)}
```

returns:

```
DMAS MFRP, {SM|SMEXT}, {size_1}, {size_2}, {size_3}, {(channel)}
```

Area type MFRP, querying pools:

```
DMAS? MFRP, [SM|SMEXT], {PER_POOL}, {(port_list)}
```

returns:

```
DMAS MFRP, {SM|SMEXT}, {pool_size}, {(pool_channels)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DMAS  DMAS  -  Define Memory Area Size）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98566.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：29 行 × 3 列。
> 首行（上游原文）：area | The area parameter specifies the type of data for which a memory area is to be set or read. It can be one of the following:
> 表内引用（3 条，供检索）：`Selecting the memory type`（raw: `02.06.07.01.04.01_Selecting_the_memory_type.md`） · `Defining a compliance pattern for pattern‑based SmartLoop testing`（raw: `02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md`） · `Technology file for a device - himem`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md#_49363__row_himem`）

### Example（取自子主题 Commands in alphabetical order › List of commands › DMAS  DMAS  -  Define Memory Area Size）

The following example illustrates the various options of the MFRE and MFRP queries. First, the free memory range of the `port12` port is queried on the port level:

```
> DMAS? MFRE,,(port12)
< DMAS MFRE,SM,84288,(port12)
```

On the pin level, the corresponding query and reply look as follows:

```
> DMAS? MFRE,,PER_PIN,(port12)
< DMAS MFRE,SM,84288,(Pin1)
< DMAS MFRE,SM,88288,(Pin2)
```

Note that the query per port returns the smaller of the two values.

`Pin1` is mapped to channel 10101, `Pin2` to channel 10102. Thus the corresponding channel related query and its reply are

```
> DMAS? MFRE,,PER_CHANNEL,(10101,10102)
< DMAS MFRE,SM,84212,84312,84640,(10101)
< DMAS MFRE,SM,88312,88312,88640,(10102)
```

The figures are slightly different, because the query per channel only considers the hardware.

Finally, the two possible options for MFRP, applied to `port12`, produce

```
> DMAS? MFRP,,PER_CHANNEL,(port12)
< DMAS MFRP,SM,84212,84312,84640,(10101)
< DMAS MFRP,SM,88312,88312,88640,(10102)
< DMAS MFRP,SM,84212,84312,84640,(10103)
< DMAS MFRP,SM,90464,90464,90736,(10104)
```

 for the PS9G pool 10101 through 10104, and

```
> DMAS? MFRP,,PER_POOL,(port12)
< DMAS MFRP,SM,347400,(10101,10102,10103,10104)
```

### DPPC（取自子主题 Commands in alphabetical order › List of commands › DPPC -  Define Per Pin subroutine Configuration）

```
DPPC {name}, {parameter}, [value], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DPPC -  Define Per Pin subroutine Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98567.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：name | Name of the Pin-Per Sequencer Subroutine label. For the query, you can enter ALL to return all PPSS labels.

### DPPS（取自子主题 Commands in alphabetical order › List of commands › DPPS  DPPS  -  Define Per Pin Subroutine label）

```
DPPS {name}, {cycle_len}
```

### DPPS?（取自子主题 Commands in alphabetical order › List of commands › DPPS  DPPS  -  Define Per Pin Subroutine label）

```
DPPS? {name}
```

returns:

```
DPPS {name}, {cycle_len}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DPPS  DPPS  -  Define Per Pin Subroutine label）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98568.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：name | Per-pin Subroutine name. This parameter can be used to call the subroutine from a parallel sequencer program. For the query, you can also enter ALL to re…

### DPRL（取自子主题 Commands in alphabetical order › List of commands › DPRL  DPRL  -  Default PRimary Level sets）

```
DPRL {level_set}, {dps_set}, [screen_select]
```

### DPRL?（取自子主题 Commands in alphabetical order › List of commands › DPRL  DPRL  -  Default PRimary Level sets）

```
DPRL?
```

returns:

```
DPRL {level_set}, {dps_set}, [screen_select]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DPRL  DPRL  -  Default PRimary Level sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98569.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：level_set | Level Set number.

### Example（取自子主题 Commands in alphabetical order › List of commands › DPRL  DPRL  -  Default PRimary Level sets）

```
DPRL?
```

returns:

```
DPRL 1,2,LEV
```

On sending a query, the system reports that the default primary level set is 1 and the default primary DPS set is 2.

### DPRT（取自子主题 Commands in alphabetical order › List of commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT {"multi-port_spec"}, [timing_set_no|"timing_set_list"][,(port)]
```

### DPRT?（取自子主题 Commands in alphabetical order › List of commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT?
```

returns:

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT?
```

returns:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT? [(port)]
```

returns:

```
DPRT {"multi-port_spec"}, {timing_set_no|"timing_set_list"}[,(port)]

```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DPRT  DPRT  -  Default PRimary Timing sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98570.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number.
> 表内引用（1 条，供检索）：`TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT?
```

returns:

```
DPRT 3,4
```

On sending a query the system reports that the default primary waveform set is 3 and the default primary timing set is 4.

### DPSA（取自子主题 Commands in alphabetical order › List of commands › DPSA  DPSA  -  Define per Pin Subroutine Address）

```
DPSA {name}, {address}, {(pinlist)}
```

### DPSA?（取自子主题 Commands in alphabetical order › List of commands › DPSA  DPSA  -  Define per Pin Subroutine Address）

```
DPSA? {name}, {(pinlist)}
```

returns:

```
DPSA {name}, {address}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DPSA  DPSA  -  Define per Pin Subroutine Address）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98571.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：name | Per-pin Subroutine name. This parameter can be used to call the subroutine from a parallel sequencer program. For the query, you can also enter ALL to re…

### DPSE（取自子主题 Commands in alphabetical order › List of commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DPSE {setnr}, {(pinlist)}, {binary_data}
```

### DPSE?（取自子主题 Commands in alphabetical order › List of commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DPSE? {setnr}
```

returns:

```
DPSE {setnr}, {(pinlist)}, {binary_data}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98572.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 4 列，含嵌套表。
> 首行（上游原文）：setnr | This number defines the set number for the measurement. The number must be an integer from 1 to 256. In the query, you can specify ALL to retrieve the d…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98572.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：24 行 × 2 列。
> 首行（上游原文）：0: Waveform template

If the first value is an '11', two values follow. They define the low/high P/F limits of a return (voltage-)drop measurement and are separated by a "," (comma). The values are given in the unit Volt [V]. The number of measurement points is 1.

This option can be selected only for the HC variant of `DC Scale DPS128`（raw: `../02.05_Test_Head_Cards/02.05.05.01_DC_Scale_DPS128_DPS64_cards.md`） channels and requires that the measurement is executed with the `PSIE`（raw: `02.06.02.02.192_PSIE_-__Power_Supply_Internal_trigger_Execute.md`） command.

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DPSE 1,(Vcc),#90000000170,0.1,0.2,0.2,0.3
```

This example defines a template which consists of 2 points (0.1, 0.2) and (0.2, 0.3). If the first measured value is in the range (0.1, 0.2) and the second value is in the range (0.2, 0.3), then the result will be a pass.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DPSE 1,(Vcc),#90000000121,15,0.1,0.2
```

This example defines a template which is 15 points long and is constant.

### Example 3（取自子主题 Commands in alphabetical order › List of commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DFPS 11,pos,(Vcc)
DFPS 12,pos,(Vdd)
DPSE 1,(@),#10 <- Delete set 1
DPSE 1,(Vcc),#152,1,2 <- Vcc min=1A, max=2A
DPSE 1,(Vdd),#152,2,3 <- Vdd min=2A, max=3A
PSST ON <- Measurement requires connect state
PSIE 1,,,(@) <- Measure both pins in parallel
PSER? 1,pval
PSER 1,P,(Vcc),#9000000006,1.501 <- value within range
PSER 1,F,(Vdd),#9000000006,3.173 <- value outside range
PSER? 1,ppf
PSER 1,P,(Vcc),#9000000000
PSER 1,F,(Vdd),#9000000000
PSER? 1,gpf
PSER 1,F,(),#9000000000
```

This example performs a measurement with format 2 and PSIE for two different pins in parallel.

### Example 4（取自子主题 Commands in alphabetical order › List of commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DFPS (10101),pos,(Vcc) <- DC Scale pin
DFPS (10102,10103),pos,(Vdd) <- DC Scale pin (Gang of two channels)
DPSE 1,(@),#10 <- Delete set 1
DPSE 1,(Vcc),#153,0.5,1.5 <- Vcc min=0.5A, max=1.5A
DPSE 1,(Vdd),#153,20,30 <- Vdd min=20A, max=30A
PSST ON <- Measurement requires connect state
PSIE 1,,,(@) <- Measure both pins in parallel
 Vcc: High Precision Mode is used
 Vdd: Only one channel of the gang is used
PSER? 1,pval
PSER 1,P,(Vcc),#9000000006,1.301 <- value within range
PSER 1,F,(Vdd),#9000000006,31.73 <- value outside range
PSER? 1,ppf
PSER 1,P,(Vcc),#9000000000
PSER 1,F,(Vdd),#9000000000
PSER? 1,gpf
PSER 1,F,(),#9000000000
```

This example performs a measurement with format 3 and PSIE for two different pins in parallel.

### DPSR（取自子主题 Commands in alphabetical order › List of commands › DPSR  DPSR  -  Define Parallel SeaRch）

```
DPSR {set_nr}, ["exec_context",] [(setup_pinlist)|(primary_port)], [(result_pinlist)], [wait_time,] [search_type], [max_err_count,] {#spec(data)}
```

### DPSR?（取自子主题 Commands in alphabetical order › List of commands › DPSR  DPSR  -  Define Parallel SeaRch）

```
DPSR? {set_nr} [, (setup_pinlist)]
```

returns:

```
DPSR {set_nr}, ["exec_context",] (setup_pinlist), (result_pinlist), [wait_time,] search_type, [max_err_count], {#spec(data)}
```

Extra parameters exec_context and wait_time are returned only if they have been defined by DPSR.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98574.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：25 行 × 4 列。
> 首行（上游原文）：set_nr | The mandatory parameter specifies the number of the search set in which the condition is to be stored. The maximum number is 128. If a search set with …

### Example（取自子主题 Commands in alphabetical order › List of commands › DPSR  DPSR  -  Define Parallel SeaRch）

```
> PSFC ALL
> DPSR 3,,,FUNC,#219,TIM,"f",B,30,130,,
> PSFC 2
> DPSR 3,(IN1),,FUNC,#220,TIM,"del",B,0,110,,
> PQFC 1
> DPSR? 3,(@)
< DPSR 3,(@),(@),FUNC,#9000000019,TIM,"f",B,30,130,,
> PQFC 2
> DPSR? 3,(@)
< DPSR 3,(OUT1),(@),FUNC,#9000000019,TIM,"f",B,30,130,,
< DPSR 3,(IN1),(@),FUNC,#9000000020,TIM,"del",B,0,110,,
```

This example illustrates:

- How the same search can be defined differently for different sites.
- How an existing condition is partially overwritten when a new condition is partially inconsistent with it.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DQUE  -  show Data QUEue low level）

```
DQUE?{(pinlist)}
```

returns:

```
DQUE {dqueue_level}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DQUE  -  show Data QUEue low level）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98575.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：dqueue_level | A reply parameter specifying the smallest number of 8-vector blocks that was left in the data queue during the last sequencer run for the specifi…

### Example（取自子主题 Commands in alphabetical order › List of commands › DQUE  -  show Data QUEue low level）

```
> DQUE? (p1)
< DQUE 26,(p1)
```

This example queries the low level of the data queue for pin p1.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › DRLS  -  DRive Level Sensitivity）

```
DRLS? {test}, {pass_value}, [limit], {(pinlist)}
```

returns:

```
DRLS {value_specifier}, {result_value}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DRLS  -  DRive Level Sensitivity）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98576.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 3 列。
> 首行（上游原文）：test | This parameter is one of the following:
> 表内引用（2 条，供检索）：`DRLV, DRLV? - (DRive LeVel)`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`） · `DRLV, DRLV? - (DRive LeVel`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DRLS  -  DRive Level Sensitivity）

```
DRLS? H,5000,,(Q0_1)
```

returns:

```
DRLS P,5000
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DRLS  -  DRive Level Sensitivity）

```
DRLS? H,5000,-1000,(Q0_1)
```

returns:

```
DRLS EQ,-490
```

### DRLV（取自子主题 Commands in alphabetical order › List of commands › DRLV  DRLV  -  DRive LeVel）

```
DRLV {level_set_no | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### DRLV?（取自子主题 Commands in alphabetical order › List of commands › DRLV  DRLV  -  DRive LeVel）

```
DRLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
DRLV {level_set | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DRLV  DRLV  -  DRive LeVel）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98577.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：level_set_no | The identification number of the level set (fixed levels) in which you want the levels to be included. The number must not exceed the maximum num…
> 表内引用（2 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

For card specifications, like level ranges, see `Digital Cards`（raw: `../02.02_Specifications/02.02.04_Digital_Cards.md`）, for example:

- `Pin Scale 1600`（raw: `../02.02_Specifications/02.02.04.01.03_PS1600_driver.md`）
- `Pins Scale 5000`（raw: `../02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › DRLV  DRLV  -  DRive LeVel）

```
DRLV 1,-1750,-850,(Q0,Q1,Q2,Q3)
```

This example sets the driver levels for level set 1 for pins Q0, Q1, Q2 and Q3. The logic 0 level is set to -1750 mV and the logic 1 level to -850 mV.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › DRLV  DRLV  -  DRive LeVel）

```
DRLV 1,-1750,-850,8000,(avi64Pin1)
```

This example shows how the 8 V drive range of an AVI64 pin is selected.

### DSCP（取自子主题 Commands in alphabetical order › List of commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP `[device_cycle`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_device_cycle`）], `[waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）], `[timing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_timing_set`）], `[level_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_level_set`）], `[dps_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_dps_set`）], `[pmu_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_pmu_set`）],
                        `[devicecycle_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_devicecycle_set`）], `[routing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_routing_set`）], `[period_res_prec`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_period_res_prec`）],

```

### DSCP?（取自子主题 Commands in alphabetical order › List of commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP?
```

returns:

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
       {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
       [period_res_compatibility_model]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DSCP  DSCP  -  Define System Control Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98578.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：device_cycle | The device_cycle parameter is an integer that defines the absolute maximum number of device cycles that you can create for one pin.Default: 256Ma…
> 表内引用（2 条，供检索）：`waveform sets and wavetables`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） · `waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）

### Example（取自子主题 Commands in alphabetical order › List of commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

### DSUS（取自子主题 Commands in alphabetical order › List of commands › DSUS  DSUS  -  Dps Sets USed）

```
DSUS {ds_No}
```

### DSUS?（取自子主题 Commands in alphabetical order › List of commands › DSUS  DSUS  -  Dps Sets USed）

```
DSUS?
```

returns:

```
DSUS {ds_No}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DSUS  DSUS  -  Dps Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98580.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：ds_No | DPS Set Number. This is the highest number currently allocated to a DPS set, or the highest number of set you want to load. The number you type must not…

### Example（取自子主题 Commands in alphabetical order › List of commands › DSUS  DSUS  -  Dps Sets USed）

```
DSUS 2
```

This example defines a maximum of 2 DPS sets.

### DSVS（取自子主题 Commands in alphabetical order › List of commands › DSVS  DSVS  -  Define Spec Value Set）

```
DSVS {spec_value_set_id}, ["description"], {"spec_type"}, [equ_set_no|PRM], [spec_set_no|"multi-port_spec"]
DSVS {spec_value_set_id},,,,
```

### DSVS?（取自子主题 Commands in alphabetical order › List of commands › DSVS  DSVS  -  Define Spec Value Set）

```
DSVS? {spec_value_set_no|ALL}
```

returns:

```
DSVS {spec_value_set_id}, ["description"], {"spec_type"}, [equ_set_no|PRM], [spec_set_no|"multi-port_spec"]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DSVS  DSVS  -  Define Spec Value Set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118966.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：spec_value_set_id | This must be an integer between 1 and 216-1.

### Example（取自子主题 Commands in alphabetical order › List of commands › DSVS  DSVS  -  Define Spec Value Set）

```
> DSVS 1, "per", TIM,PRM,
> DSVS? 1
< DSVS 1,"per",TIM,1,1
> DSVS 1, "per", TIM,1,2
< Error: Failed to execute firmware command: DSVS 1, "per", TIM,1,2
> DSVS 1,,,,
> DSVS 1, "per", TIM,1,2
> DSVS? 1
< DSVS 1,"per",TIM,1,2
```

This example shows how to redefine a spec value set. Note that you must delete the set before you can change the specification.

### DTCP（取自子主题 Commands in alphabetical order › List of commands › DTCP  DTCP  -  Define Technology Control Parameters）

```
DTCP {"key"}, {"value"}
```

### DTCP?（取自子主题 Commands in alphabetical order › List of commands › DTCP  DTCP  -  Define Technology Control Parameters）

```
DTCP? {"key"}
```

returns:

```
DTCP {"key"}, {"value"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DTCP  DTCP  -  Define Technology Control Parameters）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112750.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：key | The string specifies the system control parameter. Currently, the only supported control parameters are testpoints and extended_dram_factor.For more infor…
> 表内引用（3 条，供检索）：`testpoints`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md#_49363__row_testpoints`） · `extended_dram_factor`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md#_49363__row_extended_dram_factor`） · `Technology file for a device`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md`）

### Examples（取自子主题 Commands in alphabetical order › List of commands › DTCP  DTCP  -  Define Technology Control Parameters）

```
> DTCP? "testpoints"
< DTCP "testpoints", "0"
> DTCP "testpoints", "100"
> DTCP? "testpoints"
< DTCP "testpoints", "100"
> *RST
> DTCP? "testpoints"
< DTCP "testpoints", "100"
```

```
> DTCP "extended_dram_factor","90"
> *RST
> DTCP? "extended_dram_factor"
< DTCP "extended_dram_factor","90"
```

### DVVA（取自子主题 Commands in alphabetical order › List of commands › DVVA  DVVA  -  Define Vector VAriable）

```
DVVA {"name"}, {type}, {"evector_label"}, {xfer_mode}, [device_cycle], [start_vector_nr], ["capt_label"], [init_discard], {nr_vec_per_frame}, [nr_vec_per_sample], [nr_vector_interdisc], [nr_of_frames], [nr_frame_interdisc], {(pinlist)}
```

### DVVA?（取自子主题 Commands in alphabetical order › List of commands › DVVA  DVVA  -  Define Vector VAriable）

```
DVVA? {"name"|ALL}[, (portlist)]
```

returns:

```
DVVA {"name"}, {type}, {"vector_label"}, {xfer_mode}, [device_cycle], [start_vector_nr], ["capt_label"], [init_discard], {nr_vec_per_frame}, [nr_vec_per_sample], [nr_vector_interdisc], [nr_of_frames], [nr_frame_interdisc], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DVVA  DVVA  -  Define Vector VAriable）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99058.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 2 列。
> 首行（上游原文）：name | Name of the vector variable to be defined. The name must be unique across vector labels. If the identifier ALL is used in the query, all those vector var…

### Example（取自子主题 Commands in alphabetical order › List of commands › DVVA  DVVA  -  Define Vector VAriable）

```
> DVVA "vec_1",DIGCAPT,"port2_A",PARA,,,,0,1,1,0,\ 1,0,(I/O5_2)
> DVVA "vec_2",DIGCAPT,"port2_A",PARA,,,,0,1,1,0,1,0,(I/O7_2,I/O6_2)
> DVVA "vec_3",DIGCAPT,"port1_B",PARA,,,,0,1,1,0,\ 1,0,(Q7_1)
> DVVA? ALL,(port_1)
< DVVA "vec_3",DIGCAPT,"port1_B",PARA,,,,0,1,1,0,1,0,(Q7_1)
> DVVA? ALL,(port_2)
< DVVA "vec_1",DIGCAPT,"port2_A",PARA,,,,0,1,1,0,1,0,(I/O5_2)
< DVVA "vec_2",DIGCAPT,"port2_A",PARA,,,,0,1,1,0,1,0,(I/O7_2,I/O6_2)
```

### DVVC（取自子主题 Commands in alphabetical order › List of commands › DVVC  DVVC  -  Define Vector Variable Configuration）

```
DVVC {name}, {#data}
```

### DVVC?（取自子主题 Commands in alphabetical order › List of commands › DVVC  DVVC  -  Define Vector Variable Configuration）

```
DVVC? {name},
```

returns:

```
DVVC {name}, {#data}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › DVVC  DVVC  -  Define Vector Variable Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99059.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：name | The configuration name. This can also be ALL.

### DVCU（取自子主题 Commands in alphabetical order › List of commands › DVCU  DVCU  -  Define Vector variable Configuration Usage）

```
DVCU {label_name}, {VVC_name}, {vector_offset},
{init_discard_frames}, {number_of_frames}, {var_name_def}, {init_static_data}
```

### DVCU?（取自子主题 Commands in alphabetical order › List of commands › DVCU  DVCU  -  Define Vector variable Configuration Usage）

```
DVCU? {label_name}, {VVC_name}, {vector_offset}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99060.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：label_name | Name of the label for which usage is to be created. In the query, label_name can also be ALL.
> 表内引用（1 条，供检索）：`DVVC, DVVC? - (Define Vector Variable Configuration)`（raw: `02.06.02.02.95_DVVC__DVVC__-__Define_Vector_Variable_Configuration.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › DVCU  DVCU  -  Define Vector variable Configuration Usage）

The following example creates a usage for the label "src_ramp", using VVC "AC97", at offset 0.

VVC "AC97" looks like:

```
ATTR DIGDATA
VARIABLES LEFT,RIGHT
PINS ser_in
 SOURCE_DATA_TEMPLATE LEFT[0-19] ; RIGHT[0-19]
 MAPPING
 0 low
 1 high
```

This usage creates two vector variables, `LEFT_DATA` and `RIGHT_DATA`. It creates 1024 frames.

```
> DVCU "src_ramp","AC97",0,0,1024,"LEFT=LEFT_DATA,RIGHT=RIGHT_DATA",TRUE
> DVCU? ALL,ALL,ALL
< DVCU "src_ramp","AC97",0,0,1024,"LEFT=LEFT_DATA, RIGHT=RIGHT_DATA",TRUE
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EAEX  -  Edge Action EXpected data）

```
EAEX? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
EAEX {start_cycle}, {no_of_cycles}, {timing_set}, [err_type], {(pinlist)}, {#spec(data)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EAEX  -  Edge Action EXpected data）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98581.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. The scanning method and the range of values this paramete…

### Example（取自子主题 Commands in alphabetical order › List of commands › EAEX  -  Edge Action EXpected data）

```
EAEX? 0, 1, (pin1)
```

returns:

```
EAEX 0,1,3,,(pin1),#9000000010\x01\x04\x00\x0B\x01\x0A\x02\x19\x03\x1F\x0A
```

This example returns edge action drive and expected data (in hex notation) for one cycle. To decode the data, convert it into binary notation and use the lists above.

The data in binary format is:

```
0000 0001 0000 0100 0000 0000 0000 1011 0000 0001
0000 1010 0000 0010 0001 1001 0000 0011 0001 1111
```

The device cycle contains 1 waveform with 4 edge actions. The edge actions are RZ on the drive edges 1 and 2 and a window compare to intermediate on the receive edges 3 and 4.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EARD  -  Edge Action Result Data）

```
EARD? {start_cycle}, {no_of_cycles}, {type}, [MUX,] {(pinlist)}
```

returns:

```
EARD {start_cycle}, {no_of_cycles}, {type}, [err_type], {(pinlist)}, [MUX,] {#spec(data)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EARD  -  Edge Action Result Data）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98582.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：28 行 × 4 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. You can enter a value between 0 and 248.

### Example 1（取自子主题 Commands in alphabetical order › List of commands › EARD  -  Edge Action Result Data）

```
> EARD? 2,1,BOTH,(TX1_d0)
< EARD 2,1,BOTH,PF,MUX,(TX1_d0),#9000000052
      \x10\x01\x00\x10
      \x00\x00\x82\x00\x01\x82\x00\x02\x82\x00\x03\x82\x00\x04\x82\x00\x05\x82\x00\x06\x82\x00\x07\x82
 \x00\x08\x82\x00\x09\x82\x00\x0a\x82\x00\x0b\x82\x00\x0c\x82\x00\x0d\x82\x00\x0e\x82\x00\x0f\x82
```

This example shows the results for a Pin Scale pin TX1_d0, which is multiplexed together with one other Pin Scale pin to an HXA pin. Since the MUX flag is set, the combined results of both these pins are returned in the reply.

Byte 0 indicates that TX1_d0 is one of two multiplexed Pin Scale pins, and that it has the logical position 0 in the multiplexing order. Byte 2 and 3 contain the information that the cycle contains 16 edges.

Byte A is the same for all edges and says that the edge is associated with a fixed value (not a data parameter), and that the waveform to which it belongs occupies position 0 in the device cycle. The edges of the two Pin Scale pins are interleaved according to the logical position in the multiplexing order. The edges of TX1_d0, which has position 0, are those with an even edge index (byte B), starting from 0. The edges of the other multiplexed Pin Scale pin (position 1) have an odd index. The actions (byte C) are also the same for all edges, namely an edge compare to 0 where expected = received value (that is, no error).

### Example 2（取自子主题 Commands in alphabetical order › List of commands › EARD  -  Edge Action Result Data）

The EARD? answer will be split if the requested cycle range is greater than the available error map information, as shown below:

 !`Example`（raw: `../../../../raw/11910.png`）

```
> EARD? 0,15000, (pin1)
< EARD 0, 100, BOTH, NOER, (pin1), BinData        (a)
< EARD 100, 9900, BOTH, PF, (pin1), BinData       (b)
< EARD 10000, 5000, 1, NOER, (pin1), BinData      (c)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EARE  -  Edge Action REceived data）

```
EARE? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
EARE? {start_cycle}, {no_of_cycles}, {timing_set}, [err_type],{(pinlist)}, {#spec(data)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EARE  -  Edge Action REceived data）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98583.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. You can enter a value between 0 and 248.
> 表内引用（1 条，供检索）：`VALD? - (VALid Data)`（raw: `02.06.02.02.316_VALD__-__VALid_Data.md`）

If reconstruction is not possible (code 110 on bits 2, 1, 0), there has been more than one edge or window compare within a single test system cycle.

If error bit 7 is set, an error has occurred on at least one of these edge or window compares.

### Example（取自子主题 Commands in alphabetical order › List of commands › EARE  -  Edge Action REceived data）

```
EARE? 0, 1, (pin1)
```

returns:

```
EARE 0,1,3,ERON,(pin1),#9000000010\x01\x04\x00\x0B\x01\x0A\x02\x9A\x03\x9F\x0A
```

This example returns edge action drive and received data (in hex notation) for one cycle. To decode the data, convert it into binary notation and use the lists above.

The data in binary format is:

```
0000 0001 0000 0100 0000 0000 0000 1011 0000 0001
0000 1010 0000 0010 1001 1010 0000 0011 0001 1111
```

The device cycle contains 1 waveform with 4 edge actions. The edge actions are RZ on the drive edges 1 and 2 and a failing window compare (received value: 0) on the receive edges 3 and 4.

The EARE? answer will be split if the requested cycle range is greater than the available error map information, as shown below:

 !`Example`（raw: `../../../../raw/11910.png`）

```
EARE? 0,15000, (pin1)
EARE 0, 100, 1, NOER, (pin1), BinData (a)
EARE 100, 9900, 1, ERON, (pin1), BinData (b)
EARE 10000, 5000, 1, NOER, (pin1), BinData (c)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EDDC  -  EDge in Device Cycle）

```
EDDC? [waveform_set], [timing_set], {edge_spec},
[dev_cyc_name], [dc_ref], [direction], {(pinlist)}
```

returns:

```
EDDC {edge_number}, {dev_cyc_name}, [reuse_flag], {(pinlist)}
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EDGE  -  EDGE errors）

```
EDGE? {(pinlist)}
```

returns:

```
EDGE {fail_string},{(pinlist)}
```

for each group of consecutive pins having the same result.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EDGE  -  EDGE errors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98586.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：pinlist | The name of the pin or pins for which edge direction definitions are to be read back. This parameter can also include groups previously created by the…

### Example（取自子主题 Commands in alphabetical order › List of commands › EDGE  -  EDGE errors）

```
> EDGE? (pin1, pin2, pin3, pin4)
< EDGE ...F.... (pin1,pin2)
< EDGE .F..F... (pin3)
< EDGE ..F..... (pin4)
```

### EDSP（取自子主题 Commands in alphabetical order › List of commands › EDSP  EDSP  -  EDge SPecification）

The edge_spec parameter specifies a physical edge (d1 through d8 or r1 through r8):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}
```

The edge_spec parameter is a data parameter (D1, D2, C1, C2, E1, or E2):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}
```

### EDSP?（取自子主题 Commands in alphabetical order › List of commands › EDSP  EDSP  -  EDge SPecification）

```
EDSP? [dc_ref], {(pinlist)}
```

returns:

```
EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98589.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set | Specifies a waveform set number for a fixed timing setup.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EMAP  -  Error MAP）

```
EMAP? {pin_res},{start_cycle},{no_of_cycles},{resolution_mode},[results_per_cycle],[bits],{rep_mode},{results_align},[byte_max], [MUX,] {(pinlist)}
```

returns:

```
EMAP {pin_res},{start_cycle},{no_of_cycles},{resolution_mode},{results_per_cycle},{bits},{rep_mode},{results_align},[byte_max],{(pinlist)}, [MUX,] {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98590.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 3 列。
> 首行（上游原文）：pin_res | Specifies the pin granularity. Possible values are:

The binary data that are returned. The general format is:

Nn1n2...nNdata_stream

where the digit N defines the number of the digits ni (1 ≤i ≤N) that specify the length of data_stream in bytes.

The data stream itself consists of blocks each of which contains result data for every cycle (passed as well as failed) within a contiguous cycle range. Every block has a header that specifies

- the number of the first cycle of the block (8 bytes, big-endian encoded), and
- the block size in bytes (4 bytes, big-endian encoded).

The result data is also big-endian encoded.

If the rep_mode parameter has been set to ALL, only one block is returned, which contains the whole selected result range.

If rep_mode has been set to EOLY, then EMAP? will close a block after a failed cycle, and start a new block at the next failed cycle, if the passed cycles in-between occupy at least as much space as a block header (12 bytes). See the first example below.

If you are working with HXA pins note that the block size specifies bytes, not cycles. Thus, a block of size 32 contains 4 cycles of a HXA pin with 4 multiplexed Pin Scale pins.

 |

### Example 1（取自子主题 Commands in alphabetical order › List of commands › EMAP  -  Error MAP）

```
> EMAP? COMB,0,42,EDGE,8,,EOLY,BYTE,,(dut_tx3)
< EMAP COMB,0,42,EDGE,8,PF,EOLY,BYTE,,(dut_tx3),#9000000038
  \x00\x00\x00\x00\x00\x00\x00\x0F
  \x00\x00\x00\x03
  \x03\x00\x80
  \x00\x00\x00\x00\x00\x00\x00\x1F
  \x00\x00\x00\x0B
  \x80\x00\x00\x80\xA0\x00\x80\xA0\x00\x00\x0A
```

This example shows the format of the binary data that is returned by EMAP?. The data stream has been broken up to make it more readable. Two data blocks are returned. The information is to be decoded as follows:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98590.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 6 列。
> 首行（上游原文）：Block | Start cycle | Number of cycles | Failing edges

For each cycle, all 8 edges are reported. The first block is closed because 13 passing cycles (= 13 bytes) lie between the failed cycle 17 and the next failed cycle 31.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › EMAP  -  Error MAP）

```
> FTST?
< FTST F
> EMAP? COMB,0,50000000,EDGE,8,PF,EOLY,BYTE,3500000,(O1,O2)
< EMAP COMB,0,12000000,EDGE,8,PF,EOLY,BYTE,EOB,(O1,O2),#90003500000
```

This example illustrates the use of the byte_max parameter. The test comprises 50 million cycles. The Error Map is located in the RDRAM. If the number of errors exceeds 0.5% of the cycles, that is, as soon as more than 250,000 errors have been found, the device is to be rejected offhand. Therefore, EMAP? is called with the EOLY option, so that only failed cycles are returned, and the maximum length of the reply is restricted to 3,500,000. This is based on the worst case assumption that every error occupies 13 bytes. The answer indicates that in fact more than 0.5% of the cycles have failed. Note that only 7% of the 50 million test cycles have to be uploaded to the system controller.

### Example 3（取自子主题 Commands in alphabetical order › List of commands › EMAP  -  Error MAP）

The following example illustrates the difference between the resolution modes EDGE and SCYC.

```
> DCRM? EMAP,(@)
< DCRM EMAP,4,PFC,"c1:1 c2:2 c3:7 c4:8",(@)
> $EMAP? PPIN,0,12,EDGE,,PF,ALL,BYTE,,(out)
< EMAP PPIN,0,12,EDGE,8,PF,ALL,BYTE,,(out),#224
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00001100   11000011   10000011   00000000   00000000
     00000000   00000000   00000000   00000011   00000000   00000000   00000000   00000000

> $EMAP? PPIN,0,12,SCYC,,PF,ALL,BYTE,,(out)
< EMAP PPIN,0,12,SCYC,4,PF,ALL,BYTE,,(out),#224
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00001100   11110000   10110000   00000000   00000000
     00000000   00000000   00000000   00110000   00000000   00000000   00000000   00000000
```

The first failing cycle is cycle 0 (fifth byte in the second line of the EMAP? reply); in this cycle, edges 1,2,7,8 have failed. In addition, cycle 1 (edges 1,3,4) and 7 (edges 3,4) contain errors. With the PACK option, resolution mode SCYC compresses 12 bytes into 6:

```
> $EMAP? PPIN,0,12,SCYC,,PF,ALL,PACK,,(out)
< EMAP PPIN,0,12,SCYC,4,PF,ALL,PACK,,(out),#218
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00000110   11111011   00000000   00000000   00000011
     00000000   00000000
```

But the following call of EMAP? will produce an error message:

```
> $EMAP? PPIN,0,12,EDGE,4,PF,ALL,PACK,,(out)
```

The reason for this is that the results per cycle are only 4 bits long.

### Example 4（取自子主题 Commands in alphabetical order › List of commands › EMAP  -  Error MAP）

The following example shows the expanded format for 2 bit error codes (2 bytes per cycle):

```
> DCRM? EMAP,(@)
< DCRM EMAP,4,PFC,"c1:1 c2:2 c3:3 c4:4",(@)
> $EMAP? PPIN,0,7,EDGE,,PFC,ALL,BYTE,,(out)
< EMAP PPIN,0,7,EDGE,8,PFC,ALL,BYTE,,(out),#228
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00001110   11110011   00000000   00001111   00000000
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00001100   00000000
```

In cycle 0, edges 1, 2, and 4 have failed. In cycle 1, edges 3 and 4 have failed. In cycle 6, edge 3 has failed.

```
> $EMAP? PPIN,0,7,EDGE,4,PFC,ALL,PACK,,(out)
< EMAP PPIN,0,7,EDGE,4,PFC,ALL,PACK,,(out),#220
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00000111   11110011   00001111   00000000   00000000
     00000000   00000000   00001100
```

In this case, the PACK option is accepted because the initial segment of 4 two bit codes already makes up one byte.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EMBS  Error Map Block Size）

```
EMBS {(Block_size)}, {(pinlist)}
```

Note After invoking the EMBS command, all subsequent uploads will also utilize the user defined upload chunk size. You have to restore the internal paging mechanism into its default using the EMBS STRD command:

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EMBS  Error Map Block Size）

```
EMBSSTRD, {(pinlist)}
```

You can inquire about the error map block size for list of pins using EMBS? inquiry:

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EMBS  Error Map Block Size）

```
EMBS? {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EMBS  Error Map Block Size）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140727.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Block_size | Minimum 8 bytes up to a maximum of 16 MB. Resolution of the block size is 1 byte. The EMBS STRD command must be used to switch back to default size…

### ENSP（取自子主题 Commands in alphabetical order › List of commands › ENSP  ENSP  -  ENable Sampling Profile）

```
ENSP {operation_state},{(pinlist)}
```

### ENSP?（取自子主题 Commands in alphabetical order › List of commands › ENSP  ENSP  -  ENable Sampling Profile）

```
ENSP? {(pinlist)}
```

returns

```
ENSP {operation_state},{(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › ENSP  ENSP  -  ENable Sampling Profile）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125000.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：operation_state | Specifies the operation state (ON|OFF)

### Example（取自子主题 Commands in alphabetical order › List of commands › ENSP  ENSP  -  ENable Sampling Profile）

```
ENSP ON,(@)
```

or

```
ENSP ON,(dps1,dps2)
```

or

```
ENSP OFF,(@)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EPRC  -  Error Propagation Repetition Count）

```
EPRC? {no_of_vectors}, {(port_list)}
```

returns:

```
EPRC {no_of_vectors}, {no_of_repetitions}, {(port)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EPRC  -  Error Propagation Repetition Count）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98591.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：no_of_vectors | Specifies the size of the vector block that is to be repeated.

### Example（取自子主题 Commands in alphabetical order › List of commands › EPRC  -  Error Propagation Repetition Count）

The following examples queries the required number of repetitions for the three ports of the timing specification `MP_SPEC2`.

```
> SPRM "MP_SPEC2",1,1,1
> EPRC? 2,(@@)
< EPRC 2,228233,(Port1)
< EPRC 2,342193,(Port2)
< EPRC 2,171253,(Port3)
```

### EQFC（取自子主题 Commands in alphabetical order › List of commands › EQFC  EQFC  -  EQualization and Filter Configuration）

```
EQFC {level_set_no|level_set_id|ALL|PRM} ,{filter_parameter|ALL_specifier}, {offset_value|filter_value}, {(pinList)}
```

### EQFC?（取自子主题 Commands in alphabetical order › List of commands › EQFC  EQFC  -  EQualization and Filter Configuration）

```
EQFC? {level_set_no|level_set_id|ALL|PRM} ,{filter_parameter|ALL_specifier|ALL}, {value}, {(pinList)}

```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EQFC  EQFC  -  EQualization and Filter Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112905.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：level_set_no | The identification number of the level set (fixed levels) in which you want the filter/equalization values to be included. The number must not ex…
> 表内引用（4 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `Impact and characteristics of the equalization parameter filter_parameter`（raw: `02.06.02.02.107_EQFC__EQFC__-__EQualization_and_Filter_Configuration.md#_112905__table_filter_parameter_710x`） · `Possible values for ALL_specifier`（raw: `02.06.02.02.107_EQFC__EQFC__-__EQualization_and_Filter_Configuration.md#_112905__table_all_specifier`） · `Valid ranges for the equalization parameters (set value using "offset_value")`（raw: `02.06.02.02.107_EQFC__EQFC__-__EQualization_and_Filter_Configuration.md#_112905__table_offset_value_710x`）

Impact and characteristics of the equalization parameter filter_parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112905.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 4 列。
> 首行（上游原文）：Value | Description | PS1600 | PS5000

Possible values for ALL_specifier
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112905.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：Value | Description | Modified parameter

Valid ranges for the equalization parameters (set value using "offset_value")
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112905.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：Equalization amplitude | PS1600 | PS5000

n/a

   | -19% …17% |

The offset for the equalization amplitude is given in percentage related to the swing value.

### Example（取自子主题 Commands in alphabetical order › List of commands › EQFC  EQFC  -  EQualization and Filter Configuration）

```
EQFC 1, LPFI, 0.080, (@)
EQFC 1, EQI1, 75.5, (pin1,pin2)
```

```
EQFC? 1, ALL, (pin1,pin2)
```

```
EQFC 1, EQI1, 75.5,(pin1,pin2)
EQFC 1, EQI2, 0,(pin1,pin2)
EQFC 1, EQI3, 0,(pin1,pin2)
EQFC 1, EQO1, 0,(pin1,pin2)
EQFC 1, EQO2, 0,(pin1,pin2)
EQFC 1, EQO3, 0,(pin1,pin2)
EQFC 1, LPFI, 0,(pin1,pin2)
EQFC 1, LPFO, 0.080,(pin1,pin2)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EQFS -  EQuation FileS command transfer）

```
EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EQFS -  EQuation FileS command transfer）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98592.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification to use:

### Example（取自子主题 Commands in alphabetical order › List of commands › EQFS -  EQuation FileS command transfer）

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

This example loads the level equation file from /tmp/level_equation.

### EQSP（取自子主题 Commands in alphabetical order › List of commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP {spec_type}, {part}, {#spec(data)}
```

### EQSP?（取自子主题 Commands in alphabetical order › List of commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP?{spec_type}, {part}
```

returns:

```
EQSP {spec_type}, {part}, {#spec(data)}
```

if these are not empty, for backward compatibility.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98593.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：spec_type | The mandatory parameter defines which specification type to use. Use: LEV to specify levels TIM to specify timing

### Example（取自子主题 Commands in alphabetical order › List of commands › EQSP  EQSP  -  EQuation SPecification transfer）

The following example queries the current wavetables:

```
> EQSP? TIM,WVT
< EQSP TIM,WVT,#9000000127WAVETBL table1  # derived from waveform set 1

  PINS Pin1 Pin2
  WFDS 0  "d1:D11"
  1    0   .   .   .
  2    1   .   .   .
  BWDS ""

  @
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › ERCC  -  ERror in Cycle range Count）

ERCC? {type}, {start_cycle}, {no_of_cycles}, [MUX,] {(pinlist)}

returns:

ERCC {type}, {start_cycle}, {no_of_cycles} [, granularity], {valid_code}, {no_of_errors}, [map_mode], [MUX,] {(pin)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › ERCC  -  ERror in Cycle range Count）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98594.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 5 列。
> 首行（上游原文）：type | The type parameter can be:

### Example（取自子主题 Commands in alphabetical order › List of commands › ERCC  -  ERror in Cycle range Count）

```
> ERCC? ERCP, 1000, 200, (pin1,pin2)
< ERCC ERCP, 1000, 200, VALD, 5, F160, (pin1)
< ERCC ERCP, 1000, 200, VALD, 1, F160, (pin2)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › ERCE  -  Expected and Received Cycle data of Events）

```
ERCE? {type},{start_cycle},{no_of_cycles},{data_format},{rep_mode}, [byte_max], {(pinlist)}
```

returns:

```
ERCE  {type}, {start_cycle}, {no_of_cycles}, {data_format}, {rep_mode}, [error_status], {(pin)}, {#spec(data)}



```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › ERCE  -  Expected and Received Cycle data of Events）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118682.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 9 列，含嵌套表。
> 首行（上游原文）：type | The supported types are: RCV | Requests received data only. Can only be requested if a test point pattern has been executed for DC Scale pins.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118682.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：RCV | Requests received data only. Can only be requested if a test point pattern has been executed for DC Scale pins.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118682.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：0 | This format contains PASS/FAIL and status information for every cycle. It can be used for status analysis where expected data and measurement values are not…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118682.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：ALL | Reports all results within the selected area.

The binary data that are returned. The general format is:

#Nn1n2n...nNdata_stream

The N digit defines the number of the digits ni (1 ≤i ≤N) that specify the length of data_stream in bytes.

The data stream itself consists of a stream header and one or more answers (only one answer for data formats 0 and 1), where every answer contains the same number of data blocks.

The stream header defines

- the number of answers (4 long bytes, big-endian encoded)
- the number of data blocks per answer (4 long bytes, big-endian encoded).

Every data block consists of a block header and one data unit which contains the data of one event (td element).

The block header specifies the cycle number of the event anchor (defined with TPSE) (8 long bytes, big-endian encoded). The cycle number can be different from the event anchor, which is a vector number.

The length of the data units depends on the selected format and on the selected type. If type is set to ALL, each data unit consists of the expected data and the received data in this order.

Graphically, the structure can be illustrated by a simple example with a cycle range from 100 through 500 as follows:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118682.htm`
> 中**第 6 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：27 行 × 5 列。
> 首行（上游原文）：Content | Bytes | Bits | Description

The data block encoding for the received data is almost identical to that of data format 0 except that it also provides the measurement type and value.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118682.htm`
> 中**第 7 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 4 列。
> 首行（上游原文）：Content | Bytes | Bits | Description

### Application

DC Dynamic

### Example（取自子主题 Commands in alphabetical order › List of commands › ERCE  -  Expected and Received Cycle data of Events）

The following example shows a query for expected data only in the cycle range from 0 through 60000.

```
> ERCE? EXP,0,60000,1,ALL,,(dpsPinMea)
< ERCE EXP,0,60000,1,ALL,,(dpsPinMea),#9000000405
    /x00/x00/x00/x01/x00/x00/x00/x0F
    /x00/x00/x00/x00/x00/x00/x00/x46
    /x00/x1D
    /x00/x00/x00/x00/x00/x00/x00/x00
    /x40/x10/x00/x00/x00/x00/x00/x00
    /x00
    /x00/x00/x00/x00/x00/x00/x00/x00
    . . .
```

The data stream has been broken up to make it more readable. The answer contains 15 (`/x0F`) data blocks, of which only the first is displayed in the example. Its cycle number is 70 (`/x46`). The event is a voltage range definition (`x1D`) which is defined by DFTD as follows

```
DFTD "myNamespace",INSERT,(dpsPinMea),#2473<?xml version="1.0"?>
<testdata>
  <td id="setMeasVoltRange" type="dcset">
    <setMeasureRange type="voltage" minValue="0" maxValue="4"/>
 . . .
```

Since this is not a measurement event, the result check byte is set to 0. Note that the cycle number and the two range limits are big endian coded. The event contains no setForceValue operation.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › ERCT  -  ERror CounT）

```
ERCT? {type}, [MUX,] {(pinlist)}
```

returns:

```
ERCT {type}, {valid_code}, {no_of_errors}, [map_mode], [MUX,] {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › ERCT  -  ERror CounT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98595.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：type | The type parameter can be:

### Example（取自子主题 Commands in alphabetical order › List of commands › ERCT  -  ERror CounT）

```
> ERCT? ERCP, (Q0)
< ERCT ERCP, VALD, 1, F160, (Q0)
```

This example requests the error count for pin Q0. The system returns one error, the error count is valid, the map mode is F160.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › ERCY  -  ERror CYcle）

```
ERCY? {type}, {start_cyc_no}, [no_of_cycles], [no_of_errors], {(pinlist)}
```

returns:

```
ERCY {type}, {cycle_no}, [window_len], [expected_data], [received_data], [data_type], {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98596.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：32 行 × 3 列。
> 首行（上游原文）：type | Selects the type of error data to be returned. The parameter can be:
> 表内引用（1 条，供检索）：`WAVE`（raw: `02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › ERCY  -  ERror CYcle）

```
> ERCY? ALL,0,,2,(pin1,pin2)
< ERCY ALL,215,-2,F1,F0,E1,(pin1)
< ERCY ALL,240,,F0,FI,FIX,(pin1)
< ERCY ALL,17,,F0,F1,FIX,(pin2)
```

This example queries the system for the first two error cycles of pin1 and of pin2, starting from cycle 0. Expected and received data are also to be returned. The system returns the first two error cycles of pin1. For pin2 only one error cycle exists, therefore only one cycle can be returned.

There is an error on pin1 in cycle 215 which was a window compare 3 cycles long. The expected data was a 1, the receive data was a 0. The window compare was made to the E1 parameter.

There is an error on pin1 in cycle 240 which was an edge compare to a fixed state. The expected data was a 0, the received data was intermediate.

There is an error on pin2 in cycle 17 which was an edge compare to a fixed state. The expected data was 0, the received data was 1.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › ERMP  -  ERror MaP）

```
ERMP? {map_id}, {start_unit}, {no_of_units}, [map_mode],[edges,] [MUX,] {(pinlist)}
```

returns:

```
ERMP {map_id}, {start_unit}, {no_of_units}, {map_mode},[edges,] [MUX,] {(pinlist)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98597.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 8 列，含嵌套表。
> 首行（上游原文）：map_id | Determines the type of Error Map for which data is to be read out. Note that the allowed values depend on the settings of the DCRM command. Options tha…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98597.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 4 列。
> 首行（上游原文）：Expected Data | FAIL1 | FAIL2 | FAIL3

### Example（取自子主题 Commands in alphabetical order › List of commands › ERMP  -  ERror MaP）

```
> ERMP? OVEM, 0, 16, F160,(Q0)
< ERMP OVEM,0,16,F160,(Q0),#9000000001 0x80
```

This example requests Overview Error Map data for the output pin Q0 in the Start Analysis mode between vectors 0 and 15.

```
> $ERMP? EDGE,0,7,F160,3,(Q0,Q7)
< ERMP EDGE,0,7,F160,3,(Q0,Q7),
  1100 0000  0000 0000  0010 0000  1100 0000  0000 0000  0000 0000 0000 0000
```

This example uses the "$" prefix, by which the binary data stream is represented bitwise by an ASCII "1" or "0" (see `Storing and Retrieving Binary Data`（raw: `02.06.01.03.04_Storing_and_Retrieving_Binary_Data.md`）). The call requests edge specific data for the output pins Q0, Q7. The first three receive edges of each of the first 7 cycles are queried. One byte is returned for every cycle. The result is that there are errors at edges 1 and 2 in cycle 0 and cycle 3, and an error at edge 3 in cycle 2. The other cycles contain no errors at the first three edges.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › ERRE  -  Expected and Received Results of Events）

```
ERRE? {type}, {resultIndex}, {numResults}, {data_format}, {rep_mode}, [byte_max] [,gang_index], {(pinlist)}
```

returns:

```
ERRE {type}, {resultIndex}, {numResults}, {data_format}, {rep_mode}, [error_status] [, gang_index], {(pin)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/97182.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：type | The supported types are: RCVRequests received data only. Can only be requested if a test point pattern has been executed for DC Scale pins, or a DC patte…
> 表内引用（1 条，供检索）：`PSLR`（raw: `02.06.02.02.194_PSLR__PSLR__-__Power_Supply_Level_Ranges.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › ERRE  -  Expected and Received Results of Events）

```
# Get the number of available results
> VALR? (dpsPin)
< VALR CONS,10,(dpsPin)

# upload the first 5 received results in format 0
> ERRE? RCV,0,5,0,ALL,,,(dpsPin)
< ERRE RCV,0,5,0,ALL,(dpsPin),#9000000021
  \x00\x00\x00\x01\x00\x00\x00\x01
  \x00\x00\x00\x00\x00\x00\x00\x05
  \x00\x02\x00\x00\x0C
```

The data stream has been broken up to make it more readable. The first test point measurement failed because of a low limit violation, the fourth because of a low clamp violation.

### ESGB（取自子主题 Commands in alphabetical order › List of commands › ESGB  ESGB  -  Edge Search GloBal）

```
ESGB [lin_step], [lin_bin_step], [min_pulse]
```

### ESGB（取自子主题 Commands in alphabetical order › List of commands › ESGB  ESGB  -  Edge Search GloBal）

```
ESGB?
```

returns:

```
ESGB [lin_step], [lin_bin_step], [min_pulse]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › ESGB  ESGB  -  Edge Search GloBal）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98598.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：lin_step | The lin_step parameter defines the step width (in ns) to be used for the linear searches which can be initiated by the TTRS? query. Any negative numb…

### Example（取自子主题 Commands in alphabetical order › List of commands › ESGB  ESGB  -  Edge Search GloBal）

```
ESGB 20,30,0
```

This example defines a 20 ns step width for linear search and a 30 ns step width for the combined linear/binary search. The minimum allowed pulse width is 0 ns.

### ETDS（取自子主题 Commands in alphabetical order › List of commands › ETDS  ETDS  -  Edge Timing Definition String）

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### ETDS?（取自子主题 Commands in alphabetical order › List of commands › ETDS  ETDS  -  Edge Timing Definition String）

ETDS? {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {(pinlist)}

returns:

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › ETDS  ETDS  -  Edge Timing Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98599.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `Defining waveforms for Pin Scale 9G pins`（raw: `02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`） · `Selecting and ordering edges`（raw: `02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › ETDS  ETDS  -  Edge Timing Definition String）

```
> ETDS 1,1,,"e1:0 e2:2 e3:6 e4:4",(io)
> ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
> ETDS? 1,1,,(@)
< ETDS 1,1,,"d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4",(io)
< ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › ETDS  ETDS  -  Edge Timing Definition String）

The following example shows the various possibilities for using ETDS with fast pins:

```
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5 d3:10 d4:15",(CP)
> ETDS 401,1,,"d2:5.5",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5.5 d3:10 d4:15",(CP)
> ETDS 401,1,,"pdiv:4 d1:3 d3:14",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:14 d4:18",(CP)
> ETDS 401,1,DELTA,"d3:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:12 d4:18",(CP)
> ETDS 401,1,DELTA,"pdiv:4 d1:0 d2:1 d4:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:6 d3:10 d4:14",(CP)
```

Note in particular the effect of the first instance of the command in DELTA mode. The negative offset is not applied to the actual value of d3, which is 14, but to the calculated default value, which is 13.

### Example 3（取自子主题 Commands in alphabetical order › List of commands › ETDS  ETDS  -  Edge Timing Definition String）

This example shows how to set and retrieve a delay of a multi-port specification:

```
> ETDS? "mu_timing",2,,(In1)
< ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ETDS "mu_timing",2,,"d1:0.5",(In1)
> ETDS? "mu_timing",2,,(In1)
< ETDS "mu_timing",2,,"d1:0.5",(In1)
```

The specification name and the pin name identify the port (no pin may occur in more than one port within the same specification). Then the port and the specification identify the equation set.

### ETIM（取自子主题 Commands in alphabetical order › List of commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

### ETIM?（取自子主题 Commands in alphabetical order › List of commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM? {waveform_set}, {timing_set}, {(pinlist)}
```

returns:

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

or:

```
ETIM? {specset_id}, {timing_set_no}, {(pinlist)}
```

returns:

```
ETIM {specset_id}, {timing_set_no}, [t1], [t2], [t3], [t4], [t5], [t6],{(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98600.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `ETIM, ETIM? - (Edge TIMing)`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM 1,1,2,4,8,6,10,,(DATA)
```

This example sets the edge delays for the pin group DATA specified for waveform set 1 and timing set 1. Edges 1 to 5 are set to 2,4,8,6 and 10 ns respectively, edge 6 is unused. If no previous setting for edge 6 exists in waveform set 1 and timing set 1, then its delay remains at 0.0 ns.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EUDS  -  Edge Usage Definition String）

```
EUDS? {waveform_set}, [mode], {(pinlist)}
```

returns:

```
EUDS {waveform_set}, {definition_string}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EUDS  -  Edge Usage Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98601.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter ALL for all defined waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The wa…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › EUDS  -  Edge Usage Definition String）

```
EUDS? 1,,(@)
EUDS 1,"d1 d2 d3 r4",(io)
EUDS 1,"d1 d2 d3 d4 d5 d6 d7 d8",(clk)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EVCK  -  EVent ClocK）

```
EVCK? {"multi-port_spec"}, {(port_list)}
```

returns:

```
EVCK {"multi-port_spec"}, event_clock_per, {(port)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › EVCK  -  EVent ClocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126417.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：multi-port_spec | Name of a multi-port timing specification.

### Example（取自子主题 Commands in alphabetical order › List of commands › EVCK  -  EVent ClocK）

```
>  SCLK? "mu_burst"
<  SCLK "mu_burst",480
>  EVCK? "mu_burst",(@@)
<  EVCK "mu_burst",2448,(PortA)
<  EVCK "mu_burst",2448,(PortB)
<  EVCK "mu_burst",480,(PortD)
<  EVCK "mu_burst",480,(PortE)
```

This example returns the system clock period and the event clock periods for the multi-port timing specification `mu_burst`. The event clock periods of `PortD` and `PortE` equal the system clock period, those of `PortA` and `PortB` are different.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › EXSR -  EXecute SeaRch）

```
EXSR{set_nr}
```

Parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98602.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：set_nr | Specifies the number of the search set which is to be executed.

### Example（取自子主题 Commands in alphabetical order › List of commands › EXSR -  EXecute SeaRch）

```
> EXSR 1
> EXSR 2
```

Note that the results for search set 1 are still extant after execution of search set 2.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › FFCI  -  First Failed Cycle Information）

```
FFCI? {(no_ffcyc)} [,(port)]
```

returns:

```
FFCI {(no_ffcyc)}, {no_pins}, {#spec(data)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › FFCI  -  First Failed Cycle Information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98603.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：no_ffcyc | Number of first failed cycles to be reported.
> 表内引用（1 条，供检索）：`FFPM? (First Failing cycle information Pin Mapping)`（raw: `02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md`）

### Example 1: Firmware view（取自子主题 Commands in alphabetical order › List of commands › FFCI  -  First Failed Cycle Information）

```
$FFCI? 2
FFCI 2,7,#218
  00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000011
  01100000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
  00010000 00010000
```

This example for `Firmware view`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.md`） queries the first two cycles where failures have occurred on an output pin of the default port, that is, on any configured output pin. Note: For the query, you must use the prefix $ so that the binary data are represented by ASCII 1 or 0.

The answer is to be interpreted as follows:

- `FFCI 2,7` means that 2 cycles are reported and 7 output pins are configured. Since this entails that one byte is sufficient for the pin data, the binary data needs only one byte for the pin data consists of 2 * 9 bytes.
- `#218` defines the size of the following binary data: 2 digits for the length specifier followed by the length specifier itself that indicates a length of 18 for the binary data.
- The Firmware view displays the cycle numbers and pin data as groups of eight bytes that must be evaluated as follows:

  - Failed cycle # 3:

    - The cycle number 3 is defined by the first eight address bytes `0000000` … `00000011`.
    - The 9th byte `01100000` shows failures on the 2nd and 3rd pin: Value 0 of the MSB on the left represents the passing 1st pin.

  - Failed cycle # 16:

    - The next eight bytes 10 …17 (`00000000` … `00010000`) define the cycle number 16.
    - The last byte 18 (`00010000`) shows that the fourth pin failed.

For the assignment from bits of the pin data bytes to the configured pins, refer to `#spec(data)`（raw: `02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md#_98603__r_specData`）, the `following example`（raw: `02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md#_98603__d_Example_2`） and to firmware command `FFPM? (First Failing cycle information Pin Mapping)`（raw: `02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md`）.

The FFCI? command can also be executed using API `FW_TASK`（raw: `../02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.md`）. You must use the syntax `FWTASK_STATUS FW_TASK(const STRING& command, FW_ResultData & resultdata);` to retrieve the binary data.

### Example 2: Sort order of pins（取自子主题 Commands in alphabetical order › List of commands › FFCI  -  First Failed Cycle Information）

The pogo numbers of the following example setup are assigned in descending order to emphasize that the order of the pogo numbers and not the order of the definition by `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） matters.

```
DFPN 11105,"",(pinA)
DFPN 11104,"",(pinB)
DFPN 11103,"",(pinC)
DFPN 11102,"",(pinD)
DFPN 11101,"",(pinE)
CONF IO,F160,(pinA)
CONF I,F160,(pinB,pinC)
CONF O,F160,(pinD,pinE)
```

The FFCI? command will sort I / IO pins based on their pogo number defined for the first site resulting in the pin list pinE, pinD, pinA. The two pins pinB and pinC have no output capability and, therefore, will not be included in the FFCI? answer.

Assuming a test has been executed where pinA passes, but pinD and pinE fail for every cycle, the FFCI? answer for the first two failing cycles now would look like this:

```
FFCI? 2
FFCI 2,3,#218
  00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
  11000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
  00000001 11000000
```

 The binary data of the answer is to be interpreted as follows:

- Byte 1 …8: Address of the first cycle (`00000000` … `00000000` = 0)
- Byte 9: Pin data `11000000`
- Byte 10 …17: Address of the second cycle (`00000000` … `00000001` = 1)
- Byte 18: Pin data `11000000`

Byte 9 and 18 show that the first two pins on the left side (MSB) are failing. According to the sorting scheme that is defined in the FFCI parameter description for `#spec(data)`（raw: `02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md#_98603__r_specData`）, the failed pins are pinE (Channel 11101 and pinD (Channel 11102).

The `FFPM?`（raw: `02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md`） firmware command will return `FFPM 3,(pinE,pinD,pinA)` as pinE, pinD and pinA are configured for the I / IO mode. The pin list is sorted by the pogo number defined for the first site.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › FLBL  -  Failing LaBeLs）

```
FLBL? {cycle_info},[start_cycle]},[no_of_cycles],{(port)}
```

returns:

```
FLBL {index_of_call},{label_name},{cycle_info}, [ffc_abs],[ffc_rel],[ffv], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › FLBL  -  Failing LaBeLs）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98605.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：18 行 × 4 列。
> 首行（上游原文）：cycle_info | This parameter specifies which information is to be retrieved about the first failing cycle of the labels. Possible values are:.

### Example（取自子主题 Commands in alphabetical order › List of commands › FLBL  -  Failing LaBeLs）

```
> FLBL? ALL,0,105,(@)
< FLBL 1,"MainFailures",ALL,26,10,10,(Read)
< FLBL 1,"MainFailures",ALL,25,9,9,(Write,RowAS)
< FLBL 1,"MainFailures",ALL,20,4,4,(Addr3)
< FLBL 1,"MainFailures",ALL,23,7,7,(Data0,Data1,Data2,Data3)
< FLBL 3,"MainRowAsFail",ALL,82,18,6,(RowAS)
< FLBL 4,"MainWriteFail",ALL,92,4,4,(Write)
< FLBL 5,"MainFailures",ALL,114,10,10,(Read)
< FLBL 5,"MainFailures",ALL,113,9,9,(Write,RowAS)
< FLBL 5,"MainFailures\",ALL,108,4,4,(Addr3)
```

This example returns all available information for a single-port burst from cycle 0 through 104. The first two replies for the first call of label MainFailures are to be read as follows: Pin Read fails at cycle 26, counted from the start of the burst, which is 10 counted from the start of the label. The pins Write and RoWAS already fail at cycle 25, respectively 9.

Note that the fifth call is included in the reply although none of its failing cycles is inside the requested cycle range. Every failing label which has at least one cycle in the specified range is reported.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › FLSH -  FLuSH buffered commands）

```
FLSH {MUX}, {"init_flags"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › FLSH -  FLuSH buffered commands）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99061.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：MUX | The optional MUX parameter is designed to be used as an execution code of a testflow that is generated by the system software for disconnecting the partic…

### Syntax（取自子主题 Commands in alphabetical order › List of commands › FTCG  FTCG  -  Functional Test ConfiGure）

FTCG

```
FTCG {parameter}, {mode}, {(portlist)}
```

  FTCG?

```
FTCG? {parameter}, {(@@)}
```

returns:

```
FTCG {parameter}, {mode}, {(portlist)}
```

  Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98606.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：parameter | The parameter to be used is SKPR (SKip PRimaries).

### Example（取自子主题 Commands in alphabetical order › List of commands › FTCG  FTCG  -  Functional Test ConfiGure）

The following example illustrates the dependence of the FTCG command on the current sequencing group definitions.

```
> SQLB "MP_burst1",MPBU,28,31,"SG1",(clock)
> SQLB "MP_burst1",MPBU,28,29,"SG2",(data1)
> SQLB "MP_burst1",MPBU,31,32,"SG2",(data2)
> SQLB "MP_burst2",MPBU,32,33,"SG1",(clock)
> SQLB "MP_burst2",MPBU,30,31,"SG1",(data1)
> SQLB "MP_burst2",MPBU,33,34,"SG2",(data2)
> FTCG SKPR,ON,(clock)
> FTCG SKPR,NEVER,(data2)
> SPRM "cont_clock",,,
> SQSL "MP_burst1"
> SQGB ACQF,0
> FTST?
...
> SQSL "MP_burst2"
> FTST?
...
```

In the first functional test, sequencing group `SG1` only contains the port `clock`, and therefore activation of primary sets is suppressed at the start of `MP_burst1` only for `clock`, whereas it is enforced for ports `data1` and `data2`. In the second test, `SG1` contains both `clock` and `data1`, and therefore activation is suppressed for both these ports at the start of `MP_burst2`, and enforced only for `data2`.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › FTSM  FTSM  -  Functional Test Set Mask）

```
FTSM {mode}, [run_to], [mask_before], [mask_after][,(ref_port)]
FTSM?
FTSM?
```

returns:

```
FTSM CLEAR, , ,
```

or

```
FTSM SET, [run_to], [mask_before], [mask_after][,(ref_port)]
```

  Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98607.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：mode | Lets you set the mode of the FTSM command. The mode can be:

For a multi-port burst, this parameter specifies the reference port to which the cycle numbers of the run_to, mask_before, and mask_after parameters refer.

If you have set the run_to parameter, then the sequencers will be stopped for all ports after the reference port has completed the requested number of cycles. The mask_before, and mask_after parameters are only applied to the specified port. The other ports will not be masked,

Note that the reference port must belong to the current start label (as defined by SQSL).

   |  Application Used in the parametric functional test. Errors and warnings

An error is generated if:

- A value (run_to, mask_before, mask_after) is not in the valid range of [0... 2^48 - 2].
- The run_to and mask_before parameters are specified, and run_to is equal or bigger than mask_before.
- The run_to and the mask_after parameters are specified, and run_to is bigger than mask_after.

A warning is generated if:

- The run_to parameter and the mask_before parameter are specified and run_to < mask_before. In this case the pattern executed will always pass as all cycles executed are masked out for result evaluation.
- The run_to parameter and the mask_after parameter are specified and run_to <= mask_after. In this case the entry for the mask_after parameter can be omitted as the sequencer will not even execute the cycles that are masked out.

### Example（取自子主题 Commands in alphabetical order › List of commands › FTSM  FTSM  -  Functional Test Set Mask）

```
FTSM?
```

returns:

```
FTSM CLEAR, , ,
FTSM SET, ,10,20
```

The FTSM? query returns the current FTSM settings.

The FTSM SET command masks all cycles except for those in the range from cycle 10 to cycle 20.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › FTST  -  Functional TeST）

```
FTST? ["exec_context"]
```

returns:

```
FTST {result_flag}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › FTST  -  Functional TeST）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98608.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 6 列，含嵌套表。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98608.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：P | is returned if the functional test passes.

### Example（取自子主题 Commands in alphabetical order › List of commands › FTST  -  Functional TeST）

```
FTST?
```

returns:

```
FTST P
```

This example returns a pass result for the functional test.

### FXDL（取自子主题 Commands in alphabetical order › List of commands › FXDL  FXDL  -  FiXture DeLay）

```
FXDL {channel}, {fixture_delay}
```

### FXDL?（取自子主题 Commands in alphabetical order › List of commands › FXDL  FXDL  -  FiXture DeLay）

```
FXDL? {channel}
```

returns:

```
FXDL {channel}, {fixture_delay}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › FXDL  FXDL  -  FiXture DeLay）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98609.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：channel | The test system channel number of the digital channel. This is a five digit field. See DFPN, DFPN? - (DeFine Pin Name) for the number. You can type AL…
> 表内引用（1 条，供检索）：`DFPN, DFPN? - (DeFine Pin Name)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › FXDL  FXDL  -  FiXture DeLay）

```
FXDL 10101,2.5
```

This example sets the fixture delay of channel 10101 to 2.5 ns.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › GCTX  -  Get ConTeXt）

```
GCTX? {setup_type},[setup_comp]
```

returns:

GCTX {setup_type}{,setup_nr|"name"},"[context_name]"

### Parameters（取自子主题 Commands in alphabetical order › List of commands › GCTX  -  Get ConTeXt）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98611.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：setup_type | The type of the setup component for which the mode context is queried. Possible values are:

### Example（取自子主题 Commands in alphabetical order › List of commands › GCTX  -  Get ConTeXt）

```
> GCTX? TIM,101
< GCTX TIM,101,"High-Speed"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › GETA  -  GET vector memory Address information）

GETA? {type}, [param_1], {param_2}, {(pinlist)}

returns:

GETA {type}, {param_1}, {param_2}, {applic}, {start_addr}, {length}, {(pinlist)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › GETA  -  GET vector memory Address information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98613.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：type | Specifies the type of test for which vector area address information is required. The only allowed value is VEC (for VECtors).

### Example（取自子主题 Commands in alphabetical order › List of commands › GETA  -  GET vector memory Address information）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
> TSTL "test_1",(@)
> GETA? VEC,,9,(S0_1)
< GETA VEC,"test_1",9,PARA,520,6,(S0_1)
```

This example queries the absolute address of the parallel vector with the logical vector number 9 (the first active vector of the RPTV instruction) in the label test_1 for pin S0_1. Note that 7 padding vectors exist between the last active vector of the GENV instruction and the first active vector of the RPTV instruction.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › GETC  -  GET Cycles）

```
GETC? {(vector_no)}
```

returns:

```
GETC {(cycle_no)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98614.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：vector_no | The vector number for which you want to obtain the matching cycle number. vector_no must be a positive integer that does not exceed the maximum vect…

### Example（取自子主题 Commands in alphabetical order › List of commands › GETC  -  GET Cycles）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,103,,,(@)
< SQPG 3,GENV,7,,,(@)
< SQPG 4,MACT,256,,,(@)
< SQPG 5,GENV,1,,,(@)
< SQPG 6,MRPT,1,,,(@)
< SQPG 7,RPTV,1544,100,,(@)
< SQPG 8,GENV,1,,,(@)
< SQPG 9,STOP,,,,(@)
> GETC? 112
< GETC 104
> GETC? 1656
< GETC 154504
```

In this example, the cycle numbers are calculated from the expected values. Vector 112 is the first vector after the match loop. The last 6 vectors before the match loop are not recorded in the Error Map, because the sequencers consider them to be part of the match loop (see `Counted match loops`（raw: `02.06.07.01.08.04.03.01_Counted_match_loops.md`）). The two match loop vectors proper are also not recorded in the Error Map. Since no other loop has occurred before vector 112, the cycle number corresponding to vector 112 is calculated as 112 - 8 = 104.

The cycle number of vector 1656, the last vector of the label, is calculated as 104 + 100 * 1544 = 154504.

The calculation is more complicated if it is based on the received data, because the last match loop cycles may be recorded in the Error Map (see again `Counted match loops`（raw: `02.06.07.01.08.04.03.01_Counted_match_loops.md`）).

### Syntax（取自子主题 Commands in alphabetical order › List of commands › GETL  -  GET Label）

```
GETL? {index_first_call},[number_of_calls], {(pin_or_port)}
```

returns:

```
GETL {index_of_call},{label_name}, [start_cycle], [number_of_cycles], {(pin_or_port)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › GETL  -  GET Label）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98615.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：index_first_call | Specifies the index of the first label call within the burst for which the name is requested.

### Example（取自子主题 Commands in alphabetical order › List of commands › GETL  -  GET Label）

```
> GETL? 0,9,(@)
< GETL 0,"MainInit",0,16,(@)
< GETL 1,"MainFailures",16,24,(@)
< GETL 2,"MainPassing",40,24,(@)
< GETL 3,"MainFailures",64,24,(@)
< GETL 4,"MainPassing",88,24,(@)
< GETL 5,"MainFailures",112,24,(@)
< GETL 6,"MainPassing",136,24,(@)
< GETL 7,"MainFailures",160,24,(@)
< GETL 8,"MainDataFail",184,24,(@)
```

In this example, the label names are requested for the first 9 calls of the burst that was executed as the last test. Note that certain labels are called more than once.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › GETN  -  GEt Testdata Name）

```
GETN? {range_type}, {index}, {length}, {(pinlist)}
```

returns

```
GETN? {range_type}, {index}, {testdata_name}, {identifier}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › GETN  -  GEt Testdata Name）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118723.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：range_type | This parameter determines how the index and length parameters are to be interpreted. Possible options are: CYCL index and length refer to cycles RS…

### Example（取自子主题 Commands in alphabetical order › List of commands › GETN  -  GEt Testdata Name）

```
> FTST?
< FTST P

> VALR? (Sdd)
< VALR CONS,10,(Sdd)

> GETN? RSLT,0,1,(Sdd)
< GETN RSLT,0,"powercycle","meaLimV_0.0_0.2",(Sdd)

> VALC? (Sdd)
< VALC CONS,0,50000,(Sdd)

> GETN? CYCL,0,41000,(Sdd)
< GETN CYCL,63,"powercycle","setRange7V",(Sdd)
< GETN CYCL,40199,"powercycle","meaLimV_0.0_0.2",(Sdd)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › GETS  -  GET Sets）

```
GETS? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
GETS {start_cycle}, {no_of_cycles}, {timing_set}, {level_set}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98616.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：start_cycle | The start cycle is an integer that defines the first cycle to be reported. The start cycle is in the range 0 to 248 when the sequencer runs in the…

### Example（取自子主题 Commands in alphabetical order › List of commands › GETS  -  GET Sets）

```
GETS? 0,2000,(Q0)
```

This example requests the timing and level set information for the first 2000 test cycles of pin `Q0`. The response may be as follows:

```
GETS 0,160,2,1,(Q0)
GETS 160,704,1,1,(Q0)
GETS 864,1136,2,1,(Q0)
```

The first 160 cycles were generated with timing set 2 and level set 1, the next 704 cycles with timing set 1 and level set 1, and the last 1136 cycles with timing set 2 and level set 1 again.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › GETV  -  GET Vectors）

```
GETV? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
GETV {start_cycle}, {no_of_cycles}, {start_vector}, {no_of_vectors}, {seq_status}, {"label"|"scan_template"}, [instance], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › GETV  -  GET Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98617.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 5 列，含嵌套表。
> 首行（上游原文）：start_cycle | An integer that defines the first cycle to be reported. It is in the range 0 to 248 when the sequencer runs in the Start Analysis mode, or -248 to…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98617.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：sequencer instruction | reported as

### Example（取自子主题 Commands in alphabetical order › List of commands › GETV  -  GET Vectors）

```
> GETV? 0,50,(S0_1)
< GETV 0,9,0,9,GENV,"test_1",,(S0_1)
< GETV 9,30,9,6,RPTV,"test_1",,(S0_1)
< GETV 39,1,-1,-1,BRK,"test_1",,(S0_1)
```

The vectors for cycles 9 through 38 were generated by an RPTV instruction that generated 6 waveforms 5 times.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › GETX  -  GET eXtended vector information）

```
GETX? [type], [label], [vector], [cycle], [index], {(pinlist)}
```

returns:

```
GETX {type}, {label}, {vector}, {cycle}, [index], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › GETX  -  GET eXtended vector information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98618.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：type | The label type. You can supply one of the following options:

### Example（取自子主题 Commands in alphabetical order › List of commands › GETX  -  GET eXtended vector information）

```
> GETX? ,,,4,,(CP)
< GETX MAIN,"multi",4,4,,(CP)
```

This example asks for vector data at cycle 4 on pin CP. The system replies that cycle 4 was generated by vector 4 in a main label called multi.

Note that this type of query where only a cycle number is supplied is similar to the GETV? query requesting information on just a single cycle - see `GETV? - (GET Vectors)`（raw: `02.06.02.02.135_GETV__-__GET_Vectors.md`）.

```
> GETX? MAIN,"multi",10,,,(CP)
< GETX MAIN,"multi",10,10,,(CP)
```

This example requests the number of the cycle that was generated by vector 10 in the main label called multi. The system replies with cycle 10.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › GNOS  -  GetNumberofOccupiedSets）

GNOS? {set_type}

returns:

GNOS {NumberOfOccupiedSets},{MaxNumberOfSets},{NrOfOccupiedMSetActions},{MaxNumberOfMSETActions}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › GNOS  -  GetNumberofOccupiedSets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/142091.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：set_type | Must be MSET

### Example（取自子主题 Commands in alphabetical order › List of commands › GNOS  -  GetNumberofOccupiedSets）

```
> DSCP 4096,16,256,32,32,12800,16,1,256,9
> GNOS? MSET
< GNOS MSET,1,3201,1,12800
```

Related firmware commands:

- Configure sets: `MSET`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md`）
- Execute sets: `MEAS`（raw: `02.06.02.02.160_MEAS_-__execute_a_MEASurement_set.md`）
- Obtain results: `PMUR?`（raw: `02.06.02.02.179_PMUR___retrieve_PPMU_result.md`）

Define the maximum number of sets

- `Technology file for a device`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md`）
- `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） (pmu_set parameter)

### Syntax（取自子主题 Commands in alphabetical order › List of commands › HREX  -  High Resolution EXecution）

```
HREX? {(pinlist)}
```

returns:

```
HREX {(pin)}, {#spec(data)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › HREX  -  High Resolution EXecution）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98624.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：pinlist | Specifies the pins or pin groups for which the measurement is to be reported. A reply will be given for a pin only if the port to which it belongs is …

The binary data that are returned. The general format is:

Nn1n2...nNdata_stream

where the digit N defines the number of the digits ni (1 ≤i ≤N) that specify the length of data_stream in bytes.

The data stream itself is in principle a sequence of pairs each which consists of a repetition factor and a result value. The repetition factor indicates how often the following result value is measured before the result changes. A repetition factor of 1 is omitted.

The possible result values are:

L: Low

H: High

I: Intermediate

U: Unstable

An example is given below.

 |

### Example（取自子主题 Commands in alphabetical order › List of commands › HREX  -  High Resolution EXecution）

```
> HRIT HRES,40,0,42,0,800,(A)
> HREX? (a1,a2,b1)
< HREX (a1),#9000000020199LI199HI199LI199HI
< HREX (a2),#9000000020199LI199HI199LI199HI
> HRIT END
```

In this example, a rising edge occurs exactly in the middle of every cycle, and a falling edge at the end of every cycle for all pins. Note that the total number of results 4 * (199 + 1) equals the number of samples requested with HRIT RES.

### HRIT（取自子主题 Commands in alphabetical order › List of commands › HRIT  HRIT  -  High Resolution Interval of Time）

```
HRIT {HRES|SCOP}, {start_cyc}, {start_offs}, {stop_cyc), (stop_offs}, {samples), {(ref_port)}
HRIT END
```

### HRIT?（取自子主题 Commands in alphabetical order › List of commands › HRIT  HRIT  -  High Resolution Interval of Time）

```
HRIT? [(port)]
```

returns:

```
HRIT {task}, {param}[, start_offs] [, stop_cyc][, stop_offs][, samples][, (ref_port)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › HRIT  HRIT  -  High Resolution Interval of Time）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98627.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 2 列。
> 首行（上游原文）：HRES | Indicates the start of a high resolution measurement sequence.

### Example（取自子主题 Commands in alphabetical order › List of commands › HRIT  HRIT  -  High Resolution Interval of Time）

```
> HRIT HRES,40,0,42,0,800,(A)
> HRIT? (B)
< HRIT HRES,50,0,52,2,800,(B)
> HREX? (a1,a2,b1)
< HREX (a1),#9000000020199LI199HI199LI199HI
< HREX (a2),#9000000020199LI199HI199LI199HI
< HREX (b1),#9000000025159LI159HI199LI159HI159LI
> HRIT END
> HRIT?
< HRIT 0
```

In this example, there are two ports A and B that belong to the same sequencing group. A is the reference port. The period length for port A is 5 ns, that for port B is 4 ns. It is assumed that a rising edge occurs exactly in the middle of every cycle, and a falling edge at the end of every cycle for all pins.

The display interval is 2 cycles for port A, and 2 1/2 cycles for port B. This is reflected by the offset of 2 in the answer to the first query.

### HROL（取自子主题 Commands in alphabetical order › List of commands › HROL  HROL  -  High Resolution Option and Level）

```
HROL {PINS|LEVP}, {param1}, [param2], {(pinlist)}
```

### HROL?（取自子主题 Commands in alphabetical order › List of commands › HROL  HROL  -  High Resolution Option and Level）

```
HROL? {PINS|LEVP},{(pinlist)}
```

returns:

```
HROL {PINS|LEVP}, {param1}, [param2], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › HROL  HROL  -  High Resolution Option and Level）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98628.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 3 列。
> 首行（上游原文）：PINS | Indicates that the result resolution and possibly the High/Low definition for differential pins will be given.
> 表内引用（1 条，供检索）：`SPEC?`（raw: `02.06.02.02.225_SPEC__-__SPECification.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › HROL  HROL  -  High Resolution Option and Level）

```
> HRIT SCOP,135,0,175,0,800,(A)
> HROL PINS,1,,(HSClck)
> HROL LEVP,100,,(HSClck)
> HROL LEVP,1000,,(D0+,A0+,D0-,A0-)
> HREX? (HSClck,D0+,A0+,D0-,A0-)
> HROL LEVP,110,,(HSClck)
> HROL LEVP,1200,,(D0+,A0+,D0-,A0-)
> HREX? (HSClck,D0+,A0+,D0-,A0-)
> HRIT END
```

This example shows a measurement sequence for a scope measurement. First, the result resolution for the `HSClck` pin is set to 1. Then two measurements are taken. Before each measurement execution, the voltage levels are defined. After the second measurement, the measurement sequence is closed with HRIT END.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › HWTY  -  HardWare TYpe）

```
HWTY?
```

returns:

```
HWTY {machine}, {testhead}, {dut_if}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › HWTY  -  HardWare TYpe）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98636.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：machine | Returns PS

### Example（取自子主题 Commands in alphabetical order › List of commands › HWTY  -  HardWare TYpe）

```
> HWTY?
< HWTY VS,TH_4CC,SOC
```

### I2CA（取自子主题 Commands in alphabetical order › List of commands › I2CA  I2CA  -  I2CA bus）

```
I2CA {address}, {offset}, {#spec(data)}
```

### I2CA?（取自子主题 Commands in alphabetical order › List of commands › I2CA  I2CA  -  I2CA bus）

```

I2CA? {address}, {offset}, {size}
```

returns:

```
I2CA {address}, {offset}, {#spec(data)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › I2CA  I2CA  -  I2CA bus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98637.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：address | The mandatory parameter specifies the physical address of the EEPROM. For the X24C04 EEPROM, this would be 160, 168, or 172 (164 is reserved for the D…

### Syntax（取自子主题 Commands in alphabetical order › List of commands › INGV -  INsert Generate Vectors）

```
INGV{cmd_No}, {num_vec}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › INGV -  INsert Generate Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98639.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number before which the GENV instruction is to be inserted.

### Example（取自子主题 Commands in alphabetical order › List of commands › INGV -  INsert Generate Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,10,5,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,16,,,(@)
< ...
> TSTL "test_1",(@)
> INGV 3,11
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,10,5,,(@)
< SQPG 3,GENV,11,,,(@)
< SQPG 4,STOP,,,,(@)
< SQPG 5,STVA,32,,,(@)
< ...
```

This example inserts a GENV instruction for 11 vectors before command 2. Note that the memory type is SM, as in command 0, and that the address of command 5 has been increased.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › INSI -  INsert Instructions）

```
INSI {cmd_No}, {count}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › INSI -  INsert Instructions）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98640.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number before which instructions are to be inserted.

### Example（取自子主题 Commands in alphabetical order › List of commands › INSI -  INsert Instructions）

```
TSTL "test_1",(@)
INSI 358, 12
```

This example inserts 12 NOP sequencer instructions before command number 358.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › INST  -  INSTrument query）

```
INST? {pinlist}
```

 Returns:

```
INST {status}, {pinlist}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › INST  -  INSTrument query）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/355956.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：status | A list of instrument parameter values. See the example below for an incomplete list of possible parameters (not all cards support all parameters).

### Example（取自子主题 Commands in alphabetical order › List of commands › INST  -  INSTrument query）

```
>INST? (VCC0P9_SVR)
<INST "<instrumentStatus instrType=DPS128HC forceVoltage=320 forceVoltageHWLimitMin=-2500
forceVoltageHWLimitMax=7000 forceVoltageRangeMin=-2500 forceVoltageRangeMax=2500
compliance=na voltageClampHigh=na voltageClampLow=na voltageClampRangeMin=na
voltageClampRangeMax=na forceCurrent=na forceCurrentHWLimitMin=-1e+06
forceCurrentHWLimitMax=1e+06 forceCurrentRangeMin=na forceCurrentRangeMax=na
currentClampSource=750000 currentClampSink=750000 currentClampRangeMin=200000
currentClampRangeMax=1e+06 measureVoltageHWLimitMin=-2500 measureVoltageHWLimitMax=7000
measureVoltageRangeMin=na measureVoltageRangeMax=na measureCurrentHWLimitMin=-1e+06
measureCurrentHWLimitMax=1e+06 measureCurrentRangeMin=-1e+06 measureCurrentRangeMax=1e+06
voltageDropMaxForce=na voltageDropMaxReturn=na voltageClampFastLoad=na
voltageClampChannelOff=na slewV=na slewI=na filterV=OFF filterI=OFF measureFilter=na
forceState=ON powerAmpMode=NORMAL pbDcPower=na pbPulseEnergy=na measureType=na hvIoMode=na
samplerMode=na utiMode=na voltMoni=na badcMuxSetting=na comparatorType=na
comparatorOperationMode=na comparatorSelector=na comparatorLowValue=na
comparatorHighValue=na comparatorHysteresis=na comparatorHoldOff=na loadCap=1
currentLimiterState=na numberOfActiveChannels=1 stackLevel=1 referencePin=na />",(VCC0P9_SVR)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › JRST -  Jitter modulator ReseT）

```
JRST {(pin_list)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › JRST -  Jitter modulator ReseT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/119634.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pin_list | The pins for which the jitter modulator is to be reset. Typically, this must be done for all configured pins, so that you will usually specify @ for …

### Example（取自子主题 Commands in alphabetical order › List of commands › JRST -  Jitter modulator ReseT）

```
JRST (@)
```

This example resets the jitter modulator of all configured pins to its default state OFF.

### JSCF（取自子主题 Commands in alphabetical order › List of commands › JSCF  JSCF  -  Jitter Set ConFiguration）

```
JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}
```

### JSCF?（取自子主题 Commands in alphabetical order › List of commands › JSCF  JSCF  -  Jitter Set ConFiguration）

```
JSCF? {"jitter_set_name"|ALL|PRM}, {"property"|ALL}, {(pinlist)}
```

returns:

```
JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › JSCF  JSCF  -  Jitter Set ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116890.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：jitter_set_name | Specifies the name of a jitter set that must have been defined with JSDF.

### Example（取自子主题 Commands in alphabetical order › List of commands › JSCF  JSCF  -  Jitter Set ConFiguration）

```
> JSCF? "my_J_SET",ALL,(Pin1)
< JSCF "my_J_SET",MODE,CONT,(Pin1)
< JSCF "my_J_SET",WAVEFORM,"-100,-50,0,50,100,50,0,-50",(Pin1)
< JSCF "my_J_SET",PERIODFACTOR,25,(Pin1)
```

This example defines a simple sawtooth waveform with a peak-to-peak value of 200ps for a STDDIFF or STD pin.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › JSDF  JSDF  -  Jitter Set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117922.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：js_set_name | In the command, this is the name of a new jitter set. In the query, it is a name of an existing jitter set. If you omit this parameter in the quer…

### Example（取自子主题 Commands in alphabetical order › List of commands › JSDF  JSDF  -  Jitter Set DeFinition）

```
> JSDF   "js_set1"
> JSDF   "js_set2"
> JSDF   "js_set3"

> JSDF?
< JSDF   "js_set1"
< JSDF   "js_set2"
< JSDF   "js_set3"

```

### JSPR（取自子主题 Commands in alphabetical order › List of commands › JSPR  JSPR  -  Jitter Set PRimary set）

```
JSPR {"js_set_name"|""}
```

### JSPR?（取自子主题 Commands in alphabetical order › List of commands › JSPR  JSPR  -  Jitter Set PRimary set）

```
JSPR?
```

returns:

```
JSPR {"js_set_name"|""}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › JSPR  JSPR  -  Jitter Set PRimary set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117945.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：js_set_name | Specifies the name of an existing jitter set. Specify an empty string to inactivate the current primary set and thus to disable jitter injection.

### Example（取自子主题 Commands in alphabetical order › List of commands › JSPR  JSPR  -  Jitter Set PRimary set）

```
> JSPR   "js_set1"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › JSUD -  Jitter Set UnDefine）

```
JSUD {"js_set_name"|ALL}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › JSUD -  Jitter Set UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117930.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：js_set_name | Specifies the name of an existing jitter set.

### Example（取自子主题 Commands in alphabetical order › List of commands › JSUD -  Jitter Set UnDefine）

```
> JSUD   "js_set1"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › JSWF  -  Jitter Set WaveForm）

```
JSWF? {"jitter_set_name"}, {clock_resolution}, {(pinlist)}
```

returns:

```
JSWF {"jitter_set_name"}, {"offset_sequence"}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › JSWF  -  Jitter Set WaveForm）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/119599.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：jitter_set_name | Specifies the name of a jitter set that must have been defined with JSDF.

### Example 1（取自子主题 Commands in alphabetical order › List of commands › JSWF  -  Jitter Set WaveForm）

```
> jscf? "test",,(IO0)
< JSCF "test",WAVEFORM,SINUS,(IO0)
< JSCF "test",PERIOD,20,(IO0)
< JSCF "test",AMPLITUDE,100,(IO0)
> CLKR? EXACT,101,(@)
< CLKR 101,2.4,1.2,(@)
> jswf? "test",1200,(IO0)
< JSWF "test","0,29,47,47,29,0,-30,-48,-48,-30,-1,29,47,47,29,0,
  . . .
  -1,-30,-48,-48,-30,0,29,47,47,29,0,-30,-48,-48,-30",(IO0)
```

This example first queries the jitter waveform for pin `IO0`, and also the clock resolution for timing specification 101. It then calculates the offset sequence for this waveform and clock resolution. Note that CLKR? returns the clock resolution as nano seconds, but that JSWF? expects it to be specified as pico seconds. The reply is displayed in abbreviated form. The total length of the sequence is about 500 items.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › JSWF  -  Jitter Set WaveForm）

```
> JSCF? "test",WAVEFORM,(IO1)
< JSCF "test",WAVEFORM,"150,110,80,70,0"
> JSWF? "test",880,(IO1)
< JSWF "test","150,120,90,70,40",(IO1)
```

This example shows how JSWF? corrects the offset list if the second of two consecutive items is smaller than the first, and the maximum difference is exceeded.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › LBMD  -  LoopBack MoDe）

LBMD? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"|PRM}, {(pinlist)}

returns:

LBMD {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"|PRM}, {lpbk_mode}, {(pinlist)}

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118445.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. The maximum number is determined by the command WSUS, WSUS? - (Waveform Set…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › LBMD  -  LoopBack MoDe）

```
> LBMD? PRM,(@)
< LBMD 101,LOOP_OFF,,(pin1,pin2)
> SPRM 103,1,1,1
> LBMD? PRM,(@)
< LBMD 103,LOOP_I,2,(pin1)
< LBMD 103,LOOP_O,8,(pin2)
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › LBMD  -  LoopBack MoDe）

```
> LBMD? "lpbk_1",(@)
< LBMD "lpbk_1",LOOP_O,(pin1,pin2)
```

This example queries a wavetable.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › LBRT  -  LoopBack RouTing）

```
LBRT? {(pinlist)}
```

returns:

```
LBRT {(pin1)}, {(pin2)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118447.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：pinlist | Specifies the pins for which the partner pin is to be retrieved.

### Example（取自子主题 Commands in alphabetical order › List of commands › LBRT  -  LoopBack RouTing）

```
> LBRT? (@)
< LBRT (pin1),(pin2)
< LBRT (pin2),(pin1)
```

### LBUD（取自子主题 Commands in alphabetical order › List of commands › LBUD  LBUD  -  LaBel User Data）

```
LBUD {"UserDefinedKey"}, {"LabelName"}, [DELETE_AT_EDIT|PRESERVE_AT_EDIT][, (portlist)], #value
```

### LBUD?（取自子主题 Commands in alphabetical order › List of commands › LBUD  LBUD  -  LaBel User Data）

```
LBUD? [ALL|{"UserDefinedKey"}], [ALL|{"LabelName"}] [, (port)]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/151963.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：UserDefinedKey | A string to identify a specific category of user defined data, for example, MD5 checksum. The maximum length is 40 bytes.

### Example（取自子主题 Commands in alphabetical order › List of commands › LBUD  LBUD  -  LaBel User Data）

Attach user data example:

```
> LBUD "MD5Checksum", "Label1", DELETE_AT_EDIT, (port1), #214Checksum3457xx
```

This command attaches a MD5 checksum "214Checksum3457xx" to "Label1", at "port1". Attached data on demand will be deleted upon user editing the pattern.

Delete user data example:

```
> LBUD "MD5Checksum", "Label1", , (port1), #9000000000
```

This command detaches the MD5 checksum "214Checksum3457xx" from "Label1", at "port1".

Query user data example:

```
> LBUD? ALL,"LBL1",(port)
> LBUD? "MD5Checksum",ALL,(@@)
> LBUD? "MD5Checksum","LBL1",(port)
```

Each of these queries returns one matching result or multiple matching results. It can also return an empty result (instead of an error), if the given key does not exist.

### LSUS（取自子主题 Commands in alphabetical order › List of commands › LSUS  LSUS  -  Level Sets USed）

```
LSUS {level_set_no}
```

### LSUS?（取自子主题 Commands in alphabetical order › List of commands › LSUS  LSUS  -  Level Sets USed）

```
LSUS? [level_set_no]
```

returns:

```
LSUS {level_set_no}
```

or:

```
LSUS? [equation_set_no]
```

returns:

```
LSUS {level_set_no}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › LSUS  LSUS  -  Level Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98641.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：level_set_no | Level Set Number. This is the highest number currently allocated to a level set or the highest number of set you want to load. The number you typ…
> 表内引用（1 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › LSUS  LSUS  -  Level Sets USed）

```
LSUS 4
```

This example defines a maximum of 4 level sets.

### LSUX（取自子主题 Commands in alphabetical order › List of commands › LSUX  LSUX  -  Level Sets Used eXtended）

```
LSUX {level_set_no|SWAP|NONE}
```

### LSUX?（取自子主题 Commands in alphabetical order › List of commands › LSUX  LSUX  -  Level Sets Used eXtended）

```
LSUX?
```

returns:

```
LSUX {level_set_no}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › LSUX  LSUX  -  Level Sets Used eXtended）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98642.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：level_set_no | Level Set Number. If the number is smaller than the current value of LSUS then LSUX is set to this value. Otherwise it is set to the current valu…

### Example（取自子主题 Commands in alphabetical order › List of commands › LSUX  LSUX  -  Level Sets Used eXtended）

```
LSUX 4
```

This example defines a maximum of 4 level sets.

### LTDE（取自子主题 Commands in alphabetical order › List of commands › LTDE  LTDE  -  Load Test Data Entity）

```
LTDE "<tde_name>"
```

### LTDE?（取自子主题 Commands in alphabetical order › List of commands › LTDE  LTDE  -  Load Test Data Entity）

```
LTDE?
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › LTDE  LTDE  -  Load Test Data Entity）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124452.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：tde_name | The name of the protocol test data entity (TDE) file. This is the file name including the extension that specifies the type of the TDE. The file must…
> 表内引用（1 条，供检索）：`PTDE`（raw: `02.06.02.02.200_PTDE__PTDE__-__Path_for_Test_Data_Entities.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › LTDE  LTDE  -  Load Test Data Entity）

```
LTDE "test.prot_asg"
LTDE?
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › MCNT  -  Match loop CouNT）

```
MCNT? {(pinlist)}
```

returns:

```
MCNT {match_count},{(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › MCNT  -  Match loop CouNT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98645.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：match_count | Specifies the number of the pass after which the match condition was met.

### Example（取自子主题 Commands in alphabetical order › List of commands › MCNT  -  Match loop CouNT）

```
> MCNT? (CP)
< MCNT 16 (CP)
```

In this example, a match was obtained after 16 passes.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › MEAR  retrieve MEAsurement Results）

```
MEAR{type}, [no_of_samples], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › MEAR  retrieve MEAsurement Results）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98647.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：type | Data type to be measured. The following specifiers can be set: VMUM: Per pin parallel value retrieval from PPMU measurement (successive approximation). V…

### Example（取自子主题 Commands in alphabetical order › List of commands › MEAR  retrieve MEAsurement Results）

```
> PSFC ALL
> MEAR VAL,35,(p1,p2)
> PQFC 1
> PMUR? VAL,(p1,p2)
< PMUR P,,2,(p1)
< PMUR F,-2100,,(p2)
> PQFC 2
> PMUR? VAL,(p1,p2)
< PMUR P,,2.3,(p1)
< PMUR F,-2200,,(p2)
```

This example triggers a value measurement with 35 samples for p1 and p2 on all sites. It then retrieves the average of the samples for every pin separately for each site with PMUR?.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › MEAS -  execute a MEASurement set）

```
MEAS {id_dc}, {id_mset}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › MEAS -  execute a MEASurement set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98648.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：id_dc | The DC set identification number to be executed.

### Example（取自子主题 Commands in alphabetical order › List of commands › MEAS -  execute a MEASurement set）

```
MEAS 1,2
```

This example executes the measurement set 2 of the DC set 1.

See also an example in `MSET, MSET? - (definition of Measurement SET)`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md`）.

### MERL（取自子主题 Commands in alphabetical order › List of commands › MERL  MERL  -  Message ERror Limits）

```
MERL [error_limit], [message_limit]
```

### MERL?（取自子主题 Commands in alphabetical order › List of commands › MERL  MERL  -  Message ERror Limits）

```
MERL?
```

returns:

```
MERL [error_limit], [message_limit]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › MERL  MERL  -  Message ERror Limits）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98649.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：error_limit | The maximum number of errors that will be logged. An integer in the range 1 to 30000.Default value is 10.

### Example（取自子主题 Commands in alphabetical order › List of commands › MERL  MERL  -  Message ERror Limits）

MERL 30,30

This example sets both the error and the message limits to 30.

### MSCF（取自子主题 Commands in alphabetical order › List of commands › MSCF  MSCF  -  Modulation Set ConFiguration）

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### MSCF?（取自子主题 Commands in alphabetical order › List of commands › MSCF  MSCF  -  Modulation Set ConFiguration）

```
MSCF? {"modulation_set_name"|ALL}, {"property"|ALL}
```

returns:

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › MSCF  MSCF  -  Modulation Set ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143671.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：modulation_set_name | Specifies the name of a modulation set that must have been defined with MSDF.

### Example（取自子主题 Commands in alphabetical order › List of commands › MSCF  MSCF  -  Modulation Set ConFiguration）

```
> MSCF? "mod1",ALL
< MSCF "mod1",SHAPE,SINE
< MSCF "mod1",PERIOD,250
< MSCF "mod1",PHASE,180
< MSCF "mod1",AMPLITUDE,305
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › MSDF  MSDF  -  Modulation Set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143675.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ms_set_name | In the command, this is the name of a new modulation set. In the query, it is a name of an existing modulation set. If you omit this parameter in …

### Example（取自子主题 Commands in alphabetical order › List of commands › MSDF  MSDF  -  Modulation Set DeFinition）

```
> MSDF   "ms_set1",TIM
> MSDF   "ms_set2",TIM
> MSDF   "ms_set3",TIM

> MSDF?
< MSDF   "ms_set1",TIM
< MSDF   "ms_set2",TIM
< MSDF   "ms_set3",TIM

```

### MSET（取自子主题 Commands in alphabetical order › List of commands › MSET  MSET  -  definition of Measurement SET）

```
MSET {`id_dc`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_dc`）}, DC, {`id_mset`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_mset`）}, {`glob_act`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_glob_act`）}, `[par1`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_par1`）], `[par2`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_par2`）], {(`pinlist`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_pinlist`）)}
MSET {`id_dc`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_dc`）}, DC, {`id_mset`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_mset`）}, {`act`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_act`）}, {`id_act`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_act`）}, {`par2`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_par2`）}, {(`pinlist`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_pinlist`）)}
MSET {`id_dc`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_dc`）}, DC, {`id_mset`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_mset`）}, `VMUM`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__e_VMUM`）, {`id_act`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_act`）}, {`par2`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_par2`）},{`numOfSamples`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_numOfSamples`）},ADC`,[waveformSize`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_waveformSize`）]`,[samplePeriod`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_samplePeriod`）]{(`pinlist`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_pinlist`）)}
```

### MSET?（取自子主题 Commands in alphabetical order › List of commands › MSET  MSET  -  definition of Measurement SET）

```
MSET? {id_dc|ALL}, DC, {id_mset|ALL}, {(pinlist)}
```

returns

```
MSET {id_dc}, DC, {id_mset}, {act}, {par1}, {par2}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98657.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：53 行 × 3 列。
> 首行（上游原文）：id_dc | The DC set identification number. The number is an integer in the range 1 to 256. A DC set consists of up to 10 measurement sets. For the query, you can…
> 表内引用（2 条，供检索）：`1)`（raw: `#fntarg_1`） · `MEAS`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10.02_Sequencer_instructions.md#_99880__row_MEAS`）

### Example（取自子主题 Commands in alphabetical order › List of commands › MSET  MSET  -  definition of Measurement SET）

Setting up PPMUs:

```
MSET 1,DC,1,LEN,6,,(@)
MSET 1,DC,1,WAIT,,0,(@)
MSET 1,DC,1,ACT,,,(@)
MSET 1,DC,1,SEL,0,CURR,(p1)
MSET 1,DC,1,SEL,0,VOLT,(p2)
MSET 1,DC,1,IRNG,1,IRA,(p1)
MSET 1,DC,1,IRNG,1,90,(p2)
MSET 1,DC,1,UFOR,2,500,(p1)
MSET 1,DC,1,IFOR,2,-40,(p2)
MSET 1,DC,1,PMUL,3,-5,(p1)
MSET 1,DC,1,PMUL,3,3000,(p2)
MSET 1,DC,1,PMUH,4,5,(p1)
MSET 1,DC,1,PMUH,4,3000,(p2)
MSET 1,DC,1,ACTI,5,,(p1,p2)
```

On PS5000:

```
MSET? 3,DC,1,(dig1)
MSET 3,DC,1,LEN,7,,(@)
MSET 3,DC,1,WAIT,,0,(@)
MSET 3,DC,1,SWAIT,,0,(@)
MSET 3,DC,1,ACT,,,(dig1)
MSET 3,DC,1,SEL,0,CURR,(dig1)
MSET 3,DC,1,IRNG,1,10000,(dig1)
MSET 3,DC,1,UFOR,2,3300,(dig1)
MSET 3,DC,1,PMUL,3,-10,(dig1)
MSET 3,DC,1,PMUH,4,30,(dig1)
MSET 3,DC,1,ACTI,5,,(dig1)
MSET 3,DC,1,SYNC,6,,(dig1)
```

Setting up the relays:

```
MSET 1,DC,2,LEN,2,,(@)
MSET 1,DC,2,WAIT,,1.3,(@)
MSET 1,DC,2,ACT,,,(@)
MSET 1,DC,2,OPM,0,ON,(p1)
MSET 1,DC,2,PPMU,0,ON,(p2)
MSET 1,DC,2,ACTI,1,,(p1,p2)
```

Setting up the measurement mode:

```
MSET 1,DC,3,LEN,1,,(@)
MSET 1,DC,3,WAIT,,0,(@)
MSET 1,DC,3,ACT,,,(@)
MSET 1,DC,3,PMUM,0,I,(p1)
MSET 1,DC,3,PMUM,0,H,(p2)
```

This example illustrates the internal structure of a measurement set as well as the requirement to define different measurement sets for different tasks. Note that no ACTI action is required (or even permitted) for measurement set 3 which contains only the PMUM action.

To execute this example, use the MEAS command as shown below:

```
MEAS 1,1
MEAS 1,2
MEAS 1,3
```

These commands sequentially execute measurement sets 1, 2 and 3 of DC set 1.

To retrieve the result of this measurement, use the `PMUR?`（raw: `02.06.02.02.179_PMUR___retrieve_PPMU_result.md`） command as shown below:

```
PMUR? GPF,(@)
```

This command retrieves the global pass/fail result of all pins.

Defining a DC set for value measurement

```
MSET 2,DC,1,VMUM,0,I,1,ADC,4000,0.0004,(p1)
```

In this example, 4000 measurements will be taken with the sampling period 400 us on the pin p1.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › MVCU -  Modify Vector variable Configuration Usage）

```
MVCU {label name}, {VVC name}, {vector offset}, {Init Discard Frames}, {Number Of Frames}, {VarNameDef}, {InitStaticData}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99062.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：label name | Name of the label for which usage is to be modified.
> 表内引用（1 条，供检索）：`DVVC, DVVC? - (Define Vector Variable Configuration)`（raw: `02.06.02.02.95_DVVC__DVVC__-__Define_Vector_Variable_Configuration.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › MVCU -  Modify Vector variable Configuration Usage）

The following example modifies the usage to change vector variable names. This usage is defined for the label "src" using VVC "AC97" at offset 0.

VVC "AC97" looks like:

```
ATTR DIGDATA
  VARIABLES LEFT,RIGHT
  PINS ser_in
     SOURCE_DATA_TEMPLATE LEFT[0-19]; RIGHT[0-19]
     MAPPING
         0 low
         1 high
>MVCU"src_ramp","AC97",0,0,1024,"LEFT=Sine,
 RIGHT=Ramp",TRUE
>DVCU? ALL,ALL,ALL
<DVCU "src_ramp","AC97",0,0,1024,"LEFT=Sine,
 RIGHT=Ramp",TRUE
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › MVVA -  Modify Vector VAriable）

```
MVVA {"name"}, {type}, {"vector_label"}, {xfer_mode}, [device_cycle], [start_vector_nr], [capt_label], [init_discard], [nr_vec_per_frame], [nr_vec_per_sample], [nr_vector_interdisc], [nr_of_frames], [nr_frame_interdisc], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › MVVA -  Modify Vector VAriable）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99063.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 2 列。
> 首行（上游原文）：name | Name of a vector variable.

### Example（取自子主题 Commands in alphabetical order › List of commands › MVVA -  Modify Vector VAriable）

```
> DVVA "vec_var",DIGCAPT,"test_capt",PARA,,,,0,1,1,0,1,0,(OUT_1)
> MVVA "vec_var",DIGCAPT,"test_capt",SERI,,,,,,,,,,(OUT_1)
> DVVA? "test_capt"
< DVVA "vecvar",DIGCAPT,"test_capt",SERI,,,,0,1,1,0,1,0,(OUT_1)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › NIFE  NIFE  -  Number of Independent Fast Error）

```
NIFE {number}
```

```
NIFE?
```

returns:

```
NIFE {number}
```

`NIFE?` can be issued only if the number of independent Fast Sync ports already has been set by command `NIFE {number}`. Otherwise, the error message Failed to execute firmware command: NIFE? will be shown.

  Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/150830.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：number | Specifies the maximum number of independent Fast Sync ports. It can be [1,...,8].

### Example（取自子主题 Commands in alphabetical order › List of commands › NIFE  NIFE  -  Number of Independent Fast Error）

```
>SQST OFF
>NIFE 2
>STME FAST,
>STME ON,
```

This example configures the Fast Sync feature, and sets two independent Fast Sync ports on each test processor.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › NODV  -  Number Of Displayable Vectors）

```
NODV?
```

returns:

```
NODV {num_vec}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › NODV  -  Number Of Displayable Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98663.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：num_vec | returns the number of active vectors.

### Example（取自子主题 Commands in alphabetical order › List of commands › NODV  -  Number Of Displayable Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
> TSTL "test_1",(@)
> NODV?
< NODV 15
```

### NOOP（取自子主题 Commands in alphabetical order › List of commands › NOOP  NOOP  -  NO OPeration）

```
NOOP["string_1"|no_1],["string_2"|no_2],["string_3"|no_3],["string_4"|no_4]
```

### NOOP?（取自子主题 Commands in alphabetical order › List of commands › NOOP  NOOP  -  NO OPeration）

```
NOOP?["string_1"|no_1],["string_2"|no_2],["string_3"|no_3],["string_4"|no_4]
```

returns:

```
NOOP["string_1"|no_1],["string_2"|no_2],["string_3"|no_3],["string_4"|no_4]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › NOOP  NOOP  -  NO OPeration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98664.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：string_1 to string_4 | A string of up to 128 characters

### Example（取自子主题 Commands in alphabetical order › List of commands › NOOP  NOOP  -  NO OPeration）

```
NOOP "TF1",,,
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › OUTS  -  OUTput Search）

```
OUTS? {vector_no_1}, [vector_no_2], {vector_type}, {level_type}, {(pinlist)} [, (port)]
```

returns:

```
OUTS {cycle_no}, {output_level}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › OUTS  -  OUTput Search）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98677.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：vector_no_1 | This parameter is an absolute vector number or a range specifier depending on whether DPTH, SNGL, or RNG has been selected.

### PACT（取自子主题 Commands in alphabetical order › List of commands › PACT  PACT  -  Parallel ACTivities control）

PACT {control}, {site|ALL}

PACT {"site_string"}

### PACT?（取自子主题 Commands in alphabetical order › List of commands › PACT  PACT  -  Parallel ACTivities control）

```
PACT?
```

returns

```
PACT {control}, {site}
```

Or:

```
PACT?STR
```

returns

```
PACT {"site_string"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PACT  PACT  -  Parallel ACTivities control）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98678.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：control | The control parameter is:

### Example（取自子主题 Commands in alphabetical order › List of commands › PACT  PACT  -  Parallel ACTivities control）

```
> PACT ACTIVE, 1
> PACT MASKED, 2
> PACT MASKED, 3
```

This example masks site 2 and site 3, and makes site 1 active.

```
> PACT?
< PACT ACTIVE,1
< PACT MASKED,2
< PACT MASKED,3
> PACT? STR
< PACT "100"
```

This example shows the impact of the optional STR parameter for the query.

### PADS（取自子主题 Commands in alphabetical order › List of commands › PADS  PADS  -  Pin Attributes Definition String）

```
PADS [mode], {definition_string}, [drv_adj], [rec_adj], {(pinlist)}
```

### PADS?（取自子主题 Commands in alphabetical order › List of commands › PADS  PADS  -  Pin Attributes Definition String）

```
PADS? [mode], {(pinlist)}
```

returns:

```
PADS [mode], {definition_string}, [drv_adj], [rec_adj], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PADS  PADS  -  Pin Attributes Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98679.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：mode | Currently not used.

### Example（取自子主题 Commands in alphabetical order › List of commands › PADS  PADS  -  Pin Attributes Definition String）

```
> PADS ,"d1:0.1 d2:0.2 d3:0.3 d4:0.1 d5:0.2 d6:0.3 d7:0.1 d8:0.2",2,,(clk)

> PADS? ,(@)
< PADS ,"d1:0.1 d2:0.2 d3:0.3 d4:0.1 r1:0.1 r2:0.2 r3:0.3 r4:0.1",,-1,(io)
< PADS ,"d1:0.1 d2:0.2 d3:0.3 d4:0.1 d5:0.2 d6:0.3 d7:0.1 d8:0.2",2,,(clk)
```

### PALS（取自子主题 Commands in alphabetical order › List of commands › PALS  PALS  -  Pin ALlocation for multiple Sites）

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

### PALS?（取自子主题 Commands in alphabetical order › List of commands › PALS  PALS  -  Pin ALlocation for multiple Sites）

```
PALS? {site}, {(pinlist)}
```

returns:

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PALS  PALS  -  Pin ALlocation for multiple Sites）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98680.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：site | The site parameter is an integer that defines the number of the site where the channels are to be defined. The integer must be greater than 1 (channels f…
> 表内引用（4 条，供检索）：`DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） · `DFPN, DFPN? - (DeFine Pin Name)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） · `DFUT, DFUT? - (DeFine UTility line)`（raw: `02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md`） · `DDIC`（raw: `02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md`）

### Examples（取自子主题 Commands in alphabetical order › List of commands › PALS  PALS  -  Pin ALlocation for multiple Sites）

```
PALS 2,10201,,(Clock)
PALS 2,10202,,(D0)
```

The above example allocates the Clock pin for site 2 to channel 10201 and allocates pin D0 for site 2 to channel 10202.

```
PALS 2,(10101, 10102),,(dc1)
```

This example defines a master/slave configuration for DC Scale channels. The first channel is the master.

```
DDIC CONN, (104GO, 105GI)
DDIC CONN, (105GO, 107GI)
PALS 2,(10403, 10404, 10501, 10502, 10503, 10504, 10701, 10702),,(dc1)
```

This example defines a master/slave configuration for DC Scale UHC4 channels across boards. The first channel is the master.

```
DFAN "MCE231,2,i","",(av8_bbrx_b+)
DFAN "MCE231,6,i","",(av8_bbrx_b-)
PALS 2,"MCE231,1,i",,(av8_bbrx_b+)
PALS 3,"MCE231,3,i",,(av8_bbrx_b+)
PALS 4,"MCE231,4,i",,(av8_bbrx_b+)
PALS 2,"MCE231,5,i",,(av8_bbrx_b-)
PALS 3,"MCE231,7,i",,(av8_bbrx_b-)
PALS 4,"MCE231,8,i",,(av8_bbrx_b-)
```

This example defines a pair of differential pins av8_bbrx_b+ and av8_bbrx_b- using the MCE card in 4 sites.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PASS  -  PASS or fail result）

```
PASS? {(pin_list)}
```

or

```
PASS? {(port_list)}
```

returns:

```
PASS {res_flag}, {(pin_list)}
```

or

```
PASS {res_flag}, {(port)}
```

respectively.

Note port_list mode returns the pass or fail result per port. This is different than the case when using pin_list mode.

To report the last test result per individual pin , the PPIN command is used.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PASS  -  PASS or fail result）

```
PASS?PPIN,{(pins)}
```

returns

```
PASS PPIN,{res_flag}, {(pin}
```

Note The result (pass or fail) is returned for each pin specified in pins individually.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PASS  -  PASS or fail result）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98681.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：pin_list | The last test result is provided for the pins specified in pin_list. If more than one pin list is included, the names must be separated by a comma. N…
> 表内引用（2 条，供检索）：`MEAS`（raw: `02.06.02.02.160_MEAS_-__execute_a_MEASurement_set.md`） · `SQPG`（raw: `02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md`）

Application

Test results, see `Test Result Commands`（raw: `02.06.11_Test_Result_Commands.md`） and `Multi-Port Testing`（raw: `../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.01.02_General_Overview_of_Multi-Port_Testing__Cover.md`）.

### Example（取自子主题 Commands in alphabetical order › List of commands › PASS  -  PASS or fail result）

After a functional test has been performed, sending PASS? returns one result for the whole test.

```
PASS? (@)
```

returns:

```
PASS P, (@)
```

or

```
PASS F, (@)
```

for a passed or a failed test result respectively.

### PCLK（取自子主题 Commands in alphabetical order › List of commands › PCLK  PCLK  -  Pin CLocK）

Fixed timing:

```
PCLK{waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### PCLK?（取自子主题 Commands in alphabetical order › List of commands › PCLK  PCLK  -  Pin CLocK）

Fixed timing:

```
PCLK?{waveform_set},{timing_set},{(pinlist)} [,query_mode]
```

returns:

```
PCLK {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK? {specset_id|"multi-port_spec"}, {timing_set}, {(pinlist|portlist)} [,query_mode]
```

returns:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PCLK  PCLK  -  Pin CLocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98682.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › PCLK  PCLK  -  Pin CLocK）

```
PCLK 101,1,20,(@)
```

This example sets the test system period for specification 101 to 20 ns.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › PCLK  PCLK  -  Pin CLocK）

```
PCLK 101,1,40,(S1)
```

This example sets the test system period of pin S1 for specification 101 to 40 ns.

The `VCLK?`（raw: `02.06.02.02.319_VCLK__-__Verify_CLocK.md`） query checks whether a PCLK command with the specified parameter values was accepted with or without auto-correction.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PDIV  -  Period DIVider）

```
PDIV? {specset_id|"multi-port_spec"|"wavetbl"} [,spec_type][,(pinlist)]
```

returns:

```
PDIV {specset_id|"multi-port_spec"}, {period_div}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PDIV  -  Period DIVider）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98684.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：specset_id | Identifier of a timing specification, which is derived as follows: 100 * equation_set_no + specset_no

### Example（取自子主题 Commands in alphabetical order › List of commands › PDIV  -  Period DIVider）

```
> PDIV? "fast",WFT,(I1)
< PDIV "fast",WFT,6,(I1)
```

This example queries the implicit period divider of the fast pin I1 in the wavetable `fast`. The factor is 6.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? [PRLT,] {spec},[averages,] {(pinlist)}
```

returns:

```
PDMM {spec},, [ident], {result}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98685.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：PRLT | The extra parameter controls how the measurement is performed.The value of the parameter can be: PRLT
> 表内引用（4 条，供检索）：`PRLT?`（raw: `02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.md`） · `DC Scale XPS256 card`（raw: `../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md`） · `DFPS, DFPS? - (DeFine Power Supply)`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） · `DFPN, DFPN? - (DeFine Pin Name)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）

### Example 1: Test of the site in query focus（取自子主题 Commands in alphabetical order › List of commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? Fo_Se, (@)
```

returns:

```
PDMM Fo_Se,,POS,P,(Vee)
PDMM Fo_Se,,NEG,P,(Vee)
```

This example checks that the force/sense connections on the DUT board are correctly wired for positive and negative lines. For the pin Vee the master channel and the slave channel show a pass for both lines.

### Example 2: Test of all active sites（取自子主题 Commands in alphabetical order › List of commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? PRLT, Fo_Se, (Vcc,Vee)
PRLT? ALL
```

returns:

```
PDMM Fo_Se,,POS,P,(Vcc)
PDMM Fo_Se,,NEG,P,(Vcc)
PDMM Fo_Se,,POS,P,(Vee)
PDMM Fo_Se,,NEG,P,(Vee)

PRLT ALL,"PF0P"
```

The returned pass/fail result of PRLT? presumes that four sites are defined and sites 1, 2, and 4 are active. Sites 1 and 4 have passed the test. Site 2 shows the result for an open force to sense connection.

### Example 3: Averaging（取自子主题 Commands in alphabetical order › List of commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? Fo_Se, 10, (@)
```

returns:

```
PDMM Fo_Se,,POS,P,(Vee)
PDMM Fo_Se,,NEG,P,(Vee)
```

The returned go/no-go results are built from the average of ten measurements to improve the stability of the measurement in noisy environments.

### Example 4: Ganging（取自子主题 Commands in alphabetical order › List of commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? Ma_Sl,32,(@)
```

  returns:

```
PDMM Ma_Sl,,POS,P,(Vee1)
PDMM Ma_Sl,,POS,P,(Vee2)

```

This example checks the master and slave connections for ganged pins with an average of 32 measurements to improve the stability of the measurements in noisy environments.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PFND  -  Pin FiND）

```
PFND? [group_type,] {(pin)}
```

returns:

```
PFND {group_type}, {(list)}, {(pin)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PFND  -  Pin FiND）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98686.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：group_type | The group type can be PRT (for "port") or DIFF (for "differential pair"). PRT is the default.

### Example（取自子主题 Commands in alphabetical order › List of commands › PFND  -  Pin FiND）

```
> PFND? (I/O1_1)
< PFND PRT,(port_1,port_1.CP_1),(I/O1_1)
> PFND? DIFF,(P+)
< PFND DIFF,(P+,P-),(P+)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PMUR   retrieve PPMU result）

```
PMUR?{type}, [mode,] {(pinlist)}
```

returns

```
PMUR {judge}, [voltage], [current], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PMUR   retrieve PPMU result）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98687.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：type | Data type to be retrieved. The following specifiers can be set: VMUM: Returns the measurement value from the PPMU measurement (successive approximation) …

Target pin or pins to retrieve result

   | Note For the VAL type, either voltage or current will be returned depending on the measurement mode (I-force V-measure or V-force I-measure).

### Example 1（取自子主题 Commands in alphabetical order › List of commands › PMUR   retrieve PPMU result）

```
> PMUR? VAL,(p1,p2)
< PMUR P,,2,(p1)
< PMUR F,-2100,,(p2)
```

This example retrieves the measurement value of "p1" and "p2" for the site that has the query focus.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › PMUR   retrieve PPMU result）

```
> PMUR? GPF,(@)
< PMUR P,,,()
```

In this example, PMUR? returns the global pass/fail result for all tested pins of the site that has the query focus.

### PQFC（取自子主题 Commands in alphabetical order › List of commands › PQFC  PQFC  -  Parallel Query FoCus）

```
PQFC {site}
```

### PQFC?（取自子主题 Commands in alphabetical order › List of commands › PQFC  PQFC  -  Parallel Query FoCus）

```
PQFC?
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PQFC  PQFC  -  Parallel Query FoCus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98688.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：site | The site parameter is single integer representing the number of the site that has or shall have the query focus.

### Example（取自子主题 Commands in alphabetical order › List of commands › PQFC  PQFC  -  Parallel Query FoCus）

```
PQFC 2
```

This example sets the query focus to site 2.

### PRCF（取自子主题 Commands in alphabetical order › List of commands › PRCF  PRCF  -  Pseudo Random bit sequence ConFiguration）

```
PRCF {"PRBS_set_name"|PRM}, {property}, {"property_value"}, {(pinlist)}
```

### PRCF?（取自子主题 Commands in alphabetical order › List of commands › PRCF  PRCF  -  Pseudo Random bit sequence ConFiguration）

```
PRCF? {"PRBS_set_name"|ALL|PRM}, {property|ALL}, {(pinlist)}
```

returns:

```
PRCF {"PRBS_set_name"}, {property}, {"property_value"}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PRCF  PRCF  -  Pseudo Random bit sequence ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118218.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：PRBS_set_name | Specifies the name of a PRBS set that must have been defined with PRDF.

### Example（取自子主题 Commands in alphabetical order › List of commands › PRCF  PRCF  -  Pseudo Random bit sequence ConFiguration）

```
> PRCF? "PRBS_1",ALL,(Pin1)
< PRCF "PRBS_1",POLYNOMIAL,"101",(Pin1)
< PRCF "PRBS_1",SEED,"100",(Pin1)
```

This example defines 1 + x1 + x3 as the connection polynomial, and 100 as the initial segment for Pin1. This is the example which is also used in `Overview of pseudo random bit sequences`（raw: `02.06.17.01_Overview_of_pseudo_random_bit_sequences.md`）.

### PRDF（取自子主题 Commands in alphabetical order › List of commands › PRDF  PRDF  -  PRBS set DeFinition）

```
PRDF {"prbs_set_name"} [, "mode_context"]
```

### PRDF?（取自子主题 Commands in alphabetical order › List of commands › PRDF  PRDF  -  PRBS set DeFinition）

```
PRDF? ["prbs_set_name"]
```

returns:

```
PRDF {"prbs_set_name"} [, "mode_context"]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PRDF  PRDF  -  PRBS set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118422.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：prbs_set_name | In the command, this is the name of a new PRBS set. In the query, it is a name of an existing PRBS set. If you omit this parameter in the query,…

### Example（取自子主题 Commands in alphabetical order › List of commands › PRDF  PRDF  -  PRBS set DeFinition）

```
> PRDF   "prbs_set1"
> PRDF   "prbs_set2"
> PRDF   "prbs_set3"
```

```
> PRDF?
< PRDF   "prbs_set1"
< PRDF   "prbs_set2"
< PRDF   "prbs_set3"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PRLT  -  request Parallel ResuLTs）

```
PRLT? ["exec_context",] {site}
```

returns:

```
PRLT {site}, {"result"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PRLT  -  request Parallel ResuLTs）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98689.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts.
> 表内引用（1 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › PRLT  -  request Parallel ResuLTs）

```
PRLT? ALL
```

returns:

```
PRLT ALL, "PF0"
```

In this example, site 1 passed the last test, site 2 failed it, and site 3 was masked during the test.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PRMD  -  PRBS MoDe）

```
PRMD? {wvf_set|"wavetable_name"|specset_id|"multi_port_spec"|PRM}, {(pinlist)}
```

returns:

```
PRMD {wvf_set|"wavetable_name"|specset_id|"multi_port_spec"|PRM}, {prbs_mode}, [x_mode], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PRMD  -  PRBS MoDe）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118425.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. The maximum number is determined by the command WSUS, WSUS? - (Waveform Set…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › PRMD  -  PRBS MoDe）

```
> PRMD? PRM,(@)
< PRMD 101,PRBS_OFF,,(pin1,pin2)
> SPRM 103,1,1,1
> PRMD? PRM,(@)
< PRMD 103,PRBS_I,2,(pin1)
< PRMD 103,PRBS_O,8,(pin2)
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › PRMD  -  PRBS MoDe）

```
> PRMD? "prbs_2",(@)
< PRMD "prbs_2",PRBS_O,4,(pin1,pin2)
```

This example queries a wavetable.

### PRPR（取自子主题 Commands in alphabetical order › List of commands › PRPR  PRPR  -  PRBS PRimary set）

PRPR {"prbs_set_name"|DEFAULT}

### PRPR?（取自子主题 Commands in alphabetical order › List of commands › PRPR  PRPR  -  PRBS PRimary set）

PRPR?

returns:

```
PRPR {"prbs_set_name"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PRPR  PRPR  -  PRBS PRimary set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118421.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：prbs_set_name | Specifies the name of an existing PRBS set. If you specify "", the defaults will be restored.

### Example（取自子主题 Commands in alphabetical order › List of commands › PRPR  PRPR  -  PRBS PRimary set）

```
> PRPR   "PRBS_set"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PRUD -  PRBS set UnDefine）

PRUD {"prbs_set_name"|ALL}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PRUD -  PRBS set UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118424.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：prbs_set_name | Specifies the name of an existing PRBS set.

### Example（取自子主题 Commands in alphabetical order › List of commands › PRUD -  PRBS set UnDefine）

```
> PRUD   "prbs_set1"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PSAS  -  Power Supply Accumulated Status）

```
PSAS? [msMode ,] {mask}, {(pinlist)}
```

returns

```
PSAS {status}, {(pinlist)}

```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98691.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：20 行 × 5 列，含嵌套表。
> 首行（上游原文）：msMode | The extra parameter controls how the return value is created.The value of the parameter can be PQFC: PQFC specified: The current query focus is respect…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98691.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 3 列。
> 首行（上游原文）：Bit 0 (LSB): | Constant voltage
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98691.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：18 行 × 6 列。
> 首行（上游原文）：Bit | Flag | DPS128DPS64 | UHC4T | XPS256

### Description（取自子主题 Commands in alphabetical order › List of commands › PSAS  -  Power Supply Accumulated Status）

For the following examples (1 to 4), the assumed binary value of the status of the UHC4 pin Vcc is 10000110 (Voltage drop return, Unregulated, Constant Current).

### Example 1（取自子主题 Commands in alphabetical order › List of commands › PSAS  -  Power Supply Accumulated Status）

To get all flags:

```
PSAS? ALL,(Vcc)
```

returns

```
PSAS #86,(Vcc)
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › PSAS  -  Power Supply Accumulated Status）

To check if Unregulated (bit 2) is set:

```
PSAS? 4,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 3（取自子主题 Commands in alphabetical order › List of commands › PSAS  -  Power Supply Accumulated Status）

To check if Constant Current (bit 1) or Overpower (bit 4) is set:

```
PSAS? 18,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 4（取自子主题 Commands in alphabetical order › List of commands › PSAS  -  Power Supply Accumulated Status）

To check if Voltage Drop Force (bit 6) or DUT Board Disconnect (bit 8) is set:

```
PSAS? 320,(Vcc)
```

returns

```
PSAS P,(Vcc)
```

### Example 5（取自子主题 Commands in alphabetical order › List of commands › PSAS  -  Power Supply Accumulated Status）

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 2,(Vee)
```

This example for device pin Vee shows the DPS is working in constant current mode.

### Example 6（取自子主题 Commands in alphabetical order › List of commands › PSAS  -  Power Supply Accumulated Status）

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 64,(Vee)
```

This example for device pin Vee shows the DPS has hit the voltage drop force threshold.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PSEE -  Power Supply External trigger measurement Execute）

```
PSEE [setnr], [current_range], [samples], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSEE -  Power Supply External trigger measurement Execute）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98696.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：setnr | The set number of the external trigger measurement. (The range is 1 to 256). When this parameter is specified the corresponding set must have already be…
> 表内引用（1 条，供检索）：`DPSE`（raw: `02.06.02.02.85_DPSE__DPSE__-__Define_Power_Supply_External_trigger_measurement.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › PSEE -  Power Supply External trigger measurement Execute）

```
DFPS 11,pos,(Vcc)
DFPS 12,pos,(Vdd)
DPSE 1,(@),#10          <- Delete set 1
DPSE 1,(Vcc),#150,1,2   <- Vcc min=1A, max=2A
DPSE 1,(Vdd),#150,2,3   <- Vdd min=2A, max=3A
PSST ON      <- Measurement requires connect state
PSEE 1,,,(@)   <- Measure both pins in parallel
PSER? 1,pval
PSER 1,P,(Vcc),#9000000006,1.501 <- value within range
PSER 1,F,(Vdd),#9000000006,3.173 <- value outside range
```

This example performs a measurement with format 2 and PSEE for two different pins in parallel.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSER? [setnr], {mode}
```

returns:

```
PSER [setnr], [result], {(pinlist)}, {binary_data}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSER  -  Power Supply External trigger measurement Read results）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98697.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：setnr | The set number of the external trigger measurement. (The range is 1 to 256). If this parameter is omitted, this command returns the result of previous e…
> 表内引用（1 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › PSER  -  Power Supply External trigger measurement Read results）

```
DPSE 1,(Vcc),#90000000170,0.1,0.2,0.2,0.3
DPSE 1,(Vdd),#90000000121,2,0.1,0.2
PSEE 1,,,()
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSER? 1,PVAL
PSER 1,P,(Vcc),#9000000010,0.15,0.25
PSER 1,F,(Vdd),#9000000010,0.3,0.3
```

### Example 3（取自子主题 Commands in alphabetical order › List of commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSER? 1,PPF
PSER 1,P,(Vcc),#9000000000
PSER 1,F,(Vdd),#9000000000
```

### Example 4（取自子主题 Commands in alphabetical order › List of commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSER? 1,GPF
PSER 1,F,(),#9000000000
PRLT? ALL // get multisite results
PRLT "FPP" // site 1 fail, sites 2 & 3 are pass
```

### Example 5（取自子主题 Commands in alphabetical order › List of commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSEE, I_300mA, 32, (Vee)
PSER? ,PVAL
```

returns:

```
PSER,,(Vee),#90000000120,0001923451
```

### Example 6（取自子主题 Commands in alphabetical order › List of commands › PSER  -  Power Supply External trigger measurement Read results）

```
DPSE 1,(Vcc),#90000000096,0.1,0.2
PSIE 1,,all_sampler,,,(Vcc)
PSER? ,PVAL
```

returns:

```
PSER ,,(Vcc),#90000000190.15,0.25,0.35,0.45
```

### PSFC（取自子主题 Commands in alphabetical order › List of commands › PSFC  PSFC  -  Parallel Setup FoCus）

```
PSFC {site|"site_string"|ALL}
```

### PSFC?（取自子主题 Commands in alphabetical order › List of commands › PSFC  PSFC  -  Parallel Setup FoCus）

```

PSFC? [STR]
```

returns

```
PSFC {"site_string"|ALL}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSFC  PSFC  -  Parallel Setup FoCus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98698.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：site | A single integer representing the site number.

### Example（取自子主题 Commands in alphabetical order › List of commands › PSFC  PSFC  -  Parallel Setup FoCus）

```
PSFC "11111110"
```

In this example, 8 sites are defined. The PSFC command unsets the setup focus for the last site. The setup data of this site will not be changed by any subsequent command execution.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › PSIE -  Power Supply Internal trigger Execute）

PSIE [setnr], [current_range] [,{keep_range|"RSTO"}] [,{all_sampler|"CH_ALL"}] [,{primary_act|"NPRM"}], [samples] [,settl_time], {(pinlist)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSIE -  Power Supply Internal trigger Execute）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98699.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：setnr | The set number defined by the DPSE command. (The range is 1 to 256). This set contains the limits of the measurement point for pass/fail judgment. When …
> 表内引用（1 条，供检索）：`DPSE`（raw: `02.06.02.02.85_DPSE__DPSE__-__Define_Power_Supply_External_trigger_measurement.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › PSIE -  Power Supply Internal trigger Execute）

```
> DPSE 1,(Vcc),#90000000112,0.09,0.11
> PSIE 1,,,(Vcc)
> PSER? 1,PVAL
< PSER 1,F,(Vcc),#9000000006,0.155
```

In this example, the `DPSE`（raw: `02.06.02.02.85_DPSE__DPSE__-__Define_Power_Supply_External_trigger_measurement.md`） command specifies a current limit of 0.9 A to 0.11 A for Vcc. Then the PSIE command starts measurements for the measurement set 1. In this case, the pin name is ignored because the set number is specified with the first parameter. After the measurement, the `PSER`（raw: `02.06.02.02.190_PSER__-__Power_Supply_External_trigger_measurement_Read_results.md`） command retrieves the measurement value for Vcc. In this case, the 300 mA range that is determined by using the specified limit value, is automatically selected for the measurement.

### PSLC（取自子主题 Commands in alphabetical order › List of commands › PSLC  PSLC  -  Power Supply Load Capacitance）

```
PSLC [value], [DCS_value,] {(pinlist)}
```

### PSLC?（取自子主题 Commands in alphabetical order › List of commands › PSLC  PSLC  -  Power Supply Load Capacitance）

```

PSLC? {(pinlist)}
```

returns:

```
PSLC {value}, [DCS_value,] {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSLC  PSLC  -  Power Supply Load Capacitance）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98700.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：value | The value of the load capacitor (capacitance) in μF in the range of 0.0 ... 214748364.6.
> 表内引用（1 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › PSLC  PSLC  -  Power Supply Load Capacitance）

DC Scale DPS128/DPS64

```
PSLC ,4.7, (VDD)
```

### PSLR（取自子主题 Commands in alphabetical order › List of commands › PSLR  PSLR  -  Power Supply Level Ranges）

```
PSLR {dps_No|dps_set_id}, [vout_frc_rng], [iout_clamp_rng], [current_limiter,] [const_curr_check], [connect_state], {(pinlist)}
```

### PSLR?（取自子主题 Commands in alphabetical order › List of commands › PSLR  PSLR  -  Power Supply Level Ranges）

```
PSLR? {dps_No|dps_set_id}, {(pinlist)}
```

returns:

```
PSLR {dps_No|dps_set_id}, [vout_frc_rng], [iout_clamp_rng], [current_limiter,] [const_curr_check], [connect_state], {(pinlist)}
```

Note The PSLR command supports only DC Scale channels, except for one parameter: const_curr_check can be set for standard DPS-slot DPS's as well.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSLR  PSLR  -  Power Supply Level Ranges）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98701.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 6 列，含嵌套表。
> 首行（上游原文）：dps_No | Needed for non-equation-based setup. The identification number of the DPS set which you want to modify. The number must not exceed the maximum number a…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98701.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：HIMP | High Impedance Measurement Mode. This mode allows you to use a DC Scale card as a voltmeter.

### Example 1（取自子主题 Commands in alphabetical order › List of commands › PSLR  PSLR  -  Power Supply Level Ranges）

```
PSLR PRM,4,0.5,OFF,NORM,(dps1)
```

This example sets the following parameters for device pin Vee:

- The current primary DPS set
- A voltage of 4 V
- A current of 0.5 A
- Current check is disabled
- The connect state is set to normal, and not high impedance measurement mode

### Example 2（取自子主题 Commands in alphabetical order › List of commands › PSLR  PSLR  -  Power Supply Level Ranges）

```
PSLR PRM,,,,HDIG,(dps1)
```

This example uses the default parameters for device pin Vee, while the connect state is set to digitizer mode.

### PSLV（取自子主题 Commands in alphabetical order › List of commands › PSLV  PSLV  -  Power Supply LeVel）

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

  Note If equation based testing is being used, you specify a DPS set ID instead of a DPS set number.  Note PSLV ALL only applies changes to all non-equation-based DPS sets.

### PSLV?（取自子主题 Commands in alphabetical order › List of commands › PSLV  PSLV  -  Power Supply LeVel）

```
PSLV? {dps_No|dps_set_id}, {(pinlist)}
```

returns:

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

 Note PSLV? ALL returns information for non-equation-based DPS sets only.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSLV  PSLV  -  Power Supply LeVel）

Note The settling time parameter (setup_time) of the PSLV command and the rise_... and fall_... parameters of the `PSSR, PSSR? -(Power Supply Slew Rate)`（raw: `02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md`） command exclude each other. This also applies to the t_ms equation parameter (see `DPSPINS`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md`） and `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）).

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98702.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：dps_No | Needed for non-equation-based setup.
> 表内引用（1 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › PSLV  PSLV  -  Power Supply LeVel）

```
PSLV 1,5.2,0.5,HIZ,15,(Vee)
```

This example sets the following parameters for device pin Vee:

- DPS set 1
- A voltage of 5.2 V
- A current limit of 0.5 A
- Minimum current limit when the test system is disconnected
- A setup time of 15 ms

### PSSL（取自子主题 Commands in alphabetical order › List of commands › PSSL  PSSL   Power Supply Safety Limits）

```
PSSL [min_voltage | OFF], [max_voltage | OFF], [max_source_current | OFF], [max_sink_current | OFF], {(pin_list)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSSL  PSSL   Power Supply Safety Limits）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143177.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：min_voltage | Lowest allowed voltage in V. Must be ≤ 0.
> 表内引用（2 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） · `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › PSSL  PSSL   Power Supply Safety Limits）

```
PSSL OFF,OFF,OFF,OFF,(DPS_1)
PSSL -2,5,0.5,0.5,(DPS_2)
PSSL -1.5,3,0.5,0.5,(SIG_1A)
```

### PSSR（取自子主题 Commands in alphabetical order › List of commands › PSSR  PSSR  - Power Supply Slew Rate）

```
PSSR {dps_No|dps_set_id}, [rise_tm_per_v], [rise_settm], [fall_tm_per_v], [fall_settm], [rise_t_per_v_c2c], [rise_setup_t_c2c], [fall_t_per_v_c2c], [fall_setup_t_c2c], (pinlist)
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSSR  PSSR  - Power Supply Slew Rate）

Note The rise_... and fall_... parameters of the PSSR command and the settling time parameter (setup_time) of the `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`） command exclude each other. This also applies to the t_ms equation parameter (see `DPSPINS`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md`） and `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）). Note All time values have a resolution of microseconds (floating point values are rounded to three decimal places).

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/120504.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 2 列。
> 首行（上游原文）：dps_No | Needed for non-equation-based setup. The identification number of the DPS set which you want to modify. The number must not exceed the maximum number a…
> 表内引用（1 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › PSSR  PSSR  - Power Supply Slew Rate）

```
PSSR PRM,10,50,20,70,(Vcc)
```

This example sets the following parameters for the primary set of DPS pin Vcc:

- rise_tm_per_v = 10 ms/V
- rise_settm = 50 ms
- fall_tm_per_v = 20 ms/V
- fall_settm = 70 ms

### PSST（取自子主题 Commands in alphabetical order › List of commands › PSST  PSST  -  Power Supply STatus）

```
PSST {state} [, (pinlist)]
```

### PSST?（取自子主题 Commands in alphabetical order › List of commands › PSST  PSST  -  Power Supply STatus）

```
PSST?  [(pinlist)]
```

returns:

```
PSST {state} [, (pinlist)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSST  PSST  -  Power Supply STatus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98710.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：state | The device power supply state:

### Example 1（取自子主题 Commands in alphabetical order › List of commands › PSST  PSST  -  Power Supply STatus）

```
PSST ON
```

This example turns the DPS on.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › PSST  PSST  -  Power Supply STatus）

The following example shows the use of the PSST command in conjunction with multisite:

```
PSFC ALL ; PSST ON   # turn on all supplies of all sites

PSFC "01"              # focus on one site only of the dual-site

PSST OFF,(vcc)         # turn off vcc of one site only!
PQFC 1 ; PSST? (vcc)   # these last two commands return different
PQFC 2 ; PSST? (vcc)   # answers, since one site should have vcc
                       # connected, whereas the other site does not
```

### PSTE（取自子主题 Commands in alphabetical order › List of commands › PSTE  PSTE  -  Parallel SiTe Enable）

```
PSTE {sites}
```

### PSTE?（取自子主题 Commands in alphabetical order › List of commands › PSTE  PSTE  -  Parallel SiTe Enable）

```
PSTE? [STR]
```

returns

```
PSTE {sites|"site_string"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PSTE  PSTE  -  Parallel SiTe Enable）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98711.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：sites | The sites parameter is an integer that specifies the number of sites (to be) configured. The maximum is 1024. For more information, refer to Number of s…
> 表内引用（2 条，供检索）：`Number of sites`（raw: `../../01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md#_116532__r_numberOfSites`） · `SmarTest system parameters - default values and limits`（raw: `../../01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › PSTE  PSTE  -  Parallel SiTe Enable）

```
> PSTE 3
```

This example configures three sites (site 1, site 2, and site 3).

```
> PSTE? STR
< PSTE "101"
```

This example says that three sites are configured, but that only two of them (site 1 and site 3) are available for testing. Site 2 uses a channel that is listed in the MCDIgnore file, and therefore cannot be used for testing.

### PTDE（取自子主题 Commands in alphabetical order › List of commands › PTDE  PTDE  -  Path for Test Data Entities）

PTDE "<device_directory>/<domain>/<TDE_directory>"

### PTDE?（取自子主题 Commands in alphabetical order › List of commands › PTDE  PTDE  -  Path for Test Data Entities）

PTDE?

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PTDE  PTDE  -  Path for Test Data Entities）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124520.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：device_directory | The path to the device directory in which the test data entities (TDEs) are located.

### Example（取自子主题 Commands in alphabetical order › List of commands › PTDE  PTDE  -  Path for Test Data Entities）

```
PTDE "/mydevice/configuration/test.files"
```

### PTDS（取自子主题 Commands in alphabetical order › List of commands › PTDS  PTDS  -  Pin attributes Tweaking Definition String）

```
PTDS {channelNo}, [EBT_specifier], {set_specifier}, {timing_set}, [tweaking_set], [mode], {definition_string}
```

### PTDS?（取自子主题 Commands in alphabetical order › List of commands › PTDS  PTDS  -  Pin attributes Tweaking Definition String）

```
PTDS? {channelNo}, [EBT_specifier], {set_specifier}, {timing_set}, [tweaking_set], [mode]
```

returns:

```
PTDS {channelNo}, [EBT_specifier], {set_specifier}, {timing_set}, [tweaking_set], [mode], {definition_string}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › PTDS  PTDS  -  Pin attributes Tweaking Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98713.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 3 列。
> 首行（上游原文）：channelNo | This is a five digit field which defines the channel to which the pin is connected. See also the command DFPN, DFPN? - (DeFine Pin Name) for this pa…
> 表内引用（1 条，供检索）：`DFPN, DFPN? - (DeFine Pin Name)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › PTDS  PTDS  -  Pin attributes Tweaking Definition String）

```
PTDS 10812,0,4,5,,1,1,"d1:2,d2:0.003, d8:5, r1:-1, r2:-2"
PTDS? 10101,,all,all,,
```

The following example defines pin attributes for timing sets of the multi-port specification spec_port_1_port_2.

```
> PTDS 10101,,"spec_port_1_port_2",1,,,"d1:1 d3:3"
> PTDS 10101,,"spec_port_1_port_2",2,,,"d1:2 d2:3"
> PTDS? 10101,,"spec_port_1_port_2",ALL,,
< PTDS 10101,,"spec_port_1_port_2",1,,,"d1:1 d3:3"
< PTDS 10101,,"spec_port_1_port_2",2,,,"d1:2 d2:3"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RCLK  -  Reference CLocK source）

```
RCLK?
```

returns:

```
RCLK {clock_string}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RCLK  -  Reference CLocK source）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98715.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：clock_string | The string shows which clock source is used as reference clock. Possible values are: EXTERNAL INTERNAL

### Example（取自子主题 Commands in alphabetical order › List of commands › RCLK  -  Reference CLocK source）

```
RCLK?
```

returns:

```
RCLK INTERNAL
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RCLS  -  ReCeive Level Sensitivity）

```
RCLS? {test}, {pass_value}, [limit], {(pinlist)}
```

returns:

```
RCLS {value_specifier}, {result_value}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RCLS  -  ReCeive Level Sensitivity）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98716.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 4 列。
> 首行（上游原文）：test | This parameter is one of the following:

### Example（取自子主题 Commands in alphabetical order › List of commands › RCLS  -  ReCeive Level Sensitivity）

```
RCLS? H,3000,6000,(Q0)
```

returns:

```
RCLS EQ,5300
```

In this example a search was made to find the high level threshold between 3V and 6V. The pass/fail transition was located at 5.3V.

### RCLV（取自子主题 Commands in alphabetical order › List of commands › RCLV  RCLV  -  ReCeive LeVel）

```
RCLV {level_set_no | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### RCLV?（取自子主题 Commands in alphabetical order › List of commands › RCLV  RCLV  -  ReCeive LeVel）

```
RCLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
RCLV {level_set | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RCLV  RCLV  -  ReCeive LeVel）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98717.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：level_set | The identification number of the level set in which you want the low and high threshold levels to be included. The number must not exceed the maximu…
> 表内引用（3 条，供检索）：`DSCP, DSCP? - (Define System Control Parameter)`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

For card specifications, like level ranges, see `Digital Cards`（raw: `../02.02_Specifications/02.02.04_Digital_Cards.md`）, for example:

- `Pin Scale 1600`（raw: `../02.02_Specifications/02.02.04.01.03_PS1600_driver.md`）
- `Pins Scale 5000`（raw: `../02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › RCLV  RCLV  -  ReCeive LeVel）

```
RCLV 1,-1300,-750,(Q0)
```

This example sets the low level compare threshold for pin Q0 to -1300 mV and the high level compare threshold to -750 mV.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › RCLV  RCLV  -  ReCeive LeVel）

```
TERM 1,,,,,,HRV,(avi64Pin1)
RCLV 1,-1300,-750,3000,(avi64Pin1)
```

This example for an AVI64 pin sets the low level compare threshold to -1300 mV, the high level compare threshold to -750 mV, and the range to the 3 V range.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RDGC -  Reset DiGital Capture）

```
RDGC {"vector_label"|ALL}[,(portlist)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RDGC -  Reset DiGital Capture）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99065.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：vector_label | Vector main label. You can specify ALL to dissolve the associations for all vector labels of one or more ports.

### Example（取自子主题 Commands in alphabetical order › List of commands › RDGC -  Reset DiGital Capture）

```
> SDGC? ALL,(@@)
< SDGC "vec_lab_portA_1",STD,(I/O7_1,I/O6_1,I/O5_1)
< SDGC "vec_lab_portA_2",STD,(I/O2_1,I/O1_1,I/O0_1)
< SDGC "vec_lab_portB_1",STD,(I/O7_2,I/O6_2,I/O5_2)
< SDGC "vec_lab_portB_2",STD,(I/O3_2,I/O2_2,I/O1_2)
> RDGC ALL,(port_A)
> SDGC? ALL,(@@)
< SDGC "vec_lab_portB_1",STD,(I/O7_2,I/O6_2,I/O5_2)
< SDGC "vec_lab_portB_2",STD,(I/O3_2,I/O2_2,I/O1_2)
```

### RLYC（取自子主题 Commands in alphabetical order › List of commands › RLYC  RLYC  -  ReLaY Control）

```
RLYC [pin_mode], [dc_target], [mux_setting,] {(pinlist)}
```

### RLYC?（取自子主题 Commands in alphabetical order › List of commands › RLYC  RLYC  -  ReLaY Control）

```
RLYC? {(pinlist)}
```

returns:

```
RLYC [pin_mode], [dc_target], {(pinlist)}
```

 Note

In offline mode, the command cannot always return the correct settings of the hardware. This is especially true when hardware settings depend on pattern‑based conditional jumps and match loops.

 If SmarTest determines that the state of the hardware cannot be evaluated correctly, the message

```
WARNING: ... - reported last DC state ... may not reflect online state.
```

is issued in the ui_report window.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RLYC  RLYC  -  ReLaY Control）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98721.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：18 行 × 8 列，含嵌套表。
> 首行（上游原文）：pin_mode | This parameter controls per-pin relay resources. These are AC, DC and PPMU relays. pin_mode can take the following options: IDLE | Disconnects all re…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98721.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 2 列。
> 首行（上游原文）：IDLE | Disconnects all relays
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98721.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：OFF | Opens all channel board and clock board relays.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98721.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：MUX_VM_HIZ | Switches the MUX to the high-impedance input of the BADC.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98721.htm`
> 中**第 5 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：RLYC IDLE,OFF,(pin) | Open all relays.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RRDF -  Result Retention area DeFinition）

RRDF {area-id}, {size}[, (pinlist)]

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RRDF -  Result Retention area DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/121741.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：area-id | A unique string for identifying the result retention area. The area is referenced when being selected by its ID for result acquisition or upload. The …
> 表内引用（1 条，供检索）：`DMAS`（raw: `02.06.02.02.79_DMAS__DMAS__-__Define_Memory_Area_Size.md`）

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RRSC -  Result Retention area Select for Capture）

RRSC {area-id} | OFF

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RRSC -  Result Retention area Select for Capture）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/121743.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：area-id | A unique string identifying a specific result retention area.

Enumerated parameter to switch back to normal result acquisition.

Using OFF will return result acquisition to non-reserved memory or internal error map (as specified by DCRT).

   | Note The RRDF pin list must match the capture pins for a capture test. An error map test requires that all pins of the selected port (recording to RAM via DCRT) are included.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RRUD -  Result Retention area UnDefine）

```
RRUD
```

If the result area is currently selected for recording or upload, it will be deactivated.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RSET -  ReSET）

```
RSET {specifier}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RSET -  ReSET）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98723.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：specifier | The specifier can be:
> 表内引用（1 条，供检索）：`UHCM`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › RSET -  ReSET）

```
RSET TIM
```

This example resets all waveform sets and timing sets and loads the hardware with the default vector rate and edge placement values. Only waveform set 1 and timing set 1 in waveform set 1 is active.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RSSR  -  Retrieve Spec Search Results）

```
RSSR? {set_nr},[(setup_pinlist)]
```

returns:

```
RSSR {set_nr},(search_result),[pass_value],[fail_value],(setup_pinlist)
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98724.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：set_nr | Specifies the number of the search set for which results are to be returned.

### Example（取自子主题 Commands in alphabetical order › List of commands › RSSR  -  Retrieve Spec Search Results）

```
> PQFC 2
> RSSR? 3,(@)
< RSSR 3,P,90.1,90.2,(OUT1)
< RSSR 3,P,33.1,33,(IN1)
```

In this example, RSSR? returns the results of all setup pins in search set 3 for site 2. For OUT1, a pass/fail transition was found, for IN1 a fail/pass transition.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RRSU   Result Retention area Select for Upload）

RRSU {area-id} | OFF

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RRSU   Result Retention area Select for Upload）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140930.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：area-id | Mandatory parameter consisting of a variable string. The quotes belong to the command language (not the syntax language) and must be specified in the …

Enumerated parameter to switch back to normal result upload focus.

Using OFF will return result retrieval to the default result area or internal error map (as specified by DCRT).

   | Note The result area selected for upload must contain valid results. That means the area must have been defined via RRDF, must have been selected as recording target prior to a test execution using RRSC.

### Example（取自子主题 Commands in alphabetical order › List of commands › RRSU   Result Retention area Select for Upload）

The following example defines a result area with the name "my_area" with a size of 128KB for all pins. This area is then selected as recording target for the subsequent functional test. The results in this area remain available even after execution of additional functional tests and can later be accessed by switching the upload forcus with 'RRSU 'my_area'' to it.

```
RRDF "my_area",128000,(@)
RRSC "my_area"
FTST?
RRSC OFF
RRSU "my_area"
ERMP? EDGE,0,8000,PF,8,(emap_pin)
RRSU OFF
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RVCU -  Remove Vector variable Configuration Usage）

```
RVCU {label name}, {VVC name}, vector offset
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RVCU -  Remove Vector variable Configuration Usage）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99066.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：label name | Name of the label for which usage is to be modified.
> 表内引用（3 条，供检索）：`DVVC, DVVC? - (Define Vector Variable Configuration)`（raw: `02.06.02.02.95_DVVC__DVVC__-__Define_Vector_Variable_Configuration.md`） · `DVCU`（raw: `02.06.02.02.96_DVCU__DVCU__-__Define_Vector_variable_Configuration_Usage.md`） · `DVCU, DVCU? - (Define Vector variable Configuration Usage)`（raw: `02.06.02.02.96_DVCU__DVCU__-__Define_Vector_variable_Configuration_Usage.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › RVCU -  Remove Vector variable Configuration Usage）

The following example removes the usage defined for label "src" using VVC "AC97" at offset 0.

```
> RVCU "src","AC97",0
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RVVA -  Remove Vector VAriable）

RVVA {"name"|ALL}[, (portlist)]

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RVVA -  Remove Vector VAriable）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99067.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：name | Name of the vector variable to be deleted. ALL can be used to remove all vector variables that are associated with the vector labels of one or more ports…

### Example（取自子主题 Commands in alphabetical order › List of commands › RVVA -  Remove Vector VAriable）

```
> DVVA? ALL,(@@)
< DVVA "vec_3",DIGCAPT,"port1_A",PARA,,,,0,1,1,0,
       1,0,(Q7_1)
< DVVA "vec_1",DIGCAPT,"port2_A",PARA,,,,0,1,1,0,
       1,0,(I/O5_2)
< DVVA "vec_2",DIGCAPT,"port2_B",PARA,,,,0,1,1,0,
       1,0,(I/O7_2,I/O6_2)
> RVVA ALL,(port_2)
> DVVA? ALL,(@@)
< DVVA "vec_3",DIGCAPT,"port1_A",PARA,,,,0,1,1,0,
       1,0,(Q7_1)
```

This example removes all vector variables that are defined for vector labels associated with port port_2.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RVVC -  Remove Vector Variable Configuration）

```
RVVC {VVC name}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RVVC -  Remove Vector Variable Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99069.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：VVC name | Name of the vector variable configuration to be removed.

### SAOF（取自子主题 Commands in alphabetical order › List of commands › SAOF  SAOF  -  Set Alternating Operation Features）

```
SAOF {mode|"label"}
```

### SAOF?（取自子主题 Commands in alphabetical order › List of commands › SAOF  SAOF  -  Set Alternating Operation Features）

```
SAOF?
```

returns:

```
SAOF {mode|"label"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SAOF  SAOF  -  Set Alternating Operation Features）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98726.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：mode | The operation mode which can take the following values:

### Example（取自子主题 Commands in alphabetical order › List of commands › SAOF  SAOF  -  Set Alternating Operation Features）

The following example illustrates the effects of the APP mode:

```
> SAOF?
< SAOF ZERO
> DMAS SQPG,SM,4,(@)
> DMAS SQPG,SM,3,(@)
> DMAS? SQPG,SM,(@)
< DMAS SQPG,SM,3,(@)
> SAOF APP
> DMAS SQPG,SM,4,(@)
> SAOF ZERO
> DMAS? SQPG,SM,(@)
< DMAS SQPG,SM,7,(@)
```

### SATR（取自子主题 Commands in alphabetical order › List of commands › SATR  SATR  -  System ATtRibutes）

SATR {comm_rec_delay}

### SATR?（取自子主题 Commands in alphabetical order › List of commands › SATR  SATR  -  System ATtRibutes）

```
SATR?
```

returns:

```
SATR {comm_rec_delay}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SATR  SATR  -  System ATtRibutes）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98727.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：comm_rec_delay | The common receiver delay represents the adjustment to the round-trip delay between the drivers and receivers. The delay is in [ns] and must be…

### Example（取自子主题 Commands in alphabetical order › List of commands › SATR  SATR  -  System ATtRibutes）

```
SATR 20
```

This example sets the common receiver delay to 20 ns.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › SCLK  -  System CLocK query）

```
SCLK? {wf_set|specset_id|"multi-port_spec"|ALL|PRM}
```

returns:

```
SCLK {wf_set|specset_id|"multi-port_spec"} {sclk_val}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SCLK  -  System CLocK query）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98728.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：wf_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? - …
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › SCLK  -  System CLocK query）

```
> SCLK? 401
< SCLK 401,480
```

### SDGC（取自子主题 Commands in alphabetical order › List of commands › SDGC  SDGC  -  Setup DiGital Capture）

```
SDGC {"vector_label"},[res_mode],{(pinlist)}
```

### SDGC?（取自子主题 Commands in alphabetical order › List of commands › SDGC  SDGC  -  Setup DiGital Capture）

```
SDGC? {"vector_label"|ALL}[, (portlist)]
```

returns:

```
SDGC {"vector_label"},[res_mode],{(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SDGC  SDGC  -  Setup DiGital Capture）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99070.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：vector_label | The vector label that is to be activated for digital capture. It must be a main label, and the sequencer memory must have been specified as the l…

### Example（取自子主题 Commands in alphabetical order › List of commands › SDGC  SDGC  -  Setup DiGital Capture）

```
> SDGC? ALL
< SDGC "test_capt",STD,(OUT_1,OUT_2)
```

This example returns all the vector labels of the default port @ that are activated for digital capture.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › SDSC  -  Set number DeSCriptions）

```
SDSC? {spec_type}, {type}, [setup_comp_1], [setup_comp_2], ["description"]
```

returns:

```
SDSC {spec_type}, {type}, [setup_comp_1], [setup_comp_2], {"description"}
```

Alternatively, for multiport specifications:

```
SDSC? {TIM}, {type}, [setup_comp_1], {"multi-port_spec"}, ["description"][, (portlist)]
```

returns:

```
SDSC {TIM}, {type}, [setup_comp_1], {"multi-port_spec"}, {"description"}, {(port)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：21 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

The following table explains the interpretation of the setup_comp_1 and setup_comp_2 parameters for every accepted value pair of the spec_type and type parameters:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 4 列。
> 首行（上游原文）：spec_type | type | setup_comp_1 | setup_comp_2

### Example 1（取自子主题 Commands in alphabetical order › List of commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,,,
< SDSC TIM,EQN,1,,"gross_func_eqn"
< SDSC TIM,EQN,2,,"specs_search_eqn"
< SDSC TIM,EQN,3,,"speed_eqn"
```

This example returns all defined equation sets.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,2,"spec_port_1_port_2",,(port_1)
< SDSC TIM,EQN,1,"spec_port_1_port_2",
     "gross_func_eqn",(port_1)
```

This example returns the equation set that is associated with port port_1 in the multiport specification

spec_port_1_port_2. Note that the setup_comp_1 parameter is ignored.

### SHSP（取自子主题 Commands in alphabetical order › List of commands › SHSP  SHSP  -  SHmoo SPecs）

```
SHSP [spec_type_1], ["spec_name_1[@port[@UNCHANGED]]"], [(pinlist_1)], [spec_type_2], ["spec_name_2[@port[@UNCHANGED]]"], [(pinlist_2)]
```

### SHSP?（取自子主题 Commands in alphabetical order › List of commands › SHSP  SHSP  -  SHmoo SPecs）

```
SHSP?
```

returns:

```
SHSP [spec_type_1], ["spec_name_1"], [(pinlist_1)], [spec_type_2], ["spec_name_2"], [(pinlist_2)]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98732.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：spec_type_<number> | Which specification type to use. Use:
> 表内引用（1 条，供检索）：`DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › SHSP  SHSP  -  SHmoo SPecs）

```
> SHSP LEV, "aclk_vil",(aclkout), LEV, "adata_vil", (adata3)
> SHSP?
< SHSP LEV, "aclk_vil",(aclkout), LEV, "adata_vil", (adata3)
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › SHSP  SHSP  -  SHmoo SPecs）

In the following Pin Scale example, both spec variables occur in the period definitions associated with the two ports:

```
> CLKR? "MP_spec",(Port1)
< CLKR "MP_spec",17,3.4,(Port1)
> PRPT? "MP_spec","shmsp@Port1";
< PRPT "MP_spec",(Port2)
> SHSP TIM, "shmsp@Port1",,TIM,"shmsp@Port2",
> SHVL 17,30
> PRPT? "MP_spec","shmsp@Port1"
< PRPT "MP_spec",(Port1)
> CLKR? "MP_spec",(Port1)
< CLKR "MP_spec",17,4.25,(Port1)
```

Since `shmsp` is used in the period definitions for both port `Port1` and `Port2`, the one that is specified first in the SHSP command will be used to derive the period resolution. Note that the primary port is only changed after issuing the SHVL command.

### SHVL（取自子主题 Commands in alphabetical order › List of commands › SHVL  SHVL  -  SHmoo spec VaLues）

```
SHVL [value_1], [value_2]
```

### SHVL?（取自子主题 Commands in alphabetical order › List of commands › SHVL  SHVL  -  SHmoo spec VaLues）

```
SHVL?
```

returns:

```
SHVL [value_1], [value_2]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SHVL  SHVL  -  SHmoo spec VaLues）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98733.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：value_1 | A double float defining the new value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647. Or use RSTO to restor…

### Example（取自子主题 Commands in alphabetical order › List of commands › SHVL  SHVL  -  SHmoo spec VaLues）

```
> SHSP TIM, "shmsp@Port1",, TIM, "shmsp@Port2",
> SHVL 2,3
> SHVL?
< SHVL 2,3
```

### SLDO（取自子主题 Commands in alphabetical order › List of commands › SLDO -  Switch Level and Dps Order）

```
SLDO {order}, [report]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SLDO -  Switch Level and Dps Order）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98735.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：order | This parameter sets the switching order mode:

### Example（取自子主题 Commands in alphabetical order › List of commands › SLDO -  Switch Level and Dps Order）

```
SLDO CVDL, AMBI
```

This example switches either the DPS voltage values or the level voltage values first when changing from one DPS or level set to the next depending on which of the three above mentioned cases occur and reports any ambiguous case.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › SPCP  -  SPeCification Port list）

```
SPCP? {"multi-port_spec"|ALL}
```

returns:

```
SPCP {"multi-port_spec"}, {(portlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SPCP  -  SPeCification Port list）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98738.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：multi-port_spec | Defines the multi-port specification for which the ports are to be queried. You can enter ALL in order to display the ports for all defined mu…

### Example（取自子主题 Commands in alphabetical order › List of commands › SPCP  -  SPeCification Port list）

```
> SPCP? ALL
< SPCP "spec_port_1_port_2",(port_1,port_2)
< SPCP "spec_ClkP_P1_P2",(ClockPort,p_CP_1,p_CP_2)
< SPCP "spec_ssearch_port_1_port_2",(port_1,port_2)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › SPEC  -  SPECification）

```
SPEC? {"module:resource"},["details"],[context], [(pinlist)]
```

returns:

```
SPEC {"module:resource"},["details"],[context], {answer},[(pinlist)]
```

   Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98739.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 3 列。
> 首行（上游原文）：module:resource | Specifies the module and the resource about which information is to be returned. Currently, the following values are allowed:

### Example 1（取自子主题 Commands in alphabetical order › List of commands › SPEC  -  SPECification）

```
SPEC? "Result:Xmodes",,,(@)
```

returns

```
SPEC "Result:Xmodes",,,"1,2,4,6,8",(...)
```

This example queries which x-modes are possible for the result module on a Smart Scale system. On a Pin Scale system, x-mode 6 would be omitted in the reply.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › SPEC  -  SPECification）

The second example queries the termination modes that can be specified with the `TERM`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） command for pin "PS1600_pin" and level set 1:

```
SPEC? "Level:Term",,1,(PS1600_pin)
```

returns

```
SPEC "Level:Term",,1,"OFF,T,H,L,A,C,CT,HV,DIFHIZ",(PS1600_pin)
```

### Example 3（取自子主题 Commands in alphabetical order › List of commands › SPEC  -  SPECification）

The third example queries the range of the fixture delay:

```
SPEC? "Timing:FxdlRange",,"Global",
```

returns

```
SPEC "Timing:FxdlRange",,"Global","-0.015000,13.200000",()
```

The query returns the range for Pin Scale systems.

Note: Parameter pinlist is irrelevant for this query and may be omitted.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › SPGV -  SPlit Generate Vectors）

```
SPGV {vec_No}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SPGV -  SPlit Generate Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98740.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：vec_No | The logical vector number at which a GENV sequencer construct is to be split.

### Example（取自子主题 Commands in alphabetical order › List of commands › SPGV -  SPlit Generate Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,16,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
< SQPG 5,STVA,528,,,(@)
< ...
> SPGV 7
> TSTL "test_1",(@)
> SQPG ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,7,,,(@)
< SQPG 3,GENV,9,,,(@)
< SQPG 4,RPTV,6,5,,(@)
< SQPG 5,STOP,,,,(@)
< SQPG 6,STVA,536,,,(@)
< ...
```

This example splits a GENV sequencer construct at command number 2 before vector 7. Note the adjustment of the start address in command 6.

### SPOP（取自子主题 Commands in alphabetical order › List of commands › SPOP  SPOP  Set Performance Optimization Parameter）

```
SPOP {keyword}, {value}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SPOP  SPOP  Set Performance Optimization Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98741.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：keyword | Specifies the parameter for which performance optimization is to be changed or queried. Currently, the only possible value is: SVLR_CACHE_DEPTH: Defin…
> 表内引用（1 条，供检索）：`SVLR`（raw: `02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › SPOP  SPOP  Set Performance Optimization Parameter）

> SPOP SVLR_CACHE_DEPTH, 20

> SPOP? SVLR_CACHE_DEPTH

< SPOP SVLR_CACHE_DEPTH, 20

### SPRM（取自子主题 Commands in alphabetical order › List of commands › SPRM  SPRM  -  Set PRiMary sets）

```
SPRM [waveform_set_no], [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or:

```
SPRM {timing_specset_id}, [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or, for multiport specifications:

```
SPRM {"multi-port_spec"}, [timing_set_no|"timing_set_list"], [level_set_id|level_set_no],[dps_set_id|dps_set_no] [,(port)]
```

### SPRM?（取自子主题 Commands in alphabetical order › List of commands › SPRM  SPRM  -  Set PRiMary sets）

```
SPRM?
```

returns:

```
SPRM {waveform_set_no}, {timing_set_no}, {level_set_no|level_set_id}, {dps_set_no|dps_set_id}
```

or:

```
SPRM {timing_specset_id}, {timing_set_no}, {level_set_id|level_set_no}, {dps_set_id|dps_set_no}
```

or, for multiport specifications:

```
SPRM? [(port)]
```

returns:

```
SPRM {"multi-port_spec"}, {timing_set_no|"timing_set_list"}, {level_set_id|level_set_no},{dps_set_id|dps_set_no} [,(port)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SPRM  SPRM  -  Set PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98742.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set_no | The identification number of the waveform set. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum num…
> 表内引用（6 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `CONF, CONF? - (CONFiguration)`（raw: `02.06.02.02.31_CONF__CONF__-__CONFiguration.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `LSUS, LSUS? - (Level Sets USed)`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`） · `DSUS, DSUS? - (Dps Sets USed)`（raw: `02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › SPRM  SPRM  -  Set PRiMary sets）

The following example shows how to define and query primary timing sets for the multi-port specification spec_ClockP_P1_P2, which contains three ports:

```
> SPRM "spec_ClockP_P1_P2","2,1,2",,
> SPRM?
< SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003
> SPRM "spec_ClockP_P1_P2",2,,,(port_1.CP_1)
> SPRM?
< SPRM "spec_ClockP_P1_P2",2,101002,101003
> SPRM? (port_1.CP_1)
< SPRM "spec_ClockP_P1_P2",2,101002,101003,(port_1.CP_1)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › SPST  -  SPecset STatus）

```
SPST? {spec_type}, {equation_set_no}, {specset_no}
```

returns:

```
SPST {spec_type}, {equation_set_no}, {specset_no}, {status}
```

or, for multiport specifications:

```
SPST? {spec_type}, , {"multi-port_spec"}
```

or

```
SPST? {spec_type}, PRM,
```

returns:

```
SPST {spec_type},, {"multi-port_spec"}, {status}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SPST  -  SPecset STatus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

Status bits for the status parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：Bit | Description | Value
> 表内引用（10 条，供检索）：`ETIM`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`） · `ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） · `PCLK`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） · `CLKR`（raw: `02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md`） · `DRLV`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`） · `RCLV`（raw: `02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`） · `TERM`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） · `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`） · `SHVL`（raw: `02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md`） · `SVLR`（raw: `02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › SPST  -  SPecset STatus）

```
> SPST? lev,all,all
< SPST LEV,1,1,0
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › SPST  -  SPecset STatus）

```
> SPST? tim,all,all
<  SPST TIM,1,1,0
< SPST TIM,2,22,0
```

### Example 3（取自子主题 Commands in alphabetical order › List of commands › SPST  -  SPecset STatus）

```
> SPST? TIM,,"mu_burst"
< SPST TIM,,"mu_burst",6
```

In this last example, a multi-port specification is queried. The answer says that bits 1 and 2 have been set. This has the effect that a drive or receive period 1 limit violation will be ignored, and only a period 2 limit violation will be recorded.

### SQBV（取自子主题 Commands in alphabetical order › List of commands › SQBV  SQBV  -  SeQuencer Break Vector insertion）

```
SQBV [CTOF_align],[pattern_align],[activ_type],{(port)}
```

### SQBV?（取自子主题 Commands in alphabetical order › List of commands › SQBV  SQBV  -  SeQuencer Break Vector insertion）

```
SQBV? {(port)}
```

returns:

```
SQBV {CTOF_align},{pattern_align},{activ_type},{(portlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98745.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：CTOF_align | This parameter specifies the number of break vectors that are to be inserted before the last activation. If the specified number is not exactly div…
> 表内引用（1 条，供检索）：`FTCG`（raw: `02.06.02.02.125_FTCG__FTCG__-__Functional_Test_ConfiGure.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › SQBV  SQBV  -  SeQuencer Break Vector insertion）

The following example synchronizes two ports RX and TX, each of which is the only port in its sequencing group. The RX port does not admit any changes of primary sets, the TX port must change its primary sets several times during the testflow. This is implemented by the `FTCG`（raw: `02.06.02.02.125_FTCG__FTCG__-__Functional_Test_ConfiGure.md`） command as follows:

```
> FTCG SKPR,OFF,(@@)
> FTCG SKPR,ON,(RX)
```

In order to synchronize both ports, the time span used up by the activation sequences in TX must be filled with break vectors in RX. If both ports operate with the same period length, and the PHASE flag is set for both of them in the multi-port timing specification, then the number of break vectors that compensates the different types of activation sequences will always be a multiple of 8. The exact number must be determined by empirical tests. The required numbers could then be passed to SQBV as follows:

```
> SQBV ,1504,TIM,(RX)
> SQBV ,22048,TIM_LEV,(RX)
> SQBV ,31784,ALL,(RX)
```

The reference port is TX. This is specified by

```
> SQRP (TX)
```

Finally, the timing changes in TX may include moving receive edges across cycle boundaries, and this in turn can (in rare cases) prolong the activation sequence for the next functional test. But this is not acceptable, because only one value can be passed to SQBV for every activation sequence type. In order to secure that the length of an activation sequence is not affected by the timing of the preceding test, break vectors can be inserted in TX before the last activation of the respective sequence type, so that the sequence as a whole has the extended length even if no cycle crossing takes place in the previous test.

The required number of break vectors must again be determined by measurements. The required number of vectors could then be defined as follows:

```
> SQBV 128,,TIM,(TX)
> SQBV 128,,TIM_LEV,(TX)
> SQBV 128,,ALL,(TX)
```

Note that in this case the insertion port is identical with the reference port.

### SQEC（取自子主题 Commands in alphabetical order › List of commands › SQEC  SQEC  -  SeQuencer Execution Context）

```
SQEC {"context_name"}, {(port_list)}
```

### SQEC?（取自子主题 Commands in alphabetical order › List of commands › SQEC  SQEC  -  SeQuencer Execution Context）

```
SQEC? {"context_name"|ALL}
```

returns:

```
SQEC {"context_name"}, {(port_list)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SQEC  SQEC  -  SeQuencer Execution Context）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/137546.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：context_name | The name of the context. If a context with this name already exists, the previous definition will be overwritten.

### Example（取自子主题 Commands in alphabetical order › List of commands › SQEC  SQEC  -  SeQuencer Execution Context）

```
> SQEC "c1",(P1,P2)
> SQEC? ALL
< SQEC "c1",(P1,P2)
```

### SQGB（取自子主题 Commands in alphabetical order › List of commands › SQGB  SQGB  -  SeQuencer GloBal）

```
SQGB [mode], [analyze_delay][, (ref_port)]
```

### SQGB?（取自子主题 Commands in alphabetical order › List of commands › SQGB  SQGB  -  SeQuencer GloBal）

```
SQGB? [(portlist)]
```

returns:

```
SQGB {mode}, [analyze_delay][, (port)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SQGB  SQGB  -  SeQuencer GloBal）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98746.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：mode | Possible values are:
> 表内引用（1 条，供检索）：`GETC? - (GET Cycles)`（raw: `02.06.02.02.131_GETC__-__GET_Cycles.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › SQGB  SQGB  -  SeQuencer GloBal）

```
> PCLK? "mu_burst",1,(@@)
< PCLK "mu_burst",1,20,(P1)
< PCLK "mu_burst",1,10,(P2)
> SPRM "mu_burst",1,,
> SQSL "mu_burst"
> SQGB STSQ,30,(P2)
> SQGB? (@@)
< SQGB STSQ,15,(P1)
< SQGB STSQ,30,(P2)
```

This example configures the sequencers to stop when port P2 has completed 30 cycles. Port P1, whose period length is twice the period length of P2, will be stopped after 15 cycles. Note that P1 and P2 must belong to the same sequencing group.

### SQIB（取自子主题 Commands in alphabetical order › List of commands › SQIB  SQIB  -  SeQuencer Interrupt Behavior）

```
SQIB {BANDWIDTH|TIMEOUT}, {ERIM|ERRQ|FLIM|FLRQ}
```

### SQIB?（取自子主题 Commands in alphabetical order › List of commands › SQIB  SQIB  -  SeQuencer Interrupt Behavior）

```
SQIB? {BANDWIDTH|TIMEOUT}
```

returns:

```
SQIB {BANDWIDTH|TIMEOUT}, {ERIM|ERRQ|FLIM|FLRQ}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SQIB  SQIB  -  SeQuencer Interrupt Behavior）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/127771.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：BANDWIDTH | This refers to the behavior when the detailed error map is located in the external memory, and result recording was aborted due to a bandwidth overf…

### Example（取自子主题 Commands in alphabetical order › List of commands › SQIB  SQIB  -  SeQuencer Interrupt Behavior）

```
SQIB BANDWIDTH FLrQ
```

This example suppresses all error messages in case of a recording abort.

### SQIT?（取自子主题 Commands in alphabetical order › List of commands › SQIT  -  SeQuencer InterRupt）

```
SQIT? ["context"]
```

returns:

```
SQIT {NO}
```

or

```
SQIT {BANDWIDTH|TIMEOUT|OTHER}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SQIT  -  SeQuencer InterRupt）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/137548.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：context | The name of an execution context. For more information on execution contexts see Using execution contexts.
> 表内引用（1 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › SQIT  -  SeQuencer InterRupt）

```
> SQSL "test1"
> SQST RUN
> SQIT?
< SQIT TIMEOUT, (pin1)
```

In this example, a timeout was observed on `pin1`.

### SQLA（取自子主题 Commands in alphabetical order › List of commands › SQLA  SQLA  -  SeQuencer Label Attribute）

```
SQLA [type],{"name"},{"attr_key_1=[attr_val_1] [,attr_key_2=[attr_val_2] [,attr_key_3=[attr_val_3]]]"} [,(port)]
```

### SQLA?（取自子主题 Commands in alphabetical order › List of commands › SQLA  SQLA  -  SeQuencer Label Attribute）

```
SQLA? [type], {"name"|ALL}, {"attr_key"|ALL|SAVE} [, (portlist)]
```

returns:

```
SQLAtype, {"name"},{"attr_key_1=attr_val_1, attr_key_2=attr_val_2} [,attr_key_3=attr_val_3]" [,(port)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SQLA  SQLA  -  SeQuencer Label Attribute）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/103621.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：type | Currently, LBL is the only possible value. This is also the default.
> 表内引用（2 条，供检索）：`Selecting the memory type`（raw: `02.06.07.01.04.01_Selecting_the_memory_type.md`） · `Defining a compliance pattern for pattern‑based SmartLoop testing`（raw: `02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › SQLA  SQLA  -  SeQuencer Label Attribute）

```
> APTS LBL,"test","table1"
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,10,5,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,16,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
> SQLA ,"test","PARA_MEM=SHMEM"
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,10,5,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,0,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
```

This example changes the PARA_MEM attribute of the new label test from SM to SHMEM. Note the change of the address in command line 4.

### SQLB（取自子主题 Commands in alphabetical order › List of commands › SQLB  SQLB  -  SeQuencer LaBel definition）

```
SQLB {"label"}, {type}, {start_cmd_no}, {stop_cmd_no}, [base_wf_set|"wavetable_name"| "sync_grp"] [, (port)]
```

### SQLB（取自子主题 Commands in alphabetical order › List of commands › SQLB  SQLB  -  SeQuencer LaBel definition）

```
SQLB? {"label"|ALL}, {type|ALL}[, (portlist)]
```

returns:

```
SQLB {label}, {type}, {start_cmd_no}, {stop_cmd_no}, {"wavetable_name"|base_wf_set| "sync_grp"} [,(port)]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98748.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：19 行 × 3 列。
> 首行（上游原文）：label | The label name. It identifies the label which is to be defined for the specified port, or whose definition is to be displayed. Enter a string enclosed i…
> 表内引用（4 条，供检索）：`SmarTest character and number limits`（raw: `../../01_Getting_started/01.05_SmarTest_character_and_number_limits/01.05_SmarTest_character_and_number_limits.md#_128029__max_labels_per_port`） · `SQSL`（raw: `02.06.02.02.240_SQSL__SQSL__-__SeQuencer_Start_Label.md`） · `Burst and Multi-Burst Labels`（raw: `02.06.07.01.08.05.03_Burst_labels_and_multi-port_burst_labels.md`） · `DVCU, DVCU? - (Define Vector variable Configuration Usage`（raw: `02.06.02.02.96_DVCU__DVCU__-__Define_Vector_variable_Configuration_Usage.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › SQLB  SQLB  -  SeQuencer LaBel definition）

This example defines a burst label for the default port.

Display the whole sequencer area:

```
> SQPG? ALL,(@)
< ...
< SQPG 8,STOP,,,,(@)
```

The sequencer area comprises nine command lines. Three further lines are required for the rudimentary burst label. Thus, issue:

```
> DMAS SQPG,SM,12,(@)
```

Define the label:

```
> SQLB "burst_1",BRST,9,11,"gross_func_wtb",(@)
```

Display the whole sequencer area again:

```
> SQPG? ALL,(@)
< ...
< SQPG 8,STOP,,,,(@)
< SQPG 9,NOP,,,,(@)
< SQPG 10,NOP,,,,(@)
< SQPG 11,BEND,,,,(@)
```

You can now replace the NOP instructions in command lines 9 and 10 by CALL instructions with the SQPG command.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › SQLB  SQLB  -  SeQuencer LaBel definition）

This example queries all labels of all types for the default port.

```
> SQLB? ALL,ALL
< SQLB "test_1",MAIN,0,4,"spec_search_wtb"
< SQLB "test_2",MAIN,5,8,"spec_search_wtb"
< SQLB "burst_1",BRST,9,11,"gross_func_wtb"
```

### Example 3（取自子主题 Commands in alphabetical order › List of commands › SQLB  SQLB  -  SeQuencer LaBel definition）

This example renames the burst label `burst_1`, defined in example 1, to "BURST1".

```
> SQLB "BURST1",BRST,9,11,"gross_func_wtb"
> SQLB? ALL,BRST
< SQLB "BURST1",BRST,9,11,"gross_func_wtb"
```

### Example 4（取自子主题 Commands in alphabetical order › List of commands › SQLB  SQLB  -  SeQuencer LaBel definition）

This example illustrates the relative numbering of the command lines in SAOF APP mode.

```
> SAOF?
< SAOF ZERO
> SQLB? ALL,ALL
< SQLB "L_1",MAIN,0,2,"wf1"
> SAOF APP
> DMAS SQPG,SM,3,(@)
> SQLB "L_2",MAIN,0,2,"wf1"
> SAOF ZERO
> SQLB? ALL,ALL
< SQLB "L_1",MAIN,0,2,"wf1"
< SQLB "L_2",MAIN,3,5,"wf1"
```

### SQPG（取自子主题 Commands in alphabetical order › List of commands › SQPG  SQPG  -  SeQuencer ProGramming）

```
SQPG {cmd_No}, {instr}, [param_1], [param_2], [memory], {(port)}
```

### SQPG?（取自子主题 Commands in alphabetical order › List of commands › SQPG  SQPG  -  SeQuencer ProGramming）

```
SQPG? {cmd_No|ALL|"cmd_No_A,cmd_No_B"}, {(portlist)}
```

returns:

```
SQPG {cmd_No}, {instr}, [param_1], [param_2], [memory], {(port)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98749.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：44 行 × 3 列。
> 首行（上游原文）：cmd_No | The command number. This parameter identifies the instruction within the sequencer area of the specified port. Refer to Address instructions for furthe…

### Example 1（取自子主题 Commands in alphabetical order › List of commands › SQPG  SQPG  -  SeQuencer ProGramming）

The following is a simple example of a counted match loop:

```
SQPG 3,MACT,256,CONTINUE,,(@)
SQPG 4,GENV,5,,,(@)
SQPG 5,MRPT,5,,,(@)
```

Note that only the GENV or RPTV instruction is allowed immediately before the MACT instruction. CONTINUE, which is optional, tells SmarTest to continue the surrounding test even if the match loop failed.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › SQPG  SQPG  -  SeQuencer ProGramming）

The following example shows that inserting a GENV instruction into a label with SQPG disturbs the sequencer constructs and must be accompanied by an appropriate adjustment of the vector areas (see also `Inserting a sequencer instruction`（raw: `02.06.07.01.07.03.01_Inserting_a_sequencer_instruction.md`）).

Display the sequencer area of the default port:

```
> SQPG? ALL,(@)
< ...
< SQPG 4,STVA,504,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,GENV,9,,,(@)
< SQPG 7,STOP,,,,(@)
< SQPG 8,STVA,520,,,(@)
< ...
```

The vector area segment of the label starting at command 4 comprises 2 memory words, as shown by the start address of the following label (command line 8).

Now display the vector area segment of pin S0_1 for the label starting at command 4, and also the first memory word of the following label:

```
> $VECD? PARA,SM,504,24,(S0_1)
< VECD PARA,SM,504,16,(S0_1),
 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001
 0000 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
 0000 0010 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
```

The GENV instruction is associated with the first two memory words. The last 7 bytes of the second word are padding vectors. This is shown by making the first label the start label and then displaying the active vectors of command 6 for pin `S0_1`:

```
> SQSL "test_1"
> $VCYC? 0,9,(S0_1)
< VCYC 0,9,GENV,F160,(S0_1),
 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001
 0000 0001
```

Now insert a GENV instruction before command 6:

```
> TSTL "test_1",
> INSI 6,1
> SQPG 6,GENV,1,,,(@)
```

Display the active vectors for the two GENV instructions:

```
> $VCYC? 0,10,(S0_1)
< VCYC 0,1,GENV,F160,(S0_1), 0000 0001
< VCYC 1,9,GENV,F160,(S0_1),
 0000 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
 0000 0010
```

The first memory word is now associated with the new instruction. The first of its vectors is active, the others are inactive. The previous command 6 (now command 7) is now associated with the second and the third block. Thus the third memory word is illegally shared between two labels.

### SQRC（取自子主题 Commands in alphabetical order › List of commands › SQRC -  SeQuencer Remove execution Context）

```
SQRC {"context_name"|ALL}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SQRC -  SeQuencer Remove execution Context）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/137547.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：context_name | The name of the context to be removed.

### Example（取自子主题 Commands in alphabetical order › List of commands › SQRC -  SeQuencer Remove execution Context）

```
> SQRC "c1"
```

### SQRP（取自子主题 Commands in alphabetical order › List of commands › SQRP  SQRP  -  SeQuencer Reference Port）

```
SQRP {(port)}
```

### SQRP?（取自子主题 Commands in alphabetical order › List of commands › SQRP  SQRP  -  SeQuencer Reference Port）

```
SQRP?
```

returns:

```
SQRP {(port)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SQRP  SQRP  -  SeQuencer Reference Port）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98750.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：port | This parameter specifies the reference port.

### Example（取自子主题 Commands in alphabetical order › List of commands › SQRP  SQRP  -  SeQuencer Reference Port）

The following example synchronizes two ports RX and TX, each of which is the only port in its sequencing group. The RX port does not admit any changes of primary sets, the TX port must change its primary sets several times during the testflow. This is implemented by the `FTCG`（raw: `02.06.02.02.125_FTCG__FTCG__-__Functional_Test_ConfiGure.md`） command as follows:

```
> FTCG SKPR,OFF,(@@)
> FTCG SKPR,ON,(RX)
```

In order to synchronize both ports, the time span used up by the activation sequences in TX must be filled with break vectors in RX. If both ports operate with the same period length, and the PHASE flag is set for both of them in the multi-port timing specification, then the number of break vectors that compensates the different types of activation sequences will always be a multiple of 8. The exact number must be determined by empirical tests. The required numbers could then be passed to SQBV as follows:

```
> SQBV ,1504,TIM,(RX)
> SQBV ,22048,TIM_LEV,(RX)
> SQBV ,31784,ALL,(RX)
```

The reference port is TX. This is specified by

```
> SQRP (TX)
```

Finally, the timing changes in TX may include moving receive edges across cycle boundaries, and this in turn can (in rare cases) prolong the activation sequence for the next functional test. But this is not acceptable, because only one value can be passed to SQBV for every activation sequence type. In order to secure that the length of an activation sequence is not affected by the timing of the preceding test, break vectors can be inserted in TX before the last activation of the respective sequence type, so that the sequence as a whole has the extended length even if no cycle crossing takes place in the previous test.

The required number of break vectors must again be determined by measurements. The required number of vectors could then be defined as follows:

```
> SQBV 128,,TIM,(TX)
> SQBV 128,,TIM_LEV,(TX)
> SQBV 128,,ALL,(TX)
```

Note that in this case the insertion port is identical with the reference port.

### SQSL（取自子主题 Commands in alphabetical order › List of commands › SQSL  SQSL  -  SeQuencer Start Label）

```
SQSL  {"label"} [, site|"site_string"]
```

### SQSL?（取自子主题 Commands in alphabetical order › List of commands › SQSL  SQSL  -  SeQuencer Start Label）

```
SQSL?
```

returns:

```
SQSL {"label"}
```

With the TYPE option:

```
SQSL?TYPE
```

returns:

```
SQSL {"label"}, {type}, {(portlist)}
```

With the ALL option:

```
SQSL?ALL
```

returns:

```
SQSL {"label"}, {"site_string"}, {type}, {(portlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98751.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：label | The name of a sequencer start label. In the command, you can enter an empty string ("") to deactivate the current start label.

### Example 1（取自子主题 Commands in alphabetical order › List of commands › SQSL  SQSL  -  SeQuencer Start Label）

```
> SQSL "test_1"
> SQSL? TYPE
< SQSL "test_1",MAIN,(@)
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › SQSL  SQSL  -  SeQuencer Start Label）

```
> PSFC 2
> SQSL "test_1"
> SQSL? ALL
< SQSL "test_1","11",MAIN,(@)
> SQSL "test_2", "10"
> SQSL "test_3", 2
> SQSL? ALL
< SQSL "test_2","10",MAIN,(@)
< SQSL "test_3","01",MAIN,(@)
> SQSL?
< SQSL "test_2"
> PQFC 2
> SQSL?
< SQSL "test_3"
```

This example illustrates the definition of different start labels for different sites. Note that the restriction of the setup focus has no influence on the command, but that the setting of the query focus does affect SQSL?.

### SQST（取自子主题 Commands in alphabetical order › List of commands › SQST  SQST  -  SeQuencer STate）

SQST {seq_state} [,"exec_context"]

### SQST?（取自子主题 Commands in alphabetical order › List of commands › SQST  SQST  -  SeQuencer STate）

```
SQST? ["exec_context"]
```

returns:

```
SQST {seq_state}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SQST  SQST  -  SeQuencer STate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98752.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：seq_state | Gives the state of the sequencer:
> 表内引用（2 条，供检索）：`SQGB, SQGB? - (SeQuencer GloBal)`（raw: `02.06.02.02.232_SQGB__SQGB__-__SeQuencer_GloBal.md`） · `Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › SQST  SQST  -  SeQuencer STate）

```
SQST RUN
```

This example starts a global sequencer run.

### SQTO（取自子主题 Commands in alphabetical order › List of commands › SQTO  SQTO  -  SeQuencer TimeOut）

```
SQTO {timeout}             // in seconds
```

### SQTO?（取自子主题 Commands in alphabetical order › List of commands › SQTO  SQTO  -  SeQuencer TimeOut）

```
SQTO?
```

returns:

```
SQTO {timeout}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SQTO  SQTO  -  SeQuencer TimeOut）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98753.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：timeout | Defines the time (in seconds) that the sequencer runs. The default value is 900 and the range is 0.001 to 2147483.

### Example（取自子主题 Commands in alphabetical order › List of commands › SQTO  SQTO  -  SeQuencer TimeOut）

```
SQTO 3000
```

This example programs the sequencer to exit after 50 minutes.

### SREC（取自子主题 Commands in alphabetical order › List of commands › SREC  SREC  -  Set RECeiver mask）

```
SREC {mask_value}, {(pinlist)}
```

### SREC?（取自子主题 Commands in alphabetical order › List of commands › SREC  SREC  -  Set RECeiver mask）

```
SREC? {(pinlist)}
```

Note Executing `SREC ACT,(@)` may cause excessive overhead. You can use the `UI_SUSPEND`（raw: `../02.07_Test_Method_Reference/02.07.04.01.260_UI_SUSPEND.md`） test method API to suspend updates of the graphical user interface.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SREC  SREC  -  Set RECeiver mask）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98754.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：mask_value | The mask value parameter specifies whether a pin mask will be applied:
> 表内引用（2 条，供检索）：`DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） · `DFGE, DFGE? - (DeFine Group Expressions)`（raw: `02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › SREC  SREC  -  Set RECeiver mask）

```
SREC X, (D1, D2, D3, D4)
```

This example masks the pins D1, D2, D3 and D4.

### SRPR（取自子主题 Commands in alphabetical order › List of commands › SRPR  SRPR  -  Set Routing PRimary）

```
SRPR {set}
```

### SRPR?（取自子主题 Commands in alphabetical order › List of commands › SRPR  SRPR  -  Set Routing PRimary）

SRPR?

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SRPR  SRPR  -  Set Routing PRimary）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99079.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：set | An identification number of the routing set. This is an integer from 1 to the maximum number defined by the DSCP command. If the NONE specifier is specifi…

### Example（取自子主题 Commands in alphabetical order › List of commands › SRPR  SRPR  -  Set Routing PRimary）

```
SRPR 4
```

This example sets the routing set 4 as the primary routing set.

### SSAC（取自子主题 Commands in alphabetical order › List of commands › SSAC  SSAC  -  Source Synchronous testing  Add Configuration）

```
SSAC [read_mode],[nr_of_results],[(ref_pin}],{(pinlist)}
```

### SSAC?（取自子主题 Commands in alphabetical order › List of commands › SSAC  SSAC  -  Source Synchronous testing  Add Configuration）

```
SSAC?
```

returns:

```
SSAC {read_mode},[nr_of_results],[(ref_pin}],{(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SSAC  SSAC  -  Source Synchronous testing  Add Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98755.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：read_mode | Possible read modes are:

### Example（取自子主题 Commands in alphabetical order › List of commands › SSAC  SSAC  -  Source Synchronous testing  Add Configuration）

The following example shows how the buffer channels are configured by using a reference pin:

```
> DCGM ALL,STRT,NONE
> DCRT RAM,(@)
> SSRC (@)
> SVLR TIM,1,1,"sweep",2.4
> FTST?
> SSAC INV,,(D1),(SB)
> SSAC NORM,,(D1),(G1,G2)
> SSCT IMM,NORM,,(SB),(D1,D2,D3,CL)
> SSCT ACC,NORM,,(G1),(SB)
> SVLR TIM,1,1,"sweep",2.5
> FTST?
. . .
```

First the detailed Error Map is configured for source synchronous testing (recording mode ALL, location in RDRAM). Next the existing buffer configurations are removed. Then the sweep variable is set, and the first functional test executed. Subsequently the buffer channels are configured using D1 as the reference pin. Then the results of the first functional test are processed. Finally, the sweep variable is incremented and the next functional test executed.

### SSCT（取自子主题 Commands in alphabetical order › List of commands › SSCT  SSCT  -  Source Synchronous data  Combine and Transfer）

```
SSCT {exec_mode},[read_mode],[nr_of_results],{(dest_pin)}, {(source_pins)}
```

### SSCT?（取自子主题 Commands in alphabetical order › List of commands › SSCT  SSCT  -  Source Synchronous data  Combine and Transfer）

```
SSCT? {(dest_pins)}
```

returns:

```
SSCT {exec_mode},{read_mode},{nr_of_results},{(dest_pin)}, {(source_pins)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98756.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 3 列。
> 首行（上游原文）：exec_mode | Possible execution modes are:

### Example（取自子主题 Commands in alphabetical order › List of commands › SSCT  SSCT  -  Source Synchronous data  Combine and Transfer）

The following example shows a typical start sequence of a source synchronous test:

```
> DCGM ALL,STRT,NONE
> DCRT RAM,(@)
> SSRC (@)
> SSAC INV,128,,(SB)
> SSAC NORM,128,,(G1,G2)
> SVLR TIM,1,1,"sweep",2.4
> FTST?
> SSCT IMM,NORM,128,(SB),(D1,D2,D3,CL)
> SSCT ACC,NORM,128,(G1),(SB)
> SVLR TIM,1,1,"sweep",2.5
> FTST?
> SSCT IMM,NORM,128,(SB),(D1,D2,D3,CL)
> SSCT ACC,NORM,128,(G2),(SB,G1)
. . .
```

At first, the detailed Error Map is configured for the requirements of result buffering (error map located in RDRAM, recording mode ALL). After the first functional test the results of the data pins D1 through D3 and the output clock pin CL are immediately combined and transferred into the source buffer SB. The subsequent transfer into the first global buffer is delayed and will only be triggered by the next FTST? call. After the second functional test, the SSCT ACC call combines the results of the source buffer and the first global buffer into the second global buffer.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › SSRC -  Source Synchronous testing  Remove Configurations）

```
SSRC {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SSRC -  Source Synchronous testing  Remove Configurations）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98758.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pinlist | The pins whose buffer configurations are to be removed. Pins for which no buffer configuration exists are ignored.

### Example（取自子主题 Commands in alphabetical order › List of commands › SSRC -  Source Synchronous testing  Remove Configurations）

```
> SSRC (@)
```

This example removes all buffer configurations. Pins for which no buffer has been configured are ignored.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › SSTR  -  Source Synchronous Testing  Result query）

```
SSTR? [ALL_SITES,] {GLO|INV},{(pinlist)}
```

returns:

```
SSTR {GLO|INV},{(pinlist)},{glob_res}
```

Or:

```
SSTR? {DET},{(pin)}
```

returns:

```
SSTR {DET},{(pin)},{#spec(data)}}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98759.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：ALL_SITES | This parameter causes SSTR? to return a global result for all sites. If it is omitted, the result for that site is returned that currently has the r…

### Example（取自子主题 Commands in alphabetical order › List of commands › SSTR  -  Source Synchronous Testing  Result query）

The following example assumes that the global buffer pins G2 and G4 contain the total results of two source synchronous tests that were run in parallel:

```
> SSTR? INV,(G2)
< SSTR INV,(G2),P
> SSTR? INV,(G4)
< SSTR INV,(G4),F
> $SSTR? DET,(G4)
< SSTR DET,(G4),#9000000008,0000 0000  0001 0000  0000 0000  0000 0100  0000 0000  0000 0000  0000 0000  0000 0000
> SSTR? INV,(G2,G4)
< SSTR INV,(G2,G4),F
```

Note that the result granularity has been set to 8, so that every bit of the SSTR DET reply represents one receive edge. Note also that SSTR DET simply returns the buffer content. Since the global buffers must represent FAIL by 1 and PASS by 0, the reply indicates that one edge in the second cycle and one edge in the fourth cycle have failed in all shots for one of the two tests. All other edges have passed at least in one shot.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › STDE -  Save Test Data Entity）

STDE

### Example（取自子主题 Commands in alphabetical order › List of commands › STDE -  Save Test Data Entity）

```
STDE
```

### STME（取自子主题 Commands in alphabetical order › List of commands › STME  STME  -  SiTe Match Enable）

```
STME {ON|OFF|AUTO|FAST},
```

### STME?（取自子主题 Commands in alphabetical order › List of commands › STME  STME  -  SiTe Match Enable）

```
STME?
```

returns:

STME {ON|OFF|FAST),

### Parameters（取自子主题 Commands in alphabetical order › List of commands › STME  STME  -  SiTe Match Enable）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98760.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：ON | Turns the site match function on.
> 表内引用（1 条，供检索）：`Fast Sync`（raw: `02.06.07.01.08.04.03.03_Fast_Sync.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › STME  STME  -  SiTe Match Enable）

```
> STME AUTO,
> STME?
< STME ON,
```

This example sets the site match function to AUTO, then reads the actual setting. Since the actual setting is ON, the pin configuration cannot contain a shared digital channel.

```
>SQST OFF
>NIFE 2
>STME FAST,
>STME ON,
```

This example configures the Fast Sync feature, and sets two independent Fast Sync ports on each test processor.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › STRS  -  Spec TRansition Search）

```
STRS? ["exec_context",] [start], [stop], {mode}, [(pinlist)], {spec_type}, {"spec_name[@port[@UNCHANGED]]"}, [stepwidth], {resolution}
```

returns:

```
STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › STRS  -  Spec TRansition Search）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98762.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts .
> 表内引用（4 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） · `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`） · `Modifying the period for a search or shmoo in a multi-port setup`（raw: `02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › STRS  -  Spec TRansition Search）

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › SVLR  SVLR  -  Spec VaLues at Runtime）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98764.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:
> 表内引用（1 条，供检索）：`Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The following example queries the values of the spec variable f in a setup where both single-port and multi-port specifications occur:

```
> SVLR? TIM,ALL,ALL,"f"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",35
< SVLR TIM,,"spec_p_1_p_2","f@p_2",33
< SVLR TIM,1,1,"f",37
```

### Example 2（取自子主题 Commands in alphabetical order › List of commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The next example queries in which equation sets the spec variable f occurs:

```
> SVLR? TIM,ALL,,"f"
< SVLR TIM,1,,"f",
< SVLR TIM,2,,"f",
```

### Example 3（取自子主题 Commands in alphabetical order › List of commands › SVLR  SVLR  -  Spec VaLues at Runtime）

For this example assume that the primary timing is a multi-port specification which contains the two ports p_1 and p_2, and that p_1 and p_2 share the spec variable f in this specification. Assume further that f has been set to scope global for the port p_1. Now query the current value of f for p_1, change it globally, and query it again:

```
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",33
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",43
```

Since f is global for p_1, its value has been modified. Now change the value a second time, but this time locally, and then try to change it globally again:

```
> SVLR TIM,PRM,,"f@p_1",53
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",53
```

The second global command has no effect because f has only local scope after issuing the local command.

### TCMT（取自子主题 Commands in alphabetical order › List of commands › TCMT  TCMT  -  Test CoMment Transfer）

```
TCMT {vect_addr}, {"text"}
```

### TCMT?（取自子主题 Commands in alphabetical order › List of commands › TCMT  TCMT  -  Test CoMment Transfer）

```

TCMT? {vect_addr}, [vect_length]
```

returns a comment text for each TCMT in the range vect_addr to vect_addr `+`vect_length `- 1`.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TCMT  TCMT  -  Test CoMment Transfer）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98767.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：vect_addr | The logical number of the vector at which the comment is to be inserted or read. The specified number range must not exceed the maximum vector addre…

### Example（取自子主题 Commands in alphabetical order › List of commands › TCMT  TCMT  -  Test CoMment Transfer）

```
TCMT 2063,"Start of test 2".
```

This example inserts the comment "Start of test 2" at the logical vector address 2063.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TDEX  Test Data Extension）

Italic text in the syntax descriptions below indicates meta-syntax, as described in `Syntax conventions`（raw: `../02.12_Memory_Test_Plus_7.10.2/02.12.03.01.02_Syntax_conventions.md`）.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TDEX  Test Data Extension）

The attributes used in the XML data, grouped by element (elements are in alphabetical order):

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118015.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 2 列。
> 首行（上游原文）：apgFile | name: <apgFilePath>, a string, is the path to the compiled APG program file.
> 表内引用（5 条，供检索）：`APG program file`（raw: `../02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.md`） · `Device architecture file syntax`（raw: `../02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05.01_Device_architecture_file_syntax.md`） · `Pin mapping file syntax`（raw: `../02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.01_Pin_mapping_file_syntax.md`） · `apgc command syntax`（raw: `../02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md`） · `Macros and functions in program files`（raw: `../02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TDEX  Test Data Extension）

```
TDEX "::pattern::mtl::hsm","myLabel",#9000003254<?xml version="1.0" encoding="ISO8859-1" standalone="no" ?>
<testDataExtension
                   xsi:noNamespaceSchemaLocation="TestDataExtension.xsd">

  <pinMap>
    <pin id="0" name="pin0" xmode="2">
      <capabilities>
        <digital refInsertionCtrl="VEC"/>
      </capabilities>
    </pin>
    <pin id="1" name="pin1" xmode="4">
      <capabilities>
        <digital refInsertionCtrl="SEQ"/>
      </capabilities>
    </pin>
    <pin id="2" name="pin2" xmode="6">
      <capabilities>
        <digital refInsertionCtrl="SEQ"/>
      </capabilities>
    </pin>
    <pin id="3" name="pin3" xmode="8">
      <capabilities>
        <digital refInsertionCtrl="VEC"/>
      </capabilities>
    </pin>
    <pin id="4" name="pin4">
      <capabilities>
        <digital refInsertionCtrl="SEQ"/>
      </capabilities>
    </pin>
    <pin id="5" name="pin5" xmode="4">
      <capabilities>
        <digital refInsertionCtrl="SEQ"/>
      </capabilities>
    </pin>
  </pinMap>

  <mtlPattern>
    <sourceFiles>
      <apgFile name="/data/device/mts/pattern_defs/apg_file_name_create.apg"/>
    </sourceFiles>
    <setupConfiguration>
      <scramble name="scramble_1"/>
      <bitInversion name="bitInversion_1"/>
      <bitOrdering name="bitOrdering_1"/>
      <dbi name="dbi_1"/>
      <crc name="crc_1"/>
    </setupConfiguration>
    <deviceMaintenance>
      <refresh>
        <timer id="0" intervalMode="accumulated" refreshCtrl="none" timerMode="dynamic"/>
        <timer id="1" intervalMode="compensated" refreshCtrl="start" timerMode="static"/>
        <timer id="2" intervalMode="accumulated" refreshCtrl="none" timerMode="static"/>
        <timer id="3" intervalMode="unknown" refreshCtrl="start" timerMode="unknown"/>
      </refresh>
    </deviceMaintenance>
    <consistencyCheck>
      <sequencerProgram checkSum="21845"/>
    </consistencyCheck>
    <reconstruction>
      <pins>
        <pin id="0"/>
        <pin id="1"/>
        <pin id="2"/>
      </pins>
    </reconstruction>
    <errorCorrection>
      <layer id="0" type="dbi">
        <bus>
          <pins>
            <pin id="0"/>
            <pin id="1"/>
            <pin id="2"/>
          </pins>
          <flags>
            <pin id="3"/>
          </flags>
        </bus>
        <bus>
          <pins>
            <pin id="10"/>
            <pin id="11"/>
            <pin id="12"/>
          </pins>
          <flags>
            <pin id="13"/>
          </flags>
        </bus>
      </layer>
      <layer id="1" type="other">
        <bus>
          <pins>
            <pin id="100"/>
            <pin id="101"/>
          </pins>
          <flags>
            <pin id="103"/>
          </flags>
        </bus>
        <bus>
          <pins>
            <pin id="110"/>
            <pin id="111"/>
          </pins>
          <flags>
            <pin id="113"/>
          </flags>
        </bus>
      </layer>
    </errorCorrection>
    <compilation>
      <options expansionSize="100"
               limitVariableScope="false"
               reconstructionLevel="2"
               reusableMaintenance="true"
               wavetableGeneration="false"/>
    </compilation>
  </mtlPattern>

</testDataExtension>
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TEMP  -  read TEMPerature）

```
TEMP? [cardType]
```

returns:

```
TEMP {cardType}, {cardId}, {temperature}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TEMP  -  read TEMPerature）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98770.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：cardType | Specifies the card type for which temperature is read

### Example（取自子主题 Commands in alphabetical order › List of commands › TEMP  -  read TEMPerature）

```
TEMP? DIGIO
TEMP DIGIO,101,292.3
TEMP DIGIO,102,292.3
```

### TERM（取自子主题 Commands in alphabetical order › List of commands › TERM  TERM  -  TERMination mode）

```
TERM {level_set_no | level_set_id}, [term_mode], [term_pulldown,] [param_1], [param_2], [param_3],
 [l_range], [h_range], [hr_mode,] {(pinlist)}
```

### TERM?（取自子主题 Commands in alphabetical order › List of commands › TERM  TERM  -  TERMination mode）

```
TERM? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
TERM {level_set_no | level_set_id}, {term_mode}, [term_pulldown,] [param_1], [param_2], [param_3],
 [l_range], [h_range], [hr_mode,] {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TERM  TERM  -  TERMination mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98771.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：level_set_no | The identification number of the level set in which you want the definitions to be included. The number must not exceed the maximum number of lev…
> 表内引用（3 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `LSUS`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`） · `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`）

### Example 1（取自子主题 Commands in alphabetical order › List of commands › TERM  TERM  -  TERMination mode）

```
TERM 1,T,-1500,,,,,(Q1)
```

This example terminates the output pin Q1 to -1500 mV in level set 1.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › TERM  TERM  -  TERMination mode）

```
TERM 3,A,3000,1500,1000,I3E4,I3E4,(out)
```

This example sets the active load level of the pin group out to 3V, and sets Iol and Ioh current to 1.5 and 1.0 mA respectively. The 0 to 30 mA range is used for both the low and the high range.

### Example 3（取自子主题 Commands in alphabetical order › List of commands › TERM  TERM  -  TERMination mode）

```
TERM 1,CT,2000,,,,,(o1,o1-)
```

This example terminates the differential output pair (the o1 and o1- pins) to 2000 mV with center tap termination in level set 1.

### Example 4（取自子主题 Commands in alphabetical order › List of commands › TERM  TERM  -  TERMination mode）

```
TERM 1,OFF,PULLDOWN,,,,,,(Q1,Q2)
```

On a PS1600 card, this example switches on the pulldown resistor on the specified pins.

```
TERM 1,OFF,NONE,,,,,,(Q1,Q2)
```

On a PS1600 card, this example switches off the pulldown resistor on the specified pins.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TMUD  Tester Memory Utilization set Default values）

```
TMUD {client}, [logState],{(portlist)}
```

Parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125642.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 5 列。
> 首行（上游原文）：Parameter | Description

### Example（取自子主题 Commands in alphabetical order › List of commands › TMUD  Tester Memory Utilization set Default values）

```
> TMUD PROTOCOLTEST,ON,(mdioPort)

> TMUL? ALL,ALL,(mdioPort)
< TMUL PROTOCOLTEST,CACHE,"0,0,0",(mdioPort)
< TMUL PROTOCOLTEST,SIZE,"0,0,AUTO",(mdioPort)
```

In this example the TMUD resets the memory utilization logs of the mdioPort of the PROTOCOLTEST client. It also sets logging to ON in case it was disabled previously.

The TMUL? query is used to display that TMUD has reset all memory utilization counters to default values.

```
> TMUD ALL,ON,(@@)

> TMUL? ALL,ALL,(@@)
< TMUL PROTOCOLTEST,CACHE,"0,0,0",(mdioPort)
< TMUL PROTOCOLTEST,CACHE,"0,0,0",(otherPort)
< TMUL PROTOCOLTEST,SIZE,"0,0,65536",(mdioPort)
< TMUL PROTOCOLTEST,SIZE,"0,0,AUTO",(otherPort)
```

In this example the TMUD resets the memory utilization logs of all ports (@@) of all clients. It also sets logging to ON in case it was disabled previously for all ports and clients.

The TMUL? query is used to display that TMUD has reset all memory utilization counters to default values.

Note If the memory size was specified by `PROTOCOL_TEST::reserveTransactionMemory()` the according limit will be displayed, else AUTO is shown.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TMUL   Tester Memory Utilization Log）

TMUL? {client}, {type},{(portlist)}

returns

TMUL {client}, {type}, {"reportString"}, {(portlist)}

Parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125641.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：Name | Description

### Example（取自子主题 Commands in alphabetical order › List of commands › TMUL   Tester Memory Utilization Log）

The following example queries the `mdioPort` for details about the CACHE of the PROTOCOLTEST client. The returned string shows that entries have been found 1560 times in the cache (number of hits). It also shows that 28 entries had been added (number of misses) to the cache and no entry has been removed.

```
> TMUL? PROTOCOLTEST,CACHE,(mdioPort)
< TMUL PROTOCOLTEST,CACHE,"1560,28,0",(mdioPort)
```

The next example queries the `mdioPort` for ALL details of ALL clients. The returned strings shows the results for CACHE  and SIZE. With regards to SIZE, one can see that the minimum memory size required to store the generated data is 7488 bytes. It also shows that the maximum memory size utilized during testing was 10314 bytes and that there is no limit set, thus AUTO is displayed.

```
> TMUL? ALL,ALL,(mdioPort)
< TMUL PROTOCOLTEST,CACHE,"1560,28,0",(mdioPort)
< TMUL PROTOCOLTEST,SIZE,"7488,10314,AUTO",(mdioPort)
```

This example queries all ports (@@)`` for ALL details of ALL client.

```
> TMUL? ALL,ALL,(@@)
< TMUL PROTOCOLTEST,CACHE,"1560,28,0",(mdioPort)
< TMUL PROTOCOLTEST,CACHE,"0,0,0",(otherPort)
< TMUL PROTOCOLTEST,SIZE,"7488,10314,AUTO",(mdioPort)
< TMUL PROTOCOLTEST,SIZE,"0,0,AUTO",(otherPort)
```

### TOCF（取自子主题 Commands in alphabetical order › List of commands › TOCF  TOCF  -  Timing Level Offset search ConFiguration）

```
TOCF [search_type], {resource_type}, {start}, {number_of_steps}, {step_width}, {resolution}, [min_pass_count], [min_stable_error_count,] [histogram_step_width,] [transition_detection], [error_count_limit], [restore_flag], {(setup_pinlist)}
```

### TOCF?（取自子主题 Commands in alphabetical order › List of commands › TOCF  TOCF  -  Timing Level Offset search ConFiguration）

```
TOCF? {(pinlist)}
```

returns:

```
TOCF {search_type} {resource_type}, {start}, {number_of_steps}, {step_width}, {resolution}, {min_pass_count}, {min_stable_error_count}, {histogram_step_width}, {transition_detection}, {error_count_limit}, {restore_flag}, {(setup_pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TOCF  TOCF  -  Timing Level Offset search ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124942.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：35 行 × 3 列。
> 首行（上游原文）：search_type | This parameter defines which value of the search result is to be stored as an offset to the edge positions of the current primary timing. Possible…
> 表内引用（1 条，供检索）：`Linear search modes`（raw: `02.06.09.01.02.01_Linear_search_modes.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TOCF  TOCF  -  Timing Level Offset search ConFiguration）

```
TOCF EYE,R,1,100,1,0.1,5,PF,,NO,(Pin1)
```

This example appends a check for 5 consecutive pass results to the result of the binary search.

```
TOCF EYE,R,1,100,1,0.1,1,10,0.1,ECL,7,NO,(Pin1)
```

This example appends a histogram based search to the binary search. The histogram based search is terminated if the error count is stable for 10 consecutive search steps. A test is considered passed if the number of errors is smaller than 7.

### TOCR（取自子主题 Commands in alphabetical order › List of commands › TOCR  TOCR  -  Timing level Offset Configure Result pins）

```
TOCR [(result_pinlist)], {(setup_pin)}
```

### TOCR?（取自子主题 Commands in alphabetical order › List of commands › TOCR  TOCR  -  Timing level Offset Configure Result pins）

```
TOCR? {(result_pinlist)},
```

or

```
TOCR? , {(setup_pinlist)}
```

Both formats return:

```
TOCR {(result_pinlist)}, {(setup_pin)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TOCR  TOCR  -  Timing level Offset Configure Result pins）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125396.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：result_pinlist | In the command, this parameter specifies the result pins for the setup pin specified with setup_pin. It can be omitted for O or IO setup pins. …

### Example（取自子主题 Commands in alphabetical order › List of commands › TOCR  TOCR  -  Timing level Offset Configure Result pins）

```
TOCR (Pin2,Pin3),(Pin1)
```

This example defines `Pin2` and `Pin3` as the result pins for `Pin1`.

```
> TOCR? ,(Pin1,Pin5)
< TOCR (Pin2,Pin3),(Pin1)
```

This example queries the result pins for Pin1 and Pin5. No reply is given for setup pin Pin5, because its result pin is also Pin5.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TORC -  Timing level Offset Result Copy）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125054.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：source_waveform_set | Number of the source waveform set. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed w…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `SPRM`（raw: `02.06.02.02.228_SPRM__SPRM__-__Set_PRiMary_sets.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TORC -  Timing level Offset Result Copy）

Example 1: copies the offsets of timing set 2 of single port specification 102 to the primary timing set of the primary specification.

```
TORC 102,2,PRM,PRM,(Pin1,Pin2)
```

Example 2: copies all level_set offsets of level set 1 to all the other level sets for all pins (@).

```
> TORC 1,,ALL,,(@)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TORN  -  Timing level Offset search RuN）

```
TORN? {(pinlist)} [,"exec_context"]
```

Returns:

```
TORN {status}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TORN  -  Timing level Offset search RuN）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125309.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：pinlist | The pins for which the embedded search is to be executed. You can specify @ for all pins. Note the difference between a list of pins and @ in a multi-…
> 表内引用（1 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TORN  -  Timing level Offset search RuN）

```
> TORN? (Pin1,Pin2)
< TORN SUCCEEDED
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TORR  Timing level Offset Reset Result）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125545.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Number of a waveform set. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. Th…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TORR  Timing level Offset Reset Result）

```
TORR PRM,ALL,(Pin1)
```

This example resets the offsets for all timing sets of the current primary specification.

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TORS  -  Timing level Offset ReSult）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125236.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 2 列。
> 首行（上游原文）：waveform_set | Number of a waveform set. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. Th…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TORS  -  Timing level Offset ReSult）

```
> TORS? PRM,PRM,R,(p1)
< TORS 1,1,R,0,(p1)

> TORS? PRM,PRM,S,(p1)
< TORS 1,1,S,0,(p1)

> TORS? PRM,PRM,F,(p1)
< TORS 1,1,F,0,(p1)

> TORS? PRM,PRM,D,(p1)
< TORS 1,1,F,0,(p1)
< TORS 1,1,S,0,(p1)

> TORS? PRM,PRM,ALL,(p1)
< TORS 1,1,R,0,(p1)
< TORS 1,1,F,0,(p1)
< TORS 1,1,S,0,(p1)

> TORS? PRM,,VIL,(@)
<TORS 1,,VIL,750,(p1)
<TORS 1,,VIL,750,(p2)

> TORS? PRM,,VISWING,(@)
< TORS 1,,VIH,-450,(p1,p2)
< TORS 1,,VIL,450,(p1,p2)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TORT  -  Timing Level Offset search Result Transitions）

```
TORT? {(pinlist)}
```

returns:

```
TORT {left_boundary|NOT_FOUND}, {right_boundary|NOT_FOUND}, {(pinlist)}
```

Note The returned transition value is the latest passing value near to the transition.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125234.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：left_boundary | The offet of the left boundary or lower level of the pass area found by the last timing or level search, where the fail-pass transition was foun…

### Example（取自子主题 Commands in alphabetical order › List of commands › TORT  -  Timing Level Offset search Result Transitions）

```
TORT? (@)
TORT NOT_FOUND,NOT_FOUND, (p1,p2)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TOUD -  Timing Offset UnDefine）

```
TOUD {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TOUD -  Timing Offset UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125373.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pinlist | The pins for which the embedded timing search configuration is to be removed.

### Example（取自子主题 Commands in alphabetical order › List of commands › TOUD -  Timing Offset UnDefine）

```
TOUD (Pin1, Pin2)
```

### TPSE（取自子主题 Commands in alphabetical order › List of commands › TPSE  TPSE  -  Test Point SEquence）

```
TPSE {testdata_name}, {label_type}, {label_name}, {edit_mode}, {(pinlist)}, [#spec(test_points)]
```

### TPSE?（取自子主题 Commands in alphabetical order › List of commands › TPSE  TPSE  -  Test Point SEquence）

```
TPSE? {label_type}, {label_name}, [anchor_number],{(pinlist)}
```

returns:

```
TPSE {testdata_name}, {label_type}, {label_name}, REPLACE, {(pinlist)}, [#spec(test_points)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TPSE  TPSE  -  Test Point SEquence）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99875.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：testdata_name | Specifies the test data collection from which the test events are to be selected. The collection must have been defined with DFTD.

### Example（取自子主题 Commands in alphabetical order › List of commands › TPSE  TPSE  -  Test Point SEquence）

This example sets up a test label that generates a ramp of 4 samples on pin `vdd` in the default port.

```
DFTD "ramp_events",REPLACE,(vdd),#3628<?xml version="1.0"?>
<testdata>
  <td id="init" type="dcset">
    <setMeasureRange type="voltage" minValue="0" maxValue="3.0"/>
  </td>
  <td id="1" type="dcset">
    <setForceValue type="voltage" value="0.0"/>
  </td>
  <td id="2" type="dcset">
    <setForceValue type="voltage" value="0.5"/>
  </td>
  <td id="3" type="dcset">
    <setForceValue type="voltage" value="1.0"/>
    <measure    type="current" samples="4"/>
  </td>
  <td id="4" type="dcset">
    <setForceValue type="voltage" value="1.5"/>
  </td>
</testdata>

SQLB "ramp4",SVEC,0,3,"wavetable",(@)
. . .
SQPG 0,STVA,0,,,(@)
SQPG 1,STSA,,,,(@)
SQPG 2,GENV,512,,,(@)
SQPG 3,STOP,,,,(@)

TPSE "ramp_events",SVEC,"ramp4",REPLACE,(vdd),#3226<?xml version="1.0"?>
<sequence>
  <tp anchor="64" td="init"/>
    <tp anchor="120" td="1"/>
    <tp anchor="200" td="2"/>
    <tp anchor="300" td="3"/>
    <tp anchor="400" td="4"/>
</sequence>
```

### TPSP（取自子主题 Commands in alphabetical order › List of commands › TPSP  TPSP  -  TestPoint SuPpression）

```
TPSP {suppression_type}, {(pin_list)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TPSP  TPSP  -  TestPoint SuPpression）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/105537.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：suppression_type | Defines which types of test point operations are suppressed. Possible values are:

### Example（取自子主题 Commands in alphabetical order › List of commands › TPSP  TPSP  -  TestPoint SuPpression）

```
TPSP I,(dps1)
FTST?
TPSP OFF,(dps1)
```

In this example, input operations for `dps1` are suppressed for the following functional test. After completion of the test, the suppression is canceled.

### TSCF（取自子主题 Commands in alphabetical order › List of commands › TSCF  TSCF  -  TMU Set ConFiguration）

```
TSCF {"ts_name"}, {property}, {property_value|RESET}, {(pinlist)}
```

### TSCF?（取自子主题 Commands in alphabetical order › List of commands › TSCF  TSCF  -  TMU Set ConFiguration）

```
TSCF? {"ts_name"|ALL|PRM}, [property], {(pinlist)}
```

returns:

```
TSCF {"ts_name"}, {property}, {property_value}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSCF  TSCF  -  TMU Set ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125467.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：ts_name | Specifies the name of a TMU set that must have been defined with TSDF.

Properties and their values
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125467.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：Property | Explanation and values

### Example（取自子主题 Commands in alphabetical order › List of commands › TSCF  TSCF  -  TMU Set ConFiguration）

```
> TSCF? "TMU_set1",,(Pin1)

< TSCF "TMU_set1",PRESCALER,3,(Pin1)
< TSCF "TMU_set1",INITIAL_DISCARD,0,(Pin1)
< TSCF "TMU_set1",INTER_SAMPLE_DISCARD,500,(Pin1)
< TSCF "TMU_set1",SAMPLES_PER_MEAS,2,(Pin1)
< TSCF "TMU_set1",NUM_SHOTS,1,(Pin1)
< TSCF "TMU_set1",MEAS_PER_SHOT,5,(Pin1)
< TSCF "TMU_set1",EDGE_SELECT,RISE,(Pin1)
< TSCF "TMU_set1",DATA_RATE,50000000,(Pin1)
```

This example queries a period measurement definition. Typically, only two samples are taken for such a measurement, and these at a great distance (see the INTER_SAMPLE_DISCARD property in the example). The period resulting from this measurement can be retrieved with the `TSRS?`（raw: `02.06.02.02.278_TSRS__-__TMU_Set_ReSults.md`） query.

### TSDF（取自子主题 Commands in alphabetical order › List of commands › TSDF  TSDF  -  TMU Set DeFinition）

```
TSDF {"TMU_set_name"} [, "mode_context"]
```

### TSDF?（取自子主题 Commands in alphabetical order › List of commands › TSDF  TSDF  -  TMU Set DeFinition）

```
TSDF? ["TMU_set_name"]
```

returns:

```
TSDF {"TMU_set_name"} [, "mode_context"]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSDF  TSDF  -  TMU Set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126322.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：TMU_set_name | In the command, this is the name of a new TMU set. In the query, it is a name of an existing TMU set. If you omit this parameter in the query, TS…

### Example（取自子主题 Commands in alphabetical order › List of commands › TSDF  TSDF  -  TMU Set DeFinition）

```
> TSDF   "TMU_set1"
> TSDF   "TMU_set2"
> TSDF   "TMU_set3"

> TSDF?
< TSDF   "TMU_set1"
< TSDF   "TMU_set2"
< TSDF   "TMU_set3"

```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TSER  -  TMU Set ERror）

```
TSER? {(pinlist)}
```

returns:

```
TSER {VDL_OVERRUN|ARM_OVERRUN|OUT_OF_MEMORY|GLITCH_OVERRUN|NOT_FINISHED}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSER  -  TMU Set ERror）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126327.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：VDL_OVERRUN | The sample rate of the TMU is exceeded.
> 表内引用（1 条，供检索）：`Dealing with very high frequencies`（raw: `02.06.13.01.05_Dealing_with_very_high_data_rates.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TSER  -  TMU Set ERror）

```
> TSER? (Pin1)
< TSER ARM_OVERRUN,(Pin1)
```

### TSHA?（取自子主题 Commands in alphabetical order › List of commands › TSHA  -  Timing Setup Has Arming）

```
TSHA? {specset_id|"multi-port_spec"}, {(pinlist)}
```

returns:

TSHA {specset_id|"multi-port_spec"},{TRUE|FALSE}, {(pinlist)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSHA  -  Timing Setup Has Arming）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131111.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：specset_id | Derived as follows: 100 * equation_set_no + specset_no

### Example（取自子主题 Commands in alphabetical order › List of commands › TSHA  -  Timing Setup Has Arming）

```
> TSHA? "MP_1",(pin1)
< TSHA "MP_1",FALSE,(pin1)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TSRH  -  TMU Set Result Handle）

```
TSRH? {REQUEST|SELECT|RELEASE}, {"handle_name"}
```

returns:

TSRH {REQUEST|SELECT|RELEASE}, {"handle_name"}, {SUCCEED|FAILED}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSRH  -  TMU Set Result Handle）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126271.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：REQUEST | Defines a handle. If the request is successful, the new handle will be the active handle.

### Example（取自子主题 Commands in alphabetical order › List of commands › TSRH  -  TMU Set Result Handle）

```
> TSRH? REQUEST, "area1"
< TSRH REQUEST,"area1",SUCCEED
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TSMD  -  TMU Set Measurement Done）

TSMD? [FORCE,] {(pinlist)}

Returns:

TSMD {FINISHED|NOT_FINISHED}, {(pinlist)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSMD  -  TMU Set Measurement Done）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125551.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：FORCE | If this extra parameter is specified in the query The TMU measurement will be stopped even if it is not yet finished.

### Example（取自子主题 Commands in alphabetical order › List of commands › TSMD  -  TMU Set Measurement Done）

```
> TSMD? (Pin1)
< TSMD FINISHED,(Pin1)
```

### TSPR（取自子主题 Commands in alphabetical order › List of commands › TSPR  TSPR  -  TMU Set PRimary set）

```
TSPR {"TMU_set_name"|""}
```

### TSPR?（取自子主题 Commands in alphabetical order › List of commands › TSPR  TSPR  -  TMU Set PRimary set）

```
TSPR?
```

returns:

```
TSPR {"TMU_set_name"|""}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSPR  TSPR  -  TMU Set PRimary set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125518.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：TMU_set_name | Specifies the name of an existing TMU set.

### Example（取自子主题 Commands in alphabetical order › List of commands › TSPR  TSPR  -  TMU Set PRimary set）

```
> TSPR   "TMU_set1"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TSRC  -  Time Stamping Results Computed）

```
TSRC? [(sitesToBeDone),] [measurement_id], {result_type}, [first_sample], [no_of_samples], [(execution_control),] [(site_selector),] [(resultAreaName),] {(pinlist)}
```

returns:

```
TSRC [shotcount],{result_type}, {successinfo}, {(pin)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSRC  -  Time Stamping Results Computed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/141847.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 6 列，含嵌套表。
> 首行（上游原文）：sitesToBeDone | An extra string parameter, defining the sites to be uploaded. i.e. "01110011". This option needs parameter site_selector to be set to ALL.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/141847.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：NOT_FINISHED | Default. All three steps described above will be executed. If not all required samples have been actually taken, the query will not stop, it issu…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/141847.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ONE | Only the values of the site which has the query focus are processed (the default).

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TSRS  -  TMU Set ReSults）

```
TSRS? [(sitesToBeDone),] [measurement_id], {result_type}, [first_sample], [no_of_samples], [(execution_control),] [(site_selector),] [(resultAreaName),] [(mode),] {(pinlist)}
```

returns:

```
TSRS [measurement_id], [(sitenumber),] {result_type}, [sample_id|aggregation_type|first_sample], {result|no_of_samples}, {(pin)} [,#spec(binary_results)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSRS  -  TMU Set ReSults）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125500.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：NOT_FINISHED | All four steps described above will be executed. If not all required samples have been actually taken, the query will not stop, it will continue …
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125500.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ONE | Only the values of the site which has the query focus are processed (the default).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125500.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：21 行 × 6 列，含嵌套表。
> 首行（上游原文）：sitesToBeDone | An extra string parameter, defining the sites to be uploaded. i.e. "01110011". This option needs parameter site_selector to be set to ALL.

### Example（取自子主题 Commands in alphabetical order › List of commands › TSRS  -  TMU Set ReSults）

This example returns the descriptive statistics for the measurement blocks individually.

```
> TSRS? ,PERIOD, , , (pin_a)

    < TSRS  1,PERIOD , STDDEV ,1.36,(pin_a)
    < TSRS  1,PERIOD , MEAN 1.36,(pin_a)
    < TSRS  1,PERIOD , MAX, 1.36,(pin_a)
    < TSRS  1,PERIOD , MIN, 1.36,(pin_a)
    < TSRS  1,PERIOD , MEDIAN, 1.36,(pin_a)
    < TSRS  1,PERIOD , PP, 1.36,(pin_a)

    < TSRS  2,PERIOD , STDDEV ,1.36,(pin_a)
    < TSRS  2,PERIOD , MEAN 1.36,(pin_a)
    < TSRS  2,PERIOD , MAX, 1.36,(pin_a)
    < TSRS  2,PERIOD , MIN, 1.36,(pin_a)
    < TSRS  2,PERIOD , MEDIAN, 1.36,(pin_a)
    < TSRS  2,PERIOD , PP, 1.36,(pin_a)
```

This example returns the individual samples 100 through 119 in measurement block 2, and also the statistical values.

```
> TSRS? 2,PERIOD,100,20,(pin_a)

    < TSRS  2,PERIOD ,100,1.36,(pin_a)
    < TSRS  2,PERIOD ,101,1.37,(pin_a)
    ...
    < TSRS  2,PERIOD ,119,1.36,(pin_a)
    < TSRS  2,PERIOD , STDDEV ,1.36,(pin_a)
    < TSRS  2,PERIOD , MEAN 1.36,(pin_a)
    < TSRS  2,PERIOD , MAX, 1.36,(pin_a)
    < TSRS  2,PERIOD , MIN, 1.36,(pin_a)
    < TSRS  2,PERIOD , MEDIAN, 1.36,(pin_a)
    < TSRS  2,PERIOD , PP, 1.36,(pin_a)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TSRW  -  TMU Set RaW results）

```
TSRW? [(sitesToBeDone),] [shot], [measurement_id], [first_sample], [no_of_samples], [(execution_control),] [(site_selector),][(resultAreaName),] [(mode),] {(pinlist)}
```

returns:

```
TSRW [shot], [measurement_id], [first_sample], [no_of_samples], [(sitenumber),] {(pin)}, {#spec(raw_results)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSRW  -  TMU Set RaW results）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125519.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：NOT_FINISHED | All three steps described above will be executed. If not all required samples have been actually taken, the query will not stop, it issues a warn…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125519.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ONE | Only the values of the site which has the query focus are uploaded (the default).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125519.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 6 列，含嵌套表。
> 首行（上游原文）：sitesToBeDone | An extra string parameter, defining the sites to be uploaded. i.e. "01110011". This option needs parameter site_selector to be set to ALL.

### Example（取自子主题 Commands in alphabetical order › List of commands › TSRW  -  TMU Set RaW results）

```
> TSRW? 1,1,0,3,(std_i)

    < TSRW 1,1,0,3,(std_i),#2470.0000524107368,0.0000525147428,0.0000526187385
```

This example uploads the time stamps 0 through 2 of measurement block 1 of the first shot. The unit is seconds.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TSST  -  TeSt STatus）

```
TSST? {ALL|test_result_mask}, {ALL|test_status_mask}, {(pinlist)}
```

returns:

```
TSST {test_result}, {test_status}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSST  -  TeSt STatus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/97179.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 6 列，含嵌套表。
> 首行（上游原文）：test_result_mask | In order to mask some of the result bits, enter an integer not greater than 2047. The bits of the corresponding binary number will be combine…

### Example（取自子主题 Commands in alphabetical order › List of commands › TSST  -  TeSt STatus）

```
> TSST? ALL,ALL,(@)
< TSST 1,0,(dpsPin1)
> TSST? 0,256,(@)
< TSST P,P,(dpsPin1)
```

This example shows the effect of a mask. As shown by the first query, the only error was that at least one pin has failed the limit check. In the second query, bit 0 of the result byte is masked, and consequently TSST? returns P for both result and status.

### TSTL（取自子主题 Commands in alphabetical order › List of commands › TSTL  TSTL  -  TeST Label）

```
TSTL {"label"}, [(port)]
```

### TSTL?（取自子主题 Commands in alphabetical order › List of commands › TSTL  TSTL  -  TeST Label）

```
TSTL?
```

returns:

```
TSTL {"label"}, {(port)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSTL  TSTL  -  TeST Label）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98815.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：label | Defines the label you wish to edit. Enter an alphanumeric string, 1 to 128 characters long, enclosed in double quotes. You can deactivate the currently …

### Example（取自子主题 Commands in alphabetical order › List of commands › TSTL  TSTL  -  TeST Label）

```
TSTL "new",
```

This example selects the label "new" for editing.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TSUD -  TMU Set UnDefine）

```
TSUD {"TMU_set_name"|ALL}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSUD -  TMU Set UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126323.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：TMU_set_name | Specifies the name of an existing TMU set.

### Example（取自子主题 Commands in alphabetical order › List of commands › TSUD -  TMU Set UnDefine）

```
> TSUD   "TMU_set1"
```

### TSUS（取自子主题 Commands in alphabetical order › List of commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS {waveform_set},{timing_set}
```

### TSUS?（取自子主题 Commands in alphabetical order › List of commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS? {waveform_set}
```

returns:

```
TSUS {waveform_set},{timing_set}
```

Or:

```
TSUS? {specset_id}
```

returns:

```
TSUS {specset_id},{timing_set}
```

Or, for multiport specifications:

```
TSUS? {"multiport_spec"}[,(portlist)]
```

returns:

```
TSUS {"multiport_spec"},{timing_set}[,(port)]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSUS  TSUS  -  Timing Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98817.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS 3,7
```

This example defines a maximum of 7 timing sets in waveform set 3.

```
TSUS? "spefc",(ARMPort)
TSUS "spefc",3,(ARMPort)
```

This example queries the number of timing sets defined for port ARMPort in the multiport specification spefc.

### TSUX（取自子主题 Commands in alphabetical order › List of commands › TSUX  TSUX  -  Timing Sets Used eXtended）

```

TSUX {waveform_set},{timing_set}
```

### TSUX?（取自子主题 Commands in alphabetical order › List of commands › TSUX  TSUX  -  Timing Sets Used eXtended）

```

TSUX? {waveform_set}
```

returns:

```
TSUX {waveform_set},{timing_set}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSUX  TSUX  -  Timing Sets Used eXtended）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98818.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter ALL for all waveform sets in the query command.
> 表内引用（1 条，供检索）：`TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TSVD  -  TimStamper ValiD）

```
TSVD? {waveform_set|specset_id|"multi-port_spec"|PRM}, {"TMU_set"|PRM}
```

returns:

```
TSVD? {waveform_set|specset_id|"multi-port_spec"|PRM}, {"TMU_set"|PRM}, {VALID|ERROR}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TSVD  -  TimStamper ValiD）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/130393.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：waveform_set | Specifies a waveform set number for a fixed timing setup.

### Example（取自子主题 Commands in alphabetical order › List of commands › TSVD  -  TimStamper ValiD）

```
> TSVD? PRM, "TMU_set1"
< TSVD PRM, "TMU_set1",VALID
```

This example queries if the current primary timing is consistent to the TMU set `TMU_set1`.

### TTCF（取自子主题 Commands in alphabetical order › List of commands › TTCF  TTCF  -  Transition Test ConFiguration）

```
TTCF {"tt_name"}, {property}, {property_value}, {(pinlist)}
```

### TTCF?（取自子主题 Commands in alphabetical order › List of commands › TTCF  TTCF  -  Transition Test ConFiguration）

```
TTCF? {"tt_name"|ALL|PRM|DEFAULT}, {property|ALL}, {(pinlist)}
```

returns:

```
TTCF {"tt_name"}, {property}, {property_value}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TTCF  TTCF  -  Transition Test ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116670.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：tt_name | Specifies the name of a transition test set that must have been defined with TTDF.
> 表内引用（1 条，供检索）：`TTDF`（raw: `02.06.02.02.288_TTDF__TTDF__-__Transition_Test_set_DeFinition.md`）

Properties and their values
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116670.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：43 行 × 4 列。
> 首行（上游原文）：Property | Explanation and values

### Example（取自子主题 Commands in alphabetical order › List of commands › TTCF  TTCF  -  Transition Test ConFiguration）

```
> TTCF? "my_TT_SET",ALL,(PIN1)

< TTCF "my_TT_SET",DEVIATION_LIMIT_DUT_BEFORE_ED,100,(Pin1)
< TTCF "my_TT_SET",DEVIATION_LIMIT_ED_BEFORE_DUT,100,(Pin1)
< TTCF "my_TT_SET",DISPARITY_MODE,OFF,(Pin1)
< TTCF "my_TT_SET",ERR_BADTRAN,ON,(Pin1)
< TTCF "my_TT_SET",ERR_CNTADJOVR,ON,(Pin1)
< TTCF "my_TT_SET",ERR_CNTLMT,ON,(Pin1)
< TTCF "my_TT_SET",ERR_COMPARE,ON,(Pin1)
< TTCF "my_TT_SET",ERR_FTO,ON,(Pin1)
< TTCF "my_TT_SET",ERR_JMP2,ON,(Pin1)
< TTCF "my_TT_SET",ERR_PULSE,ON,(Pin1)
< TTCF "my_TT_SET",ERR_STO,ON,(Pin1)
< TTCF "my_TT_SET",ERR_STOP,OFF,(Pin1)
< TTCF "my_TT_SET",ERR_TE0,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TE2,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TE3,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TE4,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TRK,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TRMCNT,ON,(Pin1)
< TTCF "my_TT_SET",ERR_WRCMP,ON,(Pin1)
< TTCF "my_TT_SET",ERR_XMAX,ON,(PIN1)
< TTCF "my_TT_SET",ERR_XMIN,ON,(Pin1)
< TTCF "my_TT_SET",FIRST_INITIAL_SYNC_LIMIT,10,(Pin1)
< TTCF "my_TT_SET",FIRST_INITIAL_SYNC_MODE,ON,(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_1,"LLLLLHHHHH",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_2,"",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_3,"",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_4,"",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_5,"",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_6,"",(Pin1)
< TTCF "my_TT_SET",PULSE_STRETCHING_MODE_1BIT,STRETCH_2TO4,(Pin1)
< TTCF "my_TT_SET",PULSE_STRETCHING_MODE_2BIT,STRETCH_1TO3,(Pin1)
< TTCF "my_TT_SET",REMOVE_XTOKEN_MODE,OFF,(Pin1)
< TTCF "my_TT_SET",SUBSEQUENT_INITIAL_SYNC_LIMIT,10,(Pin1)
< TTCF "my_TT_SET",SUBSEQUENT_INITIAL_SYNC_MODE,ON,(Pin1)
< TTCF "my_TT_SET",TOKEN_SIZE,10,(Pin1)
< TTCF "my_TT_SET",TRACKING_LIMIT,4,(Pin1)
< TTCF "my_TT_SET",TRACKING_MODE,ACTIVE,(Pin1)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TTDB  -  Transition Test DeBug information）

```
TTDB? {type|ALL}, [sub_type], {(pinlist)}
```

returns:

```
TTDB {type}, [sub_type], {value}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TTDB  -  Transition Test DeBug information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116688.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：type | Specifies the information type. For a list, see the Information types and subtypes table below.

Information types and subtypes
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116688.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 4 列。
> 首行（上游原文）：Information type | Explanation and values
> 表内引用（3 条，供检索）：`Drift and transition tracking`（raw: `02.06.15.01.01_Drift_and_transition_tracking.md`） · `TTST?`（raw: `02.06.02.02.292_TTST__-__Transition_Test_STatus_information.md`） · `TTCF`（raw: `02.06.02.02.286_TTCF__TTCF__-__Transition_Test_ConFiguration.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TTDB  -  Transition Test DeBug information）

```
> TTDB? IDLE_TOKEN, 1, (Pin1)

< TTDB IDLE_TOKEN, 1, 1234,(Pin1)
```

This example queries how often the first special idle token was removed in the last sequencer run.

```
> TTDB? TRK_STATUS,ALL, (Pin1)

< TTDB TRK_STATUS,TRANS_X,"1000 1001 1101 1000", (Pin1)
< TTDB TRK_STATUS,TRANS_R,0, (Pin1)
< TTDB TRK_STATUS,TRANS_COMPOSITE,"1000 1001 1101", (Pin1)
```

The first line of the reply reports the transitions of the last 24 UI, accumulated in blocks of 6. The third line reports which accumulated transition patterns occurred in one window (= 3 UI) during the last sequencer run. Three of the 8 possible patterns were observed.

### TTDF（取自子主题 Commands in alphabetical order › List of commands › TTDF  TTDF  -  Transition Test set DeFinition）

```
TTDF {"tt_set_name"} [, "mode_context"]
```

### TTDF?（取自子主题 Commands in alphabetical order › List of commands › TTDF  TTDF  -  Transition Test set DeFinition）

```
TTDF? ["tt_set_name"]
```

returns:

```
TTDF {"tt_set_name"} [, "mode_context"]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116759.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：tt_set_name | In the command, this is the name of a new transition test set. In the query, it is a name of an existing transition test set. If you omit this par…

### Example（取自子主题 Commands in alphabetical order › List of commands › TTDF  TTDF  -  Transition Test set DeFinition）

```
> TTDF   "myTTTrckSet1"
> TTDF   "myTTPatTSet1"
> TTDF   "myTTRCTLSet1"

TTDF?
> TTDF   "myTTTrckSet1"
> TTDF   "myTTPatTSet1"
> TTDF   "myTTRCTLSet1"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TTMD  -  Transition Test MoDe query）

```
TTMD? {specset_id|"multi-port_spec"}, {timing_set}, {(pinlist)}
```

returns:

```
TTMD {specset_id|"multi-port_spec"}, {timing_set}, {tt_mode}, [clk_fwd], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TTMD  -  Transition Test MoDe query）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116966.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：specset_id | Number of a single-port timing specification. Derived as follows: 100 *equation_set_no + specset_no
> 表内引用（1 条，供检索）：`DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TTMD  -  Transition Test MoDe query）

```
> TTMD 101,1,(PIN1)
< TTMD 101,1,X4,,(PIN1)
```

### TTPR（取自子主题 Commands in alphabetical order › List of commands › TTPR  TTPR  -  Transition Test PRimary set）

TTPR {"tt_set_name"|DEFAULT}

### TTPR?（取自子主题 Commands in alphabetical order › List of commands › TTPR  TTPR  -  Transition Test PRimary set）

```
TTPR?
```

returns:

```
TTPR {"tt_set_name"}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TTPR  TTPR  -  Transition Test PRimary set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116761.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：tt_set_name | Specifies the name of an existing transition test set.

### Example（取自子主题 Commands in alphabetical order › List of commands › TTPR  TTPR  -  Transition Test PRimary set）

```
> TTPR   "myTTTrckSet1"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TTRS  -  Time TRansition Search）

```
TTRS? {start}, {stop}, {search_type}, {(pinlist)}
```

returns:

```
TTRS {value_specifier}, [pass_value], [fail_value], {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TTRS  -  Time TRansition Search）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98819.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 3 列。
> 首行（上游原文）：start | The start parameter defines the point in time (in ns), relative to the start of the cycle, where you want the search to begin.
> 表内引用（1 条，供检索）：`DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TTRS  -  Time TRansition Search）

```
TTRS? 10,80,L,(Q0)
TTRS EQ,70,80,(Q0)
```

This example executes a global search test on pin Q0. A linear sweep takes place between 10 ns and 80 ns relative to the start of the period. The system returned a pass at 70 ns and a fail at 80 ns.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TTST  -  Transition Test STatus information）

```
TTST? {status_type}, {filter}, {(pinlist)}
```

returns:

TTST {status_type}, {property}, {state}, {(pinlist)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TTST  -  Transition Test STatus information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116741.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：38 行 × 4 列。
> 首行（上游原文）：status_type | Specifies the status type. Possible values are:

### Example（取自子主题 Commands in alphabetical order › List of commands › TTST  -  Transition Test STatus information）

```
> TTST? ALL,ALL,(p1)

< TTST INTR_STATUS,DRIVE_BIT_IN_COMPARE_DATA,OFF,(p1)
< TTST INTR_STATUS,ADJUSTMENT_ERROR,OFF,(p1)
< TTST INTR_STATUS,DUT_FIFO_OVERFLOW,OFF,(p1)
< TTST INTR_STATUS,EXPECTED_FIFO_OVERFLOW,OFF,(p1)
< TTST ERR_STATUS,ERR_XMAX,OFF,(p1)
< TTST ERR_STATUS,ERR_XMIN,OFF,(p1)
< TTST ERR_STATUS,ERR_FTO,OFF,(p1)
< TTST ERR_STATUS,ERR_STO,OFF,(p1)
< TTST ERR_STATUS,ERR_TRMCNT,OFF,(p1)
< TTST ERR_STATUS,ERR_COMPARE,ON,(p1)
< TTST ERR_STATUS,ERR_TE4,OFF,(p1)
< TTST ERR_STATUS,ERR_TE3,OFF,(p1)
< TTST ERR_STATUS,ERR_TE2,ON,(p1)
< TTST ERR_STATUS,ERR_TE0,OFF,(p1)
< TTST ERR_STATUS,ERR_JMP2,ON,(p1)
< TTST ERR_STATUS,ERR_TRK,OFF,(p1)
< TTST ERR_STATUS,ERR_PULSE,OFF,(p1)
< TTST ERR_STATUS,ERR_BADTRAN,OFF,(p1)
< TTST ERR_STATUS,ERR_CNTADJOVR,OFF,(p1)
< TTST ERR_STATUS,ERR_CNTLMT,OFF,(p1)
< TTST ERR_STATUS,ERR_STOP,OFF,(p1)
< TTST ERR_STATUS,ERR_WRCMP,OFF,(p1)
```

This example returns all properties of the ERR_STATUS type. ON indicates that the respective state was observed, OFF indicates that it was not observed. Note that ON does not imply that the test failed. For this, the respective property must also be activated as an error with TTCF. In this example compare errors (ERR_COMPARE) and a jump by 2 (ERR_TE2, ERR_JMP2) were observed.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TTUD -  Transition Test UnDefine）

TTUD {"tt_set_name"}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TTUD -  Transition Test UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116760.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：tt_set_name | Specifies the name of an existing transition test set.

### Example（取自子主题 Commands in alphabetical order › List of commands › TTUD -  Transition Test UnDefine）

```
> TTUD   "myTTTrckSet1"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › TTVD  -  Transition Test ValiDate）

```
TTVD? {"tt_name"|ALL|PRM}, {(pinlist)}
```

returns:

```
TTVD {"tt_name"}, {VALID|INVALID}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › TTVD  -  Transition Test ValiDate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116763.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：tt_name | Specifies the name of a transition test set that must have been defined with TTDF.
> 表内引用（1 条，供检索）：`TTDF`（raw: `02.06.02.02.288_TTDF__TTDF__-__Transition_Test_set_DeFinition.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › TTVD  -  Transition Test ValiDate）

```
> TTVD? "mySet",(p1,p2,p3)
< TTVD  "mySet", VALID, (p1,p3)
< TTVD  "mySet", INVALID, (p3)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UDEF -  UnDEFine pin）

```
UDEF {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UDEF -  UnDEFine pin）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98821.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pinlist | Consists of single or multiple pin names or the symbol @ which removes all pins. If more than one pin is required, the names must be separated with a …

### Example（取自子主题 Commands in alphabetical order › List of commands › UDEF -  UnDEFine pin）

```
UDEF (Q3)
```

This example causes pin Q3 to be removed from the current configuration. If you subsequently redefine the channel using the same or a different name, it assumes its former operating mode and the pin type OFF.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UDGP -  UnDefine GrouP）

```
UDGP {(group)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UDGP -  UnDefine GrouP）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98822.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：group | Defines the name of the group of pins to be removed. The symbol @ can be used to dismantle all groups. If more than one group is to be removed, the name…

### Example（取自子主题 Commands in alphabetical order › List of commands › UDGP -  UnDefine GrouP）

```
UDGP (Qout)
```

This command dismantles the group entitled Qout.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UDPR -  UnDefine Pin Role）

```
UDPR "alias_set_name"|@,"pin_alias",(package_pin_name|@)
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UDPR -  UnDefine Pin Role）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112438.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：alias_set_name | The alias set name. The alias of the pin (specified by the pin name parameter) defined in this alias set is deleted. The symbol @ can be used t…

### Example（取自子主题 Commands in alphabetical order › List of commands › UDPR -  UnDefine Pin Role）

```
UDPR "@","",(@)
```

This example deletes all the alias sets.

```
UDPR "FUNC","",(@)
```

This example deletes the alias set FUNC.

```
UDPR "FUNC","CLK",(CP)
```

This example deletes the pair of package pin name CP and the pin alias CLK from the alias set FUNC.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UDPS -  Undefine DPS pin）

```
UDPS {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UDPS -  Undefine DPS pin）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98823.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pinlist | Consists of single or multiple pin names or the symbol @ which undefines all DPS pins. If more than one pin is to be removed, the names must be separa…

### Example（取自子主题 Commands in alphabetical order › List of commands › UDPS -  Undefine DPS pin）

```
UDPS (Vee)
```

This example removes pin Vee from the setup. The software saves the level data associated with the DPS channel. Therefore if you redefine the channel using the same or a different name, the DPS settings are immediately restored.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UDPT -  UnDefine PorT）

```
UDPT {(portlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UDPT -  UnDefine PorT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98824.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：portlist | List of port names or the symbol @@, which undefines all ports. If more than one port is to be removed, the names must be separated with a comma.

### Example（取自子主题 Commands in alphabetical order › List of commands › UDPT -  UnDefine PorT）

```
UDPT (port_1)
```

This command undefines port port_1.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UDRS -  UnDefine Routing Set）

```
UDRS {set}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UDRS -  UnDefine Routing Set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99081.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：set | An identification number of the routing set. This is an integer from 1 to the maximum number defined by the DSCP command. If the ALL specifier is specifie…
> 表内引用（1 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › UDRS -  UnDefine Routing Set）

```
UDRS ALL
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UDUP -  UnDefine Utility Purpose）

```
UDUP {(purpose_name)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UDUP -  UnDefine Utility Purpose）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98830.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：purpose_name | Specifies the utility purpose name or names to be undefined. The symbol @ removes all utility purpose definitions. If more than one name is to be…

### Example（取自子主题 Commands in alphabetical order › List of commands › UDUP -  UnDefine Utility Purpose）

```
UDUP (@)
```

This command undefines all defined utility purpose names.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UDUT -  UnDefine UTility line）

```
UDUT {(util_name)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UDUT -  UnDefine UTility line）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98831.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：util_name | Specifies the utility line name or names to be undefined. The symbol @ removes all utility line definitions. If more than one name is to be removed,…

### Example（取自子主题 Commands in alphabetical order › List of commands › UDUT -  UnDefine UTility line）

```
UDUT (@)
```

This command undefines all defined utility line names.

### UHCM（取自子主题 Commands in alphabetical order › List of commands › UHCM  UHCM  -  Ultra High Current power supply Modes）

```
UHCM {`set_nr`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_set_nr`）}, `[time_to_alarm`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_time_to_alarm`）,] `[reserved_param`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_reserved_param`）], `[clamp_mode`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_clamp_mode`）], `[fast_preload`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_fast_preload`）],
         `[openLoopProtection`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_openLoopProtection`）,] `[force_drop`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_force_drop`）], `[return_drop`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_return_drop`）], `[pulldown`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pulldown`）,] {(`pinlist`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pinlist`）)}

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106910.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106910.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
```

### UHCM?（取自子主题 Commands in alphabetical order › List of commands › UHCM  UHCM  -  Ultra High Current power supply Modes）

```
UHCM? {`set_nr`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_set_nr`）}, {(`pinlist`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pinlist`）)}
```

returns:

```
UHCM {`set_nr`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_set_nr`）}, `[time_to_alarm`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_time_to_alarm`）,] `[reserved_param`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_reserved_param`）], `[clamp_mode`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_clamp_mode`）], `[fast_preload`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_fast_preload`）],
         `[openLoopProtection`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_openLoopProtection`）,] `[force_drop`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_force_drop`）], `[return_drop`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_return_drop`）], {`[pulldown`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pulldown`）], {(`pinlist`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pinlist`）)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UHCM  UHCM  -  Ultra High Current power supply Modes）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106910.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ALL | Modifies all existing DPS sets.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106910.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 8 列，含嵌套表。
> 首行（上游原文）：set_nr | The mandatory identification number of the DPS set which you want to modify: ALL | Modifies all existing DPS sets.

### Example（取自子主题 Commands in alphabetical order › List of commands › UHCM  UHCM  -  Ultra High Current power supply Modes）

```
UHCM PRM,,,,0.4,0.1,(Vee)
```

This example sets the voltage drop force to 0.4 V, and the voltage drop return to 0.1 V.

### UPAS（取自子主题 Commands in alphabetical order › List of commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

```
UPAS {site}, ["{setting}"], {(purpose_name)}
```

### UPAS?（取自子主题 Commands in alphabetical order › List of commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

```
UPAS? {site}, {(purpose_name)}
```

returns:

```
UPAS {site}, "{setting}", {(purpose_name)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98832.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：site | The site parameter is an integer that defines the number of the site where the channels are to be defined. The integer must be greater than 1. When speci…
> 表内引用（1 条，供检索）：`DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

```
> DFUP (101,102,103,104),"11XX",(AWG_CNCT)
> UPAS 2,"XX11",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "11XX", (AWG_CNCT)
> PSFC 2
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "XX11", (AWG_CNCT)
```

In this example, the `DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`） command defines a utility purpose AWG_CNCT and output states for site 1. The UPAS command defines the output states of AWG_CNCT for site 2. First the settings of site 1 are activated. Then the setup focus is restricted to site 2, and the output states for site 2 are activated.

### UPST（取自子主题 Commands in alphabetical order › List of commands › UPST  UPST  -  Utility Purpose STate）

```
UPST ["setting"], {(purpose_name)}
```

### UPST?（取自子主题 Commands in alphabetical order › List of commands › UPST  UPST  -  Utility Purpose STate）

```
UPST? {(purpose_name)}
```

returns:

```
UPST "{setting}", {(purpose_name)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UPST  UPST  -  Utility Purpose STate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98833.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：setting | The optional parameter specifies the status of the utility lines in the utility purpose. The status is determined with the following specifiers: 0: Se…

Name of the utility purpose to be set or read.

For the query, you can specify multiple names, which must be separated by a comma.

Specifying the symbol @ returns the definitions of all utility purposes.

   | Note All utility lines that are set with `UTST`（raw: `02.06.02.02.313_UTST__UTST__-__UTility_line_STate.md`） or UPST will be switched in parallel when the `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`） command is performed. If the `WSDN`（raw: `02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md`） command is used immediately after FLSH, the time span during which execution will pause equals the longest settling time that is defined for any of the switched utility lines (with `UTTI`（raw: `02.06.02.02.314_UTTI__UTTI__-__UTility_line_settling_TIme.md`）) or purposes (with `UPTI`（raw: `02.06.02.02.307_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md`）).

### Example（取自子主题 Commands in alphabetical order › List of commands › UPST  UPST  -  Utility Purpose STate）

```
UPST ,(AWG_CNCT)
FLSH
WSDN
UPST? (AWG_CNCT)
```

returns

```
UPST "0110",(AWG_CNCT)
```

This example sets the utility purpose "AWG_CNCT" to the hardware, then reads the state of the utility purpose.

### UPTD（取自子主题 Commands in alphabetical order › List of commands › UPTD  UPTD  -  UP To Date）

```
UPTD {status}, {flag}
```

### UPTD?（取自子主题 Commands in alphabetical order › List of commands › UPTD  UPTD  -  UP To Date）

```
UPTD? {status}
```

returns:

```
UPTD {status}, {flag}
```

### Example（取自子主题 Commands in alphabetical order › List of commands › UPTD  UPTD  -  UP To Date）

```
UPTD? CONF
```

This example requests if the pin configuration data has been changed since the file was last loaded or saved. If the data has not changed, the response is:

```
UPTD CONF,1
```

### UPTI（取自子主题 Commands in alphabetical order › List of commands › UPTI  UPTI  -  Utility Purpose settling TIme）

```
UPTI {time}, {(purpose_name)}
```

### UPTI?（取自子主题 Commands in alphabetical order › List of commands › UPTI  UPTI  -  Utility Purpose settling TIme）

```
UPTI? {(purpose_name)}
```

returns:

```
UPTI {time}, {(purpose_name)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UPTI  UPTI  -  Utility Purpose settling TIme）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98835.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：time | Specifies the wait time to change the utility line status using the UPST and FLSH commands (in ms). 0 ... 2 147 483.646 [ms]

### Example（取自子主题 Commands in alphabetical order › List of commands › UPTI  UPTI  -  Utility Purpose settling TIme）

```
UPTI 2.5,(AWG_CNCT)
```

This example sets the settling time of the utility purpose "AWG_CNCT" to 2.5 ms.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UTDE -  Unload Test Data Entity）

```
UTDE "<file_name>" | ALL
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UTDE -  Unload Test Data Entity）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124453.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：file_name | The file name of the protocol test data entity (TDE) to unload. The specified TDE must belong to the directory specified with the PTDE command.
> 表内引用（1 条，供检索）：`PTDE`（raw: `02.06.02.02.200_PTDE__PTDE__-__Path_for_Test_Data_Entities.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › UTDE -  Unload Test Data Entity）

```
UTDE "test.prot_asg"
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UTIN  -  UTility line INputs）

```
UTIN?
```

returns:

```
UTIN {data}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UTIN  -  UTility line INputs）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98836.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：data | This parameter returns a decimal number that you must translate to binary. Ignore the most significant bit. The other bits give the state of the seven li…

### Example（取自子主题 Commands in alphabetical order › List of commands › UTIN  -  UTility line INputs）

```
UTIN?
```

returns:

```
UTIN 6
```

This example returns a decimal value of 6, which is 0000 0110b.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › UTIX  -  UTility line Inputs eXtended）

```
UTIX? [utility_group]
```

returns

```
UTIX {utility_group}, {value}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UTIX  -  UTility line Inputs eXtended）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98837.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：utility_group | This parameter specifies the utility pogo block. The pogo block is defined by a three‑digit number. For valid pogo blocks, refer to DUT interfac…

### Example 1（取自子主题 Commands in alphabetical order › List of commands › UTIX  -  UTility line Inputs eXtended）

Assuming that the first 16 utility lines of block 165 are high, then

```
UTIX? 165
```

returns

```
UTIX 165,65535
```

In this example the first 16 utility lines of block 165 were set to 0 by the `UTOT`（raw: `02.06.02.02.311_UTOT__UTOT__-__UTility_line_OuTputs.md`） command and no external device has pulled down any of the utility lines.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › UTIX  -  UTility line Inputs eXtended）

```
UTIX? 165
```

returns

```
UTIX 165,65534
```

In this example the first 16 utility lines of block 165 were either set to FFFEh by UTOT or they were set to FFFFh and an external device has pulled down line 00, or both occurrences have taken place.

### UTOT（取自子主题 Commands in alphabetical order › List of commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT {utility_group}, [mask], {value}
```

### UTOT?（取自子主题 Commands in alphabetical order › List of commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT? {utility_group}
```

returns:

```
UTOT {utility_group}, [mask], {word}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UTOT  UTOT  -  UTility line OuTputs）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98838.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：utility_group | This parameter specifies the utility pogo block. The pogo block is defined by a three‑digit number. For valid pogo blocks, refer to DUT interfac…

### Example 1（取自子主题 Commands in alphabetical order › List of commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT 165,16383,12345
```

This code sets the first sixteen utility lines of the first block, except those used for the addressing of EEPROMs related to the DUT interface. These are URW14 and URW15. URW0 to URW13 are set to the inverse of 12345. 12345 in decimal equals 0011000000111001 in binary. Inverted, this is 53190 in decimal or 1100111111000110 in binary. Thus the lines will have these states:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98838.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 4 列。
> 首行（上游原文）：URW00 = low | URW04 = low | URW08 = high | URW12 = low

For the utility lines required to address EEPROMs related to the DUT interface see `Utility lines and DUT board EEPROMs`（raw: `../02.03_DUT_board_design_reference/02.03.04.06_Utility_lines_and_DUT_board_EEPROMs.md`）.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT? 165
```

returns:

```
UTOT 165,,12345
```

The query returns the value that was written by UTOT. If you have previously executed Example 1, then the returned value will be the written value, but bits 14 and 15 may be different. This is because these lines retain the values that have been written previously.

Use the `UTIX?`（raw: `02.06.02.02.310_UTIX__-__UTility_line_Inputs_eXtended.md`） command to read back the actual state of the utility lines.

### Example 3（取自子主题 Commands in alphabetical order › List of commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT 166,65535,"5555,AAAA,0,FFFF"
```

writes the sequence AAAAh, 5555h, FFFFh, 0000h to the first sixteen utility lines of the second utility block.

### Example 4（取自子主题 Commands in alphabetical order › List of commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT? 166
```

returns the last written values. If you have just executed example 3, the result would be:

```
UTOT 166,,65535
```

### UTSC（取自子主题 Commands in alphabetical order › List of commands › UTSC  UTSC  -  UTility line Serial Configuration）

```
UTSC {(word) | ALL}, {mode} [, maskMode]
```

### UTSC?（取自子主题 Commands in alphabetical order › List of commands › UTSC  UTSC  -  UTility line Serial Configuration）

```
UTSC? {(word)} | ALL
```

returns:

```
UTSC {(word)}, {mode} [, maskMode]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UTSC  UTSC  -  UTility line Serial Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124715.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：word | One unique utility pogo block number or a list enclosed in brackets containing utility pogo blocks separated by commas. The pogo block or the list of pog…
> 表内引用（5 条，供检索）：`DUT interface layout`（raw: `../02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md`） · `Utility pogo block mapping`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md#_347642__s_Utility_pogo_block_mapping`） · `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`） · `UTOT`（raw: `02.06.02.02.311_UTOT__UTOT__-__UTility_line_OuTputs.md`） · `UTIX?`（raw: `02.06.02.02.310_UTIX__-__UTility_line_Inputs_eXtended.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › UTSC  UTSC  -  UTility line Serial Configuration）

The following example shows how to reset the mode for all utility blocks to static:

```
UTSC ALL, OFF
```

The following example shows how to gang utility blocks 1 to 4 setting the mode to serial out:

```
UTSC (165,166,167,168),RW
```

The following example shows how to change the mode of the previously set up gang to parallel out:

```
UTSC (165,166,167,168),RD
```

The following example, based on the previous setup, will lead to an error, because the fourth utility pogo block is missing:

```
UTSC (165,166,167),OFF
```

The following example shows how to turn off ganging by changing the mode of the previously set up gang to off:

```
UTSC (165,166,167,168),OFF
```

The following example shows how to set up a new gang with the second, third and fourth utility pogo block in serial out mode:

```
UTSC (166,167,168),RW
```

The following example shows how to use the UTSC? query to display the entire gang and the mode if a single utility block of a gang is given:

```
UTSC? 166
```

results in:

```
UTSC (166,167,168),RW
```

The following example shows how to use the UTSC? query to display all gangs and modes of all utility blocks:

```
UTSC? ALL
```

results in:

```
UTSC 1,OFF
UTSC (166,167,168),RW
UTSC 169,OFF
UTSC 170,OFF
UTSC 171,OFF
UTSC 172,OFF
```

The following example shows how to change the existing gang with utility blocks 2 to 4 in serial out mode to the masked mode:

```
UTSC (166,167,168),RW,MASK
```

The following example shows the query result of UTSC? with mask mode set for the second to fourth utility pogo block:

```
UTSC? ALL
```

results in:

```
UTSC 165,OFF
UTSC (166,167,168),RW,MASK
UTSC 169,OFF
UTSC 170,OFF
UTSC 171,OFF
UTSC 172,OFF
```

### UTST（取自子主题 Commands in alphabetical order › List of commands › UTST  UTST  -  UTility line STate）

```
UTST {value}, {(util_name)}
```

### UTST?（取自子主题 Commands in alphabetical order › List of commands › UTST  UTST  -  UTility line STate）

```
UTST? type, {(util_name)}
```

returns:

```
UTST {value}, {(util_name)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UTST  UTST  -  UTility line STate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98839.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：value | Specifies the output (desired) status of the utility line with the specifier 0 or 1. 0: High output 1: Low output

Specifies the utility line name or names to be set or read.

In the query, specifying @ returns all utility lines.

If more than one name is required, the names must be separated by commas.

   | Note All utility lines that are set with UTST or `UPST`（raw: `02.06.02.02.305_UPST__UPST__-__Utility_Purpose_STate.md`） will be switched in parallel when the `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`） command is performed. If the `WSDN`（raw: `02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md`） command is used immediately after FLSH, the time span during which execution will pause equals the longest settling time that is defined for any of the switched utility lines (with `UTTI`（raw: `02.06.02.02.314_UTTI__UTTI__-__UTility_line_settling_TIme.md`）) or purposes (with `UPTI`（raw: `02.06.02.02.307_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md`）).

### Example（取自子主题 Commands in alphabetical order › List of commands › UTST  UTST  -  UTility line STate）

```
UTST 1,(Filt1,Filt2)
UTST 0,(Filt3,Filt4)
FLSH
WSDN
UTST? w,(Filt1,Filt2,Filt3,Filt4)
```

will return:

```
UTST 1,(Filt1,Filt2)
UTST 0,(Filt3,Filt4)
```

This example sets the utility lines "Filt1" and "Filt2" to high output, and "Filt3" and "Filt4" to low output.

### UTTI（取自子主题 Commands in alphabetical order › List of commands › UTTI  UTTI  -  UTility line settling TIme）

```
UTTI {time}, {(util_name)}
```

### UTTI?（取自子主题 Commands in alphabetical order › List of commands › UTTI  UTTI  -  UTility line settling TIme）

```
UTTI? {(util_name)}
```

returns:

```
UTTI {time}, {(util_name)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › UTTI  UTTI  -  UTility line settling TIme）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98840.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：time | Specifies the wait time to change the utility line status using the UTST and FLSH command (in ms).
> 表内引用（2 条，供检索）：`UTST`（raw: `02.06.02.02.313_UTST__UTST__-__UTility_line_STate.md`） · `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › UTTI  UTTI  -  UTility line settling TIme）

```
UTTI 2.5,(filter)
```

This example sets the settling time of the utility line "filter" to 2.5 ms.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VALC  -  VALid Cycle range）

```
VALC? {(pinlist)}
```

returns:

```
VALC {map_state}, {start_cycle}, {no_of_cycles}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VALC  -  VALid Cycle range）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118752.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：map_state | Returns the current state of the error map. The state can be: INVL: Invalid - no error map details are available. (The setup has been changed, but n…

### Example（取自子主题 Commands in alphabetical order › List of commands › VALC  -  VALid Cycle range）

```
> VALC? (dpsPin)
< VALC CONS,0,700,(dpsPin)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VALD  -  VALid Data）

```
VALD? {map_id}, {(pinlist)}
```

returns:

```
VALD {map_state}, {map_id}, {start}, {number}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VALD  -  VALid Data）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98841.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：map_id | Determines the type of Error Map for which data is to be read out:
> 表内引用（3 条，供检索）：`FLBL`（raw: `02.06.02.02.123_FLBL__-__Failing_LaBeLs.md`） · `ERMP`（raw: `02.06.02.02.114_ERMP__-__ERror_MaP.md`） · `Pin Scale 5000 card`（raw: `../02.05_Test_Head_Cards/02.05.04.02_Pin_Scale_5000_card.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › VALD  -  VALid Data）

```
VALD? ERRM, (Q0,Q1,Q2,Q3)
```

returns:

```
VALD CONS, ERRM, 0, 1024, (Q0,Q1,Q2,Q3)
```

This example queries the error map and returns data between the cycles of 0 and 1024. The error map data is consistent with the current setup.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VALR  -  VALid Range）

```
VALR? {(pinlist)}
```

returns:

```
VALR {map_state}, {no_of_results}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VALR  -  VALid Range）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/97185.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：map_state | Returns the current state of the error map. The state can be: INVL: Invalid - no error map details are available. (The setup has been changed, but n…

### Example（取自子主题 Commands in alphabetical order › List of commands › VALR  -  VALid Range）

```
> VALR? (dpsPin)
< VALR CONS,10,(dpsPin)
```

### VCAT（取自子主题 Commands in alphabetical order › List of commands › VCAT  VCAT  -  VeCtor ATtachment）

VCAT {"label_name"}, {(port)}, {"attachment_type"}, {#spec(data)}

### VCAT?（取自子主题 Commands in alphabetical order › List of commands › VCAT  VCAT  -  VeCtor ATtachment）

```
VCAT? {"label_name"|ALL}, {(port)}, {"attachment_type"}
```

returns

```
VCAT {"label_name"}, {(port)}, {"attachment_type"}, {#spec(data)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VCAT  VCAT  -  VeCtor ATtachment）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/100378.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：18 行 × 3 列。
> 首行（上游原文）：label_name | The label must be of type MAIN or SVEC.

### Example 1（取自子主题 Commands in alphabetical order › List of commands › VCAT  VCAT  -  VeCtor ATtachment）

```
> vcat? "example",(@),"AreaPatternAttachment"
< VCAT "example", (@), "AreaPatternAttachment", #31190,(CP,I1,O1),1,std;
 1,(CP,I1,O1),-3,slow;
 4,(CP,I1,O1),2,fast;
 6,(CP,I1,O1),-3,slow;
 9,(CP,I1,O1),std,1;
```

The pattern of the example comprises 9 vectors (0 through 8). The last line refers to a virtual vector 9 which is needed for internal reasons. This vector need not be specified in the command, it is added internally.

### Example 2（取自子主题 Commands in alphabetical order › List of commands › VCAT  VCAT  -  VeCtor ATtachment）

```
> VCAT "scan_test",(@),"ScanInstanceAttachment", #2303,0,1,24,"chain_pattern 0","";
```

This example identifies a scan instance in the `scan_test` pattern, which is associated with the default port @. The length of the data stream is 30 bytes. The scan instance starts at the first X-vector of the fourth tester vector, its length is 24 X-vectors, the name of the scan test instance is `chain_pattern 0`, and the default scan structure block is used.

### Example 3（取自子主题 Commands in alphabetical order › List of commands › VCAT  VCAT  -  VeCtor ATtachment）

```
> VCAT? "myMainLabel", (myPort), "MarkerPatternAttachment"
< VCAT "myMainLabel", (myPort), "MarkerPatternAttachment", #250
 38, mySyncPoint,2,Pin1;
 71, mySecondSyncPoint,1,Pin1;
```

In this example, VCAT has attached two synchronization markers to pin Pin1 of the sequencer label `myMainLabel` at port `myPort`.

The two synchronization markers are `mySyncPoint` which is attached to the tester vector with the logical vector number 38 and `mySecondSyncPoint` which is attached to the vector with the logical vector number 71.

Synchronization takes account of place on the X-vector level. Therefore the specification of a marker contains an offset in X-vectors. If an x4-mode in assumed for the above example, the actual positions of the two markers in terms of X-vectors would be 38*4+2 = 154 and 71*4+1=285, respectively.

As the modification of the pattern is restricted to whole tester vectors the X-vector offset within the marker specification is fixed, but the tester vector offset will be updated if the pattern is modified.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VCLK  -  Verify CLocK）

```
VCLK? {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

returns:

```
VCLK {autocorrect}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VCLK  -  Verify CLocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98844.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › VCLK  -  Verify CLocK）

```
VCLK? 1,1,20,(@)
```

This example checks if a period of 20 ns will cause auto-correction to the edge placements in Timing Set 1 of Waveform Set 1 on any pin. If no auto-correction will occur the following string is returned:

```
VCLK 0
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VCYC  -  Valid CYCle）

```
VCYC? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
VCYC {start_cycle}, {no_of_cycles}, {seq_status}, {pin_oper_mode}, {(pinlist)}, {#spec(data)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VCYC  -  Valid CYCle）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98845.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 5 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. The scanning method and the range of values this paramete…

### Example（取自子主题 Commands in alphabetical order › List of commands › VCYC  -  Valid CYCle）

```
VCYC? 0, 5, (pin1)
```

returns:

```
VCYC 0,5,GENV,F160,(pin1),#9000000005\x0E\x0E\x0E\x0F\x0D\x0A
```

This example returns the physical waveform DC/DC power units in hex notation in the range of 0 to 5 cycles.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VDCG  -  Verify Device Cycle for Group）

```
VDCG? {waveform_set}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {waveform_set}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {specset_id}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {specset_id}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {wavetable_name}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {wavetable_name}, {dev_cyc_name}, {dev_cyc_len}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VDCG  -  Verify Device Cycle for Group）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98846.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 4 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › VDCG  -  Verify Device Cycle for Group）

```
VDCG? 1,ALL,(inputs)
```

returns:

```
VDCG 1,ALL,SLEN
```

This example checks the consistency of all device cycles for pins in the pin group "inputs" in waveform set 1. The test system replies that all device cycles for the specified group are consistently defined.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VDCN -  Vector Device Cycle Name）

VDCN {vec_No}, {"dev_cyc_name"}, {dev_cyc_len}, {repeat_count}, {(pinlist)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VDCN -  Vector Device Cycle Name）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98847.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：vec_No | A logical vector number of the selected label. Logical vector numbers count the active vectors of one label. The first active vector of a label has the…

### Example（取自子主题 Commands in alphabetical order › List of commands › VDCN -  Vector Device Cycle Name）

```
VDCN 93, "EXAMPL", 1, 15, (@)
```

This example downloads vector data resulting from the default values for the EXAMPL device cycle to all pins, starting at active vector 93. The download is repeated 15 times.

### VDCP（取自子主题 Commands in alphabetical order › List of commands › VDCP  VDCP   Vector Device Cycle Parameter）

VDCP {vec_no}, {"dev_cyc_name"}, {dev_cyc_len}, [ed_comp], {DD1}, {DD2}, {ED1}, {ED2}, {(pinlist)}

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VDCP  VDCP   Vector Device Cycle Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98848.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：vec_No | A logical vector number of the selected label. For the command, it determines the first active vector that will be overwritten. For the query, this par…

### Example（取自子主题 Commands in alphabetical order › List of commands › VDCP  VDCP   Vector Device Cycle Parameter）

```
> VDCP? 0,8,0,8,(S0_1)
< VDCP 0,"DNRZ",1,,F10,N,N,N,(S0_1)
< VDCP 1,"DNRZ",1,,F10,N,N,N,(S0_1)
< VDCP 2,"DNRZ",1,,F10,N,N,N,(S0_1)
< VDCP 3,"MYDC",2,,F00,N,N,N,(S0_1)
< VDCP 5,"MYDC",2,,F10,N,N,N,(S0_1)
< VDCP 7,"DNRZ",1,,F10,N,N,N,(S0_1)
> VDCP? 2,6,4,2,(S0_1)
< VDCP 5,"MYDC",2,,F10,N,N,N,(S0_1)
< VDCP 7,"DNRZ",1,,F10,N,N,N,(S0_1)
```

In the second call of VDCP? (the first call just serves to display the underlying situation) the range of interest starts at vector 6. Note that the reply starts with vector 5, and that the first occurrence of MYDC, which lies between vector 2 and vector 6, is not displayed.

### VECC（取自子主题 Commands in alphabetical order › List of commands › VECC  VECC  -  VECtor download Compressed）

```
VECC {applic}, {type} [, port], {address}, {length}, {(pin_or_port)}, {#spec(data)}
```

### VECC?（取自子主题 Commands in alphabetical order › List of commands › VECC  VECC  -  VECtor download Compressed）

```
VECC? {applic}, {type} [, port_list], {address}, [length], {(pinlist)}
```

returns:

```
VECC {applic}, {type} [, port], {address}, {length}, {(pin)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98850.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：applic | The parameter specifies the target area of the command, and the source area of the query. Possible values are:

### Example（取自子主题 Commands in alphabetical order › List of commands › VECC  VECC  -  VECtor download Compressed）

```
VECC? PARA,ALL,0,,(S0)
```

returns:

```
size: 21
data:
VECC PARA,ALL,0,,(S0)\x0A
size: 75
data:
VECD PARA,SM,0,56,(S0),#9000000016\x02Ee\x80\x02Ee\x814VX\x13Eu\x90\x00\x0A
status: 0
```

### VECD（取自子主题 Commands in alphabetical order › List of commands › VECD  VECD  -  VECtor Download）

```
VECD {applic}, {type} [, port], {address}, {length}, {(pin_or_port)}, {#spec(data)}
```

### VECD?（取自子主题 Commands in alphabetical order › List of commands › VECD  VECD  -  VECtor Download）

```
VECD? {applic}, {type} [, port_list], {address}, [length], {(pinlist)}
```

returns:

```
VECD {applic}, {type} [, port], {address}, {length}, {(pin)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98853.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：applic | The parameter specifies the target area of the command, and the source area of the query. Possible values are:

### Example（取自子主题 Commands in alphabetical order › List of commands › VECD  VECD  -  VECtor Download）

```
> VECD? PARA,SM,0,16,(OUT1)
< VECD PARA,SM,0,16,(OUT1),#9000000024\x0E\x0C\x0E\x0E\x0D\x0E\x0E\x0D\x0E\x0E\x0E\x0E
  \x0C\x0D\x0E\x0E
```

This example shows the answer as it is recorded in the MCDLog.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VNEC  -  Valid Number of Executed Cycles）

```
VNEC? {site_sel}, {value_format}, {(pin)}
```

Returns:

```
VNEC {site_sel}, {(pin)}, {value_data}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/344387.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：site_sel | Select sites. It can be a string of 1's and 0's; or "ALL" to specify all sites. The response is a string of 1's and 0's.

### Example（取自子主题 Commands in alphabetical order › List of commands › VNEC  -  Valid Number of Executed Cycles）

```
VNEC? ALL, ASC, ("pin1")
```

Returns:

```
VNEC "11",("pin1"),#138,8
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VPAR  -  Vectors in PARallel）

```
VPAR? {start_vec_No}, {stop_vec_No}
```

returns:

```
VPAR {cmd_No}, [frst_used_vec]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VPAR  -  Vectors in PARallel）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98860.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：start_vec_No | Defines the offset of the first vector to be searched from the start vector of the currently selected label. The specified address must not excee…

NISQ (Non-Interpretable SeQuence) indicates that the sequencer program does not respect its context conditions. This means, there is non-linear use of vectors, or there are partial "Match Begin" or "Match End" sequences (for example a WTER without its MBGN, a MJPE without its MEND - see the SQPG command). The label is no longer displayable by the Vector Setup in this case. No frst_used_vec parameter is returned when the parameter cmd_No is NISQ.

### Example（取自子主题 Commands in alphabetical order › List of commands › VPAR  -  Vectors in PARallel）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,10,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
> VPAR? 0,15
< VPAR 0,0
< VPAR 1,0
< VPAR 2,0
< VPAR 3,10
```

This example displays the sequencer instructions of the selected label before calling VPAR? in order to make its reply understandable.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VRCS  -  Valid ReConStruction）

```
VRCS? {reconstr_type}, [reconstr_cond,] {(pinlist)}
```

returns:

```
VRCS [reconstr_cond,] {reconstr_state}, [reconstr_oper,] {start_cycle}, {no_of_cycles}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98861.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：18 行 × 3 列。
> 首行（上游原文）：reconstr_type | The reconstruction type determines how test cycles are counted.
> 表内引用（1 条，供检索）：`FLBL`（raw: `02.06.02.02.123_FLBL__-__Failing_LaBeLs.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › VRCS  -  Valid ReConStruction）

```
VRCS? STRT, (@)
```

returns:

```
VRCS? REAL, 0, 437621, (@)
```

This example queries the number of reconstructed cycles, counting the cycles from the start of the test. The system replies that 437,621 cycles, starting from zero have been reconstructed, based on the last performed test.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VTIM  -  Verify TIMing）

```
VTIM? {waveform_set},{timing_set},{(pinlist)}
```

returns:

```
VTIM {status}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VTIM  -  Verify TIMing）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98862.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › VTIM  -  Verify TIMing）

The following example illustrates the working of VTIM? in a multi-port setup. The pins S1_1 and DS0_1 belong to the same port, and S1_2 belongs to another one.

```
> ETDS? "spec_port_1_port_2",ALL,,(S1_1,DS0_1,S1_2)
< ETDS "spec_port_1_port_2",1,,"d1:0 d2:30",(S1_1,DS0_1)
< ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(S1_1)
< ETDS "spec_port_1_port_2",2,,"d1:1 d2:12",(DS0_1)
< ETDS "spec_port_1_port_2",1,,"d1:-0.67 d2:1.33 d3:9.3",(S1_2)
```

This call of `ETDS?`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） shows that the edge timings of S1_1 and DS0_1 are the same in timing set 1, but not in timing set 2 of the port to which these pins belong.

```
> PCLK? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< PCLK "spec_port_1_port_2",1,50,(S1_1)
< PCLK "spec_port_1_port_2",2,20,(S1_1)
< PCLK "spec_port_1_port_2",1,50,(DS0_1)
< PCLK "spec_port_1_port_2",2,20,(DS0_1)
< PCLK "spec_port_1_port_2",1,16.667,(S1_2)
```

This call of `PCLK?`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） shows that the periods of S1_1 and DS0_1 are the same in the two timing sets of the port.

```
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 0
```

VTIM? returns 0 because of the different timings for S1_1 and DS0_1 in timing set 2.

```
> ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(DS0_1)
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 1
```

After changing the edge timing of DS0_1 in timing set 2 to the values of S1_1 with a call of `ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`）, VTIM? returns 1 although DS0_1 has a different timing in timing set 1 and in timing set 2, and S1_2, which belongs to another port, has different values altogether.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VWFG  -  Verify WaveForms in Groups）

There are three different ways to call VWFG?:

```
VWFG? {waveform_set}, ["dev_cyc_name"], {(pinlist)}
VWFG? {specset_id},["dev_cyc_name"],{(pinlist)}
VWFG? {wavetable_name}, ["dev_cyc_name"], {(pinlist)}
```

All three forms return:

```
VWFG {status}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VWFG  -  Verify WaveForms in Groups）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98863.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › VWFG  -  Verify WaveForms in Groups）

```
> VWFG? "spec_search_wtb","SBC",(ser_in)
< VWFG 1
> VWFG? "spec_search_wtb",,(ser_in)
< VWFG 0
```

According to this example, the waveform and device cycle definition for device cycle SBC are the same for the pins in the group ser_in within the wavetable spec_search_wtb, but this does not hold for all device cycles that are defined for the pins of this group.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › VWFS  -  Verify WaveForm Sets）

```
VWFS? {waveform_set_1},{waveform_set_2},{(pinlist)}
```

returns:

```
VWFS {status}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › VWFS  -  Verify WaveForm Sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98864.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：waveform_set_x | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, …
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › VWFS  -  Verify WaveForm Sets）

```
VWFS? 1,2,(DATA)
```

This example checks whether waveform sets 1 and 2 are the same for the pins in the group DATA. If they are the same the following string is returned:

```
VWFS 1,(DATA)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › WAIT -  WAIT）

```
WAIT {time}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › WAIT -  WAIT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98865.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：time | Enter a time in µs.

### Example（取自子主题 Commands in alphabetical order › List of commands › WAIT -  WAIT）

```
RLYC DC,PMU,(outputs); WAIT 1000; FTST?
```

This example causes the MCD to wait 1 ms (1000 µs) for the PMU relay to close before executing a functional test.

### WAVE（取自子主题 Commands in alphabetical order › List of commands › WAVE  WAVE  -  WAVEform）

```
WAVE {wvf_set}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
WAVE {specset_id|"multiport_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}, ALLOW_EQ
```

### WAVE?（取自子主题 Commands in alphabetical order › List of commands › WAVE  WAVE  -  WAVEform）

```
WAVE? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {(pinlist)}
```

returns:

```
WAVE {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › WAVE  WAVE  -  WAVEform）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98869.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? …
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › WAVE  WAVE  -  WAVEform）

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

This example first defines a logical waveform with the index 2 for waveform set 1. The waveform uses the data parameter D11, the fixed action 0, and the complement C11 of D11. Then two physical waveforms are defined for logical waveform 2, which are referenced by the physical waveform DC/DC power units 4 and 5. Waveform 4 drives to 0 at edge d1, to 0 at d3, and to 1 at d4. Waveform 5 drives to 1 at edge d1, to 0 at d3, and to 0 at d4.

### WFDF（取自子主题 Commands in alphabetical order › List of commands › WFDF  WFDF  -  WaveForm DeFinition）

```
WFDF {wvf_set}, {wfIndex}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### WFDF?（取自子主题 Commands in alphabetical order › List of commands › WFDF  WFDF  -  WaveForm DeFinition）

```
WFDF? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDF {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98871.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 4 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…
> 表内引用（4 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `WAVE`（raw: `02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） · `Restrictions for drive edges`（raw: `02.06.06.01.03.01.02.01_Restrictions_for_drive_edges.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › WFDF  WFDF  -  WaveForm DeFinition）

```
> WFDF 1,2,N,N,D11,N,N,N,(D0,D2,D2,D3)
```

This example defines a waveform referenced by waveform index 2. The waveform uses the drive data and tri-state parameter 1. Edge number 3 provides the timing for this waveform. The definitions are made for waveform set 1 and for pins D0 to D3.

### WFDS（取自子主题 Commands in alphabetical order › List of commands › WFDS  WFDS  -  WaveForm Definition String）

```
WFDS {wvf_set}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
WFDS {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### WFDS?（取自子主题 Commands in alphabetical order › List of commands › WFDS  WFDS  -  WaveForm Definition String）

```
WFDS? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDS {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › WFDS  WFDS  -  WaveForm Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98872.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 4 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…

### Example（取自子主题 Commands in alphabetical order › List of commands › WFDS  WFDS  -  WaveForm Definition String）

```
> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)
> WFDS 1,1,,"r4:EE1",(io)
> WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)

> WFDS? 1,ALL,,(@)
< WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)
< WFDS 1,1,,"r4:EE1",(io)
< WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › WFEX  -  WaveForm EXpected data）

```
WFEX? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
WFEX {start_cycle}, {no_of_cycles}, {timing_set}, [err_type], {(pinlist)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98873.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：39 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. The scanning method and the range of values this paramete…

### Example（取自子主题 Commands in alphabetical order › List of commands › WFEX  -  WaveForm EXpected data）

```
WFEX? 0, 1, (pin1)
```

returns:

```
WFEX 0,1,3,NOER,(pin1),#9000000006\x0B\x0A\x1A\x1F\x00\x00\x0A
```

This example returns edge action drive and expected data (in binary notation) for one cycle. To decode the data, convert it into binary notation and use the lists above.

The data in binary format is:

```
0000 1011  0000 1010  0001 1010
0001 1111  0000 0000  0000 0000
```

The edge actions are RZ on the drive edges 1 and 2 and a window compare to 0 on the receive edges 3 and 4. Edges 5 and 6 are unused.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › WFRE  -  WaveForm REceived data）

```
WFRE? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
WFRE {start_cycle}, {no_of_cycles}, {timing_set}, [err_type], {(pinlist)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98874.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：41 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. The scanning method and the range of values this paramete…
> 表内引用（1 条，供检索）：`VALD? - (VALid Data)`（raw: `02.06.02.02.316_VALD__-__VALid_Data.md`）

If reconstruction is not possible (code 110 on bits 2, 1, 0), there has been more than one edge or window compare within a single test system cycle.

If error bit 7 is set, an error has occurred on at least one of these edge or window compares.

### Example（取自子主题 Commands in alphabetical order › List of commands › WFRE  -  WaveForm REceived data）

```
WFRE? 0, 1, (pin1)
```

returns:

```
WFRE 0,1,3,ERON,(pin1),#9000000006\x0B\x0A\x9B\x9F\x00\x00\x0A
```

This example returns edge action drive and expected data (in binary notation) for one cycle. To decode the data, convert it into binary notation and use the lists above.

The data in binary format is:

```
0000 1011  0000 1010  1001 1011
1001 1111  0000 0000  0000 0000
```

The edge actions are RZ on the drive edges 1 and 2 and a failed window compare (received value: 1) on the receive edges 3 and 4. Edges 5 and 6 are unused.

The WFRE? answer will be split if the requested cycle range is greater than the available error map information, as shown below:

 !`Example`（raw: `../../../../raw/23378.png`）

```
WFRE? 0,15000, (pin1)
WFRE 0, 100, 1, NOER, (pin1), BinData           (a)
WFRE 100, 9900, 1, ERON, (pin1), BinData        (b)
WFRE 10000, 5000, 1, NOER, (pin1), BinData      (c)
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › WFUD -  WaveForm UnDefine）

```
WFUD {wvf_set},{wfIndex},{(pinlist)}
WFUD {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › WFUD -  WaveForm UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98875.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › WFUD -  WaveForm UnDefine）

```
WFUD 1,2,(D0,D2,D2,D3)
```

This example deletes a logical waveform defined for waveform set 1 and for pins `D0` to `D3`, referenced by waveform index 2.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › WRST -  Waveform ReSeT）

```
WRST {waveform_set}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › WRST -  Waveform ReSeT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98876.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › WRST -  Waveform ReSeT）

```
WRST 3
```

This example resets all waveform and timing entries for all pins for waveform set 3.

### WSDM（取自子主题 Commands in alphabetical order › List of commands › WSDM  WSDM  -  Waveform Set Display Mode）

```
WSDM {waveform_set}, {display_mode}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › WSDM  WSDM  -  Waveform Set Display Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98877.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum nu…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › WSDM  WSDM  -  Waveform Set Display Mode）

```
> WSDM? "spec_1", (port_1)
< WSDM  "spec_1", 0
```

This example queries the display mode of port port_1 in the multiport specification spec_1. The reply shows that it is set to the "classic" display mode.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › WSDN -  Wait Setup DoNe）

WSDN

### Example（取自子主题 Commands in alphabetical order › List of commands › WSDN -  Wait Setup DoNe）

```
FLSH
WSDN
```

The WSDN command returns if all buffered setup downloading, triggered by the FLSH command, is completed.

### WSUS（取自子主题 Commands in alphabetical order › List of commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS {waveform_set}
```

### WSUS?（取自子主题 Commands in alphabetical order › List of commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS?
```

returns:

```
WSUS {waveform_set}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › WSUS  WSUS  -  Waveform Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98878.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number. This is the highest number currently allocated to a waveform set or the highest number of a set you want to load. The number…
> 表内引用（1 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Commands in alphabetical order › List of commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS 3
```

This example sets the number of used waveform sets to 3.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › IDN  -  IDeNtify）

```
*IDN?
```

returns:

```
*IDN {id_string}
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › IDN  -  IDeNtify）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98880.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：id_string | The string contains the model, the firmware revision number, and the revision date.

### Example（取自子主题 Commands in alphabetical order › List of commands › IDN  -  IDeNtify）

```
*IDN?
```

returns:

```
*IDN Firmware  s/w rev. 3.1.0+95x, 06-Aug-01
```

### Syntax（取自子主题 Commands in alphabetical order › List of commands › OPT  -  hardware OPTions）

```
*OPT?
```

returns:

```
*OPT {`hardware_type`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_hardware_type`）}, {`board_no`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_board_no`）}, {`board_type`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_board_type`）}, {`board_id`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_board_id`）}, `[phys_location`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_phys_location`）], `[clk_board`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_clk_board`）], `[chan_1_info_1`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_chan_x_info_y`）], [chan_1_info_2], ... [chan_16_info_1], [chan_16_info_2]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98881.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：hardware_type | Returns type of the test head: PS_2CC or CS_2CC Compact test head containing two card cages. PS_4CC or CS_4CC Small test head containing four ca…

### Example（取自子主题 Commands in alphabetical order › List of commands › OPT  -  hardware OPTions）

```
> *OPT?
< *OPT JN_S,1,CNTR,254,1100,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
< *OPT JN_S,11,CLK,254,1115,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
< *OPT JN_S,101,JNIO,254,1102,11,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,
< *OPT JN_S,102,JNIO,254,1102,11,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,
```

The reply from the *OPT? query has been generated in offline mode. The board IDs are set to 254.

### Syntax（取自子主题 Commands in alphabetical order › List of commands › RST -  ReSeT）

```
*RST [type]
```

### Parameters（取自子主题 Commands in alphabetical order › List of commands › RST -  ReSeT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98882.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：type | not used | Enforces a disconnect (AC relay is open) All DPS sets, except the default set, will be deleted. All resources (for example objects defined wit…

### Example（取自子主题 Commands in alphabetical order › List of commands › RST -  ReSeT）

```
*RST
```

Resets the software and the hardware.

### Example（取自子主题 Pin configuration setup commands › Concepts of Configuration setup › Defining pin groups）

The following example contains both fixed and expression based pin group definitions:

```
> DFGP X,(SI1,SI2,SO1,SO2),(SCAN)
> DFGP O,(O1,SO1,SO2),(OUT)
> DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGE? (SCAN_OUT)
< DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGP? (SCAN_OUT)
< DFGP O,(SO1,SO2),(SCAN_OUT)
```

The DFGE command defines SCAN_OUT as the intersection of SCAN and OUT.

### Example（取自子主题 Pin configuration setup commands › Concepts of Configuration setup › Defining ports）

See the `DFPT`（raw: `02.06.02.02.66_DFPT__DFPT__-__DeFine_PorT.md`） command.

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › CHIN  -  CHannel INformation）

```
CHIN? {channel_nr|ALL}
```

returns:

CHIN {channel_nr}, {channel_type}, [phys_location], {board_no}, [clk_board], [chan_info_1], [chan_info_2]

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › CHIN  -  CHannel INformation）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98502_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：24 行 × 3 列。
> 首行（上游原文）：channel_nr | The number that identifies the channel. Specify ALL if you want information about all channels. For a digital channel, specify it with the test sys…
> 表内引用（3 条，供检索）：`DFPN, DFPN? - (DeFine Pin Name) for the number)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） · `DFPS, DFPS? - (DeFine Power Supply)`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） · `*OPT? - (hardware OPTions)`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md`）

### Examples（取自子主题 Pin configuration setup commands › List of configuration commands › CHIN  -  CHannel INformation）

```
CHIN? 10901
```

returns:

```
CHIN 10901,PSIO,120601,109,21,512,0
```

```
CHIN? ALL
```

  Return (for example):

```
CHIN 10101,PYIO,110301,101,11,3551,0
CHIN 10102,PYIO,110302,101,11,3551,0

CHIN 21701,DPS128HC,-1,217,31,191,0
CHIN 21702,DPS128HC,-1,217,31,191,0

```

### CONF（取自子主题 Pin configuration setup commands › List of configuration commands › CONF  CONF  -  CONFiguration）

```
CONF ["context",]{pin_type},[pin_oper_mode],{(pinlist)}


```

### CONF?（取自子主题 Pin configuration setup commands › List of configuration commands › CONF  CONF  -  CONFiguration）

```
CONF? ["context"|ALL,] {(pinlist)}
```

returns:

```
CONF ["context",]{pin_type},{pin_oper_mode},{(pinlist)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › CONF  CONF  -  CONFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98510_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 6 列，含嵌套表。
> 首行（上游原文）：context | This extra parameter specifies a mode context. If it is omitted, the default mode context DEFAULT is set or read. If DEFAULT is the only context defin…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98510_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：I | Configures a drive pin.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98510_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：DCSIGNAL | In the query this indicates that the pin is associated with a DC Scale channel and has been configured in PMU mode with DFPN.

### Example 1（取自子主题 Pin configuration setup commands › List of configuration commands › CONF  CONF  -  CONFiguration）

```
> CONF IO,F160,(D0,D1)
```

This example configures pins `D0` and `D1` as bidirectional pins operating in Standard Mode for the default mode context.

### Example 2（取自子主题 Pin configuration setup commands › List of configuration commands › CONF  CONF  -  CONFiguration）

```
> CONF? (sdd,vdd)
< CONF DC,DCSIGNAL,(sdd)
< CONF DC,POWER,(vdd)
```

This example queries the DC Scale channels `sdd` and `vdd`, which were set with `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） to PMU mode (`DCSIGNAL`) and with `DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） to DPS mode (`POWER`), respectively.

### CTXT（取自子主题 Pin configuration setup commands › List of configuration commands › CTXT  CTXT  -  ConTeXT）

```
CTXT {action},{"name"}
```

### CTXT?（取自子主题 Pin configuration setup commands › List of configuration commands › CTXT  CTXT  -  ConTeXT）

```
CTXT?ALL
```

returns:

```
CTXT {DEFINE},{"name"}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › CTXT  CTXT  -  ConTeXT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98513_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：action | Specifies the action. Possible values are:

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › CTXT  CTXT  -  ConTeXT）

```
> CTXT? ALL
< CTXT DEFINE,"DEFAULT"
< CTXT DEFINE,"differential"
< CTXT DEFINE,"PdrvNPrcv"
```

### DFGE（取自子主题 Pin configuration setup commands › List of configuration commands › DFGE  DFGE  -  DeFine Group by Expressions）

```
DFGE {group_type}, {"group_expression"}, {(pin_group)}
```

### DFGE?（取自子主题 Pin configuration setup commands › List of configuration commands › DFGE  DFGE  -  DeFine Group by Expressions）

```
DFGE? {(pin_group)}
```

returns:

```
DFGE {group_type}, {("group_expression")}, {(pin_group)}
```

for expression-based groups, and

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

for digital fixed groups.

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DFGE  DFGE  -  DeFine Group by Expressions）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98544_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 4 列。
> 首行（上游原文）：group_type | Defines the type of pins in the group. This can be:

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › DFGE  DFGE  -  DeFine Group by Expressions）

```
> DFGP? (SCAN)
< DFGP X,(SI1,SI2,SO1,SO2),(SCAN)
> DFGP? (OUT)
< DFGP O,(O1,SO1,SO2),(OUT)
> DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGE? (SCAN_OUT)
< DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGP? (SCAN_OUT)
< DFGP O,(SO1,SO2),(SCAN_OUT)
```

This example defines a group called SCAN_OUT which contains the pins that occur both in pin groups OUT and SCAN. Note that you must use the DFGP? query to display the pins of SCAN_OUT. DFGE? returns the group definition.

The same result would be obtained with the definition

```
> DFGE O,"OUT - O1",(SCAN_OUT)
```

### DFGP（取自子主题 Pin configuration setup commands › List of configuration commands › DFGP  DFGP  -  DeFine GrouP）

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### DFGP?（取自子主题 Pin configuration setup commands › List of configuration commands › DFGP  DFGP  -  DeFine GrouP）

```
DFGP? {(pin_group)}
```

returns:

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DFGP  DFGP  -  DeFine GrouP）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98546_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：pin_type | Defines the type of pins in the group. This can be:

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › DFGP  DFGP  -  DeFine GrouP）

```
DFGP O,(Q0,Q1,Q2,Q3),(outputs)
```

This example defines a group called outputs which contains pins Q0, Q1, Q2 and Q3.

### DFLV（取自子主题 Pin configuration setup commands › List of configuration commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV [resourceSpecifier,] [mode,] {value}
```

### DFLV?（取自子主题 Pin configuration setup commands › List of configuration commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV? [resourceSpecifier] [, mode]
```

returns

```
DFLV VIL,STD,value
DFLV VIH,STD,value
DFLV VIHH,STD,value
DFLV VOL,STD,value
DFLV VOH,STD,value
DFLV VOL_DIFF,STD,value
DFLV VOH_DIFF,STD,value
DFLV VT,STD,value
DFLV VCOM,STD,value
DFLV REC_OFFSET,STD,value
DFLV REC_SWING,STD,value
```

if neither parameter resourceSpecifier nor parameter mode have been specified.

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DFLV  DFLV  -  DeFaultLeVel）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/349982_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 4 列，含嵌套表。
> 首行（上游原文）：resourceSpecifier | The extra parameter specifies the resource to be set or queried. The following resources are supported: Resource specifier | Description
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/349982_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：Resource specifier | Description

### Example 1: Resource and mode specified（取自子主题 Pin configuration setup commands › List of configuration commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV VIL,STD,100

```

This example sets the default value for the VIL resource in STD mode to 100 mV. Other default values are not modified.

### Example 2: Resource specified, mode omitted（取自子主题 Pin configuration setup commands › List of configuration commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV VIL,100
DFLV VIH,200
```

This example sets the default value for the VIL resource to 100 mV, and VIH to 200 mV. As no operating mode is specified, the values are applied only for the STD mode.

### Example 3: Reset single resource（取自子主题 Pin configuration setup commands › List of configuration commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV VIL, RESET
```

Sets the default value for the VIL resources to the technology defined default value for all operating modes. This overwrites potential user-defined values by the initial system value.

### Example 4: Reset all default values to the technology defined values and query all values（取自子主题 Pin configuration setup commands › List of configuration commands › DFLV  DFLV  -  DeFaultLeVel）

```
DFLV RESET
DFLV? ALL, ALL
```

returns

```
DFLV VIL,STD,2250
DFLV VIH,STD,2500
DFLV VIHH,STD,0
DFLV VOL,STD,2250
DFLV VOH,STD,2500
DFLV VOL_DIFF,STD,0
DFLV VOH_DIFF,STD,0
DFLV VT,STD,2500
DFLV VCOM,STD,2500
DFLV REC_OFFSET,STD,1200
DFLV REC_SWING,STD,3200
```

for the cmos technology.

### DFPC（取自子主题 Pin configuration setup commands › List of configuration commands › DFPC  DFPC  -  DeFine Pin Comment）

```
DFPC {(pin)}, {"comment"}
```

### DFPC?（取自子主题 Pin configuration setup commands › List of configuration commands › DFPC  DFPC  -  DeFine Pin Comment）

```
DFPC? {(pinlist)}
```

returns:

```
DFPC {(pin)}, {"comment"}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DFPC  DFPC  -  DeFine Pin Comment）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131109_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：pin | In the command, this is the pin to which a comment is to be added. In the query reply, it is the pin whose comment is returned.

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › DFPC  DFPC  -  DeFine Pin Comment）

```
> DFPC (pin1), "This is a comment to pin1"
> DFPC? (pin1,pin2)
< DFPC (pin1), "This is a comment to pin1"
```

Since no comment has been defined for pin `pin2`, it is ignored in the reply.

### DFPN（取自子主题 Pin configuration setup commands › List of configuration commands › DFPN  DFPN  -  DeFine Pin Name）

```
DFPN ["connectionSet",] {channelNo_1|(list_of_DC_scale_channels)}, ["pinNo"], {(pinName)}
```

### DFPN?（取自子主题 Pin configuration setup commands › List of configuration commands › DFPN  DFPN  -  DeFine Pin Name）

```
DFPN? {(pinlist)}
```

returns:

```
DFPN {channelNo_1|(list_of_DC_scale_channels)}, ["pinNo"], {(pinName)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DFPN  DFPN  -  DeFine Pin Name）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98550_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：connectionSet | This parameter is currently not used. This extra string parameter adds the ability to define several pins containing the same DC Scale channel i…
> 表内引用（2 条，供检索）：`DDIC`（raw: `02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md`） · `Pogo pin assignment - Utility pogo blocks`（raw: `../02.03_DUT_board_design_reference/02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.md`）

### Example 1（取自子主题 Pin configuration setup commands › List of configuration commands › DFPN  DFPN  -  DeFine Pin Name）

```
> DFPN 10101,"1",(Clock)
> DFPN 10102,"2",(D0)
> DFPN? (@)
< DFPN 10101,"1",(Clock)
< DFPN 10102,"2",(CD0)
```

The above example allocates the `Clock` pin to channel 10101 and allocates pin `D0` to channel 10102, and then queries these definitions. The device pin numbers allocated are 1 and 2 respectively.

```
DFPN (11901, 11902),,(vee)
```

This example defines ganging for DC Scale channels in PMU mode.

### DFPS（取自子主题 Pin configuration setup commands › List of configuration commands › DFPS  DFPS  -  DeFine Power Supply）

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

### DFPS?（取自子主题 Pin configuration setup commands › List of configuration commands › DFPS  DFPS  -  DeFine Power Supply）

```
DFPS? {(pinlist)}
```

returns:

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DFPS  DFPS  -  DeFine Power Supply）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98551_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：dps_channel | The test system channel number of the DPS channel to be configured. The channel is to be defined as follows: For external device power supplies, t…

### Example 1（取自子主题 Pin configuration setup commands › List of configuration commands › DFPS  DFPS  -  DeFine Power Supply）

```
DFPS 11,POS,(Vee)
```

This example connects device pin Vee to channel 1 of DPS board 1. The DPS output polarity is positive.

### Example 2（取自子主题 Pin configuration setup commands › List of configuration commands › DFPS  DFPS  -  DeFine Power Supply）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98551_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 1 列。
> 首行（上游原文）：DFPS (10101, 10102),POS,(vee)

Both lines define the same master/slave configuration for DC Scale channels in DPS mode. They just use different notations. Note the five digit channel numbers.

### Example 3（取自子主题 Pin configuration setup commands › List of configuration commands › DFPS  DFPS  -  DeFine Power Supply）

```
DDIC CONN, (104GO, 105GI)
DFPS (10403, 10404, 10501, 10502),POS,(vee)
```

This example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across two boards.

### Example 4（取自子主题 Pin configuration setup commands › List of configuration commands › DFPS  DFPS  -  DeFine Power Supply）

```
DDIC CONN, (104GO, 105GI, 105GO, 106GI)
DFPS (10403, 10404, 10502, 10503, 10504, 10601),POS,(vee)
```

This example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across three boards.

### Example 5（取自子主题 Pin configuration setup commands › List of configuration commands › DFPS  DFPS  -  DeFine Power Supply）

```
DDIC CONN,(230GO, 227GI)
DFPS (23004, 22701),POS,(VDDCI)
```

This example specifies the ganging of channels across two DC Scale UHC4 cards.

### DFPT?（取自子主题 Pin configuration setup commands › List of configuration commands › DFPT  DFPT  -  DeFine PorT）

```
DFPT? {(portlist)}
```

returns:

```
DFPT {(pinlist)}, {(port)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DFPT  DFPT  -  DeFine PorT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98552_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：pinlist | Pin name or names. If more than one pin is required, the names must be separated with a comma. The @ character can be used to refer to all configured …

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › DFPT  DFPT  -  DeFine PorT）

```
DFPT? (port_1, port_2)
```

returns:

```
DFPT (CP_1,DS7_1,DS0_1,I/O7_1,...,I/O0_1,Q7_1,
Q0_1,S1_1,S0_1,_MR_1),(port_1)
DFPT (CP_2,DS7_2,DS0_2,I/O7_2,...,I/O0_2,Q7_2,
Q0_2,S1_2,S0_2,_MR_2),(port_2)
```

### DFUP（取自子主题 Pin configuration setup commands › List of configuration commands › DFUP  DFUP  -  DeFine Utility Purpose）

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### DFUP?（取自子主题 Pin configuration setup commands › List of configuration commands › DFUP  DFUP  -  DeFine Utility Purpose）

```
DFUP? {(purpose_name)}
```

returns

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DFUP  DFUP  -  DeFine Utility Purpose）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98559_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ch_No_list | Utility line channel numbers to be defined as the members of a utility purpose and specified with five digits. The channels must be separated with …

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › DFUP  DFUP  -  DeFine Utility Purpose）

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

This example defines a utility purpose AWG_CNCT and activates its standard settings.

The members and the setting values are as follows:

```
Member:      16501  16502  16503  16504
---------------------------------------
Setting:     0      1      1      0
```

### DFUT（取自子主题 Pin configuration setup commands › List of configuration commands › DFUT  DFUT  -  DeFine UTility line）

```
DFUT {ch_No}, {type}, {(util_name)}
```

### DFUT?（取自子主题 Pin configuration setup commands › List of configuration commands › DFUT  DFUT  -  DeFine UTility line）

```
DFUT? {(util_name)}
```

returns

```
DFUT {ch_No}, {type}, {(util_name)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DFUT  DFUT  -  DeFine UTility line）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98560_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ch_No | Channel number of the utility line specified with five or three digits. In the five‑digit format, the first three digits specify the utility pogo block.…

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › DFUT  DFUT  -  DeFine UTility line）

```
DFUT 16504,w,(filter)
```

This example assigns the name `filter` and operating mode w to utility line 4 of the first utility pogo block.

### DSCP（取自子主题 Pin configuration setup commands › List of configuration commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP `[device_cycle`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_device_cycle`）], `[waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）], `[timing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_timing_set`）], `[level_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_level_set`）], `[dps_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_dps_set`）], `[pmu_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_pmu_set`）],
                        `[devicecycle_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_devicecycle_set`）], `[routing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_routing_set`）], `[period_res_prec`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_period_res_prec`）],

```

### DSCP?（取自子主题 Pin configuration setup commands › List of configuration commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP?
```

returns:

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
       {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
       [period_res_compatibility_model]
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › DSCP  DSCP  -  Define System Control Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98578_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：device_cycle | The device_cycle parameter is an integer that defines the absolute maximum number of device cycles that you can create for one pin.Default: 256Ma…
> 表内引用（2 条，供检索）：`waveform sets and wavetables`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） · `waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › GCTX  -  Get ConTeXt）

```
GCTX? {setup_type},[setup_comp]
```

returns:

GCTX {setup_type}{,setup_nr|"name"},"[context_name]"

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › GCTX  -  Get ConTeXt）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98611_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：setup_type | The type of the setup component for which the mode context is queried. Possible values are:

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › GCTX  -  Get ConTeXt）

```
> GCTX? TIM,101
< GCTX TIM,101,"High-Speed"
```

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › HWTY  -  HardWare TYpe）

```
HWTY?
```

returns:

```
HWTY {machine}, {testhead}, {dut_if}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › HWTY  -  HardWare TYpe）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98636_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：machine | Returns PS

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › HWTY  -  HardWare TYpe）

```
> HWTY?
< HWTY VS,TH_4CC,SOC
```

### PACT（取自子主题 Pin configuration setup commands › List of configuration commands › PACT  PACT  -  Parallel ACTivities control）

PACT {control}, {site|ALL}

PACT {"site_string"}

### PACT?（取自子主题 Pin configuration setup commands › List of configuration commands › PACT  PACT  -  Parallel ACTivities control）

```
PACT?
```

returns

```
PACT {control}, {site}
```

Or:

```
PACT?STR
```

returns

```
PACT {"site_string"}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › PACT  PACT  -  Parallel ACTivities control）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98678_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：control | The control parameter is:

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › PACT  PACT  -  Parallel ACTivities control）

```
> PACT ACTIVE, 1
> PACT MASKED, 2
> PACT MASKED, 3
```

This example masks site 2 and site 3, and makes site 1 active.

```
> PACT?
< PACT ACTIVE,1
< PACT MASKED,2
< PACT MASKED,3
> PACT? STR
< PACT "100"
```

This example shows the impact of the optional STR parameter for the query.

### PALS（取自子主题 Pin configuration setup commands › List of configuration commands › PALS  PALS  -  Pin ALlocation for multiple Sites）

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

### PALS?（取自子主题 Pin configuration setup commands › List of configuration commands › PALS  PALS  -  Pin ALlocation for multiple Sites）

```
PALS? {site}, {(pinlist)}
```

returns:

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › PALS  PALS  -  Pin ALlocation for multiple Sites）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98680_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：site | The site parameter is an integer that defines the number of the site where the channels are to be defined. The integer must be greater than 1 (channels f…
> 表内引用（4 条，供检索）：`DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） · `DFPN, DFPN? - (DeFine Pin Name)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） · `DFUT, DFUT? - (DeFine UTility line)`（raw: `02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md`） · `DDIC`（raw: `02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.md`）

### Examples（取自子主题 Pin configuration setup commands › List of configuration commands › PALS  PALS  -  Pin ALlocation for multiple Sites）

```
PALS 2,10201,,(Clock)
PALS 2,10202,,(D0)
```

The above example allocates the Clock pin for site 2 to channel 10201 and allocates pin D0 for site 2 to channel 10202.

```
PALS 2,(10101, 10102),,(dc1)
```

This example defines a master/slave configuration for DC Scale channels. The first channel is the master.

```
DDIC CONN, (104GO, 105GI)
DDIC CONN, (105GO, 107GI)
PALS 2,(10403, 10404, 10501, 10502, 10503, 10504, 10701, 10702),,(dc1)
```

This example defines a master/slave configuration for DC Scale UHC4 channels across boards. The first channel is the master.

```
DFAN "MCE231,2,i","",(av8_bbrx_b+)
DFAN "MCE231,6,i","",(av8_bbrx_b-)
PALS 2,"MCE231,1,i",,(av8_bbrx_b+)
PALS 3,"MCE231,3,i",,(av8_bbrx_b+)
PALS 4,"MCE231,4,i",,(av8_bbrx_b+)
PALS 2,"MCE231,5,i",,(av8_bbrx_b-)
PALS 3,"MCE231,7,i",,(av8_bbrx_b-)
PALS 4,"MCE231,8,i",,(av8_bbrx_b-)
```

This example defines a pair of differential pins av8_bbrx_b+ and av8_bbrx_b- using the MCE card in 4 sites.

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › PFND  -  Pin FiND）

```
PFND? [group_type,] {(pin)}
```

returns:

```
PFND {group_type}, {(list)}, {(pin)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › PFND  -  Pin FiND）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98686_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：group_type | The group type can be PRT (for "port") or DIFF (for "differential pair"). PRT is the default.

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › PFND  -  Pin FiND）

```
> PFND? (I/O1_1)
< PFND PRT,(port_1,port_1.CP_1),(I/O1_1)
> PFND? DIFF,(P+)
< PFND DIFF,(P+,P-),(P+)
```

### PQFC（取自子主题 Pin configuration setup commands › List of configuration commands › PQFC  PQFC  -  Parallel Query FoCus）

```
PQFC {site}
```

### PQFC?（取自子主题 Pin configuration setup commands › List of configuration commands › PQFC  PQFC  -  Parallel Query FoCus）

```
PQFC?
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › PQFC  PQFC  -  Parallel Query FoCus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98688_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：site | The site parameter is single integer representing the number of the site that has or shall have the query focus.

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › PQFC  PQFC  -  Parallel Query FoCus）

```
PQFC 2
```

This example sets the query focus to site 2.

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › PRLT  -  request Parallel ResuLTs）

```
PRLT? ["exec_context",] {site}
```

returns:

```
PRLT {site}, {"result"}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › PRLT  -  request Parallel ResuLTs）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98689_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts.
> 表内引用（1 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › PRLT  -  request Parallel ResuLTs）

```
PRLT? ALL
```

returns:

```
PRLT ALL, "PF0"
```

In this example, site 1 passed the last test, site 2 failed it, and site 3 was masked during the test.

### PSSL（取自子主题 Pin configuration setup commands › List of configuration commands › PSSL  PSSL   Power Supply Safety Limits）

```
PSSL [min_voltage | OFF], [max_voltage | OFF], [max_source_current | OFF], [max_sink_current | OFF], {(pin_list)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › PSSL  PSSL   Power Supply Safety Limits）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143177_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：min_voltage | Lowest allowed voltage in V. Must be ≤ 0.
> 表内引用（2 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） · `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › PSSL  PSSL   Power Supply Safety Limits）

```
PSSL OFF,OFF,OFF,OFF,(DPS_1)
PSSL -2,5,0.5,0.5,(DPS_2)
PSSL -1.5,3,0.5,0.5,(SIG_1A)
```

### PSTE（取自子主题 Pin configuration setup commands › List of configuration commands › PSTE  PSTE  -  Parallel SiTe Enable）

```
PSTE {sites}
```

### PSTE?（取自子主题 Pin configuration setup commands › List of configuration commands › PSTE  PSTE  -  Parallel SiTe Enable）

```
PSTE? [STR]
```

returns

```
PSTE {sites|"site_string"}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › PSTE  PSTE  -  Parallel SiTe Enable）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98711_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：sites | The sites parameter is an integer that specifies the number of sites (to be) configured. The maximum is 1024. For more information, refer to Number of s…
> 表内引用（2 条，供检索）：`Number of sites`（raw: `../../01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md#_116532__r_numberOfSites`） · `SmarTest system parameters - default values and limits`（raw: `../../01_Getting_started/01.04_SmarTest_system_parameters_-_default_values_and_limits/01.04_SmarTest_system_parameters_-_default_values_and_limits.md`）

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › PSTE  PSTE  -  Parallel SiTe Enable）

```
> PSTE 3
```

This example configures three sites (site 1, site 2, and site 3).

```
> PSTE? STR
< PSTE "101"
```

This example says that three sites are configured, but that only two of them (site 1 and site 3) are available for testing. Site 2 uses a channel that is listed in the MCDIgnore file, and therefore cannot be used for testing.

### STME（取自子主题 Pin configuration setup commands › List of configuration commands › STME  STME  -  SiTe Match Enable）

```
STME {ON|OFF|AUTO|FAST},
```

### STME?（取自子主题 Pin configuration setup commands › List of configuration commands › STME  STME  -  SiTe Match Enable）

```
STME?
```

returns:

STME {ON|OFF|FAST),

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › STME  STME  -  SiTe Match Enable）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98760_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：ON | Turns the site match function on.
> 表内引用（1 条，供检索）：`Fast Sync`（raw: `02.06.07.01.08.04.03.03_Fast_Sync.md`）

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › STME  STME  -  SiTe Match Enable）

```
> STME AUTO,
> STME?
< STME ON,
```

This example sets the site match function to AUTO, then reads the actual setting. Since the actual setting is ON, the pin configuration cannot contain a shared digital channel.

```
>SQST OFF
>NIFE 2
>STME FAST,
>STME ON,
```

This example configures the Fast Sync feature, and sets two independent Fast Sync ports on each test processor.

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › UDEF -  UnDEFine pin）

```
UDEF {(pinlist)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UDEF -  UnDEFine pin）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98821_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pinlist | Consists of single or multiple pin names or the symbol @ which removes all pins. If more than one pin is required, the names must be separated with a …

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UDEF -  UnDEFine pin）

```
UDEF (Q3)
```

This example causes pin Q3 to be removed from the current configuration. If you subsequently redefine the channel using the same or a different name, it assumes its former operating mode and the pin type OFF.

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › UDGP -  UnDefine GrouP）

```
UDGP {(group)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UDGP -  UnDefine GrouP）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98822_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：group | Defines the name of the group of pins to be removed. The symbol @ can be used to dismantle all groups. If more than one group is to be removed, the name…

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UDGP -  UnDefine GrouP）

```
UDGP (Qout)
```

This command dismantles the group entitled Qout.

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › UDPS -  Undefine DPS pin）

```
UDPS {(pinlist)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UDPS -  Undefine DPS pin）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98823_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pinlist | Consists of single or multiple pin names or the symbol @ which undefines all DPS pins. If more than one pin is to be removed, the names must be separa…

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UDPS -  Undefine DPS pin）

```
UDPS (Vee)
```

This example removes pin Vee from the setup. The software saves the level data associated with the DPS channel. Therefore if you redefine the channel using the same or a different name, the DPS settings are immediately restored.

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › UDUP -  UnDefine Utility Purpose）

```
UDUP {(purpose_name)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UDUP -  UnDefine Utility Purpose）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98830_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：purpose_name | Specifies the utility purpose name or names to be undefined. The symbol @ removes all utility purpose definitions. If more than one name is to be…

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UDUP -  UnDefine Utility Purpose）

```
UDUP (@)
```

This command undefines all defined utility purpose names.

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › UDUT -  UnDefine UTility line）

```
UDUT {(util_name)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UDUT -  UnDefine UTility line）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98831_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：util_name | Specifies the utility line name or names to be undefined. The symbol @ removes all utility line definitions. If more than one name is to be removed,…

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UDUT -  UnDefine UTility line）

```
UDUT (@)
```

This command undefines all defined utility line names.

### UDVP（取自子主题 Pin configuration setup commands › List of configuration commands › UDVP -  UnDefine Virtual Pin）

```
UDVP (pinlist)
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UDVP -  UnDefine Virtual Pin）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/353743.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 4 列。
> 首行（上游原文）：pinlist | The names of the pins to undefine. The @ symbol can be used to undefine all pins that were previously defined by the VPIN command.

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UDVP -  UnDefine Virtual Pin）

- To undefine a virtual pin:

```
> UDVP (VPIN1)
```

- To undefine multiple virtual pins:

```
> UDVP (VPIN2,VPIN3)
```

- To undefine all virtual pins:

```
> UDVP (@)
```

### UPAS（取自子主题 Pin configuration setup commands › List of configuration commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

```
UPAS {site}, ["{setting}"], {(purpose_name)}
```

### UPAS?（取自子主题 Pin configuration setup commands › List of configuration commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

```
UPAS? {site}, {(purpose_name)}
```

returns:

```
UPAS {site}, "{setting}", {(purpose_name)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98832_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：site | The site parameter is an integer that defines the number of the site where the channels are to be defined. The integer must be greater than 1. When speci…
> 表内引用（1 条，供检索）：`DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`）

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

```
> DFUP (101,102,103,104),"11XX",(AWG_CNCT)
> UPAS 2,"XX11",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "11XX", (AWG_CNCT)
> PSFC 2
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "XX11", (AWG_CNCT)
```

In this example, the `DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`） command defines a utility purpose AWG_CNCT and output states for site 1. The UPAS command defines the output states of AWG_CNCT for site 2. First the settings of site 1 are activated. Then the setup focus is restricted to site 2, and the output states for site 2 are activated.

### UPST（取自子主题 Pin configuration setup commands › List of configuration commands › UPST  UPST  -  Utility Purpose STate）

```
UPST ["setting"], {(purpose_name)}
```

### UPST?（取自子主题 Pin configuration setup commands › List of configuration commands › UPST  UPST  -  Utility Purpose STate）

```
UPST? {(purpose_name)}
```

returns:

```
UPST "{setting}", {(purpose_name)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UPST  UPST  -  Utility Purpose STate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98833_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：setting | The optional parameter specifies the status of the utility lines in the utility purpose. The status is determined with the following specifiers: 0: Se…

Name of the utility purpose to be set or read.

For the query, you can specify multiple names, which must be separated by a comma.

Specifying the symbol @ returns the definitions of all utility purposes.

   | Note All utility lines that are set with `UTST`（raw: `02.06.02.02.313_UTST__UTST__-__UTility_line_STate.md`） or UPST will be switched in parallel when the `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`） command is performed. If the `WSDN`（raw: `02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md`） command is used immediately after FLSH, the time span during which execution will pause equals the longest settling time that is defined for any of the switched utility lines (with `UTTI`（raw: `02.06.02.02.314_UTTI__UTTI__-__UTility_line_settling_TIme.md`）) or purposes (with `UPTI`（raw: `02.06.02.02.307_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md`）).

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UPST  UPST  -  Utility Purpose STate）

```
UPST ,(AWG_CNCT)
FLSH
WSDN
UPST? (AWG_CNCT)
```

returns

```
UPST "0110",(AWG_CNCT)
```

This example sets the utility purpose "AWG_CNCT" to the hardware, then reads the state of the utility purpose.

### UPTI（取自子主题 Pin configuration setup commands › List of configuration commands › UPTI  UPTI  -  Utility Purpose settling TIme）

```
UPTI {time}, {(purpose_name)}
```

### UPTI?（取自子主题 Pin configuration setup commands › List of configuration commands › UPTI  UPTI  -  Utility Purpose settling TIme）

```
UPTI? {(purpose_name)}
```

returns:

```
UPTI {time}, {(purpose_name)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UPTI  UPTI  -  Utility Purpose settling TIme）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98835_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：time | Specifies the wait time to change the utility line status using the UPST and FLSH commands (in ms). 0 ... 2 147 483.646 [ms]

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UPTI  UPTI  -  Utility Purpose settling TIme）

```
UPTI 2.5,(AWG_CNCT)
```

This example sets the settling time of the utility purpose "AWG_CNCT" to 2.5 ms.

### UTST（取自子主题 Pin configuration setup commands › List of configuration commands › UTST  UTST  -  UTility line STate）

```
UTST {value}, {(util_name)}
```

### UTST?（取自子主题 Pin configuration setup commands › List of configuration commands › UTST  UTST  -  UTility line STate）

```
UTST? type, {(util_name)}
```

returns:

```
UTST {value}, {(util_name)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UTST  UTST  -  UTility line STate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98839_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：value | Specifies the output (desired) status of the utility line with the specifier 0 or 1. 0: High output 1: Low output

Specifies the utility line name or names to be set or read.

In the query, specifying @ returns all utility lines.

If more than one name is required, the names must be separated by commas.

   | Note All utility lines that are set with UTST or `UPST`（raw: `02.06.02.02.305_UPST__UPST__-__Utility_Purpose_STate.md`） will be switched in parallel when the `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`） command is performed. If the `WSDN`（raw: `02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md`） command is used immediately after FLSH, the time span during which execution will pause equals the longest settling time that is defined for any of the switched utility lines (with `UTTI`（raw: `02.06.02.02.314_UTTI__UTTI__-__UTility_line_settling_TIme.md`）) or purposes (with `UPTI`（raw: `02.06.02.02.307_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md`）).

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UTST  UTST  -  UTility line STate）

```
UTST 1,(Filt1,Filt2)
UTST 0,(Filt3,Filt4)
FLSH
WSDN
UTST? w,(Filt1,Filt2,Filt3,Filt4)
```

will return:

```
UTST 1,(Filt1,Filt2)
UTST 0,(Filt3,Filt4)
```

This example sets the utility lines "Filt1" and "Filt2" to high output, and "Filt3" and "Filt4" to low output.

### UTTI（取自子主题 Pin configuration setup commands › List of configuration commands › UTTI  UTTI  -  UTility line settling TIme）

```
UTTI {time}, {(util_name)}
```

### UTTI?（取自子主题 Pin configuration setup commands › List of configuration commands › UTTI  UTTI  -  UTility line settling TIme）

```
UTTI? {(util_name)}
```

returns:

```
UTTI {time}, {(util_name)}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › UTTI  UTTI  -  UTility line settling TIme）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98840_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：time | Specifies the wait time to change the utility line status using the UTST and FLSH command (in ms).
> 表内引用（2 条，供检索）：`UTST`（raw: `02.06.02.02.313_UTST__UTST__-__UTility_line_STate.md`） · `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`）

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › UTTI  UTTI  -  UTility line settling TIme）

```
UTTI 2.5,(filter)
```

This example sets the settling time of the utility line "filter" to 2.5 ms.

### VPIN（取自子主题 Pin configuration setup commands › List of configuration commands › VPIN  VPIN  -  Virtual PIN）

```
VPIN (pinlist)
```

### VPIN?（取自子主题 Pin configuration setup commands › List of configuration commands › VPIN  VPIN  -  Virtual PIN）

```
VPIN? ([(pinlist) | @]}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › VPIN  VPIN  -  Virtual PIN）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/353731.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 4 列。
> 首行（上游原文）：pinlist | The name to be allocated to the pin. The query returns the name of the virtual pins that have been defined. The @ symbol can be used with the VPIN? qu…

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › VPIN  VPIN  -  Virtual PIN）

- To define a virtual pin:

```
> VPIN (VPIN1)
```

- To define multiple virtual pins:

```
> VPIN (VPIN2,VPIN3)
```

- To list all defined virtual pins:

```
> VPIN? (@)
```

Returns:

```
< VPIN (VPIN1,VPIN2,VPIN3)
```

- To check for the existence of specific virtual pins:

```
> VPIN? (VPIN2,VPIN4,VPIN6)
```

Returns:

```
< VPIN (VPIN2)
```

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › IDN  -  IDeNtify）

```
*IDN?
```

returns:

```
*IDN {id_string}
```

### Parameters（取自子主题 Pin configuration setup commands › List of configuration commands › IDN  -  IDeNtify）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98880_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：id_string | The string contains the model, the firmware revision number, and the revision date.

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › IDN  -  IDeNtify）

```
*IDN?
```

returns:

```
*IDN Firmware  s/w rev. 3.1.0+95x, 06-Aug-01
```

### Syntax（取自子主题 Pin configuration setup commands › List of configuration commands › OPT  -  hardware OPTions）

```
*OPT?
```

returns:

```
*OPT {`hardware_type`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_hardware_type`）}, {`board_no`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_board_no`）}, {`board_type`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_board_type`）}, {`board_id`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_board_id`）}, `[phys_location`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_phys_location`）], `[clk_board`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_clk_board`）], `[chan_1_info_1`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md#_98881__r_chan_x_info_y`）], [chan_1_info_2], ... [chan_16_info_1], [chan_16_info_2]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98881_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：hardware_type | Returns type of the test head: PS_2CC or CS_2CC Compact test head containing two card cages. PS_4CC or CS_4CC Small test head containing four ca…

### Example（取自子主题 Pin configuration setup commands › List of configuration commands › OPT  -  hardware OPTions）

```
> *OPT?
< *OPT JN_S,1,CNTR,254,1100,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
< *OPT JN_S,11,CLK,254,1115,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
< *OPT JN_S,101,JNIO,254,1102,11,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,
< *OPT JN_S,102,JNIO,254,1102,11,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,,8,
```

The reply from the *OPT? query has been generated in offline mode. The board IDs are set to 254.

### DSCP（取自子主题 Routing Setup Commands › List of routing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP `[device_cycle`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_device_cycle`）], `[waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）], `[timing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_timing_set`）], `[level_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_level_set`）], `[dps_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_dps_set`）], `[pmu_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_pmu_set`）],
                        `[devicecycle_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_devicecycle_set`）], `[routing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_routing_set`）], `[period_res_prec`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_period_res_prec`）],

```

### DSCP?（取自子主题 Routing Setup Commands › List of routing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP?
```

returns:

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
       {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
       [period_res_compatibility_model]
```

### Parameters（取自子主题 Routing Setup Commands › List of routing setup commands › DSCP  DSCP  -  Define System Control Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98578_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：device_cycle | The device_cycle parameter is an integer that defines the absolute maximum number of device cycles that you can create for one pin.Default: 256Ma…
> 表内引用（2 条，供检索）：`waveform sets and wavetables`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） · `waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）

### Example（取自子主题 Routing Setup Commands › List of routing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

### SRPR（取自子主题 Routing Setup Commands › List of routing setup commands › SRPR  SRPR  -  Set Routing PRimary）

```
SRPR {set}
```

### SRPR?（取自子主题 Routing Setup Commands › List of routing setup commands › SRPR  SRPR  -  Set Routing PRimary）

SRPR?

### Parameters（取自子主题 Routing Setup Commands › List of routing setup commands › SRPR  SRPR  -  Set Routing PRimary）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99079_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：set | An identification number of the routing set. This is an integer from 1 to the maximum number defined by the DSCP command. If the NONE specifier is specifi…

### Example（取自子主题 Routing Setup Commands › List of routing setup commands › SRPR  SRPR  -  Set Routing PRimary）

```
SRPR 4
```

This example sets the routing set 4 as the primary routing set.

### Syntax（取自子主题 Routing Setup Commands › List of routing setup commands › UDRS -  UnDefine Routing Set）

```
UDRS {set}
```

### Parameters（取自子主题 Routing Setup Commands › List of routing setup commands › UDRS -  UnDefine Routing Set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99081_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：set | An identification number of the routing set. This is an integer from 1 to the maximum number defined by the DSCP command. If the ALL specifier is specifie…
> 表内引用（1 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Routing Setup Commands › List of routing setup commands › UDRS -  UnDefine Routing Set）

```
UDRS ALL
```

### Syntax（取自子主题 Level Setup Commands › List of level setup commands › APRM -  Activate PRiMary sets）

```
APRM {mode}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › APRM -  Activate PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98485_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：mode | Selects the activation mode:

### Example（取自子主题 Level Setup Commands › List of level setup commands › APRM -  Activate PRiMary sets）

```
APRM CNL
```

### CLMP（取自子主题 Level Setup Commands › List of level setup commands › CLMP  CLMP  -  CLaMP level）

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### CLMP?（取自子主题 Level Setup Commands › List of level setup commands › CLMP  CLMP  -  CLaMP level）

```
CLMP? {level_set|level_set_id}, {(pinlist)}
```

returns:

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › CLMP  CLMP  -  CLaMP level）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98505_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：level_set | The identification number of the level set in which you want the levels to be included. The number must not exceed the maximum number of level sets …

### Example（取自子主题 Level Setup Commands › List of level setup commands › CLMP  CLMP  -  CLaMP level）

```
CLMP 1,ON,-10,5100,(Q0,Q1,Q2,Q3)
```

This example sets the clamp levels for level set 1 for pins Q0, Q1, Q2 and Q3. The low clamp level is set to -10 mV, and the high clamp level is set to 5100 mV.

### DFSP（取自子主题 Level Setup Commands › List of level setup commands › DFSP  DFSP  -  DeFine Sampling Profile）

```
DFSP [meas_resource,] {measure_type}, {measure_range}, {sampling_rate}, [average_factor], [keep_range,] {(pinlist)}
```

### DFSP?（取自子主题 Level Setup Commands › List of level setup commands › DFSP  DFSP  -  DeFine Sampling Profile）

```
DFSP? {(pinlist)}
```

returns

```
DFSP [meas_resource,] {measure_type}, {measure_range},{sampling_rate}, [average_factor], [keep_range,] {(pinlist)}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › DFSP  DFSP  -  DeFine Sampling Profile）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124994_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：meas_resource | The measurement resource. It can be: PMU - The default value

### Example 1: Current measurements（取自子主题 Level Setup Commands › List of level setup commands › DFSP  DFSP  -  DeFine Sampling Profile）

```
DFSP CURR,0.5,2048,2,(@)
```

or

```
DFSP CURR,40,2048,,KEEP,(dps1)
```

### Example 2: Voltage measurements（取自子主题 Level Setup Commands › List of level setup commands › DFSP  DFSP  -  DeFine Sampling Profile）

```
DFSP VOLT,2,50,8,(dps1)
```

or

```
DFSP VOLT,2,50,,(@)
```

### DPRL（取自子主题 Level Setup Commands › List of level setup commands › DPRL  DPRL  -  Default PRimary Level sets）

```
DPRL {level_set}, {dps_set}, [screen_select]
```

### DPRL?（取自子主题 Level Setup Commands › List of level setup commands › DPRL  DPRL  -  Default PRimary Level sets）

```
DPRL?
```

returns:

```
DPRL {level_set}, {dps_set}, [screen_select]
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › DPRL  DPRL  -  Default PRimary Level sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98569_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：level_set | Level Set number.

### Example（取自子主题 Level Setup Commands › List of level setup commands › DPRL  DPRL  -  Default PRimary Level sets）

```
DPRL?
```

returns:

```
DPRL 1,2,LEV
```

On sending a query, the system reports that the default primary level set is 1 and the default primary DPS set is 2.

### DRLV（取自子主题 Level Setup Commands › List of level setup commands › DRLV  DRLV  -  DRive LeVel）

```
DRLV {level_set_no | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### DRLV?（取自子主题 Level Setup Commands › List of level setup commands › DRLV  DRLV  -  DRive LeVel）

```
DRLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
DRLV {level_set | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › DRLV  DRLV  -  DRive LeVel）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98577_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：level_set_no | The identification number of the level set (fixed levels) in which you want the levels to be included. The number must not exceed the maximum num…
> 表内引用（2 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

For card specifications, like level ranges, see `Digital Cards`（raw: `../02.02_Specifications/02.02.04_Digital_Cards.md`）, for example:

- `Pin Scale 1600`（raw: `../02.02_Specifications/02.02.04.01.03_PS1600_driver.md`）
- `Pins Scale 5000`（raw: `../02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md`）

### Example 1（取自子主题 Level Setup Commands › List of level setup commands › DRLV  DRLV  -  DRive LeVel）

```
DRLV 1,-1750,-850,(Q0,Q1,Q2,Q3)
```

This example sets the driver levels for level set 1 for pins Q0, Q1, Q2 and Q3. The logic 0 level is set to -1750 mV and the logic 1 level to -850 mV.

### Example 2（取自子主题 Level Setup Commands › List of level setup commands › DRLV  DRLV  -  DRive LeVel）

```
DRLV 1,-1750,-850,8000,(avi64Pin1)
```

This example shows how the 8 V drive range of an AVI64 pin is selected.

### DSUS（取自子主题 Level Setup Commands › List of level setup commands › DSUS  DSUS  -  Dps Sets USed）

```
DSUS {ds_No}
```

### DSUS?（取自子主题 Level Setup Commands › List of level setup commands › DSUS  DSUS  -  Dps Sets USed）

```
DSUS?
```

returns:

```
DSUS {ds_No}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › DSUS  DSUS  -  Dps Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98580_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：ds_No | DPS Set Number. This is the highest number currently allocated to a DPS set, or the highest number of set you want to load. The number you type must not…

### Example（取自子主题 Level Setup Commands › List of level setup commands › DSUS  DSUS  -  Dps Sets USed）

```
DSUS 2
```

This example defines a maximum of 2 DPS sets.

### ENSP（取自子主题 Level Setup Commands › List of level setup commands › ENSP  ENSP  -  ENable Sampling Profile）

```
ENSP {operation_state},{(pinlist)}
```

### ENSP?（取自子主题 Level Setup Commands › List of level setup commands › ENSP  ENSP  -  ENable Sampling Profile）

```
ENSP? {(pinlist)}
```

returns

```
ENSP {operation_state},{(pinlist)}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › ENSP  ENSP  -  ENable Sampling Profile）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125000_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：operation_state | Specifies the operation state (ON|OFF)

### Example（取自子主题 Level Setup Commands › List of level setup commands › ENSP  ENSP  -  ENable Sampling Profile）

```
ENSP ON,(@)
```

or

```
ENSP ON,(dps1,dps2)
```

or

```
ENSP OFF,(@)
```

### EQFC（取自子主题 Level Setup Commands › List of level setup commands › EQFC  EQFC  -  EQualization and Filter Configuration）

```
EQFC {level_set_no|level_set_id|ALL|PRM} ,{filter_parameter|ALL_specifier}, {offset_value|filter_value}, {(pinList)}
```

### EQFC?（取自子主题 Level Setup Commands › List of level setup commands › EQFC  EQFC  -  EQualization and Filter Configuration）

```
EQFC? {level_set_no|level_set_id|ALL|PRM} ,{filter_parameter|ALL_specifier|ALL}, {value}, {(pinList)}

```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › EQFC  EQFC  -  EQualization and Filter Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112905_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：level_set_no | The identification number of the level set (fixed levels) in which you want the filter/equalization values to be included. The number must not ex…
> 表内引用（4 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `Impact and characteristics of the equalization parameter filter_parameter`（raw: `02.06.02.02.107_EQFC__EQFC__-__EQualization_and_Filter_Configuration.md#_112905__table_filter_parameter_710x`） · `Possible values for ALL_specifier`（raw: `02.06.02.02.107_EQFC__EQFC__-__EQualization_and_Filter_Configuration.md#_112905__table_all_specifier`） · `Valid ranges for the equalization parameters (set value using "offset_value")`（raw: `02.06.02.02.107_EQFC__EQFC__-__EQualization_and_Filter_Configuration.md#_112905__table_offset_value_710x`）

Impact and characteristics of the equalization parameter filter_parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112905_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 4 列。
> 首行（上游原文）：Value | Description | PS1600 | PS5000

Possible values for ALL_specifier
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112905_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：Value | Description | Modified parameter

Valid ranges for the equalization parameters (set value using "offset_value")
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112905_2.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：Equalization amplitude | PS1600 | PS5000

n/a

   | -19% …17% |

The offset for the equalization amplitude is given in percentage related to the swing value.

### Example（取自子主题 Level Setup Commands › List of level setup commands › EQFC  EQFC  -  EQualization and Filter Configuration）

```
EQFC 1, LPFI, 0.080, (@)
EQFC 1, EQI1, 75.5, (pin1,pin2)
```

```
EQFC? 1, ALL, (pin1,pin2)
```

```
EQFC 1, EQI1, 75.5,(pin1,pin2)
EQFC 1, EQI2, 0,(pin1,pin2)
EQFC 1, EQI3, 0,(pin1,pin2)
EQFC 1, EQO1, 0,(pin1,pin2)
EQFC 1, EQO2, 0,(pin1,pin2)
EQFC 1, EQO3, 0,(pin1,pin2)
EQFC 1, LPFI, 0,(pin1,pin2)
EQFC 1, LPFO, 0.080,(pin1,pin2)
```

### Syntax（取自子主题 Level Setup Commands › List of level setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › EQFS -  EQuation FileS command transfer）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98592_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification to use:

### Example（取自子主题 Level Setup Commands › List of level setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

This example loads the level equation file from /tmp/level_equation.

### EQSP（取自子主题 Level Setup Commands › List of level setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP {spec_type}, {part}, {#spec(data)}
```

### EQSP?（取自子主题 Level Setup Commands › List of level setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP?{spec_type}, {part}
```

returns:

```
EQSP {spec_type}, {part}, {#spec(data)}
```

if these are not empty, for backward compatibility.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98593_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：spec_type | The mandatory parameter defines which specification type to use. Use: LEV to specify levels TIM to specify timing

### Example（取自子主题 Level Setup Commands › List of level setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

The following example queries the current wavetables:

```
> EQSP? TIM,WVT
< EQSP TIM,WVT,#9000000127WAVETBL table1  # derived from waveform set 1

  PINS Pin1 Pin2
  WFDS 0  "d1:D11"
  1    0   .   .   .
  2    1   .   .   .
  BWDS ""

  @
```

### Syntax（取自子主题 Level Setup Commands › List of level setup commands › FTCG  FTCG  -  Functional Test ConfiGure）

FTCG

```
FTCG {parameter}, {mode}, {(portlist)}
```

  FTCG?

```
FTCG? {parameter}, {(@@)}
```

returns:

```
FTCG {parameter}, {mode}, {(portlist)}
```

  Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98606_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：parameter | The parameter to be used is SKPR (SKip PRimaries).

### Example（取自子主题 Level Setup Commands › List of level setup commands › FTCG  FTCG  -  Functional Test ConfiGure）

The following example illustrates the dependence of the FTCG command on the current sequencing group definitions.

```
> SQLB "MP_burst1",MPBU,28,31,"SG1",(clock)
> SQLB "MP_burst1",MPBU,28,29,"SG2",(data1)
> SQLB "MP_burst1",MPBU,31,32,"SG2",(data2)
> SQLB "MP_burst2",MPBU,32,33,"SG1",(clock)
> SQLB "MP_burst2",MPBU,30,31,"SG1",(data1)
> SQLB "MP_burst2",MPBU,33,34,"SG2",(data2)
> FTCG SKPR,ON,(clock)
> FTCG SKPR,NEVER,(data2)
> SPRM "cont_clock",,,
> SQSL "MP_burst1"
> SQGB ACQF,0
> FTST?
...
> SQSL "MP_burst2"
> FTST?
...
```

In the first functional test, sequencing group `SG1` only contains the port `clock`, and therefore activation of primary sets is suppressed at the start of `MP_burst1` only for `clock`, whereas it is enforced for ports `data1` and `data2`. In the second test, `SG1` contains both `clock` and `data1`, and therefore activation is suppressed for both these ports at the start of `MP_burst2`, and enforced only for `data2`.

### LSUS（取自子主题 Level Setup Commands › List of level setup commands › LSUS  LSUS  -  Level Sets USed）

```
LSUS {level_set_no}
```

### LSUS?（取自子主题 Level Setup Commands › List of level setup commands › LSUS  LSUS  -  Level Sets USed）

```
LSUS? [level_set_no]
```

returns:

```
LSUS {level_set_no}
```

or:

```
LSUS? [equation_set_no]
```

returns:

```
LSUS {level_set_no}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › LSUS  LSUS  -  Level Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98641_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：level_set_no | Level Set Number. This is the highest number currently allocated to a level set or the highest number of set you want to load. The number you typ…
> 表内引用（1 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Level Setup Commands › List of level setup commands › LSUS  LSUS  -  Level Sets USed）

```
LSUS 4
```

This example defines a maximum of 4 level sets.

### LSUX（取自子主题 Level Setup Commands › List of level setup commands › LSUX  LSUX  -  Level Sets Used eXtended）

```
LSUX {level_set_no|SWAP|NONE}
```

### LSUX?（取自子主题 Level Setup Commands › List of level setup commands › LSUX  LSUX  -  Level Sets Used eXtended）

```
LSUX?
```

returns:

```
LSUX {level_set_no}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › LSUX  LSUX  -  Level Sets Used eXtended）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98642_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：level_set_no | Level Set Number. If the number is smaller than the current value of LSUS then LSUX is set to this value. Otherwise it is set to the current valu…

### Example（取自子主题 Level Setup Commands › List of level setup commands › LSUX  LSUX  -  Level Sets Used eXtended）

```
LSUX 4
```

This example defines a maximum of 4 level sets.

### MERL（取自子主题 Level Setup Commands › List of level setup commands › MERL  MERL  -  Message ERror Limits）

```
MERL [error_limit], [message_limit]
```

### MERL?（取自子主题 Level Setup Commands › List of level setup commands › MERL  MERL  -  Message ERror Limits）

```
MERL?
```

returns:

```
MERL [error_limit], [message_limit]
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › MERL  MERL  -  Message ERror Limits）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98649_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：error_limit | The maximum number of errors that will be logged. An integer in the range 1 to 30000.Default value is 10.

### Example（取自子主题 Level Setup Commands › List of level setup commands › MERL  MERL  -  Message ERror Limits）

MERL 30,30

This example sets both the error and the message limits to 30.

### PSLV（取自子主题 Level Setup Commands › List of level setup commands › PSLV  PSLV  -  Power Supply LeVel）

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

  Note If equation based testing is being used, you specify a DPS set ID instead of a DPS set number.  Note PSLV ALL only applies changes to all non-equation-based DPS sets.

### PSLV?（取自子主题 Level Setup Commands › List of level setup commands › PSLV  PSLV  -  Power Supply LeVel）

```
PSLV? {dps_No|dps_set_id}, {(pinlist)}
```

returns:

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

 Note PSLV? ALL returns information for non-equation-based DPS sets only.

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › PSLV  PSLV  -  Power Supply LeVel）

Note The settling time parameter (setup_time) of the PSLV command and the rise_... and fall_... parameters of the `PSSR, PSSR? -(Power Supply Slew Rate)`（raw: `02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md`） command exclude each other. This also applies to the t_ms equation parameter (see `DPSPINS`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md`） and `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）).

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98702_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：dps_No | Needed for non-equation-based setup.
> 表内引用（1 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`）

### Example（取自子主题 Level Setup Commands › List of level setup commands › PSLV  PSLV  -  Power Supply LeVel）

```
PSLV 1,5.2,0.5,HIZ,15,(Vee)
```

This example sets the following parameters for device pin Vee:

- DPS set 1
- A voltage of 5.2 V
- A current limit of 0.5 A
- Minimum current limit when the test system is disconnected
- A setup time of 15 ms

### PSSR（取自子主题 Level Setup Commands › List of level setup commands › PSSR  PSSR  - Power Supply Slew Rate）

```
PSSR {dps_No|dps_set_id}, [rise_tm_per_v], [rise_settm], [fall_tm_per_v], [fall_settm], [rise_t_per_v_c2c], [rise_setup_t_c2c], [fall_t_per_v_c2c], [fall_setup_t_c2c], (pinlist)
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › PSSR  PSSR  - Power Supply Slew Rate）

Note The rise_... and fall_... parameters of the PSSR command and the settling time parameter (setup_time) of the `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`） command exclude each other. This also applies to the t_ms equation parameter (see `DPSPINS`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md`） and `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）). Note All time values have a resolution of microseconds (floating point values are rounded to three decimal places).

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/120504_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 2 列。
> 首行（上游原文）：dps_No | Needed for non-equation-based setup. The identification number of the DPS set which you want to modify. The number must not exceed the maximum number a…
> 表内引用（1 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`）

### Example（取自子主题 Level Setup Commands › List of level setup commands › PSSR  PSSR  - Power Supply Slew Rate）

```
PSSR PRM,10,50,20,70,(Vcc)
```

This example sets the following parameters for the primary set of DPS pin Vcc:

- rise_tm_per_v = 10 ms/V
- rise_settm = 50 ms
- fall_tm_per_v = 20 ms/V
- fall_settm = 70 ms

### Syntax（取自子主题 Level Setup Commands › List of level setup commands › RCLS  -  ReCeive Level Sensitivity）

```
RCLS? {test}, {pass_value}, [limit], {(pinlist)}
```

returns:

```
RCLS {value_specifier}, {result_value}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › RCLS  -  ReCeive Level Sensitivity）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98716_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 4 列。
> 首行（上游原文）：test | This parameter is one of the following:

### Example（取自子主题 Level Setup Commands › List of level setup commands › RCLS  -  ReCeive Level Sensitivity）

```
RCLS? H,3000,6000,(Q0)
```

returns:

```
RCLS EQ,5300
```

In this example a search was made to find the high level threshold between 3V and 6V. The pass/fail transition was located at 5.3V.

### RCLV（取自子主题 Level Setup Commands › List of level setup commands › RCLV  RCLV  -  ReCeive LeVel）

```
RCLV {level_set_no | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### RCLV?（取自子主题 Level Setup Commands › List of level setup commands › RCLV  RCLV  -  ReCeive LeVel）

```
RCLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
RCLV {level_set | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › RCLV  RCLV  -  ReCeive LeVel）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98717_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：level_set | The identification number of the level set in which you want the low and high threshold levels to be included. The number must not exceed the maximu…
> 表内引用（3 条，供检索）：`DSCP, DSCP? - (Define System Control Parameter)`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

For card specifications, like level ranges, see `Digital Cards`（raw: `../02.02_Specifications/02.02.04_Digital_Cards.md`）, for example:

- `Pin Scale 1600`（raw: `../02.02_Specifications/02.02.04.01.03_PS1600_driver.md`）
- `Pins Scale 5000`（raw: `../02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md`）

### Example 1（取自子主题 Level Setup Commands › List of level setup commands › RCLV  RCLV  -  ReCeive LeVel）

```
RCLV 1,-1300,-750,(Q0)
```

This example sets the low level compare threshold for pin Q0 to -1300 mV and the high level compare threshold to -750 mV.

### Example 2（取自子主题 Level Setup Commands › List of level setup commands › RCLV  RCLV  -  ReCeive LeVel）

```
TERM 1,,,,,,HRV,(avi64Pin1)
RCLV 1,-1300,-750,3000,(avi64Pin1)
```

This example for an AVI64 pin sets the low level compare threshold to -1300 mV, the high level compare threshold to -750 mV, and the range to the 3 V range.

### Syntax（取自子主题 Level Setup Commands › List of level setup commands › RSET -  ReSET）

```
RSET {specifier}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › RSET -  ReSET）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98723_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：specifier | The specifier can be:
> 表内引用（1 条，供检索）：`UHCM`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）

### Example（取自子主题 Level Setup Commands › List of level setup commands › RSET -  ReSET）

```
RSET TIM
```

This example resets all waveform sets and timing sets and loads the hardware with the default vector rate and edge placement values. Only waveform set 1 and timing set 1 in waveform set 1 is active.

### Syntax（取自子主题 Level Setup Commands › List of level setup commands › SDSC  -  Set number DeSCriptions）

```
SDSC? {spec_type}, {type}, [setup_comp_1], [setup_comp_2], ["description"]
```

returns:

```
SDSC {spec_type}, {type}, [setup_comp_1], [setup_comp_2], {"description"}
```

Alternatively, for multiport specifications:

```
SDSC? {TIM}, {type}, [setup_comp_1], {"multi-port_spec"}, ["description"][, (portlist)]
```

returns:

```
SDSC {TIM}, {type}, [setup_comp_1], {"multi-port_spec"}, {"description"}, {(port)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：21 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

The following table explains the interpretation of the setup_comp_1 and setup_comp_2 parameters for every accepted value pair of the spec_type and type parameters:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 4 列。
> 首行（上游原文）：spec_type | type | setup_comp_1 | setup_comp_2

### Example 1（取自子主题 Level Setup Commands › List of level setup commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,,,
< SDSC TIM,EQN,1,,"gross_func_eqn"
< SDSC TIM,EQN,2,,"specs_search_eqn"
< SDSC TIM,EQN,3,,"speed_eqn"
```

This example returns all defined equation sets.

### Example 2（取自子主题 Level Setup Commands › List of level setup commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,2,"spec_port_1_port_2",,(port_1)
< SDSC TIM,EQN,1,"spec_port_1_port_2",
     "gross_func_eqn",(port_1)
```

This example returns the equation set that is associated with port port_1 in the multiport specification

spec_port_1_port_2. Note that the setup_comp_1 parameter is ignored.

### SLDO（取自子主题 Level Setup Commands › List of level setup commands › SLDO -  Switch Level and Dps Order）

```
SLDO {order}, [report]
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › SLDO -  Switch Level and Dps Order）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98735_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：order | This parameter sets the switching order mode:

### Example（取自子主题 Level Setup Commands › List of level setup commands › SLDO -  Switch Level and Dps Order）

```
SLDO CVDL, AMBI
```

This example switches either the DPS voltage values or the level voltage values first when changing from one DPS or level set to the next depending on which of the three above mentioned cases occur and reports any ambiguous case.

### SPRM（取自子主题 Level Setup Commands › List of level setup commands › SPRM  SPRM  -  Set PRiMary sets）

```
SPRM [waveform_set_no], [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or:

```
SPRM {timing_specset_id}, [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or, for multiport specifications:

```
SPRM {"multi-port_spec"}, [timing_set_no|"timing_set_list"], [level_set_id|level_set_no],[dps_set_id|dps_set_no] [,(port)]
```

### SPRM?（取自子主题 Level Setup Commands › List of level setup commands › SPRM  SPRM  -  Set PRiMary sets）

```
SPRM?
```

returns:

```
SPRM {waveform_set_no}, {timing_set_no}, {level_set_no|level_set_id}, {dps_set_no|dps_set_id}
```

or:

```
SPRM {timing_specset_id}, {timing_set_no}, {level_set_id|level_set_no}, {dps_set_id|dps_set_no}
```

or, for multiport specifications:

```
SPRM? [(port)]
```

returns:

```
SPRM {"multi-port_spec"}, {timing_set_no|"timing_set_list"}, {level_set_id|level_set_no},{dps_set_id|dps_set_no} [,(port)]
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › SPRM  SPRM  -  Set PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98742_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set_no | The identification number of the waveform set. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum num…
> 表内引用（6 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `CONF, CONF? - (CONFiguration)`（raw: `02.06.02.02.31_CONF__CONF__-__CONFiguration.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `LSUS, LSUS? - (Level Sets USed)`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`） · `DSUS, DSUS? - (Dps Sets USed)`（raw: `02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`）

### Example（取自子主题 Level Setup Commands › List of level setup commands › SPRM  SPRM  -  Set PRiMary sets）

The following example shows how to define and query primary timing sets for the multi-port specification spec_ClockP_P1_P2, which contains three ports:

```
> SPRM "spec_ClockP_P1_P2","2,1,2",,
> SPRM?
< SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003
> SPRM "spec_ClockP_P1_P2",2,,,(port_1.CP_1)
> SPRM?
< SPRM "spec_ClockP_P1_P2",2,101002,101003
> SPRM? (port_1.CP_1)
< SPRM "spec_ClockP_P1_P2",2,101002,101003,(port_1.CP_1)
```

### Syntax（取自子主题 Level Setup Commands › List of level setup commands › SPST  -  SPecset STatus）

```
SPST? {spec_type}, {equation_set_no}, {specset_no}
```

returns:

```
SPST {spec_type}, {equation_set_no}, {specset_no}, {status}
```

or, for multiport specifications:

```
SPST? {spec_type}, , {"multi-port_spec"}
```

or

```
SPST? {spec_type}, PRM,
```

returns:

```
SPST {spec_type},, {"multi-port_spec"}, {status}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › SPST  -  SPecset STatus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

Status bits for the status parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：Bit | Description | Value
> 表内引用（10 条，供检索）：`ETIM`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`） · `ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） · `PCLK`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） · `CLKR`（raw: `02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md`） · `DRLV`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`） · `RCLV`（raw: `02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`） · `TERM`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） · `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`） · `SHVL`（raw: `02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md`） · `SVLR`（raw: `02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`）

### Example 1（取自子主题 Level Setup Commands › List of level setup commands › SPST  -  SPecset STatus）

```
> SPST? lev,all,all
< SPST LEV,1,1,0
```

### Example 2（取自子主题 Level Setup Commands › List of level setup commands › SPST  -  SPecset STatus）

```
> SPST? tim,all,all
<  SPST TIM,1,1,0
< SPST TIM,2,22,0
```

### Example 3（取自子主题 Level Setup Commands › List of level setup commands › SPST  -  SPecset STatus）

```
> SPST? TIM,,"mu_burst"
< SPST TIM,,"mu_burst",6
```

In this last example, a multi-port specification is queried. The answer says that bits 1 and 2 have been set. This has the effect that a drive or receive period 1 limit violation will be ignored, and only a period 2 limit violation will be recorded.

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98764_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:
> 表内引用（1 条，供检索）：`Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）

### Example 1（取自子主题 Level Setup Commands › List of level setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The following example queries the values of the spec variable f in a setup where both single-port and multi-port specifications occur:

```
> SVLR? TIM,ALL,ALL,"f"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",35
< SVLR TIM,,"spec_p_1_p_2","f@p_2",33
< SVLR TIM,1,1,"f",37
```

### Example 2（取自子主题 Level Setup Commands › List of level setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The next example queries in which equation sets the spec variable f occurs:

```
> SVLR? TIM,ALL,,"f"
< SVLR TIM,1,,"f",
< SVLR TIM,2,,"f",
```

### Example 3（取自子主题 Level Setup Commands › List of level setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

For this example assume that the primary timing is a multi-port specification which contains the two ports p_1 and p_2, and that p_1 and p_2 share the spec variable f in this specification. Assume further that f has been set to scope global for the port p_1. Now query the current value of f for p_1, change it globally, and query it again:

```
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",33
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",43
```

Since f is global for p_1, its value has been modified. Now change the value a second time, but this time locally, and then try to change it globally again:

```
> SVLR TIM,PRM,,"f@p_1",53
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",53
```

The second global command has no effect because f has only local scope after issuing the local command.

### TERM（取自子主题 Level Setup Commands › List of level setup commands › TERM  TERM  -  TERMination mode）

```
TERM {level_set_no | level_set_id}, [term_mode], [term_pulldown,] [param_1], [param_2], [param_3],
 [l_range], [h_range], [hr_mode,] {(pinlist)}
```

### TERM?（取自子主题 Level Setup Commands › List of level setup commands › TERM  TERM  -  TERMination mode）

```
TERM? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
TERM {level_set_no | level_set_id}, {term_mode}, [term_pulldown,] [param_1], [param_2], [param_3],
 [l_range], [h_range], [hr_mode,] {(pinlist)}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › TERM  TERM  -  TERMination mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98771_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：level_set_no | The identification number of the level set in which you want the definitions to be included. The number must not exceed the maximum number of lev…
> 表内引用（3 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `LSUS`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`） · `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`）

### Example 1（取自子主题 Level Setup Commands › List of level setup commands › TERM  TERM  -  TERMination mode）

```
TERM 1,T,-1500,,,,,(Q1)
```

This example terminates the output pin Q1 to -1500 mV in level set 1.

### Example 2（取自子主题 Level Setup Commands › List of level setup commands › TERM  TERM  -  TERMination mode）

```
TERM 3,A,3000,1500,1000,I3E4,I3E4,(out)
```

This example sets the active load level of the pin group out to 3V, and sets Iol and Ioh current to 1.5 and 1.0 mA respectively. The 0 to 30 mA range is used for both the low and the high range.

### Example 3（取自子主题 Level Setup Commands › List of level setup commands › TERM  TERM  -  TERMination mode）

```
TERM 1,CT,2000,,,,,(o1,o1-)
```

This example terminates the differential output pair (the o1 and o1- pins) to 2000 mV with center tap termination in level set 1.

### Example 4（取自子主题 Level Setup Commands › List of level setup commands › TERM  TERM  -  TERMination mode）

```
TERM 1,OFF,PULLDOWN,,,,,,(Q1,Q2)
```

On a PS1600 card, this example switches on the pulldown resistor on the specified pins.

```
TERM 1,OFF,NONE,,,,,,(Q1,Q2)
```

On a PS1600 card, this example switches off the pulldown resistor on the specified pins.

### UPTD（取自子主题 Level Setup Commands › List of level setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD {status}, {flag}
```

### UPTD?（取自子主题 Level Setup Commands › List of level setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD? {status}
```

returns:

```
UPTD {status}, {flag}
```

### Example（取自子主题 Level Setup Commands › List of level setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD? CONF
```

This example requests if the pin configuration data has been changed since the file was last loaded or saved. If the data has not changed, the response is:

```
UPTD CONF,1
```

### Syntax（取自子主题 Level Setup Commands › List of level setup commands › WAIT -  WAIT）

```
WAIT {time}
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › WAIT -  WAIT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98865_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：time | Enter a time in µs.

### Example（取自子主题 Level Setup Commands › List of level setup commands › WAIT -  WAIT）

```
RLYC DC,PMU,(outputs); WAIT 1000; FTST?
```

This example causes the MCD to wait 1 ms (1000 µs) for the PMU relay to close before executing a functional test.

### Syntax（取自子主题 Level Setup Commands › List of level setup commands › RST -  ReSeT）

```
*RST [type]
```

### Parameters（取自子主题 Level Setup Commands › List of level setup commands › RST -  ReSeT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98882_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：type | not used | Enforces a disconnect (AC relay is open) All DPS sets, except the default set, will be deleted. All resources (for example objects defined wit…

### Example（取自子主题 Level Setup Commands › List of level setup commands › RST -  ReSeT）

```
*RST
```

Resets the software and the hardware.

### Example（取自子主题 Timing Setup Commands › Concepts of timing setup › Data organization of equation based timing）

The following figure exemplifies the structure of equation based timing by a schematic setup:

 !`Timing Specifications`（raw: `../../../../raw/10596.png`）

### Example（取自子主题 Timing Setup Commands › Concepts of timing setup › Defining the timing specification）

The following is a simple example of a `single-port timing specification`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.34.04.01_Single-port_timing_setup.md`）:

```
EQNSET 1 "default"

WAVETBL "table1"
CHECK all

SPECSET 1 "sp1"

# SPECNAME *****ACTUAL***** *****MINIMUM**** *****MAXIMUM**** UNITS COMMENT
f          100                                                [MHz]
```

This specification uses spec set 1 for equation set 1. It will be identified to the firmware commands by 101. The base variable f is set to 100. The `CHECK all statement`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.34.04.03.05.01_CHECK_Statement_Options.md`） activates all consistency checks (see `Consistency checks for edge delays`（raw: `02.06.06.01.05.01_Consistency_checks_for_edge_delays.md`）).

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › APRM -  Activate PRiMary sets）

```
APRM {mode}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › APRM -  Activate PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98485_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 3 列。
> 首行（上游原文）：mode | Selects the activation mode:

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › APRM -  Activate PRiMary sets）

```
APRM CNL
```

### BWDF（取自子主题 Timing Setup Commands › List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### BWDF?（取自子主题 Timing Setup Commands › List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF? {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {(pinlist)}
```

returns:

```
BWDF {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98497_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number …
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › BWDF  BWDF  -  Break Waveform DeFinition）

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

This example defines a pulse for waveform set 1, and for pins D0 to D3, driving to 1 at edge action 4 and to 0 at edge action 5. The tri-state formatter is not used.

### BWDS（取自子主题 Timing Setup Commands › List of timing setup commands › BWDS  BWDS  -  Break Waveform Definition String）

```
BWDS {wvf_set}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

### BWDS?（取自子主题 Timing Setup Commands › List of timing setup commands › BWDS  BWDS  -  Break Waveform Definition String）

```
BWDS? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {(pinlist)}
```

returns:

```
BWDS {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98498_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. Enter PRM for the Primary waveform set. The maximum number is determined by…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `WFDS, WFDS? - (WaveForm Definition String)`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › BWDS  BWDS  -  Break Waveform Definition String）

```
> BWDS? 1,,,(@)
< BWDS 1,,,"",(io)
< BWDS 1,,,"d1:F00 d5:F10",(clk)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › CDCP  -  Cycle Device Cycle Parameter）

```
CDCP? {start_cycle}, {no_of_cycles}, {strt_disp}, {disp_length}, {(pinlist)}
```

returns:

```
CDCP {cycle}, {dev_cyc_name}, {dev_cyc_len}, {DD1}, {DD2}, {ED1}, {ED2}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › CDCP  -  Cycle Device Cycle Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98499_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle to be analyzed. The range of values for this parameter depends on the analysis mode: In the Start …

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › CDCP  -  Cycle Device Cycle Parameter）

```
> CDCP? 0,8,0,8,(S0_1)
< CDCP 0,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 1,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 2,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 3,"MYDC",2,F00,N,N,N,(S0_1)
< CDCP 5,"MYDC",2,F10,N,N,N,(S0_1)
< CDCP 7,"DNRZ",1,F10,N,N,N,(S0_1)
> CDCP? 2,6,4,2,(S0_1)
< CDCP 5,"MYDC",2,F10,N,N,N,(S0_1)
< CDCP 7,"DNRZ",1,F10,N,N,N,(S0_1)
```

In the second call of CDCP? (the first call just serves to display the underlying situation) the range of interest starts at vector 6. Note that the reply starts with vector 5, and that the first occurrence of MYDC, which lies between vector 2 and vector 6, is not displayed.

### CLKR（取自子主题 Timing Setup Commands › List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res}
```

### CLKR?（取自子主题 Timing Setup Commands › List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

```
CLKR?[type,] {waveform_set|specset_id|"multi-port_spec"}
```

returns:

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res|clock_res}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98504_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `Automatic calculation of period resolution for single-port setups`（raw: `02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › CLKR  CLKR  -  CLocK Resolution）

```
> CLKR 1,,10
> CLKR? 1
< CLKR 1,1000,10

```

This example sets and queries the period resolution (10 ns) for waveform set 1. Ignore the returned value of the ref_period parameter.

```
> CLKR? "spec_port_1_port_2"
< CLKR "spec_port_1_port_2",50,5.555555556
```

This example queries the period resolution for the multi-port specification `spec_port_1_port_2`.

### DCDT（取自子主题 Timing Setup Commands › List of timing setup commands › DCDT  DCDT  -  Device Cycle DefaulT）

```
DCDT {waveform_set}, {"default_name"}
```

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DCDT  DCDT  -  Device Cycle DefaulT）

```
DCDT 1,"HOLD"
```

This example defines the default device cycle name HOLD for Waveform Set 1.

```
DCDT? "fast_ARM",(ARMPort)
DCDT "fast_ARM","Cycle",(ARMPort)
```

This example queries the default device cycle name for the ARMPort port in the multi-port specification fast_ARM.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › DCUD -  Device Cycle UnDefine）

```
DCUD {waveform_set},{"dev_cyc_name"},{(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › DCUD -  Device Cycle UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98529_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DCUD -  Device Cycle UnDefine）

```
DCUD 1,"WRITE"
```

This example deletes the device cycle `WRITE` for waveform set 1 from the device cycle table.

### DFCR（取自子主题 Timing Setup Commands › List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

```
DFCR {source_group},{dest_group}
```

### DFCR?（取自子主题 Timing Setup Commands › List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

```
DFCR?
```

returns (for every group except G4):

```
DFCR {source_group},{dest_group}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98541_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：source_group | specifies the hardware group whose local clock is to be routed to dest_group. The format is Gx, where x is the group number.

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DFCR  DFCR  -  DeFine Clock Routing）

```
> DFCR?
<
> DFCR G1,G8
> DFCR?
< DFCR G4,G3
< DFCR G4,G1
< DFCR G4,G5
< DFCR G1,G6
< DFCR G1,G2
< DFCR G1,G8
< DFCR G1,G7
```

This example changes the default routing (DFCR? gives an empty reply). Note that the inherited clocks of G6 and of all successors of G6 are also changed.

### DPRT（取自子主题 Timing Setup Commands › List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT {"multi-port_spec"}, [timing_set_no|"timing_set_list"][,(port)]
```

### DPRT?（取自子主题 Timing Setup Commands › List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT?
```

returns:

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT?
```

returns:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT? [(port)]
```

returns:

```
DPRT {"multi-port_spec"}, {timing_set_no|"timing_set_list"}[,(port)]

```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98570_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number.
> 表内引用（1 条，供检索）：`TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DPRT  DPRT  -  Default PRimary Timing sets）

```
DPRT?
```

returns:

```
DPRT 3,4
```

On sending a query the system reports that the default primary waveform set is 3 and the default primary timing set is 4.

### DSCP（取自子主题 Timing Setup Commands › List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP `[device_cycle`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_device_cycle`）], `[waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）], `[timing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_timing_set`）], `[level_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_level_set`）], `[dps_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_dps_set`）], `[pmu_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_pmu_set`）],
                        `[devicecycle_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_devicecycle_set`）], `[routing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_routing_set`）], `[period_res_prec`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_period_res_prec`）],

```

### DSCP?（取自子主题 Timing Setup Commands › List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP?
```

returns:

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
       {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
       [period_res_compatibility_model]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98578_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：device_cycle | The device_cycle parameter is an integer that defines the absolute maximum number of device cycles that you can create for one pin.Default: 256Ma…
> 表内引用（2 条，供检索）：`waveform sets and wavetables`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） · `waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › DSCP  DSCP  -  Define System Control Parameter）

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › EDDC  -  EDge in Device Cycle）

```
EDDC? [waveform_set], [timing_set], {edge_spec},
[dev_cyc_name], [dc_ref], [direction], {(pinlist)}
```

returns:

```
EDDC {edge_number}, {dev_cyc_name}, [reuse_flag], {(pinlist)}
```

### EDSP（取自子主题 Timing Setup Commands › List of timing setup commands › EDSP  EDSP  -  EDge SPecification）

The edge_spec parameter specifies a physical edge (d1 through d8 or r1 through r8):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}
```

The edge_spec parameter is a data parameter (D1, D2, C1, C2, E1, or E2):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}
```

### EDSP?（取自子主题 Timing Setup Commands › List of timing setup commands › EDSP  EDSP  -  EDge SPecification）

```
EDSP? [dc_ref], {(pinlist)}
```

returns:

```
EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98589_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set | Specifies a waveform set number for a fixed timing setup.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › EQFS -  EQuation FileS command transfer）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98592_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification to use:

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › EQFS -  EQuation FileS command transfer）

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

This example loads the level equation file from /tmp/level_equation.

### EQSP（取自子主题 Timing Setup Commands › List of timing setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP {spec_type}, {part}, {#spec(data)}
```

### EQSP?（取自子主题 Timing Setup Commands › List of timing setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

```
EQSP?{spec_type}, {part}
```

returns:

```
EQSP {spec_type}, {part}, {#spec(data)}
```

if these are not empty, for backward compatibility.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98593_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：spec_type | The mandatory parameter defines which specification type to use. Use: LEV to specify levels TIM to specify timing

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › EQSP  EQSP  -  EQuation SPecification transfer）

The following example queries the current wavetables:

```
> EQSP? TIM,WVT
< EQSP TIM,WVT,#9000000127WAVETBL table1  # derived from waveform set 1

  PINS Pin1 Pin2
  WFDS 0  "d1:D11"
  1    0   .   .   .
  2    1   .   .   .
  BWDS ""

  @
```

### ETDS（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### ETDS?（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

ETDS? {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {(pinlist)}

returns:

ETDS {waveform_set|specset_id|"multi-port_spec"}, {timing_set}, [mode], {definition_string}, {(pinlist)}

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98599_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `Defining waveforms for Pin Scale 9G pins`（raw: `02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`） · `Selecting and ordering edges`（raw: `02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

```
> ETDS 1,1,,"e1:0 e2:2 e3:6 e4:4",(io)
> ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
> ETDS? 1,1,,(@)
< ETDS 1,1,,"d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4",(io)
< ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
```

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

The following example shows the various possibilities for using ETDS with fast pins:

```
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5 d3:10 d4:15",(CP)
> ETDS 401,1,,"d2:5.5",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5.5 d3:10 d4:15",(CP)
> ETDS 401,1,,"pdiv:4 d1:3 d3:14",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:14 d4:18",(CP)
> ETDS 401,1,DELTA,"d3:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:12 d4:18",(CP)
> ETDS 401,1,DELTA,"pdiv:4 d1:0 d2:1 d4:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:6 d3:10 d4:14",(CP)
```

Note in particular the effect of the first instance of the command in DELTA mode. The negative offset is not applied to the actual value of d3, which is 14, but to the calculated default value, which is 13.

### Example 3（取自子主题 Timing Setup Commands › List of timing setup commands › ETDS  ETDS  -  Edge Timing Definition String）

This example shows how to set and retrieve a delay of a multi-port specification:

```
> ETDS? "mu_timing",2,,(In1)
< ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ETDS "mu_timing",2,,"d1:0.5",(In1)
> ETDS? "mu_timing",2,,(In1)
< ETDS "mu_timing",2,,"d1:0.5",(In1)
```

The specification name and the pin name identify the port (no pin may occur in more than one port within the same specification). Then the port and the specification identify the equation set.

### ETIM（取自子主题 Timing Setup Commands › List of timing setup commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

### ETIM?（取自子主题 Timing Setup Commands › List of timing setup commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM? {waveform_set}, {timing_set}, {(pinlist)}
```

returns:

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

or:

```
ETIM? {specset_id}, {timing_set_no}, {(pinlist)}
```

returns:

```
ETIM {specset_id}, {timing_set_no}, [t1], [t2], [t3], [t4], [t5], [t6],{(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98600_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `ETIM, ETIM? - (Edge TIMing)`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › ETIM  ETIM  -  Edge TIMing）

```
ETIM 1,1,2,4,8,6,10,,(DATA)
```

This example sets the edge delays for the pin group DATA specified for waveform set 1 and timing set 1. Edges 1 to 5 are set to 2,4,8,6 and 10 ns respectively, edge 6 is unused. If no previous setting for edge 6 exists in waveform set 1 and timing set 1, then its delay remains at 0.0 ns.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › EUDS  -  Edge Usage Definition String）

```
EUDS? {waveform_set}, [mode], {(pinlist)}
```

returns:

```
EUDS {waveform_set}, {definition_string}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › EUDS  -  Edge Usage Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98601_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter ALL for all defined waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The wa…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › EUDS  -  Edge Usage Definition String）

```
EUDS? 1,,(@)
EUDS 1,"d1 d2 d3 r4",(io)
EUDS 1,"d1 d2 d3 d4 d5 d6 d7 d8",(clk)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › EVCK  -  EVent ClocK）

```
EVCK? {"multi-port_spec"}, {(port_list)}
```

returns:

```
EVCK {"multi-port_spec"}, event_clock_per, {(port)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › EVCK  -  EVent ClocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126417_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：multi-port_spec | Name of a multi-port timing specification.

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › EVCK  -  EVent ClocK）

```
>  SCLK? "mu_burst"
<  SCLK "mu_burst",480
>  EVCK? "mu_burst",(@@)
<  EVCK "mu_burst",2448,(PortA)
<  EVCK "mu_burst",2448,(PortB)
<  EVCK "mu_burst",480,(PortD)
<  EVCK "mu_burst",480,(PortE)
```

This example returns the system clock period and the event clock periods for the multi-port timing specification `mu_burst`. The event clock periods of `PortD` and `PortE` equal the system clock period, those of `PortA` and `PortB` are different.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › FTCG  FTCG  -  Functional Test ConfiGure）

FTCG

```
FTCG {parameter}, {mode}, {(portlist)}
```

  FTCG?

```
FTCG? {parameter}, {(@@)}
```

returns:

```
FTCG {parameter}, {mode}, {(portlist)}
```

  Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98606_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：parameter | The parameter to be used is SKPR (SKip PRimaries).

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › FTCG  FTCG  -  Functional Test ConfiGure）

The following example illustrates the dependence of the FTCG command on the current sequencing group definitions.

```
> SQLB "MP_burst1",MPBU,28,31,"SG1",(clock)
> SQLB "MP_burst1",MPBU,28,29,"SG2",(data1)
> SQLB "MP_burst1",MPBU,31,32,"SG2",(data2)
> SQLB "MP_burst2",MPBU,32,33,"SG1",(clock)
> SQLB "MP_burst2",MPBU,30,31,"SG1",(data1)
> SQLB "MP_burst2",MPBU,33,34,"SG2",(data2)
> FTCG SKPR,ON,(clock)
> FTCG SKPR,NEVER,(data2)
> SPRM "cont_clock",,,
> SQSL "MP_burst1"
> SQGB ACQF,0
> FTST?
...
> SQSL "MP_burst2"
> FTST?
...
```

In the first functional test, sequencing group `SG1` only contains the port `clock`, and therefore activation of primary sets is suppressed at the start of `MP_burst1` only for `clock`, whereas it is enforced for ports `data1` and `data2`. In the second test, `SG1` contains both `clock` and `data1`, and therefore activation is suppressed for both these ports at the start of `MP_burst2`, and enforced only for `data2`.

### PCLK（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

Fixed timing:

```
PCLK{waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### PCLK?（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

Fixed timing:

```
PCLK?{waveform_set},{timing_set},{(pinlist)} [,query_mode]
```

returns:

```
PCLK {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK? {specset_id|"multi-port_spec"}, {timing_set}, {(pinlist|portlist)} [,query_mode]
```

returns:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98682_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

```
PCLK 101,1,20,(@)
```

This example sets the test system period for specification 101 to 20 ns.

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › PCLK  PCLK  -  Pin CLocK）

```
PCLK 101,1,40,(S1)
```

This example sets the test system period of pin S1 for specification 101 to 40 ns.

The `VCLK?`（raw: `02.06.02.02.319_VCLK__-__Verify_CLocK.md`） query checks whether a PCLK command with the specified parameter values was accepted with or without auto-correction.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › PDIV  -  Period DIVider）

```
PDIV? {specset_id|"multi-port_spec"|"wavetbl"} [,spec_type][,(pinlist)]
```

returns:

```
PDIV {specset_id|"multi-port_spec"}, {period_div}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › PDIV  -  Period DIVider）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98684_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：specset_id | Identifier of a timing specification, which is derived as follows: 100 * equation_set_no + specset_no

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › PDIV  -  Period DIVider）

```
> PDIV? "fast",WFT,(I1)
< PDIV "fast",WFT,6,(I1)
```

This example queries the implicit period divider of the fast pin I1 in the wavetable `fast`. The factor is 6.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › RCLK  -  Reference CLocK source）

```
RCLK?
```

returns:

```
RCLK {clock_string}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › RCLK  -  Reference CLocK source）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98715_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：clock_string | The string shows which clock source is used as reference clock. Possible values are: EXTERNAL INTERNAL

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › RCLK  -  Reference CLocK source）

```
RCLK?
```

returns:

```
RCLK INTERNAL
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › RSET -  ReSET）

```
RSET {specifier}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › RSET -  ReSET）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98723_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：specifier | The specifier can be:
> 表内引用（1 条，供检索）：`UHCM`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › RSET -  ReSET）

```
RSET TIM
```

This example resets all waveform sets and timing sets and loads the hardware with the default vector rate and edge placement values. Only waveform set 1 and timing set 1 in waveform set 1 is active.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SCLK  -  System CLocK query）

```
SCLK? {wf_set|specset_id|"multi-port_spec"|ALL|PRM}
```

returns:

```
SCLK {wf_set|specset_id|"multi-port_spec"} {sclk_val}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SCLK  -  System CLocK query）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98728_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：wf_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? - …
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › SCLK  -  System CLocK query）

```
> SCLK? 401
< SCLK 401,480
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SDSC  -  Set number DeSCriptions）

```
SDSC? {spec_type}, {type}, [setup_comp_1], [setup_comp_2], ["description"]
```

returns:

```
SDSC {spec_type}, {type}, [setup_comp_1], [setup_comp_2], {"description"}
```

Alternatively, for multiport specifications:

```
SDSC? {TIM}, {type}, [setup_comp_1], {"multi-port_spec"}, ["description"][, (portlist)]
```

returns:

```
SDSC {TIM}, {type}, [setup_comp_1], {"multi-port_spec"}, {"description"}, {(port)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：21 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

The following table explains the interpretation of the setup_comp_1 and setup_comp_2 parameters for every accepted value pair of the spec_type and type parameters:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98729_3.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 4 列。
> 首行（上游原文）：spec_type | type | setup_comp_1 | setup_comp_2

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,,,
< SDSC TIM,EQN,1,,"gross_func_eqn"
< SDSC TIM,EQN,2,,"specs_search_eqn"
< SDSC TIM,EQN,3,,"speed_eqn"
```

This example returns all defined equation sets.

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › SDSC  -  Set number DeSCriptions）

```
> SDSC? TIM,EQN,2,"spec_port_1_port_2",,(port_1)
< SDSC TIM,EQN,1,"spec_port_1_port_2",
     "gross_func_eqn",(port_1)
```

This example returns the equation set that is associated with port port_1 in the multiport specification

spec_port_1_port_2. Note that the setup_comp_1 parameter is ignored.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SPCP  -  SPeCification Port list）

```
SPCP? {"multi-port_spec"|ALL}
```

returns:

```
SPCP {"multi-port_spec"}, {(portlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SPCP  -  SPeCification Port list）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98738_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：multi-port_spec | Defines the multi-port specification for which the ports are to be queried. You can enter ALL in order to display the ports for all defined mu…

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › SPCP  -  SPeCification Port list）

```
> SPCP? ALL
< SPCP "spec_port_1_port_2",(port_1,port_2)
< SPCP "spec_ClkP_P1_P2",(ClockPort,p_CP_1,p_CP_2)
< SPCP "spec_ssearch_port_1_port_2",(port_1,port_2)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SPEC  -  SPECification）

```
SPEC? {"module:resource"},["details"],[context], [(pinlist)]
```

returns:

```
SPEC {"module:resource"},["details"],[context], {answer},[(pinlist)]
```

   Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98739_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 3 列。
> 首行（上游原文）：module:resource | Specifies the module and the resource about which information is to be returned. Currently, the following values are allowed:

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › SPEC  -  SPECification）

```
SPEC? "Result:Xmodes",,,(@)
```

returns

```
SPEC "Result:Xmodes",,,"1,2,4,6,8",(...)
```

This example queries which x-modes are possible for the result module on a Smart Scale system. On a Pin Scale system, x-mode 6 would be omitted in the reply.

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › SPEC  -  SPECification）

The second example queries the termination modes that can be specified with the `TERM`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） command for pin "PS1600_pin" and level set 1:

```
SPEC? "Level:Term",,1,(PS1600_pin)
```

returns

```
SPEC "Level:Term",,1,"OFF,T,H,L,A,C,CT,HV,DIFHIZ",(PS1600_pin)
```

### Example 3（取自子主题 Timing Setup Commands › List of timing setup commands › SPEC  -  SPECification）

The third example queries the range of the fixture delay:

```
SPEC? "Timing:FxdlRange",,"Global",
```

returns

```
SPEC "Timing:FxdlRange",,"Global","-0.015000,13.200000",()
```

The query returns the range for Pin Scale systems.

Note: Parameter pinlist is irrelevant for this query and may be omitted.

### SPRM（取自子主题 Timing Setup Commands › List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

```
SPRM [waveform_set_no], [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or:

```
SPRM {timing_specset_id}, [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or, for multiport specifications:

```
SPRM {"multi-port_spec"}, [timing_set_no|"timing_set_list"], [level_set_id|level_set_no],[dps_set_id|dps_set_no] [,(port)]
```

### SPRM?（取自子主题 Timing Setup Commands › List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

```
SPRM?
```

returns:

```
SPRM {waveform_set_no}, {timing_set_no}, {level_set_no|level_set_id}, {dps_set_no|dps_set_id}
```

or:

```
SPRM {timing_specset_id}, {timing_set_no}, {level_set_id|level_set_no}, {dps_set_id|dps_set_no}
```

or, for multiport specifications:

```
SPRM? [(port)]
```

returns:

```
SPRM {"multi-port_spec"}, {timing_set_no|"timing_set_list"}, {level_set_id|level_set_no},{dps_set_id|dps_set_no} [,(port)]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98742_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set_no | The identification number of the waveform set. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum num…
> 表内引用（6 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `CONF, CONF? - (CONFiguration)`（raw: `02.06.02.02.31_CONF__CONF__-__CONFiguration.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `LSUS, LSUS? - (Level Sets USed)`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`） · `DSUS, DSUS? - (Dps Sets USed)`（raw: `02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › SPRM  SPRM  -  Set PRiMary sets）

The following example shows how to define and query primary timing sets for the multi-port specification spec_ClockP_P1_P2, which contains three ports:

```
> SPRM "spec_ClockP_P1_P2","2,1,2",,
> SPRM?
< SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003
> SPRM "spec_ClockP_P1_P2",2,,,(port_1.CP_1)
> SPRM?
< SPRM "spec_ClockP_P1_P2",2,101002,101003
> SPRM? (port_1.CP_1)
< SPRM "spec_ClockP_P1_P2",2,101002,101003,(port_1.CP_1)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

```
SPST? {spec_type}, {equation_set_no}, {specset_no}
```

returns:

```
SPST {spec_type}, {equation_set_no}, {specset_no}, {status}
```

or, for multiport specifications:

```
SPST? {spec_type}, , {"multi-port_spec"}
```

or

```
SPST? {spec_type}, PRM,
```

returns:

```
SPST {spec_type},, {"multi-port_spec"}, {status}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:

Status bits for the status parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98743_3.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：Bit | Description | Value
> 表内引用（10 条，供检索）：`ETIM`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`） · `ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） · `PCLK`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） · `CLKR`（raw: `02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md`） · `DRLV`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`） · `RCLV`（raw: `02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`） · `TERM`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） · `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`） · `SHVL`（raw: `02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md`） · `SVLR`（raw: `02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`）

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

```
> SPST? lev,all,all
< SPST LEV,1,1,0
```

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

```
> SPST? tim,all,all
<  SPST TIM,1,1,0
< SPST TIM,2,22,0
```

### Example 3（取自子主题 Timing Setup Commands › List of timing setup commands › SPST  -  SPecset STatus）

```
> SPST? TIM,,"mu_burst"
< SPST TIM,,"mu_burst",6
```

In this last example, a multi-port specification is queried. The answer says that bits 1 and 2 have been set. This has the effect that a drive or receive period 1 limit violation will be ignored, and only a period 2 limit violation will be recorded.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › STRS  -  Spec TRansition Search）

```
STRS? ["exec_context",] [start], [stop], {mode}, [(pinlist)], {spec_type}, {"spec_name[@port[@UNCHANGED]]"}, [stepwidth], {resolution}
```

returns:

```
STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › STRS  -  Spec TRansition Search）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98762_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts .
> 表内引用（4 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） · `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`） · `Modifying the period for a search or shmoo in a multi-port setup`（raw: `02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › STRS  -  Spec TRansition Search）

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98764_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 3 列。
> 首行（上游原文）：spec_type | Which specification type to use. Use:
> 表内引用（1 条，供检索）：`Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）

### Example 1（取自子主题 Timing Setup Commands › List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The following example queries the values of the spec variable f in a setup where both single-port and multi-port specifications occur:

```
> SVLR? TIM,ALL,ALL,"f"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",35
< SVLR TIM,,"spec_p_1_p_2","f@p_2",33
< SVLR TIM,1,1,"f",37
```

### Example 2（取自子主题 Timing Setup Commands › List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

The next example queries in which equation sets the spec variable f occurs:

```
> SVLR? TIM,ALL,,"f"
< SVLR TIM,1,,"f",
< SVLR TIM,2,,"f",
```

### Example 3（取自子主题 Timing Setup Commands › List of timing setup commands › SVLR  SVLR  -  Spec VaLues at Runtime）

For this example assume that the primary timing is a multi-port specification which contains the two ports p_1 and p_2, and that p_1 and p_2 share the spec variable f in this specification. Assume further that f has been set to scope global for the port p_1. Now query the current value of f for p_1, change it globally, and query it again:

```
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",33
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",43
```

Since f is global for p_1, its value has been modified. Now change the value a second time, but this time locally, and then try to change it globally again:

```
> SVLR TIM,PRM,,"f@p_1",53
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",53
```

The second global command has no effect because f has only local scope after issuing the local command.

### TSUS（取自子主题 Timing Setup Commands › List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS {waveform_set},{timing_set}
```

### TSUS?（取自子主题 Timing Setup Commands › List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS? {waveform_set}
```

returns:

```
TSUS {waveform_set},{timing_set}
```

Or:

```
TSUS? {specset_id}
```

returns:

```
TSUS {specset_id},{timing_set}
```

Or, for multiport specifications:

```
TSUS? {"multiport_spec"}[,(portlist)]
```

returns:

```
TSUS {"multiport_spec"},{timing_set}[,(port)]
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98817_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › TSUS  TSUS  -  Timing Sets USed）

```
TSUS 3,7
```

This example defines a maximum of 7 timing sets in waveform set 3.

```
TSUS? "spefc",(ARMPort)
TSUS "spefc",3,(ARMPort)
```

This example queries the number of timing sets defined for port ARMPort in the multiport specification spefc.

### TSUX（取自子主题 Timing Setup Commands › List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

```

TSUX {waveform_set},{timing_set}
```

### TSUX?（取自子主题 Timing Setup Commands › List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

```

TSUX? {waveform_set}
```

returns:

```
TSUX {waveform_set},{timing_set}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › TSUX  TSUX  -  Timing Sets Used eXtended）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98818_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter ALL for all waveform sets in the query command.
> 表内引用（1 条，供检索）：`TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

### UPTD（取自子主题 Timing Setup Commands › List of timing setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD {status}, {flag}
```

### UPTD?（取自子主题 Timing Setup Commands › List of timing setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD? {status}
```

returns:

```
UPTD {status}, {flag}
```

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › UPTD  UPTD  -  UP To Date）

```
UPTD? CONF
```

This example requests if the pin configuration data has been changed since the file was last loaded or saved. If the data has not changed, the response is:

```
UPTD CONF,1
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VCLK  -  Verify CLocK）

```
VCLK? {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

returns:

```
VCLK {autocorrect}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VCLK  -  Verify CLocK）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98844_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VCLK  -  Verify CLocK）

```
VCLK? 1,1,20,(@)
```

This example checks if a period of 20 ns will cause auto-correction to the edge placements in Timing Set 1 of Waveform Set 1 on any pin. If no auto-correction will occur the following string is returned:

```
VCLK 0
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VDCG  -  Verify Device Cycle for Group）

```
VDCG? {waveform_set}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {waveform_set}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {specset_id}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {specset_id}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {wavetable_name}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {wavetable_name}, {dev_cyc_name}, {dev_cyc_len}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VDCG  -  Verify Device Cycle for Group）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98846_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 4 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VDCG  -  Verify Device Cycle for Group）

```
VDCG? 1,ALL,(inputs)
```

returns:

```
VDCG 1,ALL,SLEN
```

This example checks the consistency of all device cycles for pins in the pin group "inputs" in waveform set 1. The test system replies that all device cycles for the specified group are consistently defined.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VTIM  -  Verify TIMing）

```
VTIM? {waveform_set},{timing_set},{(pinlist)}
```

returns:

```
VTIM {status}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VTIM  -  Verify TIMing）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98862_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VTIM  -  Verify TIMing）

The following example illustrates the working of VTIM? in a multi-port setup. The pins S1_1 and DS0_1 belong to the same port, and S1_2 belongs to another one.

```
> ETDS? "spec_port_1_port_2",ALL,,(S1_1,DS0_1,S1_2)
< ETDS "spec_port_1_port_2",1,,"d1:0 d2:30",(S1_1,DS0_1)
< ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(S1_1)
< ETDS "spec_port_1_port_2",2,,"d1:1 d2:12",(DS0_1)
< ETDS "spec_port_1_port_2",1,,"d1:-0.67 d2:1.33 d3:9.3",(S1_2)
```

This call of `ETDS?`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`） shows that the edge timings of S1_1 and DS0_1 are the same in timing set 1, but not in timing set 2 of the port to which these pins belong.

```
> PCLK? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< PCLK "spec_port_1_port_2",1,50,(S1_1)
< PCLK "spec_port_1_port_2",2,20,(S1_1)
< PCLK "spec_port_1_port_2",1,50,(DS0_1)
< PCLK "spec_port_1_port_2",2,20,(DS0_1)
< PCLK "spec_port_1_port_2",1,16.667,(S1_2)
```

This call of `PCLK?`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`） shows that the periods of S1_1 and DS0_1 are the same in the two timing sets of the port.

```
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 0
```

VTIM? returns 0 because of the different timings for S1_1 and DS0_1 in timing set 2.

```
> ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(DS0_1)
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 1
```

After changing the edge timing of DS0_1 in timing set 2 to the values of S1_1 with a call of `ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`）, VTIM? returns 1 although DS0_1 has a different timing in timing set 1 and in timing set 2, and S1_2, which belongs to another port, has different values altogether.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VWFG  -  Verify WaveForms in Groups）

There are three different ways to call VWFG?:

```
VWFG? {waveform_set}, ["dev_cyc_name"], {(pinlist)}
VWFG? {specset_id},["dev_cyc_name"],{(pinlist)}
VWFG? {wavetable_name}, ["dev_cyc_name"], {(pinlist)}
```

All three forms return:

```
VWFG {status}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VWFG  -  Verify WaveForms in Groups）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98863_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VWFG  -  Verify WaveForms in Groups）

```
> VWFG? "spec_search_wtb","SBC",(ser_in)
< VWFG 1
> VWFG? "spec_search_wtb",,(ser_in)
< VWFG 0
```

According to this example, the waveform and device cycle definition for device cycle SBC are the same for the pins in the group ser_in within the wavetable spec_search_wtb, but this does not hold for all device cycles that are defined for the pins of this group.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › VWFS  -  Verify WaveForm Sets）

```
VWFS? {waveform_set_1},{waveform_set_2},{(pinlist)}
```

returns:

```
VWFS {status}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › VWFS  -  Verify WaveForm Sets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98864_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：waveform_set_x | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, …
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › VWFS  -  Verify WaveForm Sets）

```
VWFS? 1,2,(DATA)
```

This example checks whether waveform sets 1 and 2 are the same for the pins in the group DATA. If they are the same the following string is returned:

```
VWFS 1,(DATA)
```

### WAVE（取自子主题 Timing Setup Commands › List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
WAVE {wvf_set}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
WAVE {specset_id|"multiport_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}, ALLOW_EQ
```

### WAVE?（取自子主题 Timing Setup Commands › List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
WAVE? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {(pinlist)}
```

returns:

```
WAVE {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WAVE  WAVE  -  WAVEform）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98869_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? …
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WAVE  WAVE  -  WAVEform）

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

This example first defines a logical waveform with the index 2 for waveform set 1. The waveform uses the data parameter D11, the fixed action 0, and the complement C11 of D11. Then two physical waveforms are defined for logical waveform 2, which are referenced by the physical waveform DC/DC power units 4 and 5. Waveform 4 drives to 0 at edge d1, to 0 at d3, and to 1 at d4. Waveform 5 drives to 1 at edge d1, to 0 at d3, and to 0 at d4.

### WFDF（取自子主题 Timing Setup Commands › List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
WFDF {wvf_set}, {wfIndex}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### WFDF?（取自子主题 Timing Setup Commands › List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
WFDF? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDF {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98871_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 4 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…
> 表内引用（4 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `WAVE`（raw: `02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） · `Restrictions for drive edges`（raw: `02.06.06.01.03.01.02.01_Restrictions_for_drive_edges.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WFDF  WFDF  -  WaveForm DeFinition）

```
> WFDF 1,2,N,N,D11,N,N,N,(D0,D2,D2,D3)
```

This example defines a waveform referenced by waveform index 2. The waveform uses the drive data and tri-state parameter 1. Edge number 3 provides the timing for this waveform. The definitions are made for waveform set 1 and for pins D0 to D3.

### WFDS（取自子主题 Timing Setup Commands › List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

```
WFDS {wvf_set}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
WFDS {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### WFDS?（取自子主题 Timing Setup Commands › List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

```
WFDS? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDS {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98872_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 4 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WFDS  WFDS  -  WaveForm Definition String）

```
> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)
> WFDS 1,1,,"r4:EE1",(io)
> WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)

> WFDS? 1,ALL,,(@)
< WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)
< WFDS 1,1,,"r4:EE1",(io)
< WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
```

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › WFUD -  WaveForm UnDefine）

```
WFUD {wvf_set},{wfIndex},{(pinlist)}
WFUD {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WFUD -  WaveForm UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98875_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：wvf_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WSUS? -…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WFUD -  WaveForm UnDefine）

```
WFUD 1,2,(D0,D2,D2,D3)
```

This example deletes a logical waveform defined for waveform set 1 and for pins `D0` to `D3`, referenced by waveform index 2.

### Syntax（取自子主题 Timing Setup Commands › List of timing setup commands › WRST -  Waveform ReSeT）

```
WRST {waveform_set}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WRST -  Waveform ReSeT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98876_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by WSUS, WS…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WRST -  Waveform ReSeT）

```
WRST 3
```

This example resets all waveform and timing entries for all pins for waveform set 3.

### WSDM（取自子主题 Timing Setup Commands › List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

```
WSDM {waveform_set}, {display_mode}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98877_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum nu…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WSDM  WSDM  -  Waveform Set Display Mode）

```
> WSDM? "spec_1", (port_1)
< WSDM  "spec_1", 0
```

This example queries the display mode of port port_1 in the multiport specification spec_1. The reply shows that it is set to the "classic" display mode.

### WSUS（取自子主题 Timing Setup Commands › List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS {waveform_set}
```

### WSUS?（取自子主题 Timing Setup Commands › List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS?
```

returns:

```
WSUS {waveform_set}
```

### Parameters（取自子主题 Timing Setup Commands › List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98878_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number. This is the highest number currently allocated to a waveform set or the highest number of a set you want to load. The number…
> 表内引用（1 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 Timing Setup Commands › List of timing setup commands › WSUS  WSUS  -  Waveform Sets USed）

```
WSUS 3
```

This example sets the number of used waveform sets to 3.

### Example（取自子主题 Vector Setup Commands › Concepts of vector setup › Label definition  sequencer program  and sequencer area）

The following figure shows the label definitions of the standard example and the corresponding sections of the sequencer area for the default port @:

 !`Label Definitions and Sequencer Area`（raw: `../../../../raw/120222.png`）

Since the default port contains all configured pins, the sequencer area on the right side of this figure is stored in the memory of all pins.

### Example（取自子主题 Vector Setup Commands › Concepts of vector setup › Sequencer areas and vector areas）

The following figure illustrates the case where one pin belongs to more than one port:

 !`Vector areas for pin belonging to two ports`（raw: `../../../../raw/114615.png`）

Observe the following points in this figure:

- port1 comprises the pins Pin1 and Pin2, while port2 only contains Pin2.
- The arrows indicate which vector area segments belong to which labels. Pin2 has two vector areas, one for the labels of port1 and one for the labels of port2.
- The numbers above the arrow heads are the start addresses of the vector area segments for the respective label (as defined by STVA).
- The association of the vector generating instructions to vector area sub-segments is exemplified by Pin1 and Test 1.

### Example（取自子主题 Vector Setup Commands › Concepts of vector setup › Addressing the vector areas）

The following figure displays the relations between the sequencer program and the vector areas of the standard example, and also illustrates the various concepts introduced to describe the structure of these areas:

 !`Vector areas`（raw: `../../../../raw/120207.png`）

The left side of the figure shows a section of the sequencer area for the default port @. It contains the sequencer programs for two labels (command line 4 through 8 and line 9 through 12). The right side displays the associated segments of the vector areas for the pins IN1 and OUT1.

Notice the following points in the figure:

- An instance of the sequencer area for @ is contained in the memory of both pin IN1 and pin OUT1.
- Each of the rows on the right side represents one memory word.
- Every cell of a row represents 8 bits. Every active vector contains one physical waveform index (which is displayed in hexadecimal notation).
- The padding (inactive) vectors are left blank in the figure.
- The numbers to the left of the memory words specify the absolute start addresses of the words within the vector areas.
- The numbers above the memory words are the logical vector numbers.
- The first label contains two sequencer constructs:

  - The first construct consists of the RPTV instruction and the single words starting at address 408 in the vector areas of both pins. Only the first 7 data cells of this block contain waveform DC/DC power units.
  - The second construct consists of the GENV instruction and the two words starting at addresses 416 and 424. The last 7 cells of the second word contain no user data.

The second label contains one sequencer construct (framed by a dotted line), which comprises two words.

### Syntax（取自子主题 Vector Setup Commands › Concepts of vector setup › The pattern master file）

The syntax of the pattern master file is as follows:

hp93000,pattern_master_file,0.1

[path:

 [<relative_or_absolute_path_1 >]]

files:

 <file_name_1_1>

 <file_name_1_2>

 ...

 <file_name_1_m>

[[path:

 [<relative_or_absolute_path_2>]]

files:

 <file_name_2_1>

 <file_name_2_2>

 ...

 <file_name_2_n>

...]

The default for the path is the vectorssubdirectory of the current device. But if you specify a path, note that the reference directory for relative paths is the waste subdirectory of the device. Therefore, if your pattern files are in the subdirectory sample of the vectors directory, you must specify the relative path to this directory as ./vectors/sample.

You can add comments to a pattern master file after "-- " (2 times the minus sign followed by a space) at the beginning of a line.

### Example（取自子主题 Vector Setup Commands › Concepts of vector setup › The pattern master file）

Both the usage of relative paths and the insertion of comments are illustrated by the following example file:

```

hp93000,pattern_master_file,0.1

-- The following file must reside in <device>/vectors:
files:
   sample1.binl

-- The following path points to <device>/vectors/pmfl_test:
path: ../vectors/pmfl_test

files:
  sample2.binl.gz
  sample3.binl.gz
```

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › APDV -  APpenD Vectors）

```
APDV {cmd_No}, {vect_length}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › APDV -  APpenD Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98313_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | A number that identifies the command within the sequencer area of the port to which the label belongs. Enter the command number of a GENV or RPTV instr…

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › APDV -  APpenD Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,520,,,(@)
< ...
> TSTL "test_1",(@)
> APDV 2,25
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,34,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,544,,,(@)
< ...
```

This example appends 25 vectors to the end of the sequencer construct with the command number 2. Note the change of the start address in command line 4.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › APTS -  APpend TeSt）

```
APTS {"label"}, {type}, {base_wf_set|"wavetable"|specset_id|"multiport_spec"} [,(port)]
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › APTS -  APpend TeSt）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98316_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：label | Defines the name of the new label. Enter an alphanumeric string in double quotes containing 1 to 128 characters.
> 表内引用（3 条，供检索）：`SQPG, SQPG? - (SeQuencer ProGramming)`（raw: `02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md`） · `DVCU, DVCU? - (Define Vector variable Configuration Usage)`（raw: `02.06.02.02.96_DVCU__DVCU__-__Define_Vector_variable_Configuration_Usage.md`） · `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example 1（取自子主题 Vector Setup Commands › List of vector setup commands › APTS -  APpend TeSt）

```
> APTS "test_2",MAIN,"gross_func_wtb"
> SQLB? ALL,ALL,(@)
< SQLB "test_1",MAIN,0,3,"gross_func_wtb"
< SQLB "test_2",MAIN,4,6,"gross_func_wtb"
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,12,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,520,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
```

This example appends a label to the sequencer area of the default port @. The label has the name `test_2`, is of type MAIN and is configured with the base wavetable `gross_func_wtb`. The following two queries display the result of the call. The STVA instruction of the new label points to the actual end of the vector areas.

### Example 2（取自子主题 Vector Setup Commands › List of vector setup commands › APTS -  APpend TeSt）

```
APTS "NEW",MAIN,"spec_port_1_port_2",(port_1)
```

This example appends the label `NEW` to the sequencer area of port `port_1`. The base wavetable is identified uniquely by specifying the multi-port specification `spec_port_1_port_2` and the port `port_1`, which belongs to `spec_port_1_port_2`.

### BCMT（取自子主题 Vector Setup Commands › List of vector setup commands › BCMT  BCMT  -  Binary CoMmenT）

```
BCMT {vect_addr}, {vect_length}[, HIMEN][, (port)], {#spec(data)}
```

### BCMT?（取自子主题 Vector Setup Commands › List of vector setup commands › BCMT  BCMT  -  Binary CoMmenT）

```
BCMT? [(portlist)]
```

returns:

```
BCMT {vect_addr}, {vect_length}[, HIMEN][, (port)], {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98488_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：vect_addr | The first vector of the segment for which comments are to be transferred. This number counts the active vectors of the port (as specified for the po…

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › BCMT  BCMT  -  Binary CoMmenT）

```
> BCMT?
< BCMT 0,49,#9000000078&!This is the first vector
  of test_2&0This is the first vector of test_3
```

This call of BCMT? displays the comments of the default port. The `&` character (with the decimal ASCII value 38) indicates the (identical) length of the two comments. The first comment is at vector 33 (decimal ASCII value of the ! character), the second at vector 48 (decimal ASCII value of the 0 character).

### BLUP（取自子主题 Vector Setup Commands › List of vector setup commands › BLUP -  BLock UP to date）

```
BLUP {"name"}, {type}, {state},
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › BLUP -  BLock UP to date）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98490_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：name | The name of a label.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › BLUP -  BLock UP to date）

```
BLUP "test",LBL,UPDT,
```

This example sets the state of label `test` to up to date.

### CMNT（取自子主题 Vector Setup Commands › List of vector setup commands › CMNT  CMNT  -  CoMmeNT）

```
CMNT {act_vect_of_port}, {"text"}[, (port)]
```

### CMNT?（取自子主题 Vector Setup Commands › List of vector setup commands › CMNT  CMNT  -  CoMmeNT）

```
CMNT? {act_vect_of_port}, [vect_length][, (port)]
```

returns:

```
CMNT {act_vect_of_port}, {"text"}[, (port)]
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › CMNT  CMNT  -  CoMmeNT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98506_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：act_vect_of_port | Specifies the active vector of the referenced port at which the comment is to be inserted, or, in the query, the first vector of which the co…

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › CMNT  CMNT  -  CoMmeNT）

Display the sequencer area of the default port:

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
< SQPG 5,STVA,528,,,(@)
< SQPG 6,STSA,,,,(@)
< SQPG 7,GENV,12,,,(@)
< SQPG 8,STOP,,,,(@)
```

Add the comment "Start of test_2" to the active vector 15 of the default port @, that is, to the first active vector of the second label:

```
> CMNT 15,"Start of test_2"
```

Activate test_2 for editing and display the comments for its vectors with the label specific TCMT? query:

```
> TSTL "test_2",(@)
> TCMT? 0,11
< TCMT 0,"Start of test_2"
```

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › CMVC -  Clear and MoVe Comments）

CMVC {src_vec_No}, {dst_vec_No}, {vect_length}

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › CMVC -  Clear and MoVe Comments）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98507_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：src_vec_No | The logical vector number that determines the start of the source range.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › CMVC -  Clear and MoVe Comments）

```
> CMNT? 0,6
< CMNT 0,"0"
< CMNT 1,"1"
< CMNT 2,"2"
< CMNT 3,"3"
< CMNT 4,"4"
< CMNT 5,"5"
> TSTL "test_1",(@)
> CMVC 0,4,2
> CMNT? 0,6
< CMNT 4,"0"
< CMNT 5,"1"
```

This example moves comments in the vector range 0 to 1 to the range 4 to 5. The previous comments for vectors 4 and 5 are overwritten, the comments for vector 2 and 3 are cleared.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › CNGV -  CoNnect Generate Vectors）

```
CNGV {(cmd_No)}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › CNGV -  CoNnect Generate Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98508_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number which references the first of the two consecutive GENV sequencer constructs.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › CNGV -  CoNnect Generate Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,GENV,8,,,(@)
< SQPG 4,STOP,,,,(@)
> TSTL "test_1",(@)
> CNGV 2
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,17,,,(@)
< SQPG 3,STOP,,,,(@)
```

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › CPYV -  CopY Vectors）

```
CPYV {src_vec_No}, {dst_vec_No}, {vect_length}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98511_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：src_vec_No | The logical vector number that determines the start of the source range.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › CPYV -  CopY Vectors）

```
> SQPG? all,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
> $VECD? PARA,SM,504,24,(S0_1)
< VECD PARA,SM,504,24,(S0_1),
  0000 0001  0000 0001  0000 0001  0000 0001  0000 0001  0000 0011  0000 0001  0000 0001
  0000 0001  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000
  0000 0000  0000 0000  0000 0000  0000 0001  0000 0011  0000 0001  0000 0000  0000 0000
```

The first three active vectors of the RPTV instruction (with the logical vector numbers 9 to 11) are set to 0 for pin S0_1. Now activate the label for editing and copy vectors 12 to 14 to position 9 for S0_1:

```
> TSTL "test_1",(@)
> CPYV 12,9,3,(S0_1)
```

Display the result:

```
> $VECD? PARA,SM,504,24,(S0_1)
< VECD PARA,SM,504,24,(S0_1),
  0000 0001  0000 0001  0000 0001  0000 0001  0000 0001  0000 0011  0000 0001  0000 0001
  0000 0001  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000  0000 0000
  0000 0001  0000 0011  0000 0001  0000 0001  0000 0011  0000 0001  0000 0000  0000 0000
```

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › DELI -  DELete Instruction）

```
DELI {cmd_No}, {count}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › DELI -  DELete Instruction）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98536_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number which references the first sequencer instruction to be deleted.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › DELI -  DELete Instruction）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,27,,,(@)
< SQPG 3,RPTV,7,5,,(@)
< SQPG 4,STOP,,,,(@)
< SQPG 5,STVA,544,,,(@)
< ...
> DELI 2,1
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,7,5,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,544,,,(@)
< ...
```

This example deletes the sequencer instruction with command number 2 from the sequencer area of the default port @. Note that since the vectors of the instruction are not deleted, the start address of the following label (STVA instruction at command number 4) does not change.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › DELV -  DELete Vectors）

```
DELV {cmd_No}, {vect_length}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › DELV -  DELete Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98537_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number which references the sequencer construct where vectors are to be deleted. The instruction of the construct must be GENV (GENerate Ve…

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › DELV -  DELete Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,34,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,544,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
> TSTL "test_1",(@)
> DELV 2,25
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,520,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
```

This example deletes 25 vectors from the end of the sequencer construct referenced by command number 2. Three memory words become inactive in the process and are deleted. The start address of the following label (command line 4) is adjusted.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › DLPP -  DeLete Per Pin Subroutine）

```
DLPP {label}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › DLPP -  DeLete Per Pin Subroutine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98563_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：label | Specifies the name of the per-pin subroutine to be deleted.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › DLPP -  DeLete Per Pin Subroutine）

```
DLPP "summer"
```

This command deletes the per-pin subroutine referenced by the label "summer".

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › DLTS -  DeLete TeSt）

```
DLTS {"label"}[, (port)]
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › DLTS -  DeLete TeSt）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98565_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：label | Specifies the label to be deleted.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › DLTS -  DeLete TeSt）

```
DLTS "MPBU_port_1_port_2",(port_1)
```

This example deletes the label referenced by `MPBU_port_1_port_2` from the port `port_1`.

### DMAS（取自子主题 Vector Setup Commands › List of vector setup commands › DMAS  DMAS  -  Define Memory Area Size）

```
DMAS SQPG, [memory], {size}, {(port)}
```

### DMAS?（取自子主题 Vector Setup Commands › List of vector setup commands › DMAS  DMAS  -  Define Memory Area Size）

Area type PARA:

```
DMAS? PARA, [memory], PER_PORT, {(port_list)}
```

returns:

```
DMAS PARA, {memory}, {size}, {(port)}
```

Area type SQPG:

```
DMAS? SQPG, [SM], [PER_PORT,] {(port_list)}
```

returns:

```
DMAS SQPG, SM, {size}, {(port)}
```

Area type PPSQ:

```
DMAS? PPSQ, [SM], [PER_PORT,] {(@)}
```

returns:

```
DMAS PPSQ, SM, {size}, {(@)}
```

Area type RSLT, querying ports:

```
DMAS? RSLT, [SM], [PER_PORT,] {(port_list)}
```

returns:

```
DMAS RSLT, SM, {size}, {port}
```

Area type RSLT, querying pins:

```
DMAS? RSLT, [SM], {PER_PIN}, {(pin_list)}
```

returns:

```
DMAS RSLT, SM, {size}, {pin}
```

Area type SAVE:

```
DMAS? SAVE, ALL, [PER_PORT,] {(port_list)}
```

returns:

```
DMAS SAVE, {memory}, {size}, {(port)}
```

Area type ALL:

```
DMAS? ALL, [memory], [PER_PORT,] {(port_list)}
```

returns:

```
DMAS {area}, {memory}, {size}, {(port)}
```

Area type MFRE, querying ports:

```
DMAS? MFRE, [SM|SMEXT], [PER_PORT,] {(port_list)}
```

returns:

```
DMAS MFRE, {SM|SMEXT}, {size}, {port}
```

Area type MFRE, querying pins:

```
DMAS? MFRE, [SM|SMEXT], {PER_PIN}, {(pin_list)}
```

returns:

```
DMAS MFRE, {SM|SMEXT}, {size}, {pin}
```

Area type MFRE, querying channels:

```
DMAS? MFRE, [SM|SMEXT], {PER_CHANNEL}, {(channel_list)}
```

returns:

```
DMAS MFRE, {SM|SMEXT}, {size_1}, {size_2}, {size_3}, {(channel)}
```

Area type MFRP, querying channels:

```
DMAS? MFRP, [SM|SMEXT], {PER_CHANNEL}, {(port_list)}
```

returns:

```
DMAS MFRP, {SM|SMEXT}, {size_1}, {size_2}, {size_3}, {(channel)}
```

Area type MFRP, querying pools:

```
DMAS? MFRP, [SM|SMEXT], {PER_POOL}, {(port_list)}
```

returns:

```
DMAS MFRP, {SM|SMEXT}, {pool_size}, {(pool_channels)}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › DMAS  DMAS  -  Define Memory Area Size）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98566_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：29 行 × 3 列。
> 首行（上游原文）：area | The area parameter specifies the type of data for which a memory area is to be set or read. It can be one of the following:
> 表内引用（3 条，供检索）：`Selecting the memory type`（raw: `02.06.07.01.04.01_Selecting_the_memory_type.md`） · `Defining a compliance pattern for pattern‑based SmartLoop testing`（raw: `02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md`） · `Technology file for a device - himem`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md#_49363__row_himem`）

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › DMAS  DMAS  -  Define Memory Area Size）

The following example illustrates the various options of the MFRE and MFRP queries. First, the free memory range of the `port12` port is queried on the port level:

```
> DMAS? MFRE,,(port12)
< DMAS MFRE,SM,84288,(port12)
```

On the pin level, the corresponding query and reply look as follows:

```
> DMAS? MFRE,,PER_PIN,(port12)
< DMAS MFRE,SM,84288,(Pin1)
< DMAS MFRE,SM,88288,(Pin2)
```

Note that the query per port returns the smaller of the two values.

`Pin1` is mapped to channel 10101, `Pin2` to channel 10102. Thus the corresponding channel related query and its reply are

```
> DMAS? MFRE,,PER_CHANNEL,(10101,10102)
< DMAS MFRE,SM,84212,84312,84640,(10101)
< DMAS MFRE,SM,88312,88312,88640,(10102)
```

The figures are slightly different, because the query per channel only considers the hardware.

Finally, the two possible options for MFRP, applied to `port12`, produce

```
> DMAS? MFRP,,PER_CHANNEL,(port12)
< DMAS MFRP,SM,84212,84312,84640,(10101)
< DMAS MFRP,SM,88312,88312,88640,(10102)
< DMAS MFRP,SM,84212,84312,84640,(10103)
< DMAS MFRP,SM,90464,90464,90736,(10104)
```

 for the PS9G pool 10101 through 10104, and

```
> DMAS? MFRP,,PER_POOL,(port12)
< DMAS MFRP,SM,347400,(10101,10102,10103,10104)
```

### DPPC（取自子主题 Vector Setup Commands › List of vector setup commands › DPPC -  Define Per Pin subroutine Configuration）

```
DPPC {name}, {parameter}, [value], {(pinlist)}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › DPPC -  Define Per Pin subroutine Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98567_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：name | Name of the Pin-Per Sequencer Subroutine label. For the query, you can enter ALL to return all PPSS labels.

### DPPS（取自子主题 Vector Setup Commands › List of vector setup commands › DPPS  DPPS  -  Define Per Pin Subroutine label）

```
DPPS {name}, {cycle_len}
```

### DPPS?（取自子主题 Vector Setup Commands › List of vector setup commands › DPPS  DPPS  -  Define Per Pin Subroutine label）

```
DPPS? {name}
```

returns:

```
DPPS {name}, {cycle_len}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › DPPS  DPPS  -  Define Per Pin Subroutine label）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98568_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：name | Per-pin Subroutine name. This parameter can be used to call the subroutine from a parallel sequencer program. For the query, you can also enter ALL to re…

### DPSA（取自子主题 Vector Setup Commands › List of vector setup commands › DPSA  DPSA  -  Define per Pin Subroutine Address）

```
DPSA {name}, {address}, {(pinlist)}
```

### DPSA?（取自子主题 Vector Setup Commands › List of vector setup commands › DPSA  DPSA  -  Define per Pin Subroutine Address）

```
DPSA? {name}, {(pinlist)}
```

returns:

```
DPSA {name}, {address}, {(pinlist)}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › DPSA  DPSA  -  Define per Pin Subroutine Address）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98571_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：name | Per-pin Subroutine name. This parameter can be used to call the subroutine from a parallel sequencer program. For the query, you can also enter ALL to re…

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › FTSM  FTSM  -  Functional Test Set Mask）

```
FTSM {mode}, [run_to], [mask_before], [mask_after][,(ref_port)]
FTSM?
FTSM?
```

returns:

```
FTSM CLEAR, , ,
```

or

```
FTSM SET, [run_to], [mask_before], [mask_after][,(ref_port)]
```

  Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98607_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：mode | Lets you set the mode of the FTSM command. The mode can be:

For a multi-port burst, this parameter specifies the reference port to which the cycle numbers of the run_to, mask_before, and mask_after parameters refer.

If you have set the run_to parameter, then the sequencers will be stopped for all ports after the reference port has completed the requested number of cycles. The mask_before, and mask_after parameters are only applied to the specified port. The other ports will not be masked,

Note that the reference port must belong to the current start label (as defined by SQSL).

   |  Application Used in the parametric functional test. Errors and warnings

An error is generated if:

- A value (run_to, mask_before, mask_after) is not in the valid range of [0... 2^48 - 2].
- The run_to and mask_before parameters are specified, and run_to is equal or bigger than mask_before.
- The run_to and the mask_after parameters are specified, and run_to is bigger than mask_after.

A warning is generated if:

- The run_to parameter and the mask_before parameter are specified and run_to < mask_before. In this case the pattern executed will always pass as all cycles executed are masked out for result evaluation.
- The run_to parameter and the mask_after parameter are specified and run_to <= mask_after. In this case the entry for the mask_after parameter can be omitted as the sequencer will not even execute the cycles that are masked out.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › FTSM  FTSM  -  Functional Test Set Mask）

```
FTSM?
```

returns:

```
FTSM CLEAR, , ,
FTSM SET, ,10,20
```

The FTSM? query returns the current FTSM settings.

The FTSM SET command masks all cycles except for those in the range from cycle 10 to cycle 20.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › GETA  -  GET vector memory Address information）

GETA? {type}, [param_1], {param_2}, {(pinlist)}

returns:

GETA {type}, {param_1}, {param_2}, {applic}, {start_addr}, {length}, {(pinlist)}

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › GETA  -  GET vector memory Address information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98613_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：type | Specifies the type of test for which vector area address information is required. The only allowed value is VEC (for VECtors).

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › GETA  -  GET vector memory Address information）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
> TSTL "test_1",(@)
> GETA? VEC,,9,(S0_1)
< GETA VEC,"test_1",9,PARA,520,6,(S0_1)
```

This example queries the absolute address of the parallel vector with the logical vector number 9 (the first active vector of the RPTV instruction) in the label test_1 for pin S0_1. Note that 7 padding vectors exist between the last active vector of the GENV instruction and the first active vector of the RPTV instruction.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › INGV -  INsert Generate Vectors）

```
INGV{cmd_No}, {num_vec}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › INGV -  INsert Generate Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98639_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number before which the GENV instruction is to be inserted.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › INGV -  INsert Generate Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,10,5,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,16,,,(@)
< ...
> TSTL "test_1",(@)
> INGV 3,11
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,10,5,,(@)
< SQPG 3,GENV,11,,,(@)
< SQPG 4,STOP,,,,(@)
< SQPG 5,STVA,32,,,(@)
< ...
```

This example inserts a GENV instruction for 11 vectors before command 2. Note that the memory type is SM, as in command 0, and that the address of command 5 has been increased.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › INSI -  INsert Instructions）

```
INSI {cmd_No}, {count}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › INSI -  INsert Instructions）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98640_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cmd_No | The command number before which instructions are to be inserted.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › INSI -  INsert Instructions）

```
TSTL "test_1",(@)
INSI 358, 12
```

This example inserts 12 NOP sequencer instructions before command number 358.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › NODV  -  Number Of Displayable Vectors）

```
NODV?
```

returns:

```
NODV {num_vec}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › NODV  -  Number Of Displayable Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98663_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：num_vec | returns the number of active vectors.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › NODV  -  Number Of Displayable Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,9,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
> TSTL "test_1",(@)
> NODV?
< NODV 15
```

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › RSET -  ReSET）

```
RSET {specifier}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › RSET -  ReSET）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98723_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：specifier | The specifier can be:
> 表内引用（1 条，供检索）：`UHCM`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › RSET -  ReSET）

```
RSET TIM
```

This example resets all waveform sets and timing sets and loads the hardware with the default vector rate and edge placement values. Only waveform set 1 and timing set 1 in waveform set 1 is active.

### SAOF（取自子主题 Vector Setup Commands › List of vector setup commands › SAOF  SAOF  -  Set Alternating Operation Features）

```
SAOF {mode|"label"}
```

### SAOF?（取自子主题 Vector Setup Commands › List of vector setup commands › SAOF  SAOF  -  Set Alternating Operation Features）

```
SAOF?
```

returns:

```
SAOF {mode|"label"}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › SAOF  SAOF  -  Set Alternating Operation Features）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98726_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：mode | The operation mode which can take the following values:

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › SAOF  SAOF  -  Set Alternating Operation Features）

The following example illustrates the effects of the APP mode:

```
> SAOF?
< SAOF ZERO
> DMAS SQPG,SM,4,(@)
> DMAS SQPG,SM,3,(@)
> DMAS? SQPG,SM,(@)
< DMAS SQPG,SM,3,(@)
> SAOF APP
> DMAS SQPG,SM,4,(@)
> SAOF ZERO
> DMAS? SQPG,SM,(@)
< DMAS SQPG,SM,7,(@)
```

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › SPGV -  SPlit Generate Vectors）

```
SPGV {vec_No}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › SPGV -  SPlit Generate Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98740_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：vec_No | The logical vector number at which a GENV sequencer construct is to be split.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › SPGV -  SPlit Generate Vectors）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,16,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
< SQPG 5,STVA,528,,,(@)
< ...
> SPGV 7
> TSTL "test_1",(@)
> SQPG ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,7,,,(@)
< SQPG 3,GENV,9,,,(@)
< SQPG 4,RPTV,6,5,,(@)
< SQPG 5,STOP,,,,(@)
< SQPG 6,STVA,536,,,(@)
< ...
```

This example splits a GENV sequencer construct at command number 2 before vector 7. Note the adjustment of the start address in command 6.

### SQGB（取自子主题 Vector Setup Commands › List of vector setup commands › SQGB  SQGB  -  SeQuencer GloBal）

```
SQGB [mode], [analyze_delay][, (ref_port)]
```

### SQGB?（取自子主题 Vector Setup Commands › List of vector setup commands › SQGB  SQGB  -  SeQuencer GloBal）

```
SQGB? [(portlist)]
```

returns:

```
SQGB {mode}, [analyze_delay][, (port)]
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › SQGB  SQGB  -  SeQuencer GloBal）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98746_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：mode | Possible values are:
> 表内引用（1 条，供检索）：`GETC? - (GET Cycles)`（raw: `02.06.02.02.131_GETC__-__GET_Cycles.md`）

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › SQGB  SQGB  -  SeQuencer GloBal）

```
> PCLK? "mu_burst",1,(@@)
< PCLK "mu_burst",1,20,(P1)
< PCLK "mu_burst",1,10,(P2)
> SPRM "mu_burst",1,,
> SQSL "mu_burst"
> SQGB STSQ,30,(P2)
> SQGB? (@@)
< SQGB STSQ,15,(P1)
< SQGB STSQ,30,(P2)
```

This example configures the sequencers to stop when port P2 has completed 30 cycles. Port P1, whose period length is twice the period length of P2, will be stopped after 15 cycles. Note that P1 and P2 must belong to the same sequencing group.

### SQLA（取自子主题 Vector Setup Commands › List of vector setup commands › SQLA  SQLA  -  SeQuencer Label Attribute）

```
SQLA [type],{"name"},{"attr_key_1=[attr_val_1] [,attr_key_2=[attr_val_2] [,attr_key_3=[attr_val_3]]]"} [,(port)]
```

### SQLA?（取自子主题 Vector Setup Commands › List of vector setup commands › SQLA  SQLA  -  SeQuencer Label Attribute）

```
SQLA? [type], {"name"|ALL}, {"attr_key"|ALL|SAVE} [, (portlist)]
```

returns:

```
SQLAtype, {"name"},{"attr_key_1=attr_val_1, attr_key_2=attr_val_2} [,attr_key_3=attr_val_3]" [,(port)]
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › SQLA  SQLA  -  SeQuencer Label Attribute）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/103621_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：type | Currently, LBL is the only possible value. This is also the default.
> 表内引用（2 条，供检索）：`Selecting the memory type`（raw: `02.06.07.01.04.01_Selecting_the_memory_type.md`） · `Defining a compliance pattern for pattern‑based SmartLoop testing`（raw: `02.06.17.04.01_Defining_a_compliance_pattern_for_pattern__ased_SmartLoop_testing.md`）

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › SQLA  SQLA  -  SeQuencer Label Attribute）

```
> APTS LBL,"test","table1"
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,10,5,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,16,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
> SQLA ,"test","PARA_MEM=SHMEM"
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,RPTV,10,5,,(@)
< SQPG 3,STOP,,,,(@)
< SQPG 4,STVA,0,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,STOP,,,,(@)
```

This example changes the PARA_MEM attribute of the new label test from SM to SHMEM. Note the change of the address in command line 4.

### SQLB（取自子主题 Vector Setup Commands › List of vector setup commands › SQLB  SQLB  -  SeQuencer LaBel definition）

```
SQLB {"label"}, {type}, {start_cmd_no}, {stop_cmd_no}, [base_wf_set|"wavetable_name"| "sync_grp"] [, (port)]
```

### SQLB（取自子主题 Vector Setup Commands › List of vector setup commands › SQLB  SQLB  -  SeQuencer LaBel definition）

```
SQLB? {"label"|ALL}, {type|ALL}[, (portlist)]
```

returns:

```
SQLB {label}, {type}, {start_cmd_no}, {stop_cmd_no}, {"wavetable_name"|base_wf_set| "sync_grp"} [,(port)]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98748_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：19 行 × 3 列。
> 首行（上游原文）：label | The label name. It identifies the label which is to be defined for the specified port, or whose definition is to be displayed. Enter a string enclosed i…
> 表内引用（4 条，供检索）：`SmarTest character and number limits`（raw: `../../01_Getting_started/01.05_SmarTest_character_and_number_limits/01.05_SmarTest_character_and_number_limits.md#_128029__max_labels_per_port`） · `SQSL`（raw: `02.06.02.02.240_SQSL__SQSL__-__SeQuencer_Start_Label.md`） · `Burst and Multi-Burst Labels`（raw: `02.06.07.01.08.05.03_Burst_labels_and_multi-port_burst_labels.md`） · `DVCU, DVCU? - (Define Vector variable Configuration Usage`（raw: `02.06.02.02.96_DVCU__DVCU__-__Define_Vector_variable_Configuration_Usage.md`）

### Example 1（取自子主题 Vector Setup Commands › List of vector setup commands › SQLB  SQLB  -  SeQuencer LaBel definition）

This example defines a burst label for the default port.

Display the whole sequencer area:

```
> SQPG? ALL,(@)
< ...
< SQPG 8,STOP,,,,(@)
```

The sequencer area comprises nine command lines. Three further lines are required for the rudimentary burst label. Thus, issue:

```
> DMAS SQPG,SM,12,(@)
```

Define the label:

```
> SQLB "burst_1",BRST,9,11,"gross_func_wtb",(@)
```

Display the whole sequencer area again:

```
> SQPG? ALL,(@)
< ...
< SQPG 8,STOP,,,,(@)
< SQPG 9,NOP,,,,(@)
< SQPG 10,NOP,,,,(@)
< SQPG 11,BEND,,,,(@)
```

You can now replace the NOP instructions in command lines 9 and 10 by CALL instructions with the SQPG command.

### Example 2（取自子主题 Vector Setup Commands › List of vector setup commands › SQLB  SQLB  -  SeQuencer LaBel definition）

This example queries all labels of all types for the default port.

```
> SQLB? ALL,ALL
< SQLB "test_1",MAIN,0,4,"spec_search_wtb"
< SQLB "test_2",MAIN,5,8,"spec_search_wtb"
< SQLB "burst_1",BRST,9,11,"gross_func_wtb"
```

### Example 3（取自子主题 Vector Setup Commands › List of vector setup commands › SQLB  SQLB  -  SeQuencer LaBel definition）

This example renames the burst label `burst_1`, defined in example 1, to "BURST1".

```
> SQLB "BURST1",BRST,9,11,"gross_func_wtb"
> SQLB? ALL,BRST
< SQLB "BURST1",BRST,9,11,"gross_func_wtb"
```

### Example 4（取自子主题 Vector Setup Commands › List of vector setup commands › SQLB  SQLB  -  SeQuencer LaBel definition）

This example illustrates the relative numbering of the command lines in SAOF APP mode.

```
> SAOF?
< SAOF ZERO
> SQLB? ALL,ALL
< SQLB "L_1",MAIN,0,2,"wf1"
> SAOF APP
> DMAS SQPG,SM,3,(@)
> SQLB "L_2",MAIN,0,2,"wf1"
> SAOF ZERO
> SQLB? ALL,ALL
< SQLB "L_1",MAIN,0,2,"wf1"
< SQLB "L_2",MAIN,3,5,"wf1"
```

### SQPG（取自子主题 Vector Setup Commands › List of vector setup commands › SQPG  SQPG  -  SeQuencer ProGramming）

```
SQPG {cmd_No}, {instr}, [param_1], [param_2], [memory], {(port)}
```

### SQPG?（取自子主题 Vector Setup Commands › List of vector setup commands › SQPG  SQPG  -  SeQuencer ProGramming）

```
SQPG? {cmd_No|ALL|"cmd_No_A,cmd_No_B"}, {(portlist)}
```

returns:

```
SQPG {cmd_No}, {instr}, [param_1], [param_2], [memory], {(port)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98749_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：44 行 × 3 列。
> 首行（上游原文）：cmd_No | The command number. This parameter identifies the instruction within the sequencer area of the specified port. Refer to Address instructions for furthe…

### Example 1（取自子主题 Vector Setup Commands › List of vector setup commands › SQPG  SQPG  -  SeQuencer ProGramming）

The following is a simple example of a counted match loop:

```
SQPG 3,MACT,256,CONTINUE,,(@)
SQPG 4,GENV,5,,,(@)
SQPG 5,MRPT,5,,,(@)
```

Note that only the GENV or RPTV instruction is allowed immediately before the MACT instruction. CONTINUE, which is optional, tells SmarTest to continue the surrounding test even if the match loop failed.

### Example 2（取自子主题 Vector Setup Commands › List of vector setup commands › SQPG  SQPG  -  SeQuencer ProGramming）

The following example shows that inserting a GENV instruction into a label with SQPG disturbs the sequencer constructs and must be accompanied by an appropriate adjustment of the vector areas (see also `Inserting a sequencer instruction`（raw: `02.06.07.01.07.03.01_Inserting_a_sequencer_instruction.md`）).

Display the sequencer area of the default port:

```
> SQPG? ALL,(@)
< ...
< SQPG 4,STVA,504,,,(@)
< SQPG 5,STSA,,,,(@)
< SQPG 6,GENV,9,,,(@)
< SQPG 7,STOP,,,,(@)
< SQPG 8,STVA,520,,,(@)
< ...
```

The vector area segment of the label starting at command 4 comprises 2 memory words, as shown by the start address of the following label (command line 8).

Now display the vector area segment of pin S0_1 for the label starting at command 4, and also the first memory word of the following label:

```
> $VECD? PARA,SM,504,24,(S0_1)
< VECD PARA,SM,504,16,(S0_1),
 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001
 0000 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
 0000 0010 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
```

The GENV instruction is associated with the first two memory words. The last 7 bytes of the second word are padding vectors. This is shown by making the first label the start label and then displaying the active vectors of command 6 for pin `S0_1`:

```
> SQSL "test_1"
> $VCYC? 0,9,(S0_1)
< VCYC 0,9,GENV,F160,(S0_1),
 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001 0000 0001
 0000 0001
```

Now insert a GENV instruction before command 6:

```
> TSTL "test_1",
> INSI 6,1
> SQPG 6,GENV,1,,,(@)
```

Display the active vectors for the two GENV instructions:

```
> $VCYC? 0,10,(S0_1)
< VCYC 0,1,GENV,F160,(S0_1), 0000 0001
< VCYC 1,9,GENV,F160,(S0_1),
 0000 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
 0000 0010
```

The first memory word is now associated with the new instruction. The first of its vectors is active, the others are inactive. The previous command 6 (now command 7) is now associated with the second and the third block. Thus the third memory word is illegally shared between two labels.

### SQSL（取自子主题 Vector Setup Commands › List of vector setup commands › SQSL  SQSL  -  SeQuencer Start Label）

```
SQSL  {"label"} [, site|"site_string"]
```

### SQSL?（取自子主题 Vector Setup Commands › List of vector setup commands › SQSL  SQSL  -  SeQuencer Start Label）

```
SQSL?
```

returns:

```
SQSL {"label"}
```

With the TYPE option:

```
SQSL?TYPE
```

returns:

```
SQSL {"label"}, {type}, {(portlist)}
```

With the ALL option:

```
SQSL?ALL
```

returns:

```
SQSL {"label"}, {"site_string"}, {type}, {(portlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98751_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：label | The name of a sequencer start label. In the command, you can enter an empty string ("") to deactivate the current start label.

### Example 1（取自子主题 Vector Setup Commands › List of vector setup commands › SQSL  SQSL  -  SeQuencer Start Label）

```
> SQSL "test_1"
> SQSL? TYPE
< SQSL "test_1",MAIN,(@)
```

### Example 2（取自子主题 Vector Setup Commands › List of vector setup commands › SQSL  SQSL  -  SeQuencer Start Label）

```
> PSFC 2
> SQSL "test_1"
> SQSL? ALL
< SQSL "test_1","11",MAIN,(@)
> SQSL "test_2", "10"
> SQSL "test_3", 2
> SQSL? ALL
< SQSL "test_2","10",MAIN,(@)
< SQSL "test_3","01",MAIN,(@)
> SQSL?
< SQSL "test_2"
> PQFC 2
> SQSL?
< SQSL "test_3"
```

This example illustrates the definition of different start labels for different sites. Note that the restriction of the setup focus has no influence on the command, but that the setting of the query focus does affect SQSL?.

### SQST（取自子主题 Vector Setup Commands › List of vector setup commands › SQST  SQST  -  SeQuencer STate）

SQST {seq_state} [,"exec_context"]

### SQST?（取自子主题 Vector Setup Commands › List of vector setup commands › SQST  SQST  -  SeQuencer STate）

```
SQST? ["exec_context"]
```

returns:

```
SQST {seq_state}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › SQST  SQST  -  SeQuencer STate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98752_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：seq_state | Gives the state of the sequencer:
> 表内引用（2 条，供检索）：`SQGB, SQGB? - (SeQuencer GloBal)`（raw: `02.06.02.02.232_SQGB__SQGB__-__SeQuencer_GloBal.md`） · `Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › SQST  SQST  -  SeQuencer STate）

```
SQST RUN
```

This example starts a global sequencer run.

### SQTO（取自子主题 Vector Setup Commands › List of vector setup commands › SQTO  SQTO  -  SeQuencer TimeOut）

```
SQTO {timeout}             // in seconds
```

### SQTO?（取自子主题 Vector Setup Commands › List of vector setup commands › SQTO  SQTO  -  SeQuencer TimeOut）

```
SQTO?
```

returns:

```
SQTO {timeout}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › SQTO  SQTO  -  SeQuencer TimeOut）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98753_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：timeout | Defines the time (in seconds) that the sequencer runs. The default value is 900 and the range is 0.001 to 2147483.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › SQTO  SQTO  -  SeQuencer TimeOut）

```
SQTO 3000
```

This example programs the sequencer to exit after 50 minutes.

### SREC（取自子主题 Vector Setup Commands › List of vector setup commands › SREC  SREC  -  Set RECeiver mask）

```
SREC {mask_value}, {(pinlist)}
```

### SREC?（取自子主题 Vector Setup Commands › List of vector setup commands › SREC  SREC  -  Set RECeiver mask）

```
SREC? {(pinlist)}
```

Note Executing `SREC ACT,(@)` may cause excessive overhead. You can use the `UI_SUSPEND`（raw: `../02.07_Test_Method_Reference/02.07.04.01.260_UI_SUSPEND.md`） test method API to suspend updates of the graphical user interface.

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › SREC  SREC  -  Set RECeiver mask）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98754_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：mask_value | The mask value parameter specifies whether a pin mask will be applied:
> 表内引用（2 条，供检索）：`DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） · `DFGE, DFGE? - (DeFine Group Expressions)`（raw: `02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md`）

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › SREC  SREC  -  Set RECeiver mask）

```
SREC X, (D1, D2, D3, D4)
```

This example masks the pins D1, D2, D3 and D4.

### TCMT（取自子主题 Vector Setup Commands › List of vector setup commands › TCMT  TCMT  -  Test CoMment Transfer）

```
TCMT {vect_addr}, {"text"}
```

### TCMT?（取自子主题 Vector Setup Commands › List of vector setup commands › TCMT  TCMT  -  Test CoMment Transfer）

```

TCMT? {vect_addr}, [vect_length]
```

returns a comment text for each TCMT in the range vect_addr to vect_addr `+`vect_length `- 1`.

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › TCMT  TCMT  -  Test CoMment Transfer）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98767_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：vect_addr | The logical number of the vector at which the comment is to be inserted or read. The specified number range must not exceed the maximum vector addre…

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › TCMT  TCMT  -  Test CoMment Transfer）

```
TCMT 2063,"Start of test 2".
```

This example inserts the comment "Start of test 2" at the logical vector address 2063.

### TSTL（取自子主题 Vector Setup Commands › List of vector setup commands › TSTL  TSTL  -  TeST Label）

```
TSTL {"label"}, [(port)]
```

### TSTL?（取自子主题 Vector Setup Commands › List of vector setup commands › TSTL  TSTL  -  TeST Label）

```
TSTL?
```

returns:

```
TSTL {"label"}, {(port)}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › TSTL  TSTL  -  TeST Label）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98815_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：label | Defines the label you wish to edit. Enter an alphanumeric string, 1 to 128 characters long, enclosed in double quotes. You can deactivate the currently …

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › TSTL  TSTL  -  TeST Label）

```
TSTL "new",
```

This example selects the label "new" for editing.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › VDCG  -  Verify Device Cycle for Group）

```
VDCG? {waveform_set}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {waveform_set}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {specset_id}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {specset_id}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {wavetable_name}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {wavetable_name}, {dev_cyc_name}, {dev_cyc_len}
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › VDCG  -  Verify Device Cycle for Group）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98846_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 4 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › VDCG  -  Verify Device Cycle for Group）

```
VDCG? 1,ALL,(inputs)
```

returns:

```
VDCG 1,ALL,SLEN
```

This example checks the consistency of all device cycles for pins in the pin group "inputs" in waveform set 1. The test system replies that all device cycles for the specified group are consistently defined.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › VDCN -  Vector Device Cycle Name）

VDCN {vec_No}, {"dev_cyc_name"}, {dev_cyc_len}, {repeat_count}, {(pinlist)}

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › VDCN -  Vector Device Cycle Name）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98847_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：vec_No | A logical vector number of the selected label. Logical vector numbers count the active vectors of one label. The first active vector of a label has the…

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › VDCN -  Vector Device Cycle Name）

```
VDCN 93, "EXAMPL", 1, 15, (@)
```

This example downloads vector data resulting from the default values for the EXAMPL device cycle to all pins, starting at active vector 93. The download is repeated 15 times.

### VDCP（取自子主题 Vector Setup Commands › List of vector setup commands › VDCP  VDCP   Vector Device Cycle Parameter）

VDCP {vec_no}, {"dev_cyc_name"}, {dev_cyc_len}, [ed_comp], {DD1}, {DD2}, {ED1}, {ED2}, {(pinlist)}

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › VDCP  VDCP   Vector Device Cycle Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98848_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 2 列。
> 首行（上游原文）：vec_No | A logical vector number of the selected label. For the command, it determines the first active vector that will be overwritten. For the query, this par…

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › VDCP  VDCP   Vector Device Cycle Parameter）

```
> VDCP? 0,8,0,8,(S0_1)
< VDCP 0,"DNRZ",1,,F10,N,N,N,(S0_1)
< VDCP 1,"DNRZ",1,,F10,N,N,N,(S0_1)
< VDCP 2,"DNRZ",1,,F10,N,N,N,(S0_1)
< VDCP 3,"MYDC",2,,F00,N,N,N,(S0_1)
< VDCP 5,"MYDC",2,,F10,N,N,N,(S0_1)
< VDCP 7,"DNRZ",1,,F10,N,N,N,(S0_1)
> VDCP? 2,6,4,2,(S0_1)
< VDCP 5,"MYDC",2,,F10,N,N,N,(S0_1)
< VDCP 7,"DNRZ",1,,F10,N,N,N,(S0_1)
```

In the second call of VDCP? (the first call just serves to display the underlying situation) the range of interest starts at vector 6. Note that the reply starts with vector 5, and that the first occurrence of MYDC, which lies between vector 2 and vector 6, is not displayed.

### VECC（取自子主题 Vector Setup Commands › List of vector setup commands › VECC  VECC  -  VECtor download Compressed）

```
VECC {applic}, {type} [, port], {address}, {length}, {(pin_or_port)}, {#spec(data)}
```

### VECC?（取自子主题 Vector Setup Commands › List of vector setup commands › VECC  VECC  -  VECtor download Compressed）

```
VECC? {applic}, {type} [, port_list], {address}, [length], {(pinlist)}
```

returns:

```
VECC {applic}, {type} [, port], {address}, {length}, {(pin)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98850_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：applic | The parameter specifies the target area of the command, and the source area of the query. Possible values are:

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › VECC  VECC  -  VECtor download Compressed）

```
VECC? PARA,ALL,0,,(S0)
```

returns:

```
size: 21
data:
VECC PARA,ALL,0,,(S0)\x0A
size: 75
data:
VECD PARA,SM,0,56,(S0),#9000000016\x02Ee\x80\x02Ee\x814VX\x13Eu\x90\x00\x0A
status: 0
```

### VECD（取自子主题 Vector Setup Commands › List of vector setup commands › VECD  VECD  -  VECtor Download）

```
VECD {applic}, {type} [, port], {address}, {length}, {(pin_or_port)}, {#spec(data)}
```

### VECD?（取自子主题 Vector Setup Commands › List of vector setup commands › VECD  VECD  -  VECtor Download）

```
VECD? {applic}, {type} [, port_list], {address}, [length], {(pinlist)}
```

returns:

```
VECD {applic}, {type} [, port], {address}, {length}, {(pin)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98853_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：applic | The parameter specifies the target area of the command, and the source area of the query. Possible values are:

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › VECD  VECD  -  VECtor Download）

```
> VECD? PARA,SM,0,16,(OUT1)
< VECD PARA,SM,0,16,(OUT1),#9000000024\x0E\x0C\x0E\x0E\x0D\x0E\x0E\x0D\x0E\x0E\x0E\x0E
  \x0C\x0D\x0E\x0E
```

This example shows the answer as it is recorded in the MCDLog.

### Syntax（取自子主题 Vector Setup Commands › List of vector setup commands › VPAR  -  Vectors in PARallel）

```
VPAR? {start_vec_No}, {stop_vec_No}
```

returns:

```
VPAR {cmd_No}, [frst_used_vec]
```

### Parameters（取自子主题 Vector Setup Commands › List of vector setup commands › VPAR  -  Vectors in PARallel）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98860_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：start_vec_No | Defines the offset of the first vector to be searched from the start vector of the currently selected label. The specified address must not excee…

NISQ (Non-Interpretable SeQuence) indicates that the sequencer program does not respect its context conditions. This means, there is non-linear use of vectors, or there are partial "Match Begin" or "Match End" sequences (for example a WTER without its MBGN, a MJPE without its MEND - see the SQPG command). The label is no longer displayable by the Vector Setup in this case. No frst_used_vec parameter is returned when the parameter cmd_No is NISQ.

### Example（取自子主题 Vector Setup Commands › List of vector setup commands › VPAR  -  Vectors in PARallel）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,504,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,10,,,(@)
< SQPG 3,RPTV,6,5,,(@)
< SQPG 4,STOP,,,,(@)
> VPAR? 0,15
< VPAR 0,0
< VPAR 1,0
< VPAR 2,0
< VPAR 3,10
```

This example displays the sequencer instructions of the selected label before calling VPAR? in order to make its reply understandable.

### Examples（取自子主题 AC Testing Commands › Concepts of AC test functions › Using embedded timing and level search on a Smart Scale system）

### Binary search for the left boundary

The following example shows a binary search for the left boundary (FAIL/PASS transition) with a minimal pass count of 5 (a dot denotes PASS):

 !`Embedded timing search`（raw: `../../../../raw/124091.png`）

Note the following points in the graphic:

- It is to be understood that the largest PASS area of the linear search starts with the dot in the Linear Search line.
- To make the graphic more perspicuous, it is assumed that every transition occurs at a multiple of the binary search resolution.
- The required 5 consecutive PASS values are found after three additional steps.

### Level search

In general, the embedded level search works according to the same principles as the timing search. In particular, you can also restrict the level search to individual pins. The firmware commands and test method APIs with which the search is configured and executed are also the same for both level and timing search.

Note that a positive step width means that the level is increased, and a negative step width that it is diminished.

You can combine level searches with timing searches, but not on the same pin at the same time: If you define, for example, first a level search for a pin with TOCF, and then a timing search for the same pin, the timing search configuration will overwrite the level configuration.

### CYRM（取自子主题 AC Testing Commands › List of AC test function commands › CYRM  CYRM  -  CYcle Resolution Mode）

```
CYRM {resolution_mode}, [error_limit], {(pinlist)}
```

### CYRM?（取自子主题 AC Testing Commands › List of AC test function commands › CYRM  CYRM  -  CYcle Resolution Mode）

```
CYRM? {(pinlist)}
```

returns:

```
CYRM {resolution_mode},[error_limit], {(pinlist)}
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › CYRM  CYRM  -  CYcle Resolution Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98515_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：resolution_mode | Defines the resolution mode. This can be:
> 表内引用（1 条，供检索）：`Retrieving edge information by repeating the test`（raw: `02.06.11.01.02.02.01_Retrieving_edge_information_by_repeating_the_test.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › CYRM  CYRM  -  CYcle Resolution Mode）

```
CYRM CYCL,,(@)
CYRM CYCL,,(MatchLoopPin)
```

### DPSR（取自子主题 AC Testing Commands › List of AC test function commands › DPSR  DPSR  -  Define Parallel SeaRch）

```
DPSR {set_nr}, ["exec_context",] [(setup_pinlist)|(primary_port)], [(result_pinlist)], [wait_time,] [search_type], [max_err_count,] {#spec(data)}
```

### DPSR?（取自子主题 AC Testing Commands › List of AC test function commands › DPSR  DPSR  -  Define Parallel SeaRch）

```
DPSR? {set_nr} [, (setup_pinlist)]
```

returns:

```
DPSR {set_nr}, ["exec_context",] (setup_pinlist), (result_pinlist), [wait_time,] search_type, [max_err_count], {#spec(data)}
```

Extra parameters exec_context and wait_time are returned only if they have been defined by DPSR.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98574_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：25 行 × 4 列。
> 首行（上游原文）：set_nr | The mandatory parameter specifies the number of the search set in which the condition is to be stored. The maximum number is 128. If a search set with …

### Example（取自子主题 AC Testing Commands › List of AC test function commands › DPSR  DPSR  -  Define Parallel SeaRch）

```
> PSFC ALL
> DPSR 3,,,FUNC,#219,TIM,"f",B,30,130,,
> PSFC 2
> DPSR 3,(IN1),,FUNC,#220,TIM,"del",B,0,110,,
> PQFC 1
> DPSR? 3,(@)
< DPSR 3,(@),(@),FUNC,#9000000019,TIM,"f",B,30,130,,
> PQFC 2
> DPSR? 3,(@)
< DPSR 3,(OUT1),(@),FUNC,#9000000019,TIM,"f",B,30,130,,
< DPSR 3,(IN1),(@),FUNC,#9000000020,TIM,"del",B,0,110,,
```

This example illustrates:

- How the same search can be defined differently for different sites.
- How an existing condition is partially overwritten when a new condition is partially inconsistent with it.

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › DRLS  -  DRive Level Sensitivity）

```
DRLS? {test}, {pass_value}, [limit], {(pinlist)}
```

returns:

```
DRLS {value_specifier}, {result_value}
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › DRLS  -  DRive Level Sensitivity）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98576_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 3 列。
> 首行（上游原文）：test | This parameter is one of the following:
> 表内引用（2 条，供检索）：`DRLV, DRLV? - (DRive LeVel)`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`） · `DRLV, DRLV? - (DRive LeVel`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`）

### Example 1（取自子主题 AC Testing Commands › List of AC test function commands › DRLS  -  DRive Level Sensitivity）

```
DRLS? H,5000,,(Q0_1)
```

returns:

```
DRLS P,5000
```

### Example 2（取自子主题 AC Testing Commands › List of AC test function commands › DRLS  -  DRive Level Sensitivity）

```
DRLS? H,5000,-1000,(Q0_1)
```

returns:

```
DRLS EQ,-490
```

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › EDDC  -  EDge in Device Cycle）

```
EDDC? [waveform_set], [timing_set], {edge_spec},
[dev_cyc_name], [dc_ref], [direction], {(pinlist)}
```

returns:

```
EDDC {edge_number}, {dev_cyc_name}, [reuse_flag], {(pinlist)}
```

### EDSP（取自子主题 AC Testing Commands › List of AC test function commands › EDSP  EDSP  -  EDge SPecification）

The edge_spec parameter specifies a physical edge (d1 through d8 or r1 through r8):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}
```

The edge_spec parameter is a data parameter (D1, D2, C1, C2, E1, or E2):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}
```

### EDSP?（取自子主题 AC Testing Commands › List of AC test function commands › EDSP  EDSP  -  EDge SPecification）

```
EDSP? [dc_ref], {(pinlist)}
```

returns:

```
EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98589_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：waveform_set | Specifies a waveform set number for a fixed timing setup.

### ESGB（取自子主题 AC Testing Commands › List of AC test function commands › ESGB  ESGB  -  Edge Search GloBal）

```
ESGB [lin_step], [lin_bin_step], [min_pulse]
```

### ESGB（取自子主题 AC Testing Commands › List of AC test function commands › ESGB  ESGB  -  Edge Search GloBal）

```
ESGB?
```

returns:

```
ESGB [lin_step], [lin_bin_step], [min_pulse]
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › ESGB  ESGB  -  Edge Search GloBal）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98598_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：lin_step | The lin_step parameter defines the step width (in ns) to be used for the linear searches which can be initiated by the TTRS? query. Any negative numb…

### Example（取自子主题 AC Testing Commands › List of AC test function commands › ESGB  ESGB  -  Edge Search GloBal）

```
ESGB 20,30,0
```

This example defines a 20 ns step width for linear search and a 30 ns step width for the combined linear/binary search. The minimum allowed pulse width is 0 ns.

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › EXSR -  EXecute SeaRch）

```
EXSR{set_nr}
```

Parameter
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98602_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：set_nr | Specifies the number of the search set which is to be executed.

### Example（取自子主题 AC Testing Commands › List of AC test function commands › EXSR -  EXecute SeaRch）

```
> EXSR 1
> EXSR 2
```

Note that the results for search set 1 are still extant after execution of search set 2.

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › FTSM  FTSM  -  Functional Test Set Mask）

```
FTSM {mode}, [run_to], [mask_before], [mask_after][,(ref_port)]
FTSM?
FTSM?
```

returns:

```
FTSM CLEAR, , ,
```

or

```
FTSM SET, [run_to], [mask_before], [mask_after][,(ref_port)]
```

  Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98607_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：mode | Lets you set the mode of the FTSM command. The mode can be:

For a multi-port burst, this parameter specifies the reference port to which the cycle numbers of the run_to, mask_before, and mask_after parameters refer.

If you have set the run_to parameter, then the sequencers will be stopped for all ports after the reference port has completed the requested number of cycles. The mask_before, and mask_after parameters are only applied to the specified port. The other ports will not be masked,

Note that the reference port must belong to the current start label (as defined by SQSL).

   |  Application Used in the parametric functional test. Errors and warnings

An error is generated if:

- A value (run_to, mask_before, mask_after) is not in the valid range of [0... 2^48 - 2].
- The run_to and mask_before parameters are specified, and run_to is equal or bigger than mask_before.
- The run_to and the mask_after parameters are specified, and run_to is bigger than mask_after.

A warning is generated if:

- The run_to parameter and the mask_before parameter are specified and run_to < mask_before. In this case the pattern executed will always pass as all cycles executed are masked out for result evaluation.
- The run_to parameter and the mask_after parameter are specified and run_to <= mask_after. In this case the entry for the mask_after parameter can be omitted as the sequencer will not even execute the cycles that are masked out.

### Example（取自子主题 AC Testing Commands › List of AC test function commands › FTSM  FTSM  -  Functional Test Set Mask）

```
FTSM?
```

returns:

```
FTSM CLEAR, , ,
FTSM SET, ,10,20
```

The FTSM? query returns the current FTSM settings.

The FTSM SET command masks all cycles except for those in the range from cycle 10 to cycle 20.

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › FTST  -  Functional TeST）

```
FTST? ["exec_context"]
```

returns:

```
FTST {result_flag}
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › FTST  -  Functional TeST）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98608_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 6 列，含嵌套表。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98608_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：P | is returned if the functional test passes.

### Example（取自子主题 AC Testing Commands › List of AC test function commands › FTST  -  Functional TeST）

```
FTST?
```

returns:

```
FTST P
```

This example returns a pass result for the functional test.

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › RCLS  -  ReCeive Level Sensitivity）

```
RCLS? {test}, {pass_value}, [limit], {(pinlist)}
```

returns:

```
RCLS {value_specifier}, {result_value}
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › RCLS  -  ReCeive Level Sensitivity）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98716_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 4 列。
> 首行（上游原文）：test | This parameter is one of the following:

### Example（取自子主题 AC Testing Commands › List of AC test function commands › RCLS  -  ReCeive Level Sensitivity）

```
RCLS? H,3000,6000,(Q0)
```

returns:

```
RCLS EQ,5300
```

In this example a search was made to find the high level threshold between 3V and 6V. The pass/fail transition was located at 5.3V.

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › RSSR  -  Retrieve Spec Search Results）

```
RSSR? {set_nr},[(setup_pinlist)]
```

returns:

```
RSSR {set_nr},(search_result),[pass_value],[fail_value],(setup_pinlist)
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98724_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：set_nr | Specifies the number of the search set for which results are to be returned.

### Example（取自子主题 AC Testing Commands › List of AC test function commands › RSSR  -  Retrieve Spec Search Results）

```
> PQFC 2
> RSSR? 3,(@)
< RSSR 3,P,90.1,90.2,(OUT1)
< RSSR 3,P,33.1,33,(IN1)
```

In this example, RSSR? returns the results of all setup pins in search set 3 for site 2. For OUT1, a pass/fail transition was found, for IN1 a fail/pass transition.

### SHSP（取自子主题 AC Testing Commands › List of AC test function commands › SHSP  SHSP  -  SHmoo SPecs）

```
SHSP [spec_type_1], ["spec_name_1[@port[@UNCHANGED]]"], [(pinlist_1)], [spec_type_2], ["spec_name_2[@port[@UNCHANGED]]"], [(pinlist_2)]
```

### SHSP?（取自子主题 AC Testing Commands › List of AC test function commands › SHSP  SHSP  -  SHmoo SPecs）

```
SHSP?
```

returns:

```
SHSP [spec_type_1], ["spec_name_1"], [(pinlist_1)], [spec_type_2], ["spec_name_2"], [(pinlist_2)]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98732_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：spec_type_<number> | Which specification type to use. Use:
> 表内引用（1 条，供检索）：`DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example 1（取自子主题 AC Testing Commands › List of AC test function commands › SHSP  SHSP  -  SHmoo SPecs）

```
> SHSP LEV, "aclk_vil",(aclkout), LEV, "adata_vil", (adata3)
> SHSP?
< SHSP LEV, "aclk_vil",(aclkout), LEV, "adata_vil", (adata3)
```

### Example 2（取自子主题 AC Testing Commands › List of AC test function commands › SHSP  SHSP  -  SHmoo SPecs）

In the following Pin Scale example, both spec variables occur in the period definitions associated with the two ports:

```
> CLKR? "MP_spec",(Port1)
< CLKR "MP_spec",17,3.4,(Port1)
> PRPT? "MP_spec","shmsp@Port1";
< PRPT "MP_spec",(Port2)
> SHSP TIM, "shmsp@Port1",,TIM,"shmsp@Port2",
> SHVL 17,30
> PRPT? "MP_spec","shmsp@Port1"
< PRPT "MP_spec",(Port1)
> CLKR? "MP_spec",(Port1)
< CLKR "MP_spec",17,4.25,(Port1)
```

Since `shmsp` is used in the period definitions for both port `Port1` and `Port2`, the one that is specified first in the SHSP command will be used to derive the period resolution. Note that the primary port is only changed after issuing the SHVL command.

### SHVL（取自子主题 AC Testing Commands › List of AC test function commands › SHVL  SHVL  -  SHmoo spec VaLues）

```
SHVL [value_1], [value_2]
```

### SHVL?（取自子主题 AC Testing Commands › List of AC test function commands › SHVL  SHVL  -  SHmoo spec VaLues）

```
SHVL?
```

returns:

```
SHVL [value_1], [value_2]
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › SHVL  SHVL  -  SHmoo spec VaLues）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98733_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：value_1 | A double float defining the new value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647. Or use RSTO to restor…

### Example（取自子主题 AC Testing Commands › List of AC test function commands › SHVL  SHVL  -  SHmoo spec VaLues）

```
> SHSP TIM, "shmsp@Port1",, TIM, "shmsp@Port2",
> SHVL 2,3
> SHVL?
< SHVL 2,3
```

### SQGB（取自子主题 AC Testing Commands › List of AC test function commands › SQGB  SQGB  -  SeQuencer GloBal）

```
SQGB [mode], [analyze_delay][, (ref_port)]
```

### SQGB?（取自子主题 AC Testing Commands › List of AC test function commands › SQGB  SQGB  -  SeQuencer GloBal）

```
SQGB? [(portlist)]
```

returns:

```
SQGB {mode}, [analyze_delay][, (port)]
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › SQGB  SQGB  -  SeQuencer GloBal）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98746_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：mode | Possible values are:
> 表内引用（1 条，供检索）：`GETC? - (GET Cycles)`（raw: `02.06.02.02.131_GETC__-__GET_Cycles.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › SQGB  SQGB  -  SeQuencer GloBal）

```
> PCLK? "mu_burst",1,(@@)
< PCLK "mu_burst",1,20,(P1)
< PCLK "mu_burst",1,10,(P2)
> SPRM "mu_burst",1,,
> SQSL "mu_burst"
> SQGB STSQ,30,(P2)
> SQGB? (@@)
< SQGB STSQ,15,(P1)
< SQGB STSQ,30,(P2)
```

This example configures the sequencers to stop when port P2 has completed 30 cycles. Port P1, whose period length is twice the period length of P2, will be stopped after 15 cycles. Note that P1 and P2 must belong to the same sequencing group.

### SREC（取自子主题 AC Testing Commands › List of AC test function commands › SREC  SREC  -  Set RECeiver mask）

```
SREC {mask_value}, {(pinlist)}
```

### SREC?（取自子主题 AC Testing Commands › List of AC test function commands › SREC  SREC  -  Set RECeiver mask）

```
SREC? {(pinlist)}
```

Note Executing `SREC ACT,(@)` may cause excessive overhead. You can use the `UI_SUSPEND`（raw: `../02.07_Test_Method_Reference/02.07.04.01.260_UI_SUSPEND.md`） test method API to suspend updates of the graphical user interface.

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › SREC  SREC  -  Set RECeiver mask）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98754_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：mask_value | The mask value parameter specifies whether a pin mask will be applied:
> 表内引用（2 条，供检索）：`DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） · `DFGE, DFGE? - (DeFine Group Expressions)`（raw: `02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › SREC  SREC  -  Set RECeiver mask）

```
SREC X, (D1, D2, D3, D4)
```

This example masks the pins D1, D2, D3 and D4.

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › STRS  -  Spec TRansition Search）

```
STRS? ["exec_context",] [start], [stop], {mode}, [(pinlist)], {spec_type}, {"spec_name[@port[@UNCHANGED]]"}, [stepwidth], {resolution}
```

returns:

```
STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › STRS  -  Spec TRansition Search）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98762_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts .
> 表内引用（4 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） · `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`） · `Modifying the period for a search or shmoo in a multi-port setup`（raw: `02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › STRS  -  Spec TRansition Search）

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

### TOCF（取自子主题 AC Testing Commands › List of AC test function commands › TOCF  TOCF  -  Timing Level Offset search ConFiguration）

```
TOCF [search_type], {resource_type}, {start}, {number_of_steps}, {step_width}, {resolution}, [min_pass_count], [min_stable_error_count,] [histogram_step_width,] [transition_detection], [error_count_limit], [restore_flag], {(setup_pinlist)}
```

### TOCF?（取自子主题 AC Testing Commands › List of AC test function commands › TOCF  TOCF  -  Timing Level Offset search ConFiguration）

```
TOCF? {(pinlist)}
```

returns:

```
TOCF {search_type} {resource_type}, {start}, {number_of_steps}, {step_width}, {resolution}, {min_pass_count}, {min_stable_error_count}, {histogram_step_width}, {transition_detection}, {error_count_limit}, {restore_flag}, {(setup_pinlist)}
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › TOCF  TOCF  -  Timing Level Offset search ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124942_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：35 行 × 3 列。
> 首行（上游原文）：search_type | This parameter defines which value of the search result is to be stored as an offset to the edge positions of the current primary timing. Possible…
> 表内引用（1 条，供检索）：`Linear search modes`（raw: `02.06.09.01.02.01_Linear_search_modes.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › TOCF  TOCF  -  Timing Level Offset search ConFiguration）

```
TOCF EYE,R,1,100,1,0.1,5,PF,,NO,(Pin1)
```

This example appends a check for 5 consecutive pass results to the result of the binary search.

```
TOCF EYE,R,1,100,1,0.1,1,10,0.1,ECL,7,NO,(Pin1)
```

This example appends a histogram based search to the binary search. The histogram based search is terminated if the error count is stable for 10 consecutive search steps. A test is considered passed if the number of errors is smaller than 7.

### TOCR（取自子主题 AC Testing Commands › List of AC test function commands › TOCR  TOCR  -  Timing level Offset Configure Result pins）

```
TOCR [(result_pinlist)], {(setup_pin)}
```

### TOCR?（取自子主题 AC Testing Commands › List of AC test function commands › TOCR  TOCR  -  Timing level Offset Configure Result pins）

```
TOCR? {(result_pinlist)},
```

or

```
TOCR? , {(setup_pinlist)}
```

Both formats return:

```
TOCR {(result_pinlist)}, {(setup_pin)}
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › TOCR  TOCR  -  Timing level Offset Configure Result pins）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125396_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：result_pinlist | In the command, this parameter specifies the result pins for the setup pin specified with setup_pin. It can be omitted for O or IO setup pins. …

### Example（取自子主题 AC Testing Commands › List of AC test function commands › TOCR  TOCR  -  Timing level Offset Configure Result pins）

```
TOCR (Pin2,Pin3),(Pin1)
```

This example defines `Pin2` and `Pin3` as the result pins for `Pin1`.

```
> TOCR? ,(Pin1,Pin5)
< TOCR (Pin2,Pin3),(Pin1)
```

This example queries the result pins for Pin1 and Pin5. No reply is given for setup pin Pin5, because its result pin is also Pin5.

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › TORC -  Timing level Offset Result Copy）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125054_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：source_waveform_set | Number of the source waveform set. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed w…
> 表内引用（3 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `SPRM`（raw: `02.06.02.02.228_SPRM__SPRM__-__Set_PRiMary_sets.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › TORC -  Timing level Offset Result Copy）

Example 1: copies the offsets of timing set 2 of single port specification 102 to the primary timing set of the primary specification.

```
TORC 102,2,PRM,PRM,(Pin1,Pin2)
```

Example 2: copies all level_set offsets of level set 1 to all the other level sets for all pins (@).

```
> TORC 1,,ALL,,(@)
```

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › TORN  -  Timing level Offset search RuN）

```
TORN? {(pinlist)} [,"exec_context"]
```

Returns:

```
TORN {status}
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › TORN  -  Timing level Offset search RuN）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125309_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：pinlist | The pins for which the embedded search is to be executed. You can specify @ for all pins. Note the difference between a list of pins and @ in a multi-…
> 表内引用（1 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › TORN  -  Timing level Offset search RuN）

```
> TORN? (Pin1,Pin2)
< TORN SUCCEEDED
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › TORR  Timing level Offset Reset Result）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125545_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：waveform_set | Number of a waveform set. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. Th…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › TORR  Timing level Offset Reset Result）

```
TORR PRM,ALL,(Pin1)
```

This example resets the offsets for all timing sets of the current primary specification.

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › TORS  -  Timing level Offset ReSult）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125236_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 2 列。
> 首行（上游原文）：waveform_set | Number of a waveform set. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. Th…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › TORS  -  Timing level Offset ReSult）

```
> TORS? PRM,PRM,R,(p1)
< TORS 1,1,R,0,(p1)

> TORS? PRM,PRM,S,(p1)
< TORS 1,1,S,0,(p1)

> TORS? PRM,PRM,F,(p1)
< TORS 1,1,F,0,(p1)

> TORS? PRM,PRM,D,(p1)
< TORS 1,1,F,0,(p1)
< TORS 1,1,S,0,(p1)

> TORS? PRM,PRM,ALL,(p1)
< TORS 1,1,R,0,(p1)
< TORS 1,1,F,0,(p1)
< TORS 1,1,S,0,(p1)

> TORS? PRM,,VIL,(@)
<TORS 1,,VIL,750,(p1)
<TORS 1,,VIL,750,(p2)

> TORS? PRM,,VISWING,(@)
< TORS 1,,VIH,-450,(p1,p2)
< TORS 1,,VIL,450,(p1,p2)
```

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › TORT  -  Timing Level Offset search Result Transitions）

```
TORT? {(pinlist)}
```

returns:

```
TORT {left_boundary|NOT_FOUND}, {right_boundary|NOT_FOUND}, {(pinlist)}
```

Note The returned transition value is the latest passing value near to the transition.

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125234_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：left_boundary | The offet of the left boundary or lower level of the pass area found by the last timing or level search, where the fail-pass transition was foun…

### Example（取自子主题 AC Testing Commands › List of AC test function commands › TORT  -  Timing Level Offset search Result Transitions）

```
TORT? (@)
TORT NOT_FOUND,NOT_FOUND, (p1,p2)
```

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › TOUD -  Timing Offset UnDefine）

```
TOUD {(pinlist)}
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › TOUD -  Timing Offset UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125373_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pinlist | The pins for which the embedded timing search configuration is to be removed.

### Example（取自子主题 AC Testing Commands › List of AC test function commands › TOUD -  Timing Offset UnDefine）

```
TOUD (Pin1, Pin2)
```

### Syntax（取自子主题 AC Testing Commands › List of AC test function commands › TTRS  -  Time TRansition Search）

```
TTRS? {start}, {stop}, {search_type}, {(pinlist)}
```

returns:

```
TTRS {value_specifier}, [pass_value], [fail_value], {(pinlist)}
```

### Parameters（取自子主题 AC Testing Commands › List of AC test function commands › TTRS  -  Time TRansition Search）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98819_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 3 列。
> 首行（上游原文）：start | The start parameter defines the point in time (in ns), relative to the start of the cycle, where you want the search to begin.
> 表内引用（1 条，供检索）：`DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 AC Testing Commands › List of AC test function commands › TTRS  -  Time TRansition Search）

```
TTRS? 10,80,L,(Q0)
TTRS EQ,70,80,(Q0)
```

This example executes a global search test on pin Q0. A linear sweep takes place between 10 ns and 80 ns relative to the start of the period. The system returned a pass at 70 ns and a fail at 80 ns.

### Example（取自子主题 DC Measurement Commands › Concepts of DC measurement › DC measurements using a PPMU and a DC Scale DPS）

The graphic below illustrates the recommended setup. The MSET WAIT parameter extends the number of break vectors generated after executing the DC sub sequencer instructions.

The amount of required waiting time must be optimized manually. It depends on the application (settling time, capacitors) and on the type of DC operation.

 !`DC measurement using PPMU and DPS`（raw: `../../../../raw/134900.png`）

### Syntax（取自子主题 DC Measurement Commands › List of DC measurement commands › CSAS  -  Channel Slot Accumulated Status）

```
CSAS? [msMode,] {mask}, {(pinlist)}
```

returns:

```
CSAS {status}, {(pinlist)}

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/144688_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › CSAS  -  Channel Slot Accumulated Status）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/144688_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 4 列，含嵌套表。
> 首行（上游原文）：msMode | The extra parameter controls how the return value is created.The value of the parameter can be PQFC: PQFC specified: The current query focus is respect…


 | msMode  | The extra parameter controls how the return value is created.

The value of the parameter can be PQFC:

- PQFC specified: The current query focus is respected and allows status query per site without affecting status bits of other sites.
- PQFC not specified: The command reads (and clears) status bits of all enabled and active sites at a glance, ignoring the actual query focus.
The parameter applies only to use of parameter mask as integer value. |
 |

mask

   | Integer bit mask or ALL.

-

Integer bit mask: Integer value is used to mask out individual status bits. Each bit of mask is logically AND-ed with the corresponding bit of the DPS status. If one of the resulting bits is set, then F (Fail) is returned, otherwise P (Pass).

It is used to check for an error condition. All bit positions of the status flags that should be checked, must be set to 1 in mask. If one of the selected status bits is set, then CSAS? returns F.

- ALL: Hex value (hexadecimal representation of all status bits) is returned.
For setting the integer bit mask or interpreting a returned hex value, refer to the `status`（raw: `02.06.02.02.33_CSAS__-__Channel_Slot_Accumulated_Status.md#_144688__r_status`） parameter below. |
 |

pinlist

 |

Comma separated list of DPS128/64 or XPS256 pins. The @ character can be used to read the status for all DPS pins.

 |
 |

status

   | If mask is ALL, you need to translate the hex value (hexadecimal representation of the status bits) to its binary form as follows:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/144688_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：Bit 0: | High voltage or current of surge tracker exceeded

If mask is specified as an integer bit-mask:

- Pass: P
- Fail: F
 |

### Example 1:（取自子主题 DC Measurement Commands › List of DC measurement commands › CSAS  -  Channel Slot Accumulated Status）

```
CSAS? 3,(VCC)
```

returns either

```
CSAS P,(VCC)
```

or

```
CSAS F,(VCC)
```

The example uses the integer bitmask and checks whether a spike on the `VCC` pin exceeded the low or high limit.

- P = Pass

No spike occurred since the last CSAS? query.

- F = Fail

Either the low or high limit or both were exceeded.

### Example 2:（取自子主题 DC Measurement Commands › List of DC measurement commands › CSAS  -  Channel Slot Accumulated Status）

```
CSAS? ALL,(Vaux)
```

returns

```
CSAS #H10,(Vaux)
```

The example uses the ALL specifier and checks for an error condition on the `Vaux` pin.

- Bit 3 = 0

No "Measurement range change failed" error. All set current measurement range requests were successful.

- Bit 4 = 1

The "Clamp current correction failed". A high-accuracy clamp current correction for a DCVH setup with execution mode SER_HAC or PAR_HAC was not successful.

### CTXT（取自子主题 DC Measurement Commands › List of DC measurement commands › CTXT  CTXT  -  ConTeXT）

```
CTXT {action},{"name"}
```

### CTXT?（取自子主题 DC Measurement Commands › List of DC measurement commands › CTXT  CTXT  -  ConTeXT）

```
CTXT?ALL
```

returns:

```
CTXT {DEFINE},{"name"}
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › CTXT  CTXT  -  ConTeXT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98513_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：action | Specifies the action. Possible values are:

### Example（取自子主题 DC Measurement Commands › List of DC measurement commands › CTXT  CTXT  -  ConTeXT）

```
> CTXT? ALL
< CTXT DEFINE,"DEFAULT"
< CTXT DEFINE,"differential"
< CTXT DEFINE,"PdrvNPrcv"
```

### DDIC（取自子主题 DC Measurement Commands › List of DC measurement commands › DDIC  DDIC  -  Define DUT Interface Connection）

```
DDIC ["connectionSet",] {"circuitry_type"}, {(cp1,cp2)}
```

### DDIC?（取自子主题 DC Measurement Commands › List of DC measurement commands › DDIC  DDIC  -  Define DUT Interface Connection）

```
DDIC? {"circuitry_type"}
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › DDIC  DDIC  -  Define DUT Interface Connection）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106906_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 4 列。
> 首行（上游原文）：connectionSet | This parameter is currently not used. This extra string parameter adds the ability to define several pins containing the same DC Scale channel i…

### Example 1: Ganging（取自子主题 DC Measurement Commands › List of DC measurement commands › DDIC  DDIC  -  Define DUT Interface Connection）

```
DDIC CONN, (207GO,209GI)
DDIC? ALL
```

returns

```
DDIC CONN, (207GO,209GI)
```

### DFCT（取自子主题 DC Measurement Commands › List of DC measurement commands › DFCT -  DeFine Continuity Test）

```
DFCT {force_current}, {commutation_voltage}, {pass_volt_min}, {pass_volt_max}, {polarity}, {(pinlist)}
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › DFCT -  DeFine Continuity Test）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98542_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：force_current | The force_current parameter specifies the current (in [micro ]A) that the active load sources or sinks. The range is 0 to 35 mA for the Pin Scal…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98542_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：pass_volt_min | This parameter specifies (in mV) the minimum pass value of the test. It defines the low level threshold for the comparator during the measuremen…

This parameter specifies (in mV) the maximum pass value of the test. It defines the high level threshold for the comparator during the measurement.

   | Note If pass_volt_min > pass_volt_max, the two parameters are swapped around internally.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98542_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：polarity | The polarity is as follows:

### Example（取自子主题 DC Measurement Commands › List of DC measurement commands › DFCT -  DeFine Continuity Test）

```
DFCT 10000,1700,200,700,SPOL,(p1,p2,p3,p4)
CTST? GPF
```

This example sets up the parameters needed to execute a continuity test on pins `p1` to `p4`. The parameters are as follows:

-  Force current = 10 mA
-  Commutation voltage = 1.7 V
-  Voltage minimum pass value = 200 mV
-  Voltage maximum pass value = 700 mV
-  Single polarity measurement selected

The example also includes the CTST? (Continuity TeST) query used to execute the test.

### DPSE（取自子主题 DC Measurement Commands › List of DC measurement commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DPSE {setnr}, {(pinlist)}, {binary_data}
```

### DPSE?（取自子主题 DC Measurement Commands › List of DC measurement commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DPSE? {setnr}
```

returns:

```
DPSE {setnr}, {(pinlist)}, {binary_data}
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98572_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 4 列，含嵌套表。
> 首行（上游原文）：setnr | This number defines the set number for the measurement. The number must be an integer from 1 to 256. In the query, you can specify ALL to retrieve the d…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98572_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：24 行 × 2 列。
> 首行（上游原文）：0: Waveform template

If the first value is an '11', two values follow. They define the low/high P/F limits of a return (voltage-)drop measurement and are separated by a "," (comma). The values are given in the unit Volt [V]. The number of measurement points is 1.

This option can be selected only for the HC variant of `DC Scale DPS128`（raw: `../02.05_Test_Head_Cards/02.05.05.01_DC_Scale_DPS128_DPS64_cards.md`） channels and requires that the measurement is executed with the `PSIE`（raw: `02.06.02.02.192_PSIE_-__Power_Supply_Internal_trigger_Execute.md`） command.

### Example 1（取自子主题 DC Measurement Commands › List of DC measurement commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DPSE 1,(Vcc),#90000000170,0.1,0.2,0.2,0.3
```

This example defines a template which consists of 2 points (0.1, 0.2) and (0.2, 0.3). If the first measured value is in the range (0.1, 0.2) and the second value is in the range (0.2, 0.3), then the result will be a pass.

### Example 2（取自子主题 DC Measurement Commands › List of DC measurement commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DPSE 1,(Vcc),#90000000121,15,0.1,0.2
```

This example defines a template which is 15 points long and is constant.

### Example 3（取自子主题 DC Measurement Commands › List of DC measurement commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DFPS 11,pos,(Vcc)
DFPS 12,pos,(Vdd)
DPSE 1,(@),#10 <- Delete set 1
DPSE 1,(Vcc),#152,1,2 <- Vcc min=1A, max=2A
DPSE 1,(Vdd),#152,2,3 <- Vdd min=2A, max=3A
PSST ON <- Measurement requires connect state
PSIE 1,,,(@) <- Measure both pins in parallel
PSER? 1,pval
PSER 1,P,(Vcc),#9000000006,1.501 <- value within range
PSER 1,F,(Vdd),#9000000006,3.173 <- value outside range
PSER? 1,ppf
PSER 1,P,(Vcc),#9000000000
PSER 1,F,(Vdd),#9000000000
PSER? 1,gpf
PSER 1,F,(),#9000000000
```

This example performs a measurement with format 2 and PSIE for two different pins in parallel.

### Example 4（取自子主题 DC Measurement Commands › List of DC measurement commands › DPSE  DPSE  -  Define Power Supply External trigger measurement）

```
DFPS (10101),pos,(Vcc) <- DC Scale pin
DFPS (10102,10103),pos,(Vdd) <- DC Scale pin (Gang of two channels)
DPSE 1,(@),#10 <- Delete set 1
DPSE 1,(Vcc),#153,0.5,1.5 <- Vcc min=0.5A, max=1.5A
DPSE 1,(Vdd),#153,20,30 <- Vdd min=20A, max=30A
PSST ON <- Measurement requires connect state
PSIE 1,,,(@) <- Measure both pins in parallel
 Vcc: High Precision Mode is used
 Vdd: Only one channel of the gang is used
PSER? 1,pval
PSER 1,P,(Vcc),#9000000006,1.301 <- value within range
PSER 1,F,(Vdd),#9000000006,31.73 <- value outside range
PSER? 1,ppf
PSER 1,P,(Vcc),#9000000000
PSER 1,F,(Vdd),#9000000000
PSER? 1,gpf
PSER 1,F,(),#9000000000
```

This example performs a measurement with format 3 and PSIE for two different pins in parallel.

### Syntax（取自子主题 DC Measurement Commands › List of DC measurement commands › GNOS  -  GetNumberofOccupiedSets）

GNOS? {set_type}

returns:

GNOS {NumberOfOccupiedSets},{MaxNumberOfSets},{NrOfOccupiedMSetActions},{MaxNumberOfMSETActions}

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › GNOS  -  GetNumberofOccupiedSets）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/142091_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：set_type | Must be MSET

### Example（取自子主题 DC Measurement Commands › List of DC measurement commands › GNOS  -  GetNumberofOccupiedSets）

```
> DSCP 4096,16,256,32,32,12800,16,1,256,9
> GNOS? MSET
< GNOS MSET,1,3201,1,12800
```

Related firmware commands:

- Configure sets: `MSET`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md`）
- Execute sets: `MEAS`（raw: `02.06.02.02.160_MEAS_-__execute_a_MEASurement_set.md`）
- Obtain results: `PMUR?`（raw: `02.06.02.02.179_PMUR___retrieve_PPMU_result.md`）

Define the maximum number of sets

- `Technology file for a device`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md`）
- `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） (pmu_set parameter)

### Syntax（取自子主题 DC Measurement Commands › List of DC measurement commands › MEAS -  execute a MEASurement set）

```
MEAS {id_dc}, {id_mset}
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › MEAS -  execute a MEASurement set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98648_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：id_dc | The DC set identification number to be executed.

### Example（取自子主题 DC Measurement Commands › List of DC measurement commands › MEAS -  execute a MEASurement set）

```
MEAS 1,2
```

This example executes the measurement set 2 of the DC set 1.

See also an example in `MSET, MSET? - (definition of Measurement SET)`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md`）.

### MSET（取自子主题 DC Measurement Commands › List of DC measurement commands › MSET  MSET  -  definition of Measurement SET）

```
MSET {`id_dc`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_dc`）}, DC, {`id_mset`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_mset`）}, {`glob_act`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_glob_act`）}, `[par1`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_par1`）], `[par2`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_par2`）], {(`pinlist`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_pinlist`）)}
MSET {`id_dc`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_dc`）}, DC, {`id_mset`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_mset`）}, {`act`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_act`）}, {`id_act`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_act`）}, {`par2`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_par2`）}, {(`pinlist`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_pinlist`）)}
MSET {`id_dc`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_dc`）}, DC, {`id_mset`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_mset`）}, `VMUM`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__e_VMUM`）, {`id_act`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_id_act`）}, {`par2`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_par2`）},{`numOfSamples`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_numOfSamples`）},ADC`,[waveformSize`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_waveformSize`）]`,[samplePeriod`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_samplePeriod`）]{(`pinlist`（raw: `02.06.02.02.164_MSET__MSET__-__definition_of_Measurement_SET.md#_98657__r_pinlist`）)}
```

### MSET?（取自子主题 DC Measurement Commands › List of DC measurement commands › MSET  MSET  -  definition of Measurement SET）

```
MSET? {id_dc|ALL}, DC, {id_mset|ALL}, {(pinlist)}
```

returns

```
MSET {id_dc}, DC, {id_mset}, {act}, {par1}, {par2}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98657_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：53 行 × 3 列。
> 首行（上游原文）：id_dc | The DC set identification number. The number is an integer in the range 1 to 256. A DC set consists of up to 10 measurement sets. For the query, you can…
> 表内引用（2 条，供检索）：`1)`（raw: `#fntarg_1`） · `MEAS`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10.02_Sequencer_instructions.md#_99880__row_MEAS`）

### Example（取自子主题 DC Measurement Commands › List of DC measurement commands › MSET  MSET  -  definition of Measurement SET）

Setting up PPMUs:

```
MSET 1,DC,1,LEN,6,,(@)
MSET 1,DC,1,WAIT,,0,(@)
MSET 1,DC,1,ACT,,,(@)
MSET 1,DC,1,SEL,0,CURR,(p1)
MSET 1,DC,1,SEL,0,VOLT,(p2)
MSET 1,DC,1,IRNG,1,IRA,(p1)
MSET 1,DC,1,IRNG,1,90,(p2)
MSET 1,DC,1,UFOR,2,500,(p1)
MSET 1,DC,1,IFOR,2,-40,(p2)
MSET 1,DC,1,PMUL,3,-5,(p1)
MSET 1,DC,1,PMUL,3,3000,(p2)
MSET 1,DC,1,PMUH,4,5,(p1)
MSET 1,DC,1,PMUH,4,3000,(p2)
MSET 1,DC,1,ACTI,5,,(p1,p2)
```

On PS5000:

```
MSET? 3,DC,1,(dig1)
MSET 3,DC,1,LEN,7,,(@)
MSET 3,DC,1,WAIT,,0,(@)
MSET 3,DC,1,SWAIT,,0,(@)
MSET 3,DC,1,ACT,,,(dig1)
MSET 3,DC,1,SEL,0,CURR,(dig1)
MSET 3,DC,1,IRNG,1,10000,(dig1)
MSET 3,DC,1,UFOR,2,3300,(dig1)
MSET 3,DC,1,PMUL,3,-10,(dig1)
MSET 3,DC,1,PMUH,4,30,(dig1)
MSET 3,DC,1,ACTI,5,,(dig1)
MSET 3,DC,1,SYNC,6,,(dig1)
```

Setting up the relays:

```
MSET 1,DC,2,LEN,2,,(@)
MSET 1,DC,2,WAIT,,1.3,(@)
MSET 1,DC,2,ACT,,,(@)
MSET 1,DC,2,OPM,0,ON,(p1)
MSET 1,DC,2,PPMU,0,ON,(p2)
MSET 1,DC,2,ACTI,1,,(p1,p2)
```

Setting up the measurement mode:

```
MSET 1,DC,3,LEN,1,,(@)
MSET 1,DC,3,WAIT,,0,(@)
MSET 1,DC,3,ACT,,,(@)
MSET 1,DC,3,PMUM,0,I,(p1)
MSET 1,DC,3,PMUM,0,H,(p2)
```

This example illustrates the internal structure of a measurement set as well as the requirement to define different measurement sets for different tasks. Note that no ACTI action is required (or even permitted) for measurement set 3 which contains only the PMUM action.

To execute this example, use the MEAS command as shown below:

```
MEAS 1,1
MEAS 1,2
MEAS 1,3
```

These commands sequentially execute measurement sets 1, 2 and 3 of DC set 1.

To retrieve the result of this measurement, use the `PMUR?`（raw: `02.06.02.02.179_PMUR___retrieve_PPMU_result.md`） command as shown below:

```
PMUR? GPF,(@)
```

This command retrieves the global pass/fail result of all pins.

Defining a DC set for value measurement

```
MSET 2,DC,1,VMUM,0,I,1,ADC,4000,0.0004,(p1)
```

In this example, 4000 measurements will be taken with the sampling period 400 us on the pin p1.

### Syntax（取自子主题 DC Measurement Commands › List of DC measurement commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? [PRLT,] {spec},[averages,] {(pinlist)}
```

returns:

```
PDMM {spec},, [ident], {result}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98685_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：PRLT | The extra parameter controls how the measurement is performed.The value of the parameter can be: PRLT
> 表内引用（4 条，供检索）：`PRLT?`（raw: `02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.md`） · `DC Scale XPS256 card`（raw: `../02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.md`） · `DFPS, DFPS? - (DeFine Power Supply)`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） · `DFPN, DFPN? - (DeFine Pin Name)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）

### Example 1: Test of the site in query focus（取自子主题 DC Measurement Commands › List of DC measurement commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? Fo_Se, (@)
```

returns:

```
PDMM Fo_Se,,POS,P,(Vee)
PDMM Fo_Se,,NEG,P,(Vee)
```

This example checks that the force/sense connections on the DUT board are correctly wired for positive and negative lines. For the pin Vee the master channel and the slave channel show a pass for both lines.

### Example 2: Test of all active sites（取自子主题 DC Measurement Commands › List of DC measurement commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? PRLT, Fo_Se, (Vcc,Vee)
PRLT? ALL
```

returns:

```
PDMM Fo_Se,,POS,P,(Vcc)
PDMM Fo_Se,,NEG,P,(Vcc)
PDMM Fo_Se,,POS,P,(Vee)
PDMM Fo_Se,,NEG,P,(Vee)

PRLT ALL,"PF0P"
```

The returned pass/fail result of PRLT? presumes that four sites are defined and sites 1, 2, and 4 are active. Sites 1 and 4 have passed the test. Site 2 shows the result for an open force to sense connection.

### Example 3: Averaging（取自子主题 DC Measurement Commands › List of DC measurement commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? Fo_Se, 10, (@)
```

returns:

```
PDMM Fo_Se,,POS,P,(Vee)
PDMM Fo_Se,,NEG,P,(Vee)
```

The returned go/no-go results are built from the average of ten measurements to improve the stability of the measurement in noisy environments.

### Example 4: Ganging（取自子主题 DC Measurement Commands › List of DC measurement commands › PDMM  -  PDps Miscellaneous Measurement）

```
PDMM? Ma_Sl,32,(@)
```

  returns:

```
PDMM Ma_Sl,,POS,P,(Vee1)
PDMM Ma_Sl,,POS,P,(Vee2)

```

This example checks the master and slave connections for ganged pins with an average of 32 measurements to improve the stability of the measurements in noisy environments.

### Syntax（取自子主题 DC Measurement Commands › List of DC measurement commands › PMUR   retrieve PPMU result）

```
PMUR?{type}, [mode,] {(pinlist)}
```

returns

```
PMUR {judge}, [voltage], [current], {(pinlist)}
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › PMUR   retrieve PPMU result）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98687_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：type | Data type to be retrieved. The following specifiers can be set: VMUM: Returns the measurement value from the PPMU measurement (successive approximation) …

Target pin or pins to retrieve result

   | Note For the VAL type, either voltage or current will be returned depending on the measurement mode (I-force V-measure or V-force I-measure).

### Example 1（取自子主题 DC Measurement Commands › List of DC measurement commands › PMUR   retrieve PPMU result）

```
> PMUR? VAL,(p1,p2)
< PMUR P,,2,(p1)
< PMUR F,-2100,,(p2)
```

This example retrieves the measurement value of "p1" and "p2" for the site that has the query focus.

### Example 2（取自子主题 DC Measurement Commands › List of DC measurement commands › PMUR   retrieve PPMU result）

```
> PMUR? GPF,(@)
< PMUR P,,,()
```

In this example, PMUR? returns the global pass/fail result for all tested pins of the site that has the query focus.

### Syntax（取自子主题 DC Measurement Commands › List of DC measurement commands › PSAS  -  Power Supply Accumulated Status）

```
PSAS? [msMode ,] {mask}, {(pinlist)}
```

returns

```
PSAS {status}, {(pinlist)}

```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98691_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：20 行 × 5 列，含嵌套表。
> 首行（上游原文）：msMode | The extra parameter controls how the return value is created.The value of the parameter can be PQFC: PQFC specified: The current query focus is respect…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98691_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 3 列。
> 首行（上游原文）：Bit 0 (LSB): | Constant voltage
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98691_2.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：18 行 × 6 列。
> 首行（上游原文）：Bit | Flag | DPS128DPS64 | UHC4T | XPS256

### Description（取自子主题 DC Measurement Commands › List of DC measurement commands › PSAS  -  Power Supply Accumulated Status）

For the following examples (1 to 4), the assumed binary value of the status of the UHC4 pin Vcc is 10000110 (Voltage drop return, Unregulated, Constant Current).

### Example 1（取自子主题 DC Measurement Commands › List of DC measurement commands › PSAS  -  Power Supply Accumulated Status）

To get all flags:

```
PSAS? ALL,(Vcc)
```

returns

```
PSAS #86,(Vcc)
```

### Example 2（取自子主题 DC Measurement Commands › List of DC measurement commands › PSAS  -  Power Supply Accumulated Status）

To check if Unregulated (bit 2) is set:

```
PSAS? 4,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 3（取自子主题 DC Measurement Commands › List of DC measurement commands › PSAS  -  Power Supply Accumulated Status）

To check if Constant Current (bit 1) or Overpower (bit 4) is set:

```
PSAS? 18,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 4（取自子主题 DC Measurement Commands › List of DC measurement commands › PSAS  -  Power Supply Accumulated Status）

To check if Voltage Drop Force (bit 6) or DUT Board Disconnect (bit 8) is set:

```
PSAS? 320,(Vcc)
```

returns

```
PSAS P,(Vcc)
```

### Example 5（取自子主题 DC Measurement Commands › List of DC measurement commands › PSAS  -  Power Supply Accumulated Status）

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 2,(Vee)
```

This example for device pin Vee shows the DPS is working in constant current mode.

### Example 6（取自子主题 DC Measurement Commands › List of DC measurement commands › PSAS  -  Power Supply Accumulated Status）

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 64,(Vee)
```

This example for device pin Vee shows the DPS has hit the voltage drop force threshold.

### Syntax（取自子主题 DC Measurement Commands › List of DC measurement commands › PSEE -  Power Supply External trigger measurement Execute）

```
PSEE [setnr], [current_range], [samples], {(pinlist)}
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › PSEE -  Power Supply External trigger measurement Execute）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98696_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：setnr | The set number of the external trigger measurement. (The range is 1 to 256). When this parameter is specified the corresponding set must have already be…
> 表内引用（1 条，供检索）：`DPSE`（raw: `02.06.02.02.85_DPSE__DPSE__-__Define_Power_Supply_External_trigger_measurement.md`）

### Example（取自子主题 DC Measurement Commands › List of DC measurement commands › PSEE -  Power Supply External trigger measurement Execute）

```
DFPS 11,pos,(Vcc)
DFPS 12,pos,(Vdd)
DPSE 1,(@),#10          <- Delete set 1
DPSE 1,(Vcc),#150,1,2   <- Vcc min=1A, max=2A
DPSE 1,(Vdd),#150,2,3   <- Vdd min=2A, max=3A
PSST ON      <- Measurement requires connect state
PSEE 1,,,(@)   <- Measure both pins in parallel
PSER? 1,pval
PSER 1,P,(Vcc),#9000000006,1.501 <- value within range
PSER 1,F,(Vdd),#9000000006,3.173 <- value outside range
```

This example performs a measurement with format 2 and PSEE for two different pins in parallel.

### Syntax（取自子主题 DC Measurement Commands › List of DC measurement commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSER? [setnr], {mode}
```

returns:

```
PSER [setnr], [result], {(pinlist)}, {binary_data}
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › PSER  -  Power Supply External trigger measurement Read results）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98697_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：setnr | The set number of the external trigger measurement. (The range is 1 to 256). If this parameter is omitted, this command returns the result of previous e…
> 表内引用（1 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`）

### Example 1（取自子主题 DC Measurement Commands › List of DC measurement commands › PSER  -  Power Supply External trigger measurement Read results）

```
DPSE 1,(Vcc),#90000000170,0.1,0.2,0.2,0.3
DPSE 1,(Vdd),#90000000121,2,0.1,0.2
PSEE 1,,,()
```

### Example 2（取自子主题 DC Measurement Commands › List of DC measurement commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSER? 1,PVAL
PSER 1,P,(Vcc),#9000000010,0.15,0.25
PSER 1,F,(Vdd),#9000000010,0.3,0.3
```

### Example 3（取自子主题 DC Measurement Commands › List of DC measurement commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSER? 1,PPF
PSER 1,P,(Vcc),#9000000000
PSER 1,F,(Vdd),#9000000000
```

### Example 4（取自子主题 DC Measurement Commands › List of DC measurement commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSER? 1,GPF
PSER 1,F,(),#9000000000
PRLT? ALL // get multisite results
PRLT "FPP" // site 1 fail, sites 2 & 3 are pass
```

### Example 5（取自子主题 DC Measurement Commands › List of DC measurement commands › PSER  -  Power Supply External trigger measurement Read results）

```
PSEE, I_300mA, 32, (Vee)
PSER? ,PVAL
```

returns:

```
PSER,,(Vee),#90000000120,0001923451
```

### Example 6（取自子主题 DC Measurement Commands › List of DC measurement commands › PSER  -  Power Supply External trigger measurement Read results）

```
DPSE 1,(Vcc),#90000000096,0.1,0.2
PSIE 1,,all_sampler,,,(Vcc)
PSER? ,PVAL
```

returns:

```
PSER ,,(Vcc),#90000000190.15,0.25,0.35,0.45
```

### Syntax（取自子主题 DC Measurement Commands › List of DC measurement commands › PSIE -  Power Supply Internal trigger Execute）

PSIE [setnr], [current_range] [,{keep_range|"RSTO"}] [,{all_sampler|"CH_ALL"}] [,{primary_act|"NPRM"}], [samples] [,settl_time], {(pinlist)}

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › PSIE -  Power Supply Internal trigger Execute）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98699_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：setnr | The set number defined by the DPSE command. (The range is 1 to 256). This set contains the limits of the measurement point for pass/fail judgment. When …
> 表内引用（1 条，供检索）：`DPSE`（raw: `02.06.02.02.85_DPSE__DPSE__-__Define_Power_Supply_External_trigger_measurement.md`）

### Example（取自子主题 DC Measurement Commands › List of DC measurement commands › PSIE -  Power Supply Internal trigger Execute）

```
> DPSE 1,(Vcc),#90000000112,0.09,0.11
> PSIE 1,,,(Vcc)
> PSER? 1,PVAL
< PSER 1,F,(Vcc),#9000000006,0.155
```

In this example, the `DPSE`（raw: `02.06.02.02.85_DPSE__DPSE__-__Define_Power_Supply_External_trigger_measurement.md`） command specifies a current limit of 0.9 A to 0.11 A for Vcc. Then the PSIE command starts measurements for the measurement set 1. In this case, the pin name is ignored because the set number is specified with the first parameter. After the measurement, the `PSER`（raw: `02.06.02.02.190_PSER__-__Power_Supply_External_trigger_measurement_Read_results.md`） command retrieves the measurement value for Vcc. In this case, the 300 mA range that is determined by using the specified limit value, is automatically selected for the measurement.

### PSST（取自子主题 DC Measurement Commands › List of DC measurement commands › PSST  PSST  -  Power Supply STatus）

```
PSST {state} [, (pinlist)]
```

### PSST?（取自子主题 DC Measurement Commands › List of DC measurement commands › PSST  PSST  -  Power Supply STatus）

```
PSST?  [(pinlist)]
```

returns:

```
PSST {state} [, (pinlist)]
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › PSST  PSST  -  Power Supply STatus）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98710_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：state | The device power supply state:

### Example 1（取自子主题 DC Measurement Commands › List of DC measurement commands › PSST  PSST  -  Power Supply STatus）

```
PSST ON
```

This example turns the DPS on.

### Example 2（取自子主题 DC Measurement Commands › List of DC measurement commands › PSST  PSST  -  Power Supply STatus）

The following example shows the use of the PSST command in conjunction with multisite:

```
PSFC ALL ; PSST ON   # turn on all supplies of all sites

PSFC "01"              # focus on one site only of the dual-site

PSST OFF,(vcc)         # turn off vcc of one site only!
PQFC 1 ; PSST? (vcc)   # these last two commands return different
PQFC 2 ; PSST? (vcc)   # answers, since one site should have vcc
                       # connected, whereas the other site does not
```

### UHCM（取自子主题 DC Measurement Commands › List of DC measurement commands › UHCM  UHCM  -  Ultra High Current power supply Modes）

```
UHCM {`set_nr`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_set_nr`）}, `[time_to_alarm`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_time_to_alarm`）,] `[reserved_param`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_reserved_param`）], `[clamp_mode`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_clamp_mode`）], `[fast_preload`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_fast_preload`）],
         `[openLoopProtection`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_openLoopProtection`）,] `[force_drop`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_force_drop`）], `[return_drop`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_return_drop`）], `[pulldown`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pulldown`）,] {(`pinlist`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pinlist`）)}

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106910_2.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106910_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
```

### UHCM?（取自子主题 DC Measurement Commands › List of DC measurement commands › UHCM  UHCM  -  Ultra High Current power supply Modes）

```
UHCM? {`set_nr`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_set_nr`）}, {(`pinlist`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pinlist`）)}
```

returns:

```
UHCM {`set_nr`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_set_nr`）}, `[time_to_alarm`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_time_to_alarm`）,] `[reserved_param`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_reserved_param`）], `[clamp_mode`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_clamp_mode`）], `[fast_preload`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_fast_preload`）],
         `[openLoopProtection`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_openLoopProtection`）,] `[force_drop`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_force_drop`）], `[return_drop`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_return_drop`）], {`[pulldown`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pulldown`）], {(`pinlist`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md#_106910__r_pinlist`）)}
```

### Parameters（取自子主题 DC Measurement Commands › List of DC measurement commands › UHCM  UHCM  -  Ultra High Current power supply Modes）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106910_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ALL | Modifies all existing DPS sets.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/106910_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 8 列，含嵌套表。
> 首行（上游原文）：set_nr | The mandatory identification number of the DPS set which you want to modify: ALL | Modifies all existing DPS sets.

### Example（取自子主题 DC Measurement Commands › List of DC measurement commands › UHCM  UHCM  -  Ultra High Current power supply Modes）

```
UHCM PRM,,,,0.4,0.1,(Vee)
```

This example sets the voltage drop force to 0.4 V, and the voltage drop return to 0.1 V.

### Syntax（取自子主题 Test Result Commands › List of test result commands › CDCP  -  Cycle Device Cycle Parameter）

```
CDCP? {start_cycle}, {no_of_cycles}, {strt_disp}, {disp_length}, {(pinlist)}
```

returns:

```
CDCP {cycle}, {dev_cyc_name}, {dev_cyc_len}, {DD1}, {DD2}, {ED1}, {ED2}, {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › CDCP  -  Cycle Device Cycle Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98499_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle to be analyzed. The range of values for this parameter depends on the analysis mode: In the Start …

### Example（取自子主题 Test Result Commands › List of test result commands › CDCP  -  Cycle Device Cycle Parameter）

```
> CDCP? 0,8,0,8,(S0_1)
< CDCP 0,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 1,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 2,"DNRZ",1,F10,N,N,N,(S0_1)
< CDCP 3,"MYDC",2,F00,N,N,N,(S0_1)
< CDCP 5,"MYDC",2,F10,N,N,N,(S0_1)
< CDCP 7,"DNRZ",1,F10,N,N,N,(S0_1)
> CDCP? 2,6,4,2,(S0_1)
< CDCP 5,"MYDC",2,F10,N,N,N,(S0_1)
< CDCP 7,"DNRZ",1,F10,N,N,N,(S0_1)
```

In the second call of CDCP? (the first call just serves to display the underlying situation) the range of interest starts at vector 6. Note that the reply starts with vector 5, and that the first occurrence of MYDC, which lies between vector 2 and vector 6, is not displayed.

### Syntax（取自子主题 Test Result Commands › List of test result commands › CHER  -  CHeck ERrors）

```
CHER? [MUX,] {(pinlist)}
```

returns:

```
CHER {res_flag}, [MUX,] {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › CHER  -  CHeck ERrors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98500_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：MUX | If this flag is set, and one of the specified (Pin Scale) pins is multiplexed to an HXA pin, then the result returned for this Pin Scale pin will be combi…

### Example（取自子主题 Test Result Commands › List of test result commands › CHER  -  CHeck ERrors）

After a functional test has been performed, sending CHER? returns the result for each pin in pinlist.

```
CHER? (@)
```

returns:

```
CHER F,(Q0,Q1)
CHER P,(Q2)
CHER F,(Q3)
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › CHFA  -  CHannel FAil flag）

```
CHFA? [MUX,] {(pinlist)}
```

returns:

```
CHFA {res_flag}, [MUX,] {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › CHFA  -  CHannel FAil flag）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98501_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：MUX | If this flag is set, and one of the specified (Pin Scale) pins is multiplexed to an HXA pin, then the combined result from all Pin Scale pins multiplexed …

### Example（取自子主题 Test Result Commands › List of test result commands › CHFA  -  CHannel FAil flag）

```
CHFA? (D1)
```

returns:

```
CHFA F, (D1)
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › CYCI  -  get CYCle Information）

CYCI? {start_cycle}, {no_of_cycles}, {resolution_mode} [,MUX] [,(port)]

returns:

CYCI {cycle}, [res_mode] [, (port)], {vector_number}, [label], [type], [seq_status], [comment], [no_of_waveforms] [,MUX], {#spec(data)}

### Parameters（取自子主题 Test Result Commands › List of test result commands › CYCI  -  get CYCle Information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99098_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：73 行 × 8 列。
> 首行（上游原文）：start_cycle | The start cycle is an integer that defines the first cycle to be reported. The start cycle is in the range 0 to 248 when the sequencer runs in the…

### Example（取自子主题 Test Result Commands › List of test result commands › CYCI  -  get CYCle Information）

CYCI? 20,2,CYCL

returns:

CYCI 20,11,"TEST1",SVEC,RPTV,"comment",1,

#9000000046

 dvc_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x04\x99

 dvc_02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x0F\x0F\x00

CYCI 21,12,"TEST1",SVEC,GENV,,1,

#9000000046

 dvc_03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x04\x05\x0F\x6C

 dvc_04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x04\x0F\x0F\x0D

This example returns result information (on the cycle level) for 2 cycles and 2 output pins of the label `TEST1`, which is of type SVEC. The first cycle was generated by a RPTV instruction from logical vector 11 and has an associated comment, the second cycle was generated by a GENV instruction for logical vector 12.

The binary data reports the device cycle names, which in this example are different for each pin and cycle. The waveform offsets are zero. The reported drive/expected/received data are:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/99098_2.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：dvc_01: | DD1 = F00, DD2 = F10, ED1 = FX, ED2 = F0 error: high received on edge 3 (param E2)

### CYRM（取自子主题 Test Result Commands › List of test result commands › CYRM  CYRM  -  CYcle Resolution Mode）

```
CYRM {resolution_mode}, [error_limit], {(pinlist)}
```

### CYRM?（取自子主题 Test Result Commands › List of test result commands › CYRM  CYRM  -  CYcle Resolution Mode）

```
CYRM? {(pinlist)}
```

returns:

```
CYRM {resolution_mode},[error_limit], {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › CYRM  CYRM  -  CYcle Resolution Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98515_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：resolution_mode | Defines the resolution mode. This can be:
> 表内引用（1 条，供检索）：`Retrieving edge information by repeating the test`（raw: `02.06.11.01.02.02.01_Retrieving_edge_information_by_repeating_the_test.md`）

### Example（取自子主题 Test Result Commands › List of test result commands › CYRM  CYRM  -  CYcle Resolution Mode）

```
CYRM CYCL,,(@)
CYRM CYCL,,(MatchLoopPin)
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › CYRP  -  CYcle Resolution Parameter）

```
CYRP [recovery],[shots]
CYRP?
```

returns:

```
CYRP {recovery},{shots}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › CYRP  -  CYcle Resolution Parameter）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98516_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：recovery | Specifies whether the test is repeated with all receive edges enabled after the last fine granularity shot. This serves to reset the hardware registe…

### Example（取自子主题 Test Result Commands › List of test result commands › CYRP  -  CYcle Resolution Parameter）

```
CYRP NRCR,ONE
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › CYRS  -  CYcle Resolution State）

```
CYRS? {(pinlist)}
CYRS {result_state}, {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › CYRS  -  CYcle Resolution State）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98517_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：result_state | Specifies the result state of the selected pins. Possible values are:

### Example（取自子主题 Test Result Commands › List of test result commands › CYRS  -  CYcle Resolution State）

```
CYRS? (Out1,Out2)
CYRS CYCL,(Out1,Out2)
```

### DCEL（取自子主题 Test Result Commands › List of test result commands › DCEL  DCEL  -  Digital Compare Exception List）

```
DCEL {DCRT}, {TP}, {action}, {(pinlist)}
```

### DCEL?（取自子主题 Test Result Commands › List of test result commands › DCEL  DCEL  -  Digital Compare Exception List）

```
DCEL? {DCRT}, {parameter}, {(pinlist)}
```

returns:

```
DCEL? {DCRT}, {parameter}, {action}, {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › DCEL  DCEL  -  Digital Compare Exception List）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/128210_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 3 列。
> 首行（上游原文）：DCRT | The command for which an exception list is to be created. Currently, DCRT is the only allowed command.

### Example（取自子主题 Test Result Commands › List of test result commands › DCEL  DCEL  -  Digital Compare Exception List）

```
> DCRT RAM,(portA)
> DFPT? (portA)
< DFPT (p1,p2,p3),(portA)
> DCEL DCRT,TP,(p2)
> DCEL? DCRT,TP,(portA)
< DCEL DCRT,TP,SET,(p2)
> DCEL DCRT,TP,(p1,p3)
> DCEL? DCRT,TP,(portA)
< DCEL DCRT,TP,SET,(p1,p2,p3)
> DCRT? (portA)
< DCRT RAM,(portA)
```

Note that you can add further pins to the exception list, and that the settings of DCRT are not changed even if all three pins of `portA` are in the exception list.

### DCGM（取自子主题 Test Result Commands › List of test result commands › DCGM  DCGM  -  Digital Compare Global Mode）

```
DCGM {acqu_mode},{emap_pos_int},{ovem_pos_int}
```

### DCGM?（取自子主题 Test Result Commands › List of test result commands › DCGM  DCGM  -  Digital Compare Global Mode）

```
DCGM? [answer_type] [,"exec_context"]
```

returns:

```
DCGM {acqu_mode},{emap_pos_int},{ovem_pos_int}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › DCGM  DCGM  -  Digital Compare Global Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98522_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 4 列。
> 首行（上游原文）：acqu_mode | Specifies the recording mode for the detailed Error Map. Possible values are:

### Example（取自子主题 Test Result Commands › List of test result commands › DCGM  DCGM  -  Digital Compare Global Mode）

```
DCGM FAIL,STRT,NONE
```

This example sets the error map into acquire failure mode and specifies that the error map position is to be interpreted as a start value for the detailed error map, and to be ignored for the overview error map.

### Syntax（取自子主题 Test Result Commands › List of test result commands › DCRM  DCRM  -  Digital Compare Result Mode）

DCRM

```
DCRM {map},{mode},[bits],["sub_cycles",] {(port_list)}
```

 DCRM?

```
DCRM? [answer_type,] {map},{(port_list)}
```

returns:

```
DCRM {map},{mode},[bits],[sub_cycles,] {(port)}


```

### Parameters（取自子主题 Test Result Commands › List of test result commands › DCRM  DCRM  -  Digital Compare Result Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98524_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 5 列。
> 首行（上游原文）：Received


> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98524_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：FCM | A fixed number of cycles is combined into one result. The number can be defined by a second call of DCRM, where the number is specified as the mode parame…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98524_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：22 行 × 10 列，含嵌套表。
> 首行（上游原文）：map | Specifies which error map will be configured. Possible values are:

### Example 1（取自子主题 Test Result Commands › List of test result commands › DCRM  DCRM  -  Digital Compare Result Mode）

```
DCRM EMAP,4,PF,"c1:1,3 c2:5,7 c3:2,4 c4:6,8",(P1,P2)
```

This example configures the detailed Error Map of port `P1` and `P2` to record 1 bit results for 4 sub-cycles, each of which combines two different edges.

### Example 2（取自子主题 Test Result Commands › List of test result commands › DCRM  DCRM  -  Digital Compare Result Mode）

```
DCRM EMAP,1,PFC,(P1,P2)
```

This example configures the Error Map to record one global detailed two bit result combining all edges of a cycle at every test execution.

### Example 3（取自子主题 Test Result Commands › List of test result commands › DCRM  DCRM  -  Digital Compare Result Mode）

```
DCRM OVEM,6000,,(@)
```

This example defines that 6000 cycles will be compressed into one Overview Error Map bit when the next test will be executed.

### DCRP（取自子主题 Test Result Commands › List of test result commands › DCRP  DCRP  -  Digital Compare Result Positioning）

```
DCRP {error_map_pos},{(ref_port)}
```

### DCRP?（取自子主题 Test Result Commands › List of test result commands › DCRP  DCRP  -  Digital Compare Result Positioning）

```
DCRP? [answer_type,]{(port_list)}
```

returns:

```
DCRP {error_map_pos},{(port)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › DCRP  DCRP  -  Digital Compare Result Positioning）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98525_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：error_map_pos | Specifies the start or stop position for Error Map recording. The interpretation of the value is determined by DCGM independently for both error…

### Example 1（取自子主题 Test Result Commands › List of test result commands › DCRP  DCRP  -  Digital Compare Result Positioning）

```
> PCLK? "mu_burst",1,(@@)
< PCLK "mu_burst",1,20,(P1)
< PCLK "mu_burst",1,10,(P2)
> DCGM ALL,STRT,NONE
> DCRP 20,(P2)
> DCRP? (@@)
< DCRP 10,(P1)
< DCRP 20,(P2)
```

This example illustrates the calculation of the cycle numbers for the ports that are not used as the reference port. For interpretation mode STRT, recording will start for the reference port `P2` with cycle 16 (largest multiple of 8 smaller than 20). Since the period length for `P1` is twice the period length of `P2`, recording for `P1` will start with cycle 8 (largest multiple of 8 smaller than 10).

### Example 2（取自子主题 Test Result Commands › List of test result commands › DCRP  DCRP  -  Digital Compare Result Positioning）

```
> SQGB STSQ,14,(P2)
> DCGM ALL,HALT,NONE
> DCRP 20,(P2)
> DCRP? (@@)
< DCRP 7,(P1)
< DCRP 14,(P2)
> SQGB STRD,
> DCRP? (@@)
< DCRP 10,(P1)
< DCRP 20,(P2)
```

This example shows that a definition of the Error Map position with DCRP is ignored when the sequencer mode is STSQ, but that it can subsequently be activated. Note that the DCGM command only serves to make the initial ineffectiveness of the definition visible. It is not possible to execute a functional test with these settings when the sequencer mode is STSQ.

### Syntax（取自子主题 Test Result Commands › List of test result commands › DCRS  -  Digital Compare Result Size）

```
DCRS? [answer_type,] {map},[mode],[bits],{(port_list)}
```

returns:

```
DCRS {map},{x-mode},{bits},{no_of_cycles},{(port)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98526_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 4 列。
> 首行（上游原文）：answer_type | This parameter specifies whether the current configuration or the configuration of the last executed test is to be returned. Possible values are:

### Example（取自子主题 Test Result Commands › List of test result commands › DCRS  -  Digital Compare Result Size）

```
> DCGM ALL,HALT,NONE
> DCRT TP,(P1)
> DCRM EMAP,8,PF,(P1)
> CYRM CYCL,,(P1)
> DCRS? EMAP,,,(P1)
< DCRS EMAP,8,PF,2048,(P1)
> DCRP 3360,(P1)
> FTST?
> EMAP? PPIN,1312,2048,EDGE,8,PF,ALL,BYTE,(P1)
```

This example shows how to get hold of the first cycles of your area of interest under the following conditions:

- The area of interest is greater than the capacity of the error map.
- The acquire mode is set to ALL with DCGM, so that the first recorded cycles will be overwritten when the error map is full before the end of the test.

The solution is to interpret the error map position defined with DCRP as a stop value (by setting the second parameter of DCGM to HALT), and to calculate the last cycle to be recorded as:

```
first_cycle_of_interest + capacity_of_the_Error_Map
```

In the example, the first addend is 1312. The second addend is determined with the DCRS? query.

### DCRT（取自子主题 Test Result Commands › List of test result commands › DCRT  DCRT  -  Digital Compare Result Target）

```
DCRT {target},{(port_list)}
```

### DCRT?（取自子主题 Test Result Commands › List of test result commands › DCRT  DCRT  -  Digital Compare Result Target）

```
DCRT? [answer_type,] {(port_list)}
```

returns:

```
DCRT {target},{(port)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › DCRT  DCRT  -  Digital Compare Result Target）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98527_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 4 列。
> 首行（上游原文）：target | Specifies the target area for the error map. Possible values are:

### Examples（取自子主题 Test Result Commands › List of test result commands › DCRT  DCRT  -  Digital Compare Result Target）

### Querying the location of the error map for all ports and setting it for specific ones (multi-port label)

This example queries the location of the error map for all ports. Then, it sets the location of the error map in the test processor for port `P2`, and in RDRAM for `P1`:

```
DCRT? (@@) // Note: this is equivalent to specifying DCRT? CONF,(@@)
DCRT RAM,(P1) // Set location of error map for port P1 in RDRAM
DCRT TP,(P2) // Set location of error map for port P2 in Test Processor
```

### Querying and setting the location of the result map for the default port (non multi-port label)

To query or set the location of the error map for the default port, you need to specify @ as the port_list of the DCRT? and DCRT commands, respectively:

```
DCRT? (@) // Query location of error map for the default port
DCRT TP,(@) // Set location of error map for the default port to Test Processor
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › EAEX  -  Edge Action EXpected data）

```
EAEX? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
EAEX {start_cycle}, {no_of_cycles}, {timing_set}, [err_type], {(pinlist)}, {#spec(data)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › EAEX  -  Edge Action EXpected data）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98581_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. The scanning method and the range of values this paramete…

### Example（取自子主题 Test Result Commands › List of test result commands › EAEX  -  Edge Action EXpected data）

```
EAEX? 0, 1, (pin1)
```

returns:

```
EAEX 0,1,3,,(pin1),#9000000010\x01\x04\x00\x0B\x01\x0A\x02\x19\x03\x1F\x0A
```

This example returns edge action drive and expected data (in hex notation) for one cycle. To decode the data, convert it into binary notation and use the lists above.

The data in binary format is:

```
0000 0001 0000 0100 0000 0000 0000 1011 0000 0001
0000 1010 0000 0010 0001 1001 0000 0011 0001 1111
```

The device cycle contains 1 waveform with 4 edge actions. The edge actions are RZ on the drive edges 1 and 2 and a window compare to intermediate on the receive edges 3 and 4.

### Syntax（取自子主题 Test Result Commands › List of test result commands › EARD  -  Edge Action Result Data）

```
EARD? {start_cycle}, {no_of_cycles}, {type}, [MUX,] {(pinlist)}
```

returns:

```
EARD {start_cycle}, {no_of_cycles}, {type}, [err_type], {(pinlist)}, [MUX,] {#spec(data)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › EARD  -  Edge Action Result Data）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98582_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：28 行 × 4 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. You can enter a value between 0 and 248.

### Example 1（取自子主题 Test Result Commands › List of test result commands › EARD  -  Edge Action Result Data）

```
> EARD? 2,1,BOTH,(TX1_d0)
< EARD 2,1,BOTH,PF,MUX,(TX1_d0),#9000000052
      \x10\x01\x00\x10
      \x00\x00\x82\x00\x01\x82\x00\x02\x82\x00\x03\x82\x00\x04\x82\x00\x05\x82\x00\x06\x82\x00\x07\x82
 \x00\x08\x82\x00\x09\x82\x00\x0a\x82\x00\x0b\x82\x00\x0c\x82\x00\x0d\x82\x00\x0e\x82\x00\x0f\x82
```

This example shows the results for a Pin Scale pin TX1_d0, which is multiplexed together with one other Pin Scale pin to an HXA pin. Since the MUX flag is set, the combined results of both these pins are returned in the reply.

Byte 0 indicates that TX1_d0 is one of two multiplexed Pin Scale pins, and that it has the logical position 0 in the multiplexing order. Byte 2 and 3 contain the information that the cycle contains 16 edges.

Byte A is the same for all edges and says that the edge is associated with a fixed value (not a data parameter), and that the waveform to which it belongs occupies position 0 in the device cycle. The edges of the two Pin Scale pins are interleaved according to the logical position in the multiplexing order. The edges of TX1_d0, which has position 0, are those with an even edge index (byte B), starting from 0. The edges of the other multiplexed Pin Scale pin (position 1) have an odd index. The actions (byte C) are also the same for all edges, namely an edge compare to 0 where expected = received value (that is, no error).

### Example 2（取自子主题 Test Result Commands › List of test result commands › EARD  -  Edge Action Result Data）

The EARD? answer will be split if the requested cycle range is greater than the available error map information, as shown below:

 !`Example`（raw: `../../../../raw/11910.png`）

```
> EARD? 0,15000, (pin1)
< EARD 0, 100, BOTH, NOER, (pin1), BinData        (a)
< EARD 100, 9900, BOTH, PF, (pin1), BinData       (b)
< EARD 10000, 5000, 1, NOER, (pin1), BinData      (c)
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › EARE  -  Edge Action REceived data）

```
EARE? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
EARE? {start_cycle}, {no_of_cycles}, {timing_set}, [err_type],{(pinlist)}, {#spec(data)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › EARE  -  Edge Action REceived data）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98583_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. You can enter a value between 0 and 248.
> 表内引用（1 条，供检索）：`VALD? - (VALid Data)`（raw: `02.06.02.02.316_VALD__-__VALid_Data.md`）

If reconstruction is not possible (code 110 on bits 2, 1, 0), there has been more than one edge or window compare within a single test system cycle.

If error bit 7 is set, an error has occurred on at least one of these edge or window compares.

### Example（取自子主题 Test Result Commands › List of test result commands › EARE  -  Edge Action REceived data）

```
EARE? 0, 1, (pin1)
```

returns:

```
EARE 0,1,3,ERON,(pin1),#9000000010\x01\x04\x00\x0B\x01\x0A\x02\x9A\x03\x9F\x0A
```

This example returns edge action drive and received data (in hex notation) for one cycle. To decode the data, convert it into binary notation and use the lists above.

The data in binary format is:

```
0000 0001 0000 0100 0000 0000 0000 1011 0000 0001
0000 1010 0000 0010 1001 1010 0000 0011 0001 1111
```

The device cycle contains 1 waveform with 4 edge actions. The edge actions are RZ on the drive edges 1 and 2 and a failing window compare (received value: 0) on the receive edges 3 and 4.

The EARE? answer will be split if the requested cycle range is greater than the available error map information, as shown below:

 !`Example`（raw: `../../../../raw/11910.png`）

```
EARE? 0,15000, (pin1)
EARE 0, 100, 1, NOER, (pin1), BinData (a)
EARE 100, 9900, 1, ERON, (pin1), BinData (b)
EARE 10000, 5000, 1, NOER, (pin1), BinData (c)
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › EDGE  -  EDGE errors）

```
EDGE? {(pinlist)}
```

returns:

```
EDGE {fail_string},{(pinlist)}
```

for each group of consecutive pins having the same result.

### Parameters（取自子主题 Test Result Commands › List of test result commands › EDGE  -  EDGE errors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98586_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：pinlist | The name of the pin or pins for which edge direction definitions are to be read back. This parameter can also include groups previously created by the…

### Example（取自子主题 Test Result Commands › List of test result commands › EDGE  -  EDGE errors）

```
> EDGE? (pin1, pin2, pin3, pin4)
< EDGE ...F.... (pin1,pin2)
< EDGE .F..F... (pin3)
< EDGE ..F..... (pin4)
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › EMAP  -  Error MAP）

```
EMAP? {pin_res},{start_cycle},{no_of_cycles},{resolution_mode},[results_per_cycle],[bits],{rep_mode},{results_align},[byte_max], [MUX,] {(pinlist)}
```

returns:

```
EMAP {pin_res},{start_cycle},{no_of_cycles},{resolution_mode},{results_per_cycle},{bits},{rep_mode},{results_align},[byte_max],{(pinlist)}, [MUX,] {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98590_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 3 列。
> 首行（上游原文）：pin_res | Specifies the pin granularity. Possible values are:

The binary data that are returned. The general format is:

Nn1n2...nNdata_stream

where the digit N defines the number of the digits ni (1 ≤i ≤N) that specify the length of data_stream in bytes.

The data stream itself consists of blocks each of which contains result data for every cycle (passed as well as failed) within a contiguous cycle range. Every block has a header that specifies

- the number of the first cycle of the block (8 bytes, big-endian encoded), and
- the block size in bytes (4 bytes, big-endian encoded).

The result data is also big-endian encoded.

If the rep_mode parameter has been set to ALL, only one block is returned, which contains the whole selected result range.

If rep_mode has been set to EOLY, then EMAP? will close a block after a failed cycle, and start a new block at the next failed cycle, if the passed cycles in-between occupy at least as much space as a block header (12 bytes). See the first example below.

If you are working with HXA pins note that the block size specifies bytes, not cycles. Thus, a block of size 32 contains 4 cycles of a HXA pin with 4 multiplexed Pin Scale pins.

 |

### Example 1（取自子主题 Test Result Commands › List of test result commands › EMAP  -  Error MAP）

```
> EMAP? COMB,0,42,EDGE,8,,EOLY,BYTE,,(dut_tx3)
< EMAP COMB,0,42,EDGE,8,PF,EOLY,BYTE,,(dut_tx3),#9000000038
  \x00\x00\x00\x00\x00\x00\x00\x0F
  \x00\x00\x00\x03
  \x03\x00\x80
  \x00\x00\x00\x00\x00\x00\x00\x1F
  \x00\x00\x00\x0B
  \x80\x00\x00\x80\xA0\x00\x80\xA0\x00\x00\x0A
```

This example shows the format of the binary data that is returned by EMAP?. The data stream has been broken up to make it more readable. Two data blocks are returned. The information is to be decoded as follows:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98590_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 6 列。
> 首行（上游原文）：Block | Start cycle | Number of cycles | Failing edges

For each cycle, all 8 edges are reported. The first block is closed because 13 passing cycles (= 13 bytes) lie between the failed cycle 17 and the next failed cycle 31.

### Example 2（取自子主题 Test Result Commands › List of test result commands › EMAP  -  Error MAP）

```
> FTST?
< FTST F
> EMAP? COMB,0,50000000,EDGE,8,PF,EOLY,BYTE,3500000,(O1,O2)
< EMAP COMB,0,12000000,EDGE,8,PF,EOLY,BYTE,EOB,(O1,O2),#90003500000
```

This example illustrates the use of the byte_max parameter. The test comprises 50 million cycles. The Error Map is located in the RDRAM. If the number of errors exceeds 0.5% of the cycles, that is, as soon as more than 250,000 errors have been found, the device is to be rejected offhand. Therefore, EMAP? is called with the EOLY option, so that only failed cycles are returned, and the maximum length of the reply is restricted to 3,500,000. This is based on the worst case assumption that every error occupies 13 bytes. The answer indicates that in fact more than 0.5% of the cycles have failed. Note that only 7% of the 50 million test cycles have to be uploaded to the system controller.

### Example 3（取自子主题 Test Result Commands › List of test result commands › EMAP  -  Error MAP）

The following example illustrates the difference between the resolution modes EDGE and SCYC.

```
> DCRM? EMAP,(@)
< DCRM EMAP,4,PFC,"c1:1 c2:2 c3:7 c4:8",(@)
> $EMAP? PPIN,0,12,EDGE,,PF,ALL,BYTE,,(out)
< EMAP PPIN,0,12,EDGE,8,PF,ALL,BYTE,,(out),#224
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00001100   11000011   10000011   00000000   00000000
     00000000   00000000   00000000   00000011   00000000   00000000   00000000   00000000

> $EMAP? PPIN,0,12,SCYC,,PF,ALL,BYTE,,(out)
< EMAP PPIN,0,12,SCYC,4,PF,ALL,BYTE,,(out),#224
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00001100   11110000   10110000   00000000   00000000
     00000000   00000000   00000000   00110000   00000000   00000000   00000000   00000000
```

The first failing cycle is cycle 0 (fifth byte in the second line of the EMAP? reply); in this cycle, edges 1,2,7,8 have failed. In addition, cycle 1 (edges 1,3,4) and 7 (edges 3,4) contain errors. With the PACK option, resolution mode SCYC compresses 12 bytes into 6:

```
> $EMAP? PPIN,0,12,SCYC,,PF,ALL,PACK,,(out)
< EMAP PPIN,0,12,SCYC,4,PF,ALL,PACK,,(out),#218
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00000110   11111011   00000000   00000000   00000011
     00000000   00000000
```

But the following call of EMAP? will produce an error message:

```
> $EMAP? PPIN,0,12,EDGE,4,PF,ALL,PACK,,(out)
```

The reason for this is that the results per cycle are only 4 bits long.

### Example 4（取自子主题 Test Result Commands › List of test result commands › EMAP  -  Error MAP）

The following example shows the expanded format for 2 bit error codes (2 bytes per cycle):

```
> DCRM? EMAP,(@)
< DCRM EMAP,4,PFC,"c1:1 c2:2 c3:3 c4:4",(@)
> $EMAP? PPIN,0,7,EDGE,,PFC,ALL,BYTE,,(out)
< EMAP PPIN,0,7,EDGE,8,PFC,ALL,BYTE,,(out),#228
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00001110   11110011   00000000   00001111   00000000
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00001100   00000000
```

In cycle 0, edges 1, 2, and 4 have failed. In cycle 1, edges 3 and 4 have failed. In cycle 6, edge 3 has failed.

```
> $EMAP? PPIN,0,7,EDGE,4,PFC,ALL,PACK,,(out)
< EMAP PPIN,0,7,EDGE,4,PFC,ALL,PACK,,(out),#220
     00000000   00000000   00000000   00000000   00000000   00000000   00000000   00000000
     00000000   00000000   00000000   00000111   11110011   00001111   00000000   00000000
     00000000   00000000   00001100
```

In this case, the PACK option is accepted because the initial segment of 4 two bit codes already makes up one byte.

### Syntax（取自子主题 Test Result Commands › List of test result commands › ERCC  -  ERror in Cycle range Count）

ERCC? {type}, {start_cycle}, {no_of_cycles}, [MUX,] {(pinlist)}

returns:

ERCC {type}, {start_cycle}, {no_of_cycles} [, granularity], {valid_code}, {no_of_errors}, [map_mode], [MUX,] {(pin)}

### Parameters（取自子主题 Test Result Commands › List of test result commands › ERCC  -  ERror in Cycle range Count）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98594_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 5 列。
> 首行（上游原文）：type | The type parameter can be:

### Example（取自子主题 Test Result Commands › List of test result commands › ERCC  -  ERror in Cycle range Count）

```
> ERCC? ERCP, 1000, 200, (pin1,pin2)
< ERCC ERCP, 1000, 200, VALD, 5, F160, (pin1)
< ERCC ERCP, 1000, 200, VALD, 1, F160, (pin2)
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › ERCT  -  ERror CounT）

```
ERCT? {type}, [MUX,] {(pinlist)}
```

returns:

```
ERCT {type}, {valid_code}, {no_of_errors}, [map_mode], [MUX,] {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › ERCT  -  ERror CounT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98595_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：type | The type parameter can be:

### Example（取自子主题 Test Result Commands › List of test result commands › ERCT  -  ERror CounT）

```
> ERCT? ERCP, (Q0)
< ERCT ERCP, VALD, 1, F160, (Q0)
```

This example requests the error count for pin Q0. The system returns one error, the error count is valid, the map mode is F160.

### Syntax（取自子主题 Test Result Commands › List of test result commands › ERCY  -  ERror CYcle）

```
ERCY? {type}, {start_cyc_no}, [no_of_cycles], [no_of_errors], {(pinlist)}
```

returns:

```
ERCY {type}, {cycle_no}, [window_len], [expected_data], [received_data], [data_type], {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98596_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：32 行 × 3 列。
> 首行（上游原文）：type | Selects the type of error data to be returned. The parameter can be:
> 表内引用（1 条，供检索）：`WAVE`（raw: `02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`）

### Example（取自子主题 Test Result Commands › List of test result commands › ERCY  -  ERror CYcle）

```
> ERCY? ALL,0,,2,(pin1,pin2)
< ERCY ALL,215,-2,F1,F0,E1,(pin1)
< ERCY ALL,240,,F0,FI,FIX,(pin1)
< ERCY ALL,17,,F0,F1,FIX,(pin2)
```

This example queries the system for the first two error cycles of pin1 and of pin2, starting from cycle 0. Expected and received data are also to be returned. The system returns the first two error cycles of pin1. For pin2 only one error cycle exists, therefore only one cycle can be returned.

There is an error on pin1 in cycle 215 which was a window compare 3 cycles long. The expected data was a 1, the receive data was a 0. The window compare was made to the E1 parameter.

There is an error on pin1 in cycle 240 which was an edge compare to a fixed state. The expected data was a 0, the received data was intermediate.

There is an error on pin2 in cycle 17 which was an edge compare to a fixed state. The expected data was 0, the received data was 1.

### Syntax（取自子主题 Test Result Commands › List of test result commands › ERMP  -  ERror MaP）

```
ERMP? {map_id}, {start_unit}, {no_of_units}, [map_mode],[edges,] [MUX,] {(pinlist)}
```

returns:

```
ERMP {map_id}, {start_unit}, {no_of_units}, {map_mode},[edges,] [MUX,] {(pinlist)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98597_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 8 列，含嵌套表。
> 首行（上游原文）：map_id | Determines the type of Error Map for which data is to be read out. Note that the allowed values depend on the settings of the DCRM command. Options tha…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98597_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 4 列。
> 首行（上游原文）：Expected Data | FAIL1 | FAIL2 | FAIL3

### Example（取自子主题 Test Result Commands › List of test result commands › ERMP  -  ERror MaP）

```
> ERMP? OVEM, 0, 16, F160,(Q0)
< ERMP OVEM,0,16,F160,(Q0),#9000000001 0x80
```

This example requests Overview Error Map data for the output pin Q0 in the Start Analysis mode between vectors 0 and 15.

```
> $ERMP? EDGE,0,7,F160,3,(Q0,Q7)
< ERMP EDGE,0,7,F160,3,(Q0,Q7),
  1100 0000  0000 0000  0010 0000  1100 0000  0000 0000  0000 0000 0000 0000
```

This example uses the "$" prefix, by which the binary data stream is represented bitwise by an ASCII "1" or "0" (see `Storing and Retrieving Binary Data`（raw: `02.06.01.03.04_Storing_and_Retrieving_Binary_Data.md`）). The call requests edge specific data for the output pins Q0, Q7. The first three receive edges of each of the first 7 cycles are queried. One byte is returned for every cycle. The result is that there are errors at edges 1 and 2 in cycle 0 and cycle 3, and an error at edge 3 in cycle 2. The other cycles contain no errors at the first three edges.

### Syntax（取自子主题 Test Result Commands › List of test result commands › FFCI  -  First Failed Cycle Information）

```
FFCI? {(no_ffcyc)} [,(port)]
```

returns:

```
FFCI {(no_ffcyc)}, {no_pins}, {#spec(data)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › FFCI  -  First Failed Cycle Information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98603_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：no_ffcyc | Number of first failed cycles to be reported.
> 表内引用（1 条，供检索）：`FFPM? (First Failing cycle information Pin Mapping)`（raw: `02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md`）

### Example 1: Firmware view（取自子主题 Test Result Commands › List of test result commands › FFCI  -  First Failed Cycle Information）

```
$FFCI? 2
FFCI 2,7,#218
  00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000011
  01100000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
  00010000 00010000
```

This example for `Firmware view`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.md`） queries the first two cycles where failures have occurred on an output pin of the default port, that is, on any configured output pin. Note: For the query, you must use the prefix $ so that the binary data are represented by ASCII 1 or 0.

The answer is to be interpreted as follows:

- `FFCI 2,7` means that 2 cycles are reported and 7 output pins are configured. Since this entails that one byte is sufficient for the pin data, the binary data needs only one byte for the pin data consists of 2 * 9 bytes.
- `#218` defines the size of the following binary data: 2 digits for the length specifier followed by the length specifier itself that indicates a length of 18 for the binary data.
- The Firmware view displays the cycle numbers and pin data as groups of eight bytes that must be evaluated as follows:

  - Failed cycle # 3:

    - The cycle number 3 is defined by the first eight address bytes `0000000` … `00000011`.
    - The 9th byte `01100000` shows failures on the 2nd and 3rd pin: Value 0 of the MSB on the left represents the passing 1st pin.

  - Failed cycle # 16:

    - The next eight bytes 10 …17 (`00000000` … `00010000`) define the cycle number 16.
    - The last byte 18 (`00010000`) shows that the fourth pin failed.

For the assignment from bits of the pin data bytes to the configured pins, refer to `#spec(data)`（raw: `02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md#_98603__r_specData`）, the `following example`（raw: `02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md#_98603__d_Example_2`） and to firmware command `FFPM? (First Failing cycle information Pin Mapping)`（raw: `02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md`）.

The FFCI? command can also be executed using API `FW_TASK`（raw: `../02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.md`）. You must use the syntax `FWTASK_STATUS FW_TASK(const STRING& command, FW_ResultData & resultdata);` to retrieve the binary data.

### Example 2: Sort order of pins（取自子主题 Test Result Commands › List of test result commands › FFCI  -  First Failed Cycle Information）

The pogo numbers of the following example setup are assigned in descending order to emphasize that the order of the pogo numbers and not the order of the definition by `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） matters.

```
DFPN 11105,"",(pinA)
DFPN 11104,"",(pinB)
DFPN 11103,"",(pinC)
DFPN 11102,"",(pinD)
DFPN 11101,"",(pinE)
CONF IO,F160,(pinA)
CONF I,F160,(pinB,pinC)
CONF O,F160,(pinD,pinE)
```

The FFCI? command will sort I / IO pins based on their pogo number defined for the first site resulting in the pin list pinE, pinD, pinA. The two pins pinB and pinC have no output capability and, therefore, will not be included in the FFCI? answer.

Assuming a test has been executed where pinA passes, but pinD and pinE fail for every cycle, the FFCI? answer for the first two failing cycles now would look like this:

```
FFCI? 2
FFCI 2,3,#218
  00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
  11000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
  00000001 11000000
```

 The binary data of the answer is to be interpreted as follows:

- Byte 1 …8: Address of the first cycle (`00000000` … `00000000` = 0)
- Byte 9: Pin data `11000000`
- Byte 10 …17: Address of the second cycle (`00000000` … `00000001` = 1)
- Byte 18: Pin data `11000000`

Byte 9 and 18 show that the first two pins on the left side (MSB) are failing. According to the sorting scheme that is defined in the FFCI parameter description for `#spec(data)`（raw: `02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md#_98603__r_specData`）, the failed pins are pinE (Channel 11101 and pinD (Channel 11102).

The `FFPM?`（raw: `02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.md`） firmware command will return `FFPM 3,(pinE,pinD,pinA)` as pinE, pinD and pinA are configured for the I / IO mode. The pin list is sorted by the pogo number defined for the first site.

### Syntax（取自子主题 Test Result Commands › List of test result commands › FFPM   First Failing cycle information Pin Mapping）

```
FFPM? [port]
```

returns:

```
FFPM {no_pins}, {Pinlist}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › FFPM   First Failing cycle information Pin Mapping）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/144138.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：port | Specifies the port for the pins for which information is to be returned. If you omit this parameter information will be returned for the default port @ t…
> 表内引用（2 条，供检索）：`FFCI`（raw: `02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md`） · `#spec(data)`（raw: `02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md#_98603__r_specData`）

### Example（取自子主题 Test Result Commands › List of test result commands › FFPM   First Failing cycle information Pin Mapping）

The pogo numbers of the following example setup are assigned in descending order to emphasize that the order of the pogo numbers and not the order of the definition by `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） matters.

```
DFPN 11105,"",(pinA)
DFPN 11104,"",(pinB)
DFPN 11103,"",(pinC)
DFPN 11102,"",(pinD)
DFPN 11101,"",(pinE)
CONF IO,F160,(pinA)
CONF I,F160,(pinB,pinC)
CONF O,F160,(pinD,pinE)
```

The FFCI? command will sort I / IO pins based on their pogo number defined for the first site resulting in the pin list pinE, pinD, pinA. The two pins pinB and pinC have no output capability and, therefore, will not be included in the FFCI? answer.

Assuming a test has been executed where pinA passes, but pinD and pinE fail for every cycle, the FFCI? answer for the first two failing cycles now would look like this:

```
FFCI? 2
FFCI 2,3,#218
  00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
  11000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
  00000001 11000000
```

 The binary data of the answer is to be interpreted as follows:

- Byte 1 …8: Address of the first cycle (`00000000` … `00000000` = 0)
- Byte 9: Pin data `11000000`
- Byte 10 …17: Address of the second cycle (`00000000` … `00000001` = 1)
- Byte 18: Pin data `11000000`

Byte 9 and 18 show that the first two pins on the left side (MSB) are failing. According to the sorting scheme that is defined in the FFCI parameter description for `#spec(data)`（raw: `02.06.02.02.122_FFCI__-__First_Failed_Cycle_Information.md#_98603__r_specData`）, the failed pins are pinE (Channel 11101 and pinD (Channel 11102).

For the configuration defined above, the `FFPM?` command will return the following data:

```
FFPM 3,(pinE,pinD,pinA)
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › FTST  -  Functional TeST）

```
FTST? ["exec_context"]
```

returns:

```
FTST {result_flag}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › FTST  -  Functional TeST）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98608_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 6 列，含嵌套表。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98608_3.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：P | is returned if the functional test passes.

### Example（取自子主题 Test Result Commands › List of test result commands › FTST  -  Functional TeST）

```
FTST?
```

returns:

```
FTST P
```

This example returns a pass result for the functional test.

### Syntax（取自子主题 Test Result Commands › List of test result commands › GETC  -  GET Cycles）

```
GETC? {(vector_no)}
```

returns:

```
GETC {(cycle_no)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98614_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：vector_no | The vector number for which you want to obtain the matching cycle number. vector_no must be a positive integer that does not exceed the maximum vect…

### Example（取自子主题 Test Result Commands › List of test result commands › GETC  -  GET Cycles）

```
> SQPG? ALL,(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,GENV,103,,,(@)
< SQPG 3,GENV,7,,,(@)
< SQPG 4,MACT,256,,,(@)
< SQPG 5,GENV,1,,,(@)
< SQPG 6,MRPT,1,,,(@)
< SQPG 7,RPTV,1544,100,,(@)
< SQPG 8,GENV,1,,,(@)
< SQPG 9,STOP,,,,(@)
> GETC? 112
< GETC 104
> GETC? 1656
< GETC 154504
```

In this example, the cycle numbers are calculated from the expected values. Vector 112 is the first vector after the match loop. The last 6 vectors before the match loop are not recorded in the Error Map, because the sequencers consider them to be part of the match loop (see `Counted match loops`（raw: `02.06.07.01.08.04.03.01_Counted_match_loops.md`）). The two match loop vectors proper are also not recorded in the Error Map. Since no other loop has occurred before vector 112, the cycle number corresponding to vector 112 is calculated as 112 - 8 = 104.

The cycle number of vector 1656, the last vector of the label, is calculated as 104 + 100 * 1544 = 154504.

The calculation is more complicated if it is based on the received data, because the last match loop cycles may be recorded in the Error Map (see again `Counted match loops`（raw: `02.06.07.01.08.04.03.01_Counted_match_loops.md`）).

### Syntax（取自子主题 Test Result Commands › List of test result commands › GETS  -  GET Sets）

```
GETS? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
GETS {start_cycle}, {no_of_cycles}, {timing_set}, {level_set}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98616_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：start_cycle | The start cycle is an integer that defines the first cycle to be reported. The start cycle is in the range 0 to 248 when the sequencer runs in the…

### Example（取自子主题 Test Result Commands › List of test result commands › GETS  -  GET Sets）

```
GETS? 0,2000,(Q0)
```

This example requests the timing and level set information for the first 2000 test cycles of pin `Q0`. The response may be as follows:

```
GETS 0,160,2,1,(Q0)
GETS 160,704,1,1,(Q0)
GETS 864,1136,2,1,(Q0)
```

The first 160 cycles were generated with timing set 2 and level set 1, the next 704 cycles with timing set 1 and level set 1, and the last 1136 cycles with timing set 2 and level set 1 again.

### Syntax（取自子主题 Test Result Commands › List of test result commands › GETV  -  GET Vectors）

```
GETV? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
GETV {start_cycle}, {no_of_cycles}, {start_vector}, {no_of_vectors}, {seq_status}, {"label"|"scan_template"}, [instance], {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › GETV  -  GET Vectors）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98617_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：23 行 × 5 列，含嵌套表。
> 首行（上游原文）：start_cycle | An integer that defines the first cycle to be reported. It is in the range 0 to 248 when the sequencer runs in the Start Analysis mode, or -248 to…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98617_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：sequencer instruction | reported as

### Example（取自子主题 Test Result Commands › List of test result commands › GETV  -  GET Vectors）

```
> GETV? 0,50,(S0_1)
< GETV 0,9,0,9,GENV,"test_1",,(S0_1)
< GETV 9,30,9,6,RPTV,"test_1",,(S0_1)
< GETV 39,1,-1,-1,BRK,"test_1",,(S0_1)
```

The vectors for cycles 9 through 38 were generated by an RPTV instruction that generated 6 waveforms 5 times.

### Syntax（取自子主题 Test Result Commands › List of test result commands › GETX  -  GET eXtended vector information）

```
GETX? [type], [label], [vector], [cycle], [index], {(pinlist)}
```

returns:

```
GETX {type}, {label}, {vector}, {cycle}, [index], {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › GETX  -  GET eXtended vector information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98618_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：12 行 × 3 列。
> 首行（上游原文）：type | The label type. You can supply one of the following options:

### Example（取自子主题 Test Result Commands › List of test result commands › GETX  -  GET eXtended vector information）

```
> GETX? ,,,4,,(CP)
< GETX MAIN,"multi",4,4,,(CP)
```

This example asks for vector data at cycle 4 on pin CP. The system replies that cycle 4 was generated by vector 4 in a main label called multi.

Note that this type of query where only a cycle number is supplied is similar to the GETV? query requesting information on just a single cycle - see `GETV? - (GET Vectors)`（raw: `02.06.02.02.135_GETV__-__GET_Vectors.md`）.

```
> GETX? MAIN,"multi",10,,,(CP)
< GETX MAIN,"multi",10,10,,(CP)
```

This example requests the number of the cycle that was generated by vector 10 in the main label called multi. The system replies with cycle 10.

### Syntax（取自子主题 Test Result Commands › List of test result commands › PASS  -  PASS or fail result）

```
PASS? {(pin_list)}
```

or

```
PASS? {(port_list)}
```

returns:

```
PASS {res_flag}, {(pin_list)}
```

or

```
PASS {res_flag}, {(port)}
```

respectively.

Note port_list mode returns the pass or fail result per port. This is different than the case when using pin_list mode.

To report the last test result per individual pin , the PPIN command is used.

### Syntax（取自子主题 Test Result Commands › List of test result commands › PASS  -  PASS or fail result）

```
PASS?PPIN,{(pins)}
```

returns

```
PASS PPIN,{res_flag}, {(pin}
```

Note The result (pass or fail) is returned for each pin specified in pins individually.

### Parameters（取自子主题 Test Result Commands › List of test result commands › PASS  -  PASS or fail result）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98681_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：pin_list | The last test result is provided for the pins specified in pin_list. If more than one pin list is included, the names must be separated by a comma. N…
> 表内引用（2 条，供检索）：`MEAS`（raw: `02.06.02.02.160_MEAS_-__execute_a_MEASurement_set.md`） · `SQPG`（raw: `02.06.02.02.237_SQPG__SQPG__-__SeQuencer_ProGramming.md`）

Application

Test results, see `Test Result Commands`（raw: `02.06.11_Test_Result_Commands.md`） and `Multi-Port Testing`（raw: `../../03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.01.02_General_Overview_of_Multi-Port_Testing__Cover.md`）.

### Example（取自子主题 Test Result Commands › List of test result commands › PASS  -  PASS or fail result）

After a functional test has been performed, sending PASS? returns one result for the whole test.

```
PASS? (@)
```

returns:

```
PASS P, (@)
```

or

```
PASS F, (@)
```

for a passed or a failed test result respectively.

### SQGB（取自子主题 Test Result Commands › List of test result commands › SQGB  SQGB  -  SeQuencer GloBal）

```
SQGB [mode], [analyze_delay][, (ref_port)]
```

### SQGB?（取自子主题 Test Result Commands › List of test result commands › SQGB  SQGB  -  SeQuencer GloBal）

```
SQGB? [(portlist)]
```

returns:

```
SQGB {mode}, [analyze_delay][, (port)]
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › SQGB  SQGB  -  SeQuencer GloBal）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98746_4.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：mode | Possible values are:
> 表内引用（1 条，供检索）：`GETC? - (GET Cycles)`（raw: `02.06.02.02.131_GETC__-__GET_Cycles.md`）

### Example（取自子主题 Test Result Commands › List of test result commands › SQGB  SQGB  -  SeQuencer GloBal）

```
> PCLK? "mu_burst",1,(@@)
< PCLK "mu_burst",1,20,(P1)
< PCLK "mu_burst",1,10,(P2)
> SPRM "mu_burst",1,,
> SQSL "mu_burst"
> SQGB STSQ,30,(P2)
> SQGB? (@@)
< SQGB STSQ,15,(P1)
< SQGB STSQ,30,(P2)
```

This example configures the sequencers to stop when port P2 has completed 30 cycles. Port P1, whose period length is twice the period length of P2, will be stopped after 15 cycles. Note that P1 and P2 must belong to the same sequencing group.

### SQIB（取自子主题 Test Result Commands › List of test result commands › SQIB  SQIB  -  SeQuencer Interrupt Behavior）

```
SQIB {BANDWIDTH|TIMEOUT}, {ERIM|ERRQ|FLIM|FLRQ}
```

### SQIB?（取自子主题 Test Result Commands › List of test result commands › SQIB  SQIB  -  SeQuencer Interrupt Behavior）

```
SQIB? {BANDWIDTH|TIMEOUT}
```

returns:

```
SQIB {BANDWIDTH|TIMEOUT}, {ERIM|ERRQ|FLIM|FLRQ}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › SQIB  SQIB  -  SeQuencer Interrupt Behavior）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/127771_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：BANDWIDTH | This refers to the behavior when the detailed error map is located in the external memory, and result recording was aborted due to a bandwidth overf…

### Example（取自子主题 Test Result Commands › List of test result commands › SQIB  SQIB  -  SeQuencer Interrupt Behavior）

```
SQIB BANDWIDTH FLrQ
```

This example suppresses all error messages in case of a recording abort.

### Syntax（取自子主题 Test Result Commands › List of test result commands › VALD  -  VALid Data）

```
VALD? {map_id}, {(pinlist)}
```

returns:

```
VALD {map_state}, {map_id}, {start}, {number}, {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › VALD  -  VALid Data）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98841_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：map_id | Determines the type of Error Map for which data is to be read out:
> 表内引用（3 条，供检索）：`FLBL`（raw: `02.06.02.02.123_FLBL__-__Failing_LaBeLs.md`） · `ERMP`（raw: `02.06.02.02.114_ERMP__-__ERror_MaP.md`） · `Pin Scale 5000 card`（raw: `../02.05_Test_Head_Cards/02.05.04.02_Pin_Scale_5000_card.md`）

### Example（取自子主题 Test Result Commands › List of test result commands › VALD  -  VALid Data）

```
VALD? ERRM, (Q0,Q1,Q2,Q3)
```

returns:

```
VALD CONS, ERRM, 0, 1024, (Q0,Q1,Q2,Q3)
```

This example queries the error map and returns data between the cycles of 0 and 1024. The error map data is consistent with the current setup.

### Syntax（取自子主题 Test Result Commands › List of test result commands › VALR  -  VALid Range）

```
VALR? {(pinlist)}
```

returns:

```
VALR {map_state}, {no_of_results}, {(pinlist)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › VALR  -  VALid Range）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/97185_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：map_state | Returns the current state of the error map. The state can be: INVL: Invalid - no error map details are available. (The setup has been changed, but n…

### Example（取自子主题 Test Result Commands › List of test result commands › VALR  -  VALid Range）

```
> VALR? (dpsPin)
< VALR CONS,10,(dpsPin)
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › VCYC  -  Valid CYCle）

```
VCYC? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
VCYC {start_cycle}, {no_of_cycles}, {seq_status}, {pin_oper_mode}, {(pinlist)}, {#spec(data)}
```

### Parameters（取自子主题 Test Result Commands › List of test result commands › VCYC  -  Valid CYCle）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98845_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：26 行 × 5 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. The scanning method and the range of values this paramete…

### Example（取自子主题 Test Result Commands › List of test result commands › VCYC  -  Valid CYCle）

```
VCYC? 0, 5, (pin1)
```

returns:

```
VCYC 0,5,GENV,F160,(pin1),#9000000005\x0E\x0E\x0E\x0F\x0D\x0A
```

This example returns the physical waveform DC/DC power units in hex notation in the range of 0 to 5 cycles.

### Syntax（取自子主题 Test Result Commands › List of test result commands › VNEC  -  Valid Number of Executed Cycles）

```
VNEC? {site_sel}, {value_format}, {(pin)}
```

Returns:

```
VNEC {site_sel}, {(pin)}, {value_data}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/344387_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：site_sel | Select sites. It can be a string of 1's and 0's; or "ALL" to specify all sites. The response is a string of 1's and 0's.

### Example（取自子主题 Test Result Commands › List of test result commands › VNEC  -  Valid Number of Executed Cycles）

```
VNEC? ALL, ASC, ("pin1")
```

Returns:

```
VNEC "11",("pin1"),#138,8
```

### Syntax（取自子主题 Test Result Commands › List of test result commands › VRCS  -  Valid ReConStruction）

```
VRCS? {reconstr_type}, [reconstr_cond,] {(pinlist)}
```

returns:

```
VRCS [reconstr_cond,] {reconstr_state}, [reconstr_oper,] {start_cycle}, {no_of_cycles}, {(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98861_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：18 行 × 3 列。
> 首行（上游原文）：reconstr_type | The reconstruction type determines how test cycles are counted.
> 表内引用（1 条，供检索）：`FLBL`（raw: `02.06.02.02.123_FLBL__-__Failing_LaBeLs.md`）

### Example（取自子主题 Test Result Commands › List of test result commands › VRCS  -  Valid ReConStruction）

```
VRCS? STRT, (@)
```

returns:

```
VRCS? REAL, 0, 437621, (@)
```

This example queries the number of reconstructed cycles, counting the cycles from the start of the test. The system replies that 437,621 cycles, starting from zero have been reconstructed, based on the last performed test.

### Syntax（取自子主题 Test Result Commands › List of test result commands › WFEX  -  WaveForm EXpected data）

```
WFEX? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
WFEX {start_cycle}, {no_of_cycles}, {timing_set}, [err_type], {(pinlist)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98873_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：39 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. The scanning method and the range of values this paramete…

### Example（取自子主题 Test Result Commands › List of test result commands › WFEX  -  WaveForm EXpected data）

```
WFEX? 0, 1, (pin1)
```

returns:

```
WFEX 0,1,3,NOER,(pin1),#9000000006\x0B\x0A\x1A\x1F\x00\x00\x0A
```

This example returns edge action drive and expected data (in binary notation) for one cycle. To decode the data, convert it into binary notation and use the lists above.

The data in binary format is:

```
0000 1011  0000 1010  0001 1010
0001 1111  0000 0000  0000 0000
```

The edge actions are RZ on the drive edges 1 and 2 and a window compare to 0 on the receive edges 3 and 4. Edges 5 and 6 are unused.

### Syntax（取自子主题 Test Result Commands › List of test result commands › WFRE  -  WaveForm REceived data）

```
WFRE? {start_cycle}, {no_of_cycles}, {(pinlist)}
```

returns:

```
WFRE {start_cycle}, {no_of_cycles}, {timing_set}, [err_type], {(pinlist)}, {#spec(data)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98874_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：41 行 × 3 列。
> 首行（上游原文）：start_cycle | This is an integer that defines the first cycle for which information is to be returned. The scanning method and the range of values this paramete…
> 表内引用（1 条，供检索）：`VALD? - (VALid Data)`（raw: `02.06.02.02.316_VALD__-__VALid_Data.md`）

If reconstruction is not possible (code 110 on bits 2, 1, 0), there has been more than one edge or window compare within a single test system cycle.

If error bit 7 is set, an error has occurred on at least one of these edge or window compares.

### Example（取自子主题 Test Result Commands › List of test result commands › WFRE  -  WaveForm REceived data）

```
WFRE? 0, 1, (pin1)
```

returns:

```
WFRE 0,1,3,ERON,(pin1),#9000000006\x0B\x0A\x9B\x9F\x00\x00\x0A
```

This example returns edge action drive and expected data (in binary notation) for one cycle. To decode the data, convert it into binary notation and use the lists above.

The data in binary format is:

```
0000 1011  0000 1010  1001 1011
1001 1111  0000 0000  0000 0000
```

The edge actions are RZ on the drive edges 1 and 2 and a failed window compare (received value: 1) on the receive edges 3 and 4. Edges 5 and 6 are unused.

The WFRE? answer will be split if the requested cycle range is greater than the available error map information, as shown below:

 !`Example`（raw: `../../../../raw/23378.png`）

```
WFRE? 0,15000, (pin1)
WFRE 0, 100, 1, NOER, (pin1), BinData           (a)
WFRE 100, 9900, 1, ERON, (pin1), BinData        (b)
WFRE 10000, 5000, 1, NOER, (pin1), BinData      (c)
```

### Example（取自子主题 Utility Line Commands › Accessing Utility Lines）

For an example see the `UPAS`（raw: `02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md`） command.

### DFUP（取自子主题 Utility Line Commands › List of utility line commands › DFUP  DFUP  -  DeFine Utility Purpose）

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### DFUP?（取自子主题 Utility Line Commands › List of utility line commands › DFUP  DFUP  -  DeFine Utility Purpose）

```
DFUP? {(purpose_name)}
```

returns

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › DFUP  DFUP  -  DeFine Utility Purpose）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98559_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ch_No_list | Utility line channel numbers to be defined as the members of a utility purpose and specified with five digits. The channels must be separated with …

### Example（取自子主题 Utility Line Commands › List of utility line commands › DFUP  DFUP  -  DeFine Utility Purpose）

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

This example defines a utility purpose AWG_CNCT and activates its standard settings.

The members and the setting values are as follows:

```
Member:      16501  16502  16503  16504
---------------------------------------
Setting:     0      1      1      0
```

### DFUT（取自子主题 Utility Line Commands › List of utility line commands › DFUT  DFUT  -  DeFine UTility line）

```
DFUT {ch_No}, {type}, {(util_name)}
```

### DFUT?（取自子主题 Utility Line Commands › List of utility line commands › DFUT  DFUT  -  DeFine UTility line）

```
DFUT? {(util_name)}
```

returns

```
DFUT {ch_No}, {type}, {(util_name)}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › DFUT  DFUT  -  DeFine UTility line）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98560_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ch_No | Channel number of the utility line specified with five or three digits. In the five‑digit format, the first three digits specify the utility pogo block.…

### Example（取自子主题 Utility Line Commands › List of utility line commands › DFUT  DFUT  -  DeFine UTility line）

```
DFUT 16504,w,(filter)
```

This example assigns the name `filter` and operating mode w to utility line 4 of the first utility pogo block.

### Syntax（取自子主题 Utility Line Commands › List of utility line commands › UDUP -  UnDefine Utility Purpose）

```
UDUP {(purpose_name)}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UDUP -  UnDefine Utility Purpose）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98830_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：purpose_name | Specifies the utility purpose name or names to be undefined. The symbol @ removes all utility purpose definitions. If more than one name is to be…

### Example（取自子主题 Utility Line Commands › List of utility line commands › UDUP -  UnDefine Utility Purpose）

```
UDUP (@)
```

This command undefines all defined utility purpose names.

### Syntax（取自子主题 Utility Line Commands › List of utility line commands › UDUT -  UnDefine UTility line）

```
UDUT {(util_name)}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UDUT -  UnDefine UTility line）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98831_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：util_name | Specifies the utility line name or names to be undefined. The symbol @ removes all utility line definitions. If more than one name is to be removed,…

### Example（取自子主题 Utility Line Commands › List of utility line commands › UDUT -  UnDefine UTility line）

```
UDUT (@)
```

This command undefines all defined utility line names.

### UPAS（取自子主题 Utility Line Commands › List of utility line commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

```
UPAS {site}, ["{setting}"], {(purpose_name)}
```

### UPAS?（取自子主题 Utility Line Commands › List of utility line commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

```
UPAS? {site}, {(purpose_name)}
```

returns:

```
UPAS {site}, "{setting}", {(purpose_name)}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98832_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：site | The site parameter is an integer that defines the number of the site where the channels are to be defined. The integer must be greater than 1. When speci…
> 表内引用（1 条，供检索）：`DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`）

### Example（取自子主题 Utility Line Commands › List of utility line commands › UPAS  UPAS  -  Utility Purpose ASsignment for multi-site）

```
> DFUP (101,102,103,104),"11XX",(AWG_CNCT)
> UPAS 2,"XX11",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "11XX", (AWG_CNCT)
> PSFC 2
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "XX11", (AWG_CNCT)
```

In this example, the `DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`） command defines a utility purpose AWG_CNCT and output states for site 1. The UPAS command defines the output states of AWG_CNCT for site 2. First the settings of site 1 are activated. Then the setup focus is restricted to site 2, and the output states for site 2 are activated.

### UPOW（取自子主题 Utility Line Commands › List of utility line commands › UPOW  UPOW  -  Utility POWer）

```
UPOW {mode} [, supply, (resourceID)]
```

### UPOW?（取自子主题 Utility Line Commands › List of utility line commands › UPOW  UPOW  -  Utility POWer）

```
UPOW? [supply, (resourceID)]
```

returns:

```
UPOW {state} [, supplyId, resourceID]
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UPOW  UPOW  -  Utility POWer）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/137170.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：mode | The mandatory parameter defines the new state of the supply. Available options of the parameter: ON: Switches the supply on OFF: Switches the supply off

The returned state of the queried supply.

 Possible values are:

- ON: The supply is switched on.
- OFF: The supply is switched off.
- TRIP: Returned in case of a power fail, for example: overcurrent or DUT board undocking.Note To switch on the supply again after such power fail events have occurred, you need to use `UPOW ON` followed by the extra parameters defining the supply and the resource.
   |  Some hints and restrictions for setting the extra supplyId and resourceID parameters:

- For compatibility with the `Internal utility power supply (V93000 systems)`（raw: `../02.03_DUT_board_design_reference/02.03.05.05_Internal_utility_power_supply__V93000_systems.md`）, the UP5V supply of the first Utility Card or the internal UP5V supply of the first card cage is always switched on. The supply can be programmed by this FW command but it has no effect on the hardware.
- For compatibility with PinScale and SmartScale systems, the `Utility power supply - XP pins (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.05.02_Utility_power_supply_-_XP_pins__V93000_EXA_Scale_systems.md`） of the first Utility Card can be programmed only using the short syntax `UPOW {state}` without the extra parameters defined. The supplyId parameter set to XPP5V, XPM5V, or XPP3V3 in combination with the resourceID parameter set to 1 is not supported.
- Independently switching the XPP5V, XPM5V, and XPP3V3 supplies is supported only for the second Utility Card with resourceID parameter set to 2.
- The supplyId parameter set to UDPS is supported only in combination with the resourceID parameter set to 1: Since, the second `optional Utility Card`（raw: `../02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md`） occupies all (legacy) DPS pogo blocks, the `Internal Utility Power Option`（raw: `../02.03_DUT_board_design_reference/02.03.05.04_Internal_Utility_Power_Option__V93000_EXA_Scale_systems.md`） cannot be used if a second Utility Card is installed.

### Example（取自子主题 Utility Line Commands › List of utility line commands › UPOW  UPOW  -  Utility POWer）

```
UPOW ON
```

Switches on the `Utility power supply - XP pins (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.05.02_Utility_power_supply_-_XP_pins__V93000_EXA_Scale_systems.md`） of the first Utility Card.

### UPST（取自子主题 Utility Line Commands › List of utility line commands › UPST  UPST  -  Utility Purpose STate）

```
UPST ["setting"], {(purpose_name)}
```

### UPST?（取自子主题 Utility Line Commands › List of utility line commands › UPST  UPST  -  Utility Purpose STate）

```
UPST? {(purpose_name)}
```

returns:

```
UPST "{setting}", {(purpose_name)}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UPST  UPST  -  Utility Purpose STate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98833_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：setting | The optional parameter specifies the status of the utility lines in the utility purpose. The status is determined with the following specifiers: 0: Se…

Name of the utility purpose to be set or read.

For the query, you can specify multiple names, which must be separated by a comma.

Specifying the symbol @ returns the definitions of all utility purposes.

   | Note All utility lines that are set with `UTST`（raw: `02.06.02.02.313_UTST__UTST__-__UTility_line_STate.md`） or UPST will be switched in parallel when the `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`） command is performed. If the `WSDN`（raw: `02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md`） command is used immediately after FLSH, the time span during which execution will pause equals the longest settling time that is defined for any of the switched utility lines (with `UTTI`（raw: `02.06.02.02.314_UTTI__UTTI__-__UTility_line_settling_TIme.md`）) or purposes (with `UPTI`（raw: `02.06.02.02.307_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md`）).

### Example（取自子主题 Utility Line Commands › List of utility line commands › UPST  UPST  -  Utility Purpose STate）

```
UPST ,(AWG_CNCT)
FLSH
WSDN
UPST? (AWG_CNCT)
```

returns

```
UPST "0110",(AWG_CNCT)
```

This example sets the utility purpose "AWG_CNCT" to the hardware, then reads the state of the utility purpose.

### UPTI（取自子主题 Utility Line Commands › List of utility line commands › UPTI  UPTI  -  Utility Purpose settling TIme）

```
UPTI {time}, {(purpose_name)}
```

### UPTI?（取自子主题 Utility Line Commands › List of utility line commands › UPTI  UPTI  -  Utility Purpose settling TIme）

```
UPTI? {(purpose_name)}
```

returns:

```
UPTI {time}, {(purpose_name)}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UPTI  UPTI  -  Utility Purpose settling TIme）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98835_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：time | Specifies the wait time to change the utility line status using the UPST and FLSH commands (in ms). 0 ... 2 147 483.646 [ms]

### Example（取自子主题 Utility Line Commands › List of utility line commands › UPTI  UPTI  -  Utility Purpose settling TIme）

```
UPTI 2.5,(AWG_CNCT)
```

This example sets the settling time of the utility purpose "AWG_CNCT" to 2.5 ms.

### Syntax（取自子主题 Utility Line Commands › List of utility line commands › UTIN  -  UTility line INputs）

```
UTIN?
```

returns:

```
UTIN {data}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UTIN  -  UTility line INputs）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98836_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：data | This parameter returns a decimal number that you must translate to binary. Ignore the most significant bit. The other bits give the state of the seven li…

### Example（取自子主题 Utility Line Commands › List of utility line commands › UTIN  -  UTility line INputs）

```
UTIN?
```

returns:

```
UTIN 6
```

This example returns a decimal value of 6, which is 0000 0110b.

### Syntax（取自子主题 Utility Line Commands › List of utility line commands › UTIX  -  UTility line Inputs eXtended）

```
UTIX? [utility_group]
```

returns

```
UTIX {utility_group}, {value}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UTIX  -  UTility line Inputs eXtended）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98837_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：utility_group | This parameter specifies the utility pogo block. The pogo block is defined by a three‑digit number. For valid pogo blocks, refer to DUT interfac…

### Example 1（取自子主题 Utility Line Commands › List of utility line commands › UTIX  -  UTility line Inputs eXtended）

Assuming that the first 16 utility lines of block 165 are high, then

```
UTIX? 165
```

returns

```
UTIX 165,65535
```

In this example the first 16 utility lines of block 165 were set to 0 by the `UTOT`（raw: `02.06.02.02.311_UTOT__UTOT__-__UTility_line_OuTputs.md`） command and no external device has pulled down any of the utility lines.

### Example 2（取自子主题 Utility Line Commands › List of utility line commands › UTIX  -  UTility line Inputs eXtended）

```
UTIX? 165
```

returns

```
UTIX 165,65534
```

In this example the first 16 utility lines of block 165 were either set to FFFEh by UTOT or they were set to FFFFh and an external device has pulled down line 00, or both occurrences have taken place.

### UTOT（取自子主题 Utility Line Commands › List of utility line commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT {utility_group}, [mask], {value}
```

### UTOT?（取自子主题 Utility Line Commands › List of utility line commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT? {utility_group}
```

returns:

```
UTOT {utility_group}, [mask], {word}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UTOT  UTOT  -  UTility line OuTputs）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98838_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：utility_group | This parameter specifies the utility pogo block. The pogo block is defined by a three‑digit number. For valid pogo blocks, refer to DUT interfac…

### Example 1（取自子主题 Utility Line Commands › List of utility line commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT 165,16383,12345
```

This code sets the first sixteen utility lines of the first block, except those used for the addressing of EEPROMs related to the DUT interface. These are URW14 and URW15. URW0 to URW13 are set to the inverse of 12345. 12345 in decimal equals 0011000000111001 in binary. Inverted, this is 53190 in decimal or 1100111111000110 in binary. Thus the lines will have these states:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98838_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 4 列。
> 首行（上游原文）：URW00 = low | URW04 = low | URW08 = high | URW12 = low

For the utility lines required to address EEPROMs related to the DUT interface see `Utility lines and DUT board EEPROMs`（raw: `../02.03_DUT_board_design_reference/02.03.04.06_Utility_lines_and_DUT_board_EEPROMs.md`）.

### Example 2（取自子主题 Utility Line Commands › List of utility line commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT? 165
```

returns:

```
UTOT 165,,12345
```

The query returns the value that was written by UTOT. If you have previously executed Example 1, then the returned value will be the written value, but bits 14 and 15 may be different. This is because these lines retain the values that have been written previously.

Use the `UTIX?`（raw: `02.06.02.02.310_UTIX__-__UTility_line_Inputs_eXtended.md`） command to read back the actual state of the utility lines.

### Example 3（取自子主题 Utility Line Commands › List of utility line commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT 166,65535,"5555,AAAA,0,FFFF"
```

writes the sequence AAAAh, 5555h, FFFFh, 0000h to the first sixteen utility lines of the second utility block.

### Example 4（取自子主题 Utility Line Commands › List of utility line commands › UTOT  UTOT  -  UTility line OuTputs）

```
UTOT? 166
```

returns the last written values. If you have just executed example 3, the result would be:

```
UTOT 166,,65535
```

### UTSC（取自子主题 Utility Line Commands › List of utility line commands › UTSC  UTSC  -  UTility line Serial Configuration）

```
UTSC {(word) | ALL}, {mode} [, maskMode]
```

### UTSC?（取自子主题 Utility Line Commands › List of utility line commands › UTSC  UTSC  -  UTility line Serial Configuration）

```
UTSC? {(word)} | ALL
```

returns:

```
UTSC {(word)}, {mode} [, maskMode]
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UTSC  UTSC  -  UTility line Serial Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124715_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：word | One unique utility pogo block number or a list enclosed in brackets containing utility pogo blocks separated by commas. The pogo block or the list of pog…
> 表内引用（5 条，供检索）：`DUT interface layout`（raw: `../02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md`） · `Utility pogo block mapping`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md#_347642__s_Utility_pogo_block_mapping`） · `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`） · `UTOT`（raw: `02.06.02.02.311_UTOT__UTOT__-__UTility_line_OuTputs.md`） · `UTIX?`（raw: `02.06.02.02.310_UTIX__-__UTility_line_Inputs_eXtended.md`）

### Example（取自子主题 Utility Line Commands › List of utility line commands › UTSC  UTSC  -  UTility line Serial Configuration）

The following example shows how to reset the mode for all utility blocks to static:

```
UTSC ALL, OFF
```

The following example shows how to gang utility blocks 1 to 4 setting the mode to serial out:

```
UTSC (165,166,167,168),RW
```

The following example shows how to change the mode of the previously set up gang to parallel out:

```
UTSC (165,166,167,168),RD
```

The following example, based on the previous setup, will lead to an error, because the fourth utility pogo block is missing:

```
UTSC (165,166,167),OFF
```

The following example shows how to turn off ganging by changing the mode of the previously set up gang to off:

```
UTSC (165,166,167,168),OFF
```

The following example shows how to set up a new gang with the second, third and fourth utility pogo block in serial out mode:

```
UTSC (166,167,168),RW
```

The following example shows how to use the UTSC? query to display the entire gang and the mode if a single utility block of a gang is given:

```
UTSC? 166
```

results in:

```
UTSC (166,167,168),RW
```

The following example shows how to use the UTSC? query to display all gangs and modes of all utility blocks:

```
UTSC? ALL
```

results in:

```
UTSC 1,OFF
UTSC (166,167,168),RW
UTSC 169,OFF
UTSC 170,OFF
UTSC 171,OFF
UTSC 172,OFF
```

The following example shows how to change the existing gang with utility blocks 2 to 4 in serial out mode to the masked mode:

```
UTSC (166,167,168),RW,MASK
```

The following example shows the query result of UTSC? with mask mode set for the second to fourth utility pogo block:

```
UTSC? ALL
```

results in:

```
UTSC 165,OFF
UTSC (166,167,168),RW,MASK
UTSC 169,OFF
UTSC 170,OFF
UTSC 171,OFF
UTSC 172,OFF
```

### UTST（取自子主题 Utility Line Commands › List of utility line commands › UTST  UTST  -  UTility line STate）

```
UTST {value}, {(util_name)}
```

### UTST?（取自子主题 Utility Line Commands › List of utility line commands › UTST  UTST  -  UTility line STate）

```
UTST? type, {(util_name)}
```

returns:

```
UTST {value}, {(util_name)}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UTST  UTST  -  UTility line STate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98839_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：value | Specifies the output (desired) status of the utility line with the specifier 0 or 1. 0: High output 1: Low output

Specifies the utility line name or names to be set or read.

In the query, specifying @ returns all utility lines.

If more than one name is required, the names must be separated by commas.

   | Note All utility lines that are set with UTST or `UPST`（raw: `02.06.02.02.305_UPST__UPST__-__Utility_Purpose_STate.md`） will be switched in parallel when the `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`） command is performed. If the `WSDN`（raw: `02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.md`） command is used immediately after FLSH, the time span during which execution will pause equals the longest settling time that is defined for any of the switched utility lines (with `UTTI`（raw: `02.06.02.02.314_UTTI__UTTI__-__UTility_line_settling_TIme.md`）) or purposes (with `UPTI`（raw: `02.06.02.02.307_UPTI__UPTI__-__Utility_Purpose_settling_TIme.md`）).

### Example（取自子主题 Utility Line Commands › List of utility line commands › UTST  UTST  -  UTility line STate）

```
UTST 1,(Filt1,Filt2)
UTST 0,(Filt3,Filt4)
FLSH
WSDN
UTST? w,(Filt1,Filt2,Filt3,Filt4)
```

will return:

```
UTST 1,(Filt1,Filt2)
UTST 0,(Filt3,Filt4)
```

This example sets the utility lines "Filt1" and "Filt2" to high output, and "Filt3" and "Filt4" to low output.

### UTTI（取自子主题 Utility Line Commands › List of utility line commands › UTTI  UTTI  -  UTility line settling TIme）

```
UTTI {time}, {(util_name)}
```

### UTTI?（取自子主题 Utility Line Commands › List of utility line commands › UTTI  UTTI  -  UTility line settling TIme）

```
UTTI? {(util_name)}
```

returns:

```
UTTI {time}, {(util_name)}
```

### Parameters（取自子主题 Utility Line Commands › List of utility line commands › UTTI  UTTI  -  UTility line settling TIme）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98840_3.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：time | Specifies the wait time to change the utility line status using the UTST and FLSH command (in ms).
> 表内引用（2 条，供检索）：`UTST`（raw: `02.06.02.02.313_UTST__UTST__-__UTility_line_STate.md`） · `FLSH`（raw: `02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`）

### Example（取自子主题 Utility Line Commands › List of utility line commands › UTTI  UTTI  -  UTility line settling TIme）

```
UTTI 2.5,(filter)
```

This example sets the settling time of the utility line "filter" to 2.5 ms.

### Description（取自子主题 Commands for the TMU per pin › Concepts of the TMU per pin › TMU per Pin overview）

The following figures show the basic principles for period and pulse width measurements. Note that the sample rate of the TMU is 20 ns, and that the minimum distance between two events required by the event discarding block is about 4 ns (for this latter requirement see also `Dealing with very high data rates`（raw: `02.06.13.01.05_Dealing_with_very_high_data_rates.md`）).

### Example 2: Pulse width measurement（取自子主题 Commands for the TMU per pin › Concepts of the TMU per pin › TMU per Pin overview）

The second example illustrates a measurement where rising and falling edges are sampled alternately. This is the basis for measurements of the positive or negative pulse width. No discard before the first measurement has been defined. The graphic only illustrates the case of the positive pulse width.

 !`Pulse width measurement with the ppTMU`（raw: `../../../../raw/127185.png`）

Note the following points with respect to alternate sampling of rising and falling edges:

- The event discarding block only considers the rising edges of the prescaler output; the falling edges are ignored. Therefore all selected events (that is, also the falling edges) are represented by the prescaler as rising edges.
- If in this case the prescaler is set to n, then after selecting an edge, it skips the next n edges of the same type, and then selects the next edge of the opposite type. Thus in the example, after selecting a rising edge, it skips the next 3 rising edges and then selects the next falling edge; and after selecting a falling edge, it skips the next 3 falling edges, and then selects the next rising edge.
- If an even number (including 0) of events is to be discarded before the first sample, the first sampled event will be a rising edge. If you discard an odd number of events before the first sample, the first sampled event will be a falling edge. In this case the formulas for PW+ and PW-, as specified in the graphic, must be interchanged.
- If you specify an odd number of events to be discarded between samples (for example, only one event in the figure above), the sampled events will all be of the same type, that is, they will be either all rising or all falling edges. Therefore, if you want to measure the pulse width, the number of events to be discarded between two samples must be even.
- With alternate sampling of rising and falling edges, the period length can be calculated from the samples by the formula

 (ti+1 - ti-1) / ((prescaling_factor + 0.5) * (inter_meas_discard + 1) * 2).

### Example（取自子主题 Commands for the TMU per pin › Concepts of the TMU per pin › Storing the results of more than one TMU measurement）

```
> TSPR "TMU_set1"
> TSRH? REQUEST,"area1"
< TSRH REQUEST,"area1",SUCCEED
> FTST?
> FTST P
> TSPR "TMU_set2"
> TSRH? REQUEST,"area2"
< TSRH REQUEST,"area2",SUCCEED
> FTST?
< FTST P
> TSRS? ,PERIOD,,,(pin_a)
< TSRS ,PERIOD,,1.36,(pin_a)
> TSRH? SELECT,"area1"
< TSRH SELECT,"area1",SUCCEED
> TSRS? ,PERIOD,,,(pin_a)
< TSRS ,PERIOD,,1.38,(pin_a)
```

This example makes successively `TMU_set1` and `TMU_set2` the primary TMU set, and executes a test with each of these primary TMU sets. The results of the first measurement are stored in `area1`, those of the second in `area2`. Afterwards, the global means of both measurements are retrieved with TSRS?.

### TSCF（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSCF  TSCF  -  TMU Set ConFiguration）

```
TSCF {"ts_name"}, {property}, {property_value|RESET}, {(pinlist)}
```

### TSCF?（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSCF  TSCF  -  TMU Set ConFiguration）

```
TSCF? {"ts_name"|ALL|PRM}, [property], {(pinlist)}
```

returns:

```
TSCF {"ts_name"}, {property}, {property_value}, {(pinlist)}
```

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSCF  TSCF  -  TMU Set ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125467_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：ts_name | Specifies the name of a TMU set that must have been defined with TSDF.

Properties and their values
| Property | Explanation and values | Explanation and values |
|---|---|---|
| DATA_RATE | This property defines the data rate which is the smallest distance between two events. The unit is bits per second. | This property defines the data rate which is the smallest distance between two events. The unit is bits per second. |
| EDGE_SELECT | This mandatory property defines which edges are the events to be sampled. Possible values are: | This mandatory property defines which edges are the events to be sampled. Possible values are: |
|  | RISE | The events are rising edges. |
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125467_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 3 列。
> 首行（上游原文）：Property | Explanation and values

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSCF  TSCF  -  TMU Set ConFiguration）

```
> TSCF? "TMU_set1",,(Pin1)

< TSCF "TMU_set1",PRESCALER,3,(Pin1)
< TSCF "TMU_set1",INITIAL_DISCARD,0,(Pin1)
< TSCF "TMU_set1",INTER_SAMPLE_DISCARD,500,(Pin1)
< TSCF "TMU_set1",SAMPLES_PER_MEAS,2,(Pin1)
< TSCF "TMU_set1",NUM_SHOTS,1,(Pin1)
< TSCF "TMU_set1",MEAS_PER_SHOT,5,(Pin1)
< TSCF "TMU_set1",EDGE_SELECT,RISE,(Pin1)
< TSCF "TMU_set1",DATA_RATE,50000000,(Pin1)
```

This example queries a period measurement definition. Typically, only two samples are taken for such a measurement, and these at a great distance (see the INTER_SAMPLE_DISCARD property in the example). The period resulting from this measurement can be retrieved with the `TSRS?`（raw: `02.06.02.02.278_TSRS__-__TMU_Set_ReSults.md`） query.

### TSDF（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSDF  TSDF  -  TMU Set DeFinition）

```
TSDF {"TMU_set_name"} [, "mode_context"]
```

### TSDF?（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSDF  TSDF  -  TMU Set DeFinition）

```
TSDF? ["TMU_set_name"]
```

returns:

```
TSDF {"TMU_set_name"} [, "mode_context"]
```

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSDF  TSDF  -  TMU Set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126322_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：TMU_set_name | In the command, this is the name of a new TMU set. In the query, it is a name of an existing TMU set. If you omit this parameter in the query, TS…

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSDF  TSDF  -  TMU Set DeFinition）

```
> TSDF   "TMU_set1"
> TSDF   "TMU_set2"
> TSDF   "TMU_set3"

> TSDF?
< TSDF   "TMU_set1"
< TSDF   "TMU_set2"
< TSDF   "TMU_set3"

```

### Syntax（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSER  -  TMU Set ERror）

```
TSER? {(pinlist)}
```

returns:

```
TSER {VDL_OVERRUN|ARM_OVERRUN|OUT_OF_MEMORY|GLITCH_OVERRUN|NOT_FINISHED}, {(pinlist)}
```

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSER  -  TMU Set ERror）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126327_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：VDL_OVERRUN | The sample rate of the TMU is exceeded.
> 表内引用（1 条，供检索）：`Dealing with very high frequencies`（raw: `02.06.13.01.05_Dealing_with_very_high_data_rates.md`）

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSER  -  TMU Set ERror）

```
> TSER? (Pin1)
< TSER ARM_OVERRUN,(Pin1)
```

### TSHA?（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSHA  -  Timing Setup Has Arming）

```
TSHA? {specset_id|"multi-port_spec"}, {(pinlist)}
```

returns:

TSHA {specset_id|"multi-port_spec"},{TRUE|FALSE}, {(pinlist)}

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSHA  -  Timing Setup Has Arming）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131111_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：specset_id | Derived as follows: 100 * equation_set_no + specset_no

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSHA  -  Timing Setup Has Arming）

```
> TSHA? "MP_1",(pin1)
< TSHA "MP_1",FALSE,(pin1)
```

### Syntax（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSMD  -  TMU Set Measurement Done）

TSMD? [FORCE,] {(pinlist)}

Returns:

TSMD {FINISHED|NOT_FINISHED}, {(pinlist)}

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSMD  -  TMU Set Measurement Done）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125551_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：FORCE | If this extra parameter is specified in the query The TMU measurement will be stopped even if it is not yet finished.

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSMD  -  TMU Set Measurement Done）

```
> TSMD? (Pin1)
< TSMD FINISHED,(Pin1)
```

### Syntax（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRH  -  TMU Set Result Handle）

```
TSRH? {REQUEST|SELECT|RELEASE}, {"handle_name"}
```

returns:

TSRH {REQUEST|SELECT|RELEASE}, {"handle_name"}, {SUCCEED|FAILED}

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRH  -  TMU Set Result Handle）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126271_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：REQUEST | Defines a handle. If the request is successful, the new handle will be the active handle.

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRH  -  TMU Set Result Handle）

```
> TSRH? REQUEST, "area1"
< TSRH REQUEST,"area1",SUCCEED
```

### TSPR（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSPR  TSPR  -  TMU Set PRimary set）

```
TSPR {"TMU_set_name"|""}
```

### TSPR?（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSPR  TSPR  -  TMU Set PRimary set）

```
TSPR?
```

returns:

```
TSPR {"TMU_set_name"|""}
```

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSPR  TSPR  -  TMU Set PRimary set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125518_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：TMU_set_name | Specifies the name of an existing TMU set.

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSPR  TSPR  -  TMU Set PRimary set）

```
> TSPR   "TMU_set1"
```

### Syntax（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRC  -  Time Stamping Results Computed）

```
TSRC? [(sitesToBeDone),] [measurement_id], {result_type}, [first_sample], [no_of_samples], [(execution_control),] [(site_selector),] [(resultAreaName),] {(pinlist)}
```

returns:

```
TSRC [shotcount],{result_type}, {successinfo}, {(pin)}
```

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRC  -  Time Stamping Results Computed）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/141847_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：16 行 × 6 列，含嵌套表。
> 首行（上游原文）：sitesToBeDone | An extra string parameter, defining the sites to be uploaded. i.e. "01110011". This option needs parameter site_selector to be set to ALL.
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/141847_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：NOT_FINISHED | Default. All three steps described above will be executed. If not all required samples have been actually taken, the query will not stop, it issu…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/141847_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ONE | Only the values of the site which has the query focus are processed (the default).

### Syntax（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRS  -  TMU Set ReSults）

```
TSRS? [(sitesToBeDone),] [measurement_id], {result_type}, [first_sample], [no_of_samples], [(execution_control),] [(site_selector),] [(resultAreaName),] [(mode),] {(pinlist)}
```

returns:

```
TSRS [measurement_id], [(sitenumber),] {result_type}, [sample_id|aggregation_type|first_sample], {result|no_of_samples}, {(pin)} [,#spec(binary_results)]
```

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRS  -  TMU Set ReSults）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125500_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：NOT_FINISHED | All four steps described above will be executed. If not all required samples have been actually taken, the query will not stop, it will continue …
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125500_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ONE | Only the values of the site which has the query focus are processed (the default).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125500_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：21 行 × 6 列，含嵌套表。
> 首行（上游原文）：sitesToBeDone | An extra string parameter, defining the sites to be uploaded. i.e. "01110011". This option needs parameter site_selector to be set to ALL.

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRS  -  TMU Set ReSults）

This example returns the descriptive statistics for the measurement blocks individually.

```
> TSRS? ,PERIOD, , , (pin_a)

    < TSRS  1,PERIOD , STDDEV ,1.36,(pin_a)
    < TSRS  1,PERIOD , MEAN 1.36,(pin_a)
    < TSRS  1,PERIOD , MAX, 1.36,(pin_a)
    < TSRS  1,PERIOD , MIN, 1.36,(pin_a)
    < TSRS  1,PERIOD , MEDIAN, 1.36,(pin_a)
    < TSRS  1,PERIOD , PP, 1.36,(pin_a)

    < TSRS  2,PERIOD , STDDEV ,1.36,(pin_a)
    < TSRS  2,PERIOD , MEAN 1.36,(pin_a)
    < TSRS  2,PERIOD , MAX, 1.36,(pin_a)
    < TSRS  2,PERIOD , MIN, 1.36,(pin_a)
    < TSRS  2,PERIOD , MEDIAN, 1.36,(pin_a)
    < TSRS  2,PERIOD , PP, 1.36,(pin_a)
```

This example returns the individual samples 100 through 119 in measurement block 2, and also the statistical values.

```
> TSRS? 2,PERIOD,100,20,(pin_a)

    < TSRS  2,PERIOD ,100,1.36,(pin_a)
    < TSRS  2,PERIOD ,101,1.37,(pin_a)
    ...
    < TSRS  2,PERIOD ,119,1.36,(pin_a)
    < TSRS  2,PERIOD , STDDEV ,1.36,(pin_a)
    < TSRS  2,PERIOD , MEAN 1.36,(pin_a)
    < TSRS  2,PERIOD , MAX, 1.36,(pin_a)
    < TSRS  2,PERIOD , MIN, 1.36,(pin_a)
    < TSRS  2,PERIOD , MEDIAN, 1.36,(pin_a)
    < TSRS  2,PERIOD , PP, 1.36,(pin_a)
```

### Syntax（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRW  -  TMU Set RaW results）

```
TSRW? [(sitesToBeDone),] [shot], [measurement_id], [first_sample], [no_of_samples], [(execution_control),] [(site_selector),][(resultAreaName),] [(mode),] {(pinlist)}
```

returns:

```
TSRW [shot], [measurement_id], [first_sample], [no_of_samples], [(sitenumber),] {(pin)}, {#spec(raw_results)}
```

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRW  -  TMU Set RaW results）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125519_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：NOT_FINISHED | All three steps described above will be executed. If not all required samples have been actually taken, the query will not stop, it issues a warn…
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125519_2.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ONE | Only the values of the site which has the query focus are uploaded (the default).
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/125519_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 6 列，含嵌套表。
> 首行（上游原文）：sitesToBeDone | An extra string parameter, defining the sites to be uploaded. i.e. "01110011". This option needs parameter site_selector to be set to ALL.

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSRW  -  TMU Set RaW results）

```
> TSRW? 1,1,0,3,(std_i)

    < TSRW 1,1,0,3,(std_i),#2470.0000524107368,0.0000525147428,0.0000526187385
```

This example uploads the time stamps 0 through 2 of measurement block 1 of the first shot. The unit is seconds.

### Syntax（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSUD -  TMU Set UnDefine）

```
TSUD {"TMU_set_name"|ALL}
```

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSUD -  TMU Set UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126323_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：TMU_set_name | Specifies the name of an existing TMU set.

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSUD -  TMU Set UnDefine）

```
> TSUD   "TMU_set1"
```

### Syntax（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSVD  -  TimStamper ValiD）

```
TSVD? {waveform_set|specset_id|"multi-port_spec"|PRM}, {"TMU_set"|PRM}
```

returns:

```
TSVD? {waveform_set|specset_id|"multi-port_spec"|PRM}, {"TMU_set"|PRM}, {VALID|ERROR}
```

### Parameters（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSVD  -  TimStamper ValiD）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/130393_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：waveform_set | Specifies a waveform set number for a fixed timing setup.

### Example（取自子主题 Commands for the TMU per pin › List of commands for the TMU per pin › TSVD  -  TimStamper ValiD）

```
> TSVD? PRM, "TMU_set1"
< TSVD PRM, "TMU_set1",VALID
```

This example queries if the current primary timing is consistent to the TMU set `TMU_set1`.

### Example（取自子主题 Commands for Processing Results of Source Synchronous Testing › Concepts of source synchronous testing  html › Principles of source synchronous testing）

The following figure illustrates the principle by a very simple example with deterministic phase distortion (common mode drift):

 !`Pattern iteration for source-synchronous testing`（raw: `../../../../raw/84881.png`）

In this example, the pattern is repeated eight times. This is a certain redundancy since every cycle has passed at least in one shot already after the third shot. If unnecessary shots are to be avoided, the overall result would have to be checked after each shot.

So far, it has been assumed that only one data change occurs in every cycle, so that only one result per cycle is required. But you can also check several changes in one cycle. In this case you would have to record results on the edge level (all eight edges are recorded in one shot). In this case the whole pattern would be considered as passed if every edge passes at least in one shot.

The above discussion centers on validation of a given requirement. But you can also measure the actual setup time by setting the distance between the data edge and the clock edge to 0. The setup time will then be the time between the first and the last point where the expected values are received for both data and clock.

A group of output data pins and the associated output clock pin is called a synchronization group. One source synchronous device may contain several synchronization groups.

### SSAC（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSAC  SSAC  -  Source Synchronous testing  Add Configuration）

```
SSAC [read_mode],[nr_of_results],[(ref_pin}],{(pinlist)}
```

### SSAC?（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSAC  SSAC  -  Source Synchronous testing  Add Configuration）

```
SSAC?
```

returns:

```
SSAC {read_mode},[nr_of_results],[(ref_pin}],{(pinlist)}
```

### Parameters（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSAC  SSAC  -  Source Synchronous testing  Add Configuration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98755_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 3 列。
> 首行（上游原文）：read_mode | Possible read modes are:

### Example（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSAC  SSAC  -  Source Synchronous testing  Add Configuration）

The following example shows how the buffer channels are configured by using a reference pin:

```
> DCGM ALL,STRT,NONE
> DCRT RAM,(@)
> SSRC (@)
> SVLR TIM,1,1,"sweep",2.4
> FTST?
> SSAC INV,,(D1),(SB)
> SSAC NORM,,(D1),(G1,G2)
> SSCT IMM,NORM,,(SB),(D1,D2,D3,CL)
> SSCT ACC,NORM,,(G1),(SB)
> SVLR TIM,1,1,"sweep",2.5
> FTST?
. . .
```

First the detailed Error Map is configured for source synchronous testing (recording mode ALL, location in RDRAM). Next the existing buffer configurations are removed. Then the sweep variable is set, and the first functional test executed. Subsequently the buffer channels are configured using D1 as the reference pin. Then the results of the first functional test are processed. Finally, the sweep variable is incremented and the next functional test executed.

### SSCT（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSCT  SSCT  -  Source Synchronous data  Combine and Transfer）

```
SSCT {exec_mode},[read_mode],[nr_of_results],{(dest_pin)}, {(source_pins)}
```

### SSCT?（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSCT  SSCT  -  Source Synchronous data  Combine and Transfer）

```
SSCT? {(dest_pins)}
```

returns:

```
SSCT {exec_mode},{read_mode},{nr_of_results},{(dest_pin)}, {(source_pins)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98756_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 3 列。
> 首行（上游原文）：exec_mode | Possible execution modes are:

### Example（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSCT  SSCT  -  Source Synchronous data  Combine and Transfer）

The following example shows a typical start sequence of a source synchronous test:

```
> DCGM ALL,STRT,NONE
> DCRT RAM,(@)
> SSRC (@)
> SSAC INV,128,,(SB)
> SSAC NORM,128,,(G1,G2)
> SVLR TIM,1,1,"sweep",2.4
> FTST?
> SSCT IMM,NORM,128,(SB),(D1,D2,D3,CL)
> SSCT ACC,NORM,128,(G1),(SB)
> SVLR TIM,1,1,"sweep",2.5
> FTST?
> SSCT IMM,NORM,128,(SB),(D1,D2,D3,CL)
> SSCT ACC,NORM,128,(G2),(SB,G1)
. . .
```

At first, the detailed Error Map is configured for the requirements of result buffering (error map located in RDRAM, recording mode ALL). After the first functional test the results of the data pins D1 through D3 and the output clock pin CL are immediately combined and transferred into the source buffer SB. The subsequent transfer into the first global buffer is delayed and will only be triggered by the next FTST? call. After the second functional test, the SSCT ACC call combines the results of the source buffer and the first global buffer into the second global buffer.

### Syntax（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSRC -  Source Synchronous testing  Remove Configurations）

```
SSRC {(pinlist)}
```

### Parameters（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSRC -  Source Synchronous testing  Remove Configurations）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98758_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pinlist | The pins whose buffer configurations are to be removed. Pins for which no buffer configuration exists are ignored.

### Example（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSRC -  Source Synchronous testing  Remove Configurations）

```
> SSRC (@)
```

This example removes all buffer configurations. Pins for which no buffer has been configured are ignored.

### Syntax（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSTR  -  Source Synchronous Testing  Result query）

```
SSTR? [ALL_SITES,] {GLO|INV},{(pinlist)}
```

returns:

```
SSTR {GLO|INV},{(pinlist)},{glob_res}
```

Or:

```
SSTR? {DET},{(pin)}
```

returns:

```
SSTR {DET},{(pin)},{#spec(data)}}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98759_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：ALL_SITES | This parameter causes SSTR? to return a global result for all sites. If it is omitted, the result for that site is returned that currently has the r…

### Example（取自子主题 Commands for Processing Results of Source Synchronous Testing › List of commands for source synchronous testing › SSTR  -  Source Synchronous Testing  Result query）

The following example assumes that the global buffer pins G2 and G4 contain the total results of two source synchronous tests that were run in parallel:

```
> SSTR? INV,(G2)
< SSTR INV,(G2),P
> SSTR? INV,(G4)
< SSTR INV,(G4),F
> $SSTR? DET,(G4)
< SSTR DET,(G4),#9000000008,0000 0000  0001 0000  0000 0000  0000 0100  0000 0000  0000 0000  0000 0000  0000 0000
> SSTR? INV,(G2,G4)
< SSTR INV,(G2,G4),F
```

Note that the result granularity has been set to 8, so that every bit of the SSTR DET reply represents one receive edge. Note also that SSTR DET simply returns the buffer content. Since the global buffers must represent FAIL by 1 and PASS by 0, the reply indicates that one edge in the second cycle and one edge in the fourth cycle have failed in all shots for one of the two tests. All other edges have passed at least in one shot.

### Example（取自子主题 Commands for the protocol engine per pin › Overview of the protocol engine per pin › Drift and transition tracking）

!`Transition tracking`（raw: `../../../../raw/146398.png`）

This example picks up the example of `Overview of the protocol engine per pin`（raw: `02.06.15.01_Overview_of_the_protocol_engine_per_pin.md`）. Five observation windows are shown. There are last CD transitions in the first and third window. The fourth window has its last internal transition between A and B in the third sub-window.

### CFCF（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › CFCF  CFCF  -  Clock Forwarding ConFiguration）

```
CFCF {"cf_name"}, {(source_pin)}, {(sink_pins)} [, speed]
```

### CFCF?（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › CFCF  CFCF  -  Clock Forwarding ConFiguration）

```
CFCF? {"cf_name"}, {(pinlist)}
```

returns:

```
CFCF {"cf_name"}, {(source_pin)}, {(sink_pins)} [, speed]
```

### Parameters（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › CFCF  CFCF  -  Clock Forwarding ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117851_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：cf_name | Specifies the name of a clock forwarding set that must have been defined with CFDF.
> 表内引用（1 条，供检索）：`Implementation details of clock forwarding`（raw: `02.06.15.01.01.05.01_Implementation_details_of_clock_forwarding.md`）

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › CFCF  CFCF  -  Clock Forwarding ConFiguration）

```
> CFCF? "cf_set1",(@)
< CFCF "cf_set1",(Pin1),(Pin3, Pin2)
< CFCF "cf_set1",(Pin4),(Pin5)
> CFCF "cf_set1",(Pin1),(Pin6, Pin3)
> CFCF "cf_set1",(Pin7),(Pin4)
> CFCF? "cf_set1",(@)
> CFCF "cf_set1",(Pin1),(Pin6, Pin3)
> CFCF "cf_set1",(Pin7),(Pin4)
```

### CFDF（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › CFDF  CFDF  -  Clock Forwarding Set DeFinition）

```
CFDF {"cf_set_name"} [, "mode_context"]
```

### CFDF?（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › CFDF  CFDF  -  Clock Forwarding Set DeFinition）

```
CFDF? ["cf_set_name"]
```

returns:

```
CFDF {"cf_set_name"} [, "mode_context"]
```

### Parameters（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › CFDF  CFDF  -  Clock Forwarding Set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117850_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：cf_set_name | In the command, this is the name of a new clock forwarding set. In the query, it is a name of an existing clock forwarding set. If you omit this p…

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › CFDF  CFDF  -  Clock Forwarding Set DeFinition）

```
> CFDF   "cf_set1"
> CFDF   "cf_set2"
> CFDF   "cf_set3"

> CFDF?
< CFDF   "cf_set1"
< CFDF   "cf_set2"
< CFDF   "cf_set3"
```

### TTCF（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTCF  TTCF  -  Transition Test ConFiguration）

```
TTCF {"tt_name"}, {property}, {property_value}, {(pinlist)}
```

### TTCF?（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTCF  TTCF  -  Transition Test ConFiguration）

```
TTCF? {"tt_name"|ALL|PRM|DEFAULT}, {property|ALL}, {(pinlist)}
```

returns:

```
TTCF {"tt_name"}, {property}, {property_value}, {(pinlist)}
```

### Parameters（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTCF  TTCF  -  Transition Test ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116670_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：tt_name | Specifies the name of a transition test set that must have been defined with TTDF.
> 表内引用（1 条，供检索）：`TTDF`（raw: `02.06.02.02.288_TTDF__TTDF__-__Transition_Test_set_DeFinition.md`）

Properties and their values
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116670_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：43 行 × 4 列。
> 首行（上游原文）：Property | Explanation and values

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTCF  TTCF  -  Transition Test ConFiguration）

```
> TTCF? "my_TT_SET",ALL,(PIN1)

< TTCF "my_TT_SET",DEVIATION_LIMIT_DUT_BEFORE_ED,100,(Pin1)
< TTCF "my_TT_SET",DEVIATION_LIMIT_ED_BEFORE_DUT,100,(Pin1)
< TTCF "my_TT_SET",DISPARITY_MODE,OFF,(Pin1)
< TTCF "my_TT_SET",ERR_BADTRAN,ON,(Pin1)
< TTCF "my_TT_SET",ERR_CNTADJOVR,ON,(Pin1)
< TTCF "my_TT_SET",ERR_CNTLMT,ON,(Pin1)
< TTCF "my_TT_SET",ERR_COMPARE,ON,(Pin1)
< TTCF "my_TT_SET",ERR_FTO,ON,(Pin1)
< TTCF "my_TT_SET",ERR_JMP2,ON,(Pin1)
< TTCF "my_TT_SET",ERR_PULSE,ON,(Pin1)
< TTCF "my_TT_SET",ERR_STO,ON,(Pin1)
< TTCF "my_TT_SET",ERR_STOP,OFF,(Pin1)
< TTCF "my_TT_SET",ERR_TE0,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TE2,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TE3,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TE4,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TRK,ON,(Pin1)
< TTCF "my_TT_SET",ERR_TRMCNT,ON,(Pin1)
< TTCF "my_TT_SET",ERR_WRCMP,ON,(Pin1)
< TTCF "my_TT_SET",ERR_XMAX,ON,(PIN1)
< TTCF "my_TT_SET",ERR_XMIN,ON,(Pin1)
< TTCF "my_TT_SET",FIRST_INITIAL_SYNC_LIMIT,10,(Pin1)
< TTCF "my_TT_SET",FIRST_INITIAL_SYNC_MODE,ON,(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_1,"LLLLLHHHHH",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_2,"",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_3,"",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_4,"",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_5,"",(Pin1)
< TTCF "my_TT_SET",IDLE_TOKEN_6,"",(Pin1)
< TTCF "my_TT_SET",PULSE_STRETCHING_MODE_1BIT,STRETCH_2TO4,(Pin1)
< TTCF "my_TT_SET",PULSE_STRETCHING_MODE_2BIT,STRETCH_1TO3,(Pin1)
< TTCF "my_TT_SET",REMOVE_XTOKEN_MODE,OFF,(Pin1)
< TTCF "my_TT_SET",SUBSEQUENT_INITIAL_SYNC_LIMIT,10,(Pin1)
< TTCF "my_TT_SET",SUBSEQUENT_INITIAL_SYNC_MODE,ON,(Pin1)
< TTCF "my_TT_SET",TOKEN_SIZE,10,(Pin1)
< TTCF "my_TT_SET",TRACKING_LIMIT,4,(Pin1)
< TTCF "my_TT_SET",TRACKING_MODE,ACTIVE,(Pin1)
```

### Syntax（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTDB  -  Transition Test DeBug information）

```
TTDB? {type|ALL}, [sub_type], {(pinlist)}
```

returns:

```
TTDB {type}, [sub_type], {value}, {(pinlist)}
```

### Parameters（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTDB  -  Transition Test DeBug information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116688_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：type | Specifies the information type. For a list, see the Information types and subtypes table below.

Information types and subtypes
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116688_2.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 4 列。
> 首行（上游原文）：Information type | Explanation and values
> 表内引用（3 条，供检索）：`Drift and transition tracking`（raw: `02.06.15.01.01_Drift_and_transition_tracking.md`） · `TTST?`（raw: `02.06.02.02.292_TTST__-__Transition_Test_STatus_information.md`） · `TTCF`（raw: `02.06.02.02.286_TTCF__TTCF__-__Transition_Test_ConFiguration.md`）

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTDB  -  Transition Test DeBug information）

```
> TTDB? IDLE_TOKEN, 1, (Pin1)

< TTDB IDLE_TOKEN, 1, 1234,(Pin1)
```

This example queries how often the first special idle token was removed in the last sequencer run.

```
> TTDB? TRK_STATUS,ALL, (Pin1)

< TTDB TRK_STATUS,TRANS_X,"1000 1001 1101 1000", (Pin1)
< TTDB TRK_STATUS,TRANS_R,0, (Pin1)
< TTDB TRK_STATUS,TRANS_COMPOSITE,"1000 1001 1101", (Pin1)
```

The first line of the reply reports the transitions of the last 24 UI, accumulated in blocks of 6. The third line reports which accumulated transition patterns occurred in one window (= 3 UI) during the last sequencer run. Three of the 8 possible patterns were observed.

### TTDF（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTDF  TTDF  -  Transition Test set DeFinition）

```
TTDF {"tt_set_name"} [, "mode_context"]
```

### TTDF?（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTDF  TTDF  -  Transition Test set DeFinition）

```
TTDF? ["tt_set_name"]
```

returns:

```
TTDF {"tt_set_name"} [, "mode_context"]
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116759_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：tt_set_name | In the command, this is the name of a new transition test set. In the query, it is a name of an existing transition test set. If you omit this par…

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTDF  TTDF  -  Transition Test set DeFinition）

```
> TTDF   "myTTTrckSet1"
> TTDF   "myTTPatTSet1"
> TTDF   "myTTRCTLSet1"

TTDF?
> TTDF   "myTTTrckSet1"
> TTDF   "myTTPatTSet1"
> TTDF   "myTTRCTLSet1"
```

### Syntax（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTMD  -  Transition Test MoDe query）

```
TTMD? {specset_id|"multi-port_spec"}, {timing_set}, {(pinlist)}
```

returns:

```
TTMD {specset_id|"multi-port_spec"}, {timing_set}, {tt_mode}, [clk_fwd], {(pinlist)}
```

### Parameters（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTMD  -  Transition Test MoDe query）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116966_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：specset_id | Number of a single-port timing specification. Derived as follows: 100 *equation_set_no + specset_no
> 表内引用（1 条，供检索）：`DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTMD  -  Transition Test MoDe query）

```
> TTMD 101,1,(PIN1)
< TTMD 101,1,X4,,(PIN1)
```

### TTPR（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTPR  TTPR  -  Transition Test PRimary set）

TTPR {"tt_set_name"|DEFAULT}

### TTPR?（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTPR  TTPR  -  Transition Test PRimary set）

```
TTPR?
```

returns:

```
TTPR {"tt_set_name"}
```

### Parameters（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTPR  TTPR  -  Transition Test PRimary set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116761_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：tt_set_name | Specifies the name of an existing transition test set.

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTPR  TTPR  -  Transition Test PRimary set）

```
> TTPR   "myTTTrckSet1"
```

### Syntax（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTST  -  Transition Test STatus information）

```
TTST? {status_type}, {filter}, {(pinlist)}
```

returns:

TTST {status_type}, {property}, {state}, {(pinlist)}

### Parameters（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTST  -  Transition Test STatus information）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116741_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：38 行 × 4 列。
> 首行（上游原文）：status_type | Specifies the status type. Possible values are:

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTST  -  Transition Test STatus information）

```
> TTST? ALL,ALL,(p1)

< TTST INTR_STATUS,DRIVE_BIT_IN_COMPARE_DATA,OFF,(p1)
< TTST INTR_STATUS,ADJUSTMENT_ERROR,OFF,(p1)
< TTST INTR_STATUS,DUT_FIFO_OVERFLOW,OFF,(p1)
< TTST INTR_STATUS,EXPECTED_FIFO_OVERFLOW,OFF,(p1)
< TTST ERR_STATUS,ERR_XMAX,OFF,(p1)
< TTST ERR_STATUS,ERR_XMIN,OFF,(p1)
< TTST ERR_STATUS,ERR_FTO,OFF,(p1)
< TTST ERR_STATUS,ERR_STO,OFF,(p1)
< TTST ERR_STATUS,ERR_TRMCNT,OFF,(p1)
< TTST ERR_STATUS,ERR_COMPARE,ON,(p1)
< TTST ERR_STATUS,ERR_TE4,OFF,(p1)
< TTST ERR_STATUS,ERR_TE3,OFF,(p1)
< TTST ERR_STATUS,ERR_TE2,ON,(p1)
< TTST ERR_STATUS,ERR_TE0,OFF,(p1)
< TTST ERR_STATUS,ERR_JMP2,ON,(p1)
< TTST ERR_STATUS,ERR_TRK,OFF,(p1)
< TTST ERR_STATUS,ERR_PULSE,OFF,(p1)
< TTST ERR_STATUS,ERR_BADTRAN,OFF,(p1)
< TTST ERR_STATUS,ERR_CNTADJOVR,OFF,(p1)
< TTST ERR_STATUS,ERR_CNTLMT,OFF,(p1)
< TTST ERR_STATUS,ERR_STOP,OFF,(p1)
< TTST ERR_STATUS,ERR_WRCMP,OFF,(p1)
```

This example returns all properties of the ERR_STATUS type. ON indicates that the respective state was observed, OFF indicates that it was not observed. Note that ON does not imply that the test failed. For this, the respective property must also be activated as an error with TTCF. In this example compare errors (ERR_COMPARE) and a jump by 2 (ERR_TE2, ERR_JMP2) were observed.

### Syntax（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTUD -  Transition Test UnDefine）

TTUD {"tt_set_name"}

### Parameters（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTUD -  Transition Test UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116760_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：tt_set_name | Specifies the name of an existing transition test set.

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTUD -  Transition Test UnDefine）

```
> TTUD   "myTTTrckSet1"
```

### Syntax（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTVD  -  Transition Test ValiDate）

```
TTVD? {"tt_name"|ALL|PRM}, {(pinlist)}
```

returns:

```
TTVD {"tt_name"}, {VALID|INVALID}, {(pinlist)}
```

### Parameters（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTVD  -  Transition Test ValiDate）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116763_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：tt_name | Specifies the name of a transition test set that must have been defined with TTDF.
> 表内引用（1 条，供检索）：`TTDF`（raw: `02.06.02.02.288_TTDF__TTDF__-__Transition_Test_set_DeFinition.md`）

### Example（取自子主题 Commands for the protocol engine per pin › List of commands for protocol engine tests › TTVD  -  Transition Test ValiDate）

```
> TTVD? "mySet",(p1,p2,p3)
< TTVD  "mySet", VALID, (p1,p3)
< TTVD  "mySet", INVALID, (p3)
```

### Example（取自子主题 Commands for jitter injection › Principles of jitter injection）

!`Predefined jitter modulation waveforms`（raw: `../../../../raw/117826.png`）

These are three of the four predefined jitter modulation waveforms that are available on a Smart Scale system.

### Syntax（取自子主题 Commands for jitter injection › List of commands for jitter injection › JRST -  Jitter modulator ReseT）

```
JRST {(pin_list)}
```

### Parameters（取自子主题 Commands for jitter injection › List of commands for jitter injection › JRST -  Jitter modulator ReseT）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/119634_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：pin_list | The pins for which the jitter modulator is to be reset. Typically, this must be done for all configured pins, so that you will usually specify @ for …

### Example（取自子主题 Commands for jitter injection › List of commands for jitter injection › JRST -  Jitter modulator ReseT）

```
JRST (@)
```

This example resets the jitter modulator of all configured pins to its default state OFF.

### JSCF（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSCF  JSCF  -  Jitter Set ConFiguration）

```
JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}
```

### JSCF?（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSCF  JSCF  -  Jitter Set ConFiguration）

```
JSCF? {"jitter_set_name"|ALL|PRM}, {"property"|ALL}, {(pinlist)}
```

returns:

```
JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}
```

### Parameters（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSCF  JSCF  -  Jitter Set ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/116890_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：jitter_set_name | Specifies the name of a jitter set that must have been defined with JSDF.

### Example（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSCF  JSCF  -  Jitter Set ConFiguration）

```
> JSCF? "my_J_SET",ALL,(Pin1)
< JSCF "my_J_SET",MODE,CONT,(Pin1)
< JSCF "my_J_SET",WAVEFORM,"-100,-50,0,50,100,50,0,-50",(Pin1)
< JSCF "my_J_SET",PERIODFACTOR,25,(Pin1)
```

This example defines a simple sawtooth waveform with a peak-to-peak value of 200ps for a STDDIFF or STD pin.

### Parameters（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSDF  JSDF  -  Jitter Set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117922_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：js_set_name | In the command, this is the name of a new jitter set. In the query, it is a name of an existing jitter set. If you omit this parameter in the quer…

### Example（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSDF  JSDF  -  Jitter Set DeFinition）

```
> JSDF   "js_set1"
> JSDF   "js_set2"
> JSDF   "js_set3"

> JSDF?
< JSDF   "js_set1"
< JSDF   "js_set2"
< JSDF   "js_set3"

```

### JSPR（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSPR  JSPR  -  Jitter Set PRimary set）

```
JSPR {"js_set_name"|""}
```

### JSPR?（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSPR  JSPR  -  Jitter Set PRimary set）

```
JSPR?
```

returns:

```
JSPR {"js_set_name"|""}
```

### Parameters（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSPR  JSPR  -  Jitter Set PRimary set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117945_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：js_set_name | Specifies the name of an existing jitter set. Specify an empty string to inactivate the current primary set and thus to disable jitter injection.

### Example（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSPR  JSPR  -  Jitter Set PRimary set）

```
> JSPR   "js_set1"
```

### Syntax（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSUD -  Jitter Set UnDefine）

```
JSUD {"js_set_name"|ALL}
```

### Parameters（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSUD -  Jitter Set UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/117930_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：js_set_name | Specifies the name of an existing jitter set.

### Example（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSUD -  Jitter Set UnDefine）

```
> JSUD   "js_set1"
```

### Syntax（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSWF  -  Jitter Set WaveForm）

```
JSWF? {"jitter_set_name"}, {clock_resolution}, {(pinlist)}
```

returns:

```
JSWF {"jitter_set_name"}, {"offset_sequence"}, {(pinlist)}
```

### Parameters（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSWF  -  Jitter Set WaveForm）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/119599_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：jitter_set_name | Specifies the name of a jitter set that must have been defined with JSDF.

### Example 1（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSWF  -  Jitter Set WaveForm）

```
> jscf? "test",,(IO0)
< JSCF "test",WAVEFORM,SINUS,(IO0)
< JSCF "test",PERIOD,20,(IO0)
< JSCF "test",AMPLITUDE,100,(IO0)
> CLKR? EXACT,101,(@)
< CLKR 101,2.4,1.2,(@)
> jswf? "test",1200,(IO0)
< JSWF "test","0,29,47,47,29,0,-30,-48,-48,-30,-1,29,47,47,29,0,
  . . .
  -1,-30,-48,-48,-30,0,29,47,47,29,0,-30,-48,-48,-30",(IO0)
```

This example first queries the jitter waveform for pin `IO0`, and also the clock resolution for timing specification 101. It then calculates the offset sequence for this waveform and clock resolution. Note that CLKR? returns the clock resolution as nano seconds, but that JSWF? expects it to be specified as pico seconds. The reply is displayed in abbreviated form. The total length of the sequence is about 500 items.

### Example 2（取自子主题 Commands for jitter injection › List of commands for jitter injection › JSWF  -  Jitter Set WaveForm）

```
> JSCF? "test",WAVEFORM,(IO1)
< JSCF "test",WAVEFORM,"150,110,80,70,0"
> JSWF? "test",880,(IO1)
< JSWF "test","150,120,90,70,40",(IO1)
```

This example shows how JSWF? corrects the offset list if the second of two consecutive items is smaller than the first, and the maximum difference is exceeded.

### MSCF（取自子主题 Commands for jitter injection › List of commands for jitter injection › MSCF  MSCF  -  Modulation Set ConFiguration）

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### MSCF?（取自子主题 Commands for jitter injection › List of commands for jitter injection › MSCF  MSCF  -  Modulation Set ConFiguration）

```
MSCF? {"modulation_set_name"|ALL}, {"property"|ALL}
```

returns:

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### Parameters（取自子主题 Commands for jitter injection › List of commands for jitter injection › MSCF  MSCF  -  Modulation Set ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143671_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：modulation_set_name | Specifies the name of a modulation set that must have been defined with MSDF.

### Example（取自子主题 Commands for jitter injection › List of commands for jitter injection › MSCF  MSCF  -  Modulation Set ConFiguration）

```
> MSCF? "mod1",ALL
< MSCF "mod1",SHAPE,SINE
< MSCF "mod1",PERIOD,250
< MSCF "mod1",PHASE,180
< MSCF "mod1",AMPLITUDE,305
```

### Parameters（取自子主题 Commands for jitter injection › List of commands for jitter injection › MSDF  MSDF  -  Modulation Set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143675_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ms_set_name | In the command, this is the name of a new modulation set. In the query, it is a name of an existing modulation set. If you omit this parameter in …

### Example（取自子主题 Commands for jitter injection › List of commands for jitter injection › MSDF  MSDF  -  Modulation Set DeFinition）

```
> MSDF   "ms_set1",TIM
> MSDF   "ms_set2",TIM
> MSDF   "ms_set3",TIM

> MSDF?
< MSDF   "ms_set1",TIM
< MSDF   "ms_set2",TIM
< MSDF   "ms_set3",TIM

```

### Example（取自子主题 Commands for PRBS per pin tests and loopback tests › Overview of pseudo random bit sequences）

The following example shows a Fibonacci and a Galois LFSR for the same connection polynomial 1 + x + x3 (which corresponds to the recurrence relation sn+3 = sn+2 + sn), and also the PRBSs that they create from the seed 001. The rightmost column displays the output sequence in both cases.

 !`Fibonacci and Galois LFSR`（raw: `../../../../raw/118399.png`）

Both LFSRs create basically the same periodic PRBS. But in order to generate the same sequence right from the start, they must be initialized with different seeds. If the seed of the Fibonacci LFSR is 100 (in the output order), the seed of the Galois LFRS must be 110 in the output order.

Observe that the period of the PRBS resulting from 1 + x + x3 is maximal: The LFSR assumes each of its 2^3 = 8 possible states except 000 before the same state is reached again.

It is also obvious that if any segment on, on+1, on+2 of the output sequence is taken as the seed of the Fibonacci LFSR in the order on+2, on+1, on, the resulting PRBS will be identical with the original output sequence from on onwards.

### Examples（取自子主题 Commands for PRBS per pin tests and loopback tests › Executing a pattern  ased SmartLoop test › Defining a compliance pattern for pattern  ased SmartLoop testing）

### Model file entry

```
IOCHANNEL
10101-10108: HW=PS9G, speed= 3600Mbps, smem = 112M, loopback = 6800Mbps
...
```

### Pin configuration

```
>  DFPN? (PortD)
<  DFPN 10101,"4",(Pin4)
<  DFPN 10105,"5",(Pin5)
```

### Equation set

```
EQNSET 1 "equation set 1"

DEFINES  PortD

SPECS
p      [ns]

compliance

TIMINGSET 1 "eq 1 ts 1"
period=1.5

PINS  Pin4
d1=0 #DU

PINS  Pin5
r1=16 #RU
```

### Pattern

```
>  SQLB? ALL,MAIN,(PortD)
<  SQLB "compl",MAIN,0,3,"wavetable 1",(PortD)
>  SQLA? ALL,ALL,ALL,(PortD)
<  SQLA LBL,"compl","PARA_MEM=HSER,PARA_MCTX=DEFAULT",(PortD)
<  SQLA LBL,"burst","PARA_MEM=NONE",(PortD)
>  SQPG? ALL,(PortD)
<  SQPG 0,STVA,,0,,(PortD)
<  SQPG 1,STSA,,,,(PortD)
<  SQPG 2,GENV,100501,,,(PortD)
<  SQPG 3,STOP,,,,(PortD)
<  SQPG 4,CALL,,"compl",,(PortD)
<  SQPG 5,BEND,,,,(PortD)
```

Note that the compliance pattern `compl` comprises 100501 vectors. This is possible because channels 10101 through 10104 and 10105 through 10108 are all licensed for SmartLoop™ but only 10101 and 10105 are associated with a pin.

### Syntax（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › LBMD  -  LoopBack MoDe）

LBMD? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"|PRM}, {(pinlist)}

returns:

LBMD {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"|PRM}, {lpbk_mode}, {(pinlist)}

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118445_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. The maximum number is determined by the command WSUS, WSUS? - (Waveform Set…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example 1（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › LBMD  -  LoopBack MoDe）

```
> LBMD? PRM,(@)
< LBMD 101,LOOP_OFF,,(pin1,pin2)
> SPRM 103,1,1,1
> LBMD? PRM,(@)
< LBMD 103,LOOP_I,2,(pin1)
< LBMD 103,LOOP_O,8,(pin2)
```

### Example 2（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › LBMD  -  LoopBack MoDe）

```
> LBMD? "lpbk_1",(@)
< LBMD "lpbk_1",LOOP_O,(pin1,pin2)
```

This example queries a wavetable.

### Syntax（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › LBRT  -  LoopBack RouTing）

```
LBRT? {(pinlist)}
```

returns:

```
LBRT {(pin1)}, {(pin2)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118447_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：pinlist | Specifies the pins for which the partner pin is to be retrieved.

### Example（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › LBRT  -  LoopBack RouTing）

```
> LBRT? (@)
< LBRT (pin1),(pin2)
< LBRT (pin2),(pin1)
```

### PRCF（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRCF  PRCF  -  Pseudo Random bit sequence ConFiguration）

```
PRCF {"PRBS_set_name"|PRM}, {property}, {"property_value"}, {(pinlist)}
```

### PRCF?（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRCF  PRCF  -  Pseudo Random bit sequence ConFiguration）

```
PRCF? {"PRBS_set_name"|ALL|PRM}, {property|ALL}, {(pinlist)}
```

returns:

```
PRCF {"PRBS_set_name"}, {property}, {"property_value"}, {(pinlist)}
```

### Parameters（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRCF  PRCF  -  Pseudo Random bit sequence ConFiguration）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118218_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：PRBS_set_name | Specifies the name of a PRBS set that must have been defined with PRDF.

### Example（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRCF  PRCF  -  Pseudo Random bit sequence ConFiguration）

```
> PRCF? "PRBS_1",ALL,(Pin1)
< PRCF "PRBS_1",POLYNOMIAL,"101",(Pin1)
< PRCF "PRBS_1",SEED,"100",(Pin1)
```

This example defines 1 + x1 + x3 as the connection polynomial, and 100 as the initial segment for Pin1. This is the example which is also used in `Overview of pseudo random bit sequences`（raw: `02.06.17.01_Overview_of_pseudo_random_bit_sequences.md`）.

### PRDF（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRDF  PRDF  -  PRBS set DeFinition）

```
PRDF {"prbs_set_name"} [, "mode_context"]
```

### PRDF?（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRDF  PRDF  -  PRBS set DeFinition）

```
PRDF? ["prbs_set_name"]
```

returns:

```
PRDF {"prbs_set_name"} [, "mode_context"]
```

### Parameters（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRDF  PRDF  -  PRBS set DeFinition）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118422_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：prbs_set_name | In the command, this is the name of a new PRBS set. In the query, it is a name of an existing PRBS set. If you omit this parameter in the query,…

### Example（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRDF  PRDF  -  PRBS set DeFinition）

```
> PRDF   "prbs_set1"
> PRDF   "prbs_set2"
> PRDF   "prbs_set3"
```

```
> PRDF?
< PRDF   "prbs_set1"
< PRDF   "prbs_set2"
< PRDF   "prbs_set3"
```

### Syntax（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRMD  -  PRBS MoDe）

```
PRMD? {wvf_set|"wavetable_name"|specset_id|"multi_port_spec"|PRM}, {(pinlist)}
```

returns:

```
PRMD {wvf_set|"wavetable_name"|specset_id|"multi_port_spec"|PRM}, {prbs_mode}, [x_mode], {(pinlist)}
```

### Parameters（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRMD  -  PRBS MoDe）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118425_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 3 列。
> 首行（上游原文）：wvf_set | Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. The maximum number is determined by the command WSUS, WSUS? - (Waveform Set…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example 1（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRMD  -  PRBS MoDe）

```
> PRMD? PRM,(@)
< PRMD 101,PRBS_OFF,,(pin1,pin2)
> SPRM 103,1,1,1
> PRMD? PRM,(@)
< PRMD 103,PRBS_I,2,(pin1)
< PRMD 103,PRBS_O,8,(pin2)
```

### Example 2（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRMD  -  PRBS MoDe）

```
> PRMD? "prbs_2",(@)
< PRMD "prbs_2",PRBS_O,4,(pin1,pin2)
```

This example queries a wavetable.

### PRPR（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRPR  PRPR  -  PRBS PRimary set）

PRPR {"prbs_set_name"|DEFAULT}

### PRPR?（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRPR  PRPR  -  PRBS PRimary set）

PRPR?

returns:

```
PRPR {"prbs_set_name"}
```

### Parameters（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRPR  PRPR  -  PRBS PRimary set）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118421_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：prbs_set_name | Specifies the name of an existing PRBS set. If you specify "", the defaults will be restored.

### Example（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRPR  PRPR  -  PRBS PRimary set）

```
> PRPR   "PRBS_set"
```

### Syntax（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRUD -  PRBS set UnDefine）

PRUD {"prbs_set_name"|ALL}

### Parameters（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRUD -  PRBS set UnDefine）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/118424_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：prbs_set_name | Specifies the name of an existing PRBS set.

### Example（取自子主题 Commands for PRBS per pin tests and loopback tests › List of commands for PRBS per pin and loopback tests › PRUD -  PRBS set UnDefine）

```
> PRUD   "prbs_set1"
```

### ASWE（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › ASWE  ASWE  -  Auto SWing Enable）

```
ASWE {waveform_set|specset_id}, {enable_status}
```

### ASWE?（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › ASWE  ASWE  -  Auto SWing Enable）

```
ASWE? {waveform_set|specset_id}
```

returns:

```
ASWE {waveform_set|specset_id}, {enable_status}
```

### Parameters（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › ASWE  ASWE  -  Auto SWing Enable）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98486_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：waveform_set | Specifies the number of a waveform set for non-equation based testing. Enter PRM for the Primary Waveform Set, ALL for all waveform sets, or an i…
> 表内引用（1 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）

### Example（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › ASWE  ASWE  -  Auto SWing Enable）

```
ASWE 1,ON
```

This example enables the automatic swing adjustment for waveform set 1.

### ASWM（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › ASWM  ASWM  -  Auto SWing Mode）

```
ASWM {command}, {mode}
```

### ASWM?（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › ASWM  ASWM  -  Auto SWing Mode）

```
ASWM?
```

returns:

```
ASWM {command}, {mode}
```

### Parameters（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › ASWM  ASWM  -  Auto SWing Mode）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98487_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：command | This parameter is used to set the specified mode:

### Example（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › ASWM  ASWM  -  Auto SWing Mode）

```
ASWM SET,AUTO
```

This example sets the swing adjustment mode AUTO.

### FXDL（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › FXDL  FXDL  -  FiXture DeLay）

```
FXDL {channel}, {fixture_delay}
```

### FXDL?（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › FXDL  FXDL  -  FiXture DeLay）

```
FXDL? {channel}
```

returns:

```
FXDL {channel}, {fixture_delay}
```

### Parameters（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › FXDL  FXDL  -  FiXture DeLay）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98609_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：channel | The test system channel number of the digital channel. This is a five digit field. See DFPN, DFPN? - (DeFine Pin Name) for the number. You can type AL…
> 表内引用（1 条，供检索）：`DFPN, DFPN? - (DeFine Pin Name)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）

### Example（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › FXDL  FXDL  -  FiXture DeLay）

```
FXDL 10101,2.5
```

This example sets the fixture delay of channel 10101 to 2.5 ns.

### PADS（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › PADS  PADS  -  Pin Attributes Definition String）

```
PADS [mode], {definition_string}, [drv_adj], [rec_adj], {(pinlist)}
```

### PADS?（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › PADS  PADS  -  Pin Attributes Definition String）

```
PADS? [mode], {(pinlist)}
```

returns:

```
PADS [mode], {definition_string}, [drv_adj], [rec_adj], {(pinlist)}
```

### Parameters（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › PADS  PADS  -  Pin Attributes Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98679_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：mode | Currently not used.

### Example（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › PADS  PADS  -  Pin Attributes Definition String）

```
> PADS ,"d1:0.1 d2:0.2 d3:0.3 d4:0.1 d5:0.2 d6:0.3 d7:0.1 d8:0.2",2,,(clk)

> PADS? ,(@)
< PADS ,"d1:0.1 d2:0.2 d3:0.3 d4:0.1 r1:0.1 r2:0.2 r3:0.3 r4:0.1",,-1,(io)
< PADS ,"d1:0.1 d2:0.2 d3:0.3 d4:0.1 d5:0.2 d6:0.3 d7:0.1 d8:0.2",2,,(clk)
```

### PTDS（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › PTDS  PTDS  -  Pin attributes Tweaking Definition String）

```
PTDS {channelNo}, [EBT_specifier], {set_specifier}, {timing_set}, [tweaking_set], [mode], {definition_string}
```

### PTDS?（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › PTDS  PTDS  -  Pin attributes Tweaking Definition String）

```
PTDS? {channelNo}, [EBT_specifier], {set_specifier}, {timing_set}, [tweaking_set], [mode]
```

returns:

```
PTDS {channelNo}, [EBT_specifier], {set_specifier}, {timing_set}, [tweaking_set], [mode], {definition_string}
```

### Parameters（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › PTDS  PTDS  -  Pin attributes Tweaking Definition String）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98713_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 3 列。
> 首行（上游原文）：channelNo | This is a five digit field which defines the channel to which the pin is connected. See also the command DFPN, DFPN? - (DeFine Pin Name) for this pa…
> 表内引用（1 条，供检索）：`DFPN, DFPN? - (DeFine Pin Name)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）

### Example（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › PTDS  PTDS  -  Pin attributes Tweaking Definition String）

```
PTDS 10812,0,4,5,,1,1,"d1:2,d2:0.003, d8:5, r1:-1, r2:-2"
PTDS? 10101,,all,all,,
```

The following example defines pin attributes for timing sets of the multi-port specification spec_port_1_port_2.

```
> PTDS 10101,,"spec_port_1_port_2",1,,,"d1:1 d3:3"
> PTDS 10101,,"spec_port_1_port_2",2,,,"d1:2 d2:3"
> PTDS? 10101,,"spec_port_1_port_2",ALL,,
< PTDS 10101,,"spec_port_1_port_2",1,,,"d1:1 d3:3"
< PTDS 10101,,"spec_port_1_port_2",2,,,"d1:2 d2:3"
```

### SATR（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › SATR  SATR  -  System ATtRibutes）

SATR {comm_rec_delay}

### SATR?（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › SATR  SATR  -  System ATtRibutes）

```
SATR?
```

returns:

```
SATR {comm_rec_delay}
```

### Parameters（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › SATR  SATR  -  System ATtRibutes）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98727_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：comm_rec_delay | The common receiver delay represents the adjustment to the round-trip delay between the drivers and receivers. The delay is in [ns] and must be…

### Example（取自子主题 Calibration and Attributes Commands › List of calibration and attributes commands › SATR  SATR  -  System ATtRibutes）

```
SATR 20
```

This example sets the common receiver delay to 20 ns.

<!-- 语法节 end -->

## 是什么

**这一页是「firmware 命令」的总入口。**
它自己不定义任何命令——**它做两件事**：分流（该不该用 firmware 命令）
和分门别类（18 个类别）。

### 一、先用什么、最后才用什么：一条明确的优先级

原文把这个放在最前面，是一段**排序建议**，不是一个「也可以」：

> 「Firmware commands are used for **low level control of the test system**. In general it is
> recommended to use instead
> - **SmartRDI**
> - **Testmethod API**
> when possible, **and in that order**, and **only work with firmware commands if none of these
> meets your need**.」

**顺序是有意义的**，`and in that order` 明说了：

| 优先级 | 用什么 |
|---|---|
| 1 | **[[smartrdi]]** |
| 2 | **Testmethod API** |
| 3 | **firmware 命令**（前两个都满足不了时） |

**所以本页的定位是「退路」，不是起点。**

### 二、什么情况下退路是必须的：pin 特定的测试结果

原文给了一个**具体的例子**，而这条例子恰好是本页存在的理由：

> 「Examples for when firmware commands can be necessary are **queries** like
> **`CHFA?` - (CHannel FAil flag)** or **`CHER?` - (CHeck ERrors)** which can be used to
> **get pin specific test results**.」

**两个特征值得注意：**

| 特征 | 说明 |
|---|---|
| **是 `?` 结尾的查询** | `CHFA?` / `CHER?` ——**`?` 表示这是问句，不是设置** |
| **拿的是 pin 特定的结果** | `pin specific test results` ——**这正是前两级覆盖不到的地方** |

> **括号里的展开读法**：`CHFA?` = `CHannel FAil flag`，`CHER?` = `CHeck ERrors`。
> **原文用「大写字母组词」的方式解释缩写**——这是本语料里解释命令名的固定写法。

### 三、⚠️ 全页最要紧的一条限制：只看当前 focus 的那个 site

> 「**Any firmware queries report setup and results for the site currently in focus only.**」

**只说了一遍、只有一行，但它是本页的边界条件。**

**这条限制的后果**（本页按它的字面意思列出，**（推断）**部分已标注）：

- **multiport / multisite 下，一次查询只回答一个 site 的情况**——想拿全部 site 的结果，
  **得自己逐个 site 换 focus 再查**（**（推断）**：「只看 focus」的字面推论，
  **原文没有明说怎么遍历**）。
- **它和 [[site-focus-required-before-command]] 是同一件事的两面**：
  那一页讲「某条命令要求先聚焦 site」（**约束侧**），
  本页讲「查询只报当前聚焦 site 的结果」（**行为侧**）。
- **`Any` 和 `queries` 两个词的范围**：原文写的是 **`Any firmware queries`**——
  **限定在「查询」这一类**。**设置类的命令是否也受这条限制，原文没说。**

### 四、18 个类别

原文的 `Subtopics` 就是它的目录，**18 个类别**。本页按原文顺序列，**每类的具体命令本页都没读**：

| # | 类别 | 本页对它的了解 |
|---|---|---|
| 1 | `Introduction to firmware commands` | **只知道标题** |
| 2 | `Commands in alphabetical order` | **只知道标题**（**按字母序的总清单**） |
| 3 | `Pin configuration setup commands` | **只知道标题** |
| 4 | `Routing Setup Commands` | **只知道标题** |
| 5 | `Level Setup Commands` | **只知道标题** |
| 6 | `Timing Setup Commands` | **只知道标题**（[[timing-setup-commands]] 是它在 wiki 里的页） |
| 7 | `Vector Setup Commands` | **只知道标题** |
| 8 | `Relays and Control Commands` | **只知道标题** |
| 9 | `AC Testing Commands` | **只知道标题** |
| 10 | `DC Measurement Commands` | **只知道标题** |
| 11 | `Test Result Commands` | **只知道标题** |
| 12 | `Utility Line Commands` | **只知道标题** |
| 13 | `Commands for the TMU per pin` | **只知道标题** |
| 14 | `Commands for Processing Results of Source Synchronous Testing` | **只知道标题** |
| 15 | `Commands for the protocol engine per pin` | **只知道标题** |
| 16 | `Commands for jitter injection` | **只知道标题** |
| 17 | `Commands for PRBS per pin tests and loopback tests` | **只知道标题** |
| 18 | `Calibration and Attributes Commands` | **只知道标题** |

**这张清单本身有一个结构信息**：**第 3–12 类是按「测试资源/阶段」分的**
（pin 配置、routing、level、timing、vector、relay、AC、DC、结果、utility line），
**第 13–18 类是按「特殊硬件能力」分的**（TMU、source synchronous、protocol engine、
jitter、PRBS、calibration）。**（推断）**：依据是两组标题的命名方式不同，
**原文没有把这层分组说出来。**

### 五、语法节：**63,000 行，本 wiki 里最大的一页**

`## 语法 / 参数` 一节有 **63,395 行**——因为脚本沿 `Subtopics` 往下抽，
把 18 个类别里的命令语法和例子**逐字**抄了进来。

**这一页的读法**：

- **散文这一节（就是你现在读的）只讲「该不该用、分几类」**；
- **真正的命令表和参数在脚本那一节**，**逐字来自 18 篇本页没读的子主题**；
- **要找某条命令，用 `Commands in alphabetical order` 那一支的字母序**
  （第 2 类），而不是从头翻。

## 典型用法

**原文这篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**，
也没有任何步骤。**本页按原文能支撑的内容列三条：**

**1. 该不该用 firmware 命令（原文唯一一条决策建议）**：

```
要用某个能力
  ├─ SmartRDI 能做吗？      → 能就用它
  ├─ Testmethod API 能做吗？ → 能就用它
  └─ 都不行？               → 才用 firmware 命令
```

**2. 什么时候会走到第 3 步**：原文给的例子是**要拿 pin 特定的测试结果**时的查询
（`CHFA?`、`CHER?`）。

**3. 用查询前必须先确认一件事**：**当前 focus 的 site 是不是你要问的那个 site**
——因为 `Any firmware queries report setup and results for the site currently in focus only`。
**multisite 下这一条决定了你要不要先换 focus。**

## 和谁有关

- [[smartrdi]] — **原文推荐的第一顺位**：能用它就别用 firmware 命令
- [[testmethod]] — **原文推荐的第二顺位**（Testmethod API）；
  **注意原文用的是 `Testmethod API`，而第三顺位才是 firmware 命令**
- [[pin]] — **本页唯一给了例子的场景是「pin 特定的测试结果」**
- [[site-focus-required-before-command]] — **本页那条焦点限制的另一面**：
  那页讲「命令要求先聚焦」，本页讲「查询只报聚焦的那个」
- [[timing-setup-commands]] — **18 类里第 6 类的 wiki 页**；本页是它的父页
- [[flag]] / [[alphabetical-list-of-flags]] — **firmware 命令和 flag 是两套不同的东西**；
  本页讲的是命令，flag 有自己的一张总表
- [[utility-line-assignments]] — 第 12 类 `Utility Line Commands` 在 wiki 里的落点之一
- [[dc-test-programming]] / [[results]] / [[run]] — 第 10、11 类命令各自服务的阶段页
- `Introduction to firmware commands` / `Commands in alphabetical order` /
  `Pin configuration setup commands` / `Routing Setup Commands` / `Level Setup Commands` /
  `Vector Setup Commands` / `Relays and Control Commands` / `AC Testing Commands` /
  `DC Measurement Commands` / `Test Result Commands` / `Utility Line Commands` /
  `Commands for the TMU per pin` / `Commands for Processing Results of Source Synchronous
  Testing` / `Commands for the protocol engine per pin` / `Commands for jitter injection` /
  `Commands for PRBS per pin tests and loopback tests` / `Calibration and Attributes Commands`
  （**均未建**）— **本页 `Subtopics` 的 18 篇，本页一篇没读**；
  **语法节里那 63,000 行就是它们被脚本抽出来的片段**

## 版本

**本文档没有 `## Functional changes` 段。**

（这是一条事实，不是缺陷：原文主文档只有 `Subtopics` 加四段正文，
**没有任何版本条目，也没有 `## Related information` 段**。）

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06_Command_Reference.md`

**本页没做的**：

- **`Subtopics` 的 18 篇一篇没读**——**这是本 wiki 里最大的一个缺口**。
  本页主文档只有不到 2.4 KB，**而 18 个类别下面覆盖的是整个 firmware 命令集**。
  本页能给的**只有「该不该用」和「分几类」，没有一条命令的用法**。
- **`## 语法 / 参数` 一节里的 63,395 行，本页一个字都没有验证过。**
  它们由脚本从 18 篇子主题逐字抄出，**本页没读那些子主题**，
  所以无法判断**命令清单是否完整、`Commands in alphabetical order` 和其余 17 个类别
  之间有没有重复收录、同一命令在别处的例子有没有被漏掉**。
  （**⚠️ 重复收录的可能性是本页特别提出来的一条**：第 2 类是「按字母序」，
  其余 17 类是按资源/能力分的——**同一命令很可能同时出现在第 2 类和某一类里**，
  而这会让语法节里出现两份同样的内容。**本页没有核实，只把疑点列出来。**）
- **`CHFA?` / `CHER?` 两条命令本身没读**——**本页只有原文给的一句话解释**
  （`get pin specific test results`），**返回什么、怎么调、有没有参数，本页都不知道**。
- **「怎么遍历多个 site」原文没写，本页也不知道**——只列出「只看 focus」这条限制
  及其字面推论。
- **设置类命令是否也受「只看 focus」限制，原文没说**，本页照实标为未知。
- **图零张**（原文这篇没有图）。
- **原文没有 `## Procedure` / `## Before you begin` / `## What to do next` /
  `## Related information`**——四个都没有。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`SmartRDI` 和 `Testmethod API` 两条建议是「裸列表」**
> ——原文是 `it is recommended to use instead` 后面直接跟两条 markdown 链接，
> **句子的语法是断的**（`use instead` 后面缺宾语，链接成了列表项）。
> ② **`Testmethod API` 的大小写和本 wiki 其它页不一致**——
> 这里写 `Testmethod API`，而 `Subtopics` 和别处有 `Test Method`（带空格、分开写）的写法。
> ③ **四条 `Subtopics` 之后的正文段落，第一段以空格开头**
> （` Firmware commands are used for low level control…`），
> **和同一页里其它段落（`Any firmware queries…`）的对齐方式不同。**
> ④ **`Calibration and Attributes Commands` 是 18 类里的最后一类**，
> 而它和前面 17 类的命名方式不同（前面都是 `… Commands`，它是 `… and … Commands`）
> ——**这一条只是命名观察，不构成问题，本页列出来备查。**

`verified: doc-only`
