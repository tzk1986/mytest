# -*- coding:utf-8 -*-
"""
@Author:tang
@File:poium_test.py
@Time:2022/5/25 16:04
说明：
"""
from poium import Page, Element
from selenium import webdriver


class BaiduIndexPage(Page):
    search_input = Element(name='wd')
    search_button = Element(id_='su')


driver = webdriver.Chrome()
page = BaiduIndexPage(driver)
page.open("https://www.baidu.com")

page.search_input.send_keys("poium")
page.search_button.click()

driver.quit()
