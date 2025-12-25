"""Tests for the divide module."""
import pytest

from src.divide import divide


def test_divide_positive_numbers():
    """Test division of positive numbers."""
    assert divide(10, 2) == 5.0
    assert divide(6, 3) == 2.0


def test_divide_negative_numbers():
    """Test division with negative numbers."""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_by_zero_raises_error():
    """Test that dividing by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_divide_zero_by_number():
    """Test dividing zero by a number."""
    assert divide(0, 5) == 0.0
