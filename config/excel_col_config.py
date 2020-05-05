#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: excel_col_config.py
# time: 2020/5/5 8:24
# tool: PyCharm 
# desc: 

class ReadExcelColConfig:
    InterfaceName = 1          # 接口名称
    Uri = 2                    # 接口地址
    Method = 3                 # 请求方法
    OutputStyle = 4            # 请求体输出格式

    ValidBody = 5              # 合法请求体
    IsRun = 6                  # 是否自动编写该字段的测试用例

    ParamName = 7              # 参数名称
    ParamType = 8              # 参数类型
    JsonPathExpression = 9     # ParamName的值在ValidBody值中的jsonpath表达式
    MinBound = 10              # 最小边界值
    MaxBound = 11              # 最大边界值
    IsRequired = 12            # 必填项校验
    OptionValue = 13           # 选项值
    IsArray = 14               # 选项值是否为数组
    FormatCheck = 15           # 格式校验



class WriteExcelColConfig:
    CaseName = 1                 # 用例名称
    CaseId = 2                   # 用例编号
    Precondition = 3             # 前置条件
    TestStep = 4                 # 测试步骤
    Expectation = 5              # 期望结果
    TestData = 6                 # 测试数据
    Level = 7                    # 优先级
    Tag = 8                      # 标签
