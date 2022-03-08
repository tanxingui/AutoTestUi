import time

from common.basepage import BasePage
from utils.Auto_faker import RandomData


class Provide_Page(BasePage):
    def Provide_page(self):
        # 点击新增线索
        self.wait_click_Element(self.add_shopper_button)
        # 输入随机的手机号码
        phone = RandomData().random_mobile_phone_num()
        print(phone)
        name1 = RandomData().random_name()
        name = '自动化随机名:'+name1
        print(name)
        self.input_key(self.phone_number_input, phone)
        self.input_key(self.providename_input, name)
        # 点击确认添加
        self.click_element(self.confirm_button)
        time.sleep(1)
        # 点击弹框的确认添加
        self.click_element(self.affirm_button)
        time.sleep(6)  # 等待接口回调，否则新建不成功

