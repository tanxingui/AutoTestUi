import time

from common.basepage import BasePage
from utils.Auto_faker import RandomData


class Corder_Page(BasePage):
    def Corder_page(self):
        # 点击新增订单
        time.sleep(1)
        self.wait_click_Element(self.new_corder)
        # 下拉渠道列表，随机选择
        self.click_element(self.qudao_input)
        self.wait_click_Element(self.xialakuan1_text)
        # 随机输入客户手机号
        phone = RandomData().random_mobile_phone_num()
        print(phone)
        self.input_key(self.kehuphone_input, phone)
        # 选择下订时间
        self.wait_click_Element(self.xiading_input)
        time.sleep(0.5)
        self.wait_click_Element(self.cike_button)
        # 随机生成客户名字
        name1 = RandomData().random_name()
        name = "自动化随机名字:" + name1
        print(name)
        self.input_key(self.kehu_name, name)
        # 下拉选择下订交易类型
        self.wait_click_Element(self.type_index)
        self.wait_click_Element(self.xialakuan2_text)
        # 填写定金
        self.input_key(self.dingjin, 3000)
        # 下拉选择DCC
        self.wait_click_Element(self.dcc)
        self.wait_click_Element(self.xialakuan3_text)
        # 下拉选择车型
        self.wait_click_Element(self.model_name)
        time.sleep(1)
        self.click_element(self.yiji_chexing)
        self.click_element(self.erji_chexing)
        self.click_element(self.sanji_chexing)
        time.sleep(1)
        # 随机填写下订流水号
        numb = RandomData().random_num()
        print(numb)
        self.input_key(self.xiading_numb, numb)
        # # 本地上传下订凭证图片
        # self.click_element(self.xiading_jiahao)
        # self.input_key(self.xiading_png, 'F:\原E盘内容\图片\panhu.jpg')
        # # 确认添加
        # self.click_element(self.queren_button)
