# Reverse a Number: Write a program that takes an integer as input and outputs the reverse of that number.

n = int(input("Enter a number to reverse : "))
rev = 0
while n > 0:
    lastDigit = n % 10
    rev = (rev * 10) + lastDigit
    n = n // 10
print(f"Reverse of given number is : {rev}")