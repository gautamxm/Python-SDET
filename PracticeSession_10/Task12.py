# 12.	Write a lambda function with map to double the elements of a list.

mylist = list(map(int,input("enter numbers : ").split()))
double = list(map(lambda x: x+x,mylist))
print(double)