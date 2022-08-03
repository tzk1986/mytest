import os
import unittest


class EcshopLogin(unittest.TestCase):
    # 测试用例
    def test01_baili(self):
        # raise Exception("1")
        print("测试小唐")

    # 测试用例
    def test01_gaolei(self):
        print("测试小高")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 使用加载器发现所有用例
    testcase = unittest.defaultTestLoader.discover(start_dir=os.getcwd(), pattern='*.py', top_level_dir=None)
    # 加载用例集
    suite.addTests(testcase)
    # unittest.main(defaultTest='suite')
    unittest.TextTestRunner().run(suite)