#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: write_data_to_excel.py
# time: 2020/5/5 8:40
# tool: PyCharm 
# desc:

from config.excel_col_config import WriteExcelColConfig
from utils.operation_excel import WriteExcel


class WriteCaseToExcel:
    def __init__(self,file_name):
        self._write_excel = WriteExcel(file_name)
        self._column_config = WriteExcelColConfig()
        self._line_num = 1

    def __switch_to_next_line(self):
        self._line_num += 1


    def __write_depth(self,cell_value):
        column = self._column_config.Depth
        self._write_excel.write_value_to_cell(self._line_num, column, cell_value)


    def __write_feature_name(self,cell_value):
        column = self._column_config.Feature_Name
        self._write_excel.write_value_to_cell(self._line_num, column, cell_value)


    def __write_feature_number(self,cell_value):
        column = self._column_config.Feature_Number
        self._write_excel.write_value_to_cell(self._line_num, column, cell_value)


    def __write_is_feature(self,cell_value):
        column = self._column_config.isFeature
        self._write_excel.write_value_to_cell(self._line_num, column, cell_value)

    #############################################################################

    def __write_case_name(self,cell_value):
        column = self._column_config.Testcase_Name
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_case_number(self,cell_value):
        column = self._column_config.Testcase_Number
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_stage(self,cell_value):
        column = self._column_config.Testcase_Stage
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_level(self,cell_value):
        column = self._column_config.Testcase_Level
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_precondition(self,cell_value):
        column = self._column_config.Testcase_PrepareCondition
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_test_step(self,cell_value):
        column = self._column_config.Testcase_TestSteps
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_expectation(self,cell_value):
        column = self._column_config.Testcase_Excepted
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_test_remark(self,cell_value):
        column = self._column_config.Testcase_Remark
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_tag(self,cell_value):
        column = self._column_config.Testcase_Tags
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_activity(self,cell_value):
        column = self._column_config.Testcase_Activity
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_test_type(self,cell_value):
        column = self._column_config.Testcase_TestType
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)



    def write_title(self,depth,feature_name,feature_number,is_feature,
                    case_name, case_id, stage, level, precondition, case_steps,
                    excepted, test_data, tag, activity, test_type):

        self.__write_depth(depth)
        self.__write_feature_name(feature_name)
        self.__write_feature_number(feature_number)
        self.__write_is_feature(is_feature)

        self.__write_case_name(case_name)
        self.__write_case_number(case_id)
        self.__write_stage(stage)
        self.__write_level(level)
        self.__write_precondition(precondition)
        self.__write_test_step(case_steps)
        self.__write_expectation(excepted)
        self.__write_test_remark(test_data)
        self.__write_tag(tag)
        self.__write_activity(activity)
        self.__write_test_type(test_type)

        self.__switch_to_next_line()



    def write_feature(self,depth,feature_name,feature_number,is_feature):
        self.__write_depth(depth)
        self.__write_feature_name(feature_name)
        self.__write_feature_number(feature_number)
        self.__write_is_feature(is_feature)

        self.__switch_to_next_line()


    def write_value_to_cell(self,case_name,case_id,stage,level,precondition,case_steps,
                            excepted,test_data,tag,activity,test_type):
        self.__write_case_name(case_name)
        self.__write_case_number(case_id)
        self.__write_stage(stage)
        self.__write_level(level)
        self.__write_precondition(precondition)
        self.__write_test_step(case_steps)
        self.__write_expectation(excepted)
        self.__write_test_remark(test_data)
        self.__write_tag(tag)
        self.__write_activity(activity)
        self.__write_test_type(test_type)

        self.__switch_to_next_line()
