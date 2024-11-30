num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Select Operation which you want to perform (+, -, *, /) : ")
if operator == "+":
    res = num1 + num2
    print(f"Result : {num1} + {num2} = {res}")
elif operator == "-":
    res = num1 - num2
    print(f"Result : {num1} - {num2} = {res}")
elif operator == "*":
    res = num1 * num2
    print(f"Result : {num1} * {num2} = {res}")
else:
    res = num1 / num2
    print(f"Result : {num1} / {num2} = {res}")