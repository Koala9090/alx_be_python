import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-10, -66), -76)
        self.assertEqual(self.calc.add(121.3, 1.4), 122.7)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-2, -4), 2)
        self.assertEqual(self.calc.subtract(9.69, 3.37), 6.3199999999999996)

      
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6, 3), 18)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 99), 0)
        self.assertEqual(self.calc.multiply(-5, -5), 25)
        self.assertEqual(self.calc.multiply(3.7, 5), 18.5)
        

    def test_division(self):
        self.assertEqual(self.calc.divide(66, 2), 33)
        self.assertEqual(self.calc.divide(-8, 4), -2)
        self.assertEqual(self.calc.divide(0, 42), 0)
        self.assertAlmostEqual(self.calc.divide(5, 4), 1.25)

    def test_devision_by_zero(self):
        self.assertEqual(self.calc.divide(9, 0),None)

if __name__ == '__main__':
    unittest.main()
