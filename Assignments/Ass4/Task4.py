# Write a Python code that converts a tuple of numbers to a list, appends a given number to the list, and
# then converts it back to a tuple.

mytuple = (1,3,4,2,3,4,2)
print(mytuple)
mylist = list(mytuple)
mylist.append(10)
mytuple = tuple(mylist)
print(mytuple)

