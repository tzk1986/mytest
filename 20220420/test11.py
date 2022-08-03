import time
import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def test01_login(self):
        driver = webdriver.Chrome()
        driver.get("")
        cks = driver.get_cookies()  # 获得所有的cookie信息
        for ck in cks:
            print(ck)

        time.sleep(15)
        # 手动登录一次

        cks = driver.get_cookies()  # 获得登录后所有的cookie信息
        for ck in cks:
            print(ck)

        driver.add_cookie()
