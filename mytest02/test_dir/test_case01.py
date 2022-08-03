# -*- coding:utf-8 -*-
"""
@Author:tang
@File:test_case01.py
@Time:2022/5/26 14:18
说明：使用poium创建出的流程，直接创建测试用例，使用seldom生成报告
"""
from seldom import Seldom
import seldom

from poium import Page, Element


# class LoginPage(Page):
#     # def __init__(self, driver: webdriver.Chrome, url):
#     #     self.driver = driver
#     #     self.root_uri = url
#     username_loc = Element(xpath='//*[@id="id_username"]')
#     password_loc = Element(xpath='//*[@id="id_password"]')
#     click_loc = Element(xpath='//*[@id="login-form"]/div[3]/input')
#     url = "http://127.0.0.1:8000/admin/login/?next=/admin/"
#     zhuxiao_loc = Element(xpath='//*[@id="user-tools"]/a[3]')
from mytest02.pageobject.login_page import LoginPage


class TestLogin(seldom.TestCase):
    def test_01(self, username='admin', password='admin'):
        # driver = webdriver.Chrome()
        # driver = Seldom.driver
        self.page = LoginPage(Seldom.driver)
        self.page.open(self.page.url)

        self.page.username_loc.send_keys(username)
        self.page.password_loc.send_keys(password)
        self.page.click_loc.click()
        title = self.page.zhuxiao_loc.text

        self.assertEqual(title, "注销")
        self.quit()

    # def test_02(self):
    #     driver = LoginPage.login(self)
    #     page = ProjectPage(driver)
    #     page.open(page.url)
    #     page.AddProject(name="test", num=2, version="第一版")
    #     page.SearchProject(name="test")
    #     page.ModifyProject(version="第二版")
    #     page.DelProject(value='delete_selected')


if __name__ == '__main__':
    seldom.main(browser='chrome', debug=False)
