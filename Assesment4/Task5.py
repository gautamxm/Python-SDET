# code to remove the min and max value from set 
myset = {1,2,3,7,5,6,4}
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