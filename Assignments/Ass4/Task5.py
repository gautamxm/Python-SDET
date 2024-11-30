# Write a Python code that removes the minimum and maximum values from a set

myset = {4,2,7,10,5,6,9,18}
print(myset)
min = float('inf')
max = float('-inf')
for i in myset:
    if i < min:
        min = i
    if i > max:
        max = i
myset.remove(min)
myset.remove(max)
print(myset)

