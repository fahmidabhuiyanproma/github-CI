# test_calculator.py
# Tests for our calculator module
# pytest finds and runs any file starting with "test_"

import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    """Test that addition works correctly."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    """Test that subtraction works correctly."""
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5

def test_multiply():
    """Test that multiplication works correctly."""
    assert multiply(4, 5) == 20
    assert multiply(0, 100) == 0

def test_divide():
    """Test that division works correctly."""
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0

def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError):
        divide(5, 0)
