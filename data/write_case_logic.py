#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: write_case_logic.py
# time: 2020/5/9 7:28
# tool: PyCharm 
# desc: 


class WriteCaseLogic:

    def __init__(self,com_dict:dict,param_dict:dict,write_to_cell):

        self.interface_name = com_dict.get('interface_name')
        self.uri = com_dict.get('uri')
        self.method = com_dict.get('method')
        self.output_style = com_dict.get('output_style')

        self.valid_body = com_dict.get('valid_body')
        self.all_is_run = com_dict.get('is_run')
        ############################################################
        self.a_valid_body = com_dict.get('valid_body')
        self.a_is_run = param_dict.get('is_run')

        self.param_name = param_dict.get('param_name')
        self.param_type = param_dict.get('param_type')
        self.json_path_expr = param_dict.get('json_path_expr')
        self.min_bound = param_dict.get('min_bound')
        self.max_bound = param_dict.get('max_bound')
        self.is_required = param_dict.get('is_required')
        self.option_value = param_dict.get('option_value')
        self.is_array = param_dict.get('is_array')
        self.format_check = param_dict.get('format_check')

        self._write_to_cell = write_to_cell