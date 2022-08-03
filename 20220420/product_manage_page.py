from selenium.webdriver.common.by import By

from BasePage import BasePage


class ProductManagePage(BasePage):
    # 页面元素
    product_list_loc = (By.XPATH, "")
    cat_id_loc = (By.XPATH, "")
    sousuo_loc = (By.XPATH, "")

    # 页面动作
    def select_product(self, value=None):
        # 登录
        lp = LoginPage()  # 调用basepage，初始化对象
        lp.login_ecshop("tang", "gao")
        # 查询
        self.goto_frame("menu-frame")
        self.click(ProductManagePage.product_list_loc)
        self.quit_frame()
        self.goto_frame("main-frame")
        self.choic_select(ProductManagePage.cat_id_loc, value)
        self.click(ProductManagePage.sousuo_loc)

