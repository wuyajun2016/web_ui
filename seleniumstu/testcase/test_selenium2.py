import time
import utx
from seleniumstu.unit.baseselenium import *
import os
from seleniumstu.unit.csvdata import get_data
from seleniumstu.pageobject.BaiDuPage import *
from seleniumstu.unit.deco import dependon


class BaiduHomePageTest(BaseSeleniumDriver):

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    @utx.skip("跳过此用例")
    def test_baidu_homepape(self):
        """测试百度主页"""
        obj_baidu = BaiDuPage(self.driver, setting.item_url)
        tg = obj_baidu.get_link_text('关于百度')
        self.assertIn("百度", tg)

    @data(*get_data('testdata.csv'))
    def test_baidu_title(self,search_value,expected_result):
        """测试百度标题"""
        obj_baidu = BaiDuPage(self.driver, setting.item_url)
        obj_baidu.back_home()  # 初始化链接
        tg = obj_baidu.get_title()
        self.assertEqual("百度一下，你就知道", tg)
        self.add_img()
        obj_baidu.type_search(search_value)
        obj_baidu.click_search_btn()
        obj_baidu.wait_element_appear()
        self.add_img()

    # @dependon('test_00002_exception2')
    @tag(Tag.SMOKE)
    def test_normal_attack(self):
        """测试SMOKE"""  # 这里注释不能用demo种的return ，不然_retry会显示不出来，可能长度不够
        print("测试smoke1(这段文字会显示到原因里面)")
        assert 1 == 2

