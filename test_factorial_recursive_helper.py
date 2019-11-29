from unittest import TestCase
from A01162209_1510_labs_v2.Lab12.timer import factorial_recursive_helper

class TestFactorial_recursive_helper(TestCase):
    def test_factorial_recursive_helper(self):
        expected = 1
        actual = factorial_recursive_helper(1)
        self.assertEqual(actual, expected)

    def test_factorial_recursive_helper(self):
        expected = 3628800
        actual = factorial_recursive_helper(10)
        self.assertEqual(actual, expected)
