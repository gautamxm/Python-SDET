# Write a function find_maximum that takes three numbers as parameters and returns the largest of the three.
# Demonstrate the function with an example

def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)

a = float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

largest = find_maximum(a,b,c)
print(f"The largest of the three numbers is: {largest}")
