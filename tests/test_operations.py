"""
Test cases for arithmetic operations.
"""

from decimal import Decimal
import pytest
from calculator.evaluation import Evaluation
from calculator.operations import add, subtract, multiply, divide

def test_operation(operand1, operand2, operation, expected):
    '''Testing various operations'''
    evaluation = Evaluation(operand1, operand2, operation)
    assert evaluation.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    """
    Test divide by zero scenario.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        evaluation = Evaluation(Decimal('10'), Decimal('0'), divide)
        evaluation.perform()
