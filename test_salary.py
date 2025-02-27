import unittest
from unittest.mock import  MagicMock
from unittest import mock

import salary

class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
    def test_calculation_salary_patch(self, mock_bonus):
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        # s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    def test_calculation_salary_patch_with(self):
        with mock.patch('salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            # s.bonus_api.bonus_price = MagicMock(return_value=0)
            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary_patch_with_patcher(self):
        # def f(year):
        #     return year * 2
        # self.mock_bonus.side_effect = f
        # self.mock_bonus.side_effect = lambda year: 1
        # self.mock_bonus.side_effect = ConnectionRefusedError
        self.mock_bonus.side_effect = [
            1,
            2,
            3,
            ValueError('Bankrupt!')
        ]

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 101)
        s = salary.Salary(year=2018)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 102)
        s = salary.Salary(year=2019)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 103)
        s = salary.Salary(year=200)
        with self.assertRaises(ValueError):
            s.calculation_salary()

        # self.mock_bonus.assert_called()

    @mock.patch('salary.ThirdPartyBonusRestApi', spec=True)
    def test_calculation_salary_class(self, mock_rest):
        mock_rest = mock_rest.return_value
        # mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1
        mock_rest.get_api_name.return_value = 'money'

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_rest.bonus_price.assert_called()


