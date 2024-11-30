# 8.	Write a recursive function to find the nth Fibonacci number.

def fib(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else: return  fib(n-1) + fib(n-2)

num = int(input("enter a no. : "))
print(fib(num))