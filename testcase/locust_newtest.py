# -*- coding:utf-8 -*-
"""
@Author:tang
@File:locust_newtest.py
@Time:2022/5/27 14:03
说明：根据虫师视频讲解，编写样例，已进行了更新，HttpLocust不用，使用locust.HttpUser
"""
import locust
from locust import TaskSet, task


# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def baidu_page(self):
        self.client.get('/')


class WebsiteUser(locust.HttpUser):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
