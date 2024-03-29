# coding=utf8
# @Author : tang 2022/5/12
# remark :
import logging
from poium import Page, Element
from selenium import webdriver

logger = logging.getLogger(__name__)


class LoginPage(Page):
    # def __init__(self, driver: webdriver.Chrome, url):
    #     self.driver = driver
    #     self.root_uri = url
    username_loc = Element(xpath='//*[@id="id_username"]')
    password_loc = Element(xpath='//*[@id="id_password"]')
    click_loc = Element(xpath='//*[@id="login-form"]/div[3]/input')
    url = "http://127.0.0.1:8000/admin/login/?next=/admin/"
    zhuxiao_loc = Element(xpath='//*[@id="user-tools"]/a[3]')

    def login(self, username='admin', password='admin'):
        driver = webdriver.Chrome()

        page = LoginPage(driver)
        page.open(page.url)

        page.username_loc.send_keys(username)
        page.password_loc.send_keys(password)
        page.click_loc.click()
        return driver

# class LoginPage(BasePage):
#     # 页面元素
#     username_loc = (By.XPATH, '//*[@id="id_username"]')
#     password_loc = (By.XPATH, '//*[@id="id_password"]')
#     click_loc = (By.XPATH, '//*[@id="login-form"]/div[3]/input')
#     url = "http://127.0.0.1:8000/admin/login/?next=/admin/"
#     zhuxiao_loc = (By.XPATH, '//*[@id="user-tools"]/a[3]')
#
#     def login(self, username='admin', password='admin'):
#         # self.getURL(url=LoginPage.url)
#         logger.info("输入用户名：" + username)
#         with allure.step('Step: 输入用户名'):
#             self.set_keys(loc=LoginPage.username_loc, value=username)
#         logger.info("输入密码：" + password)
#         with allure.step('Step: 输入密码'):
#             self.set_keys(loc=LoginPage.password_loc, value=password)
#         logger.info("点击登录按钮")
#         with allure.step('Step: 点击登录按钮'):
#             self.click(loc=LoginPage.click_loc)
#         allure.attach(  # 交互后进行截图，确认交互效果
#             self._driver.get_screenshot_as_png(),
#         )
#
#     def get_except_results(self):
#         logger.info("获取注销按钮")
#         return self.get_value(loc=LoginPage.zhuxiao_loc)
