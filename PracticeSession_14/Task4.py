class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name : {self.name}, Age : {self.age}")

n1 = person("Gautam", 23)
n2 = person("Lucifer", 25)
n1.display()
n2.display()
        