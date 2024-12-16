# Write a function safe_divide(a, b) that performs division and raises a custom exception DivisionByZeroError if b is zero.
# Demonstrate its usage with appropriate exception handling.

class DivisionByZeroError(Exception):
    def __init__(self, message="Cannot divide by zero."):
        self.message = message
        super().__init__(self.message)
def safe_divide(a, b):
    if b == 0:
        raise DivisionByZeroError()
    return a / b
try:
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))
    result = safe_divide(a, b)
    print(f"The result of {a} / {b} is: {result}")

except DivisionByZeroError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print(f"Unexpected error: {e}")