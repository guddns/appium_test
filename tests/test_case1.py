import unittest

class TestLogin(unittest.TestCase):

    def test_login_successful(self):
        print('test_login_successful' + self.driver)

    def test_login_failed(self):
        print('test_login_failed')

if __name__ == '__main__':
    unittest.main()
    