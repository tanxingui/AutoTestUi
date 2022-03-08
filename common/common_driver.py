from selenium import webdriver
from config.project_config import Browser, Headless_type


class Single(object):
    _instance = None  # 类变量，存储实例，允许这个类本身与子类进行访问

    def __new__(cls, *args, **kwargs):  # 类方法但没有classmethod的装饰
        if cls._instance is None:  # 如果没有实例化过
            cls._instance = super().__new__(cls)  # new一下
        return cls._instance  # 返回对象


# class Single1(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         else:
#             pass
#         return cls._instance


class CommonDriver(Single):
    driver = None

    def get_driver(self, browser_type=Browser, headless_type=Headless_type):
        if self.driver is None:
            if not headless_type:  # 如果不是等于Ture
                if browser_type == "chrome":
                    self.driver = webdriver.Chrome()
                elif browser_type == "firefox":
                    self.driver = webdriver.Firefox()
                else:
                    raise Exception(f'{browser_type}暂不支持')
            else:
                if browser_type == "chrome":
                    self.option = webdriver.ChromeOptions()
                    self.option.add_argument('--headless')
                    # 此处的参数可以是--headless或者-headless，如果是-headless，chrome是可以的
                    self.driver = webdriver.Chrome(options=self.option)
                elif browser_type == "firefox":
                    self.option = webdriver.FirefoxOptions()
                    self.option.add_argument('--headless')
                    self.driver = webdriver.Firefox(options=self.option)
                else:
                    raise Exception(f'{browser_type}暂不支持')

            self.driver.maximize_window()
            self.driver.implicitly_wait(6)
        return self.driver


if __name__ == '__main__':
    test = CommonDriver().get_driver()
