# objective of inheritance - code reusablility, avoid duplicatio
# type of inherit - single, multi-level, hierachy, multiple 

# Single Inheritance 
# class A:
#     def __init__(self):
#         print("i am constructor from A")
#     def m1(self):
#         print("i am method from class A")
# class B(A):
#     def __init__(self):
#         print("i am constructor from B")
#     def m2(self):
#         print("i am method from class B")
# Bobj = B()
# Bobj.m2()
# Bobj.m1()

# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
# class B(A):
#     a,b = 100,200
#     def m2(self):
#         print(self.a + self.b)
# objB = B()
# objB.m1()
# objB.m2()

# Multi Level Inheritance 
# class A:
#     x,y = 10,20
#     def __init__(self):
#         print("i am construct of A")
#     def m1(self):
#         print(self.x + self.y)
# class B(A):
#     a,b = 100,200
#     def __init__(self):
#         print("i am construct of B")
#     def m2(self):
#         print(self.a + self.b)
# class C(B):
#     i,j = 1000,2000
#     def __init__(self):
#         print("i am construct of C")
#     def m3(self):
#         print(self.i + self.j)
# objC = C()
# objC.m1()
# objC.m2()
# objC.m3()


# Hierarchial Inheritance 
# class p1:
#     x,y = 10,20
#     def __init__(self):
#         print("i am constructor from p1")
#     def m1(self):
#         print(self.x + self.y)
# class c1(p1):
#     a,b = 100,200
#     def __init__(self):
#         print("i am constructor from c1")
#     def m2(self):
#         print(self.a + self.b)
# class c2(p1):
#     i,j = 1000,2000
#     def __init__(self):
#         print("i am constructor from p1")
#     def m3(self):
#         print(self.i + self.j)
# objc1 = c1()
# objc1.m1()
# objc1.m2()
# objc1.m3()  # AttributeError

# Multiple Inheritance - two parents one child
# class p1:
#     def print(self):
#         print("print from p1")
# class p2:
#     def __init__(self):
#         print("print from p2")
# class c1(p2,p1):
#     a = 10
#     def __init__(self):
#         print(self.a)

# obj = c1()
# obj.print()

# Method Over-riding
# class A:
#     def m1(self):
#         print("i m method from A")
# class B(A):
#     def m1(self):   # overriding
#         print("i m method from B")
#         # super().m1()   # invoke immediate parent class method
#     def print(self):
#         print("hi all")
# objB = B()
# objB.m1()

# class A:
#     name = "gautam"
# class B(A):
#     name = "lucifer"
#     def test(self):
#         print(super().name)
# obj = B()
# obj.test()

# Overriding Polymorphism
# class Bank:
#     def rateOfInterest(self):
#         return 0
# class xBank(Bank):
#     def rateOfInterest(self):
#         return 10
# class yBank(Bank):
#     def rateOfInterest(self):
#         return 20
# objx = xBank()   
# print(objx.rateOfInterest())    

# Method overloading not compeletly supported in python 
# class calculation:
#     def add(self, a=0,b=0,c=0):
#         print(a+b+c)
# cal = calculation()
# cal.add()
# cal.add(2,4)
# cal.add(2,4,9)