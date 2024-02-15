
from calculator.evaluations import Evaluations  
from calculator.operations import add, subtract, multiply, divide  
from calculator.evaluation import Evaluation  
from decimal import Decimal 
from typing import Callable  

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a evaluation and then return the result."""
        evaluation = Evaluation.create(a, b, operation)
        Evaluations.add_evaluation(evaluation)
        return evaluation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)
