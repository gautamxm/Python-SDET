
class rectangle:
    def calculate(self,l,b):
        self.length = l
        self.breadth = b
    def display(self):
        print(2*(self.length + self.breadth))

obj = rectangle()
obj.calculate(2,3)
obj.display()