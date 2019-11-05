import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_add2(self):
        result = rpn.calculate("0 0 +")
        self.assertEqual(0, result)
    def test_add3(self):
        result = rpn.calculate("12 150 +")
        self.assertEqual(162, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_subtract1(self):
        result = rpn.calculate("0 0 -")
        self.assertEqual(0, result)
    def test_subtract2(self):
        result = rpn.calculate("120 50 -")
        self.assertEqual(70, result)
    def test_subtract3(self):
        result = rpn.calculate("120 0 -")
        self.assertEqual(120, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_multiply1(self):
        result = rpn.calculate("5 0 *")
        self.assertEqual(0, result)
    def test_multiply2(self):
        result = rpn.calculate("5 20 *")
        self.assertEqual(100, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_divide1(self):
        result = rpn.calculate("0 3 /")
        self.assertEqual(0, result)
    def test_divide2(self):
        result = rpn.calculate("100 2 /")
        self.assertEqual(50, result)
    def test_pow(self):
        result = rpn.calculate("6 2 ^")
        self.assertEqual(36, result)
    def test_pow1(self):
        result = rpn.calculate("2 5 ^")
        self.assertEqual(32, result)
    def test_pow2(self):
        result = rpn.calculate("5 3 ^")
        self.assertEqual(125, result)

