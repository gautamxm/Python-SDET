# Write a Product class with instance attributes for name and price. Add a class method set_discount(cls, discount) to apply a discount to all products.
# Use this class method to change the price of all created products.

class Product:
    products = []
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.products.append(self)
    @classmethod
    def set_discount(cls, discount):
        for product in cls.products:
            product.price -= product.price * discount / 100
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"
product1 = Product("TV", 50000)
product2 = Product("Smartphone", 20000)
product3 = Product("Playstation", 60000)
print("Before discount:")
for product in Product.products:
    print(product)
Product.set_discount(10)
print("\nAfter 10% discount:")
for product in Product.products:
    print(product)
