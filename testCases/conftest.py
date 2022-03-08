import time
import pytest
from common.basepage import BasePage



def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        print(item.name)
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='session', autouse=True)
def init_Auto():
    print('\n开始测试')
    yield
    print('\n测试结束')
    # 退出浏览器
    try:
        time.sleep(3)
        BasePage(cla=True).quit_Browser()
    except:
        print("关闭不了")
