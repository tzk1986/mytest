from selenium.webdriver.common.by import By

from BasePage import BasePage


class LoginPage(BasePage):
    # 页面元素
    username_loc = (By.NAME, "")
    password_loc = (By.NAME, "")
    submit_loc = (By.XPATH, "")
    tuichu_loc = (By.XPATH, "")

    # 页面的动作，添加默认值，当不传参数值时，默认用户名密码admin，admin123
    def login_ecshop(self, username="admin", password="admin123"):
        self.set_keys(LoginPage.username_loc, username)
        self.set_keys(LoginPage.password_loc, password)
        self.click(LoginPage.submit_loc)

    def get_except_results(self):
        self.goto_frame("header-frame")
        return self.get_value(LoginPage.tuichu_loc)