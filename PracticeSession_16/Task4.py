
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class employee(person):
    def __init__(self,name,age,eid, salary):
        super().__init__(name,age)
        self.eid = eid
        self.sal = salary
    def display(self):
        super().display()
        print(f"ID: {self.eid}, Salary: {self.sal}")

p = person("gautam",23)
p.display()
e = employee("lucifer",24,"E123",80000)
e.display()


        