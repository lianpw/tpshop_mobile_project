import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base import Base


class PageLogin(Base):

    # 我的按钮
    my_btn = By.ID, 'com.tpshop.malls:id/mine_tv'
    # 登录链接
    login_link = By.ID, 'com.tpshop.malls:id/head_img'
    # 用户名输入框
    username_input = By.ID, 'com.tpshop.malls:id/mobile_et'
    # 密码输入框
    pwd_input = By.ID, 'com.tpshop.malls:id/pwd_et'
    # 协议选择框
    agreement_check = By.ID, 'com.tpshop.malls:id/agree_btn'
    # 登录按钮
    login_btn = By.ID, 'com.tpshop.malls:id/login_tv'

    # 点击我的按钮
    def page_click_my_btn(self):
        self.base_click(self.my_btn)

    # 点击登录按钮
    def page_click_login_link(self):
        self.base_click(self.login_link)

    # 输入用户名
    def page_input_useranme(self, username):
        self.base_input(self.username_input, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(self.pwd_input, pwd)

    # 勾选协议
    def page_checked_agreenment(self):
        self.base_click(self.agreement_check)

    # 点击登录按钮
    def page_login_btn(self):
        self.base_click(self.login_btn)

    # 判断元素是否存在
    def page_is_login_with_toast(self, message):
        return self.base_is_toast_exist(message)
