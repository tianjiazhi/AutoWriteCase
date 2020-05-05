#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: auto_generate_case_logic.py
# time: 2020/5/5 8:49
# tool: PyCharm 
# desc:
from utils.process_data import *

class AutoGenerateCasesLogic:

    def __init__(self,com_dict:dict,param_dict:dict,write_to_cell):

        self.interface_name = com_dict.get('interface_name')
        self.uri = com_dict.get('uri')
        self.method = com_dict.get('method')
        self.valid_body = com_dict.get('valid_body')
        self.output_style = com_dict.get('output_style')
        self.all_is_run = com_dict.get('is_run')
        ############################################################
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


    def auto_write_test_case(self):
        """根据单个参数生成用例名称"""
        if self.format_check: # 格式校验
            self.__process_format_check()

        # 有效性校验【即必填项和选填项在不传参时的校验】
        self.process_is_required()
        # 对枚举类型的字段进行测试用例设计
        self.process_is_array()
        # 根据参数的类型的不填分别进行用例设计
        if self.param_type.lower() == 'string':
            self.process_str()
        elif self.param_type.lower() == 'int':
            self.process_int()
        elif self.param_type.lower() == 'float':
            self.process_float()
        elif self.param_type.lower() == 'date':
            self.process_date()


    # 根据字符串类型生成用例名称：
    def process_str(self):
        if not self.min_bound:
            error = "%s接口%s参数的最小边界值不能置空,请填写后重试！" % (self.interface_name, self.param_name)
            print(error)
            return

        if not self.min_bound.isdigit():
            error = "%s接口%s参数的最小边界值不是正整数类型的值,请修改后重试！" % (self.interface_name, self.param_name)
            print(error)
            return

        if not self.max_bound:
            error = "%s接口%s参数的最大边界值不能置空,请填写后重试！" % (self.interface_name, self.param_name)
            print(error)
            return

        if not self.max_bound.isdigit():
            error = "%s接口%s参数的最大边界值不是正整数类型的值,请修改后重试！" % (self.interface_name, self.param_name)
            print(error)
            return

        if int(self.min_bound) > int(self.max_bound):
            error = "%s接口%s参数的最小边界值大于最大边界值,请修改后重试！" % (self.interface_name, self.param_name)
            print(error)
            return

        # 合法的用例
        self.__test_case_str_min_bound_sub1()
        self.__test_case_str_max_bound_add1()

        if self.min_bound == self.max_bound:
            self.__test_case_str_bound_value()
        else:
            self.__test_case_str_min_bound()
            self.__test_case_str_max_bound()


    # 根据整型生成用例名称:
    def process_int(self):
        print('用例名称: %s 参数为字符串' % self.param_name)


    # 根据时间类型生成用例名称:
    def process_date(self):
        print('用例名称: %s 参数为字符串' % self.param_name)

    # 根据浮点型生成用例名称:
    def process_float(self):
        print('用例名称: %s 参数为字符串' % self.param_name)
        print('用例名称: %s 参数为整型' % self.param_name)
        print('用例名称: %s 参数浮点型' % self.param_name)


    def process_is_required(self):
        if self.is_required == True:
            self.__test_case_is_required_check()
        else:
            self.__test_case_not_required_check()



    def process_is_array(self):
        if self.option_value:
            if self.is_array == True:
                for index, value in enumerate(self.option_value.split(',')):
                    self.__test_case_is_array_exist(index,value)
                self.__test_case_is_array_inexist()
            else:
                self.__test_case_not_array_true()
                self.__test_case_not_array_false()

    ###################################################################################################################

    def __test_case_str_min_bound_sub1(self):
        case_name = '验证[%s]参数的长度为[%d]个字符(最小边界-1)' % (self.param_name, int(self.min_bound) - 1)  # 测试通过
        case_id = '%s_%s_%s_str-min-bound-sub1' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "我是最小边界值-1"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "非法请求"  # 测试通过
        level = "level 1"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)

    def __test_case_str_max_bound_add1(self):
        case_name = '验证[%s]参数的长度为[%d]个字符(最大边界+1)' % (self.param_name, int(self.max_bound) + 1)  # 测试通过
        case_id = '%s_%s_%s_str-max-bound-add1' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "我是最小边界值+1"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "非法请求"  # 测试通过
        level = "level 1"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)

    def __test_case_str_bound_value(self):
        case_name = '验证[%s]参数的长度为[%d]个字符(边界相等)' % (self.param_name, int(self.max_bound))  # 测试通过
        case_id = '%s_%s_%s_str-bound-value' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "我是边界值"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "合法请求"  # 测试通过
        level = "level 0"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)

    def __test_case_str_min_bound(self):
        case_name = '验证[%s]参数的长度为[%d]个字符(最小边界)' % (self.param_name, int(self.min_bound))  # 测试通过
        case_id = '%s_%s_%s_str-min-bound' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "我是最小边界值"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "合法请求"  # 测试通过
        level = "level 0"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)

    def __test_case_str_max_bound(self):
        case_name = '验证[%s]参数的长度为[%d]个字符(最大边界)' % (self.param_name, int(self.max_bound))  # 测试通过
        case_id = '%s_%s_%s_str-max-bound' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "我是最大边界值"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "合法请求"  # 测试通过
        level = "level 0"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)

    ####################################################################################################################


    def __test_case_is_required_check(self):
        case_name = '验证必填参数[%s]的值为空' %self.param_name # 测试通过
        case_id = '%s_%s_%s_is-required-null' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "我是必填参数的非空校验"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "非法请求"  # 测试通过
        level = "level 1"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)


    def __test_case_not_required_check(self):
        case_name = '验证选填参数[%s]的值为空' %self.param_name # 测试通过
        case_id = '%s_%s_%s_not-required-null' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "我是选填参数的非空校验"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "合法请求"  # 测试通过
        level = "level 0"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)

    ###################################################################################################################


    def __test_case_not_array_true(self):
        case_name = '验证[%s]参数值是[%s]' % (self.param_name, self.option_value)  # 测试通过
        case_id = '%s_%s_%s_not-array-true' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=%s\n② 对[%s]接口发送请求。" % (
        self.param_name, self.option_value, self.interface_name)
        update_value = "参数等于已定义的值"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "合法请求"    # 测试通过
        level = "level 0"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)



    def __test_case_not_array_false(self):
        case_name = '验证[%s]参数值不是[%s]' % (self.param_name, self.option_value)  # 测试通过
        case_id = '%s_%s_%s_not-array-false' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "参数不等于已定义的值"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "非法请求"  # 测试通过
        level = "level 1"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)



    def __test_case_is_array_exist(self,index,value):
        case_name = '验证[%s]参数取值为[%s]' % (self.param_name, value)
        case_id = '%s_%s_%s_is-array-exist-%s' % (
        self.method, self.uri.split('/')[-1], self.param_name, str(index))  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=%s\n② 对[%s]接口发送请求。" % (
        self.param_name, str(value), self.interface_name)
        update_value = "参数等于已定义的值"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "合法请求"  # 测试通过
        level = "level 0"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)


    def __test_case_is_array_inexist(self):
        case_name = '验证[%s]参数值不在可选项数组[%s]中' % (self.param_name, self.option_value)
        case_id = '%s_%s_%s_is-array-inexist' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "参数不等于已定义的值"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "非法请求"  # 测试通过
        level = "level 1"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)

    ###################################################################################################################

    def __process_format_check(self):
        case_name = '验证[%s]参数传入错误的[%s]' % (self.param_name, self.format_check)  # 测试通过
        case_id = '%s_%s_%s_error-format' % (self.method, self.uri.split('/')[-1], self.param_name)  # 测试通过
        precondition = "① [%s]接口服务已部署完成。" % self.interface_name  # 测试通过
        case_step = "① 按照备注栏中的测试数据传入参数,校验参数取值:\n  %s=\n② 对[%s]接口发送请求。" % (self.param_name, self.interface_name)
        update_value = "参数传入错误的格式"
        test_data = self.__get_test_data(self.valid_body,self.json_path_expr,update_value)
        tag = "非法请求"  # 测试通过
        level = "level 1"  # 测试通过
        self._write_to_cell.write_value_to_cell(case_name, case_id, precondition, case_step, test_data, tag, level)


    def __get_test_data(self,json_data:str,json_path_expr:str,update_value):
        convert_dict = json_convert_dict(json_data)

        get_value = get_value_to_json_path(convert_dict, json_path_expr)
        print("参数[%s]修改前的值为：%s"%(self.param_name,get_value))

        convert_json_path = convert_json_path_expr(json_path_expr)
        print("转换后的json表达式：%s"%convert_json_path)

        update_data = update_json_data(convert_dict, convert_json_path, update_value)
        print("更新后的数据是:%s"%update_data)

        test_data = dict_convert_json(update_data)

        return test_data
