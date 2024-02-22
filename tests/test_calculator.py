"""
Test cases for the Calculator class.
"""

from calculator import Calculator

def test_addition():
    """
    Test addition operation.
    """
    assert Calculator.add(3, 2) == 5

def test_subtraction():
    """
    Test subtraction operation.
    """
    assert Calculator.subtract(4, 4) == 0

def test_divide():
    """
    Test divide operation.
    """
    assert Calculator.divide(6, 3) == 2

def test_multiply():
    """
    Test multiply operation.
    """
    assert Calculator.multiply(3, 3) == 9
