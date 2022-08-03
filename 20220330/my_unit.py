import unittest


class MyUnit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("在每个类之前执行一次，创建数据库，生成日志对象")

    def setUp(self) -> None:
        print("测试用例之前的执行，打开浏览器，加载网页")

    def tearDown(self) -> None:
        print("测试用例之后执行，收尾工作，关闭浏览器")

    @classmethod
    def tearDownClass(cls) -> None:
        print("每个类之后执行一次，关闭数据库连接，销毁日志对象")