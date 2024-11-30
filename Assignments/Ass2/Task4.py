# Calculate Power: Write a function that takes two integers, base and exponent, and calculates the power of base raised to exponent using a loop.

base = int(input("Enter the base : "))
exp = int(input("Enter the exponent : "))
result = 1
for i in range(abs(exp)):
    result *= base
print(result)