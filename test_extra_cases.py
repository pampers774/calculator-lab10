"""Дополнительные пограничные случаи для divide (доп. работа)."""
import unittest

from division_case import divide


class TestDivisionExtraCases(unittest.TestCase):

    def test_negative_zero_divisor_raises(self):
        # -0.0 == 0 в Python, поэтому по контракту это тоже нулевой делитель.
        with self.assertRaises(ZeroDivisionError):
            divide(5, -0.0)

    def test_non_terminating_fraction(self):
        # 1 / 3 нельзя точно представить во float — сравниваем приближённо.
        self.assertAlmostEqual(divide(1, 3), 0.3333333, places=7)


if __name__ == "__main__":
    unittest.main()
