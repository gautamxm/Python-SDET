# Set is unordered collection, elements have no defined order, order cant be change
# we can not access elements by indexes
# Sets store unique elements, meaning no duplicates are allowed. if we try to add it will ignored
# Mutuable but not elements - you can add or remove elements after set is created
# however th elements themselves must be immutuable means we cant have list or dictionaries as set elements

# Unordered
# myset = {1,2,3}
# print(myset)

# Unique elements
# myset = {1,1,2,3,4}
# print(myset)

# Set are mutuable
# myset = {1,1,2,3,4}
# myset.add(5)
# print(myset)
# myset.remove(2)
# print(myset)

# myset = {1,"hello",(3,4)}
# print(myset)

# Add items in set
# add() - when we want to add only one
# update() - when we add multiple
# myset = {"apple", "cherry"}
# myset.add("mango")
# set1 = {"mango", "kiwi"}
# myset.update(set1)
# print(myset)

# remove() and discard()
# myset = {"apple", "cherry", "kiwi"}
# myset.remove("orange")  if item is not there it will give error 
# myset.discard("orange")
# print(myset)

# clear - delete the item of set
# del - delete the set

# Operations on sets
set1 = {1,2,3,2}
set2 = {2,3,4,5}
# Union()
# print(set1 | set2)
# print(set1.union(set2))  set1 will print 

# Intersection()
# print(set1 & set2)
# print(set1.intersection(set2))

# Difference()
# print(set1 - set2)
# print(set1.difference(set2))

# Symmetric diff
# print(set1 ^ set2)  #unique elemts will printed
# print(set1.symmetric_difference(set2))

# Frozenset - immutuable version of set once created we cant add or modify
# frozenset1 = frozenset([1,2,3])
# print(frozenset1)
# frozenset1.add(15)  # AttributeError: 'frozenset' object has no attribute 'add'
# print(frozenset1)

# list conversion into set --duplicate handling
# mylist = [1,2,3,3,4,4]
# myset = set(mylist)
# print(myset)