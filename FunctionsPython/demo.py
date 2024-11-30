# user defined, built-in, lamda or anonymous
# Calling functiom 
# def myfun():
#     print("hello")
# myfun()

# parametera/arguments fxn 
# def myfun(name):
#     print("hello", name)
# myfun("gautam")

# def cal(a,b):
#     return a+b
# print(cal(10,10))
# sum = cal(2,3)
# print(sum)

# def fun():
#     return
# print(fun())  #print None

# def fun(i):
#     i=10
# print(fun(10))  #print None

# def cal(a,b):
#     print(a+b)
# cal(10,10)

# def cal(a,b):
#     return a+b
# print(cal(10,10))

# Types of functions 

# def sum(a,b):
#     return a+b
# print(sum(10,10))

# def fact(num):
#     ans = 1
#     for i in range(1,num+1):
#         ans = ans * i
#     print(ans)
# fact(4)

# Global variables and Local variable 
# gVar = 20
# def fun():
#     lVar = 10
#     print(lVar)
# print(gVar)
# # print(lVar)
# fun()

# When global and local variable have same name 
# xy = 100
# def cool():
#     xy = 200
#     print(xy)
# cool()
# print(xy)

# We want to change the value of global var inside the function 
# xy = 100
# def cool():
#     global xy
#     xy = 200
#     print(xy)
# cool()
# print(xy)

# Arguments Types 
# Positional argument
# Keyword arguments
# Default argument
# variable length argument *args
# keyword only variable length argument **kwargs

# def fun(i,j):
#     print(i,j)
# fun(10,20)  #positonal argument
# fun(i="10", j="20")  # keyword arguments
# fun(j="10", i="20")

# default value assigned to positional argument
# def fun(i, j="200"):
#     print(i,j)
# fun(100)
# fun(100,300)

# def greeting(name, msg):
#     print(msg + " " + name)
# greeting("john","hello")
# greeting(name="gautam", msg="hello")
# greeting(msg="gautam", name="hello")

# def fun(a,b,c):
#     print(a,b,c)
# fun(10,20,30)
# fun(a=10,c=30,b=20)
# fun(10,20,c=30)
# fun(10,b=20,c=30)
# fun(10,b=20,30)    #SyntaxError: positional argument follows keyword argument
# fun(10,20,b=30)      #TypeError: fun() got multiple values for argument 'b'

# return greatest of two numbers 
# def great(a,b):
#     if a > b:
#         return a
#     else: return b

# print(great(90,20))

# area of rectangle default height is 10
# def area(l,b,h=10):
#     ans = l*b*h
#     print(ans)

# area(10,20)

# to display person details using keyword arguments 
# def details(name,age, adr = "chd"):
#     print(name,age,adr)
# details(age=22, name="gautam")

# calculate final price of item with discount 
# def price(price,disc=10):
#     fprice = (disc/price) * 100
#     print(fprice)
# price(100)

# def si(p,r=2,t=5):
#     ans = p*r*t/100
#     print(ans)
# si(1000)

# Lamda function 
# has no name called anonymous fxn 

# x = lambda a: a+10
# print(x(5))
# x = lambda a,b: a*b
# print(x(2,3))
# x = lambda a,b,c: a+b+c
# print(x(1,2,3))

# list1 = [11,20,30,4,6,70]
# even = list(filter(lambda x: x%2 == 0,list1))
# print(even)

# city = ["jaipur", "kota", "chandigarh", "delhi", "muzaffarnagar"]
# def length(city):
#     return len(city)
# sort = sorted(city, key=length, reverse=True)
# print(sort)

# sort = sorted(city, key=lambda x: len(x), reverse=True)
# print(sort)

# map()
# finding square of no.
# num = [1,2,3,4]
# sq = list(map(lambda x: x*x, num))
# print(sq)

# reduce() 
# z = reduce(lambda x,y: x+y, [1,2,3,4])
# print(z)

# zip() -- will return tuple 
# join elements from two or more iterables 
# a = [10,20,30,40]
# b = [40,50,60]
# zip() -- (10,40),(20,50),(30,60)

# subjects = ["english", "hindi", "maths"]
# marks = [20,30,40]
# a = zip(subjects,marks)
# print(list(a))

# Variable arguments 
# *args --postional variable length argument  --provide flexibility when we dont know the no. of args
# **kwargs --keyword variable length argument
# allows a fun to accept any no. of positional argument, 
# which will be passed a tuple to the fun

# def greet(*name):
#     print("Hello", {name})
# greet("Lucifer")
# greet("David","John","Merry")

# def student(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
# student(name="bob", age=90)

# def displayinfo(*args, **kwargs):
#     print("positional arg", args)
#     print("keyword arg", kwargs)
# displayinfo(1,2,3,name="gautam", age=22, city="chd")

# def greet(name, *args):
#     print(name,args)
# greet("john", "david","bob", 23)

# def greet(name, *args, **kwargs):
#     print(name)
#     for i in args:
#         print(i)
#     for i,j in kwargs.items():
#         print(f"{i} : {j}")
# greet(300, "merry", "john", 23, name1="gautam", age=29)

# Factorial of number using recursion 
# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fact(num-1)
# print(fact(5))
