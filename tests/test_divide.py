"""Tests for the divide module."""

import unittest
from src.divide import divide


class TestDivide(unittest.TestCase):
    """Test cases for the divide function."""

    def test_divide_normal(self):
        """Test normal division."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises an appropriate error."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))

    def test_divide_negative(self):
        """Test division with negative numbers."""
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_zero_dividend(self):
        """Test dividing zero by a non-zero number."""
        self.assertEqual(divide(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
