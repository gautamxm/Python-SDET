
class product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def update(self,val):
        self.quantity += val
        self.price *= val
    def display(self):
        print(f"Name : {self.name}, Price : {self.price}, Quantity : {self.quantity}")

        