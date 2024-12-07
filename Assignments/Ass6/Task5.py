# Create a class Car with:
# • An instance variable brand
# • A class variable wheels initialized to 4
# • Add a method show() to print both variables.

class Car:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f"Brand: {self.brand}, Wheels: {Car.wheels}")

car1 = Car("Toyota")
car2 = Car("Honda")
car1.show()  # Output: Brand: Toyota, Wheels: 4
car2.show()  # Output: Brand: Honda, Wheels: 4
