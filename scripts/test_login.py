import os, sys
sys.path.append(os.getcwd())
from time import sleep
from base.get_driver import get_driver
from page.page_login import PageLogin
from base.read_yaml import read_yaml
import pytest
import allure


def get_data(key):
    return read_yaml('test_login.yml', key)


class TestLogin:

    def setup(self):
        self.driver = get_driver()
        self.login = PageLogin(self.driver)
        self.login.page_click_my_btn()
        self.login.page_click_login_link()

    @allure.step(title="测试登录脚本")
    @pytest.mark.parametrize('args', get_data('test_login'))
    def test_login(self, args):
        username = args.get('username')
        password = args.get('password')
        ischecked = args.get('ischecked')
        toast = args.get('toast')
        screen = args.get('screen')

        # allure.attach('输入用户名', username)
        allure.attach(username, '输入用户名')
        self.login.page_input_useranme(username)
        allure.attach(password, '输入密码')
        self.login.page_input_pwd(password)
        if ischecked:
            allure.attach('', '勾选协议')
            self.login.page_checked_agreenment()
        allure.attach('', '点击登录按钮')
        self.login.page_login_btn()
        sleep(1)
        self.login.base_screenshot(screen)
        allure.attach(toast, '断言toast')
        with open('./screenshot/{}.png'.format(screen), 'rb') as f:
            file = f.read()
            allure.attach(file, '图片', allure.attachment_type.PNG)
        assert self.login.page_is_login_with_toast(toast)

    def teardown(self):
        sleep(2)
        self.driver.quit()
