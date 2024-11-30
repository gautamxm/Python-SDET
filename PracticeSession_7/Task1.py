# Write a function called fizz_buzz that takes a number n as an argument and prints numbers from 1 to n. However:
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# For multiples of both 3 and 5, print "FizzBuzz" instead of the number.

n = int(input("enter a no. : "))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: 
        print(i)
        