from time import sleep

from common.basepage import BasePage
from config.project_config import Auto_login_URL
from pageObjects.mainPage import Main_Page


class Login_Page(BasePage):

    def open_loginpage(self):
        self.open_Url(Auto_login_URL)
        return self   # 返回实例可以继续调用login_auto方法

    #  废弃，没卵用的验证码识别
    # def login_auto(self, username, password):
    #     self.input_key(('name', "username"), username)
    #     self.input_key(('name', "password"), password)
    #     code = self.get_Code(('xpath', '//img'))
    #     self.input_key(('name', "captcha_text"), code)
    #     # self.input_key(('name', "captcha_text"), '123456')
    #     self.wait_click_Element(("css selector", "div>button>span"))
    #     return Main_Page()  # 返回首页的实例,方便调用首页的其他元素

    def login_auto(self, username, password):
        self.input_key(self.username_input, username)
        self.input_key(self.password_input, password)
        self.input_key(self.captcha_text_input, '123456')
        self.wait_click_Element(self.login_button)
        return Main_Page()  # 返回首页的实例,方便调用首页的其他元素

if __name__ == '__main__':
    test_login = Login_Page()
    test_login.open_loginpage()
    test_login.login_auto("tanxingui123", "123456")
