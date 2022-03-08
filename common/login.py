import time
import ddddocr
from selenium import webdriver

# option = webdriver.ChromeOptions()  # 禁止js的执行
# option.add_argument('headless')  # 浏览器不提供可视化页面
# driver = webdriver.Chrome(options=option)
driver = webdriver.Chrome()
driver.maximize_window()
print(driver.get_window_size())
driver.get('https://res.youcheyihou.com/test/backend/auto_buy_admin/index.html#/login')
# time.sleep(5)   #固定等待 针对一个元素定位
driver.implicitly_wait(5)  # 隐式等待 对下面所有的元素定位都生效
driver.find_element_by_name('username').send_keys('tanxingui')
driver.find_element_by_name('password').send_keys('1')
dr_code = driver.find_element_by_css_selector('img')  # 验证码的元素位置
with open('code.png', 'wb') as f:
    f.write(dr_code.screenshot_as_png)
ocr = ddddocr.DdddOcr()  # 实例化后调用classification方法
code = ocr.classification(dr_code.screenshot_as_png)  # 把读取的验证码赋值给code
time.sleep(1)
driver.find_element_by_name('captcha_text').send_keys(code)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[5]/div/button/span').click()
time.sleep(0.5)
driver.save_screenshot('jietu.png')  # 截图
driver.quit()
