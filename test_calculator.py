import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, -2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8, 4), 4)
        self.assertEqual(self.calc.subtract(9, -2), 11)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(7, 6), 42)
        self.assertEqual(self.calc.multiply(3, 5), 15)
    def test_divide(self):
        self.assertEqual(self.calc.divide(72, 8), 9)
        self.assertEqual(self.calc.divide(16, 3), 5)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 7), 3)
        self.assertEqual(self.calc.modulo(52, 12), 4)

if __name__ == '__main__':
    unittest.main()