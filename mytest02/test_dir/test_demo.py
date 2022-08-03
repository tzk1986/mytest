# -*- coding:utf-8 -*-
"""
@Author:tang
@File:test_demo.py
@Time:2022/5/26 18:22
说明：
"""
import seldom
from seldom import Steps


class BaiduTest(seldom.TestCase):

    def test_case_one(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="seldom")
        self.click(css="#su")
        self.assertTitle("seldom_百度搜索")

    def test_case_two(self):
        """method chaining """
        Steps(url="https://www.baidu.com").open().find("#kw").type("seldom").find("#su").click()
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main()
