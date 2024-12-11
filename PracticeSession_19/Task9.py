
def divide_numbers():
    try:
        num = float(input("Enter a number: "))
        divisor = float(input("Enter a divisor: "))
        result = num / divisor
        print(f"The result of division is: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numeric inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
divide_numbers()