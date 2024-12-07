# Write a function sum_of_squares that accepts any number of arguments and returns the sum of the squares of each argument.
# Demonstrate how you would call this function with varying numbers of arguments.

def square(*args):
    return  sum(x**2 for x in args)

print(square(2,4))
print(square(2,4,6,8))
