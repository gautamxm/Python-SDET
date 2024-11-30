# Creating Lists
# myList = [1,2,3,4]
# myList2 = ["apple", "Mmango"]
# myList3 = ["apple", 3, 4, 40.6, "kiwi"]
# myList4 = list()  #Empty List
# print(myList,myList2,myList3,myList4)

# Accessing the elements of list
# myList = ["apple", "mango", "cherry"]
# print(myList[0])
# print(myList[2])
# print(myList[-1])
# print(myList[-2])


# Range of Index 
# myList = ["apple", "mango", "cherry", "kiwi", "melon"]
# print(myList[1:4])
# print(myList[2:5])
# print(myList[-4:-1])


# Change item value 
# myList = ["apple", "banana", "cherry"]
# myList[0] = "orange"
# print(myList)


# Read item list using loop 
# myList = ["apple", "banana", "cherry"]
# for i in myList:
#     print(i)

# Check if item is exist in list or not 
# myList = ["apple", "banana", "cherry"]
# print("apple" in myList)
# print("apple" not in myList)

# Length of List 
# myList = ["apple", "banana", "cherry"]
# print(len(myList))

# Adding the elements in the list 
# append() - will add at the end in the list
# insert() - will add at specific index
# myList = ["apple", "banana", "cherry"]
# myList.append("Melon")
# print(myList)
# myList.insert(2, "kiwi")
# print(myList)

# Removing the element from list 
# pop() method pass the index to remove
# myList = ["apple", "banana", "cherry"]
# myList.pop(1)
# print(myList)

# del method
# del myList
# del myList[2]

# clear() method
# myList.clear()  # items of the list will be clear

# append() method in list , 
# list1 = ["a", "b", "c"]
# list2 = [10,20,30]
# for i in list1:
#     list2.append(i)
# print(list1) 

# list1.extend(list2)
# print(list1)


# reading a list of no. from user
# a = input().split(",")
# print(a)

# a = tuple(map(int, (input().split(" "))))  #integer type list
# print(a)

# Sorting on list 
# mylist = [28,223,323,321]
# mylist1 = ["a","j", "c", "s"]
# mylist1.sort()
# print(mylist1)

# Reversing a list 
# mylist = [10,56,36]
# mylist.sort(reverse=True)
# print(mylist)

# count()
# mylist = [30,40,30,34,67,34]
# print(mylist.count(30))