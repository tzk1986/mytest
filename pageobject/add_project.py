# coding=utf8
# @Author : tang 2022/5/12
# remark :
import logging
import time

from selenium.webdriver.common.by import By

from base.BasePage import BasePage

logger = logging.getLogger(__name__)


class ProjectPage(BasePage):
    # 页面元素，添加测试项目url
    url = "http://127.0.0.1:8000/admin/project/project/add/"
    # 项目名称
    name_loc = (By.XPATH, '//*[@id="id_project_name"]')
    # 选择项目类型
    sel_loc = (By.XPATH, '//*[@id="id_project_type"]')
    # 项目版本
    vers_loc = (By.XPATH, '//*[@id="id_project_version"]')
    # 保存按钮
    save_loc = (By.XPATH, '//*[@id="project_form"]/div/div/input[1]')

    # 筛选web
    web_loc = (By.XPATH, '//*[@id="changelist-filter"]/ul/li[1]/a')
    # 搜索框
    search_loc = (By.XPATH, '//*[@id="searchbar"]')
    # 搜索按钮
    search_btn_loc = (By.XPATH, '//*[@id="changelist-search"]/div/input[2]')

    # 搜索后第一个项目版本编辑框
    mod_vers_loc = (By.XPATH, '//*[@id="id_form-0-project_version"]')
    # 保存按钮
    mod_save_loc = (By.XPATH, '//*[@id="changelist-form"]/p/input')

    # 第一列勾选
    line_loc = (By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/td[1]/input')
    # 选择动作
    line_sel_loc = (By.XPATH, '//*[@id="changelist-form"]/div[2]/label/select')
    # 执行按钮
    execute_loc = (By.XPATH, '//*[@id="changelist-form"]/div[2]/button')
    # 删除确定按钮
    line_del_loc = (By.XPATH, '//*[@id="content"]/form/div/input[4]')

    """添加测试项目"""

    def AddProject(self, name, num, version):
        # lp = LoginPage()
        # lp.login()
        # self.driver.execute_script("window.open()")
        # self.getURL(url=ProjectPage.url)
        logger.info("输入项目名：" + str(name))
        self.set_keys(loc=ProjectPage.name_loc, value=name)
        logger.info("选择类型")
        self.choic_select(loc=ProjectPage.sel_loc, value=num)
        logger.info("输入项目版本：" + version)
        self.set_keys(loc=ProjectPage.vers_loc, value=version)
        logger.info("保存")
        self.click(loc=ProjectPage.save_loc)
        time.sleep(5)

    """过滤测试项目后，搜索"""

    def SearchProject(self, name=None):
        logger.info("选择筛选项目")
        self.click(loc=ProjectPage.web_loc)
        logger.info("输入项目名：" + name)
        self.set_keys(loc=ProjectPage.search_loc, value=name)
        logger.info("点击搜索")
        self.click(loc=ProjectPage.search_btn_loc)

    """修改测试项目的项目版本"""

    def ModifyProject(self, version):
        logger.info("删除文本")
        self.del_text(loc=ProjectPage.mod_vers_loc)
        logger.info("输入文本" + version)
        self.set_keys(loc=ProjectPage.mod_vers_loc, value=version)
        self.sec_time()
        logger.info("点击保存")
        self.click(loc=ProjectPage.mod_save_loc)

    """删除测试项目"""

    def DelProject(self, value):
        logger.info("选择第一行")
        self.click(loc=ProjectPage.line_loc)
        logger.info("选择行为" + value)
        self.choic_select(loc=ProjectPage.line_sel_loc, value=value)
        logger.info("点击执行")
        self.click(loc=ProjectPage.execute_loc)
        logger.info("二次确认")
        self.click(loc=ProjectPage.line_del_loc)
        self.sec_time()
