# Write a Python function that finds and returns the index of all occurrences of a specified element in a list using the index() method.
# If the element is not found, return None.

def findindex(list, elm):
    index = []
    for i in range(len(list)):
        if list[i] == elm:
            index.append(i)
    if index:
        return index
    else: return  None
mylist = [1,2,3,5,2,3,5,2]
elm = 2
res = findindex(mylist,elm)
print(res)

