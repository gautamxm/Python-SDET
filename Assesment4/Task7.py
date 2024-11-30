# return the index of occurence of one element in list 
mylist = [1,2,1,3,4,2,4,1]
index = []
for i in range(0, len(mylist)):
    if mylist[i] == 1:
        index.append(i)

print(index)