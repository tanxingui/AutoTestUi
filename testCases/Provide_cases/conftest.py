import pytest

from pageObjects.loginPage import Login_Page

@pytest.fixture(scope='session', autouse=False)
def init_fix():
    print('\n开始新建线索')
    test_mainpage = Login_Page().open_loginpage().login_auto('tanxingui', '1')  # 登录
    yield test_mainpage
    print('\n新建线索结束')