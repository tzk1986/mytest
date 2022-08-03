import unittest

from execl_util import *
from ddt import ddt, data, unpack

from login_page import *
from product_manage_page import ProductManagePage


@ddt
class TestCase(unittest.TestCase):

    @data(*ExcelUtil.read_execl())
    @unpack
    def test_01(self, index, username, password):
        print(index, username, password)
    #     lp = LoginPage()  # 调用basepage，初始化对象
    #     lp.login_ecshop("tang", "gao")  # 调用pageobject，定位元素，并传参`
    #
    #     self.assertEqual(lp.get_except_results(), '退出')
    #
    # def test_02(self):
    #     pm = ProductManagePage()
    #     pm.select_product("4")


os.system("allure generate ./temp -o ./report --clean")
