# 13.	Create a function that accepts another function and two numbers as arguments and 
#       applies the passed function to the numbers.

def main(func, a, b):
    return func(a, b)

def add(x, y):
    return x + y


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(main(add, num1, num2))
