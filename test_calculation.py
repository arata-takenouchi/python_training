# import unittest

import pytest

import calculation

is_release = True

class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_method(cls):
        print('end')
        del cls.cal

    def setup_method(self, method):
        print(f'method={method.__name__}')
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print(f'method={method.__name__}')
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    # @pytest.mark.skip(reason='skip')
    @pytest.mark.skipif(is_release==True, reason='skip')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
