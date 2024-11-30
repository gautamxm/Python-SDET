# 1. Write a Python code that takes a list of numbers as input and
# removes all occurrences of a specified number using the remove() method. Return the modified list.

mylist = list(map(int,input("enter numbers : ").split()))
num = int(input("enter number u want to remove : "))
for i in mylist:
    if i == num:
        mylist.remove(i)

print(mylist)
