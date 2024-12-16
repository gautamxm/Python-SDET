# 6.	Create a class Vehicle with attributes name and max_speed.
# Create a child class Car that adds an attribute num_doors.
# Write a script to create a Car object and display all its attributes.

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

class Car(Vehicle):
    def __init__(self, name, max_speed, num_doors):
        super().__init__(name, max_speed)
        self.num_doors = num_doors

car = Car("Thar", 180, 4)

print(f"Car Name: {car.name}")
print(f"Max Speed: {car.max_speed}")
print(f"Number of Doors: {car.num_doors}")
