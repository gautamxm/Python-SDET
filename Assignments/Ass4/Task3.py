# Write a Python code that takes a dictionary and returns the sum of all its values.

mydict = {"a" : 2, "b" : 4, "c" : 6, "d" : 9, "e" : 10, "f" : 7}
sum = 0

for value in mydict.values():
    sum += value

print(f"sum of all the values of dict : {sum}")


