#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: get_data_from_excel.py
# time: 2020/5/5 8:37
# tool: PyCharm 
# desc:


from config.excel_col_config import ReadExcelColConfig
from utils.operation_excel import ReaderExcel

class GetData:
    def __init__(self,file_name):
        self._operation_excel = ReaderExcel(file_name)
        self._get_column_num = ReadExcelColConfig()


    def get_sheet_lines(self):
        """获取当前sheet页的总行数"""
        return self._operation_excel.get_row_num()

    #################################################################

    def get_interface_name(self, x:int):
        """获取接口名称"""
        y = self._get_column_num.InterfaceName
        interface_name = self._operation_excel.get_cell_value(x, y)
        return interface_name


    def get_uri(self, x:int):
        """获取接口的Uri地址"""
        y = self._get_column_num.Uri
        uri = self._operation_excel.get_cell_value(x, y)
        return uri


    def get_method(self, x:int):
        """获取合法的请求体"""
        y = self._get_column_num.Method
        method = self._operation_excel.get_cell_value(x, y)
        return method


    def get_valid_body(self, x:int):
        """获取合法的请求体"""
        y = self._get_column_num.ValidBody
        valid_body = self._operation_excel.get_cell_value(x, y)
        return valid_body


    def get_output_style(self, x:int):
        """获取请求体的格式"""
        y = self._get_column_num.OutputStyle
        output_style = self._operation_excel.get_cell_value(x, y)
        return output_style


    def get_is_run(self, x:int):
        """获取case是否运行"""
        y = self._get_column_num.IsRun
        is_run = self._operation_excel.get_cell_value(x, y)
        if is_run and is_run.upper() == "YES":
            flag = True
        else:
            flag = False
        return flag





    #################################################################

    def get_param_name(self, x:int):
        """获取参数名称"""
        y = self._get_column_num.ParamName
        param_name = self._operation_excel.get_cell_value(x, y)
        return param_name


    def get_param_type(self, x:int):
        """获取参数类型"""
        y = self._get_column_num.ParamType
        param_type = self._operation_excel.get_cell_value(x, y)
        return param_type

    def get_json_path_expr(self, x:int):
        """获取jsonpath_表达式"""
        y = self._get_column_num.JsonPathExpression
        json_path_expression = self._operation_excel.get_cell_value(x, y)
        return json_path_expression



    def get_min_bound(self, x:int):
        """获取参数最小边界"""
        y = self._get_column_num.MinBound
        min_bound = str(self._operation_excel.get_cell_value(x, y))
        return min_bound


    def get_max_bound(self, x:int):
        """获取参数最大边界"""
        y = self._get_column_num.MaxBound
        max_bound = str(self._operation_excel.get_cell_value(x, y))
        return max_bound


    def get_is_required(self, x:int):
        """获取参数是否为必填字段"""
        y = self._get_column_num.IsRequired
        is_required = self._operation_excel.get_cell_value(x, y)
        if is_required and is_required.upper() == "YES":
            flag = True
        else:
            flag = False
        return flag


    def get_option_value(self, x:int):
        """获取选项值"""
        y = self._get_column_num.OptionValue
        option_value = self._operation_excel.get_cell_value(x, y)
        return option_value


    def get_is_array(self, x:int):
        """获取选项值是否为数组"""
        y = self._get_column_num.IsArray
        is_array = self._operation_excel.get_cell_value(x, y)
        if is_array and is_array.upper() == "YES":
            flag = True
        else:
            flag = False
        return flag


    def get_format_check(self, x:int):
        """获取格式校验值"""
        y = self._get_column_num.FormatCheck
        format_check = self._operation_excel.get_cell_value(x, y)
        return format_check
