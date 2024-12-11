num1,num2 = 20,8
mylist = [1,2,3]

try:
    print(num1/num2)
    print(mylist[3])
except ZeroDivisionError:
    print("divisor cant be zero")
except IndexError:
    print("index out of range")