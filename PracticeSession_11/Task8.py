# remove duplicates from array 

import array
arr = array.array("i", [1,2,3,2,5,7,2,3,1,4,5,3,6,4,5,6])
newarr = []
for i in arr:
    if i not in newarr:
        newarr.append(i)
print(newarr) 
