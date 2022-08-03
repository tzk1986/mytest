import os
import random
import time
import unittest

from selenium.webdriver.common.by import By

from my_unit import MyUnit
from selenium import webdriver


class Test2(MyUnit):

    # 流水线web测试，使用selenium获取页面元素并点击
    def test_member(self):
        global driver
        # 打开浏览器
        driver = webdriver.Chrome()
        # 等待网页元素都加载上
        driver.implicitly_wait(10)
        # 加载网页
        driver.get()
        # 加入所有cookie

        driver.add_cookie()
        driver.add_cookie()
        driver.add_cookie()
        # 加载登录后页面
        driver.get()
        time.sleep(3)
        # 断言
        self.assertIn("", driver.current_url)
        # 功能
        # 点击会员
        driver.find_element_by_xpath()
        driver.find_element(by=By.XPATH, value=xpath).click()
        # 点击会员管理
        driver.find_element_by_link_text()
        driver.find_element(by=By.LINK_TEXT, value=link_text).click()
        # 出框架
        driver.switch_to.default_content()
        # 进入frame框架，以便后续点击成功
        driver.switch_to.frame("")
        # 点击新增
        driver.find_element(by=By.XPATH, value=xpath).click()
        # 输入表单
        num = random.randint(1, 9999)
        driver.find_element_by_id()
        driver.find_element(by=By.ID, value=id).send_keys("")
        # 点击提交
        driver.find_element(by=By.XPATH, value=xpath).click()
        # 断言新增会员是否成功，判断是否有成功提示 前端div写出来的提示
        self.assertEqual("新增会员成功", driver.find_element(by=By.XPATH, value=xpath).text)
        ale = driver.switch_to.alert
        ale.accept()  # 弹窗点击确定
        ale.dismiss()  # 弹窗点击取消
