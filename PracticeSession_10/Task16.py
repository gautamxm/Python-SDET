# 16.	Write a function that takes a list of numbers and returns both the maximum and minimum numbers.

def minmax(list):
    min = max = list[0]
    for i in list:
        if i < min:
            min = i
        if i > max:
            max = i
    print(min,max)

list1 = [1,4,7,2,0,6,8,9]
minmax(list1)