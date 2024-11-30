# find the max and min elem in array

import array
arr = array.array("i", [1,2,7,3,4,5,8])
min = max = arr[0]
for i in arr:
    if min > i:
        min = i
    if max < i:
        max = i
print(min,max)