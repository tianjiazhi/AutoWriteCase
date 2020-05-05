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


    def __write_case_name(self,cell_value):
        column = self._column_config.CaseName
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_case_id(self,cell_value):
        column = self._column_config.CaseId
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_precondition(self,cell_value):
        column = self._column_config.Precondition
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_test_step(self,cell_value):
        column = self._column_config.TestStep
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_expectation(self,cell_value):
        column = self._column_config.Expectation
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_test_data(self,cell_value):
        column = self._column_config.TestData
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_tag(self,cell_value):
        column = self._column_config.Tag
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def __write_level(self,cell_value):
        column = self._column_config.Level
        self._write_excel.write_value_to_cell(self._line_num,column,cell_value)


    def write_value_to_cell(self,case_name,case_id,precondition,case_step,test_data,tag,level):
        self.__write_case_name(case_name)
        self.__write_case_id(case_id)
        self.__write_precondition(precondition)
        self.__write_test_step(case_step)
        self.__write_test_data(test_data)
        self.__write_tag(tag)
        self.__write_level(level)
        self.__switch_to_next_line()
