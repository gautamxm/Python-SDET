class employee:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
        print(f"Name : {name} of Salaray : {sal}")
    def hike(self,per):
        self.sal  += per/100 * self.sal
        print(f"Name : {self.name} of Salaray : {self.sal}")

e1 = employee(2,"Gautam", 50000)
e1.hike(10)
