# -*- coding:utf-8 -*-
"""
@Author:tang
@File:test_login_new.py
@Time:2022/5/27 11:57
说明：使用poium来做
"""
from poium import Page, Element
import allure
import pytest
import logging

from utils.yaml_util import YamlUtil

logger = logging.getLogger(__name__)

class LoginPage(Page):
    username_loc = Element(xpath='//*[@id="id_username"]')
    password_loc = Element(xpath='//*[@id="id_password"]')
    click_loc = Element(xpath='//*[@id="login-form"]/div[3]/input')
    url = "http://127.0.0.1:8000/admin/login/?next=/admin/"
    zhuxiao_loc = Element(xpath='//*[@id="user-tools"]/a[3]')


class ProjectPage(Page):
    # 页面元素，添加测试项目url
    url = "http://127.0.0.1:8000/admin/project/project/add/"
    # 项目名称
    name_loc = Element(xpath='//*[@id="id_project_name"]')
    # 选择项目类型
    sel_loc = Element(xpath='//*[@id="id_project_type"]')
    # 项目版本
    vers_loc = Element(xpath='//*[@id="id_project_version"]')
    # 保存按钮
    save_loc = Element(xpath='//*[@id="project_form"]/div/div/input[1]')

    # 筛选web
    web_loc = Element(xpath='//*[@id="changelist-filter"]/ul/li[1]/a')
    # 搜索框
    search_loc = Element(xpath='//*[@id="searchbar"]')
    # 搜索按钮
    search_btn_loc = Element(xpath='//*[@id="changelist-search"]/div/input[2]')

    # 搜索后第一个项目版本编辑框
    mod_vers_loc = Element(xpath='//*[@id="id_form-0-project_version"]')
    # 保存按钮
    mod_save_loc = Element(xpath='//*[@id="changelist-form"]/p/input')

    # 第一列勾选
    line_loc = Element(xpath='//*[@id="result_list"]/tbody/tr[1]/td[1]/input')
    # 选择动作
    line_sel_loc = Element(xpath='//*[@id="changelist-form"]/div[2]/label/select')
    # 执行按钮
    execute_loc = Element(xpath='//*[@id="changelist-form"]/div[2]/button')
    # 删除确定按钮
    line_del_loc = Element(xpath='//*[@id="content"]/form/div/input[4]')


class TestLogin:
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
        name = caseinfo['username']
        pd = caseinfo['password']
        page = LoginPage(driver)
        page.open(page.url)
        page.username_loc.send_keys(name)
        page.password_loc.send_keys(pd)
        page.click_loc.click()

        assert page.zhuxiao_loc.text == '注销'
        logger.info("登录测试成功")

    @allure.story("测试项目")
    @allure.severity('blocker')
    @allure.title("增删改查测试项目")
    @allure.step("开始增删改查测试项目")
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('project.yml'))
    def test_Project_ok(self, login_driver, caseinfo):
        name = caseinfo['projectname']
        num = caseinfo['num']
        version = caseinfo['version']
        page = ProjectPage(login_driver)
        page.open(page.url)
        # 添加
        with allure.step('Step: 添加测试项目'):
            logger.info("输入项目名：" + str(name))
            page.name_loc.send_keys(name)
            logger.info("选择类型")
            page.sel_loc.select_by_index(num)
            logger.info("输入项目版本：" + version)
            page.vers_loc.send_keys(version)
            logger.info("保存")
            page.save_loc.click()
        # 搜索
        with allure.step('Step: 搜索测试项目'):
            logger.info("选择筛选项目")
            page.web_loc.click()
            logger.info("输入项目名：" + name)
            page.search_loc.send_keys(name)
            logger.info("点击搜索")
            page.search_btn_loc.click()
        # 编辑版本
        with allure.step('Step: 修改测试项目'):
            logger.info("删除文本")
            page.mod_vers_loc.clear()
            logger.info("输入文本" + version)
            page.mod_vers_loc.send_keys("版本修正")
            logger.info("点击保存")
            page.mod_save_loc.click()
        # 删除
        with allure.step('Step: 删除测试项目'):
            logger.info("选择第一行")
            page.line_loc.click()
            logger.info("选择行为" + 'delete_selected')
            page.line_sel_loc.select_by_value('delete_selected')
            logger.info("点击执行")
            page.execute_loc.click()
            logger.info("二次确认")
            page.line_del_loc.click()