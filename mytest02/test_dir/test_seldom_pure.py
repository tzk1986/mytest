# -*- coding:utf-8 -*-
"""
@Author:tang
@File:test_seldom_pure.py
@Time:2022/5/26 16:53
说明：不使用poium，直接使用seldom来进行web测试
"""
import seldom


class TestPlatform(seldom.TestCase):
    # def start(self):
    #     self.open(url="http://127.0.0.1:8000/admin/login/?next=/admin/")
    #     self.type(xpath='//*[@id="id_username"]', text="admin")
    #     self.type(xpath='//*[@id="id_password"]', text="admin")
    #     self.click(xpath='//*[@id="login-form"]/div[3]/input')
    #     # self.s = self.Session()
    #     print("一条测试用例开始")
    #
    # def end(self):
    #
    #     print("一条测试用例结束")
    def test_01(self):
        self.delete_all_cookies()
        self.refresh()
        self.wait(3)
        self.open(url="http://127.0.0.1:8000/admin/login/?next=/admin/")
        self.type(xpath='//*[@id="id_username"]', text="admin")
        self.type(xpath='//*[@id="id_password"]', text="admin")
        self.click(xpath='//*[@id="login-form"]/div[3]/input')

    def test_02(self):
        # self.delete_all_cookies()
        # self.refresh()
        # self.wait(3)
        # self.open(url="http://127.0.0.1:8000/admin/login/?next=/admin/")
        # self.type(xpath='//*[@id="id_username"]', text="admin")
        # self.type(xpath='//*[@id="id_password"]', text="admin")
        # self.click(xpath='//*[@id="login-form"]/div[3]/input')
        self.open(url="http://127.0.0.1:8000/admin/project/project/add/")
        self.type(xpath='//*[@id="id_project_name"]', text="测试第一版")
        self.select(xpath='//*[@id="id_project_type"]', index=2)
        self.type(xpath='//*[@id="id_project_version"]', text="第一版")
        self.click(xpath='//*[@id="project_form"]/div/div/input[1]')
        self.wait(3)
        # 搜索
        self.click(xpath='//*[@id="changelist-filter"]/ul/li[1]/a')
        self.type(xpath='//*[@id="searchbar"]', text="测试第一版")
        self.click(xpath='//*[@id="changelist-search"]/div/input[2]')
        # 修改
        self.clear(xpath='//*[@id="id_form-0-project_version"]')
        self.type(xpath='//*[@id="id_form-0-project_version"]', text="第二版")
        self.click(xpath='//*[@id="changelist-form"]/p/input')
        # 删除
        self.click(xpath='//*[@id="result_list"]/tbody/tr[1]/td[1]/input')
        self.select(xpath='//*[@id="changelist-form"]/div[2]/label/select', value='delete_selected')
        self.click(xpath='//*[@id="changelist-form"]/div[2]/button')
        self.wait(5)
        self.click(xpath='//*[@id="content"]/form/div/input[4]')
        self.screenshots(file_path='./reports')
        self.wait(5)

    def test_03(self):
        # self.open(url="http://127.0.0.1:8000/admin/login/?next=/admin/")
        # self.type(xpath='//*[@id="id_username"]', text="admin")
        # self.type(xpath='//*[@id="id_password"]', text="admin")
        # self.click(xpath='//*[@id="login-form"]/div[3]/input')
        self.open(url="http://127.0.0.1:8000/admin/project/port/add/")
        self.assertInTitle("port")

    def test_04(self):
        self.open("http://127.0.0.1:8000/admin/auth/user/")
        self.assertInTitle("port")



if __name__ == '__main__':
    seldom.main(debug=False)
