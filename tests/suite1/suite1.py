import os
import unittest
from test_case1 import TestLogin

class TestSuite1(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('########## setUpClass')
        cls.driver = '############ driver'

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        cls.driver = None

    def suite_from_directory(self, directory):
        suite = unittest.TestSuite()
        for file_name in os.listdir(directory):
            if file_name.startswith('test_') and file_name.endswith('.py'):
                module_name = file_name[:-3]
                module = __import__(module_name)
                for test_case in unittest.TestLoader().loadTestsFromModule(module):
                    test_case.driver = 'gogogogogogogo'
                    suite.addTest(test_case)
        return suite

if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    test_directory = os.path.join(current_directory, '')
    suite = TestSuite1().suite_from_directory(test_directory)
    unittest.TextTestRunner().run(suite)