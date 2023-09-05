import HtmlTestRunner
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.base_page import BasePage

class AuthorizationConfirmationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    def find_confirm_button(self):
        return self.find_element('확인')
    
    def click_confirm_button(self):
        self.find_confirm_button().click()

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def find_username_field(self):
        return self.find_element('아이디')

    def find_login_button(self):
        return self.find_element('로그인')
    
    def enter_username(self, username):
        self.find_username_field().send_keys(username)

    def click_login_button(self):
        self.find_login_button().click()

