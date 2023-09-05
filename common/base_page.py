from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, locator)))
    