# Extend the Car class to include a method delete_attribute(attr_name) that checks if the attribute exists before deleting it.
# Print an appropriate message if the attribute does not exist.

class Car:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f"Brand: {self.brand}, Wheels: {Car.wheels}")

    def delete_attribute(self, attr_name):
        if hasattr(self, attr_name):
            delattr(self, attr_name)
            print(f"Attribute '{attr_name}' deleted successfully.")
        else:
            print(f"Attribute '{attr_name}' does not exist.")

car1 = Car("Tata")
car1.color = "Red"
car1.show()
car1.delete_attribute("color")
car1.delete_attribute("model")
car1.show()
