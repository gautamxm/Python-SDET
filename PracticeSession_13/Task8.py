
class employee:
    def __init__(self,eid,ename):
        self.id = eid
        self.name = ename
    def __str__(self):
        return f"Name : {self.name}, ID : {self.id}"
obj = employee(2,"lucifer")
print(obj)