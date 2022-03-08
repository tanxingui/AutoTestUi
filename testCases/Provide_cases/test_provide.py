import pytest
from utils.Auto_path import report_path


# class Test_Provide(BaseAssert):
def test_Provide(init_fix):
    test_login = init_fix
    test_provide = test_login.goto_provide()  # 去到DCC工作台的客户管理
    test_provide.Provide_page()  # 实现相关操作


if __name__ == '__main__':
    pytest.main(['test_provide.py', '-vs', '--count=2'])
