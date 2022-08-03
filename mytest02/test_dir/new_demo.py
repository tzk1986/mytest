# -*- coding:utf-8 -*-
"""
@Author:tang
@File:new_demo.py
@Time:2022/5/26 19:32
说明：
"""
import seldom
from seldom import Seldom
from poium import Page, Element


class BaiduPage(Page):
    """baidu page"""
    search_input = Element(id_="kw")
    search_button = Element(id_="su")


class BaiduSearchPage(Page):
    """
    百度搜索结果
    """
    search_result = Element(xpath="//div/h3/a", index=1)


class BaiduTest(seldom.TestCase):
    """Baidu serach test case"""

    def start(self):
        """
        可以在start中引用多个页面
        """
        self.baidu_page = BaiduPage(Seldom.driver)
        self.baidu_search_page = BaiduSearchPage(Seldom.driver)

    def test_case(self):
        """
        A simple test
        """
        self.baidu_page.open("https://www.baidu.com")
        self.baidu_page.search_input = "seldom"
        self.baidu_page.search_button.click()
        self.sleep(2)
        ret = self.baidu_search_page.search_result.text
        print(ret)


if __name__ == '__main__':
    # 需要指定browser='chrome'，这样seldom才会执行web测试，才能继承Seldom.driver
    seldom.main(browser='chrome', debug=True)
    # seldom.main(debug=True)