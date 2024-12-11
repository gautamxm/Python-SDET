
mylist = list(map(int,input("enter numbers : ").split()))
index = int(input("enter the index"))

try:
    print(mylist[index])
except IndexError:
    print("index out of range")