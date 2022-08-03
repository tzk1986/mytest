from selenium import webdriver
from selenium.webdriver.common.by import By


class test_line():
    global driver
    driver = webdriver.Chrome()
    driver.get("")

    driver.find_element(by=By.NAME, value=id).send_keys("")
    driver.find_element(by=By.NAME, value=id).send_keys("")
    driver.find_element(by=By.NAME, value=id).click()