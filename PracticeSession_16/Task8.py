
class Transport:
    def move(self):
        print("its moving")

class Airplane(Transport):
    def move(self):
        print("Airplane is flying")

class Ship(Transport):
    def move(self):
        print("ship is swimming")

class Car(Transport):
    def move(self):
        print("the car is moving")

mode =[Airplane(),Ship(),Car()]
for trans in mode:
    trans.move()