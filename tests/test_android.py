import time
import unittest
import sys
import os
from time import sleep
import doctest

import HtmlTestRunner
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from xmlrunner import xmlrunner
from HtmlTestRunner.result import HtmlTestResult

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from pages.authorization_confirmation_page import (
    AuthorizationConfirmationPage,
    LoginPage,
)

desired_caps = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "deviceName": "emulator-5554",
    "app": "/Users/hwkim03/Downloads/3002/ectpaplutter02-release.apk",
    "appPackage": "com.cafe24.ec.plusectpaplutter02",
}

appium_server_url = "http://127.0.0.1:4723"


class CustomTestRunner(unittest.TextTestRunner):
    def __init__(self, output=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output = output

    def _makeResult(self):
        return CustomTestResult(self.output, self.descriptions, self.verbosity)


class CustomTestResult(unittest.TextTestResult):
    def __init__(self, output, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output = output

    def startTest(self, test):
        super().startTest(test)
        self.test_name = "CustomPrefix_" + test.id()

    def addSuccess(self, test):
        self.testsRun += 1
        output_message = f"{self.test_name}: PASSED\n"

        if self.output:
            with open(self.output, "a") as f:
                f.write(output_message)
        else:
            self.stream.writeln(output_message)


class TestAppium(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.longMessage = True
        self.driver = webdriver.Remote(appium_server_url, desired_caps)
        self.authorization_confirmation_page = AuthorizationConfirmationPage(
            self.driver
        )
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        """
        ############################ this
        """
        self.authorization_confirmation_page.click_confirm_button()

    # def test_02(self):
    #   wait = WebDriverWait(self.driver, 10, 5, [NoSuchElementException])
    #   if wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View'))):
    #       el1 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, '확인')))
    #       el1.click()


class CustomHtmlTestResult(HtmlTestResult):
    def addSuccess(self, test):
        """Called when a test executes successfully."""
        self._save_output_data()
        testInfo = self.infoclass(self, test)
        testInfo.id = "CustomPrefix_" + test.id()
        self._prepare_callback(testInfo, self.successes, "OK", ".")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite = doctest.DocTestSuite()
    suite.addTest(unittest.makeSuite(TestAppium))
    # runner = HtmlTestRunner.HTMLTestRunner(output='reports', report_title='테스트 리포트', resultclass=CustomHtmlTestResult)
    # runner = CustomTestRunner(output='test.results.txt')
    runner = xmlrunner.XMLTestRunner(output="reports")
    runner.run(suite)
