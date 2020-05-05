#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: process_data.py
# time: 2020/5/5 8:34
# tool: PyCharm 
# desc: 

import json
from jsonpath_rw import parse


def convert_json_path_expr(json_path_expr:str)->str:
    split_list = json_path_expr.split('[')
    length = len(split_list) - 1
    lists = []

    for index, value in enumerate(split_list):
        if index != 0:
            value = '[' + value
        if not value.endswith('.') and index != length:
            value = value + '.'
        lists.append(value)
    list_convert_str = "".join(lists)
    return list_convert_str


def get_value_to_json_path(json_obj:dict,json_path_expr:str):
    try:
        json_path_expr = parse(json_path_expr)
        var_value = [match.value for match in json_path_expr.find(json_obj)][0]
        return var_value
    except AttributeError as e:
        error = "json_path表达式语法错误，请检查后重试！错误详细信息：%s"%e
        print(error)
    except IndexError as e:
        error = "未提取到结果导致列表为空，请检查后重试！错误详细信息：%s"%e
        print(error)
    except Exception as e:
        error = "发生未知错误，请检查后重试！错误详细信息：%s"%e
        print(error)




def update_json_data(json_obj:dict,key_expr:str,value):

    key = key_expr.split(".")
    key_length = len(key)
    get_json_data = json_obj
    counter = 0
    while counter < key_length:
        key_value = key[counter]
        if key_value.startswith('[') and key_value.endswith(']'):
            key_value = eval(key_value[1:-1])
        if counter + 1 == key_length:
            get_json_data[key_value] = value
        else:
            get_json_data = get_json_data[key_value]
        counter = counter + 1
    return json_obj


def dict_to_str(dictionary:dict)->str:
    """
    功能描述：将字典类型的数据转换成为字符串
    :param dictionary: 待处理的字典类型的数据。 {'size': '10', 'page': '1'}
    :return string: 经过处理后的字符串类型的数据，返回格式：size=10&page=1
    """
    string = ''
    list_data = []
    for k, v in dictionary.items():
        if v is True:
            v = 'true'
        elif v is False:
            v = 'false'
        elif v is None:
            v = 'null'
        else:
            pass
        list_data.append("{0}={1}&".format(k, v))

    for index,value in enumerate(list_data):
        string = string + value
    string = string[0:-1]   # 截取最后一个取消&符号
    print("<class 'str'> 打印转换后的字符串数据：{0}".format(string))
    return string


def json_convert_dict(json_obj:str)->dict:
    return json.loads(json_obj)


def dict_convert_json(dict_obj:dict)->str:
    return json.dumps(dict_obj,ensure_ascii=False,indent=2)


if __name__ == '__main__':
    json_obj = """
    {
        "firstName": "John", 
        "lastName": "doe", 
        "age": 26, 
        "is_adult": true,
        "address": {
            "streetAddress": "naist street", 
            "city": "Nara", 
            "postalCode": "630-0192"
        }, 
        "phoneNumbers": [
            {
                "type": "iPhone", 
                "number": "0123-4567-8888"
            }, 
            {
                "type": "home", 
                "number": "0123-4567-8910"
            }
        ]
    }"""

    json_path_expr = 'phoneNumbers[0]'

    dic = json_convert_dict(json_obj)
    print(dic)

    get_value = get_value_to_json_path(dic,json_path_expr)
    print(get_value)


    # 使用转换后的json_path修改对应字段的值
    convert_json_path = convert_json_path_expr(json_path_expr)
    print(convert_json_path)

    # 使用转换后的json_path修改对应字段的值
    update_data = update_json_data(dic,convert_json_path,"我是修改后的值")
    print(update_data)

    json_data = dict_convert_json(update_data)
    print(json_data)


    d = {'size': 1, 'page': True,'p1': False,'name': None,'sex': '男生',"type": ""}
    t = dict_to_str(d)