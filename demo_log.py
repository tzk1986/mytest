# -*- coding:utf-8 -*-
# remark : 
"""
@Author:tang
@File:demo_log.py
@Time:2022/5/13 16:32
说明：log使用尝试
"""
import logging


class Framlog:
    def getlog(self):
        # 创建日志器对象
        logger = logging.getLogger("logger")
        # logger = logging.getLogger(__name__)
        # 创建控制台处理器
        sh = logging.StreamHandler()
        # 设置日志级别，默认为warning
        logger.setLevel(logging.INFO)
        # 日志输出内容的格式——格式器 日志内容？时间 事件 日志级别 信息描述
        """括号中放入参数，参数的格式如果是字符串用s，如果是数字用d"""
        formatter = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s", datefmt="%Y/%m/%d/%X")
        logger.addHandler(sh)
        sh.setFormatter(formatter)
        return logger
# 输出错误级别的日志信息
# logger.error("这是一个错误信息")
# logger.info("这是一个info信息")
# print(help(logging.Formatter))
