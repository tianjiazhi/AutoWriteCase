#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: excel_col_config.py
# time: 2020/5/5 8:24
# tool: PyCharm 
# desc: 

class ReadExcelColConfig:
    Depth = 1                  # 层级关系
    Feature_Name = 2           # 特性名称
    Feature_Number = 3         # 特性编号
    isFeature = 4              # 是否为特性

    InterfaceName = 5          # 接口名称
    Uri = 6                    # 接口地址
    Method = 7                 # 请求方法
    OutputStyle = 8            # 请求体输出格式

    ValidBody = 9              # 合法请求体
    IsRun = 10                 # 是否自动编写该字段的测试用例

    ParamName = 11             # 参数名称
    ParamType = 12             # 参数类型
    JsonPathExpression = 13    # ParamName的值在ValidBody值中的jsonpath表达式
    MinBound = 14              # 最小边界值
    MaxBound = 15              # 最大边界值
    IsRequired = 16            # 必填项校验
    OptionValue = 17           # 选项值
    IsArray = 18               # 选项值是否为数组
    FormatCheck = 19           # 格式校验



class WriteExcelColConfig:

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



