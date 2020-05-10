#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: main.py
# time: 2020/5/5 8:43
# tool: PyCharm 
# desc:
import shutil
import time
from data.get_data_from_excel import GetData
from data.write_case_logic import WriteCaseLogic
from data.write_data_to_excel import WriteCaseToExcel


class RunMain:
    def __init__(self,read_file_name:str,write_file_name:str):
        self.get_data = GetData(read_file_name)
        self.write_file_name = write_file_name
        self.write_to_cell = WriteCaseToExcel(self.write_file_name)

    def run_main(self):
        sheet_lines = self.get_data.get_sheet_lines()
        com_dict = {}

        # 写测试用例标题行
        self.write_to_cell.write_title('层级关系','特性名称','特性编号','是否为特性',
                                       '用例名称','用例编号','测试阶段','用例级别',
                                       '预置条件','测试步骤','预期结果','用例说明',
                                       '用例标签','用例活动名','测试类型')

        self.write_to_cell.write_title('Depth','Feature_Name','Feature_Number','isFeature',
                                       'Testcase_Name','Testcase_Number','Testcase_Stage',
                                       'Testcase_Level','Testcase_PrepareCondition',
                                       'Testcase_TestSteps','Testcase_Excepted','Testcase_Remark',
                                       'Testcase_Tags','Testcase_Activity','Testcase_TestType')

        for row_num in range(2, sheet_lines + 1):

            feature_name = self.get_data.get_feature_name(row_num)
            if feature_name:
                depth = self.get_data.get_depth(row_num)
                feature_number = self.get_data.get_feature_number(row_num)
                is_feature = self.get_data.get_is_feature(row_num)
                self.write_to_cell.write_feature(depth,feature_name,feature_number,is_feature)
            else:

                interface_name = self.get_data.get_interface_name(row_num)
                uri = self.get_data.get_uri(row_num)
                method = self.get_data.get_method(row_num)

                if interface_name and uri and method:
                    # 获取公共信息保存到字典
                    com_dict = {'interface_name': None, 'uri': None, 'method': None,
                                'output_style': None, 'valid_body': None, 'is_run': None}

                    com_dict['interface_name'] = interface_name
                    com_dict['uri'] = uri
                    com_dict['method'] = method
                    com_dict['output_style'] = self.get_data.get_output_style(row_num)

                    com_dict['valid_body'] = self.get_data.get_valid_body(row_num)
                    com_dict['is_run'] = self.get_data.get_is_run(row_num)
                else:
                    # 获取每个字段的信息保存到字典中
                    param_dict = {'valid_body': None,'is_run': None,'param_name': None,
                                  'param_type': None,'json_path_expression': None,
                                  'min_bound': None, 'max_bound': None,
                                  'is_required': None, 'option_value': None,
                                  'is_array': None, 'format_check': None}
                    # 此处读取文件json

                    param_dict['valid_body'] = self.get_data.get_valid_body(row_num)
                    param_dict['is_run'] = self.get_data.get_is_run(row_num)

                    param_dict['param_name'] = self.get_data.get_param_name(row_num)
                    param_dict['param_type'] = self.get_data.get_param_type(row_num)
                    param_dict['json_path_expr'] = self.get_data.get_json_path_expr(row_num)
                    param_dict['min_bound'] = self.get_data.get_min_bound(row_num)
                    param_dict['max_bound'] = self.get_data.get_max_bound(row_num)
                    param_dict['is_required'] = self.get_data.get_is_required(row_num)
                    param_dict['option_value'] = self.get_data.get_option_value(row_num)
                    param_dict['is_array'] = self.get_data.get_is_array(row_num)
                    param_dict['format_check'] = self.get_data.get_format_check(row_num)
                    print(com_dict,param_dict)

                    # agt = AutoGenerateCasesLogic(com_dict,param_dict,self.write_to_cell)
                    # agt.auto_write_test_case()
                    wcl = WriteCaseLogic(com_dict,param_dict,self.write_to_cell)
                    wcl.auto_write_test_case()


        # 将运行结果进行备份到指定目录下
        backup_full_path = 'D:/BackupCase/Case_{0}.xlsx'.format(time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())))
        shutil.copy(self.write_file_name,backup_full_path)


if __name__ == "__main__":
    m = RunMain('./excel_file/interface_analysis_document.xlsx','./excel_file/case.xlsx')
    m.run_main()


