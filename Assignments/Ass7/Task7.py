# 7.	Use the abc module to create an abstract class Shape with a method area().
# Implement this class in child classes Square and Circle.
# Write a script to compute and display the areas of a square and a circle using the same method.

from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

square = Square(4)
circle = Circle(3)
print(f"Area of Square: {square.area()}")
print(f"Area of Circle: {circle.area():.2f}")
