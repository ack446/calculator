from decimal import Decimal
import pytest
from calculator.evaluation import Evaluation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('15'), Decimal('3'), add, Decimal('18')),
    (Decimal('20'), Decimal('10'), subtract, Decimal('10')),
    (Decimal('7'), Decimal('3'), multiply, Decimal('21')),
    (Decimal('12'), Decimal('4'), divide, Decimal('3')),
    (Decimal('10.5'), Decimal('2.5'), add, Decimal('13.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('7.5'), Decimal('3'), multiply, Decimal('22.5')),
    (Decimal('12'), Decimal('2'), divide, Decimal('6')),
])
def test_evaluation_operations(a, b, operation, expected):
    eval = Evaluation(a, b, operation)
    assert eval.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_evaluation_repr():
    eval = Evaluation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Evaluation(10, 5, add)"
    assert eval.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    eval = Evaluation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        eval.perform()
