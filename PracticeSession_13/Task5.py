class animal:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"Name : {self.name}")

n1 = animal("tiger")
n1.display()
n2 = animal("cheetah")
n2.display()
n3 = animal("lion")
n3.display()