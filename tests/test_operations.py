from decimal import Decimal
import pytest
from calculator.evaluation import Evaluation
from calculator.operations import add, subtract, multiply, divide


def test_operation_add():
    evaluation = Evaluation(Decimal('11'), Decimal('9'), add)
    assert evaluation.perform() == Decimal('19'), "Add operation failed"

def test_operation_subtract():
    evaluation = Evaluation(Decimal('5'), Decimal('5'), subtract)
    assert evaluation.perform() == Decimal('1'), "Subtract operation failed"

def test_operation_multiply():
    evaluation = Evaluation(Decimal('5'), Decimal('5'), multiply)
    assert evaluation.perform() == Decimal('25'), "Multiply operation failed"

def test_operation_divide():
    evaluation = Evaluation(Decimal('10'), Decimal('5'), divide)
    assert evaluation.perform() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        evaluation = Evaluation(Decimal('10'), Decimal('0'), divide)
        evaluation.perform()
