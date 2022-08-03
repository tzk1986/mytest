# -*- coding:utf-8 -*-
"""
@Author:tang
@File:seldom_sample.py
@Time:2022/5/25 11:56
说明：seldom样例
"""
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class MyTest(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#
#     def test_case(self):
#         self.driver.get("https://www.baidu.com")
#         self.driver.find_element(by=By.ID, value="kw").send_keys("seldom")
#         self.driver.find_element(by=By.ID, value="su").click()
#
#     def tearDown(self) -> None:
#         self.driver.close()
#
#
# if __name__ == "__main__":
#     unittest.main()
import seldom


class MyTest(seldom.TestCase):
    def test_case(self):
        self.open("https://www.baidu.com")
        self.type(css="#kw", text="seldom")
        self.click(id_="su")


if __name__ == "__main__":
    seldom.main()

# import seldom
# from seldom import Steps
#
#
# class BaiduTest(seldom.TestCase):
#
#     def test_case_one(self):
#         """a simple test case """
#         self.open("https://www.baidu.com")
#         self.type(id_="kw", text="seldom")
#         self.click(css="#su")
#         self.assertTitle("seldom_百度搜索")
#
#     def test_case_two(self):
#         """method chaining """
#         Steps(url="https://www.baidu.com").open().find("#kw").type("seldom").find("#su").click()
#         self.assertTitle("seldom_百度搜索")
#
#
# if __name__ == '__main__':
#     seldom.main()
