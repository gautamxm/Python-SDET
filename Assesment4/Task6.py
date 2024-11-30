# symmetric diff bw two sets 
# set1 = {1,2,3,2}
# set2 = {2,3,4,5}
set1 = set(map(int,input("enter numbers : ").split()))
set2 = set(map(int,input("enter numbers : ").split()))
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

