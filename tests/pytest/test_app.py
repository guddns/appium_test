# -*- coding: utf-8 -*-
import pytest

@pytest.fixture(scope='class')
def driver_init(request):
    print('################# driver_init')
    driver = 'test driver'
    request.cls.driver = driver
    yield
    print('################# driver_init yield')
    driver = None

@pytest.mark.usefixtures('driver_init')
class BasicTest:
    pass

class TestURL(BasicTest):

    def test_can_navigate_to_url(self):
        """이것은 테스트 케이스 1입니다."""
        print(self.driver)

    def test_gogogo(self):        
        print(self.driver)
        assert 1 == 2