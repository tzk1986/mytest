# -*- coding:utf-8 -*-
"""
@Author:tang
@File:fixture_test.py
@Time:2022/5/25 11:19
说明：调用接口装饰器测试
"""
import requests

from conftest import check_response


class UserLogin:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @check_response("获取用户登录token", 200, ret="form.token", check={"headers.Host": "httpbin.org"}, debug=True)
    def get_token(self):
        """获取用户登录token"""
        url = "http://127.0.0.1:8000/admin/login/?next=/admin/"

        data = {
            "username": self.username,
            "password": self.password,
            "token": "token-123"  # 假装是接口返回的toKen
        }
        r = requests.post(url, data=data)
        return r


if __name__ == '__main__':
    user_login = UserLogin("admin", "admin")
    # token = user_login.get_token()
    # print(token)
