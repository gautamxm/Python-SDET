# Write a Python function that counts the occurrences of a specific element in a tuple

def countoccur(tuple1,elm):
    count = 0
    for i in tuple1:
        if i == elm:
            count += 1
    return  count
mytuple = tuple(map(int,input("enter numbers : ").split()))
num = int(input("enter num to find its occurence : "))
res = countoccur(mytuple,num)
print(res)
