# Write a Python function that finds all keys in a dictionary that have a specific value

dic = {"A" : 10, "B" : 20, "C" : 10, "D" : 90, "E" : 10, "F" : 10}
mylist = []
for key,value in dic.items():
    if value == 10:
        mylist.append(key)
print(mylist)


