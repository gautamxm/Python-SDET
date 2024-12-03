# Creating Class 
# class myclass:
#     def myfun(self):
#         pass
#     def greet(self):
#         print("Hello Lucifer")
#     def display(self,name,age):
#         print("Hello", name,age)

# Creating objects 
# obj1 = myclass()
# obj2 = myclass()

# obj1.myfun()
# obj1.display("Gautam",20)

# obj2.myfun()
# obj2.display("Lucifer",23)

# Static Method Creation
# class myclass:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(num):
#         print(num)  #static methods dont take an implicit self parameter

# obj = myclass()
# obj.m1()
# obj.m2(10)
# myclass.m2(20)  #static method callig without creating obj

# Variables in Python 
# class myclass:
#     a,b=10,20
#     def add(self):
#         print(self.a + self.b)
#     def mul(self):
#         print(self.a * self.b)

# mc = myclass()
# mc.add()
# mc.mul()

# All Variables
# i,j = 15,25
# class myclass:
#     a,b = 10,20
#     def add(self,x,y):  # local var
#         print(x,y)      # print local
#         print(self.a + self.b)    # instance var
#         print(i,j)      # global var

# mc = myclass()
# mc.add(10,20)

# Using same name for all variables
# i,j = 15,25
# class myclass:
#     i,j = 10,20
#     def add(self,i,j):
#         print(i,j)   # print local var
#         print(self.i + self.j)   # print instance var
#         print(globals()["i"], globals()['j'])   # print global var

# mc = myclass()
# mc.add(3,4)

# Constructors in Python 
# name is fixed def __init__(self) 
# not return any value, can recieve arg/paramter 
# called automatically at the time of object creation 

# class myclass:
#     def __init__(self):
#         print("i'm contsructor")
#     def m1(self):
#         print("i'm method of class")
# obj = myclass()
# obj.m1()  # method we have to call explicitly by using object 

# class myclass:
#     def __init__(self):
#         print("i'm constructor ")
#     def m1(self):
#         print("i'm method of class")
#         print(self)  # self contain the object reference
#     def m2(self,a,b):
#         return a+b
# obj = myclass()
# obj.m1()
# print(obj.m2(3,4))

# Parameterized Constructor 
# class myclass:
#     name = "lucifer"
#     def __init__(self,name):
#         print(name)   # paramter it is 
#         print(self.name)
# obj = myclass("gautam")

# class employee:
#     def __init__(self,eid,ename,esal):    # parametrizes const 
#         self.eid = eid                    # instance variables inside the construct/methods
#         self.ename = ename
#         self.esal = esal
#     def display(self):
#         print(self.eid, self.ename, self.esal)

# obj1 = employee(2,"gautam",3000)
# obj1.display()

# __str__() const  -- define string repesnetation only
# class myclass:
#     def __str__(self):
#         return "hello i am method"
    
# obj = myclass()
# print(obj)

# class myclass:
#     def __init__(self,eid,ename,esal):
#         self.eid = eid                    # instance variables inside the construct/methods
#         self.ename = ename
#         self.esal = esal
#     def display(self):
#         print(self.eid, self.ename, self.esal)
#     def __str__(self):
#         return self.ename

# obj = myclass(2,"gautam",6000)
# obj.display()
# print(obj)

# Delete object properties in python --del 
# we can delete the object property(also called attribute) using the del keyword 

# class car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def __str__(self):
#         return f"Brand : {self.brand}, Model: {self.model}"
    
# c = car("tata","nexon")
# print(c.brand)
# print(c.model)
# print(c)
# del c.brand
# print(c.brand)    # AttributeError: 'car' object has no attribute 'brand'

