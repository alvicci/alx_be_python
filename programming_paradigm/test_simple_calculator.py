import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(3, 3), 0)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
    
    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
    
    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertIsNone(self.calc.divide(10, 0), None)
        # with self.assertRaises(ZeroDivisionError):
        #     self.calc.divide(10, 0)
