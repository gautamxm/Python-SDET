
class parent:
    def print(self):
        print("parent class")
class child(parent):
    def print(self):
        print("child class")
        

print(issubclass(child,parent))