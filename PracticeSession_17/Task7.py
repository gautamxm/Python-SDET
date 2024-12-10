
class vehicle:
    def display(self):
        pass
class car(vehicle):
    def display(self):
        print("car is started")
class bike(vehicle):
    def display(self):
        print("bike is started")
c = car()
c.display()
b = bike()
b.display()