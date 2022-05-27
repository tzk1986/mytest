# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:locust_test.py
@Time:2022/5/18 13:23
说明：
"""

import locust
import logging

from locust import task, User, between, constant, constant_pacing, constant_throughput

logger = logging.getLogger(__name__)


@locust.task
class MyUser(locust.HttpUser):
    @task
    def my_task(self):
        res = self.client.get("http://127.0.0.1:8000/admin/")
        assert res.status_code == 200

    # between 最小值和最大值之间的随机时间
    # wait_time = between(0.5, 10)
    # constant 在固定时间内
    # wait_time = constant(3)
    # constant_throughput 每秒运行X次的自适应时间
    # wait_time = constant_throughput(0.1)  # 每10秒执行一次
    # constant_pacing 每X秒运行一次的自适应时间（是constant_throughput的数学倒数）
    wait_time = constant_pacing(10)  # 每10秒执行一次


# 可以直接执行上面的脚本，或者使用下面的tasks来指定执行的函数
# class LocustTest(locust.HttpUser):
#     wait_time = locust.between(1, 2)
#     tasks = [MyUser.my_task]

"""
---------以下为网上收集的样例------


from locust import HttpUser, task, between, tag
import requests,sys
from moka_login import Login
from env import ENV
import logging

sys.path.append('../')
requests.packages.urllib3.disable_warnings()
class MyTaskCase(HttpUser):
    wait_time = between(1, 5)
    logs = make_logs

    def on_start(self):
        '''login'''
        try:
            #pre环境测试账号
            Login(event='pre', username='wayne@wayne.com', password='Qq1234567!', s=self.client).login()
        except AttributeError:
            raise TypeError (F'登陆失败')
    @task(1)
    def set_test(self):
        self.client.get(url='https://www.baidu.com/')
    @task(2)
    # @tag("leave_1")
    def get_id(self):
        """获取用户id"""

        names = 'wayne'
        event = 'pre'
        json_data = '["' + names + '"]'  # 替换取到字典中的参数值，下一步进行赋值
        data = {
            "rosterType": "1",
            "page": 1,
            "pageSize": 15,
            "params": [{
                "fieldName": "like",
                "biz": "like",
                "type": 1,
                "values": eval(json_data)
            }],
            "includeNoUsedDepartment": False,
            "bus": "20",
            "loginType": "10"
        }

        url = ENV.get(event).get('urls').get('host') +'/api/core/v1/hr/roster/rosterList?bus=20'
        # self.client.request_name = 'get_idid'  # 设置请求名
        logging.info('start')
        logging.log(level=2,msg='hahaha')
        with self.client.post(url,json=data, verify=False, catch_response=True,name='hahah') as response:
            if response.status_code== 200:
                response.success()
            else:
                # .error('接口调用错误{response}')
                response.failure('接口调用错误')
if __name__ == '__main__':
    import os
    import webbrowser
    web_host = '127.0.0.1'
    web_port='8095'
    url = 'http://'+web_host+':'+web_port
    webbrowser.get('Chrome').open(url, new=1, autoraise=True)
    os.system(F" locust -f load_pre.py  --web-auth 'wsg1':'123'   --web-host={web_host} --web-port {web_port} ")

    #locust执行命令：locust -f load_test.py  --web-host=127.0.0.1 --web-port 9001
    # --web-auth 'wayne':'123'  设置用户名和密码
    #--print-stats 在控制台打印统计信息
    # --only-summary  只打印汇总统计信息  停止后显示
    # --logfile=locust.log --loglevel=INFO 1>run.log 2>&1  生成日志文件 集成grafana和infuxDB时使用

"""




