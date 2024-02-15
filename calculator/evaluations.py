from decimal import Decimal
from typing import Callable, List
from calculator.evaluation import Evaluation

class Evaluations:
    history: List[Evaluation] = []

    @classmethod
    def add_evaluation(cls, evaluation: Evaluation):
        cls.history.append(evaluation)

    @classmethod
    def get_history(cls) -> List[Evaluation]:
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Evaluation:
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Evaluation]:
        return [eval for eval in cls.history if eval.operation.__name__ == operation_name]
