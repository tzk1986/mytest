# coding=utf8
# @Author : tang 2022/5/12
# remark :
import pytest
import locust
from locust import HttpUser
from selenium import webdriver
from selenium.webdriver.common.by import By

"""未登录浏览器使用drive"""


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    # 等待网页元素都加载上
    driver.implicitly_wait(10)
    # 需要测试登录后退出登录，再次登录，在测试用例代码中加入以下代码，模拟退出登录状态
    # driver.delete_all_cookies()
    # driver.refresh()
    # 加载网页
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    yield driver
    print("测试用例执行完毕-------")
    driver.quit()


"""登录状态浏览器使用login_driver"""


@pytest.fixture(scope="session")
def login_driver():
    driver = webdriver.Chrome()
    # 等待网页元素都加载上
    driver.implicitly_wait(10)
    # 加载网页
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

    username = driver.find_element(by=By.XPATH, value='//*[@id="id_username"]')
    username.send_keys("admin")

    password = driver.find_element(by=By.XPATH, value='//*[@id="id_password"]')
    password.send_keys("admin")

    driver.find_element(by=By.XPATH, value='//*[@id="login-form"]/div[3]/input').click()
    yield driver
    print("测试用例执行完毕-------")
    driver.quit()


"""接口检查装饰器"""
import json
from jmespath import search


# @pytest.fixture(scope="session")
# def check_response(
#         describe: str = "",
#         status_code: int = 200,
#         ret: str = None,
#         check: dict = None,
#         debug: bool = False):
#     """
#     checkout response data
#     :param describe: interface describe
#     :param status_code: http status code
#     :param ret: return data
#     :param check: check data
#     :param debug: debug Ture/False
#     :return:
#     """
#
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             func_name = func.__name__
#             if debug is True:
#                 print(f"Execute {func_name} - args: {args}")
#                 print(f"Execute {func_name} - kwargs: {kwargs}")
#
#             r = func(*args, **kwargs)
#             flat = True
#             if r.status_code != status_code:
#                 print(f"Execute {func_name} - {describe} failed: {r.status_code}")
#                 flat = False
#
#             try:
#                 r.json()
#             except json.decoder.JSONDecodeError:
#                 print(f"Execute {func_name} - {describe} failed：Not in JSON format")
#                 flat = False
#
#             if debug is True:
#                 print(f"Execute {func_name} - response:\n {r.json()}")
#
#             if flat is True:
#                 print(f"Execute {func_name} - {describe} success!")
#
#             if check is not None:
#                 for expr, value in check.items():
#                     data = search(expr, r.json())
#                     if data != value:
#                         print(f"Execute {func_name} - check data failed：{value}")
#                         raise ValueError(f"{data} != {value}")
#
#             if ret is not None:
#                 data = search(ret, r.json())
#                 if data is None:
#                     print(f"Execute {func_name} - return {ret} is None")
#                 return data
#             else:
#                 return r.json()
#
#         return wrapper
#
#     return decorator
