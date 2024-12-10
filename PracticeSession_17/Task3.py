import math
class shape:
    def area(self):
        pass
    
class rectangle(shape):
    def __init__(self,length,breadth,height):
        self.l = length
        self.b = breadth
        self.h = height
    def area(self):
        return self.l*self.b*self.h

class circle(shape):
    def __init__(self,radius):
        self.r = radius
    def area(self):
        return math.pi * self.r**2

shapes = [
    rectangle(2,3,4),
    circle(5)
]
for i in shapes:
    print(i.area())