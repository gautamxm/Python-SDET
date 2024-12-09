
class Shape:
    def draw(self):
        print("The shape is drawn.")

class square(Shape):
    def draw(self):
        print("Square is drawn")

class Triangle(Shape):
    def draw(self):
        print("Triangle is drawn")

class Circle(Shape):
    def draw(self):
        print("Circle is drawn")

draw = [square(), Triangle(), Circle()]
for shape in draw:
    shape.draw()