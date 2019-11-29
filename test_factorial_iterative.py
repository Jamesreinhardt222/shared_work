from unittest import TestCase
from A01162209_1510_labs_v2.Lab12.timer import factorial_iterative


class TestFactorial_iterative(TestCase):
    def test_factorial_iterative_1(self):
        expected = 1
        actual = factorial_iterative(1)
        self.assertEqual(actual, expected)


    def test_factorial_iterative_10(self):
        expected = 3628800
        actual = factorial_iterative(10)
        self.assertEqual(actual, expected)
