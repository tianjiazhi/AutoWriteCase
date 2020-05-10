#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: write_case_logic.py
# time: 2020/5/9 7:28
# tool: PyCharm 
# desc:

from utils.operation_json import ReaderJson
from data.case_document_defind import *

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

    def process_int(self):
        pass

    def process_float(self):
        pass

    def process_list(self):
        pass

    def public_write_case_filed_value(self,case_name,case_id,level,excepted,tag,update_value):
        # 公共不变的
        case_step = test_steps(self.param_name, self.interface_name, update_value)
        test_data = get_test_data(self.valid_body,self.json_path_expr,update_value)
        precondition = case_precondition(self.interface_name)
        stage = case_stage(1)
        activity = test_activity(0)
        test_type = test_types(0)
        self._write_to_cell.write_value_to_cell(case_name,case_id,stage,level,precondition,case_step,excepted,test_data,tag,activity,test_type)

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

#######################################################################################################################
    def process_string(self):
        # 获取某个字段的初始值
        initial_value = get_value_to_json_path(self.valid_body, self.json_path_expr)
        print(initial_value)

        if self.is_required is True:
            # '验证必填参数的非空校验--非法' -->测试通过
            self.__test_case_is_required_check()
        else:
            # '验证选填参数的非空校验--合法' --> 测试通过
            self.__test_case_not_required_check()

        if not self.option_value:
            # 对非法输入的数据进行拦截
            if not self.min_bound:
                error = "输入错误：{}接口的{}参数【最小边界值】不可为空,请填写后重试！".format(self.interface_name, self.param_name)
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
                # '验证最大边界+1--非法'  -->测试通过
                self.__test_case_str_max_bound_add1(initial_value)
            else:
                # '验证最大边界+1--非法'  -->测试通过
                self.__test_case_str_max_bound_add1(initial_value)
                # '验证最小边界-1--非法'  -->测试通过
                self.__test_case_str_min_bound_sub1(initial_value)


            if self.min_bound != self.max_bound and self.min_bound == "0":
                # '验证最大边界--合法' --> 测试通过
                self.__test_case_str_max_bound(initial_value)
            elif self.min_bound != self.max_bound and self.min_bound != "0":
                # '验证最小边界--合法' --> 测试通过
                self.__test_case_str_min_bound(initial_value)
                # '验证最大边界--合法' --> 测试通过
                self.__test_case_str_max_bound(initial_value)
            elif self.min_bound == self.max_bound and self.min_bound != "0":
                # '最大最小边界相等--合法'--># 测试通过
                self.__test_case_str_bound_value(initial_value)

        else:
            if self.is_array == True:
                for index, value in enumerate(self.option_value.split(';')):
                    # '验证传入已定义的值--合法' --> 测试通过
                    self.__test_case_is_array_exist(index, value,initial_value)
                # '验证传入已定义的值--非法' --> 测试通过
                self.__test_case_is_array_inexist(initial_value)
            else:
                # '验证传入已定义的值--合法' --> 测试通过
                self.__test_case_not_array_true(initial_value)
                # '验证传入已定义的值--非法' --> 测试通过
                self.__test_case_not_array_false(initial_value)


########################################################################################################################
    def __test_case_is_required_check(self):
        case_name = '验证必填参数[%s]的值为空' %self.param_name # 测试通过
        case_id = get_case_id(self.method, self.uri, self.param_name) + 'is-required-null'
        level = case_level(1)  # 用例级别
        tag = case_tag(1)  # 用例标签
        excepted = test_excepted()  # 期望结果
        update_value = ""
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)


    def __test_case_not_required_check(self):
        case_name = '验证选填参数[%s]的值为空' %self.param_name # 测试通过
        case_id = get_case_id(self.method, self.uri, self.param_name) + 'not-required-null'
        level = case_level(0)  # 用例级别
        tag = case_tag(0)  # 用例标签
        excepted = test_excepted("200")  # 期望结果

        update_value = ""
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)


########################################################################################################################

    def __test_case_str_min_bound_sub1(self,initial_value):
        case_name = '验证[%s]参数的长度为[%d]个字符(最小边界-1)' % (self.param_name, int(self.min_bound) - 1)  # 测试通过
        case_id = get_case_id(self.method, self.uri,self.param_name) + 'str-min-bound-sub1'
        level = case_level(1)         # 用例级别
        tag = case_tag(1)             # 用例标签
        excepted = test_excepted()    # 期望结果

        update_value = "我是最小边界值-1"
        self.public_write_case_filed_value(case_name,case_id,level,excepted,tag,update_value)


    def __test_case_str_max_bound_add1(self,initial_value):
        case_name = '验证[%s]参数的长度为[%d]个字符(最大边界+1)' % (self.param_name, int(self.max_bound) + 1)  # 测试通过
        case_id = get_case_id(self.method, self.uri, self.param_name) + 'str-max-bound-add1'
        level = case_level(2)  # 用例级别
        tag = case_tag(1)  # 用例标签
        excepted = test_excepted()  # 期望结果

        update_value = "我是最大边界值-1"
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)


    def __test_case_str_bound_value(self,initial_value):
        case_name = '验证[%s]参数的长度为[%d]个字符(最大最小边界相等)' % (self.param_name, int(self.max_bound))  # 测试通过

        case_id = get_case_id(self.method, self.uri, self.param_name) + 'str-bound-value'
        level = case_level(0)  # 用例级别
        tag = case_tag(0)  # 用例标签
        excepted = test_excepted("200")  # 期望结果

        update_value = "我是边界值"
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)


    def __test_case_str_min_bound(self,initial_value):
        case_name = '验证[%s]参数的长度为[%d]个字符(最小边界)' % (self.param_name, int(self.min_bound))  # 测试通过
        case_id = get_case_id(self.method, self.uri, self.param_name) + 'str-min-bound'
        level = case_level(0)  # 用例级别
        tag = case_tag(0)  # 用例标签
        excepted = test_excepted("200")  # 期望结果

        update_value = "我是最小边界值"
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)


    def __test_case_str_max_bound(self,initial_value):
        case_name = '验证[%s]参数的长度为[%d]个字符(最大边界)' % (self.param_name, int(self.max_bound))  # 测试通过
        case_id = get_case_id(self.method, self.uri, self.param_name) + 'str-max-bound'
        level = case_level(0)  # 用例级别
        tag = case_tag(0)  # 用例标签
        excepted = test_excepted("200")  # 期望结果

        update_value = "我是最大边界值"
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)


########################################################################################################################

    def __test_case_not_array_true(self,initial_value):
        case_name = '验证[%s]参数值是[%s]' % (self.param_name, self.option_value)  # 测试通过
        case_id = get_case_id(self.method, self.uri, self.param_name) + 'not-array-true'
        level = case_level(0)  # 用例级别
        tag = case_tag(0)  # 用例标签
        excepted = test_excepted("200")   # 期望结果

        update_value = "参数等于已定义的值"
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)


    def __test_case_not_array_false(self,initial_value):
        case_name = '验证[%s]参数值不是[%s]' % (self.param_name, self.option_value)  # 测试通过
        case_id = get_case_id(self.method, self.uri, self.param_name) + 'not-array-false'
        level = case_level(1)  # 用例级别
        tag = case_tag(1)      # 用例标签
        excepted = test_excepted()  # 期望结果

        update_value = "参数等于未定义的值"
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)


    def __test_case_is_array_exist(self,index,value,initial_value):
        case_name = '验证[%s]参数取值为[%s]' % (self.param_name, value)

        case_id = get_case_id(self.method, self.uri, self.param_name) + 'is-array-exist-%s'%str(index)
        level = case_level(0)  # 用例级别
        tag = case_tag(0)  # 用例标签
        excepted = test_excepted("200")  # 期望结果

        update_value = "参数等于已定义的值"
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)


    def __test_case_is_array_inexist(self,initial_value):
        case_name = '验证[%s]参数值不在可选项数组[%s]中' % (self.param_name, self.option_value)
        case_id = get_case_id(self.method, self.uri, self.param_name) + 'is-array-inexist'
        level = case_level(1)  # 用例级别
        tag = case_tag(1)  # 用例标签
        excepted = test_excepted()  # 期望结果

        update_value = "参数等于未被定义的值"
        self.public_write_case_filed_value(case_name, case_id, level, excepted, tag, update_value)
