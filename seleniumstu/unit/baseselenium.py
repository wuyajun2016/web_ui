import unittest
from selenium import webdriver
from utx import *
import os


class BaseSeleniumDriver(unittest.TestCase):
    """浏览器webdriver"""
    driver = None

    @classmethod
    def setUpClass(cls):
        dir_path = os.path.abspath(os.path.join(os.getcwd(), "."))  # 获取当前路径的上一级
        driver_path = dir_path + "\\driver\\chromedriver.exe"  # driver的存放路径
        if cls.driver is None:
            cls.driver = webdriver.Chrome(executable_path=driver_path)
            cls.driver.implicitly_wait(5)
            cls.driver.maximize_window()
            cls.driver.get(setting.item_url)

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()