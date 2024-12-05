class company:
    companyName = "BEBO"
    def __init__(self,ename, designation):
        self.ename = ename
        self.desg = designation
    def display(self):
        print(f"{self.ename} of {company.companyName} designation {self.desg}")

emp = company("Gautam", "Ambala")
emp.display()
        
    