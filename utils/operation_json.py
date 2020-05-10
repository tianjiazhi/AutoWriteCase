# coding = utf-8
"""
@Time      : 2020/2/7 0007 17:54
@Author    : YunFan
@File      : operation_json.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""
import json

class WriterJson:
    def __init__(self, file_path = None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = "../config/demo.json"


    def write_data(self,context):
        """将数据写到指定json文件中"""
        with open(self.file_path,"w+") as file:
            file.write(context)
        file.close()



class ReaderJson:
    def __init__(self, file_path = None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = "../config/global_var_config.json"
        self.data = self.read_data()


    def read_data(self):
        with open(self.file_path,encoding='utf-8') as f:
            data = json.load(f)
            return data


    def get_key_words(self, key=None):
        """获取json文件中的数据"""
        if key:
            return self.data[key]
        else:
            return self.data


if __name__ == '__main__':
    reader_json = ReaderJson("../test_data/json_data/test.json")
    res = reader_json.get_key_words()
    print(res)