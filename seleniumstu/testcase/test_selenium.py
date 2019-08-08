from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from seleniumstu.unit.baseselenium import *
from seleniumstu.pageobject.BaiDuPage import *
from seleniumstu.unit.deco import dependon


class ExceptionTest(BaseSeleniumDriver):

    # 截图公共方法
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_exception2(self):
        """测试异常2"""
        try:
            obj_baidu = BaiDuPage(self.driver, setting.item_url)
            obj_baidu.find_kw()
        except ElementNotVisibleException:
            raise

    @dependon('test_00002_exception2')  # utx框架中为了排序，test_00002_exception2这个名字已经变了，并非上面的test_exception2
    def test_exception(self):
        """测试异常1：超过2行怎么办.我看就短一点好了，看看能不能显示的下。就这样吧应当差不多了，走起"""
        try:
            obj_baidu = BaiDuPage(self.driver, setting.item_url)
            self.add_img()
            self.assertEqual('百度一下', obj_baidu.get_button_value())
        except NoSuchElementException:
            raise  # 主动抛出异常


