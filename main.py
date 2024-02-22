import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_print(operand1, operand2, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        operand1_decimal, operand2_decimal = map(Decimal, [operand1, operand2])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {operand1} {operation_name} {operand2} is equal to {result(operand1_decimal, operand2_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {operand1} or {operand2} is not a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, operand1, operand2, operation = sys.argv
    calculate_and_print(operand1, operand2, operation)

if __name__ == '__main__':
    main()
