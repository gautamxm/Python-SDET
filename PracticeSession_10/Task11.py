# 11.	Use a lambda function with filter to extract even numbers from a list of integers.

mylist = list(map(int,input("enter numbers : ").split()))
even = list(filter(lambda x: x%2 == 0,mylist))
print(even)