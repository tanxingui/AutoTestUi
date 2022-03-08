from common.basepage import BasePage
from pageObjects.order_Objects.corder_page import Corder_Page
from pageObjects.provide_Objects.provide_page import Provide_Page


class Main_Page(BasePage):

    def goto_provide(self):  #去到客户管理页
        # self.wait_click_Element(self.Provide_button)
        self.wait_click_Element(self.shopper_button)
        return Provide_Page()

    def goto_corder(self):   #去到C端订单页面
        self.wait_click_Element(self.corder_click)
        return Corder_Page()


