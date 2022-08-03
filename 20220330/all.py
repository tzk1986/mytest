import json
import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    testcase = unittest.defaultTestLoader.discover(os.getcwd(), "*.py")
    suite.addTests(testcase)
    # unittest.TextTestRunner(verbosity=2).run(suit)
    # 添加创建时间参数，写入报告中
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    # wb以二进制的方式写入
    name = open(os.getcwd() + "/" + nowtime + "_report.html", "wb")
    runner = HTMLTestRunner(stream=name, verbosity=2, title="一网通自动化报告", description="报告详情如下：")
    runner.run(suite)
