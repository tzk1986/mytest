"""
使用selenium测试ui，web测试
"""
import pdb
import time

from selenium import webdriver
# 打开浏览器
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 加载网页
driver.get("https://www.baidu.com/")
# 定位元素（利于封装）
# driver.find_element(By.ID,"kw").send_keys("高蕾")
# driver.find_element(By.LINK_TEXT, "新闻").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "闻").click()
# driver.find_element(By.XPATH, "//form/span[1]/input").send_keys("高蕾")
# driver.find_element(By.XPATH, "//*[substring(@autocomplete,2)='ff']").send_keys("高蕾")
# driver.find_element(By.XPATH, "//*[contains(@autocomplete,'of')]").send_keys("高蕾")
pdb.set_trace()
value = driver.find_element(By.XPATH, "//span[text()='按图片搜索']").get_attribute('class')
print(value)
time.sleep(3)
print(driver.window_handles)  # 获取所有的窗口ID
print(driver.current_window_handle)  # 获取当前窗口ID
pdb.set_trace()   # pdb调试
driver.switch_to.window(driver.window_handles[-1])  # 切换窗口到新打开的窗口

# driver.quit()
# driver.find_element(By.XPATH, "//form/span[1]/input").send_keys(Keys.ENTER)
