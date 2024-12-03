# Class variables are static variables 
class counter:
    count = 0
    def m1(self):
        counter.count += 1
        print(self.count)

a = counter()
a.m1()

b = counter()
b.m1()

c = counter()
c.m1()