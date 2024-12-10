
class person:
    name = "Gautam"
    def display(self):
        print(self.name)
class employee(person):
    def __init__(self, age):
        self.age = age
    def display(self):
        super().display()
        print(self.age)

obj = employee(23)
obj.display()
