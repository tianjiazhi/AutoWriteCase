#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: case_document_defind.py
# time: 2020/5/10 16:32
# tool: PyCharm 
# desc:
from utils.process_data import *


def case_stage(index:int):
    stage = ['Alpha','Beta','Gamma','Production']
    return stage[index]

def case_tag(index:int):
    tag = ['合法请求','非法请求']
    return tag[index]

def case_level(index:int):
    level = ['level 0','level 1','level 2','level 3','level 4']
    return level[index]

def test_types(index:int):
    type = ['API','未定义']
    return type[index]

def test_activity(index:int):
    activity = ['接口功能测试']
    return activity[index]

def test_excepted(status_code=""):
    return "①校验响应状态码:{}\n②校验响应体:".format(status_code)

def test_steps(param_name,interface_name,value):
    return "①按照备注栏中的测试数据传入参数,校验参数取值:\n {0}={2}\n②对[{1}]接口发送请求。" \
        .format(param_name,interface_name,value)

def case_precondition(interface_name):
    return "①[{0}]接口服务已部署完成。".format(interface_name)  # 测试通过

def get_case_id(method, uri,param_name):
    u = uri.split('/')[-1]
    com_case_id = '%s_%s_%s_' % (method, u, param_name)  # 测试通过
    return com_case_id

def get_test_data(convert_dict:dict,json_path_expr:str,update_value):

    convert_json_path = convert_json_path_expr(json_path_expr)
    # print("转换后的json表达式：%s"%convert_json_path)

    update_data = update_json_data(convert_dict, convert_json_path, update_value)
    # print("更新后的数据是:%s"%update_data)

    test_data = dict_convert_json(update_data)

    return test_data


######################################边界值##############################################

def get_min_bound_sub1_value(initial_value:str,min_bound:str,interface_name="", param_name=""):
    length = len(initial_value)
    if int(min_bound) > length:
        error = "%s接口的%s字段的合法值是%s个字符不能小于最小边界值%s,请重新填写后重试！"\
                % (interface_name, param_name, length, min_bound)
        print(error)
        return
    update_value = initial_value[0:int(min_bound) - 1]
    return update_value


def get_min_bound_value(initial_value: str, min_bound: str, interface_name="", param_name=""):
    length = len(initial_value)
    if int(min_bound) > length:
        error = "%s接口的%s字段的合法值是%s个字符不能小于最小边界值%s,请重新填写后重试！" \
                % (interface_name, param_name, length, min_bound)
        print(error)
        return
    update_value = initial_value[0:int(min_bound)]
    return update_value


def get_max_bound_value(initial_value: str, max_bound: str, interface_name="", param_name=""):
    length = len(initial_value)
    max = int(max_bound)
    if max < length:
        error = "%s接口的%s字段的合法值是%s个字符不能大于最大边界值%s,请重新填写后重试！" \
                % (interface_name, param_name, length, max_bound)
        print(error)
        return
    div_mod = list(divmod(max, length))
    update_value = initial_value * (div_mod[0]-1) + initial_value[0:div_mod[1]] + initial_value
    return update_value


def get_max_bound_add1_value(initial_value: str, max_bound: str, interface_name="", param_name=""):
    length = len(initial_value)
    max = int(max_bound)
    if max < length:
        error = "%s接口的%s字段的合法值是%s个字符不能大于最大边界值%s,请重新填写后重试！" \
                % (interface_name, param_name, length, max_bound)
        print(error)
        return
    div_mod = list(divmod(max, length)) # 商div_mod[0]和余数div_mod[1]
    update_value = initial_value * (div_mod[0]-1) + initial_value[0:div_mod[1] + 1] + initial_value
    return update_value


    # upper_index = []
    # lower_index = []
    # for index,value in enumerate(initial_value):
    #     if value.isupper():
    #         upper_index.append(index)
    #     elif value.islower():
    #         lower_index.append(index)
    #
    #
    # return upper_index,lower_index

if __name__ == "__main__":
    print(get_min_bound_sub1_value("我是合法的字符串aASsc","3","学生信息","name"))
    print(get_min_bound_value("我是合法的字符串aASsc","3","学生信息","name"))
    print(get_max_bound_value("我是合作坊","13","学生信息","name"))
    print(get_max_bound_add1_value("我是合作坊","13","学生信息","name"))