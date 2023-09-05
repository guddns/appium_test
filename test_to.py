import xmlrunner

class CustomXMLTestRunner(xmlrunner.XMLTestRunner):
    def _make_result(self):
        # XMLTestRunner의 _make_result 메서드 오버라이드
        print('################# _make_result')
        
        result = super()._make_result()
        
        def get_test_name(test):
            # 테스트 이름을 변경하는 함수
            # 원하는 로직에 따라 새로운 이름 반환
            return "Custom Test Name"
        
        def set_test_name(result, test):
            # 결과 객체에 새로운 테스트 이름 설정
            print('################# set_test_name')
            result.test_name = get_test_name(test)
        
        setattr(result, 'set_test_name', set_test_name)
        
        return result

if __name__ == '__main__':
    import unittest
    
    # 테스트 케이스 클래스 정의
    class MyTest(unittest.TestCase):
        def test_something(self):
            # 테스트 코드 작성
            pass
    
    loader = unittest.TestLoader()
    
    suite = loader.loadTestsFromTestCase(MyTest)
    
    runner = CustomXMLTestRunner(output='reports')
    
    runner.run(suite)