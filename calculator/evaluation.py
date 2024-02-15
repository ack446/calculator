from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Evaluation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    
    @staticmethod    
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Evaluation(a, b, operation)

    def perform(self) -> Decimal:
        return self.operation(self.a, self.b)

    def __repr__(self):
        return f"Evaluation({self.a}, {self.b}, {self.operation.__name__})"
