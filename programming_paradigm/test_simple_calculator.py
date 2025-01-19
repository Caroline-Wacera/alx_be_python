import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Test normal addition
        self.assertEqual(self.calc.add(-1, 1), 0)  # Test adding a negative number
        self.assertEqual(self.calc.add(0, 0), 0)  # Test adding zeros
        self.assertEqual(self.calc.add(-5, -3), -8)  # Test adding negative numbers

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Test normal subtraction
        self.assertEqual(self.calc.subtract(5, 5), 0)  # Test subtracting same numbers
        self.assertEqual(self.calc.subtract(0, 3), -3)  # Test subtracting from zero
        self.assertEqual(self.calc.subtract(-3, -5), 2)  # Test subtracting negative numbers

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Test normal multiplication
        self.assertEqual(self.calc.multiply(0, 3), 0)  # Test multiplying by zero
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Test multiplying by a negative number
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # Test multiplying two negative numbers

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)  # Test normal division
        self.assertEqual(self.calc.divide(5, 2), 2.5)  # Test division with decimal result
        self.assertEqual(self.calc.divide(0, 3), 0)  # Test dividing zero by a number
        self.assertIsNone(self.calc.divide(5, 0))  # Test dividing by zero
        
    def test_edge_cases(self):
        """Test additional edge cases."""
        self.assertEqual(self.calc.divide(1, 1), 1)  # Test dividing by one
        self.assertEqual(self.calc.add(-1, -1), -2)  # Test adding two negative numbers

if __name__ == '__main__':
    unittest.main()