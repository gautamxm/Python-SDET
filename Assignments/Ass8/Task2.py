# 2.	Create a program that accepts two numbers from the user and divides them. Handle the following exceptions:
# •	ZeroDivisionError if the divisor is zero.
# •	ValueError if the input is not a number.
# •	Any other generic exceptions.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print(f"Result of division: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")

except Exception as e:
    print(f"Unexpected error: {e}")
