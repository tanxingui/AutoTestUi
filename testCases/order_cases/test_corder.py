import pytest


def test_Provide(init_ccc):
    test_login = init_ccc
    test_provide = test_login.goto_corder()  # 去到订单管理页面
    test_provide.Corder_page()  # 实现相关操作


if __name__ == '__main__':
    pytest.main(['test_provide.py', '-vs'])