import time
import traceback
import ddddocr
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.common_driver import CommonDriver
from utils.Auto_log import log
from utils.Auto_path import jietus_path, common_path
from utils.Auto_yaml import get_yaml_data


class BasePage:
    def __init__(self, cla=False):
        self.list_locator = []
        self.driver = CommonDriver().get_driver()
        if not cla:  # 判断是要执行用例的类，关闭浏览器等操作就不需要获取数据了
            self.locators = get_yaml_data(f'{common_path}allElements.yaml')[self.__class__.__name__]  # 取对应的类名数据
            for element_name, locator in self.locators.items():
                setattr(self, element_name, locator)  # 设置属性element_name值为locator

    def open_Url(self, url):
        self.driver.get(url)

    def get_Element(self, locator):  # 获取元素
        now_time = time.strftime('%Y%m%d %H-%M-%S')
        element = self.driver.find_element(*locator)
        if not self.list_locator:
            self.highLightElement(element)
            self.list_locator.append(element)
        else:
            self.removehighLight(self.list_locator[len(self.list_locator) - 1])  # 移除最后一个高亮的元素
            del self.list_locator[len(self.list_locator) - 1]  # 在列表中删除最后一个元素
            self.highLightElement(element)  # 把新获取到的元素进行高亮显示
            self.list_locator.append(element)
        try:
            return element
        except:
            self.driver.save_screenshot(fr'{jietus_path}\{now_time}.png')  # 定位失败输出截图
            log.error(traceback.format_exc())
            log.error('元素无法定位')

    def input_key(self, locator, text, append=False):  # 输入值
        if not append:
            self.get_Element(locator).clear()
            self.get_Element(locator).send_keys(text)
        else:
            self.get_Element(locator).send_keys(text)

    def click_element(self, locator):  # 点击
        self.get_Element(locator).click()

    def get_element_text(self, locator):  # 获取text
        return self.get_Element(locator).text

    def get_select_Element(self, locator, text):  # 下拉框定位元素
        sel = self.get_Element(locator)  # 获取下拉框元素
        sel.click()
        time.sleep(1)
        Select(sel).select_by_visible_text(text)  # 根据文本值定位
        # Select(sel).select_by_value(text)  # 根据value值定位
        # Select(sel).select_by_index(text)  # 根据索引值定位

    def wait_click_Element(self, locator):  # 显示等待后点击
        # WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(locator)).click()
        wait = WebDriverWait(self.driver, 5, 0.5)
        element = wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).click(element).perform()

    def wait_get_element_text(self, locator):  # 显示等待后获取文本值
        return WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(locator)).text

    def quit_Browser(self):  # 关闭整个浏览器
        self.driver.quit()

    def close__Browser(self):  # 关闭单个页面
        self.driver.close()

    def save_Screenshot(self):  # 截图操作
        self.driver.save_screenshot()

    def is_browser(self, url):  # 判断某个url是否加载
        return WebDriverWait(self.driver, 5, 0.5).until(EC.url_contains(url))

    def enter(self):  # 回车
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def double_click(self, locator):  # 双击
        wait = WebDriverWait(self.driver, 5, 0.5)
        element = wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).double_click(element).perform()

    def switch_to_Frame(self, locator):  # 切换iframe
        wait = WebDriverWait(self.driver, 5, 0.5)
        wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_Default(self):  # 释放iframe，重新回到主页面
        self.driver.switch_to_default_content()

    def get_Code(self, locator):  # 识别验证码
        dr_code = self.get_Element(locator)  # 获取验证码的元素位置
        # self.driver.implicitly_wait(5)
        with open('code.png', 'wb') as f:
            f.write(dr_code.screenshot_as_png)
        ocr = ddddocr.DdddOcr()  # 实例化后调用classification方法
        code = ocr.classification(dr_code.screenshot_as_png)  # 把读取的验证码赋值给code
        return code

    def highLightElement(self, locator):
        # 封装好的高亮显示页面元素的方法
        # 使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜色分别
        # 设置为绿色和红色
        """渲染元素为高亮"""
        # print('info: element highlight "{}",红色背景,绿色字体'.format(locator))
        self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                                   locator, "background:red ;border:2px solid green;")

    def removehighLight(self, locator):
        """删除高亮元素"""
        self.driver.execute_script("arguments[0].removeAttribute('style',arguments[1]);",
                                   locator, "background:red ;border:2px solid green;")


class BaseAssert:
    @classmethod  # 类方法
    def UI_Assert(cls, exp_result, condition, result):
        print("预期文本结果 >>", exp_result)
        print("实际文本结果 >>", result)
        try:
            if condition == '=':
                assert exp_result == result
            elif condition == 'in':
                assert exp_result in result
            else:
                print('条件不满足')
        except Exception as error:
            # 日志获取详细的异常信息,format_exc()返回字符串
            log.error(traceback.format_exc())
            raise error  # 抛出异常---不影响pytest 运行结果！

# if __name__ == '__main__':
#     test_page = BasePage()
#     test_page.open_Url(Auto_login_URL)
#     test_page.input_key(('name', "username"), 'tanxingui123')
#     test_page.input_key(('name', "password"), '123456')
#     test_page.input_key(('name', "captcha_text"), '123456')
#     test_page.click_Element(("css selector", "div>button>span"))
