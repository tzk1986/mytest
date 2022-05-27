# coding=utf8
# @Author : tang 2022/5/12
# remark :
import logging
import os

import allure
import pytest

from pageobject.add_project import ProjectPage
from pageobject.login_page import LoginPage
from utils.yaml_util import YamlUtil

logger = logging.getLogger(__name__)


# 标注测试重点核心
# @allure.epic("演示下allure支持的测试")
# 标注测试场景
@allure.feature("登录以及增删改查测试项目")
class TestLogin:
    # def test_01(self):
    #     driver = webdriver.Chrome()
    #     # 等待网页元素都加载上
    #     driver.implicitly_wait(10)
    #     # 加载网页
    #     driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    #
    #     username = driver.find_element(by=By.XPATH, value='//*[@id="id_username"]')
    #     username.send_keys("admin123")
    #
    #     password = driver.find_element(by=By.XPATH, value='//*[@id="id_password"]')
    #     password.send_keys("admin")
    #
    #     driver.find_element(by=By.XPATH, value='//*[@id="login-form"]/div[3]/input').click()
    #     time.sleep(10)
    # 标注测试功能模块
    @allure.story("登录模块")
    # 标注测试用例的重要级别
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("登录成功用例")
    # 标记测试步骤
    @allure.step("开始登录")
    @allure.description("这是一个登录测试用例")  # 标记代码，优先取这个
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('login.yml'))
    def test_login_ok(self, driver, caseinfo):
        """登录页面"""
        # 获取当前目录
        print(os.getcwd())
        print(os.path.abspath(os.path.dirname(__file__)))
        # 以下都是获取上级目录
        print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # 绝对路径
        print(os.path.abspath(os.path.dirname(os.getcwd())))
        print(os.path.abspath(os.path.join(os.getcwd(), "..")))
        # 获取上上级目录
        print(os.path.abspath(os.path.join(os.getcwd(), "../..")))

        print(caseinfo['username'])
        print(caseinfo['password'])
        name = caseinfo['username']
        pd = caseinfo['password']
        page = LoginPage(driver)
        page.login(username=name, password=pd)

        # print(page.get_new_url())
        # print(page.get_except_results())
        #
        assert page.get_except_results() == '注销'
        logger.info("登录测试成功")


    @allure.story("测试项目")
    @allure.severity('blocker')
    @allure.title("增删改查测试项目")
    @allure.step("开始增删改查测试项目")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('project.yml'))
    def test_Project_ok(self, login_driver, caseinfo):
        """
        用例描述：测试项目的增删改查
        """
        print(caseinfo['projectname'])
        print(caseinfo['num'])
        print(caseinfo['version'])
        name = caseinfo['projectname']
        num = caseinfo['num']
        version = caseinfo['version']
        login_driver.get("http://127.0.0.1:8000/admin/project/project/add/")
        page = ProjectPage(login_driver)
        # 使用下面的step可以在函数中使用，装饰器只能在类上使用
        with allure.step('Step: 添加测试项目'):
            page.AddProject(name=name, num=num, version=version)
        logger.info("添加测试项目成功")
        with allure.step('Step: 搜索测试项目'):
            page.SearchProject(name=name)
        logger.info("搜索测试项目成功")
        with allure.step('Step: 修改测试项目'):
            page.ModifyProject(version="版本修正")
        logger.info("修改测试项目成功")
        with allure.step('Step: 删除测试项目'):
            page.DelProject(value='delete_selected')
        logger.info("删除测试项目成功")

    @allure.story("测试失败效果")
    @allure.title("失败测试")
    def test_three(self):
        assert False


@allure.feature("测试报告显示")
class Testfour():
    @allure.story("成功模块")
    def test_success(self):
        assert True

    @allure.story("失败模块")
    def test_failure(self):
        assert False

    @allure.story("跳过模块")
    def test_skip(self):
        pytest.skip('跳过')

    @allure.story("中断模块")
    def test_broken(self):
        raise Exception('oops')
