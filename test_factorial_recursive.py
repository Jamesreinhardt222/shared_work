from unittest import TestCase
from A01162209_1510_labs_v2.Lab12.timer import factorial_recursive

class TestFactorial_recursive(TestCase):
    def test_factorial_recursive_1(self):
        expected = 1
        actual = factorial_recursive(1)
        self.assertEqual(actual, expected)


    def test_factorial_recursive_10(self):
        expected = 3628800
        actual = factorial_recursive(10)
        self.assertEqual(actual, expected)
