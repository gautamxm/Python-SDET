
class shape:
    def __init__(self,shape="generic"):
        self.shape = shape
    def display(self):
        print(self.shape)
obj = shape()
obj.display()