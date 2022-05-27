# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:allure_history.py
@Time:2022/5/16 18:58
说明：测试报告趋势用文件
"""
import os
import json
from time import time
import ast

# 生成Allure报告
# BASEDIR 是项目位置
BASEDIR = "/Users/tangzhongkai/PycharmProjects/mytest"
# ALLURE_DIR是allure报告存放位置
ALLURE_DIR = "/Users/tangzhongkai/PycharmProjects/mytest/temp"
# ALLURE_PATH 是根据当前时间戳生成allure报告
ALLURE_PATH = os.path.join(ALLURE_DIR, str(int(time())))
command = f'pytest {BASEDIR} -s  --alluredir={ALLURE_PATH}'
os.system(command)

# 对生成的Allure报告进行进一步演进（生成一个相对独立的报告静态工程）
# ALLURE_PLUS_DIR 是存放要生成的报告
ALLURE_PLUS_DIR = "/Users/tangzhongkai/PycharmProjects/mytest/reports"
# buildOrder 是表示以构建次数为文件夹名称
buildOrder =
command = f"allure generate {ALLURE_PATH} -o {os.path.join(ALLURE_PLUS_DIR,str(buildOrder))} --clean"
os.system(command)

def get_dirname():
    hostory_file = os.path.join(ALLURE_PLUS_DIR, "history.json")
    if os.path.exists(hostory_file):
        with open(hostory_file) as f:
            li = eval(f.read())
        # 根据构建次数进行排序，从大到小
        li.sort(key=lambda x: x['buildOrder'], reverse=True)
        # 返回下一次的构建次数，所以要在排序后的历史数据中的buildOrder+1
        return li[0]["buildOrder"]+1, li
    else:
        # 首次进行生成报告，肯定会进到这一步，先创建history.json,然后返回构建次数1（代表首次）
        with open(hostory_file, "w") as f:
            pass
        return 1, None

def update_trend_data(dirname, old_data: list):
    """
    dirname：构建次数
    old_data：备份的数据
    update_trend_data(get_dirname())
    """
    WIDGETS_DIR = os.path.join(ALLURE_PLUS_DIR, f"{str(dirname)}/widgets")
    # 读取最新生成的history-trend.json数据
    with open(os.path.join(WIDGETS_DIR, "history-trend.json")) as f:
        data = f.read()

    new_data = eval(data)
    if old_data is not None:
        new_data[0]["buildOrder"] = old_data[0]["buildOrder"]+1
    else:
        old_data = []
        new_data[0]["buildOrder"] = 1
    # 给最新生成的数据添加reportUrl key，reportUrl要根据自己的实际情况更改
    new_data[0]["reportUrl"] = f"{allure_url}/{dirname}/index.html"
    # 把最新的数据，插入到备份数据列表首位
    old_data.insert(0, new_data[0])
    # 把所有生成的报告中的history-trend.json都更新成新备份的数据old_data，这样的话，点击历史趋势图就可以实现新老报告切换
    for i in range(1, dirname+1):
        with open(os.path.join(ALLURE_PLUS_DIR, f"{str(i)}/widgets/history-trend.json"), "w+") as f:
            f.write(json.dumps(old_data))
    # 把数据备份到history.json
    hostory_file = os.path.join(ALLURE_PLUS_DIR, "history.json")
    with open(hostory_file, "w+") as f:
        f.write(json.dumps(old_data))
    return old_data, new_data[0]["reportUrl"]

ALLURE_PATH = os.path.join(ALLURE_DIR, str(int(time())))
command = f'pytest {BASEDIR} -s  --alluredir={ALLURE_PATH}'
os.system(command)
# 先调用get_dirname()，获取到这次需要构建的次数
buildOrder, old_data = get_dirname()
# 再执行命令行
command = f"allure generate {ALLURE_PATH} -o {os.path.join(ALLURE_PLUS_DIR,str(buildOrder))} --clean"
os.system(command)
# 执行完毕后再调用update_trend_data()
all_data,reportUrl = update_trend_data(buildOrder, old_data)


# # 需要执行的测试脚本的路径
# test_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/testcase"
# # 需要生成的xml的路径
# allure_xml_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/reports"
# # 需要生成测试报告的路径
# allure_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/reports"
#
#
# # 获取下一个文件夹的名称，以及最近一个趋势的数据
# def get_dir():
#     print("allure_path", allure_path)
#     # 判断之前是否生成过报告
#     first_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/reports/1"
#     if os.path.exists(first_path):
#         all_result_dir = os.listdir(allure_path)
#         # 这个地方要注意，如果是mac，listdir获取到一个.DS_store的文件，使用下方的sort会报错，因而要先all_result_dir中将它remove掉
#         all_result_dir.sort(key=int)
#
#         # 取出最近一次执行的历史趋势的json
#         history_file = os.path.join(allure_path, str(int(all_result_dir[-1])), 'widgets', 'history-trend.json')
#         with open(history_file) as f:
#         data = f.read()
#         # 将下一次要生成的文件夹序号以及最新的历史趋势数据返回
#         return int(all_result_dir[-1]) + 1, data
#     else:
#     # 如果之前没有生成过，就创建一个文件夹
#         os.makedirs(os.path.join(allure_path, '1'))
#         return 1, None
#
#
# # 获取最新生成的趋势数据，这个数据里其实只有本次的结果，没有历史的结果
# def update_new_single(buildOrder):
#     new_single_file = os.path.join(allure_path, str(buildOrder), 'widgets', 'history-trend.json')
#     with open(new_single_file, 'r+') as f:
#         # data1 = f.read()
#         data = json.load(f)
#         # 写入本次是第几次执行、测试报告的路径
#         data[0]["buildOrder"] = int(buildOrder)
#         data[0]['reportUrl'] = f'http://localhost:63343/ttx_ofs_autoapi/allure_report/{str(buildOrder)}/index.html'
#     with open(new_single_file, 'w+') as f:
#         json.dump(data, f)
#
#
# # 重写新生成的history-trend.json文件，用历史+本次=最新
# def update_file(buildOrder):
#     old_data = os.path.join(allure_path, str(int(buildOrder) - 1), 'widgets', 'history-trend.json')
#     new_data = os.path.join(allure_path, str(int(buildOrder)), 'widgets', 'history-trend.json')
#     with open(old_data) as f:
#         old = json.load(f)
#         dict = []
#         for i in range(len(old)):
#             dict.append(old[i])
#         print(dict)
#     with open(new_data) as f:
#         r = f.read()
#         new_list = ast.literal_eval(r)
#         for i in range(len(dict)):
#             new_list.append(dict[i])
#     with open(new_data, 'w') as f:
#         json.dump(new_list, f)
#
#
# # 调用
# def test_allure():
#     print(allure_path)
#     buildOrder, old_data = get_dir()
#     # 先使用command生成xml文件
#     command = f'pytest {test_path} -s --alluredir={os.path.join(allure_xml_path, str(buildOrder))}'
#     os.system(command)
#     # 再使用command1由xml生成json文件的测试报告
#     command1 = f'allure generate {os.path.join(allure_xml_path, str(buildOrder))} -o {os.path.join(allure_path, str(buildOrder))} --clean'
#     print(command1)
#     os.system(command1)
#     update_new_single(buildOrder)
#     if buildOrder != 1:
#         update_file(buildOrder)
