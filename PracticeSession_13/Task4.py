
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def modify(self,new):
        self.marks += new
    def display(self):
        print(f"Name : {self.name}, Marks : {self.marks}")
obj = student("gautam",80)
obj.modify(10)
obj.display()

