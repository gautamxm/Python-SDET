# Find Factorial: Create a function that accepts a positive integer n and calculates the factorial of n using a loop.

n = int(input("Enter a number to find factorial : "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"Factorial of given no. is {fact}")
