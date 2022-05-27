import os
import time

import requests
import yaml

"""
需要使用绝对路径，不能使用相对路径（下面注释掉的路径），否则执行all.py时会报错找不到文件。
或者修改all.py执行文件的working directory到对应的路径下，才能执行成功
"""
yaml_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/date/"
# yaml_dir = os.path.abspath(os.path.dirname(os.getcwd())) + "/date/"


class YamlUtil:

    # 读取extract.yml文件
    def read_extract_yaml(self, key):
        with open(os.getcwd() + "/extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    # 写入extract.yml文件
    def write_extract_yaml(self, data):
        with open(os.getcwd() + "/extract.yml", mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
            # allow_unicode使用这个参数允许显示中文

    # 清除extract.yml文件
    def clear_extract_yaml(self):
        with open(os.getcwd() + "/extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    # 读取测试用例yml文件
    def read_testcase_yaml(self, yaml_name):
        with open(yaml_dir + yaml_name, mode='r', encoding='utf-8') as f:
            # with open(os.getcwd() + '/' + yaml_name, mode='r', encoding='utf-8') as f:

            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value
