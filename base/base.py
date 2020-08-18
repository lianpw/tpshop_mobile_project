import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def find_element(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        self.find_element(loc).send_keys(value)

    # 查找toast方法
    def base_find_toast(self, message, timeout, poll):
        # message: 预期要获取的toast的部分消息
        # message = "//*[contains(@text, '" + message + "')]"
        message = "//*[contains(@text, '{}')]".format(message)
        element = self.find_element((By.XPATH, message), timeout, poll)
        return element.text

    # 判断toast是否存在
    def base_is_toast_exist(self, message, timeout=5, poll=0.1):
        try:
            res = self.base_find_toast(message, timeout=timeout, poll=poll)
            print(res)
            return True
        except Exception:
            return False

    # 截图方法
    def base_screenshot(self, screen):
        self.driver.get_screenshot_as_file('./screenshot/{}.png'.format(screen))
