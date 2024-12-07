# Create a class Product with:
# • A constructor that takes name and price.
# • A class method from_discounted_price(name, discounted_price, discount_percentage) that initializes a product based on the discounted price.
# • Demonstrate the use of both constructors.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_discounted_price(cls, name, discounted_price, discount_percentage):
        original_price = discounted_price / (1 - discount_percentage / 100)
        return cls(name, original_price)

    def __str__(self):
        return f"Product Name: {self.name}, Price: {self.price}"

product1 = Product("TV", 10000)
product2 = Product.from_discounted_price("Remote", 450, 10)

print(product1)
print(product2)

