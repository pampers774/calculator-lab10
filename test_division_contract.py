"""Регрессионные тесты контракта divide(a, b)."""
import unittest

from division_case import divide


class TestDivisionContract(unittest.TestCase):

    def test_integer_division(self):
        self.assertEqual(divide(8, 2), 4)

    def test_fractional_result(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_negative_dividend(self):
        self.assertEqual(divide(-6, 2), -3)

    def test_zero_dividend(self):
        self.assertEqual(divide(0, 5), 0)

    def test_nonzero_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_zero_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)


if __name__ == "__main__":
    unittest.main()
