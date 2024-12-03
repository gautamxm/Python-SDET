class circle:
    def area(self,radius):
        print(3.14 * radius * radius)
    def circumference(self,radius):
        print(2 * 3.14 * radius)

obj = circle()
obj.area(4)
obj.circumference(4)