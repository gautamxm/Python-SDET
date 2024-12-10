import abc
from abc import ABC, abstractmethod

# class A(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     def display2(self):
#         print("hey i m display method")
# class B(A):
#     def display(self):
#         print("i m concrete of B") 
#     def display2(self):
#         print("i mdisplaying method")
# class C(B):
#     def display(self):
#         print("i m concrete of C") 
#     def display2(self):
#         print("i mdisplaying method")


# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
# class Tiger(Animal):
#     def eat(self):
#         print("eating non-veg")
# class Cow(Tiger):
#     def eat(self):
#         print("eating veg")
# t = Tiger()
# t.eat()
# c = Cow()
# c.eat()

# class shape(ABC):
#     def __init__(self,length,breadth):
#         self.l = length
#         self.b = breadth
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class reactangle(shape):
#     def area(self):
#         print(self.l * self.b)
#     def perimeter(self):
#         print(2 * self.l + self.b)

# obj = reactangle(7,8)
# obj.area()
# obj.perimeter()


# Access Specifiers 
# class private:
#     _a = 10    # protected var
#     __a = 100   # private var
#     def display(self):
#         print(self.__a)
#     def printing(self):
#         print(self.__a)



# class protected(private):
#     def display1(self):
#         print(self._a)

# obj = protected()
# obj.display()
# obj.display1()