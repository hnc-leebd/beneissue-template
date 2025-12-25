"""Tests for the divide module."""

import pytest
from src.divide import divide


def test_divide_normal():
    """Test normal division."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    """Test that division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_divide_zero_dividend():
    """Test dividing zero by a number."""
    assert divide(0, 5) == 0


def test_divide_negative_numbers():
    """Test division with negative numbers."""
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5
