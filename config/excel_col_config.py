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
    # CaseName = 1                 # 用例名称
    # CaseId = 2                   # 用例编号
    # Precondition = 3             # 前置条件
    # TestStep = 4                 # 测试步骤
    # Expectation = 5              # 期望结果
    # TestData = 6                 # 测试数据
    # Level = 7                    # 优先级
    # Tag = 8                      # 标签

    Depth = 1                           # 层级关系
    Feature_Name = 2                    # 特性名称
    Feature_Number = 3                  # 特性编号
    isFeature = 4                       # 是否为特性

    Testcase_Name = 5                   # 用例名称
    Testcase_Number = 6                 # 用例编号
    Testcase_Stage = 7                  # 测试阶段
    Testcase_Level = 8                  # 用例级别
    Testcase_PrepareCondition = 9       # 预置条件
    Testcase_TestSteps = 10             # 测试步骤
    Testcase_Excepted = 11              # 预期结果
    Testcase_Remark = 12                # 用例说明
    Testcase_Tags = 13                  # 用例标签
    Testcase_Activity = 14              # 用例活动名
    Testcase_TestType = 15              # 测试类型



