from selenium.webdriver.common.by import By
from seleniumstu.unit.basepage import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaiDuPage(BasePage):
    """对页面上元素进行封装，使其成为具体的操作方法"""

    search_loc = (By.ID, "kw")
    find_kw_ele = (By.ID, 'aa')
    find_button = (By.ID, 'su')
    search_num = (By.CSS_SELECTOR, '.nums_text')

    def type_search(self, search_content):
        self.find_element(*self.search_loc).send_keys(search_content)

    def find_kw(self):
        self.find_element(*self.find_kw_ele)

    def get_button_value(self):
        return self.find_element(*self.find_button).get_attribute("value")

    def click_search_btn(self):
        self.find_element(*self.find_button).click()

    def get_link_text(self, content):
        return self.driver.find_element_by_link_text(content).text

    def get_title(self):
        return self.driver.title

    def wait_element_appear(self):
        wait = WebDriverWait(self.driver, self.common_time)  # 等待元素出现，最多等待10S
        wait.until(EC.presence_of_element_located((self.search_num[0], self.search_num[1])))  # 用*self.search_num竟然不行
