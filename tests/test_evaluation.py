"""
Test cases for the Evaluation class.
"""

from decimal import Decimal
import pytest
from calculator.evaluation import Evaluation
from calculator.operations import add, subtract, multiply, divide

def test_evaluation_operations(operand1, operand2, operation, expected):
    """
    Test evaluation operations.
    """
    evalu = Evaluation(operand1, operand2, operation)
    assert evalu.perform() == expected, f"Failed {operation.__name__} operation with {operand1} and {operand2}"

def test_evaluation_repr():
    """
    Test evaluation __repr__ method.
    """
    evalu = Evaluation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Evaluation(10, 5, add)"
    assert repr(evalu) == expected_repr, "The __repr__ method output does not match the expected string."


def test_divide_by_zero():
    """
    Test divide by zero scenario.
    """
    evalu = Evaluation(Decimal('10'), Decimal('0'), divide)  # Create a Calculation instance with a zero divisor.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
        evalu.perform()  # Attempt to perform the calculation, which should trigger the ValueError.
