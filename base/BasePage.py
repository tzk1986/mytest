# coding=utf8
# @Author : tang 2022/5/12
# remark :
import logging
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from demo_log import Framlog

loggers = logging.getLogger(__name__)


class BasePage:

    # 页面登录初始化
    def __init__(self, driver: webdriver.chrome):
        # global driver  # 在unittest使得谷歌浏览器不会在执行后自动关闭，后续需要手动关闭，或者使用夹具关闭
        # self.driver = webdriver.Chrome()
        # driver = self.driver
        # driver.get()
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)  # 添加等待
        # 隐式等待
        driver.implicitly_wait(10)

    # 获取url 可以直接在这里设置获取url地址的关键字
    def getURL(self, url):
        self._driver.get(url)

    # 定位元素的关键字
    """元素定位，并收集日志，记录是否定位成功"""

    def loc_element(self, loc):
        allure.attach(  # 交互前进行截图，确认加载效果
            self._driver.get_screenshot_as_png(),
        )
        try:
            element = self._driver.find_element(*loc)
            print(loc)
            loggers.info("元素定位成功，元素：" + loc[1])
        except Exception as error:
            loggers.error("元素定位失败，元素：" + loc[1] + str(error))
        return element

    # def loc_element(self, loc):
    #     try:
    #         element = self._driver.find_element(*loc)
    #         print(loc)
    #         Framlog().getlog().info("元素定位成功，元素：" + loc[1])
    #     except Exception as error:
    #         Framlog().getlog().error("元素定位失败，元素：" + loc[1] + str(error))
    #     return element

    # def loc_element(self, loc):
    #     # print(loc)
    #     return self._driver.find_element(*loc)  # 使用*去除多余的()

    # 设置值
    def set_keys(self, loc, value):
        self.loc_element(loc).send_keys(value)

    # 点击
    def click(self, loc):
        self.loc_element(loc).click()

    # 进入框架的关键字
    def goto_frame(self, frame_name):
        self._driver.switch_to.frame(frame_name)

    # 出框架的关键字
    def quit_frame(self):
        self._driver.switch_to.default_content()

    # 下拉框关键字
    def choic_select(self, loc, value=None):
        sel = Select(self.loc_element(loc))
        sel.select_by_value(value)

    # 获取文本的值
    def get_value(self, loc):
        return self.loc_element(loc).text

    # 选择窗口
    def stay_window(self, num):
        self._driver.switch_to.window(self._driver.window_handles[num])

    # 获取当前窗口链接
    def get_new_url(self):
        return self._driver.current_url

    # 清除文本框输入值
    def del_text(self, loc):
        self.loc_element(loc).send_keys(Keys.COMMAND, "a")
        self.loc_element(loc).send_keys(Keys.DELETE)

    # 等待时间
    def sec_time(self, num=3):
        time.sleep(num)

    # 截图
    def jietu(self):
        self._driver.get_screenshot_as_png()
