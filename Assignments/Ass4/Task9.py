# Write a Python function that takes two sets and returns the difference between the two sets

set1 = set(map(int,input("enter numbers : ").split()))
set2 = set(map(int,input("enter numbers : ").split()))
print(set1 - set2)
print(set1.difference(set2))