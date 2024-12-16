# 1.	Create a polymorphic function calculate_area() that calculates the area of a Circle, Rectangle,
# and Triangle based on the shape object passed to it.

from math import pi
class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height 

    def calculate_area(self):
        return 0.5 * self.base * self.height

def calculate_area(shape):
    return shape.calculate_area()

circle = Circle(5)
rectangle = Rectangle(10, 4)
triangle = Triangle(6, 8)
print(f"Area of Circle: {calculate_area(circle):.2f}")
print(f"Area of Rectangle: {calculate_area(rectangle):.2f}")
print(f"Area of Triangle: {calculate_area(triangle):.2f}")