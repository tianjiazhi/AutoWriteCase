#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: write_case_logic.py
# time: 2020/5/9 7:28
# tool: PyCharm 
# desc:
from utils.operation_json import ReaderJson


class WriteCaseLogic:

    def __init__(self,com_dict:dict,param_dict:dict,write_to_cell):

        self.interface_name = com_dict.get('interface_name')
        self.uri = com_dict.get('uri')
        self.method = com_dict.get('method')
        self.output_style = com_dict.get('output_style')

        ############################################################
        all_is_run = com_dict.get('is_run')
        a_is_run = param_dict.get('is_run')
        if all_is_run is False and a_is_run is True:
            self.is_run = a_is_run
        else:
            self.is_run = all_is_run
        ############################################################
        a_valid_body = param_dict.get('valid_body')
        all_valid_body = com_dict.get('valid_body')
        if a_valid_body:
            valid_body = a_valid_body
        else:
            valid_body = all_valid_body
        try:
            self.valid_body = ReaderJson(valid_body).read_data()
        except FileNotFoundError as e:
            print("填写的json文件路径错误,请检查后重试！具体错误信息:{}".format(e))
        except Exception as e:
            print("未知错误，请排查错误。具体错误信息:{}".format(e))

            ############################################################

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

    def auto_write_test_case(self):
        """根据参数的类型的不填分别进行用例设计"""
        if not self.param_name:
            error = "{}接口的[参数名称]不可为空,请填写后重试！".format(self.interface_name)
            print(error)
            return

        if not self.param_name:
            error = "{}接口的{}参数[参数类型]不可为空,请填写后重试！".format(self.interface_name, self.param_name)
            print(error)
            return

        if not self.json_path_expr:
            error = "{}接口的{}参数[JsonPathExpression]不可为空,请填写后重试！".format(self.interface_name, self.param_name)
            print(error)
            return

        if self.param_type.lower() == 'string':
            self.process_string()
        elif self.param_type.lower() == 'int':
            self.process_int()
        elif self.param_type.lower() == 'float':
            self.process_float()
        elif self.param_type.lower() == 'list':
            self.process_list()


    def process_string(self):

        if self.is_required == True:
            case_name = '验证必填参数[%s]的值为""--非法' % self.param_name  # 测试通过
            print(case_name)
        else:
            case_name = '验证选填参数[%s]的值为""--合法' % self.param_name  # 测试通过
            print(case_name)

        # 对非法输入的数据进行拦截
        if not self.min_bound:
            error = "输入错误：{}接口的{}参数【最小边界值】不可为空,请填写后重试！".format(self.interface_name,self.param_name)
            print(error)
            return

        if not self.max_bound:
            error = "输入错误：{}接口的{}参数【最大边界值】不可为空,请填写后重试！".format(self.interface_name, self.param_name)
            print(error)
            return

        if not self.min_bound.isdigit():
            error = "输入错误：%s接口的%s参数的最小边界值不是正整数类型的值,请修改后重试！" % (self.interface_name, self.param_name)
            print(error)
            return

        if not self.max_bound.isdigit():
            error = "输入错误：%s接口的%s参数的最大边界值不是正整数类型的值,请修改后重试！" % (self.interface_name, self.param_name)
            print(error)
            return

        if eval(self.min_bound) > eval(self.max_bound):
            error = "输入错误：%s接口的%s参数的最小边界值大于最大边界值,请修改后重试！" % (self.interface_name, self.param_name)
            print(error)
            return

        if self.min_bound == self.max_bound == "0":
            error = "输入错误：%s接口的%s参数的最小边界值和最大边界值不能同时为0,请修改后重试！" % (self.interface_name, self.param_name)
            print(error)
            return


        if self.min_bound in ['0','1']:
            case_name = '验证[%s]参数的长度为[%d]个字符(最大边界+1)--非法' % (self.param_name, int(self.max_bound) + 1)  # 测试通过
            print(case_name)
        else:
            case_name = '验证[%s]参数的长度为[%d]个字符(最大边界+1)--非法' % (self.param_name, int(self.max_bound) + 1)  # 测试通过
            print(case_name)
            case_name = '验证[%s]参数的长度为[%d]个字符(最小边界-1)--非法' % (self.param_name, int(self.min_bound) - 1)  # 测试通过
            print(case_name)

        if self.min_bound != self.max_bound and self.min_bound == "0":
            case_name = '验证[%s]参数的长度为[%d]个字符(最大边界)--合法' % (self.param_name, int(self.max_bound))  # 测试通过
            print(case_name)
        elif self.min_bound != self.max_bound and self.min_bound != "0":
            case_name = '验证[%s]参数的长度为[%d]个字符(最小边界)--合法' % (self.param_name, int(self.min_bound))  # 测试通过
            print(case_name)
            case_name = '验证[%s]参数的长度为[%d]个字符(最大边界)--合法' % (self.param_name, int(self.max_bound))  # 测试通过
            print(case_name)
        elif self.min_bound == self.max_bound and self.min_bound != "0":
            case_name = '验证[%s]参数的长度为[%d]个字符(边界相等)--合法' % (self.param_name, int(self.max_bound))  # 测试通过
            print(case_name)


    def process_int(self):
        pass

    def process_float(self):
        pass

    def process_list(self):
        pass




