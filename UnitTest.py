import unittest

class Calculator:
    def __init__(self):
        pass
    def addition(self, a, b):
        return a + b
    def subtraction(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def division(self, a, b):
        if b != 0:
            return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_addition(self):
        self.assertEqual(self.calculator.addition(30, 1), 31)
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(54, 4), 50)
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, 5), 25)
    def test_division(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
unittest.main()
