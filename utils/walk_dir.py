#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 田佳志
# email: tianjiazhi@huawei.com
# file: walk_dir.py
# time: 2020/5/11 22:00
# tool: PyCharm 
# desc:
import base64
import os


def image_convert_base64(source_file_name, new_file_name):
    new_file_name = new_file_name + '.base64'
    with open(source_file_name, 'rb') as f:
        base_code = base64.b64encode(f.read()).decode()
    f.close()
    with open(new_file_name, 'w') as f:
        f.write(base_code)
    f.close()





def walk_dir(transactions_name,read_path,save_path='.'):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for root, dirs, files in os.walk(read_path, topdown=True):

        for dir in dirs:# 在指定目录下创建和读取的源目录相同的文件夹
            path = os.path.join(root, dir)
            new_path = path.replace(read_path,save_path)
            if not os.path.exists(new_path):
                os.makedirs(new_path)

        for file in files:
            source_file_name = os.path.join(root, file)
            new_file_name = source_file_name.replace(read_path,save_path)
            if transactions_name == 'image_convert_base64':
                image_convert_base64(source_file_name,new_file_name)


walk_dir('image_convert_base64','D:\TestResult')