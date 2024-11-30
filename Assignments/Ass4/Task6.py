# Return the symmetric difference of two sets.

set1 = set(map(int,input("enter numbers : ").split()))
set2 = set(map(int,input("enter numbers : ").split()))
print(set1 ^ set2)
print(set1.symmetric_difference(set2))