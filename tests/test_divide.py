"""Tests for the divide module."""

import pytest
from src.divide import divide


def test_divide_positive_numbers():
    """Test division of positive numbers."""
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0
    assert divide(15, 5) == 3.0


def test_divide_negative_numbers():
    """Test division with negative numbers."""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_floats():
    """Test division of float numbers."""
    assert divide(7.5, 2.5) == 3.0
    assert divide(10.0, 4.0) == 2.5


def test_divide_by_zero_raises_error():
    """Test that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_divide_zero_by_number():
    """Test division of zero by a number."""
    assert divide(0, 5) == 0.0
    assert divide(0, -3) == 0.0
