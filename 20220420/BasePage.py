"""
基础页面层
"""
from selenium import webdriver
from selenium.webdriver.support.select import Select


class BasePage:

    # 页面登录初始化
    def __init__(self):
        global driver  # 在unittest使得谷歌浏览器不会在执行后自动关闭，后续需要手动关闭，或者使用夹具关闭
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("")

    # 定位元素的关键字
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    # 设置值的关键字
    def set_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 单击的关键字
    def click(self, loc):
        self.locator_element(loc).click()

    # 进入框架的关键字
    def goto_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 出框架的关键字
    def quit_frame(self):
        self.driver.switch_to.default_content()

    # 下拉框关键字
    def choic_select(self, loc, value=None):
        sel = Select(self.locator_element(loc))
        sel.select_by_value(value)

    # 获取文本的值
    def get_value(self, loc):
        return self.locator_element(loc).text

    # 获取url 可以直接在这里设置获取url地址的关键字
    def getURL(self, url):
        self.driver.get(url)
