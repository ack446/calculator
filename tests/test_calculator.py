from calculator import Calculator

def test_addition():
    assert Calculator.add(3,2) == 5

def test_subtraction():
    assert Calculator.subtract(4,4) == 0

def test_divide():
    assert Calculator.divide(6,3) == 2

def test_multiply():
    assert Calculator.multiply(3,3) == 9
