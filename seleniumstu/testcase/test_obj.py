from seleniumstu.unit.baseselenium import *
from seleniumstu.pageobject.BaiDuPage import *
from utx import *


class ObjPageTest(BaseSeleniumDriver):

    def test_obj1(self):
        """测试对象操作：这一层不涉及页面元素"""
        obj_baidu = BaiDuPage(self.driver, setting.item_url)
        obj_baidu.type_search('test')

