import os
import unittest
import HtmlTestRunner
import xmlrunner

class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('########## setUpClass')
        cls.driver = 'driver'

    @classmethod
    def tearDownClass(cls):
        print('########## tearDownClass')
        cls.driver = None


class TestCase1(BaseTestCase):

    def test_login_successful(self):
        """
        이것은 테스트 케이스 1입니다.
        """
        print('test_login_successful' + self.driver)

    def test_login_failed(self):
        print('test_login_failed')

class TestCase2(BaseTestCase):

    def test_login_successful(self):
        print('test_login_successful' + self.driver)

    def test_login_failed(self):
        cls.toto = 'toto'
        print('test_login_failed')

class _TestClassResult(unittest.TextTestResult):
    # ...
    def get_description(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return '\n'.join((str(test), doc_first_line))
        else:
            return str(test)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCase1))
    suite.addTest(unittest.makeSuite(TestCase2))
    # runner = HtmlTestRunner.HTMLTestRunner(output='reports', report_title='기본 테스트 리포트')
    runner = xmlrunner.XMLTestRunner(output='reports')
    runner.run(suite)
