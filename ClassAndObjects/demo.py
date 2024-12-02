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
