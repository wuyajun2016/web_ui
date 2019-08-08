from utx import *


class BasePage(object):
    """
    基础类：
    1）定义driver
    2）定义元素定位方法find_element
    3）定义返回主页的方法back_home
    """

    common_time = 10  # 等待时间

    def __init__(self, driver, url):
        self.driver = driver
        # self.driver.get(url)  # 每个用例（类）跑完后，都会初始化下url(应当不能这么干，还是在用例中主动调用下好了)

    #定位方法封装
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 初始化链接，即返回到主页面
    def back_home(self):
        self.driver.get(setting.item_url)
