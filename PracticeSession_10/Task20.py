# 20.	Create a function that takes a list of numbers and removes all duplicates, returning a new list.

def removedup(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    print(newlist)
mylist = [10,20,10,30,40,20,30,50,60]
removedup(mylist)
