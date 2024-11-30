# freq of each elem

import array
arr = array.array("i", [1,2,4,4,5,3,1,2,3,4,5])
mydic = {}
for i in arr:
    if i not in mydic:
        mydic[i] = 1
    else: mydic[i] += 1

print(mydic)