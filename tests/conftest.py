import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        operand1 = Decimal(fake.random_number(digits=2))
        operand2 = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        
        # Ensure operand2 is not zero for divide operation to prevent division by zero in expected calculation
        if operation_func == divide:
            operand2 = Decimal('1') if operand2 == Decimal('0') else operand2
        
        try:
            if operation_func == divide and operand2 == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(operand1, operand2)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield operand1, operand2, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"operand1", "operand2", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("operand1,operand2,operation,expected", modified_parameters)
