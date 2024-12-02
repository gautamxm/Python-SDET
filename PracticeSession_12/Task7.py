
class employee:
    name,salary = "Gautam",50000
    def updatesalary(self,new):
        self.salary += new
    def newSalary(self):
        print(self.salary)

obj1 = employee()
obj1.updatesalary(10000)
obj1.newSalary()