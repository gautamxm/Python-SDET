
class vehicle:
    brand = "tata"
    model = "nexon"
    def display1(self):
        print(f"Brand : {self.brand}, Model : {self.model}")

class car(vehicle):
    def display2(self,numdoor):
        print(f"Brand : {self.brand}, Model : {self.model}, doors :{numdoor}")

obj2 = car()
obj2.display1()
obj2.display2(5)
        
