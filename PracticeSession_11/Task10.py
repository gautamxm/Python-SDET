# find second largest elem in array 

import array
arr1 = array.array("i", [1,2,3,12,9,10,2])
large = second = arr1[0]
for i in arr1:
    if i > large:
        second = large
        large = i
    elif large > i > second:
        second = i 
print(second)

