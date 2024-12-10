
class parent:
    def __init__(self):
        print("i m constructor of parent class")
class child(parent):
    def __init__(self):
        print("i m constructor of child class")
    def m1(self):
        super().__init__()
        

obj = child()
obj.m1()