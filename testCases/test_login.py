import os
import pytest
import allure
from common.basepage import BaseAssert
from config.project_config import Auto_zhuye_URL
from pageObjects.loginPage import Login_Page
from utils.Auto_path import testDatas_path, report_path
from utils.Auto_yaml import get_yaml_data


@allure.epic("史诗:后管UI测试")
@allure.feature('feature:登录模块测试')
@pytest.mark.Login
class Test_Login(BaseAssert):
    @pytest.mark.parametrize('casetitle,username,password,locator,expected', get_yaml_data(f"{testDatas_path}login_data.yaml"))
    @allure.story("用户故事:登录场景")
    @allure.title('{casetitle}')
    def test_Login_success(self, casetitle, username, password, locator, expected):
        with allure.step("1、打开登录页填写账号密码"):
            test_login = Login_Page()
            test_login.open_loginpage()
            test_login.login_auto(username, password)
        # 可以用pytest-assume插件，遇到一个断言失败也会自动运行，且不用封装
        # pytest.assume(test_login.get_Element_text(locator) == expected)
        # 这里用的是自己封装好的断言
        with allure.step("2、测试异常场景进行断言"):
            self.UI_Assert(expected, '=', test_login.wait_get_element_text(locator))
            if test_login.driver.current_url == Auto_zhuye_URL:  # 获取当前浏览器的地址跟首页地址对比
                test_login.wait_click_Element(('class name', "info"))
                test_login.wait_click_Element(("xpath", '//span[text()="退出账号"]'))
                test_login.wait_click_Element(("xpath", "/html/body/div[2]/div/div[3]/button[2]"))

if __name__ == '__main__':
    pytest.main(['test_login.py', '-vs', '--alluredir', f'{report_path}', '--clean-alluredir'])
    os.system(f'allure serve {report_path}')

