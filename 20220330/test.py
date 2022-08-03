import os
import unittest


from my_unit import MyUnit


class Test(MyUnit):
    age = 22

    # 测试用例

    def test01_baili(self):
        # raise Exception("1")
        print("测试小唐")
        self.assertEqual(1,2)

    # 测试用例
    # 判断为真，忽略

    def test01_gaolei(self):
        """测试小高"""
        print("测试小高")
        self.assertTrue(1)

    # 判断为否，忽略

    def test01_tanggao(self):
        """测试糖糕"""
        print("测试唐高")
        self.assertIn("a","abc")